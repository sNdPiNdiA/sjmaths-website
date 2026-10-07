/* Dock page-level tabs above the mobile navigation, outside animated page containers. */
(() => {
  'use strict';
  const query = '.study-tabs, .study-tabs-strip, .slide-tabs-strip, .tab-strip, .tabs, .tabs-nav, .tab-nav-list, .tabs-container, .tabs-bar, #mainTabNav, nav.sticky:has(.tab-btn), .topic-tablist, .ca-dashboard-tabs, .diff-tab-bar, [role="tablist"]';
  const mobile = window.matchMedia('(max-width: 768px)');
  const records = new Map();
  let observer;
  let fallbackStyle;
  let dockStylesheet;

  function ensureDockStylesheet() {
    if (document.querySelector('link[href*="/assets/css/mobile-tab-dock.css"]') || dockStylesheet) return;
    dockStylesheet = document.createElement('link');
    dockStylesheet.rel = 'stylesheet';
    dockStylesheet.href = '/assets/css/mobile-tab-dock.css?v=20261006-mobile-tab-dock-v3';
    document.head.appendChild(dockStylesheet);
  }

  function readVariables(context) {
    const variables = new Map();
    const ancestors = [];
    for (let ancestor = context; ancestor; ancestor = ancestor.parentElement) ancestors.push(ancestor);
    for (const ancestor of ancestors.reverse()) {
      const computed = getComputedStyle(ancestor);
      for (let index = 0; index < computed.length; index++) {
        const name = computed[index];
        if (name.startsWith('--')) variables.set(name, computed.getPropertyValue(name));
      }
    }
    return variables;
  }

  function preserveVariables(element, context) {
    const variables = readVariables(context);
    const original = new Map();
    const copied = new Set();
    for (const [name, value] of variables) {
      original.set(name, element.style.getPropertyValue(name));
      if (!original.get(name)) {
        element.style.setProperty(name, value);
        copied.add(name);
      }
    }
    return { original, copied };
  }

  function refreshVariables(element, record) {
    const context = record.placeholder.parentElement;
    if (!context) return;
    const variables = readVariables(context);
    for (const name of record.variables.copied) {
      if (variables.has(name)) element.style.setProperty(name, variables.get(name));
    }
  }

  function applyControlStyles(element, record) {
    const controls = element.querySelectorAll(':scope > :is(button, a, [role="tab"], .tab, .tab-btn, .study-tab-btn), :scope > * > :is(button, a, [role="tab"], .tab, .tab-btn, .study-tab-btn)');
    const enforced = { flex: '1 1 0%', 'min-width': '0', 'min-height': '44px', 'white-space': 'nowrap', 'touch-action': 'manipulation' };
    for (const control of controls) {
      if (!record.controls.has(control)) {
        const original = new Map();
        for (const property of Object.keys(enforced)) {
          original.set(property, { value: control.style.getPropertyValue(property), priority: control.style.getPropertyPriority(property) });
        }
        record.controls.set(control, original);
      }
      for (const [property, value] of Object.entries(enforced)) control.style.setProperty(property, value, 'important');
    }
    applyCompactLabels(controls, record);
  }

  function compactLabel(control, index, text) {
    const fullText = (text || control.innerText || control.textContent || '').replace(/\s+/g, ' ').trim();
    const source = fullText.toLowerCase();
    const hindi = /[\u0900-\u097f]/.test(fullText);
    const labels = [
      [/quiz|mcq|प्रश्नोत्तरी|क्विज़|क्विज/, hindi ? 'क्विज़' : 'Quiz'],
      [/mini.?test|mock.?test|\btests?\b|मिनी.?टेस्ट|मॉक.?टेस्ट|परीक्षा/, hindi ? 'टेस्ट' : 'Test'],
      [/revision|review|revise|पुनरावृत्ति|रिवीजन|दोहराव/, hindi ? 'रिवीजन' : 'Review'],
      [/exercise|practice|अभ्यास|प्रश्न/, hindi ? 'अभ्यास' : 'Practice'],
      [/concept|theor|lesson|notes?|study|learn|अवधारणा|सिद्धांत|नोट्स|पाठ/, hindi ? 'सीखें' : 'Learn'],
      [/safety|aviation|accident|सुरक्षा/, hindi ? 'सुरक्षा' : 'Safety'],
      [/mind.?map|मानचित्र/, hindi ? 'मानचित्र' : 'Map'],
      [/syllabus|पाठ्यक्रम|सिलेबस/, hindi ? 'सिलेबस' : 'Topics'],
      [/video|वीडियो/, hindi ? 'वीडियो' : 'Video'],
      [/solution|solved|हल|समाधान/, hindi ? 'हल' : 'Solve'],
      [/pyq|previous.?year|पिछले.?वर्ष/, hindi ? 'PYQ' : 'PYQs']
    ];
    for (const [pattern, label] of labels) if (pattern.test(source)) return label;
    const firstWord = fullText.replace(/^\s*\d+[.)-]?\s*/, '').split(/[\s:–—/|,(]+/)[0];
    if (firstWord) return firstWord.length > 9 ? `${firstWord.slice(0, 8)}…` : firstWord;
    return `Tab ${index + 1}`;
  }

  function applyCompactLabels(controls, record) {
    controls.forEach((control, index) => {
      const language = document.body.classList.contains('lang-hi') ? 'hi' : 'en';
      if (record.labels.has(control)) {
        const original = record.labels.get(control);
        if (document.body.classList.contains('exam-ui') && original.language !== language) {
          const copy = document.createElement('div');
          copy.innerHTML = original.html;
          copy.querySelectorAll(language === 'hi' ? '.lang-en:not(.lang-hi)' : '.lang-hi:not(.lang-en)').forEach(element => element.remove());
          const text = copy.textContent.replace(/\s+/g, ' ').trim();
          control.querySelector('.sj-mobile-tab-label').textContent = compactLabel(control, index, text);
          control.setAttribute('aria-label', text);
          control.setAttribute('title', text);
          original.language = language;
        }
        return;
      }
      const original = {
        html: control.innerHTML,
        ariaLabel: control.getAttribute('aria-label'),
        title: control.getAttribute('title'),
        language
      };
      const fullText = (control.innerText || control.textContent || '').replace(/\s+/g, ' ').trim();
      record.labels.set(control, original);
      if (fullText) {
        control.setAttribute('aria-label', fullText);
        control.setAttribute('title', fullText);
      }
      const label = document.createElement('span');
      label.className = 'sj-mobile-tab-label';
      label.textContent = compactLabel(control, index);
      control.replaceChildren(label);
    });
  }

  function restoreCompactLabels(record) {
    for (const [control, original] of record.labels) {
      control.innerHTML = original.html;
      if (original.ariaLabel === null) control.removeAttribute('aria-label');
      else control.setAttribute('aria-label', original.ariaLabel);
      if (original.title === null) control.removeAttribute('title');
      else control.setAttribute('title', original.title);
    }
  }

  function restoreControlStyles(record) {
    for (const [control, original] of record.controls) {
      for (const [property, state] of original) {
        if (state.value) control.style.setProperty(property, state.value, state.priority);
        else control.style.removeProperty(property);
      }
    }
  }

  function addFallbackStyles() {
    if (document.querySelector('link[href*="component.min.css"], link[href*="component.css"]') || fallbackStyle) return;
    fallbackStyle = document.createElement('style');
    fallbackStyle.textContent = `@media(max-width:768px){body:has(.sj-mobile-tab-dock){padding-bottom:calc(164px + env(safe-area-inset-bottom,0px))!important}.sj-mobile-tab-dock{position:fixed!important;inset:auto 0 env(safe-area-inset-bottom,0px)!important;z-index:9998!important;box-sizing:border-box!important;display:flex!important;flex-wrap:nowrap!important;align-items:center;justify-content:space-between!important;gap:.2rem!important;width:100%!important;max-width:100vw!important;min-height:60px;max-height:84px;margin:0!important;padding:.4rem max(.35rem,env(safe-area-inset-left,0px))!important;overflow:hidden!important;border:1px solid #d9ddd1;border-right:0;border-bottom:0;border-left:0;border-radius:12px 12px 0 0;background:#fffdf8!important;box-shadow:0 -8px 24px rgba(15,23,42,.12);backdrop-filter:blur(16px)}body:has(.mobile-bottom-nav) .sj-mobile-tab-dock{inset-block-end:calc(72px + env(safe-area-inset-bottom,0px))!important}.sj-mobile-tab-dock>:is(button,a,[role=tab],.tab,.tab-btn,.study-tab-btn),.sj-mobile-tab-dock>* >:is(button,a,[role=tab],.tab,.tab-btn,.study-tab-btn){flex:1 1 0%!important;min-width:0!important;min-height:44px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;touch-action:manipulation}.sj-mobile-tab-label{display:block;max-width:100%;overflow:hidden;text-overflow:ellipsis;font-size:clamp(.75rem,3vw,.875rem);line-height:1.1;text-align:center}}`;
    document.head.appendChild(fallbackStyle);
  }

  function dock() {
    if (!document.body) return;
    if (!mobile.matches) {
      for (const [element, record] of records) {
        element.classList.remove('sj-mobile-tab-dock');
        restoreCompactLabels(record);
        restoreControlStyles(record);
        for (const [name, value] of record.variables.original) {
          if (value) element.style.setProperty(name, value);
          else element.style.removeProperty(name);
        }
        if (record.placeholder.parentNode) record.placeholder.parentNode.replaceChild(element, record.placeholder);
      }
      records.clear();
      return;
    }
    addFallbackStyles();
    const candidates = [...document.querySelectorAll(query)].filter(element => !element.closest('.sj-mobile-tab-dock') && element.dataset.mobileTabDock !== 'off');
    const roots = candidates.filter(element => !candidates.some(other => other !== element && other.contains(element)));
    for (const element of roots) {
      if (records.has(element) || !element.parentNode) continue;
      const placeholder = document.createComment('mobile tab dock placeholder');
      element.parentNode.insertBefore(placeholder, element);
      const variables = preserveVariables(element, placeholder.parentElement);
      element.classList.add('sj-mobile-tab-dock');
      document.body.appendChild(element);
      const record = { placeholder, variables, controls: new Map(), labels: new Map() };
      records.set(element, record);
      applyControlStyles(element, record);
    }
    for (const [element, record] of records) applyControlStyles(element, record);
  }

  function start() {
    ensureDockStylesheet();
    dock();
    observer = new MutationObserver(dock);
    observer.observe(document.body, { childList: true, subtree: true });
    const themeObserver = new MutationObserver(() => {
      for (const [element, record] of records) {
        refreshVariables(element, record);
        if (document.body.classList.contains('exam-ui')) applyControlStyles(element, record);
      }
    });
    for (const root of [document.documentElement, document.body]) {
      themeObserver.observe(root, { attributes: true, attributeFilter: ['class', 'data-theme'] });
    }
    mobile.addEventListener('change', dock);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
