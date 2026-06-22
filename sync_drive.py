#!/usr/bin/env python3
"""
sync_drive.py
Downloads photos/videos from Google Drive and regenerates galeria.html.

Required environment variables:
  GDRIVE_SERVICE_ACCOUNT  — full JSON of the service account key
  GDRIVE_FOLDER_ID        — ID of the root Drive folder (e.g. "Semillas DGR Galería")

Drive folder structure expected:
  📁 <root folder>/
    📁 cacique/
    📁 il1907/
    📁 il1908/
    📁 il1909/
    📁 jmplus/
    📁 jrspecial/
    📁 milan/
    📁 sdgr21/
    📁 titan/
    📁 vulcano/
    📁 patron/
    📁 r1912/
"""

import io
import json
import os
import re
import sys
from pathlib import Path

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# ── Variety config (order = display order on page) ─────────────────────────
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

GALERIA_HTML = Path(__file__).parent / "galeria.html"
GALERIA_DIR  = Path(__file__).parent / "assets" / "galeria"

MARKER_START = "<!-- GALLERY-AUTO-START -->"
MARKER_END   = "<!-- GALLERY-AUTO-END -->"


# ── Google Drive helpers ────────────────────────────────────────────────────

def build_service():
    sa_json = os.environ.get("GDRIVE_SERVICE_ACCOUNT")
    if not sa_json:
        sys.exit("❌  GDRIVE_SERVICE_ACCOUNT env var not set")
    info = json.loads(sa_json)
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=["https://www.googleapis.com/auth/drive.readonly"]
    )
    return build("drive", "v3", credentials=creds, cache_discovery=False)


def list_children(service, parent_id, mime_filter=None):
    query = f"'{parent_id}' in parents and trashed=false"
    if mime_filter:
        query += f" and mimeType='{mime_filter}'"
    results = []
    page_token = None
    while True:
        resp = service.files().list(
            q=query,
            fields="nextPageToken, files(id, name, mimeType, modifiedTime)",
            pageToken=page_token,
        ).execute()
        results.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return results


def download_file(service, file_id, dest_path: Path):
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    request = service.files().get_media(fileId=file_id)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    dest_path.write_bytes(buf.getvalue())


# ── Sync logic ──────────────────────────────────────────────────────────────

def sync_variety(service, variety_key, drive_folder_id):
    """Download all new/changed files for one variety. Returns set of local filenames."""
    local_dir = GALERIA_DIR / variety_key
    local_dir.mkdir(parents=True, exist_ok=True)

    drive_files = list_children(service, drive_folder_id)
    local_names = set()

    for f in drive_files:
        name = f["name"]
        ext = Path(name).suffix.lower()
        if ext not in IMAGE_EXTS | VIDEO_EXTS:
            continue
        local_names.add(name)
        dest = local_dir / name
        # Download only if missing or Drive version is newer
        if dest.exists():
            local_mtime = dest.stat().st_mtime
            drive_mtime = f["modifiedTime"]  # ISO string — compare lexicographically (fine for this)
            from datetime import datetime, timezone
            dt = datetime.fromisoformat(drive_mtime.replace("Z", "+00:00"))
            if local_mtime >= dt.timestamp():
                continue
        print(f"  ⬇️  {variety_key}/{name}")
        download_file(service, f["id"], dest)

    return local_names


def sync_all(root_folder_id):
    service = build_service()
    subfolders = list_children(service, root_folder_id,
                               mime_filter="application/vnd.google-apps.folder")
    folder_map = {f["name"].lower().replace(" ", ""): f["id"] for f in subfolders}

    for v in VARIETIES:
        key = v["key"]
        drive_id = folder_map.get(key)
        if not drive_id:
            print(f"  ⚠️  No Drive subfolder found for '{key}' — skipping")
            continue
        print(f"📁 Syncing {key}…")
        sync_variety(service, key, drive_id)

    print("✅  Drive sync complete")


# ── Gallery HTML generation ─────────────────────────────────────────────────

def make_alt(variety_label, filename):
    stem = Path(filename).stem
    # Remove common prefixes like "galeria-cacique-"
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

    files = sorted(local_dir.iterdir(), key=lambda p: (p.suffix.lower() in VIDEO_EXTS, p.name))
    images = [f for f in files if f.suffix.lower() in IMAGE_EXTS]
    videos = [f for f in files if f.suffix.lower() in VIDEO_EXTS]

    if not images and not videos:
        return ""

    n_img = len(images)
    n_vid = len(videos)
    parts = []
    if n_img:
        parts.append(f"{n_img} {'foto' if n_img == 1 else 'fotos'}")
    if n_vid:
        parts.append(f"{n_vid} {'video' if n_vid == 1 else 'videos'}")
    count_str = " · ".join(parts)

    if subtitle:
        h3_inner = f'{label} <span style="font-size:0.7rem;color:var(--gray-3);font-weight:500;letter-spacing:0;">{subtitle}</span>'
    else:
        h3_inner = label

    lines = []
    lines.append(f'      <!-- {label.upper()} -->')
    lines.append(f'      <div class="variety-section" data-variety="{key}">')
    lines.append(f'        <div class="variety-header"><h3>{h3_inner}</h3><div class="variety-divider"></div><span class="variety-count">{count_str}</span></div>')
    lines.append(f'        <div class="gallery-grid">')

    for i, img in enumerate(images):
        tall_class = " tall" if i == 0 else ""
        src  = f"assets/galeria/{key}/{img.name}"
        alt  = make_alt(label, img.name)
        lines.append(
            f'          <div class="g-item{tall_class}" onclick="abrirLightbox(this)">'
            f'<img src="{src}" alt="{alt}">'
            f'<div class="g-overlay"><i class="fa-solid fa-magnifying-glass"></i></div></div>'
        )

    for i, vid in enumerate(videos):
        tall_class = " tall" if i == 0 and not images else ""
        src = f"assets/galeria/{key}/{vid.name}"
        lines.append(
            f'          <div class="g-item video-item{tall_class}">'
            f'<video class="g-video" autoplay muted loop playsinline>'
            f'<source src="{src}" type="video/mp4"></video>'
            f'<div class="g-overlay"><i class="fa-solid fa-play"></i></div></div>'
        )

    lines.append(f'        </div>')
    lines.append(f'      </div>')
    lines.append('')
    return "\n".join(lines)


def regenerate_gallery():
    html = GALERIA_HTML.read_text(encoding="utf-8")

    start_idx = html.find(MARKER_START)
    end_idx   = html.find(MARKER_END)
    if start_idx == -1 or end_idx == -1:
        sys.exit("❌  Markers not found in galeria.html")

    new_sections = "\n".join(build_section_html(v) for v in VARIETIES)
    new_block = f"{MARKER_START}\n{new_sections}\n      {MARKER_END}"

    new_html = html[:start_idx] + new_block + html[end_idx + len(MARKER_END):]
    GALERIA_HTML.write_text(new_html, encoding="utf-8")
    print("✅  galeria.html regenerated")


# ── Entry point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    folder_id = os.environ.get("GDRIVE_FOLDER_ID")
    if not folder_id:
        sys.exit("❌  GDRIVE_FOLDER_ID env var not set")

    sync_all(folder_id)
    regenerate_gallery()
