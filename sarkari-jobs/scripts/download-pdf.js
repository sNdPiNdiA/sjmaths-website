'use strict';

const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const fetchFn = typeof fetch !== 'undefined' ? fetch : require('undici').fetch;

const ROOT = path.resolve(__dirname, '..', '..', '..');
const CONFIG_PATH = path.join(__dirname, 'config', 'portals.json');
const PDF_DIR = path.join(ROOT, 'sarkari-jobs', 'pdfs');
const EXTRACT_DIR = path.join(ROOT, 'sarkari-jobs', 'extracted-text');
const RAW_DIR = path.join(__dirname, 'raw');

const MAX_PDF_BYTES = 50 * 1024 * 1024;       // 50 MB hard cap (most Indian govt PDFs are < 30 MB)
const PER_ATTEMPT_TIMEOUT_MS = 60000;         // 60s per GET/HEAD
const MAX_PARALLEL = 3;                       // 3 concurrent downloads
const PER_ITEM_BUDGET_MS = 120000;            // 120s total per item
const MAX_RETRIES = 2;                        // 2 retries per URL
const USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 SJMathsSarkariBot/1.0';

function todayIST() {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).format(new Date());
}

const sleep = ms => new Promise(r => setTimeout(r, ms));

function ensureDir(p) { if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true }); }

function loadJson(p, fallback) {
  if (!fs.existsSync(p)) return fallback;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return fallback; }
}

function saveJson(p, data) {
  ensureDir(path.dirname(p));
  fs.writeFileSync(p, JSON.stringify(data, null, 2), 'utf8');
}

// === HEAD probe: fast fail for dead/oversized URLs ===

async function headProbe(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 5000);
  try {
    const res = await fetchFn(url, {
      method: 'HEAD',
      signal: controller.signal,
      redirect: 'follow',
      headers: { 'User-Agent': USER_AGENT, 'Accept': '*/*' }
    });
    clearTimeout(timer);
    if (!res.ok) return { alive: false, status: res.status };
    const ct = (res.headers.get('content-type') || '').toLowerCase();
    const cl = parseInt(res.headers.get('content-length') || '0', 10);
    return { alive: true, status: res.status, contentType: ct, size: cl };
  } catch (err) {
    clearTimeout(timer);
    return { alive: false, status: 0, error: err.message };
  }
}

async function downloadToFile(url, destPath) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), PER_ATTEMPT_TIMEOUT_MS);
  try {
    const res = await fetchFn(url, {
      method: 'GET',
      signal: controller.signal,
      redirect: 'follow',
      headers: {
        'User-Agent': USER_AGENT,
        'Accept': 'application/pdf,application/octet-stream,text/html;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-IN,en;q=0.9,hi;q=0.8'
      }
    });
    if (!res.ok) {
      clearTimeout(timer);
      return { ok: false, status: res.status, error: `HTTP ${res.status}` };
    }

    const ct = (res.headers.get('content-type') || '').toLowerCase();
    const declared = parseInt(res.headers.get('content-length') || '0', 10);
    if (declared && declared > MAX_PDF_BYTES) {
      clearTimeout(timer);
      return { ok: false, status: res.status, error: `declared ${declared} > cap ${MAX_PDF_BYTES}` };
    }

    // Read body - signal is respected during arrayBuffer
    const buf = Buffer.from(await res.arrayBuffer());
    clearTimeout(timer);

    if (buf.length > MAX_PDF_BYTES) {
      return { ok: false, status: res.status, error: `body ${buf.length} > cap` };
    }
    const isPdf = buf.length >= 5 && buf.slice(0, 5).toString('ascii') === '%PDF-';
    const isHtml = buf.length >= 15 && buf.slice(0, 15).toString('ascii').toLowerCase().includes('<!doctype html');
    if (isHtml && !isPdf) {
      return { ok: false, status: res.status, error: 'response is HTML, not a PDF' };
    }
    if (!isPdf && !ct.includes('pdf') && !ct.includes('octet-stream')) {
      return { ok: false, status: res.status, error: `content-type "${ct}" and no PDF magic` };
    }
    fs.writeFileSync(destPath, buf);
    return { ok: true, status: res.status, size: buf.length, contentType: ct };
  } catch (err) {
    clearTimeout(timer);
    const aborted = err && (err.name === 'AbortError' || /aborted/i.test(err.message || ''));
    return { ok: false, status: 0, error: aborted ? `timeout after ${PER_ATTEMPT_TIMEOUT_MS}ms` : (err && err.message ? err.message : String(err)) };
  }
}

