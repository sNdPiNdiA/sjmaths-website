const fs = require('fs');
const path = require('path');

const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const MCQS_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'mcqs');
const BIMONTHLY_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'bimonthly');

function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

function getISTDateString(date) {
  const tzOffset = 5.5 * 60 * 60 * 1000;
  const istTime = date.getTime() + date.getTimezoneOffset() * 60000 + tzOffset;
  const istDate = new Date(istTime);
  const yyyy = istDate.getFullYear();
  const mm = String(istDate.getMonth() + 1).padStart(2, '0');
  const dd = String(istDate.getDate()).padStart(2, '0');
  return `${yyyy}-${mm}-${dd}`;
}

function getBimonthlyId(date) {
  const yyyy = date.getFullYear();
  const mm = String(date.getMonth() + 1).padStart(2, '0');
  const dd = date.getDate();
  const half = dd <= 15 ? 'h1' : 'h2';
  return `${yyyy}-${mm}-${half}`;
}

const UI_TRANSLATIONS = {
  'home': { hi: 'मुख्य पृष्ठ', en: 'Home' },
  'current_affairs': { hi: 'समसामयिकी', en: 'Current Affairs' },
  'bimonthly_summaries': { hi: 'द्विमासिक सारांश', en: 'Bimonthly Summaries' },
  'bimonthly_digest_title': { hi: 'द्विमासिक समसामयिकी डाइजेस्ट', en: 'Bimonthly Current Affairs Digest' },
  'bimonthly_desc': { hi: '१५ दिवसीय समेकित संशोधन कैप्सूल और सारांश:', en: 'Consolidated fortnightly revision summaries for the period:' },
  'bimonthly_mcqs': { hi: 'द्विमासिक अभ्यास प्रश्न', en: 'Bimonthly Practice MCQs' },
  'bimonthly_capsules': { hi: 'द्विमासिक रिवीजन कैप्सूल', en: 'Bimonthly Revision Capsules' },
  'explanation': { hi: 'स्पष्टीकरण', en: 'Explanation' },

  'test_your_knowledge': { hi: 'अपने ज्ञान का परीक्षण करें', en: 'Test Your Knowledge' },
  'no_highlights': { hi: 'इस अवधि के लिए कोई समाचार अपडेट नहीं मिला।', en: 'No news updates found for this period.' },
  'no_mcqs': { hi: 'इस अवधि के लिए कोई अभ्यास प्रश्न नहीं मिला।', en: 'No practice questions compiled for this period.' }
};

const CATEGORY_NAMES = {
  'national': { hi: 'राष्ट्रीय मामले', en: 'National Affairs' },
  'international': { hi: 'अंतरराष्ट्रीय मामले', en: 'International Affairs' },
  'economy': { hi: 'अर्थव्यवस्था', en: 'Economy' },
  'banking': { hi: 'बैंकिंग और वित्त', en: 'Banking & Finance' },
  'science': { hi: 'विज्ञान और प्रौद्योगिकी', en: 'Science & Tech' },
  'defence': { hi: 'रक्षा', en: 'Defence' },
  'environment': { hi: 'पर्यावरण', en: 'Environment' },
  'sports': { hi: 'खेलकूद', en: 'Sports' },
  'awards': { hi: 'पुरस्कार और सम्मान', en: 'Awards & Honors' },
  'government_schemes': { hi: 'सरकारी योजनाएं', en: 'Government Schemes' },
  'appointments': { hi: 'नियुक्तियां', en: 'Appointments' },
  'state_news': { hi: 'राज्य समाचार', en: 'State News' }
};

const CATEGORY_ICONS = {
  'national': 'fas fa-flag',
  'international': 'fas fa-globe',
  'economy': 'fas fa-coins',
  'banking': 'fas fa-university',
  'science': 'fas fa-microscope',
  'defence': 'fas fa-shield-alt',
  'environment': 'fas fa-leaf',
  'sports': 'fas fa-trophy',
  'awards': 'fas fa-award',
  'government_schemes': 'fas fa-hand-holding-heart',
  'appointments': 'fas fa-user-tie',
  'state_news': 'fas fa-map-marked-alt'
};

function t(key, defaultVal = '') {
  if (CATEGORY_NAMES[key]) {
    return `<span class="lang-hi">${CATEGORY_NAMES[key].hi}</span><span class="lang-en">${CATEGORY_NAMES[key].en}</span>`;
  }
  const item = UI_TRANSLATIONS[key];
  if (!item) return defaultVal;
  return `<span class="lang-hi">${item.hi}</span><span class="lang-en">${item.en}</span>`;
}

function getBreadcrumbsAndToggle(breadcrumbsHTML) {
  return `
    <div class="ca-top-bar" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 1.5rem; width: 100%;">
      <div class="breadcrumbs" style="margin-bottom: 0;">
        ${breadcrumbsHTML}
      </div>
      <div class="ca-lang-toggle notranslate" id="ca-lang-toggle" style="margin-bottom: 0;">
        <div class="ca-lang-option" data-lang="hi">हिंदी</div>
        <div class="ca-lang-option" data-lang="en">English</div>
      </div>
    </div>
  `;
}

