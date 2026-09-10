"""
UPSC ASO Day 57-65 Topic Page Generator
========================================
Reads GEMINI_API_KEY from environment variable.

Model Rotation (every 20 API calls):
  Calls  1-20  : gemini-3.5-flash         ("3.5 flash")
  Calls 21-40  : gemini-3.6-flash          ("3.6 flash")
  Calls 41-60  : gemini-3.7-flash          ("3.7 flash")
  Calls 61-80  : gemini-3.8-flash       ("3.8 flash")
  (beyond 80)  : cycles back to gemini-3.5-flash-lite

Usage:
    pip install google-genai
    $env:GEMINI_API_KEY = "AIza...your-key-here"
    python generate_day_pages.py
"""
import os, re, time, json, pathlib
from google import genai
from google.genai import types

# ── Load .env file if GEMINI_API_KEY is not already set ───────────────────── #
def _load_dotenv():
    script_dir = pathlib.Path(__file__).parent
    # Search in script dir then parent dir
    for candidate in [script_dir / ".env", script_dir.parent / ".env"]:
        if candidate.exists():
            for line in candidate.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    if k.strip() not in os.environ:
                        os.environ[k.strip()] = v.strip()
            break  # use first .env found

_load_dotenv()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Model IDs for "3.5 / 3.6 / 3.7 / 3.8 flash" as requested
MODEL_TIER = [
    "gemini-3.5-flash",       # 3.5 flash  - calls  1-20
    "gemini-3.6-flash",       # 3.6 flash  - calls 21-40
    "gemini-3.7-flash",       # 3.7 flash  - calls 41-60
    "gemini-3.8-flash",    # 3.8 flash  - calls 61-80
]
CALLS_PER_MODEL = 20
OUTPUT_BASE = pathlib.Path(__file__).parent
SLEEP_BETWEEN_CALLS = 4

