import fs from 'node:fs';
import crypto from 'node:crypto';

const cssUrl = new URL('../../assets/css/up-assistant-teacher-glass.css', import.meta.url);

export const upAssistantTeacherGlassCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upAssistantTeacherGlassStyleLink = '<link rel="stylesheet" href="/assets/css/up-assistant-teacher-glass.min.css?v=5e494cef" data-topic-style="up-assistant-glass">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');
const targetHash = '00a4728c5fbf';

export function externalizeUpAssistantGlassStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    const hash = crypto.createHash('sha256').update(normalize(css)).digest('hex').slice(0, 12);
    if (hash === targetHash) return upAssistantTeacherGlassStyleLink;
    return tag;
  });
}

export function hydrateUpAssistantGlassStyles(html) {
  return html.replace(
    /<link\b[^>]*data-topic-style="up-assistant-glass"[^>]*>/gi,
    () => `<style>\n        ${upAssistantTeacherGlassCss}\n    </style>`
  );
}

export function externalizeUpAssistantGlassAssets(html) {
  return externalizeUpAssistantGlassStyles(html);
}

export function hydrateUpAssistantGlassAssets(html) {
  return hydrateUpAssistantGlassStyles(html);
}
