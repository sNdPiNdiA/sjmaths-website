export function createHomepageThemeBootstrap(paletteBootstrap) {
    return `(function () {
    const key = 'sjmaths.theme.preference';
    let preference = 'system';
    try {
        preference = localStorage.getItem(key);
        if (!['system', 'light', 'dark'].includes(preference)) {
            const legacy = [
                ['sjmaths-dark', { on: 'dark', off: 'light' }],
                ['sjmaths_theme', { dark: 'dark', light: 'light' }],
                ['sj_theme', { dark: 'dark', light: 'light' }],
                ['theme', { dark: 'dark', light: 'light' }],
                ['sjmaths-test-dark', { true: 'dark', false: 'light' }],
                ['sjmaths-theme', { dark: 'dark', light: 'light' }]
            ];
            for (const [legacyKey, values] of legacy) {
                const migrated = values[localStorage.getItem(legacyKey)];
                if (!migrated) continue;
                preference = migrated;
                localStorage.setItem(key, preference);
                break;
            }
        }
    } catch (error) {
        preference = 'system';
    }
    const dark = preference === 'dark' || (preference === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
    document.documentElement.classList.toggle('dark-mode', dark);
    document.documentElement.classList.toggle('dark', dark);
    document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme-preference', preference);
    document.documentElement.style.colorScheme = dark ? 'dark' : 'light';
    document.body.classList.toggle('dark-mode', dark);
    ${paletteBootstrap}
})();`;
}
