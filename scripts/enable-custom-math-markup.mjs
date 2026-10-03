import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const roots = ['class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths'];
const apply = process.argv.includes('--apply');
const helper = '/assets/js/math-markup-compat.js';
const mathjaxScriptTag = /<script\b(?=[^>]*\bsrc=["'][^"']*mathjax[^"']*["'])[^>]*>/i;
const candidates = [];

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) return walk(file);
    return entry.isFile() && entry.name.endsWith('.html') ? [file] : [];
  });
}

for (const directory of roots) {
  for (const file of walk(path.join(root, directory))) {
    const before = fs.readFileSync(file, 'utf8');
    if (!/<span\b[^>]*\bclass="[^"]*\bmath-(?:frac|sqrt)\b/.test(before)) continue;
    const katex = before.includes('renderMathInElement(document.body');
    const mathjax = mathjaxScriptTag.test(before);
    if (!katex && !mathjax) throw new Error(`${path.relative(root, file)}: custom math spans have no recognized renderer.`);
    candidates.push({ file, before, katex, mathjax });
  }
}

if (![0, 46].includes(candidates.length)) {
  throw new Error(`Expected 0 (already migrated) or 46 custom-math pages; found ${candidates.length}. Refusing to write.`);
}

const writes = new Map();
const rendererCounts = { katex: 0, mathjax: 0 };
for (const { file, before, katex, mathjax } of candidates) {
  const eol = before.includes('\r\n') ? '\r\n' : '\n';
  let after = before;
  if (katex) {
    rendererCounts.katex++;
    const calls = [...after.matchAll(/^([ \t]*)renderMathInElement\(document\.body,\s*\{/gm)];
    if (calls.length !== 1) throw new Error(`${path.relative(root, file)}: expected one KaTeX call; found ${calls.length}.`);
    if (!after.includes('window.SJMathsMathMarkup?.prepare(document.body);')) {
      const indent = calls[0][1];
      const statement = calls[0][0];
      after = after.replace(statement, `${indent}window.SJMathsMathMarkup?.prepare(document.body);${eol}${indent}${statement.trimStart()}`);
    }
    if (mathjax) {
      const katexRenderScript = /<script\b[^>]*>(?:(?!<\/script>)[\s\S])*?renderMathInElement\(document\.body,[\s\S]*?<\/script>/i;
      const renderMatch = katexRenderScript.exec(after);
      if (!renderMatch) throw new Error(`${path.relative(root, file)}: expected the KaTeX render script on a dual-renderer page.`);
      after = after.replace(renderMatch[0], '');
      after = after
        .replace(/<link\b[^>]*href=["'][^"']*katex[^"']*["'][^>]*\/?\s*>\s*/gi, '')
        .replace(/<script\b[^>]*src=["'][^"']*katex[^"']*["'][^>]*><\/script>\s*/gi, '');
    }
    if (!mathjax && !after.includes(helper)) {
      const headClose = after.toLowerCase().indexOf('</head>');
      if (headClose < 0) throw new Error(`${path.relative(root, file)}: missing head end for helper script.`);
      after = `${after.slice(0, headClose)}<script defer src="${helper}"></script>${eol}${after.slice(headClose)}`;
    }
  }
  if (mathjax) {
    rendererCounts.mathjax++;
    const mathjaxElement = /<script\b(?=[^>]*\bsrc=["'][^"']*mathjax[^"']*["'])[^>]*>\s*<\/script>/i.exec(after);
    const helperElement = /<script\b[^>]*src=["']\/assets\/js\/math-markup-compat\.js["'][^>]*>\s*<\/script>/i.exec(after);
    if (!mathjaxElement || !helperElement) throw new Error(`${path.relative(root, file)}: expected both helper and MathJax script elements.`);
    const closeHead = after.toLowerCase().lastIndexOf('</head>');
    if (closeHead < 0) throw new Error(`${path.relative(root, file)}: missing head end for MathJax setup.`);
    const mathjaxTag = mathjaxElement[0];
    const withoutScripts = after
      .replace(mathjaxElement[0], '')
      .replace(helperElement[0], '');
    const insertion = `<script src="${helper}" data-mathjax="true"></script>${eol}${mathjaxTag}`;
    const updatedHeadClose = withoutScripts.toLowerCase().lastIndexOf('</head>');
    const headPrefix = withoutScripts.slice(0, updatedHeadClose).replace(/[ \t\r\n]*$/, '');
    after = `${headPrefix}${eol}${insertion}${eol}${withoutScripts.slice(updatedHeadClose)}`;
  }

  if (after.includes(helper) && (after.match(/math-markup-compat\.js/g) || []).length !== 1) {
    throw new Error(`${path.relative(root, file)}: expected exactly one helper script reference.`);
  }
  if (after !== before) writes.set(file, Buffer.from(after, 'utf8'));
}

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', customMathPages: candidates.length, updatedPages: writes.size, renderers: rendererCounts, helper }, null, 2));
