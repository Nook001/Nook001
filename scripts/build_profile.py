"""Generate the "frame capture" profile SVGs (light/dark x desktop/mobile).

Usage:  python scripts/build_profile.py
Output: assets/frame/{hero,hero-mobile,background,background-mobile}.svg
        assets/frame/dark/... (same names)

Logos are read from the personal website repo (../Nook001.github.io) and embedded
as data URIs, so every SVG is self-contained (GitHub serves README images without
external sub-requests).
"""
from __future__ import annotations

import base64
import io
import re
from pathlib import Path

from PIL import Image

REPO = Path(__file__).resolve().parents[1]
ORG = REPO.parent / "Nook001.github.io" / "assets" / "images" / "organizations"
OUT = REPO / "assets" / "frame"

MONO = "'Cascadia Mono','SFMono-Regular',Consolas,'Liberation Mono',monospace"
SERIF = "Georgia,'Times New Roman','Noto Serif SC',serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Microsoft YaHei','Noto Sans SC',sans-serif"

# Website palette (Nook001.github.io docs/THEMES.md) plus render-scene tones.
THEMES = {
    "light": dict(
        bg="#FAFAF7", bar="#F0F0EB", panel="#F4F3EE", grid="#E8E7E1", line="#D2D1CA",
        ink="#141414", muted="#66665F", faint="#8C8C83",
        accent="#C2402A", accent_soft="#F8E8E4", accent_text="#962F1E",
        gold="#9A7B1E", ray="#141414", miss="#A8A79F",
        sphere="#FFFFFF", sphere_line="#66665F",
        px_empty="#FFFFFF", px_sphere="#E9A898", px_floor="#DAD9D2", px_shadow="#A8A79F", px_sky="#EDEDE7",
        card="#FFFFFF", card_line="#E0E0DA", tile_line="#E0E0DA",
    ),
    "dark": dict(
        bg="#151413", bar="#1E1D1B", panel="#191817", grid="#232220", line="#3A3936",
        ink="#ECECE8", muted="#9B9B95", faint="#66665F",
        accent="#E8705A", accent_soft="#3A1F1A", accent_text="#F09A88",
        gold="#D8C070", ray="#ECECE8", miss="#66665F",
        sphere="#1E1D1B", sphere_line="#9B9B95",
        px_empty="#1E1D1B", px_sphere="#7A3527", px_floor="#2C2C2A", px_shadow="#3A3936", px_sky="#232220",
        card="#1E1D1B", card_line="#2C2C2A", tile_line="#FFFFFF",
    ),
}

PROFILE = dict(
    name="Nook.",
    headline="Incoming PhD · HKUST",
    degree="BSc CS · Warwick × HKUST",
    tags=["Render", "Agent", "System"],
    url="nook001.github.io",
)

EDUCATION = [
    dict(logos=["hkust"], org="HKUST", detail="PhD", badge="incoming"),
    dict(logos=["warwick", "hkust"], org="Warwick × HKUST", detail="BSc CS · joint degree", date="2023–27"),
]

EXPERIENCE = [  # mirrors Nook001.github.io/_data/experience.yml
    dict(logo="hkust", org="HKUST(GZ) · MAYU Lab", role="Research Assistant", date="now", current=True),
    dict(logo="tencent", org="Tencent · CSIG", role="Solution Architect", date="26.04–08"),
    dict(logo="cas", org="CAS · ISCAS", role="Distributed Systems", date="26.01–04"),
    dict(logo="shopee", org="Shopee · Digital Bank", role="Backend Engineer", date="25.12–26.04"),
    dict(logo="oppo", org="OPPO", role="Android Engineer", date="25.06–09"),
]


