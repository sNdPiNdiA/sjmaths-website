import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/up-assistant-teacher-topic.css', import.meta.url);

export const upAssistantTeacherCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const upAssistantTeacherStyleLink = '<link rel="stylesheet" href="/assets/css/up-assistant-teacher-topic.min.css?v=fea14fb1" data-topic-style="up-assistant">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeUpAssistantStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(upAssistantTeacherCss) ? upAssistantTeacherStyleLink : tag;
  });
}

export function hydrateUpAssistantStyles(html) {
  return html.replace(/<link\b[^>]*data-topic-style="up-assistant"[^>]*>/gi, () => {
    return `<style>\n${upAssistantTeacherCss}\n    </style>`;
  });
}

export function externalizeUpAssistantAssets(html) {
  return externalizeUpAssistantStyles(html);
}

export function hydrateUpAssistantAssets(html) {
  return hydrateUpAssistantStyles(html);
}
