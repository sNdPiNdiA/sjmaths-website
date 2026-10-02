/* =========================================
   RECENTLY VIEWED MODULE
   Tracks history and renders dashboard widget
   ========================================= */

(function () {
'use strict';
if (window.SJRecentViewed) return;

const CONTENT_PATTERNS = [
    '/chapter-wise-notes/',
    '/ncert-exercise-practice/',
    '/previous-year-questions/',
    '/sample-papers/set',
    '/worksheets/',
    '/tests/'
];

const MAX_HISTORY_ITEMS = 4;
const STORAGE_KEY = 'sjmaths_recent_history';

function initRecentViewed() {
    trackPageView();
    renderRecentViewed();
}

// Keep dashboard and mobile navigation on the same validated history store.
function getHistory() {
    let stored;
    try { stored = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'); }
    catch (error) {
        console.warn('SJMaths recent history could not be read:', error);
        return [];
    }
    if (!Array.isArray(stored)) return [];
    return stored.filter(item => {
        if (!item || typeof item.title !== 'string' || typeof item.url !== 'string') return false;
        try {
            const url = new URL(item.url, location.origin);
            return url.origin === location.origin && ['http:', 'https:'].includes(url.protocol);
        } catch { return false; }
    }).slice(0, MAX_HISTORY_ITEMS).map(item => ({
        ...item, type: typeof item.type === 'string' ? item.type : 'Resource',
        icon: /^fa-[a-z0-9-]+$/.test(item.icon) ? item.icon : 'fa-file-alt'
    }));
}

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
        .replace(/\s*[-–—]\s*SJMaths.*$/i, '')
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
    let history = getHistory();

    // Remove duplicates (move to top)
    history = history.filter(i => i.url !== url);

    // Add new item to start
    history.unshift(item);

    // Limit to 4 items
    if (history.length > MAX_HISTORY_ITEMS) history.pop();

    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(history)); }
    catch (error) { console.warn('SJMaths recent history could not be saved:', error); }
}

function renderRecentViewed() {
    const container = document.getElementById('recent-viewed-container');
    if (!container) return;

    const history = getHistory();

    if (history.length === 0) {
        container.style.display = 'none';
        return;
    }

    // Render the static shell; stored lesson titles are always text, never HTML.
    container.innerHTML = `
        <div class="recent-section">
            <div class="section-header-recent">
                <h2><i class="fas fa-history"></i> Pick up where you left off</h2>
                <button type="button" class="clear-btn">Clear</button>
            </div>
            <div class="recent-grid">
            </div>
        </div>
    `;
    container.querySelector('.clear-btn').addEventListener('click', window.clearRecentHistory);
    const grid = container.querySelector('.recent-grid');
    history.forEach(item => {
        const link = document.createElement('a');
        link.className = 'recent-card';
        link.href = item.url;
        const icon = document.createElement('div');
        icon.className = 'recent-icon';
        const glyph = document.createElement('i');
        glyph.className = `fas ${item.icon}`;
        icon.append(glyph);
        const info = document.createElement('div');
        info.className = 'recent-info';
        const type = document.createElement('span');
        type.className = 'recent-type';
        type.textContent = item.type;
        const title = document.createElement('h4');
        title.className = 'recent-title';
        title.textContent = item.title;
        info.append(type, title);
        link.append(icon, info);
        grid.append(link);
    });

    container.style.display = 'block';
}

// Global function to clear history
window.clearRecentHistory = function () {
    localStorage.removeItem(STORAGE_KEY);
    const container = document.getElementById('recent-viewed-container');
    if (container) container.style.display = 'none';
}
window.SJRecentViewed = { getHistory };
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initRecentViewed, { once: true });
else initRecentViewed();
})();
