import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/emerald-theme.css', import.meta.url);

export const emeraldThemeCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const emeraldThemeStyleLink = '<link rel="stylesheet" href="/assets/css/emerald-theme.min.css?v=a6538943" data-topic-theme="emerald">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeEmeraldThemeStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(emeraldThemeCss) ? emeraldThemeStyleLink : tag;
  });
}

export function hydrateEmeraldThemeStyles(html) {
  return html.replace(/<link\b[^>]*data-topic-theme="emerald"[^>]*>/gi, () => {
    return `<style>\n${emeraldThemeCss}\n</style>`;
  });
}

export function externalizeEmeraldThemeAssets(html) {
  return externalizeEmeraldThemeStyles(html);
}

export function hydrateEmeraldThemeAssets(html) {
  return hydrateEmeraldThemeStyles(html);
}
