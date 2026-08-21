/**
 * SJMaths - Class 9 Advanced Science Chapter 4: The Geometry of Power – Advanced Simple Machines
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. 3D Mechanical Advantage Concept (Lifting heavy load with effort & lever/ramp)
 * 2. 3D Wheel and Axle Machine (Concentric rotating cylinders, MA = R / r, torque equilibrium)
 * 3. 3D Hanging Mass Tension Simulator (Stationary T = mg vs accelerating upward T = m(g + a))
 * 4. 3D Atwood Machine Two-Mass Pulley System (a = (m1 - m2)g / (m1 + m2), tension T = 2*m1*m2*g/(m1 + m2))
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Class 9 Chapter 4. Retrying on window load.");
    window.addEventListener("load", () => {
      if (typeof THREE !== "undefined") initAllVisualizers();
    });
    return;
  }

  const THEME = {
    spaceDark: 0x0a0f1d,
    gridDark: 0x1e293b,
    gridLight: 0x334155,
    blue: 0x0284c7,
    emerald: 0x059669,
    purple: 0x7c3aed,
    rose: 0xe11d48,
    amber: 0xd97706,
    cyan: 0x0891b2,
    metal: 0x94a3b8,
    gold: 0xfacc15,
    wood: 0xb45309,
    white: 0xffffff
  };

  function create3DScene(containerId) {
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

    const gridHelper = new THREE.GridHelper(30, 20, THEME.gridLight, THEME.gridDark);
    gridHelper.position.y = -3;
    scene.add(gridHelper);

    const ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
    scene.add(ambientLight);
    const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(12, 18, 14);
    scene.add(dirLight);

    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };
    let rotation = { x: 0.35, y: 0.45 };

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

    window.addEventListener('touchend', () => {
      isDragging = false;
    });

    window.addEventListener('resize', () => {
      if (!container) return;
      const nw = container.clientWidth;
      const nh = container.clientHeight;
      if (nw && nh) {
        camera.aspect = nw / nh;
        camera.updateProjectionMatrix();
        renderer.setSize(nw, nh);
      }
    });

    return { scene, camera, renderer, rotation };
  }

  // ========================================================
  // SIMULATION 1: 3D Wheel and Axle Machine
  // ========================================================
  function initWheelAxleSim() {
    const setup = create3DScene('three-wheel-axle-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Fixed Mounting Stand
    const standGeo = new THREE.CylinderGeometry(0.3, 0.3, 7, 16);
    const standMat = new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.7 });
    const stand = new THREE.Mesh(standGeo, standMat);
    stand.position.set(0, 0.5, -2);
    scene.add(stand);

    // Rotating Wheel & Axle Assembly Group
    const rotorGroup = new THREE.Group();
    rotorGroup.position.set(0, 2.5, 0);

    // 1. Central Axle Cylinder (Radius r = 0.8)
    const axleGeo = new THREE.CylinderGeometry(0.8, 0.8, 2.5, 32);
    axleGeo.rotateX(Math.PI / 2);
    const axleMat = new THREE.MeshStandardMaterial({ color: THEME.purple, roughness: 0.3 });
    const axle = new THREE.Mesh(axleGeo, axleMat);
    rotorGroup.add(axle);

    // 2. Large Wheel Disk (Radius R = 2.4)
    const wheelGeo = new THREE.CylinderGeometry(2.4, 2.4, 0.4, 32);
    wheelGeo.rotateX(Math.PI / 2);
    const wheelMat = new THREE.MeshStandardMaterial({ color: THEME.blue, transparent: true, opacity: 0.7, roughness: 0.2 });
    const wheel = new THREE.Mesh(wheelGeo, wheelMat);
    rotorGroup.add(wheel);

    // Spokes for rotation visibility
    for (let i = 0; i < 4; i++) {
      const spoke = new THREE.Mesh(new THREE.BoxGeometry(4.6, 0.08, 0.08), new THREE.MeshBasicMaterial({ color: 0xffffff }));
      spoke.rotation.z = (Math.PI / 4) * i;
      rotorGroup.add(spoke);
    }

    scene.add(rotorGroup);

    // Load Mass on Axle (Hanging from Axle rope)
    const loadGroup = new THREE.Group();
    const loadBox = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1.2, 1.2), new THREE.MeshStandardMaterial({ color: THEME.rose }));
    loadGroup.add(loadBox);
    loadGroup.position.set(0.8, 0, 0.5);
    scene.add(loadGroup);

    // Load Rope
    const ropeLoad = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 2.5, 8), new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }));
    ropeLoad.position.set(0.8, 1.25, 0.5);
    scene.add(ropeLoad);

    // Effort Rope on Wheel Rim
    const effortGroup = new THREE.Group();
    const effortBall = new THREE.Mesh(new THREE.SphereGeometry(0.4, 16, 16), new THREE.MeshStandardMaterial({ color: THEME.emerald }));
    effortGroup.add(effortBall);
    effortGroup.position.set(-2.4, -0.5, 0);
    scene.add(effortGroup);

    const ropeEffort = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 3.0, 8), new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }));
    ropeEffort.position.set(-2.4, 1.0, 0);
    scene.add(ropeEffort);

    let R_val = 30; // cm
    let r_val = 6;  // cm
    let load_N = 600; // N

    function updateParams() {
      const MA = (R_val / r_val).toFixed(1);
      const effort_N = (load_N / (R_val / r_val)).toFixed(1);
      const hud = document.getElementById('three-wheel-hud');
      if (hud) {
        hud.innerHTML = `Wheel Radius: <strong>R = ${R_val} cm</strong> | Axle Radius: <strong>r = ${r_val} cm</strong> | Load: <strong>L = ${load_N} N</strong><br>
          Mechanical Advantage: <strong class="badge badge-blue">MA = R/r = ${MA}</strong> | Required Effort: <strong class="badge badge-emerald">E = L/MA = ${effort_N} N</strong> (Force Multiplied by ${MA}×)`;
      }
    }

    const sliderR = document.getElementById('slider-wheel-r');
    const sliderAxle = document.getElementById('slider-axle-r');

    if (sliderR) {
      sliderR.addEventListener('input', (e) => {
        R_val = parseFloat(e.target.value);
        wheel.scale.set(R_val / 30, R_val / 30, 1);
        updateParams();
      });
    }

    if (sliderAxle) {
      sliderAxle.addEventListener('input', (e) => {
        r_val = parseFloat(e.target.value);
        axle.scale.set(r_val / 6, r_val / 6, 1);
        updateParams();
      });
    }

    updateParams();

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      rotorGroup.rotation.z -= dt * 0.8;

      const camRadius = 15;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 3;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 1.5, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 2: 3D Hanging Mass Tension Simulator
  // ========================================================
  function initHangingMassTensionSim() {
    const setup = create3DScene('three-tension-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Ceiling Mount
    const ceil = new THREE.Mesh(new THREE.BoxGeometry(6, 0.4, 6), new THREE.MeshStandardMaterial({ color: 0x334155 }));
    ceil.position.y = 4.5;
    scene.add(ceil);

    // Hanging Rope
    const rope = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 4, 8), new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }));
    rope.position.y = 2.5;
    scene.add(rope);

    // Hanging Mass m
    const massGroup = new THREE.Group();
    const massMesh = new THREE.Mesh(
      new THREE.CylinderGeometry(1.0, 1.0, 1.2, 24),
      new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.3 })
    );
    massGroup.add(massMesh);

    // Vectors on Mass: Upward Tension T (Cyan), Downward Weight mg (Rose)
    const arrowT = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(0, 0.6, 0), 2.2, THEME.cyan, 0.5, 0.25);
    massGroup.add(arrowT);

    const arrowMg = new THREE.ArrowHelper(new THREE.Vector3(0, -1, 0), new THREE.Vector3(0, -0.6, 0), 2.2, THEME.rose, 0.5, 0.25);
    massGroup.add(arrowMg);

    massGroup.position.set(0, 0.5, 0);
    scene.add(massGroup);

    let m_kg = 5;
    let a_acc = 0; // 0 for stationary, >0 for accelerating upward
    const g_val = 9.8;

    const btnStat = document.getElementById('btn-tens-stat');
    const btnAcc = document.getElementById('btn-tens-acc');
    const hud = document.getElementById('three-tension-hud');

    function setTensionMode(mode) {
      if (mode === "stat") {
        a_acc = 0;
        if (btnStat) btnStat.classList.add('active');
        if (btnAcc) btnAcc.classList.remove('active');
        arrowT.setLength(2.2);
        if (hud) {
          const T = (m_kg * g_val).toFixed(1);
          hud.innerHTML = `State: <strong class="badge badge-emerald">Stationary at Rest (a = 0)</strong><br>
            Tension Equation: <strong class="badge badge-cyan">T = mg = 5 × 9.8 = ${T} N</strong> (Tension equals weight).`;
        }
      } else {
        a_acc = 2.5;
        if (btnAcc) btnAcc.classList.add('active');
        if (btnStat) btnStat.classList.remove('active');
        arrowT.setLength(3.0);
        if (hud) {
          const T = (m_kg * (g_val + a_acc)).toFixed(1);
          hud.innerHTML = `State: <strong class="badge badge-rose">Accelerating Upward (a = +2.5 m/s²)</strong><br>
            Tension Equation: <strong class="badge badge-cyan">T = m(g + a) = 5 × (9.8 + 2.5) = ${T} N</strong> (Tension is GREATER than weight).`;
        }
      }
    }

    if (btnStat) btnStat.addEventListener('click', () => setTensionMode('stat'));
    if (btnAcc) btnAcc.addEventListener('click', () => setTensionMode('acc'));

    setTensionMode('stat');

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      const camRadius = 14;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 2;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 1.5, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 3: 3D Atwood Machine (Two-Mass Pulley System)
  // ========================================================
  function initAtwoodMachineSim() {
    const setup = create3DScene('three-atwood-pulley-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Pulley Wheel at Top (Radius = 1.4)
    const pulleyGeo = new THREE.CylinderGeometry(1.4, 1.4, 0.4, 32);
    pulleyGeo.rotateX(Math.PI / 2);
    const pulleyMat = new THREE.MeshStandardMaterial({ color: THEME.gold, metalness: 0.8, roughness: 0.2 });
    const pulley = new THREE.Mesh(pulleyGeo, pulleyMat);
    pulley.position.set(0, 4.0, 0);
    scene.add(pulley);

    // Stand & axle
    const stand = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 8, 16), new THREE.MeshStandardMaterial({ color: 0x475569 }));
    stand.position.set(0, 0.5, -1.5);
    scene.add(stand);

    // Left Mass m1 (Heavier)
    const leftGroup = new THREE.Group();
    const meshM1 = new THREE.Mesh(new THREE.BoxGeometry(1.4, 1.4, 1.4), new THREE.MeshStandardMaterial({ color: THEME.rose }));
    leftGroup.add(meshM1);
    leftGroup.position.set(-1.4, 1.0, 0);
    scene.add(leftGroup);

    // Right Mass m2 (Lighter)
    const rightGroup = new THREE.Group();
    const meshM2 = new THREE.Mesh(new THREE.BoxGeometry(1.0, 1.0, 1.0), new THREE.MeshStandardMaterial({ color: THEME.emerald }));
    rightGroup.add(meshM2);
    rightGroup.position.set(1.4, 1.0, 0);
    scene.add(rightGroup);

    // Left Rope & Right Rope
    const ropeLeft = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 4, 8), new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }));
    ropeLeft.position.set(-1.4, 2.5, 0);
    scene.add(ropeLeft);

    const ropeRight = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 4, 8), new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }));
    ropeRight.position.set(1.4, 2.5, 0);
    scene.add(ropeRight);

    let m1 = 6.0; // kg
    let m2 = 2.0; // kg
    const g_val = 9.8;
    let simY = 0;
    let isMoving = true;

    function updateAtwoodTelemetry() {
      const a = ((m1 - m2) * g_val) / (m1 + m2);
      const T = (2 * m1 * m2 * g_val) / (m1 + m2);
      const hud = document.getElementById('three-atwood-hud');
      if (hud) {
        hud.innerHTML = `Mass 1 (Left): <strong class="badge badge-rose">m₁ = ${m1.toFixed(1)} kg</strong> | Mass 2 (Right): <strong class="badge badge-emerald">m₂ = ${m2.toFixed(1)} kg</strong><br>
          System Acceleration: <strong class="badge badge-cyan">a = (m₁−m₂)g/(m₁+m₂) = ${a.toFixed(2)} m/s²</strong> | String Tension: <strong class="badge badge-amber">T = ${T.toFixed(2)} N</strong>`;
      }
    }

    const sliderM1 = document.getElementById('slider-atwood-m1');
    const sliderM2 = document.getElementById('slider-atwood-m2');
    const btnRestart = document.getElementById('btn-atwood-reset');

    if (sliderM1) {
      sliderM1.addEventListener('input', (e) => {
        m1 = parseFloat(e.target.value);
        meshM1.scale.set(m1 / 6, m1 / 6, m1 / 6);
        updateAtwoodTelemetry();
      });
    }

    if (sliderM2) {
      sliderM2.addEventListener('input', (e) => {
        m2 = parseFloat(e.target.value);
        meshM2.scale.set(m2 / 2, m2 / 2, m2 / 2);
        updateAtwoodTelemetry();
      });
    }

    if (btnRestart) {
      btnRestart.addEventListener('click', () => {
        simY = 0;
      });
    }

    updateAtwoodTelemetry();

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      const a = ((m1 - m2) * g_val) / (m1 + m2);
      simY += a * dt * 0.4;
      if (simY > 2.5) simY = -2.5;

      leftGroup.position.y = 1.0 - simY;
      rightGroup.position.y = 1.0 + simY;

      // Adjust rope lengths
      ropeLeft.scale.y = (4.0 - leftGroup.position.y) / 4.0;
      ropeLeft.position.y = (4.0 + leftGroup.position.y) / 2;

      ropeRight.scale.y = (4.0 - rightGroup.position.y) / 4.0;
      ropeRight.position.y = (4.0 + rightGroup.position.y) / 2;

      pulley.rotation.z = -simY * 1.5;

      const camRadius = 16;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 3;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 2.0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllVisualizers() {
    initWheelAxleSim();
    initHangingMassTensionSim();
    initAtwoodMachineSim();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllVisualizers);
  } else {
    initAllVisualizers();
  }
})();
