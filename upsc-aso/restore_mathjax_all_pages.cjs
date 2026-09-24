const fs = require('fs');

const MATHJAX_COMPLETE_BLOCK = `<!-- MathJax 3 Configuration -->
    <script>
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
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>`;

async function fixMathJax() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  console.log(`Restoring MathJax across ${existingDays.length} pages...\n`);

  let fixedCount = 0;

  for (const d of existingDays) {
    let html = fs.readFileSync(d.outputPath, 'utf8');
    const original = html;

    // Pattern where MathJax was cut off right before <style>
    const cutoffPattern = /<script(?:\s+id="MathJax-script")?>\s*window\.MathJax\s*=\s*\{[\s\S]*?inlineMath:\s*\[\['\s*(?=\s*<style>)/i;
    
    if (cutoffPattern.test(html)) {
      html = html.replace(cutoffPattern, () => MATHJAX_COMPLETE_BLOCK + '\n\n    ');
    } else if (!html.includes('cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')) {
      // If it doesn't have the script at all, insert right before <style>
      if (html.includes('<style>')) {
        html = html.replace('<style>', () => MATHJAX_COMPLETE_BLOCK + '\n\n    <style>');
      }
    }

    if (html !== original) {
      fs.writeFileSync(d.outputPath, html, 'utf8');
      fixedCount++;
      console.log(`✓ Restored MathJax in Day ${d.day}: ${d.topic}`);
    }
  }

  console.log(`\nSuccessfully restored MathJax in ${fixedCount} pages.`);
}

fixMathJax().catch(console.error);
