const fs = require('fs');

const config = JSON.parse(fs.readFileSync('scripts/geography_denesting_config.json', 'utf8'));

// Build lookup maps
const sourceToGroup = new Map();
for (const group of config) {
  for (const src of group.sources) {
    sourceToGroup.set(src, group);
  }
}

// ----------------------------------------------------
// 1. UPDATE UP PGT GEOGRAPHY (up-pgt-geography/index.html)
// ----------------------------------------------------
console.log('--- Updating UP PGT Geography ---');
let pgtHtml = fs.readFileSync('up-pgt-geography/index.html', 'utf8');

for (const group of config) {
  const presentSources = group.sources.filter(s => pgtHtml.includes(`href="${s}"`));
  if (presentSources.length > 0) {
    console.log(`PGT has ${presentSources.length} sources for target ${group.target}`);
    let isFirst = true;
    for (const src of presentSources) {
      const srcKey = src.replace(/^\/geography\//, '').replace(/\/$/, '');
      const targetKey = group.target.replace(/^\/geography\//, '').replace(/\/$/, '');

      const pattern = new RegExp(`<div class="topic" data-key="${srcKey.replace(/\//g, '\\/')}"[\\s\\S]*?<a class="open-topic"[^>]*>→<\\/a>\\s*<\\/div>`, 'g');

      pgtHtml = pgtHtml.replace(pattern, (match) => {
        if (isFirst) {
          isFirst = false;
          let unifiedBlock = match;
          unifiedBlock = unifiedBlock.replace(`data-key="${srcKey}"`, `data-key="${targetKey}"`);
          unifiedBlock = unifiedBlock.replace(new RegExp(`href="${src}"`, 'g'), `href="${group.target}"`);
          unifiedBlock = unifiedBlock.replace(/<a class="topic-link"[^>]*>[\s\S]*?<\/a>/, `<a class="topic-link" href="${group.target}">${group.title}</a>`);
          unifiedBlock = unifiedBlock.replace(/<span class="topic-path">[^<]*<\/span>/, `<span class="topic-path">${group.target}</span>`);
          unifiedBlock = unifiedBlock.replace(/aria-label="[^"]*"/g, `aria-label="${group.title}"`);
          return unifiedBlock;
        } else {
          return '';
        }
      });
    }
  }
}

// Recalculate section topic counts in PGT
const sectionCardRegex = /<article class="section-card" id="([^"]+)"[\s\S]*?<\/article>/g;
let secMatch;
let totalPgtTopics = 0;
while ((secMatch = sectionCardRegex.exec(pgtHtml)) !== null) {
  const secId = secMatch[1];
  const secContent = secMatch[0];
  const count = (secContent.match(/<div class="topic"/g) || []).length;
  totalPgtTopics += count;

  const countRegex = new RegExp(`(<span data-done="${secId}">\\d+<\\/span> \\/ )\\d+`, 'g');
  pgtHtml = pgtHtml.replace(countRegex, `$1${count}`);
}

pgtHtml = pgtHtml.replace(/(<span id="stat-total">)\d+(<\/span>)/g, `$1${totalPgtTopics}$2`);
pgtHtml = pgtHtml.replace(/(<strong>)\d+(<\/strong>\s*<span>Total Topics<\/span>)/g, `$1${totalPgtTopics}$2`);
pgtHtml = pgtHtml.replace(/>\d+\s+Topics\s*·/g, `>${totalPgtTopics} Topics ·`);

fs.writeFileSync('up-pgt-geography/index.html', pgtHtml, 'utf8');
console.log(`Saved up-pgt-geography/index.html. New total topics: ${totalPgtTopics}`);

// ----------------------------------------------------
// 2. UPDATE UP TGT SOCIAL SCIENCE (up-tgt-social-science/index.html)
// ----------------------------------------------------
console.log('\n--- Updating UP TGT Social Science ---');
let tgtHtml = fs.readFileSync('up-tgt-social-science/index.html', 'utf8');

for (const group of config) {
  const presentSources = group.sources.filter(s => tgtHtml.includes(`href="${s}"`));
  if (presentSources.length > 0) {
    console.log(`TGT has ${presentSources.length} sources for target ${group.target}`);
    let isFirst = true;
    for (const src of presentSources) {
      const srcKey = src.replace(/^\//, '').replace(/\/$/, '');
      const targetKey = group.target.replace(/^\//, '').replace(/\/$/, '');

      const pattern = new RegExp(`<div class="topic" data-key="${srcKey.replace(/\//g, '\\/')}"[\\s\\S]*?<a class="open-topic"[^>]*>→<\\/a>\\s*<\\/div>`, 'g');

      tgtHtml = tgtHtml.replace(pattern, (match) => {
        if (isFirst) {
          isFirst = false;
          let unifiedBlock = match;
          unifiedBlock = unifiedBlock.replace(`data-key="${srcKey}"`, `data-key="${targetKey}"`);
          unifiedBlock = unifiedBlock.replace(new RegExp(`href="${src}"`, 'g'), `href="${group.target}"`);
          unifiedBlock = unifiedBlock.replace(/<a class="topic-link"[^>]*>[\s\S]*?<\/a>/, `<a class="topic-link" href="${group.target}">${group.title}</a>`);
          unifiedBlock = unifiedBlock.replace(/<span class="topic-path">[^<]*<\/span>/, `<span class="topic-path">${group.target}</span>`);
          unifiedBlock = unifiedBlock.replace(/aria-label="[^"]*"/g, `aria-label="${group.title}"`);
          return unifiedBlock;
        } else {
          return '';
        }
      });
    }
  }
}

const totalTgtTopics = (tgtHtml.match(/<div class="topic"/g) || []).length;
const tgtGeoTopics = (tgtHtml.match(/data-key="geography\/[^"]*"/g) || []).length;

tgtHtml = tgtHtml.replace(/(<span id="stat-total">)\d+(<\/span>)/g, `$1${totalTgtTopics}$2`);
tgtHtml = tgtHtml.replace(/(<strong>)\d+(<\/strong>\s*<span>Total Topics<\/span>)/g, `$1${totalTgtTopics}$2`);

fs.writeFileSync('up-tgt-social-science/index.html', tgtHtml, 'utf8');
console.log(`Saved up-tgt-social-science/index.html. New total: ${totalTgtTopics} (Geography: ${tgtGeoTopics})`);
