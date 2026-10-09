import fs from 'node:fs';

const topicCssUrl = new URL('../../assets/css/civics-topic.css', import.meta.url);
const hubCssUrl = new URL('../../assets/css/civics-hub.css', import.meta.url);

export const civicsTopicCss = fs.readFileSync(topicCssUrl, 'utf8').trim();
export const civicsHubCss = fs.readFileSync(hubCssUrl, 'utf8').trim();

export const civicsTopicStyleLink = '<link rel="stylesheet" href="/assets/css/civics-topic.min.css?v=a0cb147b" data-civics-style="topic">';
export const civicsHubStyleLink = '<link rel="stylesheet" href="/assets/css/civics-hub.min.css?v=307ead65" data-civics-style="hub">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

const normTopicCss = normalize(civicsTopicCss);
const normHubCss = normalize(civicsHubCss);

export function externalizeCivicsStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    const norm = normalize(css);
    if (norm === normTopicCss) return civicsTopicStyleLink;
    if (norm === normHubCss) return civicsHubStyleLink;
    return tag;
  });
}

export function hydrateCivicsStyles(html) {
  return html
    .replace(/<link\b[^>]*data-civics-style="topic"[^>]*>/gi, () => `<style>\n${civicsTopicCss}\n</style>`)
    .replace(/<link\b[^>]*data-civics-style="hub"[^>]*>/gi, () => `<style>\n${civicsHubCss}\n</style>`);
}

export function externalizeCivicsAssets(html) {
  return externalizeCivicsStyles(html);
}

export function hydrateCivicsAssets(html) {
  return hydrateCivicsStyles(html);
}
