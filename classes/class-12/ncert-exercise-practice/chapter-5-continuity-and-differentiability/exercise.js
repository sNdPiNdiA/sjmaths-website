// Auto-Timer Script
let timers = {};
let timerData = {};

let observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        const cardId = entry.target.id;
        const timerId = 't' + cardId.substring(1);
        const box = document.getElementById('timer-box-' + timerId);

        if (entry.isIntersecting) {
            entry.target.classList.add('active-card');
            startTimer(timerId, box);
        } else {
            entry.target.classList.remove('active-card');
            stopTimer(timerId, box);
        }
    });
}, { root: null, rootMargin: '0px', threshold: 0.6 });

document.querySelectorAll('.question-card').forEach(card => {
    observer.observe(card);
    const qId = card.id.substring(1);
    timerData['t' + qId] = 0;
});

function startTimer(timerId, box) {
    if (timers[timerId]) return;
    if (box) box.classList.add('running');
    timers[timerId] = setInterval(() => {
        timerData[timerId]++;
        const m = Math.floor(timerData[timerId] / 60).toString().padStart(2, '0');
        const s = (timerData[timerId] % 60).toString().padStart(2, '0');
        const display = document.getElementById(timerId);
        if (display) display.innerText = `${m}:${s}`;
    }, 1000);
}

function stopTimer(timerId, box) {
    if (timers[timerId]) { clearInterval(timers[timerId]); delete timers[timerId]; }
    if (box) box.classList.remove('running');
}

function toggleSolution(id, btn) {
    var content = document.getElementById(id);
    var isCurrentlyOpen = content.style.display === "block";
    document.querySelectorAll('.solution-content').forEach(el => el.style.display = "none");
    document.querySelectorAll('.solution-btn').forEach(el => {
        el.classList.remove('active');
        el.innerHTML = '<i class="fas fa-eye"></i> Show Solution';
    });
    if (!isCurrentlyOpen) {
        content.style.display = "block";
        btn.classList.add('active');
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Solution';
    }
}