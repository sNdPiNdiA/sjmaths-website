"""
SJMaths — Class 9 Science — Chapter 10 Generator
"Sound Waves: Characteristics and Applications"

Uses the existing Chapter 1 HTML/CSS/JS as the MASTER UI/UX, exactly like
Chapter 9 generator. Only chapter-specific content/data are replaced.

Chapter 10 source basis: supplied NCERT Grade 9 Science Chapter 10 text.
Coverage:
- 14 detailed concepts, each followed by a given/example block
- all 13 numbered in-text textbook check questions, placed inside the relevant concepts
- all 15 official end-of-chapter Revise, Reflect, Refine / NCERT exercise questions on the NCERT Exercises page
- 30-question quiz with explanations for EVERY option
- Basic/Standard/Advanced tests
- revision notes with mnemonics, tricks, formulae and traps
"""

from pathlib import Path
import importlib.util
import json
import html
import re

BASE = Path(__file__).resolve().parent

# Load an existing proven Chapter 1-compatible generator as the engine.
# Prefer Chapter 8 because it is the last confirmed working master in this
# project. Fall back to Chapter 9 if that file is also present.
_ENGINE_CANDIDATES = [
    # Your current folder contains this proven Chapter 9 generator.
    # Use it first so Chapter 10 does NOT depend on a missing
    # generate_chapter9_all_pages_detailed.py file.
    BASE / "generate_chapter9_all_pages.py",
    BASE / "generate_chapter8_all_pages.py",
    BASE / "generate_chapter8_all_pages_detailed.py",
    BASE / "generate_chapter9_all_pages_detailed.py",
]
_ENGINE_PATH = next((p for p in _ENGINE_CANDIDATES if p.exists()), None)
if _ENGINE_PATH is None:
    raise FileNotFoundError(
        "Could not find a working Chapter 8/9 generator engine. "
        "Expected one of: " + ", ".join(p.name for p in _ENGINE_CANDIDATES)
    )

_spec = importlib.util.spec_from_file_location(
    "chapter10_base_engine", _ENGINE_PATH
)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"Could not load engine: {_ENGINE_PATH}")
_engine = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_engine)

# ------------------------------------------------------------------
# Chapter metadata
# ------------------------------------------------------------------
CH1_FOLDER = "chapter-1-exploration-entering-world-of-secondary-science"
CH10_FOLDER = "chapter-10-sound-waves-characteristics-and-applications"
CH1 = BASE / CH1_FOLDER
CH10 = BASE / CH10_FOLDER

_engine.CH1 = CH1
_engine.CH8 = CH10
_engine.CH8_FOLDER = CH10_FOLDER
_engine.TITLE = "Sound Waves: Characteristics and Applications"
_engine.CHAPTER = 10
_engine.NEXT_FOLDER = "chapter-11-reproduction-how-life-continues"
_engine.NEXT_TITLE = "Ch 11: Reproduction — How Life Continues"
_engine.TEMPLATES = {
    "concepts": CH1 / "concepts" / "index.html",
    "ncert-exercises": CH1 / "ncert-exercises" / "index.html",
    "quiz": CH1 / "quiz" / "index.html",
    "tests": CH1 / "tests" / "index.html",
    "revision-notes": CH1 / "revision-notes" / "index.html",
}

# ------------------------------------------------------------------
# Navigation — same structure as Chapter 9 / Chapter 1
# ------------------------------------------------------------------
_engine.PAGE_NAV = {
    "concepts": (
        '<a href="../index.html" class="sj-btn"><i class="fas fa-arrow-left"></i> OVERVIEW</a>',
        '<a href="../ncert-exercises/" class="sj-btn next">NCERT EXERCISES <i class="fas fa-arrow-right"></i></a>',
    ),
    "ncert-exercises": (
        '<a href="../concepts/" class="sj-btn"><i class="fas fa-arrow-left"></i> CONCEPTS</a>',
        '<a href="../quiz/" class="sj-btn next">Quiz <i class="fas fa-arrow-right"></i></a>',
    ),
    "quiz": (
        '<a href="../ncert-exercises/" class="sj-btn"><i class="fas fa-arrow-left"></i> NCERT EXERCISES</a>',
        '<a href="../tests/" class="sj-btn next">Tests <i class="fas fa-arrow-right"></i></a>',
    ),
    "tests": (
        '<a href="../quiz/" class="sj-btn"><i class="fas fa-arrow-left"></i> Quiz</a>',
        '<a href="../revision-notes/" class="sj-btn next">Revision <i class="fas fa-arrow-right"></i></a>',
    ),
    "revision-notes": (
        '<a href="../tests/" class="sj-btn"><i class="fas fa-arrow-left"></i> Tests</a>',
        f'<a href="../../{_engine.NEXT_FOLDER}/" class="sj-btn next">{_engine.NEXT_TITLE} <i class="fas fa-arrow-right"></i></a>',
    ),
}
_engine.BOTTOM_NAV = {
    "concepts": (
        '<a href="../index.html" class="prev"><i class="fas fa-arrow-left"></i> Overview</a>',
        '<a href="../ncert-exercises/" class="next">NCERT Exercises <i class="fas fa-arrow-right"></i></a>',
    ),
    "ncert-exercises": (
        '<a href="../concepts/" class="prev"><i class="fas fa-arrow-left"></i> Concepts</a>',
        '<a href="../quiz/" class="next">Interactive Quiz <i class="fas fa-arrow-right"></i></a>',
    ),
    "quiz": (
        '<a href="../ncert-exercises/" class="prev"><i class="fas fa-arrow-left"></i> NCERT Exercises</a>',
        '<a href="../tests/" class="next">Tests <i class="fas fa-arrow-right"></i></a>',
    ),
    "tests": (
        '<a href="../quiz/" class="prev"><i class="fas fa-arrow-left"></i> Quiz</a>',
        '<a href="../revision-notes/" class="next">Revision <i class="fas fa-arrow-right"></i></a>',
    ),
    "revision-notes": (
        '<a href="../tests/" class="prev"><i class="fas fa-arrow-left"></i> Tests</a>',
        f'<a href="../../{_engine.NEXT_FOLDER}/" class="next">{_engine.NEXT_TITLE} <i class="fas fa-arrow-right"></i></a>',
    ),
}

# ------------------------------------------------------------------
# Clean textbook-style UI overrides
# ------------------------------------------------------------------
CLEAN_CONTENT_CSS = r"""
/* Chapter 10 — textbook-first content styling */
.sj-card {
    border: 1px solid #e2e7eb !important;
    border-radius: 18px !important;
    box-shadow: 0 5px 18px rgba(15, 23, 42, .045) !important;
    background: #fff !important;
}
.sj-card .sj-cheader {
    padding-bottom: 16px !important;
    margin-bottom: 20px !important;
    border-bottom: 1px solid #edf0f2 !important;
}
.sj-card .sj-cheader h2 {
    margin: 0 !important;
    font-size: 1.55rem !important;
    line-height: 1.25 !important;
    letter-spacing: -.015em !important;
}
.sj-cicon {
    background: #eef8f5 !important;
    color: #0f9d8a !important;
    border-radius: 12px !important;
}

/* Embedded textbook questions: clearly a textbook activity/check,
   without explanatory AI/meta copy. */
.sj-textbook-check {
    margin: 24px 0 8px !important;
    padding: 0 !important;
    border: 1px solid #f0d9bd !important;
    border-left: 4px solid #f39c12 !important;
    border-radius: 12px !important;
    background: #fffaf3 !important;
    overflow: hidden !important;
}
.sj-textbook-check-head {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 12px !important;
    padding: 11px 15px !important;
    background: #fff4df !important;
    border-bottom: 1px solid #f2dfc4 !important;
}
.sj-textbook-check-kicker {
    color: #a55b00 !important;
    font-size: .74rem !important;
    font-weight: 800 !important;
    letter-spacing: .04em !important;
    text-transform: uppercase !important;
}
.sj-textbook-check-number {
    color: #7a4a0b !important;
    font-weight: 800 !important;
    font-size: .82rem !important;
    white-space: nowrap !important;
}
.sj-textbook-check-question {
    padding: 16px 17px 10px !important;
    font-size: 1rem !important;
    line-height: 1.65 !important;
    color: #172033 !important;
}
.sj-textbook-check-options {
    margin: 0 17px 12px !important;
    padding: 12px 14px !important;
    border: 1px solid #eadfce !important;
    border-radius: 9px !important;
    background: #fff !important;
}
.sj-textbook-check-options-title {
    font-weight: 800 !important;
    margin-bottom: 6px !important;
    color: #263244 !important;
}
.sj-textbook-check-options ol {
    margin: 0 0 0 20px !important;
    padding: 0 !important;
}
.sj-textbook-check-answer {
    margin: 0 17px 16px !important;
    border-top: 1px dashed #e3d6c3 !important;
    padding-top: 10px !important;
}
.sj-textbook-check-answer summary {
    color: #d65a2a !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    list-style: none !important;
}
.sj-textbook-check-answer summary::-webkit-details-marker { display: none; }
.sj-textbook-check-answer summary:before {
    content: "▸";
    display: inline-block;
    margin-right: 7px;
    font-weight: 900;
}
.sj-textbook-check-answer[open] summary:before { content: "▾"; }
.sj-textbook-check-answer-body {
    margin-top: 11px !important;
    padding: 13px 14px !important;
    border-radius: 9px !important;
    background: #fff !important;
    border: 1px solid #ece7df !important;
}
.sj-textbook-check-note { display: none !important; }

/* Worked examples: distinct from checks, but not oversized. */
.concept-example-card {
    margin: 20px 0 !important;
    border: 1px solid #dce8e5 !important;
    border-left: 4px solid #0f9d8a !important;
    border-radius: 12px !important;
    background: #fbfefd !important;
    box-shadow: none !important;
}
.concept-example-card .sj-q-header {
    padding: 12px 15px !important;
    background: #f2faf8 !important;
    border-bottom: 1px solid #dceee9 !important;
}
.concept-example-card .sj-q-badge {
    color: #087e70 !important;
    font-weight: 800 !important;
}
.concept-example-card .sj-answer-content { padding: 0 15px 14px !important; }

/* NCERT exercise page: clean question-list treatment. */
.sj-ncert-card { overflow: hidden !important; }
.sj-ncert-card .sj-cheader { margin-bottom: 0 !important; }
.sj-section-subtitle {
    margin: 5px 0 0 !important;
    color: #687386 !important;
    font-size: .92rem !important;
    font-weight: 600 !important;
}
.sj-ncert-question {
    padding: 22px 2px !important;
    border-bottom: 1px solid #e9edf0 !important;
}
.sj-ncert-question:last-child { border-bottom: 0 !important; }
.sj-ncert-qtop {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    margin-bottom: 9px !important;
}
.sj-ncert-qnumber {
    color: #172033 !important;
    font-weight: 850 !important;
    font-size: 1.02rem !important;
}
.marks-badge {
    border: 1px solid #f0b6a9 !important;
    color: #c54c37 !important;
    background: #fff8f6 !important;
    border-radius: 6px !important;
    padding: 4px 8px !important;
    font-size: .76rem !important;
    font-weight: 800 !important;
}
.sj-ncert-qtext {
    color: #172033 !important;
    font-size: 1rem !important;
    line-height: 1.65 !important;
}
.sj-ncert-options {
    margin-top: 13px !important;
    padding: 12px 15px !important;
    border-radius: 9px !important;
    background: #f7f8fa !important;
    border: 1px solid #e8ebee !important;
}
.sj-ncert-options ol { margin: 6px 0 0 20px !important; }
.sj-ncert-answer {
    margin-top: 12px !important;
    padding-top: 10px !important;
    border-top: 1px dashed #dfe4e8 !important;
}
.sj-ncert-answer summary {
    color: #d65a2a !important;
    font-weight: 700 !important;
    cursor: pointer !important;
    list-style: none !important;
}
.sj-ncert-answer summary::-webkit-details-marker { display: none; }
.sj-ncert-answer summary:before {
    content: "▸";
    display: inline-block;
    margin-right: 7px;
}
.sj-ncert-answer[open] summary:before { content: "▾"; }

@media (max-width: 700px) {
    .sj-card .sj-cheader h2 { font-size: 1.28rem !important; }
    .sj-textbook-check-head { padding: 10px 12px !important; }
    .sj-textbook-check-question { padding: 13px 13px 8px !important; }
    .sj-textbook-check-options, .sj-textbook-check-answer { margin-left: 13px !important; margin-right: 13px !important; }
}
"""



