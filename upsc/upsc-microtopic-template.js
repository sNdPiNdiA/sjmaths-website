const STYLES_CSS = `<style>
    :root {
        --up-primary: #0f172a;
        --up-primary-light: #1e293b;
        --up-accent: #3b82f6;
        --up-accent-purple: #8b5cf6;
        --up-accent-gold: #d4af37;
        --up-surface: rgba(255, 255, 255, 0.85);
        --up-shadow-xl: 0 20px 50px rgba(0, 0, 0, 0.08);
        --up-shadow-lg: 0 10px 30px rgba(0, 0, 0, 0.06);
        --up-radius-xl: 24px;
        --up-radius-lg: 16px;
        --up-transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        --up-font-heading: 'Outfit', 'Inter', system-ui, -apple-system, sans-serif;
        --up-font-body: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    /* Bilingual Language Toggling */
    html.lang-en .lang-hi,
    body.lang-en .lang-hi,
    html:not(.lang-hi) .lang-hi,
    body:not(.lang-hi):not(.lang-en) .lang-hi {
        display: none !important;
    }

    html.lang-hi .lang-en,
    body.lang-hi .lang-en {
        display: none !important;
    }

    /* Test solutions are hidden by default and only shown when triggered by Check Answer */
    .test-question-card .sol-box {
        display: none !important;
    }
    .test-question-card:has(.opt-radio:checked) .sol-box {
        display: none !important;
    }

    /* Dark Mode Contrast & Styling */
    body.dark-mode {
        background-color: #0b0f19 !important;
        color: #f1f5f9 !important;
    }

    body.dark-mode .topic-header,
    body.dark-mode .card-premium,
    body.dark-mode .practice-question-card,
    body.dark-mode .mains-question-card,
    body.dark-mode .revision-card,
    body.dark-mode .related-topics-card,
    body.dark-mode .table-container,
    body.dark-mode table,
    body.dark-mode .timeline-item,
    body.dark-mode .subcard,
    body.dark-mode .upsc-note {
        background-color: #1e293b !important;
        color: #f1f5f9 !important;
        border-color: #334155 !important;
    }

    body.dark-mode .topic-header h1 {
        background: linear-gradient(135deg, #f1f5f9 0%, #60a5fa 50%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    body.dark-mode p,
    body.dark-mode li,
    body.dark-mode span,
    body.dark-mode h1,
    body.dark-mode h2,
    body.dark-mode h3,
    body.dark-mode h4,
    body.dark-mode h5,
    body.dark-mode strong,
    body.dark-mode .q-text-sm,
    body.dark-mode .topic-desc,
    body.dark-mode .syllabus-text,
    body.dark-mode label,
    body.dark-mode .note-content {
        color: #f8fafc !important;
    }

    body.dark-mode .study-tabs {
        background: rgba(30, 41, 59, 0.9) !important;
        border-color: #334155 !important;
    }

    body.dark-mode .tab-btn {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #94a3b8 !important;
    }

    body.dark-mode .tab-btn.active {
        background: linear-gradient(135deg, var(--up-accent), var(--up-accent-purple)) !important;
        color: #ffffff !important;
    }

    body.dark-mode .tab-btn:hover {
        background: rgba(59, 130, 246, 0.2) !important;
        color: #f1f5f9 !important;
    }

    body.dark-mode .topic-content th {
        background: #0f172a !important;
        color: #f8fafc !important;
        border-color: #334155 !important;
    }

    body.dark-mode .topic-content td {
        background: #1e293b !important;
        color: #f8fafc !important;
        border-color: #334155 !important;
    }

    body.dark-mode .breadcrumbs {
        background: rgba(30, 41, 59, 0.8) !important;
        color: #94a3b8 !important;
        border-color: #334155 !important;
    }

    body.dark-mode .related-topic-link {
        background: rgba(255, 255, 255, 0.04) !important;
        color: #f8fafc !important;
        border-color: #334155 !important;
    }

    body.dark-mode .related-topic-link:hover {
        background: rgba(59, 130, 246, 0.2) !important;
        color: #ffffff !important;
    }

    body.dark-mode .sol-box {
        background: rgba(59, 130, 246, 0.15) !important;
        color: #f1f5f9 !important;
        border-color: rgba(59, 130, 246, 0.3) !important;
    }

    body.dark-mode .practice-option-box {
        background: rgba(255, 255, 255, 0.04) !important;
        border-color: #334155 !important;
        color: #f8fafc !important;
    }

    body.dark-mode .practice-option-box:hover {
        background: rgba(59, 130, 246, 0.2) !important;
    }

    /* Mobile-First UI/UX & Text Highlighting Enhancements */
    @media (max-width: 768px) {
        .topic-container {
            padding: 0 1rem 2rem;
            margin: 1rem auto;
        }

        .topic-header {
            padding: 1.5rem 1rem;
            border-radius: 16px;
        }

        .study-tabs {
            flex-wrap: nowrap;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            padding: 0.4rem;
            scrollbar-width: none;
            justify-content: flex-start;
        }

        .study-tabs::-webkit-scrollbar {
            display: none;
        }

        .tab-btn {
            font-size: 0.85rem;
            padding: 0.5rem 0.9rem;
        }
    }

    /* Highlight & Accent Styles for Student Comfort */
    strong {
        color: var(--up-accent);
        font-weight: 700;
    }

    .keyword-tag {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
        color: var(--up-accent);
        border: 1px solid rgba(59, 130, 246, 0.2);
        padding: 0.3rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin: 0.2rem;
    }

    body.dark-mode .keyword-tag {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(139, 92, 246, 0.2));
        color: #60a5fa;
        border-color: rgba(59, 130, 246, 0.3);
    }

    .topic-container {
        max-width: 1150px;
        margin: 2rem auto;
        padding: 0 1.5rem 3rem;
        animation: upFadeIn 0.6s ease-out;
    }

    /* Breadcrumbs */
    .breadcrumbs {
        margin-bottom: 1.5rem;
        font-size: 0.88rem;
        color: #64748b;
        background: rgba(255, 255, 255, 0.6);
        display: inline-block;
        padding: 0.6rem 1.2rem;
        border-radius: 999px;
        border: 1px solid rgba(0, 0, 0, 0.04);
        backdrop-filter: blur(8px);
    }

    .breadcrumbs a {
        color: var(--up-accent);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }

    .breadcrumbs a:hover {
        color: var(--up-accent-purple);
        text-decoration: underline;
    }

    .breadcrumbs i {
        margin: 0 0.5rem;
        font-size: 0.7rem;
        color: #94a3b8;
    }

    .breadcrumbs-path {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.2rem;
    }

    /* Topic Header - Premium Hero */
    .topic-header {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.03), rgba(139, 92, 246, 0.03), rgba(212, 175, 55, 0.03));
        border: 1px solid rgba(59, 130, 246, 0.08);
        border-radius: var(--up-radius-xl);
        padding: 2.5rem 2.5rem;
        margin-bottom: 1.75rem;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
        text-align: center;
    }

    .topic-header::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -15%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.06) 0%, transparent 70%);
        pointer-events: none;
    }

    .topic-header::after {
        content: '';
        position: absolute;
        bottom: -40%;
        left: -10%;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.05) 0%, transparent 70%);
        pointer-events: none;
    }

    .topic-header h1 {
        font-family: var(--up-font-heading);
        font-size: clamp(2rem, 5vw, 2.75rem);
        font-weight: 800;
        background: linear-gradient(135deg, var(--up-primary) 0%, var(--up-accent) 50%, var(--up-accent-purple) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.75rem;
        line-height: 1.2;
        position: relative;
        letter-spacing: -0.02em;
    }

    .topic-desc {
        color: #475569;
        font-size: clamp(0.95rem, 2vw, 1.05rem);
        line-height: 1.7;
        max-width: 780px;
        margin: 0 auto;
        position: relative;
    }

    /* Meta Bar */
    .topic-meta-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        justify-content: center;
        align-items: center;
        margin-top: 1.5rem;
        padding-top: 1.25rem;
        border-top: 1px solid rgba(0, 0, 0, 0.05);
        position: relative;
    }

    .topic-difficulty {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        font-family: var(--up-font-heading);
    }

    .difficulty-medium {
        background: rgba(245, 158, 11, 0.1);
        color: #b45309;
        border: 1px solid rgba(245, 158, 11, 0.2);
    }

    .difficulty-easy {
        background: rgba(16, 185, 129, 0.1);
        color: #047857;
        border: 1px solid rgba(16, 185, 129, 0.2);
    }

    .difficulty-hard {
        background: rgba(239, 68, 68, 0.1);
        color: #b91c1c;
        border: 1px solid rgba(239, 68, 68, 0.2);
    }

    .topic-study-time {
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #475569;
        background: rgba(100, 116, 139, 0.06);
        border: 1px solid rgba(100, 116, 139, 0.12);
        font-family: var(--up-font-heading);
    }

    /* Language Toggle */
    .lang-toggle {
        display: inline-flex;
        background: rgba(59, 130, 246, 0.06);
        border: 1px solid rgba(59, 130, 246, 0.12);
        border-radius: 999px;
        padding: 0.2rem;
        gap: 0.2rem;
    }

    .lang-toggle button {
        border: none;
        background: transparent;
        color: #64748b;
        font-weight: 600;
        padding: 0.35rem 0.85rem;
        border-radius: 999px;
        cursor: pointer;
        font-size: 0.8rem;
        transition: all 0.2s ease;
    }

    .lang-toggle button.active {
        background: #ffffff;
        color: var(--up-accent);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    /* Sticky Tab Navigation */
    .study-tabs {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        padding: 0.55rem;
        background: var(--up-surface);
        border: 1px solid rgba(0, 0, 0, 0.05);
        border-radius: var(--up-radius-lg);
        margin-bottom: 2rem;
        position: sticky;
        top: 88px;
        z-index: 100;
        backdrop-filter: blur(16px);
        box-shadow: var(--up-shadow-lg);
        justify-content: center;
    }

    .tab-btn {
        border: none;
        background: transparent;
        color: #475569;
        padding: 0.65rem 1.1rem;
        border-radius: 999px;
        cursor: pointer;
        font-weight: 600;
        font-size: 0.9rem;
        font-family: var(--up-font-heading);
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: var(--up-transition);
        white-space: nowrap;
    }

    .tab-btn:hover {
        background: rgba(59, 130, 246, 0.08);
        color: var(--up-accent);
    }

    .tab-btn.active {
        background: linear-gradient(135deg, var(--up-accent), var(--up-accent-purple));
        color: #ffffff;
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.25);
    }

    .tab-btn i {
        font-size: 0.95rem;
    }
</style>`;

/* ============================================================================
 * UPSC MICROTOPIC GENERATOR — MASTER TEMPLATE (v5)
 * ============================================================================
 *
 * v5 adds operations/infrastructure improvements:
 *
 * 1. METADATA VALIDATOR — validates all metadata fields BEFORE Gemini runs.
 *    Prevents bad inputs from producing bad pages.
 *
 * 2. REAL SHA-256 CONTENT HASH — for reliable cache invalidation and
 *    duplicate detection across all generated files.
 *
 * 3. TAB-LEVEL CACHING — stores each tab as separate JSON file.
 *    Only regenerates changed tabs. Dramatically reduces API usage.
 *
 * 4. SMART RETRY — regenerates only the failed dimensions with focused
 *    prompts instead of rebuilding the entire tab. Reduces cost.
 *
 * 5. GENERATION MANIFEST — page.manifest.json tracks every tab's hash,
 *    score, and version. Enables selective regeneration.
 *
 * 6. SUBJECT-LEVEL CONFIG — subjects/ directory with subject-specific
 *    defaults (supportsTimeline, supportsMaps, defaultPracticeTypes, etc.)
 *
 * 7. PIPELINE LOGGING — structured logs with generation ID, timing,
 *    tokens, cost, retries, validator results, scores.
 *
 * 8. GEMINI API CLIENT — built-in retry logic, rate limiting, error handling.
 *
 * 9. GENERATION PIPELINE — orchestrates the full flow with caching, smart retry,
 *    manifest creation, and logging.
 *
 * Reference: generate-ssc-cgl-geography-html.js (SSC CGL 4-tab pattern)
 * ============================================================================
 */

// ============================================================================
// VERSION CONSTANTS
// ============================================================================
const VERSION = {
  generator: 'v5',
  prompt: '4.0',
  translator: '2.0',
  normalizer: '1.0',
  scorer: '1.5',
  manifest: '1.0',
};

// ============================================================================
// 6. SUBJECT-LEVEL CONFIGURATION
// ============================================================================
const SUBJECT_CONFIGS = {
  'ancient-history': {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'match'],
  },
  'medieval-history': {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'match'],
  },
  'modern-history': {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'assertion', 'advanced'],
  },
  'polity': {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'assertion', 'advanced'],
  },
  'geography': {
    supportsTimeline: false,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'match'],
  },
  'economy': {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'advanced'],
  },
  'environment': {
    supportsTimeline: false,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'match'],
  },
  'science-and-tech': {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: false,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement'],
  },
  'art-and-culture': {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'match'],
  },
  'social-issues': {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'advanced'],
  },
  'ethics': {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ['conceptual', 'statement', 'advanced'],
  },
  'csat': {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: false,
    defaultPracticeTypes: ['basic', 'conceptual', 'advanced'],
  },
};

function getSubjectConfig(subjectDir) {
  return SUBJECT_CONFIGS[subjectDir] || {
    supportsTimeline: true,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ['basic', 'conceptual', 'statement', 'assertion', 'match', 'advanced'],
  };
}

// ============================================================================
// 1. METADATA VALIDATOR — Validates ALL metadata BEFORE Gemini runs
// ============================================================================
/**
 * Validates topic metadata before any API calls are made.
 * Prevents bad inputs from producing bad pages.
 * 
 * @param {TopicMetadata} meta - The topic metadata to validate
 * @returns {{ passed: boolean, errors: string[], warnings: string[] }}
 */
