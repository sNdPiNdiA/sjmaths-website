function generateBreadcrumb() {
    const path = window.location.pathname;
    const parts = path.split('/').filter(part => part); // Filter out empty strings

    let breadcrumbContainer = document.getElementById('breadcrumb-container');
    if (!breadcrumbContainer) {
        // If there's no breadcrumb container, we create one and prepend it to the main content area
        const mainContent = document.querySelector('main') || document.body;
        if (!mainContent) {
            console.error("Could not find a <main> or <body> element to attach the breadcrumb to.");
            return;
        }
        const container = document.createElement('div');
        // Setting the ID is important if the script runs again, to avoid duplication
        container.id = 'breadcrumb-container'; 
        mainContent.prepend(container);
        breadcrumbContainer = container;
    }
    
    // Create the nav element
    const nav = document.createElement('nav');
    nav.className = 'breadcrumb';

    // Add Home link
    const homeLink = document.createElement('a');
    homeLink.href = '/';
    homeLink.textContent = 'Home';
    nav.appendChild(homeLink);

    let currentPath = '';
    const relevantParts = parts.filter(part => part.toLowerCase() !== 'index.html');

    relevantParts.forEach((part, index) => {
        currentPath += `/${part}`;
        const isLast = index === relevantParts.length - 1;
        
        const separator = document.createTextNode(' › ');
        nav.appendChild(separator);

        // Replace hyphens, underscores, and decode URI components for display
        let text = decodeURIComponent(part.replace(/[-_]/g, ' '));
        // Remove file extensions
        text = text.replace(/\.(html|htm|php|asp|aspx)$/i, '');

        // Capitalize each word for a cleaner look
        const capitalizedText = text.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');

        if (isLast) {
            const span = document.createElement('span');
            span.textContent = capitalizedText;
            nav.appendChild(span);
        } else {
            const link = document.createElement('a');
            link.href = currentPath;
            link.textContent = capitalizedText;
            nav.appendChild(link);
        }
    });
    
    // Clear any existing content and append the new breadcrumb
    breadcrumbContainer.innerHTML = ''; 
    breadcrumbContainer.appendChild(nav);
}

// Run the function when the DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', generateBreadcrumb);
} else {
    generateBreadcrumb();
}
