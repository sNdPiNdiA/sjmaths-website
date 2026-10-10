import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'scripts/data/ib-dp-aa-sl-guides.json'), 'utf8'));
const lessonData = JSON.parse(fs.readFileSync(path.join(ROOT, 'scripts/data/ib-dp-aa-sl-lessons.json'), 'utf8'));
const baseUrl = 'https://sjmaths.com/ib/dp-mathematics/';
const basePath = '/ib/dp-mathematics/';
const lessonsByTopic = new Map(data.topics.map((topic) => [
  topic.slug,
  lessonData.lessons.filter((lesson) => lesson.parentSlug === topic.slug),
]));

function esc(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

function schemaScript(page, url, breadcrumbs, articleSection) {
  const schema = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'BreadcrumbList',
        '@id': url + '#breadcrumb',
        itemListElement: breadcrumbs.map((item, index) => ({
          '@type': 'ListItem',
          position: index + 1,
          name: item.name,
          item: item.url,
        })),
      },
      {
        '@type': 'Article',
        '@id': url + '#article',
        headline: page.title,
        description: page.description,
        url,
        dateModified: data.updated,
        inLanguage: 'en',
        articleSection,
        author: { '@type': 'Person', name: 'Sandeep Jaiswal', url: 'https://sjmaths.com/pages/about.html' },
        publisher: {
          '@type': 'Organization',
          name: 'SJMaths',
          url: 'https://sjmaths.com/',
          logo: { '@type': 'ImageObject', url: 'https://sjmaths.com/assets/icons/icon-512x512.png' },
        },
      },
    ],
  };
  return '<script type="application/ld+json">' + JSON.stringify(schema).replaceAll('<', '\\u003c') + '</script>';
}

function pageHead(page, url, breadcrumbs, section) {
  const seoTitle = page.seoTitle || page.title + ' | SJMaths';
  return [
    '<!doctype html>',
    '<html lang="en">',
    '<head>',
    '  <meta charset="UTF-8">',
    '  <meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '  <title>' + esc(seoTitle) + '</title>',
    '  <meta name="description" content="' + esc(page.description) + '">',
    '  <meta name="keywords" content="' + esc(page.keywords.join(', ')) + '">',
    '  <meta name="author" content="SJMaths - Sandeep Jaiswal (PGT Maths)">',
    '  <meta name="robots" content="index, follow, max-image-preview:large">',
    '  <link rel="canonical" href="' + esc(url) + '">',
    '  <meta property="og:type" content="article">',
    '  <meta property="og:title" content="' + esc(seoTitle) + '">',
    '  <meta property="og:description" content="' + esc(page.description) + '">',
    '  <meta property="og:url" content="' + esc(url) + '">',
    '  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">',
    '  <meta property="og:site_name" content="SJMaths">',
    '  <meta name="twitter:card" content="summary_large_image">',
    '  <meta name="twitter:title" content="' + esc(seoTitle) + '">',
    '  <meta name="twitter:description" content="' + esc(page.description) + '">',
    '  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">',
    '  <link rel="icon" type="image/png" href="/favicon.png">',
    '  <link rel="preconnect" href="https://fonts.googleapis.com">',
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
    '  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'">',
    '  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"></noscript>',
    '  <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473">',
    '  <link rel="stylesheet" href="/assets/css/main.min.css?v=e4c665a0">',
    '  <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">',
    '  <link rel="stylesheet" href="/assets/css/component.min.css?v=85dbb37c">',
    '  <link rel="stylesheet" href="/assets/css/ib-page.min.css?v=ac6d658f">',
    '  <link rel="stylesheet" href="/assets/css/ib-dp-aa-sl-guides.css">',
    '  ' + schemaScript(page, url, breadcrumbs, section),
    '</head>',
  ].join('\n');
}

