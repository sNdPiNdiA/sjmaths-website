# Quantitative Aptitude topic data

This root-level folder contains a shared quantitative aptitude topic catalog and reusable topic data. It is intended to support overlapping content across UPSC CSAT, TET, banking, railways, CAT, SSC and state-government recruitment pages. There is no single syllabus shared by all of those exams, so each exam page must select topics against its current official notification and required difficulty.

## Files

- `catalog.json` lists 87 shared topics in 11 subject groups. Its `preparationBands` distinguish basic numeracy, general aptitude, advanced aptitude, school mathematics, pedagogy, and adjacent quantitative reasoning.
- `manifest.json` lists the topic files exported from SSC CGL source pages, along with their source syllabus areas and labels.
- `<topic-id>.json` stores one reusable topic file per catalog entry. Topic IDs and JSON files stay directly in this folder; there is no nested `topics/` directory.
- `../../js/quantitative-aptitude-data.js` loads the manifest, catalog or a topic and filters exam-specific sections.
- `../../../scripts/export-quantitative-aptitude-data.mjs` rebuilds the JSON from the current SSC CGL pages. It previews by default; pass `--write` to update generated files.
- `../../../scripts/quantitative-aptitude-lesson-content.mjs` contains the shared authored lesson expansions for the 59 topics without an existing SSC CGL export.
- `../../../scripts/generate-quantitative-aptitude-lessons.mjs` builds those 59 shared topic files. It previews by default; pass `--write` to regenerate them and point every catalog entry to its own JSON file.

All 87 catalog entries have `contentStatus: "shared-content"` and a dedicated `dataFile` named after the topic ID. The 28 SSC CGL exports preserve their source content and PYQs. The 59 shared-authored lessons provide topic prerequisites, a coverage checklist, concept explanations and worked examples, exam methods, revision facts, and five worked practice questions at core, foundation, standard and challenge levels. New practice questions are original; no PYQs are invented or relabelled.

The shared lessons contain four `html-fragment` sections: concepts and worked examples, methods and exam checks, key facts and formulas, and worked practice. A `learningMap` records prerequisites, topic coverage and practice levels. Shared content is tagged with `reusePolicy: "same-syllabus-review"`; check the target exam's syllabus and difficulty before displaying it. Existing PYQs carry `examId: "ssc-cgl"` and are returned only when the loader is called with `{ examId: "ssc-cgl" }`. Topic-level `reviewFlags` preserve known source issues without rewriting the original material; the Averages file flags an inconsistent answer in practice Q9. New shared lessons are currently English-only. Each consuming exam should provide its own page title and SEO description.

The catalog records syllabus boundaries from official examples: UPSC CSAT specifies Class X-level basic numeracy and data interpretation; CTET covers school-level mathematics and pedagogy; RRB NTPC and SSC CGL publish broader topic lists. CAT, banking and state-government recruitment requirements vary, so treat the corresponding preparation areas as reusable study coverage, not an official topic-by-topic mapping. Source links are recorded in `catalog.json`.

## Example

Load the shared sections for another exam and place them into containers in that page's template:

```html
<section data-qa-section="theory"></section>
<section data-qa-section="tricks"></section>
<section data-qa-section="notes"></section>
<section data-qa-section="practice"></section>
```

```js
import { loadQuantitativeAptitudeTopic } from "/assets/js/quantitative-aptitude-data.js";

const topic = await loadQuantitativeAptitudeTopic("averages", { examId: "ssc-chsl" });
for (const section of topic.sections) {
  const target = document.querySelector(`[data-qa-section="${section.id}"]`);
  if (target) target.innerHTML = section.html;
}
await window.MathJax?.typesetPromise?.();
```

To include the SSC CGL PYQ section, call the loader with `examId: "ssc-cgl"` and add a `data-qa-section="pyqs"` container. The fragments retain the source page's markup conventions, so a consuming page should provide compatible styles and any tab or math-rendering runtime it uses.

The current SSC CGL pages remain static HTML. Pages that render these fragments only after a browser fetch need static rendering or pre-rendering if their educational text must be available in the initial HTML for SEO.
