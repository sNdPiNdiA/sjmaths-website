import os
import re
import json

BASE_DIR = r"upsc/polity/Local-Government-UTs-Special-Areas"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'pri', 'pesa', 'scs', 'adcs', 'amtm', 'mlas', 'mps', 'obcs', 'lsa'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Local Government, UTs, and Special Areas
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. Evolution of PRI / Local Govt
    if 'evolution' in fl or 'local-government' in fl:
        return [
            {
                "label": "Evolution of PRI",
                "type": "branch",
                "date": "Committees",
                "children": [
                    {
                        "label": "Balwant Rai & Ashok Mehta", "type": "sub", "date": "1957 & 1977", "children": [
                            {"label": "Balwant Rai Mehta Committee (1957): Recommended 3-tier Panchayati Raj system (Gram, Panchayat Samiti, Zilla Parishad)", "type": "leaf"},
                            {"label": "Ashok Mehta Committee (1977): Recommended 2-tier system (Mandal Panchayat and Zilla Parishad); proposed political party participation", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "GVK Rao & LM Singhvi", "type": "sub", "date": "1985 & 1986", "children": [
                            {"label": "G.V.K. Rao Committee (1985): Noticed 'grass without roots' bureaucracy; recommended strengthening Zilla Parishad", "type": "leaf"},
                            {"label": "L.M. Singhvi Committee (1986): Recommended constitutional status for local bodies; proposed Nyaya Panchayats", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. 73rd Amendment
    elif '73rd-amendment' in fl:
        return [
            {
                "label": "73rd Amendment Act",
                "type": "branch",
                "date": "PRI Constitutionalization",
                "children": [
                    {
                        "label": "Part IX & 11th Schedule", "type": "sub", "date": "Structure", "children": [
                            {"label": "Added Part IX to Constitution and 11th Schedule containing 29 functional items for Panchayats", "type": "leaf"},
                            {"label": "Gram Sabha: Foundation of PRI system; consists of all registered voters in the village area", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Mandatory Bodies", "type": "sub", "date": "Elections & Finance", "children": [
                            {"label": "Three-tier system (except in states with pop < 20 lakhs); direct elections; 1/3rd seats reserved for women", "type": "leaf"},
                            {"label": "State Finance Commission (Art 243-I) appointed by Governor every 5 years; State Election Commission (Art 243K)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. Compulsory & Voluntary Provisions
    elif 'compulsory' in fl:
        return [
            {
                "label": "Compulsory Provisions",
                "type": "branch",
                "date": "Obligatory",
                "children": [
                    {
                        "label": "Obligatory Features", "type": "sub", "date": "Mandatory", "children": [
                            {"label": "Organization of Gram Sabha; establishing 3-tier system; direct elections for all members; 21 years min age to contest", "type": "leaf"},
                            {"label": "Mandatory reservation for SCs & STs in proportion to population, and 1/3rd reservation for women", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Voluntary Provisions",
                "type": "branch",
                "date": "Discretionary",
                "children": [
                    {
                        "label": "Discretionary Features", "type": "sub", "date": "Voluntary", "children": [
                            {"label": "Providing reservation for backward classes (OBCs); devolution of financial powers to tax and collect revenue", "type": "leaf"},
                            {"label": "Giving representation to MPs and MLAs in Panchayats at intermediate and district levels", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. 74th Amendment / Urban Local Government
    elif '74th-constitutional' in fl or 'urban-local' in fl or 'types-of-urban' in fl:
        return [
            {
                "label": "Urban Local Govt",
                "type": "branch",
                "date": "74th Amendment",
                "children": [
                    {
                        "label": "Part IX-A & 12th Schedule", "type": "sub", "date": "Structure", "children": [
                            {"label": "Added Part IX-A and 12th Schedule containing 18 functional items; 3 types: Nagar Panchayats, Municipal Councils, Municipal Corporations", "type": "leaf"},
                            {"label": "District Planning Committee (Art 243ZD): Consolidates plans prepared by Panchayats and Municipalities in the district", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Types of Urban Bodies", "type": "sub", "date": "Urban Types", "children": [
                            {"label": "8 types: Municipal Corporation (major cities), Municipality, Notified Area Committee, Town Area Committee, Cantonment Board, Township, Port Trust, Special Purpose Agency", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. PESA Act 1996
    elif 'pesa' in fl:
        return [
            {
                "label": "PESA Act 1996",
                "type": "branch",
                "date": "Scheduled Areas",
                "children": [
                    {
                        "label": "Tribal Decentralization", "type": "sub", "date": "PESA Mandate", "children": [
                            {"label": "Extends Part IX provisions to Fifth Schedule areas in 10 states (based on Bhuria Committee recommendations)", "type": "leaf"},
                            {"label": "Empowers Gram Sabha to safeguard traditional customs, manage minor water bodies, and approve development plans", "type": "leaf"},
                            {"label": "Mandatory consultation before land acquisition, resettlement, and granting licenses for minor minerals in tribal tracts", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. Fifth & Sixth Schedules
    elif 'schedule' in fl or 'scheduled-and-tribal' in fl:
        return [
            {
                "label": "Fifth Schedule Areas",
                "type": "branch",
                "date": "Art 244(1)",
                "children": [
                    {
                        "label": "Executive & TAC", "type": "sub", "date": "5th Schedule", "children": [
                            {"label": "Applies to scheduled areas in states other than Assam, Meghalaya, Tripura, & Mizoram; Governor has special executive powers", "type": "leaf"},
                            {"label": "Tribes Advisory Council (TAC): Established in 5th schedule states; max 20 members (3/4th must be ST MLAs)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Sixth Schedule Areas",
                "type": "branch",
                "date": "Art 244(2)",
                "children": [
                    {
                        "label": "Autonomous Districts", "type": "sub", "date": "6th Schedule", "children": [
                            {"label": "Applies to tribal areas in 4 states: Assam, Meghalaya, Tripura, and Mizoram (AMTM); autonomous district councils (ADCs) formed", "type": "leaf"},
                            {"label": "ADCs have legislative powers to make laws on land, forests, marriage; can assess taxes and establish courts", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. Administration of Tribal Areas
    elif 'administration-of-tribal' in fl:
        return [
            {
                "label": "Tribal Area Admin",
                "type": "branch",
                "date": "Sixth Schedule",
                "children": [
                    {
                        "label": "District Councils", "type": "sub", "date": "ADCs", "children": [
                            {"label": "Autonomous District Councils (30 members; 4 nominated by Governor, 26 directly elected for 5-year terms)", "type": "leaf"},
                            {"label": "Governor can dissolve or reorganize autonomous districts; laws of Parliament/State do not apply or apply with modifications", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. Administration of UTs / Delhi Status
    elif 'administration-of-uts' in fl or 'union-territories' in fl or 'delhi' in fl:
        return [
            {
                "label": "UT Administration",
                "type": "branch",
                "date": "Art 239-241",
                "children": [
                    {
                        "label": "Central Control", "type": "sub", "date": "UT Admin", "children": [
                            {"label": "UTs administered by President through an Administrator (Lieutenant Governor or Chief Commissioner) designated by President", "type": "leaf"},
                            {"label": "Parliament has supreme power to make laws on any subject in any list (including State List) for UTs", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Delhi Status (Art 239AA)", "type": "sub", "date": "NCT Delhi", "children": [
                            {"label": "69th Constitutional Amendment Act (1991) designated Delhi as National Capital Territory (NCT) with a 70-member assembly", "type": "leaf"},
                            {"label": "Delhi assembly can make laws on State/Concurrent list EXCEPT Police, Public Order, and Land (under Central Govt/LG control)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. Special Category Status
    elif 'special-category' in fl:
        return [
            {
                "label": "Special Category Status",
                "type": "branch",
                "date": "Finance",
                "children": [
                    {
                        "label": "Gadgil Formula & Finance", "type": "sub", "date": "SCS Criteria", "children": [
                            {"label": "Introduced in 1969 on 5th Finance Commission recommendations (Gadgil Formula) for hilly, low population density, border states", "type": "leaf"},
                            {"label": "Financial benefits: 90% of central scheme funds given as grants (vs 60% for others); unused funds do not lapse (carry forward)", "type": "leaf"},
                            {"label": "14th Finance Commission abolished SCS classification, replacing it with increased tax devolution (from 32% to 42%)", "type": "leaf"}
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