function header(currentLabel) {
  return [
    '<a class="skip-link study-skip" href="#main-content">Skip to main content</a>',
    '<header class="ib-nav-header">',
    '  <div class="ib-nav-container">',
    '    <a href="/" class="ib-nav-brand"><span aria-hidden="true">∑</span> SJMaths</a>',
    '    <nav class="ib-nav-links" aria-label="Main navigation">',
    '      <a href="/ib/">IB Hub</a>',
    '      <a href="/ib/myp-mathematics/">MYP Math</a>',
    '      <a href="/ib/dp-mathematics/" class="active">DP Math</a>',
    '      <button id="theme-toggle" class="ib-theme-btn" type="button" aria-label="Toggle Dark Mode"><i class="fa-solid fa-moon" aria-hidden="true"></i></button>',
    '    </nav>',
    '  </div>',
    '</header>',
  ].join('\n');
}

function breadcrumbMarkup(items) {
  return '<nav class="breadcrumb-nav" aria-label="Breadcrumb">' + items.map((item, index) => {
    const current = index === items.length - 1;
    return (index ? '<span class="breadcrumb-separator" aria-hidden="true">›</span>' : '') +
      (current ? '<span aria-current="page">' + esc(item.name) + '</span>' : '<a href="' + esc(item.url) + '">' + esc(item.name) + '</a>');
  }).join('') + '</nav>';
}

function renderCoverage(items) {
  return '<ol class="coverage-list">' + items.map((item) => {
    const match = item.match(/^([0-9]+\.[0-9]+)\s+(.+)$/);
    return '<li><span class="coverage-code">' + esc(match ? match[1] : '') + '</span><span>' + esc(match ? match[2] : item) + '</span></li>';
  }).join('') + '</ol>';
}

function renderSections(sections) {
  return sections.map((section) => '<section class="study-section">' +
    '<h3>' + esc(section.title) + '</h3>' +
    '<ul class="study-points">' + section.points.map((point) => '<li>' + esc(point) + '</li>').join('') + '</ul>' +
    '</section>').join('');
}

function renderExamples(examples) {
  return examples.map((example, index) => '<article class="worked-example">' +
    '<p class="example-label">Worked example ' + (index + 1) + '</p>' +
    '<h3>' + esc(example.title) + '</h3>' +
    '<p class="question-text"><strong>Question.</strong> ' + esc(example.question) + '</p>' +
    '<ol class="solution-steps">' + example.steps.map((step) => '<li>' + esc(step) + '</li>').join('') + '</ol>' +
    '<p class="answer-line"><strong>Answer:</strong> ' + esc(example.answer) + '</p>' +
    '</article>').join('');
}

function renderPractice(items) {
  return '<ol class="practice-list">' + items.map((item) => '<li>' +
    '<p>' + esc(item.question) + '</p>' +
    '<details><summary>Show worked answer</summary><p>' + esc(item.solution) + '</p></details>' +
    '</li>').join('') + '</ol>';
}

function renderGuideToc() {
  return '<nav class="study-toc" aria-label="On this page"><p class="toc-title">On this page</p><ul>' +
    '<li><a href="#syllabus">Syllabus coverage</a></li>' +
    '<li><a href="#topic-lessons">Topic lessons</a></li>' +
    '<li><a href="#key-ideas">Key ideas</a></li>' +
    '<li><a href="#worked-examples">Worked examples</a></li>' +
    '<li><a href="#practice">Practice</a></li>' +
    '<li><a href="#revision">Revision checklist</a></li>' +
    '</ul></nav>';
}

function renderLessonCards(topic) {
  const lessons = lessonsByTopic.get(topic.slug) || [];
  const topicPath = basePath + 'analysis-and-approaches-sl/' + topic.slug + '/';
  return '<div class="lesson-grid">' + lessons.map((lesson, index) =>
    '<a class="lesson-card" href="' + esc(topicPath + lesson.slug + '/') + '">' +
      '<span class="lesson-card-code">' + esc(lesson.code) + '</span>' +
      '<span class="lesson-card-title">' + esc(lesson.title) + '</span>' +
      '<span class="lesson-card-desc">' + esc(lesson.intro) + '</span>' +
      '<span class="lesson-card-link">Open lesson <span aria-hidden="true">→</span></span>' +
    '</a>'
  ).join('') + '</div>';
}

