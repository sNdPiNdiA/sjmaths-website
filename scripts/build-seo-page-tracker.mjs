import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = new Map(process.argv.slice(2).filter(arg => arg.startsWith('--'))
  .map(arg => {
    const splitAt = arg.indexOf('=');
    return splitAt < 0 ? [arg.slice(2), true] : [arg.slice(2, splitAt), arg.slice(splitAt + 1)];
  }));
const reportPath = path.resolve(String(args.get('report') || ''));
const bingCsvPath = path.resolve(String(args.get('bing-csv') || ''));
const outputPath = path.resolve(String(args.get('output') || ''));
const moduleBase = path.resolve(String(args.get('module-base') || ''));
const scanStartedAt = Date.parse(String(args.get('scan-start') || ''));

if (!args.get('report') || !args.get('bing-csv') || !args.get('output') || !args.get('module-base') || !Number.isFinite(scanStartedAt)) {
  throw new Error('Required options: --report=..., --bing-csv=..., --output=..., --module-base=..., --scan-start=ISO_DATE');
}
if (!outputPath.toLowerCase().endsWith('.xlsx')) throw new Error('Output must be an .xlsx workbook.');
if ([reportPath, bingCsvPath].some(file => !path.isAbsolute(file))) throw new Error('Input paths must be absolute.');
if (await fs.stat(outputPath).then(() => true, () => false)) throw new Error(`Refusing to overwrite: ${outputPath}`);

const requireFromRuntime = createRequire(path.join(moduleBase, 'package.json'));
const artifactToolUrl = pathToFileURL(requireFromRuntime.resolve('@oai/artifact-tool'));
const { FileBlob, SpreadsheetFile, Workbook } = await import(artifactToolUrl.href);
const report = JSON.parse(await fs.readFile(reportPath, 'utf8'));
const csvText = await fs.readFile(bingCsvPath, 'utf8');
const rawSourceWorkbook = await Workbook.fromCSV(csvText, { sheetName: 'Bing Pages Raw' });
const rawSourceSheet = rawSourceWorkbook.worksheets.getItem('Bing Pages Raw');
const rawValues = rawSourceSheet.getUsedRange().values;
if (!rawValues?.length || rawValues.length < 2) throw new Error('Bing CSV has no page records.');

const normalizeUrl = value => String(value || '').trim().toLowerCase().replace(/\/$/, '');
const headerIndexes = new Map(rawValues[0].map((value, index) => [String(value).trim().toLowerCase(), index]));
const col = key => {
  const found = headerIndexes.get(key.toLowerCase());
  if (found === undefined) throw new Error(`Missing Bing CSV column: ${key}`);
  return found;
};
const numberValue = value => {
  if (value === null || value === undefined || String(value).trim() === '') return null;
  const parsed = Number(String(value).replace(/,/g, '').trim());
  return Number.isFinite(parsed) ? parsed : null;
};
const percentValue = value => {
  if (value === null || value === undefined || String(value).trim() === '') return null;
  const parsed = Number(String(value).replace(/%/g, '').trim());
  return Number.isFinite(parsed) ? parsed / 100 : null;
};
const bingIndex = new Map();
for (const row of rawValues.slice(1)) {
  const key = normalizeUrl(row[col('Page')]);
  if (!key) continue;
  const list = bingIndex.get(key) || [];
  list.push(row);
  bingIndex.set(key, list);
}

function parseWorktreeStatus() {
  const snapshot = execFileSync('git', ['status', '--porcelain=v1', '-z', '--untracked-files=all'], {
    cwd: ROOT,
    encoding: 'utf8',
    maxBuffer: 20e6,
  });
  const entries = snapshot.split('\0');
  const result = new Map();
  for (let index = 0; index < entries.length; index += 1) {
    const entry = entries[index];
    if (!entry) continue;
    const status = entry.slice(0, 2).trim() || 'clean';
    const file = entry.slice(3).replace(/\\/g, '/');
    result.set(file, status === '??' ? 'untracked' : `changed:${status}`);
    if (status.includes('R') || status.includes('C')) index += 1;
  }
  return result;
}

