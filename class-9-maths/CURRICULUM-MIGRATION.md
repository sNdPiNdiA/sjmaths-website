# Class 9 curriculum migration

## What changed

- The existing Class 9 landing page, notes directory and exercise directory now list current Ganita Manjari Chapters 1–14. Chapters 9–14 link to the existing Part 2 pages and their exact tab/exercise fragments.
- Chapter and exercise links are present in source HTML. Exercise directory disclosures use native `details`/`summary` and work without JavaScript.
- Earlier-edition questions, worksheets, Exemplar resources and tests retain their URLs and content. Syllabus notices distinguish them from current practice.
- Full supplementary copies of the three retired notes pages are available under `/class-9-maths/previous-syllabus/`; original source files are retained for content-preservation checks.
- Statistics keeps its original notes URL because the current Understanding Data chapter is not a complete replacement for all its topics.

## Permanent redirects

The old directory URL, trailing-slash URL and `index.html` URL redirect in one hop in both `_redirects` and `firebase.json`:

| Retired notes route | Current topic destination |
| --- | --- |
| `chapter-9-triangles` (the existing content is Circles) | Chapter 5: Circles |
| `chapter-10-herons-formula` | Chapter 6: Measuring Space: Perimeter and Area |
| `chapter-11-surface-areas-and-volumes` | Part 2 Chapter 14: Surface Area and Volume |

Existing root `.html` aliases go directly to the final destination too. Old exercise numbers are **not** redirected to unrelated new exercise numbers.

## Local verification

```powershell
node --test scripts/class-9-curriculum-migration.test.cjs
node --test scripts/class-9-curriculum-browser.test.cjs
node --test scripts/seo-regression.test.cjs
node scripts/check-cloudflare-redirects.cjs
node scripts/audit-seo.cjs --scope=class-9-maths,class-9-ganita-manjari-part-2 --output=scratch/class-9-migration-seo.json
```

Browser fixtures cover 390, 768 and 1440 pixel widths, chapter filters, keyboard exercise disclosures, deep-linked tabs, next-exercise navigation, archive layout and no-JavaScript exercise links. They intentionally exclude shared authentication and analytics; they do not prove live hosting behavior.

Refresh just these maths discovery entries while preserving unrelated search entries and the Science/Advanced sitemap blocks:

```powershell
node generate-search-index.cjs --scope=class-9
node generate-sitemaps.cjs --scope=class-9
```

## After authorized deployment

1. Check live old URLs return HTTP 301 and their final destinations return HTTP 200. Test all three URL variants above and existing root aliases.
2. Check current and archive canonicals, source chapter links and `/sitemap-class-9.xml` on the live host.
3. Re-submit the existing sitemap in Search Console and inspect the new/changed canonical URLs. A same-domain curriculum update does not need a Change of Address request.
4. Monitor indexing, crawl errors, impressions and clicks separately from local audit results. Ranking preservation cannot be guaranteed.
5. Retain redirects for at least one year after deployment, preferably permanently where old backlinks remain useful.

This migration is prepared locally. Commit, push, deployment and Search Console verification are separate actions.
