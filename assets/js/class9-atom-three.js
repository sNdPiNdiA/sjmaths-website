/**
 * SJMaths - Class 9 Advanced Science Chapter 6: Structure of Atom
 * Interactive 3D Physics & Chemistry Concept Visualizers powered by Three.js
 *
 * Visualizations included:
 * 1. 3D Cathode Ray Discharge Tube (Negative electron beam deflection in Electric Plate fields)
 * 2. 3D Rutherford Alpha Gold Foil Scattering (Alpha particles shot towards Gold nucleus +79e, Coulomb deflection)
 * 3. 3D Bohr Hydrogen Atom Orbit Transitions (Quantized energy levels n=1..4, Photon emission/absorption waves)
 */

(() => {
  "use strict";

  if (typeof THREE === "undefined") {
    console.warn("Three.js not yet loaded for Class 9 Chapter 6. Retrying on window load.");
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
    neonGreen: 0x22c55e,
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
  // SIMULATION 1: 3D Cathode Ray Tube Discharge Deflection
  // ========================================================
  function init3DCathodeRaySim() {
    const setup = create3DScene('three-crt-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Glass Tube
    const tubeGeo = new THREE.CylinderGeometry(1.8, 1.8, 14, 32);
    tubeGeo.rotateZ(Math.PI / 2);
    const tubeMat = new THREE.MeshStandardMaterial({
      color: 0x38bdf8,
      transparent: true,
      opacity: 0.15,
      roughness: 0.1
    });
    const glassTube = new THREE.Mesh(tubeGeo, tubeMat);
    scene.add(glassTube);

    // Cathode Disk (-) Left
    const cathodeDisk = new THREE.Mesh(
      new THREE.CylinderGeometry(1.2, 1.2, 0.2, 24),
      new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.8 })
    );
    cathodeDisk.rotation.z = Math.PI / 2;
    cathodeDisk.position.x = -6.5;
    scene.add(cathodeDisk);

    // Anode Ring (+) Center
    const anodeRing = new THREE.Mesh(
      new THREE.TorusGeometry(1.0, 0.15, 16, 32),
      new THREE.MeshStandardMaterial({ color: THEME.gold, metalness: 0.9 })
    );
    anodeRing.rotation.y = Math.PI / 2;
    anodeRing.position.x = -3.5;
    scene.add(anodeRing);

    // Top & Bottom Electric Deflection Plates
    const topPlate = new THREE.Mesh(
      new THREE.BoxGeometry(4, 0.15, 2),
      new THREE.MeshStandardMaterial({ color: 0x475569 })
    );
    topPlate.position.set(0.5, 1.6, 0);
    scene.add(topPlate);

    const botPlate = new THREE.Mesh(
      new THREE.BoxGeometry(4, 0.15, 2),
      new THREE.MeshStandardMaterial({ color: 0x475569 })
    );
    botPlate.position.set(0.5, -1.6, 0);
    scene.add(botPlate);

    // Fluorescent Phosphor Screen (Right)
    const screenGeo = new THREE.CylinderGeometry(1.7, 1.7, 0.2, 32);
    screenGeo.rotateZ(Math.PI / 2);
    const screenMat = new THREE.MeshStandardMaterial({ color: 0x14532d, roughness: 0.4 });
    const screenMesh = new THREE.Mesh(screenGeo, screenMat);
    screenMesh.position.x = 6.9;
    scene.add(screenMesh);

    // Electron Beam Path (Glowing Green Line)
    const beamGroup = new THREE.Group();
    scene.add(beamGroup);

    // Glowing Spot on Screen
    const spotMesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.22, 16, 16),
      new THREE.MeshStandardMaterial({ color: 0x4ade80, emissive: 0x22c55e, emissiveIntensity: 1.0 })
    );
    scene.add(spotMesh);

    let plateState = 0; // 0 = OFF, +1 = Top Plate (+), -1 = Top Plate (-)

    function updateBeam() {
      while (beamGroup.children.length > 0) {
        beamGroup.remove(beamGroup.children[0]);
      }

      const points = [];
      const steps = 40;
      for (let i = 0; i <= steps; i++) {
        const t = i / steps;
        const px = -6.5 + t * 13.4;
        let py = 0;
        if (px > -1.5) {
          const bendT = (px + 1.5) / 8.4;
          if (plateState === 1) {
            py = Math.pow(bendT, 1.6) * 1.1; // Attracted towards positive top plate
          } else if (plateState === -1) {
            py = -Math.pow(bendT, 1.6) * 1.1; // Repelled by negative top plate
          }
        }
        points.push(new THREE.Vector3(px, py, 0));
      }

      const curve = new THREE.CatmullRomCurve3(points);
      const tube = new THREE.Mesh(
        new THREE.TubeGeometry(curve, 50, 0.08, 8, false),
        new THREE.MeshStandardMaterial({ color: THEME.neonGreen, emissive: 0x22c55e, emissiveIntensity: 0.8 })
      );
      beamGroup.add(tube);

      const lastP = points[points.length - 1];
      spotMesh.position.set(lastP.x, lastP.y, lastP.z);

      // Update plate colors
      if (plateState === 1) {
        topPlate.material.color.setHex(0xe11d48); // Positive (+) Red
        botPlate.material.color.setHex(0x0284c7); // Negative (-) Blue
      } else if (plateState === -1) {
        topPlate.material.color.setHex(0x0284c7); // Negative (-) Blue
        botPlate.material.color.setHex(0xe11d48); // Positive (+) Red
      } else {
        topPlate.material.color.setHex(0x475569);
        botPlate.material.color.setHex(0x475569);
      }

      const hud = document.getElementById('three-crt-hud');
      if (hud) {
        if (plateState === 1) {
          hud.innerHTML = `Electric Field: <strong class="badge badge-rose">Top Plate (+) / Bottom Plate (−)</strong><br>
            Beam Observation: <strong class="badge badge-emerald">Deflects Upward towards (+) plate</strong> &rarr; Proves cathode rays consist of <em>negatively charged electrons</em> ($e^-$).`;
        } else if (plateState === -1) {
          hud.innerHTML = `Electric Field: <strong class="badge badge-blue">Top Plate (−) / Bottom Plate (+)</strong><br>
            Beam Observation: <strong class="badge badge-rose">Deflects Downward away from (−) plate</strong> &rarr; Confirms electrostatic repulsion from like negative charge.`;
        } else {
          hud.innerHTML = `Electric Field: <strong class="badge badge-cyan">OFF (Field Free Region)</strong><br>
            Beam Observation: <strong class="badge badge-emerald">Straight Line Motion</strong> along discharge axis according to Newton's 1st Law.`;
        }
      }
    }

    const btnOff = document.getElementById('btn-crt-off');
    const btnPos = document.getElementById('btn-crt-pos');
    const btnNeg = document.getElementById('btn-crt-neg');

    function setField(val) {
      plateState = val;
      [btnOff, btnPos, btnNeg].forEach(b => { if (b) b.classList.remove('active'); });
      if (val === 0 && btnOff) btnOff.classList.add('active');
      if (val === 1 && btnPos) btnPos.classList.add('active');
      if (val === -1 && btnNeg) btnNeg.classList.add('active');
      updateBeam();
    }

    if (btnOff) btnOff.addEventListener('click', () => setField(0));
    if (btnPos) btnPos.addEventListener('click', () => setField(1));
    if (btnNeg) btnNeg.addEventListener('click', () => setField(-1));

    updateBeam();

    function animate() {
      requestAnimationFrame(animate);
      const camRadius = 17;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 2;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 2: 3D Rutherford Alpha Scattering
  // ========================================================
  function init3DRutherfordSim() {
    const setup = create3DScene('three-rutherford-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Central Gold Nucleus (+79e)
    const nucleusGroup = new THREE.Group();
    const nucCore = new THREE.Mesh(
      new THREE.SphereGeometry(1.2, 24, 24),
      new THREE.MeshStandardMaterial({ color: THEME.gold, metalness: 0.8, roughness: 0.2, emissive: 0xd97706, emissiveIntensity: 0.3 })
    );
    nucleusGroup.add(nucCore);
    scene.add(nucleusGroup);

    // Alpha Particle (m = 4u, q = +2e)
    const alphaMesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.35, 16, 16),
      new THREE.MeshStandardMaterial({ color: THEME.rose, emissive: 0xe11d48, emissiveIntensity: 0.6 })
    );
    scene.add(alphaMesh);

    // Trajectory Line
    const trailLineGroup = new THREE.Group();
    scene.add(trailLineGroup);

    let impactParam = 1.5; // b (offset in Y/Z)
    let isFiring = false;
    let alphaX = -12;
    let alphaY = impactParam;

    function renderTrajectory(points) {
      while (trailLineGroup.children.length > 0) {
        trailLineGroup.remove(trailLineGroup.children[0]);
      }
      if (points.length < 2) return;
      const geo = new THREE.BufferGeometry().setFromPoints(points);
      const line = new THREE.Line(geo, new THREE.LineBasicMaterial({ color: THEME.rose, linewidth: 2 }));
      trailLineGroup.add(line);
    }

    const sliderImpact = document.getElementById('slider-rutherford-b');
    const btnShoot = document.getElementById('btn-rutherford-shoot');
    const hud = document.getElementById('three-rutherford-hud');

    function updateParams() {
      const b = impactParam;
      const C = 2.0; // Coulomb factor
      let angleDeg = 0;
      if (Math.abs(b) > 0.05) {
        const rad = 2 * Math.atan(C / Math.abs(b));
        angleDeg = (rad * 180) / Math.PI;
      } else {
        angleDeg = 180; // Head-on rebound
      }

      if (hud) {
        hud.innerHTML = `Impact Parameter: <strong>b = ${b.toFixed(1)} fm</strong> | Gold Nucleus: <strong class="badge badge-amber">+79e</strong><br>
          Scattering Angle: <strong class="badge badge-rose">θ ≈ ${angleDeg.toFixed(0)}°</strong> (${b < 0.8 ? 'Massive Back-Scattering (Discovery of dense Nucleus)' : 'Small Angle Deflection'})`;
      }
    }

    if (sliderImpact) {
      sliderImpact.addEventListener('input', (e) => {
        impactParam = parseFloat(e.target.value);
        alphaY = impactParam;
        alphaX = -12;
        alphaMesh.position.set(alphaX, alphaY, 0);
        isFiring = false;
        renderTrajectory([]);
        updateParams();
      });
    }

    if (btnShoot) {
      btnShoot.addEventListener('click', () => {
        alphaX = -12;
        alphaY = impactParam;
        isFiring = true;
      });
    }

    alphaMesh.position.set(-12, impactParam, 0);
    updateParams();

    let trajPoints = [];
    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      if (isFiring) {
        alphaX += 16 * dt;

        const b = impactParam;
        const C = 2.0;
        const dx = alphaX;
        const distSq = dx * dx + b * b + 0.1;
        const dyShift = (C * 4.0) / (Math.sqrt(distSq) + Math.abs(dx));

        if (Math.abs(b) < 0.2 && dx >= 0) {
          // Rebound 180 deg
          const backX = -dx;
          alphaMesh.position.set(backX, 0, 0);
          trajPoints.push(new THREE.Vector3(backX, 0, 0));
        } else {
          const currentY = b >= 0 ? b + dyShift : b - dyShift;
          alphaMesh.position.set(alphaX, currentY, 0);
          trajPoints.push(new THREE.Vector3(alphaX, currentY, 0));
        }

        renderTrajectory(trajPoints);

        if (alphaX > 14) {
          isFiring = false;
          trajPoints = [];
        }
      }

      const camRadius = 17;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 2;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  // ========================================================
  // SIMULATION 3: 3D Bohr Model Energy Transitions
  // ========================================================
  function init3DBohrSim() {
    const setup = create3DScene('three-bohr-canvas');
    if (!setup) return;
    const { scene, camera, renderer, rotation } = setup;

    // Nucleus (Proton +1e)
    const nucleus = new THREE.Mesh(
      new THREE.SphereGeometry(0.65, 20, 20),
      new THREE.MeshStandardMaterial({ color: THEME.rose, emissive: 0xe11d48, emissiveIntensity: 0.5 })
    );
    scene.add(nucleus);

    // Discrete Circular Energy Shells (n = 1, 2, 3, 4)
    const shellRadii = [2.2, 4.2, 6.2, 8.2];
    shellRadii.forEach((r, idx) => {
      const ringGeo = new THREE.RingGeometry(r - 0.04, r + 0.04, 64);
      const ringMat = new THREE.MeshBasicMaterial({ color: 0x334155, side: THREE.DoubleSide });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.x = Math.PI / 2;
      scene.add(ring);
    });

    // Orbiting Electron
    const electronMesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.35, 16, 16),
      new THREE.MeshStandardMaterial({ color: THEME.cyan, emissive: 0x0891b2, emissiveIntensity: 0.8 })
    );
    scene.add(electronMesh);

    // Emitted Photon Wave Pulse
    const photonMesh = new THREE.Mesh(
      new THREE.SphereGeometry(0.25, 12, 12),
      new THREE.MeshStandardMaterial({ color: THEME.gold, emissive: 0xfacc15, emissiveIntensity: 1.0 })
    );
    photonMesh.visible = false;
    scene.add(photonMesh);

    let currentN = 3;
    let targetN = 2;
    let electronRadius = shellRadii[currentN - 1];
    let orbitTheta = 0;

    const btnBalmerA = document.getElementById('btn-bohr-h-alpha');
    const btnBalmerB = document.getElementById('btn-bohr-h-beta');
    const btnAbsorb = document.getElementById('btn-bohr-absorb');
    const hud = document.getElementById('three-bohr-hud');

    function triggerTransition(fromN, toN, label, colorHex, wavelengthNm) {
      currentN = toN;
      electronRadius = shellRadii[toN - 1];

      // Emit photon
      photonMesh.position.set(0, 0, 0);
      photonMesh.visible = true;
      photonMesh.material.color.setHex(colorHex);

      if (hud) {
        if (fromN > toN) {
          hud.innerHTML = `Transition: <strong class="badge badge-emerald">${label} (n = ${fromN} &rarr; ${toN})</strong><br>
            Energy Released: <strong class="badge badge-cyan">&Delta;E = E_${fromN} &minus; E_${toN}</strong> | Photon Emitted: <strong class="badge badge-amber">&lambda; = ${wavelengthNm} nm (Visible Red/Cyan Line)</strong>`;
        } else {
          hud.innerHTML = `Transition: <strong class="badge badge-rose">${label} (n = ${fromN} &rarr; ${toN})</strong><br>
            Energy Absorbed: <strong class="badge badge-purple">&Delta;E = E_${toN} &minus; E_${fromN}</strong> | Photon Absorbed from radiation field to excite electron.`;
        }
      }
    }

    if (btnBalmerA) {
      btnBalmerA.addEventListener('click', () => {
        triggerTransition(3, 2, 'Balmer H-α', 0xe11d48, '656.3');
      });
    }

    if (btnBalmerB) {
      btnBalmerB.addEventListener('click', () => {
        triggerTransition(4, 2, 'Balmer H-β', 0x0284c7, '486.1');
      });
    }

    if (btnAbsorb) {
      btnAbsorb.addEventListener('click', () => {
        triggerTransition(1, 3, 'Absorption Excitation', 0x7c3aed, '102.6');
      });
    }

    let clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      const dt = clock.getDelta();

      orbitTheta += (2.5 / (currentN * 0.8)) * dt;
      electronMesh.position.x = electronRadius * Math.cos(orbitTheta);
      electronMesh.position.z = electronRadius * Math.sin(orbitTheta);

      if (photonMesh.visible) {
        photonMesh.position.x += 12 * dt;
        photonMesh.position.y += 6 * dt;
        if (photonMesh.position.length() > 14) {
          photonMesh.visible = false;
        }
      }

      const camRadius = 18;
      camera.position.x = camRadius * Math.sin(rotation.y) * Math.cos(rotation.x);
      camera.position.y = camRadius * Math.sin(rotation.x) + 7;
      camera.position.z = camRadius * Math.cos(rotation.y) * Math.cos(rotation.x);
      camera.lookAt(0, 0, 0);

      renderer.render(scene, camera);
    }
    animate();
  }

  function initAllVisualizers() {
    init3DCathodeRaySim();
    init3DRutherfordSim();
    init3DBohrSim();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAllVisualizers);
  } else {
    initAllVisualizers();
  }
})();
