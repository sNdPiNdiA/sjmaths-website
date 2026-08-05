/* ============================================== */
/* SJMaths — Class 9 Science Chapter Engine        */
/* Handles: Section nav highlighting,             */
/* Quiz interactions, Three.js animations          */
/* ============================================== */

(function () {
    "use strict";

    /* ===== SECTION NAVIGATION HIGHLIGHT =====
       Highlights the active section link based
       on the current page URL.
    */
    var currentPage = window.location.pathname.split("/").pop();
    if (!currentPage) currentPage = "index.html";

    var sectionLinks = document.querySelectorAll(".sj-section-link");
    sectionLinks.forEach(function (link) {
        var href = link.getAttribute("href");
        if (href === currentPage) {
            link.classList.add("active");
        }
        link.addEventListener("click", function () {
            sectionLinks.forEach(function (l) { l.classList.remove("active"); });
            this.classList.add("active");
        });
    });

    /* ===== QUIZ INTERACTION =====
       Handles instant feedback on MCQ selections.
    */
    var quizOptions = document.querySelectorAll(".sj-quiz-opt");

    quizOptions.forEach(function (opt) {
        opt.addEventListener("click", function () {
            var question = this.closest(".sj-quiz-q");
            if (!question || question.dataset.answered === "true") return;

            var isCorrect = this.getAttribute("data-correct") === "true";
            var feedback = question.querySelector(".sj-quiz-feedback");
            var allOptions = question.querySelectorAll(".sj-quiz-opt");

            question.dataset.answered = "true";

            if (isCorrect) {
                this.classList.add("correct");
                if (feedback) {
                    feedback.textContent = "Correct! " + (this.getAttribute("data-explanation") || "");
                    feedback.className = "sj-quiz-feedback show correct";
                }
            } else {
                this.classList.add("wrong");
                allOptions.forEach(function (o) {
                    if (o.getAttribute("data-correct") === "true") {
                        o.classList.add("correct");
                    }
                });
                if (feedback) {
                    feedback.textContent = "Not quite. The correct answer is highlighted in green.";
                    feedback.className = "sj-quiz-feedback show wrong";
                }
            }

            allOptions.forEach(function (o) {
                o.style.cursor = "default";
            });
        });
    });

    /* ===== THREE.JS ANIMATION ENGINE =====
       Dynamically loads three.js and initializes
       animations for .sj-3d-container elements.
    */
    function initThreeJsAnimations() {
        if (typeof THREE === "undefined") {
            var script = document.createElement("script");
            script.src = "https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js";
            script.onload = function () { setupAllAnimations(); };
            document.head.appendChild(script);
        } else {
            setupAllAnimations();
        }
    }

    function setupAllAnimations() {
        var containers = document.querySelectorAll(".sj-3d-container");
        containers.forEach(function (container) {
            var animType = container.getAttribute("data-animation");
            var canvas = container.querySelector(".sj-3d-canvas");
            if (!canvas || !animType) return;

            // Dynamically resolve animType to function name, e.g. "origin-life" -> "initOriginLifeAnimation"
            var camelCaseName = animType.split("-").map(function (word) {
                return word.charAt(0).toUpperCase() + word.slice(1);
            }).join("");
            var handlerName = "init" + camelCaseName + "Animation";

            if (typeof window[handlerName] === "function") {
                window[handlerName](canvas, container);
            } else {
                switch (animType) {
                    case "atom": initAtomAnimation(canvas, container); break;
                    case "sound-wave": initSoundWaveAnimation(canvas, container); break;
                    case "motion": initMotionAnimation(canvas, container); break;
                    case "molecule": initMoleculeAnimation(canvas, container); break;
                    default: initDefaultAnimation(canvas, container);
                }
            }
        });
    }

    /* ===== Auto-init 3D on concepts page ===== */
    if (document.querySelector(".sj-3d-container")) {
        window.addEventListener("load", function () {
            initThreeJsAnimations();
        });
    }


    /* ===== ANIMATION: ATOM (Bohr Model) ===== */
    function initAtomAnimation(canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 5, 15);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        var nucleusGroup = new THREE.Group();
        var protonGeo = new THREE.SphereGeometry(0.6, 32, 32);
        var protonMat = new THREE.MeshPhongMaterial({ color: 0xef4444 });
        var neutronMat = new THREE.MeshPhongMaterial({ color: 0x64748b });

        for (var i = 0; i < 8; i++) {
            var isProton = i % 2 === 0;
            var sphere = new THREE.Mesh(protonGeo, isProton ? protonMat : neutronMat);
            var a = (i / 8) * Math.PI * 2;
            sphere.position.set(Math.cos(a) * 0.8, Math.sin(a) * 0.8, 0);
            nucleusGroup.add(sphere);
        }
        scene.add(nucleusGroup);

        var electronGeo = new THREE.SphereGeometry(0.25, 16, 16);
        var electronMat = new THREE.MeshPhongMaterial({ color: 0x0ea5e9, emissive: 0x0284c7, emissiveIntensity: 0.5 });
        var orbitRadii = [3, 5, 7];
        var electrons = [];

        orbitRadii.forEach(function (radius, shellIndex) {
            var ringGeo = new THREE.TorusGeometry(radius, 0.03, 8, 64);
            var ringMat = new THREE.MeshBasicMaterial({ color: 0x334155, transparent: true, opacity: 0.4 });
            var ring = new THREE.Mesh(ringGeo, ringMat);
            ring.rotation.x = Math.PI / 2 + (shellIndex * 0.3);
            scene.add(ring);

            var numE = shellIndex === 0 ? 2 : 8;
            for (var k = 0; k < Math.min(numE, 5); k++) {
                var el = new THREE.Mesh(electronGeo, electronMat);
                el.userData = {
                    radius: radius,
                    angle: (k / numE) * Math.PI * 2,
                    speed: 0.02 + (shellIndex * 0.005),
                    tilt: shellIndex * 0.3
                };
                electrons.push(el);
                scene.add(el);
            }
        });

        scene.add(new THREE.AmbientLight(0xffffff, 0.4));
        var pt = new THREE.PointLight(0xffffff, 1);
        pt.position.set(10, 10, 10);
        scene.add(pt);

        var isPlaying = true;
        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;
        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });
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
            isPlaying = !isPlaying;
            pb.innerHTML = isPlaying ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () { rX = 0; rY = 0; camera.position.set(0, 5, 15); });

        function anim() {
            requestAnimationFrame(anim);
            if (isPlaying) {
                nucleusGroup.rotation.y += 0.01;
                electrons.forEach(function (e) {
                    e.userData.angle += e.userData.speed;
                    var r = e.userData.radius, an = e.userData.angle, t = e.userData.tilt;
                    e.position.set(Math.cos(an) * r, Math.sin(an) * r * Math.sin(t), Math.sin(an) * r * Math.cos(t));
                });
            }
            scene.rotation.x = rX;
            scene.rotation.y = rY;
            renderer.render(scene, camera);
        }
        anim();
    }

    /* ===== ANIMATION: SOUND WAVE ===== */
    function initSoundWaveAnimation(canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 3, 15);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        var src = new THREE.Mesh(new THREE.SphereGeometry(0.8, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xef4444, emissive: 0xb91c1c, emissiveIntensity: 0.3 }));
        scene.add(src);

        var rings = [];
        for (var i = 0; i < 6; i++) {
            var r = new THREE.Mesh(new THREE.TorusGeometry(1, 0.08, 16, 64),
                new THREE.MeshPhongMaterial({ color: 0x0ea5e9, transparent: true, opacity: 0.6 }));
            r.userData = { phase: i * 0.5 };
            rings.push(r);
            scene.add(r);
        }

        var dots = [];
        var dotGeo = new THREE.SphereGeometry(0.15, 8, 8);
        var dotMat = new THREE.MeshPhongMaterial({ color: 0xfbbf24 });
        for (var d = 0; d < 30; d++) {
            var dg = new THREE.Mesh(dotGeo, dotMat);
            var an = (d / 30) * Math.PI * 2;
            dg.userData = { angle: an, baseR: 2 + (d % 5) * 1.5 };
            dots.push(dg);
            scene.add(dg);
        }

        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        var lp = new THREE.PointLight(0xffffff, 1); lp.position.set(10, 10, 10); scene.add(lp);

        var playing = true;
        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });

        var t = 0;
        function anim() {
            requestAnimationFrame(anim);
            if (playing) t += 0.02;
            rings.forEach(function (r) {
                var s = ((t + r.userData.phase) % 3) + 0.5;
                r.scale.set(s, s, 1);
                r.material.opacity = Math.max(0, 0.6 - s * 0.15);
            });
            dots.forEach(function (dg) {
                var w = Math.sin(t * 2 + dg.userData.angle * 3) * 0.8;
                var rr = dg.userData.baseR + w;
                dg.position.set(Math.cos(dg.userData.angle) * rr, 0, Math.sin(dg.userData.angle) * rr);
            });
            renderer.render(scene, camera);
        }
        anim();
    }

    /* ===== ANIMATION: MOTION (Projectile) ===== */
    function initMotionAnimation(canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 5, 20);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        var ground = new THREE.Mesh(new THREE.PlaneGeometry(30, 20),
            new THREE.MeshPhongMaterial({ color: 0x1e293b, side: THREE.DoubleSide }));
        ground.rotation.x = Math.PI / 2;
        ground.position.y = -3;
        scene.add(ground);

        var grid = new THREE.GridHelper(30, 15, 0x334155, 0x334155);
        grid.position.y = -2.9;
        scene.add(grid);

        var ball = new THREE.Mesh(new THREE.SphereGeometry(0.5, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xef4444, emissive: 0xb91c1c, emissiveIntensity: 0.3 }));
        scene.add(ball);

        var trailGeo = new THREE.BufferGeometry();
        var trailPos = new Float32Array(300);
        trailGeo.setAttribute("position", new THREE.BufferAttribute(trailPos, 3));
        var trail = new THREE.Line(trailGeo, new THREE.LineBasicMaterial({ color: 0xfbbf24, transparent: true, opacity: 0.5 }));
        scene.add(trail);

        var arrow = new THREE.ArrowHelper(new THREE.Vector3(1, 0, 0), new THREE.Vector3(0, 0, 0), 2, 0x0ea5e9, 0.5, 0.3);
        scene.add(arrow);

        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        var lp2 = new THREE.PointLight(0xffffff, 1); lp2.position.set(10, 15, 10); scene.add(lp2);

        var playing = true;
        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });
        var rb = container.querySelector(".sj-3d-reset");
        if (rb) rb.addEventListener("click", function () { t = 0; trailIdx = 0; });

        var t = 0, trailIdx = 0;
        var v0 = 12, g = 9.8, ang = Math.PI / 4;

        function anim() {
            requestAnimationFrame(anim);
            if (playing) {
                t += 0.02;
                var x = v0 * Math.cos(ang) * t;
                var y = v0 * Math.sin(ang) * t - 0.5 * g * t * t;
                ball.position.set(x - 10, y, 0);
                if (trailIdx < 100) {
                    trailPos[trailIdx * 3] = x - 10;
                    trailPos[trailIdx * 3 + 1] = y;
                    trailPos[trailIdx * 3 + 2] = 0;
                    trailIdx++;
                    trailGeo.setDrawRange(0, trailIdx);
                    trailGeo.attributes.position.needsUpdate = true;
                }
                var vx = v0 * Math.cos(ang);
                var vy = v0 * Math.sin(ang) - g * t;
                var speed = Math.sqrt(vx * vx + vy * vy);
                arrow.position.copy(ball.position);
                arrow.setDirection(new THREE.Vector3(vx, vy, 0).normalize());
                arrow.setLength(speed * 0.3, 0.5, 0.3);
                if (y < -3) { t = 0; trailIdx = 0; }
            }
            renderer.render(scene, camera);
        }
        anim();
    }

    /* ===== ANIMATION: MOLECULE (H2O) ===== */
    function initMoleculeAnimation(canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.set(0, 0, 12);
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antials: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        var o2 = new THREE.Mesh(new THREE.SphereGeometry(1.2, 32, 32),
            new THREE.MeshPhongMaterial({ color: 0xef4444 }));
        scene.add(o2);

        var hGeo = new THREE.SphereGeometry(0.7, 32, 32);
        var hMat = new THREE.MeshPhongMaterial({ color: 0xf8fafc });
        var h1 = new THREE.Mesh(hGeo, hMat); h1.position.set(2, 1.5, 0);
        var h2 = new THREE.Mesh(hGeo, hMat); h2.position.set(2, -1.5, 0);
        scene.add(h1, h2);

        var bMat = new THREE.MeshPhongMaterial({ color: 0x64748b });
        var bGeo = new THREE.CylinderGeometry(0.1, 0.1, 2.5, 8);
        var b1 = new THREE.Mesh(bGeo, bMat); b1.position.set(1, 0.75, 0); b1.rotation.z = Math.PI / 4;
        var b2 = new THREE.Mesh(bGeo, bMat); b2.position.set(1, -0.75, 0); b2.rotation.z = -Math.PI / 4;
        scene.add(b1, b2);

        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        var lp3 = new THREE.PointLight(0xffffff, 1); lp3.position.set(10, 10, 10); scene.add(lp3);

        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;
        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var playing = true;
        var pb = container.querySelector(".sj-3d-play");
        if (pb) pb.addEventListener("click", function () {
            playing = !playing;
            pb.innerHTML = playing ? '<i class="fas fa-pause"></i>' : '<i class="fas fa-play"></i>';
        });

        function anim() {
            requestAnimationFrame(anim);
            if (playing) scene.rotation.y += 0.008;
            scene.rotation.x = rX;
            scene.rotation.y = rY + (playing ? performance.now() * 0.0008 : 0);
            renderer.render(scene, camera);
        }
        anim();
    }

    /* ===== DEFAULT ANIMATION (fallback) ===== */
    function initDefaultAnimation(canvas, container) {
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(60, canvas.clientWidth / 400, 0.1, 1000);
        camera.position.z = 8;
        var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(canvas.clientWidth, 400);

        var mesh = new THREE.Mesh(new THREE.IcosahedronGeometry(2, 1),
            new THREE.MeshPhongMaterial({ color: 0x0f9d8a, wireframe: true }));
        scene.add(mesh);

        scene.add(new THREE.AmbientLight(0xffffff, 0.5));
        var lp4 = new THREE.PointLight(0xffffff, 1); lp4.position.set(10, 10, 10); scene.add(lp4);

        var rX = 0, rY = 0, drag = false, dPX = 0, dPY = 0;
        canvas.addEventListener("mousedown", function (e) { drag = true; dPX = e.clientX; dPY = e.clientY; });
        canvas.addEventListener("mouseup", function () { drag = false; });
        canvas.addEventListener("mousemove", function (e) {
            if (drag) { rY += (e.clientX - dPX) * 0.01; rX += (e.clientY - dPY) * 0.01; dPX = e.clientX; dPY = e.clientY; }
        });
        canvas.addEventListener("touchstart", function (e) { drag = true; dPX = e.touches[0].clientX; dPY = e.touches[0].clientY; });
        canvas.addEventListener("touchend", function () { drag = false; });
        canvas.addEventListener("touchmove", function (e) {
            if (drag) {
                rY += (e.touches[0].clientX - dPX) * 0.01;
                rX += (e.touches[0].clientY - dPY) * 0.01;
                dPX = e.touches[0].clientX; dPY = e.touches[0].clientY;
            }
        });

        var playing = true;
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
                mesh.rotation.x += 0.005;
                mesh.rotation.y += 0.008;
            }
            mesh.rotation.x += rX * 0.001;
            mesh.rotation.y += rY * 0.001;
            renderer.render(scene, camera);
        }
        anim();
    }

    /* ===== FLOATING DARK MODE TOGGLE BUTTON (Bottom Left, above bottom nav in mobile mode) ===== */
    function initFloatingDarkModeToggle() {
        if (document.getElementById('sjFloatingDarkToggle')) return;
        var btn = document.createElement('button');
        btn.id = 'sjFloatingDarkToggle';
        btn.setAttribute('aria-label', 'Toggle Dark Mode');

        var isDark = document.body.classList.contains('dark-mode') || localStorage.getItem('sjmaths-dark') === 'on' || localStorage.getItem('theme') === 'dark';
        if (isDark) {
            document.body.classList.add('dark-mode');
            btn.innerHTML = '<i class="fas fa-sun"></i>';
        } else {
            btn.innerHTML = '<i class="fas fa-moon"></i>';
        }

        Object.assign(btn.style, {
            position: 'fixed',
            bottom: '85px',
            left: '16px',
            width: '46px',
            height: '46px',
            borderRadius: '50%',
            background: isDark ? '#ffffff' : '#0f172a',
            color: isDark ? '#0f172a' : '#ffffff',
            border: 'none',
            boxShadow: '0 8px 25px rgba(0,0,0,0.25)',
            zIndex: '9999',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: '1.1rem',
            transition: 'all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)'
        });

        btn.addEventListener('click', function () {
            var dark = document.body.classList.toggle('dark-mode');
            localStorage.setItem('sjmaths-dark', dark ? 'on' : 'off');
            localStorage.setItem('theme', dark ? 'dark' : 'light');
            btn.innerHTML = dark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
            btn.style.background = dark ? '#ffffff' : '#0f172a';
            btn.style.color = dark ? '#0f172a' : '#ffffff';
        });

        document.body.appendChild(btn);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFloatingDarkModeToggle);
    } else {
        initFloatingDarkModeToggle();
    }
})();