// === Build candidate list: prefer direct pdfUrl, then candidateUrls, then sourceUrl page fallback ===

function isLikelyPdfUrl(url) {
  if (!url) return false;
  const u = String(url).toLowerCase();
  return u.endsWith('.pdf') || u.includes('.pdf?') || u.includes('filetype=pdf') || u.includes('/pdf/');
}

function extractPdfLinksFromHtml(html, baseUrl) {
  const $ = cheerio.load(html || '');
  const seen = new Set();
  const out = [];
  $('a[href]').each((_, el) => {
    const href = $(el).attr('href');
    if (!href) return;
    let abs = null;
    try { abs = new URL(href, baseUrl).toString(); } catch { return; }
    if (isLikelyPdfUrl(abs) && !seen.has(abs)) {
      seen.add(abs);
      out.push(abs);
    }
  });
  return out;
}

function buildCandidates(item) {
  const seen = new Set();
  const out = [];
  if (item.pdfUrl) { out.push({ url: item.pdfUrl, isDirect: true }); seen.add(item.pdfUrl); }
  for (const u of (item.candidateUrls || [])) {
    if (u && !seen.has(u)) { out.push({ url: u, isDirect: false }); seen.add(u); }
  }
  return out;
}

async function expandCandidatesFromSourcePage(item) {
  if (!item.sourceUrl || !/https?:/i.test(item.sourceUrl)) return [];
  try {
    const res = await fetchFn(item.sourceUrl, {
      method: 'GET',
      redirect: 'follow',
      headers: {
        'User-Agent': USER_AGENT,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-IN,en;q=0.9,hi;q=0.8'
      }
    });
    if (!res.ok) return [];
    const html = await res.text();
    return extractPdfLinksFromHtml(html, item.sourceUrl).map(url => ({ url, isDirect: false }));
  } catch {
    return [];
  }
}

// === Process one item within a per-item time budget ===

async function processItem(item) {
  const start = Date.now();
  const pdfPath = path.join(PDF_DIR, `${item.id}.pdf`);
  const markerPath = path.join(EXTRACT_DIR, `${item.id}.attempted`);
  const donePath = path.join(EXTRACT_DIR, `${item.id}.done`);

  // Idempotency
  if (fs.existsSync(pdfPath) && fs.statSync(pdfPath).size > 0) {
    if (fs.existsSync(donePath)) return { id: item.id, status: 'skipped-complete' };
    ensureDir(EXTRACT_DIR);
    fs.writeFileSync(markerPath, new Date().toISOString());
    return { id: item.id, status: 'skipped-downloaded' };
  }

  let candidates = buildCandidates(item);
  if (candidates.length === 0) {
    candidates = await expandCandidatesFromSourcePage(item);
  }
  if (candidates.length === 0) {
    return { id: item.id, status: 'failed-no-candidates', error: 'no pdfUrl, candidateUrls, or source-page pdf links', elapsedMs: Date.now() - start };
  }

  const tried = [];
  let last;
  for (const c of candidates) {
    if (Date.now() - start > PER_ITEM_BUDGET_MS) {
      return { id: item.id, status: 'failed-budget-exceeded', error: 'item budget exceeded', tried: tried.length, elapsedMs: Date.now() - start };
    }
    tried.push(c.url);

    // For non-direct candidates, HEAD-probe first to fail fast
    if (!c.isDirect) {
      const probe = await headProbe(c.url);
      if (!probe.alive || (probe.size && probe.size > MAX_PDF_BYTES)) {
        continue; // skip dead/oversized URL
      }
    }

    // Try GET (with retries)
    for (let i = 0; i <= MAX_RETRIES; i++) {
      last = await downloadToFile(c.url, pdfPath);
      if (last.ok) {
        ensureDir(EXTRACT_DIR);
        fs.writeFileSync(markerPath, new Date().toISOString());
        return { id: item.id, status: 'downloaded', url: c.url, size: last.size, contentType: last.contentType, elapsedMs: Date.now() - start };
      }
      if (i < MAX_RETRIES && Date.now() - start < PER_ITEM_BUDGET_MS - PER_ATTEMPT_TIMEOUT_MS) {
        await sleep(1000);
      } else {
        break;
      }
    }
  }
  return { id: item.id, status: 'failed-all-candidates', tried: tried.length, elapsedMs: Date.now() - start, lastError: last && last.error };
}

