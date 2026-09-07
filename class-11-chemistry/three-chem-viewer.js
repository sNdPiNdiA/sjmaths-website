/**
 * three-chem-viewer.js
 * Interactive Three.js 3D Models for Class 11 Chemistry
 * High-performance, mobile-responsive, dark-mode aware WebGL visualizations.
 * Includes:
 *   1. Rutherford Alpha Scattering Experiment 3D Simulator
 *   2. Bohr's Planetary Hydrogen Atom & Spectral Photon Transitions
 *   3. 3D Atomic Orbitals & Nodal Surfaces ($s, p_x, p_y, p_z, d_{z^2}, d_{x^2-y^2}, d_{xy}, d_{yz}, d_{xz}$)
 */

(function () {
    'use strict';

    if (typeof THREE === 'undefined') {
        console.warn('Three.js not loaded. ThreeChemViewer requires THREE to be available globally.');
        return;
    }

    // Shared theme helper
    function isDarkMode() {
        return document.body.classList.contains('dark-mode') || document.documentElement.classList.contains('dark-mode');
    }

    // =========================================================================
    // 1. RUTHERFORD ALPHA SCATTERING 3D SIMULATOR
    // =========================================================================
    class RutherfordViewer {
        constructor(container) {
            this.container = container;
            this.scene = null;
            this.camera = null;
            this.renderer = null;
            this.particles = [];
            this.nuclei = [];
            this.goldFoil = null;
            this.animId = null;
            this.isVisible = false;
            this.speed = 1.0;
            this.isPaused = false;

            // Mouse orbit rotation
            this.isDragging = false;
            this.previousMousePosition = { x: 0, y: 0 };
            this.rotationSpeed = 0.005;

            this.init();
        }

        init() {
            const width = this.container.clientWidth || 600;
            const height = 340;

            this.scene = new THREE.Scene();
            this.updateBackground();

            this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
            this.camera.position.set(0, 50, 160);
            this.camera.lookAt(0, 0, 0);

            this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            this.renderer.setSize(width, height);
            this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            this.container.appendChild(this.renderer.domElement);

            // Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
            this.scene.add(ambientLight);
            const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
            dirLight.position.set(50, 100, 80);
            this.scene.add(dirLight);

            // Central Gold Atom with concentrated positive nucleus
            this.createGoldLattice();

            // Event Listeners
            this.setupInteraction();
            this.setupObserver();
            this.createUI();

            // Resize
            window.addEventListener('resize', () => this.onResize());
        }

        updateBackground() {
            if (this.scene) {
                this.scene.background = new THREE.Color(isDarkMode() ? 0x0f172a : 0xf8fafc);
            }
        }

        createGoldLattice() {
            // Gold nuclei representation (heavy positive centers)
            const nucleusGeo = new THREE.SphereGeometry(3.5, 24, 24);
            const goldMat = new THREE.MeshStandardMaterial({
                color: 0xf59e0b,
                metalness: 0.8,
                roughness: 0.2,
                emissive: 0xd97706,
                emissiveIntensity: 0.3
            });

            // Thin gold foil plane representation
            const foilGeo = new THREE.BoxGeometry(90, 80, 2);
            const foilMat = new THREE.MeshStandardMaterial({
                color: 0xfef08a,
                transparent: true,
                opacity: 0.15,
                metalness: 0.9,
                roughness: 0.1
            });
            this.goldFoil = new THREE.Mesh(foilGeo, foilMat);
            this.scene.add(this.goldFoil);

            // Place a 3x3 grid of gold nuclei with one prominent central nucleus
            const spacing = 26;
            for (let i = -1; i <= 1; i++) {
                for (let j = -1; j <= 1; j++) {
                    const nucleus = new THREE.Mesh(nucleusGeo, goldMat);
                    nucleus.position.set(i * spacing, j * spacing, 0);
                    this.scene.add(nucleus);
                    this.nuclei.push(nucleus.position);

                    // Nucleus label (+)
                    const ringGeo = new THREE.RingGeometry(4.2, 4.8, 20);
                    const ringMat = new THREE.MeshBasicMaterial({ color: 0xef4444, side: THREE.DoubleSide });
                    const ring = new THREE.Mesh(ringGeo, ringMat);
                    ring.position.copy(nucleus.position);
                    this.scene.add(ring);
                }
            }

            // ZnS Detection Screen Ring (Circular phosphorescent screen)
            const screenCurve = new THREE.EllipseCurve(0, 0, 75, 75, 0, 2 * Math.PI, false, 0);
            const points = screenCurve.getPoints(50);
            const screenGeo = new THREE.BufferGeometry().setFromPoints(points);
            const screenMat = new THREE.LineDashedMaterial({
                color: 0x10b981,
                dashSize: 3,
                gapSize: 2,
                linewidth: 2
            });
            const screenLine = new THREE.Line(screenGeo, screenMat);
            screenLine.computeLineDistances();
            screenLine.rotation.x = Math.PI / 2;
            this.scene.add(screenLine);
        }

        spawnAlphaParticle() {
            // High energy alpha particle (He2+)
            const pGeo = new THREE.SphereGeometry(1.2, 12, 12);
            const pMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
            const mesh = new THREE.Mesh(pGeo, pMat);

            // Start beam from source at Z = -75, scattered in X and Y
            const rx = (Math.random() - 0.5) * 55;
            const ry = (Math.random() - 0.5) * 50;
            mesh.position.set(rx, ry, -75);

            const velocity = new THREE.Vector3(0, 0, 2.2 * this.speed);

            this.scene.add(mesh);
            this.particles.push({ mesh, velocity, life: 0 });
        }

        setupInteraction() {
            const dom = this.renderer.domElement;
            dom.style.cursor = 'grab';

            dom.addEventListener('mousedown', (e) => {
                this.isDragging = true;
                this.previousMousePosition = { x: e.clientX, y: e.clientY };
                dom.style.cursor = 'grabbing';
            });

            window.addEventListener('mouseup', () => {
                this.isDragging = false;
                if (dom) dom.style.cursor = 'grab';
            });

            dom.addEventListener('mousemove', (e) => {
                if (!this.isDragging) return;
                const deltaX = e.clientX - this.previousMousePosition.x;
                const deltaY = e.clientY - this.previousMousePosition.y;

                this.scene.rotation.y += deltaX * this.rotationSpeed;
                this.scene.rotation.x += deltaY * this.rotationSpeed;

                this.previousMousePosition = { x: e.clientX, y: e.clientY };
            });

            // Touch support
            dom.addEventListener('touchstart', (e) => {
                if (e.touches.length === 1) {
                    this.isDragging = true;
                    this.previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
                }
            }, { passive: true });

            dom.addEventListener('touchmove', (e) => {
                if (!this.isDragging || e.touches.length !== 1) return;
                const deltaX = e.touches[0].clientX - this.previousMousePosition.x;
                const deltaY = e.touches[0].clientY - this.previousMousePosition.y;

                this.scene.rotation.y += deltaX * this.rotationSpeed * 1.5;
                this.scene.rotation.x += deltaY * this.rotationSpeed * 1.5;

                this.previousMousePosition = { x: e.touches[0].clientX, y: e.touches[0].clientY };
            }, { passive: true });

            dom.addEventListener('touchend', () => {
                this.isDragging = false;
            });
        }

        setupObserver() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    this.isVisible = entry.isIntersecting;
                    if (this.isVisible && !this.animId) {
                        this.animate();
                    }
                });
            }, { threshold: 0.1 });
            observer.observe(this.container);
        }

        createUI() {
            const uiDiv = document.createElement('div');
            uiDiv.className = 'three-chem-controls';
            uiDiv.style.cssText = 'display:flex; flex-wrap:wrap; gap:8px; align-items:center; justify-content:center; margin-top:10px; font-size:12px;';

            uiDiv.innerHTML = `
                <button class="chem-3d-btn active" data-action="toggle">⏸ Pause</button>
                <button class="chem-3d-btn" data-action="reset-cam">🔄 Reset View</button>
                <button class="chem-3d-btn" data-action="aim-center">🎯 Head-on Nucleus Hit (~1/20,000)</button>
                <span style="color:var(--chem-muted); font-size:11px; margin-left:8px;">Drag to rotate in 3D • Gold Nuclei (+e)</span>
            `;

            uiDiv.addEventListener('click', (e) => {
                const btn = e.target.closest('button');
                if (!btn) return;
                const action = btn.dataset.action;
                if (action === 'toggle') {
                    this.isPaused = !this.isPaused;
                    btn.textContent = this.isPaused ? '▶ Play' : '⏸ Pause';
                } else if (action === 'reset-cam') {
                    this.scene.rotation.set(0, 0, 0);
                    this.camera.position.set(0, 50, 160);
                    this.camera.lookAt(0, 0, 0);
                } else if (action === 'aim-center') {
                    // Fire dedicated central particles for direct reflection
                    for (let k = 0; k < 4; k++) {
                        const pGeo = new THREE.SphereGeometry(1.6, 12, 12);
                        const pMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
                        const mesh = new THREE.Mesh(pGeo, pMat);
                        // Exactly aimed at (0, 0, 0)
                        mesh.position.set((Math.random() - 0.5) * 0.4, (Math.random() - 0.5) * 0.4, -75);
                        this.scene.add(mesh);
                        this.particles.push({ mesh, velocity: new THREE.Vector3(0, 0, 2.0), life: 0, isDirect: true });
                    }
                }
            });

            this.container.appendChild(uiDiv);
        }

        onResize() {
            if (!this.container || !this.renderer || !this.camera) return;
            const width = this.container.clientWidth;
            const height = 340;
            this.camera.aspect = width / height;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(width, height);
        }

        animate() {
            if (!this.isVisible) {
                this.animId = null;
                return;
            }
            this.animId = requestAnimationFrame(() => this.animate());

            if (!this.isPaused) {
                // Periodically spawn alpha particles
                if (Math.random() < 0.4) {
                    this.spawnAlphaParticle();
                }

                // Update particle positions & Coulomb electrostatic deflection
                for (let i = this.particles.length - 1; i >= 0; i--) {
                    const p = this.particles[i];
                    p.life++;

                    // Check interaction with gold nuclei
                    for (let n = 0; n < this.nuclei.length; n++) {
                        const nPos = this.nuclei[n];
                        const dist = p.mesh.position.distanceTo(nPos);

                        if (dist < 22) {
                            // Repulsive Coulomb force: F ~ 1 / r^2
                            const forceMag = Math.min(1.8, 12.0 / (dist * dist));
                            const dir = p.mesh.position.clone().sub(nPos).normalize();
                            p.velocity.add(dir.multiplyScalar(forceMag));
                        }
                    }

                    p.mesh.position.add(p.velocity);

                    // Fade or remove after traveling past detection screen
                    if (p.mesh.position.length() > 90 || p.life > 130) {
                        this.scene.remove(p.mesh);
                        p.mesh.geometry.dispose();
                        p.mesh.material.dispose();
                        this.particles.splice(i, 1);
                    }
                }
            }

            this.updateBackground();
            this.renderer.render(this.scene, this.camera);
        }
    }

    // =========================================================================
    // 2. BOHR ATOM & PHOTON TRANSITION 3D SIMULATOR
    // =========================================================================
    class BohrViewer {
        constructor(container) {
            this.container = container;
            this.scene = null;
            this.camera = null;
            this.renderer = null;
            this.animId = null;
            this.isVisible = false;

            this.orbits = [];
            this.electron = null;
            this.nucleus = null;
            this.currentN = 3;
            this.targetN = 3;
            this.currentRadius = 38;
            this.targetRadius = 38;
            this.orbitAngle = 0;
            this.photons = [];

            // Bohr orbit scaling radii (r_n = n^2 * a_0 scaled for 3D view)
            this.orbitRadii = { 1: 16, 2: 27, 3: 42, 4: 60, 5: 80 };

            // Spectral series info
            this.seriesData = {
                'lyman-21': { name: 'Lyman α (n=2 → 1)', n1: 1, n2: 2, wave: '121.6 nm (UV)', color: 0x8b5cf6 },
                'balmer-32': { name: 'Balmer H-α (n=3 → 2)', n1: 2, n2: 3, wave: '656.3 nm (Red)', color: 0xef4444 },
                'balmer-42': { name: 'Balmer H-β (n=4 → 2)', n1: 2, n2: 4, wave: '486.1 nm (Cyan)', color: 0x06b6d4 },
                'paschen-43': { name: 'Paschen α (n=4 → 3)', n1: 3, n2: 4, wave: '1875 nm (Infrared)', color: 0xf59e0b }
            };

            this.isDragging = false;
            this.prevMouse = { x: 0, y: 0 };

            this.init();
        }

        init() {
            const width = this.container.clientWidth || 600;
            const height = 360;

            this.scene = new THREE.Scene();
            this.updateBackground();

            this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
            this.camera.position.set(0, 75, 160);
            this.camera.lookAt(0, 0, 0);

            this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            this.renderer.setSize(width, height);
            this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            this.container.appendChild(this.renderer.domElement);

            // Lights
            this.scene.add(new THREE.AmbientLight(0xffffff, 0.8));
            const pt = new THREE.PointLight(0xffffff, 1.2, 200);
            pt.position.set(20, 40, 50);
            this.scene.add(pt);

            // Nucleus (Proton)
            const nucGeo = new THREE.SphereGeometry(6.5, 32, 32);
            const nucMat = new THREE.MeshStandardMaterial({
                color: 0xef4444,
                emissive: 0xb91c1c,
                emissiveIntensity: 0.5,
                roughness: 0.3
            });
            this.nucleus = new THREE.Mesh(nucGeo, nucMat);
            this.scene.add(this.nucleus);

            // Build concentric Bohr orbits
            this.buildOrbits();

            // Revolving electron
            const elGeo = new THREE.SphereGeometry(3.2, 20, 20);
            const elMat = new THREE.MeshStandardMaterial({
                color: 0x38bdf8,
                emissive: 0x0284c7,
                emissiveIntensity: 0.6
            });
            this.electron = new THREE.Mesh(elGeo, elMat);
            this.scene.add(this.electron);

            this.setupInteraction();
            this.setupObserver();
            this.createUI();

            window.addEventListener('resize', () => this.onResize());
        }

        updateBackground() {
            if (this.scene) {
                this.scene.background = new THREE.Color(isDarkMode() ? 0x0b1329 : 0xf8fafc);
            }
        }

        buildOrbits() {
            Object.entries(this.orbitRadii).forEach(([n, r]) => {
                const curve = new THREE.EllipseCurve(0, 0, r, r, 0, 2 * Math.PI, false, 0);
                const pts = curve.getPoints(64);
                const geo = new THREE.BufferGeometry().setFromPoints(pts);
                const mat = new THREE.LineBasicMaterial({
                    color: isDarkMode() ? 0x334155 : 0xcbd5e1,
                    transparent: true,
                    opacity: 0.85
                });
                const line = new THREE.Line(geo, mat);
                line.rotation.x = Math.PI / 2;
                this.scene.add(line);
                this.orbits.push(line);
            });
        }

        triggerTransition(transitionKey) {
            const trans = this.seriesData[transitionKey];
            if (!trans) return;

            // Start electron at higher orbit, transition down to lower orbit
            this.currentN = trans.n2;
            this.targetN = trans.n1;
            this.currentRadius = this.orbitRadii[trans.n2];
            this.targetRadius = this.orbitRadii[trans.n1];

            // Emit photon wave packet
            this.emitPhoton(trans.color, trans.name);

            // Update UI feedback banner
            const info = document.getElementById('bohr-spectral-info');
            if (info) {
                info.innerHTML = `<strong>${trans.name}:</strong> λ = ${trans.wave} • ΔE = E<sub>${trans.n2}</sub> − E<sub>${trans.n1}</sub> = hν`;
                info.style.borderColor = '#' + trans.color.toString(16);
            }
        }

        emitPhoton(hexColor, name) {
            // Animated wave packet moving radially outward
            const group = new THREE.Group();
            const waveGeo = new THREE.BufferGeometry();
            const pts = [];
            for (let i = 0; i <= 20; i++) {
                const t = i / 20;
                pts.push(new THREE.Vector3(t * 22, Math.sin(t * Math.PI * 5) * 3, 0));
            }
            waveGeo.setFromPoints(pts);
            const waveMat = new THREE.LineBasicMaterial({ color: hexColor, linewidth: 3 });
            const waveLine = new THREE.Line(waveGeo, waveMat);
            group.add(waveLine);

            group.position.copy(this.electron.position);
            group.rotation.y = this.orbitAngle + Math.PI / 2;
            this.scene.add(group);

            this.photons.push({ group, dir: group.position.clone().normalize(), life: 0 });
        }

        setupInteraction() {
            const dom = this.renderer.domElement;
            dom.style.cursor = 'grab';

            dom.addEventListener('mousedown', (e) => {
                this.isDragging = true;
                this.prevMouse = { x: e.clientX, y: e.clientY };
                dom.style.cursor = 'grabbing';
            });

            window.addEventListener('mouseup', () => {
                this.isDragging = false;
                if (dom) dom.style.cursor = 'grab';
            });

            dom.addEventListener('mousemove', (e) => {
                if (!this.isDragging) return;
                const dx = e.clientX - this.prevMouse.x;
                const dy = e.clientY - this.prevMouse.y;
                this.scene.rotation.y += dx * 0.006;
                this.scene.rotation.x += dy * 0.006;
                this.prevMouse = { x: e.clientX, y: e.clientY };
            });

            dom.addEventListener('touchstart', (e) => {
                if (e.touches.length === 1) {
                    this.isDragging = true;
                    this.prevMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY };
                }
            }, { passive: true });

            dom.addEventListener('touchmove', (e) => {
                if (!this.isDragging || e.touches.length !== 1) return;
                const dx = e.touches[0].clientX - this.prevMouse.x;
                const dy = e.touches[0].clientY - this.prevMouse.y;
                this.scene.rotation.y += dx * 0.009;
                this.scene.rotation.x += dy * 0.009;
                this.prevMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY };
            }, { passive: true });

            dom.addEventListener('touchend', () => { this.isDragging = false; });
        }

        setupObserver() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    this.isVisible = entry.isIntersecting;
                    if (this.isVisible && !this.animId) {
                        this.animate();
                    }
                });
            }, { threshold: 0.1 });
            observer.observe(this.container);
        }

        createUI() {
            const uiDiv = document.createElement('div');
            uiDiv.className = 'three-chem-controls';
            uiDiv.style.cssText = 'display:flex; flex-direction:column; gap:8px; align-items:center; margin-top:10px; font-size:12px;';

            uiDiv.innerHTML = `
                <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
                    <button class="chem-3d-btn active" data-series="balmer-32" style="border-color:#ef4444; color:#ef4444;">🔴 Balmer H-α (n=3 → 2)</button>
                    <button class="chem-3d-btn" data-series="balmer-42" style="border-color:#06b6d4; color:#06b6d4;">🔵 Balmer H-β (n=4 → 2)</button>
                    <button class="chem-3d-btn" data-series="lyman-21" style="border-color:#8b5cf6; color:#8b5cf6;">🟣 Lyman-α (n=2 → 1)</button>
                    <button class="chem-3d-btn" data-series="paschen-43" style="border-color:#f59e0b; color:#f59e0b;">🟠 Paschen-α (n=4 → 3)</button>
                </div>
                <div id="bohr-spectral-info" style="padding:4px 12px; border-radius:6px; border:1px solid #ef4444; background:var(--bg-surface); font-size:11px; text-align:center;">
                    <strong>Balmer H-α (n=3 → 2):</strong> λ = 656.3 nm (Red Visible Light) • ΔE = hν
                </div>
            `;

            uiDiv.addEventListener('click', (e) => {
                const btn = e.target.closest('button');
                if (!btn || !btn.dataset.series) return;
                uiDiv.querySelectorAll('button').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.triggerTransition(btn.dataset.series);
            });

            this.container.appendChild(uiDiv);
        }

        onResize() {
            if (!this.container || !this.renderer || !this.camera) return;
            const width = this.container.clientWidth;
            const height = 360;
            this.camera.aspect = width / height;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(width, height);
        }

        animate() {
            if (!this.isVisible) {
                this.animId = null;
                return;
            }
            this.animId = requestAnimationFrame(() => this.animate());

            // Smooth orbit transition
            this.currentRadius += (this.targetRadius - this.currentRadius) * 0.05;

            // Electron orbital velocity (Bohr v ~ 1/n)
            const speed = 0.045 / Math.sqrt(this.currentRadius / 15);
            this.orbitAngle += speed;

            // Position electron on orbit plane
            this.electron.position.x = Math.cos(this.orbitAngle) * this.currentRadius;
            this.electron.position.z = Math.sin(this.orbitAngle) * this.currentRadius;
            this.electron.position.y = 0;

            // Animate emitted photons
            for (let i = this.photons.length - 1; i >= 0; i--) {
                const p = this.photons[i];
                p.life++;
                p.group.position.add(p.dir.clone().multiplyScalar(1.6));
                p.group.scale.multiplyScalar(1.01);
                if (p.life > 60) {
                    this.scene.remove(p.group);
                    this.photons.splice(i, 1);
                }
            }

            this.updateBackground();
            this.renderer.render(this.scene, this.camera);
        }
    }

    // =========================================================================
    // 3. 3D ATOMIC ORBITALS & NODAL SURFACES EXPLORER
    // =========================================================================
    class OrbitalsViewer {
        constructor(container) {
            this.container = container;
            this.scene = null;
            this.camera = null;
            this.renderer = null;
            this.animId = null;
            this.isVisible = false;
            this.currentOrbital = '2px';
            this.currentMeshGroup = new THREE.Group();
            this.axesHelper = null;
            this.showNodalPlanes = false;

            this.isDragging = false;
            this.prevMouse = { x: 0, y: 0 };

            this.init();
        }

        init() {
            const width = this.container.clientWidth || 600;
            const height = 380;

            this.scene = new THREE.Scene();
            this.updateBackground();

            this.camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
            this.camera.position.set(45, 35, 70);
            this.camera.lookAt(0, 0, 0);

            this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            this.renderer.setSize(width, height);
            this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            this.container.appendChild(this.renderer.domElement);

            // Lights
            this.scene.add(new THREE.AmbientLight(0xffffff, 0.7));
            const d1 = new THREE.DirectionalLight(0xffffff, 0.8);
            d1.position.set(40, 60, 50);
            this.scene.add(d1);
            const d2 = new THREE.DirectionalLight(0xffffff, 0.4);
            d2.position.set(-40, -30, -50);
            this.scene.add(d2);

            // Cartesian 3D Axes (X=Red, Y=Green, Z=Blue)
            this.axesHelper = new THREE.AxesHelper(32);
            this.scene.add(this.axesHelper);

            // Add orbital group
            this.scene.add(this.currentMeshGroup);

            // Build initial orbital (2px)
            this.buildOrbitalMesh('2px');

            this.setupInteraction();
            this.setupObserver();
            this.createUI();

            window.addEventListener('resize', () => this.onResize());
        }

        updateBackground() {
            if (this.scene) {
                this.scene.background = new THREE.Color(isDarkMode() ? 0x0e1726 : 0xf8fafc);
            }
        }

        buildOrbitalMesh(type) {
            // Clear current mesh group
            while (this.currentMeshGroup.children.length > 0) {
                const obj = this.currentMeshGroup.children[0];
                this.currentMeshGroup.remove(obj);
                if (obj.geometry) obj.geometry.dispose();
                if (obj.material) {
                    if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose());
                    else obj.material.dispose();
                }
            }

            this.currentOrbital = type;

            // Phase Materials: Blue (+) and Amber/Orange (-)
            const posMat = new THREE.MeshStandardMaterial({
                color: 0x0284c7,
                roughness: 0.3,
                metalness: 0.1,
                transparent: true,
                opacity: 0.82
            });
            const negMat = new THREE.MeshStandardMaterial({
                color: 0xf59e0b,
                roughness: 0.3,
                metalness: 0.1,
                transparent: true,
                opacity: 0.82
            });

            // Helper to build a clean teardrop/dumbbell lobe
            const createLobe = (mat, scaleX = 1, scaleY = 1, scaleZ = 1) => {
                const geo = new THREE.SphereGeometry(10, 32, 32);
                // Distort into egg/dumbbell lobe along Z
                const pos = geo.attributes.position;
                for (let i = 0; i < pos.count; i++) {
                    const z = pos.getZ(i);
                    const stretch = 1.0 + (z / 10) * 0.45;
                    pos.setX(i, pos.getX(i) * stretch * scaleX);
                    pos.setY(i, pos.getY(i) * stretch * scaleY);
                    pos.setZ(i, (z + 4.5) * 1.35 * scaleZ);
                }
                geo.computeVertexNormals();
                return new THREE.Mesh(geo, mat);
            };

            if (type === '1s') {
                // Spherically symmetric 1s
                const geo = new THREE.SphereGeometry(18, 36, 36);
                const m = new THREE.Mesh(geo, posMat);
                this.currentMeshGroup.add(m);

            } else if (type === '2s') {
                // 2s: Inner sphere + node space + outer transparent sphere
                const outerGeo = new THREE.SphereGeometry(24, 36, 36);
                const outerMat = new THREE.MeshStandardMaterial({
                    color: 0x0284c7,
                    transparent: true,
                    opacity: 0.45,
                    roughness: 0.2
                });
                const outer = new THREE.Mesh(outerGeo, outerMat);

                const innerGeo = new THREE.SphereGeometry(11, 32, 32);
                const inner = new THREE.Mesh(innerGeo, posMat);

                // Radial node dashed wireframe ring
                const ringGeo = new THREE.RingGeometry(16.5, 17.5, 36);
                const ringMat = new THREE.MeshBasicMaterial({ color: 0xef4444, side: THREE.DoubleSide });
                const ring = new THREE.Mesh(ringGeo, ringMat);
                ring.rotation.x = Math.PI / 2;

                this.currentMeshGroup.add(outer);
                this.currentMeshGroup.add(inner);
                this.currentMeshGroup.add(ring);

            } else if (type === '2px') {
                // Dumbbell along X-axis
                const lobePos = createLobe(posMat);
                lobePos.rotation.y = Math.PI / 2;
                lobePos.position.x = 2;

                const lobeNeg = createLobe(negMat);
                lobeNeg.rotation.y = -Math.PI / 2;
                lobeNeg.position.x = -2;

                this.currentMeshGroup.add(lobePos);
                this.currentMeshGroup.add(lobeNeg);

            } else if (type === '2py') {
                // Dumbbell along Y-axis
                const lobePos = createLobe(posMat);
                lobePos.rotation.x = -Math.PI / 2;
                lobePos.position.y = 2;

                const lobeNeg = createLobe(negMat);
                lobeNeg.rotation.x = Math.PI / 2;
                lobeNeg.position.y = -2;

                this.currentMeshGroup.add(lobePos);
                this.currentMeshGroup.add(lobeNeg);

            } else if (type === '2pz') {
                // Dumbbell along Z-axis
                const lobePos = createLobe(posMat);
                lobePos.position.z = 2;

                const lobeNeg = createLobe(negMat);
                lobeNeg.rotation.x = Math.PI;
                lobeNeg.position.z = -2;

                this.currentMeshGroup.add(lobePos);
                this.currentMeshGroup.add(lobeNeg);

            } else if (type === '3dz2') {
                // 3dz^2: Dumbbell along Z with donut torus ring in XY plane
                const lobePos = createLobe(posMat, 0.9, 0.9, 1.2);
                lobePos.position.z = 1.5;

                const lobeNeg = createLobe(posMat, 0.9, 0.9, 1.2);
                lobeNeg.rotation.x = Math.PI;
                lobeNeg.position.z = -1.5;

                const donutGeo = new THREE.TorusGeometry(12, 4, 24, 48);
                const donut = new THREE.Mesh(donutGeo, negMat);

                this.currentMeshGroup.add(lobePos);
                this.currentMeshGroup.add(lobeNeg);
                this.currentMeshGroup.add(donut);

            } else if (type === '3dx2-y2') {
                // 3d(x^2 - y^2): 4 lobes lying directly along X and Y axes
                const l1 = createLobe(posMat, 0.75, 0.75, 0.9);
                l1.rotation.y = Math.PI / 2;
                l1.position.x = 2;

                const l2 = createLobe(posMat, 0.75, 0.75, 0.9);
                l2.rotation.y = -Math.PI / 2;
                l2.position.x = -2;

                const l3 = createLobe(negMat, 0.75, 0.75, 0.9);
                l3.rotation.x = -Math.PI / 2;
                l3.position.y = 2;

                const l4 = createLobe(negMat, 0.75, 0.75, 0.9);
                l4.rotation.x = Math.PI / 2;
                l4.position.y = -2;

                this.currentMeshGroup.add(l1);
                this.currentMeshGroup.add(l2);
                this.currentMeshGroup.add(l3);
                this.currentMeshGroup.add(l4);

            } else if (type === '3dxy') {
                // 3dxy: 4 lobes in XY plane between the axes (45 deg)
                const group45 = new THREE.Group();
                const l1 = createLobe(posMat, 0.75, 0.75, 0.9);
                l1.rotation.y = Math.PI / 2;
                l1.position.x = 2;

                const l2 = createLobe(posMat, 0.75, 0.75, 0.9);
                l2.rotation.y = -Math.PI / 2;
                l2.position.x = -2;

                const l3 = createLobe(negMat, 0.75, 0.75, 0.9);
                l3.rotation.x = -Math.PI / 2;
                l3.position.y = 2;

                const l4 = createLobe(negMat, 0.75, 0.75, 0.9);
                l4.rotation.x = Math.PI / 2;
                l4.position.y = -2;

                group45.add(l1); group45.add(l2); group45.add(l3); group45.add(l4);
                group45.rotation.z = Math.PI / 4;
                this.currentMeshGroup.add(group45);
            }
        }

        setupInteraction() {
            const dom = this.renderer.domElement;
            dom.style.cursor = 'grab';

            dom.addEventListener('mousedown', (e) => {
                this.isDragging = true;
                this.prevMouse = { x: e.clientX, y: e.clientY };
                dom.style.cursor = 'grabbing';
            });

            window.addEventListener('mouseup', () => {
                this.isDragging = false;
                if (dom) dom.style.cursor = 'grab';
            });

            dom.addEventListener('mousemove', (e) => {
                if (!this.isDragging) return;
                const dx = e.clientX - this.prevMouse.x;
                const dy = e.clientY - this.prevMouse.y;
                this.scene.rotation.y += dx * 0.007;
                this.scene.rotation.x += dy * 0.007;
                this.prevMouse = { x: e.clientX, y: e.clientY };
            });

            dom.addEventListener('touchstart', (e) => {
                if (e.touches.length === 1) {
                    this.isDragging = true;
                    this.prevMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY };
                }
            }, { passive: true });

            dom.addEventListener('touchmove', (e) => {
                if (!this.isDragging || e.touches.length !== 1) return;
                const dx = e.touches[0].clientX - this.prevMouse.x;
                const dy = e.touches[0].clientY - this.prevMouse.y;
                this.scene.rotation.y += dx * 0.01;
                this.scene.rotation.x += dy * 0.01;
                this.prevMouse = { x: e.touches[0].clientX, y: e.touches[0].clientY };
            }, { passive: true });

            dom.addEventListener('touchend', () => { this.isDragging = false; });
        }

        setupObserver() {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    this.isVisible = entry.isIntersecting;
                    if (this.isVisible && !this.animId) {
                        this.animate();
                    }
                });
            }, { threshold: 0.1 });
            observer.observe(this.container);
        }

        createUI() {
            const uiDiv = document.createElement('div');
            uiDiv.className = 'three-chem-controls';
            uiDiv.style.cssText = 'display:flex; flex-direction:column; gap:8px; align-items:center; margin-top:10px; font-size:12px;';

            uiDiv.innerHTML = `
                <div style="display:flex; flex-wrap:wrap; gap:6px; justify-content:center;">
                    <button class="chem-3d-btn" data-orb="1s">1s (Sphere)</button>
                    <button class="chem-3d-btn" data-orb="2s">2s (1 Radial Node)</button>
                    <button class="chem-3d-btn active" data-orb="2px">2pₓ (Dumbbell on X)</button>
                    <button class="chem-3d-btn" data-orb="2py">2p𝑦 (Dumbbell on Y)</button>
                    <button class="chem-3d-btn" data-orb="2pz">2p𝑧 (Dumbbell on Z)</button>
                    <button class="chem-3d-btn" data-orb="3dz2">3d𝑧² (Dumbbell + Donut)</button>
                    <button class="chem-3d-btn" data-orb="3dx2-y2">3d(𝑥²−𝑦²)</button>
                    <button class="chem-3d-btn" data-orb="3dxy">3d𝑥𝑦 (Cloverleaf)</button>
                </div>
                <div style="display:flex; align-items:center; gap:12px; font-size:11px; color:var(--chem-muted);">
                    <span><span style="color:#0284c7; font-weight:bold;">■</span> Positive Phase (+)</span>
                    <span><span style="color:#f59e0b; font-weight:bold;">■</span> Negative Phase (−)</span>
                    <span><span style="color:#ef4444; font-weight:bold;">━</span> X (Red) <span style="color:#10b981; font-weight:bold;">━</span> Y (Green) <span style="color:#3b82f6; font-weight:bold;">━</span> Z (Blue)</span>
                </div>
            `;

            uiDiv.addEventListener('click', (e) => {
                const btn = e.target.closest('button');
                if (!btn || !btn.dataset.orb) return;
                uiDiv.querySelectorAll('button').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.buildOrbitalMesh(btn.dataset.orb);
            });

            this.container.appendChild(uiDiv);
        }

        onResize() {
            if (!this.container || !this.renderer || !this.camera) return;
            const width = this.container.clientWidth;
            const height = 380;
            this.camera.aspect = width / height;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(width, height);
        }

        animate() {
            if (!this.isVisible) {
                this.animId = null;
                return;
            }
            this.animId = requestAnimationFrame(() => this.animate());

            // Gentle continuous rotation when not being dragged
            if (!this.isDragging) {
                this.currentMeshGroup.rotation.y += 0.005;
                this.axesHelper.rotation.y += 0.005;
            }

            this.updateBackground();
            this.renderer.render(this.scene, this.camera);
        }
    }

    // Auto-mount all 3D viewers when DOM is loaded
    function initThreeChemViewers() {
        // Rutherford
        const rutherfordContainer = document.getElementById('three-rutherford-container');
        if (rutherfordContainer) {
            new RutherfordViewer(rutherfordContainer);
        }

        // Bohr Atom
        const bohrContainer = document.getElementById('three-bohr-container');
        if (bohrContainer) {
            new BohrViewer(bohrContainer);
        }

        // Orbitals
        const orbitalsContainer = document.getElementById('three-orbitals-container');
        if (orbitalsContainer) {
            new OrbitalsViewer(orbitalsContainer);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initThreeChemViewers);
    } else {
        initThreeChemViewers();
    }

})();
