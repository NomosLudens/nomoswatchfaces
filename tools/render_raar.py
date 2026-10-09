#!/usr/bin/env python3
"""Render the exact RAAR silhouette from its verified SVG, on transparent PNG canvases."""
from pathlib import Path
import re
import io
from PIL import Image
import cairosvg
root = Path(__file__).resolve().parents[1]
source = root / "assets/raar/raar.svg"
svg = source.read_text(encoding="utf-8")
assert svg.count("<path ") == 3, "RAAR must retain three source shapes"
# Crop only outer empty margins. Do NOT alter any original path or geometry.
cropped = re.sub(r'viewBox="[^"]+"', 'viewBox="188 182 878 878"', svg, count=1)
for size in (64, 128, 256, 390):
    filename = root / f"assets/raar/raar_{size}.png"
    pixels = cairosvg.svg2png(bytestring=cropped.encode(), output_width=size, output_height=size)
    image = Image.open(io.BytesIO(pixels)).convert("RGBA")
    assert image.getextrema()[3][0] == 0, "Transparent background required"
    image.save(filename, optimize=True)
    print(f"Rendered {filename.name}: {size}x{size} RGBA")
