import fs from 'fs';
import path from 'path';

const html = fs.readFileSync('up-upper-primary-teacher/social-studies/index.html', 'utf8');
const status = JSON.parse(fs.readFileSync('content-generation-status-upper-primary-social-studies.json', 'utf8'));

const topicRegex = /<li class="topic-row">[\s\S]*?<a href="([^"]+)"[\s\S]*?<span class="topic-num">([^<]+)<\/span>[\s\S]*?<span class="lang-en">([^<]+)<\/span>/g;

let m;
const report = [];
while ((m = topicRegex.exec(html)) !== null) {
  const href = m[1].replace('/up-upper-primary-teacher/social-studies/', '').replace(/\//g, '');
  const num = m[2].trim();
  const title = m[3].trim();
  const filePath = path.join('up-upper-primary-teacher/social-studies', href, 'index.html');
  const exists = fs.existsSync(filePath);
  const sizeKb = exists ? (fs.statSync(filePath).size / 1024).toFixed(1) : 0;
  const recorded = status[href]?.fileSizeKb || 'none';
  const completed = status[href]?.completed || false;
  report.push({ num, slug: href, title: title.slice(0, 35), exists, sizeKb: Number(sizeKb), statusKb: recorded, completed });
}

console.log('Total Topics in Tracker:', report.length);
console.log('Fully Generated (>70KB):', report.filter(r => r.sizeKb >= 70).length);
console.log('Legacy/Placeholder (<70KB):', report.filter(r => r.sizeKb < 70).length);
console.log('\nBreakdown of all 48 topics:');
console.table(report);
