#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/art_and_culture/Pottery-Tradition"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'nbpw', 'pgw', 'ocp', 'brw'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'between', 'or']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Ochre Coloured Pottery
    if fl == 'ochre-coloured-pottery':
        if is_hindi:
            return [
                {"label": "कालखण्ड और विशेषताएँ", "type": "branch", "date": "~2000-1500 ई.पू.", "children": [
                    {"label": "गेरूआ रंग: नारंगी/लाल रंग का लेप, जो आसानी से हाथों में लग जाता है; कम पके और खुरदरे बर्तन", "type": "leaf"},
                    {"label": "गंगा-यमुना दोआब: ऊपरी घाटी में पाए गए; कृषि बस्तियों और शुरुआती पशुपालन के साक्ष्य प्रदान करते हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "OCP Chronology & Slip", "type": "branch", "date": "~2000-1500 BCE", "children": [
                    {"label": "Ochre wash: Features a powdery orange-red slip coating that rubs off on hands", "type": "leaf"},
                    {"label": "Stratigraphy: Serves as a transitional marker between Late Harappan and Early Vedic layers", "type": "leaf"}
                ]}
            ]

    # 2. Ochre Coloured Pottery OCP
    elif fl == 'ochre-coloured-pottery-ocp':
        if is_hindi:
            return [
                {"label": "ताम्र निधि संबंध और संरक्षण", "type": "branch", "date": "ताम्र निधि", "children": [
                    {"label": "ताम्र निधि: ओसीपी स्थलों पर तांबे की तलवारें, भाले और मानव जैसी आकृतियां (anthropomorphic figures) मिली हैं", "type": "leaf"},
                    {"label": "खराब संरक्षण: भूमिगत जलजमाव के कारण ये बर्तन अत्यधिक छिद्रयुक्त (porous) और कमजोर हो गए हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Copper Hoards & Water-logging", "type": "branch", "date": "OCP Detail", "children": [
                    {"label": "Copper Hoard overlap: Found together with flat celts, harpoons, and anthropomorphic bronze figures", "type": "leaf"},
                    {"label": "Porosity issues: Weathered, rolled, and fragile state caused by long exposure to acidic waterlogged silt", "type": "leaf"}
                ]}
            ]

    # 3. Black and Red Ware
    elif fl == 'black-and-red-ware':
        if is_hindi:
            return [
                {"label": "सांस्कृतिक प्रसार और शैली", "type": "branch", "date": "ताम्रपाषाण", "children": [
                    {"label": "अहार-बनास संस्कृति: ताम्रपाषाण कालीन राजस्थान (अहार) में मुख्य रूप से प्रयुक्त; लाल पृष्ठभूमि पर सफेद ज्यामितीय चित्र", "type": "leaf"},
                    {"label": "भौगोलिक फैलाव: गुजरात, मध्य भारत और पश्चिम बंगाल के ताम्रपाषाण स्थलों पर व्यापक रूप से पाए गए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Chalcolithic Context", "type": "branch", "date": "Chalcolithic", "children": [
                    {"label": "Ahar-Banas: Predominantly used in Rajasthan (Ahar culture) decorated with white paint outlines", "type": "leaf"},
                    {"label": "Distribution: Found in Central India, Gujarat, and Bengal chalcolithic sites as common kitchenware", "type": "leaf"}
                ]}
            ]

    # 4. Black and Red Ware BRW
    elif fl == 'black-and-red-ware-brw':
        if is_hindi:
            return [
                {"label": "उल्टी पकाई तकनीक", "type": "branch", "date": "तकनीक", "children": [
                    {"label": "उल्टी पकाई विधि: घड़े को भट्टी में उल्टा रखकर पकाया जाता था, जिससे ऑक्सीजन की कमी से अंदर का भाग काला और बाहर का भाग लाल हो जाता था", "type": "leaf"},
                    {"label": "महापाषाण (Megalithic) कब्र: दक्षिण भारत की कब्रों में बीआरडब्ल्यू बर्तन लोहे के औजारों के साथ पाए गए हैं", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Inverted Firing Metallurgy", "type": "branch", "date": "Firing", "children": [
                    {"label": "Inverted firing: Pots placed upside down in the kiln, resulting in a black interior and red exterior", "type": "leaf"},
                    {"label": "Megalithic association: Acted as primary grave goods in South Indian megaliths alongside early iron spears", "type": "leaf"}
                ]}
            ]

    # 5. Painted Grey Ware
    elif fl == 'painted-grey-ware':
        if is_hindi:
            return [
                {"label": "उत्तर वैदिक काल व कृषि", "type": "branch", "date": "लौह युग", "children": [
                    {"label": "लौह युग का विकास: उत्तरी भारत में कृषि विस्तार और लोहे के औजारों के बढ़ते प्रयोग के समकालीन", "type": "leaf"},
                    {"label": "महाभारत स्थल: हस्तिनापुर, कुरुक्षेत्र, अहिच्छत्र और जखेड़ा जैसे महत्वपूर्ण स्थलों पर पाए गए", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Iron Age & Agrarian Expansion", "type": "branch", "date": "Context", "children": [
                    {"label": "Agrarian transition: Coincides with clearing of Ganga forests and expansion of rice cultivation", "type": "leaf"},
                    {"label": "Mahabharata sites: Recovered from Hastinapur, Kurukshetra, and Mathura layers", "type": "leaf"}
                ]}
            ]

    # 6. Painted Grey Ware PGW
    elif fl == 'painted-grey-ware-pgw':
        if is_hindi:
            return [
                {"label": "तकनीकी श्रेष्ठता", "type": "branch", "date": "~1100-600 ई.पू.", "children": [
                    {"label": "विशेषताएँ: पतली दीवार वाले, अत्यंत महीन और हल्के भूरे रंग के उत्कृष्ट बर्तन; उच्च गुणवत्ता वाली मिट्टी से निर्मित", "type": "leaf"},
                    {"label": "चित्रकला: बर्तन की सतह पर काले रंग से सरल ज्यामितीय आकृतियां, संकेंद्रीय वृत्त (circles) और बिंदु बनाए जाते थे", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Technical Attributes & Designs", "type": "branch", "date": "PGW Detail", "children": [
                    {"label": "Thin-walled clay: Fine clay fired in a sealed reducing kiln to produce grey shade", "type": "leaf"},
                    {"label": "Geometrics: Painted with black geometric loops, dots, and concentric bands", "type": "leaf"}
                ]}
            ]

    # 7. Northern Black Polished Ware
    elif fl == 'northern-black-polished-ware':
        if is_hindi:
            return [
                {"label": "द्वितीय नगरीकरण का प्रतीक", "type": "branch", "date": "~600-200 ई.पू.", "children": [
                    {"label": "महाजनपद और मौर्य काल: शहरी समृद्धि और शासक वर्ग की विलासिता का प्रतीक (Elite Tableware)", "type": "leaf"},
                    {"label": "व्यापक व्यापार: उत्तरापथ (Uttarapatha) व्यापार मार्ग पर तक्षशिला, कौशाम्बी से लेकर बंगाल और दक्कन तक फैले", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Socioeconomic Context", "type": "branch", "date": "Context", "children": [
                    {"label": "Second Urbanization: Index ware for Mahajanapadas and the rise of organized cities", "type": "leaf"},
                    {"label": "Trade Networks: Traced along trade routes from Taxila to South India, proving luxury trade", "type": "leaf"}
                ]}
            ]

    # 8. Northern Black Polished Ware NBPW
    elif fl == 'northern-black-polished-ware-nbpw':
        if is_hindi:
            return [
                {"label": "दर्पण जैसी चमक और विज्ञान", "type": "branch", "date": "NBPW", "children": [
                    {"label": "चमकीली सतह: बर्तनों पर दर्पण जैसी चमकदार काली सतह; बहुत पतली मिट्टी से बने उत्कृष्ट थाली और कटोरे", "type": "leaf"},
                    {"label": "लौह अयस्क लेप: लोहे के तरल लेप (slip) के कारण पकाने के बाद बर्तन में धात्विक खनक और चमक आती है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Glossy Chemistry & Firing", "type": "branch", "date": "NBPW Detail", "children": [
                    {"label": "Mirror glaze: Glossy black slip produced by coating with iron-rich liquid clay and firing in reduction", "type": "leaf"},
                    {"label": "Deluxe tablewares: Exceptionally thin dishes and bowls, used as expensive prestige items", "type": "leaf"}
                ]}
            ]

    # 9. Glazed and Unglazed Pottery
    elif 'glazed' in fl:
        if is_hindi:
            return [
                {"label": "चमकदार (Glazed) पॉटरी का विकास", "type": "branch", "date": "मध्यकाल", "children": [
                    {"label": "इस्लामी प्रभाव: दिल्ली सल्तनत काल में भारत में ग्लेज़िंग तकनीक (कांच जैसी कोटिंग) लोकप्रिय हुई; नीले/हरे रंग", "type": "leaf"},
                    {"label": "खुर्जा व जयपुर ब्लू पॉटरी: रेत, मुल्तानी मिट्टी और कोबाल्ट/तांबा ऑक्साइड का उपयोग; बिना भट्टी की मिट्टी के बनते हैं", "type": "leaf"}
                ]},
                {"label": "बिना चमक वाले (Unglazed) क्षेत्रीय प्रकार", "type": "branch", "date": "लोक कला", "children": [
                    {"label": "अलवर की कागजी पॉटरी: अत्यंत पतली दीवार वाले दोहरे बर्तन, जो पानी को ठंडा रखने में मदद करते हैं", "type": "leaf"},
                    {"label": "निजामाबाद काली पॉटरी (UP): सरसों के तेल से चमकाए गए बर्तन, जिन पर जस्ता-रांगे की धातु से नक्काशी की जाती है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Medieval Glazed Ware Tradition", "type": "branch", "date": "Glazed", "children": [
                    {"label": "Islamic influence: Glazing techniques (vitreous coating using sand/oxides) popularized under Delhi Sultanate", "type": "leaf"},
                    {"label": "Blue Pottery (Jaipur): Uses quartz, glass, and sodium carbonate instead of clay, painted with cobalt blue", "type": "leaf"}
                ]},
                {"label": "Unglazed Regional Varieties", "type": "branch", "date": "Unglazed", "children": [
                    {"label": "Kagzi Pottery (Alwar): Exceptionally thin, double-walled pottery designed to facilitate cooling evaporation", "type": "leaf"},
                    {"label": "Nizamabad Black Ware: Polished with mustard oil and engraved with quicksilver-zinc amalgam designs", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "मृदभांड परंपरा सामान्य", "type": "branch", "date": "इतिहास", "children": [
                    {"label": "हड़प्पा काल से लेकर मध्यकाल तक मिट्टी के बर्तनों के प्रकारों का क्रमिक विकास", "type": "leaf"},
                    {"label": "मृदभांडों को पुरातत्वविदों द्वारा इतिहास का 'वर्णमाला' (Alphabet of Archaeology) माना जाता है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Pottery Tradition Overview", "type": "branch", "date": "Archaeology", "children": [
                    {"label": "Traces the chronological shift from Ochre Coloured (OCP) to Painted Grey (PGW) and NBPW wares", "type": "leaf"},
                    {"label": "Pottery acts as the primary tool for dating cultures and mapping trade routes in ancient India", "type": "leaf"}
                ]}
            ]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Normalize newlines
    html = html.replace('\r\n', '\n')

    # Remove any existing mindmap CSS/container/script tags
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n', '')
    
    # Match and clean existing interactive mindmap card
    mindmap_div_pattern = r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    
    # Match and clean existing mindmap engine script
    script_pattern = r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Get topic title from content.json if it exists
    folder_path = os.path.dirname(html_path)
    content_json_path = os.path.join(folder_path, "content.json")
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        parent_folder = os.path.dirname(folder_path)
        folder_name = os.path.basename(parent_folder)
        content_json_path = os.path.join(parent_folder, "hi", "content.json")
        if not os.path.exists(content_json_path):
            content_json_path = os.path.join(parent_folder, "content.json")

    clean_title = get_clean_title(folder_name)
    
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
        except Exception as e:
            print(f"  Error reading content.json: {e}")

    # Build unique mindmap data using refined keyword matching on the folder_name
    branches = get_custom_branches(folder_name, is_hindi)
    mindmap_data = {
        "label": clean_title,
        "type": "root",
        "children": branches
    }

    # Re-inject CSS link before closing </head>
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div before deep-dive-section
    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें — एक को खोलने पर दूसरे स्वतः बंद हो जाएंगे।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
        title_text = f"{topic_name} &mdash; Interactive Mindmap"

    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
'''
    
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback to Tab 1 notes panel
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script before </body>
    tree_json = json.dumps(mindmap_data)
    lang_str = "'hi'" if is_hindi else "'en'"
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, {lang_str});
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    # Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"  Successfully patched {html_path}")

def main():
    total_processed = 0
    for root, dirs, files in os.walk(BASE):
        rel_path = os.path.relpath(root, BASE)
        parts = rel_path.split(os.sep)
        
        is_hindi = False
        if 'hi' in parts:
            is_hindi = True
        
        for file in files:
            if file == "index.html":
                html_path = os.path.join(root, file)
                process_file(html_path, is_hindi)
                total_processed += 1
                
    print(f"\nDone! Patched {total_processed} files successfully.")

if __name__ == '__main__':
    main()
