/*
==========================================================================
SJMaths — Class 10 Science Chapter 10
The Human Eye and the Colourful World

PIXEL-PERFECT 3D OPTICS SIMULATION ENGINE (THREE.JS)
- True 3D Eyeball, Biconvex Lens Morphing & Triangular Prisms
- Exact Ray Convergence on the Retina (Normal / Myopia / Hypermetropia)
- VIBGYOR Dispersion, Rainbow Drop & Atmospheric Refraction Scenes
- Smooth Drag-to-Rotate, Zoom, Touch Controls & Zero-Overlap Labels
==========================================================================
*/

(() => {
    "use strict";

    if (typeof THREE === "undefined") {
        console.error("SJMaths Three.js: THREE is not loaded.");
        return;
    }

    /* ------------------------------------------------------------------
       COLOR PALETTE
    ------------------------------------------------------------------ */
    const C = {
        bg: 0x090d16,
        axis: 0x475569,
        laserGold: 0xfacc15,
        laserCyan: 0x38bdf8,
        laserRose: 0xf43f5e,
        laserGreen: 0x22c55e,
        sclera: 0x93c5fd,
        irisBrown: 0x78350f,
        retinaPink: 0xfb7185,
        nerveCream: 0xfde68a,
        glass: 0x38bdf8,
        muscleViolet: 0xa78bfa,
        vibgyor: [0xdc2626, 0xf97316, 0xeab308, 0x22c55e, 0x2563eb, 0x4f46e5, 0x7c3aed]
    };

    /* ------------------------------------------------------------------
       CLEAN HIGH-DPI SPRITE LABELS
    ------------------------------------------------------------------ */
    function makeLabel(text, color = "#f8fafc", bgColor = "rgba(15,23,42,0.88)", borderColor = "#334155", scaleW = 2.2, scaleH = 0.5) {
        const canvas = document.createElement("canvas");
        canvas.width = 512;
        canvas.height = 128;
        const ctx = canvas.getContext("2d");

        ctx.fillStyle = bgColor;
        ctx.strokeStyle = borderColor;
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.roundRect(8, 8, 496, 112, 22);
        ctx.fill();
        ctx.stroke();

        ctx.font = "bold 42px 'Plus Jakarta Sans', system-ui, sans-serif";
        ctx.fillStyle = color;
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(text, 256, 64);

        const texture = new THREE.CanvasTexture(canvas);
        texture.colorSpace = THREE.SRGBColorSpace;
        texture.minFilter = THREE.LinearFilter;
        const material = new THREE.SpriteMaterial({ map: texture, transparent: true, depthTest: false });
        const sprite = new THREE.Sprite(material);
        sprite.scale.set(scaleW, scaleH, 1);
        return sprite;
    }
/* ------------------------------------------------------------------
       TUBE RAY WITH INTEGRATED ARROWS
    ------------------------------------------------------------------ */
    function createGlowRay(points, color = 0x38bdf8, radius = 0.032) {
        const curve = new THREE.CatmullRomCurve3(points);
        const geom = new THREE.TubeGeometry(curve, Math.max(16, points.length * 10), radius, 10, false);
        const mat = new THREE.MeshBasicMaterial({ color: color });
        const mesh = new THREE.Mesh(geom, mat);

        for (let i = 0; i < points.length - 1; i++) {
            const pA = points[i];
            const pB = points[i + 1];
            const mid = new THREE.Vector3().addVectors(pA, pB).multiplyScalar(0.5);
            const dir = new THREE.Vector3().subVectors(pB, pA).normalize();

            if (pA.distanceTo(pB) > 0.4) {
                const coneGeom = new THREE.ConeGeometry(radius * 2.5, radius * 4.5, 12);
                const coneMat = new THREE.MeshBasicMaterial({ color: color });
                const cone = new THREE.Mesh(coneGeom, coneMat);
                cone.position.copy(mid);
                cone.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir);
                mesh.add(cone);
            }
        }
        return mesh;
    }

    function createVirtualRay(points, color = 0x94a3b8) {
        const geom = new THREE.BufferGeometry().setFromPoints(points);
        const mat = new THREE.LineDashedMaterial({
            color: color,
            dashSize: 0.12,
            gapSize: 0.08,
            linewidth: 2
        });
        const line = new THREE.Line(geom, mat);
        line.computeLineDistances();
        return line;
    }

    /* ------------------------------------------------------------------
       EQUILATERAL TRIANGULAR GLASS PRISM (EXTRUDED, APEX UP)
    ------------------------------------------------------------------ */
    function createPrismMesh(size = 1.2, depth = 1.5, inverted = false) {
        const h = size * Math.sqrt(3) / 2;
        const shape = new THREE.Shape();
        shape.moveTo(-size / 2, -h / 2);
        shape.lineTo(size / 2, -h / 2);
        shape.lineTo(0, h);
        shape.closePath();
        const geom = new THREE.ExtrudeGeometry(shape, { depth: depth, bevelEnabled: false });
        geom.translate(0, 0, -depth / 2);
        const mat = new THREE.MeshPhysicalMaterial({
            color: C.glass,
            transparent: true,
            opacity: 0.4,
            transmission: 0.85,
            roughness: 0.06,
            ior: 1.5
        });
        const mesh = new THREE.Mesh(geom, mat);
        if (inverted) mesh.rotation.z = Math.PI;
        return mesh;
    }
/* ------------------------------------------------------------------
       SHARED EYE SCAFFOLD (eyeball + cornea + retina + optic nerve)
       Light travels from LEFT (-x) towards the retina on the RIGHT (+x)
    ------------------------------------------------------------------ */
    function createEyeScaffold(world, opts = {}) {
        const o = Object.assign({ opacity: 0.16, labels: true }, opts);

        // Sclera / eyeball
        const eyeball = new THREE.Mesh(
            new THREE.SphereGeometry(1.5, 40, 28),
            new THREE.MeshPhysicalMaterial({ color: C.sclera, transparent: true, opacity: o.opacity, roughness: 0.15 })
        );
        world.add(eyeball);

        // Retina lining (seen from inside)
        const retina = new THREE.Mesh(
            new THREE.SphereGeometry(1.42, 40, 28),
            new THREE.MeshBasicMaterial({ color: C.retinaPink, side: THREE.BackSide, transparent: true, opacity: 0.85 })
        );
        world.add(retina);

        // Cornea bulge at the front
        const cornea = new THREE.Mesh(
            new THREE.SphereGeometry(0.55, 32, 24),
            new THREE.MeshPhysicalMaterial({ color: 0xbae6fd, transparent: true, opacity: 0.5, roughness: 0.05 })
        );
        cornea.scale.set(0.75, 1, 1);
        cornea.position.set(-1.25, 0, 0);
        world.add(cornea);

        // Crystalline lens (biconvex)
        const lens = new THREE.Mesh(
            new THREE.SphereGeometry(0.6, 32, 24),
            new THREE.MeshPhysicalMaterial({ color: C.glass, transparent: true, opacity: 0.5, transmission: 0.85, roughness: 0.08 })
        );
        lens.scale.set(0.38, 1, 1);
        lens.position.set(-0.45, 0, 0);
        world.add(lens);

        // Optic nerve exiting at the back
        const nerve = new THREE.Mesh(
            new THREE.CylinderGeometry(0.14, 0.18, 1.0, 16),
            new THREE.MeshStandardMaterial({ color: C.nerveCream, roughness: 0.5 })
        );
        nerve.rotation.z = -Math.PI / 2;
        nerve.position.set(2.0, 0, 0);
        world.add(nerve);

        if (o.labels) {
            const corneaLabel = makeLabel("Cornea", "#bae6fd", "rgba(15,23,42,0.88)", "#0284c7", 1.15, 0.36);
            corneaLabel.position.set(-1.55, 1.25, 0);
            world.add(corneaLabel);

            const lensLabel = makeLabel("Eye lens", "#bae6fd", "rgba(15,23,42,0.88)", "#0284c7", 1.15, 0.36);
            lensLabel.position.set(-0.35, 1.25, 0);
            world.add(lensLabel);

            const retinaLabel = makeLabel("Retina", "#fda4af", "rgba(15,23,42,0.88)", "#be123c", 1.1, 0.36);
            retinaLabel.position.set(1.05, -1.35, 0);
            world.add(retinaLabel);
        }

        return { eyeball, retina, cornea, lens, nerve };
    }
/* ------------------------------------------------------------------
       MAIN EYE & LIGHT SIMULATION CLASS
    ------------------------------------------------------------------ */
    class EyeOpticsSimulation {
        constructor(container, sceneType) {
            this.container = container;
            this.type = sceneType;
            this.step = 0;
            this.maxSteps = 1;
            this.playing = true;
            this.time = 0;

            this.isDragging = false;
            this.prevMouse = { x: 0, y: 0 };
            this.targetRotation = { x: 0, y: 0 };
            this.currentRotation = { x: 0, y: 0 };
            this.zoom = 7.5;
            this.defaultZoom = 7.5;

            // Per-scene effect handles
            this.lensMorph = null;      // { mesh, targets:[thinX, thickX], ciliary }
            this.twinkleGhost = null;   // flickering apparent star

            this.initDOM();
            this.initThree();
            this.buildBaseScene();
            this.setupInteraction();
            this.rebuildDynamicElements();
            this.animate();
        }

        initDOM() {
            this.container.innerHTML = "";
            const hAttr = parseInt(this.container.getAttribute("data-height"), 10) || 300;

            Object.assign(this.container.style, {
                position: "relative",
                borderRadius: "16px",
                overflow: "hidden",
                background: "#090d16",
                border: "1.5px solid #1e293b",
                boxShadow: "0 10px 30px rgba(0,0,0,0.4)",
                margin: "16px 0",
                userSelect: "none",
                touchAction: "pan-y"
            });

            this.canvasWrapper = document.createElement("div");
            this.canvasWrapper.style.width = "100%";
            this.canvasWrapper.style.height = hAttr + "px";
            this.canvasWrapper.style.cursor = "grab";
            this.container.appendChild(this.canvasWrapper);

            // Control bar (title + case buttons)
            this.ctrlBar = document.createElement("div");
            Object.assign(this.ctrlBar.style, {
                position: "absolute", top: "10px", left: "10px", right: "10px",
                display: "flex", justifyContent: "space-between", alignItems: "center",
                gap: "8px", pointerEvents: "none"
            });

            this.titleTag = document.createElement("div");
            Object.assign(this.titleTag.style, {
                background: "rgba(9,13,22,0.82)", border: "1px solid #1e293b",
                padding: "6px 12px", borderRadius: "10px",
                fontSize: "11.5px", fontWeight: "750", color: "#38bdf8",
                display: "flex", alignItems: "center", gap: "6px",
                backdropFilter: "blur(6px)", flexWrap: "wrap"
            });
            this.ctrlBar.appendChild(this.titleTag);

            const btnGroup = document.createElement("div");
            btnGroup.style.display = "flex";
            btnGroup.style.alignItems = "center";
            btnGroup.style.gap = "5px";
            btnGroup.style.pointerEvents = "auto";

            this.prevBtn = document.createElement("button");
            this.prevBtn.innerHTML = "❮";
            this.prevBtn.title = "Previous Case";
            this.styleButton(this.prevBtn);
            this.prevBtn.onclick = () => this.prevStep();
            btnGroup.appendChild(this.prevBtn);

            this.playBtn = document.createElement("button");
            this.playBtn.innerHTML = "⏸";
            this.playBtn.title = "Play / Pause";
            this.styleButton(this.playBtn);
            this.playBtn.onclick = () => this.togglePlay();
            btnGroup.appendChild(this.playBtn);

            this.nextBtn = document.createElement("button");
            this.nextBtn.innerHTML = "Next Case ❯";
            this.nextBtn.title = "Next Case";
            this.styleButton(this.nextBtn, true);
            this.nextBtn.onclick = () => this.nextStep();
            btnGroup.appendChild(this.nextBtn);

            this.resetBtn = document.createElement("button");
            this.resetBtn.innerHTML = "⟲ View";
            this.resetBtn.title = "Reset 3D View";
            this.styleButton(this.resetBtn);
            this.resetBtn.onclick = () => this.resetCamera();
            btnGroup.appendChild(this.resetBtn);

            this.ctrlBar.appendChild(btnGroup);
            this.container.appendChild(this.ctrlBar);
        }

        styleButton(btn, isPrimary = false) {
            Object.assign(btn.style, {
                background: isPrimary ? "linear-gradient(135deg, #7c3aed, #5b21b6)" : "#1e293b",
                border: isPrimary ? "1px solid #8b5cf6" : "1px solid #334155",
                color: "#ffffff",
                padding: "5px 11px",
                borderRadius: "7px",
                fontSize: "11px",
                fontWeight: "750",
                cursor: "pointer",
                transition: "all 0.18s ease"
            });
            btn.onmouseenter = () => {
                btn.style.transform = "translateY(-1px)";
                btn.style.boxShadow = "0 3px 8px rgba(124,58,237,0.35)";
            };
            btn.onmouseleave = () => {
                btn.style.transform = "none";
                btn.style.boxShadow = "none";
            };
        }
initThree() {
            const w = this.canvasWrapper.clientWidth || 600;
            const h = this.canvasWrapper.clientHeight || 300;

            this.scene = new THREE.Scene();
            this.scene.background = new THREE.Color(C.bg);

            this.camera = new THREE.PerspectiveCamera(38, w / h, 0.1, 200);
            this.camera.position.set(0, 0.7, this.zoom);
            this.camera.lookAt(0, 0, 0);

            this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            this.renderer.setSize(w, h);
            this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
            this.renderer.outputColorSpace = THREE.SRGBColorSpace;
            this.canvasWrapper.appendChild(this.renderer.domElement);

            const ambient = new THREE.AmbientLight(0xffffff, 0.9);
            this.scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1.4);
            dirLight.position.set(6, 10, 8);
            this.scene.add(dirLight);

            this.world = new THREE.Group();
            this.scene.add(this.world);

            this.dynamicGroup = new THREE.Group();
            this.world.add(this.dynamicGroup);

            const ro = new ResizeObserver(() => {
                const nw = this.canvasWrapper.clientWidth;
                const nh = this.canvasWrapper.clientHeight;
                if (nw > 0 && nh > 0) {
                    this.camera.aspect = nw / nh;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(nw, nh);
                }
            });
            ro.observe(this.canvasWrapper);
        }

        setupInteraction() {
            const el = this.canvasWrapper;
            const onStart = (cx, cy) => {
                this.isDragging = true;
                this.prevMouse = { x: cx, y: cy };
                el.style.cursor = "grabbing";
            };
            const onMove = (cx, cy) => {
                if (!this.isDragging) return;
                const dx = cx - this.prevMouse.x;
                const dy = cy - this.prevMouse.y;
                this.targetRotation.y += dx * 0.007;
                this.targetRotation.x = Math.max(-0.6, Math.min(0.6, this.targetRotation.x + dy * 0.007));
                this.prevMouse = { x: cx, y: cy };
            };
            const onEnd = () => {
                this.isDragging = false;
                el.style.cursor = "grab";
            };

            el.addEventListener("mousedown", e => onStart(e.clientX, e.clientY));
            window.addEventListener("mousemove", e => onMove(e.clientX, e.clientY));
            window.addEventListener("mouseup", onEnd);

            el.addEventListener("touchstart", e => {
                if (e.touches.length === 1) onStart(e.touches[0].clientX, e.touches[0].clientY);
            }, { passive: true });
            window.addEventListener("touchmove", e => {
                if (e.touches.length === 1 && this.isDragging) onMove(e.touches[0].clientX, e.touches[0].clientY);
            }, { passive: true });
            window.addEventListener("touchend", onEnd);

            el.addEventListener("wheel", e => {
                e.preventDefault();
                this.zoom = Math.max(4.5, Math.min(14.0, this.zoom + e.deltaY * 0.005));
                this.camera.position.z = this.zoom;
            }, { passive: false });
        }

        resetCamera() {
            this.targetRotation.x = 0;
            this.targetRotation.y = 0;
            this.zoom = this.defaultZoom;
            this.camera.position.set(0, 0.7, this.zoom);
        }

        togglePlay() {
            this.playing = !this.playing;
            this.playBtn.innerHTML = this.playing ? "⏸" : "▶";
        }

        nextStep() {
            this.step = (this.step + 1) % this.maxSteps;
            this.rebuildDynamicElements();
        }

        prevStep() {
            this.step = (this.step - 1 + this.maxSteps) % this.maxSteps;
            this.rebuildDynamicElements();
        }
/* --------------------------------------------------------------
           BASE SCENE GEOMETRIES
        -------------------------------------------------------------- */
        buildBaseScene() {
            switch (this.type) {
                case "eye-anatomy":
                    this.buildEyeAnatomyBase();
                    break;
                case "accommodation":
                    this.buildAccommodationBase();
                    break;
                case "defects-correction":
                    this.buildDefectsBase();
                    break;
                case "prism-dispersion":
                    this.buildPrismBase();
                    break;
                case "rainbow-drop":
                    this.buildRainbowBase();
                    break;
                case "twinkling-star":
                    this.buildTwinklingBase();
                    break;
            }
        }

        /* 1. EYE ANATOMY */
        buildEyeAnatomyBase() {
            this.maxSteps = 2;
            this.defaultZoom = 7.2;
            this.zoom = 7.2;

            createEyeScaffold(this.world, { labels: false });

            // Iris ring + pupil in front of the lens
            const iris = new THREE.Mesh(
                new THREE.TorusGeometry(0.42, 0.07, 14, 40),
                new THREE.MeshStandardMaterial({ color: C.irisBrown, roughness: 0.55 })
            );
            iris.rotation.y = Math.PI / 2;
            iris.position.set(-1.02, 0, 0);
            this.world.add(iris);

            const pupil = new THREE.Mesh(
                new THREE.CircleGeometry(0.18, 24),
                new THREE.MeshBasicMaterial({ color: 0x020617 })
            );
            pupil.rotation.y = -Math.PI / 2;
            pupil.position.set(-1.03, 0, 0);
            this.world.add(pupil);

            const irisLabel = makeLabel("Pupil & Iris", "#fde68a", "rgba(15,23,42,0.88)", "#b45309", 1.5, 0.4);
            irisLabel.position.set(-1.05, -1.3, 0);
            this.world.add(irisLabel);

            const nerveLabel = makeLabel("Optic nerve", "#fde68a", "rgba(15,23,42,0.88)", "#ca8a04", 1.5, 0.4);
            nerveLabel.position.set(2.15, 1.05, 0);
            this.world.add(nerveLabel);

            // Part labels for the anatomy tour (case 0 only)
            this.anatomyLabels = new THREE.Group();
            const t1 = makeLabel("Cornea — refracts most light", "#bae6fd", "rgba(15,23,42,0.9)", "#0284c7", 3.0, 0.46);
            t1.position.set(-0.6, 2.05, 0);
            this.anatomyLabels.add(t1);
            const t2 = makeLabel("Lens — fine focusing", "#bae6fd", "rgba(15,23,42,0.9)", "#0284c7", 2.5, 0.44);
            t2.position.set(1.9, 1.45, 0);
            this.anatomyLabels.add(t2);
            const t3 = makeLabel("Retina — screen for the image", "#fda4af", "rgba(15,23,42,0.9)", "#be123c", 3.0, 0.46);
            t3.position.set(2.6, -1.35, 0);
            this.anatomyLabels.add(t3);
            this.world.add(this.anatomyLabels);
        }

        /* 2. ACCOMMODATION */
        buildAccommodationBase() {
            this.maxSteps = 2;
            this.defaultZoom = 7.4;
            this.zoom = 7.4;

            const parts = createEyeScaffold(this.world, { labels: true });
            parts.lens.visible = false; // replaced by the morphing lens

            // Ciliary muscle ring around the lens
            const ciliary = new THREE.Mesh(
                new THREE.TorusGeometry(0.78, 0.09, 12, 40),
                new THREE.MeshStandardMaterial({ color: C.muscleViolet, roughness: 0.5 })
            );
            ciliary.rotation.y = Math.PI / 2;
            ciliary.position.set(-0.45, 0, 0);
            this.world.add(ciliary);

            const ciliaryLabel = makeLabel("Ciliary muscles", "#c4b5fd", "rgba(15,23,42,0.88)", "#7c3aed", 1.9, 0.42);
            ciliaryLabel.position.set(-0.45, -1.75, 0);
            this.world.add(ciliaryLabel);

            // Morphing lens (scale.x animated between thin and thick)
            const morphLens = new THREE.Mesh(
                new THREE.SphereGeometry(0.62, 32, 24),
                new THREE.MeshPhysicalMaterial({ color: C.glass, transparent: true, opacity: 0.55, transmission: 0.85, roughness: 0.08 })
            );
            morphLens.position.set(-0.45, 0, 0);
            morphLens.scale.set(0.30, 1.02, 1.02);
            this.world.add(morphLens);

            this.lensMorph = { mesh: morphLens, ciliary: ciliary };
        }
/* 3. DEFECTS OF VISION */
        buildDefectsBase() {
            this.maxSteps = 3;
            this.defaultZoom = 8.0;
            this.zoom = 8.0;

            createEyeScaffold(this.world, { labels: false });

            const retinaLabel = makeLabel("Retina", "#fda4af", "rgba(15,23,42,0.88)", "#be123c", 1.1, 0.36);
            retinaLabel.position.set(1.05, -1.45, 0);
            this.world.add(retinaLabel);

            const eyeLensLabel = makeLabel("Eye lens", "#bae6fd", "rgba(15,23,42,0.88)", "#0284c7", 1.2, 0.36);
            eyeLensLabel.position.set(-0.45, 1.35, 0);
            this.world.add(eyeLensLabel);
        }

        /* 4. PRISM DISPERSION */
        buildPrismBase() {
            this.maxSteps = 3;
            this.defaultZoom = 9.2;
            this.zoom = 9.2;
        }

        /* 5. RAINBOW DROP */
        buildRainbowBase() {
            this.maxSteps = 2;
            this.defaultZoom = 9.4;
            this.zoom = 9.4;
        }

        /* 6. TWINKLING STAR */
        buildTwinklingBase() {
            this.maxSteps = 2;
            this.defaultZoom = 11.0;
            this.zoom = 11.0;

            // Earth (curved ground) with the observer on top
            const earth = new THREE.Mesh(
                new THREE.SphereGeometry(7, 48, 32),
                new THREE.MeshStandardMaterial({ color: 0x166534, roughness: 0.85 })
            );
            earth.position.set(0, -7.9, 0);
            this.world.add(earth);

            // Atmosphere shells of gradually increasing refractive index
            [8.1, 9.1, 10.1].forEach((r, i) => {
                const shell = new THREE.Mesh(
                    new THREE.SphereGeometry(r, 40, 24),
                    new THREE.MeshBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.07 - i * 0.02 })
                );
                shell.position.copy(earth.position);
                this.world.add(shell);
            });

            // Observer
            const observer = new THREE.Mesh(
                new THREE.SphereGeometry(0.16, 16, 12),
                new THREE.MeshBasicMaterial({ color: 0xfacc15 })
            );
            observer.position.set(0, -0.72, 0);
            this.world.add(observer);

            const observerLabel = makeLabel("Observer", "#facc15", "rgba(15,23,42,0.88)", "#ca8a04", 1.3, 0.38);
            observerLabel.position.set(1.35, -0.95, 0);
            this.world.add(observerLabel);

            const atmosphereLabel = makeLabel("Atmosphere (n decreases upward)", "#7dd3fc", "rgba(15,23,42,0.88)", "#0284c7", 3.4, 0.46);
            atmosphereLabel.position.set(-3.4, 2.6, 0);
            this.world.add(atmosphereLabel);
        }
