import crypto from 'node:crypto';

export const upUpperPrimaryHeadThemeBootstrap = `const themePreferenceKey = 'sjmaths.theme.preference';
        const themePreference = (() => {
            try {
                const saved = localStorage.getItem(themePreferenceKey);
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
                    localStorage.setItem(themePreferenceKey, migrated);
                    return migrated;
                }
            } catch (error) {}
            return 'system';
        })();
        const isDark = themePreference === 'dark' || (themePreference === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches);
        document.documentElement.classList.toggle('dark-mode', isDark);
        document.documentElement.classList.toggle('dark', isDark);
        document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme-preference', themePreference);
        document.documentElement.style.colorScheme = isDark ? 'dark' : 'light';`;

export const upUpperPrimaryBodyThemeBootstrap = `(function () {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        document.body.classList.toggle('dark-mode', isDark);
    })();`;

export const upUpperPrimaryBootstrapFingerprints = Object.freeze({
    englishSanskritHead: 'ffc3813758fac61192caf3564b67c4edda36a22541f1046b5e896f4b12792599',
    englishSanskritBody: '8421652eac121bc6c1e00ec0df14c868e6c8d609c23d43f1c6415b9c072f7187',
    hindiHead: '6d530f9ce467ccde9ac56feba52f89b18b77f16cfaea12b003f5d7ec72f3ac30',
    hindiBody: 'e711170bd23042292ab0a9b765f80466c5dcef187bddab3c340ec318274288bf'
});

const digest = source => crypto.createHash('sha256').update(source.trim()).digest('hex');

export function migrateUpUpperPrimaryThemeBootstraps(html) {
    const counts = { englishSanskritHead: 0, englishSanskritBody: 0, hindiHead: 0, hindiBody: 0 };
    const output = html.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attributes, source) => {
        if (/\bsrc\s*=|\btype\s*=|\bdefer\b|\basync\b/i.test(attributes)) return tag;
        const hash = digest(source);
        if (hash === upUpperPrimaryBootstrapFingerprints.englishSanskritHead || hash === upUpperPrimaryBootstrapFingerprints.hindiHead) {
            const group = hash === upUpperPrimaryBootstrapFingerprints.hindiHead ? 'hindiHead' : 'englishSanskritHead';
            const paletteStart = source.indexOf('const savedTheme = localStorage.getItem');
            if (paletteStart < 0) throw new Error(`Known ${group} bootstrap lost its palette block.`);
            counts[group]++;
            return `<script>(function () {\n        ${upUpperPrimaryHeadThemeBootstrap}\n        ${source.slice(paletteStart)}</script>`;
        }
        if (hash === upUpperPrimaryBootstrapFingerprints.englishSanskritBody || hash === upUpperPrimaryBootstrapFingerprints.hindiBody) {
            const group = hash === upUpperPrimaryBootstrapFingerprints.hindiBody ? 'hindiBody' : 'englishSanskritBody';
            counts[group]++;
            return `<script>${upUpperPrimaryBodyThemeBootstrap}</script>`;
        }
        return tag;
    });
    return { html: output, counts };
}
