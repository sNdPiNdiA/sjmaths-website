/**
 * app.js
 * 
 * Reusable Universal Concept Mastery Application
 * Topic-agnostic presentation layer consuming any valid Learning-Topic JSON via LearningEngine.
 * Designed with Senior UI/UX Figma-Grade Polish & Interaction Architecture.
 */

import { createLearningEngine } from '../../engine/learning-engine.js';
import { getRequestedTopicId, loadTopicData } from '../../engine/topic-loader.js';

// Unified 8-Stage Cognitive Mastery Journey
const COGNITIVE_JOURNEY = Object.freeze([
  { id: 'understand', label: 'Understand', subtitle: 'Core Principle', icon: '1' },
  { id: 'see', label: 'See', subtitle: 'Worked Model', icon: '2' },
  { id: 'try', label: 'Try', subtitle: 'Guided Practice', icon: '3' },
  { id: 'think', label: 'Think', subtitle: 'Faded Guidance', icon: '4' },
  { id: 'build', label: 'Build', subtitle: 'Construct Solution', icon: '5' },
  { id: 'solve', label: 'Solve', subtitle: 'Independent', icon: '6' },
  { id: 'apply', label: 'Apply', subtitle: 'Transfer', icon: '7' },
  { id: 'master', label: 'Master', subtitle: 'Achievement', icon: '🏆' }
]);

const STAGE_TITLES = Object.freeze({
  understand: 'Understand',
  see: 'See',
  try: 'Try',
  think: 'Think',
  build: 'Build',
  solve: 'Solve',
  apply: 'Apply',
  master: 'Master',
  retain: 'Retain'
});

// Divisibility Rules Database for the reference drawer
const DIVISIBILITY_RULES = [
  { prime: '2', rule: 'Last digit is even (0, 2, 4, 6, 8)', example: '84 ends in 4 → divisible by 2' },
  { prime: '3', rule: 'Sum of all digits is a multiple of 3', example: '42 → 4 + 2 = 6 (multiple of 3) → divisible by 3' },
  { prime: '5', rule: 'Last digit is 0 or 5', example: '135 ends in 5 → divisible by 5' },
  { prime: '7', rule: 'Double the last digit, subtract from remaining number', example: '91 → 9 - (1 × 2) = 7 → divisible by 7' },
  { prime: '11', rule: 'Difference between alternating sum of digits is 0 or multiple of 11', example: '121 → (1+1) - 2 = 0 → divisible by 11' },
  { prime: '13', rule: 'Add 4 times the last digit to the rest', example: '91 → 9 + (1 × 4) = 13 → divisible by 13' }
];

// Lightweight synthesized Web Audio sound feedback
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

  playTone(freq, type = 'sine', duration = 0.15, gain = 0.1) {
    if (this.isMuted) return;
    try {
      this.initContext();
      if (!this.ctx) return;
      if (this.ctx.state === 'suspended') this.ctx.resume();

      const osc = this.ctx.createOscillator();
      const gainNode = this.ctx.createGain();

      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);

      gainNode.gain.setValueAtTime(gain, this.ctx.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);

      osc.connect(gainNode);
      gainNode.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    } catch (e) {
      // Audio autoplay policy fallback
    }
  }

  click() {
    this.playTone(600, 'sine', 0.05, 0.04);
  }

  success() {
    if (this.isMuted) return;
    try {
      this.initContext();
      if (!this.ctx) return;
      if (this.ctx.state === 'suspended') this.ctx.resume();

      const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6 arpeggio
      notes.forEach((freq, idx) => {
        setTimeout(() => {
          this.playTone(freq, 'triangle', 0.2, 0.08);
        }, idx * 60);
      });
    } catch (e) {}
  }

  error() {
    this.playTone(220, 'sawtooth', 0.2, 0.06);
  }

  hint() {
    this.playTone(880, 'sine', 0.18, 0.06);
  }
}

export class ConceptMasteryApp {
  constructor({ containerId = 'app-root', container = null } = {}) {
    this.container = container || (typeof document !== 'undefined' ? document.getElementById(containerId) : null);
    this.topicData = null;
    this.engine = null;
    this.currentQuestion = null;
    this.selectedChoice = null;
    this.currentExampleIndex = 0;
    this.currentStepIndex = 0;
    this.completedStepsHistory = [];
    this.isQuestionCompleted = false;
    this.audio = new AudioEffects();
    this.isReferenceDrawerOpen = false;
  }

  getStorageKey(topicId) {
    return `sjmaths_mastery_state_${topicId}`;
  }

  loadPersistedState(topicId) {
    if (typeof window === 'undefined' || !window.localStorage) return null;
    try {
      const raw = window.localStorage.getItem(this.getStorageKey(topicId));
      if (!raw) return null;
      const parsed = JSON.parse(raw);
      if (parsed && typeof parsed === 'object') {
        if (typeof parsed.currentExampleIndex === 'number') {
          this.currentExampleIndex = parsed.currentExampleIndex;
        }
        if (typeof parsed.currentStepIndex === 'number') {
          this.currentStepIndex = parsed.currentStepIndex;
        }
        if (Array.isArray(parsed.completedStepsHistory)) {
          this.completedStepsHistory = parsed.completedStepsHistory;
        }
        return parsed.engineState || null;
      }
    } catch (e) {
      console.debug('Failed to load persisted mastery state:', e);
    }
    return null;
  }

  persistState() {
    if (typeof window === 'undefined' || !window.localStorage || !this.engine || !this.topicData) return;
    try {
      const topicId = this.topicData.topic?.id || getRequestedTopicId() || 'cbse10-real-numbers-fta';
      const engineState = this.engine.exportRawState ? this.engine.exportRawState() : null;
      const payload = {
        topicId,
        currentExampleIndex: this.currentExampleIndex || 0,
        currentStepIndex: this.currentStepIndex || 0,
        completedStepsHistory: this.completedStepsHistory || [],
        engineState,
        updatedAt: Date.now()
      };
      window.localStorage.setItem(this.getStorageKey(topicId), JSON.stringify(payload));
    } catch (e) {
      console.debug('Failed to persist mastery state:', e);
    }
  }

  initTheme() {
    if (typeof window !== 'undefined') {
      const savedTheme = localStorage.getItem('sjmaths_theme') || 'paper';
      document.documentElement.setAttribute('data-theme', savedTheme);
    }
  }

  toggleTheme() {
    if (typeof window === 'undefined') return;
    const current = document.documentElement.getAttribute('data-theme') || 'paper';
    const next = current === 'paper' ? 'charcoal' : 'paper';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('sjmaths_theme', next);
    return next;
  }

  async init() {
    try {
      this.initTheme();
      this.renderLoading();

      const topicId = getRequestedTopicId() || 'cbse10-real-numbers-fta';
      this.topicData = await loadTopicData(topicId);

      const savedEngineState = this.loadPersistedState(topicId);

      this.engine = createLearningEngine({
        topicData: this.topicData,
        studentState: savedEngineState,
        onStateChange: () => {
          this.persistState();
          this.render();
        }
      });

      this.render();
    } catch (err) {
      console.error('ConceptMasteryApp init error:', err);
      this.renderError(err.message || 'Unable to load this learning topic.');
    }
  }

  typeset() {
    if (typeof window !== 'undefined' && window.MathJax) {
      if (window.MathJax.typesetPromise) {
        window.MathJax.typesetPromise().catch(err => console.debug('MathJax typeset:', err));
      } else if (window.MathJax.startup && window.MathJax.startup.promise) {
        window.MathJax.startup.promise.then(() => window.MathJax.typesetPromise());
      }
    }
  }

  toggleReferenceDrawer(open) {
    this.isReferenceDrawerOpen = open !== undefined ? open : !this.isReferenceDrawerOpen;
    const backdrop = document.getElementById('reference-drawer-backdrop');
    if (backdrop) {
      if (this.isReferenceDrawerOpen) {
        backdrop.classList.add('open');
      } else {
        backdrop.classList.remove('open');
      }
    }
  }

  // ==========================================================================
  // Layout Shell & Modern Navigation Header
  // ==========================================================================
  renderTopicHeader() {
    const topic = this.topicData?.topic || {};
    const gradeStr = topic.class ? `Class ${topic.class}` : (topic.grade || 'Class 10');
    const chapterStr = topic.chapter || 'Real Numbers';
    const isMuted = this.audio.isMuted;

    return `
      <header class="top-nav">
        <div class="brand-section">
          <a href="/" class="brand-badge">
            <div class="brand-logo-gem">SJ</div>
            <div class="brand-titles">
              <span class="brand-name">SJMATHS</span>
              <div class="breadcrumbs">
                <span>${gradeStr} • ${topic.subject || 'Mathematics'}</span>
                <span class="sep">•</span>
                <span class="active">${topic.short_title || chapterStr}</span>
              </div>
            </div>
          </a>
        </div>

        <div class="nav-actions">
          <button class="nav-tool-btn" id="btn-header-back" title="Go Back">
            <span>←</span>
            <span class="btn-label-text">Back</span>
          </button>
          <button class="nav-tool-btn" id="btn-toggle-cheat" title="Divisibility Guide">
            <span>📖</span>
            <span class="btn-label-text">Rules</span>
          </button>
          <button class="nav-tool-btn" id="btn-toggle-theme" title="Toggle Theme (Paper / Charcoal)">
            <span>🌓</span>
          </button>
          <button class="nav-tool-btn" id="btn-toggle-audio" title="${isMuted ? 'Unmute Sound' : 'Mute Sound'}">
            <span>${isMuted ? '🔇' : '🔊'}</span>
          </button>
          <button class="nav-tool-btn" id="btn-reset-session" title="Restart / Reset Practice Session">
            <span>↺</span>
            <span class="btn-label-text">Reset</span>
          </button>
        </div>
      </header>
    `;
  }

  renderCognitiveStepper(currentStudentStage) {
    const topic = this.topicData?.topic || {};
    const stagesOrder = ['understand', 'see', 'try', 'think', 'build', 'solve', 'apply', 'master'];
    let activeIndex = stagesOrder.indexOf(currentStudentStage);
    if (activeIndex === -1) {
      activeIndex = currentStudentStage === 'retain' ? 7 : 0;
    }

    const progressPercent = Math.round(((activeIndex + 1) / stagesOrder.length) * 100);

    const stepsHtml = COGNITIVE_JOURNEY.map((step, idx) => {
      const isCompleted = idx < activeIndex;
      const isActive = idx === activeIndex;
      const stateClass = isActive ? 'active' : (isCompleted ? 'completed' : '');
      const indicatorContent = isCompleted ? '✓' : step.icon;

      return `
        <div class="journey-node ${stateClass} ${isCompleted ? 'nav-clickable' : ''}" data-stage="${step.id}" title="${step.label}: ${step.subtitle}">
          <div class="node-indicator">${indicatorContent}</div>
          <span>${step.label}</span>
        </div>
      `;
    }).join('');

    return `
      <section class="stepper-card">
        <div class="stepper-header">
          <div class="topic-meta-chip">
            <span class="pulse-dot"></span>
            <span>${topic.title || 'Fundamental Theorem of Arithmetic'}</span>
          </div>
          <div class="stage-counter-pill">
            Step ${activeIndex + 1} of ${stagesOrder.length} • ${progressPercent}%
          </div>
        </div>

        <div class="journey-stepper-track">
          ${stepsHtml}
        </div>

        <div class="micro-progress-container">
          <div class="micro-progress-fill" style="width: ${progressPercent}%;"></div>
        </div>
      </section>
    `;
  }

  // Divisibility Rules Reference Modal Drawer
  renderReferenceDrawer() {
    return `
      <div class="drawer-backdrop" id="reference-drawer-backdrop">
        <div class="drawer-panel">
          <div class="drawer-drag-handle"></div>
          <div class="drawer-header">
            <div class="drawer-title">📖 Prime Divisibility Guide</div>
            <button class="drawer-close-btn" id="btn-close-drawer" aria-label="Close Reference Guide">✕</button>
          </div>

          <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.45;">
            Use these quick divisibility rules to quickly identify prime factors without tedious trial division.
          </p>

          <div style="display: flex; flex-direction: column; gap: 0.65rem;">
            ${DIVISIBILITY_RULES.map(r => `
              <div class="rule-card">
                <div class="rule-prime-tag">Prime ${r.prime}</div>
                <div class="rule-explanation"><strong>Rule:</strong> ${r.rule}</div>
                <div class="rule-explanation" style="color: var(--brand-primary); font-family: var(--font-mono); font-size: 0.82rem;"><strong>Eg:</strong> ${r.example}</div>
              </div>
            `).join('')}
          </div>
        </div>
      </div>
    `;
  }

  // ==========================================================================
  // Master Render Loop
  // ==========================================================================
  render() {
    if (!this.container || !this.engine || !this.topicData) return;

    const state = this.engine.getLearningState();
    const studentStage = state.student_stage || 'understand';

    // Reset question-level state if transitioning to a new stage
    if (this.activeStage !== studentStage) {
      this.activeStage = studentStage;
      this.currentQuestion = null;
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
      this.selectedChoice = null;
      this.clearFeedback();
    }

    let contentHtml = '';
    const isFTA = this.topicData.topic?.id === 'cbse10-real-numbers-fta';
    const isProof = this.topicData.topic?.id === 'cbse10-real-numbers-irrationality';

    const stageKeyMap = {
      'understand': 'concept_learning',
      'see': 'worked_examples',
      'try': 'guided_practice',
      'think': 'faded_guidance',
      'build': 'constructed_solution',
      'solve': 'independent_solution',
      'apply': 'transfer_mastery',
      'master': 'mastery_gate'
    };
    const unitKey = stageKeyMap[studentStage];
    const unitDef = this.topicData.units ? this.topicData.units[unitKey] : null;

    let defaultHeading = 'Concept Mastery';
    if (unitDef && unitDef.title) {
      defaultHeading = unitDef.title.replace(/^(Try|Think|Build|Solve|Apply|See|Understand)\s*—\s*/i, '');
    }

    let eyebrow = `Phase • ${STAGE_TITLES[studentStage] || studentStage}`;
    let heading = (unitDef && unitDef.title) ? defaultHeading : (this.topicData.topic?.title || 'Concept Mastery');

    switch (studentStage) {
      case 'understand':
        eyebrow = 'Step 1 • Conceptual Overview';
        heading = (unitDef && unitDef.title) ? defaultHeading : 'The Big Idea';
        contentHtml = this.renderUnderstand();
        break;
      case 'see':
        eyebrow = 'Step 2 • Visual & Worked Models';
        heading = (unitDef && unitDef.title) ? defaultHeading : (isProof ? 'Worked Proof Models' : 'Worked Examples & Step Breakdown');
        contentHtml = this.renderSee();
        break;
      case 'try':
        eyebrow = 'Step 3 • Guided Practice';
        heading = (unitDef && unitDef.title) ? defaultHeading : (isProof ? 'Step-by-Step Proof Construction' : 'Step-by-Step Guided Practice');
        contentHtml = this.renderTry();
        break;
      case 'think':
        eyebrow = 'Step 4 • Faded Guidance';
        heading = (unitDef && unitDef.title) ? defaultHeading : (isProof ? 'Complete Key Deductions' : 'Deduce Missing Steps');
        contentHtml = this.renderThink();
        break;
      case 'build':
        eyebrow = 'Step 5 • Solution Construction';
        heading = (unitDef && unitDef.title) ? defaultHeading : (isProof ? 'Construct Complete Proof' : 'Construct Complete Solution');
        contentHtml = this.renderBuild();
        break;
      case 'solve':
        eyebrow = 'Step 6 • Independent Practice';
        heading = (unitDef && unitDef.title) ? defaultHeading : 'Solve Without Scaffolding';
        contentHtml = this.renderSolve();
        break;
      case 'apply':
        eyebrow = 'Step 7 • Transfer & Reasoning';
        heading = (unitDef && unitDef.title) ? defaultHeading : 'Transfer & Real-World Reasoning';
        contentHtml = this.renderApply();
        break;
      case 'master':
        eyebrow = 'Achievement';
        heading = 'Concept Mastered';
        contentHtml = this.renderMaster();
        break;
      case 'retain':
        eyebrow = 'Retention Check';
        heading = 'Quick Recall Session';
        contentHtml = this.renderRetain();
        break;
      default:
        contentHtml = this.renderUnderstand();
    }

    this.container.innerHTML = `
      <div class="app-shell">
        ${this.renderTopicHeader()}
        ${this.renderCognitiveStepper(studentStage)}

        <main class="workspace-card">
          <div class="stage-canvas">
            <div class="stage-title-row">
              <div>
                <div class="stage-eyebrow">${eyebrow}</div>
                <h1 class="stage-heading">${heading}</h1>
              </div>
            </div>

            <div id="stage-body">${contentHtml.body || ''}</div>
            <div id="remediation-container"></div>
            <div id="feedback-container"></div>
            <div id="hint-container"></div>
            <div class="action-bar-modern" id="action-bar">${contentHtml.actions || ''}</div>
          </div>
        </main>

        ${typeof window !== 'undefined' && new URLSearchParams(window.location.search).get('debug') === 'true' ? `
          <details class="inspector-modern">
            <summary>🔍 Debug State Inspector</summary>
            <div class="inspector-content-modern">
              <div><strong>Topic:</strong> ${this.topicData.topic?.id || 'unknown'}</div>
              <div><strong>Internal Stage:</strong> ${state.current_stage}</div>
              <div><strong>Student Stage:</strong> ${studentStage}</div>
              <div><strong>Accuracy:</strong> ${Math.round((state.overall_accuracy || 1) * 100)}%</div>
              <div><strong>Active Question:</strong> ${this.currentQuestion?.id || 'none'}</div>
            </div>
          </details>
        ` : ''}

        ${this.renderReferenceDrawer()}
      </div>
    `;

    // Bind Global Header & Drawer Events
    this.bindGlobalEvents();

    if (typeof document !== 'undefined' && contentHtml.attachEvents) {
      contentHtml.attachEvents();
    }

    this.persistState();
    this.typeset();
  }

