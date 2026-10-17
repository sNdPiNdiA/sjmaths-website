"""
template.py
HTML Template generator for UPSSSC Intermediate Level Data Interpretation topics.
Ensures 100% architectural parity, bilingual isolation, SEO perfection, and accessibility.
"""

def render_html_page(topic_data):
    slug = topic_data["slug"]
    title_en = topic_data["titleEn"]
    title_hi = topic_data["titleHi"]
    page_title = topic_data["pageTitle"]
    meta_desc = topic_data["metaDesc"]
    meta_tag_en = topic_data["metaTagEn"]
    meta_tag_hi = topic_data["metaTagHi"]
    subtitle_en = topic_data["subtitleEn"]
    subtitle_hi = topic_data["subtitleHi"]
    crumb_name_en = topic_data["crumbNameEn"]
    crumb_name_hi = topic_data["crumbNameHi"]
    
    notes_html = topic_data["notesHtml"]
    practice_questions = topic_data["practiceQuestions"]  # List of 30 dicts
    test_questions = topic_data["testQuestions"]          # List of 15 dicts
    test_data_json = topic_data["testDataJson"]          # JSON string for window.upssscTestData

    # Generate practice questions HTML (30 MCQs)
    quiz_items_html = []
    for i, q in enumerate(practice_questions, 1):
        q_tag = q.get("tag", "DI Concept")
        q_en = q["qEn"]
        q_hi = q["qHi"]
        opts = q["opts"] # List of 4 tuples: [('A', 'Text En', 'Text Hi'), ...]
        ans = q["ans"]
        sol_en = q["solEn"]
        sol_hi = q["solHi"]
        chart_html = q.get("chartHtml", "")

        opt_buttons = []
        for opt_letter, opt_en, opt_hi in opts:
            opt_buttons.append(
                f'<button class="opt-btn" onclick="checkAnswer(this, \'{ans}\', {i})">'
                f'{opt_letter}. <span class="lang-en">{opt_en}</span><span class="lang-hi">{opt_hi}</span>'
                f'</button>'
            )
        opt_grid_html = "\n".join(opt_buttons)

        quiz_items_html.append(f"""
            <!-- Question {i} -->
            <div class="question-card" id="q-{i}">
                <div class="q-meta">
                    <span class="q-num">Question {i}</span>
                    <span class="q-tag">{q_tag}</span>
                </div>
                {chart_html}
                <div class="q-text lang-en">{q_en}</div>
                <div class="q-text lang-hi">{q_hi}</div>
                <div class="options-grid">
                    {opt_grid_html}
                </div>
                <div class="solution-box" id="sol-{i}">
                    <div class="sol-badge correct"><i class="fas fa-check-circle"></i> <span class="lang-en">Correct Answer: {ans}</span><span class="lang-hi">सही उत्तर: {ans}</span></div>
                    <p class="sol-text lang-en"><strong>Explanation:</strong> {sol_en}</p>
                    <p class="sol-text lang-hi"><strong>व्याख्या:</strong> {sol_hi}</p>
                </div>
            </div>""")

    all_quiz_html = "\n".join(quiz_items_html)

    # Generate mini test questions HTML (15 MCQs)
    test_items_html = []
    for i, tq in enumerate(test_questions):
        idx = i # 0-indexed
        q_num = i + 1
        tq_en = tq["qEn"]
        tq_hi = tq["qHi"]
        opts = tq["opts"]
        chart_html = tq.get("chartHtml", "")

        tq_opt_labels = []
        for opt_letter, opt_en, opt_hi in opts:
            tq_opt_labels.append(
                f'<label class="tq-opt-label">'
                f'<input type="radio" name="tq_ans_{idx}" value="{opt_letter}"> '
                f'{opt_letter}. <span class="lang-en">{opt_en}</span><span class="lang-hi">{opt_hi}</span>'
                f'</label>'
            )
        tq_opts_html = "\n".join(tq_opt_labels)

        test_items_html.append(f"""
            <!-- Test Q{q_num} -->
            <div class="test-q-box" id="tq-{idx}">
                <div class="tq-header">
                    <span class="tq-number">{q_num} / 15</span>
                    <span class="tq-weight">1 Mark</span>
                </div>
                {chart_html}
                <div class="tq-stem lang-en">{tq_en}</div>
                <div class="tq-stem lang-hi">{tq_hi}</div>
                <div class="tq-options">
                    {tq_opts_html}
                </div>
            </div>""")

    all_test_html = "\n".join(test_items_html)

    canonical_url = f"https://sjmaths.com/upsssc-intermediate-level/data-interpretation/{slug}/"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{page_title}</title>
