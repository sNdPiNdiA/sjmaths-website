import { hydrateChemistryRuntime, externalizeChemistryRuntime } from './chemistry-runtime.mjs';
const letters = ['A', 'B', 'C', 'D'];

export function cleanMathHtml(str) {
  if (!str) return '';
  return str
    .replace(/\\text\{([^{}]+)\}/g, '$1')
    // Greek symbols - negative lookahead ensures no clash with longer words
    .replace(/\\chi(?![a-zA-Z])/g, '&chi;')
    .replace(/\\Delta(?![a-zA-Z])/g, '&Delta;')
    .replace(/\\lambda(?![a-zA-Z])/g, '&lambda;')
    .replace(/\\nu(?![a-zA-Z])/g, '&nu;')
    .replace(/\\mu(?![a-zA-Z])/g, '&mu;')
    .replace(/\\pi(?![a-zA-Z])/g, '&pi;')
    .replace(/\\alpha(?![a-zA-Z])/g, '&alpha;')
    .replace(/\\beta(?![a-zA-Z])/g, '&beta;')
    .replace(/\\gamma(?![a-zA-Z])/g, '&gamma;')
    .replace(/\\theta(?![a-zA-Z])/g, '&theta;')
    .replace(/\\sigma(?![a-zA-Z])/g, '&sigma;')
    .replace(/\\epsilon(?![a-zA-Z])/g, '&epsilon;')
    .replace(/\\omega(?![a-zA-Z])/g, '&omega;')
    .replace(/\\phi(?![a-zA-Z])/g, '&phi;')
    .replace(/\\psi(?![a-zA-Z])/g, '&psi;')
    .replace(/\\rho(?![a-zA-Z])/g, '&rho;')
    .replace(/\\tau(?![a-zA-Z])/g, '&tau;')
    .replace(/\\eta(?![a-zA-Z])/g, '&eta;')
    .replace(/\\kappa(?![a-zA-Z])/g, '&kappa;')
    // Math operators & symbols
    .replace(/\\hbar(?![a-zA-Z])/g, '&#x210f;')
    .replace(/\\times(?![a-zA-Z])/g, '&times;')
    .replace(/\\cdot(?![a-zA-Z])/g, '&middot;')
    .replace(/\\pm(?![a-zA-Z])/g, '&plusmn;')
    .replace(/\\approx(?![a-zA-Z])/g, '&asymp;')
    .replace(/\\propto(?![a-zA-Z])/g, '&prop;')
    .replace(/\\infty(?![a-zA-Z])/g, '&infin;')
    .replace(/\\(?:ge|geq)(?![a-zA-Z])/g, '&ge;')
    .replace(/\\(?:le|leq)(?![a-zA-Z])/g, '&le;')
    .replace(/\\(?:ne|neq)(?![a-zA-Z])/g, '&ne;')
    .replace(/\\partial(?![a-zA-Z])/g, '&part;')
    .replace(/\\sum(?![a-zA-Z])/g, '&sum;')
    .replace(/\\int(?![a-zA-Z])/g, '&int;')
    .replace(/\\(?:to|rightarrow)(?![a-zA-Z])/g, '&rarr;')
    .replace(/\\rightleftharpoons(?![a-zA-Z])/g, '&#8652;')
    .replace(/\\AA(?![a-zA-Z])/g, '&#197;')
    // LaTeX brackets
    .replace(/\\left\(/g, '(')
    .replace(/\\right\)/g, ')')
    .replace(/\\left\[/g, '[')
    .replace(/\\right\]/g, ']')
    // Fractions: standard fractions
    .replace(/(?:&frac|\\frac)\{1\}\{2\}\s*([a-zA-Z])/g, '&frac12; $1')
    .replace(/(?:&frac|\\frac)\{1\}\{2\}/g, '&frac12;')
    .replace(/(?:&frac|\\frac)\{1\}\{4\}/g, '&frac14;')
    .replace(/(?:&frac|\\frac)\{3\}\{4\}/g, '&frac34;')
    .replace(/<span class="math-frac">\s*<span class="math-num">1<\/span>\s*<span class="math-denom">2<\/span>\s*<\/span>\s*([a-zA-Z])/g, '&frac12; $1')
    .replace(/(?:&frac|\\frac)\{([^{}]+)\}\{([^{}]+)\}/g, '<span class="math-frac"><span class="math-num">$1</span><span class="math-denom">$2</span></span>')
    // Square roots
    .replace(/\\sqrt\{([^{}]+)\}/g, '<span class="math-sqrt">&radic;<span class="math-radicand">$1</span></span>')
    // Subscripts & Superscripts (attached to a symbol/char/bracket)
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])_\{([^{}]+)\}/g, '$1<sub>$2</sub>')
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])_([a-zA-Z0-9]+)/g, '$1<sub>$2</sub>')
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])\^\{([^{}]+)\}/g, '$1<sup>$2</sup>')
    .replace(/([a-zA-Z0-9\)\]\}\&;\>])\^([0-9\+\-]+)/g, '$1<sup>$2</sup>');
}

