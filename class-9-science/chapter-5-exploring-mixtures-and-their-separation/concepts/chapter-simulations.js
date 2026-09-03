/**
 * Chapter 5 Separation Simulators
 * 1. Paper Chromatography
 * 2. Distillation
 * 3. Separating Funnel
 */

function startAllSimulations() {
    initChromatography();
    initDistillation();
    initSeparatingFunnel();
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startAllSimulations);
} else {
    startAllSimulations();
}

/* ==========================================================================
   1. Paper Chromatography Simulator
   ========================================================================== */
function initChromatography() {
    const canvas = document.getElementById("chrom-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    const analyteSelect = document.getElementById("chrom-analyte");
    const solventSelect = document.getElementById("chrom-solvent");
    const startBtn = document.getElementById("chrom-start");
    const resetBtn = document.getElementById("chrom-reset");
    const infoText = document.getElementById("chrom-info");

    let animationId = null;
    let solventHeight = 0; // percentage from line to top (0 to 1)
    let isRunning = false;

    // Define Rf values
    const pigments = {
        "black-ink": [
            { color: "#e11d48", label: "Red Dye", rfWater: 0.45, rfAlcohol: 0.3 },
            { color: "#eab308", label: "Yellow Dye", rfWater: 0.75, rfAlcohol: 0.5 },
            { color: "#2563eb", label: "Blue Dye", rfWater: 0.9, rfAlcohol: 0.7 }
        ],
        "green-dye": [
            { color: "#eab308", label: "Yellow Pigment", rfWater: 0.6, rfAlcohol: 0.45 },
            { color: "#2563eb", label: "Blue Pigment", rfWater: 0.85, rfAlcohol: 0.65 }
        ]
    };

    function draw() {
        const w = canvas.width;
        const h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        // Draw Beaker outline
        ctx.strokeStyle = "#cbd5e1";
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(w / 2 - 80, 40);
        ctx.lineTo(w / 2 - 80, h - 30);
        ctx.lineTo(w / 2 + 80, h - 30);
        ctx.lineTo(w / 2 + 80, 40);
        ctx.stroke();

        // Draw solvent level in beaker (constant water at bottom)
        ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
        ctx.fillRect(w / 2 - 76, h - 55, 152, 23);

        // Draw Chromatography Paper strip
        const paperX = w / 2 - 40;
        const paperY = 60;
        const paperW = 80;
        const paperH = h - 110;

        ctx.fillStyle = "#ffffff";
        ctx.strokeStyle = "#94a3b8";
        ctx.lineWidth = 1.5;
        ctx.fillRect(paperX, paperY, paperW, paperH);
        ctx.strokeRect(paperX, paperY, paperW, paperH);

        // Draw origin pencil line
        const originY = paperY + paperH - 40;
        ctx.strokeStyle = "#64748b";
        ctx.lineWidth = 1;
        ctx.setLineDash([4, 3]);
        ctx.beginPath();
        ctx.moveTo(paperX, originY);
        ctx.lineTo(paperX + paperW, originY);
        ctx.stroke();
        ctx.setLineDash([]); // reset

        // Draw solvent front (rising front)
        const maxTravel = paperH - 80;
        const currentFrontY = originY - (solventHeight * maxTravel);

        if (solventHeight > 0) {
            ctx.strokeStyle = "rgba(56, 189, 248, 0.7)";
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(paperX, currentFrontY);
            ctx.lineTo(paperX + paperW, currentFrontY);
            ctx.stroke();

            // wet paper look
            ctx.fillStyle = "rgba(56, 189, 248, 0.05)";
            ctx.fillRect(paperX, currentFrontY, paperW, originY - currentFrontY);
        }

        // Draw pigments separation
        const analyte = analyteSelect.value;
        const solvent = solventSelect.value;
        const activePigments = pigments[analyte];

        if (!isRunning && solventHeight === 0) {
            // Draw initial ink spot at center of pencil line
            ctx.fillStyle = analyte === "black-ink" ? "#1e293b" : "#15803d";
            ctx.beginPath();
            ctx.arc(w / 2, originY, 6, 0, Math.PI * 2);
            ctx.fill();
        } else {
            // Animate moving separated components
            activePigments.forEach(pig => {
                const rf = solvent === "water" ? pig.rfWater : pig.rfAlcohol;
                const distanceVal = solventHeight * maxTravel * rf;
                const spotY = originY - distanceVal;

                ctx.fillStyle = pig.color;
                ctx.beginPath();
                ctx.arc(w / 2, spotY, 7 - (solventHeight * 1.5), 0, Math.PI * 2);
                ctx.fill();

                // Draw text labels when finished
                if (solventHeight >= 0.99) {
                    ctx.fillStyle = "#334155";
                    ctx.font = "10px Outfit, sans-serif";
                    ctx.fillText(pig.label + ` (Rf: ${rf})`, w / 2 + 12, spotY + 3);
                }
            });

            // Draw fading original spot
            const remainingColor = 255 - Math.min(255, solventHeight * 350);
            ctx.fillStyle = `rgb(${remainingColor},${remainingColor},${remainingColor})`;
            ctx.beginPath();
            ctx.arc(w / 2, originY, 6 * (1 - solventHeight), 0, Math.PI * 2);
            ctx.fill();
        }
    }

    function animate() {
        if (solventHeight < 1) {
            solventHeight += 0.005;
            draw();
            animationId = requestAnimationFrame(animate);
        } else {
            solventHeight = 1;
            draw();
            isRunning = false;
            startBtn.disabled = false;
            infoText.innerText = `Chromatogram complete! Notice how components separated based on their differential solubility in ${solventSelect.value === "water" ? "Water" : "Alcohol"}.`;
        }
    }

    startBtn.addEventListener("click", () => {
        if (isRunning) return;
        isRunning = true;
        startBtn.disabled = true;
        infoText.innerText = "Solvent rising up the paper strip by capillary action. Components are partitioning...";
        animate();
    });

    resetBtn.addEventListener("click", () => {
        cancelAnimationFrame(animationId);
        solventHeight = 0;
        isRunning = false;
        startBtn.disabled = false;
        infoText.innerText = "Select parameters and click 'Start Chromatogram' to begin.";
        draw();
    });

    // Initial Draw
    draw();
    analyteSelect.addEventListener("change", () => { solventHeight = 0; draw(); });
    solventSelect.addEventListener("change", () => { solventHeight = 0; draw(); });
}

/* ==========================================================================
   2. Distillation Flask Simulator
   ========================================================================== */
function initDistillation() {
    const canvas = document.getElementById("dist-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    const tempSlider = document.getElementById("dist-temp");
    const tempValue = document.getElementById("dist-temp-val");
    const infoText = document.getElementById("dist-info");

    let particles = [];
    let distillateCount = 0;
    let animationId = null;

    class Molecule {
        constructor(type, x, y) {
            this.type = type; // 'acetone' (yellow) or 'water' (blue)
            this.x = x;
            this.y = y;
            this.radius = 3.5;
            this.state = "liquid"; // 'liquid', 'vapor', 'condenser', 'distillate'
            this.vx = (Math.random() - 0.5) * 1.5;
            this.vy = (Math.random() - 0.5) * 0.8;
            this.alpha = 1;
        }

        update(temp) {
            if (this.state === "liquid") {
                // Keep inside flask liquid area
                this.x += this.vx;
                this.y += this.vy;
                if (this.x < 115 || this.x > 185) this.vx *= -1;
                if (this.y < 160 || this.y > 210) this.vy *= -1;

                // Evaporation trigger
                if (this.type === "acetone" && temp >= 56) {
                    if (Math.random() < (temp - 50) * 0.001) this.state = "vapor";
                } else if (this.type === "water" && temp >= 100) {
                    if (Math.random() < (temp - 95) * 0.002) this.state = "vapor";
                }
            } else if (this.state === "vapor") {
                // Rise up flask neck
                this.y -= 1.8;
                this.x += (Math.random() - 0.5) * 0.5;
                if (this.x < 140) this.x = 140;
                if (this.x > 160) this.x = 160;

                // Enter side condenser arm at y=100
                if (this.y <= 100) {
                    this.state = "condenser";
                }
            } else if (this.state === "condenser") {
                // Travel down condenser: line from (150, 100) to (290, 160)
                this.x += 1.5;
                this.y += 0.64;

                // Turn into drop/condense
                if (this.x >= 285) {
                    this.state = "distillate";
                    this.x = 295 + (Math.random() - 0.5) * 10;
                    this.y = 200 + (Math.random() - 0.5) * 8;
                    distillateCount++;
                }
            }
        }

        draw() {
            ctx.fillStyle = this.type === "acetone" ? "rgba(245, 158, 11, 0.8)" : "rgba(37, 99, 235, 0.8)";
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Populate initial molecules
    function resetMolecules() {
        particles = [];
        distillateCount = 0;
        for (let i = 0; i < 40; i++) {
            particles.push(new Molecule("acetone", 120 + Math.random() * 60, 170 + Math.random() * 35));
            particles.push(new Molecule("water", 120 + Math.random() * 60, 170 + Math.random() * 35));
        }
    }

    function drawDistillation() {
        const w = canvas.width;
        const h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        // Bunsen Burner flame (if temperature is high)
        const temp = parseFloat(tempSlider.value);
        if (temp > 40) {
            ctx.fillStyle = temp >= 100 ? "rgba(239, 68, 68, 0.7)" : "rgba(59, 130, 246, 0.6)";
            ctx.beginPath();
            ctx.moveTo(140, 245);
            ctx.quadraticCurveTo(150, 210 - (temp * 0.25), 160, 245);
            ctx.fill();
        }

        // Flask stand & burner outline
        ctx.fillStyle = "#64748b";
        ctx.fillRect(135, 245, 30, 8); // burner base

        // Draw Distillation Flask
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 3;
        ctx.beginPath();
        // Flask neck
        ctx.moveTo(142, 60);
        ctx.lineTo(142, 140);
        // Flask bulb
        ctx.arc(150, 180, 40, -Math.PI / 2.7, Math.PI * 1.37);
        ctx.lineTo(158, 140);
        ctx.lineTo(158, 60);
        ctx.closePath();
        ctx.stroke();

        // Condenser jacket around tube
        ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
        ctx.fillStyle = "rgba(56, 189, 248, 0.1)";
        ctx.lineWidth = 14;
        ctx.beginPath();
        ctx.moveTo(160, 104);
        ctx.lineTo(280, 156);
        ctx.stroke();

        // Inner delivery tube
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(154, 101);
        ctx.lineTo(290, 159);
        ctx.lineTo(290, 190);
        ctx.stroke();

        // Water Inlet & Outlet labels
        ctx.fillStyle = "#0284c7";
        ctx.font = "9px Outfit, sans-serif";
        ctx.fillText("Cold Water In", 250, 180);
        ctx.fillText("Water Out", 175, 85);

        // Draw collection beaker
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(270, 195);
        ctx.lineTo(270, 230);
        ctx.lineTo(320, 230);
        ctx.lineTo(320, 195);
        ctx.stroke();

        // Distillate liquid in beaker
        if (distillateCount > 0) {
            ctx.fillStyle = "rgba(245, 158, 11, 0.35)";
            const fillHeight = Math.min(22, distillateCount * 0.3);
            ctx.fillRect(272, 228 - fillHeight, 46, fillHeight);
        }

        // Draw molecules
        particles.forEach(p => {
            p.update(temp);
            p.draw();
        });
    }

    function loop() {
        drawDistillation();
        const temp = parseFloat(tempSlider.value);

        // Update info panel text dynamically based on temperature triggers
        if (temp < 40) {
            infoText.innerText = "Flask mixture contains Acetone (bp 56°C, orange) and Water (bp 100°C, blue). Heat is off.";
        } else if (temp >= 56 && temp < 95) {
            infoText.innerText = "Acetone (bp 56°C) is boiling and vaporizing! It condenses in the cold condenser jacket and drips as a pure distillate into the beaker.";
        } else if (temp >= 100) {
            infoText.innerText = "Extreme Heat! Water (bp 100°C) is now vaporizing as well. The distillate is no longer pure acetone!";
        } else {
            infoText.innerText = "Warming up... Temperature is below the boiling point of both components.";
        }

        animationId = requestAnimationFrame(loop);
    }

    tempSlider.addEventListener("input", (e) => {
        tempValue.innerText = e.target.value + " °C";
    });

    // Reset button
    const resetBtn = document.getElementById("dist-reset");
    if (resetBtn) {
        resetBtn.addEventListener("click", () => {
            tempSlider.value = 20;
            tempValue.innerText = "20 °C";
            resetMolecules();
        });
    }

    resetMolecules();
    loop();
}

/* ==========================================================================
   3. Separating Funnel Simulator
   ========================================================================== */
function initSeparatingFunnel() {
    const canvas = document.getElementById("funnel-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    const shakeBtn = document.getElementById("funnel-shake");
    const settleBtn = document.getElementById("funnel-settle");
    const valveSlider = document.getElementById("funnel-valve");
    const infoText = document.getElementById("funnel-info");

    let state = "separated"; // 'separated', 'emulsion', 'settling'
    let emulsionProgress = 0;
    let waterLevel = 75; // percentage of separating funnel capacity (0 to 100)
    let oilLevel = 50;   // volume of oil layer above water
    let isContaminated = false;

    // Droplets configuration for emulsion
    let droplets = [];
    for (let i = 0; i < 60; i++) {
        droplets.push({
            x: 100 + Math.random() * 100,
            y: 80 + Math.random() * 90,
            vx: (Math.random() - 0.5) * 4,
            vy: (Math.random() - 0.5) * 4,
            type: Math.random() > 0.4 ? "water" : "oil"
        });
    }

    function drawFunnel() {
        const w = canvas.width;
        const h = canvas.height;
        ctx.clearRect(0, 0, w, h);

        const funnelCenterX = w / 2;
        const funnelStartY = 50;

        // Draw lower beaker
        ctx.strokeStyle = "#64748b";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(w / 2 - 40, 240);
        ctx.lineTo(w / 2 - 40, h - 20);
        ctx.lineTo(w / 2 + 40, h - 20);
        ctx.lineTo(w / 2 + 40, 240);
        ctx.stroke();

        // Render contents inside the lower beaker (water collected)
        const collectedWaterHeight = (75 - waterLevel) * 1.5;
        if (collectedWaterHeight > 0) {
            ctx.fillStyle = "rgba(37, 99, 235, 0.4)";
            ctx.fillRect(w / 2 - 38, h - 20 - collectedWaterHeight, 76, collectedWaterHeight);
        }

        // Render contaminated oil in the beaker
        if (isContaminated) {
            ctx.fillStyle = "rgba(234, 179, 8, 0.4)";
            ctx.fillRect(w / 2 - 38, h - 20 - collectedWaterHeight - 8, 76, 8);
        }

        // Draw immiscible layers inside Separating Funnel
        if (state === "separated") {
            const funnelPath = () => {
                ctx.beginPath();
                ctx.arc(funnelCenterX, 90, 50, Math.PI, 0, false);
                ctx.lineTo(funnelCenterX + 12, 180);
                ctx.lineTo(funnelCenterX - 12, 180);
                ctx.closePath();
            };

            // Draw Oil layer (Yellow - top)
            if (oilLevel > 0 && (waterLevel + oilLevel) > 0) {
                ctx.save();
                funnelPath();
                ctx.clip();
                ctx.fillStyle = "rgba(234, 179, 8, 0.75)"; // yellow oil
                // fill from y=50 to y=180 depending on waterLevel + oilLevel
                const topY = 180 - ((waterLevel + oilLevel) * 1.3);
                ctx.fillRect(funnelCenterX - 60, topY, 120, oilLevel * 1.3);
                ctx.restore();
            }

            // Draw Water layer (Blue - bottom)
            if (waterLevel > 0) {
                ctx.save();
                funnelPath();
                ctx.clip();
                ctx.fillStyle = "rgba(37, 99, 235, 0.6)"; // blue water
                const topY = 180 - (waterLevel * 1.3);
                ctx.fillRect(funnelCenterX - 60, topY, 120, waterLevel * 1.3);
                ctx.restore();
            }
        } else if (state === "emulsion" || state === "settling") {
            // Draw droplets swirling
            ctx.save();
            ctx.beginPath();
            ctx.arc(funnelCenterX, 90, 50, Math.PI, 0, false);
            ctx.lineTo(funnelCenterX + 12, 180);
            ctx.lineTo(funnelCenterX - 12, 180);
            ctx.closePath();
            ctx.clip();

            // Background intermediate color
            ctx.fillStyle = "rgba(234, 215, 140, 0.4)";
            ctx.fill();

            droplets.forEach(d => {
                ctx.fillStyle = d.type === "water" ? "rgba(37, 99, 235, 0.8)" : "rgba(234, 179, 8, 0.8)";
                ctx.beginPath();
                ctx.arc(d.x, d.y, 4, 0, Math.PI * 2);
                ctx.fill();

                // Swirl movement physics
                if (state === "emulsion") {
                    d.x += d.vx;
                    d.y += d.vy;
                    // bounce off boundary approx
                    if (d.x < funnelCenterX - 45 || d.x > funnelCenterX + 45) d.vx *= -1;
                    if (d.y < 70 || d.y > 170) d.vy *= -1;
                } else if (state === "settling") {
                    // Gravitational settling downwards (water) and buoyancy upwards (oil)
                    if (d.type === "water") {
                        d.y += 0.8;
                        if (d.y > 175) d.y = 175;
                    } else {
                        d.y -= 0.6;
                        if (d.y < 65) d.y = 65;
                    }
                    d.x += (Math.random() - 0.5) * 0.5;
                }
            });
            ctx.restore();
        }

        // Draw glass funnel shape shell
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(funnelCenterX, 90, 50, Math.PI, 0, false);
        ctx.lineTo(funnelCenterX + 12, 180);
        ctx.lineTo(funnelCenterX + 12, 210); // valve section
        ctx.moveTo(funnelCenterX - 12, 180);
        ctx.lineTo(funnelCenterX - 12, 210);
        ctx.stroke();

        // Draw stopcock valve slider/plug
        const valveOpening = parseFloat(valveSlider.value);
        ctx.fillStyle = valveOpening > 0 ? "#ef4444" : "#10b981";
        ctx.fillRect(funnelCenterX - 18, 192, 36, 8);

        // Draw exit nozzle
        ctx.strokeStyle = "#475569";
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(funnelCenterX - 6, 210);
        ctx.lineTo(funnelCenterX - 6, 230);
        ctx.moveTo(funnelCenterX + 6, 210);
        ctx.lineTo(funnelCenterX + 6, 230);
        ctx.stroke();

        // Draw running fluid streamline
        if (valveOpening > 0 && state === "separated") {
            ctx.fillStyle = waterLevel > 0 ? "rgba(37, 99, 235, 0.7)" : "rgba(234, 179, 8, 0.7)";
            ctx.fillRect(funnelCenterX - 3, 210, 6, 35);
        }
    }

    function loopFunnel() {
        const valveOpening = parseFloat(valveSlider.value);

        if (state === "separated" && valveOpening > 0) {
            if (waterLevel > 0) {
                // Drain water
                waterLevel -= (valveOpening * 0.15);
                if (waterLevel < 0) waterLevel = 0;
            } else if (oilLevel > 0) {
                // Drain oil (contamination warning!)
                oilLevel -= (valveOpening * 0.15);
                isContaminated = true;
                if (oilLevel < 0) oilLevel = 0;
                infoText.innerHTML = "<span style='color:#ef4444; font-weight:bold;'><i class='fas fa-circle-exclamation'></i> Oil Leaked! Close the valve immediately to prevent mixture contamination!</span>";
            }
        }

        drawFunnel();

        if (state === "emulsion") {
            infoText.innerText = "Stirring the oil and water. An emulsion of tiny dispersed droplets is formed.";
        } else if (state === "settling") {
            emulsionProgress += 0.005;
            if (emulsionProgress >= 1) {
                state = "separated";
                infoText.innerText = "Mixture settled. Water (denser, blue) sits at the bottom; Oil (less dense, yellow) sits at the top.";
            } else {
                infoText.innerText = "Settle phase active. Gravitational force pulls heavier water drops down, buoyancy pushes lighter oil up.";
            }
        } else if (state === "separated" && valveOpening === 0) {
            infoText.innerText = "Ready to drain. Slide the stopcock valve to open and carefully drain the water layer.";
        }

        requestAnimationFrame(loopFunnel);
    }

    shakeBtn.addEventListener("click", () => {
        state = "emulsion";
        valveSlider.value = 0;
        isContaminated = false;
        // randomize droplet coordinates
        droplets.forEach(d => {
            d.x = w / 2 - 40 + Math.random() * 80;
            d.y = 70 + Math.random() * 100;
        });
    });

    settleBtn.addEventListener("click", () => {
        if (state !== "emulsion") return;
        state = "settling";
        emulsionProgress = 0;
    });

    // Initialize
    loopFunnel();
}
