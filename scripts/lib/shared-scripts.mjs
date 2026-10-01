import fs from 'node:fs';

// Exact classic-script extraction only. Keep parser-blocking execution at the
// original DOM position; defer/async/module or otherwise attributed scripts stay
// inline. Never identify implementation by a loose substring or function name.
export function createSharedScripts(marker, definitions) {
  if (!/^data-[a-z-]+$/.test(marker)) throw new Error('Use a data attribute for the script marker.');
  const normalize = source => source.replace(/\r\n/g, '\n').trim();
  const scripts = definitions.map(([id, name, legacySource]) => {
    const runtimeSource = fs.readFileSync(new URL(`../../assets/js/${name}.js`, import.meta.url), 'utf8').trim();
    return {
      id, name,
      // A frozen legacy implementation may map to a consolidated runtime. Such
      // mappings require source fingerprints and browser equivalence tests.
      source: legacySource ?? runtimeSource,
      tag: `<script src="/assets/js/${name}.js" ${marker}="${id}"></script>`,
    };
  });
  const externalize = html => html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) =>
    scripts.find(script => normalize(script.source) === normalize(source))?.tag || tag);
  const markerPattern = new RegExp(`\\b${marker}=["']([^"']+)["']`, 'i');
  const hydrate = html => html.replace(/<script\b([^>]*)>\s*<\/script>/gi, (tag, attrs) => {
    // Restore only tags owned by this registry, never module/deferred variants.
    if (/\b(?:async|defer|type)\b/i.test(attrs)) return tag;
    const id = attrs.match(markerPattern)?.[1];
    const src = (attrs.match(/\bsrc=["']([^"']+)["']/i)?.[1] || '').split(/[?#]/)[0];
    const variant = scripts.find(script => script.id === id);
    return variant && [`/assets/js/${variant.name}.js`, `/assets/js/${variant.name}.min.js`].includes(src)
      ? `<script>${variant.source}</script>` : tag;
  });
  return { scripts, externalize, hydrate };
}