function validateMetadata(meta) {
  const errors = [];
  const warnings = [];

  if (!meta) {
    errors.push('Metadata is null/undefined');
    return { passed: false, errors, warnings };
  }

  // Required fields
  const required = ['name', 'hindiName', 'dir', 'subject', 'subjectDir', 'canonicalUrl', 'description', 'topicId'];
  for (const field of required) {
    if (!meta[field]) {
      errors.push(`Missing required field: ${field} `);
    }
  }

  // Name validations
  if (meta.name && meta.name.length < 3) {
    errors.push(`Name too short: "${meta.name}"(min 3 chars)`);
  }
  if (meta.name && meta.name.length > 100) {
    errors.push(`Name too long: "${meta.name}"(max 100 chars)`);
  }

  // Hindi name
  if (meta.hindiName && meta.hindiName.length < 3) {
    warnings.push(`hindiName seems too short: "${meta.hindiName}"`);
  }

  // SEO description (50-160 chars for Google)
  if (meta.description) {
    if (meta.description.length < 50) {
      warnings.push(`SEO description too short(${meta.description.length} chars, min 50)`);
    }
    if (meta.description.length > 160) {
      warnings.push(`SEO description too long(${meta.description.length} chars, max 160)`);
    }
  }

  // Canonical URL
  if (meta.canonicalUrl) {
    if (!meta.canonicalUrl.startsWith('https://sjmaths.com/')) {
      warnings.push(`canonicalUrl should start with https://sjmaths.com/: ${meta.canonicalUrl}`);
    }
    if (!meta.canonicalUrl.endsWith('/')) {
      warnings.push(`canonicalUrl should end with /: ${meta.canonicalUrl}`);
    }
  }

  // Topic ID format
  if (meta.topicId && !/^[a-z0-9.-]+$/.test(meta.topicId)) {
    warnings.push(`topicId should be lowercase alphanumeric with dots/hyphens: ${meta.topicId}`);
  }

  // Previous/next topic consistency
  if (meta.previousTopic && !meta.previousDir) {
    warnings.push('previousTopic exists but previousDir is missing');
  }
  if (meta.nextTopic && !meta.nextDir) {
    warnings.push('nextTopic exists but nextDir is missing');
  }

  // Scope validations
  if (meta.scope) {
    if (!meta.scope.mustExplain || meta.scope.mustExplain.length === 0) {
      warnings.push('scope.mustExplain is empty — add at least one concept');
    }
    if (!meta.scope.neverExplain || meta.scope.neverExplain.length === 0) {
      warnings.push('scope.neverExplain is empty — add at least one forbidden topic');
    }
    if (!meta.scope.keywords || meta.scope.keywords.length < 3) {
      warnings.push('scope.keywords has fewer than 3 entries');
    }
  } else {
    warnings.push('scope is missing — strongly recommended for content boundary enforcement');
  }

  // Difficulty
  const validDifficulties = ['easy', 'medium', 'hard'];
  if (meta.difficulty && !validDifficulties.includes(meta.difficulty)) {
    errors.push(`Invalid difficulty: "${meta.difficulty}". Must be one of: ${validDifficulties.join(', ')}`);
  }

  // Study time
  if (meta.studyTime) {
    if (typeof meta.studyTime.concepts !== 'number' || meta.studyTime.concepts < 1) {
      warnings.push('studyTime.concepts should be a positive number');
    }
    if (typeof meta.studyTime.practice !== 'number' || meta.studyTime.practice < 1) {
      warnings.push('studyTime.practice should be a positive number');
    }
  }

  // Practice types
  const validTypes = ['basic', 'conceptual', 'statement', 'assertion', 'match', 'advanced'];
  if (meta.practiceTypes) {
    for (const type of meta.practiceTypes) {
      if (!validTypes.includes(type)) {
        warnings.push(`Invalid practiceType: "${type}". Valid: ${validTypes.join(', ')}`);
      }
    }
  }

  // Learning objectives
  if (meta.learningObjectives && meta.learningObjectives.length < 2) {
    warnings.push('learningObjectives should have at least 2 entries');
  }

  // Subject directory
  if (meta.subjectDir && !SUBJECT_CONFIGS[meta.subjectDir]) {
    warnings.push(`Unknown subjectDir: "${meta.subjectDir}". Add config to SUBJECT_CONFIGS or expect defaults`);
  }

  return {
    passed: errors.length === 0,
    errors,
    warnings,
  };
}

// ============================================================================
// TOPIC METADATA — Passed in for each microtopic
// ============================================================================
/**
 * @typedef {Object} TopicMetadata
 * @property {string} name           - "Paleolithic Age"
 * @property {string} hindiName      - "पुरापाषाण काल"
 * @property {string} dir            - "paleolithic-age"
 * @property {string} subject        - "Ancient History"
 * @property {string} subjectDir     - "ancient-history"
 * @property {string} parentTopic    - "Prehistory"
 * @property {string} parentDir      - "Prehistory"
 * @property {string} previousTopic  - "Prehistoric Time Periods"
 * @property {string} previousDir    - "prehistoric-time-periods"
 * @property {string} nextTopic      - "Mesolithic Age"
 * @property {string} nextDir        - "mesolithic-age"
 * @property {string[]} childTopics  - ["Lower Paleolithic", "Middle Paleolithic", "Upper Paleolithic"]
 * @property {string[]} similarTopics- ["Stone Tools", "Bhimbetka Rock Paintings"]
 * @property {string[]} confusedTopics- ["Neolithic Age", "Chalcolithic Age"]
 * @property {string} canonicalUrl   - "https://sjmaths.com/upsc/ancient-history/Prehistory/paleolithic-age/"
 * @property {string} description    - "SEO meta description"
 * @property {string} category       - "GS-1" | "GS-2" | "GS-3" | "GS-4" | "CSAT"
 * @property {boolean} supportsMains - true if this topic has mains answer writing
 * @property {string} topicId        - unique ID, e.g. "ancient-history.prehistory.paleolithic"
 * @property {string[]} practiceTypes- ["basic","conceptual","statement","assertion","match","advanced"]
 * @property {string} difficulty     - "easy" | "medium" | "hard"
 * @property {object} studyTime      - { concepts: 20, practice: 15, revision: 8 }
 * @property {string[]} learningObjectives - ["Explain the three phases of Paleolithic Age", "Compare Acheulian and Soanian traditions"]
 * @property {Scope} scope           - topic boundary definition
 * @property {object} related        - { prerequisite: [], recommendedNext: [], advancedTopics: [] }
 */

/**
 * @typedef {Object} Scope
 * @property {string[]} mustExplain   - concepts that MUST be explained in this topic
 * @property {string[]} mayMention    - concepts that can be briefly mentioned
 * @property {string[]} neverExplain  - concepts that must NOT be explained (belong to other topics)
 * @property {string[]} relatedTopics - URLs or slugs of related microtopics
 * @property {string[]} keywords      - SEO and content keywords
 */

// ============================================================================
// GLOSSARY — Ensures consistent terminology across all pages
// ============================================================================
/**
 * Glossary maps English terms to their canonical Hindi translations.
 * This is used by the translator to ensure consistency across thousands of pages.
 * 
 * Example:
 *   "Doctrine of Eclipse" always → "ग्रहण का सिद्धांत"
 *   "Paleolithic" always → "पुरापाषाण काल"
 * 
 * A generic translator might produce different Hindi for the same English term
 * on different pages. The glossary prevents this.
 */
const DEFAULT_GLOSSARY = {
  // Prehistory
  'Paleolithic': 'पुरापाषाण काल',
  'Mesolithic': 'मध्यपाषाण काल',
  'Neolithic': 'नवपाषाण काल',
  'Chalcolithic': 'ताम्रपाषाण काल',
  'Acheulian': 'एश्यूलियन',
  'Soanian': 'सोआनियन',
  'Nevasan': 'नेवासन',
  'Handaxe': 'हस्त कुठार',
  'Cleaver': 'क्लीवर',
  'Blade': 'फलक',
  'Burin': 'ब्यूरिन',
  'Scraper': 'खुरचनी',
  'Borers': 'बेधनी',
  'Hominin': 'होमिनिन',
  'Pleistocene': 'प्लीस्टोसीन',
  'Holocene': 'होलोसीन',

  // Polity
  'Doctrine of Eclipse': 'ग्रहण का सिद्धांत',
  'Doctrine of Severability': 'पृथक्करणीयता का सिद्धांत',
  'Doctrine of Basic Structure': 'मूल संरचना का सिद्धांत',
  'Judicial Review': 'न्यायिक पुनरावलोकन',
  'Writ': 'रिट',
  'Habeas Corpus': 'बंदी प्रत्यक्षीकरण',
  'Mandamus': 'परमादेश',
  'Certiorari': 'उत्प्रेषण',
  'Prohibition': 'निषेध',
  'Quo Warranto': 'अधिकार पृच्छा',

  // Geography
  'Ecotone': 'इकोटोन',
  'Continental Drift': 'महाद्वीपीय विस्थापन',
  'Plate Tectonics': 'प्लेट विवर्तनिकी',
  'Monsoon': 'मानसून',
  'Western Ghats': 'पश्चिमी घाट',
  'Eastern Ghats': 'पूर्वी घाट',
  'Himalayas': 'हिमालय',
  'Indo-Gangetic Plain': 'सिंधु-गंगा का मैदान',
  'Deccan Plateau': 'दक्कन का पठार',
  'Thar Desert': 'थार मरुस्थल',

  // Environment
  'Biodiversity': 'जैव विविधता',
  'Ecosystem': 'पारिस्थितिकी तंत्र',
  'Biosphere': 'जीवमंडल',
  'Food Chain': 'खाद्य श्रृंखला',
  'Food Web': 'खाद्य जाल',
  'Trophic Level': 'पोषी स्तर',
  'Ecological Pyramid': 'पारिस्थितिक पिरामिड',
  'Biome': 'जैवभूमि',
  'Conservation': 'संरक्षण',
  'Endemic Species': 'स्थानिक प्रजाति',
  'Endangered': 'लुप्तप्राय',
  'Vulnerable': 'असुरक्षित',
  'Critically Endangered': 'गंभीर रूप से लुप्तप्राय',

  // Economy
  'GDP': 'सकल घरेलू उत्पाद',
  'GNP': 'सकल राष्ट्रीय उत्पाद',
  'Inflation': 'मुद्रास्फीति',
  'Deflation': 'अपस्फीति',
  'Fiscal Policy': 'राजकोषीय नीति',
  'Monetary Policy': 'मौद्रिक नीति',
  'Repo Rate': 'रेपो दर',
  'Reverse Repo Rate': 'रिवर्स रेपो दर',
  'CRR': 'नकद आरक्षित अनुपात',
  'SLR': 'वैधानिक तरलता अनुपात',
  'Budget': 'बजट',
  'Subsidy': 'सब्सिडी',
  'Tax': 'कर',
  'Direct Tax': 'प्रत्यक्ष कर',
  'Indirect Tax': 'अप्रत्यक्ष कर',
  'GST': 'वस्तु एवं सेवा कर',

  // Science & Tech
  'DNA': 'डीएनए',
  'RNA': 'आरएनए',
  'Gene': 'जीन',
  'Chromosome': 'गुणसूत्र',
  'Mutation': 'उत्परिवर्तन',
  'Photosynthesis': 'प्रकाश संश्लेषण',
  'Respiration': 'श्वसन',
  'Mitosis': 'समसूत्री विभाजन',
  'Meiosis': 'अर्धसूत्री विभाजन',
  'Antibody': 'प्रतिरक्षी',
  'Antigen': 'प्रतिजन',
  'Vaccine': 'टीका',
  'Satellite': 'उपग्रह',
  'Orbit': 'कक्षा',
  'Rocket': 'रॉकेट',
  'Nuclear Fission': 'नाभिकीय विखंडन',
  'Nuclear Fusion': 'नाभिकीय संलयन',

  // Art & Culture
  'Temple Architecture': 'मंदिर वास्तुकला',
  'Nagara Style': 'नागर शैली',
  'Dravida Style': 'द्रविड़ शैली',
  'Vesara Style': 'वेसर शैली',
  'Rock Cut': 'शैल काट',
  'Stupa': 'स्तूप',
  'Vihara': 'विहार',
  'Chaitya': 'चैत्य',
  'Mural': 'भित्तिचित्र',
  'Miniature': 'लघुचित्र',
  'Raga': 'राग',
  'Tala': 'ताल',
  'Mudra': 'मुद्रा',

  // Modern History
  'Revolt of 1857': '1857 का विद्रोह',
  'Indian National Congress': 'भारतीय राष्ट्रीय कांग्रेस',
  'Partition of Bengal': 'बंगाल का विभाजन',
  'Swadeshi Movement': 'स्वदेशी आंदोलन',
  'Non-Cooperation Movement': 'असहयोग आंदोलन',
  'Civil Disobedience Movement': 'सविनय अवज्ञा आंदोलन',
  'Quit India Movement': 'भारत छोड़ो आंदोलन',
  'Simon Commission': 'साइमन कमीशन',
  'Government of India Act': 'भारत सरकार अधिनियम',
  'Cabinet Mission': 'कैबिनेट मिशन',
  'Mountbatten Plan': 'माउंटबेटन योजना',
  'Indian Independence Act': 'भारतीय स्वतंत्रता अधिनियम',
};

// ============================================================================
// NORMALIZER — Standardizes content before translation
// ============================================================================
/**
 * Keys whose string values are prose that should get period normalization.
 * All other keys (headers, labels, terms, options, etc.) are left untouched
 * to prevent stray periods on table cells, MCQ options, and term labels.
 */
const PROSE_KEYS = new Set([
  'content', 'definition', 'explanation', 'importanceInUpsc',
  'introduction', 'body', 'conclusion', 'clarification',
  'relationship', 'description',
]);

/**
 * The Normalizer runs after Gemini generates JSON but before translation.
 * It ensures every page has consistent editorial style.
 * 
 * Normalizations applied:
 *   ✓ Whitespace — no trailing spaces, consistent newlines
 *   ✓ Bullet styles — all use consistent markers
 *   ✓ Punctuation — period added only to PROSE_KEYS (content, definition, etc.)
 *   ✓ Date formats — all to "Month YYYY" format
 *   ✓ Number ranges — en-dash
 * 
 * Structural values (headers, labels, terms, option letters, etc.) are
 * NEVER modified — no stray periods glued onto table cells or MCQ options.
 */
