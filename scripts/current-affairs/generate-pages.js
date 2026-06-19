const fs = require('fs');
const path = require('path');

const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const EXAM_MAP_PATH = path.join(__dirname, 'config', 'exam-mapping.json');
const OUTPUT_DIR = path.join(__dirname, '..', '..', 'current-affairs');

const PRIMARY_CATEGORIES = [
  'national',
  'international',
  'economy',
  'banking',
  'science',
  'defence',
  'environment',
  'sports',
  'awards',
  'government_schemes',
  'appointments',
  'state_news'
];

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


// Helper to create directory recursively if not exists
function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
}

// Get year and week number (e.g. 2026-w22)
function getYearWeek(date) {
  const target = new Date(date.valueOf());
  const dayNr = (date.getDay() + 6) % 7; // Monday is day 0
  target.setDate(target.getDate() - dayNr + 3);
  const firstThursday = target.valueOf();
  target.setMonth(0, 1);
  if (target.getDay() !== 4) {
    target.setMonth(0, 1 + ((4 - target.getDay()) + 7) % 7);
  }
  const weekNum = 1 + Math.ceil((firstThursday - target) / 604800000);
  const year = target.getFullYear();
  return `${year}-w${String(weekNum).padStart(2, '0')}`;
}

// Get bimonthly period ID (e.g. 2026-06-h1 or 2026-06-h2)
function getBimonthlyId(date) {
  const yyyy = date.getFullYear();
  const mm = String(date.getMonth() + 1).padStart(2, '0');
  const dd = date.getDate();
  const half = dd <= 15 ? 'h1' : 'h2';
  return `${yyyy}-${mm}-${half}`;
}

// Get month ID (e.g. 2026-06)
function getMonthId(date) {
  const yyyy = date.getFullYear();
  const mm = String(date.getMonth() + 1).padStart(2, '0');
  return `${yyyy}-${mm}`;
}


