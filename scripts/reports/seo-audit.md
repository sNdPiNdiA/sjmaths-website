# SJMaths SEO audit and remediation

Date: 2026-09-14
Scope: the full local static-site source tree, routing rules, metadata, structured data, internal references, generated search index/sitemaps, and representative browser behavior.

## Outcome

| Measure | Baseline | Final |
| --- | ---: | ---: |
| HTML files inspected | 5142 | 5521 |
| Indexable pages | 5069 | 4569 |
| Sitemap URLs | 4518 | 4569 |
| Hard errors | 4791 | 0 |
| Warnings | 9455 | 0 |

| Broken internal links | 4652 | 0 |
| Missing local assets | 16 | 0 |
| Missing/multiple canonicals | 10 | 0 |
| Canonical mismatches | 3 | 0 |
| Missing social metadata | 1871 | 0 |
| Duplicate IDs | 5461 | 0 |
| Missing/multiple H1 | 709 | 0 |
| Invalid breadcrumbs | 3 | 0 |
| Invalid JSON-LD | 0 | 0 |
| Unfetchable sitemap URLs | 9 | 0 |
| Indexable pages omitted from sitemap | 560 | 0 |
| Duplicate titles | 85 | 0 |
| Duplicate descriptions | 74 | 0 |

Final classification: 894 pages carry an explicit noindex directive and 58 source documents are aliases/redirects. The sitemap contains 4569 fetchable, canonical, indexable URLs.

## Remediation completed

- Added a source-preserving metadata policy and full-repository SEO audit instead of serializing/reformatting educational HTML.
- Normalized canonical and Open Graph URLs, filled missing social metadata, repaired headings and duplicate IDs, and removed invalid alternate-language declarations.
- Removed route rules that swallowed real lessons or public JSON; repaired internal links and marked 1301 links to genuinely unpublished resources as visibly unavailable rather than leaving broken URLs.
- Marked verified placeholder shells noindex while keeping them accessible to crawlers, navigation and future authors. No placeholder file or syllabus entry was deleted.
- Generated missing topic directory pages only from existing lessons and split sitemap output by maintained subject groups.
- Materialized the existing renderer's initial authored content in 1914 dynamic pages (96.8 MiB total, 51.8 KiB average), while retaining the interactive renderer for later tabs.
- Rebuilt the three modified minified SEO/client assets and refreshed their cache keys.
- Repaired malformed Class 9 exercise document containers, malformed UPSSSC embedded JSON, and malformed Class 12 Physics KaTeX/script endings.
- Sitemap lastmod is emitted only when a real content date is known; checkout timestamps are not published as update dates.

Largest prerendered source pages (monitor as authored content grows):
- `upsssc-pet/economy/bank-nationalization-reforms/index.html` — 221.1 KiB
- `upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/index.html` — 200.7 KiB
- `upsssc-pet/economy/planning-commission-five-year-plans/index.html` — 187.6 KiB
- `upsc/modern-history/The-Revolt-of-1857/Important-British-Officers-during-Suppression-of-Revolt/index.html` — 187.1 KiB
- `upsssc-pet/economy/economic-reforms-1991/index.html` — 183.4 KiB

## Verification

- Static audit: 0 errors, 0 warnings, 351 informational review signals.
- Preservation comparison: 31687 unique educational/data fragments checked across 2697 modified pages; 0 losses. 6 malformed inline data blocks were recovered from their valid authored data files.
- Dynamic prerender: 1914 successful pages; 0 failures.
- Browser: 12/12 representative viewport/page checks passed all locally testable structural and interaction checks; 2 also completed external integrations and 10 were blocked by denied CDN/Firebase access. The Class 12 Physics sweep passed 14/14 structural mobile checks. Checks cover canonical/description/OG uniqueness, one H1, duplicate IDs, horizontal overflow, source integrity, console errors and solution interaction where present.
- Regression suite: URL normalization, redirect classification, metadata idempotence, protected public data/test routes, and placeholder eligibility.

Local browser tests intentionally stubbed advertising/analytics requests; other external CDN requests were allowed but denied by the sandbox and are reported as blocked rather than passed. This audit does not claim deployment, Search Console indexing, field Core Web Vitals, or production-cache validation. Production must be rechecked after deployment.

## Remaining audit findings

- None.

The informational “little static content” signal is not treated as an error or a Google word-count rule. Directory pages and interactive tools can legitimately be concise; missing educational lessons are tracked separately in [seo-unavailable-resources.json](./seo-unavailable-resources.json) rather than padded with invented text.

## Reference policy

- [Google: canonical URL consolidation](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: block indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Google: JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google Search Essentials for developers](https://developers.google.com/search/docs/fundamentals/get-started-developers)
