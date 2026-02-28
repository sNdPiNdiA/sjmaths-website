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

    _initFloatingTOC();
    _wrapMathJaxClass12();
});

/* ── HELPERS ── */

function _initFloatingTOC() {
    // Target h2 in .sj-card
    const headings = Array.from(document.querySelectorAll('.sj-card h2')).filter(h => h.offsetParent !== null);

    if (headings.length < 2) return;

    const toc = document.createElement('nav');
    toc.className = 'floating-toc';
    const list = document.createElement('ul');

    headings.forEach((h, i) => {
        if (!h.id) h.id = `section-${i}`;
        const id = h.id;

        const li = document.createElement('li');
        const a = document.createElement('a');
        a.href = `#${id}`;
        // Remove "Step X:" prefix if present for cleaner TOC
        let text = h.textContent.replace(/^Step \d+:/, '').replace(/^Q\d+\./, '').trim();
        // Truncate if too long
        if (text.length > 35) text = text.substring(0, 32) + '...';

        a.innerHTML = `<span class="toc-num">${i + 1}</span><span class="toc-text">${text}</span>`;

        a.addEventListener('click', e => {
            e.preventDefault();
            const target = document.getElementById(id);
            const headerOffset = 100;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.scrollY - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: "smooth"
            });
        });

        li.appendChild(a);
        list.appendChild(li);
    });

    toc.appendChild(list);
    document.body.appendChild(toc);

    // Scroll Spy (Throttled)
    let rafId = null;
    window.addEventListener('scroll', () => {
        if (rafId) return;
        rafId = requestAnimationFrame(() => {
            const scrollPos = window.scrollY;
            let currentId = '';

            headings.forEach(h => {
                if (scrollPos >= h.offsetTop - 150) {
                    currentId = h.id;
                }
            });

            const links = toc.querySelectorAll('a');
            links.forEach(link => {
                link.classList.toggle('active', link.getAttribute('href') === `#${currentId}`);
            });
            rafId = null;
        });
    }, { passive: true });
}

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
