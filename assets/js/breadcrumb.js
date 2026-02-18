/**
 * SJMaths Breadcrumb Generator
 * Automatically generates breadcrumb navigation based on URL structure.
 * Supports overrides via data attributes on the body tag.
 */

(function () {
    'use strict';

    function initBreadcrumbs() {
        // Prevent duplicate breadcrumbs
        if (document.querySelector('.breadcrumb')) return;

        const path = window.location.pathname;
        // Expected format: /classes/class-9/chapter-wise-notes/chapter-7-triangles/
        const parts = path.split("/").filter(Boolean);

        // Basic validation to ensure we are in a class chapter structure
        if (!parts.includes('classes') || !parts.includes('chapter-wise-notes')) return;

        // Extract details
        const classIndex = parts.indexOf("classes") + 1;
        const classSlug = parts[classIndex] || "class-9"; // Default fallback
        const classLabel = classSlug.replace("-", " ").replace(/\b\w/g, l => l.toUpperCase());

        const chapterIndex = parts.indexOf("chapter-wise-notes") + 1;
        const chapterSlug = parts[chapterIndex];

        // derive chapter name from slug (e.g., chapter-7-triangles -> Triangles)
        // or use data-chaptername attribute if present for cleaner names
        let chapterName = document.body.dataset.chaptername;

        if (!chapterName && chapterSlug) {
            // Remove "chapter-X-" prefix
            chapterName = chapterSlug
                .replace(/^chapter-\d+-/, "")
                .replace(/-/g, " ")
                .replace(/\b\w/g, l => l.toUpperCase());
        }

        if (!chapterName) chapterName = "Chapter Notes";

        // Create Breadcrumb HTML
        const breadcrumb = document.createElement("nav");
        breadcrumb.className = "breadcrumb";
        breadcrumb.setAttribute("aria-label", "Breadcrumb");

        // Inject Styles if not present
        if (!document.getElementById('breadcrumb-style-global')) {
            const style = document.createElement('style');
            style.id = 'breadcrumb-style-global';
            style.textContent = `
              .breadcrumb {
                  max-width: 900px;
                  margin: 1rem auto 0;
                  padding: 0 1.5rem;
                  font-size: 0.9rem;
                  color: var(--text-light, #555);
                  font-family: 'Poppins', sans-serif;
              }
              .breadcrumb a { text-decoration: none; color: inherit; transition: color 0.2s; }
              .breadcrumb a:hover { color: var(--primary, #8e44ad); }
              .breadcrumb span.separator { margin: 0 5px; opacity: 0.5; }
              .breadcrumb span.current { color: var(--primary, #8e44ad); font-weight: 600; }
              @media (max-width: 600px) { .breadcrumb { padding: 0 1rem; font-size: 0.85rem; } }
          `;
            document.head.appendChild(style);
        }

        breadcrumb.innerHTML = `
        <a href="/">Home</a> <span class="separator">›</span>
        <a href="/classes/${classSlug}/">${classLabel}</a> <span class="separator">›</span>
        <a href="/classes/${classSlug}/chapter-wise-notes/">Notes</a> <span class="separator">›</span>
        <span class="current">${chapterName}</span>
      `;

        // Insertion Logic
        const contentWrapper = document.querySelector('.content-wrapper');
        const header = document.querySelector('header') || document.getElementById('header-container');

        if (contentWrapper) {
            contentWrapper.parentNode.insertBefore(breadcrumb, contentWrapper);
        } else if (header && header.nextSibling) {
            header.parentNode.insertBefore(breadcrumb, header.nextSibling);
        } else {
            // Fallback: prepend to body
            document.body.prepend(breadcrumb);
        }
    }

    // Run on load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initBreadcrumbs);
    } else {
        initBreadcrumbs();
    }

})();
