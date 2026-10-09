import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/upsssc-pet-topic.css', import.meta.url);

export const upssscPetCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upssscPetStyleLink = '<link rel="stylesheet" href="/assets/css/upsssc-pet-topic.min.css?v=114fb48b" data-upsssc-style="topic">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeUpssscPetStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(upssscPetCss) ? upssscPetStyleLink : tag;
  });
}

export function hydrateUpssscPetStyles(html) {
  return html.replace(/<link\b[^>]*data-upsssc-style="topic"[^>]*>/gi, () => {
    return `<style>\r\n    ${upssscPetCss}\r\n  </style>`;
  });
}

export function externalizeUpssscPetAssets(html) {
  return externalizeUpssscPetStyles(html);
}

export function hydrateUpssscPetAssets(html) {
  return hydrateUpssscPetStyles(html);
}
