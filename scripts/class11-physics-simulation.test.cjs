const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(require('node:path').join(__dirname, '../assets/js/class11-gravitation-three.js'), 'utf8');
const trajectoryFunction = source.slice(source.indexOf('    function calculateTrajectory(v0) {'), source.indexOf('    const launchSlider'));
function trajectory(speed) {
  const context = {
    earthR: 5, projPath: [], trajLine: null,
    THEME: { vectorGreen: 1, vectorRed: 2, sunGold: 3 },
    worldGroup: { add() {}, remove() {} }, disposeObject() {},
    THREE: {
      Vector3: class { constructor(x, y, z) { Object.assign(this, { x, y, z }); } },
      BufferGeometry: class { setFromPoints() { return this; } },
      LineBasicMaterial: class {}, Line: class {}
    }
  };
  vm.createContext(context);
  vm.runInContext(trajectoryFunction + `\ncalculateTrajectory(${speed});`, context);
  return context.projPath;
}
test('Escape simulator matches surface circular/escape thresholds and bound trajectories', () => {
  for (const speed of [3, 6]) {
    const points = trajectory(speed);
    assert.ok(points.length < 2000);
    assert.ok(Math.abs(Math.hypot(points.at(-1).x, points.at(-1).y) - 5) < 1e-8);
  }
  const circular = trajectory(11.2 / Math.sqrt(2));
  assert.equal(circular.length, 2000);
  assert.ok(circular.every(p => Math.abs(Math.hypot(p.x, p.y) - 5) < 0.002));
  const bound = trajectory(9);
  assert.equal(bound.length, 2000);
  assert.ok(bound.every(p => Math.hypot(p.x, p.y) < 15));
  for (const speed of [11.2, 15]) {
    const points = trajectory(speed);
    assert.ok(Math.hypot(points.at(-1).x, points.at(-1).y) > 35);
  }
});
