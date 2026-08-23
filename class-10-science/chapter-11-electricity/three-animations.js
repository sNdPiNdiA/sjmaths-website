/*
==========================================================================
SJMaths — Class 10 Science Chapter 11
ELECTRICITY

INTERACTIVE 3D ELECTRIC CIRCUIT SIMULATION ENGINE (THREE.JS)
- Live Electron Drift in Closed Loops (Open/Closed Switch)
- Ohm's Law: More Cells ⇒ More Voltage ⇒ Faster Charge Flow
- Resistance Factors: Thin vs Thick, Short vs Long, Copper vs Nichrome
- Series vs Parallel Networks with Glowing Lamps
- Joule Heating: Nichrome Coil Radiating Heat
- Smooth Drag-to-Rotate, Zoom, Touch Controls & Case Buttons
==========================================================================
*/

(() => {
    "use strict";

    if (typeof THREE === "undefined") {
        console.error("SJMaths Three.js: THREE is not loaded.");
        return;
    }

    /* ------------------------------------------------------------------
       COLOR PALETTE (amber electric theme)
    ------------------------------------------------------------------ */
    const C = {
        bg: 0x0b0e14,
        wire: 0x94a3b8,
        electron: 0x22d3ee,
        batteryBody: 0x334155,
        terminalPlus: 0xf59e0b,
        terminalMinus: 0x64748b,
        lampGlass: 0xcbd5e1,
        lampGlow: 0xfacc15,
        resistor: 0xb45309,
        copper: 0xf97316,
        nichrome: 0xa78bfa,
        metal: 0xcbd5e1,
        textCyan: "#67e8f9",
        textGold: "#facc15",
        textGreen: "#86efac",
        textRose: "#fda4af"
    };

    const LABEL_BG = "rgba(9,13,22,0.88)";
    const LABEL_BORDER = "#334155";

    /* ------------------------------------------------------------------
       CLEAN HIGH-DPI SPRITE LABELS
    ------------------------------------------------------------------ */
    function makeLabel(text, color = "#f8fafc", bgColor = LABEL_BG, borderColor = LABEL_BORDER, scaleW = 2.2, scaleH = 0.5) {
        const cv = document.createElement("canvas");
        cv.width = 512;
        cv.height = 128;
        const ctx = cv.getContext("2d");

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

        const texture = new THREE.CanvasTexture(cv);
        texture.colorSpace = THREE.SRGBColorSpace;
        texture.minFilter = THREE.LinearFilter;
        const mat = new THREE.SpriteMaterial({ map: texture, transparent: true, depthTest: false });
        const sprite = new THREE.Sprite(mat);
        sprite.scale.set(scaleW, scaleH, 1);
        return sprite;
    }

    /* ------------------------------------------------------------------
       GLOWING TUBE PATH WITH ARROW CONES
    ------------------------------------------------------------------ */
    function createFlowPath(points, color = C.wire, radius = 0.05, arrows = false, arrowColor = 0xfacc15) {
        const curve = new THREE.CatmullRomCurve3(points);
        const geom = new THREE.TubeGeometry(curve, Math.max(24, points.length * 12), radius, 10, false);
        const mesh = new THREE.Mesh(geom, new THREE.MeshStandardMaterial({
            color: color, roughness: 0.45, metalness: 0.55
        }));
        mesh.userData.curve = curve;

        if (arrows) {
            for (let i = 0; i < points.length - 1; i++) {
                const pA = points[i];
                const pB = points[i + 1];
                if (pA.distanceTo(pB) < 0.5) continue;
                const mid = new THREE.Vector3().addVectors(pA, pB).multiplyScalar(0.5);
                const dir = new THREE.Vector3().subVectors(pB, pA).normalize();
                const cone = new THREE.Mesh(
                    new THREE.ConeGeometry(radius * 2.6, radius * 5, 12),
                    new THREE.MeshBasicMaterial({ color: arrowColor })
                );
                cone.position.copy(mid);
                cone.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir);
                mesh.add(cone);
            }
        }
        return mesh;
    }

    /* ------------------------------------------------------------------
       ELECTRON SWARM ALONG A CURVE
    ------------------------------------------------------------------ */
    function makeElectronSwarm(curve, count, color = C.electron, size = 0.075) {
        const group = new THREE.Group();
        const riders = [];
        for (let i = 0; i < count; i++) {
            const s = new THREE.Mesh(
                new THREE.SphereGeometry(size, 12, 10),
                new THREE.MeshBasicMaterial({ color: color })
            );
            s.userData.offset = i / count;
            group.add(s);
            riders.push(s);
        }
        group.userData.riders = riders;
        group.userData.curve = curve;
        return group;
    }

    function placeElectronSwarm(swarm, t01, speed) {
        const curve = swarm.userData.curve;
        swarm.userData.riders.forEach(r => {
            const u = ((r.userData.offset + t01 * speed) % 1 + 1) % 1;
            r.position.copy(curve.getPointAt(u));
        });
    }


    /* ------------------------------------------------------------------
       BATTERY GROUP (body + terminals + polarity labels)
    ------------------------------------------------------------------ */
    function makeBattery(pos = { x: -3.4, y: -0.6, z: 0 }) {
        const g = new THREE.Group();
        const body = new THREE.Mesh(
            new THREE.BoxGeometry(0.55, 0.95, 0.4),
            new THREE.MeshStandardMaterial({ color: C.batteryBody, roughness: 0.5, metalness: 0.35 })
        );
        g.add(body);

        const plusCap = new THREE.Mesh(
            new THREE.CylinderGeometry(0.08, 0.08, 0.26, 14),
            new THREE.MeshStandardMaterial({ color: C.terminalPlus, roughness: 0.3, metalness: 0.7 })
        );
        plusCap.position.set(-0.17, 0.58, 0);
        g.add(plusCap);

        const minusCap = new THREE.Mesh(
            new THREE.CylinderGeometry(0.08, 0.08, 0.26, 14),
            new THREE.MeshStandardMaterial({ color: C.terminalMinus, roughness: 0.3, metalness: 0.7 })
        );
        minusCap.position.set(0.17, 0.58, 0);
        g.add(minusCap);

        const plusLbl = makeLabel("+", "#fbbf24", "rgba(9,13,22,0.92)", "#d97706", 0.42, 0.42);
        plusLbl.position.set(-0.62, 0.85, 0);
        g.add(plusLbl);

        const minusLbl = makeLabel("\u2212", "#cbd5e1", "rgba(9,13,22,0.92)", "#475569", 0.42, 0.42);
        minusLbl.position.set(0.62, 0.85, 0);
        g.add(minusLbl);

        g.position.set(pos.x, pos.y, pos.z);
        return g;
    }

    /* ------------------------------------------------------------------
       LAMP GROUP (glass sphere + screw base) — glow via emissive
    ------------------------------------------------------------------ */
    function makeLamp(x, y, z, glassColor = C.lampGlass) {
        const g = new THREE.Group();

        const glassMat = new THREE.MeshStandardMaterial({
            color: glassColor,
            roughness: 0.25,
            metalness: 0.05,
            emissive: new THREE.Color(C.lampGlow),
            emissiveIntensity: 0
        });
        const glass = new THREE.Mesh(new THREE.SphereGeometry(0.42, 24, 18), glassMat);
        glass.position.y = 0.42;
        g.add(glass);

        const base = new THREE.Mesh(
            new THREE.CylinderGeometry(0.16, 0.2, 0.3, 16),
            new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.35, metalness: 0.75 })
        );
        base.position.y = 0.02;
        g.add(base);

        const light = new THREE.PointLight(C.lampGlow, 0, 4.5);
        light.position.y = 0.5;
        g.add(light);

        g.userData.glass = glass;
        g.userData.glassMaterial = glassMat;
        g.userData.light = light;
        g.position.set(x, y, z);
        return g;
    }


    /* ------------------------------------------------------------------
       KNIFE SWITCH (two posts + rotating lever)
    ------------------------------------------------------------------ */
    function makeSwitch(x, y, z) {
        const g = new THREE.Group();

        const postMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.35, metalness: 0.7 });
        const postA = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 0.3, 12), postMat);
        postA.position.set(-0.55, 0.15, 0);
        g.add(postA);
        const postB = postA.clone();
        postB.position.x = 0.55;
        g.add(postB);

        const leverPivot = new THREE.Group();
        leverPivot.position.set(-0.55, 0.32, 0);
        const lever = new THREE.Mesh(
            new THREE.BoxGeometry(1.1, 0.07, 0.14),
            new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.3, metalness: 0.75 })
        );
        lever.position.x = 0.55;
        leverPivot.add(lever);
        g.add(leverPivot);

        g.userData.pivot = leverPivot;
        g.userData.closed = false;
        g.position.set(x, y, z);
        return g;
    }

    /* ------------------------------------------------------------------
       NICHROME HEATING COIL (helix curve)
    ------------------------------------------------------------------ */
    function makeCoil(x, y, z) {
        const pts = [];
        const turns = 7;
        for (let i = 0; i <= 140; i++) {
            const t = i / 140;
            pts.push(new THREE.Vector3(Math.sin(t * turns * Math.PI * 2) * 0.34, t * 2.4 - 1.2, Math.cos(t * turns * Math.PI * 2) * 0.34));
        }
        const curve = new THREE.CatmullRomCurve3(pts);
        const mat = new THREE.MeshStandardMaterial({
            color: C.nichrome,
            roughness: 0.5,
            metalness: 0.6,
            emissive: new THREE.Color(0xff5a00),
            emissiveIntensity: 0
        });
        const mesh = new THREE.Mesh(new THREE.TubeGeometry(curve, 220, 0.055, 10, false), mat);
        mesh.userData.curve = curve;

        const g = new THREE.Group();
        g.add(mesh);
        g.userData.coilMat = mat;
        g.position.set(x, y, z);
        return g;
    }

    /* ==================================================================
       MAIN SIMULATION CLASS
    ================================================================== */
    class CircuitSimulation {
        constructor(container, type) {
            this.container = container;
            this.type = type;
            this.step = 0;
            this.maxSteps = 2;
            this.playing = true;
            this.time = 0;
            this.isDragging = false;
            this.targetRotation = { x: 0, y: 0 };
            this.currentRotation = { x: 0, y: 0 };
            this.defaultZoom = 8;
            this.zoom = 8;
            this.destroyed = false;
            this.rafId = 0;
            this.cleanupFns = [];
            this.transition = 1;

            const requestedHeight = parseInt(container.getAttribute("data-height") || "340", 10);
            const hAttr = window.matchMedia("(max-width: 600px)").matches
                ? Math.min(requestedHeight, 260)
                : requestedHeight;
            Object.assign(container.style, {
                position: "relative",
                width: "100%",
                borderRadius: "14px",
                overflow: "hidden",
                background: "#0b0e14",
                border: "1.5px solid #292524",
                boxShadow: "0 10px 30px rgba(0,0,0,0.35)",
                margin: "16px 0",
                userSelect: "none",
                touchAction: "pan-y"
            });

            this.canvasWrapper = document.createElement("div");
            this.canvasWrapper.style.width = "100%";
            this.canvasWrapper.style.height = hAttr + "px";
            this.canvasWrapper.style.cursor = "grab";
            container.appendChild(this.canvasWrapper);


            // Control bar (title + case buttons)
            this.ctrlBar = document.createElement("div");
            this.ctrlBar.className = "sj-three-controls";
            Object.assign(this.ctrlBar.style, {
                position: "absolute", top: "10px", left: "10px", right: "10px",
                display: "flex", justifyContent: "space-between", alignItems: "center",
                gap: "8px", pointerEvents: "none"
            });

            this.titleTag = document.createElement("div");
            Object.assign(this.titleTag.style, {
                background: "rgba(9,13,22,0.82)", border: "1px solid #292524",
                padding: "6px 12px", borderRadius: "10px",
                fontSize: "11.5px", fontWeight: "750", color: "#fbbf24",
                display: "flex", alignItems: "center", gap: "6px",
                backdropFilter: "blur(6px)", flexWrap: "wrap"
            });
            this.ctrlBar.appendChild(this.titleTag);

            const btnGroup = document.createElement("div");
            btnGroup.className = "sj-three-buttons";
            btnGroup.style.display = "flex";
            btnGroup.style.alignItems = "center";
            btnGroup.style.gap = "5px";
            btnGroup.style.pointerEvents = "auto";

            this.prevBtn = document.createElement("button");
            this.prevBtn.innerHTML = "\u276E";
            this.prevBtn.title = "Previous Case";
            this.prevBtn.setAttribute("aria-label", "Previous animation case");
            this.styleButton(this.prevBtn);
            this.prevBtn.onclick = () => this.prevStep();
            btnGroup.appendChild(this.prevBtn);

            this.playBtn = document.createElement("button");
            this.playBtn.innerHTML = "\u23F8";
            this.playBtn.title = "Play / Pause";
            this.playBtn.setAttribute("aria-label", "Pause animation");
            this.styleButton(this.playBtn);
            this.playBtn.onclick = () => this.togglePlay();
            btnGroup.appendChild(this.playBtn);

            this.nextBtn = document.createElement("button");
            this.nextBtn.innerHTML = "Next Case \u276F";
            this.nextBtn.title = "Next Case";
            this.nextBtn.setAttribute("aria-label", "Next animation case");
            this.styleButton(this.nextBtn, true);
            this.nextBtn.onclick = () => this.nextStep();
            btnGroup.appendChild(this.nextBtn);

            this.resetBtn = document.createElement("button");
            this.resetBtn.innerHTML = "\u27F2 View";
            this.resetBtn.title = "Reset 3D View";
            this.resetBtn.setAttribute("aria-label", "Reset 3D view");
            this.styleButton(this.resetBtn);
            this.resetBtn.onclick = () => this.resetCamera();
            btnGroup.appendChild(this.resetBtn);

            this.ctrlBar.appendChild(btnGroup);
            container.insertBefore(this.ctrlBar, this.canvasWrapper);

            this.initThree();
            this.setupInteraction();
            this.buildBaseScene();
            this.rebuildDynamicElements();
            this.animate();
        }

        styleButton(btn, isPrimary = false) {
            Object.assign(btn.style, {
                background: isPrimary ? "linear-gradient(135deg, #d97706, #92400e)" : "#1e293b",
                border: isPrimary ? "1px solid #f59e0b" : "1px solid #334155",
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
                btn.style.boxShadow = "0 3px 8px rgba(217,119,6,0.35)";
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

            this.camera = new THREE.PerspectiveCamera(40, w / h, 0.1, 200);
            this.camera.position.set(0, 0.8, this.zoom);
            this.camera.lookAt(0, 0, 0);

            this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            this.renderer.setSize(w, h);
            this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
            this.renderer.outputColorSpace = THREE.SRGBColorSpace;
            this.canvasWrapper.appendChild(this.renderer.domElement);

            const ambient = new THREE.AmbientLight(0xffffff, 0.85);
            this.scene.add(ambient);
            const dirLight = new THREE.DirectionalLight(0xffffff, 1.3);
            dirLight.position.set(6, 10, 8);
            this.scene.add(dirLight);

            this.world = new THREE.Group();
            this.scene.add(this.world);

            this.baseGroup = new THREE.Group();
            this.world.add(this.baseGroup);

            this.dynamicGroup = new THREE.Group();
            this.world.add(this.dynamicGroup);

            this.resizeObserver = new ResizeObserver(() => {
                const nw = this.canvasWrapper.clientWidth;
                const nh = this.canvasWrapper.clientHeight;
                if (nw > 0 && nh > 0) {
                    this.camera.aspect = nw / nh;
                    this.camera.updateProjectionMatrix();
                    this.renderer.setSize(nw, nh);
                }
            });
            this.resizeObserver.observe(this.canvasWrapper);
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

            const onMouseDown = e => onStart(e.clientX, e.clientY);
            const onMouseMove = e => onMove(e.clientX, e.clientY);
            const onMouseUp = () => onEnd();
            el.addEventListener("mousedown", onMouseDown);
            window.addEventListener("mousemove", onMouseMove);
            window.addEventListener("mouseup", onMouseUp);

            const onTouchStart = e => {
                if (e.touches.length === 1) onStart(e.touches[0].clientX, e.touches[0].clientY);
            };
            const onTouchMove = e => {
                if (e.touches.length === 1 && this.isDragging) onMove(e.touches[0].clientX, e.touches[0].clientY);
            };
            const onTouchEnd = () => onEnd();
            el.addEventListener("touchstart", onTouchStart, { passive: true });
            window.addEventListener("touchmove", onTouchMove, { passive: true });
            window.addEventListener("touchend", onTouchEnd);

            const onWheel = e => {
                e.preventDefault();
                this.zoom = Math.max(4.5, Math.min(15.0, this.zoom + e.deltaY * 0.005));
                this.camera.position.z = this.zoom;
            };
            el.addEventListener("wheel", onWheel, { passive: false });

            this.cleanupFns.push(() => {
                el.removeEventListener("mousedown", onMouseDown);
                window.removeEventListener("mousemove", onMouseMove);
                window.removeEventListener("mouseup", onMouseUp);
                el.removeEventListener("touchstart", onTouchStart);
                window.removeEventListener("touchmove", onTouchMove);
                window.removeEventListener("touchend", onTouchEnd);
                el.removeEventListener("wheel", onWheel);
            });
        }


        /* ==================================================================
           SCENE CONSTRUCTION
        ================================================================== */
        clearGroup(g) {
            while (g.children.length > 0) {
                const child = g.children[0];
                g.remove(child);
                child.traverse(node => {
                    if (node.geometry) node.geometry.dispose();
                    if (node.material) {
                        (Array.isArray(node.material) ? node.material : [node.material]).forEach(m => {
                            if (m.map) m.map.dispose();
                            m.dispose();
                        });
                    }
                });
            }
        }

        buildBaseScene() {
            // Everything is built per-step inside rebuildDynamicElements()
            this.maxSteps = {
                "current-flow": 2,
                "ohms-law": 3,
                "resistance-factors": 3,
                "series-parallel": 2,
                "heating-effect": 3
            }[this.type] || 2;
        }

        rebuildDynamicElements() {
            this.clearGroup(this.dynamicGroup);
            this.time = 0;
            this.transition = 0;
            this.swarms = [];
            this.lamps = [];
            this.switches = [];
            this.sparks = null;

            switch (this.type) {
                case "current-flow": this.buildCurrentFlow(); break;
                case "ohms-law": this.buildOhmsLaw(); break;
                case "resistance-factors": this.buildResistanceFactors(); break;
                case "series-parallel": this.buildSeriesParallel(); break;
                case "heating-effect": this.buildHeatingEffect(); break;
            }
            this.updateCaseStatus();
        }

        updateCaseStatus() {
            this.titleTag.setAttribute("aria-live", "polite");
            this.titleTag.dataset.case = `${this.step + 1}/${this.maxSteps}`;
            this.titleTag.title = `Animation case ${this.step + 1} of ${this.maxSteps}. Use Next Case to continue.`;
        }

        /* ---------------- SCENE 1: CURRENT FLOW ---------------- */
        buildCurrentFlow() {
            const closed = this.step === 1;
            this.defaultZoom = 8.2;
            this.zoom = 8.2;

            const loopPts = [
                new THREE.Vector3(-3.57, 0.05, 0),   // battery +
                new THREE.Vector3(-3.65, 1.95, 0),
                new THREE.Vector3(1.5, 1.92, 0),     // passes through lamp
                new THREE.Vector3(3.95, 1.9, 0),
                new THREE.Vector3(3.95, -1.75, 0),
                new THREE.Vector3(0.75, -1.78, 0),   // switch right post
                new THREE.Vector3(-0.35, -1.78, 0),  // switch left post
                new THREE.Vector3(-3.65, -1.72, 0),
                new THREE.Vector3(-3.23, -0.05, 0)   // battery −
            ];
            this.dynamicGroup.add(createFlowPath(loopPts, C.wire, 0.05));

            this.dynamicGroup.add(makeBattery({ x: -3.4, y: -0.62, z: 0 }));

            // Lamp sits on the top wire
            const lamp = makeLamp(1.5, 1.5, 0);
            lamp.userData.target = closed ? 1 : 0;
            this.lamps.push(lamp);
            this.dynamicGroup.add(lamp);

            // Knife switch on the bottom wire
            const sw = makeSwitch(0.2, -1.98, 0);
            sw.userData.closed = closed;
            this.switches.push(sw);
            this.dynamicGroup.add(sw);

            // Electron swarm (visible only when closed)
            const curve = new THREE.CatmullRomCurve3(loopPts);
            const swarm = makeElectronSwarm(curve, 34);
            this.dynamicGroup.add(swarm);
            this.swarms.push({ swarm: swarm, speed: 0.09 });
            swarm.visible = closed;

            // Direction labels
            const eLbl = makeLabel("Electron drift \u2192", "#67e8f9", LABEL_BG, "#0891b2", 2.1, 0.44);
            eLbl.position.set(-1.7, -1.05, 0);
            this.dynamicGroup.add(eLbl);

            const cLbl = makeLabel("Conventional current \u2190 (+ \u2192 \u2212)", "#facc15", LABEL_BG, "#ca8a04", 3.0, 0.46);
            cLbl.position.set(0.4, 2.55, 0);
            this.dynamicGroup.add(cLbl);

            this.titleTag.innerHTML = closed
                ? `<span>CLOSED circuit:</span> <span style="color:#86efac;">current flows — lamp glows!</span> <span style="color:#67e8f9;">electrons drift opposite to conventional current</span>`
                : `<span>OPEN circuit:</span> <span style="color:#f43f5e;">gap in the path ⇒ NO current — lamp stays dark</span> <span style="color:#94a3b8;">(press Next Case to close the switch)</span>`;
        }

        /* ---------------- SCENE 2: OHM'S LAW ---------------- */
        buildOhmsLaw() {
            this.defaultZoom = 7.8;
            this.zoom = 7.8;
            const cells = [1, 2, 4][this.step];
            const speed = [0.035, 0.07, 0.14][this.step];

            const loopPts = [
                new THREE.Vector3(-3.57, 0.05, 0),
                new THREE.Vector3(-3.65, 1.35, 0),
                new THREE.Vector3(3.95, 1.32, 0),
                new THREE.Vector3(3.95, -1.75, 0),
                new THREE.Vector3(-3.65, -1.72, 0),
                new THREE.Vector3(-3.23, -0.05, 0)
            ];
            this.dynamicGroup.add(createFlowPath(loopPts, C.wire, 0.05));
            this.dynamicGroup.add(makeBattery({ x: -3.4, y: -0.62, z: 0 }));

            // Fixed resistor on the top wire
            const resistor = new THREE.Mesh(
                new THREE.CylinderGeometry(0.24, 0.24, 1.0, 20),
                new THREE.MeshStandardMaterial({ color: C.resistor, roughness: 0.55 })
            );
            resistor.rotation.z = Math.PI / 2;
            resistor.position.set(0, 1.33, 0);
            this.dynamicGroup.add(resistor);

            const rLbl = makeLabel("FIXED RESISTOR R", "#fdba74", LABEL_BG, "#c2410c", 2.4, 0.44);
            rLbl.position.set(0, 2.25, 0);
            this.dynamicGroup.add(rLbl);

            // Cell stack visual (1 / 2 / 4 cells)
            for (let i = 0; i < cells; i++) {
                const cell = new THREE.Mesh(
                    new THREE.BoxGeometry(0.42, 0.6, 0.3),
                    new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.5, metalness: 0.3 })
                );
                cell.position.set(1.4 + i * 0.55, -1.15, 0);
                this.dynamicGroup.add(cell);
            }
            const cellLbl = makeLabel(`${cells} CELL${cells > 1 ? "S" : ""}  •  V = ${[1.5, 3, 6][this.step]} V`, "#facc15", LABEL_BG, "#ca8a04", 2.8, 0.42);
            cellLbl.position.set(2.1, -0.45, 0);
            this.dynamicGroup.add(cellLbl);

            // Electron swarm
            const curve = new THREE.CatmullRomCurve3(loopPts);
            const swarm = makeElectronSwarm(curve, 30);
            this.dynamicGroup.add(swarm);
            this.swarms.push({ swarm: swarm, speed: speed });

            const vVal = ["1.5 V", "3 V", "6 V"][this.step];
            const iRel = ["I", "I ×2", "I ×4"][this.step];
            this.titleTag.innerHTML = `<span>${cells} cell${cells > 1 ? "s" : ""}: V = ${vVal}</span> <span style="color:#86efac;">⇒ current ${iRel}</span> <span style="color:#facc15;">V ∝ I (Ohm's law ✓)</span>`;
        }


        resetCamera() {
            this.targetRotation.x = 0;
            this.targetRotation.y = 0;
            this.zoom = this.defaultZoom;
            this.camera.position.set(0, 0.8, this.zoom);
            this.camera.lookAt(0, 0, 0);
        }

        togglePlay() {
            this.playing = !this.playing;
            this.playBtn.setAttribute("aria-label", this.playing ? "Pause animation" : "Play animation");
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


        /* ---------- SCENE 3: RESISTANCE FACTORS ---------- */
        buildResistanceFactors() {
            this.defaultZoom = 7.8; this.zoom = 7.8;
            const colors = [C.copper, C.copper, C.nichrome];
            const labels = ["Length → Resistance (l ∝ R)", "Thickness → Resistance (A ∝ 1/R)", "Material → Resistance (Nichrome > Copper)"];
            const shortLabel = ["Long wire (2× length)", "Thick wire (2× area)", "Copper wire — low ρ"];
            const longLabel  = ["Short wire (l)", "Thin wire (0.5× area)", "Nichrome wire — high ρ"];
            const speeds = [0.08, 0.08, 0.05];
            const yHigh = 1.5, yLow = -1.2;

            let geo1, geo2;
            if (this.step === 0) {
                geo1 = new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-2.25, yHigh, 0), new THREE.Vector3(2.25, yHigh, 0)]), 4, 0.08, 8, false);
                geo2 = new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-1.125, yLow, 0), new THREE.Vector3(1.125, yLow, 0)]), 4, 0.08, 8, false);
            } else if (this.step === 1) {
                geo1 = new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-1.75, yHigh, 0), new THREE.Vector3(1.75, yHigh, 0)]), 4, 0.16, 8, false);
                geo2 = new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-1.75, yLow, 0), new THREE.Vector3(1.75, yLow, 0)]), 4, 0.07, 8, false);
            } else {
                geo1 = new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-1.75, yHigh, 0), new THREE.Vector3(1.75, yHigh, 0)]), 4, 0.08, 8, false);
                geo2 = new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-1.75, yLow, 0), new THREE.Vector3(1.75, yLow, 0)]), 4, 0.08, 8, false);
            }

            const wire1Mat = new THREE.MeshStandardMaterial({color: colors[0], roughness: 0.35, metalness: this.step === 2 ? 0.1 : 0.7});
            this.dynamicGroup.add(new THREE.Mesh(geo1, wire1Mat));
            const wire2Mat = new THREE.MeshStandardMaterial({color: colors[1], roughness: 0.35, metalness: this.step === 2 ? 0.15 : 0.7});
            this.dynamicGroup.add(new THREE.Mesh(geo2, wire2Mat));

            this.dynamicGroup.add(makeBattery({x: -4.0, y: yHigh + 0.3, z: 0}));

            const lblS = makeLabel(shortLabel[this.step], "#fdba74", LABEL_BG, "#c24100", 3.0, 0.42);
            lblS.position.set(0, yHigh + 1.1, 0); this.dynamicGroup.add(lblS);
            const lblL = makeLabel(longLabel[this.step], "#a78bfa", LABEL_BG, "#6b21a8", 3.0, 0.42);
            lblL.position.set(0, yLow - 0.95, 0); this.dynamicGroup.add(lblL);
            const lblT = makeLabel(labels[this.step], "#fbbf24", LABEL_BG, "#92400e", 3.5, 0.46);
            lblT.position.set(0, 3.0, 0); this.dynamicGroup.add(lblT);

            const curve1 = new THREE.CatmullRomCurve3(this.step === 0
                ? [new THREE.Vector3(-2.25, yHigh, 0), new THREE.Vector3(2.25, yHigh, 0)]
                : [new THREE.Vector3(-1.75, yHigh, 0), new THREE.Vector3(1.75, yHigh, 0)]
            );
            const swarm = makeElectronSwarm(curve1, [28, 28, 18][this.step]);
            this.dynamicGroup.add(swarm);
            this.swarms.push({swarm: swarm, speed: speeds[this.step]});

            const resistVals = ["R ∝ l", "R ∝ 1/A", "R = ρl/A"][this.step];
            this.titleTag.innerHTML = `<span style="color:#fbbf24;">${labels[this.step]}</span> <span style="color:#86efac;">${resistVals}</span>`;
        }


        /* ---------- SCENE 4: SERIES & PARALLEL ---------- */
        buildSeriesParallel() {
            this.defaultZoom = 8.6; this.zoom = 8.6;
            const isSeries = this.step === 0;

            const loopPts = [
                new THREE.Vector3(-4.5, 2.2, 0),
                new THREE.Vector3(-4.5, 2.9, 0),
                new THREE.Vector3(-2.2, 2.9, 0),
                new THREE.Vector3(0, 2.9, 0),
                new THREE.Vector3(2.2, 2.9, 0),
                new THREE.Vector3(4.5, 2.9, 0),
                new THREE.Vector3(4.5, -2.9, 0),
                new THREE.Vector3(-4.5, -2.9, 0),
                new THREE.Vector3(-4.5, 2.2, 0)
            ];

            this.dynamicGroup.add(createFlowPath(loopPts, C.wire, 0.05, true, 0xf59e0b));
            this.dynamicGroup.add(makeBattery({x: -4.3, y: 1.5, z: 0}));

            const lampX = [-2.2, 0, 2.2];
            for (let i = 0; i < 3; i++) {
                const lamp = makeLamp(lampX[i],
                    isSeries ? 3.4 : (i === 0 ? 1.3 : (i === 1 ? 3.4 : -1.0)),
                    isSeries ? 0 : (i === 0 ? 1.5 : (i === 1 ? 0 : -1.5))
                );
                lamp.userData.target = 1;
                this.lamps.push(lamp);
                this.dynamicGroup.add(lamp);

                const lbl = makeLabel("L" + (i + 1), "#facc15", LABEL_BG, "#92400e", 1.0, 0.34);
                lbl.position.set(lampX[i],
                    isSeries ? 3.9 : (i === 0 ? 1.3 : (i === 1 ? 3.9 : -0.7)),
                    isSeries ? 0 : (i === 0 ? 1.5 : (i === 1 ? 0 : -1.5))
                );
                this.dynamicGroup.add(lbl);
            }

            if (!isSeries) {
                for (let i = 0; i < 3; i++) {
                    const res = new THREE.Mesh(
                        new THREE.CylinderGeometry(0.14, 0.14, 0.6, 14),
                        new THREE.MeshStandardMaterial({color: C.resistor, roughness: 0.5})
                    );
                    res.position.set(lampX[i], 0.5, [1.5, 0, -1.5][i]);
                    this.dynamicGroup.add(res);
                }
            }

            const vMeter = new THREE.Mesh(
                new THREE.BoxGeometry(0.3, 0.6, 0.25),
                new THREE.MeshStandardMaterial({color: 0x334155, roughness: 0.45, metalness: 0.5})
            );
            vMeter.position.set(3.6, 0.5, 0);
            this.dynamicGroup.add(vMeter);

            const aMeter = new THREE.Mesh(
                new THREE.BoxGeometry(0.3, 0.4, 0.25),
                new THREE.MeshStandardMaterial({color: 0x1e293b, roughness: 0.4, metalness: 0.6})
            );
            aMeter.position.set(-3.4, 2.5, 0);
            this.dynamicGroup.add(aMeter);

            const lblV = makeLabel("V", "#67e8f9", LABEL_BG, "#0891b2", 0.6, 0.3);
            lblV.position.set(3.6, 1.25, 0);
            this.dynamicGroup.add(lblV);

            const lblA = makeLabel("A", "#fbbf24", LABEL_BG, "#92400e", 0.6, 0.3);
            lblA.position.set(-3.4, 3.1, 0);
            this.dynamicGroup.add(lblA);

            const curve = new THREE.CatmullRomCurve3(loopPts);
            const swarm = makeElectronSwarm(curve, 36);
            this.dynamicGroup.add(swarm);
            this.swarms.push({swarm: swarm, speed: isSeries ? 0.07 : 0.09});

            const req = isSeries ? "SERIES: R TOTAL ADDS" : "PARALLEL: CURRENT DIVIDES";
            this.titleTag.innerHTML = `<span style="color:#fbbf24;">${isSeries ? "SERIES" : "PARALLEL"} combination</span> <span style="color:#86efac;">${req}</span>`;
        }


        /* ---------- SCENE 5: HEATING EFFECT ---------- */
        buildHeatingEffect() {
            this.defaultZoom = 7.8; this.zoom = 7.8;

            this.dynamicGroup.add(makeBattery({x: -3.8, y: 0, z: 0}));

            const pts = [
                new THREE.Vector3(-3.3, 0.3, 0), new THREE.Vector3(-3.3, 2.0, 0),
                new THREE.Vector3(3.3, 2.0, 0), new THREE.Vector3(3.3, -2.0, 0),
                new THREE.Vector3(-3.3, -2.0, 0), new THREE.Vector3(-3.3, 0.3, 0)
            ];
            this.dynamicGroup.add(createFlowPath(pts, C.wire, 0.05));

            const coil = makeCoil(-3.3, 0.3, 0);
            coil.userData.coilMat.emissiveIntensity = [0, 1, 0.85][this.step];
            this.dynamicGroup.add(coil);

            const heatGroup = new THREE.Group();
            const heatMat = new THREE.MeshBasicMaterial({color: 0xff7a00, transparent: true, opacity: 0.35});
            for (let i = 0; i < 8; i++) {
                const cone = new THREE.Mesh(new THREE.ConeGeometry(0.3 + i * 0.12, 0.8 + i * 0.4, 8), heatMat);
                cone.rotation.z = (i / 8) * Math.PI * 2;
                cone.position.set(0, 0.6 + i * 0.3, 0);
                heatGroup.add(cone);
            }
            heatGroup.position.set(-3.3, 0.6, 0);
            this.dynamicGroup.add(heatGroup);
            this.heatGroup = heatGroup;

            const tempLabels = ["Room temp — no glow", "Heating up — warm glow", "Hot — bright orange glow"];
            const lblTemp = makeLabel(tempLabels[this.step], "#fdba74", LABEL_BG, "#c2410c", 2.6, 0.42);
            lblTemp.position.set(-3.0, 3.0, 0);
            this.dynamicGroup.add(lblTemp);

            const formulaLabels = ["H = I²Rt = 0 (no current)", "H = I²Rt → coil heats up", "H = I²Rt → maximum heating!"];
            const lblFormula = makeLabel(formulaLabels[this.step], "#67e8f9", LABEL_BG, "#0891b2", 2.6, 0.44);
            lblFormula.position.set(0, -2.8, 0);
            this.dynamicGroup.add(lblFormula);

            const curve = new THREE.CatmullRomCurve3(pts);
            const swarm = makeElectronSwarm(curve, 28);
            this.dynamicGroup.add(swarm);
            this.swarms.push({swarm: swarm, speed: [0, 0.09, 0.14][this.step]});
            swarm.visible = this.step > 0;

            this.titleTag.innerHTML = `<span style="color:#fbbf24;">Joule Heating: H = I²Rt</span> <span style="color:#86efac;">Step ${this.step + 1}/3</span>`;
        }


        /* ---------- ANIMATION LOOP ---------- */
        updateElectronSwarms() {
            const t = this.time;
            this.swarms.forEach(s => {
                placeElectronSwarm(s.swarm, s.speed * t, s.speed);
            });
        }

        updateLamps() {
            this.lamps.forEach(l => {
                if (this.playing) {
                    l.userData.pulse = (l.userData.pulse || 0) + 0.02;
                }
                const s = 0.85 + 0.15 * Math.sin(l.userData.pulse || 0);
                l.userData.glass.scale.set(s, s, s);
                const target = l.userData.target || 0;
                const pulse = 0.5 + 0.3 * Math.sin((l.userData.pulse || 0) * 2);
                const glow = target * pulse;
                l.userData.glassMaterial.emissiveIntensity = glow * 2.4;
                l.userData.light.intensity = glow * 3.2;
                l.userData.light.distance = target > 0 ? 5.5 : 0;
            });
        }

        updateSwitches() {
            this.switches.forEach(sw => {
                if (sw.userData.pivot) {
                    const target = sw.userData.closed ? 0.6 : -0.65;
                    sw.userData.pivot.rotation.z += (target - sw.userData.pivot.rotation.z) * 0.08;
                }
            });
        }

        animate() {
            const render = () => {
                if (this.destroyed) return;
                this.rafId = requestAnimationFrame(render);
                if (this.playing) {
                    this.time += 0.016;
                }
                this.updateElectronSwarms();
                this.updateLamps();
                this.updateSwitches();
                this.transition = Math.min(1, this.transition + 0.045);
                const ease = this.transition * this.transition * (3 - 2 * this.transition);
                this.dynamicGroup.scale.setScalar(0.96 + ease * 0.04);

                if (this.heatGroup && this.playing) {
                    const cones = this.heatGroup.children;
                    for (let i = 0; i < cones.length; i++) {
                        const p = (this.time + i * 0.3) % 1;
                        cones[i].scale.setScalar(1 + p * 0.3);
                        cones[i].material.opacity = Math.max(0.1, 0.35 * Math.sin(p * Math.PI));
                    }
                }

                this.renderer.render(this.scene, this.camera);
            };
            render();
        }

        destroy() {
            if (this.destroyed) return;
            this.destroyed = true;
            cancelAnimationFrame(this.rafId);
            this.cleanupFns.forEach(cleanup => cleanup());
            this.cleanupFns = [];
            if (this.resizeObserver) this.resizeObserver.disconnect();
            this.clearGroup(this.world);
            if (this.renderer) {
                this.renderer.dispose();
                this.renderer.domElement.remove();
            }
        }
    }


    /* ---------- AUTO-INITIALIZE ---------- */
    function initAll() {
        const containers = document.querySelectorAll('[data-three-anim]');
        containers.forEach(el => {
            if (el.__circuitSimulation) return;
            const type = el.getAttribute("data-three-anim");
            try {
                el.__circuitSimulation = new CircuitSimulation(el, type);
            } catch (error) {
                console.error(`SJMaths Three.js: failed to initialize ${type}.`, error);
                el.textContent = "This interactive animation could not be loaded on this device.";
            }
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initAll);
    } else {
        initAll();
    }

})();
