#!/usr/bin/env python3
"""Apply the user-approved Quiz Geografia icon to Android legacy and adaptive resources."""
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "android-native" / "res"
ANDROID_RES = ROOT / "android" / "app" / "src" / "main" / "res"
MANIFEST = ROOT / "android" / "app" / "src" / "main" / "AndroidManifest.xml"

if not SOURCE.is_dir():
    raise SystemExit(f"Missing prepared Android icon resources: {SOURCE}")
if not MANIFEST.is_file():
    raise SystemExit(f"AndroidManifest.xml not found: {MANIFEST}")

ANDROID_RES.mkdir(parents=True, exist_ok=True)
for child in SOURCE.iterdir():
    target = ANDROID_RES / child.name
    if child.is_dir():
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(child, target)
    else:
        shutil.copy2(child, target)

ET.register_namespace("android", "http://schemas.android.com/apk/res/android")
tree = ET.parse(MANIFEST)
app = tree.getroot().find("application")
if app is None:
    raise SystemExit("AndroidManifest.xml has no <application> element")
ns = "{http://schemas.android.com/apk/res/android}"
app.set(ns + "icon", "@mipmap/ic_launcher")
app.set(ns + "roundIcon", "@mipmap/ic_launcher_round")
tree.write(MANIFEST, encoding="utf-8", xml_declaration=True)

required = [
    "mipmap-mdpi/ic_launcher.png",
    "mipmap-hdpi/ic_launcher.png",
    "mipmap-xhdpi/ic_launcher.png",
    "mipmap-xxhdpi/ic_launcher.png",
    "mipmap-xxxhdpi/ic_launcher.png",
    "mipmap-anydpi-v26/ic_launcher.xml",
    "mipmap-anydpi-v26/ic_launcher_round.xml",
    "drawable-nodpi/ic_launcher_foreground.png",
    "values/ic_launcher_background.xml",
]
for rel in required:
    path = ANDROID_RES / rel
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"Missing or empty Android icon resource: {path}")

manifest_text = MANIFEST.read_text(encoding="utf-8")
if 'android:icon="@mipmap/ic_launcher"' not in manifest_text:
    raise SystemExit("Manifest does not reference the approved launcher icon")
if 'android:roundIcon="@mipmap/ic_launcher_round"' not in manifest_text:
    raise SystemExit("Manifest does not reference the approved round launcher icon")

print("SUCCESS: approved Quiz Geografia icon applied to legacy and adaptive Android launcher resources.")
for rel in required:
    print(f" - {rel}")
