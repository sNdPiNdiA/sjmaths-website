function loadSamplePaperNav() {
    const navContainer = document.querySelector('.sample-paper-nav');
    if (!navContainer) return;

    // Define Sets
    const sets = [
        { name: "Set 1", file: "set1/index.html" },
        { name: "Set 2", file: "set2/index.html" },
        { name: "Set 3", file: "set3/index.html" },
        { name: "Set 4", file: "set4/index.html" },
        { name: "Set 5", file: "set5/index.html" },
        { name: "Set 6", file: "set6/index.html" },
        { name: "Set 7", file: "set7/index.html" }
    ];

    const currentPath = window.location.pathname;
    const isSetPage = currentPath.includes("/set");

    let html = `
        <div class="sp-nav-inner">
            <span class="sp-nav-label">Quick Switch:</span>
            <div class="sp-nav-list">
    `;

    sets.forEach(set => {
        const setFolder = set.file.split('/')[0];
        const isActive = currentPath.includes("/" + setFolder + "/");
        const activeClass = isActive ? 'active' : '';
        const link = isSetPage ? "../" + set.file : set.file;
        html += `<a href="${link}" class="sp-nav-link ${activeClass}">${set.name}</a>`;
    });

    html += `</div></div>`;

    navContainer.innerHTML = html;
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadSamplePaperNav);
} else {
    loadSamplePaperNav();
}