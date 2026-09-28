# SJMaths preservation-first refactor

## Objective

Reduce duplicate implementation and improve build reliability while preserving
the current interface, educational content, public routes and student journeys.
This is a refactor, not a visual redesign. Browser findings already present in
the baseline are recorded separately from regressions introduced by a batch.

## Migration tracker

| Phase | Work | Status | Required evidence |
| --- | --- | --- | --- |
| 1 | Capture representative UI and behaviour | Eight routes captured; wider journeys pending | Original 24 screenshots plus History variant baselines, 390/1280px, quiz/test/solution/guest interactions |
| 2 | Map page families and source ownership | Initial inventory complete; refine per family | Source/output/consumer inventory |
| 3 | Make builds fail reliably and prepare replacements before writes | Verified in fixtures and full staged artifact | Failure injection, successful artifact and browser comparison |
| 4 | Extract identical CSS by page family | History complete; 1,630-page UPSC and 368-page ASO groups migrated; other groups pending | Preserved cascade, screenshot and content comparison |
| 5 | Extract identical JS by page family | History's 81 four-tab pages migrated; other families pending | Preserved load order, interactions, cleanup and state |
| 6 | Separate generator infrastructure from subject-specific material | History renderer/schema separated and fixture-tested; API infrastructure and other generators pending | Fixture equivalence and generated-page browser checks |
| 7 | Consolidate maintained page templates | History renderer centralized; other families pending | Content, routes, metadata and UI parity |
| 8 | Organize maintenance scripts and state | Four read-only ASO tools organized with compatibility shims; wider scope pending | All callers resolved and existing npm commands working |
| 9 | Broaden verification coverage | History lifecycle, preservation and offline generation covered; wider scope pending | Folder scripts, remaining inline scripts and browser journeys |
| 10 | Optimize measured costs and release in batches | Reference-update optimization verified; other bottlenecks and delivery pending | Transfer/build measurements and reversible delivery |

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

## Next batches

1. Inspect remaining style/runtime groups and their authoring/repair callers
   before migrating them; resolve ASO baseline defects separately from extraction.
2. Separate API retry/status infrastructure only where actual callers can share
   it without changing subject prompts or content requirements.
3. Organize maintenance entry points after identifying package/CI/documentation
   callers; preserve public URLs and supported commands.
4. Broaden auth, PDF, search, responsive and installed-PWA runtime coverage before
   considering the site-wide refactor or any release complete.

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
node scripts/check-upsc-preservation.mjs
node scripts/extract-upsc-styles.mjs
```
