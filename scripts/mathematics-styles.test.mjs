import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {
  externalizeMathematicsGenerator,
  externalizeMathematicsStyles,
  hydrateMathematicsStyles,
  mathematicsTopicCss,
  mathematicsTopicStyleLink,
  normalizeMathematicsGenerator,
} from './lib/mathematics-styles.mjs';

const cssHash = 'd1b71cea5e3aefa8be6992c395c8f03ce2aa30422d7c282a92a378c02cf8fbcf';

test('Mathematics shared stylesheet matches the frozen 299-page source block', () => {
  assert.equal(Buffer.byteLength(mathematicsTopicCss), 15125);
  assert.equal(crypto.createHash('sha256').update(mathematicsTopicCss).digest('hex'), cssHash);
  const source = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  assert.equal((externalizeMathematicsStyles(source).match(/\$\{mathematicsTopicStyleLink\}/g) || []).length, 1);
});

test('Mathematics exact style extraction preserves cascade position and variants', () => {
  const source = `<head><link href="before.css"><style>\n${mathematicsTopicCss}\n</style><style>.later{color:red}</style></head><body>Educational content</body>`;
  assert.equal(
    externalizeMathematicsStyles(source),
    `<head><link href="before.css">${mathematicsTopicStyleLink}<style>.later{color:red}</style></head><body>Educational content</body>`,
  );
  assert.equal(externalizeMathematicsStyles(mathematicsTopicStyleLink), mathematicsTopicStyleLink);
  assert.equal(hydrateMathematicsStyles(mathematicsTopicStyleLink.replace('.css', '.min.css?v=abc')), `<style>${mathematicsTopicCss}</style>`);
  assert.equal(externalizeMathematicsStyles(`<style>${mathematicsTopicCss}.extra{color:red}</style>`), `<style>${mathematicsTopicCss}.extra{color:red}</style>`);
  assert.equal(externalizeMathematicsStyles(`<style media="print">${mathematicsTopicCss}</style>`), `<style media="print">${mathematicsTopicCss}</style>`);
});

test('Mathematics generator changes only the shared stylesheet reference and import', () => {
  const source = fs.readFileSync(new URL('../scripts/generate_mathematics.mjs', import.meta.url), 'utf8');
  const after = externalizeMathematicsGenerator(source);
  assert.equal(normalizeMathematicsGenerator(source), normalizeMathematicsGenerator(after));
  assert.ok(after.includes("import { mathematicsTopicStyleLink } from './lib/mathematics-styles.mjs';"));
  assert.equal(after.split('${mathematicsTopicStyleLink}').length - 1, 1);
  assert.equal(externalizeMathematicsGenerator(after), after);
});
