import fs from 'node:fs';

// Exact-block sharing only: never merge variants or change the cascade position.
export function createSharedStyles(marker, definitions) {
  if (!/^data-[a-z-]+$/.test(marker)) throw new Error('Use a data attribute for the style marker.');
  const normalize = css => css.replace(/\r\n/g, '\n').trim();
  const styles = definitions.map(([id, name]) => ({
    id, name,
    css: fs.readFileSync(new URL(`../../assets/css/${name}.css`, import.meta.url), 'utf8').trim(),
    link: `<link rel="stylesheet" href="/assets/css/${name}.css" ${marker}="${id}">`,
  }));
  const markerPattern = new RegExp(`\\b${marker}=["']([^"']+)["']`, 'i');
  const hydrate = html => html.replace(/<link\b[^>]*>/gi, tag => {
    const id = tag.match(markerPattern)?.[1];
    const href = (tag.match(/\bhref=["']([^"']+)["']/i)?.[1] || '').split(/[?#]/)[0];
    const variant = styles.find(style => style.id === id);
    return variant && [`/assets/css/${variant.name}.css`, `/assets/css/${variant.name}.min.css`].includes(href)
      ? `<style>${variant.css}</style>` : tag;
  });
  const externalize = html => html.replace(/<style>([\s\S]*?)<\/style>/gi, (tag, css) =>
    styles.find(style => normalize(css) === normalize(style.css))?.link || tag);
  return { styles, hydrate, externalize };
}
