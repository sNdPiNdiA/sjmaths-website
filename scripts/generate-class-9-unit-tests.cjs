// Opt-in authoring build. The original questions are snapshotted before replacement.
const fs = require('node:fs');
const path = require('node:path');
const { units } = require('./data/class-9-unit-tests.cjs');
const { ROOT, parse, applyEdits, editElement, setMetadata, escapeHtml } = require('./seo-html.cjs');
const base = 'class-9-maths/tests/unit-wise';
const archive = 'class-9-maths/previous-syllabus/unit-tests';
const domain = 'https://sjmaths.com';
const read = file => fs.readFileSync(path.join(ROOT, file), 'utf8');
const changes = new Map();
const write = (file, content) => changes.set(file, content.replace(/\r\n/g, '\n'));
const json = value => JSON.stringify(value, null, 2).replace(/</g, '\\u003c');
const auth = '<script type="module" src="/assets/js/require-auth.min.js?v=3060658c"></script>';

function metadata(source, title, description, url, robots = 'index, follow, max-image-preview:large') {
  return setMetadata(source, { title, description, canonical: domain + url, robots,
    'og:title': title, 'og:description': description, 'og:type': 'article', 'og:url': domain + url,
    'og:image': domain + '/assets/icons/icon-512x512.png', 'twitter:card': 'summary_large_image',
    'twitter:title': title, 'twitter:description': description, 'twitter:image': domain + '/assets/icons/icon-512x512.png' });
}
function diagram(question) {
  let body = '';
  let label = '';
  if (question.id === 'u2t2q7') {
    label = 'Graph of y equals x plus one and y equals minus x plus five, meeting at two comma three';
    body = '<path d="M50 260V35M40 250H285"/><path d="M50 215L230 75M50 75L230 215"/><circle cx="140" cy="145" r="4"/><text x="148" y="141">(2,3)</text><text x="240" y="65">y = x + 1</text><text x="232" y="223">y = −x + 5</text><text x="275" y="270">x</text><text x="30" y="35">y</text><text x="36" y="270">0</text>';
  } else if (question.id === 'u3t1q5') {
    label = 'Eight by six classroom floor plan with its centre and ten-unit diagonal';
    body = '<path d="M50 230H290V50H50ZM50 230L290 50"/><circle cx="170" cy="140" r="4"/><text x="45" y="252">(0,0)</text><text x="253" y="40">(8,6)</text><text x="175" y="140">(4,3)</text><text x="130" y="273">8 m</text><text x="296" y="150">6 m</text>';
  } else if (question.id === 'u4t1q13') {
    label = 'Circle of radius five, half chord four and perpendicular distance three';
    body = '<circle cx="180" cy="140" r="100"/><path d="M100 200H260M180 140V200M180 140L260 200M180 140L100 200"/><path d="M180 190H190V200"/><text x="180" y="132">O</text><text x="176" y="220">M</text><text x="85" y="218">A</text><text x="261" y="218">B</text><text x="188" y="175">3</text><text x="215" y="188">5</text><text x="215" y="222">4</text>';
  } else if (question.id === 'u4t2q11') {
    label = 'Quadrilateral with side midpoints forming the Varignon parallelogram';
    body = '<path d="M60 220L110 40L320 75L290 240ZM85 130L215 57.5L305 157.5L175 230Z"/><path d="M60 220L320 75M110 40L290 240" stroke-dasharray="5 5"/><text x="43" y="235">A</text><text x="97" y="28">B</text><text x="325" y="73">C</text><text x="290" y="260">D</text><text x="65" y="133">P</text><text x="215" y="47">Q</text><text x="315" y="160">R</text><text x="175" y="250">S</text>';
  } else if (question.id === 'u5t1q9') {
    label = 'Right square pyramid with vertical height four, face slant height five and half-base length three';
    body = '<path d="M180 35L60 220L280 235ZM180 35L135 180L330 195L280 235M60 220L135 180M180 35V209L280 235"/><text x="190" y="120">h = 4</text><text x="244" y="138">slant = 5</text><text x="199" y="245">half side = 3</text><text x="165" y="22">apex</text>';
  } else if (question.id === 'u6t1q8') {
    label = 'Probability tree for two independent fair coin tosses';
    body = '<path d="M35 140L140 75L250 45M140 75L250 105M35 140L140 205L250 175M140 205L250 245"/><text x="90" y="82">H: ½</text><text x="85" y="205">T: ½</text><text x="265" y="50">HH: ¼</text><text x="265" y="110">HT: ¼</text><text x="265" y="180">TH: ¼</text><text x="265" y="250">TT: ¼</text>';
  }
  if (!body) return '';
  return `<svg viewBox="0 0 400 290" role="img" aria-label="${escapeHtml(label)}"><title>${escapeHtml(label)}</title><g fill="none" stroke="currentColor" stroke-width="2">${body}</g></svg>`;
}
function paperMarkup(paper) {
  return `<details class="source-paper" id="source-paper" open><summary>Full question paper and step-wise model answers</summary><p>Practice marks are not official examination weightage. Written answers require self- or teacher assessment.</p>${paper.questions.map((q, i) => `
    <article class="source-question" id="paper-${q.id}" data-topics="${q.topics.join(' ')}"><h3>Question ${i + 1} · ${q.marks} mark${q.marks === 1 ? '' : 's'}</h3><p>${escapeHtml(q.question)}</p>${q.options ? '<ol type="a">' + q.options.map(option => '<li>' + escapeHtml(option) + '</li>').join('') + '</ol>' : ''}<details><summary>Model answer and reasoning</summary><p>${escapeHtml(q.finalAnswer)}</p><ol>${q.solutionSteps.map(step => '<li>' + escapeHtml(step) + '</li>').join('')}</ol>${diagram(q)}</details></article>`).join('')}</details>`;
}
function renderTest(template, unit, paper) {
  const url = `/${base}/${unit.folder}/test-${paper.paper}`;
  let source = metadata(template, `Class 9 ${unit.name} Unit Test ${paper.paper} | SJMaths`, `${paper.subHeading} for Class 9 ${unit.name}: ${unit.summary} Step-wise answers and syllabus-aligned practice.`, url);
  const $ = parse(source);
  const edits = [];
  $('script[type="application/ld+json"], .ai-summary, h1.seo-page-title, .curriculum-notice, link[href="/class-9-maths/curriculum.css"]').each((_, el) => edits.push(editElement(el, '')));
  $('script:not([src])').each((_, el) => {
    if ($(el).text().includes("fetch('test")) edits.push(editElement(el, `<script type="application/json" id="unit-test-data">${json(paper)}</script><script src="/assets/js/class-9-unit-tests.js?v=1" defer></script>`));
  });
  source = applyEdits(source, edits);
  const total = paper.questions.reduce((sum, q) => sum + q.marks, 0);
  source = source.replace('SJMaths · Earlier Paper', 'SJMaths Test Series').replace('<body>', '<body class="current-unit-test">')
    .replace('</head>', '<link rel="stylesheet" href="/assets/css/class-9-unit-tests.css?v=1">\n<script type="application/ld+json">' + json({ '@context': 'https://schema.org', '@type': 'LearningResource', name: paper.heading, url: domain + url, description: unit.summary, educationalLevel: 'Class 9', learningResourceType: 'Practice test', inLanguage: 'en', isPartOf: { '@type': 'CollectionPage', name: 'Class 9 Unit-wise Tests', url: domain + '/' + base + '/' } }) + '</script>\n</head>')
    .replace('<main class="question-panel">', `<main class="question-panel"><h1 class="unit-test-heading">${escapeHtml(paper.heading)}</h1><p class="unit-paper-meta">${escapeHtml(paper.subHeading)} · ${paper.questions.length} questions · ${total} practice marks · ${paper.timeLimit} minutes.<br>MCQs are scored automatically; written answers use step-wise self/teacher review.</p>`)
    .replace('</main>', paperMarkup(paper) + '</main>')
    .replace('<div class="result-overlay" id="resultModal">', '<div class="result-overlay" id="resultModal" role="dialog" aria-modal="true" aria-labelledby="result-heading">')
    .replace(/<a href="(?:\.\.\/){1,2}" style="display:block; margin-top:1rem; color:#666; text-decoration:none;">Back to/, `<a href="/${base}/${unit.folder}/" style="display:block; margin-top:1rem; color:#666; text-decoration:none;">Back to`);
  if (!source.includes('id="unit-test-data"')) throw new Error('Missing original test data loader in ' + url);
  return source.replace(/^[ \t]+$/gm, '');
}
function listing(title, description, url, body) {
  let source = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escapeHtml(title)}</title><link rel="icon" href="/favicon.png"><link rel="stylesheet" href="/assets/css/main.min.css?v=a3faaea0"><link rel="stylesheet" href="/class-9-maths/curriculum.css"><style>
    .unit-assessments { max-width: 66rem; margin: 2rem auto 4rem; padding: 0 1.2rem; line-height: 1.7; color: #243d31; }
    .unit-assessments h1 { font-size: clamp(1.7rem,5vw,2.5rem); line-height: 1.25; }
    .unit-assessments a { color: #176447; text-decoration: underline; text-underline-offset: .2em; }
    .unit-assessments a:focus-visible { outline: 3px solid #b77b2a; outline-offset: 3px; }
    .syllabus-unit { padding-block: 1.3rem; border-bottom: 1px solid #d5dfd4; }
    .unit-assessments .paper-links { display:flex; flex-wrap:wrap; gap:1rem; }
    .paper-links a { padding-block: .5rem; }
    .period-note { color:#66776c; font-size:.95rem; }
    body.dark-mode .unit-assessments { color:#eaf0e7; } body.dark-mode .unit-assessments a { color:#a2dcba; }
    </style></head><body><div id="header-container"></div><main class="unit-assessments"><p><a href="/class-9-maths/">Class 9 Maths</a> › <a href="/${base}/">Unit-wise tests</a></p><h1>${escapeHtml(title.replace(' | SJMaths', ''))}</h1><p>${escapeHtml(description)}</p>${body}</main><div id="footer-container"></div><script src="/assets/js/global-header.min.js?v=893d8301" defer data-cfasync="false"></script><script src="/assets/js/global-footer.min.js?v=d800b1d8" defer data-cfasync="false"></script>${auth}</body></html>`;
  source = metadata(source, title, description, url);
  return source;
}
function questionCoverage(unit) {
  const questions = unit.tests.flatMap(p => p.questions);
  return Object.entries(unit.topics).map(([id, label]) => ({ id, label, questions: questions.filter(q => q.topics.includes(id)).map(q => q.id) }));
}
const coverage = { source: 'User-provided syllabus, 2026-09-30', units: [] };
for (const unit of units) {
  const topics = questionCoverage(unit);
  if (topics.some(t => !t.questions.length)) throw new Error('Unassessed topic in unit ' + unit.number);
  coverage.units.push({ number: unit.number, name: unit.name, periods: unit.periods, topics });
  for (const paper of unit.tests) {
    const htmlFile = `${base}/${unit.folder}/test-${paper.paper}.html`;
    const dataName = paper.paper === 1 ? 'test.json' : 'test-2.json';
    const dataFile = `${base}/${unit.folder}/${dataName}`;
    const savedHtml = `${archive}/${unit.folder}/test-${paper.paper}.html`;
    const savedData = `${archive}/${unit.folder}/${dataName}`;
    let original = read(fs.existsSync(path.join(ROOT, savedHtml)) ? savedHtml : htmlFile);
    if (!fs.existsSync(path.join(ROOT, savedHtml))) {
      let archived = metadata(original, `Previous-syllabus ${unit.name} Test ${paper.paper} | SJMaths`, `Earlier-edition Class 9 ${unit.name} Test ${paper.paper}, preserved for supplementary practice. Current unit papers use the supplied six-unit syllabus.`, `/${archive}/${unit.folder}/test-${paper.paper}`);
      archived = archived.replace('</head>', '<link rel="stylesheet" href="/class-9-maths/curriculum.css">\n</head>').replace('<body>', '<body>\n<aside class="curriculum-notice"><p><strong>Previous-syllabus paper.</strong> Original questions and solutions are preserved. <a href="/' + base + '/' + unit.folder + '/">Open current unit tests</a>.</p></aside>');
      archived = archived.replace('SJMaths Test Series', 'SJMaths · Earlier Paper');
      write(savedHtml, archived);
      write(savedData, read(dataFile));
    } else {
      write(savedHtml, metadata(original, `Previous-syllabus ${unit.name} Test ${paper.paper} | SJMaths`, `Earlier-edition Class 9 ${unit.name} Test ${paper.paper}, preserved for supplementary practice. Current unit papers use the supplied six-unit syllabus.`, `/${archive}/${unit.folder}/test-${paper.paper}`));
    }
    write(htmlFile, renderTest(original, unit, paper));
    write(dataFile, json(paper) + '\n');
  }
  const detail = '<p class="period-note">' + unit.periods + ' teaching periods in the supplied syllabus; this is not examination mark weightage.</p><section class="syllabus-unit"><h2>Scope</h2><ul>' + Object.values(unit.topics).map(label => '<li>' + escapeHtml(label) + '</li>').join('') + '</ul></section><section class="syllabus-unit"><h2>Choose a paper</h2><div class="paper-links">' + unit.tests.map(paper => '<a href="test-' + paper.paper + '.html">Test ' + paper.paper + ' · ' + paper.questions.length + ' questions · ' + paper.timeLimit + ' min</a>').join('') + '</div><p>Written proofs, constructions and case responses require self- or teacher assessment; MCQs are automatically scored.</p></section><p><a href="/' + archive + '/' + unit.folder + '/">Earlier-edition papers</a></p>';
  write(`${base}/${unit.folder}/index.html`, listing(`Class 9 ${unit.name} Unit Tests | SJMaths`, unit.summary, `/${base}/${unit.folder}/`, detail));
  write(`${archive}/${unit.folder}/index.html`, listing(`Previous-syllabus ${unit.name} Tests | SJMaths`, `Earlier-edition Class 9 ${unit.name} questions and solutions are retained for supplementary practice. Current unit papers follow the supplied syllabus.`, `/${archive}/${unit.folder}/`, '<div class="paper-links"><a href="test-1.html">Previous Test 1</a><a href="test-2.html">Previous Test 2</a><a href="/' + base + '/' + unit.folder + '/">Current unit tests</a></div>'));
}
write(`${base}/syllabus-coverage.json`, json(coverage) + '\n');
const cards = units.map(unit => `<section class="syllabus-unit"><h2>Unit ${unit.roman}: ${escapeHtml(unit.name)}</h2><p class="period-note">${unit.periods} teaching periods</p><p>${escapeHtml(unit.summary)}</p><div class="paper-links"><a href="${unit.folder}/">Unit scope</a><a href="${unit.folder}/test-1.html">Test 1: Concepts and applications</a><a href="${unit.folder}/test-2.html">Test 2: Reasoning and modelling</a></div></section>`).join('\n');
let directory = listing('Class 9 Unit-wise Tests: Current Syllabus | SJMaths', 'Twelve practice papers across the six units in the supplied syllabus, with multiple-choice, written, proof, construction, graphing and contextual questions and step-wise model answers.', `/${base}/`, '<p class="period-note">The counts below are teaching periods from the supplied syllabus, not official examination marks. Practice-paper marks are specified on each test.</p>' + cards + '<p><a href="/' + archive + '/">Open previous-syllabus unit papers</a></p>');
directory = directory.replace('</head>', '<script type="application/ld+json">' + json({ '@context': 'https://schema.org', '@type': 'ItemList', itemListElement: units.map((unit, i) => ({ '@type': 'ListItem', position: i + 1, name: unit.name, url: domain + '/' + base + '/' + unit.folder + '/' })) }) + '</script></head>');
write(`${base}/index.html`, directory);
write(`${archive}/index.html`, listing('Previous-syllabus Class 9 Unit Tests | SJMaths', 'All twelve earlier unit papers remain available with their original questions, answers and timings. Current papers are linked separately.', `/${archive}/`, units.map(unit => '<section class="syllabus-unit"><h2>' + escapeHtml(unit.name) + '</h2><div class="paper-links"><a href="' + unit.folder + '/test-1.html">Previous Test 1</a><a href="' + unit.folder + '/test-2.html">Previous Test 2</a></div></section>').join('')));

if (process.argv.includes('--write')) {
  for (const [file, content] of changes) {
    const absolute = path.join(ROOT, file);
    fs.mkdirSync(path.dirname(absolute), { recursive: true });
    if (!fs.existsSync(absolute) || read(file).replace(/\r\n/g, '\n') !== content) fs.writeFileSync(absolute, content, 'utf8');
  }
}
console.log(JSON.stringify({ mode: process.argv.includes('--write') ? 'write' : 'dry-run', units: units.length, papers: units.reduce((sum, u) => sum + u.tests.length, 0), questions: units.reduce((sum, u) => sum + u.tests.reduce((count, p) => count + p.questions.length, 0), 0), assessedTopics: coverage.units.reduce((sum, u) => sum + u.topics.length, 0), generatedFiles: changes.size }, null, 2));
