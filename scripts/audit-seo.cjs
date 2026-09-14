// Read-only source audit. Run with --output=path.json to retain every finding.
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const cheerio = require('cheerio');
const { XMLParser, XMLValidator } = require('fast-xml-parser');
const policy = require('./seo-policy.cjs');
const { siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const ROOT = path.resolve(__dirname, '..');
const tracked = siteFiles();
const exists = p => { try { return fs.statSync(path.join(ROOT, p)).isFile(); } catch { return false; } };
const resolveUrl = createResolver(tracked);
const issues = [];
const pages = [];
const add = (code, file, detail, severity = 'error') => issues.push({ code, file, detail, severity });
const compact = s => s.replace(/\s+/g, ' ').trim();
const sitemapUrls = new Map();
const xml = new XMLParser();
const index = xml.parse(fs.readFileSync(path.join(ROOT, 'sitemap.xml'), 'utf8'));
const sitemapFiles = [].concat(index.sitemapindex?.sitemap || []).map(s => new URL(s.loc).pathname.slice(1));
for (const expected of policy.SITEMAP_ORDER) if (!sitemapFiles.includes(expected)) add('sitemap-index-missing-file', 'sitemap.xml', expected);
for (const actual of sitemapFiles) if (!policy.SITEMAP_ORDER.includes(actual)) add('sitemap-index-unmanaged-file', 'sitemap.xml', actual, 'warning');
for (const file of sitemapFiles) {
  if (!exists(file)) { add('sitemap-file-missing', file, 'Referenced by sitemap.xml'); continue; }
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (XMLValidator.validate(source) !== true) add('sitemap-invalid-xml', file, 'Invalid XML');
  const rows = [].concat(xml.parse(source).urlset?.url || []);
  for (const row of rows) {
    if (sitemapUrls.has(row.loc)) add('sitemap-duplicate-url', file, row.loc);
    sitemapUrls.set(row.loc, file);
    const resolved = resolveUrl(row.loc);
    if (!resolved.file || resolved.redirect) add('sitemap-unfetchable-url', file, row.loc + (resolved.redirect ? ' redirects to ' + resolved.redirect : ' missing'));
    if (row.lastmod && String(row.lastmod).slice(0, 10) > new Date().toISOString().slice(0, 10)) add('sitemap-future-lastmod', file, row.loc);
  }
}
const htmlFiles = tracked.filter(p => policy.isManagedHtmlPath(p) && !p.startsWith('scratch/'));
for (const file of htmlFiles) {
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (!source.trim()) { add('empty-html', file, 'Empty file', 'warning'); continue; }
  const $ = cheerio.load(source);
  const meta = name => $('meta').filter((_, el) => ($(el).attr('name') || $(el).attr('property') || '').toLowerCase() === name);
  const canonical = $('link[rel="canonical"]');
  const title = compact($('title').first().text());
  const description = meta('description').first().attr('content') || '';
  const noindex = /noindex/i.test(meta('robots').map((_, el) => $(el).attr('content')).get().join(' '));
  const refresh = $('meta[http-equiv="refresh" i]').length > 0;
  const route = policy.toUrl(file);
  const canon = canonical.first().attr('href') || '';
  const target = canon ? resolveUrl(canon, route) : {};
  const served = resolveUrl(route);
  const alias = Boolean(refresh || (served.redirect && served.file !== file) || (target.file && target.file !== file));
  const indexable = !noindex && !alias;
  const body = $('body').clone();
  body.find('script,style,svg,nav,header,footer').remove();
  const words = compact(body.text()).split(' ').filter(Boolean).length;
  const page = { file, route, title, description, canonical: canon, noindex, alias, indexable, words, h1: $('h1').length, sitemap: sitemapUrls.has(route), eligible: policy.isSitemapEligibleHtml(file, source) };
  pages.push(page);
  if (served.redirect && !served.file) add('physical-page-redirects-to-missing-target', file, served.chain);
  if (!indexable) continue;
  // Explicit delimiters are required by this site's source-preserving generators.
  for (const tag of ['head', 'body']) if (!new RegExp(`<${tag}\\b`, 'i').test(source) || !new RegExp(`</${tag}\\s*>`, 'i').test(source)) add('document-container-missing', file, tag);
  if ($('title').length !== 1 || !title) add('title-missing-or-multiple', file, $('title').length);
  if (meta('description').length !== 1 || !description.trim()) add('description-missing-or-multiple', file, meta('description').length);
  if (title.length < 15 || title.length > 120) add('title-length-extreme', file, title.length, 'warning');
  if (description.length < 40 || description.length > 320) add('description-length-extreme', file, description.length, 'warning');
  // Only flag a page when its primary content is a placeholder. A complete
  // chapter may legitimately label one future quiz or worksheet "Coming Soon".
  if (policy.isPlaceholderHtml(source)) {
    add('placeholder-content-indexable', file, compact(body.text()).slice(0, 240));
  }
  if (canonical.length !== 1 || !canon) add('canonical-missing-or-multiple', file, canonical.length);
  else if (canon !== route) add('canonical-not-normalized', file, { canonical: canon, expected: route });
  if (!$('html').attr('lang')) add('language-missing', file, 'html lang');
  if (!meta('viewport').length) add('viewport-missing', file, 'No viewport');
  if ($('h1').length !== 1) add('h1-missing-or-multiple', file, $('h1').length, 'warning');
  if (!/^\s*(?:\uFEFF)?<!doctype html/i.test(source)) add('doctype-missing', file, 'No HTML doctype');
  for (const name of ['og:title', 'og:description', 'og:url', 'og:image', 'twitter:card']) {
    if (!meta(name).length || !meta(name).first().attr('content')) add('social-missing', file, name, 'warning');
    else if (meta(name).length > 1) add('social-duplicate', file, name);
  }
  if (meta('og:url').length && meta('og:url').first().attr('content') !== canon) add('social-url-mismatch', file, meta('og:url').first().attr('content'));
  $('link[rel="alternate"][hreflang][href]').each((_, el) => {
    const alternate = $(el).attr('href');
    const result = resolveUrl(alternate, route);
    if (!result.external && (!result.file || result.redirect)) add('hreflang-target-invalid', file, { hreflang: $(el).attr('hreflang'), alternate, result });
  });
  if (!page.sitemap) add('indexable-not-in-sitemap', file, { eligible: page.eligible, words }, 'warning');
  // This is a review signal, NOT a Google word-count threshold or a noindex rule.
  if (words < 80) add('little-static-content', file, words, 'info');
  const ids = new Set();
  $('[id]').each((_, el) => { const id = $(el).attr('id'); if (ids.has(id)) add('duplicate-id', file, id, 'warning'); ids.add(id); });
  const uniqueLinks = new Set();
  $('a[href],form[action],link[href],script[src],img[src],source[src],video[src],video[poster],audio[src],iframe[src],object[data],meta[property="og:image"],meta[name="twitter:image"]').each((_, el) => {
    const value = $(el).attr('href') || $(el).attr('action') || $(el).attr('src') || $(el).attr('poster') || $(el).attr('data') || $(el).attr('content');
    if (!value || /^(#|mailto:|tel:|javascript:|data:|blob:)/i.test(value) || uniqueLinks.has(value)) return;
    uniqueLinks.add(value);
    const result = resolveUrl(value, route);
    if (!result.external && result.file && result.redirect && ['a', 'form'].includes(el.tagName)) add('internal-link-redirect', file, { value, destination: result.redirect }, 'warning');
    if (!result.external && !result.file) add(['a', 'form'].includes(el.tagName) ? 'broken-internal-link' : 'missing-local-asset', file, value);
  });
  $('[srcset]').each((_, el) => {
    for (const candidate of ($(el).attr('srcset') || '').split(',').map(value => value.trim().split(/\s+/)[0]).filter(Boolean)) {
      const result = resolveUrl(candidate, route);
      if (!result.external && !result.file) add('missing-local-asset', file, candidate);
    }
  });
  $('a[href^="#"]').each((_, el) => {
    let fragment = ($(el).attr('href') || '').slice(1);
    try { fragment = decodeURIComponent(fragment); } catch {}
    if (fragment && !ids.has(fragment)) add('broken-page-fragment', file, '#' + fragment, 'warning');
  });
  $('img:not([alt])').each((_, el) => add('image-alt-missing', file, $(el).attr('src'), 'warning'));
  $('[onclick],[onload],[onerror],[onchange],[onsubmit],[oninput],[onkeydown],[onkeyup]').each((_, el) => {
    for (const [name, value] of Object.entries(el.attribs || {})) {
      if (!/^on(?:click|load|error|change|submit|input|keydown|keyup)$/.test(name)) continue;
      try { new vm.Script(`(function(event){${value}\n})`); }
      catch (error) { add('inline-handler-invalid', file, { attribute: name, error: error.message }); }
    }
  });
  $('script:not([src])').each((_, el) => {
    const type = ($(el).attr('type') || 'text/javascript').toLowerCase();
    if (!['text/javascript', 'application/javascript'].includes(type) || !$(el).text().trim()) return;
    try { new vm.Script($(el).text(), { filename: file }); }
    catch (error) { add('inline-script-invalid', file, error.message); }
  });
  $('script[type="application/ld+json"]').each((_, el) => {
    let data;
    try { data = JSON.parse($(el).text()); } catch (error) { add('jsonld-invalid', file, error.message); return; }
    const schemaUrls = new Set();
    const visit = node => {
      if (!node || typeof node !== 'object') return;
      if (node['@type'] === 'BreadcrumbList') {
        const items = node.itemListElement;
        if (!Array.isArray(items) || !items.length || items.some((it, i) => !it.name || it.position !== i + 1 || (i < items.length - 1 && !it.item))) add('breadcrumb-invalid', file, node);
      }
      for (const value of Object.values(node)) {
        if (typeof value === 'string' && /^https?:\/\/(?:www\.)?sjmaths\.com\//i.test(value) && !/[{}]/.test(value)) schemaUrls.add(value);
        else if (Array.isArray(value)) value.forEach(visit);
        else visit(value);
      }
    };
    visit(data);
    for (const value of schemaUrls) {
      const result = resolveUrl(value, route);
      if (!result.file) add('structured-data-url-broken', file, value);
    }
  });
  $('script[type="application/json"]:not([src])').each((_, el) => {
    try { JSON.parse($(el).text()); }
    catch (error) { add('embedded-json-invalid', file, { id: $(el).attr('id') || '', error: error.message }); }
  });
}
// Stylesheets often hide missing font/background assets from an HTML-only crawl.
for (const file of tracked.filter(file => file.endsWith('.css'))) {
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  for (const match of source.matchAll(/url\(\s*(["']?)([^"')]+)\1\s*\)/gi)) {
    const value = match[2].trim();
    if (!value || /^(?:data:|https?:|\/\/|#|var\()/i.test(value)) continue;
    let clean;
    try { clean = decodeURIComponent(value.split(/[?#]/)[0]); } catch { clean = value.split(/[?#]/)[0]; }
    const target = path.posix.normalize(clean.startsWith('/') ? clean.slice(1) : path.posix.join(path.posix.dirname(file), clean));
    if (!tracked.includes(target)) add('css-asset-missing', file, value);
  }
}
for (const [url, sitemap] of sitemapUrls) {
  const resolved = resolveUrl(url);
  const page = pages.find(p => p.file === resolved.file);
  if (page?.noindex) add('sitemap-noindex', sitemap, url);
  if (page && page.canonical !== url) add('sitemap-canonical-mismatch', sitemap, { url, canonical: page.canonical });
}
for (const field of ['title', 'description']) {
  const groups = new Map();
  for (const p of pages.filter(p => p.indexable && p[field])) {
    const value = p[field].toLowerCase();
    if (!groups.has(value)) groups.set(value, []);
    groups.get(value).push(p.file);
  }
  for (const [value, files] of groups) if (files.length > 1) add('duplicate-' + field, files[0], { value, files }, 'warning');
}
const counts = {};
for (const issue of issues) counts[issue.code] = (counts[issue.code] || 0) + 1;
const summary = { htmlFiles: htmlFiles.length, nonemptyPages: pages.length, indexablePages: pages.filter(p => p.indexable).length, sitemapUrls: sitemapUrls.size, errors: issues.filter(i => i.severity === 'error').length, warnings: issues.filter(i => i.severity === 'warning').length, informational: issues.filter(i => i.severity === 'info').length, counts };
console.log(JSON.stringify(summary, null, 2));
const output = process.argv.find(a => a.startsWith('--output='))?.slice(9);
if (output) { fs.mkdirSync(path.dirname(path.resolve(output)), { recursive: true }); fs.writeFileSync(output, JSON.stringify({ summary, pages, issues }, null, 2) + '\n'); }
if (process.argv.includes('--strict') && summary.errors) process.exitCode = 1;
