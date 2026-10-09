import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/ahc-ro-aro-table.css', import.meta.url);

export const ahcRoAroTableCss = fs.readFileSync(cssUrl, 'utf8').trim();

export const ahcRoAroTableStyleLink = '<link rel="stylesheet" href="/assets/css/ahc-ro-aro-table.min.css?v=3171c71a" data-table-style="premium">';

const normalize = text => text.replace(/\r\n/g, '\n').split('\n').map(l => l.trim()).filter(Boolean).join('\n');

export function externalizeAhcRoAroStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(ahcRoAroTableCss) ? ahcRoAroTableStyleLink : tag;
  });
}

export function hydrateAhcRoAroStyles(html) {
  return html.replace(/<link\b[^>]*data-table-style="premium"[^>]*>/gi, () => {
    return `<style>\n${ahcRoAroTableCss}\n    </style>`;
  });
}

export function externalizeAhcRoAroAssets(html) {
  return externalizeAhcRoAroStyles(html);
}

export function hydrateAhcRoAroAssets(html) {
  return hydrateAhcRoAroStyles(html);
}
