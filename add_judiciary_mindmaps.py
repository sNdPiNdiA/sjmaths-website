import os
import re
import json

BASE_DIR = r"upsc/polity/The-Judiciary-Supreme-Court-High-Court-Lok-Adalat"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'cji', 'njac', 'aijs', 'adr', 'nalsa', 'pil', 'njdg', 'lsa'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for the Judiciary
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. CJI, Acting, Ad-hoc, Retired Judges
    if 'chief-justice' in fl or 'ad-hoc' in fl or 'acting' in fl or 'judges-since' in fl:
        return [
            {
                "label": "Office & Leadership",
                "type": "branch",
                "date": "Master of Roster",
                "children": [
                    {
                        "label": "CJI Role", "type": "sub", "date": "Head of SC", "children": [
                            {"label": "Master of the Roster: Exclusive administrative power to allocate cases and constitute benches", "type": "leaf"},
                            {"label": "First among equals; acts as administrative head of the entire Supreme Court organization", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Acting & Ad-hoc Judges", "type": "sub", "date": "Art 126 & 127", "children": [
                            {"label": "Acting CJI: Appointed by President under Article 126 if CJI office is vacant or CJI is unable to perform duties", "type": "leaf"},
                            {"label": "Ad-hoc Judges: Appointed under Article 127 by CJI with prior consent of President and consultation with concerned HC Chief Justice", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Qualifications & Salaries of SC Judges
    elif 'qualifications' in fl or 'salaries' in fl:
        return [
            {
                "label": "SC Judge Status",
                "type": "branch",
                "date": "Qualifications",
                "children": [
                    {
                        "label": "Eligibility (Art 124(3))", "type": "sub", "date": "Criteria", "children": [
                            {"label": "Must be a citizen of India; High Court judge for 5 years, OR High Court advocate for 10 years", "type": "leaf"},
                            {"label": "OR a distinguished jurist in the opinion of the President (no such appointment made so far)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Financial Safeguards",
                "type": "branch",
                "date": "Salaries & Allowances",
                "children": [
                    {
                        "label": "Consolidated Fund", "type": "sub", "date": "Safeguards", "children": [
                            {"label": "Determined by Parliament; charged on the Consolidated Fund of India (non-votable); cannot be varied to disadvantage", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. Appointment & Collegium System
    elif 'appointment' in fl or 'collegium' in fl or 'concurrence' in fl:
        return [
            {
                "label": "Three Judges Cases",
                "type": "branch",
                "date": "Collegium Evolution",
                "children": [
                    {
                        "label": "Judges Cases Setup", "type": "sub", "date": "Cases 1-3", "children": [
                            {"label": "1st Judges Case (1981): Consultation does not mean concurrence; executive has ultimate say in judicial appointments", "type": "leaf"},
                            {"label": "2nd Judges Case (1993): Consultation means concurrence; Collegium formed (CJI + 2 senior-most judges)", "type": "leaf"},
                            {"label": "3rd Judges Case (1998): Expanded Collegium to CJI + 4 senior-most judges; opinion of collegium must be in writing", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "NJAC Conflict", "type": "sub", "date": "4th Judges Case", "children": [
                            {"label": "99th Amendment (NJAC) declared unconstitutional by SC in 2015 as violating judicial independence (4th Judges Case)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Removal & Impeachment
    elif 'removal' in fl or 'impeachment' in fl:
        return [
            {
                "label": "Removal Framework",
                "type": "branch",
                "date": "Article 124(4)",
                "children": [
                    {
                        "label": "Constitutional Grounds", "type": "sub", "date": "Grounds", "children": [
                            {"label": "Article 124(4): Removed ONLY by order of President on grounds of proved misbehavior or incapacity", "type": "leaf"},
                            {"label": "Requires special majority in both houses: Majority of total membership + 2/3rd members present and voting", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Impeachment Process",
                "type": "branch",
                "date": "Inquiry Act 1968",
                "children": [
                    {
                        "label": "Judges Inquiry Act", "type": "sub", "date": "Process", "children": [
                            {"label": "Motion signed by 100 LS or 50 RS members; Speaker/Chairman can admit/refuse; 3-member committee investigates charges", "type": "leaf"},
                            {"label": "No Supreme Court judge has been impeached so far (V. Ramaswami & Soumitra Sen motions did not complete)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. Jurisdiction of Supreme Court
    elif 'jurisdiction' in fl and 'supreme' in fl:
        return [
            {
                "label": "Constitutional Powers",
                "type": "branch",
                "date": "SC Power Scope",
                "children": [
                    {
                        "label": "Original & Writ", "type": "sub", "date": "Art 131 & 32", "children": [
                            {"label": "Original (Art 131): Exclusive jurisdiction in federal disputes (Union vs States, State vs State)", "type": "leaf"},
                            {"label": "Writ (Art 32): Enforcement of Fundamental Rights; SC can issue Habeas Corpus, Mandamus, etc.", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Appellate & Advisory", "type": "sub", "date": "Art 132 & 143", "children": [
                            {"label": "Appellate (Art 132-134): Constitutional, civil, and criminal appeals; Special Leave Petition (Art 136)", "type": "leaf"},
                            {"label": "Advisory (Art 143): President can seek SC opinion on questions of law/fact; opinion not binding on President", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. High Courts & Jurisdictions
    elif 'high-court' in fl:
        return [
            {
                "label": "HC Constitution",
                "type": "branch",
                "date": "State Judiciary",
                "children": [
                    {
                        "label": "Appointment & Tenure", "type": "sub", "date": "HC Judges", "children": [
                            {"label": "Appointed by President (consults CJI, Governor, HC Chief Justice); retires at age 62; removed like an SC Judge", "type": "leaf"},
                            {"label": "Writ Jurisdiction (Art 226): Broader than SC; can issue writs for both FRs and ordinary legal rights", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "HC Superintendence", "type": "sub", "date": "Article 227", "children": [
                            {"label": "Article 227: Power of superintendence over all courts and tribunals within its territorial jurisdiction", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. Subordinate Courts & AIJS
    elif 'subordinate' in fl or 'judicial-service' in fl:
        return [
            {
                "label": "Subordinate Judiciary",
                "type": "branch",
                "date": "District Courts",
                "children": [
                    {
                        "label": "Subordinate Structure", "type": "sub", "date": "Structure", "children": [
                            {"label": "District Judge: Highest judicial authority in district; appointed by Governor in consultation with High Court", "type": "leaf"},
                            {"label": "Separation of powers: Civil side (District Judge) vs Criminal side (Sessions Judge)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "AIJS (Article 312)", "type": "sub", "date": "Proposed Services", "children": [
                            {"label": "Proposed All-India Judicial Service; requires Rajya Sabha 2/3rd resolution; aimed at centralizing district judge recruitment", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. ADR, Lok Adalat, NALSA, Gram Nyayalayas
    elif 'alternative-dispute' in fl or 'lok-adalat' in fl or 'nalsa' in fl or 'gram-nyayalayas' in fl:
        return [
            {
                "label": "Alternative Dispute Resolution",
                "type": "branch",
                "date": "ADR Tiers",
                "children": [
                    {
                        "label": "ADR & Lok Adalat", "type": "sub", "date": "ADR Systems", "children": [
                            {"label": "ADR: Includes Arbitration, Mediation, Conciliation, and Lok Adalats to reduce huge court pendency", "type": "leaf"},
                            {"label": "Lok Adalat: Statutory status under LSA Act 1987; award has force of a civil court decree; final and non-appealable", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "NALSA & Gram Nyayalayas", "type": "sub", "date": "Legal Aid", "children": [
                            {"label": "NALSA: Article 39A compliance; provides free legal aid to vulnerable sections; chaired by 2nd senior-most SC Judge", "type": "leaf"},
                            {"label": "Gram Nyayalayas Act 2008: Mobile village courts; presided over by Nyayadhikari (appointed by State in consultation with HC)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. PIL
    elif 'pil' in fl or 'public-interest' in fl:
        return [
            {
                "label": "PIL Genesis",
                "type": "branch",
                "date": "PIL Setup",
                "children": [
                    {
                        "label": "Locus Standi Shift", "type": "sub", "date": "Locus Standi", "children": [
                            {"label": "Locus Standi relaxed: Any public-spirited citizen can approach court on behalf of marginalized sections", "type": "leaf"},
                            {"label": "Introduced by Justice P.N. Bhagwati & Justice V.R. Krishna Iyer in early 1980s (S.P. Gupta case)", "type": "leaf"},
                            {"label": "Epistolary jurisdiction: Court can treat a simple postcard or letter as a writ petition", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. Judicial Review, Independence, Activism, Relations
    elif 'independence' in fl or 'activism' in fl or 'relations' in fl or 'bill-2010' in fl or 'assessment' in fl or 'difference' in fl:
        return [
            {
                "label": "Independence & Activism",
                "type": "branch",
                "date": "Judicial Dynamics",
                "children": [
                    {
                        "label": "Independence Safeguards", "type": "sub", "date": "Safeguards", "children": [
                            {"label": "Security of tenure, expenses charged on Consolidated Fund, ban on practice post-retirement, power to punish for contempt", "type": "leaf"},
                            {"label": "Judicial Review vs Activism: Review checks constitutionality; Activism involves proactive judicial policy-making (e.g., green benches)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Executive Clash", "type": "sub", "date": "Overreach", "children": [
                            {"label": "Judicial Overreach: When judiciary encroaches upon executive or legislative domains, violating separation of powers", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. E-governance in Judiciary
    elif 'e-governance' in fl:
        return [
            {
                "label": "Digital Platforms",
                "type": "branch",
                "date": "Technology",
                "children": [
                    {
                        "label": "e-Courts Project", "type": "sub", "date": "e-Courts", "children": [
                            {"label": "e-Courts Mission Mode Project: Managed by Department of Justice & SC e-Committee; aims to digitize court records", "type": "leaf"},
                            {"label": "NJDG (National Judicial Data Grid): Real-time portal tracking pendency of civil and criminal cases across India", "type": "leaf"},
                            {"label": "Virtual Courts: Online traffic challans; e-filing portals, live streaming of constitutional bench hearings", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # --- GENERAL FALLBACK (Highly detailed 3-Tier Structure) ---

# Patching Logic


    raise Exception(f"Folder '{folder_name}' has no custom mindmap branch mapped!")

def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates (using ?v=3 to force cache bypass)
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->
'''
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script with ?v=3 to force reload of wrapping logic
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=3"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Successfully patched: {filepath}")
    return True

# Main execution
def main():
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])
    print(f"Found {len(folders)} topics to process.")
    
    for idx, folder in enumerate(folders):
        folder_path = os.path.join(BASE_DIR, folder)
        html_path = os.path.join(folder_path, 'index.html')
        content_path = os.path.join(folder_path, 'content.json')
        
        if not os.path.exists(html_path):
            print(f"[{idx+1}/{len(folders)}] Skipping {folder} (index.html not found)")
            continue
            
        topic_name = get_clean_title(folder)
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        # Build custom, 3-tier deep-dive topic-specific mindmap data
        branches = get_custom_branches(folder)
        mindmap_data = {
            "label": get_clean_title(folder),
            "type": "root",
            "children": branches
        }
        
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()

def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates (using ?v=3 to force cache bypass)
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->
'''
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script with ?v=3 to force reload of wrapping logic
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=3"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Successfully patched: {filepath}")
    return True

# Main execution
def main():
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])
    print(f"Found {len(folders)} topics to process.")
    
    for idx, folder in enumerate(folders):
        folder_path = os.path.join(BASE_DIR, folder)
        html_path = os.path.join(folder_path, 'index.html')
        content_path = os.path.join(folder_path, 'content.json')
        
        if not os.path.exists(html_path):
            print(f"[{idx+1}/{len(folders)}] Skipping {folder} (index.html not found)")
            continue
            
        topic_name = get_clean_title(folder)
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        # Build custom, 3-tier deep-dive topic-specific mindmap data
        branches = get_custom_branches(folder)
        mindmap_data = {
            "label": get_clean_title(folder),
            "type": "root",
            "children": branches
        }
        
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()

