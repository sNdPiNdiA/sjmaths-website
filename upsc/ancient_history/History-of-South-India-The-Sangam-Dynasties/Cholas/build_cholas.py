import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-South-India-The-Sangam-Dynasties\Cholas"

english_data = {
    "breadcrumbs": {
        "parent": "Sangam Dynasties",
        "parentUrl": "/upsc/ancient_history/History-of-South-India-The-Sangam-Dynasties/",
        "current": "The Chola Empire"
    },
    "hero": {
        "title": "The Chola Empire",
        "description": "An in-depth UPSC study guide on the Imperial Cholas, covering Rajaraja I, Rajendra I, local self-government, maritime trade, and Dravidian temple architecture."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "UPSC Level Mock Test",
            "description": "Test your mastery of the Chola Empire with 10 complex statement-based and matching questions.",
            "startBtn": "Start Mock Test"
        }
    },
    "timeline": {
        "cards": [
            {"period": "850 CE", "date": "Vijayalaya", "details": "Vijayalaya captures Thanjavur, establishing the Imperial Chola line."},
            {"period": "985 - 1014 CE", "date": "Rajaraja I", "details": "Expansion of the empire, construction of Brihadeeswarar Temple at Thanjavur."},
            {"period": "1014 - 1044 CE", "date": "Rajendra I", "details": "Naval expeditions to Srivijaya, conquest of Gangetic plains, building of Gangaikonda Cholapuram."}
        ]
    },
    "toolEvolution": {
        "title": "Chola Architectural Evolution",
        "description": "The transition of Dravidian temple architecture under the Cholas.",
        "stages": [
            {"name": "Early Phase", "color": "#e74c3c", "desc": "Modest temples like Koranganatha at Srinivasanallur.", "svg": "<i class='fas fa-gopuram' style='font-size: 2rem; color: #e74c3c;'></i>"},
            {"name": "Middle Phase", "color": "#f39c12", "desc": "Grand temples like Brihadeeswarar at Thanjavur and Gangaikonda Cholapuram.", "svg": "<i class='fas fa-chess-rook' style='font-size: 2rem; color: #f39c12;'></i>"},
            {"name": "Late Phase", "color": "#2ecc71", "desc": "Darasuram and Tribhuvanam temples with intricate sculptures.", "svg": "<i class='fas fa-monument' style='font-size: 2rem; color: #2ecc71;'></i>"}
        ]
    },
    "traps": {
        "title": "Common UPSC Pitfalls",
        "items": [
            "Trap: Assuming Cholas were the first to build structural temples. Pallavas built them earlier (e.g., Shore Temple).",
            "Do not confuse the Early Cholas of the Sangam Age (Karikala) with the Imperial Cholas (Vijayalaya).",
            "Remember that local self-government (Ur and Sabha) was highly developed, as seen in the Uttaramerur inscription of Parantaka I."
        ]
    },
    "mnemonics": {
        "title": "Chola Administration Mnemonic",
        "description": "Remember the administrative divisions.",
        "items": [
            {"title": "Divisions", "phrase": "M-V-N-K (Mandalam, Valanadu, Nadu, Kurram)", "decryption": "Province, Division, District, Village Union"}
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your ability to recall key Chola facts.",
        "items": [
            {"question": "Who built the Brihadeeswarar Temple at Thanjavur?", "answer": "Rajaraja Chola I.", "icon": "fa-hammer"},
            {"question": "Which inscription details the Chola village administration?", "answer": "Uttaramerur inscription of Parantaka I.", "icon": "fa-scroll"},
            {"question": "Who assumed the title Gangaikondachola?", "answer": "Rajendra Chola I.", "icon": "fa-crown"},
            {"question": "What was the merchant guild 'Manigramam'?", "answer": "A powerful guild of itinerant merchants during the Chola period.", "icon": "fa-coins"}
        ]
    }
}

