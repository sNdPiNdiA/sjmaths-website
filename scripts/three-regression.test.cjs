const assert = require('assert/strict');
const fs = require('fs');
const path = require('path');
const test = require('node:test');

const ROOT = path.resolve(__dirname, '..');
const source = fs.readFileSync(
  path.join(ROOT, 'class-10-science/chapter-10-human-eye-and-the-colourful-world/three-animations.js'),
  'utf8'
);
const reflectionSource = fs.readFileSync(
  path.join(ROOT, 'class-10-science/chapter-9-light-reflection-and-refraction/three-animations.js'),
  'utf8'
);
const chemistrySource = fs.readFileSync(
  path.join(ROOT, 'class-10-science/chapter-1-chemical-reactions-and-equations/three-animations.js'),
  'utf8'
);
const electricitySource = fs.readFileSync(
  path.join(ROOT, 'class-10-science/chapter-11-electricity/three-animations.js'),
  'utf8'
);
const magnetismSource = fs.readFileSync(
  path.join(ROOT, 'class-10-science/chapter-12-magnetic-effects-of-electric-current/three-animations.js'),
  'utf8'
);
const class9MotionSource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class9-motion-three.js'),
  'utf8'
);
const class9NewtonSource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class9-newton-three.js'),
  'utf8'
);
const class11GravitationSource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class11-gravitation-three.js'),
  'utf8'
);
const class11LawsSource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class11-lawsofmotion-three.js'),
  'utf8'
);
const class11MotionPlaneSource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class11-motionplane-three.js'),
  'utf8'
);
const class11RotationalSource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class11-rotational-three.js'),
  'utf8'
);
const class11WorkEnergySource = fs.readFileSync(
  path.join(ROOT, 'assets/js/class11-workenergy-three.js'),
  'utf8'
);

