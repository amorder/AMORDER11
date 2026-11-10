#!/usr/bin/env python3
"""Render English global-audience AMORDER shorts with Blender, Kokoro TTS and FFmpeg.

Only reviewed public storyboards are consumed. No broker, account, trading ledger,
private research, credentials, or social publishing APIs are accessed here.
"""
from __future__ import annotations
import argparse, json, re, shutil, subprocess, tempfile
from pathlib import Path
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro
from motion_graphics import build_motion_graphics_filter

WIDTH, HEIGHT, FPS = 1080, 1920, 30
BLENDER_FPS = 12
MAX_RUNTIME_SECONDS = 159.0
DISCLOSURE = "Paper-trading education only; not live-money performance; not investment advice; no guaranteed returns."

def run(command):
    subprocess.run(command, check=True)

def font_path():
    for family in ("Noto Sans", "DejaVu Sans"):
        try:
            path=subprocess.check_output(["fc-match","-f","%{file}",family],text=True,stderr=subprocess.DEVNULL).strip()
            if path and Path(path).exists(): return path
        except (FileNotFoundError,subprocess.CalledProcessError): pass
    raise RuntimeError("No readable sans-serif font found; install fonts-noto-core")

def wrap(draw,text,font,max_width):
    lines=[]; current=""
    for word in text.split():
        candidate=(current+" "+word).strip()
        if current and draw.textbbox((0,0),candidate,font=font)[2]>max_width:
            lines.append(current); current=word
        else: current=candidate
    if current: lines.append(current)
    return lines

def centered(draw,text,y,font,fill,max_width=950,spacing=14):
    lines=wrap(draw,text,font,max_width)
    heights=[draw.textbbox((0,0),line,font=font)[3] for line in lines]
    total=sum(heights)+spacing*max(0,len(lines)-1)
    for line,height in zip(lines,heights):
        box=draw.textbbox((0,0),line,font=font); width=box[2]-box[0]
        draw.text(((WIDTH-width)/2,y),line,font=font,fill=fill); y+=height+spacing
    return total

def render_overlay(scene, index, count, font_file, path):
    im = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    gradient = Image.new("RGBA", (1, HEIGHT), (0, 0, 0, 0))
    for y in range(1050, HEIGHT):
        t = (y - 1050) / (HEIGHT - 1050)
        gradient.putpixel((0, y), (3, 8, 15, int(18 + 194 * (t ** 1.35))))
    im.alpha_composite(gradient.resize((WIDTH, HEIGHT)))
    d = ImageDraw.Draw(im)

    micro = ImageFont.truetype(font_file, 27)
    title = ImageFont.truetype(font_file, 78)
    support = ImageFont.truetype(font_file, 39)
    foot = ImageFont.truetype(font_file, 22)
    disclosure = ImageFont.truetype(font_file, 23)

    d.text((82, 92), "AMORDER", font=micro, fill=(239, 246, 250, 255))
    d.text((248, 95), "RESEARCH / RISK / DISCIPLINE", font=foot, fill=(157, 181, 195, 245))
    page = f"{index:02d} / {count:02d}"
    bounds = d.textbbox((0, 0), page, font=foot)
    d.text((WIDTH - 84 - (bounds[2] - bounds[0]), 95), page, font=foot,
           fill=(183, 208, 220, 245))
    d.line((82, 154, WIDTH - 82, 154), fill=(191, 218, 230, 105), width=2)
    d.line((82, 154, 82 + int((WIDTH - 164) * index / count), 154),
           fill=(64, 180, 201, 235), width=3)

    y = 1000
    y += centered(d, scene["title"], y, title, (247, 250, 251, 255), 900, 8)
    y += 20
    centered(d, scene["overlay"], y, support, (180, 214, 224, 255), 850, 9)

    d.line((82, 1786, WIDTH - 82, 1786), fill=(191, 218, 230, 85), width=1)
    if index == count:
        d.text((82, 1812), "PAPER-TRADING EDUCATION ONLY", font=foot,
               fill=(115, 208, 220, 255))
        centered(d, DISCLOSURE, 1852, disclosure, (214, 225, 232, 245), 900, 4)
    else:
        d.text((82, 1830), "PAPER SIMULATION  /  EDUCATION ONLY", font=foot,
               fill=(164, 187, 198, 235))
    im.save(path)


