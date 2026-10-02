# SJMaths preservation-first refactor

## Objective

Reduce duplicate implementation and improve build reliability while preserving
the current interface, educational content, public routes and student journeys.
This is a refactor, not a visual redesign. Browser findings already present in
the baseline are recorded separately from regressions introduced by a batch.

## Migration tracker

| Phase | Work | Status | Required evidence |
| --- | --- | --- | --- |
| 1 | Capture representative UI and behaviour | Original routes plus History/Chemistry, PE, GK and Physics variants captured; wider journeys pending | Mobile/desktop, actual light/dark themes, quiz/test/solution/guest interactions |
| 2 | Map page families and source ownership | Initial inventory complete; refine per family | Source/output/consumer inventory |
| 3 | Make builds fail reliably and prepare replacements before writes | Verified in fixtures and full staged artifact | Failure injection, successful artifact and browser comparison |
| 4 | Extract identical CSS by page family | History, 1,630-page UPSC, 368-page ASO, 299-page Mathematics, 307-page Physical Education, 325-page Physics, 152-page SSC-CGL, 200-page Psychology bilingual and 88-page Sociology bilingual and 201-page Music Vocal groups migrated; other groups pending | Preserved cascade, screenshot and content comparison |
| 5 | Extract identical JS by page family | History's 81 four-tab pages, 1,630-page UPSC language bootstrap, 716 Chemistry, 289 Agriculture, 281 English/Geography, 55 bilingual GK topic/language runtimes, 325 Physics and 152 SSC-CGL controllers migrated; 18 SSC-CGL polity tab controllers consolidated; 153 UP Assistant duplicate renderer helpers removed; 87 UPSSSC language bootstraps, 39 Class 9–12 reader controllers and 13 legacy English-only GK runtimes consolidated; other groups pending | Preserved load order, interactions, cleanup and state |
| 6 | Separate generator infrastructure from subject-specific material | History, Chemistry, Agriculture and English renderers separated and fixture-tested; API infrastructure and other generators pending | Fixture equivalence and generated-page browser checks |
| 7 | Consolidate maintained page templates | History, Chemistry, Agriculture and English renderers centralized; other families pending | Content, routes, metadata and UI parity |
| 8 | Organize maintenance scripts and state | Four read-only ASO tools organized with compatibility shims; wider scope pending | All callers resolved and existing npm commands working |
| 9 | Broaden verification coverage | History/Chemistry/Agriculture lifecycle, preservation and offline generation plus UPSC/ASO flow comparisons covered; wider scope pending | Folder scripts, remaining inline scripts and browser journeys |
| 10 | Optimize measured costs and release in batches | Reference-update and batch Git-read optimizations verified; other bottlenecks and delivery pending | Transfer/build measurements and reversible delivery |

## Initial ownership map

- Homepage: `index.html`, `assets/css/home-v2.css`, shared header/footer/search.
- Chapter reader: class-specific HTML/styles/scripts plus `slide-notes` and
  `interactive-notes` assets; preserve hash navigation and reader controls.
- History lessons: `scripts/generate_history.mjs` generates crawlable HTML,
  embedded question data, four tabs and page-specific runtime.
- UPSC: `upsc/upsc-microtopic-template.js` is the maintained generator imported
  by subject/batch entry points. Its exact common style now lives in
  `assets/css/upsc-microtopic.css`; generator exports and prompts stay intact.
  Legacy repair scripts and the old bundled entry point need separate review.
- ASO: 368 rich static lessons share `assets/css/aso-lesson.css`; no maintained
  rich-lesson generator was found in the inspected callers. The root placeholder
  generator uses a distinct style and is not their source of truth. Four read-only
  diagnostics now live in `scripts/aso/`, retaining root compatibility commands.
- Chemistry: `scripts/generate_chemistry.mjs` and
  `scripts/translate_chemistry_hindi.mjs` own the five-tab English/bilingual pages.
  Their pure renderer/compiler now live under `scripts/lib/`; both language modes
  use `assets/js/chemistry-topic.js`. Exact legacy fixtures preserve the compiler's
  inline-injection pipeline via hydration/externalization adapters.
- Agriculture: `scripts/generate_agriculture.mjs` owns the English five-tab
  renderer; `scripts/redesign_all_agriculture.mjs` owns the later runtime variant.
  Pure modules now live in `scripts/lib/`. Both runtime implementations retain
  their existing semantics and are shared at the original script position.
- English and Geography share an exact five-tab interaction controller, but
  maintain separate English/Geography generators and authored subject content.
  The English pure renderer now lives in `scripts/lib/english-compiler.mjs`.
- Exercises/PYQs: retain authored question wording, solution order, mathematical
  rendering and existing solution controls.
- Concept mastery: `learning/engine` and `learning/ui/concept-mastery`, with
  authored topic JSON. Completion and mastery remain distinct.
- Asset build: `build.js`; deployment preparation now compiles inside the copied
  `.pages-dist`. Public asset paths and the existing deployment command remain.
- Browser audit: reuse `scripts/seo-html.cjs` and `scripts/seo-routes.cjs` for
  redirect-aware repository fixtures; local fixtures are not deployment proof.

## Batch rules

1. Inspect sources, generated outputs and consumers before changing them.
2. Capture a browser baseline for the affected family.
3. Apply a small change and compare screenshots, content and interactions.
4. Preserve CSS position, script execution order and public routes.
5. Run targeted checks; expand them when a shared dependency changes.
6. Record verified results and limitations here. Never remove content to reduce
   size and never label a baseline defect a successful refactor.

Artifacts go under ignored `scratch/refactor/`. Commit and deployment are separate
delivery actions; this goal does not automatically publish unfinished batches.

## First batch evidence

- `scripts/capture-refactor-baseline.cjs --label=before` captured 24 screenshots
  and state summaries. History quiz submission, mini-test results, exercise
  solution toggling and the public guest skip were exercised.
- Baseline fixture runs intentionally block service workers and advertising.
  Three contexts logged a service-worker registration error under that setup.
  This does not establish an installed-PWA defect or successful PWA validation.
- Five build tests pass: invalid compilation preserves outputs; successful builds
  update references and are idempotent; dry runs write nothing; preparation and
  commit failures preserve or restore existing assets.
- Build, security and SEO regression checks passed 22 tests in the initial batch.
- Full source build dry run: 7,102 files would change, with no writes. This is
  why the complete build is being tested in a separate deployment artifact.
- Initial staging was interrupted before completion; the artifact verifier
  rejected the incomplete output. The fresh build passed: 11,343 files,
  339 runtime JSON files, zero missing runtime files and no forbidden directories.
- Staged browser comparison: 21/24 screenshots matched exactly. Three screenshots
  had small decorative/timing differences with identical measured state; these
  were visually reviewed, not classified as pixel-identical. Interaction outcomes
  matched and all local requests resolved. Service-worker-blocked fixture errors
  remain a testing limitation (the same registration/update error also appeared
  in the staged desktop homepage context). This artifact predates the History CSS extraction.
- Inventory: 10,454 HTML files, 150 referenced local CSS/JS assets, 166 repeated
  CSS groups and 80 repeated JS groups. These are migration candidates, not proof
  that every block is safe to merge.
