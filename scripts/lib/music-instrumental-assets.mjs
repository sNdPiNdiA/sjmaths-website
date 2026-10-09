import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/music-instrumental-topic.css', import.meta.url);

export const musicInstrumentalCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const musicInstrumentalStyleLink = '<link rel="stylesheet" href="/assets/css/music-instrumental-topic.min.css?v=98589d49" data-music-style="instrumental">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeMusicInstrumentalStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(musicInstrumentalCss) ? musicInstrumentalStyleLink : tag;
  });
}

export function hydrateMusicInstrumentalStyles(html) {
  return html.replace(/<link\b[^>]*data-music-style="instrumental"[^>]*>/gi, () => {
    return `<style>${musicInstrumentalCss}</style>`;
  });
}

export function externalizeMusicInstrumentalAssets(html) {
  return externalizeMusicInstrumentalStyles(html);
}

export function hydrateMusicInstrumentalAssets(html) {
  return hydrateMusicInstrumentalStyles(html);
}
