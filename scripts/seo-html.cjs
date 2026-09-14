const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const cheerio = require('cheerio');
const ROOT = path.resolve(__dirname, '..');
function siteFiles() {
  return [...new Set(execFileSync('git', ['ls-files', '--cached', '--others', '--exclude-standard', '-z'], {
    cwd: ROOT, encoding: 'utf8', maxBuffer: 40e6,
  }).split('\0').filter(Boolean))];
}
const escapeHtml = text => String(text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const compact = text => String(text || '').replace(/\s+/g, ' ').trim();
function applyEdits(source, edits) {
  let end = source.length;
  for (const edit of edits.sort((a, b) => b.start - a.start)) {
    if (edit.end > end) throw new Error('Overlapping source edits');
    source = source.slice(0, edit.start) + edit.text + source.slice(edit.end);
    end = edit.start;
  }
  return source;
}
function parse(source) { return cheerio.load(source, { sourceCodeLocationInfo: true }); }
function editElement(el, text) {
  const loc = el.sourceCodeLocation;
  if (!loc) throw new Error('Element has no source location');
  return { start: loc.startOffset, end: loc.endOffset, text };
}
function setMetadata(source, values) {
  const headEnd = source.search(/<\/head\s*>/i);
  if (headEnd < 0) throw new Error('No closing head');
  const head = source.slice(0, headEnd);
  const $ = parse(head);
  const edits = [];
  const additions = [];
  for (const [key, value] of Object.entries(values)) {
    let matches, tag;
    if (key === 'title') { matches = $('title'); tag = `<title>${escapeHtml(value)}</title>`; }
    else if (key === 'canonical') { matches = $('link[rel="canonical"]'); tag = `<link rel="canonical" href="${escapeHtml(value)}">`; }
    else {
      matches = $('meta').filter((_, el) => ($(el).attr('name') || $(el).attr('property')) === key);
      tag = `<meta ${key.startsWith('og:') ? 'property' : 'name'}="${key}" content="${escapeHtml(value)}">`;
    }
    if (matches.length) matches.each((i, el) => edits.push(editElement(el, i === 0 ? tag : '')));
    else additions.push(tag);
  }
  return applyEdits(head, edits) + (additions.length ? '  ' + additions.join('\n  ') + '\n' : '') + source.slice(headEnd);
}
module.exports = { ROOT, siteFiles, escapeHtml, compact, applyEdits, parse, editElement, setMetadata };
