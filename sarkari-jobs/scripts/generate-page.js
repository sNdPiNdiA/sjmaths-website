'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');
const PARSED_DIR = path.join(__dirname, 'parsed');
const QUARANTINE_DIR = path.join(__dirname, 'quarantine');

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function loadJson(p, fallback) {
  if (!fs.existsSync(p)) return fallback;
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); }
  catch { return fallback; }
}

function slugify(value) {
  return String(value || 'job')
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '') || 'job';
}

function escapeHtml(value) {
  return String(value || '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function renderJobPage(record) {
  const fields = record.fields || {};
  const bullets = [
    ['Advertisement No', fields.advertisementNo],
    ['Vacancy', fields.vacancy],
    ['Apply Start', fields.applyStart],
    ['Apply End', fields.applyEnd],
    ['Exam Date', fields.examDate],
    ['Age Limit', fields.ageMin && fields.ageMax ? `${fields.ageMin}-${fields.ageMax} years` : null],
    ['Qualification', fields.qualification],
    ['Application Fee', fields.applicationFee],
    ['Physical Standard', fields.physicalStandard],
  ].filter(([, value]) => value);

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${escapeHtml(record.title)} | SJMaths Sarkari Jobs</title>
  <meta name="description" content="${escapeHtml(record.summary || record.title)}" />
  <link rel="canonical" href="https://sjmaths.com/sarkari-jobs/${slugify(record.title)}-${record.id.slice(0, 8)}/" />
  <link rel="stylesheet" href="/assets/css/main.min.css" />
</head>
<body style="background:#f6f8fb;font-family:Arial,sans-serif;color:#18212f;line-height:1.5;">
  <main style="max-width:1100px;margin:0 auto;padding:24px;">
    <nav style="font-size:0.95rem;color:#50607a;margin-bottom:18px;"> <a href="/sarkari-jobs/">Sarkari Jobs</a> &gt; ${escapeHtml(record.title)} </nav>
    <article style="background:#fff;border:1px solid #e5eaf2;border-radius:16px;padding:24px;box-shadow:0 18px 42px rgba(15,23,42,0.08);">
      <p style="text-transform:uppercase;letter-spacing:0.18em;font-size:0.78rem;color:#4f7cff;font-weight:700;">${escapeHtml(record.portal || 'Sarkari Jobs')}</p>
      <h1 style="margin:0 0 8px;font-size:2rem;">${escapeHtml(record.title)}</h1>
      <p style="margin:0 0 16px;color:#50607a;">${escapeHtml(record.department || 'Official government notification')}</p>
      <p style="margin-bottom:18px;">${escapeHtml(record.summary || 'Official notification details will be available once the PDF is processed.')}</p>
      <ul style="display:grid;gap:10px;padding-left:18px;color:#243244;">
        ${bullets.map(([label, value]) => `<li><strong>${escapeHtml(label)}:</strong> ${escapeHtml(value)}</li>`).join('')}
      </ul>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:18px;">
        ${record.pdfUrl ? `<a href="${escapeHtml(record.pdfUrl)}" target="_blank" rel="noreferrer" style="display:inline-block;padding:10px 14px;background:#1d4ed8;color:#fff;border-radius:10px;text-decoration:none;">Open Official PDF</a>` : ''}
        ${record.sourceUrl ? `<a href="${escapeHtml(record.sourceUrl)}" target="_blank" rel="noreferrer" style="display:inline-block;padding:10px 14px;background:#0f172a;color:#fff;border-radius:10px;text-decoration:none;">View Source Page</a>` : ''}
      </div>
      <p style="margin-top:18px;color:#50607a;font-size:0.95rem;">Published: ${escapeHtml(record.publishDate || record.discoveredAt || 'Not available')}</p>
    </article>
  </main>
</body>
</html>`;
}

function main() {
  const parsedFiles = fs.existsSync(PARSED_DIR)
    ? fs.readdirSync(PARSED_DIR).filter(f => f.endsWith('.json')).sort()
    : [];

  if (parsedFiles.length === 0) {
    console.log('[generate] No parsed job files found');
    return;
  }

  let written = 0;
  for (const file of parsedFiles) {
    const record = loadJson(path.join(PARSED_DIR, file), null);
    if (!record || record.quarantine) continue;

    const slug = `${slugify(record.title)}-${record.id.slice(0, 8)}`;
    const outDir = path.join(ROOT, 'sarkari-jobs', slug);
    ensureDir(outDir);
    fs.writeFileSync(path.join(outDir, 'index.html'), renderJobPage(record), 'utf8');
    written += 1;
    console.log(`[generate] Wrote ${outDir}`);
  }

  console.log(`[generate] Summary: pages=${written}`);
}

main();
