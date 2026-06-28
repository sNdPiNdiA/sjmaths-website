import os
import re
import json

BASE_DIR = r"upsc/polity/Union-Executive-Legislature-Parliament"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'pri', 'pesa', 'ncrwc', 'gst', 'adcs', 'amtm', 'cji', 'njac', 'aijs', 'adr', 'nalsa', 'pil', 'njdg', 'lsa', 'cec', 'ecs', 'spr', 'apmc', 'zbnf', 'pkvy', 'pmksy', 'fbr', 'phwr', 'ahwr', 'isa', 'ppp', 'pmgsy', 'ls', 'rs', 'vp', 'coom', 'com'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'over', 'between', 'respect', 'under']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Union Executive & Parliament
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. President
    if 'president' in fl and 'vice' not in fl and 'parliament' not in fl:
        return [
            {
                "label": "Election & Impeachment",
                "type": "branch",
                "date": "Article 54 & 61",
                "children": [
                    {
                        "label": "Electoral College", "type": "sub", "date": "Elections", "children": [
                            {"label": "Elected by: Elected members of LS, RS, and State Legislative Assemblies (including Delhi, Puducherry, & JK)", "type": "leaf"},
                            {"label": "Impeachment (Art 61): Ground is 'violation of the Constitution'; initiated in either house by 1/4th members; passed by 2/3rd total membership majority", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Executive & Judicial",
                "type": "branch",
                "date": "Powers",
                "children": [
                    {
                        "label": "Ordinance & Pardon", "type": "sub", "date": "Art 123 & 72", "children": [
                            {"label": "Art 123: Promulgates ordinances when Parliament is in recess; co-extensive with legislative power; maximum life 6 months & 6 weeks", "type": "leaf"},
                            {"label": "Art 72: Pardoning power (pardon, commutation, remission, respite, reprieve); covers court-martial & death sentences", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Prime Minister & CoM
    elif 'prime-minister' in fl or 'council-of-minister' in fl or 'council-of-ministers' in fl:
        return [
            {
                "label": "PM Appointment & Roles",
                "type": "branch",
                "date": "Article 74-75",
                "children": [
                    {
                        "label": "Head of Government", "type": "sub", "date": "PM & Cabinet", "children": [
                            {"label": "Appointed by President (Art 75); serves as principal channel of communication between President and Cabinet (Art 78)", "type": "leaf"},
                            {"label": "91st CA (2003): CoM strength shall not exceed 15% of total Lok Sabha strength (inclusive of PM)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Cabinet Responsibilities",
                "type": "branch",
                "date": "Article 75(3)",
                "children": [
                    {
                        "label": "Collective & Individual", "type": "sub", "date": "Accountability", "children": [
                            {"label": "Collective (Art 75(3)): Council of Ministers is collectively responsible to the Lok Sabha", "type": "leaf"},
                            {"label": "Individual: Ministers hold office during pleasure of the President (dismissed only on PM's advice)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. Vice President
    elif 'vice-president' in fl:
        return [
            {
                "label": "Election & Removal",
                "type": "branch",
                "date": "Article 66",
                "children": [
                    {
                        "label": "VP Electoral College", "type": "sub", "date": "Elections", "children": [
                            {"label": "Electoral College (Art 66): Consists of ALL members of Parliament (both elected & nominated); State Assemblies have no role", "type": "leaf"},
                            {"label": "Removal: Resolution passed by Rajya Sabha by effective majority and agreed to by Lok Sabha by simple majority", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Ex-Officio Role", "type": "sub", "date": "Art 64", "children": [
                            {"label": "Ex-officio Chairman of Rajya Sabha (Art 64); receives salary of Chairman, not VP; acts as President for max 6 months during vacancy", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Presiding Officers (Speaker, Deputy Speaker, Chairman, Vice-Chairpersons)
    elif 'speaker' in fl or 'chairman' in fl or 'deputy' in fl or 'presiding' in fl:
        return [
            {
                "label": "Speaker of Lok Sabha",
                "type": "branch",
                "date": "Lok Sabha",
                "children": [
                    {
                        "label": "Powers & Functions", "type": "sub", "date": "Art 110 & 108", "children": [
                            {"label": "Decides whether a bill is a Money Bill (Art 110, decision final); presides over joint sittings of Parliament (Art 108)", "type": "leaf"},
                            {"label": "Declares members disqualified under 10th Schedule; does not vote in first instance, votes only in case of equality (casting vote)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Speaker Pro Tem", "type": "sub", "date": "Oath Duty", "children": [
                            {"label": "Appointed by President to administer oath to new members and preside over Speaker election; usually senior-most member", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Rajya Sabha Chairman",
                "type": "branch",
                "date": "Rajya Sabha",
                "children": [
                    {
                        "label": "Chairman & Deputy", "type": "sub", "date": "Presiding Officers", "children": [
                            {"label": "Chairman is Vice-President; not a member of Rajya Sabha; has casting vote; Deputy Chairman elected from members of RS", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. Parliament Structure & Membership
    elif 'composition' in fl or 'organisation' in fl or 'membership' in fl or 'houses-of' in fl or 'parliament-' in fl:
        return [
            {
                "label": "Composition of Houses",
                "type": "branch",
                "date": "Structure",
                "children": [
                    {
                        "label": "Lok Sabha vs Rajya Sabha", "type": "sub", "date": "Houses", "children": [
                            {"label": "LS (Lower House): Max strength 550 (originally 552, Anglo-Indian nominated seats abolished by 104th CA 2019)", "type": "leaf"},
                            {"label": "RS (Upper House): Max strength 250 (238 representing States/UTs, 12 nominated by President from Art/Science/Literature)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Membership Rules", "type": "sub", "date": "Disqualifications", "children": [
                            {"label": "Art 101: Disqualification on double membership; Art 102: Office of Profit, unsound mind, undischarged insolvent", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. Special Powers of Rajya Sabha
    elif 'special-power' in fl or 'position-of-rajya' in fl:
        return [
            {
                "label": "Rajya Sabha Status",
                "type": "branch",
                "date": "Syllabus Core",
                "children": [
                    {
                        "label": "Exclusive Clauses", "type": "sub", "date": "Art 312 & 249", "children": [
                            {"label": "Art 312: Pass resolution by 2/3rd majority to create a new All-India Service; Art 249: pass resolution on State List", "type": "leaf"},
                            {"label": "Art 67: Initiating Vice-President's removal resolution (exclusive starting house)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Inequality with LS", "type": "sub", "date": "Limitations", "children": [
                            {"label": "No power over Money Bills (RS can delay Money Bill for max 14 days; cannot reject/amend it); no vote on demand for grants", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. Parliamentary Privileges (Art 105)
    elif 'privileges' in fl or 'immunities' in fl:
        return [
            {
                "label": "Individual Privileges",
                "type": "branch",
                "date": "Article 105",
                "children": [
                    {
                        "label": "Personal Protections", "type": "sub", "date": "Individual", "children": [
                            {"label": "Freedom of speech in Parliament (not liable to any court proceedings for anything said or voted in house)", "type": "leaf"},
                            {"label": "Freedom from arrest: Cannot be arrested in civil cases during session & 40 days before/after (no immunity in criminal cases)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Collective Privileges",
                "type": "branch",
                "date": "House Powers",
                "children": [
                    {
                        "label": "House Powers", "type": "sub", "date": "Collective", "children": [
                            {"label": "Right to publish debates or exclude strangers; power to punish for contempt or breach of privilege (includes outsiders)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. Sessions & Devices
    elif 'sessions' in fl or 'devices' in fl or 'functioning' in fl or 'functions-of' in fl or 'role-and' in fl or 'sovereignty' in fl or 'secretariat' in fl or 'procedure' in fl or 'funds' in fl:
        return [
            {
                "label": "Sessions & Quorum",
                "type": "branch",
                "date": "Article 85",
                "children": [
                    {
                        "label": "Terminologies", "type": "sub", "date": "Sessions", "children": [
                            {"label": "Summoning, Prorogation (ends session, done by President), Adjournment (suspends sitting, done by Presiding Officer)", "type": "leaf"},
                            {"label": "Quorum: 1/10th of total membership of the house required to transact business (inclusive of Presiding Officer)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Devices of Proceedings", "type": "sub", "date": "Devices", "children": [
                            {"label": "Question Hour (first hour of sitting, starred/unstarred/short notice); Zero Hour (starts immediately after Question Hour)", "type": "leaf"},
                            {"label": "Motions: Closure motion, No-Confidence motion (needs 50 supporters, Lok Sabha only), Adjournment motion (censure)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Funds (Art 266-267)",
                "type": "branch",
                "date": "State Funds",
                "children": [
                    {
                        "label": "Union Funds Comparison", "type": "sub", "date": "Funds", "children": [
                            {"label": "Consolidated Fund (Art 266(1), needs Parliament law to withdraw); Contingency Fund (Art 267, under President's control)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. Panel of Chairpersons / Vice-Chairpersons
    elif 'panel-of' in fl:
        return [
            {
                "label": "Presiding Panels",
                "type": "branch",
                "date": "House Rules",
                "children": [
                    {
                        "label": "Lok Sabha & Rajya Sabha Panels", "type": "sub", "date": "Absent Presiding", "children": [
                            {"label": "Speaker/Chairman nominates a panel of not more than 10 chairpersons from amongst members of the House", "type": "leaf"},
                            {"label": "Any member of the panel can preside over the House when the Speaker/Chairman or Deputy Speaker/Deputy Chairman is ABSENT", "type": "leaf"},
                            {"label": "If the offices are vacant, the panel CANNOT preside; President appoints a member of the House for vacancy duties", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. Role of Bureaucracy
    elif 'role-of-bureaucracy' in fl:
        return [
            {
                "label": "Union Bureaucracy",
                "type": "branch",
                "date": "Civil Services",
                "children": [
                    {
                        "label": "Permanent Executive", "type": "sub", "date": "Administration", "children": [
                            {"label": "Cabinet Secretary: Highest civil servant of the Union; ex-officio chairman of the Civil Services Board", "type": "leaf"},
                            {"label": "Role: Politically neutral, professional administrators implementing cabinet policies and running secretariats", "type": "leaf"}
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