// Translations dictionary
const UI_TRANSLATIONS = {
  'home': { hi: 'मुख्य पृष्ठ', en: 'Home' },
  'current_affairs': { hi: 'समसामयिकी', en: 'Current Affairs' },
  'daily_archive': { hi: 'दैनिक संग्रह', en: 'Daily Archive' },
  'daily_quiz': { hi: 'दैनिक क्विज़', en: 'Daily Quiz' },
  'mcq_practice': { hi: 'बहुविकल्पीय प्रश्न अभ्यास', en: 'MCQ Practice' },
  'monthly_summaries': { hi: 'मासिक सारांश', en: 'Monthly Summaries' },
  'weekly_revision_notes': { hi: 'साप्ताहिक रिवीजन नोट्स', en: 'Weekly Revision Notes' },
  'monthly_summaries': { hi: 'मासिक सारांश', en: 'Monthly Summaries' },
  'daily_current_affairs': { hi: 'दैनिक समसामयिकी', en: 'Daily Current Affairs' },
  'daily_desc': { hi: 'प्रतियोगी परीक्षाओं के लिए विस्तृत समाचार अपडेट, दिनांक', en: 'Comprehensive news updates for competitive exams, compiled on' },
  'previous_day': { hi: 'पिछला दिन', en: 'Previous Day' },
  'next_day': { hi: 'अगला दिन', en: 'Next Day' },
  'test_your_knowledge': { hi: 'अपने ज्ञान का परीक्षण करें', en: 'Test Your Knowledge' },
  'attempt_quiz_desc': { hi: 'आज के समाचार अपडेट पर आधारित इंटरेटिव बहुविकल्पीय प्रश्नोत्तरी का प्रयास करें।', en: "Attempt the interactive MCQ quiz based on today's news updates." },
  'start_quiz': { hi: 'आज की प्रश्नोत्तरी शुरू करें', en: "Start Today's Quiz" },
  'archive_desc': { hi: 'विस्तृत दैनिक समाचार अपडेट और अभ्यास बहुविकल्पीय प्रश्नों को देखने के लिए एक तिथि चुनें।', en: 'Select a date to view comprehensive daily news updates and practice MCQs' },
  'hub_title': { hi: 'समसामयिकी हब', en: 'Current Affairs Hub' },
  'hub_desc': { hi: 'प्रतियोगी परीक्षाओं की तैयारी के लिए स्वचालित समसामयिकी मंच। दैनिक समाचार, परीक्षा-विशेष हाइलाइट्स, डाउनलोड करने योग्य मासिक पत्रिकाएं और इंटरेटिव क्विज़।', en: 'Automated current affairs platform for competitive exam preparation. Daily news, exam-specific highlights, monthly summaries, and interactive quizzes.' },
  'weekly_notes': { hi: 'साप्ताहिक नोट्स', en: 'Weekly Notes' },
  'monthly_summaries': { hi: 'मासिक सारांश', en: 'Monthly Summaries' },
  'syllabus_exam_channels': { hi: 'पाठ्यक्रम के अनुसार परीक्षा चैनल', en: 'Syllabus-wise Exam Channels' },
  'todays_highlights': { hi: 'आज के मुख्य समाचार', en: "Today's News Highlights" },
  'view_full_archive': { hi: 'पूर्ण दैनिक संग्रह देखें', en: 'View Full Daily Archive' },
  'mcq_hub_title': { hi: 'दैनिक बहुविकल्पीय प्रश्न अभ्यास हब', en: 'Daily MCQ Practice Hub' },
  'mcq_hub_desc': { hi: 'दैनिक रिवीजन बहुविकल्पीय प्रश्नों का अभ्यास करने और स्पष्टीकरण कैप्सूल की समीक्षा करने के लिए एक तिथि चुनें।', en: 'Select a date to practice daily revision MCQs and review explanation capsules.' },
  'notes_title': { hi: 'मासिक समसामयिकी सारांश', en: 'Monthly Current Affairs Summaries' },
  'notes_desc': { hi: 'मासिक समसामयिकी संशोधन सारांश पढ़ें और श्रेणी-वार तैयारी करें।', en: 'Read monthly current affairs revision summaries and prepare category-wise.' },
  'weekly_title': { hi: 'साप्ताहिक समसामयिकी सारांश', en: 'Weekly Current Affairs Digests' },
  'weekly_desc': { hi: 'साप्ताहिक समेकित संशोधन कैप्सूल और सारांश ब्राउज़ करें। सप्ताहांत पाठ्यक्रम संशोधन के लिए आदर्श।', en: 'Browse weekly consolidated revision capsules and summaries. Ideal for weekend syllabus revisions.' },
  'monthly_title': { hi: 'मासिक समसामयिकी सारांश', en: 'Monthly Summaries' },
  'monthly_desc': { hi: 'विस्तृत मासिक समसामयिकी संकलन और श्रेणी-वार विश्लेषण पढ़ें।', en: 'Read detailed monthly current affairs compilations and category-wise analysis.' },
  'about': { hi: 'हमारे बारे में', en: 'About' },
  'contact': { hi: 'संपर्क करें', en: 'Contact' },
  'privacy': { hi: 'गोपनीयता नीति', en: 'Privacy Policy' },
  'terms': { hi: 'नियम व शर्तें', en: 'Terms' },
  'sitemap': { hi: 'साइटमैप', en: 'Sitemap' },
  'all_rights_reserved': { hi: 'सर्वाधिकार सुरक्षित।', en: 'All Rights Reserved.' },
  'categories_syllabus': { hi: 'कवर किए गए पाठ्यक्रम श्रेणियां:', en: 'Covered Syllabus Categories:' },
  'latest_updates': { hi: 'नवीनतम अपडेट', en: 'Latest Updates' },
  'articles_in_last_30_days': { hi: 'पिछले 30 दिनों में लेख', en: 'articles in last 30 days' },
  'no_recent_updates': { hi: 'इस परीक्षा के लिए कोई हालिया अपडेट नहीं मिला। जल्द ही दोबारा जांचें!', en: 'No recent updates found for this exam. Check back soon!' },
  'exam_prep': { hi: 'परीक्षा तैयारी', en: 'Exam prep' },
  'custom_updates_mcqs': { hi: 'कस्टम पाठ्यक्रम अपडेट और बहुविकल्पीय प्रश्न।', en: 'Custom syllabus updates & MCQs.' },
  'explore': { hi: 'एक्सप्लोर करें', en: 'Explore' },
  'june_magazine': { hi: 'जून 2026 मासिक पत्रिका', en: 'June 2026 Monthly Magazine' },
  'june_magazine_desc': { hi: 'श्रेणी सारांश, 100+ बहुविकल्पीय प्रश्न, महत्वपूर्ण दिन और राज्य-वार समाचार शामिल हैं।', en: 'Includes category summaries, 100+ MCQs, important days, and state-wise news.' },
  'format_notes': { hi: 'प्रारूप: ऑनलाइन सारांश', en: 'Format: online summary' },
  'download': { hi: 'डाउनलोड करें', en: 'Download' },
  'weekly_digest_desc': { hi: 'जून 1 से जून 7, 2026 तक समेकित संशोधन कैप्सूल।', en: 'Consolidated revision capsules from June 1 to June 7, 2026.' },
  'read_digest': { hi: 'डाइजेस्ट पढ़ें', en: 'Read Digest' },
  'monthly_digest_desc': { hi: 'त्वरित पढ़ने के लिए वर्गीकृत पूर्ण मासिक सारांश।', en: 'Full monthly summary categorized for quick reading.' },
  'read_summary': { hi: 'सारांश पढ़ें', en: 'Read Summary' },
  'daily_capsules_desc': { hi: 'दैनिक समाचार कैप्सूल और संशोधन प्रश्न', en: 'Daily news capsule & revision questions' },
  'no_daily_archives': { hi: 'अभी तक कोई दैनिक संग्रह उपलब्ध नहीं है।', en: 'No daily archives available yet.' },
  'no_highlights': { hi: 'कोई हालिया समाचार हाइलाइट उपलब्ध नहीं हैं।', en: 'No recent news highlights available.' },
  'keywords': { hi: 'कीवर्ड:', en: 'Keywords:' },
  'highlight': { hi: 'मुख्य आकर्षण', en: 'Highlight' },
  
  // Exams
  'exam_ssc-cgl': { hi: 'एसएससी सीजीएल', en: 'SSC CGL' },
  'exam_ssc-chsl': { hi: 'एसएससी सीएचएसएल', en: 'SSC CHSL' },
  'exam_ssc-mts': { hi: 'एसएससी एमटीएस', en: 'SSC MTS' },
  'exam_railway': { hi: 'रेलवे परीक्षा', en: 'Railway Exams' },
  'exam_roaro': { hi: 'आरओ/एआरओ', en: 'RO/ARO' },
  'exam_uppcs': { hi: 'यूपीपीसीएस', en: 'UPPCS' },
  'exam_upsc': { hi: 'यूपीएससी', en: 'UPSC' },

  // Exam Descriptions
  'exam_desc_ssc-cgl': { hi: 'विशेष रूप से एसएससी सीजीएल परीक्षा के लिए अनुकूलित दैनिक अपडेट, नियुक्तियां, पुरस्कार और खेलकूद समाचार।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for SSC CGL.' },
  'exam_desc_ssc-chsl': { hi: 'एसएससी सीएचएसएल के लिए नवीनतम नियुक्तियां, पुरस्कार, खेलकूद और महत्वपूर्ण राष्ट्रीय समसामयिकी समाचार।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for SSC CHSL.' },
  'exam_desc_ssc-mts': { hi: 'एसएससी एमटीएस सामान्य जागरूकता के लिए महत्वपूर्ण दैनिक समाचार और समसामयिकी अपडेट।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for SSC MTS.' },
  'exam_desc_railway': { hi: 'आरआरबी एनटीपीसी और ग्रुप डी सामान्य जागरूकता परीक्षा की तैयारी के लिए लक्षित समसामयिकी।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for Railway.' },
  'exam_desc_roaro': { hi: 'समीक्षा अधिकारी (RO/ARO) प्रारंभिक और मुख्य परीक्षा के लिए विशेष रूप से तैयार की गई दैनिक राष्ट्रीय-अंतरराष्ट्रीय घटनाएं।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for RO/ARO.' },
  'exam_desc_uppcs': { hi: 'यूपीपीसीएस प्रारंभिक परीक्षा के लिए विशेष उत्तर प्रदेश राज्य विशिष्ट समाचार और दैनिक समसामयिकी।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for UPPCS.' },
  'exam_desc_upsc': { hi: 'यूपीएससी सिविल सेवा परीक्षा (IAS/IPS) के लिए दैनिक विश्लेषणात्मक समाचार सारांश और महत्वपूर्ण सरकारी रिपोर्ट।', en: 'Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for UPSC.' },

  // Categories
  'cat_national': { hi: 'राष्ट्रीय मामले', en: 'National Affairs' },
  'cat_international': { hi: 'अंतरराष्ट्रीय मामले', en: 'International Affairs' },
  'cat_economy': { hi: 'अर्थव्यवस्था', en: 'Economy' },
  'cat_banking': { hi: 'बैंकिंग और वित्त', en: 'Banking & Finance' },
  'cat_science': { hi: 'विज्ञान और प्रौद्योगिकी', en: 'Science & Tech' },
  'cat_defence': { hi: 'रक्षा', en: 'Defence' },
  'cat_environment': { hi: 'पर्यावरण', en: 'Environment' },
  'cat_sports': { hi: 'खेलकूद', en: 'Sports' },
  'cat_awards': { hi: 'पुरस्कार और सम्मान', en: 'Awards & Honors' },
  'cat_books_and_authors': { hi: 'पुस्तकें और लेखक', en: 'Books & Authors' },
  'cat_appointments': { hi: 'नियुक्तियां', en: 'Appointments' },
  'cat_government_schemes': { hi: 'सरकारी योजनाएं', en: 'Government Schemes' },
  'cat_state_news': { hi: 'राज्य समाचार', en: 'State News' },
  'cat_places_in_news': { hi: 'चर्चित स्थल', en: 'Places in News' },
  'cat_committees': { hi: 'समितियां', en: 'Committees' },
  'cat_reports_indices': { hi: 'रिपोर्ट और सूचकांक', en: 'Reports & Indices' },
  'cat_important_days': { hi: 'महत्वपूर्ण दिवस', en: 'Important Days' },
  'cat_miscellaneous': { hi: 'विविध', en: 'Miscellaneous' },
  'explore_by_topics': { hi: 'विषयवार खोजें', en: 'Explore by Topics' },
  'exam_prep_channels': { hi: 'परीक्षा-वार तैयारी चैनल', en: 'Explore Exam Channels' },
  'bimonthly_summaries': { hi: 'द्विमासिक सारांश', en: 'Bimonthly Summaries' },


  'bimonthly_title': { hi: 'द्विमासिक समसामयिकी सारांश', en: 'Bimonthly Current Affairs Digests' },
  'bimonthly_desc': { hi: 'द्विमासिक (१५ दिवसीय) समेकित संशोधन कैप्सूल और सारांश ब्राउज़ करें।', en: 'Browse fortnightly (15-day) consolidated revision capsules and summaries.' },
  'bimonthly_digest_desc': { hi: '१५ दिनों का समेकित संशोधन कैप्सूल।', en: 'Consolidated revision capsules for the 15-day period.' },
  'read_bimonthly': { hi: 'द्विमासिक पढ़ें', en: 'Read Digest' },
  'topic_title': { hi: 'विषयवार समसामयिकी', en: 'Topic-wise Current Affairs' },
  'topic_desc': { hi: 'इस विषय के लिए संकलित साप्ताहिक, द्विमासिक और मासिक समाचार कैप्सूल एवं रिवीजन नोट्स।', en: 'Compiled weekly, bimonthly, and monthly news capsules and revision notes for this topic.' },
  'weekly_compilation': { hi: 'साप्ताहिक संकलन', en: 'Weekly Compilations' },
  'bimonthly_compilation': { hi: 'द्विमासिक संकलन', en: 'Bimonthly Compilations' },
  'monthly_compilation': { hi: 'मासिक संकलन', en: 'Monthly Compilations' }
};

