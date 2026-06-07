'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const cheerio = require('cheerio');

const fetchFn = typeof fetch !== 'undefined' ? fetch : require('undici').fetch;

const ROOT = path.resolve(__dirname, '..', '..', '..');
const CONFIG_PATH = path.join(__dirname, 'config', 'portals.json');
const PROCESSED_PATH = path.join(ROOT, 'sarkari-jobs', 'data', 'processed.json');
const RAW_DIR = path.join(__dirname, 'raw');

// === Time helpers (IST is the canonical timezone for Indian government jobs) ===

function todayIST() {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).format(new Date());
}

function nowIST() {
  const parts = new Intl.DateTimeFormat('en-IN', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  }).formatToParts(new Date());
  const get = t => parts.find(p => p.type === t).value;
  return `${get('year')}-${get('month')}-${get('day')}T${get('hour')}:${get('minute')}:${get('second')}+05:30`;
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function randomDelay(minMs, maxMs) {
  const span = Math.max(0, maxMs - minMs);
  return sleep(minMs + Math.floor(Math.random() * span));
}

// === IO helpers ===

function ensureDir(p) {
  if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
}

function loadJson(p, fallback) {
  if (!fs.existsSync(p)) return fallback;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch (err) { console.error(`[fetch] WARN: failed to parse ${p}: ${err.message}`); return fallback; }
}

function saveJson(p, data) {
  ensureDir(path.dirname(p));
  fs.writeFileSync(p, JSON.stringify(data, null, 2), 'utf8');
}

// === ID + dedup ===

function sha1(s) {
  return crypto.createHash('sha1').update(s).digest('hex');
}

function makeId(portalId, url) {
  return `${portalId}-${sha1(`${portalId}|${url}`).slice(0, 16)}`;
}

function loadProcessedIds() {
  const data = loadJson(PROCESSED_PATH, { ids: [], entries: {} });
  return new Set(data.ids || []);
}

// === Date parser - handles DD/MM/YYYY, ISO, "5 June 2026", Hindi month names ===

const HINDI_MONTHS = {
  'जनवरी': 1, 'फ़रवरी': 2, 'फरवरी': 2, 'मार्च': 3, 'अप्रैल': 4, 'मई': 5, 'जून': 6,
  'जुलाई': 7, 'अगस्त': 8, 'सितंबर': 9, 'सितम्बर': 9, 'अक्टूबर': 10, 'अक्तूबर': 10,
  'नवंबर': 11, 'नवम्बर': 11, 'दिसंबर': 12, 'दिसम्बर': 12
};

const ENGLISH_MONTHS = {
  jan: 1, january: 1, feb: 2, february: 2, mar: 3, march: 3, apr: 4, april: 4,
  may: 5, jun: 6, june: 6, jul: 7, july: 7, aug: 8, august: 8, sep: 9, sept: 9, september: 9,
  oct: 10, october: 10, nov: 11, november: 11, dec: 12, december: 12
};

function pad2(n) { return String(n).padStart(2, '0'); }

function parseDate(raw) {
  if (!raw) return null;
  const text = String(raw).trim().replace(/\s+/g, ' ');
  if (!text) return null;

  // ISO: 2026-06-05 or 2026/06/05
  let m = text.match(/^(\d{4})[-\/.](\d{1,2})[-\/.](\d{1,2})$/);
  if (m) return `${m[1]}-${pad2(m[2])}-${pad2(m[3])}`;

  // DD/MM/YYYY or DD-MM-YYYY (Indian convention)
  m = text.match(/^(\d{1,2})[-\/.](\d{1,2})[-\/.](\d{2,4})$/);
  if (m) {
    let yyyy = m[3].length === 2 ? `20${m[3]}` : m[3];
    return `${yyyy}-${pad2(m[2])}-${pad2(m[1])}`;
  }

  // "5 June 2026" / "June 5, 2026" / "Jun 5 2026"
  m = text.match(/^(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})$/);
  if (m && ENGLISH_MONTHS[m[2].toLowerCase()]) {
    return `${m[3]}-${pad2(ENGLISH_MONTHS[m[2].toLowerCase()])}-${pad2(m[1])}`;
  }
  m = text.match(/^([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})$/);
  if (m && ENGLISH_MONTHS[m[1].toLowerCase()]) {
    return `${m[3]}-${pad2(ENGLISH_MONTHS[m[1].toLowerCase()])}-${pad2(m[2])}`;
  }

  // Hindi: "05 जून 2026" or "जून 05, 2026"
  m = text.match(/^(\d{1,2})\s+([\u0900-\u097F]+)\s+(\d{4})$/);
  if (m && HINDI_MONTHS[m[2]]) {
    return `${m[3]}-${pad2(HINDI_MONTHS[m[2]])}-${pad2(m[1])}`;
  }
  m = text.match(/^([\u0900-\u097F]+)\s+(\d{1,2}),?\s+(\d{4})$/);
  if (m && HINDI_MONTHS[m[1]]) {
    return `${m[3]}-${pad2(HINDI_MONTHS[m[1]])}-${pad2(m[2])}`;
  }

  return null;
}

