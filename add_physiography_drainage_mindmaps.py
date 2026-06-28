import os
import re
import json

BASE_DIR = r"upsc/geography/Physiography-Drainage"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'jcsb'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Physiography-Drainage Geography
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    if 'brahmaputra' in fl:
        return [
            {
                "label": "Source & Course",
                "type": "branch",
                "date": "Hydrology",
                "children": [
                    {
                        "label": "Tibetan & Indian Flow", "type": "sub", "date": "Course", "children": [
                            {"label": "Source: Chemayungdung glacier near Mansarovar; flows east as Yarlung Tsangpo in Tibet", "type": "leaf"},
                            {"label": "Enters India: Turns sharp south at Namcha Barwa (great bend); enters Arunachal as Dihang/Siang", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Tributaries & Floodplain",
                "type": "branch",
                "date": "Drainage Basin",
                "children": [
                    {
                        "label": "Tributaries & Islands", "type": "sub", "date": "Geomorphology", "children": [
                            {"label": "Right Bank: Subansiri, Kameng, Manas, Sankosh; Left Bank: Dibang, Lohit, Dhansiri, Kopili", "type": "leaf"},
                            {"label": "Majuli: World's largest river island; system prone to severe annual flooding & bank erosion in Assam", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'ganga' in fl:
        return [
            {
                "label": "Origin & Tributaries",
                "type": "branch",
                "date": "River Course",
                "children": [
                    {
                        "label": "Headwaters & Right Bank", "type": "sub", "date": "Tributaries", "children": [
                            {"label": "Formed by Alaknanda & Bhagirathi confluence at Devprayag; originates as Bhagirathi from Gangotri glacier", "type": "leaf"},
                            {"label": "Right bank: Yamuna (largest, joins at Prayagraj), Son, Punpun; Damodar joins Hooghly", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Left Bank Tributaries", "type": "sub", "date": "Tributaries", "children": [
                            {"label": "Left bank: Ramganga, Gomti, Ghaghara, Gandak, Kosi (Sorrow of Bihar, high silt/course shifting)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Delta & Basin",
                "type": "branch",
                "date": "Estuary",
                "children": [
                    {
                        "label": "Sundarbans Delta", "type": "sub", "date": "Delta Profile", "children": [
                            {"label": "World's largest delta formed with Brahmaputra; splits into Bhagirathi-Hooghly & Padma (enters Bangladesh)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'indus' in fl:
        return [
            {
                "label": "Source & Course",
                "type": "branch",
                "date": "River Course",
                "children": [
                    {
                        "label": "Ladakh Flow", "type": "sub", "date": "Origin", "children": [
                            {"label": "Source: Bokhar Chu glacier near Mansarovar lake; flows NW through Ladakh range; cuts Gilgit gorge", "type": "leaf"},
                            {"label": "Tributaries in Ladakh: Shyok, Gilgit, Zanskar, Hunza, Kabul; enters Pakistan near Mithankot", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Panjnad & Treaty",
                "type": "branch",
                "date": "Hydropolitics",
                "children": [
                    {
                        "label": "Five Rivers & Treaty", "type": "sub", "date": "JCSB Rivers", "children": [
                            {"label": "Jhelum (Verinag), Chenab (Bara Lacha, largest tributary), Ravi (Rohtang), Beas, Sutlej (Rakas lake)", "type": "leaf"},
                            {"label": "Indus Water Treaty 1960: India controls Eastern rivers (Ravi, Beas, Sutlej); Pakistan Western (Indus, Jhelum, Chenab)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'himalayan-drainage' in fl or 'classification-of-drainage' in fl:
        return [
            {
                "label": "Geographical Types",
                "type": "branch",
                "date": "Drainage Evolution",
                "children": [
                    {
                        "label": "Antecedent vs Consequent", "type": "sub", "date": "Drainage Types", "children": [
                            {"label": "Antecedent: Rivers existed before mountain uplift; cut deep gorges (Indus, Satluj, Brahmaputra)", "type": "leaf"},
                            {"label": "Consequent: Flow follows slope of terrain; typical of peninsular rivers (Godavari, Krishna)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Drainage Patterns",
                "type": "branch",
                "date": "Relief Patterns",
                "children": [
                    {
                        "label": "Geomorphic Forms", "type": "sub", "date": "Patterns", "children": [
                            {"label": "Dendritic (tree-like, plains); Radial (volcano/dome, Amarkantak); Trellis (folded strata); Centripetal (lakes)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'peninsular-river' in fl:
        return [
            {
                "label": "East Flowing Rivers",
                "type": "branch",
                "date": "Deltas",
                "children": [
                    {
                        "label": "Major Eastern Rivers", "type": "sub", "date": "East Flow", "children": [
                            {"label": "Godavari: Largest (Dakshin Ganga), source Trimbakeshwar; Krishna: Mahabaleshwar; Cauvery: Talakaveri", "type": "leaf"},
                            {"label": "Mahanadi: Chhattisgarh hills, Hirakud dam; all east-flowing rivers form extensive coastal deltas", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "West Flowing Rivers",
                "type": "branch",
                "date": "Estuaries",
                "children": [
                    {
                        "label": "Major Western Rivers", "type": "sub", "date": "Rift Flow", "children": [
                            {"label": "Narmada (Amarkantak) & Tapi (Multai); flow through structural rift valleys; form estuaries (no deltas)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'himalaya' in fl:
        return [
            {
                "label": "Geological Orogeny",
                "type": "branch",
                "date": "Plate Tectonics",
                "children": [
                    {
                        "label": "Tectonic Collision", "type": "sub", "date": "Orogeny", "children": [
                            {"label": "Formed by collision of Indian & Eurasian plates; Tethys sea sediment compression; young fold mountains", "type": "leaf"},
                            {"label": "Three parallel ranges: Great Himalayas (Himadri), Middle (Himachal), and Outer (Shiwalik foothills)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Regional Divisions",
                "type": "branch",
                "date": "Relief Zones",
                "children": [
                    {
                        "label": "West to East Hills", "type": "sub", "date": "Sectors", "children": [
                            {"label": "Kashmir, Himachal, Kumaon (western); Central (Nepal); Assam & Purvanchal (eastern hills)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'plateau' in fl or 'peninsular' in fl:
        return [
            {
                "label": "Central Highlands",
                "type": "branch",
                "date": "Highlands",
                "children": [
                    {
                        "label": "Malwa & Bundelkhand", "type": "sub", "date": "Northern Block", "children": [
                            {"label": "Malwa Plateau (basaltic traps); Vindhyan & Satpura ranges (blocks with Narmada rift between them)", "type": "leaf"},
                            {"label": "Chhotanagpur: Mineral storehouse of India (coal, iron); Rajmahal hills mark eastern boundary", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Deccan Plateau",
                "type": "branch",
                "date": "Southern Block",
                "children": [
                    {
                        "label": "Ghats & Deccan Trap", "type": "sub", "date": "Basalt Flow", "children": [
                            {"label": "Deccan Trap: Black soil basaltic lava flow; Western Ghats (continuous, Sahyadri) vs Eastern Ghats (discontinuous)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'plain' in fl:
        return [
            {
                "label": "Geomorphological Zones",
                "type": "branch",
                "date": "Plains Profile",
                "children": [
                    {
                        "label": "Bhabar & Terai", "type": "sub", "date": "Morphology", "children": [
                            {"label": "Bhabar: Pebble-studded zone at foothills; rivers disappear; Terai: Swampy, wet forest zone re-emergence", "type": "leaf"},
                            {"label": "Bhangar: Older, elevated alluvial soil containing kankar (lime nodules); Khadar: Fertile new floodplains", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Regional Plains",
                "type": "branch",
                "date": "Sectors",
                "children": [
                    {
                        "label": "West to East Plains", "type": "sub", "date": "Basins", "children": [
                            {"label": "Punjab (Sindhu-Sutlej, land of Doabs), Ganga plains (Rohilkhand, Awadh), and Brahmaputra valley (Assam)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'coast' in fl or 'island' in fl:
        return [
            {
                "label": "Coastal Plains",
                "type": "branch",
                "date": "Maritime",
                "children": [
                    {
                        "label": "West vs East Coasts", "type": "sub", "date": "Margins", "children": [
                            {"label": "West: Kathiawar, Konkan, Malabar; submerged coast, narrow, estuaries; East: Utkal, Northern Circars, Coromandel", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Island Groups",
                "type": "branch",
                "date": "Territories",
                "children": [
                    {
                        "label": "Andaman & Lakshadweep", "type": "sub", "date": "Islands", "children": [
                            {"label": "Andaman & Nicobar: Volcanic origin, Barren Island (active); Lakshadweep: Coral origin (atolls)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'desert' in fl:
        return [
            {
                "label": "Physiographic Features",
                "type": "branch",
                "date": "Thar Desert",
                "children": [
                    {
                        "label": "Sand Dunes & Lakes", "type": "sub", "date": "Arid morphology", "children": [
                            {"label": "Barchans (crescent-shaped dunes); shifting sand dunes (dhrians); inland drainage systems (Luni river)", "type": "leaf"},
                            {"label": "Saline lakes (playas) like Sambhar lake; high salt extraction; arid climate, <15cm rainfall", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'lake' in fl:
        return [
            {
                "label": "Lakes of India",
                "type": "branch",
                "date": "Limnology",
                "children": [
                    {
                        "label": "Genetic Types", "type": "sub", "date": "Morphology", "children": [
                            {"label": "Tectonic: Wular Lake (J&K, largest freshwater); Glacial: Roopkund; Oxbow: Kanwar Lake (Bihar)", "type": "leaf"},
                            {"label": "Lagoon/Salt: Chilika (Odisha, largest brackish), Pulicat; Crater: Lonar (Maharashtra, basaltic meteorite)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'geological' in fl or 'physiographic' in fl:
        return [
            {
                "label": "Geological Blocks",
                "type": "branch",
                "date": "Relief",
                "children": [
                    {
                        "label": "Structural Relief", "type": "sub", "date": "Slabs", "children": [
                            {"label": "Peninsular Block (stable shield, gneiss); Himalayas (flexible, folded); Indo-Ganga-Brahmaputra trough", "type": "leaf"}
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