/* --------------------------------------------------------------
           DYNAMIC CASE BUILDERS
        -------------------------------------------------------------- */
        rebuildDynamicElements() {
            while (this.dynamicGroup.children.length > 0) {
                const child = this.dynamicGroup.children.pop();
                if (child.geometry) child.geometry.dispose();
            }
            this.twinkleGhost = null;

            // 1. EYE ANATOMY
            if (this.type === "eye-anatomy") {
                if (this.step === 0) {
                    this.titleTag.innerHTML = `<span>👁 Anatomy Tour:</span> <span style="color:#fde68a;">drag to rotate the eyeball</span>`;
                    if (this.anatomyLabels) this.anatomyLabels.visible = true;
                } else {
                    this.titleTag.innerHTML = `<span>👁 Image Formation:</span> <span style="color:#facc15;">real, INVERTED image on the retina</span>`;
                    if (this.anatomyLabels) this.anatomyLabels.visible = false;

                    // Object (upright arrow)
                    const objShaft = new THREE.Mesh(
                        new THREE.CylinderGeometry(0.03, 0.03, 0.7, 8),
                        new THREE.MeshBasicMaterial({ color: C.laserGreen })
                    );
                    objShaft.position.set(-3.6, 0.35, 0);
                    this.dynamicGroup.add(objShaft);
                    const objHead = new THREE.Mesh(
                        new THREE.ConeGeometry(0.08, 0.2, 10),
                        new THREE.MeshBasicMaterial({ color: C.laserGreen })
                    );
                    objHead.position.set(-3.6, 0.8, 0);
                    this.dynamicGroup.add(objHead);

                    [-0.55, 0, 0.55].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-3.6, y + 0.55, 0),
                            new THREE.Vector3(-0.45, y * 0.9, 0),
                            new THREE.Vector3(1.02, 0, 0)
                        ], C.laserGold, 0.026));
                    });

                    // Inverted image arrow on the retina
                    const imgShaft = new THREE.Mesh(
                        new THREE.CylinderGeometry(0.035, 0.035, 0.5, 8),
                        new THREE.MeshBasicMaterial({ color: C.laserRose })
                    );
                    imgShaft.position.set(1.28, -0.32, 0);
                    this.dynamicGroup.add(imgShaft);
                    const imgHead = new THREE.Mesh(
                        new THREE.ConeGeometry(0.09, 0.22, 10),
                        new THREE.MeshBasicMaterial({ color: C.laserRose })
                    );
                    imgHead.position.set(1.28, -0.64, 0);
                    imgHead.rotation.z = Math.PI;
                    this.dynamicGroup.add(imgHead);

                    const imgLabel = makeLabel("Real, inverted image", "#fda4af", "rgba(15,23,42,0.9)", "#be123c", 2.3, 0.42);
                    imgLabel.position.set(2.6, -0.75, 0);
                    this.dynamicGroup.add(imgLabel);
                }
            }

            // 2. ACCOMMODATION
            else if (this.type === "accommodation") {
                const isNear = this.step === 1;
                this.titleTag.innerHTML = isNear
                    ? `<span>Near object:</span> <span style="color:#c4b5fd;">muscles CONTRACT → lens THICK → short f</span>`
                    : `<span>Distant object:</span> <span style="color:#facc15;">muscles RELAXED → lens THIN → long f</span>`;

                if (this.lensMorph) {
                    this.lensMorph.target = isNear ? 0.54 : 0.30;
                }

                if (!isNear) {
                    [-0.55, 0, 0.55].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-4.6, y, 0),
                            new THREE.Vector3(-0.45, y * 0.92, 0),
                            new THREE.Vector3(1.18, 0, 0)
                        ], C.laserGold, 0.026));
                    });
                    const dLabel = makeLabel("Parallel rays from a distant object", "#facc15", "rgba(15,23,42,0.9)", "#ca8a04", 3.2, 0.44);
                    dLabel.position.set(-1.6, 1.6, 0);
                    this.dynamicGroup.add(dLabel);
                } else {
                    // Object tip at (-3.4, 1.05); diverging rays hit lens and focus on retina
                    [[-0.45, 0], [-0.45, 0.5], [-0.45, -0.5]].forEach(p => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-3.4, 1.05, 0),
                            new THREE.Vector3(p[0], p[1] * 0.85 + 0.12, 0),
                            new THREE.Vector3(1.18, 0, 0)
                        ], C.laserGold, 0.026));
                    });
                    const objDot = new THREE.Mesh(
                        new THREE.SphereGeometry(0.09, 14, 10),
                        new THREE.MeshBasicMaterial({ color: C.laserGreen })
                    );
                    objDot.position.set(-3.4, 1.05, 0);
                    this.dynamicGroup.add(objDot);
                    const nLabel = makeLabel("Diverging rays from a NEARBY object", "#c4b5fd", "rgba(15,23,42,0.9)", "#7c3aed", 3.4, 0.46);
                    nLabel.position.set(-1.4, 1.85, 0);
                    this.dynamicGroup.add(nLabel);
                }
            }