function renderLessonToc() {
  return '<nav class="study-toc" aria-label="On this page"><p class="toc-title">On this page</p><ul>' +
    '<li><a href="#syllabus">Syllabus coverage</a></li>' +
    '<li><a href="#key-ideas">Key ideas</a></li>' +
    '<li><a href="#worked-example">Worked example</a></li>' +
    '<li><a href="#practice">Practice</a></li>' +
    '<li><a href="#common-mistakes">Common mistakes</a></li>' +
    '<li><a href="#more-lessons">More lessons</a></li>' +
    '</ul></nav>';
}

function renderLesson(lesson, index) {
  const topic = data.topics.find((item) => item.slug === lesson.parentSlug);
  const topicPath = basePath + 'analysis-and-approaches-sl/' + topic.slug + '/';
  const lessonPath = topicPath + lesson.slug + '/';
  const url = baseUrl + 'analysis-and-approaches-sl/' + topic.slug + '/' + lesson.slug + '/';
  const siblings = lessonsByTopic.get(topic.slug);
  const previous = siblings[index - 1];
  const next = siblings[index + 1];
  const crumbs = [
    { name: 'Home', url: 'https://sjmaths.com/' },
    { name: 'IB Mathematics', url: 'https://sjmaths.com/ib/' },
    { name: 'IB DP Mathematics', url: baseUrl },
    { name: 'AA SL', url: baseUrl + 'analysis-and-approaches-sl/' },
    { name: topic.name, url: 'https://sjmaths.com' + topicPath },
    { name: lesson.title, url },
  ];
  const page = {
    ...lesson,
    title: lesson.title,
    seoTitle: (lesson.seoTitle || lesson.title) + ' | IB Math AA SL | SJMaths',
  };
  const related = [
    '<a href="' + esc(topicPath) + '"><span>Topic overview</span><strong>' + esc(topic.name) + ' for IB Math AA SL</strong></a>',
  ];
  if (previous) related.push('<a href="' + esc(topicPath + previous.slug + '/') + '"><span>Previous lesson</span><strong>' + esc(previous.title) + '</strong></a>');
  if (next) related.push('<a href="' + esc(topicPath + next.slug + '/') + '"><span>Next lesson</span><strong>' + esc(next.title) + '</strong></a>');
  const moreLessons = siblings.map((item) =>
    '<a class="lesson-card" href="' + esc(topicPath + item.slug + '/') + '"' + (item.slug === lesson.slug ? ' aria-current="page"' : '') + '>' +
      '<span class="lesson-card-code">' + esc(item.code) + '</span>' +
      '<span class="lesson-card-title">' + esc(item.title) + '</span>' +
      '<span class="lesson-card-desc">' + esc(item.intro) + '</span>' +
    '</a>'
  ).join('');
  const body = [
    '<body>',
    header('AA SL'),
    '<section class="ib-hero">',
    '  <div class="ib-hero-container">',
    '    ' + breadcrumbMarkup(crumbs),
    '    <p class="guide-kicker">IB Diploma Programme · Mathematics: Analysis and Approaches · Standard Level</p>',
    '    <h1 class="ib-hero-title">' + esc(page.title) + '</h1>',
    '    <p class="ib-hero-desc">' + esc(lesson.intro) + '</p>',
    '    <div class="meta-pills"><span class="meta-pill">' + esc(lesson.code) + '</span><span class="meta-pill">' + esc(topic.name) + '</span><span class="meta-pill">AA SL · current syllabus</span></div>',
    '  </div>',
    '</section>',
    '<main id="main-content" class="main-content study-main">',
    '  <div class="study-layout">',
    '    ' + renderLessonToc(),
    '    <article class="study-article">',
    '      <section id="syllabus" class="study-section">',
    '        <p class="section-badge">Syllabus map</p>',
    '        <h2 class="section-title">What this lesson covers</h2>',
    '        <p class="section-desc">This lesson focuses on the listed AA SL syllabus points. Use the topic overview for the complete syllabus map and links to the other lessons.</p>',
    '        ' + renderCoverage(lesson.coverage),
    '      </section>',
    '      <section id="key-ideas" class="study-section">',
    '        <p class="section-badge">Learn the ideas</p>',
    '        <h2 class="section-title">Key ideas and methods</h2>',
    '        <ul class="study-points">' + lesson.points.map((point) => '<li>' + esc(point) + '</li>').join('') + '</ul>',
    '      </section>',
    '      <section id="worked-example" class="study-section">',
    '        <p class="section-badge">Follow the reasoning</p>',
    '        <h2 class="section-title">Worked example</h2>',
    '        <p class="section-desc">This original example shows the method step by step; it is not copied from an IB examination paper.</p>',
    '        ' + renderExamples([lesson.example]),
    '      </section>',
    '      <section id="practice" class="study-section">',
    '        <p class="section-badge">Try it yourself</p>',
    '        <h2 class="section-title">Practice with worked answers</h2>',
    '        ' + renderPractice(lesson.practice),
    '      </section>',
    '      <section id="common-mistakes" class="study-section">',
    '        <p class="section-badge">Avoid these slips</p>',
    '        <h2 class="section-title">Common mistakes</h2>',
    '        <ul class="study-points">' + lesson.mistakes.map((item) => '<li>' + esc(item) + '</li>').join('') + '</ul>',
    '      </section>',
    '      <section id="more-lessons" class="study-section">',
    '        <p class="section-badge">Continue studying</p>',
    '        <h2 class="section-title">More ' + esc(topic.name) + ' lessons</h2>',
    '        <div class="lesson-grid">' + moreLessons + '</div>',
    '      </section>',
    '      <section class="study-section source-note">',
    '        <h2>About this guide</h2>',
    '        <p>This is an independent SJMaths study resource, not an official IB publication. It follows the current AA guide first assessed in 2021. The IB states that this curriculum has its final assessment in November 2028; students beginning the new course should use the separate first-assessment-2029 guide when available.</p>',
    '        <p>Check the <a href="' + esc(data.officialOverview) + '">IB Mathematics programme page</a> and the <a href="' + esc(data.officialGuide) + '">official AA subject guide</a> for the authoritative syllabus and examination-session requirements.</p>',
    '      </section>',
    '      <nav class="related-guides" aria-label="Related study guides">' + related.join('') + '</nav>',
    '    </article>',
    '  </div>',
    '</main>',
    '<footer class="ib-footer"><p>© 2026 SJMaths · IB DP Mathematics resources · Created by Sandeep Jaiswal (PGT Maths).</p><p>Independent study material; not affiliated with or endorsed by the International Baccalaureate.</p></footer>',
    '<script src="/assets/js/ib-theme.min.js?v=97caae90" defer></script>',
    '</body>',
    '</html>',
  ];
  const html = pageHead(page, url, crumbs, 'IB DP Mathematics AA SL · ' + topic.name) + '\n' + body.join('\n');
  const output = path.join(ROOT, lessonPath, 'index.html');
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, html + '\n', 'utf8');
  return output;
}

