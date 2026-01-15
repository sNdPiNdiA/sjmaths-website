document.addEventListener('DOMContentLoaded', () => {
    const navContainers = document.querySelectorAll('.nav-controls');
    if (navContainers.length === 0) return;

    // 1. Define Chapter Order (Folder Names)
    const chapters = {
        "class-9": [
            "chapter-1-number-systems",
            "chapter-2-polynomials",
            "chapter-3-coordinate-geometry",
            "chapter-4-linear-equations-in-two-variables",
            "chapter-5-introduction-to-euclids-geometry",
            "chapter-6-lines-and-angles",
            "chapter-7-triangles",
            "chapter-8-quadrilaterals",
            "chapter-9-circles",
            "chapter-10-herons-formula",
            "chapter-11-surface-areas-and-volumes",
            "chapter-12-statistics"
        ],
        "class-10": [
            "chapter-1-real-numbers",
            "chapter-2-polynomials",
            "chapter-3-pair-of-linear-equations-in-two-variables",
            "chapter-4-quadratic-equations",
            "chapter-5-arithmetic-progressions",
            "chapter-6-triangles",
            "chapter-7-coordinate-geometry",
            "chapter-8-introduction-to-trigonometry",
            "chapter-9-some-applications-of-trigonometry",
            "chapter-10-circles",
            "chapter-11-areas-related-to-circles",
            "chapter-12-surface-areas-and-volumes",
            "chapter-13-statistics",
            "chapter-14-probability"
        ],
        "class-11": [
            "chapter-1-sets",
            "chapter-2-relations-and-functions",
            "chapter-3-trigonometric-functions",
            "chapter-4-complex-numbers-and-quadratic-equations",
            "chapter-5-linear-inequalities",
            "chapter-6-permutations-and-combinations",
            "chapter-7-binomial-theorem",
            "chapter-8-sequences-and-series",
            "chapter-9-straight-lines",
            "chapter-10-conic-sections",
            "chapter-11-introduction-to-three-dimensional-geometry",
            "chapter-12-limits-and-derivatives",
            "chapter-13-statistics",
            "chapter-14-probability"
        ]
    };

    // 2. Identify Current Context
    const path = window.location.pathname;
    let currentClass = null;
    if (path.includes("class-9")) currentClass = "class-9";
    else if (path.includes("class-10")) currentClass = "class-10";
    else if (path.includes("class-11")) currentClass = "class-11";

    if (!currentClass || !chapters[currentClass]) return;

    // Extract folder name
    const pathSegments = path.split('/');
    const currentFolder = pathSegments.find(seg => chapters[currentClass].includes(seg));

    if (!currentFolder) return;

    const currentIndex = chapters[currentClass].indexOf(currentFolder);

    // 3. Determine Links
    let prevLink, nextLink, prevText, nextText;

    // Previous Logic
    if (currentIndex > 0) {
        const prevFolder = chapters[currentClass][currentIndex - 1];
        prevLink = `../${prevFolder}/index.html`;
        prevText = "Previous Chapter";
    } else {
        prevLink = "../index.html"; // Back to Chapter Index
        prevText = "All Chapters";
    }

    // Next Logic
    if (currentIndex < chapters[currentClass].length - 1) {
        const nextFolder = chapters[currentClass][currentIndex + 1];
        nextLink = `../${nextFolder}/index.html`;
        nextText = "Next Chapter";
    } else {
        nextLink = "../index.html"; // Back to Chapter Index
        nextText = "All Chapters";
    }

    // 4. Inject HTML
    const navHTML = `
        <a href="${prevLink}" class="nav-btn"><i class="fas fa-arrow-left"></i> ${prevText}</a>
        <a href="${nextLink}" class="nav-btn">${nextText} <i class="fas fa-arrow-right"></i></a>
    `;

    navContainers.forEach(container => {
        container.innerHTML = navHTML;
    });
});