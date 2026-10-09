import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/hindi-theme.css', import.meta.url);

export const hindiThemeCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const hindiThemeStyleLink = '<link rel="stylesheet" href="/assets/css/hindi-theme.min.css?v=757a9f79" data-topic-theme="hindi">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeHindiThemeStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(hindiThemeCss) ? hindiThemeStyleLink : tag;
  });
}

export function hydrateHindiThemeStyles(html) {
  return html.replace(/<link\b[^>]*data-topic-theme="hindi"[^>]*>/gi, () => {
    return `<style>\n${hindiThemeCss}\n</style>`;
  });
}

export function externalizeHindiThemeAssets(html) {
  return externalizeHindiThemeStyles(html);
}

export function hydrateHindiThemeAssets(html) {
  return hydrateHindiThemeStyles(html);
}