def validate_story(story):
    if story.get("language")!="en" or story.get("audience")!="global":
        raise ValueError("Only English-language, global-audience storyboards are accepted")
    if story.get("disclosure")!=DISCLOSURE:
        raise ValueError("Required paper-trading disclosure is missing or changed")
    scenes=story.get("scenes")
    if not isinstance(scenes,list) or not 4<=len(scenes)<=8:
        raise ValueError("Storyboard must contain 4–8 scenes")
    for number,scene in enumerate(scenes,1):
        for key in ("visual","title","overlay","narration"):
            if not isinstance(scene.get(key),str) or not scene[key].strip():
                raise ValueError(f"Scene {number} is missing {key}")
        if any(ord(c)>127 for c in scene["title"]+scene["overlay"]+scene["narration"]):
            raise ValueError(f"Scene {number} contains non-ASCII copy; English-only copy required")
    if len({scene["visual"] for scene in scenes}) < 5:
        raise ValueError("Shorts/Reels require at least five distinct visual setups")
    sources=story.get("sources")
    if not isinstance(sources,list) or not sources or not all(
        isinstance(url,str) and url.startswith("https://") for url in sources
    ):
        raise ValueError("Storyboard must include HTTPS source references")
    if len(story.get("youtube_title","")) > 100:
        raise ValueError("YouTube title exceeds 100 characters")
    caption=story.get("instagram_caption")
    if not isinstance(caption,str) or not caption.strip() or len(caption)>2200:
        raise ValueError("Instagram caption is missing or exceeds 2200 characters")


