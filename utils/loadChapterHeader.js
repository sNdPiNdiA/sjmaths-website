document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('header');
    if (!header) return;

    // Determine Class Name from URL
    const path = window.location.pathname;
    let className = "Class 9"; // Default fallback

    if (path.includes("class-10")) className = "Class 10";
    else if (path.includes("class-11")) className = "Class 11";
    else if (path.includes("class-12")) className = "Class 12";

    // Determine paths based on depth
    // Standard path: classes/class-X/chapter-wise-notes/chapter-Y/index.html (Depth 4)
    // Sample Papers: classes/class-X/sample-papers/index.html (Depth 3)
    const isSamplePaper = path.includes("/sample-papers/");
    const rootPath = isSamplePaper ? "../../../" : "../../../../";
    const classPath = isSamplePaper ? "../" : "../../";

    // Inject Header HTML
    header.innerHTML = `
        <a href="${rootPath}index.html" class="logo">
            <span style="font-size: 1.5em;">&int;</span> SJMaths
        </a>
        <div style="display: flex; align-items: center; gap: 10px;">
            <a href="${classPath}index.html" class="nav-btn" style="font-size: 0.9rem; padding: 5px 15px;">
                <i class="fas fa-graduation-cap"></i> ${className}
            </a>
            <button id="darkToggle" class="nav-btn" style="padding:6px 12px;" aria-label="Toggle Dark Mode">
                <i class="fas fa-moon"></i>
            </button>
        </div>
    `;

    // Sync Icon State (in case main.js ran before injection or dark mode was already applied)
    const icon = document.querySelector('#darkToggle i');
    if (document.body.classList.contains('dark-mode') && icon) {
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }
});