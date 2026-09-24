import fs from 'fs';
import path from 'path';

// ── 1. Configuration & Multi-Key Env Loading ───────────────────────────────── //
function loadAllGeminiKeys() {
  const envMap = {};

  // 1. Read process.env for any GEMINI_API_KEY or GOOGLE_API_KEY variables
  for (const [k, v] of Object.entries(process.env)) {
    if ((k.startsWith('GEMINI_API_KEY') || k === 'GOOGLE_API_KEY') && v && v.trim()) {
      envMap[k] = v.trim().replace(/^['"]|['"]$/g, '');
    }
  }

  // 2. Read .env files from potential relative paths
  const envPaths = ['.env', '../.env', 'upsc-aso/.env'];
  for (const p of envPaths) {
    if (fs.existsSync(p)) {
      const content = fs.readFileSync(p, 'utf8');
      for (const line of content.split(/\r?\n/)) {
        const eqIdx = line.indexOf('=');
        if (eqIdx > 0) {
          const varName = line.slice(0, eqIdx).trim();
          const val = line.slice(eqIdx + 1).trim().replace(/^['"]|['"]$/g, '');
          if ((varName.startsWith('GEMINI_API_KEY') || varName === 'GOOGLE_API_KEY') && val) {
            if (!envMap[varName]) {
              envMap[varName] = val;
            }
          }
        }
      }
    }
  }

  // 3. Build unique key pool (ordered: GEMINI_API_KEY_1, GEMINI_API_KEY_2, ..., GEMINI_API_KEY, GOOGLE_API_KEY)
  const sortedNames = Object.keys(envMap).sort((a, b) => {
    const numA = parseInt(a.replace(/\D/g, '') || '999', 10);
    const numB = parseInt(b.replace(/\D/g, '') || '999', 10);
    return numA - numB;
  });

  const uniqueKeys = [];
  const seenKeyValues = new Set();

  for (const name of sortedNames) {
    const val = envMap[name];
    if (val && !seenKeyValues.has(val)) {
      seenKeyValues.add(val);
      const masked = val.length > 8 ? `${val.slice(0, 6)}...${val.slice(-4)}` : '***';
      uniqueKeys.push({ name, key: val, masked });
    }
  }

  return uniqueKeys;
}

class KeyManager {
  constructor(keys) {
    this.keys = keys;
    this.currentIndex = 0;
  }

  selectKey(selector) {
    if (!selector) return;
    const sel = String(selector).trim();
    // Match by 1-based index (e.g. "1" or "2")
    if (/^\d+$/.test(sel)) {
      const idx = parseInt(sel, 10) - 1;
      if (idx >= 0 && idx < this.keys.length) {
        this.currentIndex = idx;
        console.log(`[KEY MANAGER] Selected key #${idx + 1} (${this.keys[idx].name}) via selector '${selector}'`);
        return;
      }
    }
    // Match by variable name (case-insensitive)
    const foundIdx = this.keys.findIndex(k => k.name.toLowerCase() === sel.toLowerCase());
    if (foundIdx !== -1) {
      this.currentIndex = foundIdx;
      console.log(`[KEY MANAGER] Selected key #${foundIdx + 1} (${this.keys[foundIdx].name}) via selector '${selector}'`);
      return;
    }
    // Raw key string (>20 characters)
    if (sel.length > 20) {
      const masked = `${sel.slice(0, 6)}...${sel.slice(-4)}`;
      this.keys.unshift({ name: 'CLI_SUPPLIED_KEY', key: sel, masked });
      this.currentIndex = 0;
      console.log(`[KEY MANAGER] Using custom CLI API key: ${masked}`);
      return;
    }
    console.warn(`[KEY MANAGER] Warning: Selector '${selector}' did not match any known key in pool. Defaulting to ${this.getActiveKey()?.name}`);
  }

  getActiveKey() {
    return this.keys[this.currentIndex] || null;
  }

  rotateToNextKey(reason = '') {
    if (this.keys.length <= 1) return false;
    const prev = this.keys[this.currentIndex];
    this.currentIndex = (this.currentIndex + 1) % this.keys.length;
    const next = this.keys[this.currentIndex];
    console.warn(`\n[KEY ROTATION] ⚠️ ${reason} on ${prev.name} (${prev.masked}).`);
    console.warn(`[KEY ROTATION] ➡️ Switched to active key: ${next.name} (${next.masked}) [Key ${this.currentIndex + 1}/${this.keys.length}]\n`);
    return true;
  }

  printSummary() {
    console.log(`\nGemini API Key Pool (${this.keys.length} unique keys loaded):`);
    this.keys.forEach((k, i) => {
      const activeMark = i === this.currentIndex ? ' [ACTIVE]' : '';
      console.log(`  [${i + 1}] ${k.name}: ${k.masked}${activeMark}`);
    });
    console.log(`Automatic key rotation is ENABLED on HTTP 429 / quota limits.`);
    console.log(`Override active key anytime using: --key=<number_or_name>\n`);
  }
}

const ALL_GEMINI_KEYS = loadAllGeminiKeys();
if (ALL_GEMINI_KEYS.length === 0) {
  console.error('ERROR: No GEMINI_API_KEY, GEMINI_API_KEY_1, or GOOGLE_API_KEY found in environment or .env file.');
  process.exit(1);
}

export const keyManager = new KeyManager(ALL_GEMINI_KEYS);

// ── 2. Subject Title & Meta Mapping ───────────────────────────────────────── //
const SUBJECT_MAP = {
  'aerodynamics-performance-stability': {
    name: 'Aerodynamics, Flight Performance & Stability',
    phase: 'Phase 2: Aeronautics & Aerodynamics'
  },
  'fluid-mechanics-machinery': {
    name: 'Fluid Mechanics & Machinery',
    phase: 'Phase 1: Fluids & Heat Transfer'
  },
  'aircraft-systems-instrumentation-maintenance': {
    name: 'Aircraft Systems, Instrumentation & Maintenance',
    phase: 'Phase 5: Systems & Maintenance'
  },
  'aircraft-structures-materials': {
    name: 'Aircraft Structures, Materials & Stress Analysis',
    phase: 'Phase 3: Structures & Materials'
  },
  'heat-transfer': {
    name: 'Aeronautical Heat Transfer & Thermodynamics',
    phase: 'Phase 1: Fluids & Heat Transfer'
  },
  'atc-aerodromes-flight-planning': {
    name: 'Air Traffic Control, Aerodromes & Flight Planning',
    phase: 'Phase 7: ATC & Flight Planning'
  },
  'propulsion': {
    name: 'Aircraft Propulsion & Gas Turbine Engines',
    phase: 'Phase 4: Propulsion'
  },
  'avionics-navigation-surveillance': {
    name: 'Avionics, Navigation & Surveillance (CNS/ATM)',
    phase: 'Phase 6: Avionics & Navigation'
  },
  'regulations-aviation-safety': {
    name: 'Aircraft Rules, Air Law & Aviation Safety (DGCA / ICAO)',
    phase: 'Phase 8: Rules, Regulations & Safety'
  }
};

// ── 3. Checkpointing & Progress Tracking ──────────────────────────────────── //
const PROGRESS_FILE = path.resolve('upsc-aso/microtopics_progress.json');

function loadProgress() {
  if (fs.existsSync(PROGRESS_FILE)) {
    try {
      return JSON.parse(fs.readFileSync(PROGRESS_FILE, 'utf8'));
    } catch (e) {
      console.warn('Warning: Could not parse progress file, initializing fresh.');
    }
  }
  return { completed: {}, failed: {}, lastUpdated: new Date().toISOString() };
}

function saveProgress(progress) {
  progress.lastUpdated = new Date().toISOString();
  fs.writeFileSync(PROGRESS_FILE, JSON.stringify(progress, null, 2), 'utf8');
}

// ── Intelligent JSON Sanitizer & Parser for LaTeX ────────────────────────── //
function sanitizeAndParseJson(raw) {
  let cleaned = raw.trim();
  if (cleaned.startsWith('```json')) {
    cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  } else if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
  }

  // Attempt direct JSON.parse first
  try {
    return JSON.parse(cleaned);
  } catch (err1) {
    // Fall back to intelligent repair
  }

  let repaired = '';
  let inString = false;
  let isEscaped = false;

  for (let i = 0; i < cleaned.length; i++) {
    const ch = cleaned[i];
    if (inString) {
      if (isEscaped) {
        isEscaped = false;
        const nextChars = cleaned.slice(i, i + 8);
        if (/^(frac|nu|rho|tau|theta|partial|alpha|beta|gamma|sigma|lambda|mu|times|cdot|approx|infty|text|left|right|sqrt|mathbf|rm|int|omega|psi|phi|Delta|nabla|sum|prod)/.test(nextChars)) {
          repaired += '\\\\' + ch;
        } else if (/^["\\/bfnrt]/.test(ch) || (ch === 'u' && /^[0-9a-fA-F]{4}/.test(cleaned.slice(i + 1, i + 5)))) {
          repaired += '\\' + ch;
        } else {
          repaired += '\\\\' + ch;
        }
      } else {
        if (ch === '\\') {
          isEscaped = true;
        } else if (ch === '"') {
          inString = false;
          repaired += ch;
        } else {
          if (ch === '\n') repaired += '\\n';
          else if (ch === '\r') repaired += '\\r';
          else if (ch === '\t') repaired += '\\t';
          else repaired += ch;
        }
      }
    } else {
      if (ch === '"') inString = true;
      repaired += ch;
    }
  }

  try {
    return JSON.parse(repaired);
  } catch (err2) {
    fs.writeFileSync('upsc-aso/debug_failed_repaired.json', repaired);
    throw new Error(`JSON parse failed after repair: ${err2.message}`);
  }
}

// ── 4. Gemini API Client with Auto Key Rotation & Backoff ─────────────────── //
async function callGeminiWithRetry(prompt, model = 'gemini-3.5-flash-lite', maxRetries = 6) {
  let delayMs = 2000;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const activeKeyObj = keyManager.getActiveKey();
    if (!activeKeyObj) {
      throw new Error('No active Gemini API key found in KeyManager pool.');
    }

    const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${activeKeyObj.key}`;
    const payload = {
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: {
        responseMimeType: 'application/json',
        temperature: 0.25,
        maxOutputTokens: 65536
      }
    };

    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const data = await res.json();
        const candidate = data.candidates?.[0];
        if (!candidate || !candidate.content?.parts?.[0]?.text) {
          throw new Error('Empty response from Gemini API');
        }
        return sanitizeAndParseJson(candidate.content.parts[0].text);
      }

      const status = res.status;
      const errorText = await res.text();

      // Handle 429 Rate Limit / Quota Exceeded & 403 Forbidden Quota
      if (status === 429 || status === 403 || errorText.includes('RESOURCE_EXHAUSTED') || errorText.includes('quota')) {
        console.warn(`[API ${status}] Attempt ${attempt}/${maxRetries} using ${activeKeyObj.name} hit quota/rate limit.`);
        
        // Auto-rotate to another key in the pool if available
        const rotated = keyManager.rotateToNextKey(`HTTP ${status} on ${activeKeyObj.name}`);
        if (rotated) {
          await new Promise(r => setTimeout(r, 1000));
          continue;
        }

        // If no alternate key is available, perform backoff
        console.warn(`No alternate key available in pool. Backing off ${delayMs}ms...`);
        await new Promise(r => setTimeout(r, delayMs + Math.random() * 1000));
        delayMs *= 2;
        continue;
      }

      if (status === 500 || status === 503) {
        console.warn(`[API ${status} Server Busy] Attempt ${attempt}/${maxRetries}. Backing off ${delayMs}ms...`);
        await new Promise(r => setTimeout(r, delayMs));
        delayMs *= 2;
        continue;
      }

      throw new Error(`Gemini API HTTP ${status} (${activeKeyObj.name}): ${errorText}`);
    } catch (err) {
      if (attempt === maxRetries) throw err;
      console.warn(`[Attempt ${attempt}/${maxRetries} Error]: ${err.message}. Retrying...`);
      await new Promise(r => setTimeout(r, delayMs));
      delayMs *= 1.5;
    }
  }
}

// ── 5. Prompt Builder (8 Pillars + UPSC Practice + Mini Test + Flashcards) ─── //
function buildMicrotopicPrompt(topic) {
  const subMeta = SUBJECT_MAP[topic.subject_slug] || { name: topic.subject_slug, phase: 'UPSC ASO' };

  return `You are a distinguished aerospace professor, DGCA Air Safety Officer mentor, and senior curriculum designer for SJMaths.com.

Your task is to generate complete, textbook-grade study content for the UPSC Air Safety Officer (ASO) examination for the following microtopic:
Topic: "${topic.title}"
Subject: "${subMeta.name}"
Day: ${topic.day}
Syllabus Phase: "${subMeta.phase}"

CRITICAL FORMATTING MANDATE (ABSOLUTE NO LONG PARAGRAPHS):
- Long continuous paragraphs are STRICTLY FORBIDDEN!
- Every paragraph must be STRICTLY 1 to 2 sentences maximum (under 35 words).
- All explanations, physical mechanisms, principles, and applications MUST be structured as:
  1. Concise lead definition callouts (<div class="lead-definition">).
  2. Bulleted item lists (<ul class="concept-list"><li><strong>Key Term:</strong> 1-2 sentence explanation.</li></ul>).
  3. Distinct step-by-step boxes (<div class="step-item"><strong>Step N: [Title]</strong>...</div>).
  4. Structured trap cards (<div class="trap-box">...</div>).
- High visual scannability, punchy bullet points, and instant memorability are required for top-rank preparation.

YOU MUST RETURN STRICT VALID JSON. DO NOT WRAP IN MARKDOWN BACKTICKS. RETURN ONLY RAW JSON OBJECT CONFORMING TO THIS EXACT STRUCTURE:

{
  "pillar1_definition": "HTML string containing: <div class=\\"lead-definition\\">1-2 sentence rigorous technical definition with governing equation ($...$).</div><ul class=\\"concept-list\\"><li><strong>Physical Meaning:</strong> 1-2 concise sentences.</li><li><strong>Governing Law:</strong> 1-2 concise sentences.</li><li><strong>Continuum Boundary:</strong> 1-2 concise sentences.</li></ul><div class=\\"nomenclature-box\\"><h4 style=\\"margin-top:0;color:#38bdf8;\\">Nomenclature & Symbols</h4><ul class=\\"concept-list\\"><li>$symbol$ = Name and physical interpretation (Units)</li>...</ul></div>",
  "pillar2_physical_mechanism": "HTML string containing NO long paragraphs! Use 3 to 4 distinct step cards: <div class=\\"step-item\\"><strong>1. Molecular Kinetic State:</strong> 1-2 concise sentences explaining molecular collisions, mean free path, or parcel dynamics.</div><div class=\\"step-item\\"><strong>2. Continuum Forces & Gradients:</strong> 1-2 concise sentences on pressure/shear stress equilibrium.</div><div class=\\"step-item\\"><strong>3. Aerodynamic Consequence:</strong> 1-2 concise sentences on how this dictates lift, drag, pressure, or engine mass flow.</div>",
  "pillar3_derivation": "HTML string containing complete analytical derivation broken into numbered step boxes: <div class=\\"step-item\\"><strong>Step 1: Governing Relation</strong><p style=\\"margin:4px 0;\\">1-line explanation.</p>$$Equation 1$$</div><div class=\\"step-item\\"><strong>Step 2: Boundary / Thermodynamic Conditions</strong><p style=\\"margin:4px 0;\\">1-line explanation.</p>$$Equation 2$$</div><div class=\\"step-item\\"><strong>Step 3: Integration & Substitution</strong><p style=\\"margin:4px 0;\\">1-line explanation.</p>$$Equation 3$$</div><div class=\\"step-item\\"><strong>Step 4: Final Working Law</strong><p style=\\"margin:4px 0;\\">1-line conclusion.</p>$$Final Equation$$</div>",
  "pillar4_dimensions_units": "HTML string containing clean bullet points: <ul class=\\"concept-list\\"><li><strong>Fundamental Dimensions:</strong> $[M^a L^b T^c \\theta^d]$ with algebraic breakdown.</li><li><strong>SI Unit:</strong> Primary unit name and fundamental breakdown ($kg/(m\\cdot s)$, etc.).</li><li><strong>CGS Unit:</strong> Primary unit name and exact conversion factor.</li><li><strong>Aeronautical & Imperial Equivalents:</strong> Slugs, psi, knots, bars, and conversion formulas in separate concise bullets.</li></ul>",
  "pillar5_engineering_table": "HTML string containing a formatted responsive table comparing 5-6 standard reference values for aviation engineering fluids or flight regimes (ISA sea level vs FL300, Jet A-1 kerosene, Avgas 100LL, Skydrol LD-4 hydraulic fluid, engine oil). Wrap in <div class=\\"overflow-x-auto\\"><table class=\\"data-table\\">...</table></div>.",
  "aso_relevance": "HTML string containing 4 distinct bullet cards: <ul class=\\"aso-bullets\\"><li><strong>1. Aircraft Systems & Flight Deck Monitoring:</strong> Which specific aircraft instruments, transducers, fuel/engine sensors, or hydraulic systems rely on this parameter in 1-2 concise sentences.</li><li><strong>2. Flight Safety & Dispatch Envelopes:</strong> How this dictates takeoff roll, gross weight limits, climb gradients, or stall margin calculations in 1-2 concise sentences.</li><li><strong>3. DGCA CAR & ICAO Airworthiness Compliance:</strong> The specific regulatory mandate (DGCA CAR Section 2 / ICAO Annex 8 Airworthiness / ICAO Annex 14) governing fluid checks or airframe limits in 1-2 concise sentences.</li><li><strong>4. Air Safety Investigation & Incident Prevention:</strong> How a DGCA Air Safety Officer evaluates this parameter during incident root-cause analysis, flight data recorder audits, or ramp checks in 1-2 concise sentences.</li></ul>",
  "pillar6_airworthiness_safety": "HTML string with 3 distinct bullet blocks: <ul class=\\"concept-list\\"><li><strong>Regulatory Standards (DGCA CAR & ICAO):</strong> Exact CAR Section and ICAO Annex citation explained in 1-2 concise sentences.</li><li><strong>Critical Aircraft Systems:</strong> Impact on pitot-static, FADEC, bleed air, fuel boost pumps, or flight controls in 1-2 concise sentences.</li><li><strong>Aviation Incident Case Study:</strong> Real aircraft incident (Flight number, aircraft type, failure mechanism, and root safety cause) in 2 concise bullets.</li></ul>",
  "pillar7_examiner_traps": "HTML string containing 4 structured trap boxes: <div class=\\"trap-box\\"><div class=\\"trap-header\\"><i class=\\"fas fa-exclamation-triangle text-amber-400\\"></i> Trap 1: [Trap Name]</div><p class=\\"trap-misconception\\"><strong>❌ Examiner Trap:</strong> 1 concise sentence stating the common error.</p><p class=\\"trap-correction\\"><strong>✅ UPSC Truth:</strong> 1-2 concise sentences giving the correct rule, sign convention, or formula.</p></div> (Repeat for Traps 2, 3, 4)",
  "pillar8_worked_numerical": {
    "problem_statement": "Realistic aircraft engineering scenario problem statement in 2-3 concise sentences.",
    "given_data": "Formatted list of given flight parameters with appropriate units.",
    "formula_used": "Governing mathematical formula in LaTeX.",
    "step_by_step_solution": "3 distinct, numbered calculation steps with numerical substitutions and units.",
    "final_answer": "Final computed value with correct units.",
    "air_safety_takeaway": "Operational air safety takeaway in 1-2 concise sentences explaining why this matters during an airworthiness audit or incident investigation."
  },
  "practice_questions": [
    {
      "id": 1,
      "type": "conceptual",
      "question": "Question text in crisp English with LaTeX if needed...",
      "options": ["A. Option text", "B. Option text", "C. Option text", "D. Option text"],
      "correct_index": 0,
      "explanation": "Exhaustive step-by-step technical explanation of why the correct option is right and why the other three distractors are false."
    }
  ],
  "mini_test": [
    {
      "id": 1,
      "question": "High-yield UPSC exam simulation question...",
      "options": ["A. Option text", "B. Option text", "C. Option text", "D. Option text"],
      "correct_index": 0,
      "explanation": "Clear explanation of the solution."
    }
  ],
  "flashcards": [
    {
      "front": "Prompt or formula question for active recall...",
      "back": "Exact formula, definition, dimensional formula, or safety rule."
    }
  ]
}

MANDATORY RULES:
1. NO LONG PARAGRAPHS: Any paragraph over 2 sentences is strictly forbidden. Use bullet points and step boxes.
2. "practice_questions": Exactly 12 to 14 questions. Must include a mix of: Conceptual, Statement-based ("Which of the statements given above is/are correct?"), Numerical calculations, and Assertion-Reasoning.
3. "mini_test": Exactly 10 questions. UPSC exam difficulty (+3 / -1 marking standard).
4. "flashcards": Exactly 8 to 10 flashcards for high-yield spaced repetition.
5. Use clean MathJax LaTeX: write inline math as $...$ and display equations as $$...$$. NEVER insert HTML tags like <span> or entities inside LaTeX $ tags.
6. Content must be exhaustive, rigorous, and completely written out (NO PLACEHOLDERS, NO "etc.", NO shortcuts). The candidate must be able to score rank 1 using these notes.
7. CRITICAL JSON ESCAPING: Because you are returning a raw JSON string, EVERY single backslash in LaTeX expressions MUST be escaped with a double backslash (e.g. \\\\rho, \\\\mu, \\\\frac{a}{b}, \\\\tau, \\\\theta, \\\\Delta, \\\\cdot, \\\\approx, \\\\nu, \\\\sigma). Single unescaped backslashes break JSON string syntax.`;
}

// ── 6. HTML Template Engine (Cockpit Aesthetic, 4 Tabs, MathJax 3) ────────── //
function renderMicrotopicHtml(topic, data) {
  const subMeta = SUBJECT_MAP[topic.subject_slug] || { name: topic.subject_slug, phase: 'Phase 1' };
  const canonicalUrl = `https://sjmaths.com${topic.href}`;
  const parentSubjectHref = `/upsc-aso/${topic.subject_slug}/`;

  // Render Practice Questions HTML
  const practiceQuestionsHtml = (data.practice_questions || []).map((q, idx) => {
    const qNum = idx + 1;
    const optLetters = ['A', 'B', 'C', 'D'];
    const optionsHtml = q.options.map((opt, oIdx) => {
      const cleanOpt = opt.replace(/^[A-D]\.\s*/, '');
      return `
        <div class="quiz-option" onclick="handleQuizSelect(this, ${qNum}, ${oIdx}, ${q.correct_index})">
          <span class="opt-letter">${optLetters[oIdx]}</span>
          <span class="opt-text">${cleanOpt}</span>
        </div>`;
    }).join('');

    return `
      <div class="question-card" id="practice-q-${qNum}">
        <div class="q-header">
          <span class="q-badge">Question ${qNum} • ${q.type || 'Conceptual'}</span>
        </div>
        <div class="q-text">${q.question}</div>
        <div class="quiz-options-group">
          ${optionsHtml}
        </div>
        <div class="explanation-box" id="practice-exp-${qNum}">
          <div class="exp-title"><i class="fas fa-check-circle text-emerald-400"></i> Solution & Technical Rationale:</div>
          <div class="exp-content">${q.explanation}</div>
        </div>
      </div>`;
  }).join('\n');

  // Render Mini Test Questions HTML
  const miniTestQuestionsHtml = (data.mini_test || []).map((q, idx) => {
    const qNum = idx + 1;
    const optLetters = ['A', 'B', 'C', 'D'];
    const optionsHtml = q.options.map((opt, oIdx) => {
      const cleanOpt = opt.replace(/^[A-D]\.\s*/, '');
      return `
        <div class="test-option" onclick="handleTestSelect(this, ${qNum}, ${oIdx})">
          <span class="opt-letter">${optLetters[oIdx]}</span>
          <span class="opt-text">${cleanOpt}</span>
        </div>`;
    }).join('');

    return `
      <div class="test-question-item" id="test-q-${qNum}" data-correct="${q.correct_index}">
        <div class="q-header">
          <span class="q-badge">Question ${qNum} of 10</span>
          <span class="q-marks">+3 / -1</span>
        </div>
        <div class="q-text">${q.question}</div>
        <div class="test-options-group">
          ${optionsHtml}
        </div>
        <div class="test-explanation" id="test-exp-${qNum}" style="display:none;">
          <div class="exp-title"><i class="fas fa-info-circle text-cyan-400"></i> Rationale:</div>
          <div class="exp-content">${q.explanation}</div>
        </div>
      </div>`;
  }).join('\n');

  // Render Flashcards HTML
  const flashcardsHtml = (data.flashcards || []).map((f, idx) => {
    return `
      <div class="flashcard-container" onclick="this.classList.toggle('flipped')">
        <div class="flashcard-inner">
          <div class="flashcard-front">
            <div class="card-num">Card #${idx + 1}</div>
            <div class="card-prompt">${f.front}</div>
            <div class="card-hint"><i class="fas fa-sync-alt"></i> Click to flip</div>
          </div>
          <div class="flashcard-back">
            <div class="card-num">Key Takeaway #${idx + 1}</div>
            <div class="card-answer">${f.back}</div>
            <div class="card-hint"><i class="fas fa-check"></i> Mastered</div>
          </div>
        </div>
      </div>`;
  }).join('\n');

  // Worked Numerical HTML
  const num = data.pillar8_worked_numerical || {};
  const formattedFormula = num.formula_used ? (num.formula_used.includes('$') ? num.formula_used : `$$${num.formula_used}$$`) : '';
  const formattedAns = num.final_answer ? (num.final_answer.includes('$') ? num.final_answer : `$${num.final_answer}$`) : '';

  const numericalHtml = `
    <div class="numerical-card">
      <div class="num-section-title"><i class="fas fa-calculator text-cyan-400"></i> Realistic Aircraft Scenario</div>
      <p class="num-problem">${num.problem_statement || ''}</p>
      
      <div class="num-grid">
        <div class="num-box">
          <div class="num-label">Given Flight Parameters:</div>
          <div class="num-val">${num.given_data || ''}</div>
        </div>
        <div class="num-box">
          <div class="num-label">Governing Formula:</div>
          <div class="num-val">${formattedFormula}</div>
        </div>
      </div>

      <div class="num-solution">
        <div class="num-label">Step-by-Step Analytical Solution:</div>
        <div class="num-solution-steps">${num.step_by_step_solution || ''}</div>
        <div class="num-final-ans"><strong>Final Answer:</strong> ${formattedAns}</div>
      </div>

      <div class="num-safety-box">
        <div class="safety-title"><i class="fas fa-shield-alt text-amber-400"></i> Air Safety Officer Operational Takeaway:</div>
        <p class="safety-desc">${num.air_safety_takeaway || ''}</p>
      </div>
    </div>`;

  // Dedicated ASO Relevance HTML
  let asoRelevanceHtml = data.aso_relevance || '';
  if (asoRelevanceHtml && !asoRelevanceHtml.includes('<ul')) {
    asoRelevanceHtml = `<ul class="aso-bullets">${asoRelevanceHtml}</ul>`;
  }
  if (!asoRelevanceHtml) {
    asoRelevanceHtml = `
      <ul class="aso-bullets">
        <li>
          <strong>1. Aircraft Systems & Flight Deck Monitoring:</strong>
          Critical for sensor calibration, pitot-static probes, and engine/fuel transducer telemetry under variable flight envelopes.
        </li>
        <li>
          <strong>2. Flight Safety & Dispatch Envelopes:</strong>
          Directly influences gross takeoff weight, climb gradients, density altitude limits, and balanced field length calculations.
        </li>
        <li>
          <strong>3. DGCA CAR & ICAO Airworthiness:</strong>
          Governed under DGCA CAR Section 2 and ICAO Annex 8 to guarantee fluid purity, pressure tolerances, and airframe structural limits.
        </li>
        <li>
          <strong>4. Air Safety Investigation & Forensics:</strong>
          Evaluated by safety inspectors during FDR/CVR data correlation, fluid contamination audits, and incident root-cause determination.
        </li>
      </ul>`;
  }

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.title} | UPSC Air Safety Officer (ASO) Preparation</title>
    <meta name="description" content="Master ${topic.title} for UPSC Air Safety Officer (DGCA): Complete 8-pillar theory, mathematical derivations, engineering tables, air safety applications, 14 practice MCQs, and timed mini-test.">
    <link rel="canonical" href="${canonicalUrl}">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Standardized MathJax 3 Configuration -->
    <script>
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
      svg: { fontCache: 'global' }
    };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <!-- Schema.org BreadcrumbList -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://sjmaths.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "UPSC ASO Hub",
          "item": "https://sjmaths.com/upsc-aso/"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "${subMeta.name}",
          "item": "https://sjmaths.com${parentSubjectHref}"
        },
        {
          "@type": "ListItem",
          "position": 4,
          "name": "${topic.title}",
          "item": "${canonicalUrl}"
        }
      ]
    }
    </script>

    <style>
        :root {
            --bg-void: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #ffffff;
            --bg-card-hover: #f1f5f9;
            --border-glass: #e2e8f0;
            --border-accent: rgba(37, 99, 235, 0.25);
            --cyan-primary: #0284c7;
            --cyan-glow: rgba(2, 132, 199, 0.12);
            --indigo-accent: #4f46e5;
            --emerald-accent: #059669;
            --amber-accent: #d97706;
            --text-main: #0f172a;
            --text-sub: #475569;
            --text-muted: #64748b;
        }

        html, body {
            background-color: var(--bg-void) !important;
            background: #f8fafc !important;
            color: #1e293b !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.7;
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
        }

        * {
            box-sizing: border-box;
        }

        /* Top Sticky Bar */
        .sj-topbar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-glass);
            position: sticky;
            top: 0;
            z-index: 1000;
            padding: 0.75rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        }

        .sj-brand {
            display: flex;
            align-items: center;
            gap: 0.65rem;
            text-decoration: none;
        }

        .brand-logo-text {
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 800;
            background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            color: #38bdf8;
        }

        .badge-aso {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: rgba(56, 189, 248, 0.12);
            color: var(--cyan-primary);
            padding: 2px 8px;
            border-radius: 6px;
            border: 1px solid rgba(56, 189, 248, 0.25);
        }

        .topbar-nav {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .topbar-link {
            color: var(--text-sub);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 0.4rem;
            transition: color 0.2s ease;
        }

        .topbar-link:hover {
            color: var(--cyan-primary);
        }

        .micro-container {
            max-width: 1120px;
            margin: 0 auto;
            padding: 1.5rem 1rem 4rem;
        }

        /* Top Breadcrumb Nav */
        .breadcrumb-trail {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
            font-size: 0.84rem;
            color: var(--text-muted);
            margin-bottom: 1.25rem;
            padding: 0.25rem 0;
        }

        .breadcrumb-trail a {
            color: var(--cyan-primary);
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .breadcrumb-trail a:hover {
            color: var(--cyan-primary);
            text-decoration: underline;
        }

        .breadcrumb-trail .separator {
            font-size: 0.65rem;
            color: var(--text-muted);
        }

        .breadcrumb-trail .current-page {
            color: var(--text-sub);
            font-weight: 500;
        }

        /* Hero Header */
        .micro-hero {
            background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%) !important;
            border: 1px solid var(--border-glass) !important;
            border-left: 5px solid var(--cyan-primary) !important;
            border-radius: 1rem !important;
            padding: 1.75rem 2rem !important;
            margin-bottom: 1.5rem !important;
            box-shadow: 0 2px 12px rgba(15, 23, 42, 0.04) !important;
            position: relative !important;
            overflow: hidden !important;
            display: flex !important;
            flex-direction: column !important;
            height: auto !important;
            min-height: auto !important;
        }

        .hero-meta-badges {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            flex-wrap: wrap;
            margin-bottom: 0.85rem;
        }

        .hero-badge {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 20px;
            background: #eff6ff;
            color: var(--cyan-primary);
            border: 1px solid #bfdbfe;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .hero-badge.day-badge {
            background: #eef2ff;
            color: var(--indigo-accent);
            border-color: #c7d2fe;
        }

        .micro-hero h1 {
            font-family: 'Outfit', sans-serif !important;
            font-size: clamp(1.8rem, 4vw, 2.5rem) !important;
            font-weight: 800 !important;
            color: #0f172a !important;
            margin: 0.25rem 0 0.75rem !important;
            line-height: 1.25 !important;
        }

        .hero-desc {
            font-size: 0.98rem;
            color: var(--text-sub);
            max-width: 900px;
            margin: 0;
            line-height: 1.6;
        }

        /* Air Safety Officer & Aircraft Relevance Banner */
        .aso-mission-banner {
            background: linear-gradient(135deg, #eff6ff 0%, #f0fdf4 100%);
            border: 1px solid #bfdbfe;
            border-left: 5px solid var(--cyan-primary);
            border-radius: 14px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 10px rgba(2, 132, 199, 0.04);
        }

        .aso-mission-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-bottom: 0.85rem;
            border-bottom: 1px solid rgba(56, 189, 248, 0.2);
            padding-bottom: 0.75rem;
        }

        .aso-mission-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }

        .aso-mission-title i {
            color: var(--cyan-primary);
            font-size: 1.25rem;
        }

        .aso-mission-tag {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: rgba(56, 189, 248, 0.15);
            color: var(--cyan-primary);
            padding: 3px 10px;
            border-radius: 20px;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }

        .aso-mission-intro {
            font-size: 0.92rem;
            color: var(--text-sub);
            margin-bottom: 1.25rem;
            line-height: 1.6;
        }

        .aso-bullets {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
            list-style: none !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        .aso-bullets li {
            background: #ffffff;
            border: 1px solid var(--border-glass);
            border-radius: 10px;
            padding: 1rem 1.15rem;
            font-size: 0.88rem;
            line-height: 1.6;
            color: #334155;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .aso-bullets li:hover {
            border-color: #93c5fd;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(2, 132, 199, 0.08);
        }

        .aso-bullets li strong {
            color: var(--cyan-primary);
            display: block;
            margin-bottom: 0.4rem;
            font-size: 0.92rem;
        }

        /* 4 Main Tabs Bar */
        .tab-strip {
            display: flex;
            gap: 0.35rem;
            margin-bottom: 2rem;
            background: #f1f5f9;
            padding: 5px;
            border-radius: 12px;
            border: 1px solid var(--border-glass);
            overflow-x: auto;
            scrollbar-width: none;
        }

        .tab-strip::-webkit-scrollbar {
            display: none;
        }

        .tab-btn {
            background: transparent;
            border: none;
            outline: none;
            font-family: 'Outfit', sans-serif;
            font-size: 0.92rem;
            font-weight: 600;
            color: var(--text-sub);
            padding: 0.65rem 1.15rem;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.2s ease;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex-shrink: 0;
        }

        .tab-btn:hover {
            color: #0f172a;
            background: #e2e8f0;
        }

        .tab-btn.active {
            color: #1e40af;
            background: #ffffff;
            border: 1px solid var(--border-glass);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
            font-weight: 700;
        }

        /* Tab Content Panels */
        .tab-panel {
            display: none;
            animation: fadeIn 0.3s ease-in-out;
        }

        .tab-panel.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* 8 Pillar Cards in Tab 1 */
        .pillar-card {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 1rem;
            padding: 1.75rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .pillar-card:hover {
            border-color: rgba(56, 189, 248, 0.25);
        }

        .pillar-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 1.2rem;
            display: flex;
            align-items: center;
            gap: 0.65rem;
            border-bottom: 1px solid #f1f5f9;
            padding-bottom: 0.65rem;
        }

        .pillar-title i {
            color: var(--cyan-primary);
        }

        .pillar-content {
            font-size: 0.96rem;
            line-height: 1.75;
            color: #334155;
        }

        .pillar-content h3, .pillar-content h4 {
            font-family: 'Outfit', sans-serif;
            color: #0f172a;
            margin-top: 1.25rem;
            margin-bottom: 0.5rem;
        }

        .pillar-content ul, .pillar-content ol {
            padding-left: 1.35rem;
            margin: 0.75rem 0;
        }

        .pillar-content li {
            margin-bottom: 0.4rem;
        }

        .lead-definition {
            background: #f0f9ff;
            border-left: 4px solid var(--cyan-primary);
            border-radius: 8px;
            padding: 1rem 1.25rem;
            font-size: 1rem;
            line-height: 1.65;
            margin-bottom: 1.25rem;
            color: #0c4a6e;
            font-weight: 500;
        }

        .concept-list {
            list-style: none !important;
            padding: 0 !important;
            margin: 1rem 0 !important;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .concept-list li {
            background: #f8fafc;
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            padding: 0.85rem 1.15rem;
            line-height: 1.6;
            margin-bottom: 0 !important;
            color: #334155;
        }

        .concept-list li strong {
            color: var(--cyan-primary);
        }

        .step-item {
            background: #f8fafc;
            border: 1px solid var(--border-glass);
            border-left: 3px solid var(--indigo-accent);
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        }

        .step-item strong {
            color: var(--indigo-accent);
            font-size: 0.98rem;
            display: block;
            margin-bottom: 0.4rem;
        }

        .trap-box {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 10px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        }

        .trap-header {
            font-weight: 700;
            color: #b45309;
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .trap-misconception {
            color: #b91c1c;
            margin: 0 0 0.4rem !important;
            font-size: 0.92rem;
            line-height: 1.5;
        }

        .trap-correction {
            color: #15803d;
            margin: 0 !important;
            font-size: 0.92rem;
            line-height: 1.5;
        }

        .nomenclature-box {
            background: var(--bg-surface);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-top: 1.25rem;
        }

        /* Responsive Data Tables */
        .overflow-x-auto {
            overflow-x: auto;
            margin: 1.25rem 0;
            border-radius: 8px;
            border: 1px solid var(--border-glass);
        }

        .data-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.88rem;
            text-align: left;
            background: #ffffff;
        }

        .data-table th {
            background: #f1f5f9;
            color: #0f172a;
            padding: 10px 14px;
            font-weight: 700;
            border-bottom: 2px solid #cbd5e1;
            white-space: nowrap;
        }

        .data-table td {
            padding: 10px 14px;
            border-bottom: 1px solid var(--border-glass);
            color: #334155;
        }

        .data-table tr:hover td {
            background: #eff6ff;
        }

        /* Numerical Card Styling */
        .numerical-card {
            background: #f8fafc;
            border: 1px solid #bfdbfe;
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1rem;
        }

        .num-section-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--cyan-primary);
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .num-problem {
            font-size: 0.95rem;
            color: #1e293b;
            margin-bottom: 1.25rem;
            line-height: 1.6;
        }

        .num-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1.25rem;
        }

        @media (max-width: 640px) {
            .num-grid { grid-template-columns: 1fr; }
        }

        .num-box {
            background: #ffffff;
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            padding: 1rem;
        }

        .num-label {
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.4rem;
        }

        .num-val {
            font-size: 0.92rem;
            color: #0f172a;
            font-family: 'Fira Code', monospace;
        }

        .num-solution {
            background: #ffffff;
            border-radius: 8px;
            padding: 1.25rem;
            border: 1px solid var(--border-glass);
            border-left: 3px solid var(--emerald-accent);
            margin-bottom: 1.25rem;
        }

        .num-solution-steps {
            font-size: 0.92rem;
            color: #1e293b;
            line-height: 1.7;
            margin-top: 0.5rem;
        }

        .num-final-ans {
            margin-top: 0.75rem;
            padding: 0.6rem 0.85rem;
            background: #ecfdf5;
            border: 1px solid #a7f3d0;
            border-radius: 6px;
            color: #065f46;
            font-weight: 600;
            font-family: 'Fira Code', monospace;
        }

        .num-safety-box {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-radius: 8px;
            padding: 1rem;
        }

        .safety-title {
            font-weight: 700;
            color: #b45309;
            font-size: 0.9rem;
            margin-bottom: 0.4rem;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }

        .safety-desc {
            font-size: 0.88rem;
            color: #78350f;
            margin: 0;
            line-height: 1.55;
        }

        /* Tab 2: Practice Questions */
        .question-card {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        }

        .q-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.75rem;
        }

        .q-badge {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 12px;
            background: rgba(56, 189, 248, 0.1);
            color: var(--cyan-primary);
        }

        .q-text {
            font-size: 1.02rem;
            font-weight: 600;
            color: #0f172a;
            margin-bottom: 1rem;
            line-height: 1.6;
        }

        .quiz-options-group {
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
            margin-bottom: 1rem;
        }

        .quiz-option {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            background: #f8fafc;
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 0.94rem;
            color: #1e293b;
        }

        .quiz-option:hover {
            border-color: #93c5fd;
            background: #eff6ff;
        }

        .quiz-option.correct {
            border-color: #86efac !important;
            background: #dcfce7 !important;
            color: #14532d !important;
            font-weight: 600;
        }

        .quiz-option.incorrect {
            border-color: #fca5a5 !important;
            background: #fee2e2 !important;
            color: #7f1d1d !important;
        }

        .opt-letter {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.06);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: 700;
            flex-shrink: 0;
        }

        .explanation-box {
            display: none;
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-top: 1rem;
        }

        .exp-title {
            font-weight: 700;
            color: #15803d;
            font-size: 0.88rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .exp-content {
            font-size: 0.9rem;
            color: #166534;
            line-height: 1.6;
        }

        /* Tab 3: Mini Test */
        .test-header-bar {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .test-info {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .test-timer {
            font-family: 'Fira Code', monospace;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--amber-accent);
            background: rgba(245, 158, 11, 0.1);
            padding: 4px 12px;
            border-radius: 6px;
            border: 1px solid rgba(245, 158, 11, 0.2);
        }

        .test-question-item {
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.25rem;
        }

        .q-marks {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--emerald-accent);
            background: rgba(16, 185, 129, 0.1);
            padding: 2px 8px;
            border-radius: 6px;
        }

        .test-options-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .test-option {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            background: var(--bg-surface);
            border: 1px solid var(--border-glass);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 0.92rem;
        }

        .test-option:hover {
            border-color: var(--cyan-primary);
        }

        .test-option.selected {
            border-color: var(--cyan-primary);
            background: rgba(56, 189, 248, 0.15);
            color: #0f172a;
            font-weight: 600;
        }

        .test-submit-btn {
            background: linear-gradient(135deg, #0284c7, #2563eb);
            color: #0f172a;
            border: none;
            padding: 0.85rem 2rem;
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }

        .test-submit-btn:hover {
            opacity: 0.95;
            transform: translateY(-1px);
        }

        .test-result-box {
            display: none;
            background: var(--bg-card);
            border: 1px solid var(--border-glass);
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        .score-big {
            font-family: 'Outfit', sans-serif;
            font-size: 3rem;
            font-weight: 800;
            color: var(--cyan-primary);
        }

        /* Tab 4: Flashcards */
        .flashcards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.25rem;
        }

        .flashcard-container {
            perspective: 1000px;
            height: 220px;
            cursor: pointer;
        }

        .flashcard-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
            transform-style: preserve-3d;
        }

        .flashcard-container.flipped .flashcard-inner {
            transform: rotateY(180deg);
        }

        .flashcard-front, .flashcard-back {
            background: linear-gradient(135deg, #eff6ff, #f8fafc);
            border-color: #bfdbfe;
            color: #0f172a;
            transform: rotateY(180deg);
        }

        .card-num {
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--cyan-primary);
        }

        .card-prompt {
            font-size: 1.05rem;
            font-weight: 600;
            line-height: 1.45;
        }

        .card-answer {
            font-size: 0.95rem;
            line-height: 1.55;
            color: #0f172a;
        }

        .card-hint {
            font-size: 0.75rem;
            color: var(--text-muted);
        }

        /* Bottom Action Bar */
        .bottom-actions {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 3rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-glass);
            flex-wrap: wrap;
            gap: 1rem;
        }

        .action-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--cyan-primary);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.92rem;
            transition: color 0.2s ease;
        }

        .action-link:hover {
            color: #0f172a;
            text-decoration: underline;
        }

        .complete-btn {
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: #6ee7b7;
            padding: 0.6rem 1.25rem;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s ease;
        }

        .complete-btn:hover {
            background: rgba(16, 185, 129, 0.2);
        }

        .complete-btn.marked {
            background: var(--emerald-accent);
            color: #0f172a;
        }

        .micro-footer {
            border-top: 1px solid var(--border-glass);
            padding: 2.5rem 1rem;
            text-align: center;
            color: var(--text-muted);
            font-size: 0.85rem;
            margin-top: 4rem;
            background: #f8fafc;
        }

        .footer-sub {
            font-size: 0.76rem;
            color: #475569;
            margin-top: 0.35rem;
        }
    </style>