// 3. DEFECTS & CORRECTION
            else if (this.type === "defects-correction") {
                const FOCUS_ON = 1.25;   // on the retina
                const FOCUS_FRONT = 0.5; // myopia
                const FOCUS_BACK = 1.85; // hypermetropia

                if (this.step === 0) {
                    this.titleTag.innerHTML = `<span>Normal eye:</span> <span style="color:#22c55e;">parallel rays focus exactly ON the retina ✓</span>`;
                    [-0.55, 0, 0.55].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-4.6, y, 0),
                            new THREE.Vector3(-0.45, y * 0.92, 0),
                            new THREE.Vector3(FOCUS_ON, 0, 0)
                        ], C.laserGreen, 0.026));
                    });
                    const okLabel = makeLabel("Sharp image ON the retina", "#86efac", "rgba(15,23,42,0.9)", "#16a34a", 2.9, 0.44);
                    okLabel.position.set(2.4, 1.35, 0);
                    this.dynamicGroup.add(okLabel);
                }

                else if (this.step === 1) {
                    this.titleTag.innerHTML = `<span>Myopia:</span> <span style="color:#f43f5e;">focus in FRONT of retina</span> <span style="color:#38bdf8;">→ concave lens corrects</span>`;

                    // Defective focus (gold)
                    [-0.5, 0.5].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-4.6, y, 0),
                            new THREE.Vector3(-0.45, y * 0.9, 0),
                            new THREE.Vector3(FOCUS_FRONT, 0, 0),
                            new THREE.Vector3(1.05, -y * 0.35, 0)
                        ], C.laserGold, 0.024));
                    });
                    const badDot = new THREE.Mesh(
                        new THREE.SphereGeometry(0.09, 14, 10),
                        new THREE.MeshBasicMaterial({ color: C.laserRose })
                    );
                    badDot.position.set(FOCUS_FRONT, 0, 0);
                    this.dynamicGroup.add(badDot);
                    const badLabel = makeLabel("Focus in front of retina ✗", "#fda4af", "rgba(15,23,42,0.9)", "#be123c", 2.9, 0.44);
                    badLabel.position.set(0.35, 1.5, 0);
                    this.dynamicGroup.add(badLabel);

                    // Corrective concave lens
                    const concave = new THREE.Mesh(
                        new THREE.CylinderGeometry(0.78, 0.78, 0.14, 36),
                        new THREE.MeshPhysicalMaterial({ color: 0xc4b5fd, transparent: true, opacity: 0.5, roughness: 0.1 })
                    );
                    concave.rotation.z = Math.PI / 2;
                    concave.position.set(-2.75, 0, 0);
                    this.dynamicGroup.add(concave);
                    const ccLabel = makeLabel("Concave lens", "#c4b5fd", "rgba(15,23,42,0.9)", "#7c3aed", 1.7, 0.4);
                    ccLabel.position.set(-2.75, -1.25, 0);
                    this.dynamicGroup.add(ccLabel);

                    // Corrected rays (cyan)
                    [-0.55, 0.55].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-4.9, y, 0),
                            new THREE.Vector3(-2.75, y * 1.16, 0),
                            new THREE.Vector3(-0.45, y * 0.9, 0),
                            new THREE.Vector3(FOCUS_ON, 0, 0)
                        ], C.laserCyan, 0.024));
                    });
                }
