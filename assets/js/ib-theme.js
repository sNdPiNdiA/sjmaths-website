(function () {
    'use strict';

    const preferenceKey = 'sjmaths.theme.preference';
    const toggleSelector = '#theme-toggle, #darkToggle, #themeToggle, #darkModeToggleBtn, [data-action="toggle-dark"], .theme-toggle';
    const mediaQuery = window.matchMedia?.('(prefers-color-scheme: dark)');

    function readPreference() {
        try {
            const saved = localStorage.getItem(preferenceKey);
            if (['system', 'light', 'dark'].includes(saved)) return saved;
            const legacy = [
                ['sjmaths-dark', { on: 'dark', off: 'light' }],
                ['sjmaths_theme', { dark: 'dark', light: 'light' }],
                ['sj_theme', { dark: 'dark', light: 'light' }],
                ['theme', { dark: 'dark', light: 'light' }],
                ['sjmaths-test-dark', { true: 'dark', false: 'light' }],
                ['sjmaths-theme', { dark: 'dark', light: 'light' }]
            ];
            for (const [key, values] of legacy) {
                const migrated = values[localStorage.getItem(key)];
                if (!migrated) continue;
                localStorage.setItem(preferenceKey, migrated);
                return migrated;
            }
        } catch (error) {
            // Use the system preference when browser storage is unavailable.
        }
        return 'system';
    }

    let preference = readPreference();

    function isDark(value = preference) {
        return value === 'dark' || (value === 'system' && Boolean(mediaQuery?.matches));
    }

    function syncButtons(dark) {
        document.querySelectorAll(toggleSelector).forEach(button => {
            const icon = button.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-sun', dark);
                icon.classList.toggle('fa-moon', !dark);
            }
            button.setAttribute('aria-pressed', String(dark));
            button.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
            button.title = dark ? 'Switch to light theme' : 'Switch to dark theme';
        });
    }

    function apply(announce = true) {
        const dark = isDark();
        const theme = dark ? 'dark' : 'light';
        document.documentElement.classList.toggle('dark-mode', dark);
        document.documentElement.classList.toggle('dark', dark);
        document.documentElement.setAttribute('data-theme', theme);
        document.documentElement.setAttribute('data-theme-preference', preference);
        document.documentElement.style.colorScheme = theme;
        document.body?.classList.toggle('dark-mode', dark);
        syncButtons(dark);
        if (announce) {
            const detail = { preference, theme, isDark: dark };
            window.dispatchEvent(new CustomEvent('sjmaths:themechange', { detail }));
            window.dispatchEvent(new CustomEvent('themeChanged', { detail: { isDark: dark } }));
        }
    }

    function syncLegacyPreference() {
        try {
            const dark = isDark();
            const compatibility = dark ? 'dark' : 'light';
            localStorage.setItem('sjmaths-dark', dark ? 'on' : 'off');
            localStorage.setItem('sjmaths_theme', compatibility);
            localStorage.setItem('sj_theme', compatibility);
            localStorage.setItem('theme', compatibility);
            localStorage.setItem('sjmaths-test-dark', String(dark));
        } catch (error) {
            // Theme changes remain available in memory if compatibility writes fail.
        }
    }

    function setPreference(next, persist = true) {
        if (!['system', 'light', 'dark'].includes(next)) return;
        preference = next;
        if (persist) {
            try {
                localStorage.setItem(preferenceKey, next);
            } catch (error) {
                // The current page still follows the in-memory preference.
            }
            syncLegacyPreference();
        }
        apply();
    }

    apply(false);
    document.addEventListener('click', event => {
        const button = event.target.closest(toggleSelector);
        if (!button || button.matches(':disabled, [aria-disabled="true"]')) return;
        event.preventDefault();
        setPreference(isDark() ? 'light' : 'dark');
    });
    window.addEventListener('storage', event => {
        if (event.key !== preferenceKey) return;
        preference = ['system', 'light', 'dark'].includes(event.newValue) ? event.newValue : 'system';
        apply();
    });
    mediaQuery?.addEventListener?.('change', () => {
        if (preference === 'system') {
            syncLegacyPreference();
            apply();
        }
    });
})();
