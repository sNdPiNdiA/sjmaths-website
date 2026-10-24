#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const subjects = ['ancient-history', 'medieval-history', 'modern-history', 'art-and-culture', 'polity', 'economy'];
let linked = 0;

for (const subj of subjects) {
  const subjDir = path.join(ROOT, 'upsc', subj);
  if (!fs.existsSync(subjDir)) continue;

  function walk(dir) {
    for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, item.name);
      if (item.isDirectory()) {
        walk(full);
      } else if (item.name === 'index.html') {
        const tabsPj = path.join(path.dirname(full), 'tabs', 'practice.json');
        if (fs.existsSync(tabsPj)) {
          try {
            const pj = JSON.parse(fs.readFileSync(tabsPj, 'utf8'));
            const html = fs.readFileSync(full, 'utf8');
            const pageMatch = html.match(/<script id="upsc-page-data" type="application\/json">([\s\S]*?)<\/script>/);
            if (pageMatch) {
              const d = JSON.parse(pageMatch[1]);
              const hasInPage = d.practice && d.practice.levels && Object.values(d.practice.levels).some(l => Array.isArray(l) && l.length > 0);
              const hasInTabs = pj.levels && Object.values(pj.levels).some(l => Array.isArray(l) && l.length > 0);
              if (!hasInPage && hasInTabs) {
                linked++;
                d.practice = { levels: pj.levels };
                if (Array.isArray(d.tabs) && !d.tabs.includes('practice')) d.tabs.push('practice');
                const newHtml = html.replace(pageMatch[0], `<script id="upsc-page-data" type="application/json">${JSON.stringify(d)}</script>`);
                fs.writeFileSync(full, newHtml, 'utf8');
              }
            }
          } catch (e) {
            console.error('Error on', full, e.message);
          }
        }
      }
    }
  }
  walk(subjDir);
}
console.log(`Successfully linked existing tabs/practice.json to index.html for ${linked} topics.`);

