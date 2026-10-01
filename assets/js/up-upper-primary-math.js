/**
 * ==========================================================================
 * UP Upper Primary Teacher Mathematics — Master Common Interactive Scripts
 * Path: /assets/js/up-upper-primary-math.js
 * ==========================================================================
 */

/**
 * Interactive MCQ Option Checking
 * Handles both click signatures across all 26 topics.
 * @param {HTMLElement} btn - The clicked option button
 * @param {string} mcqId - The container or question identifier
 * @param {string} option - Option letter ('A', 'B', 'C', 'D')
 * @param {boolean} isCorrect - Whether the clicked option is correct
 */
function checkOption(btn, mcqId, option, isCorrect) {
    if (!btn) return;
    
    // Find parent MCQ card container
    const parentCard = btn.closest('.mcq-card') || (mcqId ? document.getElementById(mcqId) : null);
    if (!parentCard) return;
    
    const allButtons = parentCard.querySelectorAll('.option-btn');
    
    // Disable all options in this card once clicked to freeze selection
    allButtons.forEach(b => {
        b.disabled = true;
        b.style.cursor = 'default';
    });
    
    if (isCorrect) {
        btn.classList.add('correct-choice', 'selected-correct');
    } else {
        btn.classList.add('wrong-choice', 'selected-wrong');
        
        // Find and highlight the correct option automatically
        allButtons.forEach(b => {
            const onclickAttr = b.getAttribute('onclick') || '';
            if (onclickAttr.includes('true') || onclickAttr.includes('isCorrect = true')) {
                b.classList.add('correct-choice', 'selected-correct');
            }
        });
    }
}

/**
 * Collapsible Solution Drawer Toggle
 * @param {string} drawerId - The HTML element ID of the solution drawer
 */
function toggleSolution(drawerId) {
    const drawer = document.getElementById(drawerId);
    if (drawer) {
        drawer.classList.toggle('open');
    }
}

/**
 * Legacy Topic MCQ Checker (Topics 1-7 Compatibility)
 */
function checkMcqAnswer(qNum, selectedOpt, isCorrect) {
    const card = document.getElementById(`mcq-card-${qNum}`) || document.querySelector(`[data-q="${qNum}"]`);
    if (!card) return;
    
    const allOptions = card.querySelectorAll('.option-btn, .option-item');
    allOptions.forEach(opt => {
        const btn = opt.tagName === 'BUTTON' ? opt : opt.querySelector('button');
        if (btn) {
            btn.disabled = true;
        }
    });
    
    const selectedBtn = event ? event.currentTarget : null;
    if (selectedBtn) {
        if (isCorrect) {
            selectedBtn.classList.add('correct-choice');
        } else {
            selectedBtn.classList.add('wrong-choice');
        }
    }
}

/**
 * Language Switcher Functions (Topics 1-7)
 */
function setLanguage(lang) {
    if (lang === 'english') {
        document.body.classList.remove('lang-hindi', 'lang-mode-hi');
        document.body.classList.add('lang-english', 'lang-mode-en');
        localStorage.setItem('sjmaths_preferred_language', 'english');
    } else {
        document.body.classList.remove('lang-english', 'lang-mode-en');
        document.body.classList.add('lang-hindi', 'lang-mode-hi');
        localStorage.setItem('sjmaths_preferred_language', 'hindi');
    }
}

function toggleLocalLanguage() {
    const isCurrentlyHi = document.body.classList.contains('lang-mode-hi') || document.body.classList.contains('lang-hindi');
    setLanguage(isCurrentlyHi ? 'english' : 'hindi');
}

/**
 * Topic Completion Tracker
 */
function toggleTopicCompletion(topicSlug) {
    if (!topicSlug) return;
    const key = `completed_topic_${topicSlug}`;
    const current = localStorage.getItem(key) === 'true';
    localStorage.setItem(key, String(!current));
    updateTopicStatus(topicSlug);
}

function updateTopicStatus(topicSlug) {
    if (!topicSlug) return;
    const btn = document.getElementById('mark-complete-btn');
    const isDone = localStorage.getItem(`completed_topic_${topicSlug}`) === 'true';
    if (btn) {
        if (isDone) {
            btn.innerHTML = '<i class="fa-solid fa-circle-check"></i> Completed';
            btn.style.background = '#d1fae5';
            btn.style.color = '#065f46';
            btn.style.borderColor = '#10b981';
        } else {
            btn.innerHTML = '<i class="fa-regular fa-circle-check"></i> Mark Complete';
            btn.style.background = '#ffffff';
            btn.style.color = '#1e293b';
            btn.style.borderColor = '#cbd5e1';
        }
    }
}

// Auto-initialize preferences on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    // 1. Language preference
    const savedLang = localStorage.getItem('sjmaths_preferred_language');
    if (savedLang) {
        setLanguage(savedLang);
    }
});