<meta content="{meta_desc}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="{canonical_url}" rel="canonical"/>
<meta content="{title_en} | UPSSSC Mains" property="og:title"/>
<meta content="{meta_desc}" property="og:description"/>
<meta content="{canonical_url}" property="og:url"/>
<meta content="article" property="og:type"/>
<meta content="SJMaths" property="og:site_name"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{title_en} | UPSSSC Mains" name="twitter:title"/>
<meta content="{meta_desc}" name="twitter:description"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" name="twitter:image"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Instant Theme & Language Initialization (Prevents FOUC & Double Text) -->
<script>
(function() {{
  try {{
    var p = localStorage.getItem('sjmaths.theme.preference') || 
            (localStorage.getItem('sjmaths-dark') === 'on' ? 'dark' : 
            (localStorage.getItem('theme') || 'system'));
    var d = p === 'dark' || (p === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    if (d) {{
      document.documentElement.classList.add('dark-mode');
      document.documentElement.setAttribute('data-theme', 'dark');
      document.documentElement.style.colorScheme = 'dark';
    }}

    var lang = localStorage.getItem('sjmaths_preferred_language') || localStorage.getItem('sj_pref_lang') || 'en';
    if (lang === 'hi') {{
      document.documentElement.classList.add('lang-hi', 'lang-mode-hi');
      document.documentElement.classList.remove('lang-en');
      document.documentElement.lang = 'hi';
    }} else {{
      document.documentElement.classList.add('lang-en');
      document.documentElement.classList.remove('lang-hi', 'lang-mode-hi');
      document.documentElement.lang = 'en';
    }}
  }} catch(e) {{}}
}})();
</script>

<!-- Fonts & Icons -->
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400..700;1,9..40,400..700&amp;family=Outfit:wght@400..800&amp;display=swap" rel="stylesheet"/>
<link as="style" crossorigin="anonymous" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript>
<link href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" rel="stylesheet"/>
</noscript>

<!-- Stylesheets -->
<link href="/assets/css/main.min.css?v=e4c665a0" rel="stylesheet"/>
<link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
<link href="/assets/css/component.min.css?v=85dbb37c" rel="stylesheet"/>

<!-- Schema.org Data -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Article",
      "headline": "{title_en} - UPSSSC Mains",
      "description": "{meta_desc}",
      "url": "{canonical_url}",
      "inLanguage": ["en", "hi"],
      "publisher": {{
        "@type": "Organization",
        "name": "SJMaths",
        "url": "https://sjmaths.com"
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" }},
        {{ "@type": "ListItem", "position": 2, "name": "UPSSSC Intermediate Level", "item": "https://sjmaths.com/upsssc-intermediate-level/" }},
        {{ "@type": "ListItem", "position": 3, "name": "Data Interpretation", "item": "https://sjmaths.com/upsssc-intermediate-level/#subj-di" }},
        {{ "@type": "ListItem", "position": 4, "name": "{crumb_name_en}", "item": "{canonical_url}" }}
      ]
    }}
  ]
}}
</script>

<link href="/assets/css/upsssc-intermediate.min.css?v=91ebe014" rel="stylesheet"/>
</head>
<body class="exam-ui">
<div id="header-container"></div>
<main class="topic-page-container" id="main-content">

<!-- Top Bar: Breadcrumbs & Dedicated Bilingual Language Toggle -->
<div class="page-top-bar">
    <div class="breadcrumbs-path">
        <a href="/"><i class="fas fa-home"></i> <span class="lang-en">Home</span><span class="lang-hi">होम</span></a>
        <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-intermediate-level/"><span class="lang-en">UPSSSC Intermediate Level</span><span class="lang-hi">यूपीएसएसएससी इंटरमीडिएट स्तर</span></a>
        <i class="fas fa-chevron-right"></i>
        <a href="/upsssc-intermediate-level/#subj-di"><span class="lang-en">Data Interpretation</span><span class="lang-hi">डाटा इंटरप्रिटेशन</span></a>
        <i class="fas fa-chevron-right"></i>
        <span class="lang-en">{crumb_name_en}</span>
        <span class="lang-hi">{crumb_name_hi}</span>
    </div>

    <!-- On-Page Language Toggle Button -->
    <button class="lang-toggle-pill" id="pageLangToggle" onclick="toggleLanguageMode()" aria-label="Switch Language / भाषा बदलें">
        <i class="fas fa-language" style="color: #0284c7;"></i>
        <span class="lang-en">हिंदी में पढ़ें</span>
        <span class="lang-hi">Read in English</span>
    </button>
</div>

<!-- Header -->
<div class="topic-header">
    <div class="topic-meta-tag">
        <span class="lang-en">{meta_tag_en}</span>
        <span class="lang-hi">{meta_tag_hi}</span>
    </div>
    <h1>
        <span class="lang-en">{title_en}</span>
        <span class="lang-hi">{title_hi}</span>
    </h1>
    <p class="topic-subtitle">
        <span class="lang-en">{subtitle_en}</span>
        <span class="lang-hi">{subtitle_hi}</span>
    </p>
</div>

