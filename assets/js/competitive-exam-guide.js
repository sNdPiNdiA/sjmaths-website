/**
 * Competitive Exam Study Guide Engine
 * Dynamically loads and renders content from content.json
 */

(function () {
    'use strict';

    let guideData = null;
    let questionsPerPage = 10;
    let currentPage = 1;
    let userAnswers = [];
    let currentTestIdx = 0;
    let testTimerInterval = null;
    let testSeconds = 0;

    // Load content files (supports split files theory.json, practice.json, mastery.json or fallback to content.json)
    function loadContent() {
        const cacheBuster = '?v=' + Date.now();
        fetch('theory.json' + cacheBuster)
            .then(res => {
                if (res.ok) {
                    // Split mode
                    return Promise.all([
                        res.json(),
                        fetch('practice.json' + cacheBuster).then(r => {
                            if (!r.ok) throw new Error('Failed to load practice.json');
                            return r.json();
                        }),
                        fetch('mastery.json' + cacheBuster).then(r => {
                            if (!r.ok) throw new Error('Failed to load mastery.json');
                            return r.json();
                        })
                    ]).then(([theoryData, practiceData, masteryData]) => {
                        guideData = {
                            ...theoryData,
                            ...practiceData
                        };
                        if (guideData.deepDive && guideData.deepDive.sections && masteryData.sections) {
                            guideData.deepDive.sections.forEach((sec, idx) => {
                                if (masteryData.sections[idx]) {
                                    sec.masteryZone = masteryData.sections[idx].masteryZone || [];
                                }
                            });
                        }
                        initGuide();
                    });
                } else {
                    // Fallback to unified content.json
                    return fetch('content.json' + cacheBuster)
                        .then(r => {
                            if (!r.ok) throw new Error('Failed to load content.json');
                            return r.json();
                        })
                        .then(data => {
                            guideData = data;
                            initGuide();
                        });
                }
            })
            .catch(err => {
                console.error('Error initializing study guide:', err);
            });
    }

    function renderMasteryZone(masteryZone, secIdx) {
        if (!masteryZone || !masteryZone.length) return '';
        const isHindi = document.documentElement.lang === 'hi';
        const labels = {
            title: isHindi ? "🎯 खंड महारत क्षेत्र" : "🎯 Section Mastery Zone",
            desc: isHindi ? "इस खंड की अवधारणाओं पर पूर्ण नियंत्रण पाने के लिए नीचे दिए गए विभिन्न श्रेणियों के प्रश्नों को हल करें:" : "Solve the different categories of questions below to master this section:"
        };

        const grouped = {};
        masteryZone.forEach((q, originalIdx) => {
            const type = q.type;
            if (!grouped[type]) {
                grouped[type] = [];
            }
            grouped[type].push({ q, idx: originalIdx });
        });

        const orderedTypes = [
            "MCQ", "Multiple Correct MCQ", "True/False", "Fill in the Blank",
            "Match the Following", "One-Liner", "Assertion-Reason", "Statement-Based",
            "Why", "How", "Case Study", "Teach the Concept"
        ];

        const presentTypes = orderedTypes.filter(t => grouped[t] && grouped[t].length > 0);

        const typeLabels = {
            "MCQ": isHindi ? "बहुविकल्पीय (MCQ)" : "MCQ",
            "Multiple Correct MCQ": isHindi ? "बहु-विकल्प सही" : "Multi-Correct",
            "True/False": isHindi ? "सत्य / असत्य" : "True/False",
            "Fill in the Blank": isHindi ? "रिक्त स्थान" : "Fill Blank",
            "Match the Following": isHindi ? "सुमेलित करें" : "Matching",
            "One-Liner": isHindi ? "एक-रेखीय" : "One-Liner",
            "Assertion-Reason": isHindi ? "कथन-कारण" : "Assertion-Reason",
            "Statement-Based": isHindi ? "कथन आधारित" : "Statement-Based",
            "Why": isHindi ? "क्यों? (तर्क)" : "Why?",
            "How": isHindi ? "कैसे? (प्रक्रिया)" : "How?",
            "Case Study": isHindi ? "मामला अध्ययन" : "Case Study",
            "Teach the Concept": isHindi ? "अवधारणा समझाएं" : "Teach Concept"
        };

        const groupsHtml = presentTypes.map((type, idx) => {
            const label = typeLabels[type] || type;
            const count = grouped[type].length;
            const isActive = idx === 0;
            const questionsHtml = grouped[type].map(item => renderMasteryQuestion(item.q, secIdx, item.idx, isHindi)).join('');
            return `
                <div class="mastery-type-group">
                    <button class="mastery-type-header-btn ${isActive ? 'active' : ''}" onclick="toggleMasteryTypeGroup(this, ${secIdx}, '${type}')">
                        <span>${label} (${count})</span>
                        <i class="fas fa-chevron-down" style="transform: ${isActive ? 'rotate(180deg)' : 'rotate(0deg)'}"></i>
                    </button>
                    <div class="mastery-type-questions-content" id="mastery-type-content-${secIdx}-${type.replace(/\s+/g, '-')}" style="${isActive ? 'display: flex;' : 'display: none;'}">
                        ${questionsHtml}
                    </div>
                </div>
            `;
        }).join('');

        return `
            <div class="mastery-zone" style="margin-top: 2rem; border-top: 2px dashed rgba(212,175,55,0.25); padding-top: 1.5rem;">
                <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.25rem; font-weight: 800; color: #d4af37; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem;">
                    <i class="fas fa-bullseye"></i> ${labels.title}
                </h3>
                <p style="font-size: 0.88rem; color: var(--text-light); margin-bottom: 1.25rem; font-family: 'Inter', sans-serif;">${labels.desc}</p>
                <div class="mastery-questions-list">
                    ${groupsHtml}
                </div>
            </div>
        `;
    }

    function renderMasteryQuestion(q, secIdx, qIdx, isHindi) {
        let badgeText = q.type;
        if (isHindi) {
            const typeTranslations = {
                "MCQ": "बहुविकल्पीय प्रश्न (MCQ)",
                "Multiple Correct MCQ": "बहु-विकल्प सही प्रश्न",
                "True/False": "सत्य / असत्य",
                "Fill in the Blank": "रिक्त स्थान भरें",
                "Match the Following": "सुमेलित करें",
                "One-Liner": "एक-रेखीय प्रश्न (One-Liner)",
                "Assertion-Reason": "कथन और कारण",
                "Statement-Based": "कथन आधारित प्रश्न",
                "Why": "क्यों? (तर्क प्रश्न)",
                "How": "कैसे? (प्रक्रिया प्रश्न)",
                "Case Study": "केस स्टडी (मामला अध्ययन)",
                "Teach the Concept": "अवधारणा समझाएं"
            };
            badgeText = typeTranslations[q.type] || q.type;
        }

        if (q.type === "MCQ" || q.type === "Assertion-Reason" || q.type === "Statement-Based") {
            const optsHtml = (q.opts || []).map((opt, optIdx) => `
                <button class="mastery-opt-btn" onclick="checkMasteryMCQ(this, ${secIdx}, ${qIdx}, ${optIdx})">
                    ${opt}
                </button>
            `).join('');

            return `
                <div class="mastery-q-card" id="mastery-card-${secIdx}-${qIdx}">
                    <div class="mastery-q-header">
                        <span class="mastery-badge">${badgeText}</span>
                    </div>
                    <div class="mastery-q-text">${q.q}</div>
                    <div class="mastery-options">
                        ${optsHtml}
                    </div>
                    <div class="mastery-explanation" id="mastery-exp-${secIdx}-${qIdx}" style="display:none;">
                        <strong>${isHindi ? "स्पष्टीकरण:" : "Explanation:"}</strong> ${q.sol}
                    </div>
                </div>
            `;
        } else if (q.type === "Multiple Correct MCQ") {
            const cbHtml = (q.opts || []).map((opt, optIdx) => `
                <label class="mastery-checkbox-label">
                    <input type="checkbox" name="mastery-cb-${secIdx}-${qIdx}" value="${optIdx}">
                    <span>${opt}</span>
                </label>
            `).join('');

            return `
                <div class="mastery-q-card" id="mastery-card-${secIdx}-${qIdx}">
                    <div class="mastery-q-header">
                        <span class="mastery-badge">${badgeText}</span>
                    </div>
                    <div class="mastery-q-text">${q.q}</div>
                    <div class="mastery-checkboxes">
                        ${cbHtml}
                    </div>
                    <button class="mastery-submit-btn" onclick="checkMasteryMultiMCQ(this, ${secIdx}, ${qIdx})">
                        ${isHindi ? "उत्तर सबमिट करें" : "Submit Answer"}
                    </button>
                    <div class="mastery-explanation" id="mastery-exp-${secIdx}-${qIdx}" style="display:none;">
                        <strong>${isHindi ? "स्पष्टीकरण:" : "Explanation:"}</strong> ${q.sol}
                    </div>
                </div>
            `;
        } else if (q.type === "True/False") {
            return `
                <div class="mastery-q-card" id="mastery-card-${secIdx}-${qIdx}">
                    <div class="mastery-q-header">
                        <span class="mastery-badge">${badgeText}</span>
                    </div>
                    <div class="mastery-q-text">${q.q}</div>
                    <div class="mastery-tf-buttons">
                        <button class="mastery-opt-btn" onclick="checkMasteryTF(this, ${secIdx}, ${qIdx}, true)">
                            ${isHindi ? "सत्य (True)" : "True"}
                        </button>
                        <button class="mastery-opt-btn" onclick="checkMasteryTF(this, ${secIdx}, ${qIdx}, false)">
                            ${isHindi ? "असत्य (False)" : "False"}
                        </button>
                    </div>
                    <div class="mastery-explanation" id="mastery-exp-${secIdx}-${qIdx}" style="display:none;">
                        <strong>${isHindi ? "स्पष्टीकरण:" : "Explanation:"}</strong> ${q.sol}
                    </div>
                </div>
            `;
        } else if (q.type === "Fill in the Blank") {
            return `
                <div class="mastery-q-card" id="mastery-card-${secIdx}-${qIdx}">
                    <div class="mastery-q-header">
                        <span class="mastery-badge">${badgeText}</span>
                    </div>
                    <div class="mastery-q-text">${q.q}</div>
                    <div style="display: flex; gap: 0.5rem; align-items: center; margin-top: 0.5rem; flex-wrap: wrap;">
                        <input type="text" class="mastery-input" placeholder="${isHindi ? "यहाँ लिखें..." : "Type here..."}" id="mastery-blank-input-${secIdx}-${qIdx}">
                        <button class="mastery-submit-btn" onclick="checkMasteryBlank(this, ${secIdx}, ${qIdx})" style="margin-top:0;">
                            ${isHindi ? "जांचें" : "Check"}
                        </button>
                    </div>
                    <div class="mastery-explanation" id="mastery-exp-${secIdx}-${qIdx}" style="display:none;">
                        <strong>${isHindi ? "स्पष्टीकरण:" : "Explanation:"}</strong> ${q.sol}
                    </div>
                </div>
            `;
        } else if (q.type === "Match the Following") {
            const itemsHtml = (q.items || []).map((item, itemIdx) => {
                const selectOptions = (q.options || []).map(opt => `
                    <option value="${opt.val}">${opt.text}</option>
                `).join('');
                
                return `
                    <div style="display: flex; justify-content: space-between; align-items: center; gap: 1rem; border-bottom: 1px dashed rgba(128,128,128,0.1); padding: 0.4rem 0; flex-wrap: wrap;">
                        <span style="font-size: 0.88rem; color: var(--text-dark);">${item.left}</span>
                        <select class="mastery-select" name="mastery-match-select-${secIdx}-${qIdx}-${itemIdx}">
                            <option value="">${isHindi ? "चुनें..." : "Select..."}</option>
                            ${selectOptions}
                        </select>
                    </div>
                `;
            }).join('');

            return `
                <div class="mastery-q-card" id="mastery-card-${secIdx}-${qIdx}">
                    <div class="mastery-q-header">
                        <span class="mastery-badge">${badgeText}</span>
                    </div>
                    <div class="mastery-q-text">${q.q}</div>
                    <div style="display: flex; flex-direction: column; gap: 0.25rem; margin-top: 0.5rem;">
                        ${itemsHtml}
                    </div>
                    <button class="mastery-submit-btn" onclick="checkMasteryMatching(this, ${secIdx}, ${qIdx})">
                        ${isHindi ? "मिलान जांचें" : "Check Match"}
                    </button>
                    <div class="mastery-explanation" id="mastery-exp-${secIdx}-${qIdx}" style="display:none;">
                        <strong>${isHindi ? "स्पष्टीकरण:" : "Explanation:"}</strong> ${q.sol}
                    </div>
                </div>
            `;
        } else {
            return `
                <div class="mastery-q-card" id="mastery-card-${secIdx}-${qIdx}">
                    <div class="mastery-q-header">
                        <span class="mastery-badge">${badgeText}</span>
                    </div>
                    <div class="mastery-q-text">${q.q}</div>
                    <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem;">
                        <textarea class="mastery-input" style="width: 100%; min-height: 60px; resize: vertical;" placeholder="${isHindi ? "स्वयं-परीक्षण के लिए अपना उत्तर यहाँ लिखें (वैकल्पिक)..." : "Write your answer here to self-test (optional)..."}"></textarea>
                        <button class="mastery-action-btn" onclick="toggleMasteryExp(${secIdx}, ${qIdx})">
                            ${isHindi ? "आदर्श उत्तर देखें" : "Reveal Model Answer"}
                        </button>
                    </div>
                    <div class="mastery-explanation" id="mastery-exp-${secIdx}-${qIdx}" style="display:none;">
                        <strong>${isHindi ? "स्पष्टीकरण / आदर्श उत्तर:" : "Explanation / Model Answer:"}</strong> ${q.sol}
                    </div>
                </div>
            `;
        }
    }

    function initGuide() {
        if (!guideData) return;

        // Render Breadcrumbs
        const breadcrumbs = document.querySelector('.breadcrumbs');
        if (breadcrumbs && guideData.breadcrumbs) {
            breadcrumbs.innerHTML = `
                <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem; margin: 0 0.4rem;"></i>
                <a href="${guideData.breadcrumbs.parentUrl}">${guideData.breadcrumbs.parent}</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem; margin: 0 0.4rem;"></i>
                <span>${guideData.breadcrumbs.current}</span>
            `;
        }

        // Render Hero Section
        const heroSection = document.querySelector('.hero-section');
        if (heroSection && guideData.hero) {
            heroSection.innerHTML = `
                <div class="hero-copy">
                    <h1>${guideData.hero.title}</h1>
                    <p>${guideData.hero.description}</p>
                    <div class="hero-actions" aria-label="Page shortcuts">
                        <a href="#main-content" class="btn-action btn-next" style="text-decoration:none;"><i class="fas fa-arrow-down"></i> Start Reading</a>
                    </div>
                </div>
            `;
        }

        // Setup Mindmap
        const mindmapSection = document.getElementById('mindmap-section');
        if (mindmapSection && guideData.mindmap) {
            mindmapSection.style.display = 'block';
            mindmapSection.innerHTML = `
                <h2 class="card-title"><i class="fas fa-project-diagram"></i> ${guideData.mindmap.title}</h2>
                <p style="margin-bottom: 1.5rem; color: var(--text-light); font-size: 0.95rem;">${guideData.mindmap.description}</p>
                <div class="mindmap-container">
                    ${guideData.mindmap.nodes.map(node => `
                        <div class="mindmap-node">
                            <div class="node-title"><i class="fas ${node.icon}"></i> ${node.title}</div>
                            <ul class="node-items">
                                ${node.items.map(item => `<li>${item}</li>`).join('')}
                            </ul>
                        </div>
                    `).join('')}
                </div>
            `;
        }

        // Setup Deep Dive Study Notes
        const deepDiveSection = document.getElementById('deep-dive-section');
        if (deepDiveSection && guideData.deepDive) {
            deepDiveSection.innerHTML = `
                <h2 class="card-title"><i class="fas fa-book-open"></i> ${guideData.deepDive.title}</h2>
                <p style="margin-bottom: 1.5rem; color: var(--text-light); font-size: 0.95rem;">${guideData.deepDive.description}</p>
                <div class="accordion-container">
                    ${guideData.deepDive.sections.map((sec, idx) => `
                        <div class="accordion-item">
                            <button class="accordion-header" onclick="toggleAccordion(this)">
                                <span>${sec.title}</span>
                                <i class="fas fa-chevron-down"></i>
                            </button>
                            <div class="accordion-body">
                                ${sec.content}
                                ${renderMasteryZone(sec.masteryZone, idx)}
                            </div>
                        </div>
                    `).join('')}
                </div>
            `;
        }

        // Setup Active Recall Flashcards
        const flashcardsSection = document.getElementById('flashcards-section');
        if (flashcardsSection && guideData.flashcards) {
            const cards = guideData.flashcards.items || guideData.flashcards.cards || [];
            flashcardsSection.innerHTML = `
                <h2 class="card-title"><i class="fas fa-layer-group"></i> ${guideData.flashcards.title}</h2>
                <p style="margin-bottom: 1.5rem; color: var(--text-light); font-size: 0.95rem;">${guideData.flashcards.description}</p>
                <div class="flashcards-grid">
                    ${cards.map(fc => {
                        const question = fc.question || fc.front || '';
                        const answer = fc.answer || fc.back || '';
                        const icon = fc.icon || 'fa-question-circle';
                        return `
                            <div class="flashcard" onclick="toggleFlashcard(this)">
                                <div class="flashcard-front">
                                    <i class="fas ${icon} flashcard-icon"></i>
                                    <div style="font-size: 0.95rem; font-weight: 700; line-height: 1.4; color: var(--text-dark);">${question}</div>
                                    <div class="flashcard-instruction"><i class="fas fa-rotate"></i> Click to flip</div>
                                </div>
                                <div class="flashcard-back">
                                    <div style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">${answer}</div>
                                    <div class="flashcard-instruction" style="color: var(--primary-pre); margin-top: 0.75rem;"><i class="fas fa-rotate"></i> Flip back</div>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            `;
        }

        // Setup Timeline
        const timelineContainer = document.querySelector('.interactive-timeline');
        if (timelineContainer && guideData.timeline) {
            timelineContainer.innerHTML = '';
            guideData.timeline.cards.forEach((card, idx) => {
                const activeClass = idx === 0 ? 'active' : '';
                const cardEl = document.createElement('div');
                cardEl.className = `timeline-card ${activeClass}`;
                cardEl.onclick = () => toggleTimeline(cardEl);
                cardEl.innerHTML = `
                    <div class="timeline-period">${card.period}</div>
                    <div class="timeline-date">${card.date}</div>
                    <div class="click-instruction"><i class="fas fa-hand-pointer"></i> ${guideData.labels.clickToExpand}</div>
                    <div class="timeline-details">${card.details}</div>
                `;
                timelineContainer.appendChild(cardEl);
            });
        }

        // Setup Mnemonics
        const mnemonicsSection = document.getElementById('mnemonics-section');
        if (mnemonicsSection && guideData.mnemonics) {
            mnemonicsSection.innerHTML = `
                <h2 class="card-title"><i class="fas fa-lightbulb"></i> ${guideData.mnemonics.title}</h2>
                <p>${guideData.mnemonics.description}</p>
            `;
            guideData.mnemonics.items.forEach(item => {
                const container = document.createElement('div');
                container.className = 'mnemonic-container';
                container.innerHTML = `
                    <div class="mnemonic-title">${item.title}</div>
                    <div class="mnemonic-phrase">${item.phrase}</div>
                    <div class="mnemonic-decryption">${item.decryption}</div>
                `;
                mnemonicsSection.appendChild(container);
            });
        }

        // Setup Evolution Chart
        const evolutionSection = document.getElementById('evolution-section');
        if (evolutionSection && guideData.toolEvolution) {
            evolutionSection.innerHTML = `
                <h2 class="card-title"><i class="fas fa-hammer"></i> ${guideData.toolEvolution.title}</h2>
                <p>${guideData.toolEvolution.description}</p>
                <div class="evolution-chart"></div>
            `;
            const chart = evolutionSection.querySelector('.evolution-chart');
            guideData.toolEvolution.stages.forEach(stage => {
                const stageEl = document.createElement('div');
                stageEl.className = 'tool-stage';
                stageEl.innerHTML = `
                    ${stage.svg}
                    <strong style="color: ${stage.color};">${stage.name}</strong>
                    <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">${stage.desc}</p>
                `;
                chart.appendChild(stageEl);
            });
        }

        // Setup Traps
        const trapsSection = document.getElementById('traps-section');
        if (trapsSection && guideData.traps) {
            trapsSection.innerHTML = `
                <h2 class="card-title" style="color: #e74c3c;"><i class="fas fa-triangle-exclamation"></i> ${guideData.traps.title}</h2>
                <ul style="padding-left: 1.25rem; font-size: 0.9rem; line-height: 1.6;">
                    ${guideData.traps.items.map(item => `<li style="margin-bottom: 0.5rem;">${item}</li>`).join('')}
                </ul>
            `;
        }

        // Initialize Practice Questions
        renderPracticeQuestions(1);

        // Setup Mock Test Intro Labels
        const testIntro = document.getElementById('testIntro');
        if (testIntro && guideData.labels && guideData.labels.mockIntro) {
            testIntro.innerHTML = `
                <i class="fas fa-graduation-cap" style="font-size: 3rem; color: #d4af37; margin-bottom: 1rem;"></i>
                <h2>${guideData.labels.mockIntro.title}</h2>
                <p style="color: var(--text-light); margin: 0.5rem 0 1.5rem;">${guideData.labels.mockIntro.description}</p>
                <button class="btn-action btn-next" onclick="startTest()">${guideData.labels.mockIntro.startBtn}</button>
            `;
        }
        
        // Setup initial userAnswers array
        userAnswers = Array(guideData.mockTestQuestions ? guideData.mockTestQuestions.length : 0).fill(null);

        // Hide unused tabs and empty cards dynamically
        const hasPractice = guideData.practiceQuestions && guideData.practiceQuestions.length > 0;
        const hasMock = guideData.mockTestQuestions && guideData.mockTestQuestions.length > 0;
        const practiceTabBtn = document.querySelector('.tab-btn[data-tab="practice-panel"]');
        const testTabBtn = document.querySelector('.tab-btn[data-tab="test-panel"]');
        const studyTabs = document.querySelector('.study-tabs');

        if (practiceTabBtn && !hasPractice) {
            practiceTabBtn.style.display = 'none';
        }
        if (testTabBtn && !hasMock) {
            testTabBtn.style.display = 'none';
        }
        if (studyTabs && !hasPractice && !hasMock) {
            studyTabs.style.display = 'none';
        }

        const timelineCard = document.querySelector('.interactive-timeline');
        if (timelineCard) {
            const parentCard = timelineCard.closest('.card-premium');
            const hasTimeline = guideData.timeline && guideData.timeline.cards && guideData.timeline.cards.length > 0;
            if (parentCard && !hasTimeline) {
                parentCard.style.display = 'none';
            }
        }

        const mnemonicsCard = document.getElementById('mnemonics-section');
        if (mnemonicsCard) {
            const hasMnemonics = guideData.mnemonics && guideData.mnemonics.items && guideData.mnemonics.items.length > 0;
            if (!hasMnemonics) {
                mnemonicsCard.style.display = 'none';
            }
        }

        const trapsCard = document.getElementById('traps-section');
        if (trapsCard) {
            const hasTraps = guideData.traps && guideData.traps.items && guideData.traps.items.length > 0;
            if (!hasTraps) {
                trapsCard.style.display = 'none';
            }
        }
    }

    // ==================== ACCORDION TOGGLE ====================
    window.toggleAccordion = function (btn) {
        const item = btn.parentNode;
        const body = item.querySelector('.accordion-body');
        const icon = btn.querySelector('.fa-chevron-down');
        
        const isOpen = body.style.display === 'block';
        
        // Close all other accordions inside this container
        const container = item.parentNode;
        container.querySelectorAll('.accordion-body').forEach(b => b.style.display = 'none');
        container.querySelectorAll('.fa-chevron-down').forEach(i => i.style.transform = 'rotate(0deg)');
        container.querySelectorAll('.accordion-header').forEach(h => h.classList.remove('active-header'));
        
        if (!isOpen) {
            body.style.display = 'block';
            icon.style.transform = 'rotate(180deg)';
            btn.classList.add('active-header');
        }
    };

    // ==================== FLASHCARD TOGGLE ====================
    window.toggleFlashcard = function (card) {
        card.classList.toggle('flipped');
    };
 
    // ==================== TIMELINE TOGGLE ====================
    window.toggleTimeline = function (card) {
        const isActive = card.classList.contains('active');
        document.querySelectorAll('.timeline-card').forEach(c => c.classList.remove('active'));
        if (!isActive) {
            card.classList.add('active');
        }
    };

    // ==================== TABS SYSTEM ====================
    window.switchTab = function (tabId) {
        const btn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
        if (btn) {
            // Remove active states
            document.querySelectorAll('.tab-btn').forEach(b => {
                b.classList.remove('active');
                b.setAttribute('aria-selected', 'false');
            });
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));

            // Set active states
            btn.classList.add('active');
            btn.setAttribute('aria-selected', 'true');
            document.getElementById(tabId).classList.add('active');

            // Scroll into view
            const container = document.querySelector('.study-tabs');
            if (container) {
                container.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    };

    // Setup native click listeners on tabs
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const target = btn.getAttribute('data-tab');
                switchTab(target);
            });
        });
        loadContent();
    });

    // ==================== PRACTICE ZONE QUESTIONS ====================
    window.renderPracticeQuestions = function (page) {
        if (!guideData || !guideData.practiceQuestions) return;

        const container = document.getElementById('practiceQuestionsContainer');
        if (!container) return;
        container.innerHTML = '';
        
        const start = (page - 1) * questionsPerPage;
        const end = start + questionsPerPage;
        const pageQs = guideData.practiceQuestions.slice(start, end);

        pageQs.forEach((q, idx) => {
            const globalIdx = start + idx;
            const card = document.createElement('div');
            card.className = 'practice-card';
            
            const isMultiple = Array.isArray(q.ans);
            let optsHtml = '';
            q.opts.forEach((opt, optIdx) => {
                if (isMultiple) {
                    optsHtml += `<li class="opt-item" data-idx="${optIdx}" onclick="togglePracticeOption(this)">${opt}</li>`;
                } else {
                    optsHtml += `<li class="opt-item" onclick="checkPracticeAnswer(this, ${globalIdx}, ${optIdx})">${opt}</li>`;
                }
            });

            const isHindi = document.documentElement.lang === 'hi';
            const submitBtnHtml = isMultiple ? `
                <button class="sol-btn submit-mult-btn" style="border-style: solid; margin-right: 0.5rem;" onclick="checkPracticeMultipleAnswer(this, ${globalIdx})">
                    ${isHindi ? 'उत्तर सबमिट करें' : 'Submit Answer'}
                </button>
            ` : '';

            card.innerHTML = `
                <div class="q-header">
                    <span class="q-badge">Q ${globalIdx + 1}</span>
                    <div>${q.q.replace(/\n/g, '<br>')}</div>
                </div>
                <ul class="options-list">${optsHtml}</ul>
                <div style="display: flex; align-items: center; flex-wrap: wrap;">
                    ${submitBtnHtml}
                    <button class="sol-btn" onclick="toggleExplanation(${globalIdx})">${isHindi ? 'स्पष्टीकरण दिखाएं' : 'Show Explanation'}</button>
                </div>
                <div class="explanation-box" id="exp-${globalIdx}">
                    <strong>${isHindi ? 'स्पष्टीकरण:' : 'Explanation:'}</strong> ${q.sol}
                </div>
            `;
            container.appendChild(card);
        });

        renderPagination();
    };

    function renderPagination() {
        if (!guideData || !guideData.practiceQuestions) return;
        const pagination = document.getElementById('practicePagination');
        if (!pagination) return;
        pagination.innerHTML = '';
        const totalPages = Math.ceil(guideData.practiceQuestions.length / questionsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const dot = document.createElement('div');
            dot.className = `page-dot ${i === currentPage ? 'active' : ''}`;
            dot.textContent = i;
            dot.onclick = () => {
                currentPage = i;
                renderPracticeQuestions(i);
                document.getElementById('practice-panel').scrollIntoView({ behavior: 'smooth', block: 'start' });
            };
            pagination.appendChild(dot);
        }
    }

    window.togglePracticeOption = function (element) {
        if (element.style.pointerEvents === 'none') return;
        element.classList.toggle('selected-multiple');
    };

    window.checkPracticeMultipleAnswer = function (btn, qIdx) {
        if (!guideData) return;
        const q = guideData.practiceQuestions[qIdx];
        const correctAnswers = q.ans;
        const parent = btn.closest('.practice-card');
        const items = parent.querySelectorAll('.opt-item');
        
        items.forEach(item => {
            item.style.pointerEvents = 'none';
            const optIdx = parseInt(item.getAttribute('data-idx'));
            const isSelected = item.classList.contains('selected-multiple');
            
            if (correctAnswers.includes(optIdx)) {
                item.classList.remove('selected-multiple');
                item.classList.add('selected-correct');
            } else if (isSelected) {
                item.classList.remove('selected-multiple');
                item.classList.add('selected-incorrect');
            }
        });
        
        btn.style.display = 'none';
        toggleExplanation(qIdx, true);
    };

    window.checkPracticeAnswer = function (element, qIdx, selectedIdx) {
        if (!guideData) return;
        const correctAnswer = guideData.practiceQuestions[qIdx].ans;
        const parent = element.parentNode;
        const items = parent.querySelectorAll('.opt-item');
        
        items.forEach(item => item.style.pointerEvents = 'none');

        if (selectedIdx === correctAnswer) {
            element.classList.add('selected-correct');
        } else {
            element.classList.add('selected-incorrect');
            if (typeof correctAnswer === 'number') {
                items[correctAnswer].classList.add('selected-correct');
            }
        }
        
        toggleExplanation(qIdx, true);
    };

    window.toggleExplanation = function (idx, forceShow = false) {
        const box = document.getElementById(`exp-${idx}`);
        if (!box) return;
        if (forceShow || box.style.display === 'none' || box.style.display === '') {
            box.style.display = 'block';
        } else {
            box.style.display = 'none';
        }
    };

    // ==================== MOCK TEST ENGINE ====================
    window.startTest = function () {
        document.getElementById('testIntro').style.display = 'none';
        document.getElementById('testPlayCard').style.display = 'block';
        document.getElementById('testResultsCard').style.display = 'none';
        currentTestIdx = 0;
        userAnswers.fill(null);
        testSeconds = 0;
        clearInterval(testTimerInterval);
        testTimerInterval = setInterval(updateTestTimer, 1000);
        renderTestQuestion();
    };

    function updateTestTimer() {
        testSeconds++;
        const mins = String(Math.floor(testSeconds / 60)).padStart(2, '0');
        const secs = String(testSeconds % 60).padStart(2, '0');
        const timer = document.getElementById('testTimer');
        if (timer) {
            timer.textContent = `Time: ${mins}:${secs}`;
        }
    }

    function renderTestQuestion() {
        if (!guideData || !guideData.mockTestQuestions) return;
        const container = document.getElementById('testQuestionArea');
        if (!container) return;
        container.innerHTML = '';
        
        const q = guideData.mockTestQuestions[currentTestIdx];
        document.getElementById('testProgress').textContent = `Question ${currentTestIdx + 1} of ${guideData.mockTestQuestions.length}`;

        let optionsHtml = '';
        q.opts.forEach((opt, optIdx) => {
            const isSelected = userAnswers[currentTestIdx] === optIdx;
            optionsHtml += `<div class="test-opt ${isSelected ? 'selected' : ''}" onclick="selectTestOption(${optIdx})">${opt}</div>`;
        });

        container.innerHTML = `
            <div class="test-q-num">Question ${currentTestIdx + 1}</div>
            <div class="test-q-text">${q.q.replace(/\n/g, '<br>')}</div>
            <div class="test-options">${optionsHtml}</div>
        `;

        // Buttons configuration
        const prevBtn = document.getElementById('btnPrevTest');
        if (prevBtn) {
            prevBtn.disabled = currentTestIdx === 0;
            prevBtn.textContent = guideData.labels.mockPlay.prevBtn;
        }

        const nextBtn = document.getElementById('btnNextTest');
        if (nextBtn) {
            if (currentTestIdx === guideData.mockTestQuestions.length - 1) {
                nextBtn.textContent = guideData.labels.mockPlay.submitBtn;
                nextBtn.className = 'btn-action btn-submit';
            } else {
                nextBtn.textContent = guideData.labels.mockPlay.nextBtn;
                nextBtn.className = 'btn-action btn-next';
            }
        }
    }

    window.selectTestOption = function (optIdx) {
        userAnswers[currentTestIdx] = optIdx;
        renderTestQuestion();
    };

    window.prevTestQuestion = function () {
        if (currentTestIdx > 0) {
            currentTestIdx--;
            renderTestQuestion();
        }
    };

    window.nextTestQuestion = function () {
        if (!guideData) return;
        if (currentTestIdx < guideData.mockTestQuestions.length - 1) {
            currentTestIdx++;
            renderTestQuestion();
        } else {
            submitTest();
        }
    };

    window.submitTest = function () {
        if (!guideData) return;
        clearInterval(testTimerInterval);
        document.getElementById('testPlayCard').style.display = 'none';
        document.getElementById('testResultsCard').style.display = 'block';

        let correctCount = 0;
        guideData.mockTestQuestions.forEach((q, idx) => {
            if (userAnswers[idx] === q.ans) {
                correctCount++;
            }
        });

        // Set Score
        document.getElementById('resultScoreCircle').textContent = `${correctCount}/${guideData.mockTestQuestions.length}`;
        
        const summaryText = document.getElementById('resultSummaryText');
        if (summaryText) {
            if (document.documentElement.lang === 'hi') {
                summaryText.textContent = `आपने ${guideData.mockTestQuestions.length} में से ${correctCount} प्रश्नों का सही उत्तर ${Math.floor(testSeconds / 60)} मिनट और ${testSeconds % 60} सेकंड में दिया।`;
            } else {
                summaryText.textContent = `You answered ${correctCount} questions correctly out of ${guideData.mockTestQuestions.length} in ${Math.floor(testSeconds / 60)} minutes and ${testSeconds % 60} seconds.`;
            }
        }

        // Render review panel
        const reviewArea = document.getElementById('testReviewArea');
        if (reviewArea) {
            reviewArea.innerHTML = '';
            guideData.mockTestQuestions.forEach((q, idx) => {
                const isCorrect = userAnswers[idx] === q.ans;
                const reviewItem = document.createElement('div');
                reviewItem.className = 'review-item';
                
                reviewItem.innerHTML = `
                    <div class="review-badge ${isCorrect ? 'correct' : 'incorrect'}">
                        ${isCorrect ? '<i class="fas fa-check"></i> Correct' : '<i class="fas fa-xmark"></i> Incorrect / Unanswered'}
                    </div>
                    <div style="font-weight: 600; margin-bottom: 0.5rem;">Q${idx + 1}. ${q.q.replace(/\n/g, '<br>')}</div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>Your Answer:</strong> ${userAnswers[idx] !== null ? q.opts[userAnswers[idx]] : '<span style="color:#e74c3c">Not Answered</span>'}
                    </div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>Correct Answer:</strong> ${q.opts[q.ans]}
                    </div>
                    <div style="background: rgba(0,0,0,0.02); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem; margin-top: 0.5rem;">
                        <strong>Explanation:</strong> ${q.sol}
                    </div>
                `;
                reviewArea.appendChild(reviewItem);
            });
        }
    };

    window.restartTest = function () {
        startTest();
    };

    // ==================== INTERACTIVE MASTERY ZONE HANDLERS ====================
    window.checkMasteryMCQ = function (element, secIdx, qIdx, selectedIdx) {
        const q = guideData.deepDive.sections[secIdx].masteryZone[qIdx];
        const parent = element.parentNode;
        const buttons = parent.querySelectorAll('.mastery-opt-btn');
        
        buttons.forEach(btn => btn.style.pointerEvents = 'none');
        
        if (selectedIdx === q.ans) {
            element.classList.add('mastery-correct-anim');
        } else {
            element.classList.add('mastery-incorrect-anim');
            buttons[q.ans].classList.add('mastery-correct-anim');
        }
        
        const exp = document.getElementById(`mastery-exp-${secIdx}-${qIdx}`);
        if (exp) exp.style.display = 'block';
    };

    window.checkMasteryMultiMCQ = function (btn, secIdx, qIdx) {
        const q = guideData.deepDive.sections[secIdx].masteryZone[qIdx];
        const parent = btn.parentNode;
        const checkboxes = parent.querySelectorAll(`input[name="mastery-cb-${secIdx}-${qIdx}"]`);
        
        let selectedIdxs = [];
        checkboxes.forEach((cb) => {
            if (cb.checked) {
                selectedIdxs.push(parseInt(cb.value));
            }
            cb.disabled = true;
        });
        
        const isCorrect = Array.isArray(q.ans) && 
                          selectedIdxs.length === q.ans.length && 
                          selectedIdxs.every(v => q.ans.includes(v));
                          
        checkboxes.forEach((cb, idx) => {
            const label = cb.closest('label');
            if (q.ans.includes(idx)) {
                label.style.color = '#27ae60';
                label.style.fontWeight = 'bold';
            } else if (cb.checked) {
                label.style.color = '#c0392b';
            }
        });
        
        if (isCorrect) {
            btn.classList.add('mastery-correct-anim');
            btn.textContent = document.documentElement.lang === 'hi' ? "सही! 🎉" : "Correct! 🎉";
        } else {
            btn.classList.add('mastery-incorrect-anim');
            btn.textContent = document.documentElement.lang === 'hi' ? "गलत। पुनः प्रयास करें!" : "Incorrect. Try again!";
        }
        
        const exp = document.getElementById(`mastery-exp-${secIdx}-${qIdx}`);
        if (exp) exp.style.display = 'block';
        
        btn.style.pointerEvents = 'none';
    };

    window.checkMasteryTF = function (element, secIdx, qIdx, isTrueSelected) {
        const q = guideData.deepDive.sections[secIdx].masteryZone[qIdx];
        const parent = element.parentNode;
        const buttons = parent.querySelectorAll('.mastery-opt-btn');
        
        buttons.forEach(btn => btn.style.pointerEvents = 'none');
        
        const correctBtn = q.ans === true ? buttons[0] : buttons[1];
        
        if (isTrueSelected === q.ans) {
            element.classList.add('mastery-correct-anim');
        } else {
            element.classList.add('mastery-incorrect-anim');
            correctBtn.classList.add('mastery-correct-anim');
        }
        
        const exp = document.getElementById(`mastery-exp-${secIdx}-${qIdx}`);
        if (exp) exp.style.display = 'block';
    };

    window.checkMasteryBlank = function (btn, secIdx, qIdx) {
        const q = guideData.deepDive.sections[secIdx].masteryZone[qIdx];
        const input = document.getElementById(`mastery-blank-input-${secIdx}-${qIdx}`);
        if (!input) return;
        
        const val = input.value.trim().toLowerCase();
        const correctVal = q.ans.trim().toLowerCase();
        
        const isCorrect = val === correctVal || 
                          val.replace(/\s+/g, '') === correctVal.replace(/\s+/g, '') || 
                          val.includes(correctVal) || 
                          (correctVal.includes(val) && val.length >= 3);
        
        input.disabled = true;
        btn.style.pointerEvents = 'none';
        
        if (isCorrect) {
            input.classList.add('mastery-correct-anim');
            btn.classList.add('mastery-correct-anim');
        } else {
            input.classList.add('mastery-incorrect-anim');
            btn.classList.add('mastery-incorrect-anim');
            input.value = `${input.value} (${document.documentElement.lang === 'hi' ? "सही उत्तर: " : "Correct: "} ${q.ans})`;
        }
        
        const exp = document.getElementById(`mastery-exp-${secIdx}-${qIdx}`);
        if (exp) exp.style.display = 'block';
    };

    window.checkMasteryMatching = function (btn, secIdx, qIdx) {
        const q = guideData.deepDive.sections[secIdx].masteryZone[qIdx];
        const parent = btn.parentNode;
        const selects = parent.querySelectorAll(`select[name^="mastery-match-select-${secIdx}-${qIdx}-"]`);
        
        let allCorrect = true;
        selects.forEach((select, idx) => {
            const val = select.value;
            const correctVal = q.items[idx].key;
            select.disabled = true;
            
            if (val === correctVal) {
                select.style.borderColor = '#2ecc71';
                select.style.color = '#27ae60';
            } else {
                select.style.borderColor = '#e74c3c';
                select.style.color = '#c0392b';
                allCorrect = false;
            }
        });
        
        if (allCorrect) {
            btn.classList.add('mastery-correct-anim');
            btn.textContent = document.documentElement.lang === 'hi' ? "सही! 🎉" : "Correct! 🎉";
        } else {
            btn.classList.add('mastery-incorrect-anim');
            btn.textContent = document.documentElement.lang === 'hi' ? "गलत। व्याख्या देखें।" : "Incorrect. See explanation.";
        }
        
        const exp = document.getElementById(`mastery-exp-${secIdx}-${qIdx}`);
        if (exp) exp.style.display = 'block';
        
        btn.style.pointerEvents = 'none';
    };

    window.toggleMasteryExp = function (secIdx, qIdx) {
        const exp = document.getElementById(`mastery-exp-${secIdx}-${qIdx}`);
        if (!exp) return;
        if (exp.style.display === 'none' || exp.style.display === '') {
            exp.style.display = 'block';
        } else {
            exp.style.display = 'none';
        }
    };

    window.toggleMasteryTypeGroup = function (btn, secIdx, type) {
        const group = btn.parentNode;
        const content = group.querySelector('.mastery-type-questions-content');
        const icon = btn.querySelector('.fa-chevron-down');
        
        const isOpen = content.style.display === 'flex';
        const list = group.parentNode;
        
        // Collapse all other mastery groups in this section
        list.querySelectorAll('.mastery-type-questions-content').forEach(c => {
            c.style.display = 'none';
        });
        list.querySelectorAll('.fa-chevron-down').forEach(i => {
            i.style.transform = 'rotate(0deg)';
        });
        list.querySelectorAll('.mastery-type-header-btn').forEach(b => {
            b.classList.remove('active');
        });
        
        // Toggle the clicked one
        if (!isOpen) {
            content.style.display = 'flex';
            if (icon) icon.style.transform = 'rotate(180deg)';
            btn.classList.add('active');
            
            // Smooth scroll to header button
            setTimeout(() => {
                btn.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    };

})();
