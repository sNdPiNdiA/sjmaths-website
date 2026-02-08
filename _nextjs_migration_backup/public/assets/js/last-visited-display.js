document.addEventListener('DOMContentLoaded', () => {
    const lvContainer = document.getElementById('last-visited-container');
    const lastVisitedData = JSON.parse(localStorage.getItem('sjmaths_last_visited'));

    if (lvContainer && lastVisitedData) {
        lvContainer.innerHTML = `
            <div class="last-visited-section">
                <div class="lv-content">
                    <h3><i class="fas fa-history"></i> Pick up where you left off</h3>
                    <h2>${lastVisitedData.title}</h2>
                </div>
                <a href="${lastVisitedData.url}" class="lv-btn">Continue <i class="fas fa-arrow-right"></i></a>
            </div>
        `;
        lvContainer.style.display = 'block';
    }
});