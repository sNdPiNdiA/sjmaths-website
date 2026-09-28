/* Shared mobile navigation for generated subject/topic pages. */
(function () {
  'use strict';

  function initTopicMobileNav() {
    const header = document.querySelector('.site-header');
    const inner = header?.querySelector('.header-inner');
    let actions = header?.querySelector('.header-actions');
    if (!actions && header) {
      const existingBack = header.querySelector('a.back-btn, a.back');
      if (existingBack) {
        actions = document.createElement('div');
        actions.className = 'header-actions';
        existingBack.replaceWith(actions);
        actions.appendChild(existingBack);
      }
    }
    if (!header || !inner || !actions || document.getElementById('topic-mobile-nav')) return;

    const toggle = document.createElement('button');
    toggle.type = 'button';
    toggle.className = 'topic-mobile-toggle';
    toggle.setAttribute('aria-controls', 'topic-mobile-nav');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open topic navigation');
    toggle.innerHTML = '<span aria-hidden="true">☰</span><span class="topic-mobile-toggle-label">Menu</span>';
    actions.appendChild(toggle);

    const nav = document.createElement('nav');
    nav.id = 'topic-mobile-nav';
    nav.className = 'topic-mobile-nav';
    nav.setAttribute('aria-label', 'Topic navigation');

    const links = [];
    const addLink = (href, label) => {
      if (!href || !label || links.some(link => link.href === href)) return;
      links.push({ href, label });
    };
    addLink('/', 'SJMaths home');
    header.querySelectorAll('a.back-btn, a.back, a[href*="tracker"]').forEach(link => {
      addLink(link.getAttribute('href'), link.textContent.replace(/\s+/g, ' ').trim());
    });
    links.forEach(({ href, label }) => {
      const link = document.createElement('a');
      link.href = href;
      link.textContent = label;
      nav.appendChild(link);
    });
    inner.appendChild(nav);

    const setOpen = open => {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close topic navigation' : 'Open topic navigation');
      toggle.querySelector('span')?.replaceChildren(document.createTextNode(open ? '×' : '☰'));
    };

    toggle.addEventListener('click', event => {
      event.stopPropagation();
      setOpen(!nav.classList.contains('is-open'));
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) {
        setOpen(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', event => {
      if (nav.classList.contains('is-open') && !nav.contains(event.target) && !toggle.contains(event.target)) {
        setOpen(false);
      }
    });
    window.addEventListener('resize', () => {
      if (window.innerWidth > 700) setOpen(false);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTopicMobileNav, { once: true });
  } else {
    initTopicMobileNav();
  }
}());
