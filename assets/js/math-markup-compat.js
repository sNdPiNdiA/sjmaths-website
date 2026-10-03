(() => {
  'use strict';

  const mathSpanSelector = 'span.math-frac, span.math-sqrt';
  const textBlockSelector = 'p, li, td, th, h1, h2, h3, h4, h5, h6';

  function delimiterAt(text) {
    let mode = null;
    for (const match of text.matchAll(/\\\(|\\\)|\\\[|\\\]|\$\$|\$/g)) {
      const token = match[0];
      if ((token === '$' || token === '$$') && text[match.index - 1] === '\\') continue;
      if (token === '$' || token === '$$') {
        if (mode === token) mode = null;
        else if (!mode) mode = token;
      } else if (token === '\\(' || token === '\\[') mode = token;
      else if ((token === '\\)' && mode === '\\(') || (token === '\\]' && mode === '\\[')) mode = null;
    }
    return mode;
  }

  function texContent(node) {
    if (node.nodeType === Node.TEXT_NODE) return node.data;
    if (node.nodeType !== Node.ELEMENT_NODE) return '';

    if (node.matches('sub, .math-sub')) return `_{${[...node.childNodes].map(texContent).join('')}}`;
    if (node.matches('sup, .math-sup')) return `^{${[...node.childNodes].map(texContent).join('')}}`;

    if (node.matches('span.math-frac')) {
      const numerator = [...node.children].find(child => child.matches('.math-num'));
      const denominator = [...node.children].find(child => child.matches('.math-denom'));
      if (numerator && denominator) return `\\frac{${texContent(numerator)}}{${texContent(denominator)}}`;
    }
    if (node.matches('span.math-sqrt')) {
      const radicand = [...node.children].find(child => child.matches('.math-radicand'));
      if (radicand) return `\\sqrt{${texContent(radicand)}}`;
    }
    return [...node.childNodes].map(texContent).join('');
  }

  function prepare(root = document.body) {
    if (!root?.querySelectorAll) return 0;
    const candidates = [...root.querySelectorAll(mathSpanSelector)].filter(node =>
      !node.parentElement?.closest(mathSpanSelector)
    );
    const touchedBlocks = new Set();
    let converted = 0;

    for (const node of candidates) {
      const block = node.closest(textBlockSelector) || node.parentElement;
      if (!block) continue;
      const range = document.createRange();
      range.selectNodeContents(block);
      range.setEndBefore(node);
      const insideMath = Boolean(delimiterAt(range.toString()));
      const hasNativeLayout = (() => {
        if (typeof window.getComputedStyle !== 'function') return false;
        const style = window.getComputedStyle(node);
        if (style.display !== 'inline-flex' && style.display !== 'flex') return false;
        if (node.matches('span.math-frac')) {
          const numerator = node.querySelector('.math-num');
          const denominator = node.querySelector('.math-denom');
          return Boolean(numerator && denominator
            && window.getComputedStyle(numerator).display === 'block'
            && window.getComputedStyle(denominator).display === 'block');
        }
        return Boolean(node.querySelector('.math-radicand'));
      })();
      const tex = texContent(node);

      node.replaceWith(document.createTextNode(insideMath || hasNativeLayout ? tex : `$${tex}$`));
      block.normalize();
      touchedBlocks.add(block);
      converted++;
    }

    for (const block of touchedBlocks) {
      const openDelimiter = delimiterAt(block.textContent || '');
      const closingDelimiter = openDelimiter === '$' ? '$'
        : openDelimiter === '$$' ? '$$'
        : openDelimiter === '\\(' ? '\\)'
        : openDelimiter === '\\[' ? '\\]' : '';
      if (closingDelimiter) block.append(document.createTextNode(closingDelimiter));
    }
    return converted;
  }

  const currentScript = document.currentScript;
  const mathJaxPresent = currentScript?.dataset.mathjax === 'true';
  window.SJMathsMathMarkup = Object.freeze({ prepare, mathJaxPresent });

  // MathJax 3 must receive continuous TeX before its initial typeset. Install
  // the hook before the async MathJax script is loaded on compatible pages.
  if (mathJaxPresent) {
    const config = window.MathJax || {};
    const startup = { ...(config.startup || {}) };
    const originalPageReady = startup.pageReady;
    startup.pageReady = function (...args) {
      const continueStartup = () => {
        prepare(document.body);
        if (typeof originalPageReady === 'function') return originalPageReady.apply(this, args);
        return window.MathJax.startup.defaultPageReady();
      };
      if (document.readyState !== 'loading') return continueStartup();
      return new Promise(resolve => {
        document.addEventListener('DOMContentLoaded', () => resolve(continueStartup()), { once: true });
      });
    };
    window.MathJax = { ...config, startup };
  } else {
    // Register before page renderers (which are loaded later in the document)
    // so custom HTML wrappers become continuous TeX before KaTeX auto-render.
    // Some legacy pages have a malformed or skipped inline renderer callback;
    // render directly when KaTeX is already available, while leaving the shared
    // main.js renderer in control on pages that use it.
    const prepareWhenReady = () => {
      prepare(document.body);
      if (typeof window.renderMath === 'function' || typeof window.renderMathInElement !== 'function') return;
      window.renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false },
          { left: '\\[', right: '\\]', display: true }
        ],
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option'],
        throwOnError: false
      });
    };
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', prepareWhenReady, { once: true });
    } else {
      prepareWhenReady();
    }
  }
})();
