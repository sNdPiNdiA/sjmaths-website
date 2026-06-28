import os
import re
import json

BASE_DIR = r"ssc-cgl/general-awareness/static-gk"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp', 'ist', 'gmt', 'utc', 'uv', 'co2', 'tisco', 'jnpt', 'cag', 'niti', 'upsc', 'spsc', 'nhrc', 'cic', 'cvc', 'sc', 'st', 'obc', 'dpsp', 'vp', 'pm', 'amtm', 'hc', 'gdp', 'gnp', 'ndp', 'nnp', 'nfia', 'pdi', 'gva', 'cso', 'nso', 'fyp', 'ndc', 'rbi', 'crr', 'slr', 'msf', 'omo', 'npa', 'ibc', 'mat', 'frbm', 'msme', 'lpg', 'fdi', 'fii', 'psu', 'bop', 'cacp', 'msp', 'frp', 'bec', 'bcg', 'atp', 'rbc', 'wbc', 'sa', 'cns', 'adh', 'kg', 'hp', 'tir', 'sonar', 'tnt', 'rdx', 'gk', 'un', 'unsc', 'icj', 'imf', 'wto', 'saarc', 'asean', 'brics', 'unesco', 'who', 'interpol', 'adb', 'hq', 'nh', 'k2', 'ad', 'lbw'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between', 'or', 'life', 'major', 'era', 'sects', 'teachings', 'councils', 'findings', 'trade', 'sites', 'rig', 'later']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Complete detailed mindmaps for all 2 CGL Static GK folders
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. STATIC GK: DAYS, BOOKS & AUTHORS, SPORTS TERMS & TROPHIES
    if 'days-books' in fl:
        return [
            {
                "label": "Important Days", "type": "branch", "date": "Calendar Days",
                "children": [
                    {
                        "label": "National & International (Jan-Jun)", "type": "sub", "date": "Jan - Jun",
                        "children": [
                            {"label": "Jan: 9 (Pravasi Bharatiya), 12 (National Youth), 15 (Army), 24 (Girl Child), 25 (Voters); Feb: 4 (Cancer), 28 (Science Day)", "type": "leaf"},
                            {"label": "Mar: 8 (Women's Day), 21 (Forestry), 22 (Water); Apr: 7 (Health), 18 (Heritage), 22 (Earth Day)", "type": "leaf"},
                            {"label": "May: 1 (Labour), 31 (Anti-Tobacco); Jun: 5 (Environment), 21 (Yoga Day)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "National & International (Jul-Dec)", "type": "sub", "date": "Jul - Dec",
                        "children": [
                            {"label": "Jul: 11 (World Population), 29 (Tiger Day); Aug: 29 (National Sports Day - Dhyan Chand)", "type": "leaf"},
                            {"label": "Sep: 5 (Teachers), 8 (Literacy), 16 (Ozone Day); Oct: 2 (Non-Violence), 8 (Air Force), 24 (UN Day)", "type": "leaf"},
                            {"label": "Nov: 14 (Children/Diabetes), 26 (Constitution); Dec: 1 (AIDS), 10 (Human Rights), 25 (Good Governance)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Famous Books & Authors", "type": "branch", "date": "Literature",
                "children": [
                    {
                        "label": "Ancient & Medieval Classics", "type": "sub", "date": "Classics",
                        "children": [
                            {"label": "Chanakya: Arthashastra; Kalhana: Rajatarangini (Kashmir history); Banabhatta: Harshacharita, Kadambari", "type": "leaf"},
                            {"label": "Kalidasa: Shakuntala, Meghaduta; Al-Biruni: Kitab-ul-Hind; Abul Fazl: Akbarnama, Ain-i-Akbari; Gulbadan: Humayunnama", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Modern Literature", "type": "sub", "date": "Modern Books",
                        "children": [
                            {"label": "Rabindranath Tagore: Gitanjali (Nobel 1913), Gora; Mahatma Gandhi: My Experiments with Truth, Hind Swaraj", "type": "leaf"},
                            {"label": "Jawaharlal Nehru: Discovery of India; Premchand: Godan, Gaban; Arundhati Roy: The God of Small Things", "type": "leaf"},
                            {"label": "Salman Rushdie: Midnight's Children; Vikram Seth: A Suitable Boy", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Sports Trophies & Terminology", "type": "branch", "date": "Sports GK",
                "children": [
                    {
                        "label": "Major Sports & Trophies", "type": "sub", "date": "Trophies",
                        "children": [
                            {"label": "Cricket: Ranji Trophy, Duleep Trophy, Vijay Hazare, Deodhar, Ashes Series, Ryder Cup (Golf)", "type": "leaf"},
                            {"label": "Football: Durand Cup (oldest in Asia), Santosh Trophy, Subroto, Rovers; Hockey: Sultan Azlan Shah, Aga Khan Cup", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Sports Terminology", "type": "sub", "date": "Terms",
                        "children": [
                            {"label": "Cricket: Chinaman, Maiden Over, Silly Point, Yorker, Googly, LBW; Football: Offside, Dribble, Yellow Card", "type": "leaf"},
                            {"label": "Tennis: Deuce, Ace, Grand Slam, Volley; Chess: Checkmate, Gambit; Swimming: Butterfly Stroke; Hockey: Bully", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. STATIC GK: SUPERLATIVES, ORGANIZATIONS & SYMBOLS
    elif 'superlatives' in fl:
        return [
            {
                "label": "Superlatives (India & World)", "type": "branch", "date": "Superlatives",
                "children": [
                    {
                        "label": "Indian Superlatives", "type": "sub", "date": "India Firsts",
                        "children": [
                            {"label": "Highest: K2 peak (Godwin-Austen), Tehri Dam (on Bhagirathi), Kunchikal Falls (waterfall)", "type": "leaf"},
                            {"label": "Longest: Ganga river, Indira Gandhi Canal, Hirakud Dam (Mahanadi river), NH 44 highway", "type": "leaf"},
                            {"label": "Largest: Wular Lake (freshwater, J&K), Chilika Lake (saline, Odisha), Thar Desert", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "World Superlatives", "type": "sub", "date": "World Records",
                        "children": [
                            {"label": "Highest: Mount Everest, Pamir Plateau (Tibet), Angel Falls (waterfall, Venezuela)", "type": "leaf"},
                            {"label": "Largest: Russia (area), India (population), Pacific Ocean, Sahara Desert; Deepest: Mariana Trench", "type": "leaf"},
                            {"label": "Longest: Nile river, Great Wall of China", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "International Organizations", "type": "branch", "date": "Global Bodies",
                "children": [
                    {
                        "label": "UN & Finance Institutions", "type": "sub", "date": "UN & Finance",
                        "children": [
                            {"label": "United Nations (UN): Established Oct 24, 1945; HQ: New York; ICJ at The Hague, Netherlands", "type": "leaf"},
                            {"label": "IMF & World Bank: Established 1944 (Bretton Woods); HQ: Washington D.C.; WTO: 1995 (Marrakesh); HQ: Geneva", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Regional & Specialized Bodies", "type": "sub", "date": "Regional & Others",
                        "children": [
                            {"label": "SAARC: 1985; HQ Kathmandu; ASEAN: 1967; HQ Jakarta; BRICS: Brazil, Russia, India, China, South Africa", "type": "leaf"},
                            {"label": "UNESCO: HQ Paris; WHO: HQ Geneva; INTERPOL: HQ Lyon (France); ADB: HQ Manila", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "National Symbols & Insignia", "type": "branch", "date": "National Pride",
                "children": [
                    {
                        "label": "Flag, Anthem & Song", "type": "sub", "date": "Symbols Core",
                        "children": [
                            {"label": "National Flag (Tiranga): Designed by Pingali Venkayya; adopted July 22, 1947; 3:2 ratio; 24-spoke Ashoka Chakra", "type": "leaf"},
                            {"label": "National Anthem (Jana Gana Mana): Tagore; sung 1911; adopted Jan 24, 1950; playing time 52 seconds", "type": "leaf"},
                            {"label": "National Song (Vande Mataram): Bankim Chandra Chatterjee in 'Anandamath'; adopted Jan 24, 1950", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Emblem & Calendar", "type": "sub", "date": "Emblem & Calendar",
                        "children": [
                            {"label": "State Emblem: Sarnath Lion Capital of Ashoka; adopted Jan 26, 1950; motto 'Satyameva Jayate' (Mundaka Upanishad)", "type": "leaf"},
                            {"label": "National Calendar: Based on Saka Era (starts 78 AD); adopted March 22, 1957; first month is Chaitra", "type": "leaf"}
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
    # We find "id="traps-section"" to inject the mindmap card after it
    if 'id="traps-section"' in html:
        pos = html.find('id="traps-section"')
        end_div = html.find('</div>', pos)
        if end_div != -1:
            insert_pos = end_div + len('</div>')
            html = html[:insert_pos] + "\n" + mindmap_card + "\n" + html[insert_pos:]
    elif '<!-- Prep Tracker -->' in html:
        html = html.replace('<!-- Prep Tracker -->', mindmap_card + '\n<!-- Prep Tracker -->', 1)
    else:
        # Fallback to checklist
        pos = html.find('Self-Evaluation Checklist')
        if pos != -1:
            card_pos = html.rfind('<div class="card-premium">', 0, pos)
            if card_pos != -1:
                html = html[:card_pos] + mindmap_card + "\n" + html[card_pos:]

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
