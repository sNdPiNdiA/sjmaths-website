# Current Ganita Manjari worksheets

The collection contains all fourteen current chapter worksheets and a separately labelled Geometry Foundations supplement. It follows the six-unit syllabus supplied on 30 September 2026, not an inferred examination marks blueprint.

There are 169 distinct questions: 120 reused from the syllabus-aligned unit bank with their original wording and solutions, plus 49 worksheet-only questions. Related computational activities appear in their topic worksheet and the algorithms worksheet, giving 175 question placements in total. `syllabus-coverage.json` maps all 77 topic groups to question anchors; this is a coverage map, not an assertion that every atomic learning outcome is exhaustively assessed.

## Maintenance

- Edit worksheet-specific questions and chapter mappings in `scripts/data/class-9-worksheets.cjs`.
- Edit shared practice in `scripts/data/class-9-unit-tests.cjs`, then regenerate the unit papers before the worksheets.
- Each worksheet presents Foundation, Practice and Challenge sections, native one-click answer disclosures, step-wise model solutions, and previous/next navigation.
- Diagrams from the unit papers are reused at build time. Worksheet-specific diagrams are defined in the worksheet generator.
- Earlier worksheet files are not modified or redirected. The worksheet directory links every existing earlier sheet separately.
- Auth uses the existing shared guard. No new Firebase listener is introduced.

```text
node scripts/generate-class-9-worksheets.cjs
node scripts/generate-class-9-worksheets.cjs --write
node generate-sitemaps.cjs --scope=class-9
node generate-search-index.cjs --scope=class-9
node --test scripts/class-9-worksheets.test.cjs
node --test scripts/class-9-worksheets-browser.test.cjs
```

The generator defaults to a dry run; `--write` creates current pages and updates their two hub entry points. Do not edit generated HTML directly. Optional print/share behaviour is isolated in `assets/js/class-9-worksheets.js`; styles are scoped in `assets/css/class-9-worksheets.css`. Native individual answer disclosures and all educational HTML remain available without JavaScript.

Printing defaults to questions only. “Include answer key” opens solutions for the print operation, and the after-print handler restores the student’s previous answer visibility. This option does not award marks; proof, construction and written responses still require self- or teacher assessment.

Local browser fixtures exclude shared authentication, analytics and site chrome. They verify worksheet interactions at 390, 768 and 1366 pixels and without JavaScript, including print-media answer visibility. They do not verify an operating-system print dialog, a live Firebase session, deployment or search indexing.
