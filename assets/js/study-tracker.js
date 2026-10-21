/**
 * SJMaths Study Tracker Module
 * Tracks visits to Classes & Exam pages and persists the last visited page
 * in localStorage so users can seamlessly continue where they left off.
 */

(function () {
    'use strict';

    const STORAGE_KEY_LAST = 'sjmaths_last_study_page';
    const STORAGE_KEY_HISTORY = 'sjmaths_study_history';
    const MAX_HISTORY = 4;

    function classifyStudyPage(pathname) {
        if (!pathname) return null;
        const path = pathname.toLowerCase().replace(/\\/g, '/');

        // Excluded pages (utility, account, auth, general info, homepage)
        if (path === '/' || path === '/index.html' || path === '' ||
            path.startsWith('/login') || path.startsWith('/signup') ||
            path.startsWith('/dashboard') || path.startsWith('/profile') ||
            path.startsWith('/settings') || path.startsWith('/notifications') ||
            path.startsWith('/admin') || path.startsWith('/privacy-policy') ||
            path.startsWith('/404') || path.startsWith('/offline') ||
            path.startsWith('/search')) {
            return null;
        }

        // ==========================================
        // 1. CLASS PAGES
        // ==========================================
        if (path.includes('/class-9') || path.startsWith('/class-9')) {
            let icon = 'fa-calculator';
            let badge = 'CBSE Foundation';
            if (path.includes('science')) { icon = 'fa-atom'; badge = 'Class 9 Science'; }
            else if (path.includes('advanced-maths')) { icon = 'fa-square-root-alt'; badge = 'Advanced Maths'; }
            else if (path.includes('notes')) { icon = 'fa-book-open'; badge = 'Revision Notes'; }
            else if (path.includes('ncert') || path.includes('exercise')) { icon = 'fa-check-double'; badge = 'NCERT Solutions'; }
            else if (path.includes('worksheet')) { icon = 'fa-tasks'; badge = 'Worksheet'; }
            else if (path.includes('test')) { icon = 'fa-vial'; badge = 'Chapter Test'; }
            return { type: 'class', category: 'Class 9', badge, icon, accent: 'var(--color-c9, #16634b)' };
        }

        if (path.includes('/class-10') || path.startsWith('/class-10') || path.includes('class-10')) {
            let icon = 'fa-square-root-alt';
            let badge = 'CBSE Board';
            if (path.includes('social')) { icon = 'fa-globe-americas'; badge = 'Social Science'; }
            else if (path.includes('science')) { icon = 'fa-flask'; badge = 'Science Board'; }
            else if (path.includes('adaptive') || path.includes('learning')) { icon = 'fa-wand-magic-sparkles'; badge = 'Adaptive Hub'; }
            else if (path.includes('notes')) { icon = 'fa-book-open'; badge = 'Chapter Notes'; }
            else if (path.includes('ncert') || path.includes('exercise')) { icon = 'fa-check-double'; badge = 'NCERT Solutions'; }
            else if (path.includes('pyq') || path.includes('previous-year')) { icon = 'fa-history'; badge = '10-Year PYQs'; }
            return { type: 'class', category: 'Class 10', badge, icon, accent: 'var(--color-c10, #c2410c)' };
        }

        if (path.includes('/class-11') || path.startsWith('/class-11')) {
            let icon = 'fa-infinity';
            let badge = 'Higher Secondary';
            if (path.includes('physics')) { icon = 'fa-atom'; badge = 'Class 11 Physics'; }
            else if (path.includes('chemistry')) { icon = 'fa-flask-vial'; badge = 'Class 11 Chemistry'; }
            else if (path.includes('applied')) { icon = 'fa-chart-line'; badge = 'Applied Maths'; }
            else if (path.includes('notes')) { icon = 'fa-book-open'; badge = 'Notes'; }
            else if (path.includes('ncert')) { icon = 'fa-check-double'; badge = 'NCERT Solutions'; }
            return { type: 'class', category: 'Class 11', badge, icon, accent: 'var(--color-c11, #047857)' };
        }

        if (path.includes('/class-12') || path.startsWith('/class-12')) {
            let icon = 'fa-shapes';
            let badge = 'Board & Entrance';
            if (path.includes('physics')) { icon = 'fa-atom'; badge = 'Class 12 Physics'; }
            else if (path.includes('notes')) { icon = 'fa-book-open'; badge = 'Notes'; }
            else if (path.includes('ncert')) { icon = 'fa-check-double'; badge = 'NCERT Solutions'; }
            else if (path.includes('pyq')) { icon = 'fa-history'; badge = 'Board PYQs'; }
            return { type: 'class', category: 'Class 12', badge, icon, accent: 'var(--color-c12, #16634b)' };
        }

        if (path.includes('/smart-learning') || path.includes('/learning/topics')) {
            return { type: 'class', category: 'Adaptive Learning', badge: 'Class 10 Smart Hub', icon: 'fa-wand-magic-sparkles', accent: 'var(--color-c10, #c2410c)' };
        }

        if (path.includes('/ebooks')) {
            return { type: 'class', category: 'Revision Guides', badge: 'E-Books & Formulas', icon: 'fa-book-open', accent: 'var(--color-c12, #16634b)' };
        }

        // ==========================================
        // 2. EXAM PAGES
        // ==========================================
        if (path.includes('/upsc-topicwise-pyqs')) {
            let badge = '30-Year Archive (1995–2026)';
            if (path.includes('economy')) badge = 'UPSC PYQ Economy';
            else if (path.includes('polity')) badge = 'UPSC PYQ Polity';
            else if (path.includes('geography')) badge = 'UPSC PYQ Geography';
            else if (path.includes('history')) badge = 'UPSC PYQ History';
            else if (path.includes('environment')) badge = 'UPSC PYQ Environment';
            else if (path.includes('science')) badge = 'UPSC PYQ Science & Tech';
            return { type: 'exam', category: 'UPSC PYQs', badge, icon: 'fa-fire', accent: 'var(--color-upsc, #16634b)' };
        }
        if (path.includes('/upsc-aso')) {
            return { type: 'exam', category: 'UPSC ASO', badge: 'Air Safety Officer', icon: 'fa-plane', accent: 'var(--color-upsc, #16634b)' };
        }
        if (path.includes('/upsc-apfc')) {
            return { type: 'exam', category: 'UPSC APFC', badge: 'EPFO & APFC Hub', icon: 'fa-landmark', accent: 'var(--color-upsc, #16634b)' };
        }
        if (path.includes('/upsc')) {
            return { type: 'exam', category: 'UPSC', badge: 'Civil Services (GS & CSAT)', icon: 'fa-compass', accent: 'var(--color-upsc, #16634b)' };
        }
        if (path.includes('/upsssc-pet-topicwise-pyqs')) {
            let badge = '700 MCQs (2022–2025)';
            if (path.includes('graph')) badge = 'PET Graph Analysis (DI)';
            else if (path.includes('table')) badge = 'PET Table Analysis (DI)';
            else if (path.includes('unseen')) badge = 'PET Hindi Passages';
            else if (path.includes('general-hindi')) badge = 'PET General Hindi';
            else if (path.includes('history')) badge = 'PET Indian History';
            else if (path.includes('national-movement')) badge = 'PET National Movement';
            else if (path.includes('geography')) badge = 'PET Geography';
            else if (path.includes('economy')) badge = 'PET Indian Economy';
            else if (path.includes('constitution')) badge = 'PET Constitution & Polity';
            else if (path.includes('science')) badge = 'PET General Science';
            else if (path.includes('current-affairs')) badge = 'PET Current Affairs';
            else if (path.includes('general-awareness')) badge = 'PET General Awareness';
            else if (path.includes('arithmetic')) badge = 'PET Arithmetic';
            else if (path.includes('reasoning')) badge = 'PET Logic & Reasoning';
            else if (path.includes('english')) badge = 'PET English';
            return { type: 'exam', category: 'UPSSSC PET PYQs', badge, icon: 'fa-fire', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/upsssc-pet')) {
            let badge = 'State Commission';
            if (path.includes('current-affairs')) badge = 'PET Current Affairs';
            else if (path.includes('general-awareness')) badge = 'PET General Awareness';
            else if (path.includes('hindi')) badge = 'PET Hindi';
            else if (path.includes('history')) badge = 'PET History';
            else if (path.includes('geography')) badge = 'PET Geography';
            else if (path.includes('polity')) badge = 'PET Polity';
            else if (path.includes('economy')) badge = 'PET Economy';
            else if (path.includes('science')) badge = 'PET Science';
            else if (path.includes('english')) badge = 'PET English';
            return { type: 'exam', category: 'UPSSSC PET', badge, icon: 'fa-scroll', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/upsssc-intermediate')) {
            return { type: 'exam', category: 'UPSSSC Intermediate', badge: 'Intermediate Level Mains', icon: 'fa-layer-group', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/upsssc-lower-mains')) {
            return { type: 'exam', category: 'UPSSSC Lower Mains', badge: 'Lower Subordinate Services', icon: 'fa-briefcase', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/upsssc-up-gk')) {
            return { type: 'exam', category: 'UPSSSC UP GK', badge: 'UP Special GK 20M', icon: 'fa-map-marked-alt', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/upsssc-computer')) {
            return { type: 'exam', category: 'UPSSSC Computer', badge: 'Computer & IT 15M', icon: 'fa-laptop-code', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/upsssc')) {
            return { type: 'exam', category: 'UPSSSC', badge: 'State Commission', icon: 'fa-scroll', accent: 'var(--color-upsssc, #0d9488)' };
        }
        if (path.includes('/ssc-cgl') || path.includes('/ssc')) {
            return { type: 'exam', category: 'SSC CGL', badge: 'Staff Selection (CGL & CHSL)', icon: 'fa-clipboard-list', accent: 'var(--color-ssc, #995028)' };
        }
        if (path.includes('/ahc-ro-aro')) {
            return { type: 'exam', category: 'AHC RO / ARO', badge: 'High Court Judiciary', icon: 'fa-balance-scale', accent: 'var(--color-state, #16634b)' };
        }
        if (path.includes('/up-tgt-pgt-gk')) {
            return { type: 'exam', category: 'UP TGT & PGT GK', badge: 'General Knowledge 30M', icon: 'fa-globe-asia', accent: 'var(--color-state, #16634b)' };
        }
        if (path.includes('/up-assistant-teacher')) {
            return { type: 'exam', category: 'UP Assistant Teacher', badge: 'Super TET (Primary)', icon: 'fa-chalkboard-teacher', accent: 'var(--color-state, #16634b)' };
        }
        if (path.includes('/up-upper-primary')) {
            return { type: 'exam', category: 'UP Upper Primary', badge: 'Junior High School 6-8', icon: 'fa-user-graduate', accent: 'var(--color-state, #16634b)' };
        }
        const tgtMatch = path.match(/\/up-tgt-([a-z-]+)/);
        if (tgtMatch && tgtMatch[1] !== 'pgt-gk') {
            const rawSub = tgtMatch[1];
            const subName = rawSub.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
            return { type: 'exam', category: `UP TGT ${subName}`, badge: 'TGT Teacher Exam', icon: 'fa-award', accent: 'var(--color-state, #16634b)' };
        }
        if (path.includes('/up-tgt')) {
            return { type: 'exam', category: 'UP TGT', badge: 'TGT Teacher Exam', icon: 'fa-award', accent: 'var(--color-state, #16634b)' };
        }
        const pgtMatch = path.match(/\/up-pgt-([a-z-]+)/);
        if (pgtMatch) {
            const rawSub = pgtMatch[1];
            const subName = rawSub.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
            return { type: 'exam', category: `UP PGT ${subName}`, badge: 'PGT Teacher Exam', icon: 'fa-award', accent: 'var(--color-state, #16634b)' };
        }
        if (path.includes('/up-pgt')) {
            return { type: 'exam', category: 'UP PGT', badge: 'PGT Teacher Exam', icon: 'fa-award', accent: 'var(--color-state, #16634b)' };
        }
        if (path.includes('/csir-net')) {
            return { type: 'exam', category: 'CSIR NET', badge: 'National Eligibility Test', icon: 'fa-graduation-cap', accent: 'var(--brand-primary, #16634b)' };
        }
        if (path.includes('/ib')) {
            return { type: 'exam', category: 'IB Mathematics', badge: 'Diploma & MYP', icon: 'fa-globe', accent: '#885a17' };
        }
        if (path.includes('/sat')) {
            return { type: 'exam', category: 'Digital SAT Math', badge: 'College Board Prep', icon: 'fa-pen-ruler', accent: 'var(--color-amber, #d97706)' };
        }
        if (path.includes('/current-affairs')) {
            return { type: 'exam', category: 'Current Affairs', badge: 'Daily CA & MCQs', icon: 'fa-newspaper', accent: 'var(--color-ssc, #995028)' };
        }
        if (path.includes('/competitive-exams')) {
            return { type: 'exam', category: 'Competitive Exams', badge: 'Govt Prep Hub', icon: 'fa-landmark', accent: 'var(--color-upsc, #16634b)' };
        }

        // Subject exam hubs
        const subjects = [
            'history', 'geography', 'economics', 'civics', 'physics', 'chemistry',
            'mathematics', 'hindi', 'english', 'sanskrit', 'agriculture', 'art',
            'commerce', 'home-science', 'military-science', 'music-instrumental',
            'music-vocal', 'physical-education', 'psychology', 'sociology', 'logic'
        ];
        for (const s of subjects) {
            if (path.includes(`/${s}/`) || path === `/${s}`) {
                const name = s.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
                return { type: 'exam', category: `${name} Hub`, badge: 'Subject Syllabus', icon: 'fa-book', accent: 'var(--brand-primary, #16634b)' };
            }
        }

        return null;
    }

    function saveStudyPage(item) {
        if (!item || !item.url) return;
        try {
            const normalized = {
                url: item.url,
                path: item.path || item.url.split('?')[0].split('#')[0],
                title: (item.title || 'Study Resource').slice(0, 100),
                category: item.category || 'Study Hub',
                badge: item.badge || (item.type === 'class' ? 'School Curriculum' : 'Competitive Exam'),
                type: item.type === 'class' ? 'class' : 'exam',
                icon: item.icon || (item.type === 'class' ? 'fa-graduation-cap' : 'fa-landmark'),
                timestamp: item.timestamp || Date.now()
            };

            // Save as primary last study page
            localStorage.setItem(STORAGE_KEY_LAST, JSON.stringify(normalized));

            // Also maintain history array (max items)
            let history = [];
            try {
                history = JSON.parse(localStorage.getItem(STORAGE_KEY_HISTORY) || '[]');
                if (!Array.isArray(history)) history = [];
            } catch (e) {
                history = [];
            }

            // Deduplicate by path
            history = history.filter(h => h && h.path !== normalized.path && h.url !== normalized.url);
            history.unshift(normalized);
            if (history.length > MAX_HISTORY) history = history.slice(0, MAX_HISTORY);

            localStorage.setItem(STORAGE_KEY_HISTORY, JSON.stringify(history));
        } catch (error) {
            console.warn('SJMaths study tracker could not save:', error);
        }
    }

    function getLastStudyPage() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY_LAST);
            if (!raw) return null;
            const item = JSON.parse(raw);
            if (!item || !item.url || typeof item.url !== 'string') return null;
            return item;
        } catch (error) {
            return null;
        }
    }

    function getStudyHistory() {
        try {
            const raw = localStorage.getItem(STORAGE_KEY_HISTORY);
            if (!raw) return [];
            const list = JSON.parse(raw);
            return Array.isArray(list) ? list : [];
        } catch (error) {
            return [];
        }
    }

    function clearLastStudyPage() {
        try {
            localStorage.removeItem(STORAGE_KEY_LAST);
        } catch (error) {}
    }

    function formatRelativeTime(timestamp) {
        if (!timestamp) return 'Recently';
        const elapsedSec = Math.max(0, Math.floor((Date.now() - timestamp) / 1000));
        if (elapsedSec < 90) return 'Just now';
        const elapsedMin = Math.floor(elapsedSec / 60);
        if (elapsedMin < 60) return `${elapsedMin} min${elapsedMin === 1 ? '' : 's'} ago`;
        const elapsedHours = Math.floor(elapsedMin / 60);
        if (elapsedHours < 24) return `${elapsedHours} hour${elapsedHours === 1 ? '' : 's'} ago`;
        const elapsedDays = Math.floor(elapsedHours / 24);
        if (elapsedDays === 1) return 'Yesterday';
        if (elapsedDays < 30) return `${elapsedDays} days ago`;
        const elapsedMonths = Math.floor(elapsedDays / 30);
        return `${elapsedMonths} month${elapsedMonths === 1 ? '' : 's'} ago`;
    }

    function trackCurrentPage() {
        try {
            if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
            const path = window.location.pathname;
            const classification = classifyStudyPage(path);
            if (!classification) return;

            let pageTitle = '';
            const h1 = document.querySelector('h1');
            if (h1 && h1.textContent.trim().length > 3 && h1.textContent.trim().length < 85) {
                pageTitle = h1.textContent.replace(/\s+/g, ' ').trim();
            } else {
                pageTitle = document.title
                    .split('|')[0]
                    .split('—')[0]
                    .split('–')[0]
                    .replace(/\s*[-–—]\s*SJMaths.*$/i, '')
                    .replace(/SJMaths/i, '')
                    .trim();
            }

            if (!pageTitle) pageTitle = classification.category;

            saveStudyPage({
                url: window.location.pathname + window.location.search + window.location.hash,
                path: window.location.pathname,
                title: pageTitle,
                category: classification.category,
                badge: classification.badge,
                type: classification.type,
                icon: classification.icon,
                timestamp: Date.now()
            });
        } catch (error) {
            console.debug('Study tracker tracking error:', error);
        }
    }

    // Expose API globally
    window.SJStudyTracker = {
        classifyStudyPage,
        saveStudyPage,
        getLastStudyPage,
        getStudyHistory,
        clearLastStudyPage,
        formatRelativeTime,
        trackCurrentPage
    };

    // Auto-track current page if not already run
    if (!window.__sjStudyTrackerTracked) {
        window.__sjStudyTrackerTracked = true;
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', trackCurrentPage, { once: true });
        } else {
            trackCurrentPage();
        }
    }
})();
