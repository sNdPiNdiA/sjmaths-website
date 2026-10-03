import fs from 'fs';
import path from 'path';

const KATEX_HEAD_BLOCK = `<!-- KaTeX for High-Fidelity Mathematical & Scientific Typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous"/>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof renderMathInElement === 'function' && !window.SJMathsMathMarkup?.mathJaxPresent) {
            window.SJMathsMathMarkup?.prepare(document.body);
            renderMathInElement(document.body, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\\\(', right: '\\\\)', display: false },
                    { left: '\\\\[', right: '\\\\]', display: true }
                ],
                ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option'],
                throwOnError: false
            });
        }
    });
</script>`;

function hasMathExpression(html) {
    return /\$[a-zA-Z0-9\\(+\-\^_\s\.\/]{2,}\$/.test(html) ||
           html.includes('\\frac{') ||
           html.includes('\\sqrt{') ||
           html.includes('\\Delta') ||
           html.includes('\\times') ||
           html.includes('\\pm') ||
           html.includes('\\equiv') ||
           html.includes('\\sum') ||
           html.includes('\\int');
}

const targetDirs = [
    'up-upper-primary-teacher',
    'class-9-maths',
    'class-10-maths',
    'class-11-maths',
    'class-12-maths',
    'class-9-science',
    'class-10-science',
    'class-11-physics',
    'class-12-physics',
    'class-11-chemistry',
    'physics',
    'chemistry',
    'mathematics'
];

let globalStats = { checked: 0, updated: 0, mathCount: 0 };

function processDirectory(dir) {
    if (!fs.existsSync(dir)) return;
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
        const fullPath = path.join(dir, entry.name);

        if (entry.isDirectory()) {
            if (['node_modules', '.git', 'dist', 'build', '.gemini', 'assets'].includes(entry.name)) continue;
            processDirectory(fullPath);
        } else if (entry.name.endsWith('.html')) {
            globalStats.checked++;
            let html = fs.readFileSync(fullPath, 'utf8');

            const hasMath = hasMathExpression(html);
            if (!hasMath) continue;
            globalStats.mathCount++;
            const hasMathJax = /<script\b(?=[^>]*\bsrc=["'][^"']*mathjax[^"']*["'])[^>]*>/i.test(html);
            const hasCustomMathMarkup = /<span\b[^>]*\bclass=["'][^"']*\bmath-(?:frac|sqrt)\b/i.test(html);

            let modified = false;

            // 1. Remove old broken KaTeX tags or old auto-render scripts
            if (html.includes('katex.min.js') || html.includes('katex.min.css') || html.includes('renderMathInElement')) {
                const cleanedHtml = html
                    .replace(/<!-- KaTeX[^>]*-->[\s\r\n]*/gi, '')
                    .replace(/<link[^>]*href="[^"]*katex[^"]*"[^>]*\/?>[\s\r\n]*/gi, '')
                    .replace(/<script[^>]*src="[^"]*katex[^"]*"[^>]*><\/script>[\s\r\n]*/gi, '')
                    .replace(/<script[^>]*src="[^"]*auto-render[^"]*"[^>]*><\/script>[\s\r\n]*/gi, '')
                    .replace(/<script[^>]*renderMathInElement[\s\S]*?<\/script>[\s\r\n]*/gi, '');

                if (cleanedHtml !== html) {
                    html = cleanedHtml;
                    modified = true;
                }
            }

            // 2. Insert KaTeX only when MathJax is not already typesetting the page.
            if (!hasMathJax && !html.includes('https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css')) {
                if (html.includes('</head>')) {
                    html = html.replace('</head>', () => `${KATEX_HEAD_BLOCK}\n</head>`);
                    modified = true;
                } else if (/<body[^>]*>/i.test(html)) {
                    html = html.replace(/<body[^>]*>/i, (m) => `${KATEX_HEAD_BLOCK}\n${m}`);
                    modified = true;
                } else {
                    html = `${KATEX_HEAD_BLOCK}\n` + html;
                    modified = true;
                }
            }

            if (hasCustomMathMarkup && !html.includes('/assets/js/math-markup-compat.js')) {
                if (hasMathJax) {
                    throw new Error(`Custom math markup needs compatibility setup before MathJax: ${fullPath}`);
                }
                const headClose = html.toLowerCase().lastIndexOf('</head>');
                if (headClose < 0) throw new Error(`Custom math markup needs a helper script but </head> is missing: ${fullPath}`);
                html = `${html.slice(0, headClose)}<script defer src="/assets/js/math-markup-compat.js"></script>\n${html.slice(headClose)}`;
                modified = true;
            }

            // Math-rendering cannot cross nested HTML fraction/radical spans.
            // Load the tiny bridge only on pages that contain those wrappers.
            if (/\bmath-(?:frac|sqrt)\b/.test(html) && !html.includes('/assets/js/math-markup-compat.js')) {
                const helperTag = '<script src="/assets/js/math-markup-compat.js"></script>';
                const mathJaxScript = /<script\b[^>]*id=["']MathJax-script["'][^>]*>/i.exec(html);
                if (mathJaxScript) {
                    html = `${html.slice(0, mathJaxScript.index)}${helperTag}\n${html.slice(mathJaxScript.index)}`;
                    modified = true;
                } else if (html.includes('</head>')) {
                    const deferredHelper = '<script defer src="/assets/js/math-markup-compat.js"></script>';
                    html = html.replace('</head>', () => `${deferredHelper}\n</head>`);
                    modified = true;
                } else if (/<body[^>]*>/i.test(html)) {
                    html = html.replace(/<body[^>]*>/i, (match) => `<script defer src="/assets/js/math-markup-compat.js"></script>\n${match}`);
                    modified = true;
                }
            }

            // 3. Ensure up-upper-primary-topic.min.js has the latest cache-buster
            if (html.includes('up-upper-primary-topic.min.js') && !html.includes('up-upper-primary-topic.min.js?v=20261002_02')) {
                html = html.replace(
                    /\/assets\/js\/up-upper-primary-topic\.min\.js(\?v=[a-zA-Z0-9_\-]+)?/g,
                    () => '/assets/js/up-upper-primary-topic.min.js?v=20261002_02'
                );
                modified = true;
            }

            // Verify integrity of the injected block
            if (!html.includes("delimiters: [") || !html.includes("left: '$$'")) {
                console.error(`ERROR: KaTeX block corrupted in ${fullPath}!`);
                process.exit(1);
            }

            if (modified) {
                fs.writeFileSync(fullPath, html, 'utf8');
                globalStats.updated++;
            }
        }
    }
}

console.log('================================================================');
console.log('Safe KaTeX 0.16.11 Deployment Across All Math & Science Topics');
console.log(`Scanning targets: ${targetDirs.join(', ')}`);
console.log('================================================================\n');

for (const t of targetDirs) {
    processDirectory(path.join(process.cwd(), t));
}

console.log('\n================================================================');
console.log(`Scan & Fix Complete:`);
console.log(`Total HTML Files Examined: ${globalStats.checked}`);
console.log(`Files Containing Math Expressions: ${globalStats.mathCount}`);
console.log(`Files Successfully Updated With KaTeX: ${globalStats.updated}`);
console.log('================================================================');
