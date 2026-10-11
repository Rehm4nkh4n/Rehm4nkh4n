#!/usr/bin/env python3
"""Embed the supplied profile portrait into the profile SVG assets.

Expected layout:
  repository-root/
    IdMain.jpeg              # supplied portrait (JPEG or PNG is also accepted)
    right_pointing.png       # optional portrait for connect.svg
    assets/hero.svg
    assets/id-dashboard.svg
    assets/connect.svg       # optional
    scripts/embed_images.py

Run from any directory with: python scripts/embed_images.py
The script writes self-contained SVGs (no external image URLs).
"""
from __future__ import annotations

import base64
import mimetypes
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

# Prefer the exact filename supplied by the user, then support common variants.
PORTRAIT_CANDIDATES = ("IdMain.jpeg", "IdMain.jpg", "id.png", "id.jpg", "id.jpeg")
CONNECT_CANDIDATES = ("right_pointing.png", "right_pointing.jpg", "right_pointing.jpeg")


def find_first_existing(names: tuple[str, ...]) -> Path | None:
    return next((ROOT / name for name in names if (ROOT / name).is_file()), None)


def data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    if mime not in {"image/png", "image/jpeg", "image/webp", "image/gif"}:
        raise ValueError(f"Unsupported image type for {path.name}: {mime or 'unknown'}")
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def replace_first_image_href(svg_text: str, uri: str) -> str:
    """Replace the href of the first SVG image while preserving its geometry."""
    pattern = re.compile(r'(<image\b[^>]*?\bhref=")[^"]*(")', re.DOTALL)
    updated, count = pattern.subn(lambda m: m.group(1) + uri + m.group(2), svg_text, count=1)
    if count == 0:
        raise ValueError("No <image href=...> element found in SVG")
    return updated


def embed_portrait(path: Path, image: Path) -> None:
    svg_text = path.read_text(encoding="utf-8")
    svg_text = replace_first_image_href(svg_text, data_uri(image))
    path.write_text(svg_text, encoding="utf-8")
    print(f"Embedded {image.name} -> {path.relative_to(ROOT)}")


def main() -> None:
    if not ASSETS.is_dir():
        raise SystemExit(f"Assets folder not found: {ASSETS}")

    portrait = find_first_existing(PORTRAIT_CANDIDATES)
    if portrait is None:
        expected = ", ".join(PORTRAIT_CANDIDATES)
        raise SystemExit(f"Portrait image not found in repository root. Expected one of: {expected}")

    for name in ("hero.svg", "id-dashboard.svg"):
        svg_path = ASSETS / name
        if not svg_path.is_file():
            print(f"Skipping missing file: {svg_path.relative_to(ROOT)}")
            continue
        embed_portrait(svg_path, portrait)

    connect_svg = ASSETS / "connect.svg"
    connect_image = find_first_existing(CONNECT_CANDIDATES)
    if connect_svg.is_file() and connect_image is not None:
        embed_portrait(connect_svg, connect_image)
    elif connect_svg.is_file():
        print("Skipped connect.svg: optional right_pointing image not found.")

    print("Done. SVG images are embedded; no external image URLs are required.")


if __name__ == "__main__":
    main()
