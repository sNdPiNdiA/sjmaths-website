/** Homepage interactions. Resource destinations remain ordinary HTML links. */
(() => {
    'use strict';
    // main.js owns theme behaviour; this page only places its existing control.
    function placeThemeControl() {
        const control = document.getElementById('darkToggle');
        const target = document.getElementById('home-theme-control');
        if (control && target) target.append(control);
    }
    if (document.readyState === 'complete') placeThemeControl();
    else document.addEventListener('DOMContentLoaded', placeThemeControl, { once: true });
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
        selectClass(tabs.find(tab => tab.classList.contains('active')) || tabs[0]);
    }
    function selectClass(tab, focus = false) {
        if (!tab) return;
        tabs.forEach(item => {
            const selected = item === tab;
            item.classList.toggle('active', selected);
            if (mobileAccordion.matches) item.setAttribute('aria-expanded', String(selected));
            else item.setAttribute('aria-selected', String(selected));
            item.tabIndex = selected ? 0 : -1;
        });
        if (mobileAccordion.matches) panels.forEach(panel => panelsContainer.append(panel));
        panels.forEach(panel => {
            const selected = panel.id === tab.getAttribute('aria-controls');
            panel.classList.toggle('active', selected);
            panel.hidden = !selected;
            if (selected && mobileAccordion.matches) mobileOptions.get(tab)?.slot.append(panel);
        });
        if (focus) tab.focus();
    }
    setMobileClassLayout(mobileAccordion.matches);
    mobileAccordion.addEventListener('change', event => setMobileClassLayout(event.matches));
    tabs.forEach((tab, index) => {
        tab.addEventListener('click', () => selectClass(tab));
        tab.addEventListener('keydown', event => {
            let next;
            if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
            if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
            if (stackedTabs.matches && event.key === 'ArrowDown') next = (index + 1) % tabs.length;
            if (stackedTabs.matches && event.key === 'ArrowUp') next = (index - 1 + tabs.length) % tabs.length;
            if (event.key === 'Home') next = 0;
            if (event.key === 'End') next = tabs.length - 1;
            if (next !== undefined) {
                event.preventDefault();
                selectClass(tabs[next], true);
            }
        });
    });
    if (tabs.length) selectClass(tabs[0]);

    document.querySelectorAll('.faq-question').forEach((button, index) => {
        const answer = button.closest('.faq-item').querySelector('.faq-answer');
        answer.id = `home-faq-answer-${index}`;
        answer.hidden = true;
        button.setAttribute('aria-controls', answer.id);
        button.addEventListener('click', () => {
            const open = button.getAttribute('aria-expanded') !== 'true';
            document.querySelectorAll('.faq-item').forEach(item => {
                item.classList.remove('open');
                item.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
                item.querySelector('.faq-answer').hidden = true;
            });
            button.closest('.faq-item').classList.toggle('open', open);
            button.setAttribute('aria-expanded', String(open));
            answer.hidden = !open;
        });
    });

    // Preserve incoming category links using visible sections rather than hiding resources.
    const params = new URLSearchParams(location.search);
    const sectionIds = { school: 'school-classes-section', competitive: 'competitive-exams-section', tools: 'tools-section', live: 'live-batches-container' };
    const sectionId = sectionIds[params.get('tab') || params.get('category')];
    if (sectionId) document.getElementById(sectionId)?.scrollIntoView();

    const top = document.getElementById('backToTop');
    if (top) {
        const update = () => top.classList.toggle('visible', window.scrollY > 400);
        window.addEventListener('scroll', update, { passive: true });
        update();
    }
})();
