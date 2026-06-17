"""
Genera el catálogo PDF de Semillas DGR S.A.
Una página por variedad con 5 fotos, diseño profesional negro/rojo/blanco.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import os

# ── COLORES ──
NEGRO      = colors.HexColor("#0a0a0a")
SURFACE2   = colors.HexColor("#181818")
SURFACE3   = colors.HexColor("#1f1f1f")
ROJO       = colors.HexColor("#cc2222")
BLANCO     = colors.HexColor("#ffffff")
GRIS       = colors.HexColor("#888888")
GRIS3      = colors.HexColor("#444444")
VERDE      = colors.HexColor("#5eba45")
VERDE_BG   = colors.HexColor("#0e2009")

W, H = A4  # 595 x 842 pt  (210 x 297 mm)

BASE  = "/Users/lucianacastillo/Desktop/Claude Code/assets/catalogo"
OUTPUT = "/Users/lucianacastillo/Desktop/Claude Code/Catalogo_Semillas_DGR.pdf"
LOGO   = "/Users/lucianacastillo/Desktop/Claude Code/assets/logo-dark.jpeg"
BHN    = "/Users/lucianacastillo/Desktop/Claude Code/assets/bhn-seed.png"

def foto(variedad_dir, filename):
    return os.path.join(BASE, variedad_dir, filename)

# ── DATOS DE VARIEDADES ──
VARIEDADES = [
    {
        "nombre": "CACIQUE",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Variedad indeterminada con alta carga de frutos por planta. Excelente adaptación "
            "a condiciones tropicales con producción uniforme y consistente. Fruto firme con "
            "buena vida poscosecha."
        ),
        "specs": [
            ("Porte",          "Indeterminado"),
            ("Vida poscosecha","Larga"),
        ],
        "resistencias": ["V", "F1", "F2", "F3"],
        "bhn": True,
        "fotos": [
            foto("CACIQUE", "WhatsApp Image 2026-06-16 at 10.37.17.jpeg"),
            foto("CACIQUE", "WhatsApp Image 2026-06-16 at 10.36.14.jpeg"),
            foto("CACIQUE", "WhatsApp Image 2026-06-16 at 10.37.17 (1).jpeg"),
            foto("CACIQUE", "WhatsApp Image 2026-06-16 at 10.37.18 (1).jpeg"),
            foto("CACIQUE", "WhatsApp Image 2026-06-16 at 10.37.18.jpeg"),
        ],
    },
    {
        "nombre": "IL-1907",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Híbrido de tomate indeterminado con follaje vigoroso, fruto grande y multilocular "
            "con excelente firmeza. Adaptado específicamente a las condiciones climáticas de "
            "Costa Rica. Ideal para producción bajo invernadero y a campo abierto."
        ),
        "specs": [
            ("Porte",          "Indeterminado"),
            ("Tipo de fruto",  "Multilocular"),
            ("Vida poscosecha","LSL — Larga vida anaquel"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "TYLCV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("IL 1907", "WhatsApp Image 2026-06-16 at 09.13.09.jpeg"),
            foto("IL 1907", "WhatsApp Image 2026-06-16 at 09.13.01.jpeg"),
            foto("IL 1907", "WhatsApp Image 2026-06-16 at 09.14.09.jpeg"),
            foto("IL 1907", "WhatsApp Image 2026-06-16 at 09.17.48.jpeg"),
            foto("IL 1907", "WhatsApp Image 2026-06-16 at 09.15.27.jpeg"),
        ],
    },
    {
        "nombre": "IL-1908",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Planta indeterminada de porte alto con frutos de excelente calibre y larga vida "
            "poscosecha. Alta productividad con 3–5 frutos por racimo. Ideal para producción "
            "de invierno y verano."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Frutos/racimo",  "3 – 5"),
            ("Peso promedio",  "240 – 280 g"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "TSWV", "TYLCV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("IL 1908", "WhatsApp Image 2026-06-16 at 09.18.38.jpeg"),
            foto("IL 1908", "WhatsApp Image 2026-06-16 at 09.18.28.jpeg"),
            foto("IL 1908", "WhatsApp Image 2026-06-16 at 09.19.24.jpeg"),
            foto("IL 1908", "WhatsApp Image 2026-06-16 at 09.20.11.jpeg"),
            foto("IL 1908", "WhatsApp Image 2026-06-16 at 09.27.53.jpeg"),
        ],
    },
    {
        "nombre": "IL-1909",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Planta indeterminada con frutos de calibre extragrande y excelente poscosecha. "
            "Alta productividad con 3–5 frutos por racimo. Frutos con calibres superiores a "
            "310 g, destacados por su firmeza y larga vida comercial."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Frutos/racimo",  "3 – 5"),
            ("Peso promedio",  "230 – 310 g"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "TSWV", "TYLCV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("IL 1909", "WhatsApp Image 2026-06-16 at 09.39.45 (1).jpeg"),
            foto("IL 1909", "WhatsApp Image 2026-06-16 at 09.34.36.jpeg"),
            foto("IL 1909", "WhatsApp Image 2026-06-16 at 09.34.44.jpeg"),
            foto("IL 1909", "WhatsApp Image 2026-06-16 at 09.35.07.jpeg"),
            foto("IL 1909", "WhatsApp Image 2026-06-16 at 09.40.26.jpeg"),
        ],
    },
    {
        "nombre": "JM PLUS",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Tomate indeterminado de follaje firme moderado. Fruto extragrande redondeado con "
            "mesocarpio grueso y consistencia muy firme. Excelente comportamiento en poscosecha "
            "y alto valor comercial."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Frutos/racimo",  "3 – 5"),
            ("Peso promedio",  "250 – 350 g"),
            ("Forma",          "Redondeada extragrande"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "TSWV", "TYLCV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("JM PLUS", "WhatsApp Image 2026-06-16 at 10.24.00.jpeg"),
            foto("JM PLUS", "WhatsApp Image 2026-06-16 at 10.23.52 (1).jpeg"),
            foto("JM PLUS", "WhatsApp Image 2026-06-16 at 10.23.52.jpeg"),
        ],
    },
    {
        "nombre": "JR SPECIAL",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Excelente vida poscosecha y alto valor comercial. Planta robusta con buen amarre "
            "de frutos y producción consistente por racimo. Ideal para mercados que exigen "
            "calidad y durabilidad."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Peso promedio",  "250 – 300 g"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "TMV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.57.43.jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.57.32.jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.58.22 (1).jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.59.17.jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 10.00.33.jpeg"),
        ],
    },
    {
        "nombre": "MILAN",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Planta indeterminada con alta carga de frutos por planta (3–7 por racimo). "
            "Excelente vida larga de anaquel y amplia resistencia a enfermedades. "
            "Destacada productividad en condiciones tropicales."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Frutos/racimo",  "3 – 7"),
            ("Peso promedio",  "250 – 300 g"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "TMV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("MILAN", "WhatsApp Image 2026-06-16 at 10.22.45.jpeg"),
            foto("MILAN", "WhatsApp Image 2026-06-16 at 10.11.54.jpeg"),
            foto("MILAN", "WhatsApp Image 2026-06-16 at 10.11.53.jpeg"),
            foto("MILAN", "WhatsApp Image 2026-06-16 at 10.15.11.jpeg"),
            foto("MILAN", "WhatsApp Image 2026-06-16 at 10.15.13.jpeg"),
        ],
    },
    {
        "nombre": "PATRÓN",
        "categoria": "Portainjerto",
        "tipo_tag": "portainjerto",
        "descripcion": (
            "Excelente alternativa para cultivar en suelos con problemas de hongos patógenos "
            "y nemátodos. Sistema radicular eficiente con alta capacidad de absorción de "
            "nutrientes y tolerancia a estreses abióticos: pH, salinidad y bajas temperaturas."
        ),
        "specs": [
            ("Uso recomendado", "Suelos con hongos y nemátodos"),
            ("Beneficio clave", "Sistema radicular eficiente"),
            ("Tolerancias",     "pH, salinidad, frío"),
        ],
        "resistencias": ["V", "F1", "F2", "F3"],
        "bhn": True,
        "fotos": [
            foto("PORTAINJERTO PATRON", "WhatsApp Image 2026-06-16 at 10.41.45.jpeg"),
            foto("PORTAINJERTO PATRON", "WhatsApp Image 2026-06-16 at 10.41.26.jpeg"),
            foto("PORTAINJERTO PATRON", "WhatsApp Image 2026-06-16 at 10.41.27.jpeg"),
            foto("PORTAINJERTO PATRON", "WhatsApp Image 2026-06-16 at 10.41.45 (1).jpeg"),
            foto("PORTAINJERTO PATRON", "WhatsApp Image 2026-06-16 at 11.45.58.jpeg"),
        ],
    },
    {
        "nombre": "R1912",
        "categoria": "Portainjerto",
        "tipo_tag": "portainjerto",
        "descripcion": (
            "Portainjerto intraespecífico de innovación genética. Excelente compatibilidad "
            "entre portainjerto y copa, brindando un sinergismo óptimo entre ambos materiales. "
            "Maximiza la resistencia a enfermedades y el potencial de alta producción."
        ),
        "specs": [
            ("Tipo",           "Intraespecífico"),
            ("Compatibilidad", "Alta con variedades BHN"),
            ("Beneficio",      "Máxima resistencia + producción"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "TSWV", "FORL", "Bacteria"],
        "bhn": True,
        "fotos": [
            foto("PORTAINJERTO R1912", "WhatsApp Image 2026-06-16 at 11.20.15 (1).jpeg"),
            foto("PORTAINJERTO R1912", "WhatsApp Image 2026-06-16 at 11.22.54.jpeg"),
            foto("PORTAINJERTO R1912", "WhatsApp Image 2026-06-16 at 11.19.17.jpeg"),
            foto("PORTAINJERTO R1912", "WhatsApp Image 2026-06-16 at 11.21.45.jpeg"),
            foto("PORTAINJERTO R1912", "WhatsApp Image 2026-06-16 at 11.20.15.jpeg"),
        ],
    },
    {
        "nombre": "SDGR 21",
        "categoria": "Tomate DGR",
        "tipo_tag": "tomate",
        "descripcion": (
            "Tomate tipo Beef indeterminado con planta robusta. Frutos globosos, firmes y de "
            "excelente calidad. Variedad insignia de Semillas DGR, desarrollada para las "
            "condiciones del trópico centroamericano."
        ),
        "specs": [
            ("Porte",      "Indeterminado"),
            ("Tipo",       "Beef"),
            ("Forma",      "Globosa"),
            ("Peso aprox.", "300 g"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "TMV", "TYLCV", "LSL"],
        "bhn": False,
        "fotos": [
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.43.21.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.43.04.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.43.32.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.45.19.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.55.03.jpeg"),
        ],
    },
    {
        "nombre": "TITAN",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Planta indeterminada de porte alto con excelentes características tanto para "
            "invierno como para verano. Fruto tipo bola con hombros medios y cierre perfecto. "
            "Alta adaptabilidad a diferentes condiciones de cultivo."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Frutos/racimo",  "3 – 5"),
            ("Peso promedio",  "250 – 350 g"),
            ("Forma",          "Tipo bola"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "LSL"],
        "bhn": True,
        "fotos": [
            foto("TITAN", "WhatsApp Image 2026-06-16 at 11.41.15.jpeg"),
            foto("TITAN", "WhatsApp Image 2026-06-16 at 11.25.58.jpeg"),
            foto("TITAN", "WhatsApp Image 2026-06-16 at 11.35.27.jpeg"),
            foto("TITAN", "WhatsApp Image 2026-06-16 at 11.36.57.jpeg"),
            foto("TITAN", "WhatsApp Image 2026-06-16 at 11.42.38.jpeg"),
        ],
    },
    {
        "nombre": "VULCANO",
        "categoria": "Tomate BHN",
        "tipo_tag": "tomate",
        "descripcion": (
            "Planta indeterminada de porte alto adaptada a invierno y verano. Fruto tipo bola "
            "con hombros medios y cierre excelente. Larga vida de anaquel y alta resistencia "
            "a enfermedades foliares y del suelo."
        ),
        "specs": [
            ("Altura aprox.",  "1.8 metros"),
            ("Racimos/planta", "8 – 10"),
            ("Frutos/racimo",  "3 – 5"),
            ("Peso promedio",  "250 – 300 g"),
            ("Forma",          "Tipo bola"),
        ],
        "resistencias": ["V", "F1", "F2", "F3", "N", "TMV", "TYLCV", "LSL"],
        "bhn": True,
        "fotos": [],
    },
]

RES_NOMBRES = {
    "V":        "Verticillium dahliae",
    "F1":       "Fusarium Raza 1",
    "F2":       "Fusarium Raza 2",
    "F3":       "Fusarium Raza 3",
    "N":        "Nemátodos (Mi)",
    "TMV":      "Tomato mosaic virus",
    "TSWV":     "Tomato spotted wilt virus",
    "TYLCV":    "Tomato yellow leaf curl virus",
    "LSL":      "Long Shelf Life",
    "FORL":     "Fusarium crown & root rot",
    "Bacteria": "Resistencia bacteriana",
}

# ── LAYOUT CONSTANTS ──
MARGIN = 8 * mm
HALF   = W / 2


def draw_image_box(c, path, x, y, w, h, radius=1.5*mm):
    """Draws a rounded-corner clipped image box with dark bg fallback."""
    # Dark background
    c.setFillColor(SURFACE3)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=0)
    if path and os.path.exists(path):
        try:
            c.drawImage(path, x, y, width=w, height=h,
                        preserveAspectRatio=True, anchor='c', mask='auto')
        except Exception:
            pass


def wrap_text(c, text, font, size, max_width):
    """Returns list of wrapped lines."""
    words = text.split()
    lines, line = [], ""
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_page(c, variedad, page_num, total):
    c.saveState()

    fotos = variedad.get("fotos", [])

    # ── BACKGROUND ──
    c.setFillColor(NEGRO)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── RED TOP BAR ──
    c.setFillColor(ROJO)
    c.rect(0, H - 14*mm, W, 14*mm, fill=1, stroke=0)

    # Logo in bar
    if os.path.exists(LOGO):
        try:
            c.drawImage(LOGO, MARGIN, H - 12.5*mm,
                        width=28*mm, height=10*mm,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            c.setFillColor(BLANCO)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(MARGIN, H - 8*mm, "SEMILLAS DGR")

    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7)
    c.drawRightString(W - MARGIN, H - 5.5*mm, "FICHA TÉCNICA DE VARIEDAD")
    c.setFont("Helvetica", 6)
    c.drawRightString(W - MARGIN, H - 9.5*mm, f"Pág. {page_num} / {total}")

    # ── CATEGORY TAG ──
    y = H - 23*mm
    cat = variedad["categoria"]
    tag_color = ROJO if variedad["tipo_tag"] == "tomate" else VERDE
    tag_bg = colors.HexColor("#2a0a0a") if variedad["tipo_tag"] == "tomate" else colors.HexColor("#0a1f08")
    c.setFillColor(tag_bg)
    c.roundRect(MARGIN, y - 1.5*mm, 40*mm, 7*mm, 2*mm, fill=1, stroke=0)
    c.setFillColor(tag_color)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN + 2.5*mm, y + 1*mm, cat.upper())

    # BHN logo (top-right)
    if variedad["bhn"] and os.path.exists(BHN):
        try:
            c.drawImage(BHN, W - 50*mm, H - 30*mm,
                        width=38*mm, height=14*mm,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            pass

    # ── VARIETY NAME ──
    y -= 10*mm  # y = H-33mm
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(MARGIN, y, variedad["nombre"])

    # Red underline
    y -= 5*mm
    c.setStrokeColor(ROJO)
    c.setLineWidth(2)
    c.line(MARGIN, y, 90*mm, y)

    # ── TWO-COLUMN BLOCK: Description+Specs (left) | Hero image (right) ──
    # This block spans from y down to y - 95mm
    block_top = y - 3*mm      # ~H-41mm
    block_h   = 95 * mm
    block_bot = block_top - block_h  # ~H-136mm

    left_w  = HALF - MARGIN - 3*mm   # ~95mm
    right_x = HALF + 3*mm
    right_w = W - right_x - MARGIN   # ~92mm

    # Hero image (right column)
    draw_image_box(c, fotos[0] if fotos else None,
                   right_x, block_bot, right_w, block_h)

    # Description (left column)
    y_left = block_top
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 8)
    desc_lines = wrap_text(c, variedad["descripcion"], "Helvetica", 8, left_w)
    for ln in desc_lines:
        c.drawString(MARGIN, y_left, ln)
        y_left -= 5*mm

    y_left -= 3*mm

    # Specs (left column, below description)
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN, y_left, "CARACTERÍSTICAS")
    c.setStrokeColor(ROJO)
    c.setLineWidth(1)
    c.line(MARGIN, y_left - 1.5*mm, MARGIN + 38*mm, y_left - 1.5*mm)
    y_left -= 7*mm

    for label, valor in variedad["specs"]:
        c.setFillColor(SURFACE2)
        c.roundRect(MARGIN, y_left - 1.5*mm, left_w, 7*mm, 1.5*mm, fill=1, stroke=0)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN + 3*mm, y_left + 1.5*mm, label + ":")
        c.setFillColor(BLANCO)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawRightString(MARGIN + left_w - 3*mm, y_left + 1.5*mm, valor)
        y_left -= 9*mm

    # ── SEPARATOR ──
    sep_y = block_bot - 5*mm
    c.setStrokeColor(GRIS3)
    c.setLineWidth(0.5)
    c.line(MARGIN, sep_y, W - MARGIN, sep_y)

    # ── RESISTANCES (two columns) ──
    y_res = sep_y - 7*mm
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN, y_res, "RESISTENCIAS")
    c.setStrokeColor(ROJO)
    c.setLineWidth(1)
    c.line(MARGIN, y_res - 1.5*mm, MARGIN + 38*mm, y_res - 1.5*mm)
    y_res -= 7*mm

    res_list  = variedad["resistencias"]
    col_w_res = (W - 2*MARGIN - 5*mm) / 2
    for i, code in enumerate(res_list):
        col_x = MARGIN if i % 2 == 0 else MARGIN + col_w_res + 5*mm
        row_y = y_res - (i // 2) * 9*mm
        nombre_res = RES_NOMBRES.get(code, code)
        c.setFillColor(VERDE_BG)
        c.roundRect(col_x, row_y - 1.5*mm, col_w_res, 7*mm, 1.5*mm, fill=1, stroke=0)
        c.setFillColor(VERDE)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(col_x + 3*mm, row_y + 1.5*mm, code)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 7)
        c.drawString(col_x + 14*mm, row_y + 1.5*mm, nombre_res)

    # ── 4 SMALL IMAGES (bottom strip) ──
    strip_h   = 45 * mm
    strip_top = 22 * mm + strip_h   # 67mm from bottom
    img_count = min(4, len(fotos) - 1)
    if img_count > 0:
        gap   = 2.5 * mm
        img_w = (W - 2*MARGIN - (img_count - 1) * gap) / img_count
        for i in range(img_count):
            ix = MARGIN + i * (img_w + gap)
            iy = 22 * mm
            draw_image_box(c, fotos[i + 1], ix, iy, img_w, strip_h)

    # ── FOOTER ──
    foot_h = 20 * mm
    c.setFillColor(SURFACE2)
    c.rect(0, 0, W, foot_h, fill=1, stroke=0)
    c.setStrokeColor(ROJO)
    c.setLineWidth(1)
    c.line(0, foot_h, W, foot_h)

    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN, foot_h - 5*mm, "Distribuido por: SEMILLAS DGR S.A.")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 6.5)
    c.drawString(MARGIN, foot_h - 9.5*mm,  "Milton Castillo H.  |  semillasdgrsa@gmail.com")
    c.drawString(MARGIN, foot_h - 13.5*mm, "+506 8820-4170  |  +506 2102-0910  |  +506 7053-6966")

    c.drawRightString(W - MARGIN, foot_h - 5*mm,  "semillasdgrsa@gmail.com")
    c.drawRightString(W - MARGIN, foot_h - 9.5*mm, "semillasdgrsa.github.io/semillasdgr")
    c.drawRightString(W - MARGIN, foot_h - 13.5*mm, "@semillasdgr")

    c.restoreState()


def generar():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Catálogo de Variedades — Semillas DGR S.A.")
    c.setAuthor("Semillas DGR S.A.")
    c.setSubject("Fichas Técnicas de Variedades de Tomate y Portainjertos")

    total = len(VARIEDADES)
    for i, var in enumerate(VARIEDADES, 1):
        draw_page(c, var, i, total)
        c.showPage()

    c.save()
    print(f"✅ PDF generado: {OUTPUT}")
    print(f"   {total} fichas — {sum(len(v['fotos']) for v in VARIEDADES)} fotos incluidas")


if __name__ == "__main__":
    generar()