// === Concurrency-limited runner ===

async function runWithConcurrency(items, limit, worker) {
  const results = new Array(items.length);
  let idx = 0;
  const runners = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (true) {
      const i = idx++;
      if (i >= items.length) return;
      results[i] = await worker(items[i]);
    }
  });
  await Promise.all(runners);
  return results;
}

// === Main ===

async function main() {
  if (!fs.existsSync(CONFIG_PATH)) {
    console.error(`[download] FATAL: portals.json not found at ${CONFIG_PATH}`);
    process.exit(1);
  }
  const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  const enabledIds = new Set((config.portals || []).filter(p => p.enabled).map(p => p.id));
  const today = todayIST();
  const rawPath = path.join(RAW_DIR, `${today}.json`);
  const items = loadJson(rawPath, []);
  if (items.length === 0) {
    console.log(`[download] No raw items for ${today} - nothing to do`);
    return;
  }
  const candidates = items.filter(i => enabledIds.has(i.portal));
  console.log(`[download] ${candidates.length} items, concurrency=${MAX_PARALLEL}, per-item budget=${PER_ITEM_BUDGET_MS}ms`);

  ensureDir(PDF_DIR);
  ensureDir(EXTRACT_DIR);

  const t0 = Date.now();
  const results = await runWithConcurrency(candidates, MAX_PARALLEL, processItem);

  let downloaded = 0, failed = 0, skipped = 0, totalBytes = 0;
  for (let i = 0; i < results.length; i++) {
    const r = results[i];
    const item = candidates[i];
    if (r.status === 'downloaded') {
      downloaded++;
      totalBytes += r.size || 0;
      console.log(`[download] OK   ${item.id} (${(r.size / 1024).toFixed(1)} KB in ${(r.elapsedMs / 1000).toFixed(1)}s) ${r.url.slice(0, 80)}`);
    } else if (r.status.startsWith('skipped')) {
      skipped++;
      console.log(`[download] --   ${item.id} ${r.status}`);
    } else {
      failed++;
      const errDetail = r.lastError ? ` - ${r.lastError}` : (r.error ? ` - ${r.error}` : '');
      console.warn(`[download] FAIL ${item.id} ${r.status} (${r.tried || 0} tried, ${(r.elapsedMs / 1000).toFixed(1)}s)${errDetail}`);
    }
  }

  const reportPath = path.join(__dirname, 'download-report.json');
  saveJson(reportPath, { date: today, generatedAt: new Date().toISOString(), downloaded, failed, skipped, totalBytes, results });

  const totalSec = ((Date.now() - t0) / 1000).toFixed(1);
  console.log(`\n[download] Summary: downloaded=${downloaded}, skipped=${skipped}, failed=${failed}, totalSize=${(totalBytes / 1024 / 1024).toFixed(2)} MB, wall=${totalSec}s`);
  if (failed > 0) console.log(`[download] Failed items will be re-attempted on the next pipeline run (idempotent)`);
}

main().catch(err => {
  console.error('[download] Fatal pipeline error:', err);
  process.exit(1);
});
