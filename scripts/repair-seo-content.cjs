// Source-preserving repairs for verified repeated markup and embedded guide content.
const fs = require('fs');
const path = require('path');
const { ROOT, siteFiles, parse, applyEdits, editElement, escapeHtml: esc } = require('./seo-html.cjs');
const stats = { files: 0, duplicatePhysicsBlocks: 0, duplicateQuestionCards: 0, guideIds: 0, staticGuides: 0 };
for (const file of siteFiles().filter(f => /^(class-12-physics|class-10-maths|upsc|ahc-ro-aro|ssc-cgl)\//.test(f) && f.endsWith('.html'))) {
  const original = fs.readFileSync(path.join(ROOT, file), 'utf8');
  let source = original;
  let $ = parse(source);
  let edits = [];
  const raw = el => source.slice(el.sourceCodeLocation.startOffset, el.sourceCodeLocation.endOffset);
  if (file.startsWith('class-12-physics/')) {
    const seen = new Set();
    $('body > .app, body > nav, body > script, body > link').each((_, el) => {
      const html = raw(el);
      if (seen.has(html)) { edits.push(editElement(el, '')); stats.duplicatePhysicsBlocks++; }
      else seen.add(html);
    });
  }
  if (file.startsWith('class-10-maths/previous-year-questions/')) {
    const seen = new Set();
    $('.question-card[id]').each((_, el) => {
      const html = raw(el);
      if (seen.has(html)) { edits.push(editElement(el, '')); stats.duplicateQuestionCards++; }
      else seen.add(html);
    });
  }
  if (edits.length) { source = applyEdits(source, edits); $ = parse(source); edits = []; }
  if (/competitive-exam-guide(?:\.min)?\.js/.test(source)) {
    // Keep the existing engine's target contract while giving Hindi targets unique IDs.
    const ids = new Set();
    $('[id]').each((_, el) => {
      const id = $(el).attr('id');
      if (ids.has(id) && $(el).closest('.lang-hi').length) {
        const tag = source.slice(el.sourceCodeLocation.startTag.startOffset, el.sourceCodeLocation.startTag.endOffset);
        edits.push({ start: el.sourceCodeLocation.startTag.startOffset, end: el.sourceCodeLocation.startTag.endOffset,
          text: tag.replace(/\bid=(["'])[^"']*\1/, `id="${esc(id)}-hi" data-guide-id="${esc(id)}"`) });
        stats.guideIds++;
      }
      ids.add(id);
    });
    // Put the authored hero and notes directly in HTML. JS enhances these same targets.
    for (const lang of ['en', 'hi']) {
      const json = $(`#embedded-study-guide-data${lang === 'hi' ? '-hi' : ''}`).first().text();
      if (!json) continue;
      let data;
      try { data = JSON.parse(json); } catch { continue; }
      const scope = $(`.lang-${lang}`);
      const target = scope.length ? scope.find('#deep-dive-section, [data-guide-id="deep-dive-section"]').first() : (lang === 'en' ? $('#deep-dive-section').first() : $([]));
      if (target.length && !target.html().trim() && data.deepDive?.sections?.length) {
        const html = `<h2 class="card-title">${data.deepDive.title || 'Study Notes'}</h2>${data.deepDive.description ? `<p>${data.deepDive.description}</p>` : ''}<div class="study-notes-content">${data.deepDive.sections.map(sec => `<section class="study-section"><h3>${sec.title}</h3><div class="section-content">${sec.content}</div></section>`).join('')}</div>`;
        const loc = target[0].sourceCodeLocation;
        edits.push({ start: loc.startTag.endOffset, end: loc.endTag.startOffset, text: html });
        stats.staticGuides++;
      }
      if (lang === 'en' && data.hero) {
        const hero = $('.hero-section').first();
        if (hero.length && !hero.html().trim()) {
          const loc = hero[0].sourceCodeLocation;
          edits.push({ start: loc.startTag.endOffset, end: loc.endTag.startOffset, text: `<div class="hero-copy"><h1>${data.hero.title}</h1><p>${data.hero.description || ''}</p></div>` });
        }
      }
    }
  }
  if (edits.length) source = applyEdits(source, edits);
  if (source !== original) { fs.writeFileSync(path.join(ROOT, file), source); stats.files++; }
}
console.log(JSON.stringify(stats));
