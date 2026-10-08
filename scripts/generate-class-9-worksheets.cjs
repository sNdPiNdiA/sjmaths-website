// Opt-in worksheet authoring build. Earlier worksheet files are never rewritten.
const fs = require('node:fs');
const path = require('node:path');
const { worksheets } = require('./data/class-9-worksheets.cjs');
const { units } = require('./data/class-9-unit-tests.cjs');
const { ROOT, parse, applyEdits, editElement, setMetadata, escapeHtml } = require('./seo-html.cjs');
const domain = 'https://sjmaths.com';
const base = 'class-9-maths/worksheets/current-syllabus';
const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');
const changes = new Map();
const write = (file, content) => changes.set(file, content.replace(/\r\n/g, '\n').replace(/^[ \t]+$/gm, ''));
const levels = [['foundation', 'Foundation'], ['practice', 'Practice'], ['challenge', 'Challenge']];
function metadata(source, title, description, url) {
  return setMetadata(source, { title, description, canonical: domain + url, robots: 'index, follow, max-image-preview:large',
    'og:title': title, 'og:description': description, 'og:url': domain + url, 'og:type': 'article', 'og:image': domain + '/assets/icons/icon-512x512.png',
    'twitter:card': 'summary_large_image', 'twitter:title': title, 'twitter:description': description, 'twitter:image': domain + '/assets/icons/icon-512x512.png' });
}
const sharedDiagrams = new Map();
for (const unit of units) for (const paper of unit.tests) {
  const $ = parse(read(`class-9-maths/tests/unit-wise/${unit.folder}/test-${paper.paper}.html`));
  for (const q of paper.questions) {
    const svg = $('#paper-' + q.id + ' svg').first();
    if (svg.length) sharedDiagrams.set(q.id, $.html(svg));
  }
}
function diagram(q) {
  if (sharedDiagrams.has(q.id)) return sharedDiagrams.get(q.id);
  let label, body;
  if (q.diagram === 'bars') {
    label = 'Stacked counts and percentage bars for cycling and walking groups A and B';
    body = '<text x="15" y="25">Counts: cycling / walking</text><rect x="50" y="45" width="48" height="35" fill="#287052"/><rect x="98" y="45" width="72" height="35" fill="#d5bb83"/><rect x="50" y="95" width="64" height="35" fill="#287052"/><rect x="114" y="95" width="96" height="35" fill="#d5bb83"/><text x="20" y="68">A</text><text x="20" y="118">B</text><text x="220" y="68">12 / 18 = 30</text><text x="220" y="118">16 / 24 = 40</text><text x="15" y="170">Each percentage bar: 100%</text><rect x="50" y="190" width="112" height="35" fill="#287052"/><rect x="162" y="190" width="168" height="35" fill="#d5bb83"/><text x="53" y="251">40% cycling</text><text x="194" y="251">60% walking</text>';
  } else if (q.diagram === 'midpoints') {
    label = 'Eight by six rectangle and rhombus formed by joining its side midpoints';
    body = '<path d="M70 50H310V230H70ZM190 50L310 140L190 230L70 140Z"/><text x="170" y="35">8 cm</text><text x="320" y="145">6 cm</text><circle cx="190" cy="50" r="3"/><circle cx="310" cy="140" r="3"/><circle cx="190" cy="230" r="3"/><circle cx="70" cy="140" r="3"/>';
  }
  return body ? `<svg viewBox="0 0 400 290" role="img" aria-label="${escapeHtml(label)}"><title>${escapeHtml(label)}</title><g fill="none" stroke="currentColor" stroke-width="2">${body}</g></svg>` : '';
}
function sheetUrl(sheet) { return '/' + base + '/' + sheet.folder + '/'; }
function renderSheet(sheet, index) {
  const title = `Class 9 ${sheet.name} Worksheet | SJMaths`;
  const description = `Practice Class 9 ${sheet.name}: ${sheet.topicGroups.join(', ')}. Foundation, practice and challenge questions with step-wise answers.`;
  let number = 0;
  const questions = levels.map(([level, name]) => `<section class="sheet-section" id="${level}"><h2>${name}</h2>${sheet.questions.filter(q => q.level === level).map(q => {
    number++;
    return `<article class="worksheet-question" id="question-${q.id}" data-source="${q.source}"><p class="question-concept">${escapeHtml(q.concept)} · ${q.marks} practice mark${q.marks === 1 ? '' : 's'}</p><h3>Question ${number}</h3><p class="question-text">${escapeHtml(q.question)}</p>${q.options ? '<ol class="question-options">' + q.options.map(option => '<li>' + escapeHtml(option) + '</li>').join('') + '</ol>' : ''}<details class="worksheet-solution"><summary>Show step-wise answer</summary><p>${escapeHtml(q.finalAnswer)}</p><ol>${q.solutionSteps.map(step => '<li>' + escapeHtml(step) + '</li>').join('')}</ol>${diagram(q)}</details></article>`;
  }).join('\n')}</section>`).join('\n');
  const neighbours = `<nav class="sheet-neighbours" aria-label="Worksheet navigation">${index > 0 ? '<a href="' + sheetUrl(worksheets[index - 1]) + '">← Previous worksheet</a>' : '<a href="/class-9-maths/worksheets/">All worksheets</a>'}${index < worksheets.length - 1 ? '<a href="' + sheetUrl(worksheets[index + 1]) + '">Next worksheet →</a>' : '<a href="/class-9-maths/worksheets/">All worksheets →</a>'}</nav>`;
  const schema = { '@context': 'https://schema.org', '@type': 'LearningResource', name: title, description, url: domain + sheetUrl(sheet), educationalLevel: 'Class 9', learningResourceType: 'Worksheet', inLanguage: 'en', about: sheet.topicGroups, isPartOf: { '@type': 'CollectionPage', name: 'Class 9 Maths Worksheets', url: domain + '/class-9-maths/worksheets/' } };
  let source = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escapeHtml(title)}</title><link rel="icon" href="/favicon.png"><link rel="stylesheet" href="/assets/css/main.min.css?v=a3faaea0"><link rel="stylesheet" href="/assets/css/component.min.css?v=9dc5c71e"><link rel="stylesheet" href="/assets/css/class-9-worksheets.css?v=3"><script type="application/ld+json">${JSON.stringify(schema).replace(/</g, '\\u003c')}</script></head><body class="current-worksheet"><div id="header-container"></div><main><div class="sheet-paper"><nav class="sheet-breadcrumbs" aria-label="Breadcrumb"><a href="/class-9-maths/">Class 9 Maths</a><span aria-hidden="true">›</span><a href="/class-9-maths/worksheets/">Worksheets</a></nav><p class="sheet-kicker">${sheet.number ? 'Chapter ' + sheet.number : 'Supplement'} · ${escapeHtml(sheet.unit)}</p><h1>${escapeHtml(sheet.name)} Worksheet</h1><p class="sheet-meta">${sheet.questions.length} questions <span aria-hidden="true">·</span> ${sheet.topicGroups.map(escapeHtml).join(' <span aria-hidden="true">·</span> ')}</p><p class="sheet-instructions">Try each question before opening its solution.</p><p class="print-fields">Name: ________________________ &nbsp; Class: __________ &nbsp; Date: __________</p><div class="sheet-actions" aria-label="Worksheet tools"><button type="button" id="print-sheet">Print worksheet</button><label><input type="checkbox" id="print-sheet-answers"> Include answer key</label><button type="button" id="toggle-sheet-answers" aria-pressed="false">Show all answers</button><button type="button" id="share-sheet">Share worksheet</button><span class="share-status" id="sheet-share-status" role="status" aria-live="polite"></span></div><nav class="sheet-level-links" aria-label="Worksheet levels">${levels.map(([level, name]) => '<a href="#' + level + '">' + name + '</a>').join('')}</nav>${questions}${neighbours}</div></main><div id="footer-container"></div><script src="/assets/js/class-9-worksheets.js?v=1" defer></script><script src="/assets/js/global-header.min.js?v=893d8301" defer data-cfasync="false"></script><script src="/assets/js/global-footer.min.js?v=d800b1d8" defer data-cfasync="false"></script><script type="module" src="/assets/js/require-auth.min.js?v=3060658c"></script></body></html>`;
  return metadata(source, title, description, sheetUrl(sheet));
}
worksheets.forEach((sheet, index) => write(base + '/' + sheet.folder + '/index.html', renderSheet(sheet, index)));

const card = sheet => `<article class="worksheet-entry" data-chapter="${sheet.number || 'geometry'}"><p>${sheet.number ? 'Chapter ' + sheet.number : 'Geometry supplement'} · ${escapeHtml(sheet.unit)}</p><h2><a href="${sheetUrl(sheet)}">${escapeHtml(sheet.name)}</a></h2><p>${sheet.questions.length} questions · ${sheet.topicGroups.map(escapeHtml).join(' · ')}</p><div class="worksheet-links">${levels.map(([level, name]) => '<a href="' + sheetUrl(sheet) + '#' + level + '">' + name + '</a>').join('')}</div></article>`;
const oldLinks = [];
for (const folder of fs.readdirSync(path.join(ROOT, 'class-9-maths/worksheets'), { withFileTypes: true }).filter(entry => entry.isDirectory() && entry.name.startsWith('chapter-'))) {
  for (const file of fs.readdirSync(path.join(ROOT, 'class-9-maths/worksheets', folder.name)).filter(file => file.endsWith('.html'))) {
    const $ = parse(read('class-9-maths/worksheets/' + folder.name + '/' + file));
    const name = $('h1').text().replace(/^Chapter\s+\d+:\s*/, '');
    oldLinks.push('<li><a href="/class-9-maths/worksheets/' + folder.name + '/' + file + '">' + escapeHtml(name) + ' · ' + escapeHtml(file.replace('.html', '')) + '</a></li>');
  }
}
const directory = '<main class="chapters-container worksheet-directory" id="chapter-grid"><h2>Current Ganita Manjari chapter worksheets</h2><p>Choose a chapter. Each worksheet has foundation, practice and challenge questions.</p><div class="worksheet-directory-list">' + worksheets.filter(sheet => sheet.number).map(card).join('\n') + '</div><h2>Unit IV: Geometry foundations</h2><p>Extra practice for Euclid, lines and angles, and triangle congruence.</p>' + card(worksheets.at(-1)) + '<details id="earlier-worksheets"><summary>Earlier-edition worksheets — supplementary practice</summary><ul>' + oldLinks.join('\n') + '</ul></details></main>';
const hubFile = 'class-9-maths/worksheets/index.html';
let hub = read(hubFile);
let $ = parse(hub);
const edits = [editElement($('#chapter-grid')[0], directory)];
$('script[type="module"]:not([src])').each((_, el) => {
  const text = $(el).text();
  if (text.includes('const chapters = [')) {
    const remaining = text.slice(text.indexOf('// Back to Top Logic'));
    if (!remaining.startsWith('// Back to Top Logic')) throw new Error('Worksheet hub module structure changed');
    edits.push(editElement(el, '<script type="module">' + remaining + '</script>'));
  }
});
edits.push(editElement($('.curriculum-notice')[0], '<aside class="curriculum-notice" data-curriculum="mixed" aria-label="Worksheet syllabus"><p><strong>Current syllabus:</strong> 14 chapters plus Geometry Foundations. <a href="#earlier-worksheets">Earlier worksheets</a></p></aside>'));
hub = applyEdits(hub, edits);
hub = hub.replace('/assets/css/class-9-worksheets.css?v=1', '/assets/css/class-9-worksheets.css?v=3');
if (!hub.includes('href="/assets/css/class-9-worksheets.css?v=3"')) hub = hub.replace('</head>', '<link rel="stylesheet" href="/assets/css/class-9-worksheets.css?v=3">\n</head>');
hub = hub.replace('Download chapter-wise printable worksheets for practice and revision.', 'Practice current Ganita Manjari topics with printable chapter-wise questions and step-wise solutions.');
hub = hub.replace('This page provides comprehensive <strong>Class 9 Maths Worksheets - SJMaths</strong>. Download free printable worksheets for Class 9 Mathematics. Chapter-wise practice sheets for Number Systems, Polynomials, Geometry, and more.', 'Current worksheets cover coordinates, numbers, linear models, identities, circles, mensuration, probability, sequences, logic, data, algorithms, quadrilaterals and paired equations.');
const hubTitle = 'Class 9 Ganita Manjari Worksheets: Current Syllabus | SJMaths';
const hubDescription = 'Printable Class 9 Ganita Manjari worksheets for all 14 chapters, plus geometry foundations: foundation, practice and challenge questions with step-wise answers.';
hub = metadata(hub, hubTitle, hubDescription, '/class-9-maths/worksheets/');
$ = parse(hub);
const schemaEdits = [];
$('script[type="application/ld+json"]').each((_, el) => {
  const schema = JSON.parse($(el).text());
  if (schema['@type'] === 'LearningResource') {
    schema.name = schema.headline = hubTitle; schema.description = hubDescription;
    schemaEdits.push(editElement(el, '<script type="application/ld+json">' + JSON.stringify(schema, null, 2) + '</script>'));
  }
});
hub = applyEdits(hub, schemaEdits);
write(hubFile, hub);

let dashboard = read('class-9-maths/index.html');
$ = parse(dashboard);
const dashboardEdits = [];
for (const sheet of worksheets.filter(sheet => sheet.number)) {
  const chapterCard = $('#chapters-grid .ch-card-item').eq(sheet.number - 1);
  if (chapterCard.find('.ch-card-title').text().replace(/\s+/g, ' ').trim() !== sheet.name) throw new Error('Chapter order/name mismatch for ' + sheet.number);
  const tabs = chapterCard.find('.ch-quick-tabs-grid');
  const old = tabs.find('.sheet-tab');
  const link = '<a href="' + sheetUrl(sheet) + '" class="quick-tab-pill sheet-tab"><i class="fas fa-file-alt"></i><span>Sheets</span></a>';
  if (old.length) dashboardEdits.push(editElement(old[0], link));
  else {
    const loc = tabs[0]?.sourceCodeLocation;
    if (!loc) throw new Error('Missing chapter tabs for ' + sheet.number);
    dashboardEdits.push({ start: loc.startTag.endOffset, end: loc.startTag.endOffset, text: '\n                        ' + link });
  }
}
dashboard = applyEdits(dashboard, dashboardEdits).replace('Earlier-edition Worksheets</a>', 'Current-syllabus Worksheets</a>');
const oldCopy = 'Study current Ganita Manjari chapter notes, worked examples and NCERT solutions. Chapters 9–14 also include mini tests. Earlier-edition worksheets and papers are labelled separately.';
const newCopy = 'Study current Ganita Manjari chapter notes, worked examples and NCERT solutions, with chapter-wise worksheets and six-unit practice tests. Chapters 9–14 also include mini tests. Earlier-edition practice is labelled separately.';
dashboard = dashboard.replaceAll(oldCopy, newCopy);
write('class-9-maths/index.html', dashboard);
const mapping = { source: 'User-provided six-unit syllabus, 2026-09-30', worksheets: worksheets.map(sheet => ({ chapter: sheet.number, name: sheet.name, url: sheetUrl(sheet), questions: sheet.questions.map(q => ({ id: q.id, level: q.level, concept: q.concept, source: q.source })) })), units: units.map(unit => ({ number: unit.number, topics: Object.entries(unit.topics).map(([id, label]) => ({ id, label, worksheetQuestions: worksheets.flatMap(sheet => sheet.questions.filter(q => q.id.startsWith('u' + unit.number + 't') && q.topics.includes(id)).map(q => ({ id: q.id, url: sheetUrl(sheet) + '#question-' + q.id }))) })) })) };
if (mapping.units.some(unit => unit.topics.some(topic => !topic.worksheetQuestions.length))) throw new Error('A supplied topic has no worksheet question');
write(base + '/syllabus-coverage.json', JSON.stringify(mapping, null, 2) + '\n');
if (process.argv.includes('--write')) for (const [file, content] of changes) {
  const absolute = path.join(ROOT, file);
  fs.mkdirSync(path.dirname(absolute), { recursive: true });
  if (!fs.existsSync(absolute) || read(file).replace(/\r\n/g, '\n') !== content) fs.writeFileSync(absolute, content, 'utf8');
}
console.log(JSON.stringify({ mode: process.argv.includes('--write') ? 'write' : 'dry-run', chapters: 14, supplements: 1, questionPlacements: worksheets.reduce((n, sheet) => n + sheet.questions.length, 0), uniqueQuestions: new Set(worksheets.flatMap(sheet => sheet.questions.map(q => q.id))).size, worksheetOnlyQuestions: worksheets.reduce((n, sheet) => n + sheet.additions.length, 0), generatedFiles: changes.size }, null, 2));