function t(key, defaultVal = '') {
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

// Header/Footer boilerplate wrapper matching SJMaths site structure
function getHTMLTemplate(title, description, canonicalUrl, contentHTML, isQuiz = false) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} | SJMaths</title>
    <meta name="description" content="${description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
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

    <!-- Structured Data: Breadcrumbs -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://sjmaths.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Current Affairs",
          "item": "https://sjmaths.com/current-affairs/"
        }
      ]
    }
    </script>
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
    ${isQuiz ? '<script src="/assets/js/current-affairs-quiz.min.js" defer></script>' : '<script src="/assets/js/current-affairs.min.js" defer></script>'}
</body>
</html>`;
}

// Generate a card HTML for an article
function generateArticleCard(item) {
  const badgeHTML = item.categories.map(cat => `<span class="ca-badge ca-badge-category">${t('cat_' + cat, cat.replace('_', ' '))}</span>`).join('') +
                    (item.examTags || []).map(exam => `<span class="ca-badge ca-badge-exam">${t('exam_' + exam, exam.toUpperCase())}</span>`).join('');
  
  const importanceBadge = item.importance === 'high' ? `<span class="ca-badge ca-badge-importance-high"><i class="fas fa-star"></i> ${t('highlight', 'Highlight')}</span>` : '';
  const dateFormatted = new Date(item.pubDate).toLocaleDateString('en-IN', {
    day: 'numeric',
    month: 'short',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });

  const imageHTML = item.imageUrl ? `<img src="${item.imageUrl}" alt="${item.title}" class="ca-card-image" loading="lazy">` : '';
  const hasDesc = item.description && item.description.trim().length > 0;
  const descHTML = hasDesc ? `<p class="ca-card-desc">${item.description}</p>` : '';
  const sourceHTML = item.source && item.source !== 'Merged Current Affairs' ? `<span class="ca-card-source"><i class="fas fa-newspaper"></i> ${item.source}</span>` : '';

  return `
    <article class="ca-card" data-categories="${item.categories.join(',')}" data-exams="${(item.examTags || []).join(',')}">
      <div class="ca-card-meta">
        ${sourceHTML}
        <span><i class="far fa-calendar-alt" style="margin-right: 0.3rem;"></i>${dateFormatted}</span>
      </div>
      <h3 class="ca-card-title" style="line-height: 1.45; font-size: 1.4rem;">${item.title}</h3>
      ${imageHTML}
      ${descHTML}
      <div class="ca-card-badges">
        ${importanceBadge}
        ${badgeHTML}
      </div>
      <div style="margin-top: 0.6rem; font-size: 0.8rem; color: var(--text-light); font-weight: 500;">
        <strong>${t('keywords', 'Keywords:')}</strong> ${item.keywords.join(', ')}
      </div>
    </article>
  `;
}

// 1. Generate Daily Pages (static detailed view for a day)
function generateDailyPages(allData) {
  const dates = Object.keys(allData).sort((a, b) => new Date(b) - new Date(a));
  
  dates.forEach((dateStr, idx) => {
    const items = allData[dateStr];
    ensureDir(path.join(OUTPUT_DIR, 'daily', dateStr));

    const prevDate = dates[idx + 1] ? dates[idx + 1] : null;
    const nextDate = dates[idx - 1] ? dates[idx - 1] : null;

    const navHTML = `
      <div class="ca-date-nav">
        ${prevDate ? `<a href="../${prevDate}/" class="ca-date-btn"><i class="fas fa-arrow-left"></i> ${t('previous_day', 'Previous Day')} (${prevDate})</a>` : `<span class="ca-date-btn disabled"><i class="fas fa-arrow-left"></i> ${t('previous_day', 'Previous')}</span>`}
        <span class="ca-current-date-label"><i class="far fa-calendar-alt"></i> ${new Date(dateStr).toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' })}</span>
        ${nextDate ? `<a href="../${nextDate}/" class="ca-date-btn">${t('next_day', 'Next Day')} (${nextDate}) <i class="fas fa-arrow-right"></i></a>` : `<span class="ca-date-btn disabled">${t('next_day', 'Next')} <i class="fas fa-arrow-right"></i></span>`}
      </div>
    `;

    const categoryGroups = {};
    items.forEach(item => {
      const primaryCat = item.categories[0] || 'national';
      if (!categoryGroups[primaryCat]) {
        categoryGroups[primaryCat] = [];
      }
      categoryGroups[primaryCat].push(item);
    });

    let contentHTML = `
      ${getBreadcrumbsAndToggle(`
        <a href="/">${t('home', 'Home')}</a> &gt; 
        <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
        <a href="/current-affairs/daily/">${t('daily_archive', 'Daily Archive')}</a> &gt; 
        <span>${dateStr}</span>
      `)}
      <div class="ca-header">
        <h1>${t('daily_current_affairs', 'Daily Current Affairs')}</h1>
        <p>${t('daily_desc', 'Comprehensive news updates for competitive exams, compiled on')} ${dateStr}</p>
      </div>
      ${navHTML}
      <div class="ca-news-list">
    `;

    // Render grouped by category
    Object.keys(categoryGroups).sort().forEach(cat => {
      contentHTML += `
        <h2 style="font-family: 'Outfit', sans-serif; margin: 2rem 0 1rem 0; font-size: 1.8rem; color: var(--primary); text-transform: capitalize; border-bottom: 2px solid rgba(142,68,173,0.1); padding-bottom: 0.5rem;">
          <i class="fas fa-folder-open"></i> ${t('cat_' + cat, cat.replace('_', ' ') + ' Affairs')}
        </h2>
      `;
      categoryGroups[cat].forEach(item => {
        contentHTML += generateArticleCard(item);
      });
    });

    contentHTML += `
      </div>
      <div style="text-align: center; margin: 3rem 0; padding: 2rem; background: var(--glass); border-radius: 1.25rem; box-shadow: var(--shadow-md); border: 1px solid rgba(142,68,173,0.1);">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem; color: var(--text-dark);">${t('test_your_knowledge', 'Test Your Knowledge')}</h3>
        <p style="color: var(--text-light); margin-bottom: 1.5rem;">${t('attempt_quiz_desc', "Attempt the interactive MCQ quiz based on today's news updates.")}</p>
        <a href="/current-affairs/quiz/?date=${dateStr}" class="btn nav-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.8rem 2rem; border-radius: 50px;">
          <i class="fas fa-play"></i> ${t('start_quiz', "Start Today's Quiz")}
        </a>
      </div>
    `;

    const html = getHTMLTemplate(
      `Daily Current Affairs for ${dateStr}`,
      `Read the latest daily current affairs for ${dateStr}. Daily updated study material, news analysis, and current events for SSC CGL, Railway, UPSC, and State PSCs.`,
      `https://sjmaths.com/current-affairs/daily/${dateStr}/`,
      contentHTML
    );

    fs.writeFileSync(path.join(OUTPUT_DIR, 'daily', dateStr, 'index.html'), html, 'utf8');
  });
}