else {
                    this.titleTag.innerHTML = `<span>Hypermetropia:</span> <span style="color:#f43f5e;">focus BEHIND retina</span> <span style="color:#facc15;">→ convex lens corrects</span>`;

                    // Defective focus (gold)
                    [-0.5, 0.5].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-4.6, y, 0),
                            new THREE.Vector3(-0.45, y * 0.9, 0),
                            new THREE.Vector3(FOCUS_BACK, 0, 0)
                        ], C.laserGold, 0.024));
                    });
                    const badDot = new THREE.Mesh(
                        new THREE.SphereGeometry(0.09, 14, 10),
                        new THREE.MeshBasicMaterial({ color: C.laserRose })
                    );
                    badDot.position.set(FOCUS_BACK, 0, 0);
                    this.dynamicGroup.add(badDot);
                    const badLabel = makeLabel("Focus behind retina ✗", "#fda4af", "rgba(15,23,42,0.9)", "#be123c", 2.7, 0.44);
                    badLabel.position.set(1.9, 1.55, 0);
                    this.dynamicGroup.add(badLabel);

                    // Corrective convex lens
                    const convex = new THREE.Mesh(
                        new THREE.SphereGeometry(0.8, 32, 24),
                        new THREE.MeshPhysicalMaterial({ color: 0xfde68a, transparent: true, opacity: 0.5, roughness: 0.1 })
                    );
                    convex.scale.set(0.24, 1, 1);
                    convex.position.set(-2.75, 0, 0);
                    this.dynamicGroup.add(convex);
                    const cvLabel = makeLabel("Convex lens", "#fde68a", "rgba(15,23,42,0.9)", "#ca8a04", 1.7, 0.4);
                    cvLabel.position.set(-2.75, -1.25, 0);
                    this.dynamicGroup.add(cvLabel);

                    // Corrected rays (cyan): pre-converged by the convex lens
                    [-0.55, 0.55].forEach(y => {
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-4.9, y, 0),
                            new THREE.Vector3(-2.75, y * 0.62, 0),
                            new THREE.Vector3(-0.45, y * 0.52, 0),
                            new THREE.Vector3(FOCUS_ON, 0, 0)
                        ], C.laserCyan, 0.024));
                    });
                }
            }
