/** Homepage interactions. Resource destinations remain ordinary HTML links. */
(() => {
    'use strict';
    // main.js owns theme behaviour; this page moves its existing control between
    // the intro on larger screens and the shared header on phones.
    function placeThemeControl() {
        const control = document.getElementById('darkToggle');
        const headerActions = document.querySelector('#site-header .header-actions');
        const desktopTarget = document.getElementById('home-theme-control');
        if (!control) return false;
        if (window.matchMedia('(max-width: 768px)').matches) {
            if (headerActions) {
                const menuButton = headerActions.querySelector('.mobile-toggle');
                if (!headerActions.contains(control)) headerActions.insertBefore(control, menuButton);
                return true;
            }
            return false;
        } else if (desktopTarget) {
            if (!desktopTarget.contains(control)) desktopTarget.append(control);
            return true;
        }
        return false;
    }

    function initThemeControlPlacement() {
        if (!placeThemeControl()) {
            const observer = new MutationObserver(() => {
                if (placeThemeControl()) observer.disconnect();
            });
            observer.observe(document.body, { childList: true, subtree: true });
            setTimeout(() => observer.disconnect(), 6000);
        }
    }

    if (document.readyState === 'complete') initThemeControlPlacement();
    else document.addEventListener('DOMContentLoaded', initThemeControlPlacement, { once: true });
    window.matchMedia('(max-width: 768px)').addEventListener('change', placeThemeControl);
    const tabs = [...document.querySelectorAll('.class-pill-btn')];
    const panels = [...document.querySelectorAll('.class-subject-panel')];
    const tablist = document.querySelector('.class-pills-bar');
    const stackedTabs = matchMedia('(min-width: 901px)');
    const mobileAccordion = matchMedia('(max-width: 768px)');
    const panelsContainer = document.querySelector('.class-panels-container');
    const mobileOptions = new Map();
    const updateTabOrientation = () => tablist?.setAttribute('aria-orientation', stackedTabs.matches ? 'vertical' : 'horizontal');
    updateTabOrientation();
    stackedTabs.addEventListener('change', updateTabOrientation);
    function setMobileClassLayout(mobile) {
        const workspace = document.querySelector('.school-workspace');
        if (!tablist || !panelsContainer || !workspace) return;
        workspace.classList.toggle('mobile-class-accordion', mobile);
        if (mobile) {
            tablist.setAttribute('role', 'group');
            tablist.removeAttribute('aria-orientation');
            tabs.forEach(tab => {
                const option = document.createElement('div');
                option.className = 'mobile-class-option';
                const slot = document.createElement('div');
                slot.className = 'mobile-class-panel-slot';
                tablist.insertBefore(option, tab);
                option.append(tab, slot);
                tab.setAttribute('role', 'button');
                tab.removeAttribute('aria-selected');
                tab.setAttribute('aria-expanded', 'false');
                mobileOptions.set(tab, { option, slot });
            });
        } else {
            panels.forEach(panel => panelsContainer.append(panel));
            tabs.forEach(tab => {
                const { option } = mobileOptions.get(tab) || {};
                if (option) tablist.insertBefore(tab, option);
                option?.remove();
                mobileOptions.delete(tab);
                tab.setAttribute('role', 'tab');
                tab.removeAttribute('aria-expanded');
                tab.setAttribute('aria-selected', String(tab.classList.contains('active')));
            });
            tablist.setAttribute('role', 'tablist');
            updateTabOrientation();
        }
        const activeTab = tabs.find(tab => tab.classList.contains('active'));
        if (activeTab) {
            selectClass(activeTab);
        } else if (!mobile) {
            selectClass(tabs[0]);
        } else {
            tabs.forEach(tab => {
                tab.classList.remove('active');
                tab.setAttribute('aria-expanded', 'false');
                tab.tabIndex = 0;
            });
            panels.forEach(panel => {
                panel.classList.remove('active');
                panel.hidden = true;
                panelsContainer.append(panel);
            });
        }
    }
    function selectClass(tab, focus = false) {
        if (!tab) return;
        const isCurrentlyActive = tab.classList.contains('active');
        const willCollapse = mobileAccordion.matches && isCurrentlyActive;

        tabs.forEach(item => {
            const selected = !willCollapse && item === tab;
            item.classList.toggle('active', selected);
            if (mobileAccordion.matches) item.setAttribute('aria-expanded', String(selected));
            else item.setAttribute('aria-selected', String(selected));
            item.tabIndex = selected || (!mobileAccordion.matches && item === tabs[0]) ? 0 : (mobileAccordion.matches ? 0 : -1);
        });
        if (mobileAccordion.matches) panels.forEach(panel => panelsContainer.append(panel));
        panels.forEach(panel => {
            const selected = !willCollapse && panel.id === tab.getAttribute('aria-controls');
            panel.classList.toggle('active', selected);
            panel.hidden = !selected;
            if (selected && mobileAccordion.matches) mobileOptions.get(tab)?.slot.append(panel);
        });
        if (focus && !willCollapse) tab.focus();
    }
    setMobileClassLayout(mobileAccordion.matches);
    mobileAccordion.addEventListener('change', event => setMobileClassLayout(event.matches));
    tabs.forEach((tab, index) => {
        tab.addEventListener('click', () => selectClass(tab));
        tab.addEventListener('keydown', event => {
            let next;
            if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
            if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
            const isVertical = stackedTabs.matches || mobileAccordion.matches;
            if (isVertical && event.key === 'ArrowDown') next = (index + 1) % tabs.length;
            if (isVertical && event.key === 'ArrowUp') next = (index - 1 + tabs.length) % tabs.length;
            if (event.key === 'Home') next = 0;
            if (event.key === 'End') next = tabs.length - 1;
            if (next !== undefined) {
                event.preventDefault();
                selectClass(tabs[next], true);
            }
        });
    });
    if (tabs.length && !mobileAccordion.matches) selectClass(tabs[0]);

    document.querySelectorAll('.faq-question').forEach((button, index) => {
        const item = button.closest('.faq-item');
        const answer = item.querySelector('.faq-answer');
        answer.id = `home-faq-answer-${index}`;
        button.setAttribute('aria-controls', answer.id);
        button.addEventListener('click', () => {
            const isOpen = item.classList.contains('open');
            document.querySelectorAll('.faq-item').forEach(other => {
                if (other !== item) {
                    other.classList.remove('open');
                    other.querySelector('.faq-question')?.setAttribute('aria-expanded', 'false');
                }
            });
            item.classList.toggle('open', !isOpen);
            button.setAttribute('aria-expanded', String(!isOpen));
        });
    });

    // Preserve incoming category links using visible sections rather than hiding resources.
    const params = new URLSearchParams(location.search);
    const sectionIds = { school: 'school-classes-section', competitive: 'competitive-exams-section', tools: 'tools-section', live: 'live-batches-container' };
    const sectionId = sectionIds[params.get('tab') || params.get('category')];
    if (sectionId) document.getElementById(sectionId)?.scrollIntoView();

    const top = document.getElementById('backToTop');
    if (top) {
        const update = () => {
            const show = window.scrollY > 300;
            top.classList.toggle('visible', show);
            top.classList.toggle('show', show);
        };
        window.addEventListener('scroll', update, { passive: true });
        update();
    }

    /* =========================================================
       CONTINUE LEARNING WIDGET (Resumes Last Visited Class/Exam)
       ========================================================= */
    function formatStudyRelativeTime(timestamp) {
        if (!timestamp) return 'Recently';
        const elapsedSec = Math.max(0, Math.floor((Date.now() - timestamp) / 1000));
        if (elapsedSec < 90) return 'Just now';
        const elapsedMin = Math.floor(elapsedSec / 60);
        if (elapsedMin < 60) return `${elapsedMin} min${elapsedMin === 1 ? '' : 's'} ago`;
        const elapsedHours = Math.floor(elapsedMin / 60);
        if (elapsedHours < 24) return `${elapsedHours} hour${elapsedHours === 1 ? '' : 's'} ago`;
        const elapsedDays = Math.floor(elapsedHours / 24);
        if (elapsedDays === 1) return 'Yesterday';
        if (elapsedDays < 30) return `${elapsedDays} days ago`;
        const elapsedMonths = Math.floor(elapsedDays / 30);
        return `${elapsedMonths} month${elapsedMonths === 1 ? '' : 's'} ago`;
    }

    function initContinueStudyWidget() {
        const section = document.getElementById('continue-study-section');
        const continueBtn = document.getElementById('continue-study-btn');
        const titleEl = document.getElementById('continue-card-title');
        const catBadge = document.getElementById('continue-category-badge');
        const typeBadge = document.getElementById('continue-type-badge');
        const iconEl = document.getElementById('continue-icon');
        const timeText = document.getElementById('continue-time-text');
        const card = document.getElementById('continue-card');
        const dismissBtn = document.getElementById('continue-dismiss-btn');
        const recentChipsContainer = document.getElementById('continue-recent-chips');
        const chipsList = document.getElementById('continue-chips-list');

        if (!section || !continueBtn) return;

        let lastPage = null;
        try {
            const raw = localStorage.getItem('sjmaths_last_study_page');
            if (raw) lastPage = JSON.parse(raw);
        } catch (e) {
            lastPage = null;
        }

        if (!lastPage || !lastPage.url || typeof lastPage.url !== 'string') {
            section.style.display = 'none';
            return;
        }

        continueBtn.href = lastPage.url;
        if (titleEl) titleEl.textContent = lastPage.title || lastPage.category || 'Study Hub';
        if (catBadge) catBadge.textContent = lastPage.category || 'Study Hub';
        if (typeBadge) typeBadge.textContent = lastPage.badge || (lastPage.type === 'class' ? 'CBSE Curriculum' : 'Competitive Exam');
        if (iconEl && lastPage.icon) iconEl.className = `fas ${lastPage.icon}`;
        if (timeText) timeText.textContent = formatStudyRelativeTime(lastPage.timestamp);

        if (card && lastPage.category) {
            let accentColor = '#16634b';
            let tintColor = '#eaf0e7';
            let borderColor = 'rgba(22, 99, 75, 0.25)';

            if (lastPage.category.includes('Class 10') || lastPage.category.includes('SSC')) {
                accentColor = '#c2410c';
                tintColor = '#fff7ed';
                borderColor = 'rgba(194, 65, 12, 0.25)';
            } else if (lastPage.category.includes('UPSSSC') || lastPage.category.includes('SAT')) {
                accentColor = '#0d9488';
                tintColor = '#f0fdfa';
                borderColor = 'rgba(13, 148, 136, 0.25)';
            } else if (lastPage.category.includes('IB')) {
                accentColor = '#885a17';
                tintColor = '#faf5ea';
                borderColor = 'rgba(136, 90, 23, 0.25)';
            }

            card.style.setProperty('--continue-accent', accentColor);
            card.style.setProperty('--continue-tint', tintColor);
            card.style.setProperty('--continue-border', borderColor);
        }

        // Display secondary recent chips if available
        if (chipsList && recentChipsContainer) {
            try {
                const history = JSON.parse(localStorage.getItem('sjmaths_study_history') || '[]');
                const otherItems = history.filter(h => h && h.url !== lastPage.url && h.path !== lastPage.path).slice(0, 2);
                if (otherItems.length > 0) {
                    chipsList.replaceChildren();
                    otherItems.forEach(item => {
                        const chip = document.createElement('a');
                        chip.className = 'continue-chip-link';
                        chip.href = item.url;
                        const chipIcon = document.createElement('i');
                        chipIcon.className = `fas ${item.icon || 'fa-book'}`;
                        chip.append(chipIcon, document.createTextNode(' ' + (item.title || item.category)));
                        chipsList.append(chip);
                    });
                    recentChipsContainer.style.display = 'flex';
                } else {
                    recentChipsContainer.style.display = 'none';
                }
            } catch (e) {
                recentChipsContainer.style.display = 'none';
            }
        }

        section.style.display = 'block';

        if (dismissBtn && !dismissBtn.dataset.bound) {
            dismissBtn.dataset.bound = 'true';
            dismissBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                try {
                    localStorage.removeItem('sjmaths_last_study_page');
                } catch (err) {}
                section.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
                section.style.opacity = '0';
                section.style.transform = 'translateY(-8px)';
                setTimeout(() => {
                    section.style.display = 'none';
                    section.style.opacity = '';
                    section.style.transform = '';
                }, 260);
            });
        }
    }

    // Capture clicks on all classes and exam links on the homepage
    function bindHomepageStudyLinkTracking() {
        document.addEventListener('click', (event) => {
            const link = event.target.closest('a');
            if (!link || !link.href) return;
            try {
                const url = new URL(link.href, window.location.origin);
                if (url.origin !== window.location.origin) return;

                const tracker = window.SJStudyTracker;
                if (!tracker) return;

                const classification = tracker.classifyStudyPage(url.pathname);
                if (classification) {
                    let label = link.innerText.replace(/\s+/g, ' ').trim();
                    if (!label || label.length < 4 || ['Notes', 'NCERT Solutions', 'Worksheets', 'Chapter Tests', '10Y PYQs', 'Quizzes', 'Board PYQs'].includes(label)) {
                        label = `${classification.category} ${label}`.trim();
                    }
                    tracker.saveStudyPage({
                        url: url.pathname + url.search + url.hash,
                        path: url.pathname,
                        title: label || classification.category,
                        category: classification.category,
                        badge: classification.badge,
                        type: classification.type,
                        icon: classification.icon,
                        timestamp: Date.now()
                    });
                }
            } catch (e) {}
        }, { capture: true });
    }

    initContinueStudyWidget();
    bindHomepageStudyLinkTracking();
    window.addEventListener('pageshow', initContinueStudyWidget);
})();
