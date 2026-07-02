#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Socio-Religious-Reform-Movements"

MINDMAP_DATA = {
    "directions-of-reforms": {
        "en": [
            {"label": "Reformer Classes", "type": "branch", "date": "Two Directions", "children": [
                {"label": "Reformist Movements: Aimed at modifying social institutions from within; e.g., Brahmo Samaj, Prarthana Samaj, Aligarh Movement", "type": "leaf"},
                {"label": "Revivalist Movements: Aimed at reviving golden Vedic/Islamic traditions to counter Western hegemony; e.g., Arya Samaj, Deoband Movement", "type": "leaf"}]},
            {"label": "Core Aims", "type": "branch", "date": "Focus Areas", "children": [
                {"label": "Eradication of social inequalities, caste hierarchy, untouchability, and gender discrimination", "type": "leaf"},
                {"label": "Promotion of rationalism, scientific outlook, and humanism in religious beliefs", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सुधारक वर्ग", "type": "branch", "date": "दो दिशाएं", "children": [
                {"label": "सुधारवादी आंदोलन: सामाजिक संस्थाओं में भीतर से बदलाव लाना लक्ष्य था; जैसे ब्रह्म समाज, प्रार्थना समाज, अलीगढ़ आंदोलन", "type": "leaf"},
                {"label": "पुनरुत्थानवादी आंदोलन: पश्चिमी आधिपत्य का मुकाबला करने हेतु प्राचीन वैदिक/इस्लामी परंपराओं को पुनर्जीवित करना; जैसे आर्य समाज, देवबंद आंदोलन", "type": "leaf"}]},
            {"label": "मुख्य लक्ष्य", "type": "branch", "date": "प्रमुख क्षेत्र", "children": [
                {"label": "सामाजिक असमानताओं, जाति पदानुक्रम, अस्पृश्यता और लैंगिक भेदभाव का उन्मूलन", "type": "leaf"},
                {"label": "धार्मिक विश्वासों में तर्कवाद, वैज्ञानिक दृष्टिकोण और मानवतावाद को बढ़ावा देना", "type": "leaf"}]}
        ]
    },
    "factors-leading-to-reform": {
        "en": [
            {"label": "Western Influence", "type": "branch", "date": "External Factors", "children": [
                {"label": "Spread of English education introduced ideas of democracy, liberty, and rationalist philosophy", "type": "leaf"},
                {"label": "Christian missionary activities challenged traditional practices, forcing internal introspection", "type": "leaf"}]},
            {"label": "Internal Factors", "type": "branch", "date": "Local Awakening", "children": [
                {"label": "Rise of an educated Indian middle class seeking modernization of traditional society", "type": "leaf"},
                {"label": "Growth of print media and vernacular press highlighting social abuses and encouraging reform debates", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पश्चिमी प्रभाव", "type": "branch", "date": "बाहरी कारक", "children": [
                {"label": "अंग्रेजी शिक्षा के प्रसार ने लोकतंत्र, स्वतंत्रता और तर्कसंगत दर्शन के विचारों से परिचित कराया", "type": "leaf"},
                {"label": "ईसाई मिशनरी गतिविधियों ने पारंपरिक प्रथाओं को चुनौती दी, जिससे आंतरिक आत्म-निरीक्षण शुरू हुआ", "type": "leaf"}]},
            {"label": "आंतरिक कारक", "type": "branch", "date": "स्थानीय जागृति", "children": [
                {"label": "शिक्षित भारतीय मध्यम वर्ग का उदय जो पारंपरिक समाज का आधुनिकीकरण चाहता था", "type": "leaf"},
                {"label": "प्रिंट मीडिया और स्थानीय भाषाओं के प्रेस का विकास जिसने सामाजिक कुप्रथाओं को रेखांकित किया और सुधारों पर बहस को बढ़ावा दिया", "type": "leaf"}]}
        ]
    },
    "hindu-reform-movements": {
        "en": [
            {"label": "Brahmo Samaj", "type": "branch", "date": "1828", "children": [
                {"label": "Founded by Raja Rammohan Roy (Father of Indian Renaissance); worked for Sati abolition (1829 Regulation XVII)", "type": "leaf"},
                {"label": "Opposed idol worship, priesthood, polygamy; promoted monotheism & Upanishad study", "type": "leaf"},
                {"label": "Later splits: Adi Brahmo Samaj (Debendranath Tagore) and Brahmo Samaj of India (Keshub Chandra Sen)", "type": "leaf"}]},
            {"label": "Arya Samaj", "type": "branch", "date": "1875", "children": [
                {"label": "Founded by Swami Dayanand Saraswati (Mul Shankar) in Bombay; slogan: 'Go back to Vedas'", "type": "leaf"},
                {"label": "Published Satyarth Prakash; established DAV (Dayanand Anglo-Vedic) schools; started Shuddhi movement", "type": "leaf"}]},
            {"label": "Other Movements", "type": "branch", "date": "Regional", "children": [
                {"label": "Prarthana Samaj (1867): Founded by Atmaram Pandurang in Bombay; popularized by M.G. Ranade", "type": "leaf"},
                {"label": "Ramakrishna Mission (1897): Founded by Swami Vivekananda in Belur; advocated practical Vedanta & service to humanity", "type": "leaf"},
                {"label": "Young Bengal Movement (1820s-30s): Led by Henry Vivian Derozio; promoted radical free thought", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "ब्रह्म समाज", "type": "branch", "date": "1828", "children": [
                {"label": "राजा राममोहन राय (भारतीय पुनर्जागरण के जनक) द्वारा स्थापित; सती उन्मूलन (1829 नियमन XVII) हेतु कार्य किया", "type": "leaf"},
                {"label": "मूर्ति पूजा, पुरोहित वर्ग, बहुविवाह का विरोध; एकेश्वरवाद और उपनिषदों के अध्ययन को बढ़ावा दिया", "type": "leaf"},
                {"label": "बाद में विभाजन: आदि ब्रह्म समाज (देवेंद्रनाथ टैगोर) और भारतीय ब्रह्म समाज (केशव चंद्र सेन)", "type": "leaf"}]},
            {"label": "आर्य समाज", "type": "branch", "date": "1875", "children": [
                {"label": "बम्बई में स्वामी दयानंद सरस्वती (मूल शंकर) द्वारा स्थापित; नारा: 'वेदों की ओर लौटो'", "type": "leaf"},
                {"label": "सत्यार्थ प्रकाश का प्रकाशन; डीएवी (दयानंद एंग्लो-वैदिक) स्कूलों की स्थापना; शुद्धि आंदोलन चलाया", "type": "leaf"}]},
            {"label": "अन्य आंदोलन", "type": "branch", "date": "क्षेत्रीय", "children": [
                {"label": "प्रार्थना समाज (1867): बम्बई में आत्माराम पांडुरंग द्वारा स्थापित; एम.जी. रानाडे द्वारा लोकप्रिय बनाया गया", "type": "leaf"},
                {"label": "रामकृष्ण मिशन (1897): स्वामी विवेकानंद द्वारा बेलूर में स्थापित; व्यावहारिक वेदांत और मानव सेवा का प्रचार किया", "type": "leaf"},
                {"label": "यंग बंगाल आंदोलन (1820-30): हेनरी विवियन डेरोजियो के नेतृत्व में; कट्टरपंथी मुक्त विचारों को बढ़ावा दिया", "type": "leaf"}]}
        ]
    },
    "parsi-reform-movement": {
        "en": [
            {"label": "Sabha & Leaders", "type": "branch", "date": "1851", "children": [
                {"label": "Rahnumai Mazdayasnan Sabha (Religious Reform Association) founded in Bombay by Naoroji Furdonji, Dadabhai Naoroji, and S.S. Bengalee", "type": "leaf"},
                {"label": "Rast Goftar (Truth Teller) weekly journal launched to propagate reformist ideas", "type": "leaf"}]},
            {"label": "Aims & Impact", "type": "branch", "date": "Reforms", "children": [
                {"label": "Aimed at restoring Zoroastrianism to its original purity and removing orthodox social customs", "type": "leaf"},
                {"label": "Promoted modern education, especially for Parsi women, and initiated family reforms", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सभा और नेता", "type": "branch", "date": "1851", "children": [
                {"label": "बम्बई में नौरोजी फरदुनजी, दादाभाई नौरोजी और एस.एस. बंगाली द्वारा रहनुमाई माजदायसनन सभा की स्थापना", "type": "leaf"},
                {"label": "सुधारवादी विचारों के प्रचार-प्रसार हेतु 'रास्त गोफ्तार' (सत्यवादी) साप्ताहिक पत्रिका की शुरुआत", "type": "leaf"}]},
            {"label": "उद्देश्य और प्रभाव", "type": "branch", "date": "सुधार", "children": [
                {"label": "पारसी धर्म (जरथुस्त्र धर्म) को उसकी मूल शुद्धता में बहाल करना और रूढ़िवादी सामाजिक प्रथाओं को समाप्त करना", "type": "leaf"},
                {"label": "आधुनिक शिक्षा, विशेषकर पारसी महिलाओं के लिए, को बढ़ावा दिया और पारिवारिक सुधार शुरू किए", "type": "leaf"}]}
        ]
    },
    "reform-movements-among-muslims": {
        "en": [
            {"label": "Aligarh Movement", "type": "branch", "date": "Sir Syed Ahmed Khan", "children": [
                {"label": "Sir Syed Ahmed Khan founded MAO (Muhammadan Anglo-Oriental) College at Aligarh (1875), later AMU", "type": "leaf"},
                {"label": "Advocated modern western education; interpreted Quran rationally; opposed purdah and polygamy", "type": "leaf"},
                {"label": "Founded Scientific Society to translate western science works into Urdu", "type": "leaf"}]},
            {"label": "Deoband School", "type": "branch", "date": "Revivalist 1866", "children": [
                {"label": "Founded at Deoband (UP) by Muhammad Qasim Nanautavi and Rashid Ahmad Gangohi", "type": "leaf"},
                {"label": "Revivalist seminary focused on Quranic teaching and Islamic law; issued fatwas against western education", "type": "leaf"},
                {"label": "Supported Indian National Congress nationalist struggle against British rule", "type": "leaf"}]},
            {"label": "Ahmadiyya Movement", "type": "branch", "date": "Mirza Ghulam Ahmad", "children": [
                {"label": "Founded in 1889 by Mirza Ghulam Ahmad; based on liberal principles; emphasized human brotherhood", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अलीगढ़ आंदोलन", "type": "branch", "date": "सर सैयद अहमद खान", "children": [
                {"label": "सर सैयद अहमद खान ने अलीगढ़ में एमएओ कॉलेज (1875) की स्थापना की, जो बाद में अलीगढ़ मुस्लिम विश्वविद्यालय बना", "type": "leaf"},
                {"label": "आधुनिक पश्चिमी शिक्षा के पक्षधर; कुरान की तर्कसंगत व्याख्या की; पर्दा प्रथा और बहुविवाह का विरोध किया", "type": "leaf"},
                {"label": "पश्चिमी विज्ञान के कार्यों का उर्दू में अनुवाद करने हेतु साइंटिफिक सोसाइटी की स्थापना की", "type": "leaf"}]},
            {"label": "देवबंद स्कूल", "type": "branch", "date": "पुनरुत्थानवादी 1866", "children": [
                {"label": "मुहम्मद कासिम नानौतवी और राशिद अहमद गंगोही द्वारा देवबंद (यूपी) में स्थापित", "type": "leaf"},
                {"label": "कुरान की शिक्षाओं और इस्लामी कानून पर केंद्रित पुनरुत्थानवादी मदरसा; पश्चिमी शिक्षा के विरुद्ध फतवा जारी किया", "type": "leaf"},
                {"label": "ब्रिटिश शासन के खिलाफ भारतीय राष्ट्रीय कांग्रेस के राष्ट्रवादी संघर्ष का समर्थन किया", "type": "leaf"}]},
            {"label": "अहमदिया आंदोलन", "type": "branch", "date": "मिर्जा गुलाम अहमद", "children": [
                {"label": "1889 में मिर्जा गुलाम अहमद द्वारा स्थापित; उदारवादी सिद्धांतों पर आधारित; मानव बंधुत्व पर बल दिया", "type": "leaf"}]}
        ]
    },
    "sikh-reform-movement": {
        "en": [
            {"label": "Singh Sabha", "type": "branch", "date": "1873", "children": [
                {"label": "Singh Sabha Movement founded in Amritsar to counter Christian & Hindu proselytizing", "type": "leaf"},
                {"label": "Established Khalsa schools and colleges across Punjab to promote modern Punjabi education", "type": "leaf"}]},
            {"label": "Akali Movement", "type": "branch", "date": "1920s", "children": [
                {"label": "Gurdwara Reform Movement (Akali Movement) aimed to liberate Gurdwaras from corrupt Mahants", "type": "leaf"},
                {"label": "Led to passing of Sikh Gurdwaras Act 1925, giving SGPC (Shiromani Gurdwara Parbandhak Committee) democratic control over shrines", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सिंह सभा", "type": "branch", "date": "1873", "children": [
                {"label": "ईसाई और हिंदू धर्म परिवर्तन गतिविधियों का मुकाबला करने के लिए अमृतसर में सिंह सभा आंदोलन की स्थापना", "type": "leaf"},
                {"label": "आधुनिक पंजाबी शिक्षा को बढ़ावा देने के लिए पूरे पंजाब में खालसा स्कूलों और कॉलेजों की स्थापना की", "type": "leaf"}]},
            {"label": "अकाली आंदोलन", "type": "branch", "date": "1920 का दशक", "children": [
                {"label": "गुरुद्वारा सुधार आंदोलन (अकाली आंदोलन) का लक्ष्य गुरुद्वारों को भ्रष्ट महंतों के नियंत्रण से मुक्त कराना था", "type": "leaf"},
                {"label": "सिख गुरुद्वारा अधिनियम 1925 पारित होने का मार्ग प्रशस्त हुआ, जिससे SGPC को गुरुद्वारों का लोकतांत्रिक नियंत्रण मिला", "type": "leaf"}]}
        ]
    },
    "impact-and-significance": {
        "en": [
            {"label": "Social Impact", "type": "branch", "date": "Abolition of Evils", "children": [
                {"label": "Abolition of Sati (1829) and female infanticide; passing of Hindu Widow Remarriage Act 1856", "type": "leaf"},
                {"label": "Raised the minimum age of marriage for women (Age of Consent Act 1891, Child Marriage Restraint Act 1929)", "type": "leaf"}]},
            {"label": "National Awakening", "type": "branch", "date": "Nationalism", "children": [
                {"label": "Fostered self-respect and cultural confidence, countering British colonial theory of racial superiority", "type": "leaf"},
                {"label": "Created a secular and rational basis for the emerging national movement and political organizations", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सामाजिक प्रभाव", "type": "branch", "date": "कुप्रथाओं का अंत", "children": [
                {"label": "सती प्रथा (1829) और शिशु हत्या का उन्मूलन; हिंदू विधवा पुनर्विवाह अधिनियम 1856 का पारित होना", "type": "leaf"},
                {"label": "महिलाओं के विवाह की न्यूनतम आयु बढ़ाई गई (सहमति आयु अधिनियम 1891, बाल विवाह निषेध अधिनियम 1929)", "type": "leaf"}]},
            {"label": "राष्ट्रीय चेतना", "type": "branch", "date": "राष्ट्रवाद", "children": [
                {"label": "स्वाभिमान और सांस्कृतिक आत्मविश्वास को बढ़ावा दिया, जिससे नस्लीय श्रेष्ठता के ब्रिटिश औपनिवेशिक दावों का खंडन हुआ", "type": "leaf"},
                {"label": "उभरते हुए राष्ट्रीय आंदोलन और राजनीतिक संगठनों के लिए एक धर्मनिरपेक्ष और तर्कसंगत आधार तैयार किया", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "directions-of-reforms": "directions-of-reforms",
    "factors-leading-to-reform-movements": "factors-leading-to-reform",
    "hindu-reform-movements": "hindu-reform-movements",
    "parsi-reform-movement": "parsi-reform-movement",
    "reform-movements-among-muslims": "reform-movements-among-muslims",
    "sikh-reform-movement": "sikh-reform-movement",
    "impact-of-reform-movements": "impact-and-significance",
    "significance-of-reform-movements": "impact-and-significance"
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "directions-of-reforms")
    
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
