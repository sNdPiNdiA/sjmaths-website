// Client-side interactions for SJMaths Current Affairs platform
document.addEventListener('DOMContentLoaded', () => {
  initMCQInteractions();
  initFilterControls();
});

/**
 * Initializes interactions for MCQ cards (static or dynamically generated)
 */
function initMCQInteractions() {
  document.body.addEventListener('click', (e) => {
    const option = e.target.closest('.ca-mcq-option');
    if (!option || option.classList.contains('disabled')) return;

    const card = option.closest('.ca-mcq-card');
    if (!card) return;

    const options = card.querySelectorAll('.ca-mcq-option');
    const explanation = card.querySelector('.ca-mcq-explanation');
    const correctIndex = parseInt(card.dataset.correct, 10);
    const selectedIndex = parseInt(option.dataset.index, 10);

    // Disable all options in this card after choice
    options.forEach((opt) => opt.classList.add('disabled'));

    if (selectedIndex === correctIndex) {
      option.classList.add('correct');
      // Play a subtle success vibration/animation if supported
      if (navigator.vibrate) navigator.vibrate(20);
      updateStreak(true);
    } else {
      option.classList.add('wrong');
      // Highlight the correct one
      const correctOption = card.querySelector(`.ca-mcq-option[data-index="${correctIndex}"]`);
      if (correctOption) {
        correctOption.classList.add('correct');
      }
      updateStreak(false);
    }

    // Reveal explanation
    if (explanation) {
      explanation.style.display = 'block';
    }
  });
}

/**
 * Updates the user's daily study streak in localStorage
 */
function updateStreak(isCorrect) {
  try {
    const today = new Date().toDateString();
    const streakData = JSON.parse(localStorage.getItem('sjmaths_ca_streak') || '{"count": 0, "lastDate": ""}');
    
    if (streakData.lastDate === today) {
      return; // Already studied today
    }

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toDateString();

    if (streakData.lastDate === yesterdayStr) {
      streakData.count += 1;
    } else {
      streakData.count = 1; // Reset streak if missed a day
    }
    streakData.lastDate = today;
    localStorage.setItem('sjmaths_ca_streak', JSON.stringify(streakData));
    console.log(`Current CA Streak: ${streakData.count} days!`);
  } catch (err) {
    console.error('Error updating streak in localStorage:', err);
  }
}

/**
 * Handles search and filter controls on listing pages
 */
function initFilterControls() {
  const container = document.getElementById('ca-news-container');
  if (!container) return; // Not a dynamic listing page

  const filterExam = document.getElementById('filter-exam');
  const filterCategory = document.getElementById('filter-category');
  const searchInput = document.getElementById('filter-search');
  const pillsContainer = document.querySelector('.ca-categories-pills');

  // Load URL params to pre-fill filters
  const urlParams = new URLSearchParams(window.location.search);
  if (filterExam && urlParams.has('exam')) {
    filterExam.value = urlParams.get('exam');
  }
  if (filterCategory && urlParams.has('category')) {
    filterCategory.value = urlParams.get('category');
  }
  if (searchInput && urlParams.has('q')) {
    searchInput.value = urlParams.get('q');
  }

  // Handle category pills clicking
  if (pillsContainer) {
    pillsContainer.addEventListener('click', (e) => {
      const pill = e.target.closest('.ca-category-pill');
      if (!pill) return;

      pillsContainer.querySelectorAll('.ca-category-pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');

      const category = pill.dataset.category;
      if (filterCategory) {
        filterCategory.value = category;
        filterCategory.dispatchEvent(new Event('change'));
      }
    });
  }

  // Trigger filtering when filters change
  const applyFilters = () => {
    const examValue = filterExam ? filterExam.value : '';
    const categoryValue = filterCategory ? filterCategory.value : '';
    const searchValue = searchInput ? searchInput.value.toLowerCase().trim() : '';

    // Update URL parameters without reloading
    const newParams = new URLSearchParams();
    if (examValue) newParams.set('exam', examValue);
    if (categoryValue) newParams.set('category', categoryValue);
    if (searchValue) newParams.set('q', searchValue);
    
    const newUrl = window.location.pathname + (newParams.toString() ? '?' + newParams.toString() : '');
    window.history.replaceState({ path: newUrl }, '', newUrl);

    // Filter static elements in container
    const cards = container.querySelectorAll('.ca-card');
    let visibleCount = 0;

    cards.forEach((card) => {
      const categories = (card.dataset.categories || '').split(',');
      const exams = (card.dataset.exams || '').split(',');
      const title = card.querySelector('.ca-card-title').textContent.toLowerCase();
      const desc = card.querySelector('.ca-card-desc').textContent.toLowerCase();

      const matchesExam = !examValue || exams.includes(examValue);
      const matchesCategory = !categoryValue || categories.includes(categoryValue);
      const matchesSearch = !searchValue || title.includes(searchValue) || desc.includes(searchValue);

      if (matchesExam && matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    // Update results indicator if it exists
    const resultsIndicator = document.getElementById('ca-results-count');
    if (resultsIndicator) {
      const isHi = document.body.classList.contains('lang-hi');
      resultsIndicator.textContent = isHi 
        ? `${visibleCount} लेख दिखाए जा रहे हैं` 
        : `Showing ${visibleCount} articles`;
    }

    // Toggle no results view
    const noResults = document.getElementById('ca-no-results');
    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  };

  // Listen for filter inputs
  if (filterExam) filterExam.addEventListener('change', applyFilters);
  if (filterCategory) filterCategory.addEventListener('change', applyFilters);
  
  let searchDebounce;
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      clearTimeout(searchDebounce);
      searchDebounce = setTimeout(applyFilters, 250);
    });
  }

  // Update search input placeholders dynamically
  const updatePlaceholders = () => {
    const isHi = document.body.classList.contains('lang-hi');
    if (searchInput) {
      searchInput.placeholder = isHi ? "समाचार खोजें..." : "Search news...";
    }
    const globalSearch = document.getElementById('site-search');
    if (globalSearch) {
      globalSearch.placeholder = isHi ? "विषय खोजें..." : "Search topics...";
    }
  };

  updatePlaceholders();
  window.addEventListener('ca-lang-changed', updatePlaceholders);
}