// 2. Generate Daily Archive page listing all dates
function generateDailyArchive(dates) {
  ensureDir(path.join(OUTPUT_DIR, 'daily'));

  const dateListHTML = dates.map(date => {
    return `
      <a href="./${date}/" class="stat-card" style="text-align: left; display: flex; align-items: center; justify-content: space-between; padding: 1.2rem 1.5rem; text-decoration: none; color: inherit;">
        <div>
          <span style="font-weight: 700; font-size: 1.1rem; color: var(--text-dark); display: block;"><i class="far fa-calendar-check"></i> ${date}</span>
          <span style="font-size: 0.85rem; color: var(--text-light);">${t('daily_capsules_desc', 'Daily news capsule & revision questions')}</span>
        </div>
        <i class="fas fa-arrow-right" style="color: var(--primary);"></i>
      </a>
    `;
  }).join('');

  const contentHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; 
      <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
      <span>${t('daily_archive', 'Daily Archive')}</span>
    `)}
    <div class="ca-header">
      <h1>${t('daily_current_affairs', 'Daily Current Affairs Archive')}</h1>
      <p>${t('archive_desc', 'Select a date to view comprehensive daily news updates and practice MCQs')}</p>
    </div>
    <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 2rem;">
      ${dateListHTML || `<p style="grid-column: 1/-1; text-align: center; color: var(--text-light);">${t('no_daily_archives', 'No daily archives available yet.')}</p>`}
    </div>
  `;

  const html = getHTMLTemplate(
    'Daily Current Affairs Archive',
    'Browse the full archive of daily current affairs. Get daily news updates, revision capsules, and competitive exam summaries.',
    'https://sjmaths.com/current-affairs/daily/',
    contentHTML
  );

  fs.writeFileSync(path.join(OUTPUT_DIR, 'daily', 'index.html'), html, 'utf8');
}

