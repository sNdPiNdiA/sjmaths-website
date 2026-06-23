/**
 * Shared logic for Class 12 Revision Notes
 */

document.addEventListener('DOMContentLoaded', () => {
    // Initialize solution toggles
    window.toggleAnswer = function (id) {
        const block = document.getElementById(id);
        const btn = event.currentTarget;
        const icon = btn.querySelector('i');

        if (block.style.display === 'block') {
            block.style.display = 'none';
            icon.classList.replace('fa-chevron-up', 'fa-chevron-down');
            btn.innerHTML = `Check Answer <i class="fas fa-chevron-down"></i>`;
        } else {
            block.style.display = 'block';
            icon.classList.replace('fa-chevron-down', 'fa-chevron-up');
            btn.innerHTML = `Hide Answer <i class="fas fa-chevron-up"></i>`;
        }
    };

    // Initialize Checklist Persistence
    const chapterId = document.body.dataset.chapter;
    const classId = document.body.dataset.class;

    if (chapterId && classId) {
        const storageKey = `checklist-class${classId}-ch${chapterId}`;
        const checkboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');

        // Load state
        const savedState = JSON.parse(localStorage.getItem(storageKey) || '{}');
        checkboxes.forEach((cb, index) => {
            if (savedState[index]) {
                cb.checked = true;
                cb.closest('.checklist-item').classList.add('checked');
            }

            // Save on change
            cb.addEventListener('change', () => {
                const updatedState = JSON.parse(localStorage.getItem(storageKey) || '{}');
                updatedState[index] = cb.checked;
                localStorage.setItem(storageKey, JSON.stringify(updatedState));

                if (cb.checked) {
                    cb.closest('.checklist-item').classList.add('checked');
                } else {
                    cb.closest('.checklist-item').classList.remove('checked');
                }
            });
        });
    }

    _wrapMathJaxClass12();
});

/* ── HELPERS ── */


function _wrapMathJaxClass12() {
    // Simple wrapper for MathJax to prevent overflow on mobile
    if (window.MathJax && window.MathJax.startup) {
        window.MathJax.startup.promise.then(() => {
            const displayMath = document.querySelectorAll('mjx-container[display="true"]');
            displayMath.forEach(el => {
                if (!el.parentElement.classList.contains('math-scroll')) {
                    const wrapper = document.createElement('div');
                    wrapper.className = 'math-scroll';
                    // Inline styles if CSS missing
                    wrapper.style.overflowX = 'auto';
                    wrapper.style.margin = '1rem 0';
                    el.parentNode.insertBefore(wrapper, el);
                    wrapper.appendChild(el);
                }
            });
        });
    } else if (window.MathJax) {
        // Fallback: If startup is not yet ready, wait for it or try again shortly
        setTimeout(_wrapMathJaxClass12, 100);
    }
}
