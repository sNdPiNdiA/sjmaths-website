(function () {
    "use strict";

    /* ===== ANIMATION: CELL (3D Model) ===== */
    window.initCellAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 2, 12);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        /* Cell membrane (translucent sphere) */
        var membraneGeo = new THREE.SphereGeometry(5, 64, 64);
        var membraneMat = new THREE.MeshPhongMaterial({
            color: 0x0f9d8a, transparent: true, opacity: 0.15, side: THREE.DoubleSide
        });
        var membrane = new THREE.Mesh(membraneGeo, membraneMat);
        scene.add(membrane);

        /* Nucleus */
        var nucleusGeo = new THREE.SphereGeometry(1.5, 32, 32);
        var nucleusMat = new THREE.MeshPhongMaterial({ color: 0x8b5cf6, transparent: true, opacity: 0.8 });
        var nucleus = new THREE.Mesh(nucleusGeo, nucleusMat);
        scene.add(nucleus);

        /* Nucleolus */
        var nucleolusGeo = new THREE.SphereGeometry(0.6, 16, 16);
        var nucleolusMat = new THREE.MeshPhongMaterial({ color: 0x6d28d9 });
        var nucleolus = new THREE.Mesh(nucleolusGeo, nucleolusMat);
        nucleus.add(nucleolus);

        /* Mitochondria */
        var mitoGeo = new THREE.SphereGeometry(0.5, 16, 16);
        mitoGeo.scale(1.5, 0.8, 0.8);
        var mitoMat = new THREE.MeshPhongMaterial({ color: 0xf59e0b });
        for (var i = 0; i < 5; i++) {
            var mito = new THREE.Mesh(mitoGeo, mitoMat);
            var angle = (i / 5) * Math.PI * 2;
            mito.position.set(Math.cos(angle) * 3, Math.sin(angle) * 2, Math.sin(angle) * 2);
            mito.rotation.z = angle;
            scene.add(mito);
        }

        /* Vacuole */
        var vacGeo = new THREE.SphereGeometry(1, 32, 32);
        var vacMat = new THREE.MeshPhongMaterial({ color: 0x60a5fa, transparent: true, opacity: 0.3 });
        var vacuole = new THREE.Mesh(vacGeo, vacMat);
        vacuole.position.set(2.5, -1, 1);
        scene.add(vacuole);

        /* Endoplasmic Reticulum */
        var erPoints = [];
        for (var j = 0; j < 20; j++) {
            var t = j / 20;
            erPoints.push(new THREE.Vector3(
                Math.cos(t * Math.PI * 2) * 3.5,
                Math.sin(t * Math.PI * 2) * 1.5,
                Math.cos(t * Math.PI * 4) * 1
            ));
        }
        var erCurve = new THREE.CatmullRomCurve3(erPoints);
        var erGeo = new THREE.TubeGeometry(erCurve, 64, 0.15, 8, false);
        var erMat = new THREE.MeshPhongMaterial({ color: 0x10b981 });
        var er = new THREE.Mesh(erGeo, erMat);
        scene.add(er);

        /* Lighting */
        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        var light = new THREE.PointLight(0xffffff, 0.8);
        light.position.set(10, 10, 10);
        scene.add(light);

        /* Drag controls */
        var rotX = 0, rotY = 0, isDrag = false, pX = 0, pY = 0;
        canvas.addEventListener("mousedown", function (e) { isDrag = true; pX = e.clientX; pY = e.clientY; });
        canvas.addEventListener("mouseup", function () { isDrag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (isDrag) { rotY += (e.clientX - pX) * 0.01; rotX += (e.clientY - pY) * 0.01; pX = e.clientX; pY = e.clientY; }
        });
        canvas.addEventListener("touchstart", function (e) { isDrag = true; pX = e.touches[0].clientX; pY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { isDrag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (isDrag) {
                rotY += (e.touches[0].clientX - pX) * 0.01;
                rotX += (e.touches[0].clientY - pY) * 0.01;
                pX = e.touches[0].clientX;
                pY = e.touches[0].clientY;
            }
        });

        var playing = true;
        var playBtn = container.querySelector(".sj-3d-play");
        if (playBtn) playBtn.addEventListener("click", function () {
            playing = !playing;
            playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var resetBtn = container.querySelector(".sj-3d-reset");
        if (resetBtn) resetBtn.addEventListener("click", function () { rotX = 0; rotY = 0; });

        function animate() {
            requestAnimationFrame(animate);
            if (playing) {
                scene.rotation.y += 0.005;
                nucleus.rotation.y += 0.01;
            }
            scene.rotation.x = rotX;
            scene.rotation.y = rotY + (playing ? performance.now() * 0.0005 : 0);
            renderer.render(scene, camera);
        }
        animate();
    };

    /* ===== ANIMATION: ORIGIN OF LIFE (Vesicle Self-Assembly) ===== */
    window.initOriginLifeAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 10);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Hot spring background lighting
        scene.add(new THREE.AmbientLight(0x221100, 0.6));
        var fireLight = new THREE.PointLight(0xff7700, 2, 30);
        fireLight.position.set(5, 5, 5);
        scene.add(fireLight);
        var blueLight = new THREE.PointLight(0x0077ff, 1.5, 30);
        blueLight.position.set(-5, -5, 5);
        scene.add(blueLight);

        // Core molecules (Glowing organic polymer/RNA strand)
        var coreGroup = new THREE.Group();
        var numSegments = 30;
        var rnaSpheres = [];
        for (var i = 0; i < numSegments; i++) {
            var helixGeo = new THREE.SphereGeometry(0.12, 16, 16);
            var helixMat = new THREE.MeshPhongMaterial({ color: 0xec4899, emissive: 0xdb2777, emissiveIntensity: 0.5 });
            var m1 = new THREE.Mesh(helixGeo, helixMat);
            var a = (i / numSegments) * Math.PI * 4;
            var py = (i / numSegments) * 4 - 2;
            m1.position.set(Math.cos(a) * 0.6, py, Math.sin(a) * 0.6);
            coreGroup.add(m1);
            rnaSpheres.push(m1);
        }
        scene.add(coreGroup);

        // Lipids group
        var lipids = [];
        var lipidGroup = new THREE.Group();
        var numLipids = 120;
        var headGeo = new THREE.SphereGeometry(0.15, 8, 8);
        var headMat = new THREE.MeshPhongMaterial({ color: 0x0ea5e9 });
        var tailGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.35, 6);
        var tailMat = new THREE.MeshPhongMaterial({ color: 0xf59e0b });

        for (var j = 0; j < numLipids; j++) {
            var lg = new THREE.Group();
            
            var head = new THREE.Mesh(headGeo, headMat);
            head.position.y = 0.175;
            lg.add(head);

            var tail = new THREE.Mesh(tailGeo, tailMat);
            tail.position.y = -0.05;
            lg.add(tail);

            // Random initial placement in a large sphere
            var theta = Math.random() * Math.PI * 2;
            var phi = Math.acos((Math.random() * 2) - 1);
            var dist = 4.5 + Math.random() * 3.5;
            lg.position.set(
                Math.sin(phi) * Math.cos(theta) * dist,
                Math.sin(phi) * Math.sin(theta) * dist,
                Math.cos(phi) * dist
            );

            // Store target assembled position on a sphere of radius 2.2
            var targetX = Math.sin(phi) * Math.cos(theta) * 2.2;
            var targetY = Math.sin(phi) * Math.sin(theta) * 2.2;
            var targetZ = Math.cos(phi) * 2.2;

            // Target rotation to orient tails pointing inwards
            var targetDir = new THREE.Vector3(targetX, targetY, targetZ).normalize();
            var alignAxis = new THREE.Vector3(0, 1, 0);
            var q = new THREE.Quaternion().setFromUnitVectors(alignAxis, targetDir);
            
            lg.userData = {
                initPos: lg.position.clone(),
                targetPos: new THREE.Vector3(targetX, targetY, targetZ),
                targetRot: q,
                randRotAxis: new THREE.Vector3(Math.random(), Math.random(), Math.random()).normalize(),
                randRotSpeed: Math.random() * 0.05
            };

            lipidGroup.add(lg);
            lipids.push(lg);
        }
        scene.add(lipidGroup);

        // Control variables
        var playing = true;
        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;
        var progress = 0; // 0 to 1 (Assembly factor)

        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });

        // Touch support
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () { rX = 0; rY = 0; progress = 0; });

        function anim() {
            requestAnimationFrame(anim);
            if (playing) {
                progress += 0.003;
                if (progress > 1.2) progress = -0.3; // Loop back
                
                var assemblyFactor = Math.max(0, Math.min(1, progress));

                lipids.forEach(function (lg) {
                    // Interpolate position
                    lg.position.lerpVectors(lg.userData.initPos, lg.userData.targetPos, assemblyFactor);
                    // Interpolate rotation
                    var startRot = new THREE.Quaternion().setFromAxisAngle(lg.userData.randRotAxis, performance.now() * 0.001 * lg.userData.randRotSpeed);
                    lg.quaternion.slerpQuaternions(startRot, lg.userData.targetRot, assemblyFactor);
                });

                coreGroup.rotation.y += 0.01;
                lipidGroup.rotation.y += 0.002;
            }

            scene.rotation.x = rX;
            scene.rotation.y = rY;
            renderer.render(scene, camera);
        }
        anim();
    };

    /* ===== ANIMATION: MICROSCOPE ZOOM SIMULATOR ===== */
    window.initMicroscopeZoomAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 8);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        var light = new THREE.PointLight(0xffffff, 1.2);
        light.position.set(10, 10, 10);
        scene.add(light);

        // Group to hold current zoom visualizer models
        var modelGroup = new THREE.Group();
        scene.add(modelGroup);

        var currentZoomLevel = 1;

        // Model Builders
        function createHumanModel() {
            var g = new THREE.Group();
            var body = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 2, 8), new THREE.MeshPhongMaterial({ color: 0x38bdf8 }));
            body.position.y = -0.2;
            var head = new THREE.Mesh(new THREE.SphereGeometry(0.4, 16, 16), new THREE.MeshPhongMaterial({ color: 0x38bdf8 }));
            head.position.y = 1;
            g.add(body, head);
            return g;
        }

        function createCellModel() {
            var g = new THREE.Group();
            for (var x = -2; x <= 2; x++) {
                for (var y = -2; y <= 2; y++) {
                    var cellGeo = new THREE.BoxGeometry(0.7, 0.7, 0.3);
                    var edges = new THREE.EdgesGeometry(cellGeo);
                    var line = new THREE.LineSegments(edges, new THREE.LineBasicMaterial({ color: 0x10b981 }));
                    var fill = new THREE.Mesh(cellGeo, new THREE.MeshPhongMaterial({ color: 0x10b981, transparent: true, opacity: 0.2 }));
                    var cell = new THREE.Group();
                    cell.add(line, fill);
                    cell.position.set(x * 0.8, y * 0.8, 0);
                    g.add(cell);
                }
            }
            return g;
        }

        function createBacteriaModel() {
            var g = new THREE.Group();
            var body = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 1.8, 16), new THREE.MeshPhongMaterial({ color: 0xf59e0b }));
            body.rotation.z = Math.PI / 2;
            
            var curvePoints = [];
            for (var i = 0; i < 10; i++) {
                curvePoints.push(new THREE.Vector3(-0.9 - i*0.2, Math.sin(i*0.8)*0.2, 0));
            }
            var tubeGeo = new THREE.TubeGeometry(new THREE.CatmullRomCurve3(curvePoints), 32, 0.05, 8, false);
            var flagella = new THREE.Mesh(tubeGeo, new THREE.MeshPhongMaterial({ color: 0xd97706 }));
            
            g.add(body, flagella);
            return g;
        }

        function createVirusModel() {
            var g = new THREE.Group();
            var head = new THREE.Mesh(new THREE.IcosahedronGeometry(0.7, 0), new THREE.MeshPhongMaterial({ color: 0xa855f7 }));
            head.position.y = 0.8;
            var sheath = new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.8, 8), new THREE.MeshPhongMaterial({ color: 0xc084fc }));
            sheath.position.y = 0;
            g.add(head, sheath);

            for (var i = 0; i < 6; i++) {
                var leg = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.8, 4), new THREE.MeshPhongMaterial({ color: 0x9333ea }));
                leg.position.y = -0.4;
                var angle = (i / 6) * Math.PI * 2;
                leg.position.x = Math.cos(angle) * 0.3;
                leg.position.z = Math.sin(angle) * 0.3;
                leg.rotation.z = Math.cos(angle) * 0.5;
                g.add(leg);
            }
            return g;
        }

        function createAtomModel() {
            var g = new THREE.Group();
            for (var i = 0; i < 6; i++) {
                var n = new THREE.Mesh(new THREE.SphereGeometry(0.2, 16, 16), new THREE.MeshPhongMaterial({ color: i % 2 === 0 ? 0xef4444 : 0x64748b }));
                n.position.set(Math.random()*0.2 - 0.1, Math.random()*0.2 - 0.1, Math.random()*0.2 - 0.1);
                g.add(n);
            }
            var ringGeo = new THREE.TorusGeometry(1.8, 0.02, 8, 64);
            var ringMat = new THREE.MeshBasicMaterial({ color: 0x475569, transparent: true, opacity: 0.5 });
            var r1 = new THREE.Mesh(ringGeo, ringMat);
            r1.rotation.x = Math.PI / 4;
            var r2 = new THREE.Mesh(ringGeo, ringMat);
            r2.rotation.y = Math.PI / 4;
            g.add(r1, r2);
            return g;
        }

        function updateModel(zoom) {
            modelGroup.clear();
            var m;
            switch(zoom) {
                case 1: m = createHumanModel(); break;
                case 2: m = createCellModel(); break;
                case 3: m = createBacteriaModel(); break;
                case 4: m = createVirusModel(); break;
                case 5: m = createAtomModel(); break;
            }
            modelGroup.add(m);
        }

        updateModel(1);

        var slider = container.querySelector("#microscope-zoom-slider");
        var zoomLabel = container.querySelector("#zoom-label");
        
        var labels = [
            "Scale: Human Height (1.7 m) - Naked Eye limit is 0.1 mm",
            "Scale: Onion Peel Cells (200 µm) - Light Microscope required",
            "Scale: Mitochondria / Bacteria (1 µm) - Electron Microscope detail",
            "Scale: Virus Structure (100 nm) - Nanometre scale details",
            "Scale: Oxygen Atom / Molecules (0.1 nm) - Chemical scale"
        ];

        if (slider) {
            slider.addEventListener("input", function (e) {
                var val = parseInt(e.target.value);
                currentZoomLevel = val;
                if (zoomLabel) zoomLabel.textContent = labels[val - 1];
                updateModel(val);
            });
        }

        var playing = true;
        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;

        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });

        // Touch support
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () {
            rX = 0; rY = 0;
            if (slider) { slider.value = 1; slider.dispatchEvent(new Event('input')); }
        });

        function anim() {
            requestAnimationFrame(anim);
            if (playing) {
                modelGroup.rotation.y += 0.007;
            }
            modelGroup.rotation.x = rX;
            modelGroup.rotation.y = rY + (playing ? performance.now() * 0.0005 : 0);
            renderer.render(scene, camera);
        }
        anim();
    };

    /* ===== ANIMATION: FLUID MOSAIC MEMBRANE MODEL ===== */
    window.initFluidMosaicAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 4, 9);
        camera.lookAt(0, 0, 0);
        
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        var l = new THREE.PointLight(0xffffff, 1.2);
        l.position.set(10, 10, 10);
        scene.add(l);

        var lipidsGroup = new THREE.Group();
        scene.add(lipidsGroup);

        var lipidsArray = [];
        var numX = 9, numZ = 6;
        var spacingX = 1.0, spacingZ = 0.9;

        var headGeo = new THREE.SphereGeometry(0.16, 12, 12);
        var tailGeo = new THREE.CylinderGeometry(0.02, 0.01, 0.5, 6);
        
        var headMat = new THREE.MeshPhongMaterial({ color: 0x0ea5e9, shininess: 80 });
        var tailMat = new THREE.MeshPhongMaterial({ color: 0xf59e0b });

        for (var x = 0; x < numX; x++) {
            for (var z = 0; z < numZ; z++) {
                var px = (x - (numX - 1) / 2) * spacingX;
                var pz = (z - (numZ - 1) / 2) * spacingZ;

                var upLipid = new THREE.Group();
                var upHead = new THREE.Mesh(headGeo, headMat);
                upHead.position.y = 0.5;
                var upTail = new THREE.Mesh(tailGeo, tailMat);
                upTail.position.y = 0.15;
                upLipid.add(upHead, upTail);
                upLipid.position.set(px, 1.0, pz);
                lipidsGroup.add(upLipid);

                var downLipid = new THREE.Group();
                var downHead = new THREE.Mesh(headGeo, headMat);
                downHead.position.y = -0.5;
                var downTail = new THREE.Mesh(tailGeo, tailMat);
                downTail.position.y = -0.15;
                downLipid.add(downHead, downTail);
                downLipid.position.set(px + 0.1, -1.0, pz + 0.1);
                lipidsGroup.add(downLipid);

                lipidsArray.push({
                    group: upLipid,
                    baseX: px,
                    baseZ: pz,
                    baseY: 1.0,
                    phase: (x + z) * 0.5
                });
                lipidsArray.push({
                    group: downLipid,
                    baseX: px + 0.1,
                    baseZ: pz + 0.1,
                    baseY: -1.0,
                    phase: (x + z) * 0.5 + Math.PI
                });
            }
        }

        var proteinMat = new THREE.MeshPhongMaterial({ color: 0x10b981, specular: 0x222222, shininess: 50 });
        var protein = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 0.7, 2.6, 16), proteinMat);
        protein.position.set(0, 0, 0);
        scene.add(protein);

        var ringGeo = new THREE.TorusGeometry(0.5, 0.1, 8, 16);
        var ringMat = new THREE.MeshPhongMaterial({ color: 0x047857 });
        var ringTop = new THREE.Mesh(ringGeo, ringMat);
        ringTop.rotation.x = Math.PI / 2;
        ringTop.position.y = 1.31;
        protein.add(ringTop);

        var playing = true;
        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;

        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });

        // Touch support
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () { rX = 0; rY = 0; });

        function anim() {
            requestAnimationFrame(anim);
            if (playing) {
                var t = performance.now() * 0.0025;
                lipidsArray.forEach(function (l) {
                    l.group.position.y = l.baseY + Math.sin(t + l.phase) * 0.08;
                    l.group.position.x = l.baseX + Math.cos(t * 0.5 + l.phase) * 0.05;
                });
                protein.position.x = Math.sin(t * 0.3) * 0.8;
                protein.position.z = Math.cos(t * 0.2) * 0.5;
                protein.rotation.y += 0.002;
            }

            scene.rotation.x = rX;
            scene.rotation.y = rY + (playing ? performance.now() * 0.0001 : 0);
            renderer.render(scene, camera);
        }
        anim();
    };

    /* ===== ANIMATION: OSMOSIS & TONICITY ===== */
    window.initOsmosisTonicityAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 9);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        var l = new THREE.PointLight(0xffffff, 1);
        l.position.set(10, 10, 10);
        scene.add(l);

        var cellGeo = new THREE.SphereGeometry(2, 64, 64);
        var cellMat = new THREE.MeshPhongMaterial({
            color: 0x0f9d8a, transparent: true, opacity: 0.45, side: THREE.DoubleSide
        });
        var cell = new THREE.Mesh(cellGeo, cellMat);
        scene.add(cell);

        var insideGroup = new THREE.Group();
        scene.add(insideGroup);
        for (var i = 0; i < 15; i++) {
            var m = new THREE.Mesh(new THREE.SphereGeometry(0.18, 16, 16), new THREE.MeshPhongMaterial({ color: 0x10b981 }));
            var dist = Math.random() * 1.2;
            var theta = Math.random() * Math.PI * 2;
            var phi = Math.acos((Math.random() * 2) - 1);
            m.position.set(
                Math.sin(phi) * Math.cos(theta) * dist,
                Math.sin(phi) * Math.sin(theta) * dist,
                Math.cos(phi) * dist
            );
            insideGroup.add(m);
        }

        var waters = [];
        var waterGroup = new THREE.Group();
        scene.add(waterGroup);
        var numWaters = 60;
        for (var w = 0; w < numWaters; w++) {
            var water = new THREE.Mesh(new THREE.SphereGeometry(0.08, 8, 8), new THREE.MeshPhongMaterial({ color: 0x3b82f6 }));
            var theta = Math.random() * Math.PI * 2;
            var phi = Math.acos((Math.random() * 2) - 1);
            var dist = 1.0 + Math.random() * 5.0;
            water.position.set(
                Math.sin(phi) * Math.cos(theta) * dist,
                Math.sin(phi) * Math.sin(theta) * dist,
                Math.cos(phi) * dist
            );
            water.userData = {
                angle: theta,
                phi: phi,
                dist: dist,
                speed: 0.05 + Math.random() * 0.05
            };
            waterGroup.add(water);
            waters.push(water);
        }

        var currentMode = "iso";
        var targetCellScale = 1.0;

        function updateTonicityMode(mode) {
            currentMode = mode;
            container.querySelectorAll(".sj-3d-btn").forEach(function (b) {
                b.style.background = "#475569";
            });
            var activeBtn = container.querySelector("#btn-" + mode);
            if (activeBtn) activeBtn.style.background = "#0f9d8a";

            if (mode === "hypo") {
                targetCellScale = 1.45;
            } else if (mode === "hyper") {
                targetCellScale = 0.6;
            } else {
                targetCellScale = 1.0;
            }
        }

        var btnHypo = container.querySelector("#btn-hypo");
        var btnIso = container.querySelector("#btn-iso");
        var btnHyper = container.querySelector("#btn-hyper");

        if (btnHypo) btnHypo.addEventListener("click", function () { updateTonicityMode("hypo"); });
        if (btnIso) btnIso.addEventListener("click", function () { updateTonicityMode("iso"); });
        if (btnHyper) btnHyper.addEventListener("click", function () { updateTonicityMode("hyper"); });

        var playing = true;
        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;

        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });

        // Touch support
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () { rX = 0; rY = 0; updateTonicityMode("iso"); });

        function anim() {
            requestAnimationFrame(anim);
            if (playing) {
                var cScale = cell.scale.x;
                var lerpedScale = THREE.MathUtils.lerp(cScale, targetCellScale, 0.05);
                cell.scale.set(lerpedScale, lerpedScale, lerpedScale);

                waters.forEach(function (w) {
                    if (currentMode === "hypo") {
                        w.userData.dist -= w.userData.speed;
                        if (w.userData.dist < 0.2) w.userData.dist = 5.0;
                    } else if (currentMode === "hyper") {
                        w.userData.dist += w.userData.speed;
                        if (w.userData.dist > 5.0) w.userData.dist = 0.2;
                    } else {
                        w.userData.dist += (Math.random() - 0.5) * 0.05;
                        if (w.userData.dist < 0.1) w.userData.dist = 4.0;
                        if (w.userData.dist > 5.5) w.userData.dist = 1.0;
                    }
                    
                    var th = w.userData.angle;
                    var ph = w.userData.phi;
                    var d = w.userData.dist;
                    w.position.set(
                        Math.sin(ph) * Math.cos(th) * d,
                        Math.sin(ph) * Math.sin(th) * d,
                        Math.cos(ph) * d
                    );
                });

                insideGroup.rotation.y += 0.005;
            }
            scene.rotation.x = rX;
            scene.rotation.y = rY + (playing ? performance.now() * 0.0003 : 0);
            renderer.render(scene, camera);
        }
        anim();
    };

    /* ===== ANIMATION: CELL DIVISION (Mitosis & Meiosis) ===== */
    window.initCellDivisionAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 10);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        var l = new THREE.PointLight(0xffffff, 1.2);
        l.position.set(10, 10, 10);
        scene.add(l);

        var divisionMode = "mitosis";

        var rootGroup = new THREE.Group();
        scene.add(rootGroup);

        var membranes = [];
        var chromosomes = [];

        function rebuildDivisionModel() {
            rootGroup.clear();
            membranes = [];
            chromosomes = [];

            if (divisionMode === "mitosis") {
                var c1 = new THREE.Mesh(new THREE.SphereGeometry(1.6, 32, 32), new THREE.MeshPhongMaterial({ color: 0x0f9d8a, transparent: true, opacity: 0.25 }));
                var c2 = new THREE.Mesh(new THREE.SphereGeometry(1.6, 32, 32), new THREE.MeshPhongMaterial({ color: 0x0f9d8a, transparent: true, opacity: 0.25 }));
                rootGroup.add(c1, c2);
                membranes.push(c1, c2);

                var chrom1 = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 1.2, 12), new THREE.MeshPhongMaterial({ color: 0xef4444 }));
                chrom1.rotation.z = Math.PI / 4;
                var chrom2 = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 1.2, 12), new THREE.MeshPhongMaterial({ color: 0x3b82f6 }));
                chrom2.rotation.z = -Math.PI / 4;
                
                c1.add(chrom1);
                c2.add(chrom2);
                chromosomes.push(chrom1, chrom2);

            } else {
                for (var i = 0; i < 4; i++) {
                    var c = new THREE.Mesh(new THREE.SphereGeometry(1.0, 16, 16), new THREE.MeshPhongMaterial({ color: 0xec4899, transparent: true, opacity: 0.25 }));
                    rootGroup.add(c);
                    membranes.push(c);

                    var chrom = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 0.7, 8), new THREE.MeshPhongMaterial({ color: i % 2 === 0 ? 0xef4444 : 0x3b82f6 }));
                    chrom.rotation.z = (Math.random() - 0.5) * 1.5;
                    c.add(chrom);
                    chromosomes.push(chrom);
                }
            }
        }

        rebuildDivisionModel();

        var btnMitosis = container.querySelector("#btn-mitosis");
        var btnMeiosis = container.querySelector("#btn-meiosis");

        function updateDivisionMode(mode) {
            divisionMode = mode;
            container.querySelectorAll(".sj-3d-btn").forEach(function (b) {
                b.style.background = "#475569";
            });
            var activeBtn = container.querySelector("#btn-" + mode);
            if (activeBtn) activeBtn.style.background = mode === "mitosis" ? "#ec4899" : "#a855f7";
            rebuildDivisionModel();
        }

        if (btnMitosis) btnMitosis.addEventListener("click", function () { updateDivisionMode("mitosis"); });
        if (btnMeiosis) btnMeiosis.addEventListener("click", function () { updateDivisionMode("meiosis"); });

        var playing = true;
        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;

        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });

        // Touch support
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () { rX = 0; rY = 0; updateDivisionMode("mitosis"); });

        function anim() {
            requestAnimationFrame(anim);
            if (playing) {
                var t = performance.now() * 0.0015;
                
                if (divisionMode === "mitosis") {
                    var d = (Math.sin(t) + 1) * 1.5;
                    membranes[0].position.set(-d, 0, 0);
                    membranes[1].position.set(d, 0, 0);
                    chromosomes[0].rotation.y = t;
                    chromosomes[1].rotation.y = -t;
                } else {
                    var d = (Math.sin(t) + 1) * 1.2;
                    membranes[0].position.set(-d, -d, 0);
                    membranes[1].position.set(d, -d, 0);
                    membranes[2].position.set(-d, d, 0);
                    membranes[3].position.set(d, d, 0);
                }
            }
            rootGroup.rotation.x = rX;
            rootGroup.rotation.y = rY + (playing ? performance.now() * 0.0002 : 0);
            renderer.render(scene, camera);
        }
        anim();
    };

})();
