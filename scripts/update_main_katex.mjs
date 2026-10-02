import fs from 'fs';
import esbuild from 'esbuild';

const mainPath = 'assets/js/main.js';
let content = fs.readFileSync(mainPath, 'utf8');

const mathSnippet = `
    /* =========================================
       UNIVERSAL MATH TYPESETTING (KaTeX Engine)
       Auto-detects LaTeX math expressions ($...$, $$...$$)
       and dynamically typesets them across all pages
       ========================================= */
    (function () {
        const KATEX_CSS = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css';
        const KATEX_JS = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js';
        const KATEX_AUTO = 'https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js';

        let katexLoaded = false;
        let katexLoading = false;
        const callbacks = [];

        function loadKaTeX(cb) {
            if (window.katex && typeof window.renderMathInElement === 'function') {
                cb();
                return;
            }
            callbacks.push(cb);
            if (katexLoading) return;
            katexLoading = true;

            if (!document.querySelector('link[href*="katex"]')) {
                const link = document.createElement('link');
                link.rel = 'stylesheet';
                link.href = KATEX_CSS;
                link.crossOrigin = 'anonymous';
                document.head.appendChild(link);
            }

            function load(src, next) {
                const s = document.createElement('script');
                s.src = src;
                s.defer = true;
                s.crossOrigin = 'anonymous';
                s.onload = next;
                document.head.appendChild(s);
            }

            load(KATEX_JS, () => {
                load(KATEX_AUTO, () => {
                    katexLoaded = true;
                    katexLoading = false;
                    while (callbacks.length) {
                        try { callbacks.shift()(); } catch (e) {}
                    }
                });
            });
        }

        const options = {
            delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false },
                { left: '\\(', right: '\\)', display: false },
                { left: '\\[', right: '\\]', display: true }
            ],
            ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
            throwOnError: false
        };

        function checkAndRenderMath(root) {
            const el = root || document.body;
            if (!el) return;
            const text = el.textContent || '';
            const html = el.innerHTML || '';
            if (text.includes('$') || html.includes('\\frac') || html.includes('\\sqrt') || html.includes('\\Delta')) {
                loadKaTeX(() => {
                    if (typeof window.renderMathInElement === 'function') {
                        try {
                            window.renderMathInElement(el, options);
                        } catch (e) {}
                    }
                });
            }
        }

        window.renderMath = checkAndRenderMath;

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => checkAndRenderMath());
        } else {
            checkAndRenderMath();
        }

        window.addEventListener('themeChanged', () => checkAndRenderMath());
    })();
`;

if (!content.includes('UNIVERSAL MATH TYPESETTING (KaTeX Engine)')) {
    const lastClosing = content.lastIndexOf('})();');
    if (lastClosing !== -1) {
        content = content.slice(0, lastClosing) + mathSnippet + content.slice(lastClosing);
        fs.writeFileSync(mainPath, content, 'utf8');
        console.log('Appended KaTeX auto-loader to assets/js/main.js');
    }
}

esbuild.buildSync({
    entryPoints: ['assets/js/main.js'],
    outfile: 'assets/js/main.min.js',
    minify: true,
    sourcemap: false,
    write: true
});
console.log('Compiled assets/js/main.min.js successfully (Size: ' + fs.statSync('assets/js/main.min.js').size + ' bytes)');
