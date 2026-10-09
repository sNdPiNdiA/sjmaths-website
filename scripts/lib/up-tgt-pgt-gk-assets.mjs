import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/up-tgt-pgt-gk-topic.css', import.meta.url);

export const upTgtPgtGkCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upTgtPgtGkStyleLink = '<link rel="stylesheet" href="/assets/css/up-tgt-pgt-gk-topic.min.css?v=8fb8e4c5" data-up-gk-style="topic">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeUpTgtPgtGkStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(upTgtPgtGkCss) ? upTgtPgtGkStyleLink : tag;
  });
}

export function hydrateUpTgtPgtGkStyles(html) {
  return html.replace(/<link\b[^>]*data-up-gk-style="topic"[^>]*>/gi, () => {
    return `<style>${upTgtPgtGkCss}</style>`;
  });
}

export function externalizeUpTgtPgtGkAssets(html) {
  return externalizeUpTgtPgtGkStyles(html);
}

export function hydrateUpTgtPgtGkAssets(html) {
  return hydrateUpTgtPgtGkStyles(html);
}