</head>
<body>
    <!-- Dedicated ASO Cockpit Topbar -->
    <header class="sj-topbar">
        <a href="/" class="sj-brand">
            <span class="brand-logo-text">SJMaths</span>
            <span class="badge-aso">Air Safety Officer</span>
        </a>
        <nav class="topbar-nav">
            <a href="/upsc-aso/" class="topbar-link"><i class="fas fa-th-large"></i> 97-Day Plan</a>
            <a href="${parentSubjectHref}" class="topbar-link"><i class="fas fa-arrow-left"></i> ${subMeta.name}</a>
        </nav>
    </header>

    <main class="micro-container" id="main-content">
        <!-- Sleek Top Breadcrumb Trail -->
        <nav class="breadcrumb-trail" aria-label="Breadcrumb">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <span class="separator"><i class="fas fa-chevron-right"></i></span>
            <a href="/upsc-aso/">UPSC ASO Hub</a>
            <span class="separator"><i class="fas fa-chevron-right"></i></span>
            <a href="${parentSubjectHref}">${subMeta.name}</a>
            <span class="separator"><i class="fas fa-chevron-right"></i></span>
            <span class="current-page">${topic.title}</span>
        </nav>

        <!-- Hero Header -->
        <section class="micro-hero">
            <div class="hero-meta-badges">
                <span class="hero-badge day-badge"><i class="fas fa-calendar-day"></i> Day ${topic.day} Study Module</span>
                <span class="hero-badge"><i class="fas fa-layer-group"></i> ${subMeta.phase}</span>
                <span class="hero-badge"><i class="fas fa-clock"></i> 45-60 min Master Cycle</span>
            </div>
            <h1>${topic.title}</h1>
            <p class="hero-desc">Textbook-grade UPSC Air Safety Officer deep-dive: Comprehensive theoretical foundations, analytical derivations, engineering reference data, DGCA/ICAO airworthiness integration, 14 practice MCQs, and timed mini-test.</p>
        </section>

        <!-- Dedicated Air Safety Officer & Aircraft Operations Relevance Banner -->
        <div class="aso-mission-banner">
            <div class="aso-mission-header">
                <div class="aso-mission-title">
                    <i class="fas fa-plane-circle-check"></i> How This Topic Is Useful for Air Safety Officers &amp; Aircraft Operations
                </div>
                <span class="aso-mission-tag">DGCA CAR &amp; ICAO Mandate</span>
            </div>
            <p class="aso-mission-intro">
                In aviation operations and UPSC ASO assessments, this parameter is critical across 4 core operational pillars:
            </p>
            ${asoRelevanceHtml}
        </div>

        <!-- 4 Primary Navigation Tabs -->
        <div class="tab-strip" role="tablist">
            <button class="tab-btn active" role="tab" aria-selected="true" onclick="switchMicroTab('tab-concepts', this)">
                <i class="fas fa-book-open"></i> 1. Concepts & 8 Pillars
            </button>
            <button class="tab-btn" role="tab" aria-selected="false" onclick="switchMicroTab('tab-practice', this)">
                <i class="fas fa-tasks"></i> 2. UPSC Practice Questions (14 MCQs)
            </button>
            <button class="tab-btn" role="tab" aria-selected="false" onclick="switchMicroTab('tab-minitest', this)">
                <i class="fas fa-stopwatch"></i> 3. Timed Mini Test (+3/-1)
            </button>
            <button class="tab-btn" role="tab" aria-selected="false" onclick="switchMicroTab('tab-flashcards', this)">
                <i class="fas fa-brain"></i> 4. Active Recall & Summary
            </button>
        </div>

        <!-- ==================== TAB 1: CONCEPTS & 8 PILLARS ==================== -->
        <section id="tab-concepts" class="tab-panel active" role="tabpanel">
            <!-- Pillar 1: Formal Definition -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-file-contract"></i> Pillar 1: Formal Technical Definition & Nomenclature</h2>
                <div class="pillar-content">
                    ${data.pillar1_definition || ''}
                </div>
            </div>

            <!-- Pillar 2: Physical Mechanism -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-atom"></i> Pillar 2: Microscopic Physics & Continuum Mechanics</h2>
                <div class="pillar-content">
                    ${data.pillar2_physical_mechanism || ''}
                </div>
            </div>

            <!-- Pillar 3: Derivation & Equations -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-square-root-alt"></i> Pillar 3: Mathematical Derivations & Governing Laws</h2>
                <div class="pillar-content">
                    ${data.pillar3_derivation || ''}
                </div>
            </div>

            <!-- Pillar 4: Dimensions & Units -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-ruler-combined"></i> Pillar 4: Dimensional Analysis, SI/CGS Units & Conversion Factors</h2>
                <div class="pillar-content">
                    ${data.pillar4_dimensions_units || ''}
                </div>
            </div>

            <!-- Pillar 5: Reference Data Table -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-table"></i> Pillar 5: Aviation Engineering Reference Data</h2>
                <div class="pillar-content">
                    ${data.pillar5_engineering_table || ''}
                </div>
            </div>

            <!-- Pillar 6: Airworthiness & Flight Safety -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-plane-shield"></i> Pillar 6: Aircraft Airworthiness, Systems & DGCA CAR / ICAO Compliance</h2>
                <div class="pillar-content">
                    ${data.pillar6_airworthiness_safety || ''}
                </div>
            </div>

            <!-- Pillar 7: Examiner Traps -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-exclamation-triangle text-amber-400"></i> Pillar 7: High-Frequency UPSC Examiner Traps & Misconceptions</h2>
                <div class="pillar-content">
                    ${data.pillar7_examiner_traps || ''}
                </div>
            </div>

            <!-- Pillar 8: Worked Aircraft Numerical -->
            <div class="pillar-card">
                <h2 class="pillar-title"><i class="fas fa-calculator text-cyan-400"></i> Pillar 8: Step-by-Step Worked Aircraft Numerical Problem</h2>
                <div class="pillar-content">
                    ${numericalHtml}
                </div>
            </div>
        </section>

        <!-- ==================== TAB 2: PRACTICE QUESTIONS ==================== -->
        <section id="tab-practice" class="tab-panel" role="tabpanel">
            <div style="margin-bottom:1.5rem;color:var(--text-sub);font-size:0.95rem;">
                <i class="fas fa-info-circle text-cyan-400"></i> Click an option to instantly verify your answer and unlock the in-depth technical rationale.
            </div>
            ${practiceQuestionsHtml}
        </section>

        <!-- ==================== TAB 3: TIMED MINI TEST ==================== -->
        <section id="tab-minitest" class="tab-panel" role="tabpanel">
            <div class="test-header-bar">
                <div class="test-info">
                    <div>
                        <strong style="color: #0f172a;">UPSC Simulation Test</strong>
                        <div style="font-size:0.8rem;color:var(--text-muted);">10 Questions • +3 Correct • -1 Incorrect</div>
                    </div>
                </div>
                <div class="test-timer" id="test-timer-display"><i class="fas fa-stopwatch"></i> 15:00</div>
            </div>

            <div id="test-questions-wrapper">
                ${miniTestQuestionsHtml}
            </div>

            <div style="text-align:center;margin-top:2rem;">
                <button class="test-submit-btn" id="submit-test-btn" onclick="submitMiniTest()">
                    <i class="fas fa-paper-plane"></i> Submit Test & View Analysis
                </button>
            </div>

            <div class="test-result-box" id="test-result-box">
                <h3 style="color: #0f172a;margin-top:0;">Test Performance Analysis</h3>
                <div class="score-big" id="test-score-display">0 / 30</div>
                <p id="test-score-feedback" style="color:var(--text-sub);"></p>
                <button class="complete-btn" style="margin:1rem auto 0;" onclick="reviewTestAnswers()">
                    <i class="fas fa-search"></i> Review Explanations
                </button>
            </div>
        </section>

        <!-- ==================== TAB 4: FLASHCARDS ==================== -->
        <section id="tab-flashcards" class="tab-panel" role="tabpanel">
            <div style="margin-bottom:1.5rem;color:var(--text-sub);font-size:0.95rem;">
                <i class="fas fa-lightbulb text-amber-400"></i> Interactive Active Recall Cards: Click any card to flip between the question and the formula/takeaway.
            </div>
            <div class="flashcards-grid">
                ${flashcardsHtml}
            </div>
        </section>

        <!-- Bottom Action Bar -->
        <div class="bottom-actions">
            <a href="${parentSubjectHref}" class="action-link"><i class="fas fa-arrow-left"></i> Back to ${subMeta.name}</a>
            <button class="complete-btn" id="mark-topic-btn" onclick="toggleTopicCompletion('${topic.slug}')">
                <i class="far fa-check-circle"></i> Mark as Mastered
            </button>
            <a href="/upsc-aso/" class="action-link">Syllabus Tracker <i class="fas fa-arrow-right"></i></a>
        </div>
    </main>

    <footer class="micro-footer">
        <div class="footer-content">
            <p>© 2026 SJMaths • Dedicated UPSC Air Safety Officer (ASO) Preparation Hub</p>
            <p class="footer-sub">Aviation Fluid Dynamics &amp; Airworthiness Compliance • Standardized for DGCA / UPSC Exam</p>
        </div>
    </footer>

    <script>
    // Tab Switcher with MathJax Typeset Trigger
    function switchMicroTab(tabId, btn) {
        document.querySelectorAll('.tab-strip .tab-btn').forEach(b => {
            b.classList.remove('active');
            b.setAttribute('aria-selected', 'false');
        });
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        const activePanel = document.getElementById(tabId);
        if (activePanel) activePanel.classList.add('active');

        // Re-typeset MathJax formulas in newly displayed tab
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise();
        }
    }

    // Practice Quiz Option Handler
    function handleQuizSelect(optEl, qNum, chosenIdx, correctIdx) {
        const parentCard = document.getElementById('practice-q-' + qNum);
        if (!parentCard) return;
        
        // Prevent re-selection
        if (parentCard.dataset.answered) return;
        parentCard.dataset.answered = 'true';

        const allOpts = parentCard.querySelectorAll('.quiz-option');
        if (chosenIdx === correctIdx) {
            optEl.classList.add('correct');
        } else {
            optEl.classList.add('incorrect');
            allOpts[correctIdx].classList.add('correct');
        }

        const expBox = document.getElementById('practice-exp-' + qNum);
        if (expBox) {
            expBox.style.display = 'block';
            if (window.MathJax && window.MathJax.typesetPromise) {
                window.MathJax.typesetPromise([expBox]);
            }
        }
    }

    // Timed Mini Test Engine
    const userTestAnswers = {};
    let testSecondsLeft = 900; // 15 mins
    let testTimerInterval = null;

    function startTimer() {
        testTimerInterval = setInterval(() => {
            testSecondsLeft--;
            const mins = Math.floor(testSecondsLeft / 60);
            const secs = testSecondsLeft % 60;
            const display = document.getElementById('test-timer-display');
            if (display) {
                display.innerHTML = '<i class="fas fa-stopwatch"></i> ' + 
                    (mins < 10 ? '0' : '') + mins + ':' + (secs < 10 ? '0' : '') + secs;
            }
            if (testSecondsLeft <= 0) {
                clearInterval(testTimerInterval);
                submitMiniTest();
            }
        }, 1000);
    }
    startTimer();

    function handleTestSelect(optEl, qNum, chosenIdx) {
        const qItem = document.getElementById('test-q-' + qNum);
        if (!qItem) return;
        qItem.querySelectorAll('.test-option').forEach(o => o.classList.remove('selected'));
        optEl.classList.add('selected');
        userTestAnswers[qNum] = chosenIdx;
    }

    function submitMiniTest() {
        if (testTimerInterval) clearInterval(testTimerInterval);
        document.getElementById('submit-test-btn').style.display = 'none';

        let correct = 0;
        let incorrect = 0;
        let unattempted = 0;

        document.querySelectorAll('.test-question-item').forEach((qEl, idx) => {
            const qNum = idx + 1;
            const correctIdx = parseInt(qEl.dataset.correct, 10);
            const chosen = userTestAnswers[qNum];

            const opts = qEl.querySelectorAll('.test-option');
            if (chosen === undefined) {
                unattempted++;
            } else if (chosen === correctIdx) {
                correct++;
                opts[chosen].classList.add('correct');
            } else {
                incorrect++;
                opts[chosen].classList.add('incorrect');
                opts[correctIdx].classList.add('correct');
            }
        });

        const totalScore = (correct * 3) - (incorrect * 1);
        const resultBox = document.getElementById('test-result-box');
        resultBox.style.display = 'block';
        document.getElementById('test-score-display').innerText = totalScore + ' / 30';
        document.getElementById('test-score-feedback').innerText = 
            'Correct: ' + correct + ' (+ ' + (correct*3) + ') | Incorrect: ' + incorrect + ' (- ' + incorrect + ') | Unattempted: ' + unattempted;
        
        resultBox.scrollIntoView({ behavior: 'smooth' });
    }

    function reviewTestAnswers() {
        document.querySelectorAll('.test-explanation').forEach(e => {
            e.style.display = 'block';
        });
        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise();
        }
    }

    // Spaced Repetition Completion Persistence
    function toggleTopicCompletion(slug) {
        const key = 'aso_topic_done_' + slug;
        const btn = document.getElementById('mark-topic-btn');
        const isDone = localStorage.getItem(key) === 'true';
        if (isDone) {
            localStorage.removeItem(key);
            btn.classList.remove('marked');
            btn.innerHTML = '<i class="far fa-check-circle"></i> Mark as Mastered';
        } else {
            localStorage.setItem(key, 'true');
            btn.classList.add('marked');
            btn.innerHTML = '<i class="fas fa-check-circle"></i> Mastered!';
        }
    }

    // Init Completion Button State
    document.addEventListener('DOMContentLoaded', () => {
        const key = 'aso_topic_done_${topic.slug}';
        if (localStorage.getItem(key) === 'true') {
            const btn = document.getElementById('mark-topic-btn');
            if (btn) {
                btn.classList.add('marked');
                btn.innerHTML = '<i class="fas fa-check-circle"></i> Mastered!';
            }
        }
    });
    </script>
