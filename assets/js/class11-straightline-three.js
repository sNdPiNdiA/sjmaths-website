/**
 * SJMaths - Class 11 Physics Chapter 2: Motion in a Straight Line
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. Position-Time (x-t), Velocity-Time (v-t) & Slope/Tangent Visualizer (Instantaneous velocity v = dx/dt)
 * 2. 1D Uniform Accelerated Motion (x = v0*t + 1/2*a*t^2, v = v0 + a*t, car acceleration & braking)
 * 3. Vertical Ball Throw & Free Fall under Gravity (Upward projection from building, peak v=0, quadratic fall t=5s)
 * 4. 1D Relative Motion & Overtaking Simulator (Two cars on parallel tracks, v_rel = vA - vB, same vs opposite directions)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Chapter 2. Retrying on load.");
    return;
  }

  const THEME = {
    spaceDark: 0x090d16,
    gold: 0xf59e0b,
    blue: 0x38bdf8,
    emerald: 0x10b981,
    purple: 0xa855f7,
    rose: 0xf43f5e,
    cyan: 0x06b6d4,
    metal: 0x64748b,
    white: 0xffffff
  };

  function create3DCanvas(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return null;

    container.innerHTML = '';
    const width = container.clientWidth || 600;
    const height = container.clientHeight || 360;

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(THEME.spaceDark);

    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.appendChild(renderer.domElement);

    const gridHelper = new THREE.GridHelper(30, 20, 0x334155, 0x1e293b);
    gridHelper.position.y = -3;
    scene.add(gridHelper);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);
    const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(12, 18, 14);
    scene.add(dirLight);

    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };
    let rotation = { x: 0.3, y: 0.4 };

    const dom = renderer.domElement;
    dom.style.cursor = 'grab';

    dom.addEventListener('mousedown', (e) => {
      isDragging = true;
      prevMousePos = { x: e.clientX, y: e.clientY };
      dom.style.cursor = 'grabbing';
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      const dx = e.clientX - prevMousePos.x;
      const dy = e.clientY - prevMousePos.y;
      rotation.y += dx * 0.008;
      rotation.x += dy * 0.008;
      rotation.x = Math.max(-1.4, Math.min(1.4, rotation.x));
      prevMousePos = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
      dom.style.cursor = 'grab';
    });

    dom.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        prevMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    }, { passive: true });

    dom.addEventListener('touchmove', (e) => {
      if (!isDragging || e.touches.length !== 1) return;
      const dx = e.touches[0].clientX - prevMousePos.x;
      const dy = e.touches[0].clientY - prevMousePos.y;
      rotation.y += dx * 0.008;
      rotation.x += dy * 0.008;
      rotation.x = Math.max(-1.4, Math.min(1.4, rotation.x));
      prevMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    }, { passive: true });

    window.addEventListener('touchend', () => { isDragging = false; });

    const onResize = () => {
      if (!container.parentElement) return;
      const w = container.clientWidth || 600;
      const h = container.clientHeight || 360;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    };
    window.addEventListener('resize', onResize);

    return { scene, camera, renderer, rotation, onResize };
  }

  /* =========================================================================
     1. SIMULATION: 3D Position-Time & Instantaneous Tangent Slope (v = dx/dt)
     ========================================================================= */
  function initSlopeTangentSimulation() {
    const setup = create3DCanvas('three-slope-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 12, 26);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // 3D Curve Mesh for x(t) = a * t^2
    let curveMesh;
    function buildCurve(a) {
      if (curveMesh) {
        group.remove(curveMesh);
        curveMesh.geometry.dispose();
      }
      const pts = [];
      for (let t = -6; t <= 6; t += 0.2) {
        const px = t * 1.8;
        const py = (0.2 * a * t * t) - 2;
        pts.push(new THREE.Vector3(px, py, 0));
      }
      const curve = new THREE.CatmullRomCurve3(pts);
      curveMesh = new THREE.Mesh(
        new THREE.TubeGeometry(curve, 64, 0.12, 8, false),
        new THREE.MeshStandardMaterial({ color: THEME.cyan, roughness: 0.3 })
      );
      group.add(curveMesh);
    }

    // Moving Probe Point on Curve
    const probe = new THREE.Mesh(
      new THREE.SphereGeometry(0.5, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.gold, emissive: 0xd97706, emissiveIntensity: 0.6 })
    );
    group.add(probe);

    // Tangent Line Rod (slope = dx/dt)
    const tangentGeo = new THREE.CylinderGeometry(0.08, 0.08, 10, 16);
    tangentGeo.rotateZ(Math.PI / 2);
    const tangentMat = new THREE.MeshBasicMaterial({ color: THEME.rose });
    const tangentRod = new THREE.Mesh(tangentGeo, tangentMat);
    group.add(tangentRod);

    const tSlider = document.getElementById('slope-t-slider');
    const aSlider = document.getElementById('slope-a-slider');
    const slopeHudText = document.getElementById('slope-hud-display');

    function updateSlope() {
      const t = tSlider ? parseFloat(tSlider.value) : 2.0;
      const a = aSlider ? parseFloat(aSlider.value) : 1.0;

      buildCurve(a);

      const px = t * 1.8;
      const py = (0.2 * a * t * t) - 2;
      probe.position.set(px, py, 0);

      // Derivative slope: dy/dx_world = (0.4 * a * t) / 1.8
      const slope = (0.4 * a * t) / 1.8;
      const angle = Math.atan(slope);

      tangentRod.position.set(px, py, 0);
      tangentRod.rotation.z = angle;

      const v_inst = a * t;

      if (slopeHudText) {
        slopeHudText.innerHTML = `Time: <b>t = ${t.toFixed(1)}s</b> &bull; Position: <b>x(t) = ${(0.5 * a * t * t).toFixed(1)}m</b> &bull; Tangent Slope: <span style="color:#f43f5e; font-weight:700;">v = dx/dt = ${v_inst.toFixed(2)} m/s</span>`;
      }
    }

    [tSlider, aSlider].forEach(sl => {
      if (sl) sl.addEventListener('input', updateSlope);
    });
    updateSlope();

    function animate() {
      requestAnimationFrame(animate);
      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     2. SIMULATION: 1D Uniform Accelerated Motion (x = v0*t + 1/2*a*t^2)
     ========================================================================= */
  function initAcceleratedMotionSimulation() {
    const setup = create3DCanvas('three-accel1d-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Track
    const trackGeo = new THREE.BoxGeometry(28, 0.4, 4);
    const trackMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
    const track = new THREE.Mesh(trackGeo, trackMat);
    track.position.y = -1.5;
    group.add(track);

    // Track Distance Markers
    for (let x = -12; x <= 12; x += 4) {
      const mark = new THREE.Mesh(new THREE.BoxGeometry(0.15, 0.5, 3.8), new THREE.MeshBasicMaterial({ color: 0x475569 }));
      mark.position.set(x, -1.2, 0);
      group.add(mark);
    }

    // Vehicle
    const carGeo = new THREE.BoxGeometry(3.0, 1.6, 2.0);
    const carMat = new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.3 });
    const car = new THREE.Mesh(carGeo, carMat);
    group.add(car);

    // Velocity Vector Arrow
    const vArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.emerald, 0.8, 0.4);
    group.add(vArrow);

    let time = 0;
    const v0Slider = document.getElementById('accel-v0-slider');
    const aSlider = document.getElementById('accel-a-slider');
    const accelHudText = document.getElementById('accel-hud-display');
    const resetBtn = document.getElementById('accel-reset-btn');

    function resetCar() {
      time = 0;
    }

    if (resetBtn) resetBtn.addEventListener('click', resetCar);

    function animate() {
      requestAnimationFrame(animate);

      const v0 = v0Slider ? parseFloat(v0Slider.value) : 2.0;
      const a = aSlider ? parseFloat(aSlider.value) : 1.5;

      time += 0.02;

      // Kinematic displacement x(t) = v0*t + 0.5*a*t^2
      const xWorld = -12 + (v0 * time + 0.5 * a * time * time);
      const vCurrent = v0 + a * time;

      if (xWorld > 12) {
        time = 0;
      }

      car.position.set(xWorld, 0, 0);

      vArrow.position.set(xWorld, 1.2, 0);
      vArrow.setLength(Math.max(0.8, vCurrent * 0.45), 0.6, 0.3);

      if (accelHudText) {
        accelHudText.innerHTML = `Elapsed Time: <b>t = ${time.toFixed(1)}s</b> &bull; Speed: <span style="color:#10b981; font-weight:700;">v = v₀ + at = ${vCurrent.toFixed(1)} m/s</span> &bull; Position: <span style="color:#38bdf8; font-weight:700;">x = ${(v0 * time + 0.5 * a * time * time).toFixed(1)} m</span>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     3. SIMULATION: Vertical Ball Throw from Building & Free Fall (Example 2.3)
     ========================================================================= */
  function initVerticalFreeFallSimulation() {
    const setup = create3DCanvas('three-freefall-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 12, 28);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Ground
    const groundGeo = new THREE.BoxGeometry(20, 0.4, 8);
    const groundMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.position.set(0, -10, 0);
    group.add(ground);

    // Building Structure (y0 = 25m scaled)
    const bldgHeight = 8.0;
    const bldgGeo = new THREE.BoxGeometry(4.5, bldgHeight, 4.5);
    const bldgMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.6 });
    const bldg = new THREE.Mesh(bldgGeo, bldgMat);
    bldg.position.set(-6, -10 + bldgHeight / 2, 0);
    group.add(bldg);

    // Ball
    const ball = new THREE.Mesh(
      new THREE.SphereGeometry(0.6, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.rose, emissive: 0xe11d48, emissiveIntensity: 0.5 })
    );
    group.add(ball);

    // Velocity Vector
    const vArrow = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.gold, 0.8, 0.4);
    group.add(vArrow);

    let time = 0;
    const v0 = 20.0; // Upward initial velocity
    const g = 10.0;
    const y0 = 25.0; // Building height
    const tTotal = 5.0; // Total flight time to ground

    const throwBtn = document.getElementById('fall-throw-btn');
    const fallHudText = document.getElementById('fall-hud-display');

    function resetThrow() {
      time = 0;
    }

    if (throwBtn) throwBtn.addEventListener('click', resetThrow);

    function animate() {
      requestAnimationFrame(animate);

      time += 0.025;
      if (time > tTotal + 0.5) {
        time = 0;
      }

      const tClamped = Math.min(tTotal, time);
      // y(t) = y0 + v0*t - 0.5*g*t^2
      const yPhys = y0 + v0 * tClamped - 0.5 * g * tClamped * tClamped;
      const vPhys = v0 - g * tClamped;

      // Scale to 3D scene units (ground is -10, building roof is -2, peak y=45m is +6)
      const yScene = -10 + (yPhys / 45.0) * 16.0;

      ball.position.set(-3.0, yScene, 0);

      // Velocity arrow
      const vDir = new THREE.Vector3(0, vPhys >= 0 ? 1 : -1, 0);
      vArrow.position.set(-3.0, yScene, 0);
      vArrow.setDirection(vDir);
      vArrow.setLength(Math.max(0.5, Math.abs(vPhys) * 0.15), 0.6, 0.3);

      if (fallHudText) {
        let phase = tClamped <= 2.0 ? "Ascending to Peak" : (tClamped < 5.0 ? "Descending to Ground" : "Hit Ground (y = 0)");
        fallHudText.innerHTML = `t = <b>${tClamped.toFixed(2)}s</b> &bull; Height from Ground: <span style="color:#38bdf8; font-weight:700;">y = ${yPhys.toFixed(1)}m</span> &bull; Velocity: <span style="color:#f59e0b; font-weight:700;">v = ${vPhys.toFixed(1)} m/s</span> &bull; <i>${phase}</i>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     4. SIMULATION: 1D Relative Velocity & Overtaking (v_rel = vA - vB)
     ========================================================================= */
  function initRelativeMotion1DSimulation() {
    const setup = create3DCanvas('three-rel1d-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 12, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Two Parallel Tracks
    const track1 = new THREE.Mesh(new THREE.BoxGeometry(28, 0.3, 2.5), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
    track1.position.set(0, -1.5, 2.0);
    group.add(track1);

    const track2 = new THREE.Mesh(new THREE.BoxGeometry(28, 0.3, 2.5), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
    track2.position.set(0, -1.5, -2.0);
    group.add(track2);

    // Car A (Blue)
    const carA = new THREE.Mesh(new THREE.BoxGeometry(3.0, 1.4, 1.8), new THREE.MeshStandardMaterial({ color: THEME.blue }));
    group.add(carA);

    // Car B (Rose)
    const carB = new THREE.Mesh(new THREE.BoxGeometry(3.0, 1.4, 1.8), new THREE.MeshStandardMaterial({ color: THEME.rose }));
    group.add(carB);

    let posA = -10;
    let posB = -6;

    const vaSlider = document.getElementById('rel1d-va-slider');
    const vbSlider = document.getElementById('rel1d-vb-slider');
    const dirSelect = document.getElementById('rel1d-dir-select');
    const rel1dHudText = document.getElementById('rel1d-hud-display');

    function animate() {
      requestAnimationFrame(animate);

      const vA = vaSlider ? parseFloat(vaSlider.value) : 15;
      let vB = vbSlider ? parseFloat(vbSlider.value) : 10;
      const isOpposite = dirSelect && dirSelect.value === 'opposite';
      if (isOpposite) vB = -vB;

      posA += vA * 0.005;
      posB += vB * 0.005;

      if (posA > 14) posA = -14;
      if (posB > 14) posB = -14;
      if (posB < -14) posB = 14;

      carA.position.set(posA, -0.6, 2.0);
      carB.position.set(posB, -0.6, -2.0);
      carB.rotation.y = isOpposite ? Math.PI : 0;

      // v_AB = vA - vB
      const v_rel = vA - vB;

      if (rel1dHudText) {
        rel1dHudText.innerHTML = `Car A: <b>${vA} m/s</b> | Car B: <b>${Math.abs(vB)} m/s (${isOpposite ? 'Opposite' : 'Same'})</b> ➔ Relative Velocity: <span style="color:#f59e0b; font-weight:700;">v_AB = v_A − v_B = ${v_rel.toFixed(1)} m/s</span>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllStraightLine3D() {
    initSlopeTangentSimulation();
    initAcceleratedMotionSimulation();
    initVerticalFreeFallSimulation();
    initRelativeMotion1DSimulation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllStraightLine3D);
  } else {
    initAllStraightLine3D();
  }
})();