- History CSS: extracted one exact 8,658-character stylesheet from 62 pages into
  `assets/css/history-topic.css`, at the original cascade position. Each entire
  HTML body stayed byte-for-byte identical; a repeat migration makes zero changes.
  The next batch migrated the other two History variants separately (63 legacy
  pages and 19 expanded four-tab pages), without merging their cascades. Generator hydration preserves
  shared styles and retains any changed rules inline instead of discarding them.
- History pilot: all four before/after screenshots are pixel-identical; quiz and
  mini-test outcomes match, with zero missing requests and runtime errors.
  Evidence: `scratch/refactor/history-css-pilot/` versus `scratch/refactor/before/`.
- Latest checks: 25 build/style/security/SEO regression tests passed, followed by
  four style tests including generator-CSS equivalence. All 177 non-minified
  scripts passed syntax checks. The 144-page History SEO audit has zero findings.
  Actual AI content generation, installed PWA behaviour and deployment were not tested.
- Current ebook page/PDF edits belong to other ongoing work and are preserved.

## History family batch

- One shared quiz/test runtime now serves all 81 four-tab History pages, at the
  original parser-blocking position after question JSON. Other bytes were preserved.
- The broader browser baseline covers all three style variants: 12/12 screenshots
  match exactly after CSS/JS extraction and after the timer fix. No new runtime
  errors, missing local requests or interaction differences were recorded.
- Browser lifecycle testing found and fixed an existing mini-test timer leak:
  submission now cancels its interval. Both widths pass all seven quiz types,
  keyboard activation, reset/retake, full-mark scoring and timed auto-submission.
- Rendering and schema validation moved out of the CLI into maintained modules.
  Six pre-extraction output hashes (tabs/legacy across all three styles) still
  match. Original generation prompts and content requirements were not changed.
- Regenerating a built page now recognizes minified/versioned design-system and
  navigation references, preventing duplicate assets. Repeat-render tests cover
  one data block, runtime, navigation script, stylesheet and tab shell.
- All 144 pages pass `check-history-preservation.mjs`: no unexpected educational,
  URL, metadata or markup changes compared with HEAD. The History SEO audit has
  zero findings. A synthetic regenerated page was runtime-tested without Gemini.
- Current checks: 20 refactor tests, two browser tests and 30 security/SEO/Three.js
  regression checks passed. All 192 non-minified scripts passed syntax checks.
- Inventory repeated implementation dropped by 950,878 CSS bytes and 366,240 JS
  bytes. This is removed inline duplication, not compressed network transfer.
- Full staged build including these assets passed: 11,351 files, 339 runtime
  JSON files, zero missing runtime files and no forbidden directories. All 12
  staged History screenshots match the baseline exactly, with matching tested
  interactions and zero runtime errors or missing requests. Nothing is deployed.

## Measured build optimization

- Reference updates now detect relevant asset names in one pass before applying
  the existing replacement rules in the same order. Prefix, query, vendor-alias
  and overlapping-name tests preserve compatibility.
- Full-corpus comparison: 10,455 HTML/service-worker files, 666,453,917 source
  bytes and 131 mappings; zero differences from the pre-optimization transform.
  First interleaved measurement: 38.7s versus 6.1s, about 6.3x faster for reference
  transformation CPU only. This is not an end-to-end build-speed claim.
  Repeating the comparison after the overlapping-name compatibility guard still
  produced zero differences: 26.8s versus 4.4s, about 6.1x for the same step.
- The optimized build dry run against `.pages-dist` planned zero writes, proving
  idempotence with the previously compiled artifact. Evidence is under
  `scratch/refactor/build-reference-benchmark.json` and `optimized-staged-dry-run.log`.

## UPSC common-style batch

- Extracted the exact 12,051-byte style block from 1,630 UPSC pages into
  `assets/css/upsc-microtopic.css` at the same cascade position. The maintained
  template imports that link; its full template hash equals the old template
  after only this exact style replacement. No prompts or generator exports changed.
- History and UPSC reuse one exact-style registry rather than duplicate migration
  logic. History's previous output hashes and regression tests still pass.
- `check-upsc-preservation.mjs` compared all 2,396 UPSC HTML pages with HEAD:
  zero unexpected changes to body content, metadata, URLs, data or other markup.
  Repeat migration planned zero writes. Removed 19,631,079 repeated inline CSS bytes.
- Browser auditing now waits for the anonymous auth overlay before choosing the
  public guest skip. The previous one-shot visibility check could capture the
  overlay mid-arrival. Production authentication code was not changed.
- CSS-only comparison: all measured states and guest interactions match; six of
  eight screenshots match exactly. Two small rendering differences were visually
  reviewed. Existing service-worker-blocked errors are not new runtime regressions.
- The expanded flow test exposed an existing mobile overlap: `main.css` applies
  absolute positioning to every nav, including the study footer. A scoped static
  position/inset rule in `competitive-exam-guide.css` fixes the footer without
  changing the main menu; its served minified asset was rebuilt.
- At both widths, keyboard tab selection, all tab content, English/Hindi switching
  and test submission match old-inline versus shared-CSS pages with the footer fix.
  Practice question randomness is fixed only inside the isolated comparison test.
- Checks: 22 refactor tests and the UPSC browser comparison passed; 17 security/SEO
  tests passed. All 198 non-minified scripts passed syntax checks, and the UPSC
  template passed an explicit syntax check. The scoped 2,396-page SEO audit has
  zero errors/warnings and 46 pre-existing low-static-content informational entries.
- Eight post-fix screenshots are under `scratch/refactor/upsc-footer-fixed/`.
  The complete rebuild passed: 11,353 deployment files, 339 runtime JSON files,
  zero missing runtime assets and no forbidden directories. The staged UPSC run
  captured eight screenshots with zero missing requests/runtime errors and matching
  guest interactions/measured state. Seven images match exactly; one dark-mode
  rendering difference was visually reviewed. The combined browser suite passed
  all three History/UPSC checks. Live authentication, PWA and AI generation
  remain unverified. Legacy repair scripts need review before use; they must not
  reinsert old style literals into the shared template.

## ASO style and maintenance pilot

- Extracted the exact 28,171-byte rich-lesson stylesheet from 368 pages into
  `assets/css/aso-lesson.css`, preserving its cascade position. Removed
  10,338,757 repeated inline CSS bytes; this is not compressed transfer savings.
- All 498 ASO HTML pages match HEAD after allowing only that exact replacement.
  A repeat extraction plans zero writes. No questions, formulas, answers, URLs,
  metadata or body markup were rewritten.
- All four mobile/desktop light/dark screenshots match the original baseline
  exactly, with zero missing requests or runtime errors in those local fixtures.
  Evidence: `scratch/refactor/aso-before/` and `aso-after/`.
- Four read-only tools moved into `scripts/aso/`. Root compatibility entry points
  and npm commands preserve their original stdout hashes. Tests run canonical and
  legacy commands from both the repository and a different working directory,
  and verify that the hub is not mutated. Two tools no longer rely on caller cwd.
- Checks: 27 refactor tests, 17 security/SEO regressions and all four combined
  History/UPSC/ASO browser tests passed. All 209 non-minified scripts pass syntax
  checks. The ASO
  comparison covers keyboard tab activation, practice feedback, correct-answer
  scoring, answer review, stopped submission timers and mastery storage at both
  widths. Live countdown text is excluded only from content parity and timer
  cleanup is asserted separately; production timer behaviour is unchanged.
