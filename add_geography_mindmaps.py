import os
import re
import json

MINDMAPS = {
    "Changed-Names-of-Some-Cities-States-and-Countries": {
        "label": "Changed Names\n(Cities & Nations)",
        "type": "root",
        "children": [
            {
                "label": "Decolonization &\nNational Identity",
                "type": "branch",
                "date": "Post-Colonial Era",
                "children": [
                    {"label": "Nations", "type": "sub", "date": "Geopolitical Shift", "children": [
                        {"label": "Ceylon -> Sri Lanka (1972);\nSiam -> Thailand (1939);\nAbyssinia -> Ethiopia", "type": "leaf"},
                        {"label": "Burma -> Myanmar (1989);\nEast Pakistan -> Bangladesh (1971);\nPersia -> Iran (1935)", "type": "leaf"},
                        {"label": "Bechuanaland -> Botswana (1966);\nNyasaland -> Malawi (1964);\nMesopotamia -> Iraq", "type": "leaf"}
                    ]},
                    {"label": "Indian States & Regions", "type": "sub", "date": "Federal Reorganization", "children": [
                        {"label": "United Provinces -> Uttar Pradesh (1950);\nMadras State -> Tamil Nadu (1969)", "type": "leaf"},
                        {"label": "Mysore State -> Karnataka (1973);\nOrissa -> Odisha (2011)", "type": "leaf"},
                        {"label": "Pondicherry -> Puducherry (2006);\nUttaranchal -> Uttarakhand (2007)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Urban & Cultural\nReclamation",
                "type": "branch",
                "date": "Native Names",
                "children": [
                    {"label": "Indian Cities", "type": "sub", "date": "Municipal Changes", "children": [
                        {"label": "Bombay -> Mumbai (1995);\nMadras -> Chennai (1996)", "type": "leaf"},
                        {"label": "Calcutta -> Kolkata (2001);\nBangalore -> Bengaluru (2014)", "type": "leaf"},
                        {"label": "Trivandrum -> Thiruvananthapuram (1991);\nPoona -> Pune (2008);\nCawnpore -> Kanpur (1948)", "type": "leaf"}
                    ]},
                    {"label": "Global Cities", "type": "sub", "date": "Spelling & Regimes", "children": [
                        {"label": "Peking -> Beijing (Pinyin transition);\nSaigon -> Ho Chi Minh City (1976)", "type": "leaf"},
                        {"label": "Christiania -> Oslo (1925);\nAngora -> Ankara (1930);\nConstantinople -> Istanbul (1930)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Modern Sovereign\nCorrections",
                "type": "branch",
                "date": "Recent Updates",
                "children": [
                    {"label": "Geopolitical Changes", "type": "sub", "date": "Sovereign Pronunciations", "children": [
                        {"label": "Turkey -> Türkiye (2022);\nreflects authentic national spelling", "type": "leaf"},
                        {"label": "Swaziland -> Eswatini (2018);\nprevents confusion with Switzerland", "type": "leaf"},
                        {"label": "Holland -> Netherlands (2020);\nrebrands to drop regional bias", "type": "leaf"},
                        {"label": "Zaire -> DR Congo (1997);\nUpper Volta -> Burkina Faso (1984)", "type": "leaf"},
                        {"label": "Czech Republic -> Czechia (2016);\nKampuchea -> Cambodia (1989)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Continents-and-Important-Cities-of-the-World": {
        "label": "Continents &\nGlobal Cities",
        "type": "root",
        "children": [
            {
                "label": "Asia & Africa\nHubs",
                "type": "branch",
                "date": "Eastern Hemisphere",
                "children": [
                    {"label": "Asia", "type": "sub", "date": "Economic Powerhouses", "children": [
                        {"label": "Tokyo: World's largest metro area;\nSingapore: Chokepoint trade at Malacca Strait", "type": "leaf"},
                        {"label": "Shanghai: Busiest cargo container port;\nMumbai: Financial capital, natural harbor", "type": "leaf"},
                        {"label": "Dubai: Aviation crossroads;\nJerusalem: Geopolitical & religious core", "type": "leaf"}
                    ]},
                    {"label": "Africa", "type": "sub", "date": "Resource & Trade Hubs", "children": [
                        {"label": "Cairo: Megacity on Nile delta;\nLagos: West African economic powerhouse", "type": "leaf"},
                        {"label": "Johannesburg: Gold & mineral exchange;\nNairobi: Silicon Savannah tech center", "type": "leaf"},
                        {"label": "Cape Town: Port on Cape Route;\nAddis Ababa: AU Headquarters", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Europe & The\nAmericas",
                "type": "branch",
                "date": "Western Hemisphere",
                "children": [
                    {"label": "Europe", "type": "sub", "date": "Diplomatic & Trade", "children": [
                        {"label": "London: Financial center, GMT line;\nParis: Political & cultural center on Seine", "type": "leaf"},
                        {"label": "Frankfurt: ECB bank seat;\nGeneva: UN agencies, WTO, WHO", "type": "leaf"},
                        {"label": "Rotterdam: Largest European seaport;\nMoscow: Eurasian political command", "type": "leaf"}
                    ]},
                    {"label": "North & South America", "type": "sub", "date": "Hemispheric Giants", "children": [
                        {"label": "New York: UN Headquarters, Wall Street;\nWashington D.C.: IMF & World Bank seats", "type": "leaf"},
                        {"label": "São Paulo: Busiest city in South America;\nBuenos Aires: Estuary trade on La Plata", "type": "leaf"},
                        {"label": "Mexico City: Aztec core, megacity;\nVancouver: Canadian Pacific trade hub", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Oceania Hubs",
                "type": "branch",
                "date": "Pacific Region",
                "children": [
                    {"label": "Oceania Cities", "type": "sub", "date": "Trade & Capitals", "children": [
                        {"label": "Sydney: Deep natural harbor, finance;\nMelbourne: Cultural & industrial capital", "type": "leaf"},
                        {"label": "Canberra: Planned federal capital city;\nAuckland: Major Polynesian maritime hub", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Distinctive-Names-of-CountriesTowns-Geographical-Epithets": {
        "label": "Geographical\nEpithets",
        "type": "root",
        "children": [
            {
                "label": "National & Land\nEpithets",
                "type": "branch",
                "date": "Countries & Islands",
                "children": [
                    {"label": "Sun & Climate", "type": "sub", "date": "Natural Features", "children": [
                        {"label": "Japan: Land of the Rising Sun;\nNorway: Land of the Midnight Sun", "type": "leaf"},
                        {"label": "Finland: Land of Thousand Lakes;\nCanada: Land of the Maple Leaf", "type": "leaf"}
                    ]},
                    {"label": "Economic & Resource", "type": "sub", "date": "Commodity Monikers", "children": [
                        {"label": "Cuba: Sugar Bowl of the World;\nAustralia: Land of Golden Fleece (wool)", "type": "leaf"},
                        {"label": "South Africa: Land of Diamonds;\nChile: Land of Copper", "type": "leaf"}
                    ]},
                    {"label": "Cultural & Scenic", "type": "sub", "date": "Leisure & Heritage", "children": [
                        {"label": "Switzerland: Playground of Europe;\nIreland: Emerald Isle (lush vegetation)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Urban & City\nEpithets",
                "type": "branch",
                "date": "Towns & Capitals",
                "children": [
                    {"label": "Classics", "type": "sub", "date": "Ancient & Modern", "children": [
                        {"label": "Rome: Eternal City / City of Seven Hills;\nNew York: The Big Apple / Empire City", "type": "leaf"},
                        {"label": "Chicago: Windy City;\nParis: City of Light (La Ville Lumière)", "type": "leaf"}
                    ]},
                    {"label": "Specialty Cities", "type": "sub", "date": "Geographical", "children": [
                        {"label": "Venice: Queen of the Adriatic;\nLhasa: Forbidden City (Tibet)", "type": "leaf"},
                        {"label": "Jaipur: Pink City;\nPittsburgh: Steel City;\nDetroit: Motor City", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Water & Path\nEpithets",
                "type": "branch",
                "date": "Chokepoints & Rivers",
                "children": [
                    {"label": "Global Passages", "type": "sub", "date": "Sea Epithets", "children": [
                        {"label": "Gibraltar: Key to the Mediterranean;\nBab-el-Mandeb: Gate of Tears", "type": "leaf"},
                        {"label": "Pamir Plateau: Roof of the World;\nKent: Garden of England", "type": "leaf"}
                    ]},
                    {"label": "Sorrow Rivers", "type": "sub", "date": "Flooding Hazards", "children": [
                        {"label": "Hwang Ho: Sorrow of China (Yellow River);\nDamodar: Sorrow of Bengal", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Economic-Classification-of-Countries-of-the-World": {
        "label": "Economic\nClassifications",
        "type": "root",
        "children": [
            {
                "label": "Development\nCategories",
                "type": "branch",
                "date": "Comparative States",
                "children": [
                    {"label": "Developed Economies", "type": "sub", "date": "Advanced tertiary/quaternary", "children": [
                        {"label": "High GNI per capita;\nadvanced tech (USA, Germany, Japan)", "type": "leaf"},
                        {"label": "High life expectancy;\nlow infant mortality rates", "type": "leaf"}
                    ]},
                    {"label": "Developing / Emerging", "type": "sub", "date": "Transitioning", "children": [
                        {"label": "Rapid industrialization;\nstructural shift (India, Brazil, China)", "type": "leaf"},
                        {"label": "High infrastructure spending;\nvarying income inequality", "type": "leaf"}
                    ]},
                    {"label": "Least Developed (LDCs)", "type": "sub", "date": "UN Vulnerable List", "children": [
                        {"label": "Low per capita income + low human assets;\nhigh economic vulnerability", "type": "leaf"},
                        {"label": "45+ countries (e.g., Niger, Yemen,\nBurundi, South Sudan)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Classification\nFrameworks",
                "type": "branch",
                "date": "Global Institutions",
                "children": [
                    {"label": "World Bank", "type": "sub", "date": "GNI per capita", "children": [
                        {"label": "Low, Lower-Middle (India),\nUpper-Middle (China), & High-Income", "type": "leaf"}
                    ]},
                    {"label": "UN Development (UNDP)", "type": "sub", "date": "Human Indices", "children": [
                        {"label": "HDI: Health (life span), Knowledge (schooling),\nand Living Standard (GNI)", "type": "leaf"}
                    ]},
                    {"label": "IMF classification", "type": "sub", "date": "Advanced vs emerging", "children": [
                        {"label": "Considers exports, financial integration,\nand overall economic health", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Important-Cities-Situated-on-the-Banks-of-Rivers": {
        "label": "Riverside Cities",
        "type": "root",
        "children": [
            {
                "label": "Europe & Asia\nRivers",
                "type": "branch",
                "date": "Old World Geography",
                "children": [
                    {"label": "Europe Riverside", "type": "sub", "date": "Capital Capitals", "children": [
                        {"label": "London: River Thames;\nParis: River Seine", "type": "leaf"},
                        {"label": "Rome: River Tiber;\nBerlin: River Spree", "type": "leaf"},
                        {"label": "Vienna / Budapest / Belgrade: Danube;\nWarsaw: Vistula River;\nKyiv: Dnieper", "type": "leaf"}
                    ]},
                    {"label": "Asia & Middle East", "type": "sub", "date": "Key Hubs", "children": [
                        {"label": "New Delhi: Yamuna;\nBaghdad: Tigris River", "type": "leaf"},
                        {"label": "Yangon: Irrawaddy River;\nBangkok: Chao Phraya", "type": "leaf"},
                        {"label": "Tokyo: Sumida River;\nShanghai: Yangtze / Huangpu", "type": "leaf"},
                        {"label": "Cairo: Nile River;\nKhartoum: Blue & White Nile confluence", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Americas &\nOceania Rivers",
                "type": "branch",
                "date": "New World & South",
                "children": [
                    {"label": "North & South America", "type": "sub", "date": "Estuaries & Rivers", "children": [
                        {"label": "New York: Hudson River;\nWashington D.C.: Potomac River", "type": "leaf"},
                        {"label": "Montreal: St. Lawrence River;\nBuenos Aires: Rio de la Plata", "type": "leaf"},
                        {"label": "Manaus: Amazon River;\nNew Orleans: Mississippi River", "type": "leaf"}
                    ]},
                    {"label": "Oceania", "type": "sub", "date": "Australia", "children": [
                        {"label": "Sydney: Parramatta River;\nMelbourne: Yarra River", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Regional-Grouping-of-Countries-of-the-World": {
        "label": "Regional\nGroupings",
        "type": "root",
        "children": [
            {
                "label": "Trade & Economic\nIntegration",
                "type": "branch",
                "date": "Market Blocs",
                "children": [
                    {"label": "Customs Unions & FTAs", "type": "sub", "date": "Economic Agreements", "children": [
                        {"label": "European Union (EU): Single currency,\nfree movement, Schengen zone", "type": "leaf"},
                        {"label": "USMCA: North America (formerly NAFTA);\nASEAN: SE Asia economic integration", "type": "leaf"},
                        {"label": "Mercosur: Southern South America;\nGCC: Gulf Cooperation Council (Middle East)", "type": "leaf"},
                        {"label": "RCEP: Regional Comprehensive Economic Partnership;\nCPTPP: Trans-Pacific partnership", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Security &\nGeopolitical",
                "type": "branch",
                "date": "Defense & Power",
                "children": [
                    {"label": "Defense Alliances", "type": "sub", "date": "Military Packs", "children": [
                        {"label": "NATO: Transatlantic security pact (Article 5);\nSCO: Shanghai Cooperation (Eurasian security)", "type": "leaf"},
                        {"label": "QUAD: Indo-Pacific security dialogue;\nAUKUS: Trilateral defense pact (subs)", "type": "leaf"}
                    ]},
                    {"label": "Political Platforms", "type": "sub", "date": "Multilateral Forums", "children": [
                        {"label": "BRICS: Brazil, Russia, India, China,\nSouth Africa + Middle East expansion", "type": "leaf"},
                        {"label": "G20: Top 19 nations + EU + AU;\nG7: Advanced industrialized economies", "type": "leaf"},
                        {"label": "Commonwealth of Nations: Former colonies;\nOPEC: Petroleum exporting cartel", "type": "leaf"}
                    ]}
                ]
            }
        ]
    }
}

BASE_DIR = r"upsc/geography/World-Regional-Geography"

# Patching Logic
def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
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

    # Re-inject script
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
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
            
        topic_name = folder.replace('-', ' ')
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        mindmap_key = folder
        if mindmap_key not in MINDMAPS:
            print(f"[{idx+1}/{len(folders)}] WARNING: Key {mindmap_key} not in pre-defined list. Creating default.")
            MINDMAPS[mindmap_key] = {
                "label": topic_name.replace(" ", "\n"),
                "type": "root",
                "children": [
                    {"label": "Overview", "type": "branch", "date": "Concept", "children": [
                        {"label": "Definition", "type": "sub", "children": [
                            {"label": "Key features", "type": "leaf"}
                        ]}
                    ]}
                ]
            }
            
        mindmap_data = MINDMAPS[mindmap_key]
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()