const statusByFile = parseWorktreeStatus();
const issueCodes = new Map();
for (const issue of report.issues || []) {
  if (!issueCodes.has(issue.file)) issueCodes.set(issue.file, new Set());
  issueCodes.get(issue.file).add(issue.code);
}
const eligible = (report.pages || []).filter(page => page.indexable);
const statByPage = await Promise.all(eligible.map(async page => {
  const absolutePath = path.resolve(ROOT, page.file);
  try {
    const stat = await fs.stat(absolutePath);
    return { page, mtime: stat.mtime, mtimeMs: stat.mtimeMs, exists: true };
  } catch {
    return { page, mtime: null, mtimeMs: null, exists: false };
  }
}));

const headers = [
  'scope_status', 'review_status', 'source_file', 'worktree_state', 'source_last_modified',
  'canonical_url', 'source_route', 'baseline_title', 'baseline_description', 'h1_count',
  'static_word_count', 'in_sitemap', 'automated_finding_codes',
  'gsc_clicks', 'gsc_impressions', 'gsc_ctr', 'gsc_avg_position', 'gsc_checked_on',
  'bing_clicks_web', 'bing_impressions_web', 'bing_ctr_web', 'bing_avg_position_web',
  'bing_page_url', 'bing_url_match', 'bing_checked_on', 'target_query',
  'public_serp_query', 'public_serp_checked_on', 'public_serp_observation',
  'review_notes', 'edit_notes', 'verification_status', 'blocker',
];
const checkedDate = new Date('2026-09-24T00:00:00+05:30');
const safeText = value => {
  if (value === null || value === undefined) return '';
  const text = String(value);
  return /^[\s]*[=+@-]/.test(text) ? `'${text}` : text;
};
const beyondClass9Cutoff = file => {
  if (!/^class-9-/i.test(file)) return false;
  const match = file.match(/chapter-(\d+)/i);
  return Boolean(match && Number(match[1]) > 9);
};

const trackerRows = statByPage.map(({ page, mtime, mtimeMs, exists }) => {
  const excluded = beyondClass9Cutoff(page.file);
  const sourceChangedDuringAudit = mtimeMs !== null && mtimeMs > scanStartedAt;
  const urlKey = normalizeUrl(page.canonical);
  const bingRows = bingIndex.get(urlKey) || [];
  const bing = bingRows.length === 1 ? bingRows[0] : null;
  const sourceState = statusByFile.get(page.file.replace(/\\/g, '/')) || 'clean';
  const reviewStatus = excluded ? 'EXCLUDED' : !exists ? 'SOURCE_MISSING' : sourceChangedDuringAudit ? 'HOLD_FOR_RESCAN' : 'QUEUED';
  const notes = excluded
    ? 'Class 9 after Chapter 9 is outside the requested scope.'
    : !exists
      ? 'Source file is missing; resolve before page review.'
      : sourceChangedDuringAudit
        ? 'Source changed after the crawl began; refresh this row before editing.'
        : '';

  return [
    excluded ? 'OUT_OF_SCOPE_CLASS9_AFTER_CHAPTER9' : 'IN_SCOPE',
    reviewStatus,
    safeText(page.file),
    sourceState,
    mtime || null,
    safeText(page.canonical),
    safeText(page.route),
    safeText(page.title),
    safeText(page.description),
    Number.isFinite(Number(page.h1)) ? Number(page.h1) : null,
    Number.isFinite(Number(page.words)) ? Number(page.words) : null,
    page.sitemap ? 'yes' : 'no',
    [...(issueCodes.get(page.file) || [])].sort().join('; '),
    null, null, null, null, null,
    bing ? numberValue(bing[col('Clicks')]) : null,
    bing ? numberValue(bing[col('Impressions')]) : null,
    bing ? percentValue(bing[col('CTR')]) : null,
    bing ? numberValue(bing[col('Avg. Position')]) : null,
    bing ? safeText(bing[col('Page')]) : '',
    bing ? 'exact canonical URL' : bingRows.length > 1 ? 'duplicate export URL; not merged' : 'no exact canonical match',
    bing ? checkedDate : null,
    '', '', null, '', safeText(notes), '', '', '',
  ];
});

