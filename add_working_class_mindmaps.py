#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Struggles-of-the-Working-Class"

MINDMAP_DATA = {
    "all-india-trade-union-congress": {
        "en": [
            {"label": "Foundation", "type": "branch", "date": "1920", "children": [
                {"label": "Established Oct 31, 1920 in Bombay; influenced by Russian Revolution (1917) and ILO formation (1919)", "type": "leaf"},
                {"label": "First President: Lala Lajpat Rai (declared: 'Militarism and capitalism are twin twin-born children of imperialism')", "type": "leaf"},
                {"label": "First General Secretary: Dewan Chaman Lall; Joseph Baptista was also co-founder", "type": "leaf"}]},
            {"label": "Later Developments", "type": "branch", "date": "Splits", "children": [
                {"label": "First Split (1929 Nagpur Session): Presided by Jawaharlal Nehru; reformists left to form Indian Trades Union Federation (ITUF)", "type": "leaf"},
                {"label": "Red Trade Union Congress (RTUC) split in 1931 under communist influence", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थापना", "type": "branch", "date": "1920", "children": [
                {"label": "31 अक्टूबर 1920 को बॉम्बे में स्थापना; रूसी क्रांति (1917) और आईएलओ (1919) के गठन का गहरा प्रभाव", "type": "leaf"},
                {"label": "प्रथम अध्यक्ष: लाला लाजपत राय (घोषणा की: 'सैन्यवाद और पूंजीवाद साम्राज्यवाद की जुड़वां संतानें हैं')", "type": "leaf"},
                {"label": "प्रथम महासचिव: दीवान चमन लाल; जोसेफ बैप्टिस्टा भी सह-संस्थापक थे", "type": "leaf"}]},
            {"label": "परवर्ती विकास", "type": "branch", "date": "विभाजन", "children": [
                {"label": "प्रथम विभाजन (1929 नागपुर सत्र): जवाहरलाल नेहरू की अध्यक्षता; सुधारवादियों ने अलग होकर 'इंडियन ट्रेड यूनियन फेडरेशन' (ITUF) बनाया", "type": "leaf"},
                {"label": "1931 में साम्यवादी प्रभाव के कारण 'रेड ट्रेड यूनियन कांग्रेस' (RTUC) का गठन", "type": "leaf"}]}
        ]
    },
    "initial-efforts-for-working-classs-conditions": {
        "en": [
            {"label": "Early Philanthropists", "type": "branch", "date": "Pre-1900", "children": [
                {"label": "Sasipada Banerji: Baranagar Institute (1870); published first labor journal 'Bharat Shramjeevi'", "type": "leaf"},
                {"label": "Sorabjee Shapoorji Bengalee: Advocated labor bills in Bombay Legislative Council", "type": "leaf"},
                {"label": "N.M. Lokhande: Founded Bombay Millhands Association (1890) & journal 'Dinabandhu'; Father of Trade Union Movement", "type": "leaf"}]},
            {"label": "First Factory Act (1881)", "type": "branch", "date": "Ripon", "children": [
                {"label": "Enacted under Lord Ripon; focused primarily on child labor regulation", "type": "leaf"},
                {"label": "Prohibited employment of children under 7; limited 7-12 age group to 9 hours of work per day with 4 holidays/month", "type": "leaf"}]},
            {"label": "Second Factory Act (1891)", "type": "branch", "date": "Lansdowne", "children": [
                {"label": "Enacted under Lord Lansdowne; focused on female labor welfare", "type": "leaf"},
                {"label": "Limited women's working hours to 11 hours per day with a 1.5-hour midday interval; weekly off introduced", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक परोपकारी प्रयास", "type": "branch", "date": "1900 से पूर्व", "children": [
                {"label": "शशिपाद बनर्जी: बारानागर संस्थान (1870) की स्थापना; पहले श्रम समाचार पत्र 'भारत श्रमजीवी' का प्रकाशन", "type": "leaf"},
                {"label": "सोराबजी शपूरजी बंगाली: बॉम्बे विधान परिषद में श्रम विधेयकों के समर्थन में आवाज उठाई", "type": "leaf"},
                {"label": "एन.एम. लोखंडे: बॉम्बे मिलहैंड्स एसोसिएशन (1890) और 'दीनबंधु' पत्र के संस्थापक; भारतीय श्रम आंदोलन के जनक", "type": "leaf"}]},
            {"label": "प्रथम कारखाना अधिनियम (1881)", "type": "branch", "date": "रिपन", "children": [
                {"label": "लॉर्ड रिपन के कार्यकाल में पारित; मुख्य रूप से बाल श्रम के नियमन पर केंद्रित", "type": "leaf"},
                {"label": "7 वर्ष से कम आयु के बच्चों के नियोजन पर रोक; 7-12 वर्ष के बच्चों के लिए 9 घंटे कार्यसीमा और 4 दिन की मासिक छुट्टी", "type": "leaf"}]},
            {"label": "द्वितीय कारखाना अधिनियम (1891)", "type": "branch", "date": "लैंसडाउन", "children": [
                {"label": "लॉर्ड लैंसडाउन के कार्यकाल में पारित; महिला श्रम कल्याण पर केंद्रित", "type": "leaf"},
                {"label": "महिला कामगारों के लिए कार्यसीमा 11 घंटे प्रतिदिन तय; दोपहर में 1.5 घंटे का विश्राम और साप्ताहिक अवकाश अनिवार्य", "type": "leaf"}]}
        ]
    },
    "meerut-conspiracy-case-1929": {
        "en": [
            {"label": "The Crackdown", "type": "branch", "date": "March 1929", "children": [
                {"label": "Arrest of 31 labor leaders & communists (including English activists Philip Spratt, Ben Bradley, Lester Hutchinson)", "type": "leaf"},
                {"label": "Accused of conspiring to deprive the British King Emperor of sovereignty over India", "type": "leaf"}]},
            {"label": "Defense & Support", "type": "branch", "date": "Solidarity", "children": [
                {"label": "Central Defense Committee formed by Congress (Motilal Nehru, Jawaharlal Nehru, M.C. Chagla defended them)", "type": "leaf"},
                {"label": "Attracted global support; figures like Albert Einstein, Romain Rolland, and H.G. Wells supported the accused", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दमनकारी कार्रवाई", "type": "branch", "date": "मार्च 1929", "children": [
                {"label": "31 श्रमिक नेताओं और कम्युनिस्टों की गिरफ्तारी (ब्रिटिश कार्यकर्ता फिलिप स्प्रैट, बेन ब्रेडले, लेस्टर हचिंसन शामिल)", "type": "leaf"},
                {"label": "ब्रिटिश सम्राट को भारत की संप्रभुता से वंचित करने के षड्यंत्र का आरोप", "type": "leaf"}]},
            {"label": "बचाव और वैश्विक समर्थन", "type": "branch", "date": "एकजुटता", "children": [
                {"label": "कांग्रेस द्वारा केंद्रीय रक्षा समिति का गठन (मोतीलाल नेहरू, जवाहरलाल नेहरू, एम.सी. छागला ने वकालत की)", "type": "leaf"},
                {"label": "वैश्विक स्तर पर ध्यान आकर्षित किया; अल्बर्ट आइंस्टीन, रोमेन रोलैंड और एच.जी. वेल्स ने आरोपियों के पक्ष में बयान दिए", "type": "leaf"}]}
        ]
    },
    "trade-union-act-1926": {
        "en": [
            {"label": "Legal Status", "type": "branch", "date": "Act of 1926", "children": [
                {"label": "Provided a system for registration of trade unions and granted them legal corporate personality", "type": "leaf"},
                {"label": "Immunity granted to registered unions from civil and criminal prosecution for genuine trade union activities", "type": "leaf"}]},
            {"label": "Conditions", "type": "branch", "date": "Rules", "children": [
                {"label": "At least 50% of the executive committee members must be actively engaged in the relevant industry", "type": "leaf"},
                {"label": "Prevented general funds from being spent on political activities unless a separate political fund was created", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कानूनी दर्जा", "type": "branch", "date": "1926 का अधिनियम", "children": [
                {"label": "ट्रेड यूनियनों के पंजीकरण के लिए एक प्रणाली प्रदान की और उन्हें कानूनी दर्जा दिया", "type": "leaf"},
                {"label": "पंजीकृत यूनियनों को वैध गतिविधियों के लिए दीवानी और आपराधिक कानूनी कार्रवाइयों से छूट प्रदान की", "type": "leaf"}]},
            {"label": "शर्तें", "type": "branch", "date": "नियम", "children": [
                {"label": "कार्यकारी समिति के कम से कम 50% सदस्यों का संबंधित उद्योग से प्रत्यक्ष जुड़ाव होना अनिवार्य", "type": "leaf"},
                {"label": "राजनीतिक गतिविधियों के लिए सामान्य कोष के उपयोग पर प्रतिबंध; पृथक राजनीतिक कोष की अनुमति", "type": "leaf"}]}
        ]
    },
    "trade-disputes-act-1929": {
        "en": [
            {"label": "Provisions", "type": "branch", "date": "Act of 1929", "children": [
                {"label": "Made establishment of Courts of Inquiry and Conciliation Boards compulsory for settling industrial disputes", "type": "leaf"},
                {"label": "Declared strikes in public utility services (railways, post, electricity) illegal without 14 days' prior notice", "type": "leaf"}]},
            {"label": "Bans & Political Context", "type": "branch", "date": "Controversy", "children": [
                {"label": "Forbade sympathetic strikes and lockouts; banned political strikes", "type": "leaf"},
                {"label": "Passed alongside Public Safety Bill; led to Bhagat Singh throwing bombs in Central Assembly (April 1929) in protest", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रावधान", "type": "branch", "date": "1929 का अधिनियम", "children": [
                {"label": "औद्योगिक विवादों के निपटारे हेतु जांच अदालतों और सुलह बोर्डों की स्थापना अनिवार्य की", "type": "leaf"},
                {"label": "जनोपयोगी सेवाओं (रेलवे, डाक, बिजली, पानी) में बिना 14 दिन के पूर्व नोटिस के हड़ताल को अवैध घोषित किया", "type": "leaf"}]},
            {"label": "प्रतिबंध और राजनीतिक संदर्भ", "type": "branch", "date": "विवाद", "children": [
                {"label": "सहानुभूतिपूर्ण हड़तालों और तालाबंदी पर प्रतिबंध लगाया; राजनीतिक हड़तालों को अवैध घोषित किया", "type": "leaf"},
                {"label": "पब्लिक सेफ्टी बिल के साथ पारित किया गया; जिसके विरोध में भगत सिंह और बटुकेश्वर दत्त ने केंद्रीय असेंबली में बम फेंका", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "all-india-trade-union-congress": "all-india-trade-union-congress",
    "all-india-trade-union-congress-aituc": "all-india-trade-union-congress",
    "initial-efforts-for-working-classs-conditions": "initial-efforts-for-working-classs-conditions",
    "meerut-conspiracy-case": "meerut-conspiracy-case-1929",
    "meerut-conspiracy-case-1929": "meerut-conspiracy-case-1929",
    "trade-disputes-act-1929": "trade-disputes-act-1929",
    "trade-union-act-1926": "trade-union-act-1926"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def ensure_base_html(path, folder_name):
    if os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    clean_title = get_clean_title(folder_name)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{clean_title} - UPSC Civil Services Study Guide | SJMaths</title>
</head>
<body>
    <!-- Interactive Mindmap -->
</body>
</html>
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_hi_stub(en_html_path, hi_html_path, folder_name):
    if not os.path.exists(en_html_path):
        ensure_base_html(en_html_path, folder_name)
        
    with open(en_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)
    
    clean_title = get_clean_title(folder_name)
    if '<title>' in html:
        html = re.sub(r'<title>[^<]+</title>',
                      f'<title>{clean_title} (Hindi) - UPSC Civil Services Study Guide | SJMaths</title>',
                      html, count=1)
    
    os.makedirs(os.path.dirname(hi_html_path), exist_ok=True)
    with open(hi_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def inject_mindmap(html_path, folder_name, lang):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')

    # Remove any old mindmap links/scripts
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, key)
    
    branches = MINDMAP_DATA.get(canonical_key, {}).get(lang, [])
    if not branches:
        branches = [{"label": clean_title, "type": "branch", "date": "Topic", "children": [{"label": "Information structured here for UPSC", "type": "leaf"}]}]
        
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html and '<head>' in html:
        html = html.replace('</head>', css_link + '</head>')

    if lang == 'hi':
        instr = 'किसी कार्ड पर क्लिक करें।'
        title_text = f"{clean_title} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Click any card to expand or collapse.'
        title_text = f"{clean_title} &mdash; Interactive Mindmap"

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
    if re.search(r'<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">', html):
        html = re.sub(r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)', mindmap_card + r'\1', html)
    elif '<div class="tab-panel active" id="notes-panel" role="tabpanel"' in html:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        html = html.replace(marker, marker + '\n' + mindmap_card, 1)
    elif '<body>' in html:
        html = html.replace('<body>', '<body>\n' + mindmap_card, 1)

    tree_json = json.dumps(mindmap_data, ensure_ascii=False)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, '{lang}');
    </script>
'''
    if '</body>' in html:
        html = html.replace('</body>', inline_script + '\n</body>')
    else:
        html += inline_script

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    total_en = 0
    total_hi = 0
    
    if not os.path.exists(BASE_DIR):
        print(f"Directory {BASE_DIR} does not exist.")
        return

    for root_dir, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d != 'hi']
        folder_name = os.path.basename(root_dir)
        
        if root_dir == BASE_DIR:
            continue

        en_path = os.path.join(root_dir, 'index.html')
        hi_dir = os.path.join(root_dir, 'hi')
        hi_path = os.path.join(hi_dir, 'index.html')

        ensure_base_html(en_path, folder_name)
        inject_mindmap(en_path, folder_name, 'en')
        total_en += 1

        if not os.path.exists(hi_path):
            create_hi_stub(en_path, hi_path, folder_name)

        inject_mindmap(hi_path, folder_name, 'hi')
        total_hi += 1
        
        print(f"Processed: {folder_name}")

    print(f"\nCreated+patched {total_en} English and {total_hi} Hindi pages.")

if __name__ == '__main__':
    main()
