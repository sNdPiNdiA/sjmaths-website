import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/chemistry-topic.css', import.meta.url);

export const chemistryTopicCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const chemistryTopicStyleLink = '<link rel="stylesheet" href="/assets/css/chemistry-topic.min.css?v=993fd937" data-chemistry-style="theme">';

const normalize = text => text.replace(/\r\n/g, '\n').trim();

export function externalizeChemistryStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(chemistryTopicCss) ? chemistryTopicStyleLink : tag;
  });
}

export function hydrateChemistryStyles(html) {
  return html.replace(/<link\b[^>]*data-chemistry-style="theme"[^>]*>/gi, () => {
    return `<style>\n${chemistryTopicCss}\n</style>`;
  });
}

export function externalizeChemistryAssets(html) {
  return externalizeChemistryStyles(html);
}

export function hydrateChemistryAssets(html) {
  return hydrateChemistryStyles(html);
}