FINAL_UI_CSS = r"""
/* ================================================================
   Chapter 10 final textbook UI — no meta/AI-looking presentation
   ================================================================ */
.sj-page-content { max-width: 1180px !important; margin: 0 auto !important; }

/* Concept cards */
.sj-card {
    background: #fff !important;
    border: 1px solid #e3e8ea !important;
    border-radius: 18px !important;
    box-shadow: 0 5px 18px rgba(20, 35, 45, .045) !important;
    padding: 28px 30px !important;
    margin: 0 0 22px !important;
}
.sj-card .sj-cheader {
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    padding: 0 0 17px !important;
    margin: 0 0 20px !important;
    border-bottom: 1px solid #edf0f2 !important;
}
.sj-card .sj-cheader h2 {
    font-size: 1.48rem !important;
    font-weight: 850 !important;
    color: #142033 !important;
    margin: 0 !important;
}
.sj-cicon {
    width: 42px !important;
    height: 42px !important;
    min-width: 42px !important;
    display: grid !important;
    place-items: center !important;
    border-radius: 11px !important;
    background: #eef8f5 !important;
    color: #0b9b87 !important;
}

/* Textbook checks: compact, clearly distinct from ordinary prose */
.sj-textbook-check {
    margin: 20px 0 5px !important;
    border: 1px solid #eadfcf !important;
    border-left: 4px solid #f39c12 !important;
    border-radius: 12px !important;
    background: #fffdf9 !important;
    overflow: hidden !important;
}
.sj-textbook-check-head {
    padding: 10px 14px !important;
    background: #fff7e8 !important;
    border-bottom: 1px solid #f0e2cb !important;
}
.sj-textbook-check-kicker {
    font-size: .72rem !important;
    font-weight: 850 !important;
    color: #9a5b00 !important;
    letter-spacing: .055em !important;
    text-transform: uppercase !important;
}
.sj-textbook-check-number {
    min-width: 34px !important;
    height: 26px !important;
    display: inline-grid !important;
    place-items: center !important;
    padding: 0 8px !important;
    border-radius: 13px !important;
    background: #f39c12 !important;
    color: #fff !important;
    font-size: .75rem !important;
    font-weight: 850 !important;
}
.sj-textbook-check-question {
    padding: 14px 15px 10px !important;
    font-size: .98rem !important;
    line-height: 1.62 !important;
    color: #1a2738 !important;
}
.sj-textbook-check-answer {
    margin: 0 15px 14px !important;
    padding-top: 9px !important;
    border-top: 1px dashed #e3d6c2 !important;
}
.sj-textbook-check-answer summary {
    color: #0a907e !important;
    font-size: .9rem !important;
    font-weight: 800 !important;
    cursor: pointer !important;
}
.sj-textbook-check-answer-body {
    margin-top: 10px !important;
    padding: 12px 13px !important;
    border: 1px solid #e5ecea !important;
    border-radius: 9px !important;
    background: #fbfefd !important;
}

/* Worked textbook examples */
.concept-example-card {
    margin: 20px 0 !important;
    border: 1px solid #d9e8e4 !important;
    border-left: 4px solid #0f9d8a !important;
    border-radius: 12px !important;
    background: #fbfefd !important;
    overflow: hidden !important;
    box-shadow: none !important;
}
.concept-example-card .sj-q-header {
    min-height: 46px !important;
    padding: 10px 14px !important;
    background: #f1faf7 !important;
    border-bottom: 1px solid #dcece8 !important;
}
.concept-example-card .sj-q-badge {
    color: #087e70 !important;
    font-weight: 850 !important;
    letter-spacing: .01em !important;
}
.concept-example-card .sj-q-text {
    color: #172033 !important;
    font-weight: 700 !important;
    line-height: 1.5 !important;
}
.concept-example-card .sj-answer-content {
    padding: 12px 15px 15px !important;
    color: #253246 !important;
    line-height: 1.65 !important;
}

/* NCERT: individual question cards */
.sj-ncert-card { overflow: visible !important; }
.sj-ncert-card .sj-cheader { margin-bottom: 8px !important; }
.sj-section-subtitle { color: #697586 !important; font-size: .9rem !important; margin-top: 3px !important; }
.sj-ncert-question {
    margin: 16px 0 !important;
    padding: 18px 19px 14px !important;
    border: 1px solid #e1e7e9 !important;
    border-radius: 14px !important;
    background: #fff !important;
    box-shadow: 0 3px 12px rgba(20,35,45,.035) !important;
}
.sj-ncert-question:last-child { margin-bottom: 0 !important; }
.sj-ncert-qtop {
    display:flex !important;
    align-items:center !important;
    justify-content:space-between !important;
    gap:12px !important;
    margin-bottom: 10px !important;
}
.sj-ncert-qnumber {
    width: 34px !important;
    height: 34px !important;
    display:grid !important;
    place-items:center !important;
    border-radius: 10px !important;
    background: #eef8f5 !important;
    color:#087e70 !important;
    font-weight: 850 !important;
    font-size: .82rem !important;
}
.marks-badge {
    border: 0 !important;
    background: #fff4ef !important;
    color: #c44e38 !important;
    border-radius: 7px !important;
    padding: 5px 9px !important;
    font-size: .72rem !important;
    font-weight: 850 !important;
    text-transform: uppercase !important;
    letter-spacing: .03em !important;
}
.sj-ncert-qtext {
    color:#172033 !important;
    font-size:1rem !important;
    line-height:1.62 !important;
    font-weight: 650 !important;
}
.sj-ncert-options {
    margin-top: 13px !important;
    padding: 12px 14px !important;
    border: 1px solid #e7ebed !important;
    border-radius: 9px !important;
    background: #f8fafb !important;
}
.sj-ncert-options > strong { color:#445064 !important; font-size:.83rem !important; }
.sj-ncert-options ol { margin: 7px 0 0 20px !important; padding:0 !important; }
.sj-ncert-options li { margin: 4px 0 !important; color:#273447 !important; line-height:1.5 !important; }
.sj-ncert-answer {
    margin-top: 12px !important;
    padding-top: 10px !important;
    border-top: 1px dashed #dce3e6 !important;
}
.sj-ncert-answer summary {
    color:#0b907e !important;
    font-size:.9rem !important;
    font-weight:800 !important;
    cursor:pointer !important;
    list-style:none !important;
}
.sj-ncert-answer summary::-webkit-details-marker { display:none !important; }
.sj-ncert-answer summary:before { content:'▸'; display:inline-block; margin-right:7px; }
.sj-ncert-answer[open] summary:before { content:'▾'; }
.sj-ncert-answer .sj-answer-content {
    margin-top: 10px !important;
    padding: 13px 14px !important;
    border-radius: 9px !important;
    background:#fbfefd !important;
    border:1px solid #e2ece9 !important;
    line-height:1.65 !important;
}

@media (max-width:700px) {
    .sj-card { padding:20px 16px !important; border-radius:14px !important; }
    .sj-card .sj-cheader h2 { font-size:1.28rem !important; }
    .sj-ncert-question { padding:15px 14px 12px !important; }
    .sj-textbook-check-question { padding:13px 13px 9px !important; }
}
"""

def inject_clean_content_css(doc):
    if '/* Chapter 10 — textbook-first content styling */' in doc:
        return doc
    return doc.replace('</head>', '<style id="sj-ch10-clean-content-ui">' + CLEAN_CONTENT_CSS + '</style>\\n</head>', 1)

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def e(s):
    return html.escape(str(s), quote=True)

def example(title, html_body, *, question=None, answer_label="Show Ideal Answer"):
    """Render an example INSIDE the Concepts page using the same card pattern
    used by the Chapter 6 NCERT worked-example cards.

    For textbook examples, pass question=... and the body becomes the
    expandable model answer. For ordinary concept illustrations, the body is
    shown directly inside the same visual card.
    """
    if question is not None:
        return f'''
<div class="sj-exercise-q concept-example-card">
    <div class="sj-q-header">
        <span class="sj-q-badge">{title}</span>
        <span class="sj-q-text">{question}</span>
    </div>
    <details class="sj-ideal-answer">
        <summary><i class="fas fa-book-reader"></i> {answer_label}</summary>
        <div class="sj-answer-content">
            {html_body}
        </div>
    </details>
</div>
'''

    return f'''
<div class="sj-exercise-q concept-example-card">
    <div class="sj-q-header">
        <span class="sj-q-badge">{title}</span>
        <span class="sj-q-text">Example</span>
    </div>
    <div class="sj-answer-content" style="margin-top:12px;">
        {html_body}
    </div>
</div>
'''


def textbook_example(num, question, answer_html):
    return example(f"EX 10.{num}", answer_html, question=question)

