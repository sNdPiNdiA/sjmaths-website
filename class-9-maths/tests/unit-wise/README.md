# Current Class 9 unit papers

These papers follow the six-unit syllabus supplied on 30 September 2026. The document specifies teaching periods, not an official examination marks distribution. Do not relabel these periods or practice-paper marks as board-exam weightage.

## Content and preservation

- Two papers per unit: concepts/applications and reasoning/modelling.
- 120 questions, with step-wise model answers, across 77 mapped topic groups. The mapping is in `syllabus-coverage.json`; it shows question coverage, not a claim that every student outcome is exhaustively assessed in one paper.
- Current units are Number System, Algebra, Coordinate Geometry, Geometry, Mensuration, and Statistics and Probability.
- The twelve earlier papers and their original JSON question banks are retained in `/class-9-maths/previous-syllabus/unit-tests/`. Current paper URLs remain unchanged.
- MCQs are automatically scored. Written answers, diagrams, constructions and proofs require self- or teacher assessment. The result screen identifies these separately.
- All questions and solutions also exist in source HTML. The full-paper disclosure remains available without JavaScript; normal test mode presents one question at a time.

## Editing and regeneration

Edit `scripts/data/class-9-unit-tests.cjs`, then run:

```text
node scripts/generate-class-9-unit-tests.cjs
node scripts/generate-class-9-unit-tests.cjs --write
node generate-sitemaps.cjs --scope=class-9
node generate-search-index.cjs --scope=class-9
```

The default generation command is a dry run. The write command archives earlier files only when their archive does not exist; it never replaces existing archived JSON questions. It refreshes archive metadata and directory pages. Increment the paper version if an assessment changes so stored answers cannot attach to different questions.

The new interface is a scoped extension of the existing `TestEngine`; other classes' engines and authentication scripts are unchanged. Its assets are `assets/js/class-9-unit-tests.js` and `assets/css/class-9-unit-tests.css`. Increment their query-string versions in the generator after changing a deployed asset.

## Verification

```text
node --test scripts/class-9-unit-tests.test.cjs scripts/class-9-curriculum-migration.test.cjs
node --test scripts/class-9-unit-tests-browser.test.cjs scripts/class-9-curriculum-browser.test.cjs
node scripts/audit-seo.cjs --scope=class-9-maths,class-9-ganita-manjari-part-2
```

Browser fixtures exercise the actual local test engine and scoped assets, but exclude Firebase authentication, analytics and external MathJax. Passing local tests does not verify deployment, live authentication or search indexing.

Historical approximation values in the Mensuration paper were checked against institutional sources: [University of Auckland lecture notes on π](https://www.math.auckland.ac.nz/class190/lectures/pi_history.pdf) and [IIT Bombay research notes](https://www.ircc.iitb.ac.in/IRCC-Webpage/rnd/PDF/IIT_Bombay_Research_Dissemination_Award_K_Ramasubramanian.pdf). Geometric-mean squaring is explicitly described as an equivalent mathematical construction, not attributed as the exact historical procedure.
