import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/agriculture-theme.css', import.meta.url);

export const agricultureThemeCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const agricultureThemeStyleLink = '<link rel="stylesheet" href="/assets/css/agriculture-theme.min.css?v=f0fb5bcc" data-topic-theme="agriculture">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeAgricultureThemeStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(agricultureThemeCss) ? agricultureThemeStyleLink : tag;
  });
}

export function hydrateAgricultureThemeStyles(html) {
  return html.replace(/<link\b[^>]*data-topic-theme="agriculture"[^>]*>/gi, () => {
    return `<style>\n${agricultureThemeCss}\n</style>`;
  });
}

export function externalizeAgricultureThemeAssets(html) {
  return externalizeAgricultureThemeStyles(html);
}

export function hydrateAgricultureThemeAssets(html) {
  return hydrateAgricultureThemeStyles(html);
}
