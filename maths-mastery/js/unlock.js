// maths-mastery/js/unlock.js

const MATHS_MASTERY_PROGRESS_KEY = "maths_mastery_progress";

const DEFAULT_PROGRESS = {
    "fractions": {
        "types-of-fractions": true, // First one is unlocked by default
        "equivalent-fractions": false,
        "simplification": false
    },
    "algebra": {
        "basic-expressions": true,
        "solving-equations": false
    }
};

// TODO: Replace with backend mastery validation
/**
 * Initializes the default unlock state in localStorage.
 * This is a placeholder and should be replaced with a backend call.
 */
function initializeProgress() {
    const progress = getProgress();
    if (!progress) {
        // Hardcoded for now, should be fetched from a config or API
        saveProgress(DEFAULT_PROGRESS);
    }
}

/**
 * Reads the entire progress object from localStorage.
 * @returns {object | null} The progress object or null if not found.
 */
function getProgress() {
    const progressJSON = localStorage.getItem(MATHS_MASTERY_PROGRESS_KEY);
    return progressJSON ? JSON.parse(progressJSON) : null;
}

/**
 * Saves the progress object to localStorage.
 * @param {object} progress The progress object to save.
 */
function saveProgress(progress) {
    localStorage.setItem(MATHS_MASTERY_PROGRESS_KEY, JSON.stringify(progress));
}

/**
 * Checks if a specific microtopic is unlocked for a given topic.
 * @param {string} topic The topic id (e.g., "fractions").
 * @param {string} microtopic The microtopic id (e.g., "types-of-fractions").
 * @returns {boolean} True if the microtopic is unlocked, false otherwise.
 */
function isUnlocked(topic, microtopic) {
    const progress = getProgress();
    return progress?.[topic]?.[microtopic] === true;
}

/**
 * Unlocks a specific microtopic for a given topic.
 * @param {string} topic The topic id (e.g., "fractions").
 * @param {string} microtopic The microtopic id (e.g., "simplification").
 */
function unlockMicrotopic(topic, microtopic) {
    const progress = getProgress();
    if (progress && progress[topic]) {
        progress[topic][microtopic] = true;
        saveProgress(progress);
    }
}

/**
 * Gets the next microtopic to be unlocked for a given topic.
 * This is a simple placeholder logic.
 * @param {string} currentTopic The current topic id.
 * @param {string} currentMicrotopic The current microtopic id.
 * @returns {string | null} The ID of the next microtopic to unlock, or null if it's the last one.
 */
function getNextMicrotopic(currentTopic, currentMicrotopic) {
    const progress = getProgress();
    if (!progress || !progress[currentTopic]) {
        return null;
    }

    const microtopics = Object.keys(progress[currentTopic]);
    const currentIndex = microtopics.indexOf(currentMicrotopic);

    if (currentIndex !== -1 && currentIndex < microtopics.length - 1) {
        return microtopics[currentIndex + 1];
    }

    return null; // No more microtopics to unlock in this topic
}


// Initialize progress on script load
initializeProgress();
