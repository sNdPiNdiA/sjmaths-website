import json
import os

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\polity\Historical-Background-Making-of-Constitution\Indian-Councils-Act-1892"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- THEORY GENERATION (ENGLISH) -----------------
theory_en = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Indian Councils Act, 1892"
    },
    "hero": {
        "title": "Indian Councils Act, 1892",
        "description": "Master the Indian Councils Act of 1892—a milestone in India's constitutional history that expanded legislative councils, introduced the first elements of representative democracy via indirect elections, and granted councils the rights to discuss the budget and ask questions of the executive."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Assess your understanding of the Indian Councils Act of 1892, including council expansion, budget discussion limits, indirect election mechanisms, and questioning rights through a timed UPSC-standard test.",
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
        "description": "Key milestones leading to and resulting from the Indian Councils Act of 1892.",
        "cards": [
            {
                "period": "Indian Councils Act, 1861",
                "date": "1861",
                "details": "Associated Indians with lawmaking and initiated decentralization, but left the legislative councils with zero control over executive functions or finances."
            },
            {
                "period": "Foundation of Indian National Congress",
                "date": "1885",
                "details": "Formed in Bombay. Immediately demanded legislative council reform, inclusion of elected representatives, and control over public finance."
            },
            {
                "period": "Indian Councils Act, 1892",
                "date": "1892",
                "details": "Enacted by British Parliament. Expanded council size, allowed budget discussion and questioning, and introduced indirect elections through recommendations."
            },
            {
                "period": "Indian Councils Act, 1909 (Morley-Minto)",
                "date": "1909",
                "details": "Succeeded the 1892 reforms, introducing direct elections (limited franchise), supplementary questions, and a separate electorate for Muslims."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Memory triggers to help retain the provisions of the Indian Councils Act of 1892.",
        "items": [
            {
                "title": "Mnemonic 1",
                "phrase": "\"B-E-Q\"",
                "decryption": "<strong>B</strong>udget discussion allowed (but no voting), <strong>E</strong>lection (indirect system through recommendations), <strong>Q</strong>uestions allowed on public interest (with 6 days' notice, no supplementaries)."
            },
            {
                "title": "Mnemonic 2",
                "phrase": "\"MIN-10 MAX-16\"",
                "decryption": "The number of additional (non-official) members in the Central Legislative Council was increased to a minimum of 10 and a maximum of 16."
            },
            {
                "title": "Mnemonic 3",
                "phrase": "\"NO VOTING, NO SUPPLEMENTARIES\"",
                "decryption": "Remember the key limitations of the 1892 Act: members could talk about the budget but not vote on it, and could ask questions but not ask follow-ups (supplementaries)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Quick revision before solving practice questions.",
        "items": [
            {
                "question": "Did the Indian Councils Act of 1892 allow members to vote on the budget?",
                "answer": "No. Members could **discuss the budget**, but they had **no power to vote** on it or propose resolutions.",
                "icon": "fa-sack-dollar"
            },
            {
                "question": "What is the significance of the 1892 Act regarding representation?",
                "answer": "It introduced the **first element of indirect election** by filling non-official seats based on recommendations from local bodies.",
                "icon": "fa-check-to-slot"
            },
            {
                "question": "Was the word 'election' explicitly used in the text of the 1892 Act?",
                "answer": "No, the word **'election' was carefully avoided**. The process was termed as nomination on the recommendation of certain bodies.",
                "icon": "fa-align-left"
            },
            {
                "question": "What notice period was required for members to ask questions under the 1892 Act?",
                "answer": "A notice of **six days** was mandatory, and the President of the Council could disallow any question without stating reasons.",
                "icon": "fa-clock"
            }
        ]
    },
    "traps": {
        "title": "UPSC Civil Services Exam Traps to Avoid",
        "items": [
            "<strong>Trap 1:</strong> Believing that the 1892 Act introduced direct popular elections. In reality, it was a limited, indirect system where local bodies (municipalities, universities, chambers of commerce) made recommendations, which the Viceroy/Governor then nominated.",
            "<strong>Trap 2:</strong> Assuming that members could ask supplementary questions. Under the 1892 Act, members were restricted to asking only the primary question. The right to ask supplementary questions was introduced later by the Morley-Minto Reforms (1909).",
            "<strong>Trap 3:</strong> Thinking that the Act established an Indian majority in the councils. Although it increased the number of non-official Indian members, the British officials still strictly maintained an official majority in both Central and provincial councils."
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Comprehensive analysis of the Indian Councils Act of 1892 for UPSC Prelims and Mains.",
        "sections": [
            {
                "title": "1. Expansion of Legislative Councils & Official Majority",
                "content": "<p>The Indian Councils Act of 1892 was passed largely in response to demands from the Indian National Congress (founded in 1885). A primary change was the expansion of the legislative councils at both the Central (Imperial) and provincial levels.</p><p>For the Central Legislative Council, the number of additional (non-official) members was raised from the previous limit (6 to 12) to a minimum of <strong>10</strong> and a maximum of <strong>16</strong>. Similarly, the provincial councils were expanded; for example, Bengal was raised to 20 members, and the North-Western Provinces and Oudh to 15. However, despite the expansion of non-official seats, the British strictly maintained an <strong>official majority</strong> of government officers in all councils, ensuring they retained absolute legislative control.</p><svg viewBox=\"0 0 800 280\" width=\"100%\" height=\"280\" class=\"responsive-svg-diagram\" style=\"margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 10px;\"><style>.svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: #2c3e50; font-size: 16px; } .svg-node { fill: #fdfefe; stroke: #2980b9; stroke-width: 2px; rx: 6px; ry: 6px; } .svg-split { fill: #ebf5fb; stroke: #2ecc71; stroke-width: 2.5px; rx: 6px; ry: 6px; } .svg-text-bold { font-family: 'Inter', sans-serif; font-size: 11px; fill: #2c3e50; font-weight: 700; } .svg-text { font-family: 'Inter', sans-serif; font-size: 10px; fill: #2c3e50; font-weight: 500; } .svg-arrow { fill: none; stroke: #bdc3c7; stroke-width: 2px; marker-end: url(#arrowhead-1892); }</style><defs><marker id=\"arrowhead-1892\" markerWidth=\"8\" markerHeight=\"6\" refX=\"6\" refY=\"3\" orient=\"auto\"><polygon points=\"0 0, 8 3, 0 6\" fill=\"#bdc3c7\" /></marker></defs><text x=\"20\" y=\"30\" class=\"svg-title\">Central Legislative Council Structure (1892)</text><rect x=\"280\" y=\"40\" width=\"240\" height=\"45\" class=\"svg-split\" /><text x=\"400\" y=\"67\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">Viceroy of India</text><path d=\"M 340 85 L 220 130\" class=\"svg-arrow\" /><path d=\"M 460 85 L 580 130\" class=\"svg-arrow\" /><rect x=\"60\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"200\" y=\"148\" class=\"svg-text-bold\" fill=\"#2980b9\" text-anchor=\"middle\">Official Majority (British Officials)</text><text x=\"200\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">Had absolute voting power to pass bills</text><rect x=\"460\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"600\" y=\"148\" class=\"svg-text-bold\" fill=\"#e74c3c\" text-anchor=\"middle\">Additional Members (10 to 16)</text><text x=\"600\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">Both Official & Non-Official members</text><path d=\"M 600 185 L 600 215\" class=\"svg-arrow\" /><rect x=\"440\" y=\"215\" width=\"320\" height=\"50\" class=\"svg-split\" /><text x=\"600\" y=\"232\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">Non-Official Seats (Indians/Merchants)</text><text x=\"600\" y=\"248\" class=\"svg-text\" text-anchor=\"middle\">Appointed on recommendations of local bodies</text></svg>"
            },
            {
                "title": "2. Budget Discussion & Right to Ask Questions (Interpellation)",
                "content": "<p>Prior to 1892, legislative councils were strictly restricted to debating proposed laws. Under the 1892 Act, the functions of the councils were expanded, giving them two important new deliberative rights: budget discussion and the right to ask questions (interpellation).</p><p>Firstly, members were given the right to discuss the <strong>annual financial statement (budget)</strong>. However, this power was strictly limited: they could express views, but could not propose resolutions, vote on the budget, or divide the house. Secondly, members could ask questions of the executive on matters of public interest. This was subject to a mandatory <strong>six days' notice</strong>. Furthermore, the President of the Council had absolute authority to disallow any question without explaining why, and <strong>no supplementary questions</strong> (follow-ups) were permitted. This marked the absolute infancy of parliamentary questioning in India.</p><div class=\"table-responsive\" style=\"margin: 1.5rem 0; overflow-x: auto; border-radius: 8px; border: 1px solid rgba(128,128,128,0.15);\"><table style=\"width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;\"><thead><tr style=\"background: var(--bg-card); border-bottom: 2px solid rgba(128,128,128,0.15);\"><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 25%;\">Legislative Feature</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 35%;\">Under Indian Councils Act of 1861</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 40%;\">Under Indian Councils Act of 1892</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">Budget discussion</td><td style=\"padding: 12px;\">Completely barred. Financial discussions were prohibited.</td><td style=\"padding: 12px;\">Allowed discussion of the annual financial statement, but no voting.</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1); background: rgba(128,128,128,0.02);\"><td style=\"padding: 12px; font-weight: bold;\">Questioning the Executive</td><td style=\"padding: 12px;\">Not allowed. Members could not interrogate executive actions.</td><td style=\"padding: 12px;\">Allowed with 6 days' notice. No supplementary questions permitted.</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">Veto and Disallowance</td><td style=\"padding: 12px;\">Viceroy held supreme veto over all bills.</td><td style=\"padding: 12px;\">Viceroy maintained veto, and the President of the Council could disallow questions.</td></tr></tbody></table></div>"
            },
            {
                "title": "3. Introduction of Representative Principle & Indirect Elections",
                "content": "<p>The Indian Councils Act of 1892 is historically significant for introducing the elective principle, laying the conceptual groundwork for representative government in modern India. However, the word <strong>'election' was deliberately omitted</strong> from the text of the Act due to conservative opposition in the British Parliament.</p><p>Instead, the Act provided a mechanism where non-official seats were filled via **nomination on the recommendation of specific bodies**. For the Central Legislative Council, the Viceroy nominated members on the recommendation of the provincial legislative councils and the Bengal Chamber of Commerce. For provincial councils, Governors nominated members based on recommendations from district boards, municipalities, universities, zamindars, and trade associations. This indirect election method linked the government with local civic bodies, paving the way for popular representation.</p>"
            }
        ]
    }
}

# ----------------- THEORY GENERATION (HINDI) -----------------
theory_hi = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "भारतीय परिषद अधिनियम, 1892"
    },
    "hero": {
        "title": "भारतीय परिषद अधिनियम, 1892",
        "description": "भारतीय परिषद अधिनियम, 1892 पर महारत हासिल करें—यह भारत के संवैधानिक इतिहास में एक महत्वपूर्ण मील का पत्थर था जिसने विधायी परिषदों का विस्तार किया, अप्रत्यक्ष चुनावों के माध्यम से प्रतिनिधि लोकतंत्र के पहले तत्वों की शुरुआत की, और परिषदों को बजट पर चर्चा करने और कार्यकारी से प्रश्न पूछने का अधिकार दिया।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरएक्टिव यूपीएससी मॉक टेस्ट",
            "description": "1892 के भारतीय परिषद अधिनियम, परिषद विस्तार, बजट चर्चा सीमाओं, अप्रत्यक्ष चुनाव तंत्र और प्रश्न पूछने के अधिकारों के संबंध में अपनी समझ का परीक्षण करें।",
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
        "description": "1892 के भारतीय परिषद अधिनियम की ओर ले जाने वाले और उसके बाद के प्रमुख मील के पत्थर।",
        "cards": [
            {
                "period": "भारतीय परिषद अधिनियम, 1861",
                "date": "1861",
                "details": "कानून बनाने में भारतीयों को शामिल किया और विकेंद्रीकरण की शुरुआत की, लेकिन कार्यकारी कार्यों या वित्त पर परिषदों का कोई नियंत्रण नहीं था।"
            },
            {
                "period": "भारतीय राष्ट्रीय कांग्रेस की स्थापना",
                "date": "1885",
                "details": "बॉम्बे में गठित। इसने तुरंत विधायी परिषद में सुधार, निर्वाचित प्रतिनिधियों को शामिल करने और सार्वजनिक वित्त पर नियंत्रण की मांग की।"
            },
            {
                "period": "भारतीय परिषद अधिनियम, 1892",
                "date": "1892",
                "details": "ब्रिटिश संसद द्वारा पारित। परिषद के आकार का विस्तार किया गया, बजट पर चर्चा और प्रश्न पूछने की अनुमति दी गई, और सिफारिशों के माध्यम से अप्रत्यक्ष चुनावों की शुरुआत की गई।"
            },
            {
                "period": "भारतीय परिषद अधिनियम, 1909 (मार्ले-मिंटो)",
                "date": "1909",
                "details": "1892 के सुधारों के बाद आया, जिसने प्रत्यक्ष चुनाव (सीमित मताधिकार), पूरक प्रश्न और मुसलमानों के लिए अलग निर्वाचन क्षेत्र की शुरुआत की।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के तरीके (Mnemonics)",
        "description": "1892 के भारतीय परिषद अधिनियम के प्रावधानों को याद रखने के लिए मेमोरी हैक्स।",
        "items": [
            {
                "title": "मेमोरी हैक 1",
                "phrase": "\"B-E-Q\"",
                "decryption": "<strong>B</strong>udget (बजट पर चर्चा की अनुमति, लेकिन मतदान नहीं), <strong>E</strong>lection (अप्रत्यक्ष चुनाव प्रणाली - सिफारिशों पर आधारित), <strong>Q</strong>uestions (लोकहित के मामलों पर प्रश्न पूछने का अधिकार - 6 दिन के नोटिस के साथ, कोई पूरक प्रश्न नहीं)।"
            },
            {
                "title": "मेमोरी हैक 2",
                "phrase": "\"न्यूनतम 10 अधिकतम 16\"",
                "decryption": "केंद्रीय विधायी परिषद में अतिरिक्त (गैर-सरकारी) सदस्यों की संख्या बढ़ाकर न्यूनतम 10 और अधिकतम 16 कर दी गई।"
            },
            {
                "title": "मेमोरी हैक 3",
                "phrase": "\"कोई मतदान नहीं, कोई पूरक प्रश्न नहीं\"",
                "decryption": "1892 के अधिनियम की मुख्य सीमाएं याद रखें: सदस्य बजट पर बात कर सकते थे लेकिन वोट नहीं दे सकते थे, और प्रश्न पूछ सकते थे लेकिन अनुवर्ती (पूरक) प्रश्न नहीं पूछ सकते थे।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड",
        "description": "अभ्यास प्रश्नों को हल करने से पहले त्वरित पुनरीक्षण।",
        "items": [
            {
                "question": "क्या 1892 के भारतीय परिषद अधिनियम ने सदस्यों को बजट पर मतदान करने की अनुमति दी थी?",
                "answer": "नहीं। सदस्य **बजट पर चर्चा** कर सकते थे, लेकिन उन्हें **मतदान करने** या कोई प्रस्ताव रखने का कोई अधिकार नहीं था।",
                "icon": "fa-sack-dollar"
            },
            {
                "question": "प्रतिनिधित्व के संबंध में 1892 के अधिनियम का क्या महत्व है?",
                "answer": "इसने स्थानीय निकायों की सिफारिशों के आधार पर गैर-सरकारी सीटों को भरकर **अप्रत्यक्ष चुनाव का पहला तत्व** पेश किया।",
                "icon": "fa-check-to-slot"
            },
            {
                "question": "क्या 1892 के अधिनियम के पाठ में 'चुनाव' (election) शब्द का स्पष्ट रूप से उपयोग किया गया था?",
                "answer": "नहीं, **'चुनाव' शब्द के प्रयोग से सावधानीपूर्वक बचा गया** था। इस प्रक्रिया को कुछ निकायों की सिफारिशों पर नामांकन के रूप में वर्णित किया गया था।",
                "icon": "fa-align-left"
            },
            {
                "question": "1892 के अधिनियम के तहत सदस्यों को प्रश्न पूछने के लिए कितने दिन पहले नोटिस देना आवश्यक था?",
                "answer": "कम से कम **छह दिन** का नोटिस अनिवार्य था, और परिषद का अध्यक्ष बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार कर सकता था।",
                "icon": "fa-clock"
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा में बचने योग्य जाल (Common Traps)",
        "items": [
            "<strong>जाल 1:</strong> यह मान लेना कि 1892 के अधिनियम ने प्रत्यक्ष रूप से आम चुनाव शुरू किए थे। वास्तव में, यह एक सीमित, अप्रत्यक्ष प्रणाली थी जहाँ स्थानीय निकाय (नगर पालिकाएँ, विश्वविद्यालय, वाणिज्य मंडल) सिफारिशें करते थे, जिन्हें वायसराय/गवर्नर द्वारा नामांकित किया जाता था।",
            "<strong>जाल 2:</strong> यह मान लेना कि सदस्य पूरक प्रश्न पूछ सकते थे। 1892 के अधिनियम के तहत, सदस्य केवल प्राथमिक प्रश्न पूछने तक सीमित थे। पूरक (अनुवर्ती) प्रश्न पूछने का अधिकार बाद में मार्ले-मिंटो सुधार (1909) द्वारा पेश किया गया था।",
            "<strong>जाल 3:</strong> यह सोचना कि अधिनियम ने परिषदों में भारतीयों का बहुमत स्थापित किया था। यद्यपि इसने गैर-सरकारी भारतीय सदस्यों की संख्या में वृद्धि की, लेकिन अंग्रेजों ने केंद्रीय और प्रांतीय दोनों परिषदों में सरकारी बहुमत (सरकारी अधिकारियों का बहुमत) को सख्ती से बनाए रखा।"
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (गहन अध्ययन)",
        "description": "यूपीएससी प्रारंभिक और मुख्य परीक्षा के लिए 1892 के भारतीय परिषद अधिनियम का व्यापक विश्लेषण।",
        "sections": [
            {
                "title": "1. विधायी परिषदों का विस्तार और सरकारी बहुमत",
                "content": "<p>1892 का भारतीय परिषद अधिनियम मुख्य रूप से भारतीय राष्ट्रीय कांग्रेस (1885 में स्थापित) की मांगों के जवाब में पारित किया गया था। इसका एक प्राथमिक बदलाव केंद्रीय (शाही) और प्रांतीय दोनों स्तरों पर विधायी परिषदों का विस्तार था।</p><p>केंद्रीय विधायी परिषद के लिए, अतिरिक्त (गैर-सरकारी) सदस्यों की संख्या को पिछली सीमा (6 से 12) से बढ़ाकर न्यूनतम <strong>10</strong> और अधिकतम <strong>16</strong> कर दिया गया। इसी तरह, प्रांतीय परिषदों का विस्तार किया गया; उदाहरण के लिए, बंगाल में सदस्यों की संख्या बढ़ाकर 20 और उत्तर-पश्चिमी प्रांतों तथा अवध के लिए 15 कर दी गई। हालांकि, गैर-सरकारी सीटों में वृद्धि के बावजूद, अंग्रेजों ने सभी परिषदों में सरकारी अधिकारियों का <strong>सरकारी बहुमत</strong> सख्ती से बनाए रखा, जिससे यह सुनिश्चित हुआ कि उनके पास पूर्ण विधायी नियंत्रण बना रहे।</p><svg viewBox=\"0 0 800 280\" width=\"100%\" height=\"280\" class=\"responsive-svg-diagram\" style=\"margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 10px;\"><style>.svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: #2c3e50; font-size: 16px; } .svg-node { fill: #fdfefe; stroke: #2980b9; stroke-width: 2px; rx: 6px; ry: 6px; } .svg-split { fill: #ebf5fb; stroke: #2ecc71; stroke-width: 2.5px; rx: 6px; ry: 6px; } .svg-text-bold { font-family: 'Inter', sans-serif; font-size: 11px; fill: #2c3e50; font-weight: 700; } .svg-text { font-family: 'Inter', sans-serif; font-size: 10px; fill: #2c3e50; font-weight: 500; } .svg-arrow { fill: none; stroke: #bdc3c7; stroke-width: 2px; marker-end: url(#arrowhead-1892); }</style><defs><marker id=\"arrowhead-1892\" markerWidth=\"8\" markerHeight=\"6\" refX=\"6\" refY=\"3\" orient=\"auto\"><polygon points=\"0 0, 8 3, 0 6\" fill=\"#bdc3c7\" /></marker></defs><text x=\"20\" y=\"30\" class=\"svg-title\">केंद्रीय विधायी परिषद संरचना (1892)</text><rect x=\"280\" y=\"40\" width=\"240\" height=\"45\" class=\"svg-split\" /><text x=\"400\" y=\"67\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">भारत के वायसराय</text><path d=\"M 340 85 L 220 130\" class=\"svg-arrow\" /><path d=\"M 460 85 L 580 130\" class=\"svg-arrow\" /><rect x=\"60\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"200\" y=\"148\" class=\"svg-text-bold\" fill=\"#2980b9\" text-anchor=\"middle\">सरकारी बहुमत (ब्रिटिश अधिकारी)</text><text x=\"200\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">विधेयकों को पारित करने के लिए पूर्ण मतदान शक्ति थी</text><rect x=\"460\" y=\"130\" width=\"280\" height=\"55\" class=\"svg-node\" /><text x=\"600\" y=\"148\" class=\"svg-text-bold\" fill=\"#e74c3c\" text-anchor=\"middle\">अतिरिक्त सदस्य (10 से 16)</text><text x=\"600\" y=\"165\" class=\"svg-text\" text-anchor=\"middle\">सरकारी और गैर-सरकारी दोनों सदस्य</text><path d=\"M 600 185 L 600 215\" class=\"svg-arrow\" /><rect x=\"440\" y=\"215\" width=\"320\" height=\"50\" class=\"svg-split\" /><text x=\"600\" y=\"232\" class=\"svg-text-bold\" fill=\"#27ae60\" text-anchor=\"middle\">गैर-सरकारी सीटें (भारतीय/व्यापारी)</text><text x=\"600\" y=\"248\" class=\"svg-text\" text-anchor=\"middle\">स्थानीय निकायों की सिफारिशों पर नियुक्त</text></svg>"
            },
            {
                "title": "2. बजट चर्चा और प्रश्न पूछने का अधिकार (Interpellation)",
                "content": "<p>1892 से पहले, विधायी परिषदें केवल प्रस्तावित कानूनों पर बहस करने तक सीमित थीं। 1892 के अधिनियम के तहत परिषदों के कार्यों का विस्तार किया गया, जिससे उन्हें दो महत्वपूर्ण नए विमर्शी अधिकार मिले: बजट चर्चा और प्रश्न पूछने का अधिकार।</p><p>सर्वप्रथम, सदस्यों को <strong>वार्षिक वित्तीय विवरण (बजट)</strong> पर चर्चा करने का अधिकार दिया गया। हालांकि, यह शक्ति अत्यंत सीमित थी: वे विचार व्यक्त कर सकते थे, लेकिन वे कोई प्रस्ताव नहीं रख सकते थे, बजट पर मतदान नहीं कर सकते थे, या सदन का विभाजन नहीं कर सकते थे। दूसरे, सदस्यों को सार्वजनिक हित के मामलों पर कार्यकारी से प्रश्न पूछने की अनुमति दी गई। इसके लिए कम से कम <strong>छह दिन का नोटिस</strong> देना अनिवार्य था। इसके अलावा, परिषद के अध्यक्ष को बिना कोई कारण बताए किसी भी प्रश्न को अस्वीकार करने का पूर्ण अधिकार था, और <strong>कोई पूरक प्रश्न</strong> (follow-ups) पूछने की अनुमति नहीं थी। यह भारत में संसदीय प्रश्नकाल की शुरुआत का प्रतीक था।</p><div class=\"table-responsive\" style=\"margin: 1.5rem 0; overflow-x: auto; border-radius: 8px; border: 1px solid rgba(128,128,128,0.15);\"><table style=\"width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem;\"><thead><tr style=\"background: var(--bg-card); border-bottom: 2px solid rgba(128,128,128,0.15);\"><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 25%;\">विधायी विशेषता</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 35%;\">1861 के भारतीय परिषद अधिनियम के तहत</th><th style=\"padding: 12px; font-weight: bold; color: var(--text-dark); width: 40%;\">1892 के भारतीय परिषद अधिनियम के तहत</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">बजट चर्चा</td><td style=\"padding: 12px;\">पूरी तरह से प्रतिबंधित। वित्तीय चर्चा वर्जित थी।</td><td style=\"padding: 12px;\">वार्षिक वित्तीय विवरण पर चर्चा की अनुमति थी, लेकिन मतदान नहीं।</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1); background: rgba(128,128,128,0.02);\"><td style=\"padding: 12px; font-weight: bold;\">कार्यकारी से प्रश्न पूछना</td><td style=\"padding: 12px;\">अनुमति नहीं थी। सदस्य कार्यकारी कार्यों से पूछताछ नहीं कर सकते थे।</td><td style=\"padding: 12px;\">6 दिन के नोटिस के साथ अनुमति। पूरक प्रश्न पूछने की अनुमति नहीं थी।</td></tr><tr style=\"border-bottom: 1px solid rgba(128,128,128,0.1);\"><td style=\"padding: 12px; font-weight: bold;\">वीटो और निरस्तीकरण</td><td style=\"padding: 12px;\">वायसराय के पास सभी विधेयकों पर वीटो का सर्वोच्च अधिकार था।</td><td style=\"padding: 12px;\">वायसराय ने वीटो बनाए रखा, और परिषद का अध्यक्ष प्रश्नों को अस्वीकार कर सकता था।</td></tr></tbody></table></div>"
            },
            {
                "title": "3. प्रतिनिधित्व सिद्धांत और अप्रत्यक्ष चुनाव की शुरुआत",
                "content": "<p>1892 का भारतीय परिषद अधिनियम आधुनिक भारत में प्रतिनिधि सरकार की वैचारिक नींव रखने के लिए ऐतिहासिक रूप से महत्वपूर्ण है। हालाँकि, ब्रिटिश संसद में रूढ़िवादी विरोध के कारण अधिनियम के पाठ से <strong>'चुनाव' (election) शब्द को जानबूझकर छोड़ दिया गया</strong> था।</p><p>इसके बजाय, अधिनियम ने एक ऐसा तंत्र प्रदान किया जहाँ गैर-सरकारी सीटों को **विशिष्ट निकायों की सिफारिश पर नामांकन** के माध्यम से भरा जाता था। केंद्रीय विधायी परिषद के लिए, वायसराय ने प्रांतीय विधायी परिषदों और बंगाल चैंबर ऑफ कॉमर्स की सिफारिश पर सदस्यों को नामांकित किया। प्रांतीय परिषदों के लिए, गवर्नरों ने जिला बोर्डों, नगर पालिकाओं, विश्वविद्यालयों, जमींदारों और व्यापार संघों की सिफारिशों के आधार पर सदस्यों को नामांकित किया। अप्रत्यक्ष चुनाव की इस पद्धति ने सरकार को स्थानीय नागरिक निकायों से जोड़ा, जिसने आगे चलकर लोकप्रिय प्रतिनिधित्व का मार्ग प्रशस्त किया।</p>"
            }
        ]
    }
}

with open(os.path.join(BASE_DIR, "theory.json"), "w", encoding="utf-8") as f:
    json.dump(theory_en, f, ensure_ascii=False, indent=4)

with open(os.path.join(HI_DIR, "theory.json"), "w", encoding="utf-8") as f:
    json.dump(theory_hi, f, ensure_ascii=False, indent=4)

print("Theory JSON files for 1892 generated successfully.")
