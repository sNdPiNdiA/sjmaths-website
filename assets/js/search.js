// ===== SEARCH MODULE (DEBOUNCED & OPTIMIZED) =====

// 1. State Management
let searchTimeout;
let lastQuery = '';

// 2. The Search Logic (Plug your real logic here later)
const executeSearch = (query) => {
    console.log(`Searching for: "${query}"`);

    // Example: Toggle visibility of items based on data-tags
    // const items = document.querySelectorAll('.class-card, .feature-card');
    // items.forEach(item => {
    //     const text = item.innerText.toLowerCase();
    //     item.style.display = text.includes(query) ? 'block' : 'none';
    // });
};

// 3. Event Listener with Debounce
document.addEventListener('input', ({ target }) => {
    // Check if the target is a search input
    const input = target.closest('.search-input');
    if (!input) return;

    // Clear the previous timer (this is the "debounce" magic)
    clearTimeout(searchTimeout);

    // Set a new timer
    searchTimeout = setTimeout(() => {
        const query = input.value.trim().toLowerCase();

        // Prevent searching for the exact same thing twice
        if (query === lastQuery) return;
        lastQuery = query;

        executeSearch(query);
    }, 300); // Wait 300ms after the last keystroke
});