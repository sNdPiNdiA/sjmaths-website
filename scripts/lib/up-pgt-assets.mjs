import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/up-pgt-topic.css', import.meta.url);

export const upPgtCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upPgtStyleLink = '<link rel="stylesheet" href="/assets/css/up-pgt-topic.min.css?v=f6e2a830" data-up-pgt-style="topic">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeUpPgtStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(upPgtCss) ? upPgtStyleLink : tag;
  });
}

export function hydrateUpPgtStyles(html) {
  return html.replace(/<link\b[^>]*data-up-pgt-style="topic"[^>]*>/gi, () => {
    return `<style>\n${upPgtCss}\n</style>`;
  });
}

export function externalizeUpPgtAssets(html) {
  return externalizeUpPgtStyles(html);
}

export function hydrateUpPgtAssets(html) {
  return hydrateUpPgtStyles(html);
}
