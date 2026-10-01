import fs from 'node:fs';

const stylePath = new URL('../../assets/css/psychology-bilingual-topic.css', import.meta.url);
export const psychologyBilingualStyleLink = '<link rel="stylesheet" href="/assets/css/psychology-bilingual-topic.css" data-psychology-bilingual-style="shared">';
const normalize = source => source.replace(/\r\n/g, '\n').trim();

export function assertPsychologyBilingualTemplateStyle(templateSource) {
  const styles = [...templateSource.matchAll(/<style>([\s\S]*?)<\/style>/gi)];
  const sharedStyle = normalize(fs.readFileSync(stylePath, 'utf8'));
  if (styles.length !== 1 || normalize(styles[0][1]) !== sharedStyle) {
    throw new Error('Psychology bilingual translation template no longer matches the audited shared stylesheet.');
  }
}

export function externalizePsychologyBilingualStyle(html, styleSource, { strict = false } = {}) {
  const style = normalize(styleSource ?? fs.readFileSync(stylePath, 'utf8'));
  let matches = 0;
  const output = html.replace(/<style>([\s\S]*?)<\/style>/gi, (tag, source) => {
    if (normalize(source) !== style) return tag;
    matches++;
    return psychologyBilingualStyleLink;
  });
  if (strict && matches !== 1) {
    throw new Error(`Expected one exact shared Psychology bilingual stylesheet, found ${matches}.`);
  }
  return output;
}

export function hydratePsychologyBilingualStyle(html) {
  const style = fs.readFileSync(stylePath, 'utf8').trim();
  return html.replace(/<link\b([^>]*)>/gi, (tag, attributes) =>
    /data-psychology-bilingual-style="shared"/.test(attributes) ? `<style>${style}</style>` : tag);
}

