document.addEventListener("DOMContentLoaded", async () => {
    try {
        const studyTabs = document.querySelector(".study-tabs");
        const topicContent = document.getElementById("topic-content");
        const pageDataScript = document.getElementById("upsc-page-data");

        if (!studyTabs || !topicContent || !pageDataScript) {
            console.error("Missing essential elements for UPSC renderer.");
            return;
        }

        // Optional debug outline: visit the page with `?dbg=outline` or `#dbg-outline`
        try {
            const dbgParam = (new URLSearchParams(window.location.search).get('dbg') || '').toLowerCase();
            if (dbgParam === 'outline' || window.location.hash.includes('dbg-outline')) {
                topicContent.style.outline = '4px solid #ff00aa';
                topicContent.style.backgroundColor = '#ffffff';
                topicContent.style.color = '#0b0b0b';
                topicContent.style.boxShadow = '0 8px 0 rgba(0,0,0,0.6)';
                topicContent.setAttribute('data-dbg', 'outline');
                console.info('UPSC renderer: applied dbg-outline to #topic-content');
            }
        } catch (e) {
            // ignore debug helper failures
        }

        const pageData = JSON.parse(pageDataScript.textContent);
        const tabDataKeys = ["overview", "concepts", "visual", "comparisons", "practice", "pyqs", "mains", "revision", "test"];

        const loadTabData = async () => {
            const basePath = window.location.pathname.replace(/\/?index\.html$/, "/").replace(/\/?$/, "/");
            // Prefer the embedded list of available tab files ("tabs" key inside
            // #upsc-page-data) so we never probe tabs/*.json that were never
            // generated — probing produced a guaranteed 404 per missing tab.
            let keys = [];
            if (Array.isArray(pageData.tabs) && pageData.tabs.length > 0) {
                keys = tabDataKeys.filter(key => pageData.tabs.includes(key) && !pageData[key]);
            } else if (!Array.isArray(pageData.tabs)) {
                // Older incomplete pages have no generated tab files to load.
                keys = [];
            }

            const results = await Promise.all(keys.map(async (key) => {
                try {
                    const response = await fetch(`${basePath}tabs/${key}.json`, { cache: "no-cache" });
                    if (!response.ok) return null;
                    return [key, await response.json()];
                } catch (error) {
                    console.warn(`Could not load UPSC tab JSON: ${key}`, error);
                    return null;
                }
            }));

            results.filter(Boolean).forEach(([key, value]) => {
                pageData[key] = value;
            });
        };

        await loadTabData();

        // Normalize string encoding in case files were served with wrong charset (mojibake)
        const tryFixEncoding = (s) => {
            if (typeof s !== 'string') return s;
            // If string already contains Devanagari, assume correct
            if (/[\u0900-\u097F]/.test(s)) return s;
            // Only attempt fixes when there are signs of mojibake (typical Latin-1 artifacts)
            if (!/[\u00C0-\u00FF]|Ã|Â/.test(s)) return s;
            try {
                // Convert Latin1-interpreted UTF-8 back to proper UTF-8 when needed
                const decoded = decodeURIComponent(escape(s));
                // If decoded contains Devanagari and original didn't, prefer decoded
                if (/[\u0900-\u097F]/.test(decoded) && !/[\u0900-\u097F]/.test(s)) return decoded;
            } catch (e) {
                // ignore
            }
            return s;
        };

        // Convert simple markdown-like bold/italic markers into HTML
        const mdToHtml = (s) => {
            if (typeof s !== 'string') return s;
            // strong (**) then emphasis (*)
            s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
            s = s.replace(/\*(.+?)\*/g, '<em>$1</em>');
            return s;
        };

        // Recursively normalize all strings inside data object
        const normalizeStrings = (obj) => {
            if (typeof obj === 'string') {
                return mdToHtml(tryFixEncoding(obj));
            }
            if (Array.isArray(obj)) return obj.map(normalizeStrings);
            if (obj && typeof obj === 'object') {
                Object.keys(obj).forEach(k => { obj[k] = normalizeStrings(obj[k]); });
                return obj;
            }
            return obj;
        };

        // Helper function to render bilingual text (applies encoding/markdown fixes & strict lang toggle)
        const renderBilingual = (obj) => {
            if (typeof obj === 'string') {
                const cleanedStr = mdToHtml(tryFixEncoding(obj));
                const hasHindi = /[\u0900-\u097F]/.test(cleanedStr);
                const hasEnglish = /[a-zA-Z]/.test(cleanedStr.replace(/<[^>]+>/g, ""));

                if (hasHindi) {
                    return `<span class="lang-hi">${cleanedStr}</span>`;
                } else if (hasEnglish && !hasHindi) {
                    return `<span class="lang-en">${cleanedStr}</span>`;
                } else {
                    return `<span class="lang-en lang-hi">${cleanedStr}</span>`;
                }
            }
            if (obj && (obj.en || obj.hi)) {
                const enStr = mdToHtml(tryFixEncoding(obj.en || ""));
                const hiStr = mdToHtml(tryFixEncoding(obj.hi || ""));
                return `<span class="lang-en">${enStr}</span><span class="lang-hi">${hiStr}</span>`;
            }
            return "";
        };

        // Inject modern UI stylesheet for rich text presentation
        if (!document.getElementById('upsc-rich-ui-styles')) {
            const styleTag = document.createElement('style');
            styleTag.id = 'upsc-rich-ui-styles';
            styleTag.textContent = `
                .subcards-container {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
                    gap: 1.5rem;
                    margin: 1.5rem 0 2.5rem;
                }
                .subcard {
                    background: rgba(255, 255, 255, 0.95);
                    backdrop-filter: blur(12px);
                    -webkit-backdrop-filter: blur(12px);
                    border: 1px solid rgba(212, 175, 55, 0.22);
                    border-radius: 20px;
                    padding: 1.6rem 1.75rem;
                    box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.05), 0 4px 12px rgba(212, 175, 55, 0.08);
                    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease, border-color 0.3s ease;
                    display: flex;
                    flex-direction: column;
                }
                body.dark-mode .subcard {
                    background: rgba(15, 23, 42, 0.85);
                    border-color: rgba(212, 175, 55, 0.3);
                    color: #f8fafc;
                }
                .subcard:hover {
                    transform: translateY(-4px);
                    box-shadow: 0 20px 40px -10px rgba(41, 128, 185, 0.18), 0 8px 24px rgba(212, 175, 55, 0.2);
                    border-color: rgba(41, 128, 185, 0.4);
                }
                .subcard h4 {
                    font-family: 'Outfit', 'Inter', sans-serif;
                    font-size: 1.18rem;
                    font-weight: 700;
                    color: #0f172a;
                    margin: 0 0 1.1rem;
                    padding-bottom: 0.65rem;
                    border-bottom: 2px solid rgba(41, 128, 185, 0.18);
                    line-height: 1.35;
                }
                body.dark-mode .subcard h4 {
                    color: #f1f5f9;
                    border-bottom-color: rgba(212, 175, 55, 0.3);
                }
                .formatted-bullet-group {
                    display: flex;
                    flex-direction: column;
                    gap: 0.75rem;
                    margin: 0.75rem 0 1rem;
                }
                .bullet-item-row {
                    display: flex;
                    align-items: flex-start;
                    gap: 0.75rem;
                    background: rgba(248, 250, 252, 0.9);
                    border: 1px solid rgba(226, 232, 240, 0.9);
                    border-radius: 12px;
                    padding: 0.85rem 1.1rem;
                    transition: all 0.2s ease;
                }
                body.dark-mode .bullet-item-row {
                    background: rgba(30, 41, 59, 0.7);
                    border-color: rgba(51, 65, 85, 0.8);
                }
                .bullet-item-row:hover {
                    background: rgba(255, 255, 255, 1);
                    border-color: rgba(41, 128, 185, 0.3);
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
                }
                body.dark-mode .bullet-item-row:hover {
                    background: rgba(30, 41, 59, 0.95);
                    border-color: rgba(212, 175, 55, 0.4);
                }
                .bullet-icon-wrap {
                    color: #2563eb;
                    font-size: 0.95rem;
                    margin-top: 0.2rem;
                    flex-shrink: 0;
                }
                .bullet-text-wrap {
                    color: #334155;
                    font-size: 0.98rem;
                    line-height: 1.7;
                }
                body.dark-mode .bullet-text-wrap {
                    color: #cbd5e1;
                }
                .bullet-text-wrap strong {
                    color: #0f172a;
                    font-weight: 700;
                }
                body.dark-mode .bullet-text-wrap strong {
                    color: #fbbf24;
                }
                .content-callout-card {
                    border-radius: 14px;
                    padding: 1.1rem 1.3rem;
                    margin: 1rem 0;
                    position: relative;
                    backdrop-filter: blur(8px);
                }
                .trick-callout {
                    background: linear-gradient(135deg, rgba(245, 158, 11, 0.09) 0%, rgba(212, 175, 55, 0.14) 100%);
                    border: 1px solid rgba(245, 158, 11, 0.35);
                }
                .trap-callout {
                    background: linear-gradient(135deg, rgba(239, 68, 68, 0.09) 0%, rgba(220, 38, 38, 0.14) 100%);
                    border: 1px solid rgba(239, 68, 68, 0.35);
                }
                .callout-badge {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.45rem;
                    font-family: 'Outfit', sans-serif;
                    font-size: 0.78rem;
                    font-weight: 800;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                    padding: 0.3rem 0.7rem;
                    border-radius: 99px;
                    margin-bottom: 0.6rem;
                }
                .trick-callout .callout-badge {
                    background: rgba(245, 158, 11, 0.2);
                    color: #b45309;
                    border: 1px solid rgba(245, 158, 11, 0.35);
                }
                body.dark-mode .trick-callout .callout-badge {
                    color: #fbbf24;
                }
                .trap-callout .callout-badge {
                    background: rgba(239, 68, 68, 0.2);
                    color: #b91c1c;
                    border: 1px solid rgba(239, 68, 68, 0.35);
                }
                body.dark-mode .trap-callout .callout-badge {
                    color: #fca5a5;
                }
                .callout-text {
                    font-size: 0.96rem;
                    line-height: 1.7;
                    color: #1e293b;
                }
                body.dark-mode .callout-text {
                    color: #f1f5f9;
                }
                .formula-badge {
                    display: inline-block;
                    background: linear-gradient(135deg, rgba(41, 128, 185, 0.12), rgba(139, 92, 246, 0.12));
                    border: 1px solid rgba(41, 128, 185, 0.3);
                    color: #1e3a8a;
                    font-family: 'Outfit', 'Inter', monospace;
                    font-weight: 700;
                    font-size: 0.92rem;
                    padding: 0.15rem 0.55rem;
                    border-radius: 6px;
                    margin: 0.15rem 0.2rem;
                }
                body.dark-mode .formula-badge {
                    color: #93c5fd;
                    border-color: rgba(147, 197, 253, 0.3);
                    background: rgba(30, 58, 138, 0.3);
                }
                .table-container {
                    overflow-x: auto;
                    border-radius: 16px;
                    border: 1px solid rgba(212, 175, 55, 0.25);
                    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
                    margin: 1.5rem 0 2rem;
                    background: #ffffff;
                }
                body.dark-mode .table-container {
                    background: #0f172a;
                    border-color: rgba(212, 175, 55, 0.3);
                }
                .table-container table {
                    width: 100%;
                    border-collapse: separate;
                    border-spacing: 0;
                }
                .table-container th {
                    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                    color: #f8fafc;
                    font-family: 'Outfit', sans-serif;
                    font-size: 0.95rem;
                    font-weight: 700;
                    padding: 1rem 1.25rem;
                    border: none;
                }
                .table-container td {
                    padding: 1rem 1.25rem;
                    border-bottom: 1px solid #f1f5f9;
                    color: #334155;
                    font-size: 0.95rem;
                    line-height: 1.65;
                }
                body.dark-mode .table-container td {
                    border-bottom-color: #1e293b;
                    color: #cbd5e1;
                }
                .table-container tr:nth-child(even) {
                    background: #f8fafc;
                }
                body.dark-mode .table-container tr:nth-child(even) {
                    background: #1e293b;
                }
                .upsc-note {
                    border-radius: 16px;
                    padding: 1.35rem 1.6rem;
                    margin-bottom: 1rem;
                    border-left: 5px solid #3b82f6;
                    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.04);
                    background: rgba(255, 255, 255, 0.95);
                    border-top: 1px solid rgba(0, 0, 0, 0.05);
                    border-right: 1px solid rgba(0, 0, 0, 0.05);
                    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
                }
                body.dark-mode .upsc-note {
                    background: rgba(15, 23, 42, 0.9);
                    border-top-color: rgba(255, 255, 255, 0.05);
                    border-right-color: rgba(255, 255, 255, 0.05);
                    border-bottom-color: rgba(255, 255, 255, 0.05);
                }
                .upsc-note.tip {
                    border-left-color: #10b981;
                    background: linear-gradient(135deg, rgba(16, 185, 129, 0.05) 0%, rgba(255, 255, 255, 0.95) 100%);
                }
                .upsc-note.trap {
                    border-left-color: #f59e0b;
                    background: linear-gradient(135deg, rgba(245, 158, 11, 0.05) 0%, rgba(255, 255, 255, 0.95) 100%);
                }
                #topic-content ul {
                    list-style: none;
                    padding: 0;
                    margin: 1rem 0 2rem;
                    display: flex;
                    flex-direction: column;
                    gap: 0.75rem;
                }
                #topic-content ul li {
                    background: rgba(255, 255, 255, 0.9);
                    border: 1px solid rgba(226, 232, 240, 0.9);
                    border-radius: 12px;
                    padding: 0.95rem 1.25rem;
                    color: #334155;
                    font-size: 0.96rem;
                    line-height: 1.7;
                    position: relative;
                    padding-left: 2.75rem;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.02);
                }
                body.dark-mode #topic-content ul li {
                    background: rgba(15, 23, 42, 0.85);
                    border-color: rgba(51, 65, 85, 0.8);
                    color: #cbd5e1;
                }
                #topic-content ul li::before {
                    content: '\\f058';
                    font-family: 'Font Awesome 6 Free';
                    font-weight: 900;
                    position: absolute;
                    left: 1.1rem;
                    top: 0.95rem;
                    color: #059669;
                    font-size: 1.05rem;
                }
            `;
            document.head.appendChild(styleTag);
        }

        // Helper function to render formatted content strings into structured HTML
        const renderFormattedContent = (contentObj, language) => {
            // Format each translation separately: paragraph/list boundaries must
            // never split a language wrapper into invalid HTML.
            if (!language) {
                if (contentObj && typeof contentObj === 'object') {
                    return ['en', 'hi'].filter(lang => contentObj[lang]).map(lang =>
                        `<div class="lang-${lang} formatted-language-content">${renderFormattedContent(contentObj[lang], lang)}</div>`
                    ).join('');
                }
                if (typeof contentObj !== 'string' || !contentObj.trim()) return '';
                const lang = /[\u0900-\u097F]/.test(contentObj) ? 'hi' : /[a-zA-Z]/.test(contentObj) ? 'en' : 'shared';
                const classes = lang === 'shared' ? 'lang-en lang-hi' : `lang-${lang}`;
                return `<div class="${classes} formatted-language-content">${renderFormattedContent(contentObj, lang)}</div>`;
            }
            const rawStr = mdToHtml(tryFixEncoding(contentObj));
            if (!rawStr) return '';

            const lines = rawStr.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
            if (lines.length <= 1 && !rawStr.includes('• ') && !rawStr.includes('- ')) {
                return `<p class="bullet-text-wrap">${rawStr}</p>`;
            }

            let resultHtml = "";
            let inList = false;

            lines.forEach(line => {
                if (pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities" && /^MCQ\s+—\s*/.test(line)) {
                    if (inList) { resultHtml += `</div>`; inList = false; }
                    const example = line.replace(/^MCQ\s+—\s*/, "");
                    const separator = example.indexOf(" :: ");
                    if (separator < 0) {
                        resultHtml += `<article class="lesson-worked-example lesson-mcq"><div class="lesson-example-prompt"><span class="lesson-example-label">Question · MCQ</span>${renderFormattedContent(example)}</div></article>`;
                        return;
                    }
                    const promptAndOptions = example.slice(0, separator).split(" || ");
                    const prompt = promptAndOptions.shift();
                    const choices = promptAndOptions.map(choice => {
                        const match = choice.match(/^([A-D])\)\s*(.*)$/);
                        const optionText = match ? match[2] : choice;
                        const optionContent = `<p class="bullet-text-wrap">${mdToHtml(tryFixEncoding(optionText))}</p>`;
                        return `<div class="lesson-mcq-option" role="listitem"><span class="lesson-mcq-letter">${match ? match[1] : ""}</span>${optionContent}</div>`;
                    }).join("");
                    const working = example.slice(separator + 4).trim();
                    resultHtml += `
                        <article class="lesson-worked-example lesson-mcq">
                            <div class="lesson-example-prompt"><span class="lesson-example-label">Question · MCQ</span>${renderFormattedContent(prompt)}</div>
                            ${choices ? `<div class="lesson-example-options" role="list" aria-label="Answer options">${choices}</div>` : ""}
                            ${working ? `<div class="lesson-example-working"><span class="lesson-example-label">Correct option and reasoning</span>${renderFormattedContent(working)}</div>` : ""}
                        </article>
                    `;
                    return;
                }
                if (pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities" && /^Worked\s+—\s*/.test(line)) {
                    if (inList) { resultHtml += `</div>`; inList = false; }
                    const example = line.replace(/^Worked\s+—\s*/, "");
                    const workedSeparator = " :: ";
                    let separator = example.indexOf(workedSeparator);
                    let separatorLength = workedSeparator.length;
                    if (separator < 0) {
                        separator = example.indexOf(":");
                        separatorLength = 1;
                    }
                    if (separator < 0) {
                        separator = example.indexOf(", then ");
                        separatorLength = 7;
                    }
                    const prompt = separator < 0 ? example : example.slice(0, separator);
                    const working = separator < 0 ? "" : example.slice(separator + separatorLength).trim();
                    resultHtml += `
                        <article class="lesson-worked-example">
                            <div class="lesson-example-prompt">
                                <span class="lesson-example-label">Question</span>
                                ${renderFormattedContent(prompt)}
                            </div>
                            ${working ? `<div class="lesson-example-working"><span class="lesson-example-label">Working</span>${renderFormattedContent(working)}</div>` : ""}
                        </article>
                    `;
                    return;
                }

                if (pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities" && /^(Shortcut|Exam check|Exam formats):/i.test(line)) {
                    if (inList) { resultHtml += `</div>`; inList = false; }
                    const separator = line.indexOf(":");
                    resultHtml += `<div class="lesson-tip"><strong>${line.slice(0, separator)}:</strong>${renderFormattedContent(line.slice(separator + 1))}</div>`;
                    return;
                }

                if (pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities" && /^Derivation:/i.test(line)) {
                    if (inList) { resultHtml += `</div>`; inList = false; }
                    resultHtml += `<div class="lesson-derivation"><strong>Derivation:</strong>${renderFormattedContent(line.slice(line.indexOf(":") + 1))}</div>`;
                    return;
                }

                // Short-trick / Mnemonic / Important Tip
                if (/^(•\s*)?(\*\*|\*)?(याद रखने की शार्ट-ट्रिक|शार्ट-ट्रिक|Short-trick|Smart-Trick|परीक्षा हेतु महत्वपूर्ण|Note|Tip|परीक्षा रणनीति|परीक्षक का जाल):?/i.test(line)) {
                    if (inList) { resultHtml += `</div>`; inList = false; }
                    const cleanLine = line.replace(/^[•\-\*]\s*/, '');
                    const isTrap = /परीक्षक का जाल|Trap/i.test(line);
                    const iconClass = isTrap ? "fa-shield-halved" : "fa-lightbulb";
                    const badgeTitle = renderBilingual(isTrap ? {en: 'Examiner Trap', hi: 'परीक्षक का जाल'} : {en: 'Short-Trick / Mnemonic', hi: 'शॉर्ट ट्रिक / स्मरण सूत्र'});
                    
                    resultHtml += `
                        <div class="content-callout-card ${isTrap ? 'trap-callout' : 'trick-callout'}">
                            <div class="callout-badge">
                                <i class="fas ${iconClass}"></i> <span>${badgeTitle}</span>
                            </div>
                            <div class="callout-text">${cleanLine}</div>
                        </div>
                    `;
                    return;
                }

                // Bullet point item (• or -)
                if (/^[•\-\*]\s+/.test(line)) {
                    const itemText = line.replace(/^[•\-\*]\s+/, '');
                    let formattedItem = itemText.replace(/([A-Z0-9\u0900-\u097F\s\/]+?\s*\+\s*[A-Z0-9\u0900-\u097F\s\/]+?\s*=\s*\*\*?[A-Z0-9\u0900-\u097F\s\(\)]+\*\*?)/gi, '<span class="formula-badge">$1</span>');

                    if (!inList) {
                        resultHtml += `<div class="formatted-bullet-group">`;
                        inList = true;
                    }
                    resultHtml += `
                        <div class="bullet-item-row">
                            <div class="bullet-icon-wrap"><i class="fas fa-check-circle"></i></div>
                            <div class="bullet-text-wrap">${formattedItem}</div>
                        </div>
                    `;
                    return;
                }

                // Regular line
                if (inList) { resultHtml += `</div>`; inList = false; }
                resultHtml += `<p class="bullet-text-wrap">${line}</p>`;
            });

            if (inList) { resultHtml += `</div>`; }

            return resultHtml;
        };

        // Normalize the pageData loaded from inline JSON and fetched JSON tabs
        normalizeStrings(pageData);

        // Helper to shuffle an array (Fisher-Yates algorithm)
        const shuffleArray = (array) => {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        };

        const renderTabContent = (tabName) => {
            let contentHtml = "";

            switch (tabName) {
                case "overview":
                    contentHtml = `
                    <h2>${renderBilingual(pageData.overview.title)}</h2>
                    <p>${renderBilingual(pageData.overview.definition)}</p><h3>${renderBilingual({ en: "Importance in the Exam", hi: "परीक्षा में महत्व" })}</h3>
                    <p>${renderBilingual(pageData.overview.importanceInUpsc)}</p>
                    <h3>${renderBilingual({ en: "Learning Outcomes", hi: "सीखने के परिणाम" })}</h3>
                    <ul>
                        ${(pageData.overview.learningOutcomes || pageData.learningObjectives || []).map(obj => `<li>${renderBilingual(obj)}</li>`).join("")}
                    </ul>
                    ${pageData.overview.prerequisites && pageData.overview.prerequisites.length > 0 ? `
                    <h3>${renderBilingual({ en: "Prerequisites", hi: "आवश्यक शर्तें" })}</h3>
                    <ul>
                        ${pageData.overview.prerequisites.map(p => `<li>${renderBilingual(p)}</li>`).join("")}
                    </ul>
                    ` : ""}
                `;
                    break;
                case "concepts":
                    contentHtml = `
                    ${pageData.concepts.sections.map(section => {
                        let sectionHtml = `<h3>${renderBilingual(section.title)}</h3>`;
                        if (section.type === "paragraph") {
                            sectionHtml += renderFormattedContent(section.content);
                        } else if (section.type === "table") {
                            sectionHtml += `
                                <div class="table-container">
                                    <table>
                                        <thead>
                                            <tr>
                                                ${section.headers.map(header => `<th>${renderBilingual(header)}</th>`).join("")}
                                            </tr>
                                        </thead>
                                        <tbody>
                                            ${section.rows.map(row => `<tr>${row.map(cell => `<td>${renderBilingual(cell)}</td>`).join("")}</tr>`).join("")}
                                        </tbody>
                                    </table>
                                </div>
                            `;
                        } else if (section.type === "list") {
                            sectionHtml += `<ul>${section.items.map(item => `<li><strong>${renderBilingual(item.term)}:</strong> ${renderFormattedContent(item.definition)}</li>`).join("")}</ul>`;
                        } else if (section.type === "subcards") {
                            sectionHtml += `<div class="subcards-container">${section.items.map(item => `<div class="subcard"><h4><i class="fas fa-bookmark" style="color: #2563eb; font-size: 0.95rem;"></i> ${renderBilingual(item.title)}</h4>${renderFormattedContent(item.content)}</div>`).join("")}</div>`;
                        }
                        return sectionHtml;
                    }).join("")}
                    ${pageData.concepts.upscNotes && pageData.concepts.upscNotes.length > 0 ? `
                    <h3>${renderBilingual({ en: "Exam Notes & Insights", hi: "परीक्षा नोट्स और अंतर्दृष्टि" })}</h3>
                    <div class="upsc-notes-container">
                        ${pageData.concepts.upscNotes.map(note => `<div class="upsc-note ${note.type}"><p class="note-content"><i class="fas fa-lightbulb"></i> ${renderBilingual(note.content)}</p></div>`).join("")}
                    </div>
                    ` : ""}
                    ${pageData.concepts.keyTakeaways && pageData.concepts.keyTakeaways.length > 0 ? `
                    <h3>${renderBilingual({ en: "Key Takeaways", hi: "मुख्य बातें" })}</h3>
                    <ul>
                        ${pageData.concepts.keyTakeaways.map(item => `<li>${renderBilingual(item)}</li>`).join("")}
                    </ul>
                    ` : ""}
                `;
                    break;
                case "visual":
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Visual Learning Aids", hi: "दृश्य शिक्षण सहायक" })}</h2>
                    ${pageData.visual.visualBlocks.map(block => {
                        let blockHtml = `<h4>${renderBilingual(block.title)}</h4>`;
                        if (block.type === "timeline") {
                            blockHtml += `<div class="timeline">${block.data.map(item => `<div class="timeline-item"><h5>${renderBilingual(item.label)}</h5><p>${renderBilingual(item.description)}</p></div>`).join("")}</div>`;
                        } else if (block.type === "flow") {
                            blockHtml += `<div class="flowchart">${block.data.map(item => `<span>${renderBilingual(item)}</span>`).join(" â†’ ")}</div>`;
                        } else if (block.type === "tree") {
                            // Recursive rendering for tree structure
                            const renderTree = (node) => {
                                let treeHtml = `<ul><li>${renderBilingual(node.root || node.label)}`;
                                if (node.branches && node.branches.length > 0) {
                                    treeHtml += `<ul>${node.branches.map(branch => renderTree(branch)).join("")}</ul>`;
                                }
                                if (node.children && node.children.length > 0) {
                                    treeHtml += `<ul>${node.children.map(child => `<li>${renderBilingual(child)}</li>`).join("")}</ul>`;
                                }
                                treeHtml += `</li></ul>`;
                                return treeHtml;
                            };
                            blockHtml += `<div class="tree-view">${renderTree(block.data)}</div>`;
                        } else if (block.type === "table") {
                            blockHtml += `
                                <div class="table-container">
                                    <table>
                                        <thead>
                                            <tr>
                                                ${block.headers.map(header => `<th>${renderBilingual(header)}</th>`).join("")}
                                            </tr>
                                        </thead>
                                        <tbody>
                                            ${block.rows.map(row => `<tr>${row.map(cell => `<td>${renderBilingual(cell)}</td>`).join("")}</tr>`).join("")}
                                        </tbody>
                                    </table>
                                </div>
                            `;
                        }
                        return blockHtml;
                    }).join("")}
                `;
                    break;
                case "comparisons":
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Comparisons & Connections", hi: "तुलना और संबंध" })}</h2>
                    ${pageData.comparisons.differenceTables && pageData.comparisons.differenceTables.length > 0 ? `
                        ${pageData.comparisons.differenceTables.map(table => `
                            <h4>${renderBilingual(table.title)}</h4>
                            <div class="table-container">
                                <table>
                                    <thead>
                                        <tr>
                                            ${table.headers.map(header => `<th>${renderBilingual(header)}</th>`).join("")}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${table.rows.map(row => `<tr>${row.map(cell => `<td>${renderBilingual(cell)}</td>`).join("")}</tr>`).join("")}
                                    </tbody>
                                </table>
                            </div>
                        `).join("")}
                    ` : ""}
                    ${pageData.comparisons.similarityTables && pageData.comparisons.similarityTables.length > 0 ? `
                        ${pageData.comparisons.similarityTables.map(table => `
                            <h4>${renderBilingual(table.title)}</h4>
                            <div class="table-container">
                                <table>
                                    <thead>
                                        <tr>
                                            ${table.headers.map(header => `<th>${renderBilingual(header)}</th>`).join("")}
                                        </tr>
                                    </thead>
                                    <tbody>
                                        ${table.rows.map(row => `<tr>${row.map(cell => `<td>${renderBilingual(cell)}</td>`).join("")}</tr>`).join("")}
                                    </tbody>
                                </table>
                            </div>
                        `).join("")}
                    ` : ""}
                    ${pageData.comparisons.evolution ? `
                        <h4>${renderBilingual(pageData.comparisons.evolution.title)}</h4>
                        <p>${pageData.comparisons.evolution.steps.map(step => renderBilingual(step)).join(" â†’ ")}</p>
                    ` : ""}
                    ${pageData.comparisons.frequentlyConfused && pageData.comparisons.frequentlyConfused.length > 0 ? `
                        <h3>${renderBilingual({ en: "Frequently Confused Concepts", hi: "अक्सर भ्रमित होने वाली अवधारणाएँ" })}</h3>
                        <ul>
                            ${pageData.comparisons.frequentlyConfused.map(item => `<li><strong>${renderBilingual(item.topicA)}</strong> vs <strong>${renderBilingual(item.topicB)}</strong>: ${renderBilingual(item.clarification)}</li>`).join("")}
                        </ul>
                    ` : ""}
                    ${pageData.comparisons.conceptConnections && pageData.comparisons.conceptConnections.length > 0 ? `
                        <h3>${renderBilingual({ en: "Concept Connections", hi: "अवधारणा संबंध" })}</h3>
                        <ul>
                            ${pageData.comparisons.conceptConnections.map(item => `<li><strong>${renderBilingual(item.from)}</strong> to <strong>${renderBilingual(item.to)}</strong>: ${renderBilingual(item.relationship)}</li>`).join("")}
                        </ul>
                    ` : ""}
                `;
                    break;
                case "practice":
                    const identityPracticeLevels = pageData.practice && pageData.practice.levels ? pageData.practice.levels : {};
                    const isAlgebraicIdentitiesPractice = pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities";
                    const identityPracticeCount = Object.values(identityPracticeLevels).reduce((total, questions) => total + (Array.isArray(questions) ? questions.length : 0), 0);
                    const practiceLevelEntries = Object.entries(identityPracticeLevels).filter(([_, questions]) => Array.isArray(questions) && questions.length > 0);
                    const levelNames = {
                        easy: { en: "Easy", hi: "सरल" },
                        medium: { en: "Medium", hi: "मध्यम" },
                        hard: { en: "Hard", hi: "कठिन" },
                        mcq: { en: "MCQs", hi: "बहुविकल्पीय" },
                        statementBased: { en: "Statements", hi: "कथन आधारित" },
                        match: { en: "Matching", hi: "मिलान करें" },
                        assertionReason: { en: "Assertion-Reason", hi: "अभिकथन और कारण" }
                    };
                    const hasMultipleSubTabs = practiceLevelEntries.length > 1;

                    let subTabsHtml = "";
                    if (hasMultipleSubTabs) {
                        subTabsHtml = `
                            <div class="practice-sub-tabs" role="tablist" aria-label="Practice Difficulty Levels">
                                ${practiceLevelEntries.map(([type, questions], idx) => {
                                    const lvlName = levelNames[type] || { en: formatQuestionLevel(type), hi: formatQuestionLevel(type) };
                                    return `
                                        <button type="button" class="sub-tab-btn${idx === 0 ? " active" : ""}" data-subtab="practice-${type}" role="tab" aria-selected="${idx === 0 ? "true" : "false"}">
                                            <span>${renderBilingual(lvlName)}</span>
                                            <span class="subtab-count">${questions.length}</span>
                                        </button>
                                    `;
                                }).join("")}
                            </div>
                        `;
                    }

                    contentHtml = `
                    <h2>${renderBilingual({ en: "Practice Questions", hi: "अभ्यास प्रश्न" })}</h2>
                    ${isAlgebraicIdentitiesPractice ? `<p class="practice-intro"><strong>${identityPracticeCount} questions</strong><span>Choose one answer. Select an option to check it and see the reasoning.</span></p>` : ""}
                    ${subTabsHtml}
                    <div class="practice-questions-container${isAlgebraicIdentitiesPractice ? " algebraic-identities-practice" : ""}">
                        ${practiceLevelEntries.length > 0 ? practiceLevelEntries.map(([type, questions], idx) => {
                            const lvlName = levelNames[type] || { en: formatQuestionLevel(type), hi: formatQuestionLevel(type) };
                            const prevLevel = idx > 0 ? practiceLevelEntries[idx - 1] : null;
                            const nextLevel = idx < practiceLevelEntries.length - 1 ? practiceLevelEntries[idx + 1] : null;

                            return `
                            <div class="practice-sub-panel${idx === 0 ? " active" : ""}" id="practice-${type}" data-subpanel="practice-${type}" role="tabpanel"${idx === 0 ? "" : ' style="display: none;"'}>
                                <div class="practice-level ${type}-level">
                                    <h3>${renderBilingual({en: formatQuestionLevel(type), hi: ({easy:"सरल",medium:"मध्यम",hard:"कठिन",mcq:"बहुविकल्पीय",statementBased:"कथन आधारित",match:"मिलान करें",assertionReason:"अभिकथन और कारण"})[type] || formatQuestionLevel(type)})} ${renderBilingual({en: "Questions", hi: "प्रश्न"})}${Array.isArray(questions) ? ` <span class="practice-level-count">${questions.length}</span>` : ""}</h3>
                                    ${Array.isArray(questions) ? questions.map((q, qIndex) => {
                            let qHtml = `<div class="practice-question-card"><div class="q-row"><div class="q-num-badge">${qIndex + 1}</div><div class="q-body">`;
                            if (q.question) {
                                qHtml += `<p class="q-text-sm">${renderBilingual(q.question)}</p>`;
                            }
                            if (q.statements) {
                                qHtml += `<ul class="statement-list">${q.statements.map((s, i) => `<li><span class="statement-index">${i + 1}</span><span>${renderBilingual(s.text || s)}</span></li>`).join("")}</ul>`;
                            }
                            if (q.assertion) {
                                qHtml += `<p class="q-text-sm"><strong><span class="lang-en">Assertion (A):</span><span class="lang-hi">अभिकथन (A):</span></strong> ${renderBilingual(q.assertion)}</p>`;
                                qHtml += `<p class="q-text-sm"><strong><span class="lang-en">Reason (R):</span><span class="lang-hi">कारण (R):</span></strong> ${renderBilingual(q.reason)}</p>`;
                            }
                            if (q.pairs) {
                                qHtml += `<div class="match-pairs">${q.pairs.map((pair, i) => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><label class="match-choice"><span>${renderBilingual(pair.right)}</span><select aria-label="Match ${i + 1}"><option value="">Choose</option>${q.pairs.map((_, n) => `<option value="${n + 1}">${n + 1}</option>`).join("")}</select></label></div>`).join("")}</div>`;
                            }

                            qHtml += `<div class="options-container">`;
                            if (q.options && Array.isArray(q.options)) {
                                q.options.forEach(option => {
                                    const optionText = pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities"
                                        ? mdToHtml(tryFixEncoding(option.text || ""))
                                        : renderBilingual(option.text);
                                    qHtml += `
                                                    <div class="practice-option-box">
                                                        <label class="opt-label">
                                                            <input type="radio" name="p-${type}-${q.id || qIndex}" class="opt-radio" data-q-id="${q.id || qIndex}" data-opt-letter="${option.letter}" data-correct="${option.letter === q.correctAnswer}">
                                                            <span><b>${option.letter}.</b> ${optionText}</span>
                                                        </label>
                                                    </div>
                                                `;
                                });
                            }
                            qHtml += `</div><div class="sol-box"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${q.correctAnswer || q.correctMapping || ""}</strong> ${renderBilingual(q.explanation)}</p></div></div></div></div>`;
                            return qHtml;
                        }).join("") : ""}
                                </div>
                                ${hasMultipleSubTabs ? `
                                <div class="practice-subtab-nav${prevLevel ? " has-prev" : ""}">
                                    ${prevLevel ? `
                                        <button type="button" class="practice-nav-btn prev" data-target="practice-${prevLevel[0]}">
                                            <i class="fas fa-arrow-left"></i>
                                            <span>
                                                <small>${renderBilingual({ en: "Previous Level", hi: "पिछला स्तर" })}</small>
                                                <strong>${renderBilingual(levelNames[prevLevel[0]] || { en: formatQuestionLevel(prevLevel[0]), hi: formatQuestionLevel(prevLevel[0]) })}</strong>
                                            </span>
                                        </button>
                                    ` : ""}
                                    ${nextLevel ? `
                                        <button type="button" class="practice-nav-btn next" data-target="practice-${nextLevel[0]}">
                                            <span>
                                                <small>${renderBilingual({ en: "Next Level", hi: "अगला स्तर" })}</small>
                                                <strong>${renderBilingual(levelNames[nextLevel[0]] || { en: formatQuestionLevel(nextLevel[0]), hi: formatQuestionLevel(nextLevel[0]) })}</strong>
                                            </span>
                                            <i class="fas fa-arrow-right"></i>
                                        </button>
                                    ` : `
                                        <button type="button" class="practice-nav-btn next finish-practice" data-target-tab="tab-pyqs">
                                            <span>
                                                <small>${renderBilingual({ en: "Next Section", hi: "अगला खंड" })}</small>
                                                <strong>${renderBilingual({ en: "Previous Year Questions", hi: "पिछले वर्ष के प्रश्न" })}</strong>
                                            </span>
                                            <i class="fas fa-arrow-right"></i>
                                        </button>
                                    `}
                                </div>
                                ` : ""}
                            </div>
                            `;
                        }).join("") : `<p>${renderBilingual({ en: "Practice questions not available.", hi: "अभ्यास प्रश्न उपलब्ध नहीं हैं।" })}</p>`}
                    </div>
                `;
                    break;
                case "pyqs":
                    const pyqs = pageData.pyqs || {};
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Previous Year Questions", hi: "पिछले वर्ष के प्रश्न" })}</h2>
                    <div class="practice-questions-container">
                        ${pyqs.questions && pyqs.questions.length > 0 ? pyqs.questions.map((q, qIndex) => {
                        let qHtml = `<div class="practice-question-card"><div class="q-row"><div class="q-num-badge">${qIndex + 1}</div><div class="q-body">`;
                        if (q.year) {
                            qHtml += `<span class="keyword-tag">${renderBilingual({ en: `UPSSSC PET ${q.year}`, hi: `UPSSSC PET ${q.year}` })}</span>`;
                        }
                        if (q.question) {
                            qHtml += `<p class="q-text-sm">${renderBilingual(q.question)}</p>`;
                        }
                        if (q.statements) {
                            qHtml += `<ul class="statement-list">${q.statements.map((s, i) => `<li><span class="statement-index">${i + 1}</span><span>${renderBilingual(s.text || s)}</span></li>`).join("")}</ul>`;
                        }
                        if (q.pairs) {
                            qHtml += `<div class="match-pairs">${q.pairs.map((pair, i) => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><label class="match-choice"><span>${renderBilingual(pair.right)}</span><select aria-label="Match ${i + 1}"><option value="">Choose</option>${q.pairs.map((_, n) => `<option value="${n + 1}">${n + 1}</option>`).join("")}</select></label></div>`).join("")}</div>`;
                        }
                        qHtml += `<div class="options-container">`;
                        if (q.options && Array.isArray(q.options)) {
                            q.options.forEach(option => {
                                qHtml += `
                                        <div class="practice-option-box">
                                            <label class="opt-label">
                                                <input type="radio" name="pyq-${q.id || qIndex}" class="opt-radio" data-correct="${option.letter === q.correctAnswer}">
                                                <span><b>${option.letter}.</b> ${renderBilingual(option.text)}</span>
                                            </label>
                                        </div>
                                    `;
                            });
                        }
                        qHtml += `</div><div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${q.correctAnswer || q.correctMapping || ""}</strong> ${renderBilingual(q.explanation)}</p></div>`;
                        qHtml += `</div></div></div>`;
                        return qHtml;
                    }).join("") : `<p>${renderBilingual({ en: "Previous year questions will be available soon.", hi: "पिछले वर्ष के प्रश्न जल्द ही उपलब्ध होंगे।" })}</p>`}
                    </div>
                `;
                    break;
                case "mains":
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Mains Answer Writing", hi: "मुख्य उत्तर लेखन" })}</h2>
                    ${pageData.mains.questions.map(q => `
                        <div class="mains-question-card">
                            <h3>${renderBilingual(q.question)} <span class="mains-marks">(${q.marks} Marks)</span></h3>
                            <h4>${renderBilingual({ en: "Expected Structure", hi: "अपेक्षित संरचना" })}</h4>
                            <ul>
                                ${q.structure.map(item => `<li>${renderBilingual(item)}</li>`).join("")}
                            </ul>
                            ${q.keywords && q.keywords.length > 0 ? `
                            <h4>${renderBilingual({ en: "Keywords", hi: "मुख्य शब्द" })}</h4>
                            <p>${q.keywords.map(kw => `<span class="keyword-tag">${renderBilingual(kw)}</span>`).join("")}</p>
                            ` : ""}
                            <div class="model-answer-section">
                                <h4>${renderBilingual({ en: "Model Answer", hi: "मॉडल उत्तर" })}</h4>
                                <p><strong>${renderBilingual({ en: "Introduction:", hi: "परिचय:" })}</strong> ${renderBilingual(q.modelAnswer.introduction)}</p>
                                <p><strong>${renderBilingual({ en: "Body:", hi: "मुख्य भाग:" })}</strong> ${renderBilingual(q.modelAnswer.body)}</p>
                                <p><strong>${renderBilingual({ en: "Conclusion:", hi: "निष्कर्ष:" })}</strong> ${renderBilingual(q.modelAnswer.conclusion)}</p>
                            </div>
                            ${q.valueAddition && q.valueAddition.length > 0 ? `
                            <h4>${renderBilingual({ en: "Value Addition", hi: "मूल्य संवर्धन" })}</h4>
                            <ul>
                                ${q.valueAddition.map(item => `<li>${renderBilingual(item)}</li>`).join("")}
                            </ul>
                            ` : ""}
                            ${q.diagram ? `
                            <h4>${renderBilingual({ en: "Diagram/Flowchart", hi: "आरेख/फ्लोचार्ट" })}</h4>
                            <div class="diagram-container">
                                ${q.diagram.type === "flow" ? `<div class="flowchart">${q.diagram.data.map(item => `<span>${renderBilingual(item)}</span>`).join(" â†’ ")}</div>` : renderBilingual(q.diagram.description)}
                            </div>
                            ` : ""}
                        </div>
                    `).join("")}
                `;
                    break;
                case "revision":
                    const revision = pageData.revision || {};
                    const revisionTakeaways = pageData.concepts?.keyTakeaways || [];
                    const hasStructuredRevision = Boolean(
                        revision.onePageNotes?.columns?.length
                        || revision.mnemonics?.length
                        || revision.flashcards?.length
                        || revision.frequentlyConfusedFacts?.length
                        || revision.examDaySheet?.fiveFacts?.length
                        || revision.examDaySheet?.threeTraps?.length
                        || revision.examDaySheet?.oneMnemonic
                    );
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Revision Notes", hi: "रिवीजन नोट्स" })}</h2>
                    ${revision.onePageNotes && revision.onePageNotes.columns ? `
                    <div class="revision-grid">
                        ${revision.onePageNotes.columns.map(column => `
                            <div class="revision-card">
                                <h3>${renderBilingual(column.title)}</h3>
                                <ul>${column.points.map(point => `<li>${renderBilingual(point)}</li>`).join("")}</ul>
                            </div>
                        `).join("")}
                    </div>
                    ` : ""}
                    ${revision.mnemonics && revision.mnemonics.length > 0 ? `
                    <h3>${renderBilingual({ en: "Mnemonics", hi: "स्मृति सहायक" })}</h3>
                    <div class="revision-grid">
                        ${revision.mnemonics.map(item => `
                            <div class="revision-card">
                                <h4>${renderBilingual(item.phrase)}</h4>
                                <p><strong>${renderBilingual(item.meaning)}</strong></p>
                                <p>${renderBilingual(item.explanation)}</p>
                            </div>
                        `).join("")}
                    </div>
                    ` : ""}
                    ${revision.flashcards && revision.flashcards.length > 0 ? `
                    <h3>${renderBilingual({ en: "Flashcards", hi: "फ्लैशकार्ड" })}</h3>
                    <div class="revision-grid">
                        ${revision.flashcards.map(card => `
                            <div class="revision-card">
                                <h4>${renderBilingual(card.question)}</h4>
                                <p>${renderBilingual(card.answer)}</p>
                            </div>
                        `).join("")}
                    </div>
                    ` : ""}
                    ${revision.frequentlyConfusedFacts && revision.frequentlyConfusedFacts.length > 0 ? `
                    <h3>${renderBilingual({ en: "Frequently Confused Facts", hi: "अक्सर भ्रमित करने वाले तथ्य" })}</h3>
                    <ul>${revision.frequentlyConfusedFacts.map(item => `<li><strong>${renderBilingual(item.misconception)}</strong> ${renderBilingual(item.correction)}</li>`).join("")}</ul>
                    ` : ""}
                    ${revision.examDaySheet ? `
                    <h3>${renderBilingual({ en: "Exam Day Sheet", hi: "परीक्षा दिवस शीट" })}</h3>
                    ${revision.examDaySheet.fiveFacts ? `<h4>${renderBilingual({ en: "Five Facts", hi: "पांच तथ्य" })}</h4><ul>${revision.examDaySheet.fiveFacts.map(item => `<li>${renderBilingual(item)}</li>`).join("")}</ul>` : ""}
                    ${revision.examDaySheet.threeTraps ? `<h4>${renderBilingual({ en: "Three Traps", hi: "तीन जाल" })}</h4><ul>${revision.examDaySheet.threeTraps.map(item => `<li>${renderBilingual(item)}</li>`).join("")}</ul>` : ""}
                    ${revision.examDaySheet.oneMnemonic ? `<div class="revision-card"><h4>${renderBilingual(revision.examDaySheet.oneMnemonic.phrase)}</h4><p>${renderBilingual(revision.examDaySheet.oneMnemonic.meaning)}</p></div>` : ""}
                    ` : ""}
                    ${!hasStructuredRevision && revisionTakeaways.length ? `
                    <h3>${renderBilingual({ en: "Key Takeaways", hi: "मुख्य बातें" })}</h3>
                    <ul>${revisionTakeaways.map(item => `<li>${renderBilingual(item)}</li>`).join("")}</ul>
                    ` : ""}
                `;
                    break;
                case "test":
                    const test = pageData.test || {};
                    const hasTestLevels = Boolean(test.levels && Object.keys(test.levels).length > 0);

                    if (hasTestLevels) {
                        const testLevelEntries = Object.entries(test.levels).filter(([_, qs]) => Array.isArray(qs) && qs.length > 0);
                        const testLevelNames = {
                            easy: { en: "Easy", hi: "सरल" },
                            medium: { en: "Medium", hi: "मध्यम" },
                            hard: { en: "Hard", hi: "कठिन" }
                        };

                        contentHtml = `
                        <h2>${renderBilingual({ en: "3-Level Mini Test", hi: "3-स्तरीय मिनी टेस्ट" })}</h2>
                        <p class="test-intro-text">${renderBilingual({
                            en: "Attempt questions under exam conditions. Submit each level individually to reveal your instant score, performance breakdown, and bilingual solutions.",
                            hi: "परीक्षा प्रारूप में प्रश्नों को हल करें। अपना तत्काल स्कोर, प्रदर्शन विश्लेषण और विस्तृत समाधान देखने के लिए प्रत्येक स्तर को जमा करें।"
                        })}</p>

                        <div class="test-sub-tabs" role="tablist" aria-label="Mini Test Levels">
                            ${testLevelEntries.map(([lvl, qs], idx) => {
                                const lvlName = testLevelNames[lvl] || { en: formatQuestionLevel(lvl), hi: formatQuestionLevel(lvl) };
                                return `
                                    <button type="button" class="sub-tab-btn${idx === 0 ? " active" : ""}" data-test-subtab="test-${lvl}" role="tab" aria-selected="${idx === 0}">
                                        <span>${renderBilingual(lvlName)}</span>
                                        <span class="subtab-count">${qs.length}</span>
                                    </button>
                                `;
                            }).join("")}
                        </div>

                        <div class="test-sub-panels-wrapper">
                            ${testLevelEntries.map(([lvl, questions], idx) => {
                                const lvlName = testLevelNames[lvl] || { en: formatQuestionLevel(lvl), hi: formatQuestionLevel(lvl) };
                                const prevLevel = idx > 0 ? testLevelEntries[idx - 1] : null;
                                const nextLevel = idx < testLevelEntries.length - 1 ? testLevelEntries[idx + 1] : null;

                                return `
                                <div class="test-sub-panel${idx === 0 ? " active" : ""}" id="test-${lvl}" data-test-subpanel="test-${lvl}" role="tabpanel"${idx === 0 ? "" : ' style="display: none;"'}>
                                    <div class="test-level-header">
                                        <h3>${renderBilingual(lvlName)} ${renderBilingual({ en: "Test", hi: "टेस्ट" })} <span class="test-level-badge">${questions.length} ${renderBilingual({ en: "Questions", hi: "प्रश्न" })}</span></h3>
                                        <span class="test-timer-indicator"><i class="fas fa-clock"></i> ${renderBilingual({ en: "Target: 10 mins", hi: "लक्षित समय: 10 मिनट" })}</span>
                                    </div>
                                    <div class="practice-questions-container test-questions-container">
                                        ${questions.map((q, qIndex) => {
                                            let qHtml = `<div class="practice-question-card test-question-card" data-level="${lvl}"><div class="q-row"><div class="q-num-badge">${qIndex + 1}</div><div class="q-body">`;
                                            if (q.question) {
                                                qHtml += `<p class="q-text-sm">${renderBilingual(q.question)}</p>`;
                                            }
                                            if (q.statements) {
                                                qHtml += `<ul class="statement-list">${q.statements.map((s, i) => `<li><span class="statement-index">${i + 1}</span><span>${renderBilingual(s.text || s)}</span></li>`).join("")}</ul>`;
                                            }
                                            if (q.assertion) {
                                                qHtml += `<p class="q-text-sm"><strong><span class="lang-en">Assertion (A):</span><span class="lang-hi">अभिकथन (A):</span></strong> ${renderBilingual(q.assertion)}</p>`;
                                                qHtml += `<p class="q-text-sm"><strong><span class="lang-en">Reason (R):</span><span class="lang-hi">कारण (R):</span></strong> ${renderBilingual(q.reason)}</p>`;
                                            }
                                            if (q.pairs) {
                                                qHtml += `<div class="match-pairs">${q.pairs.map((pair, i) => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><label class="match-choice"><span>${renderBilingual(pair.right)}</span><select aria-label="Match ${i + 1}"><option value="">Choose</option>${q.pairs.map((_, n) => `<option value="${n + 1}">${n + 1}</option>`).join("")}</select></label></div>`).join("")}</div>`;
                                            }

                                            qHtml += `<div class="options-container">`;
                                            if (q.options && Array.isArray(q.options)) {
                                                q.options.forEach(option => {
                                                    qHtml += `
                                                        <div class="practice-option-box test-option-box">
                                                            <label class="opt-label">
                                                                <input type="radio" name="mini-test-${lvl}-${q.id || qIndex}" class="opt-radio" data-correct="${option.letter === q.correctAnswer}" data-opt="${option.letter}">
                                                                <span><b>${option.letter}.</b> ${renderBilingual(option.text)}</span>
                                                            </label>
                                                        </div>
                                                    `;
                                                });
                                            }
                                            qHtml += `</div><div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${q.correctAnswer || ""}</strong> ${renderBilingual(q.explanation)}</p></div></div></div></div>`;
                                            return qHtml;
                                        }).join("")}
                                    </div>

                                    <div class="test-level-action-row">
                                        <button type="button" class="btn-submit-level-test" data-level="${lvl}">
                                            <i class="fas fa-check-circle"></i> ${renderBilingual({ en: `Submit ${formatQuestionLevel(lvl)} Test`, hi: `${({'easy': 'सरल', 'medium': 'मध्यम', 'hard': 'कठिन'})[lvl] || formatQuestionLevel(lvl)} टेस्ट जमा करें` })}
                                        </button>
                                        <div class="test-level-score-badge" id="score-badge-${lvl}" style="display:none;"></div>
                                    </div>

                                    <div class="practice-subtab-nav${prevLevel ? " has-prev" : ""}">
                                        ${prevLevel ? `
                                            <button type="button" class="practice-nav-btn prev" data-test-target="test-${prevLevel[0]}">
                                                <i class="fas fa-arrow-left"></i>
                                                <span>
                                                    <small>${renderBilingual({ en: "Previous Level", hi: "पिछला स्तर" })}</small>
                                                    <strong>${renderBilingual(testLevelNames[prevLevel[0]] || { en: formatQuestionLevel(prevLevel[0]), hi: formatQuestionLevel(prevLevel[0]) })}</strong>
                                                </span>
                                            </button>
                                        ` : ""}
                                        ${nextLevel ? `
                                            <button type="button" class="practice-nav-btn next" data-test-target="test-${nextLevel[0]}">
                                                <span>
                                                    <small>${renderBilingual({ en: "Next Level", hi: "अगला स्तर" })}</small>
                                                    <strong>${renderBilingual(testLevelNames[nextLevel[0]] || { en: formatQuestionLevel(nextLevel[0]), hi: formatQuestionLevel(nextLevel[0]) })}</strong>
                                                </span>
                                                <i class="fas fa-arrow-right"></i>
                                            </button>
                                        ` : `
                                            <button type="button" class="practice-nav-btn next finish-practice" data-target-tab="tab-overview">
                                                <span>
                                                    <small>${renderBilingual({ en: "Test Completed", hi: "टेस्ट पूर्ण हुआ" })}</small>
                                                    <strong>${renderBilingual({ en: "Review Notes", hi: "नोट्स दोहराएं" })}</strong>
                                                </span>
                                                <i class="fas fa-arrow-right"></i>
                                            </button>
                                        `}
                                    </div>
                                </div>
                                `;
                            }).join("")}
                        </div>
                        `;
                    } else {
                        const testGroups = [["mcq", "MCQs"], ["statementBased", "Statement Based"], ["match", "Match the Following"]];
                        const renderTestQuestion = (q, qIndex, groupKey) => {
                            let qHtml = `<div class="practice-question-card test-question-card"><div class="q-row"><div class="q-num-badge">${qIndex + 1}</div><div class="q-body">`;
                            qHtml += q.question ? `<p class="q-text-sm">${renderBilingual(q.question)}</p>` : "";
                            if (q.statements) qHtml += `<p class="q-text-sm statement-intro">${renderBilingual({ en: "Consider the following statements:", hi: "निम्नलिखित कथनों पर विचार करें:" })}</p><ul class="statement-list">${q.statements.map((statement, i) => `<li><span class="statement-index">${i + 1}</span><span>${renderBilingual(statement.text || statement)}</span></li>`).join("")}</ul>`;
                            if (q.pairs) qHtml += `<div class="match-pairs">${q.pairs.map((pair, i) => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><label class="match-choice"><span>${renderBilingual(pair.right)}</span><select aria-label="Match ${i + 1}"><option value="">Choose</option>${q.pairs.map((_, n) => `<option value="${n + 1}">${n + 1}</option>`).join("")}</select></label></div>`).join("")}</div>`;
                            qHtml += `<div class="options-container">${(q.options || []).map(option => `
                            <div class="practice-option-box"><label class="opt-label"><input type="radio" name="t-${groupKey}-${q.id || qIndex}" class="opt-radio" data-correct="${option.letter === q.correctAnswer}"><span><b>${option.letter}.</b> ${renderBilingual(option.text)}</span></label></div>
                        `).join("")}</div>`;
                            qHtml += `<div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${q.correctAnswer || q.correctMapping || ""}</strong> ${renderBilingual(q.explanation)}</p></div>`;
                            qHtml += `</div></div></div>`;
                            return qHtml;
                        };
                        contentHtml = `
                        <h2>${renderBilingual({ en: "Mock Test", hi: "मॉक टेस्ट" })}</h2>
                        ${testGroups.map(([key, label]) => test[key] && test[key].length > 0 ? `<h3>${renderBilingual({ en: label, hi: ({'MCQs': 'बहुविकल्पीय प्रश्न', 'Statement Based': 'कथन आधारित', 'Match the Following': 'निम्नलिखित का मिलान करें'})[label] || label })}</h3><div class="practice-questions-container">${test[key].map((q, qIndex) => renderTestQuestion(q, qIndex, key)).join("")}</div>` : "").join("")}
                        ${testGroups.some(([key]) => test[key]?.length) ? `<div class="mock-test-submit"><button class="btn-submit-test" type="button" onclick="submitMockTest(this)">${renderBilingual({en: "Submit Test", hi: "टेस्ट जमा करें"})}</button><span class="mock-test-result" role="status"></span></div>` : `<p>${renderBilingual({en: "Test questions are not available yet.", hi: "टेस्ट के प्रश्न अभी उपलब्ध नहीं हैं।"})}</p>`}
                        ${test.mains ? `<h3>${renderBilingual({ en: "Mains Practice", hi: "मुख्य अभ्यास" })}</h3>${(Array.isArray(test.mains) ? test.mains : (test.mains.questions || [test.mains])).map(q => `<div class="mains-question-card"><h4>${renderBilingual(q.question)} ${q.marks ? `<span class="mains-marks">(${q.marks} Marks)</span>` : ""}</h4>${q.structure ? `<ul>${q.structure.map(item => `<li>${renderBilingual(item)}</li>`).join("")}</ul>` : ""}${q.modelAnswer ? `<div class="model-answer-section">${q.modelAnswer.introduction ? `<p><strong>${renderBilingual({ en: "Introduction:", hi: "परिचय:" })}</strong> ${renderBilingual(q.modelAnswer.introduction)}</p>` : ""}${q.modelAnswer.body ? `<p><strong>${renderBilingual({ en: "Body:", hi: "मुख्य भाग:" })}</strong> ${renderBilingual(q.modelAnswer.body)}</p>` : ""}${q.modelAnswer.conclusion ? `<p><strong>${renderBilingual({ en: "Conclusion:", hi: "निष्कर्ष:" })}</strong> ${renderBilingual(q.modelAnswer.conclusion)}</p>` : ""}</div>` : ""}</div>`).join("")}` : ""}
                    `;
                    }
                    break;
                default:
                    contentHtml = `<h2>${renderBilingual({ en: `Content for ${tabName}`, hi: `${tabName} के लिए सामग्री` })}</h2><p>${renderBilingual({ en: "Loading...", hi: "लोड हो रहा है..." })}</p>`;
            }

            topicContent.innerHTML = contentHtml;
            if (typeof window.renderMathInElement === "function") {
                window.SJMathsMathMarkup?.prepare(topicContent);
                window.renderMathInElement(topicContent, {
                    delimiters: [
                        { left: "$$", right: "$$", display: true },
                        { left: "$", right: "$", display: false },
                        { left: "\\(", right: "\\)", display: false },
                        { left: "\\[", right: "\\]", display: true }
                    ],
                    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "option"],
                    throwOnError: false
                });
            }
            if (tabName === "practice") {
                const subTabsBar = topicContent.querySelector('.practice-sub-tabs');
                if (subTabsBar) {
                    const subTabButtons = subTabsBar.querySelectorAll('.sub-tab-btn');
                    const subPanels = topicContent.querySelectorAll('.practice-sub-panel');

                    const activateSubTab = (targetSubtabId, shouldScroll = false) => {
                        subTabButtons.forEach(btn => {
                            const isMatch = btn.dataset.subtab === targetSubtabId;
                            btn.classList.toggle('active', isMatch);
                            btn.setAttribute('aria-selected', String(isMatch));
                        });
                        subPanels.forEach(panel => {
                            const isMatch = panel.dataset.subpanel === targetSubtabId;
                            panel.style.display = isMatch ? 'block' : 'none';
                            panel.classList.toggle('active', isMatch);
                        });
                        if (shouldScroll) {
                            const headerOffset = 90;
                            const elementPosition = subTabsBar.getBoundingClientRect().top + window.pageYOffset;
                            window.scrollTo({ top: Math.max(0, elementPosition - headerOffset), behavior: 'smooth' });
                        }
                    };

                    subTabsBar.addEventListener('click', (e) => {
                        const clickedBtn = e.target.closest('.sub-tab-btn');
                        if (clickedBtn && clickedBtn.dataset.subtab) {
                            activateSubTab(clickedBtn.dataset.subtab, false);
                        }
                    });

                    topicContent.addEventListener('click', (e) => {
                        const navBtn = e.target.closest('.practice-nav-btn');
                        if (navBtn) {
                            if (navBtn.dataset.target) {
                                activateSubTab(navBtn.dataset.target, true);
                            } else if (navBtn.dataset.targetTab) {
                                const targetTab = navBtn.dataset.targetTab;
                                const mainTabBtn = studyTabs.querySelector(`.tab-btn[data-tab="${targetTab}"]`);
                                if (mainTabBtn && mainTabBtn.style.display !== 'none') {
                                    mainTabBtn.click();
                                    const tabsPos = studyTabs.getBoundingClientRect().top + window.pageYOffset;
                                    window.scrollTo({ top: Math.max(0, tabsPos - 70), behavior: 'smooth' });
                                } else {
                                    activateSubTab(subTabButtons[0]?.dataset.subtab, true);
                                }
                            }
                        }

                        const optBox = e.target.closest('.practice-option-box');
                        if (optBox && !optBox.closest('#tab-test, .test-question-card')) {
                            const card = optBox.closest('.practice-question-card');
                            if (card) {
                                const container = optBox.closest('.options-container');
                                const solBox = card.querySelector('.sol-box');
                                let correctLetter = '';
                                if (solBox) {
                                    const solText = solBox.textContent || '';
                                    const match = solText.match(/(?:Answer|उत्तर):\s*([A-D])/i);
                                    if (match) correctLetter = match[1].toUpperCase();
                                }
                                const clickedMatch = (optBox.textContent || '').match(/([A-D])\./i);
                                const clickedLetter = clickedMatch ? clickedMatch[1].toUpperCase() : '';
                                if (container && correctLetter) {
                                    container.querySelectorAll('.practice-option-box').forEach(box => {
                                        const bm = (box.textContent || '').match(/([A-D])\./i);
                                        const bl = bm ? bm[1].toUpperCase() : '';
                                        if (bl === correctLetter) {
                                            box.classList.add('correct', 'correct-option');
                                        } else if (box === optBox && bl !== correctLetter) {
                                            box.classList.add('incorrect', 'incorrect-option');
                                        }
                                    });
                                }
                                if (solBox) solBox.style.display = 'block';
                            }
                        }
                    });
                }
            }

            if (tabName === "test") {
                const testSubTabsBar = topicContent.querySelector('.test-sub-tabs');
                if (testSubTabsBar) {
                    const subTabButtons = testSubTabsBar.querySelectorAll('.sub-tab-btn');
                    const subPanels = topicContent.querySelectorAll('.test-sub-panel');

                    const activateTestSubTab = (targetSubtabId, shouldScroll = false) => {
                        subTabButtons.forEach(btn => {
                            const isMatch = btn.dataset.testSubtab === targetSubtabId;
                            btn.classList.toggle('active', isMatch);
                            btn.setAttribute('aria-selected', String(isMatch));
                        });
                        subPanels.forEach(panel => {
                            const isMatch = panel.dataset.testSubpanel === targetSubtabId;
                            panel.style.display = isMatch ? 'block' : 'none';
                            panel.classList.toggle('active', isMatch);
                        });
                        if (shouldScroll) {
                            const headerOffset = 90;
                            const elementPosition = testSubTabsBar.getBoundingClientRect().top + window.pageYOffset;
                            window.scrollTo({ top: Math.max(0, elementPosition - headerOffset), behavior: 'smooth' });
                        }
                    };

                    testSubTabsBar.addEventListener('click', (e) => {
                        const clickedBtn = e.target.closest('.sub-tab-btn');
                        if (clickedBtn && clickedBtn.dataset.testSubtab) {
                            activateTestSubTab(clickedBtn.dataset.testSubtab, false);
                        }
                    });

                    topicContent.addEventListener('click', (e) => {
                        const navBtn = e.target.closest('.practice-nav-btn');
                        if (navBtn) {
                            if (navBtn.dataset.testTarget) {
                                activateTestSubTab(navBtn.dataset.testTarget, true);
                            } else if (navBtn.dataset.targetTab) {
                                const targetTab = navBtn.dataset.targetTab;
                                const mainTabBtn = studyTabs.querySelector(`.tab-btn[data-tab="${targetTab}"]`);
                                if (mainTabBtn && mainTabBtn.style.display !== 'none') {
                                    mainTabBtn.click();
                                    const tabsPos = studyTabs.getBoundingClientRect().top + window.pageYOffset;
                                    window.scrollTo({ top: Math.max(0, tabsPos - 70), behavior: 'smooth' });
                                }
                            }
                        }

                        const submitBtn = e.target.closest('.btn-submit-level-test');
                        if (submitBtn) {
                            const level = submitBtn.dataset.level;
                            const panel = topicContent.querySelector(`.test-sub-panel[data-test-subpanel="test-${level}"]`);
                            if (panel) {
                                const cards = panel.querySelectorAll('.test-question-card');
                                if (!cards.length) return;
                                panel.classList.add('level-test-submitted');
                                let score = 0, answered = 0;
                                cards.forEach(card => {
                                    const checked = card.querySelector('input[type=radio]:checked');
                                    const solBox = card.querySelector('.sol-box');
                                    if (solBox) solBox.style.display = 'block';

                                    if (checked) {
                                        answered++;
                                        const isCorrect = checked.dataset.correct === 'true';
                                        if (isCorrect) score++;
                                    }
                                    card.querySelectorAll('.test-option-box').forEach(box => {
                                        const input = box.querySelector('input[type=radio]');
                                        if (input) {
                                            input.disabled = true;
                                            if (input.dataset.correct === 'true') {
                                                box.classList.add('correct', 'correct-option', 'answer-correct');
                                            } else if (input.checked && input.dataset.correct !== 'true') {
                                                box.classList.add('incorrect', 'incorrect-option', 'answer-wrong');
                                            }
                                        }
                                    });
                                });

                                const pct = Math.round((score / cards.length) * 100);
                                let badgeClass = 'score-avg';
                                let remark = { en: "Good Effort!", hi: "अच्छा प्रयास!" };
                                if (pct >= 70) {
                                    badgeClass = 'score-pass';
                                    remark = { en: "Excellent!", hi: "शानदार प्रदर्शन!" };
                                } else if (pct < 40) {
                                    badgeClass = 'score-fail';
                                    remark = { en: "Needs Revision", hi: "पुनरीक्षण आवश्यक" };
                                }

                                const scoreBadge = panel.querySelector(`#score-badge-${level}`);
                                if (scoreBadge) {
                                    scoreBadge.className = `test-level-score-badge ${badgeClass}`;
                                    scoreBadge.style.display = 'inline-flex';
                                    scoreBadge.innerHTML = `
                                        <span><b>${score} / ${cards.length}</b> ${renderBilingual({ en: "Correct", hi: "सही" })} (${pct}%)</span>
                                        <span class="score-remark">— ${renderBilingual(remark)}</span>
                                    `;
                                }

                                submitBtn.disabled = true;
                                submitBtn.innerHTML = `<i class="fas fa-check-double"></i> ${renderBilingual({ en: "Test Submitted", hi: "टेस्ट जमा हो गया" })}`;
                            }
                        }
                    });
                }
            }

            const tabButtons = [...studyTabs.querySelectorAll('.tab-btn:not([style*="display: none"])')];
            const currentIndex = tabButtons.findIndex(button => button.dataset.tab.replace('tab-', '') === tabName);
            const previous = currentIndex > 0 ? tabButtons[currentIndex - 1] : null;
            const next = currentIndex >= 0 && currentIndex < tabButtons.length - 1 ? tabButtons[currentIndex + 1] : null;
            const nav = document.createElement('nav');
            nav.className = 'study-tab-footer';
            nav.setAttribute('aria-label', 'Study tab navigation');
            nav.innerHTML = `<button type="button" class="tab-nav-btn prev" ${previous ? '' : 'disabled'}><span>←</span><small>${renderBilingual({en: "Previous", hi: "पिछला"})}</small><strong>${previous ? previous.innerHTML : renderBilingual({en: 'Start', hi: 'शुरुआत'})}</strong></button><span class="tab-nav-progress">${Math.max(currentIndex + 1, 1)} / ${tabButtons.length}</span><button type="button" class="tab-nav-btn next" ${next ? '' : 'disabled'}><small>${renderBilingual({en: "Next", hi: "अगला"})}</small><strong>${next ? next.innerHTML : renderBilingual({en: 'Complete', hi: 'समाप्त'})}</strong><span>→</span></button>`;
            nav.querySelector('.prev')?.addEventListener('click', () => previous?.click());
            nav.querySelector('.next')?.addEventListener('click', () => next?.click());
            topicContent.appendChild(nav);
        };

        studyTabs.addEventListener("click", (event) => {
            const clickedButton = event.target.closest(".tab-btn");
            if (!clickedButton) return;

            // Remove "active" from all buttons
            studyTabs.querySelectorAll(".tab-btn").forEach(btn => {
                btn.classList.remove("active");
                btn.setAttribute("aria-selected", "false");
            });

            // Add "active" to clicked button
            clickedButton.classList.add("active");
            clickedButton.setAttribute("aria-selected", "true");

            const tabName = clickedButton.dataset.tab.replace("tab-", "");
            try { localStorage.setItem(`upsc-tab:${location.pathname}`, tabName); } catch (e) { }
            renderTabContent(tabName);
        });

        // Initial render for the active tab (Overview by default)
        let savedTab = null;
        try { savedTab = localStorage.getItem(`upsc-tab:${location.pathname}`); } catch (e) { }
        const savedButton = savedTab && studyTabs.querySelector(`.tab-btn[data-tab="tab-${savedTab}"]`);
        const initialTab = savedButton || studyTabs.querySelector(".tab-btn.active");
        if (initialTab) {
            studyTabs.querySelectorAll('.tab-btn').forEach(btn => { btn.classList.toggle('active', btn === initialTab); btn.setAttribute('aria-selected', String(btn === initialTab)); });
            const tabName = initialTab.dataset.tab.replace("tab-", "");
            renderTabContent(tabName);
        } else {
            renderTabContent("overview");
        }

        // Handle Mains tab visibility
        const mainsTabButton = document.getElementById("mains-tab-btn");
        if (mainsTabButton) {
            mainsTabButton.style.display = pageData.supportsMains ? "" : "none";
        }
    } catch (err) {
        console.error('UPSC renderer caught error:', err);
        try { document.getElementById('topic-content').innerHTML = '<div style="padding:1rem;color:#b91c1c;background:#fff7f7;border:1px solid #fecaca;border-radius:8px">Rendering failed — check console for details.</div>'; } catch (e) { }
    }
});
document.addEventListener("DOMContentLoaded",()=>{const e=document.querySelector('.topic-desc');e&&/\bundefined\b/i.test(e.textContent.trim())&&e.remove()});
const formatQuestionLevel = value => `${String(value || "").charAt(0).toUpperCase()}${String(value || "").slice(1).toLowerCase()}`;

function submitMockTest(button) {
    const root = button.closest('.topic-content');
    const cards = root.querySelectorAll('.test-question-card');
    if (!cards.length) return;
    root.classList.add('mock-test-submitted');
    let score = 0, answered = 0;
    cards.forEach(card => {
        const selected = card.querySelector('input[type=radio]:checked');
        if (selected) { answered++; if (selected.dataset.correct === 'true') score++; }
    });
    const result = root.querySelector('.mock-test-result');
    if (result) result.innerHTML = `<span class="lang-en">${score} / ${cards.length} correct — ${answered} answered</span><span class="lang-hi">${score} / ${cards.length} सही — ${answered} उत्तर दिए</span>`;
    button.disabled = true;
    button.innerHTML = '<span class="lang-en">Test Submitted</span><span class="lang-hi">टेस्ट जमा हो गया</span>';
}