function normalizeContent(data) {
  function normalize(obj, key = '') {
    if (typeof obj === 'string') {
      let text = obj;

      // 1. Trim whitespace
      text = text.trim();

      // 2. Collapse multiple spaces
      text = text.replace(/  +/g, ' ');

      // 3. Remove trailing spaces from each line
      text = text.split('\n').map(line => line.trimEnd()).join('\n');

      // 4. Standardize bullet markers (•, -, *, → all become •)
      text = text.replace(/^[-*→]\s/gm, '• ');

      // 5. Add period only to prose fields (content, definition, explanation, etc.)
      // NOT to headers, labels, terms, option letters, or other structural values
      if (PROSE_KEYS.has(key) && text.length > 20 &&
        !text.endsWith('.') && !text.endsWith('?') && !text.endsWith('!') &&
        !text.endsWith(':') && !text.endsWith('\n')) {
        text += '.';
      }

      // 6. Standardize date formats: "Jan 2024" → "January 2024"
      const monthAbbr = /(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})/g;
      const monthFull = {
        Jan: 'January', Feb: 'February', Mar: 'March', Apr: 'April',
        May: 'May', Jun: 'June', Jul: 'July', Aug: 'August',
        Sep: 'September', Oct: 'October', Nov: 'November', Dec: 'December'
      };
      text = text.replace(monthAbbr, (match, m, y) => `${monthFull[m] || m} ${y}`);

      // 7. Standardize number ranges: "10-20" → "10–20" (en-dash)
      text = text.replace(/(\d+)-(\d+)/g, '$1–$2');

      // 8. Remove duplicate spaces after periods
      text = text.replace(/\.  +/g, '. ');

      return text;
    }

    if (Array.isArray(obj)) {
      return obj.map((item) => normalize(item, key));
    }

    if (typeof obj === 'object' && obj !== null) {
      if (typeof obj.en === 'string' && typeof obj.hi === 'string') {
        return {
          en: normalize(obj.en, key),
          hi: normalize(obj.hi, key)
        };
      }
      const result = {};
      for (const [k, value] of Object.entries(obj)) {
        result[k] = normalize(value, k);
      }
      return result;
    }

    return obj;
  }

  return normalize(data);
}

// ============================================================================
// GLOSSARY-BASED TRANSLATOR
// ============================================================================
/**
 * Keys that should NOT be wrapped in { en, hi } because they are
 * structural values used by the renderer (option letters, correct answers,
 * match pair IDs, visual block types, etc.).
 */
const STRUCTURAL_KEYS = new Set([
  'id', 'letter', 'correct', 'correctAnswer', 'correctMapping',
  'left', 'right', 'type', 'marks', 'number', 'icon',
  'difficulty', 'estimatedReadingTime',
]);

/**
 * Translates English JSON to bilingual { en, hi } format.
 * If the JSON already contains bilingual { en, hi } objects (e.g. directly generated by Gemini),
 * it returns them with 0 translation API calls.
 * If untranslated strings remain, it collects them all and translates in 1 batch call.
 * 
 * @param {Object} englishJson - The normalized JSON from Gemini
 * @param {Function} translateFn - async (text, targetLang) => translatedText (supports string, array, or object)
 * @param {Object} glossary - Custom glossary entries for this subject
 * @returns {Object} Bilingual JSON with { en, hi } on all text fields
 */
async function translateToBilingual(englishJson, translateFn, glossary = {}) {
  if (!englishJson) return null;

  const mergedGlossary = { ...DEFAULT_GLOSSARY, ...glossary };

  function applyGlossary(text) {
    if (typeof text !== 'string') return text;
    let result = text;
    for (const [en, hi] of Object.entries(mergedGlossary)) {
      const escaped = en.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const regex = new RegExp(`\\b${escaped}\\b`, 'gi');
      result = result.replace(regex, hi);
    }
    return result;
  }

  function isBilingual(obj) {
    return (
      typeof obj === 'object' &&
      obj !== null &&
      !Array.isArray(obj) &&
      typeof obj.en === 'string' &&
      typeof obj.hi === 'string'
    );
  }

  // 1. Collect untranslated strings
  const stringsToTranslate = new Set();

  function collect(obj, key = '') {
    if (STRUCTURAL_KEYS.has(key)) return;
    if (isBilingual(obj)) return;

    if (typeof obj === 'string') {
      if (obj.trim().length > 0) {
        stringsToTranslate.add(obj);
      }
      return;
    }

    if (Array.isArray(obj)) {
      obj.forEach(item => collect(item, key));
      return;
    }

    if (typeof obj === 'object' && obj !== null) {
      for (const [k, v] of Object.entries(obj)) {
        collect(v, k);
      }
    }
  }

  collect(englishJson);

  // 2. Batch translate strings if any untranslated strings exist
  const translationMap = new Map();
  if (stringsToTranslate.size > 0 && typeof translateFn === 'function') {
    const uniqueStrings = Array.from(stringsToTranslate);
    try {
      const glossaryStrings = uniqueStrings.map(s => applyGlossary(s));
      const res = await translateFn(glossaryStrings, 'hi');
      if (Array.isArray(res)) {
        uniqueStrings.forEach((str, i) => {
          translationMap.set(str, res[i] || str);
        });
      } else if (typeof res === 'object' && res !== null && !(res instanceof Promise)) {
        uniqueStrings.forEach(str => {
          translationMap.set(str, res[str] || applyGlossary(str));
        });
      } else {
        await Promise.all(uniqueStrings.map(async (str) => {
          const hi = await translateFn(applyGlossary(str), 'hi');
          translationMap.set(str, hi || str);
        }));
      }
    } catch {
      uniqueStrings.forEach(str => translationMap.set(str, applyGlossary(str)));
    }
  }

  // 3. Transform JSON into bilingual structure
  function transform(obj, key = '') {
    if (STRUCTURAL_KEYS.has(key)) {
      return obj;
    }

    if (isBilingual(obj)) {
      return {
        en: obj.en,
        hi: applyGlossary(obj.hi)
      };
    }

    if (typeof obj === 'string') {
      const hi = translationMap.get(obj) || applyGlossary(obj);
      return { en: obj, hi };
    }

    if (Array.isArray(obj)) {
      return obj.map(item => transform(item, key));
    }

    if (typeof obj === 'object' && obj !== null) {
      const result = {};
      for (const [k, v] of Object.entries(obj)) {
        result[k] = transform(v, k);
      }
      return result;
    }

    return obj;
  }

  return transform(englishJson);
}

// ============================================================================
// CONTENT HASHER — Real SHA-256 for change detection
// ============================================================================
/**
 * Generates a content hash for the generated page.
 * Delegates to generateSha256Hash for the real SHA-256 implementation.
 * 
 * Used for:
 *   - Change detection (did the content actually change?)
 *   - Cache invalidation (bust CDN cache when hash changes)
 *   - Duplicate detection (same hash = same content)
 *   - Regeneration decisions (skip if hash unchanged)
 * 
 * @param {string|Object} data - Content to hash
 * @returns {Promise<string>} Hex SHA-256 with "sha256-" prefix
 */
async function generateContentHash(data) {
  return await generateSha256Hash(data);
}

// ============================================================================
// SCORER — Enterprise quality gate
// ============================================================================
/**
 * Scores every generated page on 6 dimensions.
 * If overallScore < 90, the page should be auto-regenerated.
 * 
 * Dimensions:
 *   seo             — meta description length, title length, canonical URL, keywords
 *   coverage        — all required sections present, word count adequate
 *   duplication     — percentage of unique content (lower = more duplicate)
 *   readability     — sentence length, paragraph length, complexity
 *   upscQuality     — relevance to UPSC exam pattern, trap warnings present
 *   hallucinationRisk — mentions of forbidden topics, fabricated data
 */
class PageScorer {
  constructor(meta) {
    this.meta = meta;
    this.scores = {};
  }

  score(tabName, data) {
    const scores = {
      seo: this.scoreSeo(),
      coverage: this.scoreCoverage(tabName, data),
      duplication: this.scoreDuplication(data),
      readability: this.scoreReadability(data),
      upscQuality: this.scoreUpscQuality(tabName, data),
      hallucinationRisk: this.scoreHallucinationRisk(data),
    };

    // Weighted overall score
    const weights = {
      seo: 0.10,
      coverage: 0.25,
      duplication: 0.15,
      readability: 0.15,
      upscQuality: 0.25,
      hallucinationRisk: 0.10,
    };

    let overall = 0;
    for (const [dim, score] of Object.entries(scores)) {
      overall += score * (weights[dim] || 0);
    }

    return {
      dimensions: scores,
      overall: Math.round(overall),
      passed: overall >= 80,
      tabName,
      timestamp: new Date().toISOString(),
    };
  }

  scoreSeo() {
    let score = 100;
    const desc = this.meta.description || '';

    if (desc.length < 50) score -= 20;
    if (desc.length > 160) score -= 10;
    if (!this.meta.canonicalUrl) score -= 15;
    if (!this.meta.topicId) score -= 10;

    const title = `${this.meta.name} | UPSC ${this.meta.category} | SJMaths`;
    if (title.length > 70) score -= 10;

    return Math.max(0, score);
  }

  scoreCoverage(tabName, data) {
    if (!data) return 0;

    let score = 100;
    const wordCount = this.countWords(data);

    const minWords = {
      overview: 50, concepts: 200, visual: 50,
      comparisons: 100, practice: 200, mains: 100,
      revision: 50, test: 200,
    };

    if (wordCount < (minWords[tabName] || 50)) {
      score -= 30;
    }

    // Check for empty arrays
    const hasEmpty = this.hasEmptyArrays(data);
    if (hasEmpty) score -= 20;

    return Math.max(0, score);
  }

  scoreDuplication(data) {
    if (!data) return 50;

    const strings = [];
    const collect = (obj) => {
      if (typeof obj === 'string') strings.push(obj);
      if (Array.isArray(obj)) obj.forEach(collect);
      if (typeof obj === 'object' && obj !== null) {
        Object.values(obj).forEach(collect);
      }
    };
    collect(data);

    if (strings.length === 0) return 50;

    const unique = new Set(strings);
    const ratio = unique.size / strings.length;

    // Score: 100 if all unique, 0 if all duplicate
    return Math.round(ratio * 100);
  }

  scoreReadability(data) {
    if (!data) return 50;

    const text = JSON.stringify(data);
    const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);

    if (sentences.length === 0) return 50;

    const avgLength = sentences.reduce((sum, s) => sum + s.split(/\s+/).length, 0) / sentences.length;

    // Ideal: 15-25 words per sentence
    if (avgLength < 10) return 60;
    if (avgLength > 40) return 60;
    if (avgLength >= 15 && avgLength <= 25) return 100;
    return 80;
  }

  scoreUpscQuality(tabName, data) {
    if (!data) return 0;

    let score = 70; // Start at 70

    const text = JSON.stringify(data).toLowerCase();

    // Check for UPSC-relevant keywords
    const upscKeywords = ['prelims', 'mains', 'upsc', 'exam', 'pyq', 'previous year'];
    const hasUpscKeywords = upscKeywords.some(k => text.includes(k));
    if (hasUpscKeywords) score += 10;

    // Check for trap warnings (concepts tab)
    if (tabName === 'concepts' && text.includes('trap')) score += 10;
    if (tabName === 'concepts' && text.includes('common mistake')) score += 10;

    // Check for mnemonics (revision tab)
    if (tabName === 'revision' && text.includes('mnemonic')) score += 10;

    return Math.min(100, score);
  }

  scoreHallucinationRisk(data) {
    if (!data || !this.meta.scope?.neverExplain) return 100;

    const text = JSON.stringify(data).toLowerCase();
    const forbidden = this.meta.scope.neverExplain.map(t => t.toLowerCase());

    let risk = 0;
    for (const topic of forbidden) {
      if (text.includes(topic)) {
        risk += 20; // Each forbidden topic mention costs 20 points
      }
    }

    return Math.max(0, 100 - risk);
  }

  countWords(obj) {
    if (typeof obj === 'string') return obj.split(/\s+/).length;
    if (Array.isArray(obj)) return obj.reduce((sum, item) => sum + this.countWords(item), 0);
    if (typeof obj === 'object' && obj !== null) {
      return Object.values(obj).reduce((sum, val) => sum + this.countWords(val), 0);
    }
    return 0;
  }

  hasEmptyArrays(obj) {
    if (Array.isArray(obj) && obj.length === 0) return true;
    if (typeof obj === 'object' && obj !== null) {
      return Object.values(obj).some(v => this.hasEmptyArrays(v));
    }
    return false;
  }
}

// ============================================================================
// QUALITY CONTROL LAYER
// ============================================================================
class QualityControl {
  constructor(meta) {
    this.meta = meta;
    this.errors = [];
    this.warnings = [];
  }

  validate(tabName, data) {
    this.errors = [];
    this.warnings = [];

    if (!data) {
      this.errors.push(`[${tabName}] No data generated`);
      return this.result();
    }

    if (data === null || data === undefined) {
      this.errors.push(`[${tabName}] Data is null/undefined`);
      return this.result();
    }

    // Word count
    const wordCount = this.countWords(data);
    const limits = { overview: 250, concepts: 2000, visual: 500, comparisons: 1000, revision: 400 };
    if (limits[tabName] && wordCount > limits[tabName]) {
      this.warnings.push(`[${tabName}] Word count ${wordCount} exceeds limit ${limits[tabName]}`);
    }

    // Empty arrays
    this.checkEmpty(data, tabName);

    // Duplicate content
    this.checkDuplicates(data, tabName);

    // Forbidden topics
    if (this.meta.scope?.neverExplain) {
      this.checkForbiddenTopics(data, tabName);
    }

    // Required sections
    this.checkRequiredSections(tabName, data);

    return this.result();
  }

  countWords(obj) {
    if (typeof obj === 'string') return obj.split(/\s+/).length;
    if (Array.isArray(obj)) return obj.reduce((sum, item) => sum + this.countWords(item), 0);
    if (typeof obj === 'object' && obj !== null) {
      return Object.values(obj).reduce((sum, val) => sum + this.countWords(val), 0);
    }
    return 0;
  }

  checkEmpty(obj, path) {
    if (Array.isArray(obj) && obj.length === 0) {
      this.warnings.push(`[${path}] Empty array`);
    }
    if (typeof obj === 'object' && obj !== null) {
      for (const [key, value] of Object.entries(obj)) {
        this.checkEmpty(value, `${path}.${key}`);
      }
    }
  }

  checkDuplicates(obj, path) {
    const strings = [];
    const collect = (o, p) => {
      if (typeof o === 'string') {
        if (strings.includes(o)) {
          this.warnings.push(`[${p}] Duplicate text found`);
        }
        strings.push(o);
      }
      if (Array.isArray(o)) o.forEach((item, i) => collect(item, `${p}[${i}]`));
      if (typeof o === 'object' && o !== null) {
        for (const [k, v] of Object.entries(o)) collect(v, `${p}.${k}`);
      }
    };
    collect(obj, path);
  }

