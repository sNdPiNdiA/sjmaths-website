import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { moveBreadcrumbsToTop } = require('./apply_standard_top_breadcrumbs.cjs');

// ── Load .env ─────────────────────────────────────────────────────────────── //
function loadEnv() {
  let key = process.env.GEMINI_API_KEY;
  if (!key) {
    for (const p of ['.env', '../.env', 'upsc-aso/.env']) {
      if (fs.existsSync(p)) {
        for (const line of fs.readFileSync(p, 'utf8').split('\n')) {
          const m = line.match(/^\s*GEMINI_API_KEY\s*=\s*(.*)\s*$/);
          if (m) {
            key = m[1].trim().replace(/^['"]|['"]$/g, '');
            break;
          }
        }
      }
      if (key) break;
    }
  }
  return key;
}

const GEMINI_API_KEY = loadEnv();
if (!GEMINI_API_KEY) {
  console.error('ERROR: GEMINI_API_KEY not found in environment or .env file.');
  process.exit(1);
}

// ── Model Configuration & Persistent Call Tracker ───────────────────────── //
// User Specification: Use ONLY gemini-3.5-flash-lite with maximum output tokens (65,536)
const MODEL_NAME = 'gemini-3.5-flash-lite';
const MAX_OUTPUT_TOKENS = 65536;
const CALL_COUNT_FILE = path.resolve('upsc-aso/.api_call_count.json');

export function getPersistentCallCount() {
  try {
    if (fs.existsSync(CALL_COUNT_FILE)) {
      const data = JSON.parse(fs.readFileSync(CALL_COUNT_FILE, 'utf8'));
      return data.callCount || 0;
    }
  } catch (e) {}
  return 0;
}

export function incrementPersistentCallCount() {
  const current = getPersistentCallCount() + 1;
  fs.writeFileSync(CALL_COUNT_FILE, JSON.stringify({ callCount: current, lastUpdated: new Date().toISOString() }, null, 2), 'utf8');
  return current;
}

export function getModelForCallIndex() {
  return MODEL_NAME;
}

// ── Master System Instruction based on User Specification ─────────────────── //
const SYSTEM_PROMPT = `You are an expert aviation educator, UPSC Air Safety Officer exam mentor, instructional designer, aviation safety specialist, and senior frontend/UI/UX developer for SJMaths.com.

Your task is to generate a complete, standalone, production-ready, highly interactive HTML study page for the UPSC Air Safety Officer (ASO) DGCA examination.

CRITICAL PEDAGOGICAL MANDATE (NO SHORTCUTS, NO CONDENSED FORMULA CARDS):
The candidate is aiming for TOP RANK in the UPSC Air Safety Officer recruitment exam.
DO NOT JUST GIVE FORMULAS! A formula box alone is strictly forbidden and completely unacceptable.
The study notes in Tab 1 MUST BE EXHAUSTIVE, DETAILED, TEXTBOOK-GRADE, AND THOROUGH.

MANDATORY 8-ELEMENT REQUIREMENT FOR EVERY SINGLE SUBTOPIC:
For EVERY subtopic in the list, you MUST generate an independent, full-length concept card (<div class="concept-card">).
NEVER COMBINE SUBTOPICS! If 7 subtopics are listed, you MUST write 7 complete, distinct concept cards in Tab 1.
Each subtopic card MUST contain:
1. FORMAL TECHNICAL DEFINITION: Clear, rigorous scientific/engineering definition in a callout box.
2. BASIC CONCEPT & PHYSICAL MECHANISM: Explain the 'why' at molecular and continuum levels (e.g. continuum limit, mean free path, fluid parcel equilibrium, stress tensor).
3. MATHEMATICAL DERIVATION & EQUATIONS: Step-by-step mathematical derivation showing how the equation is obtained, with every single variable defined.
4. DIMENSIONS & UNITS: Fundamental dimensions in [M, L, T, \\theta], SI units, CGS units, and metric/imperial conversion factors.
5. REFERENCE VALUES TABLE: Standard engineering data for atmospheric air, Jet A-1, Avgas 100LL, Skydrol LD-4, water, and aircraft structural fluids.
6. AIRCRAFT APPLICATION & AIR SAFETY OFFICER CONNECTION: Real aircraft systems (Fly-By-Wire flight controls, fuel feed systems, pitot-static probes, turbine lubrication, de-icing holdover times, DGCA CAR Section 2 airworthiness compliance, real accident case studies).
7. UPSC TRAPS & COMMON MISCONCEPTIONS: Explicitly warn where UPSC exam setters set traps (e.g. gauge vs absolute pressure, vector vs scalar, laminar vs turbulent assumptions).
8. STEP-BY-STEP WORKED NUMERICAL: Realistic aircraft parameters with Given, Formula, Calculation, Units, and Aviation Operational Interpretation.

STYLING & UI/UX RULES:
1. EYE-FRIENDLY CALM DAYLIGHT THEME:
   - Use: \`html, body { background-color: #f8fafc !important; color: #1e293b !important; }\`
   - Card backgrounds: \`#ffffff\`, borders: \`#e2e8f0\`, surface: \`#ffffff\`.
   - Never allow harsh pitch-black backgrounds or low-contrast washed-out text.
   - Text must have high contrast and stress-free readability: deep slate headings (\`#0f172a\`), readable slate body (\`#1e293b\`), secondary labels (\`#64748b\`).
2. MATHJAX CONFIGURATION (CRITICAL FOR FORMULA RENDERING):
   - You MUST include window.MathJax configuration BEFORE loading the MathJax script:
     <script>
     window.MathJax = {
         tex: {
             inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
             displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
             processEscapes: true,
             processEnvironments: true
         },
         options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] },
         svg: { fontCache: 'global' }
     };
     </script>
     <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
   - NEVER include polyfill.io script (it is deprecated and blocked).
   - In switchTab(tabNum), ALWAYS call: if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }
3. RESPONSIVE TABLES & MOBILE READINESS:
   - Every <table> must be wrapped in <div class="overflow-x-auto" style="overflow-x: auto;"> to prevent mobile overflow.
4. HERO SECTION:
   - Include: Badge, Title, concise metadata badges in one clean flex row.
   - DO NOT include duplicate navigation buttons or progress roadmaps in the hero!
5. 5-TAB ARCHITECTURE:
   - Single sticky segmented tab strip:
     [ 1. Comprehensive Notes ] [ 2. Concept Quiz (12 MCQs) ] [ 3. Aviation & Accidents ] [ 4. High-Yield Revision ] [ 5. Dual Mini Tests (+3/-1) ]
6. TAB 5 TESTS:
   - Level 1: Concept Mastery (10 questions, 80% passing threshold).
   - Level 2: UPSC Air Safety Officer Challenge (10 questions, +3 for correct, -1 for wrong negative marking, score breakdown, and benchmark bands).
7. POST-TAB SECTIONS:
   - Active Recall prompts ("Can You Explain These Without Notes?").
   - UPSC Interview Corner (collapsible <details> model answers).
   - Page Completion Checklist with localStorage persistence.
   - Footer Navigation (Previous, Plan, Next).

OUTPUT FORMAT:
Output ONLY valid, standalone HTML string starting with <!DOCTYPE html> and ending with </html>. Ensure all MathJax equations and HTML tags are valid and properly closed.`;

// ── Call Gemini API Exclusively with gemini-3.5-flash-lite & Max Tokens ─── //
async function callGemini(userPrompt, preferredModel = null) {
  const callCount = incrementPersistentCallCount();
  const targetModel = preferredModel || MODEL_NAME;
  let lastErr = null;

  console.log(`\n------------------------------------------------------------`);
  console.log(`[API Call #${callCount}] Target Model: ${targetModel} (Max Output Tokens: ${MAX_OUTPUT_TOKENS})`);

  const maxRetries = 4;
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    console.log(`  [Call #${callCount}] Requesting ${targetModel} (attempt ${attempt}/${maxRetries})...`);
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/${targetModel}:generateContent?key=${GEMINI_API_KEY}`;
    const body = {
      contents: [{ role: 'user', parts: [{ text: userPrompt }] }],
      systemInstruction: { parts: [{ text: SYSTEM_PROMPT }] },
      generationConfig: {
        temperature: 0.35,
        maxOutputTokens: MAX_OUTPUT_TOKENS
      }
    };

    try {
      const res = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });

      if (res.ok) {
        const data = await res.json();
        const text = data.candidates?.[0]?.content?.parts?.[0]?.text;
        if (text && text.trim().length > 0) {
          console.log(`  ✓ Received valid output from ${targetModel} (${text.length} chars)`);
          return text;
        }
      }

      const errText = await res.text();
      console.warn(`  Warning: ${targetModel} returned ${res.status}: ${errText.slice(0, 150)}...`);
      lastErr = new Error(`Gemini API Error ${res.status}: ${errText}`);

      if (res.status === 503 || res.status === 429) {
        const waitTime = attempt * 3500;
        console.log(`  Model ${targetModel} busy/spiking (${res.status}). Waiting ${waitTime/1000}s before retry...`);
        await new Promise(r => setTimeout(r, waitTime));
        continue;
      } else {
        break;
      }
    } catch (err) {
      console.warn(`  Network error with ${targetModel}: ${err.message}`);
      lastErr = err;
      await new Promise(r => setTimeout(r, 2000));
    }
  }

  throw lastErr || new Error('All model attempts failed');
}

// ── Clean & Validate HTML Post-Processor ────────────────────────────────── //
function cleanAndValidateHtml(rawHtml, { day, subject, subjectSlug, topic, prevTopic, nextTopic } = {}) {
  let html = rawHtml.trim().replace(/^```[a-zA-Z]*\n?/, '').replace(/\n?```$/, '').trim();

  // 1. Fix CSS background-clip vendor prefix order and ensure color: transparent
  html = html.replace(/-webkit-background-clip:\s*text;\s*(background-clip:\s*text;)?/g, 'background-clip: text;\n            -webkit-background-clip: text;\n            color: transparent;');
  html = html.replace(/(background-clip:\s*text;\s*)+/g, 'background-clip: text;\n            -webkit-background-clip: text;\n            color: transparent;\n            ');

  // 2. Ensure HTML ends cleanly with </html>
  if (!html.includes('</html>')) {
    console.warn(`[Day ${day}] HTML was truncated by model. Applying auto-completion recovery...`);
    const lastScriptOpen = html.lastIndexOf('<script');
    const lastScriptClose = html.lastIndexOf('</script>');
    if (lastScriptOpen > lastScriptClose) {
      html = html.substring(0, lastScriptOpen).trim();
    }

    if (!html.includes('id="chk1"')) {
      html += `
        <!-- Completion Checklist -->
        <div class="checklist-container" style="margin-top: 2rem;">
            <h3 style="color: #fff; margin-top: 0;"><i class="fa-solid fa-square-check" style="color: #10b981;"></i> Page Completion Checklist</h3>
            <div class="checklist-item" onclick="toggleCheck(this, event)">
                <input type="checkbox" id="chk1"><label for="chk1">Studied Core Concepts & Formulas</label>
            </div>
            <div class="checklist-item" onclick="toggleCheck(this, event)">
                <input type="checkbox" id="chk2"><label for="chk2">Reviewed Aviation Safety Applications</label>
            </div>
            <div class="checklist-item" onclick="toggleCheck(this, event)">
                <input type="checkbox" id="chk3"><label for="chk3">Completed Concept Quiz & Dual Mini Tests</label>
            </div>
        </div>`;
    }

    if (!html.includes('class="page-nav-footer"') && !html.includes('class="page-footer-nav"')) {
      html += `
        <div class="page-footer-nav" style="display:flex;justify-content:space-between;align-items:center;margin-top:3rem;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,0.1);">
            <a href="/upsc-aso/" class="nav-btn-link" style="color:#fff;text-decoration:none;"><i class="fa-solid fa-arrow-left"></i> Previous: ${prevTopic || 'Study Plan'}</a>
            <a href="/upsc-aso/" class="nav-btn-link" style="color:#fff;text-decoration:none;">Next: ${nextTopic || 'Next Day'} <i class="fa-solid fa-arrow-right"></i></a>
        </div>`;
    }

    const divOpenCount = (html.match(/<div\b/gi) || []).length;
    const divCloseCount = (html.match(/<\/div>/gi) || []).length;
    for (let i = 0; i < (divOpenCount - divCloseCount); i++) {
      html += '\n    </div>';
    }

    html += `
    <script>
        function switchTab(tabNum) {
            document.querySelectorAll('.tab-btn').forEach((btn, idx) => btn.classList.toggle('active', idx === tabNum - 1));
            document.querySelectorAll('.tab-content').forEach((c, idx) => c.classList.toggle('active', idx === tabNum - 1));
            document.querySelectorAll('.progress-step').forEach((s, idx) => s.classList.toggle('active', idx <= tabNum - 1));
            if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        function selectOption(el, qNum, opt, isCorrect) {
            const card = el.closest ? el.closest('.quiz-card') : document.getElementById('q' + qNum);
            if (!card) return;
            card.querySelectorAll('.option-item, .quiz-option').forEach(item => item.classList.remove('selected', 'correct', 'incorrect'));
            el.classList.add('selected');
            if (isCorrect !== undefined) {
                el.classList.add(isCorrect ? 'correct' : 'incorrect');
                const fb = document.getElementById('fb-' + qNum);
                if (fb) fb.className = 'quiz-feedback ' + (isCorrect ? 'correct-fb' : 'incorrect-fb');
            }
        }
        function checkAnswer(qNum, correctOpt) {
            const card = document.getElementById('q' + qNum);
            if (!card) return;
            const exp = document.getElementById('exp' + qNum);
            if (exp) exp.style.display = 'block';
        }
        const STORAGE_KEY = 'sj_upsc_aso_day${day}_progress';
        function initChecklist() {
            const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
            for (let i = 1; i <= 5; i++) {
                const chk = document.getElementById('chk' + i);
                if (chk && saved['chk' + i]) chk.checked = true;
            }
        }
        function toggleCheck(itemEl, ev) {
            const chk = itemEl.querySelector('input[type="checkbox"]');
            const target = ev ? ev.target : (window.event ? window.event.target : null);
            if (target !== chk && chk) chk.checked = !chk.checked;
            if (chk) {
                const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
                saved[chk.id] = chk.checked;
                localStorage.setItem(STORAGE_KEY, JSON.stringify(saved));
            }
        }
        document.addEventListener('DOMContentLoaded', initChecklist);
    </script>
</body>
</html>`;
  }

  // 3. Remove deprecated/blocked polyfill.io
  html = html.replace(/<script\s+src="https:\/\/polyfill\.io\/[^"]*"[^>]*><\/script>\s*/gi, '');

  // 4. Ensure MathJax configuration precedes MathJax script
  const mathJaxConfigSnippet = `<script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true,
                processEnvironments: true
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
            },
            svg: {
                fontCache: 'global'
            }
        };
    </script>`;

  if (html.includes('tex-mml-chtml.js') || html.includes('mathjax')) {
    if (!html.includes("['$', '$']") && !html.includes('["$", "$"]')) {
      const mathScriptRegex = /(<script[^>]*src="[^"]*mathjax[^"]*"[^>]*><\/script>|<script\s+id="MathJax-script"[^>]*><\/script>)/i;
      if (mathScriptRegex.test(html)) {
        html = html.replace(mathScriptRegex, `${mathJaxConfigSnippet}\n    $1`);
      }
    }
  } else if (html.includes('</head>')) {
    html = html.replace('</head>', `    ${mathJaxConfigSnippet}\n    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>\n</head>`);
  }

  // 5. Ensure switchTab re-renders MathJax for newly visible tabs
  if (html.includes('function switchTab') && !html.includes('MathJax.typesetPromise')) {
    html = html.replace(/(function\s+switchTab\s*\([^)]*\)\s*\{[\s\S]*?)(window\.scrollTo|\}$)/, (match, p1, p2) => {
      return `${p1}if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }\n            ${p2}`;
    });
  }

  // 6. Fix common LaTeX delimiter typos (\( paired with $)
  html = html.replace(/\\\(([a-zA-Z0-9_\^\\]+)\$/g, '\\($1\\)');
  html = html.replace(/\$([a-zA-Z0-9_\^\\]+)\\\)/g, '\\($1\\)');

  // 7. Ensure mobile viewport meta tag
  if (!html.includes('name="viewport"')) {
    html = html.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">');
  }

  // 8. Mobile-First Responsive Stylesheet
  const RESPONSIVE_CSS = `
/* ==========================================================================
   MOBILE-FIRST RESPONSIVE ENHANCEMENT (SJMaths ASO Study Hub)
   ========================================================================== */
html, body {
    max-width: 100vw !important;
    overflow-x: hidden !important;
    position: relative;
    background-color: #f8fafc !important;
    background: #f8fafc !important;
    color: #1e293b !important;
    -webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}
* {
    box-sizing: border-box;
}

/* Fluid Responsive Typography */
h1, .hero-title {
    font-size: clamp(1.45rem, 4.5vw, 2.5rem) !important;
    line-height: 1.25 !important;
    word-break: break-word;
    overflow-wrap: break-word;
}
h2 {
    font-size: clamp(1.2rem, 3.5vw, 1.75rem) !important;
    line-height: 1.3 !important;
    word-break: break-word;
}
h3 {
    font-size: clamp(1.05rem, 3vw, 1.35rem) !important;
    line-height: 1.35 !important;
    word-break: break-word;
}

/* Touch-Optimized Segmented Tab Strip (GUARANTEED HORIZONTAL) */
nav [role="tablist"],
nav.sticky div.flex,
nav div.flex,
.tab-strip,
#tab-nav,
.tabs-container,
.tab-nav {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 0.35rem !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
    max-width: 100% !important;
}
nav [role="tablist"]::-webkit-scrollbar,
nav.sticky div.flex::-webkit-scrollbar,
nav div.flex::-webkit-scrollbar,
.tab-strip::-webkit-scrollbar,
#tab-nav::-webkit-scrollbar,
.tabs-container::-webkit-scrollbar,
.tab-nav::-webkit-scrollbar,
.no-scrollbar::-webkit-scrollbar {
    display: none !important;
}
.tab-btn,
nav [role="tablist"] button,
nav.sticky button {
    display: inline-flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    white-space: nowrap !important;
    touch-action: manipulation;
    -webkit-tap-highlight-color: transparent;
    user-select: none;
    min-height: 38px;
}

/* Responsive Tables & Containers - NEVER override display on .overflow-x-auto */
table {
    max-width: 100% !important;
    width: 100% !important;
    border-collapse: collapse;
}
.data-table, .concept-card table, table.table-custom {
    display: block !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: thin;
}
.overflow-x-auto {
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch !important;
    max-width: 100% !important;
}

/* Prevent MathJax Display Formulas from Blowing Out Screen Width */
mjx-container[jax="CHTML"][display="true"] {
    overflow-x: auto !important;
    overflow-y: hidden !important;
    max-width: 100% !important;
    padding: 0.5rem 0.25rem !important;
    margin: 0.75rem 0 !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: thin;
}
mjx-container {
    max-width: 100% !important;
}

/* Mobile Viewport Refinements (< 640px) */
@media (max-width: 640px) {
    body {
        font-size: 14px !important;
    }
    main, .max-w-7xl, .container, .module-container {
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
    }
    .concept-card {
        padding: 1.15rem 0.75rem !important;
        margin-bottom: 1.25rem !important;
        border-radius: 0.75rem !important;
    }
    .definition-callout, .callout-def, .trap-box, .numerical-box, .math-box, .derivation-box {
        padding: 0.85rem 0.75rem !important;
        margin: 0.85rem 0 !important;
        font-size: 0.875rem !important;
    }
    .tab-btn {
        padding: 0.4rem 0.75rem !important;
        font-size: 0.75rem !important;
    }
    table th, table td, .data-table th, .data-table td {
        padding: 0.45rem 0.6rem !important;
        font-size: 0.75rem !important;
        white-space: nowrap;
    }
    .quiz-card, .quiz-item, .mcq-card, .question-card {
        padding: 1rem 0.75rem !important;
        margin-bottom: 1rem !important;
    }
    .quiz-option, .option-item, .option-label, label.block {
        padding: 0.65rem 0.75rem !important;
        font-size: 0.85rem !important;
        min-height: 44px;
        display: flex;
        align-items: center;
    }
    .grid-cols-2, .grid-cols-3, .grid-cols-4, .sm\\:grid-cols-2, .md\\:grid-cols-2, .sm\\:grid-cols-3, .md\\:grid-cols-3 {
        grid-template-columns: 1fr !important;
    }
    .hero-badge, .badge-exam {
        font-size: 0.7rem !important;
        padding: 0.25rem 0.5rem !important;
    }
    .checklist-item {
        padding: 0.6rem 0.75rem !important;
        font-size: 0.85rem !important;
    }
    .page-footer-nav, .page-nav-footer {
        flex-direction: column !important;
        gap: 0.75rem !important;
        align-items: stretch !important;
        text-align: center;
    }
    .page-footer-nav a, .page-nav-footer a, .nav-btn-link {
        width: 100% !important;
        justify-content: center !important;
        display: flex !important;
    }
}

/* Tablet Refinements (641px - 1024px) */
@media (min-width: 641px) and (max-width: 1024px) {
    main, .max-w-7xl {
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
    }
    .concept-card {
        padding: 1.5rem !important;
    }
}
`;

  if (!html.includes('MOBILE-FIRST RESPONSIVE ENHANCEMENT')) {
    if (html.includes('</style>')) {
      html = html.replace('</style>', `${RESPONSIVE_CSS}\n    </style>`);
    } else if (html.includes('</head>')) {
      html = html.replace('</head>', `    <style>${RESPONSIVE_CSS}</style>\n</head>`);
    }
  }

  // Universal Quiz CSS
  const QUIZ_CSS = `
/* Universal Quiz Option Interactive States */
.quiz-opt-correct,
.option-item.correct,
.quiz-option.correct,
.quiz-opt-btn.correct,
label.quiz-opt-correct {
    border-color: #10b981 !important;
    background-color: #dcfce7 !important;
    color: #065f46 !important;
}
.quiz-opt-incorrect,
.option-item.incorrect,
.quiz-option.incorrect,
.quiz-opt-btn.incorrect,
label.quiz-opt-incorrect {
    border-color: #ef4444 !important;
    background-color: #fee2e2 !important;
    color: #991b1b !important;
}
.quiz-exp-revealed {
    display: block !important;
    opacity: 1 !important;
    visibility: visible !important;
    animation: fadeIn 0.3s ease-out;
}
`;

  if (!html.includes('.quiz-opt-correct')) {
    if (html.includes('</style>')) {
      html = html.replace('</style>', `${QUIZ_CSS}\n    </style>`);
    } else if (html.includes('</head>')) {
      html = html.replace('</head>', `    <style>${QUIZ_CSS}</style>\n</head>`);
    }
  }

  // Universal Quiz Script
  const QUIZ_ENGINE_SCRIPT = `
<!-- UNIVERSAL INTERACTIVE QUIZ & TEST FEEDBACK SYSTEM -->
<script id="universal-quiz-feedback">
(function() {
    function getScopedVar(name) {
        try {
            if (typeof window !== 'undefined' && window[name] !== undefined) return window[name];
        } catch(e) {}
        try {
            return eval('typeof ' + name + ' !== "undefined" ? ' + name + ' : undefined');
        } catch(e) {}
        return undefined;
    }

    function normalizeAns(val) {
        if (val === undefined || val === null) return -1;
        if (typeof val === 'number') return val;
        const str = String(val).trim().toUpperCase();
        if (str === 'A') return 0;
        if (str === 'B') return 1;
        if (str === 'C') return 2;
        if (str === 'D') return 3;
        const num = parseInt(str, 10);
        return isNaN(num) ? -1 : num;
    }

    function handleOptionInteraction(target) {
        const optionEl = target.closest('label, .option-item, .quiz-opt-btn, .quiz-option, .quiz-opt-label, .quiz-choice, [data-option]');
        if (!optionEl) return;

        const card = optionEl.closest('.quiz-card, .quiz-item, .test-card, .concept-card, [id^="qc-"], [id^="q-card-"], [id^="q-block-"], [id^="q-box-"], [id^="card-q-"], [id^="l1-card-"], [id^="l2-card-"], [data-question], [data-qid], [data-q]') || optionEl.parentElement?.parentElement;
        if (!card) return;

        let allOptions = Array.from(card.querySelectorAll('label, .option-item, .quiz-opt-btn, .quiz-option, .quiz-opt-label, .quiz-choice, [data-option]'));
        if (allOptions.length === 0 && card.parentElement) {
            allOptions = Array.from(card.parentElement.querySelectorAll('label, .option-item, .quiz-opt-btn, .quiz-option'));
        }

        const radio = optionEl.querySelector('input[type="radio"]') || (target.tagName === 'INPUT' ? target : null);
        let selectedIdx = allOptions.indexOf(optionEl);
        if (radio && radio.value !== undefined) {
            const valIdx = normalizeAns(radio.value);
            if (valIdx !== -1) selectedIdx = valIdx;
        }

        if (selectedIdx === -1 && !radio) return;
        if (radio) radio.checked = true;

        const rName = radio?.name || card.querySelector('input[type="radio"]')?.name || '';
        const l1Match = rName.match(/(?:l1|t1|test1)[-_]?q?(\d+)/i) || (card.id && card.id.match(/(?:l1|t1)[-_]?card[-_]?(\d+)/i));
        const l2Match = rName.match(/(?:l2|t2|test2)[-_]?q?(\d+)/i) || (card.id && card.id.match(/(?:l2|t2)[-_]?card[-_]?(\d+)/i));
        const qMatch = rName.match(/(?:q|quiz)[-_]?(\d+)/i) || (card.id && card.id.match(/(?:qc|q|card|q-block|q-box)[-_]?(\d+)/i));

        let qNum = -1;
        if (l1Match) qNum = parseInt(l1Match[1], 10);
        else if (l2Match) qNum = parseInt(l2Match[1], 10);
        else if (qMatch) qNum = parseInt(qMatch[1], 10);
        else if (card.getAttribute('data-q') || card.getAttribute('data-qid') || card.getAttribute('data-question')) {
            qNum = parseInt(card.getAttribute('data-q') || card.getAttribute('data-qid') || card.getAttribute('data-question'), 10);
        }

        let correctIdx = -1;
        let explanationText = '';

        if (card.getAttribute('data-answer') || card.getAttribute('data-correct')) {
            correctIdx = normalizeAns(card.getAttribute('data-answer') || card.getAttribute('data-correct'));
        }

        if (correctIdx === -1) {
            allOptions.forEach((opt, idx) => {
                if (opt.getAttribute('data-correct') === 'true' || opt.classList.contains('correct-answer') || (opt.getAttribute('onclick') && /,\\s*true\\s*\\)/i.test(opt.getAttribute('onclick')))) {
                    correctIdx = idx;
                }
            });
        }

        if (correctIdx === -1) {
            const btn = card.querySelector('button[onclick*="Ans"], button[onclick*="Answer"], button[onclick*="Check"], button[onclick*="verify"]');
            if (btn) {
                const m = btn.getAttribute('onclick').match(/['"]([A-D])['"]/i);
                if (m) correctIdx = normalizeAns(m[1]);
            }
        }

        if (correctIdx === -1) {
            const ansMap = getScopedVar('quizAnswers') || getScopedVar('answers');
            if (ansMap) {
                const val = ansMap[rName] || ansMap['q' + qNum] || ansMap[String(qNum)];
                if (val !== undefined) {
                    if (typeof val === 'object' && val.correct !== undefined) {
                        correctIdx = normalizeAns(val.correct);
                        if (val.exp) explanationText = val.exp;
                    } else {
                        correctIdx = normalizeAns(val);
                    }
                }
            }
        }

        if (correctIdx === -1 && !l1Match && !l2Match) {
            const qData = getScopedVar('quizData') || getScopedVar('quizQuestions') || getScopedVar('mcqsTab2');
            if (Array.isArray(qData)) {
                let item = qData[qNum];
                if (!item || (qNum > 0 && qData[qNum - 1])) {
                    item = qData[qNum - 1] || qData[qNum];
                }
                if (item) {
                    correctIdx = normalizeAns(item.answer !== undefined ? item.answer : (item.correct !== undefined ? item.correct : item.ans));
                    if (item.exp || item.explanation) explanationText = item.exp || item.explanation;
                }
            }
        }

        if (correctIdx === -1 && l1Match) {
            const l1Data = getScopedVar('level1Data') || getScopedVar('test1Data') || getScopedVar('testDataLevel1') || getScopedVar('testLevel1Data') || getScopedVar('level1Questions') || getScopedVar('testDataL1') || getScopedVar('l1QuestionsData');
            if (Array.isArray(l1Data)) {
                let item = l1Data[qNum] || (qNum > 0 ? l1Data[qNum - 1] : null);
                if (item) {
                    correctIdx = normalizeAns(item.answer !== undefined ? item.answer : (item.correct !== undefined ? item.correct : item.ans));
                    if (item.exp || item.explanation) explanationText = item.exp || item.explanation;
                }
            }
        }

        if (correctIdx === -1 && l2Match) {
            const l2Data = getScopedVar('level2Data') || getScopedVar('test2Data') || getScopedVar('testDataLevel2') || getScopedVar('testLevel2Data') || getScopedVar('level2Questions') || getScopedVar('testDataL2') || getScopedVar('l2QuestionsData');
            if (Array.isArray(l2Data)) {
                let item = l2Data[qNum] || (qNum > 0 ? l2Data[qNum - 1] : null);
                if (item) {
                    correctIdx = normalizeAns(item.answer !== undefined ? item.answer : (item.correct !== undefined ? item.correct : item.ans));
                    if (item.exp || item.explanation) explanationText = item.exp || item.explanation;
                }
            }
        }

        if (correctIdx === -1) {
            const expElCheck = card.querySelector('.explanation, .quiz-explanation, .explanation-box, .quiz-exp-box, .quiz-feedback, [id*="exp"], [id*="feedback"]');
            const txt = (expElCheck ? expElCheck.textContent : card.textContent) || '';
            const match = txt.match(/Correct(?:\\s+Answer|\\s+Option)?:\\s*([A-D])/i) || txt.match(/\\(Correct:\\s*([A-D])\\)/i);
            if (match) {
                correctIdx = normalizeAns(match[1]);
            }
        }

        if (correctIdx === -1) return;

        const isCorrect = (selectedIdx === correctIdx);
        const correctLetter = String.fromCharCode(65 + correctIdx);

        allOptions.forEach((opt, idx) => {
            opt.classList.remove(
                'quiz-opt-correct', 'quiz-opt-incorrect', 'correct', 'incorrect',
                'border-emerald-500', 'bg-emerald-500/20', 'text-emerald-300',
                'border-rose-500', 'bg-rose-500/20', 'text-rose-300'
            );

            if (idx === correctIdx) {
                opt.classList.add('quiz-opt-correct', 'correct', 'border-emerald-500', 'bg-emerald-50', 'text-emerald-800', 'font-semibold');
                opt.style.setProperty('border-color', '#10b981', 'important');
                opt.style.setProperty('background-color', '#dcfce7', 'important');
                opt.style.setProperty('color', '#065f46', 'important');
            } else if (idx === selectedIdx && !isCorrect) {
                opt.classList.add('quiz-opt-incorrect', 'incorrect', 'border-rose-500', 'bg-rose-50', 'text-rose-800');
                opt.style.setProperty('border-color', '#ef4444', 'important');
                opt.style.setProperty('background-color', '#fee2e2', 'important');
                opt.style.setProperty('color', '#991b1b', 'important');
            } else {
                opt.style.removeProperty('border-color');
                opt.style.removeProperty('background-color');
                opt.style.removeProperty('color');
            }
        });

        let expEl = card.querySelector('.explanation, .quiz-explanation, .explanation-box, .quiz-exp-box, .quiz-feedback, [id*="exp"], [id*="feedback"], [id*="fb"]');
        if (!expEl && qNum !== -1) {
            expEl = document.getElementById('q-exp-' + qNum) || 
                    document.getElementById('q-exp-' + (qNum - 1)) || 
                    document.getElementById('quiz-feedback-' + qNum) || 
                    document.getElementById('quiz-feedback-' + (qNum - 1)) || 
                    document.getElementById('q' + qNum + '-explanation') ||
                    document.getElementById('explanation-' + qNum) ||
                    document.getElementById('q' + qNum + '-feedback') ||
                    document.getElementById('fb-' + qNum) ||
                    document.getElementById('qexp-' + qNum) ||
                    document.getElementById('l1-fb-' + qNum) ||
                    document.getElementById('l2-fb-' + qNum);
        }

        if (!expEl) {
            expEl = document.createElement('div');
            expEl.className = 'quiz-feedback mt-3 p-3 rounded-lg border text-sm text-slate-200';
            card.appendChild(expEl);
        }

        if (expEl) {
            expEl.classList.remove('hidden');
            expEl.style.setProperty('display', 'block', 'important');
            expEl.classList.add('quiz-exp-revealed');

            let statusBadge = expEl.querySelector('.quiz-status-badge');
            if (!statusBadge) {
                statusBadge = document.createElement('div');
                statusBadge.className = 'quiz-status-badge font-bold mb-1.5 flex items-center gap-1.5';
                expEl.insertBefore(statusBadge, expEl.firstChild);
            }

            if (isCorrect) {
                statusBadge.innerHTML = '<span class="text-emerald-400 font-bold" style="color:#10b981;"><i class="fa-solid fa-circle-check mr-1"></i> Correct Answer!</span>';
                expEl.style.setProperty('border-color', 'rgba(16, 185, 129, 0.4)', 'important');
                expEl.style.setProperty('background-color', 'rgba(16, 185, 129, 0.08)', 'important');
            } else {
                statusBadge.innerHTML = '<span class="text-rose-400 font-bold" style="color:#ef4444;"><i class="fa-solid fa-circle-xmark mr-1"></i> Incorrect (Correct Answer: Option ' + correctLetter + ')</span>';
                expEl.style.setProperty('border-color', 'rgba(239, 68, 68, 0.4)', 'important');
                expEl.style.setProperty('background-color', 'rgba(239, 68, 68, 0.08)', 'important');
            }

            if (explanationText && (expEl.textContent.trim().length < 40 || !expEl.querySelector('.quiz-exp-content'))) {
                let contentEl = expEl.querySelector('.quiz-exp-content');
                if (!contentEl) {
                    contentEl = document.createElement('div');
                    contentEl.className = 'quiz-exp-content mt-1 text-slate-300 text-xs sm:text-sm leading-relaxed';
                    expEl.appendChild(contentEl);
                }
                contentEl.innerHTML = '<strong>Explanation:</strong> ' + explanationText;
            }

            if (window.MathJax && window.MathJax.typesetPromise) {
                window.MathJax.typesetPromise([expEl]).catch(function(){});
            }
        }
    }

    document.addEventListener('click', function(e) {
        const optionTarget = e.target.closest('label, .option-item, .quiz-opt-btn, .quiz-option, .quiz-opt-label, .quiz-choice, [data-option]');
        if (optionTarget) {
            handleOptionInteraction(optionTarget);
        }
    });

    document.addEventListener('change', function(e) {
        if (e.target.matches('input[type="radio"]')) {
            handleOptionInteraction(e.target);
        }
    });
})();
</script>
`;

  if (!html.includes('id="universal-quiz-feedback"')) {
    if (html.includes('</body>')) {
      html = html.replace('</body>', `${QUIZ_ENGINE_SCRIPT}\n</body>`);
    } else {
      html = html + QUIZ_ENGINE_SCRIPT;
    }
  }

  if (day && topic && subject && subjectSlug) {
    html = moveBreadcrumbsToTop(html, { day, subject, subjectSlug, topic });
  }

  return html;
}

// ── Generate Page for Given Topic Metadata ────────────────────────────────── //
export async function generateStudyPage({ day, subject, subjectSlug, topic, slug, subtopics, prevTopic, nextTopic, outputPath }) {
  console.log(`\n============================================================`);
  console.log(`Generating: Day ${day} • ${topic} (${subject})`);
  console.log(`Subtopics: ${subtopics.join(', ')}`);
  console.log(`Output: ${outputPath}`);

  const userPrompt = `Create a complete study page for my website SJMaths.com for:

**Exam:** UPSC Air Safety Officer — DGCA
**Day:** ${day}
**Subject:** ${subject}
**Topic:** ${topic}
**Subtopics to cover:** ${subtopics.join(', ')}
**Previous topic:** ${prevTopic || 'Course Orientation & Strategy'}
**Next topic:** ${nextTopic || 'Next Day Study Module'}

CRITICAL PEDAGOGICAL MANDATE:
Do NOT output compressed summary cards or formula-only boxes!
For EVERY one of the ${subtopics.length} subtopics (${subtopics.join(', ')}), you MUST generate an independent, complete concept card in Tab 1 containing:
1. Technical Definition
2. Basic Physical Concept & Molecular/Continuum Mechanics
3. Step-by-Step Mathematical Derivation & Equations
4. Dimensions in [M, L, T, \\theta], SI and CGS Units
5. Engineering Reference Data Table
6. Aircraft Application & DGCA Air Safety Connection (CAR Section 2 rules, failure modes, accidents)
7. UPSC Traps & Common Exam Pitfalls
8. Step-by-Step Worked Numerical with real aircraft values, full math, and operational takeaway.

Include all 5 tabs:
Tab 1: Exhaustive Notes (with all ${subtopics.length} distinct concept cards)
Tab 2: Concept Quiz (12 MCQs with detailed explanations)
Tab 3: Aviation & Accidents (Case studies & CAR connections)
Tab 4: High-Yield Revision Summary
Tab 5: Dual Mini Tests (Level 1 Mastery 10 MCQs + Level 2 UPSC ASO Challenge 10 MCQs with +3/-1 negative marking)
Post-tab: Active Recall questions, UPSC Interview Corner (<details> model answers), and completion checklist.`;

  const rawHtml = await callGemini(userPrompt);
  const html = cleanAndValidateHtml(rawHtml, { day, subject, subjectSlug, topic, prevTopic, nextTopic });

  const outDir = path.dirname(outputPath);
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  fs.writeFileSync(outputPath, html, 'utf8');
  console.log(`✓ Successfully saved: ${outputPath} (${html.length} bytes)`);
  return outputPath;
}

// ── Parse Day Metadata from upsc-aso/index.html ──────────────────────────── //
export function parseAllDays() {
  const indexPath = path.resolve('upsc-aso/index.html');
  if (!fs.existsSync(indexPath)) return [];
  const html = fs.readFileSync(indexPath, 'utf8');

  const phaseSubjectMap = {
    'p1': (t) => (t.toLowerCase().includes('heat') || t.toLowerCase().includes('conduction') || t.toLowerCase().includes('radiation') || t.toLowerCase().includes('exchanger')) ? { name: 'Heat Transfer', slug: 'heat-transfer' } : { name: 'Fluid Mechanics & Machinery', slug: 'fluid-mechanics-machinery' },
    'p2': () => ({ name: 'Aerodynamics, Performance & Stability', slug: 'aerodynamics-performance-stability' }),
    'p3': () => ({ name: 'Aircraft Structures & Materials', slug: 'aircraft-structures-materials' }),
    'p4': () => ({ name: 'Propulsion & Gas Turbines', slug: 'propulsion' }),
    'p5': () => ({ name: 'Aircraft Systems, Instrumentation & Maintenance', slug: 'aircraft-systems-instrumentation-maintenance' }),
    'p6': () => ({ name: 'Avionics, Radar & Navigation', slug: 'avionics-navigation-surveillance' }),
    'p7': () => ({ name: 'Air Traffic Control, Aerodromes & Flight Planning', slug: 'atc-aerodromes-flight-planning' }),
    'p8': () => ({ name: 'Aviation Rules, Regulations & Safety', slug: 'regulations-aviation-safety' }),
    'p9': () => ({ name: 'PYQ, Mock Tests & Final Consolidation', slug: 'mock-tests-consolidation' })
  };

  const subsectionRegex = /<details class="syllabus-subsection"([^>]*)>([\s\S]*?)<\/details>/gi;
  let match;
  const days = [];

  while ((match = subsectionRegex.exec(html)) !== null) {
    const attrs = match[1];
    const content = match[2];

    const prefixMatch = attrs.match(/data-prefix="([^"]*)"/);
    const prefix = prefixMatch ? prefixMatch[1] : '';

    const dayMatch = content.match(/class="badge-exam"[^>]*>([\s\S]*?)<\/span>/);
    const dayText = dayMatch ? dayMatch[1].replace(/<[^>]+>/g, '').trim() : '';
    const dayNumMatch = dayText.match(/Day\s+(\d+)/i);
    const dayNum = dayNumMatch ? parseInt(dayNumMatch[1], 10) : days.length + 1;

    const titleMatch = content.match(/class="subsection-title(?:-link)?"[^>]*>([\s\S]*?)<\/(?:span|a)>/);
    const rawTitle = titleMatch ? titleMatch[1].replace(/<[^>]+>/g, '').trim() : '';
    const titleText = rawTitle.replace(/&amp;/g, '&');

    const itemRegex = /<li\s+class="syllabus-item([^"]*)">([\s\S]*?)<\/li>/gi;
    let itemM;
    const subtopics = [];
    while ((itemM = itemRegex.exec(content)) !== null) {
      const liContent = itemM[2];
      const aMatch = liContent.match(/<a\s+[^>]*href="([^"]*)"[^>]*>([\s\S]*?)<\/a>/i);
      if (aMatch) {
        subtopics.push(aMatch[2].replace(/&amp;/g, '&').replace(/<[^>]+>/g, '').trim());
      }
    }

    const subjInfo = phaseSubjectMap[prefix] ? phaseSubjectMap[prefix](titleText) : { name: 'General Aviation', slug: 'general-aviation' };
    const cleanTitleForSlug = titleText.toLowerCase().replace(/&/g, 'and');
    const slug = cleanTitleForSlug.replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

    days.push({
      day: dayNum,
      dayText,
      prefix,
      subject: subjInfo.name,
      subjectSlug: subjInfo.slug,
      topic: titleText,
      slug,
      subtopics
    });
  }

  // Populate prevTopic and nextTopic
  for (let i = 0; i < days.length; i++) {
    days[i].prevTopic = i > 0 ? `Day ${days[i - 1].day} • ${days[i - 1].topic}` : 'UPSC ASO Syllabus & Study Plan';
    days[i].nextTopic = i < days.length - 1 ? `Day ${days[i + 1].day} • ${days[i + 1].topic}` : 'Final Consolidation';
    days[i].outputPath = path.resolve(`upsc-aso/${days[i].subjectSlug}/${days[i].slug}/index.html`);
  }

  return days;
}

const scriptArg = process.argv[1] ? process.argv[1].replace(/\\/g, '/') : '';
const isCli = scriptArg && (import.meta.url.endsWith(scriptArg) || scriptArg.includes('generate_gemini_study_page'));

if (isCli) {
  const args = process.argv.slice(2);
  let dayArg = null;
  let rangeArg = null;
  let allArg = false;

  for (const a of args) {
    if (a.startsWith('--day=')) dayArg = a.split('=')[1];
    else if (a === '--day') dayArg = args[args.indexOf(a) + 1];
    else if (a.startsWith('--range=')) rangeArg = a.split('=')[1];
    else if (a === '--range') rangeArg = args[args.indexOf(a) + 1];
    else if (a === '--all') allArg = true;
  }

  const allDays = parseAllDays();

  async function run() {
    if (dayArg) {
      const dayNum = parseInt(dayArg, 10);
      const dayData = allDays.find(d => d.day === dayNum);
      if (!dayData) {
        console.error(`Day ${dayNum} not found in study plan.`);
        process.exit(1);
      }
      await generateStudyPage(dayData);
    } else if (rangeArg) {
      const [start, end] = rangeArg.split('-').map(n => parseInt(n.trim(), 10));
      const targetDays = allDays.filter(d => d.day >= start && d.day <= end);
      console.log(`Generating Days ${start} to ${end} (${targetDays.length} pages)...`);
      for (const d of targetDays) {
        await generateStudyPage(d);
        console.log('Sleeping 4s between API calls...');
        await new Promise(r => setTimeout(r, 4000));
      }
    } else if (allArg) {
      console.log(`Generating all ${allDays.length} days...`);
      for (const d of allDays) {
        await generateStudyPage(d);
        console.log('Sleeping 4s between API calls...');
        await new Promise(r => setTimeout(r, 4000));
      }
    } else {
      console.log('UPSC Air Safety Officer — Gemini Study Page Generator');
      console.log('----------------------------------------------------');
      console.log('Usage:');
      console.log('  node upsc-aso/generate_gemini_study_page.mjs --day=1');
      console.log('  node upsc-aso/generate_gemini_study_page.mjs --range=1-5');
      console.log('  node upsc-aso/generate_gemini_study_page.mjs --all');
    }
  }

  run().catch(console.error);
}