function renderTopicGuide(topic, index) {
  const slug = topic.slug;
  const pagePath = basePath + 'analysis-and-approaches-sl/' + slug + '/';
  const url = baseUrl + 'analysis-and-approaches-sl/' + slug + '/';
  const crumbs = [
    { name: 'Home', url: 'https://sjmaths.com/' },
    { name: 'IB Mathematics', url: 'https://sjmaths.com/ib/' },
    { name: 'IB DP Mathematics', url: baseUrl },
    { name: 'AA SL', url: baseUrl + 'analysis-and-approaches-sl/' },
    { name: topic.name, url },
  ];
  const previous = data.topics[index - 1];
  const next = data.topics[index + 1];
  const moreLinks = [];
  if (previous) moreLinks.push('<a href="' + pagePath.replace(slug + '/', previous.slug + '/') + '"><span>Previous topic</span><strong>Topic ' + previous.number + ': ' + esc(previous.name) + '</strong></a>');
  if (next) moreLinks.push('<a href="' + pagePath.replace(slug + '/', next.slug + '/') + '"><span>Next topic</span><strong>Topic ' + next.number + ': ' + esc(next.name) + '</strong></a>');
  moreLinks.push('<a href="/ib/dp-mathematics/aa-vs-ai/"><span>Course choice</span><strong>Compare IB Math AA and AI</strong></a>');
  moreLinks.push('<a href="/ib/command-terms/"><span>Exam language</span><strong>IB command terms</strong></a>');

  const sections = [
    '<body>',
    header('AA SL'),
    '<section class="ib-hero">',
    '  <div class="ib-hero-container">',
    '    ' + breadcrumbMarkup(crumbs),
    '    <p class="guide-kicker">IB Diploma Programme · Mathematics: Analysis and Approaches · Standard Level</p>',
    '    <h1 class="ib-hero-title">' + esc(topic.name) + ' for IB Math AA SL</h1>',
    '    <p class="ib-hero-desc">' + esc(topic.intro) + '</p>',
    '    <div class="meta-pills">',
    '      <span class="meta-pill">Topic ' + topic.number + ' of 5</span>',
    '      <span class="meta-pill">Standard Level</span>',
    '      <span class="meta-pill">Current syllabus · final assessment Nov 2028</span>',
    '    </div>',
    '  </div>',
    '</section>',
    '<main id="main-content" class="main-content study-main">',
    '  <div class="study-layout">',
    '    ' + renderGuideToc(),
    '    <article class="study-article">',
    '      <section id="syllabus" class="study-section">',
    '        <p class="section-badge">Syllabus map</p>',
    '        <h2 class="section-title">AA SL ' + topic.name + ' syllabus</h2>',
    '        <p class="section-desc">The checklist below names the Standard Level syllabus points for this topic. Higher Level extensions are not included on this page.</p>',
    '        ' + renderCoverage(topic.coverage),
    '      </section>',
    '      <section id="topic-lessons" class="study-section">',
    '        <p class="section-badge">Study by topic</p>',
    '        <h2 class="section-title">' + esc(topic.name) + ' lessons</h2>',
    '        <p class="section-desc">Work through focused lessons mapped to the syllabus points. Each lesson includes concise notes, an original worked example, practice and common mistakes.</p>',
    '        ' + renderLessonCards(topic),
    '      </section>',
    '      <section id="key-ideas" class="study-section">',
    '        <p class="section-badge">Learn the ideas</p>',
    '        <h2 class="section-title">Key ideas and methods</h2>',
    '        ' + renderSections(topic.sections),
    '      </section>',
    '      <section id="worked-examples" class="study-section">',
    '        <p class="section-badge">Follow the reasoning</p>',
    '        <h2 class="section-title">Worked examples</h2>',
    '        <p class="section-desc">These original examples show common reasoning steps. They are not copied from IB examination papers.</p>',
    '        ' + renderExamples(topic.examples),
    '      </section>',
    '      <section id="practice" class="study-section">',
    '        <p class="section-badge">Try it yourself</p>',
    '        <h2 class="section-title">Practice with worked answers</h2>',
    '        <ol class="practice-list">' + topic.practice.map((item, qIndex) => '<li>' +
      '<p><strong>Question ' + (qIndex + 1) + '.</strong> ' + esc(item.question) + '</p>' +
      '<details><summary>Show worked answer</summary><p>' + esc(item.solution) + '</p></details>' +
      '</li>').join('') + '</ol>',
    '      </section>',
    '      <section class="study-section">',
    '        <p class="section-badge">Avoid these slips</p>',
    '        <h2 class="section-title">Common mistakes</h2>',
    '        <ul class="study-points">' + topic.commonMistakes.map((item) => '<li>' + esc(item) + '</li>').join('') + '</ul>',
    '      </section>',
    '      <section id="revision" class="study-section revision-panel">',
    '        <p class="section-badge">Before you move on</p>',
    '        <h2 class="section-title">Revision checklist</h2>',
    '        <ul class="checklist">' + topic.revision.map((item) => '<li>' + esc(item) + '</li>').join('') + '</ul>',
    '      </section>',
    '      <section class="study-section source-note">',
    '        <h2>About this guide</h2>',
    '        <p>This is an independent SJMaths study resource, not an official IB publication. It follows the current AA guide first assessed in 2021. The IB states that this curriculum has its final assessment in November 2028; students beginning the new course should use the separate first-assessment-2029 guide when available.</p>',
    '        <p>Check the <a href="' + esc(data.officialOverview) + '">IB Mathematics programme page</a> and the <a href="' + esc(data.officialGuide) + '">official AA subject guide</a> for the authoritative syllabus and examination-session requirements.</p>',
    '      </section>',
    '      <nav class="related-guides" aria-label="Related study guides">' + moreLinks.join('') + '</nav>',
    '    </article>',
    '  </div>',
    '</main>',
    '<footer class="ib-footer"><p>© 2026 SJMaths · IB DP Mathematics resources · Created by Sandeep Jaiswal (PGT Maths).</p><p>Independent study material; not affiliated with or endorsed by the International Baccalaureate.</p></footer>',
    '<script src="/assets/js/ib-theme.min.js?v=97caae90" defer></script>',
    '</body>',
    '</html>',
  ];
  const page = { ...topic, seoTitle: topic.name + ' | IB Math AA SL | SJMaths' };
  const html = pageHead(page, url, crumbs, 'IB DP Mathematics AA SL · Topic ' + topic.number) + '\n' + sections.join('\n');
  const output = path.join(ROOT, pagePath, 'index.html');
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, html + '\n', 'utf8');
  return output;
}