trackerRows.sort((a, b) => {
  const aExcluded = a[0] === 'OUT_OF_SCOPE_CLASS9_AFTER_CHAPTER9' ? 1 : 0;
  const bExcluded = b[0] === 'OUT_OF_SCOPE_CLASS9_AFTER_CHAPTER9' ? 1 : 0;
  if (aExcluded !== bExcluded) return aExcluded - bExcluded;
  const aImpressions = Number.isFinite(a[19]) ? a[19] : -1;
  const bImpressions = Number.isFinite(b[19]) ? b[19] : -1;
  if (aImpressions !== bImpressions) return bImpressions - aImpressions;
  return String(a[5]).localeCompare(String(b[5]));
});

const workbook = Workbook.create();
const tracker = workbook.worksheets.add('SEO Tracker');
const rawSheet = workbook.worksheets.add('Bing Pages Raw');
const rawRange = rawSheet.getRangeByIndexes(0, 0, rawValues.length, rawValues[0].length);
rawRange.values = rawValues;
const startRow = 8;
const lastDataRow = startRow + trackerRows.length;
const lastColumn = 'AG';
const dataRange = tracker.getRange(`A${startRow}:${lastColumn}${lastDataRow}`);
tracker.getRange('A1:B6').values = [
  ['SJMaths SEO page review tracker', ''],
  ['Audit snapshot', `2026-09-24 07:59 Asia/Kolkata. The site-wide scan overlapped a content-generation job; ${statByPage.filter(row => row.mtimeMs !== null && row.mtimeMs > scanStartedAt).length} source pages changed during or after the scan and are marked HOLD_FOR_RESCAN.`],
  ['Coverage', `${eligible.length} indexable page candidates; ${trackerRows.filter(row => row[0] === 'IN_SCOPE').length} in scope and ${trackerRows.filter(row => row[0] !== 'IN_SCOPE').length} Class 9 pages after Chapter 9 excluded.`],
  ['Bing source', `${rawValues.length - 1} URL rows from the 24 Sep 2026 Pages export. The CSV has no query or date-window columns; page detail is Web-only. Exact canonical URL matches only are joined.`],
  ['GSC source', 'Per-page Search Console export was unavailable. Blank GSC fields mean not supplied, not zero.'],
  ['Use', 'Start with QUEUED rows. Re-scan HOLD_FOR_RESCAN rows after the active content-generation job completes. Use the raw Bing tab to investigate URL variants not joined to a canonical page.'],
];
tracker.getRange(`A${startRow}:${lastColumn}${lastDataRow}`).values = [headers, ...trackerRows];

const excelColumn = index => {
  let result = '';
  while (index > 0) {
    const remainder = (index - 1) % 26;
    result = String.fromCharCode(65 + remainder) + result;
    index = Math.floor((index - 1) / 26);
  }
  return result;
};
const trackerTable = tracker.tables.add(`A${startRow}:${excelColumn(headers.length)}${lastDataRow}`, true, 'SEOPageAuditTracker');
trackerTable.showFilterButton = true;
tracker.showGridLines = false;
tracker.freezePanes.freezeRows(startRow);
tracker.freezePanes.freezeColumns(4);
tracker.getRange(`A1:${lastColumn}1`).format = { font: { name: 'Arial', size: 14, bold: true, color: '#234B38' } };
tracker.getRange('A2:A6').format = { font: { name: 'Arial', size: 10, bold: true, color: '#234B38' } };
tracker.getRange('B2:B6').format = { font: { name: 'Arial', size: 10, color: '#30352F' }, wrapText: false, verticalAlignment: 'center' };
tracker.getRange(`A${startRow}:${lastColumn}${startRow}`).format = {
  fill: '#234B38',
  font: { name: 'Arial', size: 10, bold: true, color: '#FFFFFF' },
  horizontalAlignment: 'center',
  verticalAlignment: 'center',
  wrapText: true,
};
tracker.getRange(`A${startRow}:${lastColumn}${lastDataRow}`).format.font = { name: 'Arial', size: 9, color: '#27312B' };
tracker.getRange(`E${startRow + 1}:E${lastDataRow}`).format.numberFormat = 'yyyy-mm-dd hh:mm';
tracker.getRange(`Y${startRow + 1}:Y${lastDataRow}`).format.numberFormat = 'yyyy-mm-dd';
tracker.getRange(`AB${startRow + 1}:AB${lastDataRow}`).format.numberFormat = 'yyyy-mm-dd';
tracker.getRange(`P${startRow + 1}:P${lastDataRow}`).format.numberFormat = '0.00%';
tracker.getRange(`U${startRow + 1}:U${lastDataRow}`).format.numberFormat = '0.00%';
tracker.getRange(`J${startRow + 1}:K${lastDataRow}`).format.numberFormat = '#,##0';
tracker.getRange(`N${startRow + 1}:O${lastDataRow}`).format.numberFormat = '#,##0';
tracker.getRange(`S${startRow + 1}:T${lastDataRow}`).format.numberFormat = '#,##0';
tracker.getRange(`Q${startRow + 1}:Q${lastDataRow}`).format.numberFormat = '0.00';
tracker.getRange(`V${startRow + 1}:V${lastDataRow}`).format.numberFormat = '0.00';
tracker.getRange(`B${startRow + 1}:B${lastDataRow}`).conditionalFormats.add('containsText', {
  text: 'HOLD_FOR_RESCAN', format: { fill: '#FFF0C2', font: { bold: true, color: '#725100' } },
});
tracker.getRange(`B${startRow + 1}:B${lastDataRow}`).conditionalFormats.add('containsText', {
  text: 'EXCLUDED', format: { fill: '#E8EAE7', font: { color: '#59615A' } },
});

