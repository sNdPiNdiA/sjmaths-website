/* Apply the shared exam UI while preserving lesson content and metadata. */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const vm = require('vm');
const { parse } = require('./seo-html.cjs');
const ROOT = path.resolve(__dirname, '..');
const roots = ['upsssc-pet', 'up-assistant-teacher', 'upsc'];
const fonts = 'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Source+Serif+4:ital,wght@0,400;0,600;1,400&amp;display=swap';
function decorate(source) {
  if (!/<head\b/i.test(source) || !/<body\b/i.test(source)) return source;
  const lineBreaks = source.match(/\r\n|\n/g) || [];
  const crlfCount = lineBreaks.filter(lineBreak => lineBreak === '\r\n').length;
  const eol = crlfCount > lineBreaks.length - crlfCount ? '\r\n' : '\n';
  let result = source.replace(/<body\b([^>]*)>/i, (tag, attrs) => {
    if (/class=["'][^"']*\bexam-ui\b/.test(attrs)) return tag;
    if (/class=["']/.test(attrs)) return tag.replace(/class=(["'])/, 'class=$1exam-ui ');
    return `<body class="exam-ui"${attrs}>`;
  });
  // Eight month tabs need readable labels and touch targets, so retain their
  // existing horizontal strip rather than compressing them into the four-tab dock.
  if (source.includes('month-sub-nav')) result = result.replace(/class="study-tabs"(?![^>]*data-mobile-tab-dock)/, 'class="study-tabs" data-mobile-tab-dock="off"');
  result = result.replace(/mobile-tab-dock\.js\?v=[^"']+/g, 'mobile-tab-dock.js?v=20261007-exam-strip');
  result = result.replace(/mobile-tab-dock\.min\.js(?:\?v=[^"']*)?/g, 'mobile-tab-dock.min.js?v=eb26185ea1-main-tabs');
  result = result.replace(/upsc-renderer(?:\.[a-f0-9]{12})?\.min\.js(?:\?v=[^"']*)?/g, 'upsc-renderer.e208a1f3d3da.min.js?v=e208a1f3d3da-bilingual-v4');
  result = result.replace(/upsc-language\.min\.js\?v=[^"']+/g, 'upsc-language.min.js?v=devanagari-only-20261009');
  result = result.replace(/<link\b[^>]*href=["']https:\/\/fonts.googleapis.com\/css2[^"']*["'][^>]*>/gi,
    `<link href="${fonts}" rel="stylesheet"/>`);
  const links = [];
  if (!result.includes('/assets/css/syllabus-planner.')) links.push('<link href="/assets/css/syllabus-planner.min.css?v=e666edd9" rel="stylesheet"/>');
  if (!result.includes('fonts.googleapis.com/css2')) links.push(`<link href="${fonts}" rel="stylesheet"/>`);
  if (!result.includes('/assets/css/exam-learning.')) links.push('<link href="/assets/css/exam-learning.min.css?v=98e3b0ce68-spacing" rel="stylesheet"/>');
  result = result.replace(/<\/head>/i, links.join(eol) + (links.length ? eol : '') + '</head>');
  if (!/id=["']header-container["']/.test(result)) result = result.replace(/(<body\b[^>]*>)/i, `$1${eol}<div id="header-container"></div>`);
  if (!/id=["']footer-container["']/.test(result)) result = result.replace(/<\/body>/i, `<div id="footer-container"></div>${eol}</body>`);
  const components = [];
  if (!result.includes('/assets/js/upsc-language')) components.push('<script defer src="/assets/js/upsc-language.min.js?v=devanagari-only-20261009"></script>');
  if (!result.includes('/assets/js/global-header')) components.push('<script defer src="/assets/js/global-header.min.js?v=1a5de11b"></script>');
  if (!result.includes('/assets/js/global-footer')) components.push('<script defer src="/assets/js/global-footer.min.js?v=103a5a49"></script>');
  return result.replace(/<\/body>/i, components.join(eol) + (components.length ? eol : '') + '</body>');
}
function fingerprint(source) {
  const $ = parse(source);
  const scripts = $('script').filter((_, el) => !/\/assets\/js\/(?:global-(header|footer)|upsc-language|upsc-renderer(?:\.[a-f0-9]{12})?\.min\.js)/.test($(el).attr('src') || '')).map((_, el) => {
    if ($(el).attr('src')) $(el).attr('src', $(el).attr('src').replace(/\?v=[^?#]+/, ''));
    return $.html(el);
  }).get();
  $('script,style').remove();
  return {
    text: $('body').text().replace(/\s+/g, ' ').trim(),
    links: $('a').map((_, el) => $(el).attr('href') || '').get(),
    ids: $('[id]').map((_, el) => $(el).attr('id')).get().filter(id => !['header-container','footer-container'].includes(id)),
    metadata: $('title,meta,link[rel="canonical"]').map((_, el) => $.html(el)).get(),
    scripts,
  };
}
function files(selectedRoots = roots) {
  const list = [];
  function walk(dir) {
    for (const entry of fs.readdirSync(path.join(ROOT, dir), { withFileTypes: true })) {
      const file = `${dir}/${entry.name}`;
      if (entry.isDirectory()) walk(file);
      else if (file.endsWith('.html')) list.push(file);
    }
  }
  selectedRoots.forEach(walk);
  return list;
}
function main() {
  const write = process.argv.includes('--write');
  const requestedRoots = process.argv.filter(arg => arg.startsWith('--root=')).map(arg => arg.slice('--root='.length));
  const selectedRoots = requestedRoots.length ? [...new Set(requestedRoots)] : roots;
  const unknownRoots = selectedRoots.filter(root => !roots.includes(root));
  if (unknownRoots.length) throw new Error(`Unknown exam UI root(s): ${unknownRoots.join(', ')}`);
  const report = { pages: [], changed: 0, incomplete: [], syntaxErrors: [], duplicateIds: [], missingAssets: [], missingUI: [] };
  for (const file of files(selectedRoots)) {
    const absolute = path.join(ROOT, file);
    const before = fs.readFileSync(absolute, 'utf8');
    if (!/<head\b/i.test(before) || !/<body\b/i.test(before)) {
      report.incomplete.push(file);
      continue;
    }
    const after = decorate(before);
    if (JSON.stringify(fingerprint(before)) !== JSON.stringify(fingerprint(after))) throw new Error(`Content changed: ${file}`);
    if (write && before !== after) { fs.writeFileSync(absolute, after); report.changed++; }
    const source = write ? after : before;
    const $ = parse(source);
    const ids = $('[id]').map((_, el) => $(el).attr('id')).get();
    const duplicates = ids.filter((id, i) => ids.indexOf(id) !== i);
    if (duplicates.length) report.duplicateIds.push({ file, ids: [...new Set(duplicates)] });
    $('script').each((_, el) => {
      const type = $(el).attr('type');
      const code = $(el).html();
      if ($(el).attr('src') || type === 'module') return;
      try {
        if (type && /json/.test(type)) JSON.parse(code);
        else if (!type || /javascript/.test(type)) new vm.Script(code);
      } catch (error) { report.syntaxErrors.push({ file, message: error.message }); }
    });
    $('[src],link[href]').each((_, el) => {
      const url = $(el).attr('src') || $(el).attr('href');
      if (!url || !url.startsWith('/') || url.startsWith('//')) return;
      const target = path.join(ROOT, url.split(/[?#]/)[0]);
      if (!fs.existsSync(target)) report.missingAssets.push({ file, url });
    });
    if (!/\/assets\/css\/exam-learning(?:\.min)?\.css/.test(source) || !$('body').hasClass('exam-ui')) report.missingUI.push(file);
    report.pages.push({ file, contentPreserved: true, fingerprint: crypto.createHash('sha256').update(JSON.stringify(fingerprint(source))).digest('hex'), tabs: $('.study-tabs .tab-btn,.syllabus-tabs .tab-btn').length });
  }
  fs.mkdirSync(path.join(ROOT, 'scratch'), { recursive: true });
  fs.writeFileSync(path.join(ROOT, 'scratch/exam-ui-verification.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify({ roots: selectedRoots, pages: report.pages.length, changed: report.changed, incomplete: report.incomplete, syntaxErrors: report.syntaxErrors, duplicateIds: report.duplicateIds, missingAssets: report.missingAssets, missingUI: report.missingUI.length }, null, 2));
  if (report.syntaxErrors.length || report.missingUI.length) process.exitCode = 1;
}
module.exports = { decorate, fingerprint };
if (require.main === module) main();
