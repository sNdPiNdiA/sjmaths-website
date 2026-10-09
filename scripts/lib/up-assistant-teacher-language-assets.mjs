import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/up-assistant-teacher-language.css', import.meta.url);

export const upAssistantTeacherLanguageCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upAssistantTeacherLanguageStyleLink = '<link rel="stylesheet" href="/assets/css/up-assistant-teacher-language.min.css?v=263e2ca5" data-topic-style="up-assistant-language">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeUpAssistantLanguageStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(upAssistantTeacherLanguageCss) ? upAssistantTeacherLanguageStyleLink : tag;
  });
}

export function hydrateUpAssistantLanguageStyles(html) {
  return html.replace(/<link\b[^>]*data-topic-style="up-assistant-language"[^>]*>/gi, () => {
    return `<style>\n${upAssistantTeacherLanguageCss}\n    </style>`;
  });
}

export function externalizeUpAssistantLanguageAssets(html) {
  return externalizeUpAssistantLanguageStyles(html);
}

export function hydrateUpAssistantLanguageAssets(html) {
  return hydrateUpAssistantLanguageStyles(html);
}
