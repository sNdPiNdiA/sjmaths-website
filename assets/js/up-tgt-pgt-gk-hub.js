
let currentFilter = 'all';

function filterByModule(modId) {
  currentFilter = modId;
  
  // Update pill active classes
  const pills = document.querySelectorAll('.filter-pill');
  pills.forEach(pill => {
    if (modId === 'all' && pill.textContent.includes('All')) {
      pill.classList.add('active');
    } else if (pill.getAttribute('onclick')?.includes(modId)) {
      pill.classList.add('active');
    } else {
      pill.classList.remove('active');
    }
  });

  applyFilters();
}

function applyFilters() {
  const query = document.getElementById('dirSearchInput').value.trim().toLowerCase();
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
        const searchData = item.getAttribute('data-search') || '';
        const isSearchMatch = !query || searchData.includes(query);

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

document.getElementById('dirSearchInput').addEventListener('input', applyFilters);
