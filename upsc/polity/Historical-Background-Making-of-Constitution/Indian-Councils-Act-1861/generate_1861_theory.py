import json
import os

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\polity\Historical-Background-Making-of-Constitution\Indian-Councils-Act-1861"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- THEORY GENERATION (ENGLISH) -----------------
theory_en = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Indian Councils Act, 1861"
    },
    "hero": {
        "title": "Indian Councils Act, 1861",
        "description": "Master the Indian Councils Act of 1861—a landmark legislation that initiated legislative decentralization in British India, introduced representative institutions by nominating Indians to the legislative council, gave statutory backing to the portfolio system, and vested the Viceroy with emergency ordinance-making powers (UPSC GS Paper-II: Constitutional History)."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Assess your understanding of the Indian Councils Act of 1861, including the restoration of legislative powers, the nomination of non-official Indians, the portfolio system, and the Viceroy's ordinance powers through a timed UPSC-standard test.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Historical Timeline & Development",
        "description": "Key milestones leading to and resulting from the Indian Councils Act of 1861.",
        "cards": [
            {
                "period": "Government of India Act, 1858",
                "date": "1858",
                "details": "Abolished the East India Company and established direct Crown Rule. The home government was fully restructured, but the internal administration in India remained highly centralized."
            },
            {
                "period": "Introduction of Portfolio System",
                "date": "1859",
                "details": "Lord Canning introduced the cabinet-like portfolio system on an executive basis to streamline administrative departments."
            },
            {
                "period": "Indian Councils Act, 1861",
                "date": "1861",
                "details": "Passed by British Parliament. Associated Indians with lawmaking, initiated decentralization, gave statutory backing to the portfolio system, and authorized emergency ordinances."
            },
            {
                "period": "First Nomination of Indians",
                "date": "1862",
                "details": "Lord Canning nominated three non-official Indian members: the Raja of Benares, the Maharaja of Patiala, and Sir Dinkar Rao to the Imperial Legislative Council."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Memory triggers to help retain the provisions of the Indian Councils Act of 1861.",
        "items": [
            {
                "title": "Mnemonic 1",
                "phrase": "\"P-O-D\"",
                "decryption": "<strong>P</strong>ortfolio system statutory backing, <strong>O</strong>rdinance power in emergency (6-month limit), <strong>D</strong>ecentralization begins (restoring legislative power to Bombay and Madras presidencies)."
            },
            {
                "title": "Mnemonic 2",
                "phrase": "\"B-P-D (Three Indian Nominees)\"",
                "decryption": "Raja of <strong>B</strong>enares, Maharaja of <strong>P</strong>atiala, and Sir <strong>D</strong>inkar Rao nominated as non-official members by Lord Canning in 1862."
            },
            {
                "title": "Mnemonic 3",
                "phrase": "\"VETO AND ORDINANCE\"",
                "decryption": "The Viceroy could bypass his council via veto and issue ordinances having a life of exactly 6 months."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Quick revision before solving practice questions.",
        "items": [
            {
                "question": "Which Act associated Indians with the law-making process for the first time?",
                "answer": "The <strong>Indian Councils Act of 1861</strong>.",
                "icon": "fa-users"
            },
            {
                "question": "Who were the first three Indians nominated to the Legislative Council?",
                "answer": "The <strong>Raja of Benares</strong>, the <strong>Maharaja of Patiala</strong>, and <strong>Sir Dinkar Rao</strong>, nominated by Lord Canning in 1862.",
                "icon": "fa-user-tie"
            },
            {
                "question": "How did the 1861 Act reverse the centralization trend started by the Charter Act of 1833?",
                "answer": "It initiated <strong>decentralization</strong> by restoring legislative powers to the Madras and Bombay Presidencies.",
                "icon": "fa-arrows-split-up-and-left"
            },
            {
                "question": "What was the validity of an emergency ordinance issued by the Viceroy under the 1861 Act?",
                "answer": "An ordinance had a maximum life of <strong>six months</strong>.",
                "icon": "fa-clock"
            }
        ]
    },
    "traps": {
        "title": "UPSC Civil Services Exam Traps to Avoid",
        "items": [
            "<strong>Trap 1:</strong> Assuming that the non-official Indian members nominated under the 1861 Act were elected or had representative powers. In reality, they were strictly handpicked nominees of the Viceroy, and their role was entirely advisory.",
            "<strong>Trap 2:</strong> Believing the Portfolio System was created from scratch in 1861. In fact, Lord Canning introduced it informally in 1859; the 1861 Act merely gave it statutory recognition/legal sanction.",
            "<strong>Trap 3:</strong> Confusing the legislative scope of the restored presidencies. While Bombay and Madras recovered legislative powers, all their local bills still required the absolute assent of the Viceroy, keeping overall imperial control highly centralized."
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Comprehensive analysis of the Indian Councils Act of 1861 for UPSC Prelims and Mains.",
        "sections": [
            {
                "title": "1. Representative Institutions & Nomination of Indians",
                "content": "<p>The Indian Councils Act of 1861 is a historic landmark in the constitutional evolution of India. It initiated the policy of associating Indians with the administrative and legislative machinery. The Act provided that the Viceroy should nominate some non-official members to his expanded legislative council (varying from 6 to 12 additional members, appointed for a two-year term).</p><p>Pursuant to this provision, in 1862, the Viceroy <strong>Lord Canning</strong> nominated three Indians as non-official members to his Legislative Council: the <strong>Raja of Benares</strong>, the <strong>Maharaja of Patiala</strong>, and <strong>Sir Dinkar Rao</strong>. However, their powers were highly restricted. The Legislative Council could not discuss financial matters, ask questions, or exercise any control over the executive branch. It functioned strictly as a machinery for validation of laws.</p><svg viewBox=\"0 0 800 280\" width=\"100%\" height=\"280\" class=\"responsive-svg-diagram\" style=\"margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 10px;\"><style>.svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: #2c3e50; font-size: 16px; } .svg-node { fill: #fdfefe; stroke: #2980b9; stroke-width: 2px; rx: 6px; ry: 6px; } .svg-split { fill: #ebf5fb; stroke: #2ecc71; stroke-width: 2.5px; rx: 6px; ry: 6px; } .svg-text-bold { font-family: 'Inter', sans-serif; font-size: 11px; fill: #2c3e50; font-weight: 700; } .svg-text { font-family: 'Inter', sans-serif; font-size: 10px; fill: #2c3e50; font-weight: 500; } .svg-arrow { fill: none; stroke: #bdc3c7; stroke-width: 2px; marker-end: url(#arrowhead-1861); }</style><defs><marker id=\"arrowhead-1861\" markerWidth=\"8\" markerHeight=\"6\" refX=\"6\" refY=\"3\" orient=\"auto\"><polygon points=\"0 0, 8 3, 0 6\" fill=\"#bdc3c7\" /></marker></defs><text x=\"20\" y=\"30\" class=\"svg-title\">Viceroy's Expanded Legislative Council (1861)</text><rect x=\"280\" y=\"40\" width=\"240\" height=\"45\" class=\"svg-split\" /><text x=\"400\" y=\"67\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">Viceroy of India (Executive Head)</text><path d=\"M 340 85 L 220 130\" class=\"svg-arrow\" /><path d=\"M 460 85 L 580 130\" class=\"svg-arrow\" /><rect x=\"60\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"200\" y=\"148\" class=\"svg-text-bold\" fill=\"#2980b9\" text-anchor=\"middle\">Executive Council (5 Members)</text><text x=\"200\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">Ordinary members in charge of portfolios</text><rect x=\"460\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"600\" y=\"148\" class=\"svg-text-bold\" fill=\"#e74c3c\" text-anchor=\"middle\">Additional Legislative Members (6 to 12)</text><text x=\"600\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">Nominated for 2 years (Official & Non-Official)</text><path d=\"M 600 185 L 600 215\" class=\"svg-arrow\" /><rect x=\"440\" y=\"215\" width=\"320\" height=\"50\" class=\"svg-split\" /><text x=\"600\" y=\"232\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">First 3 Non-Official Indian Appointees (1862)</text><text x=\"600\" y=\"248\" class=\"svg-text\" text-anchor=\"middle\">Raja of Benares, Maharaja of Patiala, Sir Dinkar Rao</text></svg>"
            },
            {
                "title": "2. Decentralization & Reversing Charter Act of 1833",
                "content": "<p>The Act initiated a major shift in the administrative philosophy of British India by reversing the centralization trend that had reached its peak under the Charter Act of 1833. The legislative powers that were stripped from the Madras and Bombay Presidencies in 1833 were restored. This legislative devolution laid the foundations of provincial autonomy, which culminated in the Government of India Act of 1935.</p><p>Furthermore, the Act provided for the establishment of new legislative councils for other provinces. Consequently, legislative councils were set up for the province of <strong>Bengal in 1862</strong>, the <strong>North-Western Frontier Province (NWFP) in 1886</strong>, and <strong>Punjab in 1897</strong>, enabling local administration and legislative validation across the expanding empire.</p><div class=\"table-responsive\" style=\"margin: 1.5rem 0; overflow-x: auto; border-radius: 8px; border: 1px solid rgba(128,128,128,0.15);\"><table style=\"width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;\"><thead><tr style=\"background: var(--bg-card); border-bottom: 2px solid rgba(128,128,128,0.15);\"><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 25%;\">Legislative Feature</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 35%;\">Under Charter Act of 1833 (Peak Centralization)</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 40%;\">Under Indian Councils Act of 1861 (Decentralization)</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">Bombay & Madras Presidencies</td><td style=\"padding: 12px;\">Completely deprived of local legislative powers.</td><td style=\"padding: 12px;\">Legislative powers fully restored; could frame local laws.</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1); background: rgba(128,128,128,0.02);\"><td style=\"padding: 12px; font-weight: bold;\">Imperial Overlordship</td><td style=\"padding: 12px;\">Governor-General in Council made the sole lawgiver for all India.</td><td style=\"padding: 12px;\">Viceroy maintained ultimate veto; local bills required Viceroy's assent.</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">New Provincial Councils</td><td style=\"padding: 12px;\">No provision for local provincial legislative bodies.</td><td style=\"padding: 12px;\">Mandated new legislative councils for Bengal, NWFP, and Punjab.</td></tr></tbody></table></div>"
            },
            {
                "title": "3. Portfolio System & Viceroy's Ordinance-Making Power",
                "content": "<p>In terms of executive functioning, the Act gave statutory recognition to the <strong>Portfolio System</strong>, which had been informally introduced by Lord Canning in 1859. Under this system, members of the Viceroy's Executive Council were made heads of specific departments (e.g., Home, Revenue, Military, Finance, and Law). This transformed the council into a cabinet-like structure where a member could issue final orders on behalf of the government for his department, streamlining administrative efficiency.</p><p>Crucially, Section 26 of the Act empowered the Viceroy to issue <strong>Ordinances</strong> during emergencies without the concurrence of the Legislative Council. These ordinances held the same legal force as acts passed by the council, but had a strict validity limit of <strong>six months</strong>. This power remains the historical precedent for Article 123 of the modern Constitution of India, which empowers the President of India to promulgate ordinances when Parliament is not in session.</p>"
            }
        ]
    }
}

# ----------------- THEORY GENERATION (HINDI) -----------------
theory_hi = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "भारतीय परिषद अधिनियम, 1861"
    },
    "hero": {
        "title": "भारतीय परिषद अधिनियम, 1861",
        "description": "भारतीय परिषद अधिनियम, 1861 पर महारत हासिल करें—यह एक ऐतिहासिक कानून था जिसने ब्रिटिश भारत में विधायी विकेंद्रीकरण की शुरुआत की, परिषद में भारतीयों को नामांकित करके प्रतिनिधि संस्थानों की नींव रखी, पोर्टफोलियो प्रणाली को वैधानिक मान्यता दी, और वायसराय को आपातकालीन अध्यादेश जारी करने की शक्ति दी (यूपीएससी सामान्य अध्ययन पेपर-II: संवैधानिक इतिहास)।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरएक्टिव यूपीएससी मॉक टेस्ट",
            "description": "1861 के भारतीय परिषद अधिनियम, विधायी शक्तियों की बहाली, गैर-आधिकारिक भारतीयों के नामांकन, पोर्टफोलियो प्रणाली और वायसराय की अध्यादेश शक्तियों के संबंध में अपनी समझ का परीक्षण करें।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण जमा करें"
        }
    },
    "timeline": {
        "title": "ऐतिहासिक कालक्रम और विकास",
        "description": "1861 के भारतीय परिषद अधिनियम की ओर ले जाने वाले और उसके बाद के प्रमुख मील के पत्थर।",
        "cards": [
            {
                "period": "भारत सरकार अधिनियम, 1858",
                "date": "1858",
                "details": "ईस्ट इंडिया कंपनी का अंत हुआ और प्रत्यक्ष क्राउन शासन स्थापित हुआ। गृह सरकार का पुनर्गठन हुआ, लेकिन भारत का आंतरिक प्रशासन अत्यधिक केंद्रीकृत रहा।"
            },
            {
                "period": "पोर्टफोलियो प्रणाली की शुरुआत",
                "date": "1859",
                "details": "लॉर्ड कैनिंग ने प्रशासनिक विभागों को सुव्यवस्थित करने के लिए कार्यकारी स्तर पर कैबिनेट जैसी पोर्टफोलियो प्रणाली की शुरुआत की।"
            },
            {
                "period": "भारतीय परिषद अधिनियम, 1861",
                "date": "1861",
                "details": "ब्रिटिश संसद द्वारा पारित। इसके तहत भारतीयों को कानून बनाने से जोड़ा गया, विकेंद्रीकरण की शुरुआत हुई, पोर्टफोलियो प्रणाली को कानूनी मान्यता मिली और अध्यादेश शक्ति दी गई।"
            },
            {
                "period": "भारतीयों का पहला नामांकन",
                "date": "1862",
                "details": "लॉर्ड कैनिंग ने तीन गैर-सरकारी भारतीय सदस्यों को नामांकित किया: बनारस के राजा, पटियाला के महाराजा और सर दिनकर राव।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के तरीके (Mnemonics)",
        "description": "1861 के भारतीय परिषद अधिनियम के प्रावधानों को याद रखने के लिए मेमोरी हैक्स।",
        "items": [
            {
                "title": "मेमोरी हैक 1",
                "phrase": "\"P-O-D\"",
                "decryption": "<strong>P</strong>ortfolio (पोर्टफोलियो प्रणाली को वैधानिक मान्यता), <strong>O</strong>rdinance (आपातकाल में 6 महीने के लिए अध्यादेश जारी करने की शक्ति), <strong>D</strong>ecentralization (मद्रास और बॉम्बे प्रेसीडेंसियों की विधायी शक्तियों की बहाली)।"
            },
            {
                "title": "मेमोरी हैक 2",
                "phrase": "\"B-P-D (तीन भारतीय मनोनीत सदस्य)\"",
                "decryption": "बनारस के राजा (<strong>B</strong>enares), पटियाला के महाराजा (<strong>P</strong>atiala), और सर दिनकर राव (<strong>D</strong>inkar Rao) को 1862 में लॉर्ड कैनिंग द्वारा गैर-आधिकारिक सदस्यों के रूप में मनोनीत किया गया।"
            },
            {
                "title": "मेमोरी हैक 3",
                "phrase": "\"वीटो और अध्यादेश\"",
                "decryption": "वायसराय अपनी परिषद को दरकिनार कर वीटो कर सकते थे और अध्यादेश जारी कर सकते थे जिसकी अवधि ठीक 6 महीने होती थी।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड",
        "description": "अभ्यास प्रश्नों को हल करने से पहले त्वरित पुनरीक्षण।",
        "items": [
            {
                "question": "किस अधिनियम ने पहली बार कानून बनाने की प्रक्रिया में भारतीयों को शामिल किया?",
                "answer": "<strong>1861 का भारतीय परिषद अधिनियम</strong>।",
                "icon": "fa-users"
            },
            {
                "question": "विधायी परिषद में नामांकित होने वाले पहले तीन भारतीय कौन थे?",
                "answer": "<strong>बनारस के राजा</strong>, <strong>पटियाला के महाराजा</strong>, और <strong>सर दिनकर राव</strong> (1862 में लॉर्ड कैनिंग द्वारा मनोनीत)।",
                "icon": "fa-user-tie"
            },
            {
                "question": "1861 के अधिनियम ने 1833 के चार्टर अधिनियम द्वारा शुरू की गई केंद्रीकरण की प्रवृत्ति को कैसे उलझाया?",
                "answer": "इसने मद्रास और बॉम्बे प्रेसीडेंसियों को विधायी शक्तियां लौटाकर <strong>विकेंद्रीकरण</strong> की शुरुआत की।",
                "icon": "fa-arrows-split-up-and-left"
            },
            {
                "question": "1861 के अधिनियम के तहत वायसराय द्वारा जारी आपातकालीन अध्यादेश की वैधता क्या थी?",
                "answer": "एक अध्यादेश की अधिकतम अवधि <strong>छह महीने</strong> की होती थी।",
                "icon": "fa-clock"
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा में बचने योग्य जाल (Common Traps)",
        "items": [
            "<strong>जाल 1:</strong> यह मान लेना कि 1861 के अधिनियम के तहत मनोनीत गैर-सरकारी भारतीय सदस्य निर्वाचित थे या उनके पास वास्तविक प्रतिनिधित्व शक्तियां थीं। वास्तव में, वे वायसराय द्वारा चुने गए थे और उनकी भूमिका विशुद्ध रूप से सलाहकार थी।",
            "<strong>जाल 2:</strong> यह विश्वास करना कि पोर्टफोलियो प्रणाली को 1861 में शून्य से बनाया गया था। वास्तव में, लॉर्ड कैनिंग ने इसे 1859 में अनौपचारिक रूप से शुरू किया था; 1861 के अधिनियम ने केवल इसे वैधानिक/कानूनी मान्यता दी।",
            "<strong>जाल 3:</strong> बहाल की गई प्रेसीडेंसियों के विधायी दायरे को लेकर भ्रमित होना। यद्यपि बॉम्बे और मद्रास को विधायी अधिकार वापस मिल गए, लेकिन उनके स्थानीय विधेयकों के लिए वायसराय की अंतिम सहमति आवश्यक थी।"
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (गहन अध्ययन)",
        "description": "यूपीएससी प्रारंभिक और मुख्य परीक्षा के लिए 1861 के भारतीय परिषद अधिनियम का व्यापक विश्लेषण।",
        "sections": [
            {
                "title": "1. प्रतिनिधि संस्थाएं और भारतीयों का नामांकन",
                "content": "<p>1861 का भारतीय परिषद अधिनियम भारत के संवैधानिक इतिहास में एक महत्वपूर्ण मील का पत्थर है। इसने प्रशासन और विधायी तंत्र में भारतीयों को जोड़ने की नीति की शुरुआत की। अधिनियम में प्रावधान किया गया कि वायसराय को अपनी विस्तारित विधायी परिषद में कुछ गैर-सरकारी सदस्यों को नामांकित करना चाहिए (जिसमें 6 से 12 अतिरिक्त सदस्य शामिल हो सकते थे, जो दो वर्ष की अवधि के लिए नियुक्त होते थे)।</p><p>इस प्रावधान के अनुसार, 1862 में वायसराय <strong>लॉर्ड कैनिंग</strong> ने अपनी विधायी परिषद में तीन भारतीयों को गैर-सरकारी सदस्यों के रूप में मनोनीत किया: <strong>बनारस के राजा</strong>, <strong>पटियाला के महाराजा</strong>, और <strong>सर दिनकर राव</strong>। हालाँकि, उनके विधायी अधिकार अत्यंत सीमित थे। विधायी परिषद को वित्तीय मामलों पर चर्चा करने, प्रश्न पूछने या कार्यकारी शाखा पर किसी प्रकार का नियंत्रण रखने की अनुमति नहीं थी। यह कानून के सत्यापन के लिए केवल एक मशीनरी के रूप में कार्य करती थी।</p><svg viewBox=\"0 0 800 280\" width=\"100%\" height=\"280\" class=\"responsive-svg-diagram\" style=\"margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 10px;\"><style>.svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: #2c3e50; font-size: 16px; } .svg-node { fill: #fdfefe; stroke: #2980b9; stroke-width: 2px; rx: 6px; ry: 6px; } .svg-split { fill: #ebf5fb; stroke: #2ecc71; stroke-width: 2.5px; rx: 6px; ry: 6px; } .svg-text-bold { font-family: 'Inter', sans-serif; font-size: 11px; fill: #2c3e50; font-weight: 700; } .svg-text { font-family: 'Inter', sans-serif; font-size: 10px; fill: #2c3e50; font-weight: 500; } .svg-arrow { fill: none; stroke: #bdc3c7; stroke-width: 2px; marker-end: url(#arrowhead-1861); }</style><defs><marker id=\"arrowhead-1861\" markerWidth=\"8\" markerHeight=\"6\" refX=\"6\" refY=\"3\" orient=\"auto\"><polygon points=\"0 0, 8 3, 0 6\" fill=\"#bdc3c7\" /></marker></defs><text x=\"20\" y=\"30\" class=\"svg-title\">वायसराय की विस्तारित विधायी परिषद (1861)</text><rect x=\"280\" y=\"40\" width=\"240\" height=\"45\" class=\"svg-split\" /><text x=\"400\" y=\"67\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">भारत के वायसराय (कार्यकारी प्रमुख)</text><path d=\"M 340 85 L 220 130\" class=\"svg-arrow\" /><path d=\"M 460 85 L 580 130\" class=\"svg-arrow\" /><rect x=\"60\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"200\" y=\"148\" class=\"svg-text-bold\" fill=\"#2980b9\" text-anchor=\"middle\">कार्यकारी परिषद (5 सदस्य)</text><text x=\"200\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">विभागों के प्रभारी सामान्य सदस्य</text><rect x=\"460\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"600\" y=\"148\" class=\"svg-text-bold\" fill=\"#e74c3c\" text-anchor=\"middle\">अतिरिक्त विधायी सदस्य (6 से 12)</text><text x=\"600\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">2 वर्ष के लिए मनोनीत (सरकारी और गैर-सरकारी)</text><path d=\"M 600 185 L 600 215\" class=\"svg-arrow\" /><rect x=\"440\" y=\"215\" width=\"320\" height=\"50\" class=\"svg-split\" /><text x=\"600\" y=\"232\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">प्रथम 3 गैर-सरकारी भारतीय मनोनीत सदस्य (1862)</text><text x=\"600\" y=\"248\" class=\"svg-text\" text-anchor=\"middle\">बनारस के राजा, पटियाला के महाराजा, सर दिनकर राव</text></svg>"
            },
            {
                "title": "2. विकेंद्रीकरण और 1833 के चार्टर अधिनियम को उलटना",
                "content": "<p>अधिनियम ने केंद्रीकरण की उस प्रवृत्ति को उलट दिया जो 1833 के चार्टर अधिनियम के तहत अपने चरम पर पहुंच गई थी, जिससे ब्रिटिश भारत के प्रशासनिक दर्शन में एक बड़ा बदलाव आया। मद्रास और बॉम्बे प्रेसीडेंसियों से 1833 में छीनी गई विधायी शक्तियों को बहाल कर दिया गया। इस विधायी विकेंद्रीकरण ने प्रांतीय स्वायत्तता की नींव रखी, जो 1935 के भारत सरकार अधिनियम में पूर्ण रूप से सामने आई।</p><p>इसके अलावा, अधिनियम ने अन्य प्रांतों के लिए नई विधायी परिषदों की स्थापना का प्रावधान किया। परिणामस्वरूप, <strong>बंगाल के लिए 1862</strong> में, <strong>उत्तर-पश्चिमी सीमांत प्रांत (NWFP) के लिए 1886</strong> में, और <strong>पंजाब के लिए 1897</strong> में विधायी परिषदें स्थापित की गईं, जिससे साम्राज्य के विभिन्न हिस्सों में स्थानीय विधायी कार्य संभव हो सके।</p><div class=\"table-responsive\" style=\"margin: 1.5rem 0; overflow-x: auto; border-radius: 8px; border: 1px solid rgba(128,128,128,0.15);\"><table style=\"width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;\"><thead><tr style=\"background: var(--bg-card); border-bottom: 2px solid rgba(128,128,128,0.15);\"><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 25%;\">विधायी विशेषता</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 35%;\">1833 के चार्टर अधिनियम के तहत (चरम केंद्रीकरण)</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 40%;\">1861 के भारतीय परिषद अधिनियम के तहत (विकेंद्रीकरण)</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">बॉम्बे और मद्रास प्रेसीडेंसियां</td><td style=\"padding: 12px;\">स्थानीय विधायी शक्तियों से पूरी तरह से वंचित।</td><td style=\"padding: 12px;\">विधायी शक्तियां बहाल की गईं; स्थानीय कानून बना सकती थीं।</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1); background: rgba(128,128,128,0.02);\"><td style=\"padding: 12px; font-weight: bold;\">शाही अधिपत्य</td><td style=\"padding: 12px;\">गवर्नर-जनरल इन काउंसिल पूरे भारत के लिए एकमात्र कानून निर्माता।</td><td style=\"padding: 12px;\">वायसराय के पास अंतिम वीटो शक्ति रही; स्थानीय विधेयकों के लिए वायसराय की सहमति आवश्यक थी।</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">नई प्रांतीय परिषदें</td><td style=\"padding: 12px;\">स्थानीय प्रांतीय विधायी निकायों के लिए कोई प्रावधान नहीं।</td><td style=\"padding: 12px;\">बंगाल, NWFP और पंजाब के लिए नई विधायी परिषदों की स्थापना का प्रावधान।</td></tr></tbody></table></div>"
            },
            {
                "title": "3. पोर्टफोलियो प्रणाली और वायसराय की अध्यादेश शक्ति",
                "content": "<p>कार्यकारी कामकाज के मामले में, अधिनियम ने <strong>पोर्टफोलियो प्रणाली</strong> को वैधानिक मान्यता दी, जिसे लॉर्ड कैनिंग ने 1859 में अनौपचारिक रूप से पेश किया था। इस प्रणाली के तहत, वायसराय की कार्यकारी परिषद के सदस्यों को विशिष्ट विभागों (जैसे गृह, राजस्व, सैन्य, वित्त और कानून) का प्रमुख बनाया गया था। इसने परिषद को एक कैबिनेट जैसी संरचना में बदल दिया जहाँ एक सदस्य अपने विभाग के लिए सरकार की ओर से अंतिम आदेश जारी कर सकता था, जिससे प्रशासनिक दक्षता में सुधार हुआ।</p><p>इसके अलावा, अधिनियम की धारा 26 ने वायसराय को विधायी परिषद की सहमति के बिना आपातकाल के दौरान <strong>अध्यादेश</strong> जारी करने का अधिकार दिया। इन अध्यादेशों की शक्ति विधायी परिषद द्वारा पारित कानूनों के समान थी, लेकिन इनकी वैधता अधिकतम <strong>छह महीने</strong> तक थी। यह शक्ति आधुनिक भारत के संविधान के अनुच्छेद 123 का एक ऐतिहासिक पूर्ववृत्त है, जो भारत के राष्ट्रपति को संसद के सत्र में न होने पर अध्यादेश जारी करने का अधिकार देता है।</p>"
            }
        ]
    }
}

with open(os.path.join(BASE_DIR, "theory.json"), "w", encoding="utf-8") as f:
    json.dump(theory_en, f, ensure_ascii=False, indent=4)

with open(os.path.join(HI_DIR, "theory.json"), "w", encoding="utf-8") as f:
    json.dump(theory_hi, f, ensure_ascii=False, indent=4)

print("Theory JSON files generated successfully.")
