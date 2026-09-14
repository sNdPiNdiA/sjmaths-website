const fs = require('fs');
const path = require('path');
const policy = require('./seo-policy.cjs');
const { ROOT, siteFiles, parse, compact, escapeHtml: esc, editElement, applyEdits, setMetadata } = require('./seo-html.cjs');
const files = siteFiles().filter(policy.isManagedHtmlPath);
const titleGroups = new Map(), descriptionGroups = new Map();
const rows = [];
for (const file of files) {
  const source = fs.readFileSync(path.join(ROOT, file), 'utf8');
  if (policy.hasNoindex(source) || policy.hasRedirect(source)) continue;
  const $ = parse(source.slice(0, source.indexOf('</head>') + 7));
  const title = compact($('title').text());
  const description = $('meta[name="description"]').first().attr('content') || '';
  rows.push({ file, title, description });
  for (const [map, value] of [[titleGroups, title], [descriptionGroups, description]]) map.set(value, (map.get(value) || 0) + 1);
}
const stats = { files: 0, headings: 0, duplicateIds: 0, metadata: 0, embeddedStubs: 0 };
for (const row of rows) {
  const original = fs.readFileSync(path.join(ROOT, row.file), 'utf8');
  let source = original;
  let $ = parse(source);
  const embedded = $('#upsc-page-data').text();
  if (embedded && /Content under preparation.*check back soon for comprehensive notes/.test(embedded)) {
    const data = JSON.parse(embedded);
    if (data.concepts?.sections?.length === 1 && !data.practice && !data.pyqs && !data.test) {
      source = setMetadata(source, { robots: 'noindex, follow' });
      fs.writeFileSync(path.join(ROOT, row.file), source); stats.embeddedStubs++; stats.files++; continue;
    }
  }
  const edits = [];
  if ($('h1').length > 1 && row.file.startsWith('class-9-advanced-maths/')) {
    $('h1').slice(1).each((_, el) => {
      const raw = source.slice(el.sourceCodeLocation.startOffset, el.sourceCodeLocation.endOffset);
      edits.push(editElement(el, raw.replace(/^<h1\b/, '<h2').replace(/<\/h1>$/, '</h2>'))); stats.headings++;
    });
  }
  if (!$('h1').length) {
    const title = row.title.replace(/\s*\|\s*SJMaths$/i, '');
    const badge = $('.reader-title-badge').first();
    const container = $('.sj-page-content, .hero-section, main, .sj-container, .container').first();
    if (badge.length) {
      const el = badge[0]; const raw = source.slice(el.sourceCodeLocation.startOffset, el.sourceCodeLocation.endOffset);
      edits.push(editElement(el, raw.replace(/^<div\b/, '<h1').replace(/<\/div>$/, '</h1>')));
    } else if (container.length) {
      const at = container[0].sourceCodeLocation.startTag.endOffset;
      edits.push({ start: at, end: at, text: `\n<h1 class="seo-page-heading">${esc(title)}</h1>\n` });
    } else {
      const body = source.match(/<body\b[^>]*>/i);
      if (body) { const at = body.index + body[0].length; edits.push({ start: at, end: at, text: `\n<h1 class="seo-page-heading">${esc(title)}</h1>\n` }); }
    }
    stats.headings++;
  }
  if (edits.length) source = applyEdits(source, edits);
  // Resolve remaining duplicate IDs one at a time so nested source offsets stay valid.
  for (let pass = 0; pass < 100; pass++) {
    if (pass > 0 || edits.length) $ = parse(source);
    const seen = new Map(); let duplicate;
    $('[id]').each((_, el) => { const id = $(el).attr('id'); if (seen.has(id) && !duplicate) duplicate = { id, el, first: seen.get(id) }; else seen.set(id, el); });
    if (!duplicate) break;
    const { id, el, first } = duplicate;
    const raw = node => source.slice(node.sourceCodeLocation.startOffset, node.sourceCodeLocation.endOffset);
    if (raw(el) === raw(first) && (!$(el).closest('.question-card').length || $(el).hasClass('question-card') || el.tagName === 'script')) {
      source = applyEdits(source, [editElement(el, '')]);
    } else {
      let n = 2; while ($(`[id="${id}-${n}"]`).length) n++;
      const nextId = `${id}-${n}`;
      const loc = el.sourceCodeLocation.startTag;
      const editList = [{ start: loc.startOffset, end: loc.endOffset, text: source.slice(loc.startOffset, loc.endOffset).replace(/\bid=(["'])[^"']*\1/, `id="${nextId}"`) }];
      const card = $(el).closest('.question-card');
      if (card.length) card.find('[onclick], [aria-controls]').each((_, button) => {
        const at = button.sourceCodeLocation.startTag;
        const before = source.slice(at.startOffset, at.endOffset);
        const after = before.replace(`'${id}'`, `'${nextId}'`).replace(`aria-controls="${id}"`, `aria-controls="${nextId}"`);
        if (after !== before) editList.push({ start: at.startOffset, end: at.endOffset, text: after });
      });
      source = applyEdits(source, editList);
    }
    stats.duplicateIds++;
  }
  if (titleGroups.get(row.title) > 1 || descriptionGroups.get(row.description) > 1) {
    const parts = row.file.split('/');
    const chapter = parts.find(p => /^chapter-\d/.test(p));
    let context = (chapter || parts.at(-2) || parts[0]).replace(/-/g, ' ').replace(/\b[a-z]/g, c => c.toUpperCase());
    const shortTitle = row.title.replace(/\s*\|\s*SJMaths$/i, '');
    if (row.file === 'ahc-ro-aro/index.html') context = 'Preparation Hub';
    else if (row.file === 'ahc-ro-aro/syllabus/index.html') context = 'Syllabus';
    else if (!chapter && /\/index\.html$/.test(row.file)) context = parts.slice(0, -2).slice(-2).map(p => p.replace(/-/g, ' ')).join(' / ').replace(/\b[a-z]/g, c => c.toUpperCase());
    const title = `${shortTitle} — ${context} | SJMaths`;
    const description = `${shortTitle} in ${context}. Read the study material and revision resources provided on this SJMaths page.`;
    source = setMetadata(source, { title, description, 'og:title': title, 'og:description': description, 'twitter:title': title, 'twitter:description': description });
    stats.metadata++;
  }
  if (source !== original) { fs.writeFileSync(path.join(ROOT, row.file), source); stats.files++; }
}
console.log(JSON.stringify(stats));