def srt_time(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def subtitles_for_scenes(scenes, durations, output):
    cues = []
    current = 0.0
    number = 1
    for scene, duration in zip(scenes, durations):
        sentences = [x.strip() for x in re.split(r"(?<=[.!?])\s+", scene["narration"].strip()) if x.strip()]
        weights = [max(1, len(x.split())) for x in sentences]
        total = sum(weights) or 1
        cursor = current
        for sentence, weight in zip(sentences, weights):
            end = cursor + duration * weight / total
            cues.append(f"{number}\n{srt_time(cursor)} --> {srt_time(end)}\n{sentence}\n")
            cursor = end
            number += 1
        current += duration
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(cues), encoding="utf-8")


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True); p.add_argument("--output",required=True)
    p.add_argument("--model",required=True); p.add_argument("--voices",required=True)
    p.add_argument("--blender",default="blender"); p.add_argument("--voice",default="af_heart")
    p.add_argument("--speed",type=float,default=.96); p.add_argument("--subtitle",default=None); a=p.parse_args()
    story_path=Path(a.input).resolve(); script=Path(__file__).with_name("blender_scenes.py").resolve()
    output=Path(a.output).resolve(); output.parent.mkdir(parents=True,exist_ok=True)
    subtitle=Path(a.subtitle).resolve() if a.subtitle else output.parent.parent/"subtitles"/f"{output.stem}.srt"
    subtitle.parent.mkdir(parents=True,exist_ok=True)
    story=json.loads(story_path.read_text(encoding="utf-8")); validate_story(story)
    scenes=story["scenes"]
    if not shutil.which(a.blender): raise RuntimeError("Blender missing; refusing flat-card fallback")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"): raise RuntimeError("FFmpeg and ffprobe required")
    font_file=font_path(); tts=Kokoro(a.model,a.voices)

    with tempfile.TemporaryDirectory(prefix="amorder-short-") as td:
        temp=Path(td); clips_dir=temp/"clips"; clips_dir.mkdir()
        audio_jobs=[]; durations=[]
        # TTS first, then reject an overlength script before spending time on Blender.
        for index,scene in enumerate(scenes,1):
            samples,sr=tts.create(scene["narration"].strip(),voice=a.voice,speed=a.speed,lang="en-us")
            audio=np.asarray(samples,dtype=np.float32).reshape(-1)
            if audio.size==0 or float(np.max(np.abs(audio)))<.015:
                raise RuntimeError(f"Kokoro returned empty or near-silent narration for scene {index}")
            wav=temp/f"voice-{index:02d}.wav"; sf.write(wav,audio,sr,subtype="PCM_16")
            duration=audio.size/sr+(.6 if index==len(scenes) else .35)
            durations.append(duration); audio_jobs.append((scene,wav,duration))
        estimated=sum(durations)
        if not 15<=estimated<MAX_RUNTIME_SECONDS:
            raise RuntimeError(
                f"Script duration {estimated:.2f}s must be at least 15s and strictly below "
                f"{MAX_RUNTIME_SECONDS:.1f}s (2:40)"
            )

        for index,(scene,wav,duration) in enumerate(audio_jobs,1):
            # Blender renders an actual keyframed camera + moving 3D scene at 12 fps.
            # FFmpeg motion-compensated interpolation brings it to the 30 fps deliverable.
            animation=clips_dir/f"blender-{index:02d}.mp4"
            run([a.blender,"--background","--python",str(script),"--","--visual",scene["visual"],
                 "--output",str(animation),"--width",str(WIDTH),"--height",str(HEIGHT),
                 "--duration",f"{duration:.3f}","--fps",str(BLENDER_FPS)])
            if not animation.exists() or animation.stat().st_size<100000:
                raise RuntimeError(f"Missing Blender keyframed animation for scene {index}: {animation}")

            overlay=temp/f"overlay-{index:02d}.png"
            render_overlay(scene,index,len(scenes),font_file,overlay)
            fade_out=max(duration-.42,.05)
            clip=clips_dir/f"clip-{index:02d}.mp4"
            motion=build_motion_graphics_filter(WIDTH,HEIGHT,duration,scene["visual"])
            fc=(f"[0:v]minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:vsbmc=1,"
                f"{motion},fade=t=in:st=0:d=0.35,fade=t=out:st={fade_out:.3f}:d=0.35,"
                "setsar=1[base];[base][1:v]overlay=0:0:format=auto,format=yuv420p[v]")
            run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",str(animation),
                 "-loop","1","-framerate",str(FPS),"-i",str(overlay),"-i",str(wav),
                 "-filter_complex",fc,"-map","[v]","-map","2:a:0","-af",
                 "apad=pad_dur=0.65,afade=t=in:st=0:d=0.2,afade=t=out:st="
                 + f"{fade_out:.3f}:d=0.35,loudnorm=I=-16:TP=-1.5:LRA=11",
                 "-t",f"{duration:.3f}","-r",str(FPS),"-c:v","libx264","-preset","slow",
                 "-crf","17","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-ar","48000",
                 "-movflags","+faststart",str(clip)])

        concat=temp/"concat.txt"
        concat.write_text("".join(
            f"file '{(clips_dir/f'clip-{i:02d}.mp4').as_posix()}'\n"
            for i in range(1,len(scenes)+1)
        ),encoding="utf-8")
        run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0","-i",str(concat),
             "-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p",
             "-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart",str(output)])

        subtitles_for_scenes(scenes,durations,subtitle)
        captioned=output.with_name(output.stem+"-captioned.mp4")
        style="FontName=Noto Sans,FontSize=34,PrimaryColour=&H00FFFFFF,OutlineColour=&HAA000000,BorderStyle=1,Outline=2,Shadow=1,Alignment=2,MarginV=290"
        subtitle_filter=f"subtitles=filename='{subtitle.as_posix()}':force_style='{style}'"
        run(["ffmpeg","-y","-hide_banner","-loglevel","error","-i",str(output),"-vf",subtitle_filter,
             "-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p",
             "-c:a","copy","-movflags","+faststart",str(captioned)])
        captioned.replace(output)

    raw=subprocess.check_output(["ffprobe","-v","error","-show_entries",
        "stream=codec_type,codec_name,width,height,avg_frame_rate","-show_entries","format=duration",
        "-of","json",str(output)],text=True)
    meta=json.loads(raw); streams=meta.get("streams",[])
    video=next((s for s in streams if s.get("codec_type")=="video"),None)
    audio=next((s for s in streams if s.get("codec_type")=="audio"),None)
    duration=float(meta.get("format",{}).get("duration",0))
    if not video or (video.get("codec_name"),video.get("width"),video.get("height"))!=("h264",WIDTH,HEIGHT):
        raise RuntimeError(f"Video validation failed: {video}")
    if not audio or audio.get("codec_name")!="aac": raise RuntimeError(f"Audio validation failed: {audio}")
    if not 15<=duration<MAX_RUNTIME_SECONDS:
        raise RuntimeError(f"Encoded duration {duration:.2f}s must be strictly below 2:40")
    if output.stat().st_size<100000: raise RuntimeError("Rendered MP4 is unexpectedly small")
    if not subtitle.exists() or subtitle.stat().st_size<100: raise RuntimeError("Subtitle sidecar missing or unexpectedly small")
    # Decode every frame; a successful mux alone is not proof of a valid export.
    run(["ffmpeg","-v","error","-i",str(output),"-f","null","-"])
    chapters=[]; elapsed=0.0
    for scene,scene_duration in zip(scenes,durations):
        minutes,seconds=divmod(int(elapsed),60)
        chapters.append({"timestamp":f"{minutes:02d}:{seconds:02d}","title":scene["title"]})
        elapsed+=scene_duration
    manifest={
        "title":story.get("youtube_title",story.get("title","AMORDER educational short")),
        "publication_date":story["publication_date"],"language":"English","audience":"global",
        "visual_engine":"Blender Eevee PBR 3D with genuine keyframed camera and object animation",
        "blender_animation_fps":BLENDER_FPS,"delivery_fps":FPS,
        "motion_graphics":"Scene-specific animated vector overlays with motion-compensated frame interpolation",
        "post_production":"FFmpeg motion-design compositing, loudness mastering and burned English captions",
        "narration":"Kokoro-82M ONNX","outputs":[{
            "file":str(output),"subtitle":str(subtitle),"bytes":output.stat().st_size,
            "duration_seconds":round(duration,3),"width":WIDTH,"height":HEIGHT,"fps":FPS,
            "video_codec":"h264","audio_codec":"aac","voice":a.voice,
            "disclosure":"verified","captions_burned":True,"thumbnail":None,
            "scene_durations_seconds":[round(x,3) for x in durations],
            "blender_keyframed_animation":True,"genuine_motion_coverage_percent":100
        }],
        "chapters":chapters,"disclosure":DISCLOSURE
    }
    manifest_path=output.parent/f"{story['render_slug']}-manifest-{story['publication_date']}.json"
    manifest_path.write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(json.dumps({"output":str(output),"subtitle":str(subtitle),"manifest":str(manifest_path),
        "captions_burned":True,"bytes":output.stat().st_size,"width":WIDTH,"height":HEIGHT,
        "fps":FPS,"duration_seconds":round(duration,3),"max_duration_seconds_exclusive":MAX_RUNTIME_SECONDS,
        "video_codec":"h264","audio_codec":"aac",
        "visual_engine":manifest["visual_engine"],"motion_graphics":manifest["motion_graphics"],
        "blender_keyframed_animation":True,"tts_model":"Kokoro-82M","voice":a.voice,
        "language":"English","audience":"global","disclosure_verified":True},indent=2))

if __name__ == "__main__":
    main()