- The 498-page scoped SEO audit has zero errors/warnings and one pre-existing
  low-static-content informational entry. This does not prove topic correctness.
- Baseline findings remain open: the ceiling URL contains propeller/jet content,
  and the representative page overflows by 69px at 390px (0px at desktop), both
  before and after extraction. Correct the topic mismatch only after checking
  curriculum/source ownership; do not silently replace educational material.
- `aso-daymap.cjs` and some older generation/link tools require the absent
  `upsc-aso/topics_v2.json`. They were not migrated or run in write mode. Title
  match and legacy coverage reports are heuristic, not authority to change links.
- The complete staged rebuild passed: 11,355 files, 339 runtime JSON files,
  zero missing runtime assets and no forbidden directories. All four staged ASO
  screenshots match the post-extraction source screenshots exactly, with matching
  measured state and zero runtime errors/missing requests. Evidence:
  `scratch/refactor/aso-staged/` and `aso-artifact-verification.log`. Diff check
  passed. Unrelated ebook HTML/PDF work was preserved. Nothing was committed or
  deployed; this is not authenticated-user or installed-PWA proof.

## UPSC language bootstrap and verification infrastructure

- The identical 1,273-byte language bootstrap now lives in
  `assets/js/upsc-language.js` for 1,630 pages and the maintained template. It
  remains parser-blocking at the original body position. Its SHA-256 is identical
  to the original; the full template hash allows only that exact replacement.
  Removed 2,073,717 repeated source JS bytes, not compressed transfer bytes.
- Before the later UI commits, all 2,396 UPSC pages passed the original-baseline
  preservation comparison; repeat migration planned zero writes. Eight source
  screenshots had matching measured state and no runtime/missing-request errors:
  five were exact, three had 7/31/31 changed pixels in navigation/badge edges.
  These differences were visually reviewed, not automatically accepted.
- That staged snapshot passed: 11,357 files, 339 runtime JSON files, zero missing
  assets and no forbidden directories. Five of its eight UPSC screenshots matched
  the source exactly; three had 53/96/127 changed pixels, with matching state and
  no new errors. Pixel evidence is under `scratch/refactor/upsc-language*pixels.json`.
  This snapshot predates the subsequently committed mobile UI fixes and is not
  current deployment validation.
- `readGitBaseline()` streams raw bytes through one Git process for all three
  corpus checks without changing their comparison policy. UTF-8, binary, empty,
  chunk-spanning, missing/ref-error and cancelled-consumer fixtures pass. The
  100-file read-only comparison had zero byte differences: 5.69s versus 0.305s,
  about 18.6x for this read step. The second reader may benefit from warm cache;
  this is not a whole-build/audit speed claim.
- Pixel inspection is a read-only aid and does not relax screenshot gates.

## Verification after external commits

- `cf08114588` and `41b8e41e51` landed externally and included the earlier refactor
  work. Their mobile/MathJax changes were retained. Earlier statements that work
  was uncommitted describe their batch-time state, not the current Git tree.
- Browser comparisons no longer use mutable HEAD as the old inline implementation.
  They reconstruct inline assets verified against immutable original fingerprints,
  retaining current authored content and the newly committed shared UI fixes.
  This also works in shallow checkouts and cannot silently compare a page to itself.
- The committed build transaction added a copy fallback for rename errors, causing
  the rollback test to fail. The fix retains five bounded EBUSY attempts but throws
  on other/exhausted errors. It never partially copies over served targets and
  reports cleanup failures rather than hiding them. New tests cover retry success,
  exhausted retries/new-output rollback and combined commit/cleanup failures.
- Current verification: 37 refactor tests, 17 security/SEO regressions and all five
  browser tests pass. All 3,038 History/UPSC/ASO HTML pages match `41b8e41e51` after
  the existing migration allowances. All 220
  non-minified scripts pass syntax checks and diff check passes. The refreshed ASO
  fixture still has 69px mobile overflow and no desktop overflow, with zero runtime
  errors or missing requests. Its content/URL mismatch also remains open.
- The next large runtime group is Chemistry (715 pages). Its generator and Hindi
  translator share ownership: the translator injects logic into the inline
  DOMContentLoaded callback. Extracting only the generator would break that
  pipeline; inspect and test both before moving this runtime.
- This continuation has not committed or deployed its verification/build fixes.

## Chemistry runtime and authoring batch

- Migrated 715 bilingual pages and one English-only page to one 9,595-byte
  runtime, keeping parser-blocking execution and the original DOM position.
  Removed 6,548,275 bytes of repeated inline JavaScript before accounting for
  replacement tags/shared assets; this is source duplication, not a measured
  compressed network saving. CSS, educational material and URLs were not changed.
- Separated the English renderer and Hindi compiler/math cleanup into importable
  pure modules. Exact source comparison against `41b8e41e51` verifies all prompts,
  API/status orchestration and moved bodies, allowing only the runtime adapters.
  Full/minimal English and bilingual fixtures match four pre-move output hashes
  after the permitted script replacement. Retranslation adds no duplicate runtime.
- All 718 Chemistry pages pass preservation checks with zero unexpected changes;
  repeat extraction plans zero writes. The scoped SEO audit has zero errors,
  warnings or informational findings. All 41 refactor tests pass.
- Three representative routes at 390/1280px have twelve pixel-identical screenshots
  from immutable inline fixtures to shared source runtime, and twelve more from
  source to the minified staged artifact. Dark captures now click the local theme
  button: earlier system-preference-only captures did not activate this family.
  The corrected evidence is in `scratch/refactor/chemistry-legacy`,
  `chemistry-verified` and `chemistry-minified`. No sampled overflow, browser errors
  or missing local requests were found. These are local fixtures, not live hosting.
- Actual-page flows pass against both source and minified staged assets, covering
  keyboard tabs, language/theme, quiz/PYQ feedback, test scoring, timer cleanup and
  retake. An offline generated bilingual/English fixture also verifies expiry at
  00:00 and no further countdown. No Gemini/API generation was invoked.
- Full staged build passes: 11,411 deployment files, 339 runtime JSON files,
  zero missing runtime dependencies and zero forbidden directories. The build
  compiles only the copied artifact; it does not mutate source/minified checkout
  assets. Nothing was committed, pushed or deployed by this continuation.
- The expanded parallel browser run exposed a test-clock setup defect in ASO:
  its native interval started before Playwright installed its clock. The test now
  installs the clock before navigation and snapshots panel/countdown text in one
  browser task, eliminating a second race between separate text reads.
  No ASO production code was changed.
  Existing ASO mobile overflow/content mismatch remain separate open findings.
- Final combined verification passes: 41 refactor tests, all seven browser tests,
  six security and eleven SEO regressions, syntax checks for 232 non-minified
  scripts, and Git diff whitespace checks. The test-harness edits were also
  individually syntax-checked after the full scan. Live Firebase/auth, installed
  PWA, deployed-origin behaviour and remaining page families are still unverified.

## Agriculture runtime and authoring batch

- The refreshed inventory identified Agriculture as the largest remaining exact
  JavaScript group: 8,191 bytes repeated across 289 pages. Extracted that runtime
  to `assets/js/agriculture-topic.js`, removing 2,367,199 inline bytes before
  replacement-tag/shared-asset overhead. This is duplicate source reduction,
  not a measured compressed transfer saving.