// 3. Generate Exam-Specific Pages
function generateExamPages(allData, exams) {
  // Aggregate articles from the last 30 days
  const allArticles = [];
  Object.keys(allData).forEach(date => {
    allArticles.push(...allData[date]);
  });

  exams.forEach(exam => {
    ensureDir(path.join(OUTPUT_DIR, exam.id));

    // Filter items subscribing to this exam
    const examArticles = allArticles.filter(item => (item.examTags || []).includes(exam.id));
    
    // Sort by publication date (newest first)
    examArticles.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));

    // Group by Date
    const groupedByDate = {};
    examArticles.forEach(item => {
      const dateOnly = item.pubDate.split('T')[0];
      if (!groupedByDate[dateOnly]) {
        groupedByDate[dateOnly] = [];
      }
      groupedByDate[dateOnly].push(item);
    });

    let articlesHTML = '';
    const sortedDates = Object.keys(groupedByDate).sort((a, b) => new Date(b) - new Date(a));

    sortedDates.forEach(date => {
      articlesHTML += `
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; margin: 2rem 0 1rem 0; color: var(--text-dark); display: flex; align-items: center; gap: 0.5rem; border-bottom: 1px dashed rgba(0,0,0,0.1); padding-bottom: 0.3rem;">
          <i class="far fa-calendar-alt"></i> ${new Date(date).toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' })}
        </h2>
      `;
      groupedByDate[date].forEach(item => {
        articlesHTML += generateArticleCard(item);
      });
    });

    const categoriesList = exam.categories.map(cat => `<span class="ca-category-pill" style="pointer-events: none;">${t('cat_' + cat, cat.replace('_', ' '))}</span>`).join('');

    const contentHTML = `
      ${getBreadcrumbsAndToggle(`
        <a href="/">${t('home', 'Home')}</a> &gt; 
        <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
        <span>${t('exam_' + exam.id, exam.name)}</span>
      `)}
      <div class="ca-header" style="text-align: left; margin-bottom: 2rem;">
        <h1 style="font-size: 2.2rem; background: linear-gradient(135deg, var(--primary), #e74c3c); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">${t('exam_' + exam.id, exam.name)} ${t('current_affairs', 'Current Affairs')}</h1>
        <p style="margin-top: 0.5rem;">${t('exam_desc_' + exam.id, `Syllabus-focused daily updates, awards, sports, appointments, and national events filtered specifically for ${exam.name}.`)}</p>
      </div>

      <div style="margin-bottom: 2rem;">
        <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; margin-bottom: 0.75rem; color: var(--text-dark);">${t('categories_syllabus', 'Covered Syllabus Categories:')}</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
          ${categoriesList}
        </div>
      </div>

      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.6rem; color: var(--text-dark);">${t('latest_updates', 'Latest Updates')}</h2>
        <span style="font-size: 0.9rem; color: var(--text-light); font-weight: 500;" id="ca-results-count">${examArticles.length} ${t('articles_in_last_30_days', 'articles in last 30 days')}</span>
      </div>

      <div class="ca-news-list" id="ca-news-container">
        ${articlesHTML || `<p style="text-align: center; padding: 3rem; color: var(--text-light);">${t('no_recent_updates', 'No recent updates found for this exam. Check back soon!')}</p>`}
      </div>
    `;

    const html = getHTMLTemplate(
      `${exam.name} Current Affairs — Daily Updated Syllabus Material`,
      `Get syllabus-focused ${exam.name} current affairs, daily news, appointments, awards, and sports updates. Specially curated for ${exam.name} general awareness preparation.`,
      `https://sjmaths.com/current-affairs/${exam.id}/`,
      contentHTML
    );

    fs.writeFileSync(path.join(OUTPUT_DIR, exam.id, 'index.html'), html, 'utf8');
  });
}

// 4. Generate Hub Landing page
function generateHubLanding(allData, exams) {
  // Get latest 5 articles
  const allArticles = [];
  Object.keys(allData).forEach(date => {
    allArticles.push(...allData[date]);
  });
  allArticles.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));
  const latestArticles = allArticles.slice(0, 5);

  const highlightsHTML = latestArticles.map(item => generateArticleCard(item)).join('');

  // Generate topic cards HTML
  const topicCardsHTML = PRIMARY_CATEGORIES.map(cat => {
    const icon = CATEGORY_ICONS[cat] || 'fas fa-folder';
    return `
      <a href="/current-affairs/topic/${cat}/" class="ca-topic-card" style="background: white; border: 1px solid rgba(142, 68, 173, 0.12); border-radius: 0.75rem; padding: 1.25rem 1rem; text-align: center; cursor: pointer; display: flex; flex-direction: column; align-items: center; gap: 0.6rem; box-shadow: 0 2px 8px rgba(0,0,0,0.02); text-decoration: none; transition: all 0.2s ease;">
        <i class="${icon}" style="font-size: 1.5rem; color: var(--primary);"></i>
        <span style="font-family: 'Outfit', sans-serif; font-size: 0.9rem; font-weight: 600; color: var(--text-dark);">${t('cat_' + cat, cat.replace('_', ' '))}</span>
      </a>
    `;
  }).join('');

  // Generate horizontal exam list
  const examLineHTML = exams.map(exam => `
    <a href="/current-affairs/${exam.id}/" class="ca-exam-line-btn">
      <i class="fas fa-graduation-cap"></i> ${t('exam_' + exam.id, exam.name)}
    </a>
  `).join('');

  const contentHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; <span>${t('current_affairs', 'Current Affairs')}</span>
    `)}
    
    <div class="ca-header" style="margin-bottom: 3rem;">
      <h1>${t('hub_title', 'Current Affairs Hub')}</h1>
      <p>${t('hub_desc', 'Automated current affairs platform for competitive exam preparation. Daily news, exam-specific highlights, monthly summaries, and interactive quizzes.')}</p>
    </div>

    <!-- Quick Navigation Bento Grid -->
    <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 3rem;">
      <a href="/current-affairs/daily/" class="stat-card" style="background: white; border: 1px solid rgba(142,68,173,0.1); text-decoration: none;">
        <span class="stat-value"><i class="far fa-calendar-alt"></i></span>
        <span class="stat-label">${t('daily_archive', 'Daily Archive')}</span>
      </a>
      <a href="/current-affairs/quiz/" class="stat-card" style="background: white; border: 1px solid rgba(142,68,173,0.1); text-decoration: none;">
        <span class="stat-value"><i class="fas fa-vial"></i></span>
        <span class="stat-label">${t('daily_quiz', 'Daily Quiz')}</span>
      </a>
      <a href="/current-affairs/weekly/" class="stat-card" style="background: white; border: 1px solid rgba(142,68,173,0.1); text-decoration: none;">
        <span class="stat-value"><i class="fas fa-book-open"></i></span>
        <span class="stat-label">${t('weekly_notes', 'Weekly Notes')}</span>
      </a>

    </div>

    <!-- Explore by Topics Section -->
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.8rem; margin: 2rem 0 1rem 0; color: var(--text-dark);"><i class="fas fa-th-large"></i> ${t('explore_by_topics', 'Explore by Topics')}</h2>
    <div class="ca-topics-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 1rem; margin-bottom: 3rem;">
      ${topicCardsHTML}
    </div>

    <!-- Highlights and Latest Update -->
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;" id="highlights-title-row">
      <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.8rem; color: var(--text-dark);"><i class="fas fa-bolt"></i> ${t('todays_highlights', "Today's News Highlights")}</h2>
      <a href="/current-affairs/daily/" style="color: var(--primary); font-weight: 600; font-size: 0.95rem;">${t('view_full_archive', 'View Full Daily Archive')} &rarr;</a>
    </div>

    <div class="ca-news-list" id="ca-news-container">
      ${highlightsHTML || `<p style="text-align: center; color: var(--text-light); padding: 3rem;">${t('no_highlights', 'No recent news highlights available.')}</p>`}
    </div>

    <!-- Exam Wise Hub Bento Section at the very bottom -->
    <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.8rem; margin: 4rem 0 1rem 0; text-align: center; color: var(--text-dark);"><i class="fas fa-graduation-cap"></i> ${t('exam_prep_channels', 'Explore Exam Channels')}</h2>
    <div class="ca-exams-row">
      ${examLineHTML}
    </div>
  `;

  const html = getHTMLTemplate(
    'Current Affairs Hub for Competitive Exams',
    'Comprehensive automated current affairs preparation hub. Free daily news updates, MCQ quizzes, weekly summaries, and monthly notes updates for SSC, Banking, Railways, State PSC and UPSC.',
    'https://sjmaths.com/current-affairs/',
    contentHTML
  );

  fs.writeFileSync(path.join(OUTPUT_DIR, 'index.html'), html, 'utf8');
}

