import fs from 'node:fs';
import path from 'node:path';

function decodeHtml(html) {
  return String(html || '')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

function getTopicsForHub(hubPath, prefix) {
  if (!fs.existsSync(hubPath)) return [];
  const html = fs.readFileSync(hubPath, 'utf8');
  const secRegex = /<details class="module-accordion" data-sec-idx="([^"]+)"[\s\S]*?<h3 class="module-title">[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;
  let sMatch;
  const topicList = [];
  while ((sMatch = secRegex.exec(html)) !== null) {
    const [_, secIdx, secTitleHi, secTitleEn, secBody] = sMatch;
    const topicRegex = /<li class="topic-row">[\s\S]*?<input[^>]*id="([^"]+)"[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-hi">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>[\s\S]*?<span class="topic-tag">([^<]+)<\/span>/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(secBody)) !== null) {
      const href = tMatch[2].startsWith('/') ? tMatch[2] : '/' + tMatch[2];
      const cleanHref = href.endsWith('/') ? href : href + '/';
      const slug = cleanHref.replace(prefix, '').replace(/\//g, '');
      topicList.push({
        chkId: tMatch[1],
        href: cleanHref,
        slug,
        numStr: tMatch[3].trim(),
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

const sstTopics = getTopicsForHub('up-upper-primary-teacher/social-studies/index.html', '/up-upper-primary-teacher/social-studies/');
const sciTopics = getTopicsForHub('up-upper-primary-teacher/science/index.html', '/up-upper-primary-teacher/science/');
const gkTopics = getTopicsForHub('up-upper-primary-teacher/general-knowledge/index.html', '/up-upper-primary-teacher/general-knowledge/');

console.log('Social Studies Topics:', sstTopics.length);
console.log('Science Topics:', sciTopics.length);
console.log('General Knowledge Topics:', gkTopics.length);
console.log('Total Topics:', sstTopics.length + sciTopics.length + gkTopics.length);

// Also check existing index.html files for these topics
let sstExists = 0, sciExists = 0, gkExists = 0;
sstTopics.forEach(t => { if (fs.existsSync(path.join('up-upper-primary-teacher/social-studies', t.slug, 'index.html'))) sstExists++; });
sciTopics.forEach(t => { if (fs.existsSync(path.join('up-upper-primary-teacher/science', t.slug, 'index.html'))) sciExists++; });
gkTopics.forEach(t => { if (fs.existsSync(path.join('up-upper-primary-teacher/general-knowledge', t.slug, 'index.html'))) gkExists++; });

const gkSec5 = gkTopics.filter(t => t.secIdx === 5);
console.log('GK Sec 5 Topics Count:', gkSec5.length);
gkSec5.forEach(t => {
  const p = path.join('up-upper-primary-teacher/general-knowledge', t.slug, 'index.html');
  const exists = fs.existsSync(p);
  const content = exists ? fs.readFileSync(p, 'utf8') : '';
  const isComingSoon = content.includes('coming-soon-card') || content.includes('Coming Soon');
  console.log(`- ${t.slug} (exists: ${exists}, comingSoon: ${isComingSoon})`);
});
