import fs from 'node:fs/promises';
import path from 'node:path';
import * as cheerio from 'cheerio';

const baseDir = path.resolve('ssc-cgl/general-awareness/history-and-culture');

const topics = [
  'rise-of-mahajanapadas-magadha-empire',
  'buddhism-life-of-buddha-teachings-councils',
  'jainism-mahavira-philosophy-sects',
  'mauryan-empire',
  'gupta-empire',
  'post-gupta-period'
];

const esc = (value = '') => String(value)
  .replace(/&/g, '&amp;')
  .replace(/</g, '&lt;')
  .replace(/>/g, '&gt;')
  .replace(/"/g, '&quot;');

function html($, node) {
  return $(node).html() || '';
}

function extractQuestions($, selector) {
  const letters = ['A', 'B', 'C', 'D'];
  return $(selector).map((_, card) => {
    const qRaw = $(card).find('h4').first().text().trim();
    const q = qRaw.replace(/^Q\d+\.\s*/, '').trim();
    const options = $(card).find('.option').map((__, option) => {
      return $(option).text().replace(/^[A-D]\.\s*/, '').trim();
    }).get();
    const answerLine = $(card).find('.answer-box').first().text().trim();
    const answerLetter = (answerLine.match(/Answer:\s*([A-D])/) || [])[1] || 'A';
    const explanation = $(card).find('.answer-box p').first().text().trim();
    return { q, options, answer: letters.indexOf(answerLetter), explanation };
  }).get();
}

function extractPage(file) {
  const $ = cheerio.load(file);
  const title = $('.topic-header h1').first().text().trim() || $('title').text().replace('| SSC CGL | SJMaths', '').trim();
  const description = $('meta[name="description"]').attr('content') || $('.topic-header p').first().text().trim();
  const theory = $('#tab-theory .card-premium').map((_, card) => ({
    heading: $(card).find('.card-title').first().text().trim(),
    bodyHtml: html($, $(card).find('.theory-para').first())
  })).get();
  const practice = extractQuestions($, '#tab-practice .practice-question-card');
  const pyqs = extractQuestions($, '#tab-pyqs .practice-question-card');
  const test = extractQuestions($, '#tab-test .practice-question-card');
  return { title, description, theory, practice, pyqs, test };
}

function nav() {
  return `<div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory & Concepts</span>
                <span class="lang-hi">सिद्धांत और अवधारणाएं</span>
            </button>
            <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">
                <span class="lang-en">Practice (30 Qs)</span>
                <span class="lang-hi">अभ्यास (30 प्रश्न)</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">
                <span class="lang-en">SSC PYQs</span>
                <span class="lang-hi">SSC PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>`;
}

function practiceCard(q, index, group, prefix) {
  const letters = ['A', 'B', 'C', 'D'];
  return `<div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${index + 1}</div>
                        <div class="q-body">
                            <p class="lang-en q-text-sm">${esc(q.q)}</p>
                            <p class="lang-hi q-text-sm">${esc(q.q)}</p>
                            <div class="options-container">
                                ${q.options.map((option, optIndex) => `<div class="practice-option-box">
                                    <label class="opt-label">
                                        <input type="radio" name="${prefix}${index}" class="opt-radio">
                                        <span><b>${letters[optIndex]}.</b> ${esc(option)}</span>
                                    </label>
                                </div>`).join('\n                                ')}
                            </div>
                            <div class="sol-box">
                                <p class="sol-text"><strong>Answer: ${letters[q.answer]}.</strong> ${esc(q.options[q.answer] || '')}</p>
                                <p class="sol-text">${esc(q.explanation)}</p>
                            </div>
                        </div>
                    </div>
                </div>`;
}

function pyqCard(q, index) {
  const letters = ['A', 'B', 'C', 'D'];
  return `<div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${index + 1}</div>
                        <div class="q-body">
                            <div class="q-header"><span class="exam-badge"><i class="fas fa-award"></i> SSC PYQ Pattern</span>
                                <p class="q-text"><span class="lang-en">${esc(q.q)}</span><span class="lang-hi">${esc(q.q)}</span></p>
                            </div>
                            <div class="q-options">
                                ${q.options.map((option, optIndex) => `<div class="practice-option-box" onclick="this.querySelector('input').checked=true">
                                    <label class="opt-label"><input type="radio" name="pyq${index}" class="opt-radio">
                                        <span><b>${letters[optIndex]}.</b> ${esc(option)}</span></label>
                                </div>`).join('\n                                ')}
                            </div>
                            <div class="sol-box">
                                <p class="sol-text"><strong>Answer: ${letters[q.answer]}.</strong> ${esc(q.options[q.answer] || '')}</p>
                                <p class="sol-text">${esc(q.explanation)}</p>
                            </div>
                        </div>
                    </div>
                </div>`;
}

function practiceTab(questions) {
  const groups = [
    ['easy', questions.slice(0, 10)],
    ['moderate', questions.slice(10, 20)],
    ['hard', questions.slice(20, 30)]
  ];
  return `<div id="tab-practice" class="tab-content" style="display:none">
                <div class="diff-tab-bar">
                    <button class="diff-nav-item active diff-tab-btn-active" id="btn-diff-easy" onclick="switchDifficulty('easy')"><span class="lang-en">Easy (1-10)</span><span class="lang-hi">आसान (1-10)</span></button>
                    <button class="diff-nav-item diff-tab-btn-inactive" id="btn-diff-moderate" onclick="switchDifficulty('moderate')"><span class="lang-en">Moderate (11-20)</span><span class="lang-hi">मध्यम (11-20)</span></button>
                    <button class="diff-nav-item diff-tab-btn-inactive" id="btn-diff-hard" onclick="switchDifficulty('hard')"><span class="lang-en">Hard (21-30)</span><span class="lang-hi">कठिन (21-30)</span></button>
                </div>
                ${groups.map(([name, items]) => `<div id="diff-${name}" class="difficulty-section" style="display:${name === 'easy' ? 'block' : 'none'}">${items.map((q, i) => practiceCard(q, i + (name === 'easy' ? 0 : name === 'moderate' ? 10 : 20), name, 'practice')).join('\n')}</div>`).join('\n')}
            </div>`;
}

function testTab(questions) {
  return `<div id="tab-test" class="tab-content" style="display:none">
                <div id="test-start-scr" class="test-start-scr">
                    <h3><i class="fas fa-stopwatch"></i> <span class="lang-en">15-Question Timed Test</span><span class="lang-hi">15-प्रश्न टाइम्ड टेस्ट</span></h3>
                    <p style="color:#666;margin-bottom:20px"><span class="lang-en">Multi-statement & match-type questions - SSC CGL exam pattern</span><span class="lang-hi">बहु-कथन और मिलान प्रकार के प्रश्न - SSC CGL परीक्षा पैटर्न</span></p>
                    <div class="tinfo-grid">
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Questions</span><span class="lang-hi">प्रश्न</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Minutes</span><span class="lang-hi">मिनट</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">+2</div><div class="tinfo-lbl"><span class="lang-en">Marks</span><span class="lang-hi">अंक</span></div></div>
                    </div>
                    <button class="start-test-btn" onclick="startTest()"><i class="fas fa-play"></i> <span class="lang-en">Start Test</span><span class="lang-hi">टेस्ट शुरू करें</span></button>
                </div>
                <div id="test-area" style="display:none">${questions.map((q, i) => practiceCard(q, i, 'test', 'test')).join('\n')}</div>
            </div>`;
}

export function render(slug, data) {
  const canonical = `https://sjmaths.com/ssc-cgl/general-awareness/history-and-culture/${slug}/`;
  const testData = data.test.map((q) => ({ ans: ['A', 'B', 'C', 'D'][q.answer] || 'A', solEn: q.explanation, solHi: q.explanation }));
  return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${esc(data.title)} - SSC CGL</title>
    <meta name="description" content="${esc(data.description)}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="${canonical}">
    <meta property="og:title" content="${esc(data.title)} - SSC CGL">
    <meta property="og:description" content="${esc(data.description)}">
    <meta property="og:url" content="${canonical}">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="SJMaths">

    <!-- CSS Dependencies -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=c54bbbc3">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=94ee8a40">
</head>

<body>
  <!-- Dynamic Header Container -->
      <div id="header-container"></div>
    <div class="container">
        <div class="top-controls"></div>

        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <div class="breadcrumbs-path">
                <a href="../../../syllabus/">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../">History & Culture</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${esc(data.title)}</span>
                <span class="lang-hi">${esc(data.title)}</span>
            </div>
        </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${esc(data.title)}</span>
                <span class="lang-hi">${esc(data.title)}</span>
            </h1>
            <p>
                <span class="lang-en">${esc(data.description)}</span>
                <span class="lang-hi">${esc(data.description)}</span>
            </p>
        </div>

        ${nav()}

        <div class="topic-content">
            <div id="tab-theory" class="tab-content" style="display:block">
                ${data.theory.map((section) => `<div class="card-premium">
                    <h3 class="card-title"><span class="lang-en">${esc(section.heading)}</span><span class="lang-hi">${esc(section.heading)}</span></h3>
                    <div class="theory-para">${section.bodyHtml}</div>
                </div>`).join('\n')}
            </div>

            ${practiceTab(data.practice)}

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <h2 class="section-title"><span class="lang-en">SSC PYQs and Repeated Exam Themes (${data.pyqs.length} Questions)</span><span class="lang-hi">SSC PYQs और बार-बार पूछे जाने वाले विषय (${data.pyqs.length} प्रश्न)</span></h2>
                <div class="info-banner">
                    <p class="sol-text"><strong class="lang-en"><i class="fas fa-info-circle"></i> Note:</strong><strong class="lang-hi"><i class="fas fa-info-circle"></i> नोट:</strong> <span class="lang-en">These are SSC CGL level previous-year-style and repeated-theme questions.</span><span class="lang-hi">ये SSC CGL स्तर के पिछले-वर्ष शैली और repeated-theme प्रश्न हैं।</span></p>
                </div>
                ${data.pyqs.map((q, i) => pyqCard(q, i)).join('\n')}
            </div>

            ${testTab(data.test)}
        </div>
    </div>
    <script>
                window.upssscTestData = ${JSON.stringify(testData)};
            </script>

<!-- JavaScript Script References -->
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
    <script src="/assets/js/upsssc-lower.min.js?v=04b168f8" defer data-cfasync="false"></script>
</body>

</html>`;
}

if (import.meta.url === `file://${process.argv[1].replaceAll('\\', '/')}`) {
  for (const slug of topics) {
    const filePath = path.join(baseDir, slug, 'index.html');
    const current = await fs.readFile(filePath, 'utf8');
    const data = extractPage(current);
    await fs.writeFile(filePath, render(slug, data), 'utf8');
    console.log(`Reformatted ${filePath}`);
  }
}