# ---------------------------------------------------------------- logos
def _png_uri(path: Path, size: int = 128) -> str:
    im = Image.open(path)
    if path.suffix == ".ico":
        im.size = max(im.info.get("sizes", {im.size}))
        im.load()
    im = im.convert("RGBA")
    if path.name == "cas.png":  # opaque square: keep only the round seal
        from PIL import ImageDraw
        mask = Image.new("L", im.size, 0)
        ImageDraw.Draw(mask).ellipse((0, 0, im.width - 1, im.height - 1), fill=255)
        im.putalpha(mask)
    bbox = im.getbbox()
    if bbox:
        im = im.crop(bbox)
    im.thumbnail((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def _warwick_uri() -> str:
    svg = (ORG / "warwick.svg").read_text(encoding="utf-8")
    # Logos sit on white tiles in both themes: always use the dark (positive) crest.
    svg = re.sub(r"<style>.*?</style>", "<style>.crest_positive{fill:#0c0c0c}.crest_negative{display:none}</style>", svg, flags=re.S)
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


LOGOS = {
    "hkust": (_png_uri(ORG / "hkust.ico"), 1.0),
    "warwick": (_warwick_uri(), 463.15 / 655),
    "tencent": (_png_uri(ORG / "tencent.png"), 1.0),
    "cas": (_png_uri(ORG / "cas.png"), 1.0),
    "shopee": (_png_uri(ORG / "shopee.png"), 1.0),
    "oppo": (_png_uri(ORG / "oppo.ico"), 1.0),
}


def tile(name: str, x: float, y: float, s: float, t: dict) -> str:
    """White rounded tile with the organisation mark centred inside."""
    uri, aspect = LOGOS[name]
    pad = s * 0.17
    inner = s - 2 * pad
    w, h = (inner * aspect, inner) if aspect < 1 else (inner, inner / aspect)
    return (
        f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s * 0.22:.1f}" fill="#FFFFFF" stroke="{t["tile_line"]}" stroke-opacity="{0.12 if t is THEMES["dark"] else 1}" stroke-width="1.5"/>'
        f'<image href="{uri}" x="{x + (s - w) / 2:.1f}" y="{y + (s - h) / 2:.1f}" width="{w:.1f}" height="{h:.1f}" preserveAspectRatio="xMidYMid meet"/>'
    )


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- hero
ANIM_CSS = """
.d{stroke-dasharray:1;stroke-dashoffset:0;fill:none}
.a1{animation:a1 9s linear infinite}.a2{animation:a2 9s linear infinite}
.b1{animation:b1 9s linear infinite}.b2{animation:b2 9s linear infinite}
.c1{animation:c1 9s linear infinite}
@keyframes a1{0%{stroke-dashoffset:1}11%,95%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
@keyframes a2{0%,11%{stroke-dashoffset:1}22%,95%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
@keyframes b1{0%,33%{stroke-dashoffset:1}44%,95%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
@keyframes b2{0%,44%{stroke-dashoffset:1}55%,95%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
@keyframes c1{0%,66%{stroke-dashoffset:1}80%,95%{stroke-dashoffset:0}100%{stroke-dashoffset:1}}
.pa{animation:pa 9s linear infinite}.pb{animation:pb 9s linear infinite}.pc{animation:pc 9s linear infinite}
@keyframes pa{0%,23%{fill:var(--e);stroke:var(--k)}25%,95%{fill:var(--k);stroke:var(--k)}100%{fill:var(--e)}}
@keyframes pb{0%,56%{fill:var(--e);stroke:var(--k)}58%,95%{fill:var(--s);stroke:var(--s)}100%{fill:var(--e)}}
@keyframes pc{0%,80%{fill:var(--e);stroke:var(--k)}82%,95%{fill:var(--y);stroke:var(--y)}100%{fill:var(--e)}}
.hx{animation:hx 9s linear infinite}@keyframes hx{0%,54%{opacity:0}56%,95%{opacity:1}100%{opacity:0}}
.hp{animation:hp 9s linear infinite}@keyframes hp{0%,10%{opacity:0}11%,95%{opacity:1}100%{opacity:0}}
.live{animation:live 1.6s ease-in-out infinite}@keyframes live{50%{opacity:.25}}
@media (prefers-reduced-motion: reduce){*{animation:none!important}}
"""


def scene(t: dict) -> str:
    """Ray-tracing scene in a 322x264 local frame (origin = panel top-left at 300,18).

    Three primary rays: (A) hits the sphere, reflects and reaches the light;
    (B) hits the floor, its shadow ray is blocked by the sphere; (C) misses.
    Each finished ray lights one pixel of the framebuffer inset (top-right).
    Geometry is computed for sphere C=(490,168) r=32 and light at (498,38).
    """
    hatch = "".join(f"M{x} 236l-8 8" for x in range(312, 622, 20))
    grid_v = "".join(f"M{x} 18V236" for x in range(340, 622, 40))
    grid_h = "".join(f"M300 {y}H622" for y in range(58, 236, 40))
    sphere_px = [(24, 16), (32, 16), (16, 24), (24, 24), (32, 24), (40, 24), (16, 32), (40, 32), (24, 40)]
    floor_px = [(0, 48), (8, 48), (40, 48), (48, 48), (56, 48)]
    px = "".join(f'<rect x="{x}" y="{y}" width="8" height="8" fill="{t["px_sphere"]}"/>' for x, y in sphere_px)
    px += "".join(f'<rect x="{x}" y="{y}" width="8" height="8" fill="{t["px_floor"]}"/>' for x, y in floor_px)
    px += f'<rect x="0" y="56" width="64" height="8" fill="{t["px_floor"]}"/>'
    return f"""
<rect x="300" y="18" width="322" height="264" rx="4" fill="{t['panel']}" stroke="{t['grid']}"/>
<path d="{grid_v}{grid_h}" stroke="{t['grid']}" stroke-width="0.6"/>
<path d="M300 236H622" stroke="{t['line']}" stroke-width="1.2"/>
<path d="{hatch}" stroke="{t['grid']}"/>
<rect x="476" y="36" width="44" height="4" fill="{t['gold']}"/>
<circle cx="490" cy="168" r="32" fill="{t['sphere']}" stroke="{t['sphere_line']}"/>
<path d="M472 152a22 22 0 0 1 14-10" stroke="{t['sphere_line']}" stroke-width="1.5" fill="none" opacity="0.5"/>
<path d="M322 138l14 8-14 8z" fill="{t['ink']}"/>
<path d="M346 126V170" stroke="{t['line']}"/>
<path class="d a1" pathLength="1" d="M336 146L462 152" stroke="{t['ray']}" stroke-width="1.4"/>
<path class="d a2" pathLength="1" d="M462 152L392 46" stroke="{t['accent']}" stroke-width="1.4"/>
<path class="d a2" pathLength="1" d="M462 152L498 40" stroke="{t['gold']}" stroke-width="1"/>
<circle class="hp" cx="462" cy="152" r="2.6" fill="{t['ray']}"/>
<path class="d b1" pathLength="1" d="M336 146L436 236" stroke="{t['ray']}" stroke-width="1.4"/>
<path class="d b2" pathLength="1" d="M436 236L461 183" stroke="{t['gold']}" stroke-width="1"/>
<path class="hx" d="M456 178l10 10M466 178l-10 10" stroke="{t['accent']}" stroke-width="1.6"/>
<path class="d c1" pathLength="1" d="M336 146L622 108" stroke="{t['miss']}" stroke-width="1.2"/>
<g transform="translate(548 28)" style="--e:{t['px_empty']};--k:{t['accent']};--s:{t['px_shadow']};--y:{t['px_sky']}">
<rect width="64" height="64" fill="{t['px_empty']}" stroke="{t['line']}"/>
{px}
<rect class="pa" x="24" y="32" width="8" height="8" fill="{t['accent']}" stroke="{t['accent']}"/>
<rect class="pb" x="16" y="48" width="8" height="8" fill="{t['px_shadow']}" stroke="{t['px_shadow']}"/>
<rect class="pc" x="48" y="8" width="8" height="8" fill="{t['px_sky']}" stroke="{t['px_sky']}"/>
</g>"""


def tags_text(t: dict) -> str:
    sep = f'<tspan fill="{t["faint"]}">  |  </tspan>'
    return sep.join(esc(x) for x in PROFILE["tags"])


def hero(t: dict, mobile: bool) -> str:
    W, H = (720, 1000) if mobile else (1200, 560)
    bar = 60 if mobile else 48
    fs_bar = 22 if mobile else 16
    title = "Nook — Incoming PhD at HKUST; BSc CS, Warwick × HKUST joint degree; Render | Agent | System. Opens nook001.github.io."
    if mobile:
        info = f"""
<text x="40" y="178" font-family="{SERIF}" font-size="104" fill="{t['ink']}">{PROFILE['name']}</text>
<text x="44" y="240" font-family="{SANS}" font-size="34" fill="{t['accent']}">{esc(PROFILE['headline'])}</text>
<text x="44" y="286" font-family="{SANS}" font-size="29" fill="{t['muted']}">{esc(PROFILE['degree'])}</text>
<text x="44" y="344" font-family="{MONO}" font-size="28" fill="{t['ink']}">{tags_text(t)}</text>
<g transform="translate(40 384) scale(1.988) translate(-300 -18)">{scene(t)}</g>"""
        link_y = 958
        link = f"""
<rect x="40" y="{link_y - 34}" width="48" height="48" rx="8" fill="none" stroke="{t['line']}"/>
<text x="64" y="{link_y}" text-anchor="middle" font-family="{SANS}" font-size="26" fill="{t['accent']}">↗</text>
<text x="104" y="{link_y - 6}" font-family="{MONO}" font-size="24" fill="{t['ink']}">{PROFILE['url']}</text>
<text x="104" y="{link_y + 22}" font-family="{SANS}" font-size="21" fill="{t['muted']}">Tap to visit my website</text>"""
    else:
        info = f"""
<text x="56" y="200" font-family="{SERIF}" font-size="92" fill="{t['ink']}">{PROFILE['name']}</text>
<text x="60" y="262" font-family="{SANS}" font-size="28" fill="{t['accent']}">{esc(PROFILE['headline'])}</text>
<text x="60" y="302" font-family="{SANS}" font-size="23" fill="{t['muted']}">{esc(PROFILE['degree'])}</text>
<text x="60" y="372" font-family="{MONO}" font-size="23" fill="{t['ink']}">{tags_text(t)}</text>
<g transform="translate(598 78) scale(1.667) translate(-300 -18)">{scene(t)}</g>"""
        link_y = 494
        link = f"""
<rect x="56" y="{link_y - 30}" width="42" height="42" rx="7" fill="none" stroke="{t['line']}"/>
<text x="77" y="{link_y - 1}" text-anchor="middle" font-family="{SANS}" font-size="22" fill="{t['accent']}">↗</text>
<text x="114" y="{link_y - 8}" font-family="{MONO}" font-size="19" fill="{t['ink']}">{PROFILE['url']}</text>
<text x="114" y="{link_y + 15}" font-family="{SANS}" font-size="16" fill="{t['muted']}">Click to visit my website</text>"""
    right = "64 spp · 16.6 ms" if not mobile else "64 spp"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{esc(title)}</title>
<style>{ANIM_CSS}</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="10" fill="{t['bg']}" stroke="{t['line']}" stroke-width="1.5"/>
<path d="M1 {bar}H{W - 1}" stroke="{t['line']}"/>
<path d="M11 1H{W - 11}a10 10 0 0 1 10 10V{bar}H1V11a10 10 0 0 1 10-10z" fill="{t['bar']}"/>
<circle class="live" cx="{28 if mobile else 26}" cy="{bar / 2}" r="{6 if mobile else 5}" fill="{t['accent']}"/>
<text x="{44 if mobile else 40}" y="{bar / 2 + fs_bar * 0.36:.1f}" font-family="{MONO}" font-size="{fs_bar}" fill="{t['ink']}">FRAME 0426<tspan fill="{t['muted']}">  ·  path tracing</tspan></text>
<text x="{W - 24}" y="{bar / 2 + fs_bar * 0.36:.1f}" text-anchor="end" font-family="{MONO}" font-size="{fs_bar}" fill="{t['muted']}">{right}</text>
{info}
{link}
</svg>
"""


# ---------------------------------------------------------------- education + experience
def edu_card(t: dict, x: float, y: float, w: float, h: float, k: float) -> str:
    """k = type scale (1 desktop, ~1.45 mobile)."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{t["card"]}" stroke="{t["card_line"]}" stroke-width="1.5"/>',
           f'<text x="{x + 32}" y="{y + 46 * k:.0f}" font-family="{MONO}" font-size="{17 * k:.0f}" letter-spacing="2" fill="{t["accent"]}">EDUCATION</text>']
    s = 72 * min(k, 1.15)  # smaller marks on phones so the joint-degree row fits
    row_h = (h - 80 * k) / len(EDUCATION)
    for i, e in enumerate(EDUCATION):
        ry = y + 80 * k + i * row_h
        cy = ry + row_h / 2
        if i:
            out.append(f'<path d="M{x + 32} {ry:.0f}H{x + w - 32}" stroke="{t["card_line"]}" stroke-width="1.5"/>')
        lx = x + 32
        step = s + 10 * k  # joint degree: two marks side by side
        for j, lg in enumerate(e["logos"]):
            out.append(tile(lg, lx + j * step, cy - s / 2, s, t))
        tx = lx + s + (len(e["logos"]) - 1) * step + 22 * k
        out.append(f'<text x="{tx:.0f}" y="{cy - 4 * k:.0f}" font-family="{SANS}" font-size="{25 * k:.0f}" fill="{t["ink"]}">{esc(e["org"])}</text>')
        out.append(f'<text x="{tx:.0f}" y="{cy + 26 * k:.0f}" font-family="{SANS}" font-size="{20 * k:.0f}" fill="{t["muted"]}">{esc(e["detail"])}</text>')
        if e.get("badge"):
            bw, bh = 116 * k, 34 * k
            bx = x + w - 32 - bw
            out.append(f'<rect x="{bx:.0f}" y="{cy - bh / 2 - 6 * k:.0f}" width="{bw:.0f}" height="{bh:.0f}" rx="{6 * k:.0f}" fill="{t["accent_soft"]}"/>')
            out.append(f'<text x="{bx + bw / 2:.0f}" y="{cy + 6 * k - 6 * k:.0f}" text-anchor="middle" font-family="{MONO}" font-size="{17 * k:.0f}" fill="{t["accent_text"]}">{esc(e["badge"])}</text>')
        if e.get("date"):
            out.append(f'<text x="{x + w - 32}" y="{cy - 4 * k:.0f}" text-anchor="end" font-family="{MONO}" font-size="{17 * k:.0f}" fill="{t["faint"]}">{esc(e["date"])}</text>')
    return "\n".join(out)


