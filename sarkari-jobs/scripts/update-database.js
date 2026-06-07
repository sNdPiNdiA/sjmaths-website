'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT = path.resolve(__dirname, '..', '..');
const DATA_DIR = path.join(ROOT, 'sarkari-jobs', 'data');
const PARSED_DIR = path.join(__dirname, 'parsed');
const QUARANTINE_DIR = path.join(__dirname, 'quarantine');
const RAW_DIR = path.join(__dirname, 'raw');

function ensureDir(p) { fs.mkdirSync(p, { recursive: true }); }
function loadJson(p, fallback) { if (!fs.existsSync(p)) return fallback; try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return fallback; } }
function saveJson(p, data) { ensureDir(path.dirname(p)); fs.writeFileSync(p, JSON.stringify(data, null, 2), 'utf8'); }
function sha1(value) { return crypto.createHash('sha1').update(String(value)).digest('hex'); }
function nowIST() { return new Intl.DateTimeFormat('en-IN', { timeZone: 'Asia/Kolkata', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }).formatToParts(new Date()).reduce((acc, part) => { if (part.type !== 'literal') acc[part.type] = part.value; return acc; }, {}); }
function isoIST() { const p = nowIST(); return `${p.year}-${p.month}-${p.day}T${p.hour}:${p.minute}:${p.second}+05:30`; }
function slugify(value) { return String(value || 'job').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') || 'job'; }
function toDate(value) { return value ? String(value).slice(0, 10) : null; }

function loadRawItems() {
  const files = fs.readdirSync(RAW_DIR).filter(f => f.endsWith('.json')).sort().reverse();
  if (!files.length) return [];
  return loadJson(path.join(RAW_DIR, files[0]), []);
}

function main() {
  ensureDir(DATA_DIR);
  const jobsFile = path.join(DATA_DIR, 'jobs.json');
  const processedFile = path.join(DATA_DIR, 'processed.json');

  const existingJobs = loadJson(jobsFile, { version: 1, lastUpdated: null, cap: 500, jobs: [] }).jobs || [];
  const ledger = loadJson(processedFile, { version: 1, ids: [], entries: {} });

  const rawItems = loadRawItems();
  const rawMap = new Map(rawItems.map(item => [item.id, item]));

  const parsedFiles = fs.existsSync(PARSED_DIR) ? fs.readdirSync(PARSED_DIR).filter(f => f.endsWith('.json')).sort() : [];
  const parsedJobs = [];

  for (const file of parsedFiles) {
    const record = loadJson(path.join(PARSED_DIR, file), null);
    if (!record || record.quarantine) continue;
    const raw = rawMap.get(record.id) || {};
    const slug = `${slugify(record.title)}-${record.id.slice(0, 8)}`;
    parsedJobs.push({
      id: record.id,
      portal: record.portal,
      title: record.title,
      department: record.department,
      officialWebsite: record.officialWebsite,
      sourceUrl: record.sourceUrl || raw.sourceUrl || null,
      pdfUrl: record.pdfUrl || raw.pdfUrl || null,
      publishDate: toDate(record.publishDate || raw.notificationDate || raw.discoveredAt || null),
      discoveredAt: record.discoveredAt || raw.discoveredAt || null,
      pageUrl: `/sarkari-jobs/${slug}/`,
      vacancy: record.fields?.vacancy || null,
      applyStart: record.fields?.applyStart || null,
      applyEnd: record.fields?.applyEnd || null,
      qualification: record.fields?.qualification || null,
      summary: record.summary || null,
      qualityScore: record.qualityScore || 0,
      hash: sha1(`${record.id}|${record.pdfUrl || ''}`),
      mode: 'notification'
    });
  }

  const merged = [...existingJobs];
  for (const job of parsedJobs) {
    if (!ledger.ids.includes(job.id)) {
      merged.unshift(job);
      ledger.ids.push(job.id);
      ledger.entries[job.id] = { id: job.id, addedAt: isoIST(), title: job.title };
    }
  }

  merged.sort((a, b) => (a.publishDate || '0000-00-00') < (b.publishDate || '0000-00-00') ? 1 : -1);
  const trimmed = merged.slice(0, 500);

  saveJson(jobsFile, { version: 1, lastUpdated: isoIST(), cap: 500, jobs: trimmed });
  saveJson(processedFile, { version: 1, ids: Array.from(new Set(ledger.ids)), entries: ledger.entries });

  console.log(`[database] jobs=${trimmed.length}, new=${parsedJobs.length}, ledger=${ledger.ids.length}`);
}

main();
