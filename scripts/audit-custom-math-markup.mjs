import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { load } = require('cheerio');
const roots = ['class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths'];
const totals = { pages: 0, customMathSpans: 0, withinDelimiters: 0, outsideDelimiters: 0 };
const examples = [];

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
  for (const match of text.matchAll(/\\\(|\\\)|\\\[|\\\]|\$\$|\$/g)) {
    const token = match[0];
    if (token === '$' || token === '$$') {
      if (mode === token) mode = null;
      else if (!mode) mode = token;
    } else if (token === '\\(' || token === '\\[') mode = token;
    else if ((token === '\\)' && mode === '\\(') || (token === '\\]' && mode === '\\[')) mode = null;
  }
  return mode;
}

function textBefore(root, target) {
  let result = '';
  function visit(node) {
    if (node === target) return true;
    if (node.type === 'text') result += node.data;
    else for (const child of node.children || []) if (visit(child)) return true;
    return false;
  }
  visit(root);
  return result;
}

for (const root of roots) {
  for (const file of walk(root)) {
    const html = fs.readFileSync(file, 'utf8');
    if (!html.includes('math-frac') && !html.includes('math-sqrt')) continue;
    const $ = load(html);
    let pageHasCustomMath = false;
    $('span.math-frac, span.math-sqrt').each((_, element) => {
      if ($(element).parents('span.math-frac, span.math-sqrt').length) return;
      pageHasCustomMath = true;
      totals.customMathSpans++;
      const block = $(element).closest('p,li,td,th,h1,h2,h3,h4,h5,h6').get(0) || element.parent;
      if (delimiterAt(textBefore(block, element))) totals.withinDelimiters++;
      else {
        totals.outsideDelimiters++;
        if (examples.length < 20) examples.push({ file, span: $.html(element), context: $(block).text().trim().slice(0, 220) });
      }
    });
    if (pageHasCustomMath) totals.pages++;
  }
}

console.log(JSON.stringify({ ...totals, examples }, null, 2));
