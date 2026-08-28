/**
 * app.js
 * 
 * SJMaths Concept Mastery — Universal 5-Stage Concept & Typology-Driven UI Engine
 * Implements the Full Pedagogical Journey:
 *   1. Concepts (Understand the Core Theory & Theorems)
 *   2. Worked Examples (See Step-by-Step Solved Models)
 *   3. Strategy Choices (Learn the Moves & Sequencing)
 *   4. Guided Calculation (Choose & Compute Math)
 *   5. Notebook Solve & Stepwise Self-Audit (Paper Work & Rubric Audit)
 */

import { getRequestedTopicId, loadTopicData, resolveTopicAssetPaths } from '../../engine/topic-loader.js';

// Synthesized Web Audio feedback
class AudioEffects {
  constructor() {
    this.ctx = null;
    this.isMuted = typeof window !== 'undefined' ? localStorage.getItem('sjmaths_audio_muted') === 'true' : false;
  }

  initContext() {
    if (!this.ctx && typeof window !== 'undefined' && (window.AudioContext || window.webkitAudioContext)) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
  }

  toggleMute() {
    this.isMuted = !this.isMuted;
    if (typeof window !== 'undefined') {
      localStorage.setItem('sjmaths_audio_muted', this.isMuted ? 'true' : 'false');
    }
    return this.isMuted;
  }

  playTone(freq = 440, type = 'sine', duration = 0.15, vol = 0.08) {
    if (this.isMuted) return;
    try {
      this.initContext();
      if (!this.ctx) return;
      if (this.ctx.state === 'suspended') this.ctx.resume();
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      gain.gain.setValueAtTime(vol, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    } catch (e) {}
  }

  click() {
    this.playTone(520, 'sine', 0.05, 0.04);
  }

  success() {
    if (this.isMuted) return;
    try {
      this.initContext();
      if (!this.ctx) return;
      if (this.ctx.state === 'suspended') this.ctx.resume();
      const now = this.ctx.currentTime;
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, now + idx * 0.08);
        gain.gain.setValueAtTime(0.06, now + idx * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.08 + 0.18);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now + idx * 0.08);
        osc.stop(now + idx * 0.08 + 0.18);
      });
    } catch (e) {}
  }

  error() {
    if (this.isMuted) return;
    try {
      this.initContext();
      if (!this.ctx) return;
      if (this.ctx.state === 'suspended') this.ctx.resume();
      const now = this.ctx.currentTime;
      [330, 260].forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(freq, now + idx * 0.1);
        gain.gain.setValueAtTime(0.05, now + idx * 0.1);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.1 + 0.15);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now + idx * 0.1);
        osc.stop(now + idx * 0.1 + 0.15);
      });
    } catch (e) {}
  }
}

export class ConceptMasteryApp {
  constructor({ containerId = 'app-root' } = {}) {
    this.containerId = containerId;
    this.container = null;
    this.audio = new AudioEffects();
    
    // Topic Data
    this.topicData = null;
    this.concepts = [];
    this.workedExamples = [];
    this.questionTypes = [];
    
    // Active Navigation State
    this.currentStageId = 'concepts'; // 'concepts' | 'worked_examples' | 'stage_1_strategy' | 'stage_2_calc' | 'stage_3_notebook'
    this.currentTypeIndex = 0;
    this.currentProblemIndex = 0;
    this.stageProblemIndices = {
      stage_1_strategy: 0,
      stage_2_calc: 1,
      stage_3_notebook: 2
    };
    this.currentStepIndex = 0;
    this.currentWorkedExampleIndex = 0;
    
    // Active Step Interaction State
    this.selectedStrategyIndex = null;
    this.calcInputs = {}; // { divisor, quotient, generic }
    this.stepFeedback = null;
    this.activeFocusInputId = null;
    this.showStepHint = false;
    
    // Stage 3 Notebook State
    this.notebookRubricRevealed = false;
    this.notebookAuditSelections = {}; // { [stepIdx]: true | false }
    
    // Mastery Tracking per Typology: { [type_id]: { stage1_streak, stage2_streak, stage3_verified, is_mastered } }
    this.masteryState = {};
    
    // UI Drawer state
    this.isReferenceDrawerOpen = false;

    // Theme state (Pleasing Dark / Natural Warm Light)
    this.isDarkMode = localStorage.getItem('sjmaths_theme') === 'dark';
    this.applyTheme();
  }

  applyTheme() {
    if (typeof document !== 'undefined') {
      if (this.isDarkMode) {
        document.documentElement.setAttribute('data-theme', 'dark');
      } else {
        document.documentElement.removeAttribute('data-theme');
      }
    }
  }

  toggleTheme() {
    this.isDarkMode = !this.isDarkMode;
    localStorage.setItem('sjmaths_theme', this.isDarkMode ? 'dark' : 'light');
    this.applyTheme();
    this.render();
  }

  async init() {
    this.container = document.getElementById(this.containerId);
    if (!this.container) {
      console.error(`Container #${this.containerId} not found.`);
      return;
    }

    this.renderLoading('Loading curriculum dataset...');

    try {
      const topicId = getRequestedTopicId();
      
      // Dynamically load topic-specific CSS & JS if available
      const assets = resolveTopicAssetPaths(topicId);
      if (assets?.cssPath && typeof document !== 'undefined') {
        let link = document.getElementById('topic-specific-css');
        if (!link) {
          link = document.createElement('link');
          link.id = 'topic-specific-css';
          link.rel = 'stylesheet';
          link.href = assets.cssPath;
          document.head.appendChild(link);
        } else {
          link.href = assets.cssPath;
        }
      }

      this.topicData = await loadTopicData(topicId);
      this.parseCurriculumSections();
      this.loadSavedMasteryState();
      this.render();
    } catch (err) {
      console.error('Failed to initialize topic data:', err);
      this.renderError(err.message || 'Failed to load learning dataset.');
    }
  }

  parseCurriculumSections() {
    this.concepts = Array.isArray(this.topicData.concepts) ? this.topicData.concepts : [];
    this.workedExamples = Array.isArray(this.topicData.worked_examples) ? this.topicData.worked_examples : [];
    if (this.workedExamples.length === 0 && this.topicData.units && this.topicData.units.worked_examples) {
      const legacyExamples = this.topicData.units.worked_examples.examples;
      if (Array.isArray(legacyExamples)) this.workedExamples = legacyExamples;
    }
    
    if (Array.isArray(this.topicData.question_types) && this.topicData.question_types.length > 0) {
      this.questionTypes = this.topicData.question_types;
    } else {
      const legacyPool = [];
      if (this.topicData.units) {
        Object.values(this.topicData.units).forEach(unit => {
          if (Array.isArray(unit.questions)) legacyPool.push(...unit.questions);
          if (Array.isArray(unit.question_pool)) legacyPool.push(...unit.question_pool);
        });
      }
      this.questionTypes = [
        {
          type_id: 'default_type',
          type_title: this.topicData.topic?.title || 'Core Practice',
          description: 'Step-by-step concept mastery practice.',
          pool: legacyPool
        }
      ];
    }
  }

  loadSavedMasteryState() {
    const topicId = this.topicData?.topic?.id || 'default';
    const storageKey = `sjmaths_mastery_${topicId}`;
    const navKey = `sjmaths_nav_${topicId}`;

    try {
      const saved = localStorage.getItem(storageKey);
      if (saved) {
        this.masteryState = JSON.parse(saved);
      }
      const savedNav = localStorage.getItem(navKey);
      if (savedNav) {
        const nav = JSON.parse(savedNav);
        if (nav.currentStageId) this.currentStageId = nav.currentStageId;
        if (nav.currentTypeIndex !== undefined && nav.currentTypeIndex < this.questionTypes.length) {
          this.currentTypeIndex = nav.currentTypeIndex;
        }
        if (nav.currentProblemIndex !== undefined) this.currentProblemIndex = nav.currentProblemIndex;
        if (nav.stageProblemIndices) {
          this.stageProblemIndices = Object.assign({
            stage_1_strategy: 0,
            stage_2_calc: 1,
            stage_3_notebook: 2
          }, nav.stageProblemIndices);
        }
        if (nav.currentStepIndex !== undefined) this.currentStepIndex = nav.currentStepIndex;
        if (nav.currentWorkedExampleIndex !== undefined) this.currentWorkedExampleIndex = nav.currentWorkedExampleIndex;
      }
    } catch (e) {}

    const isAllUnlocked = this.topicData?.topic?.unlock_all_types === true || this.topicData?.unlock_all_types === true;

    this.questionTypes.forEach((qt, idx) => {
      if (!this.masteryState[qt.type_id]) {
        this.masteryState[qt.type_id] = {
          stage1_streak: 0,
          stage2_streak: 0,
          stage3_verified: 0,
          stage2_unlocked: false,
          stage3_unlocked: false,
          is_mastered: false,
          is_unlocked: isAllUnlocked || idx === 0
        };
      } else if (isAllUnlocked) {
        this.masteryState[qt.type_id].is_unlocked = true;
      }
    });
  }

