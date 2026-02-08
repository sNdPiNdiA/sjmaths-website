function loadScrollProgress() {
    // Logic moved to assets/js/ui-utils.js to prevent duplicate listeners
    // This function is kept to prevent errors if called by legacy scripts
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadScrollProgress);
} else {
    loadScrollProgress();
}