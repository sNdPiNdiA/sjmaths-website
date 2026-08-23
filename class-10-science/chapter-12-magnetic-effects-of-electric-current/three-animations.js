/* ============================================================
   SJMaths — Chapter 12 Three.js Visual Physics Engine
   Magnetic Effects of Electric Current
   Paste as: three-animations.js
   Requires: Three.js r160+
============================================================ */

(() => {
    "use strict";

    if (!window.THREE) {
        console.error("SJMaths Three.js: THREE is not loaded.");
        return;
    }

    const THREE = window.THREE;
    const instances = {};
    const TAU = Math.PI * 2;

    const palette = {
        bg: 0x08111f,
        grid: 0x1e293b,
        field: 0xf59e0b,
        field2: 0xff7a59,
        current: 0xe5483f,
        wire: 0xcbd5e1,
        north: 0xef4444,
        south: 0x38bdf8,
        white: 0xf8fafc,
        force: 0xf97316,
        green: 0x34d399,
        gold: 0xfacc15
    };

    /* =========================================================
       RENDERER
    ========================================================= */

    function rendererFor(el) {
        const r = new THREE.WebGLRenderer({
            antialias: true,
            alpha: false
        });

        r.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
        r.setClearColor(palette.bg, 1);
        r.outputColorSpace = THREE.SRGBColorSpace;

        el.innerHTML = "";
        el.style.position = "relative";
        el.style.overflow = "hidden";
        el.appendChild(r.domElement);

        return r;
    }

    function addLegend(el, items) {
        const legend = document.createElement("div");
        legend.className = "anim-legend";
        items.forEach(item => {
            const chip = document.createElement("span");
            chip.className = item[0];
            chip.textContent = item[1];
            legend.appendChild(chip);
        });
        el.appendChild(legend);
    }

    function resize(state) {
        const w = Math.max(280, state.el.clientWidth);
        const h = Math.max(
            260,
            state.el.clientHeight || Number(state.el.dataset.height) || 360
        );

        state.renderer.setSize(w, h, false);

        state.camera.aspect = w / h;
        state.camera.updateProjectionMatrix();
    }

    /* =========================================================
       BASIC SCENE
    ========================================================= */

    function basicScene(el) {
        const scene = new THREE.Scene();

        scene.fog = new THREE.Fog(
            palette.bg,
            8,
            24
        );

        const camera = new THREE.PerspectiveCamera(
            42,
            1,
            0.1,
            60
        );

        camera.position.set(
            0,
            2.4,
            8
        );

        const renderer = rendererFor(el);

        /* Lighting */

        const ambient =
            new THREE.AmbientLight(
                0xffffff,
                1.35
            );

        scene.add(ambient);

        const key =
            new THREE.DirectionalLight(
                0xffffff,
                2.2
            );

        key.position.set(
            5,
            7,
            8
        );

        scene.add(key);

        const rim =
            new THREE.PointLight(
                palette.field,
                2.2,
                15
            );

        rim.position.set(
            -4,
            3,
            4
        );

        scene.add(rim);

        const state = {
            el,
            scene,
            camera,
            renderer,

            paused: false,
            direction: 1,

            yaw: 0,
            pitch: 0,

            dragging: false,
            px: 0,
            py: 0,

            zoom: 8,

            clock: new THREE.Clock(),
            lastTime: performance.now(),

            objects: []
        };

        addDragCamera(state);

        window.addEventListener(
            "resize",
            () => resize(state),
            { passive: true }
        );

        resize(state);

        state.resizeObserver = new ResizeObserver(() => resize(state));
        state.resizeObserver.observe(el);

        return state;
    }

    /* =========================================================
       DRAG + ZOOM CAMERA
    ========================================================= */

    function addDragCamera(state) {

        const canvas =
            state.renderer.domElement;

        canvas.style.touchAction = "none";
        canvas.style.cursor = "grab";

        canvas.addEventListener(
            "pointerdown",
            e => {

                state.dragging = true;

                state.px = e.clientX;
                state.py = e.clientY;

                canvas.style.cursor = "grabbing";

                canvas.setPointerCapture?.(
                    e.pointerId
                );
            }
        );

        canvas.addEventListener(
            "pointermove",
            e => {

                if (!state.dragging) return;

                const dx =
                    e.clientX - state.px;

                const dy =
                    e.clientY - state.py;

                state.px = e.clientX;
                state.py = e.clientY;

                state.yaw += dx * 0.008;

                state.pitch = Math.max(
                    -1.15,
                    Math.min(
                        1.15,
                        state.pitch + dy * 0.006
                    )
                );
            }
        );

        const release = () => {
            state.dragging = false;
            canvas.style.cursor = "grab";
        };

        canvas.addEventListener(
            "pointerup",
            release
        );

        canvas.addEventListener(
            "pointercancel",
            release
        );

        canvas.addEventListener(
            "wheel",
            e => {

                e.preventDefault();

                state.zoom *=
                    e.deltaY > 0
                        ? 1.08
                        : 0.93;

                state.zoom = Math.max(
                    4.2,
                    Math.min(
                        14,
                        state.zoom
                    )
                );

            },
            { passive: false }
        );
    }

    function cameraOrbit(
        state,
        target,
        radius = state.zoom
    ) {

        const cp =
            Math.cos(state.pitch);

        state.camera.position.set(
            target.x +
            Math.sin(state.yaw) *
            cp *
            radius,

            target.y +
            Math.sin(state.pitch) *
            radius,

            target.z +
            Math.cos(state.yaw) *
            cp *
            radius
        );

        state.camera.lookAt(target);
    }

    /* =========================================================
       MATERIAL HELPERS
    ========================================================= */

    function glowMaterial(
        color,
        opacity = 1
    ) {

        return new THREE.MeshBasicMaterial({
            color,

            transparent:
                opacity < 1,

            opacity,

            blending:
                opacity < 1
                    ? THREE.AdditiveBlending
                    : THREE.NormalBlending,

            depthWrite:
                opacity >= 1
        });
    }

    function tube(
        points,
        color,
        radius = 0.018,
        opacity = 0.8
    ) {

        const curve =
            new THREE.CatmullRomCurve3(
                points
            );

        const geometry =
            new THREE.TubeGeometry(
                curve,
                Math.max(
                    32,
                    points.length * 10
                ),
                radius,
                8,
                false
            );

        return new THREE.Mesh(
            geometry,
            glowMaterial(
                color,
                opacity
            )
        );
    }

    function arrow(
        start,
        end,
        color,
        head = 0.09
    ) {

        const direction =
            new THREE.Vector3()
                .subVectors(
                    end,
                    start
                )
                .normalize();

        const length =
            start.distanceTo(end);

        return new THREE.ArrowHelper(
            direction,
            start,
            length,
            color,
            head * 1.8,
            head
        );
    }

    function glowSphere(
        position,
        color,
        size = 0.06
    ) {

        const mesh =
            new THREE.Mesh(
                new THREE.SphereGeometry(
                    size,
                    12,
                    12
                ),
                glowMaterial(color)
            );

        mesh.position.copy(
            position
        );

        return mesh;
    }

    /* =========================================================
       1. MAGNETIC FIELD — STRAIGHT CURRENT CARRYING CONDUCTOR
    ========================================================= */

    function magneticWire(el) {

        const s =
            basicScene(el);
        addLegend(el, [["current", "● CURRENT"], ["field", "◎ FIELD LINES"]]);

        const group =
            new THREE.Group();

        s.scene.add(group);

        /* Wire */

        const wire =
            new THREE.Mesh(
                new THREE.CylinderGeometry(
                    0.09,
                    0.09,
                    5.2,
                    24
                ),
                new THREE.MeshStandardMaterial({
                    color:
                        palette.wire,
                    metalness:
                        0.75,
                    roughness:
                        0.22
                })
            );

        wire.rotation.z =
            Math.PI / 2;

        group.add(wire);

        /* Current arrow */

        const currentArrow =
            arrow(
                new THREE.Vector3(
                    -2.4,
                    0,
                    0
                ),

                new THREE.Vector3(
                    2.4,
                    0,
                    0
                ),

                palette.current,
                0.14
            );

        group.add(currentArrow);

        /* Current particles */

        const particles =
            new THREE.Group();

        group.add(particles);

        for (
            let i = 0;
            i < 18;
            i++
        ) {

            const p =
                glowSphere(
                    new THREE.Vector3(
                        -2.3 +
                        (i / 17) * 4.6,
                        0,
                        0
                    ),
                    palette.current,
                    0.055
                );

            particles.add(p);
        }

        /* Magnetic field rings */

        const rings = [];
        const fieldArrows = [];

        for (
            let r = 0.55;
            r <= 2.4;
            r += 0.38
        ) {

            const pts = [];

            for (
                let i = 0;
                i <= 100;
                i++
            ) {

                const a =
                    (i / 100) *
                    TAU;

                pts.push(
                    new THREE.Vector3(
                        0,
                        Math.cos(a) * r,
                        Math.sin(a) * r
                    )
                );
            }

            const ring =
                tube(
                    pts,
                    palette.field,
                    0.018,
                    0.65
                );

            group.add(ring);

            rings.push(ring);

            const a =
                Math.PI * 0.55;

            const p1 =
                new THREE.Vector3(
                    0,
                    Math.cos(a) * r,
                    Math.sin(a) * r
                );

            const p2 =
                new THREE.Vector3(
                    0,
                    Math.cos(a + 0.18) * r,
                    Math.sin(a + 0.18) * r
                );

            const fieldArrow = arrow(
                    p1,
                    p2,
                    palette.field,
                    0.08
                );
            group.add(fieldArrow);
            fieldArrows.push({ arrow: fieldArrow, start: p1, end: p2 });
        }

        /* Labels made as 3D sprites */

        const labelGroup =
            new THREE.Group();

        group.add(labelGroup);

        /* Update */

        s.update = dt => {

            if (!s.paused) {

                particles.children.forEach(
                    (p, i) => {

                        const rawX =
                            ((i / 18) * 5 +
                                s.clock.elapsedTime *
                                1.4 *
                                s.direction) % 5;
                        const x = (rawX + 5) % 5;

                        p.position.x =
                            -2.5 + x;
                    }
                );

                // The magnetic field around a straight conductor is stationary;
                // only the charge markers move along the conductor.
            }

            cameraOrbit(
                s,
                new THREE.Vector3(
                    0,
                    0,
                    0
                ),
                8
            );
        };

        s.reverse = () => {

            s.direction *= -1;

            currentArrow.setDirection(
                new THREE.Vector3(
                    s.direction,
                    0,
                    0
                )
            );
            fieldArrows.forEach(item => {
                const start = item.start.clone();
                const end = item.end.clone();
                if (s.direction < 0) {
                    item.arrow.position.copy(end);
                    item.arrow.setDirection(start.sub(end).normalize());
                    item.arrow.setLength(item.start.distanceTo(item.end), 0.144, 0.08);
                } else {
                    item.arrow.position.copy(start);
                    item.arrow.setDirection(end.sub(start).normalize());
                    item.arrow.setLength(item.start.distanceTo(item.end), 0.144, 0.08);
                }
            });
        };

        s.toggle = () => {
            s.paused =
                !s.paused;
        };

        return s;
    }

    /* =========================================================
       2. SOLENOID
    ========================================================= */

    function solenoid(el) {

        const s =
            basicScene(el);
        addLegend(el, [["current", "● COIL CURRENT"], ["field", "→ UNIFORM FIELD"]]);

        const group =
            new THREE.Group();

        s.scene.add(group);

        /* Solenoid coil */

        const coil =
            new THREE.Group();

        group.add(coil);

        const turns = 22;
        const length = 4.8;
        const radius = 1.25;

        for (
            let i = 0;
            i < turns;
            i++
        ) {

            const x =
                -length / 2 +
                i *
                (length /
                    (turns - 1));

            const pts = [];

            for (
                let j = 0;
                j <= 80;
                j++
            ) {

                const a =
                    (j / 80) *
                    TAU;

                pts.push(
                    new THREE.Vector3(
                        x,
                        Math.cos(a) *
                        radius,
                        Math.sin(a) *
                        radius
                    )
                );
            }

            coil.add(
                tube(
                    pts,
                    palette.current,
                    0.028,
                    0.95
                )
            );
        }

        /* Field inside solenoid */

        const fieldLines =
            new THREE.Group();
        const fieldArrows = [];

        group.add(fieldLines);

        for (
            let y = -0.9;
            y <= 0.9;
            y += 0.36
        ) {

            for (
                let z = -0.55;
                z <= 0.55;
                z += 0.55
            ) {

                const pts = [
                    new THREE.Vector3(
                        -2.3,
                        y,
                        z
                    ),

                    new THREE.Vector3(
                        2.3,
                        y,
                        z
                    )
                ];

                fieldLines.add(
                    tube(
                        pts,
                        palette.field,
                        0.022,
                        0.82
                    )
                );

                const insideArrow = arrow(
                        new THREE.Vector3(
                            1.45,
                            y,
                            z
                        ),

                        new THREE.Vector3(
                            2.1,
                            y,
                            z
                        ),

                        palette.field,
                        0.08
                    );
                insideArrow.userData.baseDirection = new THREE.Vector3(1, 0, 0);
                fieldLines.add(insideArrow);
                fieldArrows.push(insideArrow);
            }
        }

        /* External return field */

        for (
            let r = 1.7;
            r <= 2.8;
            r += 0.42
        ) {

            const pts = [];

            for (
                let i = 0;
                i <= 80;
                i++
            ) {

                const t =
                    (i / 80) *
                    Math.PI;

                pts.push(
                    new THREE.Vector3(
                        Math.cos(t) *
                        2.55,

                        Math.sin(t) *
                        r *
                        0.78,

                        0
                    )
                );
            }

            fieldLines.add(
                tube(
                    pts,
                    palette.field2,
                    0.018,
                    0.55
                )
            );
        }

        /* Direction arrows at ends */

        const leftReturnArrow = arrow(
                new THREE.Vector3(
                    -2.6,
                    0,
                    0
                ),

                new THREE.Vector3(
                    -3.3,
                    0,
                    0
                ),

                palette.field2,
                0.1
            );
        leftReturnArrow.userData.baseDirection = new THREE.Vector3(-1, 0, 0);
        group.add(leftReturnArrow);
        fieldArrows.push(leftReturnArrow);

        const rightReturnArrow = arrow(
                new THREE.Vector3(
                    2.6,
                    0,
                    0
                ),

                new THREE.Vector3(
                    3.3,
                    0,
                    0
                ),

                palette.field2,
                0.1
            );
        rightReturnArrow.userData.baseDirection = new THREE.Vector3(1, 0, 0);
        group.add(rightReturnArrow);
        fieldArrows.push(rightReturnArrow);

        s.update = dt => {

            if (!s.paused) {

                // A solenoid's field does not rotate during steady current.
                // Reverse changes the current/field direction, not the geometry.
            }

            cameraOrbit(
                s,
                new THREE.Vector3(
                    0,
                    0,
                    0
                ),
                7.8
            );
        };

        s.reverse = () => {
            s.direction *= -1;
            fieldArrows.forEach(fieldArrow => {
                fieldArrow.setDirection(fieldArrow.userData.baseDirection.clone().multiplyScalar(s.direction));
            });
        };

        s.toggle = () => {
            s.paused =
                !s.paused;
        };

        return s;
    }

    /* =========================================================
       3. ELECTRIC MOTOR
    ========================================================= */

    function motor(el) {

        const s =
            basicScene(el);
        addLegend(el, [["current", "● CURRENT"], ["field", "◎ MAGNETIC FIELD"], ["force", "↻ TORQUE"]]);

        const root =
            new THREE.Group();

        s.scene.add(root);

        /* N pole */

        const N =
            new THREE.Mesh(
                new THREE.BoxGeometry(
                    1.05,
                    2.8,
                    1.1
                ),

                new THREE.MeshStandardMaterial({
                    color:
                        palette.north,
                    roughness:
                        0.35
                })
            );

        N.position.x = -2.8;

        root.add(N);

        /* S pole */

        const S =
            new THREE.Mesh(
                new THREE.BoxGeometry(
                    1.05,
                    2.8,
                    1.1
                ),

                new THREE.MeshStandardMaterial({
                    color:
                        palette.south,
                    roughness:
                        0.35
                })
            );

        S.position.x = 2.8;

        root.add(S);

        /* Magnetic field */

        for (
            let y = -1;
            y <= 1;
            y += 0.5
        ) {

            root.add(
                arrow(
                    new THREE.Vector3(
                        -2.15,
                        y,
                        0
                    ),

                    new THREE.Vector3(
                        2.15,
                        y,
                        0
                    ),

                    palette.field,
                    0.08
                )
            );
        }

        /* Rotating coil */

        const rotating =
            new THREE.Group();

        root.add(rotating);

        const frameMat =
            new THREE.MeshStandardMaterial({
                color:
                    palette.current,
                metalness:
                    0.35,
                roughness:
                    0.28
            });

        const bars = [

            [
                new THREE.Vector3(
                    -1.65,
                    1.05,
                    0
                ),

                new THREE.Vector3(
                    1.65,
                    1.05,
                    0
                )
            ],

            [
                new THREE.Vector3(
                    -1.65,
                    -1.05,
                    0
                ),

                new THREE.Vector3(
                    1.65,
                    -1.05,
                    0
                )
            ],

            [
                new THREE.Vector3(
                    -1.65,
                    -1.05,
                    0
                ),

                new THREE.Vector3(
                    -1.65,
                    1.05,
                    0
                )
            ],

            [
                new THREE.Vector3(
                    1.65,
                    -1.05,
                    0
                ),

                new THREE.Vector3(
                    1.65,
                    1.05,
                    0
                )
            ]
        ];

        bars.forEach(
            ([a, b]) => {

                const mid =
                    a.clone()
                        .add(b)
                        .multiplyScalar(
                            0.5
                        );

                const len =
                    a.distanceTo(b);

                const geometry =
                    new THREE.BoxGeometry(
                        len,
                        0.08,
                        0.08
                    );

                const mesh =
                    new THREE.Mesh(
                        geometry,
                        frameMat
                    );

                mesh.position.copy(mid);

                mesh.rotation.z =
                    Math.atan2(
                        b.y - a.y,
                        b.x - a.x
                    );

                rotating.add(
                    mesh
                );
            }
        );

        /* Axle */

        const axle =
            new THREE.Mesh(
                new THREE.CylinderGeometry(
                    0.09,
                    0.09,
                    4.3,
                    20
                ),

                new THREE.MeshStandardMaterial({
                    color:
                        palette.wire,
                    metalness:
                        0.85
                })
            );

        axle.rotation.z =
            Math.PI / 2;

        rotating.add(axle);

        /* Split ring */

        const comm =
            new THREE.Mesh(
                new THREE.TorusGeometry(
                    0.42,
                    0.09,
                    12,
                    40
                ),

                glowMaterial(
                    palette.gold
                )
            );

        comm.rotation.y =
            Math.PI / 2;

        comm.position.x =
            1.95;

        rotating.add(comm);

        /* Brushes */

        const brushMat =
            new THREE.MeshStandardMaterial({
                color:
                    palette.wire,
                metalness:
                    0.3
            });

        const brush1 =
            new THREE.Mesh(
                new THREE.BoxGeometry(
                    0.16,
                    0.4,
                    0.25
                ),
                brushMat
            );

        brush1.position.set(
            1.95,
            0.48,
            0
        );

        root.add(
            brush1
        );

        const brush2 =
            brush1.clone();

        brush2.position.y =
            -0.48;

        root.add(
            brush2
        );

        /* Force arrows */

        const forceArrows = [];
        const leftForce = arrow(
                new THREE.Vector3(
                    -1.65,
                    0.2,
                    0
                ),

                new THREE.Vector3(
                    -1.65,
                    -0.7,
                    0
                ),

                palette.force,
                0.1
            );
        leftForce.userData.baseDirection = new THREE.Vector3(0, -1, 0);
        root.add(leftForce);
        forceArrows.push(leftForce);

        const rightForce = arrow(
                new THREE.Vector3(
                    1.65,
                    -0.2,
                    0
                ),

                new THREE.Vector3(
                    1.65,
                    0.7,
                    0
                ),

                palette.force,
                0.1
            );
        rightForce.userData.baseDirection = new THREE.Vector3(0, 1, 0);
        root.add(rightForce);
        forceArrows.push(rightForce);

        s.update = dt => {

            if (!s.paused) {

                rotating.rotation.y +=
                    dt *
                    1.15 *
                    s.direction;
            }

            cameraOrbit(
                s,
                new THREE.Vector3(
                    0,
                    0,
                    0
                ),
                8
            );
        };

        s.reverse = () => {
            s.direction *= -1;
            forceArrows.forEach(forceArrow => {
                forceArrow.setDirection(forceArrow.userData.baseDirection.clone().multiplyScalar(s.direction));
            });
        };

        s.toggle = () => {
            s.paused =
                !s.paused;
        };

        return s;
    }

    /* =========================================================
       4. AC GENERATOR
    ========================================================= */

    function generator(el) {

        const s =
            basicScene(el);
        addLegend(el, [["field", "◎ MAGNETIC FIELD"], ["force", "↻ MOTION"], ["induced", "⚡ INDUCED CURRENT"]]);

        const root =
            new THREE.Group();

        s.scene.add(root);

        /* N pole */

        const N =
            new THREE.Mesh(
                new THREE.BoxGeometry(
                    0.9,
                    2.6,
                    1.2
                ),

                new THREE.MeshStandardMaterial({
                    color:
                        palette.north
                })
            );

        N.position.x =
            -2.65;

        root.add(N);

        /* S pole */

        const S =
            new THREE.Mesh(
                new THREE.BoxGeometry(
                    0.9,
                    2.6,
                    1.2
                ),

                new THREE.MeshStandardMaterial({
                    color:
                        palette.south
                })
            );

        S.position.x =
            2.65;

        root.add(S);

        /* Magnetic field */

        for (
            let y = -1;
            y <= 1;
            y += 0.5
        ) {

            root.add(
                arrow(
                    new THREE.Vector3(
                        -2.1,
                        y,
                        0
                    ),

                    new THREE.Vector3(
                        2.1,
                        y,
                        0
                    ),

                    palette.field,
                    0.07
                )
            );
        }

        /* Rotor */

        const rotor =
            new THREE.Group();

        root.add(rotor);

        const rotorMat =
            new THREE.MeshStandardMaterial({
                color:
                    palette.current,
                metalness:
                    0.4,
                roughness:
                    0.3
            });

        const pts = [

            new THREE.Vector3(
                -1.55,
                -1,
                0
            ),

            new THREE.Vector3(
                1.55,
                -1,
                0
            ),

            new THREE.Vector3(
                1.55,
                1,
                0
            ),

            new THREE.Vector3(
                -1.55,
                1,
                0
            )
        ];

        for (
            let i = 0;
            i < 4;
            i++
        ) {

            const a = pts[i];

            const b =
                pts[
                (i + 1) % 4
                ];

            const mid =
                a.clone()
                    .add(b)
                    .multiplyScalar(
                        0.5
                    );

            const len =
                a.distanceTo(b);

            const geometry =
                new THREE.BoxGeometry(
                    len,
                    0.07,
                    0.07
                );

            const mesh =
                new THREE.Mesh(
                    geometry,
                    rotorMat
                );

            mesh.position.copy(
                mid
            );

            mesh.rotation.z =
                Math.atan2(
                    b.y - a.y,
                    b.x - a.x
                );

            rotor.add(mesh);
        }

        /* Shaft */

        const shaft =
            new THREE.Mesh(
                new THREE.CylinderGeometry(
                    0.09,
                    0.09,
                    4.2,
                    18
                ),

                new THREE.MeshStandardMaterial({
                    color:
                        palette.wire,
                    metalness:
                        0.85
                })
            );

        shaft.rotation.z =
            Math.PI / 2;

        rotor.add(shaft);

        /* Slip rings */

        for (
            const x of [1.75, 2.05]
        ) {

            const ring =
                new THREE.Mesh(
                    new THREE.TorusGeometry(
                        0.3,
                        0.075,
                        12,
                        36
                    ),

                    glowMaterial(
                        palette.field2
                    )
                );

            ring.rotation.y =
                Math.PI / 2;

            ring.position.x =
                x;

            rotor.add(ring);
        }

        /* Output waveform */

        const wavePts = [];

        for (
            let i = 0;
            i <= 120;
            i++
        ) {

            const x =
                -2.2 +
                (i / 120) *
                4.4;

            const y =
                Math.sin(
                    (i / 120) *
                    TAU *
                    1.7
                ) *
                0.42;

            wavePts.push(
                new THREE.Vector3(
                    x,
                    y,
                    -1.75
                )
            );
        }

        const wave =
            tube(
                wavePts,
                palette.green,
                0.035,
                1
            );

        root.add(wave);

        s.update = dt => {

            if (!s.paused) {

                rotor.rotation.y +=
                    dt *
                    1.0 *
                    s.direction;
            }

            const t =
                s.clock.elapsedTime;

            wave.position.y =
                Math.sin(
                    t * 1.8 * s.direction
                ) *
                0.08;

            cameraOrbit(
                s,
                new THREE.Vector3(
                    0,
                    0,
                    0
                ),
                8.2
            );
        };

        s.reverse = () => {
            s.direction *= -1;
        };

        s.toggle = () => {
            s.paused =
                !s.paused;
        };

        return s;
    }

    /* =========================================================
       AUTO INITIALIZATION
    ========================================================= */

    function create(
        name,
        factory
    ) {

        document
            .querySelectorAll(
                `[data-three-animation="${name}"]`
            )
            .forEach(
                el => {

                    const instance =
                        factory(el);

                    instances[
                        name
                    ] = instance;
                }
            );
    }

    create(
        "magnetic-wire",
        magneticWire
    );

    create(
        "solenoid",
        solenoid
    );

    create(
        "motor",
        motor
    );

    create(
        "generator",
        generator
    );

    /* =========================================================
       PUBLIC CONTROLS
    ========================================================= */

    window.SJThree = {

        toggle(name) {

            if (
                instances[name]
            ) {
                instances[
                    name
                ].toggle();
            }
        },

        reverse(name) {

            if (
                instances[name]
            ) {
                instances[
                    name
                ].reverse();
            }
        }
    };

    // Backward-compatible bridge for the inline controls in Chapter 12 HTML.
    window.threeControl = function (name, action) {
        if (!window.SJThree || !window.SJThree[action]) return;
        window.SJThree[action](name);
    };

    /* =========================================================
       GLOBAL ANIMATION LOOP
    ========================================================= */

    function animate() {

        requestAnimationFrame(
            animate
        );

        const now =
            performance.now();

        Object
            .values(instances)
            .forEach(
                state => {

                    const dt =
                        Math.min(
                            0.04,
                            (now -
                                (
                                    state.lastTime ||
                                    now - 16
                                )) /
                            1000
                        );

                    state.lastTime =
                        now;

                    if (
                        state.update
                    ) {
                        state.update(dt);
                    }

                    state.renderer.render(
                        state.scene,
                        state.camera
                    );
                }
            );
    }

    animate();

})();
