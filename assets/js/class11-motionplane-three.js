/**
 * SJMaths - Class 11 Physics Chapter 3: Motion in a Plane
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. 3D Vector Resolution & Parallelogram Law (Components Ax, Ay, Az, resultant R = sqrt(A^2 + B^2 + 2AB cosθ))
 * 2. Relative Velocity & Rain-Man / River-Boat 3D Vector Simulator (v_rm = v_r - v_m, umbrella angle calculation)
 * 3. 3D Projectile Trajectory & Range Simulator (Parabolic path, maximum height, flight time, complementary angles)
 * 4. Uniform Circular Motion & Centripetal Acceleration (Tangential velocity v, centripetal ac = v^2/R, frequency & period)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Chapter 3. Retrying on load.");
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

    window.addEventListener('touchmove', (e) => {
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
     1. SIMULATION: 3D Vector Resolution & Parallelogram Addition
     ========================================================================= */
  function initVectorAdditionSimulation() {
    const setup = create3DCanvas('three-vector-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 14, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Vector A (along +x)
    const arrowA = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 8.0, THEME.blue, 1.0, 0.5);
    group.add(arrowA);

    // Vector B (at angle theta)
    const arrowB = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 6.0, THEME.rose, 1.0, 0.5);
    group.add(arrowB);

    // Resultant Vector R = A + B (Parallelogram diagonal)
    const arrowR = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 12.0, THEME.gold, 1.2, 0.6);
    group.add(arrowR);

    // Parallelogram dashed helper lines
    const lineMat = new THREE.LineDashedMaterial({ color: 0x64748b, dashSize: 0.4, gapSize: 0.2 });
    const paraGeo = new THREE.BufferGeometry();
    const paraLines = new THREE.LineSegments(paraGeo, lineMat);
    group.add(paraLines);

    const magASlider = document.getElementById('vec-a-slider');
    const magBSlider = document.getElementById('vec-b-slider');
    const thetaSlider = document.getElementById('vec-theta-slider');
    const vecHudText = document.getElementById('vec-result-display');

    function updateVectors() {
      const A = magASlider ? parseFloat(magASlider.value) : 7.0;
      const B = magBSlider ? parseFloat(magBSlider.value) : 5.0;
      const thetaDeg = thetaSlider ? parseFloat(thetaSlider.value) : 60;
      const thetaRad = (thetaDeg * Math.PI) / 180;

      arrowA.setLength(A, 0.8, 0.4);

      const bDir = new THREE.Vector3(Math.cos(thetaRad), Math.sin(thetaRad), 0);
      arrowB.setDirection(bDir);
      arrowB.setLength(B, 0.8, 0.4);

      // Resultant Vector R
      const rx = A + B * Math.cos(thetaRad);
      const ry = B * Math.sin(thetaRad);
      const R_mag = Math.sqrt(rx * rx + ry * ry);
      const rDir = new THREE.Vector3(rx, ry, 0).normalize();

      arrowR.setDirection(rDir);
      arrowR.setLength(R_mag, 1.0, 0.5);

      // Dashed lines to form parallelogram
      const posA = new THREE.Vector3(A, 0, 0);
      const posB = new THREE.Vector3(B * Math.cos(thetaRad), B * Math.sin(thetaRad), 0);
      const posR = new THREE.Vector3(rx, ry, 0);

      paraLines.geometry.setFromPoints([
        posA, posR,
        posB, posR
      ]);
      paraLines.computeLineDistances();

      const alphaDeg = (Math.atan2(ry, rx) * 180) / Math.PI;

      if (vecHudText) {
        vecHudText.innerHTML = `Resultant |<b>R</b>| = √(A² + B² + 2AB cosθ) = <span style="color:#f59e0b; font-weight:700;">${R_mag.toFixed(2)} units</span> &bull; Angle with <b>A</b>: α = ${alphaDeg.toFixed(1)}°`;
      }
    }

    [magASlider, magBSlider, thetaSlider].forEach(sl => {
      if (sl) sl.addEventListener('input', updateVectors);
    });
    updateVectors();

    function animate() {
      requestAnimationFrame(animate);
      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     2. SIMULATION: Relative Velocity & Rain-Man Vector Simulator
     ========================================================================= */
  function initRelativeVelocitySimulation() {
    const setup = create3DCanvas('three-relvel-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Rain Streaks Particle System
    const rainCount = 400;
    const rainGeo = new THREE.BufferGeometry();
    const rainPositions = new Float32Array(rainCount * 3);
    for (let i = 0; i < rainCount * 3; i += 3) {
      rainPositions[i] = (Math.random() - 0.5) * 24;
      rainPositions[i + 1] = Math.random() * 16 - 4;
      rainPositions[i + 2] = (Math.random() - 0.5) * 16;
    }
    rainGeo.setAttribute('position', new THREE.BufferAttribute(rainPositions, 3));
    const rainMat = new THREE.PointsMaterial({ color: 0x38bdf8, size: 0.25, transparent: true, opacity: 0.7 });
    const rainParticles = new THREE.Points(rainGeo, rainMat);
    group.add(rainParticles);

    // Walking Stick-Figure / Cyclist Base
    const manMesh = new THREE.Mesh(
      new THREE.CylinderGeometry(0.5, 0.5, 2.0, 16),
      new THREE.MeshStandardMaterial({ color: THEME.gold })
    );
    manMesh.position.set(0, -2, 0);
    group.add(manMesh);

    // Umbrella
    const umbrellaGeo = new THREE.ConeGeometry(2.0, 1.0, 16, 1, true);
    const umbrellaMat = new THREE.MeshStandardMaterial({ color: THEME.rose, side: THREE.DoubleSide });
    const umbrella = new THREE.Mesh(umbrellaGeo, umbrellaMat);
    umbrella.position.set(0, -0.5, 0);
    group.add(umbrella);

    // Velocity Vectors
    const vRainArrow = new THREE.ArrowHelper(new THREE.Vector3(0, -1, 0), new THREE.Vector3(4, 3, 0), 4.0, THEME.blue, 0.8, 0.4);
    group.add(vRainArrow);

    const vManArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(4, 3, 0), 3.0, THEME.gold, 0.6, 0.3);
    group.add(vManArrow);

    const vRelArrow = new THREE.ArrowHelper(new THREE.Vector3(-0.6, -0.8, 0), new THREE.Vector3(4, 3, 0), 5.0, THEME.rose, 0.8, 0.4);
    group.add(vRelArrow);

    const vManSlider = document.getElementById('rel-vman-slider');
    const vRainSlider = document.getElementById('rel-vrain-slider');
    const relHudText = document.getElementById('rel-hud-display');

    function animate() {
      requestAnimationFrame(animate);

      const vMan = vManSlider ? parseFloat(vManSlider.value) : 10;
      const vRain = vRainSlider ? parseFloat(vRainSlider.value) : 25;

      // Animate falling rain relative to man
      const positions = rainGeo.attributes.position.array;
      for (let i = 1; i < rainCount * 3; i += 3) {
        positions[i] -= vRain * 0.008;
        positions[i - 1] -= vMan * 0.008; // Apparent drift
        if (positions[i] < -4) {
          positions[i] = 12;
          positions[i - 1] = (Math.random() - 0.5) * 24;
        }
      }
      rainGeo.attributes.position.needsUpdate = true;

      // Relative Velocity: v_rm = v_r - v_m = (0 i - vRain j) - (vMan i) = -vMan i - vRain j
      const thetaRad = Math.atan2(vMan, vRain);
      const thetaDeg = (thetaRad * 180) / Math.PI;

      // Tilt umbrella into relative rain angle
      umbrella.rotation.z = -thetaRad;

      // Vector arrows update
      vRainArrow.setLength(vRain * 0.15, 0.6, 0.3);
      vManArrow.setLength(vMan * 0.25, 0.6, 0.3);

      const vRelDir = new THREE.Vector3(-vMan, -vRain, 0).normalize();
      const vRelMag = Math.sqrt(vMan * vMan + vRain * vRain);
      vRelArrow.setDirection(vRelDir);
      vRelArrow.setLength(vRelMag * 0.15, 0.8, 0.4);

      if (relHudText) {
        relHudText.innerHTML = `Relative Speed: |<b>v</b><sub>r,m</sub>| = √(v<sub>r</sub>² + v<sub>m</sub>²) = <span style="color:#f43f5e; font-weight:700;">${vRelMag.toFixed(1)} m/s</span> &bull; Umbrella Tilt: <span style="color:#f59e0b; font-weight:700;">θ = tan⁻¹(v<sub>m</sub>/v<sub>r</sub>) = ${thetaDeg.toFixed(1)}°</span> with vertical`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     3. SIMULATION: 3D Projectile Trajectory & Range Simulator
     ========================================================================= */
  function initProjectileSimulation() {
    const setup = create3DCanvas('three-projectile-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 12, 28);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Ground line / grid
    const groundGeo = new THREE.BoxGeometry(32, 0.2, 8);
    const groundMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
    const ground = new THREE.Mesh(groundGeo, groundMat);
    ground.position.set(0, -3, 0);
    group.add(ground);

    // Cannon Barrel
    const cannonGeo = new THREE.CylinderGeometry(0.5, 0.6, 2.5, 16);
    cannonGeo.translate(0, 1.25, 0);
    const cannonMat = new THREE.MeshStandardMaterial({ color: THEME.metal, metalness: 0.6 });
    const cannon = new THREE.Mesh(cannonGeo, cannonMat);
    cannon.position.set(-14, -3, 0);
    group.add(cannon);

    // Projectile Ball
    const ball = new THREE.Mesh(
      new THREE.SphereGeometry(0.6, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.rose, emissive: 0xe11d48, emissiveIntensity: 0.4 })
    );
    group.add(ball);

    // Trajectory Path Curve
    let pathMesh;
    function updateTrajectoryPath(v0, thetaDeg) {
      if (pathMesh) {
        group.remove(pathMesh);
        pathMesh.geometry.dispose();
      }
      const g = 9.8;
      const thetaRad = (thetaDeg * Math.PI) / 180;
      const v0x = v0 * Math.cos(thetaRad);
      const v0y = v0 * Math.sin(thetaRad);
      const T = (2 * v0y) / g;

      const points = [];
      for (let step = 0; step <= 60; step++) {
        const t = (step / 60) * T;
        const px = -14 + v0x * t;
        const py = -3 + v0y * t - 0.5 * g * t * t;
        points.push(new THREE.Vector3(px, Math.max(-3, py), 0));
      }
      const curve = new THREE.CatmullRomCurve3(points);
      pathMesh = new THREE.Mesh(
        new THREE.TubeGeometry(curve, 60, 0.08, 6, false),
        new THREE.MeshBasicMaterial({ color: THEME.cyan })
      );
      group.add(pathMesh);
    }

    let time = 0;
    let v0 = 16.0;
    let angleDeg = 45;

    const angleSlider = document.getElementById('proj-angle-slider');
    const speedSlider = document.getElementById('proj-speed-slider');
    const fireBtn = document.getElementById('proj-fire-btn');
    const projHudText = document.getElementById('proj-hud-display');

    function resetLaunch() {
      time = 0;
    }

    if (fireBtn) fireBtn.addEventListener('click', resetLaunch);

    function animate() {
      requestAnimationFrame(animate);

      const deg = angleSlider ? parseFloat(angleSlider.value) : angleDeg;
      const speed = speedSlider ? parseFloat(speedSlider.value) : v0;

      cannon.rotation.z = -((90 - deg) * Math.PI) / 180;

      const g = 9.8;
      const thetaRad = (deg * Math.PI) / 180;
      const v0x = speed * Math.cos(thetaRad);
      const v0y = speed * Math.sin(thetaRad);
      const T_f = (2 * v0y) / g;
      const H_max = (v0y * v0y) / (2 * g);
      const Range = (speed * speed * Math.sin(2 * thetaRad)) / g;

      updateTrajectoryPath(speed, deg);

      time += 0.03;
      if (time > T_f) {
        time = 0;
      }

      const bx = -14 + v0x * time;
      const by = -3 + v0y * time - 0.5 * g * time * time;
      ball.position.set(bx, Math.max(-3, by), 0);

      if (projHudText) {
        projHudText.innerHTML = `Range: <b style="color:#10b981;">R = ${Range.toFixed(1)}m</b> | Max Height: <b style="color:#38bdf8;">hₘ = ${H_max.toFixed(1)}m</b> | Flight Time: <b style="color:#f59e0b;">T = ${T_f.toFixed(2)}s</b>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     4. SIMULATION: Uniform Circular Motion & Centripetal Acceleration
     ========================================================================= */
  function initCircularMotionSimulation() {
    const setup = create3DCanvas('three-circmotion-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 16, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    const R = 8.0;

    // Circular Orbit Track
    const orbitGeo = new THREE.RingGeometry(R - 0.06, R + 0.06, 64);
    const orbitMat = new THREE.MeshBasicMaterial({ color: 0x334155, side: THREE.DoubleSide });
    const orbitMesh = new THREE.Mesh(orbitGeo, orbitMat);
    orbitMesh.rotation.x = Math.PI / 2;
    group.add(orbitMesh);

    // Centre Pivot
    const pivot = new THREE.Mesh(
      new THREE.CylinderGeometry(0.4, 0.4, 1.0, 16),
      new THREE.MeshStandardMaterial({ color: THEME.metal })
    );
    group.add(pivot);

    // Orbiting Particle
    const particle = new THREE.Mesh(
      new THREE.SphereGeometry(0.8, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.emerald, roughness: 0.3 })
    );
    group.add(particle);

    // Tangential Velocity Vector Arrow (v)
    const vArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.blue, 0.8, 0.4);
    group.add(vArrow);

    // Centripetal Acceleration Vector Arrow (a_c towards centre)
    const aArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.rose, 0.8, 0.4);
    group.add(aArrow);

    let angle = 0;
    const omegaSlider = document.getElementById('circ-omega-slider');
    const circHudText = document.getElementById('circ-hud-display');

    function animate() {
      requestAnimationFrame(animate);

      const omega = omegaSlider ? parseFloat(omegaSlider.value) : 1.5;
      angle += omega * 0.015;

      const px = R * Math.cos(angle);
      const pz = R * Math.sin(angle);
      particle.position.set(px, 0, pz);

      // Tangential velocity vector (-sin θ, 0, cos θ)
      const tDir = new THREE.Vector3(-Math.sin(angle), 0, Math.cos(angle)).normalize();
      vArrow.position.set(px, 0.8, pz);
      vArrow.setDirection(tDir);
      vArrow.setLength(omega * 2.2, 0.6, 0.3);

      // Centripetal acceleration vector directed strictly towards origin (0, 0, 0)
      const cDir = new THREE.Vector3(-px, 0, -pz).normalize();
      aArrow.position.set(px, 0.8, pz);
      aArrow.setDirection(cDir);
      const a_c = omega * omega * R;
      aArrow.setLength(Math.min(7, a_c * 0.3), 0.8, 0.4);

      if (circHudText) {
        const v = omega * R;
        circHudText.innerHTML = `Angular Speed: <b>${omega.toFixed(1)} rad/s</b> &bull; Linear Speed: <span style="color:#38bdf8; font-weight:700;">v = ωR = ${v.toFixed(1)} m/s</span> &bull; Centripetal Acc: <span style="color:#f43f5e; font-weight:700;">a_c = v²/R = ${a_c.toFixed(1)} m/s²</span>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllMotionInPlane3D() {
    initVectorAdditionSimulation();
    initRelativeVelocitySimulation();
    initProjectileSimulation();
    initCircularMotionSimulation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllMotionInPlane3D);
  } else {
    initAllMotionInPlane3D();
  }
})();