function replaceBalancedContainer(html, startPattern, newContent) {
  let startIndex = -1;
  if (typeof startPattern === 'string') {
    startIndex = html.indexOf(startPattern);
  } else if (startPattern instanceof RegExp) {
    const m = html.match(startPattern);
    if (m) startIndex = m.index;
  }
  if (startIndex === -1) return html;

  const divRegex = /<\/?div\b[^>]*>/gi;
  divRegex.lastIndex = startIndex;

  let depth = 0;
  let match;
  while ((match = divRegex.exec(html)) !== null) {
    if (match[0].startsWith('</')) {
      depth--;
      if (depth === 0) {
        const endIndex = match.index + match[0].length;
        return html.substring(0, startIndex) + newContent + html.substring(endIndex);
      }
    } else {
      depth++;
    }
  }
  return html;
}

// Build complete bilingual HTML with strict container-based replacements
export function buildCompleteBilingualHtml(originalHtml, enData, hiData, quizData, pyqData, testData) {
  let html = hydrateChemistryRuntime(originalHtml);

  // 1. Language Toggle Button
  if (!html.includes('id="btn-lang-toggle"')) {
    html = html.replace(
      /(<div class="header-actions">)/,
      `$1\n      <button type="button" class="lang-toggle-btn" id="btn-lang-toggle" aria-label="Switch Language / भाषा बदलें">🌐 <span style="font-weight:900;">EN</span> (हिन्दी)</button>`
    );
  }

  // 1b. Inject CSS visibility rules
  if (!html.includes('html[data-lang="en"]')) {
    html = html.replace(
      '</style>',
      'html[data-lang="en"] .lang-hi { display: none !important; }\nhtml[data-lang="hi"] .lang-en { display: none !important; }\nhtml:not([data-lang="hi"]) .lang-hi { display: none !important; }\n</style>'
    );
  }

  // 1c. Inject inline JS logic for language toggle
  if (!html.includes('setLanguage(')) {
    const langScriptSnippet = `
  // Bilingual (English / Hindi) Language Toggle Logic
  const langToggleBtn = document.getElementById('btn-lang-toggle');
  function setLanguage(lang, save) {
    if (lang !== 'hi' && lang !== 'en') lang = 'en';
    document.documentElement.setAttribute('data-lang', lang);
    if (save !== false) {
      localStorage.setItem('sjmaths_preferred_language', lang);
    }
    if (langToggleBtn) {
      langToggleBtn.innerHTML = lang === 'hi' ? '🌐 <span style="font-weight:900;">हिन्दी</span> (EN)' : '🌐 <span style="font-weight:900;">EN</span> (हिन्दी)';
    }
  }
  const savedLang = localStorage.getItem('sjmaths_preferred_language') || 'en';
  setLanguage(savedLang, false);

  if (langToggleBtn) {
    langToggleBtn.addEventListener('click', () => {
      const currentLang = document.documentElement.getAttribute('data-lang') || 'en';
      const nextLang = currentLang === 'en' ? 'hi' : 'en';
      setLanguage(nextLang, true);
    });
  }
`;
    html = html.replace(
      "document.addEventListener('DOMContentLoaded', () => {",
      "document.addEventListener('DOMContentLoaded', () => {" + langScriptSnippet
    );
  }

  // 2. Hero Kicker, Title, Lead
  if (hiData.kicker_hi) {
    html = html.replace(
      /<div class="kicker"[^>]*>[\s\S]*?<\/div>/,
      `<div class="kicker" style="color: #2563eb; font-weight: 800;">
        <span class="lang-en">${enData.kicker}</span>
        <span class="lang-hi">${hiData.kicker_hi}</span>
      </div>`
    );
  }

  if (hiData.title_hi) {
    html = html.replace(
      /<h1>[\s\S]*?<\/h1>/,
      `<h1>
        <span class="lang-en">${enData.title}</span>
        <span class="lang-hi">${hiData.title_hi}</span>
      </h1>`
    );
  }

  if (hiData.lead_hi) {
    html = html.replace(
      /<p class="lead">[\s\S]*?<\/p>/,
      `<p class="lead">
        <span class="lang-en">${enData.lead}</span>
        <span class="lang-hi">${hiData.lead_hi}</span>
      </p>`
    );
  }

  // 3. Tab Buttons labels
  html = html.replace(
    /<span>📖<\/span>\s*(?:<[^>]+>)*\s*<span>Study Notes<\/span>/,
    `<span>📖</span> <span class="lang-en">Study Notes</span><span class="lang-hi">अध्ययन नोट्स</span>`
  );
  html = html.replace(
    /<span>⚡<\/span>\s*(?:<[^>]+>)*\s*<span>Revision Summary<\/span>/,
    `<span>⚡</span> <span class="lang-en">Revision Summary</span><span class="lang-hi">रिवीज़न सारांश</span>`
  );
  html = html.replace(
    /<span>❓<\/span>\s*(?:<[^>]+>)*\s*<span>Practice Quiz<\/span>/,
    `<span>❓</span> <span class="lang-en">Practice Quiz</span><span class="lang-hi">अभ्यास क्विज़</span>`
  );
  html = html.replace(
    /<span>🏛️<\/span>\s*(?:<[^>]+>)*\s*<span>PYQs & Trends<\/span>/,
    `<span>🏛️</span> <span class="lang-en">PYQs & Trends</span><span class="lang-hi">विगत वर्ष प्रश्न</span>`
  );
  html = html.replace(
    /<span>⏱️<\/span>\s*(?:<[^>]+>)*\s*<span>Topic Test<\/span>/,
    `<span>⏱️</span> <span class="lang-en">Topic Test</span><span class="lang-hi">टॉपिक टेस्ट</span>`
  );

  // 4. Tab 1: Sections
  if (Array.isArray(hiData.sections_hi)) {
    enData.sections.forEach((sec, idx) => {
      const hiSec = hiData.sections_hi[idx];
      if (!hiSec) return;

      const enBulletsHtml = sec.bullets.map(b => `<li>${b}</li>`).join('');
      const hiBulletsHtml = (hiSec.bullets_hi || []).map(b => `<li>${b}</li>`).join('');

      const oldSecRegex = new RegExp(
        `<section class="notes-section" id="note-sec-${idx + 1}">[\\s\\S]*?<h2>[\\s\\S]*?<\\/h2>[\\s\\S]*?<div class="prose-content">[\\s\\S]*?<\\/div>\\s*<\\/section>`
      );

      const bilingualSec = `
      <section class="notes-section" id="note-sec-${idx + 1}">
        <h2>
          <span class="lang-en">${sec.heading}</span>
          <span class="lang-hi">${hiSec.heading_hi || sec.heading}</span>
        </h2>
        <div class="prose-content">
          <div class="lang-en">
            <ul class="notes-bullet-list">${enBulletsHtml}</ul>
          </div>
          <div class="lang-hi">
            <ul class="notes-bullet-list">${hiBulletsHtml}</ul>
          </div>
        </div>
      </section>`;

      html = html.replace(oldSecRegex, bilingualSec.trim());
    });
  }

  // 5. Formula Sheet (Clean block replacement)
  if (Array.isArray(enData.formulas) && enData.formulas.length > 0) {
    const cardsHtml = enData.formulas.map((f, idx) => {
      const hiF = (hiData.formula_meta_hi && hiData.formula_meta_hi[idx]) || {};
      const condEn = cleanMathHtml(f.conditions || '');
      const unitEn = cleanMathHtml(f.units || '');
      const condHi = cleanMathHtml(hiF.conditions_hi || condEn);
      const unitHi = cleanMathHtml(hiF.units_hi || unitEn);
      const eqHtml = cleanMathHtml(f.eq || '');

      return `
            <div class="formula-card">
              <div class="formula-name">
                <span class="lang-en">${f.name}</span>
                <span class="lang-hi">${hiF.name_hi || f.name}</span>
              </div>
              <div class="formula-eq">${eqHtml}</div>
              <div class="formula-meta">
                <div class="lang-en">
                  ${condEn ? `<div><strong>Conditions:</strong> ${condEn}</div>` : ''}
                  ${unitEn ? `<div><strong>Units:</strong> ${unitEn}</div>` : ''}
                </div>
                <div class="lang-hi">
                  ${condHi ? `<div><strong>शर्तें:</strong> ${condHi}</div>` : ''}
                  ${unitHi ? `<div><strong>इकाइयाँ:</strong> ${unitHi}</div>` : ''}
                </div>
              </div>
            </div>`;
    }).join('');

    const bilingualFormulaBox = `
        <div class="formula-sheet-box">
          <div class="formula-sheet-title">
            <span class="lang-en">📐 Key Formulas & Equations</span>
            <span class="lang-hi">📐 महत्वपूर्ण सूत्र एवं समीकरण</span>
          </div>
          <div class="formula-grid">
${cardsHtml}
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="formula-sheet-box">', bilingualFormulaBox.trim());
  }

  // 6. Exceptions (Clean block replacement)
  if (Array.isArray(enData.exceptions) && enData.exceptions.length > 0) {
    const excListHtml = enData.exceptions.map((exc, idx) => {
      const hiExc = (hiData.exceptions_hi && hiData.exceptions_hi[idx]) || {};
      return `
            <div class="exception-card">
              <div class="exception-head">
                <span class="exception-badge"><span class="lang-en">Exception</span><span class="lang-hi">अपवाद</span></span>
                <span class="exception-rule"><span class="lang-en">${exc.rule}</span><span class="lang-hi">${hiExc.rule_hi || exc.rule}</span></span>
              </div>
              <p class="exception-detail">
                <span class="lang-en"><strong>Observation:</strong> ${exc.observation}</span>
                <span class="lang-hi"><strong>प्रेक्षण:</strong> ${hiExc.observation_hi || exc.observation}</span>
              </p>
            </div>`;
    }).join('');

    const bilingualExceptions = `
        <div class="exception-alert-box">
          <div class="exception-alert-title">
            <span class="lang-en">⚠️ Important Exceptions & Anomalies</span>
            <span class="lang-hi">⚠️ महत्वपूर्ण अपवाद एवं विसंगतियाँ</span>
          </div>
          <div class="exception-list">
${excListHtml}
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="exception-alert-box">', bilingualExceptions.trim());
  }

  // 7. Shortcuts / Tricks (Clean block replacement)
  if (Array.isArray(enData.tricks) && enData.tricks.length > 0) {
    const trickListHtml = enData.tricks.map((trk, idx) => {
      const hiTrk = (hiData.tricks_hi && hiData.tricks_hi[idx]) || {};
      return `
            <div class="trick-card">
              <div class="trick-title"><span class="lang-en">${trk.title}</span><span class="lang-hi">${hiTrk.title_hi || trk.title}</span></div>
              <div class="trick-shortcut">${trk.shortcut}</div>
              <p class="trick-app">
                <span class="lang-en"><strong>Application:</strong> ${trk.application}</span>
                <span class="lang-hi"><strong>अनुप्रयोग:</strong> ${hiTrk.application_hi || trk.application}</span>
              </p>
            </div>`;
    }).join('');

    const bilingualTricks = `
        <div class="trick-box">
          <div class="trick-box-title">
            <span class="lang-en">💡 Shortcuts & Memory Aids</span>
            <span class="lang-hi">💡 शॉर्टकट एवं स्मरणीय सूत्र</span>
          </div>
          <div class="tricks-grid">
${trickListHtml}
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="trick-box">', bilingualTricks.trim());
  }

  // 8. Comparison Matrix (Clean block replacement)
  if (enData.comparison && hiData.comparison_hi) {
    const comp = enData.comparison;
    const hiComp = hiData.comparison_hi;

    const ths = comp.headers.map((h, i) => {
      const hHi = (hiComp.headers_hi && hiComp.headers_hi[i]) || h;
      return `<th><span class="lang-en">${h}</span><span class="lang-hi">${hHi}</span></th>`;
    }).join('');

    const trs = comp.rows.map((row, rIdx) => {
      const hiRow = (hiComp.rows_hi && hiComp.rows_hi[rIdx]) || [];
      const tds = row.map((cell, cIdx) => {
        const cHi = hiRow[cIdx] || cell;
        return `<td><span class="lang-en">${cell}</span><span class="lang-hi">${cHi}</span></td>`;
      }).join('');
      return `<tr>${tds}</tr>`;
    }).join('');

    const bilingualComparison = `
        <div class="comparison-card">
          <div class="comparison-title">
            <span class="lang-en">⚖️ ${comp.title.replace(/^⚖️\s*/, '')}</span>
            <span class="lang-hi">⚖️ ${(hiComp.title_hi || comp.title).replace(/^⚖️\s*/, '')}</span>
          </div>
          <div class="table-responsive">
            <table class="styled-table">
              <thead><tr>${ths}</tr></thead>
              <tbody>${trs}</tbody>
            </table>
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="comparison-card">', bilingualComparison.trim());
  }

  // 9. Exam Points Card (Clean block replacement)
  if (Array.isArray(enData.exam_points) && enData.exam_points.length > 0) {
    const enPoints = enData.exam_points.map(p => `<li>${p}</li>`).join('');
    const hiPoints = (hiData.exam_points_hi || enData.exam_points).map(p => `<li>${p}</li>`).join('');

    const bilingualExamPoints = `
        <div class="exam-points-card">
          <div class="exam-points-title">
            <span class="lang-en">🎯 Key Exam Points</span>
            <span class="lang-hi">🎯 महत्वपूर्ण परीक्षा बिंदु (Key Exam Points)</span>
          </div>
          <div class="lang-en">
            <ul class="exam-points-list">${enPoints}</ul>
          </div>
          <div class="lang-hi">
            <ul class="exam-points-list">${hiPoints}</ul>
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="exam-points-card">', bilingualExamPoints.trim());
  }

  // 10. Common Errors Card (Clean block replacement)
  if (Array.isArray(enData.common_errors) && enData.common_errors.length > 0) {
    const enErrors = enData.common_errors.map(e => `<li>${e}</li>`).join('');
    const hiErrors = (hiData.common_errors_hi || enData.common_errors).map(e => `<li>${e}</li>`).join('');

    const bilingualCommonErrors = `
        <div class="common-errors-card">
          <div class="common-errors-title">
            <span class="lang-en">🚫 Common Errors & Confusions</span>
            <span class="lang-hi">🚫 सामान्य भ्रांतियाँ एवं त्रुटियाँ (Common Errors)</span>
          </div>
          <div class="lang-en">
            <ul class="common-errors-list">${enErrors}</ul>
          </div>
          <div class="lang-hi">
            <ul class="common-errors-list">${hiErrors}</ul>
          </div>
        </div>`;

    html = replaceBalancedContainer(html, '<div class="common-errors-card">', bilingualCommonErrors.trim());
  }

  // 11. Tab 2: Revision Summary
  // Build bilingual summary concepts
  let conceptsHtml = '';
  if (Array.isArray(enData.summary_concepts)) {
    conceptsHtml = enData.summary_concepts.map((c, idx) => {
      const hiC = (hiData.summary_concepts_hi && hiData.summary_concepts_hi[idx]) || {};
      return `
          <div class="summary-concept-card">
            <div class="summary-concept-header">
              <h3 class="summary-concept-title">
                <span class="lang-en">${c.title}</span>
                <span class="lang-hi">${hiC.title_hi || c.title}</span>
              </h3>
            </div>
            <div class="summary-concept-body prose-content">
              <div class="lang-en"><p>${c.body.replace(/<\/?p>/g, '')}</p></div>
              <div class="lang-hi"><p>${hiC.body_hi || c.body}</p></div>
            </div>
          </div>`;
    }).join('\n');
  }

  // Build bilingual glossary
  let glossaryHtml = '';
  if (Array.isArray(enData.glossary)) {
    glossaryHtml = enData.glossary.map((g, idx) => {
      const hiG = (hiData.glossary_hi && hiData.glossary_hi[idx]) || {};
      return `
          <div class="glossary-item">
            <div class="glossary-term-wrap">
              <span class="glossary-term">
                <span class="lang-en">${g.term}</span>
                <span class="lang-hi">${hiG.term_hi || g.term}</span>
              </span>
            </div>
            <div class="glossary-def">
              <span class="lang-en">${g.definition}</span>
              <span class="lang-hi">${hiG.definition_hi || g.definition}</span>
            </div>
          </div>`;
    }).join('\n');
  }

  // Build takeaways
  const enTakeaways = (enData.key_takeaways || []).map(x => `<li>${x}</li>`).join('');
  const hiTakeaways = (hiData.key_takeaways_hi || enData.key_takeaways || []).map(x => `<li>${x}</li>`).join('');

  // Build recall
  const enRecall = (enData.quick_recall || []).map(x => `<li>${x}</li>`).join('');
  const hiRecall = (hiData.quick_recall_hi || enData.quick_recall || []).map(x => `<li>${x}</li>`).join('');

  // Build differences
  let differencesHtml = '';
  if (Array.isArray(enData.key_differences)) {
    differencesHtml = enData.key_differences.map((cf, idx) => {
      const hiCf = (hiData.key_differences_hi && hiData.key_differences_hi[idx]) || {};
      return `
          <div class="confusion-item">
            <div class="confusion-terms">
              <span class="conf-badge-a"><span class="lang-en">${cf.term_a}</span><span class="lang-hi">${hiCf.term_a_hi || cf.term_a}</span></span>
              <span class="conf-vs">VS</span>
              <span class="conf-badge-b"><span class="lang-en">${cf.term_b}</span><span class="lang-hi">${hiCf.term_b_hi || cf.term_b}</span></span>
            </div>
            <p class="confusion-diff">
              <span class="lang-en">${cf.difference}</span>
              <span class="lang-hi">${hiCf.difference_hi || cf.difference}</span>
            </p>
          </div>`;
    }).join('\n');
  }

  const bilingualTab2 = `
      <!-- TAB 2: REVISION SUMMARY & GLOSSARY -->
      <article class="tab-panel hidden" id="tab-summary" role="tabpanel" aria-labelledby="tab-btn-summary">
        <div class="summary-container">
          <div class="summary-hero-box" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);">
            <h2>
              <span class="lang-en">⚡ Quick Revision: ${enData.title}</span>
              <span class="lang-hi">⚡ त्वरित रिवीज़न: ${hiData.title_hi || enData.title}</span>
            </h2>
            <p>
              <span class="lang-en">Core formulas, rapid recall points, and distinguishing criteria at a glance.</span>
              <span class="lang-hi">मुख्य सूत्र, त्वरित स्मरण बिंदु एवं तुलनात्मक मानदंड एक नज़र में।</span>
            </p>
          </div>

${conceptsHtml}

          <h2>
            <span class="lang-en">📚 Terms & Units Glossary</span>
            <span class="lang-hi">📚 पारिभाषिक शब्दावली एवं इकाइयाँ</span>
          </h2>

${glossaryHtml}

          <h2>
            <span class="lang-en">🎯 Key Takeaways</span>
            <span class="lang-hi">🎯 महत्वपूर्ण निष्कर्ष (Key Takeaways)</span>
          </h2>
          <div class="lang-en">
            <ul class="summary-list">${enTakeaways}</ul>
          </div>
          <div class="lang-hi">
            <ul class="summary-list">${hiTakeaways}</ul>
          </div>

          <h2>
            <span class="lang-en">📌 Quick Recall</span>
            <span class="lang-hi">📌 त्वरित स्मरण (Quick Recall)</span>
          </h2>
          <div class="lang-en">
            <ul class="summary-list">${enRecall}</ul>
          </div>
          <div class="lang-hi">
            <ul class="summary-list">${hiRecall}</ul>
          </div>

          <h2>
            <span class="lang-en">⚖️ Key Differences</span>
            <span class="lang-hi">⚖️ महत्वपूर्ण अंतर (Key Differences)</span>
          </h2>
${differencesHtml}
        </div>
      </article>`;

  const sumStart = html.indexOf('<article class="tab-panel hidden" id="tab-summary"');
  const sumEnd = html.indexOf('</article>', sumStart);
  if (sumStart !== -1 && sumEnd !== -1) {
    html = html.substring(0, sumStart) + bilingualTab2.trim() + html.substring(sumEnd + '</article>'.length);
  }

  // 12. Tab 3: Practice Quiz Header & Cards Container
  html = html.replace(
    /<h2>❓ Practice Questions \((\d+) MCQs\)<\/h2>/,
    `<h2><span class="lang-en">❓ Practice Questions ($1 MCQs)</span><span class="lang-hi">❓ अभ्यास प्रश्न ($1 बहुविकल्पीय प्रश्न)</span></h2>`
  );
  html = html.replace(
    /<p>Select an option to test your understanding with instant verification and explanations\.<\/p>/,
    `<p><span class="lang-en">Select an option to test your understanding with instant verification and explanations.</span><span class="lang-hi">अपनी समझ का परीक्षण करने के लिए विकल्प चुनें। तत्काल समाधान एवं व्याख्या उपलब्ध।</span></p>`
  );
  html = html.replace(
    /<div class="score-pill">Score: <span id="quizScore">0<\/span> \/ (\d+)<\/div>/,
    `<div class="score-pill"><span class="lang-en">Score:</span><span class="lang-hi">स्कोर:</span> <span id="quizScore">0</span> / $1</div>`
  );
  html = html.replace(
    /<button type="button" class="btn-reset-quiz" id="btnResetQuiz">Restart Quiz<\/button>/,
    `<button type="button" class="btn-reset-quiz" id="btnResetQuiz"><span class="lang-en">Restart Quiz</span><span class="lang-hi">क्विज़ पुनः आरंभ करें</span></button>`
  );

  const qListStart = html.indexOf('<div class="quiz-questions-list">');
  const qArtEnd = html.indexOf('</article>', qListStart);
  if (qListStart !== -1 && qArtEnd !== -1 && Array.isArray(quizData)) {
    let quizCardsHtml = '\n';
    quizData.forEach((q, idx) => {
      const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
      const opts = optsList.map((opt, oIdx) => {
        const optHi = (q.options_hi && q.options_hi[oIdx]) || opt;
        return `
      <button type="button" class="quiz-option-btn" data-qindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">
          <span class="lang-en">${opt}</span>
          <span class="lang-hi">${optHi}</span>
        </span>
      </button>`;
      }).join('');

      const qHi = q.question_hi || q.question;
      const expHi = q.explanation_hi || q.explanation || '';

      quizCardsHtml += `
      <div class="quiz-question-card" id="q-card-${idx}" data-correct="${q.correct_index ?? 0}">
        <div class="q-header">
          <span class="q-number">
            <span class="lang-en">Question ${idx + 1} of ${quizData.length}</span>
            <span class="lang-hi">प्रश्न ${idx + 1} / ${quizData.length}</span>
          </span>
        </div>
        <h3 class="q-text">
          <span class="lang-en">${q.question || 'Practice Question'}</span>
          <span class="lang-hi">${qHi}</span>
        </h3>
        <div class="quiz-options-group">${opts}
    </div>
        <div class="q-feedback hidden" id="feedback-${idx}">
          <div class="feedback-indicator"></div>
          <p class="feedback-explanation">
            <strong><span class="lang-en">Explanation:</span><span class="lang-hi">व्याख्या:</span></strong>
            <span class="lang-en">${q.explanation || 'See solution above.'}</span>
            <span class="lang-hi">${expHi}</span>
          </p>
        </div>
      </div>
    `;
    });
    quizCardsHtml += '\n        </div>\n      ';

    html = html.substring(0, qListStart + '<div class="quiz-questions-list">'.length) +
           quizCardsHtml +
           html.substring(qArtEnd);
  }

  // 13. Tab 4: PYQs & Trends Header & Cards Container
  html = html.replace(
    /<h2>🏛️ Exam Trends & Question Pattern<\/h2>/,
    `<h2><span class="lang-en">🏛️ Exam Trends & Question Pattern</span><span class="lang-hi">🏛️ परीक्षा ट्रेंड एवं प्रश्न पैटर्न</span></h2>`
  );
  html = html.replace(
    /<p>Historical question weightage and patterns for <strong>([\s\S]*?)<\/strong> in UP PGT Chemistry\.<\/p>/,
    `<p><span class="lang-en">Historical question weightage and patterns for <strong>${enData.title}</strong> in UP PGT Chemistry.</span><span class="lang-hi">UP PGT रसायन विज्ञान में <strong>${hiData.title_hi || enData.title}</strong> हेतु विगत वर्षों के प्रश्न भार एवं पैटर्न।</span></p>`
  );
  html = html.replace(
    /<span class="pyq-stat-label">Expected Questions<\/span>/,
    `<span class="pyq-stat-label"><span class="lang-en">Expected Questions</span><span class="lang-hi">अपेक्षित प्रश्न</span></span>`
  );
  html = html.replace(
    /<span class="pyq-stat-label">Topic Weightage<\/span>/,
    `<span class="pyq-stat-label"><span class="lang-en">Topic Weightage</span><span class="lang-hi">टॉपिक भार (Weightage)</span></span>`
  );
  html = html.replace(
    /<span class="pyq-stat-label">Difficulty<\/span>/,
    `<span class="pyq-stat-label"><span class="lang-en">Difficulty</span><span class="lang-hi">कठिनाई स्तर</span></span>`
  );

  const pListStart = html.indexOf('<div class="pyq-questions-list">');
  const pArtEnd = html.indexOf('</article>', pListStart);
  if (pListStart !== -1 && pArtEnd !== -1 && Array.isArray(pyqData)) {
    let pyqCardsHtml = '\n';
    pyqData.forEach((q, idx) => {
      const optsList = Array.isArray(q.options) && q.options.length === 4 ? q.options : ['Option A', 'Option B', 'Option C', 'Option D'];
      const opts = optsList.map((opt, oIdx) => {
        const optHi = (q.options_hi && q.options_hi[oIdx]) || opt;
        return `
      <button type="button" class="quiz-option-btn" data-pyqindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">
          <span class="lang-en">${opt}</span>
          <span class="lang-hi">${optHi}</span>
        </span>
      </button>`;
      }).join('');

      const correctIdx = (typeof q.correct_index === 'number' && q.correct_index >= 0 && q.correct_index < 4) ? q.correct_index : 0;
      const correctOptTextEn = optsList[correctIdx] || '';
      const correctOptTextHi = (q.options_hi && q.options_hi[correctIdx]) || correctOptTextEn;
      const qHi = q.question_hi || q.question;
      const expHi = q.explanation_hi || q.explanation || '';

      pyqCardsHtml += `
      <div class="pyq-card" id="pyq-card-${idx}" data-correct="${correctIdx}">
        <div class="pyq-header-meta">
          <span class="pyq-badge">${q.year_tag || 'UP PGT'}</span>
        </div>
        <div class="pyq-question-text">
          <span class="lang-en">${q.question || 'PYQ Question'}</span>
          <span class="lang-hi">${qHi}</span>
        </div>
        <div class="quiz-options-group">${opts}
    </div>
        <div class="pyq-expl-box hidden" id="pyq-expl-${idx}">
          <strong>
            <span class="lang-en">Answer: Option ${letters[correctIdx]} (${correctOptTextEn})</span>
            <span class="lang-hi">उत्तर: विकल्प ${letters[correctIdx]} (${correctOptTextHi})</span>
          </strong>
          <span class="lang-en">${q.explanation || ''}</span>
          <span class="lang-hi">${expHi}</span>
        </div>
      </div>
    `;
    });
    pyqCardsHtml += '\n        </div>\n      ';

    html = html.substring(0, pListStart + '<div class="pyq-questions-list">'.length) +
           pyqCardsHtml +
           html.substring(pArtEnd);
  }

  // 14. Tab 5: Timed Topic Test
  html = html.replace(
    /<h2>⏱️ Timed Topic Test<\/h2>/,
    `<h2><span class="lang-en">⏱️ Timed Topic Test</span><span class="lang-hi">⏱️ समयबद्ध टॉपिक टेस्ट</span></h2>`
  );
  html = html.replace(
    /<p>(\d+) questions &bull; (\d+) minutes &bull; Timed practice<\/p>/,
    `<p><span class="lang-en">$1 questions &bull; $2 minutes &bull; Timed practice</span><span class="lang-hi">$1 प्रश्न &bull; $2 मिनट &bull; समयबद्ध अभ्यास</span></p>`
  );
  html = html.replace(
    /<div class="test-instruction-box" id="testStartWrap">[\s\S]*?<h3>Instructions<\/h3>[\s\S]*?<ul>[\s\S]*?<\/ul>[\s\S]*?<button type="button" class="btn-start-test"[^>]*>Start Test<\/button>[\s\S]*?<\/div>/,
    `<div class="test-instruction-box" id="testStartWrap">
      <h3><span class="lang-en">Instructions</span><span class="lang-hi">निर्देश</span></h3>
      <ul>
        <li><strong><span class="lang-en">Questions:</span><span class="lang-hi">प्रश्न:</span></strong> <span class="lang-en">10 MCQs</span><span class="lang-hi">10 बहुविकल्पीय प्रश्न</span></li>
        <li><strong><span class="lang-en">Time Allowed:</span><span class="lang-hi">समय सीमा:</span></strong> <span class="lang-en">10 Minutes</span><span class="lang-hi">10 मिनट</span></li>
        <li><strong><span class="lang-en">Marking:</span><span class="lang-hi">अंकन:</span></strong> <span class="lang-en">+1 mark for correct, 0 for unattempted or wrong</span><span class="lang-hi">सही उत्तर हेतु +1 अंक, गलत या अनुत्तरित हेतु 0</span></li>
      </ul>
      <button type="button" class="btn-start-test" id="btnStartTest" style="background: linear-gradient(135deg, #1e3a8a, #2563eb);">
        <span class="lang-en">Start Test</span>
        <span class="lang-hi">टेस्ट प्रारंभ करें</span>
      </button>
    </div>`
  );

  const tListStart = html.indexOf('<div class="test-questions-list">');
  const tSubmitBar = html.indexOf('<div class="test-submit-bar">', tListStart);
  if (tListStart !== -1 && tSubmitBar !== -1 && Array.isArray(testData)) {
    let testCardsHtml = '\n';
    testData.forEach((t, idx) => {
      const optsList = Array.isArray(t.options) && t.options.length === 4 ? t.options : ['Option A', 'Option B', 'Option C', 'Option D'];
      const opts = optsList.map((opt, oIdx) => {
        const optHi = (t.options_hi && t.options_hi[oIdx]) || opt;
        return `
      <button type="button" class="test-option-btn" data-tindex="${idx}" data-optindex="${oIdx}">
        <span class="option-letter">${letters[oIdx]}</span>
        <span class="option-text">
          <span class="lang-en">${opt}</span>
          <span class="lang-hi">${optHi}</span>
        </span>
      </button>`;
      }).join('');

      const tHi = t.question_hi || t.question;
      const expHi = t.explanation_hi || t.explanation || '';

      testCardsHtml += `
      <div class="test-question-card" id="t-card-${idx}" data-correct="${t.correct_index ?? 0}">
        <div class="test-q-header">
          <span class="t-badge">
            <span class="lang-en">Question ${idx + 1} of ${testData.length}</span>
            <span class="lang-hi">प्रश्न ${idx + 1} / ${testData.length}</span>
          </span>
        </div>
        <div class="test-question-text">
          <span class="lang-en">${t.question || 'Test Question'}</span>
          <span class="lang-hi">${tHi}</span>
        </div>
        <div class="test-options-grid">${opts}
    </div>
        <div class="t-feedback hidden" id="t-feedback-${idx}">
          <p class="feedback-explanation">
            <strong><span class="lang-en">Solution:</span><span class="lang-hi">हल एवं व्याख्या:</span></strong>
            <span class="lang-en">${t.explanation || ''}</span>
            <span class="lang-hi">${expHi}</span>
          </p>
        </div>
      </div>
    `;
    });
    testCardsHtml += '\n          </div>\n          ';

    html = html.substring(0, tListStart + '<div class="test-questions-list">'.length) +
           testCardsHtml +
           html.substring(tSubmitBar);
  }

  // Submit test button
  html = html.replace(
    /<button type="button" class="btn-submit-test" id="btnSubmitTest"[^>]*>[\s\S]*?Submit Test[\s\S]*?<\/button>/,
    `<button type="button" class="btn-submit-test" id="btnSubmitTest" style="background: #2563eb;"><span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट जमा करें</span></button>`
  );

  // Result modal
  html = html.replace(
    /<h3>Test Result<\/h3>/,
    `<h3><span class="lang-en">Test Result</span><span class="lang-hi">परीक्षा परिणाम</span></h3>`
  );
  html = html.replace(
    /<p id="resFeedbackText">[\s\S]*?Review detailed solutions above for all questions\.[\s\S]*?<\/p>/,
    `<p id="resFeedbackText"><span class="lang-en">Review detailed solutions above for all questions.</span><span class="lang-hi">सभी प्रश्नों के विस्तृत समाधान ऊपर देखें।</span></p>`
  );
  html = html.replace(
    /<button type="button" class="btn-retake-test" id="btnRetakeTest">[\s\S]*?Retake Test[\s\S]*?<\/button>/,
    `<button type="button" class="btn-retake-test" id="btnRetakeTest"><span class="lang-en">Retake Test</span><span class="lang-hi">पुनः टेस्ट दें</span></button>`
  );

  // 15. Sidebar
  html = html.replace(
    /<span class="side-badge">Syllabus Section<\/span>/,
    `<span class="side-badge"><span class="lang-en">Syllabus Section</span><span class="lang-hi">पाठ्यक्रम अनुभाग</span></span>`
  );
  html = html.replace(
    /<h3>Physical Chemistry<\/h3>/,
    `<h3><span class="lang-en">Physical Chemistry</span><span class="lang-hi">भौतिक रसायन</span></h3>`
  );
  html = html.replace(
    /<h3>Inorganic Chemistry<\/h3>/,
    `<h3><span class="lang-en">Inorganic Chemistry</span><span class="lang-hi">अकार्बनिक रसायन</span></h3>`
  );
  html = html.replace(
    /<h3>Organic Chemistry<\/h3>/,
    `<h3><span class="lang-en">Organic Chemistry</span><span class="lang-hi">कार्बनिक रसायन</span></h3>`
  );
  html = html.replace(
    /<p class="side-desc">Branch topics covered under official UP PGT Chemistry curriculum\.<\/p>/,
    `<p class="side-desc"><span class="lang-en">Branch topics covered under official UP PGT Chemistry curriculum.</span><span class="lang-hi">आधिकारिक UP PGT रसायन विज्ञान पाठ्यक्रम के अंतर्गत शामिल विषय।</span></p>`
  );

  // 16. Bottom Navigation buttons
  html = html.replace(
    /<span>Exam Tracker →<\/span>/g,
    `<span class="lang-en">Exam Tracker →</span><span class="lang-hi">परीक्षा ट्रैकर →</span>`
  );
  html = html.replace(
    /<span>Next Topic →<\/span>/g,
    `<span class="lang-en">Next Topic →</span><span class="lang-hi">अगला टॉपिक →</span>`
  );
  html = html.replace(
    /<span>← Previous Topic<\/span>/g,
    `<span class="lang-en">← Previous Topic</span><span class="lang-hi">← पिछला टॉपिक</span>`
  );

  return externalizeChemistryRuntime(html);
}
