import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import {
  externalizeMathematicsGenerator,
  externalizeMathematicsStyles,
  hydrateMathematicsStyles,
  mathematicsTopicCss,
  mathematicsTopicStyleLink,
  normalizeMathematicsGenerator,
} from './lib/mathematics-styles.mjs';
import {
  formatMathematicsOption,
  hasUndelimitedMathematics,
  normalizeMathematicsMarkup,
  normalizeRepeatedDisplayMathDelimiters,
} from './lib/mathematics-option-markup.mjs';

const cssHash = '8ebfdd570816fc96e19b3b3221bb2bdf0357ef785756d0d7b0bf80da6a4d7223';

function countUnescapedDollarDelimiters(value) {
  let slashCount = 0;
  let delimiterCount = 0;
  for (const character of value) {
    if (character === '\\') {
      slashCount++;
      continue;
    }
    if (character === '$' && slashCount % 2 === 0) delimiterCount++;
    slashCount = 0;
  }
  return delimiterCount;
}

test('Mathematics shared stylesheet matches the frozen 299-page source block', () => {
  assert.equal(Buffer.byteLength(mathematicsTopicCss), 15314);
  assert.equal(crypto.createHash('sha256').update(mathematicsTopicCss).digest('hex'), cssHash);
  assert.match(mathematicsTopicCss, /\.table-wrap\s*\{[^}]*contain:\s*layout paint/);
  assert.match(mathematicsTopicCss, /grid-template-columns: repeat\(auto-fit, minmax\(min\(100%, 310px\), 1fr\)\)/);
  assert.match(mathematicsTopicCss, /\.shortcut-formula\s*\{[^}]*overflow-x:\s*auto/);
  assert.match(mathematicsTopicCss, /\.katex-display\s*\{[^}]*overflow-x:\s*auto/);
  assert.match(mathematicsTopicCss, /\.interp-grid,\s*\.traps-grid,[^}]*\{\s*grid-template-columns:\s*minmax\(0,\s*1fr\)/);
  const minifiedCss = fs.readFileSync(new URL('../assets/css/mathematics-topic.min.css', import.meta.url), 'utf8');
  const sharedStyleHref = mathematicsTopicStyleLink.match(/href=["']([^"']+)["']/)?.[1] || '';
  const minifiedAssetHash = crypto.createHash('sha256').update(minifiedCss).digest('hex');
  assert.ok(sharedStyleHref.endsWith('?v=' + minifiedAssetHash.slice(0, 8)), 'generated pages must use the current minified asset hash');
  assert.ok(minifiedCss.includes('.table-wrap{contain:layout paint;overflow-x:auto;'), 'served stylesheet must contain table overflow within its scrollport');
  assert.ok(minifiedCss.includes('.katex-display{max-width:100%;overflow-x:auto;overflow-y:hidden}'), 'served stylesheet must contain long display equations');
  assert.match(minifiedCss, /\.shortcut-card\{[^}]*min-width:0/, 'served minified stylesheet must prevent intrinsic card overflow');
  assert.ok(minifiedCss.includes('.shortcuts-grid{grid-template-columns:minmax(0,1fr)}'), 'served mobile grid must shrink within the page');
  assert.ok(minifiedCss.includes('.interp-grid,.traps-grid,.methods-grid,.mcq-options-grid,.cross-nav{grid-template-columns:minmax(0,1fr)}'), 'served one-column grids must shrink around long formulas');
  const source = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  assert.equal((externalizeMathematicsStyles(source).match(/\$\{mathematicsTopicStyleLink\}/g) || []).length, 1);
});

test('Mathematics exact style extraction preserves cascade position and variants', () => {
  const source = `<head><link href="before.css"><style>\n${mathematicsTopicCss}\n</style><style>.later{color:red}</style></head><body>Educational content</body>`;
  assert.equal(
    externalizeMathematicsStyles(source),
    `<head><link href="before.css">${mathematicsTopicStyleLink}<style>.later{color:red}</style></head><body>Educational content</body>`,
  );
  assert.equal(externalizeMathematicsStyles(mathematicsTopicStyleLink), mathematicsTopicStyleLink);
  assert.equal(hydrateMathematicsStyles(mathematicsTopicStyleLink.replace('?v=4472833c', '?v=abc')), `<style>${mathematicsTopicCss}</style>`);
  assert.equal(externalizeMathematicsStyles(`<style>${mathematicsTopicCss}.extra{color:red}</style>`), `<style>${mathematicsTopicCss}.extra{color:red}</style>`);
  assert.equal(externalizeMathematicsStyles(`<style media="print">${mathematicsTopicCss}</style>`), `<style media="print">${mathematicsTopicCss}</style>`);
});

