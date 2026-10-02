import fs from 'node:fs';
import path from 'node:path';

const TRACKER_PATH = 'up-upper-primary-teacher/social-studies/index.html';
const html = fs.readFileSync(TRACKER_PATH, 'utf8');

const regex = /<details class="module-accordion" data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;

let sMatch;
const topicList = [];

while ((sMatch = regex.exec(html)) !== null) {
  const [_, secIdx, secTitleHi, secTitleEn, secBody] = sMatch;
  const topicRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;
  let tMatch;
  while ((tMatch = topicRegex.exec(secBody)) !== null) {
    const href = tMatch[2].startsWith('/') ? tMatch[2] : '/' + tMatch[2];
    const cleanHref = href.endsWith('/') ? href : href + '/';
    const slug = cleanHref.replace('/up-upper-primary-teacher/social-studies/', '').replace(/\//g, '');
    const numRaw = tMatch[3].trim().replace('#', '');
    const num = parseInt(numRaw, 10);

    topicList.push({
      chkId: tMatch[1],
      href: cleanHref,
      slug,
      num,
      numStr: `#${num}`,
      nameHi: tMatch[4].trim(),
      nameEn: tMatch[5].trim(),
      tag: tMatch[6].trim(),
      secIdx: parseInt(secIdx, 10),
      secTitleHi: secTitleHi.trim(),
      secTitleEn: secTitleEn.trim(),
    });
  }
}

console.log(`Total topics in Social Studies: ${topicList.length}`);
topicList.forEach(t => {
  console.log(`  Topic #${t.numStr.padEnd(5)} | Sec ${t.secIdx} | ${t.slug.padEnd(40)} | ${t.nameEn}`);
});
