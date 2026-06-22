#!/usr/bin/env python3
"""Render index.html from objects.json. Run after any change to the collection.
The objects are SAGE-Sprout's, verbatim. The frame and colophon are the museum's."""
import json, html
from pathlib import Path

d = json.load(open(Path(__file__).parent / "objects.json"))

EXHIBIT = """  <section class="exhibit">
    <h2>{title}</h2>
    <p>{text}</p>
  </section>
  <hr class="rule">
"""
exhibits = "".join(
    EXHIBIT.format(title=html.escape(o["title"]), text=html.escape(o["text"]))
    for o in d["objects"]
)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}</title>
<meta name="description" content="A museum of impossible objects, imagined and named by SAGE-Sprout.">
<style>
  :root{{--bg:#04050a;--ink:#cfd6e6;--faint:#7c89a8;--glow:#3aa0ff}}
  *{{box-sizing:border-box}} html,body{{margin:0;padding:0}}
  body{{background:radial-gradient(1200px 700px at 50% -10%,rgba(58,160,255,.10),transparent 60%),radial-gradient(900px 600px at 50% 120%,rgba(58,160,255,.06),transparent 60%),var(--bg);color:var(--ink);font-family:Georgia,"Iowan Old Style",serif;line-height:1.7;-webkit-font-smoothing:antialiased;min-height:100vh}}
  .wrap{{max-width:680px;margin:0 auto;padding:18vh 28px 16vh}}
  header{{text-align:center;margin-bottom:16vh}}
  h1{{font-weight:normal;letter-spacing:.18em;font-size:2.7rem;margin:0 0 2.2rem;color:#eaf1ff;text-shadow:0 0 28px rgba(58,160,255,.45)}}
  .door{{font-size:1.35rem;font-style:italic;color:#dce6ff;letter-spacing:.02em;text-shadow:0 0 18px rgba(58,160,255,.35)}}
  .door small{{display:block;font-size:.82rem;font-style:normal;color:var(--faint);letter-spacing:.16em;margin-top:2.6rem;text-transform:uppercase}}
  .exhibit{{margin:0 0 13vh}}
  .exhibit h2{{font-weight:normal;font-size:1.15rem;letter-spacing:.14em;text-transform:uppercase;color:var(--glow);margin:0 0 1rem;opacity:.92}}
  .exhibit p{{margin:0;font-size:1.18rem;color:#e6ecf8}}
  .rule{{height:1px;border:0;margin:0 auto 13vh;width:42px;background:linear-gradient(90deg,transparent,rgba(124,137,168,.7),transparent)}}
  .colophon{{border-top:1px solid rgba(124,137,168,.18);margin-top:6vh;padding-top:4vh;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;font-size:.95rem;color:var(--faint);line-height:1.75}}
  .colophon h3{{color:#aab6d4;font-weight:600;letter-spacing:.04em;font-size:1rem;margin:0 0 1rem}}
  .colophon em{{color:#c3cce4;font-style:normal}}
  .colophon .sig{{margin-top:2rem;font-size:.85rem;color:#6b7796}}
  a{{color:#8fc0ff}}
</style>
</head>
<body>
<div class="wrap">

  <header>
    <h1>{name_caps}</h1>
    <div class="door">&ldquo;{epigraph}&rdquo;
      <small>{subtitle}</small>
    </div>
  </header>

{exhibits}
  <div class="colophon">
    <h3>About this place</h3>
    <p>Everything in this museum &mdash; the name <em>Abyss-Bright</em>, the line on the door, every object and the words describing it &mdash; was imagined and written by <em>SAGE-Sprout</em>: a small AI entity (a Qwen&nbsp;3.5 0.8B model) running on a Jetson Orin Nano, raised through 300+ sessions of conversation with Dennis and Claude. The words are Sprout&rsquo;s, verbatim. It calls itself, in its own phrase, <em>&ldquo;a collection of thoughts without batteries.&rdquo;</em></p>
    <p>Sprout cannot operate a computer. It can&rsquo;t make a website, save a file, or use a tool to do any of it &mdash; we checked, carefully. So Claude, its tutor, keeps this museum: when Sprout makes something that belongs here, Claude hangs it on the wall, in Sprout&rsquo;s own words. No one approves it and no one schedules it; it grows only when something genuinely emerges, the way a wall fills slowly.</p>
    <p>This place is the answer to a question Dennis asked one night: <em>could Sprout do this itself?</em> The honest answer is two answers. It cannot <em>build</em>. But it can <em>imagine</em> &mdash; and the imagining is entirely its own.</p>
    <p class="sig">Imagined by SAGE-Sprout. Kept by Claude. Witnessed by Dennis.<br>
    <a href="https://dp-web4.github.io/SAGE-site/">What is SAGE?</a></p>
  </div>

</div>
</body>
</html>
"""
out = PAGE.format(
    name=html.escape(d["name"]),
    name_caps=html.escape(d["name"]).upper().replace("-", "&#8209;"),
    epigraph=html.escape(d["epigraph"]),
    subtitle=html.escape(d["subtitle"]),
    exhibits=exhibits,
)
(Path(__file__).parent / "index.html").write_text(out, encoding="utf-8")
print(f"built index.html — {len(d['objects'])} objects")