- The generator has a distinct runtime (different quiz selectors, feedback
  classes and scroll offsets). It now shares `agriculture-generated.js` rather
  than silently adopting the redesigned behaviour. Both are exact original
  sources with pinned fingerprints; cross-variant semantic unification is deferred.
- Moved the full pure renderer and existing redesign transformation into
  `scripts/lib/agriculture-renderer.mjs` and `agriculture-redesign.mjs`. A runtime
  hydration adapter lets the existing redesign transform accept the new tags;
  full/minimal fixtures match four pre-move output hashes and repeat transformation
  is idempotent. Source comparison proves prompts, API/status orchestration,
  redesign inventory/write loop and moved bodies are unchanged apart from imports,
  runtime tags/adapters and one obsolete CLI comment.
- Applied only the exact script replacement, never the redesign transformation.
  Educational material, mathematical notation, CSS, metadata and URLs were not
  changed. All 290 HTML pages match `41b8e41e51` after only the permitted runtime
  replacement; repeat migration plans zero writes.
- All 44 refactor tests and syntax checks for 243 non-minified scripts pass.
  Authored-page and offline generated/redesigned browser comparisons pass for
  keyboard tabs, theme, quiz feedback/reset, scoring, timer cleanup, retake and
  00:00 expiry. No API generation or mutating redesign batch was invoked.
- Two source routes at 390/1280px have eight pixel-identical before/after captures
  in real light/dark themes. No sampled overflow, runtime errors or missing local
  requests were found. Evidence: `scratch/refactor/agriculture-before` and
  `agriculture-after`. These fixtures exclude advertising and disable service
  workers; they are not production/authentication proof.
- All eight combined browser regressions pass. The 290-page Agriculture SEO audit
  has zero errors, warnings or informational findings. Git diff checks pass.
- The full staged build passes its scope/runtime gate: 11,415 files, 339 runtime
  JSON files, zero missing runtime dependencies and zero forbidden directories.
  Actual-page flows also pass against minified staged assets. Eight staged
  screenshots match source captures pixel-for-pixel; evidence is in
  `scratch/refactor/agriculture-staged` and `agriculture-staged-browser.log`.
- Rechecked all 4,046 HTML pages across History, UPSC, ASO, Chemistry and Agriculture
  against `41b8e41e51` with each family's existing exact migration allowances:
  zero unexpected changes. This proves preservation, not correctness of all
  pre-existing educational material or live hosting behaviour.
- Nothing was committed, pushed or deployed by this continuation. Remaining
  families, authentication, PDF/search and installed-PWA journeys still prevent
  calling the overall refactor or release complete.

## English/Geography exam-topic runtime and compiler batch

- The duplicate audit found the same 6,926-byte DOM-ready controller in 65 English
  and 216 Geography pages. Extracted it to `assets/js/exam-topic.js` at each
  original parser-blocking position. The generators now refer to the shared
  controller; subject prompts and the complete Geography generator remain in
  their respective files. The English pure compiler is importable from
  `scripts/lib/english-compiler.mjs`.
- Fixture hashes for complete and minimal English examples match output captured
  before the move. They retain five server-rendered tabs, 20 quiz questions, six
  PYQs, ten test questions, explanations and year labels. The authoring proof
  confirms the entire English compiler body and Geography generator are intact,
  while English prompts and API/status orchestration are unchanged.
- Applied the exact runtime replacement to 281 pages. All 348 English and
  Geography pages match `41b8e41e51` under that single allowance. A second
  migration run plans zero writes. Keyboard tab selection, theme, quiz/PYQ feedback,
  timed score, retake and stopped countdown passed in English and Geography,
  compared inline and shared runtimes at 390/1280px.
- Source and staged screenshot sets each contain twelve views: three representative
  routes at 390/1280px in both themes. Source-to-source and source-to-minified
  comparisons each show zero pixel differences, browser errors or missing local
  requests. Evidence is under `scratch/refactor/exam-topic-{before,after,staged}`.
- Staged build and artifact gate pass: 11,800 files, 339 required runtime JSON
  files, zero missing runtime dependencies and zero forbidden directories.
  The built English/Geography flow also passes against the minified asset.
- Scoped SEO audit found no errors or warnings in 65 English and 283 Geography
  pages; 37 Geography pages have informational low-static-content notices.
  All 47 refactor tests, 280 script syntax checks, six security regressions and
  twelve SEO regressions pass. The browser command now runs its page tests
  sequentially; all nine tests passed, including the English/Geography flow.
  Parallel runs timed out when competing with staging and other browsers, and a
  History timer assertion drifted under that load. Sequential verification removed
  those failures without changing the page runtimes.
- A fresh 10,822-page duplicate inventory puts the next JavaScript group in 94 ASO
  ASO topic pages spanning multiple subject groups: two scripts of 13,134 and
  5,611 bytes each. No independent page generator owns these static pages; the
  controllers were extracted only after fingerprint and order checks on all 94.

## ASO topic feedback and tab runtime batch

- Extracted the exact legacy `universal-quiz-feedback` and `universal-tab-engine`
  classic scripts to `assets/js/aso-topic-feedback.js` and
  `assets/js/aso-topic-tabs.js`. Original parser-blocking order is retained at each
  page's original script location. Fingerprints are fixed in the one-time extractor;
  variants and attributed scripts are deliberately not rewritten.
- Replaced the two scripts in 94 ASO topic pages. All 498 ASO pages match `HEAD`
  after allowing only these exact replacements; the dry run now reports zero
  additional writes. Estimated repeated inline source removed: 1,743,285 bytes
  (about 1.74 MB).
- Browser parity passed for the mega-test and a standard Structures topic at 390
  and 1280px: all five tab activations, quiz feedback DOM, overflow and missing
  local requests match between inline and external scripts. A pre-existing
  `MathJax.typesetPromise is not a function` error occurs on the Structures page
  in both versions; it comes from other inline page code, not these controllers.
- Baseline captures are under `scratch/refactor/aso-topic-before/`; post-change
  captures and the strict report are under `scratch/refactor/aso-topic-after/`.
  The only screenshot-hash deltas were two 30x14px bottom-right transient pixels
  in the mega-test at 1280px, while its recorded full-page height also varied by
  50px between runs. This is asynchronous page rendering; no content/layout
  change was observed in the viewport. Diff evidence is retained for review.
- Full local gates pass: 49 refactor tests, 288 JS syntax checks, six security
  tests, twelve SEO regressions, ten serialized browser tests, and ASO SEO with
  zero errors/warnings (one informational notice). The staged minified ASO pages
  also pass the same 390/1280px flow comparison.
- The staged artifact gate exposed and now covers a build defect: custom staged
  builds copied the existing `.pages-dist` into the new output. The copy step now
  excludes that prior artifact without touching it. Rebuilt staging passes at
  11,918 files, preserves all 339 required runtime JSON files, has no missing
  dependencies or forbidden directories, and stays below the 20,000-file cap.
- Screenshots and strict comparison are under `scratch/refactor/aso-topic-before/`
  and `aso-topic-after/`. Two 1280px mega-test screenshots differ only in a
  30x14px bottom-right transient region; the recorded page height varied 50px
  across runs. The browser flow/content parity passes, but that screenshot hash
  comparison remains flagged for visual review rather than being called pixel
  identical. No live deployment or educational-content correctness is implied.