  saveMasteryState() {
    const topicId = this.topicData?.topic?.id || 'default';
    const storageKey = `sjmaths_mastery_${topicId}`;
    const navKey = `sjmaths_nav_${topicId}`;

    try {
      localStorage.setItem(storageKey, JSON.stringify(this.masteryState));
      localStorage.setItem(navKey, JSON.stringify({
        currentStageId: this.currentStageId,
        currentTypeIndex: this.currentTypeIndex,
        currentProblemIndex: this.currentProblemIndex,
        stageProblemIndices: this.stageProblemIndices,
        currentStepIndex: this.currentStepIndex,
        currentWorkedExampleIndex: this.currentWorkedExampleIndex
      }));
    } catch (e) {}
  }

  getCurrentType() {
    return this.questionTypes[this.currentTypeIndex] || this.questionTypes[0];
  }

  getHighestActiveTypeIndex() {
    for (let i = 0; i < this.questionTypes.length; i++) {
      const typeId = this.questionTypes[i].type_id;
      const m = this.masteryState[typeId];
      if (!m || !m.is_mastered) {
        return i;
      }
    }
    return Math.max(0, this.questionTypes.length - 1);
  }

  getCurrentProblem() {
    const type = this.getCurrentType();
    if (!type || !Array.isArray(type.pool) || type.pool.length === 0) return null;
    let pIdx = this.currentProblemIndex;
    if (this.stageProblemIndices && this.stageProblemIndices[this.currentStageId] !== undefined) {
      pIdx = this.stageProblemIndices[this.currentStageId];
    }
    return type.pool[pIdx % type.pool.length];
  }

  getCurrentStep() {
    const problem = this.getCurrentProblem();
    if (!problem || !Array.isArray(problem.steps)) return null;
    return problem.steps[this.currentStepIndex] || problem.steps[0];
  }

  // ==========================================================================
  // RENDER PIPELINE
  // ==========================================================================

  render() {
    if (!this.container || !this.topicData) return;

    this.container.innerHTML = `
      <div class="mastery-app-layout">
        ${this.renderNavbar()}
        
        <main class="mastery-main-content">
          ${this.renderStageStepper()}
          ${this.isPracticingStages() ? this.renderTypologyTabs() : ''}
          
          <div class="stage-workspace-card">
            ${this.renderCurrentStageView()}
          </div>
        </main>

        ${this.renderReferenceDrawer()}
      </div>
    `;

    this.attachEvents();
    this.triggerMathJax();
  }

  isPracticingStages() {
    return ['stage_1_strategy', 'stage_2_calc', 'stage_3_notebook'].includes(this.currentStageId);
  }

  renderNavbar() {
    const topic = this.topicData.topic || {};
    const prevTopic = this.topicData.previous_topic;
    return `
      <header class="mastery-navbar compact">
        <div class="nav-left">
          <a href="/" class="brand-link" title="Return to SJMaths Home">
            <span class="brand-badge">SJMATHS</span>
          </a>
          ${prevTopic ? `
            <a href="${prevTopic.url || `/learning/ui/concept-mastery/?topic=${prevTopic.id}`}" class="btn-nav-action btn-nav-prev" title="Previous Topic: ${prevTopic.title || 'Previous'}">
              <span class="btn-label-desktop">← Prev Topic</span>
              <span class="btn-label-mobile">← Prev</span>
            </a>
          ` : ''}
          <div class="topic-meta-header">
            <span class="topic-title-h1">${topic.title || 'Concept Mastery'}</span>
          </div>
        </div>

        <div class="nav-right">
          <button id="btn-toggle-theme" class="btn-nav-action btn-theme-toggle" title="${this.isDarkMode ? 'Switch to Light Theme' : 'Switch to Dark Theme'}">
            <span class="theme-icon">${this.isDarkMode ? '☀️' : '🌙'}</span>
            <span class="btn-label-desktop">${this.isDarkMode ? 'Light' : 'Dark'}</span>
          </button>
          <button id="btn-toggle-sound" class="btn-nav-icon" title="Toggle Sound">
            ${this.audio.isMuted ? '🔇' : '🔊'}
          </button>
          <button id="btn-toggle-drawer" class="btn-nav-action" title="View Formulas">
            <span class="formula-icon">📖</span>
            <span class="btn-label-desktop">Formula Guide</span>
          </button>
        </div>
      </header>
    `;
  }

  renderStageStepper() {
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id] || { stage1_streak: 0, stage2_streak: 0, stage3_verified: 0 };
    
    const isStage2Unlocked = m.stage2_unlocked || m.stage1_streak >= 2 || m.stage2_streak > 0 || m.is_mastered;
    const isStage3Unlocked = m.stage3_unlocked || m.stage2_streak >= 2 || m.stage3_verified > 0 || m.is_mastered;

    const stages = [
      {
        id: 'concepts',
        label: 'Concepts',
        icon: '💡',
        progressText: 'Theory',
        isDone: true,
        isUnlocked: true
      },
      {
        id: 'worked_examples',
        label: 'Solutions',
        icon: '📖',
        progressText: `${this.workedExamples.length} Examples`,
        isDone: true,
        isUnlocked: true
      },
      {
        id: 'stage_1_strategy',
        label: 'Strategy',
        icon: '🎯',
        progressText: `${m.stage1_streak || 0}/2`,
        isDone: m.stage1_streak >= 2,
        isUnlocked: true
      },
      {
        id: 'stage_2_calc',
        label: 'Guided Calc',
        icon: isStage2Unlocked ? '✏️' : '🔒',
        progressText: `${m.stage2_streak || 0}/2`,
        isDone: m.stage2_streak >= 2,
        isUnlocked: isStage2Unlocked
      },
      {
        id: 'stage_3_notebook',
        label: 'Notebook',
        icon: isStage3Unlocked ? '📝' : '🔒',
        progressText: `${m.stage3_verified || 0}/2`,
        isDone: m.stage3_verified >= 2,
        isUnlocked: isStage3Unlocked
      }
    ];

