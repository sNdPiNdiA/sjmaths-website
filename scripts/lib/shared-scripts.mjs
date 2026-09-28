import fs from 'node:fs';

// Exact classic-script extraction only. Keep parser-blocking execution at the
// original DOM position; defer/async/module or otherwise attributed scripts stay
// inline. Never identify implementation by a loose substring or function name.
export function createSharedScripts(marker, definitions) {
  if (!/^data-[a-z-]+$/.test(marker)) throw new Error('Use a data attribute for the script marker.');
  const normalize = source => source.replace(/\r\n/g, '\n').trim();
  const scripts = definitions.map(([id, name]) => ({
    id, name,
    source: fs.readFileSync(new URL(`../../assets/js/${name}.js`, import.meta.url), 'utf8').trim(),
    tag: `<script src="/assets/js/${name}.js" ${marker}="${id}"></script>`,
  }));
  const externalize = html => html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) =>
    scripts.find(script => normalize(script.source) === normalize(source))?.tag || tag);
  return { scripts, externalize };
}
