import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/logic-topic.css', import.meta.url);

export const logicTopicCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const logicTopicStyleLink = '<link rel="stylesheet" href="/assets/css/logic-topic.min.css?v=7cabe963" data-study-guide-style="logic">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeLogicStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(logicTopicCss) ? logicTopicStyleLink : tag;
  });
}

export function hydrateLogicStyles(html) {
  return html.replace(/<link\b[^>]*data-study-guide-style="logic"[^>]*>/gi, () => {
    return `<style>\n${logicTopicCss}\n</style>`;
  });
}

export function externalizeLogicAssets(html) {
  return externalizeLogicStyles(html);
}

export function hydrateLogicAssets(html) {
  return hydrateLogicStyles(html);
}