  checkForbiddenTopics(obj, path) {
    const forbidden = this.meta.scope.neverExplain.map(t => t.toLowerCase());
    const text = JSON.stringify(obj).toLowerCase();
    for (const topic of forbidden) {
      if (text.includes(topic)) {
        this.warnings.push(`[${path}] Contains forbidden topic: "${topic}"`);
      }
    }
  }

  checkRequiredSections(tabName, data) {
    const required = {
      overview: ['title', 'definition', 'importanceInUpsc', 'learningOutcomes'],
      concepts: ['sections', 'keyTakeaways'],
      visual: ['visualBlocks'],
      comparisons: ['differenceTables'],
      practice: ['levels'],
      mains: ['questions'],
      revision: ['onePageNotes', 'examDaySheet'],
      test: ['mcq', 'statementBased'],
    };

    const sections = required[tabName] || [];
    for (const section of sections) {
      if (!data[section]) {
        this.errors.push(`[${tabName}] Missing required section: "${section}"`);
      }
    }
  }

  result() {
    return {
      passed: this.errors.length === 0,
      errors: this.errors,
      warnings: this.warnings,
    };
  }
}

// ============================================================================
// SEO VALIDATOR — Includes FAQ Schema generation
// ============================================================================
function validateSeo(meta) {
  const issues = [];

  if (!meta.description || meta.description.length < 50) {
    issues.push('Meta description too short (min 50 chars)');
  }
  if (meta.description && meta.description.length > 160) {
    issues.push('Meta description too long (max 160 chars)');
  }

  const title = `${meta.name} | UPSC ${meta.category} | SJMaths`;
  if (title.length > 70) {
    issues.push(`SEO title too long: ${title.length} chars (max 70)`);
  }

  if (!meta.canonicalUrl) {
    issues.push('Missing canonical URL');
  }

  if (!meta.topicId) {
    issues.push('Missing topicId');
  }

  return {
    passed: issues.length === 0,
    issues,
  };
}

/**
 * Generates FAQ structured data for SEO.
 * This is auto-generated from the topic metadata and content.
 * FAQ schema significantly improves search result visibility.
 */
function generateFaqSchema(meta, overviewData) {
  const faqs = [];

  // FAQ 1: What is [Topic]?
  if (overviewData?.definition) {
    faqs.push({
      '@type': 'Question',
      name: `What is ${meta.name}?`,
      acceptedAnswer: {
        '@type': 'Answer',
        text: typeof overviewData.definition === 'string'
          ? overviewData.definition
          : (overviewData.definition.en || ''),
      },
    });
  }

  // FAQ 2: Why is [Topic] important for UPSC?
  if (overviewData?.importanceInUpsc) {
    faqs.push({
      '@type': 'Question',
      name: `Why is ${meta.name} important for UPSC?`,
      acceptedAnswer: {
        '@type': 'Answer',
        text: typeof overviewData.importanceInUpsc === 'string'
          ? overviewData.importanceInUpsc
          : (overviewData.importanceInUpsc.en || ''),
      },
    });
  }

  // FAQ 3: What are the key topics in [Topic]?
  if (meta.scope?.mustExplain && meta.scope.mustExplain.length > 0) {
    faqs.push({
      '@type': 'Question',
      name: `What are the key topics in ${meta.name}?`,
      acceptedAnswer: {
        '@type': 'Answer',
        text: `The key topics include: ${meta.scope.mustExplain.join(', ')}.`,
      },
    });
  }

  // FAQ 4: How to study [Topic] for UPSC?
  if (meta.studyTime) {
    const totalTime = Object.values(meta.studyTime).reduce((a, b) => a + b, 0);
    faqs.push({
      '@type': 'Question',
      name: `How much time should I spend on ${meta.name} for UPSC?`,
      acceptedAnswer: {
        '@type': 'Answer',
        text: `You should spend approximately ${totalTime} minutes: ${meta.studyTime.concepts || 0} minutes on concepts, ${meta.studyTime.practice || 0} minutes on practice, and ${meta.studyTime.revision || 0} minutes on revision.`,
      },
    });
  }

  // FAQ 5: What is the difficulty level of [Topic]?
  if (meta.difficulty) {
    const difficultyMap = {
      easy: 'Easy — suitable for beginners',
      medium: 'Medium — requires conceptual understanding',
      hard: 'Hard — requires in-depth analysis and practice',
    };
    faqs.push({
      '@type': 'Question',
      name: `What is the difficulty level of ${meta.name}?`,
      acceptedAnswer: {
        '@type': 'Answer',
        text: difficultyMap[meta.difficulty] || meta.difficulty,
      },
    });
  }

  if (faqs.length === 0) return null;

  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs,
  };
}

// ============================================================================
// SPLIT PROMPTS
// ============================================================================
// ============================================================================
// SPLIT PROMPTS
// ============================================================================
const BILINGUAL_INSTRUCTION = `
BILINGUAL OUTPUT REQUIREMENT:
Generate ALL user-facing text strings directly as bilingual objects containing "en" (English) and "hi" (Hindi translation).
Do NOT wrap structural keys (like "id", "letter", "correct", "type", "marks", "number", "estimatedReadingTime") in { en, hi }.
Example: { "title": { "en": "English Title", "hi": "हिंदी शीर्षक" }, "id": 1 }

STRICT HINDI SCRIPT RULES:
- All "hi" values MUST be written in PROPER DEVANAGARI HINDI (हिंदी लिपि).
- NEVER write in Latin script / Hinglish (e.g. NEVER write "ka Parichay", "vajan aur map", "kshetron mein", "viksit kiya gaya").
- NEVER copy English strings into "hi" fields without translating them into Hindi.
- Incorrect: { "en": "Standardized Weights", "hi": "Standardized Weights" } or { "en": "Introduction", "hi": "Introduction ka Parichay" }
- Correct: { "en": "Standardized Weights", "hi": "मानकीकृत बाट/वजन" } and { "en": "Introduction", "hi": "परिचय" }
`;

function promptOverview(meta) {
  return `You are a UPSC faculty member. Write a brief overview for the microtopic "${meta.name}" (${meta.hindiName || meta.name}).

TOPIC CONTEXT:
- Subject: ${meta.subject}
- Parent Topic: ${meta.parentTopic}
- Category: ${meta.category}
- Difficulty: ${meta.difficulty || 'medium'}

SCOPE (stay within these boundaries):
- Must explain: ${(meta.scope?.mustExplain || []).join(', ')}
- May mention: ${(meta.scope?.mayMention || []).join(', ')}
- NEVER explain: ${(meta.scope?.neverExplain || []).join(', ')}

${BILINGUAL_INSTRUCTION}

RULES:
- Max 250 words total
- Do NOT explain concepts (that's Tab 2)
- Do NOT compare with other topics (that's Tab 4)
- Output ONLY valid JSON

Output this exact JSON:
{
  "title": { "en": "${meta.name}", "hi": "${meta.hindiName || meta.name}" },
  "definition": { "en": "One sentence definition in English.", "hi": "एक वाक्य की परिभाषा हिंदी में।" },
  "importanceInUpsc": { "en": "2-3 sentences on why this matters for UPSC Prelims/Mains.", "hi": "यूपीएससी प्रीलिम्स/मेन्स के लिए यह क्यों महत्वपूर्ण है, इस पर 2-3 वाक्य।" },
  "learningOutcomes": [
    { "en": "Outcome 1 in English", "hi": "परिणाम 1 हिंदी में" },
    { "en": "Outcome 2 in English", "hi": "परिणाम 2 हिंदी में" }
  ],
  "prerequisites": [
    { "en": "Prerequisite Topic 1", "hi": "पूर्वापेक्षा विषय 1" }
  ],
  "estimatedReadingTime": 15
}`;
}

function promptConcepts(meta) {
  return `You are a UPSC faculty member. Write detailed concept notes for "${meta.name}" (${meta.hindiName || meta.name}).

TOPIC CONTEXT:
- Subject: ${meta.subject}
- Parent Topic: ${meta.parentTopic}
- Category: ${meta.category}
- Difficulty: ${meta.difficulty || 'medium'}

SCOPE (CRITICAL — stay within these boundaries):
- Must explain thoroughly: ${(meta.scope?.mustExplain || []).join(', ')}
- May mention briefly: ${(meta.scope?.mayMention || []).join(', ')}
- NEVER explain (belong to other topics): ${(meta.scope?.neverExplain || []).join(', ')}

${BILINGUAL_INSTRUCTION}

RULES:
- Max 2000 words
- Explain ONLY concepts that belong to this microtopic
- NEVER explain sibling microtopics
- NEVER compare with other topics (that's Tab 4)
- Output ONLY valid JSON

Output this JSON:
{
  "sections": [
    {
      "title": { "en": "Section Title", "hi": "अनुभाग शीर्षक" },
      "type": "paragraph",
      "content": { "en": "Full explanation with key terms in **bold**.", "hi": "**बोल्ड** में मुख्य शब्दों के साथ पूर्ण व्याख्या।" }
    },
    {
      "title": { "en": "Classification Table", "hi": "वर्गीकरण तालिका" },
      "type": "table",
      "headers": [
        { "en": "Column 1", "hi": "स्तंभ 1" },
        { "en": "Column 2", "hi": "स्तंभ 2" }
      ],
      "rows": [
        [
          { "en": "Row 1 Col 1", "hi": "पंक्ति 1 स्तंभ 1" },
          { "en": "Row 1 Col 2", "hi": "पंक्ति 1 स्तंभ 2" }
        ]
      ]
    },
    {
      "title": { "en": "Key Characteristics", "hi": "मुख्य विशेषताएं" },
      "type": "list",
      "items": [
        {
          "term": { "en": "Characteristic 1", "hi": "विशेषता 1" },
          "definition": { "en": "Explanation in English.", "hi": "हिंदी में व्याख्या।" }
        }
      ]
    },
    {
      "title": { "en": "Sub-concepts", "hi": "उप-अवधारणाएं" },
      "type": "subcards",
      "items": [
        {
          "title": { "en": "Sub-concept 1", "hi": "उप-अवधारणा 1" },
          "content": { "en": "Explanation.", "hi": "व्याख्या।" }
        }
      ]
    }
  ],
  "upscNotes": [
    {
      "type": "trap",
      "content": { "en": "Common mistake students make.", "hi": "छात्रों द्वारा की जाने वाली सामान्य गलती।" }
    },
    {
      "type": "tip",
      "content": { "en": "Exam-specific insight.", "hi": "परीक्षा-विशिष्ट अंतर्दृष्टि।" }
    }
  ],
  "keyTakeaways": [
    { "en": "Takeaway 1", "hi": "मुख्य बिंदु 1" },
    { "en": "Takeaway 2", "hi": "मुख्य बिंदु 2" }
  ]
}`;
}

function promptVisual(meta) {
  return `You are a UPSC faculty member. Create visual learning aids for "${meta.name}" (${meta.hindiName || meta.name}).

SCOPE:
- Must explain: ${(meta.scope?.mustExplain || []).join(', ')}
- NEVER explain: ${(meta.scope?.neverExplain || []).join(', ')}

${BILINGUAL_INSTRUCTION}

RULES:
- Max 500 words total (mostly labels)
- No SVG, no HTML
- Output ONLY valid JSON

Output this JSON:
{
  "visualBlocks": [
    {
      "type": "timeline",
      "title": { "en": "Chronological Development", "hi": "कालानुक्रमिक विकास" },
      "data": [
        {
          "label": { "en": "Period 1", "hi": "काल 1" },
          "description": { "en": "Key event", "hi": "प्रमुख घटना" }
        }
      ]
    },
    {
      "type": "flow",
      "title": { "en": "Process Flow", "hi": "प्रक्रिया प्रवाह" },
      "data": [
        { "en": "Step 1", "hi": "चरण 1" },
        { "en": "Step 2", "hi": "चरण 2" }
      ]
    },
    {
      "type": "tree",
      "title": { "en": "Classification Hierarchy", "hi": "वर्गीकरण पदानुक्रम" },
      "data": {
        "root": { "en": "Central Concept", "hi": "केंद्रीय अवधारणा" },
        "branches": [
          {
            "label": { "en": "Branch 1", "hi": "शाखा 1" },
            "children": [
              { "en": "Sub 1a", "hi": "उप 1a" }
            ]
          }
        ]
      }
    },
    {
      "type": "table",
      "title": { "en": "Data Summary", "hi": "डेटा सारांश" },
      "headers": [
        { "en": "Header 1", "hi": "शीर्षक 1" },
        { "en": "Header 2", "hi": "शीर्षक 2" }
      ],
      "rows": [
        [
          { "en": "Value 1", "hi": "मान 1" },
          { "en": "Value 2", "hi": "मान 2" }
        ]
      ]
    }
  ]
}`;
}

function promptComparisons(meta) {
  return `You are a UPSC faculty member. Create comparison tables for "${meta.name}" (${meta.hindiName || meta.name}).

SCOPE:
- Current topic: ${meta.name}
- Related topics: ${(meta.scope?.relatedTopics || []).join(', ')}

${BILINGUAL_INSTRUCTION}

RULES:
- Max 1000 words
- Output ONLY valid JSON

Output this JSON:
{
  "differenceTables": [
    {
      "title": { "en": "${meta.name} vs Related Topic", "hi": "${meta.hindiName || meta.name} बनाम संबंधित विषय" },
      "headers": [
        { "en": "Aspect", "hi": "पहलू" },
        { "en": "${meta.name}", "hi": "${meta.hindiName || meta.name}" },
        { "en": "Related Topic", "hi": "संबंधित विषय" }
      ],
      "rows": [
        [
          { "en": "Aspect 1", "hi": "पहलू 1" },
          { "en": "Value for current", "hi": "वर्तमान का मान" },
          { "en": "Value for related", "hi": "संबंधित का मान" }
        ]
      ]
    }
  ],
  "similarityTables": [
    {
      "title": { "en": "Similarities", "hi": "समानताएं" },
      "headers": [
        { "en": "Shared Aspect", "hi": "साझा पहलू" },
        { "en": "Description", "hi": "विवरण" }
      ],
      "rows": [
        [
          { "en": "Aspect 1", "hi": "पहलू 1" },
          { "en": "How they are similar", "hi": "वे कैसे समान हैं" }
        ]
      ]
    }
  ],
  "evolution": {
    "title": { "en": "Evolutionary Progression", "hi": "द्विविकास प्रोग्रेशन" },
    "steps": [
      { "en": "Previous Stage", "hi": "पिछला चरण" },
      { "en": "${meta.name}", "hi": "${meta.hindiName || meta.name}" }
    ]
  },
  "frequentlyConfused": [
    {
      "topicA": { "en": "${meta.name}", "hi": "${meta.hindiName || meta.name}" },
      "topicB": { "en": "Confused Topic", "hi": "भ्रामक विषय" },
      "clarification": { "en": "Clarification.", "hi": "स्पष्टीकरण।" }
    }
  ],
  "conceptConnections": [
    {
      "from": { "en": "Concept A", "hi": "अवधारणा A" },
      "to": { "en": "Concept B", "hi": "अवधारणा B" },
      "relationship": { "en": "How they connect.", "hi": "वे कैसे जुड़ते हैं।" }
    }
  ]
}`;
}

