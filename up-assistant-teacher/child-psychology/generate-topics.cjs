/**
 * Generator: Creates individual microtopic pages for Child Psychology
 * with tabbed structure: Concepts/Theories (Tab 1), Practice Questions (Tab 2),
 * Mini Test (Tab 3), Revision (Tab 4).
 * 
 * For now, generates Tab 1 structure with placeholders for Gemini 3.5 Flash Lite content.
 */
const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname);
const OUTPUT_DIR = path.join(BASE_DIR, 'topics');

if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

const microtopics = [
    {
        id: 'child-psychology-mt-1-1',
        title: 'Individual Differences',
        titleHi: 'वैयक्तिक भिन्नता',
        slug: 'individual-differences'
    },
    {
        id: 'child-psychology-mt-1-2',
        title: 'Factors Affecting Child Development',
        titleHi: 'बाल विकास को प्रभावित करने वाले कारक',
        slug: 'factors-affecting-child-development'
    },
    {
        id: 'child-psychology-mt-1-3',
        title: 'Identification of Learning Needs',
        titleHi: 'सीखने की आवश्यकता की पहचान',
        slug: 'identification-of-learning-needs'
    },
    {
        id: 'child-psychology-mt-1-4',
        title: 'Creating Conducive Learning Environment',
        titleHi: 'पढ़ने के लिए वातावरण का सृजन करना',
        slug: 'creating-conducive-learning-environment'
    },
    {
        id: 'child-psychology-mt-1-5',
        title: 'Learning Theories & Practical Classroom Application',
        titleHi: 'सीखने के सिद्धान्त तथा कक्षा-शिक्षण में व्यावहारिक उपयोगिता',
        slug: 'learning-theories-and-classroom-application'
    },
    {
        id: 'child-psychology-mt-1-6',
        title: 'Special Provisions for Divyang Students',
        titleHi: 'दिव्यांग छात्रों हेतु विशेष व्यवस्था',
        slug: 'special-provisions-for-divyang-students'
    }
];

