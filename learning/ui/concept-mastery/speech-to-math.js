// Speech-to-Math Parser & Grammar Compiler
// Converts spoken natural language phrases into mathematical notation and structured field intents.

const SMALL_NUMBERS = {
  'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
  'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
  'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
  'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19
};

const TENS_NUMBERS = {
  'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
  'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90
};

const SUPERSCRIPTS = {
  '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
  '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
  '+': '⁺', '-': '⁻', 'n': 'ⁿ', 'm': 'ᵐ', 'x': 'ˣ'
};

export class SpeechToMathParser {
  constructor() {}

  toSuperscript(numStr) {
    return String(numStr).split('').map(ch => SUPERSCRIPTS[ch] || ch).join('');
  }

  wordsToNumbers(text) {
    if (!text || typeof text !== 'string') return '';

    // Split text into tokens keeping punctuation / whitespace
    const tokens = text.toLowerCase().replace(/[,]/g, ' ').split(/\s+/).filter(Boolean);
    const resultTokens = [];
    let currentNumber = null;
    let currentScale = 0;

    for (let i = 0; i < tokens.length; i++) {
      const token = tokens[i];

      if (token in SMALL_NUMBERS) {
        const val = SMALL_NUMBERS[token];
        if (currentNumber === null) {
          currentNumber = val;
        } else {
          currentNumber += val;
        }
      } else if (token in TENS_NUMBERS) {
        const val = TENS_NUMBERS[token];
        if (currentNumber === null) {
          currentNumber = val;
        } else {
          currentNumber += val;
        }
      } else if (token === 'hundred') {
        if (currentNumber === null) currentNumber = 1;
        currentNumber *= 100;
      } else if (token === 'thousand') {
        if (currentNumber === null) currentNumber = 1;
        currentNumber *= 1000;
        currentScale += currentNumber;
        currentNumber = 0;
      } else if (token === 'and' && currentNumber !== null && i + 1 < tokens.length && (tokens[i + 1] in SMALL_NUMBERS || tokens[i + 1] in TENS_NUMBERS)) {
        // "two hundred and five" -> skip "and"
        continue;
      } else {
        if (currentNumber !== null) {
          resultTokens.push(String(currentScale + currentNumber));
          currentNumber = null;
          currentScale = 0;
        }
        resultTokens.push(token);
      }
    }

    if (currentNumber !== null) {
      resultTokens.push(String(currentScale + currentNumber));
    }

    return resultTokens.join(' ');
  }

  parse(rawText) {
    if (!rawText || typeof rawText !== 'string') return '';

    // Step 1: Normalize number words to digits
    let text = this.wordsToNumbers(rawText);

    // Step 2: Clean speech filler artifacts and phonetic corrections
    text = text
      .replace(/\bh\s*c\s*f\b/gi, 'HCF')
      .replace(/\bl\s*c\s*m\b/gi, 'LCM')
      .replace(/\bat\s+cf\b/gi, 'HCF')
      .replace(/\bel\s+see\s+em\b/gi, 'LCM')
      .replace(/\bpie\b/gi, 'π')
      .replace(/\bpi\b/gi, 'π');

    // Step 3: Handle square roots and radicals
    text = text
      .replace(/\b(?:square\s+root\s+of|under\s+root|root)\s*([a-z0-9]+)/gi, '√$1');

    // Step 4: Handle exponents and powers
    // e.g. "3 to the power of 4", "5 raised to 2", "3 power 2"
    text = text.replace(/([a-z0-9]+)\s+(?:to\s+the\s+power\s+of|raised\s+to\s+the\s+power\s+of|raised\s+to|raise\s+to|to\s+the\s+power|power)\s+([0-9]+|[a-z])/gi, (match, base, exp) => {
      return `${base}${this.toSuperscript(exp)}`;
    });

    // "x squared", "3 squared"
    text = text.replace(/([a-z0-9]+)\s+squared\b/gi, (match, base) => `${base}²`);
    // "x cubed", "2 cubed"
    text = text.replace(/([a-z0-9]+)\s+cubed\b/gi, (match, base) => `${base}³`);

    // Step 5: Arithmetic Operators
    text = text
      .replace(/\b(?:multiplied\s+by|times|into|star)\b/gi, '×')
      .replace(/\b(?:divided\s+by|over)\b/gi, '÷')
      .replace(/\b(?:plus|add)\b/gi, '+')
      .replace(/\b(?:minus|subtract)\b/gi, '-')
      .replace(/\b(?:is\s+equal\s+to|equal\s+to|equals)\b/gi, '=');

    // Normalize spacing around math operators
    text = text
      .replace(/\s*([+×÷=])\s*/g, ' $1 ')
      .replace(/\s*-\s*/g, ' - ')
      .replace(/\s+/g, ' ')
      .trim();

    // Clean space between coefficients and single-letter variable powers: e.g. "5 q²" -> "5q²", "2 x" -> "2x"
    text = text.replace(/(\d+)\s+([a-z][²³⁴⁵⁶⁷⁸⁹ⁿ]?)(?=\s|$|[+×÷=\-])/gi, (match, d, v) => {
      // Don't collapse English words like "5 is" or "5 in"
      if (v === 'is' || v === 'in' || v === 'if' || v === 'as' || v === 'at' || v === 'or' || v === 'an') {
        return match;
      }
      if (v.length === 1 && !/[pqxyzabckmn]/i.test(v)) {
        return match;
      }
      return `${d}${v}`;
    });

    return text;
  }