// 4. PRISM DISPERSION
            else if (this.type === "prism-dispersion") {
                const EXIT = new THREE.Vector3(0.62, -0.78, 0); // fan origin on prism right face

                if (this.step === 0 || this.step === 1) {
                    const fullSpectrum = this.step === 0;
                    this.titleTag.innerHTML = fullSpectrum
                        ? `<span>Dispersion:</span> <span style="color:#f8fafc;">white light → VIBGYOR spectrum</span>`
                        : `<span>Deviation:</span> <span style="color:#f87171;">red least</span> <span style="color:#93c5fd;">• violet most</span>`;

                    this.dynamicGroup.add(createPrismMesh(1.5, 1.4));
                    this.dynamicGroup.children[this.dynamicGroup.children.length - 1].position.set(0, -0.42, 0);

                    // Incident white beam + refracted segment inside the prism
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-4.6, 1.2, 0), new THREE.Vector3(-0.72, 0.5, 0)], 0xf8fafc, 0.04));
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-0.72, 0.5, 0), EXIT], 0xe2e8f0, 0.03));

                    // Emergent VIBGYOR fan (red top = least deviation)
                    C.vibgyor.forEach((col, k) => {
                        if (!fullSpectrum && k !== 0 && k !== 6) return;
                        const yEnd = 0.95 - k * 0.44;
                        const midY = (-0.78 + yEnd) / 2 - 0.08;
                        this.dynamicGroup.add(createGlowRay([
                            EXIT,
                            new THREE.Vector3(2.6, midY, 0),
                            new THREE.Vector3(4.7, yEnd, 0)
                        ], col, fullSpectrum ? 0.03 : 0.045));
                    });

                    const wlLabel = makeLabel("White light", "#f8fafc", "rgba(15,23,42,0.9)", "#94a3b8", 1.6, 0.4);
                    wlLabel.position.set(-3.9, 1.65, 0);
                    this.dynamicGroup.add(wlLabel);

                    const redLabel = makeLabel("Red — bends least", "#fca5a5", "rgba(15,23,42,0.9)", "#dc2626", 2.2, 0.42);
                    redLabel.position.set(3.6, 1.35, 0);
                    this.dynamicGroup.add(redLabel);

                    const violetLabel = makeLabel("Violet — bends most", "#c4b5fd", "rgba(15,23,42,0.9)", "#7c3aed", 2.4, 0.42);
                    violetLabel.position.set(3.7, -2.15, 0);
                    this.dynamicGroup.add(violetLabel);
                }

                else {
                    this.titleTag.innerHTML = `<span>Newton:</span> <span style="color:#fde68a;">inverted 2nd prism recombines the spectrum → WHITE</span>`;

                    const p1 = createPrismMesh(1.4, 1.3);
                    p1.position.set(-1.55, -0.45, 0);
                    this.dynamicGroup.add(p1);

                    const p2 = createPrismMesh(1.4, 1.3, true);
                    p2.position.set(1.75, -0.45, 0);
                    this.dynamicGroup.add(p2);

                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-4.6, 0.85, 0), new THREE.Vector3(-2.2, 0.32, 0)], 0xf8fafc, 0.04));

                    // Parallel spectrum travelling between the prisms
                    C.vibgyor.forEach((col, k) => {
                        const y = 0.36 - k * 0.13;
                        this.dynamicGroup.add(createGlowRay([
                            new THREE.Vector3(-0.68, y, 0),
                            new THREE.Vector3(1.05, y, 0)
                        ], col, 0.03));
                    });

                    // Recombined white beam
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(2.42, -0.28, 0), new THREE.Vector3(4.7, -0.28, 0)], 0xf8fafc, 0.045));

                    const sLabel = makeLabel("Splits", "#fda4af", "rgba(15,23,42,0.9)", "#be123c", 1.2, 0.38);
                    sLabel.position.set(-1.55, -1.95, 0);
                    this.dynamicGroup.add(sLabel);

                    const rLabel = makeLabel("Recombines → WHITE", "#f8fafc", "rgba(15,23,42,0.9)", "#94a3b8", 2.6, 0.44);
                    rLabel.position.set(3.4, 0.35, 0);
                    this.dynamicGroup.add(rLabel);
                }
            }
