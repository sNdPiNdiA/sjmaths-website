// Repair metadata in place without serializing/reformatting educational HTML.
const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { ROOT, siteFiles, compact, parse, setMetadata, collapseDuplicateDocumentShell } = require('./seo-html.cjs');
const dry = process.argv.includes('--dry-run');
const syncSocial = process.argv.includes('--sync-social');
const scopes = process.argv.find(arg => arg.startsWith('--scope='))?.slice(8).split(',').map(value => value.trim()).filter(Boolean) || [];
const files = siteFiles().filter(policy.isManagedHtmlPath).filter(file => !scopes.length || scopes.some(scope => file.startsWith(scope)));
const pages = files.map(file => {
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  const $ = parse(source.slice(0, source.indexOf('</head>') + 7));
  return { file, title: compact($('title').first().text()), description: $('meta[name="description"]').first().attr('content') || '' };
});
const counts = { title: new Map(), description: new Map() };
const truncateAtWord = (value, limit) => {
  if (value.length <= limit) return value;
  const clipped = value.slice(0, limit - 1).replace(/\s+\S*$/, '').replace(/[\s,;:–—-]+$/, '');
  return `${clipped}.`;
};
const truncateTitle = (value, limit) => {
  if (value.length <= limit) return value;
  const suffix = value.match(/(\s*\|\s*[^|]+\s*\|\s*SJMaths)$/i)?.[1] || ' | SJMaths';
  const head = value.slice(0, Math.max(1, limit - suffix.length)).replace(/\s+\S*$/, '').replace(/[\s,;:–—-]+$/, '');
  return head + suffix;
};
for (const p of pages) for (const key of Object.keys(counts)) counts[key].set(p[key], (counts[key].get(p[key]) || 0) + 1);
let modified = 0, placeholders = 0;
for (const p of pages) {
  const original = fs.readFileSync(path.join(ROOT, p.file), 'utf8');
  const source = p.file === 'upsc-aso/index.html' ? collapseDuplicateDocumentShell(original) : original;
  if (!source.trim() || !/<\/head>/i.test(source)) continue;
  const noindex = policy.hasNoindex(source);
  const placeholder = policy.isPlaceholderHtml(source);
  if (placeholder) {
    if (!noindex) { const next = setMetadata(source, { robots: 'noindex, follow' }); if (!dry) fs.writeFileSync(path.join(ROOT, p.file), next); modified++; placeholders++; }
    continue;
  }
  if (noindex || policy.hasRedirect(source)) continue;
  const $ = parse(source);
  const meta = key => $('meta').filter((_, el) => ($(el).attr('name') || $(el).attr('property')) === key);
  const currentCanonical = $('link[rel="canonical"]').first().attr('href');
  const expected = policy.toUrl(p.file);
  // Retain intentional aliases such as pages/about/index.html -> pages/about.
  if (p.file.startsWith('pages/') && /\/index\.html$/.test(p.file) && currentCanonical && currentCanonical !== expected) continue;
  let title = p.title;
  let description = p.description;
  const topic = compact($('h1').first().text());
  const basename = path.posix.basename(p.file, '.html');
  if (counts.title.get(title) > 1 && topic && !/^(notes|chapter notes|study guide|welcome|exemplar practice updating)$/i.test(topic)) {
    const classLabel = p.file.match(/^class-(\d+)-(maths|physics|science)\//);
    const prefix = classLabel && !topic.toLowerCase().includes('class ' + classLabel[1]) ? `Class ${classLabel[1]} ${classLabel[2] === 'maths' ? 'Maths' : classLabel[2][0].toUpperCase() + classLabel[2].slice(1)}: ` : '';
    title = `${prefix}${topic.replace(/\s*\|\s*SJMaths$/i, '')} | SJMaths`;
    // Some topic pages retain the chapter's H1; use the existing route label to distinguish them.
    if (basename !== 'index' && !title.toLowerCase().includes(basename.replace(/-/g, ' '))) {
      const label = basename.replace(/-/g, ' ').replace(/\b[a-z]/g, c => c.toUpperCase());
      if (!/exercise|test|set|paper/.test(basename)) title = `${label} — ${p.title.replace(/\s*\|\s*SJMaths$/i, '')} | SJMaths`;
    }
  }
  if (!description) description = p.file === 'hackathon/webmcp/demo/index.html'
    ? 'Explore the SJMaths WebMCP demo: curriculum discovery, prerequisite checks, practice evaluation, hints and adaptive next steps for Class 10 Maths.'
    : compact($('main p').first().text());
  if (counts.description.get(description) > 1 && title !== p.title) {
    const label = title.replace(/\s*\|\s*SJMaths$/i, '');
    description = `${label}. ${description}`;
  }
  title = title
    .replace(/\s*\|\s*UP Upper Primary Teacher \(Class 6-8\)\s*\|\s*SJMaths$/i, ' | UP Teacher | SJMaths')
    .replace(/\s*[-|]\s*UP Upper Primary Teacher Syllabus\s*\|\s*SJMaths$/i, ' | UP Teacher | SJMaths')
    .replace(/\s*\|\s*UP Assistant Teacher(?: Exam)?\s*\|\s*SJMaths$/i, ' | UP Assistant Teacher | SJMaths');
  title = truncateTitle(title, 120);
  if (description && description.length < 40) description = `${description.replace(/[.\s]+$/, '')}. Includes concise notes and revision guidance for exam preparation.`;
  description = truncateAtWord(description, 320);
  const values = {};
  if (title !== p.title || $('title').length > 1) values.title = title;
  if (description !== p.description || meta('description').length > 1) values.description = description;
  if (currentCanonical !== expected || $('link[rel="canonical"]').length !== 1) values.canonical = expected;
  const defaults = { 'og:title': title, 'og:description': description, 'og:url': expected, 'og:image': 'https://sjmaths.com/assets/icons/icon-512x512.png', 'twitter:card': 'summary', 'twitter:title': title, 'twitter:description': description, 'twitter:image': 'https://sjmaths.com/assets/icons/icon-512x512.png' };
  for (const [key, value] of Object.entries(defaults)) {
    if (!meta(key).first().attr('content') || meta(key).length > 1 || (key === 'og:url' && meta(key).attr('content') !== expected) || (title !== p.title && /:title$/.test(key)) || (description !== p.description && /:description$/.test(key)) || (syncSocial && /:title$/.test(key) && meta(key).first().attr('content') !== title) || (syncSocial && /:description$/.test(key) && meta(key).first().attr('content') !== description)) values[key] = value;
  }
  if (!Object.keys(values).length) {
    if (source !== original) { if (!dry) fs.writeFileSync(path.join(ROOT, p.file), source); modified++; }
    continue;
  }
  const next = setMetadata(source, values);
  if (next !== original) { if (!dry) fs.writeFileSync(path.join(ROOT, p.file), next); modified++; }
}
console.log(JSON.stringify({ dryRun: dry, scope: scopes.join(',') || null, inspected: pages.length, modified, placeholdersNoindexed: placeholders }));