test('Mathematics generator changes only the shared stylesheet reference and import', () => {
  const source = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  const after = externalizeMathematicsGenerator(source);
  assert.equal(normalizeMathematicsGenerator(source), normalizeMathematicsGenerator(after));
  assert.ok(after.includes("import { mathematicsTopicStyleLink } from './lib/mathematics-styles.mjs';"));
  assert.equal(after.split('${mathematicsTopicStyleLink}').length - 1, 1);
  assert.equal(externalizeMathematicsGenerator(after), after);
});

test('Mathematics topic renderers typeset delimited formulas inside domain code values', () => {
  const generator = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  const fixer = fs.readFileSync(new URL('./fix_maths_rendering_all_files.mjs', import.meta.url), 'utf8');
  const allowedIgnoredTags = "ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'option']";
  assert.ok(generator.includes(allowedIgnoredTags), 'newly generated pages must allow math in <code> values');
  assert.ok(fixer.includes(allowedIgnoredTags), 'the shared rendering repair must allow math in <code> values');

  const mathRoot = fileURLToPath(new URL('../mathematics/', import.meta.url));
  const pages = [];
  const walk = directory => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const file = path.join(directory, entry.name);
      if (entry.isDirectory()) walk(file);
      else if (entry.isFile() && entry.name === 'index.html') pages.push(file);
    }
  };
  walk(mathRoot);

  let codeMathExpressions = 0;
  for (const file of pages) {
    const html = fs.readFileSync(file, 'utf8');
    const codeValues = [...html.matchAll(/<code\b[^>]*>([\s\S]*?)<\/code>/gi)];
    const hasDelimitedCodeMath = codeValues.some(([, content]) => /\$[^$]+\$|\\\(|\\\[/.test(content));
    if (!hasDelimitedCodeMath) continue;

    codeMathExpressions += codeValues.filter(([, content]) => /\$[^$]+\$|\\\(|\\\[/.test(content)).length;
    assert.ok(html.includes(allowedIgnoredTags), `${file}: renderer must not skip <code> math`);
    assert.ok(!html.includes("ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option']"), `${file}: stale renderer still skips <code>`);
  }
  assert.ok(codeMathExpressions > 0, 'fixture pages must exercise the code-math regression');
});

test('Mathematics MCQ options format raw TeX without putting prose into math mode', () => {
  assert.equal(formatMathematicsOption(String.raw`\text{(A) } 1:2 \text{ internal}`, 'A'), String.raw`$1:2 \text{ internal}$`);
  assert.equal(formatMathematicsOption(String.raw`\text{(A) } X^2 + Y^2 = 4`, 'A'), String.raw`$X^2 + Y^2 = 4$`);
  assert.equal(formatMathematicsOption(String.raw`No, because induction and well-ordering fail for \mathbb{R}`, 'A'), String.raw`No, because induction and well-ordering fail for $\mathbb{R}$`);
  assert.equal(formatMathematicsOption(String.raw`\mathbb{N} with standard successor`, 'A'), String.raw`$\mathbb{N}$ with standard successor`);
  assert.equal(formatMathematicsOption(String.raw`(B) \frac{1}{2}`, 'B'), String.raw`$\frac{1}{2}$`);
  assert.equal(formatMathematicsOption('$x^2 + y^2$', 'A'), '$x^2 + y^2$');
  assert.equal(formatMathematicsOption('A prime number', 'A'), 'A prime number');
  assert.equal(formatMathematicsOption('(A) 3', 'A'), '3');
  assert.throws(() => formatMathematicsOption('(A)', 'A'), /contains only its repeated label/);
  assert.equal(formatMathematicsOption('(A) $\\mathbb{R}$', 'A'), '$\\mathbb{R}$');
  assert.equal(formatMathematicsOption(String.raw`\text{(A) Both (A) and (R) are true}`, 'A'), 'Both (A) and (R) are true');
  assert.equal(formatMathematicsOption(String.raw`\text{Multiple values possible}`, 'C'), 'Multiple values possible');
  assert.equal(formatMathematicsOption('$x^2', 'A'), '$x^2$');
  assert.equal(formatMathematicsOption('($\\det$(A))^3', 'A'), '$(\\det(A))^3$');
  assert.equal(hasUndelimitedMathematics(String.raw`No, because induction and well-ordering fail for $\mathbb{R}$`), false);
});

test('Repeated dollar delimiters are normalized for existing and future topic formulas', () => {
  assert.equal(normalizeRepeatedDisplayMathDelimiters('$$$x^2$$'), '$$x^2$$');
  assert.equal(normalizeRepeatedDisplayMathDelimiters('$$$$x^2$$$$'), '$$x^2$$');
  assert.equal(normalizeMathematicsMarkup(String.raw`$$\{0, 1}$$`), String.raw`$$\{0, 1\}$$`);
  assert.equal(normalizeMathematicsMarkup(String.raw`$$S = \left\{x \in \mathbb{R} : x > 0 \right}$$`), String.raw`$$S = \left\{x \in \mathbb{R} : x > 0 \right\}$$`);
  assert.equal(normalizeMathematicsMarkup(String.raw`$$\{\{1,2}, \{3\}}$$`), String.raw`$$\{\{1,2\}, \{3\}\}$$`);
  const generator = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  assert.ok(generator.includes('normalizeMathematicsMarkup(`<!doctype html>'));
  assert.ok(generator.includes('never add extra dollars such as $$$'));

  const mathRoot = fileURLToPath(new URL('../mathematics/', import.meta.url));
  const pages = [];
  const walk = directory => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const file = path.join(directory, entry.name);
      if (entry.isDirectory()) walk(file);
      else if (entry.isFile() && entry.name === 'index.html') pages.push(file);
    }
  };
  walk(mathRoot);
  for (const file of pages) {
    assert.doesNotMatch(fs.readFileSync(file, 'utf8'), /\$\$\$/, `${file}: repeated dollar delimiters break KaTeX rendering`);
  }
});

