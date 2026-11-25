#!/usr/bin/env python3
"""Generate print-ready PNG and SVG QR files after GitHub Pages is public."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "qr_config.json"
PLACEHOLDER = "SET_PUBLIC_GITHUB_PAGES_URL_HERE"

if not CONFIG.exists():
    raise SystemExit("Missing qr_config.json. Copy qr_config.example.json and set the final public GitHub Pages URL first.")

config = json.loads(CONFIG.read_text(encoding="utf-8"))
url = str(config.get("public_url", "")).strip()
if not url.startswith("https://") or PLACEHOLDER in url:
    raise SystemExit("QR not generated: public_url must be the final public HTTPS GitHub Pages URL.")
if "localhost" in url.lower() or "127.0.0.1" in url or "0.0.0.0" in url:
    raise SystemExit("QR not generated: local development addresses are not allowed.")
if not re.fullmatch(r"https://[A-Za-z0-9.-]+(?::\d+)?(?:/[A-Za-z0-9._~!$&'()*+,;=:@%/-]*)?(?:\?[A-Za-z0-9._~!$&'()*+,;=:@%/?-]*)?(?:#[A-Za-z0-9._~!$&'()*+,;=:@%/?-]*)?", url):
    raise SystemExit("QR not generated: public_url contains unsupported characters.")

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_H
    from qrcode.image.svg import SvgPathImage
except ImportError as exc:
    raise SystemExit("Install dependencies with: python -m pip install -r requirements.txt") from exc

qr = qrcode.QRCode(version=None, error_correction=ERROR_CORRECT_H, box_size=12, border=4)
qr.add_data(url)
qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white").save(ROOT / "qr_geografico.png")
qr.make_image(image_factory=SvgPathImage, fill_color="black", back_color="white").save(ROOT / "qr_geografico.svg")
print(f"Created qr_geografico.png and qr_geografico.svg for {url}")