# ------------------------------------------------------------------
# DETAILED CONCEPTS — every concept has a given example immediately after it.
# ------------------------------------------------------------------
CONCEPTS = [
("1", "fa-wave-square", "Production of Sound", '''
<p>Sound is produced when an object <strong>vibrates</strong>. Vibration means periodic to-and-fro motion (oscillation) about a position of rest. A vibrating source transfers energy to the surrounding medium and creates the disturbance that we perceive as sound.</p>
<div class="sj-grid">
<div class="sj-grid-card"><h4>String / Membrane</h4><p>Plucking a stretched string or striking a membrane makes it vibrate.</p></div>
<div class="sj-grid-card"><h4>Air Column</h4><p>In a flute, vibration of the air inside the hollow pipe produces sound.</p></div>
<div class="sj-grid-card"><h4>Human Voice</h4><p>Human sound is produced by vibration of vocal cords in the larynx.</p></div>
<div class="sj-grid-card"><h4>Source</h4><p>The vibrating object that produces sound is called the <strong>source</strong> of sound.</p></div>
</div>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Sound is an everyday sensory experience and a form of energy. Sound is produced by vibrating objects. Vibrating strings, membranes, air columns and other vibrating objects can act as sound sources. In humans and some animals, sound is produced by vibration of vocal cords in the larynx.</p></div>
''', example("Concept Example", '''
<p>Stretch a rubber band across an open cardboard box and pluck it. Sound is heard while the band vibrates. When the vibration stops, the sound stops.</p>
<p><strong>Conclusion:</strong> The observation directly supports the statement <strong>“sound is produced by vibrations.”</strong></p>
<p><strong>Exam trap:</strong> Merely touching or holding an object does not necessarily produce sound; the relevant condition is vibration.</p>''')),
("2", "fa-guitar", "Tuning Fork and Evidence of Vibration", '''
<p>A <strong>tuning fork</strong> is a U-shaped metal bar with two prongs (tines) and a stem. Striking a prong gently against a soft rubber pad makes the prongs vibrate and produce a nearly single-frequency sound.</p>
<p>When a vibrating prong touches water, waves form on the water surface. This gives visible evidence that the prong is vibrating.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>A tuning fork is a U-shaped metal bar with a stem; its two sides are called prongs or tines. Striking a prong against a soft rubber pad makes it vibrate. A vibrating prong produces sound and can make waves on a water surface.</p></div>
''', example("Concept Example", '''
<p>Strike a tuning fork on a soft rubber pad and bring it near your ear: you hear sound. Touch the vibrating prong to water: ripples appear.</p>
<p><strong>Inference:</strong> both observations support the conclusion that the tuning fork produces sound because its prongs vibrate.</p>''')),
("3", "fa-arrows-to-circle", "Propagation of Sound: The Medium", '''
<p>Sound travels from its source to the listener through a <strong>medium</strong>. Sound can propagate through <strong>solids, liquids and gases</strong>. The material through which sound propagates is called the medium.</p>
<table class="sj-table"><thead><tr><th>Medium</th><th>Can sound travel?</th><th>Source-based example</th></tr></thead><tbody>
<tr><td>Solid</td><td>Yes</td><td>Knocking heard through a desk</td></tr>
<tr><td>Liquid</td><td>Yes</td><td>Submerged spoons in water</td></tr>
<tr><td>Gas</td><td>Yes</td><td>Ordinary speech through air</td></tr>
</tbody></table>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Sound can propagate through solids, liquids and gases. The material through which sound propagates is called the medium. Desk, water and air activities provide evidence that sound can travel through all three states of matter.</p></div>
''', example("Concept Example", '''
<p>If a friend scratches a desk, placing your ear against the desk lets you hear the sound through the solid. Similarly, tapping two spoons while they are submerged in water shows that sound can reach through a liquid.</p>
<p><strong>Memory line:</strong> <strong>S-L-G = Solid, Liquid, Gas</strong> — all three can carry sound.</p>''')),
("4", "fa-vacuum", "Sound Needs a Material Medium", '''
<p>A <strong>vacuum</strong> is a region with no matter/medium. Sound cannot propagate through vacuum because sound is a <strong>mechanical wave</strong> and requires particles of a medium to transmit the disturbance.</p>
<p>In the vacuum bell-jar experiment, an electric bell continues to vibrate but becomes fainter as air is removed. Near vacuum, almost no sound is heard; when air is restored, the sound returns.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>A vacuum is a space where there is no medium (matter). In the vacuum bell-jar experiment, the bell becomes fainter as air is removed even though it continues ringing. When air is let back in, the sound returns. Sound therefore needs a material medium to propagate.</p></div>
''', example("Concept Example", '''
<p>Two astronauts outside a spacecraft cannot directly hear one another's voices or the clanking of metal through the near-vacuum of space. They communicate through devices fitted into their spacesuits.</p>
<p><strong>Why?</strong> No material medium is available in the surrounding space to transmit the sound wave.</p>''')),
("5", "fa-compress-arrows-alt", "Sound Wave: Compression and Rarefaction", '''
<p>In air, a vibrating source creates alternating regions of higher and lower density. A <strong>compression (C)</strong> is a region of higher-than-average density; a <strong>rarefaction (R)</strong> is a region of lower-than-average density.</p>
<p>The disturbance moves through the medium because neighbouring particles collide and transfer the disturbance. The particles themselves only oscillate about their mean positions; they do not travel with the wave.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>A slinky demonstrates propagation of a disturbance: closely spaced and spread-out regions travel while each turn oscillates about its own position. In air, the high-density region is a compression and the low-density region is a rarefaction. The alternating disturbance travels without actual flow of the medium's particles.</p></div>
''', example("Concept Example", '''
<p>When a piston moves forward, it pushes nearby air particles closer together, creating a compression. When it moves backward, the nearby air becomes less dense, creating a rarefaction. Continuous oscillation produces <strong>C–R–C–R</strong> successions that travel through the air.</p>
<p><strong>Exam distinction:</strong> <strong>disturbance/energy travels; medium particles oscillate.</strong></p>''')),
("6", "fa-arrows-left-right", "Longitudinal and Mechanical Waves", '''
<p>In a sound wave, particles of the medium vibrate <strong>parallel</strong> to the direction of wave propagation. Such a wave is called a <strong>longitudinal wave</strong>.</p>
<p>Sound is also a <strong>mechanical wave</strong> because it requires a material medium. Mechanical waves may be longitudinal or transverse. In a transverse wave, particles vibrate perpendicular to the direction of propagation.</p>
<div class="sj-grid"><div class="sj-grid-card"><h4>Sound</h4><p>Mechanical + longitudinal + needs medium.</p></div><div class="sj-grid-card"><h4>Light</h4><p>Not mechanical; can travel through vacuum and is transverse.</p></div></div>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Sound particles vibrate parallel to the direction of propagation, so sound is longitudinal. Sound is also mechanical because it requires a material medium. Mechanical waves may be longitudinal or transverse; transverse waves have particle vibration perpendicular to propagation.</p></div>
''', example("Concept Example", '''
<p>If the wave travels to the right and the particles move back-and-forth right-left, particle vibration is parallel to propagation: the wave is <strong>longitudinal</strong>.</p>
<p>If particles move up-down while the wave travels right, the vibration is perpendicular: that is <strong>transverse</strong>.</p>''')),
("7", "fa-bolt", "Energy Carried by Sound", '''
<p>Sound is a form of <strong>energy</strong>. A vibrating source transfers energy to the surrounding medium. The vibrating particles collide with neighbouring particles, transferring the disturbance and energy onward.</p>
<p>The medium particles do not move from the source to the listener as a continuous stream. What is transmitted is the <strong>energy/disturbance</strong>.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Sound transfers energy through the medium. Vibrations of particles and collisions with neighbouring particles transfer this energy. A microphone converts sound energy into electrical energy, while a speaker converts an electrical signal into sound.</p></div>
''', example("Concept Example", '''
<p>Place grains on a tightly stretched sheet over a container and make a loud sound nearby. The sound wave makes the sheet vibrate and the grains move or jump even though the sound source never touches the sheet.</p>
<p><strong>Conclusion:</strong> sound transfers energy through the medium.</p>''')),
("8", "fa-chart-line", "Graphical Representation of a Sound Wave", '''
<p>At a fixed instant, the density of the medium varies periodically with distance from the source. A graph can show <strong>density vs distance</strong>. Above-average density represents compression; below-average density represents rarefaction.</p>
<p>The highest and lowest points of the density graph are called <strong>crest</strong> and <strong>trough</strong> respectively in the graphical representation used in the chapter.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>At a given instant, density varies periodically with distance. The graph uses average density as the reference line. Above-average density corresponds to compression; below-average density corresponds to rarefaction. The highest and lowest points are called crest and trough.</p></div>
''', example("Concept Example", '''
<p>On a density–distance graph, mark regions above the average-density line as <strong>C</strong> and regions below it as <strong>R</strong>. The distance from one corresponding point in a cycle to the next corresponding point is one wavelength.</p>
<p><strong>Graph trick:</strong> First draw/locate the average-density line; then identify C above and R below it.</p>''')),
("9", "fa-ruler-horizontal", "Wavelength, Frequency and Time Period", '''
<p><strong>Wavelength (λ)</strong> is the distance between two consecutive crests or two consecutive troughs. Its SI unit is metre (m).</p>
<p><strong>Frequency (ν)</strong> is the number of complete density oscillations per unit time. Its SI unit is hertz (Hz). <strong>Time period (T)</strong> is the time taken for one complete oscillation and is measured in seconds.</p>
<p>The key relation is <strong>ν = 1/T</strong>.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Wavelength is the distance between consecutive crests or consecutive troughs. Frequency is the number of complete density oscillations per unit time. Time period is the time for one complete oscillation. Frequency and time period obey ν = 1/T.</p></div>
''', textbook_example("1", "If there are 10 density oscillations in 2 seconds at a given position, then calculate the (i) frequency of sound wave, and (ii) its time period.", '''
<p><strong>Example 10.1:</strong> If there are 10 density oscillations in 2 seconds at a given position, then calculate the (i) frequency of sound wave, and (ii) its time period.</p>
<p><strong>Answer:</strong> Number of oscillations = 10; time taken = 2 s.</p>
<p>Frequency of sound wave = number of oscillations / time taken = 10 / 2 = <strong>5 Hz</strong>.</p>
<p>Time taken for a single density oscillation at a position = 2 s / 10 = <strong>0.2 s</strong>.</p>''')),
("10", "fa-wave-square", "Amplitude and Intensity", '''
<p>For the sound wave described in this chapter, <strong>amplitude</strong> is the maximum change in air density from the average density in a compression or rarefaction. A larger amplitude means the wave carries more energy.</p>
<p><strong>Intensity</strong> is the sound energy passing through unit area perpendicular to the propagation direction in unit time. As sound spreads over a larger area, intensity decreases with distance from the source.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Amplitude is the maximum change in air density compared with average density. Larger amplitude means more energy. Intensity is the sound energy passing through unit area perpendicular to propagation in unit time. Intensity decreases as sound spreads over a larger area.</p></div>
''', example("Concept Example", '''
<p>If a plate is struck harder, the source transfers more energy. The sound wave has larger amplitude, the sheet in the grains experiment vibrates more strongly, and the grains jump higher.</p>
<p><strong>Exam distinction:</strong> amplitude is a physical wave quantity; loudness is human perception.</p>''')),
("11", "fa-gauge-high", "Speed of Sound and v = λν", '''
<p>Wave speed is the distance travelled by a point on the wave (such as a crest) per unit time. One wavelength is covered in one time period, so:</p>
<p style="font-size:1.15rem;text-align:center;"><strong>v = λ/T = λν</strong></p>
<p>Sound travels fastest in solids, slower in liquids and slowest in gases. The chapter gives approximate values at 15 °C: steel 5000 m s<sup>−1</sup>, water 1500 m s<sup>−1</sup>, air 340 m s<sup>−1</sup>.</p>
<p>In air, speed increases with temperature and humidity. For a given medium, changing frequency changes wavelength so that <strong>v = λν</strong> remains satisfied.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>One wavelength is covered in one time period, so v = λ/T = λν. Sound is fastest in solids, slower in liquids and slowest in gases. At 15 °C, the chapter gives about 5000 m s−1 in steel, 1500 m s−1 in water and 340 m s−1 in air.</p></div>
''', textbook_example("2", "Human hearing roughly spans 20 Hz to 20 kHz. What are the corresponding wavelengths in air for these two frequencies? Use the speed of sound in air as 344 m s−1.", '''
<p><strong>Answer:</strong> Using the relation between wavelength (λ), frequency (ν), and speed (v),</p>
<p>speed of the wave = frequency × wavelength</p>
<p>Therefore, wavelength = speed of the wave / frequency.</p>
<p>(i) For ν = 20 Hz, λ = 344 m s<sup>−1</sup> / 20 s<sup>−1</sup> = <strong>17.2 m</strong>.</p>
<p>(ii) For ν = 20 kHz = 20000 Hz, λ = 344 m s<sup>−1</sup> / 20000 s<sup>−1</sup> = <strong>0.0172 m = 1.72 cm</strong>.</p>
<p>The wavelength of sound in air corresponding to the frequency (i) 20 Hz is 17.2 m, and (ii) 20000 Hz is 1.72 cm.</p>''') + "\n" + textbook_example("3", "During a thunderstorm, lightning is seen before thunder is heard because sound travels much slower than light. If the time delay between seeing the lightning flash and hearing the thunder is measured to be 5 s, estimate the distance to the lightning strike. Use the speed of sound in air as 340 m s−1. Assume that light (speed = 300000 km s−1) reaches you almost instantaneously.", '''
<p><strong>Answer:</strong> Distance = v × t = 340 m s<sup>−1</sup> × 5 s = <strong>1700 m</strong>.</p>
<p>Lightning struck about <strong>1.7 km</strong> away.</p>''') + "\n" + textbook_example("4", "From the graphical representation of a sound wave propagating in steel (Fig. 10.22), find its wavelength. Calculate its frequency and time period if the speed of sound in steel is 5000 m s−1.", '''
<p><strong>Answer:</strong> From graph (Fig. 10.22), the wavelength λ = <strong>50 m</strong>.</p>
<p>Using Eq. (10.2), the frequency of the sound wave is ν = v/λ = 5000 m s<sup>−1</sup> / 50 m = <strong>100 Hz</strong>.</p>
<p>Using Eq. (10.1), the time period of the sound wave is T = 1/ν = 1/100 Hz = <strong>0.01 s</strong>.</p>''')),
("12", "fa-ear-listen", "Human Perception: Pitch, Loudness, Timbre", '''
<p><strong>Pitch</strong> is how humans perceive frequency. Higher-frequency sounds generally have higher pitch; lower-frequency sounds have lower pitch.</p>
<p><strong>Loudness</strong> is how humans perceive amplitude. Larger amplitude generally sounds louder. Loudness is subjective, while intensity is measurable. Sound loudness is commonly expressed in <strong>decibels (dB)</strong>.</p>
<p><strong>Timbre</strong> is the quality that makes sounds from different instruments or voices distinguishable even when they have the same note and loudness. It depends on the pattern/intensity of overtones and on source shape, material and construction.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Pitch is how frequency is perceived, while loudness is how amplitude is perceived. Intensity is measurable whereas loudness depends on the listener. Timbre makes different instruments sound different at the same note and loudness because of their overtone patterns.</p></div>
''', example("Concept Example", '''
<p>A flute and a tabla can play the same musical note at the same loudness but still sound different. Their different overtone patterns give them different <strong>timbres</strong>.</p>
<p><strong>Memory:</strong> Frequency → Pitch; Amplitude → Loudness; Overtone pattern → Timbre.</p>''')),
("13", "fa-volume-high", "Audible, Infrasonic and Ultrasonic Sound", '''
<p>Humans can normally hear approximately <strong>20 Hz to 20 kHz</strong>. Frequencies below 20 Hz are <strong>infrasonic</strong>; frequencies above 20 kHz are <strong>ultrasonic</strong>.</p>
<table class="sj-table"><thead><tr><th>Range</th><th>Frequency</th><th>Example / use</th></tr></thead><tbody>
<tr><td>Infrasonic</td><td>&lt; 20 Hz</td><td>Earthquakes, volcanic eruptions, severe storms</td></tr>
<tr><td>Audible</td><td>20 Hz–20 kHz</td><td>Human hearing</td></tr>
<tr><td>Ultrasonic</td><td>&gt; 20 kHz</td><td>Ultrasonography, kidney-stone treatment, cleaning, defect detection, echolocation</td></tr>
</tbody></table>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Human hearing is approximately 20 Hz to 20 kHz. Below 20 Hz is infrasonic; above 20 kHz is ultrasonic. Ultrasound has applications including ultrasonography, kidney-stone treatment, ultrasonic welding, cleaning, defect detection and locating objects.</p></div>
''', example("Concept Example", '''
<p>15 Hz → <strong>infrasonic</strong>. 500 Hz → <strong>audible</strong>. 40 kHz = 40,000 Hz → <strong>ultrasonic</strong>.</p>
<p><strong>Boundary trap:</strong> 20 Hz and 20 kHz are included in the stated human audible range; below/above these limits are infrasound/ultrasound.</p>''')),
("14", "fa-satellite-dish", "Reflection, Echo, Reverberation, Echolocation and SONAR", '''
<p>Sound can reflect from solid or liquid surfaces and follows the same basic laws of reflection as light: angle of incidence equals angle of reflection, measured from the normal.</p>
<p>An <strong>echo</strong> is a reflected sound heard separately from the original. A time gap of at least 0.1 s is needed for separate perception. With v = 340 m s<sup>−1</sup>, minimum echo distance is <strong>17 m</strong> because the sound travels to the surface and back.</p>
<p><strong>Reverberation</strong> is persistence of sound due to multiple reflections, especially when reflections arrive with time differences less than about 0.05 s.</p>
<p><strong>Echolocation</strong> uses reflected sound to locate objects. Bats emit ultrasonic bursts. <strong>SONAR</strong> sends ultrasonic waves into water and analyses returning echoes to determine underwater-object distance, direction and speed.</p>
<div class="sj-detail"><h4>Detailed Explanation</h4><p>Sound reflects from surfaces. An echo is heard separately when the time gap is at least 0.1 s; at 340 m s−1 the minimum echo distance is 17 m. Reverberation is persistence from multiple reflections. Echolocation and SONAR use reflected sound to locate objects.</p></div>
''', textbook_example("5", "You clap in an empty corridor and hear an echo after 0.5 s. If the speed of sound in air is 340 m s−1, calculate your distance from the wall.", '''
<p><strong>Answer:</strong> Sound travels to the wall and back, thus,</p>
<p>distance from wall = <strong>v × t / 2 = 340 m s<sup>−1</sup> × 0.5 s / 2 = 85 m</strong>.</p>''') + "\n" + textbook_example("6", "A naval sonar signal sent into seawater returns after 0.90 s. The speed of sound in seawater is 1530 m s−1. How far is the object?", '''
<p><strong>Answer:</strong> Time taken for the signal to reach the object and travel back = 0.90 s.</p>
<p>Time taken to reach the object is half of above time = 0.90 s / 2 = <strong>0.45 s</strong>.</p>
<p>Thus, distance = speed × time = 1530 m s<sup>−1</sup> × 0.45 s = <strong>688.5 m</strong>.</p>''')),
]


