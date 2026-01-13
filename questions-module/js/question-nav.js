function loadQuestionNav(containerId, prevLink, nextLink) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
        <a id="navPrev" class="nav-btn btn-prev ${!prevLink ? 'disabled' : ''}" href="${prevLink || '#'}">
            ← Previous
        </a>
        <a id="navNext" class="nav-btn btn-next ${!nextLink ? 'disabled' : ''}" href="${nextLink || '#'}">
            Next →
        </a>
    `;
}
