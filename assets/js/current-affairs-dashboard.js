// Dynamic Current Affairs Dashboard Script for SJMaths
document.addEventListener('DOMContentLoaded', () => {
    const dashboard = new CurrentAffairsDashboard('ca-dashboard-root');
});

class CurrentAffairsDashboard {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        if (!this.container) return;

        this.currentTab = 'news'; // news, oneliners, mnemonics, mindmap, quiz
        this.date = this.getTodayIST();
        this.data = null;

        // Register global language switch listener
        window.addEventListener('ca-lang-changed', () => {
            this.render();
        });

        this.init();
    }

    getTodayIST() {
        const date = new Date();
        const tzOffset = 5.5 * 60 * 60 * 1000; // IST is UTC + 5:30
        const istTime = date.getTime() + date.getTimezoneOffset() * 60000 + tzOffset;
        const istDate = new Date(istTime);
        const yyyy = istDate.getFullYear();
        const mm = String(istDate.getMonth() + 1).padStart(2, '0');
        const dd = String(istDate.getDate()).padStart(2, '0');
        return `${yyyy}-${mm}-${dd}`;
    }

    async init() {
        this.renderFrame();
        this.setupEventListeners();
        await this.loadData();
    }

    renderFrame() {
        const isHi = document.body.classList.contains('lang-hi');
        
        this.container.innerHTML = `
            <!-- Date Navigator -->
            <div class="ca-date-nav">
                <button class="ca-date-btn" id="ca-prev-date">
                    <i class="fas fa-chevron-left"></i> <span class="lang-hi">पिछला दिन</span><span class="lang-en">Prev Day</span>
                </button>
                <div style="display: flex; align-items: center; gap: 0.75rem;">
                    <i class="far fa-calendar-alt" style="font-size: 1.25rem; color: var(--primary);"></i>
                    <input type="date" id="ca-date-picker" class="ca-current-date-label" style="border: none; background: transparent; outline: none; cursor: pointer; font-family: inherit; font-weight: 700; color: inherit;" value="${this.date}">
                </div>
                <button class="ca-date-btn" id="ca-next-date">
                    <span class="lang-hi">अगला दिन</span><span class="lang-en">Next Day</span> <i class="fas fa-chevron-right"></i>
                </button>
            </div>

            <!-- Learning Tabs Menu -->
            <div class="ca-dashboard-tabs">
                <button class="ca-dashboard-tab active" data-tab="news">
                    <i class="fas fa-newspaper"></i>
                    <span><span class="lang-hi">समाचार</span><span class="lang-en">News</span></span>
                </button>
                <button class="ca-dashboard-tab" data-tab="oneliners">
                    <i class="fas fa-bolt"></i>
                    <span><span class="lang-hi">वन-लाइनर्स</span><span class="lang-en">One-Liners</span></span>
                </button>
                <button class="ca-dashboard-tab" data-tab="mnemonics">
                    <i class="fas fa-brain"></i>
                    <span><span class="lang-hi">मेमोरी ट्रिक्स</span><span class="lang-en">Mnemonics</span></span>
                </button>
                <button class="ca-dashboard-tab" data-tab="mindmap">
                    <i class="fas fa-project-diagram"></i>
                    <span><span class="lang-hi">माइंडमैप</span><span class="lang-en">Mindmap</span></span>
                </button>
                <button class="ca-dashboard-tab" data-tab="quiz">
                    <i class="fas fa-vial"></i>
                    <span><span class="lang-hi">दैनिक क्विज़</span><span class="lang-en">Daily Quiz</span></span>
                </button>
            </div>

            <!-- Tab Content Panel -->
            <div id="ca-dashboard-content" style="min-height: 300px;">
                <div style="text-align: center; padding: 3rem;">
                    <i class="fas fa-spinner fa-spin fa-2x" style="color: var(--primary);"></i>
                </div>
            </div>
        `;
    }

    setupEventListeners() {
        // Tab switching
        const tabsContainer = this.container.querySelector('.ca-dashboard-tabs');
        tabsContainer.addEventListener('click', (e) => {
            const button = e.target.closest('.ca-dashboard-tab');
            if (!button) return;

            tabsContainer.querySelectorAll('.ca-dashboard-tab').forEach(b => b.classList.remove('active'));
            button.classList.add('active');

            this.currentTab = button.dataset.tab;
            this.renderTabContent();
        });

        // Date selection
        const datePicker = document.getElementById('ca-date-picker');
        datePicker.addEventListener('change', async (e) => {
            this.date = e.target.value;
            await this.loadData();
        });

        document.getElementById('ca-prev-date').addEventListener('click', async () => {
            const d = new Date(this.date);
            d.setDate(d.getDate() - 1);
            this.setDateValue(d);
            await this.loadData();
        });

        document.getElementById('ca-next-date').addEventListener('click', async () => {
            const d = new Date(this.date);
            d.setDate(d.getDate() + 1);
            this.setDateValue(d);
            await this.loadData();
        });
    }

    setDateValue(dateObj) {
        const yyyy = dateObj.getFullYear();
        const mm = String(dateObj.getMonth() + 1).padStart(2, '0');
        const dd = String(dateObj.getDate()).padStart(2, '0');
        this.date = `${yyyy}-${mm}-${dd}`;
        document.getElementById('ca-date-picker').value = this.date;
    }

    async loadData() {
        const contentPanel = document.getElementById('ca-dashboard-content');
        contentPanel.innerHTML = `
            <div style="text-align: center; padding: 4rem 1rem;">
                <i class="fas fa-spinner fa-spin fa-3x" style="color: var(--primary); margin-bottom: 1rem;"></i>
                <p class="lang-hi">समाचार लोड किए जा रहे हैं...</p>
                <p class="lang-en">Loading today's updates...</p>
            </div>
        `;

        try {
            // Attempt to load from JSON path
            const res = await fetch(`/current-affairs/data/daily-${this.date}.json`);
            if (res.ok) {
                this.data = await res.json();
            } else {
                // If it fails (e.g. today's file not generated yet), use premium mock demo data
                this.data = this.getMockData(this.date);
            }
        } catch (e) {
            console.warn("Dynamic load failed, switching to live demonstration mock dataset.");
            this.data = this.getMockData(this.date);
        }

        this.renderTabContent();
    }

    renderTabContent() {
        const panel = document.getElementById('ca-dashboard-content');
        if (!this.data) {
            panel.innerHTML = `
                <div style="text-align: center; padding: 3rem 1rem;">
                    <i class="fas fa-exclamation-triangle fa-2x" style="color: var(--secondary); margin-bottom: 1rem;"></i>
                    <p class="lang-hi">चयनित तिथि के लिए कोई डेटा उपलब्ध नहीं है।</p>
                    <p class="lang-en">No current affairs data found for this date.</p>
                </div>
            `;
            return;
        }

        switch (this.currentTab) {
            case 'news':
                this.renderNews(panel);
                break;
            case 'oneliners':
                this.renderOneliners(panel);
                break;
            case 'mnemonics':
                this.renderMnemonics(panel);
                break;
            case 'mindmap':
                this.renderMindmap(panel);
                break;
            case 'quiz':
                this.renderQuiz(panel);
                break;
        }
    }

    renderNews(panel) {
        if (!this.data.news || this.data.news.length === 0) {
            panel.innerHTML = `<p style="text-align: center; padding: 2rem;">No news items available.</p>`;
            return;
        }

        panel.innerHTML = this.data.news.map(item => {
            const isHi = document.body.classList.contains('lang-hi');
            const title = isHi ? item.title_hi : item.title_en;
            const desc = isHi ? item.desc_hi : item.desc_en;
            const category = isHi ? item.category_hi : item.category_en;
            const source = item.source || 'Official Update';

            return `
                <article class="ca-card">
                    <div class="ca-card-meta">
                        <span class="ca-card-source"><i class="fas fa-newspaper"></i> ${source}</span>
                        <span><i class="far fa-calendar-alt"></i> ${this.date}</span>
                    </div>
                    <h3 class="ca-card-title">${title}</h3>
                    <p class="ca-card-desc">${desc}</p>
                    <div class="ca-card-badges">
                        <span class="ca-badge ca-badge-category">${category}</span>
                        ${item.exams ? item.exams.map(ex => `<span class="ca-badge ca-badge-exam">${ex}</span>`).join('') : ''}
                    </div>
                </article>
            `;
        }).join('');
    }

    renderOneliners(panel) {
        if (!this.data.oneliners || this.data.oneliners.length === 0) {
            panel.innerHTML = `<p style="text-align: center; padding: 2rem;">No one-liners available.</p>`;
            return;
        }

        const isHi = document.body.classList.contains('lang-hi');
        const list = isHi ? this.data.oneliners.hi : this.data.oneliners.en;

        panel.innerHTML = `
            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                ${list.map(line => `
                    <div class="ca-oneliner-card">
                        <i class="fas fa-bolt" style="color: var(--secondary); margin-right: 0.5rem;"></i>
                        ${line}
                    </div>
                `).join('')}
            </div>
        `;
    }

    renderMnemonics(panel) {
        if (!this.data.mnemonics || this.data.mnemonics.length === 0) {
            panel.innerHTML = `<p style="text-align: center; padding: 2rem;">No memory tricks available.</p>`;
            return;
        }

        const isHi = document.body.classList.contains('lang-hi');

        panel.innerHTML = this.data.mnemonics.map(m => {
            const topic = isHi ? m.topic_hi : m.topic_en;
            const hook = isHi ? m.hook_hi : m.hook_en;
            const explanation = isHi ? m.explain_hi : m.explain_en;

            return `
                <div class="ca-mnemonic-card">
                    <div style="font-weight: 700; font-size: 0.9rem; color: var(--text-light); margin-bottom: 0.5rem; text-transform: uppercase;">
                        <i class="fas fa-brain"></i> Topic: ${topic}
                    </div>
                    <div class="ca-mnemonic-phrase">
                        "${hook}"
                    </div>
                    <div class="ca-mnemonic-explain">
                        ${explanation}
                    </div>
                </div>
            `;
        }).join('');
    }

    renderMindmap(panel) {
        if (!this.data.mindmapText) {
            panel.innerHTML = `<p style="text-align: center; padding: 2rem;">No mindmap structure available.</p>`;
            return;
        }

        panel.innerHTML = `
            <div class="ca-mindmap-container">
                <pre class="mermaid">
                    ${this.data.mindmapText}
                </pre>
            </div>
        `;

        // Safely re-initialize mermaid dynamically
        if (window.mermaid) {
            try {
                window.mermaid.init(undefined, document.querySelectorAll('.mermaid'));
            } catch (err) {
                console.error("Mermaid initialization failed", err);
            }
        } else {
            // Load Mermaid dynamically from CDN if not already loaded
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js';
            script.onload = () => {
                window.mermaid.initialize({ startOnLoad: true, theme: document.body.classList.contains('dark-mode') ? 'dark' : 'default' });
                window.mermaid.init(undefined, document.querySelectorAll('.mermaid'));
            };
            document.head.appendChild(script);
        }
    }

    renderQuiz(panel) {
        panel.innerHTML = `<div id="ca-dashboard-quiz-root"></div>`;
        if (window.CurrentAffairsQuiz) {
            new window.CurrentAffairsQuiz('ca-dashboard-quiz-root', { date: this.date });
        } else {
            // Fallback load quiz engine
            const script = document.createElement('script');
            script.src = '/assets/js/current-affairs-quiz.min.js';
            script.onload = () => {
                new window.CurrentAffairsQuiz('ca-dashboard-quiz-root', { date: this.date });
            };
            document.head.appendChild(script);
        }
    }

    getMockData(date) {
        // Return structured demo data based on today's current affairs to showcase it perfectly
        return {
            news: [
                {
                    title_en: "India Hosts BRICS National Security Advisers Meeting",
                    title_hi: "भारत ने की ब्रिक्स राष्ट्रीय सुरक्षा सलाहकारों की बैठक की मेजबानी",
                    desc_en: "India is hosting the annual BRICS National Security Advisers meeting starting today in New Delhi. Discussions will focus on non-traditional security challenges, counter-terrorism, and cybersecurity frameworks under expanding memberships.",
                    desc_hi: "भारत आज नई दिल्ली में वार्षिक ब्रिक्स राष्ट्रीय सुरक्षा सलाहकारों की बैठक की मेजबानी कर रहा है। चर्चाओं में गैर-पारंपरिक सुरक्षा चुनौतियों, आतंकवाद के विरोध और साइबर सुरक्षा ढांचे पर विशेष ध्यान दिया जाएगा।",
                    category_en: "International Relations",
                    category_hi: "अंतरराष्ट्रीय संबंध",
                    source: "PIB National",
                    exams: ["UPSC", "SSC CGL", "RO/ARO"]
                },
                {
                    title_en: "ARIES Study Highlights Role of Non-Methane Hydrocarbons (NMHCs) on Tropospheric Ozone",
                    title_hi: "ARIES अध्ययन ने क्षोभमंडलीय ओजोन पर गैर-मीथेन हाइड्रोकार्बन (NMHCs) के प्रभाव को उजागर किया",
                    desc_en: "Researchers at the Aryabhatta Research Institute of Observational Sciences (ARIES), Nainital found that NMHCs like ethane and propane serve as primary catalysts in forming tropospheric ozone and organic aerosols, affecting local air quality.",
                    desc_hi: "नैनीताल के आर्यभट्ट रिसर्च इंस्टीट्यूट ऑफ ऑब्जर्वेशनल साइंसेज (ARIES) के शोधकर्ताओं ने पाया कि ईथेन और प्रोपेन जैसे NMHCs निचले वायुमंडल में हानिकारक ओजोन बनाने में मुख्य उत्प्रेरक का काम करते हैं।",
                    category_en: "Environment & Ecology",
                    category_hi: "पर्यावरण और पारिस्थितिकी",
                    source: "Science Daily",
                    exams: ["UPSC", "UPPCS"]
                },
                {
                    title_en: "12th International Yoga Day Celebrated Globally with 'Healthy Ageing' Theme",
                    title_hi: "12वां अंतर्राष्ट्रीय योग दिवस विश्व स्तर पर 'स्वस्थ वृद्धावस्था' थीम के साथ मनाया गया",
                    desc_en: "The 12th International Day of Yoga was celebrated worldwide. Prime Minister Narendra Modi led the central celebrations in Kolkata, highlighting yoga as a key preventive healthcare lifestyle tool.",
                    desc_hi: "दुनिया भर में 12वां अंतर्राष्ट्रीय योग दिवस मनाया गया। प्रधानमंत्री नरेंद्र मोदी ने कोलकाता में मुख्य समारोह का नेतृत्व किया और योग को स्वास्थ्य संरक्षण जीवनशैली का एक महत्वपूर्ण साधन बताया।",
                    category_en: "National Schemes & Health",
                    category_hi: "राष्ट्रीय योजनाएं और स्वास्थ्य",
                    source: "NDTV News",
                    exams: ["SSC CGL", "Railway", "UPSC"]
                }
            ],
            oneliners: {
                en: [
                    "India hosts the 2026 BRICS National Security Advisers (NSA) Summit in New Delhi focusing on cybersecurity.",
                    "Aryabhatta Research Institute (ARIES), Nainital highlights the critical role of Non-Methane Hydrocarbons (NMHCs) in generating toxic tropospheric ozone.",
                    "The theme for the 12th International Day of Yoga (June 21, 2026) is 'Yoga for Healthy Ageing'.",
                    "Dr. Reddy's Laboratories launches Semaglutide oral tablets in India for managing Type-2 diabetes."
                ],
                hi: [
                    "भारत साइबर सुरक्षा पर केंद्रित नई दिल्ली में 2026 ब्रिक्स राष्ट्रीय सुरक्षा सलाहकार (NSA) शिखर सम्मेलन की मेजबानी कर रहा है।",
                    "आर्यभट्ट रिसर्च इंस्टीट्यूट (ARIES), नैनीताल ने जहरीली क्षोभमंडलीय ओजोन बनाने में गैर-मीथेन हाइड्रोकार्बन (NMHCs) की महत्वपूर्ण भूमिका पर प्रकाश डाला है।",
                    "12वें अंतर्राष्ट्रीय योग दिवस (21 जून, 2026) की थीम 'स्वस्थ वृद्धावस्था के लिए योग' है।",
                    "डॉ. रेड्डीज लैबोरेटरीज ने टाइप-2 मधुमेह के प्रबंधन के लिए भारत में सेमाग्लूटाइड ओरल टैबलेट लॉन्च की।"
                ]
            },
            mnemonics: [
                {
                    topic_en: "BRICS Official Members (Expanded)",
                    topic_hi: "ब्रिक्स के आधिकारिक सदस्य (विस्तारित)",
                    hook_en: "B-R-I-C-S  E-I-E-I-O",
                    hook_hi: "B-R-I-C-S  E-I-E-I-O",
                    explain_en: "Remember the members: <strong>B</strong>razil, <strong>R</strong>ussia, <strong>I</strong>ndia, <strong>C</strong>hina, <strong>S</strong>outh Africa + <strong>E</strong>gypt, <strong>I</strong>ran, <strong>E</strong>thiopia, <strong>U</strong>AE.",
                    explain_hi: "सदस्य देशों को याद रखें: <strong>B</strong>razil, <strong>R</strong>ussia, <strong>I</strong>ndia, <strong>C</strong>hina, <strong>S</strong>outh Africa + <strong>E</strong>gypt, <strong>I</strong>ran, <strong>E</strong>thiopia, <strong>U</strong>AE।"
                },
                {
                    topic_en: "Common Non-Methane Hydrocarbons (NMHCs)",
                    topic_hi: "सामान्य गैर-मीथेन हाइड्रोकार्बन (NMHCs)",
                    hook_en: "E-P-I-C",
                    hook_hi: "E-P-I-C",
                    explain_en: "Remember ground level precursors: <strong>E</strong>thane, <strong>P</strong>ropane, <strong>I</strong>soprene as <strong>C</strong>atalysts.",
                    explain_hi: "निचले स्तर के ओजोन अग्रदूतों को याद रखें: <strong>E</strong>thane, <strong>P</strong>ropane, <strong>I</strong>soprene को <strong>C</strong>atalysts (उत्प्रेरक) के रूप में।"
                }
            ],
            mindmapText: `
mindmap
  root((June 22 Current Affairs))
    BRICS NSA 2026
      Host New Delhi
      Focus Cyber Threats
      Focus Counter Terrorism
    Air Quality ARIES
      NMHC study
      Ethane Propane
      Ground Level Ozone
    Yoga Day 12th
      Theme Healthy Ageing
      PM led Kolkata
            `.trim()
        };
    }
}
