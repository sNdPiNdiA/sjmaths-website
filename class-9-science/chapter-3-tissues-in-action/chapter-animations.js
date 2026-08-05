(function () {
    "use strict";

    /* ===== ANIMATION: VASCULAR CONDUCTION (Xylem vs Phloem) ===== */
    window.initXylemPhloemAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a); // Deep slate background
        var camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 15);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Xylem Tube (Left)
        var xylemTubeGeo = new THREE.CylinderGeometry(0.8, 0.8, 8, 32, 1, true);
        var xylemTubeMat = new THREE.MeshPhongMaterial({
            color: 0x0284c7,
            transparent: true,
            opacity: 0.35,
            side: THREE.DoubleSide
        });
        var xylemTube = new THREE.Mesh(xylemTubeGeo, xylemTubeMat);
        xylemTube.position.set(-2.5, 0, 0);
        scene.add(xylemTube);

        // Phloem Tube (Right)
        var phloemTubeGeo = new THREE.CylinderGeometry(0.8, 0.8, 8, 32, 1, true);
        var phloemTubeMat = new THREE.MeshPhongMaterial({
            color: 0xeab308,
            transparent: true,
            opacity: 0.35,
            side: THREE.DoubleSide
        });
        var phloemTube = new THREE.Mesh(phloemTubeGeo, phloemTubeMat);
        phloemTube.position.set(2.5, 0, 0);
        scene.add(phloemTube);

        // Labels
        var labelContainer = document.createElement("div");
        labelContainer.style.cssText = "position:absolute; top:45px; left:0; width:100%; display:flex; justify-content:space-around; pointer-events:none; color:#f8fafc; font-family:sans-serif; font-size:0.8rem; font-weight:700; text-transform:uppercase;";
        labelContainer.innerHTML = `
            <span>Xylem (Water 1-Way)</span>
            <span>Phloem (Food 2-Way)</span>
        `;
        container.appendChild(labelContainer);

        // Particles
        var waterParticles = [];
        var foodParticles = [];
        var numParticles = 25;

        // Xylem Particles (Water: Blue spheres moving UP only)
        for (var i = 0; i < numParticles; i++) {
            var geo = new THREE.SphereGeometry(0.12, 8, 8);
            var mat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
            var mesh = new THREE.Mesh(geo, mat);
            mesh.position.set(
                -2.5 + (Math.random() - 0.5) * 0.8,
                (Math.random() - 0.5) * 7.5,
                (Math.random() - 0.5) * 0.8
            );
            scene.add(mesh);
            waterParticles.push(mesh);
        }

        // Phloem Particles (Food: Yellow/Orange spheres moving UP and DOWN)
        for (var i = 0; i < numParticles; i++) {
            var geo = new THREE.SphereGeometry(0.15, 8, 8);
            var mat = new THREE.MeshBasicMaterial({ color: 0xfacc15 });
            var mesh = new THREE.Mesh(geo, mat);
            mesh.position.set(
                2.5 + (Math.random() - 0.5) * 0.8,
                (Math.random() - 0.5) * 7.5,
                (Math.random() - 0.5) * 0.8
            );
            // assign random direction (-1 or 1)
            mesh.userData = { dir: Math.random() > 0.5 ? 1 : -1 };
            scene.add(mesh);
            foodParticles.push(mesh);
        }

        // Lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.7));
        var light = new THREE.DirectionalLight(0xffffff, 1.0);
        light.position.set(5, 5, 5);
        scene.add(light);

        // Speed Sliders
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; font-family: sans-serif; font-size: 0.9rem;";
        controlsDiv.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <label style="font-weight:700; color:#1e293b;">Flow Velocity: <span id="lbl-speed">1.0</span>x</label>
                <input type="range" id="slide-speed" min="0.1" max="3.0" step="0.1" value="1.0" style="width:60%;">
            </div>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var slideSpeed = controlsDiv.querySelector("#slide-speed");
        var lblSpeed = controlsDiv.querySelector("#lbl-speed");
        var speedMultiplier = 1.0;

        slideSpeed.addEventListener("input", function (e) {
            speedMultiplier = parseFloat(e.target.value);
            lblSpeed.textContent = speedMultiplier.toFixed(1);
        });

        // Controls
        var playing = true;
        var playBtn = container.querySelector(".sj-3d-play");
        var resetBtn = container.querySelector(".sj-3d-reset");

        if (playBtn) {
            playBtn.addEventListener("click", function () {
                playing = !playing;
                playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
            });
        }
        if (resetBtn) {
            resetBtn.addEventListener("click", function () {
                waterParticles.forEach(function (p) { p.position.y = (Math.random() - 0.5) * 7.5; });
                foodParticles.forEach(function (p) { p.position.y = (Math.random() - 0.5) * 7.5; });
            });
        }

        // Drag controls
        var rotX = 0, rotY = 0, isDrag = false, pX = 0, pY = 0;
        canvas.addEventListener("mousedown", function (e) { isDrag = true; pX = e.clientX; pY = e.clientY; });
        canvas.addEventListener("mouseup", function () { isDrag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (isDrag) { rotY += (e.clientX - pX) * 0.01; rotX += (e.clientY - pY) * 0.01; pX = e.clientX; pY = e.clientY; }
        });

        function animate() {
            requestAnimationFrame(animate);

            if (playing) {
                var delta = 0.02 * speedMultiplier;

                // Move Xylem particles upward
                waterParticles.forEach(function (p) {
                    p.position.y += delta;
                    if (p.position.y > 4.0) {
                        p.position.y = -4.0;
                    }
                });

                // Move Phloem particles bidirectional
                foodParticles.forEach(function (p) {
                    p.position.y += delta * p.userData.dir;
                    if (p.position.y > 4.0) {
                        p.position.y = -4.0;
                    } else if (p.position.y < -4.0) {
                        p.position.y = 4.0;
                    }
                });
            }

            scene.rotation.y = rotY;
            scene.rotation.x = rotX;
            renderer.render(scene, camera);
        }
        animate();
    };

    /* ===== ANIMATION: NEURON ELECTRICAL IMPULSE ===== */
    window.initNeuronSignalAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a);
        var camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 15);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Neuron structure groups
        var cellBodyGeo = new THREE.SphereGeometry(1.2, 32, 32);
        var cellBodyMat = new THREE.MeshPhongMaterial({ color: 0x4f46e5 });
        var cellBody = new THREE.Mesh(cellBodyGeo, cellBodyMat);
        cellBody.position.set(-5, 0, 0);
        scene.add(cellBody);

        // Axon (long tube)
        var axonGeo = new THREE.CylinderGeometry(0.2, 0.2, 8, 16);
        var axonMat = new THREE.MeshPhongMaterial({ color: 0x6366f1 });
        var axon = new THREE.Mesh(axonGeo, axonMat);
        axon.rotation.z = -Math.PI / 2;
        axon.position.set(-0.5, 0, 0);
        scene.add(axon);

        // Myelin Sheaths (3 cylindrical beads around axon)
        var sheathPositions = [-3, -0.5, 2];
        sheathPositions.forEach(function (pos) {
            var sheathGeo = new THREE.CylinderGeometry(0.35, 0.35, 1.8, 16);
            var sheathMat = new THREE.MeshPhongMaterial({ color: 0xa5b4fc, transparent: true, opacity: 0.75 });
            var sheath = new THREE.Mesh(sheathGeo, sheathMat);
            sheath.rotation.z = -Math.PI / 2;
            sheath.position.set(pos, 0, 0);
            scene.add(sheath);
        });

        // Axon Terminals (Dendrites / Branches at the end)
        var termGeo = new THREE.CylinderGeometry(0.05, 0.05, 1.5, 8);
        var termMat = new THREE.MeshPhongMaterial({ color: 0x4f46e5 });
        var term1 = new THREE.Mesh(termGeo, termMat);
        term1.position.set(3.8, 0.5, 0);
        term1.rotation.z = -Math.PI / 4;
        scene.add(term1);

        var term2 = new THREE.Mesh(termGeo, termMat);
        term2.position.set(3.8, -0.5, 0);
        term2.rotation.z = Math.PI / 4;
        scene.add(term2);

        // Electrical Impulse Pulse (Yellow Sphere)
        var pulseGeo = new THREE.SphereGeometry(0.22, 16, 16);
        var pulseMat = new THREE.MeshBasicMaterial({ color: 0xfacc15 });
        var pulse = new THREE.Mesh(pulseGeo, pulseMat);
        pulse.position.set(-5, 0, 0);
        scene.add(pulse);

        // Lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        var light = new THREE.PointLight(0xffffff, 1.2);
        light.position.set(-2, 3, 5);
        scene.add(light);

        // Controls
        var playing = true;
        var triggerImpulse = false;
        var t = 0; // parameter along axon path

        var playBtn = container.querySelector(".sj-3d-play");
        var resetBtn = container.querySelector(".sj-3d-reset");

        if (playBtn) {
            playBtn.addEventListener("click", function () {
                playing = !playing;
                playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
            });
        }
        if (resetBtn) {
            resetBtn.addEventListener("click", function () {
                t = 0;
                pulse.position.set(-5, 0, 0);
            });
        }

        // Trigger Button UI
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; text-align: center;";
        controlsDiv.innerHTML = `
            <button id="btn-impulse" class="sj-btn" style="background:#eab308; color:#000; border:none; padding:10px 20px; font-weight:700; font-family:sans-serif; border-radius:50px; cursor:pointer; transition:0.2s;">
                <i class="fas fa-bolt"></i> Trigger Action Potential
            </button>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var btnImpulse = controlsDiv.querySelector("#btn-impulse");
        btnImpulse.addEventListener("click", function () {
            t = 0; // restart pulse
            triggerImpulse = true;
        });

        // Drag controls
        var rotX = 0, rotY = 0, isDrag = false, pX = 0, pY = 0;
        canvas.addEventListener("mousedown", function (e) { isDrag = true; pX = e.clientX; pY = e.clientY; });
        canvas.addEventListener("mouseup", function () { isDrag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (isDrag) { rotY += (e.clientX - pX) * 0.01; rotX += (e.clientY - pY) * 0.01; pX = e.clientX; pY = e.clientY; }
        });

        function animate() {
            requestAnimationFrame(animate);

            if (playing) {
                t += 0.015;
                if (t > 1.0) {
                    t = 0; // loop pulse
                }

                // Axon path is from X = -5 to X = 4.
                var startX = -5;
                var endX = 4;
                var currentX = startX + (endX - startX) * t;
                pulse.position.x = currentX;

                // Introduce saltatory conduction jump (voltage pulse jumps node-to-node)
                // We add a tiny y-axis offset wobble between nodes
                var nodeOffset = Math.sin(t * Math.PI * 3) * 0.25;
                pulse.position.y = Math.max(0, nodeOffset);
            }

            scene.rotation.y = rotY;
            scene.rotation.x = rotX;
            renderer.render(scene, camera);
        }
        animate();
    };

    /* ===== ANIMATION: JOINT MOVEMENT AND MUSCLE ACTION ===== */
    window.initJointMovementAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a);
        var camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 1, 10);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        var light = new THREE.DirectionalLight(0xffffff, 0.9);
        light.position.set(5, 10, 7);
        scene.add(light);

        // Group to hold Hinge model
        var hingeGroup = new THREE.Group();
        scene.add(hingeGroup);

        // Group to hold Ball & Socket model
        var ballSocketGroup = new THREE.Group();
        scene.add(ballSocketGroup);
        ballSocketGroup.visible = false;

        // --- HINGE JOINT MODEL ---
        // Upper Arm Bone (Fixed)
        var upperBoneGeo = new THREE.CylinderGeometry(0.25, 0.25, 3.8, 16);
        var boneMat = new THREE.MeshPhongMaterial({ color: 0xe2e8f0, roughness: 0.2 });
        var upperBone = new THREE.Mesh(upperBoneGeo, boneMat);
        upperBone.position.set(0, 2, 0);
        hingeGroup.add(upperBone);

        // Elbow Joint Pivot point
        var pivotGeo = new THREE.SphereGeometry(0.4, 16, 16);
        var pivotMat = new THREE.MeshPhongMaterial({ color: 0x94a3b8 });
        var pivot = new THREE.Mesh(pivotGeo, pivotMat);
        pivot.position.set(0, 0, 0);
        hingeGroup.add(pivot);

        // Lower Arm Bone (Rotatable Group)
        var lowerBoneGroup = new THREE.Group();
        lowerBoneGroup.position.set(0, 0, 0);
        hingeGroup.add(lowerBoneGroup);

        var lowerBone = new THREE.Mesh(upperBoneGeo, boneMat);
        lowerBone.position.set(0, -1.9, 0);
        lowerBoneGroup.add(lowerBone);

        // Muscle Biceps (Front)
        var bicepGeo = new THREE.CylinderGeometry(0.35, 0.35, 2.5, 16);
        var muscleMat = new THREE.MeshPhongMaterial({ color: 0xef4444, shininess: 30 });
        var biceps = new THREE.Mesh(bicepGeo, muscleMat);
        biceps.position.set(-0.6, 1.8, 0);
        hingeGroup.add(biceps);

        // Muscle Triceps (Back)
        var triceps = new THREE.Mesh(bicepGeo, muscleMat);
        triceps.position.set(0.6, 1.8, 0);
        hingeGroup.add(triceps);

        // --- BALL & SOCKET JOINT MODEL ---
        // Shoulder Socket (Cup)
        var socketGeo = new THREE.SphereGeometry(0.8, 32, 16, 0, Math.PI * 2, 0, Math.PI / 2);
        var socketMat = new THREE.MeshPhongMaterial({ color: 0x64748b, transparent: true, opacity: 0.6, side: THREE.DoubleSide });
        var socket = new THREE.Mesh(socketGeo, socketMat);
        socket.rotation.x = Math.PI; // turn it into a cup pointing down
        socket.position.set(0, 2, 0);
        ballSocketGroup.add(socket);

        // Ball Pivot
        var ballGeo = new THREE.SphereGeometry(0.5, 32, 32);
        var ballMat = new THREE.MeshPhongMaterial({ color: 0xcbd5e1 });
        var ball = new THREE.Mesh(ballGeo, ballMat);
        ball.position.set(0, 2, 0);
        ballSocketGroup.add(ball);

        // Arm bone attached to ball (Rotatable Group)
        var armBoneGroup = new THREE.Group();
        armBoneGroup.position.set(0, 2, 0);
        ballSocketGroup.add(armBoneGroup);

        var armBone = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 3.8, 16), boneMat);
        armBone.position.set(0, -1.9, 0);
        armBoneGroup.add(armBone);

        // Controls / UI
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; font-family: sans-serif; font-size: 0.9rem; text-align: center;";
        controlsDiv.innerHTML = `
            <div style="display:flex; justify-content:center; gap:10px; margin-bottom:12px;">
                <button id="btn-mode-hinge" class="sj-3d-btn" style="background:#0f9d8a; color:white; padding:6px 12px; font-size:0.75rem; border-radius:20px; border:none; cursor:pointer;">Hinge Joint (Elbow)</button>
                <button id="btn-mode-ball" class="sj-3d-btn" style="background:#475569; color:white; padding:6px 12px; font-size:0.75rem; border-radius:20px; border:none; cursor:pointer;">Ball & Socket (Shoulder)</button>
            </div>
            <div style="display:flex; justify-content:center; align-items:center; gap:10px;">
                <label style="font-weight:700; color:#1e293b;">Rotation / Flexion: </label>
                <input type="range" id="slide-flex" min="0" max="130" value="0" style="width:50%;">
                <span id="lbl-flex">0</span>&deg;
            </div>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var btnHinge = controlsDiv.querySelector("#btn-mode-hinge");
        var btnBall = controlsDiv.querySelector("#btn-mode-ball");
        var slideFlex = controlsDiv.querySelector("#slide-flex");
        var lblFlex = controlsDiv.querySelector("#lbl-flex");

        var currentMode = "hinge";
        var angleVal = 0; // in degrees
        var playing = true;
        var playTime = 0;

        btnHinge.addEventListener("click", function () {
            currentMode = "hinge";
            hingeGroup.visible = true;
            ballSocketGroup.visible = false;
            btnHinge.style.background = "#0f9d8a";
            btnBall.style.background = "#475569";
            slideFlex.min = "0";
            slideFlex.max = "130";
            slideFlex.value = "0";
            lblFlex.textContent = "0";
            angleVal = 0;
            camera.position.set(0, 1, 10);
            camera.lookAt(0, 1, 0);
        });

        btnBall.addEventListener("click", function () {
            currentMode = "ball";
            hingeGroup.visible = false;
            ballSocketGroup.visible = true;
            btnHinge.style.background = "#475569";
            btnBall.style.background = "#0f9d8a";
            slideFlex.min = "-60";
            slideFlex.max = "60";
            slideFlex.value = "0";
            lblFlex.textContent = "0";
            angleVal = 0;
            camera.position.set(0, 1, 10);
            camera.lookAt(0, 1, 0);
        });

        var manualControl = false;
        slideFlex.addEventListener("input", function (e) {
            manualControl = true;
            angleVal = parseFloat(e.target.value);
            lblFlex.textContent = Math.round(angleVal);
        });

        var playBtn = container.querySelector(".sj-3d-play");
        var resetBtn = container.querySelector(".sj-3d-reset");

        if (playBtn) {
            playBtn.addEventListener("click", function () {
                playing = !playing;
                playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
            });
        }
        if (resetBtn) {
            resetBtn.addEventListener("click", function () {
                manualControl = false;
                slideFlex.value = "0";
                lblFlex.textContent = "0";
                angleVal = 0;
            });
        }

        // Drag controls
        var rotX = 0, rotY = 0, isDrag = false, pX = 0, pY = 0;
        canvas.addEventListener("mousedown", function (e) { isDrag = true; pX = e.clientX; pY = e.clientY; });
        canvas.addEventListener("mouseup", function () { isDrag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (isDrag) { rotY += (e.clientX - pX) * 0.01; rotX += (e.clientY - pY) * 0.01; pX = e.clientX; pY = e.clientY; }
        });

        function animate() {
            requestAnimationFrame(animate);

            if (playing && !manualControl) {
                playTime += 0.025;
                if (currentMode === "hinge") {
                    // swing between 0 and 110 degrees
                    angleVal = (Math.sin(playTime) + 1) * 55;
                } else {
                    // circular rotation swing
                    angleVal = Math.sin(playTime) * 45;
                }
                slideFlex.value = angleVal;
                lblFlex.textContent = Math.round(angleVal);
            }

            var rad = angleVal * Math.PI / 180;

            if (currentMode === "hinge") {
                // Rotate the lower arm bone around pivot
                lowerBoneGroup.rotation.z = -rad;

                // Animate Biceps (bulge & shorten)
                // When bent, biceps gets shorter and wider
                var scaleBulge = 1.0 + (angleVal / 130) * 0.7; // bulge biceps
                var scaleLen = 1.0 - (angleVal / 130) * 0.3; // shorten
                biceps.scale.set(scaleBulge, scaleLen, scaleBulge);
                biceps.position.y = 1.8 - (angleVal / 130) * 0.45;
                biceps.position.x = -0.6 + (angleVal / 130) * 0.15;

                // Animate Triceps (stretch & thin)
                var scaleTricepsBulge = 1.0 - (angleVal / 130) * 0.2;
                var scaleTricepsLen = 1.0 + (angleVal / 130) * 0.15;
                triceps.scale.set(scaleTricepsBulge, scaleTricepsLen, scaleTricepsBulge);
                triceps.position.y = 1.8 + (angleVal / 130) * 0.25;
                triceps.position.x = 0.6 + (angleVal / 130) * 0.05;

            } else {
                // Ball and socket rotation (pitch and roll)
                armBoneGroup.rotation.z = -rad;
                armBoneGroup.rotation.x = Math.cos(playTime) * 0.3;
            }

            scene.rotation.y = rotY;
            scene.rotation.x = rotX;
            renderer.render(scene, camera);
        }
        animate();
    };

})();
