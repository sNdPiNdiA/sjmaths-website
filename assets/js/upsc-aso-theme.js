(function () {
  'use strict';

  const preferenceKey = 'sjmaths.theme.preference';
  const mediaQuery = window.matchMedia?.('(prefers-color-scheme: dark)');
  const controls = () => document.querySelectorAll('[data-aso-theme-toggle]');
  const isValidPreference = value => ['system', 'light', 'dark'].includes(value);

  const readPreference = () => {
    try {
      const saved = localStorage.getItem(preferenceKey);
      if (isValidPreference(saved)) return saved;

      const legacy = [
        ['sjmaths-dark', { on: 'dark', off: 'light' }],
        ['sjmaths_theme', { dark: 'dark', light: 'light' }],
        ['sj_theme', { dark: 'dark', light: 'light' }],
        ['theme', { dark: 'dark', light: 'light' }],
        ['sjmaths-test-dark', { true: 'dark', false: 'light' }]
      ];
      for (const [key, values] of legacy) {
        const migrated = values[localStorage.getItem(key)];
        if (migrated) {
          localStorage.setItem(preferenceKey, migrated);
          return migrated;
        }
      }
    } catch (error) {
      // Restricted storage falls back to the operating system preference.
    }
    return 'system';
  };

  let preference = window.SJMathsTheme?.getPreference() || readPreference();
  const resolvesDark = value => value === 'dark' || (value === 'system' && Boolean(mediaQuery?.matches));

  const updateControls = isDark => {
    controls().forEach(control => {
      const icon = control.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-sun', isDark);
        icon.classList.toggle('fa-moon', !isDark);
      }
      control.setAttribute('aria-pressed', String(isDark));
      control.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      control.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';
    });
  };

  const apply = value => {
    preference = isValidPreference(value) ? value : 'system';
    const isDark = resolvesDark(preference);
    const root = document.documentElement;
    root.dataset.theme = isDark ? 'dark' : 'light';
    root.dataset.themePreference = preference;
    root.style.colorScheme = isDark ? 'dark' : 'light';
    root.classList.toggle('dark-mode', isDark);
    root.classList.toggle('dark', isDark);
    document.body?.classList.toggle('dark-mode', isDark);
    updateControls(isDark);
    return isDark;
  };

  const savePreference = value => {
    preference = value;
    const isDark = apply(value);
    try {
      localStorage.setItem(preferenceKey, value);
      const resolved = isDark ? 'dark' : 'light';
      localStorage.setItem('sjmaths-dark', isDark ? 'on' : 'off');
      localStorage.setItem('sjmaths_theme', resolved);
      localStorage.setItem('sj_theme', resolved);
      localStorage.setItem('theme', resolved);
      localStorage.setItem('sjmaths-test-dark', String(isDark));
    } catch (error) {
      // The current page remains themed even when persistence is unavailable.
    }
    const detail = { preference, theme: isDark ? 'dark' : 'light', isDark };
    window.dispatchEvent(new CustomEvent('sjmaths:themechange', { detail }));
    window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark } }));
  };

  const syncFromSiteTheme = event => {
    if (event.type === 'themeChanged' && window.SJMathsTheme?.getPreference) {
      preference = window.SJMathsTheme.getPreference();
      apply(preference);
      return;
    }
    if (event?.detail && isValidPreference(event.detail.preference)) {
      preference = event.detail.preference;
      apply(preference);
    } else if (event?.detail && typeof event.detail.isDark === 'boolean') {
      preference = event.detail.isDark ? 'dark' : 'light';
      apply(preference);
    } else if (event?.detail?.theme === 'dark' || event?.detail?.theme === 'light') {
      preference = event.detail.theme;
      apply(preference);
    }
  };

  apply(preference);
  document.addEventListener('DOMContentLoaded', () => apply(preference), { once: true });
  window.addEventListener('sjmaths:themechange', syncFromSiteTheme);
  window.addEventListener('themeChanged', syncFromSiteTheme);
  window.addEventListener('storage', event => {
    if (event.key === preferenceKey) apply(isValidPreference(event.newValue) ? event.newValue : 'system');
  });
  mediaQuery?.addEventListener?.('change', () => {
    if (preference === 'system') apply('system');
  });

  document.addEventListener('click', event => {
    const control = event.target.closest?.('[data-aso-theme-toggle]');
    if (!control || control.matches(':disabled, [aria-disabled="true"]')) return;
    event.preventDefault();
    const next = resolvesDark(preference) ? 'light' : 'dark';
    if (window.SJMathsTheme?.setPreference) window.SJMathsTheme.setPreference(next);
    else savePreference(next);
  });
})();
