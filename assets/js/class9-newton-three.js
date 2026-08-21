/**
 * SJMaths - Class 9 Advanced Science Chapter 3: Newton's Laws of Motion
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. 3D Accelerating Elevator & Pseudo Force (F_pseudo = -m * a_frame, apparent weight N = m(g ± a))
 * 2. 3D Gravitational Orbit & Centripetal Force (Earth orbiting Sun, velocity vector tangent vs inward gravity)
 * 3. 3D Air Resistance & Terminal Fall (Streamlined metal sphere vs flat parachute/paper sheet)
 * 4. 3D Wrench Torque & Lever Arm Simulator (tau = F * d * sin(theta), force angle & length)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Class 9 Chapter 3. Retrying on load.");
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
  // SIMULATION 1: 3D Elevator & Pseudo Force
  // ========================================================
  function initElevatorPseudoSim() {
    const setup = create3DScene('three-pseudo-lift-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Elevator shaft frame
    const shaftGeo = new THREE.BoxGeometry(7, 14, 7);
    const shaftWire = new THREE.WireframeGeometry(shaftGeo);
    const shaftLine = new THREE.LineSegments(shaftWire, new THREE.LineBasicMaterial({ color: 0x334155 }));
    shaftLine.position.y = 0;
    scene.add(shaftLine);

    // Elevator Cabin Group
    const liftGroup = new THREE.Group();

    // Glass Elevator box
    const cabGeo = new THREE.BoxGeometry(4.5, 4.5, 4.5);
    const cabMat = new THREE.MeshStandardMaterial({
      color: THEME.blue,
      transparent: true,
      opacity: 0.25,
      roughness: 0.1
    });
    const cabin = new THREE.Mesh(cabGeo, cabMat);
    liftGroup.add(cabin);

    // Weighing scale platform inside cabin
    const scale = new THREE.Mesh(
      new THREE.CylinderGeometry(1.2, 1.2, 0.2, 24),
      new THREE.MeshStandardMaterial({ color: THEME.metal, metalness: 0.8, roughness: 0.3 })
    );
    scale.position.y = -2.1;
    liftGroup.add(scale);

    // Person Avatar (m = 60 kg)
    const person = new THREE.Mesh(
      new THREE.SphereGeometry(0.55, 16, 16),
      new THREE.MeshStandardMaterial({ color: THEME.emerald, roughness: 0.3 })
    );
    person.position.y = -1.35;
    liftGroup.add(person);

    // Force Vectors: Gravity (Down), Normal N (Up), Pseudo Force (F_pseudo)
    const arrowGravity = new THREE.ArrowHelper(new THREE.Vector3(0, -1, 0), new THREE.Vector3(-0.6, -1.35, 0), 1.6, THEME.rose, 0.4, 0.2);
    liftGroup.add(arrowGravity);

    const arrowNormal = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(0.6, -1.35, 0), 2.2, THEME.cyan, 0.4, 0.2);
    liftGroup.add(arrowNormal);

    scene.add(liftGroup);

    let liftMode = "up"; // "up", "down", "rest"
    let mass = 60; // kg
    let g = 9.8; // m/s^2
    let a = 4.5; // m/s^2
    let posY = 0;
    let velY = 0;

    const btnUp = document.getElementById('btn-lift-up');
    const btnDown = document.getElementById('btn-lift-down');
    const btnRest = document.getElementById('btn-lift-rest');
    const hud = document.getElementById('three-pseudo-hud');

    function updateMode(mode) {
      liftMode = mode;
      [btnUp, btnDown, btnRest].forEach(b => { if (b) b.classList.remove('active'); });
      if (mode === "up" && btnUp) btnUp.classList.add('active');
      if (mode === "down" && btnDown) btnDown.classList.add('active');
      if (mode === "rest" && btnRest) btnRest.classList.add('active');
    }

    if (btnUp) btnUp.addEventListener('click', () => updateMode('up'));
    if (btnDown) btnDown.addEventListener('click', () => updateMode('down'));
    if (btnRest) btnRest.addEventListener('click', () => updateMode('rest'));

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      let effectiveA = 0;
      let pseudoMag = 0;
      let apparentWeight = 0;

      if (liftMode === "up") {
        effectiveA = a;
        posY += effectiveA * dt * 0.8;
        if (posY > 3.5) posY = -3.5;
        pseudoMag = mass * a;
        apparentWeight = mass * (g + a);
        arrowNormal.setLength(2.6);
        if (hud) {
          hud.innerHTML = `Lift Acceleration: <strong class="badge badge-rose">a = +4.5 m/s² (Upward)</strong><br>
            Pseudo Force: <strong class="badge badge-amber">F_pseudo = −${pseudoMag.toFixed(0)} N (Downward)</strong> | Scale Reading: <strong class="badge badge-cyan">N = m(g + a) = ${apparentWeight.toFixed(0)} N (Feels Heavier)</strong>`;
        }
      } else if (liftMode === "down") {
        effectiveA = -a;
        posY += effectiveA * dt * 0.8;
        if (posY < -3.5) posY = 3.5;
        pseudoMag = mass * a;
        apparentWeight = mass * (g - a);
        arrowNormal.setLength(1.0);
        if (hud) {
          hud.innerHTML = `Lift Acceleration: <strong class="badge badge-rose">a = −4.5 m/s² (Downward)</strong><br>
            Pseudo Force: <strong class="badge badge-amber">F_pseudo = +${pseudoMag.toFixed(0)} N (Upward)</strong> | Scale Reading: <strong class="badge badge-cyan">N = m(g − a) = ${apparentWeight.toFixed(0)} N (Feels Lighter)</strong>`;
        }
      } else {
        posY = 0;
        pseudoMag = 0;
        apparentWeight = mass * g;
        arrowNormal.setLength(1.8);
        if (hud) {
          hud.innerHTML = `Lift at Constant Speed / Rest: <strong class="badge badge-blue">a = 0 m/s² (Inertial Frame)</strong><br>
            Pseudo Force: <strong class="badge badge-emerald">F_pseudo = 0 N</strong> | Scale Reading: <strong class="badge badge-cyan">N = mg = ${apparentWeight.toFixed(0)} N (True Weight)</strong>`;
        }
      }

      liftGroup.position.y = posY;

      const camRadius = 16;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 2;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 2: 3D Orbital Motion & Gravitational Orbit
  // ========================================================
  function initGravitationalOrbitSim() {
    const setup = create3DScene('three-orbit-sim-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Glowing Central Sun
    const sunGeo = new THREE.SphereGeometry(1.6, 24, 24);
    const sunMat = new THREE.MeshStandardMaterial({
      color: THEME.gold,
      emissive: 0xf59e0b,
      emissiveIntensity: 0.9,
      roughness: 0.2
    });
    const sun = new THREE.Mesh(sunGeo, sunMat);
    scene.add(sun);

    // Orbit ring
    const orbitRadius = 7.5;
    const orbitGeo = new THREE.RingGeometry(orbitRadius - 0.05, orbitRadius + 0.05, 64);
    const orbitMat = new THREE.MeshBasicMaterial({ color: 0x334155, side: THREE.DoubleSide });
    const orbitRing = new THREE.Mesh(orbitGeo, orbitMat);
    orbitRing.rotation.x = Math.PI / 2;
    scene.add(orbitRing);

    // Earth Planet
    const earthGroup = new THREE.Group();
    const earthGeo = new THREE.SphereGeometry(0.65, 20, 20);
    const earthMat = new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.4 });
    const earth = new THREE.Mesh(earthGeo, earthMat);
    earthGroup.add(earth);

    // Tangential Velocity Vector (Cyan)
    const arrowVel = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), new THREE.Vector3(0, 0, 0), 2.4, THEME.cyan, 0.5, 0.25);
    earthGroup.add(arrowVel);

    // Centripetal Inward Gravitational Force Vector (Rose)
    const arrowGrav = new THREE.ArrowHelper(new THREE.Vector3(-1, 0, 0), new THREE.Vector3(0, 0, 0), 2.2, THEME.rose, 0.5, 0.25);
    earthGroup.add(arrowGrav);

    scene.add(earthGroup);

    let orbitAngle = 0;
    let isGravityOn = true;
    let isOrbiting = true;
    let tangentX = 0, tangentZ = 0;

    const btnToggleGrav = document.getElementById('btn-orbit-gravity');
    const hud = document.getElementById('three-orbit-hud');

    if (btnToggleGrav) {
      btnToggleGrav.addEventListener('click', () => {
        isGravityOn = !isGravityOn;
        btnToggleGrav.innerHTML = isGravityOn ? '<i class="fas fa-sun"></i> Disable Sun Gravity' : '<i class="fas fa-undo"></i> Restore Gravity';
        btnToggleGrav.classList.toggle('active', !isGravityOn);
        if (!isGravityOn) {
          // Record tangential trajectory
          tangentX = -Math.sin(orbitAngle);
          tangentZ = Math.cos(orbitAngle);
        }
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      if (isGravityOn) {
        orbitAngle += dt * 0.8;
        const ex = orbitRadius * Math.cos(orbitAngle);
        const ez = orbitRadius * Math.sin(orbitAngle);
        earthGroup.position.set(ex, 0, ez);

        // Update velocity arrow along tangent
        const dirV = new THREE.Vector3(-Math.sin(orbitAngle), 0, Math.cos(orbitAngle));
        arrowVel.setDirection(dirV);

        // Update gravity arrow toward Sun (0, 0, 0)
        const dirG = new THREE.Vector3(-ex, 0, -ez).normalize();
        arrowGrav.setDirection(dirG);
        arrowGrav.visible = true;

        if (hud) {
          hud.innerHTML = `Gravitational Force: <strong class="badge badge-rose">F_g = GMm/r² (Centripetal pull)</strong> | Tangential Velocity: <strong class="badge badge-cyan">v = √(GM/r)</strong><br>
            Stable Orbit: Continual free fall curved toward Sun without crashing due to forward inertia.`;
        }
      } else {
        // Linear tangent fly-away
        earthGroup.position.x += tangentX * dt * 6.0;
        earthGroup.position.z += tangentZ * dt * 6.0;
        arrowGrav.visible = false;

        if (earthGroup.position.length() > 22) {
          // Loop back
          isGravityOn = true;
          orbitAngle = 0;
          if (btnToggleGrav) {
            btnToggleGrav.innerHTML = '<i class="fas fa-sun"></i> Disable Sun Gravity';
            btnToggleGrav.classList.remove('active');
          }
        }

        if (hud) {
          hud.innerHTML = `Sun Gravity: <strong class="badge badge-rose">OFF</strong> | Earth flies in a straight line along tangent at constant velocity according to Newton's 1st Law.`;
        }
      }

      const camRadius = 19;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 7;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 3: 3D Air Resistance vs Vacuum Drop
  // ========================================================
  function initAirResistanceSim() {
    const setup = create3DScene('three-air-resistance-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Dual Chamber Dividers (Left: Air, Right: Vacuum)
    const leftLabel = new THREE.Mesh(
      new THREE.PlaneGeometry(6, 12),
      new THREE.MeshBasicMaterial({ color: 0x0284c7, transparent: true, opacity: 0.08, side: THREE.DoubleSide })
    );
    leftLabel.position.set(-4, 0, 0);
    scene.add(leftLabel);

    const rightLabel = new THREE.Mesh(
      new THREE.PlaneGeometry(6, 12),
      new THREE.MeshBasicMaterial({ color: 0x7c3aed, transparent: true, opacity: 0.08, side: THREE.DoubleSide })
    );
    rightLabel.position.set(4, 0, 0);
    scene.add(rightLabel);

    // Left Chamber: Heavy Ball vs Light Flat Sheet (Air)
    const sphereAir = new THREE.Mesh(
      new THREE.SphereGeometry(0.4, 16, 16),
      new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.3 })
    );
    scene.add(sphereAir);

    const sheetAir = new THREE.Mesh(
      new THREE.BoxGeometry(1.2, 0.05, 1.2),
      new THREE.MeshStandardMaterial({ color: THEME.amber, roughness: 0.3 })
    );
    scene.add(sheetAir);

    // Right Chamber: Heavy Ball vs Light Flat Sheet (Vacuum)
    const sphereVac = new THREE.Mesh(
      new THREE.SphereGeometry(0.4, 16, 16),
      new THREE.MeshStandardMaterial({ color: THEME.emerald, roughness: 0.3 })
    );
    scene.add(sphereVac);

    const sheetVac = new THREE.Mesh(
      new THREE.BoxGeometry(1.2, 0.05, 1.2),
      new THREE.MeshStandardMaterial({ color: THEME.rose, roughness: 0.3 })
    );
    scene.add(sheetVac);

    let dropTime = 0;
    const gVal = 9.8;
    const btnDrop = document.getElementById('btn-drop-reset');
    const hud = document.getElementById('three-air-hud');

    if (btnDrop) {
      btnDrop.addEventListener('click', () => {
        dropTime = 0;
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();
      dropTime += dt;

      // Vacuum kinematics (Exact equal quadratic fall: y = y0 - 0.5 * g * t^2)
      const yVac = Math.max(-2.5, 4.5 - 0.5 * gVal * dropTime * dropTime * 0.4);
      sphereVac.position.set(2.5, yVac, 0);
      sheetVac.position.set(5.5, yVac, 0);

      // Air kinematics (Sphere experiences small drag, flat sheet experiences high drag)
      const ySphereAir = Math.max(-2.5, 4.5 - 0.5 * (gVal - 1.2) * dropTime * dropTime * 0.4);
      const ySheetAir = Math.max(-2.5, 4.5 - 0.5 * (gVal - 6.5) * dropTime * dropTime * 0.4);
      sphereAir.position.set(-5.5, ySphereAir, 0);
      sheetAir.position.set(-2.5, ySheetAir, 0);
      sheetAir.rotation.z = Math.sin(dropTime * 4) * 0.2; // Fluttering sheet

      if (yVac <= -2.5 && ySheetAir <= -2.5) {
        dropTime = 0; // Auto-loop
      }

      if (hud) {
        hud.innerHTML = `Chamber 1 (In Air): <span class="badge badge-amber">Flat Sheet Lags</span> (High Air Drag) vs Compact Sphere.<br>
          Chamber 2 (In Vacuum): <span class="badge badge-emerald">Both Fall Together</span> with identical acceleration $g = 9.8\\text{ m/s}^2$.`;
      }

      const camRadius = 17;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 2;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 1, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 4: 3D Torque & Lever Arm Wrench
  // ========================================================
  function initTorqueWrenchSim() {
    const setup = create3DScene('three-torque-wrench-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Bolt Pivot Center (Hexagon)
    const boltGeo = new THREE.CylinderGeometry(0.8, 0.8, 1.2, 6);
    const boltMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.8, roughness: 0.2 });
    const bolt = new THREE.Mesh(boltGeo, boltMat);
    bolt.position.set(0, -1.5, 0);
    scene.add(bolt);

    // Wrench Group (Rotates about origin)
    const wrenchGroup = new THREE.Group();
    wrenchGroup.position.set(0, -1.5, 0);

    const armGeo = new THREE.BoxGeometry(6, 0.4, 0.8);
    const armMat = new THREE.MeshStandardMaterial({ color: THEME.metal, metalness: 0.6, roughness: 0.3 });
    const arm = new THREE.Mesh(armGeo, armMat);
    arm.position.x = 3;
    wrenchGroup.add(arm);

    // Applied Force Arrow
    const arrowForce = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(5.8, 0, 0), 2.5, THEME.rose, 0.6, 0.3);
    wrenchGroup.add(arrowForce);

    scene.add(wrenchGroup);

    let armLength = 5.8;
    let forceMag = 20; // N
    let forceAngleDeg = 90; // degrees

    function updateTorque() {
      const rad = (forceAngleDeg * Math.PI) / 180;
      const dirF = new THREE.Vector3(-Math.cos(rad), Math.sin(rad), 0);
      arrowForce.setDirection(dirF);
      arrowForce.position.set(armLength, 0, 0);

      const torque = forceMag * armLength * Math.sin(rad);
      const hud = document.getElementById('three-torque-hud');
      if (hud) {
        hud.innerHTML = `Lever Arm: <strong>d = ${(armLength * 0.1).toFixed(2)} m</strong> | Force: <strong>F = ${forceMag} N</strong> | Angle: <strong>θ = ${forceAngleDeg}°</strong><br>
          Torque Generated: <strong class="badge badge-emerald">τ = F·d·sinθ = ${(torque * 0.1).toFixed(2)} N·m</strong> (${forceAngleDeg === 90 ? 'Maximum Torque' : forceAngleDeg === 0 ? 'Zero Torque (No rotation)' : 'Reduced Torque'})`;
      }
    }

    const sliderLength = document.getElementById('slider-wrench-len');
    const sliderAngle = document.getElementById('slider-wrench-angle');

    if (sliderLength) {
      sliderLength.addEventListener('input', (e) => {
        armLength = parseFloat(e.target.value);
        arm.scale.x = armLength / 5.8;
        arm.position.x = armLength / 2;
        updateTorque();
      });
    }

    if (sliderAngle) {
      sliderAngle.addEventListener('input', (e) => {
        forceAngleDeg = parseFloat(e.target.value);
        updateTorque();
      });
    }

    updateTorque();

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      const rad = (forceAngleDeg * Math.PI) / 180;
      const torque = forceMag * armLength * Math.sin(rad);
      wrenchGroup.rotation.z += torque * 0.0008 * dt * 60;

      const camRadius = 15;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 3;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(2, -1.5, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllVisualizers() {
    initElevatorPseudoSim();
    initGravitationalOrbitSim();
    initAirResistanceSim();
    initTorqueWrenchSim();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllVisualizers);
  } else {
    initAllVisualizers();
  }
})();
