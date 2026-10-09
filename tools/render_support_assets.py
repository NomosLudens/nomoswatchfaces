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
    glifo = ROOT / "assets/raar/raar_128.png"
    if glifo.exists():
        raar = Image.open(glifo).convert("RGBA").resize((120, 120))
        board.paste(raar, (40, 74), raar)
    colon = Image.open(OUT/"separators/colon_64.png")
    board.paste(colon, (260, 67), colon)
    frame = Image.open(OUT/"battery/battery_frame_67x240.png")
    board.paste(frame, (448, 56), frame)
    d.text((35, 265), "RAAR (EXISTENTE)", font=font, fill=(140,140,140))
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



# These are two independent language packs. The English directory is preserved.
# ZIP import/locale switching inside Zepp Maker is NOT verified.
PTBR_DAYS = (("SEG", "SEG"), ("TER", "TER"), ("QUA", "QUA"),
             ("QUI", "QUI"), ("SEX", "SEX"), ("SAB", "SÁB"), ("DOM", "DOM"))
PTBR_MONTHS = (("JAN", "JAN"), ("FEV", "FEV"), ("MAR", "MAR"),
               ("ABR", "ABR"), ("MAI", "MAI"), ("JUN", "JUN"),
               ("JUL", "JUL"), ("AGO", "AGO"), ("SET", "SET"),
               ("OUT", "OUT"), ("NOV", "NOV"), ("DEZ", "DEZ"))
EN_DAYS = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
EN_MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN",
             "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")


def make_ptbr_preview():
    board = Image.new("RGB", (1150, 540), (6, 6, 7))
    d = ImageDraw.Draw(board)
    font = ImageFont.truetype(FONT, 19)
    d.text((26, 24), "NOMOS FACE 01 / DATA PT-BR", font=font, fill=(230, 230, 230))
    d.text((26, 71), "DIAS DA SEMANA", font=font, fill=(255, 112, 24))
    for i, (key, _) in enumerate(PTBR_DAYS):
        im = Image.open(OUT / "date/pt-BR/weekdays" / f"{key}.png")
        im.thumbnail((150, 60))
        board.paste(im, (10 + i * 160, 112), im)
    d.text((26, 241), "MESES", font=font, fill=(255, 112, 24))
    for i, (key, _) in enumerate(PTBR_MONTHS):
        im = Image.open(OUT / "date/pt-BR/months" / f"{key}.png")
        im.thumbnail((154, 60))
        board.paste(im, (8 + i % 6 * 190, 293 + i // 6 * 80), im)
    target = OUT / "support/date-pt-BR-preview.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    board.save(target, optimize=True)


def build_locale_zip(destination, days_dir, months_dir, day_keys, month_keys):
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as z:
        for folder, keys in ((days_dir, day_keys), (months_dir, month_keys)):
            for key in keys:
                path = folder / f"{key}.png"
                assert path.is_file(), f"Missing localized asset: {path}"
                z.write(path, f"{folder.name}/{path.name}")
    with zipfile.ZipFile(destination) as z:
        assert z.testzip() is None and len(z.namelist()) == 19


def main():
    for width in (64, 96, 128): make_colon(width)
    for w, h in ((67, 240), (89, 320)): make_battery(w, h)
    for value in ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"):
        text_asset(value, OUT / "date/weekdays" / f"{value}.png")
    for value in ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"):
        text_asset(value, OUT / "date/months" / f"{value}.png")
    # Keep all 19 existing English images and add 19 independent pt-BR files.
    for key, display in PTBR_DAYS:
        text_asset(display, OUT / "date/pt-BR/weekdays" / f"{key}.png")
    for key, display in PTBR_MONTHS:
        text_asset(display, OUT / "date/pt-BR/months" / f"{key}.png")
    preview()
    make_ptbr_preview()
    pngs = [*sorted((OUT/"separators").glob("*.png")),
            *sorted((OUT/"battery").glob("*.png")),
            *sorted((OUT/"date").rglob("*.png"))]
    assert len(pngs) == 45, f"expected 45 total transparent PNG assets, got {len(pngs)}"
    en_days = OUT/"date/weekdays"
    en_months = OUT/"date/months"
    pt_days = OUT/"date/pt-BR/weekdays"
    pt_months = OUT/"date/pt-BR/months"
    for folder, expected in ((en_days, 7), (en_months, 12), (pt_days, 7), (pt_months, 12)):
        assert len(list(folder.glob("*.png"))) == expected, folder
    # Accented Saturday is rendered in the PNG but filename remains ASCII.
    assert (pt_days/"SAB.png").is_file()
    for path in pngs:
        im = Image.open(path)
        assert im.mode == "RGBA" and im.size == ((220, 72) if "date" in path.parts else im.size)
        assert im.getchannel("A").getextrema()[0] == 0, path
    (ROOT/"dist").mkdir(parents=True, exist_ok=True)
    build_locale_zip(ROOT/"dist/NOMOS_FACE_01_DATA_EN.zip",
                     en_days, en_months, EN_DAYS, EN_MONTHS)
    build_locale_zip(ROOT/"dist/NOMOS_FACE_01_DATA_PT_BR.zip",
                     pt_days, pt_months,
                     [key for key, _ in PTBR_DAYS],
                     [key for key, _ in PTBR_MONTHS])
    zp = ROOT/"dist/NOMOS_FACE_01_COMPLEMENTOS.zip"
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for path in pngs:
            z.write(path, path.relative_to(OUT))
        z.write(OUT/"support/preview.png", "support/preview.png")
        z.write(OUT/"support/date-pt-BR-preview.png", "support/date-pt-BR-preview.png")
    with zipfile.ZipFile(zp) as z:
        assert z.testzip() is None and len(z.namelist()) == 47
    print("ASSETS_PASS: 45 transparent PNGs incl. 19 EN + 19 PT-BR date assets; 2 locale ZIPs + main ZIP")
    print("NOTE: Zepp Maker locale support and physical Bip 6 flow NOT TESTED")


if __name__ == "__main__":
    main()