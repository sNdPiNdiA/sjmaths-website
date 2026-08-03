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
            const results = await Promise.all(tabDataKeys.map(async (key) => {
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

        // Helper function to render bilingual text (applies encoding/markdown fixes)
        const renderBilingual = (obj) => {
            if (typeof obj === 'string') return mdToHtml(tryFixEncoding(obj));
            if (obj && obj.en) return `<span class="lang-en">${mdToHtml(tryFixEncoding(obj.en))}</span><span class="lang-hi">${mdToHtml(tryFixEncoding(obj.hi || obj.en))}</span>`;
            return "";
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
                    <p>${renderBilingual(pageData.overview.definition)}</p><h3>${renderBilingual({ en: "Importance in UPSC", hi: "UPSC में महत्व" })}</h3>
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
                            sectionHtml += `<p>${renderBilingual(section.content)}</p>`;
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
                            sectionHtml += `<ul>${section.items.map(item => `<li><strong>${renderBilingual(item.term)}:</strong> ${renderBilingual(item.definition)}</li>`).join("")}</ul>`;
                        } else if (section.type === "subcards") {
                            sectionHtml += `<div class="subcards-container">${section.items.map(item => `<div class="subcard"><h4>${renderBilingual(item.title)}</h4><p>${renderBilingual(item.content)}</p></div>`).join("")}</div>`;
                        }
                        return sectionHtml;
                    }).join("")}
                    ${pageData.concepts.upscNotes && pageData.concepts.upscNotes.length > 0 ? `
                    <h3>${renderBilingual({ en: "UPSC Notes & Insights", hi: "UPSC नोट्स और अंतर्दृष्टि" })}</h3>
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
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Practice Questions", hi: "अभ्यास प्रश्न" })}</h2>
                    <div class="practice-questions-container">
                        ${pageData.practice && pageData.practice.levels ? Object.entries(pageData.practice.levels).map(([type, questions]) => `
                            <div class="practice-level ${type}-level">
                                <h3>${renderBilingual(type)} Questions</h3>
                                ${Array.isArray(questions) ? shuffleArray(questions).map((q, qIndex) => {
                        let qHtml = `<div class="practice-question-card"><div class="q-row"><div class="q-num-badge">${qIndex + 1}</div><div class="q-body">`;
                        if (q.question) {
                            qHtml += `<p class="q-text-sm">${renderBilingual(q.question)}</p>`;
                        }
                        if (q.statements) {
                            qHtml += `<ul>${q.statements.map(s => `<li>${renderBilingual(s.text || s)}</li>`).join("")}</ul>`;
                        }
                        if (q.assertion) {
                            qHtml += `<p class="q-text-sm"><strong><span class="lang-en">Assertion (A):</span><span class="lang-hi">अभिकथन (A):</span></strong> ${renderBilingual(q.assertion)}</p>`;
                            qHtml += `<p class="q-text-sm"><strong><span class="lang-en">Reason (R):</span><span class="lang-hi">कारण (R):</span></strong> ${renderBilingual(q.reason)}</p>`;
                        }
                        if (q.pairs) {
                            qHtml += `<div class="match-pairs">${q.pairs.map(pair => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><span>${renderBilingual(pair.right)}</span></div>`).join("")}</div>`;
                        }

                        qHtml += `<div class="options-container">`;
                        if (q.options && Array.isArray(q.options)) {
                            q.options.forEach(option => {
                                qHtml += `
                                                <div class="practice-option-box">
                                                    <label class="opt-label">
                                                        <input type="radio" name="p-${q.id}" class="opt-radio" data-q-id="${q.id}" data-opt-letter="${option.letter}">
                                                        <span><b>${option.letter}.</b> ${renderBilingual(option.text)}</span>
                                                    </label>
                                                </div>
                                            `;
                            });
                        }
                        qHtml += `</div><div class="sol-box"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${q.correctAnswer || q.correctMapping || ""}</strong> ${renderBilingual(q.explanation)}</p></div></div></div></div>`;
                        return qHtml;
                    }).join("") : ""}
                            </div>
                        `).join("") : `<p>${renderBilingual({ en: "Practice questions not available.", hi: "अभ्यास प्रश्न उपलब्ध नहीं हैं।" })}</p>`}
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
                            qHtml += `<ul>${q.statements.map(s => `<li>${renderBilingual(s.text || s)}</li>`).join("")}</ul>`;
                        }
                        if (q.pairs) {
                            qHtml += `<div class="match-pairs">${q.pairs.map(pair => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><span>${renderBilingual(pair.right)}</span></div>`).join("")}</div>`;
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
                        qHtml += `<button class="btn-check-test" onclick="
                                const parent = this.closest('.q-body');
                                const selected = parent.querySelector('input[type=radio]:checked');
                                if (!selected) { alert('Please select an option first!'); return; }
                                const isCorrect = selected.getAttribute('data-correct') === 'true';
                                parent.querySelector('.sol-box').style.setProperty('display', 'block', 'important');
                                this.style.display = 'none';
                                selected.closest('.practice-option-box').style.background = isCorrect ? '#ecfdf5' : '#fef2f2';
                                selected.closest('.practice-option-box').style.borderColor = isCorrect ? '#10b981' : '#ef4444';
                            " style="margin-top:1rem; padding:0.6rem 1.2rem; background:var(--up-primary); color:white; border:none; border-radius:30px; cursor:pointer; font-weight:600; font-size:0.9rem; font-family:'Outfit',sans-serif; transition:all 0.2s;"><span class="lang-en">Check Answer</span><span class="lang-hi">उत्तर जांचें</span></button>`;
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
                `;
                    break;
                case "test":
                    const test = pageData.test || {};
                    const testGroups = [["mcq", "MCQs"], ["statementBased", "Statement Based"], ["match", "Match the Following"]];
                    const renderTestQuestion = (q, qIndex, groupKey) => {
                        let qHtml = `<div class="practice-question-card test-question-card"><div class="q-row"><div class="q-num-badge">${qIndex + 1}</div><div class="q-body">`;
                        qHtml += q.question ? `<p class="q-text-sm">${renderBilingual(q.question)}</p>` : "";
                        if (q.statements) qHtml += `<p class="q-text-sm">${renderBilingual({ en: "Consider the following statements:", hi: "निम्नलिखित कथनों पर विचार करें:" })}</p><ul>${q.statements.map(statement => `<li>${renderBilingual(statement.text || statement)}</li>`).join("")}</ul>`;
                        if (q.pairs) qHtml += `<div class="match-pairs">${q.pairs.map(pair => `<div class="match-item"><span>${renderBilingual(pair.left)}</span><span>${renderBilingual(pair.right)}</span></div>`).join("")}</div>`;
                        qHtml += `<div class="options-container">${(q.options || []).map(option => `
                        <div class="practice-option-box"><label class="opt-label"><input type="radio" name="t-${groupKey}-${q.id || qIndex}" class="opt-radio" data-correct="${option.letter === q.correctAnswer}"><span><b>${option.letter}.</b> ${renderBilingual(option.text)}</span></label></div>
                    `).join("")}</div>`;
                        qHtml += `<button class="btn-check-test" onclick="
                            const parent = this.closest('.q-body');
                            const selected = parent.querySelector('input[type=radio]:checked');
                            if (!selected) { alert('Please select an option first!'); return; }
                            const isCorrect = selected.getAttribute('data-correct') === 'true';
                            parent.querySelector('.sol-box').style.setProperty('display', 'block', 'important');
                            this.style.display = 'none';
                            selected.closest('.practice-option-box').style.background = isCorrect ? '#ecfdf5' : '#fef2f2';
                            selected.closest('.practice-option-box').style.borderColor = isCorrect ? '#10b981' : '#ef4444';
                        " style="margin-top:1rem; padding:0.6rem 1.2rem; background:var(--up-primary); color:white; border:none; border-radius:30px; cursor:pointer; font-weight:600; font-size:0.9rem; font-family:'Outfit',sans-serif; transition:all 0.2s;"><span class="lang-en">Check Answer</span><span class="lang-hi">उत्तर जांचें</span></button>`;
                        qHtml += `<div class="sol-box" style="display:none; margin-top:1rem;"><p class="sol-text"><strong>${renderBilingual({ en: "Answer:", hi: "उत्तर:" })} ${q.correctAnswer || q.correctMapping || ""}</strong> ${renderBilingual(q.explanation)}</p></div>`;
                        qHtml += `</div></div></div>`;
                        return qHtml;
                    };
                    contentHtml = `
                    <h2>${renderBilingual({ en: "Mock Test", hi: "मॉक टेस्ट" })}</h2>
                    ${testGroups.map(([key, label]) => test[key] && test[key].length > 0 ? `<h3>${renderBilingual({ en: label, hi: (label === 'MCQs' ? 'बहुविकल्पीय प्रश्न' : label) })}</h3><div class="practice-questions-container">${test[key].map((q, qIndex) => renderTestQuestion(q, qIndex, key)).join("")}</div>` : "").join("")}
                    ${test.mains ? `<h3>${renderBilingual({ en: "Mains Practice", hi: "मुख्य अभ्यास" })}</h3>${(Array.isArray(test.mains) ? test.mains : (test.mains.questions || [test.mains])).map(q => `<div class="mains-question-card"><h4>${renderBilingual(q.question)} ${q.marks ? `<span class="mains-marks">(${q.marks} Marks)</span>` : ""}</h4>${q.structure ? `<ul>${q.structure.map(item => `<li>${renderBilingual(item)}</li>`).join("")}</ul>` : ""}${q.modelAnswer ? `<div class="model-answer-section">${q.modelAnswer.introduction ? `<p><strong>${renderBilingual({ en: "Introduction:", hi: "परिचय:" })}</strong> ${renderBilingual(q.modelAnswer.introduction)}</p>` : ""}${q.modelAnswer.body ? `<p><strong>${renderBilingual({ en: "Body:", hi: "मुख्य भाग:" })}</strong> ${renderBilingual(q.modelAnswer.body)}</p>` : ""}${q.modelAnswer.conclusion ? `<p><strong>${renderBilingual({ en: "Conclusion:", hi: "निष्कर्ष:" })}</strong> ${renderBilingual(q.modelAnswer.conclusion)}</p>` : ""}</div>` : ""}</div>`).join("")}` : ""}
                `;
                    break;
                default:
                    contentHtml = `<h2>${renderBilingual({ en: `Content for ${tabName}`, hi: `${tabName} के लिए सामग्री` })}</h2><p>${renderBilingual({ en: "Loading...", hi: "लोड हो रहा है..." })}</p>`;
            }

            topicContent.innerHTML = contentHtml;
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
            renderTabContent(tabName);
        });

        // Initial render for the active tab (Overview by default)
        const initialTab = studyTabs.querySelector(".tab-btn.active");
        if (initialTab) {
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
