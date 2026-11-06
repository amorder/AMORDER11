#!/usr/bin/env python3
"""Render a public-safe AMORDER educational vertical short; no broker data or secrets."""
import argparse, json, math, shutil, subprocess, tempfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DURATION = 720, 1280, 24, 3.65
SCENES = [
    ("01  RESEARCH FIRST", "आधी डेटा तपासा", "Verify the data and sources before forming a view.", "No assumptions. No invented facts."),
    ("02  RISK BEFORE ACTION", "आधी जोखीम ठरवा", "Understand the downside before considering an order.", "Risk control is part of the process."),
    ("03  PAPER, NOT LIVE", "फक्त सिम्युलेशन", "Test the workflow with simulated orders—not real money.", "Paper trading is a process test."),
    ("04  REVIEW EVERY STEP", "प्रत्येक पायरी नोंदवा", "Journal the process and learn from each result.", "A signal is not a fill."),
    ("05  NO TRADE IS A DECISION", "व्यवहार नाही हाही निर्णय", "When the rules do not line up, do not force a trade.", "Patience is a valid outcome."),
    ("PROCESS OVER HYPE", "शिस्त • शिकणे • नोंद", "Research  •  Risk  •  Paper  •  Review", "PAPER SIMULATION  •  EDUCATION ONLY"),
]
NARRATION = ("Here's the AMORDER journey. We start with research and verify the data before acting. "
             "Then we define risk before considering an order. We test the workflow through paper "
             "simulation, not real money. Every step is reviewed and journaled. If the rules do not "
             "line up, no trade is a valid decision. Process over hype.")

def font_path():
    try:
        p = subprocess.check_output(["fc-match", "-f", "%{file}", "Noto Sans Devanagari"], text=True).strip()
        if p and Path(p).exists(): return p
    except Exception: pass
    return "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(fp, size):
    try: return ImageFont.truetype(fp, size)
    except OSError: return ImageFont.load_default()

def centered(d, text, y, f, color):
    b = d.textbbox((0, 0), text, font=f)
    d.text((max(28, (W-(b[2]-b[0]))//2), y), text, font=f, fill=color)

def frame(scene, idx, local_t, fonts):
    title, mr, body, note = scene
    im = Image.new("RGB", (W, H), (7, 16, 42)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((42, 38, 678, 100), 30, fill=(16, 31, 65), outline=(47, 69, 110), width=2)
    d.ellipse((66, 56, 92, 82), fill=(70, 174, 255))
    d.text((112, 52), "AMORDER  /  JOURNEY", font=fonts["small"], fill=(230, 240, 255))
    d.rounded_rectangle((42, 130, 678, 145), 8, fill=(27, 43, 77))
    d.rounded_rectangle((42, 130, 42+int(636*(idx+local_t)/len(SCENES)), 145), 8, fill=(67, 172, 255))
    d.rounded_rectangle((42, 220, 678, 1000), 42, fill=(11, 27, 58), outline=(47, 70, 113), width=2)
    pts = [(95+j*88, 365+int(40*math.sin(j*.9+local_t*1.8+idx))) for j in range(7)]
    d.line(pts, fill=(74, 161, 222), width=5)
    for j,(x,y) in enumerate(pts):
        r = 8 if j < int(local_t*2)+1 else 6
        d.ellipse((x-r,y-r,x+r,y+r), fill=(124,207,255))
    centered(d, title, 500, fonts["title"], (245,248,255))
    centered(d, mr, 590, fonts["marathi"], (104,202,255))
    words, lines, line = body.split(), [], ""
    for word in words:
        candidate = (line+" "+word).strip()
        if d.textbbox((0,0),candidate,font=fonts["body"])[2] > 570 and line:
            lines.append(line); line=word
        else: line=candidate
    if line: lines.append(line)
    y = 700-(len(lines)-1)*14
    for s in lines:
        centered(d,s,y,fonts["body"],(222,232,247)); y += 55
    centered(d,note,865,fonts["small"],(148,171,205))
    labels=["RESEARCH","RISK","PAPER","REVIEW"]
    for k,label in enumerate(labels):
        x=54+k*157; active=(idx==k or (idx==5 and k==3))
        d.rounded_rectangle((x,1040,x+145,1092),18,fill=(20,48,83) if active else (13,28,54),
                            outline=(75,178,255) if active else (42,58,87),width=2)
        b=d.textbbox((0,0),label,font=fonts["tiny"]); tw=b[2]-b[0]
        d.text((x+(145-tw)//2,1057),label,font=fonts["tiny"],
               fill=(145,215,255) if active else (105,126,158))
    centered(d,"PAPER SIMULATION  •  EDUCATION ONLY",1155,fonts["tiny"],(225,235,251))
    centered(d,"No live-money performance  •  No guaranteed returns",1205,fonts["tiny"],(139,158,190))
    return im

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True)
    a=ap.parse_args(); story=json.loads(Path(a.input).read_text(encoding="utf-8"))
    if story.get("topic") != "AMORDER educational paper-trading journey": raise SystemExit("Unsafe storyboard topic")
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); fp=font_path()
    fonts={"title":font(fp,43),"marathi":font(fp,34),"body":font(fp,28),"small":font(fp,22),"tiny":font(fp,18)}
    with tempfile.TemporaryDirectory(prefix="amorder-short-") as td:
        fd=Path(td)/"frames"; fd.mkdir(); n=round(DURATION*FPS); i=0
        for j,s in enumerate(SCENES):
            for k in range(n):
                frame(s,j,k/n,fonts).save(fd/f"{i:05d}.png",optimize=True); i+=1
        silent=Path(td)/"visual.mp4"
        subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",str(fd/"%05d.png"),
                        "-c:v","libx264","-preset","veryfast","-crf","25","-pix_fmt","yuv420p","-an",str(silent)],check=True)
        wav=Path(td)/"narration.wav"
        if shutil.which("espeak"):
            subprocess.run(["espeak","-v","en-us","-s","148","-w",str(wav),NARRATION],check=True)
            subprocess.run(["ffmpeg","-y","-loglevel","error","-i",str(silent),"-i",str(wav),"-map","0:v:0","-map","1:a:0",
                            "-c:v","copy","-c:a","aac","-b:a","64k","-shortest","-movflags","+faststart",str(out)],check=True)
        else: shutil.copyfile(silent,out)
    print(f"Rendered {out} ({out.stat().st_size} bytes)")

if __name__=="__main__": main()