const widths = [24, 24, 46, 19, 21, 66, 66, 64, 76, 11, 17, 12, 36, 15, 17, 13, 19, 17, 16, 19, 14, 21, 70, 27, 17, 34, 34, 21, 55, 58, 38, 25, 42];
widths.forEach((width, index) => tracker.getRange(`${excelColumn(index + 1)}1:${excelColumn(index + 1)}${lastDataRow}`).format.columnWidth = width);
tracker.getRange(`A${startRow}:${lastColumn}${startRow}`).format.rowHeight = 34;
rawSheet.showGridLines = false;
rawSheet.freezePanes.freezeRows(1);
rawSheet.getRange(`A1:E${rawValues.length}`).format.font = { name: 'Arial', size: 10, color: '#27312B' };
rawSheet.getRange('A1:E1').format = {
  fill: '#234B38', font: { name: 'Arial', size: 10, bold: true, color: '#FFFFFF' },
  horizontalAlignment: 'center', verticalAlignment: 'center', wrapText: true,
};
const rawTable = rawSheet.tables.add(`A1:E${rawValues.length}`, true, 'BingPageExport');
rawTable.showFilterButton = true;
rawSheet.getRange(`A1:A${rawValues.length}`).format.columnWidth = 78;
rawSheet.getRange(`B1:E${rawValues.length}`).format.columnWidth = 20;

workbook.recalculate();
const preview = await workbook.render({ sheetName: 'SEO Tracker', range: 'A1:H13', scale: 1, format: 'png' });
const previewPath = path.join(os.tmpdir(), `sjmaths-seo-tracker-preview-${process.pid}.png`);
await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
const summaryInspect = await workbook.inspect({ kind: 'sheet', maxChars: 1200 });
const trackerInspect = await workbook.inspect({ kind: 'region', sheetId: tracker.name, range: 'A1:H12', maxChars: 2200 });
const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(outputPath);
const reopened = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
const savedInspect = await reopened.inspect({ kind: 'sheet', maxChars: 1200 });

console.log(JSON.stringify({
  output: outputPath,
  preview: previewPath,
  auditSnapshot: new Date((await fs.stat(reportPath)).mtimeMs).toISOString(),
  auditSummary: report.summary,
  trackerRows: trackerRows.length,
  inScope: trackerRows.filter(row => row[0] === 'IN_SCOPE').length,
  excludedClass9AfterChapter9: trackerRows.filter(row => row[0] !== 'IN_SCOPE').length,
  heldForRescan: trackerRows.filter(row => row[1] === 'HOLD_FOR_RESCAN').length,
  bingSourceRows: rawValues.length - 1,
  exactBingCanonicalMatches: trackerRows.filter(row => row[23] === 'exact canonical URL').length,
  summaryInspect: summaryInspect.ndjson,
  trackerInspect: trackerInspect.ndjson,
  savedInspect: savedInspect.ndjson,
}, null, 2));