# ------------------------------------------------------------------
# IN-CONCEPT TEXTBOOK CHECKS
# These are the numbered questions embedded inside the textbook body.
# They are NOT the official end-of-chapter NCERT exercise set.
# ------------------------------------------------------------------
def textbook_check(number, question, answer_html, *, options=None, note=None):
    option_html = ""
    if options:
        option_html = """
<div class="sj-textbook-check-options">
    <div class="sj-textbook-check-options-title">Options</div>
    <ol>
        %s
    </ol>
</div>
""" % "\n".join(f"<li>{opt}</li>" for opt in options)
    note_html = ""
    return f"""
<div class="sj-textbook-check">
    <div class="sj-textbook-check-head">
        <span class="sj-textbook-check-kicker">Check Your Understanding</span>
        <span class="sj-textbook-check-number">Q{number}</span>
    </div>
    <div class="sj-textbook-check-question">{question}</div>
    {option_html}
    <details class="sj-textbook-check-answer">
        <summary><i class="fas fa-circle-check"></i> View Answer</summary>
        <div class="sj-textbook-check-answer-body">{answer_html}</div>
    </details>
    {note_html}
</div>
"""

IN_CONCEPT_CHECKS = {
    "1": [textbook_check(
        1,
        "Explore various ways of producing sound.",
        "<p>This is an open-ended activity. Sample observations include <strong>clapping hands, plucking a rubber band, striking a tuning fork, beating a drum, blowing across an air column</strong>, or striking a metal object. In each case, a vibrating part acts as the sound-producing source.</p>",
        note="This is an in-text activity/check from the textbook, not an end-of-chapter NCERT exercise."
    ), textbook_check(
        2,
        "Make a list of different types of musical instruments and identify their vibrating parts which produce sound.",
        "<table class=\"sj-table\"><thead><tr><th>Instrument</th><th>Vibrating part</th></tr></thead><tbody><tr><td>Guitar</td><td>Strings</td></tr><tr><td>Tabla</td><td>Stretched membrane</td></tr><tr><td>Flute</td><td>Air column</td></tr><tr><td>Violin</td><td>Strings</td></tr><tr><td>Drum</td><td>Membrane</td></tr></tbody></table><p>Any scientifically correct examples are acceptable.</p>",
        note="This is the textbook's embedded activity/check."
    )],
    "4": [textbook_check(
        3,
        "Assertion (A): We cannot hear the sound of a bell ringing in a closed jar after most of the air is pumped out. <br>Reason (R): Sound requires a medium to travel.",
        "<p><strong>Correct option: (ii)</strong> Both A and R are true, and R is the correct explanation of A.</p><p>As air is removed, the material medium needed for sound propagation is reduced. Hence the bell may still vibrate, but the sound becomes very faint.</p>",
        options=["(i) Both A and R are true, but R is not the correct explanation of A.","(ii) Both A and R are true, and R is the correct explanation of A.","(iii) A is true, but R is false.","(iv) A is false, but R is true."]
    )],
    "6": [textbook_check(
        4,
        "Assertion (A): Compressions and rarefactions move through the medium. <br>Reason (R): Individual particles of the medium continuously move forward with the wave.",
        "<p><strong>Correct option: (iii)</strong> A is true, but R is false.</p><p>Compressions and rarefactions propagate through the medium. The individual particles only oscillate about their mean positions; they do not continuously move forward with the wave.</p>",
        options=["(i) Both A and R are true, but R is not the correct explanation of A.","(ii) Both A and R are true, and R is the correct explanation of A.","(iii) A is true, but R is false.","(iv) A is false, but R is true."]
    )],
    "7": [textbook_check(
        5,
        "When sound travels from a tuning fork to your ear, which of the following actually reaches your ear?",
        "<p><strong>Correct option: (ii) Energy carried by sound waves.</strong></p><p>The medium particles vibrate about their mean positions. The disturbance and energy are transferred through the medium; the same air particles near the tuning fork do not travel all the way to the ear.</p>",
        options=["(i) Air particles near the tuning fork","(ii) Energy carried by sound waves","(iii) The tuning fork material","(iv) A continuous stream of compressed air"]
    )],
    "8": [textbook_check(
        6,
        "The variation of density of the medium for two sound waves is shown in Fig. 10.17 (a) and (b). Label compression and rarefaction by C and R on it. In Fig. 10.17 (c) and (d), label the axes and draw the curves corresponding to Fig. 10.17 (a) and (b).",
        "<p><strong>Answer:</strong> Regions where density is <strong>above the average density</strong> are compressions (C), while regions where density is <strong>below the average density</strong> are rarefactions (R). For the graphs, put <strong>distance</strong> on the x-axis and <strong>density</strong> on the y-axis, with the average-density line as the reference.</p><p>The corresponding curves should reproduce the same periodic density pattern shown in the source figures.</p>",
        note="The question refers directly to the textbook's Fig. 10.17; the learner should work on that figure rather than a substitute diagram."
    )],
    "9": [textbook_check(
        7,
        "Conduct the rubber-band activity with a thick rubber band and then with a thin rubber band. Does the thin rubber band vibrate faster? If yes, how do the frequency and time period of the sound produced by the thin rubber band differ from that of the thick rubber band?",
        "<p>For the setup described, the thin rubber band can vibrate faster. A faster vibration means a <strong>higher frequency</strong> and therefore a <strong>shorter time period</strong>, because <strong>T = 1/ν</strong>.</p>",
    ), textbook_check(
        8,
        "If the frequency of a sound wave produced by an oscillating piston of a long tube filled with air is 20 Hz, then how many oscillations does the piston complete per minute?",
        "<p>Frequency = 20 oscillations s<sup>−1</sup>.</p><p>In 60 s: <strong>20 × 60 = 1200 oscillations</strong>.</p><p><strong>Answer: 1200 oscillations per minute.</strong></p>"
    ), textbook_check(
        9,
        "For the sound wave represented by the graph shown in Fig. 10.19, what is half of its wavelength?",
        "<p>From Fig. 10.19, the wavelength is <strong>3.0 cm</strong>. Therefore, half wavelength = 3.0/2 = <strong>1.5 cm</strong>.</p>"
    )],
    "11": [textbook_check(
        10,
        "Table 10.1 gives the speed of sound in steel, water and air. Compare: (i) the speed of sound in water with respect to the speed in air, and (ii) the speed of sound in steel with respect to the speed in water.",
        "<p>(i) Water with respect to air = 1500/340 = <strong>75/17 ≈ 4.41</strong>.</p><p>(ii) Steel with respect to water = 5000/1500 = <strong>10/3 ≈ 3.33</strong>.</p>",
        note="Use the approximate values given in Table 10.1 at 15 °C."
    ), textbook_check(
        11,
        "Two friends are standing along a steel fence at a distance of 340 m from each other. Calculate the time difference between the sound reaching through air and through steel. Would it be possible to distinguish between the two sounds? Use the values in Table 10.1 and 0.1 s as the minimum interval for separate hearing.",
        "<p>Through air: t<sub>air</sub> = 340/340 = <strong>1.00 s</strong>.</p><p>Through steel: t<sub>steel</sub> = 340/5000 = <strong>0.068 s</strong>.</p><p>Time difference = 1.00 − 0.068 = <strong>0.932 s</strong>.</p><p>Since 0.932 s &gt; 0.1 s, <strong>yes, the two sounds can be distinguished separately</strong>.</p>"
    )],
    "14": [textbook_check(
        12,
        "An experiment is being set up that requires echoes to arrive at least 0.2 s after the emission of sound. What minimum distance should a reflecting surface be placed at? Assume the speed of sound to be 343 m s−1.",
        "<p>The given time is the round-trip time.</p><p>d = vt/2 = (343 × 0.2)/2 = <strong>34.3 m</strong>.</p><p><strong>Minimum distance = 34.3 m.</strong></p>"
    ), textbook_check(
        13,
        "A sonar signal sent to find the depth of the ocean takes 4 s to return. What is the depth if the speed of sound in seawater is 1500 m s−1?",
        "<p>The 4 s is the round-trip time.</p><p>Depth = vt/2 = (1500 × 4)/2 = <strong>3000 m</strong>.</p><p><strong>Depth = 3000 m = 3 km.</strong></p>"
    )]
}