<!-- Tabs Navigation -->
<div class="topic-tabs-bar">
    <button class="topic-tab-btn active" onclick="switchTopicTab('notes')">
        <i class="fas fa-book-open"></i>
        <span class="lang-en">Pointwise Notes</span>
        <span class="lang-hi">बिंदुवार नोट्स</span>
    </button>
    <button class="topic-tab-btn" onclick="switchTopicTab('quiz')">
        <i class="fas fa-question-circle"></i>
        <span class="lang-en">30 Practice MCQs</span>
        <span class="lang-hi">30 अभ्यास प्रश्न</span>
    </button>
    <button class="topic-tab-btn" onclick="switchTopicTab('test')">
        <i class="fas fa-stopwatch"></i>
        <span class="lang-en">15-Q Mini Test</span>
        <span class="lang-hi">15 प्रश्न मिनी टेस्ट</span>
    </button>
</div>

<!-- Tab 1: Pointwise Revision Notes -->
<div class="topic-tab-pane active" id="pane-notes">
    <div class="study-notes-wrapper">
        {notes_html}
    </div>
</div>

<!-- Tab 2: 30 Revision MCQs -->
<div class="topic-tab-pane" id="pane-quiz">
    <div class="quiz-interactive-container">
        <div class="quiz-header-banner">
            <div>
                <h2>
                    <span class="lang-en">{title_en}: 30 High-Yield Practice MCQs</span>
                    <span class="lang-hi">{title_hi}: 30 महत्वपूर्ण अभ्यास प्रश्न</span>
                </h2>
                <p>
                    <span class="lang-en">Curated from UPSSSC, UPPSC, PET, and competitive exams with complete step-by-step mathematical solutions. Click any option to verify your answer instantly.</span>
                    <span class="lang-hi">यूपीएसएसएससी, पीईटी एवं प्रतियोगी परीक्षाओं के पैटर्न पर आधारित विस्तृत गणितीय हल सहित प्रश्न। तुरंत उत्तर एवं हल देखने के लिए किसी भी विकल्प पर क्लिक करें।</span>
                </p>
            </div>
        </div>

        <div class="questions-list">
            {all_quiz_html}
        </div>
    </div>
</div>

<!-- Tab 3: 15-Q Mini Test -->
<div class="topic-tab-pane" id="pane-test">
    <div class="test-interface-container">
        <div class="test-top-bar">
            <div class="test-info-meta">
                <h3>
                    <span class="lang-en">Micro Test: {crumb_name_en}</span>
                    <span class="lang-hi">माइक्रो टेस्ट: {crumb_name_hi}</span>
                </h3>
                <p>
                    <span class="lang-en">15 Questions | 15 Minutes | 1 Mark per Question | Negative Marking: 0.25</span>
                    <span class="lang-hi">15 प्रश्न | 15 मिनट | प्रति प्रश्न 1 अंक | नकारात्मक अंकन: 0.25</span>
                </p>
            </div>
            <div class="test-timer-badge">
                <i class="fas fa-clock"></i>
                <span id="testTimer">15:00</span>
            </div>
        </div>

        <div class="test-questions-flow" id="testQuestionsContainer">
            {all_test_html}

            <!-- Submit Button Area -->
            <div class="test-actions-bar">
                <button class="test-submit-btn" onclick="submitMiniTest()">
                    <i class="fas fa-paper-plane"></i>
                    <span class="lang-en">Submit Mini Test &amp; View Result</span>
                    <span class="lang-hi">मिनी टेस्ट सबमिट करें व परिणाम देखें</span>
                </button>
            </div>

            <!-- Result Scorecard Container -->
            <div class="test-scorecard" id="testScorecard" style="display: none;">
                <div class="scorecard-header">
                    <div class="score-circle">
                        <span id="scoreValue">0</span>
                        <small>/ 15</small>
                    </div>
                    <div class="score-details">
                        <h4 id="scoreFeedback">Test Completed!</h4>
                        <p id="scoreBreakdown">Correct: 0 | Incorrect: 0 | Unattempted: 15</p>
                    </div>
                </div>
                <div class="scorecard-actions">
                    <button class="review-btn" onclick="reviewTestAnswers()">
                        <i class="fas fa-eye"></i>
                        <span class="lang-en">Review Answers &amp; Explanations</span>
                        <span class="lang-hi">उत्तर एवं व्याख्या देखें</span>
                    </button>
                    <button class="retake-btn" onclick="resetMiniTest()">
                        <i class="fas fa-redo"></i>
                        <span class="lang-en">Retake Test</span>
                        <span class="lang-hi">पुनः टेस्ट दें</span>
                    </button>
                </div>
            </div>

        </div>
    </div>
</div>

</main>
<div id="footer-container"></div>

<script>
// Test Data Configuration
window.upssscTestData = {test_data_json};
</script>

<!-- JS Scripts -->
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=b47d6b04"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=36197f29"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-footer.min.js?v=ea62137b"></script>
<script defer src="/assets/js/upsssc-intermediate.min.js?v=a2f3fc07"></script>
<script defer src="/assets/js/mobile-tab-dock.min.js?v=71d1adf2-mobile-tab-dock-v7"></script>
</body>
</html>
"""
