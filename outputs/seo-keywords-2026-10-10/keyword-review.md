# Search Console keyword review — 10 October 2026

## Evidence

Inspected the signed-in Google Search Console domain property `sjmaths.com`, Web search, Last 3 months: 7 July–6 October 2026. Report totals: 160 clicks, 965 impressions, 16.6% CTR, average position 34.1; last update shown as 31 hours ago. The query table exposed 165 rows. Query totals need not equal property totals because Search Console omits some query data.

Downloaded the unfiltered CSV export into `gsc-export/`. Filtered each query below in the live UI and opened its Pages breakdown. All listed non-brand queries had zero clicks. Most had only a handful of impressions, so these changes address visible content gaps without claiming statistically proven ranking gains.

| Query | Impressions | Position | Observed landing page | Decision |
|---|---:|---:|---|---|
| allahabad high court ro preparation tips | 11 | 52.0 | `/ahc-ro-aro/` | Add preparation tips and align title, H1 and descriptions |
| allahabad high court aro preparation tips | 6 | 51.8 | `/ahc-ro-aro/` | Same shared preparation section |
| up tgt home science syllabus | 3 | 43.0 | `/up-tgt-home-science/` | Include all six sections in intro and replace implementation-focused summary with study guidance |
| ssc cgl science syllabus | 3 | 79.3 | `/ssc-cgl/syllabus/` | Add visible science scope and link to existing science checklist |
| ssc economics syllabus | 3 | 80.7 | `/ssc-cgl/syllabus/` | Explain General Awareness versus specialized Finance and Economics; link to existing checklist |
| how to prepare static gk for ssc cgl | 2 | 40.5 | `/ssc-cgl/general-awareness/static-gk/` | Add a practical study method and align title/H1 to preparation intent |
| ssc cgl quantitative aptitude histogram | 2 | 30.5 | `/ssc-cgl/quantitative-aptitude/tables-and-graphs/` | Existing page is a direct match for the histogram query; retained |
| reasoning ssc cgl syllabus | 2 | 71.0 | SSC CGL syllabus query cluster | Syllabus hub already lists Reasoning as a full subject; no extra duplicate section |
| international monetary fund upsc | 2 | 74.0 | IMF topic page | Existing title and full topic page already match; retained |
| ipcc upsc | 3 | 78.0 | Legacy `Intergovernmental-Panel-on-Climate-Change-IPCC/` | Existing redirect targets current IPCC page; add acronym/full form, quick facts and translated H1 there |
| northern plains of india map | 1 | 66.0 | `/upsc/geography/Physiography-Drainage/Plains-Northern-Plains-of-India/` | Add bilingual regional map guide and NCERT map/chapter link; translate H1 and intro |
| kigali agreement upsc | 7 | 83.6 | Montreal Protocol and Kigali Agreement topic | Current title, intro and amendment explanation already match; retained |
| government of india act 1858 notes | 6 | 86.5 | Legacy `/upsc/modern_history/…/Government-of-India-Act-1858/` | Current modern-history page already matches; retained |
| 16 mahajanapadas in map | 3 | 48.7 | Legacy ancient_history (2 impressions) and current ancient-history (1) | Current page already has region/capital map guide and references; retained |
| compound interest installment formula | 3 | 52.3 | Legacy nested installment-formulas URL | Existing redirect targets interest lesson, which already includes formulas and worked examples; retained |

## Changes

Changed six existing pages using the shared `scripts/seo-html.cjs` source-location utilities. Titles and descriptions were aligned across standard, Open Graph and Twitter metadata. Relevant existing structured-data names/descriptions were kept consistent. Added sections are static crawlable HTML, outside runtime-replaced topic content. No educational questions, formulas, lessons, topic data, trackers or tab implementations were removed. Preserved the pre-existing Home Science working-copy edits.

The RO/ARO tips are general preparation advice; they do not introduce claims about recruitment stages or current typing thresholds. The Northern Plains section is a map-reading guide with an external NCERT map, rather than a newly drawn geographic map.

## Sources checked

- [SSC CGL 2026 examination notice](https://ssc.gov.in/api/attachment/uploads/masterData/NoticeBoards/Notice_of_adv_cgl_2025.pdf): the document itself states 2026 despite its filename. General Awareness includes everyday scientific understanding and the economic scene; Paper III separately covers Finance and Economics.
- [IPCC introduction](https://www.ipcc.ch/about/) and [IPCC history](https://www.ipcc.ch/about/history/): full form, 1988 WMO/UNEP origins and assessment role.
- [NCERT Physical Features of India](https://www.ncert.nic.in/textbook/pdf/iess102.pdf): Punjab, Ganga and Brahmaputra regional divisions.

## Review and limits

Source inspection results are saved in `source-review.json`: all five pages have one H1; all JSON-LD blocks parse; no new duplicate IDs; no removed original hrefs; standard/social descriptions match; existing topic-content, embedded topic data and syllabus lists remain identical to their pre-edit working-copy snapshots.

Local browser review used a temporary server at `http://127.0.0.1:8087/`. Confirmed visible new RO/ARO tips, Home Science overview, IPCC quick facts and Northern Plains guide. The new SSC science/economics links reveal their respective tab sections. English and Hindi IPCC/Northern Plains summaries appear after reload with the corresponding selected language.

Observed an existing language-switch interaction issue on IPCC: immediately switching can leave inline `display: none` on text in the newly selected language; reload displays it correctly. The symptom affects existing headings and tab labels too. Shared language scripts were not changed in this keyword task. Some existing Northern Plains overview content is English-only and becomes blank in Hindi; the newly added map guide is bilingual.

The previously open localhost:8082 preview returned the site's offline page, so it was not treated as current source evidence. No full site audit, mobile layout review or complete regression suite was run. No commit, push or deployment was performed. Search Console rankings and indexed snippets have not been re-evaluated after these local changes; improvement requires deployment and later Google recrawling.
