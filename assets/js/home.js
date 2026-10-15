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
})();
