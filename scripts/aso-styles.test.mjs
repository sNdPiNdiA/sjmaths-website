import test from 'node:test';
import assert from 'node:assert/strict';
import { asoLessonCss, asoStyleLink, hydrateAsoStyles, externalizeAsoStyles } from './lib/aso-styles.mjs';
test('ASO exact extraction preserves surrounding content and order', () => {
  const prefix = '<head><link href="prior.css">', suffix = '</head><body>Original $x^2$<script>window.test=true</script></body>';
  assert.equal(externalizeAsoStyles(prefix + `<style>${asoLessonCss}</style>` + suffix), prefix + asoStyleLink + suffix);
  assert.equal(externalizeAsoStyles(hydrateAsoStyles(asoStyleLink)), asoStyleLink);
  assert.equal(hydrateAsoStyles(asoStyleLink.replace('.css', '.min.css?v=1234')), `<style>${asoLessonCss}</style>`);
  assert.equal(externalizeAsoStyles(`<style>${asoLessonCss}.extra{color:red}</style>`), `<style>${asoLessonCss}.extra{color:red}</style>`);
  assert.equal(externalizeAsoStyles(`<style media="print">${asoLessonCss}</style>`), `<style media="print">${asoLessonCss}</style>`);
});
