(function () {
    "use strict";

    /* ===== ANIMATION 1: POSITION VS TIME GRAPH PLOTTER ===== */
    window.initPositionTimeGraphAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a);
        
        // Orthographic camera for flat 2D layout representation
        var camera = new THREE.OrthographicCamera(-8, 8, 5, -5, 0.1, 100);
        camera.position.set(0, 0, 10);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Track line (from X=-7 to X=-1)
        var trackGeo = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(-7, 0, 0),
            new THREE.Vector3(-1, 0, 0)
        ]);
        var trackMat = new THREE.LineBasicMaterial({ color: 0x64748b, linewidth: 2 });
        var track = new THREE.Line(trackGeo, trackMat);
        scene.add(track);

        // Tick marks on track
        for (var i = 0; i <= 6; i++) {
            var x = -7 + i;
            var tickGeo = new THREE.BufferGeometry().setFromPoints([
                new THREE.Vector3(x, -0.15, 0),
                new THREE.Vector3(x, 0.15, 0)
            ]);
            var tick = new THREE.Line(tickGeo, trackMat);
            scene.add(tick);
        }

        // Runner (Blue Sphere representing the athlete)
        var runnerGeo = new THREE.SphereGeometry(0.2, 16, 16);
        var runnerMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
        var runner = new THREE.Mesh(runnerGeo, runnerMat);
        runner.position.set(-7, 0, 0);
        scene.add(runner);

        // Graph Axes on the right side (from X=1 to X=7, Y=-4 to Y=4)
        var axesGeo = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(1, -3, 0),
            new THREE.Vector3(7, -3, 0), // X axis (Time)
            new THREE.Vector3(1, -3, 0),
            new THREE.Vector3(1, 3, 0)   // Y axis (Position)
        ]);
        var axesMat = new THREE.LineBasicMaterial({ color: 0xe2e8f0 });
        var axes = new THREE.Line(axesGeo, axesMat);
        scene.add(axes);

        // Plotted line graph
        var plotPoints = [];
        var plotGeometry = new THREE.BufferGeometry();
        var plotMaterial = new THREE.LineBasicMaterial({ color: 0xfacc15, linewidth: 3 });
        var plotLine = new THREE.Line(plotGeometry, plotMaterial);
        scene.add(plotLine);

        // Markers/Labels
        var labelContainer = document.createElement("div");
        labelContainer.style.cssText = "position:absolute; bottom:55px; left:0; width:100%; display:flex; justify-content:space-around; pointer-events:none; color:#f8fafc; font-family:sans-serif; font-size:0.75rem; font-weight:700;";
        labelContainer.innerHTML = `
            <span>Runner Track (1D Motion)</span>
            <span>Position-Time Graph</span>
        `;
        container.appendChild(labelContainer);

        // Speed/Position Controls UI
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; font-family: sans-serif; font-size: 0.9rem; text-align: center;";
        controlsDiv.innerHTML = `
            <div style="display:flex; justify-content:center; align-items:center; gap:10px; margin-bottom: 10px;">
                <label style="font-weight:700; color:#1e293b;">Runner Position: <span id="lbl-pos">0</span> m</label>
                <input type="range" id="slide-pos" min="0" max="6" step="0.1" value="0" style="width:40%;">
            </div>
            <div>
                <button id="btn-play-run" class="sj-btn" style="background:#0f9d8a; color:white; border:none; padding:6px 12px; border-radius:20px; cursor:pointer;">
                    <i class="fas fa-play"></i> Auto-Run
                </button>
            </div>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var slidePos = controlsDiv.querySelector("#slide-pos");
        var lblPos = controlsDiv.querySelector("#lbl-pos");
        var btnPlay = controlsDiv.querySelector("#btn-play-run");

        var curTime = 0;
        var maxTime = 6;
        var running = false;
        var manual = false;

        btnPlay.addEventListener("click", function () {
            running = !running;
            btnPlay.innerHTML = running ? '<i class="fas fa-pause"></i> Pause' : '<i class="fas fa-play"></i> Auto-Run';
            if (running && curTime >= maxTime) {
                curTime = 0;
                plotPoints = [];
            }
        });

        slidePos.addEventListener("input", function (e) {
            manual = true;
            running = false;
            btnPlay.innerHTML = '<i class="fas fa-play"></i> Auto-Run';
            var val = parseFloat(e.target.value);
            runner.position.x = -7 + val;
            lblPos.textContent = val.toFixed(1);
            
            // Record manual plotting point
            curTime += 0.05;
            if (curTime > maxTime) curTime = 0;
            
            plotPoints.push(new THREE.Vector3(1 + (curTime/maxTime)*6, -3 + (val/6)*6, 0));
            if (plotPoints.length > 100) plotPoints.shift();
            plotGeometry.setFromPoints(plotPoints);
        });

        // Main animation loop
        function animate() {
            requestAnimationFrame(animate);

            if (running) {
                curTime += 0.02;
                if (curTime > maxTime) {
                    curTime = 0;
                    plotPoints = [];
                }

                // Simulate constant speed auto-run
                var currentPos = (Math.sin(curTime * Math.PI / maxTime)) * 6; // sinusoidal back/forth
                runner.position.x = -7 + currentPos;
                lblPos.textContent = currentPos.toFixed(1);
                slidePos.value = currentPos;

                // Add point to graph
                var graphX = 1 + (curTime / maxTime) * 6;
                var graphY = -3 + (currentPos / 6) * 6;
                plotPoints.push(new THREE.Vector3(graphX, graphY, 0));
                
                plotGeometry.setFromPoints(plotPoints);
            }

            renderer.render(scene, camera);
        }
        animate();
    };

    /* ===== ANIMATION 2: CONSTANT ACCELERATION PHYSICS SIMULATOR ===== */
    window.initConstantAccelerationAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a);
        var camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 2, 12);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Ground highway plane
        var groundGeo = new THREE.PlaneGeometry(30, 4);
        var groundMat = new THREE.MeshPhongMaterial({ color: 0x334155, side: THREE.DoubleSide });
        var ground = new THREE.Mesh(groundGeo, groundMat);
        ground.rotation.x = -Math.PI / 2;
        scene.add(ground);

        // Road dashed line
        var lineGeo = new THREE.PlaneGeometry(30, 0.1);
        var lineMat = new THREE.MeshBasicMaterial({ color: 0xfacc15 });
        var roadLine = new THREE.Mesh(lineGeo, lineMat);
        roadLine.rotation.x = -Math.PI / 2;
        roadLine.position.y = 0.01;
        scene.add(roadLine);

        // Vehicle (Car shape - red box with wheels)
        var carGroup = new THREE.Group();
        scene.add(carGroup);

        var bodyGeo = new THREE.BoxGeometry(1.6, 0.6, 0.8);
        var bodyMat = new THREE.MeshPhongMaterial({ color: 0xef4444 });
        var body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = 0.5;
        carGroup.add(body);

        var cabinGeo = new THREE.BoxGeometry(0.8, 0.4, 0.7);
        var cabin = new THREE.Mesh(cabinGeo, bodyMat);
        cabin.position.set(-0.1, 0.9, 0);
        carGroup.add(cabin);

        // Lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        var light = new THREE.DirectionalLight(0xffffff, 0.8);
        light.position.set(0, 10, 5);
        scene.add(light);

        // Vectors (Arrows)
        // Velocity vector: Green arrow
        var velArrow = new THREE.ArrowHelper(
            new THREE.Vector3(1, 0, 0),
            new THREE.Vector3(0, 1.2, 0),
            1.5,
            0x10b981,
            0.4,
            0.2
        );
        carGroup.add(velArrow);

        // Acceleration vector: Blue arrow
        var accArrow = new THREE.ArrowHelper(
            new THREE.Vector3(1, 0, 0),
            new THREE.Vector3(0, 1.8, 0),
            1.0,
            0x3b82f6,
            0.4,
            0.2
        );
        carGroup.add(accArrow);

        // Controls UI
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; font-family: sans-serif; font-size: 0.9rem;";
        controlsDiv.innerHTML = `
            <div style="display:flex; justify-content:space-around; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
                <div>
                    <label style="font-weight:700; color:#1e293b;">Initial Velocity (u): <span id="lbl-u">5.0</span> m/s</label>
                    <input type="range" id="slide-u" min="0" max="10" step="0.5" value="5.0" style="display:block;">
                </div>
                <div>
                    <label style="font-weight:700; color:#1e293b;">Acceleration (a): <span id="lbl-a">1.0</span> m/s²</label>
                    <input type="range" id="slide-a" min="-4" max="4" step="0.2" value="1.0" style="display:block;">
                </div>
            </div>
            <div style="text-align:center; display:flex; justify-content:center; gap:10px;">
                <button id="btn-play-acc" class="sj-3d-btn" style="background:#0f9d8a; color:white; border:none; padding:6px 12px; border-radius:20px; cursor:pointer;"><i class="fas fa-play"></i> Start Sim</button>
                <button id="btn-reset-acc" class="sj-3d-btn" style="background:#475569; color:white; border:none; padding:6px 12px; border-radius:20px; cursor:pointer;"><i class="fas fa-redo"></i> Reset</button>
            </div>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var slideU = controlsDiv.querySelector("#slide-u");
        var slideA = controlsDiv.querySelector("#slide-a");
        var lblU = controlsDiv.querySelector("#lbl-u");
        var lblA = controlsDiv.querySelector("#lbl-a");
        var btnPlay = controlsDiv.querySelector("#btn-play-acc");
        var btnReset = controlsDiv.querySelector("#btn-reset-acc");

        var posX = -12;
        var uVal = 5.0;
        var aVal = 1.0;
        var vVal = uVal;
        var simRunning = false;
        var timeElapsed = 0;

        slideU.addEventListener("input", function (e) {
            uVal = parseFloat(e.target.value);
            lblU.textContent = uVal.toFixed(1);
            if (!simRunning) vVal = uVal;
        });

        slideA.addEventListener("input", function (e) {
            aVal = parseFloat(e.target.value);
            lblA.textContent = aVal.toFixed(1);
        });

        btnPlay.addEventListener("click", function () {
            simRunning = !simRunning;
            btnPlay.innerHTML = simRunning ? '<i class="fas fa-pause"></i> Pause' : '<i class="fas fa-play"></i> Start Sim';
        });

        btnReset.addEventListener("click", function () {
            simRunning = false;
            posX = -12;
            vVal = uVal;
            timeElapsed = 0;
            carGroup.position.x = posX;
            btnPlay.innerHTML = '<i class="fas fa-play"></i> Start Sim';
        });

        // Initial car placement
        carGroup.position.set(posX, 0, 0);

        // Drag camera rotation
        var rotX = 0, rotY = 0, isDrag = false, pX = 0, pY = 0;
        canvas.addEventListener("mousedown", function (e) { isDrag = true; pX = e.clientX; pY = e.clientY; });
        canvas.addEventListener("mouseup", function () { isDrag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (isDrag) { rotY += (e.clientX - pX) * 0.01; rotX += (e.clientY - pY) * 0.01; pX = e.clientX; pY = e.clientY; }
        });

        function animate() {
            requestAnimationFrame(animate);

            if (simRunning) {
                var dt = 0.016; // 60 FPS delta
                timeElapsed += dt;

                // Physics update: v = u + at, s = ut + 0.5at^2
                vVal = uVal + aVal * timeElapsed;
                var dx = vVal * dt;
                posX += dx;

                // Stop if car runs off boundary
                if (posX > 12 || posX < -12) {
                    simRunning = false;
                    btnPlay.innerHTML = '<i class="fas fa-play"></i> Start Sim';
                }

                carGroup.position.x = posX;
            }

            // Dynamically scale/render arrows
            if (vVal >= 0) {
                velArrow.setDirection(new THREE.Vector3(1, 0, 0));
                velArrow.setLength(Math.max(0.1, vVal * 0.3), 0.4, 0.2);
                velArrow.visible = true;
            } else {
                velArrow.setDirection(new THREE.Vector3(-1, 0, 0));
                velArrow.setLength(Math.max(0.1, -vVal * 0.3), 0.4, 0.2);
                velArrow.visible = true;
            }

            if (aVal >= 0) {
                accArrow.setDirection(new THREE.Vector3(1, 0, 0));
                accArrow.setLength(Math.max(0.1, aVal * 0.5), 0.4, 0.2);
                accArrow.visible = aVal !== 0;
            } else {
                accArrow.setDirection(new THREE.Vector3(-1, 0, 0));
                accArrow.setLength(Math.max(0.1, -aVal * 0.5), 0.4, 0.2);
                accArrow.visible = aVal !== 0;
            }

            scene.rotation.y = rotY;
            scene.rotation.x = rotX;
            renderer.render(scene, camera);
        }
        animate();
    };

    /* ===== ANIMATION 3: UNIFORM CIRCULAR MOTION & TANGENTIAL RELEASE ===== */
    window.initCircularMotionAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0f172a);
        var camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 10);

        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Circular ring boundary
        var radius = 2.5;
        var ringGeo = new THREE.RingGeometry(radius - 0.05, radius + 0.05, 64);
        var ringMat = new THREE.MeshBasicMaterial({ color: 0x64748b, side: THREE.DoubleSide });
        var boundaryRing = new THREE.Mesh(ringGeo, ringMat);
        scene.add(boundaryRing);

        // Center pivot sphere
        var centerGeo = new THREE.SphereGeometry(0.1, 16, 16);
        var centerMat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
        var centerPivot = new THREE.Mesh(centerGeo, centerMat);
        scene.add(centerPivot);

        // Marble (Yellow Sphere rotating inside)
        var marbleGeo = new THREE.SphereGeometry(0.2, 16, 16);
        var marbleMat = new THREE.MeshPhongMaterial({ color: 0xfacc15, shininess: 50 });
        var marble = new THREE.Mesh(marbleGeo, marbleMat);
        scene.add(marble);

        // Tangent Velocity Vector Arrow
        var velocityArrow = new THREE.ArrowHelper(
            new THREE.Vector3(0, 1, 0),
            new THREE.Vector3(0, 0, 0),
            1.5,
            0x10b981,
            0.4,
            0.2
        );
        scene.add(velocityArrow);

        // Lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.7));
        var light = new THREE.DirectionalLight(0xffffff, 1.0);
        light.position.set(0, 0, 10);
        scene.add(light);

        // Controls UI
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; text-align: center;";
        controlsDiv.innerHTML = `
            <div style="display:flex; justify-content:center; gap:10px; margin-bottom: 10px;">
                <button id="btn-release" class="sj-btn" style="background:#ef4444; color:white; border:none; padding:10px 20px; font-weight:700; border-radius:50px; cursor:pointer;">
                    <i class="fas fa-expand-arrows-alt"></i> Lift Ring (Release Marble)
                </button>
            </div>
            <button id="btn-reset-cir" class="sj-3d-btn" style="background:#475569; color:white; border:none; padding:6px 12px; border-radius:20px; cursor:pointer;"><i class="fas fa-redo"></i> Reset Ring</button>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var btnRelease = controlsDiv.querySelector("#btn-release");
        var btnReset = controlsDiv.querySelector("#btn-reset-cir");

        var theta = 0;
        var angularVelocity = 2.5; // rad/s
        var released = false;
        var releaseVelVector = new THREE.Vector3();
        var marblePosition = new THREE.Vector3(radius, 0, 0);

        btnRelease.addEventListener("click", function () {
            if (!released) {
                released = true;
                boundaryRing.visible = false; // "Lift" the ring

                // Compute tangential direction vector
                // Path is (R*cos(theta), R*sin(theta))
                // Tangent vector is (-sin(theta), cos(theta))
                releaseVelVector.set(-Math.sin(theta), Math.cos(theta), 0).normalize();
            }
        });

        btnReset.addEventListener("click", function () {
            released = false;
            boundaryRing.visible = true;
            theta = 0;
            marblePosition.set(radius, 0, 0);
            marble.position.copy(marblePosition);
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
            var dt = 0.016;

            if (!released) {
                // Uniform circular path
                theta += angularVelocity * dt;
                marblePosition.set(radius * Math.cos(theta), radius * Math.sin(theta), 0);
                marble.position.copy(marblePosition);

                // Update tangent arrow helpers
                var tangent = new THREE.Vector3(-Math.sin(theta), Math.cos(theta), 0).normalize();
                velocityArrow.position.copy(marblePosition);
                velocityArrow.setDirection(tangent);
                velocityArrow.visible = true;
            } else {
                // Moves in a straight tangential path after release
                var ds = releaseVelVector.clone().multiplyScalar(radius * angularVelocity * dt);
                marblePosition.add(ds);
                marble.position.copy(marblePosition);

                // Hide tangent arrow once flying away
                velocityArrow.visible = false;
            }

            scene.rotation.y = rotY;
            scene.rotation.x = rotX;
            renderer.render(scene, camera);
        }
        animate();
    };

})();