function promptPractice(meta) {
  const types = meta.practiceTypes || ['basic', 'conceptual', 'statement', 'assertion', 'match', 'advanced'];

  return `You are a UPSC faculty member. Create practice questions for "${meta.name}" (${meta.hindiName || meta.name}).

SCOPE:
- Must test: ${(meta.scope?.mustExplain || []).join(', ')}

${BILINGUAL_INSTRUCTION}

STRICT QUANTITY REQUIREMENT:
- You MUST generate AT LEAST 20 practice questions total (5 in basic, 5 in conceptual, 5 in statementBased, 5 in match/advanced).
- Every question MUST have 4 options (A, B, C, D) and a detailed bilingual explanation.
- IMPORTANT: All questions, options, statements, and explanations MUST contain complete, detailed, realistic UPSC history content.
- NEVER use placeholders, dummy text, or copy the example questions/options literally (e.g. do not write "Question 1?", "Option 1", "Statement 1").
- Write actual historical statements and questions relevant to the microtopic!

RULES:
- Create practice questions across basic, conceptual, statementBased, match.
- Output ONLY valid JSON.

Output this JSON structure:
{
  "levels": {
    "basic": [
      {
        "id": 1,
        "question": { "en": "Question 1?", "hi": "प्रश्न 1?" },
        "options": [
          { "letter": "A", "text": { "en": "Option 1", "hi": "विकल्प 1" }, "correct": false },
          { "letter": "B", "text": { "en": "Option 2", "hi": "विकल्प 2" }, "correct": true },
          { "letter": "C", "text": { "en": "Option 3", "hi": "विकल्प 3" }, "correct": false },
          { "letter": "D", "text": { "en": "Option 4", "hi": "विकल्प 4" }, "correct": false }
        ],
        "explanation": { "en": "Explanation.", "hi": "व्याख्या।" }
      }
      /* Include 5 questions in basic */
    ],
    "conceptual": [
      /* Include 5 questions in conceptual (IDs 6-10) */
    ],
    "statementBased": [
      {
        "id": 11,
        "question": { "en": "Consider the following statements:", "hi": "निम्नलिखित कथनों पर विचार कीजिए:" },
        "statements": [
          { "number": 1, "text": { "en": "Statement 1", "hi": "कथन 1" }, "correct": true },
          { "number": 2, "text": { "en": "Statement 2", "hi": "कथन 2" }, "correct": false }
        ],
        "options": [
          { "letter": "A", "text": { "en": "1 only", "hi": "केवल 1" }, "correct": true },
          { "letter": "B", "text": { "en": "2 only", "hi": "केवल 2" }, "correct": false },
          { "letter": "C", "text": { "en": "Both 1 and 2", "hi": "1 और 2 दोनों" }, "correct": false },
          { "letter": "D", "text": { "en": "Neither 1 nor 2", "hi": "न तो 1 और न ही 2" }, "correct": false }
        ],
        "explanation": { "en": "Explanation.", "hi": "व्याख्या।" }
      }
      /* Include 5 questions in statementBased (IDs 11-15) */
    ],
    "match": [
      {
        "id": 16,
        "question": {
          "en": "Match the Maratha Chiefs in List I with their respective territories in List II:",
          "hi": "सूची I में दिए गए मराठा सरदारों को सूची II में उनके संबंधित क्षेत्रों के साथ सुमेलित कीजिए:"
        },
        "pairs": [
          { "left": { "en": "1. Gaekwad", "hi": "1. गायकवाड़" }, "right": { "en": "A. Gwalior", "hi": "A. ग्वालियर" } },
          { "left": { "en": "2. Bhonsle", "hi": "2. भोंसले" }, "right": { "en": "B. Indore", "hi": "B. इंदौर" } },
          { "left": { "en": "3. Holkar", "hi": "3. होलकर" }, "right": { "en": "C. Baroda", "hi": "C. बड़ौदा" } },
          { "left": { "en": "4. Scindia", "hi": "4. सिंधिया" }, "right": { "en": "D. Nagpur", "hi": "D. नागपुर" } }
        ],
        "options": [
          { "letter": "A", "text": { "en": "1-C, 2-D, 3-B, 4-A", "hi": "1-C, 2-D, 3-B, 4-A" }, "correct": true },
          { "letter": "B", "text": { "en": "1-A, 2-B, 3-C, 4-D", "hi": "1-A, 2-B, 3-C, 4-D" }, "correct": false },
          { "letter": "C", "text": { "en": "1-D, 2-A, 3-B, 4-C", "hi": "1-D, 2-A, 3-B, 4-C" }, "correct": false },
          { "letter": "D", "text": { "en": "1-B, 2-C, 3-D, 4-A", "hi": "1-B, 2-C, 3-D, 4-A" }, "correct": false }
        ],
        "explanation": {
          "en": "Gaekwad ruled Baroda (C), Bhonsle ruled Nagpur (D), Holkar ruled Indore (B), Scindia ruled Gwalior (A).",
          "hi": "गायकवाड़ ने बड़ौदा (C) पर शासन किया, भोंसले ने नागपुर (D) पर शासन किया, होलकर ने इंदौर (B) पर शासन किया, सिंधिया ने ग्वालियर (A) पर शासन किया।"
        }
      }
      /* Include 5 questions in match (IDs 16-20) */
    ]
  }
}`;
}

function promptMains(meta) {
  return `You are a UPSC faculty member. Create mains answer writing content for "${meta.name}" (${meta.hindiName || meta.name}).

${BILINGUAL_INSTRUCTION}

Output this JSON:
{
  "questions": [
    {
      "marks": 10,
      "question": { "en": "10-mark question?", "hi": "10 अंक का प्रश्न?" },
      "structure": [
        { "en": "Intro point", "hi": "प्रस्तावना बिंदु" },
        { "en": "Body point", "hi": "मुख्य भाग बिंदु" },
        { "en": "Conclusion", "hi": "निष्कर्ष" }
      ],
      "keywords": [
        { "en": "keyword1", "hi": "कीवर्ड1" }
      ],
      "modelAnswer": {
        "introduction": { "en": "2-3 sentence intro.", "hi": "2-3 वाक्य की प्रस्तावना।" },
        "body": { "en": "Key arguments and evidence.", "hi": "मुख्य तर्क और साक्ष्य।" },
        "conclusion": { "en": "1-2 sentence conclusion.", "hi": "1-2 वाक्य का निष्कर्ष।" }
      },
      "valueAddition": [
        { "en": "Relevant fact or data point", "hi": "प्रासंगिक तथ्य या डेटा बिंदु" }
      ],
      "diagram": {
        "type": "flow",
        "data": [
          { "en": "Step 1", "hi": "चरण 1" }
        ]
      }
    }
  ]
}`;
}

function promptRevision(meta) {
  return `You are a UPSC faculty member. Create ultra-condensed revision notes for "${meta.name}" (${meta.hindiName || meta.name}).

${BILINGUAL_INSTRUCTION}

Output this JSON:
{
  "onePageNotes": {
    "columns": [
      {
        "title": { "en": "Section 1", "hi": "अनुभाग 1" },
        "points": [
          { "en": "Point 1", "hi": "बिंदु 1" }
        ]
      }
    ]
  },
  "mnemonics": [
    {
      "phrase": { "en": "Acronym", "hi": "संक्षिप्त नाम" },
      "meaning": { "en": "Meaning", "hi": "अर्थ" },
      "explanation": { "en": "Explanation", "hi": "व्याख्या" }
    }
  ],
  "flashcards": [
    {
      "question": { "en": "Question?", "hi": "प्रश्न?" },
      "answer": { "en": "Answer.", "hi": "उत्तर।" }
    }
  ],
  "frequentlyConfusedFacts": [
    {
      "misconception": { "en": "Wrong belief", "hi": "गलत धारणा" },
      "correction": { "en": "Correct fact", "hi": "सही तथ्य" }
    }
  ],
  "examDaySheet": {
    "fiveFacts": [
      { "en": "Fact 1", "hi": "तथ्य 1" }
    ],
    "threeTraps": [
      { "en": "Trap 1", "hi": "ट्रैप 1" }
    ],
    "oneMnemonic": {
      "phrase": { "en": "Quick mnemonic", "hi": "त्वरित निमोनिक" },
      "meaning": { "en": "Meaning", "hi": "अर्थ" }
    }
  }
}`;
}

function promptTest(meta) {
  return `You are a UPSC faculty member. Create a test for "${meta.name}" (${meta.hindiName || meta.name}).

${BILINGUAL_INSTRUCTION}

Output this JSON:
{
  "mcq": [
    {
      "id": 1,
      "question": { "en": "Question?", "hi": "प्रश्न?" },
      "options": [
        { "letter": "A", "text": { "en": "Option 1", "hi": "विकल्प 1" } },
        { "letter": "B", "text": { "en": "Option 2", "hi": "विकल्प 2" } }
      ],
      "correctAnswer": "B",
      "explanation": { "en": "Explanation.", "hi": "व्याख्या।" }
    }
  ],
  "statementBased": [
    {
      "id": 16,
      "question": { "en": "Consider the following statements:", "hi": "निम्नलिखित कथनों पर विचार कीजिए:" },
      "statements": [
        { "number": 1, "text": { "en": "Statement 1", "hi": "कथन 1" }, "correct": true }
      ],
      "options": [
        { "letter": "A", "text": { "en": "1 only", "hi": "केवल 1" }, "correct": true }
      ],
      "explanation": { "en": "Explanation.", "hi": "व्याख्या।" }
    }
  ],
  "match": [
    {
      "id": 19,
      "question": {
        "en": "Match the Maratha Chiefs in List I with their respective territories in List II:",
        "hi": "सूची I में दिए गए मराठा सरदारों को सूची II में उनके संबंधित क्षेत्रों के साथ सुमेलित कीजिए:"
      },
      "pairs": [
        { "left": { "en": "1. Gaekwad", "hi": "1. गायकवाड़" }, "right": { "en": "A. Gwalior", "hi": "A. ग्वालियर" } },
        { "left": { "en": "2. Bhonsle", "hi": "2. भोंसले" }, "right": { "en": "B. Indore", "hi": "B. इंदौर" } },
        { "left": { "en": "3. Holkar", "hi": "3. होलकर" }, "right": { "en": "C. Baroda", "hi": "C. बड़ौदा" } },
        { "left": { "en": "4. Scindia", "hi": "4. सिंधिया" }, "right": { "en": "D. Nagpur", "hi": "D. नागपुर" } }
      ],
      "options": [
        { "letter": "A", "text": { "en": "1-C, 2-D, 3-B, 4-A", "hi": "1-C, 2-D, 3-B, 4-A" } },
        { "letter": "B", "text": { "en": "1-A, 2-B, 3-C, 4-D", "hi": "1-A, 2-B, 3-C, 4-D" } }
      ],
      "correctAnswer": "A",
      "explanation": {
        "en": "Gaekwad ruled Baroda (C), Bhonsle ruled Nagpur (D), Holkar ruled Indore (B), Scindia ruled Gwalior (A).",
        "hi": "गायकवाड़ ने बड़ौदा (C) पर शासन किया, भोंसले ने नागपुर (D) पर शासन किया, होलकर ने इंदौर (B) पर शासन किया, सिंधिया ने ग्वालियर (A) पर शासन किया।"
      }
    }
  ],
  "mains": {
    "id": 21,
    "question": { "en": "Mains question?", "hi": "मेंस प्रश्न?" },
    "marks": 10,
    "modelAnswer": { "en": "Brief outline.", "hi": "संक्षिप्त रूपरेखा।" }
  }
}`;
}

// ============================================================================
// PROMPT DISPATCHER
// ============================================================================
const PROMPT_GENERATORS = {
  overview: promptOverview,
  concepts: promptConcepts,
  visual: promptVisual,
  comparisons: promptComparisons,
  practice: promptPractice,
  mains: promptMains,
  revision: promptRevision,
  test: promptTest,
};

function generatePrompt(tabName, meta) {
  const generator = PROMPT_GENERATORS[tabName];
  if (!generator) throw new Error(`Unknown tab: ${tabName}`);
  return generator(meta);
}

// ============================================================================
// RESPONSE PARSER
// ============================================================================
function parseResponse(raw) {
  let cleaned = raw.trim();
  if (cleaned.startsWith('```json')) {
    cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  } else if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
  }

  // Normalize common formatting issues in model output
  cleaned = cleaned.replace(/[\u2018\u2019]/g, "'");
  cleaned = cleaned.replace(/[\u201c\u201d]/g, '"');

  const tryJsonParse = (text) => {
    try {
      return JSON.parse(text);
    } catch (err) {
      return null;
    }
  };

  let parsed = tryJsonParse(cleaned);
  if (parsed !== null) return parsed;

  const jsonMatch = cleaned.match(/[\{\[][\s\S]*[\}\]]/);
  if (jsonMatch) {
    cleaned = jsonMatch[0];
    parsed = tryJsonParse(cleaned);
    if (parsed !== null) return parsed;

    // Attempt to repair common JSON-like syntax from model output
    const repaired = cleaned
      .replace(/(\{|,|\[|\s)([A-Za-z0-9_\-]+)\s*:/g, '$1"$2":')
      .replace(/'/g, '"')
      .replace(/,\s*([}\]])/g, '$1');

    parsed = tryJsonParse(repaired);
    if (parsed !== null) return parsed;

    try {
      return Function('"use strict"; return (' + repaired + ')')();
    } catch (e3) {
      throw new Error(`Failed to parse JSON: ${e3.message}`);
    }
  }

  throw new Error(`No JSON found in response: ${new Error('JSON parse failed').message}`);
}

