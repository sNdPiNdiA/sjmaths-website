const fs = require('fs');
const path = require('path');

const indexPath = path.resolve('upsc-aso/index.html');
let content = fs.readFileSync(indexPath, 'utf8');

// 1. Remove upsssc-lower.min.css stylesheet
content = content.replace(/<link rel="stylesheet" href="\/assets\/css\/upsssc-lower\.min\.css\?v=[^"]*">\r?\n?/, '');

// 2. Modern, eye-friendly, calm daylight UI stylesheet
const newStyle = `<style>
        :root {
            --bg-canvas: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #ffffff;
            --border-color: #e2e8f0;
            --border-subtle: #f1f5f9;
            --text-dark: #0f172a;
            --text-body: #334155;
            --text-light: #64748b;
            --primary-blue: #1e40af;
            --primary-hover: #2563eb;
            --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.05);
            --shadow-md: 0 4px 16px -2px rgba(15, 23, 42, 0.06);
            --accent-gradient: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
        }

        html, body {
            background-color: var(--bg-canvas) !important;
            color: var(--text-body) !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            line-height: 1.65;
            -webkit-font-smoothing: antialiased;
        }

        .syllabus-container {
            max-width: 1200px;
            margin: 1.5rem auto 3rem;
            padding: 1.75rem 1.25rem;
            animation: fadeIn 0.4s ease-out;
        }

        .syllabus-header {
            text-align: center;
            margin-bottom: 2.25rem;
        }

        .syllabus-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2rem, 4vw, 2.6rem);
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 0.75rem 0;
            letter-spacing: -0.025em;
        }

        .syllabus-header p {
            font-size: 1.05rem;
            color: var(--text-light);
            max-width: 820px;
            margin: 0 auto;
            line-height: 1.65;
        }

        /* At a Glance Exam Plan Container */
        .exam-plan-container {
            margin-bottom: 2rem;
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }

        .exam-plan-container h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
            text-align: center;
            margin: 0 0 1.25rem 0;
        }

        .exam-plan-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid var(--border-color);
            font-size: 0.88rem;
        }

        .exam-plan-table thead tr {
            background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%) !important;
        }

        .exam-plan-table th {
            background: transparent !important;
            color: #ffffff !important;
            padding: 11px 14px !important;
            font-weight: 700 !important;
            font-size: 0.82rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
            border: none !important;
            white-space: nowrap;
        }

        .exam-plan-table td {
            padding: 10px 14px !important;
            color: var(--text-body) !important;
            border-bottom: 1px solid var(--border-color) !important;
            border-top: none !important;
            border-left: none !important;
            border-right: none !important;
            line-height: 1.5 !important;
        }

        .exam-plan-table tbody tr:last-child td {
            border-bottom: none !important;
        }

        .exam-plan-table tbody tr:nth-child(even) {
            background: #f8fafc;
        }

        .exam-plan-table tbody tr:hover {
            background: #eff6ff;
        }

        /* Tracker Banner */
        .tracker-banner {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            box-shadow: var(--shadow-sm);
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.75rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            flex-wrap: wrap;
        }

        .tracker-info h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-dark);
            margin: 0 0 0.2rem 0;
        }

        .tracker-info p {
            font-size: 0.88rem;
            color: var(--text-light);
            margin: 0;
        }

        .tracker-progress-container {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-grow: 1;
            max-width: 480px;
            justify-content: flex-end;
        }

        .progress-bar-wrapper {
            background: #f1f5f9;
            border-radius: 999px;
            height: 10px;
            width: 100%;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }

        .progress-bar-fill {
            background: linear-gradient(90deg, #1e40af, #3b82f6);
            height: 100%;
            width: 0%;
            transition: width 0.4s ease-out;
            border-radius: 999px;
        }

        .progress-percentage {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 1.1rem;
            color: var(--primary-blue);
            min-width: 48px;
            text-align: right;
        }

        /* Syllabus Navigation Tabs */
        .syllabus-tabs {
            display: flex;
            justify-content: center;
            gap: 0.35rem;
            margin: 0 auto 2rem;
            background: #f1f5f9;
            padding: 5px;
            border-radius: 999px;
            border: 1px solid var(--border-color);
            width: fit-content;
            max-width: 100%;
            overflow-x: auto;
            scrollbar-width: none;
        }

        .syllabus-tabs::-webkit-scrollbar {
            display: none;
        }

        .tab-btn {
            background: transparent;
            border: none;
            outline: none;
            padding: 0.55rem 1.15rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 0.88rem;
            color: var(--text-light);
            cursor: pointer;
            border-radius: 999px;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .tab-btn:hover:not(.active) {
            color: var(--text-dark);
            background: #e2e8f0;
        }

        .tab-btn.active {
            background: var(--primary-blue);
            color: #ffffff;
            box-shadow: 0 2px 8px rgba(30, 64, 175, 0.25);
        }

        .tab-panel {
            display: none;
            animation: slideUp 0.35s ease-out;
        }

        .tab-panel.active {
            display: block;
        }

        /* Grid & Cards */
        .subjects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(48%, 1fr));
            gap: 1.25rem;
            margin-bottom: 1.5rem;
        }

        @media (max-width: 768px) {
            .subjects-grid {
                grid-template-columns: 1fr;
            }
        }

        .subject-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            box-shadow: var(--shadow-sm);
            padding: 1.25rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            position: relative;
            overflow: hidden;
            max-height: 750px;
            display: flex;
            flex-direction: column;
        }

        .subject-card:hover {
            box-shadow: var(--shadow-md);
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
            font-size: 1.18rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
        }

        .subject-title i {
            color: var(--primary-blue);
            opacity: 0.9;
        }

        .card-scrollable {
            overflow-y: auto;
            flex-grow: 1;
            padding-right: 0.35rem;
        }

        .card-scrollable::-webkit-scrollbar {
            width: 5px;
        }

        .card-scrollable::-webkit-scrollbar-track {
            background: transparent;
        }

        .card-scrollable::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 10px;
        }

        .syllabus-list {
            list-style: none;
            padding: 0.35rem 0.5rem 0.5rem;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.2rem;
        }

        .syllabus-item {
            padding: 0.35rem 0.5rem;
            border-radius: 6px;
            transition: background-color 0.15s ease;
            display: flex;
            align-items: center;
            gap: 0.55rem;
            cursor: pointer;
        }

        .syllabus-item:hover {
            background: #f8fafc;
        }

        .syllabus-checkbox {
            appearance: none;
            -webkit-appearance: none;
            width: 17px;
            height: 17px;
            border: 2px solid #cbd5e1;
            border-radius: 4px;
            outline: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
            background: #ffffff;
        }

        .syllabus-checkbox::before {
            content: "\\f00c";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            font-size: 0.65rem;
            color: #ffffff;
            display: none;
        }

        .syllabus-checkbox:checked {
            background: var(--primary-blue);
            border-color: var(--primary-blue);
        }

        .syllabus-checkbox:checked::before {
            display: block;
        }

        .syllabus-text {
            font-size: 0.86rem;
            color: var(--text-body);
            line-height: 1.45;
            cursor: pointer;
            transition: color 0.2s ease;
            user-select: none;
            flex-grow: 1;
        }

        .microtopic-link {
            color: inherit;
            text-decoration: none;
            transition: color 0.15s ease;
        }

        .microtopic-link:hover {
            color: var(--primary-blue);
            text-decoration: underline;
        }

        .syllabus-checkbox:checked + .syllabus-text .microtopic-link {
            color: #94a3b8;
            text-decoration: line-through;
        }

        /* Day Modules Accordion */
        details.syllabus-subsection {
            background: var(--bg-surface);
            border: 1px solid var(--border-color);
            border-radius: 9px;
            margin-bottom: 0.45rem;
            transition: all 0.2s ease;
            overflow: hidden;
        }

        details.syllabus-subsection:hover {
            border-color: #cbd5e1;
        }

        details.syllabus-subsection[open] {
            border-color: #93c5fd;
            box-shadow: 0 2px 8px rgba(37, 99, 235, 0.05);
        }

        summary.subsection-summary {
            padding: 0.6rem 0.85rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            list-style: none;
            user-select: none;
            gap: 0.5rem;
        }

        summary.subsection-summary::-webkit-details-marker {
            display: none;
        }

        .subsection-meta {
            display: flex;
            align-items: center;
            gap: 0.6rem;
        }

        .subsection-progress {
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.18rem 0.55rem;
            background: #f1f5f9;
            color: var(--text-light);
            border: 1px solid var(--border-color);
            border-radius: 999px;
            white-space: nowrap;
        }

        .subsection-progress.completed {
            background: #ecfdf5;
            color: #059669;
            border-color: #a7f3d0;
        }

        .toggle-icon {
            font-size: 0.75rem;
            color: var(--text-light);
            transition: transform 0.25s ease;
        }

        details.syllabus-subsection[open] .toggle-icon {
            transform: rotate(180deg);
            color: var(--primary-blue);
        }

        .subsection-title-link {
            font-size: 0.92rem;
            color: #1e3a8a;
            font-weight: 700;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: color 0.15s ease;
        }

        .subsection-title-link:hover {
            color: var(--primary-hover);
            text-decoration: underline;
        }

        .subsection-title-link i {
            font-size: 0.72rem;
            opacity: 0.7;
            transition: transform 0.15s ease;
        }

        .subsection-title-link:hover i {
            transform: translate(2px, -2px);
            opacity: 1;
            color: var(--primary-hover);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideUp {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @media (max-width: 768px) {
            .syllabus-container {
                padding: 1.25rem 0.75rem !important;
                margin: 0.5rem auto !important;
            }
            .syllabus-header {
                margin-bottom: 1.5rem !important;
            }
            .syllabus-tabs {
                justify-content: flex-start !important;
                border-radius: 12px !important;
                padding: 4px !important;
                margin-bottom: 1.25rem !important;
            }
            .tab-btn {
                padding: 0.45rem 0.85rem !important;
                font-size: 0.82rem !important;
            }
            .tracker-banner {
                flex-direction: column !important;
                align-items: stretch !important;
                gap: 0.85rem !important;
                padding: 1rem !important;
            }
            .tracker-progress-container {
                max-width: 100% !important;
                width: 100% !important;
                justify-content: space-between !important;
            }
            .progress-bar-wrapper {
                flex-grow: 1 !important;
            }
            .exam-plan-container {
                padding: 1rem !important;
            }
            .exam-plan-table th, .exam-plan-table td {
                padding: 8px 10px !important;
                font-size: 0.8rem !important;
            }
        }
    </style>`;