function renderComparison() {
  const page = data.comparison;
  const url = baseUrl + page.slug + '/';
  const crumbs = [
    { name: 'Home', url: 'https://sjmaths.com/' },
    { name: 'IB Mathematics', url: 'https://sjmaths.com/ib/' },
    { name: 'IB DP Mathematics', url: baseUrl },
    { name: 'AA vs AI', url },
  ];
  const rows = page.rows.map((row) => '<tr><th scope="row">' + esc(row.factor) + '</th><td>' + esc(row.aa) + '</td><td>' + esc(row.ai) + '</td></tr>').join('');
  const questions = page.faq.map((item) => '<details class="faq-item"><summary>' + esc(item.question) + '</summary><p>' + esc(item.answer) + '</p></details>').join('');
  const body = [
    '<body>',
    header('DP Math'),
    '<section class="ib-hero">',
    '  <div class="ib-hero-container">',
    '    ' + breadcrumbMarkup(crumbs),
    '    <p class="guide-kicker">IB Diploma Programme · Course choice guide</p>',
    '    <h1 class="ib-hero-title">IB Math AA vs AI</h1>',
    '    <p class="ib-hero-desc">' + esc(page.intro) + '</p>',
    '    <div class="meta-pills"><span class="meta-pill">AA or AI</span><span class="meta-pill">SL or HL</span><span class="meta-pill">Current syllabus through Nov 2028</span></div>',
    '  </div>',
    '</section>',
    '<main id="main-content" class="main-content study-main compare-main">',
    '  <article class="study-article compare-article">',
    '    <section class="study-section">',
    '      <p class="section-badge">Compare the courses</p>',
    '      <h2 class="section-title">What is the difference between IB Math AA and AI?</h2>',
    '      <p class="section-desc">Both courses build mathematical understanding, but their emphasis and exam technology rules differ. The current IB curriculum offers each course at SL and HL.</p>',
    '      <div class="comparison-table-wrap" role="region" aria-label="Scrollable AA and AI course comparison" tabindex="0"><table class="comparison-table"><caption>Current DP Mathematics courses (first assessment 2021)</caption><thead><tr><th scope="col">Aspect</th><th scope="col">Analysis and Approaches (AA)</th><th scope="col">Applications and Interpretation (AI)</th></tr></thead><tbody>' + rows + '</tbody></table></div>',
    '    </section>',
    '    <section class="study-section">',
    '      <p class="section-badge">Make a considered choice</p>',
    '      <h2 class="section-title">How should I choose?</h2>',
    '      <ul class="study-points">' + page.guidance.map((item) => '<li>' + esc(item) + '</li>').join('') + '</ul>',
    '    </section>',
    '    <section class="study-section assessment-callout">',
    '      <p class="section-badge">Assessment snapshot</p>',
    '      <h2 class="section-title">How do the exams differ?</h2>',
    '      <p>' + esc(page.assessment) + '</p>',
    '    </section>',
    '    <section class="study-section">',
    '      <p class="section-badge">Common questions</p>',
    '      <h2 class="section-title">AA vs AI FAQs</h2>',
    '      <div class="faq-list">' + questions + '</div>',
    '    </section>',
    '    <section class="study-section source-note">',
    '      <h2>Check the official course information</h2>',
    '      <p>Course descriptions and assessment rules can change by syllabus session. Confirm your course choice and examination requirements with your school and the official IB materials.</p>',
    '      <ul><li><a href="' + esc(data.officialOverview) + '">IB DP Mathematics course overview and syllabus transition</a></li><li><a href="' + esc(data.officialGuide) + '">IB Mathematics: Analysis and Approaches guide</a></li><li><a href="https://www.ibo.org/globalassets/new-structure/university-admission/pdfs/dp-mathematics-applications-and-interpretation-guide-en.pdf">IB Mathematics: Applications and Interpretation guide</a></li></ul>',
    '    </section>',
    '    <nav class="related-guides" aria-label="Related IB mathematics resources">',
    '      <a href="/ib/dp-mathematics/"><span>Course hub</span><strong>IB DP Mathematics</strong></a>',
    '      <a href="/ib/dp-mathematics/analysis-and-approaches-sl/"><span>Available course guide</span><strong>Math AA SL topics and resources</strong></a>',
    '      <a href="/ib/command-terms/"><span>Exam language</span><strong>IB command terms</strong></a>',
    '    </nav>',
    '    <p class="independent-note">This independent guide is not affiliated with or endorsed by the International Baccalaureate.</p>',
    '  </article>',
    '</main>',
    '<footer class="ib-footer"><p>© 2026 SJMaths · IB DP Mathematics resources · Created by Sandeep Jaiswal (PGT Maths).</p></footer>',
    '<script src="/assets/js/ib-theme.min.js?v=97caae90" defer></script>',
    '</body>',
    '</html>',
  ];
  const html = pageHead(page, url, crumbs, 'IB DP Mathematics course selection') + '\n' + body.join('\n');
  const output = path.join(ROOT, 'ib/dp-mathematics', page.slug, 'index.html');
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, html + '\n', 'utf8');
  return output;
}

