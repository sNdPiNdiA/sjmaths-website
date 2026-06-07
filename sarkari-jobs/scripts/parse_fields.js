'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const CONFIG_PATH = path.join(__dirname, 'config', 'portals.json');
const RAW_DIR = path.join(__dirname, 'raw');
const PARSED_DIR = path.join(__dirname, 'parsed');
const QUARANTINE_DIR = path.join(__dirname, 'quarantine');
const EXTRACT_DIR = path.join(ROOT, 'sarkari-jobs', 'extracted-text');

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function loadJson(p, fallback) {
  if (!fs.existsSync(p)) return fallback;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch { return fallback; }
}

function saveJson(p, data) {
  ensureDir(path.dirname(p));
  fs.writeFileSync(p, JSON.stringify(data, null, 2), 'utf8');
}

function todayIST() {
  return new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  }).format(new Date());
}

function parseDate(raw) {
  if (!raw) return null;
  const text = String(raw).trim();
  const m = text.match(/(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})/);
  return m ? m[1] : null;
}

function sanitizeText(text) {
  return String(text || '').replace(/\s+/g, ' ').trim();
}

function findValue(text, patterns) {
  for (const pattern of patterns) {
    if (!pattern) continue;
    const match = text.match(new RegExp(pattern, 'i'));
    if (match) {
      return sanitizeText(match[1] || match[0]);
    }
  }
  return null;
}

function buildRecord(item, portalConfig, text) {
  const regex = portalConfig.regex || {};
  const fields = {
    advertisementNo: findValue(text, [regex.advertisement_no]),
    vacancy: findValue(text, [regex.vacancy]),
    applyStart: findValue(text, [regex.apply_start]),
    applyEnd: findValue(text, [regex.apply_end]),
    examDate: findValue(text, [regex.exam_date]),
    ageMin: findValue(text, [regex.age_min]),
    ageMax: findValue(text, [regex.age_max]),
    qualification: findValue(text, [regex.qualification]),
    applicationFee: findValue(text, [regex.application_fee]),
    physicalStandard: findValue(text, [regex.physical_standard]),
  };

  const candidate = item.pdfUrl || item.sourceUrl || item.candidateUrls?.[0] || null;
  const summary = sanitizeText(text).slice(0, 180) || sanitizeText(item.title || '');
  const publishDate = parseDate(item.notificationDate || '') || item.notificationDate || null;

  return {
    id: item.id,
    portal: item.portal,
    title: sanitizeText(item.title || 'Untitled job notification'),
    department: item.department || portalConfig.department || null,
    officialWebsite: item.officialWebsite || portalConfig.officialWebsite || null,
    sourceUrl: item.sourceUrl || null,
    pdfUrl: item.pdfUrl || null,
    candidateUrls: item.candidateUrls || [],
    discoveredAt: item.discoveredAt || null,
    publishDate,
    summary,
    fields,
    generatedAt: new Date().toISOString(),
    qualityScore: [fields.vacancy, fields.applyEnd, fields.qualification].filter(Boolean).length / 3,
    quarantine: !fields.vacancy || !fields.applyEnd,
    textSource: fs.existsSync(path.join(EXTRACT_DIR, `${item.id}.txt`)) ? 'pdf-text' : 'title-only'
  };
}

function main() {
  if (!fs.existsSync(CONFIG_PATH)) {
    console.error('[parse] FATAL: portals.json not found');
    process.exit(1);
  }

  const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  ensureDir(PARSED_DIR);
  ensureDir(QUARANTINE_DIR);

  const rawFiles = fs.readdirSync(RAW_DIR).filter(f => f.endsWith('.json')).sort().reverse();
  if (rawFiles.length === 0) {
    console.log('[parse] No raw files to parse');
    return;
  }

  const rawPath = path.join(RAW_DIR, rawFiles[0]);
  const items = loadJson(rawPath, []);
  const portalMap = new Map((config.portals || []).map(p => [p.id, p]));

  let parsed = 0;
  let quarantined = 0;

  for (const item of items) {
    const portalConfig = portalMap.get(item.portal) || {};
    const textPath = path.join(EXTRACT_DIR, `${item.id}.txt`);
    const text = fs.existsSync(textPath) ? fs.readFileSync(textPath, 'utf8') : sanitizeText(item.title || '');
    const record = buildRecord(item, portalConfig, text);

    const outPath = path.join(record.quarantine ? QUARANTINE_DIR : PARSED_DIR, `${item.id}.json`);
    saveJson(outPath, record);

    if (record.quarantine) quarantined += 1;
    else parsed += 1;
    console.log(`[parse] ${record.quarantine ? 'Q' : 'OK'} ${item.id} (${record.title})`);
  }

  console.log(`[parse] Summary: parsed=${parsed}, quarantined=${quarantined}, date=${todayIST()}`);
}

main();
