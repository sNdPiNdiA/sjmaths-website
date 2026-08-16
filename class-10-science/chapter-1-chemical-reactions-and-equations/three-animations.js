/*
=========================================================
SJMaths — Class 10 Science
Chapter 1: Chemical Reactions and Equations

TEACHING-FOCUSED THREE.JS SIMULATIONS

Scenes:
1. reaction
2. balance
3. combination
4. decomposition
5. displacement
6. double
7. energy
8. redox
9. corrosion
10. rancidity

Requires:
Three.js r180+ loaded globally as window.THREE

Example:
<div data-three-animation="reaction"></div>
=========================================================
*/

(() => {
    "use strict";

    if (typeof THREE === "undefined") {
        console.error(
            "SJMaths Three.js animations: THREE is not loaded."
        );
        return;
    }

    /* =====================================================
       COLOURS
    ===================================================== */

    const C = {
        red: 0xe5483f,
        darkRed: 0xb92d28,
        orange: 0xf39c12,
        green: 0x159957,
        blue: 0x2878d7,

        iron: 0x737a80,
        copper: 0xb76c3b,
        silver: 0xc8cdd2,

        oxygen: 0xdf514d,
        hydrogen: 0xf1f3f5,
        chlorine: 0x89a762,

        water: 0x75bce7,
        rust: 0x92502f,

        magnesium: 0xb8bcc1,
        oxide: 0xeeeeee,

        yellow: 0xf3c74f,

        white: 0xffffff,
        black: 0x171717,
        grey: 0x687078,

        glass: 0xaed6ef
    };

    /* =====================================================
       HELPERS
    ===================================================== */

    function clamp(value, min, max) {
        return Math.max(min, Math.min(max, value));
    }

    function lerp(a, b, t) {
        return a + (b - a) * t;
    }

    function smooth(t) {
        return t * t * (3 - 2 * t);
    }

    function makeMaterial(color, options = {}) {

        return new THREE.MeshStandardMaterial({
            color,
            roughness: options.roughness ?? 0.45,
            metalness: options.metalness ?? 0.05,
            transparent: options.transparent ?? false,
            opacity: options.opacity ?? 1
        });
    }

    function makeSphere(radius, color) {

        const mesh = new THREE.Mesh(
            new THREE.SphereGeometry(
                radius,
                28,
                20
            ),
            makeMaterial(color)
        );

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        return mesh;
    }

    function makeBox(
        width,
        height,
        depth,
        color
    ) {

        const mesh = new THREE.Mesh(
            new THREE.BoxGeometry(
                width,
                height,
                depth
            ),
            makeMaterial(color)
        );

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        return mesh;
    }

    function makeCylinder(
        radiusTop,
        radiusBottom,
        height,
        color
    ) {

        const mesh = new THREE.Mesh(
            new THREE.CylinderGeometry(
                radiusTop,
                radiusBottom,
                height,
                32
            ),
            makeMaterial(color)
        );

        mesh.castShadow = true;
        mesh.receiveShadow = true;

        return mesh;
    }

    function createText(
        text,
        color = "#171717",
        width = 4,
        height = 0.5,
        fontSize = 44
    ) {

        const canvas =
            document.createElement("canvas");

        canvas.width = 1000;
        canvas.height = 180;

        const ctx =
            canvas.getContext("2d");

        ctx.clearRect(
            0,
            0,
            canvas.width,
            canvas.height
        );

        ctx.font =
            `700 ${fontSize}px Arial`;

        ctx.fillStyle = color;

        ctx.textAlign = "center";
        ctx.textBaseline = "middle";

        ctx.fillText(
            text,
            canvas.width / 2,
            canvas.height / 2
        );

        const texture =
            new THREE.CanvasTexture(canvas);

        texture.colorSpace =
            THREE.SRGBColorSpace;

        const sprite =
            new THREE.Sprite(
                new THREE.SpriteMaterial({
                    map: texture,
                    transparent: true
                })
            );

        sprite.scale.set(
            width,
            height,
            1
        );

        return sprite;
    }

    function setVisible(object, visible) {

        if (!object) return;

        object.visible = visible;
    }

    function clearGroup(group) {

        while (group.children.length) {

            const child =
                group.children.pop();

            child.traverse(node => {

                if (node.geometry) {
                    node.geometry.dispose();
                }

                if (node.material) {

                    if (
                        Array.isArray(
                            node.material
                        )
                    ) {
                        node.material.forEach(
                            m => m.dispose()
                        );
                    } else {
                        node.material.dispose();
                    }
                }
            });
        }
    }

    /* =====================================================
       LAB CLASS
    ===================================================== */

    class SJScienceLab {

        constructor(container, type) {

            this.container = container;
            this.type = type;

            this.width = 1;
            this.height = 1;

            this.step = 0;
            this.stepCount = 1;

            this.playing = false;
            this.time = 0;
            this.stepDuration = 3.2;

            this.scene =
                new THREE.Scene();

            this.scene.background =
                new THREE.Color(
                    0xf7f8fa
                );

            this.camera =
                new THREE.PerspectiveCamera(
                    38,
                    1,
                    0.1,
                    100
                );

            this.camera.position.set(
                0,
                1.2,
                11
            );

            this.renderer =
                new THREE.WebGLRenderer({
                    antialias: true,
                    alpha: true
                });

            this.renderer.setPixelRatio(
                Math.min(
                    window.devicePixelRatio || 1,
                    2
                )
            );

            this.renderer.outputColorSpace =
                THREE.SRGBColorSpace;

            this.renderer.shadowMap.enabled =
                true;

            this.renderer.shadowMap.type =
                THREE.PCFSoftShadowMap;

            container.innerHTML = "";

            container.appendChild(
                this.renderer.domElement
            );

            this.root =
                new THREE.Group();

            this.scene.add(
                this.root
            );

            this.addLighting();

            this.createControls();

            this.resize();

            this.resizeObserver =
                new ResizeObserver(
                    () => this.resize()
                );

            this.resizeObserver.observe(
                container
            );

            this.build();

            this.animate();
        }

        /* =================================================
           LIGHTING
        ================================================= */

        addLighting() {

            const ambient =
                new THREE.HemisphereLight(
                    0xffffff,
                    0xd7dadd,
                    2.3
                );

            this.scene.add(
                ambient
            );

            const key =
                new THREE.DirectionalLight(
                    0xffffff,
                    3
                );

            key.position.set(
                4,
                8,
                7
            );

            key.castShadow = true;

            this.scene.add(
                key
            );

            const fill =
                new THREE.DirectionalLight(
                    0xffffff,
                    1.2
                );

            fill.position.set(
                -5,
                3,
                4
            );

            this.scene.add(
                fill
            );
        }

        /* =================================================
           RESIZE
        ================================================= */

        resize() {

            const width =
                Math.max(
                    280,
                    this.container.clientWidth
                );

            const height =
                Math.max(
                    260,
                    this.container.clientHeight
                );

            this.width = width;
            this.height = height;

            this.renderer.setSize(
                width,
                height,
                false
            );

            this.camera.aspect =
                width / height;

            this.camera.updateProjectionMatrix();
        }

        /* =================================================
           CONTROLS
        ================================================= */

        createControls() {

            this.controls =
                document.createElement(
                    "div"
                );

            this.controls.className =
                "sj-three-controls";

            this.controls.innerHTML = `
                <button data-action="prev">‹</button>
                <button data-action="play">▶ Play</button>
                <button data-action="next">›</button>
                <button data-action="replay">↺</button>
                <span class="sj-three-step">Step 1</span>
            `;

            Object.assign(
                this.controls.style,
                {
                    position: "absolute",
                    left: "12px",
                    right: "12px",
                    bottom: "10px",
                    height: "42px",
                    display: "flex",
                    gap: "6px",
                    alignItems: "center",
                    justifyContent: "center",
                    pointerEvents: "auto"
                }
            );

            this.container.style.position =
                "relative";

            this.container.appendChild(
                this.controls
            );

            this.controls
                .querySelectorAll(
                    "button"
                )
                .forEach(button => {

                    Object.assign(
                        button.style,
                        {
                            border: "1px solid #d8dadd",
                            background: "#ffffff",
                            color: "#24272a",
                            borderRadius: "9px",
                            padding: "7px 12px",
                            fontWeight: "800",
                            cursor: "pointer"
                        }
                    );
                });

            this.controls
                .querySelector(
                    ".sj-three-step"
                ).style.color =
                "#687078";

            this.controls
                .querySelector(
                    ".sj-three-step"
                ).style.fontSize =
                "11px";

            this.controls
                .addEventListener(
                    "click",
                    event => {

                        const button =
                            event.target.closest(
                                "button"
                            );

                        if (!button) {
                            return;
                        }

                        const action =
                            button.dataset.action;

                        if (
                            action === "play"
                        ) {
                            this.togglePlay();
                        }

                        if (
                            action === "next"
                        ) {
                            this.nextStep();
                        }

                        if (
                            action === "prev"
                        ) {
                            this.previousStep();
                        }

                        if (
                            action === "replay"
                        ) {
                            this.restart();
                        }
                    }
                );
        }

        updateControls() {

            const label =
                this.controls
                    .querySelector(
                        ".sj-three-step"
                    );

            label.textContent =
                `Step ${this.step + 1} of ${this.stepCount}`;

            const play =
                this.controls
                    .querySelector(
                        '[data-action="play"]'
                    );

            play.textContent =
                this.playing
                    ? "❚❚ Pause"
                    : "▶ Play";
        }

        /* =================================================
           STEP SYSTEM
        ================================================= */

        nextStep() {

            this.step =
                Math.min(
                    this.step + 1,
                    this.stepCount - 1
                );

            this.time = 0;

            this.updateControls();

            this.applyStep();
        }

        previousStep() {

            this.step =
                Math.max(
                    this.step - 1,
                    0
                );

            this.time = 0;

            this.updateControls();

            this.applyStep();
        }

        restart() {

            this.step = 0;
            this.time = 0;
            this.playing = false;

            this.updateControls();

            this.applyStep();
        }

        togglePlay() {

            this.playing =
                !this.playing;

            this.updateControls();
        }

        /* =================================================
           GROUND
        ================================================= */

        addGround() {

            const plane =
                new THREE.Mesh(
                    new THREE.PlaneGeometry(
                        20,
                        12
                    ),
                    makeMaterial(
                        0xffffff
                    )
                );

            plane.rotation.x =
                -Math.PI / 2;

            plane.position.y =
                -2.15;

            plane.receiveShadow =
                true;

            this.scene.add(
                plane
            );
        }

        /* =================================================
           BUILD
        ================================================= */

        build() {

            clearGroup(
                this.root
            );

            this.addGround();

            const builders = {

                reaction:
                    () => this.buildReaction(),

                balance:
                    () => this.buildBalance(),

                combination:
                    () => this.buildCombination(),

                decomposition:
                    () => this.buildDecomposition(),

                displacement:
                    () => this.buildDisplacement(),

                double:
                    () => this.buildDouble(),

                energy:
                    () => this.buildEnergy(),

                redox:
                    () => this.buildRedox(),

                corrosion:
                    () => this.buildCorrosion(),

                rancidity:
                    () => this.buildRancidity()
            };

            (
                builders[this.type] ||
                builders.reaction
            )();

            this.restart();
        }

        /* =================================================
           COMMON LABELS
        ================================================= */

        addTitle(text) {

            const title =
                createText(
                    text,
                    "#171717",
                    6.5,
                    0.48,
                    42
                );

            title.position.set(
                0,
                2.65,
                0
            );

            this.root.add(
                title
            );

            this.titleObject =
                title;
        }

        addMessage(
            text,
            y = -1.35,
            color = "#687078"
        ) {

            const label =
                createText(
                    text,
                    color,
                    6,
                    0.42,
                    32
                );

            label.position.set(
                0,
                y,
                0
            );

            this.root.add(
                label
            );

            return label;
        }

        /* =================================================
           TEST TUBE
        ================================================= */

        createTestTube(
            x,
            y = 0
        ) {

            const group =
                new THREE.Group();

            const glass =
                new THREE.Mesh(
                    new THREE.CylinderGeometry(
                        0.72,
                        0.72,
                        2.6,
                        40,
                        1,
                        true
                    ),
                    makeMaterial(
                        C.glass,
                        {
                            transparent: true,
                            opacity: 0.24
                        }
                    )
                );

            group.add(
                glass
            );

            const bottom =
                makeCylinder(
                    0.72,
                    0.72,
                    0.1,
                    C.glass
                );

            bottom.material.opacity =
                0.30;

            bottom.material.transparent =
                true;

            bottom.position.y =
                -1.3;

            group.add(
                bottom
            );

            group.position.set(
                x,
                y,
                0
            );

            this.root.add(
                group
            );

            return group;
        }

        addLiquid(
            tube,
            color,
            height = 0.8
        ) {

            const liquid =
                makeCylinder(
                    0.62,
                    0.62,
                    height,
                    color
                );

            liquid.material.transparent =
                true;

            liquid.material.opacity =
                0.50;

            liquid.position.y =
                -1.3 +
                height / 2;

            tube.add(
                liquid
            );

            return liquid;
        }

        /* =================================================
           STEP 1
           MAGNESIUM REACTION
        ================================================= */

        buildReaction() {

            this.stepCount = 5;

            this.addTitle(
                "Magnesium ribbon + oxygen"
            );

            this.reaction = {};

            /* Burner */

            const burner =
                makeCylinder(
                    0.42,
                    0.52,
                    0.9,
                    0x70757b
                );

            burner.position.set(
                -3.2,
                -1.35,
                0
            );

            this.root.add(
                burner
            );

            this.reaction.burner =
                burner;

            /* Flame */

            const flame =
                makeSphere(
                    0.28,
                    C.yellow
                );

            flame.scale.set(
                0.75,
                1.6,
                0.75
            );

            flame.position.set(
                -3.2,
                -0.65,
                0
            );

            flame.visible =
                false;

            this.root.add(
                flame
            );

            this.reaction.flame =
                flame;

            /* Magnesium ribbon */

            const ribbon =
                makeBox(
                    1.65,
                    0.12,
                    0.08,
                    C.magnesium
                );

            ribbon.position.set(
                -3.2,
                0.05,
                0
            );

            ribbon.rotation.z =
                -0.08;

            this.root.add(
                ribbon
            );

            this.reaction.ribbon =
                ribbon;

            /* Oxygen molecules */

            this.reaction.oxygen =
                [];

            for (
                let i = 0;
                i < 8;
                i++
            ) {

                const molecule =
                    new THREE.Group();

                const o1 =
                    makeSphere(
                        0.13,
                        C.oxygen
                    );

                const o2 =
                    makeSphere(
                        0.13,
                        C.oxygen
                    );

                o1.position.x =
                    -0.14;

                o2.position.x =
                    0.14;

                molecule.add(o1);
                molecule.add(o2);

                molecule.position.set(
                    -1.2 +
                    Math.random() * 2.3,

                    1.0 +
                    Math.random() * 0.9,

                    0
                );

                this.root.add(
                    molecule
                );

                this.reaction.oxygen.push(
                    molecule
                );
            }

            /* MgO powder */

            this.reaction.mgo =
                [];

            for (
                let i = 0;
                i < 18;
                i++
            ) {

                const particle =
                    makeSphere(
                        0.10,
                        C.oxide
                    );

                particle.position.set(
                    -0.8 +
                    Math.random() * 1.6,

                    -1.35 +
                    Math.random() * 0.35,

                    0.15
                );

                particle.visible =
                    false;

                this.root.add(
                    particle
                );

                this.reaction.mgo.push(
                    particle
                );
            }

            this.reaction.observation =
                this.addMessage(
                    "Observe: heating → dazzling white light → new white solid",
                    -1.65,
                    "#7b4c39"
                );

            this.reaction.equation =
                this.addMessage(
                    "2Mg + O₂ → 2MgO",
                    -1.95,
                    "#171717"
                );

            this.applyReactionStep = () => {

                const s =
                    this.step;

                setVisible(
                    this.reaction.flame,
                    s >= 1
                );

                if (s >= 1) {

                    this.reaction.ribbon.scale.y =
                        1 +
                        0.08 *
                        Math.sin(
                            this.time * 5
                        );

                    this.reaction.ribbon.material.color
                        .setHex(
                            s >= 2
                                ? 0xffffff
                                : C.magnesium
                        );
                }

                this.reaction.oxygen
                    .forEach(
                        (molecule, i) => {

                            if (s >= 2) {

                                const targetX =
                                    -3.2 +
                                    (
                                        i %
                                        4
                                    ) *
                                    0.35;

                                const targetY =
                                    0.1 +
                                    (
                                        Math.floor(
                                            i / 4
                                        )
                                    ) *
                                    0.28;

                                molecule.position.x =
                                    lerp(
                                        molecule.position.x,
                                        targetX,
                                        0.035
                                    );

                                molecule.position.y =
                                    lerp(
                                        molecule.position.y,
                                        targetY,
                                        0.035
                                    );
                            }
                        }
                    );

                this.reaction.mgo
                    .forEach(
                        particle => {

                            particle.visible =
                                s >= 3;
                        }
                    );

                setVisible(
                    this.reaction.observation,
                    s >= 4
                );

                setVisible(
                    this.reaction.equation,
                    s >= 4
                );
            };
        }

        /* =================================================
           BALANCING
        ================================================= */

        buildBalance() {

            this.stepCount = 5;

            this.addTitle(
                "Balance by changing coefficients"
            );

            this.balance = {};

            this.balance.formula =
                this.addMessage(
                    "Fe + H₂O → Fe₃O₄ + H₂",
                    1.55,
                    "#171717"
                );

            this.balance.countLabel =
                this.addMessage(
                    "Count atoms on each side",
                    -1.45,
                    "#687078"
                );

            /* Atom panels */

            this.balance.left =
                this.createAtomCountPanel(
                    -3.0,
                    "Reactants"
                );

            this.balance.right =
                this.createAtomCountPanel(
                    3.0,
                    "Products"
                );

            this.balance.initial =
                [
                    {
                        element: "Fe",
                        left: 1,
                        right: 3
                    },

                    {
                        element: "O",
                        left: 1,
                        right: 4
                    },

                    {
                        element: "H",
                        left: 2,
                        right: 4
                    }
                ];

            this.balance.final =
                [
                    {
                        element: "Fe",
                        left: 3,
                        right: 3
                    },

                    {
                        element: "O",
                        left: 4,
                        right: 4
                    },

                    {
                        element: "H",
                        left: 8,
                        right: 8
                    }
                ];

            this.balance.state =
                this.addMessage(
                    "Atoms are conserved — only coefficients change",
                    -1.82,
                    "#159957"
                );

            this.applyBalanceStep =
                () => {

                    const s =
                        this.step;

                    if (s <= 1) {

                        this.balance.formula
                            .material
                            .map;

                    }

                    if (s === 0) {

                        this.balance.formula
                            .visible = true;

                    }

                    if (s >= 1) {

                        this.renderCountPanels(
                            this.balance.initial
                        );
                    }

                    if (s >= 2) {

                        this.balance.formula.scale.set(
                            6.3,
                            0.55,
                            1
                        );

                        this.balance.formula
                            .position.y =
                            1.55;
                    }

                    if (s >= 3) {

                        this.balance.formula
                            .visible = false;

                        this.balance.corrected =
                            this.addMessage(
                                "3Fe + 4H₂O → Fe₃O₄ + 4H₂",
                                1.55,
                                "#159957"
                            );
                    }

                    if (s >= 4) {

                        this.renderCountPanels(
                            this.balance.final
                        );

                        this.balance.countLabel
                            .textContent =
                            "Every element now has the same atom count";
                    }

                    if (s < 3) {

                        if (
                            this.balance.corrected
                        ) {
                            this.balance.corrected
                                .visible = false;
                        }
                    }

                    if (s < 4) {

                        this.balance.countLabel
                            .textContent =
                            "Count atoms on each side";
                    }
                };
        }

        createAtomCountPanel(
            x,
            title
        ) {

            const group =
                new THREE.Group();

            group.position.x =
                x;

            this.root.add(
                group
            );

            const heading =
                createText(
                    title,
                    "#171717",
                    2.8,
                    0.35,
                    32
                );

            heading.position.y =
                0.85;

            group.add(
                heading
            );

            return group;
        }

        renderCountPanels(
            data
        ) {

            [
                this.balance.left,
                this.balance.right
            ]
                .forEach(
                    group => {

                        while (
                            group.children.length > 1
                        ) {

                            const child =
                                group.children.pop();

                            this.disposeObject(
                                child
                            );
                        }
                    }
                );

            const rows =
                data;

            rows.forEach(
                (row, index) => {

                    const y =
                        0.3 -
                        index * 0.55;

                    const left =
                        createText(
                            `${row.element} = ${row.left}`,
                            row.left ===
                                row.right
                                ? "#159957"
                                : "#b92d28",
                            2.5,
                            0.33,
                            28
                        );

                    left.position.y =
                        y;

                    this.balance.left.add(
                        left
                    );

                    const right =
                        createText(
                            `${row.element} = ${row.right}`,
                            row.left ===
                                row.right
                                ? "#159957"
                                : "#b92d28",
                            2.5,
                            0.33,
                            28
                        );

                    right.position.y =
                        y;

                    this.balance.right.add(
                        right
                    );
                }
            );
        }

        /* =================================================
           COMBINATION
        ================================================= */

        buildCombination() {

            this.stepCount = 4;

            this.addTitle(
                "Combination: substances form one product"
            );

            this.combination = {};

            const left =
                this.createTestTube(
                    -2.5
                );

            const right =
                this.createTestTube(
                    0
                );

            const product =
                this.createTestTube(
                    3
                );

            this.addLiquid(
                left,
                0xe0e0e0,
                0.7
            );

            this.addLiquid(
                right,
                C.water,
                0.7
            );

            this.addLiquid(
                product,
                0xcfe6d0,
                1.0
            );

            this.combination.left =
                left;

            this.combination.right =
                right;

            this.combination.product =
                product;

            this.combination.note =
                this.addMessage(
                    "Two reactants → one product",
                    -1.65
                );

            this.combination.equation =
                this.addMessage(
                    "CaO + H₂O → Ca(OH)₂",
                    -1.95,
                    "#171717"
                );
        }

        /* =================================================
           DECOMPOSITION
        ================================================= */

        buildDecomposition() {

            this.stepCount = 4;

            this.addTitle(
                "Decomposition: one substance breaks apart"
            );

            this.decomposition = {};

            const tube =
                this.createTestTube(
                    0
                );

            this.addLiquid(
                tube,
                0xe1e1e1,
                0.75
            );

            const burner =
                makeCylinder(
                    0.45,
                    0.55,
                    0.85,
                    0x70757b
                );

            burner.position.set(
                0,
                -1.6,
                0
            );

            this.root.add(
                burner
            );

            const flame =
                makeSphere(
                    0.28,
                    C.orange
                );

            flame.scale.y =
                1.6;

            flame.position.set(
                0,
                -0.78,
                0
            );

            flame.visible =
                false;

            this.root.add(
                flame
            );

            this.decomposition.tube =
                tube;

            this.decomposition.flame =
                flame;

            this.decomposition.particles =
                [];

            for (
                let i = 0;
                i < 10;
                i++
            ) {

                const particle =
                    makeSphere(
                        0.1,
                        C.rust
                    );

                particle.position.set(
                    0,
                    -0.5,
                    0
                );

                this.root.add(
                    particle
                );

                this.decomposition.particles
                    .push(
                        particle
                    );
            }

            this.decomposition.note =
                this.addMessage(
                    "Energy supplied → compound splits into simpler substances",
                    -1.55
                );

            this.decomposition.equation =
                this.addMessage(
                    "CaCO₃  ──heat──→  CaO + CO₂",
                    -1.92,
                    "#171717"
                );
        }

        /* =================================================
           DISPLACEMENT
        ================================================= */

        buildDisplacement() {

            this.stepCount = 5;

            this.addTitle(
                "Displacement: iron replaces copper"
            );

            this.displacement = {};

            const beaker =
                this.createTestTube(
                    0
                );

            const solution =
                this.addLiquid(
                    beaker,
                    0x4b91d3,
                    0.9
                );

            const nail =
                makeBox(
                    0.18,
                    2.0,
                    0.12,
                    C.iron
                );

            nail.position.set(
                0,
                1.0,
                0.2
            );

            nail.rotation.z =
                -0.04;

            this.root.add(
                nail
            );

            const copper =
                [];

            for (
                let i = 0;
                i < 25;
                i++
            ) {

                const particle =
                    makeSphere(
                        0.055,
                        C.copper
                    );

                particle.position.set(

                    -0.45 +
                    Math.random() *
                    0.9,

                    -0.6 +
                    Math.random() *
                    0.9,

                    0.3
                );

                this.root.add(
                    particle
                );

                copper.push(
                    particle
                );
            }

            this.displacement.nail =
                nail;

            this.displacement.solution =
                solution;

            this.displacement.copper =
                copper;

            this.displacement.note =
                this.addMessage(
                    "Iron enters CuSO₄ → copper leaves the solution",
                    -1.55
                );

            this.displacement.equation =
                this.addMessage(
                    "Fe + CuSO₄ → FeSO₄ + Cu",
                    -1.92,
                    "#171717"
                );
        }

        /* =================================================
           DOUBLE DISPLACEMENT
        ================================================= */

        buildDouble() {

            this.stepCount = 5;

            this.addTitle(
                "Double displacement + precipitation"
            );

            this.double = {};

            const left =
                this.createTestTube(
                    -2.1
                );

            const right =
                this.createTestTube(
                    0
                );

            const result =
                this.createTestTube(
                    2.7
                );

            this.addLiquid(
                left,
                0xb6d9ed,
                0.8
            );

            this.addLiquid(
                right,
                0xcce5c2,
                0.8
            );

            this.addLiquid(
                result,
                0xe5eff4,
                1
            );

            const precipitate =
                [];

            for (
                let i = 0;
                i < 35;
                i++
            ) {

                const p =
                    makeSphere(
                        0.07,
                        0xffffff
                    );

                p.position.set(
                    2.7 +
                    (
                        Math.random() -
                        0.5
                    ) *
                    0.9,

                    -1.1 +
                    Math.random() *
                    1.0,

                    0.2
                );

                p.visible =
                    false;

                this.root.add(
                    p
                );

                precipitate.push(
                    p
                );
            }

            this.double.precipitate =
                precipitate;

            this.double.note =
                this.addMessage(
                    "Ions exchange partners → insoluble BaSO₄ forms",
                    -1.55
                );

            this.double.equation =
                this.addMessage(
                    "Na₂SO₄ + BaCl₂ → BaSO₄↓ + 2NaCl",
                    -1.92,
                    "#171717"
                );
        }

        /* =================================================
           ENERGY
        ================================================= */

        buildEnergy() {

            this.stepCount = 5;

            this.addTitle(
                "Exothermic vs endothermic"
            );

            this.energy = {};

            this.createEnergySetup(
                -2.8,
                "EXOTHERMIC",
                C.red
            );

            this.createEnergySetup(
                2.8,
                "ENDOTHERMIC",
                C.blue
            );

            this.energy.note =
                this.addMessage(
                    "Watch the thermometer: heat leaves in exothermic reactions and enters in endothermic reactions.",
                    -1.7
                );
        }

        createEnergySetup(
            x,
            title,
            color
        ) {

            const group =
                new THREE.Group();

            group.position.x =
                x;

            this.root.add(
                group
            );

            const label =
                createText(
                    title,
                    color === C.red
                        ? "#b92d28"
                        : "#2878d7",
                    2.6,
                    0.34,
                    30
                );

            label.position.y =
                1.7;

            group.add(
                label
            );

            const beaker =
                makeBox(
                    2.6,
                    1.8,
                    0.55,
                    0xe9eef2
                );

            beaker.material.transparent =
                true;

            beaker.material.opacity =
                0.35;

            beaker.position.y =
                0.1;

            group.add(
                beaker
            );

            const liquid =
                makeBox(
                    2.1,
                    0.7,
                    0.45,
                    color
                );

            liquid.material.transparent =
                true;

            liquid.material.opacity =
                0.42;

            liquid.position.y =
                -0.35;

            group.add(
                liquid
            );

            const thermometer =
                makeCylinder(
                    0.07,
                    0.07,
                    1.8,
                    0xf5f5f5
                );

            thermometer.position.set(
                0.7,
                0.4,
                0.35
            );

            group.add(
                thermometer
            );

            const mercury =
                makeCylinder(
                    0.085,
                    0.085,
                    0.45,
                    C.red
                );

            mercury.position.set(
                0.7,
                -0.35,
                0.42
            );

            group.add(
                mercury
            );

            group.userData =
            {
                mercury
            };
        }

        /* =================================================
           REDOX
        ================================================= */

        buildRedox() {

            this.stepCount = 5;

            this.addTitle(
                "Redox: oxygen moves from CuO to H₂"
            );

            this.redox = {};

            /* CuO */

            const cu =
                makeSphere(
                    0.30,
                    C.copper
                );

            cu.position.set(
                -3,
                0,
                0
            );

            const oxygen =
                makeSphere(
                    0.22,
                    C.oxygen
                );

            oxygen.position.set(
                -2.45,
                0,
                0
            );

            /* H₂ */

            const h1 =
                makeSphere(
                    0.20,
                    C.hydrogen
                );

            const h2 =
                makeSphere(
                    0.20,
                    C.hydrogen
                );

            h1.position.set(
                -1,
                0,
                0
            );

            h2.position.set(
                -0.55,
                0,
                0
            );

            /* Product */

            const copper =
                makeSphere(
                    0.30,
                    C.copper
                );

            copper.position.set(
                2.7,
                0,
                0
            );

            const waterOxygen =
                makeSphere(
                    0.22,
                    C.oxygen
                );

            waterOxygen.position.set(
                2.0,
                0.45,
                0
            );

            const waterH1 =
                makeSphere(
                    0.18,
                    C.hydrogen
                );

            const waterH2 =
                makeSphere(
                    0.18,
                    C.hydrogen
                );

            waterH1.position.set(
                1.55,
                0.15,
                0
            );

            waterH2.position.set(
                2.45,
                0.15,
                0
            );

            [
                cu,
                oxygen,
                h1,
                h2,
                copper,
                waterOxygen,
                waterH1,
                waterH2
            ].forEach(
                object =>
                    this.root.add(object)
            );

            const oLabel =
                createText(
                    "oxygen",
                    "#b92d28",
                    1.6,
                    0.30,
                    28
                );

            oLabel.position.set(
                -2.45,
                0.6,
                0
            );

            this.root.add(
                oLabel
            );

            this.redox.cuo =
            {
                cu,
                oxygen
            };

            this.redox.hydrogen =
            {
                h1,
                h2
            };

            this.redox.products =
            {
                copper,
                waterOxygen,
                waterH1,
                waterH2
            };

            this.redox.note =
                this.addMessage(
                    "CuO loses oxygen → reduction",
                    -1.35,
                    "#b92d28"
                );

            this.redox.note2 =
                this.addMessage(
                    "H₂ gains oxygen → oxidation",
                    -1.75,
                    "#159957"
                );

            this.redox.equation =
                this.addMessage(
                    "CuO + H₂ → Cu + H₂O",
                    -2.05,
                    "#171717"
                );
        }

        /* =================================================
           CORROSION
        ================================================= */

        buildCorrosion() {

            this.stepCount = 5;

            this.addTitle(
                "Corrosion: compare exposed and protected iron"
            );

            this.corrosion = {};

            this.createCorrosionColumn(
                -2.8,
                false
            );

            this.createCorrosionColumn(
                2.8,
                true
            );

            this.corrosion.note =
                this.addMessage(
                    "Time passes → moisture and air attack exposed iron",
                    -1.75
                );
        }

        createCorrosionColumn(
            x,
            painted
        ) {

            const group =
                new THREE.Group();

            group.position.x =
                x;

            this.root.add(
                group
            );

            const heading =
                createText(
                    painted
                        ? "PAINTED IRON"
                        : "EXPOSED IRON",
                    painted
                        ? "#159957"
                        : "#92502f",
                    2.8,
                    0.35,
                    28
                );

            heading.position.y =
                1.75;

            group.add(
                heading
            );

            const iron =
                makeBox(
                    2.7,
                    0.5,
                    0.7,
                    C.iron
                );

            iron.position.y =
                -0.1;

            group.add(
                iron
            );

            let paint = null;

            if (painted) {

                paint =
                    makeBox(
                        2.8,
                        0.15,
                        0.75,
                        C.red
                    );

                paint.position.y =
                    0.2;

                group.add(
                    paint
                );
            }

            const rust =
                [];

            for (
                let i = 0;
                i < 24;
                i++
            ) {

                const particle =
                    makeSphere(
                        0.06,
                        C.rust
                    );

                particle.position.set(
                    -1.1 +
                    Math.random() *
                    2.2,

                    0.05 +
                    Math.random() *
                    0.4,

                    0.4
                );

                particle.visible =
                    false;

                group.add(
                    particle
                );

                rust.push(
                    particle
                );
            }

            group.userData =
            {
                painted,
                rust,
                paint
            };

            if (!this.corrosion.groups) {
                this.corrosion.groups = [];
            }

            this.corrosion.groups.push(
                group
            );
        }

        /* =================================================
           RANCIDITY
        ================================================= */

        buildRancidity() {

            this.stepCount = 5;

            this.addTitle(
                "Rancidity: why nitrogen helps protect food"
            );

            this.rancidity = {};

            this.createFoodPacket(
                -2.8,
                false
            );

            this.createFoodPacket(
                2.8,
                true
            );

            this.rancidity.note =
                this.addMessage(
                    "Less oxygen contact → slower oxidation of fats and oils",
                    -1.75
                );
        }

        createFoodPacket(
            x,
            nitrogenProtected
        ) {

            const group =
                new THREE.Group();

            group.position.x =
                x;

            this.root.add(
                group
            );

            const heading =
                createText(
                    nitrogenProtected
                        ? "NITROGEN FLUSHED"
                        : "AIR PRESENT",
                    nitrogenProtected
                        ? "#159957"
                        : "#b92d28",
                    3,
                    0.34,
                    27
                );

            heading.position.y =
                1.65;

            group.add(
                heading
            );

            const packet =
                makeBox(
                    2.8,
                    1.75,
                    0.25,
                    0xffffff
                );

            packet.position.y =
                -0.05;

            group.add(
                packet
            );

            const chips =
                [];

            for (
                let i = 0;
                i < 12;
                i++
            ) {

                const chip =
                    makeSphere(
                        0.14,
                        C.yellow
                    );

                chip.scale.y =
                    0.45;

                chip.position.set(
                    -0.85 +
                    (
                        i % 4
                    ) *
                    0.55,

                    -0.45 +
                    Math.floor(
                        i / 4
                    ) *
                    0.38,

                    0.18
                );

                group.add(
                    chip
                );

                chips.push(
                    chip
                );
            }

            const oxygen =
                [];

            for (
                let i = 0;
                i < 12;
                i++
            ) {

                const particle =
                    makeSphere(
                        0.06,
                        C.oxygen
                    );

                particle.position.set(
                    -1.1 +
                    Math.random() *
                    2.2,

                    0.65 +
                    Math.random() *
                    0.6,

                    0.2
                );

                particle.visible =
                    !nitrogenProtected;

                group.add(
                    particle
                );

                oxygen.push(
                    particle
                );
            }

            group.userData =
            {
                nitrogenProtected,
                oxygen,
                chips
            };

            if (!this.rancidity.groups) {
                this.rancidity.groups = [];
            }

            this.rancidity.groups.push(
                group
            );
        }

        /* =================================================
           STEP APPLICATION
        ================================================= */

        applyStep() {

            if (
                this.applyReactionStep
            ) {
                this.applyReactionStep();
            }

            if (
                this.applyBalanceStep
            ) {
                this.applyBalanceStep();
            }
        }

        /* =================================================
           UNIVERSAL ANIMATION
        ================================================= */

        animate() {

            if (this.destroyed) {
                return;
            }

            requestAnimationFrame(
                () => this.animate()
            );

            const delta =
                1 / 60;

            if (this.playing) {

                this.time +=
                    delta;

                if (
                    this.time >
                    this.stepDuration
                ) {

                    if (
                        this.step <
                        this.stepCount - 1
                    ) {

                        this.nextStep();

                    } else {

                        this.playing =
                            false;

                        this.updateControls();
                    }
                }
            }

            this.animateScene();

            this.renderer.render(
                this.scene,
                this.camera
            );
        }

        /* =================================================
           ANIMATE SCENE
        ================================================= */

        animateScene() {

            const t =
                this.time;

            /* ---------------------------------------------
               Reaction
            --------------------------------------------- */

            if (
                this.type ===
                "reaction"
            ) {

                if (this.reaction) {

                    const p =
                        (
                            Math.sin(
                                t * 5
                            ) + 1
                        ) / 2;

                    this.reaction.flame.scale.y =
                        1.3 +
                        p * 0.5;

                    if (
                        this.step >= 2
                    ) {

                        this.reaction.oxygen
                            .forEach(
                                (molecule, index) => {

                                    molecule.rotation.y =
                                        t * 0.7;

                                    molecule.position.x +=
                                        (
                                            -3.1 -
                                            molecule.position.x
                                        ) *
                                        0.018;

                                    molecule.position.y +=
                                        (
                                            0.05 +
                                            (
                                                index %
                                                4
                                            ) *
                                            0.28 -
                                            molecule.position.y
                                        ) *
                                        0.018;
                                }
                            );
                    }
                }
            }

            /* ---------------------------------------------
               Balance
            --------------------------------------------- */

            if (
                this.type ===
                "balance"
            ) {

                if (
                    this.step === 2 &&
                    this.balance.formula
                ) {

                    this.balance.formula
                        .scale.x =
                        6.3 +
                        Math.sin(
                            t * 4
                        ) *
                        0.08;
                }
            }

            /* ---------------------------------------------
               Combination
            --------------------------------------------- */

            if (
                this.type ===
                "combination"
            ) {

                const p =
                    (
                        Math.sin(
                            t * 1.2
                        ) + 1
                    ) / 2;

                if (
                    this.combination
                ) {

                    this.combination.left
                        .position.x =
                        lerp(
                            -2.5,
                            -1.3,
                            p
                        );

                    this.combination.right
                        .position.x =
                        lerp(
                            0,
                            -1.3,
                            p
                        );

                    this.combination.product
                        .scale.setScalar(
                            0.95 +
                            0.08 * p
                        );
                }
            }

            /* ---------------------------------------------
               Decomposition
            --------------------------------------------- */

            if (
                this.type ===
                "decomposition"
            ) {

                const flame =
                    this.decomposition
                        ?.flame;

                if (flame) {

                    flame.scale.y =
                        1.25 +
                        (
                            Math.sin(
                                t * 5
                            ) + 1
                        ) *
                        0.35;
                }

                if (
                    this.step >= 2
                ) {

                    this.decomposition
                        .particles
                        .forEach(
                            (
                                particle,
                                index
                            ) => {

                                const angle =
                                    (
                                        index /
                                        this.decomposition
                                            .particles
                                            .length
                                    ) *
                                    Math.PI *
                                    2;

                                particle.position.x =
                                    Math.cos(
                                        angle
                                    ) *
                                    0.9;

                                particle.position.y =
                                    Math.sin(
                                        angle
                                    ) *
                                    0.55;
                            }
                        );
                }
            }

            /* ---------------------------------------------
               Displacement
            --------------------------------------------- */

            if (
                this.type ===
                "displacement"
            ) {

                if (
                    this.step >= 2
                ) {

                    this.displacement.copper
                        .forEach(
                            (
                                particle,
                                index
                            ) => {

                                particle.position.y +=
                                    0.0008 +
                                    Math.sin(
                                        t * 2 +
                                        index
                                    ) *
                                    0.0004;

                                particle.position.x +=
                                    Math.sin(
                                        t +
                                        index
                                    ) *
                                    0.0002;
                            }
                        );
                }
            }

            /* ---------------------------------------------
               Double displacement
            --------------------------------------------- */

            if (
                this.type ===
                "double"
            ) {

                const visible =
                    this.step >= 3;

                this.double
                    .precipitate
                    .forEach(
                        (
                            particle,
                            index
                        ) => {

                            particle.visible =
                                visible;

                            if (visible) {

                                particle.position.y =
                                    lerp(
                                        particle.position.y,
                                        -1.15,
                                        0.018
                                    );
                            }
                        }
                    );
            }

            /* ---------------------------------------------
               Energy
            --------------------------------------------- */

            if (
                this.type ===
                "energy"
            ) {

                const amount =
                    (
                        Math.sin(
                            t * 2
                        ) + 1
                    ) / 2;

                this.root.children
                    .forEach(
                        object => {

                            if (
                                object.userData
                            ) {
                                const mercury =
                                    object.userData
                                        .mercury;

                                if (mercury) {

                                    mercury.scale.y =
                                        0.7 +
                                        amount *
                                        (
                                            this.step >= 2
                                                ? 1.4
                                                : 0.5
                                        );
                                }
                            }
                        }
                    );
            }

            /* ---------------------------------------------
               Redox — oxygen transfer
            --------------------------------------------- */

            if (
                this.type ===
                "redox"
            ) {

                const oxygen =
                    this.redox
                        ?.cuo
                        ?.oxygen;

                if (
                    oxygen &&
                    this.step >= 2
                ) {

                    const p =
                        (
                            Math.sin(
                                t * 1.2
                            ) + 1
                        ) / 2;

                    oxygen.position.x =
                        lerp(
                            -2.45,
                            0.8,
                            p
                        );

                    oxygen.position.y =
                        0.35 +
                        Math.sin(
                            t * 3
                        ) *
                        0.08;
                }
            }

            /* ---------------------------------------------
               Corrosion
            --------------------------------------------- */

            if (
                this.type ===
                "corrosion"
            ) {

                if (
                    this.corrosion.groups
                ) {

                    this.corrosion.groups
                        .forEach(
                            group => {

                                group.userData
                                    .rust
                                    .forEach(
                                        particle => {

                                            particle.visible =
                                                !group
                                                    .userData
                                                    .painted &&
                                                this.step >=
                                                2;
                                        }
                                    );
                            }
                        );
                }
            }

            /* ---------------------------------------------
               Rancidity
            --------------------------------------------- */

            if (
                this.type ===
                "rancidity"
            ) {

                if (
                    this.rancidity.groups
                ) {

                    this.rancidity.groups
                        .forEach(
                            group => {

                                const protectedPacket =
                                    group
                                        .userData
                                        .nitrogenProtected;

                                group.userData
                                    .oxygen
                                    .forEach(
                                        oxygen => {

                                            oxygen.visible =
                                                !protectedPacket &&
                                                this.step >=
                                                1;
                                        }
                                    );

                                if (
                                    !protectedPacket &&
                                    this.step >= 3
                                ) {

                                    group.userData
                                        .chips
                                        .forEach(
                                            chip => {

                                                chip.material
                                                    .color
                                                    .setHex(
                                                        C.rust
                                                    );
                                            }
                                        );
                                }
                            }
                        );
                }
            }
        }

        /* =================================================
           DISPOSE
        ================================================= */

        disposeObject(object) {

            object.traverse(
                node => {

                    node.geometry?.dispose();

                    if (
                        node.material
                    ) {

                        if (
                            Array.isArray(
                                node.material
                            )
                        ) {

                            node.material
                                .forEach(
                                    material =>
                                        material.dispose()
                                );

                        } else {

                            node.material.dispose();
                        }
                    }
                }
            );
        }

        destroy() {

            this.destroyed =
                true;

            this.resizeObserver?.disconnect();

            this.renderer.dispose();

            this.controls?.remove();

            this.container.innerHTML =
                "";
        }
    }

    /* =========================================================
       INITIALIZE
    ========================================================= */

    function initialize() {

        document
            .querySelectorAll(
                "[data-three-animation]"
            )
            .forEach(
                container => {

                    if (
                        container
                            .dataset
                            .sjThreeInitialized
                        === "1"
                    ) {
                        return;
                    }

                    container
                        .dataset
                        .sjThreeInitialized =
                        "1";

                    const type =
                        (
                            container
                                .dataset
                                .threeAnimation ||
                            "reaction"
                        ).toLowerCase();

                    container.style.height =
                        container.dataset.height
                            ? `${parseInt(
                                container.dataset.height,
                                10
                            )}px`
                            : "360px";

                    container.style.position =
                        "relative";

                    container.style.overflow =
                        "hidden";

                    container.style.borderRadius =
                        "18px";

                    container.style.background =
                        "#f7f8fa";

                    try {

                        container
                            ._sjScienceLab =
                            new SJScienceLab(
                                container,
                                type
                            );

                    } catch (
                    error
                    ) {

                        console.error(
                            "SJMaths animation error:",
                            error
                        );

                        container.innerHTML = `
                            <div style="
                                height:100%;
                                display:flex;
                                align-items:center;
                                justify-content:center;
                                padding:20px;
                                font:700 13px system-ui;
                                color:#687078;
                                text-align:center;
                            ">
                                Animation could not be initialized.
                            </div>
                        `;
                    }
                }
            );
    }

    /* =========================================================
       PUBLIC API
    ========================================================= */

    window.SJMathsThreeAnimations = {

        init:
            initialize,

        play:
            selector => {

                const element =
                    document.querySelector(
                        selector
                    );

                element
                    ?._sjScienceLab
                    ?.togglePlay();
            },

        pause:
            selector => {

                const element =
                    document.querySelector(
                        selector
                    );

                if (
                    element?._sjScienceLab
                ) {

                    element
                        ._sjScienceLab
                        .playing =
                        false;

                    element
                        ._sjScienceLab
                        .updateControls();
                }
            },

        next:
            selector => {

                document
                    .querySelector(
                        selector
                    )
                    ?._sjScienceLab
                    ?.nextStep();
            },

        previous:
            selector => {

                document
                    .querySelector(
                        selector
                    )
                    ?._sjScienceLab
                    ?.previousStep();
            },

        replay:
            selector => {

                document
                    .querySelector(
                        selector
                    )
                    ?._sjScienceLab
                    ?.restart();
            },

        destroy:
            selector => {

                document
                    .querySelector(
                        selector
                    )
                    ?._sjScienceLab
                    ?.destroy();
            }
    };

    /* =========================================================
       START
    ========================================================= */

    if (
        document.readyState ===
        "loading"
    ) {

        document.addEventListener(
            "DOMContentLoaded",
            initialize,
            {
                once: true
            }
        );

    } else {

        initialize();
    }

})();