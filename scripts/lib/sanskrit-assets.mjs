import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/sanskrit-topic.css', import.meta.url);

export const sanskritTopicCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const sanskritTopicStyleLink = '<link rel="stylesheet" href="/assets/css/sanskrit-topic.min.css?v=b485e100" data-study-guide-style="sanskrit">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeSanskritStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(sanskritTopicCss) ? sanskritTopicStyleLink : tag;
  });
}

export function hydrateSanskritStyles(html) {
  return html.replace(/<link\b[^>]*data-study-guide-style="sanskrit"[^>]*>/gi, () => {
    return `<style>\n${sanskritTopicCss}\n</style>`;
  });
}

export function externalizeSanskritAssets(html) {
  return externalizeSanskritStyles(html);
}

export function hydrateSanskritAssets(html) {
  return hydrateSanskritStyles(html);
}
