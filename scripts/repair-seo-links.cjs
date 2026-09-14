const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { ROOT, siteFiles, parse, applyEdits, editElement, escapeHtml: esc, compact } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const files = siteFiles();
const resolve = createResolver(files);
const bySlug = new Map();
for (const file of files.filter(f => f.endsWith('/index.html'))) {
  const key = file.split('/')[0] + '/' + file.split('/').at(-2);
  if (!bySlug.has(key)) bySlug.set(key, []);
  bySlug.get(key).push(file);
}
const known = {
  '/class-9-maths/worksheets/chapter-1-number-system/': '/class-9-maths/worksheets/chapter-1-use-of-coordinates/',
  '/class-9-advanced-science/chapter-4-the-geometry-of-power-advanced-simple-machines/': '/class-9-advanced-science/chapter-4-geometry-of-power-advanced-simple-machines/',
  '/class-9-advanced-science/chapter-10/': '/class-9-advanced-science/chapter-10-engineering-life-miracles-in-biotechnology/',
  '/class-9-science/chapter-12-patterns-in-life-diversity/': '/class-9-science/chapter-12-patterns-in-life-diversity-and-classification/',
  '/class-9-science/chapter-13-earth-as-a-system-energy/': '/class-9-science/chapter-13-earth-as-a-system-energy-matter-and-life/',
  '/class-9-science/chapter-8-motion-in-living-organisms/': '/class-9-science/chapter-8-journey-inside-atom/',
  '/class-9-science/chapter-9-next-chapter/': '/class-9-science/chapter-9-atomic-foundations-of-matter/',
  '/class-9-science/chapter-10-sound-waves-characteristics/': '/class-9-science/chapter-10-sound-waves-characteristics-and-applications/',
  '/class-11-applied-mathematics/chapter-7-permutations-and-combinations/': '/class-11-applied-mathematics/chapter-8-combinatorics/',
};
const unavailable = [];
const counts = { files: 0, correctedLinks: 0, unavailableLinks: 0, assets: 0, languageAlternates: 0 };
for (const file of files.filter(policy.isManagedHtmlPath)) {
  const original = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (policy.hasNoindex(original) || policy.hasRedirect(original)) continue;
  let source = original;
  // Only known missing assets are replaced, using established shared scripts/images.
  source = source.replace(/https:\/\/sjmaths\.com\/assets\/images\/(?:og-applied-maths-ch[2-8]|sat-og-card)\.png/g, () => { counts.assets++; return 'https://sjmaths.com/assets/icons/icon-512x512.png'; });
  if (file.startsWith('class-10-social-science/history/')) source = source.replace(/src="\.\.\/\.\.\/assets\/js\/main\.min\.js/g, 'src="/assets/js/main.min.js');
  if (/^class-11-applied-mathematics\/chapter-[56]-/.test(file)) source = source.replace(/<script src="\/assets\/js\/load-components\.min\.js[^>]*><\/script>/g, '<script src="/assets/js/global-header.min.js" defer></script>\n    <script src="/assets/js/global-footer.min.js" defer></script>');
  if (file === 'class-11-applied-mathematics/chapter-9-probability/index.html') {
    source = source.replace(/<script src="\/assets\/js\/component\.min\.js[^>]*><\/script>/g, '<script src="/assets/js/global-header.min.js" defer></script>');
    source = source.replace(/<script src="\/assets\/js\/improved-ui\.min\.js[^>]*><\/script>/g, '<script src="/assets/js/global-footer.min.js" defer></script>');
  }
  const $ = parse(source);
  const edits = [];
  const base = policy.toUrl(file);
  $('a[data-unavailable-href]').each((_, el) => unavailable.push({ file, label: compact($(el).text()).replace(/\s*\(not yet available\)$/, ''), url: new URL($(el).attr('data-unavailable-href'), base).href }));
  $('a[href]').each((_, el) => {
    const href = $(el).attr('href');
    if (!href || /^(#|mailto:|tel:|javascript:|data:)/i.test(href)) return;
    const result = resolve(href, base);
    if (result.external || (result.file && !result.redirect)) return;
    let url;
    try { url = new URL(href, base); } catch { return; }
    let target = (result.file && result.redirect ? result.redirect : url.pathname).replace(/\/{2,}/g, '/');
    for (const [oldPath, newPath] of Object.entries(known)) if (target.startsWith(oldPath)) target = newPath + target.slice(oldPath.length);
    const key = file.split('/')[0] + '/' + target.split('/').filter(Boolean).at(-1);
    if (!resolve(target).file && bySlug.get(key)?.length === 1) target = policy.toLocalUrl(bySlug.get(key)[0]);
    const loc = el.sourceCodeLocation.startTag;
    const tag = source.slice(loc.startOffset, loc.endOffset);
    if (resolve(target).file) {
      edits.push({ start: loc.startOffset, end: loc.endOffset, text: tag.replace(/\bhref\s*=\s*(["'])[\s\S]*?\1/i, `href="${esc(target + url.search + url.hash)}"`) });
      counts.correctedLinks++;
    } else {
      const label = compact($(el).text());
      unavailable.push({ file, label, url: url.href });
      const newTag = tag.replace(/\bhref\s*=\s*(["'])[\s\S]*?\1/i, `data-unavailable-href="${esc(href)}"`).replace(/\s(?:aria-disabled|title)\s*=\s*(["'])[\s\S]*?\1/gi, '').replace(/>$/, ' aria-disabled="true" title="This resource is not yet available">');
      edits.push({ start: loc.startOffset, end: loc.endOffset, text: newTag });
      if (el.sourceCodeLocation.endTag) edits.push({ start: el.sourceCodeLocation.endTag.startOffset, end: el.sourceCodeLocation.endTag.startOffset, text: ' <small class="resource-status">(not yet available)</small>' });
      counts.unavailableLinks++;
    }
  });
  $('link[rel="alternate"][hreflang]').each((_, el) => {
    const href = $(el).attr('href');
    const result = resolve(href, base);
    // A missing/redirected language document is not an alternate translation.
    // Query-only toggles whose canonical is the same English page are not either.
    if (!result.external && (!result.file || result.redirect || (/[?&]lang=hi(?:&|$)/.test(href) && file.startsWith('current-affairs/')))) {
      edits.push(editElement(el, '')); counts.languageAlternates++;
    }
  });
  $('script[type="application/ld+json"]').each((_, el) => {
    const raw = $(el).text();
    let data;
    try { data = JSON.parse(raw); } catch { return; }
    let changed = false;
    const visit = value => {
      if (!value || typeof value !== 'object') return;
      if (value['@type'] === 'BreadcrumbList' && Array.isArray(value.itemListElement) && value.itemListElement.length > 3 && value.itemListElement.every(i => i.url && !i.item)) {
        value['@type'] = 'ItemList'; changed = true;
      }
      for (const v of Object.values(value)) if (Array.isArray(v)) v.forEach(visit); else visit(v);
    };
    visit(data);
    if (changed) edits.push(editElement(el, `<script type="application/ld+json">${JSON.stringify(data).replace(/</g, '\\u003c')}</script>`));
  });
  if (edits.length) source = applyEdits(source, edits);
  if (source !== original) { fs.writeFileSync(path.join(ROOT, file), source); counts.files++; }
}
fs.mkdirSync(path.join(ROOT, 'scripts/reports'), { recursive: true });
fs.writeFileSync(path.join(ROOT, 'scripts/reports/seo-unavailable-resources.json'), JSON.stringify(unavailable, null, 2) + '\n');
console.log(JSON.stringify(counts));