// 5. Generate placeholder pages for static hubs (Quiz, MCQs, notes, Weekly, Monthly)
function generateStaticHubs(allData) {
  // A. Quiz Landing
  ensureDir(path.join(OUTPUT_DIR, 'quiz'));
  const quizHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; 
      <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
      <span>${t('daily_quiz', 'Daily Quiz')}</span>
    `)}
    <div id="ca-quiz-root"></div>
  `;
  const quizPage = getHTMLTemplate(
    'Daily Interactive Current Affairs Quiz',
    'Test your daily current affairs knowledge with interactive timed quizzes. Get detailed explanations and track your preparation scores for competitive exams.',
    'https://sjmaths.com/current-affairs/quiz/',
    quizHTML,
    true
  );
  fs.writeFileSync(path.join(OUTPUT_DIR, 'quiz', 'index.html'), quizPage, 'utf8');

  // B. MCQ Practice Landing
  ensureDir(path.join(OUTPUT_DIR, 'mcq'));
  const mcqHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; 
      <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
      <span>${t('mcq_practice', 'MCQ Practice')}</span>
    `)}
    <div class="ca-header">
      <h1>${t('mcq_hub_title', 'Daily MCQ Practice Hub')}</h1>
      <p>${t('mcq_hub_desc', 'Select a date to practice daily revision MCQs and review explanation capsules.')}</p>
    </div>
    <div id="ca-mcq-dates-root" class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin-top: 2rem;">
      <!-- Populated via client-side js or static list -->
      <div style="grid-column: 1/-1; text-align: center; padding: 3rem; color: var(--text-light);">
        <i class="fas fa-spinner fa-spin fa-2x" style="color: var(--primary); margin-bottom: 1rem;"></i>
        <p>Loading available practice dates...</p>
      </div>
    </div>

    <script>
      document.addEventListener('DOMContentLoaded', async () => {
        const root = document.getElementById('ca-mcq-dates-root');
        const today = new Date();
        const tzOffset = 5.5 * 60 * 60 * 1000;
        const listHTML = [];
        const isHi = document.body.classList.contains('lang-hi');
        const label = isHi ? '10+ प्रश्नों का अभ्यास करें' : 'Practice 10+ Questions';
        
        for (let i = 0; i < 14; i++) {
          const target = new Date(today.getTime() + today.getTimezoneOffset() * 60000 + tzOffset - (i * 24 * 60 * 60 * 1000));
          const yyyy = target.getFullYear();
          const mm = String(target.getMonth() + 1).padStart(2, '0');
          const dd = String(target.getDate()).padStart(2, '0');
          const dateStr = yyyy + '-' + mm + '-' + dd;
          
          listHTML.push(
            '<a href="/current-affairs/quiz/?date=' + dateStr + '" class="stat-card" style="text-align: left; text-decoration: none; border: 1px solid rgba(142,68,173,0.1); background: white;">' +
              '<span class="stat-value" style="font-size: 1.3rem; margin-bottom: 0.2rem;"><i class="fas fa-clipboard-check"></i> ' + dateStr + '</span>' +
              '<span class="stat-label" style="font-size: 0.75rem;">' + label + '</span>' +
            '</a>'
          );
        }
        root.innerHTML = listHTML.join('');
      });
    </script>
  `;
  const mcqPage = getHTMLTemplate(
    'Daily Current Affairs MCQ Practice Hub',
    'Practice daily syllabus current affairs questions with four options, instant evaluation feedback, and descriptive answer explanations.',
    'https://sjmaths.com/current-affairs/mcq/',
    mcqHTML
  );
  fs.writeFileSync(path.join(OUTPUT_DIR, 'mcq', 'index.html'), mcqPage, 'utf8');

  // Extract unique periods from allData keys
  const dates = Object.keys(allData).sort((a, b) => new Date(b) - new Date(a));
  const uniqueMonths = [...new Set(dates.map(d => getMonthId(new Date(d))))].sort().reverse();
  const uniqueBimonths = [...new Set(dates.map(d => getBimonthlyId(new Date(d))))].sort().reverse();
  const uniqueWeeks = [...new Set(dates.map(d => getYearWeek(new Date(d))))].sort().reverse();

  // Helper to map date strings for specific periods
  const getDatesForMonth = (mId) => dates.filter(d => getMonthId(new Date(d)) === mId);
  const getDatesForBimonth = (bId) => dates.filter(d => getBimonthlyId(new Date(d)) === bId);
  const getDatesForWeek = (wId) => dates.filter(d => getYearWeek(new Date(d)) === wId);

  // D. Weekly Digest Landing Index
  ensureDir(path.join(OUTPUT_DIR, 'weekly'));
  const weeklyListHTML = uniqueWeeks.map(weekId => {
    return `
      <div class="stat-card" style="text-align: left; padding: 1.5rem; background: white; border: 1px solid rgba(142,68,173,0.1);">
        <span class="stat-value" style="font-size: 1.4rem; margin-bottom: 0.5rem;"><i class="fas fa-calendar-week"></i> ${weekId}</span>
        <p style="font-size: 0.85rem; color: var(--text-light); margin-bottom: 1rem;">${t('weekly_digest_desc', 'Consolidated revision capsules for the week.')} (${weekId})</p>
        <a href="./${weekId}/" style="color: var(--primary); font-weight: 700; font-size: 0.85rem;">${t('read_digest', 'Read Digest')} &rarr;</a>
      </div>
    `;
  }).join('');

  const weeklyHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; 
      <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
      <span>${t('weekly_revision_notes', 'Weekly Revision Notes')}</span>
    `)}
    <div class="ca-header">
      <h1>${t('weekly_title', 'Weekly Current Affairs Digests')}</h1>
      <p>${t('weekly_desc', 'Browse weekly consolidated revision capsules and summaries. Ideal for weekend syllabus revisions.')}</p>
    </div>
    <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
      ${weeklyListHTML || `<p style="grid-column: 1/-1; text-align: center; color: var(--text-light);">${t('no_highlights', 'No weekly digests available yet.')}</p>`}
    </div>
  `;
  const weeklyPage = getHTMLTemplate(
    'Weekly Current Affairs Digest & Revision Capsules',
    'Weekly consolidated current affairs capsules and revision digests for quick weekly exam revision and general awareness syllabus cover.',
    'https://sjmaths.com/current-affairs/weekly/',
    weeklyHTML
  );
  fs.writeFileSync(path.join(OUTPUT_DIR, 'weekly', 'index.html'), weeklyPage, 'utf8');

  // E. Monthly Digest Landing Index
  ensureDir(path.join(OUTPUT_DIR, 'monthly'));
  const monthlyListHTML = uniqueMonths.map(monthId => {
    return `
      <div class="stat-card" style="text-align: left; padding: 1.5rem; background: white; border: 1px solid rgba(142,68,173,0.1);">
        <span class="stat-value" style="font-size: 1.4rem; margin-bottom: 0.5rem;"><i class="far fa-calendar-alt"></i> ${monthId}</span>
        <p style="font-size: 0.85rem; color: var(--text-light); margin-bottom: 1rem;">${t('monthly_digest_desc', 'Full monthly summary categorized for quick reading.')} (${monthId})</p>
        <a href="./${monthId}/" style="color: var(--primary); font-weight: 700; font-size: 0.85rem;">${t('read_summary', 'Read Summary')} &rarr;</a>
      </div>
    `;
  }).join('');

  const monthlyHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; 
      <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
      <span>${t('monthly_summaries', 'Monthly Summaries')}</span>
    `)}
    <div class="ca-header">
      <h1>${t('monthly_title', 'Monthly Current Affairs Summaries')}</h1>
      <p>${t('monthly_desc', 'Read detailed monthly current affairs compilations and category-wise analysis.')}</p>
    </div>
    <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
      ${monthlyListHTML || `<p style="grid-column: 1/-1; text-align: center; color: var(--text-light);">${t('no_highlights', 'No monthly summaries available yet.')}</p>`}
    </div>
  `;
  const monthlyPage = getHTMLTemplate(
    'Monthly Current Affairs Summaries & Analysis',
    'Browse full monthly current affairs summary capsules and detailed analysis tables for general awareness prep.',
    'https://sjmaths.com/current-affairs/monthly/',
    monthlyHTML
  );
  fs.writeFileSync(path.join(OUTPUT_DIR, 'monthly', 'index.html'), monthlyPage, 'utf8');

  // F. Bimonthly Digest Landing Index
  ensureDir(path.join(OUTPUT_DIR, 'bimonthly'));
  const bimonthlyListHTML = uniqueBimonths.map(bimonthId => {
    return `
      <div class="stat-card" style="text-align: left; padding: 1.5rem; background: white; border: 1px solid rgba(142,68,173,0.1);">
        <span class="stat-value" style="font-size: 1.4rem; margin-bottom: 0.5rem;"><i class="fas fa-history"></i> ${bimonthId}</span>
        <p style="font-size: 0.85rem; color: var(--text-light); margin-bottom: 1rem;">${t('bimonthly_digest_desc', 'Fortnightly 15-day consolidated revision capsules.')} (${bimonthId})</p>
        <a href="./${bimonthId}/" style="color: var(--primary); font-weight: 700; font-size: 0.85rem;">${t('read_bimonthly', 'Read Digest')} &rarr;</a>
      </div>
    `;
  }).join('');

  const bimonthlyHTML = `
    ${getBreadcrumbsAndToggle(`
      <a href="/">${t('home', 'Home')}</a> &gt; 
      <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
      <span>${t('bimonthly_summaries', 'Bimonthly Summaries')}</span>
    `)}
    <div class="ca-header">
      <h1>${t('bimonthly_title', 'Bimonthly Current Affairs Digests')}</h1>
      <p>${t('bimonthly_desc', 'Browse fortnightly (15-day) consolidated revision capsules and summaries.')}</p>
    </div>
    <div class="stats-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
      ${bimonthlyListHTML || `<p style="grid-column: 1/-1; text-align: center; color: var(--text-light);">${t('no_highlights', 'No bimonthly summaries available yet.')}</p>`}
    </div>
  `;
  const bimonthlyPage = getHTMLTemplate(
    'Bimonthly Current Affairs Digests & Fortnightly Summaries',
    'Fortnightly current affairs digests and revision summaries compiled for competitive exam general awareness revisions.',
    'https://sjmaths.com/current-affairs/bimonthly/',
    bimonthlyHTML
  );
  fs.writeFileSync(path.join(OUTPUT_DIR, 'bimonthly', 'index.html'), bimonthlyPage, 'utf8');
}

