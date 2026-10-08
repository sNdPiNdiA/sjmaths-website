import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { PAGE_TEMPLATE } from '../upsc/upsc-microtopic-template.js';
import { upscStyleLink, upscTopicCss, hydrateUpscStyles, externalizeUpscStyles } from './lib/upsc-styles.mjs';

const require = createRequire(import.meta.url);
const { decorate: decorateExamUI, fingerprint } = require('./apply-exam-ui.cjs');

test('UPSC microtopic template retains extracted styles and shared exam UI', () => {
  const hash = crypto.createHash('sha256').update(PAGE_TEMPLATE).digest('hex');
  // Update this baseline intentionally when the generated page template changes.
  assert.equal(hash, 'f5dbaf20084fc10970056011bb3b831c75e14be24638fbd696ac56738eee41c7');
  assert.equal(PAGE_TEMPLATE.split(upscStyleLink).length - 1, 1);
  assert.match(PAGE_TEMPLATE, /<body class="exam-ui">/);
  assert.match(PAGE_TEMPLATE, /\/assets\/css\/syllabus-planner\.min\.css/);
  assert.match(PAGE_TEMPLATE, /\/assets\/css\/exam-learning\.min\.css/);
});
test('UPSC extraction preserves cascade and leaves modified or attributed rules inline', () => {
  const original = `<head><link href="before.css"><style>\n${upscTopicCss}\n</style><style>.later{color:red}</style></head><body>Original</body>`;
  assert.equal(externalizeUpscStyles(original), `<head><link href="before.css">${upscStyleLink}<style>.later{color:red}</style></head><body>Original</body>`);
  assert.equal(externalizeUpscStyles(hydrateUpscStyles(upscStyleLink)), upscStyleLink);
  assert.equal(hydrateUpscStyles(upscStyleLink.replace('.css', '.min.css?v=1234')), `<style>${upscTopicCss}</style>`);
  for (const source of [`<style>${upscTopicCss}.extra{color:red}</style>`, `<style media="print">${upscTopicCss}</style>`]) assert.equal(externalizeUpscStyles(source), source);
});

test('shared exam UI decoration follows the page newline style without changing content', () => {
  const source = '<html>\r\n<head>\r\n</head>\r\n<body>\r\n<p>Lesson text</p>\r\n</body>\r\n</html>';
  const decorated = decorateExamUI(source);
  assert.doesNotMatch(decorated, /(?<!\r)\n/);
  assert.deepEqual(fingerprint(decorated), fingerprint(source));
});
