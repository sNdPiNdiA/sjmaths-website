document.addEventListener('DOMContentLoaded', () => {
    const footer = document.querySelector('footer');
    if (!footer) return;

    const currentYear = new Date().getFullYear();

    // Determine paths based on depth
    // Standard path: classes/class-X/chapter-wise-notes/chapter-Y/index.html
    // Sample Papers: classes/class-X/sample-papers/index.html
    const path = window.location.pathname;
    const isSamplePaper = path.includes("/sample-papers/");
    const rootPath = isSamplePaper ? "../../../" : "../../../../";
    const classPath = isSamplePaper ? "../" : "../../";

    // Determine Class Name for link
    let className = "Class Dashboard";

    if (path.includes("class-9")) className = "Class 9";
    else if (path.includes("class-10")) className = "Class 10";
    else if (path.includes("class-11")) className = "Class 11";
    else if (path.includes("class-12")) className = "Class 12";

    // Inject Footer HTML
    footer.innerHTML = `
        <div style="margin-bottom: 1rem;">
            <a href="${rootPath}index.html" style="margin: 0 10px; text-decoration: none; color: inherit;">Home</a>
            <span style="opacity: 0.5;">|</span>
            <a href="${classPath}index.html" style="margin: 0 10px; text-decoration: none; color: inherit;">${className}</a>
            <span style="opacity: 0.5;">|</span>
            <a href="${rootPath}contact.html" style="margin: 0 10px; text-decoration: none; color: inherit;">Contact</a>
        </div>
        <div>
            &copy; ${currentYear} SJMaths. Empowering Students.
        </div>
    `;

    // Enforce basic styles to ensure consistency across chapters
    footer.style.textAlign = 'center';
    footer.style.padding = '2rem';
    footer.style.color = '#777';
    footer.style.fontSize = '0.9rem';
    footer.style.borderTop = '1px solid rgba(0,0,0,0.05)';
    footer.style.marginTop = '3rem';
});