  bindGlobalEvents() {
    if (typeof document === 'undefined') return;
    const btnCheat = document.getElementById('btn-toggle-cheat');
    if (btnCheat) {
      btnCheat.onclick = () => {
        this.audio.click();
        this.toggleReferenceDrawer(true);
      };
    }

    const btnClose = document.getElementById('btn-close-drawer');
    if (btnClose) {
      btnClose.onclick = () => {
        this.audio.click();
        this.toggleReferenceDrawer(false);
      };
    }

    const backdrop = document.getElementById('reference-drawer-backdrop');
    if (backdrop) {
      backdrop.onclick = (e) => {
        if (e.target === backdrop) {
          this.toggleReferenceDrawer(false);
        }
      };
    }

    const btnTheme = document.getElementById('btn-toggle-theme');
    if (btnTheme) {
      btnTheme.onclick = () => {
        this.audio.click();
        this.toggleTheme();
      };
    }

    const btnAudio = document.getElementById('btn-toggle-audio');
    if (btnAudio) {
      btnAudio.onclick = () => {
        const isMuted = this.audio.toggleMute();
        btnAudio.title = isMuted ? 'Unmute Sound Effects' : 'Mute Sound Effects';
        btnAudio.innerHTML = `<span>${isMuted ? '🔇' : '🔊'}</span>`;
        if (!isMuted) this.audio.click();
      };
    }

    const btnBack = document.getElementById('btn-header-back');
    if (btnBack) {
      btnBack.onclick = () => {
        this.audio?.click();
        const state = this.engine ? this.engine.getLearningState() : {};
        const studentStage = state.student_stage || 'understand';
        const stagesOrder = ['understand', 'see', 'try', 'think', 'build', 'solve', 'apply', 'master'];
        const currentIdx = stagesOrder.indexOf(studentStage);
        if (currentIdx > 0) {
          this.goToStage(stagesOrder[currentIdx - 1]);
        } else if (typeof window !== 'undefined' && window.history.length > 1) {
          window.history.back();
        } else if (typeof window !== 'undefined') {
          window.location.href = '/';
        }
      };
    }

    const stageNodes = document.querySelectorAll('.journey-node[data-stage]');
    stageNodes.forEach(node => {
      node.onclick = () => {
        const targetStage = node.dataset.stage;
        const state = this.engine ? this.engine.getLearningState() : {};
        const studentStage = state.student_stage || 'understand';
        const stagesOrder = ['understand', 'see', 'try', 'think', 'build', 'solve', 'apply', 'master'];
        const currentIdx = stagesOrder.indexOf(studentStage);
        const targetIdx = stagesOrder.indexOf(targetStage);
        if (targetIdx !== -1 && targetIdx <= currentIdx) {
          this.goToStage(targetStage);
        }
      };
    });

    const btnResetSession = document.getElementById('btn-reset-session');
    if (btnResetSession) {
      btnResetSession.onclick = () => {
        if (confirm('Restart practice session from the beginning?')) {
          this.resetSession();
        }
      };
    }
  }

  goToStage(targetStudentStage) {
    const stageMap = {
      'understand': 'concept_learning',
      'see': 'worked_examples',
      'try': 'guided_practice',
      'think': 'faded_guidance',
      'build': 'constructed_solution',
      'solve': 'independent_solution',
      'apply': 'transfer_mastery',
      'master': 'mastery_gate',
      'retain': 'delayed_retrieval'
    };
    const internalStage = stageMap[targetStudentStage];
    if (internalStage && this.engine && typeof this.engine.setStage === 'function') {
      this.audio?.click();
      this.engine.setStage(internalStage);
      this.activeStage = null;
      this.currentQuestion = null;
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
      this.selectedChoice = null;
      this.currentHintLevel = 0;
      this.clearFeedback();
      this.render();
    }
  }

  resetSession() {
    this.audio?.click();
    try {
      localStorage.removeItem('sjmaths_concept_mastery_state');
      localStorage.removeItem(`sjmaths_state_${this.topicData?.topic?.id || 'fta'}`);
    } catch (e) {
      // ignore
    }

    if (this.engine && typeof this.engine.resetLearnerState === 'function') {
      this.engine.resetLearnerState();
    } else {
      this.engine = createLearningEngine({ topicData: this.topicData });
    }

    this.activeStage = null;
    this.currentQuestion = null;
    this.currentStepIndex = 0;
    this.completedStepsHistory = [];
    this.isQuestionCompleted = false;
    this.lastSubmittedAnswer = null;
    this.selectedChoice = null;
    this.currentHintLevel = 0;
    this.clearFeedback();
    this.render();
  }

  renderConceptCardContent(item) {
    if (!item) return '';
    if (typeof item === 'string') {
      return `<p class="concept-card-text">${this.formatMathExpression(item)}</p>`;
    }

    let html = '';
    if (item.summary) {
      html += `<div class="concept-card-summary">${this.formatMathExpression(item.summary)}</div>`;
    }

    if (Array.isArray(item.points) && item.points.length > 0) {
      html += `
        <div class="concept-point-list">
          ${item.points.map(pt => `
            <div class="concept-point-item">
              <span class="concept-point-icon">${pt.icon || '•'}</span>
              <div>${this.formatMathExpression(pt.text || pt)}</div>
            </div>
          `).join('')}
        </div>
      `;
    } else if (Array.isArray(item.steps) && item.steps.length > 0) {
      html += `
        <div class="concept-point-list">
          ${item.steps.map((st, sIdx) => `
            <div class="concept-point-item">
              <span class="concept-point-icon">${sIdx + 1}</span>
              <div>${this.formatMathExpression(st.text || st)}</div>
            </div>
          `).join('')}
        </div>
      `;
    } else if (item.text) {
      const rawText = item.text;
      const numberedMatches = rawText.match(/\d+\.\s+[^0-9]+/g);
      if (numberedMatches && numberedMatches.length >= 2) {
        html += `
          <div class="concept-point-list">
            ${numberedMatches.map((chunk, cIdx) => {
              const cleanChunk = chunk.replace(/^\d+\.\s*/, '').trim();
              return `
                <div class="concept-point-item">
                  <span class="concept-point-icon">${cIdx + 1}</span>
                  <div>${this.formatMathExpression(cleanChunk)}</div>
                </div>
              `;
            }).join('')}
          </div>
        `;
      } else {
        const sentences = rawText.split(/(?<=\.\s+)(?=[A-Z])/).filter(Boolean);
        if (sentences.length > 1) {
          html += `
            <div class="concept-point-list">
              ${sentences.map(st => `
                <div class="concept-point-item">
                  <span class="concept-point-icon">•</span>
                  <div>${this.formatMathExpression(st.trim())}</div>
                </div>
              `).join('')}
            </div>
          `;
        } else {
          html += `<p class="concept-card-text">${this.formatMathExpression(rawText)}</p>`;
        }
      }
    }

    if (item.formula || item.equation) {
      html += `
        <div class="concept-formula-box">
          <span>📐</span>
          <span>${this.formatMathExpression(item.formula || item.equation)}</span>
        </div>
      `;
    }

    if (item.trap || item.warning) {
      html += `
        <div class="concept-trap-callout">
          <span>⚠️ ${this.formatMathExpression(item.trap || item.warning)}</span>
        </div>
      `;
    }

    return html;
  }

