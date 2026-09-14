// Repair fragment navigation without fabricating sections that do not exist.
const fs = require('fs');
const path = require('path');
const { ROOT, siteFiles } = require('./seo-html.cjs');

let changedFiles = 0;
let corrected = 0;
let disabled = 0;
for (const file of siteFiles().filter(file => file.endsWith('.html'))) {
  const target = path.join(ROOT, file);
  const original = fs.readFileSync(target, 'utf8');
  let source = original;
  const ids = new Set([...source.matchAll(/\bid=["']([^"']+)["']/gi)].map(match => match[1]));

  if (/href=["']#top["']/i.test(source) && !ids.has('top')) {
    source = source.replace(/<body\b(?![^>]*\bid=)/i, '<body id="top"');
    ids.add('top');
    corrected++;
  }

  source = source.replace(/<a\b[^>]*\bhref=["']#([^"']+)["'][^>]*>/gi, tag => {
    const fragment = tag.match(/\bhref=["']#([^"']+)["']/i)?.[1];
    if (!fragment || ids.has(fragment)) return tag;
    const tab = tag.match(/\bdata-tab=["']([^"']+)["']/i)?.[1];
    const replacement = tab && ids.has(tab) ? tab : fragment === 'practice' && ids.has('section-practice') ? 'section-practice' : '';
    if (replacement) {
      corrected++;
      return tag.replace(/\bhref=["']#[^"']+["']/i, `href="#${replacement}"`);
    }
    disabled++;
    return tag
      .replace(/\s*href=["']#[^"']+["']/i, '')
      .replace(/^<a\b/i, '<a aria-disabled="true" title="This section is not available on this page"');
  });

  if (source !== original) {
    fs.writeFileSync(target, source);
    changedFiles++;
  }
}
console.log(JSON.stringify({ changedFiles, correctedFragments: corrected, disabledUnavailableFragments: disabled }));
