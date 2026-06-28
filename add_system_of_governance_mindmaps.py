import os
import re
import json

BASE_DIR = r"upsc/polity/System-of-Governance-Emergency-Provisions"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'pri', 'pesa', 'ncrwc', 'gst', 'adcs', 'amtm'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'over', 'some']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for System of Governance
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. Legislative Relations & Territorial Powers
    if 'legislative-relations' in fl or 'territorial' in fl:
        return [
            {
                "label": "Territorial & Lists",
                "type": "branch",
                "date": "Article 245-248",
                "children": [
                    {
                        "label": "Territorial Jurisdiction", "type": "sub", "date": "Jurisdiction", "children": [
                            {"label": "Parliament can make laws for whole/part of India; extra-territorial legislation power lies solely with Parliament", "type": "leaf"},
                            {"label": "State Legislature can make laws only for whole or part of respective state (territorial nexus rule)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Distribution of Lists", "type": "sub", "date": "7th Schedule", "children": [
                            {"label": "7th Schedule: Union List (100 items), State List (61 items), Concurrent List (52 items); Residuary powers with Union (Art 248)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Union Entry on State List",
                "type": "branch",
                "date": "Articles 249-252",
                "children": [
                    {
                        "label": "Extraordinary Situations", "type": "sub", "date": "Supremacy", "children": [
                            {"label": "Art 249: Legislative authority in national interest; Art 250: during Emergency; Art 252: request by 2+ states", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Administrative Relations
    elif 'administrative-relations' in fl:
        return [
            {
                "label": "Executive Directions",
                "type": "branch",
                "date": "Article 256-257",
                "children": [
                    {
                        "label": "Union Supremacy", "type": "sub", "date": "Directions", "children": [
                            {"label": "Art 256: State executive power must ensure compliance with Parliamentary laws; Art 257: Union directions to states", "type": "leaf"},
                            {"label": "Art 365: Non-compliance with Union administrative directions is ground for invoking President's Rule under Art 356", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Delegation of Powers", "type": "sub", "date": "Art 258 & 258A", "children": [
                            {"label": "Art 258: President can delegate Union executive functions to states; Art 258A: Governor can delegate state functions to Union", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. Financial Relations
    elif 'financial-relations' in fl:
        return [
            {
                "label": "Distribution of Revenues",
                "type": "branch",
                "date": "Article 268-281",
                "children": [
                    {
                        "label": "Tax Devolution & Grants", "type": "sub", "date": "Fiscal Devolution", "children": [
                            {"label": "Art 268: Taxes levied by Union but collected/appropriated by states (stamp duties); GST Council (Art 279A)", "type": "leaf"},
                            {"label": "Art 275: Grants-in-aid from Consolidated Fund of India to needy states recommended by Finance Commission", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Borrowing Powers",
                "type": "branch",
                "date": "Article 292-293",
                "children": [
                    {
                        "label": "Fiscal Boundaries", "type": "sub", "date": "Borrowing", "children": [
                            {"label": "Art 292: Union has unlimited borrowing power (within/outside India); Art 293: State can only borrow within India", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Emergencies (National, State, Financial)
    elif 'emergency' in fl or 'emergencies' in fl:
        return [
            {
                "label": "National Emergency (Art 352)",
                "type": "branch",
                "date": "Article 352",
                "children": [
                    {
                        "label": "Declaration & Effects", "type": "sub", "date": "NE Details", "children": [
                            {"label": "Grounds: War, external aggression, OR armed rebellion (replaced 'internal disturbance' by 44th CA 1978)", "type": "leaf"},
                            {"label": "Requires written cabinet advice; approved by both houses in 1 month by special majority; extends 6 months at a time", "type": "leaf"},
                            {"label": "Effect (Art 358 & 359): Art 19 freedoms suspended under Art 358; right to move court suspended under Art 359 (except Art 20 & 21)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "President's Rule (Art 356)",
                "type": "branch",
                "date": "Article 356",
                "children": [
                    {
                        "label": "State Machinery Collapse", "type": "sub", "date": "PR Details", "children": [
                            {"label": "Grounds: Failure of constitutional machinery (Art 356) OR non-compliance with central directions (Art 365)", "type": "leaf"},
                            {"label": "Approved by both houses in 2 months by simple majority; maximum limit of 3 years (reviewed every 6 months)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Financial Emergency (Art 360)",
                "type": "branch",
                "date": "Article 360",
                "children": [
                    {
                        "label": "Fiscal Crisis", "type": "sub", "date": "FE Details", "children": [
                            {"label": "Declared by President if financial stability or credit of India is threatened; simple majority approval; no max time limit", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. Inter-State Relations / Councils / Zonal / Water Disputes
    elif 'inter-state' in fl or 'interstate' in fl or 'zonal' in fl:
        return [
            {
                "label": "Water & Councils",
                "type": "branch",
                "date": "Inter-State Relations",
                "children": [
                    {
                        "label": "Water Disputes (Art 262)", "type": "sub", "date": "Water Disputes", "children": [
                            {"label": "Parliament can legislate on inter-state river valley disputes; excludes jurisdiction of Supreme Court", "type": "leaf"},
                            {"label": "Inter-State River Water Disputes Act 1956 provides for ad-hoc tribunals (Cauvery, Krishna tribunals)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Inter-State Council (Art 263)", "type": "sub", "date": "Article 263", "children": [
                            {"label": "Constitutional body appointed by President; recommended by Sarkaria Commission; chaired by PM; CMs are members", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Zonal Councils",
                "type": "branch",
                "date": "Statutory Zones",
                "children": [
                    {
                        "label": "Statutory Setup", "type": "sub", "date": "Zonal Councils", "children": [
                            {"label": "Statutory bodies established under States Reorganisation Act 1956; 5 zones; chaired by Union Home Minister", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. Special Provisions for some States / National Integration Council
    elif 'special-provisions' in fl or 'integration' in fl:
        return [
            {
                "label": "Special States",
                "type": "branch",
                "date": "Asymmetric Federalism",
                "children": [
                    {
                        "label": "Article 371-371J", "type": "sub", "date": "Special Provisions", "children": [
                            {"label": "Art 371: Maharashtra & Gujarat; Art 371A: Nagaland (protects religious/social practices); Art 371F: Sikkim", "type": "leaf"},
                            {"label": "Art 371J: Hyderabad-Karnataka region special development board; ensures institutional balance", "type": "leaf"}
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

