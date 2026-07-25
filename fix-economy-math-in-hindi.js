/**
 * fix-economy-math-in-hindi.js
 * 
 * Problem: AI put Hindi/Devanagari text inside LaTeX \text{} commands
 * in lang-hi sections. MathJax cannot render Devanagari in math mode.
 * 
 * Fix: Find any $$...$$ or $...$ blocks that CONTAIN Devanagari characters
 * and convert them to plain HTML (leaving English-only math for MathJax).
 */

const fs = require('fs');
const path = require('path');

// Convert LaTeX string to readable plain HTML
function latexToPlainHtml(latex, isDisplay) {
    let r = latex
        // \text{content} → content  (THE main fix for Hindi-in-math)
        .replace(/\\text\s*\{([^}]*)\}/g, '$1')
        .replace(/\\mathrm\s*\{([^}]*)\}/g, '$1')
        .replace(/\\mathbf\s*\{([^}]*)\}/g, '<strong>$1</strong>')
        .replace(/\\mathit\s*\{([^}]*)\}/g, '<em>$1</em>')
        // Fractions
        .replace(/\\frac\s*\{([^}]*)\}\s*\{([^}]*)\}/g, '($1) / ($2)')
        // Subscripts  _{x} and _x
        .replace(/_\{([^}]*)\}/g, '<sub>$1</sub>')
        .replace(/\^\{([^}]*)\}/g, '<sup>$1</sup>')
        .replace(/_([A-Za-z0-9])/g, '<sub>$1</sub>')
        .replace(/\^([A-Za-z0-9])/g, '<sup>$1</sup>')
        // Greek & math symbols
        .replace(/\\Delta/g, 'Δ').replace(/\\delta/g, 'δ')
        .replace(/\\Sigma/g, 'Σ').replace(/\\sigma/g, 'σ')
        .replace(/\\sum/g, 'Σ').replace(/\\prod/g, 'Π')
        .replace(/\\alpha/g, 'α').replace(/\\beta/g, 'β')
        .replace(/\\gamma/g, 'γ').replace(/\\pi/g, 'π')
        .replace(/\\theta/g, 'θ').replace(/\\lambda/g, 'λ')
        .replace(/\\mu/g, 'μ').replace(/\\omega/g, 'ω')
        .replace(/\\times/g, ' × ').replace(/\\cdot/g, ' · ')
        .replace(/\\div/g, ' ÷ ').replace(/\\pm/g, ' ± ')
        .replace(/\\neq/g, ' ≠ ').replace(/\\geq/g, ' ≥ ')
        .replace(/\\leq/g, ' ≤ ').replace(/\\approx/g, ' ≈ ')
        .replace(/\\infty/g, '∞')
        .replace(/\\rightarrow/g, ' → ').replace(/\\leftarrow/g, ' ← ')
        .replace(/\\Rightarrow/g, ' ⇒ ').replace(/\\to/g, ' → ')
        .replace(/\\ge/g, ' ≥ ').replace(/\\le/g, ' ≤ ')
        // Alignment & structure (remove)
        .replace(/\\\\/g, '  ').replace(/&/g, ' ')
        .replace(/\\begin\{[^}]*\}/g, '').replace(/\\end\{[^}]*\}/g, '')
        .replace(/\\left[\(\[\{|.]/g, '(').replace(/\\right[\)\]\}|.]/g, ')')
        .replace(/\\qquad/g, '  ').replace(/\\quad/g, ' ')
        // Remove any remaining LaTeX commands
        .replace(/\\[a-zA-Z]+\s*/g, '')
        // Remove bare curly braces
        .replace(/\{|\}/g, '')
        // Collapse whitespace
        .replace(/\s+/g, ' ').trim();

    if (isDisplay) {
        return `<div style="text-align:center;margin:0.75em 0;font-style:italic;color:var(--text-dark,#2c3e50);">${r}</div>`;
    }
    return `<span style="font-style:italic;">${r}</span>`;
}

// Process a single HTML file
function fixFile(filePath) {
    let html = fs.readFileSync(filePath, 'utf8');
    let changes = 0;

    // Fix display math $$...$$ that contains Devanagari
    html = html.replace(/\$\$([\s\S]*?)\$\$/g, (match, latex) => {
        if (/[\u0900-\u097F]/.test(latex)) {
            changes++;
            return latexToPlainHtml(latex, true);
        }
        return match; // English-only math → keep for MathJax
    });

    // Fix inline math $...$ that contains Devanagari
    html = html.replace(/\$([^$\n]{1,300}?)\$/g, (match, latex) => {
        if (/[\u0900-\u097F]/.test(latex)) {
            changes++;
            return latexToPlainHtml(latex, false);
        }
        return match;
    });

    if (changes > 0) {
        fs.writeFileSync(filePath, html, 'utf8');
    }
    return changes;
}

const economyDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness/economy';

const dirs = fs.readdirSync(economyDir).filter(d =>
    fs.statSync(path.join(economyDir, d)).isDirectory()
);

let totalFixed = 0;
for (const dir of dirs) {
    const file = path.join(economyDir, dir, 'index.html');
    if (!fs.existsSync(file)) continue;
    const n = fixFile(file);
    console.log(`${n > 0 ? '✅' : '⏭️ '} ${dir} — ${n} math block(s) converted`);
    totalFixed += n;
}

console.log(`\n🎉 Done! Converted ${totalFixed} Devanagari-in-math blocks across all pages.`);