  extractFieldIntent(rawText) {
    if (!rawText || typeof rawText !== 'string') return null;

    const normalized = this.wordsToNumbers(rawText);

    // 1. Check Factor Ladder Divisor & Quotient
    const divisorMatch = normalized.match(/(?:prime\s+)?divisor\s+(?:is\s+)?([0-9]+)/i);
    const quotientMatch = normalized.match(/quotient\s+(?:is\s+)?([0-9]+)/i);
    if (divisorMatch || quotientMatch) {
      return {
        type: 'ladder',
        divisor: divisorMatch ? divisorMatch[1] : null,
        quotient: quotientMatch ? quotientMatch[1] : null
      };
    }

    // 2. Check HCF and LCM dual values
    const hcfMatch = normalized.match(/\bhcf\b\s+(?:is\s+)?([0-9]+)/i);
    const lcmMatch = normalized.match(/\blcm\b\s+(?:is\s+)?([0-9]+)/i);
    if (hcfMatch || lcmMatch) {
      return {
        type: 'hcf_lcm',
        hcf: hcfMatch ? hcfMatch[1] : null,
        lcm: lcmMatch ? lcmMatch[1] : null
      };
    }

    return null;
  }

  extractOptionIndex(rawText) {
    if (!rawText || typeof rawText !== 'string') return null;

    const normalized = this.wordsToNumbers(rawText).trim().toLowerCase();

    // "option A" -> 0, "option B" -> 1, "option C" -> 2, "option D" -> 3
    const letterMatch = normalized.match(/(?:select\s+|choose\s+)?(?:option|choice)\s+([a-d])/i);
    if (letterMatch) {
      return letterMatch[1].toLowerCase().charCodeAt(0) - 'a'.charCodeAt(0);
    }

    // "option 1" -> 0, "option 2" -> 1
    const digitMatch = normalized.match(/(?:select\s+|choose\s+)?(?:option|choice)\s+([1-9])/i);
    if (digitMatch) {
      return parseInt(digitMatch[1], 10) - 1;
    }

    // "first option", "second choice", etc.
    if (/\b(?:first|1st)\s+(?:option|choice)\b/i.test(normalized)) return 0;
    if (/\b(?:second|2nd)\s+(?:option|choice)\b/i.test(normalized)) return 1;
    if (/\b(?:third|3rd)\s+(?:option|choice)\b/i.test(normalized)) return 2;
    if (/\b(?:fourth|4th)\s+(?:option|choice)\b/i.test(normalized)) return 3;

    return null;
  }
}

// Voice-to-Math Interactive Controller
export class VoiceMathController {
  constructor(app) {
    this.app = app;
    this.parser = new SpeechToMathParser();
    this.recognition = null;
    this.isListening = false;
    this.activeTargetInputId = null;
    this.currentSpokenText = '';
    this.currentMathText = '';
    this.isGuideModalOpen = false;
    this.initRecognition();
  }

