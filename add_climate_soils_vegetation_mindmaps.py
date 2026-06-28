import os
import re
import json

BASE_DIR = r"upsc/geography/Climate-Soils-Vegetation"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'icar', 'isfr', 'itcz', 'tej'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Factual Mappings for Climate-Soils-Vegetation Geography
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    if 'mechanism' in fl or 'monsoon' in fl:
        return [
            {
                "label": "Classic Theories",
                "type": "branch",
                "date": "Monsoon",
                "children": [
                    {
                        "label": "Thermal & Dynamic", "type": "sub", "date": "Surface Systems", "children": [
                            {"label": "Halley's Thermal: Macro land-sea breeze; summer low pressure on land pulls moist sea winds", "type": "leaf"},
                            {"label": "Flohn's Dynamic: ITCZ migrates north in summer; draws SE trade winds across equator (coriolis deflection to SW)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Upper Air Dynamics",
                "type": "branch",
                "date": "Jet Streams",
                "children": [
                    {
                        "label": "Somali & Easterly Jets", "type": "sub", "date": "Upper Air", "children": [
                            {"label": "Subtropical Westerly Jet: Retreat north of Himalayas is crucial trigger for monsoonal burst", "type": "leaf"},
                            {"label": "Tropical Easterly Jet (TEJ): Tibetan Plateau heating creates high-level easterly flow over peninsula", "type": "leaf"},
                            {"label": "Somali Jet: Cross-equatorial low-level jet; intensifies moisture feed to Arabian Sea branch", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'nino' in fl:
        return [
            {
                "label": "Pacific Anomalies",
                "type": "branch",
                "date": "ENSO Cycle",
                "children": [
                    {
                        "label": "El Nino vs La Nina", "type": "sub", "date": "Walker Cell", "children": [
                            {"label": "El Niño: Warming of Central & East Pacific; weakens Walker circulation, causing monsoon dry spells & droughts", "type": "leaf"},
                            {"label": "La Niña: Cooling of East Pacific; intensifies Walker circulation, bringing surplus monsoonal rains & floods", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Teleconnections",
                "type": "branch",
                "date": "Ocean Oscillations",
                "children": [
                    {
                        "label": "IOD & MJO", "type": "sub", "date": "Anomalies", "children": [
                            {"label": "Positive IOD: Warm west Indian Ocean; increases rainfall, offsets negative El Niño drought impacts", "type": "leaf"},
                            {"label": "Negative IOD: Warm east Indian Ocean; suppresses monsoonal flow; Madden-Julian Oscillation active/break cycles", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'factor' in fl or 'influence' in fl:
        return [
            {
                "label": "Physiographic Factors",
                "type": "branch",
                "date": "Relief & Barriers",
                "children": [
                    {
                        "label": "Himalayas & Ghats", "type": "sub", "date": "Topography", "children": [
                            {"label": "Himalayas: Direct barrier shield blocking cold Siberian winds; intercepts SW monsoon forcing precipitation", "type": "leaf"},
                            {"label": "Western Ghats: High rainfall on windward side; rain-shadow dry arid zone (As) on leeward Deccan side", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Atmospheric Factors",
                "type": "branch",
                "date": "Winds & Pressure",
                "children": [
                    {
                        "label": "Disturbances & Maritime", "type": "sub", "date": "Winds", "children": [
                            {"label": "Western Disturbances: Low-pressure systems from Mediterranean; brings essential winter rains to NW crops", "type": "leaf"},
                            {"label": "Continentality: Extreme seasonal temperature swings in inland north plains vs maritime south", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'koppen' in fl:
        return [
            {
                "label": "Tropical Climates",
                "type": "branch",
                "date": "Köppen System",
                "children": [
                    {
                        "label": "Amw & Aw Zones", "type": "sub", "date": "Tropical Zones", "children": [
                            {"label": "Amw: Monsoon wet, short dry season (Malabar coast, high precipitation, evergreen forest)", "type": "leaf"},
                            {"label": "Aw: Tropical savanna (peninsular plateau, dry winter, deciduous vegetation)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Arid & Temperate",
                "type": "branch",
                "date": "Other Zones",
                "children": [
                    {
                        "label": "Deserts & Steppes", "type": "sub", "date": "Dry & Cold", "children": [
                            {"label": "Bshw: Semi-arid steppe (NW India, Deccan rainshadow); Bwhw: Hot desert (Thar, low rain)", "type": "leaf"},
                            {"label": "Cwg: Warm temperate, dry winter (Gangetic plains); Dfc: Cold humid winter (Arunachal Pradesh)", "type": "leaf"},
                            {"label": "E & ET: Polar and Tundra climates found in high altitude Himalayan zones", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'erosion' in fl:
        return [
            {
                "label": "Water Erosion",
                "type": "branch",
                "date": "Water Runoff",
                "children": [
                    {
                        "label": "Erosion Stages", "type": "sub", "date": "Degradation", "children": [
                            {"label": "Stages: Splash (raindrop impact) -> Sheet (topsoil layer removed) -> Rill (channels) -> Gully (ravines)", "type": "leaf"},
                            {"label": "Chambal Ravines: Classic badland topography created by unchecked, deep gully erosion in alluvial tracts", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Wind & Human Factors",
                "type": "branch",
                "date": "Winds",
                "children": [
                    {
                        "label": "Topsoil Loss Triggers", "type": "sub", "date": "Factors", "children": [
                            {"label": "Deforestation & overgrazing denude protective vegetation; intense dry summer winds blow away dry topsoil", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'conservation' in fl:
        return [
            {
                "label": "Mechanical Measures",
                "type": "branch",
                "date": "Engineering",
                "children": [
                    {
                        "label": "Engineering Controls", "type": "sub", "date": "Structures", "children": [
                            {"label": "Contour Bunding & Terracing: Reduces slope length; slows surface runoff velocity on hilly terrains", "type": "leaf"},
                            {"label": "Check Dams & Gully Plugging: Arrests soil movement in gullies; silt trapping and water retention", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Biological & Farming",
                "type": "branch",
                "date": "Agronomic",
                "children": [
                    {
                        "label": "Agronomic Methods", "type": "sub", "date": "Vegetative", "children": [
                            {"label": "Strip Cropping & Cover Crops: Alternating dense crops binds soil; shelterbelts act as windbreaks in arid zones", "type": "leaf"},
                            {"label": "Crop Rotation & Agroforestry: Restores soil nutrients; deep tree roots stabilize sub-surface soil", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'acidity' in fl or 'texture' in fl:
        return [
            {
                "label": "Soil Chemistry",
                "type": "branch",
                "date": "pH Properties",
                "children": [
                    {
                        "label": "pH & Remediation", "type": "sub", "date": "Chemistry", "children": [
                            {"label": "Optimal pH: 6-7; acidic soils (high leaching in laterites) neutralized using Lime (CaCO3)", "type": "leaf"},
                            {"label": "Saline/Alkaline (Usar): High capillary draw of salts in dry irrigated zones; treated using Gypsum (CaSO4)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Textural Profiles",
                "type": "branch",
                "date": "Physical State",
                "children": [
                    {
                        "label": "Physical Properties", "type": "sub", "date": "Textures", "children": [
                            {"label": "Texture classes: Sand, silt, & clay; determines soil aeration, water-holding capacity, & nutrient retention", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'mineral' in fl or 'soil' in fl:
        return [
            {
                "label": "Major Soil Taxonomy",
                "type": "branch",
                "date": "ICAR Classes",
                "children": [
                    {
                        "label": "Alluvial & Black", "type": "sub", "date": "Major Soil", "children": [
                            {"label": "Alluvial (40%): Khadar (new loam, fertile) vs Bhangar (old clay, kankar); rich in potash, deficient in nitrogen", "type": "leaf"},
                            {"label": "Black (Regur): Basaltic origin; self-ploughing cracks; high moisture retentive clay; rich in iron, lime, magnesia", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Leached & Acidic",
                "type": "branch",
                "date": "Special Soils",
                "children": [
                    {
                        "label": "Laterite & Peaty", "type": "sub", "date": "Acidic soils", "children": [
                            {"label": "Laterite: High rain leaching removes silica, leaving iron/aluminum oxides; poor in organic matter", "type": "leaf"},
                            {"label": "Peaty/Marshy: High organic accumulation (Kari soils); highly acidic, heavy black clay found in wet areas", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'mangrove' in fl:
        return [
            {
                "label": "Adaptations",
                "type": "branch",
                "date": "Halophytes",
                "children": [
                    {
                        "label": "Halophytic Features", "type": "sub", "date": "Biology", "children": [
                            {"label": "Pneumatophores (breathing roots) to absorb oxygen in waterlogged saline soils; stilt roots for stability", "type": "leaf"},
                            {"label": "Vivipary reproduction: Seeds germinate while still attached to parent tree; adapts to tidal currents", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Distribution",
                "type": "branch",
                "date": "Estuarine",
                "children": [
                    {
                        "label": "Estuarine Zones", "type": "sub", "date": "Geography", "children": [
                            {"label": "Sundarbans (largest deltaic mangrove forest); Mahanadi, Godavari, Krishna, & Cauvery deltas; Gujarat coast", "type": "leaf"},
                            {"label": "Acts as bio-shield against cyclones, storm surges, & coastal erosion; rich spawning ground for marine life", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'forest' in fl:
        return [
            {
                "label": "Forest Cover Stats",
                "type": "branch",
                "date": "ISFR Report",
                "children": [
                    {
                        "label": "National Status", "type": "sub", "date": "Data", "children": [
                            {"label": "ISFR latest: Forest & tree cover is ~24.6% of geographical area", "type": "leaf"},
                            {"label": "State rankings: Madhya Pradesh has largest area; Mizoram has highest percentage forest cover (~84%)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Policy Goals",
                "type": "branch",
                "date": "Framework",
                "children": [
                    {
                        "label": "National Target", "type": "sub", "date": "Forest Policy", "children": [
                            {"label": "National Forest Policy 1988: Target of 33% total geographical area under forest cover to maintain ecology", "type": "leaf"},
                            {"label": "Forest categorization: Reserved (highest protection), Protected, and Unclassed forests", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    elif 'vegetation' in fl:
        return [
            {
                "label": "Moist & Dry Forests",
                "type": "branch",
                "date": "Deciduous",
                "children": [
                    {
                        "label": "Tropical Types", "type": "sub", "date": "Moist/Dry", "children": [
                            {"label": "Tropical Evergreen: >200cm rain; multi-layered canopy; Ebony, Mahogany, Rosewood, Rubber", "type": "leaf"},
                            {"label": "Tropical Deciduous (Monsoon): 70-200cm rain; shed leaves in dry season; Teak, Sal, Sandalwood, Bamboo", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Montane & Arid",
                "type": "branch",
                "date": "Coniferous",
                "children": [
                    {
                        "label": "Alpine & Thorn", "type": "sub", "date": "High/Dry", "children": [
                            {"label": "Montane: Coniferous pine, deodar, oak with altitude; Thorn: Acacia, cactus in low rain zones", "type": "leaf"}
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

