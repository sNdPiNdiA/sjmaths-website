/**
 * SJMaths - Class 9 Advanced Science Chapter 5: Work and Energy
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. 3D Damped Energy Pendulum (Non-conservative air resistance/friction converting mechanical energy to heat)
 * 2. 3D Hooke's Law Spring & Elastic Potential Energy (F = -kx, U = 1/2 k x^2, visual spring coil stretch)
 * 3. 3D Spring Launcher Energy Conversion (Spring PE -> Kinetic Energy -> Block Launch, 1/2 k x^2 = 1/2 m v^2)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Class 9 Chapter 5. Retrying on window load.");
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
  // SIMULATION 1: 3D Damped Energy Pendulum
  // ========================================================
  function initDampedPendulumSim() {
    const setup = create3DScene('three-pendulum-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Pivot Stand
    const pivot = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 16), new THREE.MeshStandardMaterial({ color: 0x94a3b8 }));
    pivot.position.set(0, 4.0, 0);
    scene.add(pivot);

    const armGroup = new THREE.Group();
    armGroup.position.set(0, 4.0, 0);

    const rod = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 5.5, 8), new THREE.MeshStandardMaterial({ color: 0xcbd5e1 }));
    rod.position.y = -2.75;
    armGroup.add(rod);

    const bob = new THREE.Mesh(new THREE.SphereGeometry(0.7, 24, 24), new THREE.MeshStandardMaterial({ color: THEME.purple, roughness: 0.2 }));
    bob.position.y = -5.5;
    armGroup.add(bob);

    scene.add(armGroup);

    let maxAngle = Math.PI / 3; // 60 degrees initial
    let currentAngle = maxAngle;
    let angularVel = 0;
    let damping = 0.05; // non-conservative damping
    let isDamped = true;

    const btnToggleDamp = document.getElementById('btn-damp-toggle');
    const btnReset = document.getElementById('btn-damp-reset');
    const hud = document.getElementById('three-damp-hud');

    if (btnToggleDamp) {
      btnToggleDamp.addEventListener('click', () => {
        isDamped = !isDamped;
        btnToggleDamp.innerHTML = isDamped ? '<i class="fas fa-wind"></i> Friction/Drag: ON' : '<i class="fas fa-shield-alt"></i> Conservative (No Drag)';
        btnToggleDamp.classList.toggle('active', isDamped);
      });
    }

    if (btnReset) {
      btnReset.addEventListener('click', () => {
        currentAngle = Math.PI / 3;
        angularVel = 0;
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = Math.min(clock.getDelta(), 0.1);

      // Simple harmonic motion ODE with damping: theta'' = -(g/L)*sin(theta) - c*theta'
      const g_L = 9.8 / 5.5;
      const angularAcc = -g_L * Math.sin(currentAngle) - (isDamped ? damping * angularVel : 0);
      angularVel += angularAcc * dt;
      currentAngle += angularVel * dt;

      armGroup.rotation.z = currentAngle;

      const currentDeg = (Math.abs(currentAngle) * (180 / Math.PI)).toFixed(1);
      const energyFraction = Math.max(0, (1 - Math.cos(currentAngle)) / (1 - Math.cos(Math.PI / 3)) * 100).toFixed(0);

      if (hud) {
        hud.innerHTML = `Mode: <strong class="${isDamped ? 'badge badge-rose' : 'badge badge-emerald'}">${isDamped ? 'Non-Conservative (Friction/Air Drag)' : 'Ideal Conservative System'}</strong><br>
          Current Angle: <strong>${currentDeg}°</strong> | Mechanical Energy: <strong class="badge badge-cyan">${energyFraction}%</strong> (${isDamped ? 'Energy dissipates as heat' : 'E_total = PE + KE = Constant'})`;
      }

      const camRadius = 16;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 2;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 1.5, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 2: 3D Hooke's Law Spring & Elastic PE
  // ========================================================
  function initSpringHookeSim() {
    const setup = create3DScene('three-spring-hooke-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Fixed Wall Stand (Left)
    const wall = new THREE.Mesh(new THREE.BoxGeometry(0.8, 4, 4), new THREE.MeshStandardMaterial({ color: 0x475569 }));
    wall.position.set(-6, 0, 0);
    scene.add(wall);

    // Spring Coils (Using a parametric helical curve)
    const springGroup = new THREE.Group();
    scene.add(springGroup);

    // Attached Movable Block
    const block = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.6, 1.6), new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.3 }));
    block.position.set(0, 0, 0);
    scene.add(block);

    // Restoring Force Arrow (Rose)
    const arrowRestoring = new THREE.ArrowHelper(new THREE.Vector3(-1, 0, 0), new THREE.Vector3(0, 1.4, 0), 2.0, THEME.rose, 0.5, 0.25);
    scene.add(arrowRestoring);

    let k_val = 50; // N/m
    let x_val = 2.0; // m (displacement)

    function updateSpring(x) {
      while (springGroup.children.length > 0) {
        springGroup.remove(springGroup.children[0]);
      }

      const length = 6 + x;
      const coils = 12;
      const radius = 0.55;
      const points = [];
      const steps = 120;

      for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        const px = -6 + t * length;
        const py = radius * Math.sin(t * coils * Math.PI * 2);
        const pz = radius * Math.cos(t * coils * Math.PI * 2);
        points.push(new THREE.Vector3(px, py, pz));
      }

      const curve = new THREE.CatmullRomCurve3(points);
      const tubeGeo = new THREE.TubeGeometry(curve, 100, 0.08, 8, false);
      const tubeMat = new THREE.MeshStandardMaterial({ color: THEME.metal, metalness: 0.8, roughness: 0.2 });
      const springMesh = new THREE.Mesh(tubeGeo, tubeMat);
      springGroup.add(springMesh);

      block.position.x = -6 + length + 0.8;

      const F = (k_val * x).toFixed(1);
      const U = (0.5 * k_val * x * x).toFixed(2);

      arrowRestoring.position.set(block.position.x, 1.3, 0);
      arrowRestoring.setDirection(new THREE.Vector3(x >= 0 ? -1 : 1, 0, 0));
      arrowRestoring.setLength(Math.max(0.5, Math.abs(x) * 1.2));

      const hud = document.getElementById('three-spring-hud');
      if (hud) {
        hud.innerHTML = `Spring Constant: <strong>k = ${k_val} N/m</strong> | Extension: <strong>x = ${x.toFixed(2)} m</strong><br>
          Restoring Force: <strong class="badge badge-rose">F = −kx = −${F} N</strong> | Stored Elastic PE: <strong class="badge badge-emerald">U = ½kx² = ${U} J</strong>`;
      }
    }

    const sliderX = document.getElementById('slider-spring-x');
    const sliderK = document.getElementById('slider-spring-k');

    if (sliderX) {
      sliderX.addEventListener('input', (e) => {
        x_val = parseFloat(e.target.value);
        updateSpring(x_val);
      });
    }

    if (sliderK) {
      sliderK.addEventListener('input', (e) => {
        k_val = parseFloat(e.target.value);
        updateSpring(x_val);
      });
    }

    updateSpring(x_val);

    function animate() {
      requestAnimationFrame(animate);
      const camRadius = 16;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 3;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 3: 3D Spring Launcher (PE -> KE Conversion)
  // ========================================================
  function initSpringLauncherSim() {
    const setup = create3DScene('three-launcher-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Track platform
    const track = new THREE.Mesh(new THREE.BoxGeometry(32, 0.4, 4), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
    track.position.set(0, -1.2, 0);
    scene.add(track);

    // Wall (Left)
    const wall = new THREE.Mesh(new THREE.BoxGeometry(0.8, 3, 4), new THREE.MeshStandardMaterial({ color: 0x475569 }));
    wall.position.set(-14, 0.5, 0);
    scene.add(wall);

    // Launcher Spring
    const springGroup = new THREE.Group();
    scene.add(springGroup);

    // Projectile Block (m = 0.5 kg)
    const projectile = new THREE.Mesh(
      new THREE.BoxGeometry(1.4, 1.4, 1.4),
      new THREE.MeshStandardMaterial({ color: THEME.emerald, roughness: 0.3 })
    );
    projectile.position.set(-6, -0.3, 0);
    scene.add(projectile);

    let k_const = 100; // N/m
    let compression = 2.5; // m
    let mass = 0.5; // kg
    let isLaunched = false;
    let projX = -14 + (6 - compression);
    let projV = 0;

    function renderCoil(c) {
      while (springGroup.children.length > 0) {
        springGroup.remove(springGroup.children[0]);
      }
      const len = 6 - c;
      const points = [];
      const steps = 80;
      for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        const px = -14 + t * len;
        const py = -0.3 + 0.45 * Math.sin(t * 10 * Math.PI * 2);
        const pz = 0.45 * Math.cos(t * 10 * Math.PI * 2);
        points.push(new THREE.Vector3(px, py, pz));
      }
      const curve = new THREE.CatmullRomCurve3(points);
      const tube = new THREE.Mesh(
        new THREE.TubeGeometry(curve, 70, 0.07, 8, false),
        new THREE.MeshStandardMaterial({ color: THEME.metal, metalness: 0.8 })
      );
      springGroup.add(tube);
    }

    renderCoil(compression);
    projectile.position.x = -14 + (6 - compression) + 0.7;

    const btnLaunch = document.getElementById('btn-launcher-fire');
    const hud = document.getElementById('three-launcher-hud');

    if (btnLaunch) {
      btnLaunch.addEventListener('click', () => {
        isLaunched = true;
        // Total PE = 1/2 * k * x^2
        const PE = 0.5 * k_const * compression * compression;
        // Max Speed = sqrt(2*PE / m)
        projV = Math.sqrt((2 * PE) / mass);
        btnLaunch.classList.add('active');
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      if (isLaunched) {
        projX += projV * dt * 0.7;
        projectile.position.x = projX;

        if (projX > 14) {
          // Reset
          isLaunched = false;
          projX = -14 + (6 - compression) + 0.7;
          projectile.position.x = projX;
          if (btnLaunch) btnLaunch.classList.remove('active');
        }
      }

      const PE_val = (0.5 * k_const * compression * compression).toFixed(2);
      const V_max = Math.sqrt((2 * (0.5 * k_const * compression * compression)) / mass).toFixed(2);

      if (hud) {
        hud.innerHTML = `Spring PE Stored: <strong class="badge badge-amber">U = ½kx² = ${PE_val} J</strong> | Mass: <strong>m = ${mass} kg</strong><br>
          Max Velocity (100% Conversion): <strong class="badge badge-emerald">v = √(kx²/m) = ${V_max} m/s</strong> (Kinetic Energy K = ½mv² = ${PE_val} J)`;
      }

      const camRadius = 18;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 4;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllVisualizers() {
    initDampedPendulumSim();
    initSpringHookeSim();
    initSpringLauncherSim();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllVisualizers);
  } else {
    initAllVisualizers();
  }
})();
