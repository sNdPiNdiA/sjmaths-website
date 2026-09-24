const fs = require('fs');
const path = require('path');

const MATHJAX_CONFIG_SNIPPET = `<script>
    window.MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
            displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
            processEscapes: true,
            processEnvironments: true
        },
        options: {
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        },
        svg: {
            fontCache: 'global'
        }
    };
</script>`;

async function run() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  console.log(`Applying MathJax, UI & UX fixes across ${existingDays.length} generated Day pages...\n`);

  let modifiedCount = 0;

  for (const d of existingDays) {
    let html = fs.readFileSync(d.outputPath, 'utf8');
    const originalHtml = html;

    // 1. Strip polyfill.io
    html = html.replace(/<script\s+src="https:\/\/polyfill\.io\/[^"]*"[^>]*><\/script>\s*/gi, '');

    // 2. Fix MathJax configuration
    const hasMathJaxScript = html.includes('tex-mml-chtml.js') || html.includes('mathjax');
    const hasInlineConfig = html.includes("['$', '$']") || html.includes('["$", "$"]');

    if (hasMathJaxScript && !hasInlineConfig) {
      // Find the MathJax script tag
      const scriptRegex = /(<script[^>]*src="[^"]*mathjax[^"]*"[^>]*><\/script>|<script\s+id="MathJax-script"[^>]*><\/script>)/i;
      if (scriptRegex.test(html)) {
        html = html.replace(scriptRegex, `${MATHJAX_CONFIG_SNIPPET}\n    $1`);
      }
    }

    // 3. Fix switchTab to invoke MathJax.typesetPromise
    if (html.includes('function switchTab') && !html.includes('MathJax.typesetPromise')) {
      // Look for switchTab function body and insert before window.scrollTo or closing brace
      if (html.includes('window.scrollTo')) {
        html = html.replace(/(function\s+switchTab\s*\([^)]*\)\s*\{[\s\S]*?)(window\.scrollTo)/, (match, p1, p2) => {
          return `${p1}if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }\n            ${p2}`;
        });
      } else {
        html = html.replace(/(function\s+switchTab\s*\([^)]*\)\s*\{[\s\S]*?)(\n\s*\})/, (match, p1, p2) => {
          return `${p1}\n            if (window.MathJax && window.MathJax.typesetPromise) { window.MathJax.typesetPromise(); }${p2}`;
        });
      }
    }

    // 4. Specific LaTeX delimiter fixes
    html = html.replace(/\\\((\\rho_s)\$/g, '\\($1\\)');
    html = html.replace(/\\\(q_\\infty\s*=\s*\\frac\{1\}\{2\}\\rho V_\\infty\^2\$/g, '\\(q_\\infty = \\frac{1}{2}\\rho V_\\infty^2\\)');
    html = html.replace(/\\\((\\theta)\$/g, '\\($1\\)');
    html = html.replace(/\\\((\\delta)\$/g, '\\($1\\)');
    html = html.replace(/\\\(D_e\$/g, '\\(D_e\\)');
    html = html.replace(/\\\(m\$/g, '\\(m\\)');
    html = html.replace(/\$y = x\^2\$\$/g, '$y = x^2$');
    html = html.replace(/<p class="text-center font-mono text-blue-300">\$-k A_c/g, () => '<p class="text-center font-mono text-blue-300">$$\-k A_c');
    html = html.replace(/Where: \$v_w = \\text\{Workpiece velocity\}, d = \\text\{Depth of cut\}\$\$/g, 'Where: $v_w = \\text{Workpiece velocity}, d = \\text{Depth of cut}$');
    html = html.replace(/document\.getElementById\('l2-feedback\.innerText'\)/g, "document.getElementById('l2-feedback').innerText");

    // Replace accidental \.<br> with \)<br> (finite wings)
    html = html.replace(/\\\.<br>/g, '\\)<br>');
    html = html.replace(/\\\.\s*<br\s*\/?>/gi, '\\)<br>');
    html = html.replace(/\[M L\^\{-1\} T\^\{-2\}\]`<br>/g, '[M L^{-1} T^{-2}]\\)<br>');

    // Replace accidental \</td> with \)</td> (convection & fuselage tables)
    html = html.replace(/\\\s*<\/td>/g, '\\)</td>');

    // Replace missing <td>\( in lifting line
    html = html.replace(/<\/td>\\([0-9]+(?:\^[a-zA-Z0-9_\^\\]+)?)/g, '</td><td>\\($1');

    // Unclosed cycles in fatigue
    html = html.replace(/Cycles\s*\\\(\[-\]<\/li>/g, 'Cycles \\([-]\\)</li>');

    // Missing $ in apparent strain
    html = html.replace(/Expansion Coefficients \(\$\\alpha\$\): \$\[\\theta\^\{-1\}\]<br>/g, 'Expansion Coefficients ($\\alpha$): $[\\theta^{-1}]$<br>');

    // Unclosed \( in theory of shells
    html = html.replace(/or\s*\\\(\[([^\]]+)\]<\/p>/g, 'or \\([$1]\\)</p>');

    // 5. Dark theme override
    if (!html.includes('background-color: #060911 !important') && !html.includes('background-color:#060911!important')) {
      if (html.includes('</style>')) {
        html = html.replace('</style>', '    html, body { background-color: #060911 !important; color: #f8fafc !important; }\n    </style>');
      }
    }

    // 6. Responsive tables CSS
    if (!html.includes('table {') && !html.includes('display: block; overflow-x: auto') && html.includes('</style>')) {
      html = html.replace('</style>', '    table { max-width: 100%; display: block; overflow-x: auto; -webkit-overflow-scrolling: touch; }\n    </style>');
    }

    if (html !== originalHtml) {
      fs.writeFileSync(d.outputPath, html, 'utf8');
      modifiedCount++;
      console.log(`✓ Fixed: Day ${d.day} • ${d.topic}`);
    }
  }

  console.log(`\nSuccessfully audited and updated ${modifiedCount} / ${existingDays.length} pages.`);
}

run().catch(console.error);