# Add the embedded textbook checks to the relevant concepts.
_engine.CONCEPTS = [
    (num, icon, title, body + "\n" + "\n".join(IN_CONCEPT_CHECKS.get(num, [])))
    for num, icon, title, body in _engine.CONCEPTS
]

# The Chapter 9 engine expects each concept as exactly 4 values:
# (number, icon, title, body).
# Chapter 10 concepts additionally carry a fifth value containing the
# "Given Example" block. Merge that example into the body so the proven
# Chapter 1/9 rendering function can consume the data without changing UI.
_engine.CONCEPTS = [
    (num, icon, title, body + example_html)
    if len(item) == 5
    else item
    for item in CONCEPTS
    for num, icon, title, body, *rest in [item]
    for example_html in [rest[0] if rest else ""]
]

# Append the in-concept textbook checks AFTER the example blocks have been merged.
_engine.CONCEPTS = [
    (num, icon, title, body + "\n" + "\n".join(IN_CONCEPT_CHECKS.get(num, [])))
    for num, icon, title, body in _engine.CONCEPTS
]

# ------------------------------------------------------------------
# NCERT / in-chapter + end-of-chapter coverage
# The source contains 13 numbered in-chapter questions and 15 end questions.
# We retain all 28 as separate entries.
# ------------------------------------------------------------------

def nq(n, q, ans, marks="2", options=None):
    return (n, q, options or [], ans, marks)

# ------------------------------------------------------------------
# OFFICIAL END-OF-CHAPTER NCERT EXERCISES — Q1–Q15
# These are deliberately kept separate from the 13 in-concept textbook
# checks rendered inside the Concepts page.
# ------------------------------------------------------------------
NCERT = [
    nq(1,
       "Which observation best supports the idea that sound is a mechanical wave?",
       "<p><strong>Correct option: (ii) Sound needs a medium to propagate.</strong></p><p>A mechanical wave requires a material medium for propagation. Sound cannot travel through vacuum.</p>",
       "1",
       ["(i) Sound shows reflection", "(ii) Sound needs a medium to propagate", "(iii) Sound has frequency", "(iv) Sound carries energy"]),
    nq(2,
       "For a sound wave propagating in a medium, increasing its frequency will increase its",
       "<p><strong>Correct option: (iii) number of compressions per second.</strong></p><p>Frequency is the number of complete oscillations (and hence compressions/rarefactions) passing a point per second.</p>",
       "1",
       ["(i) wavelength", "(ii) speed", "(iii) number of compressions per second", "(iv) time period"]),
    nq(3,
       "If 20 compressions pass a point in 4 seconds, the frequency is",
       "<p>Frequency = number of compressions/time = 20/4 = <strong>5 Hz</strong>.</p><p><strong>Correct option: (ii) 5 Hz.</strong></p>",
       "1",
       ["(i) 80 Hz", "(ii) 5 Hz", "(iii) 10 Hz", "(iv) 0.2 Hz"]),
    nq(4,
       "In a room, the reflected sound reaches the ear 0.05 s after its production. Will it produce an echo or reverberation? Justify your answer.",
       "<p>It will produce <strong>reverberation</strong>, not a clearly separate echo.</p><p>An echo requires a sufficiently large time gap for the reflected sound to be heard separately; the chapter gives about <strong>0.1 s</strong> for separate perception. A reflection arriving after only 0.05 s is heard as persistence/reverberation.</p>",
       "2"),
    nq(5,
       "Graphs representing two sound waves are given in Fig. 10.30. If the scales on the X and Y axes of the two graphs are the same, which of the two sound waves has (i) greater wavelength, and (ii) smaller amplitude?",
       "<p><strong>(i) Greater wavelength:</strong> the wave whose consecutive corresponding points are farther apart horizontally.</p><p><strong>(ii) Smaller amplitude:</strong> the wave whose maximum displacement from the average-density line is smaller vertically.</p><p>Use the same X- and Y-axis scales shown in Fig. 10.30 to identify the respective curves.</p>",
       "2",
       []),
    nq(6,
       "The sound waves emitted by three sources A, B and C are represented in Fig. 10.31. If the frequency of A is maximum and C is minimum, identify the corresponding curves, and mark A, B and C on them.",
       "<p>For the same horizontal distance, the curve with the <strong>greatest number of complete oscillations</strong> has the highest frequency and must be marked <strong>A</strong>. The curve with the <strong>fewest oscillations</strong> has the lowest frequency and must be marked <strong>C</strong>. The remaining curve is <strong>B</strong>.</p>",
       "2",
       []),
    nq(7,
       "Draw a graph to represent a sound wave for which the density amplitude is 3 units and wavelength is 4 cm.",
       "<p>Draw a periodic density-versus-distance graph about the average-density line. The maximum displacement from the average density should be <strong>3 units</strong> above and below the average, and one complete wavelength should occupy <strong>4 cm</strong> along the distance axis.</p><p>The supplied diagram area is a guide; the graph should be labelled with density and distance.</p>",
       "3",
       []),
    nq(8,
       "In a movie, while showing the explosion of a spacecraft in space, a flash of light is shown along with sound at the same time. What are the errors in this depiction?",
       "<p>There are two errors:</p><ol><li><strong>Sound cannot propagate through the near-vacuum of space</strong> because it requires a material medium.</li><li>Light travels much faster than sound, and light can travel through vacuum. Therefore the light and sound should not be shown as arriving together through the same vacuum path.</li></ol>",
       "3"),
    nq(9,
       "A source produces a sound wave of wavelength 3.44 m. If the wave travels with a speed of 344 m s−1, find its time period.",
       "<p>Using v = λν:</p><p>ν = v/λ = 344/3.44 = <strong>100 Hz</strong>.</p><p>Therefore, T = 1/ν = 1/100 = <strong>0.01 s</strong>.</p>",
       "2"),
    nq(10,
       "A ship searching for a sunken ship sent a sonar signal and detected an echo after 5 s. If the ultrasonic wave travels at 1525 m s−1 in seawater, approximately how far down in the ocean is the wreckage of the sunken ship located?",
       "<p>The 5 s is the round-trip time.</p><p>Depth = vt/2 = (1525 × 5)/2 = <strong>3812.5 m</strong>.</p><p><strong>Approximate depth = 3.81 km.</strong></p>",
       "2"),
    nq(11,
       "A vehicle is fitted with an ultrasonic distance sensor as part of parking assistance system which provides echolocation, while the driver is reversing the vehicle. It emits ultrasonic wave (about 40 kHz) which is reflected by the obstacle. When the warning beep starts sounding at a distance of 1.2 m from the obstacle, how much time is taken by ultrasonic wave to travel to the obstacle and come back? Assume the speed of ultrasonic wave in air to be 345 m s−1.",
       "<p>Round-trip distance = 2 × 1.2 = <strong>2.4 m</strong>.</p><p>Time = distance/speed = 2.4/345 = <strong>0.00696 s</strong> ≈ <strong>6.96 ms</strong>.</p>",
       "2"),
    nq(12,
       "The speed of sound in air is about 331 m s−1 at 0 ºC and nearly 344 m s−1 at 22 ºC. Roughly how much extra time will the sound of thunder take to travel a distance of 1720 m, if the air temperature changes from 22 ºC to 0 ºC? Assume that all other conditions remain unchanged.",
       "<p>At 22 °C: t₂₂ = 1720/344 = <strong>5.00 s</strong>.</p><p>At 0 °C: t₀ = 1720/331 ≈ <strong>5.20 s</strong>.</p><p>Extra time ≈ 5.20 − 5.00 = <strong>0.20 s</strong>.</p>",
       "3"),
    nq(13,
       "The variation of density of medium for a sound wave propagating with a speed of 340 m s−1 is shown in Fig. 10.32. Calculate the wavelength and frequency of the sound wave.",
       "<p>From Fig. 10.32, the wavelength is <strong>8 cm = 0.08 m</strong>.</p><p>Using v = λν:</p><p>ν = 340/0.08 = <strong>4250 Hz</strong>.</p><p><strong>Wavelength = 8 cm; frequency = 4250 Hz.</strong></p>",
       "2",
       []),
    nq(14,
       "The graphical representation of two sound waves A and B propagating at the same speed of 345 m s−1 is shown in Fig. 10.33. What is the wavelength of each of them? Also, calculate their frequencies.",
       "<p>From Fig. 10.33:</p><p><strong>For A:</strong> λ = 2.5 cm = 0.025 m. ν = 345/0.025 = <strong>13,800 Hz</strong>.</p><p><strong>For B:</strong> λ = 5.0 cm = 0.05 m. ν = 345/0.05 = <strong>6900 Hz</strong>.</p>",
       "3",
       []),
    nq(15,
       "Two identical sound sources are placed at A and B — one in air and one submerged in water (Fig. 10.34). Both produce sounds at the same time, which travel horizontally to the vertical side of the cliff and come back. If the time taken by the sound to return to A is 4.5 times than that of B, what is the ratio between the speeds of sound in air and water?",
       "<p>The path distance is the same for both sounds, so t ∝ 1/v.</p><p>Given t<sub>air</sub> = 4.5 t<sub>water</sub>, therefore v<sub>water</sub>/v<sub>air</sub> = 4.5.</p><p>Hence <strong>v<sub>air</sub> : v<sub>water</sub> = 1 : 4.5 = 2 : 9</strong>.</p>",
       "3",
       [])
]

# ------------------------------------------------------------------
# Inline diagrams for the figure-referenced end-of-chapter questions.
# The numbering below matches the official exercise question number.
# ------------------------------------------------------------------
def _svg(body, label):
    return f'<div class="sj-svg-diagram" role="img" aria-label="{label}"><svg viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg">{body}</svg></div>'