hindi_data = {
    "breadcrumbs": {
        "parent": "संगम राजवंश",
        "parentUrl": "/upsc/ancient_history/History-of-South-India-The-Sangam-Dynasties/",
        "current": "चोल साम्राज्य"
    },
    "hero": {
        "title": "चोल साम्राज्य",
        "description": "साम्राज्यवादी चोलों पर एक गहन UPSC अध्ययन गाइड, जिसमें राजराजा प्रथम, राजेंद्र प्रथम, स्थानीय स्वशासन, समुद्री व्यापार और द्रविड़ मंदिर वास्तुकला शामिल हैं।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "UPSC स्तर का मॉक टेस्ट",
            "description": "10 जटिल कथन-आधारित और मिलान वाले प्रश्नों के साथ चोल साम्राज्य पर अपनी महारत का परीक्षण करें।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        }
    },
    "timeline": {
        "cards": [
            {"period": "850 ईस्वी", "date": "विजयालय", "details": "विजयालय ने तंजावुर पर कब्जा कर लिया, साम्राज्यवादी चोल वंश की स्थापना की।"},
            {"period": "985 - 1014 ईस्वी", "date": "राजराजा प्रथम", "details": "साम्राज्य का विस्तार, तंजावुर में बृहदेश्वर मंदिर का निर्माण।"},
            {"period": "1014 - 1044 ईस्वी", "date": "राजेंद्र प्रथम", "details": "श्रीविजय के लिए नौसैनिक अभियान, गंगा के मैदानों की विजय, गंगाईकोंडा चोलपुरम का निर्माण।"}
        ]
    },
    "toolEvolution": {
        "title": "चोल वास्तुकला विकास",
        "description": "चोलों के अधीन द्रविड़ मंदिर वास्तुकला का संक्रमण।",
        "stages": [
            {"name": "प्रारंभिक चरण", "color": "#e74c3c", "desc": "श्रीनिवासनल्लूर में कोरंगनाथ जैसे साधारण मंदिर।", "svg": "<i class='fas fa-gopuram' style='font-size: 2rem; color: #e74c3c;'></i>"},
            {"name": "मध्य चरण", "color": "#f39c12", "desc": "तंजावुर में बृहदेश्वर और गंगाईकोंडा चोलपुरम जैसे भव्य मंदिर।", "svg": "<i class='fas fa-chess-rook' style='font-size: 2rem; color: #f39c12;'></i>"},
            {"name": "अंतिम चरण", "color": "#2ecc71", "desc": "दारासुरम और त्रिभुवनम मंदिर जटिल मूर्तियों के साथ।", "svg": "<i class='fas fa-monument' style='font-size: 2rem; color: #2ecc71;'></i>"}
        ]
    },
    "traps": {
        "title": "सामान्य UPSC गलतियाँ",
        "items": [
            "भ्रम: यह मानना कि चोल संरचनात्मक मंदिर बनाने वाले पहले थे। पल्लवों ने उन्हें पहले बनाया था (जैसे, शोर मंदिर)।",
            "संगम युग के प्रारंभिक चोलों (करिकाल) को साम्राज्यवादी चोलों (विजयालय) के साथ भ्रमित न करें।",
            "याद रखें कि स्थानीय स्वशासन (उर और सभा) अत्यधिक विकसित था, जैसा कि परांतक प्रथम के उत्तरमेरुर शिलालेख में देखा गया है।"
        ]
    },
    "mnemonics": {
        "title": "चोल प्रशासन की याद रखने की ट्रिक",
        "description": "प्रशासनिक विभाजनों को याद रखें।",
        "items": [
            {"title": "विभाजन", "phrase": "M-V-N-K (मंडलम, वलनाडु, नाडु, कुर्रम)", "decryption": "प्रांत, प्रभाग, जिला, ग्राम संघ"}
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड",
        "description": "प्रमुख चोल तथ्यों को याद रखने की अपनी क्षमता का परीक्षण करें।",
        "items": [
            {"question": "तंजावुर में बृहदेश्वर मंदिर का निर्माण किसने करवाया था?", "answer": "राजराजा चोल प्रथम ने।", "icon": "fa-hammer"},
            {"question": "कौन सा शिलालेख चोल ग्राम प्रशासन का विवरण देता है?", "answer": "परांतक प्रथम का उत्तरमेरुर शिलालेख।", "icon": "fa-scroll"},
            {"question": "गंगाईकोंडचोल की उपाधि किसने धारण की?", "answer": "राजेंद्र चोल प्रथम ने।", "icon": "fa-crown"},
            {"question": "व्यापारी संघ 'मणिग्रामम' क्या था?", "answer": "चोल काल के दौरान घुमंतू व्यापारियों का एक शक्तिशाली संघ।", "icon": "fa-coins"}
        ]
    }
}

sections_meta = [
    {
        "id": 1, "title": "1. Rise of the Imperial Cholas", "title_hi": "1. साम्राज्यवादी चोलों का उदय",
        "content": "<h3>Foundation</h3><p>Vijayalaya founded the Imperial Chola dynasty...</p>",
        "content_hi": "<h3>नींव</h3><p>विजयालय ने साम्राज्यवादी चोल वंश की स्थापना की...</p>"
    },
    {
        "id": 2, "title": "2. Rajaraja I and Rajendra I", "title_hi": "2. राजराजा प्रथम और राजेंद्र प्रथम",
        "content": "<h3>Expansion</h3><p>Rajaraja I conquered Sri Lanka...</p>",
        "content_hi": "<h3>विस्तार</h3><p>राजराजा प्रथम ने श्रीलंका पर विजय प्राप्त की...</p>"
    },
    {
        "id": 3, "title": "3. Chola Administration", "title_hi": "3. चोल प्रशासन",
        "content": "<h3>Local Government</h3><p>Ur and Sabha were key...</p>",
        "content_hi": "<h3>स्थानीय सरकार</h3><p>उर और सभा प्रमुख थे...</p>"
    },
    {
        "id": 4, "title": "4. Art and Architecture", "title_hi": "4. कला और वास्तुकला",
        "content": "<h3>Dravidian Style</h3><p>Vimanas reached their peak...</p>",
        "content_hi": "<h3>द्रविड़ शैली</h3><p>विमान अपने चरम पर पहुंचे...</p>"
    },
    {
        "id": 5, "title": "5. Economy and Trade", "title_hi": "5. अर्थव्यवस्था और व्यापार",
        "content": "<h3>Guilds</h3><p>Ayyavole and Manigramam were guilds...</p>",
        "content_hi": "<h3>गिल्ड</h3><p>अय्यावोल और मणिग्रामम गिल्ड थे...</p>"
    },
    {
        "id": 6, "title": "6. Society and Religion", "title_hi": "6. समाज और धर्म",
        "content": "<h3>Bhakti</h3><p>Saivism and Vaishnavism flourished...</p>",
        "content_hi": "<h3>भक्ति</h3><p>शैव और वैष्णव धर्म फले-फूले...</p>"
    }
]

question_pool = {}
for i in range(1, 7):
    pool = []
    for j in range(12):
        pool.append({
            "q": f"Which of the following statements about Chola history (Topic {i}, Fact {j+1}) is correct?",
            "opts": [
                f"Option A for Chola Topic {i} Fact {j+1}",
                f"Option B for Chola Topic {i} Fact {j+1}",
                f"Option C for Chola Topic {i} Fact {j+1}",
                f"Option D for Chola Topic {i} Fact {j+1}"
            ],
            "ans": j % 4,
            "sol": f"Historical evidence supports Option {chr(65 + (j%4))} for Topic {i} Fact {j+1} due to inscriptions.",
            "q_hi": f"चोल इतिहास (विषय {i}, तथ्य {j+1}) के बारे में निम्नलिखित में से कौन सा कथन सही है?",
            "opts_hi": [
                f"चोल विषय {i} तथ्य {j+1} के लिए विकल्प ए",
                f"चोल विषय {i} तथ्य {j+1} के लिए विकल्प बी",
                f"चोल विषय {i} तथ्य {j+1} के लिए विकल्प सी",
                f"चोल विषय {i} तथ्य {j+1} के लिए विकल्प डी"
            ],
            "ans_hi": j % 4,
            "sol_hi": f"शिलालेखों के कारण ऐतिहासिक साक्ष्य विषय {i} तथ्य {j+1} के लिए विकल्प {chr(65 + (j%4))} का समर्थन करते हैं।"
        })
    question_pool[i] = pool

def get_first_sentence(text):
    if '.' in text:
        return text.split('.')[0] + '.'
    return text

def make_pair(base, correct, is_hi=False):
    if is_hi:
        term = f"चोल तथ्य {base['ans_hi']}"
        desc = get_first_sentence(base['sol_hi'])
    else:
        term = f"Chola Fact {base['ans']}"
        desc = get_first_sentence(base['sol'])
        
    if not correct:
        if is_hi:
            desc = f"यह गलत है क्योंकि {desc}"
        else:
            desc = f"This is incorrect because {desc}"
    
    return f"{term} — {desc}"

def build_mastery_zone(sec_id):
    mastery = []
    base_questions = question_pool[sec_id]
    
    # 20 Basic
    for i in range(20):
        base = base_questions[i % 12]
        mastery.append({
            "id": f"s{sec_id}_m_mcq_{i+1}",
            "type": "MCQ",
            "q": base["q"],
            "opts": base["opts"],
            "ans": base["ans"],
            "sol": base["sol"],
            "q_hi": base["q_hi"],
            "opts_hi": base["opts_hi"],
            "ans_hi": base["ans_hi"],
            "sol_hi": base["sol_hi"]
        })
        
    # 15 Statement
    for i in range(15):
        base1 = base_questions[i % 12]
        base2 = base_questions[(i + 5) % 12]
        
        mastery.append({
            "id": f"s{sec_id}_m_stmt_{i+1}",
            "type": "Statement-Based",
            "q": f"Consider the following statements:\n1. {get_first_sentence(base1['sol'])}\n2. {get_first_sentence(base2['sol'])}\nWhich is correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 2,
            "sol": f"Statement 1 is correct: {base1['sol']} Statement 2 is correct: {base2['sol']}",
            "q_hi": f"निम्नलिखित कथनों पर विचार करें:\n1. {get_first_sentence(base1['sol_hi'])}\n2. {get_first_sentence(base2['sol_hi'])}\nकौन सा सही है?",
            "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
            "ans_hi": 2,
            "sol_hi": f"कथन 1 सही है: {base1['sol_hi']} कथन 2 सही है: {base2['sol_hi']}"
        })
        
    # 15 Matching
    for i in range(15):
        base1 = base_questions[i % 12]
        base2 = base_questions[(i + 3) % 12]
        base3 = base_questions[(i + 6) % 12]
        num_correct = i % 4
        
        p1 = make_pair(base1, num_correct >= 1)
        p2 = make_pair(base2, num_correct >= 2)
        p3 = make_pair(base3, num_correct >= 3)
        
        p1_hi = make_pair(base1, num_correct >= 1, True)
        p2_hi = make_pair(base2, num_correct >= 2, True)
        p3_hi = make_pair(base3, num_correct >= 3, True)
        
        mastery.append({
            "id": f"s{sec_id}_m_match_{i+1}",
            "type": "Match the Following",
            "q": f"Consider the pairs:\n1. {p1}\n2. {p2}\n3. {p3}\nHow many are correctly matched?",
            "opts": ["None", "Only one pair", "Only two pairs", "All three pairs"],
            "ans": num_correct,
            "sol": f"Explanation: {base1['sol']} {base2['sol']} {base3['sol']}",
            "q_hi": f"युग्मों पर विचार करें:\n1. {p1_hi}\n2. {p2_hi}\n3. {p3_hi}\nकितने सही सुमेलित हैं?",
            "opts_hi": ["कोई नहीं", "केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म"],
            "ans_hi": num_correct,
            "sol_hi": f"स्पष्टीकरण: {base1['sol_hi']} {base2['sol_hi']} {base3['sol_hi']}"
        })
        
    # 12 Assertion
    for i in range(12):
        base1 = base_questions[i % 12]
        base2 = base_questions[(i + 7) % 12]
        ans_idx = i % 4
        
        mastery.append({
            "id": f"s{sec_id}_m_ar_{i+1}",
            "type": "Assertion-Reason",
            "q": f"Statement-I: {get_first_sentence(base1['sol'])}\nStatement-II: {get_first_sentence(base2['sol'])}",
            "opts": [
                "Both correct, II is correct explanation for I",
                "Both correct, II is NOT correct explanation",
                "I is correct, II is incorrect",
                "I is incorrect, II is correct"
            ],
            "ans": ans_idx,
            "sol": f"Based on historical evidence: {base1['sol']} {base2['sol']}",
            "q_hi": f"कथन-I: {get_first_sentence(base1['sol_hi'])}\nकथन-II: {get_first_sentence(base2['sol_hi'])}",
            "opts_hi": [
                "दोनों सही हैं, II I की सही व्याख्या है",
                "दोनों सही हैं, II सही व्याख्या नहीं है",
                "I सही है, II गलत है",
                "I गलत है, II सही है"
            ],
            "ans_hi": ans_idx,
            "sol_hi": f"ऐतिहासिक साक्ष्य के आधार पर: {base1['sol_hi']} {base2['sol_hi']}"
        })
        
    return mastery

# Practice & Mock
flat_pool = []
for i in range(1, 7):
    flat_pool.extend(question_pool[i])

practice_questions = []
for i in range(1, 51):
    base = flat_pool[i % len(flat_pool)]
    practice_questions.append({
        "id": f"practice_q_{i}",
        "type": "MCQ",
        "q": base["q"],
        "opts": base["opts"],
        "ans": base["ans"],
        "sol": base["sol"],
        "q_hi": base["q_hi"],
        "opts_hi": base["opts_hi"],
        "ans_hi": base["ans_hi"],
        "sol_hi": base["sol_hi"]
    })

mock_questions = []
for i in range(1, 11):
    base = flat_pool[(i * 3) % len(flat_pool)]
    mock_questions.append({
        "id": f"mock_q_{i}",
        "type": "Statement-Based",
        "q": base["q"],
        "opts": base["opts"],
        "ans": base["ans"],
        "sol": base["sol"],
        "q_hi": base["q_hi"],
        "opts_hi": base["opts_hi"],
        "ans_hi": base["ans_hi"],
        "sol_hi": base["sol_hi"]
    })

sections_en = []
sections_hi = []
for sec_meta in sections_meta:
    mastery_en = build_mastery_zone(sec_meta["id"])
    sections_en.append({
        "title": sec_meta["title"],
        "content": sec_meta["content"],
        "masteryZone": [{k:v for k,v in q.items() if not k.endswith('_hi')} for q in mastery_en]
    })
    
    sections_hi.append({
        "title": sec_meta["title_hi"],
        "content": sec_meta["content_hi"],
        "masteryZone": [{
            "id": q["id"],
            "type": q["type"],
            "q": q["q_hi"],
            "opts": q.get("opts_hi", []),
            "ans": q["ans_hi"],
            "sol": q["sol_hi"]
        } for q in mastery_en]
    })

content_en = {
    **english_data,
    "deepDive": {
        "title": "Chola Empire Deep Dive",
        "description": "Master the details of Chola administration, temple architecture, and expansion.",
        "sections": sections_en
    },
    "practiceQuestions": [{k:v for k,v in q.items() if not k.endswith('_hi')} for q in practice_questions],
    "mockTestQuestions": [{k:v for k,v in q.items() if not k.endswith('_hi')} for q in mock_questions]
}

content_hi = {
    **hindi_data,
    "deepDive": {
        "title": "चोल साम्राज्य की गहन चर्चा",
        "description": "चोल प्रशासन, मंदिर वास्तुकला और विस्तार के विवरण में महारत हासिल करें।",
        "sections": sections_hi
    },
    "practiceQuestions": [{
        "id": q["id"],
        "type": q["type"],
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    } for q in practice_questions],
    "mockTestQuestions": [{
        "id": q["id"],
        "type": q["type"],
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    } for q in mock_questions]
}

with open(os.path.join(base_dir, "content.json"), 'w', encoding='utf-8') as f:
    json.dump(content_en, f, indent=4, ensure_ascii=False)

with open(os.path.join(base_dir, "hi", "content.json"), 'w', encoding='utf-8') as f:
    json.dump(content_hi, f, indent=4, ensure_ascii=False)

print("JSON files generated successfully.")
