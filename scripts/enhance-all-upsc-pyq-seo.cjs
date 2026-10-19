const fs = require('fs');
const path = require('path');

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function renderQuestionArticle(q, topicName, idx, total, isDrill = false) {
  if (!q) return '';
  const qId = q.id || `q-${idx}`;
  const exam = q.exam || (isDrill ? 'UPSC Concept Drill' : 'UPSC Prelims');
  const year = q.year ? ` ${q.year}` : '';
  const qNum = q.questionNum ? ` · ${q.questionNum}` : '';
  const badgeText = isDrill ? `Concept Drill ${idx} of ${total}` : `${exam}${year}${qNum}`;

  let optionsHtml = '';
  let correctKey = '';
  let correctExpEn = '';
  let correctExpHi = '';

  if (Array.isArray(q.options)) {
    optionsHtml = q.options.map(opt => {
      const isCorrect = opt.correct === true;
      if (isCorrect) {
        correctKey = opt.key || '';
        if (opt.explanation?.en) correctExpEn = opt.explanation.en;
        if (opt.explanation?.hi) correctExpHi = opt.explanation.hi;
      }
      return `
        <div class="pyq-seo-option-row${isCorrect ? ' correct-option' : ''}">
          <strong>(${escapeHtml(opt.key)})</strong>
          <span class="lang-en">${escapeHtml(opt.text?.en || '')}</span>
          ${opt.text?.hi ? `<span class="lang-hi" lang="hi">${escapeHtml(opt.text.hi)}</span>` : ''}
          ${isCorrect ? '<span class="pyq-seo-correct-pill">✓ [Official Key]</span>' : ''}
        </div>`;
    }).join('\n');
  } else if (q.blank) {
    correctKey = q.blank.answer || '';
    correctExpEn = q.blank.explanation?.en || '';
    correctExpHi = q.blank.explanation?.hi || '';
    optionsHtml = `
      <div class="pyq-seo-option-row correct-option">
        <strong>Fill in the blank:</strong> <span>${escapeHtml(q.blank.answer || '')}</span>
      </div>`;
  }

  return `
    <article class="pyq-seo-question-item" id="seo-${escapeHtml(qId)}">
      <div class="pyq-seo-q-header">
        <span class="pyq-seo-badge">${escapeHtml(badgeText)}</span>
        <span class="pyq-seo-topic">${escapeHtml(topicName || '')}</span>
      </div>
      <div class="pyq-seo-q-text">
        <div class="lang-en"><strong>Question:</strong> ${escapeHtml(q.question?.en || '').replace(/\n/g, '<br>')}</div>
        ${q.question?.hi ? `<div class="lang-hi" lang="hi"><strong>प्रश्न:</strong> ${escapeHtml(q.question.hi).replace(/\n/g, '<br>')}</div>` : ''}
      </div>
      <div class="pyq-seo-options">
        ${optionsHtml}
      </div>
      <div class="pyq-seo-answer-box">
        <div class="pyq-seo-answer-key"><strong>Correct Answer:</strong> Option ${escapeHtml(correctKey)}</div>
        ${correctExpEn ? `<div class="lang-en"><strong>Explanation:</strong> ${escapeHtml(correctExpEn).replace(/\n/g, '<br>')}</div>` : ''}
        ${correctExpHi ? `<div class="lang-hi" lang="hi"><strong>व्याख्या:</strong> ${escapeHtml(correctExpHi).replace(/\n/g, '<br>')}</div>` : ''}
      </div>
    </article>`;
}

function getHtmlFiles(dir) {
  let res = [];
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) res = res.concat(getHtmlFiles(full));
    else if (ent.isFile() && ent.name === 'index.html' && full !== path.join('upsc-topicwise-pyqs', 'index.html')) res.push(full);
  }
  return res;
}

const files = getHtmlFiles('upsc-topicwise-pyqs');
console.log(`Processing ${files.length} topic files...`);

let updatedCount = 0;