SVG = {
    5: _svg('''<text x="12" y="30">(a)</text><line x1="55" y1="70" x2="525" y2="70" stroke="currentColor"/><path d="M55 70 C85 25 115 25 145 70 S205 115 235 70 S295 25 325 70 S385 115 415 70 S475 25 505 70" fill="none" stroke="currentColor" stroke-width="3"/><text x="12" y="145">(b)</text><line x1="55" y1="165" x2="525" y2="165" stroke="currentColor"/><path d="M55 165 C125 35 195 35 265 165 S405 295 475 165" fill="none" stroke="currentColor" stroke-width="3"/><text x="250" y="220">Distance</text><text x="8" y="62">Density</text>''', "Fig. 10.30"),
    6: _svg('''<line x1="55" y1="115" x2="530" y2="115" stroke="currentColor" stroke-dasharray="3"/><path d="M55 115 C70 50 85 50 100 115 S130 180 145 115 S160 50 175 115 S205 180 220 115 S235 50 250 115 S280 180 295 115 S310 50 325 115 S355 180 370 115 S385 50 400 115 S430 180 445 115 S460 50 475 115 S505 180 520 115" fill="none" stroke="#ef4444" stroke-width="2.5"/><path d="M55 115 C80 60 105 60 130 115 S180 170 205 115 S230 60 255 115 S305 170 330 115 S355 60 380 115 S430 170 455 115 S480 60 505 115" fill="none" stroke="#3b82f6" stroke-width="2.5"/><path d="M55 115 C115 65 175 65 235 115 S355 165 415 115 S475 65 525 115" fill="none" stroke="#10b981" stroke-width="2.5"/><text x="8" y="30">Density</text><text x="250" y="220">Distance</text><g transform="translate(100, 15)"><line x1="0" y1="5" x2="25" y2="5" stroke="#ef4444" stroke-width="3"/><text x="32" y="9" font-size="12" font-weight="bold">Curve A (Max freq)</text><line x1="180" y1="5" x2="205" y2="5" stroke="#3b82f6" stroke-width="3"/><text x="212" y="9" font-size="12" font-weight="bold">Curve B (Mid freq)</text><line x1="360" y1="5" x2="385" y2="5" stroke="#10b981" stroke-width="3"/><text x="392" y="9" font-size="12" font-weight="bold">Curve C (Min freq)</text></g>''', "Fig. 10.31"),
    7: _svg('''<line x1="55" y1="110" x2="530" y2="110" stroke="currentColor"/><path d="M55 110 C115 30 175 30 235 110 S355 190 415 110 S535 30 595 110" fill="none" stroke="currentColor" stroke-width="3"/><text x="5" y="30">+3</text><text x="8" y="116">0</text><text x="5" y="192">−3</text><text x="250" y="220">Distance (cm), λ = 4 cm</text>''', "Required graph"),
    13: _svg('''<line x1="55" y1="110" x2="530" y2="110" stroke="currentColor"/><path d="M55 110 C135 35 215 35 295 110 S455 185 535 110" fill="none" stroke="currentColor" stroke-width="3"/><line x1="135" y1="195" x2="455" y2="195" stroke="currentColor"/><text x="265" y="218">8 cm</text><text x="10" y="35">Density</text><text x="250" y="35">Distance</text>''', "Fig. 10.32"),
    14: _svg('''<line x1="55" y1="65" x2="530" y2="65" stroke="currentColor"/><path d="M55 65 C80 25 105 25 130 65 S180 105 205 65 S255 25 280 65 S330 105 355 65 S405 25 430 65 S480 105 505 65" fill="none" stroke="currentColor" stroke-width="2.5"/><line x1="55" y1="155" x2="530" y2="155" stroke="currentColor"/><path d="M55 155 C105 75 155 75 205 155 S305 235 355 155 S455 75 505 155" fill="none" stroke="currentColor" stroke-width="2.5"/><text x="15" y="35">A</text><text x="15" y="125">B</text><text x="250" y="25">2.5 cm</text><text x="250" y="205">5.0 cm</text>''', "Fig. 10.33"),
    15: _svg('''<line x1="480" y1="25" x2="480" y2="205" stroke="currentColor" stroke-width="5"/><text x="490" y="120">Cliff</text><circle cx="90" cy="70" r="8" fill="currentColor"/><circle cx="90" cy="165" r="8" fill="currentColor"/><text x="72" y="52">A</text><text x="72" y="188">B</text><path d="M100 70 H470 M470 80 H100 M100 165 H470 M470 175 H100" fill="none" stroke="currentColor" stroke-width="2"/><text x="210" y="58">air</text><text x="210" y="153">water</text>''', "Fig. 10.34"),
}

_engine.NCERT = [(n, qtext + SVG.get(n, ""), options, ans, marks) for n, qtext, options, ans, marks in NCERT]

try:
    _engine.EXTRA_CSS = getattr(_engine, "EXTRA_CSS", "") + '.sj-detail{margin:1rem 0;padding:1rem;border-left:4px solid currentColor;border-radius:8px}.sj-svg-diagram{margin:1rem auto;padding:.75rem;max-width:680px;overflow-x:auto;border:1px solid rgba(127,127,127,.25);border-radius:10px}.sj-svg-diagram svg{display:block;width:100%;height:auto;min-height:170px}.sj-svg-diagram text{font-family:inherit;fill:currentColor}.sj-textbook-check{margin:1.25rem 0;padding:0;border:1px solid #f6c15b;border-radius:14px;background:linear-gradient(180deg,#fffaf0 0%,#ffffff 100%);overflow:hidden;box-shadow:0 5px 18px rgba(15,23,42,.06)}.sj-textbook-check-head{display:flex;justify-content:space-between;align-items:center;gap:10px;padding:10px 14px;background:#fff1cf;border-bottom:1px solid #f6c15b}.sj-textbook-check-kicker{font-size:.68rem;font-weight:900;letter-spacing:.08em;color:#9a6700}.sj-textbook-check-number{font-size:.75rem;font-weight:800;color:#7c5a00;background:#fff;border:1px solid #f6c15b;border-radius:999px;padding:4px 9px}.sj-textbook-check-title{padding:13px 16px 3px;font-weight:900;color:#7c3f00}.sj-textbook-check-question{padding:0 16px 12px;font-weight:700;line-height:1.65}.sj-textbook-check-options{margin:0 16px 12px;padding:10px 13px;background:#fff;border:1px solid #f2d48e;border-radius:9px}.sj-textbook-check-options-title{font-weight:800;margin-bottom:5px;color:#7c5a00}.sj-textbook-check-options ol{margin:0;padding-left:22px}.sj-textbook-check-answer{margin:0 16px 12px}.sj-textbook-check-answer summary{cursor:pointer;color:#0f766e;font-weight:800;padding:8px 0}.sj-textbook-check-answer-body{padding:12px 14px;background:#f0fdfa;border:1px solid #99e6dc;border-radius:9px}.sj-textbook-check-note{padding:10px 16px 14px;font-size:.82rem;color:#64748b}.sj-ncert-notice{margin:0 0 18px;padding:14px 16px;border-left:5px solid #e74c3c;border-radius:10px;background:#fff5f3;line-height:1.6}.sj-ncert-question{padding:20px 0;border-bottom:1px solid #e2e8f0}.sj-ncert-qtop{display:flex;justify-content:space-between;align-items:center;gap:12px}.sj-ncert-qnumber{font-weight:900;color:#e74c3c;font-size:.8rem;letter-spacing:.08em;text-transform:uppercase}.sj-ncert-qtext{margin-top:7px;font-size:1.02rem;font-weight:750;line-height:1.65}.sj-ncert-options{margin-top:12px;padding:12px 15px;border-radius:9px;background:#f8fafc}.sj-ncert-options ol{margin:6px 0 0;padding-left:22px}.sj-ncert-answer{margin-top:12px}.sj-ncert-answer summary{cursor:pointer;color:#0f9d8a;font-weight:800;font-size:.92rem}.sj-ncert-answer .sj-answer-content{margin-top:10px;padding:15px;border-radius:10px;background:#f8fafc;line-height:1.65}'
except Exception:
    pass

# ------------------------------------------------------------------
# QUIZ — every option receives an explanation, including wrong options.
# ------------------------------------------------------------------
def q(question, options, correct, explanations):
    assert len(options) == len(explanations), (question, options, explanations)
    assert 0 <= correct < len(options)
    return {
        "question": question,
        "options": options,
        "correctIdx": correct,
        "explanations": explanations,
    }

QUIZ = [
 q("Sound is produced when an object:", ["melts", "vibrates", "becomes heavier", "cools"], 1,
   ["Melting is a change of state and is not the defining cause of sound production.", "Correct: sound is produced by vibrating objects.", "Mass change is not required for sound production.", "Cooling is not the defining mechanism of sound production."]),
 q("Which medium cannot carry sound?", ["Steel", "Water", "Air", "Vacuum"], 3,
   ["Steel is a solid medium and sound can propagate through it.", "Water is a liquid medium and sound can propagate through it.", "Air is a gas medium and ordinarily carries sound.", "Correct: vacuum has no material medium, so sound cannot propagate through it."]),
 q("A sound wave in air is best described as:", ["A longitudinal mechanical wave", "A transverse electromagnetic wave", "A stationary wave only", "A particle stream"], 0,
   ["Correct: sound is mechanical and longitudinal in the chapter's treatment.", "Sound is not an electromagnetic wave and requires a medium.", "Sound is not restricted to stationary waves.", "Medium particles oscillate; they do not stream continuously from source to listener."]),
 q("A compression is a region of:", ["Lower-than-average density", "Higher-than-average density", "Zero density", "Constant zero pressure"], 1,
   ["Lower density is characteristic of rarefaction.", "Correct: compression is a region of higher-than-average density.", "A sound wave does not create a zero-density region in ordinary propagation.", "Compression is not defined as zero pressure."]),
 q("In a sound wave, particles of the medium:", ["Travel from source to listener", "Remain completely stationary", "Oscillate about mean positions", "Disappear after each compression"], 2,
   ["The particles do not travel with the wave as a continuous stream.", "They vibrate rather than remain perfectly stationary.", "Correct: particles oscillate about their mean positions while the disturbance travels.", "Particles remain part of the medium; they do not disappear."]),
 q("Sound is called mechanical because it:", ["Has a frequency", "Needs a material medium", "Is always loud", "Has a wavelength"], 1,
   ["Frequency is a property of waves but does not define 'mechanical'.", "Correct: mechanical waves require a material medium.", "Mechanical does not mean loud.", "Wavelength is shared by many types of waves and does not define mechanical waves."]),
 q("In a longitudinal wave, particle vibration is:", ["Parallel to propagation", "Perpendicular to propagation", "Always circular", "Zero"], 0,
   ["Correct: particle vibration is parallel to the direction of propagation.", "Perpendicular vibration describes a transverse wave.", "Circular motion is not the defining feature here.", "Particles vibrate; their vibration is not zero."]),
 q("Which quantity is transferred by a sound wave from source to listener?", ["The source particles themselves", "Energy", "The source material", "A continuous air stream"], 1,
   ["Source particles do not travel all the way to the listener.", "Correct: sound propagation transfers energy through the medium.", "The material of the source does not travel with the sound wave.", "There is no continuous stream of compressed air carrying the sound to the listener."]),
 q("The SI unit of frequency is:", ["metre", "second", "hertz", "decibel"], 2,
   ["Metre is the SI unit of wavelength.", "Second is the SI unit of time period.", "Correct: hertz (Hz) is s⁻¹, the SI unit of frequency.", "Decibel is commonly used for sound level/loudness, not SI frequency."]),
 q("The relation between frequency and time period is:", ["ν = T", "ν = 1/T", "ν = T²", "ν = λ/T"], 1,
   ["Frequency is not numerically equal to time period except in a special numerical coincidence.", "Correct: frequency and time period are reciprocals.", "Their relation is reciprocal, not squared.", "λ/T is wave speed, not frequency in general."]),
 q("If frequency increases in the same medium, wavelength generally:", ["Increases", "Decreases", "Becomes zero", "Never changes"], 1,
   ["For fixed speed, v = λν, so increasing ν requires λ to decrease.", "Correct: wavelength decreases when speed remains constant.", "Frequency increase does not make wavelength zero.", "Wavelength changes with frequency in the same medium when speed is fixed."]),
 q("Which relation gives wave speed?", ["v = λν", "v = λ/ν", "v = ν/λ", "v = T/λ"], 0,
   ["Correct: speed equals wavelength multiplied by frequency.", "λ/ν has incorrect dimensions for speed.", "ν/λ does not give speed.", "T/λ is inverse of the correct dimensional relation."]),
 q("Sound travels fastest in the chapter's comparison through:", ["Air", "Water", "Steel", "Vacuum"], 2,
   ["Air is a gas and is the slowest among these three media.", "Water carries sound faster than air but slower than steel in the stated values.", "Correct: steel is listed at about 5000 m s⁻¹.", "Sound cannot propagate through vacuum."]),
 q("At 15 °C, the approximate speed of sound in air is:", ["340 m s⁻¹", "1500 m s⁻¹", "5000 m s⁻¹", "34 m s⁻¹"], 0,
   ["Correct: the chapter table gives about 340 m s⁻¹.", "1500 m s⁻¹ is the stated approximate value for water.", "5000 m s⁻¹ is the stated approximate value for steel.", "34 m s⁻¹ is far below the chapter's air value."]),
 q("A larger sound-wave amplitude generally means:", ["Less energy", "More energy", "No energy", "Lower frequency automatically"], 1,
   ["The chapter states that larger amplitude carries more energy.", "Correct: larger amplitude corresponds to greater energy carried by the wave.", "A sound wave carries energy.", "Amplitude and frequency are different quantities; changing amplitude does not automatically determine frequency."]),
 q("Which human perception is mainly associated with frequency?", ["Pitch", "Loudness", "Timbre only", "Echo"], 0,
   ["Correct: pitch is how frequency is perceived.", "Loudness is mainly associated with amplitude/intensity perception.", "Timbre depends strongly on overtone pattern and source characteristics.", "Echo is a reflected sound phenomenon."]),
 q("Which human perception is mainly associated with amplitude?", ["Pitch", "Loudness", "Wavelength", "Frequency"], 1,
   ["Pitch is mainly related to frequency perception.", "Correct: larger amplitude is generally perceived as louder sound.", "Wavelength is a physical wave quantity, not a human perception.", "Frequency is a physical wave quantity."]),
 q("Human hearing range is approximately:", ["2–200 Hz", "20 Hz–20 kHz", "20 kHz–200 kHz", "200 Hz–2 kHz"], 1,
   ["This is not the stated human hearing range.", "Correct: approximately 20 Hz to 20 kHz.", "Frequencies above 20 kHz are ultrasonic for humans.", "This is only a small portion of the audible range."]),
 q("A 15 Hz sound is:", ["Audible to normal humans", "Ultrasonic", "Infrasonic", "A light wave"], 2,
   ["15 Hz is below the lower human hearing limit.", "Ultrasonic means above 20 kHz, not 15 Hz.", "Correct: below 20 Hz is infrasonic.", "Frequency alone here describes sound; it is not light."]),
 q("A 40 kHz sound is:", ["Infrasonic", "Audible to normal humans", "Ultrasonic", "Zero-frequency"], 2,
   ["Infrasonic means below 20 Hz.", "40 kHz is above the approximate human upper limit of 20 kHz.", "Correct: above 20 kHz is ultrasonic.", "40 kHz is a non-zero frequency."]),
 q("The minimum distance of a reflecting surface for a separate echo in air at 340 m s⁻¹ is approximately:", ["3.4 m", "17 m", "34 m", "170 m"], 1,
   ["3.4 m would correspond to a much shorter round-trip time.", "Correct: 340×0.1/2 = 17 m.", "34 m is the total round-trip distance, not the one-way distance.", "170 m is ten times the stated minimum."]),
 q("For an echo, why is vt divided by 2 when finding wall distance?", ["Because sound stops halfway", "Because sound travels to the wall and returns", "Because speed is doubled", "Because time is halved by the ear"], 1,
   ["Sound does not stop halfway.", "Correct: measured echo time is for the complete outward-and-return path.", "The speed is not doubled in the calculation.", "The ear does not halve the physical travel time."]),
 q("Reverberation is mainly due to:", ["A single vibration only", "Multiple reflections persisting after the source stops", "Vacuum", "Zero amplitude"], 1,
   ["A single vibration does not describe reverberation.", "Correct: multiple reflections can make sound persist after the source stops.", "Vacuum prevents sound propagation rather than causing reverberation.", "Zero amplitude would mean no sound energy."]),
 q("Bats locate prey using:", ["Only visible light", "Ultrasonic echolocation", "Infrasonic waves", "Radio waves"], 1,
   ["Bats are nocturnal and the chapter describes sound-based echolocation.", "Correct: bats emit ultrasonic bursts and analyse reflected echoes.", "Infrasonic waves are below 20 Hz and are not the mechanism described.", "Radio waves are not the sound mechanism described here."]),
 q("SONAR primarily uses:", ["Ultrasonic waves", "Visible light", "Infrasonic waves", "X-rays"], 0,
   ["Correct: SONAR sends ultrasonic waves into water and analyses echoes.", "Visible light is not the sound-based SONAR signal described.", "The chapter identifies ultrasonic waves for SONAR.", "X-rays are electromagnetic radiation, not SONAR sound waves."]),
 q("If a SONAR pulse returns after 0.90 s and v = 1530 m s⁻¹, the object is about:", ["688.5 m away", "1377 m away", "3060 m away", "170 m away"], 0,
   ["Correct: 1530×0.90/2 = 688.5 m.", "1377 m is approximately the full round-trip distance, not one-way distance.", "3060 m would correspond to 2 seconds at that speed without the return-time adjustment.", "170 m is not obtained from the given values."]),
 q("If 10 oscillations occur in 2 s, frequency and time period are:", ["10 Hz, 0.1 s", "5 Hz, 0.2 s", "2 Hz, 0.5 s", "20 Hz, 0.05 s"], 1,
   ["10 Hz would require 20 oscillations in 2 s.", "Correct: ν=10/2=5 Hz and T=1/5=0.2 s.", "2 Hz would mean only 4 oscillations in 2 s.", "20 Hz would mean 40 oscillations in 2 s."]),
 q("If v = 344 m s⁻¹ and ν = 20 kHz, wavelength is:", ["17.2 m", "1.72 m", "0.0172 m", "172 m"], 2,
   ["17.2 m corresponds to 20 Hz, not 20 kHz.", "1.72 m is 100 times too large.", "Correct: λ=344/20000=0.0172 m=1.72 cm.", "172 m is much too large for this frequency."]),
 q("Which quantity has unit metre?", ["Frequency", "Time period", "Wavelength", "Intensity"], 2,
   ["Frequency is measured in Hz.", "Time period is measured in seconds.", "Correct: wavelength has SI unit metre.", "Intensity is energy per unit area per unit time and is not measured in metre."]),
 q("A tone is best described in the chapter as:", ["A sound of a single frequency", "Any noise above 100 dB", "Only an ultrasonic sound", "A reflected sound"], 0,
   ["Correct: a tone is a sound of a single frequency, such as a tuning-fork sound.", "Tone is not defined by a 100 dB threshold.", "A tone need not be ultrasonic.", "A reflected sound is an echo, not necessarily a tone."]),
]
assert len(QUIZ) == 30
_engine.QUIZ = QUIZ