// 6. Generate Dedicated Topic Landing Pages compiling weekly, bimonthly, monthly updates with download links
// 6. Generate Dedicated Topic Landing Pages compiling weekly, bimonthly, monthly updates with download links
function generateTopicPages(allData) {
  PRIMARY_CATEGORIES.forEach(category => {
    ensureDir(path.join(OUTPUT_DIR, 'topic', category));

    // Group dates by periods
    const weeks = {};
    const bimonths = {};
    const months = {};

    Object.keys(allData).forEach(dateStr => {
      const items = allData[dateStr].filter(item => item.categories.includes(category));
      if (items.length === 0) return;

      const date = new Date(dateStr);
      const weekId = getYearWeek(date);
      const bimonthId = getBimonthlyId(date);
      const monthId = getMonthId(date);

      if (!weeks[weekId]) weeks[weekId] = [];
      weeks[weekId].push(...items);

      if (!bimonths[bimonthId]) bimonths[bimonthId] = [];
      bimonths[bimonthId].push(...items);

      if (!months[monthId]) months[monthId] = [];
      months[monthId].push(...items);
    });

    const monthListHTML = Object.keys(months).sort().reverse().map(monthId => {
      const count = months[monthId].length;
      return `
        <div style="border-bottom: 1px solid rgba(142,68,173,0.1); padding: 1rem 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <span style="font-weight: 700; font-size: 1.1rem; color: var(--text-dark);"><i class="far fa-calendar-alt"></i> ${monthId}</span>
            <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 0.2rem;">${count} articles compiled for ${t('cat_' + category, category)}.</p>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <a href="/current-affairs/monthly/${monthId}/" class="btn nav-btn" style="padding: 8px 16px; border-radius: 50px; font-size: 0.85rem;">View Monthly Page</a>

          </div>
        </div>
      `;
    }).join('');

    const bimonthListHTML = Object.keys(bimonths).sort().reverse().map(bimonthId => {
      const count = bimonths[bimonthId].length;
      return `
        <div style="border-bottom: 1px solid rgba(142,68,173,0.1); padding: 1rem 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <span style="font-weight: 700; font-size: 1.1rem; color: var(--text-dark);"><i class="fas fa-history"></i> ${bimonthId}</span>
            <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 0.2rem;">${count} articles compiled for ${t('cat_' + category, category)}.</p>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <a href="/current-affairs/bimonthly/${bimonthId}/" class="btn nav-btn" style="padding: 8px 16px; border-radius: 50px; font-size: 0.85rem;">View Bimonthly Page</a>
          </div>
        </div>
      `;
    }).join('');

    // Separate latest week from previous weeks
    const sortedWeekIds = Object.keys(weeks).sort().reverse();
    let latestWeekHTML = '';
    let previousWeeksHTML = '';

    if (sortedWeekIds.length > 0) {
      const latestWeekId = sortedWeekIds[0];
      const articlesCardsHTML = weeks[latestWeekId].map(item => generateArticleCard(item)).join('');
      latestWeekHTML = `
        <div class="ca-card" style="padding: 2rem; margin-bottom: 2.5rem; display: flex; flex-direction: column;">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(142,68,173,0.1); padding-bottom: 0.8rem; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem; width: 100%;">
            <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; color: var(--primary); margin: 0;"><i class="fas fa-calendar-week"></i> Latest Week's Articles (${latestWeekId})</h2>
            <div style="display: flex; gap: 0.5rem;">
              <a href="/current-affairs/weekly/${latestWeekId}/" class="btn nav-btn" style="padding: 8px 18px; border-radius: 50px; font-size: 0.85rem;">View Week Page</a>
            </div>
          </div>
          <div class="ca-news-list">
            ${articlesCardsHTML}
          </div>
        </div>
      `;

      // Previous weeks
      const previousWeekIds = sortedWeekIds.slice(1);
      previousWeeksHTML = previousWeekIds.map(weekId => {
        const count = weeks[weekId].length;
        return `
          <div style="border-bottom: 1px solid rgba(142,68,173,0.1); padding: 1rem 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
            <div>
              <span style="font-weight: 700; font-size: 1.1rem; color: var(--text-dark);"><i class="fas fa-calendar-week"></i> ${weekId}</span>
              <p style="font-size: 0.85rem; color: var(--text-light); margin-top: 0.2rem;">${count} articles compiled for ${t('cat_' + category, category)}.</p>
            </div>
            <div style="display: flex; gap: 0.5rem;">
              <a href="/current-affairs/weekly/${weekId}/" class="btn nav-btn" style="padding: 8px 16px; border-radius: 50px; font-size: 0.85rem;">View Weekly Page</a>
            </div>
          </div>
        `;
      }).join('');
    }

    const icon = CATEGORY_ICONS[category] || 'fas fa-folder';

    const contentHTML = `
      ${getBreadcrumbsAndToggle(`
        <a href="/">${t('home', 'Home')}</a> &gt; 
        <a href="/current-affairs/">${t('current_affairs', 'Current Affairs')}</a> &gt; 
        <span>${t('cat_' + category, category)}</span>
      `)}
      
      <div class="ca-header" style="margin-bottom: 3rem;">
        <h1><i class="${icon}"></i> ${t('cat_' + category, category)}</h1>
        <p>${t('topic_desc', 'Compiled weekly, bimonthly, and monthly news capsules and revision notes for this topic.')}</p>
      </div>

      <!-- Latest Week's Articles -->
      ${latestWeekHTML || `<p style="color: var(--text-light); text-align: center; padding: 2rem;">No recent weekly articles available for this topic.</p>`}

      <div style="display: grid; grid-template-columns: 1fr; gap: 2rem; margin-bottom: 3rem;">
        <!-- Monthly Compilations Card -->
        <div class="ca-card" style="padding: 2rem;">
          <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; color: var(--primary); margin-bottom: 1.5rem; border-bottom: 2px solid rgba(142,68,173,0.1); padding-bottom: 0.5rem;"><i class="far fa-calendar-alt"></i> ${t('monthly_compilation', 'Monthly Compilations')}</h2>
          ${monthListHTML || `<p style="color: var(--text-light); text-align: center; padding: 2rem;">No monthly compilations available for this topic yet.</p>`}
        </div>

        <!-- Bimonthly Compilations Card -->
        <div class="ca-card" style="padding: 2rem;">
          <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; color: var(--primary); margin-bottom: 1.5rem; border-bottom: 2px solid rgba(142,68,173,0.1); padding-bottom: 0.5rem;"><i class="fas fa-history"></i> ${t('bimonthly_compilation', 'Bimonthly Compilations')}</h2>
          ${bimonthListHTML || `<p style="color: var(--text-light); text-align: center; padding: 2rem;">No bimonthly compilations available for this topic yet.</p>`}
        </div>

        <!-- Previous Weekly Compilations Card -->
        ${previousWeeksHTML ? `
        <div class="ca-card" style="padding: 2rem;">
          <h2 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; color: var(--primary); margin-bottom: 1.5rem; border-bottom: 2px solid rgba(142,68,173,0.1); padding-bottom: 0.5rem;"><i class="fas fa-calendar-week"></i> Previous Weekly Compilations</h2>
          ${previousWeeksHTML}
        </div>
        ` : ''}
      </div>
    `;

    const html = getHTMLTemplate(
      `${category.replace('_', ' ').replace(/\b\w/g, c => c.toUpperCase())} Current Affairs — Weekly, Bimonthly, Monthly Compilations`,
      `Read topic-wise current affairs for ${category.replace('_', ' ')}. Free weekly notes, fortnightly bimonthly digests, and monthly magazines.`,
      `https://sjmaths.com/current-affairs/topic/${category}/`,
      contentHTML
    );

    fs.writeFileSync(path.join(OUTPUT_DIR, 'topic', category, 'index.html'), html, 'utf8');
  });
}

