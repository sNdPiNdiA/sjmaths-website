(function () {
    "use strict";

    /* ===== ANIMATION: CRICKET SHOT (Projectile Modeling) ===== */
    window.initCricketAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        scene.background = new THREE.Color(0xe0f2fe); // Day sky blue background
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 5, 25);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);

        // Ground Plane (Grass field)
        var groundGeo = new THREE.PlaneGeometry(100, 100);
        var groundMat = new THREE.MeshPhongMaterial({ color: 0x16a34a, side: THREE.DoubleSide }); // brighter green
        var ground = new THREE.Mesh(groundGeo, groundMat);
        ground.rotation.x = -Math.PI / 2;
        ground.position.y = -2;
        scene.add(ground);

        // Pitch (Brown rectangle)
        var pitchGeo = new THREE.PlaneGeometry(6, 30);
        var pitchMat = new THREE.MeshPhongMaterial({ color: 0xd97706, side: THREE.DoubleSide }); // brighter brown
        var pitch = new THREE.Mesh(pitchGeo, pitchMat);
        pitch.rotation.x = -Math.PI / 2;
        pitch.position.set(0, -1.99, 0);
        scene.add(pitch);

        // Ball (Red sphere) - larger for visibility
        var ballGeo = new THREE.SphereGeometry(0.6, 16, 16);
        var ballMat = new THREE.MeshPhongMaterial({ color: 0xdc2626 });
        var ball = new THREE.Mesh(ballGeo, ballMat);
        scene.add(ball);

        // Trajectory Line
        var lineGeo = new THREE.BufferGeometry();
        var lineMat = new THREE.LineBasicMaterial({ color: 0x0284c7, linewidth: 4 });
        var line = new THREE.Line(lineGeo, lineMat);
        scene.add(line);

        // Lighting - brighter day lighting
        scene.add(new THREE.AmbientLight(0xffffff, 0.9));
        var light = new THREE.PointLight(0xffffff, 1.2);
        light.position.set(10, 20, 10);
        scene.add(light);

        // UI Controls inside container
        var velocity = 15;
        var angle = 45;
        var airResistance = false;
        var spin = false;

        // Sliders & Checkbox UI injection
        var controlsDiv = document.createElement("div");
        controlsDiv.style.cssText = "padding: 15px; background: rgba(15,23,42,0.05); border-radius: 12px; margin-top: 15px; font-family: sans-serif; font-size: 0.9rem; display: grid; grid-template-columns: 1fr; gap: 10px;";
        if (window.innerWidth >= 768) {
            controlsDiv.style.gridTemplateColumns = "1fr 1fr";
        }

        controlsDiv.innerHTML = `
            <div>
                <label style="display:block; font-weight:700; margin-bottom:5px;">Launch Angle: <span id="lbl-angle">45</span>°</label>
                <input type="range" id="slide-angle" min="15" max="75" value="45" style="width:100%;">
            </div>
            <div>
                <label style="display:block; font-weight:700; margin-bottom:5px;">Initial Speed: <span id="lbl-speed">15</span> m/s</label>
                <input type="range" id="slide-speed" min="5" max="30" value="15" style="width:100%;">
            </div>
            <div style="grid-column: span 1; display: flex; gap: 15px; align-items:center; margin-top:5px;">
                <label style="font-weight:700;"><input type="checkbox" id="chk-air"> Air Resistance</label>
                <label style="font-weight:700;"><input type="checkbox" id="chk-spin"> Spin (Magnus Effect)</label>
            </div>
        `;
        container.parentNode.insertBefore(controlsDiv, container.nextSibling);

        var slideAngle = controlsDiv.querySelector("#slide-angle");
        var slideSpeed = controlsDiv.querySelector("#slide-speed");
        var chkAir = controlsDiv.querySelector("#chk-air");
        var chkSpin = controlsDiv.querySelector("#chk-spin");

        var lblAngle = controlsDiv.querySelector("#lbl-angle");
        var lblSpeed = controlsDiv.querySelector("#lbl-speed");

        slideAngle.addEventListener("input", function (e) {
            angle = parseFloat(e.target.value);
            lblAngle.textContent = angle;
            resetPath();
        });
        slideSpeed.addEventListener("input", function (e) {
            velocity = parseFloat(e.target.value);
            lblSpeed.textContent = velocity;
            resetPath();
        });
        chkAir.addEventListener("change", function (e) {
            airResistance = e.target.checked;
            resetPath();
        });
        chkSpin.addEventListener("change", function (e) {
            spin = e.target.checked;
            resetPath();
        });

        // Path calculation variables
        var t = 0;
        var points = [];
        var playing = true;

        var playBtn = container.querySelector(".sj-3d-play");
        if (playBtn) playBtn.addEventListener("click", function () {
            playing = !playing;
            playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });

        var resetBtn = container.querySelector(".sj-3d-reset");
        if (resetBtn) resetBtn.addEventListener("click", function () {
            t = 0;
            resetPath();
        });

        function resetPath() {
            t = 0;
            points = [];
            // Generate full trajectory for the dotted line
            var tempPoints = [];
            var g = 9.8;
            var theta = (angle * Math.PI) / 180;
            var maxT = (2 * velocity * Math.sin(theta)) / g;
            if (airResistance) maxT *= 0.85; // rough estimate of shorter hangtime

            for (var time = 0; time <= maxT + 0.1; time += 0.05) {
                var pos = getTrajectoryPoint(time, velocity, theta, airResistance, spin);
                if (pos.y < -2) {
                    tempPoints.push(new THREE.Vector3(pos.x, -2, pos.z));
                    break;
                }
                tempPoints.push(pos);
            }
            lineGeo.setFromPoints(tempPoints);
        }

        function getTrajectoryPoint(time, v0, theta, air, magnus) {
            var g = 9.8;
            var x, y, z;
            
            if (air) {
                // simple model of drag: exponential velocity decay
                var k = 0.15; // drag coefficient
                x = (v0 * Math.cos(theta) / k) * (1 - Math.exp(-k * time)) - 10; // offset left
                y = ((v0 * Math.sin(theta) + g/k) / k) * (1 - Math.exp(-k * time)) - (g * time / k) - 2;
            } else {
                x = v0 * Math.cos(theta) * time - 10;
                y = v0 * Math.sin(theta) * time - 0.5 * g * time * time - 2;
            }
            
            z = 0;
            if (magnus) {
                // Magnus effect causes horizontal deflection/drift over time
                z = 0.2 * v0 * time * time;
            }
            return new THREE.Vector3(x, y, z);
        }

        resetPath();

        // Drag controls
        var rotX = 0.1, rotY = 0.4, isDrag = false, pX = 0, pY = 0;
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

        function animate() {
            requestAnimationFrame(animate);

            if (playing) {
                t += 0.025;
                var theta = (angle * Math.PI) / 180;
                var pos = getTrajectoryPoint(t, velocity, theta, airResistance, spin);
                
                if (pos.y < -2) {
                    ball.position.set(pos.x, -2, pos.z);
                    t = 0; // restart
                } else {
                    ball.position.copy(pos);
                }
            }

            // apply rotation views
            scene.rotation.y = rotY;
            scene.rotation.x = rotX;

            renderer.render(scene, camera);
        }
        animate();
    };

    /* ===== ANIMATION: SOLAR ECLIPSE (Shadow Modeling) ===== */
    window.initEclipseAnimation = function (canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(65, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 8, 20);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
        renderer.setSize(canvas.clientWidth, 400);
        scene.background = new THREE.Color(0x0a0f1d); // Deep space background (slightly lighter than black)

        // Sun (Large glowing yellow sphere)
        var sunGeo = new THREE.SphereGeometry(3, 32, 32);
        var sunMat = new THREE.MeshBasicMaterial({ color: 0xf59e0b });
        var sun = new THREE.Mesh(sunGeo, sunMat);
        sun.position.set(-15, 0, 0);
        scene.add(sun);

        // Earth (Medium blue sphere)
        var earthGeo = new THREE.SphereGeometry(2, 32, 32);
        var earthMat = new THREE.MeshPhongMaterial({ color: 0x0284c7, shininess: 30 });
        var earth = new THREE.Mesh(earthGeo, earthMat);
        earth.position.set(5, 0, 0);
        scene.add(earth);

        // Moon (Small grey sphere) - scaled up for visibility
        var moonGeo = new THREE.SphereGeometry(0.85, 16, 16);
        var moonMat = new THREE.MeshPhongMaterial({ color: 0x94a3b8 }); // lighter grey
        var moon = new THREE.Mesh(moonGeo, moonMat);
        scene.add(moon);

        // Shadow Cone (Representing light blockage) - scaled up and made more opaque
        var shadowGeo = new THREE.ConeGeometry(1.2, 10, 16, 1, true);
        var shadowMat = new THREE.MeshBasicMaterial({
            color: 0x111827,
            transparent: true,
            opacity: 0.65,
            side: THREE.DoubleSide
        });
        var shadowCone = new THREE.Mesh(shadowGeo, shadowMat);
        shadowCone.rotation.z = -Math.PI / 2; // point towards earth
        scene.add(shadowCone);

        // Lighting - increased ambient lighting so dark sides are visible
        scene.add(new THREE.AmbientLight(0xffffff, 0.45));
        var sunLight = new THREE.DirectionalLight(0xffffff, 1.8);
        sunLight.position.set(-15, 0, 0);
        scene.add(sunLight);

        // Drag controls
        var rotX = 0.3, rotY = 0, isDrag = false, pX = 0, pY = 0;
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
        if (resetBtn) resetBtn.addEventListener("click", function () { rotX = 0.3; rotY = 0; angle = 0; });

        var angle = 0;

        function animate() {
            requestAnimationFrame(animate);

            if (playing) {
                angle += 0.012;
            }

            // Moon orbit path: crosses exactly between Sun (-15,0,0) and Earth (5,0,0) at angle = 0 (or multiple)
            var distance = 3.5;
            var mx = 5 + Math.cos(angle) * distance;
            var mz = Math.sin(angle) * distance * 0.6; // slightly squashed ellipse orbit
            var my = Math.sin(angle) * distance * 0.2; // slight inclination

            moon.position.set(mx, my, mz);

            // Orient shadow cone pointing directly away from the Sun through the Moon's center
            var sunPos = new THREE.Vector3(-15, 0, 0);
            var moonPos = moon.position.clone();
            var dir = new THREE.Vector3().subVectors(moonPos, sunPos).normalize();
            
            // Cone base sits at moon center, extends outwards along the direction vector
            shadowCone.position.copy(moonPos).addScaledVector(dir, 4); 
            shadowCone.lookAt(moonPos.clone().addScaledVector(dir, 10));
            shadowCone.rotation.x += Math.PI / 2; // correct orientation lookAt offset

            // Apply camera rotations
            scene.rotation.y = rotY;
            scene.rotation.x = rotX;

            renderer.render(scene, camera);
        }
        animate();
    };

})();
