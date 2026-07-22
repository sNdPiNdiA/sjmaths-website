const fs = require('fs');

const days = JSON.parse(fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso-parsed.json'));

// Slugify helper
function slugify(text) {
    return text.toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-|-$)+/g, '');
}

const phases = [
    { id: 'phase-1', code: 'P1', title: 'Phase 1: Foundations', badge: 'Days 1 - 27', desc: 'Engineering Fundamentals, Fluid Mechanics & Machinery, Thermodynamics, and Heat Transfer core principles.', filter: d => d.macroPhase.includes('PHASE 1') },
    { id: 'phase-2', code: 'P2', title: 'Phase 2: Core Aeronautical', badge: 'Days 28 - 53', desc: 'Aerodynamics, Airfoils, Compressible Flow, Aircraft Structures, and Aircraft Propulsion systems.', filter: d => d.macroPhase.includes('PHASE 2') },
    { id: 'phase-3', code: 'P3', title: 'Phase 3: Systems & Applied', badge: 'Days 54 - 79', desc: 'Aircraft Systems & Avionics, Hydraulics, Cockpit Controls, Flight Controls, Navigation, Flight Mechanics, and Elements of Aeronautics.', filter: d => d.macroPhase.includes('PHASE 3') },
    { id: 'phase-4', code: 'P4', title: 'Phase 4: Regulatory & Operational', badge: 'Days 80 - 117', desc: 'Air Traffic Control (ATC), Air Safety & Human Factors, DGCA / ICAO Aviation Regulations, and Aircraft Maintenance.', filter: d => d.macroPhase.includes('PHASE 4') },
    { id: 'phase-5', code: 'P5', title: 'Phase 5: PYQs, Mocks & Final Revision', badge: 'Days 118 - 129', desc: 'Full-syllabus PYQ sweep, 100-Question Timed Mock Tests, Error Book Drilling, and Phase Formula Book rapid recall.', filter: d => d.macroPhase.includes('PHASE 5') }
];

