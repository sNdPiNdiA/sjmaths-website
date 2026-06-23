/**
 * Shared logic for Class 9 Revision Notes
 * Includes: Scroll Animations, Accordion Toggles, Quiz Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('Class 9 Notes JS Loaded');
    initClass9NotesScrollAnimations();
});

// --- SCROLL ANIMATIONS ---
function initClass9NotesScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    // Elements to animate
    const elementsToAnimate = document.querySelectorAll('.note-section, .accordion-item, .quiz-container, .card, .interactive-box');
    elementsToAnimate.forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });
}

// --- ACCORDION LOGIC ---
function toggleAccordion(header) {
    header.classList.toggle('active');
    const body = header.nextElementSibling;
    const icon = header.querySelector('.fa-chevron-down, .fa-chevron-up');

    if (body.classList.contains('open')) {
        body.classList.remove('open');
        icon.classList.remove('fa-chevron-up');
        icon.classList.add('fa-chevron-down');
    } else {
        body.classList.add('open');
        icon.classList.remove('fa-chevron-down');
        icon.classList.add('fa-chevron-up');
    }
}

// --- QUIZ LOGIC ---
function checkQuiz(element, isCorrect) {
    const parent = element.parentElement;
    const options = parent.querySelectorAll('.quiz-option');
    options.forEach(opt => opt.style.pointerEvents = 'none'); // Disable clicks

    if (isCorrect) {
        element.classList.add('correct', 'pop');
        element.innerHTML += ' <i class="fas fa-check-circle"></i>';
    } else {
        element.classList.add('wrong', 'shake');
        element.innerHTML += ' <i class="fas fa-times-circle"></i>';

        // Find and highlight correct answer
        setTimeout(() => {
            const correctOpt = Array.from(options).find(opt => opt.getAttribute('onclick')?.includes('true'));
            if (correctOpt) {
                correctOpt.classList.add('correct', 'pop');
                correctOpt.innerHTML += ' <i class="fas fa-check-circle"></i>';
            }
        }, 500);
    }
}
