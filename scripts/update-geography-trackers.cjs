const fs = require('fs');

const config = JSON.parse(fs.readFileSync('scripts/geography_consolidation_config.json', 'utf8'));

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

// Parse topics: <div class="topic" data-key="...">...</div>
// We can use a regex that matches each topic div
// In PGT: <div class="topic" data-key="..."><label class="check">...</label><div class="topic-copy"><a class="topic-link" href="...">...</a>...</div><a class="open-topic" ...>→</a></div>
const pgtTopicRegex = /<div class="topic" data-key="([^"]+)"[^>]*>([\s\S]*?)<\/div>/g;

// To avoid corrupting nested divs, let's extract by splitting on `<div class="topic"`
function processPgtHtml(html) {
  // Let's replace each cluster in PGT
  for (const group of config) {
    // Find if any sources are present in PGT
    const presentSources = group.sources.filter(s => html.includes(`href="${s}"`));
    if (presentSources.length > 0) {
      console.log(`PGT has ${presentSources.length} sources for target ${group.target}: ${presentSources.join(', ')}`);

      // We want to replace the first occurrence with the unified topic, and remove the other occurrences
      let isFirst = true;
      for (const src of presentSources) {
        const srcKey = src.replace(/^\/geography\//, '').replace(/\/$/, '');
        const targetKey = group.target.replace(/^\/geography\//, '').replace(/\/$/, '');

        // Pattern for this topic in PGT
        // <div class="topic" data-key="srcKey" ...>...</div>
        // Notice each topic in PGT ends with </div> right after <a class="open-topic"...>→</a>
        const pattern = new RegExp(`<div class="topic" data-key="${srcKey.replace(/\//g, '\\/')}"[\\s\\S]*?<a class="open-topic"[^>]*>→<\\/a>\\s*<\\/div>`, 'g');

        html = html.replace(pattern, (match) => {
          if (isFirst) {
            isFirst = false;
            // Return updated unified topic block
            let unifiedBlock = match;
            // update data-key
            unifiedBlock = unifiedBlock.replace(`data-key="${srcKey}"`, `data-key="${targetKey}"`);
            // update hrefs
            unifiedBlock = unifiedBlock.replace(new RegExp(`href="${src}"`, 'g'), `href="${group.target}"`);
            // update topic title in <a class="topic-link"...>...</a>
            unifiedBlock = unifiedBlock.replace(/<a class="topic-link"[^>]*>[\s\S]*?<\/a>/, `<a class="topic-link" href="${group.target}">${group.title}</a>`);
            // update topic path
            unifiedBlock = unifiedBlock.replace(/<span class="topic-path">[^<]*<\/span>/, `<span class="topic-path">${group.target}</span>`);
            // update aria-label
            unifiedBlock = unifiedBlock.replace(/aria-label="[^"]*"/g, `aria-label="${group.title}"`);
            return unifiedBlock;
          } else {
            // Remove subsequent merged topic blocks
            return '';
          }
        });
      }
    }
  }

  // Recalculate section topic counts
  const sectionCardRegex = /<article class="section-card" id="([^"]+)"[\s\S]*?<\/article>/g;
  let secMatch;
  let totalTopics = 0;
  while ((secMatch = sectionCardRegex.exec(html)) !== null) {
    const secId = secMatch[1];
    const secContent = secMatch[0];
    const count = (secContent.match(/<div class="topic"/g) || []).length;
    totalTopics += count;

    // Update <small><span data-done="secId">0</span> / 12</small>
    const countRegex = new RegExp(`(<span data-done="${secId}">\\d+<\\/span> \\/ )\\d+`, 'g');
    html = html.replace(countRegex, `$1${count}`);
  }

  // Update total stat counters
  html = html.replace(/(<span id="stat-total">)\d+(<\/span>)/g, `$1${totalTopics}$2`);
  html = html.replace(/(<strong>)\d+(<\/strong>\s*<span>Total Topics<\/span>)/g, `$1${totalTopics}$2`);
  html = html.replace(/>\d+\s+Topics\s*·/g, `>${totalTopics} Topics ·`);

  return { html, totalTopics };
}

const pgtResult = processPgtHtml(pgtHtml);
fs.writeFileSync('up-pgt-geography/index.html', pgtResult.html, 'utf8');
console.log(`Saved up-pgt-geography/index.html. New total topics: ${pgtResult.totalTopics}`);

// ----------------------------------------------------
// 2. UPDATE UP TGT SOCIAL SCIENCE (up-tgt-social-science/index.html)
// ----------------------------------------------------
console.log('\n--- Updating UP TGT Social Science ---');
let tgtHtml = fs.readFileSync('up-tgt-social-science/index.html', 'utf8');

function processTgtHtml(html) {
  for (const group of config) {
    const presentSources = group.sources.filter(s => html.includes(`href="${s}"`));
    if (presentSources.length > 0) {
      console.log(`TGT has ${presentSources.length} sources for target ${group.target}: ${presentSources.join(', ')}`);

      let isFirst = true;
      for (const src of presentSources) {
        const srcKey = src.replace(/^\//, '').replace(/\/$/, ''); // in TGT data-key starts with 'geography/...'
        const targetKey = group.target.replace(/^\//, '').replace(/\/$/, '');

        // Pattern for this topic in TGT
        const pattern = new RegExp(`<div class="topic" data-key="${srcKey.replace(/\//g, '\\/')}"[\\s\\S]*?<a class="open-topic"[^>]*>→<\\/a>\\s*<\\/div>`, 'g');

        html = html.replace(pattern, (match) => {
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

  // Recalculate total topics in TGT
  const totalTopics = (html.match(/<div class="topic"/g) || []).length;
  const geoTopics = (html.match(/data-key="geography\/[^"]*"/g) || []).length;

  html = html.replace(/(<span id="stat-total">)\d+(<\/span>)/g, `$1${totalTopics}$2`);
  html = html.replace(/(<strong>)\d+(<\/strong>\s*<span>Total Topics<\/span>)/g, `$1${totalTopics}$2`);

  return { html, totalTopics, geoTopics };
}

const tgtResult = processTgtHtml(tgtHtml);
fs.writeFileSync('up-tgt-social-science/index.html', tgtResult.html, 'utf8');
console.log(`Saved up-tgt-social-science/index.html. New total topics: ${tgtResult.totalTopics} (Geography: ${tgtResult.geoTopics})`);
