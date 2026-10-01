(function() {
    window.switchTab = function(arg1, arg2) {
        let tabIndex = 1;
        let targetId = null;

        if (typeof arg1 === 'number') {
            tabIndex = arg1 === 0 ? 1 : arg1;
        } else if (typeof arg1 === 'string') {
            if (/^\d+$/.test(arg1)) {
                tabIndex = parseInt(arg1, 10);
                if (tabIndex === 0) tabIndex = 1;
            } else {
                targetId = arg1;
            }
        } else if (arg1 && arg1.target && typeof arg2 === 'string') {
            targetId = arg2;
        } else if (typeof arg2 === 'number') {
            tabIndex = arg2;
        }

        const idAliasMap = {
            'tab-notes': 1, 'tab-study': 1, 'tab-core': 1, 'tab1': 1, 'notes': 1, 'tab-1': 1, 'tab-content-1': 1, 'tabContent1': 1,
            'tab-quiz': 2, 'tab-equations': 2, 'tab2': 2, 'quiz': 2, 'tab-2': 2, 'tab-content-2': 2, 'tabContent2': 2,
            'tab-aviation': 3, 'tab-application': 3, 'tab3': 3, 'aviation': 3, 'tab-3': 3, 'tab-content-3': 3, 'tabContent3': 3,
            'tab-revision': 4, 'tab-mcqs': 4, 'tab4': 4, 'revision': 4, 'tab-4': 4, 'tab-content-4': 4, 'tabContent4': 4,
            'tab-tests': 5, 'tab-test': 5, 'tab-recall': 5, 'tab5': 5, 'tests': 5, 'tab-5': 5, 'tab-content-5': 5, 'tabContent5': 5
        };

        if (targetId && idAliasMap[targetId]) {
            tabIndex = idAliasMap[targetId];
        }

        const btnSelectors = [
            '.tab-btn', '.tab-button', '.nav-tab', '.tab-trigger',
            'button[id^="tab-btn-"]', 'button[id^="tabBtn"]', 'button[id^="btn-tab-"]',
            'nav button[onclick*="switchTab"]', '.tab-nav button'
        ];
        const allButtons = Array.from(document.querySelectorAll(btnSelectors.join(',')));
        const uniqueButtons = [];
        allButtons.forEach(b => { if (!uniqueButtons.includes(b)) uniqueButtons.push(b); });

        uniqueButtons.forEach((btn, idx) => {
            const btnCall = btn.getAttribute('onclick') || '';
            const btnId = btn.id || '';
            let isCurrent = false;

            if (btnId === `tab-btn-${tabIndex}` || btnId === `tabBtn${tabIndex}` || btnId === `btn-tab-${tabIndex}`) {
                isCurrent = true;
            } else if (btnCall.includes(`switchTab(${tabIndex})`) || btnCall.includes(`switchTab('${tabIndex}')`)) {
                isCurrent = true;
            } else if (targetId && (btnCall.includes(`'${targetId}'`) || btnCall.includes(`"${targetId}"`))) {
                isCurrent = true;
            } else if (idx === tabIndex - 1 && !btnCall.includes('switchTab(')) {
                isCurrent = true;
            }

            btn.classList.toggle('active', isCurrent);
            if (isCurrent) {
                btn.classList.remove('bg-white', 'text-slate-300', 'bg-slate-800', 'bg-aviation-800');
            }
        });

        const panelSelectors = [
            '.tab-content', '.tab-pane', '.tab-panel',
            '[id^="tab-content-"]', '[id^="tabContent"]',
            '[id^="tab-1"]', '[id^="tab-2"]', '[id^="tab-3"]', '[id^="tab-4"]', '[id^="tab-5"]',
            '#tab-study', '#tab-quiz', '#tab-application', '#tab-revision', '#tab-test', '#tab-tests',
            '#tab-notes', '#tab-aviation', '#tab-core', '#tab-equations', '#tab-mcqs', '#tab-recall',
            '[id^="content-tab-"]', '[id^="content-tab"]'
        ];
        const allPanels = Array.from(document.querySelectorAll(panelSelectors.join(',')));
        const uniquePanels = [];
        allPanels.forEach(p => { 
            if (!uniquePanels.includes(p) && p.tagName !== 'BUTTON' && p.tagName !== 'NAV') {
                uniquePanels.push(p); 
            }
        });

        let activePanel = null;
        if (targetId) {
            activePanel = document.getElementById(targetId);
        }
        if (!activePanel) {
            const possibleIds = [
                `tab-content-${tabIndex}`,
                `tabContent${tabIndex}`,
                `tab-${tabIndex}`,
                `content-tab-${tabIndex}`,
                `content-tab${tabIndex}`,
                `tab${tabIndex}`,
                `panel-${tabIndex}`
            ];
            for (let pid of possibleIds) {
                const el = document.getElementById(pid);
                if (el) { activePanel = el; break; }
            }
        }
        if (!activePanel && uniquePanels.length >= tabIndex) {
            activePanel = uniquePanels[tabIndex - 1];
        }

        uniquePanels.forEach(p => {
            p.classList.add('hidden');
            p.classList.remove('active');
            p.style.display = 'none';
        });

        if (activePanel) {
            activePanel.classList.remove('hidden');
            activePanel.classList.add('active');
            activePanel.style.display = 'block';
        }

        document.querySelectorAll('.progress-step').forEach((s, idx) => {
            s.classList.toggle('active', idx <= tabIndex - 1);
        });

        if (window.MathJax && window.MathJax.typesetPromise) {
            if (activePanel) {
                window.MathJax.typesetPromise([activePanel]).catch(function(){});
            } else {
                window.MathJax.typesetPromise().catch(function(){});
            }
        }
    };

    window.switchStudyTab = window.switchTab;

    document.addEventListener('DOMContentLoaded', function() {
        const hasActivePanel = document.querySelector('.tab-content.active, .tab-pane.active, .tab-panel.active');
        if (!hasActivePanel) {
            window.switchTab(1);
        }
    });
})();
