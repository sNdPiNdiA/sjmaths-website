const fs = require('fs');
const path = require('path');
const { ROOT, siteFiles, parse, setMetadata, editElement, applyEdits, compact } = require('./seo-html.cjs');
let physics = 0, titles = 0;
for (const file of siteFiles().filter(file => file.endsWith('.html'))) {
  if (!file.startsWith('class-12-physics/') && !/^class-9-maths\/ncert-exercise-practice\/chapter-[34]-/.test(file)) continue;
  const target = path.join(ROOT, file);
  const original = fs.readFileSync(target, 'utf8');
  let source = original;
  if (file.startsWith('class-12-physics/')) {
    // The truncated inline onload swallows the following CSS/schema tags.
    // The existing class12-physics engine already renders KaTeX on DOM ready.
    source = source.replace(/^<script defer src="(https:\/\/cdn\.jsdelivr\.net\/npm\/katex@0\.16\.9\/dist\/contrib\/auto-render\.min\.js)" onload="[^\r\n]*$/gm, '<script defer src="$1"></script>');
    if (source !== original) physics++;
  } else {
    const $ = parse(source);
    const chapter = $('body').attr('data-chaptername');
    const heading = compact($('h1').first().text());
    if (!['The World of Numbers', 'Algebraic Identities'].includes(chapter)) continue;
    if (!$('title').text().includes(chapter)) {
      const title = `Class 9 ${chapter} — ${heading} | SJMaths`;
      const description = `Practice ${chapter} with ${heading.toLowerCase()} for Class 9 Maths. Read the questions and worked solutions on SJMaths.`;
      source = setMetadata(source, { title, description, 'og:title': title, 'og:description': description, 'twitter:title': title, 'twitter:description': description });
      const doc = parse(source), edits = [];
      doc('script[type="application/ld+json"]').each((_, el) => {
        const data = JSON.parse(doc(el).text());
        for (const node of data['@graph'] || [data]) {
          if (['LearningResource', 'Article', 'WebPage'].includes(node['@type'])) {
            if (node.name) node.name = title;
            if (node.headline) node.headline = title;
            if (node.description) node.description = description;
          }
        }
        edits.push(editElement(el, `<script type="application/ld+json">${JSON.stringify(data, null, 2).replace(/</g, '\\u003c')}</script>`));
      });
      source = applyEdits(source, edits);
      titles++;
    }
  }
  if (source !== original) fs.writeFileSync(target, source);
}
console.log(JSON.stringify({ physics, titles }));
