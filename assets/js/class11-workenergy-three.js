/**
 * SJMaths - Class 11 Physics Chapter 5: Work, Energy and Power
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. 3D Work Done & Scalar Dot Product (W = F . d = F d cos(theta), positive, zero, and negative work)
 * 2. Motion in a Vertical Circle & Energy Transformation (Potential vs Kinetic, minimum looping speeds sqrt(5gL))
 * 3. Spring Potential Energy & Harmonic Oscillation (Hooke's Law F = -kx, parabolic energy well V(x)=1/2 k x^2)
 * 4. 3D Elastic & Inelastic Collision Dynamics (1D/2D momentum & kinetic energy exchange with variable coefficient of restitution e)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Chapter 5. Retrying on load.");
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
     1. SIMULATION: 3D Work Done & Scalar Dot Product (W = F . d = F d cosθ)
     ========================================================================= */
  function initWorkDotSimulation() {
    const setup = create3DCanvas('three-work-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 14, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Block on a flat surface
    const blockGeo = new THREE.BoxGeometry(3.0, 2.0, 3.0);
    const blockMat = new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.35 });
    const block = new THREE.Mesh(blockGeo, blockMat);
    block.position.set(0, -1.0, 0);
    group.add(block);

    // Displacement Vector d (Along +x direction)
    const arrowD = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, -1, 0), 8.0, THEME.emerald, 1.0, 0.5);
    group.add(arrowD);

    // Force Vector F (Applied at centre of block)
    const arrowF = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 7.0, THEME.rose, 1.0, 0.5);
    group.add(arrowF);

    // Force Projection Component F cos(theta) dashed arrow
    const arrowProj = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 7.0, THEME.gold, 0.8, 0.4);
    group.add(arrowProj);

    const angleSlider = document.getElementById('work-angle-slider');
    const forceSlider = document.getElementById('work-force-slider');
    const dispSlider = document.getElementById('work-disp-slider');
    const workValText = document.getElementById('work-val-display');

    function updateWork() {
      const thetaDeg = angleSlider ? parseFloat(angleSlider.value) : 45;
      const F_mag = forceSlider ? parseFloat(forceSlider.value) : 10;
      const d_mag = dispSlider ? parseFloat(dispSlider.value) : 6;

      const thetaRad = (thetaDeg * Math.PI) / 180;
      const W = F_mag * d_mag * Math.cos(thetaRad);

      arrowD.setLength(d_mag, 0.8, 0.4);

      // Force Vector direction in xy plane
      const fDir = new THREE.Vector3(Math.cos(thetaRad), Math.sin(thetaRad), 0).normalize();
      arrowF.setDirection(fDir);
      arrowF.setLength(F_mag * 0.5, 0.8, 0.4);

      // Projection length along x
      const projLength = Math.max(0.1, Math.abs(F_mag * Math.cos(thetaRad)) * 0.5);
      const projDir = new THREE.Vector3(Math.cos(thetaRad) >= 0 ? 1 : -1, 0, 0);
      arrowProj.setDirection(projDir);
      arrowProj.setLength(projLength, 0.6, 0.3);

      let nature = "Positive Work (W > 0, θ < 90°)";
      let color = "#10b981";
      if (Math.abs(thetaDeg - 90) < 1) {
        nature = "Zero Work (W = 0, θ = 90°)";
        color = "#94a3b8";
      } else if (thetaDeg > 90) {
        nature = "Negative Work (W < 0, θ > 90°)";
        color = "#f43f5e";
      }

      if (workValText) {
        workValText.innerHTML = `W = F d cosθ = (${F_mag.toFixed(0)}N) × (${d_mag.toFixed(1)}m) × cos(${thetaDeg}°) = <span style="color:${color}; font-weight:700;">${W.toFixed(2)} J</span> &bull; <i>${nature}</i>`;
      }
    }

    [angleSlider, forceSlider, dispSlider].forEach(sl => {
      if (sl) sl.addEventListener('input', updateWork);
    });
    updateWork();

    function animate() {
      requestAnimationFrame(animate);
      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     2. SIMULATION: Motion in a Vertical Circle & Energy Transformation
     ========================================================================= */
  function initVerticalCircleSimulation() {
    const setup = create3DCanvas('three-vertcircle-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    const radius = 6.0;

    // Circular Orbit Ring Guide
    const ringGeo = new THREE.RingGeometry(radius - 0.05, radius + 0.05, 64);
    const ringMat = new THREE.MeshBasicMaterial({ color: 0x334155, side: THREE.DoubleSide });
    const ringMesh = new THREE.Mesh(ringGeo, ringMat);
    group.add(ringMesh);

    // Central Pivot Pin
    const pivot = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 1.0, 16), new THREE.MeshStandardMaterial({ color: THEME.metal }));
    pivot.rotation.x = Math.PI / 2;
    group.add(pivot);

    // String Line
    const stringGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, -radius, 0)]);
    const stringMat = new THREE.LineBasicMaterial({ color: 0xf8fafc, linewidth: 2 });
    const stringLine = new THREE.Line(stringGeo, stringMat);
    group.add(stringLine);

    // Bob
    const bob = new THREE.Mesh(new THREE.SphereGeometry(0.8, 32, 32), new THREE.MeshStandardMaterial({ color: THEME.purple, roughness: 0.3 }));
    group.add(bob);

    // Velocity Vector Arrow
    const velArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 3.0, THEME.rose, 0.8, 0.4);
    group.add(velArrow);

    let angle = -Math.PI / 2; // Starts at lowest point A
    let isPlaying = true;
    let g = 9.8;
    let L = radius;
    let v0 = Math.sqrt(5 * g * L) * 0.95; // Initial bottom velocity near critical looping

    const playBtn = document.getElementById('vert-play-btn');
    const modeSelect = document.getElementById('vert-mode-select');
    const speedDisplay = document.getElementById('vert-speed-display');
    const energyDisplay = document.getElementById('vert-energy-display');

    if (playBtn) {
      playBtn.addEventListener('click', () => {
        isPlaying = !isPlaying;
        playBtn.innerHTML = isPlaying ? '<i class="fas fa-pause"></i> Pause' : '<i class="fas fa-play"></i> Play';
      });
    }

    if (modeSelect) {
      modeSelect.addEventListener('change', () => {
        const val = modeSelect.value;
        if (val === 'loop') v0 = Math.sqrt(5 * g * L) * 1.05; // Full loop
        else if (val === 'semi') v0 = Math.sqrt(2.5 * g * L); // Oscillation / slackens
        else if (val === 'slack') v0 = Math.sqrt(3.6 * g * L); // Leaves circle
      });
    }

    function animate() {
      requestAnimationFrame(animate);

      if (isPlaying) {
        // Height h relative to lowest point
        const h = radius * (1 + Math.sin(angle));
        // Energy conservation: 1/2 m v^2 + m g h = 1/2 m v0^2
        const vSq = v0 * v0 - 2 * g * h;
        let v = Math.sqrt(Math.max(0.1, vSq));
        let omega = v / radius;

        angle += omega * 0.015;

        // Position of Bob
        const bx = radius * Math.cos(angle);
        const by = radius * Math.sin(angle);
        bob.position.set(bx, by, 0);

        stringLine.geometry.setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(bx, by, 0)]);

        // Velocity direction (tangential)
        const tDir = new THREE.Vector3(-Math.sin(angle), Math.cos(angle), 0).normalize();
        velArrow.position.set(bx, by, 0.5);
        velArrow.setDirection(tDir);
        velArrow.setLength(Math.max(0.5, v * 0.35), 0.6, 0.3);

        const PE = g * h;
        const KE = 0.5 * vSq;

        if (speedDisplay) speedDisplay.textContent = `${v.toFixed(1)} m/s (h = ${h.toFixed(1)}m)`;
        if (energyDisplay) energyDisplay.innerHTML = `KE: <span style="color:#10b981;">${KE.toFixed(0)} J</span> | PE: <span style="color:#a855f7;">${PE.toFixed(0)} J</span>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     3. SIMULATION: Spring Potential Energy & Harmonic Oscillation
     ========================================================================= */
  function initSpringSimulation() {
    const setup = create3DCanvas('three-spring-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Left Rigid Fixed Wall
    const wallGeo = new THREE.BoxGeometry(0.8, 6.0, 6.0);
    const wallMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.6 });
    const wall = new THREE.Mesh(wallGeo, wallMat);
    wall.position.set(-9, 0, 0);
    group.add(wall);

    // Oscillating Mass Block
    const blockGeo = new THREE.BoxGeometry(2.5, 2.5, 2.5);
    const blockMat = new THREE.MeshStandardMaterial({ color: THEME.cyan, roughness: 0.3 });
    const block = new THREE.Mesh(blockGeo, blockMat);
    group.add(block);

    // Spring Helix Mesh
    let springMesh;
    function createSpringHelix(length) {
      const points = [];
      const coils = 12;
      const radius = 1.0;
      const totalPoints = 180;
      for (let i = 0; i <= totalPoints; i++) {
        const t = i / totalPoints;
        const x = -8.6 + t * length;
        const y = Math.sin(t * coils * Math.PI * 2) * radius;
        const z = Math.cos(t * coils * Math.PI * 2) * radius;
        points.push(new THREE.Vector3(x, y, z));
      }
      const curve = new THREE.CatmullRomCurve3(points);
      return new THREE.Mesh(
        new THREE.TubeGeometry(curve, 120, 0.1, 8, false),
        new THREE.MeshStandardMaterial({ color: THEME.gold, metalness: 0.5 })
      );
    }

    springMesh = createSpringHelix(8.6);
    group.add(springMesh);

    let time = 0;
    let amplitude = 4.0;
    let k = 100;
    let m = 2.0;

    const ampSlider = document.getElementById('spring-amp-slider');
    const kSlider = document.getElementById('spring-k-slider');
    const energyText = document.getElementById('spring-energy-display');

    function animate() {
      requestAnimationFrame(animate);

      const amp = ampSlider ? parseFloat(ampSlider.value) : amplitude;
      const kVal = kSlider ? parseFloat(kSlider.value) : k;
      const omega = Math.sqrt(kVal / m);

      time += 0.03;
      const xDisp = amp * Math.cos(omega * time);
      const blockX = xDisp;

      block.position.set(blockX, 0, 0);

      // Rebuild spring tube with updated length
      group.remove(springMesh);
      springMesh.geometry.dispose();
      springMesh = createSpringHelix(blockX + 8.6);
      group.add(springMesh);

      const PE = 0.5 * kVal * xDisp * xDisp;
      const totalE = 0.5 * kVal * amp * amp;
      const KE = Math.max(0, totalE - PE);

      if (energyText) {
        energyText.innerHTML = `x = ${xDisp.toFixed(2)}m &bull; PE = <span style="color:#f59e0b;">${PE.toFixed(1)} J</span> | KE = <span style="color:#10b981;">${KE.toFixed(1)} J</span> | Total: ${totalE.toFixed(1)} J`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     4. SIMULATION: 3D 1D/2D Elastic & Inelastic Collisions
     ========================================================================= */
  function initCollisionSimulation() {
    const setup = create3DCanvas('three-collision-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 14, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Sphere 1 (Striking body)
    const sphere1 = new THREE.Mesh(
      new THREE.SphereGeometry(1.2, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.rose, roughness: 0.3 })
    );
    group.add(sphere1);

    // Sphere 2 (Target body)
    const sphere2 = new THREE.Mesh(
      new THREE.SphereGeometry(1.2, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.emerald, roughness: 0.3 })
    );
    group.add(sphere2);

    let pos1 = -10.0;
    let pos2 = 0.0;
    let v1 = 0.2;
    let v2 = 0.0;
    let hasCollided = false;

    const m1Slider = document.getElementById('col-m1-slider');
    const m2Slider = document.getElementById('col-m2-slider');
    const eSlider = document.getElementById('col-e-slider');
    const triggerBtn = document.getElementById('col-fire-btn');
    const colStatusText = document.getElementById('col-status-display');

    function resetSimulation() {
      pos1 = -10.0;
      pos2 = 0.0;
      v1 = 0.22;
      v2 = 0.0;
      hasCollided = false;
    }

    if (triggerBtn) {
      triggerBtn.addEventListener('click', resetSimulation);
    }

    function animate() {
      requestAnimationFrame(animate);

      const m1 = m1Slider ? parseFloat(m1Slider.value) : 1.0;
      const m2 = m2Slider ? parseFloat(m2Slider.value) : 1.0;
      const e = eSlider ? parseFloat(eSlider.value) : 1.0;

      sphere1.scale.setScalar(0.7 + m1 * 0.3);
      sphere2.scale.setScalar(0.7 + m2 * 0.3);

      pos1 += v1;
      pos2 += v2;

      // Detect Impact
      const touchDist = (0.7 + m1 * 0.3) + (0.7 + m2 * 0.3);
      if (!hasCollided && (pos2 - pos1) <= touchDist) {
        hasCollided = true;
        // 1D Collision Velocity Equations with coefficient of restitution e
        const u1 = v1;
        const u2 = v2;
        const v1_f = ((m1 - e * m2) * u1 + (1 + e) * m2 * u2) / (m1 + m2);
        const v2_f = ((1 + e) * m1 * u1 + (m2 - e * m1) * u2) / (m1 + m2);
        v1 = v1_f;
        v2 = v2_f;

        if (colStatusText) {
          colStatusText.innerHTML = `Post-Collision: <b>v<sub>1f</sub> = ${(v1 * 50).toFixed(1)} m/s</b>, <b>v<sub>2f</sub> = ${(v2 * 50).toFixed(1)} m/s</b> (restitution e = ${e.toFixed(2)})`;
        }
      }

      if (pos1 > 16 || pos2 > 16 || pos1 < -16) {
        resetSimulation();
      }

      sphere1.position.set(pos1, 0, 0);
      sphere2.position.set(pos2, 0, 0);

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllWorkEnergy3D() {
    initWorkDotSimulation();
    initVerticalCircleSimulation();
    initSpringSimulation();
    initCollisionSimulation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllWorkEnergy3D);
  } else {
    initAllWorkEnergy3D();
  }
})();