function generateHTML() {
    let tabButtons = '';
    let tabPanels = '';
    let tabTitlesObj = {};

    phases.forEach((phase, idx) => {
        const isFirst = idx === 0;
        const phaseDays = days.filter(phase.filter);
        tabTitlesObj[phase.id] = phase.title;

        tabButtons += `
            <button class="tab-btn ${isFirst ? 'active' : ''}" data-target="${phase.id}">
                <i class="fas ${idx === 0 ? 'fa-square-root-variable' : (idx === 1 ? 'fa-plane' : (idx === 2 ? 'fa-microchip' : (idx === 3 ? 'fa-shield-halved' : 'fa-clipboard-check')))}"></i> 
                <span>${phase.title}</span> 
                <span class="badge" id="badge-${phase.id}">(0%)</span>
            </button>`;

        const subjectMap = new Map();
        phaseDays.forEach(d => {
            if (!subjectMap.has(d.subject)) {
                subjectMap.set(d.subject, []);
            }
            subjectMap.get(d.subject).push(d);
        });

        let subjectCardsHTML = '';
        let subjIndex = 0;

        subjectMap.forEach((subjDays, subjName) => {
            subjIndex++;
            const subjId = `${phase.id}-subj-${subjIndex}`;
            let detailsHTML = '';

            subjDays.forEach((d) => {
                const dayBadgeColor = d.type.includes('STUDY') ? '#2980b9' : (d.type.includes('REVISION') ? '#e67e22' : (d.type.includes('FLOAT') ? '#8e44ad' : '#27ae60'));

                const rawMicro = d.microtopics || '';
                const microItems = rawMicro.split(/;|•|\n/).map(s => s.trim()).filter(Boolean);

                let listItemsHTML = '';
                microItems.forEach((itemText, mIdx) => {
                    const cbId = `aso-cb-d${d.day}-m${mIdx + 1}`;
                    const topicSlug = slugify(itemText);
                    const topicUrl = `/upsc-aso/day-${d.day}/${topicSlug}/`;

                    listItemsHTML += `
                        <li class="syllabus-item">
                            <input type="checkbox" class="syllabus-checkbox" id="${cbId}">
                            <label for="${cbId}" class="syllabus-text">
                                <a href="${topicUrl}" class="microtopic-link" onclick="event.stopPropagation();">${itemText}</a>
                            </label>
                        </li>`;
                });

                detailsHTML += `
                    <details class="syllabus-subsection" data-prefix="${phase.id}" data-grp-idx="${d.day}" open style="margin-bottom: 0.85rem;">
                        <summary class="subsection-summary">
                            <div style="display: flex; flex-direction: column; gap: 0.25rem; flex-grow: 1; padding-right: 0.5rem;">
                                <div style="display: flex; align-items: center; gap: 0.5rem; flex-wrap: wrap;">
                                    <span class="badge-exam" style="background: rgba(41, 128, 185, 0.1); color: ${dayBadgeColor}; font-weight: 700;">Day ${d.day} • ${d.type}</span>
                                    <span style="font-size: 0.75rem; color: #718096; background: rgba(0,0,0,0.04); padding: 2px 8px; border-radius: 10px;"><i class="far fa-clock"></i> ${d.time}</span>
                                    <span style="font-size: 0.75rem; color: #d4af37; font-weight: 600; background: rgba(212, 175, 55, 0.1); padding: 2px 8px; border-radius: 10px;">${d.phaseCode}</span>
                                </div>
                                <span class="subsection-title" style="margin-top: 0.25rem; font-size: 0.95rem; color: #1a202c; font-weight: 600;">
                                    ${d.subject}
                                </span>
                            </div>
                            <div class="subsection-meta">
                                <span class="subsection-progress" id="${phase.id}-prog-${d.day}">0/${microItems.length}</span>
                                <i class="fas fa-chevron-down toggle-icon"></i>
                            </div>
                        </summary>
                        <ul class="syllabus-list" style="padding: 0.5rem 0.75rem;">
                            ${listItemsHTML}
                        </ul>
                    </details>`;
            });

            subjectCardsHTML += `
                <div class="subject-card" id="${subjId}">
                    <h2 class="subject-title">
                        <span>${subjName}</span>
                        <i class="fas fa-layer-group"></i>
                    </h2>
                    <div class="card-scrollable">
                        ${detailsHTML}
                    </div>
                </div>`;
        });

        tabPanels += `
            <!-- ==================== ${phase.title.toUpperCase()} PANEL ==================== -->
            <div class="tab-panel ${isFirst ? 'active' : ''}" id="panel-${phase.id}">
                <div class="syllabus-intro-alert">
                    <i class="fas fa-circle-info"></i>
                    <div>
                        <strong>${phase.title} (${phase.badge})</strong>: ${phase.desc} Click any microtopic to open its structured study module.
                    </div>
                </div>
                <div class="subjects-grid">
                    ${subjectCardsHTML}
                </div>
            </div>`;
    });

    const fullPageHTML = `<!DOCTYPE html><html lang="en"><head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UPSC Air Safety Officer (ASO) 129-Day Study Plan & Interactive Microtopic Syllabus Tracker | SJMaths</title>
    <meta name="description" content="Exhaustive 129-day interactive microtopic study plan for UPSC Air Safety Officer (ASO) exam. Access structured study modules for 650+ subtopics across Engineering, Aerodynamics, Aircraft Structures, Avionics, Regulations & Maintenance.">
    
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/upsc-aso/">
    <meta name="keywords" content="UPSC Air Safety Officer, UPSC ASO Study Plan, UPSC ASO Syllabus, Aeronautical Engineering Syllabus, DGCA CAR Regulations, Aircraft Maintenance, Aerodynamics Microtopics, SJMaths">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Open Graph -->
    <meta property="og:title" content="UPSC Air Safety Officer (ASO) 129-Day Study Plan & Microtopic Tracker | SJMaths">
    <meta property="og:description" content="Interactive 129-day microtopic tracker for UPSC Air Safety Officer exam. Learn & check off 650+ individual subtopics across Engineering, Aerodynamics, Systems, and DGCA Regulations.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://sjmaths.com/upsc-aso/">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="UPSC Air Safety Officer (ASO) 129-Day Study Plan | SJMaths">
    <meta name="twitter:description" content="Exhaustive sequenced 129-day microtopic checklist for UPSC Air Safety Officer exam. Track daily subtopics, PYQs, and timed mock tests.">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Outfit:wght@500;600;700;800&amp;display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript>
        <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    </noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=c54bbbc3">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=94ee8a40">
    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 10px 30px -5px rgba(41, 128, 185, 0.15);
            --accent-gradient: linear-gradient(135deg, #1e3c72, #2a5298, #d4af37);
        }

        .syllabus-container {
            max-width: 1150px;
            margin: 2rem auto;
            padding: 2.5rem 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }

        .syllabus-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .syllabus-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }

        .syllabus-header p {
            font-size: 1.1rem;
            color: var(--text-light);
            max-width: 850px;
            margin: 0 auto;
            line-height: 1.6;
        }

        .syllabus-tabs {
            display: flex;
            justify-content: center;
            gap: 0.75rem;
            margin-bottom: 2.5rem;
            flex-wrap: wrap;
            border-bottom: 2px solid rgba(0, 0, 0, 0.05);
            padding-bottom: 1rem;
        }

        .tab-btn {
            background: transparent;
            border: none;
            outline: none;
            padding: 0.75rem 1.25rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 0.95rem;
            color: var(--text-light);
            cursor: pointer;
            border-radius: 30px;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .tab-btn:hover {
            color: #1e3c72;
            background: rgba(30, 60, 114, 0.05);
        }

        .tab-btn.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3);
        }

        .tab-panel {
            display: none;
            animation: slideUp 0.4s ease-out;
        }

        .tab-panel.active {
            display: block;
        }

        .subjects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(48%, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        @media (max-width: 768px) {
            .subjects-grid {
                grid-template-columns: 1fr;
            }
        }

        .subject-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 1.75rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            overflow: hidden;
            max-height: 850px;
            display: flex;
            flex-direction: column;
        }

        .subject-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 15px 35px -5px rgba(30, 60, 114, 0.2);
        }

        .subject-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--accent-gradient);
        }

        .subject-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
        }

        .subject-title i {
            color: #1e3c72;
            opacity: 0.85;
        }

        .card-scrollable {
            overflow-y: auto;
            flex-grow: 1;
            padding-right: 0.5rem;
        }

        .card-scrollable::-webkit-scrollbar {
            width: 6px;
        }

        .card-scrollable::-webkit-scrollbar-track {
            background: transparent;
        }

        .card-scrollable::-webkit-scrollbar-thumb {
            background: rgba(30, 60, 114, 0.2);
            border-radius: 10px;
        }

        .syllabus-list {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }

        .syllabus-item {
            padding: 0.4rem 0.6rem;
            border-radius: 6px;
            transition: background-color 0.2s ease;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            cursor: pointer;
        }

        .syllabus-item:hover {
            background: rgba(30, 60, 114, 0.04);
        }

        .syllabus-checkbox {
            appearance: none;
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border: 2px solid var(--text-light);
            border-radius: 4px;
            outline: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }

        .syllabus-checkbox::before {
            content: "\\f00c";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            font-size: 0.7rem;
            color: #ffffff;
            display: none;
        }

        .syllabus-checkbox:checked {
            background: var(--accent-gradient);
            border-color: transparent;
        }

        .syllabus-checkbox:checked::before {
            display: block;
        }

        .syllabus-text {
            font-size: 0.88rem;
            color: var(--text-dark);
            line-height: 1.45;
            cursor: pointer;
            transition: color 0.2s ease, text-decoration 0.2s ease;
            user-select: none;
            flex-grow: 1;
        }

        .microtopic-link {
            color: inherit;
            text-decoration: none;
            transition: color 0.2s ease;
        }

        .microtopic-link:hover {
            color: #1e3c72;
            text-decoration: underline;
        }

        .syllabus-checkbox:checked + .syllabus-text .microtopic-link {
            color: #9ca3af;
            text-decoration: line-through;
        }

        .tracker-banner {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 1.5rem;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            flex-wrap: wrap;
        }

        .tracker-info h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 0.25rem;
        }

        .tracker-info p {
            font-size: 0.9rem;
            color: var(--text-light);
        }

        .tracker-progress-container {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-grow: 1;
            max-width: 500px;
            justify-content: flex-end;
        }

        .progress-bar-wrapper {
            background: rgba(0, 0, 0, 0.05);
            border-radius: 10px;
            height: 12px;
            width: 100%;
            overflow: hidden;
            position: relative;
        }

        .progress-bar-fill {
            background: var(--accent-gradient);
            height: 100%;
            width: 0%;
            transition: width 0.4s ease-out;
            border-radius: 10px;
        }

        .progress-percentage {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.15rem;
            color: #1e3c72;
            min-width: 55px;
            text-align: right;
        }

        .syllabus-intro-alert {
            background: rgba(30, 60, 114, 0.05);
            border: 1px solid rgba(30, 60, 114, 0.15);
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 2rem;
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--text-dark);
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
        }

        .syllabus-intro-alert i {
            color: #1e3c72;
            font-size: 1.25rem;
            margin-top: 0.2rem;
        }

        details.syllabus-subsection {
            background: rgba(255, 255, 255, 0.6);
            border: 1px solid rgba(0, 0, 0, 0.06);
            border-radius: 10px;
            transition: all 0.3s ease;
            overflow: hidden;
        }

        details.syllabus-subsection[open] {
            background: var(--glass-bg);
            border-color: rgba(30, 60, 114, 0.25);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        }

        summary.subsection-summary {
            padding: 0.85rem 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            list-style: none;
            user-select: none;
        }

        summary.subsection-summary::-webkit-details-marker {
            display: none;
        }

        .subsection-meta {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .subsection-progress {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.2rem 0.6rem;
            background: rgba(0, 0, 0, 0.05);
            color: var(--text-light);
            border-radius: 12px;
            white-space: nowrap;
        }

        .subsection-progress.completed {
            background: rgba(46, 204, 113, 0.15);
            color: #2ecc71;
        }

        .toggle-icon {
            font-size: 0.8rem;
            color: var(--text-light);
            transition: transform 0.3s ease;
        }

        details.syllabus-subsection[open] .toggle-icon {
            transform: rotate(180deg);
            color: #1e3c72;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>

    <!-- Structured Data: Breadcrumbs -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://sjmaths.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "UPSC Air Safety Officer (ASO) Study Plan",
          "item": "https://sjmaths.com/upsc-aso/"
        }
      ]
    }
    </script>
</head>

<body>
    <!-- Dynamic Header -->
    <div id="header-container"></div>

    <main class="syllabus-container" id="main-content">
        
        <!-- Header Section -->
        <div class="syllabus-header">
            <h1>UPSC Air Safety Officer (ASO) Study Plan</h1>
            <p>Interactive 129-Day Sequenced Study Plan built from the 620-microtopic Ultimate Checklist. Every single subtopic is listed individually so you can learn, track, and master each topic step by step.</p>
        </div>

        <!-- Examination Overview Table -->
        <div class="exam-plan-container" style="margin-bottom: 2.5rem; overflow-x: auto;">
            <h2 style="text-align: center; margin-bottom: 1.25rem; font-family: 'Outfit', sans-serif;">UPSC ASO 129-Day Study Plan Overview</h2>
            <table class="exam-plan-table" style="width: 100%; border-collapse: collapse; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                <thead>
                    <tr style="background: rgba(30, 60, 114, 0.1); border-bottom: 2px solid #1e3c72;">
                        <th style="padding: 14px; text-align: left; border: 1px solid var(--glass-border);">Phase</th>
                        <th style="padding: 14px; text-align: left; border: 1px solid var(--glass-border);">Phase Name</th>
                        <th style="padding: 14px; text-align: center; border: 1px solid var(--glass-border);">Days</th>
                        <th style="padding: 14px; text-align: left; border: 1px solid var(--glass-border);">Core Focus Area & Subjects</th>
                        <th style="padding: 14px; text-align: center; border: 1px solid var(--glass-border);">Est. Daily Time</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: bold; color: #1e3c72;">Phase 1</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: 600;"><a href="#" onclick="openPhase('phase-1', event)" style="color: #2980b9; text-decoration: none;">Foundations</a></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Days 1 – 27</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border);">Engineering Fundamentals, Fluid Mechanics & Machinery, Thermodynamics, Heat Transfer</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">120 - 465 min</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: bold; color: #1e3c72;">Phase 2</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: 600;"><a href="#" onclick="openPhase('phase-2', event)" style="color: #2980b9; text-decoration: none;">Core Aeronautical</a></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Days 28 – 53</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border);">Aerodynamics, Airfoil Theory, Aircraft Structures, FEM, Aircraft Propulsion</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">120 - 465 min</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: bold; color: #1e3c72;">Phase 3</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: 600;"><a href="#" onclick="openPhase('phase-3', event)" style="color: #2980b9; text-decoration: none;">Systems & Applied</a></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Days 54 – 79</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border);">Aircraft Systems & Avionics, Hydraulics, Cockpit Controls, Flight Mechanics, Elements of Aeronautics</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">120 - 450 min</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: bold; color: #1e3c72;">Phase 4</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: 600;"><a href="#" onclick="openPhase('phase-4', event)" style="color: #2980b9; text-decoration: none;">Regulatory & Operational</a></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Days 80 – 117</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border);">ATC & Planning, Air Safety & Human Factors, DGCA / ICAO Aviation Regulations, Aircraft Maintenance</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">120 - 465 min</td>
                    </tr>
                    <tr>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: bold; color: #1e3c72;">Phase 5</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border); font-weight: 600;"><a href="#" onclick="openPhase('phase-5', event)" style="color: #2980b9; text-decoration: none;">PYQs, Mocks & Final Revision</a></td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Days 118 – 129</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border);">Full Syllabus PYQ Sweep, 100-Q Timed Mocks, Error Book Drilling, Phase Formula Books, Rapid Recall</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">150 - 180 min</td>
                    </tr>
                    <tr style="background: rgba(0, 0, 0, 0.02); font-weight: bold;">
                        <td colspan="2" style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Total Curriculum Scope</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">129 Days</td>
                        <td style="padding: 12px; border: 1px solid var(--glass-border);">650+ Individual Microtopics Checklist</td>
                        <td style="padding: 12px; text-align: center; border: 1px solid var(--glass-border);">Complete Mastery</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <script>
        function openPhase(phaseId, e) {
            if (e) e.preventDefault();
            const targetTab = document.querySelector(\`.tab-btn[data-target="\${phaseId}"]\`);
            if (targetTab) {
                targetTab.click();
            }
        }
        </script>

        <!-- Progress Tracker Banner -->
        <div class="tracker-banner">
            <div class="tracker-info">
                <h2><span id="activeProgressTitle">Phase 1: Foundations</span> Progress</h2>
                <p>Check off each individual microtopic as you finish studying it. Progress is saved automatically.</p>
            </div>
            <div class="tracker-progress-container">
                <div class="progress-bar-wrapper">
                    <div class="progress-bar-fill" id="syllabusProgressBar"></div>
                </div>
                <div class="progress-percentage" id="syllabusProgressPercent">0%</div>
            </div>
        </div>

        <!-- Dynamic Phase Tabs Navigation -->
        <div class="syllabus-tabs">
            ${tabButtons}
        </div>

        <!-- Dynamic Tab Panels -->
        ${tabPanels}

    </main>

    <!-- Interactive Script for Tabs, Microtopic Checkboxes, LocalStorage & Progress -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabPanels = document.querySelectorAll('.tab-panel');
            const progressBar = document.getElementById('syllabusProgressBar');
            const progressPercent = document.getElementById('syllabusProgressPercent');
            const activeProgressTitle = document.getElementById('activeProgressTitle');

            const tabTitles = ${JSON.stringify(tabTitlesObj)};

            function getActiveTab() {
                const activeBtn = document.querySelector('.tab-btn.active');
                return activeBtn ? activeBtn.getAttribute('data-target') : 'phase-1';
            }

            // Tab Switching Logic
            tabButtons.forEach(button => {
                button.addEventListener('click', () => {
                    const targetTab = button.getAttribute('data-target');

                    tabButtons.forEach(btn => btn.classList.remove('active'));
                    button.classList.add('active');

                    tabPanels.forEach(panel => {
                        panel.classList.remove('active');
                        if (panel.id === \`panel-\${targetTab}\`) {
                            panel.classList.add('active');
                        }
                    });

                    if (activeProgressTitle) {
                        activeProgressTitle.innerHTML = tabTitles[targetTab] || 'Study Plan';
                    }
                    updateProgress();

                    document.querySelector('.syllabus-tabs').scrollIntoView({ behavior: 'smooth', block: 'start' });
                });
            });

            // Interactive Microtopic Checkboxes & Local Storage
            const checkboxes = document.querySelectorAll('.syllabus-checkbox');
            const storedProgress = JSON.parse(localStorage.getItem('upsc-aso-microtopics-progress')) || {};

            checkboxes.forEach(checkbox => {
                const id = checkbox.id;
                if (storedProgress[id]) {
                    checkbox.checked = true;
                }

                checkbox.addEventListener('change', () => {
                    storedProgress[checkbox.id] = checkbox.checked;
                    localStorage.setItem('upsc-aso-microtopics-progress', JSON.stringify(storedProgress));
                    updateProgress();
                });
            });

            // Progress recalculation logic for phase tabs and subsections
            function updateProgress() {
                const activeTab = getActiveTab();
                const tabIds = ['phase-1', 'phase-2', 'phase-3', 'phase-4', 'phase-5'];

                tabIds.forEach(tabId => {
                    const panel = document.getElementById(\`panel-\${tabId}\`);
                    if (!panel) return;

                    const tabCheckboxes = panel.querySelectorAll('.syllabus-checkbox');
                    const total = tabCheckboxes.length;
                    const checked = Array.from(tabCheckboxes).filter(cb => cb.checked).length;
                    const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;

                    const badge = document.getElementById(\`badge-\${tabId}\`);
                    if (badge) {
                        badge.textContent = \`(\${percentage}%)\`;
                    }

                    if (tabId === activeTab) {
                        if (progressBar) progressBar.style.width = \`\${percentage}%\`;
                        if (progressPercent) progressPercent.textContent = \`\${percentage}%\`;
                    }
                });

                // Subsection badges
                const subsections = document.querySelectorAll('.syllabus-subsection');
                subsections.forEach(sub => {
                    const prefix = sub.getAttribute('data-prefix');
                    const grpIdx = sub.getAttribute('data-grp-idx');
                    const subCheckboxes = sub.querySelectorAll('.syllabus-checkbox');
                    const subTotal = subCheckboxes.length;
                    const subChecked = Array.from(subCheckboxes).filter(cb => cb.checked).length;

                    const progEl = document.getElementById(\`\${prefix}-prog-\${grpIdx}\`);
                    if (progEl) {
                        progEl.textContent = \`\${subChecked}/\${subTotal}\`;
                        if (subChecked === subTotal && subTotal > 0) {
                            progEl.classList.add('completed');
                        } else {
                            progEl.classList.remove('completed');
                        }
                    }
                });
            }

            updateProgress();
        });
    </script>

    <!-- Analytics Module -->
    <script type="module">
        const load = async () => {
            try {
                await import("/assets/js/firebase-analytics-only.min.js?v=b9396571");
            } catch (e) { console.debug("Analytics deferred"); }
        };
        if ('requestIdleCallback' in window) requestIdleCallback(load); else setTimeout(load, 3000);
    </script>

    <!-- Footer Section -->
    <footer id="site-footer"></footer>

    <!-- Back to Top Button -->
    <button id="backToTop" class="back-to-top" aria-label="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <!-- JavaScript References -->
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body></html>`;

    return fullPageHTML;
}

if (!fs.existsSync('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso')) {
    fs.mkdirSync('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso', { recursive: true });
}

fs.writeFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso/index.html', generateHTML());
console.log('Successfully regenerated c:/Users/sande/Documents/GitHub/sjmaths-website/upsc-aso/index.html');
