/**
 * Shared logic for Class 9 Revision Notes
 * Includes: Accordion Toggles, Quiz Logic
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('Class 9 Notes JS Loaded');
});

// --- ACCORDION LOGIC ---
function toggleAccordion(header) {
    header.classList.toggle('active');
    const body = header.nextElementSibling;
    if (body.style.display === "block") {
        body.style.display = "none";
        header.querySelector('i').classList.remove('fa-chevron-up');
        header.querySelector('i').classList.add('fa-chevron-down');
    } else {
        body.style.display = "block";
        header.querySelector('i').classList.remove('fa-chevron-down');
        header.querySelector('i').classList.add('fa-chevron-up');
    }
}

// --- QUIZ LOGIC ---
function checkQuiz(element, isCorrect) {
    const parent = element.parentElement;
    const options = parent.querySelectorAll('.quiz-option');
    options.forEach(opt => opt.style.pointerEvents = 'none'); // Disable clicks

    if (isCorrect) {
        element.classList.add('correct');
        element.innerHTML += ' <i class="fas fa-check-circle"></i>';
    } else {
        element.classList.add('wrong');
        element.innerHTML += ' <i class="fas fa-times-circle"></i>';
        // Find and highlight correct answer
        options.forEach(opt => {
            if (opt.getAttribute('onclick').includes('true')) {
                opt.classList.add('correct');
            }
        });
    }
}
