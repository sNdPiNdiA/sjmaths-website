/* =========================================
   SEARCH MODULE (Data-Driven & Optimized)
   ========================================= */

(function () {
    let searchIndex = [];
    let isIndexLoaded = false;
    let isFetching = false;
    let searchTimeout;

    // 1. Lazy Fetch Search Index
    function loadSearchIndex() {
        if (isFetching || isIndexLoaded) return;
        isFetching = true;

        fetch('/assets/js/search-index.json')
            .then(response => response.json())
            .then(data => {
                searchIndex = data;
                isIndexLoaded = true;
            })
            .catch(err => {
                console.warn('Search index failed to load:', err);
                isFetching = false;
            });
    }

    // 2. Event Delegation for Search Input (Handles async header loading)
    document.addEventListener('input', (e) => {
        if (!e.target.matches('.header-search input')) return;

        const input = e.target;
        const wrapper = input.closest('.header-search');
        let resultsContainer = wrapper.querySelector('.search-results');

        // Ensure index is loading if user types quickly
        loadSearchIndex();

        // Create results container if it doesn't exist
        if (!resultsContainer) {
            resultsContainer = document.createElement('div');
            resultsContainer.className = 'search-results';
            wrapper.appendChild(resultsContainer);
        }

        // Debounce Search
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const query = input.value.trim().toLowerCase();

            if (query.length < 2) {
                resultsContainer.style.display = 'none';
                return;
            }

            if (!isIndexLoaded) {
                resultsContainer.innerHTML = '<div class="search-message">Loading index...</div>';
                resultsContainer.style.display = 'block';
                return;
            }

            // Perform Search
            const results = searchIndex.filter(item =>
                item.title.toLowerCase().includes(query) ||
                item.tags.some(tag => tag.toLowerCase().includes(query))
            );

            renderResults(results, resultsContainer);
        }, 300);
    });

    // 3. Render Logic
    function renderResults(results, container) {
        container.innerHTML = '';

        if (results.length === 0) {
            container.innerHTML = '<div class="search-message">No results found</div>';
        } else {
            results.slice(0, 8).forEach(item => { // Limit to 8 results
                const div = document.createElement('div');
                div.className = 'search-result-item';
                div.innerHTML = `
                    <a href="${item.url}">
                        <div class="result-title">${item.title}</div>
                        <div class="result-type">${item.category}</div>
                    </a>
                `;
                container.appendChild(div);
            });
        }
        container.style.display = 'block';
    }

    // 4. Close on Click Outside
    document.addEventListener('click', (e) => {
        const wrapper = document.querySelector('.header-search');
        if (wrapper && !wrapper.contains(e.target)) {
            const results = wrapper.querySelector('.search-results');
            if (results) results.style.display = 'none';
        }
    });

    // 5. Trigger Load on Interaction (Focus or Hover)
    document.addEventListener('focusin', (e) => {
        if (e.target.matches('.header-search input')) {
            loadSearchIndex();
        }
    });

    document.addEventListener('mouseover', (e) => {
        if (e.target.closest('.header-search')) {
            loadSearchIndex();
        }
    });
})();