    return `
      <div class="stage-stepper-bar compact-strip">
        ${stages.map((st, idx) => {
          const isActive = this.currentStageId === st.id;
          return `
            <button 
              class="stage-step-pill ${isActive ? 'active' : ''} ${st.isDone ? 'completed' : ''} ${!st.isUnlocked ? 'locked' : ''}"
              data-stage-id="${st.id}"
              title="${st.label}"
              ${!st.isUnlocked ? 'disabled' : ''}
            >
              <span class="step-icon">${st.icon}</span>
              <span class="step-label">${idx + 1}. ${st.label}</span>
              <span class="step-badge">${st.progressText}</span>
            </button>
          `;
        }).join('')}
      </div>
    `;
  }

  renderTypologyTabs() {
    return `
      <nav class="typology-nav-bar compact" aria-label="Question Types">
        <div class="typology-pill-list">
          ${this.questionTypes.map((qt, idx) => {
            const m = this.masteryState[qt.type_id] || {};
            const isActive = idx === this.currentTypeIndex;
            const isMastered = m.is_mastered;
            const isUnlocked = m.is_unlocked || idx === 0;

            let statusIcon = '🔒';
            if (isMastered) statusIcon = '🏆';
            else if (isActive) statusIcon = '▶';
            else if (isUnlocked) statusIcon = '✓';

            return `
              <button 
                class="typology-pill-btn ${isActive ? 'active' : ''} ${isMastered ? 'mastered' : ''} ${!isUnlocked ? 'locked' : ''}"
                data-type-index="${idx}"
                ${!isUnlocked ? 'disabled' : ''}
              >
                <span class="type-pill-icon">${statusIcon}</span>
                <span class="type-pill-text">${qt.type_title || `Type ${idx + 1}`}</span>
              </button>
            `;
          }).join('')}
        </div>
      </nav>
    `;
  }

  renderCurrentStageView() {
    if (this.currentStageId === 'concepts') {
      return this.renderConceptsView();
    } else if (this.currentStageId === 'worked_examples') {
      return this.renderWorkedExamplesView();
    }

    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id] || {};
    const problem = this.getCurrentProblem();

    if (!problem) {
      return `<div class="empty-state-card"><p>No questions found in this typology pool.</p></div>`;
    }

    if (this.currentStageId === 'stage_1_strategy') {
      return this.renderStage1Strategy(problem, m);
    } else if (this.currentStageId === 'stage_2_calc') {
      return this.renderStage2Calc(problem, m);
    } else if (this.currentStageId === 'stage_3_notebook') {
      return this.renderStage3Notebook(problem, m);
    }

    return ``;
  }

  // ==========================================================================
  // SECTION 1: CONCEPTS (UNDERSTAND)
  // ==========================================================================

  renderConceptsView() {
    return `
      <div class="stage-panel concepts-panel">
        <div class="panel-hero-bar">
          <div class="problem-statement-card">
            <span class="problem-tag">CHAPTER THEORY</span>
            <h2 class="problem-statement-text">Core Definitions & Theorems</h2>
          </div>
        </div>

        <div class="concepts-grid">
          ${this.concepts.map(c => `
            <article class="concept-card">
              <h3 class="concept-card-title">${c.title || c.name}</h3>
              ${c.subtitle ? `<div class="concept-card-subtitle" style="font-size:0.9rem; color:var(--text-muted, #64748b); margin-top:-0.35rem; margin-bottom:0.75rem; font-weight:600;">${c.subtitle}</div>` : ''}
              
              <div class="concept-statement-box">
                <p class="concept-formal-statement">${c.statement || c.summary || ''}</p>
              </div>

              ${c.formula || c.example_math ? `
                <div class="concept-formula-chip">
                  <span class="formula-chip-label">Formula / Rule:</span>
                  <span class="formula-chip-math">\\(${c.formula || c.example_math}\\)</span>
                </div>
              ` : ''}

              ${c.diagram_svg ? `
                <div class="concept-diagram-container" style="margin: 1rem 0; display: flex; justify-content: center; align-items: center; background: var(--bg-surface-elevated, rgba(0,0,0,0.03)); border-radius: 12px; padding: 1rem; border: 1px solid var(--border-color, rgba(0,0,0,0.08));">
                  ${c.diagram_svg}
                </div>
              ` : ''}

              ${Array.isArray(c.points) && c.points.length > 0 ? `
                <div class="concept-points-list" style="margin-top:0.75rem;">
                  <ul style="list-style:none; padding-left:0; margin:0; display:flex; flex-direction:column; gap:0.5rem;">
                    ${c.points.map(p => `
                      <li style="display:flex; align-items:flex-start; gap:0.5rem; font-size:0.95rem; line-height:1.5;">
                        <span style="color:var(--primary, #3b82f6); font-weight:bold;">${p.icon || '•'}</span>
                        <span>${p.text || this.toDisplayText(p)}</span>
                      </li>
                    `).join('')}
                  </ul>
                </div>
              ` : ''}

              ${c.explanation ? `
                <div class="concept-explanation-text" style="margin-top:0.75rem;">
                  <p>${c.explanation.replace(/\n\n/g, '<br><br>')}</p>
                </div>
              ` : ''}

              ${c.trap ? `
                <div class="concept-trap-box">
                  <div class="concept-trap-header">⚠️ COMMON TRAP / MISCONCEPTION:</div>
                  <p class="concept-trap-text">${c.trap}</p>
                </div>
              ` : ''}

              ${Array.isArray(c.notes) && c.notes.length > 0 ? `
                <div class="concept-notes-box" style="margin-top:0.75rem;">
                  <strong>Important Notes:</strong>
                  <ul>
                    ${c.notes.map(n => `<li>${this.toDisplayText(n)}</li>`).join('')}
                  </ul>
                </div>
              ` : ''}
            </article>
          `).join('')}
        </div>

        <div class="stage-footer-actions">
          <button id="btn-goto-examples-bottom" class="btn-primary-action">
            Next: Study Textbook Solutions (All Question Types) →
          </button>
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // SECTION 2: WORKED EXAMPLES (SEE TEXTBOOK-STYLE STEPWISE SOLUTIONS)
  // ==========================================================================

  // ==========================================================================
  // SAFE GENERIC RENDERING HELPERS (no educational object is ever stringified)
  // ==========================================================================

  toDisplayText(value, preferredKeys = []) {
    if (value === null || value === undefined) return '';
    if (typeof value === 'string') return value;
    if (typeof value === 'number' || typeof value === 'boolean') return String(value);
    if (Array.isArray(value)) {
      return value.map(item => this.toDisplayText(item, preferredKeys)).filter(Boolean).join('<br>');
    }
    if (typeof value === 'object') {
      const keys = [...preferredKeys, 'statement', 'action', 'focus', 'text', 'title', 'label', 'name',
        'description', 'summary', 'content', 'explanation', 'reason', 'why', 'value',
        'calculation', 'formula', 'math', 'latex', 'expression', 'answer'];
      for (const key of keys) {
        const v = value[key];
        if (typeof v === 'string' && v.trim()) return v;
        if (typeof v === 'number' || typeof v === 'boolean') return String(v);
      }
      for (const key of keys) {
        const v = value[key];
        if (v && typeof v === 'object') {
          const nested = this.toDisplayText(v, preferredKeys);
          if (nested) return nested;
        }
      }
      return '';
    }
    return '';
  }

  renderWorkedExampleStep(step, index) {
    if (step === null || step === undefined) return '';
    if (typeof step === 'string' || typeof step === 'number' || typeof step === 'boolean') {
      const text = this.toDisplayText(step);
      if (!text) return '';
      return `
              <div class="textbook-step-row">
                <div class="step-num-badge">Step ${index + 1}</div>
                <div class="step-content-col">
                  <p class="step-narrative-statement">${text}</p>
                </div>
              </div>
            `;
    }
    if (typeof step !== 'object') return '';

    const stepNumber = this.toDisplayText(step.step_number ?? step.step_id ?? step.step) || String(index + 1);
    const statement = this.toDisplayText(step.statement ?? step.action ?? step.focus ?? step.narrative ?? step.description ?? step.text, ['statement']);
    const calculation = this.toDisplayText(step.calculation ?? step.working ?? step.math ?? step.formula ?? step.latex ?? step.expression, ['calculation']);
    const reason = this.toDisplayText(step.reason ?? step.why ?? step.justification ?? step.explanation, ['reason']);
    const result = this.toDisplayText(step.result ?? step.classification ?? step.verdict, ['result']);

    if (!statement && !calculation && !reason && !result) return '';

    return `
              <div class="textbook-step-row">
                <div class="step-num-badge">Step ${stepNumber}</div>
                <div class="step-content-col">
                  ${statement ? `<p class="step-narrative-statement">${statement}</p>` : ''}
                  ${calculation ? `<div class="step-math-block">\\[${calculation}\\]</div>` : ''}
                  ${reason ? `<div class="step-reason-bracket"><span class="reason-prefix">Why?</span> ${reason}</div>` : ''}
                  ${result ? `<div class="step-reason-bracket"><span class="reason-prefix">Result:</span> ${result}</div>` : ''}
                </div>
              </div>
            `;
  }

  renderWorkedExamplesView() {
    const ex = this.workedExamples[this.currentWorkedExampleIndex] || this.workedExamples[0];
    if (!ex) {
      return `
        <div class="empty-state-card"><p>No worked examples are available for this topic yet.</p></div>
      `;
    }

    const totalEx = this.workedExamples.length;
    const exNumber = this.currentWorkedExampleIndex + 1;
    const typeLabel = ex.type_label || ex.type_title || `Type ${exNumber}`;
    const exTitle = this.toDisplayText(ex.title ?? ex.type_title ?? `Worked Example ${exNumber}`);
    const problemText = this.toDisplayText(ex.statement ?? ex.problem ?? ex.question);
    const isLastExample = exNumber >= totalEx;

    return `
      <div class="stage-panel worked-examples-panel">
        <div class="panel-hero-bar">
          <div class="problem-statement-card">
            <span class="problem-tag">Worked Example ${exNumber} of ${totalEx}</span>
            <h2 class="problem-statement-text">${exTitle}</h2>
          </div>
        </div>

        <div class="textbook-problem-card">
          <div class="textbook-q-badge">Question (${typeLabel}):</div>
          <h3 class="textbook-problem-text">${problemText}</h3>
        </div>



        <div class="textbook-solution-sheet">
          <div class="solution-header-banner">
            <span class="solution-title-tag">Step-by-Step Solution:</span>
            <span class="solution-hint-tag">Observe how each step is justified</span>
          </div>

          <div class="textbook-stepwise-flow">
            ${Array.isArray(ex.steps) ? ex.steps.map((st, idx) => this.renderWorkedExampleStep(st, idx)).join('') : ''}
          </div>

          ${ex.conclusion ? `
            <div class="textbook-conclusion-block">
              <div class="conclusion-badge">Result:</div>
              <div class="conclusion-body-text">
                ${this.toDisplayText(ex.conclusion).replace(/\n\n/g, '<br><br>')}
              </div>
            </div>
          ` : `
            <div class="textbook-conclusion-block">
              <strong>Final Answer:</strong> ${this.toDisplayText(ex.final_canonical_answer ?? ex.final_answer)}
            </div>
          `}
        </div>


        <div class="stage-footer-actions dual">
          <div class="nav-button-group">
            ${exNumber > 1 ? `
              <button id="btn-prev-example" class="btn-secondary-action">← Previous</button>
            ` : ''}

            ${!isLastExample ? `
              <button id="btn-next-example" class="btn-secondary-action">Next Example (${exNumber + 1} of ${totalEx}) →</button>
            ` : ''}
          </div>

          <button id="btn-start-strategy-practice" class="btn-primary-action" data-target-type="${this.getHighestActiveTypeIndex()}">
            ${isLastExample ? 'Continue to Strategy →' : `Practice ${typeLabel} Questions →`}
          </button>
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // STAGE 3: STRATEGY CHOICES (TRY)
  // ==========================================================================

  renderStage1Strategy(problem, mastery) {
    if (this.showStageSuccessPanel) {
      return this.renderStageSuccessPanel(problem, mastery);
    }
    if (this.showProblemSolutionRecap) {
      return this.renderProblemCompletedRecap(problem, mastery);
    }

    const curType = this.getCurrentType();
    const step = this.getCurrentStep();
    const totalSteps = problem.steps.length;

    return `
      <div class="stage-panel stage-strategy-panel">
        <div class="panel-hero-bar">
          <div class="problem-meta-row">
            <div class="problem-meta-left">
              <span class="problem-tag">Problem ${this.currentProblemIndex + 1}</span>
              <span class="typology-sub-badge">${curType.type_title || ''}</span>
            </div>
            <div class="stage-milestone-pill">
              🎯 ${mastery.stage1_streak || 0}/2 Clean Solves
            </div>
          </div>
          <h2 class="problem-statement-text">${problem.statement}</h2>
        </div>

        <div class="strategy-decision-counter">
          <span class="decision-count-badge">Strategy Question ${this.toDisplayText(step.step_number) || (this.currentStepIndex + 1)} of ${totalSteps}</span>
        </div>


        <div class="active-step-card">
          ${this.currentStepIndex > 0 ? `
            <div class="completed-steps-ledger">
              <div class="ledger-header">
                <span class="ledger-icon">📝</span>
                <span class="ledger-title">Strategy Progress:</span>
              </div>
              <div class="ledger-list">
                ${problem.steps.slice(0, this.currentStepIndex).map(prevStep => `
                  <div class="ledger-step-row">
                    <div class="ledger-step-header">
                      <span class="ledger-check">✓</span>
                      <span class="ledger-step-label">Step ${prevStep.step_number}:</span>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}

          <div class="step-card-meta">
            <span class="step-focus-pill">Step ${step.step_number}: ${step.focus}</span>
          </div>

          <h3 class="strategy-question-title">${step.strategy_question}</h3>

          <div class="strategy-options-list">
            ${(() => {
              if (!this.shuffledStrategyOptions || this.shuffledStrategyStepId !== `${problem.id}_${step.step_number}`) {
                const indexedOptions = step.strategy_options.map((optText, origIdx) => ({
                  origIdx,
                  optText,
                  isCorrect: origIdx === step.correct_strategy_index
                }));
                // Fisher-Yates shuffle
                for (let i = indexedOptions.length - 1; i > 0; i--) {
                  const j = Math.floor(Math.random() * (i + 1));
                  [indexedOptions[i], indexedOptions[j]] = [indexedOptions[j], indexedOptions[i]];
                }
                this.shuffledStrategyOptions = indexedOptions;
                this.shuffledStrategyStepId = `${problem.id}_${step.step_number}`;
              }

              return this.shuffledStrategyOptions.map((item, displayIdx) => {
                const isSelected = this.selectedStrategyIndex === item.origIdx;
                const isFeedbackCorrect = this.stepFeedback && this.stepFeedback.isCorrect;
                const isFeedbackWrong = this.stepFeedback && !this.stepFeedback.isCorrect;
                
                let stateClass = '';
                if (isSelected) {
                  if (isFeedbackCorrect) stateClass = 'correct';
                  else if (isFeedbackWrong) stateClass = 'wrong';
                  else stateClass = 'selected';
                }

                return `
                  <button 
                    class="strategy-option-btn ${stateClass}"
                    data-option-index="${item.origIdx}"
                    ${isFeedbackCorrect ? 'disabled' : ''}
                  >
                    <span class="option-letter">${String.fromCharCode(65 + displayIdx)}</span>
                    <span class="option-content">${item.optText}</span>
                  </button>
                `;
              }).join('');
            })()}
          </div>

          ${this.renderStepFeedbackBox()}
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // STAGE 4: GUIDED CALCULATION (THINK)
  // ==========================================================================

  renderStage2Calc(problem, mastery) {
    if (this.showStageSuccessPanel) {
      return this.renderStageSuccessPanel(problem, mastery);
    }
    if (this.showProblemSolutionRecap) {
      return this.renderProblemCompletedRecap(problem, mastery);
    }

    const curType = this.getCurrentType();
    const step = this.getCurrentStep();
    const totalSteps = problem.steps.length;

    return `
      <div class="stage-panel stage-calc-panel">
        <div class="panel-hero-bar">
          <div class="problem-meta-row">
            <div class="problem-meta-left">
              <span class="problem-tag">Problem ${this.currentProblemIndex + 1}</span>
              <span class="typology-sub-badge">${curType.type_title || ''}</span>
            </div>
            <div class="stage-milestone-pill">
              ✏️ ${mastery.stage2_streak || 0}/2 Clean Solves
            </div>
          </div>
          <h2 class="problem-statement-text">${problem.statement}</h2>
        </div>

        <div class="steps-progress-track">
          ${problem.steps.map((st, sIdx) => {
            const isCompleted = sIdx < this.currentStepIndex;
            const isCurrent = sIdx === this.currentStepIndex;
            const statusClass = isCompleted ? 'completed' : (isCurrent ? 'active' : 'pending');
            return `
              <div class="step-progress-node ${statusClass}">
                <div class="node-circle">${isCompleted ? '✓' : st.step_number}</div>
                <span class="node-label">${st.focus}</span>
              </div>
            `;
          }).join('')}
        </div>

        <div class="active-step-card">
          ${this.currentStepIndex > 0 ? `
            <div class="completed-steps-ledger">
              <div class="ledger-header">
                <span class="ledger-icon">📝</span>
                <span class="ledger-title">Notebook Progress:</span>
              </div>
              <div class="ledger-list">
                ${problem.steps.slice(0, this.currentStepIndex).map(prevStep => `
                  <div class="ledger-step-row">
                    <div class="ledger-step-header">
                      <span class="ledger-check">✓</span>
                      <span class="ledger-step-label">Step ${prevStep.step_number}:</span>
                    </div>
                    <div class="ledger-math">\\[${prevStep.rubric_math || prevStep.calculation || ''}\\]</div>
                  </div>
                `).join('')}
              </div>
            </div>
          ` : ''}

          <div class="step-card-meta">
            <span class="step-focus-pill">Step ${step.step_number}: ${step.focus}</span>
            <button id="btn-toggle-hint" class="btn-hint-toggle ${this.showStepHint ? 'active' : ''}">
              💡 ${this.showStepHint ? 'Hide Hint' : 'Hint'}
            </button>
          </div>

          ${this.showStepHint ? `
            <div class="step-hint-callout">
              <span class="hint-icon">💡</span>
              <div class="hint-text">${step.hint || step.revisit_topic?.tip || 'Re-read the step goal above and check your calculation against it.'}</div>
            </div>
          ` : ''}

          <h3 class="calc-prompt-title">${step.calc_prompt || step.strategy_question}</h3>

          <div class="calc-input-section">
            ${step.calc_template ? `
              <div class="calc-template-box">
                <div class="template-math-display">\\[${this.toDisplayText(step.calc_template.format_latex)}\\]</div>
                <div class="template-fields-row">
                  ${step.calc_template.fields.map(f => `
                    <div class="calc-field-group">
                      <label for="input-calc-${f.key}">${this.toDisplayText(f.label).replace(/\s*\([^)]*\)/g, '')}:</label>
                      <input 
                        type="text" 
                        id="input-calc-${f.key}" 
                        data-calc-field="${f.key}"
                        class="calc-input-box math-field" 
                        placeholder="Enter value" 
                        value="${this.calcInputs[f.key] || ''}"
                        ${this.stepFeedback && this.stepFeedback.isCorrect ? 'disabled' : ''}
                      />
                    </div>
                  `).join('')}
                </div>
              </div>
            ` : (step.expected_divisor !== undefined && step.expected_divisor !== null ? `
              <div class="dual-calc-inputs">
                <div class="calc-field-group">
                  <label for="input-calc-divisor">Prime Divisor:</label>
                  <input 
                    type="text" 
                    id="input-calc-divisor" 
                    data-calc-field="divisor"
                    class="calc-input-box math-field" 
                    placeholder="Prime divisor" 
                    value="${this.calcInputs.divisor || ''}"
                    ${this.stepFeedback && this.stepFeedback.isCorrect ? 'disabled' : ''}
                  />
                </div>
                <div class="calc-field-group">
                  <label for="input-calc-quotient">Resulting Quotient:</label>
                  <input 
                    type="text" 
                    id="input-calc-quotient" 
                    data-calc-field="quotient"
                    class="calc-input-box math-field" 
                    placeholder="Quotient" 
                    value="${this.calcInputs.quotient || ''}"
                    ${this.stepFeedback && this.stepFeedback.isCorrect ? 'disabled' : ''}
                  />
                </div>
              </div>
            ` : `
              <div class="single-calc-input">
                <input 
                  type="text" 
                  id="input-calc-generic" 
                  data-calc-field="generic"
                  class="calc-input-box math-field full-width" 
                  placeholder="Enter number..." 
                  value="${this.calcInputs.generic || ''}"
                  ${this.stepFeedback && this.stepFeedback.isCorrect ? 'disabled' : ''}
                />
              </div>
            `)}

            ${this.renderMathKeypad()}
          </div>

          <div class="step-actions-row">
            <button id="btn-submit-calc" class="btn-primary-action" ${this.stepFeedback && this.stepFeedback.isCorrect ? 'disabled' : ''}>
              ${this.stepFeedback && this.stepFeedback.isCorrect ? '✓ Verified! Moving to next step...' : 'Check Calculation ✓'}
            </button>
          </div>

          ${this.renderStepFeedbackBox()}
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // STAGE 5: NOTEBOOK SOLVE & SELF-AUDIT (BUILD/SOLVE)
  // ==========================================================================

  renderStage3Notebook(problem, mastery) {
    if (this.showProblemSolutionRecap) {
      return this.renderProblemCompletedRecap(problem, mastery);
    }

    const curType = this.getCurrentType();

    return `
      <div class="stage-panel stage-notebook-panel">
        <div class="panel-hero-bar">
          <div class="problem-meta-row">
            <div class="problem-meta-left">
              <span class="problem-tag">Problem ${this.currentProblemIndex + 1}</span>
              <span class="typology-sub-badge">${curType.type_title || ''}</span>
            </div>
            <div class="stage-milestone-pill">
              📝 ${mastery.stage3_verified || 0}/2 Clean Solves
            </div>
          </div>
          <h2 class="problem-statement-text">${problem.statement}</h2>
        </div>

        ${!this.notebookRubricRevealed ? `
          <div class="notebook-prompt-card">
            <div class="notebook-icon-header">📓 Paper & Pen Solve</div>
            <p class="notebook-instruction-text">
              1. Solve this problem completely in your mathematics notebook.<br>
              2. Show all step-by-step workings, division lines, or algebraic justifications.<br>
              3. When finished, click below to audit your work against the official board exam rubric.
            </p>
            <button id="btn-reveal-rubric" class="btn-reveal-rubric-action">
              🚀 I have solved this in my notebook → View Marking Scheme
            </button>
          </div>
        ` : `
          <div class="rubric-checklist-card">
            <div class="rubric-header">
              <h3>🔍 Step-by-Step Self-Audit Checklist</h3>
              <p>Compare each line in your notebook with the rubric below:</p>
            </div>

            <div class="rubric-items-list">
              ${problem.steps.map((st, sIdx) => {
                const auditVal = this.notebookAuditSelections[sIdx];
                return `
                  <div class="rubric-item ${auditVal === true ? 'marked-correct' : (auditVal === false ? 'marked-wrong' : '')}">
                    <div class="rubric-step-meta">
                      <span class="rubric-step-badge">Step ${st.step_number}: ${st.focus}</span>
                      <div class="rubric-text-rule">${st.rubric_text}</div>
                      ${st.rubric_math ? `<div class="rubric-math-box">\\[${st.rubric_math}\\]</div>` : ''}
                    </div>

                    <div class="rubric-toggle-buttons">
                      <button 
                        class="btn-rubric-toggle correct ${auditVal === true ? 'selected' : ''}" 
                        data-audit-step="${sIdx}" 
                        data-audit-val="true"
                      >
                        ✓ Correct in my notebook
                      </button>
                      <button 
                        class="btn-rubric-toggle wrong ${auditVal === false ? 'selected' : ''}" 
                        data-audit-step="${sIdx}" 
                        data-audit-val="false"
                      >
                        ✕ Made a mistake here
                      </button>
                    </div>

                    ${auditVal === false && st.revisit_topic ? `
                      <div class="revisit-remediation-box">
                        <div class="revisit-tip">💡 <strong>Review Tip:</strong> ${st.revisit_topic.tip}</div>
                        ${st.revisit_topic.url ? `
                          <a href="${st.revisit_topic.url}" class="btn-revisit-link" target="_blank">
                            📖 Review ${st.revisit_topic.title} Lesson ↗
                          </a>
                        ` : ''}
                      </div>
                    ` : ''}
                  </div>
                `;
              }).join('')}
            </div>

            <div class="rubric-submit-bar">
              <button 
                id="btn-submit-audit" 
                class="btn-primary-action" 
                ${Object.keys(this.notebookAuditSelections).length < problem.steps.length ? 'disabled' : ''}
              >
                Confirm Self-Audit & Complete Problem ✓
              </button>
            </div>
          </div>
        `}
      </div>
    `;
  }

  // ==========================================================================
  // PROBLEM COMPLETED RECAP (TEXTBOOK-STYLE FULL SOLUTION)
  // ==========================================================================

  renderProblemCompletedRecap(problem, mastery) {
    const isStage1 = this.currentStageId === 'stage_1_strategy';
    const isStage2 = this.currentStageId === 'stage_2_calc';
    const isStage3 = this.currentStageId === 'stage_3_notebook';

    let progressCount = 0;
    let targetCount = 2;
    let stageName = '';
    let nextStageTitle = '';
    let isStageTargetReached = false;

    if (isStage1) {
      progressCount = mastery.stage1_streak || 0;
      stageName = 'Stage 1: Strategy Choices';
      nextStageTitle = 'Advance to Stage 2 (Guided Calculation)';
      isStageTargetReached = progressCount >= 2;
    } else if (isStage2) {
      progressCount = mastery.stage2_streak || 0;
      stageName = 'Stage 2: Guided Calculation';
      nextStageTitle = 'Advance to Stage 3 (Notebook Solve)';
      isStageTargetReached = progressCount >= 2;
    } else if (isStage3) {
      progressCount = mastery.stage3_verified || 0;
      stageName = 'Stage 3: Notebook Solve';
      nextStageTitle = this.currentTypeIndex + 1 < this.questionTypes.length 
        ? `Study Type ${this.currentTypeIndex + 2} Model Solution` 
        : 'Topic Fully Mastered!';
      isStageTargetReached = mastery.is_mastered;
    }

    return `
      <div class="stage-panel stage-solution-recap-panel">
        <div class="problem-completed-hero-card">
          <div class="completed-hero-header">
            <span class="completed-badge-icon">🎉</span>
            <div class="completed-hero-text">
              <h2 class="completed-hero-title">Outstanding Work! Question Solved!</h2>
              <p class="completed-hero-sub">Here is your complete textbook-style stepwise solution:</p>
            </div>
          </div>
          <div class="completed-milestone-bar">
            <span class="milestone-stage-tag">${stageName}</span>
            <strong class="milestone-streak-count">${progressCount} / ${targetCount} Clean Solves</strong>
          </div>
        </div>

        <div class="textbook-solution-sheet">
          <div class="solution-header-row">
            <span class="solution-title-tag">📖 Stepwise Solution</span>
          </div>

          <div class="textbook-problem-summary">
            <strong>Problem:</strong> ${problem.statement}
          </div>

          <div class="textbook-stepwise-flow">
            ${problem.steps.map(st => `
              <div class="textbook-step-row">
                <div class="step-narrative-statement">
                  <strong>Step ${st.step_number}:</strong> ${this.toDisplayText(st.focus) || `Step ${st.step_number}`}
                </div>
                ${st.rubric_math ? `
                  <div class="step-math-block">
                    \\[${st.rubric_math}\\]
                  </div>
                ` : ''}
              </div>
            `).join('')}
          </div>

          <div class="textbook-conclusion-block">
            <strong>Final Answer:</strong> ${this.toDisplayText(problem.final_canonical_answer)}
          </div>
        </div>

        <div class="stage-footer-actions center-align">
          <button id="btn-advance-after-recap" class="btn-primary-action btn-large">
            ${isStageTargetReached ? `🏆 ${nextStageTitle} →` : `Next Question (Problem ${this.currentProblemIndex + 2}) →`}
          </button>
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // STAGE SUCCESS — COMPACT CONFIRMATION (never reveals worked solutions)
  // ==========================================================================

  showStageSuccess(title, message, actionLabel) {
    return `
      <div class="stage-panel stage-success-panel" role="status">
        <div class="stage-success-banner">
          <span class="stage-success-icon">✓</span>
          <div class="stage-success-text">
            <h2 class="stage-success-title">${title}</h2>
            <p class="stage-success-message">${message}</p>
          </div>
        </div>
        <div class="stage-success-actions">
          <button id="btn-advance-after-recap" class="btn-primary-action">${actionLabel}</button>
        </div>
      </div>
    `;
  }

  renderStageSuccessPanel(problem, mastery) {
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id] || {};
    const isStage1 = this.currentStageId === 'stage_1_strategy';

    const isStageTargetReached = isStage1
      ? (m.stage1_streak || 0) >= 2
      : (m.stage2_streak || 0) >= 2;

    const title = isStage1 ? '✓ Correct strategy' : '✓ Calculation Complete';
    const fallbackMessage = isStage1
      ? 'You identified the right mathematical move.'
      : 'Every calculation checked out correctly.';
    const message = (this.stepFeedback && this.stepFeedback.isCorrect && this.stepFeedback.message)
      ? this.stepFeedback.message
      : fallbackMessage;
    const actionLabel = isStageTargetReached
      ? (isStage1 ? 'Continue to Guided Calc →' : 'Continue to Notebook →')
      : 'Next Question →';

    return this.showStageSuccess(title, message, actionLabel);
  }

  renderStepFeedbackBox() {
    if (!this.stepFeedback) return '';

    const isCorrect = this.stepFeedback.isCorrect;
    return `
      <div class="step-feedback-banner ${isCorrect ? 'correct' : 'wrong'}">
        <div class="feedback-icon">${isCorrect ? '🎉' : '⚠️'}</div>
        <div class="feedback-text-content">
          <strong>${isCorrect ? (this.currentStageId === 'stage_1_strategy' ? '✓ Correct strategy' : '✓ Correct!') : 'Not quite.'}</strong>
          <p>${this.stepFeedback.message}</p>
        </div>
      </div>
    `;
  }

  renderMathKeypad() {
    const step = this.getCurrentStep();
    let keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', '-', '.', '⌫', 'Clear'];
    
    // If current step expects algebraic variables, prepend convenient letter keys
    const fields = step?.calc_template?.fields || [];
    const hasVariable = fields.some(f => typeof f.expected === 'string' && /^[a-zA-Z]$/.test(f.expected));
    if (hasVariable) {
      keys = ['a', 'b', 'x', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '/', '-', '.', '⌫', 'Clear'];
    }

    return `
      <div class="math-keypad-row">
        ${keys.map(k => `
          <button type="button" class="keypad-key-btn" data-key="${k}">${k}</button>
        `).join('')}
      </div>
    `;
  }

  renderReferenceDrawer() {
    const ref = this.topicData.reference_drawer || { title: '📖 Reference Guide', items: [] };
    return `
      <aside class="reference-drawer ${this.isReferenceDrawerOpen ? 'open' : ''}">
        <div class="drawer-header">
          <h3 class="drawer-title">${ref.title || '📖 Reference Guide'}</h3>
          <button id="btn-close-drawer" class="btn-drawer-close" title="Close Guide">✕</button>
        </div>
        <div class="drawer-body">
          ${ref.description ? `<p class="drawer-desc">${ref.description}</p>` : ''}
          <div class="reference-rules-list">
            ${(ref.items || []).map(it => `
              <div class="ref-rule-card">
                <span class="ref-rule-tag">${it.tag || it.name || 'Rule'}</span>
                <p class="ref-rule-text">${it.rule || ''}</p>
                ${it.formula ? `<div class="ref-rule-formula"><strong>Formula:</strong> \\(${it.formula}\\)</div>` : ''}
                ${it.example ? `<div class="ref-rule-example"><strong>Example:</strong> \\(${it.example}\\)</div>` : ''}
              </div>
            `).join('')}
          </div>
        </div>
      </aside>
      ${this.isReferenceDrawerOpen ? `<div id="drawer-backdrop" class="drawer-backdrop"></div>` : ''}
    `;
  }

  triggerMathJax() {
    if (typeof window === 'undefined') return;

    const doTypeset = () => {
      if (window.MathJax) {
        if (window.MathJax.typesetPromise) {
          window.MathJax.typesetPromise([this.container || document.body]).catch(() => {});
        } else if (window.MathJax.typeset) {
          try { window.MathJax.typeset([this.container || document.body]); } catch (e) {}
        }
      }
    };

    // Immediate attempt + requestAnimationFrame + timeout for async script readiness
    doTypeset();
    requestAnimationFrame(doTypeset);
    setTimeout(doTypeset, 150);
  }

  // ==========================================================================
  // EVENT HANDLERS
  // ==========================================================================

  attachEvents() {
    // Navigation: Stage Stepping
    this.container.querySelectorAll('.stage-step-pill, .stage-step-card').forEach(btn => {
      btn.addEventListener('click', () => {
        const stageId = btn.getAttribute('data-stage-id');
        if (stageId && stageId !== this.currentStageId && !btn.disabled) {
          this.audio.click();
          this.switchStage(stageId);
        }
      });
    });

    // Navigation: Typology switching
    this.container.querySelectorAll('.typology-pill-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const typeIdx = parseInt(btn.getAttribute('data-type-index'), 10);
        if (!isNaN(typeIdx) && typeIdx !== this.currentTypeIndex) {
          this.audio.click();
          this.switchTypology(typeIdx);
        }
      });
    });

    // Concepts -> Worked Examples CTAs
    const btnGotoEx = document.getElementById('btn-goto-examples');
    const btnGotoExBottom = document.getElementById('btn-goto-examples-bottom');
    [btnGotoEx, btnGotoExBottom].forEach(el => {
      if (el) {
        el.addEventListener('click', () => {
          this.audio.click();
          this.switchStage('worked_examples');
        });
      }
    });

    // Worked Examples navigation: handled by prev/next + practice buttons below

    const btnPrevEx = document.getElementById('btn-prev-example');
    if (btnPrevEx) {
      btnPrevEx.addEventListener('click', () => {
        this.audio.click();
        if (this.currentWorkedExampleIndex > 0) {
          this.currentWorkedExampleIndex--;
          this.render();
        }
      });
    }

    const btnNextEx = document.getElementById('btn-next-example');
    if (btnNextEx) {
      btnNextEx.addEventListener('click', () => {
        this.audio.click();
        if (this.currentWorkedExampleIndex < this.workedExamples.length - 1) {
          this.currentWorkedExampleIndex++;
          this.render();
        }
      });
    }

    const btnStartStrategy = document.getElementById('btn-start-strategy-practice');
    if (btnStartStrategy) {
      btnStartStrategy.addEventListener('click', () => {
        this.audio.success();
        const targetType = parseInt(btnStartStrategy.getAttribute('data-target-type'), 10);
        const validIndex = !isNaN(targetType) ? targetType : this.getHighestActiveTypeIndex();
        this.switchTypology(validIndex);
      });
    }

    // Navbar controls
    const btnTheme = document.getElementById('btn-toggle-theme');
    if (btnTheme) {
      btnTheme.addEventListener('click', () => {
        this.audio.click();
        this.toggleTheme();
      });
    }

    const btnSound = document.getElementById('btn-toggle-sound');
    if (btnSound) {
      btnSound.addEventListener('click', () => {
        this.audio.toggleMute();
        this.render();
      });
    }

    const btnDrawer = document.getElementById('btn-toggle-drawer');
    if (btnDrawer) {
      btnDrawer.addEventListener('click', () => {
        this.audio.click();
        this.isReferenceDrawerOpen = !this.isReferenceDrawerOpen;
        this.render();
      });
    }

    const btnCloseDrawer = document.getElementById('btn-close-drawer');
    const backdrop = document.getElementById('drawer-backdrop');
    [btnCloseDrawer, backdrop].forEach(el => {
      if (el) {
        el.addEventListener('click', () => {
          this.isReferenceDrawerOpen = false;
          this.render();
        });
      }
    });

    // Stage 1 Strategy Selection (Instant Tap Feedback & Auto-advance)
    this.container.querySelectorAll('.strategy-option-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const optIdx = parseInt(btn.getAttribute('data-option-index'), 10);
        this.handleInstantStrategySelection(optIdx);
      });
    });

    // Stage 2 Calculation Inputs & Keypad
    this.container.querySelectorAll('.calc-input-box').forEach(inp => {
      inp.addEventListener('focus', () => {
        this.activeFocusInputId = inp.id;
      });
      inp.addEventListener('input', (e) => {
        const fieldKey = inp.getAttribute('data-calc-field') || inp.id.replace('input-calc-', '');
        this.calcInputs[fieldKey] = e.target.value;
      });
      inp.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const btnSubmitCalc = document.getElementById('btn-submit-calc');
          if (btnSubmitCalc) btnSubmitCalc.click();
        }
      });
    });

    this.container.querySelectorAll('.keypad-key-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        this.audio.click();
        const key = btn.getAttribute('data-key');
        this.handleKeypadInput(key);
      });
    });

    const btnSubmitCalc = document.getElementById('btn-submit-calc');
    if (btnSubmitCalc) {
      btnSubmitCalc.addEventListener('click', () => this.handleCalculationSubmission());
    }

    // Next Step
    const btnNextStep = document.getElementById('btn-next-step');
    if (btnNextStep) {
      btnNextStep.addEventListener('click', () => this.handleNextStepOrProblem());
    }

    // Stage 3: Notebook Rubric
    const btnRevealRubric = document.getElementById('btn-reveal-rubric');
    if (btnRevealRubric) {
      btnRevealRubric.addEventListener('click', () => {
        this.audio.success();
        this.notebookRubricRevealed = true;
        this.render();
      });
    }

    this.container.querySelectorAll('.btn-rubric-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        this.audio.click();
        const stepIdx = parseInt(btn.getAttribute('data-audit-step'), 10);
        const val = btn.getAttribute('data-audit-val') === 'true';
        this.notebookAuditSelections[stepIdx] = val;
        this.render();
      });
    });

    const btnSubmitAudit = document.getElementById('btn-submit-audit');
    if (btnSubmitAudit) {
      btnSubmitAudit.addEventListener('click', () => this.handleNotebookAuditSubmission());
    }

    // Hint Toggle Button
    const btnToggleHint = document.getElementById('btn-toggle-hint');
    if (btnToggleHint) {
      btnToggleHint.addEventListener('click', () => {
        this.audio.click();
        this.showStepHint = !this.showStepHint;
        this.render();
      });
    }

    // Advance After Problem Completed Recap
    const btnAdvanceRecap = document.getElementById('btn-advance-after-recap');
    if (btnAdvanceRecap) {
      btnAdvanceRecap.addEventListener('click', () => {
        this.audio.success();
        this.advanceFromRecap();
      });
    }
  }

  // ==========================================================================
  // LOGICAL EVALUATION
  // ==========================================================================

  switchStage(stageId) {
    this.currentStageId = stageId;
    this.currentStepIndex = 0;
    this.resetStepState();
    this.saveMasteryState();
    this.render();
  }

  switchTypology(typeIdx) {
    const targetType = this.questionTypes[typeIdx];
    const m = targetType ? (this.masteryState[targetType.type_id] || {}) : {};
    const isUnlocked = typeIdx === 0 || m.is_unlocked;

    this.currentTypeIndex = isUnlocked ? typeIdx : this.getHighestActiveTypeIndex();
    this.currentStageId = 'stage_1_strategy';
    this.currentProblemIndex = 0;
    this.stageProblemIndices = {
      stage_1_strategy: 0,
      stage_2_calc: 1,
      stage_3_notebook: 2
    };
    this.currentStepIndex = 0;
    this.resetStepState();
    this.saveMasteryState();
    this.render();
  }

  resetStepState() {
    this.selectedStrategyIndex = null;
    this.calcInputs = {};
    this.stepFeedback = null;
    this.notebookRubricRevealed = false;
    this.notebookAuditSelections = {};
    this.showStageSuccessPanel = false;
    this.showProblemSolutionRecap = false;
    this.showStepHint = false;
  }

  handleKeypadInput(key) {
    const targetId = this.activeFocusInputId || 'input-calc-divisor' || 'input-calc-generic';
    const inputEl = document.getElementById(targetId) || document.querySelector('.calc-input-box');
    if (!inputEl) return;

    if (key === '⌫') {
      inputEl.value = inputEl.value.slice(0, -1);
    } else if (key === 'Clear') {
      inputEl.value = '';
    } else {
      inputEl.value += key;
    }

    inputEl.dispatchEvent(new Event('input'));
    inputEl.focus();
  }

  handleInstantStrategySelection(optIdx) {
    const step = this.getCurrentStep();
    if (!step) return;

    this.selectedStrategyIndex = optIdx;
    const isCorrect = optIdx === step.correct_strategy_index;
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id];
    const optDetail = step.option_details?.[optIdx];

    if (isCorrect) {
      this.audio.success();
      this.stepFeedback = {
        isCorrect: true,
        message: optDetail?.explanation || 'Correct strategy.'
      };
      this.render();

      setTimeout(() => {
        this.handleNextStepOrProblem();
      }, 700);
    } else {
      this.audio.error();
      m.stage1_streak = 0;
      this.saveMasteryState();
      this.stepFeedback = {
        isCorrect: false,
        message: optDetail?.explanation || step.revisit_topic?.tip || 'Not quite. Think about which mathematical move is needed here, then try again.'
      };
      this.render();
    }
  }

  handleCalculationSubmission() {
    const step = this.getCurrentStep();
    if (!step) return;

    let isCorrect = false;
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id];

    if (step.calc_template) {
      const fields = step.calc_template.fields || [];
      
      // Group fields by pair_group (if present)
      const groups = {};
      fields.forEach(f => {
        const gKey = f.pair_group || ('ungrouped_' + f.key);
        if (!groups[gKey]) groups[gKey] = [];
        groups[gKey].push(f);
      });

      const pairGroupEntries = Object.entries(groups).filter(([k, g]) => g.length === 2 && g[0].pair_group);

      if (pairGroupEntries.length > 1) {
        // Multi-pair table: User can enter pairs in ANY order among the rows!
        // Expected pairs list: [[d1, q1], [d2, q2], ...] (normalized with min, max)
        const expectedPairs = pairGroupEntries.map(([k, g]) => {
          const e1 = g[0].expected;
          const e2 = g[1].expected;
          return [Math.min(e1, e2), Math.max(e1, e2)];
        });

        // User pairs
        const userPairs = pairGroupEntries.map(([k, g]) => {
          const raw1 = parseInt(String(this.calcInputs[g[0].key] || '').trim(), 10);
          const raw2 = parseInt(String(this.calcInputs[g[1].key] || '').trim(), 10);
          return {
            groupKey: k,
            field1: g[0].key,
            field2: g[1].key,
            validNumbers: !isNaN(raw1) && !isNaN(raw2),
            normalized: [Math.min(raw1, raw2), Math.max(raw1, raw2)],
            product: raw1 * raw2
          };
        });

        // Match user pairs against expected pairs
        const unmatchedExpected = [...expectedPairs];
        const invalidGroups = [];

        userPairs.forEach(up => {
          if (!up.validNumbers) {
            invalidGroups.push(up);
            return;
          }
          const matchIdx = unmatchedExpected.findIndex(ep => ep[0] === up.normalized[0] && ep[1] === up.normalized[1]);
          if (matchIdx !== -1) {
            unmatchedExpected.splice(matchIdx, 1);
          } else {
            invalidGroups.push(up);
          }
        });

        isCorrect = unmatchedExpected.length === 0 && invalidGroups.length === 0;

        // Visually highlight error fields
        setTimeout(() => {
          pairGroupEntries.forEach(([k, g]) => {
            const el1 = document.getElementById(`input-calc-${g[0].key}`);
            const el2 = document.getElementById(`input-calc-${g[1].key}`);
            if (el1) el1.classList.remove('field-error', 'field-success');
            if (el2) el2.classList.remove('field-error', 'field-success');

            const isGroupInvalid = invalidGroups.some(ig => ig.groupKey === k);
            if (isGroupInvalid) {
              if (el1) el1.classList.add('field-error');
              if (el2) el2.classList.add('field-error');
            } else if (!isCorrect) {
              if (el1) el1.classList.add('field-success');
              if (el2) el2.classList.add('field-success');
            }
          });
        }, 50);

      } else {
        const parseNum = (val) => {
          const s = String(val || '').trim();
          if (!s) return NaN;
          if (s.includes('/')) {
            const parts = s.split('/');
            if (parts.length === 2) {
              const num = parseFloat(parts[0]);
              const den = parseFloat(parts[1]);
              if (!isNaN(num) && !isNaN(den) && den !== 0) return num / den;
            }
          }
          return parseFloat(s);
        };

        isCorrect = Object.values(groups).every(groupFields => {
          if (groupFields.length === 2 && groupFields[0].pair_group) {
            const raw1 = parseNum(this.calcInputs[groupFields[0].key]);
            const raw2 = parseNum(this.calcInputs[groupFields[1].key]);
            const exp1 = typeof groupFields[0].expected === 'number' ? groupFields[0].expected : parseNum(groupFields[0].expected);
            const exp2 = typeof groupFields[1].expected === 'number' ? groupFields[1].expected : parseNum(groupFields[1].expected);
            return (!isNaN(raw1) && !isNaN(raw2)) && (
              (Math.abs(raw1 - exp1) < 0.01 && Math.abs(raw2 - exp2) < 0.01) ||
              (Math.abs(raw1 - exp2) < 0.01 && Math.abs(raw2 - exp1) < 0.01)
            );
          } else {
            return groupFields.every(f => {
              const rawUser = String(this.calcInputs[f.key] || '').trim();
              if (rawUser === '') return false;
              if (typeof f.expected === 'string' && isNaN(parseNum(f.expected))) {
                return rawUser.toLowerCase() === f.expected.toLowerCase();
              }
              const uVal = parseNum(rawUser);
              const eVal = typeof f.expected === 'number' ? f.expected : parseNum(f.expected);
              if (!isNaN(eVal)) {
                return !isNaN(uVal) && Math.abs(uVal - eVal) < 0.01;
              }
              return rawUser.toLowerCase() === String(f.expected).toLowerCase();
            });
          }
        });
      }
    } else if (step.expected_divisor !== undefined && step.expected_divisor !== null) {
      const userDiv = parseInt(String(this.calcInputs.divisor || '').trim(), 10);
      const userQuo = parseInt(String(this.calcInputs.quotient || '').trim(), 10);
      isCorrect = userDiv === step.expected_divisor && userQuo === step.expected_quotient;
    } else {
      const normalize = (str) => String(str || '').replace(/\s+/g, '').replace(/x/g, '×').toLowerCase();
      const userVal = normalize(this.calcInputs.generic);
      const expVal = normalize(step.expected_value || step.expected_quotient);
      isCorrect = userVal === expVal || (expVal.length > 3 && userVal.includes(expVal));
    }

    if (isCorrect) {
      this.audio.success();
      this.stepFeedback = {
        isCorrect: true,
        message: 'Calculation verified.'
      };
      this.render();

      setTimeout(() => {
        this.handleNextStepOrProblem();
      }, 650);
    } else {
      this.audio.error();
      m.stage2_streak = 0;
      this.saveMasteryState();
      this.stepFeedback = {
        isCorrect: false,
        message: step.hint || step.revisit_topic?.tip || 'Calculation value does not match. Please verify your computation and retry.',
        tip: step.revisit_topic?.tip
      };
      this.render();
    }
  }

  handleNextStepOrProblem() {
    const problem = this.getCurrentProblem();
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id];

    if (this.currentStepIndex < problem.steps.length - 1) {
      this.currentStepIndex++;
      this.resetStepState();
      this.saveMasteryState();
      this.render();
    } else {
      this.audio.success();
      
      if (this.currentStageId === 'stage_1_strategy') {
        m.stage1_streak = (m.stage1_streak || 0) + 1;
        if (m.stage1_streak >= 2) {
          m.stage2_unlocked = true;
        }
      } else if (this.currentStageId === 'stage_2_calc') {
        m.stage2_streak = (m.stage2_streak || 0) + 1;
        if (m.stage2_streak >= 2) {
          m.stage3_unlocked = true;
        }
      }

      this.saveMasteryState();
      if (this.currentStageId === 'stage_3_notebook') {
        this.showProblemSolutionRecap = true;
      } else {
        this.showStageSuccessPanel = true;
      }
      this.render();
    }
  }

  handleNotebookAuditSubmission() {
    const problem = this.getCurrentProblem();
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id];

    const allCorrect = problem.steps.every((st, sIdx) => this.notebookAuditSelections[sIdx] === true);

    if (allCorrect) {
      this.audio.success();
      m.stage3_verified = (m.stage3_verified || 0) + 1;
      
      if (m.stage3_verified >= 2) {
        m.is_mastered = true;
        if (this.currentTypeIndex + 1 < this.questionTypes.length) {
          const nextType = this.questionTypes[this.currentTypeIndex + 1];
          if (this.masteryState[nextType.type_id]) {
            this.masteryState[nextType.type_id].is_unlocked = true;
          }
        }
      }
      this.saveMasteryState();
      this.showProblemSolutionRecap = true;
      this.render();
    } else {
      this.audio.error();
      this.saveMasteryState();
      this.render();
    }
  }

  advanceFromRecap() {
    const curType = this.getCurrentType();
    const m = this.masteryState[curType.type_id];
    const poolLen = (curType && curType.pool) ? curType.pool.length : 1;

    this.showProblemSolutionRecap = false;
    this.resetStepState();

    if (this.currentStageId === 'stage_1_strategy') {
      if (m.stage1_streak >= 2) {
        this.currentStageId = 'stage_2_calc';
        this.currentStepIndex = 0;
        this.saveMasteryState();
        this.render();
        return;
      }
    } else if (this.currentStageId === 'stage_2_calc') {
      if (m.stage2_streak >= 2) {
        this.currentStageId = 'stage_3_notebook';
        this.currentStepIndex = 0;
        this.saveMasteryState();
        this.render();
        return;
      }
    } else if (this.currentStageId === 'stage_3_notebook') {
      if (m.is_mastered) {
        if (this.currentTypeIndex + 1 < this.questionTypes.length) {
          const nextTypeIdx = this.currentTypeIndex + 1;
          const nextType = this.questionTypes[nextTypeIdx];
          if (this.masteryState[nextType.type_id]) {
            this.masteryState[nextType.type_id].is_unlocked = true;
          }
          this.currentTypeIndex = nextTypeIdx;
          this.currentWorkedExampleIndex = nextTypeIdx;
          this.currentStageId = 'worked_examples';
          this.currentProblemIndex = 0;
          this.currentStepIndex = 0;
          this.resetStepState();
          this.saveMasteryState();
          this.render();
          return;
        } else {
          alert('🏆 Congratulations! You have fully completed all question types in this chapter topic!');
          return;
        }
      }
    }

    if (this.stageProblemIndices && this.stageProblemIndices[this.currentStageId] !== undefined) {
      this.stageProblemIndices[this.currentStageId] = (this.stageProblemIndices[this.currentStageId] + 1) % poolLen;
    }
    this.currentProblemIndex = (this.currentProblemIndex + 1) % poolLen;
    this.currentStepIndex = 0;
    this.saveMasteryState();
    this.render();
  }

  renderLoading(msg = 'Loading...') {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="loading-state-wrapper">
        <div class="loading-spinner"></div>
        <p class="loading-text">${msg}</p>
      </div>
    `;
  }

  renderError(msg = 'An error occurred.') {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="error-state-card">
        <div class="error-icon">⚠️</div>
        <h2 class="error-title">Unable to Load Topic</h2>
        <p class="error-desc">${msg}</p>
        <button onclick="window.location.reload()" class="btn-primary-action">Reload Page</button>
      </div>
    `;
  }
}
