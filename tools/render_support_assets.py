#!/usr/bin/env python3
"""Render NOMOS FACE 01 support assets; rendering is not a Zepp hardware test."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
ORANGE = (255, 112, 24, 255)
GRAY = (119, 119, 124, 255)
WHITE = (205, 205, 208, 255)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def save(img, dest):
    dest.parent.mkdir(parents=True, exist_ok=True)
    assert img.mode == "RGBA" and img.getchannel("A").getextrema()[0] == 0
    img.save(dest, optimize=True)


def make_colon(width):
    height = 2 * width
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    r = int(width * 0.21)
    for cy in (round(height * 0.30), round(height * 0.70)):
        draw.ellipse((width // 2 - r, cy - r, width // 2 + r, cy + r), fill=ORANGE)
    # Both points are required. A previous rendering had only the first dot.
    a = img.getchannel("A")
    assert a.getpixel((width // 2, round(height * 0.30))) == 255
    assert a.getpixel((width // 2, round(height * 0.70))) == 255
    assert a.getpixel((width // 2, height // 2)) == 0
    save(img, OUT / "separators" / f"colon_{width}.png")


def make_battery(width, height):
    m, stroke = max(3, round(width * .09)), max(2, round(width * .045))
    inner = m + stroke + 3
    frame = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(frame).rounded_rectangle((m, m, width-m-1, height-m-1), radius=6,
                                            outline=WHITE, width=stroke)
    save(frame, OUT / "battery" / f"battery_frame_{width}x{height}.png")
    fill = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ImageDraw.Draw(fill).rectangle((inner, inner, width-inner-1, height-inner-1), fill=ORANGE)
    save(fill, OUT / "battery" / f"battery_fill_full_{width}x{height}.png")


def text_asset(label, destination):
    w, h = 220, 72
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, 39)
    advance = [draw.textlength(c, font=font) for c in label]
    tracking = 9
    total = sum(advance) + tracking * (len(label)-1)
    x = (w-total)/2
    for c, step in zip(label, advance):
        draw.text((round(x), 5), c, font=font, fill=GRAY)
        x += step + tracking
    save(img, destination)


def preview():
    board = Image.new("RGB", (1180, 700), (6, 6, 7))
    d = ImageDraw.Draw(board)
    font = ImageFont.truetype(FONT, 19)
    d.text((28, 16), "NOMOS FACE 01 / COMPLEMENTOS", font=font, fill=(238,238,238))
    glifo = ROOT / "assets/har/har_128.png"
    if glifo.exists():
        har = Image.open(glifo).convert("RGBA").resize((120, 120))
        board.paste(har, (40, 74), har)
    colon = Image.open(OUT/"separators/colon_64.png")
    board.paste(colon, (260, 67), colon)
    frame = Image.open(OUT/"battery/battery_frame_67x240.png")
    board.paste(frame, (448, 56), frame)
    d.text((35, 265), "HAR (EXISTENTE)", font=font, fill=(140,140,140))
    d.text((260, 265), "DOIS PONTOS", font=font, fill=(140,140,140))
    d.text((448, 315), "BATERIA - MOLDURA", font=font, fill=(140,140,140))
    d.text((28, 380), "SEMANA / CANDIDATO", font=font, fill=(190,190,190))
    for i, txt in enumerate(["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]):
        a = Image.open(OUT/"date/weekdays"/f"{txt}.png")
        a.thumbnail((155, 60))
        x = 8 + i*165
        board.paste(a, (x, 420), a)
    d.text((28, 505), "MESES / CANDIDATO", font=font, fill=(190,190,190))
    for i, txt in enumerate(["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]):
        a = Image.open(OUT/"date/months"/f"{txt}.png")
        a.thumbnail((155, 60))
        board.paste(a, (8 + (i%6)*190, 544 + (i//6)*75), a)
    (OUT/"support").mkdir(parents=True, exist_ok=True)
    board.save(OUT/"support/preview.png", optimize=True)


def main():
    for width in (64, 96, 128): make_colon(width)
    for w, h in ((67, 240), (89, 320)): make_battery(w, h)
    for value in ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"):
        text_asset(value, OUT / "date/weekdays" / f"{value}.png")
    for value in ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"):
        text_asset(value, OUT / "date/months" / f"{value}.png")
    preview()
    pngs = [*sorted((OUT/"separators").glob("*.png")),
            *sorted((OUT/"battery").glob("*.png")),
            *sorted((OUT/"date").rglob("*.png"))]
    assert len(pngs) == 26, f"expected 26 support assets, got {len(pngs)}"
    assert len([p for p in pngs if p.parent.name == "weekdays"]) == 7
    assert len([p for p in pngs if p.parent.name == "months"]) == 12
    for path in pngs:
        im = Image.open(path)
        assert im.mode == "RGBA" and im.getchannel("A").getextrema()[0] == 0, path
    (ROOT/"dist").mkdir(parents=True, exist_ok=True)
    zp = ROOT/"dist/NOMOS_FACE_01_COMPLEMENTOS.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for path in pngs:
            z.write(path, path.relative_to(OUT))
        z.write(OUT/"support/preview.png", "support/preview.png")
    with zipfile.ZipFile(zp) as z:
        assert z.testzip() is None and len(z.namelist()) == 27
    print("ASSETS_PASS: 26 transparent PNGs + preview + ZIP")
    print("NOTE: Zepp Maker binding and physical Bip 6 flow NOT TESTED")


if __name__ == "__main__":
    main()