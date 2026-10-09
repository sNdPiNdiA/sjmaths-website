import fs from 'node:fs';

const accountingCssUrl = new URL('../../assets/css/commerce-accounting.css', import.meta.url);
const hubCssUrl = new URL('../../assets/css/commerce-hub.css', import.meta.url);
const topicCssUrl = new URL('../../assets/css/commerce-topic.css', import.meta.url);
const auditingCssUrl = new URL('../../assets/css/commerce-auditing.css', import.meta.url);

export const commerceAccountingCss = fs.readFileSync(accountingCssUrl, 'utf8').trim();
export const commerceHubCss = fs.readFileSync(hubCssUrl, 'utf8').trim();
export const commerceTopicCss = fs.readFileSync(topicCssUrl, 'utf8').trim();
export const commerceAuditingCss = fs.readFileSync(auditingCssUrl, 'utf8').trim();

export const commerceAccountingStyleLink = '<link rel="stylesheet" href="/assets/css/commerce-accounting.min.css?v=b9bb64ec" data-commerce-style="accounting">';
export const commerceHubStyleLink = '<link rel="stylesheet" href="/assets/css/commerce-hub.min.css?v=35e5b48f" data-commerce-style="hub">';
export const commerceTopicStyleLink = '<link rel="stylesheet" href="/assets/css/commerce-topic.min.css?v=d9975251" data-commerce-style="topic">';
export const commerceAuditingStyleLink = '<link rel="stylesheet" href="/assets/css/commerce-auditing.min.css?v=0b4e2ccb" data-commerce-style="auditing">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

const normAccountingCss = normalize(commerceAccountingCss);
const normHubCss = normalize(commerceHubCss);
const normTopicCss = normalize(commerceTopicCss);
const normAuditingCss = normalize(commerceAuditingCss);

export function externalizeCommerceStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    const norm = normalize(css);
    if (norm === normAccountingCss) return commerceAccountingStyleLink;
    if (norm === normHubCss) return commerceHubStyleLink;
    if (norm === normTopicCss) return commerceTopicStyleLink;
    if (norm === normAuditingCss) return commerceAuditingStyleLink;
    return tag;
  });
}

export function hydrateCommerceStyles(html) {
  return html
    .replace(/<link\b[^>]*data-commerce-style="accounting"[^>]*>/gi, () => `<style>\n    ${commerceAccountingCss}\n  </style>`)
    .replace(/<link\b[^>]*data-commerce-style="hub"[^>]*>/gi, () => `<style>\n${commerceHubCss}\n</style>`)
    .replace(/<link\b[^>]*data-commerce-style="topic"[^>]*>/gi, () => `<style>\n${commerceTopicCss}\n</style>`)
    .replace(/<link\b[^>]*data-commerce-style="auditing"[^>]*>/gi, () => `<style>\n${commerceAuditingCss}\n</style>`);
}

export function externalizeCommerceAssets(html) {
  return externalizeCommerceStyles(html);
}

export function hydrateCommerceAssets(html) {
  return hydrateCommerceStyles(html);
}