function main() {
  validateLessons();
  const outputs = data.topics.map(renderTopicGuide);
  for (const topic of data.topics) {
    (lessonsByTopic.get(topic.slug) || []).forEach((lesson, index) => outputs.push(renderLesson(lesson, index)));
  }
  outputs.push(renderComparison());
  console.log('Generated ' + outputs.length + ' IB DP Mathematics pages:');
  for (const output of outputs) console.log('  ' + path.relative(ROOT, output).replaceAll(path.sep, '/'));
}

function validateLessons() {
  if (!Array.isArray(lessonData.lessons) || lessonData.lessons.length === 0) throw new Error('Lesson data must contain at least one lesson.');
  const routeKeys = new Set();
  for (const lesson of lessonData.lessons) {
    if (!data.topics.some((topic) => topic.slug === lesson.parentSlug)) throw new Error('Unknown lesson parent: ' + lesson.parentSlug);
    const routeKey = lesson.parentSlug + '/' + lesson.slug;
    if (routeKeys.has(routeKey)) throw new Error('Duplicate lesson route: ' + routeKey);
    routeKeys.add(routeKey);
    if (!lesson.slug || !lesson.title || !lesson.description || !lesson.intro || !lesson.code ||
      !Array.isArray(lesson.coverage) || !lesson.coverage.length || !Array.isArray(lesson.points) || !lesson.points.length ||
      !lesson.example || !Array.isArray(lesson.practice) || !lesson.practice.length || !Array.isArray(lesson.mistakes) || !lesson.mistakes.length) {
      throw new Error('Incomplete lesson record: ' + routeKey);
    }
  }
  for (const topic of data.topics) {
    const topicLessons = lessonsByTopic.get(topic.slug) || [];
    if (!topicLessons.length) throw new Error('No topic lessons found for ' + topic.slug);
    const coveredCodes = new Set(topicLessons.flatMap((lesson) => lesson.coverage.map((item) => item.match(/^(\d+\.\d+)/)?.[1]).filter(Boolean)));
    const requiredCodes = topic.coverage.map((item) => item.match(/^(\d+\.\d+)/)?.[1]).filter(Boolean);
    const missingCodes = requiredCodes.filter((code) => !coveredCodes.has(code));
    if (missingCodes.length) throw new Error('Lessons do not cover ' + topic.slug + ' syllabus points: ' + missingCodes.join(', '));
  }
}

main();
