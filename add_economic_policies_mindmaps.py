#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Economic-Policies-of-The-British"

MINDMAP_DATA = {
    "revenue-terms": {
        "en": [
            {"label": "Revenue Intermediaries", "type": "branch", "date": "Terminology", "children": [
                {"label": "Lathiyals: Armed guards hired by Zamindars to forcefully collect rent and silence peasant protests", "type": "leaf"},
                {"label": "Gomastas: Paid native agents of EIC who supervised weavers and secured supply contracts", "type": "leaf"},
                {"label": "Jotedars: Wealthy peasants in Bengal who owned large lands and controlled local grain trade and lending", "type": "leaf"}]},
            {"label": "Regulatory Terms", "type": "branch", "date": "Terminology", "children": [
                {"label": "Patni System: Sub-infeudation system where Zamindars leased parts of their estate to sub-landlords", "type": "leaf"},
                {"label": "Sunset Law: Clause in Permanent Settlement requiring revenue deposition by sunset of the due date", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजस्व मध्यस्थ", "type": "branch", "date": "शब्दावली", "children": [
                {"label": "लाठियाल: जमींदारों द्वारा जबरन किराया वसूलने और किसान विरोध को दबाने के लिए नियुक्त लठैत", "type": "leaf"},
                {"label": "गुमाश्ता: EIC के वेतनभोगी एजेंट जो बुनकरों की निगरानी करते थे और आपूर्ति अनुबंध हासिल करते थे", "type": "leaf"},
                {"label": "जोतदार: बंगाल में अमीर किसान जिनके पास बड़ी जमीनें थीं और वे स्थानीय अनाज व्यापार व साहूकारी को नियंत्रित करते थे", "type": "leaf"}]},
            {"label": "नियामक शर्तें", "type": "branch", "date": "शब्दावली", "children": [
                {"label": "पटनी प्रणाली: उप-जमींदारी व्यवस्था जहां जमींदार अपनी संपत्ति के कुछ हिस्से उप-जमींदारों को पट्टे पर देते थे", "type": "leaf"},
                {"label": "सूर्यास्त कानून: स्थायी बंदोबस्त में नियत तारीख के सूर्यास्त तक राजस्व जमा करने की अनिवार्य शर्त", "type": "leaf"}]}
        ]
    },
    "finance-imperialism": {
        "en": [
            {"label": "Characteristics of Phase", "type": "branch", "date": "1858-1947", "children": [
                {"label": "Started post-1857; focused on exporting British capital to India rather than importing Indian goods", "type": "leaf"},
                {"label": "Search for secure high-interest investment avenues for surplus capital accumulated in Britain", "type": "leaf"}]},
            {"label": "Key Fields of Investment", "type": "branch", "date": "1858-1947", "children": [
                {"label": "Railways: Main focus with a guaranteed 5% interest rate paid from Indian taxes (private risk at public expense)", "type": "leaf"},
                {"label": "Municipal loans, government debt, coal mines, jute mills, tea/coffee plantations, and shipping", "type": "leaf"}]},
            {"label": "Colonial Control", "type": "branch", "date": "1858-1947", "children": [
                {"label": "Financial institutions and exchange banks remained under British monopoly to control local credit", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "इस चरण की विशेषताएं", "type": "branch", "date": "1858-1947", "children": [
                {"label": "1857 के बाद शुरू हुआ; भारतीय वस्तुओं के आयात के बजाय भारत में ब्रिटिश पूंजी के निर्यात पर ध्यान केंद्रित किया", "type": "leaf"},
                {"label": "ब्रिटेन में संचित अधिशेष पूंजी के लिए सुरक्षित उच्च-ब्याज निवेश मार्गों की खोज की गई", "type": "leaf"}]},
            {"label": "निवेश के प्रमुख क्षेत्र", "type": "branch", "date": "1858-1947", "children": [
                {"label": "रेलवे: भारतीय करों से भुगतान की जाने वाली 5% गारंटीकृत ब्याज दर के साथ मुख्य फोकस (सार्वजनिक खर्च पर निजी उद्यम)", "type": "leaf"},
                {"label": "नगर पालिका ऋण, सरकारी ऋण, कोयला खदानें, जूट मिलें, चाय/कॉफी बागान और नौवहन", "type": "leaf"}]},
            {"label": "औपनिवेशिक नियंत्रण", "type": "branch", "date": "1858-1947", "children": [
                {"label": "स्थानीय ऋण को नियंत्रित करने के लिए वित्तीय संस्थान और एक्सचेंज बैंक ब्रिटिश एकाधिकार के अधीन रहे", "type": "leaf"}]}
        ]
    },
    "free-trade": {
        "en": [
            {"label": "Ideological Foundations", "type": "branch", "date": "1813-1858", "children": [
                {"label": "Influenced by Adam Smith's laissez-faire and the rise of British industrial capitalists challenging EIC monopoly", "type": "leaf"},
                {"label": "Charter Act of 1813 ended EIC's trade monopoly in India (except tea and China trade)", "type": "leaf"}]},
            {"label": "De-industrialization Policy", "type": "branch", "date": "1813-1858", "children": [
                {"label": "One-way free trade: British machine-made textiles imported at nominal duties while Indian exports faced high tariffs", "type": "leaf"},
                {"label": "Transformed India from an exporter of processed textiles into a raw material exporter (cotton, silk) and finished goods importer", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "वैचारिक आधार", "type": "branch", "date": "1813-1858", "children": [
                {"label": "एडम स्मिथ के मुक्त व्यापार (laissez-faire) और EIC एकाधिकार को चुनौती देने वाले ब्रिटिश उद्योगपतियों के उदय से प्रभावित", "type": "leaf"},
                {"label": "1813 के चार्टर अधिनियम ने भारत में EIC के व्यापारिक एकाधिकार को समाप्त कर दिया (चाय और चीन व्यापार को छोड़कर)", "type": "leaf"}]},
            {"label": "वि-औद्योगिकीकरण की नीति", "type": "branch", "date": "1813-1858", "children": [
                {"label": "एकतरफा मुक्त व्यापार: ब्रिटिश निर्मित कपड़े मामूली शुल्क पर आयातित, जबकि भारतीय निर्यात पर भारी सीमा शुल्क था", "type": "leaf"},
                {"label": "भारत को प्रसंस्कृत वस्त्रों के निर्यातक से कच्चे माल (कपास, रेशम) के निर्यातक और तैयार माल के आयातक में बदल दिया", "type": "leaf"}]}
        ]
    },
    "mercantilism": {
        "en": [
            {"label": "Monopoly Trade", "type": "branch", "date": "1757-1813", "children": [
                {"label": "Focused on EIC's monopoly of trade, acquiring goods at low prices and selling them in Europe at high margins", "type": "leaf"},
                {"label": "Used Bengal's surplus revenues ('investments') to purchase Indian export goods, ending inflow of British bullion", "type": "leaf"}]},
            {"label": "Political Annexations", "type": "branch", "date": "1757-1813", "children": [
                {"label": "Combined trade with territorial conquests (Bengal, Mysore, Carnatic) to secure administrative revenues", "type": "leaf"},
                {"label": "Excluded European rival trading companies (French, Dutch) through military victories and treaty alliances", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "एकाधिकार व्यापार", "type": "branch", "date": "1757-1813", "children": [
                {"label": "EIC के व्यापार एकाधिकार पर ध्यान केंद्रित, कम कीमतों पर सामान खरीदना और यूरोप में उच्च मार्जिन पर बेचना", "type": "leaf"},
                {"label": "ब्रिटिश बुलियन (सोने-चांदी) के प्रवाह को समाप्त कर भारतीय निर्यात माल खरीदने हेतु बंगाल के अधिशेष राजस्व का उपयोग किया", "type": "leaf"}]},
            {"label": "राजनीतिक विलय", "type": "branch", "date": "1757-1813", "children": [
                {"label": "प्रशासनिक राजस्व सुरक्षित करने के लिए क्षेत्रीय विजयों (बंगाल, मैसूर, कर्नाटक) के साथ व्यापार को जोड़ा", "type": "leaf"},
                {"label": "सैन्य जीत और संधि गठबंधनों के माध्यम से यूरोपीय प्रतिद्वंद्वी व्यापारिक कंपनियों (फ्रांसीसी, डच) को बाहर कर दिया", "type": "leaf"}]}
        ]
    },
    "drain-of-wealth": {
        "en": [
            {"label": "Nationalist Exposure", "type": "branch", "date": "Drain Theory", "children": [
                {"label": "Exposed by Dadabhai Naoroji in 1867 paper; popularized by R.C. Dutt and Dinshaw Wacha", "type": "leaf"},
                {"label": "Highlighted that a large part of India's national wealth was sent to England without any equivalent return", "type": "leaf"}]},
            {"label": "Components of Drain", "type": "branch", "date": "Drain Theory", "children": [
                {"label": "Home Charges: India Office expenses in London, pensions of civil/military officers", "type": "leaf"},
                {"label": "Guaranteed interest on British investments (railways), military expenditure for overseas wars, and private remittances", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राष्ट्रवादी प्रकटीकरण", "type": "branch", "date": "धन निकासी का सिद्धांत", "children": [
                {"label": "1867 के शोधपत्र में दादाभाई नौरोजी द्वारा उजागर किया गया; आर.सी. दत्त और दिनशा वाचा द्वारा लोकप्रिय बनाया गया", "type": "leaf"},
                {"label": "इस बात पर प्रकाश डाला कि भारत की राष्ट्रीय संपत्ति का एक बड़ा हिस्सा बिना किसी समकक्ष रिटर्न के इंग्लैंड भेजा जाता था", "type": "leaf"}]},
            {"label": "निकासी के घटक", "type": "branch", "date": "धन निकासी का सिद्धांत", "children": [
                {"label": "गृह प्रभार: लंदन में इंडिया ऑफिस के खर्च, सिविल/सैन्य अधिकारियों की पेंशन", "type": "leaf"},
                {"label": "ब्रिटिश निवेश (रेलवे) पर गारंटीकृत ब्याज, विदेशी युद्धों के लिए सैन्य खर्च और निजी प्रेषण (remittances)", "type": "leaf"}]}
        ]
    },
    "general-impact": {
        "en": [
            {"label": "Structural Impoverishment", "type": "branch", "date": "Economic Impact", "children": [
                {"label": "De-industrialization of traditional textile centers (Dacca, Murshidabad) causing massive urban-to-rural migration", "type": "leaf"},
                {"label": "Extreme pressure on land leading to fragmentation of agricultural holdings and rural landlessness", "type": "leaf"}]},
            {"label": "Stagnant Agriculture", "type": "branch", "date": "Economic Impact", "children": [
                {"label": "Recurrent devastating famines due to lack of public works investment (except railways) and high taxation", "type": "leaf"},
                {"label": "Chronic agrarian debt due to integration of local crops with volatile global markets", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "ढांचागत दरिद्रता", "type": "branch", "date": "आर्थिक प्रभाव", "children": [
                {"label": "पारंपरिक कपड़ा केंद्रों (ढाका, मुर्शिदाबाद) के वि-औद्योगिकीकरण के कारण बड़े पैमाने पर शहरी से ग्रामीण पलायन हुआ", "type": "leaf"},
                {"label": "भूमि पर अत्यधिक दबाव बढ़ा जिससे कृषि जोतों का विखंडन हुआ और ग्रामीण भूमिहीनता बढ़ी", "type": "leaf"}]},
            {"label": "ठहरावग्रस्त कृषि", "type": "branch", "date": "आर्थिक प्रभाव", "children": [
                {"label": "सार्वजनिक कार्यों के निवेश की कमी (रेलवे को छोड़कर) और उच्च कराधान के कारण बार-बार विनाशकारी अकाल पड़े", "type": "leaf"},
                {"label": "अस्थिर वैश्विक बाजारों के साथ स्थानीय फसलों के एकीकरण के कारण क्रोनिक कृषि ऋणग्रस्तता उत्पन्न हुई", "type": "leaf"}]}
        ]
    },
    "mahalwari": {
        "en": [
            {"label": "Core Features", "type": "branch", "date": "Mahalwari", "children": [
                {"label": "Introduced by Holt Mackenzie (1822) and reformed by William Bentinck / James Thomason (1833)", "type": "leaf"},
                {"label": "Implemented in Punjab, North-West Provinces, and Central India, covering about 30% of British India's land", "type": "leaf"}]},
            {"label": "Assessment & Collection", "type": "branch", "date": "Mahalwari", "children": [
                {"label": "Revenue assessed on the basis of the entire village community ('Mahal') rather than individual peasants", "type": "leaf"},
                {"label": "Village headman ('Lambaradar') held responsibility for collecting and depositing the revenue", "type": "leaf"}]},
            {"label": "Impact", "type": "branch", "date": "Mahalwari", "children": [
                {"label": "High state demand (initially up to 66% of rental value) led to land sales and sub-infeudation", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य विशेषताएं", "type": "branch", "date": "महलवाड़ी", "children": [
                {"label": "होल्ट मैकेंजी (1822) द्वारा शुरू की गई और विलियम बेंटिक / जेम्स थॉमसन (1833) द्वारा संशोधित की गई", "type": "leaf"},
                {"label": "पंजाब, उत्तर-पश्चिम प्रांतों और मध्य भारत में लागू की गई, जिसने ब्रिटिश भारत की लगभग 30% भूमि को कवर किया", "type": "leaf"}]},
            {"label": "मूल्यांकन और संग्रह", "type": "branch", "date": "महलवाड़ी", "children": [
                {"label": "राजस्व का मूल्यांकन व्यक्तिगत किसानों के बजाय पूरे ग्राम समुदाय ('महल') के आधार पर किया जाता था", "type": "leaf"},
                {"label": "ग्राम प्रधान ('लंबरदार') के पास राजस्व वसूलने और जमा करने की जिम्मेदारी थी", "type": "leaf"}]},
            {"label": "प्रभाव", "type": "branch", "date": "महलवाड़ी", "children": [
                {"label": "उच्च राज्य मांग (शुरू में किराये के मूल्य का 66% तक) के कारण भूमि की बिक्री और उप-पट्टेदारी बढ़ी", "type": "leaf"}]}
        ]
    },
    "permanent-settlement": {
        "en": [
            {"label": "Core Features", "type": "branch", "date": "Permanent", "children": [
                {"label": "Introduced by Lord Cornwallis in 1793 in Bengal, Bihar, Orissa, and Northern Circars (19% of British India)", "type": "leaf"},
                {"label": "Zamindars recognized as absolute owners of land; revenue demand fixed permanently", "type": "leaf"}]},
            {"label": "Assessment & Sharing", "type": "branch", "date": "Permanent", "children": [
                {"label": "Share of collection: 10/11th to EIC, and 1/11th retained by the Zamindar", "type": "leaf"},
                {"label": "Sunset Law: Zamindars lost ownership if revenue was not paid by sunset of the specified date", "type": "leaf"}]},
            {"label": "Impact", "type": "branch", "date": "Permanent", "children": [
                {"label": "Oppression of tenants-at-will; rise of absentee landlordism and sub-infeudation", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य विशेषताएं", "type": "branch", "date": "स्थायी बंदोबस्त", "children": [
                {"label": "लॉर्ड कॉर्नवालिस द्वारा 1793 में बंगाल, बिहार, उड़ीसा और उत्तरी सरकार (ब्रिटिश भारत का 19%) में पेश किया गया", "type": "leaf"},
                {"label": "जमींदारों को भूमि के पूर्ण स्वामियों के रूप में मान्यता दी गई; राजस्व की मांग स्थायी रूप से तय की गई", "type": "leaf"}]},
            {"label": "मूल्यांकन और बंटवारा", "type": "branch", "date": "स्थायी बंदोबस्त", "children": [
                {"label": "संग्रह का हिस्सा: 10/11 भाग EIC को जाता था, और 1/11 भाग जमींदार द्वारा रखा जाता था", "type": "leaf"},
                {"label": "सूर्यास्त कानून (Sunset Law): यदि निर्दिष्ट तिथि के सूर्यास्त तक राजस्व का भुगतान नहीं किया गया तो जमींदारों ने स्वामित्व खो दिया", "type": "leaf"}]},
            {"label": "प्रभाव", "type": "branch", "date": "स्थायी बंदोबस्त", "children": [
                {"label": "बटाईदार किसानों (tenants-at-will) का उत्पीड़न हुआ; अनुपस्थित जमींदारी और उप-जमींदारी का उदय हुआ", "type": "leaf"}]}
        ]
    },
    "ryotwari": {
        "en": [
            {"label": "Core Features", "type": "branch", "date": "Ryotwari", "children": [
                {"label": "Developed by Alexander Read (1792) and Thomas Munro (1820)", "type": "leaf"},
                {"label": "Implemented in Madras, Bombay, and parts of Assam, covering about 51% of British India's land", "type": "leaf"}]},
            {"label": "Assessment & Collection", "type": "branch", "date": "Ryotwari", "children": [
                {"label": "Direct settlement between the state and the cultivator ('Ryot'); no intermediary Zamindars", "type": "leaf"},
                {"label": "Land revenue not fixed permanently; revised periodically (every 20 to 30 years) based on soil productivity", "type": "leaf"}]},
            {"label": "Impact", "type": "branch", "date": "Ryotwari", "children": [
                {"label": "Excessive state assessment (up to 50-60% of produce) forced Ryots into the clutches of local moneylenders", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य विशेषताएं", "type": "branch", "date": "रैयतवाड़ी", "children": [
                {"label": "अलेक्जेंडर रीड (1792) और थॉमस मुनरो (1820) द्वारा विकसित", "type": "leaf"},
                {"label": "मद्रास, बॉम्बे और असम के कुछ हिस्सों में लागू किया गया, जिसने ब्रिटिश भारत की लगभग 51% भूमि को कवर किया", "type": "leaf"}]},
            {"label": "मूल्यांकन और संग्रह", "type": "branch", "date": "रैयतवाड़ी", "children": [
                {"label": "राज्य और किसान ('रैयत') के बीच सीधा समझौता; बीच में कोई बिचौलिया जमींदार नहीं था", "type": "leaf"},
                {"label": "भू-राजस्व स्थायी रूप से तय नहीं था; मिट्टी की उत्पादकता के आधार पर समय-समय पर (हर 20 से 30 वर्ष में) संशोधित किया जाता था", "type": "leaf"}]},
            {"label": "प्रभाव", "type": "branch", "date": "रैयतवाड़ी", "children": [
                {"label": "अत्यधिक राज्य मूल्यांकन (उपज का 50-60% तक) ने रैयतों को स्थानीय साहूकारों के चंगुल में धकेल दिया", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "associated-terms-of-british-revenue-system": "revenue-terms",
    "colonialism-phase-of-finance-imperialism": "finance-imperialism",
    "colonialism-phase-of-finance-imperialism-1858-onwards": "finance-imperialism",
    "colonialism-phase-of-free-trade": "free-trade",
    "colonialism-phase-of-free-trade-1813-1858": "free-trade",
    "colonialism-phase-of-mercantilism": "mercantilism",
    "colonialism-phase-of-mercantilism-1757-1813": "mercantilism",
    "drain-of-wealth-theory": "drain-of-wealth",
    "impact-of-british-policy-on-indian-economy": "general-impact",
    "land-revenue-mahalwari": "mahalwari",
    "land-revenue-permanent-settlement": "permanent-settlement",
    "land-revenue-ryotwari": "ryotwari"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('EIC', 'EIC (East India Company)')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "permanent-settlement")
    
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
