#!/usr/bin/env python3
"""Generate 29 Zepp weather icons from installed GNOME Adwaita SVGs.

Builds image assets, NOT a running Zepp watch face.
Dependencies: Pillow, CairoSVG, adwaita-icon-theme.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import cairosvg
import csv
import io
import os
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.getenv("ADWAITA_ICONS_ROOT", "/usr/share/icons/Adwaita/symbolic/status"))
CSV = ROOT / "assets/weather/mapeamento.csv"
OUT = ROOT / "assets/weather/png_64"
OUT.mkdir(parents=True, exist_ok=True)

with CSV.open(encoding="utf-8-sig", newline="") as f:
    mapping = list(csv.DictReader(f, delimiter=";"))
assert [int(r["code"]) for r in mapping] == list(range(29)), "Expect 0–28 in order"

def base_image(name):
    path = SOURCE / (name + "-symbolic.svg")
    if not path.exists():
        raise FileNotFoundError(f"Missing Adwaita icon: {path}")
    svg = path.read_text()
    svg = svg.replace('<svg ', '<svg style="fill:#F0F0ED" ', 1)
    svg = svg.replace("#222222", "#F0F0ED").replace("#2e3436", "#F0F0ED")
    svg = svg.replace('fill-opacity="0.34902"', 'fill-opacity="0.85"')
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=192, output_height=192)
    return Image.open(io.BytesIO(png)).convert("RGBA").resize((48, 48), Image.Resampling.LANCZOS)

for r in mapping:
    code = int(r["code"])
    im = Image.new("RGBA", (64,64), (0,0,0,0))
    im.alpha_composite(base_image(r["source"]), (8,5))
    d = ImageDraw.Draw(im)
    orange = (255,112,24,255)
    for j in range(int(r["severity"])):
        d.rounded_rectangle((22+j*7,56,26+j*7,59), radius=1, fill=orange)
    if r["overlay"] == "rain":
        for x in (47,52): d.line([(x,35),(x-3,43)], fill=orange, width=2)
    elif r["overlay"] == "hail":
        for x in (45,51): d.ellipse((x,40,x+4,44), fill=orange)
    elif r["overlay"] == "dust":
        d.arc((40,29,58,45), 35,200,fill=orange,width=2)
    elif r["overlay"] == "wind":
        d.line([(42,43),(55,43)],fill=orange,width=2)
    elif r["overlay"] == "alert":
        d.line([(51,31),(51,40)],fill=orange,width=3)
        d.ellipse((50,43,53,46),fill=orange)
    im.save(OUT / f"{code}.png",optimize=True)

sheet = Image.new("RGB", (900,726), (16,16,16))
d = ImageDraw.Draw(sheet)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
font1 = ImageFont.truetype(font_path, 16)
font2 = ImageFont.truetype(font_path, 11)
d.text((22,12), "NOMOS / WEATHER 00-28 | 64x64 RGBA",font=font1,fill=(248,248,248))
for r in mapping:
    code=int(r["code"]); x=(code%5)*180; y=(code//5)*112+54
    icon=Image.open(OUT/f"{code}.png")
    sheet.paste(icon,(x+16,y+4),icon)
    d.text((x+90,y+14),f"{code:02}",font=font1,fill=(255,112,24))
    words=r["description_ptbr"].split(); lines=[]; current=""
    for word in words:
        new=(current+" "+word).strip()
        if current and d.textlength(new,font=font2)>154:
            lines.append(current);current=word
        else: current=new
    if current: lines.append(current)
    for j,line in enumerate(lines[:2]):
        d.text((x+12,y+71+j*14),line,font=font2,fill=(185,185,185))
sheet.save(ROOT/"assets/weather/preview.png",optimize=True)

archive=ROOT/"dist/nomos-weather-29.zip"
archive.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(archive,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(OUT.glob("*.png"),key=lambda p:int(p.stem)): z.write(p,p.name)
    z.write(CSV,"mapeamento.csv")

license=Path("/usr/share/doc/adwaita-icon-theme/copyright")
if license.exists():
    target=ROOT/"docs/licenses/adwaita-debian-copyright.txt"
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(license,target)

images=list(OUT.glob("*.png"))
assert len(images)==29
assert all(Image.open(p).size==(64,64) and Image.open(p).mode=="RGBA" and Image.open(p).getextrema()[3][0]==0 for p in images)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len([p for p in z.namelist() if re.fullmatch(r"\d+\.png",p)])==29
print("ASSETS PASS: 29 PNG 64x64 RGBA, transparent alpha; ZIP integrity PASS")
