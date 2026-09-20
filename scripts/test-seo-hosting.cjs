const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');
const { ROOT, siteFiles } = require('./seo-html.cjs');
const policy = require('./seo-policy.cjs');
const { collectRuntimeJsonFiles } = require('./runtime-json-assets.cjs');

const option = name => process.argv.find(arg => arg.startsWith(`--${name}=`))?.slice(name.length + 3);
const base = new URL(option('base') || 'https://sjmaths.com');
const canonicalOrigin = (option('canonical') || 'https://sjmaths.com').replace(/\/$/, '');
const concurrency = Math.max(1, Number(option('concurrency') || 24));
const runtimeOnly = process.argv.includes('--runtime-only');
const runtimeConcurrency = Math.max(1, Number(option('runtime-concurrency') || Math.min(concurrency, 8)));
const samplePerSitemap = Math.max(1, Number(option('samples') || 3));
const timeoutMs = Math.max(1000, Number(option('timeout') || 20000));
const previewNoindex = option('preview-noindex') !== 'false' && base.hostname.endsWith('.web.app') && base.hostname.includes('--');
const cacheBust = option('cache-bust');

const decodeXml = value => value.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
const locations = source => [...source.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/gi)].map(match => decodeXml(match[1]));
const target = value => {
  const source = new URL(value);
  const url = new URL(source.pathname + source.search, base);
  if (cacheBust) url.searchParams.set('_seo_check', cacheBust);
  return url.href;
};

async function request(url, init = {}) {
  let lastError;
  for (let attempt = 0; attempt < 3; attempt++) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await fetch(url, { redirect: 'manual', ...init, signal: controller.signal });
      if (response.status >= 500 && attempt < 2) continue;
      return response;
    } catch (error) {
      lastError = error;
      if (attempt === 2) throw error;
    } finally {
      clearTimeout(timer);
    }
  }
  throw lastError;
}

async function pool(items, worker, limit = concurrency) {
  let cursor = 0;
  const results = new Array(items.length);
  await Promise.all(Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (cursor < items.length) {
      const index = cursor++;
      results[index] = await worker(items[index], index);
    }
  }));
  return results;
}

function chooseSamples(groups) {
  const selected = new Set();
  for (const urls of groups) {
    if (!urls.length) continue;
    for (let i = 0; i < samplePerSitemap; i++) {
      selected.add(urls[Math.round(i * (urls.length - 1) / Math.max(samplePerSitemap - 1, 1))]);
    }
  }
  return [...selected];
}

function runtimeJsonReferences(source, pageUrl) {
  const references = [];
  for (const match of source.matchAll(/(?:window\.)?QUESTIONS_JSON\s*=\s*['"]([^'"]+)['"]/g)) {
    try { references.push(new URL(match[1], pageUrl).href); }
    catch {}
  }
  return [...new Set(references)];
}