// ============================================================================
// CROSS-LINK RULES
// ============================================================================
const CROSS_LINK_RULES = {
  concepts: {
    currentTopic: 100,
    relatedTopics: 0,
    rule: 'NEVER explain sibling microtopics. Only explain the current topic.',
  },
  comparisons: {
    currentTopic: 50,
    relatedTopics: 50,
    rule: 'Only in tables. No detailed explanations of other topics. Brief connections only.',
  },
  revision: {
    currentTopic: 95,
    relatedTopics: 5,
    rule: 'Focus on current topic. Only mention related topics for contextual mnemonics or confusion clarifications.',
  },
};

// ============================================================================
// RELATED TOPICS CARD
// ============================================================================
const RELATED_TOPICS_CARD = `
  <div class="related-topics-card">
    <h2 class="card-title">
      <i class="fas fa-sitemap"></i>
      <span class="lang-en">Related Topics</span>
      <span class="lang-hi">संबंधित विषय</span>
    </h2>
    <div class="related-topics-grid">
      <div class="related-topic-group">
        <h3><span class="lang-en">Previous Topic</span><span class="lang-hi">पिछला विषय</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[PREVIOUS_DIR]/" class="related-topic-link">
          <i class="fas fa-arrow-left"></i>
          <span class="lang-en">[PREVIOUS_TOPIC]</span>
          <span class="lang-hi">[PREVIOUS_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Current Topic</span><span class="lang-hi">वर्तमान विषय</span></h3>
        <span class="related-topic-current">
          <i class="fas fa-circle"></i>
          <span class="lang-en">[TOPIC_NAME]</span>
          <span class="lang-hi">[HINDI_NAME]</span>
        </span>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Next Topic</span><span class="lang-hi">अगला विषय</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[NEXT_DIR]/" class="related-topic-link">
          <i class="fas fa-arrow-right"></i>
          <span class="lang-en">[NEXT_TOPIC]</span>
          <span class="lang-hi">[NEXT_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Parent Topic</span><span class="lang-hi">मूल विषय</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/" class="related-topic-link">
          <i class="fas fa-level-up-alt"></i>
          <span class="lang-en">[PARENT_TOPIC]</span>
          <span class="lang-hi">[PARENT_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Child Topics</span><span class="lang-hi">उप-विषय</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[CHILD_DIR]/" class="related-topic-link">
          <span class="lang-en">[CHILD_TOPIC]</span>
          <span class="lang-hi">[CHILD_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Similar Topics</span><span class="lang-hi">समान विषय</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[SIMILAR_DIR]/" class="related-topic-link">
          <span class="lang-en">[SIMILAR_TOPIC]</span>
          <span class="lang-hi">[SIMILAR_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Frequently Confused With</span><span class="lang-hi">अक्सर भ्रमित</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[CONFUSED_DIR]/" class="related-topic-link confused">
          <i class="fas fa-question-circle"></i>
          <span class="lang-en">[CONFUSED_TOPIC]</span>
          <span class="lang-hi">[CONFUSED_TOPIC_HI]</span>
        </a>
      </div>
    </div>
  </div>
`;

// ============================================================================
// FULL HTML PAGE TEMPLATE
// ============================================================================
const PAGE_TEMPLATE = `<!DOCTYPE html>
<html lang="en">
<head>
    ${STYLES_CSS}
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[SEO_TITLE]</title>
    <meta name="description" content="[SEO_DESCRIPTION]">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="[CANONICAL_URL]">
    <meta name="keywords" content="[SEO_KEYWORDS]">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c"></noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=bcdc8e39">

    <!-- Open Graph -->
    <meta property="og:title" content="[OG_TITLE]">
    <meta property="og:description" content="[OG_DESCRIPTION]">
    <meta property="og:type" content="article">
    <meta property="og:url" content="[CANONICAL_URL]">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="[OG_TITLE]">
    <meta name="twitter:description" content="[OG_DESCRIPTION]">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
            { "@type": "ListItem", "position": 2, "name": "UPSC IAS Prep", "item": "https://sjmaths.com/upsc/" },
            { "@type": "ListItem", "position": 3, "name": "[SUBJECT]", "item": "https://sjmaths.com/upsc/[SUBJECT_DIR]/" },
            { "@type": "ListItem", "position": 4, "name": "[PARENT_TOPIC]", "item": "https://sjmaths.com/upsc/[SUBJECT_DIR]/[PARENT_DIR]/" },
            { "@type": "ListItem", "position": 5, "name": "[TOPIC_NAME]", "item": "[CANONICAL_URL]" }
          ]
        },
        {
          "@type": "LearningResource",
          "name": "[TOPIC_NAME]",
          "description": "[SEO_DESCRIPTION]",
          "learningResourceType": "Study Notes",
          "educationalLevel": "UPSC Civil Services / IAS",
          "url": "[CANONICAL_URL]"
        }
      ]
    }
    </script>

    <!-- FAQ Schema (auto-generated) -->
    <script type="application/ld+json">[FAQ_SCHEMA]</script>
</head>
<body>
    <div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="/">Home</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/upsc/">UPSC</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/upsc/[SUBJECT_DIR]/">[SUBJECT]</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/">[PARENT_TOPIC]</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">[TOPIC_NAME]</span>
                <span class="lang-hi">[HINDI_NAME]</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">[TOPIC_NAME]</span>
                <span class="lang-hi">[HINDI_NAME]</span>
            </h1>
            <p class="topic-desc">
                <span class="lang-en">[SEO_DESCRIPTION]</span>
                <span class="lang-hi">[HINDI_DESCRIPTION]</span>
            </p>
            <div class="topic-meta-bar">
                <span class="topic-difficulty [DIFFICULTY_CLASS]">
                    <i class="fas fa-signal"></i>
                    <span class="lang-en">[DIFFICULTY_LABEL]</span>
                    <span class="lang-hi">[DIFFICULTY_LABEL_HI]</span>
                </span>
                <span class="topic-study-time">
                    <i class="fas fa-clock"></i>
                    <span class="lang-en">[STUDY_TIME_LABEL]</span>
                    <span class="lang-hi">[STUDY_TIME_LABEL_HI]</span>
                </span>
                <div class="lang-toggle">
                    <button id="langEn" class="active" aria-pressed="true">EN</button>
                    <button id="langHi" aria-pressed="false">हिन्दी</button>
                </div>
            </div>
        </div>

        <!-- 8-Tab Navigation -->
        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="tab-overview" role="tab" aria-selected="true">
                <i class="fas fa-compass"></i> <span class="lang-en">1. Overview</span><span class="lang-hi">1. अवलोकन</span>
            </button>
            <button class="tab-btn" data-tab="tab-concepts" role="tab" aria-selected="false">
                <i class="fas fa-book-open"></i> <span class="lang-en">2. Concepts</span><span class="lang-hi">2. अवधारणाएँ</span>
            </button>
            <button class="tab-btn" data-tab="tab-visual" role="tab" aria-selected="false">
                <i class="fas fa-diagram-project"></i> <span class="lang-en">3. Visual</span><span class="lang-hi">3. दृश्य</span>
            </button>
            <button class="tab-btn" data-tab="tab-comparisons" role="tab" aria-selected="false">
                <i class="fas fa-scale-balanced"></i> <span class="lang-en">4. Comparisons</span><span class="lang-hi">4. तुलना</span>
            </button>
            <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false">
                <i class="fas fa-list-check"></i> <span class="lang-en">5. Practice</span><span class="lang-hi">5. अभ्यास</span>
            </button>
            <button class="tab-btn" data-tab="tab-mains" role="tab" aria-selected="false" id="mains-tab-btn" style="display:none">
                <i class="fas fa-pen-fancy"></i> <span class="lang-en">6. Mains</span><span class="lang-hi">6. मेंस</span>
            </button>
            <button class="tab-btn" data-tab="tab-revision" role="tab" aria-selected="false">
                <i class="fas fa-rotate"></i> <span class="lang-en">7. Revision</span><span class="lang-hi">7. पुनरावृत्ति</span>
            </button>
            <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false">
                <i class="fas fa-graduation-cap"></i> <span class="lang-en">8. Test</span><span class="lang-hi">8. टेस्ट</span>
            </button>
        </div>

        <!-- Tab Content -->
        <div class="topic-content" id="topic-content"></div>

        <!-- Related Topics Card -->
        [RELATED_TOPICS_HTML]
    </main>

    <!-- Page data as JSON -->
    <script id="upsc-page-data" type="application/json">
    {
        "topicId": "[TOPIC_ID]",
        "topicName": "[TOPIC_NAME]",
        "hindiName": "[HINDI_NAME]",
        "subject": "[SUBJECT]",
        "subjectDir": "[SUBJECT_DIR]",
        "parentTopic": "[PARENT_TOPIC]",
        "parentDir": "[PARENT_DIR]",
        "previousTopic": "[PREVIOUS_TOPIC]",
        "previousDir": "[PREVIOUS_DIR]",
        "nextTopic": "[NEXT_TOPIC]",
        "nextDir": "[NEXT_DIR]",
        "difficulty": "[DIFFICULTY]",
        "studyTime": [STUDY_TIME_JSON],
        "learningObjectives": [LEARNING_OBJECTIVES_JSON],
        "supportsMains": [SUPPORTS_MAINS],
        "overview": [OVERVIEW_JSON],
        "concepts": [CONCEPTS_JSON],
        "visual": [VISUAL_JSON],
        "comparisons": [COMPARISONS_JSON],
        "practice": [PRACTICE_JSON],
        "mains": [MAINS_JSON],
        "revision": [REVISION_JSON],
        "test": [TEST_JSON],
        "version": {
            "generator": "[GENERATOR_VERSION]",
            "prompt": "[PROMPT_VERSION]",
            "translator": "[TRANSLATOR_VERSION]",
            "normalizer": "[NORMALIZER_VERSION]"
        },
        "contentHash": "[CONTENT_HASH]",
        "generatedAt": "[GENERATED_AT]"
    }
    </script>

    <!-- Reusable renderers -->
    <script src="/assets/js/upsc-renderer.min.js" defer></script>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>

    <script>
        (function () {
            const btnEn = document.getElementById('langEn');
            const btnHi = document.getElementById('langHi');
            const apply = (lang) => {
                document.documentElement.classList.toggle('lang-hi', lang === 'hi');
                document.documentElement.classList.toggle('lang-en', lang !== 'hi');
                document.body.classList.toggle('lang-hi', lang === 'hi');
                document.body.classList.toggle('lang-en', lang !== 'hi');
                if (btnEn) btnEn.classList.toggle('active', lang !== 'hi');
                if (btnHi) btnHi.classList.toggle('active', lang === 'hi');
                if (btnEn) btnEn.setAttribute('aria-pressed', String(lang !== 'hi'));
                if (btnHi) btnHi.setAttribute('aria-pressed', String(lang === 'hi'));
                try { localStorage.setItem('sj_pref_lang', lang); } catch (e) { }
            };
            document.addEventListener('DOMContentLoaded', () => {
                const pref = (localStorage.getItem('sj_pref_lang') || 'en');
                apply(pref);
                if (btnEn) btnEn.addEventListener('click', () => apply('en'));
                if (btnHi) btnHi.addEventListener('click', () => apply('hi'));
            });
        })();
    </script>
</body>
</html>`;

// ============================================================================
// HTML ASSEMBLER
// ============================================================================
/**
 * Cleans undefined values from an object, converting them to null.
 * This ensures valid JSON output when stringifying.
 */
function cleanUndefined(obj) {
  if (typeof obj === 'undefined') return null;
  if (Array.isArray(obj)) return obj.map(item => cleanUndefined(item));
  if (obj && typeof obj === 'object') {
    const cleaned = {};
    for (const [key, value] of Object.entries(obj)) {
      if (typeof value !== 'undefined') {
        cleaned[key] = cleanUndefined(value);
      } else {
        cleaned[key] = null;
      }
    }
    return cleaned;
  }
  return obj;
}

