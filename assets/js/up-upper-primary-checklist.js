(function () {
    'use strict';

    function readItem(storageKey) {
        try {
            return localStorage.getItem(storageKey);
        } catch (error) {
            return null;
        }
    }

    function writeItem(storageKey, value) {
        try {
            localStorage.setItem(storageKey, value);
            return true;
        } catch (error) {
            return false;
        }
    }

    function readProgress(storageKey) {
        const raw = readItem(storageKey);
        if (!raw) return {};

        try {
            const parsed = JSON.parse(raw);
            return parsed && typeof parsed === 'object' && !Array.isArray(parsed) ? parsed : {};
        } catch (error) {
            return {};
        }
    }

    function writeProgress(storageKey, progress) {
        // Keep the checklist usable in sessions where browser storage is unavailable.
        writeItem(storageKey, JSON.stringify(progress));
    }

    function isInteractiveTarget(target) {
        return target instanceof Element && Boolean(
            target.closest('a, button, input, label, select, textarea')
        );
    }

    function initialize(checkboxes, storageKey, onProgressChange) {
        const items = Array.from(checkboxes || []);
        const key = storageKey || 'up-upper-primary-teacher-checklist-v2';

        function refreshFromStorage() {
            const progress = readProgress(key);
            items.forEach(checkbox => {
                checkbox.checked = Boolean(progress[checkbox.id]);
            });
            if (typeof onProgressChange === 'function') onProgressChange();
        }

        const initialProgress = readProgress(key);
        items.forEach(checkbox => {
            checkbox.checked = Boolean(initialProgress[checkbox.id]);

            checkbox.addEventListener('change', () => {
                // Merge against the latest saved state instead of a page-load snapshot.
                const latestProgress = readProgress(key);
                latestProgress[checkbox.id] = checkbox.checked;
                writeProgress(key, latestProgress);
                if (typeof onProgressChange === 'function') onProgressChange();
            });

            const row = checkbox.closest('.topic-row');
            if (row) {
                row.addEventListener('click', event => {
                    if (event.target === checkbox || isInteractiveTarget(event.target)) return;
                    checkbox.checked = !checkbox.checked;
                    checkbox.dispatchEvent(new Event('change'));
                });
            }
        });

        window.addEventListener('storage', event => {
            if (event.key === key || event.key === null) refreshFromStorage();
        });
    }

    window.SJMathsChecklist = Object.freeze({
        initialize,
        readItem,
        writeItem
    });
})();
