import test from 'node:test';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
import fs from 'node:fs';
import {
  externalizePhysicalEducationStyles,
  externalizePhysicalEducationTranslator,
  hydratePhysicalEducationStyles,
  normalizePhysicalEducationTranslator,
  physicalEducationTopicCss,
  physicalEducationTopicStyleLink,
} from './lib/physical-education-styles.mjs';

const cssHash = '34f193a181aa35da82f31146efb40dec39dbe13521105025814ee4b25198f6cf';

test('shared stylesheet matches the frozen 307-page bilingual source block', () => {
  assert.equal(Buffer.byteLength(physicalEducationTopicCss), 10765);
  assert.equal(crypto.createHash('sha256').update(physicalEducationTopicCss).digest('hex'), cssHash);
});

test('exact extraction preserves cascade location and leaves style variants alone', () => {
  const source = `<head><link href="before.css"><style>\n${physicalEducationTopicCss}\n</style><style>.later{color:red}</style></head><body>Lesson</body>`;
  assert.equal(
    externalizePhysicalEducationStyles(source),
    `<head><link href="before.css">${physicalEducationTopicStyleLink}<style>.later{color:red}</style></head><body>Lesson</body>`,
  );
  assert.equal(externalizePhysicalEducationStyles(physicalEducationTopicStyleLink), physicalEducationTopicStyleLink);
  assert.equal(hydratePhysicalEducationStyles(physicalEducationTopicStyleLink.replace('.css', '.min.css?v=abc')), `<style>${physicalEducationTopicCss}</style>`);
  assert.equal(externalizePhysicalEducationStyles(`<style>${physicalEducationTopicCss}.extra{color:red}</style>`), `<style>${physicalEducationTopicCss}.extra{color:red}</style>`);
  assert.equal(externalizePhysicalEducationStyles(`<style media="print">${physicalEducationTopicCss}</style>`), `<style media="print">${physicalEducationTopicCss}</style>`);
});

test('translator changes only its exact shared style and import', () => {
  const source = fs.readFileSync(new URL('./translate_physical_education_hindi.mjs', import.meta.url), 'utf8');
  const after = externalizePhysicalEducationTranslator(source);
  assert.equal(normalizePhysicalEducationTranslator(source), normalizePhysicalEducationTranslator(after));
  assert.ok(after.includes("import { physicalEducationTopicStyleLink } from './lib/physical-education-styles.mjs';"));
  assert.equal(after.split('${physicalEducationTopicStyleLink}').length - 1, 1);
  assert.equal(externalizePhysicalEducationTranslator(after), after);
});
