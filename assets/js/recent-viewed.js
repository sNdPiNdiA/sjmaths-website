/* =========================================
   RECENTLY VIEWED MODULE
   Tracks history and renders dashboard widget
   ========================================= */

const CONTENT_PATTERNS = [
    '/chapter-wise-notes/',
    '/ncert-exercise-practice/',
    '/previous-year-questions/',
    '/sample-papers/set',
    '/worksheets/',
    '/maths-mastery/'
];

const MAX_HISTORY_ITEMS = 4;
const STORAGE_KEY = 'sjmaths_recent_history';

document.addEventListener('DOMContentLoaded', () => {
    trackPageView();
    renderRecentViewed();
});

function trackPageView() {
    const path = window.location.pathname;

    // 1. Identify Content Pages (Exclude dashboards/lists)
    const isContentPage = CONTENT_PATTERNS.some(pattern => path.includes(pattern));

    // Exclude intermediate list pages (usually have 'dashboard-grid' class)
    if (!isContentPage || document.querySelector('.dashboard-grid')) return;

    // 2. Extract Metadata
    // Clean up title (remove site name)
    let pageTitle = document.title
        .split('|')[0]
        .split('-')[0]
        .replace('SJMaths', '')
        .trim();

    const url = window.location.href;

    // Determine Type & Icon
    let type = 'Resource';
    let icon = 'fa-file-alt';

    if (path.includes('notes')) { type = 'Notes'; icon = 'fa-book-open'; }
    else if (path.includes('ncert')) { type = 'Solution'; icon = 'fa-pen-nib'; }
    else if (path.includes('pyq') || path.includes('questions')) { type = 'PYQ'; icon = 'fa-history'; }
    else if (path.includes('sample')) { type = 'Sample Paper'; icon = 'fa-file-contract'; }
    else if (path.includes('mastery')) { type = 'Concept'; icon = 'fa-brain'; }

    const item = {
        title: pageTitle || 'Untitled Resource',
        url: url,
        type: type,
        icon: icon,
        timestamp: Date.now()
    };

    // 3. Update LocalStorage
    let history = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    // Remove duplicates (move to top)
    history = history.filter(i => i.url !== url);

    // Add new item to start
    history.unshift(item);

    // Limit to 4 items
    if (history.length > MAX_HISTORY_ITEMS) history.pop();

    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
}

function renderRecentViewed() {
    const container = document.getElementById('recent-viewed-container');
    if (!container) return;

    const history = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

    if (history.length === 0) {
        container.style.display = 'none';
        return;
    }

    // Render HTML
    container.innerHTML = `
        <div class="recent-section">
            <div class="section-header-recent">
                <h2><i class="fas fa-history"></i> Pick up where you left off</h2>
                <button onclick="clearRecentHistory()" class="clear-btn">Clear</button>
            </div>
            <div class="recent-grid">
                ${history.map(item => `
                    <a href="${item.url}" class="recent-card">
                        <div class="recent-icon"><i class="fas ${item.icon}"></i></div>
                        <div class="recent-info">
                            <span class="recent-type">${item.type}</span>
                            <h4 class="recent-title">${item.title}</h4>
                        </div>
                    </a>
                `).join('')}
            </div>
        </div>
    `;

    container.style.display = 'block';
}

// Global function to clear history
window.clearRecentHistory = function () {
    localStorage.removeItem(STORAGE_KEY);
    const container = document.getElementById('recent-viewed-container');
    if (container) container.style.display = 'none';
}