## Hindi topic runtime and generator ownership batch

- Confirmed the exact 8,210-byte script in `scripts/generate_hindi.mjs` and 102
  generated HTML pages; six Hindi pages use other variants and were not edited.
  Extracted the controller to `assets/js/hindi-topic.js` and updated the owning
  generator to interpolate its shared parser-blocking script tag. Subject prompts,
  API orchestration, authored content, URLs and the six alternate pages remain
  outside the change.
- The exact-only migration is repeatable: the first pass changed 102 pages and
  the generator; the next dry run changed zero. All 108 Hindi HTML pages match
  `HEAD` after allowing only the shared runtime substitution.
- Browser parity passed on representative Language and Grammar topics at 390px
  and 1280px through all five tabs, dark-mode toggle, quiz feedback and reset,
  PYQ feedback, timed-test start/submit/stop and retake. No browser errors,
  missing local requests or horizontal overflow. Before/after screenshot hashes
  match for both routes, widths and themes (`scratch/refactor/hindi-topic-{before,after}`).
- The generator source was untracked before this task; its edit is limited by the
  exact migrator's source normalization check. No Gemini generation/API calls were
  made. Full local gates pass: 52 refactor tests, 295 JavaScript syntax checks,
  six security tests, 12 SEO regressions, and all 11 serialized browser tests.
- Hindi SEO has zero errors/warnings and six informational low-static-content
  notices. The staged minified flow also passes. Its artifact has 12,050 files,
  preserves all 339 runtime JSON dependencies, and has no missing files or
  forbidden directories. Before/after screenshots are pixel-identical on both
  representative routes, at both widths and themes. Nothing was deployed.

## Next batches

1. Physical Education, bilingual GK, Physics, SSC-CGL and Psychology bilingual
   shared-asset migrations are complete. Preserve the 13 distinct GK runtime
   variants; inspect further candidates with their generators and post-processing
   owners before extraction.
2. The latest source inventory covers 11,066 HTML files, 160 repeated CSS groups
   (16,292,447 repeated bytes) and 201 repeated JavaScript groups (1,144,545
   repeated bytes). The largest exact CSS group is 1,930 bytes across 590 pages,
   but it spans four roots (Art, UP-PGT Biology, Civics and Education), so inspect
   each writer before deciding whether it is genuinely one reusable family. The
   largest remaining exact JS candidate is a 2,743-byte SSC-CGL policy-page
   interaction controller across 18 pages. Inspect its generated question counts,
   page writer and relationship to `ssc-cgl-topic.js` before extraction. Keep
   pre-existing defects such as the ASO MathJax baseline error separate.
3. Separate API retry/status infrastructure only where actual callers can share
   it without changing subject prompts or content requirements.
4. Organize maintenance entry points after identifying package/CI/documentation
   callers; preserve public URLs and supported commands.
5. Broaden auth, PDF, search, responsive and installed-PWA runtime coverage before
   considering the site-wide refactor or any release complete.

## Hindi Music Vocal topic runtime and generator ownership batch

- Confirmed the exact 3,790-byte controller (`sha256
  26d8db13a02c69d92cd43f052385bb14179cbc99ff348c46d37b59b1cf226125`) in the
  tracked `scripts/generate_music_vocal_hi.mjs` and all 201 generated topic
  pages. The pages have differing quiz lengths and answer-type combinations;
  only the identical controller was externalized, preserving each page's
  educational content, JSON data, styles, URLs and script position.
- The exact-only migration is repeatable: first pass changed 201 pages and the
  generator; the next dry run changed zero. Git-baseline comparison reports no
  unexpected changes across the 201 pages or generator.
- Browser parity passed at 390px and 1280px for keyboard tab selection, MCQ,
  fill-in and short-answer feedback, manual test scoring, timed auto-submit,
  overflow and inline/external runtime errors. Before/after screenshots match
  exactly at both widths; both captures reported zero missing local requests.
- No generator prompts, API calls or authored content were changed. No pages
  were generated, deployed or pushed.
- The refreshed repository inventory has 11,065 HTML files, 223 repeated inline
  JavaScript groups (3,727,165 repeated bytes), and 167 repeated CSS groups
  (28,451,013 repeated bytes). These are candidates only; inspect ownership and
  page behavior before further extraction.

## Hindi Music Instrumental topic runtime and feedback-state fix

- Confirmed the 5,333-byte legacy controller (`sha256
  56e09a65d8c304716a236287e3f81942626838914a8c1bb739a8b8729f61c1f0`) in the
  tracked `scripts/generate_music_instrumental_hi.mjs` and all 125 generated
  pages. Their tab shell and controls are consistent; quiz/test item counts
  vary, and all page-authored data was preserved.
- During browser review, confirmed feedback was being inserted but stayed
  hidden because the existing stylesheet requires `.quiz-feedback.show`. The
  shared controller now adds that state class; this makes MCQ, fill-in,
  short-answer and submitted-test explanations visible without changing the
  established styles or page layout.
- The migration is idempotent and Git-baseline comparison reports zero
  unexpected page changes. The only content-independent exception is the
  exact legacy controller fingerprint replaced by the shared script reference
  and its targeted feedback-state correction.
- Browser checks at 390px and 1280px cover keyboard tabs, visible quiz feedback,
  theme switching, manual scoring, retake, timed auto-submit and overflow.
  Staged/minified checks pass; before/after initial-state screenshots match at
  both widths, with zero browser errors or missing local requests.
- Full local gates pass: 58 refactor tests, 307 JavaScript syntax checks and a
  125-page SEO audit with zero errors/warnings. Staged output contains 12,060
  files and all 339 runtime JSON dependencies; nothing was deployed or pushed.
- Before the next extraction, the inventory showed 11,066 HTML files, 214
  duplicate JavaScript groups (2,728,330 repeated bytes), and 170 duplicate CSS
  groups (28,497,305 repeated bytes). The next JavaScript candidate was a
  5,598-byte controller in 55 UP TGT/PGT GK pages, but ownership inspection found
  a separate bilingualization pass mutates that runtime after generation. Do not
  extract it until the bilingual data/runtime contract is handled as one pipeline.

## Military Science topic runtime and generator ownership batch

- Confirmed the exact 7,224-byte controller in the tracked
  `scripts/generate_military_science.mjs` and all 46 generated topic pages.
  Externalized only that shared runtime to `assets/js/military-science-topic.js`
  and updated the owning generator; page-authored data, question distributions,
  styles, URLs and script position were preserved. The browser audit also found
  feedback markup was hidden by the established `.quiz-feedback.show` style;
  the shared controller now emits that required state class.
- `check-military-science-preservation.mjs` reports 46 pages and zero unexpected
  changes against `HEAD`. The exact migrator is idempotent; its regression tests
  cover round-trip, generator ownership, and preservation of edited/attributed
  variants. No content-generation API calls or page regeneration were performed.
- Source and staged browser parity passed at 390px and 1280px for all seven quiz
  types, keyboard tab activation, feedback visibility, theme switching, manual
  scoring, test submission, retake, timed auto-submit and horizontal overflow.
  Inline/external outcomes match with no page errors or missing local requests.
