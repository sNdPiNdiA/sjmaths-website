/**
 * SJMaths - Class 11 Physics Chapter 6: Systems of Particles & Rotational Motion
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. Centre of Mass of Discrete & Continuous 3D Systems (Multi-particle cluster with dynamic mass weighting)
 * 2. 3D Vector Cross Product & Torque Simulator (r x F = tau, right-hand rule, moment arm)
 * 3. Moment of Inertia & Geometry Inspector (Ring, Disc, Solid Cylinder, Solid Sphere, Hollow Sphere comparison)
 * 4. Pure Rolling Motion on an Inclined Plane (Translation + Rotation superposition, contact point v=0)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Chapter 6. Retrying on load.");
    return;
  }

  // --- Theme Colors ---
  const THEME = {
    spaceDark: 0x090d16,
    gold: 0xf59e0b,
    blue: 0x38bdf8,
    emerald: 0x10b981,
    purple: 0xa855f7,
    rose: 0xf43f5e,
    cyan: 0x06b6d4,
    metal: 0x64748b,
    white: 0xffffff,
    wood: 0xb45309
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

    // Subtle grid/stars
    const gridHelper = new THREE.GridHelper(30, 20, 0x334155, 0x1e293b);
    gridHelper.position.y = -4;
    scene.add(gridHelper);

    // Lighting
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.75);
    scene.add(ambientLight);
    const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(12, 20, 15);
    scene.add(dirLight);

    // Interactive mouse drag
    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };
    let rotation = { x: 0.35, y: 0.5 };

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

    // Touch support
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
     1. SIMULATION: Centre of Mass (CM) of Discrete 3D Particle Cluster
     ========================================================================= */
  function initCentreOfMassSimulation() {
    const setup = create3DCanvas('three-cm-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 14, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // 3 Discrete Particles on an Equilateral Triangle Frame
    const posA = new THREE.Vector3(-6, 0, -3.5);
    const posB = new THREE.Vector3(6, 0, -3.5);
    const posC = new THREE.Vector3(0, 0, 6.8);

    // Connecting Rods
    const frameGeo = new THREE.BufferGeometry().setFromPoints([
      posA, posB, posB, posC, posC, posA
    ]);
    const frameMat = new THREE.LineBasicMaterial({ color: 0x475569, linewidth: 2 });
    group.add(new THREE.LineSegments(frameGeo, frameMat));

    // Particle Meshes
    function makeMassSphere(color) {
      return new THREE.Mesh(
        new THREE.SphereGeometry(1.0, 32, 32),
        new THREE.MeshStandardMaterial({ color, roughness: 0.3 })
      );
    }

    const sphereA = makeMassSphere(THEME.blue);
    sphereA.position.copy(posA);
    group.add(sphereA);

    const sphereB = makeMassSphere(THEME.purple);
    sphereB.position.copy(posB);
    group.add(sphereB);

    const sphereC = makeMassSphere(THEME.emerald);
    sphereC.position.copy(posC);
    group.add(sphereC);

    // Centre of Mass Indicator Sphere (Glowing Gold)
    const cmSphere = new THREE.Mesh(
      new THREE.SphereGeometry(0.7, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.gold, emissive: 0xd97706, emissiveIntensity: 0.8 })
    );
    group.add(cmSphere);

    // Dashed lines from CM to particles
    const lineMat = new THREE.LineDashedMaterial({ color: 0xf59e0b, dashSize: 0.4, gapSize: 0.2 });
    const cmLinesGeo = new THREE.BufferGeometry();
    const cmLines = new THREE.LineSegments(cmLinesGeo, lineMat);
    group.add(cmLines);

    // Slider Controls
    const sliderA = document.getElementById('cm-mass-a');
    const sliderB = document.getElementById('cm-mass-b');
    const sliderC = document.getElementById('cm-mass-c');
    const cmCoordText = document.getElementById('cm-coord-display');

    function updateCM() {
      const mA = sliderA ? parseFloat(sliderA.value) : 1.0;
      const mB = sliderB ? parseFloat(sliderB.value) : 1.0;
      const mC = sliderC ? parseFloat(sliderC.value) : 1.0;

      // Scale spheres to represent mass
      sphereA.scale.setScalar(0.7 + mA * 0.25);
      sphereB.scale.setScalar(0.7 + mB * 0.25);
      sphereC.scale.setScalar(0.7 + mC * 0.25);

      const totalM = mA + mB + mC;
      const cmX = (mA * posA.x + mB * posB.x + mC * posC.x) / totalM;
      const cmY = (mA * posA.y + mB * posB.y + mC * posC.y) / totalM;
      const cmZ = (mA * posA.z + mB * posB.z + mC * posC.z) / totalM;

      cmSphere.position.set(cmX, cmY, cmZ);

      // Update dashed lines
      const linePts = [
        new THREE.Vector3(cmX, cmY, cmZ), posA,
        new THREE.Vector3(cmX, cmY, cmZ), posB,
        new THREE.Vector3(cmX, cmY, cmZ), posC
      ];
      cmLines.geometry.setFromPoints(linePts);
      cmLines.computeLineDistances();

      if (cmCoordText) {
        cmCoordText.textContent = `(${cmX.toFixed(2)}, ${cmZ.toFixed(2)}) • Total Mass: ${totalM.toFixed(1)} kg`;
      }
    }

    [sliderA, sliderB, sliderC].forEach(sl => {
      if (sl) sl.addEventListener('input', updateCM);
    });

    updateCM();

    function animate() {
      requestAnimationFrame(animate);
      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     2. SIMULATION: Vector Cross Product & Torque (τ = r × F)
     ========================================================================= */
  function initTorqueSimulation() {
    const setup = create3DCanvas('three-torque-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 16, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Pivot Origin (Fulcrum)
    const pivotGeo = new THREE.CylinderGeometry(0.8, 0.8, 2.0, 32);
    const pivotMat = new THREE.MeshStandardMaterial({ color: THEME.metal, metalness: 0.6 });
    const pivot = new THREE.Mesh(pivotGeo, pivotMat);
    group.add(pivot);

    // Lever Arm / Wrench
    const leverLength = 10;
    const leverGeo = new THREE.BoxGeometry(leverLength, 0.4, 0.8);
    leverGeo.translate(leverLength / 2, 0, 0);
    const leverMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.4 });
    const lever = new THREE.Mesh(leverGeo, leverMat);
    group.add(lever);

    // Vector r (Position vector arrow along lever)
    const arrowR = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), leverLength, THEME.blue, 1.0, 0.5);
    group.add(arrowR);

    // Force Vector F arrow (Applied at tip of lever)
    const arrowF = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(leverLength, 0, 0), 5, THEME.rose, 1.0, 0.5);
    group.add(arrowF);

    // Torque Vector τ = r × F (Points along z-axis / perpendicular to plane)
    const arrowTau = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), new THREE.Vector3(0, 0, 0), 6, THEME.gold, 1.2, 0.6);
    group.add(arrowTau);

    // UI Sliders
    const angleSlider = document.getElementById('torque-angle-slider');
    const forceSlider = document.getElementById('torque-force-slider');
    const armSlider = document.getElementById('torque-arm-slider');
    const torqueValText = document.getElementById('torque-val-display');

    function updateTorque() {
      const thetaDeg = angleSlider ? parseFloat(angleSlider.value) : 90;
      const F_mag = forceSlider ? parseFloat(forceSlider.value) : 10;
      const r_mag = armSlider ? parseFloat(armSlider.value) : 8;

      const thetaRad = (thetaDeg * Math.PI) / 180;
      const tau = r_mag * F_mag * Math.sin(thetaRad);

      // Update Lever & r vector
      lever.scale.set(r_mag / leverLength, 1, 1);
      arrowR.setLength(r_mag, 0.8, 0.4);

      // Force Vector direction in xy plane
      const fDir = new THREE.Vector3(Math.cos(thetaRad), Math.sin(thetaRad), 0).normalize();
      arrowF.position.set(r_mag, 0, 0);
      arrowF.setDirection(fDir);
      arrowF.setLength(F_mag * 0.4, 0.8, 0.4);

      // Torque Vector (out of plane, +z or -z)
      const tauDir = new THREE.Vector3(0, 0, Math.sin(thetaRad) >= 0 ? 1 : -1);
      arrowTau.setDirection(tauDir);
      arrowTau.setLength(Math.max(0.5, Math.abs(tau) * 0.12), 1.0, 0.5);

      if (torqueValText) {
        torqueValText.textContent = `|τ| = r F sinθ = (${r_mag.toFixed(1)}m) × (${F_mag.toFixed(0)}N) × sin(${thetaDeg}°) = ${tau.toFixed(2)} N m`;
      }
    }

    [angleSlider, forceSlider, armSlider].forEach(sl => {
      if (sl) sl.addEventListener('input', updateTorque);
    });

    updateTorque();

    function animate() {
      requestAnimationFrame(animate);
      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     3. SIMULATION: Moments of Inertia of Standard Geometries
     ========================================================================= */
  function initMomentOfInertiaSimulation() {
    const setup = create3DCanvas('three-moi-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 12, 18);
    camera.lookAt(0, 0, 0);

    const bodyGroup = new THREE.Group();
    scene.add(bodyGroup);

    // Rotation Axis Line
    const axisGeo = new THREE.CylinderGeometry(0.12, 0.12, 16, 16);
    const axisMat = new THREE.MeshBasicMaterial({ color: THEME.gold });
    const axisMesh = new THREE.Mesh(axisGeo, axisMat);
    scene.add(axisMesh);

    // Geometries Library
    const R = 4.5;
    const geometries = {
      ring: new THREE.TorusGeometry(R, 0.4, 16, 64),
      disc: new THREE.CylinderGeometry(R, R, 0.5, 64),
      solid_cylinder: new THREE.CylinderGeometry(R, R, 5.0, 32),
      hollow_cylinder: new THREE.CylinderGeometry(R, R, 5.0, 32, 1, true),
      solid_sphere: new THREE.SphereGeometry(R, 32, 32),
      rod: new THREE.CylinderGeometry(0.35, 0.35, 12.0, 16)
    };

    const mat = new THREE.MeshStandardMaterial({
      color: THEME.cyan,
      roughness: 0.35,
      metalness: 0.2,
      side: THREE.DoubleSide
    });

    let currentMesh = new THREE.Mesh(geometries.ring, mat);
    bodyGroup.add(currentMesh);

    const shapeSelect = document.getElementById('moi-shape-select');
    const moiFormulaText = document.getElementById('moi-formula-display');
    const moiKText = document.getElementById('moi-k-display');

    const formulas = {
      ring: { formula: "I = M R² = 1.00 M R²", k: "k = R", factor: 1.0 },
      disc: { formula: "I = ½ M R² = 0.50 M R²", k: "k = R / √2 ≈ 0.707 R", factor: 0.5 },
      solid_cylinder: { formula: "I = ½ M R² = 0.50 M R²", k: "k = R / √2", factor: 0.5 },
      hollow_cylinder: { formula: "I = M R² = 1.00 M R²", k: "k = R", factor: 1.0 },
      solid_sphere: { formula: "I = ⅖ M R² = 0.40 M R²", k: "k = √(⅖) R ≈ 0.632 R", factor: 0.4 },
      rod: { formula: "I = ⅟₁₂ M L² = 0.083 M L²", k: "k = L / √12", factor: 0.083 }
    };

    function updateShape() {
      const type = shapeSelect ? shapeSelect.value : 'ring';
      bodyGroup.remove(currentMesh);
      currentMesh = new THREE.Mesh(geometries[type], mat);
      bodyGroup.add(currentMesh);

      if (moiFormulaText) moiFormulaText.textContent = formulas[type].formula;
      if (moiKText) moiKText.textContent = `Radius of Gyration: ${formulas[type].k}`;
    }

    if (shapeSelect) {
      shapeSelect.addEventListener('change', updateShape);
    }
    updateShape();

    function animate() {
      requestAnimationFrame(animate);
      // Spin body about y-axis
      bodyGroup.rotation.y += 0.02;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     4. SIMULATION: Pure Rolling Motion on an Incline (v_contact = 0)
     ========================================================================= */
  function initRollingSimulation() {
    const setup = create3DCanvas('three-rolling-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 22);
    camera.lookAt(0, 0, 0);

    const rollGroup = new THREE.Group();
    scene.add(rollGroup);

    // Inclined Plane Ramp
    const rampLength = 24;
    const rampAngle = 0.22; // ~12 degrees
    const rampGeo = new THREE.BoxGeometry(rampLength, 0.4, 6);
    const rampMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
    const ramp = new THREE.Mesh(rampGeo, rampMat);
    ramp.rotation.z = -rampAngle;
    rollGroup.add(ramp);

    // Rolling Cylinder Wheel
    const wheelR = 2.0;
    const wheelGeo = new THREE.CylinderGeometry(wheelR, wheelR, 1.6, 32);
    const wheelMat = new THREE.MeshStandardMaterial({ color: THEME.emerald, roughness: 0.35 });
    const wheel = new THREE.Mesh(wheelGeo, wheelMat);
    wheel.rotation.x = Math.PI / 2;
    rollGroup.add(wheel);

    // Spoke markers on wheel to clearly see rotation
    const spokeGeo = new THREE.BoxGeometry(wheelR * 1.9, 0.15, 1.65);
    const spokeMat = new THREE.MeshBasicMaterial({ color: THEME.gold });
    const spoke1 = new THREE.Mesh(spokeGeo, spokeMat);
    wheel.add(spoke1);
    const spoke2 = new THREE.Mesh(spokeGeo, spokeMat);
    spoke2.rotation.z = Math.PI / 2;
    wheel.add(spoke2);

    // Velocity Vector Arrows on Rolling Body
    // 1. Top Point (v = 2 v_cm)
    const topArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.rose, 0.8, 0.4);
    rollGroup.add(topArrow);

    // 2. Centre of Mass (v = v_cm)
    const cmArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 2.0, THEME.blue, 0.6, 0.3);
    rollGroup.add(cmArrow);

    // 3. Contact Point Indicator (v = 0)
    const contactDot = new THREE.Mesh(
      new THREE.SphereGeometry(0.3, 16, 16),
      new THREE.MeshBasicMaterial({ color: THEME.rose })
    );
    rollGroup.add(contactDot);

    let sPos = -rampLength / 2 + 3; // Along ramp coordinate
    let rollSpeed = 0.08;

    function animate() {
      requestAnimationFrame(animate);

      sPos += rollSpeed;
      if (sPos > rampLength / 2 - 3) {
        sPos = -rampLength / 2 + 3;
      }

      // Position along ramp
      const rampX = sPos * Math.cos(rampAngle);
      const rampY = -sPos * Math.sin(rampAngle) + wheelR + 0.2;
      wheel.position.set(rampX, rampY, 0);

      // Pure rolling condition: omega * R = v -> theta = s / R
      const theta = sPos / wheelR;
      wheel.rotation.z = -theta;

      // Update Vector Positions
      const dirAlongRamp = new THREE.Vector3(Math.cos(rampAngle), -Math.sin(rampAngle), 0);

      // CM Arrow
      cmArrow.position.set(rampX, rampY, 1.0);
      cmArrow.setDirection(dirAlongRamp);

      // Top Point Arrow (2 v_cm)
      const topX = rampX - wheelR * Math.sin(rampAngle);
      const topY = rampY + wheelR * Math.cos(rampAngle);
      topArrow.position.set(topX, topY, 1.0);
      topArrow.setDirection(dirAlongRamp);

      // Bottom Contact Point (v = 0)
      const botX = rampX + wheelR * Math.sin(rampAngle);
      const botY = rampY - wheelR * Math.cos(rampAngle);
      contactDot.position.set(botX, botY, 1.0);

      rollGroup.rotation.x = rotation.x;
      rollGroup.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  // --- Auto-Initialize ---
  function initAllRotational3D() {
    initCentreOfMassSimulation();
    initTorqueSimulation();
    initMomentOfInertiaSimulation();
    initRollingSimulation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllRotational3D);
  } else {
    initAllRotational3D();
  }
})();
