import { createSharedStyles } from './shared-styles.mjs';

const registry = createSharedStyles('data-sociology-bilingual-style', [['shared', 'sociology-bilingual-topic']]);
const normalize = source => source.replace(/\r\n/g, '\n').trim();

export const sociologyBilingualStyleLink = registry.styles[0].link;
export const sociologyBilingualCss = registry.styles[0].css;

export function externalizeSociologyBilingualStyle(html, styleSource = sociologyBilingualCss, { strict = false } = {}) {
  const style = normalize(styleSource);
  let matches = 0;
  const output = html.replace(/<style>([\s\S]*?)<\/style>/gi, (tag, source) => {
    if (normalize(source) !== style) return tag;
    matches++;
    return sociologyBilingualStyleLink;
  });
  if (strict && matches !== 1) throw new Error(`Expected one exact shared Sociology bilingual stylesheet, found ${matches}.`);
  return output;
}

export function hydrateSociologyBilingualStyle(html) {
  return registry.hydrate(html);
}