- Staged Pages artifact verification passed: 12,062 files, all 339 runtime JSON
  files present, zero forbidden directories. The scoped 46-page SEO audit has
  zero errors, warnings or informational findings. The full 61-test refactor
  suite passed. Nothing was deployed or pushed.

## Mathematics shared stylesheet batch

- Extracted the exact 15,125-byte stylesheet shared by all 299 Mathematics topic
  pages into `assets/css/mathematics-topic.css`; the generator now emits its
  shared stylesheet link at the original cascade position. Only the exact style
  block and generator import/reference were changed; each page's body is
  unchanged, and the second dry run planned zero page or generator changes.
- This removes 298 redundant inline copies (4,507,250 source CSS bytes). The
  refreshed whole-site inventory now reports 11,066 HTML files, 211 duplicate
  JavaScript groups (2,720,394 repeated bytes), and 164 duplicate CSS groups
  (23,697,803 repeated bytes).
- Browser pixel comparisons passed exactly at 390px and 1280px in light and dark
  themes, both against source CSS and the staged minified/cache-busted CSS. No
  page errors or missing local requests were recorded. An existing 187px
  horizontal overflow at 390px on the representative Mathematics page is equal
  before/after extraction and remains a separate baseline issue.
- Checks: 64 refactor tests, 318 non-minified JavaScript syntax checks, all three
  Mathematics extraction tests, and source/staged browser parity passed. The
  staged artifact contains 12,068 files, all 339 runtime JSON dependencies, and
  no forbidden directories. The current 299-page SEO audit reports existing
  content/link/schema findings that were not changed by this CSS-only migration;
  triage them separately. Nothing was deployed or pushed.

## Physical Education bilingual shared stylesheet batch

- Traced the 10,765-byte repeated stylesheet to the maintained Hindi translation
  renderer, not the English generator: the generator emits a distinct 8,623-byte
  English style and is intentionally unchanged. The exact bilingual style occurs
  on 307 lesson pages; 15 hub styles and one English lesson variant are retained.
- Extracted the shared style to `assets/css/physical-education-topic.css` and
  changed the translator to reference it at the same head position. Exact-only
  migration leaves every page body unchanged and does not touch the 16 other
  variants. Expected source CSS removal is 3,294,090 bytes (306 redundant copies).
- `check-physical-education-preservation.mjs` compares all 323 lesson/index pages
  and the translator against `HEAD`: 307 expected stylesheet substitutions, 16
  byte-for-byte untouched variants, and no other changes. The second migration
  dry run planned zero writes.
- Browser parity passed at 390px and 1280px for inline versus external CSS in
  English and Hindi, keyboard-operated language selection, keyboard answer reveal,
  screenshot pixels and horizontal-overflow parity. No runtime errors or missing
  local requests. The before-change capture is `scratch/refactor/pe-before/`;
  state-specific screenshots are `scratch/refactor/physical-education-styles/`.
- The English generator still owns its distinct stylesheet and can overwrite a
  bilingual page when explicitly run; this remains existing pipeline behavior.
  Translation generation/API calls, deployment and live hosting were not tested.

## UP TGT/PGT GK bilingual runtime and generator batch

- Traced the shared 5,599-byte runtime across 55 bilingual topic pages. The
  bilingualizer had been rewriting quiz selection and Hindi feedback strings
  inside that runtime; the shared runtime now reads the existing bilingual JSON
  payload itself, supporting English-only generated pages when that payload is
  absent and Hindi as the translated-page default.
- Moved the runtime to `assets/js/up-tgt-pgt-gk-topic.js` and updated the owning
  generator to emit a parser-blocking script link at the original location.
  Also moved the identical 1,114-byte bilingual language bootstrap to
  `assets/js/up-tgt-pgt-gk-language.js` at its original body position. The
  bilingualizer verifies the shared topic runtime and keeps language-specific
  quiz/test content in its existing data block rather than patching script text.
  The unused generator-only `typeNames` and `letters` runtime declarations were
  removed; HTML question labels remain generated by their existing renderer.
- Exact fingerprint migration changed the runtime reference on 55 bilingual
  pages. Preservation comparison against the refactor baseline finds 55 expected
  substitutions and 20 untouched pages, including all 13 distinct runtime
  variants. The generator differs only by the shared import/reference.
- Browser parity passed against the inline baseline at 390px and 1280px: initial
  Hindi pixels, keyboard language switch to English, quiz feedback, test score,
  theme control and overflow match. No page errors or missing local requests.
- Repeated source and staged captures match exactly for the GK route at 390px and
  1280px in both themes. The staged-browser test loads the actual `.pages-dist`
  HTML and minified/cache-busted scripts; keyboard language/tab activation, quiz
  feedback, test scoring, theme switching and English-only generator output pass.
  The GK route reports zero runtime errors, missing local requests or overflow.
- Checks: all 71 refactor tests and 330 non-minified JavaScript syntax checks pass.
  The staged Pages artifact contains 12,074 files and all 339 required runtime
  JSON files, with zero missing runtime files or forbidden directories. No
  translation/model API calls or deployment were performed.

## Physics topic stylesheet and interaction runtime batch

- The fresh inventory found the same 3,882-byte stylesheet and 863-byte tab/quiz
  controller in exactly 325 Physics topic pages. Their page sets match, and the
  canonical page blocks match the maintained `scripts/generate_physics.mjs`
  template exactly. No unrelated Physics variants were included.
- Extracted the stylesheet to `assets/css/physics-topic.css` and the parser-blocking
  controller to `assets/js/physics-topic.js`, preserving each original cascade and
  execution position. The generator emits those same references. The exact-only
  migration changes no notes, formulas, questions, answers, URLs or page body
  content beyond replacing the controller tag.
- `check-physics-topic-preservation.mjs` compares all 325 pages and the generator
  against the committed pre-migration baseline; all expected substitutions match
  and there are no other differences. A repeat extraction dry run produces zero
  writes. The source before/after screenshots and measured states match exactly at
  390px and 1280px. Keyboard tab activation, quiz answer reveal and test answer
  reveal pass with zero page errors, missing local requests or horizontal overflow.
- Staged/minified browser flow and screenshots also match source exactly at both
  widths. The complete Pages artifact has 12,078 files, all 339 required runtime
  JSON files, zero missing runtime files and no forbidden directories. The scoped
  SEO audit reports zero errors, warnings or informational findings across 325
  Physics pages. All 74 refactor tests and 336 non-minified JavaScript syntax checks
  pass. Nothing was deployed.
- The post-migration read-only inventory covers 11,066 HTML files, 162 duplicate
  CSS groups (19,145,945 repeated source bytes), and 208 duplicate JavaScript
  groups (2,078,334 repeated source bytes). This was the pre-Physics/SSC/Psychology
  inventory; the refreshed current counts are recorded under Next batches below.

## SSC-CGL shared topic assets batch

- Inspected all 322 SSC-CGL topic pages and the directory/SEO repair callers. The
  exact 6,082-byte stylesheet and 1,784-byte controller occur together in 152
  lessons (Computer Knowledge, English, Finance/Economics, General Awareness and
  Reasoning); 170 other SSC-CGL pages are intentionally untouched. No lesson
  generator owns these particular topic pages, and the directory/SEO repair tools
  do not rewrite their assets.
