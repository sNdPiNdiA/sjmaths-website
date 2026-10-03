import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const require = createRequire(import.meta.url);
const { load } = require('cheerio');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const targets = [
  'agriculture', 'class-10-science', 'class-11-applied-mathematics',
  'class-11-chemistry', 'class-11-physics', 'class-12-physics',
  'class-9-advanced-maths', 'class-9-advanced-science', 'class-9-science',
  'home-science', 'sat', 'ssc-cgl', 'up-assistant-teacher', 'upsc', 'upsssc-pet'
];
const helperPath = '/assets/js/math-markup-compat.js';
const mathJaxUrl = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
const apply = process.argv.includes('--apply');
const candidates = [];

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry => {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) return walk(file);
    return entry.isFile() && entry.name.endsWith('.html') ? [file] : [];
  });
}

function delimiterAt(text) {
  let mode = null;
  for (const match of text.matchAll(/\\\(|\\\)|\\\[|\\\]|\$\$?/g)) {
    const token = match[0];
    if (!token) continue;
    if ((token === '$' || token === '$$') && text[match.index - 1] === '\\') continue;
    if (token === '$' || token === '$$') {
      if (mode === token) mode = null;
      else if (!mode) mode = token;
    } else if (token === '\\(' || token === '\\[') mode = token;
    else if ((token === '\\)' && mode === '\\(') || (token === '\\]' && mode === '\\[')) mode = null;
  }
  return mode;
}

function textBefore(block, target) {
  let text = '';
  function visit(node) {
    if (node === target) return true;
    if (node.type === 'text') text += node.data;
    else for (const child of node.children || []) if (visit(child)) return true;
    return false;
  }
  visit(block);
  return text;
}

function hasDelimitedCustomMath(html) {
  const $ = load(html);
  let found = false;
  $('span.math-frac, span.math-sqrt').each((_, node) => {
    if (found || $(node).parents('span.math-frac, span.math-sqrt').length) return;
    const block = $(node).closest('p,li,td,th,h1,h2,h3,h4,h5,h6').get(0) || node.parent;
    if (delimiterAt(textBefore(block, node))) found = true;
  });
  return found;
}

function getScriptBlocks(html) {
  return [...html.matchAll(/<script\b[^>]*>[\s\S]*?<\/script\s*>/gi)].map(match => ({
    text: match[0], index: match.index
  }));
}

