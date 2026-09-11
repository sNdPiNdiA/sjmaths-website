/*
=========================================================
SJMaths — Class 10 Science
Chapter 1: Chemical Reactions and Equations

DYNAMIC 3D CHEMICAL REACTION ENGINE (THREE.JS r160+)
- Full Step-by-Step Play / Pause / Loop Animations
- Native High-DPI DOM Typography Overlays
- 10 Complete CBSE Board Laboratory Simulations
=========================================================
*/

(() => {
    "use strict";

    if (!window.THREE) {
        console.error("SJMaths Three.js: THREE is not loaded.");
        return;
    }

    const THREE = window.THREE;

    /* ------------------------------------------------------------------
       COLOR PALETTE
    ------------------------------------------------------------------ */
    const C = {
        primary: 0x4f7fe8,
        darkPrimary: 0x2d5dc4,
        red: 0xdc2626,
        darkRed: 0x991b1b,
        amber: 0xd97706,
        green: 0x16a34a,
        blue: 0x2563eb,

        iron: 0x71717a,
        ironRust: 0xb45309,
        copper: 0xb45309,
        copperBright: 0xf59e0b,
        silver: 0xa1a1aa,

        oxygen: 0xef4444,
        hydrogen: 0x38bdf8,
        magnesium: 0xd4d4d8,
        oxide: 0xffffff,

        solutionBlue: 0x38bdf8,
        solutionGreen: 0x86efac,
        solutionClear: 0xe0f2fe,
        solutionWhite: 0xffffff,

        glass: 0xbae6fd,
        flameCore: 0xfef08a,
        flameOuter: 0xf97316
    };

    /* ------------------------------------------------------------------
       GEOMETRY HELPERS
    ------------------------------------------------------------------ */
    function makeMat(color, opts = {}) {
        return new THREE.MeshStandardMaterial({
            color,
            roughness: opts.roughness ?? 0.35,
            metalness: opts.metalness ?? 0.15,
            transparent: opts.transparent ?? false,
            opacity: opts.opacity ?? 1.0,
            side: opts.side ?? THREE.FrontSide
        });
    }

    function makeSphere(radius, color, opts = {}) {
        const mesh = new THREE.Mesh(new THREE.SphereGeometry(radius, 24, 18), makeMat(color, opts));
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        return mesh;
    }

    function makeBox(w, h, d, color, opts = {}) {
        const mesh = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), makeMat(color, opts));
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        return mesh;
    }

    function makeCylinder(rTop, rBot, h, color, opts = {}) {
        const mesh = new THREE.Mesh(new THREE.CylinderGeometry(rTop, rBot, h, 28), makeMat(color, opts));
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        return mesh;
    }

    /* ------------------------------------------------------------------
       SCENE CONFIGURATIONS & DESCRIPTIONS
    ------------------------------------------------------------------ */
    const SCENE_CONFIGS = {
        reaction: {
            title: "Burning of Magnesium Ribbon in Air",
            eq: "2Mg (s) + O₂ (g)  ──→  2MgO (s)",
            steps: [
                "Step 1: Clean magnesium ribbon held with tongs over burner.",
                "Step 2: Burner ignites — ribbon heats up in atmospheric oxygen.",
                "Step 3: Magnesium burns with an intense, dazzling white flame!",
                "Step 4: Reaction produces white Magnesium Oxide (MgO) powder."
            ]
        },
        balance: {
            title: "Balancing: Law of Conservation of Mass",
            eq: "3Fe + 4H₂O  ──→  Fe₃O₄ + 4H₂",
            steps: [
                "Step 1: Skeleton equation: Fe + H₂O → Fe₃O₄ + H₂.",
                "Step 2: Count atoms: Left (1 Fe, 2 H, 1 O) vs Right (3 Fe, 2 H, 4 O).",
                "Step 3: Add coefficients: 3 Fe on left + 4 H₂O to balance oxygen.",
                "Step 4: Add 4 before H₂ on right: Perfectly balanced (3 Fe, 8 H, 4 O)."
            ]
        },
        combination: {
            title: "Combination: 2+ Reactants → 1 Product",
            eq: "CaO (s) + H₂O (l)  ──→  Ca(OH)₂ (aq) + Heat",
            steps: [
                "Step 1: Solid Calcium Oxide (Quicklime, CaO) in reaction vessel.",
                "Step 2: Water (H₂O) is poured into the quicklime.",
                "Step 3: Vigorous exothermic reaction produces intense boiling heat & steam.",
                "Step 4: Single product formed: Slaked lime (Calcium Hydroxide, Ca(OH)₂)."
            ]
        },
        decomposition: {
            title: "Thermal Decomposition: 1 Compound → Simpler Substances",
            eq: "CaCO₃ (s)  ──Heat──→  CaO (s) + CO₂ (g) ↑",
            steps: [
                "Step 1: Calcium Carbonate (Limestone, CaCO₃) placed in test tube.",
                "Step 2: Strong heat applied from burner flame.",
                "Step 3: Bonds break as CO₂ gas bubbles rapidly rise out of tube.",
                "Step 4: Solid Calcium Oxide (CaO) residue remains at bottom."
            ]
        },
        displacement: {
            title: "Displacement: Fe Replaces Cu from Solution",
            eq: "Fe (s) + CuSO₄ (aq)  ──→  FeSO₄ (aq) + Cu (s)",
            steps: [
                "Step 1: Clean grey iron nail suspended above blue CuSO₄ solution.",
                "Step 2: Iron nail immersed into the copper sulphate solution.",
                "Step 3: Iron displaces Cu²⁺ ions — solution turns pale green (FeSO₄).",
                "Step 4: Reddish-brown copper layer deposits completely onto the iron nail."
            ]
        },
        double: {
            title: "Double Displacement & Precipitation",
            eq: "Na₂SO₄ (aq) + BaCl₂ (aq)  ──→  BaSO₄ (s) ↓ + 2NaCl (aq)",
            steps: [
                "Step 1: Colorless solutions of Na₂SO₄ and BaCl₂.",
                "Step 2: Both transparent solutions are mixed together.",
                "Step 3: Ions exchange partners (SO₄²⁻ binds Ba²⁺).",
                "Step 4: Insoluble white Barium Sulphate (BaSO₄ ↓) precipitate settles."
            ]
        },
        energy: {
            title: "Energy Classification: Exothermic vs Endothermic",
            eq: "Exothermic: Heat Released 🔥  |  Endothermic: Energy Absorbed ❄️",
            steps: [
                "Step 1: Baseline temperature in both reaction chambers.",
                "Step 2: Exothermic (Respiration/Slaking): Heat released, mercury rises!",
                "Step 3: Endothermic (Photosynthesis/Decomposition): Heat absorbed, mercury falls!",
                "Step 4: Exothermic radiates heat outward; Endothermic draws heat inward."
            ]
        },
        redox: {
            title: "Redox: Simultaneous Oxidation & Reduction",
            eq: "CuO + H₂  ──Heat──→  Cu + H₂O",
            steps: [
                "Step 1: Black Copper(II) Oxide (CuO) and Hydrogen (H₂) gas.",
                "Step 2: Heat applied — oxygen bond with copper weakens.",
                "Step 3: Oxygen atom migrates to H₂ to form water (H₂O).",
                "Step 4: CuO is Reduced to shiny brown Cu; H₂ is Oxidised to H₂O."
            ]
        },
        corrosion: {
            title: "Corrosion: Oxidation of Metals by Moisture & Air",
            eq: "4Fe + 3O₂ + 2xH₂O  ──→  2Fe₂O₃·xH₂O (Rust)",
            steps: [
                "Step 1: Left: Unprotected iron nail | Right: Painted protected nail.",
                "Step 2: Moisture and atmospheric oxygen attack the bare metal surface.",
                "Step 3: Left nail develops thick flaky reddish-brown rust layer.",
                "Step 4: Protected nail remains 100% clean and rust-free."
            ]
        },
        rancidity: {
            title: "Rancidity: Oxidation of Fats & Oils in Food",
            eq: "Fats/Oils + O₂  ──→  Foul Smell & Taste (Rancid)",
            steps: [
                "Step 1: Fried snacks exposed to air vs sealed packet.",
                "Step 2: Atmospheric oxygen attacks unsaturated fats in open food.",
                "Step 3: Open chips spoil and develop bad smell/rancid taste.",
                "Step 4: Nitrogen flushing in sealed pack prevents oxidation completely."
            ]
        }
    };

    /* ------------------------------------------------------------------
       SIMULATION ENGINE CLASS
    ------------------------------------------------------------------ */
    class SJScienceLab {
        constructor(container, type) {
            this.container = container;
            this.type = type;
            this.config = SCENE_CONFIGS[type] || SCENE_CONFIGS.reaction;
            this.step = 0;
            this.stepCount = this.config.steps.length;
            this.playing = false;
            this.time = 0;
            this.stepDuration = 3.0;
            this.isVisible = true;

            this.scene = new THREE.Scene();
            this.scene.background = new THREE.Color(0xf8fafc);

            this.camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
            this.camera.position.set(0, 0, 7.8);
            this.camera.lookAt(0, 0, 0);

            this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
            this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
            this.renderer.outputColorSpace = THREE.SRGBColorSpace;
            this.renderer.shadowMap.enabled = true;
            this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;

            container.innerHTML = "";
            container.appendChild(this.renderer.domElement);

            this.root = new THREE.Group();
            this.scene.add(this.root);

            this.buildDOMOverlays();
            this.addLighting();
            this.resize();

            // Resize Observer
            this.resizeObserver = new ResizeObserver(() => this.resize());
            this.resizeObserver.observe(container);

            // Intersection Observer to pause rendering when offscreen (60fps battery & GPU friendly)
            if ("IntersectionObserver" in window) {
                this.intersectionObserver = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        this.isVisible = entry.isIntersecting || entry.intersectionRatio > 0;
                    });
                }, { threshold: 0, rootMargin: "50px" });
                this.intersectionObserver.observe(container);
            }

            this.build3DScene();
            this.updateDOMOverlays();
            this.applyStep();
            this.animate();
        }

        buildDOMOverlays() {
            this.topOverlay = document.createElement("div");
            this.topOverlay.className = "sj-anim-top";
            this.topOverlay.innerHTML = `<div class="sj-anim-title">${this.config.title}</div>`;
            this.container.appendChild(this.topOverlay);

            this.bottomOverlay = document.createElement("div");
            this.bottomOverlay.className = "sj-anim-bottom-info";
            this.bottomOverlay.innerHTML = `
                <div class="sj-anim-eq">${this.config.eq}</div>
                <div class="sj-anim-desc">${this.config.steps[0]}</div>
            `;
            this.container.appendChild(this.bottomOverlay);

            this.controls = document.createElement("div");
            this.controls.className = "sj-three-controls";
            this.controls.innerHTML = `
                <button data-action="prev" title="Previous Step">‹</button>
                <button data-action="play" title="Auto Play">▶ Play</button>
                <button data-action="next" title="Next Step">›</button>
                <button data-action="replay" title="Restart">↺</button>
                <span class="sj-three-step">Step 1 / ${this.stepCount}</span>
            `;
            this.container.appendChild(this.controls);

            this.controls.addEventListener("click", (e) => {
                const btn = e.target.closest("button");
                if (!btn) return;
                const action = btn.dataset.action;
                if (action === "play") this.togglePlay();
                else if (action === "next") this.nextStep();
                else if (action === "prev") this.previousStep();
                else if (action === "replay") this.restart();
            });
        }

        updateDOMOverlays() {
            const descEl = this.bottomOverlay.querySelector(".sj-anim-desc");
            if (descEl && this.config.steps[this.step]) {
                descEl.textContent = this.config.steps[this.step];
            }

            const label = this.controls.querySelector(".sj-three-step");
            if (label) label.textContent = `Step ${this.step + 1} / ${this.stepCount}`;

            const playBtn = this.controls.querySelector('[data-action="play"]');
            if (playBtn) playBtn.textContent = this.playing ? "❚❚ Pause" : "▶ Play";
        }

        addLighting() {
            const ambient = new THREE.HemisphereLight(0xffffff, 0xe2e8f0, 2.5);
            this.scene.add(ambient);

            const dirLight = new THREE.DirectionalLight(0xffffff, 2.6);
            dirLight.position.set(4, 7, 5);
            dirLight.castShadow = true;
            this.scene.add(dirLight);

            const fill = new THREE.DirectionalLight(0xffffff, 1.2);
            fill.position.set(-4, 2, 4);
            this.scene.add(fill);
        }

        resize() {
            const width = Math.max(240, this.container.clientWidth);
            const height = Math.max(220, this.container.clientHeight);

            this.renderer.setSize(width, height, true);
            this.camera.aspect = width / height;
            this.camera.updateProjectionMatrix();
        }

        nextStep() {
            this.step = (this.step + 1) % this.stepCount;
            this.time = 0;
            this.updateDOMOverlays();
            this.applyStep();
        }

        previousStep() {
            this.step = (this.step - 1 + this.stepCount) % this.stepCount;
            this.time = 0;
            this.updateDOMOverlays();
            this.applyStep();
        }

        restart() {
            this.step = 0;
            this.time = 0;
            this.playing = false;
            this.updateDOMOverlays();
            this.applyStep();
        }

        togglePlay() {
            if (this.step >= this.stepCount - 1 && !this.playing) {
                this.step = 0;
                this.time = 0;
                this.applyStep();
            }
            this.playing = !this.playing;
            this.updateDOMOverlays();
        }

        createTestTube(x, y = 0) {
            const group = new THREE.Group();
            const glass = new THREE.Mesh(
                new THREE.CylinderGeometry(0.48, 0.48, 2.0, 28, 1, true),
                makeMat(C.glass, { transparent: true, opacity: 0.35, roughness: 0.1 })
            );
            group.add(glass);

            const bottom = makeSphere(0.48, C.glass, { transparent: true, opacity: 0.45 });
            bottom.position.y = -1.0;
            group.add(bottom);

            group.position.set(x, y, 0);
            this.root.add(group);
            return group;
        }

        addLiquid(tube, color, height = 0.9) {
            const liquid = makeCylinder(0.44, 0.44, height, color, { transparent: true, opacity: 0.7 });
            liquid.position.y = -1.0 + height / 2;
            tube.add(liquid);
            return liquid;
        }

        /* ------------------------------------------------------------------
           3D EXPERIMENT SCENES
        ------------------------------------------------------------------ */
        build3DScene() {
            const type = this.type;

            if (type === "reaction") {
                const burner = makeCylinder(0.35, 0.45, 0.8, 0x475569);
                burner.position.set(-1.4, -0.9, 0);
                this.root.add(burner);

                const flame = makeSphere(0.22, C.flameCore);
                flame.scale.set(0.8, 1.8, 0.8);
                flame.position.set(-1.4, -0.35, 0);
                flame.visible = false;
                this.root.add(flame);

                const ribbon = makeBox(1.5, 0.12, 0.08, C.magnesium);
                ribbon.position.set(-1.0, 0.15, 0);
                ribbon.rotation.z = -0.15;
                this.root.add(ribbon);

                const oxygenMols = [];
                for (let i = 0; i < 6; i++) {
                    const mol = new THREE.Group();
                    const a1 = makeSphere(0.12, C.oxygen);
                    const a2 = makeSphere(0.12, C.oxygen);
                    a1.position.x = -0.1;
                    a2.position.x = 0.1;
                    mol.add(a1);
                    mol.add(a2);
                    mol.position.set(1.0 + (i % 3) * 0.6, -0.3 + Math.floor(i / 3) * 0.6, 0);
                    this.root.add(mol);
                    oxygenMols.push({ mesh: mol, basePos: mol.position.clone() });
                }

                const mgoGroup = new THREE.Group();
                for (let i = 0; i < 24; i++) {
                    const p = makeSphere(0.06, 0xffffff);
                    p.position.set(-1.0 + (Math.random() - 0.5) * 0.7, -0.2 + (Math.random() - 0.5) * 0.3, (Math.random() - 0.5) * 0.3);
                    mgoGroup.add(p);
                }
                mgoGroup.visible = false;
                this.root.add(mgoGroup);

                this.animReaction = { flame, ribbon, mgoGroup, oxygenMols };
            }

            else if (type === "balance") {
                const feAtoms = [];
                for (let i = 0; i < 3; i++) {
                    const fe = makeSphere(0.22, C.iron);
                    fe.position.set(-1.6 + i * 0.5, 0.3, 0);
                    this.root.add(fe);
                    feAtoms.push(fe);
                }

                const h2oMols = [];
                for (let i = 0; i < 4; i++) {
                    const mol = new THREE.Group();
                    const o = makeSphere(0.18, C.oxygen);
                    const h1 = makeSphere(0.1, C.hydrogen);
                    const h2 = makeSphere(0.1, C.hydrogen);
                    h1.position.set(-0.15, -0.12, 0);
                    h2.position.set(0.15, -0.12, 0);
                    mol.add(o);
                    mol.add(h1);
                    mol.add(h2);
                    mol.position.set(-1.6 + (i % 2) * 0.6, -0.5 + Math.floor(i / 2) * 0.5, 0);
                    this.root.add(mol);
                    h2oMols.push(mol);
                }

                const products = new THREE.Group();
                for (let i = 0; i < 3; i++) {
                    const fe = makeSphere(0.2, C.iron);
                    fe.position.set(1.1 + (i % 2) * 0.4, 0.1 + Math.floor(i / 2) * 0.4, 0);
                    products.add(fe);
                }
                for (let i = 0; i < 4; i++) {
                    const o = makeSphere(0.16, C.oxygen);
                    o.position.set(1.5 + (i % 2) * 0.35, 0.0 + Math.floor(i / 2) * 0.35, 0.1);
                    products.add(o);
                }
                this.root.add(products);

                this.animBalance = { feAtoms, h2oMols, products };
            }

            else if (type === "combination") {
                const t1 = this.createTestTube(-1.6, 0);
                this.addLiquid(t1, 0xe2e8f0, 0.8);

                const t2 = this.createTestTube(0, 0);
                const l2 = this.addLiquid(t2, C.solutionBlue, 0.8);

                const t3 = this.createTestTube(1.6, 0);
                const l3 = this.addLiquid(t3, C.solutionClear, 1.1);

                // Steam particles
                const steam = new THREE.Group();
                for (let i = 0; i < 18; i++) {
                    const s = makeSphere(0.05, 0xffffff, { transparent: true, opacity: 0.6 });
                    s.position.set(1.6 + (Math.random() - 0.5) * 0.3, 0.2 + Math.random() * 0.8, (Math.random() - 0.5) * 0.3);
                    steam.add(s);
                }
                steam.visible = false;
                this.root.add(steam);

                this.animCombination = { t1, t2, t3, l2, l3, steam };
            }

            else if (type === "decomposition") {
                const tube = this.createTestTube(0, 0.1);
                const solid = this.addLiquid(tube, 0xf1f5f9, 0.7);

                const burner = makeCylinder(0.35, 0.45, 0.8, 0x475569);
                burner.position.set(0, -1.1, 0);
                this.root.add(burner);

                const flame = makeSphere(0.24, C.flameOuter);
                flame.scale.set(0.8, 1.6, 0.8);
                flame.position.set(0, -0.5, 0);
                flame.visible = false;
                this.root.add(flame);

                const gasGroup = new THREE.Group();
                for (let i = 0; i < 16; i++) {
                    const g = makeSphere(0.06, 0x94a3b8);
                    g.position.set((Math.random() - 0.5) * 0.35, 0.2 + Math.random() * 0.9, (Math.random() - 0.5) * 0.35);
                    gasGroup.add(g);
                }
                this.root.add(gasGroup);

                this.animDecomp = { flame, gasGroup, solid };
            }

            else if (type === "displacement") {
                const beaker = makeCylinder(0.8, 0.8, 1.8, C.glass, { transparent: true, opacity: 0.35 });
                beaker.position.set(0, -0.2, 0);
                this.root.add(beaker);

                const solution = makeCylinder(0.76, 0.76, 1.1, C.solutionBlue, { transparent: true, opacity: 0.7 });
                solution.position.set(0, -0.55, 0);
                this.root.add(solution);

                const nail = makeBox(0.18, 1.6, 0.12, C.iron);
                nail.position.set(0, 0.7, 0);
                nail.targetY = 0.7;
                this.root.add(nail);

                this.animDisp = { nail, solution };
            }

            else if (type === "double") {
                const t1 = this.createTestTube(-1.6, 0);
                this.addLiquid(t1, C.solutionClear, 0.8);

                const t2 = this.createTestTube(0, 0);
                this.addLiquid(t2, C.solutionClear, 0.8);

                const t3 = this.createTestTube(1.6, 0);
                this.addLiquid(t3, C.solutionClear, 1.0);

                const pGroup = new THREE.Group();
                for (let i = 0; i < 26; i++) {
                    const p = makeSphere(0.055, 0xffffff);
                    p.position.set(1.6 + (Math.random() - 0.5) * 0.6, -0.9 + Math.random() * 0.8, (Math.random() - 0.5) * 0.3);
                    pGroup.add(p);
                }
                this.root.add(pGroup);

                this.animDouble = { pGroup };
            }

            else if (type === "energy") {
                const exo = makeBox(1.6, 1.5, 0.4, 0xfee2e2, { transparent: true, opacity: 0.6 });
                exo.position.set(-1.4, -0.1, 0);
                this.root.add(exo);

                const endo = makeBox(1.6, 1.5, 0.4, 0xe0f2fe, { transparent: true, opacity: 0.6 });
                endo.position.set(1.4, -0.1, 0);
                this.root.add(endo);

                const t1 = makeCylinder(0.06, 0.06, 1.5, 0xffffff);
                t1.position.set(-1.4, 0.2, 0.25);
                this.root.add(t1);

                const m1 = makeCylinder(0.075, 0.075, 0.8, C.red);
                m1.position.set(-1.4, -0.15, 0.28);
                m1.targetScaleY = 0.8;
                this.root.add(m1);

                const t2 = makeCylinder(0.06, 0.06, 1.5, 0xffffff);
                t2.position.set(1.4, 0.2, 0.25);
                this.root.add(t2);

                const m2 = makeCylinder(0.075, 0.075, 0.35, C.blue);
                m2.position.set(1.4, -0.38, 0.28);
                m2.targetScaleY = 0.8;
                this.root.add(m2);

                this.animEnergy = { m1, m2 };
            }

            else if (type === "redox") {
                const cuAtom = makeSphere(0.32, C.copper);
                cuAtom.position.set(-1.5, 0, 0);
                this.root.add(cuAtom);

                const oAtom = makeSphere(0.24, C.oxygen);
                oAtom.position.set(-1.0, 0, 0);
                oAtom.targetX = -1.0;
                this.root.add(oAtom);

                const h1 = makeSphere(0.18, C.hydrogen);
                const h2 = makeSphere(0.18, C.hydrogen);
                h1.position.set(1.0, 0, 0);
                h2.position.set(1.3, 0, 0);
                this.root.add(h1);
                this.root.add(h2);

                this.animRedox = { oAtom, cuAtom, h1, h2 };
            }

            else if (type === "corrosion") {
                const nail1 = makeBox(0.22, 1.8, 0.22, C.iron);
                nail1.position.set(-1.4, 0, 0);
                this.root.add(nail1);

                const rustGroup = new THREE.Group();
                for (let i = 0; i < 28; i++) {
                    const r = makeSphere(0.06, C.ironRust);
                    r.position.set(-1.4 + (Math.random() - 0.5) * 0.32, -0.8 + Math.random() * 1.6, (Math.random() - 0.5) * 0.32);
                    rustGroup.add(r);
                }
                this.root.add(rustGroup);

                const nail2 = makeBox(0.22, 1.8, 0.22, C.primary);
                nail2.position.set(1.4, 0, 0);
                this.root.add(nail2);

                this.animCorrosion = { rustGroup, nail1, nail2 };
            }

            else if (type === "rancidity") {
                const openBag = makeBox(1.4, 1.6, 0.35, 0xfecaca, { transparent: true, opacity: 0.6 });
                openBag.position.set(-1.4, -0.1, 0);
                this.root.add(openBag);

                const closedBag = makeBox(1.4, 1.6, 0.35, 0xbbf7d0, { transparent: true, opacity: 0.6 });
                closedBag.position.set(1.4, -0.1, 0);
                this.root.add(closedBag);

                // Chips inside open bag
                const badChips = makeCylinder(0.3, 0.3, 0.1, 0xd97706);
                badChips.position.set(-1.4, -0.3, 0.1);
                this.root.add(badChips);

                // Chips inside closed bag
                const goodChips = makeCylinder(0.3, 0.3, 0.1, 0xfacc15);
                goodChips.position.set(1.4, -0.3, 0.1);
                this.root.add(goodChips);

                this.animRancid = { openBag, closedBag, badChips, goodChips };
            }
        }

        /* ------------------------------------------------------------------
           STEP UPDATES
        ------------------------------------------------------------------ */
        applyStep() {
            const s = this.step;

            if (this.type === "reaction" && this.animReaction) {
                this.animReaction.flame.visible = s >= 1;
                this.animReaction.mgoGroup.visible = s >= 3;
                this.animReaction.ribbon.material.color.setHex(s >= 2 ? 0xffffff : C.magnesium);
            }

            if (this.type === "balance" && this.animBalance) {
                this.animBalance.feAtoms.forEach((fe, i) => {
                    fe.visible = s >= 2 || i === 0;
                });
                this.animBalance.h2oMols.forEach((mol, i) => {
                    mol.visible = s >= 2 || i === 0;
                });
                this.animBalance.products.visible = s >= 3;
            }

            if (this.type === "combination" && this.animCombination) {
                this.animCombination.steam.visible = s >= 2;
                this.animCombination.l3.material.color.setHex(s >= 3 ? 0x86efac : C.solutionClear);
            }

            if (this.type === "decomposition" && this.animDecomp) {
                this.animDecomp.flame.visible = s >= 1;
                this.animDecomp.gasGroup.visible = s >= 2;
                this.animDecomp.solid.material.color.setHex(s >= 3 ? 0xfef08a : 0xf1f5f9);
            }

            if (this.type === "displacement" && this.animDisp) {
                this.animDisp.nail.targetY = s >= 1 ? -0.2 : 0.7;
                this.animDisp.nail.material.color.setHex(s >= 2 ? C.copper : C.iron);
                this.animDisp.solution.material.color.setHex(s >= 2 ? C.solutionGreen : C.solutionBlue);
            }

            if (this.type === "double" && this.animDouble) {
                this.animDouble.pGroup.visible = s >= 2;
            }

            if (this.type === "energy" && this.animEnergy) {
                this.animEnergy.m1.targetScaleY = s >= 1 ? 1.4 : 0.8;
                this.animEnergy.m2.targetScaleY = s >= 2 ? 0.4 : 0.8;
            }

            if (this.type === "redox" && this.animRedox) {
                this.animRedox.oAtom.targetX = s >= 2 ? 0.7 : -1.0;
                this.animRedox.cuAtom.material.color.setHex(s >= 2 ? C.copperBright : 0x1e293b);
            }

            if (this.type === "corrosion" && this.animCorrosion) {
                this.animCorrosion.rustGroup.visible = s >= 2;
                this.animCorrosion.nail1.material.color.setHex(s >= 2 ? C.ironRust : C.iron);
            }

            if (this.type === "rancidity" && this.animRancid) {
                this.animRancid.badChips.material.color.setHex(s >= 2 ? 0x78350f : 0xfacc15);
            }
        }

        /* ------------------------------------------------------------------
           ANIMATION LOOP
        ------------------------------------------------------------------ */
        animate() {
            if (this.destroyed) return;
            requestAnimationFrame(() => this.animate());

            // Skip rendering if scrolled outside viewport
            if (!this.isVisible) return;

            const delta = 1 / 60;
            if (this.playing) {
                this.time += delta;
                if (this.time > this.stepDuration) {
                    this.time = 0;
                    this.step = (this.step + 1) % this.stepCount;
                    this.updateDOMOverlays();
                    this.applyStep();
                }
            }

            const t = performance.now() * 0.003;

            // Live continuous particle, flame, and smooth lerp motions
            if (this.type === "reaction" && this.animReaction) {
                if (this.animReaction.flame.visible) {
                    this.animReaction.flame.scale.y = 1.6 + Math.sin(t * 8) * 0.3;
                    this.animReaction.flame.scale.x = 0.8 + Math.cos(t * 7) * 0.1;
                }
                if (this.step >= 2) {
                    this.animReaction.oxygenMols.forEach((item, idx) => {
                        item.mesh.position.x = item.basePos.x - Math.min(1.8, (t % 3) * 0.6);
                        item.mesh.rotation.y = t * 2 + idx;
                    });
                }
            }

            if (this.type === "combination" && this.animCombination) {
                if (this.animCombination.steam.visible) {
                    this.animCombination.steam.children.forEach((p) => {
                        p.position.y += 0.015;
                        if (p.position.y > 1.4) p.position.y = 0.2;
                    });
                }
            }

            if (this.type === "decomposition" && this.animDecomp) {
                if (this.animDecomp.flame.visible) {
                    this.animDecomp.flame.scale.y = 1.4 + Math.sin(t * 7) * 0.25;
                }
                if (this.animDecomp.gasGroup.visible) {
                    this.animDecomp.gasGroup.children.forEach((g) => {
                        g.position.y += 0.02;
                        if (g.position.y > 1.3) g.position.y = 0.2;
                    });
                }
            }

            if (this.type === "displacement" && this.animDisp) {
                if (typeof this.animDisp.nail.targetY === "number") {
                    this.animDisp.nail.position.y += (this.animDisp.nail.targetY - this.animDisp.nail.position.y) * 0.1;
                }
            }

            if (this.type === "double" && this.animDouble) {
                if (this.animDouble.pGroup.visible) {
                    this.animDouble.pGroup.rotation.y = t * 0.3;
                }
            }

            if (this.type === "energy" && this.animEnergy) {
                if (typeof this.animEnergy.m1.targetScaleY === "number") {
                    this.animEnergy.m1.scale.y += (this.animEnergy.m1.targetScaleY - this.animEnergy.m1.scale.y) * 0.1;
                }
                if (typeof this.animEnergy.m2.targetScaleY === "number") {
                    this.animEnergy.m2.scale.y += (this.animEnergy.m2.targetScaleY - this.animEnergy.m2.scale.y) * 0.1;
                }
            }

            if (this.type === "redox" && this.animRedox) {
                if (typeof this.animRedox.oAtom.targetX === "number") {
                    this.animRedox.oAtom.position.x += (this.animRedox.oAtom.targetX - this.animRedox.oAtom.position.x) * 0.1;
                }
            }

            this.renderer.render(this.scene, this.camera);
        }

        destroy() {
            this.destroyed = true;
            this.resizeObserver?.disconnect();
            this.intersectionObserver?.disconnect();
            this.renderer.dispose();
            this.container.innerHTML = "";
        }
    }

    /* ------------------------------------------------------------------
       INITIALIZATION BOOTSTRAPPER
    ------------------------------------------------------------------ */
    function initialize() {
        document.querySelectorAll("[data-three-animation]").forEach(container => {
            if (container.dataset.sjThreeInitialized === "1") return;
            container.dataset.sjThreeInitialized = "1";

            const type = (container.dataset.threeAnimation || "reaction").toLowerCase();
            const h = container.dataset.height ? `${parseInt(container.dataset.height, 10)}px` : "340px";
            container.style.height = h;

            try {
                container._sjScienceLab = new SJScienceLab(container, type);
            } catch (err) {
                console.error("SJMaths animation error:", err);
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initialize, { once: true });
    } else {
        initialize();
    }
})();