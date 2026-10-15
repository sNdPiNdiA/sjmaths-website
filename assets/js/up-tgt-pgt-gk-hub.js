(function () {
  'use strict';
  let currentFilter = 'all';

  function applyFilters() {
    const input = document.getElementById('dirSearchInput');
    const query = input ? input.value.trim().toLowerCase() : '';
    const moduleBlocks = document.querySelectorAll('.directory-module-block');
    let totalVisibleTopics = 0;

    moduleBlocks.forEach(block => {
      const mod = block.getAttribute('data-mod');
      const isModuleMatch = (currentFilter === 'all' || currentFilter === mod);

      if (!isModuleMatch) {
        block.style.display = 'none';
        return;
      }

      let moduleHasVisibleTopics = false;
      const sectionGroups = block.querySelectorAll('.section-group');

      sectionGroups.forEach(sec => {
        let secHasVisible = false;
        const topicItems = sec.querySelectorAll('.topic-item');

        topicItems.forEach(item => {
          const searchData = (item.getAttribute('data-search') || '').toLowerCase();
          const isSearchMatch = !query || searchData.includes(query) || item.textContent.toLowerCase().includes(query);

          if (isSearchMatch) {
            item.style.display = '';
            secHasVisible = true;
            moduleHasVisibleTopics = true;
            totalVisibleTopics++;
          } else {
            item.style.display = 'none';
          }
        });

        sec.style.display = secHasVisible ? '' : 'none';
      });

      block.style.display = moduleHasVisibleTopics ? '' : 'none';
    });

    const noResults = document.getElementById('noResultsMsg');
    if (noResults) {
      noResults.style.display = totalVisibleTopics === 0 ? 'block' : 'none';
    }
  }

  function filterByModule(modId) {
    currentFilter = modId;

    // Update pill active classes and aria-pressed
    const pills = document.querySelectorAll('.filter-pill');
    pills.forEach(pill => {
      const isMatch = (modId === 'all' && pill.textContent.includes('All')) ||
                      (pill.getAttribute('onclick')?.includes(modId));
      pill.classList.toggle('active', !!isMatch);
      pill.setAttribute('aria-pressed', String(!!isMatch));
    });

    applyFilters();
  }

  // Expose filterByModule on window for inline onclick attributes
  window.filterByModule = filterByModule;

  function initGkHub() {
    const searchInput = document.getElementById('dirSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', applyFilters);
    }
    const pills = document.querySelectorAll('.filter-pill');
    pills.forEach(pill => {
      pill.setAttribute('aria-pressed', String(pill.classList.contains('active')));
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGkHub, { once: true });
  } else {
    initGkHub();
  }
})();