def exp_card(t: dict, x: float, y: float, w: float, h: float, k: float) -> str:
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{t["card"]}" stroke="{t["card_line"]}" stroke-width="1.5"/>',
           f'<text x="{x + 32}" y="{y + 46 * k:.0f}" font-family="{MONO}" font-size="{17 * k:.0f}" letter-spacing="2" fill="{t["accent"]}">EXPERIENCE</text>']
    s = 46 * k
    top = y + 70 * k
    row_h = (h - 70 * k - 18 * k) / len(EXPERIENCE)
    for i, e in enumerate(EXPERIENCE):
        cy = top + i * row_h + row_h / 2
        out.append(tile(e["logo"], x + 32, cy - s / 2, s, t))
        tx = x + 32 + s + 18 * k
        out.append(f'<text x="{tx:.0f}" y="{cy - 3 * k:.0f}" font-family="{SANS}" font-size="{20 * k:.0f}" fill="{t["ink"]}">{esc(e["org"])}</text>')
        out.append(f'<text x="{tx:.0f}" y="{cy + 21 * k:.0f}" font-family="{SANS}" font-size="{17 * k:.0f}" fill="{t["muted"]}">{esc(e["role"])}</text>')
        if e.get("current"):
            out.append(f'<circle class="live" cx="{x + w - 32 - 54 * k:.0f}" cy="{cy - 3 * k:.0f}" r="{5 * k:.1f}" fill="{t["accent"]}"/>')
            out.append(f'<text x="{x + w - 32}" y="{cy + 3 * k:.0f}" text-anchor="end" font-family="{MONO}" font-size="{17 * k:.0f}" fill="{t["accent"]}">{esc(e["date"])}</text>')
        else:
            out.append(f'<text x="{x + w - 32}" y="{cy + 3 * k:.0f}" text-anchor="end" font-family="{MONO}" font-size="{16 * k:.0f}" fill="{t["faint"]}">{esc(e["date"])}</text>')
    return "\n".join(out)


