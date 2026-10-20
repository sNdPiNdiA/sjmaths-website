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

    const EXACT_LEGACY_MAP = {
    "chk-gk-topics-1-1": "chk-general-knowledge-1-1",
    "chk-gk-topics-1-2": "chk-general-knowledge-1-2",
    "chk-gk-topics-1-3": "chk-general-knowledge-1-3",
    "chk-gk-topics-1-4": "chk-general-knowledge-1-4",
    "chk-gk-topics-1-5": "chk-general-knowledge-1-5",
    "chk-gk-topics-1-6": "chk-general-knowledge-1-6",
    "chk-gk-topics-1-7": "chk-general-knowledge-1-7",
    "chk-gk-topics-1-8": "chk-general-knowledge-1-8",
    "chk-gk-topics-1-9": "chk-general-knowledge-1-9",
    "chk-gk-topics-1-10": "chk-general-knowledge-1-10",
    "chk-gk-topics-1-11": "chk-general-knowledge-1-11",
    "chk-gk-topics-1-12": "chk-general-knowledge-1-12",
    "chk-gk-topics-1-13": "chk-general-knowledge-1-13",
    "chk-gk-topics-1-14": "chk-general-knowledge-1-14",
    "chk-gk-topics-2-1": "chk-general-knowledge-2-1",
    "chk-gk-topics-2-2": "chk-general-knowledge-2-2",
    "chk-gk-topics-2-3": "chk-general-knowledge-2-3",
    "chk-gk-topics-2-4": "chk-general-knowledge-2-4",
    "chk-gk-topics-2-5": "chk-general-knowledge-2-5",
    "chk-gk-topics-2-6": "chk-general-knowledge-2-6",
    "chk-gk-topics-2-7": "chk-general-knowledge-2-7",
    "chk-gk-topics-2-8": "chk-general-knowledge-2-8",
    "chk-gk-topics-2-9": "chk-general-knowledge-2-9",
    "chk-gk-topics-2-10": "chk-general-knowledge-2-10",
    "chk-gk-topics-3-1": "chk-general-knowledge-3-1",
    "chk-gk-topics-3-2": "chk-general-knowledge-3-2",
    "chk-gk-topics-3-3": "chk-general-knowledge-3-3",
    "chk-gk-topics-3-4": "chk-general-knowledge-3-4",
    "chk-gk-topics-3-5": "chk-general-knowledge-3-5",
    "chk-gk-topics-3-6": "chk-general-knowledge-3-6",
    "chk-gk-topics-3-7": "chk-general-knowledge-3-7",
    "chk-gk-topics-3-8": "chk-general-knowledge-3-8",
    "chk-gk-topics-3-9": "chk-general-knowledge-3-9",
    "chk-gk-topics-3-10": "chk-general-knowledge-3-10",
    "chk-gk-topics-3-11": "chk-general-knowledge-3-11",
    "chk-gk-topics-3-12": "chk-general-knowledge-3-12",
    "chk-gk-topics-3-13": "chk-general-knowledge-3-13",
    "chk-gk-topics-4-1": "chk-general-knowledge-4-1",
    "chk-gk-topics-4-2": "chk-general-knowledge-4-2",
    "chk-gk-topics-4-3": "chk-general-knowledge-4-3",
    "chk-gk-topics-4-4": "chk-general-knowledge-4-4",
    "chk-gk-topics-4-5": "chk-general-knowledge-4-5",
    "chk-gk-topics-4-6": "chk-general-knowledge-4-6",
    "chk-gk-topics-4-7": "chk-general-knowledge-4-7",
    "chk-gk-topics-4-8": "chk-general-knowledge-4-8",
    "chk-gk-topics-5-1": "chk-general-knowledge-5-1",
    "chk-gk-topics-5-2": "chk-general-knowledge-5-2",
    "chk-gk-topics-5-3": "chk-general-knowledge-5-3",
    "chk-gk-topics-5-4": "chk-general-knowledge-5-4",
    "chk-gk-topics-5-5": "chk-general-knowledge-5-5",
    "chk-gk-topics-5-6": "chk-general-knowledge-5-6",
    "chk-gk-topics-5-7": "chk-general-knowledge-5-7",
    "chk-gk-topics-5-8": "chk-general-knowledge-5-8",
    "chk-gk-topics-6-1": "chk-general-knowledge-6-1",
    "chk-gk-topics-6-2": "chk-general-knowledge-6-2",
    "chk-gk-topics-6-3": "chk-general-knowledge-6-3",
    "chk-gk-topics-6-4": "chk-general-knowledge-6-4",
    "chk-gk-topics-6-5": "chk-general-knowledge-6-5",
    "chk-gk-topics-6-6": "chk-general-knowledge-6-6",
    "chk-gk-topics-6-7": "chk-general-knowledge-6-7",
    "chk-gk-topics-6-8": "chk-general-knowledge-6-8",
    "chk-gk-topics-6-9": "chk-general-knowledge-6-9",
    "chk-gk-topics-6-10": "chk-general-knowledge-6-10",
    "chk-sst-hist-1-1": "chk-social-studies-1-1",
    "chk-sst-hist-1-2": "chk-social-studies-1-2",
    "chk-sst-hist-1-3": "chk-social-studies-1-3",
    "chk-sst-hist-1-4": "chk-social-studies-1-4",
    "chk-sst-hist-1-5": "chk-social-studies-1-5",
    "chk-sst-hist-1-6": "chk-social-studies-1-6",
    "chk-sst-hist-1-7": "chk-social-studies-1-7",
    "chk-sst-hist-1-8": "chk-social-studies-1-8",
    "chk-sst-hist-1-9": "chk-social-studies-1-9",
    "chk-sst-hist-2-1": "chk-social-studies-2-10",
    "chk-sst-hist-2-2": "chk-social-studies-2-11",
    "chk-sst-hist-2-3": "chk-social-studies-2-12",
    "chk-sst-hist-2-4": "chk-social-studies-2-13",
    "chk-sst-hist-2-5": "chk-social-studies-2-14",
    "chk-sst-hist-2-6": "chk-social-studies-2-15",
    "chk-sst-hist-2-7": "chk-social-studies-2-16",
    "chk-sst-hist-2-8": "chk-social-studies-2-17",
    "chk-sst-hist-2-9": "chk-social-studies-2-18",
    "chk-sst-hist-2-10": "chk-social-studies-2-19",
    "chk-sst-hist-2-11": "chk-social-studies-2-20",
    "chk-sst-hist-2-12": "chk-social-studies-2-21",
    "chk-sst-hist-2-13": "chk-social-studies-2-22",
    "chk-sst-civics-1-1": "chk-social-studies-3-23",
    "chk-sst-civics-1-2": "chk-social-studies-3-24",
    "chk-sst-civics-1-3": "chk-social-studies-3-25",
    "chk-sst-civics-1-4": "chk-social-studies-3-26",
    "chk-sst-civics-1-5": "chk-social-studies-3-27",
    "chk-sst-civics-1-6": "chk-social-studies-3-28",
    "chk-sst-civics-1-7": "chk-social-studies-3-29",
    "chk-sst-civics-1-8": "chk-social-studies-3-30",
    "chk-sst-geo-1-1": "chk-social-studies-4-31",
    "chk-sst-geo-1-2": "chk-social-studies-4-32",
    "chk-sst-geo-1-3": "chk-social-studies-4-33",
    "chk-sst-geo-1-4": "chk-social-studies-4-34",
    "chk-sst-geo-1-5": "chk-social-studies-4-35",
    "chk-sst-geo-1-6": "chk-social-studies-4-36",
    "chk-sst-geo-1-7": "chk-social-studies-4-37",
    "chk-sst-geo-1-8": "chk-social-studies-4-38",
    "chk-sst-geo-1-9": "chk-social-studies-4-39",
    "chk-sst-geo-1-10": "chk-social-studies-4-40",
    "chk-sst-geo-2-1": "chk-social-studies-5-41",
    "chk-sst-geo-2-2": "chk-social-studies-5-42",
    "chk-sst-geo-2-3": "chk-social-studies-5-43",
    "chk-sst-geo-2-4": "chk-social-studies-5-44",
    "chk-sst-geo-2-5": "chk-social-studies-5-45",
    "chk-sst-geo-2-6": "chk-social-studies-5-46",
    "chk-sst-geo-2-7": "chk-social-studies-5-47",
    "chk-sst-geo-2-8": "chk-social-studies-5-48",
    "chk-math-card-1-1": "chk-mathematics-1-1",
    "chk-math-card-1-2": "chk-mathematics-1-2",
    "chk-math-card-1-3": "chk-mathematics-1-3",
    "chk-math-card-1-4": "chk-mathematics-1-4",
    "chk-math-card-1-5": "chk-mathematics-1-5",
    "chk-math-card-1-6": "chk-mathematics-1-6",
    "chk-math-card-1-7": "chk-mathematics-1-7",
    "chk-math-card-2-1": "chk-mathematics-2-8",
    "chk-math-card-2-2": "chk-mathematics-2-9",
    "chk-math-card-2-3": "chk-mathematics-2-10",
    "chk-math-card-3-1": "chk-mathematics-3-11",
    "chk-math-card-3-2": "chk-mathematics-3-12",
    "chk-math-card-3-3": "chk-mathematics-3-13",
    "chk-math-card-3-4": "chk-mathematics-3-14",
    "chk-math-card-3-5": "chk-mathematics-3-15",
    "chk-math-card-3-6": "chk-mathematics-3-16",
    "chk-math-card-4-1": "chk-mathematics-4-17",
    "chk-math-card-4-2": "chk-mathematics-4-18",
    "chk-math-card-4-3": "chk-mathematics-4-19",
    "chk-math-card-4-4": "chk-mathematics-4-20",
    "chk-math-card-5-1": "chk-mathematics-5-21",
    "chk-math-card-5-2": "chk-mathematics-5-22",
    "chk-math-card-5-3": "chk-mathematics-5-23",
    "chk-math-card-6-1": "chk-mathematics-6-24",
    "chk-math-card-6-2": "chk-mathematics-6-25",
    "chk-math-card-6-3": "chk-mathematics-6-26",
    "chk-sci-card-1-1": "chk-science-1-1",
    "chk-sci-card-1-2": "chk-science-1-2",
    "chk-sci-card-1-3": "chk-science-1-3",
    "chk-sci-card-1-4": "chk-science-1-4",
    "chk-sci-card-1-5": "chk-science-1-5",
    "chk-sci-card-1-6": "chk-science-1-6",
    "chk-sci-card-1-7": "chk-science-1-7",
    "chk-sci-card-1-8": "chk-science-1-8",
    "chk-sci-card-1-9": "chk-science-1-9",
    "chk-sci-card-1-10": "chk-science-1-10",
    "chk-sci-card-1-11": "chk-science-1-11",
    "chk-sci-card-1-12": "chk-science-1-12",
    "chk-sci-card-1-13": "chk-science-1-13",
    "chk-sci-card-1-14": "chk-science-1-14",
    "chk-sci-card-2-1": "chk-science-2-1",
    "chk-sci-card-2-2": "chk-science-2-2",
    "chk-sci-card-2-3": "chk-science-2-3",
    "chk-sci-card-2-4": "chk-science-2-4",
    "chk-sci-card-2-5": "chk-science-2-5",
    "chk-sci-card-2-6": "chk-science-2-6",
    "chk-sci-card-3-1": "chk-science-3-1",
    "chk-sci-card-3-2": "chk-science-3-2",
    "chk-sci-card-3-3": "chk-science-3-3",
    "chk-sci-card-3-4": "chk-science-3-4",
    "chk-sci-card-3-5": "chk-science-3-5",
    "chk-sci-card-3-6": "chk-science-3-6",
    "chk-sci-card-4-1": "chk-science-4-1",
    "chk-sci-card-4-2": "chk-science-4-2",
    "chk-sci-card-4-3": "chk-science-4-3",
    "chk-sci-card-4-4": "chk-science-4-4",
    "chk-sci-card-4-5": "chk-science-4-5",
    "chk-sci-card-4-6": "chk-science-4-6",
    "chk-sci-card-4-7": "chk-science-4-7",
    "chk-sci-card-4-8": "chk-science-4-8"
};

    const REVERSE_LEGACY_MAP = {};
    for (const key in EXACT_LEGACY_MAP) {
        REVERSE_LEGACY_MAP[EXACT_LEGACY_MAP[key]] = key;
    }

    const LEGACY_ALIASES = [
        ['chk-gk-topics-', 'chk-general-knowledge-'],
        ['chk-math-card-', 'chk-mathematics-'],
        ['chk-sci-card-', 'chk-science-'],
        ['chk-sst-hist-', 'chk-social-studies-'],
        ['chk-sst-civics-', 'chk-social-studies-'],
        ['chk-sst-geo-', 'chk-social-studies-']
    ];

    function getAlternateId(id) {
        if (!id || typeof id !== 'string') return null;
        if (EXACT_LEGACY_MAP[id]) return EXACT_LEGACY_MAP[id];
        if (REVERSE_LEGACY_MAP[id]) return REVERSE_LEGACY_MAP[id];
        for (let i = 0; i < LEGACY_ALIASES.length; i++) {
            const [legacy, standard] = LEGACY_ALIASES[i];
            if (id.startsWith(legacy)) {
                return id.replace(legacy, standard);
            }
            if (id.startsWith(standard)) {
                return id.replace(standard, legacy);
            }
        }
        return null;
    }

    function readProgress(storageKey) {
        const raw = readItem(storageKey);
        if (!raw) return {};

        try {
            const parsed = JSON.parse(raw);
            if (Array.isArray(parsed)) {
                const normalized = {};
                parsed.forEach(item => {
                    if (item && typeof item === 'string') {
                        normalized[item] = true;
                        const alt = getAlternateId(item);
                        if (alt) normalized[alt] = true;
                    }
                });
                return normalized;
            }
            if (parsed && typeof parsed === 'object') {
                return parsed;
            }
            return {};
        } catch (error) {
            return {};
        }
    }

    function isItemChecked(progress, id) {
        if (!progress || !id) return false;
        if (progress[id]) return true;
        const alt = getAlternateId(id);
        return alt ? Boolean(progress[alt]) : false;
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
                checkbox.checked = isItemChecked(progress, checkbox.id);
            });
            if (typeof onProgressChange === 'function') onProgressChange();
        }

        const initialProgress = readProgress(key);
        items.forEach(checkbox => {
            checkbox.checked = isItemChecked(initialProgress, checkbox.id);

            checkbox.addEventListener('change', () => {
                // Merge against the latest saved state instead of a page-load snapshot.
                const latestProgress = readProgress(key);
                latestProgress[checkbox.id] = checkbox.checked;
                const alt = getAlternateId(checkbox.id);
                if (alt) {
                    latestProgress[alt] = checkbox.checked;
                }
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
        writeItem,
        readProgress,
        writeProgress,
        isItemChecked
    });
})();
