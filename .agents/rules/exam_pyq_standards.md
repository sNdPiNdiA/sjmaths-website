# Exam PYQs & Practice Player Standards

## 1. Single-Question Quiz Player & SEO Archive Separation
- When creating or modifying interactive MCQ / PYQ practice pages:
  - **Single Question at a Time**: The active quiz viewport must display only the current question with its options, immediate feedback, and explanation.
  - **Collapsed SEO Question Archive**: The full question archive rendered for search engine crawlers MUST be enclosed in `<details class="pyq-seo-details">` without the `open` attribute. Search bots (Googlebot) fully parse and index closed `<details>` content, preventing spoiler leaks for human students.
  - **Namespaced Archive Anchors**: Archive question headings or articles must use namespaced IDs (e.g., `id="seo-q{qNum}"`) so direct hash navigation (`#q{qNum}`) targets the interactive player without jumping past it into the archive.
  - **Smooth Scroll-to-Top**: Navigation triggers (Next/Previous buttons, arrow keys `ArrowLeft`/`ArrowRight`, progress segment clicks, and dropdown jumps) must smoothly scroll the viewport back to the top of the question card.

## 2. Graph & Data Interpretation (DI) Visual Invariants
- Questions involving Line Graphs, Bar Charts, Pie Charts, or Histograms must NEVER omit visual diagrams or use placeholders.
- Always generate clean, inline vector SVGs (`graphSvg`) with exact coordinate grids, markers, labels, and legends, accompanied by structured data tables (`tableData`).

## 3. Exam Shift & Metadata Synchronisation
- When attributing or updating exam shifts (e.g., "7 Sep 2025 · Shift 1"):
  - Update `manifest.json` (`examShifts` array, dates, and shift labels).
  - Update question-level `shift` strings across all subject JSON datasets and consolidated master JSONs.
  - Update `<select id="shiftFilterSelect">` options in build templates.
  - Update hero statistics, total question counts, and shift counts across HTML and JSON-LD schema (`Course`, `FAQPage`).

## 4. Homepage Exam Suite Integration Checklist
- When adding a new exam PYQ bank or module to the website:
  1. **Exam Suite Card**: Add a top-row featured button with category accent color, gradient tint, and question count badge (matching peer cards like UPSC), plus quick-link topic chips.
  2. **Tools Grid**: Add a dedicated tool card in `#tools-section` with metadata chips and accent color.
  3. **FAQ & Schema**: Add corresponding visible FAQ item and JSON-LD `FAQPage` entry.
  4. **Study Tracker**: Register pathname patterns in `assets/js/study-tracker.js` and rebuild `assets/js/study-tracker.min.js`.
  5. **Verification**: Always run `node scripts/audit-seo.cjs` across scopes to guarantee 0 errors and 0 warnings.