function getHTMLTemplate(title, description, canonicalUrl, contentHTML) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} | SJMaths</title>
    <meta name="description" content="${description}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="${canonicalUrl}">
    <link rel="icon" type="image/png" href="/favicon.png">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css">
    <link rel="stylesheet" href="/assets/css/layout.min.css">
    <link rel="stylesheet" href="/assets/css/component.min.css">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css">
    <link rel="stylesheet" href="/assets/css/pages.min.css">
    <link rel="stylesheet" href="/assets/css/current-affairs.min.css">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- FontAwesome -->
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css" onload="this.onload=null;this.rel='stylesheet'">
    <noscript>
        <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css">
    </noscript>
</head>
<body>
    <div id="header-container"></div>
    <main class="ca-container" id="main-content">
        ${contentHTML}
    </main>
    <div id="footer-container"></div>
    <script src="/assets/js/main.min.js" defer></script>
    <script src="/assets/js/global-header.min.js" defer></script>
    <script src="/assets/js/global-footer.min.js" defer></script>
    <script src="/assets/js/current-affairs-lang.min.js" defer></script>
    <script src="/assets/js/current-affairs.min.js" defer></script>
</body>
</html>`;
}

function main() {
  console.log('Generating Bimonthly Current Affairs Digests...');
  
  if (!fs.existsSync(PROCESSED_DIR)) {
    console.log('Processed directory does not exist.');
    return;
  }

  const files = fs.readdirSync(PROCESSED_DIR).filter(file => file.endsWith('.json') && /^\d{4}-\d{2}-\d{2}\.json$/.test(file));
  if (files.length === 0) {
    console.log('No processed data files found.');
    return;
  }

  // Load and group dates by bimonthly ID
  const bimonthGroups = {};
  files.forEach(file => {
    const dateStr = file.replace('.json', '');
    const date = new Date(dateStr);
    const bimonthId = getBimonthlyId(date);

    if (!bimonthGroups[bimonthId]) {
      bimonthGroups[bimonthId] = [];
    }
    bimonthGroups[bimonthId].push(dateStr);
  });

  ensureDir(BIMONTHLY_DIR);

  Object.keys(bimonthGroups).forEach(bimonthId => {
    const dateStrings = bimonthGroups[bimonthId];
    const newsItems = [];
    const mcqItems = [];

    // Collect all news and MCQs for this period
    dateStrings.forEach(dateStr => {
      const processedPath = path.join(PROCESSED_DIR, `${dateStr}.json`);
      const mcqPath = path.join(MCQS_DIR, `${dateStr}.json`);

      if (fs.existsSync(processedPath)) {
        try {
          newsItems.push(...JSON.parse(fs.readFileSync(processedPath, 'utf8')));
        } catch (err) {
          console.error(`Error reading ${processedPath}:`, err.message);
        }
      }

      if (fs.existsSync(mcqPath)) {
        try {
          mcqItems.push(...JSON.parse(fs.readFileSync(mcqPath, 'utf8')));
        } catch (err) {
          console.error(`Error reading ${mcqPath}:`, err.message);
        }
      }
    });

    if (newsItems.length === 0) return;

    // Group bimonthly news topic-wise
    const categorizedNews = {};
    newsItems.forEach(item => {
      item.categories.forEach(cat => {
        if (!CATEGORY_NAMES[cat]) return;
        if (!categorizedNews[cat]) {
          categorizedNews[cat] = [];
        }
        if (!categorizedNews[cat].some(existing => existing.id === item.id)) {
          categorizedNews[cat].push(item);
        }
      });
    });

    let categoryCompilationsHTML = '';
    const activeCats = Object.keys(categorizedNews).sort();

    activeCats.forEach(cat => {
      const articles = categorizedNews[cat];
      const itemsHTML = articles.map(item => {
        const hasDesc = item.description && item.description.trim().length > 0;
        const descHTML = hasDesc ? `<p class="ca-card-desc" style="font-size: 0.95rem; color: var(--text-light); line-height: 1.6; margin-top: 0.5rem; margin-bottom: 0.5rem;">${item.description}</p>` : '';
        const sourceText = item.source && item.source !== 'Merged Current Affairs' ? `<span style="margin-right: 1rem;"><i class="fas fa-newspaper" style="color: var(--primary); opacity: 0.8; margin-right: 0.3rem;"></i>${item.source}</span>` : '';
        const dateText = `<span><i class="far fa-calendar-alt" style="color: var(--primary); opacity: 0.8; margin-right: 0.3rem;"></i>${item.pubDate.split('T')[0]}</span>`;
        return `
          <div class="ca-card" data-categories="${item.categories.join(',')}" style="margin-bottom: 1.5rem; padding: 1.6rem; border-radius: 1rem; border-left: 4px solid var(--primary); background: var(--glass); box-shadow: var(--shadow-sm);">
            <h4 class="ca-card-title" style="font-family: 'Outfit', sans-serif; font-size: 1.25rem; font-weight: 700; color: var(--text-dark); line-height: 1.45; margin: 0;">${item.title}</h4>
            ${descHTML}
            <div style="margin-top: 0.8rem; display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: var(--text-light); font-weight: 500;">
              ${sourceText}${dateText}
            </div>
          </div>
        `;
      }).join('');

      const icon = CATEGORY_ICONS[cat] || 'fas fa-chevron-circle-right';
      categoryCompilationsHTML += `
        <div class="ca-category-section" data-category="${cat}">
          <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.4rem; color: var(--primary); margin: 2rem 0 1rem 0; border-bottom: 1px solid rgba(142,68,173,0.1); padding-bottom: 0.4rem;">
            <i class="${icon}"></i> ${t(cat)}
          </h3>
          <div>${itemsHTML}</div>
        </div>
      `;
    });

    // Topic-wise notes download links removed for bimonthly period

    // Generate Bimonthly MCQs (top 20)
    const mcqsHTML = mcqItems.slice(0, 20).map((q, idx) => `
      <div class="ca-mcq-card" data-correct="${q.correctAnswer}" style="margin-bottom: 1.5rem; padding: 1.5rem; border-radius: 1rem;">
        <div class="ca-mcq-question" style="font-size: 1.1rem;">Q${idx + 1}. ${q.question}</div>
        <div class="ca-mcq-options" style="margin-top: 1rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.8rem;">
          ${q.options.map((opt, optIdx) => `
            <div class="ca-mcq-option" data-index="${optIdx}" style="display: flex; align-items: center; gap: 0.8rem; padding: 0.85rem 1.15rem; font-size: 0.95rem; border-radius: 0.75rem; border: 1px solid rgba(0,0,0,0.1); background: rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
              <div class="ca-mcq-option-letter" style="display: flex; justify-content: center; align-items: center; width: 28px; height: 28px; font-size: 0.8rem; font-weight: 700; background: rgba(142,68,173,0.1); color: var(--primary); border-radius: 50%; flex-shrink: 0;">${String.fromCharCode(65 + optIdx)}</div>
              <div style="flex: 1; line-height: 1.4;">${opt}</div>
            </div>
          `).join('')}
        </div>
        <div class="ca-mcq-explanation" style="display: none; padding: 1rem; font-size: 0.88rem; margin-top: 1rem;">
          <div class="ca-mcq-explanation-title"><i class="fas fa-info-circle"></i> ${t('explanation', 'Explanation')}</div>
          <p>${q.explanation}</p>
        </div>
      </div>
    `).join('');

    const contentHTML = `
      ${getBreadcrumbsAndToggle(`
        <a href="/">${t('home', 'Home')}</a> &gt; 
        <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
        <a href="/current-affairs/bimonthly/">${t('bimonthly_summaries', 'Bimonthly Summaries')}</a> &gt; 
        <span>${bimonthId}</span>
      `)}
      
      <div class="ca-header" style="text-align: left; margin-bottom: 3rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem;">
          <div>
            <h1 style="font-size: 2.2rem; background: linear-gradient(135deg, var(--primary), #e74c3c); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">${t('bimonthly_digest_title', 'Bimonthly Current Affairs Digest')}</h1>
            <p style="margin-top: 0.3rem;">${t('bimonthly_desc', 'Consolidated fortnightly summaries for the period:')} ${bimonthId}</p>
          </div>
        </div>
      </div>


      <!-- Category compilations -->
      <div style="background: rgba(142,68,173,0.02); border: 1px solid rgba(142,68,173,0.1); border-radius: 1.25rem; padding: 2rem; margin-bottom: 3rem;">
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.6rem; color: var(--text-dark); margin-bottom: 1.5rem;"><i class="far fa-list-alt"></i> ${t('bimonthly_capsules', 'Bimonthly Revision Capsules')}</h2>
        ${categoryCompilationsHTML || `<p style="text-align: center; color: var(--text-light);">${t('no_highlights', 'No updates compiled for this period.')}</p>`}
      </div>

      <!-- MCQs -->
      <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.6rem; color: var(--primary); margin: 3rem 0 1.5rem 0; border-bottom: 2px solid rgba(142,68,173,0.1); padding-bottom: 0.5rem;"><i class="fas fa-check-double"></i> ${t('bimonthly_mcqs', 'Bimonthly Practice MCQs')}</h2>
      <div class="ca-news-list">
        ${mcqsHTML || `<p style="text-align: center; color: var(--text-light);">${t('no_mcqs', 'No practice questions compiled for this period.')}</p>`}
      </div>
    `;

    const html = getHTMLTemplate(
      `Bimonthly Current Affairs Digest — ${bimonthId}`,
      `Bimonthly current affairs digest and compiled revision capsules for period ${bimonthId}. Free fortnightly general awareness updates and practice MCQs.`,
      `https://sjmaths.com/current-affairs/bimonthly/${bimonthId}/`,
      contentHTML
    );

    ensureDir(path.join(BIMONTHLY_DIR, bimonthId));
    fs.writeFileSync(path.join(BIMONTHLY_DIR, bimonthId, 'index.html'), html, 'utf8');
    console.log(`Generated bimonthly digest: ${bimonthId}`);
  });
}

main();
