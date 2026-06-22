#!/usr/bin/env python3
"""
sync_drive.py
Downloads photos/videos from a public Google Drive folder and regenerates galeria.html.
No API keys or credentials required — folder must be shared as "Anyone with the link".

Usage:
  python sync_drive.py

Environment variables (optional override):
  GDRIVE_FOLDER_ID  — override the hardcoded folder ID below
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────────
GDRIVE_FOLDER_ID = os.environ.get(
    "GDRIVE_FOLDER_ID", "1YT6UrUEq01DrqlfyE_RlLrlnkZEEo6Mo"
)

VARIETIES = [
    {"key": "cacique",   "label": "CACIQUE",    "subtitle": None},
    {"key": "il1907",    "label": "IL 1907",    "subtitle": None},
    {"key": "il1908",    "label": "IL 1908",    "subtitle": None},
    {"key": "il1909",    "label": "IL 1909",    "subtitle": None},
    {"key": "jmplus",    "label": "JM PLUS",    "subtitle": None},
    {"key": "jrspecial", "label": "JR Special", "subtitle": None},
    {"key": "milan",     "label": "MILAN",      "subtitle": None},
    {"key": "sdgr21",    "label": "SDGR 21",    "subtitle": None},
    {"key": "titan",     "label": "TITAN",      "subtitle": None},
    {"key": "vulcano",   "label": "VULCANO",    "subtitle": None},
    {"key": "patron",    "label": "PATRÓN",     "subtitle": "Portainjerto"},
    {"key": "r1912",     "label": "R 1912",     "subtitle": "Portainjerto"},
]

IMAGE_EXTS = {".jpeg", ".jpg", ".png", ".webp"}
VIDEO_EXTS = {".mp4", ".mov"}

REPO_ROOT    = Path(__file__).parent
GALERIA_HTML = REPO_ROOT / "galeria.html"
GALERIA_DIR  = REPO_ROOT / "assets" / "galeria"
TMP_DIR      = Path("/tmp/drive_sync")

MARKER_START = "<!-- GALLERY-AUTO-START -->"
MARKER_END   = "<!-- GALLERY-AUTO-END -->"


# ── Drive sync ───────────────────────────────────────────────────────────────

def sync_from_drive():
    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)
    TMP_DIR.mkdir(parents=True)

    url = f"https://drive.google.com/drive/folders/{GDRIVE_FOLDER_ID}"
    print(f"⬇️  Downloading from Drive: {url}")
    result = subprocess.run(
        ["gdown", "--folder", url, "-O", str(TMP_DIR), "--fuzzy"],
        capture_output=False,
    )
    if result.returncode != 0:
        print("⚠️  gdown exited with errors (large files may have been skipped). Processing what was downloaded…")

    changed = False
    for v in VARIETIES:
        key = v["key"]
        src_dir = TMP_DIR / key
        if not src_dir.exists():
            print(f"  ⚠️  No subfolder '{key}' found in Drive — skipping")
            continue

        dst_dir = GALERIA_DIR / key
        dst_dir.mkdir(parents=True, exist_ok=True)

        # Add new images from Drive (videos are managed manually, not via Drive)
        drive_image_names = set()
        for src_file in src_dir.iterdir():
            ext = src_file.suffix.lower()
            if ext not in IMAGE_EXTS:
                continue
            drive_image_names.add(src_file.name)
            dst_file = dst_dir / src_file.name
            if not dst_file.exists():
                shutil.copy2(src_file, dst_file)
                print(f"  ✅  Added {key}/{src_file.name}")
                changed = True

        # Delete images removed from Drive (videos are never auto-deleted)
        for dst_file in dst_dir.iterdir():
            if dst_file.suffix.lower() in IMAGE_EXTS and dst_file.name not in drive_image_names:
                dst_file.unlink()
                print(f"  🗑️  Removed {key}/{dst_file.name}")
                changed = True

    shutil.rmtree(TMP_DIR)
    return changed


# ── Gallery HTML regeneration ────────────────────────────────────────────────

def make_alt(variety_label, filename):
    stem = Path(filename).stem
    stem = re.sub(r"^galeria-[a-z0-9]+-", "", stem)
    stem = re.sub(r"^video-[a-z0-9]+-?", "", stem)
    stem = stem.replace("-", " ").replace("_", " ").strip()
    return f"{variety_label} — {stem.capitalize()}" if stem else variety_label


def build_section_html(v):
    key      = v["key"]
    label    = v["label"]
    subtitle = v["subtitle"]
    local_dir = GALERIA_DIR / key

    if not local_dir.exists():
        return ""

    files  = sorted(local_dir.iterdir(), key=lambda p: (p.suffix.lower() in VIDEO_EXTS, p.name))
    images = [f for f in files if f.suffix.lower() in IMAGE_EXTS]
    videos = [f for f in files if f.suffix.lower() in VIDEO_EXTS]

    if not images and not videos:
        return ""

    parts = []
    if images:
        parts.append(f"{len(images)} {'foto' if len(images) == 1 else 'fotos'}")
    if videos:
        parts.append(f"{len(videos)} {'video' if len(videos) == 1 else 'videos'}")
    count_str = " · ".join(parts)

    h3_inner = (
        f'{label} <span style="font-size:0.7rem;color:var(--gray-3);font-weight:500;letter-spacing:0;">{subtitle}</span>'
        if subtitle else label
    )

    lines = [
        f'      <!-- {label.upper()} -->',
        f'      <div class="variety-section" data-variety="{key}">',
        f'        <div class="variety-header"><h3>{h3_inner}</h3><div class="variety-divider"></div><span class="variety-count">{count_str}</span></div>',
        f'        <div class="gallery-grid">',
    ]

    for i, img in enumerate(images):
        tall = " tall" if i == 0 else ""
        src  = f"assets/galeria/{key}/{img.name}"
        alt  = make_alt(label, img.name)
        lines.append(
            f'          <div class="g-item{tall}" onclick="abrirLightbox(this)">'
            f'<img src="{src}" alt="{alt}">'
            f'<div class="g-overlay"><i class="fa-solid fa-magnifying-glass"></i></div></div>'
        )

    for i, vid in enumerate(videos):
        tall = " tall" if i == 0 and not images else ""
        src  = f"assets/galeria/{key}/{vid.name}"
        lines.append(
            f'          <div class="g-item video-item{tall}">'
            f'<video class="g-video" autoplay muted loop playsinline>'
            f'<source src="{src}" type="video/mp4"></video>'
            f'<div class="g-overlay"><i class="fa-solid fa-play"></i></div></div>'
        )

    lines += ['        </div>', '      </div>', '']
    return "\n".join(lines)


def regenerate_gallery():
    html = GALERIA_HTML.read_text(encoding="utf-8")
    start = html.find(MARKER_START)
    end   = html.find(MARKER_END)
    if start == -1 or end == -1:
        sys.exit("❌  Markers not found in galeria.html")

    new_sections = "\n".join(build_section_html(v) for v in VARIETIES)
    new_block    = f"{MARKER_START}\n{new_sections}\n      {MARKER_END}"
    GALERIA_HTML.write_text(
        html[:start] + new_block + html[end + len(MARKER_END):],
        encoding="utf-8"
    )
    print("✅  galeria.html regenerated")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    changed = sync_from_drive()
    if changed:
        regenerate_gallery()
    else:
        print("✅  No new files — gallery is up to date")