</body>
</html>`;
}

// ── 7. Single Topic Processing Runner ─────────────────────────────────────── //
export async function processTopic(topic, options = {}) {
  const model = options.model || 'gemini-3.5-flash-lite';
  const force = options.force || false;
  const dryRun = options.dryRun || false;

  console.log(`\n======================================================`);
  console.log(`Processing [#${topic.id}/544] Day ${topic.day}: "${topic.title}"`);
  console.log(`Target: ${topic.filePath}`);
  console.log(`======================================================`);

  if (dryRun) {
    console.log('[DRY-RUN] Skipped API call and file generation.');
    return { status: 'dry-run' };
  }

  // Ensure target folder exists
  const targetDir = path.dirname(path.resolve(topic.filePath));
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  // Build prompt
  const prompt = buildMicrotopicPrompt(topic);

  // Call Gemini
  const startTime = Date.now();
  console.log(`Calling Gemini API (${model})...`);
  const data = await callGeminiWithRetry(prompt, model);
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.log(`Gemini response received in ${elapsed}s.`);

  // Validate output fields
  if (!data || typeof data !== 'object' || !data.pillar1_definition || !data.pillar3_derivation) {
    throw new Error('Incomplete data received from Gemini API');
  }

  // Render HTML
  const finalHtml = renderMicrotopicHtml(topic, data);

  // Atomic write
  const targetPath = path.resolve(topic.filePath);
  const tempPath = targetPath + '.tmp';
  fs.writeFileSync(tempPath, finalHtml, 'utf8');
  fs.renameSync(tempPath, targetPath);

  console.log(`Successfully generated and written: ${topic.filePath} (${finalHtml.length} bytes)`);

  return {
    status: 'success',
    elapsedSeconds: parseFloat(elapsed),
    bytes: finalHtml.length,
    timestamp: new Date().toISOString()
  };
}

