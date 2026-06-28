import os
import re
import json

BASE_DIR = r"upsc/polity/Political-Dynamics"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'rpa', 'ls', 'la', 'adr', 'evm', 'vvpat', 'ficci', 'assocham', 'aituc', 'intuc', 'bku', 'abvp', 'nsui', 'ima', 'bci', 'rss', 'vhp'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Political Dynamics
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. Party System & Elections
    if 'party-system' in fl or 'parties-and-election' in fl:
        return [
            {
                "label": "Electoral Criteria",
                "type": "branch",
                "date": "ECI Guidelines",
                "children": [
                    {
                        "label": "National Party Status", "type": "sub", "date": "National Criteria", "children": [
                            {"label": "Must win 2% seats in LS from 3 different states; OR poll 6% votes in 4+ states in LS/LA + win 4 LS seats", "type": "leaf"},
                            {"label": "OR recognized as a State Party in at least 4 states; grants common symbol and free airtime on state media", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "State Party Status", "type": "sub", "date": "State Criteria", "children": [
                            {"label": "Must poll 6% votes in State LA + win 2 seats; OR poll 6% votes in State LS + win 1 seat", "type": "leaf"},
                            {"label": "OR win 3% of total seats in state LA (min 3 seats); OR win 1 out of 25 LS seats allotted to state", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Indian Party Phases",
                "type": "branch",
                "date": "Evolution",
                "children": [
                    {
                        "label": "Dominance vs Coalition", "type": "sub", "date": "Phases", "children": [
                            {"label": "Congress System (Rajni Kothari): One-party dominance from 1952-1967; factionalism within Congress served as opposition", "type": "leaf"},
                            {"label": "Coalition Era: Multi-party coalitions from 1989 (National Front) to 2014; rise of regional identity-based parties", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Anti-Defection / 10th Schedule
    elif '10th-schedule' in fl or 'defection' in fl:
        return [
            {
                "label": "Anti-Defection Law",
                "type": "branch",
                "date": "10th Schedule",
                "children": [
                    {
                        "label": "52nd & 91st Amendments", "type": "sub", "date": "Constitutional", "children": [
                            {"label": "52nd Amendment (1985) added 10th Schedule to curb political defection (Aya Ram Gaya Ram culture)", "type": "leaf"},
                            {"label": "91st Amendment (2003) deleted split exemption (1/3rd split); requires 2/3rd merger to escape defection", "type": "leaf"},
                            {"label": "Limits Union/State Council of Ministers to 15% of total house strength (min 12 for states) to check ministerial baits", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Deciding Authority", "type": "sub", "date": "Speaker Power", "children": [
                            {"label": "Deciding authority is Speaker/Chairman; Kihoto Hollohan (1992) case made Speaker's decision subject to judicial review", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. RPA 1951, Criminalization, & State Funding
    elif 'representation' in fl or 'rpa' in fl or 'criminalization' in fl or 'funding' in fl:
        return [
            {
                "label": "RPA 1951 Features",
                "type": "branch",
                "date": "Syllabus Core",
                "children": [
                    {
                        "label": "Conduct & Disqualifications", "type": "sub", "date": "RPA 1951", "children": [
                            {"label": "Section 8: Disqualification of candidate on conviction for specific offenses (including Section 8(4) struck down)", "type": "leaf"},
                            {"label": "Section 8(3): Person convicted of any offense and sentenced to 2+ years is disqualified for 6 years post-release", "type": "leaf"},
                            {"label": "Lily Thomas Case (2013): Struck down Section 8(4); sitting MPs/MLAs disqualified immediately upon conviction", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Criminalization & Funding",
                "type": "branch",
                "date": "Electoral Clean-up",
                "children": [
                    {
                        "label": "Clean-up Interventions", "type": "sub", "date": "Reforms", "children": [
                            {"label": "Association for Democratic Reforms (ADR) case: Mandatory declaration of assets, liabilities, and criminal antecedents", "type": "leaf"},
                            {"label": "State Funding: Indrajit Gupta Committee recommended partial state funding (in kind, not cash) to level the field", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Pressure Groups
    elif 'pressure-group' in fl or 'pressure-groups' in fl:
        return [
            {
                "label": "Typology & Methods",
                "type": "branch",
                "date": "Pressure Groups",
                "children": [
                    {
                        "label": "Types of Groups", "type": "sub", "date": "Types", "children": [
                            {"label": "Business (FICCI, ASSOCHAM); Trade Unions (AITUC, INTUC); Agrarian (BKU, All India Kisan Sabha); Student (ABVP, NSUI)", "type": "leaf"},
                            {"label": "Professional (IMA, BCI); Caste/Religious (RSS, VHP, caste associations); tribal organizations", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Techniques & Lobbying", "type": "sub", "date": "Methods", "children": [
                            {"label": "Lobbying, petitioning, public debate, media campaigns, strikes (bandhs), civil disobedience, and litigation", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Role & Criticisms",
                "type": "branch",
                "date": "Applied Review",
                "children": [
                    {
                        "label": "Governance Value", "type": "sub", "date": "Participation", "children": [
                            {"label": "Acts as link between government and citizens; fosters participatory democracy; aggregates minority interests", "type": "leaf"},
                            {"label": "Criticisms: Promoting narrow sectional interests at cost of national interest; foreign funding subversion; violent protests", "type": "leaf"}
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

