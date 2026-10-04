/* Interactive, demand-rendered solids models for Class 11 Physics, Chapter 8. */
(() => {
  'use strict';

  if (!window.THREE) return; // Inline SVGs remain visible if WebGL/Three.js is unavailable.

  const emerald = 0x059669;
  const amber = 0xd97706;
  const ink = 0x334155;
  const background = 0xf8fafc;

  function addLights(scene) {
    scene.add(new THREE.HemisphereLight(0xffffff, 0xcbd5e1, 1.2));
    const key = new THREE.DirectionalLight(0xffffff, 1.6);
    key.position.set(4, 7, 6);
    scene.add(key);
  }

  function arrow(scene, direction, color, length = 0.5) {
    const helper = new THREE.ArrowHelper(direction, new THREE.Vector3(), length, color, 0.18, 0.12);
    scene.add(helper);
    return helper;
  }

  function boot(container, build) {
    const host = container.querySelector('.solid-sim-canvas');
    const fallback = container.querySelector('.solid-sim-fallback');
    if (!host || !fallback) return;
    let renderer;
    try {
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'low-power' });
    } catch {
      return;
    }
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(background);
    const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 40);
    addLights(scene);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
    renderer.domElement.setAttribute('aria-hidden', 'true');
    renderer.domElement.tabIndex = -1;
    host.appendChild(renderer.domElement);
    let draw = () => {};
    try {
      draw = build(scene, camera, container) || draw;
    } catch {
      renderer.dispose();
      renderer.domElement.remove();
      return;
    }

    let visible = false;
    let frame = 0;
    let dead = false;
    const render = () => {
      frame = 0;
      if (dead || !visible || document.hidden) return;
      const width = host.clientWidth;
      const height = host.clientHeight;
      if (!width || !height) return;
      renderer.setSize(width, height, false);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      draw();
      renderer.render(scene, camera);
    };
    const requestRender = () => {
      if (!frame && visible && !document.hidden) frame = requestAnimationFrame(render);
    };
    const resizeObserver = new ResizeObserver(requestRender);
    resizeObserver.observe(host);
    const intersectionObserver = new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
      if (visible) requestRender();
      else if (frame) cancelAnimationFrame(frame), frame = 0;
    }, { rootMargin: '80px' });
    intersectionObserver.observe(container);
    const onVisibility = () => document.hidden ? (frame && cancelAnimationFrame(frame), frame = 0) : requestRender();
    const dispose = () => {
      if (dead) return;
      dead = true;
      if (frame) cancelAnimationFrame(frame);
      resizeObserver.disconnect();
      intersectionObserver.disconnect();
      document.removeEventListener('visibilitychange', onVisibility);
      window.removeEventListener('pagehide', onPageHide);
      window.removeEventListener('pageshow', onPageShow);
      scene.traverse(object => {
        object.geometry?.dispose?.();
        const materials = Array.isArray(object.material) ? object.material : [object.material];
        materials.filter(Boolean).forEach(material => material.dispose());
      });
      renderer.dispose();
      renderer.domElement.remove();
      fallback.hidden = false;
    };
    document.addEventListener('visibilitychange', onVisibility);
    const onPageHide = event => { if (!event.persisted) dispose(); };
    const onPageShow = () => requestRender();
    window.addEventListener('pagehide', onPageHide);
    window.addEventListener('pageshow', onPageShow);
    fallback.hidden = true;
    container.querySelector('input[type="range"]')?.addEventListener('input', requestRender);
    requestRender();
  }

  function buildTension(scene, camera, container) {
    camera.position.set(4.8, 3.4, 7.5);
    camera.lookAt(0, 1.1, 0);
    const rods = [];
    const colors = [emerald, amber];
    [-0.85, 0.85].forEach((x, i) => {
      const original = new THREE.Mesh(new THREE.CylinderGeometry(0.19, 0.19, 2.1, 32), new THREE.MeshBasicMaterial({ color: colors[i], wireframe: true, transparent: true, opacity: 0.22 }));
      original.position.set(x, 1.05, 0);
      scene.add(original);
      const rod = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.15, 2.1, 32), new THREE.MeshStandardMaterial({ color: colors[i], roughness: 0.42, metalness: 0.08 }));
      rod.position.set(x, 1.05, 0);
      scene.add(rod);
      const upper = arrow(scene, new THREE.Vector3(0, 1, 0), amber, 0.45);
      const lower = arrow(scene, new THREE.Vector3(0, -1, 0), amber, 0.45);
      rods.push({ rod, upper, lower, x, original });
    });
    const ground = new THREE.Mesh(new THREE.PlaneGeometry(7, 5), new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 1 }));
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -0.06;
    scene.add(ground);
    const slider = container.querySelector('input[type="range"]');
    const value = container.querySelector('[data-sim-readout]');
    const fmt = new Intl.NumberFormat('en', { maximumFractionDigits: 2 });
    const update = () => {
      const force = Number(slider.value);
      const area = Math.PI * 0.005 ** 2;
      const materials = [{ name: 'Steel', young: 200e9 }, { name: 'Copper', young: 110e9 }];
      rods.forEach(({ rod, upper, lower, x }, i) => {
        const extension = force * 2 / (area * materials[i].young);
        const shownExtension = extension * 80;
        const height = 2.1 + shownExtension;
        rod.scale.y = height / 2.1;
        rod.position.y = height / 2;
        upper.position.set(x, height + 0.1, 0);
        lower.position.set(x, -0.08, 0);
      });
      value.textContent = `Steel: ${fmt.format(force * 2 / (area * 200e9) * 1000)} mm · Copper: ${fmt.format(force * 2 / (area * 110e9) * 1000)} mm`;
    };
    slider.addEventListener('input', update);
    update();
    return update;
  }

  function buildShear(scene, camera, container) {
    camera.position.set(4.2, 3.2, 6.8);
    camera.lookAt(0, 1.1, 0);
    const geometry = new THREE.BoxGeometry(2.4, 2.2, 1.3, 2, 6, 2);
    const base = geometry.attributes.position.array.slice();
    const block = new THREE.Mesh(geometry, new THREE.MeshStandardMaterial({ color: 0x10b981, roughness: 0.62, metalness: 0.02 }));
    block.position.y = 1.1;
    scene.add(block);
    const edges = new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(2.4, 2.2, 1.3)), new THREE.LineBasicMaterial({ color: ink, transparent: true, opacity: 0.38 }));
    edges.position.y = 1.1;
    scene.add(edges);
    const top = arrow(scene, new THREE.Vector3(1, 0, 0), amber, 0.58);
    const bottom = arrow(scene, new THREE.Vector3(-1, 0, 0), amber, 0.58);
    const floor = new THREE.Mesh(new THREE.BoxGeometry(3.2, 0.16, 2), new THREE.MeshStandardMaterial({ color: 0xcbd5e1 }));
    floor.position.set(0, -0.08, 0);
    scene.add(floor);
    const slider = container.querySelector('input[type="range"]');
    const value = container.querySelector('[data-sim-readout]');
    const update = () => {
      const gamma = Number(slider.value);
      const positions = geometry.attributes.position;
      for (let i = 0; i < positions.count; i++) {
        positions.setX(i, base[i * 3] + gamma * (base[i * 3 + 1] + 1.1));
      }
      positions.needsUpdate = true;
      geometry.computeVertexNormals();
      const dx = gamma * 2.2;
      const angle = Math.atan(gamma) * 180 / Math.PI;
      top.position.set(1.2 + dx, 2.32, 0);
      bottom.position.set(-1.35, -0.16, 0);
      value.textContent = `Shear strain γ = ${gamma.toFixed(2)} · top shift Δx = ${dx.toFixed(2)} units · θ = ${angle.toFixed(1)}°`;
    };
    slider.addEventListener('input', update);
    update();
    return update;
  }

  function buildBeam(scene, camera, container) {
    camera.position.set(4.2, 2.8, 7.2);
    camera.lookAt(0, -0.05, 0);
    const length = 2;
    const breadth = 0.06;
    const depth = 0.12;
    const young = 200e9;
    const secondMoment = breadth * depth ** 3 / 12;
    const amplification = 60;
    const segments = 28;
    const vertices = [];
    const indices = [];
    for (let i = 0; i <= segments; i++) {
      const x = -length + 2 * length * i / segments;
      for (const y of [-depth / 2, depth / 2]) for (const z of [-breadth / 2, breadth / 2]) vertices.push(x, y, z);
      if (i < segments) {
        const a = i * 4;
        const b = a + 4;
        for (const [p, q] of [[0, 1], [1, 3], [3, 2], [2, 0]]) indices.push(a + p, a + q, b + q, a + p, b + q, b + p);
        indices.push(a, a + 1, a + 3, a, a + 3, a + 2, b, b + 2, b + 3, b, b + 3, b + 1);
      }
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
    geo.setIndex(indices);
    geo.computeVertexNormals();
    const beam = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: emerald, roughness: 0.5, side: THREE.DoubleSide }));
    scene.add(beam);
    const supportMat = new THREE.MeshStandardMaterial({ color: amber, roughness: 0.7 });
    [-length, length].forEach(x => {
      const support = new THREE.Mesh(new THREE.ConeGeometry(0.24, 0.36, 4), supportMat);
      support.position.set(x, -0.24, 0);
      support.rotation.y = Math.PI / 4;
      scene.add(support);
    });
    const loadArrow = arrow(scene, new THREE.Vector3(0, -1, 0), amber, 0.65);
    const slider = container.querySelector('input[type="range"]');
    const value = container.querySelector('[data-sim-readout]');
    const update = () => {
      const load = Number(slider.value);
      const delta = load * length ** 3 / (48 * young * secondMoment);
      for (let i = 0; i <= segments; i++) {
        const x = vertices[i * 12];
        const distanceFromSupport = length / 2 * (1 - Math.abs(x) / length);
        const shapeRatio = distanceFromSupport * (3 * length ** 2 - 4 * distanceFromSupport ** 2) / length ** 3;
        const deflection = delta * shapeRatio;
        const visual = -deflection * amplification;
        for (let corner = 0; corner < 4; corner++) geo.attributes.position.setY(i * 4 + corner, vertices[i * 12 + corner * 3 + 1] + visual);
      }
      geo.attributes.position.needsUpdate = true;
      geo.computeVertexNormals();
      loadArrow.position.set(0, 0.55, 0);
      loadArrow.setLength(0.35 + load / 1500 * 0.35, 0.16, 0.11);
      value.textContent = `Centre load = ${load.toFixed(0)} N · calculated sag = ${(delta * 1000).toFixed(2)} mm`;
    };
    slider.addEventListener('input', update);
    update();
    return update;
  }

  function start() {
    document.querySelectorAll('.solid-sim[data-sim]').forEach(container => {
      const builders = { tension: buildTension, shear: buildShear, beam: buildBeam };
      const build = builders[container.dataset.sim];
      if (build) boot(container, build);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