function main() {
  console.log('Generating SJMaths Current Affairs HTML pages...');
  
  if (!fs.existsSync(EXAM_MAP_PATH)) {
    console.error('Exam mapping config file not found at:', EXAM_MAP_PATH);
    process.exit(1);
  }

  const { exams } = JSON.parse(fs.readFileSync(EXAM_MAP_PATH, 'utf8'));
  ensureDir(OUTPUT_DIR);

  // Load all processed data
  let allData = {};
  if (fs.existsSync(PROCESSED_DIR)) {
    const files = fs.readdirSync(PROCESSED_DIR);
    files.forEach(file => {
      if (file.endsWith('.json') && /^\d{4}-\d{2}-\d{2}\.json$/.test(file)) {
        const dateStr = file.replace('.json', '');
        const filePath = path.join(PROCESSED_DIR, file);
        try {
          allData[dateStr] = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        } catch (err) {
          console.error(`Error loading processed file ${filePath}:`, err.message);
        }
      }
    });
  }

  const dates = Object.keys(allData).sort((a, b) => new Date(b) - new Date(a));
  console.log(`Loaded ${dates.length} dates from processed folder.`);

  // Generate page types
  generateDailyPages(allData);
  generateDailyArchive(dates);
  generateExamPages(allData, exams);
  generateHubLanding(allData, exams);
  generateStaticHubs(allData);
  generateTopicPages(allData);

  console.log('Static site generation for Current Affairs completed successfully!');
}

main();
