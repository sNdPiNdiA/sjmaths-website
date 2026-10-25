document.addEventListener("DOMContentLoaded", async () => {
    try {
        const studyTabs = document.querySelector(".study-tabs");
        const topicContent = document.getElementById("topic-content");
        const pageDataScript = document.getElementById("upsc-page-data");

        if (!studyTabs || !topicContent || !pageDataScript) {
            console.error("Missing essential elements for UPSC renderer.");
            return;
        }

        if (!document.getElementById("upsc-consolidated-study-styles")) {
            const style = document.createElement("style");
            style.id = "upsc-consolidated-study-styles";
            style.textContent = `
                .study-overview-card {
                    background: #ffffff;
                    border: 1px solid #e2e8f0;
                    border-radius: 16px;
                    padding: 2rem;
                    margin-bottom: 2rem;
                    box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
                }
                .study-card-badge {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    background: #f0fdf4;
                    border: 1px solid #bbf7d0;
                    color: #166534;
                    font-size: 0.75rem;
                    font-weight: 700;
                    letter-spacing: 0.05em;
                    text-transform: uppercase;
                    padding: 0.3rem 0.8rem;
                    border-radius: 9999px;
                    margin-bottom: 1rem;
                }
                .study-main-title {
                    font-size: 1.85rem;
                    font-weight: 800;
                    color: #0f172a;
                    line-height: 1.3;
                    margin: 0 0 1rem 0;
                }
                .study-lead-definition {
                    font-size: 1.1rem;
                    line-height: 1.7;
                    color: #475569;
                    margin-bottom: 1.5rem;
                }
                .study-meta-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 1.25rem;
                    margin: 1.5rem 0;
                }
                .study-meta-item {
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 1.25rem;
                }
                .study-meta-item h4 {
                    margin: 0 0 0.5rem 0;
                    font-size: 0.95rem;
                    font-weight: 700;
                    color: #0f766e;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }
                .study-meta-item p, .study-meta-item ul {
                    margin: 0;
                    font-size: 0.92rem;
                    line-height: 1.6;
                    color: #334155;
                }
                .study-meta-item ul {
                    padding-left: 1.25rem;
                }
                .study-prereq-bar {
                    display: flex;
                    flex-wrap: wrap;
                    align-items: center;
                    gap: 0.5rem;
                    margin-top: 1.25rem;
                    padding-top: 1rem;
                    border-top: 1px dashed #e2e8f0;
                }
                .prereq-label {
                    font-size: 0.85rem;
                    font-weight: 700;
                    color: #64748b;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.35rem;
                }
                .prereq-chips {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0.4rem;
                }
                .prereq-chip {
                    background: #f1f5f9;
                    border: 1px solid #e2e8f0;
                    padding: 0.2rem 0.65rem;
                    border-radius: 9999px;
                    font-size: 0.82rem;
                    font-weight: 600;
                    color: #334155;
                }
                .study-section-wrapper {
                    margin-top: 2.5rem;
                    padding-top: 1.75rem;
                    border-top: 1px solid #e2e8f0;
                }
                .study-section-header {
                    margin-bottom: 1.5rem;
                }
                .section-pill {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.4rem;
                    font-size: 0.75rem;
                    font-weight: 700;
                    text-transform: uppercase;
                    letter-spacing: 0.06em;
                    padding: 0.25rem 0.75rem;
                    border-radius: 9999px;
                    background: #e0f2fe;
                    color: #0369a1;
                    margin-bottom: 0.5rem;
                }
                .study-section-header h2 {
                    font-size: 1.45rem;
                    font-weight: 800;
                    color: #0f172a;
                    margin: 0;
                }
                .visual-block-card {
                    background: #ffffff;
                    border: 1px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 1.5rem;
                    margin-bottom: 1.5rem;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
                }
                .visual-block-card h4 {
                    margin: 0 0 1rem 0;
                    font-size: 1.1rem;
                    font-weight: 700;
                    color: #1e293b;
                }
                .study-takeaways-card {
                    background: linear-gradient(135deg, #f0fdf4 0%, #ecfdf5 100%);
                    border: 1px solid #bbf7d0;
                    border-radius: 14px;
                    padding: 1.5rem;
                }
                .study-takeaways-card ul {
                    margin: 0;
                    padding-left: 1.25rem;
                }
                .study-takeaways-card li {
                    margin-bottom: 0.6rem;
                    font-size: 0.95rem;
                    line-height: 1.6;
                    color: #166534;
                }
                .study-action-card {
                    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                    border-radius: 16px;
                    padding: 2rem;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    gap: 1.5rem;
                    flex-wrap: wrap;
                    margin-top: 3rem;
                    margin-bottom: 1.5rem;
                    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
                    border: 1px solid rgba(255, 255, 255, 0.1);
                }
                .action-card-content {
                    display: flex;
                    align-items: center;
                    gap: 1.25rem;
                    flex: 1 1 300px;
                }
                .action-icon {
                    width: 52px;
                    height: 52px;
                    border-radius: 12px;
                    background: rgba(255, 255, 255, 0.1);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.4rem;
                    color: #38bdf8;
                    flex-shrink: 0;
                }
                body.exam-ui .topic-content .study-action-card .action-text :is(h2,h3,h4),
                body .study-action-card .action-text :is(h2,h3,h4) {
                    color: #ffffff !important;
                    font-size: 1.25rem !important;
                    font-weight: 700 !important;
                    margin: 0 0 0.35rem 0 !important;
                }
                body.exam-ui .topic-content .study-action-card .action-text p,
                body .study-action-card .action-text p {
                    color: #cbd5e1 !important;
                    font-size: 0.95rem !important;
                    margin: 0 !important;
                    line-height: 1.5 !important;
                }
                body.exam-ui .topic-content .study-meta-item h4 {
                    color: #0f766e !important;
                }
                body.exam-ui .topic-content .visual-block-card h4 {
                    color: #1e293b !important;
                }
                .btn-proceed-practice {
                    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
                    color: #ffffff !important;
                    border: none;
                    padding: 0.9rem 1.75rem;
                    border-radius: 10px;
                    font-weight: 700;
                    font-size: 1rem;
                    display: inline-flex;
                    align-items: center;
                    gap: 0.6rem;
                    cursor: pointer;
                    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
                    transition: all 0.2s ease;
                    white-space: nowrap;
                }
                .btn-proceed-practice:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.45);
                    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
                }

                /* Dark mode styling */
                body.dark-mode .study-overview-card,
                [data-theme="dark"] .study-overview-card {
                    background: #1e293b;
                    border-color: #334155;
                    box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.3);
                }
                body.dark-mode .study-main-title,
                [data-theme="dark"] .study-main-title {
                    color: #f8fafc;
                }
                body.dark-mode .study-lead-definition,
                [data-theme="dark"] .study-lead-definition {
                    color: #cbd5e1;
                }
                body.dark-mode .study-meta-item,
                [data-theme="dark"] .study-meta-item {
                    background: #0f172a;
                    border-color: #334155;
                }
                body.dark-mode .study-meta-item p,
                body.dark-mode .study-meta-item ul,
                [data-theme="dark"] .study-meta-item p,
                [data-theme="dark"] .study-meta-item ul {
                    color: #94a3b8;
                }
                body.dark-mode .prereq-chip,
                [data-theme="dark"] .prereq-chip {
                    background: #334155;
                    border-color: #475569;
                    color: #e2e8f0;
                }
                body.dark-mode .study-section-wrapper,
                [data-theme="dark"] .study-section-wrapper {
                    border-top-color: #334155;
                }
                body.dark-mode .study-section-header h2,
                [data-theme="dark"] .study-section-header h2 {
                    color: #f8fafc;
                }
                body.dark-mode .visual-block-card,
                [data-theme="dark"] .visual-block-card {
                    background: #1e293b;
                    border-color: #334155;
                }
                body.dark-mode .visual-block-card h4,
                [data-theme="dark"] .visual-block-card h4 {
                    color: #f8fafc;
                }
                body.dark-mode .study-takeaways-card,
                [data-theme="dark"] .study-takeaways-card {
                    background: rgba(16, 185, 129, 0.12);
                    border-color: rgba(16, 185, 129, 0.3);
                }
                body.dark-mode .study-takeaways-card li,
                [data-theme="dark"] .study-takeaways-card li {
                    color: #86efac;
                }

                /* Related topics card language toggle enforcement */
                html.lang-hi .related-topics-card .lang-hi,
                body.lang-hi .related-topics-card .lang-hi,
                body.lang-mode-hi .related-topics-card .lang-hi,
                html.lang-hi .related-topic-group .lang-hi,
                body.lang-hi .related-topic-group .lang-hi,
                body.lang-mode-hi .related-topic-group .lang-hi {
                    display: inline !important;
                }
                html.lang-hi .related-topics-card .lang-en,
                body.lang-hi .related-topics-card .lang-en,
                body.lang-mode-hi .related-topics-card .lang-en,
                html.lang-hi .related-topic-group .lang-en,
                body.lang-hi .related-topic-group .lang-en,
                body.lang-mode-hi .related-topic-group .lang-en {
                    display: none !important;
                }
                html.lang-en .related-topics-card .lang-en,
                body.lang-en .related-topics-card .lang-en,
                body:not(.lang-hi):not(.lang-mode-hi) .related-topics-card .lang-en,
                html.lang-en .related-topic-group .lang-en,
                body.lang-en .related-topic-group .lang-en,
                body:not(.lang-hi):not(.lang-mode-hi) .related-topic-group .lang-en {
                    display: inline !important;
                }
                html.lang-en .related-topics-card .lang-hi,
                body.lang-en .related-topics-card .lang-hi,
                body:not(.lang-hi):not(.lang-mode-hi) .related-topics-card .lang-hi,
                html.lang-en .related-topic-group .lang-hi,
                body.lang-en .related-topic-group .lang-hi,
                body:not(.lang-hi):not(.lang-mode-hi) .related-topic-group .lang-hi {
                    display: none !important;
                }
            `;
            document.head.appendChild(style);
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
        const tabDataKeys = ["notes", "practice", "revision", "mains", "test", "overview", "concepts", "visual", "comparisons", "pyqs"];

        const loadTabData = async () => {
            const basePath = window.location.pathname.replace(/\/?index\.html$/, "/").replace(/\/?$/, "/");

            // 1. First attempt: load consolidated tabs.json (fastest, single HTTP request)
            try {
                const response = await fetch(`${basePath}tabs.json`, { cache: "no-cache" });
                if (response.ok) {
                    const tabsData = await response.json();
                    if (tabsData && typeof tabsData === "object") {
                        if (tabsData.notes && typeof tabsData.notes === "object") {
                            pageData.notes = tabsData.notes;
                            if (tabsData.notes.overview) pageData.overview = tabsData.notes.overview;
                            if (tabsData.notes.concepts) pageData.concepts = tabsData.notes.concepts;
                            if (tabsData.notes.visual) pageData.visual = tabsData.notes.visual;
                            if (tabsData.notes.comparisons) pageData.comparisons = tabsData.notes.comparisons;
                        }
                        if (tabsData.practice !== undefined) pageData.practice = tabsData.practice;
                        if (tabsData.revision !== undefined) pageData.revision = tabsData.revision;
                        if (tabsData.mains !== undefined) pageData.mains = tabsData.mains;
                        if (tabsData.test !== undefined) pageData.test = tabsData.test;
                        return;
                    }
                }
            } catch (e) {
                // Fall back to individual tab files below
            }

            // 2. Fallback: load individual tab files if tabs.json is absent
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
                if (key === "notes" && value && typeof value === "object") {
                    pageData.notes = value;
                    if (value.overview) pageData.overview = value.overview;
                    if (value.concepts) pageData.concepts = value.concepts;
                    if (value.visual) pageData.visual = value.visual;
                    if (value.comparisons) pageData.comparisons = value.comparisons;
                } else {
                    pageData[key] = value;
                }
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
                const enStr = mdToHtml(tryFixEncoding(obj.en || obj.hi || ""));
                const hiStr = mdToHtml(tryFixEncoding(obj.hi || obj.en || ""));
                return `<span class="lang-en">${enStr}</span><span class="lang-hi">${hiStr}</span>`;
            }
            return "";
        };

        const parseStatementQuestion = (questionObj) => {
            if (!questionObj) return null;

            const enText = typeof questionObj === 'string' ? questionObj : (questionObj.en || '');
            const hiText = typeof questionObj === 'string' ? '' : (questionObj.hi || '');

            const hasStatements = /(?:^|\n|:\s*|\.\s+)(?:1|१)[\.\)]\s+[\s\S]+?(?:2|२)[\.\)]\s+/;
            if (!hasStatements.test(enText) && !hasStatements.test(hiText)) {
                return null;
            }

            const splitParts = (text) => {
                if (!text) return { intro: '', statements: [], prompt: '' };

                const firstNumMatch = text.match(/(?:^|\n|:\s*|\.\s+)([1-4१-४])[\.\)]\s+/);
                if (!firstNumMatch) return { intro: text, statements: [], prompt: '' };

                const firstNumIdx = text.indexOf(firstNumMatch[0]);
                let intro = text.slice(0, firstNumIdx + (firstNumMatch[0].startsWith(':') || firstNumMatch[0].startsWith('.') ? 1 : 0)).trim();

                const promptRegex = /(?:\n|\.\s+)(which of the (?:statements|pairs|above)|ऊपर दिए गए|उपरोक्त|इनमें से कौन|निम्न में से कौन)[\s\S]*$/i;
                let statementsBody = text.slice(firstNumIdx + firstNumMatch[0].length);
                let prompt = '';

                const promptMatch = statementsBody.match(promptRegex);
                if (promptMatch) {
                    prompt = statementsBody.slice(promptMatch.index).trim().replace(/^\.?\s*/, '');
                    statementsBody = statementsBody.slice(0, promptMatch.index).trim();
                }

                const numRegex = /(?:^|\n|\.\s+)(?:[2-9२-९])[\.\)]\s+/g;
                let rawStatements = [];
                let lastIndex = 0;
                let m;
                while ((m = numRegex.exec(statementsBody)) !== null) {
                    const stmt = statementsBody.slice(lastIndex, m.index).trim().replace(/\.$/, '');
                    if (stmt) rawStatements.push(stmt);
                    lastIndex = m.index + m[0].length;
                }
                const finalStmt = statementsBody.slice(lastIndex).trim().replace(/\.$/, '');
                if (finalStmt) rawStatements.push(finalStmt);

                return { intro, statements: rawStatements, prompt };
            };

            const enParts = splitParts(enText);
            const hiParts = splitParts(hiText);

            const maxLen = Math.max(enParts.statements.length, hiParts.statements.length);
            if (maxLen < 2) return null;

            const statements = [];
            for (let i = 0; i < maxLen; i++) {
                statements.push({
                    en: enParts.statements[i] || '',
                    hi: hiParts.statements[i] || ''
                });
            }

            return {
                intro: { en: enParts.intro, hi: hiParts.intro },
                statements,
                prompt: { en: enParts.prompt, hi: hiParts.prompt }
            };
        };

        const renderQuestionContent = (q) => {
            let html = "";
            if (q.statements && Array.isArray(q.statements) && q.statements.length > 0) {
                if (q.question) html += `<p class="q-text-sm q-intro-text">${renderBilingual(q.question)}</p>`;
                html += `<ol class="statement-list">${q.statements.map((s, i) => `<li class="statement-item"><span class="statement-index">${i + 1}</span><span class="statement-text">${renderBilingual(s.text || s)}</span></li>`).join("")}</ol>`;
            } else {
                const parsed = parseStatementQuestion(q.question);
                if (parsed) {
                    if (parsed.intro && (parsed.intro.en || parsed.intro.hi)) {
                        html += `<p class="q-text-sm q-intro-text">${renderBilingual(parsed.intro)}</p>`;
                    }
                    html += `<ol class="statement-list">${parsed.statements.map((s, i) => `<li class="statement-item"><span class="statement-index">${i + 1}</span><span class="statement-text">${renderBilingual(s)}</span></li>`).join("")}</ol>`;
                    if (parsed.prompt && (parsed.prompt.en || parsed.prompt.hi)) {
                        html += `<p class="q-text-sm q-prompt-text">${renderBilingual(parsed.prompt)}</p>`;
                    }
                } else if (q.question) {
                    html += `<p class="q-text-sm">${renderBilingual(q.question)}</p>`;
                }
            }
            if (q.assertion) {
                html += `<p class="q-text-sm"><strong><span class="lang-en">Assertion (A):</span><span class="lang-hi">अभिकथन (A):</span></strong> ${renderBilingual(q.assertion)}</p>`;
                html += `<p class="q-text-sm"><strong><span class="lang-en">Reason (R):</span><span class="lang-hi">कारण (R):</span></strong> ${renderBilingual(q.reason)}</p>`;
            }
            if (q.pairs) {
                html += `<div class="match-pairs">${q.pairs.map((pair, i) => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><label class="match-choice"><span>${renderBilingual(pair.right)}</span><select aria-label="Match ${i + 1}"><option value="">Choose</option>${q.pairs.map((_, n) => `<option value="${n + 1}">${n + 1}</option>`).join("")}</select></label></div>`).join("")}</div>`;
            }
            return html;
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
                .study-overview-card {
                    background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 250, 252, 0.95) 100%);
                    border: 1px solid rgba(212, 175, 55, 0.28);
                    border-radius: 20px;
                    padding: 2rem 2.2rem;
                    margin: 0.5rem 0 2rem;
                    box-shadow: 0 12px 36px -10px rgba(0, 0, 0, 0.06), 0 4px 16px rgba(212, 175, 55, 0.08);
                }
                body.dark-mode .study-overview-card {
                    background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%);
                    border-color: rgba(212, 175, 55, 0.35);
                    color: #f8fafc;
                }
                .study-card-badge {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    background: linear-gradient(135deg, rgba(212, 175, 55, 0.15) 0%, rgba(245, 158, 11, 0.18) 100%);
                    color: #b45309;
                    border: 1px solid rgba(212, 175, 55, 0.4);
                    font-size: 0.8rem;
                    font-weight: 800;
                    text-transform: uppercase;
                    letter-spacing: 0.06em;
                    padding: 0.35rem 0.85rem;
                    border-radius: 999px;
                    margin-bottom: 1.1rem;
                }
                body.dark-mode .study-card-badge {
                    color: #fde68a;
                    border-color: rgba(212, 175, 55, 0.5);
                }
                .study-main-title {
                    font-family: 'Outfit', 'Inter', sans-serif;
                    font-size: 1.85rem;
                    font-weight: 800;
                    color: #0f172a;
                    line-height: 1.3;
                    margin: 0 0 1rem;
                }
                body.dark-mode .study-main-title {
                    color: #f8fafc;
                }
                .study-lead-definition {
                    font-size: 1.08rem;
                    line-height: 1.75;
                    color: #334155;
                    margin-bottom: 1.75rem;
                    font-weight: 450;
                }
                body.dark-mode .study-lead-definition {
                    color: #cbd5e1;
                }
                .study-meta-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 1.25rem;
                    margin-bottom: 1.25rem;
                }
                .study-meta-item {
                    background: rgba(241, 245, 249, 0.65);
                    border: 1px solid rgba(226, 232, 240, 0.9);
                    border-radius: 14px;
                    padding: 1.2rem 1.35rem;
                }
                body.dark-mode .study-meta-item {
                    background: rgba(30, 41, 59, 0.5);
                    border-color: rgba(51, 65, 85, 0.8);
                }
                .study-meta-item h4 {
                    font-family: 'Outfit', sans-serif;
                    font-size: 0.98rem;
                    font-weight: 700;
                    color: #0f172a;
                    margin: 0 0 0.6rem;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }
                body.dark-mode .study-meta-item h4 {
                    color: #f8fafc;
                }
                .study-meta-item h4 i {
                    color: #2563eb;
                }
                body.dark-mode .study-meta-item h4 i {
                    color: #60a5fa;
                }
                .study-meta-item p {
                    font-size: 0.94rem;
                    line-height: 1.65;
                    color: #475569;
                    margin: 0;
                }
                body.dark-mode .study-meta-item p {
                    color: #cbd5e1;
                }
                .study-meta-item ul {
                    margin: 0.5rem 0 0 !important;
                    gap: 0.45rem !important;
                }
                .study-meta-item ul li {
                    padding: 0.65rem 0.9rem 0.65rem 2.2rem !important;
                    font-size: 0.9rem !important;
                    line-height: 1.5 !important;
                    border-radius: 8px !important;
                }
                .study-meta-item ul li::before {
                    left: 0.75rem !important;
                    top: 0.65rem !important;
                    font-size: 0.85rem !important;
                }
                .study-prereq-bar {
                    display: flex;
                    align-items: center;
                    flex-wrap: wrap;
                    gap: 0.6rem;
                    padding-top: 1rem;
                    border-top: 1px dashed rgba(203, 213, 225, 0.8);
                }
                body.dark-mode .study-prereq-bar {
                    border-top-color: rgba(51, 65, 85, 0.7);
                }
                .prereq-label {
                    font-size: 0.86rem;
                    font-weight: 700;
                    color: #64748b;
                    display: flex;
                    align-items: center;
                    gap: 0.4rem;
                }
                body.dark-mode .prereq-label {
                    color: #94a3b8;
                }
                .prereq-chips {
                    display: flex;
                    flex-wrap: wrap;
                    gap: 0.45rem;
                }
                .prereq-chip {
                    background: rgba(226, 232, 240, 0.7);
                    border: 1px solid rgba(203, 213, 225, 0.9);
                    border-radius: 999px;
                    padding: 0.2rem 0.65rem;
                    font-size: 0.82rem;
                    color: #334155;
                }
                body.dark-mode .prereq-chip {
                    background: rgba(51, 65, 85, 0.6);
                    border-color: rgba(71, 85, 105, 0.8);
                    color: #cbd5e1;
                }
                .study-section-wrapper {
                    margin: 2.2rem 0;
                    padding-top: 1.5rem;
                    border-top: 1px solid rgba(226, 232, 240, 0.8);
                }
                body.dark-mode .study-section-wrapper {
                    border-top-color: rgba(51, 65, 85, 0.8);
                }
                .study-section-header {
                    margin-bottom: 1.25rem;
                }
                .section-pill {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.4rem;
                    font-size: 0.78rem;
                    font-weight: 800;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                    color: #2563eb;
                    background: rgba(37, 99, 235, 0.08);
                    border: 1px solid rgba(37, 99, 235, 0.2);
                    border-radius: 999px;
                    padding: 0.25rem 0.65rem;
                    margin-bottom: 0.45rem;
                }
                body.dark-mode .section-pill {
                    color: #60a5fa;
                    background: rgba(37, 99, 235, 0.2);
                    border-color: rgba(96, 165, 250, 0.3);
                }
                .study-section-header h2 {
                    font-family: 'Outfit', 'Inter', sans-serif;
                    font-size: 1.5rem;
                    font-weight: 700;
                    color: #0f172a;
                    margin: 0;
                }
                body.dark-mode .study-section-header h2 {
                    color: #f8fafc;
                }
                .concept-section-block {
                    margin-bottom: 1.8rem;
                }
                .concept-section-block h3 {
                    font-family: 'Outfit', 'Inter', sans-serif;
                    font-size: 1.25rem;
                    font-weight: 700;
                    color: #1e293b;
                    margin: 1.3rem 0 0.8rem;
                }
                body.dark-mode .concept-section-block h3 {
                    color: #f1f5f9;
                }
                .visual-block-card {
                    background: rgba(255, 255, 255, 0.95);
                    border: 1px solid rgba(212, 175, 55, 0.25);
                    border-radius: 16px;
                    padding: 1.5rem;
                    margin-bottom: 1.5rem;
                    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
                }
                body.dark-mode .visual-block-card {
                    background: rgba(15, 23, 42, 0.85);
                    border-color: rgba(212, 175, 55, 0.3);
                }
                .visual-block-card h4 {
                    font-family: 'Outfit', sans-serif;
                    font-size: 1.15rem;
                    font-weight: 700;
                    color: #0f172a;
                    margin: 0 0 1rem;
                }
                body.dark-mode .visual-block-card h4 {
                    color: #f8fafc;
                }
                .study-takeaways-card {
                    background: linear-gradient(135deg, rgba(16, 185, 129, 0.06) 0%, rgba(255, 255, 255, 0.95) 100%);
                    border: 1px solid rgba(16, 185, 129, 0.28);
                    border-radius: 18px;
                    padding: 1.5rem 1.8rem;
                    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.05);
                }
                body.dark-mode .study-takeaways-card {
                    background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(15, 23, 42, 0.9) 100%);
                    border-color: rgba(16, 185, 129, 0.35);
                }
                .study-action-card {
                    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
                    border-radius: 20px;
                    padding: 1.8rem 2.2rem;
                    margin: 2.5rem 0 1.5rem;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 1.5rem;
                    flex-wrap: wrap;
                    box-shadow: 0 16px 40px -10px rgba(15, 23, 42, 0.35);
                }
                .action-card-content {
                    display: flex;
                    align-items: center;
                    gap: 1.25rem;
                }
                .action-icon {
                    width: 52px;
                    height: 52px;
                    border-radius: 14px;
                    background: rgba(59, 130, 246, 0.2);
                    border: 1px solid rgba(59, 130, 246, 0.4);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 1.35rem;
                    color: #60a5fa;
                    flex-shrink: 0;
                }
                .action-text h3 {
                    font-family: 'Outfit', sans-serif;
                    font-size: 1.2rem;
                    font-weight: 700;
                    color: #ffffff;
                    margin: 0 0 0.3rem;
                }
                .action-text p {
                    font-size: 0.92rem;
                    color: #cbd5e1;
                    margin: 0;
                    line-height: 1.5;
                }
                .btn-proceed-practice {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.65rem;
                    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
                    color: #ffffff;
                    border: 1px solid rgba(255, 255, 255, 0.2);
                    border-radius: 12px;
                    padding: 0.85rem 1.5rem;
                    font-family: 'Outfit', sans-serif;
                    font-size: 0.98rem;
                    font-weight: 700;
                    cursor: pointer;
                    transition: all 0.25s ease;
                    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35);
                    flex-shrink: 0;
                }
                .btn-proceed-practice:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 12px 28px rgba(37, 99, 235, 0.5);
                    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
                }
                /* Concept Flow & Progression Cards (Study Notes Visual Enhancements) */
                .concept-flow-card {
                    background: #ffffff;
                    border: 1px solid #e2e8f0;
                    border-radius: 14px;
                    padding: 1.25rem 1.5rem;
                    margin: 1.5rem 0;
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
                    transition: transform 0.2s ease, box-shadow 0.2s ease;
                }
                .concept-flow-card:hover {
                    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.07);
                }
                body.dark-mode .concept-flow-card {
                    background: #1e293b !important;
                    border-color: #334155 !important;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
                }
                .concept-flow-header {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 1rem;
                    padding-bottom: 0.5rem;
                    border-bottom: 1px dashed #e2e8f0;
                }
                body.dark-mode .concept-flow-header {
                    border-bottom-color: #334155;
                }
                .concept-flow-header .flow-pill {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.4rem;
                    font-size: 0.78rem;
                    font-weight: 700;
                    text-transform: uppercase;
                    letter-spacing: 0.04em;
                    color: #047857;
                    background: rgba(4, 120, 87, 0.08);
                    border: 1px solid rgba(4, 120, 87, 0.2);
                    border-radius: 999px;
                    padding: 0.2rem 0.65rem;
                }
                body.dark-mode .concept-flow-header .flow-pill {
                    color: #34d399;
                    background: rgba(52, 211, 153, 0.12);
                    border-color: rgba(52, 211, 153, 0.3);
                }
                .concept-flow-track {
                    display: flex;
                    align-items: center;
                    justify-content: space-around;
                    gap: 0.75rem;
                    flex-wrap: wrap;
                }
                .flow-node {
                    display: flex;
                    align-items: center;
                    gap: 0.65rem;
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 10px;
                    padding: 0.65rem 0.95rem;
                    min-width: 140px;
                    flex: 1 1 auto;
                    transition: border-color 0.2s ease, background 0.2s ease;
                }
                body.dark-mode .flow-node {
                    background: #0f172a !important;
                    border-color: #334155 !important;
                }
                .flow-node.highlight {
                    border-color: #047857;
                    background: rgba(4, 120, 87, 0.05);
                }
                body.dark-mode .flow-node.highlight {
                    border-color: #34d399;
                    background: rgba(52, 211, 153, 0.08) !important;
                }
                .flow-node-index {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 28px;
                    height: 28px;
                    border-radius: 50%;
                    background: #047857;
                    color: #ffffff;
                    font-size: 0.75rem;
                    font-weight: 700;
                    flex-shrink: 0;
                }
                .flow-node.highlight .flow-node-index {
                    background: #2563eb;
                }
                .flow-node-content {
                    display: flex;
                    flex-direction: column;
                }
                .flow-node-title {
                    font-weight: 700;
                    font-size: 0.92rem;
                    color: #1e293b;
                    line-height: 1.25;
                }
                body.dark-mode .flow-node-title {
                    color: #f1f5f9;
                }
                .flow-node-sub {
                    font-size: 0.75rem;
                    color: #64748b;
                    margin-top: 0.15rem;
                }
                body.dark-mode .flow-node-sub {
                    color: #94a3b8;
                }
                .flow-connector {
                    color: #94a3b8;
                    font-size: 1rem;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-shrink: 0;
                }
                body.dark-mode .flow-connector {
                    color: #64748b;
                }
                @media (max-width: 640px) {
                    .concept-flow-track {
                        flex-direction: column;
                        align-items: stretch;
                    }
                    .flow-connector {
                        transform: rotate(90deg);
                        padding: 0.25rem 0;
                    }
                }
                /* Embedded Study SVGs Defensive Styles */
                .concept-section-block svg {
                    max-width: 100%;
                    height: auto;
                    margin: 1.25rem auto;
                    display: block;
                    background: #f8fafc;
                    border: 1px solid #e2e8f0;
                    border-radius: 12px;
                    padding: 0.75rem;
                    overflow: visible;
                }
                body.dark-mode .concept-section-block svg {
                    background: #0f172a !important;
                    border-color: #334155 !important;
                }
                body.dark-mode .concept-section-block svg text {
                    fill: #f1f5f9 !important;
                }
                body.dark-mode .concept-section-block svg line,
                body.dark-mode .concept-section-block svg path {
                    stroke: #60a5fa !important;
                }
                body.dark-mode .concept-section-block svg rect {
                    stroke: #334155 !important;
                }
                @media (max-width: 640px) {
                    .study-overview-card {
                        padding: 1.4rem 1.2rem;
                    }
                    .study-main-title {
                        font-size: 1.4rem;
                    }
                    .study-lead-definition {
                        font-size: 0.98rem;
                    }
                    .study-action-card {
                        padding: 1.4rem 1.2rem;
                        flex-direction: column;
                        align-items: stretch;
                    }
                    .action-card-content {
                        flex-direction: column;
                        align-items: flex-start;
                    }
                    .btn-proceed-practice {
                        width: 100%;
                        justify-content: center;
                    }
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

            // Transform crude SVG linear sequences into clean, responsive concept-flow-cards
            const sanitizeContent = (html, l) => {
                if (!html || typeof html !== 'string' || !html.includes('<svg')) return html;
                return html.replace(/<svg[\s\S]*?<\/svg>/gi, (match) => {
                    if (match.includes('linearGradient') || match.includes('<style') || match.includes('role-of-st') || match.includes('Theories-of-development')) {
                        return match;
                    }
                    const textMatches = Array.from(match.matchAll(/<text[^>]*>([\s\S]*?)<\/text>/gi));
                    let steps = [];
                    if (textMatches.length === 1) {
                        const raw = textMatches[0][1].replace(/<[^>]+>/g, '').replace(/&gt;/g, '>').replace(/&lt;/g, '<');
                        if (raw.includes('->') || raw.includes('→') || raw.includes('-->')) {
                            steps = raw.split(/\s*(?:-->|->|→)\s*/).map(s => s.trim()).filter(Boolean);
                        }
                    } else if (textMatches.length >= 2 && textMatches.length <= 8) {
                        steps = textMatches.map(t => t[1].replace(/<[^>]+>/g, '').trim()).filter(Boolean);
                    }
                    if (steps.length >= 2) {
                        const isHindi = l === 'hi' || /[\u0900-\u097F]/.test(steps.join(''));
                        const pillLabel = isHindi ? 'प्रक्रिया / कालक्रम प्रवाह' : 'Process & Chronology Flow';
                        const stepsHtml = steps.map((step, idx) => {
                            const isLast = idx === steps.length - 1;
                            const connector = !isLast ? `<div class="flow-connector" aria-hidden="true"><i class="fas fa-arrow-right"></i></div>` : '';
                            return `<div class="flow-node${isLast ? ' highlight' : ''}"><span class="flow-node-index">${idx + 1}</span><div class="flow-node-content"><span class="flow-node-title">${step}</span></div></div>${connector}`;
                        }).join('');
                        return `<div class="concept-flow-card"><div class="concept-flow-header"><span class="flow-pill"><i class="fas fa-route"></i> ${pillLabel}</span></div><div class="concept-flow-track">${stepsHtml}</div></div>`;
                    }
                    return match;
                });
            };
            const processedStr = sanitizeContent(rawStr, language);

            const lines = processedStr.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
            if (lines.length <= 1 && !processedStr.includes('• ') && !processedStr.includes('- ')) {
                return /^<(div|table|article|section|figure|svg)\b/i.test(processedStr.trim()) ? processedStr : `<p class="bullet-text-wrap">${processedStr}</p>`;
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
                if (/^<(div|table|article|section|figure|svg)\b/i.test(line.trim())) {
                    resultHtml += line;
                } else {
                    resultHtml += `<p class="bullet-text-wrap">${line}</p>`;
                }
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

        // Helper to format option letter safely (prevents [object Object])
        const formatLetter = (val) => {
            if (!val && val !== 0) return '';
            if (typeof val === 'string') return val.trim();
            if (typeof val === 'number') return ['A','B','C','D','E'][val] || String(val);
            if (typeof val === 'object') return (val.en || val.hi || Object.values(val)[0] || '').toString().trim();
            return String(val);
        };

        let currentTabAbortController = null;
        const topicTestState = {
            selectedOptions: {},
            submittedLevels: {}
        };

        const renderTabContent = (tabName) => {
            if (currentTabAbortController) {
                currentTabAbortController.abort();
            }
            currentTabAbortController = new AbortController();
            const { signal } = currentTabAbortController;

            let contentHtml = "";

            switch (tabName) {
                case "notes":
                case "overview":
                case "concepts":
                case "visual":
                case "comparisons":
                    const overview = pageData.overview || pageData.notes?.overview || {};
                    const concepts = pageData.concepts || pageData.notes?.concepts || {};
                    const visual = pageData.visual || pageData.notes?.visual || {};
                    const comparisons = pageData.comparisons || pageData.notes?.comparisons || {};

                    let notesHtml = `
                    <div class="study-overview-card">
                        <div class="study-card-badge">
                            <i class="fas fa-landmark"></i>
                            <span>${renderBilingual({ en: "UPSC Civil Services Foundation", hi: "UPSC सिविल सेवा आधारभूत अध्ययन" })}</span>
                        </div>
                        <h1 class="study-main-title">${renderBilingual(overview.title || { en: pageData.topicName, hi: pageData.hindiName || pageData.topicName })}</h1>
                        ${overview.definition ? `
                        <p class="study-lead-definition">${renderBilingual(overview.definition)}</p>
                        ` : ""}
                        
                        <div class="study-meta-grid">
                            ${overview.importanceInUpsc ? `
                            <div class="study-meta-item importance-item">
                                <h4><i class="fas fa-bullseye"></i> ${renderBilingual({ en: "Relevance for Prelims & Mains", hi: "प्रारंभिक एवं मुख्य परीक्षा महत्व" })}</h4>
                                <p>${renderBilingual(overview.importanceInUpsc)}</p>
                            </div>
                            ` : ""}

                            ${((overview.learningOutcomes || pageData.learningObjectives || []).length > 0) ? `
                            <div class="study-meta-item outcomes-item">
                                <h4><i class="fas fa-graduation-cap"></i> ${renderBilingual({ en: "Key Learning Outcomes", hi: "सीखने के मुख्य परिणाम" })}</h4>
                                <ul>
                                    ${(overview.learningOutcomes || pageData.learningObjectives || []).map(obj => `
                                        <li>${renderBilingual(obj)}</li>
                                    `).join("")}
                                </ul>
                            </div>
                            ` : ""}
                        </div>

                        ${overview.prerequisites && overview.prerequisites.length > 0 ? `
                        <div class="study-prereq-bar">
                            <span class="prereq-label"><i class="fas fa-layer-group"></i> ${renderBilingual({ en: "Prerequisites:", hi: "आवश्यक पूर्व ज्ञान:" })}</span>
                            <div class="prereq-chips">
                                ${overview.prerequisites.map(p => `<span class="prereq-chip">${renderBilingual(p)}</span>`).join("")}
                            </div>
                        </div>
                        ` : ""}
                    </div>
                    `;

                    // Core Concepts & Provisions
                    if (concepts.sections && concepts.sections.length > 0) {
                        notesHtml += `
                        <div class="study-section-wrapper" id="core-concepts-section">
                            <div class="study-section-header">
                                <span class="section-pill"><i class="fas fa-book-open"></i> ${renderBilingual({ en: "Core Provisions", hi: "मुख्य प्रावधान" })}</span>
                                <h2>${renderBilingual({ en: "Core Concepts & Provisions", hi: "मुख्य अवधारणाएँ एवं संवैधानिक प्रावधान" })}</h2>
                            </div>
                            ${concepts.sections.map(section => {
                                let sectionHtml = `<div class="concept-section-block"><h3>${renderBilingual(section.title)}</h3>`;
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
                                sectionHtml += `</div>`;
                                return sectionHtml;
                            }).join("")}
                        </div>
                        `;
                    }

                    // Visual Learning Aids
                    if (visual && Array.isArray(visual.visualBlocks) && visual.visualBlocks.length > 0) {
                        notesHtml += `
                        <div class="study-section-wrapper" id="visual-aids-section">
                            <div class="study-section-header">
                                <span class="section-pill"><i class="fas fa-diagram-project"></i> ${renderBilingual({ en: "Visual Synthesis", hi: "दृश्य आरेख" })}</span>
                                <h2>${renderBilingual({ en: "Visual Frameworks & Diagrams", hi: "दृश्य रूपरेखा एवं आरेख" })}</h2>
                            </div>
                            ${visual.visualBlocks.map(block => {
                                let blockHtml = `<div class="visual-block-card"><h4>${renderBilingual(block.title)}</h4>`;
                                if (block.type === "timeline") {
                                    blockHtml += `<div class="timeline">${block.data.map(item => `<div class="timeline-item"><h5>${renderBilingual(item.label)}</h5><p>${renderBilingual(item.description)}</p></div>`).join("")}</div>`;
                                } else if (block.type === "flow") {
                                    blockHtml += `<div class="flowchart">${block.data.map(item => `<span>${renderBilingual(item)}</span>`).join(" → ")}</div>`;
                                } else if (block.type === "tree") {
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
                                blockHtml += `</div>`;
                                return blockHtml;
                            }).join("")}
                        </div>
                        `;
                    }

                    // Comparisons & Connections
                    const hasComparisons = Boolean(
                        comparisons && (
                            (comparisons.differenceTables && comparisons.differenceTables.length > 0) ||
                            (comparisons.similarityTables && comparisons.similarityTables.length > 0) ||
                            comparisons.evolution ||
                            (comparisons.frequentlyConfused && comparisons.frequentlyConfused.length > 0) ||
                            (comparisons.conceptConnections && comparisons.conceptConnections.length > 0)
                        )
                    );

                    if (hasComparisons) {
                        notesHtml += `
                        <div class="study-section-wrapper" id="comparisons-section">
                            <div class="study-section-header">
                                <span class="section-pill"><i class="fas fa-scale-balanced"></i> ${renderBilingual({ en: "Comparative Analysis", hi: "तुलनात्मक विश्लेषण" })}</span>
                                <h2>${renderBilingual({ en: "Key Distinctions & Interconnections", hi: "तुलनात्मक अंतर एवं वैचारिक संबंध" })}</h2>
                            </div>
                            ${comparisons.differenceTables && comparisons.differenceTables.length > 0 ? `
                                ${comparisons.differenceTables.map(table => `
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
                            ${comparisons.similarityTables && comparisons.similarityTables.length > 0 ? `
                                ${comparisons.similarityTables.map(table => `
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
                            ${comparisons.evolution ? `
                                <h4>${renderBilingual(comparisons.evolution.title)}</h4>
                                <p>${comparisons.evolution.steps.map(step => renderBilingual(step)).join(" → ")}</p>
                            ` : ""}
                            ${comparisons.frequentlyConfused && comparisons.frequentlyConfused.length > 0 ? `
                                <h3>${renderBilingual({ en: "Frequently Confused Concepts", hi: "अक्सर भ्रमित होने वाली अवधारणाएँ" })}</h3>
                                <ul>
                                    ${comparisons.frequentlyConfused.map(item => `<li><strong>${renderBilingual(item.topicA)}</strong> vs <strong>${renderBilingual(item.topicB)}</strong>: ${renderBilingual(item.clarification)}</li>`).join("")}
                                </ul>
                            ` : ""}
                            ${comparisons.conceptConnections && comparisons.conceptConnections.length > 0 ? `
                                <h3>${renderBilingual({ en: "Concept Connections", hi: "अवधारणा संबंध" })}</h3>
                                <ul>
                                    ${comparisons.conceptConnections.map(item => `<li><strong>${renderBilingual(item.from)}</strong> to <strong>${renderBilingual(item.to)}</strong>: ${renderBilingual(item.relationship)}</li>`).join("")}
                                </ul>
                            ` : ""}
                        </div>
                        `;
                    }

                    // Exam Notes, Traps & Tips
                    if (concepts.upscNotes && concepts.upscNotes.length > 0) {
                        notesHtml += `
                        <div class="study-section-wrapper" id="exam-notes-section">
                            <div class="study-section-header">
                                <span class="section-pill"><i class="fas fa-lightbulb"></i> ${renderBilingual({ en: "High-Yield Insights", hi: "महत्वपूर्ण परीक्षा संकेत" })}</span>
                                <h2>${renderBilingual({ en: "Exam Notes, Traps & Pro-Tips", hi: "परीक्षा नोट्स, सावधानियां एवं रणनीति" })}</h2>
                            </div>
                            <div class="upsc-notes-container">
                                ${concepts.upscNotes.map(note => `
                                    <div class="upsc-note ${note.type || 'tip'}">
                                        <p class="note-content">
                                            <i class="fas ${note.type === 'trap' ? 'fa-triangle-exclamation' : 'fa-lightbulb'}"></i>
                                            ${renderBilingual(note.content)}
                                        </p>
                                    </div>
                                `).join("")}
                            </div>
                        </div>
                        `;
                    }

                    // Key Takeaways
                    if (concepts.keyTakeaways && concepts.keyTakeaways.length > 0) {
                        notesHtml += `
                        <div class="study-section-wrapper" id="takeaways-section">
                            <div class="study-section-header">
                                <span class="section-pill"><i class="fas fa-bookmark"></i> ${renderBilingual({ en: "Summary", hi: "त्वरित सारांश" })}</span>
                                <h2>${renderBilingual({ en: "Key Takeaways", hi: "मुख्य निष्कर्ष" })}</h2>
                            </div>
                            <div class="study-takeaways-card">
                                <ul>
                                    ${concepts.keyTakeaways.map(item => `<li>${renderBilingual(item)}</li>`).join("")}
                                </ul>
                            </div>
                        </div>
                        `;
                    }

                    // Call to Action Card: Proceed to Practice Questions
                    notesHtml += `
                    <div class="study-action-card">
                        <div class="action-card-content">
                            <div class="action-icon"><i class="fas fa-list-check"></i></div>
                            <div class="action-text">
                                <h3>${renderBilingual({ en: "Ready to Test Your Understanding?", hi: "क्या आप अपनी समझ का परीक्षण करने के लिए तैयार हैं?" })}</h3>
                                <p>${renderBilingual({ en: "Reinforce what you learned with topic-wise Prelims practice questions and detailed explanations.", hi: "टॉपिक-वाइज प्रीलिम्स अभ्यास प्रश्नों और विस्तृत व्याख्याओं के साथ अपनी तैयारी को सुदृढ़ करें।" })}</p>
                            </div>
                        </div>
                        <button type="button" class="btn-proceed-practice" data-action="go-to-practice">
                            <span>${renderBilingual({ en: "Go to Practice Questions", hi: "अभ्यास प्रश्नों पर जाएं" })}</span>
                            <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                    `;

                    contentHtml = notesHtml;
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
                            qHtml += renderQuestionContent(q);

                            const rawCorrectAnswer = formatLetter(q.correctAnswer);
                            const correctOpt = (q.options && Array.isArray(q.options))
                                ? q.options.find(o => o.correct === true || formatLetter(o.letter) === rawCorrectAnswer)
                                : null;
                            const resolvedCorrectLetter = rawCorrectAnswer || (correctOpt ? formatLetter(correctOpt.letter) : '') || (typeof q.ans === 'number' && ['A','B','C','D'][q.ans]) || '';

                            qHtml += `<div class="options-container">`;
                            if (q.options && Array.isArray(q.options)) {
                                q.options.forEach(option => {
                                    const optionText = pageData.topicId === "up-assistant-teacher.mathematics.algebraic-identities"
                                        ? mdToHtml(tryFixEncoding(option.text || ""))
                                        : renderBilingual(option.text);
                                    const optLetter = formatLetter(option.letter);
                                    const isOptCorrect = option.correct === true || (Boolean(resolvedCorrectLetter) && optLetter === resolvedCorrectLetter);
                                    qHtml += `
                                                    <div class="practice-option-box" data-opt-letter="${optLetter}" data-correct="${isOptCorrect}">
                                                        <label class="opt-label">
                                                            <input type="radio" name="p-${type}-${q.id || qIndex}" class="opt-radio" data-q-id="${q.id || qIndex}" data-opt-letter="${optLetter}" data-correct="${isOptCorrect}">
                                                            <span><b>${optLetter}.</b> ${optionText}</span>
                                                        </label>
                                                    </div>
                                                `;
                                });
                            }
                            qHtml += `</div><div class="sol-box"><p class="sol-text"><strong>${renderBilingual({ en: `Answer: ${resolvedCorrectLetter || q.correctMapping || ""}`, hi: `उत्तर: ${resolvedCorrectLetter || q.correctMapping || ""}` })}</strong> ${renderBilingual(q.explanation)}</p></div></div></div></div>`;
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
                                        <button type="button" class="practice-nav-btn next finish-practice" data-target-tab="tab-revision">
                                            <span>
                                                <small>${renderBilingual({ en: "Next Section", hi: "अगला खंड" })}</small>
                                                <strong>${renderBilingual({ en: "Revision Notes", hi: "रिवीजन नोट्स" })}</strong>
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
                        qHtml += renderQuestionContent(q);
                        const rawCorrectAnswer = formatLetter(q.correctAnswer);
                        const correctOpt = (q.options && Array.isArray(q.options))
                            ? q.options.find(o => o.correct === true || formatLetter(o.letter) === rawCorrectAnswer)
                            : null;
                        const resolvedCorrectLetter = rawCorrectAnswer || (correctOpt ? formatLetter(correctOpt.letter) : '') || (typeof q.ans === 'number' && ['A','B','C','D'][q.ans]) || '';

                        qHtml += `<div class="options-container">`;
                        if (q.options && Array.isArray(q.options)) {
                            q.options.forEach(option => {
                                const optLetter = formatLetter(option.letter);
                                const isOptCorrect = option.correct === true || (Boolean(resolvedCorrectLetter) && optLetter === resolvedCorrectLetter);
                                qHtml += `
                                        <div class="practice-option-box" data-opt-letter="${optLetter}" data-correct="${isOptCorrect}">
                                            <label class="opt-label">
                                                <input type="radio" name="pyq-${q.id || qIndex}" class="opt-radio" data-opt-letter="${optLetter}" data-correct="${isOptCorrect}">
                                                <span><b>${optLetter}.</b> ${renderBilingual(option.text)}</span>
                                            </label>
                                        </div>
                                    `;
                            });
                        }
                        qHtml += `</div><div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: `Answer: ${resolvedCorrectLetter || q.correctMapping || ""}`, hi: `उत्तर: ${resolvedCorrectLetter || q.correctMapping || ""}` })}</strong> ${renderBilingual(q.explanation)}</p></div>`;
                        qHtml += `</div></div></div>`;
                        return qHtml;
                    }).join("") : `<p>${renderBilingual({ en: "Previous year questions will be available soon.", hi: "पिछले वर्ष के प्रश्न जल्द ही उपलब्ध होंगे।" })}</p>`}
                    </div>
                `;
                    break;
                case "mains":
                    if (!pageData.mains || !Array.isArray(pageData.mains.questions) || pageData.mains.questions.length === 0) {
                        contentHtml = `
                        <h2>${renderBilingual({ en: "Mains Answer Writing", hi: "मुख्य उत्तर लेखन" })}</h2>
                        <div class="content-callout-card trick-callout" style="margin: 1.5rem 0; padding: 1.5rem; border-radius: 14px;">
                            <div class="callout-badge"><i class="fas fa-pen-fancy"></i> <span>${renderBilingual({ en: "Mains Questions in Preparation", hi: "मुख्य उत्तर लेखन तैयार हो रहा है" })}</span></div>
                            <p class="callout-text">${renderBilingual({
                                en: "Model answer frameworks, structured introductions, body points, and conclusions for Mains GS are currently being curated for this topic.",
                                hi: "इस विषय के लिए मुख्य परीक्षा GS के मॉडल उत्तर ढांचे, संरचित परिचय, मुख्य बिंदु और निष्कर्ष वर्तमान में तैयार किए जा रहे हैं।"
                            })}</p>
                        </div>
                        `;
                        break;
                    }
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
                                ${q.diagram.type === "flow" ? `<div class="flowchart">${q.diagram.data.map(item => `<span>${renderBilingual(item)}</span>`).join(" → ")}</div>` : renderBilingual(q.diagram.description)}
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
                        ${revision.mnemonics.map(item => {
                            const phrase = item.phrase || item.title || (item.text?.en?.phrase ? { en: item.text.en.phrase, hi: item.text?.hi?.phrase || item.text.en.phrase } : null);
                            const meaning = item.meaning || (item.text?.en?.title ? { en: item.text.en.title, hi: item.text?.hi?.title || item.text.en.title } : null);
                            const explanation = item.explanation || item.decryption || (item.text?.en?.decryption ? { en: item.text.en.decryption, hi: item.text?.hi?.decryption || item.text.en.decryption } : null);
                            return `
                            <div class="revision-card">
                                ${phrase ? `<h4>${renderBilingual(phrase)}</h4>` : ""}
                                ${meaning ? `<p><strong>${renderBilingual(meaning)}</strong></p>` : ""}
                                ${explanation ? `<p>${renderBilingual(explanation)}</p>` : ""}
                            </div>
                        `;}).join("")}
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
                    <ul>${revision.frequentlyConfusedFacts.map(item => {
                        const mis = item.misconception || item.fact;
                        const cor = item.correction || item.clarification;
                        return `<li>${mis ? `<strong>${renderBilingual(mis)}</strong>` : ""} ${cor ? renderBilingual(cor) : ""}</li>`;
                    }).join("")}</ul>
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
                                            qHtml += renderQuestionContent(q);

                                            const rawCorrectAnswer = formatLetter(q.correctAnswer);
                                            const correctOpt = (q.options && Array.isArray(q.options))
                                                ? q.options.find(o => o.correct === true || formatLetter(o.letter) === rawCorrectAnswer)
                                                : null;
                                            const resolvedCorrectLetter = rawCorrectAnswer || (correctOpt ? formatLetter(correctOpt.letter) : '') || (typeof q.ans === 'number' && ['A','B','C','D'][q.ans]) || '';

                                            qHtml += `<div class="options-container">`;
                                            if (q.options && Array.isArray(q.options)) {
                                                q.options.forEach(option => {
                                                    const optLetter = formatLetter(option.letter);
                                                    const isOptCorrect = option.correct === true || (Boolean(resolvedCorrectLetter) && optLetter === resolvedCorrectLetter);
                                                    qHtml += `
                                                        <div class="practice-option-box test-option-box" data-opt-letter="${optLetter}" data-correct="${isOptCorrect}">
                                                            <label class="opt-label">
                                                                <input type="radio" name="mini-test-${lvl}-${q.id || qIndex}" class="opt-radio" data-correct="${isOptCorrect}" data-opt="${optLetter}" data-opt-letter="${optLetter}">
                                                                <span><b>${optLetter}.</b> ${renderBilingual(option.text)}</span>
                                                            </label>
                                                        </div>
                                                    `;
                                                });
                                            }
                                            qHtml += `</div><div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: `Answer: ${resolvedCorrectLetter || ""}`, hi: `उत्तर: ${resolvedCorrectLetter || ""}` })}</strong> ${renderBilingual(q.explanation)}</p></div></div></div></div>`;
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
                                            <button type="button" class="practice-nav-btn next finish-practice" data-target-tab="tab-notes">
                                                <span>
                                                    <small>${renderBilingual({ en: "Test Completed", hi: "टेस्ट पूर्ण हुआ" })}</small>
                                                    <strong>${renderBilingual({ en: "Review Study Notes", hi: "स्टडी नोट्स दोहराएं" })}</strong>
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
                            const rawCorrectAnswer = formatLetter(q.correctAnswer);
                            qHtml += `<div class="options-container">${(q.options || []).map(option => {
                                const optLetter = formatLetter(option.letter);
                                const isCorrect = optLetter === rawCorrectAnswer;
                                return `
                            <div class="practice-option-box"><label class="opt-label"><input type="radio" name="t-${groupKey}-${q.id || qIndex}" class="opt-radio" data-correct="${isCorrect}"><span><b>${optLetter}.</b> ${renderBilingual(option.text)}</span></label></div>
                        `;
                            }).join("")}</div>`;
                            qHtml += `<div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${rawCorrectAnswer || q.correctMapping || ""}</strong> ${renderBilingual(q.explanation)}</p></div>`;
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
            if (tabName === "notes") {
                const proceedBtn = topicContent.querySelector('.btn-proceed-practice');
                if (proceedBtn) {
                    proceedBtn.addEventListener('click', () => {
                        const practiceTabBtn = studyTabs.querySelector('.tab-btn[data-tab="tab-practice"]');
                        if (practiceTabBtn) {
                            practiceTabBtn.click();
                            const tabsPos = studyTabs.getBoundingClientRect().top + window.pageYOffset;
                            window.scrollTo({ top: Math.max(0, tabsPos - 70), behavior: 'smooth' });
                        }
                    });
                }
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
                                const correctElem = container ? container.querySelector('[data-correct="true"]') : null;
                                if (correctElem) {
                                    correctLetter = correctElem.dataset.optLetter || (correctElem.querySelector('input')?.dataset.optLetter) || '';
                                    if (!correctLetter) {
                                        const bm = (correctElem.textContent || '').match(/([A-D])\./i);
                                        if (bm) correctLetter = bm[1].toUpperCase();
                                    }
                                }
                                if (!correctLetter && solBox) {
                                    const solText = solBox.textContent || '';
                                    const match = solText.match(/(?:Answer|उत्तर):\s*([A-D])/i) || solText.match(/([A-D])\./);
                                    if (match) correctLetter = match[1].toUpperCase();
                                }

                                const clickedLetter = optBox.dataset.optLetter || (optBox.querySelector('input')?.dataset.optLetter) || ((optBox.textContent || '').match(/([A-D])\./i)?.[1]?.toUpperCase() || '');
                                const isClickedCorrect = optBox.dataset.correct === 'true' || optBox.querySelector('input[data-correct="true"]') !== null || (Boolean(correctLetter) && clickedLetter === correctLetter);

                                if (container) {
                                    container.querySelectorAll('.practice-option-box').forEach(box => {
                                        box.classList.remove('correct', 'correct-option', 'incorrect', 'incorrect-option');
                                        const bl = box.dataset.optLetter || (box.querySelector('input')?.dataset.optLetter) || ((box.textContent || '').match(/([A-D])\./i)?.[1]?.toUpperCase() || '');
                                        const isBoxCorrect = box.dataset.correct === 'true' || box.querySelector('input[data-correct="true"]') !== null || (Boolean(correctLetter) && bl === correctLetter);
                                        if (isBoxCorrect) {
                                            box.classList.add('correct', 'correct-option');
                                        } else if (box === optBox && !isClickedCorrect) {
                                            box.classList.add('incorrect', 'incorrect-option');
                                        }
                                    });
                                }
                                const radio = optBox.querySelector('input[type="radio"]');
                                if (radio) radio.checked = true;
                                if (solBox) solBox.style.display = 'block';
                            }
                        }
                    }, { signal });
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

                    // Track user selections in test panels
                    topicContent.addEventListener('change', (e) => {
                        const radio = e.target.closest('input[type=radio]');
                        if (radio && radio.name && radio.dataset.optLetter) {
                            topicTestState.selectedOptions[radio.name] = radio.dataset.optLetter;
                        }
                    }, { signal });

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

                                topicTestState.submittedLevels[level] = {
                                    score,
                                    answered,
                                    total: cards.length,
                                    pct,
                                    badgeClass,
                                    remark
                                };
                            }
                        }
                    }, { signal });

                    // Restore test state if previously interacted
                    Object.entries(topicTestState.selectedOptions).forEach(([name, letter]) => {
                        const r = topicContent.querySelector(`input[name="${name}"][data-opt-letter="${letter}"]`);
                        if (r) r.checked = true;
                    });
                    Object.entries(topicTestState.submittedLevels).forEach(([lvl, data]) => {
                        const p = topicContent.querySelector(`.test-sub-panel[data-test-subpanel="test-${lvl}"]`);
                        if (p) {
                            p.classList.add('level-test-submitted');
                            p.querySelectorAll('.sol-box').forEach(s => s.style.display = 'block');
                            p.querySelectorAll('.test-option-box').forEach(box => {
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
                            const badge = p.querySelector(`#score-badge-${lvl}`);
                            if (badge) {
                                badge.className = `test-level-score-badge ${data.badgeClass}`;
                                badge.style.display = 'inline-flex';
                                badge.innerHTML = `<span><b>${data.score} / ${data.total}</b> ${renderBilingual({ en: "Correct", hi: "सही" })} (${data.pct}%)</span><span class="score-remark">— ${renderBilingual(data.remark)}</span>`;
                            }
                            const sBtn = p.querySelector('.btn-submit-level-test');
                            if (sBtn) {
                                sBtn.disabled = true;
                                sBtn.innerHTML = `<i class="fas fa-check-double"></i> ${renderBilingual({ en: "Test Submitted", hi: "टेस्ट जमा हो गया" })}`;
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

        const normalizeTabKey = (key) => {
            if (!key) return "notes";
            const k = key.replace(/^tab-/, '').toLowerCase();
            if (k === "overview" || k === "concepts" || k === "visual" || k === "comparisons" || k === "study-notes" || k === "notes") {
                return "notes";
            }
            if (k === "pyqs") return "practice";
            return k;
        };

        // Render the clean 5-tab structure: 1. Study Notes, 2. Practice Questions, 3. Revision, 4. Mains, 5. Test
        const setupTabBar = () => {
            const supportsMains = Boolean(pageData.supportsMains);
            let tabIndex = 1;
            const tabs = [
                { id: "notes", icon: "fa-book-open", en: "Study Notes", hi: "अध्ययन नोट्स", visible: true },
                { id: "practice", icon: "fa-list-check", en: "Practice Questions", hi: "अभ्यास प्रश्न", visible: true },
                { id: "revision", icon: "fa-rotate", en: "Revision", hi: "पुनरावृत्ति", visible: true },
                { id: "mains", icon: "fa-pen-fancy", en: "Mains", hi: "मुख्य परीक्षा", visible: supportsMains, btnId: "mains-tab-btn" },
                { id: "test", icon: "fa-graduation-cap", en: "Test", hi: "टेस्ट", visible: true }
            ];

            studyTabs.innerHTML = tabs.map(tab => {
                if (!tab.visible) {
                    return `<button class="tab-btn" data-tab="tab-${tab.id}" role="tab" aria-selected="false"${tab.btnId ? ` id="${tab.btnId}"` : ''} style="display:none;"><i class="fas ${tab.icon}"></i> <span class="lang-en">${tab.en}</span><span class="lang-hi">${tab.hi}</span></button>`;
                }
                const num = tabIndex++;
                return `<button class="tab-btn${num === 1 ? ' active' : ''}" data-tab="tab-${tab.id}" role="tab" aria-selected="${num === 1 ? 'true' : 'false'}"${tab.btnId ? ` id="${tab.btnId}"` : ''}><i class="fas ${tab.icon}"></i> <span class="lang-en">${num}. ${tab.en}</span><span class="lang-hi">${num}. ${tab.hi}</span></button>`;
            }).join("");
        };
        setupTabBar();

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

            const tabName = normalizeTabKey(clickedButton.dataset.tab);
            try { localStorage.setItem(`upsc-tab:${location.pathname}`, tabName); } catch (e) { }
            renderTabContent(tabName);
        });

        // Initial render for the active tab (Hash support, e.g. #notes, #concepts, #visual, etc.)
        const getHashTab = () => {
            const h = (window.location.hash || '').replace(/^#tab-/, '').replace(/^#/, '').toLowerCase();
            if (!h) return null;
            const norm = normalizeTabKey(h);
            return studyTabs.querySelector(`.tab-btn[data-tab="tab-${norm}"]`);
        };

        const handleDeepHashScroll = () => {
            const h = (window.location.hash || '').replace(/^#tab-/, '').replace(/^#/, '').toLowerCase();
            const targetMap = {
                "concepts": "core-concepts-section",
                "visual": "visual-aids-section",
                "comparisons": "comparisons-section"
            };
            const targetId = targetMap[h];
            if (targetId) {
                requestAnimationFrame(() => {
                    setTimeout(() => {
                        const el = document.getElementById(targetId);
                        if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
                    }, 50);
                });
            }
        };

        let savedTab = null;
        try {
            const rawSaved = localStorage.getItem(`upsc-tab:${location.pathname}`);
            if (rawSaved) savedTab = normalizeTabKey(rawSaved);
        } catch (e) { }
        const savedButton = savedTab && studyTabs.querySelector(`.tab-btn[data-tab="tab-${savedTab}"]`);
        const hashButton = getHashTab();
        const initialTab = hashButton || savedButton || studyTabs.querySelector(".tab-btn.active") || studyTabs.querySelector('.tab-btn[data-tab="tab-notes"]');
        if (initialTab) {
            studyTabs.querySelectorAll('.tab-btn').forEach(btn => {
                const isMatch = btn === initialTab;
                btn.classList.toggle('active', isMatch);
                btn.setAttribute('aria-selected', String(isMatch));
            });
            const tabName = normalizeTabKey(initialTab.dataset.tab);
            renderTabContent(tabName);
            handleDeepHashScroll();
        } else {
            renderTabContent("notes");
        }

        // Listen for hashchange events
        window.addEventListener('hashchange', () => {
            const targetBtn = getHashTab();
            if (targetBtn) {
                targetBtn.click();
                handleDeepHashScroll();
            }
        });

        // Handle Mains tab visibility
        const mainsTabButton = document.getElementById("mains-tab-btn");
        if (mainsTabButton) {
            mainsTabButton.style.display = pageData.supportsMains ? "" : "none";
        }

        // Hydrate Current Topic Hindi name in Related Topics card if available
        try {
            const currentTopicHi = document.querySelector('.related-topic-current .lang-hi');
            if (currentTopicHi && pageData.overview?.title?.hi && !/[\u0900-\u097F]/.test(currentTopicHi.textContent)) {
                currentTopicHi.textContent = pageData.overview.title.hi;
            }
        } catch (e) { }
    } catch (err) {
        console.error('UPSC renderer caught error:', err);
        try { document.getElementById('topic-content').innerHTML = '<div style="padding:1rem;color:#b91c1c;background:#fff7f7;border:1px solid #fecaca;border-radius:8px">Rendering failed — check console for details.</div>'; } catch (e) { }
    }
});
document.addEventListener("DOMContentLoaded",()=>{const e=document.querySelector('.topic-desc');e&&/\bundefined\b/i.test(e.textContent.trim())&&e.remove()});
const formatQuestionLevel = value => `${String(value || "").charAt(0).toUpperCase()}${String(value || "").slice(1).toLowerCase()}`;

function submitMockTest(button) {
    const root = button.closest('#topic-content') || button.closest('.topic-content') || document;
    const cards = root.querySelectorAll('.test-question-card');
    if (!cards.length) return;
    root.classList.add('mock-test-submitted');
    let score = 0, answered = 0;
    cards.forEach(card => {
        const selected = card.querySelector('input[type=radio]:checked');
        const solBox = card.querySelector('.sol-box');
        if (solBox) solBox.style.display = 'block';

        if (selected) {
            answered++;
            if (selected.dataset.correct === 'true') score++;
        }
        card.querySelectorAll('.practice-option-box').forEach(box => {
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
    const result = root.querySelector('.mock-test-result');
    if (result) {
        result.innerHTML = `<span class="lang-en"><strong>${score} / ${cards.length}</strong> correct (${pct}%) — ${answered} answered</span><span class="lang-hi"><strong>${score} / ${cards.length}</strong> सही (${pct}%) — ${answered} उत्तर दिए</span>`;
    }
    button.disabled = true;
    button.innerHTML = '<span class="lang-en"><i class="fas fa-check-double"></i> Test Submitted</span><span class="lang-hi"><i class="fas fa-check-double"></i> टेस्ट जमा हो गया</span>';
}
