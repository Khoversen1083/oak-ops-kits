#!/usr/bin/env python3
"""
IG Carousel renderer for @kevhov.ai.

Reads a carousel.json file describing a single carousel post (8 slides), renders
each slide as a 1080x1350 JPG, and drops them in iCloud 00-Post Today/ for
manual phone upload.

Programmatic API:
    from render import Carousel
    car = Carousel.from_json("/path/to/carousel.json")
    paths = car.render()           # -> list[Path] of 8 JPGs

Or from the command line:
    python3 render.py /path/to/carousel.json
    python3 render.py /path/to/reel-folder    # auto-finds carousel.json inside

Carousel JSON schema:
    {
      "keyword": "ENGINE",
      "hook": "Never run out of AI build ideas",
      "hook_sub": "(optional second-line tease)",
      "stakes": "Most builders are still typing prompts one at a time.",
      "system_name": "The Two-Skill Engine",
      "system_oneliner": "v2-signal scrapes trends, v2-write turns each into a reel.",
      "system_blocks": ["SCRAPE", "SCORE", "WRITE"],
      "steps": [
        {"title": "Scrape",  "body": "v2-signal pulls every viral AI reel from 12 handles overnight."},
        {"title": "Score",   "body": "Each gets a threat-match + tool-demo score in Notion."},
        {"title": "Write",   "body": "v2-write drafts caption + capcut-lines from the winner."}
      ],
      "payoff": "10 minutes of curation replaces 4 hours of ideation.",
      "cta_body": "I'll send the full build, the prompts, and the Notion schema."
    }
"""
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent
TEMPLATE_PATH = SKILL_DIR / "slide-magazine.html"
TOKENS_PATH = SKILL_DIR / "tokens.json"

ICLOUD_ROOT = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/@kevhov.ai/00-Post Today"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SLIDE_WIDTH = 1080
SLIDE_HEIGHT = 1350
DEVICE_SCALE = 2  # retina output, then sips downscales when converting

TOTAL_SLIDES = 8


def _accent_wrap(text: str) -> str:
    """Wrap *italic*-marked spans in an accent class for display headlines."""
    if not text:
        return ""
    return re.sub(r"\*(.+?)\*", r'<span class="accent">\1</span>', text)


def _strong_wrap(text: str) -> str:
    """Wrap **bold** in <strong> for body copy."""
    if not text:
        return ""
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)


def _render_hook(d: dict) -> tuple[str, str]:
    body = f"""
      <div class="hook-headline">{_accent_wrap(d['hook'])}</div>
      { f'<div class="hook-sub">{d.get("hook_sub","")}</div>' if d.get("hook_sub") else "" }
    """
    return body, "swipe →"


def _render_stakes(d: dict) -> tuple[str, str]:
    body = f"""
      <div class="stakes-label">the cost</div>
      <div class="stakes-headline">{_accent_wrap(d['stakes'])}</div>
    """
    return body, "keep going →"


def _render_system(d: dict) -> tuple[str, str]:
    blocks = d.get("system_blocks") or []
    blocks_html = ""
    if blocks:
        rendered = []
        for i, b in enumerate(blocks):
            rendered.append(f'<div class="block"><span class="pin"></span>{b}</div>')
            if i < len(blocks) - 1:
                rendered.append('<div class="arrow">→</div>')
        blocks_html = f'<div class="system-blocks">{"".join(rendered)}</div>'

    body = f"""
      <div class="system-label">the system</div>
      <div class="system-name">{_accent_wrap(d['system_name'])}</div>
      <div class="system-oneliner">{d.get('system_oneliner','')}</div>
      {blocks_html}
    """
    return body, "the steps →"


def _render_step(d: dict, idx: int) -> tuple[str, str]:
    step = d["steps"][idx]
    body = f"""
      <div class="step-header">
        <div class="step-badge">STEP {idx+1:02d}</div>
        <div class="step-label">of 03</div>
      </div>
      <div class="step-title">{_accent_wrap(step['title'])}</div>
      <div class="step-body">{_strong_wrap(step['body'])}</div>
    """
    right = "next step →" if idx < 2 else "the payoff →"
    return body, right


def _render_payoff(d: dict) -> tuple[str, str]:
    body = f"""
      <div class="payoff-label">what changes</div>
      <div class="payoff-headline">{_accent_wrap(d['payoff'])}</div>
    """
    return body, "one more →"


def _render_cta(d: dict) -> tuple[str, str]:
    body = f"""
      <div class="cta-label">want the build?</div>
      <div class="cta-comment">comment</div>
      <div><span class="cta-keyword">{d['keyword']}</span></div>
      <div class="cta-body">{d.get('cta_body','')}</div>
      <div class="cta-handle">@kevhov.ai</div>
    """
    return body, "save · share"


