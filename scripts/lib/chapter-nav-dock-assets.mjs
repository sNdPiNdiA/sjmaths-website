import fs from 'node:fs';
import crypto from 'node:crypto';

const cssUrl = new URL('../../assets/css/chapter-nav-dock.css', import.meta.url);

export const chapterNavDockCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const chapterNavDockStyleLink = '<link rel="stylesheet" href="/assets/css/chapter-nav-dock.min.css?v=1cdd6ded" data-maths-style="nav-dock">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
const targetHash = '40d1a612de5c';

export function externalizeChapterNavDockStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    const hash = crypto.createHash('sha256').update(normalize(css)).digest('hex').slice(0, 12);
    if (hash === targetHash) return chapterNavDockStyleLink;
    return tag;
  });
}

export function hydrateChapterNavDockStyles(html) {
  return html.replace(
    /<link\b[^>]*data-maths-style="nav-dock"[^>]*>/gi,
    () => `<style>\n${chapterNavDockCss}\n</style>`
  );
}

export function externalizeChapterNavDockAssets(html) {
  return externalizeChapterNavDockStyles(html);
}

export function hydrateChapterNavDockAssets(html) {
  return hydrateChapterNavDockStyles(html);
}
