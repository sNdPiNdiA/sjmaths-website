#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Evolution-of-Administrative-and-Police-Services"

MINDMAP_DATA = {
    "aitchison-committee": {
        "en": [
            {"label": "Structural Changes", "type": "branch", "date": "1886", "children": [
                {"label": "Aitchison Committee chaired by Sir Charles Aitchison; recommended dropping terms 'covenanted' & 'uncovenanted'", "type": "leaf"},
                {"label": "Proposed a three-tier system: Imperial Civil Service (held in England), Provincial Civil Service (held in India), and Subordinate Civil Service", "type": "leaf"},
                {"label": "Recommended increasing the maximum age limit for the civil services competitive exam to 23 years", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संरचनात्मक परिवर्तन", "type": "branch", "date": "1886", "children": [
                {"label": "सर चार्ल्स एचिसन की अध्यक्षता में गठित समिति; 'अनुबंधित' (covenanted) और 'गैर-अनुबंधित' शब्दों को हटाने की सिफारिश की", "type": "leaf"},
                {"label": "त्रि-स्तरीय प्रणाली का प्रस्ताव: इंपीरियल सिविल सर्विस (इंग्लैंड में परीक्षा), प्रांतीय सिविल सर्विस (भारत में परीक्षा) और अधीनस्थ सिविल सर्विस", "type": "leaf"},
                {"label": "सिविल सेवा प्रतियोगी परीक्षा में शामिल होने की अधिकतम आयु सीमा को बढ़ाकर 23 वर्ष करने की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "evolution-of-police-1791": {
        "en": [
            {"label": "Cornwallis Reforms", "type": "branch", "date": "1791", "children": [
                {"label": "Lord Cornwallis organized a regular police force, relieving Zamindars of their traditional policing duties", "type": "leaf"},
                {"label": "Created circles (Thanas) in districts, each headed by a Daroga (an Indian officer)", "type": "leaf"},
                {"label": "Established Superintendent of Police (SP) as head of district administration to manage the Darogas", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कार्नवालिस के सुधार", "type": "branch", "date": "1791", "children": [
                {"label": "लॉर्ड कार्नवालिस ने नियमित पुलिस बल का गठन किया, जमींदारों को उनके पारंपरिक पुलिसिंग कर्तव्यों से मुक्त किया", "type": "leaf"},
                {"label": "जिलों में पुलिस थानों (Thanas) की स्थापना की, प्रत्येक थाने का प्रमुख एक दारोगा (भारतीय अधिकारी) होता था", "type": "leaf"},
                {"label": "दारोगाओं के नियंत्रण और जिला पुलिस प्रशासन के प्रबंधन हेतु जिला स्तर पर पुलिस अधीक्षक (SP) का पद बनाया", "type": "leaf"}]}
        ]
    },
    "goi-act-1935": {
        "en": [
            {"label": "Public Service Commissions", "type": "branch", "date": "1935 Act", "children": [
                {"label": "Mandated establishment of Federal Public Service Commission at Center & Provincial Commissions in provinces", "type": "leaf"},
                {"label": "Safeguarded the terms of service, pay, and pensions of Secretary of State appointed civil servants", "type": "leaf"},
                {"label": "Divided administrative control of services between the federal center and autonomous provinces", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लोक सेवा आयोग", "type": "branch", "date": "1935 का अधिनियम", "children": [
                {"label": "केंद्र में संघीय लोक सेवा आयोग (FPSC) और प्रांतों में प्रांतीय लोक सेवा आयोगों (PPSC) की स्थापना अनिवार्य की", "type": "leaf"},
                {"label": "भारत सचिव (Secretary of State) द्वारा नियुक्त सिविल सेवकों की सेवा शर्तों, वेतन और पेंशन का संरक्षण किया", "type": "leaf"},
                {"label": "संघीय केंद्र और स्वायत्त प्रांतों के बीच प्रशासनिक सेवाओं के नियंत्रण को विभाजित किया", "type": "leaf"}]}
        ]
    },
    "civil-services-act-1861": {
        "en": [
            {"label": "Covenant Reservation", "type": "branch", "date": "1861", "children": [
                {"label": "Indian Civil Services Act 1861 reserved certain high-level administrative posts exclusively for covenanted officers", "type": "leaf"},
                {"label": "Mandated competitive exams be held only in London; medium was English with classical Greek & Latin test papers", "type": "leaf"},
                {"label": "Effectively restricted Indian entry into the higher civil services despite Queen's 1858 equal opportunity promise", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अनुबंधित पदों का आरक्षण", "type": "branch", "date": "1861", "children": [
                {"label": "भारतीय सिविल सेवा अधिनियम 1861 ने कुछ उच्च प्रशासनिक पदों को केवल अनुबंधित (Covenanted) अधिकारियों हेतु आरक्षित किया", "type": "leaf"},
                {"label": "प्रतियोगी परीक्षा केवल लंदन में आयोजित करने का प्रावधान; माध्यम अंग्रेजी था और प्रश्नपत्र ग्रीक व लैटिन भाषाओं पर आधारित थे", "type": "leaf"},
                {"label": "महारानी विक्टोरिया के 1858 के घोषणापत्र में दिए समान अवसर के वादे के बावजूद भारतीयों के प्रवेश को कठिन बनाया", "type": "leaf"}]}
        ]
    },
    "islington-commission": {
        "en": [
            {"label": "Indianization Proposals", "type": "branch", "date": "1912", "children": [
                {"label": "Islington Commission on Public Services recommended filling 25% of superior posts with Indians", "type": "leaf"},
                {"label": "Proposed recruitment should be conducted partly in England and partly in India to facilitate entry", "type": "leaf"},
                {"label": "Report was delayed due to WWI, rendering its proposals obsolete by the time of publication", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "भारतीयकरण के प्रस्ताव", "type": "branch", "date": "1912", "children": [
                {"label": "सार्वजनिक सेवाओं पर गठित इस्लिंगटन आयोग ने उच्च प्रशासनिक पदों के 25% हिस्से को भारतीयों से भरने की सिफारिश की", "type": "leaf"},
                {"label": "भारतीयों के प्रवेश को सुगम बनाने के लिए भर्ती परीक्षा आंशिक रूप से इंग्लैंड में और आंशिक रूप से भारत में आयोजित करने का सुझाव दिया", "type": "leaf"},
                {"label": "WWI के कारण रिपोर्ट के प्रकाशन में देरी हुई, जिससे प्रकाशन के समय तक इसकी सिफारिशें पुरानी हो चुकी थीं", "type": "leaf"}]}
        ]
    },
    "lee-commission": {
        "en": [
            {"label": "Recruitment Ratios", "type": "branch", "date": "1924", "children": [
                {"label": "Lee Commission addressed ethnic imbalances in superior civil services recruitment", "type": "leaf"},
                {"label": "Recommended 40% British recruits, 40% directly recruited Indians, and 20% promoted from provincial services", "type": "leaf"},
                {"label": "Urged immediate establishment of a Public Service Commission (duly formed in 1926 under Ross Barker)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "भर्ती का अनुपात", "type": "branch", "date": "1924", "children": [
                {"label": "ली आयोग ने उच्च सिविल सेवाओं में जातीय असंतुलन (ब्रिटिश बनाम भारतीय) को दूर करने का प्रयास किया", "type": "leaf"},
                {"label": "भविष्य की भर्ती में 40% ब्रिटिश, 40% सीधे भर्ती होने वाले भारतीय और 20% प्रांतीय सेवाओं से पदोन्नति का अनुपात सुझाया", "type": "leaf"},
                {"label": "एक लोक सेवा आयोग की तत्काल स्थापना का आग्रह किया (1926 में सर रॉस बार्कर के अधीन गठित हुआ)", "type": "leaf"}]}
        ]
    },
    "montford-reforms": {
        "en": [
            {"label": "Simultaneous Exams", "type": "branch", "date": "1919", "children": [
                {"label": "Recommended holding civil service recruitment exams simultaneously in London and India (started in Allahabad, 1922)", "type": "leaf"},
                {"label": "Proposed that 33% of superior posts be recruited in India, increasing by 1.5% annually", "type": "leaf"},
                {"label": "Created safeguards for public servants and protected them from political interference under Dyarchy", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "एक साथ परीक्षा", "type": "branch", "date": "1919", "children": [
                {"label": "लंदन और भारत में एक साथ सिविल सेवा परीक्षा आयोजित करने की सिफारिश की (1922 में इलाहाबाद में पहली बार शुरू)", "type": "leaf"},
                {"label": "उच्च पदों पर भारतीय भर्ती का प्रारंभिक प्रतिशत 33% रखने और इसे प्रतिवर्ष 1.5% बढ़ाने का प्रस्ताव दिया", "type": "leaf"},
                {"label": "द्वैध शासन के अंतर्गत लोक सेवकों की रक्षा के लिए सुरक्षा उपाय किए और उन्हें राजनीतिक हस्तक्षेप से दूर रखा", "type": "leaf"}]}
        ]
    },
    "police-commission-of-1860": {
        "en": [
            {"label": "Modern Hierarchy", "type": "branch", "date": "1860", "children": [
                {"label": "Police Commission of 1860 recommended a centralized, uniform police system across British India", "type": "leaf"},
                {"label": "Led to Indian Police Act 1861; created Inspector General (IG) at provincial level & Superintendent (SP) at district level", "type": "leaf"},
                {"label": "Established sub-inspector, head constable, and constable ranks, creating the modern police structure", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आधुनिक पदानुक्रम", "type": "branch", "date": "1860", "children": [
                {"label": "1860 के पुलिस आयोग ने पूरे ब्रिटिश भारत में एक समान, केंद्रीकृत पुलिस प्रणाली स्थापित करने की सिफारिश की", "type": "leaf"},
                {"label": "भारतीय पुलिस अधिनियम 1861 का मार्ग प्रशस्त किया; प्रांत में आईजी (IG) और जिले में एसपी (SP) का पद सृजित किया", "type": "leaf"},
                {"label": "उप-निरीक्षक, मुख्य आरक्षी (हेड कांस्टेबल) और आरक्षी (कांस्टेबल) के पदों का गठन कर आधुनिक ढांचा तैयार किया", "type": "leaf"}]}
        ]
    },
    "proclamation-of-1858": {
        "en": [
            {"label": "Crown Declarations", "type": "branch", "date": "1858", "children": [
                {"label": "Queen Victoria's Proclamation declared that Indians, irrespective of race or creed, could enter offices based on merit", "type": "leaf"},
                {"label": "Promised equal treatment and access to public services; however, covenanted posts remained out of reach", "type": "leaf"},
                {"label": "London-only examinations and high cost of travel acted as structural barriers for Indian applicants", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "महारानी की घोषणा", "type": "branch", "date": "1858", "children": [
                {"label": "महारानी विक्टोरिया के घोषणापत्र में कहा गया कि योग्यता के आधार पर भारतीयों को बिना किसी नस्लीय भेदभाव के सेवा का अधिकार होगा", "type": "leaf"},
                {"label": "सार्वजनिक सेवाओं में समान व्यवहार का वादा किया गया; हालांकि, अनुबंधित उच्च पद अभी भी पहुंच से बाहर रहे", "type": "leaf"},
                {"label": "केवल लंदन में परीक्षा का आयोजन और यात्रा की अत्यधिक लागत ने भारतीय आवेदकों के लिए बाधा का कार्य किया", "type": "leaf"}]}
        ]
    },
    "william-bentincks-contribution": {
        "en": [
            {"label": "Administrative Reforms", "type": "branch", "date": "1828-1835", "children": [
                {"label": "Lord William Bentinck reorganized judicial administration; abolished provincial courts of appeal and circuit courts", "type": "leaf"},
                {"label": "Appointed Indian judicial officers (Sadr Amins and Deputy Collectors) to reduce costs and administrative delays", "type": "leaf"},
                {"label": "Combined the offices of Collector and Magistrate, creating a centralized local executive head", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रशासनिक सुधार", "type": "branch", "date": "1828-1835", "children": [
                {"label": "लॉर्ड विलियम बेंटिक ने न्याय प्रशासन का पुनर्गठन किया; प्रांतीय अपील अदालतों और सर्किट अदालतों को समाप्त किया", "type": "leaf"},
                {"label": "लागत और प्रशासनिक विलंब को कम करने हेतु भारतीय न्यायिक अधिकारियों (सद्र अमीन और डिप्टी कलेक्टर) की नियुक्ति की", "type": "leaf"},
                {"label": "कलेक्टर और मजिस्ट्रेट के पदों को मिलाकर एक शक्तिशाली स्थानीय कार्यकारी प्रमुख का पद बनाया", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "aitchison-committee-on-public-services": "aitchison-committee",
    "aitchison-committee-on-public-services-1886": "aitchison-committee",
    "evolution-of-police-1791": "evolution-of-police-1791",
    "government-of-india-act-1935": "goi-act-1935",
    "indian-civil-services-act-1861": "civil-services-act-1861",
    "islington-commission": "islington-commission",
    "islington-commission-1912": "islington-commission",
    "lee-commission": "lee-commission",
    "lee-commission-1924": "lee-commission",
    "montford-reforms": "montford-reforms",
    "montford-reforms-1919": "montford-reforms",
    "police-commission-of-1860": "police-commission-of-1860",
    "proclamation-of-1858": "proclamation-of-1858",
    "william-bentincks-contribution": "william-bentincks-contribution"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('Montford', 'Montagu-Chelmsford')
    title = title.replace('Act 1935', 'Act (1935)')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "aitchison-committee")
    
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
