(function () {
    let searchIndex = [];
    let isIndexLoaded = false;
    let searchIndexPromise = null;
    let selectedIndex = -1;
    let filteredResults = [];

    // 1. Inject Premium Search Modal
    function injectSearchModal() {
        if (document.getElementById('search-overlay')) return;

        const overlay = document.createElement('div');
        overlay.id = 'search-overlay';
        overlay.className = 'search-overlay';
        overlay.innerHTML = `
            <div class="search-modal">
                <div class="search-modal-header">
                    <i class="fas fa-search"></i>
                    <input type="text" id="search-modal-input" class="search-modal-input" placeholder="Search for anything (chapters, exercises, topics)..." autocomplete="off">
                    <button class="search-modal-close">ESC</button>
                </div>
                <div id="search-results-viewport" class="search-results-viewport">
                    <div class="search-empty">
                        <i class="fas fa-keyboard"></i>
                        <p>Start typing to search...</p>
                    </div>
                </div>
                <div class="search-modal-footer">
                    <div class="kb-hint"><span class="kb-key">↑↓</span> to navigate</div>
                    <div class="kb-hint"><span class="kb-key">ENTER</span> to select</div>
                    <div class="kb-hint"><span class="kb-key">ESC</span> to close</div>
                </div>
            </div>
        `;
        document.body.appendChild(overlay);

        // Add CSS if not yet added
        if (!document.querySelector('link[href*="search-premium.css"]')) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = '/assets/css/search-premium.css';
            document.head.appendChild(link);
        }

        // Event Listeners for the Modal
        const input = overlay.querySelector('#search-modal-input');
        const closeBtn = overlay.querySelector('.search-modal-close');

        input.addEventListener('input', (e) => handleSearch(e.target.value));
        input.addEventListener('keydown', handleKeydown);
        closeBtn.addEventListener('click', closeSearch);
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) closeSearch();
        });
    }

    // 2. Search Logic
    function handleSearch(query) {
        const viewport = document.getElementById('search-results-viewport');
        const term = query.trim().toLowerCase();

        if (term.length < 2) {
            viewport.innerHTML = `
                <div class="search-empty">
                    <i class="fas fa-keyboard"></i>
                    <p>Type at least 2 characters...</p>
                </div>
            `;
            filteredResults = [];
            selectedIndex = -1;
            return;
        }

        if (!isIndexLoaded) {
            viewport.innerHTML = '<div class="search-empty"><i class="fas fa-spinner fa-spin"></i><p>Loading index...</p></div>';
            loadSearchIndex()
                .then(() => {
                    const input = document.getElementById('search-modal-input');
                    if (input && input.value.trim().toLowerCase() === term) {
                        handleSearch(input.value);
                    }
                })
                .catch(() => {
                    const input = document.getElementById('search-modal-input');
                    if (input && input.value.trim().toLowerCase() === term) {
                        viewport.innerHTML = '<div class="search-empty"><i class="fas fa-exclamation-circle"></i><p>Search is temporarily unavailable. Please try again.</p></div>';
                    }
                });
            return;
        }

        // Filter and Group
        filteredResults = searchIndex.filter(item =>
            String(item.title || '').toLowerCase().includes(term) ||
            (Array.isArray(item.tags) && item.tags.some(tag => String(tag).toLowerCase().includes(term)))
        ).slice(0, 15); // Limit results for performance

        renderResults(filteredResults, term);
    }

    function renderResults(results, term) {
        const viewport = document.getElementById('search-results-viewport');
        if (results.length === 0) {
            viewport.innerHTML = `<div class="search-empty"><i class="fas fa-search"></i><p>No results found for "${escapeHtml(term)}"</p></div>`;
            selectedIndex = -1;
            return;
        }

        // Grouping by Category
        const groups = {};
        results.forEach(item => {
            const cat = item.category || 'General';
            if (!groups[cat]) groups[cat] = [];
            groups[cat].push(item);
        });

        let html = '';
        Object.keys(groups).forEach(cat => {
            html += `<div class="search-group-title">${escapeHtml(cat)}</div>`;
            groups[cat].forEach(item => {
                const icon = getIconForUrl(item.url);
                const safeUrl = getSafeSearchUrl(item.url);
                html += `
                    <a href="${escapeHtml(safeUrl)}" class="search-item" data-url="${escapeHtml(safeUrl)}">
                        <div class="search-item-icon"><i class="${icon}"></i></div>
                        <div class="search-item-info">
                            <span class="search-item-title">${highlightMatch(String(item.title || ''), term)}</span>
                            <span class="search-item-path">${escapeHtml(String(item.url || ''))}</span>
                        </div>
                    </a>
                `;
            });
        });

        viewport.innerHTML = html;
        selectedIndex = -1; // Reset selection on new render
    }

    function highlightMatch(text, term) {
        const safeText = escapeHtml(text);
        const escapedTerm = escapeRegExp(term);
        if (!escapedTerm) return safeText;
        const regex = new RegExp(`(${escapedTerm})`, 'gi');
        return safeText.replace(regex, '<strong>$1</strong>');
    }

    function escapeHtml(value) {
        return String(value ?? '').replace(/[&<>"']/g, (character) => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        })[character]);
    }

    function escapeRegExp(value) {
        return String(value ?? '').replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function getSafeSearchUrl(value) {
        try {
            const url = new URL(String(value || ''), window.location.origin);
            if (url.origin !== window.location.origin || !url.pathname.startsWith('/')) return '#';
            return `${url.pathname}${url.search}${url.hash}`;
        } catch {
            return '#';
        }
    }

    function getIconForUrl(url) {
        if (url.includes('exercise')) return 'fas fa-pen-nib';
        if (url.includes('chapter')) return 'fas fa-book';
        if (url.includes('test')) return 'fas fa-file-alt';
        if (url.includes('formula')) return 'fas fa-square-root-alt';
        return 'fas fa-link';
    }

    // 3. Modal Controls
    function openSearch() {
        injectSearchModal();
        const overlay = document.getElementById('search-overlay');
        overlay.classList.add('active');
        document.body.style.overflow = 'hidden';

        const input = document.getElementById('search-modal-input');
        setTimeout(() => input.focus(), 100);

        loadSearchIndex().catch(() => {
            // A typed query displays the actionable error state and retries.
        }); // Pre-emptive load
    }

    function closeSearch() {
        const overlay = document.getElementById('search-overlay');
        if (overlay) {
            overlay.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    // 4. Keyboard Navigation
    function handleKeydown(e) {
        const items = document.querySelectorAll('.search-item');

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
            updateSelection(items);
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            selectedIndex = Math.max(selectedIndex - 1, 0);
            updateSelection(items);
        } else if (e.key === 'Enter') {
            if (selectedIndex >= 0 && items[selectedIndex]) {
                window.location.href = items[selectedIndex].getAttribute('href');
            }
        } else if (e.key === 'Escape') {
            e.preventDefault();
            closeSearch();
        }
    }

    function updateSelection(items) {
        items.forEach((item, i) => {
            if (i === selectedIndex) {
                item.classList.add('selected');
                item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
            } else {
                item.classList.remove('selected');
            }
        });
    }

    // 5. Data Loading
    function loadSearchIndex() {
        if (isIndexLoaded) return Promise.resolve(searchIndex);
        if (searchIndexPromise) return searchIndexPromise;

        searchIndexPromise = fetch('/assets/js/search-index.json')
            .then(res => {
                if (!res.ok) throw new Error(`Search index request failed with ${res.status}`);
                return res.json();
            })
            .then(data => {
                searchIndex = data;
                isIndexLoaded = true;
                return searchIndex;
            })
            .catch(err => {
                searchIndexPromise = null;
                console.error('Search index failed:', err);
                throw err;
            });

        return searchIndexPromise;
    }

    // 6. Global Event Listeners (Triggers)
    document.addEventListener('keydown', (e) => {
        // Cmd/Ctrl + K or /
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
            e.preventDefault();
            openSearch();
        }
        if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            e.preventDefault();
            openSearch();
        }
    });

    // Intercept existing search inputs
    document.addEventListener('focusin', (e) => {
        if (e.target.matches('.header-search input, #searchInput, #site-search')) {
            e.target.blur();
            openSearch();
        }
    });

    document.addEventListener('click', (e) => {
        if (e.target.closest('.header-search button, #searchBtn, #mobileSearchBtn')) {
            e.preventDefault();
            openSearch();
        }
    });

    window.openSearch = openSearch;
    window.closeSearch = closeSearch;

})();