// 5. RAINBOW DROP
            else if (this.type === "rainbow-drop") {
                if (this.step === 0) {
                    this.titleTag.innerHTML = `<span>Inside a raindrop:</span> <span style="color:#7dd3fc;">refract → internally reflect → refract again</span>`;

                    const drop = new THREE.Mesh(
                        new THREE.SphereGeometry(1.5, 48, 32),
                        new THREE.MeshPhysicalMaterial({ color: C.glass, transparent: true, opacity: 0.3, transmission: 0.9, roughness: 0.05 })
                    );
                    drop.position.set(0, 0.2, 0);
                    this.dynamicGroup.add(drop);

                    const entry = new THREE.Vector3(-0.45, 1.63, 0);   // on droplet surface
                    const back = new THREE.Vector3(1.44, -0.22, 0);    // internal reflection point
                    const exitP = new THREE.Vector3(2.35, -1.42, 0);   // dispersed rays leave

                    // Sunlight in (white)
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-4.2, 2.9, 0), entry], 0xf8fafc, 0.04));
                    // Refracted + internally reflected path (dim white)
                    this.dynamicGroup.add(createGlowRay([entry, back, exitP], 0xcbd5e1, 0.028));

                    // Dispersed VIBGYOR fan towards the observer
                    C.vibgyor.forEach((col, k) => {
                        this.dynamicGroup.add(createGlowRay([
                            exitP,
                            new THREE.Vector3(exitP.x + 1.15, exitP.y + 0.5 - k * 0.34, 0)
                        ], col, 0.03));
                    });

                    const sunLabel = makeLabel("Sunlight", "#fde68a", "rgba(15,23,42,0.9)", "#ca8a04", 1.5, 0.4);
                    sunLabel.position.set(-3.8, 3.25, 0);
                    this.dynamicGroup.add(sunLabel);

                    const obsLabel = makeLabel("Observer sees VIBGYOR", "#86efac", "rgba(15,23,42,0.9)", "#16a34a", 2.9, 0.44);
                    obsLabel.position.set(3.6, -2.6, 0);
                    this.dynamicGroup.add(obsLabel);
                }

                else {
                    this.titleTag.innerHTML = `<span>Rainbow:</span> <span style="color:#facc15;">always forms OPPOSITE the Sun</span>`;

                    // Sun
                    const sun = new THREE.Mesh(
                        new THREE.SphereGeometry(0.45, 24, 18),
                        new THREE.MeshBasicMaterial({ color: 0xfde047 })
                    );
                    sun.position.set(-4.2, 2.3, 0);
                    this.dynamicGroup.add(sun);
                    const sunGlow = new THREE.PointLight(0xfde047, 1.4, 12);
                    sunGlow.position.copy(sun.position);
                    this.dynamicGroup.add(sunGlow);

                    const sunTag = makeLabel("Sun", "#fde68a", "rgba(15,23,42,0.9)", "#ca8a04", 1.1, 0.38);
                    sunTag.position.set(-4.2, 3.1, 0);
                    this.dynamicGroup.add(sunTag);

                    // Concentric VIBGYOR arcs (red outermost) bowing away from the Sun
                    const arcCenter = { x: 0.8, y: -1.05 };
                    C.vibgyor.forEach((col, k) => {
                        const radius = 3.35 - k * 0.13;
                        const arc = new THREE.Mesh(
                            new THREE.TorusGeometry(radius, 0.06, 10, 90, Math.PI * 0.55),
                            new THREE.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.95 })
                        );
                        arc.position.set(arcCenter.x, arcCenter.y, 0);
                        arc.rotation.z = Math.PI * 0.02;
                        this.dynamicGroup.add(arc);
                    });

                    const observer = new THREE.Mesh(
                        new THREE.SphereGeometry(0.14, 14, 10),
                        new THREE.MeshBasicMaterial({ color: 0xfacc15 })
                    );
                    observer.position.set(0.8, -2.15, 0);
                    this.dynamicGroup.add(observer);

                    const obsTag = makeLabel("Observer", "#facc15", "rgba(15,23,42,0.9)", "#ca8a04", 1.4, 0.38);
                    obsTag.position.set(2.3, -2.5, 0);
                    this.dynamicGroup.add(obsTag);
                }
            }