// === PDF URL resolution ===

function isLikelyPdfHref(href) {
  if (!href) return false;
  const h = href.toLowerCase();
  return h.endsWith('.pdf') || h.includes('.pdf?') || h.includes('filetype=pdf') || h.includes('/pdf/');
}

function isLikelyNotificationHref(href) {
  if (!href) return false;
  const h = href.toLowerCase();
  return h.includes('notification') || h.includes('advt') || h.includes('advertisement') || h.includes('notice') || h.includes('recruitment') || h.includes('vacancy') || h.includes('getfile') || h.includes('download');
}

function resolveUrl(href, base) {
  if (!href) return null;
  try { return new URL(href, base).toString(); }
  catch { return null; }
}

function extractPdfCandidates($, $container, baseUrl) {
  const direct = [];
  const indirect = [];
  $container.find('a[href]').each((_, el) => {
    const href = $(el).attr('href');
    const abs = resolveUrl(href, baseUrl);
    if (!abs) return;
    if (isLikelyPdfHref(abs) || isLikelyPdfHref(href)) direct.push(abs);
    else if (isLikelyNotificationHref(href) || isLikelyNotificationHref(abs)) indirect.push(abs);
  });
  // De-duplicate while preserving order
  const seen = new Set();
  const uniq = arr => arr.filter(u => (seen.has(u) ? false : (seen.add(u), true)));
  return { pdfUrl: uniq(direct)[0] || null, candidates: uniq([...direct, ...indirect]).slice(0, 5) };
}

// === HTML scraper (cheerio) ===

function scrapeHtml(html, baseUrl, selectors) {
  const $ = cheerio.load(html);
  const items = [];
  $(selectors.container).each((_, el) => {
    const $el = $(el);
    const rawTitle = $el.find(selectors.title).first().text().trim().replace(/\s+/g, ' ');
    const rawDate = $el.find(selectors.date).first().text().trim();
    const { pdfUrl, candidates } = extractPdfCandidates($, $el, baseUrl);
    let sourceUrl = null;
    if (selectors.link) {
      const $a = $el.is('a[href]') ? $el : $el.find('a[href]').first();
      sourceUrl = resolveUrl($a.attr('href'), baseUrl);
    }
    if (!rawTitle) return;
    items.push({
      title: rawTitle,
      notificationDate: parseDate(rawDate),
      sourceUrl,
      pdfUrl,
      candidateUrls: candidates
    });
  });
  return items;
}

// === Fetch wrapper ===

async function fetchWithRetry(url, opts, retries = 2) {
  let lastErr;
  for (let attempt = 0; attempt <= retries; attempt++) {
    const controller = new AbortController();
    const timeoutMs = (opts && opts.timeoutMs) || 15000;
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const res = await fetchFn(url, {
        signal: controller.signal,
        redirect: 'follow',
        headers: {
          'User-Agent': (opts && opts.userAgent) || 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 SJMathsSarkariBot/1.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-IN,en;q=0.9,hi;q=0.8'
        }
      });
      clearTimeout(timer);
      if (res.status === 429 || res.status >= 500) {
        throw new Error(`HTTP ${res.status}`);
      }
      if (!res.ok) {
        return { ok: false, status: res.status, html: null, finalUrl: res.url };
      }
      const html = await res.text();
      return { ok: true, status: 200, html, finalUrl: res.url || url };
    } catch (err) {
      clearTimeout(timer);
      lastErr = err;
      if (attempt < retries) await sleep(1500 * (attempt + 1));
    }
  }
  return { ok: false, status: 0, html: null, finalUrl: url, error: lastErr && lastErr.message };
}

