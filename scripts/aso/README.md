# ASO read-only diagnostics

Run from any working directory using an absolute entry-point path, or use the
following npm commands from the repository root:

- `npm run aso:count`: count hub microtopic markers.
- `npm run aso:disk-check`: compare three legacy pillars with hub links.
- `npm run aso:verify`: suggest title-based link matches (heuristic, not authority).
- `npm run aso:coverage`: compare a curated legacy plan with folder names.

These tools do not edit content. The old root `aso-*.cjs` commands remain supported
through compatibility entry points. Coverage and match warnings require manual
curriculum review; they are not permission to rewrite links or remove lessons.

Other root ASO scripts are not yet migrated. Some write files; `aso-daymap.cjs`
and related generation/link tools depend on the currently absent
`upsc-aso/topics_v2.json`. Do not run write tools without reviewing their inputs.
Rich static lessons use `assets/css/aso-lesson.css`; the placeholder generator
has a separate style and is not their maintained source of truth.
