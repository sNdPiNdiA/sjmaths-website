import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { load } from 'cheerio';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const SOURCE_ROOT = path.join(ROOT, 'ssc-cgl', 'quantitative-aptitude');
const DATA_ROOT = path.join(ROOT, 'assets', 'data', 'quantitative-aptitude');
const SOURCE_EXAM_ID = 'ssc-cgl';
const GENERATOR_ID = 'scripts/export-quantitative-aptitude-data.mjs';
const EXPECTED_SECTIONS = ['theory', 'tricks', 'notes', 'practice', 'pyqs'];
const writeEnabled = process.argv.includes('--write');

function cleanText(value) {
  return String(value ?? '').replace(/\s+/g, ' ').trim();
}

function topicIdFromHref(href) {
  const pathname = String(href ?? '').split(/[?#]/, 1)[0].replace(/\\/g, '/').replace(/\/+$/, '');
  const topicId = path.posix.basename(pathname);
  return /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(topicId) ? topicId : null;
}

function sectionIdFromPanel(panelId) {
  return String(panelId ?? '').replace(/^tab-/, '');
}

function mapSyllabusItems(hubHtml) {
  const $ = load(hubHtml);
  const topics = new Map();

  $('main.subject-container .section-card').each((_, section) => {
    const area = cleanText($(section).find('.section-title').first().text());
    $(section).find('.topic-list .topic-item').each((__, item) => {
      const link = $(item).find('a.topic-text').first();
      const href = link.attr('href') || link.attr('data-unavailable-href');
      const id = topicIdFromHref(href);
      if (!id) return;

      const labelNode = link.clone();
      labelNode.find('.resource-status').remove();
      const syllabusItem = {
        label: cleanText(labelNode.text()),
        available: Boolean(link.attr('href')) && link.attr('aria-disabled') !== 'true',
      };
      const entry = topics.get(id) ?? { syllabusAreas: [], syllabusItems: [] };
      if (area && !entry.syllabusAreas.includes(area)) entry.syllabusAreas.push(area);
      entry.syllabusItems.push(syllabusItem);
      topics.set(id, entry);
    });
  });

  return topics;
}

function sectionLabel($, sectionId) {
  let label = '';
  $('.main-tabs-nav button.tab-btn').each((_, button) => {
    const onclick = $(button).attr('onclick') ?? '';
    if (onclick.includes(`tab-${sectionId}`)) label = cleanText($(button).text());
  });
  return label || sectionId;
}

function makeTopicData(topicId, topicHtml) {
  const $ = load(topicHtml);
  const title = cleanText($('.topic-header h1').first().text());
  const description = cleanText($('.topic-header p').first().text());
  const sourcePage = `ssc-cgl/quantitative-aptitude/${topicId}/index.html`;
  if (!title) throw new Error(`Missing topic H1 in ${sourcePage}`);

  const panels = new Map();
  $('.tab-panel').each((_, panel) => {
    const id = sectionIdFromPanel($(panel).attr('id'));
    if (!id || panels.has(id)) throw new Error(`Missing or duplicate tab panel id in ${sourcePage}`);
    panels.set(id, {
      id,
      label: sectionLabel($, id),
      format: 'html-fragment',
      reusePolicy: id === 'pyqs' ? 'exam-specific' : 'same-syllabus-review',
      ...(id === 'pyqs' ? { examId: SOURCE_EXAM_ID } : {}),
      html: ($(panel).html() ?? '').trim(),
    });
  });

  const found = [...panels.keys()];
  if (found.length !== EXPECTED_SECTIONS.length || EXPECTED_SECTIONS.some(id => !panels.has(id))) {
    throw new Error(`Expected the five standard sections in ${sourcePage}; found ${found.join(', ') || 'none'}`);
  }

  return {
    schemaVersion: 1,
    generatedBy: GENERATOR_ID,
    id: topicId,
    title,
    description,
    source: { examId: SOURCE_EXAM_ID, page: sourcePage },
    sections: EXPECTED_SECTIONS.map(id => panels.get(id)),
    reviewFlags: topicId === 'averages'
      ? [{
          sectionId: 'practice',
          reference: 'Q9',
          note: 'The source calculation gives 112, but the listed options and marked answer do not include 112.',
        }]
      : [],
  };
}

function serialize(data) {
  return `${JSON.stringify(data, null, 2)}\n`;
}

function assertManagedOrMissing(filePath) {
  if (!fs.existsSync(filePath)) return;
  let current;
  try {
    current = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    throw new Error(`Refusing to overwrite non-JSON output: ${path.relative(ROOT, filePath)}`);
  }
  if (current.generatedBy !== GENERATOR_ID) {
    throw new Error(`Refusing to overwrite a file not owned by this exporter: ${path.relative(ROOT, filePath)}`);
  }
}

function writeOrReport(filePath, contents, outputs) {
  outputs.push({ path: path.relative(ROOT, filePath).replace(/\\/g, '/'), bytes: Buffer.byteLength(contents) });
  if (!writeEnabled) return;
  fs.mkdirSync(path.dirname(filePath), { recursive: true });
  fs.writeFileSync(filePath, contents, 'utf8');
}

if (!fs.existsSync(SOURCE_ROOT)) throw new Error(`Missing source directory: ${SOURCE_ROOT}`);
const hubPath = path.join(SOURCE_ROOT, 'index.html');
if (!fs.existsSync(hubPath)) throw new Error(`Missing source syllabus page: ${hubPath}`);

const syllabusItems = mapSyllabusItems(fs.readFileSync(hubPath, 'utf8'));
const topicDirectories = fs.readdirSync(SOURCE_ROOT, { withFileTypes: true })
  .filter(entry => entry.isDirectory())
  .map(entry => entry.name)
  .sort((a, b) => a.localeCompare(b));
if (topicDirectories.length === 0) throw new Error('No SSC CGL topic pages were found.');

const outputs = [];
const topicEntries = [];
let extractedSectionCount = 0;

for (const topicId of topicDirectories) {
  const sourcePage = path.join(SOURCE_ROOT, topicId, 'index.html');
  if (!fs.existsSync(sourcePage)) throw new Error(`Missing topic page: ${sourcePage}`);

  const topicData = makeTopicData(topicId, fs.readFileSync(sourcePage, 'utf8'));
  const topicPath = path.join(DATA_ROOT, `${topicId}.json`);
  assertManagedOrMissing(topicPath);
  writeOrReport(topicPath, serialize(topicData), outputs);
  extractedSectionCount += topicData.sections.length;

  const syllabus = syllabusItems.get(topicId) ?? { syllabusAreas: [], syllabusItems: [] };
  topicEntries.push({
    id: topicId,
    title: topicData.title,
    data: `${topicId}.json`,
    syllabusAreas: syllabus.syllabusAreas,
    syllabusItems: syllabus.syllabusItems,
    sections: topicData.sections.map(section => section.id),
  });
}

const manifest = {
  schemaVersion: 1,
  generatedBy: GENERATOR_ID,
  id: 'quantitative-aptitude',
  title: 'Quantitative Aptitude',
  sourceExamId: SOURCE_EXAM_ID,
  sourceSyllabusPage: 'ssc-cgl/quantitative-aptitude/index.html',
  totalTopics: topicEntries.length,
  totalSections: extractedSectionCount,
  topics: topicEntries,
};
const manifestPath = path.join(DATA_ROOT, 'manifest.json');
assertManagedOrMissing(manifestPath);
writeOrReport(manifestPath, serialize(manifest), outputs);

console.log(JSON.stringify({
  mode: writeEnabled ? 'write' : 'dry-run',
  sourceTopics: topicDirectories.length,
  extractedSections: extractedSectionCount,
  outputFiles: outputs.length,
  totalBytes: outputs.reduce((total, output) => total + output.bytes, 0),
  outputs,
}, null, 2));
