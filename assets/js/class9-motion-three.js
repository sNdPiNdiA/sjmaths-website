/**
 * SJMaths - Class 9 Advanced Science Chapter 2: Understanding Motion through Experience
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * 3D Visualizations included:
 * 1. 3D Reference Frames (Passenger in Moving Bus vs Roadside Observer)
 * 2. 3D Distance vs Displacement Track (Curved track path length vs direct vector displacement)
 * 3. 3D Vector Triangle Law Addition (Vector A East, Vector B North, Resultant R in 3D space)
 * 4. 3D Kinematic Car Acceleration & Braking (v = u + at, s = ut + 1/2 a t^2)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Class 9 Chapter 2. Retrying on window load.");
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
    road: 0x1e293b,
    roadMark: 0xfacc15,
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
    gridHelper.position.y = -2;
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

  // ==========================================
  // SIMULATION 1: 3D Frame of Reference
  // ==========================================
  function initFrameOfReferenceSim() {
    const setup = create3DScene('three-frame-ref-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Road surface
    const roadGeo = new THREE.PlaneGeometry(36, 6);
    const roadMat = new THREE.MeshStandardMaterial({ color: THEME.road, roughness: 0.8 });
    const road = new THREE.Mesh(roadGeo, roadMat);
    road.rotation.x = -Math.PI / 2;
    road.position.y = -1.98;
    scene.add(road);

    // Road dashed stripes
    for (let x = -16; x <= 16; x += 4) {
      const stripe = new THREE.Mesh(
        new THREE.PlaneGeometry(2, 0.2),
        new THREE.MeshBasicMaterial({ color: THEME.roadMark })
      );
      stripe.rotation.x = -Math.PI / 2;
      stripe.position.set(x, -1.97, 0);
      scene.add(stripe);
    }

    // Bus Group (Glass transparent bus with passenger)
    const busGroup = new THREE.Group();
    const busBody = new THREE.Mesh(
      new THREE.BoxGeometry(6, 2.4, 3),
      new THREE.MeshStandardMaterial({ color: THEME.blue, transparent: true, opacity: 0.35, roughness: 0.2 })
    );
    busBody.position.y = 0;
    busGroup.add(busBody);

    // Wheels
    const wheelMat = new THREE.MeshStandardMaterial({ color: 0x0f172a });
    const wGeo = new THREE.CylinderGeometry(0.5, 0.5, 0.4, 16);
    wGeo.rotateZ(Math.PI / 2);
    [[-1.8, -1.2, 1.4], [1.8, -1.2, 1.4], [-1.8, -1.2, -1.4], [1.8, -1.2, -1.4]].forEach(pos => {
      const w = new THREE.Mesh(wGeo, wheelMat);
      w.position.set(...pos);
      busGroup.add(w);
    });

    // Passenger inside bus
    const passGeo = new THREE.SphereGeometry(0.35, 16, 16);
    const passMat = new THREE.MeshStandardMaterial({ color: THEME.emerald });
    const passenger = new THREE.Mesh(passGeo, passMat);
    passenger.position.set(0, 0.2, 0);
    busGroup.add(passenger);

    // Passenger label indicator
    const ballInside = new THREE.Mesh(
      new THREE.SphereGeometry(0.18, 16, 16),
      new THREE.MeshStandardMaterial({ color: THEME.rose })
    );
    ballInside.position.set(0.8, -0.2, 0);
    busGroup.add(ballInside);

    busGroup.position.set(-8, -0.6, 0);
    scene.add(busGroup);

    // Roadside Standing Observer (Observer B)
    const obsGeo = new THREE.CylinderGeometry(0.25, 0.25, 1.2, 16);
    const obsMat = new THREE.MeshStandardMaterial({ color: THEME.amber });
    const observer = new THREE.Mesh(obsGeo, obsMat);
    observer.position.set(0, -1.4, 4);
    scene.add(observer);

    let viewMode = "ground"; // "ground" or "bus"
    let speed = 4.0;
    let busX = -10;

    const btnGround = document.getElementById('btn-ref-ground');
    const btnBus = document.getElementById('btn-ref-bus');
    const hud = document.getElementById('three-frame-ref-hud');

    if (btnGround) {
      btnGround.addEventListener('click', () => {
        viewMode = "ground";
        btnGround.classList.add('active');
        if (btnBus) btnBus.classList.remove('active');
      });
    }
    if (btnBus) {
      btnBus.addEventListener('click', () => {
        viewMode = "bus";
        btnBus.classList.add('active');
        if (btnGround) btnGround.classList.remove('active');
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();
      busX += speed * dt;
      if (busX > 14) busX = -14;
      busGroup.position.x = busX;

      if (viewMode === "ground") {
        const radius = 16;
        camera.position.x = radius * Math.sin(rotation.y) * Math.cos(rotation.x);
        camera.position.y = radius * Math.sin(rotation.x) + 3;
        camera.position.z = radius * Math.cos(rotation.y) * Math.cos(rotation.x);
        camera.lookAt(0, 0, 0);
        if (hud) {
          hud.innerHTML = `<strong>Observer Frame: Roadside (Inertial)</strong><br>Bus Speed: <span class="badge badge-emerald">v = 4.0 m/s</span> | Passenger appears moving with bus at +4.0 m/s relative to ground.`;
        }
      } else {
        // Bus frame
        camera.position.x = busGroup.position.x - 2;
        camera.position.y = busGroup.position.y + 1.2;
        camera.position.z = busGroup.position.z + 5.5;
        camera.lookAt(busGroup.position.x, busGroup.position.y, busGroup.position.z);
        if (hud) {
          hud.innerHTML = `<strong>Observer Frame: Passenger in Bus (Moving Frame)</strong><br>Passenger Speed: <span class="badge badge-blue">v_rel = 0 m/s (At Rest)</span> | Roadside tree & observer appear rushing backward at −4.0 m/s.`;
        }
      }

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 2: 3D Distance vs Displacement Runner
  // ========================================================
  function initDistDispSim() {
    const setup = create3DScene('three-dist-disp-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Track path curve (Semi-circular track from A(-6, 0) to B(6, 0))
    const curvePoints = [];
    const radius = 6;
    for (let i = 0; i <= 60; i++) {
      const theta = (Math.PI * i) / 60;
      curvePoints.push(new THREE.Vector3(-radius * Math.cos(theta), -1.95, radius * Math.sin(theta)));
    }
    const curve = new THREE.CatmullRomCurve3(curvePoints);
    const trackGeo = new THREE.TubeGeometry(curve, 64, 0.18, 8, false);
    const trackMat = new THREE.MeshStandardMaterial({ color: THEME.amber, roughness: 0.4 });
    const trackMesh = new THREE.Mesh(trackGeo, trackMat);
    scene.add(trackMesh);

    // Direct Displacement Line (A to B straight vector)
    const dispGeo = new THREE.CylinderGeometry(0.12, 0.12, 12, 16);
    dispGeo.rotateZ(Math.PI / 2);
    const dispMat = new THREE.MeshStandardMaterial({ color: THEME.cyan, roughness: 0.3 });
    const dispLine = new THREE.Mesh(dispGeo, dispMat);
    dispLine.position.set(0, -1.95, 0);
    scene.add(dispLine);

    // Marker flags A and B
    const startFlag = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 1, 16), new THREE.MeshStandardMaterial({ color: THEME.emerald }));
    startFlag.position.set(-6, -1.45, 0);
    scene.add(startFlag);

    const endFlag = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 1, 16), new THREE.MeshStandardMaterial({ color: THEME.rose }));
    endFlag.position.set(6, -1.45, 0);
    scene.add(endFlag);

    // Runner Avatar (Glowing sphere with direction pointer)
    const runner = new THREE.Mesh(
      new THREE.SphereGeometry(0.45, 20, 20),
      new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.2, emissive: 0x0284c7, emissiveIntensity: 0.4 })
    );
    runner.position.set(-6, -1.45, 0);
    scene.add(runner);

    let progress = 0;
    let isRunning = true;
    const hud = document.getElementById('three-dist-disp-hud');
    const toggleBtn = document.getElementById('btn-runner-toggle');

    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        isRunning = !isRunning;
        toggleBtn.innerHTML = isRunning ? '<i class="fas fa-pause"></i> Pause Motion' : '<i class="fas fa-play"></i> Resume Motion';
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      if (isRunning) {
        progress += dt * 0.2;
        if (progress > 1) progress = 0;
      }

      const currentPos = curve.getPoint(progress);
      runner.position.copy(currentPos);
      runner.position.y = -1.45;

      const distTraveled = (progress * Math.PI * radius).toFixed(1);
      const curDisp = (currentPos.distanceTo(new THREE.Vector3(-6, -1.95, 0))).toFixed(1);

      if (hud) {
        hud.innerHTML = `Track Progress: <strong>${Math.round(progress * 100)}%</strong> | Actual Path Distance: <span class="badge badge-amber">${distTraveled} m</span> | Direct Displacement: <span class="badge badge-cyan">${curDisp} m</span>`;
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

  // ========================================================
  // SIMULATION 3: 3D Vector Triangle Law Simulator
  // ========================================================
  function initVectorTriangleSim() {
    const setup = create3DScene('three-vector-triangle-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    const vecGroup = new THREE.Group();
    scene.add(vecGroup);

    let magA = 4;
    let magB = 3;

    function buildVectors(a, b) {
      while (vecGroup.children.length > 0) {
        vecGroup.remove(vecGroup.children[0]);
      }

      // Vector A (East along X)
      const dirA = new THREE.Vector3(1, 0, 0);
      const arrowA = new THREE.ArrowHelper(dirA, new THREE.Vector3(0, -1.5, 0), a, THEME.blue, 0.8, 0.4);
      arrowA.line.material.linewidth = 4;
      vecGroup.add(arrowA);

      // Vector B (North along Z or Y - in 3D let's place on ground plane along Z)
      const originB = new THREE.Vector3(a, -1.5, 0);
      const dirB = new THREE.Vector3(0, 0, 1);
      const arrowB = new THREE.ArrowHelper(dirB, originB, b, THEME.rose, 0.8, 0.4);
      arrowB.line.material.linewidth = 4;
      vecGroup.add(arrowB);

      // Resultant Vector R (From origin (0, -1.5, 0) to tip of B (a, -1.5, b))
      const targetR = new THREE.Vector3(a, 0, b);
      const lengthR = targetR.length();
      const dirR = targetR.clone().normalize();
      const arrowR = new THREE.ArrowHelper(dirR, new THREE.Vector3(0, -1.5, 0), lengthR, THEME.emerald, 1.0, 0.5);
      arrowR.line.material.linewidth = 5;
      vecGroup.add(arrowR);

      const hud = document.getElementById('three-vector-hud');
      if (hud) {
        const thetaDeg = (Math.atan2(b, a) * (180 / Math.PI)).toFixed(1);
        hud.innerHTML = `Vector A = <strong>${a} units (East)</strong> | Vector B = <strong>${b} units (North)</strong><br>Resultant: <span class="badge badge-emerald">|R| = √(${a}² + ${b}²) = ${lengthR.toFixed(2)} units</span> (θ = ${thetaDeg}° North of East)`;
      }
    }

    buildVectors(magA, magB);

    const sliderA = document.getElementById('slider-vec-a');
    const sliderB = document.getElementById('slider-vec-b');

    if (sliderA) {
      sliderA.addEventListener('input', (e) => {
        magA = parseFloat(e.target.value);
        buildVectors(magA, magB);
      });
    }
    if (sliderB) {
      sliderB.addEventListener('input', (e) => {
        magB = parseFloat(e.target.value);
        buildVectors(magA, magB);
      });
    }

    function animate() {
      requestAnimationFrame(animate);
      const camRadius = 15;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 4;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(magA / 2, -1.5, magB / 2);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 4: 3D Kinematics Toy Car Acceleration
  // ========================================================
  function initToyCarAccelerationSim() {
    const setup = create3DScene('three-kinematics-car-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Track surface
    const track = new THREE.Mesh(
      new THREE.PlaneGeometry(40, 5),
      new THREE.MeshStandardMaterial({ color: THEME.road, roughness: 0.7 })
    );
    track.rotation.x = -Math.PI / 2;
    track.position.y = -1.98;
    scene.add(track);

    // Track Distance Markers
    for (let m = -15; m <= 15; m += 5) {
      const marker = new THREE.Mesh(
        new THREE.BoxGeometry(0.1, 0.4, 4),
        new THREE.MeshBasicMaterial({ color: 0x94a3b8 })
      );
      marker.position.set(m, -1.8, 0);
      scene.add(marker);
    }

    // Toy Car Mesh
    const car = new THREE.Group();
    const carBody = new THREE.Mesh(
      new THREE.BoxGeometry(2.4, 0.9, 1.4),
      new THREE.MeshStandardMaterial({ color: THEME.rose, roughness: 0.3 })
    );
    carBody.position.y = 0.5;
    car.add(carBody);

    const cabin = new THREE.Mesh(
      new THREE.BoxGeometry(1.2, 0.7, 1.2),
      new THREE.MeshStandardMaterial({ color: THEME.spaceDark, roughness: 0.2 })
    );
    cabin.position.set(-0.2, 1.1, 0);
    car.add(cabin);

    // Wheels
    const wGeo = new THREE.CylinderGeometry(0.35, 0.35, 0.25, 16);
    wGeo.rotateZ(Math.PI / 2);
    const wMat = new THREE.MeshStandardMaterial({ color: 0x0f172a });
    [[-0.8, 0.3, 0.75], [0.8, 0.3, 0.75], [-0.8, 0.3, -0.75], [0.8, 0.3, -0.75]].forEach(p => {
      const w = new THREE.Mesh(wGeo, wMat);
      w.position.set(...p);
      car.add(w);
    });

    car.position.set(-15, -1.95, 0);
    scene.add(car);

    let u = 0.0; // Initial velocity
    let a = 2.0; // Acceleration m/s^2
    let simTime = 0.0;
    let isAccelerating = true;

    const btnReset = document.getElementById('btn-car-reset');
    const sliderAcc = document.getElementById('slider-car-acc');
    const hud = document.getElementById('three-kinematics-hud');

    if (btnReset) {
      btnReset.addEventListener('click', () => {
        simTime = 0.0;
        car.position.x = -15;
      });
    }

    if (sliderAcc) {
      sliderAcc.addEventListener('input', (e) => {
        a = parseFloat(e.target.value);
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      simTime += dt;
      const s = u * simTime + 0.5 * a * simTime * simTime;
      const v = u + a * simTime;

      car.position.x = -15 + s;

      if (car.position.x > 15) {
        simTime = 0;
        car.position.x = -15;
      }

      if (hud) {
        hud.innerHTML = `Time: <strong>${simTime.toFixed(1)} s</strong> | Acceleration: <strong class="badge badge-rose">a = ${a.toFixed(1)} m/s²</strong> | Speed: <strong class="badge badge-blue">v = ${v.toFixed(1)} m/s</strong> | Displacement: <strong class="badge badge-cyan">s = ${s.toFixed(1)} m</strong>`;
      }

      const camRadius = 18;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 4;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, -1, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllVisualizers() {
    initFrameOfReferenceSim();
    initDistDispSim();
    initVectorTriangleSim();
    initToyCarAccelerationSim();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllVisualizers);
  } else {
    initAllVisualizers();
  }
})();