async function main() {
  const indexResponse = await request(target(new URL('/sitemap.xml', canonicalOrigin)), { headers: { accept: 'application/xml,text/xml', 'cache-control': 'no-cache' } });
  const indexSource = await indexResponse.text();
  const sitemapUrls = locations(indexSource);
  const issues = [];
  if (indexResponse.status !== 200) issues.push({ code: 'sitemap-index-status', url: indexResponse.url, status: indexResponse.status });
  if (!sitemapUrls.length) issues.push({ code: 'sitemap-index-empty', url: indexResponse.url });

  const sitemapGroups = await pool(sitemapUrls, async sitemapUrl => {
    const url = target(sitemapUrl);
    try {
      const response = await request(url, { headers: { accept: 'application/xml,text/xml' } });
      const source = await response.text();
      if (response.status !== 200) issues.push({ code: 'sitemap-status', url, status: response.status });
      const urls = locations(source);
      if (!urls.length) issues.push({ code: 'sitemap-empty', url });
      return urls;
    } catch (error) {
      issues.push({ code: 'sitemap-request', url, error: error.message });
      return [];
    }
  });

  const publicUrls = [...new Set(sitemapGroups.flat())];
  const publicUrlSet = new Set(publicUrls);
  const runtimeAssetUrls = new Set();
  for (const file of collectRuntimeJsonFiles({ root: ROOT })) {
    if (file !== 'manifest.json' && file !== 'assets/js/search-index.json') {
      runtimeAssetUrls.add(policy.toUrl(file));
    }
  }
  for (const file of siteFiles().filter(value => value.endsWith('.html'))) {
    const canonicalUrl = policy.toUrl(file);
    if (!publicUrlSet.has(canonicalUrl)) continue;
    const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
    for (const assetUrl of runtimeJsonReferences(source, canonicalUrl)) runtimeAssetUrls.add(assetUrl);
  }
  let completedHeads = 0;
  const heads = runtimeOnly ? [] : await pool(publicUrls, async canonicalUrl => {
    const url = target(canonicalUrl);
    try {
      const response = await request(url, { method: 'HEAD', headers: { accept: 'text/html' } });
      const type = response.headers.get('content-type') || '';
      const xRobots = response.headers.get('x-robots-tag') || '';
      if (response.status !== 200) issues.push({ code: 'page-status', url, status: response.status, location: response.headers.get('location') });
      if (response.status === 200 && !type.toLowerCase().includes('text/html')) issues.push({ code: 'page-content-type', url, value: type });
      if (!previewNoindex && /noindex/i.test(xRobots)) issues.push({ code: 'page-x-robots-noindex', url, value: xRobots });
      return { url, status: response.status };
    } catch (error) {
      issues.push({ code: 'page-request', url, error: error.message });
      return { url, error: error.message };
    } finally {
      completedHeads++;
      if (completedHeads % 500 === 0 || completedHeads === publicUrls.length) console.log(`Checked ${completedHeads}/${publicUrls.length} sitemap URLs`);
    }
  });

  const runtimeAssets = await pool([...runtimeAssetUrls], async assetUrl => {
    const url = target(assetUrl);
    try {
      const response = await request(url, { method: 'HEAD', headers: { accept: 'application/json,text/plain' } });
      const contentType = response.headers.get('content-type') || '';
      const passed = response.status === 200 && (!contentType || /json|javascript|text\/plain/i.test(contentType));
      if (!passed) issues.push({ code: 'runtime-asset-status', url, status: response.status, contentType });
      return { url, status: response.status, contentType, passed };
    } catch (error) {
      issues.push({ code: 'runtime-asset-request', url, error: error.message });
      return { url, error: error.message, passed: false };
    }
  }, runtimeConcurrency);

  const samples = runtimeOnly ? [] : chooseSamples(sitemapGroups);
  const sampledPages = await pool(samples, async canonicalUrl => {
    const url = target(canonicalUrl);
    try {
      const response = await request(url, { headers: { accept: 'text/html' } });
      const source = await response.text();
      const $ = cheerio.load(source);
      const canonicals = $('link[rel="canonical"]').map((_, el) => $(el).attr('href')).get();
      const descriptions = $('meta[name="description"]');
      const ogUrls = $('meta[property="og:url"]').map((_, el) => $(el).attr('content')).get();
      const robots = $('meta[name="robots"]').attr('content') || '';
      const jsonErrors = [];
      $('script[type="application/ld+json"]').each((_, el) => {
        try { JSON.parse($(el).html()); } catch (error) { jsonErrors.push(error.message); }
      });
      const runtimeAssets = [];
      for (const assetUrl of runtimeJsonReferences(source, url)) {
        try {
          const assetResponse = await request(assetUrl, { method: 'HEAD', headers: { accept: 'application/json,text/plain' } });
          const contentType = assetResponse.headers.get('content-type') || '';
          const passed = assetResponse.status === 200 && (!contentType || /json|javascript|text\/plain/i.test(contentType));
          runtimeAssets.push({ url: assetUrl, status: assetResponse.status, contentType, passed });
          if (!passed) issues.push({ code: 'sample-runtime-asset', url: assetUrl, page: url, status: assetResponse.status, contentType });
        } catch (error) {
          runtimeAssets.push({ url: assetUrl, error: error.message, passed: false });
          issues.push({ code: 'sample-runtime-asset-request', url: assetUrl, page: url, error: error.message });
        }
      }
      const checks = {
        canonical: canonicals.length === 1 && canonicals[0] === canonicalUrl,
        description: descriptions.length === 1 && Boolean(descriptions.attr('content')?.trim()),
        ogUrl: ogUrls.length === 1 && ogUrls[0] === canonicalUrl,
        h1: $('h1').length === 1,
        indexable: !/noindex/i.test(robots),
        jsonLd: jsonErrors.length === 0,
        runtimeAssets: runtimeAssets.every(asset => asset.passed),
      };
      for (const [name, passed] of Object.entries(checks)) {
        if (!passed) issues.push({ code: `sample-${name}`, url, canonicalUrl, value: name === 'jsonLd' ? jsonErrors : undefined });
      }
      return { url, canonicalUrl, status: response.status, bytes: Buffer.byteLength(source), runtimeAssets, checks };
    } catch (error) {
      issues.push({ code: 'sample-request', url, canonicalUrl, error: error.message });
      return { url, canonicalUrl, error: error.message };
    }
  });

  const result = {
    generatedAt: new Date().toISOString(), base: base.href, canonicalOrigin, previewNoindex, runtimeOnly,
    sitemapFiles: sitemapUrls.length, sitemapUrls: publicUrls.length,
    runtimeAssets: runtimeAssets.length,
    runtimeAssetsPassed: runtimeAssets.filter(row => row.passed).length,
    headPassed: heads.filter(row => row.status === 200).length,
    sampledPages: sampledPages.length,
    sampledPassed: sampledPages.filter(row => row.checks && Object.values(row.checks).every(Boolean)).length,
    issues,
  };
  const output = path.join(ROOT, 'scratch/seo-hosting.json');
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, JSON.stringify({ ...result, samples: sampledPages }, null, 2) + '\n');
  console.log(JSON.stringify(result, null, 2));
  if (issues.length) process.exitCode = 1;
}

main().catch(error => { console.error(error); process.exitCode = 1; });
