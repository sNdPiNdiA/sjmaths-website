// Auto-Timer Script
let timers = {};
let timerData = {};

let observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        const timerId = 't' + entry.target.id.substring(1);
        const box = document.getElementById('timer-box-' + timerId);
        if (entry.isIntersecting) {
            entry.target.classList.add('active-card');
            startTimer(timerId, box);
        } else {
            entry.target.classList.remove('active-card');
            stopTimer(timerId, box);
        }
    });
}, { root: null, rootMargin: '0px', threshold: 0.9 });

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

// Back to Top Button
const backToTopBtn = document.getElementById('backToTop');

if (backToTopBtn) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// --- Mark as Important Feature ---
document.addEventListener('DOMContentLoaded', initImportantMarking);

function initImportantMarking() {
    // Create a unique storage key based on the URL path
    const pageKey = window.location.pathname;
    const storageKey = `sjmaths_important_${pageKey}`;

    // Load saved data
    let importantQuestions = JSON.parse(localStorage.getItem(storageKey)) || [];

    document.querySelectorAll('.question-card').forEach(card => {
        const qId = card.id;
        const header = card.querySelector('.q-header');

        if (!header) return;

        // Create the Star Button
        const btn = document.createElement('button');
        btn.className = 'mark-important-btn';
        btn.innerHTML = '<i class="fas fa-star"></i>';
        btn.title = 'Mark as Important';
        btn.setAttribute('aria-label', 'Mark as Important');

        // Apply saved state
        if (importantQuestions.includes(qId)) {
            btn.classList.add('active');
            card.classList.add('important');
        }

        // Click Handler
        btn.addEventListener('click', () => {
            const isActive = btn.classList.toggle('active');
            card.classList.toggle('important', isActive);

            if (isActive) {
                if (!importantQuestions.includes(qId)) importantQuestions.push(qId);
            } else {
                importantQuestions = importantQuestions.filter(id => id !== qId);
            }
            localStorage.setItem(storageKey, JSON.stringify(importantQuestions));
        });

        // Inject into Header (Group with Timer for alignment)
        const timer = header.querySelector('.timer-box');
        if (timer) {
            const wrapper = document.createElement('div');
            wrapper.style.display = 'flex';
            wrapper.style.alignItems = 'center';
            wrapper.style.gap = '10px';

            // Insert wrapper before timer, then move timer and btn inside
            timer.parentNode.insertBefore(wrapper, timer);
            wrapper.appendChild(timer);
            wrapper.appendChild(btn);
        } else {
            header.appendChild(btn);
        }
    });
}

// --- Last Visited Tracker ---
document.addEventListener('DOMContentLoaded', () => {
    // Only track if we are on an actual exercise page (has questions)
    if (document.querySelector('.question-card')) {
        const pageTitle = document.title.replace(' | SJMaths', '').trim();

        const lastVisited = {
            title: pageTitle,
            url: window.location.href,
            timestamp: Date.now()
        };

        localStorage.setItem('sjmaths_last_visited', JSON.stringify(lastVisited));
    }
});