// === Aggregator fallback (placeholder for v1) ===
// Implemented SarkariResult aggregator search + cross-source PDF-URL dedup here.

async function fetchViaAggregator(portal, config) {
  if (!portal.useAggregatorFallback || !config.aggregatorFallback?.enabled) return [];
  
  const provider = config.aggregatorFallback.providers.find(p => p.enabled);
  if (!provider) return [];

  console.log(`[fetch] [${portal.id}] executing aggregator fallback via ${provider.id}`);
  const searchUrl = provider.searchUrlTemplate.replace('{query}', encodeURIComponent(portal.shortName || portal.id));
  
  const fs2 = config.fetchSettings || {};
  const ua = fs2.userAgent;
  
  const results = [];
  
  // 1. Fetch Search Results
  console.log(`[fetch] [${portal.id}] [agg] GET ${searchUrl}`);
  const searchRes = await fetchWithRetry(searchUrl, { userAgent: ua });
  if (!searchRes.ok) {
    console.warn(`[fetch] [${portal.id}] [agg] search FAILED (${searchRes.status}) - ${searchUrl}`);
    return [];
  }

  const $ = cheerio.load(searchRes.html);
  const linksToVisit = [];
  
  $(provider.selectors.searchContainer).each((_, el) => {
    const $el = $(el);
    const title = $el.find(provider.selectors.searchTitle).first().text().trim();
    let href = null;
    
    if (provider.selectors.searchLink.endsWith('@href')) {
        const sel = provider.selectors.searchLink.split('@')[0];
        href = $el.is(sel) ? $el.attr('href') : $el.find(sel).first().attr('href');
    } else {
        href = $el.find(provider.selectors.searchLink).first().attr('href');
    }

    if (href && title) {
        const absHref = resolveUrl(href, searchRes.finalUrl);
        if (absHref) linksToVisit.push({ title, url: absHref });
    }
  });

  console.log(`[fetch] [${portal.id}] [agg] found ${linksToVisit.length} candidate links`);

  // 2. Fetch Individual Job Pages (limit to top 3 to avoid spamming)
  for (const link of linksToVisit.slice(0, 3)) {
    await randomDelay(fs2.minDelayMs || 1000, fs2.maxDelayMs || 3000);
    console.log(`[fetch] [${portal.id}] [agg] GET job page: ${link.url}`);
    
    const jobRes = await fetchWithRetry(link.url, { userAgent: ua });
    if (!jobRes.ok) continue;

    const $job = cheerio.load(jobRes.html);
    
    // Custom contains pseudo-selector implementation for Cheerio
    const findByContains = (selectorText) => {
        const match = selectorText.match(/(.*?):contains\(['"](.*?)['"]\)/);
        if (match) {
            const elType = match[1] || '*';
            const textToFind = match[2];
            return $job(elType).filter(function() {
                return $job(this).text().includes(textToFind);
            }).first().attr('href');
        }
        return null;
    };

    let pdfHref = null;
    let officialHref = null;

    // Try multiple possible selectors for PDF link
    const pdfSelectors = provider.selectors.jobPdfLink.split(',').map(s => s.trim());
    for (const sel of pdfSelectors) {
        pdfHref = findByContains(sel);
        if (pdfHref) break;
    }

    const officialSelectors = provider.selectors.jobOfficialLink.split(',').map(s => s.trim());
    for (const sel of officialSelectors) {
        officialHref = findByContains(sel);
        if (officialHref) break;
    }

    const absPdfUrl = resolveUrl(pdfHref, jobRes.finalUrl);
    const absOfficialUrl = resolveUrl(officialHref, jobRes.finalUrl);

    if (absPdfUrl || absOfficialUrl) {
         // Attempt to extract date from the title or page if possible. For now, null.
         results.push({
            title: link.title,
            notificationDate: null, 
            sourceUrl: absOfficialUrl || link.url,
            pdfUrl: absPdfUrl,
            candidateUrls: absPdfUrl ? [absPdfUrl] : []
        });
    }
  }

  return results;
}

// === Main ===

async function scrapePortal(portal, config) {
  const fs2 = config.fetchSettings || {};
  const minD = fs2.minDelayMs || 1000;
  const maxD = fs2.maxDelayMs || 3000;
  const ua = fs2.userAgent;
  const results = [];

  for (const page of portal.listingPages || []) {
    await randomDelay(minD, maxD);
    console.log(`[fetch] [${portal.id}] GET ${page.url}`);
    const r = await fetchWithRetry(page.url, { userAgent: ua });
    if (!r.ok) {
      console.warn(`[fetch] [${portal.id}] FAILED (${r.status}${r.error ? ' ' + r.error : ''}) - ${page.url}`);
      continue;
    }
    let items;
    try {
      items = scrapeHtml(r.html, r.finalUrl, page.selectors);
    } catch (err) {
      console.warn(`[fetch] [${portal.id}] selector error on ${page.url}: ${err.message}`);
      continue;
    }
    console.log(`[fetch] [${portal.id}] parsed ${items.length} items from ${page.url}`);
    for (const it of items) {
      const canonical = it.pdfUrl || it.sourceUrl;
      if (!canonical) continue;
      const id = makeId(portal.id, canonical);
      results.push({
        id,
        portal: portal.id,
        department: portal.department,
        officialWebsite: portal.officialWebsite,
        title: it.title,
        notificationDate: it.notificationDate,
        sourceUrl: it.sourceUrl,
        pdfUrl: it.pdfUrl,
        candidateUrls: it.candidateUrls,
        discoveredAt: nowIST(),
        fetchStatus: it.pdfUrl ? 'pdf-found' : 'pdf-not-found'
      });
    }
  }

  // Aggregator fallback
  const agg = await fetchViaAggregator(portal, config);
  for (const it of agg) {
    const canonical = it.pdfUrl || it.sourceUrl;
    if (!canonical) continue;
    results.push({ ...it, id: makeId(portal.id, canonical), portal: portal.id, department: portal.department, officialWebsite: portal.officialWebsite, discoveredAt: nowIST() });
  }

  return results;
}

async function main() {
  if (!fs.existsSync(CONFIG_PATH)) {
    console.error(`[fetch] FATAL: portals.json not found at ${CONFIG_PATH}`);
    process.exit(1);
  }
  const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  const enabled = (config.portals || []).filter(p => p.enabled);
  console.log(`[fetch] Sarkari Jobs fetch starting - ${enabled.length} portals enabled`);

  const seen = loadProcessedIds();
  console.log(`[fetch] Long-term dedup ledger has ${seen.size} ids`);

  const allNew = [];
  for (const portal of enabled) {
    try {
      const items = await scrapePortal(portal, config);
      for (const it of items) {
        if (seen.has(it.id)) continue;
        allNew.push(it);
        seen.add(it.id);
      }
    } catch (err) {
      console.error(`[fetch] [${portal.id}] CRASH: ${err.message} - continuing with other portals`);
    }
  }

  ensureDir(RAW_DIR);
  const today = todayIST();
  const outPath = path.join(RAW_DIR, `${today}.json`);

  // Merge with any existing same-day output (re-runs within the same day)
  let existing = [];
  if (fs.existsSync(outPath)) {
    try { existing = JSON.parse(fs.readFileSync(outPath, 'utf8')); } catch {}
  }
  const map = new Map();
  for (const it of existing) map.set(it.id, it);
  for (const it of allNew) if (!map.has(it.id)) map.set(it.id, it);
  const merged = Array.from(map.values());

  // Sort: pdf-found first, then by discoveredAt
  merged.sort((a, b) => {
    if (a.fetchStatus !== b.fetchStatus) return a.fetchStatus === 'pdf-found' ? -1 : 1;
    return a.discoveredAt < b.discoveredAt ? 1 : -1;
  });

  saveJson(outPath, merged);

  const pdfFound = merged.filter(i => i.fetchStatus === 'pdf-found').length;
  const pdfMissing = merged.length - pdfFound;
  console.log(`[fetch] Wrote ${merged.length} new items to ${path.relative(ROOT, outPath)} (pdf-found=${pdfFound}, pdf-missing=${pdfMissing})`);
  if (pdfMissing > 0) {
    console.log(`[fetch] NOTE: ${pdfMissing} items have no direct PDF link - download-pdf.js will attempt to resolve from candidateUrls`);
  }
}

main().catch(err => {
  console.error('[fetch] Fatal pipeline error:', err);
  process.exit(1);
});
