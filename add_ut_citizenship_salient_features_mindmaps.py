import os
import re
import json

BASE_DIR = r"upsc/polity/Union-Territory-Citizenship-Salient-Features"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Union Territory, Citizenship, and Salient Features
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. ARTICLES 1-4 & UNION TERRITORIES
    if 'article-1-4' in fl or 'union-and-its' in fl:
        return [
            {
                "label": "Part I of the Constitution\n(Articles 1 to 4)",
                "type": "branch",
                "date": "Union & Territory",
                "children": [
                    {
                        "label": "Territory & Admission", "type": "sub", "date": "Art 1 & 2", "children": [
                            {"label": "Art 1: India, that is Bharat, shall be a Union of States (rather than a Federation); defines territory of India into States, UTs, and Acquired territories", "type": "leaf"},
                            {"label": "Art 2: Vests power in Parliament to admit new states into the Union of India or establish new states on terms it thinks fit", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Alteration & Boundary", "type": "sub", "date": "Art 3 & 4", "children": [
                            {"label": "Art 3: Form new states, alter areas/boundaries/names of existing states; requires President's recommendation and state legislature view referral", "type": "leaf"},
                            {"label": "Art 4: Laws under Art 2 & 3 are not considered amendments under Art 368; can be passed by a simple majority", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. CITIZENSHIP ACT 1955 & AMENDMENTS
    elif 'citizenship-act-1955' in fl or 'citizenship-act-2016' in fl or 'amendment-act-2016' in fl:
        return [
            {
                "label": "Citizenship Act 1955",
                "type": "branch",
                "date": "Statutory Law",
                "children": [
                    {
                        "label": "Acquisition & Loss", "type": "sub", "date": "Provisions", "children": [
                            {"label": "Provides for acquisition of citizenship (birth, descent, registration, naturalization, incorporation) and loss (renunciation, termination, deprivation)", "type": "leaf"},
                            {"label": "Acts as the comprehensive post-1950 statutory code; has been amended in 1986, 1992, 2003, 2005, 2015, and 2019", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. CAA 2019
    elif 'citizenship-amendment-act-2019' in fl:
        return [
            {
                "label": "CAA 2019 Details",
                "type": "branch",
                "date": "2019 Amendment",
                "children": [
                    {
                        "label": "Key Clauses", "type": "sub", "date": "Amendments", "children": [
                            {"label": "Grants citizenship to illegal migrants of Hindu, sikh, Buddhist, Jain, Parsi, and Christian communities from Pakistan, Bangladesh, and Afghanistan", "type": "leaf"},
                            {"label": "Cut-off date: Entered India on or before December 31, 2014; reduces naturalization residency requirement from 11 to 5 years", "type": "leaf"},
                            {"label": "Exemptions: Scheduled Areas under 6th Schedule (Assam, Meghalaya, Tripura, Mizoram) and Inner Line Permit (ILP) states", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. CONSTITUTIONAL PROVISIONS OF CITIZENSHIP
    elif 'constitutional-provisions' in fl or 'provisions-of-citizenship' in fl:
        return [
            {
                "label": "Part II: Citizenship\n(Articles 5 to 11)",
                "type": "branch",
                "date": "Constitutional Core",
                "children": [
                    {
                        "label": "Core Articles", "type": "sub", "date": "Art 5-8", "children": [
                            {"label": "Art 5: Citizenship at commencement; Art 6: Migrants from Pakistan to India; Art 7: Migrants to Pakistan returning to India", "type": "leaf"},
                            {"label": "Art 8: Citizenship rights of persons of Indian origin residing outside India (diplomatic registration)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Termination & Power", "type": "sub", "date": "Art 9-11", "children": [
                            {"label": "Art 9: Voluntary acquisition of foreign citizenship automatically terminates Indian citizenship (no dual citizenship)", "type": "leaf"},
                            {"label": "Art 10: Continuance of citizenship rights subject to Parliamentary laws; Art 11: Vests absolute legislative power in Parliament", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. STATE REORGANIZATION COMMISSION
    elif 're-organization' in fl or 'reorganization' in fl:
        return [
            {
                "label": "State Reorganization",
                "type": "branch",
                "date": "Commissions",
                "children": [
                    {
                        "label": "Pre-1953 Panels", "type": "sub", "date": "Dhar & JVP", "children": [
                            {"label": "Dhar Commission (1948): Rejected linguistic reorganization; recommended reorganization based on administrative convenience", "type": "leaf"},
                            {"label": "JVP Committee (1948): Consisted of Nehru, Patel, and Sitaramayya; formally rejected language as the basis", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Fazl Ali Commission (1953)", "type": "sub", "date": "SRC 1953", "children": [
                            {"label": "Members: Fazl Ali, K.M. Panikkar, and H.N. Kunzru; accepted language as a major factor but rejected 'one language-one state' theory", "type": "leaf"},
                            {"label": "Led to State Reorganisation Act 1956, abolishing Part A, B, C, D classification and creating 14 states and 6 UTs", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. NRI, PIO, AND OCI
    elif 'comparison-between' in fl or 'non-resident' in fl or 'diaspora' in fl or 'pravasi' in fl:
        return [
            {
                "label": "Diaspora & NRIs",
                "type": "branch",
                "date": "Diaspora Profile",
                "children": [
                    {
                        "label": "NRI vs OCI", "type": "sub", "date": "Legal Status", "children": [
                            {"label": "NRI: Indian citizen living abroad (>182 days); holds Indian passport; enjoys full voting and political rights in India", "type": "leaf"},
                            {"label": "OCI Cardholder: Foreign citizen of Indian origin (except Pakistan/Bangladesh); lifelong visa-free travel; no voting/public office rights", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Diaspora Initiatives", "type": "sub", "date": "Engagements", "children": [
                            {"label": "Pravasi Bharatiya Divas (Jan 9) marks Gandhi's 1915 return from South Africa; MEA conventions to connect global diaspora", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. CONSTITUTION AND TYPES
    elif 'constitution-and-types' in fl:
        return [
            {
                "label": "Constitutional Types",
                "type": "branch",
                "date": "Comparative Polity",
                "children": [
                    {
                        "label": "Written vs Unwritten", "type": "sub", "date": "Codification", "children": [
                            {"label": "Written: Codified in a single document, supreme law, rigid/semi-rigid (e.g., USA, India)", "type": "leaf"},
                            {"label": "Unwritten: Evolved over time, parliamentary supremacy, flexible (e.g., UK)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Federal vs Unitary", "type": "sub", "date": "Divisions", "children": [
                            {"label": "Federal: Dual government, division of powers, independent judiciary (e.g., US); Unitary: Single central government (e.g., UK)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. DELIMITATION COMMISSION
    elif 'delimitation' in fl:
        return [
            {
                "label": "Delimitation Commission",
                "type": "branch",
                "date": "Article 82",
                "children": [
                    {
                        "label": "Mandate & Power", "type": "sub", "date": "Constituency Borders", "children": [
                            {"label": "Art 82: Parliament enacts Delimitation Act after census; Commission appointed by President in collaboration with Election Commission", "type": "leaf"},
                            {"label": "Decisions have the force of law and CANNOT be questioned in any court of law (protects election timelines)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. ACQUISITION OF CITIZENSHIP
    elif 'acquisition' in fl:
        return [
            {
                "label": "Acquisition Modes",
                "type": "branch",
                "date": "Citizenship Act 1955",
                "children": [
                    {
                        "label": "Five Methodologies", "type": "sub", "date": "Acquisition", "children": [
                            {"label": "By Birth (jus soli): Based on cut-off dates and parental citizenship status; By Descent (jus sanguinis): Born outside India", "type": "leaf"},
                            {"label": "By Registration: Resident 7 years, married to citizen; By Naturalization: Resident 12 years (11 years + last 12 months)", "type": "leaf"},
                            {"label": "By Incorporation of Territory: If a foreign territory becomes part of India (e.g., Pondicherry, Sikkim)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. LOSING CITIZENSHIP
    elif 'losing' in fl:
        return [
            {
                "label": "Loss of Citizenship",
                "type": "branch",
                "date": "Termination Modes",
                "children": [
                    {
                        "label": "Three Methods", "type": "sub", "date": "Loss", "children": [
                            {"label": "By Renunciation: Voluntary declaration (children lose citizenship but can resume it upon turning 18)", "type": "leaf"},
                            {"label": "By Termination: Automatic loss if an Indian citizen voluntarily acquires citizenship of another country (dual citizenship ban)", "type": "leaf"},
                            {"label": "By Deprivation: Compulsory termination by Central Govt on grounds of fraud, disloyalty to Constitution, or trade with enemy", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. SALIENT FEATURES OF INDIAN CONSTITUTION
    elif 'salient-features' in fl:
        return [
            {
                "label": "Constitutional Core",
                "type": "branch",
                "date": "Salient Features",
                "children": [
                    {
                        "label": "Key Features", "type": "sub", "date": "Structural", "children": [
                            {"label": "Lengthiest written constitution; drawn from various sources; blend of rigidity & flexibility; federal system with unitary bias", "type": "leaf"},
                            {"label": "Parliamentary form of government; synthesis of Parliamentary Sovereignty & Judicial Supremacy; single integrated judiciary", "type": "leaf"},
                            {"label": "Fundamental Rights, DPSP, Fundamental Duties; secular state; universal adult franchise; independent bodies (CAG, ECI, UPSC)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    raise Exception(f"Folder '{folder_name}' has no custom mindmap branch mapped!")

# Patching Logic
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
        # Fallback 1: notes-panel
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)
        else:
            # Fallback 2: notes-panel (with single quotes or slight variant)
            tab1_marker_alt = '<div class="tab-panel active" id="notes-panel" role="tabpanel">'
            if tab1_marker_alt in html:
                html = html.replace(tab1_marker_alt, tab1_marker_alt + '\n' + mindmap_card, 1)
            else:
                # Fallback 3: card-premium with deep-dive-section id
                div_marker = '<div class="card-premium" id="deep-dive-section">'
                if div_marker in html:
                    html = html.replace(div_marker, mindmap_card + '\n' + div_marker, 1)

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