// Replace <style>...</style>
content = content.replace(/<style>[\s\S]*?<\/style>/, newStyle);

// 3. Clean up the table HTML
const oldTableRegex = /<table class="exam-plan-table"[\s\S]*?<\/table>/;
const newTable = `<table class="exam-plan-table">
<thead><tr>
<th>Phase</th>
<th style="text-align:center;">Days</th>
<th>Focus</th>
<th style="text-align:center;">Daily time</th>
</tr></thead><tbody>
<tr><td style="font-weight:700;color:#1e40af;">Phase 1</td><td style="text-align:center;">Days 1-20</td><td>Fluid Mechanics, Machinery and Heat Transfer</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 2</td><td style="text-align:center;">Days 21-40</td><td>Aeronautics, Aerodynamics, Performance and Stability</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 3</td><td style="text-align:center;">Days 41-55</td><td>Structures, Materials, Stress, Plates and Shells</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 4</td><td style="text-align:center;">Days 56-65</td><td>Propulsion</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 5</td><td style="text-align:center;">Days 66-80</td><td>Systems, Instrumentation and Maintenance</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 6</td><td style="text-align:center;">Days 81-88</td><td>Avionics, Navigation and Surveillance</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 7</td><td style="text-align:center;">Days 89-94</td><td>Industrial Aerodynamics, ATC, Aerodromes and Flight Planning</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 8</td><td style="text-align:center;">Days 95-97</td><td>Rules, Regulations, Safety and Human Factors</td><td style="text-align:center;">3-3.5h; 2-3h tests</td></tr>
<tr><td style="font-weight:700;color:#1e40af;">Phase 9</td><td style="text-align:center;">Days 98-100</td><td>PYQ, Mocks and Final Consolidation</td><td style="text-align:center;">3-4h mocks</td></tr>
</tbody></table>`;

content = content.replace(oldTableRegex, newTable);

fs.writeFileSync(indexPath, content, 'utf8');
console.log('Successfully updated upsc-aso/index.html UI & UX!');