function addHelper(html, mathJaxPresent) {
  if (html.includes(helperPath)) return html;
  const helperTag = `<script src="${helperPath}"${mathJaxPresent ? ' data-mathjax="true"' : ''}></script>`;
  const mathJax = /<script\b(?=[^>]*\bsrc=["'][^"']*mathjax[^"']*["'])[^>]*>/i.exec(html);
  if (mathJaxPresent && mathJax) return `${html.slice(0, mathJax.index)}${helperTag}\n${html.slice(mathJax.index)}`;

  const katexComment = /<!--[\s\S]*?KaTeX[\s\S]*?-->/i.exec(html);
  if (katexComment) return `${html.slice(0, katexComment.index)}${helperTag}\n${html.slice(katexComment.index)}`;

  const scripts = getScriptBlocks(html);
  const rendererScript = scripts.find(({ text }) => /renderMathInElement\s*\(/i.test(text));
  if (rendererScript) return `${html.slice(0, rendererScript.index)}${helperTag}\n${html.slice(rendererScript.index)}`;

  const mainScript = /<script\b(?=[^>]*\bsrc=["'][^"']*\/assets\/js\/main(?:\.min)?\.js[^"']*["'])[^>]*>/i.exec(html);
  if (mainScript) return `${html.slice(0, mainScript.index)}${helperTag}\n${html.slice(mainScript.index)}`;

  const closeHead = html.toLowerCase().lastIndexOf('</head>');
  if (closeHead < 0) throw new Error('Cannot add math compatibility script: </head> is missing.');
  return `${html.slice(0, closeHead)}${helperTag}\n${html.slice(closeHead)}`;
}

function ensureMathJax(html) {
  if (/src=["'][^"']*mathjax[^"']*["']/i.test(html)) return html;
  const block = `<script>\nwindow.MathJax = { tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']], processEscapes: true } };\n</script>\n<script src="${helperPath}" data-mathjax="true"></script>\n<script async id="MathJax-script" src="${mathJaxUrl}"></script>\n`;
  const closeHead = html.toLowerCase().lastIndexOf('</head>');
  if (closeHead < 0) throw new Error('Cannot add MathJax: </head> is missing.');
  return `${html.slice(0, closeHead)}${block}${html.slice(closeHead)}`;
}

function stripKaTeXRenderer(html, file, keepKaTeX) {
  const originalHeadClose = html.toLowerCase().indexOf('</head>');
  const originalRenderCall = html.toLowerCase().indexOf('rendermathinelement(document.body');
  if (keepKaTeX && html.includes(helperPath) && originalHeadClose >= 0
    && originalRenderCall >= 0 && originalRenderCall < originalHeadClose) {
    const originalScriptOpen = html.toLowerCase().lastIndexOf('<script', originalRenderCall);
    const originalScriptClose = html.toLowerCase().indexOf('</script', originalRenderCall);
    if (originalScriptOpen >= 0 && originalScriptClose >= 0 && originalScriptClose < originalHeadClose
      && html.slice(originalScriptOpen, originalScriptClose).includes('SJMathsMathMarkup?.prepare(document.body)')) return html;
  }
  let result = html;
  if (!keepKaTeX) {
    result = result
      .replace(/<!--[^>]*\bKaTeX\b[^>]*-->/gi, '')
      .replace(/<link\b[^>]*href=["'][^"']*katex[^"']*["'][^>]*\/?\s*>\s*/gi, '')
      .replace(/<script\b(?=[^>]*\bsrc=["'][^"']*(?:katex\.min|auto-render)[^"']*["'])[^>]*>[\s\S]*?<\/script\s*>\s*/gi, '');
  }

  const headClose = result.toLowerCase().indexOf('</head>');
  const renderCall = result.toLowerCase().indexOf('rendermathinelement(document.body');
  if (headClose >= 0 && (renderCall < 0 || renderCall > headClose)) return result;
  if (headClose < 0 || renderCall < 0) {
    throw new Error(`${path.relative(root, file)}: cannot safely locate the KaTeX page-render block in <head>.`);
  }
  const scriptOpen = result.toLowerCase().lastIndexOf('<script', renderCall);
  const scriptClose = result.toLowerCase().indexOf('</script', renderCall);
  if (scriptOpen < 0) throw new Error(`${path.relative(root, file)}: KaTeX page-render script has no opening tag.`);
  const blockEnd = scriptClose >= 0 && scriptClose < headClose
    ? result.indexOf('>', scriptClose) + 1
    : headClose;
  result = result.slice(0, scriptOpen) + result.slice(blockEnd);

  if (keepKaTeX) {
    const closeHead = result.toLowerCase().indexOf('</head>');
    const renderer = `<script>\ndocument.addEventListener('DOMContentLoaded', function () {\n  if (typeof renderMathInElement !== 'function') return;\n  window.SJMathsMathMarkup?.prepare(document.body);\n  renderMathInElement(document.body, {\n    delimiters: [\n      { left: '$$', right: '$$', display: true },\n      { left: '$', right: '$', display: false },\n      { left: '\\\\(', right: '\\\\)', display: false },\n      { left: '\\\\[', right: '\\\\]', display: true }\n    ],\n    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option'],\n    throwOnError: false\n  });\n});\n</script>\n`;
    result = `${result.slice(0, closeHead)}${renderer}${result.slice(closeHead)}`;
  }
  return result;
}

const writes = new Map();
const folderStats = Object.fromEntries(targets.map(folder => [folder, { pages: 0, updated: 0, mathJax: 0, katexOrMain: 0, addedMathJax: 0, removedDuplicateKatex: 0 }]));

for (const folder of targets) {
  for (const file of walk(path.join(root, folder))) {
    const before = fs.readFileSync(file, 'utf8');
    if (!hasDelimitedCustomMath(before)) continue;
    const stats = folderStats[folder];
    stats.pages++;
    const hasMathJax = /src=["'][^"']*mathjax[^"']*["']/i.test(before);
    const hasDirectKatex = /katex\.min\.js|renderMathInElement\s*\(\s*document\.body/i.test(before);
    const hasKatexOrMain = /katex\.min\.js|renderMathInElement\s*\(|\/assets\/js\/main(?:\.min)?\.js/i.test(before);
    let after = before;

    if (hasMathJax && hasDirectKatex) {
      after = stripKaTeXRenderer(after, file, false);
      stats.removedDuplicateKatex++;
    }

    if (hasMathJax) {
      after = addHelper(after, true);
      stats.mathJax++;
    } else if (hasKatexOrMain) {
      stats.katexOrMain++;
      after = addHelper(after, false);
      if (hasDirectKatex) after = stripKaTeXRenderer(after, file, true);
    } else {
      after = ensureMathJax(after);
      stats.addedMathJax++;
    }

    if (!after.includes(helperPath)) throw new Error(`${path.relative(root, file)}: compatibility helper was not added.`);
    if (/src=["'][^"']*mathjax[^"']*["']/i.test(after)
      && /katex\.min\.js|renderMathInElement\s*\(\s*document\.body/i.test(after)) {
      throw new Error(`${path.relative(root, file)}: duplicate MathJax/KaTeX rendering remains.`);
    }
    if (after !== before) {
      stats.updated++;
      writes.set(file, Buffer.from(after, 'utf8'));
    }
  }
}

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', candidatePages: Object.values(folderStats).reduce((sum, item) => sum + item.pages, 0), updatedPages: writes.size, folders: folderStats }, null, 2));