// ── 8. Batch CLI Runner ───────────────────────────────────────────────────── //
async function runCli() {
  const args = process.argv.slice(2);
  let filterDay = null;
  let filterId = null;
  let filterRange = null;
  let runAll = false;
  let force = false;
  let dryRun = false;
  let model = 'gemini-3.5-flash-lite';
  let delayMs = 2000;
  let selectedKey = null;

  for (const arg of args) {
    if (arg.startsWith('--day=')) filterDay = parseInt(arg.split('=')[1], 10);
    else if (arg.startsWith('--id=')) filterId = parseInt(arg.split('=')[1], 10);
    else if (arg.startsWith('--range=')) {
      const [start, end] = arg.split('=')[1].split('-').map(Number);
      filterRange = { start, end };
    }
    else if (arg === '--all') runAll = true;
    else if (arg === '--force') force = true;
    else if (arg === '--dry-run') dryRun = true;
    else if (arg.startsWith('--model=')) model = arg.split('=')[1];
    else if (arg.startsWith('--delay=')) delayMs = parseInt(arg.split('=')[1], 10);
    else if (arg.startsWith('--key=')) selectedKey = arg.split('=')[1];
  }

  // Configure KeyManager
  if (selectedKey || process.env.ACTIVE_GEMINI_KEY) {
    keyManager.selectKey(selectedKey || process.env.ACTIVE_GEMINI_KEY);
  }
  keyManager.printSummary();

  const manifestPath = path.resolve('upsc-aso/all_544_microtopics.json');
  if (!fs.existsSync(manifestPath)) {
    console.error('ERROR: all_544_microtopics.json manifest not found.');
    process.exit(1);
  }

  const allTopics = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  let targetTopics = allTopics;

  if (filterId) {
    targetTopics = allTopics.filter(t => t.id === filterId);
  } else if (filterDay) {
    targetTopics = allTopics.filter(t => t.day === filterDay);
  } else if (filterRange) {
    targetTopics = allTopics.filter(t => t.id >= filterRange.start && t.id <= filterRange.end);
  } else if (!runAll) {
    console.log(`
Usage: node upsc-aso/generate_microtopics_batch.mjs [options]

Options:
  --day=<n>         Generate all microtopics for Day <n> (e.g. --day=1)
  --id=<n>          Generate single microtopic by ID (e.g. --id=3)
  --range=<s-e>     Generate range of IDs (e.g. --range=1-7)
  --all             Generate all 544 microtopics
  --force           Force regenerate even if already completed
  --dry-run         Preview matched topics without calling API
  --model=<name>    Gemini model name (default: gemini-3.5-flash-lite)
  --delay=<ms>      Delay in ms between API calls (default: 2000)
  --key=<sel>       Select API key from pool (e.g. --key=1, --key=GEMINI_API_KEY_1)
    `);
    process.exit(0);
  }

  console.log(`Found ${targetTopics.length} matching microtopics to process.`);
  const progress = loadProgress();

  let completedCount = 0;
  let skippedCount = 0;
  let failedCount = 0;

  for (const topic of targetTopics) {
    if (!force && progress.completed[topic.id]) {
      console.log(`[SKIP] Topic #${topic.id} "${topic.title}" already completed. (Use --force to regenerate)`);
      skippedCount++;
      continue;
    }

    try {
      const res = await processTopic(topic, { model, force, dryRun });
      if (!dryRun) {
        progress.completed[topic.id] = {
          title: topic.title,
          day: topic.day,
          filePath: topic.filePath,
          ...res
        };
        delete progress.failed[topic.id];
        saveProgress(progress);
        completedCount++;
      }
    } catch (err) {
      console.error(`[ERROR] Failed to process #${topic.id} "${topic.title}":`, err.message);
      progress.failed[topic.id] = {
        title: topic.title,
        day: topic.day,
        error: err.message,
        timestamp: new Date().toISOString()
      };
      saveProgress(progress);
      failedCount++;
    }

    if (delayMs > 0 && !dryRun) {
      console.log(`Waiting ${delayMs}ms before next request...`);
      await new Promise(r => setTimeout(r, delayMs));
    }
  }

  console.log(`\n======================================================`);
  console.log(`BATCH FINISHED:`);
  console.log(` - Completed: ${completedCount}`);
  console.log(` - Skipped:   ${skippedCount}`);
  console.log(` - Failed:    ${failedCount}`);
  console.log(`======================================================\n`);
}

// Run if called directly
runCli().catch(err => {
  console.error('Fatal CLI Error:', err);
  process.exit(1);
});
