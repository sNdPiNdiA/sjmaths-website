import os
import re
import json

BASE_DIR = r"upsc/polity/State-Executive-State-Legislature"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'pri', 'pesa', 'ncrwc', 'com', 'mlas', 'mps', 'obcs'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'over']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for State Executive & Legislature
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. Governor & Powers
    if 'governor' in fl or 'state-executive' in fl:
        return [
            {
                "label": "Office & Dual Role",
                "type": "branch",
                "date": "Article 153-156",
                "children": [
                    {
                        "label": "Constitutional Office", "type": "sub", "date": "Dual Role", "children": [
                            {"label": "Appointed by President (Art 155); holds office during pleasure of President (Art 156, doctrine of pleasure)", "type": "leaf"},
                            {"label": "Dual role: Constitutional head of State & vital agent of the Central Government in the state", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Discretionary Powers", "type": "sub", "date": "Art 163 Discretion", "children": [
                            {"label": "Constitutional (Art 163): Reserving a bill for President (Art 200); recommending President's Rule (Art 356)", "type": "leaf"},
                            {"label": "Situational: Appointing CM when no party has clear majority; dismissing CoM if it loses confidence of Assembly", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Legislative & Judicial",
                "type": "branch",
                "date": "Powers",
                "children": [
                    {
                        "label": "Veto & Pardon", "type": "sub", "date": "Art 200 & 161", "children": [
                            {"label": "Art 200: Veto powers over bills (gives assent, withholds assent, returns bill, or reserves for President)", "type": "leaf"},
                            {"label": "Art 161: Pardoning powers (pardon, reprieve, respite, remit); cannot pardon death sentences (only President can)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Chief Minister & Council of Ministers
    elif 'chief-minister' in fl or 'com' in fl or 'ministers' in fl or 'cmcom' in fl:
        return [
            {
                "label": "CM Appointment & Roles",
                "type": "branch",
                "date": "Article 164",
                "children": [
                    {
                        "label": "Head of Government", "type": "sub", "date": "CM Profile", "children": [
                            {"label": "Appointed by Governor (Art 164); serves as principal channel of communication between Governor and CoM (Art 167)", "type": "leaf"},
                            {"label": "Chairs Cabinet meetings, advises Governor on minister appointments, and allocates portfolios", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Ministerial Responsibilities",
                "type": "branch",
                "date": "Accountability",
                "children": [
                    {
                        "label": "Collective & Individual", "type": "sub", "date": "Responsibilities", "children": [
                            {"label": "Collective (Art 164): Council of Ministers is collectively responsible to the Legislative Assembly of the State", "type": "leaf"},
                            {"label": "Individual: Ministers hold office during pleasure of the Governor (dismissed only on advice of CM)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. State Legislature / Assembly / Council / Speaker
    elif 'legislature' in fl or 'assembly' in fl or 'council' in fl or 'speaker' in fl:
        return [
            {
                "label": "Unicameral vs Bicameral",
                "type": "branch",
                "date": "Structure",
                "children": [
                    {
                        "label": "Assembly (Vidhan Sabha)", "type": "sub", "date": "Assembly", "children": [
                            {"label": "Direct elections; pop strength 60 to 500 (exceptions like Sikkim 32, Goa 40); Speaker holds administrative control", "type": "leaf"},
                            {"label": "Money Bills (Art 207) originate only in Assembly; Rajya Sabha equivalent (Legislative Council) has only delaying power", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Council (Vidhan Parishad)", "type": "sub", "date": "Article 169", "children": [
                            {"label": "Art 169: Parliament can create or abolish Legislative Council if Assembly passes resolution by special majority", "type": "leaf"},
                            {"label": "Indirect election: 1/3 elected by local bodies, 1/3 by MLAs, 1/12 by graduates, 1/12 by teachers, 1/6 nominated by Governor", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Commissions (Sarkaria, Punchhi, ARC)
    elif 'sarkaria' in fl or 'arc' in fl or 'commission' in fl or 'recommendations' in fl:
        return [
            {
                "label": "Governor Office Reforms",
                "type": "branch",
                "date": "Commissions",
                "children": [
                    {
                        "label": "Sarkaria & Punchhi", "type": "sub", "date": "Panels", "children": [
                            {"label": "Sarkaria Commission (1983): Governor should be an eminent person outside the state; not active in politics recently", "type": "leaf"},
                            {"label": "Punchhi Commission (2007): Proposed fixed 5-year term for Governor; removal should match President's impeachment process", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "NCRWC & Selection", "type": "sub", "date": "Selection Panels", "children": [
                            {"label": "NCRWC: Recommended selection of Governor by panel of PM, HM, Speaker, and State CM to check central bias", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. Advocate General
    elif 'advocate-general' in fl:
        return [
            {
                "label": "State Law Officer",
                "type": "branch",
                "date": "Article 165",
                "children": [
                    {
                        "label": "Appointment & Role", "type": "sub", "date": "Advocate General", "children": [
                            {"label": "Appointed by Governor; qualified to be High Court judge; holds office during pleasure of Governor (no fixed tenure)", "type": "leaf"},
                            {"label": "Right to speak and take part in proceedings of State Legislature & committees; enjoys MLA privileges (no voting rights)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. Parliament Control
    elif 'control' in fl:
        return [
            {
                "label": "Parliamentary Control",
                "type": "branch",
                "date": "Federal Balance",
                "children": [
                    {
                        "label": "Legislative Supremacy", "type": "sub", "date": "Articles", "children": [
                            {"label": "Art 249: Parliament can legislate on state list in national interest if Rajya Sabha passes 2/3rd resolution", "type": "leaf"},
                            {"label": "Art 250: Parliament acquires power to legislate on any state subject during National Emergency", "type": "leaf"},
                            {"label": "Art 252: Parliament can legislate on state list for 2+ states if their assemblies pass resolutions requesting it", "type": "leaf"}
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

