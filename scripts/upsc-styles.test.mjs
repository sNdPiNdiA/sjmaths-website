import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { PAGE_TEMPLATE } from '../upsc/upsc-microtopic-template.js';
import { upscStyleLink, upscTopicCss, hydrateUpscStyles, externalizeUpscStyles } from './lib/upsc-styles.mjs';

test('shared UPSC template equals pre-extraction template except exact style and language-script replacements', () => {
  const hash = crypto.createHash('sha256').update(PAGE_TEMPLATE).digest('hex');
  // Recorded from the previous template after ONLY the exact runtime replacement.
  assert.equal(hash, 'b596da8d5d54c0cdc1f113178811724d3523b3b070bd930f9205fc55104f9607');
  assert.equal(PAGE_TEMPLATE.split(upscStyleLink).length - 1, 1);
});
test('UPSC extraction preserves cascade and leaves modified or attributed rules inline', () => {
  const original = `<head><link href="before.css"><style>\n${upscTopicCss}\n</style><style>.later{color:red}</style></head><body>Original</body>`;
  assert.equal(externalizeUpscStyles(original), `<head><link href="before.css">${upscStyleLink}<style>.later{color:red}</style></head><body>Original</body>`);
  assert.equal(externalizeUpscStyles(hydrateUpscStyles(upscStyleLink)), upscStyleLink);
  assert.equal(hydrateUpscStyles(upscStyleLink.replace('.css', '.min.css?v=1234')), `<style>${upscTopicCss}</style>`);
  for (const source of [`<style>${upscTopicCss}.extra{color:red}</style>`, `<style media="print">${upscTopicCss}</style>`]) assert.equal(externalizeUpscStyles(source), source);
});