// 6. TWINKLING STAR
            else if (this.type === "twinkling-star") {
                const observerTop = new THREE.Vector3(0, -0.56, 0);

                if (this.step === 0) {
                    this.titleTag.innerHTML = `<span>Stars = POINT sources:</span> <span style="color:#facc15;">apparent position flickers → TWINKLE ✨</span>`;

                    // Actual star
                    const star = new THREE.Mesh(
                        new THREE.SphereGeometry(0.12, 16, 12),
                        new THREE.MeshBasicMaterial({ color: 0xf8fafc })
                    );
                    star.position.set(-2.7, 4.2, 0);
                    this.dynamicGroup.add(star);
                    const starLight = new THREE.PointLight(0xf8fafc, 1.2, 14);
                    starLight.position.copy(star.position);
                    this.dynamicGroup.add(starLight);

                    // Flickering "apparent" ghost (higher than actual)
                    const ghost = new THREE.Mesh(
                        new THREE.SphereGeometry(0.17, 18, 14),
                        new THREE.MeshBasicMaterial({ color: C.laserCyan, transparent: true, opacity: 0.85 })
                    );
                    ghost.position.set(-2.28, 4.72, 0);
                    ghost.userData.baseX = ghost.position.x;
                    ghost.userData.baseY = ghost.position.y;
                    this.twinkleGhost = ghost;
                    this.dynamicGroup.add(ghost);

                    const actualLabel = makeLabel("Actual position", "#e2e8f0", "rgba(15,23,42,0.9)", "#94a3b8", 1.9, 0.4);
                    actualLabel.position.set(-3.9, 3.6, 0);
                    this.dynamicGroup.add(actualLabel);

                    const apparentLabel = makeLabel("Apparent (higher) — flickers", "#7dd3fc", "rgba(15,23,42,0.9)", "#0284c7", 3.0, 0.44);
                    apparentLabel.position.set(-1.15, 5.35, 0);
                    this.dynamicGroup.add(apparentLabel);

                    // Refracted ray bending through the atmosphere to the observer
                    this.dynamicGroup.add(createGlowRay([
                        new THREE.Vector3(-2.7, 4.2, 0),
                        new THREE.Vector3(-1.55, 2.4, 0),
                        new THREE.Vector3(-0.7, 0.8, 0),
                        observerTop
                    ], C.laserGold, 0.024));
                }

                else {
                    this.titleTag.innerHTML = `<span>Planets = EXTENDED sources:</span> <span style="color:#22c55e;">variations cancel → NO twinkle</span>`;

                    // Planet disc (extended source)
                    const planet = new THREE.Mesh(
                        new THREE.SphereGeometry(0.34, 24, 18),
                        new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.6 })
                    );
                    planet.position.set(-2.5, 4.1, 0);
                    this.dynamicGroup.add(planet);

                    const planetLabel = makeLabel("Planet — steady glow ✓", "#86efac", "rgba(15,23,42,0.9)", "#16a34a", 2.7, 0.44);
                    planetLabel.position.set(-1.35, 5.05, 0);
                    this.dynamicGroup.add(planetLabel);

                    this.dynamicGroup.add(createGlowRay([
                        new THREE.Vector3(-2.5, 4.1, 0),
                        new THREE.Vector3(-1.45, 2.35, 0),
                        new THREE.Vector3(-0.68, 0.8, 0),
                        observerTop
                    ], C.laserGreen, 0.026));
                }
            }
        }