def background(t: dict, mobile: bool) -> str:
    title = ("Education: HKUST PhD (incoming); Warwick × HKUST BSc CS joint degree, 2023–27. "
             "Experience: HKUST(GZ) MAYU Lab Research Assistant (now); Tencent CSIG Solution Architect; "
             "CAS ISCAS Distributed Systems; Shopee Digital Bank Backend Engineer; OPPO Android Engineer.")
    if mobile:
        W, k = 720, 1.42
        eh, xh, gap = 440, 620, 24
        H = eh + gap + xh
        body = edu_card(t, 1, 1, W - 2, eh - 2, k) + exp_card(t, 1, eh + gap, W - 2, xh - 1, k)
    else:
        W, H, gap = 1200, 440, 24
        cw = (W - gap) / 2
        body = edu_card(t, 1, 1, cw - 1, H - 2, 1) + exp_card(t, cw + gap, 1, cw - 1, H - 2, 1)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{esc(title)}</title>
<style>.live{{animation:live 1.6s ease-in-out infinite}}@keyframes live{{50%{{opacity:.25}}}}@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}</style>
{body}
</svg>
"""


# ---------------------------------------------------------------- projects
# Full-size Dynamic Shader stage captures (≈9 MB) live in the git-excluded preview
# folder; the committed SVGs already embed compressed copies.
SHOTS = REPO / ".profile-preview" / "sources" / "dynamic-shader-stages"
# 16:10 project screenshots (built by .profile-preview/build_v3.py), kept out of git
V3 = REPO / ".profile-preview" / "sources" / "project-shots"


def _jpeg_uri(path: Path, w: int = 560, h: int = 350, anchor_y: float = 0.5) -> str:
    im = Image.open(path).convert("RGB")
    scale = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    x0, y0 = (im.width - w) // 2, round((im.height - h) * anchor_y)
    buf = io.BytesIO()
    im.crop((x0, y0, x0 + w, y0 + h)).save(buf, "JPEG", quality=80, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


DS_STAGES = [  # (label, file) — same scene, three stages of the pipeline
    ("01  vanilla", "vanilla.png"),
    ("02  + shadows · lighting · water", "shadow.png"),
    ("03  final · 3D perspective + post", "final.png"),
]

DYNAMIC = dict(
    kicker="PROJECT 01", meta="stardew valley · smapi mod", link_label="nexusmods ↗",
    name="Dynamic Shader",
    desc="Dynamic lighting, shadows and water effects for Stardew Valley.",
    desc_m=["Dynamic lighting, shadows and water", "effects for Stardew Valley."],
    badge="250K+ downloads", tech="HLSL · C# · Harmony",
)

STRIPS = {
    "mywarwickplus": dict(
        kicker="PROJECT 02 · ANDROID", name="MyWarwickPlus", shot="mywarwickplus.jpg", anchor=0.0,
        desc="A native Android client for Warwick timetables, coursework and messages.",
        desc_m=["A native Android client for Warwick", "timetables, coursework and messages."],
        tech="Kotlin · Jetpack Compose ↗", motion="progress", motion_label="next · CS324",
    ),
    "qingyin": dict(
        kicker="PROJECT 03 · LINUX", name="Qingyin 清音", shot="qingyin.jpg", anchor=0.0,
        desc="A Chinese-first local music player for Linux.",
        desc_m=["A Chinese-first local music player", "for Linux."],
        tech="Rust · Qt Quick · GStreamer ↗", motion="eq", motion_label="now playing",
    ),
}

PROJECT_CSS = """
.scan{animation:scan 7.5s linear infinite}
@keyframes scan{0%{transform:translateX(0);opacity:0}4%{opacity:1}92%{opacity:1}100%{transform:translateX(var(--run));opacity:0}}
.f1{animation:f1 7.5s linear infinite}.f2{animation:f2 7.5s linear infinite}.f3{animation:f3 7.5s linear infinite}
@keyframes f1{0%,3%{opacity:0}6%,30%{opacity:1}34%,100%{opacity:0}}
@keyframes f2{0%,34%{opacity:0}38%,62%{opacity:1}66%,100%{opacity:0}}
@keyframes f3{0%,66%{opacity:0}70%,100%{opacity:1}}
.pg{transform-box:fill-box;transform-origin:left;animation:pg 6s linear infinite}
@keyframes pg{from{transform:scaleX(.08)}to{transform:scaleX(1)}}
.eq rect{transform-box:fill-box;transform-origin:bottom;animation:eq 1.2s ease-in-out infinite}
@keyframes eq{0%,100%{transform:scaleY(.3)}50%{transform:scaleY(1)}}
@media (prefers-reduced-motion: reduce){*{animation:none!important}.scan{opacity:0}}
"""


def _frame(uri: str, x: float, y: float, w: float, h: float, cid: str, t: dict, hl: str = "") -> str:
    out = (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/></clipPath>'
           f'<image href="{uri}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})"/>'
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="none" stroke="{t["line"]}"/>')
    if hl:
        out += f'<rect class="{hl}" x="{x - 3}" y="{y - 3}" width="{w + 6}" height="{h + 6}" rx="8" fill="none" stroke="{t["accent"]}" stroke-width="2.5"/>'
    return out


def _topbar(t: dict, W: int, bar: int, fs: int, left: str, meta: str, right: str) -> str:
    return (f'<rect x="1" y="1" width="{W - 2}" height="{{H}}" rx="10" fill="{t["bg"]}" stroke="{t["line"]}" stroke-width="1.5"/>'
            f'<path d="M11 1H{W - 11}a10 10 0 0 1 10 10V{bar}H1V11a10 10 0 0 1 10-10z" fill="{t["bar"]}"/>'
            f'<path d="M1 {bar}H{W - 1}" stroke="{t["line"]}"/>'
            f'<text x="24" y="{bar / 2 + fs * 0.36:.1f}" font-family="{MONO}" font-size="{fs}" fill="{t["accent"]}">{esc(left)}'
            f'<tspan fill="{t["muted"]}">  ·  {esc(meta)}</tspan></text>'
            f'<text x="{W - 24}" y="{bar / 2 + fs * 0.36:.1f}" text-anchor="end" font-family="{MONO}" font-size="{fs}" fill="{t["muted"]}">{esc(right)}</text>')


def dynamic_card(t: dict, mobile: bool, uris: list[str]) -> str:
    p = DYNAMIC
    title = f"{p['name']} — {p['desc']} {p['badge']} on Nexus Mods. Vanilla, then shadows, lighting and water, then the final frame with 3D perspective and post-processing."
    if mobile:
        W, bar, fs, k = 720, 60, 22, 1.42
        fw, fh = 316, 198
        big_w, big_h = 672, 420
        y0 = bar + 28
        frames = (_frame(uris[0], 24, y0, fw, fh, "c1", t, "f1") + _frame(uris[1], 24 + fw + 40, y0, fw, fh, "c2", t, "f2")
                  + f'<path d="M{24 + fw + 14} {y0 + fh / 2 - 8}l12 8-12 8z" fill="{t["faint"]}"/>'
                  + _frame(uris[2], 24, y0 + fh + 72, big_w, big_h, "c3", t, "f3"))
        labels = (f'<text x="24" y="{y0 + fh + 34}" font-family="{MONO}" font-size="20" fill="{t["muted"]}">01 vanilla</text>'
                  f'<text x="{24 + fw + 40}" y="{y0 + fh + 34}" font-family="{MONO}" font-size="20" fill="{t["muted"]}">02 + light · water</text>'
                  f'<text x="24" y="{y0 + fh + 72 + big_h + 34}" font-family="{MONO}" font-size="20" fill="{t["accent"]}">03 final · 3D + post</text>')
        ty = y0 + fh + 72 + big_h + 104
        desc = "".join(f'<text x="24" y="{ty + 44 + i * 36}" font-family="{SANS}" font-size="27" fill="{t["muted"]}">{esc(s)}</text>' for i, s in enumerate(p["desc_m"]))
        H = ty + 44 + 36 * len(p["desc_m"]) + 96
        foot = (f'<rect x="24" y="{H - 82}" width="240" height="48" rx="8" fill="{t["accent_soft"]}"/>'
                f'<text x="144" y="{H - 50}" text-anchor="middle" font-family="{MONO}" font-size="22" fill="{t["accent_text"]}">{esc(p["badge"])}</text>'
                f'<text x="{W - 24}" y="{H - 50}" text-anchor="end" font-family="{MONO}" font-size="21" fill="{t["faint"]}">{esc(p["tech"])}</text>')
        body = (frames + labels
                + f'<text x="24" y="{ty}" font-family="{SERIF}" font-size="50" fill="{t["ink"]}">{esc(p["name"])}</text>' + desc + foot)
        scan = ""  # the frame highlight carries the motion on phones
    else:
        W, bar, fs = 1200, 48, 16
        gap, fw = 56, 336
        fh = fw * 10 / 16
        y0 = 84
        xs = [40 + i * (fw + gap) for i in range(3)]
        frames = "".join(_frame(u, x, y0, fw, fh, f"c{i}", t, f"f{i + 1}") for i, (u, x) in enumerate(zip(uris, xs)))
        frames += "".join(f'<path d="M{x + fw + gap / 2 - 6} {y0 + fh / 2 - 9}l14 9-14 9z" fill="{t["faint"]}"/>' for x in xs[:2])
        labels = "".join(
            f'<text x="{x}" y="{y0 + fh + 32:.0f}" font-family="{MONO}" font-size="16" fill="{t["accent"] if i == 2 else t["muted"]}">{esc(lbl)}</text>'
            for i, ((lbl, _), x) in enumerate(zip(DS_STAGES, xs)))
        ty = y0 + fh + 104
        H = int(ty + 120)
        body = (frames + labels
                + f'<text x="40" y="{ty:.0f}" font-family="{SERIF}" font-size="42" fill="{t["ink"]}">{esc(p["name"])}</text>'
                + f'<text x="40" y="{ty + 38:.0f}" font-family="{SANS}" font-size="20" fill="{t["muted"]}">{esc(p["desc"])}</text>'
                + f'<rect x="40" y="{ty + 62:.0f}" width="176" height="36" rx="6" fill="{t["accent_soft"]}"/>'
                + f'<text x="128" y="{ty + 86:.0f}" text-anchor="middle" font-family="{MONO}" font-size="16" fill="{t["accent_text"]}">{esc(p["badge"])}</text>'
                + f'<text x="{W - 40}" y="{ty + 86:.0f}" text-anchor="end" font-family="{MONO}" font-size="16" fill="{t["faint"]}">{esc(p["tech"])}</text>')
        scan = (f'<g class="scan" style="--run:{xs[2] + fw - 40}px"><rect x="40" y="{y0 - 10}" width="2.5" height="{fh + 20:.0f}" fill="{t["accent"]}"/></g>')
    meta = "smapi mod" if mobile else p["meta"]
    top = _topbar(t, W, bar, fs, p["kicker"], meta, p["link_label"]).replace("{H}", str(H - 2))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{esc(title)}</title>
<style>{PROJECT_CSS}</style>
{top}
{body}
{scan}
</svg>
"""


