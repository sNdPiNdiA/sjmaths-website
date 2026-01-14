/* ==========================================
   SJMATHS - DYNAMIC FAVICON LOADER
   Injects the favicon into the head of all pages
   ========================================== */

(function () {
    // Configuration: Absolute path ensures it works from any depth
    const FAVICON_PATH = '/assets/favicon.svg';

    function loadFavicon() {
        let link = document.querySelector("link[rel*='icon']");

        if (!link) {
            link = document.createElement('link');
            link.rel = 'icon';
            document.head.appendChild(link);
        }

        link.type = 'image/svg+xml';
        link.href = FAVICON_PATH;
    }

    // Run immediately
    loadFavicon();
})();