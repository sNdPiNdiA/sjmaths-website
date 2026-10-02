import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const TRACKER_PATH = path.join(ROOT, 'up-upper-primary-teacher', 'mathematics', 'index.html');

function decodeHtml(html) {
  return String(html || '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function extractSyllabus() {
  if (!fs.existsSync(TRACKER_PATH)) {
    console.error(`Tracker file not found: ${TRACKER_PATH}`);
    return [];
  }
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
      const slug = cleanHref.replace('/up-upper-primary-teacher/mathematics/', '').replace(/\//g, '');
      const numRaw = tMatch[3].trim().replace('#', '');
      const num = parseInt(numRaw, 10);

      topicList.push({
        chkId: tMatch[1],
        href: cleanHref,
        slug,
        num,
        numStr: `#${num}`,
        nameHi: decodeHtml(tMatch[4].trim()),
        nameEn: decodeHtml(tMatch[5].trim().replace(/^\(|\)$/g, '')),
        tag: tMatch[6].trim(),
        secIdx: parseInt(secIdx, 10),
        secTitleHi: decodeHtml(secTitleHi.trim()),
        secTitleEn: decodeHtml(secTitleEn.trim()),
      });
    }
  }

  return topicList;
}

const topics = extractSyllabus();
console.log(`Extracted ${topics.length} Mathematics micro-topics from tracker:`);
const bySec = {};
topics.forEach(t => {
  bySec[t.secIdx] = bySec[t.secIdx] || { title: t.secTitleEn, list: [] };
  bySec[t.secIdx].list.push(t);
});

for (const [sec, data] of Object.entries(bySec)) {
  console.log(`\nSection ${sec}: ${data.title} (${data.list.length} topics)`);
  data.list.forEach(t => {
    console.log(`  Topic #${t.num}: ${t.nameEn} [${t.slug}] (${t.tag})`);
  });
}
