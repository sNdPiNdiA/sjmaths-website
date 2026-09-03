/* Chapter 6: How Forces Affect Motion — Interactive Simulations */
function startForcesSimulation() {
    /* ---- Force Calculator (F = ma) ---- */
    const massEl = document.getElementById("fc-mass");
    const accEl = document.getElementById("fc-acc");
    const massValEl = document.getElementById("fc-mass-val");
    const accValEl = document.getElementById("fc-acc-val");
    const resultEl = document.getElementById("fc-result");

    function updateForceCalculator() {
        if (!massEl || !accEl || !massValEl || !accValEl || !resultEl) return;
        const m = parseFloat(massEl.value);
        const a = parseFloat(accEl.value);
        const F = m * a;
        massValEl.textContent = m;
        accValEl.textContent = a.toFixed(1);
        resultEl.textContent = F.toFixed(1) + " N";
    }

    if (massEl && accEl) {
        massEl.addEventListener("input", updateForceCalculator);
        accEl.addEventListener("input", updateForceCalculator);
        updateForceCalculator();
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startForcesSimulation);
} else {
    startForcesSimulation();
}
