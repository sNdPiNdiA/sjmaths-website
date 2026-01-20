document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle Logic
    const toggleBtn = document.querySelector('.mobile-toggle');
    const nav = document.querySelector('nav');
    
    if (toggleBtn && nav) {
        toggleBtn.addEventListener('click', () => {
            nav.classList.toggle('active');
            const icon = toggleBtn.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
            }
        });
    }
});

function toggleChapter(header) {
    const item = header.parentElement;
    const panel = item.querySelector('.exercise-panel');

    // Exclusive Accordion behavior (closes others when one opens)
    document.querySelectorAll('.chapter-item.active').forEach(openItem => {
        if (openItem !== item) {
            openItem.classList.remove('active');
            openItem.querySelector('.exercise-panel').style.maxHeight = null;
        }
    });

    // Toggle current chapter
    item.classList.toggle('active');

    if (item.classList.contains('active')) {
        panel.style.maxHeight = panel.scrollHeight + "px";
    } else {
        panel.style.maxHeight = null;
    }
}