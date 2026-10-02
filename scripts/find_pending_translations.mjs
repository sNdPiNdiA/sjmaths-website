import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const status = JSON.parse(fs.readFileSync(path.join(ROOT, 'content-generation-status-upper-primary-translation.json'), 'utf8'));

function getTopics(hubRelativePath, prefix, secKey) {
  const html = fs.readFileSync(path.join(ROOT, hubRelativePath), 'utf8');
  const secRegex = /<details class="module-accordion"[\s\S]*?<ul class="module-list">([\s\S]*?)<\/ul>/g;
  let sMatch;
  const list = [];
  while ((sMatch = secRegex.exec(html)) !== null) {
    const topicRegex = /<li class="topic-row">[\s\S]*?<a href="([^"]+)"/g;
    let tMatch;
    while ((tMatch = topicRegex.exec(sMatch[1])) !== null) {
      let href = tMatch[1].startsWith('/') ? tMatch[1] : '/' + tMatch[1];
      let cleanHref = href.endsWith('/') ? href : href + '/';
      let slug = cleanHref.replace(prefix, '').replace(/\//g, '');
      list.push({ secKey, slug });
    }
  }
  return list;
}

const all = [
  ...getTopics('up-upper-primary-teacher/social-studies/index.html', '/up-upper-primary-teacher/social-studies/', 'social-studies'),
  ...getTopics('up-upper-primary-teacher/science/index.html', '/up-upper-primary-teacher/science/', 'science'),
  ...getTopics('up-upper-primary-teacher/general-knowledge/index.html', '/up-upper-primary-teacher/general-knowledge/', 'general-knowledge')
];

const remaining = all.filter(t => !status[`${t.secKey}/${t.slug}`] || status[`${t.secKey}/${t.slug}`].status !== 'completed');
console.log('REMAINING COUNT:', remaining.length);
console.log(JSON.stringify(remaining, null, 2));
