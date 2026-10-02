import fs from 'fs';

const html = fs.readFileSync('up-upper-primary-teacher/english/index.html', 'utf8');
const regex = /<a\s+[^>]*href=["']([^"']+)["'][^>]*>([\s\S]*?)<\/a>/gi;
let m;
const topics = [];
while ((m = regex.exec(html)) !== null) {
  const href = m[1];
  const text = m[2].replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
  if (href.includes('/english/') && href !== '/up-upper-primary-teacher/english/' && href !== '/up-upper-primary-teacher/' && !href.includes('mailto')) {
    topics.push({ href, text });
  }
}
console.log('Total topics listed in english/index.html:', topics.length);
topics.forEach((t, i) => console.log(`${i + 1}. [${t.href}] -> ${t.text}`));
