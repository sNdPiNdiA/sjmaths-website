import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/upsc-apfc-lesson.css', import.meta.url);

export const upscApfcLessonCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upscApfcLessonStyleLink = '<link rel="stylesheet" href="/assets/css/upsc-apfc-lesson.min.css?v=1f61178c" data-apfc-style="lesson">';

const normalize = text => text.replace(/\r\n/g, '\n').trim();

export function externalizeUpscApfcStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(upscApfcLessonCss) ? upscApfcLessonStyleLink : tag;
  });
}

export function hydrateUpscApfcStyles(html) {
  return html.replace(/<link\b[^>]*data-apfc-style="lesson"[^>]*>/gi, () => {
    return `<style>\n${upscApfcLessonCss}\n  </style>`;
  });
}

export function externalizeUpscApfcAssets(html) {
  return externalizeUpscApfcStyles(html);
}

export function hydrateUpscApfcAssets(html) {
  return hydrateUpscApfcStyles(html);
}
