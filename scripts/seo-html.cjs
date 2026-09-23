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
  const $ = parse(source);
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
  if (additions.length) edits.push({ start: headEnd, end: headEnd, text: '  ' + additions.join('\n  ') + '\n' });
  return applyEdits(source, edits);
}
function collapseDuplicateDocumentShell(source) {
  const firstHeadOpen = source.search(/<head\b[^>]*>/i);
  const firstHeadClose = source.search(/<\/head\s*>/i);
  const secondHtml = source.toLowerCase().indexOf('<html', firstHeadClose + 7);
  if (firstHeadOpen < 0 || firstHeadClose < 0 || secondHtml < 0) return source;
  const secondHeadOpen = source.toLowerCase().indexOf('<head', secondHtml);
  const secondHeadClose = source.toLowerCase().indexOf('</head>', secondHeadOpen);
  const secondBodyOpen = source.toLowerCase().indexOf('<body', secondHeadClose);
  const secondBodyEnd = source.indexOf('>', secondBodyOpen);
  if ([secondHeadOpen, secondHeadClose, secondBodyOpen, secondBodyEnd].some(index => index < 0)) return source;
  const firstHead = source.slice(firstHeadOpen, firstHeadClose + 7);
  const secondHead = source.slice(secondHeadOpen, secondHeadClose + 7);
  const resourceSignature = head => head
    .replace(/<title\b[^>]*>[\s\S]*?<\/title>/gi, '')
    .replace(/<meta\b[^>]*>/gi, '')
    .replace(/<link\b[^>]*rel=["']canonical["'][^>]*>/gi, '')
    .replace(/<script\b[^>]*type=["']application\/ld\+json["'][^>]*>[\s\S]*?<\/script>/gi, '')
    .replace(/>\s+</g, '><')
    .trim();
  if (resourceSignature(firstHead) !== resourceSignature(secondHead)) return source;
  let removeStart = secondHtml;
  if (source.slice(secondHtml - 2, secondHtml) === 'l>') removeStart -= 2;
  source = source.slice(0, removeStart) + source.slice(secondBodyEnd + 1);
  source = source.replace(/<div\s+id=["']header-container-duplicate["']\s*><\/div>\s*/i, '');
  source = source.replace(/<main\s+class=["']syllabus-container["']\s+id=["']main-content-duplicate["']\s*>/i, '');
  return source;
}
module.exports = { ROOT, siteFiles, escapeHtml, compact, applyEdits, parse, editElement, setMetadata, collapseDuplicateDocumentShell };