function generateTopicPage(topic) {
    return `<!DOCTYPE html>
<html lang="hi">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.title} | ${topic.titleHi} - बाल मनोविज्ञान | SJMaths</title>
    <meta name="description" content="${topic.title} - Child Psychology microtopic for UP Assistant Teacher. Concepts, practice questions, mini test and revision.">
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 10px 30px -5px rgba(212, 175, 55, 0.1);
            --accent-gradient: linear-gradient(135deg, #d4af37, #2980b9);
        }
        body.dark-mode {
            --glass-bg: rgba(30, 30, 46, 0.95);
            --glass-border: rgba(255, 255, 255, 0.05);
            --shadow-lg: 0 10px 30px -5px rgba(0, 0, 0, 0.3);
        }
        .topic-container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 2.5rem 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }
        .topic-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .topic-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .topic-header p {
            font-size: 1rem;
            color: var(--text-light);
        }
        .back-link {
            display: inline-block;
            margin-bottom: 1.5rem;
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .back-link:hover {
            text-decoration: underline;
        }
        .tabs-nav {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }
        .tab-btn {
            background: transparent;
            border: none;
            outline: none;
            padding: 0.6rem 1.2rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
            color: var(--text-light);
            cursor: pointer;
            border-radius: 25px;
            transition: all 0.3s ease;
        }
        .tab-btn:hover {
            color: #d4af37;
            background: rgba(212, 175, 55, 0.05);
        }
        .tab-btn.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(212, 175, 55, 0.3);
        }
        .tab-panel {
            display: none;
            animation: slideUp 0.4s ease-out;
        }
        .tab-panel.active {
            display: block;
        }
        .content-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-lg);
        }
        .content-card h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .content-card h2 i {
            color: #d4af37;
        }
        .content-card p, .content-card li {
            font-size: 0.95rem;
            color: var(--text-light);
            line-height: 1.7;
        }
        .content-card ul {
            margin: 0.5rem 0;
            padding-left: 1.5rem;
        }
        .content-card li {
            margin-bottom: 0.5rem;
        }
        .highlight-box {
            background: rgba(212, 175, 55, 0.08);
            border-left: 4px solid #d4af37;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        .highlight-box strong {
            color: #d4af37;
        }
        .mnemonic-box {
            background: rgba(46, 204, 113, 0.08);
            border-left: 4px solid #2ecc71;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        .mnemonic-box strong {
            color: #2ecc71;
        }
        .tips-box {
            background: rgba(52, 152, 219, 0.08);
            border-left: 4px solid #3498db;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        .tips-box strong {
            color: #3498db;
        }
        .mistakes-box {
            background: rgba(231, 76, 60, 0.08);
            border-left: 4px solid #e74c3c;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
        }
        .mistakes-box strong {
            color: #e74c3c;
        }
        .placeholder-note {
            background: rgba(155, 89, 182, 0.08);
            border: 1px dashed rgba(155, 89, 182, 0.3);
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            text-align: center;
            color: #9b59b6;
            font-size: 0.9rem;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>

<body>
    <div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <a href="/up-assistant-teacher/child-psychology/" class="back-link"><i class="fas fa-arrow-left"></i> <span class="lang-hi">वापस बाल मनोविज्ञान पर जाएँ</span><span class="lang-en">Back to Child Psychology</span></a>

        <div class="topic-header">
            <h1>
                <span class="lang-hi">${topic.titleHi}</span>
                <span class="lang-en">${topic.title}</span>
            </h1>
            <p>
                <span class="lang-hi">बाल मनोविज्ञान - अवधारणाएँ और सिद्धान्त</span>
                <span class="lang-en">Child Psychology - Concepts and Theories</span>
            </p>
        </div>

        <!-- Tabs Navigation -->
        <div class="tabs-nav">
            <button class="tab-btn active" data-target="concepts">
                <i class="fas fa-lightbulb"></i>
                <span class="lang-hi">अवधारणाएँ</span>
                <span class="lang-en">Concepts</span>
            </button>
            <button class="tab-btn" data-target="practice">
                <i class="fas fa-pen"></i>
                <span class="lang-hi">अभ्यास प्रश्न</span>
                <span class="lang-en">Practice Questions</span>
            </button>
            <button class="tab-btn" data-target="test">
                <i class="fas fa-clock"></i>
                <span class="lang-hi">मिनी टेस्ट</span>
                <span class="lang-en">Mini Test</span>
            </button>
            <button class="tab-btn" data-target="revision">
                <i class="fas fa-redo"></i>
                <span class="lang-hi">पुनरावृत्ति</span>
                <span class="lang-en">Revision</span>
            </button>
        </div>

        <!-- Tab 1: Concepts & Theories -->
        <div class="tab-panel active" id="panel-concepts">
            <!-- Overview -->
            <div class="content-card">
                <h2><i class="fas fa-eye"></i> <span class="lang-hi">अवलोकन</span><span class="lang-en">Overview</span></h2>
                <div class="placeholder-note">
                    <i class="fas fa-robot"></i> 
                    <strong>Gemini 3.5 Flash Lite Generated Content</strong><br>
                    <span class="lang-hi">यह खंड AI द्वारा जनरेट किया जा रहा है...</span><br>
                    <span class="lang-en">This section will be populated by AI...</span>
                </div>
            </div>

            <!-- Detailed Explanation -->
            <div class="content-card">
                <h2><i class="fas fa-book"></i> <span class="lang-hi">विस्तृत व्याख्या</span><span class="lang-en">Detailed Explanation</span></h2>
                <div class="placeholder-note">
                    <i class="fas fa-robot"></i> 
                    <strong>Gemini 3.5 Flash Lite Generated Content</strong><br>
                    <span class="lang-hi">विस्तृत व्याख्या AI द्वारा जनरेट की जा रही है...</span><br>
                    <span class="lang-en">Detailed explanation will be generated by AI...</span>
                </div>
            </div>

            <!-- Mnemonics -->
            <div class="content-card">
                <h2><i class="fas fa-magic"></i> <span class="lang-hi">स्मृति सहायक (मnémonic)</span><span class="lang-en">Mnemonics</span></h2>
                <div class="mnemonic-box">
                    <strong>💡 Mnemonic:</strong> <span class="lang-hi">(जनरेट किया जा रहा है...)</span><br>
                    <span class="lang-en">(Being generated...)</span>
                </div>
            </div>

            <!-- Tips & Tricks -->
            <div class="content-card">
                <h2><i class="fas fa-star"></i> <span class="lang-hi">सुझाव और ट्रिक्स</span><span class="lang-en">Tips & Tricks</span></h2>
                <div class="tips-box">
                    <strong>✓ Tip:</strong> <span class="lang-hi">(जनरेट किया जा रहा है...)</span><br>
                    <span class="lang-en">(Being generated...)</span>
                </div>
            </div>

            <!-- Mistakes to Avoid -->
            <div class="content-card">
                <h2><i class="fas fa-exclamation-triangle"></i> <span class="lang-hi">ऐसे गलतियाँ न करें</span><span class="lang-en">Mistakes to Avoid</span></h2>
                <div class="mistakes-box">
                    <strong>⚠ Common Mistake:</strong> <span class="lang-hi">(जनरेट किया जा रहा है...)</span><br>
                    <span class="lang-en">(Being generated...)</span>
                </div>
            </div>
        </div>

        <!-- Tab 2: Practice Questions (Placeholder) -->
        <div class="tab-panel" id="panel-practice">
            <div class="content-card">
                <h2><i class="fas fa-pen"></i> <span class="lang-hi">अभ्यास प्रश्न</span><span class="lang-en">Practice Questions</span></h2>
                <div class="placeholder-note">
                    <i class="fas fa-tools"></i> 
                    <strong>Coming Soon</strong><br>
                    <span class="lang-hi">20+ अभ्यास प्रश्न जल्द ही जोड़े जाएंगे...</span><br>
                    <span class="lang-en">20+ practice questions will be added soon...</span>
                </div>
            </div>
        </div>

        <!-- Tab 3: Mini Test (Placeholder) -->
        <div class="tab-panel" id="panel-test">
            <div class="content-card">
                <h2><i class="fas fa-clock"></i> <span class="lang-hi">मिनी टेस्ट</span><span class="lang-en">Mini Test</span></h2>
                <div class="placeholder-note">
                    <i class="fas fa-tools"></i> 
                    <strong>Coming Soon</strong><br>
                    <span class="lang-hi">10 प्रश्नों का मिनी टेस्ट जल्द ही उपलब्ध होगा...</span><br>
                    <span class="lang-en">Mini test with 10 questions coming soon...</span>
                </div>
            </div>
        </div>

        <!-- Tab 4: Revision (Placeholder) -->
        <div class="tab-panel" id="panel-revision">
            <div class="content-card">
                <h2><i class="fas fa-redo"></i> <span class="lang-hi">पुनरावृत्ति</span><span class="lang-en">Revision</span></h2>
                <div class="placeholder-note">
                    <i class="fas fa-tools"></i> 
                    <strong>Coming Soon</strong><br>
                    <span class="lang-hi">पुनरावृत्ति सामग्री जल्द ही जोड़ी जाएगी...</span><br>
                    <span class="lang-en">Revision material will be added soon...</span>
                </div>
            </div>
        </div>
    </main>

    <div id="footer-container"></div>

    <button id="backToTop" class="back-to-top" aria-label="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabPanels = document.querySelectorAll('.tab-panel');

            tabButtons.forEach(function(button) {
                button.addEventListener('click', function() {
                    const targetTab = button.getAttribute('data-target');

                    tabButtons.forEach(function(btn) { btn.classList.remove('active'); });
                    button.classList.add('active');

                    tabPanels.forEach(function(panel) {
                        panel.classList.remove('active');
                        if (panel.id === 'panel-' + targetTab) {
                            panel.classList.add('active');
                        }
                    });
                });
            });
        });
    </script>

    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>

</html>`;
}

// Generate all topic pages
microtopics.forEach(topic => {
    const html = generateTopicPage(topic);
    const filePath = path.join(OUTPUT_DIR, topic.slug + '.html');
    fs.writeFileSync(filePath, html, 'utf8');
    console.log('✓ Created topics/' + topic.slug + '.html');
});

console.log('\n✅ Done! Created ' + microtopics.length + ' microtopic pages in topics/ folder.');
console.log('\n📝 Next step: Integrate Gemini 3.5 Flash Lite API to populate Tab 1 content for each microtopic.');