function assemblePage(meta, bilingualData, score) {
  let html = PAGE_TEMPLATE;

  // Difficulty labels
  const difficultyLabels = {
    easy: { en: 'Easy', hi: 'सरल' },
    medium: { en: 'Medium', hi: 'मध्यम' },
    hard: { en: 'Hard', hi: 'कठिन' },
  };
  const diff = difficultyLabels[meta.difficulty] || difficultyLabels.medium;

  // Study time
  const studyTime = meta.studyTime || { concepts: 15, practice: 10, revision: 5 };
  const totalTime = Object.values(studyTime).reduce((a, b) => a + b, 0);

  // Learning objectives
  const objectives = (meta.learningObjectives || []).map(item => {
    if (typeof item === 'object' && item !== null && item.en) return item;
    return { en: String(item), hi: String(item) };
  });

  // Clean undefined values from bilingualData before serialization
  const cleanedData = cleanUndefined(bilingualData);

  // Content hash
  const contentHash = generateContentHash(cleanedData);

  // FAQ schema
  const faqSchema = generateFaqSchema(meta, cleanedData.overview);

  // Replace metadata placeholders
  const replacements = {
    '[SEO_TITLE]': `${meta.name} | UPSC ${meta.category} | SJMaths`,
    '[SEO_DESCRIPTION]': meta.description,
    '[SEO_KEYWORDS]': `UPSC ${meta.name}, ${meta.subject} ${meta.name}, UPSC ${meta.category} ${meta.name}`,
    '[CANONICAL_URL]': meta.canonicalUrl,
    '[OG_TITLE]': `${meta.name} - UPSC ${meta.category} | SJMaths`,
    '[OG_DESCRIPTION]': meta.description,
    '[TOPIC_NAME]': meta.name,
    '[HINDI_NAME]': meta.hindiName,
    '[HINDI_DESCRIPTION]': meta.hindiDescription || meta.description,
    '[SUBJECT]': meta.subject,
    '[SUBJECT_DIR]': meta.subjectDir,
    '[PARENT_TOPIC]': meta.parentTopic,
    '[PARENT_DIR]': meta.parentDir,
    '[TOPIC_ID]': meta.topicId || `${meta.subjectDir}.${meta.parentDir}.${meta.dir}`,
    '[SUPPORTS_MAINS]': meta.supportsMains ? 'true' : 'false',
    '[PREVIOUS_TOPIC]': meta.previousTopic || '',
    '[PREVIOUS_DIR]': meta.previousDir || '',
    '[NEXT_TOPIC]': meta.nextTopic || '',
    '[NEXT_DIR]': meta.nextDir || '',
    '[DIFFICULTY]': meta.difficulty || 'medium',
    '[DIFFICULTY_CLASS]': `difficulty-${meta.difficulty || 'medium'}`,
    '[DIFFICULTY_LABEL]': diff.en,
    '[DIFFICULTY_LABEL_HI]': diff.hi,
    '[STUDY_TIME_LABEL]': `${totalTime} min total (Concepts: ${studyTime.concepts || 0}m, Practice: ${studyTime.practice || 0}m, Revision: ${studyTime.revision || 0}m)`,
    '[STUDY_TIME_LABEL_HI]': `कुल ${totalTime} मिनट (अवधारणाएँ: ${studyTime.concepts || 0}मि, अभ्यास: ${studyTime.practice || 0}मि, पुनरावृत्ति: ${studyTime.revision || 0}मि)`,
    '[GENERATOR_VERSION]': VERSION.generator,
    '[PROMPT_VERSION]': VERSION.prompt,
    '[TRANSLATOR_VERSION]': VERSION.translator,
    '[NORMALIZER_VERSION]': VERSION.normalizer,
    '[CONTENT_HASH]': contentHash,
    '[GENERATED_AT]': new Date().toISOString(),
    '[FAQ_SCHEMA]': JSON.stringify(faqSchema || {}),
  };

  for (const [key, value] of Object.entries(replacements)) {
    html = html.replace(new RegExp(key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g'), value);
  }

  // Inject JSON data — use cleanedData to ensure no undefined values
  html = html.replace('[OVERVIEW_JSON]', JSON.stringify(cleanedData.overview));
  html = html.replace('[CONCEPTS_JSON]', JSON.stringify(cleanedData.concepts));
  html = html.replace('[VISUAL_JSON]', JSON.stringify(cleanedData.visual));
  html = html.replace('[COMPARISONS_JSON]', JSON.stringify(cleanedData.comparisons));
  html = html.replace('[PRACTICE_JSON]', JSON.stringify(cleanedData.practice));
  html = html.replace('[MAINS_JSON]', JSON.stringify(cleanedData.mains));
  html = html.replace('[REVISION_JSON]', JSON.stringify(cleanedData.revision));
  html = html.replace('[TEST_JSON]', JSON.stringify(cleanedData.test || {}));
  html = html.replace('[STUDY_TIME_JSON]', JSON.stringify(studyTime));
  html = html.replace('[LEARNING_OBJECTIVES_JSON]', JSON.stringify(objectives));

  // Related topics card — dynamically build clean valid links only
  function buildRelatedTopicsHtml(metaData) {
    const groups = [];

    if (metaData.previousDir && metaData.previousTopic) {
      groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Previous Topic</span><span class="lang-hi">पिछला विषय</span></h3>
          <a href="/upsc/${metaData.subjectDir}/${metaData.parentDir}/${metaData.previousDir}/" class="related-topic-link">
            <i class="fas fa-arrow-left"></i>
            <span class="lang-en">${metaData.previousTopic}</span>
            <span class="lang-hi">${metaData.previousTopicHi || metaData.previousTopic}</span>
          </a>
        </div>`);
    }

    groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Current Topic</span><span class="lang-hi">वर्तमान विषय</span></h3>
          <span class="related-topic-current">
            <i class="fas fa-circle"></i>
            <span class="lang-en">${metaData.name}</span>
            <span class="lang-hi">${metaData.hindiName}</span>
          </span>
        </div>`);

    if (metaData.nextDir && metaData.nextTopic) {
      groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Next Topic</span><span class="lang-hi">अगला विषय</span></h3>
          <a href="/upsc/${metaData.subjectDir}/${metaData.parentDir}/${metaData.nextDir}/" class="related-topic-link">
            <i class="fas fa-arrow-right"></i>
            <span class="lang-en">${metaData.nextTopic}</span>
            <span class="lang-hi">${metaData.nextTopicHi || metaData.nextTopic}</span>
          </a>
        </div>`);
    }

    if (metaData.parentDir && metaData.parentTopic) {
      groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Parent Topic</span><span class="lang-hi">मूल विषय</span></h3>
          <a href="/upsc/${metaData.subjectDir}/${metaData.parentDir}/" class="related-topic-link">
            <i class="fas fa-level-up-alt"></i>
            <span class="lang-en">${metaData.parentTopic}</span>
            <span class="lang-hi">${metaData.parentTopicHi || metaData.parentTopic}</span>
          </a>
        </div>`);
    }

    if (Array.isArray(metaData.childDirs) && metaData.childDirs.length > 0) {
      const childLinks = metaData.childDirs.map((dir, i) => {
        const nameEn = metaData.childTopics?.[i] || dir;
        const nameHi = metaData.childTopicsHi?.[i] || nameEn;
        return `<a href="/upsc/${metaData.subjectDir}/${metaData.parentDir}/${dir}/" class="related-topic-link"><span class="lang-en">${nameEn}</span><span class="lang-hi">${nameHi}</span></a>`;
      }).join('');
      groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Child Topics</span><span class="lang-hi">उप-विषय</span></h3>
          ${childLinks}
        </div>`);
    }

    if (Array.isArray(metaData.similarDirs) && metaData.similarDirs.length > 0) {
      const similarLinks = metaData.similarDirs.map((dir, i) => {
        const nameEn = metaData.similarTopics?.[i] || dir;
        const nameHi = metaData.similarTopicsHi?.[i] || nameEn;
        return `<a href="/upsc/${metaData.subjectDir}/${metaData.parentDir}/${dir}/" class="related-topic-link"><span class="lang-en">${nameEn}</span><span class="lang-hi">${nameHi}</span></a>`;
      }).join('');
      groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Similar Topics</span><span class="lang-hi">समान विषय</span></h3>
          ${similarLinks}
        </div>`);
    }

    if (Array.isArray(metaData.confusedDirs) && metaData.confusedDirs.length > 0) {
      const confusedLinks = metaData.confusedDirs.map((dir, i) => {
        const nameEn = metaData.confusedTopics?.[i] || dir;
        const nameHi = metaData.confusedTopicsHi?.[i] || nameEn;
        return `<a href="/upsc/${metaData.subjectDir}/${metaData.parentDir}/${dir}/" class="related-topic-link confused"><i class="fas fa-question-circle"></i> <span class="lang-en">${nameEn}</span><span class="lang-hi">${nameHi}</span></a>`;
      }).join('');
      groups.push(`
        <div class="related-topic-group">
          <h3><span class="lang-en">Frequently Confused With</span><span class="lang-hi">अक्सर भ्रमित</span></h3>
          ${confusedLinks}
        </div>`);
    }

    return `
  <div class="related-topics-card">
    <h2 class="card-title">
      <i class="fas fa-sitemap"></i>
      <span class="lang-en">Related Topics</span>
      <span class="lang-hi">संबंधित विषय</span>
    </h2>
    <div class="related-topics-grid">
      ${groups.join('\n')}
    </div>
  </div>`;
  }

  html = html.replace('[RELATED_TOPICS_HTML]', buildRelatedTopicsHtml(meta));

  return html;
}

// ============================================================================
// TEST DATA EXTRACTOR
// ============================================================================
function extractTestData(bilingualData) {
  return bilingualData.test || null;
}

// ============================================================================
// 2. REAL SHA-256 CONTENT HASH (v5)
// ============================================================================
/**
 * Production-grade SHA-256 hasher for content.
 * Uses crypto.subtle (browser) or crypto.createHash (Node.js).
 * 
 * @param {string|Object} data - Content to hash
 * @returns {Promise<string>} Hex SHA-256 with "sha256-" prefix
 */
async function generateSha256Hash(data) {
  const json = typeof data === 'string' ? data : JSON.stringify(data);
  const encoder = new TextEncoder();
  const bytes = encoder.encode(json);

  // Browser/Cloudflare Workers: SubtleCrypto
  if (typeof crypto !== 'undefined' && crypto.subtle) {
    const hashBuffer = await crypto.subtle.digest('SHA-256', bytes);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return 'sha256-' + hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  }

  // Node.js: crypto module
  try {
    const nodeCrypto = require('crypto');
    return 'sha256-' + nodeCrypto.createHash('sha256').update(json).digest('hex');
  } catch (e) {
    // Fallback: simple hash (dev only)
    let hash = 0;
    for (let i = 0; i < json.length; i++) {
      hash = ((hash << 5) - hash) + json.charCodeAt(i);
      hash = hash & hash;
    }
    return 'simple-' + Math.abs(hash).toString(16).padStart(8, '0');
  }
}

// ============================================================================
// 3. TAB-LEVEL CACHING (v5)
// ============================================================================
/**
 * Manages per-tab JSON files and the page manifest.
 * Only regenerates tabs whose content has changed.
 * Dramatically reduces API usage.
 * 
 * Directory structure:
 *   upsc/[subjectDir]/[parentDir]/[topicDir]/
 *     index.html              ← assembled page
 *     page.manifest.json      ← per-tab hashes, scores, versions
 *     tabs/
 *       overview.json
 *       concepts.json
 *       visual.json
 *       comparisons.json
 *       practice.json
 *       mains.json
 *       revision.json
 *       test.json
 */
class TabCache {
  constructor(fs, path, baseDir, meta) {
    this.fs = fs;
    this.path = path;
    this.baseDir = baseDir;
    this.meta = meta;
    this.cacheDir = path.join(baseDir, 'upsc', meta.subjectDir, meta.parentDir, meta.dir, 'tabs');
    this.manifestPath = path.join(baseDir, 'upsc', meta.subjectDir, meta.parentDir, meta.dir, 'page.manifest.json');
  }

  /**
   * Gets a cached tab. Returns null if cache miss or hash changed.
   */
  async get(tabName) {
    try {
      const tabFile = this.path.join(this.cacheDir, `${tabName}.json`);
      const manifest = await this.getManifest();
      const stored = manifest?.tabs?.[tabName];

      if (!stored) return null;

      const content = JSON.parse(this.fs.readFileSync(tabFile, 'utf8'));
      const currentHash = await generateSha256Hash(content);

      // Return cached if hash matches
      if (currentHash === stored.hash) {
        return { data: content, hash: currentHash, score: stored.score };
      }

      return null; // Hash changed → regenerate
    } catch {
      return null; // Cache miss
    }
  }

  /**
   * Stores a tab's data to the cache.
   */
  async set(tabName, data, score, hash) {
    try {
      this.fs.mkdirSync(this.cacheDir, { recursive: true });
      this.fs.writeFileSync(this.path.join(this.cacheDir, `${tabName}.json`), JSON.stringify(data, null, 2), 'utf8');
      await this.updateManifest(tabName, hash, score);
    } catch (err) {
      console.error(`[Cache] Failed to store ${tabName}:`, err.message);
    }
  }

  /**
   * Updates the page manifest with a tab's hash and score.
   */
  async updateManifest(tabName, hash, score) {
    const manifest = await this.getManifest() || {
      topicId: this.meta.topicId,
      topicName: this.meta.name,
      subject: this.meta.subject,
      subjectDir: this.meta.subjectDir,
      generatorVersion: VERSION.generator,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      tabs: {},
    };

    manifest.updatedAt = new Date().toISOString();
    manifest.tabs[tabName] = { hash, score, version: VERSION };

    try {
      this.fs.writeFileSync(this.manifestPath, JSON.stringify(manifest, null, 2), 'utf8');
    } catch (err) {
      console.error('[Cache] Failed to write manifest:', err.message);
    }
  }

  /**
   * Reads the current page manifest.
   */
  async getManifest() {
    try {
      return JSON.parse(this.fs.readFileSync(this.manifestPath, 'utf8'));
    } catch {
      return null;
    }
  }

  /**
   * Returns which tabs need regeneration based on hash comparison.
   */
  async getStaleTabs(requestedTabs) {
    const stale = [];
    const manifest = await this.getManifest();

    for (const tabName of requestedTabs) {
      const stored = manifest?.tabs?.[tabName];
      if (!stored) {
        stale.push(tabName);
        continue;
      }
      // Try loading cached data and check hash
      const cached = await this.get(tabName);
      if (!cached) {
        stale.push(tabName);
      }
    }

    return stale;
  }
}

// ============================================================================
// 4. SMART RETRY — Focused regeneration for failed dimensions (v5)
// ============================================================================
/**
 * Analyzes scorer results and returns a focused prompt to fix only
 * the failing dimensions, instead of rebuilding the entire tab.
 * 
 * @param {string} tabName - The tab being retried
 * @param {Object} score - The PageScorer result
 * @param {Object} originalJson - The data that needs fixing
 * @returns {string|null} A focused prompt, or null if general retry needed
 */
function getFocusedRetryPrompt(tabName, score, originalJson) {
  const dims = score.dimensions;
  const issues = [];
  const scope = originalJson.scope || {};

  if (dims.readability < 80) {
    issues.push(`READABILITY: Sentences are too long/short. Rewrite to use 15-25 words per sentence. Break long sentences into shorter ones. Current avg: ${JSON.stringify(originalJson).split(/[.!?]+/).length > 0 ? 'needs improvement' : 'unknown'}`);
  }

  if (dims.duplication < 80) {
    issues.push(`DUPLICATION: Some text appears multiple times. Remove duplicate sentences and rephrase repeated ideas.`);
  }

  if (dims.coverage < 80) {
    issues.push(`COVERAGE: Some sections are too short. Ensure each subsection has adequate content.`);
  }

  if (dims.upscQuality < 80) {
    issues.push(`UPSC QUALITY: Add more UPSC-specific content: exam tips, trap warnings, common mistakes, high-yield facts.`);
  }

  if (dims.hallucinationRisk < 80) {
    issues.push(`HALLUCINATION RISK: Remove content that explains topics outside this microtopic's scope. Stick to: ${JSON.stringify(scope.mustExplain || [])}`);
  }

  if (issues.length === 0) return null;

  return `You previously generated content for a UPSC microtopic, but it needs improvement in these areas:
${issues.map(i => `- ${i}`).join('\n')}

KEEP all existing correct content. Only fix the issues listed above.
Output ONLY valid JSON with the same structure as before.`;
}

