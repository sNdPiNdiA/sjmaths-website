import fs from 'fs';
import path from 'path';

const html = fs.readFileSync('up-upper-primary-teacher/general-knowledge/index.html', 'utf8');

const secRegex = /<details class="module-accordion" data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;

let sMatch;
const allTopics = [];
while ((sMatch = secRegex.exec(html)) !== null) {
  const [_, secIdx, secTitleHi, secTitleEn, secBody] = sMatch;
  const tRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;
  let tMatch;
  let count = 0;
  while ((tMatch = tRegex.exec(secBody)) !== null) {
    const rawHref = tMatch[2];
    const cleanHref = rawHref.startsWith('/') ? rawHref : '/' + rawHref;
    const slug = cleanHref.replace('/up-upper-primary-teacher/general-knowledge/', '').replace(/\//g, '');
    const targetPath = path.join('up-upper-primary-teacher/general-knowledge', slug, 'index.html');
    const exists = fs.existsSync(targetPath);
    const sizeKb = exists ? (fs.statSync(targetPath).size / 1024).toFixed(1) : 0;

    allTopics.push({
      secIdx: parseInt(secIdx, 10),
      secTitleEn: secTitleEn.trim(),
      secTitleHi: secTitleHi.trim(),
      chkId: tMatch[1],
      href: cleanHref,
      slug,
      num: tMatch[3].trim(),
      nameHi: tMatch[4].trim(),
      nameEn: tMatch[5].trim(),
      tag: tMatch[6].trim(),
      exists,
      sizeKb: Number(sizeKb)
    });
    count++;
  }
  console.log(`Module ${secIdx}: ${secTitleEn.trim()} -> ${count} topics`);
}

console.log(`\nTotal extracted topics: ${allTopics.length}`);
console.log('Fully Generated (>70KB):', allTopics.filter(t => t.sizeKb >= 70).length);
console.log('Needs Generation (<70KB):', allTopics.filter(t => t.sizeKb < 70).length);

console.log('\nSample topics:');
console.table(allTopics.slice(0, 15).map(t => ({
  sec: t.secIdx,
  num: t.num,
  slug: t.slug,
  sizeKb: t.sizeKb,
  nameEn: t.nameEn.slice(0, 35)
})));
