#!/usr/bin/env python3
"""Render English global-audience AMORDER shorts with Blender, Kokoro TTS and FFmpeg.

Only reviewed public storyboards are consumed. No broker, account, trading ledger,
private research, credentials, or social publishing APIs are accessed here.
"""
from __future__ import annotations
import argparse, json, shutil, subprocess, tempfile
from pathlib import Path
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro

WIDTH, HEIGHT, FPS = 1080, 1920, 30
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

def render_overlay(scene,index,count,font_file,path):
    im=Image.new("RGBA",(WIDTH,HEIGHT),(0,0,0,0)); d=ImageDraw.Draw(im)
    label=ImageFont.truetype(font_file,30); title=ImageFont.truetype(font_file,82)
    support=ImageFont.truetype(font_file,42); foot=ImageFont.truetype(font_file,24)
    disclosure=ImageFont.truetype(font_file,27)
    d.rounded_rectangle((66,82,1014,160),radius=36,fill=(7,21,44,218),outline=(80,148,196,150),width=2)
    d.text((100,104),"AMORDER  /  DATA DISCIPLINE",font=label,fill=(220,239,250,255))
    page=f"{index:02d} / {count:02d}"; pb=d.textbbox((0,0),page,font=label)
    d.text((970-(pb[2]-pb[0]),104),page,font=label,fill=(95,210,233,255))
    d.rounded_rectangle((86,1045,994,1052),radius=4,fill=(43,74,102,180))
    x=86+int(908*index/count)
    d.rounded_rectangle((86,1045,max(90,x),1052),radius=4,fill=(58,205,226,245))
    th=centered(d,scene["title"],1120,title,(246,250,255,255),930,12)
    centered(d,scene["overlay"],1120+th+44,support,(174,215,235,255),900,10)
    if index==count:
        d.rounded_rectangle((65,1588,1015,1818),radius=28,fill=(5,15,34,235),outline=(68,133,168,180),width=2)
        centered(d,"PAPER-TRADING EDUCATION ONLY",1622,label,(112,220,234,255),880,8)
        centered(d,DISCLOSURE,1688,disclosure,(228,237,247,255),850,10)
    else:
        d.text((88,1718),"PAPER SIMULATION  •  EDUCATION ONLY",font=foot,fill=(166,193,216,235))
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

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True); p.add_argument("--output",required=True)
    p.add_argument("--model",required=True); p.add_argument("--voices",required=True)
    p.add_argument("--blender",default="blender"); p.add_argument("--voice",default="af_heart")
    p.add_argument("--speed",type=float,default=.96); a=p.parse_args()
    story_path=Path(a.input).resolve(); script=Path(__file__).with_name("blender_scenes.py").resolve()
    output=Path(a.output).resolve(); output.parent.mkdir(parents=True,exist_ok=True)
    story=json.loads(story_path.read_text(encoding="utf-8")); validate_story(story)
    scenes=story["scenes"]
    if not shutil.which(a.blender): raise RuntimeError("Blender missing; refusing flat-card fallback")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"): raise RuntimeError("FFmpeg and ffprobe required")
    font_file=font_path(); tts=Kokoro(a.model,a.voices)

    with tempfile.TemporaryDirectory(prefix="amorder-short-") as td:
        temp=Path(td); plates=temp/"plates"; plates.mkdir()
        run([a.blender,"--background","--python",str(script),"--","--input",str(story_path),"--output-dir",str(plates)])
        clips=[]
        for index,scene in enumerate(scenes,1):
            samples,sr=tts.create(scene["narration"].strip(),voice=a.voice,speed=a.speed,lang="en-us")
            audio=np.asarray(samples,dtype=np.float32).reshape(-1)
            if audio.size==0 or float(np.max(np.abs(audio)))<.015:
                raise RuntimeError(f"Kokoro returned empty or near-silent narration for scene {index}")
            wav=temp/f"voice-{index:02d}.wav"; sf.write(wav,audio,sr,subtype="PCM_16")
            plate=plates/f"{index:02d}.png"
            if not plate.exists() or plate.stat().st_size<10000: raise RuntimeError(f"Missing Blender scene plate {plate}")
            overlay=temp/f"overlay-{index:02d}.png"; render_overlay(scene,index,len(scenes),font_file,overlay)
            duration=audio.size/sr+(.68 if index==len(scenes) else .48)
            clip=temp/f"clip-{index:02d}.mp4"; zoom="min(zoom+0.00032,1.045)"
            fc=(f"[0:v]zoompan=z='{zoom}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
                f"d=1:s={WIDTH}x{HEIGHT}:fps={FPS},setsar=1[base];"
                "[base][1:v]overlay=0:0:format=auto,format=yuv420p[v]")
            run(["ffmpeg","-y","-hide_banner","-loglevel","error",
                 "-loop","1","-framerate",str(FPS),"-i",str(plate),
                 "-loop","1","-framerate",str(FPS),"-i",str(overlay),"-i",str(wav),
                 "-filter_complex",fc,"-map","[v]","-map","2:a:0","-af",
                 "apad=pad_dur=0.75,loudnorm=I=-16:TP=-1.5:LRA=11",
                 "-t",f"{duration:.3f}","-r",str(FPS),"-c:v","libx264","-preset","medium",
                 "-crf","18","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-ar","48000",
                 "-movflags","+faststart",str(clip)])
            clips.append(clip)
        concat=temp/"concat.txt"
        concat.write_text("".join(f"file '{x.as_posix()}'\n" for x in clips),encoding="utf-8")
        run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","concat","-safe","0","-i",str(concat),
             "-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p",
             "-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart",str(output)])

    raw=subprocess.check_output(["ffprobe","-v","error","-show_entries",
        "stream=codec_type,codec_name,width,height","-show_entries","format=duration",
        "-of","json",str(output)],text=True)
    meta=json.loads(raw); streams=meta.get("streams",[])
    video=next((s for s in streams if s.get("codec_type")=="video"),None)
    audio=next((s for s in streams if s.get("codec_type")=="audio"),None)
    duration=float(meta.get("format",{}).get("duration",0))
    if not video or (video.get("codec_name"),video.get("width"),video.get("height"))!=("h264",WIDTH,HEIGHT):
        raise RuntimeError(f"Video validation failed: {video}")
    if not audio or audio.get("codec_name")!="aac": raise RuntimeError(f"Audio validation failed: {audio}")
    if not 15<=duration<=45: raise RuntimeError(f"Duration {duration:.2f}s is outside 15–45s")
    if output.stat().st_size<100000: raise RuntimeError("Rendered MP4 is unexpectedly small")
    print(json.dumps({"output":str(output),"bytes":output.stat().st_size,"width":WIDTH,"height":HEIGHT,
        "fps":FPS,"duration_seconds":round(duration,3),"video_codec":"h264","audio_codec":"aac",
        "tts_model":"Kokoro-82M","voice":a.voice,"language":"English","audience":"global",
        "disclosure_verified":True},indent=2))

if __name__=="__main__": main()