def strip_card(t: dict, mobile: bool, key: str, uri: str) -> str:
    p = STRIPS[key]
    title = f"{p['name']} — {p['desc']} {p['tech'].rstrip(' ↗')}."
    if mobile:
        W, k = 720, 1.42
        iw, ih = 672, 420
        img = _frame(uri, 24, 24, iw, ih, "s", t)
        y = 24 + ih + 56
        text = (f'<text x="24" y="{y}" font-family="{MONO}" font-size="21" letter-spacing="2" fill="{t["accent"]}">{esc(p["kicker"])}</text>'
                f'<text x="24" y="{y + 58}" font-family="{SERIF}" font-size="46" fill="{t["ink"]}">{esc(p["name"])}</text>'
                + "".join(f'<text x="24" y="{y + 104 + i * 36}" font-family="{SANS}" font-size="27" fill="{t["muted"]}">{esc(s)}</text>' for i, s in enumerate(p["desc_m"])))
        my = y + 104 + 36 * len(p["desc_m"]) + 40
        H = my + 104
        mx, mfs, mw = 24, 21, 220
        # phones: tech stack gets its own line so it never collides with the motion row
        tech = f'<text x="24" y="{my + 58}" font-family="{MONO}" font-size="20" fill="{t["faint"]}">{esc(p["tech"])}</text>'
    else:
        W, H = 1200, 250
        iw, ih = 336, 210
        img = _frame(uri, 20, 20, iw, ih, "s", t)
        x = 20 + iw + 40
        text = (f'<text x="{x}" y="66" font-family="{MONO}" font-size="16" letter-spacing="2" fill="{t["accent"]}">{esc(p["kicker"])}</text>'
                f'<text x="{x}" y="118" font-family="{SERIF}" font-size="38" fill="{t["ink"]}">{esc(p["name"])}</text>'
                f'<text x="{x}" y="156" font-family="{SANS}" font-size="20" fill="{t["muted"]}">{esc(p["desc"])}</text>')
        my, mx, mfs, mw = 202, x, 16, 200
        tech = f'<text x="{W - 40}" y="{my + 6}" text-anchor="end" font-family="{MONO}" font-size="16" fill="{t["faint"]}">{esc(p["tech"])}</text>'
    if p["motion"] == "progress":
        bh = mfs * 0.45
        lw = len(p["motion_label"]) * mfs * 0.62 + 16
        motion = (f'<text x="{mx}" y="{my + 6}" font-family="{MONO}" font-size="{mfs}" fill="{t["muted"]}">{esc(p["motion_label"])}</text>'
                  f'<rect x="{mx + lw:.0f}" y="{my - bh / 2:.0f}" width="{mw}" height="{bh:.0f}" rx="{bh / 2:.0f}" fill="{t["card_line"]}"/>'
                  f'<rect class="pg" x="{mx + lw:.0f}" y="{my - bh / 2:.0f}" width="{mw}" height="{bh:.0f}" rx="{bh / 2:.0f}" fill="{t["accent"]}"/>')
    else:
        bw, bh, step = mfs * 0.3, mfs * 1.2, mfs * 0.48
        delays = [-0.2, -0.7, -0.4, -0.95, -0.1]
        bars = "".join(f'<rect x="{mx + i * step:.1f}" y="{my + 6 - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" style="animation-delay:{d}s"/>' for i, d in enumerate(delays))
        motion = (f'<g class="eq" fill="{t["accent"]}">{bars}</g>'
                  f'<text x="{mx + 5 * step + 12:.0f}" y="{my + 6}" font-family="{MONO}" font-size="{mfs}" fill="{t["muted"]}">{esc(p["motion_label"])}</text>')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{esc(title)}</title>