// ============================================================================
// 5. GENERATION MANIFEST (v5)
// ============================================================================
/**
 * Creates a generation manifest for the entire page.
 * Enables selective regeneration and provides an audit trail.
 */
function createManifest(meta, tabResults) {
  const tabs = {};
  for (const [tabName, result] of Object.entries(tabResults)) {
    if (result) {
      tabs[tabName] = {
        hash: result.contentHash || 'unknown',
        score: result.score?.overall || 0,
        promptVersion: VERSION.prompt,
        attempts: result.attempt || 1,
      };
    }
  }

  const allScores = Object.values(tabs).map(t => t.score);
  const avgScore = allScores.length > 0
    ? Math.round(allScores.reduce((a, b) => a + b, 0) / allScores.length)
    : 0;

  return {
    topicId: meta.topicId,
    topicName: meta.name,
    subject: meta.subject,
    subjectDir: meta.subjectDir,
    parentTopic: meta.parentTopic,
    parentDir: meta.parentDir,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
    generatorVersion: VERSION.generator,
    translatorVersion: VERSION.translator,
    scorerVersion: VERSION.scorer,
    manifestVersion: VERSION.manifest,
    globalScore: avgScore,
    tabs,
  };
}

// ============================================================================
// 7. PIPELINE LOGGING (v5)
// ============================================================================
let logCounter = 0;

/**
 * Creates a structured log entry for a generation event.
 */
function createLogEntry(event, details = {}) {
  const entry = {
    id: `gen-${Date.now()}-${++logCounter}`,
    timestamp: new Date().toISOString(),
    event,
    ...details,
  };

  // In production: write to file or database
  if (typeof console !== 'undefined') {
    const prefix = `[Pipeline:${entry.id}]`;
    if (event === 'error') {
      console.error(prefix, JSON.stringify(entry, null, 2));
    } else if (event === 'warning') {
      console.warn(prefix, JSON.stringify(entry, null, 2));
    } else {
      console.log(prefix, JSON.stringify(entry, null, 2));
    }
  }

  return entry;
}

// ============================================================================
// 8. GEMINI API CLIENT (v5) — Rate-limited singleton
// ============================================================================
/**
 * Singleton Gemini API client with automatic rate limiting.
 * 
 * Every request automatically waits REQUEST_DELAY ms after completion
 * before the next request is allowed to fire. This ensures that ALL
 * callers (generation, translation, retries, etc.) follow the same rate
 * limit without scattering sleep() calls throughout the code.
 * 
 * Usage:
 *   const client = GeminiClient.getInstance(apiKey);
 *   const text = await client.generate(prompt);
 */
class GeminiClient {
  constructor(apiKey, options = {}) {
    this.apiKey = apiKey;
    this.model = options.model || 'gemini-3.5-flash-lite';
    this.temperature = options.temperature ?? 0.1;
    this.maxRetries = options.maxRetries || 5;
    this.REQUEST_DELAY = options.requestDelay || 13000; // 13 seconds between requests
    this.lastRequestTime = 0;
  }

  /**
   * Gets or creates the singleton instance.
   */
  static getInstance(apiKey, options = {}) {
    if (!GeminiClient._instance || GeminiClient._instance.apiKey !== apiKey) {
      GeminiClient._instance = new GeminiClient(apiKey, options);
    }
    return GeminiClient._instance;
  }

  /**
   * Generates content via the Gemini API with:
   *   - Automatic rate limiting (13s delay between requests)
   *   - Exponential backoff on 429 rate limits
   *   - Retry logic (5 attempts by default)
   *   - Structured logging
   * 
   * @param {string} prompt - The prompt text
   * @returns {Promise<string>} The raw response text
   */
  async generate(prompt) {
    for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
      try {
        const url = `https://generativelanguage.googleapis.com/v1beta/models/${this.model}:generateContent?key=${this.apiKey}`;

        // Enforce rate limit: wait if we're within the REQUEST_DELAY window
        const elapsed = Date.now() - this.lastRequestTime;
        if (elapsed < this.REQUEST_DELAY) {
          const wait = this.REQUEST_DELAY - elapsed;
          await new Promise(r => setTimeout(r, wait));
        }

        const startTime = Date.now();
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 90000); // 90s timeout

        const res = await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: { temperature: this.temperature }
          }),
          signal: controller.signal
        });
        clearTimeout(timeoutId);

        const data = await res.json();
        const duration = Date.now() - startTime;
        this.lastRequestTime = Date.now();

        if (data.error) {
          // If we hit rate limits or quota limits, fallback to gemini-3.5-flash-lite
          if (this.model !== 'gemini-3.5-flash-lite' && (data.error.code === 429 || data.error.message.includes('Quota exceeded') || data.error.message.includes('limit') || data.error.status === 'RESOURCE_EXHAUSTED')) {
            createLogEntry('warning', {
              message: `API limit hit with model ${this.model}. Falling back to gemini-3.5-flash-lite on attempt ${attempt}.`,
              error: data.error.message
            });
            this.model = 'gemini-3.5-flash-lite';
            // Wait slightly and retry immediately with the fallback model
            await new Promise(r => setTimeout(r, 5000));
            continue;
          }

          if (data.error.code === 429) {
            const wait = Math.min(15000 * Math.pow(2, attempt - 1), 60000);
            createLogEntry('warning', {
              message: `Rate limited (429) on attempt ${attempt}`,
              wait,
              duration,
            });
            await new Promise(r => setTimeout(r, wait));
            continue;
          }
          throw new Error(`Gemini API error: ${data.error.message}`);
        }

        if (!data.candidates || !data.candidates[0]) {
          throw new Error(`No candidates in response: ${JSON.stringify(data)}`);
        }

        const text = data.candidates[0].content.parts[0].text;

        createLogEntry('success', {
          tabName: 'api',
          attempt,
          duration,
          responseLength: text.length,
        });

        return text;
      } catch (err) {
        createLogEntry('error', {
          message: err.message,
          attempt,
          maxRetries: this.maxRetries,
        });
        if (attempt >= this.maxRetries) throw err;
        await new Promise(r => setTimeout(r, 5000 * attempt));
      }
    }
  }

  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

// ============================================================================
// 9. COMPLETE GENERATION PIPELINE (v5)
// ============================================================================
/**
 * Orchestrates the full generation flow for a single tab with:
 *   - Tab-level caching (only regenerate stale tabs)
 *   - Smart retry (focused prompts for failed dimensions)
 *   - Quality control validation
 *   - Normalization
 *   - Scoring
 *   - Translation
 *   - Manifest creation
 *   - Pipeline logging
 * 
 * @param {string} tabName - The tab to generate
 * @param {TopicMetadata} meta - Topic metadata
 * @param {Function} callGeminiFn - Function to call Gemini API
 * @param {Function} translateFn - Translation function
 * @param {Object} glossary - Subject-specific glossary
 * @param {TabCache} [cache] - Optional TabCache instance
 * @returns {Object} { data, score, validation, version, contentHash, attempt }
 */
async function generateTab(tabName, meta, callGeminiFn, translateFn, glossary = {}, cache = null) {
  const log = (event, details) => createLogEntry(event, { tabName, ...details });

  // Check cache first
  if (cache) {
    const cached = await cache.get(tabName);
    if (cached) {
      log('cache-hit', { hash: cached.hash, score: cached.score });
      return {
        data: cached.data,
        score: { overall: cached.score },
        cached: true,
        contentHash: cached.hash,
      };
    }
    log('cache-miss', {});
  }

  const maxRetries = 2;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const startTime = Date.now();

    try {
      // 1. Generate prompt (requests bilingual { en, hi } directly)
      const prompt = generatePrompt(tabName, meta);

      // 2. Call Gemini (1 API call)
      const raw = await callGeminiFn(prompt);

      // 3. Parse JSON
      const parsedJson = parseResponse(raw);

      // 4. Validate
      const qc = new QualityControl(meta);
      const validation = qc.validate(tabName, parsedJson);
      if (!validation.passed) {
        log('validation-failed', { errors: validation.errors, attempt });
        if (attempt >= maxRetries) {
          throw new Error(`[${tabName}] Quality gate: validation failed after ${maxRetries} attempts. Errors: ${validation.errors.join('; ')}`);
        }
        continue;
      }

      // 5. Normalize (normalizes both en and hi text)
      const normalized = normalizeContent(parsedJson, glossary);

      // 6. Score
      const scorer = new PageScorer(meta);
      const score = scorer.score(tabName, normalized);

      // 7. Smart retry: if score < 75, try focused fix
      if (!score.passed && score.overall < 75) {
        if (attempt >= maxRetries) {
          log('warning', { message: `Using tab content with score ${score.overall}` });
        } else {
          const focusedPrompt = getFocusedRetryPrompt(tabName, score, normalized);
          if (focusedPrompt) {
            log('smart-retry', { score: score.overall, dimensions: score.dimensions });
            continue;
          }
        }
      }

      // 8. Translate (bypasses translation API calls if already bilingual)
      const bilingual = await translateToBilingual(normalized, translateFn, glossary);

      const duration = Date.now() - startTime;
      const contentHash = await generateSha256Hash(bilingual);

      log('success', {
        attempt,
        duration,
        score: score.overall,
        contentHash,
      });

      // Store in cache
      if (cache) {
        await cache.set(tabName, bilingual, score.overall, contentHash);
      }

      return {
        data: bilingual,
        score,
        validation,
        version: VERSION,
        contentHash,
        attempt,
        duration,
      };
    } catch (err) {
      log('error', { message: err.message, attempt });
      if (attempt >= maxRetries) throw err;
    }
  }
}

// ============================================================================
// 10. BATCH GENERATOR — 1 Call Per Tab for Maximum Quality (v5)
// ============================================================================
/**
 * Generates multiple topics in a single batch.
 * Reuses a single GeminiClient instance and TabCache.
 * Generates each tab in a separate, focused API call for maximum quality.
 * 
 * @param {TopicMetadata[]} topics - Array of topic metadata
 * @param {Object} options - Generation options
 * @param {string[]} [options.tabs] - Specific tabs to generate (default: all)
 * @param {boolean} [options.forceRegenerate] - Skip cache and regenerate all
 * @returns {Promise<Object[]>} Array of results per topic
 */
async function generateBatch(topics, options = {}) {
  const { tabs, forceRegenerate = false } = options;
  const targetTabs = tabs || ['overview', 'concepts', 'visual', 'comparisons', 'practice', 'mains', 'revision', 'test'];
  
  const results = [];
  
  for (const meta of topics) {
    const topicResult = {
      topicId: meta.topicId,
      topicName: meta.name,
      subject: meta.subject,
      tabs: {},
      errors: [],
    };

    // Initialize tab cache for this topic
    const cache = new TabCache(
      require('fs'),
      require('path'),
      process.cwd(),
      meta
    );

    // Determine which tabs need generation
    let tabsToGenerate = targetTabs;
    if (!forceRegenerate && cache) {
      const staleTabs = await cache.getStaleTabs(targetTabs);
      tabsToGenerate = staleTabs;
      createLogEntry('batch-cache-check', {
        topicId: meta.topicId,
        totalTabs: targetTabs.length,
        staleTabs: staleTabs.length,
        cachedTabs: targetTabs.length - staleTabs.length,
      });
    }

    // Generate only stale/missing tabs
    for (const tabName of tabsToGenerate) {
      try {
        createLogEntry('batch-tab-start', { topicId: meta.topicId, tabName });
        const tabResult = await generateTab(tabName, meta, callGemini, translate, {}, cache);
        topicResult.tabs[tabName] = {
          data: tabResult.data,
          score: tabResult.score,
          cached: tabResult.cached || false,
        };
      } catch (err) {
        createLogEntry('batch-tab-error', { topicId: meta.topicId, tabName, error: err.message });
        topicResult.errors.push({ tabName, error: err.message });
      }
    }

    // Assemble final page
    try {
      const bilingualData = {};
      for (const tabName of targetTabs) {
        const cached = await cache.get(tabName);
        if (cached) {
          bilingualData[tabName] = cached.data;
        } else if (topicResult.tabs[tabName]) {
          bilingualData[tabName] = topicResult.tabs[tabName].data;
        }
      }

      const html = assemblePage(meta, bilingualData);
      
      // Write index.html
      const fs = require('fs');
      const path = require('path');
      const pageDir = path.join(process.cwd(), 'upsc', meta.subjectDir, meta.parentDir, meta.dir);
      fs.mkdirSync(pageDir, { recursive: true });
      fs.writeFileSync(path.join(pageDir, 'index.html'), html, 'utf8');

      topicResult.html = html;
      topicResult.success = true;
      createLogEntry('batch-topic-complete', { topicId: meta.topicId, success: true });
    } catch (err) {
      topicResult.success = false;
      topicResult.assemblyError = err.message;
      createLogEntry('batch-topic-error', { topicId: meta.topicId, error: err.message });
    }

    results.push(topicResult);
  }

  return results;
}

// ============================================================================
// 11. SINGLE-TOPIC GENERATOR — convenient wrapper (v5)
// ============================================================================
/**
 * Generates a single topic page.
 * This is the main entry point for CLI usage.
 * 
 * @param {TopicMetadata} meta - Topic metadata
 * @param {Object} options - Generation options
 * @param {string[]} [options.tabs] - Specific tabs to generate
 * @param {boolean} [options.forceRegenerate] - Skip cache
 * @returns {Promise<Object>} Generation result
 */
async function generateSingleTopic(meta, options = {}) {
  const results = await generateBatch([meta], options);
  return results[0];
}

// ============================================================================
// EXPORTS
// ============================================================================
export {
  VERSION,
  SUBJECT_CONFIGS,
  getSubjectConfig,
  DEFAULT_GLOSSARY,
  PROMPT_GENERATORS,
  generatePrompt,
  promptOverview,
  promptConcepts,
  promptVisual,
  promptComparisons,
  promptPractice,
  promptMains,
  promptRevision,
  promptTest,
  normalizeContent,
  translateToBilingual,
  generateContentHash,
  generateSha256Hash,
  QualityControl,
  PageScorer,
  validateMetadata,
  validateSeo,
  generateFaqSchema,
  CROSS_LINK_RULES,
  RELATED_TOPICS_CARD,
  PAGE_TEMPLATE,
  parseResponse,
  cleanUndefined,
  assemblePage,
  extractTestData,
  TabCache,
  GeminiClient,
  getFocusedRetryPrompt,
  createManifest,
  createLogEntry,
  generateTab,
  generateBatch,
  generateSingleTopic,
};
