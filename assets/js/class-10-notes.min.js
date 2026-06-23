/**
 * class-10-notes.js
 * Shared interactivity for Class 10 Chapter Notes.
 * Includes: Scroll Animations, Quiz Logic with visual feedback.
 */

document.addEventListener('DOMContentLoaded', () => {
    initClass10NotesScrollAnimations();
});

// --- SCROLL ANIMATIONS (IntersectionObserver) ---
function initClass10NotesScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Once visible, stop observing — only animate in once
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.08 });

    // Target the key layout elements used across Class 10 notes
    const targets = document.querySelectorAll(
        '.sj-card, .calc-box, .box-ncert, .box-formula, .box-pyq, ' +
        '.box-mistake, .box-tip, .accordion-item, .quiz-container'
    );

    targets.forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });
}

// --- ACCORDION TOGGLE (smooth open/close) ---
function toggleAccordion(header) {
    const body = header.nextElementSibling;
    const icon = header.querySelector('.fa-chevron-down, .fa-chevron-up');

    if (body && body.classList.contains('accordion-body')) {
        if (body.classList.contains('open')) {
            body.classList.remove('open');
            if (icon) {
                icon.classList.replace('fa-chevron-up', 'fa-chevron-down');
            }
            header.classList.remove('active');
        } else {
            body.classList.add('open');
            if (icon) {
                icon.classList.replace('fa-chevron-down', 'fa-chevron-up');
            }
            header.classList.add('active');
        }
    }
}

// --- QUIZ LOGIC (with shake/pop animations) ---
function checkQuiz(element, isCorrect) {
    const parent = element.parentElement;
    const options = parent.querySelectorAll('.quiz-option');
    options.forEach(opt => {
        opt.style.pointerEvents = 'none'; // Disable all further clicks
    });

    if (isCorrect) {
        element.classList.add('correct', 'pop');
        element.innerHTML += ' <i class="fas fa-check-circle"></i>';
    } else {
        element.classList.add('wrong', 'shake');
        element.innerHTML += ' <i class="fas fa-times-circle"></i>';

        // Highlight the correct answer after a short delay
        setTimeout(() => {
            const correctOpt = Array.from(options).find(
                opt => opt.getAttribute('onclick')?.includes('true')
            );
            if (correctOpt && !correctOpt.classList.contains('correct')) {
                correctOpt.classList.add('correct', 'pop');
                correctOpt.innerHTML += ' <i class="fas fa-check-circle"></i>';
            }
        }, 500);
    }
}

// --- SCROLL PROGRESS BAR (if element exists in page) ---
let ticking = false;
window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            const bar = document.getElementById('myBar');
            if (bar) {
                const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
                const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                bar.style.width = scrollHeight > 0 ? (scrollTop / scrollHeight * 100) + '%' : '0%';
            }
            ticking = false;
        });
        ticking = true;
    }
}, { passive: true });
