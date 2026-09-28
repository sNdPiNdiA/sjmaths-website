const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { spawnSync } = require('node:child_process');
const { ROOT } = require('./seo-html.cjs');

for (const [legacy, canonical] of [
  ['aso-count.cjs', 'count.cjs'],
  ['aso-hub-disk-check.cjs', 'hub-disk-check.cjs'],
  ['aso-hub-verify.cjs', 'hub-verify.cjs'],
  ['aso-coverage-audit.cjs', 'coverage-audit.cjs'],
]) {
  test(`${legacy} preserves output and works outside the repository`, () => {
    const hub = path.join(ROOT, 'upsc-aso/index.html');
    const before = fs.readFileSync(hub);
    let expected;
    for (const cwd of [ROOT, os.tmpdir()]) {
      for (const file of [legacy, `scripts/aso/${canonical}`]) {
        const result = spawnSync(process.execPath, [path.join(ROOT, file)], {
          cwd, encoding: 'utf8', timeout: 20000, maxBuffer: 5e6,
        });
        assert.equal(result.status, 0, result.stderr || String(result.error));
        assert.equal(result.stderr, '');
        if (expected === undefined) expected = result.stdout;
        else assert.equal(result.stdout, expected);
      }
    }
    assert.deepEqual(fs.readFileSync(hub), before, 'diagnostic must not mutate the hub');
  });
}