for (const file of files) {
  let html = fs.readFileSync(file, 'utf8');

  // Fix broken subject links and structured data URLs
  html = html
    .replace(/href=["']\/upsc-topicwise-pyqs\/ancient-history\/["']/g, 'href="/upsc-topicwise-pyqs/#subj-ancient-history"')
    .replace(/"item":\s*"https:\/\/sjmaths\.com\/upsc-topicwise-pyqs\/ancient-history\/"/g, '"item": "https://sjmaths.com/upsc-topicwise-pyqs/#subj-ancient-history"')
    .replace(/href=["']\/upsc-topicwise-pyqs\/art-and-culture\/["']/g, 'href="/upsc-topicwise-pyqs/#subj-art-culture"')
    .replace(/"item":\s*"https:\/\/sjmaths\.com\/upsc-topicwise-pyqs\/art-and-culture\/"/g, '"item": "https://sjmaths.com/upsc-topicwise-pyqs/#subj-art-culture"')
    .replace(/href=["']\/upsc-topicwise-pyqs\/medieval-history\/["']/g, 'href="/upsc-topicwise-pyqs/#subj-medieval-history"')
    .replace(/"item":\s*"https:\/\/sjmaths\.com\/upsc-topicwise-pyqs\/medieval-history\/"/g, '"item": "https://sjmaths.com/upsc-topicwise-pyqs/#subj-medieval-history"')
    .replace(/href=["']\/upsc-topicwise-pyqs\/modern-history\/["']/g, 'href="/upsc-topicwise-pyqs/#subj-modern-history"')
    .replace(/"item":\s*"https:\/\/sjmaths\.com\/upsc-topicwise-pyqs\/modern-history\/"/g, '"item": "https://sjmaths.com/upsc-topicwise-pyqs/#subj-modern-history"');

  // Title trimming if > 115 chars
  let titleMatch = html.match(/<title>([\s\S]*?)<\/title>/i);
  let title = titleMatch ? titleMatch[1].trim() : '';
  if (title.length > 115) {
    title = title.replace(/\s*-\s*UPSC Topicwise PYQs & Concept Drills \(1995-2026\)/, ' - UPSC PYQs & Drills (1995-2026)');
    if (title.length > 115) {
      title = title.replace(/\s*-\s*UPSC Topicwise PYQs \(1995-2026\)/, ' - UPSC PYQs (1995-2026)');
    }
    if (title.length > 115) {
      title = title.slice(0, 112).trim() + '...';
    }
    html = html.replace(/<title>[\s\S]*?<\/title>/i, `<title>${title}</title>`);
  }

  // Description trimming if > 300 chars
  let descMatch = html.match(/<meta\s+name=["']description["']\s+content=["']([\s\S]*?)["']/i);
  let desc = descMatch ? descMatch[1].trim() : '';
  if (desc.length > 300) {
    desc = desc.slice(0, 290).replace(/\s+[^ ]*$/, '') + '...';
    html = html.replace(/<meta\s+name=["']description["']\s+content=["'][\s\S]*?["']/i, `<meta name="description" content="${desc}">`);
  }

  // Canonical tag check
  const canonMatch = html.match(/<link\s+rel=["']canonical["']\s+href=["']([^"']+)["']/i);
  const canonUrl = canonMatch ? canonMatch[1] : '';

  // OpenGraph & Twitter tags
  if (!html.includes('property="og:title"')) {
    const ogTags = `
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:site_name" content="SJMaths">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${escapeHtml(title)}">
  <meta property="og:description" content="${escapeHtml(desc)}">
  <meta property="og:url" content="${escapeHtml(canonUrl)}">
  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${escapeHtml(title)}">
  <meta name="twitter:description" content="${escapeHtml(desc)}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">`;

    html = html.replace(/(<link\s+rel=["']canonical["'][^>]*>)/i, `$1\n${ogTags}`);
  }

  // Static SEO Question Archive Generation
  const dataMatch = html.match(/<script id="pyq-topic-data" type="application\/json">([\s\S]*?)<\/script>/);
  if (dataMatch && !html.includes('class="pyq-seo-archive"')) {
    let data;
    try {
      data = JSON.parse(dataMatch[1]);
    } catch (e) {
      console.error(`Failed to parse JSON in ${file}:`, e.message);
      continue;
    }

    const clusters = data.clusters || [];
    let pyqArticles = '';
    let drillArticles = '';

    clusters.forEach((cl, idx) => {
      if (cl.anchorPyq) {
        pyqArticles += renderQuestionArticle(cl.anchorPyq, cl.topic, idx + 1, clusters.length, false);
      }
      if (cl.conceptDrill) {
        drillArticles += renderQuestionArticle(cl.conceptDrill, cl.topic, idx + 1, clusters.length, true);
      }
    });

    const totalQs = clusters.length + (clusters[0]?.conceptDrill ? clusters.length : 0);
    const archiveHtml = `
    <!-- Complete Crawlable SEO Question Archive & Detailed Solutions -->
    <section class="pyq-seo-archive" aria-label="Official Questions and Answers Archive">
      <noscript>
        <p style="padding: 15px; background: #fff3cd; color: #856404; border-radius: 8px; margin-bottom: 20px;">
          JavaScript is currently disabled. Below is the complete archive of all ${totalQs} official UPSC Prelims questions and bilingual explanations for this topic.
        </p>
      </noscript>
      <details class="pyq-seo-details" open>
        <summary class="pyq-seo-summary">
          <span class="lang-en">Official Questions Archive &amp; Full Answer Keys (${totalQs} Questions)</span>
          <span class="lang-hi">आधिकारिक प्रश्न संग्रह एवं विस्तृत उत्तर कुंजी (${totalQs} प्रश्न)</span>
        </summary>
        <div class="pyq-seo-items-grid">
          ${pyqArticles}
          ${drillArticles}
        </div>
      </details>
    </section>
`;

    // Insert before </main>
    html = html.replace(/<\/div>\s*<\/main>/, `</div>\n${archiveHtml}    </main>`);
  }

  fs.writeFileSync(file, html, 'utf8');
  updatedCount++;
}

console.log(`Successfully enhanced ${updatedCount} topic files with SEO metadata, crawlable archives, and validated links!`);