<style>{PROJECT_CSS}</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="10" fill="{t['bg']}" stroke="{t['line']}" stroke-width="1.5"/>
{img}
{text}
{motion}
{tech}
</svg>
"""


# ---------------------------------------------------------------- stack + contact
# Icons: tandpfun/skill-icons (MIT, see assets/frame/LICENSE-skill-icons.md),
# downloaded to the git-excluded preview folder and embedded as data URIs.
ICONS = REPO / ".profile-preview" / "sources" / "skill-icons"
STACK = [
    ("LANGUAGES", ["Java", "Kotlin", "TypeScript", "CS", "Python", "Rust"]),
    ("TOOLS", ["Spring", "Redis", "RabbitMQ", "Bun", "PyTorch", "Blender"]),
]
STACK_NAMES = {"CS": "C#"}
CONTACT = dict(email="nook_lyz@outlook.com", heading="Get in touch")


def _icon_uri(name: str, theme: str) -> str:
    f = ICONS / f"{name}-{'Dark' if theme == 'dark' else 'Light'}.svg"
    if not f.exists():
        f = ICONS / f"{name}.svg"  # single-variant icons (TypeScript, C#, Rust)
    return "data:image/svg+xml;base64," + base64.b64encode(f.read_bytes()).decode()


def footer(t: dict, theme: str, mobile: bool) -> str:
    names = ", ".join(STACK_NAMES.get(n, n) for _, row in STACK for n in row)
    title = f"Tech stack: {names}. Contact: {CONTACT['email']} (opens your mail app)."
    if mobile:
        W, bar, fs = 720, 60, 22
        s, gap, x0 = 88, 20, 24
        rows = []
        y = bar + 64
        for label, icons in STACK:
            rows.append(f'<text x="{x0}" y="{y}" font-family="{MONO}" font-size="20" letter-spacing="2" fill="{t["muted"]}">{label}</text>')
            rows += [f'<image href="{_icon_uri(n, theme)}" x="{x0 + i * (s + gap)}" y="{y + 20}" width="{s}" height="{s}"/>' for i, n in enumerate(icons)]
            y += 20 + s + 64
        dy = y - 24
        contact = (f'<path d="M24 {dy}H{W - 24}" stroke="{t["line"]}"/>'
                   f'<text x="24" y="{dy + 74}" font-family="{SERIF}" font-size="46" fill="{t["ink"]}">{CONTACT["heading"]}</text>'
                   f'<text x="24" y="{dy + 122}" font-family="{MONO}" font-size="26" fill="{t["accent"]}">{CONTACT["email"]}</text>'
                   f'<text x="24" y="{dy + 160}" font-family="{SANS}" font-size="22" fill="{t["muted"]}">Tap to send an email</text>')
        H = dy + 200
    else:
        W, bar, fs = 1200, 48, 16
        s, gap, x0 = 60, 18, 190
        rows = []
        for r, (label, icons) in enumerate(STACK):
            y = 84 + r * 92
            rows.append(f'<text x="40" y="{y + s / 2 + 5:.0f}" font-family="{MONO}" font-size="15" letter-spacing="2" fill="{t["muted"]}">{label}</text>')
            rows += [f'<image href="{_icon_uri(n, theme)}" x="{x0 + i * (s + gap)}" y="{y}" width="{s}" height="{s}"/>' for i, n in enumerate(icons)]
        H = 84 + 2 * 92 + 18
        cx = 800
        contact = (f'<path d="M{cx - 44} 80V{H - 34}" stroke="{t["line"]}"/>'
                   f'<text x="{cx}" y="132" font-family="{SERIF}" font-size="36" fill="{t["ink"]}">{CONTACT["heading"]}</text>'
                   f'<text x="{cx}" y="172" font-family="{MONO}" font-size="19" fill="{t["accent"]}">{CONTACT["email"]}</text>'
                   f'<text x="{cx}" y="202" font-family="{SANS}" font-size="16" fill="{t["muted"]}">Click to send an email</text>')
    top = _topbar(t, W, bar, fs, "STACK", "contact", "mailto ↗").replace("{H}", str(H - 2))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t"><title id="t">{esc(title)}</title>
{top}
{"".join(rows)}
{contact}
</svg>
"""