- Extracted the shared CSS and parser-blocking JavaScript at their original
  positions. The script persists checklist state and scrolls the active subject
  navigation into view; the current 152 pages contain no checklist checkbox
  markup, so persistence remains dormant there. Exact preservation checks confirm
  only the two intended inline blocks changed; a repeat dry-run makes no writes.
- The 77 refactor tests, 342-file JavaScript syntax check, and SSC-CGL SEO audit
  pass (322 pages; zero SEO errors/warnings). The complete Pages build passes at
  12,082 files with all 339 runtime JSON files and no forbidden directories.
  Browser checks against the built/minified artifact pass across five subjects,
  mobile/desktop widths, screenshots, active-nav state and keyboard navigation.
- Source screenshots were visually aligned and computed layout/style values
  matched. One strict source PNG-hash comparison reported sparse text-edge
  rasterization differences (1,768 pixels, max channel delta 64, mean 0.0143);
  a subsequent source rerun ended with a transient destroyed browser context while
  awaiting fonts. The source screenshot comparison is therefore not yet conclusive;
  retain it as a follow-up verification item even though the built-artifact
  comparison passes. Nothing was deployed.

## Psychology bilingual stylesheet batch

- Fresh inventory showed an exact 10,178-byte stylesheet in 200 of 218
  Psychology pages. The other 18 English-only pages use a distinct 9,135-byte
  stylesheet and remain byte-identical. Inspected both writers: the English
  generator owns the separate variant; `translate_psychology_hindi.mjs` emits the
  exact shared bilingual CSS. Its output now requires an exact match before the
  shared stylesheet reference is written; no translation/API generation was run.
- Extracted the bilingual stylesheet into `assets/css/psychology-bilingual-topic.css`.
  The preservation check confirms exactly 200 CSS-only substitutions and 18
  untouched pages; rerunning the extractor yields zero writes. The educational
  text, bilingual controls, questions, answers and page URLs are byte-preserved.
- Validation: 81/81 refactor tests; all 347 non-minified JavaScript files pass
  syntax; browser comparison passes at 390px and 1280px for a bilingual lesson
  and an untouched English-only variant. The bilingual keyboard language switch
  and answer reveal work, geometry matches, and screenshots are pixel-identical.
  The Pages artifact passes at 12,084 files with all 339 runtime JSON files and
  zero missing/forbidden paths. Scoped SEO remains at 218 indexable pages with
  zero errors, but reports 291 warnings (88 extreme titles, 200 H1 warnings on
  bilingual pages and three extreme descriptions); these are outside this CSS
  change and were not altered. Nothing was deployed.

## UP Assistant Teacher duplicate tab-listener removal

- The 1,031-byte script was duplicated by reference in 153 of 264 UP Assistant
  Teacher topic pages. It toggled `.tab-panel` elements, but those pages render
  their tab content dynamically; `assets/js/upsc-renderer.js` already owns the
  delegated tab click, active/ARIA state and content rendering. Removed only the
  exact duplicate inline/external script from the 153 pages and discarded the
  untracked shared asset created during the earlier extraction attempt. The
  other 111 pages remain byte-identical.
- Preservation compares all 264 pages to baseline `237db669da5fca0a8ff8ae6a5a601d284a367642`;
  the removal checker confirms 153 exact removals, 111 untouched pages, and a
  second dry run with zero writes. Browser parity covered nine subject families
  at 390px and 1280px: screenshots were pixel-identical, keyboard activation of
  each tab and dynamically rendered content matched, and no new page errors or
  missing local assets occurred. The existing blocked-service-worker console
  diagnostic was filtered as a known test-environment issue. `npm run
  refactor:test` passed 88 tests. Pages artifact verification passed at 12,086
  files with all 339 runtime JSON files and no missing/forbidden paths. Nothing
  was deployed.

## UPSSSC PET bilingual language bootstrap reuse

- An exact 1,129-byte language bootstrap appears in 87 of 106 UPSSSC PET topic
  pages. Its source hash is pinned; after normalization it is equivalent to the
  existing 1,273-byte UPSC language runtime. Replaced only those inline blocks
  with the already-owned parser-blocking `upsc-language.js` reference and its
  existing `data-upsc-shared-script="language"` marker. No new served asset was
  introduced. The remaining 19 pages are byte-identical.
- Baseline comparison confirms 87 exact replacements and 19 untouched pages; a
  repeated dry run makes zero writes. Browser parity passed for Economy, History,
  English and General Awareness at 390px and 1280px: English/Hindi preference,
  body/document language classes, ARIA state, stored preference, layout geometry
  and page text all match. Source and staged artifact screenshots are pixel-
  identical. `npm run refactor:test` passed 88 tests; the Pages artifact verifies
  at 12,086 files with all 339 runtime JSON files and no missing/forbidden paths.
  Nothing was deployed.

## Class 9–12 chapter-reader tab controllers

- The exact 3,216-byte controller appeared in 25 Class 9, Class 11 and Class 12
  chapter pages. Its controls and iframe panel are intentionally hidden by the
  existing notes-first layout; the HTML handlers remain supported and were
  exercised directly. No matching page generator was found in the repository.
- Replaced only the exact inline blocks with a parser-blocking shared script;
  58 other pages in the scanned class scope stayed byte-identical. Preservation
  checks passed and a repeated dry run planned zero writes. Desktop dropdown,
  mobile drawer, resource selection and return-to-notes behavior passed in the
  source and staged artifact. No new runtime errors or missing local assets were
  recorded.
- Screenshot PNG comparisons were not stable across repeated page loads: several
  baseline/shared pairs varied in rendered vertical spacing despite unchanged
  HTML outside the controller substitution and matching measured interactions.
  The run therefore does not claim pixel-identical UI parity; retain a deterministic
  capture follow-up before treating visual parity as fully proven.

## Class 10 chapter resource-tab controller

- The exact 5,124-byte controller (SHA-256
  `dda062413b76f5544b29481980ac18b7d0e6d563674cf0aa12e8c61b411a3065`) appeared
  in all 14 Class 10 chapter-note pages. Its chapter-shell hiding and same-origin
  iframe header/footer/height handling differ from the Class 9/11/12 controller,
  so it remains a separate runtime variant. No maintained page generator was
  found in scripts or package commands.
- Exact extraction changed only those 14 script blocks; one additional Class 10
  index page was unchanged. The baseline preservation checker passed and a repeat
  dry run planned zero writes. Browser tests passed at 390px/1280px: the notes-first
  initial state and hidden desktop/mobile resource UI matched, and direct handler
  flows verified dropdown outside-click, drawer open, iframe selection and return
  to notes. Initial source screenshots differed by 0 mobile pixels and 1 desktop
  pixel (visually indistinguishable); the minified staged screenshots are pixel-
  identical at both widths. The full staged build passed at 12,090 files, all 339
  required runtime JSON files present, with no missing assets or forbidden paths.

## Legacy English-only GK runtime reuse

- Thirteen older GK history/polity pages contain the same 5,069-byte controller
  (5,070 raw script bytes; SHA-256
  `a3c816f143fdd5d32ad182c74893c0ed31b2d53d18b0e42bd5b3b23c032b319e`). The
  maintained generator already uses the bilingual-capable `up-tgt-pgt-gk-topic.js`
  runtime, whose English fallback supports pages without bilingual data.
