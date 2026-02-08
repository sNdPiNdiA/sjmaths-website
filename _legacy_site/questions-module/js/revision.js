
/* --- 3. REVISION MODE --- */
let revisionMode = false;
function toggleRevisionMode() {
    revisionMode = !revisionMode;
    const btn = document.getElementById('revisionModeBtn');
    const cards = document.querySelectorAll('.question-card');

    btn.classList.toggle('active');

    if (revisionMode) {
        btn.innerHTML = '<span id="modeIcon">●</span> Revision Mode: ON';
        let visibleCount = 0;
        cards.forEach(card => {
            if (card.classList.contains('is-important')) {
                card.style.display = "block";
                visibleCount++;
            } else {
                card.style.display = "none";
            }
        });
        if (visibleCount === 0) {
            if (window.showToast) window.showToast("No questions marked as Important yet!", "info");
            else console.log("No questions marked as Important yet!");
        }
    } else {
        btn.innerHTML = '<span id="modeIcon">○</span> Revision Mode: OFF';
        cards.forEach(card => card.style.display = "block");
    }
}