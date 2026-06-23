/**
 * Interactive Notes Enhancements
 * Features: Scroll Animations, Progress Tracking, Floating ToC
 */

document.addEventListener('DOMContentLoaded', () => {
    // Defer non-critical UI enhancements to unblock main thread
    requestAnimationFrame(() => {
        initNotesScrollAnimations();
        initProgressBar();
        initFloatingToC();
        enhanceToggles();
    });
});

// --- 1. SCROLL ANIMATIONS ---
function initNotesScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Select elements to animate
    const elements = document.querySelectorAll('.sj-card, .box-ncert, .box-formula, .box-pyq');

    // Batch DOM writes: Use requestAnimationFrame or simply iterate
    // Adding classes is generally fast, but grouping them helps
    requestAnimationFrame(() => {
        elements.forEach((el, index) => {
            el.classList.add('animate-on-scroll');
            // Add staggered delays for groups
            if (index % 3 === 1) el.classList.add('delay-100');
            if (index % 3 === 2) el.classList.add('delay-200');
            observer.observe(el);
        });
    });
}

// --- 2. CHECKLIST PROGRESS BAR ---
function initProgressBar() {
    const checkboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');
    if (!checkboxes.length) return;

    // Create progress bar element
    const progressContainer = document.createElement('div');
    progressContainer.className = 'progress-container';
    progressContainer.innerHTML = '<div class="progress-bar" id="readingProgress"></div>';
    document.body.prepend(progressContainer);

    const progressBar = document.getElementById('readingProgress');

    function updateProgress() {
        const total = checkboxes.length;
        const checked = document.querySelectorAll('.checklist-item input[type="checkbox"]:checked').length;
        const percentage = (checked / total) * 100;
        progressBar.style.width = `${percentage}%`;

        // Optional: Change color on completion
        if (percentage === 100) {
            progressBar.style.background = '#00C853'; // Bright Green
        }
    }

    checkboxes.forEach(cb => {
        cb.addEventListener('change', updateProgress);
    });

    // Initial update
    setTimeout(updateProgress, 500); // Delay to allow storage to load
}

// --- 3. FLOATING TABLE OF CONTENTS ---
function initFloatingToC() {
    const headers = document.querySelectorAll('h2');

    // Phase 1: READ (Check visibility and text) - Do this BEFORE any DOM writes
    const validHeaders = [];
    headers.forEach((header, index) => {
        const text = header.innerText.trim();
        // offsetParent triggers reflow, so do this before appending anything new
        if (text && header.offsetParent !== null) {
            validHeaders.push({ element: header, text: text, index: index });
        }
    });

    // Phase 2: WRITE (Create and Append Elements)
    // Now it's safe to write to DOM without causing thrashing against the previous reads
    const tocContainer = document.createElement('div');
    tocContainer.className = 'floating-toc';
    tocContainer.id = 'floatingToC';
    tocContainer.innerHTML = `
        <div class="toc-header">
            <span>Quick Nav</span>
            <i class="fas fa-times" id="closeToC" style="cursor:pointer;"></i>
        </div>
        <ul class="toc-list" id="tocList"></ul>
    `;
    document.body.appendChild(tocContainer);

    const toggleBtn = document.createElement('div');
    toggleBtn.className = 'toc-toggle';
    toggleBtn.id = 'tocToggle';
    toggleBtn.innerHTML = '<i class="fas fa-list-ul"></i>';
    toggleBtn.title = "Table of Contents";
    document.body.appendChild(toggleBtn);

    const tocList = document.getElementById('tocList');

    const tocItems = validHeaders.map(item => {
        const id = item.element.id || `section-${item.index}`;
        item.element.id = id; // Write ID if missing

        return `<li class="toc-item">
            <a href="#${id}" class="toc-link">${item.text}</a>
        </li>`;
    });

    tocList.innerHTML = tocItems.join('');

    // Add click listeners (delegated)
    tocList.addEventListener('click', (e) => {
        if (e.target.classList.contains('toc-link')) {
            e.preventDefault();
            const targetId = e.target.getAttribute('href').substring(1);
            document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });

            if (window.innerWidth < 1200) {
                tocContainer.classList.remove('active');
            }
        }
    });

    // 4. Toggle Logic
    const closeBtn = document.getElementById('closeToC');

    function toggleToC() {
        tocContainer.classList.toggle('active');
    }

    toggleBtn.addEventListener('click', toggleToC);
    closeBtn.addEventListener('click', toggleToC);

    // 5. Scroll Spy (Highlight active section using IntersectionObserver)
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -60% 0px', // Active when near top of viewport
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                document.querySelectorAll('.toc-link').forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    headers.forEach(header => observer.observe(header));
}

// --- 4. ENHANCED TOGGLES ---
function enhanceToggles() {
    // Override the default inline toggle function
    window.toggleAnswer = function (id) {
        const block = document.getElementById(id);
        const btn = event.currentTarget || document.querySelector(`button[onclick="toggleAnswer('${id}')"]`);
        const icon = btn.querySelector('i');

        // Use class-based toggling for CSS transitions
        if (block.classList.contains('show')) {
            block.classList.remove('show');
            setTimeout(() => { block.style.display = 'none'; }, 400); // Wait for transition
            icon.className = 'fas fa-chevron-down';
            btn.innerHTML = `Show Answer <i class="fas fa-chevron-down"></i>`;
        } else {
            block.style.display = 'block';
            // Small delay to allow display:block to apply before adding class for transition
            setTimeout(() => { block.classList.add('show'); }, 10);
            icon.className = 'fas fa-chevron-up';
            btn.innerHTML = `Hide Answer <i class="fas fa-chevron-up"></i>`;
        }
    };
}