SLOT_RENDERERS = [
    ("hook",   _render_hook),
    ("stakes", _render_stakes),
    ("system", _render_system),
    ("step",   lambda d: _render_step(d, 0)),
    ("step",   lambda d: _render_step(d, 1)),
    ("step",   lambda d: _render_step(d, 2)),
    ("payoff", _render_payoff),
    ("cta",    _render_cta),
]


class Carousel:
    def __init__(self, data: dict, output_dir: Path = None):
        self._validate(data)
        self.data = data
        self.keyword = data["keyword"].upper()
        self.slug = self.keyword.lower()
        self.today = date.today().isoformat()
        self.date_label = date.today().strftime("%b %Y").upper()
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            self.output_dir = ICLOUD_ROOT / f"{self.today}-{self.slug}-carousel" / "carousel"

    @classmethod
    def from_json(cls, path, output_dir=None):
        p = Path(path)
        if p.is_dir():
            cand = p / "carousel.json"
            if not cand.exists():
                raise FileNotFoundError(f"No carousel.json in {p}")
            p = cand
        data = json.loads(p.read_text())
        # If json lives inside a reel folder, drop output next to it.
        out = output_dir or (p.parent / "carousel")
        return cls(data, output_dir=out)

    @staticmethod
    def _validate(d: dict):
        required = ["keyword", "hook", "stakes", "system_name", "steps", "payoff"]
        missing = [k for k in required if k not in d or not d[k]]
        if missing:
            raise ValueError(f"carousel.json missing required keys: {missing}")
        if len(d["steps"]) != 3:
            raise ValueError(f"steps must be exactly 3 items, got {len(d['steps'])}")
        for i, s in enumerate(d["steps"]):
            if "title" not in s or "body" not in s:
                raise ValueError(f"step {i+1} missing title or body")

    def _render_slide_html(self, slot_index: int) -> str:
        slot_class, renderer = SLOT_RENDERERS[slot_index]
        body, footer_right = renderer(self.data)
        html = TEMPLATE_PATH.read_text()
        subs = {
            "KEYWORD": self.keyword,
            "DATE": self.date_label,
            "SLIDE_INDEX": str(slot_index + 1),
            "SLIDE_INDEX_PADDED": f"{slot_index+1:02d}",
            "TOTAL_SLIDES": str(TOTAL_SLIDES),
            "TOTAL_SLIDES_PADDED": f"{TOTAL_SLIDES:02d}",
            "SLOT_CLASS": slot_class,
            "SLOT_BODY": body,
            "FOOTER_RIGHT": footer_right,
        }
        for k, v in subs.items():
            html = html.replace("{{" + k + "}}", v)
        return html

    def render(self) -> list[Path]:
        if shutil.which("sips") is None:
            raise RuntimeError("`sips` not found on PATH — required for PNG -> JPG conversion (macOS only).")
        if not Path(CHROME).exists():
            raise RuntimeError(f"Chrome not found at {CHROME}. Edit render.py CHROME constant.")

        self.output_dir.mkdir(parents=True, exist_ok=True)
        tmp_dir = Path("/tmp") / f"carousel-{self.slug}-{self.today}"
        tmp_dir.mkdir(parents=True, exist_ok=True)

        jpg_paths = []
        for i in range(TOTAL_SLIDES):
            html_path = tmp_dir / f"slide-{i+1:02d}.html"
            png_path = tmp_dir / f"slide-{i+1:02d}.png"
            jpg_path = self.output_dir / f"{i+1:02d}.jpg"

            html_path.write_text(self._render_slide_html(i))

            subprocess.run([
                CHROME, "--headless=new", "--disable-gpu",
                f"--window-size={SLIDE_WIDTH},{SLIDE_HEIGHT}",
                f"--force-device-scale-factor={DEVICE_SCALE}",
                "--hide-scrollbars",
                "--virtual-time-budget=10000",
                f"--screenshot={png_path}",
                f"file://{html_path}",
            ], check=True, capture_output=True)

            if not png_path.exists():
                raise RuntimeError(f"Chrome did not produce {png_path}")

            # PNG -> JPG (downscale-aware via sips); also resize to exact 1080x1350
            subprocess.run([
                "sips",
                "-s", "format", "jpeg",
                "-s", "formatOptions", "92",
                "-z", str(SLIDE_HEIGHT), str(SLIDE_WIDTH),
                str(png_path),
                "--out", str(jpg_path),
            ], check=True, capture_output=True)

            jpg_paths.append(jpg_path)

        return jpg_paths


def main():
    if len(sys.argv) != 2:
        print("Usage: render.py <carousel.json | reel-folder>", file=sys.stderr)
        sys.exit(2)
    car = Carousel.from_json(sys.argv[1])
    paths = car.render()
    print(f"Rendered {len(paths)} slides to {car.output_dir}")
    for p in paths:
        print(f"  {p}")


if __name__ == "__main__":
    main()