# ------------------------------------------------------------------
# REVISION — detailed + mnemonics/tricks as requested.
# ------------------------------------------------------------------
_engine.REVISION = '''
<section class="sj-card">
<div class="sj-cheader"><div class="sj-cicon"><i class="fas fa-bolt"></i></div><div><small style="color:#0f9d8a;font-weight:800;text-transform:uppercase;font-size:.65rem;display:block;">Master Revision</small><h2>Sound Waves — One-Glance Core</h2></div></div>
<div class="sj-grid">
<div class="sj-grid-card"><h4>Production</h4><p>Sound is produced by <strong>vibrations</strong>.</p></div>
<div class="sj-grid-card"><h4>Nature</h4><p>Sound is a <strong>mechanical longitudinal wave</strong> and needs a medium.</p></div>
<div class="sj-grid-card"><h4>Medium</h4><p>Sound travels through <strong>solids, liquids and gases</strong>, not vacuum.</p></div>
<div class="sj-grid-card"><h4>Propagation</h4><p>Energy/disturbance travels; particles oscillate about mean positions.</p></div>
</div>
</section>

<section class="sj-card">
<h2>Formula Sheet</h2>
<table class="sj-table"><thead><tr><th>Quantity</th><th>Formula / Relation</th><th>Unit</th></tr></thead><tbody>
<tr><td>Frequency</td><td><strong>ν = number of oscillations / time</strong></td><td>Hz</td></tr>
<tr><td>Time period</td><td><strong>T = 1/ν</strong></td><td>s</td></tr>
<tr><td>Wave speed</td><td><strong>v = λν = λ/T</strong></td><td>m s<sup>−1</sup></td></tr>
<tr><td>Wavelength</td><td><strong>λ = v/ν</strong></td><td>m</td></tr>
<tr><td>Echo distance</td><td><strong>d = vt/2</strong></td><td>m</td></tr>
<tr><td>Round-trip time</td><td><strong>t = 2d/v</strong></td><td>s</td></tr>
</tbody></table>
<div class="sj-ibox info"><div><strong>Most important numerical trick:</strong> If the signal goes to a wall/object and comes back, the measured time is <strong>round-trip time</strong>. Therefore divide by 2 when finding one-way distance.</div></div>
</section>

<section class="sj-card">
<h2>Mnemonics & Memory Tricks</h2>
<div class="sj-grid">
<div class="sj-grid-card"><h4>Sound's Nature</h4><p><strong>“Mechanical Needs Matter”</strong> → sound is mechanical, so it needs a material medium.</p></div>
<div class="sj-grid-card"><h4>Medium</h4><p><strong>S-L-G</strong> → Solid, Liquid, Gas. <strong>V = Vacuum → No sound.</strong></p></div>
<div class="sj-grid-card"><h4>Wave Type</h4><p><strong>Long = Along</strong> → in a longitudinal wave, particles vibrate along/parallel to propagation.</p></div>
<div class="sj-grid-card"><h4>Perception</h4><p><strong>Frequency → Pitch; Amplitude → Loudness; Overtones → Timbre.</strong></p></div>
<div class="sj-grid-card"><h4>Frequency–Time</h4><p><strong>Fast vibration = high ν = small T.</strong> Remember: <strong>ν and T are inverse friends.</strong></p></div>
<div class="sj-grid-card"><h4>Speed Order</h4><p><strong>Solid &gt; Liquid &gt; Gas</strong> for the chapter's sound-speed comparison.</p></div>
<div class="sj-grid-card"><h4>Human Hearing</h4><p><strong>20–20,000</strong> → 20 Hz to 20 kHz. Below 20 = infra; above 20 kHz = ultra.</p></div>
<div class="sj-grid-card"><h4>Echo Rule</h4><p><strong>“Go + Return = Divide by 2.”</strong> Use d = vt/2.</p></div>
</div>
</section>

<section class="sj-card">
<h2>C / R & Graph Tricks</h2>
<p><strong>Compression:</strong> density above average. <strong>Rarefaction:</strong> density below average.</p>
<p><strong>Wavelength:</strong> distance between corresponding points — C to next C, R to next R, crest to crest, or trough to trough.</p>
<p><strong>Frequency from graph:</strong> in the same distance, more complete cycles → higher frequency.</p>
<p><strong>Amplitude from graph:</strong> greater vertical displacement from average line → greater amplitude.</p>
</section>

<section class="sj-card">
<h2>High-Yield Comparisons</h2>
<table class="sj-table"><thead><tr><th>Pair</th><th>Remember</th></tr></thead><tbody>
<tr><td>Pitch vs Loudness</td><td>Pitch ↔ frequency; Loudness ↔ amplitude.</td></tr>
<tr><td>Intensity vs Loudness</td><td>Intensity is measurable; loudness is listener-dependent perception.</td></tr>
<tr><td>Echo vs Reverberation</td><td>Echo = separately heard reflection; reverberation = persistence from multiple reflections.</td></tr>
<tr><td>Audible vs Infra vs Ultra</td><td>&lt;20 Hz = infra; 20 Hz–20 kHz = audible; &gt;20 kHz = ultra.</td></tr>
<tr><td>Sound vs Light</td><td>Sound needs medium; light can travel through vacuum.</td></tr>
</tbody></table>
</section>

<section class="sj-card">
<h2>Common Exam Traps</h2>
<ol>
<li><strong>Particles do not travel with the wave.</strong> The disturbance and energy propagate.</li>
<li><strong>Vacuum:</strong> no sound, even if the source is visibly vibrating.</li>
<li><strong>Echo calculations:</strong> always check whether the given time is round-trip.</li>
<li><strong>20 Hz and 20 kHz:</strong> these are the stated boundaries of the approximate audible range.</li>
<li><strong>Frequency vs wavelength:</strong> in the same medium, increasing frequency decreases wavelength because v = λν.</li>
<li><strong>Amplitude vs frequency:</strong> changing amplitude does not automatically change frequency.</li>
<li><strong>Decibel:</strong> it is commonly used for sound loudness/level, not the SI unit of frequency.</li>
<li><strong>Reverberation:</strong> do not call every reflection an echo; separate perception matters.</li>
</ol>
</section>

<section class="sj-card">
<h2>Must-Memorise Values</h2>
<table class="sj-table"><thead><tr><th>Fact</th><th>Value</th></tr></thead><tbody>
<tr><td>Human audible range</td><td>20 Hz to 20 kHz</td></tr>
<tr><td>Air at 15 °C</td><td>≈ 340 m s<sup>−1</sup></td></tr>
<tr><td>Water at 15 °C</td><td>≈ 1500 m s<sup>−1</sup></td></tr>
<tr><td>Steel at 15 °C</td><td>≈ 5000 m s<sup>−1</sup></td></tr>
<tr><td>Air at 0 °C</td><td>≈ 331 m s<sup>−1</sup></td></tr>
<tr><td>Air at 22 °C</td><td>≈ 344 m s<sup>−1</sup></td></tr>
<tr><td>Separate echo threshold</td><td>≈ 0.1 s</td></tr>
<tr><td>Minimum echo distance at 340 m s<sup>−1</sup></td><td>≈ 17 m</td></tr>
</tbody></table>
</section>
'''

