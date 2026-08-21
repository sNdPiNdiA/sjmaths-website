/**
 * SJMaths - Class 11 Physics Chapter 4: Laws of Motion
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. Galileo's Double Inclined Plane & Law of Inertia (Newton's 1st Law, slope reduction towards infinite horizontal motion)
 * 2. Newton's Second Law & Momentum Dynamics (F = dp/dt = m*a, applied force, mass, and resulting acceleration)
 * 3. Static vs Kinetic Friction on an Adjustable Incline (Angle of Repose, f_s <= mu_s * N, transition to sliding)
 * 4. Car on a Banked Circular Curve (Centripetal force, normal component N sin(theta), friction assistance, safe speeds)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Chapter 4. Retrying on load.");
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
     1. SIMULATION: Galileo's Double Inclined Plane & Law of Inertia
     ========================================================================= */
  function initGalileoSimulation() {
    const setup = create3DCanvas('three-galileo-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 12, 24);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Incline 1 (Left Ramp, fixed 30 deg slope)
    const rampLeftGeo = new THREE.BoxGeometry(10, 0.4, 4);
    rampLeftGeo.translate(-4.5, 2.5, 0);
    const rampMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
    const rampLeft = new THREE.Mesh(rampLeftGeo, rampMat);
    rampLeft.rotation.z = -0.52; // -30 deg
    group.add(rampLeft);

    // Incline 2 (Right Ramp, variable slope angle)
    const rampRightGeo = new THREE.BoxGeometry(16, 0.4, 4);
    rampRightGeo.translate(8, 0, 0);
    const rampRightMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.8 });
    const rampRight = new THREE.Mesh(rampRightGeo, rampRightMat);
    rampRight.position.set(0, -2.5, 0);
    group.add(rampRight);

    // Marble Sphere
    const sphere = new THREE.Mesh(
      new THREE.SphereGeometry(0.8, 32, 32),
      new THREE.MeshStandardMaterial({ color: THEME.gold, metalness: 0.3, roughness: 0.2 })
    );
    group.add(sphere);

    let thetaRight = 0.52; // ~30 deg
    let s = -8; // Along ramp coordinate
    let v = 0;
    let isPlaying = true;
    const initialH = 4.5;

    const angleSlider = document.getElementById('galileo-angle-slider');
    const galileoDesc = document.getElementById('galileo-desc-display');

    function animate() {
      requestAnimationFrame(animate);

      if (angleSlider) {
        const deg = parseFloat(angleSlider.value);
        thetaRight = (deg * Math.PI) / 180;
        rampRight.rotation.z = thetaRight;
      }

      if (isPlaying) {
        // Simplified energy conservation on friction-free track
        if (s < 0) {
          // Left ramp: accelerating downward
          const a = 9.8 * Math.sin(0.52);
          v += a * 0.008;
          s += v * 0.05;
        } else {
          // Right ramp: decelerating upward
          const a = -9.8 * Math.sin(thetaRight);
          v += a * 0.008;
          s += v * 0.05;
          if (v <= 0 && s > 0.5) {
            // Reached apex, reverse
            v = -0.1;
          }
        }

        if (s < -8) {
          s = -8;
          v = 0;
        }

        // Compute 3D position
        if (s < 0) {
          sphere.position.x = s * Math.cos(0.52);
          sphere.position.y = -s * Math.sin(0.52) - 1.8;
        } else {
          sphere.position.x = s * Math.cos(thetaRight);
          sphere.position.y = s * Math.sin(thetaRight) - 1.8;
        }
        sphere.position.z = 0;
      }

      if (galileoDesc && angleSlider) {
        const deg = parseFloat(angleSlider.value);
        if (deg === 0) {
          galileoDesc.innerHTML = `<span style="color:#10b981; font-weight:700;">Horizontal Track (θ = 0°):</span> In the absence of friction, the ball travels forever with constant velocity (Galileo's Law of Inertia &bull; Newton's 1st Law).`;
        } else {
          galileoDesc.innerHTML = `Right Incline: <b>${deg}°</b> &bull; Ball travels a distance <i>d = h / sin θ</i> to reach identical initial height <i>h</i>.`;
        }
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     2. SIMULATION: Newton's Second Law & Momentum Dynamics (F = m a)
     ========================================================================= */
  function initNewtonSecondSimulation() {
    const setup = create3DCanvas('three-newton2-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Track
    const trackGeo = new THREE.BoxGeometry(26, 0.4, 4);
    const trackMat = new THREE.MeshStandardMaterial({ color: 0x1e293b });
    const track = new THREE.Mesh(trackGeo, trackMat);
    track.position.y = -1.5;
    group.add(track);

    // Accelerating Crate
    const crateGeo = new THREE.BoxGeometry(3, 2.5, 2.5);
    const crateMat = new THREE.MeshStandardMaterial({ color: THEME.blue, roughness: 0.4 });
    const crate = new THREE.Mesh(crateGeo, crateMat);
    group.add(crate);

    // Applied Force Vector Arrow
    const fArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.rose, 0.8, 0.4);
    group.add(fArrow);

    // Acceleration Vector Arrow
    const aArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 1.8, 0), 3.0, THEME.gold, 0.6, 0.3);
    group.add(aArrow);

    let posX = -10;
    let velX = 0;

    const fSlider = document.getElementById('newton-f-slider');
    const mSlider = document.getElementById('newton-m-slider');
    const n2HudText = document.getElementById('newton-acc-display');

    function animate() {
      requestAnimationFrame(animate);

      const F = fSlider ? parseFloat(fSlider.value) : 10;
      const m = mSlider ? parseFloat(mSlider.value) : 2;
      const a = F / m;

      crate.scale.setScalar(0.7 + m * 0.15);

      velX += a * 0.005;
      posX += velX * 0.05;

      if (posX > 11) {
        posX = -10;
        velX = 0;
      }

      crate.position.set(posX, 0, 0);

      fArrow.position.set(posX + 1.5, 0, 0);
      fArrow.setLength(F * 0.35, 0.8, 0.4);

      aArrow.position.set(posX, 1.8, 0);
      aArrow.setLength(a * 0.45, 0.6, 0.3);

      if (n2HudText) {
        n2HudText.innerHTML = `Applied Force: <b style="color:#f43f5e;">${F.toFixed(0)} N</b> | Mass: <b style="color:#38bdf8;">${m.toFixed(1)} kg</b> ➔ Acceleration: <b style="color:#f59e0b;">a = F/m = ${a.toFixed(2)} m/s²</b>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     3. SIMULATION: Static vs Kinetic Friction on Adjustable Incline
     ========================================================================= */
  function initFrictionSimulation() {
    const setup = create3DCanvas('three-friction-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 10, 22);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    // Incline Plane
    const rampLength = 20;
    const rampGeo = new THREE.BoxGeometry(rampLength, 0.5, 5);
    const rampMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.9 });
    const ramp = new THREE.Mesh(rampGeo, rampMat);
    group.add(ramp);

    // Block on Incline
    const blockGeo = new THREE.BoxGeometry(2.5, 1.6, 2.5);
    const blockMat = new THREE.MeshStandardMaterial({ color: THEME.cyan, roughness: 0.5 });
    const block = new THREE.Mesh(blockGeo, blockMat);
    group.add(block);

    // Forces Arrows (N, mg, friction)
    const normArrow = new THREE.ArrowHelper(new THREE.Vector3(0, 1, 0), new THREE.Vector3(0, 0, 0), 3.0, THEME.emerald, 0.6, 0.3);
    group.add(normArrow);

    const frictArrow = new THREE.ArrowHelper(new THREE.Vector3(-1, 0, 0), new THREE.Vector3(0, 0, 0), 3.0, THEME.rose, 0.6, 0.3);
    group.add(frictArrow);

    let blockS = 0; // Position along ramp
    let blockV = 0;

    const angleSlider = document.getElementById('frict-angle-slider');
    const muSlider = document.getElementById('frict-mu-slider');
    const frictHudText = document.getElementById('frict-hud-display');

    function animate() {
      requestAnimationFrame(animate);

      const deg = angleSlider ? parseFloat(angleSlider.value) : 15;
      const mu_s = muSlider ? parseFloat(muSlider.value) : 0.4;
      const mu_k = mu_s * 0.8;
      const theta = (deg * Math.PI) / 180;

      ramp.rotation.z = -theta;

      const reposeAngleDeg = (Math.atan(mu_s) * 180) / Math.PI;

      if (deg > reposeAngleDeg) {
        // Accelerates down the slope
        const a = 9.8 * (Math.sin(theta) - mu_k * Math.cos(theta));
        blockV += Math.max(0, a) * 0.01;
        blockS += blockV * 0.05;
        if (blockS > rampLength / 2 - 2) {
          blockS = -rampLength / 2 + 2;
          blockV = 0;
        }
      } else {
        blockS = 0;
        blockV = 0;
      }

      // Position Block
      const bx = blockS * Math.cos(theta) - 1.0 * Math.sin(theta);
      const by = -blockS * Math.sin(theta) + 1.0 * Math.cos(theta);
      block.position.set(bx, by, 0);
      block.rotation.z = -theta;

      // Normal force perpendicular to plane
      const nDir = new THREE.Vector3(Math.sin(theta), Math.cos(theta), 0);
      normArrow.position.set(bx, by, 1.5);
      normArrow.setDirection(nDir);

      // Friction force up the slope
      const fDir = new THREE.Vector3(-Math.cos(theta), Math.sin(theta), 0);
      frictArrow.position.set(bx, by, 1.5);
      frictArrow.setDirection(fDir);

      if (frictHudText) {
        if (deg <= reposeAngleDeg) {
          frictHudText.innerHTML = `Angle θ = <b>${deg}°</b> ≤ θ<sub>repose</sub> (${reposeAngleDeg.toFixed(1)}°) &bull; <span style="color:#10b981; font-weight:700;">Static Equilibrium (f<sub>s</sub> = mg sinθ)</span>`;
        } else {
          frictHudText.innerHTML = `Angle θ = <b>${deg}°</b> > θ<sub>repose</sub> (${reposeAngleDeg.toFixed(1)}°) &bull; <span style="color:#f43f5e; font-weight:700;">Sliding Under Kinetic Friction (f<sub>k</sub> = μ<sub>k</sub> N)</span>`;
        }
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     4. SIMULATION: Car on a Banked Circular Curve (Circular Dynamics)
     ========================================================================= */
  function initBankedCurveSimulation() {
    const setup = create3DCanvas('three-banking-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 16, 26);
    camera.lookAt(0, 0, 0);

    const group = new THREE.Group();
    scene.add(group);

    const R = 9.0;

    // Banked circular track ring
    const trackGeo = new THREE.TorusGeometry(R, 1.8, 16, 64);
    const trackMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
    const trackMesh = new THREE.Mesh(trackGeo, trackMat);
    trackMesh.rotation.x = Math.PI / 2;
    group.add(trackMesh);

    // Car Vehicle
    const carGeo = new THREE.BoxGeometry(2.2, 1.2, 3.2);
    const carMat = new THREE.MeshStandardMaterial({ color: THEME.purple, roughness: 0.3 });
    const car = new THREE.Mesh(carGeo, carMat);
    group.add(car);

    // Centripetal Force Arrow
    const cpArrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 4.0, THEME.gold, 0.8, 0.4);
    group.add(cpArrow);

    let angle = 0;
    const thetaBankSlider = document.getElementById('bank-angle-slider');
    const speedSlider = document.getElementById('bank-speed-slider');
    const bankHudText = document.getElementById('bank-hud-display');

    function animate() {
      requestAnimationFrame(animate);

      const bankDeg = thetaBankSlider ? parseFloat(thetaBankSlider.value) : 18;
      const speed = speedSlider ? parseFloat(speedSlider.value) : 1.0;
      const bankRad = (bankDeg * Math.PI) / 180;

      angle += speed * 0.02;

      const cx = R * Math.cos(angle);
      const cz = R * Math.sin(angle);
      const cy = 0;

      car.position.set(cx, cy, cz);
      // Orient car along tangent and tilt into bank angle
      car.rotation.y = -angle + Math.PI / 2;
      car.rotation.z = bankRad;

      // Centripetal acceleration arrow directed toward centre (0,0,0)
      const toCenter = new THREE.Vector3(-cx, 0, -cz).normalize();
      cpArrow.position.set(cx, cy + 1.2, cz);
      cpArrow.setDirection(toCenter);
      cpArrow.setLength(speed * 3.5, 0.8, 0.4);

      if (bankHudText) {
        const v0 = Math.sqrt(R * 9.8 * Math.tan(bankRad));
        bankHudText.innerHTML = `Bank Angle: <b>${bankDeg}°</b> &bull; Optimum Speed (Zero Tyre Wear): <span style="color:#f59e0b; font-weight:700;">v₀ = √(Rg tanθ) ≈ ${(v0 * 3.6).toFixed(1)} km/h</span>`;
      }

      group.rotation.x = rotation.x;
      group.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllLawsOfMotion3D() {
    initGalileoSimulation();
    initNewtonSecondSimulation();
    initFrictionSimulation();
    initBankedCurveSimulation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllLawsOfMotion3D);
  } else {
    initAllLawsOfMotion3D();
  }
})();