test('Eye Optics simulation owns and releases its animation lifecycle', () => {
  assert.match(source, /this\.rafId = null/);
  assert.match(source, /cancelAnimationFrame\(this\.rafId\)/);
  assert.match(source, /this\.resizeObserver = new ResizeObserver/);
  assert.match(source, /this\.resizeObserver\.disconnect\(\)/);
  assert.match(source, /this\.renderer\.dispose\(\)/);
  assert.match(source, /while \(this\.dynamicGroup\.children\.length > 0\) \{[\s\S]*?this\.disposeObject\(child\)/);
  assert.match(source, /this\.reducedMotion = .*prefers-reduced-motion/s);
  assert.match(source, /document\.addEventListener\("visibilitychange"/);
  assert.match(source, /document\.removeEventListener\("visibilitychange"/);
});

test('Eye Optics simulation stores window interaction handlers for teardown', () => {
  assert.match(source, /this\.interactionHandlers = \{/);
  assert.match(source, /window\.removeEventListener\("mousemove", handlers\.onMouseMove\)/);
  assert.match(source, /window\.removeEventListener\("touchmove", handlers\.onTouchMove\)/);
  assert.match(source, /handlers\.el\.removeEventListener\("wheel", handlers\.onWheel\)/);
});

test('Reflection Optics simulation owns and releases its animation lifecycle', () => {
  assert.match(reflectionSource, /this\.rafId = null/);
  assert.match(reflectionSource, /cancelAnimationFrame\(this\.rafId\)/);
  assert.match(reflectionSource, /this\.resizeObserver = new ResizeObserver/);
  assert.match(reflectionSource, /this\.resizeObserver\.disconnect\(\)/);
  assert.match(reflectionSource, /this\.renderer\.dispose\(\)/);
  assert.match(reflectionSource, /this\.reducedMotion = .*prefers-reduced-motion/s);
  assert.match(reflectionSource, /this\.disposeObject\(child\)/);
  assert.match(reflectionSource, /document\.removeEventListener\("visibilitychange"/);
});

test('Science Lab simulation cancels offscreen animation and releases scene resources', () => {
  assert.match(chemistrySource, /this\.rafId = null/);
  assert.match(chemistrySource, /cancelAnimationFrame\(this\.rafId\)/);
  assert.match(chemistrySource, /this\.resizeObserver = new ResizeObserver/);
  assert.match(chemistrySource, /this\.intersectionObserver = new IntersectionObserver/);
  assert.match(chemistrySource, /this\.renderer\.dispose\(\)/);
  assert.match(chemistrySource, /this\.disposeObject\(this\.scene\)/);
  assert.match(chemistrySource, /this\.reducedMotion = .*prefers-reduced-motion/s);
  assert.match(chemistrySource, /document\.removeEventListener\("visibilitychange"/);
});

test('Circuit simulation respects reduced motion and removes page lifecycle listeners', () => {
  assert.match(electricitySource, /this\.rafId = 0/);
  assert.match(electricitySource, /cancelAnimationFrame\(this\.rafId\)/);
  assert.match(electricitySource, /this\.resizeObserver = new ResizeObserver/);
  assert.match(electricitySource, /this\.renderer\.dispose\(\)/);
  assert.match(electricitySource, /this\.reducedMotion = .*prefers-reduced-motion/s);
  assert.match(electricitySource, /if \(!this\.reducedMotion\) this\.rafId = requestAnimationFrame\(render\)/);
  assert.match(electricitySource, /document\.removeEventListener\("visibilitychange"/);
});

test('Magnetism simulations share a cancellable lifecycle and dispose scene resources', () => {
  assert.match(magnetismSource, /let animationFrameId = null/);
  assert.match(magnetismSource, /cancelAnimationFrame\(animationFrameId\)/);
  assert.match(magnetismSource, /state\.resizeObserver = new ResizeObserver/);
  assert.match(magnetismSource, /state\.cleanupFns\.push/);
  assert.match(magnetismSource, /state\.renderer\.dispose\(\)/);
  assert.match(magnetismSource, /function disposeObject\(object\)/);
  assert.match(magnetismSource, /reducedMotion: .*prefers-reduced-motion/s);
  assert.match(magnetismSource, /document\.addEventListener\("visibilitychange"/);
});

test('Class 9 motion simulations share cancellable RAF and input lifecycles', () => {
  assert.match(class9MotionSource, /const lifecycle = \{/);
  assert.match(class9MotionSource, /cancelAnimationFrame\(this\.rafId\)|cancelAnimationFrame\(this\.rafId\)/);
  assert.match(class9MotionSource, /lifecycle\.rafId = requestAnimationFrame\(animate\)/);
  assert.match(class9MotionSource, /lifecycle\.reducedMotion/);
  assert.match(class9MotionSource, /lifecycle\.cleanupFns\.push/);
  assert.match(class9MotionSource, /function disposeObject\(object\)/);
  assert.match(class9MotionSource, /renderer\.dispose\(\)/);
});

test('Class 9 Newton simulations share cancellable RAF and input lifecycles', () => {
  assert.match(class9NewtonSource, /const lifecycle = \{/);
  assert.match(class9NewtonSource, /cancelAnimationFrame\(this\.rafId\)/);
  assert.match(class9NewtonSource, /lifecycle\.rafId = requestAnimationFrame\(animate\)/);
  assert.match(class9NewtonSource, /lifecycle\.reducedMotion/);
  assert.match(class9NewtonSource, /lifecycle\.cleanupFns\.push/);
  assert.match(class9NewtonSource, /function disposeObject\(object\)/);
  assert.match(class9NewtonSource, /renderer\.dispose\(\)/);
});

test('Class 11 gravitation simulations share cancellable RAF and dispose dynamic geometry', () => {
  assert.match(class11GravitationSource, /const lifecycle = \{/);
  assert.match(class11GravitationSource, /cancelAnimationFrame\(frameId\)/);
  assert.match(class11GravitationSource, /lifecycle\.schedule\(animate\)/);
  assert.match(class11GravitationSource, /reducedMotion: .*prefers-reduced-motion/s);
  assert.match(class11GravitationSource, /document\.addEventListener\('visibilitychange'/);
  assert.match(class11GravitationSource, /document\.removeEventListener\('visibilitychange'/);
  assert.match(class11GravitationSource, /disposeObject\(sweepSectorMesh\)/);
  assert.match(class11GravitationSource, /renderer\.dispose\(\)/);
});

test('Class 11 Laws of Motion simulations share cancellable RAF and dispose scenes', () => {
  assert.match(class11LawsSource, /const lifecycle = \{/);
  assert.match(class11LawsSource, /cancelAnimationFrame\(frameId\)/);
  assert.match(class11LawsSource, /lifecycle\.schedule\(animate\)/);
  assert.match(class11LawsSource, /reducedMotion: .*prefers-reduced-motion/s);
  assert.match(class11LawsSource, /document\.addEventListener\('visibilitychange'/);
  assert.match(class11LawsSource, /document\.removeEventListener\('visibilitychange'/);
  assert.match(class11LawsSource, /disposeObject\(scene\)/);
  assert.match(class11LawsSource, /renderer\.dispose\(\)/);
});

test('Class 11 Motion in a Plane simulations share cancellable RAF and dispose scenes', () => {
  assert.match(class11MotionPlaneSource, /const lifecycle = \{/);
  assert.match(class11MotionPlaneSource, /cancelAnimationFrame\(frameId\)/);
  assert.match(class11MotionPlaneSource, /lifecycle\.schedule\(animate\)/);
  assert.match(class11MotionPlaneSource, /reducedMotion: .*prefers-reduced-motion/s);
  assert.match(class11MotionPlaneSource, /document\.addEventListener\('visibilitychange'/);
  assert.match(class11MotionPlaneSource, /document\.removeEventListener\('visibilitychange'/);
  assert.match(class11MotionPlaneSource, /disposeObject\(scene\)/);
  assert.match(class11MotionPlaneSource, /renderer\.dispose\(\)/);
});

test('Class 11 rotational simulations share cancellable RAF and dispose scenes', () => {
  assert.match(class11RotationalSource, /const lifecycle = \{/);
  assert.match(class11RotationalSource, /cancelAnimationFrame\(frameId\)/);
  assert.match(class11RotationalSource, /lifecycle\.schedule\(animate\)/);
  assert.match(class11RotationalSource, /reducedMotion: .*prefers-reduced-motion/s);
  assert.match(class11RotationalSource, /document\.addEventListener\('visibilitychange'/);
  assert.match(class11RotationalSource, /document\.removeEventListener\('visibilitychange'/);
  assert.match(class11RotationalSource, /disposeObject\(scene\)/);
  assert.match(class11RotationalSource, /renderer\.dispose\(\)/);
});

test('Class 11 Work Energy simulations share cancellable RAF and dispose scenes', () => {
  assert.match(class11WorkEnergySource, /const lifecycle = \{/);
  assert.match(class11WorkEnergySource, /cancelAnimationFrame\(frameId\)/);
  assert.match(class11WorkEnergySource, /lifecycle\.schedule\(animate\)/);
  assert.match(class11WorkEnergySource, /reducedMotion: .*prefers-reduced-motion/s);
  assert.match(class11WorkEnergySource, /document\.addEventListener\('visibilitychange'/);
  assert.match(class11WorkEnergySource, /document\.removeEventListener\('visibilitychange'/);
  assert.match(class11WorkEnergySource, /disposeObject\(scene\)/);
  assert.match(class11WorkEnergySource, /renderer\.dispose\(\)/);
});