test('All generated Mathematics MCQ options have math delimiters and a shared formatter', () => {
  const generator = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  assert.ok(generator.includes("formatMathematicsOption, normalizeMathematicsMarkup } from './lib/mathematics-option-markup.mjs';"));
  assert.ok(generator.includes('const optionText = formatMathematicsOption(opt, letters[oIdx]);'));

  const mathRoot = fileURLToPath(new URL('../mathematics/', import.meta.url));
  const pages = [];
  const walk = directory => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const file = path.join(directory, entry.name);
      if (entry.isDirectory()) walk(file);
      else if (entry.isFile() && entry.name === 'index.html') pages.push(file);
    }
  };
  walk(mathRoot);

  let optionCount = 0;
  for (const file of pages) {
    const html = fs.readFileSync(file, 'utf8');
    for (const [, optionBlock] of html.matchAll(/<div\b(?=[^>]*class=["'][^"']*\bmcq-option\b[^"']*["'])[^>]*>([\s\S]*?)<\/div>/gi)) {
      const label = optionBlock.match(/<span\b[^>]*class=["'][^"']*\bopt-label\b[^"']*["'][^>]*>([\s\S]*?)<\/span>/i)?.[1]?.replace(/<[^>]*>/g, '').trim();
      const optionText = optionBlock.match(/<span\b[^>]*class=["'][^"']*\bopt-text\b[^"']*["'][^>]*>([\s\S]*?)<\/span>/i)?.[1];
      if (!optionText) continue;
      optionCount++;
      assert.equal(countUnescapedDollarDelimiters(optionText) % 2, 0, file + ': answer option ' + label + ' has unbalanced math delimiters: ' + optionText);
      assert.notEqual(optionText.trim(), '', `${file}: answer option ${label} is empty`);
      assert.equal(hasUndelimitedMathematics(optionText), false, `${file}: raw math remains in an MCQ option: ${optionText}`);
      const duplicatedLabel = new RegExp(`^\\s*(?:\\(${label}\\)|\\\\text\\{\\s*\\(${label}\\)\\s*\\})\\s+`, 'i');
      assert.equal(duplicatedLabel.test(optionText), false, `${file}: option label is repeated in its text: ${optionText}`);
    }
  }
  assert.ok(optionCount > 0, 'Mathematics topic pages must contain MCQ answer options');
});

test('Options embedded in three mathematics MCQ prompts appear as separate answer choices', () => {
  const pages = [
    '../mathematics/coordinate-geometry/two-dimensional/general-second-degree/hyperbola-condition/index.html',
    '../mathematics/linear-algebra/linear-transformations/transpose/index.html',
    '../mathematics/mechanics/statics/equilibrium-under-three-forces/index.html',
  ];
  for (const relativePath of pages) {
    const html = fs.readFileSync(new URL(relativePath, import.meta.url), 'utf8');
    assert.doesNotMatch(html, /<span class="opt-text">\s*<\/span>/, `${relativePath}: answer choices must not be empty`);
    const questions = [...html.matchAll(/<div class="mcq-question">([\s\S]*?)<\/div>/g)].map(([, question]) => question);
    assert.doesNotMatch(questions.join('\n'), /\\n\s*\(A\)\s|\$\s*\(A\)\\\s/, `${relativePath}: choices remain duplicated inside question text`);
    assert.match(html, /Both A and R are true and R is the correct explanation/, `${relativePath}: assertion/reason answer wording must be retained`);
  }
});

test('Cartesian plane x-axis ratio MCQ key and explanation agree with the section formula', () => {
  const page = fs.readFileSync(new URL('../mathematics/coordinate-geometry/two-dimensional/cartesian-plane/index.html', import.meta.url), 'utf8');
  const start = page.indexOf('<div class="mcq-box" id="mcq-2"');
  const end = page.indexOf('<div class="mcq-box" id="mcq-3"', start);
  assert.ok(start >= 0 && end > start, 'the x-axis ratio MCQ must remain present');
  const question = page.slice(start, end);
  assert.match(question, /data-correct="0"/);
  assert.equal([...question.matchAll(/handleOptionClick\(this, (\d+), 2\)/g)].every(([, correct]) => correct === '0'), true);
  assert.match(question, /6m - 3n = 0[\s\S]*m:n = 1:2[\s\S]*division is internal/i);
  assert.doesNotMatch(question, /Wait, sign check/);
});

test('Cartesian plane shifted-origin MCQ key agrees with its completed-square derivation', () => {
  const page = fs.readFileSync(new URL('../mathematics/coordinate-geometry/two-dimensional/cartesian-plane/index.html', import.meta.url), 'utf8');
  const start = page.indexOf('<div class="mcq-box" id="mcq-3"');
  const end = page.indexOf('<div class="mcq-box" id="mcq-4"', start);
  assert.ok(start >= 0 && end > start, 'the shifted-origin MCQ must remain present');
  const question = page.slice(start, end);
  assert.match(question, /data-correct="0"/);
  assert.match(question, /handleOptionClick\(this, 0, 3\)/);
  assert.match(question, /<span class="opt-text">\$X\^2 \+ Y\^2 = 4\$<\/span>/);
  assert.match(question, /X\^2 \+ Y\^2 - 4 = 0[\\\s\S]*X\^2 \+ Y\^2 = 4/);
});

test('Direction-cosine angle formulas use complete acute-angle absolute values', () => {
  for (const file of [
    '../mathematics/vectors-and-three-dimensional-geometry/three-dimensional/angle-between-two-planes/index.html',
    '../mathematics/vectors-and-three-dimensional-geometry/three-dimensional/angle-between-two-lines/index.html',
  ]) {
    const page = fs.readFileSync(new URL(file, import.meta.url), 'utf8');
    assert.match(page, /\\cos \\theta = \\left\|l_1 l_2 \+ m_1 m_2 \+ n_1 n_2\\right\|/);
  }
});

test('Mathematics topic pages retain their renderers and valid structured data', () => {
  const mathRoot = fileURLToPath(new URL('../mathematics/', import.meta.url));
  const sharedStyleHref = mathematicsTopicStyleLink.match(/href=["']([^"']+)["']/)?.[1] || '';
  const pages = [];
  const walk = directory => {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
      const file = path.join(directory, entry.name);
      if (entry.isDirectory()) walk(file);
      else if (entry.isFile() && entry.name === 'index.html') pages.push(file);
    }
  };
  walk(mathRoot);
  assert.equal(pages.length, 299, 'audit must cover every mathematics topic page');

  for (const file of pages) {
    const html = fs.readFileSync(file, 'utf8');
    const relativePath = path.relative(mathRoot, file);
    assert.ok(html.includes('href="' + sharedStyleHref + '"'), relativePath + ': page must load the current shared stylesheet');
    assert.doesNotMatch(html, /^\s*undefined\s*$/m, relativePath + ': page scripts must not be replaced by placeholders');
    assert.equal((html.match(/katex@0\.16\.11\/dist\/katex\.min\.js/g) || []).length, 1, relativePath + ': load KaTeX once');
    for (const [, json] of html.matchAll(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)) {
      assert.doesNotThrow(() => JSON.parse(json), relativePath + ': structured data must remain valid JSON');
    }
  }
});