# ------------------------------------------------------------------
# Tests — same Chapter 1 engine, chapter-specific data.
# ------------------------------------------------------------------
AR = [
"(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).",
"(B) Both Assertion (A) and Reason (R) are true but Reason (R) is not the correct explanation of Assertion (A).",
"(C) Assertion (A) is true but Reason (R) is false.",
"(D) Assertion (A) is false but Reason (R) is true."
]

def mcq(question, options, idx, marks=1):
    return {"type":"mcq","marks":marks,"question":question,"options":options,"correctIdx":idx}

def ar(qtext, idx=0, marks=1):
    return {"type":"ar","marks":marks,"question":qtext,"options":AR,"correctIdx":idx}

def sub(question, answer, marks=2):
    return {"type":"subjective","marks":marks,"question":question,"sampleAnswer":answer}

def case(question, answer, marks=5):
    return {"type":"case","marks":marks,"question":question,"sampleAnswer":answer}

TESTS = {
"basic": [
 mcq("Sound is produced by:",["Vibration","Melting","Freezing","Reflection"],0),
 mcq("Sound can propagate through:",["Only gases","Only liquids","Solids, liquids and gases","Vacuum only"],2),
 mcq("A compression is a region of:",["Higher density","Lower density","Zero density","No particles"],0),
 mcq("SI unit of frequency is:",["m","s","Hz","dB"],2),
 mcq("The relation between frequency and time period is:",["ν=T","ν=1/T","ν=T²","ν=λ/T"],1),
 mcq("Human audible range is approximately:",["20 Hz–20 kHz","2 Hz–2 kHz","20 kHz–200 kHz","200 Hz–20 kHz"],0),
 mcq("Which is ultrasonic?",["15 Hz","500 Hz","20 kHz","40 kHz"],3),
 mcq("Approximate speed of sound in air at 15 °C is:",["34","340","1500","5000"],1),
 sub("Define wavelength and frequency.","Wavelength is the distance between consecutive corresponding points such as crests; frequency is the number of complete oscillations per unit time.",2),
 sub("Why can sound not travel through vacuum?","Sound is a mechanical wave and requires a material medium whose particles transmit the disturbance.",2),
],
"standard": [
 mcq("If 30 oscillations occur in 5 s, the frequency is:",["6 Hz","25 Hz","150 Hz","0.167 Hz"],0),
 mcq("If v=340 m s−1 and ν=170 Hz, wavelength is:",["2 m","0.5 m","510 m","57.8 m"],0),
 mcq("Which statement is correct?",["Particles travel with sound","Energy travels while particles oscillate","Sound travels in vacuum","Frequency equals amplitude"],1),
 mcq("For an echo after 0.4 s at 340 m s−1, wall distance is:",["68 m","136 m","170 m","34 m"],0),
 ar("Assertion: Sound is a mechanical wave.\n\nReason: Sound needs a material medium to propagate.",0),
 ar("Assertion: Increasing frequency in the same medium decreases wavelength.\n\nReason: v=λν and speed remains fixed for the given medium.",0),
 sub("Differentiate echo and reverberation.","Echo is a reflected sound heard separately after sufficient time gap. Reverberation is persistence of sound caused by multiple reflections arriving close together.",3),
 sub("Explain why lightning is seen before thunder is heard.","Light travels much faster than sound, so the light reaches the observer almost immediately while sound takes longer.",2),
 sub("A sonar pulse returns after 2 s in water at 1500 m s−1. Find depth.","Depth = vt/2 = 1500×2/2 = 1500 m.",3),
 case("A sound source has frequency 500 Hz and wavelength 0.68 m.\n\n1. Find speed. (1)\n2. Find time period. (1)\n3. Is the sound audible to humans? (1)\n4. What happens to wavelength if frequency doubles in the same medium? (1)\n5. State the key speed relation. (1)","1. v=λν=0.68×500=340 m s−1.\n2. T=1/500=0.002 s.\n3. 500 Hz lies in the audible range.\n4. Wavelength halves.\n5. v=λν.",5),
],
"advanced": [
 mcq("A density graph has wavelength 4 cm and wave speed 400 m s−1. Frequency is:",["100 Hz","1000 Hz","10,000 Hz","1600 Hz"],2),
 mcq("If a return-time measurement is used in SONAR, one-way distance is:",["vt","2vt","vt/2","v/t"],2),
 mcq("Which statement about loudness is most accurate in the chapter?",["It is identical to intensity","It is a listener-dependent perception related to amplitude","It is frequency measured in Hz","It exists only for ultrasound"],1),
 mcq("A sound wave has frequency 20 kHz in air at 344 m s−1. Its wavelength is:",["17.2 m","1.72 m","1.72 cm","0.172 cm"],2),
 ar("Assertion: The two ears help the brain locate the direction of a sound.\n\nReason: The brain compares tiny differences in arrival time at the two ears.",0),
 ar("Assertion: A soft curtain is generally a strong reflector of sound.\n\nReason: Soft porous surfaces tend to absorb sound.",3),
 sub("Explain why a larger amplitude sound can be heard from farther away initially.","Larger amplitude means more energy is carried by the sound wave. Although intensity decreases as sound spreads, a higher-energy wave can remain perceptible over a larger distance.",3),
 sub("Explain the difference between pitch, loudness and timbre.","Pitch is the perception of frequency; loudness is the perception associated mainly with amplitude; timbre is the quality determined by the pattern/intensity of overtones and source characteristics.",5),
 sub("A thunder delay is 5 s and sound speed is 340 m s−1. Estimate distance.","Distance = vt = 340×5 = 1700 m = 1.7 km, assuming light arrival is effectively instantaneous.",3),
 case("A sonar signal returns after 0.90 s in seawater where v=1530 m s−1.\n\n1. State why ultrasonic waves are used. (1)\n2. Is 0.90 s a one-way or round-trip time? (1)\n3. Calculate object distance. (1)\n4. Name the principle used by bats. (1)\n5. Name the human technology based on the same reflected-sound principle underwater. (1)","1. Ultrasonic waves are suitable for locating objects by reflected sound.\n2. It is the round-trip time.\n3. d=1530×0.90/2=688.5 m.\n4. Echolocation.\n5. SONAR.",5),
]
}
_engine.TESTS = TESTS



# Explicitly label the tab as NCERT Exercises so it cannot be confused with
# the in-concept textbook checks.
_original_replace_tbar = _engine.replace_tbar
def _chapter10_replace_tbar(doc, page_type):
    doc = _original_replace_tbar(doc, page_type)
    if page_type == "ncert-exercises":
        doc = doc.replace(">NCERT<", ">NCERT Exercises<")
        doc = doc.replace(">NCERT Solutions<", ">NCERT Exercises<")
    return doc
_engine.replace_tbar = _chapter10_replace_tbar

def concepts_html():
    blocks = []
    for num, icon, title, body in _engine.CONCEPTS:
        blocks.append(f"""
<section class="sj-card">
    <div class="sj-cheader">
        <div class="sj-cicon"><i class="fas {icon}"></i></div>
        <div>
            <h2>{num}. {title}</h2>
        </div>
    </div>
    {body}
</section>
""")
    return "\n".join(blocks)

_engine.concepts_html = concepts_html


def ncert_html():
    blocks = []
    for qno, question, options, answer, marks in _engine.NCERT:
        option_html = ""
        if options:
            lis = "\n".join(f"<li>{html.escape(str(option))}</li>" for option in options)
            option_html = f"""
<div class="sj-ncert-options">
    <strong>Options:</strong>
    <ol>{lis}</ol>
</div>
"""
        blocks.append(f"""
<div class="sj-ncert-question">
    <div class="sj-ncert-qtop">
        <div class="sj-ncert-qnumber">Q{qno}</div>
        <span class="marks-badge">{marks} Marks</span>
    </div>
    <div class="sj-ncert-qtext">{question}</div>
    {option_html}
    <details class="sj-ncert-answer">
        <summary><i class="fas fa-book-reader"></i> View Solution &amp; Marking Scheme</summary>
        <div class="sj-answer-content">{answer}</div>
    </details>
</div>
""")
    return f"""
<section class="sj-card sj-ncert-card">
    <div class="sj-cheader">
        <div class="sj-cicon" style="color:#e74c3c;"><i class="fas fa-pencil-ruler"></i></div>
        <div>
            <h2>Revise, Reflect, Refine</h2>
            <p class="sj-section-subtitle">Questions 1–15</p>
        </div>
    </div>
    {''.join(blocks)}
</section>
"""

_engine.ncert_html = ncert_html

# Inject the final UI CSS into content pages. The earlier version defined
# the stylesheet but never actually attached it to the Chapter 1 template.
_original_build_content_page = _engine.build_content_page

def build_content_page(page_type, content):
    template = _engine.TEMPLATES[page_type]
    if not template.exists():
        raise FileNotFoundError(f"Missing Chapter 1 template: {template}")
    doc = template.read_text(encoding="utf-8")
    doc = _engine.update_metadata(doc, page_type)
    doc = _engine.replace_tbar(doc, page_type)
    doc = _engine.replace_page_content(doc, content, page_type)
    doc = inject_clean_content_css(doc)
    doc = doc.replace("</head>", "<style id=\"sj-ch10-final-ui\">" + FINAL_UI_CSS + "</style>\n</head>", 1)
    marker = f"\n<!-- SJMaths Class 9 Science | Chapter 10 | Page: {page_type} -->\n"
    doc = doc.replace("<body>", "<body>" + marker, 1)
    output_dir = _engine.CH8 / page_type
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / "index.html"
    output.write_text(doc, encoding="utf-8")
    print(f"✓ {output}")

_engine.build_content_page = build_content_page

_engine.DESCRIPTIONS = {
 "concepts": "Detailed Class 9 Science Chapter 10 concepts: production and propagation of sound, sound waves, C/R, wavelength, frequency, amplitude, intensity, speed, perception, reflection, echo, reverberation, ultrasound, infrasound, echolocation and SONAR.",
 "ncert-exercises": "Official Class 9 Science Chapter 10 end-of-chapter NCERT exercise questions Q1–Q15 with model answers, calculations and marking guidance. In-concept textbook checks are kept separately on the Concepts page.",
 "quiz": "30-question Chapter 10 interactive quiz with explanations for every correct and incorrect option.",
 "tests": "Basic, Standard and Advanced Chapter 10 tests covering conceptual, numerical, assertion-reasoning and case-based questions.",
 "revision-notes": "Detailed Chapter 10 revision with formulas, mnemonics, memory tricks, graph tricks, values and common exam traps."
}

# ------------------------------------------------------------------
# Patch metadata wording from Chapter 9 engine and run it.
# ------------------------------------------------------------------
def main():
    # Execute the proven Chapter 1/Chapter 9 pipeline with Chapter 10 data.
    # The renderer uses the patched globals above. Only the engine's
    # console header is hard-coded to Chapter 9, so rewrite those labels
    # temporarily for accurate Chapter 10 output.
    import builtins

    original_print = builtins.print

    def chapter10_print(*args, **kwargs):
        converted = []
        for value in args:
            if isinstance(value, str):
                value = value.replace(
                    "SJMaths — Class 9 Science Chapter 9",
                    "SJMaths — Class 9 Science Chapter 10"
                )
                value = value.replace(
                    "Atomic Foundations of Matter",
                    "Sound Waves: Characteristics and Applications"
                )
                value = value.replace(
                    "CONTENT:     Chapter 9",
                    "CONTENT:     Chapter 10"
                )
                value = value.replace(
                    "Chapter 9 folder not found",
                    "Chapter 10 folder not found"
                )
            converted.append(value)
        original_print(*converted, **kwargs)

    builtins.print = chapter10_print
    try:
        _engine.main()
    finally:
        builtins.print = original_print


if __name__ == "__main__":
    main()