  isSupported() {
    return typeof window !== 'undefined' && ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window);
  }

  initRecognition() {
    if (!this.isSupported()) return;
    try {
      const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
      this.recognition = new SpeechRec();
      this.recognition.continuous = false;
      this.recognition.interimResults = true;
      this.recognition.lang = 'en-US';

      this.recognition.onstart = () => {
        this.isListening = true;
        this.updateListeningUI(true);
      };

      this.recognition.onresult = (event) => {
        let interim = '';
        let final = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
          if (event.results[i].isFinal) {
            final += event.results[i][0].transcript;
          } else {
            interim += event.results[i][0].transcript;
          }
        }

        const raw = final || interim;
        this.currentSpokenText = raw;
        this.currentMathText = this.parser.parse(raw);
        this.updatePreviewUI(raw, this.currentMathText, Boolean(final));

        if (final) {
          this.handleFinalResult(final, this.currentMathText);
        }
      };

      this.recognition.onerror = (event) => {
        console.warn('Speech recognition warning:', event.error);
        this.isListening = false;
        this.updateListeningUI(false);
      };

      this.recognition.onend = () => {
        this.isListening = false;
        this.updateListeningUI(false);
      };
    } catch (e) {
      console.warn('SpeechRecognition init error:', e);
    }
  }

  toggle(targetInputId) {
    if (!this.isSupported()) {
      alert('Voice math input is supported in Chrome, Edge, Safari, and Chromium Android browsers. Please ensure microphone permissions are allowed.');
      return;
    }
    if (this.isListening) {
      this.stop();
    } else {
      this.start(targetInputId);
    }
  }

  start(targetInputId) {
    if (!this.recognition) this.initRecognition();
    if (!this.recognition) return;
    if (targetInputId) this.activeTargetInputId = targetInputId;
    try {
      if (this.app?.audio) this.app.audio.click();
      this.recognition.start();
    } catch (e) {
      // Already running or starting
    }
  }

  stop() {
    if (this.recognition && this.isListening) {
      try {
        this.recognition.stop();
      } catch (e) {}
    }
    this.isListening = false;
    this.updateListeningUI(false);
  }

  handleFinalResult(rawSpoken, parsedMath) {
    // 1. Option choice selection in MCQ mode
    const optIdx = this.parser.extractOptionIndex(rawSpoken);
    if (optIdx !== null) {
      const stepOptBtns = document.querySelectorAll('.step-opt-btn');
      const singleOptBtns = document.querySelectorAll('.single-opt-btn');
      if (stepOptBtns.length > optIdx) {
        stepOptBtns[optIdx].click();
        return;
      } else if (singleOptBtns.length > optIdx) {
        singleOptBtns[optIdx].click();
        return;
      }
    }

    // 2. Multi-field intent (e.g. Divisor & Quotient, or HCF & LCM)
    const fieldIntent = this.parser.extractFieldIntent(rawSpoken);
    if (fieldIntent) {
      if (fieldIntent.type === 'ladder') {
        const divInput = document.getElementById('step-input-divisor');
        const quoInput = document.getElementById('step-input-quotient');
        if (fieldIntent.divisor && divInput) {
          divInput.value = fieldIntent.divisor;
          divInput.dispatchEvent(new Event('input', { bubbles: true }));
          this.pulseField(divInput);
        }
        if (fieldIntent.quotient && quoInput) {
          quoInput.value = fieldIntent.quotient;
          quoInput.dispatchEvent(new Event('input', { bubbles: true }));
          this.pulseField(quoInput);
        }
        if (this.app?.audio) this.app.audio.success();
        return;
      } else if (fieldIntent.type === 'hcf_lcm') {
        const hcfInput = document.getElementById('input-obj-hcf') || document.querySelector('[data-key="hcf"]');
        const lcmInput = document.getElementById('input-obj-lcm') || document.querySelector('[data-key="lcm"]');
        if (fieldIntent.hcf && hcfInput) {
          hcfInput.value = fieldIntent.hcf;
          hcfInput.dispatchEvent(new Event('input', { bubbles: true }));
          this.pulseField(hcfInput);
        }
        if (fieldIntent.lcm && lcmInput) {
          lcmInput.value = fieldIntent.lcm;
          lcmInput.dispatchEvent(new Event('input', { bubbles: true }));
          this.pulseField(lcmInput);
        }
        if (this.app?.audio) this.app.audio.success();
        return;
      }
    }

    // 3. Insert into active target field
    let target = this.activeTargetInputId ? document.getElementById(this.activeTargetInputId) : null;
    if (!target) {
      target = document.getElementById('step-input-divisor') ||
               document.getElementById('step-input-quotient') ||
               document.getElementById('step-ans-input') ||
               document.getElementById('single-ans-input') ||
               document.querySelector('.obj-ans-field');
    }

    if (target) {
      target.value = parsedMath;
      target.dispatchEvent(new Event('input', { bubbles: true }));
      this.pulseField(target);
      if (this.app?.audio) this.app.audio.success();
    }
  }

  pulseField(field) {
    if (!field) return;
    field.style.transition = 'box-shadow 0.3s ease, border-color 0.3s ease';
    field.style.borderColor = 'var(--brand-primary)';
    field.style.boxShadow = '0 0 0 3.5px var(--brand-glow)';
    setTimeout(() => {
      field.style.borderColor = '';
      field.style.boxShadow = '';
    }, 650);
  }

  updateListeningUI(isListening) {
    const micBtns = document.querySelectorAll('.btn-voice-input');
    micBtns.forEach(btn => {
      btn.classList.toggle('listening', isListening);
      const label = btn.querySelector('.voice-btn-label');
      if (label) label.textContent = isListening ? 'Listening...' : 'Voice Input';
    });

    const livePill = document.getElementById('voice-live-pill');
    if (livePill) {
      livePill.style.display = isListening ? 'flex' : 'none';
    }
  }

  updatePreviewUI(spoken, parsedMath, isFinal) {
    const liveSpoken = document.getElementById('voice-preview-spoken');
    const liveMath = document.getElementById('voice-preview-math');
    if (liveSpoken) liveSpoken.textContent = `"${spoken}"`;
    if (liveMath) liveMath.textContent = parsedMath || '-';
  }

  getSpokenExamples(stageName, question) {
    const examples = [];
    const q = question || {};

    if (stageName === 'try' || (Array.isArray(q.options) && q.options.length > 0)) {
      examples.push({ spoken: 'Option B', math: 'Selects Choice B', action: 'option', val: 'option B' });
      examples.push({ spoken: 'First option', math: 'Selects Choice 1', action: 'option', val: 'first option' });
    }

    if (stageName === 'think' || (Array.isArray(q.steps) && q.steps.some(s => s.current !== undefined))) {
      examples.push({ spoken: 'divisor 3 quotient 75', math: 'Fills Divisor: 3, Quotient: 75', action: 'fill_ladder', divisor: '3', quotient: '75' });
      examples.push({ spoken: 'divisor 5 quotient 15', math: 'Fills Divisor: 5, Quotient: 15', action: 'fill_ladder', divisor: '5', quotient: '15' });
    }

    if (stageName === 'build' || stageName === 'solve' || stageName === 'apply') {
      if (q.canonical_form || (q.steps && q.steps.length > 0)) {
        examples.push({ spoken: '3 squared times 5', math: '3² × 5', action: 'insert', val: '3² × 5' });
        examples.push({ spoken: '2 cubed into 3 squared', math: '2³ × 3²', action: 'insert', val: '2³ × 3²' });
      }
      if (q.answer && typeof q.answer === 'object') {
        examples.push({ spoken: 'HCF 15 LCM 225', math: 'Fills HCF: 15, LCM: 225', action: 'fill_hcf_lcm', hcf: '15', lcm: '225' });
      }
    }

    if (examples.length === 0) {
      examples.push({ spoken: '3 squared times 5', math: '3² × 5', action: 'insert', val: '3² × 5' });
      examples.push({ spoken: 'root 5 is irrational', math: '√5 is irrational', action: 'insert', val: '√5 is irrational' });
    }

    return examples;
  }

  renderVoiceBar(targetInputId, stageName, currentQuestion) {
    const examples = this.getSpokenExamples(stageName, currentQuestion);

    return `
      <div class="voice-controls-bar" data-target-input="${targetInputId}">
        <div class="voice-actions-row">
          <button type="button" class="btn-voice-input ${this.isListening ? 'listening' : ''}" data-target-input="${targetInputId}" title="Speak math expression or numbers">
            <span class="voice-mic-icon">🎙️</span>
            <span class="voice-btn-label">${this.isListening ? 'Listening...' : 'Speak Math'}</span>
          </button>

          <button type="button" class="btn-voice-guide" id="btn-toggle-voice-guide" title="View what to say cheat sheet">
            <span>💬</span>
            <span>Spoken Examples Guide</span>
          </button>
        </div>

        <div class="voice-live-pill" id="voice-live-pill" style="display: ${this.isListening ? 'flex' : 'none'};">
          <div class="voice-wave-bars">
            <span class="wave-bar"></span>
            <span class="wave-bar"></span>
            <span class="wave-bar"></span>
            <span class="wave-bar"></span>
          </div>
          <div class="voice-live-content">
            <span class="voice-live-tag">Heard:</span>
            <span class="voice-preview-spoken" id="voice-preview-spoken">"${this.currentSpokenText || 'Listening...'}"</span>
            <span class="voice-live-arrow">➜</span>
            <span class="voice-live-tag">Math:</span>
            <span class="voice-preview-math" id="voice-preview-math">${this.currentMathText || '-'}</span>
          </div>
        </div>

        <div class="voice-examples-bar">
          <span class="voice-examples-label">💡 Spoken Examples:</span>
          <div class="voice-examples-list">
            ${examples.map(ex => `
              <button type="button" class="voice-example-chip" data-action="${ex.action}" data-val="${ex.val || ''}" data-divisor="${ex.divisor || ''}" data-quotient="${ex.quotient || ''}" data-hcf="${ex.hcf || ''}" data-lcm="${ex.lcm || ''}" title="Click to try or speak: &quot;${ex.spoken}&quot;">
                <span class="chip-quote">"</span>
                <span class="chip-spoken">${ex.spoken}</span>
                <span class="chip-quote">"</span>
                <span class="chip-arrow">➜</span>
                <span class="chip-math">${ex.math}</span>
              </button>
            `).join('')}
          </div>
        </div>
      </div>
    `;
  }

  renderVoiceGuideModal() {
    return `
      <div class="voice-guide-modal-overlay" id="voice-guide-modal" style="display: none;">
        <div class="voice-guide-modal-card">
          <div class="voice-guide-header">
            <div class="voice-guide-title">
              <span>🎙️</span>
              <span>Voice-to-Math "What to Say" Guide</span>
            </div>
            <button type="button" class="voice-guide-close-btn" id="btn-close-voice-guide">✕</button>
          </div>
          <div class="voice-guide-body">
            <p class="voice-guide-intro">
              You can speak equations, factor ladders, powers, and choices naturally. The platform translates your speech into clean math notation in real time.
            </p>

            <div class="voice-guide-table-wrap">
              <table class="voice-guide-table">
                <thead>
                  <tr>
                    <th>Category</th>
                    <th>What You Can Say</th>
                    <th>Converted Math Output</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Exponents & Powers</strong></td>
                    <td><code>"three squared times five"</code><br><code>"two cubed into three"</code><br><code>"five to the power four"</code></td>
                    <td><span class="vg-math">3² × 5</span><br><span class="vg-math">2³ × 3</span><br><span class="vg-math">5⁴</span></td>
                  </tr>
                  <tr>
                    <td><strong>Numbers & Digits</strong></td>
                    <td><code>"two hundred twenty five"</code><br><code>"seventy five"</code><br><code>"three thousand three hundred seventy five"</code></td>
                    <td><span class="vg-math">225</span><br><span class="vg-math">75</span><br><span class="vg-math">3375</span></td>
                  </tr>
                  <tr>
                    <td><strong>Factor Ladder (Think Stage)</strong></td>
                    <td><code>"divisor three quotient 75"</code><br><code>"prime divisor 5 quotient 15"</code></td>
                    <td><span class="vg-math">Divisor: 3, Quotient: 75</span><br><span class="vg-math">Divisor: 5, Quotient: 15</span></td>
                  </tr>
                  <tr>
                    <td><strong>Dual Fields (HCF & LCM)</strong></td>
                    <td><code>"HCF is 15 and LCM is 225"</code><br><code>"LCM 225 HCF 15"</code></td>
                    <td><span class="vg-math">HCF: 15, LCM: 225</span></td>
                  </tr>
                  <tr>
                    <td><strong>Roots & Proofs</strong></td>
                    <td><code>"root five is irrational"</code><br><code>"p squared equals 5 q squared"</code></td>
                    <td><span class="vg-math">√5 is irrational</span><br><span class="vg-math">p² = 5q²</span></td>
                  </tr>
                  <tr>
                    <td><strong>Multiple Choice Options</strong></td>
                    <td><code>"Option B"</code> / <code>"Option 2"</code><br><code>"First option"</code> / <code>"Second choice"</code></td>
                    <td><span class="vg-math">Selects & checks the option</span></td>
                  </tr>
                  <tr>
                    <td><strong>Arithmetic Operations</strong></td>
                    <td><code>"twenty five divided by five"</code><br><code>"two times three plus five"</code></td>
                    <td><span class="vg-math">25 ÷ 5</span><br><span class="vg-math">2 × 3 + 5</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="voice-guide-footer">
            <button type="button" class="btn-modern btn-modern-primary" id="btn-guide-got-it">Got it, Let's Practice! ✓</button>
          </div>
        </div>
      </div>
    `;
  }

  attachEvents() {
    // 1. Mic Buttons
    document.querySelectorAll('.btn-voice-input').forEach(btn => {
      btn.onclick = () => {
        const targetId = btn.dataset.targetInput || this.activeTargetInputId;
        this.toggle(targetId);
      };
    });

    // 2. Voice Guide Modal
    const guideBtn = document.getElementById('btn-toggle-voice-guide');
    const modal = document.getElementById('voice-guide-modal');
    const closeBtn = document.getElementById('btn-close-voice-guide');
    const gotItBtn = document.getElementById('btn-guide-got-it');

    if (guideBtn && modal) {
      guideBtn.onclick = () => {
        if (this.app?.audio) this.app.audio.click();
        modal.style.display = 'flex';
      };
    }
    const closeModal = () => {
      if (modal) modal.style.display = 'none';
    };
    if (closeBtn) closeBtn.onclick = closeModal;
    if (gotItBtn) gotItBtn.onclick = closeModal;
    if (modal) {
      modal.onclick = (e) => {
        if (e.target === modal) closeModal();
      };
    }

    // 3. Spoken Example Chips
    document.querySelectorAll('.voice-example-chip').forEach(chip => {
      chip.onclick = () => {
        if (this.app?.audio) this.app.audio.click();
        const action = chip.dataset.action;
        const val = chip.dataset.val;

        if (action === 'fill_ladder') {
          const divInput = document.getElementById('step-input-divisor');
          const quoInput = document.getElementById('step-input-quotient');
          if (divInput) {
            divInput.value = chip.dataset.divisor;
            divInput.dispatchEvent(new Event('input', { bubbles: true }));
            this.pulseField(divInput);
          }
          if (quoInput) {
            quoInput.value = chip.dataset.quotient;
            quoInput.dispatchEvent(new Event('input', { bubbles: true }));
            this.pulseField(quoInput);
          }
        } else if (action === 'fill_hcf_lcm') {
          const hcfInput = document.getElementById('input-obj-hcf') || document.querySelector('[data-key="hcf"]');
          const lcmInput = document.getElementById('input-obj-lcm') || document.querySelector('[data-key="lcm"]');
          if (hcfInput) {
            hcfInput.value = chip.dataset.hcf;
            hcfInput.dispatchEvent(new Event('input', { bubbles: true }));
            this.pulseField(hcfInput);
          }
          if (lcmInput) {
            lcmInput.value = chip.dataset.lcm;
            lcmInput.dispatchEvent(new Event('input', { bubbles: true }));
            this.pulseField(lcmInput);
          }
        } else if (action === 'option') {
          this.handleFinalResult(val, val);
        } else if (action === 'insert' && val) {
          let target = this.activeTargetInputId ? document.getElementById(this.activeTargetInputId) : null;
          if (!target) {
            target = document.getElementById('step-input-divisor') ||
                     document.getElementById('step-input-quotient') ||
                     document.getElementById('step-ans-input') ||
                     document.getElementById('single-ans-input') ||
                     document.querySelector('.obj-ans-field');
          }
          if (target) {
            target.value = val;
            target.dispatchEvent(new Event('input', { bubbles: true }));
            this.pulseField(target);
          }
        }
      };
    });
  }
}

