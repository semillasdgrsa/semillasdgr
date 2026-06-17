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
HEROES = "/Users/lucianacastillo/Desktop/Claude Code/assets"
ORIG   = "/Users/lucianacastillo/Desktop/Claude Code/assets/variedades foto principal"

def hero(filename):
    return os.path.join(HEROES, filename)

def original(filename):
    return os.path.join(ORIG, filename)
OUTPUT = "/Users/lucianacastillo/Desktop/Claude Code/Catalogo_Semillas_DGR.pdf"
LOGO   = "/Users/lucianacastillo/Desktop/Claude Code/assets/galeria/logo-light.jpeg"
LOGO_DARK = "/Users/lucianacastillo/Desktop/Claude Code/assets/galeria/logo-dark.jpeg"
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
        "resistencias": ["TMV", "TSWV", "TYLCV", "F1", "F2", "F3", "V", "N"],
        "bhn": True,
        "fotos": [
            original("CACIQUE.jpeg"),
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
        "resistencias": ["TMV", "TYLCV", "F1", "F2", "F3", "V", "N", "LSL"],
        "bhn": True,
        "fotos": [
            original("IL 1907.jpeg"),
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
        "resistencias": ["TMV", "TSWV", "TYLCV", "F1", "F2", "F3", "V", "N", "LSL"],
        "bhn": True,
        "fotos": [
            original("IL1908.jpeg"),
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
        "resistencias": ["TMV", "TSWV", "TYLCV", "F1", "F2", "F3", "V", "N", "LSL"],
        "bhn": True,
        "fotos": [
            original("IL 1909.jpeg"),
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
        "resistencias": ["TMV", "TSWV", "TYLCV", "F1", "F2", "F3", "V", "N", "LSL"],
        "bhn": True,
        "fotos": [
            original("JM PLUS.jpeg"),
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
        "resistencias": ["TMV", "F1", "F2", "F3", "V", "LSL"],
        "bhn": True,
        "fotos": [
            original("JR SPECIAL.jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.57.32.jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.57.43.jpeg"),
            foto("JR SPECIAL", "WhatsApp Image 2026-06-16 at 09.58.22 (1).jpeg"),
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
        "resistencias": ["TMV", "F1", "F2", "F3", "V", "LSL"],
        "bhn": True,
        "fotos": [
            original("MILAN.jpeg"),
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
        "resistencias": ["F1", "F2", "F3", "V"],
        "bhn": True,
        "fotos": [
            original("PORTAINJERTO PATRON.jpeg"),
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
        "resistencias": ["TMV", "TSWV", "Bacteria", "F1", "F2", "F3", "FORL", "V", "N"],
        "bhn": True,
        "fotos": [
            original("PORTAINJERTO R 1912.jpeg"),
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
        "resistencias": ["TMV", "TYLCV", "F1", "F2", "F3", "V", "LSL"],
        "bhn": False,
        "fotos": [
            original("SDGR 21.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.43.04.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.43.32.jpeg"),
            foto("SDGR 21", "WhatsApp Image 2026-06-16 at 09.43.21.jpeg"),
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
        "resistencias": ["TMV", "F1", "F2", "F3", "V", "N", "LSL"],
        "bhn": True,
        "fotos": [
            original("TITAN.jpeg"),
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
        "resistencias": ["TMV", "TYLCV", "F1", "F2", "F3", "V", "N", "LSL"],
        "bhn": True,
        "fotos": [
            original("VULCANO.jpeg"),
            foto("VULCANO", "WhatsApp Image 2026-06-16 at 21.10.35 (4).jpeg"),
            foto("VULCANO", "WhatsApp Image 2026-06-16 at 21.10.35.jpeg"),
            foto("VULCANO", "WhatsApp Image 2026-06-16 at 21.10.35 (5).jpeg"),
            foto("VULCANO", "WhatsApp Image 2026-06-16 at 21.10.36.jpeg"),
        ],
    },
]

RES_NOMBRES = {
    "TMV":      "Tomato Mosaic Virus",
    "TSWV":     "Tomato Spotted Wilt Virus",
    "TYLCV":    "Tomato Yellow Leaf Curl Virus",
    "Bacteria": "Clavibacter michiganensis",
    "F1":       "Fusarium oxysporum raza 1",
    "F2":       "Fusarium oxysporum raza 2",
    "F3":       "Fusarium oxysporum raza 3",
    "FORL":     "Fusarium radicis-lycopersici",
    "V":        "Verticillium dahliae",
    "N":        "Meloidogyne spp. (Mi)",
    "LSL":      "Long Shelf Life",
}

GLOSARIO = [
    ("VIRUS", ROJO, [
        ("TMV",   "Tomato Mosaic Virus",            "Virus del mosaico del tomate. Causa moteado y deformación foliar."),
        ("TSWV",  "Tomato Spotted Wilt Virus",       "Virus de la marchitez manchada. Transmitido por trips."),
        ("TYLCV", "Tomato Yellow Leaf Curl Virus",   "Virus del enrollamiento amarillo. Transmitido por mosca blanca."),
    ]),
    ("BACTERIAS", colors.HexColor("#c8a020"), [
        ("Bacteria", "Clavibacter michiganensis",    "Bacteria del cancro bacterial. Manchas en hojas y frutos."),
    ]),
    ("HONGOS", VERDE, [
        ("F1", "Fusarium oxysporum raza 1", "Marchitamiento vascular por Fusarium, raza 1."),
        ("F2", "Fusarium oxysporum raza 2", "Marchitamiento vascular por Fusarium, raza 2."),
        ("F3", "Fusarium oxysporum raza 3", "Marchitamiento vascular por Fusarium, raza 3."),
        ("FORL",     "Fusarium radicis-lycopersici",   "Pudrición de raíz y corona por Fusarium."),
        ("V",        "Verticillium dahliae",            "Marchitamiento vascular por Verticillium."),
    ]),
    ("NEMÁTODOS", colors.HexColor("#60a0c8"), [
        ("N",    "Meloidogyne spp. (Mi)",             "Nemátodos del nudo de raíz. Reducen absorción de nutrientes."),
    ]),
    ("CARACTERÍSTICA", GRIS, [
        ("LSL",  "Long Shelf Life",                  "Larga vida de anaquel. Mayor firmeza y durabilidad postcosecha."),
    ]),
]

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

    # ── RED TOP BAR (20mm) ──
    bar_h = 20*mm
    c.setFillColor(ROJO)
    c.rect(0, H - bar_h, W, bar_h, fill=1, stroke=0)

    # Logos centrados verticalmente en la franja roja: DGR izq, BHN al lado
    logo_h = 12*mm
    logo_y = H - bar_h + (bar_h - logo_h) / 2
    dgr_w = 30*mm
    dgr_x = MARGIN
    if os.path.exists(LOGO):
        try:
            c.drawImage(LOGO, dgr_x, logo_y, width=dgr_w, height=logo_h,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            pass
    bw = 22*mm
    bx = dgr_x + dgr_w + 4*mm
    if os.path.exists(BHN):
        try:
            c.drawImage(BHN, bx, logo_y, width=bw, height=logo_h,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            pass

    # Texto derecha en la franja
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7)
    c.drawRightString(W - MARGIN, H - 7*mm, "FICHA TÉCNICA DE VARIEDAD")
    c.setFont("Helvetica", 6)
    c.drawRightString(W - MARGIN, H - 12*mm, f"Pág. {page_num} / {total}")

    # ── CATEGORY TAG ──
    y = H - bar_h - 16*mm
    cat = variedad["categoria"]
    tag_color = ROJO if variedad["tipo_tag"] == "tomate" else VERDE
    tag_bg = colors.HexColor("#2a0a0a") if variedad["tipo_tag"] == "tomate" else colors.HexColor("#0a1f08")
    c.setFillColor(tag_bg)
    c.roundRect(MARGIN, y - 1.5*mm, 40*mm, 7*mm, 2*mm, fill=1, stroke=0)
    c.setFillColor(tag_color)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(MARGIN + 2.5*mm, y + 1*mm, cat.upper())

    # ── VARIETY NAME ──
    y -= 14*mm
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(MARGIN, y, variedad["nombre"])

    # Red underline
    y -= 8*mm
    c.setStrokeColor(ROJO)
    c.setLineWidth(2)
    c.line(MARGIN, y, 90*mm, y)

    # ── TWO-COLUMN BLOCK: Description+Specs (left) | Hero image (right) ──
    block_top = y - 8*mm
    block_h   = 95 * mm
    block_bot = block_top - block_h

    left_w  = HALF - MARGIN - 3*mm
    right_x = HALF + 3*mm
    right_w = W - right_x - MARGIN

    # Hero image (right column)
    draw_image_box(c, fotos[0] if fotos else None,
                   right_x, block_bot, right_w, block_h)

    # Description (left column)
    y_left = block_top
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 8.5)
    desc_lines = wrap_text(c, variedad["descripcion"], "Helvetica", 8.5, left_w)
    for ln in desc_lines:
        c.drawString(MARGIN, y_left, ln)
        y_left -= 5.5*mm

    y_left -= 6*mm

    # Specs (left column, below description)
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN, y_left, "CARACTERÍSTICAS")
    c.setStrokeColor(ROJO)
    c.setLineWidth(1)
    c.line(MARGIN, y_left - 1.5*mm, MARGIN + 38*mm, y_left - 1.5*mm)
    y_left -= 9*mm

    for label, valor in variedad["specs"]:
        c.setFillColor(SURFACE2)
        c.roundRect(MARGIN, y_left - 1.5*mm, left_w, 7.5*mm, 1.5*mm, fill=1, stroke=0)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN + 3*mm, y_left + 2*mm, label + ":")
        c.setFillColor(BLANCO)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawRightString(MARGIN + left_w - 3*mm, y_left + 2*mm, valor)
        y_left -= 10*mm

    # ── SEPARATOR ──
    sep_y = block_bot - 10*mm
    c.setStrokeColor(GRIS3)
    c.setLineWidth(0.5)
    c.line(MARGIN, sep_y, W - MARGIN, sep_y)

    # ── RESISTANCES (two columns) ──
    y_res = sep_y - 14*mm
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(MARGIN, y_res, "RESISTENCIAS")
    c.setStrokeColor(ROJO)
    c.setLineWidth(1)
    c.line(MARGIN, y_res - 1.5*mm, MARGIN + 38*mm, y_res - 1.5*mm)
    y_res -= 9*mm

    res_list  = variedad["resistencias"]
    col_w_res = (W - 2*MARGIN - 5*mm) / 2
    half = -(-len(res_list) // 2)  # ceil division
    for i, code in enumerate(res_list):
        col = 0 if i < half else 1
        row  = i if col == 0 else i - half
        col_x = MARGIN if col == 0 else MARGIN + col_w_res + 5*mm
        row_y = y_res - row * 9.5*mm
        nombre_res = RES_NOMBRES.get(code, code)
        c.setFillColor(VERDE_BG)
        c.roundRect(col_x, row_y - 1.5*mm, col_w_res, 7.5*mm, 1.5*mm, fill=1, stroke=0)
        c.setFillColor(VERDE)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(col_x + 3*mm, row_y + 2*mm, code)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 7)
        c.drawString(col_x + 14*mm, row_y + 2*mm, nombre_res)

    # ── 4 SMALL IMAGES (bottom strip) ──
    strip_h   = 45 * mm
    img_count = min(4, len(fotos) - 1)
    if img_count > 0:
        gap   = 2.5 * mm
        img_w = (W - 2*MARGIN - (img_count - 1) * gap) / img_count
        for i in range(img_count):
            ix = MARGIN + i * (img_w + gap)
            iy = 32 * mm
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


def draw_glossary_page(c, page_num, total):
    c.saveState()

    # Background
    c.setFillColor(NEGRO)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Red top bar (20mm)
    bar_h = 20*mm
    c.setFillColor(ROJO)
    c.rect(0, H - bar_h, W, bar_h, fill=1, stroke=0)

    # Logos centrados en la franja roja: BHN izq, DGR (fondo negro) al lado
    logo_h = 12*mm
    logo_y = H - bar_h + (bar_h - logo_h) / 2
    bw = 22*mm
    bx = MARGIN
    if os.path.exists(BHN):
        try:
            c.drawImage(BHN, bx, logo_y, width=bw, height=logo_h,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            pass
    dgr_x = bx + bw + 4*mm
    dgr_w = 30*mm
    if os.path.exists(LOGO):
        try:
            c.drawImage(LOGO, dgr_x, logo_y, width=dgr_w, height=logo_h,
                        preserveAspectRatio=True, mask='auto')
        except Exception:
            pass

    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7)
    c.drawRightString(W - MARGIN, H - 7*mm, "GLOSARIO DE RESISTENCIAS")
    c.setFont("Helvetica", 6)
    c.drawRightString(W - MARGIN, H - 12*mm, f"Pág. {page_num} / {total}")

    # Title
    y = H - bar_h - 12*mm
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(MARGIN, y, "Glosario de Resistencias")
    y -= 7*mm
    c.setStrokeColor(ROJO)
    c.setLineWidth(2)
    c.line(MARGIN, y, 110*mm, y)
    y -= 8*mm

    # Intro text
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 8)
    intro = ("Los códigos de resistencia se clasifican en dos niveles: HR (High Resistance / Resistencia Alta) e "
             "IR (Intermediate Resistance / Resistencia Intermedia). Se organizan por grupo de patógeno: "
             "Virus → Bacterias → Hongos → Nemátodos.")
    for ln in wrap_text(c, intro, "Helvetica", 8, W - 2*MARGIN):
        c.drawString(MARGIN, y, ln)
        y -= 5*mm
    y -= 4*mm

    # HR / IR legend boxes
    legend_items = [
        ("HR", "High Resistance / Resistencia Alta",
         "La planta controla eficazmente el patógeno bajo presión normal de la enfermedad.",
         VERDE, VERDE_BG),
        ("IR", "Intermediate Resistance / Resistencia Intermedia",
         "La planta reduce el impacto pero puede mostrar síntomas leves bajo alta presión.",
         colors.HexColor("#c8a020"), colors.HexColor("#1a1500")),
    ]
    box_w = (W - 2*MARGIN - 4*mm) / 2
    for idx, (badge, title, desc, col, bgcol) in enumerate(legend_items):
        bx = MARGIN + idx * (box_w + 4*mm)
        c.setFillColor(bgcol)
        c.roundRect(bx, y - 15*mm, box_w, 18*mm, 2*mm, fill=1, stroke=0)
        c.setFillColor(col)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(bx + 3*mm, y - 3*mm, badge)
        c.setFillColor(BLANCO)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(bx + 14*mm, y - 3*mm, title)
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 7)
        for i, ln in enumerate(wrap_text(c, desc, "Helvetica", 7, box_w - 6*mm)):
            c.drawString(bx + 3*mm, y - 8.5*mm - i*4.5*mm, ln)
    y -= 24*mm

    # Group sections
    col_w = (W - 2*MARGIN - 5*mm) / 2
    col_x = [MARGIN, MARGIN + col_w + 5*mm]
    col_idx = 0
    col_y = [y, y]

    for group_name, group_color, items in GLOSARIO:
        cx = col_x[col_idx]
        cy = col_y[col_idx]

        # Group header
        c.setFillColor(group_color)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(cx, cy, group_name)
        c.setStrokeColor(group_color)
        c.setLineWidth(0.75)
        c.line(cx, cy - 1.5*mm, cx + col_w, cy - 1.5*mm)
        cy -= 6*mm

        for code, name, desc in items:
            row_h = 17*mm
            c.setFillColor(SURFACE2)
            c.roundRect(cx, cy - row_h + 2*mm, col_w, row_h, 1.5*mm, fill=1, stroke=0)

            c.setFillColor(group_color)
            c.setFont("Helvetica-Bold", 8.5)
            c.drawString(cx + 3*mm, cy - 3*mm, code)

            c.setFillColor(BLANCO)
            c.setFont("Helvetica-Bold", 7.5)
            name_lines = wrap_text(c, name, "Helvetica-Bold", 7.5, col_w - 6*mm)
            for i, ln in enumerate(name_lines[:2]):
                c.drawString(cx + 3*mm, cy - 7.5*mm - i*4.5*mm, ln)

            c.setFillColor(GRIS)
            c.setFont("Helvetica", 6.5)
            desc_lines = wrap_text(c, desc, "Helvetica", 6.5, col_w - 6*mm)
            base_y = cy - 7.5*mm - len(name_lines[:2])*4.5*mm
            for i, ln in enumerate(desc_lines[:2]):
                c.drawString(cx + 3*mm, base_y - 4*mm - i*4*mm, ln)

            cy -= row_h + 2*mm

        cy -= 4*mm
        col_y[col_idx] = cy
        col_idx = (col_idx + 1) % 2

    # Footer
    foot_h = 20*mm
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
    c.drawString(MARGIN, foot_h - 9.5*mm, "Milton Castillo H.  |  semillasdgrsa@gmail.com")
    c.drawString(MARGIN, foot_h - 13.5*mm, "+506 8820-4170  |  +506 2102-0910  |  +506 7053-6966")
    c.drawRightString(W - MARGIN, foot_h - 5*mm, "semillasdgrsa@gmail.com")
    c.drawRightString(W - MARGIN, foot_h - 9.5*mm, "semillasdgrsa.github.io/semillasdgr")
    c.drawRightString(W - MARGIN, foot_h - 13.5*mm, "@semillasdgr")

    c.restoreState()


def draw_cover_page(c):
    """Portada + índice de variedades."""
    c.saveState()

    # ── FONDO ──
    c.setFillColor(NEGRO)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # ── FRANJA ROJA SUPERIOR (35mm) ──
    cover_bar = 35*mm
    c.setFillColor(ROJO)
    c.rect(0, H - cover_bar, W, cover_bar, fill=1, stroke=0)

    # Logo centrado en franja roja
    if os.path.exists(LOGO):
        try:
            logo_w, logo_h = 50*mm, 18*mm
            lx = (W - logo_w) / 2
            ly = H - cover_bar + (cover_bar - logo_h) / 2
            c.drawImage(LOGO, lx, ly, width=logo_w, height=logo_h,
                        preserveAspectRatio=True, anchor='c', mask='auto')
        except Exception:
            pass

    # ── TÍTULO (centrado entre barra roja e índice) ──
    # Espacio disponible: desde H-cover_bar hasta H-118mm (índice)
    title_center_y = H - cover_bar - (118*mm - cover_bar) / 2  # centro del espacio
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 34)
    title = "CATÁLOGO DE FICHAS TÉCNICAS"
    c.drawCentredString(W / 2, title_center_y + 12*mm, title)

    c.setFillColor(ROJO)
    c.setFont("Helvetica-Bold", 46)
    c.drawCentredString(W / 2, title_center_y - 10*mm, "2026")

    # Línea decorativa
    c.setStrokeColor(ROJO)
    c.setLineWidth(1.5)
    c.line(MARGIN * 3, title_center_y - 22*mm, W - MARGIN * 3, title_center_y - 22*mm)

    c.setFillColor(GRIS)
    c.setFont("Helvetica", 9)
    c.drawCentredString(W / 2, title_center_y - 29*mm, "Semillas DGR S.A.  ·  Belén, Heredia, Costa Rica")

    # ── ÍNDICE DE VARIEDADES ──
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(W / 2, H - 118*mm, "ÍNDICE DE VARIEDADES")
    c.setStrokeColor(GRIS3)
    c.setLineWidth(0.5)
    c.line(MARGIN, H - 121*mm, W - MARGIN, H - 121*mm)

    # Grid: 4 columnas x 3 filas = 12 variedades
    cols = 4
    rows = 3
    gap_x = 4*mm
    gap_y = 5*mm
    grid_top = H - 128*mm
    grid_w = W - 2*MARGIN
    cell_w = (grid_w - (cols - 1) * gap_x) / cols
    cell_h = (grid_top - 28*mm - (rows - 1) * gap_y) / rows  # 28mm for footer area
    img_h = cell_h - 10*mm  # space for name below image

    for idx, var in enumerate(VARIEDADES):
        col = idx % cols
        row = idx // cols
        cx = MARGIN + col * (cell_w + gap_x)
        cy = grid_top - row * (cell_h + gap_y) - cell_h

        # Foto principal
        foto_path = var["fotos"][0] if var["fotos"] else None
        c.setFillColor(SURFACE3)
        c.roundRect(cx, cy + 10*mm, cell_w, img_h, 2*mm, fill=1, stroke=0)
        if foto_path and os.path.exists(foto_path):
            try:
                c.drawImage(foto_path, cx, cy + 10*mm, width=cell_w, height=img_h,
                            preserveAspectRatio=True, anchor='c', mask='auto')
            except Exception:
                pass

        # Nombre
        tag_color = ROJO if var["tipo_tag"] == "tomate" else VERDE
        c.setFillColor(tag_color)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(cx + cell_w / 2, cy + 3.5*mm, var["nombre"])

        # Categoría
        c.setFillColor(GRIS)
        c.setFont("Helvetica", 6)
        c.drawCentredString(cx + cell_w / 2, cy + 0.5*mm, var["categoria"])

    # ── FOOTER ──
    foot_h = 22*mm
    c.setFillColor(SURFACE2)
    c.rect(0, 0, W, foot_h, fill=1, stroke=0)
    c.setStrokeColor(ROJO)
    c.setLineWidth(1)
    c.line(0, foot_h, W, foot_h)

    text_x = MARGIN
    c.setFillColor(BLANCO)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(text_x, foot_h - 6*mm, "Distribuido por: SEMILLAS DGR S.A.")
    c.setFillColor(GRIS)
    c.setFont("Helvetica", 6.5)
    c.drawString(text_x, foot_h - 10.5*mm, "Milton Castillo H.  |  semillasdgrsa@gmail.com")
    c.drawString(text_x, foot_h - 14.5*mm, "+506 8820-4170  |  +506 2102-0910  |  +506 7053-6966")
    c.drawRightString(W - MARGIN, foot_h - 6*mm, "semillasdgr-cr.com")
    c.drawRightString(W - MARGIN, foot_h - 10.5*mm, "semillasdgrsa@gmail.com")
    c.drawRightString(W - MARGIN, foot_h - 14.5*mm, "@semillasdgr")

    c.restoreState()


def generar():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    c.setTitle("Catálogo de Variedades — Semillas DGR S.A.")
    c.setAuthor("Semillas DGR S.A.")
    c.setSubject("Fichas Técnicas de Variedades de Tomate y Portainjertos")

    # Portada
    draw_cover_page(c)
    c.showPage()

    total = len(VARIEDADES) + 1  # +1 for glossary page (portada no cuenta)
    for i, var in enumerate(VARIEDADES, 1):
        draw_page(c, var, i, total)
        c.showPage()

    draw_glossary_page(c, total, total)
    c.showPage()

    c.save()
    print(f"✅ PDF generado: {OUTPUT}")
    print(f"   Portada + {total - 1} fichas + 1 glosario — {sum(len(v['fotos']) for v in VARIEDADES)} fotos incluidas")


def generar_individuales():
    """Genera un PDF individual (ficha + glosario) por cada variedad."""
    out_dir = os.path.join(os.path.dirname(OUTPUT), "assets", "fichas")
    os.makedirs(out_dir, exist_ok=True)
    for var in VARIEDADES:
        nombre_slug = var["nombre"].replace(" ", "_").replace("-", "")
        out_path = os.path.join(out_dir, f"Ficha_{nombre_slug}.pdf")
        c = canvas.Canvas(out_path, pagesize=A4)
        c.setTitle(f"Ficha Técnica — {var['nombre']} — Semillas DGR S.A.")
        c.setAuthor("Semillas DGR S.A.")
        draw_page(c, var, 1, 2)
        c.showPage()
        draw_glossary_page(c, 2, 2)
        c.showPage()
        c.save()
        print(f"  ✅ {out_path}")
    print(f"\n✅ {len(VARIEDADES)} fichas individuales generadas en assets/fichas/")


if __name__ == "__main__":
    generar()
    generar_individuales()
