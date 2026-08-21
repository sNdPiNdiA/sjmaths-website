/**
 * SJMaths - Class 11 Physics Chapter 7: Gravitation
 * Interactive 3D Physics Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. Kepler's Laws (Elliptical Orbit, Areal Velocity sweep ΔA, Velocity vectors, Foci)
 * 2. Variation of 'g' (3D Earth cutaway, altitude & depth slider, gravity field graph)
 * 3. Gravitational Potential Well & Escape Velocity (Projectile launch trajectory simulator)
 * 4. Satellite Orbit Simulator (Low-Earth, Polar, Geostationary & Spacecraft orbital mechanics)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded. Initializer will retry.");
    return;
  }

  // --- Theme Colors ---
  const THEME = {
    spaceDark: 0x090d16,
    sunGold: 0xf59e0b,
    sunCorona: 0xfbbf24,
    earthBlue: 0x38bdf8,
    earthAtmosphere: 0x0284c7,
    earthCore: 0xef4444,
    earthMantle: 0xf97316,
    earthCrust: 0x10b981,
    planetPurple: 0xa855f7,
    vectorGreen: 0x22c55e,
    vectorRed: 0xf43f5e,
    orbitLine: 0x6366f1,
    sweepArea: 0xf59e0b,
    gridLine: 0x1e293b,
    white: 0xffffff,
    satellite: 0xe2e8f0
  };

  // Helper: setup responsive scene
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

    // Subtle starfield
    const starGeo = new THREE.BufferGeometry();
    const starCount = 300;
    const starPos = new Float32Array(starCount * 3);
    for (let i = 0; i < starCount * 3; i += 3) {
      starPos[i] = (Math.random() - 0.5) * 120;
      starPos[i + 1] = (Math.random() - 0.5) * 120;
      starPos[i + 2] = (Math.random() - 0.5) * 120;
    }
    starGeo.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
    const starMat = new THREE.PointsMaterial({ color: 0x94a3b8, size: 0.6, transparent: true, opacity: 0.6 });
    scene.add(new THREE.Points(starGeo, starMat));

    // Ambient & Directional light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambientLight);
    const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(10, 20, 15);
    scene.add(dirLight);

    // Orbit controls or mouse interaction
    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };
    let rotation = { x: 0.3, y: 0.5 };

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

    // Resize handler
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
     1. SIMULATION: Kepler's Laws of Planetary Motion
     ========================================================================= */
  function initKeplerSimulation() {
    const setup = create3DCanvas('three-kepler-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 18, 26);
    camera.lookAt(0, 0, 0);

    const orbitGroup = new THREE.Group();
    scene.add(orbitGroup);

    // Orbit parameters
    const a = 12; // Semi-major axis
    const e = 0.55; // Eccentricity
    const b = a * Math.sqrt(1 - e * e); // Semi-minor axis
    const c = a * e; // Focus distance from center

    // Draw Ellipse Orbit Track
    const curvePoints = [];
    for (let i = 0; i <= 100; i++) {
      const theta = (i / 100) * Math.PI * 2;
      curvePoints.push(new THREE.Vector3(a * Math.cos(theta) - c, 0, b * Math.sin(theta)));
    }
    const orbitGeo = new THREE.BufferGeometry().setFromPoints(curvePoints);
    const orbitMat = new THREE.LineBasicMaterial({ color: THEME.orbitLine, linewidth: 2 });
    const orbitLine = new THREE.Line(orbitGeo, orbitMat);
    orbitGroup.add(orbitLine);

    // Major and minor axes lines
    const axisGeo = new THREE.BufferGeometry().setFromPoints([
      new THREE.Vector3(-a - c, 0, 0), new THREE.Vector3(a - c, 0, 0)
    ]);
    const axisMat = new THREE.LineDashedMaterial({ color: 0x475569, dashSize: 0.5, gapSize: 0.3 });
    const axisLine = new THREE.Line(axisGeo, axisMat);
    axisLine.computeLineDistances();
    orbitGroup.add(axisLine);

    // Sun at Focus S (x = 0, y = 0, z = 0)
    const sunGeo = new THREE.SphereGeometry(1.6, 32, 32);
    const sunMat = new THREE.MeshStandardMaterial({
      color: THEME.sunGold,
      emissive: 0xd97706,
      emissiveIntensity: 0.7,
      roughness: 0.2
    });
    const sun = new THREE.Mesh(sunGeo, sunMat);
    sun.position.set(0, 0, 0);
    orbitGroup.add(sun);

    // Sun glow ring
    const glowGeo = new THREE.RingGeometry(1.7, 2.4, 32);
    const glowMat = new THREE.MeshBasicMaterial({ color: THEME.sunCorona, side: THREE.DoubleSide, transparent: true, opacity: 0.4 });
    const glow = new THREE.Mesh(glowGeo, glowMat);
    glow.rotation.x = Math.PI / 2;
    orbitGroup.add(glow);

    // Empty Focus (S')
    const focusGeo = new THREE.SphereGeometry(0.35, 16, 16);
    const focusMat = new THREE.MeshBasicMaterial({ color: 0x64748b });
    const emptyFocus = new THREE.Mesh(focusGeo, focusMat);
    emptyFocus.position.set(-2 * c, 0, 0);
    orbitGroup.add(emptyFocus);

    // Planet
    const planetGeo = new THREE.SphereGeometry(0.8, 32, 32);
    const planetMat = new THREE.MeshStandardMaterial({ color: THEME.earthBlue, roughness: 0.3 });
    const planet = new THREE.Mesh(planetGeo, planetMat);
    orbitGroup.add(planet);

    // Radius Vector Line (Sun to Planet)
    const radiusLineGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0,0,0), new THREE.Vector3(1,0,0)]);
    const radiusLineMat = new THREE.LineBasicMaterial({ color: THEME.vectorGreen, linewidth: 2 });
    const radiusLine = new THREE.Line(radiusLineGeo, radiusLineMat);
    orbitGroup.add(radiusLine);

    // Velocity Vector Arrow
    const velArrow = new THREE.ArrowHelper(new THREE.Vector3(0, 0, 1), new THREE.Vector3(0, 0, 0), 3, THEME.vectorRed, 0.8, 0.4);
    orbitGroup.add(velArrow);

    // Sectorial Sweep Mesh (Kepler 2nd Law Area)
    let sweepSectorMesh = null;

    // Animation variable: Mean anomaly M
    let M = 0;
    let isPlaying = true;
    let simSpeed = 1.0;
    let showSweep = true;

    // Solve Kepler's equation M = E - e*sin(E) for Eccentric Anomaly E
    function solveKepler(meanAnomaly, ecc) {
      let E = meanAnomaly;
      for (let i = 0; i < 6; i++) {
        E = E - (E - ecc * Math.sin(E) - meanAnomaly) / (1 - ecc * Math.cos(E));
      }
      return E;
    }

    // UI Hookups
    const playBtn = document.getElementById('kepler-play-btn');
    if (playBtn) {
      playBtn.addEventListener('click', () => {
        isPlaying = !isPlaying;
        playBtn.innerHTML = isPlaying ? '<i class="fas fa-pause"></i> Pause' : '<i class="fas fa-play"></i> Play';
      });
    }

    const eccSlider = document.getElementById('kepler-ecc-slider');
    const eccVal = document.getElementById('kepler-ecc-val');
    if (eccSlider) {
      eccSlider.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        if (eccVal) eccVal.textContent = val.toFixed(2);
        // Update orbit shape
        const newB = a * Math.sqrt(1 - val * val);
        const newC = a * val;
        emptyFocus.position.set(-2 * newC, 0, 0);

        const newPoints = [];
        for (let i = 0; i <= 100; i++) {
          const theta = (i / 100) * Math.PI * 2;
          newPoints.push(new THREE.Vector3(a * Math.cos(theta) - newC, 0, newB * Math.sin(theta)));
        }
        orbitLine.geometry.setFromPoints(newPoints);
      });
    }

    const speedSlider = document.getElementById('kepler-speed-slider');
    if (speedSlider) {
      speedSlider.addEventListener('input', (e) => {
        simSpeed = parseFloat(e.target.value);
      });
    }

    const infoDist = document.getElementById('kepler-info-dist');
    const infoVel = document.getElementById('kepler-info-vel');
    const infoArea = document.getElementById('kepler-info-area');

    function animate() {
      requestAnimationFrame(animate);

      if (isPlaying) {
        M += 0.015 * simSpeed;
        if (M > Math.PI * 2) M -= Math.PI * 2;
      }

      const curE = eccSlider ? parseFloat(eccSlider.value) : e;
      const curB = a * Math.sqrt(1 - curE * curE);
      const curC = a * curE;

      const E_anom = solveKepler(M, curE);

      // Planet Position in orbital plane
      const x = a * Math.cos(E_anom) - curC;
      const z = curB * Math.sin(E_anom);
      planet.position.set(x, 0, z);

      // Distance r from Sun
      const r = Math.sqrt(x * x + z * z);
      const perihelionDist = a * (1 - curE);
      const aphelionDist = a * (1 + curE);

      // Velocity magnitude (Vis-Viva Equation: v = sqrt(GM * (2/r - 1/a)))
      // Normalized for visualization
      const vMag = Math.sqrt(Math.max(0.1, 2 / r - 1 / a)) * 6.5;

      // Velocity direction (tangent dx/dE, dz/dE)
      const dx_dE = -a * Math.sin(E_anom);
      const dz_dE = curB * Math.cos(E_anom);
      const vDir = new THREE.Vector3(dx_dE, 0, dz_dE).normalize();

      velArrow.position.copy(planet.position);
      velArrow.setDirection(vDir);
      velArrow.setLength(vMag * 0.7, 0.8, 0.4);

      // Update Radius Line
      const radPts = [new THREE.Vector3(0, 0, 0), new THREE.Vector3(x, 0, z)];
      radiusLine.geometry.setFromPoints(radPts);

      // Sectorial Sweep Visualizer (Swept area in past Δt)
      if (orbitGroup) {
        if (sweepSectorMesh) orbitGroup.remove(sweepSectorMesh);
        const sweepPts = [new THREE.Vector3(0, 0, 0)];
        const steps = 14;
        const deltaM = 0.35;
        for (let s = 0; s <= steps; s++) {
          const pastM = M - deltaM * (1 - s / steps);
          const pastE = solveKepler(pastM, curE);
          sweepPts.push(new THREE.Vector3(a * Math.cos(pastE) - curC, 0, curB * Math.sin(pastE)));
        }
        sweepPts.push(new THREE.Vector3(0, 0, 0));

        // Create fan shape
        const shape = new THREE.Shape();
        shape.moveTo(0, 0);
        for (let s = 1; s < sweepPts.length - 1; s++) {
          shape.lineTo(sweepPts[s].x, sweepPts[s].z);
        }
        shape.closePath();

        const sweepGeo = new THREE.ShapeGeometry(shape);
        const sweepMat = new THREE.MeshBasicMaterial({ color: THEME.sweepArea, transparent: true, opacity: 0.35, side: THREE.DoubleSide });
        sweepSectorMesh = new THREE.Mesh(sweepGeo, sweepMat);
        sweepSectorMesh.rotation.x = Math.PI / 2;
        orbitGroup.add(sweepSectorMesh);
      }

      // Smooth rotation with mouse interaction
      orbitGroup.rotation.x = rotation.x;
      orbitGroup.rotation.y = rotation.y;

      // Update real-time HUD values
      if (infoDist) infoDist.textContent = (r * 12.4).toFixed(1) + " × 10⁶ km";
      if (infoVel) infoVel.textContent = (vMag * 4.8).toFixed(1) + " km/s";
      if (infoArea) infoArea.textContent = "Constant (L/2m = " + (4.47).toFixed(2) + " AU²/yr)";

      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     2. SIMULATION: Variation of Gravity 'g' with Altitude & Depth (Earth 3D Cutaway)
     ========================================================================= */
  function initGravityVariationSimulation() {
    const setup = create3DCanvas('three-gravity-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 14, 22);
    camera.lookAt(0, 0, 0);

    const earthGroup = new THREE.Group();
    scene.add(earthGroup);

    const R_E = 6.0; // Earth radius units

    // Outer Crust / Atmosphere Shell
    const earthGeo = new THREE.SphereGeometry(R_E, 32, 32, 0, Math.PI * 1.5, 0, Math.PI);
    const earthMat = new THREE.MeshStandardMaterial({
      color: THEME.earthBlue,
      roughness: 0.4,
      metalness: 0.1,
      side: THREE.DoubleSide
    });
    const earthMesh = new THREE.Mesh(earthGeo, earthMat);
    earthGroup.add(earthMesh);

    // Mantle Cutaway
    const mantleGeo = new THREE.SphereGeometry(R_E * 0.7, 32, 32, 0, Math.PI * 1.5, 0, Math.PI);
    const mantleMat = new THREE.MeshStandardMaterial({
      color: THEME.earthMantle,
      roughness: 0.5,
      side: THREE.DoubleSide
    });
    const mantleMesh = new THREE.Mesh(mantleGeo, mantleMat);
    earthGroup.add(mantleMesh);

    // Core Cutaway
    const coreGeo = new THREE.SphereGeometry(R_E * 0.35, 32, 32, 0, Math.PI * 1.5, 0, Math.PI);
    const coreMat = new THREE.MeshStandardMaterial({
      color: THEME.earthCore,
      emissive: 0xb91c1c,
      emissiveIntensity: 0.3,
      side: THREE.DoubleSide
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    earthGroup.add(coreMesh);

    // Cutaway Section Flat Planes
    const planeGeo = new THREE.PlaneGeometry(R_E, R_E);
    const planeMat = new THREE.MeshStandardMaterial({ color: 0x334155, side: THREE.DoubleSide });
    const cut1 = new THREE.Mesh(planeGeo, planeMat);
    cut1.position.set(R_E / 2, 0, 0);
    cut1.rotation.y = Math.PI / 2;
    earthGroup.add(cut1);

    // Equator / Orbit Ring
    const ringGeo = new THREE.RingGeometry(R_E - 0.05, R_E + 0.05, 64);
    const ringMat = new THREE.MeshBasicMaterial({ color: THEME.vectorGreen, side: THREE.DoubleSide });
    const surfaceRing = new THREE.Mesh(ringGeo, ringMat);
    surfaceRing.rotation.x = Math.PI / 2;
    earthGroup.add(surfaceRing);

    // Probe Test Particle
    const probeGeo = new THREE.SphereGeometry(0.5, 16, 16);
    const probeMat = new THREE.MeshStandardMaterial({ color: 0xfacc15, emissive: 0xeab308, emissiveIntensity: 0.5 });
    const probe = new THREE.Mesh(probeGeo, probeMat);
    probe.position.set(R_E, 0, 0);
    earthGroup.add(probe);

    // Gravity Vector Arrow on Probe pointing towards centre
    const gArrow = new THREE.ArrowHelper(new THREE.Vector3(-1, 0, 0), probe.position, 3.5, THEME.vectorRed, 0.8, 0.4);
    earthGroup.add(gArrow);

    // UI Slider hookups
    const gSlider = document.getElementById('g-pos-slider');
    const gValText = document.getElementById('g-val-display');
    const gDescText = document.getElementById('g-desc-display');

    function updateProbePosition(rFactor) {
      // rFactor: 0 (Centre) -> 1.0 (Surface R_E) -> 2.5 (High Altitude 2.5 R_E)
      const currentRadius = R_E * rFactor;
      probe.position.set(currentRadius, 0, 0);

      let gValue = 9.8;
      let gArrowLen = 3.5;
      let statusDesc = "";

      if (rFactor <= 1.0) {
        // Inside Earth (Depth d): g(d) = g * (1 - d/R) = g * r/R
        gValue = 9.8 * rFactor;
        gArrowLen = 3.5 * rFactor;
        const depthKm = ((1 - rFactor) * 6400).toFixed(0);
        statusDesc = rFactor === 0
          ? "Centre of Earth (d = R_E) ➔ Net Gravity g = 0 m/s² (Weightlessness)"
          : `Inside Earth (Depth d = ${depthKm} km) ➔ g = g₀(1 - d/R) = ${gValue.toFixed(2)} m/s² (Linear)`;
      } else {
        // Outside Earth (Altitude h): g(h) = g / (1 + h/R)^2
        gValue = 9.8 / (rFactor * rFactor);
        gArrowLen = 3.5 / (rFactor * rFactor);
        const altKm = ((rFactor - 1) * 6400).toFixed(0);
        statusDesc = `Above Surface (Altitude h = ${altKm} km) ➔ g = GM/(R+h)² = ${gValue.toFixed(2)} m/s² (Inverse-Square)`;
      }

      gArrow.position.copy(probe.position);
      gArrow.setDirection(new THREE.Vector3(-1, 0, 0));
      gArrow.setLength(Math.max(0.4, gArrowLen), 0.6, 0.3);

      if (gValText) gValText.textContent = `${gValue.toFixed(2)} m/s²`;
      if (gDescText) gDescText.textContent = statusDesc;
    }

    if (gSlider) {
      gSlider.addEventListener('input', (e) => {
        updateProbePosition(parseFloat(e.target.value));
      });
    }

    updateProbePosition(1.0);

    function animate() {
      requestAnimationFrame(animate);
      earthGroup.rotation.x = rotation.x;
      earthGroup.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     3. SIMULATION: Escape Velocity & Gravitational Potential Energy
     ========================================================================= */
  function initEscapeVelocitySimulation() {
    const setup = create3DCanvas('three-escape-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 16, 28);
    camera.lookAt(0, 0, 0);

    const worldGroup = new THREE.Group();
    scene.add(worldGroup);

    // Planet Earth
    const earthR = 5.0;
    const earthGeo = new THREE.SphereGeometry(earthR, 32, 32);
    const earthMat = new THREE.MeshStandardMaterial({ color: THEME.earthBlue, roughness: 0.3 });
    const earth = new THREE.Mesh(earthGeo, earthMat);
    worldGroup.add(earth);

    // Launch Cannon on North Pole
    const cannonGeo = new THREE.CylinderGeometry(0.3, 0.4, 1.2, 16);
    const cannonMat = new THREE.MeshStandardMaterial({ color: 0x475569 });
    const cannon = new THREE.Mesh(cannonGeo, cannonMat);
    cannon.position.set(0, earthR + 0.6, 0);
    worldGroup.add(cannon);

    // Projectile Rocket
    const rocketGeo = new THREE.ConeGeometry(0.35, 0.9, 16);
    const rocketMat = new THREE.MeshStandardMaterial({ color: 0xef4444, emissive: 0xb91c1c, emissiveIntensity: 0.6 });
    const rocket = new THREE.Mesh(rocketGeo, rocketMat);
    worldGroup.add(rocket);

    // Trajectory Line
    let trajLine = null;

    let vLaunch = 11.2; // km/s
    let isLaunching = false;
    let projT = 0;
    let projPath = [];

    function calculateTrajectory(v0) {
      projPath = [];
      const GM = 120; // Simulated gravitational parameter
      let r = earthR + 0.6;
      let vr = (v0 / 11.2) * 4.2; // Normalized initial radial velocity
      let vt = 1.1; // Small tangential velocity component
      let theta = Math.PI / 2;
      const dt = 0.05;

      for (let step = 0; step < 400; step++) {
        const x = r * Math.cos(theta);
        const y = r * Math.sin(theta);
        projPath.push(new THREE.Vector3(x, y, 0));

        // Gravitational acceleration a = -GM / r^2
        const ar = -GM / (r * r) + (vt * vt) / r;
        const at = -(vr * vt) / r;

        vr += ar * dt;
        vt += at * dt;
        r += vr * dt;
        theta += (vt / r) * dt;

        // Crash on Earth surface
        if (r < earthR) {
          projPath.push(new THREE.Vector3(earthR * Math.cos(theta), earthR * Math.sin(theta), 0));
          break;
        }
        // Escaped beyond boundary
        if (r > 35) break;
      }

      if (trajLine) worldGroup.remove(trajLine);
      const trajGeo = new THREE.BufferGeometry().setFromPoints(projPath);
      const isEscape = v0 >= 11.2;
      const trajColor = isEscape ? THEME.vectorGreen : v0 >= 7.9 ? THEME.vectorRed : THEME.sunGold;
      const trajMat = new THREE.LineBasicMaterial({ color: trajColor, linewidth: 2 });
      trajLine = new THREE.Line(trajGeo, trajMat);
      worldGroup.add(trajLine);
    }

    const launchSlider = document.getElementById('escape-speed-slider');
    const launchValText = document.getElementById('escape-speed-val');
    const launchStatus = document.getElementById('escape-status-display');
    const launchBtn = document.getElementById('escape-launch-btn');

    function updateLaunchInfo(speed) {
      vLaunch = speed;
      if (launchValText) launchValText.textContent = `${speed.toFixed(1)} km/s`;
      let status = "";
      if (speed < 7.92) {
        status = "Sub-orbital Trajectory: Speed < 7.92 km/s ➔ Projectile falls back to Earth surface.";
      } else if (speed >= 7.92 && speed < 11.2) {
        status = "Closed Elliptical Orbit: 7.92 km/s ≤ Speed < 11.2 km/s ➔ Bound satellite orbit (Total Energy E < 0).";
      } else if (Math.abs(speed - 11.2) < 0.05) {
        status = "Parabolic Escape Trajectory: Speed = 11.2 km/s (Escape Speed) ➔ Total Energy E = 0, escapes to infinity.";
      } else {
        status = "Hyperbolic Unbound Path: Speed > 11.2 km/s ➔ Total Energy E > 0, escapes with surplus residual kinetic energy.";
      }
      if (launchStatus) launchStatus.textContent = status;
      calculateTrajectory(speed);
    }

    if (launchSlider) {
      launchSlider.addEventListener('input', (e) => {
        updateLaunchInfo(parseFloat(e.target.value));
      });
    }

    if (launchBtn) {
      launchBtn.addEventListener('click', () => {
        isLaunching = true;
        projT = 0;
      });
    }

    updateLaunchInfo(11.2);

    function animate() {
      requestAnimationFrame(animate);

      if (isLaunching && projPath.length > 0) {
        projT += 1;
        if (projT < projPath.length) {
          rocket.position.copy(projPath[projT]);
          if (projT < projPath.length - 1) {
            const dir = new THREE.Vector3().subVectors(projPath[projT + 1], projPath[projT]).normalize();
            rocket.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir);
          }
        } else {
          isLaunching = false;
        }
      } else if (!isLaunching && projPath.length > 0) {
        rocket.position.copy(projPath[0]);
      }

      worldGroup.rotation.x = rotation.x;
      worldGroup.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  /* =========================================================================
     4. SIMULATION: Earth Satellites & Orbital Mechanics (LEO, Polar, Geo)
     ========================================================================= */
  function initSatelliteSimulation() {
    const setup = create3DCanvas('three-satellite-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    camera.position.set(0, 18, 28);
    camera.lookAt(0, 0, 0);

    const satWorld = new THREE.Group();
    scene.add(satWorld);

    // Earth Sphere
    const earthR = 5.0;
    const earthGeo = new THREE.SphereGeometry(earthR, 32, 32);
    const earthMat = new THREE.MeshStandardMaterial({ color: THEME.earthBlue, roughness: 0.3 });
    const earth = new THREE.Mesh(earthGeo, earthMat);
    satWorld.add(earth);

    // Earth Rotation Axis
    const axisGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, -earthR - 2, 0), new THREE.Vector3(0, earthR + 2, 0)]);
    const axisMat = new THREE.LineBasicMaterial({ color: 0x94a3b8 });
    satWorld.add(new THREE.Line(axisGeo, axisMat));

    // Satellite Models & Orbits
    // 1. Geostationary Orbit (r = 15.0, T = 24h period sync with Earth)
    const geoR = 15.0;
    const geoCurve = new THREE.EllipseCurve(0, 0, geoR, geoR, 0, 2 * Math.PI, false, 0);
    const geoGeo = new THREE.BufferGeometry().setFromPoints(geoCurve.getPoints(64));
    const geoMat = new THREE.LineBasicMaterial({ color: THEME.sunGold, transparent: true, opacity: 0.6 });
    const geoOrbit = new THREE.Line(geoGeo, geoMat);
    geoOrbit.rotation.x = Math.PI / 2;
    satWorld.add(geoOrbit);

    const geoSat = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.4, 0.4), new THREE.MeshStandardMaterial({ color: THEME.sunGold }));
    satWorld.add(geoSat);

    // 2. Polar Orbit (r = 6.2, inclined at 90 deg)
    const polarR = 6.4;
    const polarCurve = new THREE.EllipseCurve(0, 0, polarR, polarR, 0, 2 * Math.PI, false, 0);
    const polarGeo = new THREE.BufferGeometry().setFromPoints(polarCurve.getPoints(64));
    const polarMat = new THREE.LineBasicMaterial({ color: THEME.vectorGreen, transparent: true, opacity: 0.7 });
    const polarOrbit = new THREE.Line(polarGeo, polarMat);
    satWorld.add(polarOrbit);

    const polarSat = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 0.8, 8), new THREE.MeshStandardMaterial({ color: THEME.vectorGreen }));
    satWorld.add(polarSat);

    // 3. Low Earth Orbit (LEO) (r = 5.6, slight inclination)
    const leoR = 5.6;
    const leoCurve = new THREE.EllipseCurve(0, 0, leoR, leoR, 0, 2 * Math.PI, false, 0);
    const leoGeo = new THREE.BufferGeometry().setFromPoints(leoCurve.getPoints(64));
    const leoMat = new THREE.LineBasicMaterial({ color: THEME.planetPurple, transparent: true, opacity: 0.8 });
    const leoOrbit = new THREE.Line(leoGeo, leoMat);
    leoOrbit.rotation.x = Math.PI / 2.3;
    satWorld.add(leoOrbit);

    const leoSat = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), new THREE.MeshStandardMaterial({ color: THEME.planetPurple }));
    satWorld.add(leoSat);

    let angleGeo = 0;
    let anglePolar = 0;
    let angleLEO = 0;

    function animate() {
      requestAnimationFrame(animate);

      // Earth rotation (24h period)
      earth.rotation.y += 0.008;

      // Geostationary satellite: exactly synchronised with Earth rotation
      angleGeo += 0.008;
      geoSat.position.set(geoR * Math.cos(angleGeo), 0, geoR * Math.sin(angleGeo));

      // Polar satellite: rapid 100-minute orbit across poles
      anglePolar += 0.035;
      polarSat.position.set(polarR * Math.cos(anglePolar), polarR * Math.sin(anglePolar), 0);

      // LEO satellite: 85-minute fast orbital period
      angleLEO += 0.045;
      leoSat.position.set(
        leoR * Math.cos(angleLEO),
        leoR * Math.sin(angleLEO) * Math.sin(Math.PI / 2.3),
        leoR * Math.sin(angleLEO) * Math.cos(Math.PI / 2.3)
      );

      satWorld.rotation.x = rotation.x;
      satWorld.rotation.y = rotation.y;
      renderer.render(scene, camera);
    }
    animate();
  }

  // --- Auto-Initialize on DOM Loaded or Dynamic Call ---
  function initAllGravitation3D() {
    initKeplerSimulation();
    initGravityVariationSimulation();
    initEscapeVelocitySimulation();
    initSatelliteSimulation();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllGravitation3D);
  } else {
    initAllGravitation3D();
  }
})();