def main() -> None:
    ds_uris = [_jpeg_uri(SHOTS / f) for _, f in DS_STAGES]
    strip_uris = {k: _jpeg_uri(V3 / p["shot"], anchor_y=p["anchor"]) for k, p in STRIPS.items()}
    for theme, t in THEMES.items():
        d = OUT / "dark" if theme == "dark" else OUT
        d.mkdir(parents=True, exist_ok=True)
        files = {
            "hero.svg": hero(t, False),
            "hero-mobile.svg": hero(t, True),
            "background.svg": background(t, False),
            "background-mobile.svg": background(t, True),
            "project-dynamic-shader.svg": dynamic_card(t, False, ds_uris),
            "project-dynamic-shader-mobile.svg": dynamic_card(t, True, ds_uris),
        }
        for key, uri in strip_uris.items():
            files[f"project-{key}.svg"] = strip_card(t, False, key, uri)
            files[f"project-{key}-mobile.svg"] = strip_card(t, True, key, uri)
        files["footer.svg"] = footer(t, theme, False)
        files["footer-mobile.svg"] = footer(t, theme, True)
        for name, svg in files.items():
            (d / name).write_text(svg, encoding="utf-8", newline="\n")
            print(f"{(d / name).relative_to(REPO)}  {len(svg.encode()):,} B")


if __name__ == "__main__":
    main()
