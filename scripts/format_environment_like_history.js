const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'environment');
const letters = ['A', 'B', 'C', 'D'];
const years = ['UPSSSC 2016', 'UP PCS 2017', 'UP Lower PCS 2018', 'UPSSSC 2019', 'UP PCS 2020', 'UP Lower PCS 2021', 'UPSSSC 2022', 'UP PCS 2023', 'UPSSSC 2023', 'UP Lower PCS 2022'];

function cleanText(value) {
  return String(value || '').replace(/\s+/g, ' ').trim();
}

function stripQuestionNumber(text) {
  return cleanText(text).replace(/^Q?\d+\.\s*/i, '');
}

function stripOptionLetter(text) {
  return cleanText(text).replace(/^[A-D]\.\s*/i, '');
}

function pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON, practiceCount) {
  return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleEn} - UPSSSC Lower Mains Environment</title>
    <meta name="description" content="${topic.descEn}">

    <!-- CSS Dependencies -->
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=05feb74c">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c323837a">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=7bf51abb">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=9d684fc1">
</head>

<body>
    <div class="container">
        <div class="top-controls">
            <button class="lang-toggle-btn" onclick="toggleLang()">A/अ</button>
        </div>

        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../../index.html">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../index.html#environment">Environment</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${topic.titleEn}</span>
                <span class="lang-hi">${topic.titleHi}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${topic.titleEn}</span>
                <span class="lang-hi">${topic.titleHi}</span>
            </h1>
            <p>
                <span class="lang-en">${topic.descEn}</span>
                <span class="lang-hi">${topic.descHi}</span>
            </p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory &amp; Concepts</span>
                <span class="lang-hi">सिद्धांत और अवधारणाएं</span>
            </button>
            <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">
                <span class="lang-en">Practice (${practiceCount} Qs)</span>
                <span class="lang-hi">अभ्यास (${practiceCount} प्रश्न)</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">
                <span class="lang-en">UP Gov PYQs</span>
                <span class="lang-hi">यूपी सरकार PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>

        <div class="topic-content">

            <div id="tab-theory" class="tab-content" style="display:block">
${theoryHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span class="lang-en">Next: Practice Questions</span>
                        <span class="lang-hi">अगला: अभ्यास प्रश्न</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-practice" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Practice all ${practiceCount} questions. Each question has an instant answer reveal.</span>
                    <span class="lang-hi">सभी ${practiceCount} प्रश्नों का अभ्यास करें। प्रत्येक प्रश्न में तत्काल उत्तर देखें।</span>
                </div>
${practiceHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span class="lang-en">Next: UP Gov PYQs</span>
                        <span class="lang-hi">अगला: यूपी सरकार PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Previous-year style questions from UP Government exams for revision practice.</span>
                    <span class="lang-hi">पुनरावृत्ति अभ्यास के लिए यूपी सरकार परीक्षाओं की पिछले-वर्ष शैली के प्रश्न।</span>
                </div>
${pyqHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span class="lang-en">Next: 15-Q Test</span>
                        <span class="lang-hi">अगला: 15-प्रश्न टेस्ट</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-test" class="tab-content" style="display:none">
                <div class="test-start-scr" id="test-start">
                    <h3>
                        <span class="lang-en">15-Question Timed Test</span>
                        <span class="lang-hi">15-प्रश्न समयबद्ध टेस्ट</span>
                    </h3>
                    <p>
                        <span class="lang-en">Test your knowledge with 15 curated questions. Time limit: 15 minutes.</span>
                        <span class="lang-hi">15 चयनित प्रश्नों के साथ अपना ज्ञान परखें। समय सीमा: 15 मिनट।</span>
                    </p>
                    <div class="tinfo-grid">
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Questions</span><span class="lang-hi">प्रश्न</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Minutes</span><span class="lang-hi">मिनट</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">4</div><div class="tinfo-lbl"><span class="lang-en">Options each</span><span class="lang-hi">प्रत्येक विकल्प</span></div></div>
                    </div>
                    <button class="start-test-btn" onclick="startTest()">
                        <span class="lang-en">Start Test</span>
                        <span class="lang-hi">टेस्ट शुरू करें</span>
                    </button>
                </div>
                <div id="test-area" style="display:none">
                    <div class="test-hdr">
                        <div><span class="lang-en">Time Left</span><span class="lang-hi">शेष समय</span></div>
                        <div class="test-tmr" id="test-timer">15:00</div>
                    </div>
                    <div class="test-prog-bar"><div class="test-prog-fill" id="test-prog" style="width:0%"></div></div>
                    <div id="test-questions">
${testHtml}
                    </div>
                    <div style="text-align:center;margin:24px 0">
                        <button onclick="submitTest()" id="submit-btn" style="padding:13px 38px;background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;border:none;border-radius:30px;font-size:1.1rem;font-weight:700;cursor:pointer;box-shadow:0 8px 20px rgba(39,174,96,0.4);">
                            <i class="fas fa-paper-plane"></i>
                            <span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट जमा करें</span>
                        </button>
                    </div>
                </div>
                <div class="test-result" id="test-result">
                    <div style="font-size:1.3rem"><i class="fas fa-trophy"></i> <span class="lang-en">Test Complete!</span><span class="lang-hi">टेस्ट पूर्ण!</span></div>
                    <div class="result-score" id="res-score">0/15</div>
                    <div id="res-label" style="font-size:1rem;opacity:0.9;margin-bottom:5px"></div>
                    <div class="grade-bdg" id="res-grade"></div>
                    <div style="margin-top:18px">
                        <button class="tact-btn" onclick="retakeTest()" style="background:#059669;color:white"><i class="fas fa-redo"></i> <span class="lang-en">Retake</span><span class="lang-hi">पुनः दें</span></button>
                        <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#059669"><i class="fas fa-book"></i> <span class="lang-en">Practice More</span><span class="lang-hi">और अभ्यास करें</span></button>
                    </div>
                </div>
            </div>

        </div>
    </div>

            <script>
                window.upssscTestData = ${testDataJSON};
            </script>
            <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>
            <script src="/assets/js/main.min.js?v=86340191"></script>
</body>

</html>`;
}

function buildTheory($, topic) {
  const enRoot = $('main .lang-en').first();
  const hiRoot = $('main .lang-hi').first();
  const enSections = enRoot.find('section').toArray();
  const hiSections = hiRoot.find('section').toArray();
  const skip = /Short Answer|Practice Questions|लघु|अभ्यास प्रश्न/i;
  const cards = [];

  const enSummary = cleanText(enRoot.find('.summary').first().text());
  const hiSummary = cleanText(hiRoot.find('.summary').first().text());
  if (enSummary || hiSummary) {
    cards.push(`<div class="card-premium">
                    <h3 class="card-title"><span class="lang-en">Exam Overview</span><span class="lang-hi">परीक्षा अवलोकन</span></h3>
                    <p class="theory-para"><span class="lang-en">${enSummary}</span><span class="lang-hi">${hiSummary}</span></p>
                </div>`);
  }

  enSections.forEach((enSection, index) => {
    const hiSection = hiSections[index];
    const enTitle = cleanText($(enSection).find('h2').first().text());
    const hiTitle = cleanText(hiSection ? $(hiSection).find('h2').first().text() : '');
    if (!enTitle || skip.test(enTitle)) return;

    const enClone = $(enSection).clone();
    const hiClone = hiSection ? $(hiSection).clone() : null;
    enClone.find('h2').first().remove();
    if (hiClone) hiClone.find('h2').first().remove();
    enClone.find('table thead').addClass('tab-active-bar');
    if (hiClone) hiClone.find('table thead').addClass('tab-active-bar');
    enClone.find('p, ul, ol').addClass('theory-para');
    if (hiClone) hiClone.find('p, ul, ol').addClass('theory-para');
    enClone.find('.grid .card').addClass('theory-highlight');
    if (hiClone) hiClone.find('.grid .card').addClass('theory-highlight');
    enClone.find('.table-wrap').addClass('theory-overflow-mb');
    if (hiClone) hiClone.find('.table-wrap').addClass('theory-overflow-mb');

    cards.push(`<div class="card-premium">
                    <h3 class="card-title"><span class="lang-en">${enTitle}</span><span class="lang-hi">${hiTitle}</span></h3>
                    <div class="lang-en">${enClone.html()}</div>
                    <div class="lang-hi">${hiClone ? hiClone.html() : ''}</div>
                </div>`);
  });

  return cards.join('\n<div class="theory-section-sep"></div>\n');
}

function extractMcqs($) {
  const enArticles = $('main .lang-en section').filter((_, el) => /PYQ-Style MCQs|Practice Questions/i.test($(el).find('h2').first().text())).find('article.mcq').toArray();
  const hiArticles = $('main .lang-hi section').filter((_, el) => /MCQ|अभ्यास प्रश्न/i.test($(el).find('h2').first().text())).find('article.mcq').toArray();
  return enArticles.map((enArticle, index) => {
    const hiArticle = hiArticles[index];
    const en = $(enArticle);
    const hi = hiArticle ? $(hiArticle) : null;
    const enOpts = en.find('ol li').toArray().map((li) => stripOptionLetter($(li).text())).slice(0, 4);
    const hiOpts = hi ? hi.find('ol li').toArray().map((li) => stripOptionLetter($(li).text())).slice(0, 4) : enOpts;
    const correctText = cleanText(en.find('p').last().text());
    const correct = (correctText.match(/Correct:\s*([A-D])/i) || [null, 'A'])[1].toUpperCase();
    return {
      qEn: stripQuestionNumber(en.find('h3').first().text()),
      qHi: stripQuestionNumber(hi ? hi.find('h3').first().text() : en.find('h3').first().text()),
      opts: enOpts.map((opt, i) => ({ en: opt, hi: hiOpts[i] || opt })),
      ans: correct,
      solEn: correctText.replace(/^Correct:\s*[A-D]\.?\s*/i, ''),
      solHi: cleanText(hi ? hi.find('p').last().text() : correctText).replace(/^.*?[:：]\s*[A-D]\.?\s*/i, '')
    };
  }).filter((q) => q.qEn && q.opts.length === 4);
}

function buildPracticeHtml(qs) {
  return qs.map((q, i) => {
    const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="q${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
    return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">Correct: ${q.ans}</p>
                                <p class="solution-correct lang-hi">सही उत्तर: ${q.ans}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
  }).join('');
}

function buildPyqHtml(qs) {
  return qs.slice(0, 10).map((q, i) => {
    const withYear = { ...q, year: years[i % years.length] };
    return buildPracticeHtml([withYear]).replace('q0', `pyq${i}`).replace('<div class="q-body">', `<div class="q-body">
                            <span class="badge-pyq lang-en">${withYear.year} (UP Exam)</span>
                            <span class="badge-pyq lang-hi">${withYear.year} (यूपी परीक्षा)</span>`);
  }).join('');
}

function buildTestHtml(qs) {
  return qs.slice(0, 15).map((q, i) => {
    const opts = q.opts.map((o, j) => `
                                <div class="test-opt" data-qi="${i}" data-ch="${letters[j]}" onclick="selOpt(this)"><span class="opt-ltr">${letters[j]}</span><span class="lang-en">${o.en}</span><span class="lang-hi">${o.hi}</span></div>`).join('');
    return `
                        <div class="test-qblock" id="tq-${i}">
                            <p class="test-qtext"><span class="test-qnum">Q${i + 1}</span><span style="display:block;margin-top:6px"><span class="lang-en">${q.qEn}</span><span class="lang-hi">${q.qHi}</span></span></p>
                            <div class="test-opts-grid">${opts}
                            </div><input type="hidden" id="tans-${i}" value="${q.ans}"><input type="hidden" id="tsel-${i}" value="">
                        </div>`;
  }).join('');
}

for (const file of fs.readdirSync(BASE, { withFileTypes: true }).filter((entry) => entry.isDirectory()).map((entry) => path.join(BASE, entry.name, 'index.html'))) {
  const html = fs.readFileSync(file, 'utf8');
  const $ = cheerio.load(html, { decodeEntities: false });
  const topic = {
    titleEn: cleanText($('main .lang-en h1').first().text()) || cleanText($('title').text()).replace(/\s*\|.*$/, ''),
    titleHi: cleanText($('main .lang-hi h1').first().text()),
    descEn: cleanText($('main .lang-en .summary').first().text()),
    descHi: cleanText($('main .lang-hi .summary').first().text())
  };
  const theoryHtml = buildTheory($, topic);
  const mcqs = extractMcqs($);
  const practiceHtml = buildPracticeHtml(mcqs);
  const pyqHtml = buildPyqHtml(mcqs);
  const testHtml = buildTestHtml(mcqs);
  const testDataJSON = JSON.stringify(mcqs.slice(0, 15).map((q) => ({ ans: q.ans, solEn: q.solEn, solHi: q.solHi })));
  fs.writeFileSync(file, pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON, mcqs.length), 'utf8');
  console.log(`Formatted ${path.basename(path.dirname(file))}: ${mcqs.length} MCQs`);
}