  // ==========================================================================
  // 1. Understand (Concept Learning Overview)
  // ==========================================================================
  renderUnderstand() {
    const unit = this.topicData.units?.concept_learning || {};
    const seq = Array.isArray(unit.learning_sequence) ? unit.learning_sequence : [];
    const instructions = Array.isArray(unit.instruction) ? unit.instruction : (unit.instruction ? [unit.instruction] : []);
    const mnemonics = Array.isArray(unit.mnemonics) ? unit.mnemonics : [];

    const bigIdea = this.topicData.topic?.description || seq[0]?.summary || seq[0]?.text || instructions[0] || 'Understand the core principles and methods.';
    const detailConcepts = seq.length > 0 ? seq : (instructions.length > 0 ? instructions.map((t, idx) => ({ title: `Key Rule ${idx + 1}`, text: t })) : []);
    
    const keyPoints = Array.isArray(this.topicData.learning_objectives) && this.topicData.learning_objectives.length > 0
      ? this.topicData.learning_objectives.slice(0, 4)
      : [
          'Decompose composite numbers systematically using prime factors.',
          'Verify divisibility using mental arithmetic rules.',
          'Express solutions in standard expanded and exponential forms.'
        ];

    const body = `
      <div class="concept-hero-card">
        <div class="concept-hero-tag">
          <span>✨</span>
          <span>The Big Idea</span>
        </div>
        <p class="concept-hero-text">${this.formatMathExpression(bigIdea)}</p>
      </div>

      ${detailConcepts.length > 0 ? `
        <div class="concept-objectives-heading">Core Concept Principles:</div>
        <div class="concept-sequence-grid">
          ${detailConcepts.map((item, idx) => `
            <div class="concept-sequence-card">
              <div class="concept-card-header">
                <span class="concept-card-num">0${idx + 1}</span>
                <strong class="concept-card-title">${item.title || `Principle ${idx + 1}`}</strong>
              </div>
              ${this.renderConceptCardContent(item)}
            </div>
          `).join('')}
        </div>
      ` : ''}

      ${mnemonics.length > 0 ? `
        <div class="mnemonics-card">
          <div class="mnemonics-title">
            <span>💡</span>
            <span>Key Rules to Remember</span>
          </div>
          <div class="mnemonics-list">
            ${mnemonics.map(m => `
              <div class="mnemonic-pill">${m.text || m}</div>
            `).join('')}
          </div>
        </div>
      ` : ''}

      <div class="concept-objectives-heading">Target Competencies for this Session:</div>
      <div class="objectives-grid">
        ${keyPoints.map((pt, idx) => `
          <div class="objective-item-pill">
            <div class="obj-icon">0${idx + 1}</div>
            <div>${pt}</div>
          </div>
        `).join('')}
      </div>
    `;

    const actions = `
      <button class="btn-modern btn-modern-primary" id="btn-continue-see">
        <span>Continue to Worked Examples</span>
        <span>→</span>
      </button>
    `;

    const attachEvents = () => {
      const btn = document.getElementById('btn-continue-see');
      if (btn) {
        btn.onclick = () => {
          this.audio.click();
          this.engine.submitInteraction({ question_id: 'c_01', is_correct: true, stage: 'concept_learning' });
          this.render();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // 2. See (Worked Examples with Step-by-Step Ladder Progression)
  // ==========================================================================
  renderWorkedExampleStep(step, index) {
    if (!step) return '';
    if (typeof step === 'string') {
      return `
        <div class="step-card-modern">
          <div class="step-card-modern-header">
            <span class="step-num-badge">Step ${index + 1}</span>
          </div>
          <div class="step-explanation-block">
            <div>${step}</div>
          </div>
        </div>
      `;
    }

    const headingVal = step.focus || (step.number !== undefined ? step.number : (step.expression || step.prompt || ''));
    const divisorVal = step.divisor !== undefined ? step.divisor : (step.action || step.operation || '');
    const reasonVal = step.reason || step.explanation || step.why || '';
    const calcVal = step.calculation || step.result || step.math || '';
    const actionLabel = step.divisor !== undefined ? 'Choose prime' : (step.action ? 'Action' : 'Operation');

    return `
      <div class="step-card-modern">
        <div class="step-card-modern-header">
          <span class="step-num-badge">Step ${index + 1}</span>
          ${headingVal !== '' ? `<span class="step-target-value">${headingVal}</span>` : ''}
        </div>
        
        <div class="step-explanation-block">
          ${divisorVal !== '' ? `
            <div class="step-action-tag">
              <span>${actionLabel}:</span>
              <strong class="highlight">${divisorVal}</strong>
            </div>
          ` : ''}
          ${reasonVal ? `
            <div class="step-why-quote">
              <strong>Why?</strong> ${reasonVal}
            </div>
          ` : ''}
          ${calcVal ? `
            <div class="step-calc-badge">${calcVal}</div>
          ` : ''}
        </div>
      </div>
    `;
  }

  renderSee() {
    const unit = this.topicData.units?.worked_examples || {};
    const examples = Array.isArray(unit.examples) ? unit.examples : [];
    const displayPolicy = unit.display_policy || {};

    if (examples.length === 0) {
      return {
        body: '<p style="color: var(--text-secondary);">Observe how each step is executed systematically.</p>',
        actions: '<button class="btn-modern btn-modern-primary" id="btn-ready-try">I\'m Ready to Try →</button>',
        attachEvents: () => {
          const btn = document.getElementById('btn-ready-try');
          if (btn) btn.onclick = () => {
            this.audio.click();
            this.engine.submitInteraction({ question_id: 'w_01', is_correct: true, stage: 'worked_examples' });
            this.render();
          };
        }
      };
    }

    const currentIdx = Math.max(0, Math.min(this.currentExampleIndex || 0, examples.length - 1));
    const ex = examples[currentIdx];
    const exKey = `example_${currentIdx + 1}`;
    const policy = displayPolicy[exKey] || (currentIdx === 0 ? 'fully_revealed' : (currentIdx === 1 ? 'progressive_reveal' : 'interactive_observation'));
    const problemText = ex.question || ex.problem || ex.prompt || `Worked Example ${currentIdx + 1}`;

    // Compute progression track nodes (e.g. 84 → 42 → 21 → 7 → 1)
    const steps = Array.isArray(ex.steps) ? ex.steps : [];
    let trackHtml = '';
    if (steps.length > 0 && steps[0].number !== undefined) {
      const numbersChain = steps.map(s => s.number);
      const lastStep = steps[steps.length - 1];
      if (lastStep.divisor !== undefined && lastStep.number !== undefined) {
        const nextQuot = lastStep.number / lastStep.divisor;
        numbersChain.push(nextQuot === 1 ? 1 : Math.floor(nextQuot));
      }
      trackHtml = `
        <div class="progression-nodes-bar">
          <span style="font-size: 0.76rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; margin-right: 0.35rem;">Chain:</span>
          ${numbersChain.map((num, nIdx) => `
            <span class="progression-node-pill">${num}</span>
            ${nIdx < numbersChain.length - 1 ? '<span class="progression-arrow-sep">→</span>' : ''}
          `).join('')}
        </div>
      `;
    }

    // Answers summary block
    const answersList = [];
    if (ex.expanded_answer) answersList.push({ label: 'Expanded Form', val: ex.expanded_answer });
    if (ex.exponential_answer) answersList.push({ label: 'Exponential Form', val: ex.exponential_answer });
    if (ex.final_answer) answersList.push({ label: 'Result', val: ex.final_answer });
    if (ex.answer && !ex.expanded_answer && !ex.exponential_answer) answersList.push({ label: 'Answer', val: ex.answer });

    const answersHtml = answersList.length > 0 ? `
      <div class="factor-complete-summary-card" id="example-answers-${currentIdx}">
        <div class="complete-title-line">
          <span>✓</span>
          <span>Final Factorisation</span>
        </div>
        ${answersList.map(a => `
          <div class="summary-answer-row">
            <strong>${a.label}:</strong>
            <span class="summary-answer-highlight">${a.val}</span>
          </div>
        `).join('')}
      </div>
    ` : '';

    let stepsContainerHtml = '';

    if (policy === 'progressive_reveal' && steps.length > 1) {
      stepsContainerHtml = `
        <div style="display: flex; flex-direction: column; gap: 0.85rem;" id="reveal-box-${currentIdx}">
          <div id="revealed-steps-${currentIdx}" style="display: flex; flex-direction: column; gap: 0.85rem;">
            ${this.renderWorkedExampleStep(steps[0], 0)}
          </div>
          <button class="btn-modern btn-modern-secondary btn-reveal-next" data-ex-idx="${currentIdx}" data-total="${steps.length}" data-current="1" style="align-self: flex-start;">
            <span>Reveal Next Step (${steps.length - 1} remaining)</span>
            <span>↓</span>
          </button>
          <div id="progressive-answer-${currentIdx}" style="display: none;">
            ${answersHtml}
          </div>
        </div>
      `;
    } else if (Array.isArray(ex.options) && ex.options.length > 0) {
      stepsContainerHtml = `
        <div>
          <div class="options-grid-modern">
            ${ex.options.map(opt => `
              <button class="opt-btn-modern example-opt-btn" data-is-correct="${opt === ex.answer}">
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
          ${ex.explanation ? `<p style="font-size: 0.92rem; color: var(--text-secondary); margin-top: 0.5rem;">${ex.explanation}</p>` : ''}
          <div id="observation-feedback" style="margin-top: 0.5rem;"></div>
        </div>
      `;
    } else {
      stepsContainerHtml = `
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          ${steps.map((st, sIdx) => this.renderWorkedExampleStep(st, sIdx)).join('')}
          ${answersHtml}
        </div>
      `;
    }

    const body = `
      <div class="example-stage-wrapper">
        <div class="example-stepper-nav">
          <span class="example-count-chip">Worked Example ${currentIdx + 1} of ${examples.length}</span>
          <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">Observe the systematic prime division</span>
        </div>

        <div class="question-prompt-card">
          <div class="question-prompt-text">${problemText}</div>
        </div>

        ${trackHtml}
        ${stepsContainerHtml}
      </div>
    `;

    const isLastExample = currentIdx >= examples.length - 1;
    const actions = isLastExample ? `
      ${examples.length > 1 ? `<button class="btn-modern btn-modern-secondary" id="btn-prev-example">← Previous Example</button>` : '<button class="btn-modern btn-modern-secondary" id="btn-back-understand">← Back to Concept</button>'}
      <button class="btn-modern btn-modern-primary" id="btn-ready-try">
        <span>I'm Ready to Try</span>
        <span>→</span>
      </button>
    ` : `
      ${currentIdx > 0 ? `<button class="btn-modern btn-modern-secondary" id="btn-prev-example">← Previous</button>` : '<button class="btn-modern btn-modern-secondary" id="btn-back-understand">← Back to Concept</button>'}
      <button class="btn-modern btn-modern-primary" id="btn-next-example">Next Example (${currentIdx + 2} of ${examples.length}) →</button>
    `;

    const attachEvents = () => {
      const btnBackUnderstand = document.getElementById('btn-back-understand');
      if (btnBackUnderstand) {
        btnBackUnderstand.onclick = () => {
          this.goToStage('understand');
        };
      }

      const btnNext = document.getElementById('btn-next-example');
      if (btnNext) {
        btnNext.onclick = () => {
          this.audio.click();
          this.currentExampleIndex = currentIdx + 1;
          this.render();
        };
      }

      const btnPrev = document.getElementById('btn-prev-example');
      if (btnPrev) {
        btnPrev.onclick = () => {
          this.audio.click();
          this.currentExampleIndex = Math.max(0, currentIdx - 1);
          this.render();
        };
      }

      const btnReveal = document.querySelector('.btn-reveal-next');
      if (btnReveal) {
        btnReveal.onclick = () => {
          this.audio.click();
          const total = Number(btnReveal.dataset.total);
          let current = Number(btnReveal.dataset.current);

          if (ex && ex.steps && current < total) {
            const nextStepHtml = this.renderWorkedExampleStep(ex.steps[current], current);
            const container = document.getElementById(`revealed-steps-${currentIdx}`);
            if (container) {
              container.insertAdjacentHTML('beforeend', nextStepHtml);
            }
            current += 1;
            btnReveal.dataset.current = current;

            if (current >= total) {
              btnReveal.style.display = 'none';
              const ansSummary = document.getElementById(`progressive-answer-${currentIdx}`);
              if (ansSummary) ansSummary.style.display = 'block';
            } else {
              btnReveal.innerHTML = `<span>Reveal Next Step (${total - current} remaining)</span> <span>↓</span>`;
            }
            this.typeset();
          }
        };
      }

      const optBtns = document.querySelectorAll('.example-opt-btn');
      optBtns.forEach(b => {
        b.onclick = () => {
          const isCorrect = b.dataset.isCorrect === 'true';
          if (isCorrect) this.audio.success(); else this.audio.error();
          optBtns.forEach(btn => btn.classList.remove('correct', 'incorrect'));
          b.classList.add(isCorrect ? 'correct' : 'incorrect');
          const fb = document.getElementById('observation-feedback');
          if (fb) {
            fb.innerHTML = `
              <div class="feedback-card-modern ${isCorrect ? 'correct' : 'incorrect'}">
                <div class="feedback-header-row">
                  <span>${isCorrect ? '✓' : '✕'}</span>
                  <span>${isCorrect ? 'Correct Form' : 'Composite Factors Remaining'}</span>
                </div>
                <div class="feedback-body-msg">
                  ${isCorrect ? 'Excellent! Every factor in this product is prime.' : 'Notice that some factors are still composite. Always factorise until every term is prime.'}
                </div>
              </div>
            `;
          }
        };
      });

      const btnReady = document.getElementById('btn-ready-try');
      if (btnReady) {
        btnReady.onclick = () => {
          this.audio.click();
          this.engine.submitInteraction({ question_id: 'w_01', is_correct: true, stage: 'worked_examples' });
          this.render();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // Step Normalization & Factor Ladder Helpers
  // ==========================================================================
  normalizeStep(step) {
    if (!step) return { current: '', divisor: null, quotient: null, divisors: [2, 3, 5, 7, 11, 13] };
    if (Array.isArray(step)) {
      return {
        current: step[0],
        divisor: step[1],
        quotient: step[2],
        divisors: [2, 3, 5, 7, 11, 13]
      };
    }
    return {
      current: step.current,
      divisor: step.correct_divisor || step.divisor,
      quotient: step.quotient,
      divisors: step.divisors || [2, 3, 5, 7, 11, 13]
    };
  }

  syncCompletedStepsHistory(q, stepIdx, isCompleted = false) {
    if (!q || !Array.isArray(q.steps)) return;
    const targetCount = isCompleted ? q.steps.length : stepIdx;
    
    while (this.completedStepsHistory.length < targetCount && this.completedStepsHistory.length < q.steps.length) {
      const idx = this.completedStepsHistory.length;
      const norm = this.normalizeStep(q.steps[idx]);
      this.completedStepsHistory.push({
        current: norm.current,
        divisor: norm.divisor,
        quotient: norm.quotient
      });
    }
  }

  renderFactorLadder(activeNumber, completedSteps = []) {
    const validSteps = (completedSteps || []).filter(s => s && s.current !== undefined && s.current !== null);
    if (validSteps.length === 0 && !activeNumber) return '';

    return `
      <div class="factor-ladder-card">
        <div class="ladder-card-title">Division Ladder</div>
        <div class="math-ladder-display">
          ${validSteps.map(s => {
            const rawDiv = s.divisor !== undefined && s.divisor !== null && !isNaN(s.divisor) ? s.divisor : (s.quotient ? Math.round(s.current / s.quotient) : '•');
            const rawQuot = s.quotient !== undefined && s.quotient !== null && !isNaN(s.quotient) ? s.quotient : (s.divisor ? Math.round(s.current / s.divisor) : '•');
            return `
              <div class="math-ladder-row">
                <span class="ladder-divisor-cell">${rawDiv}</span>
                <span class="ladder-step-bracket">│</span>
                <span class="ladder-target-cell">${s.current}</span>
                <span class="ladder-step-note">${s.current} ÷ ${rawDiv} = <strong>${rawQuot}</strong></span>
              </div>
            `;
          }).join('')}

          ${activeNumber !== undefined && activeNumber !== 1 ? `
            <div class="math-ladder-row active-row">
              <span class="ladder-divisor-cell active-divisor">?</span>
              <span class="ladder-step-bracket">│</span>
              <span class="ladder-target-cell active-target">${activeNumber}</span>
              <span class="ladder-step-badge">Divide by prime</span>
            </div>
          ` : ''}

          ${activeNumber === 1 ? `
            <div class="math-ladder-row complete-row">
              <span class="ladder-divisor-cell"></span>
              <span class="ladder-step-bracket">│</span>
              <span class="ladder-target-cell complete-one">1</span>
              <span class="ladder-step-badge complete-badge">✓ Complete</span>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  formatMathExpression(str) {
    if (!str) return '';
    return String(str)
      .replace(/\s*\^\s*([2-5])/g, (m, p) => {
        const sup = { '2': '²', '3': '³', '4': '⁴', '5': '⁵' };
        return sup[p] || `^${p}`;
      })
      .replace(/\s*\*\s*/g, ' × ')
      .replace(/\s*x\s*/g, ' × ')
      .replace(/\s*\\times\s*/g, ' × ')
      .replace(/\s*×\s*/g, ' × ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  normalizeStep(step) {
    if (!step) return {};
    if (Array.isArray(step)) return { current: step[0], divisor: step[1], quotient: step[2] };
    if (typeof step === 'object') return { ...step };
    return {};
  }
  findOriginalQuestion(qId) {
    if (!qId || !this.topicData?.units) return null;
    const units = this.topicData.units;
    const searchLists = (list) => {
      if (Array.isArray(list)) {
        const found = list.find(item => item && item.id === qId);
        if (found) return found;
      }
      return null;
    };
    if (Array.isArray(units)) {
      for (const u of units) {
        if (u.questions) { const f = searchLists(u.questions); if (f) return f; }
        if (u.practice_stages?.guided_and_independent) { const f = searchLists(u.practice_stages.guided_and_independent); if (f) return f; }
        if (u.practice_stages?.transfer_and_pyq) { const f = searchLists(u.practice_stages.transfer_and_pyq); if (f) return f; }
      }
    } else if (typeof units === 'object') {
      for (const uKey of Object.keys(units)) {
        const u = units[uKey];
        if (u.questions) { const f = searchLists(u.questions); if (f) return f; }
        if (u.examples) { const f = searchLists(u.examples); if (f) return f; }
      }
    }
    return null;
  }

  renderPreviousCompletedSteps(steps, currentStepIdx, history = []) {
    if (!Array.isArray(steps) || steps.length === 0 || currentStepIdx <= 0) return '';
    
    const count = Math.min(currentStepIdx, steps.length);
    const completed = steps.slice(0, count);

    return `
      <div class="previous-completed-steps-wrapper" style="display: flex; flex-direction: column; gap: 0.65rem; margin-bottom: 0.85rem;">
        <div style="font-size: 0.74rem; font-weight: 800; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.05em; display: flex; align-items: center; gap: 0.35rem;">
          <span style="color: var(--success-primary); font-weight: 900;">✓</span>
          <span>Completed Steps (${count} of ${steps.length}):</span>
        </div>
        ${completed.map((st, sIdx) => {
          const histItem = history[sIdx] || {};
          const stepFocus = st.focus || st.prompt || (st.number !== undefined ? `Divide ${st.number}` : `Step ${sIdx + 1}`);
          const stepAns = histItem.answer || histItem.selectedText || (histItem.divisor ? `${histItem.current} ÷ ${histItem.divisor} = ${histItem.quotient}` : null) || st.correct || st.answer || (Array.isArray(st.options) ? st.options[0] : '');

          return `
            <div class="step-card-modern" style="border-left: 4px solid var(--success-primary); background: var(--bg-surface-inset); padding: 0.75rem 0.95rem;">
              <div class="step-card-modern-header" style="margin-bottom: 0.35rem;">
                <span class="step-num-badge" style="background: var(--success-soft); color: var(--success-primary);">✓ Step ${sIdx + 1}</span>
                <span class="step-target-value" style="font-size: 0.92rem; font-weight: 750; color: var(--text-primary);">${stepFocus}</span>
              </div>
              ${stepAns ? `
                <div style="font-size: 0.88rem; color: var(--text-secondary); margin-top: 0.3rem; display: flex; align-items: baseline; gap: 0.45rem; flex-wrap: wrap;">
                  <strong style="color: var(--success-primary); font-size: 0.78rem; text-transform: uppercase;">Solved:</strong>
                  <span class="equation-math" style="font-weight: 750; color: var(--text-primary); background: var(--bg-surface); padding: 0.2rem 0.55rem; border-radius: var(--radius-xs); border: 1px solid var(--border-subtle);">${this.formatMathExpression(stepAns)}</span>
                </div>
              ` : ''}
            </div>
          `;
        }).join('')}
      </div>
    `;
  }

  renderCompletedSolutionCard(q, isLadderQuestion, stepsHistory = []) {
    const origQ = this.findOriginalQuestion(q.id) || q;
    const factorisations = origQ.prime_factorisations || q.prime_factorisations || {};

    if (isLadderQuestion) {
      const divisorsList = stepsHistory.map(s => s.divisor).filter(Boolean);
      let expandedForm = divisorsList.join(' × ');
      let expForm = expandedForm;
      if (divisorsList.length > 0) {
        const counts = {};
        divisorsList.forEach(d => { counts[d] = (counts[d] || 0) + 1; });
        const expSup = { 2: '²', 3: '³', 4: '⁴', 5: '⁵' };
        expForm = Object.keys(counts).map(d => {
          const c = counts[d];
          return c > 1 ? `${d}${expSup[c] || `^${c}`}` : `${d}`;
        }).join(' × ');
      }

      return `
        <div class="factor-complete-summary-card">
          <div class="complete-title-line">
            <span>✓</span>
            <span>Factorisation Complete</span>
          </div>
          <div class="summary-answer-block">
            <div class="summary-answer-label">Expanded Form:</div>
            <div class="summary-equation-badge">
              ${q.number ? `<span>${q.number} = </span>` : ''}
              <span class="equation-math">${this.formatMathExpression(expandedForm)}</span>
            </div>
          </div>
          <div class="summary-answer-block">
            <div class="summary-answer-label">Prime Factorisation:</div>
            <div class="summary-equation-badge">
              ${q.number ? `<span>${q.number} = </span>` : ''}
              <span class="equation-math">${this.formatMathExpression(expForm)}</span>
            </div>
          </div>
        </div>
      `;
    }

    // HCF & LCM and Structured Question Solutions
    let answerHtml = '';
    const ans = origQ.answer || origQ.final_answer || q.answer || '';

    if (typeof ans === 'object' && ans !== null) {
      if (ans.hcf !== undefined && ans.lcm !== undefined) {
        answerHtml = `
          <div class="summary-answer-block">
            <div class="summary-answer-label">Highest Common Factor (HCF):</div>
            <div class="summary-equation-badge">
              <span class="equation-math">HCF = ${this.formatMathExpression(ans.hcf)}</span>
            </div>
          </div>
          <div class="summary-answer-block">
            <div class="summary-answer-label">Least Common Multiple (LCM):</div>
            <div class="summary-equation-badge">
              <span class="equation-math">LCM = ${this.formatMathExpression(ans.lcm)}</span>
            </div>
          </div>
        `;
      } else {
        answerHtml = Object.entries(ans).map(([key, val]) => `
          <div class="summary-answer-block">
            <div class="summary-answer-label">${key.replace(/_/g, ' ').toUpperCase()}:</div>
            <div class="summary-equation-badge">
              <span class="equation-math">${this.formatMathExpression(val)}</span>
            </div>
          </div>
        `).join('');
      }
    } else if (ans) {
      answerHtml = `
        <div class="summary-answer-block">
          <div class="summary-answer-label">Complete Solution:</div>
          <div class="summary-equation-badge">
            <span class="equation-math">${this.formatMathExpression(ans)}</span>
          </div>
        </div>
      `;
    }

    if (origQ.expanded_answer && !answerHtml.includes(origQ.expanded_answer)) {
      answerHtml += `
        <div class="summary-answer-block" style="margin-top: 0.35rem;">
          <div class="summary-answer-label">Expanded Form:</div>
          <div class="summary-equation-badge">
            <span class="equation-math">${this.formatMathExpression(origQ.expanded_answer)}</span>
          </div>
        </div>
      `;
    }

    if (origQ.exponential_answer && !answerHtml.includes(origQ.exponential_answer)) {
      answerHtml += `
        <div class="summary-answer-block" style="margin-top: 0.35rem;">
          <div class="summary-answer-label">Exponential Form:</div>
          <div class="summary-equation-badge">
            <span class="equation-math">${this.formatMathExpression(origQ.exponential_answer)}</span>
          </div>
        </div>
      `;
    }

    return `
      ${Object.keys(factorisations).length > 0 ? `
        <div class="factor-ladder-card" style="background: var(--bg-surface-inset); margin-bottom: 0.75rem; border-left: 4px solid var(--brand-primary); padding: 0.75rem 1rem;">
          <div style="font-size: 0.72rem; font-weight: 800; text-transform: uppercase; color: var(--brand-primary); margin-bottom: 0.35rem;">
            📊 Given Prime Factorisations:
          </div>
          <div style="display: flex; flex-wrap: wrap; gap: 0.65rem;">
            ${Object.entries(factorisations).map(([num, factors]) => `
              <div style="font-family: var(--font-mono); font-size: 0.94rem; font-weight: 750; background: var(--bg-surface); padding: 0.35rem 0.65rem; border-radius: var(--radius-xs); border: 1px solid var(--border-subtle);">
                ${num} = <span style="color: var(--brand-primary);">${factors}</span>
              </div>
            `).join('')}
          </div>
        </div>
      ` : ''}

      <div class="factor-complete-summary-card">
        <div class="complete-title-line">
          <span>✓</span>
          <span>Question Solved</span>
        </div>
        ${answerHtml || `
          <div class="summary-answer-block">
            <div class="summary-answer-label">Solution:</div>
            <div class="summary-equation-badge">
              <span class="equation-math">Correctly Solved</span>
            </div>
          </div>
        `}
      </div>

      ${origQ.explanation || origQ.reason || origQ.solution?.explanation ? `
        <div style="margin-top: 0.65rem; font-size: 0.85rem; color: var(--text-secondary); background: var(--bg-surface-soft); padding: 0.65rem 0.85rem; border-radius: var(--radius-xs); border: 1px solid var(--border-subtle); line-height: 1.45;">
          <strong>💡 Key Insight:</strong> ${origQ.explanation || origQ.reason || origQ.solution?.explanation}
        </div>
      ` : ''}
    `;
  }

  // ==========================================================================
  // 3. Try (Guided Stepwise Practice with Factor Ladder & Live Feedback)
  // ==========================================================================
  renderTry() {
    if (!this.currentQuestion) {
      this.currentQuestion = this.engine.getNextQuestion();
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
    }
    if (!this.currentQuestion) return { body: '<p>No questions available.</p>' };

    const q = this.currentQuestion;
    const promptText = q.question || `Prime factorise ${q.number || ''}:`;
    const steps = Array.isArray(q.steps) ? q.steps : [];
    const stepIdx = Math.min(this.currentStepIndex || 0, Math.max(0, steps.length - 1));
    const activeStep = steps[stepIdx];
    const activeStepNorm = this.normalizeStep(activeStep);
    const availableDivisors = activeStepNorm.divisors || [2, 3, 5, 7, 11, 13];

    // Check if this is a division ladder question (e.g. FTA) or a multi-step HCF/LCM question
    const isLadderQuestion = Boolean(q.number !== undefined && (activeStepNorm.current !== undefined || (activeStep && (activeStep.divisor !== undefined || activeStep.correct_divisor !== undefined || Array.isArray(activeStep)))));

    if (this.isQuestionCompleted) {
      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${isLadderQuestion ? this.renderFactorLadder(1, this.completedStepsHistory) : this.renderPreviousCompletedSteps(steps, steps.length, this.completedStepsHistory)}
        ${this.renderCompletedSolutionCard(q, isLadderQuestion, this.completedStepsHistory)}
      `;

      const actions = `
        <button class="btn-modern btn-modern-primary" id="btn-next-question">
          <span>Next Practice Question</span>
          <span>→</span>
        </button>
      `;

      const attachEvents = () => {
        const btnNext = document.getElementById('btn-next-question');
        if (btnNext) {
          btnNext.onclick = () => {
            this.audio.click();
            this.currentStepIndex = 0;
            this.currentQuestion = null;
            this.completedStepsHistory = [];
            this.isQuestionCompleted = false;
            this.render();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // NON-LADDER (HCF/LCM Structured Step Workspace)
    if (!isLadderQuestion && activeStep) {
      const hasOptions = Array.isArray(activeStep.options) && activeStep.options.length > 0;
      const stepFocus = activeStep.focus || activeStep.prompt || `Step ${stepIdx + 1}`;
      
      const discoveredFactorisations = {};
      if (Array.isArray(this.completedStepsHistory)) {
        this.completedStepsHistory.forEach(s => {
          if (s.factorNumber && s.factorisation) {
            discoveredFactorisations[s.factorNumber] = s.factorisation;
          }
        });
      }

      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${Object.keys(discoveredFactorisations).length > 0 ? `
          <div class="factor-ladder-card" style="background: var(--bg-surface-inset); margin-bottom: 1rem; border-left: 4px solid var(--brand-primary); padding: 0.85rem 1rem;">
            <div style="font-size: 0.76rem; font-weight: 800; text-transform: uppercase; color: var(--brand-primary); margin-bottom: 0.45rem;">
              ✓ Your Discovered Prime Factorisations:
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.65rem;">
              ${Object.entries(discoveredFactorisations).map(([num, factors]) => `
                <div style="font-family: var(--font-mono); font-size: 0.96rem; font-weight: 750; background: var(--bg-surface); padding: 0.4rem 0.75rem; border-radius: var(--radius-xs); border: 1px solid var(--border-subtle); box-shadow: var(--shadow-xs);">
                  ${num} = <span style="color: var(--brand-primary);">${factors}</span>
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        ${this.renderPreviousCompletedSteps(steps, stepIdx, this.completedStepsHistory)}

        <div class="step-card-modern">
          <div class="step-card-modern-header">
            <span class="step-num-badge">Step ${stepIdx + 1} of ${steps.length}</span>
            <span class="step-target-value">${stepFocus}</span>
          </div>

          ${hasOptions ? `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">${activeStep.prompt || 'Select the correct rule or value:'}</div>
            <div class="options-grid-vertical" id="hcf-step-options-grid">
              ${activeStep.options.map((opt, oIdx) => `
                <button type="button" class="opt-btn-choice hcf-step-opt-btn" data-val="${opt}" data-idx="${oIdx}">
                  <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                  <span>${opt}</span>
                </button>
              `).join('')}
            </div>
          ` : `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">Enter the ${stepFocus} value:</div>
            <input type="text" id="hcf-step-ans" class="input-field-modern" placeholder="e.g. 2² × 3 or 12" autocomplete="off" style="font-size: 1.08rem; font-family: var(--font-mono);">
            ${this.renderMathKeypad('hcf-step-ans')}
          `}

          <div id="hcf-step-feedback" class="inline-tip-box" style="display: none; margin-top: 0.75rem;"></div>
        </div>
      `;

      const actions = `
        ${!hasOptions ? `
          <button class="btn-modern btn-modern-primary" id="btn-hcf-step-check">
            <span>Check</span>
            <span>✓</span>
          </button>
        ` : ''}
        <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
          <span>← Back to Examples</span>
        </button>
        <button class="btn-modern btn-modern-secondary" id="btn-hint">
          <span>💡 Need a Hint?</span>
        </button>
      `;

      const attachEvents = () => {
        const btnBackStage = document.getElementById('btn-back-stage');
        if (btnBackStage) {
          btnBackStage.onclick = () => {
            this.goToStage('see');
          };
        }

        const fbBox = document.getElementById('hcf-step-feedback');
        const origQ = this.findOriginalQuestion(q.id) || q;
        const currentStepDef = origQ.steps ? origQ.steps[stepIdx] : activeStep;
        const factorNum = currentStepDef?.factor_number || (activeStep.focus && activeStep.focus.startsWith('Factorise ') ? activeStep.focus.replace('Factorise ', '').trim() : null);

        if (hasOptions) {
          const optBtns = document.querySelectorAll('.hcf-step-opt-btn');
          optBtns.forEach(btn => {
            btn.onclick = () => {
              const val = btn.dataset.val;
              const idx = parseInt(btn.dataset.idx, 10);
              this.audio.click();

              const evalRes = this.engine.submitInteraction({
                question_id: q.id,
                step_id: stepIdx,
                selected_index: idx,
                response: val
              });

              if (evalRes.is_correct) {
                this.audio.success();
                optBtns.forEach(b => b.classList.remove('selected', 'incorrect', 'correct'));
                btn.classList.add('correct');
                const bullet = btn.querySelector('.choice-radio-bullet');
                if (bullet) bullet.innerText = '●';

                this.completedStepsHistory.push({
                  stepIdx,
                  step_id: stepIdx,
                  focus: stepFocus,
                  answer: val,
                  factorNumber: factorNum,
                  factorisation: currentStepDef?.correct || val
                });

                if (stepIdx < steps.length - 1) {
                  this.currentStepIndex = stepIdx + 1;
                  setTimeout(() => { this.render(); }, 450);
                } else {
                  this.isQuestionCompleted = true;
                  setTimeout(() => { this.render(); }, 450);
                }
              } else {
                this.audio.error();
                btn.classList.add('incorrect');
                if (fbBox) {
                  fbBox.className = 'inline-tip-box error';
                  fbBox.innerHTML = `✕ ${evalRes.feedback || activeStep.feedback?.wrong || 'Check your rule and try again.'}`;
                  fbBox.style.display = 'block';
                }
              }
            };
          });
        } else {
          this.attachMathKeypadEvents('hcf-step-ans');
          const handleCheck = () => {
            const inputVal = document.getElementById('hcf-step-ans')?.value?.trim();
            if (!inputVal) return;
            const evalRes = this.engine.submitInteraction({
              question_id: q.id,
              step_id: stepIdx,
              response: inputVal
            });

            if (evalRes.is_correct) {
              this.audio.success();
              this.completedStepsHistory.push({
                stepIdx,
                step_id: stepIdx,
                focus: stepFocus,
                answer: inputVal,
                factorNumber: factorNum,
                factorisation: currentStepDef?.correct || inputVal
              });

              if (stepIdx < steps.length - 1) {
                this.currentStepIndex = stepIdx + 1;
                setTimeout(() => { this.render(); }, 450);
              } else {
                this.isQuestionCompleted = true;
                setTimeout(() => { this.render(); }, 450);
              }
            } else {
              this.audio.error();
              if (fbBox) {
                fbBox.className = 'inline-tip-box error';
                fbBox.innerHTML = `✕ ${evalRes.feedback || 'Check your calculation.'}`;
                fbBox.style.display = 'block';
              }
            }
          };

          const checkBtn = document.getElementById('btn-hcf-step-check');
          if (checkBtn) checkBtn.onclick = handleCheck;
          const inputElem = document.getElementById('hcf-step-ans');
          if (inputElem) inputElem.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
        }

        const btnHint = document.getElementById('btn-hint');
        if (btnHint) {
          btnHint.onclick = () => {
            this.audio.hint();
            this.requestHint();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // LADDER QUESTION WORKSPACE
    this.syncCompletedStepsHistory(q, stepIdx, false);
    const currentTarget = activeStepNorm.current || q.number;

    const body = `
      <div class="question-prompt-card">
        <div class="question-prompt-text">${promptText}</div>
      </div>

      <div class="step-card-modern">
        <div class="step-card-modern-header">
          <span class="step-num-badge">Step ${stepIdx + 1} of ${steps.length}</span>
          <span class="step-target-value">Divide ${currentTarget}</span>
        </div>

        ${this.renderFactorLadder(currentTarget, this.completedStepsHistory)}

        <div class="input-group-modern" id="step1-wrapper">
          <div class="input-label-modern">Choose the smallest prime divisor for ${currentTarget}:</div>
          <div class="options-grid-modern" id="divisor-grid">
            ${availableDivisors.map(d => `
              <button type="button" class="opt-btn-modern divisor-opt" data-val="${d}">
                <span>${d}</span>
              </button>
            `).join('')}
          </div>
          <div id="step1-inline-tip" class="inline-tip-box" style="display: none;"></div>
        </div>

        <div class="input-group-modern" id="step2-wrapper" style="display: none; animation: stageEnter var(--transition-medium) ease-out;">
          <div class="input-label-modern">Calculate quotient:</div>
          <div class="quotient-calc-row">
            <span class="math-target">${currentTarget}</span>
            <span class="math-op">÷</span>
            <span id="chosen-divisor-label" class="math-div-tag">2</span>
            <span class="math-op">=</span>
            <input type="number" id="quotient-input" class="input-field-modern quotient-in" placeholder="Quotient" inputmode="numeric">
            <button type="button" class="btn-modern btn-modern-primary btn-inline-check" id="btn-check">
              <span>Check</span>
              <span>✓</span>
            </button>
          </div>
        </div>
      </div>
    `;

    const actions = `
      <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
        <span>← Back to Examples</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-hint">
        <span>💡 Need a Hint?</span>
      </button>
    `;

    const attachEvents = () => {
      const btnBackStage = document.getElementById('btn-back-stage');
      if (btnBackStage) {
        btnBackStage.onclick = () => {
          this.goToStage('see');
        };
      }

      this.selectedChoice = null;

      const optBtns = document.querySelectorAll('.divisor-opt');
      const tipBox = document.getElementById('step1-inline-tip');
      const step2 = document.getElementById('step2-wrapper');
      const qInput = document.getElementById('quotient-input');
      const lbl = document.getElementById('chosen-divisor-label');

      optBtns.forEach(btn => {
        btn.onclick = () => {
          const val = Number(btn.dataset.val);
          this.selectedChoice = val;
          this.audio.click();

          const evalRes = this.engine.submitInteraction({
            question_id: q.id,
            step_id: stepIdx,
            divisor: val,
            input_type: 'divisor'
          });

          if (evalRes.is_correct) {
            this.audio.success();
            optBtns.forEach(b => {
              b.classList.remove('selected', 'incorrect', 'warn-alt', 'correct');
              if (Number(b.dataset.val) === val) b.classList.add('correct');
            });

            if (tipBox) {
              tipBox.className = 'inline-tip-box success';
              tipBox.innerHTML = `✓ ${currentTarget} is divisible by ${val}. Now enter the quotient below.`;
              tipBox.style.display = 'block';
            }

            if (lbl) lbl.innerText = val;
            if (step2) step2.style.display = 'block';
            if (qInput) {
              qInput.value = '';
              qInput.focus();
            }
          } else {
            this.audio.error();
            optBtns.forEach(b => b.classList.remove('selected', 'correct'));
            const isAlternative = evalRes.mathematical_validity === 'valid_alternative';

            if (isAlternative) {
              btn.classList.add('warn-alt');
              if (tipBox) {
                tipBox.className = 'inline-tip-box warning';
                tipBox.innerHTML = `💡 ${evalRes.feedback || `${val} is a valid factor, but dividing by the smallest prime first is recommended.`}`;
                tipBox.style.display = 'block';
              }
            } else {
              btn.classList.add('incorrect');
              if (tipBox) {
                tipBox.className = 'inline-tip-box error';
                tipBox.innerHTML = `✕ ${evalRes.feedback || `${currentTarget} is not divisible by ${val}. Try another prime.`}`;
                tipBox.style.display = 'block';
              }
            }

            if (step2) step2.style.display = 'none';
          }
        };
      });

      const handleCheck = () => {
        const quotVal = qInput?.value?.trim();
        if (!this.selectedChoice || !quotVal) {
          if (tipBox) {
            tipBox.className = 'inline-tip-box warning';
            tipBox.innerHTML = 'Please enter your calculated quotient.';
            tipBox.style.display = 'block';
          }
          return;
        }

        const result = this.engine.submitInteraction({
          question_id: q.id,
          step_id: stepIdx,
          divisor: this.selectedChoice,
          quotient: Number(quotVal)
        });

        if (result.is_correct) {
          this.audio.success();
          this.completedStepsHistory.push({
            current: currentTarget,
            divisor: this.selectedChoice,
            quotient: Number(quotVal)
          });

          if (stepIdx < steps.length - 1) {
            this.currentStepIndex = stepIdx + 1;
            setTimeout(() => { this.render(); }, 450);
          } else {
            this.isQuestionCompleted = true;
            setTimeout(() => { this.render(); }, 450);
          }
        } else {
          this.audio.error();
          if (tipBox) {
            tipBox.className = 'inline-tip-box error';
            tipBox.innerHTML = `✕ Incorrect quotient. Calculate ${currentTarget} ÷ ${this.selectedChoice}.`;
            tipBox.style.display = 'block';
          }
        }
      };

      const btnCheck = document.getElementById('btn-check');
      if (btnCheck) btnCheck.onclick = handleCheck;

      if (qInput) {
        qInput.onkeydown = (e) => {
          if (e.key === 'Enter') handleCheck();
        };
      }

      const btnHint = document.getElementById('btn-hint');
      if (btnHint) {
        btnHint.onclick = () => {
          this.audio.hint();
          this.requestHint();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // 4. Think (Faded Guidance - Interactive Step-by-Step Factorizer)
  // ==========================================================================
  renderThink() {
    if (!this.currentQuestion) {
      this.currentQuestion = this.engine.getNextQuestion();
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
    }
    if (!this.currentQuestion) return { body: '<p>No questions available.</p>' };

    const q = this.currentQuestion;
    const promptText = q.question || `Factorise ${q.number || ''}:`;
    const steps = Array.isArray(q.steps) ? q.steps : [];
    const stepIdx = Math.min(this.currentStepIndex || 0, Math.max(0, steps.length - 1));
    const activeStep = steps[stepIdx];
    const activeStepNorm = this.normalizeStep(activeStep);
    const currentNumber = activeStepNorm.current || q.number;
    const primeChoices = [2, 3, 5, 7, 11, 13];

    const isLadderQuestion = Boolean(q.number !== undefined && (activeStepNorm.current !== undefined || (activeStep && (activeStep.divisor !== undefined || activeStep.correct_divisor !== undefined || Array.isArray(activeStep)))));

    if (this.isQuestionCompleted) {
      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${isLadderQuestion ? this.renderFactorLadder(1, this.completedStepsHistory) : this.renderPreviousCompletedSteps(steps, steps.length, this.completedStepsHistory)}
        ${this.renderCompletedSolutionCard(q, isLadderQuestion, this.completedStepsHistory)}
      `;

      const actions = `
        <button class="btn-modern btn-modern-primary" id="btn-next-question">
          <span>Next Practice Question</span>
          <span>→</span>
        </button>
      `;

      const attachEvents = () => {
        const btnNext = document.getElementById('btn-next-question');
        if (btnNext) {
          btnNext.onclick = () => {
            this.audio.click();
            this.currentStepIndex = 0;
            this.currentQuestion = null;
            this.completedStepsHistory = [];
            this.isQuestionCompleted = false;
            this.render();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // NON-LADDER (HCF/LCM Structured Step Workspace)
    if (!isLadderQuestion && activeStep) {
      const hasOptions = Array.isArray(activeStep.options) && activeStep.options.length > 0;
      const stepFocus = activeStep.focus || activeStep.prompt || `Step ${stepIdx + 1}`;
      
      const discoveredFactorisations = {};
      if (Array.isArray(this.completedStepsHistory)) {
        this.completedStepsHistory.forEach(s => {
          if (s.factorNumber && s.factorisation) {
            discoveredFactorisations[s.factorNumber] = s.factorisation;
          }
        });
      }

      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${Object.keys(discoveredFactorisations).length > 0 ? `
          <div class="factor-ladder-card" style="background: var(--bg-surface-inset); margin-bottom: 1rem; border-left: 4px solid var(--brand-primary); padding: 0.85rem 1rem;">
            <div style="font-size: 0.76rem; font-weight: 800; text-transform: uppercase; color: var(--brand-primary); margin-bottom: 0.45rem;">
              ✓ Your Discovered Prime Factorisations:
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.65rem;">
              ${Object.entries(discoveredFactorisations).map(([num, factors]) => `
                <div style="font-family: var(--font-mono); font-size: 0.96rem; font-weight: 750; background: var(--bg-surface); padding: 0.4rem 0.75rem; border-radius: var(--radius-xs); border: 1px solid var(--border-subtle); box-shadow: var(--shadow-xs);">
                  ${num} = <span style="color: var(--brand-primary);">${factors}</span>
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        ${this.renderPreviousCompletedSteps(steps, stepIdx, this.completedStepsHistory)}

        <div class="step-card-modern">
          <div class="step-card-modern-header">
            <span class="step-num-badge">Step ${stepIdx + 1} of ${steps.length}</span>
            <span class="step-target-value">${stepFocus}</span>
          </div>

          ${hasOptions ? `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">${activeStep.prompt || 'Select the correct rule or value:'}</div>
            <div class="options-grid-vertical" id="think-step-options-grid">
              ${activeStep.options.map((opt, oIdx) => `
                <button type="button" class="opt-btn-choice think-step-opt-btn" data-val="${opt}" data-idx="${oIdx}">
                  <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                  <span>${opt}</span>
                </button>
              `).join('')}
            </div>
          ` : `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">Enter the ${stepFocus} value:</div>
            <input type="text" id="think-step-ans" class="input-field-modern" placeholder="e.g. 2² × 3 or 12" autocomplete="off" style="font-size: 1.08rem; font-family: var(--font-mono);">
            ${this.renderMathKeypad('think-step-ans')}
          `}

          <div id="think-step-feedback" class="inline-tip-box" style="display: none; margin-top: 0.75rem;"></div>
        </div>
      `;

      const actions = `
        ${!hasOptions ? `
          <button class="btn-modern btn-modern-primary" id="btn-think-step-check">
            <span>Check</span>
            <span>✓</span>
          </button>
        ` : ''}
        <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
          <span>← Back to Guided</span>
        </button>
        <button class="btn-modern btn-modern-secondary" id="btn-hint">
          <span>💡 Need a Hint?</span>
        </button>
      `;

      const attachEvents = () => {
        const btnBackStage = document.getElementById('btn-back-stage');
        if (btnBackStage) {
          btnBackStage.onclick = () => {
            this.goToStage('try');
          };
        }

        const fbBox = document.getElementById('think-step-feedback');
        const origQ = this.findOriginalQuestion(q.id) || q;
        const currentStepDef = origQ.steps ? origQ.steps[stepIdx] : activeStep;
        const factorNum = currentStepDef?.factor_number || (activeStep.focus && activeStep.focus.startsWith('Factorise ') ? activeStep.focus.replace('Factorise ', '').trim() : null);

        if (hasOptions) {
          const optBtns = document.querySelectorAll('.think-step-opt-btn');
          optBtns.forEach(btn => {
            btn.onclick = () => {
              const val = btn.dataset.val;
              const idx = parseInt(btn.dataset.idx, 10);
              this.audio.click();

              const evalRes = this.engine.submitInteraction({
                question_id: q.id,
                step_id: stepIdx,
                selected_index: idx,
                response: val
              });

              if (evalRes.is_correct) {
                this.audio.success();
                optBtns.forEach(b => b.classList.remove('selected', 'incorrect', 'correct'));
                btn.classList.add('correct');
                const bullet = btn.querySelector('.choice-radio-bullet');
                if (bullet) bullet.innerText = '●';

                this.completedStepsHistory.push({
                  stepIdx,
                  step_id: stepIdx,
                  focus: stepFocus,
                  answer: val,
                  factorNumber: factorNum,
                  factorisation: currentStepDef?.correct || val
                });

                if (stepIdx < steps.length - 1) {
                  this.currentStepIndex = stepIdx + 1;
                  setTimeout(() => { this.render(); }, 450);
                } else {
                  this.isQuestionCompleted = true;
                  setTimeout(() => { this.render(); }, 450);
                }
              } else {
                this.audio.error();
                btn.classList.add('incorrect');
                if (fbBox) {
                  fbBox.className = 'inline-tip-box error';
                  fbBox.innerHTML = `✕ ${evalRes.feedback || activeStep.feedback?.wrong || 'Check your rule and try again.'}`;
                  fbBox.style.display = 'block';
                }
              }
            };
          });
        } else {
          this.attachMathKeypadEvents('think-step-ans');
          const handleCheck = () => {
            const inputVal = document.getElementById('think-step-ans')?.value?.trim();
            if (!inputVal) return;
            const evalRes = this.engine.submitInteraction({
              question_id: q.id,
              step_id: stepIdx,
              response: inputVal
            });

            if (evalRes.is_correct) {
              this.audio.success();
              this.completedStepsHistory.push({
                stepIdx,
                step_id: stepIdx,
                focus: stepFocus,
                answer: inputVal,
                factorNumber: factorNum,
                factorisation: currentStepDef?.correct || inputVal
              });

              if (stepIdx < steps.length - 1) {
                this.currentStepIndex = stepIdx + 1;
                setTimeout(() => { this.render(); }, 450);
              } else {
                this.isQuestionCompleted = true;
                setTimeout(() => { this.render(); }, 450);
              }
            } else {
              this.audio.error();
              if (fbBox) {
                fbBox.className = 'inline-tip-box error';
                fbBox.innerHTML = `✕ ${evalRes.feedback || 'Check your calculation.'}`;
                fbBox.style.display = 'block';
              }
            }
          };

          const checkBtn = document.getElementById('btn-think-step-check');
          if (checkBtn) checkBtn.onclick = handleCheck;
          const inputElem = document.getElementById('think-step-ans');
          if (inputElem) inputElem.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
        }

        const btnHint = document.getElementById('btn-hint');
        if (btnHint) {
          btnHint.onclick = () => {
            this.audio.hint();
            this.requestHint();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // DIRECT QUESTION (No step subdivisions, e.g. multiple choice reasoning in Think)
    if (!isLadderQuestion) {
      const hasOptions = Array.isArray(q.options) && q.options.length > 0;

      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        <div class="step-card-modern">
          ${hasOptions ? `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">Select the correct statement:</div>
            <div class="options-grid-vertical" id="think-direct-options-grid">
              ${q.options.map((opt, oIdx) => `
                <button type="button" class="opt-btn-choice think-direct-opt-btn" data-val="${opt}" data-idx="${oIdx}">
                  <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                  <span>${opt}</span>
                </button>
              `).join('')}
            </div>
          ` : `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">Your response:</div>
            <input type="text" id="think-direct-ans" class="input-field-modern" placeholder="e.g. 2² × 3 or 252" autocomplete="off" style="font-size: 1.08rem; font-family: var(--font-mono);">
            ${this.renderMathKeypad('think-direct-ans')}
          `}

          <div id="think-direct-feedback" class="inline-tip-box" style="display: none; margin-top: 0.75rem;"></div>
        </div>
      `;

      const actions = `
        ${!hasOptions ? `
          <button class="btn-modern btn-modern-primary" id="btn-think-direct-check">
            <span>Check</span>
            <span>✓</span>
          </button>
        ` : ''}
        <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
          <span>← Back to Guided</span>
        </button>
        <button class="btn-modern btn-modern-secondary" id="btn-hint">
          <span>💡 Need a Hint?</span>
        </button>
      `;

      const attachEvents = () => {
        const btnBackStage = document.getElementById('btn-back-stage');
        if (btnBackStage) {
          btnBackStage.onclick = () => {
            this.goToStage('try');
          };
        }

        const fbBox = document.getElementById('think-direct-feedback');

        if (hasOptions) {
          const optBtns = document.querySelectorAll('.think-direct-opt-btn');
          optBtns.forEach(btn => {
            btn.onclick = () => {
              const val = btn.dataset.val;
              const idx = parseInt(btn.dataset.idx, 10);
              this.audio.click();

              const evalRes = this.engine.submitInteraction({
                question_id: q.id,
                selected_index: idx,
                response: val
              });

              if (evalRes.is_correct) {
                this.audio.success();
                optBtns.forEach(b => b.classList.remove('selected', 'incorrect', 'correct'));
                btn.classList.add('correct');
                const bullet = btn.querySelector('.choice-radio-bullet');
                if (bullet) bullet.innerText = '●';

                this.isQuestionCompleted = true;
                this.lastSubmittedAnswer = val;
                setTimeout(() => { this.render(); }, 450);
              } else {
                this.audio.error();
                btn.classList.add('incorrect');
                if (fbBox) {
                  fbBox.className = 'inline-tip-box error';
                  fbBox.innerHTML = `✕ ${evalRes.feedback || 'Check your reasoning and try again.'}`;
                  fbBox.style.display = 'block';
                }
              }
            };
          });
        } else {
          this.attachMathKeypadEvents('think-direct-ans');
          const handleCheck = () => {
            const inputVal = document.getElementById('think-direct-ans')?.value?.trim();
            if (!inputVal) return;
            const evalRes = this.engine.submitInteraction({
              question_id: q.id,
              response: inputVal
            });

            if (evalRes.is_correct) {
              this.audio.success();
              this.isQuestionCompleted = true;
              this.lastSubmittedAnswer = inputVal;
              setTimeout(() => { this.render(); }, 450);
            } else {
              this.audio.error();
              if (fbBox) {
                fbBox.className = 'inline-tip-box error';
                fbBox.innerHTML = `✕ ${evalRes.feedback || 'Check your calculation.'}`;
                fbBox.style.display = 'block';
              }
            }
          };

          const checkBtn = document.getElementById('btn-think-direct-check');
          if (checkBtn) checkBtn.onclick = handleCheck;
          const inputElem = document.getElementById('think-direct-ans');
          if (inputElem) inputElem.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
        }

        const btnHint = document.getElementById('btn-hint');
        if (btnHint) {
          btnHint.onclick = () => {
            this.audio.hint();
            this.requestHint();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // LADDER WORKSPACE FOR FTA
    this.syncCompletedStepsHistory(q, stepIdx, false);

    const body = `
      <div class="question-prompt-card">
        <div class="question-prompt-text">${promptText}</div>
      </div>

      <div class="step-card-modern">
        <div class="step-card-modern-header">
          <span class="step-num-badge">Step ${stepIdx + 1} of ${steps.length}</span>
          <span class="step-target-value">Divide ${currentNumber}</span>
        </div>

        ${this.renderFactorLadder(currentNumber, this.completedStepsHistory)}

        <div class="input-group-modern" id="think-prime-group">
          <div class="input-label-modern">Choose the smallest prime divisor for ${currentNumber}:</div>
          <div class="options-grid-modern" id="think-prime-grid">
            ${primeChoices.map(p => `
              <button type="button" class="opt-btn-modern think-prime-btn" data-val="${p}">
                <span>${p}</span>
              </button>
            `).join('')}
          </div>
          <div id="think-inline-tip" class="inline-tip-box" style="display: none;"></div>
        </div>

        <div class="input-group-modern" id="think-calc-group" style="display: none; animation: stageEnter var(--transition-medium) ease-out;">
          <div class="input-label-modern">Calculate quotient:</div>
          <div class="quotient-calc-row">
            <span class="math-target">${currentNumber}</span>
            <span class="math-op">÷</span>
            <span id="think-chosen-prime-tag" class="math-div-tag">2</span>
            <span class="math-op">=</span>
            <input type="number" id="think-quotient-in" class="input-field-modern quotient-in" placeholder="Quotient" inputmode="numeric">
            <button type="button" class="btn-modern btn-modern-primary btn-inline-check" id="btn-think-check">
              <span>Check</span>
              <span>✓</span>
            </button>
          </div>
        </div>
      </div>
    `;

    const actions = `
      <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
        <span>← Back to Guided</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-hint">
        <span>💡 Need a Hint?</span>
      </button>
    `;

    const attachEvents = () => {
      const btnBackStage = document.getElementById('btn-back-stage');
      if (btnBackStage) {
        btnBackStage.onclick = () => { this.goToStage('try'); };
      }

      this.selectedChoice = null;
      const primeBtns = document.querySelectorAll('.think-prime-btn');
      const tipBox = document.getElementById('think-inline-tip');
      const calcGroup = document.getElementById('think-calc-group');
      const primeTag = document.getElementById('think-chosen-prime-tag');
      const quotIn = document.getElementById('think-quotient-in');

      primeBtns.forEach(btn => {
        btn.onclick = () => {
          const val = Number(btn.dataset.val);
          this.selectedChoice = val;
          this.audio.click();

          const evalRes = this.engine.submitInteraction({
            question_id: q.id,
            step_id: stepIdx,
            divisor: val,
            input_type: 'divisor'
          });

          if (evalRes.is_correct) {
            this.audio.success();
            primeBtns.forEach(b => {
              b.classList.remove('selected', 'incorrect', 'warn-alt', 'correct');
              if (Number(b.dataset.val) === val) b.classList.add('correct');
            });
            if (tipBox) {
              tipBox.className = 'inline-tip-box success';
              tipBox.innerHTML = `✓ ${currentNumber} is divisible by ${val}. Now enter the quotient below.`;
              tipBox.style.display = 'block';
            }
            if (primeTag) primeTag.innerText = val;
            if (calcGroup) calcGroup.style.display = 'block';
            if (quotIn) { quotIn.value = ''; quotIn.focus(); }
          } else {
            this.audio.error();
            primeBtns.forEach(b => b.classList.remove('selected', 'correct'));
            if (evalRes.mathematical_validity === 'valid_alternative') {
              btn.classList.add('warn-alt');
              if (tipBox) {
                tipBox.className = 'inline-tip-box warning';
                tipBox.innerHTML = `💡 ${evalRes.feedback || `${val} is a valid factor, but dividing by the smallest prime first is recommended.`}`;
                tipBox.style.display = 'block';
              }
            } else {
              btn.classList.add('incorrect');
              if (tipBox) {
                tipBox.className = 'inline-tip-box error';
                tipBox.innerHTML = `✕ ${evalRes.feedback || `${currentNumber} is not divisible by ${val}. Check divisibility rules.`}`;
                tipBox.style.display = 'block';
              }
            }
            if (calcGroup) calcGroup.style.display = 'none';
          }
        };
      });

      const handleCheck = () => {
        const quotVal = quotIn?.value?.trim();
        if (!this.selectedChoice || !quotVal) {
          if (tipBox) {
            tipBox.className = 'inline-tip-box warning';
            tipBox.innerHTML = 'Please enter your calculated quotient.';
            tipBox.style.display = 'block';
          }
          return;
        }

        const result = this.engine.submitInteraction({
          question_id: q.id,
          step_id: stepIdx,
          divisor: this.selectedChoice,
          quotient: Number(quotVal)
        });

        if (result.is_correct) {
          this.audio.success();
          this.completedStepsHistory.push({
            current: currentNumber,
            divisor: this.selectedChoice,
            quotient: Number(quotVal)
          });

          if (stepIdx < steps.length - 1) {
            this.currentStepIndex = stepIdx + 1;
            setTimeout(() => { this.render(); }, 450);
          } else {
            this.isQuestionCompleted = true;
            setTimeout(() => { this.render(); }, 450);
          }
        } else {
          this.audio.error();
          if (tipBox) {
            tipBox.className = 'inline-tip-box error';
            tipBox.innerHTML = `✕ ${result.feedback || `Check calculation: ${currentNumber} ÷ ${this.selectedChoice}.`}`;
            tipBox.style.display = 'block';
          }
          if (quotIn) {
            quotIn.value = '';
            quotIn.focus();
          }
        }
      };

      const btnThinkCheck = document.getElementById('btn-think-check');
      if (btnThinkCheck) btnThinkCheck.onclick = handleCheck;

      if (quotIn) {
        quotIn.onkeydown = (e) => {
          if (e.key === 'Enter') handleCheck();
        };
      }

      const btnHint = document.getElementById('btn-hint');
      if (btnHint) {
        btnHint.onclick = () => {
          this.audio.hint();
          this.requestHint();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // Formula Math Keypad Helper Component
  // ==========================================================================
  renderMathKeypad(inputId) {
    return `
      <div class="math-keypad-container" data-target-input="${inputId}">
        <div class="math-keypad-row">
          <span class="math-keypad-label">Primes:</span>
          <button type="button" class="math-sym-pill prime-pill" data-sym="2">2</button>
          <button type="button" class="math-sym-pill prime-pill" data-sym="3">3</button>
          <button type="button" class="math-sym-pill prime-pill" data-sym="5">5</button>
          <button type="button" class="math-sym-pill prime-pill" data-sym="7">7</button>
          <button type="button" class="math-sym-pill prime-pill" data-sym="11">11</button>
          <button type="button" class="math-sym-pill prime-pill" data-sym="13">13</button>
        </div>
        <div class="math-keypad-row">
          <span class="math-keypad-label">Powers & Ops:</span>
          <button type="button" class="math-sym-pill op-pill" data-sym=" × " title="Multiplication">×</button>
          <button type="button" class="math-sym-pill power-pill" data-sym="²" title="Squared (Power 2)">²</button>
          <button type="button" class="math-sym-pill power-pill" data-sym="³" title="Cubed (Power 3)">³</button>
          <button type="button" class="math-sym-pill power-pill" data-sym="⁴" title="Power 4">⁴</button>
          <button type="button" class="math-sym-pill power-pill" data-sym="⁵" title="Power 5">⁵</button>
          <button type="button" class="math-sym-pill action-pill" data-action="backspace" title="Delete Last Character">⌫</button>
          <button type="button" class="math-sym-pill action-pill" data-action="clear" title="Clear Field">Clear</button>
        </div>
      </div>
    `;
  }

  attachMathKeypadEvents(inputId) {
    const keypad = document.querySelector(`.math-keypad-container[data-target-input="${inputId}"]`);
    const input = document.getElementById(inputId);
    if (!keypad || !input) return;

    keypad.querySelectorAll('.math-sym-pill').forEach(btn => {
      btn.onclick = (e) => {
        e.preventDefault();
        this.audio.click();
        const sym = btn.dataset.sym;
        const action = btn.dataset.action;

        if (action === 'backspace') {
          const start = input.selectionStart !== null ? input.selectionStart : input.value.length;
          const end = input.selectionEnd !== null ? input.selectionEnd : input.value.length;
          if (start === end && start > 0) {
            input.value = input.value.substring(0, start - 1) + input.value.substring(end);
            input.focus();
            input.setSelectionRange(start - 1, start - 1);
          } else if (start !== end) {
            input.value = input.value.substring(0, start) + input.value.substring(end);
            input.focus();
            input.setSelectionRange(start, start);
          }
          return;
        }

        if (action === 'clear') {
          input.value = '';
          input.focus();
          return;
        }

        if (sym) {
          const start = input.selectionStart !== null ? input.selectionStart : input.value.length;
          const end = input.selectionEnd !== null ? input.selectionEnd : input.value.length;
          input.value = input.value.substring(0, start) + sym + input.value.substring(end);
          input.focus();
          const newPos = start + sym.length;
          input.setSelectionRange(newPos, newPos);
        }
      };
    });
  }

  // ==========================================================================
  // Worked Solution & Step Breakdown Helper
  // ==========================================================================
  renderWorkedSolutionAccordion(q) {
    if (!q || !q.solution) return '';
    const sol = q.solution;
    return `
      <div class="worked-solution-card">
        <div class="worked-solution-header">
          <span>📖</span>
          <span>Step-by-Step Worked Solution</span>
        </div>
        ${Array.isArray(sol.steps) && sol.steps.length > 0 ? `
          <div class="solution-ladder-box">
            <div style="font-size: 0.72rem; font-weight: 700; color: var(--text-secondary); text-transform: uppercase; margin-bottom: 0.2rem;">
              Division Chain:
            </div>
            ${sol.steps.map(([curr, div, quot]) => `
              <div class="ladder-step-line">
                <span class="ladder-num">${curr}</span>
                <span class="ladder-op">÷</span>
                <span class="ladder-div">${div}</span>
                <span class="ladder-eq">=</span>
                <span class="ladder-quot">${quot}</span>
              </div>
            `).join('')}
          </div>
        ` : ''}
        ${sol.expanded ? `
          <div class="solution-detail-row">
            <strong>Expanded Form:</strong> <span>${this.formatMathExpression(sol.expanded)}</span>
          </div>
        ` : ''}
        ${sol.exponential ? `
          <div class="solution-detail-row">
            <strong>Exponential Form:</strong> <span style="color: var(--success-text); font-weight: 800;">${this.formatMathExpression(sol.exponential)}</span>
          </div>
        ` : ''}
        ${sol.explanation ? `
          <div class="solution-explanation-text">
            💡 <strong>Rationale:</strong> ${sol.explanation}
          </div>
        ` : ''}
      </div>
    `;
  }

  // ==========================================================================
  // 5. Build (Constructed Solution)
  // ==========================================================================
  renderBuild() {
    if (!this.currentQuestion) {
      this.currentQuestion = this.engine.getNextQuestion();
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
      this.currentHintLevel = 0;
    }
    if (!this.currentQuestion) return { body: '<p>No questions remaining.</p>' };

    const q = this.currentQuestion;
    const promptText = q.question || `Construct the complete solution for ${q.number || ''}:`;
    const steps = Array.isArray(q.steps) ? q.steps : [];
    const stepIdx = Math.min(this.currentStepIndex || 0, Math.max(0, steps.length - 1));
    const activeStep = steps[stepIdx];

    if (this.isQuestionCompleted) {
      const isStageAdvancing = this.engine.getLearningState().student_stage !== 'build';
      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${steps.length > 0 ? this.renderPreviousCompletedSteps(steps, steps.length, this.completedStepsHistory) : ''}
        ${this.renderCompletedSolutionCard(q, false, this.completedStepsHistory)}
      `;

      const actions = `
        <button class="btn-modern btn-modern-primary" id="btn-next-question">
          <span>${isStageAdvancing ? 'Continue to Independent Solving' : 'Next Question'}</span>
          <span>→</span>
        </button>
      `;

      const attachEvents = () => {
        const btnNext = document.getElementById('btn-next-question');
        if (btnNext) {
          btnNext.onclick = () => {
            this.audio.click();
            this.currentQuestion = null;
            this.currentStepIndex = 0;
            this.completedStepsHistory = [];
            this.isQuestionCompleted = false;
            this.lastSubmittedAnswer = null;
            this.currentHintLevel = 0;
            this.render();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // Stepwise Constructed Question
    if (activeStep) {
      const hasOptions = Array.isArray(activeStep.options) && activeStep.options.length > 0;
      const stepFocus = activeStep.focus || activeStep.prompt || `Step ${stepIdx + 1}`;

      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${this.renderPreviousCompletedSteps(steps, stepIdx, this.completedStepsHistory)}

        <div class="step-card-modern">
          <div class="step-card-modern-header">
            <span class="step-num-badge">Step ${stepIdx + 1} of ${steps.length}</span>
            <span class="step-target-value">${stepFocus}</span>
          </div>

          ${hasOptions ? `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">${activeStep.prompt || 'Select the correct step statement:'}</div>
            <div class="options-grid-vertical" id="build-step-options-grid">
              ${activeStep.options.map((opt, oIdx) => `
                <button type="button" class="opt-btn-choice build-step-opt-btn" data-val="${opt}" data-idx="${oIdx}">
                  <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                  <span>${opt}</span>
                </button>
              `).join('')}
            </div>
          ` : `
            <div class="input-label-modern" style="margin-bottom: 0.5rem;">Enter your deduction for ${stepFocus}:</div>
            <input type="text" id="build-step-ans" class="input-field-modern" placeholder="e.g. p² = 3q²" autocomplete="off" style="font-size: 1.08rem; font-family: var(--font-mono);">
            ${this.renderMathKeypad('build-step-ans')}
          `}

          <div id="build-step-feedback" class="inline-tip-box" style="display: none; margin-top: 0.75rem;"></div>
        </div>
      `;

      const actions = `
        ${!hasOptions ? `
          <button class="btn-modern btn-modern-primary" id="btn-build-step-check">
            <span>Check</span>
            <span>✓</span>
          </button>
        ` : ''}
        <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
          <span>← Back to Think</span>
        </button>
        <button class="btn-modern btn-modern-secondary" id="btn-hint">
          <span>💡 Need a Hint?</span>
        </button>
      `;

      const attachEvents = () => {
        const btnBackStage = document.getElementById('btn-back-stage');
        if (btnBackStage) {
          btnBackStage.onclick = () => {
            this.goToStage('think');
          };
        }

        const fbBox = document.getElementById('build-step-feedback');
        const origQ = this.findOriginalQuestion(q.id) || q;
        const currentStepDef = origQ.steps ? origQ.steps[stepIdx] : activeStep;

        if (hasOptions) {
          const optBtns = document.querySelectorAll('.build-step-opt-btn');
          optBtns.forEach(btn => {
            btn.onclick = () => {
              const val = btn.dataset.val;
              const idx = parseInt(btn.dataset.idx, 10);
              this.audio.click();

              const evalRes = this.engine.submitInteraction({
                question_id: q.id,
                step_id: stepIdx,
                selected_index: idx,
                response: val
              });

              if (evalRes.is_correct) {
                this.audio.success();
                optBtns.forEach(b => b.classList.remove('selected', 'incorrect', 'correct'));
                btn.classList.add('correct');
                const bullet = btn.querySelector('.choice-radio-bullet');
                if (bullet) bullet.innerText = '●';

                this.completedStepsHistory.push({
                  stepIdx,
                  step_id: stepIdx,
                  focus: stepFocus,
                  answer: val
                });

                if (stepIdx < steps.length - 1) {
                  this.currentStepIndex = stepIdx + 1;
                  setTimeout(() => { this.render(); }, 450);
                } else {
                  this.isQuestionCompleted = true;
                  setTimeout(() => { this.render(); }, 450);
                }
              } else {
                this.audio.error();
                btn.classList.add('incorrect');
                if (fbBox) {
                  fbBox.className = 'inline-tip-box error';
                  fbBox.innerHTML = `✕ ${evalRes.feedback || activeStep.feedback?.wrong || 'Check your deduction and try again.'}`;
                  fbBox.style.display = 'block';
                }
              }
            };
          });
        } else {
          this.attachMathKeypadEvents('build-step-ans');
          const handleCheck = () => {
            const inputVal = document.getElementById('build-step-ans')?.value?.trim();
            if (!inputVal) return;
            const evalRes = this.engine.submitInteraction({
              question_id: q.id,
              step_id: stepIdx,
              response: inputVal
            });

            if (evalRes.is_correct) {
              this.audio.success();
              this.completedStepsHistory.push({
                stepIdx,
                step_id: stepIdx,
                focus: stepFocus,
                answer: inputVal
              });

              if (stepIdx < steps.length - 1) {
                this.currentStepIndex = stepIdx + 1;
                setTimeout(() => { this.render(); }, 450);
              } else {
                this.isQuestionCompleted = true;
                setTimeout(() => { this.render(); }, 450);
              }
            } else {
              this.audio.error();
              if (fbBox) {
                fbBox.className = 'inline-tip-box error';
                fbBox.innerHTML = `✕ ${evalRes.feedback || 'Check your calculation.'}`;
                fbBox.style.display = 'block';
              }
            }
          };

          const checkBtn = document.getElementById('btn-build-step-check');
          if (checkBtn) checkBtn.onclick = handleCheck;
          const inputElem = document.getElementById('build-step-ans');
          if (inputElem) inputElem.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
        }

        const btnHint = document.getElementById('btn-hint');
        if (btnHint) {
          btnHint.onclick = () => {
            this.audio.hint();
            this.requestHint();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    // Direct single question fallback
    const hasOptions = Array.isArray(q.options) && q.options.length > 0;
    const isFTA = this.topicData.topic?.id === 'cbse10-real-numbers-fta';

    const body = `
      <div class="question-prompt-card">
        <div class="question-prompt-text">${promptText}</div>
      </div>

      <div class="step-card-modern">
        <div class="input-label-modern" style="margin-bottom: 0.5rem;">
          ${hasOptions ? 'Select the correct statement:' : (isFTA ? 'Write the final prime factorisation:' : 'Enter your complete constructed solution:')}
        </div>
        
        ${hasOptions ? `
          <div class="options-grid-vertical" id="build-options-grid">
            ${q.options.map((opt, idx) => `
              <button type="button" class="opt-btn-choice build-opt-btn" data-val="${opt}" data-idx="${idx}">
                <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
        ` : `
          <input type="text" id="build-ans" class="input-field-modern" placeholder="${isFTA ? 'e.g. 2² × 3² × 5' : 'e.g. p² = 3q² or irrational'}" autocomplete="off" style="font-size: 1.08rem; font-family: var(--font-mono);">
          ${isFTA ? this.renderMathKeypad('build-ans') : ''}
        `}
      </div>
    `;

    const actions = `
      <button class="btn-modern btn-modern-primary" id="btn-check">
        <span>Check Answer</span>
        <span>✓</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
        <span>← Back to Think</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-hint">
        <span>💡 Need a Hint?</span>
      </button>
    `;

    const attachEvents = () => {
      const btnBackStage = document.getElementById('btn-back-stage');
      if (btnBackStage) {
        btnBackStage.onclick = () => {
          this.goToStage('think');
        };
      }

      let selectedOption = null;
      let selectedIndex = null;

      if (hasOptions) {
        const optBtns = document.querySelectorAll('.build-opt-btn');
        optBtns.forEach(btn => {
          btn.onclick = () => {
            this.audio.click();
            optBtns.forEach(b => {
              b.classList.remove('selected');
              const bullet = b.querySelector('.choice-radio-bullet');
              if (bullet) bullet.innerText = '○';
            });
            btn.classList.add('selected');
            const bullet = btn.querySelector('.choice-radio-bullet');
            if (bullet) bullet.innerText = '●';
            selectedOption = btn.dataset.val;
            selectedIndex = parseInt(btn.dataset.idx, 10);
          };
        });
      } else {
        this.attachMathKeypadEvents('build-ans');
      }

      const handleCheck = () => {
        const ans = hasOptions ? selectedOption : document.getElementById('build-ans')?.value?.trim();
        if (!ans) {
          this.showFeedback({
            isCorrect: false,
            title: 'Incomplete Input',
            message: hasOptions ? 'Please select an option.' : 'Please enter your constructed factorisation.'
          });
          return;
        }

        const payload = { question_id: q.id, response: ans };
        if (selectedIndex !== null) payload.selected_index = selectedIndex;

        const result = this.engine.submitInteraction(payload);
        if (result.is_correct) {
          this.audio.success();
          this.isQuestionCompleted = true;
          this.lastSubmittedAnswer = ans;
          this.showFeedback({
            isCorrect: true,
            title: 'Correct!',
            message: result.feedback || 'Great job constructing the complete solution.'
          });
          setTimeout(() => {
            this.render();
          }, 550);
        } else {
          this.audio.error();
          this.showFeedback({
            isCorrect: false,
            title: 'Check Your Work',
            message: result.feedback || 'Review your steps and retry.',
            allowRetry: true,
            onRetry: () => {
              this.clearFeedback();
              if (!hasOptions) {
                const input = document.getElementById('build-ans');
                if (input) input.focus();
              }
            }
          });
        }
      };

      const btnCheck = document.getElementById('btn-check');
      if (btnCheck) btnCheck.onclick = handleCheck;

      if (!hasOptions) {
        const input = document.getElementById('build-ans');
        if (input) input.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
      }

      const btnHint = document.getElementById('btn-hint');
      if (btnHint) {
        btnHint.onclick = () => {
          this.audio.hint();
          this.requestHint();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // 6. Solve (Independent Solution)
  // ==========================================================================
  renderSolve() {
    if (!this.currentQuestion) {
      this.currentQuestion = this.engine.getNextQuestion();
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
      this.currentHintLevel = 0;
    }
    if (!this.currentQuestion) return { body: '<p>No questions remaining.</p>' };

    const q = this.currentQuestion;
    const promptText = q.question || `Solve independently: Find the prime factorisation of ${q.number || ''}`;
    const steps = Array.isArray(q.steps) ? q.steps : [];

    if (this.isQuestionCompleted) {
      const isStageAdvancing = this.engine.getLearningState().student_stage !== 'solve';
      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${steps.length > 0 ? this.renderPreviousCompletedSteps(steps, steps.length, this.completedStepsHistory) : ''}
        ${this.renderCompletedSolutionCard(q, false, this.completedStepsHistory)}
      `;

      const actions = `
        <button class="btn-modern btn-modern-primary" id="btn-next-question">
          <span>${isStageAdvancing ? 'Continue to Real-World Applications' : 'Next Question'}</span>
          <span>→</span>
        </button>
      `;

      const attachEvents = () => {
        const btnNext = document.getElementById('btn-next-question');
        if (btnNext) {
          btnNext.onclick = () => {
            this.audio.click();
            this.currentQuestion = null;
            this.currentStepIndex = 0;
            this.completedStepsHistory = [];
            this.isQuestionCompleted = false;
            this.lastSubmittedAnswer = null;
            this.currentHintLevel = 0;
            this.render();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    const hasOptions = Array.isArray(q.options) && q.options.length > 0;

    const body = `
      <div class="question-prompt-card">
        <div class="question-prompt-text">${promptText}</div>
      </div>

      <div class="step-card-modern">
        <div class="input-label-modern" style="margin-bottom: 0.5rem;">
          ${hasOptions ? 'Select the correct statement:' : 'Your final solution:'}
        </div>
        
        ${hasOptions ? `
          <div class="options-grid-vertical" id="solve-options-grid">
            ${q.options.map((opt, idx) => `
              <button type="button" class="opt-btn-choice solve-opt-btn" data-val="${opt}" data-idx="${idx}">
                <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
        ` : `
          <input type="text" id="solve-ans" class="input-field-modern" placeholder="e.g. 2² × 3³ × 7 or 360" autocomplete="off" style="font-size: 1.08rem; font-family: var(--font-mono);">
          ${this.renderMathKeypad('solve-ans')}
        `}
      </div>
    `;

    const actions = `
      <button class="btn-modern btn-modern-primary" id="btn-check">
        <span>Check Solution</span>
        <span>✓</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
        <span>← Back to Build</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-hint">
        <span>💡 Need a Hint?</span>
      </button>
    `;

    const attachEvents = () => {
      const btnBackStage = document.getElementById('btn-back-stage');
      if (btnBackStage) {
        btnBackStage.onclick = () => {
          this.goToStage('build');
        };
      }

      let selectedOption = null;
      let selectedIndex = null;

      if (hasOptions) {
        const optBtns = document.querySelectorAll('.solve-opt-btn');
        optBtns.forEach(btn => {
          btn.onclick = () => {
            this.audio.click();
            optBtns.forEach(b => {
              b.classList.remove('selected');
              const bullet = b.querySelector('.choice-radio-bullet');
              if (bullet) bullet.innerText = '○';
            });
            btn.classList.add('selected');
            const bullet = btn.querySelector('.choice-radio-bullet');
            if (bullet) bullet.innerText = '●';
            selectedOption = btn.dataset.val;
            selectedIndex = parseInt(btn.dataset.idx, 10);
          };
        });
      } else {
        this.attachMathKeypadEvents('solve-ans');
      }

      const handleCheck = () => {
        const ans = hasOptions ? selectedOption : document.getElementById('solve-ans')?.value?.trim();
        if (!ans) {
          this.showFeedback({
            isCorrect: false,
            title: 'Incomplete',
            message: hasOptions ? 'Please select an option.' : 'Please enter your solution.'
          });
          return;
        }

        const payload = { question_id: q.id, response: ans };
        if (selectedIndex !== null) payload.selected_index = selectedIndex;

        const result = this.engine.submitInteraction(payload);
        if (result.is_correct) {
          this.audio.success();
          this.isQuestionCompleted = true;
          this.lastSubmittedAnswer = ans;
          this.showFeedback({
            isCorrect: true,
            title: 'Correct!',
            message: result.feedback || 'Independent mastery successfully demonstrated.'
          });
          setTimeout(() => {
            this.render();
          }, 550);
        } else {
          this.audio.error();
          this.showFeedback({
            isCorrect: false,
            title: 'Check Your Answer',
            message: result.feedback || 'Check your prime factorisation calculation.',
            allowRetry: true,
            onRetry: () => {
              this.clearFeedback();
              if (!hasOptions) {
                const input = document.getElementById('solve-ans');
                if (input) input.focus();
              }
            }
          });
        }
      };

      const btnCheck = document.getElementById('btn-check');
      if (btnCheck) btnCheck.onclick = handleCheck;

      if (!hasOptions) {
        const input = document.getElementById('solve-ans');
        if (input) input.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
      }

      const btnHint = document.getElementById('btn-hint');
      if (btnHint) {
        btnHint.onclick = () => {
          this.audio.hint();
          this.requestHint();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // 7. Apply (Transfer Mastery)
  // ==========================================================================
  renderApply() {
    if (!this.currentQuestion) {
      this.currentQuestion = this.engine.getNextQuestion();
      this.currentStepIndex = 0;
      this.completedStepsHistory = [];
      this.isQuestionCompleted = false;
      this.lastSubmittedAnswer = null;
      this.currentHintLevel = 0;
    }
    if (!this.currentQuestion) return { body: '<p>No questions remaining.</p>' };

    const q = this.currentQuestion;
    const promptText = q.question || `Apply your knowledge: Factorise ${q.number || ''}`;
    const steps = Array.isArray(q.steps) ? q.steps : [];

    if (this.isQuestionCompleted) {
      const isMasteryReached = this.engine.getLearningState().student_stage === 'master' || this.engine.getLearningState().current_stage === 'mastery_gate';
      const body = `
        <div class="question-prompt-card">
          <div class="question-prompt-text">${promptText}</div>
        </div>

        ${steps.length > 0 ? this.renderPreviousCompletedSteps(steps, steps.length, this.completedStepsHistory) : ''}
        ${this.renderCompletedSolutionCard(q, false, this.completedStepsHistory)}
      `;

      const actions = `
        <button class="btn-modern btn-modern-primary" id="btn-next-question">
          <span>${isMasteryReached ? 'Claim Topic Mastery' : 'Next Application'}</span>
          <span>${isMasteryReached ? '🏆' : '→'}</span>
        </button>
      `;

      const attachEvents = () => {
        const btnNext = document.getElementById('btn-next-question');
        if (btnNext) {
          btnNext.onclick = () => {
            this.audio.click();
            this.currentQuestion = null;
            this.currentStepIndex = 0;
            this.completedStepsHistory = [];
            this.isQuestionCompleted = false;
            this.lastSubmittedAnswer = null;
            this.currentHintLevel = 0;
            this.render();
          };
        }
      };

      return { body, actions, attachEvents };
    }

    const hasOptions = Array.isArray(q.options) && q.options.length > 0;

    const body = `
      <div class="question-prompt-card">
        <div class="question-prompt-text">${promptText}</div>
      </div>

      <div class="step-card-modern">
        <div class="input-label-modern" style="margin-bottom: 0.5rem;">Your response:</div>
        
        ${hasOptions ? `
          <div class="options-grid-vertical" id="apply-options-grid">
            ${q.options.map((opt, idx) => `
              <button type="button" class="opt-btn-choice apply-opt-btn" data-val="${opt}" data-idx="${idx}">
                <span class="choice-radio-bullet" style="color: var(--brand-primary); font-weight: 800; font-size: 1.1rem; margin-right: 0.35rem;">○</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
        ` : `
          <input type="text" id="apply-ans" class="input-field-modern" placeholder="Enter your response" autocomplete="off" style="font-size: 1.08rem;">
          ${this.renderMathKeypad('apply-ans')}
        `}
      </div>
    `;

    const actions = `
      <button class="btn-modern btn-modern-primary" id="btn-check">
        <span>Submit Answer</span>
        <span>✓</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-back-stage">
        <span>← Back to Solve</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-hint">
        <span>💡 Need a Hint?</span>
      </button>
    `;

    const attachEvents = () => {
      const btnBackStage = document.getElementById('btn-back-stage');
      if (btnBackStage) {
        btnBackStage.onclick = () => {
          this.goToStage('solve');
        };
      }

      let selectedOption = null;
      let selectedIndex = null;

      if (hasOptions) {
        const optBtns = document.querySelectorAll('.apply-opt-btn');
        optBtns.forEach(btn => {
          btn.onclick = () => {
            this.audio.click();
            optBtns.forEach(b => {
              b.classList.remove('selected');
              const bullet = b.querySelector('.choice-radio-bullet');
              if (bullet) bullet.innerText = '○';
            });
            btn.classList.add('selected');
            const bullet = btn.querySelector('.choice-radio-bullet');
            if (bullet) bullet.innerText = '●';
            selectedOption = btn.dataset.val;
            selectedIndex = parseInt(btn.dataset.idx, 10);
          };
        });
      } else {
        this.attachMathKeypadEvents('apply-ans');
      }

      const handleCheck = () => {
        let ans = hasOptions ? selectedOption : document.getElementById('apply-ans')?.value?.trim();
        if (!ans) {
          this.showFeedback({
            isCorrect: false,
            title: 'Incomplete',
            message: hasOptions ? 'Please select an option.' : 'Please enter your response.'
          });
          return;
        }

        const payload = { question_id: q.id, response: ans };
        if (selectedIndex !== null) payload.selected_index = selectedIndex;

        const result = this.engine.submitInteraction(payload);
        if (result.is_correct) {
          this.audio.success();
          this.isQuestionCompleted = true;
          this.lastSubmittedAnswer = ans;
          this.showFeedback({
            isCorrect: true,
            title: 'Correct Application!',
            message: result.feedback || 'Transfer concept mastered successfully.'
          });
          setTimeout(() => {
            this.render();
          }, 600);
        } else {
          this.audio.error();
          this.showFeedback({
            isCorrect: false,
            title: 'Check Reasoning',
            message: result.feedback || 'Review your reasoning and calculation.',
            allowRetry: true,
            onRetry: () => {
              this.clearFeedback();
              if (!hasOptions) {
                const input = document.getElementById('apply-ans');
                if (input) input.focus();
              }
            }
          });
        }
      };

      const btnCheck = document.getElementById('btn-check');
      if (btnCheck) btnCheck.onclick = handleCheck;

      if (!hasOptions) {
        const input = document.getElementById('apply-ans');
        if (input) input.onkeydown = (e) => { if (e.key === 'Enter') handleCheck(); };
      }

      const btnHint = document.getElementById('btn-hint');
      if (btnHint) {
        btnHint.onclick = () => {
          this.audio.hint();
          this.requestHint();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // 8. Master (Topic Completion & Mastery Celebration)
  // ==========================================================================
  renderMaster() {
    const topicTitle = this.topicData.topic?.title || 'Concept';
    const currentTopicId = this.topicData.topic?.id || '';
    const isFTA = currentTopicId === 'cbse10-real-numbers-fta' || currentTopicId === 'fta';
    const nextTopic = isFTA ? {
      id: 'cbse10-real-numbers-hcf-lcm',
      title: 'HCF & LCM Using Prime Factorisation',
      description: 'Apply your prime factorisation foundation to find Highest Common Factor (HCF) and Least Common Multiple (LCM) with minimum and maximum exponent rules.'
    } : null;

    let skillsList = [];
    if (Array.isArray(this.topicData.skills)) {
      skillsList = this.topicData.skills;
    } else if (this.topicData.skills && typeof this.topicData.skills === 'object') {
      skillsList = Object.entries(this.topicData.skills).map(([k, v]) => ({
        id: k,
        title: v.title || v.name || v.description || k
      }));
    } else {
      skillsList = [
        { title: 'Prime Factorisation Mechanics' },
        { title: 'Divisibility Rule Selection' },
        { title: 'Expanded & Exponential Notation' },
        { title: 'Uniqueness Reasoning & Verification' }
      ];
    }

    const body = `
      <div class="mastery-celebration-wrapper">
        <div class="celebration-shield-badge">🏆</div>
        <h2 class="mastery-headline">${topicTitle} Mastered!</h2>
        <p style="color: var(--text-secondary); max-width: 520px; text-align: center; font-size: 1.05rem;">
          Outstanding effort! You have successfully mastered all core principles, step-by-step algorithms, and transfer problems for this topic.
        </p>

        <div class="mastery-skills-card">
          <div class="skills-list-title">Verified Competencies:</div>
          <ul class="skills-list-container">
            ${skillsList.map(sk => `
              <li>
                <div class="chk">✓</div>
                <span><strong>${sk.title || sk.id}</strong></span>
              </li>
            `).join('')}
          </ul>
        </div>

        ${nextTopic ? `
          <div class="next-topic-banner-card">
            <div class="next-topic-tag">Recommended Next Topic</div>
            <div class="next-topic-title">${nextTopic.title}</div>
            <div class="next-topic-desc">${nextTopic.description}</div>
            <button type="button" class="btn-modern btn-modern-primary btn-next-topic" id="btn-banner-next-topic">
              <span>Start Next Topic</span>
              <span>→</span>
            </button>
          </div>
        ` : ''}
      </div>
    `;

    const actions = `
      ${nextTopic ? `
        <button class="btn-modern btn-modern-primary" id="btn-next-topic-action">
          <span>Start HCF & LCM Topic</span>
          <span>→</span>
        </button>
      ` : ''}
      <button class="btn-modern btn-modern-secondary" id="btn-goto-retain">
        <span>Practice Retention ⚡</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-reset">
        <span>Reset & Practice Again ↺</span>
      </button>
    `;

    const attachEvents = () => {
      const handleNextTopic = () => {
        this.audio.click();
        if (typeof window !== 'undefined') {
          const newUrl = new URL(window.location.href);
          newUrl.searchParams.set('topic', 'cbse10-real-numbers-hcf-lcm');
          window.location.href = newUrl.toString();
        }
      };

      const btnBanner = document.getElementById('btn-banner-next-topic');
      if (btnBanner) btnBanner.onclick = handleNextTopic;

      const btnNextAction = document.getElementById('btn-next-topic-action');
      if (btnNextAction) btnNextAction.onclick = handleNextTopic;

      const btnRetain = document.getElementById('btn-goto-retain');
      if (btnRetain) {
        btnRetain.onclick = () => {
          this.audio.click();
          this.engine.setStage('delayed_retrieval');
          this.render();
        };
      }

      const btnReset = document.getElementById('btn-reset');
      if (btnReset) {
        btnReset.onclick = () => {
          this.resetSession();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // 9. Retain (Retention Quick Check)
  // ==========================================================================
  renderRetain() {
    const topicTitle = this.topicData.topic?.title || 'Concept';
    const currentTopicId = this.topicData.topic?.id || '';
    const isFTA = currentTopicId === 'cbse10-real-numbers-fta' || currentTopicId === 'fta';

    const body = `
      <div class="concept-hero-card" style="border-color: rgba(16, 185, 129, 0.4);">
        <div class="concept-hero-tag" style="color: #34d399;">
          <span>⚡</span>
          <span>Retention Active</span>
        </div>
        <p class="concept-hero-text">You have mastered <strong>${topicTitle}</strong>. Periodic quick recall helps cement strong long-term memory retrieval.</p>
      </div>

      ${isFTA ? `
        <div class="next-topic-banner-card" style="margin-top: 1.25rem;">
          <div class="next-topic-tag">Ready to Move Forward?</div>
          <div class="next-topic-title">HCF & LCM Using Prime Factorisation</div>
          <div class="next-topic-desc">Advance to the next chapter topic to discover how HCF and LCM are solved with the Fundamental Theorem of Arithmetic.</div>
          <button type="button" class="btn-modern btn-modern-primary btn-next-topic" id="btn-retain-next-topic">
            <span>Continue to HCF & LCM</span>
            <span>→</span>
          </button>
        </div>
      ` : ''}
    `;

    const actions = `
      ${isFTA ? `
        <button class="btn-modern btn-modern-primary" id="btn-retain-next-topic-action">
          <span>Go to HCF & LCM Topic</span>
          <span>→</span>
        </button>
      ` : ''}
      <button class="btn-modern btn-modern-secondary" id="btn-quick-solve">
        <span>Start Quick Recall Practice</span>
        <span>→</span>
      </button>
      <button class="btn-modern btn-modern-secondary" id="btn-reset">
        <span>Start Over ↺</span>
      </button>
    `;

    const attachEvents = () => {
      const handleNextTopic = () => {
        this.audio.click();
        if (typeof window !== 'undefined') {
          const newUrl = new URL(window.location.href);
          newUrl.searchParams.set('topic', 'cbse10-real-numbers-hcf-lcm');
          window.location.href = newUrl.toString();
        }
      };

      const btnRetainNext = document.getElementById('btn-retain-next-topic');
      if (btnRetainNext) btnRetainNext.onclick = handleNextTopic;

      const btnRetainNextAction = document.getElementById('btn-retain-next-topic-action');
      if (btnRetainNextAction) btnRetainNextAction.onclick = handleNextTopic;

      const btnSolve = document.getElementById('btn-quick-solve');
      if (btnSolve) {
        btnSolve.onclick = () => {
          this.audio.click();
          this.engine.submitInteraction({ question_id: 'ret_01', is_correct: true, stage: 'delayed_retrieval' });
          this.render();
        };
      }
      const btnReset = document.getElementById('btn-reset');
      if (btnReset) {
        btnReset.onclick = () => {
          this.resetSession();
        };
      }
    };

    return { body, actions, attachEvents };
  }

  // ==========================================================================
  // Feedback & Coaching Helpers
  // ==========================================================================
  clearFeedback() {
    if (typeof document === 'undefined') return;
    const fbContainer = document.getElementById('feedback-container');
    if (fbContainer) fbContainer.innerHTML = '';
  }

  showFeedback(options, isCorrectLegacy) {
    const container = document.getElementById('feedback-container');
    if (!container) return;

    if (typeof options === 'string') {
      const isCorrect = isCorrectLegacy !== undefined ? isCorrectLegacy : true;
      container.innerHTML = `
        <div class="feedback-card-modern ${isCorrect ? 'correct' : 'incorrect'}">
          <div class="feedback-header-row">
            <span>${isCorrect ? '✓' : '✕'}</span>
            <span>${isCorrect ? 'Correct' : 'Incorrect'}</span>
          </div>
          <div class="feedback-body-msg">${options}</div>
        </div>
      `;
      return;
    }

    const { isCorrect, title, message, hint, allowRetry, onRetry } = options || {};
    const icon = isCorrect ? '✓' : '✕';
    const headerTitle = title || (isCorrect ? 'Good Choice' : 'Check Your Step');

    container.innerHTML = `
      <div class="feedback-card-modern ${isCorrect ? 'correct' : 'incorrect'}">
        <div class="feedback-header-row">
          <span>${icon}</span>
          <span>${headerTitle}</span>
        </div>
        <div class="feedback-body-msg">${message || ''}</div>
        ${hint ? `
          <div class="feedback-hint-nested">
            <div class="feedback-hint-title">💡 Divisibility Hint</div>
            <div class="feedback-hint-text">${hint}</div>
          </div>
        ` : ''}
        ${allowRetry ? `
          <div class="feedback-actions-bar">
            <button class="btn-modern btn-modern-secondary" id="btn-feedback-retry" style="padding: 0.5rem 1rem; font-size: 0.85rem;">
              <span>Try Again</span>
              <span>↺</span>
            </button>
          </div>
        ` : ''}
      </div>
    `;

    if (allowRetry && onRetry) {
      const retryBtn = document.getElementById('btn-feedback-retry');
      if (retryBtn) {
        retryBtn.onclick = () => {
          this.audio.click();
          onRetry();
        };
      }
    }

    this.typeset();
  }

  showRemediation(remediation) {
    const container = document.getElementById('remediation-container');
    if (!container) return;
    container.innerHTML = `
      <div class="remediation-card-modern">
        <div class="remediation-title-row">
          <span>🎓</span>
          <span>Coach Recap: ${remediation.skill_title || 'Divisibility Rule Review'}</span>
        </div>
        <div class="remediation-text">
          ${remediation.concept_recap || remediation.guidance || 'Review the core divisibility principles before continuing.'}
        </div>
      </div>
    `;
  }

  requestHint() {
    if (!this.currentQuestion) return;
    this.currentHintLevel = Math.min((this.currentHintLevel || 0) + 1, 3);
    const res = this.engine.requestHint({
      question_id: this.currentQuestion.id,
      hint_level: this.currentHintLevel
    });
    const btnHint = document.getElementById('btn-hint');
    if (res && res.hint_text) {
      const container = document.getElementById('hint-container');
      if (container) {
        container.innerHTML = `
          <div class="hint-accordion-card">
            <div class="hint-badge-tier">💡 Hint Level ${this.currentHintLevel} of 3</div>
            <div class="hint-content-text">${res.hint_text}</div>
          </div>
        `;
        this.typeset();
      }
      if (btnHint) {
        if (this.currentHintLevel >= 3) {
          btnHint.innerText = '💡 Final Hint Displayed';
          btnHint.disabled = true;
        } else {
          btnHint.innerText = `💡 Show Another Hint (${this.currentHintLevel}/3)`;
        }
      }
    }
  }

  // ==========================================================================
  // Loading & Error States
  // ==========================================================================
  renderLoading() {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="app-shell" style="align-items: center; justify-content: center; min-height: 60vh;">
        <div class="stage-eyebrow" style="margin-bottom: 1rem;">Loading Mastery Session</div>
        <div style="font-family: var(--font-display); font-size: 1.5rem; font-weight: 800; color: #fff;">
          Preparing interactive curriculum...
        </div>
      </div>
    `;
  }

  renderError(errMsg) {
    if (!this.container) return;
    this.container.innerHTML = `
      <div class="app-shell" style="align-items: center; justify-content: center; min-height: 60vh;">
        <main class="workspace-card" style="text-align: center; max-width: 520px; width: 100%;">
          <div style="font-size: 2.75rem; margin-bottom: 0.75rem;">⚠️</div>
          <h2 style="font-family: var(--font-display); font-size: 1.4rem; font-weight: 800; margin-bottom: 0.5rem; color: #fff;">Unable to load learning topic</h2>
          <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.5;">${errMsg}</p>
          <div style="display: flex; gap: 0.75rem; justify-content: center;">
            <button class="btn-modern btn-modern-primary" onclick="window.location.reload()">Try Again ↺</button>
            <a href="/" class="btn-modern btn-modern-secondary">Back to Home</a>
          </div>
        </main>
      </div>
    `;
  }
}