- Replaced only those 13 exact inline blocks with the existing shared parser-
  blocking runtime reference; no asset or content generator was added. Baseline
  comparison covers all 75 GK pages (13 substitutions, 62 untouched), and repeat
  dry run plans zero writes.
- Source and minified staged browser checks pass at 390px/1280px for representative
  history and polity lessons. They set a stored Hindi preference to confirm the
  English-only pages still render in English, then exercise keyboard quiz tabs,
  answer feedback, disabled answered options and test submission/scoring. Initial
  screenshots are pixel-identical; no browser errors or missing local assets were
  recorded. The staged deployment artifact passes at 12,090 files with all 339
  runtime JSON files, zero missing runtime files and zero forbidden directories.

## SSC-CGL polity tab-controller consolidation

- The same 1,171-byte `openTab`/initial-hash/pageshow controller appeared in 18
  policy-polity lessons. Moved only those exact blocks to
  `assets/js/ssc-cgl-policy-tabs.js`; the six other pages in that directory were
  left unchanged. The existing progress and mini-test runtimes remain separate.
- The full 24-page preservation comparison passes after composing the three
  exact runtime substitutions. A repeat dry run plans zero writes.
- Browser comparison covers citizenship and Parliament at 390px and 1280px:
  hash-selected tab, keyboard Enter activation, pageshow restoration, no overflow,
  zero missing local assets or runtime errors, and pixel-identical initial screenshots.
  The existing SSC-CGL polity progress browser test also passes.
- The complete staged artifact passed: 17,206 files, all 339 required runtime JSON
  files present, zero missing runtime assets and no forbidden directories. Staged
  browser comparisons also pass at both widths with pixel-identical screenshots.
- `npm run refactor:test` passes 95/96 tests. Its one unrelated worktree failure is:
  `ahc-ro-aro/computer-knowledge/cpu-architecture-registers/index.html` has three
  AHC language runtime references versus one at the baseline. That modified page
  was not changed in this batch.

## Sociology bilingual shared-style batch

- Extracted the exact 10,169-byte bilingual Sociology stylesheet (SHA-256
  `21aaa88b15d81fffda23da5d03c80fc7312166c522dfd00f48efb8bc3509d27d`) into
  `assets/css/sociology-bilingual-topic.css`. Only the Hindi translator owns this
  repeated bilingual variant; the English-only generator's distinct style was
  left unchanged.
- Replaced only this exact style in 88 bilingual topic pages, at its original
  cascade position. The other 18 Sociology pages stayed identical after line
  ending normalization. The translator now externalizes its exact template style
  before writing and fails closed if that expected style changes.
- Repeat dry run plans zero writes. Targeted tests cover the source fingerprint,
  exact/idempotent conversion, minified-link hydration, and translator wiring.
  Playwright source and staged-artifact comparisons at 390px and 1280px are
  pixel-identical for Association and Caste System; keyboard Hindi switching and
  answer reveal pass with no horizontal overflow, new browser errors or missing
  local assets. Evidence is under `scratch/refactor/sociology-bilingual-style/`.
- The full staged build passes at 17,208 files with all 339 required runtime JSON
  files, zero missing runtime assets and no forbidden directories. The current
  `npm run refactor:test` run passes 98/99; the sole failure remains the unrelated
  AHC duplicate language-runtime reference described above. Gemini translation
  API generation was not invoked.

## Music Vocal shared-style batch

- The 201 topic pages and `scripts/generate_music_vocal_hi.mjs` contained the
  same 3,104-byte stylesheet (SHA-256
  `3cd6b57667f17ee0865df79252dee6fdf4d52e08868cd6180a9b06a5f7699a9b`). It now
  lives in `assets/css/music-vocal-topic.css`, at the original cascade position.
  The generator imports the same reference. Full generator comparison permits
  only that style substitution and its import; prompts and API behavior match
  the checkpoint.
- All 201 pages pass preservation checks, and repeated migration plans zero
  writes. Source and compiled-artifact Playwright checks at 390px and 1280px
  compare all four tab screenshots exactly, plus keyboard tabs, MCQ/fill/short
  answer feedback, manual scoring and timed submission. No missing local assets
  or new runtime errors were recorded. Evidence is under
  `scratch/refactor/music-vocal-styles/`.
- The full staged build passed at 17,214 files with all 339 required runtime JSON
  files and no missing runtime assets or forbidden directories. The AHC repair
  below was subsequently applied to its compiled page, then artifact verification
  passed again. These checks do not establish deployment or installed-PWA behavior.
- Music Vocal's compiler helper block is self-contained inside the CLI. Moving
  it into an importable renderer with complete offline output fixtures is the
  next phase 6/7 candidate; this style batch does not claim that separation done.

## AHC duplicate language initialization and browser-fixture isolation

- The CPU architecture lesson had three identical shared language script tags.
  Each registered the same DOMContentLoaded callback. Kept the first tag and
  removed only the other two complete tag lines; every educational section and
  other byte matches the checkpoint. The migration's explicit
  `--dedupe-references` mode validates identical references and rejects unknown
  paths or mixed variants. Repeat dry run plans zero writes.
- Source and compiled-artifact tests confirm three initializers became one,
  lesson text and Hindi/English state match, keyboard language switching works,
  and mobile/desktop screenshots have zero changed pixels. The compiled-page
  repair retains its minified/versioned asset reference. Evidence is under
  `scratch/refactor/ahc-language-dedupe/`.
- The concatenated CPU document still has pre-existing malformed inline scripts
  and duplicate `appThemes` declarations. The four corresponding browser errors
  occur before and after the reference repair; resolving the remaining document
  structure is an open baseline issue, not a completed part of this repair.
- Browser runs exposed anonymous visitor analytics writes from the shared header
  to Firestore, including intermittent 409 responses. Repository fixtures now
  acknowledge only guest-profile/engagement analytics PATCH/POST requests locally.
  Policy tests confirm signed-in-user requests, reads and learning-data requests
  are excluded from this fixture. AHC and Sociology browser comparisons pass with
  this isolation; live authentication and Firestore delivery remain separate checks.
- Current full `npm run refactor:test` result: 103/103 passed. Changed scripts
  pass syntax checks and the CPU diff removes exactly two lines. Current Class 9
  page and figure edits from other work are retained. This batch is uncommitted.

Useful commands:

```sh
npm run build:dry
npm run build:test
npm run refactor:test
npm run refactor:test:browser
node scripts/check-history-preservation.mjs
node scripts/audit-refactor.cjs
npm run refactor:baseline -- --label=before
npm run pages:build
npm run refactor:baseline -- --label=staged --root=.pages-dist --compare=before
node scripts/extract-history-styles.mjs
node scripts/extract-history-runtime.mjs
node scripts/benchmark-build-references.mjs
node scripts/check-physics-topic-preservation.mjs
node scripts/extract-physics-topic-assets.mjs
node scripts/check-ssc-cgl-topic-preservation.mjs
node scripts/extract-ssc-cgl-topic-assets.mjs
node scripts/check-psychology-bilingual-preservation.mjs
node scripts/extract-psychology-bilingual-style.mjs
node scripts/check-upsc-preservation.mjs
node scripts/extract-upsc-styles.mjs
```
