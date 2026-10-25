import fs from 'fs';

const html = fs.readFileSync('upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/index.html', 'utf8');
const m = html.match(/<script id="upsc-page-data"[^>]*>([\s\S]*?)<\/script>/);
if (m) {
  const d = JSON.parse(m[1]);
  console.log('topicId:', d.topicId);
  console.log('topicName:', d.topicName);
  console.log('tabs:', d.tabs);
  console.log('supportsMains:', d.supportsMains);
}