TOPICS = [
    {"day": 57, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Relief valve - system pressure protection", "slug": "relief-valve-system-pressure-protection"},
    {"day": 57, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Actuator - linear, rotary, tandem", "slug": "actuator-linear-rotary-tandem"},
    {"day": 57, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Hydraulic fluids - MIL-O-5606, MIL-O-83282, Skydrol 500B-4, Barco 882", "slug": "hydraulic-fluids-mil-o-5606-mil-o-83282-skydrol-500b-4-barco-882"},
    {"day": 57, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Landing gear - retraction/extension, sequence valves", "slug": "landing-gear-retraction-extension-sequence-valves"},
    {"day": 57, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Brakes anti-skid, autobrake (Dunlop brake control)", "slug": "brakes-anti-skid-autobrake-dunlop-brake-control"},
    {"day": 57, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Nose wheel steering - hydraulic/electric/pneumatic", "slug": "nose-wheel-steering-hydraulic-electric-pneumatic"},
    {"day": 58, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Depressurisation - engine start sequence", "slug": "depressurisation-engine-start-sequence"},
    {"day": 58, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Cooling of hydraulic fluid - heat exchanger loop", "slug": "cooling-of-hydraulic-fluid-heat-exchanger-loop"},
    {"day": 58, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "AC/DC power generation in aircraft", "slug": "ac-dc-power-generation-in-aircraft"},
    {"day": 58, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Transformer Rectifier Unit (TRU) - 3-phase to DC", "slug": "transformer-rectifier-unit-tru-3-phase-to-dc"},
    {"day": 58, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "DC machine - lap-wound armature, EMF calculation", "slug": "dc-machine-lap-wound-armature-emf-calculation"},
    {"day": 58, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Commutator - function in DC generator", "slug": "commutator-function-in-dc-generator"},
    {"day": 59, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Compound generator - speed/packaging limitation", "slug": "compound-generator-speed-packaging-limitation"},
    {"day": 59, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Magnetically coupled coils - inductance calculation", "slug": "magnetically-coupled-coils-inductance-calculation"},
    {"day": 59, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "AC frequency - cycles per time calculation", "slug": "ac-frequency-cycles-per-time-calculation"},
    {"day": 59, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "BJT biasing - saturation voltage, base current", "slug": "bjt-biasing-saturation-voltage-base-current"},
    {"day": 59, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Logic gates AND/OR/NOT, Boolean algebra", "slug": "logic-gates-and-or-not-boolean-algebra"},
    {"day": 59, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Number system conversion - octal/decimal/binary", "slug": "number-system-conversion-octal-decimal-binary"},
    {"day": 60, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Bleed air source - high-pressure compressor", "slug": "bleed-air-source-high-pressure-compressor"},
    {"day": 60, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Air cycle refrigeration - bootstrap cycle", "slug": "air-cycle-refrigeration-bootstrap-cycle"},
    {"day": 60, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Cabin pressurisation outflow valve, differential pressure", "slug": "cabin-pressurisation-outflow-valve-differential-pressure"},
    {"day": 60, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Humidity control - dehumidifiers, separators", "slug": "humidity-control-dehumidifiers-separators"},
    {"day": 60, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Pressure regulator / unloading valve", "slug": "pressure-regulator-unloading-valve"},
    {"day": 60, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Gaseous oxygen system - high-pressure cylinders", "slug": "gaseous-oxygen-system-high-pressure-cylinders"},
    # ── DAY 61 ─────────────────────────────────────────────────────────────
    {"day": 61, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "LOX (liquid oxygen) system - combat aircraft", "slug": "lox-liquid-oxygen-system-combat-aircraft"},
    {"day": 61, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Hypoxia - symptoms, altitude thresholds", "slug": "hypoxia-symptoms-altitude-thresholds"},
    {"day": 61, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Pressure-regulating valve in O2 system", "slug": "pressure-regulating-valve-in-o2-system"},
    {"day": 61, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Fuel booster pumps - cavitation prevention", "slug": "fuel-booster-pumps-cavitation-prevention"},
    {"day": 61, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Fuel temperature at altitude - effect on system", "slug": "fuel-temperature-at-altitude-effect-on-system"},
    {"day": 61, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Engine feed pumps - purpose (aeration/cavitation)", "slug": "engine-feed-pumps-purpose-aeration-cavitation"},
    # ── DAY 62 ─────────────────────────────────────────────────────────────
    {"day": 62, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Thermal de-icing - hot bleed air system", "slug": "thermal-de-icing-hot-bleed-air-system"},
    {"day": 62, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Pneumatic boots - inflation cycle", "slug": "pneumatic-boots-inflation-cycle"},
    {"day": 62, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Windscreen wipers - limitation on plastic", "slug": "windscreen-wipers-limitation-on-plastic"},
    {"day": 62, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Windscreen misting / fogging - at altitude", "slug": "windscreen-misting-fogging-at-altitude"},
    {"day": 62, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Primary control surfaces - aileron, elevator, rudder", "slug": "primary-control-surfaces-aileron-elevator-rudder"},
    {"day": 62, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Control axes - roll (aileron), pitch (elevator), yaw (rudder)", "slug": "control-axes-roll-aileron-pitch-elevator-yaw-rudder"},
    # ── DAY 63 ─────────────────────────────────────────────────────────────
    {"day": 63, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Fly-by-wire (FBW) - first aircraft (Airbus A320)", "slug": "fly-by-wire-fbw-first-aircraft-airbus-a320"},
    {"day": 63, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "FADEC - full authority digital engine control", "slug": "fadec-full-authority-digital-engine-control"},
    {"day": 63, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Spoiler function on landing - lift dump, drag", "slug": "spoiler-function-on-landing-lift-dump-drag"},
    {"day": 63, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Flap types and effect on landing distance", "slug": "flap-types-and-effect-on-landing-distance"},
    {"day": 63, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Airspeed indicator (ASI) - pitot-static", "slug": "airspeed-indicator-asi-pitot-static"},
    {"day": 63, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Altimeter - pressure altitude, encoding", "slug": "altimeter-pressure-altitude-encoding"},
    # ── DAY 64 ─────────────────────────────────────────────────────────────
    {"day": 64, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Attitude indicator - artificial horizon", "slug": "attitude-indicator-artificial-horizon"},
    {"day": 64, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Heading indicator - directional gyro", "slug": "heading-indicator-directional-gyro"},
    {"day": 64, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Turn coordinator / turn and slip indicator", "slug": "turn-coordinator-turn-and-slip-indicator"},
    {"day": 64, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Vertical speed indicator (VSI)", "slug": "vertical-speed-indicator-vsi"},
    {"day": 64, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Manifold pressure gauge - fuel/oil pressure instrument", "slug": "manifold-pressure-gauge-fuel-oil-pressure-instrument"},
    {"day": 64, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "Ratiometer pressure indicator", "slug": "ratiometer-pressure-indicator"},
    # ── DAY 65 ─────────────────────────────────────────────────────────────
    {"day": 65, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "ADF - loop antenna, sense antenna, bearing indicator", "slug": "adf-loop-antenna-sense-antenna-bearing-indicator"},
    {"day": 65, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "VOR - ground transmitter, OBS, CDI, short-range", "slug": "vor-ground-transmitter-obs-cdi-short-range"},
    {"day": 65, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "ILS localizer, glideslope, marker beacons (3 transmitters)", "slug": "ils-localizer-glideslope-marker-beacons-3-transmitters"},
    {"day": 65, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "DME - UHF range (960-1215 MHz), receiving range", "slug": "dme-uhf-range-960-1215-mhz-receiving-range"},
    {"day": 65, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "GPS - pseudo-range concept, satellite geometry", "slug": "gps-pseudo-range-concept-satellite-geometry"},
    {"day": 65, "subject": "Aircraft Systems and Avionics", "phase": "Phase 3: Systems and Applied", "title": "GPS receiver components - antenna, processor, clock", "slug": "gps-receiver-components-antenna-processor-clock"},
]

SYSTEM_INSTRUCTION = (
    "You are an expert UPSC Air Safety Officer (ASO) exam content writer. "
    "Your content is concise, factually precise, uses bullet points, tables, mnemonics, "
    "tips and tricks. You write for aspirants from basics to advanced level. "
    "Do NOT use long paragraphs. Keep each section brief and punchy. "
    "Output only the raw HTML content (no markdown fences, no `html wrapper)."
)

HTML_BOILERPLATE_TOP = """<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Day __DAY__: __TITLE__ | UPSC Air Safety Officer (ASO) Study Hub</title>
    <meta name="description" content="Concise UPSC ASO study module for __TITLE__ - Day __DAY__. Includes theory, tables, mnemonics, 10 MCQs, and mini test.">
    <link rel="canonical" href="https://sjmaths.com/upsc-aso/day-__DAY__/__SLUG__/">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=a88cc396">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=2b8ae814">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=dd2cffe9">
    <script>
    MathJax = {
      tex: { inlineMath: [['$','$'],['\\(','\\)']], displayMath: [['',''],['\\[','\\]']], processEscapes: true },
      options: { ignoreHtmlClass: 'tex2jax_ignore', processHtmlClass: 'tex2jax_process' }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        :root { --glass-bg:rgba(255,255,255,0.96); --glass-border:rgba(255,255,255,0.25); --shadow-lg:0 10px 30px -5px rgba(30,60,114,0.12); --accent-gradient:linear-gradient(135deg,#1e3c72,#2a5298,#d4af37); }
        .module-container { max-width:1100px; margin:2rem auto; padding:2rem 1.5rem; }
        .breadcrumb-nav { display:flex; align-items:center; gap:.5rem; font-size:.9rem; color:#718096; margin-bottom:1.5rem; }
        .breadcrumb-nav a { color:#2b6cb0; text-decoration:none; }
        .breadcrumb-nav a:hover { text-decoration:underline; }
        .module-header { background:var(--glass-bg); border:1px solid var(--glass-border); border-radius:1.25rem; padding:2rem; box-shadow:var(--shadow-lg); margin-bottom:2rem; position:relative; overflow:hidden; }
        .module-header::before { content:''; position:absolute; top:0; left:0; width:5px; height:100%; background:var(--accent-gradient); }
        .module-header h1 { font-family:'Outfit',sans-serif; font-size:2.2rem; font-weight:800; color:#1a202c; margin-bottom:.75rem; }
        .module-badges { display:flex; align-items:center; gap:.75rem; flex-wrap:wrap; }
        .badge-tag { font-size:.8rem; font-weight:700; padding:4px 12px; border-radius:20px; background:rgba(30,60,114,.08); color:#1e3c72; }
        .main-tabs { display:flex; gap:1rem; margin-bottom:2rem; border-bottom:2px solid #e2e8f0; padding-bottom:.5rem; flex-wrap:wrap; }
        .tab-button { background:transparent; border:none; outline:none; font-family:'Outfit',sans-serif; font-size:1.05rem; font-weight:700; color:#718096; padding:.75rem 1.5rem; cursor:pointer; border-radius:10px; transition:all .3s ease; display:flex; align-items:center; gap:.6rem; }
        .tab-button:hover { color:#1e3c72; background:rgba(30,60,114,.05); }
        .tab-button.active { color:#fff; background:var(--accent-gradient); box-shadow:0 4px 15px rgba(30,60,114,.25); }
        .tab-content-panel { display:none; animation:fadeIn .4s ease-out; }
        .tab-content-panel.active { display:block; }
        .step-card { background:var(--glass-bg); border:1px solid var(--glass-border); border-radius:1rem; padding:1.75rem; box-shadow:0 4px 12px rgba(0,0,0,.03); margin-bottom:1.75rem; }
        .step-title { font-family:'Outfit',sans-serif; font-size:1.3rem; font-weight:700; color:#1e3c72; margin-bottom:1rem; display:flex; align-items:center; gap:.6rem; border-bottom:1px solid #edf2f7; padding-bottom:.6rem; }
        .step-title i { color:#d4af37; }
        .content-box { font-size:1rem; line-height:1.75; color:#2d3748; }
        .formula-card { background:#f7fafc; border-left:4px solid #3182ce; padding:1.25rem; border-radius:8px; font-family:'Fira Code',monospace; margin:1.25rem 0; overflow-x:auto; }
        .mnemonic-box { background:#fffbea; border-left:4px solid #d4af37; padding:1rem 1.25rem; border-radius:8px; margin:1rem 0; }
        .tip-box { background:#ebf8ff; border-left:4px solid #3182ce; padding:1rem 1.25rem; border-radius:8px; margin:1rem 0; }
        table.aso-table { width:100%; border-collapse:collapse; margin:1rem 0; font-size:.92rem; }
        table.aso-table th { background:rgba(30,60,114,.08); color:#1e3c72; font-weight:700; padding:10px 12px; text-align:left; border:1px solid #e2e8f0; }
        table.aso-table td { padding:9px 12px; border:1px solid #e2e8f0; vertical-align:top; }
        table.aso-table tr:nth-child(even) { background:#f8fafc; }
        .mcq-card { background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:1.5rem; margin-bottom:1.5rem; box-shadow:0 2px 8px rgba(0,0,0,.02); }
        .mcq-question { font-weight:600; font-size:1.05rem; color:#1a202c; margin-bottom:1rem; line-height:1.6; }
        .mcq-options { display:flex; flex-direction:column; gap:.6rem; margin-bottom:1rem; }
        .mcq-option { padding:.75rem 1rem; border:1px solid #cbd5e0; border-radius:8px; cursor:pointer; transition:all .2s ease; font-size:.95rem; }
        .mcq-option:hover { border-color:#3182ce; background:#ebf8ff; }
        .mcq-option.correct { border-color:#38a169; background:#c6f6d5; color:#22543d; font-weight:600; }
        .mcq-option.incorrect { border-color:#e53e3e; background:#fed7d7; color:#742a2a; }
        .explanation-box { display:none; background:#f7fafc; border:1px solid #e2e8f0; padding:1rem 1.25rem; border-radius:8px; margin-top:1rem; font-size:.92rem; color:#4a5568; line-height:1.6; }
        .check-btn { background:#3182ce; color:#fff; border:none; padding:.5rem 1.25rem; border-radius:6px; font-weight:600; cursor:pointer; transition:background .2s ease; }
        .check-btn:hover { background:#2b6cb0; }
        @keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
    </style>
<script type="application/ld+json" data-seo-schema="true">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"UPSC ASO","item":"https://sjmaths.com/upsc-aso/"},{"@type":"ListItem","position":3,"name":"Day __DAY__","item":"https://sjmaths.com/upsc-aso/day-__DAY__/"},{"@type":"ListItem","position":4,"name":"__TITLE__","item":"https://sjmaths.com/upsc-aso/day-__DAY__/__SLUG__/"}]}
</script>
</head>
<body>
    <div id="header-container"></div>
    <main class="module-container" id="main-content">
        <div class="breadcrumb-nav">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size:.7rem"></i>
            <a href="/upsc-aso/">UPSC ASO Hub</a> <i class="fas fa-chevron-right" style="font-size:.7rem"></i>
            <span>Day __DAY__ &bull; __TITLE__</span>
        </div>
        <div class="module-header">
            <h1>__TITLE__</h1>
            <div class="module-badges">
                <span class="badge-tag"><i class="fas fa-calendar-day"></i> Day __DAY__ of 129</span>
                <span class="badge-tag"><i class="fas fa-book"></i> __SUBJECT__</span>
                <span class="badge-tag"><i class="fas fa-layer-group"></i> __PHASE__</span>
                <span class="badge-tag"><i class="far fa-clock"></i> 60-90 min Master Cycle</span>
            </div>
        </div>
        <div class="main-tabs">
            <button class="tab-button active" onclick="switchTab('tab-concepts',this)"><i class="fas fa-book-open"></i> 1. Concepts &amp; Theories</button>
            <button class="tab-button" onclick="switchTab('tab-practice',this)"><i class="fas fa-tasks"></i> 2. UPSC Level Practice Questions (10 MCQs)</button>
            <button class="tab-button" onclick="switchTab('tab-minitest',this)"><i class="fas fa-vial"></i> 3. Mini Test &amp; Active Recall</button>
        </div>
"""

HTML_BOILERPLATE_BOTTOM = """
    </main>
    <script>
        function switchTab(tabId, btn) {
            document.querySelectorAll('.tab-button').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content-panel').forEach(p => p.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        }
        let selectedOptions = {};
        function selectOption(el, qId) {
            const parent = el.closest('.mcq-options');
            parent.querySelectorAll('.mcq-option').forEach(o => o.classList.remove('correct','incorrect'));
            selectedOptions[qId] = el;
        }
        function checkMCQ(qId, correctOpt) {
            const selected = selectedOptions[qId];
            const explain = document.getElementById('explain-' + qId);
            if (!selected) { alert('Please select an option first!'); return; }
            if (selected.getAttribute('data-opt') === correctOpt) { selected.classList.add('correct'); }
            else { selected.classList.add('incorrect'); }
            if (explain) { explain.style.display = 'block'; }
        }
    </script>
    <script type="module">
        const load = async () => { try { await import("/assets/js/firebase-analytics-only.min.js?v=b9396571"); } catch(e) { console.debug("Analytics deferred"); } };
        if ('requestIdleCallback' in window) requestIdleCallback(load); else setTimeout(load, 3000);
    </script>
    <button id="backToTop" class="back-to-top" aria-label="Back to Top"><i class="fas fa-arrow-up"></i></button>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=3aa5cdc4" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=c199667b" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=2bd12836" defer data-cfasync="false"></script>
    <script type="module" src="/assets/js/require-auth.min.js?v=d0c03e2d"></script>
</body>
</html>"""

def build_prompt(topic):
    d = topic['day']
    t = topic['title']
    s = topic['subject']
    ph = topic['phase']
    sl = topic['slug']
    return f"""Generate ONLY the inner body content (3 tab panels) for a UPSC ASO study page.
Topic: {t}
Day: {d} of 129 | Subject: {s} | Phase: {ph}

Output EXACTLY this structure (no extra wrappers):

<div id="tab-concepts" class="tab-content-panel active">
  [5 step-cards as described below]
</div>
<div id="tab-practice" class="tab-content-panel">
  [step-card with 10 MCQs]
</div>
<div id="tab-minitest" class="tab-content-panel">
  [step-cards with 3 Grand Test MCQs + Error Analysis + Quick Revision]
</div>

CONTENT RULES:
- Step 1 Understand: 3 short bullet-point paragraphs (basics to advanced). NO long prose.
- Step 2 Learn: Key formulas in LaTeX ($...$), at least 1 comparison table (class="aso-table"), categorized lists.
- Step 3 Memorize: bullet facts + 1 MNEMONIC in <div class="mnemonic-box"> + 1-2 <div class="tip-box"> exam tips.
- Step 4 Aviation Application: 2-3 real examples with <h3> headings. Aircraft/ASO context.
- Step 5 UPSC Focus: frequently asked patterns, common traps, exam shortcuts in bullets.
- Tab 2: EXACTLY 10 MCQs. IDs: d{d}01 to d{d}10. Each has 4 options, check-btn, explanation-box.
- Tab 3: EXACTLY 3 Grand Test MCQs (IDs d{d}51-d{d}53) + Error Analysis section + Quick Revision cheat-sheet box.
- MCQ format: <div class="mcq-card"><div class="mcq-question">Qn. ...</div><div class="mcq-options"><div class="mcq-option" data-opt="A" onclick="selectOption(this,d{d}0n)">A) ...</div>...</div><button class="check-btn" onclick="checkMCQ(d{d}0n,'X')">Check Answer</button><div class="explanation-box" id="explain-d{d}0n">...</div></div>
- Use step-card class for each section card. Use step-title class for section headings with <i class="fas fa-..."></i> icon.
- Output ONLY the 3 div panels. No DOCTYPE, no head, no body tags. No markdown.
"""

def get_model(call_index):
    """Cycles through MODEL_TIER every CALLS_PER_MODEL calls (3.5->3.6->3.7->3.8->3.5...)."""
    tier = (call_index // CALLS_PER_MODEL) % len(MODEL_TIER)
    return MODEL_TIER[tier]

def sanitize(raw):
    """Strip accidental markdown ```html ... ``` fences the model may add."""
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-zA-Z]*\r?\n?", "", raw)
        raw = re.sub(r"\r?\n?```$", "", raw)
    return raw.strip()

def generate_page(topic, call_index):
    model_name = get_model(call_index)
    print(f"  [Call {call_index+1}] Model: {model_name}")
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model=model_name,
        contents=build_prompt(topic),
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.6,
            max_output_tokens=8192,
        ),
    )
    inner = sanitize(response.text)
    top = (HTML_BOILERPLATE_TOP
           .replace("__DAY__", str(topic['day']))
           .replace("__TITLE__", topic['title'])
           .replace("__SUBJECT__", topic['subject'])
           .replace("__PHASE__", topic['phase'])
           .replace("__SLUG__", topic['slug']))
    return top + "\n" + inner + "\n" + HTML_BOILERPLATE_BOTTOM

def save_page(topic, html):
    out_dir = OUTPUT_BASE / f"day-{topic['day']}" / topic["slug"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "index.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"  Saved: day-{topic['day']}/{topic['slug']}/index.html")

def load_progress():
    pf = OUTPUT_BASE / ".gen_progress.json"
    if pf.exists():
        return set(json.loads(pf.read_text(encoding="utf-8")))
    return set()

def save_progress(done):
    pf = OUTPUT_BASE / ".gen_progress.json"
    pf.write_text(json.dumps(sorted(done), indent=2), encoding="utf-8")

def main():
    if not GEMINI_API_KEY:
        raise SystemExit(
            "ERROR: GEMINI_API_KEY environment variable is not set.\n"
            "  Run: $env:GEMINI_API_KEY = 'your-api-key'"
        )
    done = load_progress()
    call_index = len(done)
    print(f"\n{'='*60}")
    print(f"UPSC ASO Day 57-65 Generator | {len(TOPICS)} topics total")
    print(f"Already done: {len(done)} | Remaining: {len(TOPICS)-len(done)}")
    print(f"Models: 3.5={MODEL_TIER[0]}, 3.6={MODEL_TIER[1]}")
    print(f"        3.7={MODEL_TIER[2]}, 3.8={MODEL_TIER[3]}")
    print(f"{'='*60}\n")
    for i, topic in enumerate(TOPICS):
        key = f"day{topic['day']}-{topic['slug']}"
        if key in done:
            print(f"[{i+1}/{len(TOPICS)}] SKIP: {topic['title']}")
            continue
        print(f"\n[{i+1}/{len(TOPICS)}] Generating: Day {topic['day']} - {topic['title']}")
        for attempt in range(2):
            try:
                html = generate_page(topic, call_index)
                save_page(topic, html)
                done.add(key)
                save_progress(done)
                call_index += 1
                print(f"  Done. Sleeping {SLEEP_BETWEEN_CALLS}s...")
                time.sleep(SLEEP_BETWEEN_CALLS)
                break
            except Exception as exc:
                print(f"  ERROR (attempt {attempt+1}): {exc}")
                if attempt == 0:
                    print("  Retrying in 30s...")
                    time.sleep(30)
                else:
                    print("  Skipping this topic.")
    print(f"\nDone! {len(done)}/{len(TOPICS)} pages generated.")

if __name__ == "__main__":
    main()
