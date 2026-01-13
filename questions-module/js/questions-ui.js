/* --- 2. STATUS TOGGLE --- */
function toggleStatus(id, type) {
    const card = document.getElementById(id);
    const btn = card.querySelector(type === 'important' ? '.imp-btn' : '.mast-btn');
    const storageKey = `${id}-${type}`;

    btn.classList.toggle('active');
    if (type === 'important') card.classList.toggle('is-important');
    if (type === 'mastered') card.classList.toggle('is-mastered');

    if (btn.classList.contains('active')) {
        localStorage.setItem(storageKey, 'true');
    } else {
        localStorage.removeItem(storageKey);
    }
}


/* --- 4. INITIAL LOAD --- */
window.addEventListener('DOMContentLoaded', () => {
    // Check Theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        document.getElementById('themeToggle').innerHTML = '☀';
    }

    // Check Card Status
    document.querySelectorAll('.question-card').forEach(card => {
        const id = card.id;
        if (localStorage.getItem(`${id}-important`)) {
            card.classList.add('is-important');
            card.querySelector('.imp-btn').classList.add('active');
        }
        if (localStorage.getItem(`${id}-mastered`)) {
            card.classList.add('is-mastered');
            card.querySelector('.mast-btn').classList.add('active');
        }
    });
});

