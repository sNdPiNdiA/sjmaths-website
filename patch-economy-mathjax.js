const fs = require('fs');
const path = require('path');

// Build the MathJax block as an array and join — avoids ALL $ interpretation issues
// The $ in ['$','$'] would be mangled by str.replace() if used directly
const lines = [
    '',
    '    <!-- MathJax for rendering LaTeX math formulas -->',
    '    <script>',
    '        window.MathJax = {',
    '            tex: {',
    // We write the JS string chars individually so Node never sees $' as a replace pattern
    "                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],",
    "                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],",
    '                processEscapes: true',
    '            },',
    '            options: {',
    "                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']",
    '            }',
    '        };',
    '    <\/script>',
    '    <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"><\/script>',
    ''
];
const mathjaxBlock = lines.join('\n');

const economyDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness/economy';

const topicDirs = fs.readdirSync(economyDir).filter(d =>
    fs.statSync(path.join(economyDir, d)).isDirectory()
);

let patched = 0;
for (const dir of topicDirs) {
    const filePath = path.join(economyDir, dir, 'index.html');
    if (!fs.existsSync(filePath)) continue;

    let html = fs.readFileSync(filePath, 'utf8');

    // 1. Strip ALL previous broken MathJax injections
    //    Remove any <!-- MathJax ... --> comment + surrounding script tags
    html = html.replace(/\n?\s*<!-- MathJax for rendering[\s\S]*?<\/script>/g, '');
    html = html.replace(/\n?\s*<script[^>]*mathjax[^>]*><\/script>/g, '');

    // 2. Verify </head> exists
    if (!html.includes('<\/head>')) {
        console.warn('No </head> in: ' + filePath);
        continue;
    }

    // 3. Inject BEFORE </head> using a replacer function (avoids $ issues in replacement string)
    html = html.replace('<\/head>', function() {
        return mathjaxBlock + '<\/head>';
    });

    fs.writeFileSync(filePath, html, 'utf8');
    console.log('Fixed: ' + dir);
    patched++;
}

console.log('\nDone! Fixed ' + patched + ' / ' + topicDirs.length + ' economy pages.');