/* --------------------------------------------------------------
           RENDER LOOP + SCENE-SPECIFIC EFFECTS
        -------------------------------------------------------------- */
        updateEffects() {
            // Accommodation: smooth lens thinning/thickening
            if (this.lensMorph && this.lensMorph.target !== undefined) {
                const m = this.lensMorph;
                m.mesh.scale.x += (m.target - m.mesh.scale.x) * 0.07;
                const squash = 1.04 - (m.mesh.scale.x - 0.30) * 0.28;
                m.mesh.scale.y += (squash - m.mesh.scale.y) * 0.07;
                m.mesh.scale.z = m.mesh.scale.y;
                if (m.ciliary) {
                    const squeezeTarget = m.target > 0.42 ? 0.9 : 1.05;
                    const s = m.ciliary.scale.x + (squeezeTarget - m.ciliary.scale.x) * 0.07;
                    m.ciliary.scale.set(s, s, s);
                }
            }

            // Twinkling: flicker the apparent star
            if (this.twinkleGhost && !this.isDragging) {
                const g = this.twinkleGhost;
                g.position.y = g.userData.baseY + Math.sin(this.time * 4.2) * 0.15;
                g.position.x = g.userData.baseX + Math.sin(this.time * 2.6) * 0.09;
                g.material.opacity = 0.55 + 0.4 * Math.sin(this.time * 6.0);
            }
        }

        animate() {
            requestAnimationFrame(() => this.animate());

            this.currentRotation.x += (this.targetRotation.x - this.currentRotation.x) * 0.12;
            this.currentRotation.y += (this.targetRotation.y - this.currentRotation.y) * 0.12;

            if (this.world) {
                this.world.rotation.x = this.currentRotation.x;
                this.world.rotation.y = this.currentRotation.y;
            }

            if (this.playing) {
                this.time += 0.02;
                if (!this.isDragging) {
                    this.camera.position.x = Math.sin(this.time * 0.4) * 0.25;
                    this.camera.position.y = 0.7 + Math.cos(this.time * 0.4) * 0.12;
                    this.camera.lookAt(0, 0, 0);
                }
                this.updateEffects();
            }

            this.renderer.render(this.scene, this.camera);
        }
    }

    /* ------------------------------------------------------------------
       BOOTSTRAP — mount a simulation into every [data-three-animation]
    ------------------------------------------------------------------ */
    function initAllEyeScenes() {
        const containers = document.querySelectorAll("[data-three-animation]");
        containers.forEach(el => {
            if (!el._opticsLabInitialized) {
                const animType = el.getAttribute("data-three-animation");
                new EyeOpticsSimulation(el, animType);
                el._opticsLabInitialized = true;
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initAllEyeScenes);
    } else {
        initAllEyeScenes();
    }
})();