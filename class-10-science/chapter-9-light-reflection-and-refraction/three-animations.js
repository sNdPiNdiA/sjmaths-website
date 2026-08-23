/*
==========================================================================
SJMaths — Class 10 Science Chapter 9
Light – Reflection and Refraction

PIXEL-PERFECT 3D OPTICS SIMULATION ENGINE (THREE.JS)
- Exact Mathematical Ray Tracing & Focal Collinearity
- True 3D Geometries (Biconcave & Biconvex Lenses, Parabolic Mirrors)
- Zero-Overlap Intelligent Label Placement
- Smooth Drag-to-Rotate, Zoom, and Touch Controls
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
        mirrorFront: 0x93c5fd,
        mirrorBack: 0x334155,
        glass: 0x38bdf8,
        normal: 0xc084fc,
        textLight: "#f8fafc",
        textGold: "#facc15",
        textCyan: "#38bdf8"
    };

    /* ------------------------------------------------------------------
       CLEAN HIGH-DPI SPRITE LABELS
    ------------------------------------------------------------------ */
    function makeLabel(text, color = "#f8fafc", bgColor = "rgba(15,23,42,0.88)", borderColor = "#334155", scaleW = 2.2, scaleH = 0.5) {
        const canvas = document.createElement("canvas");
        canvas.width = 512;
        canvas.height = 128;
        const ctx = canvas.getContext("2d");

        // Rounded badge
        ctx.fillStyle = bgColor;
        ctx.strokeStyle = borderColor;
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.roundRect(8, 8, 496, 112, 22);
        ctx.fill();
        ctx.stroke();

        // Text
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
        // Do not use CatmullRomCurve3 here: it bends the optical ray between
        // points and makes reflection/refraction diagrams physically wrong.
        const mesh = new THREE.Group();
        const mat = new THREE.MeshBasicMaterial({ color: color });
        const segments = [];

        // Build one straight tube per ray segment and place one arrow on each
        // sufficiently long segment.
        for (let i = 0; i < points.length - 1; i++) {
            const pA = points[i];
            const pB = points[i + 1];
            const curve = new THREE.LineCurve3(pA, pB);
            const geom = new THREE.TubeGeometry(curve, 1, radius, 10, false);
            const segment = new THREE.Mesh(geom, mat);
            segment.visible = false;
            mesh.add(segment);
            segments.push(segment);

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
        const pulse = new THREE.Mesh(
            new THREE.SphereGeometry(radius * 3.2, 10, 10),
            new THREE.MeshBasicMaterial({ color: color })
        );
        pulse.visible = false;
        mesh.add(pulse);
        mesh.userData.rayMotion = { points, pulse, segments, progress: 0 };
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
       REALISTIC 3D CANDLE
    ------------------------------------------------------------------ */
    function createCandle(height = 1.0, isReal = true) {
        const group = new THREE.Group();
        const baseRadius = 0.08;

        const bodyGeom = new THREE.CylinderGeometry(baseRadius, baseRadius, height, 20);
        const bodyMat = new THREE.MeshStandardMaterial({
            color: isReal ? 0xf97316 : 0x06b6d4,
            roughness: 0.25,
            metalness: 0.1,
            transparent: !isReal,
            opacity: isReal ? 1.0 : 0.65
        });
        const body = new THREE.Mesh(bodyGeom, bodyMat);
        body.position.y = height / 2;
        group.add(body);

        const wickGeom = new THREE.CylinderGeometry(0.015, 0.015, 0.12, 8);
        const wickMat = new THREE.MeshBasicMaterial({ color: 0x111827 });
        const wick = new THREE.Mesh(wickGeom, wickMat);
        wick.position.y = height + 0.06;
        group.add(wick);

        const flameGeom = new THREE.ConeGeometry(0.1, 0.28, 16);
        const flameMat = new THREE.MeshBasicMaterial({
            color: isReal ? 0xfef08a : 0x67e8f9,
            transparent: true,
            opacity: 0.95
        });
        const flame = new THREE.Mesh(flameGeom, flameMat);
        flame.position.y = height + 0.22;
        group.add(flame);

        if (isReal) {
            const light = new THREE.PointLight(0xfef08a, 1.2, 3);
            light.position.y = height + 0.22;
            group.add(light);
        }

        return group;
    }

    // Cartesian image solution in the diagram's world coordinates.  The
    // object is on the left of the optical element (x < 0); f is a positive
    // physical focal distance.  A negative image distance means a virtual
    // image on the object's side for a lens.
    function solveImageDistance(objectX, focalDistance) {
        const objectDistance = Math.abs(objectX);
        const denominator = (1 / focalDistance) - (1 / objectDistance);
        return Math.abs(denominator) < 1e-6 ? Infinity : 1 / denominator;
    }

    function imageHeight(objectHeight, objectX, imageDistance) {
        if (!Number.isFinite(imageDistance)) return objectHeight;
        return objectHeight * Math.abs(imageDistance / objectX);
    }

    /* ------------------------------------------------------------------
       TRUE BICONCAVE LENS GEOMETRY BUILDER
    ------------------------------------------------------------------ */
    function createBiconcaveLensGeometry(radius = 1.3, height = 2.4, waistThickness = 0.08, edgeThickness = 0.38) {
        const points = [];
        const segments = 24;
        points.push(new THREE.Vector2(0, -waistThickness));
        for (let i = 0; i <= segments; i++) {
            const r = (i / segments) * radius;
            const t = r / radius;
            const thickness = waistThickness + (edgeThickness - waistThickness) * t * t;
            points.push(new THREE.Vector2(r, -thickness));
        }
        for (let i = segments; i >= 0; i--) {
            const r = (i / segments) * radius;
            const t = r / radius;
            const thickness = waistThickness + (edgeThickness - waistThickness) * t * t;
            points.push(new THREE.Vector2(r, thickness));
        }
        const geom = new THREE.LatheGeometry(points, 40);
        geom.rotateZ(Math.PI / 2);
        return geom;
    }

    /* ------------------------------------------------------------------
       MAIN OPTICS SIMULATION CLASS
    ------------------------------------------------------------------ */
    class OpticsSimulation {
        constructor(container, sceneType) {
            this.container = container;
            this.type = sceneType;
            this.step = 0;
            this.maxSteps = 3;
            this.playing = true;
            this.time = 0;

            this.isDragging = false;
            this.prevMouse = { x: 0, y: 0 };
            this.targetRotation = { x: 0, y: 0 };
            this.currentRotation = { x: 0, y: 0 };
            this.zoom = 7.5;

            this.initDOM();
            this.initThree();
            this.buildBaseScene();
            this.setupInteraction();
            this.animate();
        }

        initDOM() {
            this.container.innerHTML = "";
            this.container.style.position = "relative";
            this.container.style.borderRadius = "16px";
            this.container.style.overflow = "hidden";
            this.container.style.background = "#090d16";
            this.container.style.border = "1.5px solid #1e293b";
            this.container.style.boxShadow = "0 10px 30px rgba(0,0,0,0.4)";
            this.container.style.margin = "16px 0";
            this.container.style.userSelect = "none";
            this.container.style.touchAction = "pan-y";

            this.canvasWrapper = document.createElement("div");
            this.canvasWrapper.style.width = "100%";
            this.canvasWrapper.style.height = this.container.dataset.height ? `${this.container.dataset.height}px` : "300px";
            this.canvasWrapper.style.cursor = "grab";
            this.container.appendChild(this.canvasWrapper);

            this.ctrlBar = document.createElement("div");
            Object.assign(this.ctrlBar.style, {
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "8px 12px",
                background: "rgba(15, 23, 42, 0.95)",
                borderTop: "1px solid #1e293b",
                fontSize: "11px",
                color: "#94a3b8",
                flexWrap: "wrap",
                gap: "6px"
            });

            this.titleTag = document.createElement("div");
            this.titleTag.style.fontWeight = "750";
            this.titleTag.style.color = "#38bdf8";
            this.titleTag.style.display = "flex";
            this.titleTag.style.alignItems = "center";
            this.titleTag.style.gap = "6px";
            this.ctrlBar.appendChild(this.titleTag);

            const btnGroup = document.createElement("div");
            btnGroup.style.display = "flex";
            btnGroup.style.alignItems = "center";
            btnGroup.style.gap = "5px";

            this.prevBtn = document.createElement("button");
            this.prevBtn.type = "button";
            this.prevBtn.innerHTML = "❮";
            this.prevBtn.title = "Previous Case";
            this.styleButton(this.prevBtn);
            this.prevBtn.onclick = e => { e.preventDefault(); e.stopPropagation(); this.prevStep(); };
            btnGroup.appendChild(this.prevBtn);

            this.playBtn = document.createElement("button");
            this.playBtn.type = "button";
            this.playBtn.innerHTML = "⏸";
            this.playBtn.title = "Play / Pause";
            this.styleButton(this.playBtn);
            this.playBtn.onclick = e => { e.preventDefault(); e.stopPropagation(); this.togglePlay(); };
            btnGroup.appendChild(this.playBtn);

            this.nextBtn = document.createElement("button");
            this.nextBtn.type = "button";
            this.nextBtn.innerHTML = "Next Case ❯";
            this.styleButton(this.nextBtn, true);
            this.nextBtn.onclick = e => { e.preventDefault(); e.stopPropagation(); this.nextStep(); };
            btnGroup.appendChild(this.nextBtn);

            this.resetBtn = document.createElement("button");
            this.resetBtn.type = "button";
            this.resetBtn.innerHTML = "↺ View";
            this.resetBtn.title = "Reset 3D View";
            this.styleButton(this.resetBtn);
            this.resetBtn.onclick = e => { e.preventDefault(); e.stopPropagation(); this.resetCamera(); };
            btnGroup.appendChild(this.resetBtn);

            this.ctrlBar.appendChild(btnGroup);
            this.container.appendChild(this.ctrlBar);
        }

        styleButton(btn, isPrimary = false) {
            Object.assign(btn.style, {
                background: isPrimary ? "linear-gradient(135deg, #2563eb, #1d4ed8)" : "#1e293b",
                border: isPrimary ? "1px solid #3b82f6" : "1px solid #334155",
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
                btn.style.boxShadow = "0 3px 8px rgba(37,99,235,0.3)";
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

            this.camera = new THREE.PerspectiveCamera(38, w / h, 0.1, 100);
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
                this.zoom = Math.max(4.5, Math.min(11.0, this.zoom + e.deltaY * 0.005));
                this.camera.position.z = this.zoom;
            }, { passive: false });
        }

        resetCamera() {
            this.targetRotation.x = 0;
            this.targetRotation.y = 0;
            this.zoom = 7.5;
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
                case "reflection-laws":
                    this.buildReflectionLawsBase();
                    break;
                case "concave-mirror":
                    this.buildConcaveMirrorBase();
                    break;
                case "convex-mirror":
                    this.buildConvexMirrorBase();
                    break;
                case "glass-slab":
                    this.buildGlassSlabBase();
                    break;
                case "convex-lens":
                    this.buildConvexLensBase();
                    break;
                case "concave-lens":
                    this.buildConcaveLensBase();
                    break;
                case "power-comparison":
                    this.buildPowerComparisonBase();
                    break;
            }
            this.rebuildDynamicElements();
        }

        /* 1. LAWS OF REFLECTION */
        buildReflectionLawsBase() {
            this.maxSteps = 3;
            const mirror = new THREE.Mesh(
                new THREE.BoxGeometry(4.8, 0.08, 2.6),
                new THREE.MeshStandardMaterial({ color: C.mirrorFront, metalness: 0.95, roughness: 0.08, transparent: true, opacity: 0.9 })
            );
            mirror.position.y = -0.04;
            this.world.add(mirror);

            const back = new THREE.Mesh(
                new THREE.BoxGeometry(4.8, 0.04, 2.6),
                new THREE.MeshStandardMaterial({ color: C.mirrorBack, roughness: 0.85 })
            );
            back.position.y = -0.1;
            this.world.add(back);

            this.world.add(createVirtualRay([new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 2.3, 0)], C.normal));
            const normalLabel = makeLabel("Normal (N)", "#c084fc", "rgba(15,23,42,0.9)", "#7e22ce", 1.8, 0.45);
            normalLabel.position.set(0, 2.55, 0);
            this.world.add(normalLabel);
        }

        /* 2. CONCAVE MIRROR */
        buildConcaveMirrorBase() {
            this.maxSteps = 4;
            const mirrorGeom = new THREE.CylinderGeometry(2.5, 2.5, 2.4, 32, 1, true, Math.PI * 0.83, Math.PI * 0.34);
            const mirrorMat = new THREE.MeshStandardMaterial({ color: C.mirrorFront, metalness: 0.92, roughness: 0.12, side: THREE.DoubleSide });
            const mirror = new THREE.Mesh(mirrorGeom, mirrorMat);
            mirror.rotation.y = Math.PI / 2;
            // The ray diagrams use the mirror pole at x = 0.
            mirror.position.set(0, 0, 0);
            this.world.add(mirror);

            this.world.add(createVirtualRay([new THREE.Vector3(-4.8, 0, 0), new THREE.Vector3(3.2, 0, 0)], C.axis));

            const pLabel = makeLabel("Pole (P)", "#f8fafc", "rgba(15,23,42,0.85)", "#334155", 1.2, 0.35);
            pLabel.position.set(0.1, -0.4, 0);
            this.world.add(pLabel);

            const fLabel = makeLabel("Focus (F)", "#facc15", "rgba(15,23,42,0.85)", "#ca8a04", 1.2, 0.35);
            fLabel.position.set(-1.25, -0.4, 0);
            this.world.add(fLabel);

            const cLabel = makeLabel("Centre (C)", "#38bdf8", "rgba(15,23,42,0.85)", "#0284c7", 1.2, 0.35);
            cLabel.position.set(-2.5, -0.4, 0);
            this.world.add(cLabel);
        }

        /* 3. CONVEX MIRROR */
        buildConvexMirrorBase() {
            this.maxSteps = 2;
            const mirrorGeom = new THREE.CylinderGeometry(2.5, 2.5, 2.4, 32, 1, true, -Math.PI * 0.17, Math.PI * 0.34);
            const mirrorMat = new THREE.MeshStandardMaterial({ color: C.mirrorFront, metalness: 0.92, roughness: 0.12, side: THREE.DoubleSide });
            const mirror = new THREE.Mesh(mirrorGeom, mirrorMat);
            mirror.rotation.y = Math.PI / 2;
            // The ray diagrams use the mirror pole at x = 0.
            mirror.position.set(0, 0, 0);
            this.world.add(mirror);

            this.world.add(createVirtualRay([new THREE.Vector3(-4.8, 0, 0), new THREE.Vector3(3.5, 0, 0)], C.axis));

            const pLabel = makeLabel("Pole (P)", "#f8fafc", "rgba(15,23,42,0.85)", "#334155", 1.2, 0.35);
            pLabel.position.set(-0.1, -0.4, 0);
            this.world.add(pLabel);

            const fLabel = makeLabel("Focus (F)", "#facc15", "rgba(15,23,42,0.85)", "#ca8a04", 1.2, 0.35);
            fLabel.position.set(1.25, -0.4, 0);
            this.world.add(fLabel);
        }

        /* 4. GLASS SLAB */
        buildGlassSlabBase() {
            this.maxSteps = 2;
            const slabGeom = new THREE.BoxGeometry(4.2, 1.5, 2.4);
            const slabMat = new THREE.MeshPhysicalMaterial({
                color: C.glass,
                transparent: true,
                opacity: 0.35,
                roughness: 0.05,
                transmission: 0.88,
                ior: 1.5
            });
            const slab = new THREE.Mesh(slabGeom, slabMat);
            this.world.add(slab);

            const edges = new THREE.LineSegments(new THREE.EdgesGeometry(slabGeom), new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.45 }));
            this.world.add(edges);

            // Clean labels placed outside the ray path (top left and top right)
            const airLabel = makeLabel("Air (Rarer, n = 1.0)", "#94a3b8", "rgba(15,23,42,0.9)", "#334155", 2.2, 0.42);
            airLabel.position.set(-2.2, 1.45, 0);
            this.world.add(airLabel);

            const slabTag = makeLabel("Glass Slab (Denser, n = 1.50)", "#38bdf8", "rgba(15,23,42,0.9)", "#0284c7", 2.9, 0.45);
            slabTag.position.set(0, 1.1, 0);
            this.world.add(slabTag);
        }

        /* 5. CONVEX LENS */
        buildConvexLensBase() {
            this.maxSteps = 3;
            const lensGeom = new THREE.SphereGeometry(1.6, 32, 16);
            lensGeom.scale(0.18, 1.35, 1.35);
            const lensMat = new THREE.MeshPhysicalMaterial({
                color: C.glass,
                transparent: true,
                opacity: 0.45,
                transmission: 0.9,
                roughness: 0.08
            });
            const lens = new THREE.Mesh(lensGeom, lensMat);
            this.world.add(lens);

            this.world.add(createVirtualRay([new THREE.Vector3(-4.8, 0, 0), new THREE.Vector3(4.8, 0, 0)], C.axis));

            const oLabel = makeLabel("O", "#f8fafc", "rgba(15,23,42,0.85)", "#334155", 0.6, 0.35);
            oLabel.position.set(0, -0.4, 0);
            this.world.add(oLabel);

            const f1Label = makeLabel("F₁", "#facc15", "rgba(15,23,42,0.85)", "#ca8a04", 0.8, 0.35);
            f1Label.position.set(-1.4, -0.4, 0);
            this.world.add(f1Label);

            const f2Label = makeLabel("F₂", "#facc15", "rgba(15,23,42,0.85)", "#ca8a04", 0.8, 0.35);
            f2Label.position.set(1.4, -0.4, 0);
            this.world.add(f2Label);
        }

        /* 6. CONCAVE LENS */
        buildConcaveLensBase() {
            this.maxSteps = 2;

            // True Biconcave Lens 3D mesh representation
            const topBlock = new THREE.Mesh(
                createBiconcaveLensGeometry(),
                new THREE.MeshPhysicalMaterial({ color: C.glass, transparent: true, opacity: 0.42, transmission: 0.88, roughness: 0.08 })
            );
            this.world.add(topBlock);

            const edges = new THREE.LineSegments(new THREE.EdgesGeometry(topBlock.geometry), new THREE.LineBasicMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.4 }));
            this.world.add(edges);

            this.world.add(createVirtualRay([new THREE.Vector3(-4.8, 0, 0), new THREE.Vector3(4.8, 0, 0)], C.axis));

            const f1Label = makeLabel("Focus F₁", "#facc15", "rgba(15,23,42,0.9)", "#ca8a04", 1.4, 0.36);
            f1Label.position.set(-1.4, -0.45, 0);
            this.world.add(f1Label);
        }

        /* 7. POWER COMPARISON */
        buildPowerComparisonBase() {
            this.maxSteps = 2;
            this.world.add(createVirtualRay([new THREE.Vector3(-4.8, 0, 0), new THREE.Vector3(4.8, 0, 0)], C.axis));
        }

        /* --------------------------------------------------------------
           DYNAMIC CASE RAY TRACING & PERFECT INTERSECTIONS
        -------------------------------------------------------------- */
        rebuildDynamicElements() {
            while (this.dynamicGroup.children.length > 0) {
                const child = this.dynamicGroup.children.pop();
                if (child.geometry) child.geometry.dispose();
            }

            // 1. Reflection Laws
            if (this.type === "reflection-laws") {
                const angleDeg = this.step === 0 ? 45 : this.step === 1 ? 30 : 60;
                this.titleTag.innerHTML = `<span>⚡ Reflection:</span> <span style="color:#facc15;">∠i = ∠r = ${angleDeg}°</span>`;
                const rad = (angleDeg * Math.PI) / 180;
                const len = 2.5;

                const incStart = new THREE.Vector3(-Math.sin(rad) * len, Math.cos(rad) * len, 0);
                const hit = new THREE.Vector3(0, 0, 0);
                const refEnd = new THREE.Vector3(Math.sin(rad) * len, Math.cos(rad) * len, 0);

                this.dynamicGroup.add(createGlowRay([incStart, hit], C.laserGold, 0.034));
                this.dynamicGroup.add(createGlowRay([hit, refEnd], C.laserCyan, 0.034));

                const incLabel = makeLabel(`Incident Ray (∠i = ${angleDeg}°)`, "#facc15", "rgba(15,23,42,0.9)", "#ca8a04", 2.3, 0.44);
                incLabel.position.set(incStart.x * 0.62, incStart.y * 0.62 + 0.22, 0);
                this.dynamicGroup.add(incLabel);

                const refLabel = makeLabel(`Reflected Ray (∠r = ${angleDeg}°)`, "#38bdf8", "rgba(15,23,42,0.9)", "#0284c7", 2.3, 0.44);
                refLabel.position.set(refEnd.x * 0.62, refEnd.y * 0.62 + 0.22, 0);
                this.dynamicGroup.add(refLabel);
            }

            // 2. Concave Mirror
            else if (this.type === "concave-mirror") {
                if (this.step === 0) {
                    this.titleTag.innerHTML = `<span>Concave Mirror:</span> <span style="color:#facc15;">Parallel Rays Converge at Focus F</span>`;
                    [-0.75, -0.38, 0.38, 0.75].forEach(y => {
                        const start = new THREE.Vector3(-4.2, y, 0);
                        const hit = new THREE.Vector3(0, y, 0);
                        const focus = new THREE.Vector3(-1.25, 0, 0);
                        const ext = new THREE.Vector3(-2.8, -y * 1.24, 0);
                        this.dynamicGroup.add(createGlowRay([start, hit, focus, ext], C.laserGold, 0.026));
                    });
                } else if (this.step === 1) {
                    this.titleTag.innerHTML = `<span>Concave Mirror:</span> <span style="color:#38bdf8;">Object Beyond C → Real Inverted Diminished Image</span>`;
                    const candle = createCandle(1.1, true);
                    candle.position.set(-3.3, 0, 0);
                    this.dynamicGroup.add(candle);

                    const imageDistance = solveImageDistance(-3.3, 1.25);
                    const img = createCandle(imageHeight(1.1, -3.3, imageDistance), false);
                    img.rotation.z = Math.PI;
                    img.position.set(-Math.abs(imageDistance), 0, 0);
                    this.dynamicGroup.add(img);

                    const realImage = new THREE.Vector3(-Math.abs(imageDistance), -imageHeight(1.1, -3.3, imageDistance), 0);
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-3.3, 1.1, 0), new THREE.Vector3(0, 1.1, 0), realImage], C.laserGold, 0.024));
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-3.3, 1.1, 0), new THREE.Vector3(0, -0.7, 0), realImage], C.laserCyan, 0.024));
                } else if (this.step === 2) {
                    this.titleTag.innerHTML = `<span>Concave Mirror:</span> <span style="color:#facc15;">Object at C → Same Size Real Inverted Image at C</span>`;
                    const candle = createCandle(0.9, true);
                    candle.position.set(-2.5, 0, 0);
                    this.dynamicGroup.add(candle);

                    const imageDistance = solveImageDistance(-2.5, 1.25);
                    const img = createCandle(imageHeight(0.9, -2.5, imageDistance), false);
                    img.rotation.z = Math.PI;
                    img.position.set(-Math.abs(imageDistance), 0, 0);
                    this.dynamicGroup.add(img);

                    const sameSizeImage = new THREE.Vector3(-Math.abs(imageDistance), -imageHeight(0.9, -2.5, imageDistance), 0);
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-2.5, 0.9, 0), new THREE.Vector3(0, 0.9, 0), sameSizeImage], C.laserGold, 0.024));
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-2.5, 0.9, 0), new THREE.Vector3(0, 0.35, 0), sameSizeImage], C.laserCyan, 0.024));
                } else {
                    this.titleTag.innerHTML = `<span>Concave Mirror:</span> <span style="color:#f43f5e;">Object Between P & F → Virtual Erect Magnified</span>`;
                    const candle = createCandle(0.65, true);
                    candle.position.set(-0.6, 0, 0);
                    this.dynamicGroup.add(candle);

                    const imageDistance = solveImageDistance(-0.6, 1.25);
                    const imageH = imageHeight(0.65, -0.6, imageDistance);
                    const img = createCandle(imageH, false);
                    img.position.set(Math.abs(imageDistance), 0, 0);
                    this.dynamicGroup.add(img);

                    // Real incident and reflected rays in front of the mirror.
                    // The reflected rays diverge, so their backward dashed
                    // extensions meet behind the mirror at the virtual image.
                    const topObject = new THREE.Vector3(-0.6, 0.65, 0);
                    const topHit = new THREE.Vector3(0, 0.65, 0);
                    const topReflected = new THREE.Vector3(-1.9, 1.15, 0);
                    const lowerObject = new THREE.Vector3(-0.6, 0.18, 0);
                    const lowerHit = new THREE.Vector3(0, 0.18, 0);
                    const lowerReflected = new THREE.Vector3(-1.9, -0.55, 0);

                    this.dynamicGroup.add(createGlowRay([topObject, topHit], C.laserGold, 0.024));
                    this.dynamicGroup.add(createGlowRay([topHit, topReflected], C.laserGold, 0.024));
                    this.dynamicGroup.add(createGlowRay([lowerObject, lowerHit], C.laserCyan, 0.024));
                    this.dynamicGroup.add(createGlowRay([lowerHit, lowerReflected], C.laserCyan, 0.024));

                    const virtualImage = new THREE.Vector3(Math.abs(imageDistance), imageH, 0);
                    this.dynamicGroup.add(createVirtualRay([topHit, virtualImage], 0x38bdf8));
                    this.dynamicGroup.add(createVirtualRay([lowerHit, virtualImage], 0x38bdf8));
                }
            }

            // 3. Convex Mirror (PERFECT COLLINEAR RAYS & ACCURATE VIRTUAL INTERSECTION)
            else if (this.type === "convex-mirror") {
                this.titleTag.innerHTML = `<span>Convex Mirror:</span> <span style="color:#38bdf8;">Diverging Action → Virtual, Erect & Diminished Image</span>`;
                
                const objX = -2.8;
                const objH = 1.1;
                const candle = createCandle(objH, true);
                candle.position.set(objX, 0, 0);
                this.dynamicGroup.add(candle);

                // Focus at (1.25, 0)
                const fX = 1.25;
                // Virtual image position via mirror formula: 1/v = 1/f - 1/u = 1/1.25 - 1/(-2.8) = 0.8 + 0.357 = 1.157 => v = +0.864
                const imgX = 0.864;
                const imgH = objH * (imgX / Math.abs(objX)); // 1.1 * (0.864/2.8) = 0.34

                const virtCandle = createCandle(imgH, false);
                virtCandle.position.set(imgX, 0, 0);
                this.dynamicGroup.add(virtCandle);

                // Ray 1: Parallel to axis from (-2.8, 1.1) to mirror vertex (0, 1.1)
                const pHit1 = new THREE.Vector3(0, objH, 0);
                const pStart1 = new THREE.Vector3(objX, objH, 0);
                this.dynamicGroup.add(createGlowRay([pStart1, pHit1], C.laserGold, 0.028));

                // Ray 1 Virtual backward line to focus (1.25, 0)
                const pFocus = new THREE.Vector3(fX, 0, 0);
                this.dynamicGroup.add(createVirtualRay([pHit1, pFocus], 0x38bdf8));

                // Ray 1 Reflected ray: exactly in line with direction from Focus (1.25, 0) through (0, 1.1)
                const dir1 = new THREE.Vector3().subVectors(pHit1, pFocus).normalize();
                const pRef1 = new THREE.Vector3().addVectors(pHit1, dir1.clone().multiplyScalar(2.6));
                this.dynamicGroup.add(createGlowRay([pHit1, pRef1], C.laserGold, 0.028));

                // Ray 2: Aiming at Pole (0,0) with angle i = angle r
                const anglePole = Math.atan2(objH, Math.abs(objX));
                const pRef2 = new THREE.Vector3(objX, -objH, 0);
                this.dynamicGroup.add(createGlowRay([pStart1, new THREE.Vector3(0, 0, 0), pRef2], C.laserCyan, 0.024));
                this.dynamicGroup.add(createVirtualRay([new THREE.Vector3(0, 0, 0), new THREE.Vector3(imgX, imgH, 0)], 0x38bdf8));
            }

            // 4. Glass Slab Refraction (CLEAN NON-OVERLAPPING LABELS & EXACT SNELL SINE)
            else if (this.type === "glass-slab") {
                this.titleTag.innerHTML = `<span>Glass Slab Refraction:</span> <span style="color:#facc15;">Emergent Ray || Incident Ray (Lateral Shift d)</span>`;
                
                const yTop = 0.75;
                const yBot = -0.75;
                const hitTop = new THREE.Vector3(-1.0, yTop, 0);
                const hitBot = new THREE.Vector3(0.45, yBot, 0);

                const incStart = new THREE.Vector3(-3.2, 1.8, 0);
                const emergEnd = new THREE.Vector3(2.65, -1.8, 0);

                // Incident, Inside, Emergent rays
                this.dynamicGroup.add(createGlowRay([incStart, hitTop], C.laserGold, 0.034));
                this.dynamicGroup.add(createGlowRay([hitTop, hitBot], C.laserCyan, 0.034));
                this.dynamicGroup.add(createGlowRay([hitBot, emergEnd], C.laserGold, 0.034));

                // Normal lines at top and bottom interfaces
                this.dynamicGroup.add(createVirtualRay([new THREE.Vector3(-1.0, 1.3, 0), new THREE.Vector3(-1.0, 0.2, 0)], C.normal));
                this.dynamicGroup.add(createVirtualRay([new THREE.Vector3(0.45, -0.2, 0), new THREE.Vector3(0.45, -1.3, 0)], C.normal));

                // Undeviated dotted line continuation
                const undeviatedEnd = new THREE.Vector3(1.5, -1.8, 0);
                this.dynamicGroup.add(createVirtualRay([hitTop, undeviatedEnd], 0x94a3b8));

                // Clean lateral shift indicator placed below without overlapping
                const shiftLabel = makeLabel("Lateral Shift (d)", "#facc15", "rgba(15,23,42,0.92)", "#ca8a04", 2.2, 0.44);
                shiftLabel.position.set(2.05, -1.15, 0);
                this.dynamicGroup.add(shiftLabel);
            }

            // 5. Convex Lens
            else if (this.type === "convex-lens") {
                if (this.step === 0) {
                    this.titleTag.innerHTML = `<span>Convex Lens:</span> <span style="color:#facc15;">Parallel Rays Converge at Real Focus F₂</span>`;
                    [-0.7, -0.35, 0.35, 0.7].forEach(y => {
                        const p1 = new THREE.Vector3(-4.0, y, 0);
                        const p2 = new THREE.Vector3(0, y, 0);
                        const p3 = new THREE.Vector3(1.4, 0, 0);
                        const p4 = new THREE.Vector3(3.4, -y * 1.28, 0);
                        this.dynamicGroup.add(createGlowRay([p1, p2, p3, p4], C.laserGold, 0.026));
                    });
                } else if (this.step === 1) {
                    this.titleTag.innerHTML = `<span>Convex Lens:</span> <span style="color:#38bdf8;">Object Beyond 2F₁ → Real Inverted Image</span>`;
                    const candle = createCandle(1.0, true);
                    candle.position.set(-3.0, 0, 0);
                    this.dynamicGroup.add(candle);

                    const imageDistance = solveImageDistance(-3.0, 1.4);
                    const img = createCandle(imageHeight(1.0, -3.0, imageDistance), false);
                    img.rotation.z = Math.PI;
                    img.position.set(Math.abs(imageDistance), 0, 0);
                    this.dynamicGroup.add(img);

                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-3.0, 1.0, 0), new THREE.Vector3(0, 1.0, 0), new THREE.Vector3(1.4, 0, 0), new THREE.Vector3(2.1, -0.65, 0)], C.laserGold, 0.024));
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-3.0, 1.0, 0), new THREE.Vector3(0, 0, 0), new THREE.Vector3(2.1, -0.65, 0)], C.laserCyan, 0.024));
                } else {
                    this.titleTag.innerHTML = `<span>Convex Lens (Magnifier):</span> <span style="color:#f43f5e;">Object Between F₁ & O → Virtual Erect Enlarged</span>`;
                    const candle = createCandle(0.7, true);
                    candle.position.set(-0.7, 0, 0);
                    this.dynamicGroup.add(candle);

                    const imageDistance = solveImageDistance(-0.7, 1.4);
                    const imageH = imageHeight(0.7, -0.7, imageDistance);
                    const img = createCandle(imageH, false);
                    img.position.set(-Math.abs(imageDistance), 0, 0);
                    this.dynamicGroup.add(img);

                    const virtualImage = new THREE.Vector3(-Math.abs(imageDistance), imageH, 0);
                    // Two real rays emerge from the object and diverge after
                    // the lens; dashed backward extensions meet at the image.
                    const rayA = new THREE.Vector3(0, 0.7, 0);
                    const rayB = new THREE.Vector3(0, 0.2, 0);
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-0.7, 0.7, 0), rayA, new THREE.Vector3(2.2, 1.25, 0)], C.laserGold, 0.024));
                    this.dynamicGroup.add(createGlowRay([new THREE.Vector3(-0.7, 0.7, 0), rayB, new THREE.Vector3(2.2, -0.45, 0)], C.laserCyan, 0.024));
                    this.dynamicGroup.add(createVirtualRay([rayA, virtualImage], 0x38bdf8));
                    this.dynamicGroup.add(createVirtualRay([rayB, virtualImage], 0x38bdf8));
                }
            }

            // 6. Concave Lens (TRUE COLLINEAR DIVERGENCE FROM F₁)
            else if (this.type === "concave-lens") {
                this.titleTag.innerHTML = `<span>Concave Lens:</span> <span style="color:#38bdf8;">Diverging Action → Virtual Focus at F₁</span>`;
                const fX = -1.4; // F1 position

                [-0.65, -0.3, 0.3, 0.65].forEach(y => {
                    const pHit = new THREE.Vector3(0, y, 0);
                    const pStart = new THREE.Vector3(-4.0, y, 0);

                    // 1. Incoming parallel ray
                    this.dynamicGroup.add(createGlowRay([pStart, pHit], C.laserGold, 0.026));

                    // 2. Virtual backward dashed line to Focus F1 (-1.4, 0)
                    const pF1 = new THREE.Vector3(fX, 0, 0);
                    this.dynamicGroup.add(createVirtualRay([pHit, pF1], 0x38bdf8));

                    // 3. Forward diverging ray: EXACTLY in line with vector from F1 through hit point
                    const dir = new THREE.Vector3().subVectors(pHit, pF1).normalize();
                    const pEnd = new THREE.Vector3().addVectors(pHit, dir.clone().multiplyScalar(2.6));
                    this.dynamicGroup.add(createGlowRay([pHit, pEnd], C.laserGold, 0.026));
                });
            }

            // 7. Power Comparison
            else if (this.type === "power-comparison") {
                const isHighPower = this.step === 0;
                const fDist = isHighPower ? 1.1 : 2.6;
                const pText = isHighPower ? "+8.0 D (Short f = 12.5 cm)" : "+2.0 D (Long f = 50 cm)";
                this.titleTag.innerHTML = `<span>Power P = 1/f:</span> <span style="color:${isHighPower ? "#facc15" : "#38bdf8"};">${pText}</span>`;

                const lensGeom = new THREE.SphereGeometry(1.4, 32, 16);
                lensGeom.scale(isHighPower ? 0.34 : 0.14, 1.3, 1.3);
                const lensMat = new THREE.MeshPhysicalMaterial({ color: C.glass, transparent: true, opacity: 0.5 });
                const lens = new THREE.Mesh(lensGeom, lensMat);
                this.dynamicGroup.add(lens);

                [-0.55, 0.55].forEach(y => {
                    const p1 = new THREE.Vector3(-3.8, y, 0);
                    const p2 = new THREE.Vector3(0, y, 0);
                    const p3 = new THREE.Vector3(fDist, 0, 0);
                    const p4 = new THREE.Vector3(fDist + 1.2, -y * 0.9, 0);
                    this.dynamicGroup.add(createGlowRay([p1, p2, p3, p4], C.laserGold, 0.03));
                });

                const powerLabel = makeLabel(`P = ${pText}`, isHighPower ? "#facc15" : "#38bdf8", "rgba(15,23,42,0.9)", isHighPower ? "#ca8a04" : "#0284c7", 3.8, 0.52);
                powerLabel.position.set(0, 1.45, 0);
                this.dynamicGroup.add(powerLabel);
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

            if (this.playing) this.time += 0.02;
            this.camera.lookAt(0, 0, 0);

            // Draw each ray from its source in sequence. The glowing pulse is
            // the drawing front; after completion the full ray remains shown.
            this.dynamicGroup.traverse(node => {
                const motion = node.userData && node.userData.rayMotion;
                if (!motion || !motion.points || motion.points.length < 2) return;
                if (motion.progress < 1) {
                    if (this.playing) motion.progress = Math.min(1, motion.progress + 0.012 * 0.7);
                    const segmentCount = motion.segments.length;
                    const revealed = motion.progress * segmentCount;
                    motion.segments.forEach((segment, index) => {
                        segment.visible = index < revealed;
                    });
                    motion.pulse.visible = motion.progress < 1;
                } else {
                    motion.segments.forEach(segment => { segment.visible = true; });
                    motion.pulse.visible = false;
                    return;
                }
                const lengths = [];
                let total = 0;
                for (let i = 0; i < motion.points.length - 1; i++) {
                    const length = motion.points[i].distanceTo(motion.points[i + 1]);
                    lengths.push(length);
                    total += length;
                }
                if (!total) return;
                // Slow classroom-friendly ray motion.
                let distance = motion.progress * total;
                for (let i = 0; i < lengths.length; i++) {
                    if (distance <= lengths[i] || i === lengths.length - 1) {
                        const ratio = lengths[i] ? distance / lengths[i] : 0;
                        motion.pulse.position.lerpVectors(motion.points[i], motion.points[i + 1], ratio);
                        break;
                    }
                    distance -= lengths[i];
                }
            });

            this.renderer.render(this.scene, this.camera);
        }
    }

    function initAllOpticsScenes() {
        const containers = document.querySelectorAll("[data-three-animation]");
        containers.forEach(el => {
            if (!el._opticsLabInitialized) {
                const animType = el.getAttribute("data-three-animation");
                new OpticsSimulation(el, animType);
                el._opticsLabInitialized = true;
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initAllOpticsScenes);
    } else {
        initAllOpticsScenes();
    }
})();
