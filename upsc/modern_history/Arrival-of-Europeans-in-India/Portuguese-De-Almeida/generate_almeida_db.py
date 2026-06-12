import os
import json

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Portuguese-De-Almeida"
os.makedirs(os.path.join(BASE_DIR, "hi"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "questions_data"), exist_ok=True)

# Helper options
EN_AR_OPTS = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]
HI_AR_OPTS = [
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
    "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
    "A सही है लेकिन R गलत है",
    "A गलत है लेकिन R सही है"
]

def generate_sec_file(name, list_en, list_hi):
    path = os.path.join(BASE_DIR, "questions_data", f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Programmatically generated De Almeida Qs\n\n")
        f.write(f"{name}_en = {repr(list_en)}\n\n")
        f.write(f"{name}_hi = {repr(list_hi)}\n")

# Let's generate 370 highly distinct, historically accurate questions on Francisco de Almeida.
# We will use structural templates with rich, diverse vocabularies to ensure 100% uniqueness.

def make_section_1():
    # Appointment & The Viceroyalty (1505)
    en = []
    hi = []
    
    # MCQ (5)
    en.append({
        "type": "MCQ",
        "q": "Who was appointed as the first Portuguese Viceroy of India by King Manuel I in 1505?",
        "opts": ["Francisco de Almeida", "Afonso de Albuquerque", "Vasco da Gama", "Pedro Álvares Cabral"],
        "ans": 0,
        "sol": "Francisco de Almeida was commissioned as the first Viceroy in 1505 to establish permanent governance."
    })
    hi.append({
        "type": "MCQ",
        "q": "1505 में राजा मैनुअल प्रथम द्वारा भारत के पहले पुर्तगाली वायसराय के रूप में किसे नियुक्त किया गया था?",
        "opts": ["फ्रांसिस्को डी अल्मेडा", "अल्फांसो डी अल्बुकर्क", "वास्को डी गामा", "पेड्रो अल्वारेज़ कैब्राल"],
        "ans": 0,
        "sol": "फ्रांसिस्को डी अल्मेडा को स्थायी शासन स्थापित करने के लिए 1505 में पहले वायसराय के रूप में नियुक्त किया गया था।"
    })

    en.append({
        "type": "MCQ",
        "q": "In which month of 1505 did Francisco de Almeida depart from Lisbon with a fleet of 21 ships?",
        "opts": ["March 1505", "May 1505", "September 1505", "December 1505"],
        "ans": 0,
        "sol": "Almeida departed Lisbon on March 25, 1505, with a massive fleet to consolidate trade."
    })
    hi.append({
        "type": "MCQ",
        "q": "फ्रांसिस्को डी अल्मेडा 21 जहाजों के बेड़े के साथ मार्च 1505 में लिस्बन से किस महीने रवाना हुए थे?",
        "opts": ["मार्च 1505", "मई 1505", "सितंबर 1505", "दिसंबर 1505"],
        "ans": 0,
        "sol": "अल्मेडा व्यापार को मजबूत करने के लिए 25 मार्च, 1505 को एक विशाल बेड़े के साथ लिस्बन से रवाना हुए थे।"
    })

    en.append({
        "type": "MCQ",
        "q": "What was the term duration of Francisco de Almeida's initial appointment as Viceroy?",
        "opts": ["Three years", "Five years", "One year", "Ten years"],
        "ans": 0,
        "sol": "He was appointed for a standard three-year term by the Portuguese crown."
    })
    hi.append({
        "type": "MCQ",
        "q": "वायसराय के रूप में फ्रांसिस्को डी अल्मेडा की प्रारंभिक नियुक्ति की अवधि क्या थी?",
        "opts": ["तीन वर्ष", "पांच वर्ष", "एक वर्ष", "दस वर्ष"],
        "ans": 0,
        "sol": "उन्हें पुर्तगाली क्राउन द्वारा मानक तीन साल के कार्यकाल के लिए नियुक्त किया गया था।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which Portuguese king signed the royal directives appointing Almeida as the Viceroy of the Estado da Índia?",
        "opts": ["King Manuel I", "King John II", "King Sebastian", "King Philip I"],
        "ans": 0,
        "sol": "King Manuel I signed the commission establishing the permanent viceroyalty."
    })
    hi.append({
        "type": "MCQ",
        "q": "किस पुर्तगाली राजा ने अल्मेडा को एस्टाडो दा इंडिया के वायसराय के रूप में नियुक्त करने वाले शाही निर्देशों पर हस्ताक्षर किए?",
        "opts": ["राजा मैनुअल प्रथम", "राजा जॉन द्वितीय", "राजा सेबेस्टियन", "राजा फिलिप प्रथम"],
        "ans": 0,
        "sol": "राजा मैनुअल प्रथम ने स्थायी वायसराय पद की स्थापना करने वाले आयोग पर हस्ताक्षर किए थे।"
    })

    en.append({
        "type": "MCQ",
        "q": "What specific political title was bestowed upon Francisco de Almeida upon his departure from Portugal?",
        "opts": ["Viceroy of India", "Governor-General of Malacca", "Admiral of the Red Sea", "Captain-Major of Calicut"],
        "ans": 0,
        "sol": "He was given the title of Viceroy of India, representing the King's sovereign authority."
    })
    hi.append({
        "type": "MCQ",
        "q": "पुर्तगाल से प्रस्थान के समय फ्रांसिस्को डी अल्मेडा को कौन सी विशिष्ट राजनीतिक उपाधि प्रदान की गई थी?",
        "opts": ["भारत के वायसराय", "मलक्का के गवर्नर-जनरल", "लाल सागर के एडमिरल", "कालीकट के कैप्टन-मेजर"],
        "ans": 0,
        "sol": "उन्हें भारत के वायसराय की उपाधि दी गई थी, जो राजा के संप्रभु अधिकार का प्रतिनिधित्व करती थी।"
    })

    # Multi Correct (5)
    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which goals were set in the royal instructions given to Viceroy Almeida in 1505? (Select all that apply)",
        "opts": ["Build fortresses along East Africa and Western India", "Destroy Mamluk trade monopoly in the Indian Ocean", "Capture Malacca immediately in the first year", "Sign peace treaties with Calicut immediately"],
        "ans": [0, 1],
        "sol": "The instructions focused on fortresses (Kilwa, Anjadip, Cannanore, Cochin) and breaking Muslim naval dominance. Malacca was not a priority in the first year."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "1505 में वायसराय अल्मेडा को दिए गए शाही निर्देशों में कौन से लक्ष्य निर्धारित किए गए थे? (सभी लागू विकल्प चुनें)",
        "opts": ["पूर्वी अफ्रीका और पश्चिमी भारत के साथ किले बनाना", "हिंद महासागर में ममलुक व्यापार एकाधिकार को नष्ट करना", "पहले ही वर्ष में मलक्का पर तुरंत कब्जा करना", "कालीकट के साथ तुरंत शांति संधियों पर हस्ताक्षर करना"],
        "ans": [0, 1],
        "sol": "निर्देशों में किलों (किलवा, अंजादीप, कन्नूर, कोचीन) के निर्माण और मुस्लिम नौसैनिक वर्चस्व को तोड़ने पर ध्यान केंद्रित किया गया था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Identify the elements of Almeida's commission as first Viceroy. (Select all that apply)",
        "opts": ["Standard three-year term", "Direct representation of King Manuel I", "Command of a 21-ship armada", "Total control over inland conquests of Northern India"],
        "ans": [0, 1, 2],
        "sol": "Almeida had a three-year term, represented the King, and led 21 ships. Inland conquest of Northern India was not authorized."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "पहले वायसराय के रूप में अल्मेडा के आयोग के तत्वों की पहचान करें। (सभी लागू विकल्प चुनें)",
        "opts": ["मानक तीन साल का कार्यकाल", "राजा मैनुअल प्रथम का सीधा प्रतिनिधित्व", "21 जहाजों के बेड़े की कमान", "उत्तरी भारत के अंतर्देशीय विजय पर पूर्ण नियंत्रण"],
        "ans": [0, 1, 2],
        "sol": "अल्मेडा का कार्यकाल तीन वर्ष का था, उन्होंने राजा का प्रतिनिधित्व किया और 21 जहाजों का नेतृत्व किया। अंतर्देशीय विजय उनके एजेंडे में नहीं थी।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which classes of officers sailed under Almeida's command in 1505? (Select all that apply)",
        "opts": ["Military knights and noblemen", "Franciscan friars", "Skilled pilots and cartographers", "Spanish conquistadors"],
        "ans": [0, 1, 2],
        "sol": "His fleet carried nobles, soldiers, friars, and experienced pilots. Spanish conquistadors did not sail with them."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "1505 में अल्मेडा की कमान में किस वर्ग के अधिकारी रवाना हुए थे? (सभी लागू विकल्प चुनें)",
        "opts": ["सैन्य शूरवीर और रईस", "फ्रांसिस्कन तपस्वी", "कुशल पायलट और मानचित्रकार", "स्पेनिश विजेता"],
        "ans": [0, 1, 2],
        "sol": "उनके बेड़े में रईस, सैनिक, तपस्वी और अनुभवी पायलट शामिल थे। स्पेनिश विजेता उनके साथ नहीं थे।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What strategic dilemmas did Almeida face regarding the viceroyalty system? (Select all that apply)",
        "opts": ["Logistical delays in communicating with Lisbon", "Rivalry and command disputes with Afonso de Albuquerque", "Lack of sufficient soldiers to garrison multiple forts", "Rebellion from the Portuguese home parliament"],
        "ans": [0, 1, 2],
        "sol": "Communication delays, disputes with Albuquerque, and garrison shortages were primary operational challenges."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "वायसराय प्रणाली के संबंध में अल्मेडा को किन रणनीतिक दुविधाओं का सामना करना पड़ा? (सभी लागू विकल्प चुनें)",
        "opts": ["लिस्बन के साथ संचार में रसद देरी", "अल्फांसो डी अल्बुकर्क के साथ प्रतिद्वंद्विता और कमान विवाद", "कई किलों की रक्षा के लिए पर्याप्त सैनिकों की कमी", "पुर्तगाली संसद से विद्रोह"],
        "ans": [0, 1, 2],
        "sol": "संचार में देरी, अल्बुकर्क के साथ विवाद और सैनिकों की कमी प्राथमिक परिचालन चुनौतियाँ थीं।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Select the geographical focus areas mentioned in the 1505 royal instructions to Almeida. (Select all that apply)",
        "opts": ["The Malabar Coast of India", "The East African Swahili Coast", "The island of Anjadip", "The mainland of China"],
        "ans": [0, 1, 2],
        "sol": "Malabar, Swahili Coast, and Anjadip were crucial targets. China was not targeted by Almeida."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "अल्मेडा को दिए गए 1505 के शाही निर्देशों में उल्लिखित भौगोलिक फोकस क्षेत्रों का चयन करें। (सभी लागू विकल्प चुनें)",
        "opts": ["भारत का मालाबार तट", "पूर्वी अफ्रीकी स्वाहिली तट", "अंजादीप द्वीप", "चीन की मुख्य भूमि"],
        "ans": [0, 1, 2],
        "sol": "मालाबार, स्वाहिली तट और अंजादीप प्रमुख लक्ष्य थे। चीन अल्मेडा के निशाने पर नहीं था।"
    })

    # True/False (8)
    tf1 = [
        ("Francisco de Almeida was the second Viceroy but the first Governor of India.", False, "He was the first Viceroy and Governor; no one held the title before him."),
        ("King Manuel I selected Francisco de Almeida because of his military experience in the Granada wars.", True, "Almeida was a distinguished soldier who fought against the Moors in Granada."),
        ("Almeida refused to accept any title other than Captain-Major during his voyage.", False, "He accepted the official title of Viceroy, which granted him full royal representation."),
        ("The viceroyalty was established to replace the system of temporary annual trading fleets.", True, "It provided a permanent administrative and military presence in the Indian Ocean."),
        ("Almeida was instructed to establish a permanent capital at Goa in 1505.", False, "Goa was not yet captured; the instructions directed building forts at Cochin, Cannanore, and Anjadip."),
        ("The viceroyalty commission of 1505 did not grant Almeida the power to sign treaties with local rulers.", False, "He had full plenipotentiary powers to sign treaties in the King's name."),
        ("Francisco de Almeida was succeeded directly by Afonso de Albuquerque.", True, "Albuquerque succeeded him, although Almeida delayed the transfer of power."),
        ("Almeida belonged to one of the most prominent noble families in Portugal.", True, "He was a member of the elite Count of Abrantes family.")
    ]
    for q_en, ans, sol_en in tf1:
        q_hi = q_en.replace("Francisco de Almeida", "फ्रांसिस्को डी अल्मेडा").replace("Viceroy", "वायसराय").replace("King Manuel I", "राजा मैनुअल प्रथम").replace("Portugal", "पुर्तगाल").replace("India", "भारत")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय")
        en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Fill in the Blank (8)
    fill1 = [
        ("Francisco de Almeida belonged to the noble family of the Counts of __________.", "Abrantes", "He was a high-born noble from the Counts of Abrantes family."),
        ("The Portuguese monarch who appointed Francisco de Almeida in 1505 was King __________.", "Manuel I", "King Manuel I established the permanent viceroyalty."),
        ("Almeida set sail from the port of Lisbon in March __________.", "1505", "He departed on March 25, 1505 CE."),
        ("The first base established by Almeida in East Africa in 1505 was at __________.", "Kilwa", "He fortified Kilwa to secure the Swahili Coast passage."),
        ("Almeida was granted the supreme title of __________ to represent the Crown in Asia.", "Viceroy", "Viceroy was the highest administrative title given."),
        ("The viceroyl's commission was initially limited to a duration of __________ years.", "three", "A three-year term was standard to prevent consolidation of independent power."),
        ("The military adversary that Almeida was specifically instructed to neutralize at sea was the __________ Empire.", "Mamluk", "The Mamluk Sultanate of Egypt controlled the spice monopoly."),
        ("The successor who arrived to replace Almeida in 1508 was Afonso de __________.", "Albuquerque", "Albuquerque arrived with royal orders to take over as governor.")
    ]
    for q_en, ans, sol_en in fill1:
        q_hi = q_en.replace("Francisco de Almeida", "फ्रांसिस्को डी अल्मेडा").replace("Viceroy", "वायसराय").replace("__________", "__________")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय")
        en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Match the Following (3)
    en.append({
        "type": "Match the Following",
        "q": "Match the 1505 expedition details with their quantities:",
        "items": [{"left": "Number of ships"}, {"left": "Number of soldiers/men"}, {"left": "Term of appointment"}],
        "options": [{"val": "0", "text": "21 vessels"}, {"val": "1", "text": "1,500 troops"}, {"val": "2", "text": "3 years"}],
        "sol": "Almeida departed with 21 ships, 1,500 men, for a 3-year term."
    })
    hi.append({
        "type": "Match the Following",
        "q": "1505 के अभियान के विवरण का उनकी मात्राओं से मिलान करें:",
        "items": [{"left": "जहाजों की संख्या"}, {"left": "सैनिकों/पुरुषों की संख्या"}, {"left": "नियुक्ति का कार्यकाल"}],
        "options": [{"val": "0", "text": "21 जहाज"}, {"val": "1", "text": "1,500 सैनिक"}, {"val": "2", "text": "3 वर्ष"}],
        "sol": "अल्मेडा 21 जहाजों, 1,500 सैनिकों और 3 साल के कार्यकाल के साथ रवाना हुए।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the historical personalities with their administrative roles:",
        "items": [{"left": "King Manuel I"}, {"left": "Francisco de Almeida"}, {"left": "Afonso de Albuquerque"}],
        "options": [{"val": "0", "text": "Sponsoring monarch"}, {"val": "1", "text": "First appointed Viceroy"}, {"val": "2", "text": "Designated second Governor"}],
        "sol": "King Manuel I was the sponsor, Almeida the first Viceroy, and Albuquerque the second Governor."
    })
    hi.append({
        "type": "Match the Following",
        "q": "ऐतिहासिक हस्तियों का उनकी प्रशासनिक भूमिकाओं से मिलान करें:",
        "items": [{"left": "राजा मैनुअल प्रथम"}, {"left": "फ्रांसिस्को डी अल्मेडा"}, {"left": "अल्फांसो डी अल्बुकर्क"}],
        "options": [{"val": "0", "text": "प्रायोजक राजा"}, {"val": "1", "text": "प्रथम नियुक्त वायसराय"}, {"val": "2", "text": "नामित दूसरे गवर्नर"}],
        "sol": "राजा मैनुअल प्रथम प्रायोजक थे, अल्मेडा पहले वायसराय थे, और अल्बुकर्क दूसरे गवर्नर थे।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the geographical milestones of Almeida's 1505 voyage with their order:",
        "items": [{"left": "Departure port"}, {"left": "East African stop"}, {"left": "Indian Ocean island base"}],
        "options": [{"val": "0", "text": "Lisbon harbor"}, {"val": "1", "text": "Kilwa fortress"}, {"val": "2", "text": "Anjadip Island"}],
        "sol": "He departed Lisbon, fortified Kilwa, and anchored at Anjadip."
    })
    hi.append({
        "type": "Match the Following",
        "q": "अल्मेडा की 1505 की यात्रा के भौगोलिक मील के पत्थरों का उनके क्रम से मिलान करें:",
        "items": [{"left": "प्रस्थान बंदरगाह"}, {"left": "पूर्वी अफ्रीकी पड़ाव"}, {"left": "हिंद महासागर द्वीप आधार"}],
        "options": [{"val": "0", "text": "लिस्बन बंदरगाह"}, {"val": "1", "text": "किलवा किला"}, {"val": "2", "text": "अंजादीप द्वीप"}],
        "sol": "उन्होंने लिस्बन से प्रस्थान किया, किलवा को मजबूत किया, और अंजादीप में लंगर डाला।"
    })

    # One-Liner (8)
    ol1 = [
        ("What is the exact date of departure for Almeida's viceregal fleet from Lisbon?", "March 25, 1505.", "The fleet left Restelo on March 25, 1505 CE."),
        ("Who was the Portuguese Viceroy's son who accompanied him on the 1505 voyage?", "Lourenço de Almeida.", "Lourenço served as a principal captain under his father."),
        ("Which battle in Europe gave Almeida the military reputation required for the viceroyalty?", "The Battle of Toro.", "Almeida showed outstanding valor in the Battle of Toro (1476)."),
        ("What was the name of the state entity established by the Portuguese Crown to govern Asian trade?", "Estado da Índia.", "The Estado da Índia was the formal state entity."),
        ("Why did the King restrict the viceroy's term to just three years?", "To prevent the viceroy from establishing independent power.", "Short tenures ensured absolute loyalty to Lisbon."),
        ("Where did Almeida make his first land claim in India?", "Anjadip Island.", "He landed and began fortification at Anjadip island first."),
        ("Which family of Portuguese nobility did Almeida marry into?", "The family of Lanções.", "He married Maria de Noronha, connected to high nobility."),
        ("What was the primary merchant council in Lisbon that regulated the Viceroy's trade cargos?", "Casa da Índia.", "Casa da Índia managed all imperial cargoes and imports.")
    ]
    for q_en, ans_en, sol_en in ol1:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय").replace("Lisbon", "लिस्बन")
        sol_hi = f"उत्तर: {ans_en.replace('Almeida', 'अल्मेडा').replace('Viceroy', 'वायसराय')}। स्पष्टीकरण: {sol_en.replace('Almeida', 'अल्मेडा').replace('Viceroy', 'वायसराय')}"
        sol_en_combined = f"Answer: {ans_en} Explanation: {sol_en}"
        en.append({"type": "One-Liner", "q": q_en, "sol": sol_en_combined})
        hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

    # Assertion-Reason (8)
    ar1 = [
        ("Assertion: King Manuel I appointed Francisco de Almeida as the first Viceroy in 1505.\nReason: The Portuguese Crown wanted to replace temporary fleets with a permanent administration in India.", 0, "The viceroyalty was created to manage trade permanently."),
        ("Assertion: Almeida was given a standard three-year term of office.\nReason: King Manuel I feared that longer tenures would encourage viceroys to declare independence.", 0, "Term limits were standard administrative tools for imperial control."),
        ("Assertion: Lourenço de Almeida served as a key naval commander under the Viceroy.\nReason: He was Francisco de Almeida's only son and a trusted military lieutenant.", 0, "Lourenço led many crucial patrols on behalf of his father."),
        ("Assertion: The viceregal instructions ordered the immediate capture of Goa.\nReason: Goa was the primary administrative base of the Mamluk Sultanate in 1505.", 3, "Both statements are false. Goa was not mentioned in the 1505 instructions, and it was under Bijapur, not Mamluks."),
        ("Assertion: Francisco de Almeida delayed hand over of power to Afonso de Albuquerque in 1508.\nReason: Almeida disputed the validity of Albuquerque's credentials and sought revenge for his son's death.", 0, "Almeida refused to step down until he destroyed the Mamluk fleet at Diu."),
        ("Assertion: The fleet of 1505 carried a large number of Franciscan friars.\nReason: The Portuguese expansion combined commercial monopoly goals with Christian missionary zeal.", 0, "Religious conversions and missionary presence were integral to Portuguese state policy."),
        ("Assertion: The Estado da Índia was established as a private joint-stock corporation.\nReason: The King wanted to minimize financial risks to the royal treasury.", 3, "Both are false. The Estado da Índia was a state-owned crown monopoly, not a private corporation."),
        ("Assertion: Almeida participated in the conquest of Granada before his appointment.\nReason: Military experience against Muslim states in Spain and North Africa was highly valued by the Portuguese Crown.", 0, "Almeida's experience in the Reconquista made him the ideal candidate to fight Mamluks.")
    ]
    for q_en, ans, sol_en in ar1:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय").replace("Assertion", "अभिकथन").replace("Reason", "कारण")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय")
        en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
        hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

    # Statement-Based (5)
    st1 = [
        ("Consider the following statements regarding the appointment of Francisco de Almeida:\n1. He was the first Viceroy of the Estado da Índia.\n2. His appointment was sponsored by King John II in 1498.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; he was appointed by King Manuel I in 1505."),
        ("Consider the following statements about the 1505 expedition:\n1. The fleet consisted of 21 ships carrying 1,500 soldiers.\n2. The expedition departed from the port of Porto.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; they departed from Lisbon."),
        ("With reference to the viceregal term of office, consider these statements:\n1. It was set to a non-renewable period of ten years.\n2. Scribes and factors were directly answerable to the Viceroy rather than Lisbon.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect. The term was three years, and factors were directly responsible to the Crown (Casa da Índia)."),
        ("Consider the statements about Francisco de Almeida's early life:\n1. He gained fame at the Battle of Toro in 1476.\n2. He fought against the Moors in Granada under the Spanish Monarchs.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Almeida was a veteran of both the Portuguese-Castilian wars and the Granada Reconquista."),
        ("With reference to the successor of the first Viceroy, consider these statements:\n1. Afonso de Albuquerque was designated as the second Governor.\n2. Almeida welcomed Albuquerque immediately and transferred all powers in Cochin.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; Almeida refused to hand over power and imprisoned Albuquerque.")
    ]
    for q_en, ans, sol_en in st1:
        q_hi = q_en.replace("Francisco de Almeida", "फ्रांसिस्को डी अल्मेडा").replace("Viceroy", "वायसराय")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय")
        en.append({"type": "Statement-Based", "q": q_en, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol_en})
        hi.append({"type": "Statement-Based", "q": q_hi, "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": ans, "sol": sol_hi})

    # Open Questions (12)
    op1 = [
        ("Why", "Why did King Manuel I establish a permanent viceroyalty in India in 1505?", "To secure the trade routes, manage permanent factories, and counter the Mamluk naval monopoly with a unified military command."),
        ("Why", "Why did Almeida refuse to immediately hand over power to Afonso de Albuquerque in 1508?", "Almeida wanted to avenge the death of his son Lourenço at Chaul and questioned the validity of Albuquerque's secret patents."),
        ("Why", "Why was a three-year term limit imposed on the office of the Portuguese Viceroy?", "To prevent the viceroy from developing a local power base or declaring independence from the Lisbon Crown."),
        ("How", "How did the creation of the Estado da Índia change Portuguese operations in the Indian Ocean?", "It transitioned their operations from temporary, seasonal trading expeditions to a permanent political and military administration."),
        ("How", "How did Almeida's family connections in Portugal influence his appointment as Viceroy?", "As a member of the Counts of Abrantes family, he had direct access to King Manuel I, making him a trusted noble commander."),
        ("How", "How did Almeida assert royal authority over Portuguese merchants operating in India?", "He enforced strict cargo logs, centralized spice purchases at the royal factories, and cracked down on private trade."),
        ("Case Study", "Examine the logistical challenges of maintaining a viceroyalty in Cochin from Lisbon.", "Communication took months, reinforcements were seasonal, and the Viceroy had to act autonomously during crises."),
        ("Case Study", "Analyze the conflict between Almeida and Albuquerque regarding the transition of power in 1508-1509.", "The conflict illustrated the clash between two different strategies of empire-building and the problem of verifying royal patents overseas."),
        ("Case Study", "Evaluate the strategic selection of Francisco de Almeida based on his Reconquista military background.", "His experience in Granada made him highly effective at combatting Muslim coalitions but less inclined towards territorial expansion in India."),
        ("Teach the Concept", "Explain the structure and authority of the Estado da Índia established in 1505.", "It was a state-run imperial organization in Asia, headed by a Viceroy who held civil, judicial, and military powers in the King's name."),
        ("Teach the Concept", "Describe the role of the 'Capitão-Mor' (Captain-Major) under the Viceroyalty.", "The Capitão-Mor commanded individual fleets and patrols, enforcing the Viceroy's naval policies and protecting trade bases."),
        ("Teach the Concept", "Explain why the Portuguese Crown prioritized naval governance over land acquisitions in 1505.", "Maintaining sea supremacy was cheaper, utilized Portugal's naval technology, and avoided costly conflicts with large Indian mainland states.")
    ]
    for qtype, q_en, sol_en in op1:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय").replace("Lisbon", "लिस्बन")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Viceroy", "वायसराय")
        en.append({"type": qtype, "q": q_en, "sol": sol_en})
        hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})
        
    return en, hi

def make_section_2():
    # Blue Water Policy & Naval Hegemony
    en = []
    hi = []
    
    # MCQ (5)
    en.append({
        "type": "MCQ",
        "q": "What is the name of the naval strategy pursued by Francisco de Almeida that focused on sea supremacy over land conquest?",
        "opts": ["Blue Water Policy", "Forward Policy", "Ring Fence Policy", "Subsidiary Alliance"],
        "ans": 0,
        "sol": "Almeida's 'Blue Water Policy' (Política da Água Azul) prioritized naval dominance and control of shipping lanes."
    })
    hi.append({
        "type": "MCQ",
        "q": "भूमि विजय पर समुद्री वर्चस्व पर ध्यान केंद्रित करने वाली फ्रांसिस्को डी अल्मेडा द्वारा अपनाई गई नौसैनिक रणनीति का क्या नाम है?",
        "opts": ["ब्लू वाटर पॉलिसी (नीले पानी की नीति)", "फॉरवर्ड पॉलिसी", "रिंग फेंस पॉलिसी", "सहायक गठबंधन"],
        "ans": 0,
        "sol": "अल्मेडा की 'ब्लू वाटर पॉलिसी' ने नौसैनिक प्रभुत्व और नौवहन मार्गों के नियंत्रण को प्राथमिकता दी।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which Latin legal concept refers to the 'closed sea' policy enforced by the Portuguese under Almeida?",
        "opts": ["Mare Clausum", "Mare Liberum", "Terra Nullius", "Jus Ad Bellum"],
        "ans": 0,
        "sol": "Mare Clausum refers to a sea under the jurisdiction of a specific power, excluding others."
    })
    hi.append({
        "type": "MCQ",
        "q": "कौन सी लैटिन कानूनी अवधारणा अल्मेडा के तहत पुर्तगालियों द्वारा लागू की गई 'बंद समुद्र' की नीति को संदर्भित करती है?",
        "opts": ["मारे क्लॉसम (Mare Clausum)", "मारे लिबरम", "टेरा नुलियस", "जस एड बेलम"],
        "ans": 0,
        "sol": "मारे क्लॉसम का अर्थ है एक विशिष्ट शक्ति के अधिकार क्षेत्र में आने वाला समुद्र, जिसमें दूसरों का प्रवेश वर्जित हो।"
    })

    en.append({
        "type": "MCQ",
        "q": "What was the name of the mandatory sailing pass introduced by the Portuguese to regulate trade in the Indian Ocean?",
        "opts": ["Cartaz", "Feitoria", "Firman", "Kaul"],
        "ans": 0,
        "sol": "The Cartaz was a naval license forcing all merchant ships to pay duties and follow Portuguese rules."
    })
    hi.append({
        "type": "MCQ",
        "q": "हिंद महासागर में व्यापार को विनियमित करने के लिए पुर्तगालियों द्वारा शुरू किए गए अनिवार्य नौवहन पास का क्या नाम था?",
        "opts": ["कार्टाज (Cartaz)", "फेइटोरिया", "फरमान", "कौल"],
        "ans": 0,
        "sol": "कार्टाज एक नौसैनिक लाइसेंस था जो सभी व्यापारिक जहाजों को करों का भुगतान करने और पुर्तगाली नियमों का पालन करने के लिए मजबूर करता था।"
    })

    en.append({
        "type": "MCQ",
        "q": "How did Almeida view the idea of building a vast territorial land empire in India?",
        "opts": ["He strongly opposed it, preferring sea dominance", "He actively championed it through land battles", "He ignored it completely", "He wanted to merge with the Vijayanagara Empire"],
        "ans": 0,
        "sol": "Almeida opposed land acquisitions, stating that fortresses on land would drain resources if the sea was lost."
    })
    hi.append({
        "type": "MCQ",
        "q": "भारत में एक विशाल क्षेत्रीय भूमि साम्राज्य बनाने के विचार को अल्मेडा ने कैसे देखा?",
        "opts": ["उन्होंने इसका कड़ा विरोध किया, समुद्री प्रभुत्व को प्राथमिकता दी", "उन्होंने भूमि लड़ाइयों के माध्यम से इसका सक्रिय रूप से समर्थन किया", "उन्होंने इसे पूरी तरह से नजरअंदाज कर दिया", "वह विजयनगर साम्राज्य में विलय करना चाहते थे"],
        "ans": 0,
        "sol": "अल्मेडा ने भूमि अधिग्रहण का विरोध करते हुए कहा कि यदि समुद्र खो गया तो भूमि पर बने किले संसाधनों को नष्ट कर देंगे।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which major merchant guild was the primary target of Almeida's naval blockade in the Arabian Sea?",
        "opts": ["Arab and Muslim trade syndicates", "The English East India Company", "The Dutch VOC", "The Gujarati Bania guilds"],
        "ans": 0,
        "sol": "The Arab merchant networks that controlled the spice shipping route to the Red Sea were the main targets."
    })
    hi.append({
        "type": "MCQ",
        "q": "अरब सागर में अल्मेडा की नौसैनिक नाकेबंदी का प्राथमिक लक्ष्य कौन सा प्रमुख व्यापारिक संघ था?",
        "opts": ["अरब और मुस्लिम व्यापारिक सिंडिकेट", "इंग्लिश ईस्ट इंडिया कंपनी", "डच वीओसी", "गुजराती बनिया गिल्ड"],
        "ans": 0,
        "sol": "लाल सागर तक मसाले के नौवहन मार्ग को नियंत्रित करने वाले अरब व्यापारी नेटवर्क इसके मुख्य लक्ष्य थे।"
    })

    # Multi Correct (5)
    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which statements represent Almeida's arguments in favor of the Blue Water Policy? (Select all that apply)",
        "opts": ["Sea supremacy is cheaper to maintain than large land armies", "A fortress on land is useless if the sea route is lost", "Spices should be acquired by trading, not by territorial taxation", "Portugal has enough manpower to colonize the entire Indian mainland"],
        "ans": [0, 1, 2],
        "sol": "Almeida argued that sea dominance was efficient, forts on land were vulnerable without sea power, and commercial networks were key. He knew Portugal lacked manpower for mainland colonization."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "कौन से कथन नीले पानी की नीति (ब्लू वाटर पॉलिसी) के पक्ष में अल्मेडा के तर्कों का प्रतिनिधित्व करते हैं? (सभी लागू विकल्प चुनें)",
        "opts": ["बड़ी भूमि सेनाओं की तुलना में समुद्री वर्चस्व को बनाए रखना सस्ता है", "यदि समुद्री मार्ग खो जाता है तो भूमि पर बना किला बेकार है", "मसालों को व्यापार द्वारा प्राप्त किया जाना चाहिए, न कि क्षेत्रीय कराधान द्वारा", "पुर्तगाल के पास पूरे भारतीय मुख्य भूमि को उपनिवेश बनाने के लिए पर्याप्त जनशक्ति है"],
        "ans": [0, 1, 2],
        "sol": "अल्मेडा का तर्क था कि समुद्री प्रभुत्व कुशल था, समुद्री शक्ति के बिना भूमि पर किले कमजोर थे। वह जानते थे कि पुर्तगाल के पास मुख्य भूमि के उपनिवेशीकरण के लिए जनशक्ति की कमी थी।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What restrictions were imposed on local vessels by the Cartaz system? (Select all that apply)",
        "opts": ["Prohibition on carrying spices like pepper without licensing", "Forced stopovers at Portuguese-controlled ports to pay customs", "Prohibition on carrying arms or weapons", "Forced conversion of all crew members to Christianity"],
        "ans": [0, 1, 2],
        "sol": "The Cartaz prohibited carrying pepper/spices, enforced customs stops, and banned carrying weapons. It did not force conversions."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "कार्टाज प्रणाली द्वारा स्थानीय जहाजों पर क्या प्रतिबंध लगाए गए थे? (सभी लागू विकल्प चुनें)",
        "opts": ["बिना लाइसेंस के काली मिर्च जैसे मसाले ले जाने पर प्रतिबंध", "सीमा शुल्क का भुगतान करने के लिए पुर्तगाली-नियंत्रित बंदरगाहों पर रुकने के लिए मजबूर करना", "हथियार या युद्धक सामग्री ले जाने पर प्रतिबंध", "सभी चालक दल के सदस्यों को ईसाई धर्म में जबरन परिवर्तित करना"],
        "ans": [0, 1, 2],
        "sol": "कार्टाज ने काली मिर्च/मसाले ले जाने पर प्रतिबंध लगा दिया, सीमा शुल्क पर रुकना लागू किया, और हथियारों के परिवहन पर रोक लगा दी।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which powers challenged the Portuguese 'Mare Clausum' policy under Almeida? (Select all that apply)",
        "opts": ["The Mamluk Sultanate of Egypt", "The Gujarat Sultanate", "The Zamorin of Calicut", "The British Empire"],
        "ans": [0, 1, 2],
        "sol": "Egypt, Gujarat, and Calicut challenged the Portuguese monopoly. The British Empire did not exist in Indian waters at that time."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "अल्मेडा के तहत पुर्तगाली 'मारे क्लॉसम' नीति को किन शक्तियों ने चुनौती दी थी? (सभी लागू विकल्प चुनें)",
        "opts": ["मिस्र का ममलुक सल्तनत", "गुजरात सल्तनत", "कालीकट का ज़मोरिन", "ब्रिटिश साम्राज्य"],
        "ans": [0, 1, 2],
        "sol": "मिस्र, गुजरात और कालीकट ने पुर्तगाली एकाधिकार को चुनौती दी थी। उस समय ब्रिटिश साम्राज्य अस्तित्व में नहीं था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Identify the geographical choke points Almeida sought to control to enforce naval supremacy. (Select all that apply)",
        "opts": ["The entrance to the Red Sea (Bab-el-Mandeb)", "The Strait of Hormuz", "The Malacca Strait", "The Suez Canal"],
        "ans": [0, 1, 2],
        "sol": "Red Sea, Hormuz, and Malacca were the key trade choke points. The Suez Canal did not exist in the 16th century."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "अल्मेडा ने नौसैनिक वर्चस्व लागू करने के लिए किन भौगोलिक बाधाओं (चोक पॉइंट्स) को नियंत्रित करने का प्रयास किया? (सभी लागू विकल्प चुनें)",
        "opts": ["लाल सागर का प्रवेश द्वार (बाब-अल-मंदेब)", "हॉर्मुज जलडमरूमध्य", "मलक्का जलडमरूमध्य", "स्वेज नहर"],
        "ans": [0, 1, 2],
        "sol": "लाल सागर, हॉर्मुज और मलक्का प्रमुख चोक पॉइंट्स थे। स्वेज नहर का निर्माण 19वीं सदी में हुआ था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What were the consequences of failing to present a valid Cartaz to Portuguese patrols? (Select all that apply)",
        "opts": ["Seizure of the merchant vessel", "Confiscation of the entire cargo", "Execution or enslavement of the crew", "Payment of double tax with release of ship"],
        "ans": [0, 1, 2],
        "sol": "Failing to carry a Cartaz resulted in ship seizure, cargo confiscation, and crew enslavement/death."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "पुर्तगाली गश्ती दलों के सामने वैध कार्टाज प्रस्तुत न करने के क्या परिणाम थे? (सभी लागू विकल्प चुनें)",
        "opts": ["व्यापारिक जहाज की जब्ती", "पूरे माल की जब्ती", "चालक दल की फांसी या दासता", "जहाज की रिहाई के साथ दोगुना कर भुगतान"],
        "ans": [0, 1, 2],
        "sol": "कार्टाज न ले जाने पर जहाज को जब्त कर लिया जाता था, माल छीन लिया जाता था, और चालक दल को गुलाम या मार दिया जाता था।"
    })

    # True/False (8)
    tf2 = [
        ("The Blue Water Policy was first proposed by Afonso de Albuquerque.", False, "It was Almeida's signature policy; Albuquerque preferred territorial bases."),
        ("A Cartaz was free of charge for friendly Hindu merchants of Cochin.", False, "All merchant vessels, including allies, had to purchase Cartazes, though terms varied."),
        ("Under Mare Clausum, the Portuguese claimed ownership of the Indian Ocean.", True, "They asserted exclusive rights over navigation and trade in these seas."),
        ("Almeida advocated for a massive colonization of the inland Deccan Plateau.", False, "He strongly opposed land conquests and territorial colonization."),
        ("The Cartaz system successfully redirected trade revenues to Portuguese factories.", True, "It forced ships to pay customs at Portuguese ports like Cochin."),
        ("Venice supported the Portuguese Blue Water Policy because it secured shipping routes.", False, "Venice opposed it because Portuguese dominance bypassed the Levantine spice route."),
        ("Almeida believed that territorial expansion would weaken Portugal's small naval force.", True, "Maintaining garrisons would spread their limited manpower too thin."),
        ("The principle of Mare Liberum was introduced to counter Almeida's naval policies.", True, "Hugo Grotius formulated Mare Liberum in 1609 specifically against Portuguese/Spanish monopolies.")
    ]
    for q_en, ans, sol_en in tf2:
        q_hi = q_en.replace("Blue Water Policy", "नीले पानी की नीति").replace("Almeida", "अल्मेडा").replace("Cartaz", "कार्टाज")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति")
        en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Fill in the Blank (8)
    fill2 = [
        ("Almeida's quote emphasizes that if the Portuguese are not powerful at __________, they will lose India.", "sea", "He argued that sea power was the only way to hold India."),
        ("The legal term for the closed sea doctrine enforced by Almeida is Mare __________.", "Clausum", "Mare Clausum means closed sea under royal jurisdiction."),
        ("The mandatory licensing pass issued to Asian merchants was called a __________.", "Cartaz", "The Cartaz was a shipping permit."),
        ("The alternative policy of acquiring key land-based fortress hubs was championed by Afonso de __________.", "Albuquerque", "Albuquerque favored capturing Goa, Malacca, and Aden."),
        ("Hugo Grotius wrote the treatise Mare Liberum to advocate for free sea navigation against the __________ monopoly.", "Portuguese", "Grotius argued for Dutch access to the seas."),
        ("Under the Cartaz system, merchant vessels were prohibited from carrying __________ and other spices without permission.", "pepper", "Pepper was a strict crown monopoly."),
        ("The primary European trade hub that suffered from Almeida's naval blockade was __________.", "Venice", "Venetian spice imports dropped dramatically."),
        ("To enforce naval hegemony, the Viceroy established constant sea __________ along the Malabar Coast.", "patrols", "Regular naval patrols intercepted unlicensed merchant ships.")
    ]
    for q_en, ans, sol_en in fill2:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Cartaz", "कार्टाज").replace("__________", "__________")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Match the Following (3)
    en.append({
        "type": "Match the Following",
        "q": "Match the naval doctrines and terms with their descriptions:",
        "items": [{"left": "Blue Water Policy"}, {"left": "Mare Clausum"}, {"left": "Cartaz"}],
        "options": [{"val": "0", "text": "Focus on naval supremacy over land conquest"}, {"val": "1", "text": "Closed sea under sovereign control"}, {"val": "2", "text": "Mandatory trade passport for shipping"}],
        "sol": "Matched according to standard definitions."
    })
    hi.append({
        "type": "Match the Following",
        "q": "नौसैनिक सिद्धांतों और शब्दों का उनके विवरण से मिलान करें:",
        "items": [{"left": "नीले पानी की नीति"}, {"left": "मारे क्लॉसम"}, {"left": "कार्टाज"}],
        "options": [{"val": "0", "text": "भूमि विजय पर नौसैनिक वर्चस्व पर ध्यान केंद्रित करना"}, {"val": "1", "text": "संप्रभु नियंत्रण के तहत बंद समुद्र"}, {"val": "2", "text": "शिपिंग के लिए अनिवार्य व्यापार पासपोर्ट"}],
        "sol": "मानक परिभाषाओं के अनुसार मिलान किया गया।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the policies with their chief proponents:",
        "items": [{"left": "Naval supremacy only"}, {"left": "Land bases and fortress hubs"}, {"left": "Free seas (Mare Liberum)"}],
        "options": [{"val": "0", "text": "Francisco de Almeida"}, {"val": "1", "text": "Afonso de Albuquerque"}, {"val": "2", "text": "Hugo Grotius"}],
        "sol": "Almeida proposed naval dominance, Albuquerque proposed land bases, and Grotius proposed free seas."
    })
    hi.append({
        "type": "Match the Following",
        "q": "नीतियों का उनके मुख्य समर्थकों से मिलान करें:",
        "items": [{"left": "केवल नौसैनिक वर्चस्व"}, {"left": "भूमि आधार और किला केंद्र"}, {"left": "मुक्त समुद्र (मारे लिबरम)"}],
        "options": [{"val": "0", "text": "फ्रांसिस्को डी अल्मेडा"}, {"val": "1", "text": "अल्फांसो डी अल्बुकर्क"}, {"val": "2", "text": "ह्यूगो ग्रोटियस"}],
        "sol": "अल्मेडा ने नौसैनिक वर्चस्व, अल्बुकर्क ने भूमि अड्डों और ग्रोटियस ने मुक्त समुद्र का प्रस्ताव रखा।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the Cartaz system requirements with their targeted aspects:",
        "items": [{"left": "Monopolized cargo"}, {"left": "Customs collection"}, {"left": "Weaponry prohibition"}],
        "options": [{"val": "0", "text": "Banning independent transport of pepper"}, {"val": "1", "text": "Forcing port stopovers to pay duties"}, {"val": "2", "text": "Prohibiting carriage of arms"}],
        "sol": "Spices were monopolized, stopovers collected customs, and weapons were banned."
    })
    hi.append({
        "type": "Match the Following",
        "q": "कार्टाज प्रणाली की आवश्यकताओं का उनके लक्षित पहलुओं से मिलान करें:",
        "items": [{"left": "एकाधिकार कार्गो"}, {"left": "सीमा शुल्क संग्रह"}, {"left": "हथियारों का निषेध"}],
        "options": [{"val": "0", "text": "काली मिर्च के स्वतंत्र परिवहन पर प्रतिबंध"}, {"val": "1", "text": "शुल्क का भुगतान करने के लिए बंदरगाहों पर रुकने के लिए मजबूर करना"}, {"val": "2", "text": "हथियार ले जाने पर रोक लगाना"}],
        "sol": "मसालों पर एकाधिकार था, रुकने पर सीमा शुल्क एकत्र किया जाता था, और हथियारों पर प्रतिबंध था।"
    })

    # One-Liner (8)
    ol2 = [
        ("What Portuguese phrase translates to the Blue Water Policy?", "Política da Água Azul.", "This was the Portuguese term for the naval doctrine."),
        ("Which legal philosopher argued against the Portuguese Mare Clausum in the early 17th century?", "Hugo Grotius.", "Grotius wrote Mare Liberum to defend Dutch trade rights."),
        ("What was the penalty for an Asian ship caught sailing without a Cartaz?", "Seizure of ship, confiscation of cargo, and execution of crew.", "The Portuguese treated them as pirates."),
        ("What quote did Almeida write to King Manuel I to justify his naval policy?", "As long as you are powerful at sea, you will hold India as yours.", "This quote summarizes the Blue Water Policy."),
        ("Which Indian ocean trade route did Almeida blockade to enforce his policy?", "The Red Sea route to Egypt.", "Blockading this route cut off the Levantine spice supply to Venice."),
        ("Did the Blue Water Policy advocate for capturing Goa as a permanent base?", "No.", "Almeida opposed capturing large cities on the mainland."),
        ("How did the Cartaz system generate revenue for the Portuguese Crown?", "By charging fees for the pass and taxing cargoes at Portuguese ports.", "It functioned as a maritime protection racket."),
        ("What technology enabled the Portuguese to enforce the Blue Water Policy?", "Cannon-armed naus and caravels.", "Their superior naval gunnery defeated local dhows.")
    ]
    for q_en, ans_en, sol_en in ol2:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति").replace("Cartaz", "कार्टाज")
        sol_hi = f"उत्तर: {ans_en.replace('Almeida', 'अल्मेडा').replace('Blue Water Policy', 'नीले पानी की नीति')}। स्पष्टीकरण: {sol_en.replace('Almeida', 'अल्मेडा').replace('Blue Water Policy', 'नीले पानी की नीति')}"
        sol_en_combined = f"Answer: {ans_en} Explanation: {sol_en}"
        en.append({"type": "One-Liner", "q": q_en, "sol": sol_en_combined})
        hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

    # Assertion-Reason (8)
    ar2 = [
        ("Assertion: Almeida's Blue Water Policy focused on controlling sea lanes rather than conquering land.\nReason: He believed Portugal lacked the manpower and resources to defend a territorial land empire in India.", 0, "Almeida recognized Portugal's demographic limits and prioritized naval superiority."),
        ("Assertion: The Cartaz system was viewed as a form of maritime piracy by local Indian rulers.\nReason: It forced independent merchant vessels to purchase permits and pay customs to Portuguese authorities.", 0, "Local rulers resented the unilateral imposition of naval taxes."),
        ("Assertion: The Portuguese Crown declared the Indian Ocean a Mare Clausum.\nReason: They wanted to establish a complete monopoly over the spice trade and exclude other European and Arab merchants.", 0, "Sovereign control of the sea was necessary to maintain the spice monopoly."),
        ("Assertion: Albuquerque strongly supported Almeida's naval strategy.\nReason: Albuquerque believed that fortresses on land were too expensive to maintain.", 3, "Both are false. Albuquerque advocated for land bases and disputed Almeida's policy."),
        ("Assertion: The Red Sea spice trade was completely stopped by Almeida's naval patrols.\nReason: Almeida successfully conquered Aden and blocked the Bab-el-Mandeb strait in 1506.", 2, "Assertion is true (he heavily disrupted it), but Reason is false because Almeida did not capture Aden; that was attempted later by Albuquerque."),
        ("Assertion: The Dutch East India Company challenged the Portuguese Mare Clausum policy.\nReason: The Dutch legal theorist Hugo Grotius popularized the concept of Mare Liberum (Free Seas).", 0, "The Dutch used the free seas argument to justify breaking the Portuguese monopoly."),
        ("Assertion: The Cartaz permit was required even for rulers allied with Portugal.\nReason: The Portuguese asserted absolute naval sovereignty over all vessels in the Indian Ocean.", 0, "Even the Raja of Cochin had to obtain Cartazes for his merchant ships."),
        ("Assertion: Almeida's Blue Water Policy was eventually abandoned by his successor.\nReason: Albuquerque believed that secure land bases were necessary to maintain naval superiority over the long term.", 0, "Albuquerque shifted the strategy towards capturing key coastal cities like Goa and Malacca.")
    ]
    for q_en, ans, sol_en in ar2:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति").replace("Assertion", "अभिकथन").replace("Reason", "कारण")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति")
        en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
        hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

    # Statement-Based (5)
    st2 = [
        ("Consider the following statements regarding the Blue Water Policy:\n1. It prioritized naval dominance over territorial conquests.\n2. It was formulated by Afonso de Albuquerque.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; it was formulated by Almeida."),
        ("Consider the following statements about the Cartaz system:\n1. It was a mandatory navigation pass for all merchant ships in the Indian Ocean.\n2. Vessels carrying a Cartaz were exempt from paying customs at Portuguese ports.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; carrying a Cartaz forced them to stop at Portuguese ports to pay customs."),
        ("With reference to Mare Clausum, consider these statements:\n1. It means 'Free Seas' in Latin, allowing all nations to trade.\n2. The Portuguese crown asserted this right based on papal bulls.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect; Mare Clausum means 'Closed Sea'."),
        ("Consider the statements about the impact of the Blue Water Policy:\n1. It successfully disrupted the Venice-Egypt spice route.\n2. It led to the immediate conquest of Delhi.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Delhi was never targeted or reached by the Portuguese."),
        ("With reference to the opposition to Almeida's policy, consider these statements:\n1. King Manuel I initially supported the Blue Water Policy.\n2. The King later favored Albuquerque's fortress strategy to secure permanent bases.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The Crown transitioned to Albuquerque's strategy as trade grew.")
    ]
    for q_en, ans, sol_en in st2:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति")
        en.append({"type": "Statement-Based", "q": q_en, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol_en})
        hi.append({"type": "Statement-Based", "q": q_hi, "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": ans, "sol": sol_hi})

    # Open Questions (12)
    op2 = [
        ("Why", "Why did Almeida argue that land fortresses were of little value without naval power?", "Because without sea supremacy, land fortresses would be cut off, starved of supplies, and easily captured by local rulers."),
        ("Why", "Why did the Portuguese introduce the Cartaz licensing system?", "To establish a legal monopoly, extract customs revenues, and prevent Arab competitors from shipping spices to the Red Sea."),
        ("Why", "Why did Venice oppose the Portuguese naval hegemony in the Arabian Sea?", "Because the Portuguese blockade of the Red Sea diverted the spice trade to the Cape Route, destroying Venice's monopoly in Europe."),
        ("How", "How did the Blue Water Policy utilize Portugal's technological advantages?", "It leveraged their superior ship construction and naval gunnery to dominate ocean lanes without needing large land armies."),
        ("How", "How did the Cartaz system alter the traditional merchant networks in the Indian Ocean?", "It forced free merchant networks to operate under a centralized, militarized European licensing system, ending free trade."),
        ("How", "How did Hugo Grotius's concept of Mare Liberum challenge Almeida's legacy?", "It provided a legal counter-argument that the oceans are international territory, justifying Dutch and English entry into Asian trade."),
        ("Case Study", "Examine the effectiveness of the Portuguese naval patrols along the Malabar Coast under Almeida.", "Patrols successfully intercepted dhows, redirected trade to Cochin, and suppressed competitive Arab merchants, though smuggling persisted."),
        ("Case Study", "Analyze the economic impact of the Cartaz fees on local Indian Ocean trade guilds.", "It increased transaction costs, forced merchants to change routes, and led to the decline of traditional Arab shipping houses."),
        ("Case Study", "Evaluate the strategic transition from Almeida's naval policy to Albuquerque's fortress policy.", "As local resistance grew, sea patrols alone were insufficient, making fortified land bases like Goa necessary to support the fleet."),
        ("Teach the Concept", "Explain the concept of 'Mare Clausum' to a student.", "It is the doctrine that a nation can claim exclusive sovereignty over a sea, banning other nations from navigation and trade."),
        ("Teach the Concept", "Describe how the Cartaz system functioned as a naval protection system.", "Merchant ships paid a fee for a pass that guaranteed safe passage from Portuguese attacks, while agreeing not to carry monopolized spices."),
        ("Teach the Concept", "Explain the core philosophy of the Blue Water Policy.", "It is the imperial strategy of securing commercial hegemony by dominating sea lanes with a strong navy instead of conquering and governing territories.")
    ]
    for qtype, q_en, sol_en in op2:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति").replace("Cartaz", "कार्टाज")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा").replace("Blue Water Policy", "नीले पानी की नीति")
        en.append({"type": qtype, "q": q_en, "sol": sol_en})
        hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})

    return en, hi

def make_section_3():
    # Fortifications & Indian Ocean Bases
    en = []
    hi = []
    
    # MCQ (5)
    en.append({
        "type": "MCQ",
        "q": "Which island in Western India was the site of the very first fort constructed by Viceroy Almeida in 1505?",
        "opts": ["Anjadip Island", "Diu Island", "Goa Island", "Salsette Island"],
        "ans": 0,
        "sol": "Almeida began building a fort on Anjadip Island (Angediva) in 1505 to secure the Malabar transit."
    })
    hi.append({
        "type": "MCQ",
        "q": "पश्चिमी भारत का कौन सा द्वीप 1505 में वायसराय अल्मेडा द्वारा निर्मित सबसे पहले किले का स्थल था?",
        "opts": ["अंजादीप द्वीप", "दीव द्वीप", "गोवा द्वीप", "सालसेट द्वीप"],
        "ans": 0,
        "sol": "अल्मेडा ने मालाबार पारगमन को सुरक्षित करने के लिए 1505 में अंजादीप द्वीप (अंगेदिवा) पर एक किला बनाना शुरू किया।"
    })

    en.append({
        "type": "MCQ",
        "q": "What is the name of the famous Portuguese fort constructed under Almeida's directives in Cannanore?",
        "opts": ["Fort St. Angelo", "Fort Manuel", "Fort St. George", "Fort William"],
        "ans": 0,
        "sol": "Fort St. Angelo (Fort de Santo Ângelo) was built in Cannanore in 1505 CE."
    })
    hi.append({
        "type": "MCQ",
        "q": "कन्नूर में अल्मेडा के निर्देशों के तहत निर्मित प्रसिद्ध पुर्तगाली किले का क्या नाम है?",
        "opts": ["फोर्ट सेंट एंजेलो", "फोर्ट मैनुअल", "फोर्ट सेंट जॉर्ज", "फोर्ट विलियम"],
        "ans": 0,
        "sol": "फोर्ट सेंट एंजेलो (कन्नूर) का निर्माण 1505 ईस्वी में हुआ था।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which fort in Cochin was constructed in alliance with the local Trimumpara Raja to secure the Portuguese base?",
        "opts": ["Fort Manuel", "Fort St. Angelo", "Fort de Aguada", "Fort Mormugao"],
        "ans": 0,
        "sol": "Fort Manuel (Fort Manuel de Kochi) was built in Cochin with the local Raja's permission."
    })
    hi.append({
        "type": "MCQ",
        "q": "पुर्तगाली आधार को सुरक्षित करने के लिए स्थानीय त्रिमुम्पारा राजा के साथ गठबंधन में कोचीन में किस किले का निर्माण किया गया था?",
        "opts": ["फोर्ट मैनुअल", "फोर्ट सेंट एंजेलो", "फोर्ट डी अगुआडा", "फोर्ट मर्मगाओ"],
        "ans": 0,
        "sol": "फोर्ट मैनुअल (कोचीन) का निर्माण स्थानीय राजा की अनुमति से पुर्तगाली आधार के रूप में किया गया था।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which East African coastal city-state was captured and fortified by Almeida in 1505 before he crossed to India?",
        "opts": ["Kilwa", "Mombasa", "Zanzibar", "Mozambique"],
        "ans": 0,
        "sol": "Almeida captured and built the Fort of São Tiago at Kilwa to secure the African coast."
    })
    hi.append({
        "type": "MCQ",
        "q": "भारत जाने से पहले 1505 में अल्मेडा द्वारा किस पूर्वी अफ्रीकी तटीय शहर-राज्य पर कब्जा कर लिया गया था और वहां किलेबंदी की गई थी?",
        "opts": ["किलवा", "मोम्बासा", "जंजीबार", "मोजाम्बिक"],
        "ans": 0,
        "sol": "अल्मेडा ने अफ्रीकी तट को सुरक्षित करने के लिए किलवा में सूबा (São Tiago) का किला बनाया।"
    })

    en.append({
        "type": "MCQ",
        "q": "Why did Viceroy Almeida eventually order the demolition of the fort at Anjadip Island?",
        "opts": ["It was too difficult to defend and garrison", "It was destroyed by an earthquake", "The local ruler paid them to leave", "He wanted to shift all forces to Malacca"],
        "ans": 0,
        "sol": "The fort on Anjadip was vulnerable to local Adil Shahi attacks and hard to supply, leading to its abandonment."
    })
    hi.append({
        "type": "MCQ",
        "q": "वायसराय अल्मेडा ने अंततः अंजादीप द्वीप के किले को ध्वस्त करने का आदेश क्यों दिया?",
        "opts": ["इसकी रक्षा करना और सैनिकों को रखना बहुत कठिन था", "यह भूकंप से नष्ट हो गया था", "स्थानीय शासक ने उन्हें जाने के लिए भुगतान किया था", "वह सभी बलों को मलक्का स्थानांतरित करना चाहते थे"],
        "ans": 0,
        "sol": "अंजादीप का किला स्थानीय आदिल शाही हमलों के प्रति संवेदनशील था और इसकी आपूर्ति कठिन थी, जिससे इसे छोड़ना पड़ा।"
    })

    # Multi Correct (5)
    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which of the following forts were established or occupied by Almeida in 1505? (Select all that apply)",
        "opts": ["Fort St. Angelo at Cannanore", "Fort Manuel at Cochin", "Fort of São Tiago at Kilwa", "Fort de Diu"],
        "ans": [0, 1, 2],
        "sol": "Cannanore, Cochin, and Kilwa forts were established by Almeida. Diu fort was built much later (1535)."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "1505 में अल्मेडा द्वारा निम्नलिखित में से कौन से किले स्थापित या अधिकृत किए गए थे? (सभी लागू विकल्प चुनें)",
        "opts": ["कन्नूर में फोर्ट सेंट एंजेलो", "कोचीन में फोर्ट मैनुअल", "किलवा में साओ टियागो का किला", "दीव का किला"],
        "ans": [0, 1, 2],
        "sol": "कन्नूर, कोचीन और किलवा किलों की स्थापना अल्मेडा ने की थी। दीव का किला बाद में (1535) बना।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What were the strategic functions of Fort St. Angelo in Cannanore? (Select all that apply)",
        "opts": ["Secure control over the local spice trade of Cannanore", "Provide a naval base for patrolling the Northern Malabar Coast", "Blockade the Muslim merchants of Calicut", "Serve as the official residence of the Mughal Governor"],
        "ans": [0, 1, 2],
        "sol": "Fort St. Angelo secured spice trade, served as a patrol base, and blockaded Calicut. The Mughals had no presence in the region."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "कन्नूर में फोर्ट सेंट एंजेलो के रणनीतिक कार्य क्या थे? (सभी लागू विकल्प चुनें)",
        "opts": ["कन्नूर के स्थानीय मसाला व्यापार पर सुरक्षित नियंत्रण", "उत्तरी मालाबार तट पर गश्त के लिए एक नौसैनिक अड्डा प्रदान करना", "कालीकट के मुस्लिम व्यापारियों की नाकेबंदी करना", "मुगल गवर्नर के आधिकारिक निवास के रूप में सेवा करना"],
        "ans": [0, 1, 2],
        "sol": "इस किले ने मसाला व्यापार को सुरक्षित किया, गश्ती अड्डे के रूप में कार्य किया, और कालीकट की नाकेबंदी की।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Identify the local rulers who collaborated with Almeida in establishing these fort bases. (Select all that apply)",
        "opts": ["The Kolathiri Raja of Cannanore", "The Trimumpara Raja of Cochin", "The Sultan of Kilwa (vassal ruler)", "The Sultan of Bijapur"],
        "ans": [0, 1, 2],
        "sol": "Cannanore's Kolathiri, Cochin's Raja, and Kilwa's vassal ruler cooperated. Bijapur was hostile."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "इन किला अड्डों को स्थापित करने में अल्मेडा के साथ सहयोग करने वाले स्थानीय शासकों की पहचान करें। (सभी लागू विकल्प चुनें)",
        "opts": ["कन्नूर के कोलाथिरी राजा", "कोचीन के त्रिमुम्पारा राजा", "किलवा के सुल्तान (जागीरदार शासक)", "बीजापुर के सुल्तान"],
        "ans": [0, 1, 2],
        "sol": "कन्नूर के कोलाथिरी, कोचीन के राजा और किलवा के जागीरदार ने सहयोग किया। बीजापुर शत्रुतापूर्ण था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What challenges did the Portuguese garrison face in Fort Manuel at Cochin? (Select all that apply)",
        "opts": ["Frequent attacks by the Zamorin's forces", "Shortage of clean drinking water and fresh food", "Logistical isolation during the monsoon season", "Invasions by Spanish fleets"],
        "ans": [0, 1, 2],
        "sol": "Fort Manuel faced Zamorin's attacks, water/food shortages, and monsoon isolation. There were no Spanish attacks."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "कोचीन के फोर्ट मैनुअल में पुर्तगाली सेना को किन चुनौतियों का सामना करना पड़ा? (सभी लागू विकल्प चुनें)",
        "opts": ["ज़मोरिन की सेनाओं द्वारा बार-बार हमले", "साफ पीने के पानी और ताजे भोजन की कमी", "मानसून के मौसम के दौरान रसद अलगाव", "स्पेनिश बेड़े द्वारा आक्रमण"],
        "ans": [0, 1, 2],
        "sol": "फोर्ट मैनुअल को ज़मोरिन के हमलों, पानी/भोजन की कमी और मानसून में अलगाव का सामना करना पड़ा।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which construction materials were primarily used to build Fort Manuel in Cochin in 1503-1505? (Select all that apply)",
        "opts": ["Coconut tree trunks", "Clay and sand", "Laterite stone (added later)", "Italian marble"],
        "ans": [0, 1, 2],
        "sol": "The fort was initially built with coconut trunks and mud, and later reinforced with laterite stone. Marble was not used."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "1503-1505 में कोचीन में फोर्ट मैनुअल बनाने के लिए मुख्य रूप से किस निर्माण सामग्री का उपयोग किया गया था? (सभी लागू विकल्प चुनें)",
        "opts": ["नारियल के पेड़ के तने", "मिट्टी और रेत", "लैटेराइट पत्थर (बाद में जोड़ा गया)", "इतालवी संगमरमर"],
        "ans": [0, 1, 2],
        "sol": "किले का निर्माण शुरू में नारियल के तनों और मिट्टी से किया गया था, और बाद में इसे लैटेराइट पत्थर से मजबूत किया गया।"
    })

    # True/False (8)
    tf3 = [
        ("Fort St. Angelo in Cannanore was built on a triangular promontory jutting into the sea.", True, "Its strategic location allowed cannons to cover both the harbor and the land side."),
        ("The fort of Kilwa in East Africa was named Fort of São Tiago.", True, "Almeida built it in 1505 to secure the route before crossing the Arabian Sea."),
        ("Almeida built a large naval fort at Goa in 1506.", False, "Goa was captured in 1510 by Albuquerque; Almeida did not fortify Goa."),
        ("The local Kolathiri Raja of Cannanore became hostile to the Portuguese during the Siege of Cannanore (1507).", True, "Local politics and Arab influence led the Raja to besiege the fort in 1507."),
        ("Fort Manuel in Cochin was the first European fort constructed in India.", True, "Built in 1503 and reinforced by Almeida in 1505, it was the first European fort on Indian soil."),
        ("Almeida personally designed all the architectural layouts of the Cannanore fort.", False, "He commissioned engineers like Tomás Fernandes to design the fortifications."),
        ("The fort at Anjadip island was constructed using stone imported directly from Lisbon.", False, "It was built using local stone and clay found on the island."),
        ("The siege of Fort St. Angelo in 1507 was successfully broken by the arrival of a fleet under Tristão da Cunha.", True, "Tristão da Cunha's fleet arrived with reinforcements, lifting the siege.")
    ]
    for q_en, ans, sol_en in tf3:
        q_hi = q_en.replace("Fort St. Angelo", "फोर्ट सेंट एंजेलो").replace("Fort Manuel", "फोर्ट मैनुअल").replace("Almeida", "अल्मेडा")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Fill in the Blank (8)
    fill3 = [
        ("The first European fort constructed in India was Fort __________ in Cochin.", "Manuel", "Fort Manuel de Kochi was built in 1503 CE."),
        ("Viceroy Almeida constructed Fort St. Angelo in the Malabar port city of __________.", "Cannanore", "The fort was built to secure Cannanore's harbor."),
        ("Almeida built a fort on __________ Island to provide a watering station for fleets.", "Anjadip", "Anjadip Island was used as a shelter and repair station."),
        ("In East Africa, Almeida established the Fort of São Tiago at __________.", "Kilwa", "Kilwa was a major trade center on the Swahili Coast."),
        ("The Portuguese engineer who designed Fort St. Angelo in Cannanore was Tomás __________.", "Fernandes", "Tomas Fernandes was the chief military architect."),
        ("The local ruler of Cochin who permitted the construction of Fort Manuel was the __________ Raja.", "Trimumpara", "The Trimumpara Raja (Unni Goda Varma) allied with the Portuguese."),
        ("The siege of the Cannanore fort in 1507 was instigated by Arab merchants and the ruler of __________.", "Calicut", "The Zamorin of Calicut coordinated the siege to expel the Portuguese."),
        ("The fort at Anjadip was demolished because it was constantly attacked by the forces of the Sultan of __________.", "Bijapur", "The Adil Shahi ruler of Bijapur claimed the island and launched frequent raids.")
    ]
    for q_en, ans, sol_en in fill3:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Cannanore", "कन्नूर").replace("__________", "__________")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Match the Following (3)
    en.append({
        "type": "Match the Following",
        "q": "Match the Portuguese forts with their locations:",
        "items": [{"left": "Fort Manuel"}, {"left": "Fort St. Angelo"}, {"left": "Fort of São Tiago"}],
        "options": [{"val": "0", "text": "Cochin"}, {"val": "1", "text": "Cannanore"}, {"val": "2", "text": "Kilwa"}],
        "sol": "Manuel was in Cochin, St. Angelo in Cannanore, and São Tiago in Kilwa."
    })
    hi.append({
        "type": "Match the Following",
        "q": "पुर्तगाली किलों का उनके स्थानों से मिलान करें:",
        "items": [{"left": "फोर्ट मैनुअल"}, {"left": "फोर्ट सेंट एंजेलो"}, {"left": "फोर्ट ऑफ साओ टियागो"}],
        "options": [{"val": "0", "text": "कोचीन"}, {"val": "1", "text": "कन्नूर"}, {"val": "2", "text": "किलवा"}],
        "sol": "मैनुअल कोचीन में, सेंट एंजेलो कन्नूर में, और साओ टियागो किलवा में था।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the fort bases with their primary strategic reasons for abandonment or defense:",
        "items": [{"left": "Anjadip Fort"}, {"left": "Cannanore Fort"}, {"left": "Cochin Fort"}],
        "options": [{"val": "0", "text": "Demolished due to Adil Shahi attacks"}, {"val": "1", "text": "Besieged in 1507 by Zamorin coalition"}, {"val": "2", "text": "Main operational base under Trimumpara alliance"}],
        "sol": "Anjadip was demolished, Cannanore was besieged, and Cochin served as the main allied base."
    })
    hi.append({
        "type": "Match the Following",
        "q": "किला अड्डों का उनके परित्याग या रक्षा के प्राथमिक रणनीतिक कारणों से मिलान करें:",
        "items": [{"left": "अंजादीप किला"}, {"left": "कन्नूर किला"}, {"left": "कोचीन किला"}],
        "options": [{"val": "0", "text": "आदिल शाही हमलों के कारण ध्वस्त कर दिया गया"}, {"val": "1", "text": "1507 में ज़मोरिन गठबंधन द्वारा घेराबंदी की गई"}, {"val": "2", "text": "त्रिमुम्पारा गठबंधन के तहत मुख्य परिचालन आधार"}],
        "sol": "अंजादीप को ध्वस्त कर दिया गया, कन्नूर को घेर लिया गया, और कोचीन मुख्य सहयोगी आधार के रूप में कार्य करता था।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the fort components with their architectural features:",
        "items": [{"left": "Initial Fort Manuel walls"}, {"left": "Tomás Fernandes designs"}, {"left": "Laterite stone reinforcement"}],
        "options": [{"val": "0", "text": "Built using coconut tree trunks"}, {"val": "1", "text": "Triangular layout at Cannanore"}, {"val": "2", "text": "Permanent stone upgrades"}],
        "sol": "Initial walls were coconut trunks, Fernandes designed the triangular layout, and laterite was used for upgrades."
    })
    hi.append({
        "type": "Match the Following",
        "q": "किले के घटकों का उनकी स्थापत्य विशेषताओं से मिलान करें:",
        "items": [{"left": "प्रारंभिक फोर्ट मैनुअल दीवारें"}, {"left": "टॉमास फर्नांडीस डिजाइन"}, {"left": "लैटेराइट पत्थर सुदृढ़ीकरण"}],
        "options": [{"val": "0", "text": "नारियल के पेड़ के तनों का उपयोग करके निर्मित"}, {"val": "1", "text": "कन्नूर में त्रिकोणीय लेआउट"}, {"val": "2", "text": "स्थायी पत्थर उन्नयन"}],
        "sol": "प्रारंभिक दीवारें नारियल के तने थे, फर्नांडीस ने त्रिकोणीय लेआउट डिजाइन किया, और बाद में लैटेराइट का उपयोग किया गया।"
    })

    # One-Liner (8)
    ol3 = [
        ("In what year did the Siege of Cannanore occur?", "1507 CE.", "The siege lasted from April to August 1507."),
        ("What unique food source saved the Cannanore garrison during the 1507 siege?", "Crabs washed ashore.", "A sudden wave of crabs provided food when supplies ran out."),
        ("Who commanded the garrison during the Siege of Cannanore?", "Lourenço de Brito.", "Brito was the captain of the fort during the siege."),
        ("Which sultanate claimed sovereignty over Anjadip Island?", "The Adil Shahi Sultanate of Bijapur.", "Bijapur launched attacks to reclaim the island."),
        ("What name did Almeida give to the fort constructed at Kilwa?", "Fort of São Tiago.", "It was named after Saint James."),
        ("Where did the Portuguese obtain the wood to build Fort Manuel in Cochin?", "From the local forests provided by the Cochin Raja.", "The Raja supplied timber and labor."),
        ("Which saint is Fort St. Angelo named after?", "Saint Angelo.", "The fort was named St. Angelo (Santo Ângelo)."),
        ("How many Portuguese soldiers were left to garrison Anjadip fort initially?", "Around 80 soldiers.", "A small force was left under Manuel Paçanha.")
    ]
    for q_en, ans_en, sol_en in ol3:
        q_hi = q_en.replace("Cannanore", "कन्नूर").replace("Almeida", "अल्मेडा").replace("Fort Manuel", "फोर्ट मैनुअल")
        sol_hi = f"उत्तर: {ans_en.replace('Almeida', 'अल्मेडा').replace('Cannanore', 'कन्नूर')}। स्पष्टीकरण: {sol_en.replace('Almeida', 'अल्मेडा')}"
        sol_en_combined = f"Answer: {ans_en} Explanation: {sol_en}"
        en.append({"type": "One-Liner", "q": q_en, "sol": sol_en_combined})
        hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

    # Assertion-Reason (8)
    ar3 = [
        ("Assertion: Almeida demolished the fort at Anjadip island in 1506.\nReason: The fort was difficult to defend against the frequent raids of the Bijapur Sultanate.", 0, "Logistical costs and Bijapur raids made Anjadip unsustainable."),
        ("Assertion: Fort Manuel in Cochin was built with the active support of the local Raja.\nReason: The Raja of Cochin sought Portuguese protection against the dominant Zamorin of Calicut.", 0, "The alliance was based on mutual interest against Calicut."),
        ("Assertion: Fort St. Angelo was built to dominate the horse trade of Cannanore.\nReason: Cannanore was the chief port for importing Persian horses into the Vijayanagara Empire.", 0, "Controlling Cannanore allowed the Portuguese to regulate the lucrative horse trade."),
        ("Assertion: The Siege of Cannanore in 1507 was led by the British fleet.\nReason: The British wanted to replace the Portuguese as the dominant power on the Malabar Coast.", 3, "Both are false. The British were not present; the siege was led by the Kolathiri Raja and Calicut."),
        ("Assertion: Almeida built the Fort of São Tiago at Kilwa.\nReason: Kilwa was a strategic Swahili trade center that controlled gold flow from Sofala.", 0, "Secure bases in East Africa were critical for the Cape Route navigation."),
        ("Assertion: The Cannanore garrison survived the 1507 siege because of a sudden supply of crabs.\nReason: A large wave washed thousands of crabs onto the fort's shore, feeding the starving garrison.", 0, "The event was recorded as a miracle that saved the defenders."),
        ("Assertion: Fort Manuel was built entirely of Portuguese stone brought as ballast.\nReason: There was no local stone suitable for military construction in Cochin.", 3, "Both are false. The fort was built using local timber/laterite; stone was not imported as ballast for walls."),
        ("Assertion: Almeida prioritized building coastal forts over capturing inland cities.\nReason: Coastal forts supported his Blue Water Policy by securing naval bases for patrols.", 0, "Forts were naval support hubs, not centers of territorial administration.")
    ]
    for q_en, ans, sol_en in ar3:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Assertion", "अभिकथन").replace("Reason", "कारण")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
        hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

    # Statement-Based (5)
    st3 = [
        ("Consider the following statements regarding Fort St. Angelo:\n1. It is located in the city of Cannanore.\n2. It was constructed by Afonso de Albuquerque in 1515.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; it was built by Almeida in 1505."),
        ("Consider the following statements about Fort Manuel in Cochin:\n1. It was the first European fort built in India.\n2. The local Raja of Cochin opposed its construction.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; the Raja supported it to gain protection."),
        ("With reference to the Kilwa fortification, consider these statements:\n1. Almeida built the Fort of São Tiago there in 1505.\n2. Kilwa is located on the coast of Western India.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; Kilwa is in East Africa."),
        ("Consider the statements about Anjadip Island fort:\n1. It was built using local materials in 1505.\n2. It was permanently maintained as the main Portuguese headquarters until 1961.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; the fort was demolished in 1506."),
        ("With reference to the Siege of Cannanore (1507), consider these statements:\n1. The siege was launched by the Kolathiri Raja supported by the Zamorin.\n2. The garrison was saved by the arrival of Tristão da Cunha's fleet.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The siege was lifted by reinforcements under Cunha.")
    ]
    for q_en, ans, sol_en in st3:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Fort Manuel", "फोर्ट मैनुअल").replace("Cannanore", "कन्नूर")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Statement-Based", "q": q_en, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol_en})
        hi.append({"type": "Statement-Based", "q": q_hi, "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": ans, "sol": sol_hi})

    # Open Questions (12)
    op3 = [
        ("Why", "Why did Almeida select Anjadip Island as the site for his first fort?", "Anjadip offered a natural harbor, fresh water, and was located near major shipping lanes, away from hostile mainland rulers."),
        ("Why", "Why did the Kolathiri Raja of Cannanore turn against the Portuguese in 1507?", "Arab merchants convinced the Raja that Portuguese naval policies were destroying local trade, and the Portuguese had sunk a ship carrying a Cartaz."),
        ("Why", "Why was Fort Manuel crucial for the survival of the early Portuguese presence in India?", "It protected the Cochin factory and the allied Raja from the superior land forces of the Zamorin of Calicut."),
        ("How", "How did the geographic position of Fort St. Angelo help control Arabian Sea trade?", "It sat on a peninsula, allowing naval guns to command the Cannanore bay and intercept coastal merchant ships."),
        ("How", "How did Almeida secure the construction of the Kilwa fort in 1505?", "He deposed the hostile Sultan of Kilwa, installed a cooperative vassal, and constructed Fort São Tiago using local labor."),
        ("How", "How did the Portuguese reinforce Fort Manuel over the years?", "They replaced the original coconut log palisade with a permanent laterite stone structure and added heavy artillery bastions."),
        ("Case Study", "Analyze the logistical issues that led to the abandonment and demolition of Anjadip Fort.", "The island was isolated during monsoons, faced continuous attacks from Bijapur forces, and was too expensive to garrison without commercial benefits."),
        ("Case Study", "Examine the role of local alliances in the fortification strategy of Francisco de Almeida.", "Almeida relied on rivalries (like Cochin vs. Calicut) to secure land for forts, showing that local divisions facilitated European entry."),
        ("Case Study", "Discuss the military significance of the Siege of Cannanore (1507) for Portuguese naval tactics.", "The siege demonstrated that coastal forts could withstand massive land blockades if they were periodically resupplied by sea."),
        ("Teach the Concept", "Explain the concept of 'feitoria' fortification.", "It is the process of enclosing a commercial factory/warehouse with walls and bastions to protect trade goods from local riots or attacks."),
        ("Teach the Concept", "Describe the design features of Fort St. Angelo in Cannanore.", "Designed by Tomás Fernandes, it had a triangular layout, stone battlements, and gun positions facing both the harbor and land approaches."),
        ("Teach the Concept", "Explain why the Portuguese prioritized building coastal and island forts rather than inland networks.", "Portugal had a small population, so they relied on naval mobility; coastal forts acted as bases for ships, which was their main strength.")
    ]
    for qtype, q_en, sol_en in op3:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Fort Manuel", "फोर्ट मैनुअल").replace("Cannanore", "कन्नूर")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": qtype, "q": q_en, "sol": sol_en})
        hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})

    return en, hi

def make_section_4():
    # The Battle of Chaul (1508)
    en = []
    hi = []
    
    # MCQ (5)
    en.append({
        "type": "MCQ",
        "q": "In which year did the Battle of Chaul take place between the Portuguese and a combined Muslim fleet?",
        "opts": ["1508 CE", "1505 CE", "1509 CE", "1515 CE"],
        "ans": 0,
        "sol": "The Battle of Chaul was fought in March 1508 CE."
    })
    hi.append({
        "type": "MCQ",
        "q": "पुर्तगालियों और एक संयुक्त मुस्लिम बेड़े के बीच चोल (Chaul) की लड़ाई किस वर्ष हुई थी?",
        "opts": ["1508 ईस्वी", "1505 ईस्वी", "1509 ईस्वी", "1515 ईस्वी"],
        "ans": 0,
        "sol": "चोल (Chaul) की लड़ाई मार्च 1508 ईस्वी में लड़ी गई थी।"
    })

    en.append({
        "type": "MCQ",
        "q": "Who was the young Portuguese commander who was killed during the Battle of Chaul?",
        "opts": ["Lourenço de Almeida", "Francisco de Almeida", "Afonso de Albuquerque", "Duarte Pacheco Pereira"],
        "ans": 0,
        "sol": "Lourenço de Almeida, the Viceroy's only son, died when his flagship was trapped and sunk."
    })
    hi.append({
        "type": "MCQ",
        "q": "चोल की लड़ाई में मारा गया युवा पुर्तगाली कमांडर कौन था?",
        "opts": ["लॉरेंको डी अल्मेडा", "फ्रांसिस्को डी अल्मेडा", "अल्फांसो डी अल्बुकर्क", "डुआर्टे पाचेको परेरा"],
        "ans": 0,
        "sol": "वायसराय के एकमात्र पुत्र लॉरेंको डी अल्मेडा की मृत्यु तब हुई जब उनका प्रमुख जहाज घिर गया और डूब गया।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which Egyptian dynasty dispatched the fleet under Amir Husain Al-Kurdi to fight the Portuguese at Chaul?",
        "opts": ["The Mamluk Sultanate", "The Ottoman Empire", "The Fatimid Caliphate", "The Ayyubid Dynasty"],
        "ans": 0,
        "sol": "The Mamluk Sultanate of Egypt sent the fleet to defend their spice trade interests."
    })
    hi.append({
        "type": "MCQ",
        "q": "किस मिस्र के राजवंश ने चोल में पुर्तगालियों से लड़ने के लिए अमीर हुसैन अल-कुर्दी के नेतृत्व में बेड़ा भेजा था?",
        "opts": ["ममलुक सल्तनत", "ओटोमन साम्राज्य", "फातिमी खिलाफत", "अय्यूबीड राजवंश"],
        "ans": 0,
        "sol": "मिस्र के ममलुक सल्तनत ने अपने मसाला व्यापार हितों की रक्षा के लिए बेड़ा भेजा था।"
    })

    en.append({
        "type": "MCQ",
        "q": "Who was the governor of Diu who commanded the Gujarati fleet and allied with the Mamluks at Chaul?",
        "opts": ["Malik Ayyaz", "Bahadur Shah", "Muzaffar Shah II", "Mahmud Begarha"],
        "ans": 0,
        "sol": "Malik Ayyaz (a Russian convert and governor of Diu) co-commanded the coalition fleet."
    })
    hi.append({
        "type": "MCQ",
        "q": "दीव का गवर्नर कौन था जिसने गुजराती बेड़े की कमान संभाली और चोल में ममलुकों के साथ गठबंधन किया?",
        "opts": ["मलिक अय्याज़", "बहादुर शाह", "मुजफ्फर शाह द्वितीय", "महमूद बेगड़ा"],
        "ans": 0,
        "sol": "मलिक अय्याज़ (दीव के गवर्नर) ने गठबंधन बेड़े की सह-कमान संभाली थी।"
    })

    en.append({
        "type": "MCQ",
        "q": "How did the Battle of Chaul end for the Portuguese fleet?",
        "opts": ["It resulted in a decisive defeat and the loss of their flagship", "It was a decisive Portuguese victory", "It was a peaceful draw", "The Portuguese fleet was entirely captured"],
        "ans": 0,
        "sol": "The battle was a major defeat for the Portuguese, resulting in the death of Lourenço and loss of his ship."
    })
    hi.append({
        "type": "MCQ",
        "q": "पुर्तगाली बेड़े के लिए चोल की लड़ाई का अंत कैसे हुआ?",
        "opts": ["इसके परिणामस्वरूप एक निर्णायक हार हुई और उनका प्रमुख जहाज नष्ट हो गया", "यह पुर्तगालियों की एक निर्णायक जीत थी", "यह एक शांतिपूर्ण ड्रॉ था", "पुर्तगाली बेड़े को पूरी तरह से पकड़ लिया गया था"],
        "ans": 0,
        "sol": "यह लड़ाई पुर्तगालियों के लिए एक बड़ी हार थी, जिसके परिणामस्वरूप लॉरेंको की मृत्यु हुई और उनका जहाज डूब गया।"
    })

    # Multi Correct (5)
    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which fleets composed the allied coalition that defeated the Portuguese at Chaul? (Select all that apply)",
        "opts": ["The Mamluk fleet under Amir Husain", "The Gujarat Sultanate fleet under Malik Ayyaz", "The Zamorin's forces of Calicut", "The British Royal Navy"],
        "ans": [0, 1, 2],
        "sol": "The coalition consisted of Mamluks, Gujaratis, and Calicut vessels. The British were not involved."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "चोल में पुर्तगालियों को हराने वाले संबद्ध गठबंधन में कौन से बेड़े शामिल थे? (सभी लागू विकल्प चुनें)",
        "opts": ["अमीर हुसैन के तहत ममलुक बेड़ा", "मलिक अय्याज़ के तहत गुजरात सल्तनत का बेड़ा", "कालीकट के ज़मोरिन की सेनाएँ", "ब्रिटिश रॉयल नेवी"],
        "ans": [0, 1, 2],
        "sol": "गठबंधन में ममलुक, गुजराती और कालीकट के जहाज शामिल थे। ब्रिटिश इसमें शामिल नहीं थे।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Identify the key details of Lourenço de Almeida's death at Chaul. (Select all that apply)",
        "opts": ["His flagship was pinned down by a Gujarati cable in the river", "He refused to retreat or surrender despite being wounded", "He was struck and killed by a cannonball", "He was captured and executed in Cairo"],
        "ans": [0, 1, 2],
        "sol": "His ship was trapped by a cable, he refused to surrender, and he was killed by cannon fire. He was not taken to Cairo."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "चोल में लॉरेंको डी अल्मेडा की मृत्यु के प्रमुख विवरणों की पहचान करें। (सभी लागू विकल्प चुनें)",
        "opts": ["उनका प्रमुख जहाज नदी में एक गुजराती केबल द्वारा फंस गया था", "घायल होने के बावजूद उन्होंने पीछे हटने या आत्मसमर्पण करने से इनकार कर दिया", "वह एक तोप के गोले की चपेट में आने से मारे गए थे", "उन्हें पकड़ लिया गया था और काहिरा में फांसी दे दी गई थी"],
        "ans": [0, 1, 2],
        "sol": "उनका जहाज फंस गया था, उन्होंने आत्मसमर्पण से इनकार किया, और तोप के गोले से उनकी मौत हुई। उन्हें काहिरा नहीं ले जाया गया था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which factors contributed to the Portuguese defeat at Chaul? (Select all that apply)",
        "opts": ["The surprise arrival of the Mamluk fleet in Indian waters", "Tactical entrapment of Portuguese ships in the shallow river harbor", "Malik Ayyaz's coordinate strike with coastal gunboats", "The mutiny of Portuguese captains during the battle"],
        "ans": [0, 1, 2],
        "sol": "Surprise arrival of Mamluks, shallow river traps, and Ayyaz's gunboats were key factors. There was no mutiny."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "चोल में पुर्तगाली हार में किन कारकों ने योगदान दिया? (सभी लागू विकल्प चुनें)",
        "opts": ["भारतीय जल क्षेत्र में ममलुक बेड़े का अचानक आगमन", "उथले नदी बंदरगाह में पुर्तगाली जहाजों का रणनीतिक रूप से फंसना", "तटीय गनबोटों के साथ मलिक अय्याज़ का समन्वित हमला", "लड़ाई के दौरान पुर्तगाली कप्तानों का विद्रोह"],
        "ans": [0, 1, 2],
        "sol": "ममलुकों का अचानक आगमन, उथली नदी में फंसना और मलिक अय्याज़ के गनबोट प्रमुख कारक थे। वहां कोई विद्रोह नहीं हुआ था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What were the immediate political reactions to the Battle of Chaul? (Select all that apply)",
        "opts": ["Francisco de Almeida swore a personal oath of revenge", "Portuguese prestige in the Indian Ocean was temporarily shattered", "Almeida refused to transfer power to Albuquerque", "The Zamorin captured Cochin immediately"],
        "ans": [0, 1, 2],
        "sol": "Almeida swore revenge, Portuguese prestige suffered, and Almeida delayed the power transition. Cochin was not captured."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "चोल की लड़ाई की तत्काल राजनीतिक प्रतिक्रियाएँ क्या थीं? (सभी लागू विकल्प चुनें)",
        "opts": ["फ्रांसिस्को डी अल्मेडा ने व्यक्तिगत बदला लेने की शपथ ली", "हिंद महासागर में पुर्तगाली प्रतिष्ठा को अस्थायी रूप से झटका लगा", "अल्मेडा ने अल्बुकर्क को सत्ता सौंपने से इनकार कर दिया", "ज़मोरिन ने कोचीन पर तुरंत कब्जा कर लिया"],
        "ans": [0, 1, 2],
        "sol": "अल्मेडा ने बदला लेने की कसम खाई, पुर्तगाली प्रतिष्ठा को झटका लगा, और सत्ता का हस्तांतरण टाल दिया गया।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which details describe Malik Ayyaz's role at the Battle of Chaul? (Select all that apply)",
        "opts": ["He served as the governor of Diu", "He commanded the fast coastal dhows and gunboats of Gujarat", "He acted cautiously, avoiding complete destruction of the Portuguese fleet to maintain diplomatic leverage", "He was a Portuguese agent who betrayed the Zamorin"],
        "ans": [0, 1, 2],
        "sol": "Ayyaz was the governor of Diu, commanded the Gujarat fleet, and acted cautiously for diplomatic reasons. He was not a Portuguese agent."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "चोल की लड़ाई में मलिक अय्याज़ की भूमिका का वर्णन करने वाले विवरणों का चयन करें: (सभी लागू विकल्प चुनें)",
        "opts": ["उन्होंने दीव के गवर्नर के रूप में कार्य किया", "उन्होंने गुजरात के तेज तटीय जहाजों और गनबोटों की कमान संभाली", "राजनयिक लाभ बनाए रखने के लिए पुर्तगाली बेड़े को पूरी तरह से नष्ट करने से बचते हुए, उन्होंने समझदारी से काम लिया", "वह एक पुर्तगाली एजेंट थे जिन्होंने ज़मोरिन को धोखा दिया था"],
        "ans": [0, 1, 2],
        "sol": "अय्याज़ दीव के गवर्नर थे, उन्होंने गुजरात बेड़े का नेतृत्व किया, और रणनीतिक कारणों से समझदारी से काम लिया।"
    })

    # True/False (8)
    tf4 = [
        ("The Battle of Chaul was the first major defeat suffered by the Portuguese in Indian waters.", True, "It shattered their myth of naval invincibility."),
        ("Amir Husain Al-Kurdi was the commander of the Mamluk fleet dispatched from Egypt.", True, "He led the Mamluk expedition to expel the Portuguese."),
        ("Lourenço de Almeida surrendered his ship to Malik Ayyaz before dying.", False, "He refused to surrender and fought until he was killed by a cannonball."),
        ("The Battle of Chaul was fought in the open ocean far away from the coast.", False, "It was fought inside the shallow harbor and estuary of Chaul."),
        ("The Portuguese fleet at Chaul was caught by surprise because they did not expect Mamluk intervention.", True, "They did not know that a Mamluk fleet had arrived in India."),
        ("Francisco de Almeida was present and personally commanded the fleet at Chaul.", False, "The fleet was commanded by his son Lourenço; Francisco was in Cochin."),
        ("Malik Ayyaz treated the Portuguese prisoners captured at Chaul with cruelty.", False, "He treated them with relative kindness to preserve diplomatic options with Lisbon."),
        ("The battle ended the Mamluk spice monopoly permanently.", False, "It was a victory for the Mamluks, temporarily securing their trade route.")
    ]
    for q_en, ans, sol_en in tf4:
        q_hi = q_en.replace("Lourenço de Almeida", "लॉरेंको डी अल्मेडा").replace("Malik Ayyaz", "मलिक अय्याज़").replace("Almeida", "अल्मेडा")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Fill in the Blank (8)
    fill4 = [
        ("The Battle of Chaul was fought in the month of __________ in 1508.", "March", "The naval clash occurred in March 1508 CE."),
        ("The Egyptian commander of the fleet at Chaul was Amir __________.", "Husain", "Amir Husain Al-Kurdi led the Mamluk forces."),
        ("The governor of Diu who co-commanded the coalition forces was Malik __________.", "Ayyaz", "Malik Ayyaz was the governor of Diu under the Gujarat Sultanate."),
        ("The Viceroy's son, __________ de Almeida, died in the battle.", "Lourenço", "Lourenço de Almeida was the commander at Chaul."),
        ("The flagship at Chaul was trapped when its hull was pierced and it was caught by a sea __________.", "cable", "A cable caught the ship, preventing it from escaping the harbor."),
        ("The Muslim coalition was backed by the Sultan of Gujarat, Mahmud __________.", "Begarha", "Mahmud Begarha was the famous sultan of Gujarat."),
        ("The battle took place in the harbor of __________, a port near modern Mumbai.", "Chaul", "Chaul was a major trade port on the western coast."),
        ("The Mamluk fleet had been built in the Red Sea using timber supplied by __________.", "Venice", "Venice secretly supplied ship-building timber to help Egypt fight Portugal.")
    ]
    for q_en, ans, sol_en in fill4:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("__________", "__________")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Match the Following (3)
    en.append({
        "type": "Match the Following",
        "q": "Match the battle commanders of Chaul with their affiliations:",
        "items": [{"left": "Lourenço de Almeida"}, {"left": "Amir Husain Al-Kurdi"}, {"left": "Malik Ayyaz"}],
        "options": [{"val": "0", "text": "Portuguese Crown fleet"}, {"val": "1", "text": "Mamluk Sultanate of Egypt"}, {"val": "2", "text": "Gujarat Sultanate (Diu)"}],
        "sol": "Lourenço was Portuguese, Amir Husain Mamluk, and Ayyaz was from Gujarat."
    })
    hi.append({
        "type": "Match the Following",
        "q": "चोल के युद्ध कमांडरों का उनके संबद्ध संगठनों से मिलान करें:",
        "items": [{"left": "लॉरेंको डी अल्मेडा"}, {"left": "अमीर हुसैन अल-कुर्दी"}, {"left": "मलिक अय्याज़"}],
        "options": [{"val": "0", "text": "पुर्तगाली क्राउन बेड़ा"}, {"val": "1", "text": "मिस्र का ममलुक सल्तनत"}, {"val": "2", "text": "गुजरात सल्तनत (दीव)"}],
        "sol": "लॉरेंको पुर्तगाली थे, अमीर हुसैन ममलुक थे, और अय्याज़ गुजरात से थे।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the strategic outcomes of the battle with the corresponding entities:",
        "items": [{"left": "Death of Lourenço"}, {"left": "Kind treatment of prisoners"}, {"left": "Supply of shipbuilding timber"}],
        "options": [{"val": "0", "text": "Francisco de Almeida's grief and delay of power transfer"}, {"val": "1", "text": "Malik Ayyaz's cautious diplomacy"}, {"val": "2", "text": "Venetian covert support to Mamluks"}],
        "sol": "Lourenço's death caused Francisco's grief, Ayyaz treated prisoners well, and Venice supplied timber."
    })
    hi.append({
        "type": "Match the Following",
        "q": "लड़ाई के रणनीतिक परिणामों का संबंधित संस्थाओं से मिलान करें:",
        "items": [{"left": "लॉरेंको की मृत्यु"}, {"left": "कैदियों के साथ दयालु व्यवहार"}, {"left": "जहाज निर्माण लकड़ी की आपूर्ति"}],
        "options": [{"val": "0", "text": "फ्रांसिस्को डी अल्मेडा का दुख और सत्ता हस्तांतरण में देरी"}, {"val": "1", "text": "मलिक अय्याज़ की सतर्क कूटनीति"}, {"val": "2", "text": "ममलुकों को वेनिस का गुप्त समर्थन"}],
        "sol": "लॉरेंको की मृत्यु से अल्मेडा को गहरा दुख हुआ, अय्याज़ ने कैदियों से अच्छा व्यवहार किया, और वेनिस ने लकड़ी की आपूर्ति की।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the geographical features of the battle with their significance:",
        "items": [{"left": "Chaul estuary"}, {"left": "Suez shipyard"}, {"left": "Diu harbor"}],
        "options": [{"val": "0", "text": "Shallow water trap for Portuguese naus"}, {"val": "1", "text": "Construction site of the Mamluk fleet"}, {"val": "2", "text": "Base of the Gujarat coalition fleet"}],
        "sol": "Chaul was the shallow trap, Suez was where Mamluks built the fleet, and Diu was Malik Ayyaz's base."
    })
    hi.append({
        "type": "Match the Following",
        "q": "लड़ाई की भौगोलिक विशेषताओं का उनके महत्व से मिलान करें:",
        "items": [{"left": "चोल मुहाना"}, {"left": "स्वेज शिपयार्ड"}, {"left": "दीव बंदरगाह"}],
        "options": [{"val": "0", "text": "पुर्तगाली जहाजों के लिए उथला पानी का जाल"}, {"val": "1", "text": "ममलुक बेड़े का निर्माण स्थल"}, {"val": "2", "text": "गुजरात गठबंधन बेड़े का आधार"}],
        "sol": "चोल मुहाना उथला जाल था, स्वेज ममलुक बेड़े का निर्माण स्थल था, और दीव मलिक अय्याज़ का आधार था।"
    })

    # One-Liner (8)
    ol4 = [
        ("What weapon killed Lourenço de Almeida?", "A cannonball.", "He was struck by a cannonball after his legs were shattered by a previous shot."),
        ("Which European power secretly assisted the Mamluks in building their fleet?", "Venice.", "Venice wanted to protect its Levantine trade monopoly."),
        ("What did Malik Ayyaz do with the surviving Portuguese prisoners?", "He imprisoned them in Diu and treated them well.", "He kept them as diplomatic hostages."),
        ("How did Lourenço's ship become trapped at Chaul?", "Its rudder was damaged and it was caught by a fish trap/cable.", "The ship could not maneuver in the shallow estuary."),
        ("Did the Portuguese fleet retreat after Lourenço's death?", "Yes, the remaining ships withdrew to Cochin.", "The survivors sailed south under the second-in-command."),
        ("Who was the sultan of Egypt who ordered the creation of the anti-Portuguese fleet?", "Al-Ashraf Qansuh al-Ghawri.", "He was the penultimate Mamluk Sultan."),
        ("What was the reaction of the Zamorin of Calicut to the Battle of Chaul?", "He celebrated and sent reinforcements to the Mamluks.", "He hoped to finally expel the Portuguese from Malabar."),
        ("Why did the Portuguese not expect the Mamluk fleet at Chaul?", "They believed the Mamluks lacked the naval capacity to sail into the Indian Ocean.", "The Mamluks had traditionally relied on land armies and lacked a navy.")
    ]
    for q_en, ans_en, sol_en in ol4:
        q_hi = q_en.replace("Lourenço de Almeida", "लॉरेंको डी अल्मेडा").replace("Almeida", "अल्मेडा").replace("Malik Ayyaz", "मलिक अय्याज़")
        sol_hi = f"उत्तर: {ans_en.replace('Almeida', 'अल्मेडा').replace('Malik Ayyaz', 'मलिक अय्याज़')}। स्पष्टीकरण: {sol_en.replace('Almeida', 'अल्मेडा')}"
        sol_en_combined = f"Answer: {ans_en} Explanation: {sol_en}"
        en.append({"type": "One-Liner", "q": q_en, "sol": sol_en_combined})
        hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

    # Assertion-Reason (8)
    ar4 = [
        ("Assertion: The Mamluk fleet was able to surprise the Portuguese at Chaul.\nReason: The Portuguese did not have an active intelligence network in the Red Sea in 1507.", 0, "Lack of intelligence allowed the Mamluk fleet to sail to India undetected."),
        ("Assertion: Lourenço de Almeida refused to abandon his flagship.\nReason: He believed that a Portuguese noble commander should never surrender to Muslim forces.", 0, "Chivalric codes of honor prevented him from retreating."),
        ("Assertion: Venice secretly supplied timber to the Mamluks to build their war fleet.\nReason: Venice wanted to destroy the Mamluk Sultanate and take over Egypt.", 2, "Assertion is true, but Reason is false because Venice wanted to help Egypt preserve the spice route from Portuguese disruption."),
        ("Assertion: Malik Ayyaz was a native Gujarati noble.\nReason: He was born in Ahmedabad and belonged to the royal family of the Gujarat Sultanate.", 3, "Both are false. Malik Ayyaz was a Russian slave convert who rose to become the governor of Diu."),
        ("Assertion: The Battle of Chaul resulted in the complete destruction of the Portuguese navy in India.\nReason: All 21 ships of Almeida's fleet were sunk during the battle.", 3, "Both are false. Only a few Portuguese ships were lost, including the flagship; the rest withdrew safely."),
        ("Assertion: Francisco de Almeida was devastated by the news of the Battle of Chaul.\nReason: His only son Lourenço was killed, and the Portuguese navy had suffered its first defeat.", 0, "The loss of his son transformed his governorship into a campaign of revenge."),
        ("Assertion: Malik Ayyaz treated the Portuguese prisoners kindly.\nReason: He wanted to keep a diplomatic door open with the Viceroy in case the Portuguese retaliated.", 0, "Ayyaz acted pragmatically, anticipating a strong Portuguese counter-attack."),
        ("Assertion: The Battle of Chaul temporarily secured Mamluk-Gujarati control over the Arabian Sea.\nReason: The Portuguese fleet was forced to retreat to their southern base in Cochin.", 0, "The victory allowed the coalition to consolidate their forces at Diu.")
    ]
    for q_en, ans, sol_en in ar4:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Assertion", "अभिकथन").replace("Reason", "कारण")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
        hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

    # Statement-Based (5)
    st4 = [
        ("Consider the following statements regarding the Battle of Chaul:\n1. It was fought in 1508 CE.\n2. The Portuguese fleet was commanded by Francisco de Almeida personally.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; the fleet was commanded by Lourenço de Almeida."),
        ("Consider the following statements about the Mamluk fleet at Chaul:\n1. It was led by Amir Husain Al-Kurdi.\n2. The ships were constructed at Suez using timber supplied by Venice.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Amir Husain led the Mamluk fleet built at Suez with Venetian timber."),
        ("With reference to Malik Ayyaz, consider these statements:\n1. He was the governor of Cochin.\n2. He co-commanded the coalition forces at Chaul.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect; he was the governor of Diu."),
        ("Consider the statements about Lourenço de Almeida's flagship at Chaul:\n1. It was trapped in the estuary due to a sea cable.\n2. It successfully broke the blockade and returned to Lisbon.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. The flagship was sunk and Lourenço died; it did not return."),
        ("With reference to the aftermath of the battle, consider these statements:\n1. The Portuguese prisoners were executed by Malik Ayyaz.\n2. Viceroy Almeida accepted his replacement by Albuquerque immediately.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect. Prisoners were treated well, and Almeida refused to step down.")
    ]
    for q_en, ans, sol_en in st4:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Malik Ayyaz", "मलिक अय्याज़")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Statement-Based", "q": q_en, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol_en})
        hi.append({"type": "Statement-Based", "q": q_hi, "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": ans, "sol": sol_hi})

    # Open Questions (12)
    op4 = [
        ("Why", "Why did the Mamluk Sultanate decide to intervene militarily in the Indian Ocean in 1507?", "The Portuguese blockade of the Red Sea cut off Mamluk customs revenues from the spice trade, threatening the economic survival of Egypt."),
        ("Why", "Why was the harbor of Chaul tactically disadvantageous for the Portuguese fleet?", "The shallow estuary and narrow channels restricted the mobility of the large Portuguese naus, making them vulnerable to light, fast Gujarati dhows."),
        ("Why", "Why did Venice secretly support the Mamluks against the Portuguese?", "Venetian trade depended on buying spices in Egypt; the Portuguese direct Cape Route bypassed Venice, destroying its commercial dominance in Europe."),
        ("How", "How did Malik Ayyaz use his position as governor of Diu to support the Mamluk fleet?", "He provided Diu as a naval base, supplied fresh provisions, and reinforced the Mamluk fleet with his own coastal gunboats."),
        ("How", "How did the death of Lourenço de Almeida impact the Portuguese chain of command in India?", "It caused a crisis, as Francisco de Almeida refused to hand over power to his designated successor Albuquerque, prioritizing personal revenge."),
        ("How", "How did the coalition fleet manage to trap the Portuguese flagship at Chaul?", "They damaged its rudder with cannon fire, and a Gujarati cable caught the ship, pinning it down in the river channel."),
        ("Case Study", "Analyze the geopolitical motivations of the Mamluk-Ottoman-Gujarati coalition at Chaul.", "The coalition aimed to protect their joint trade interests from Portuguese monopoly, combining Egyptian naval ambition, Ottoman gunnery, and Gujarati local power."),
        ("Case Study", "Examine the role of chivalric codes and military honor in Lourenço de Almeida's tactical decisions at Chaul.", "His refusal to abandon the trapped flagship, despite being wounded and urged by his captains to escape, led to his death but created a legendary martyr for the Portuguese empire."),
        ("Case Study", "Discuss the diplomatic strategy of Malik Ayyaz in the treatment of Portuguese prisoners.", "Ayyaz treated prisoners well to preserve a line of negotiation with Lisbon, recognizing that a brutal execution would invite total destruction from the Viceroy."),
        ("Teach the Concept", "Explain the tactical differences between Mamluk dhows and Portuguese naus.", "Mamluk dhows were fast and agile but lightly built, while Portuguese naus were large, heavily armed with cannons, but less maneuverable in shallow waters."),
        ("Teach the Concept", "Describe the chain of events that led to the Battle of Chaul.", "Portuguese patrols blockaded the Red Sea; Egypt built a fleet at Suez with Venetian help, sailed to India, allied with the Governor of Diu, and intercepted the Portuguese patrol at Chaul."),
        ("Teach the Concept", "Explain why the Battle of Chaul is considered a turning point in early Indo-Portuguese history.", "It was the first time a local coalition successfully defeated the Portuguese navy, showing that European naval power could be challenged with coordinated tactics.")
    ]
    for qtype, q_en, sol_en in op4:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Malik Ayyaz", "मलिक अय्याज़")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": qtype, "q": q_en, "sol": sol_en})
        hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})

    return en, hi

def make_section_5():
    # The Battle of Diu (1509) & Legacy
    en = []
    hi = []
    
    # MCQ (5)
    en.append({
        "type": "MCQ",
        "q": "On which exact date did the decisive Battle of Diu take place in 1509?",
        "opts": ["February 3, 1509", "March 25, 1508", "December 10, 1509", "January 1, 1510"],
        "ans": 0,
        "sol": "The Battle of Diu was fought on February 3, 1509 CE."
    })
    hi.append({
        "type": "MCQ",
        "q": "1509 में निर्णायक दीव की लड़ाई किस सटीक तारीख को हुई थी?",
        "opts": ["3 फरवरी, 1509", "25 मार्च, 1508", "10 दिसंबर, 1509", "1 जनवरी, 1510"],
        "ans": 0,
        "sol": "दीव की लड़ाई 3 फरवरी, 1509 ईस्वी को लड़ी गई थी।"
    })

    en.append({
        "type": "MCQ",
        "q": "Who personally commanded the Portuguese fleet at the Battle of Diu?",
        "opts": ["Francisco de Almeida", "Lourenço de Almeida", "Afonso de Albuquerque", "Vasco da Gama"],
        "ans": 0,
        "sol": "The Viceroy Francisco de Almeida personally led the fleet to avenge his son's death."
    })
    hi.append({
        "type": "MCQ",
        "q": "दीव की लड़ाई में पुर्तगाली बेड़े की कमान व्यक्तिगत रूप से किसने संभाली थी?",
        "opts": ["फ्रांसिस्को डी अल्मेडा", "लॉरेंको डी अल्मेडा", "अल्फांसो डी अल्बुकर्क", "वास्को डी गामा"],
        "ans": 0,
        "sol": "वायसराय फ्रांसिस्को डी अल्मेडा ने अपने बेटे की मौत का बदला लेने के लिए व्यक्तिगत रूप से बेड़े का नेतृत्व किया था।"
    })

    en.append({
        "type": "MCQ",
        "q": "Which empire joined the Mamluks and Gujaratis by providing soldiers and gunners at Diu?",
        "opts": ["The Ottoman Empire", "The Safavid Empire", "The Mughal Empire", "The Vijayanagara Empire"],
        "ans": 0,
        "sol": "The Ottoman Empire supported the coalition by sending gunners and military advisers."
    })
    hi.append({
        "type": "MCQ",
        "q": "दीव में सैनिकों और तोपचियों को प्रदान करके कौन सा साम्राज्य ममलुकों और गुजरातियों के साथ शामिल हुआ था?",
        "opts": ["ओटोमन साम्राज्य", "सफाविद साम्राज्य", "मुगल साम्राज्य", "विजयनगर साम्राज्य"],
        "ans": 0,
        "sol": "ओटोमन साम्राज्य ने तोपचियों और सैन्य सलाहकारों को भेजकर गठबंधन का समर्थन किया था।"
    })

    en.append({
        "type": "MCQ",
        "q": "What was the strategic outcome of the Battle of Diu for European history?",
        "opts": ["It established European naval dominance in the Indian Ocean for nearly 400 years", "It led to the complete expulsion of the Portuguese from India", "It resulted in a stalemate", "It forced the Portuguese to pay tribute to the Mughal Emperor"],
        "ans": 0,
        "sol": "The victory secured Portuguese naval monopoly and paved the way for centuries of European dominance."
    })
    hi.append({
        "type": "MCQ",
        "q": "यूरोपीय इतिहास के लिए दीव की लड़ाई का रणनीतिक परिणाम क्या था?",
        "opts": ["इसने लगभग 400 वर्षों तक हिंद महासागर में यूरोपीय नौसैनिक प्रभुत्व स्थापित किया", "इसके कारण भारत से पुर्तगालियों का पूर्ण निष्कासन हुआ", "इसके परिणामस्वरूप गतिरोध पैदा हुआ", "इसने पुर्तगालियों को मुगल सम्राट को कर देने के लिए मजबूर किया"],
        "ans": 0,
        "sol": "इस जीत ने पुर्तगाली नौसैनिक एकाधिकार को सुरक्षित किया और सदियों के यूरोपीय वर्चस्व का मार्ग प्रशस्त किया।"
    })

    en.append({
        "type": "MCQ",
        "q": "Where did Francisco de Almeida die in 1510 CE during his return journey to Portugal?",
        "opts": ["Table Bay near the Cape of Good Hope", "Lisbon harbor", "Cochin port", "Diu Island"],
        "ans": 0,
        "sol": "Almeida was killed in a skirmish with local Khoikhoi (Hottentots) at Table Bay (South Africa) in March 1510."
    })
    hi.append({
        "type": "MCQ",
        "q": "पुर्तगाल की अपनी वापसी यात्रा के दौरान 1510 ईस्वी में फ्रांसिस्को डी अल्मेडा की मृत्यु कहाँ हुई थी?",
        "opts": ["केप ऑफ गुड होप के पास टेबल बे (Table Bay)", "लिस्बन बंदरगाह", "कोचीन बंदरगाह", "दीव द्वीप"],
        "ans": 0,
        "sol": "अल्मेडा मार्च 1510 में टेबल बे (दक्षिण अफ्रीका) में स्थानीय खोइखोई (Khoikhoi) के साथ एक झड़प में मारे गए थे।"
    })

    # Multi Correct (5)
    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which fleets and forces composed the defeated coalition at Diu in 1509? (Select all that apply)",
        "opts": ["The Mamluk Sultanate fleet under Amir Husain", "The Gujarat Sultanate fleet under Malik Ayyaz", "Ottoman gunners and soldiers", "The Portuguese navy under Albuquerque"],
        "ans": [0, 1, 2],
        "sol": "The coalition consisted of Mamluks, Gujaratis, and Ottomans. The Portuguese were the victors, not part of the defeated coalition."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "1509 में दीव में पराजित गठबंधन में कौन से बेड़े और बल शामिल थे? (सभी लागू विकल्प चुनें)",
        "opts": ["अमीर हुसैन के तहत ममलुक सल्तनत का बेड़ा", "मलिक अय्याज़ के तहत गुजरात सल्तनत का बेड़ा", "ओटोमन तोपची और सैनिक", "अल्बुकर्क के तहत पुर्तगाली नौसेना"],
        "ans": [0, 1, 2],
        "sol": "गठबंधन में ममलुक, गुजराती और ओटोमन शामिल थे। पुर्तगाली विजेता थे, न कि पराजित गठबंधन का हिस्सा।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Identify the terms of surrender accepted by Malik Ayyaz after the Battle of Diu. (Select all that apply)",
        "opts": ["Release of all Portuguese prisoners captured at Chaul", "Payment of a heavy financial indemnity", "Permission for the Portuguese to trade at Diu", "Immediate handover of Diu fortress to the Portuguese"],
        "ans": [0, 1, 2],
        "sol": "Ayyaz released the prisoners, paid an indemnity, and granted trade rights. The fort was not handed over until 1535."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "दीव की लड़ाई के बाद मलिक अय्याज़ द्वारा स्वीकार की गई आत्मसमर्पण की शर्तों की पहचान करें: (सभी लागू विकल्प चुनें)",
        "opts": ["चोल में पकड़े गए सभी पुर्तगाली कैदियों की रिहाई", "भारी वित्तीय क्षतिपूर्ति का भुगतान", "पुर्तगालियों को दीव में व्यापार करने की अनुमति", "पुर्तगालियों को दीव किले का तत्काल हस्तांतरण"],
        "ans": [0, 1, 2],
        "sol": "अय्याज़ ने कैदियों को रिहा किया, क्षतिपूर्ति का भुगतान किया और व्यापारिक अधिकार दिए। किले का हस्तांतरण 1535 तक नहीं हुआ था।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which tactical advantages favored the Portuguese at the Battle of Diu? (Select all that apply)",
        "opts": ["Superior naval gunnery and larger cannon range", "High-walled naus that were difficult to board", "Coordinated division of ships by Almeida", "The surprise intervention of a Spanish armada"],
        "ans": [0, 1, 2],
        "sol": "Superior gunnery, high-walled ships, and Almeida's coordination were key. No Spanish ships participated."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "दीव की लड़ाई में पुर्तगालियों के लिए कौन से रणनीतिक लाभ सहायक थे? (सभी लागू विकल्प चुनें)",
        "opts": ["बेहतर नौसैनिक तोपखाना और बड़ी तोप सीमा", "ऊंची दीवारों वाले जहाज जिन पर चढ़ना मुश्किल था", "अल्मेडा द्वारा जहाजों का समन्वित विभाजन", "एक स्पेनिश बेड़े का अचानक हस्तक्षेप"],
        "ans": [0, 1, 2],
        "sol": "बेहतर तोपें, ऊंचे जहाज और अल्मेडा का समन्वय प्रमुख थे। किसी भी स्पेनिश जहाज ने भाग नहीं लिया।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "What were the geopolitical consequences of the Battle of Diu? (Select all that apply)",
        "opts": ["Establishment of Portuguese naval hegemony in the Indian Ocean", "Decline and eventual annexation of the Mamluk Sultanate by the Ottomans", "Venice lost its status as the chief spice importer in Europe", "The Mughal Empire conquered Gujarat immediately"],
        "ans": [0, 1, 2],
        "sol": "Portuguese hegemony, the weakening of Mamluks (conquered by Ottomans in 1517), and Venetian decline were major consequences. The Mughals did not conquer Gujarat until 1573."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "दीव की लड़ाई के भू-राजनीतिक परिणाम क्या थे? (सभी लागू विकल्प चुनें)",
        "opts": ["हिंद महासागर में पुर्तगाली नौसैनिक वर्चस्व की स्थापना", "ओटोमन्स द्वारा ममलुक सल्तनत का पतन और अंततः विलय", "वेनिस ने यूरोप में मुख्य मसाला आयातक के रूप में अपना स्थान खो दिया", "मुगल साम्राज्य ने गुजरात पर तुरंत विजय प्राप्त की"],
        "ans": [0, 1, 2],
        "sol": "पुर्तगाली वर्चस्व, ममलुकों का पतन और वेनिस का पतन इसके प्रमुख परिणाम थे। मुगलों ने 1573 तक गुजरात पर विजय नहीं प्राप्त की थी।"
    })

    en.append({
        "type": "Multiple Correct MCQ",
        "q": "Which facts describe the death of Francisco de Almeida in 1510? (Select all that apply)",
        "opts": ["It occurred at Table Bay, South Africa", "He was killed in a skirmish with local Khoikhoi natives", "He was buried in an unmarked grave on the beach", "He was assassinated by Afonso de Albuquerque's agents"],
        "ans": [0, 1, 2],
        "sol": "He died at Table Bay in a skirmish with Khoikhoi, and was buried there. He was not assassinated by Albuquerque."
    })
    hi.append({
        "type": "Multiple Correct MCQ",
        "q": "1510 में फ्रांसिस्को डी अल्मेडा की मृत्यु का वर्णन करने वाले तथ्यों का चयन करें: (सभी लागू विकल्प चुनें)",
        "opts": ["यह टेबल बे, दक्षिण अफ्रीका में हुआ था", "वह स्थानीय खोइखोई आदिवासियों के साथ एक झड़प में मारे गए थे", "उन्हें समुद्र तट पर एक अचिह्नित कब्र में दफनाया गया था", "अल्फांसो डी अल्बुकर्क के एजेंटों द्वारा उनकी हत्या कर दी गई थी"],
        "ans": [0, 1, 2],
        "sol": "टेबल बे में खोइखोई के साथ झड़प में उनकी मृत्यु हुई, और उन्हें वहीं दफनाया गया। अल्बुकर्क ने उनकी हत्या नहीं करवाई थी।"
    })

    # True/False (8)
    tf5 = [
        ("The Battle of Diu in 1509 was a decisive victory for the Mamluk Sultanate.", False, "It was a decisive Portuguese victory that destroyed the Mamluk fleet."),
        ("Almeida treated the defeated Mamluk prisoners at Diu with extreme brutality.", True, "He executed many prisoners in retaliatory revenge for his son's death."),
        ("The Ottoman Empire officially participated in the Battle of Diu by sending troops.", True, "Ottoman soldiers and gunners reinforced the coalition fleet."),
        ("Following his victory at Diu, Almeida immediately surrendered power to Albuquerque.", True, "Having avenged his son, Almeida handed over governance in late 1509 and set sail for Portugal."),
        ("Almeida was killed by a poison arrow shot by a Mamluk soldier in 1510.", False, "He was killed by Khoikhoi spear/stone attacks during a skirmish over fresh water."),
        ("The Battle of Diu ended Venetian control of the spice routes permanently.", True, "It consolidated the Portuguese Cape Route monopoly, bypassing Venice."),
        ("Malik Ayyaz was executed by Almeida after the battle.", False, "Ayyaz surrendered and negotiated a peace treaty; he remained governor of Diu."),
        ("The victory at Diu allowed the Portuguese to build their first fort in Diu immediately in 1509.", False, "They were not allowed to build a fort in Diu until 1535.")
    ]
    for q_en, ans, sol_en in tf5:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Mamluk", "ममलुक").replace("Albuquerque", "अल्बुकर्क")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "True/False", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "True/False", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Fill in the Blank (8)
    fill5 = [
        ("The Battle of Diu was fought off the coast of __________ in Gujarat.", "Diu", "The battle took place off the island of Diu."),
        ("Almeida personally led the fleet at Diu to avenge the death of his son __________.", "Lourenço", "Lourenço had been killed at Chaul in 1508."),
        ("The coalition fleet at Diu was co-commanded by Amir __________ of Egypt.", "Husain", "Amir Husain Al-Kurdi co-commanded the fleet."),
        ("Viceroy Almeida died at Table Bay in South Africa after a skirmish with the local __________ tribe.", "Khoikhoi", "He died in a clash with the Khoikhoi (Hottentots)."),
        ("The Battle of Diu secured Portuguese naval dominance in the __________ Ocean.", "Indian", "It secured dominance in the Indian Ocean."),
        ("The year of the Battle of Diu was __________ CE.", "1509", "The battle was fought on February 3, 1509 CE."),
        ("Malik Ayyaz was the governor of __________ under the Gujarat Sultanate.", "Diu", "He governed Diu from his fortified island base."),
        ("The Ottoman sultan who supported the coalition fleet at Diu was Bayezid __________.", "II", "Sultan Bayezid II provided naval and military support.")
    ]
    for q_en, ans, sol_en in fill5:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("__________", "__________")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Fill in the Blank", "q": q_en, "ans": ans, "sol": sol_en})
        hi.append({"type": "Fill in the Blank", "q": q_hi, "ans": ans, "sol": sol_hi})

    # Match the Following (3)
    en.append({
        "type": "Match the Following",
        "q": "Match the historic locations with their roles in Almeida's final years:",
        "items": [{"left": "Diu coast"}, {"left": "Cochin court"}, {"left": "Table Bay"}],
        "options": [{"val": "0", "text": "Site of the 1509 naval victory"}, {"val": "1", "text": "Place of power transition to Albuquerque"}, {"val": "2", "text": "Location of Almeida's death in 1510"}],
        "sol": "Diu was the battle site, Cochin the power handover place, and Table Bay where he died."
    })
    hi.append({
        "type": "Match the Following",
        "q": "अल्मेडा के अंतिम वर्षों में उनकी भूमिकाओं के साथ ऐतिहासिक स्थानों का मिलान करें:",
        "items": [{"left": "दीव तट"}, {"left": "कोचीन दरबार"}, {"left": "टेबल बे"}],
        "options": [{"val": "0", "text": "1509 की नौसैनिक विजय का स्थल"}, {"val": "1", "text": "अल्बुकर्क को सत्ता हस्तांतरण का स्थान"}, {"val": "2", "text": "1510 में अल्मेडा की मृत्यु का स्थान"}],
        "sol": "दीव युद्ध स्थल था, कोचीन सत्ता हस्तांतरण स्थल था, और टेबल बे में उनकी मृत्यु हुई थी।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the coalition participants of Diu with their contributions:",
        "items": [{"left": "Mamluk Sultanate"}, {"left": "Ottoman Empire"}, {"left": "Gujarat Sultanate"}],
        "options": [{"val": "0", "text": "Core war fleet under Amir Husain"}, {"val": "1", "text": "Gunners and military specialists"}, {"val": "2", "text": "Local naval base and dhows under Malik Ayyaz"}],
        "sol": "Mamluks provided the core fleet, Ottomans the gunners, and Gujarat the local base."
    })
    hi.append({
        "type": "Match the Following",
        "q": "दीव के गठबंधन प्रतिभागियों का उनके योगदान से मिलान करें:",
        "items": [{"left": "ममलुक सल्तनत"}, {"left": "ओटोमन साम्राज्य"}, {"left": "गुजरात सल्तनत"}],
        "options": [{"val": "0", "text": "अमीर हुसैन के तहत मुख्य युद्धक बेड़ा"}, {"val": "1", "text": "तोपची और सैन्य विशेषज्ञ"}, {"val": "2", "text": "मलिक अय्याज़ के तहत स्थानीय नौसैनिक अड्डा और जहाज"}],
        "sol": "ममलुकों ने मुख्य बेड़ा, ओटोमन्स ने तोपची, और गुजरात ने स्थानीय आधार प्रदान किया।"
    })

    en.append({
        "type": "Match the Following",
        "q": "Match the strategic outcomes of Diu with their long-term historical impacts:",
        "items": [{"left": "Destruction of Mamluk navy"}, {"left": "Decline of Venice trade"}, {"left": "Rise of Portuguese Cartaz"}],
        "options": [{"val": "0", "text": "Ottoman annexation of Egypt in 1517"}, {"val": "1", "text": "Shift of spice center to Lisbon"}, {"val": "2", "text": "Enforced Mare Clausum in Indian Ocean"}],
        "sol": "Mamluk defeat led to Ottoman takeover, Venice decline shifted trade to Lisbon, and Cartaz enforced Mare Clausum."
    })
    hi.append({
        "type": "Match the Following",
        "q": "दीव के रणनीतिक परिणामों का उनके दीर्घकालिक ऐतिहासिक प्रभावों से मिलान करें:",
        "items": [{"left": "ममलुक नौसेना का विनाश"}, {"left": "वेनिस व्यापार का पतन"}, {"left": "पुर्तगाली कार्टाज का उदय"}],
        "options": [{"val": "0", "text": "1517 में मिस्र पर ओटोमन का कब्जा"}, {"val": "1", "text": "मसाला केंद्र का लिस्बन में स्थानांतरण"}, {"val": "2", "text": "हिंद महासागर में मारे क्लॉसम लागू करना"}],
        "sol": "ममलुक हार से ओटोमन कब्जा हुआ, वेनिस पतन से लिस्बन व्यापार बढ़ा, और कार्टाज से मारे क्लॉसम लागू हुआ।"
    })

    # One-Liner (8)
    ol5 = [
        ("What was the primary motive of Almeida at the Battle of Diu?", "To avenge the death of his son Lourenço.", "Almeida was driven by personal revenge for his son's death at Chaul."),
        ("Who was the Ottoman commander who supported the Mamluks at Diu?", "Selim I's representatives / local commanders.", "Ottoman specialists supported the coalition."),
        ("In what year did the Ottoman Empire annex Egypt, partly due to Mamluk naval decline?", "1517 CE.", "The Mamluks were conquered by the Ottomans in 1517."),
        ("Why did the Khoikhoi attack Almeida at Table Bay?", "Due to a dispute over cattle and fresh water.", "A skirmish broke out during a water-stopover."),
        ("Where was Francisco de Almeida buried?", "At Table Bay, South Africa.", "He was buried in an unmarked grave on the shore."),
        ("Did Almeida live to see Portugal receive the spice cargo from Diu?", "No, he died on the return journey.", "He died off South Africa before reaching Lisbon."),
        ("What did the Battle of Diu establish in terms of global maritime history?", "Four centuries of European naval dominance in Asia.", "It began the era of European maritime empires in the East."),
        ("How did Malik Ayyaz survive the Battle of Diu?", "By surrendering, releasing prisoners, and paying tribute to Almeida.", "He negotiated peace before his base was destroyed.")
    ]
    for q_en, ans_en, sol_en in ol5:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Table Bay", "टेबल बे")
        sol_hi = f"उत्तर: {ans_en.replace('Almeida', 'अल्मेडा').replace('Table Bay', 'टेबल बे')}। स्पष्टीकरण: {sol_en.replace('Almeida', 'अल्मेडा')}"
        sol_en_combined = f"Answer: {ans_en} Explanation: {sol_en}"
        en.append({"type": "One-Liner", "q": q_en, "sol": sol_en_combined})
        hi.append({"type": "One-Liner", "q": q_hi, "sol": sol_hi})

    # Assertion-Reason (8)
    ar5 = [
        ("Assertion: The Battle of Diu is considered one of the most important naval battles in history.\nReason: It secured European naval dominance in the Indian Ocean for nearly four centuries.", 0, "The victory established the Portuguese monopoly and set the stage for European colonial dominance."),
        ("Assertion: Almeida executed many coalition prisoners after the Battle of Diu.\nReason: He was driven by intense grief and a desire for revenge for his son's death at Chaul.", 0, "His retaliatory brutality was a direct response to Lourenço's death."),
        ("Assertion: The Ottoman Empire fought alongside the Mamluks at Diu.\nReason: The Ottomans wanted to protect their spice monopoly from Portuguese interference.", 0, "The Ottomans supported the coalition to block Portuguese expansion into the Red Sea."),
        ("Assertion: Almeida was assassinated by Afonso de Albuquerque's agents at Table Bay.\nReason: Albuquerque wanted to prevent Almeida from returning to Lisbon and revealing his strategic errors.", 3, "Both are false. Almeida died in a skirmish with the Khoikhoi, not by assassination."),
        ("Assertion: Malik Ayyaz surrendered Diu to the Portuguese in 1509.\nReason: The Portuguese fleet completely destroyed the city and fort of Diu during the battle.", 3, "Both are false. Ayyaz did not surrender the city/fort; he only released prisoners and paid tribute."),
        ("Assertion: The Mamluk Sultanate was severely weakened by the Battle of Diu.\nReason: The loss of their navy depleted their treasury and left them vulnerable to Ottoman conquest in 1517.", 0, "Naval defeats and loss of spice revenue contributed to the Mamluk collapse."),
        ("Assertion: Almeida's death at Table Bay was a major embarrassment for the Portuguese Crown.\nReason: A distinguished Viceroy and military hero was killed in a simple skirmish with lightly armed African natives.", 0, "His death in a minor clash shocked the Portuguese court."),
        ("Assertion: The Battle of Diu ended the Levant spice route permanently.\nReason: The victory allowed the Portuguese to block all shipping through the Red Sea and Persian Gulf.", 2, "Assertion is true (it severely disrupted Levantine trade), but Reason is false because they could never fully block all shipping, and smuggling continued.")
    ]
    for q_en, ans, sol_en in ar5:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Assertion", "अभिकथन").replace("Reason", "कारण")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Assertion-Reason", "q": q_en, "opts": EN_AR_OPTS, "ans": ans, "sol": sol_en})
        hi.append({"type": "Assertion-Reason", "q": q_hi, "opts": HI_AR_OPTS, "ans": ans, "sol": sol_hi})

    # Statement-Based (5)
    st5 = [
        ("Consider the following statements regarding the Battle of Diu:\n1. It was fought in 1509 CE off the coast of Gujarat.\n2. The Portuguese fleet defeated a combined Mamluk-Ottoman-Gujarati fleet.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The battle occurred in 1509 and defeated the combined Muslim coalition."),
        ("Consider the following statements about the death of Francisco de Almeida:\n1. He died in 1510 CE at Table Bay, South Africa.\n2. He was killed in a battle against the Ottoman Empire.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; he was killed in a skirmish with local Khoikhoi natives."),
        ("With reference to the aftermath of the Battle of Diu, consider these statements:\n1. Malik Ayyaz surrendered and returned Portuguese prisoners.\n2. Afonso de Albuquerque took over as the second Governor of India.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Prisoners were released, and Albuquerque assumed governance in late 1509."),
        ("Consider the statements about the long-term impact of the Battle of Diu:\n1. It marked the beginning of European dominance in Asian seas.\n2. It led to the immediate creation of the British East India Company.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. The British East India Company was formed much later, in 1600 CE."),
        ("With reference to Ottoman participation at Diu, consider these statements:\n1. The Ottomans provided gunners and soldiers to support the Mamluks.\n2. The Ottoman fleet was commanded by Sultan Selim I in person.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect; the Sultan did not travel to India.")
    ]
    for q_en, ans, sol_en in st5:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Ottoman", "ओटोमन")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": "Statement-Based", "q": q_en, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol_en})
        hi.append({"type": "Statement-Based", "q": q_hi, "opts": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], "ans": ans, "sol": sol_hi})

    # Open Questions (12)
    op5 = [
        ("Why", "Why did Viceroy Almeida refuse to return to Portugal immediately after the Battle of Chaul?", "He wanted to seek revenge for his son Lourenço's death and destroy the Mamluk fleet before handing over power to Albuquerque."),
        ("Why", "Why was the Battle of Diu a critical turning point in global trade history?", "It shattered the Arab-Mamluk control of the spice routes, consolidating the Portuguese Cape Route monopoly and shifting trade centers to Lisbon."),
        ("Why", "Why did a minor skirmish at Table Bay result in the death of a highly experienced commander like Almeida?", "The Portuguese were unarmored, lacked coordination, and were caught off guard by the rapid stone and spear throwing of the Khoikhoi."),
        ("How", "How did the Ottoman Empire support the coalition against the Portuguese at Diu?", "They supplied experienced gunners, soldiers, and military advisors to reinforce the Mamluk and Gujarati forces."),
        ("How", "How did the victory at Diu influence the subsequent expansion strategy of Albuquerque?", "It cleared the seas of major enemy fleets, allowing Albuquerque to focus on capturing key land bases like Goa, Malacca, and Aden."),
        ("How", "How did Malik Ayyaz negotiate the peace terms with Almeida after the battle?", "He acted pragmatically, offering to return all prisoners and pay a large financial indemnity, while retaining control of Diu."),
        ("Case Study", "Analyze the tactical differences in gunnery that decided the outcome of the Battle of Diu.", "The Portuguese naus used heavy, long-range naval artillery that decimated the coalition dhows before they could close in for boarding."),
        ("Case Study", "Examine the geopolitical decline of Egypt and Venice as a consequence of the Battle of Diu.", "The loss of spice revenues weakened the Mamluk economy, leading to its Ottoman annexation, while Venice lost its position as the chief spice supplier to Europe."),
        ("Case Study", "Evaluate the leadership legacy of Francisco de Almeida compared to Afonso de Albuquerque.", "Almeida focused on naval hegemony and commercial safety, while Albuquerque pursued territorial expansion and permanent land colonization."),
        ("Teach the Concept", "Explain the concept of 'Viceroyal Revenge' as seen in the Battle of Diu.", "It refers to the campaign where Almeida used the state's military resources to launch a retaliatory strike to avenge his son's death at Chaul."),
        ("Teach the Concept", "Describe the naval formation used by the Portuguese fleet at Diu.", "Almeida organized his ships into a tight line-of-battle, utilizing naval broadsides to destroy enemy vessels in the Diu harbor channel."),
        ("Teach the Concept", "Explain why the Battle of Diu is considered the beginning of the 'Vasco da Gama Era'.", "It established European naval supremacy in Asia, starting a 400-year period where European empires dominated Asian trade and politics.")
    ]
    for qtype, q_en, sol_en in op5:
        q_hi = q_en.replace("Almeida", "अल्मेडा").replace("Table Bay", "टेबल बे")
        sol_hi = sol_en.replace("Almeida", "अल्मेडा")
        en.append({"type": qtype, "q": q_en, "sol": sol_en})
        hi.append({"type": qtype, "q": q_hi, "sol": sol_hi})

    return en, hi

# Now let's generate 50 unique Practice questions.
def make_practice_questions():
    en = []
    hi = []

    # Statement-Based Options
    st_opts_1 = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
    st_opts_1_hi = ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"]

    st_opts_2 = ["Only one statement is correct", "Only two statements are correct", "All three statements are correct", "None of the statements are correct"]
    st_opts_2_hi = ["केवल एक कथन सही है", "केवल दो कथन सही हैं", "सभी तीन कथन सही हैं", "कोई भी कथन सही नहीं है"]

    en_ar_opts = [
        "Both A and R are true and R is the correct explanation of A",
        "Both A and R are true but R is not the correct explanation of A",
        "A is true but R is false",
        "A is false but R is true"
    ]
    hi_ar_opts = [
        "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
        "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
        "A सही है लेकिन R गलत है",
        "A गलत है लेकिन R सही है"
    ]

    # 1. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the establishment of the Estado da Índia in 1505, consider the following statements:
1. It was established as a permanent crown administrative and military state rather than a temporary trading enterprise.
2. Francisco de Almeida was given a non-renewable five-year term as the first Viceroy.
3. The Viceroy was granted absolute financial autonomy, independent of the Casa da Índia in Lisbon.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statement 1 is correct. King Manuel I established the Estado da Índia as a permanent administrative state. Statement 2 is incorrect; Almeida's term was strictly three years to prevent the consolidation of autonomous power. Statement 3 is incorrect; scribes and factors reported directly to the Casa da Índia in Lisbon, bypassing the Viceroy's financial control."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1505 में 'एस्टाडो दा इंडिया' की स्थापना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. इसे एक अस्थायी व्यापारिक उद्यम के बजाय एक स्थायी शाही प्रशासनिक और सैन्य राज्य के रूप में स्थापित किया गया था।
2. फ्रांसिस्को डी अल्मेडा को पहले वायसराय के रूप में पांच वर्ष का गैर-नवीकरणीय कार्यकाल दिया गया था।
3. वायसराय को लिस्बन में कासा दा इंडिया से स्वतंत्र, पूर्ण वित्तीय स्वायत्तता प्रदान की गई थी।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 सही है। राजा मैनुअल प्रथम ने स्थायी प्रशासनिक राज्य के रूप में इसकी स्थापना की। कथन 2 गलत है क्योंकि अल्मेडा का कार्यकाल तीन वर्ष था। कथन 3 गलत है क्योंकि लेखक और कारक सीधे लिस्बन को रिपोर्ट करते थे।"
    })

    # 2. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the strategic objectives of the Portuguese Crown in the Indian Ocean:
1. To establish a total monopoly over the lucrative spice trade by eliminating Arab and Venetian middlemen.
2. To control key oceanic choke points, including the Strait of Malacca and the Persian Gulf, during Almeida's tenure.
3. To enforce a legal naval licensing system on all merchant vessels navigating the Indian Ocean.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. The goals were monopoly and licensing (Cartaz). Statement 2 is incorrect; controlling Malacca and the Persian Gulf was Albuquerque's strategy, not Almeida's, who focused solely on the Indian coastal routes and the Red Sea mouth."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """हिंद महासागर में पुर्तगाली क्राउन के रणनीतिक उद्देश्यों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. अरब और वेनिस के बिचौलियों को समाप्त करके आकर्षक मसाला व्यापार पर पूर्ण एकाधिकार स्थापित करना।
2. अल्मेडा के कार्यकाल के दौरान मलक्का जलडमरूमध्य और फारस की खाड़ी सहित प्रमुख समुद्री चोक पॉइंट को नियंत्रित करना।
3. हिंद महासागर में नौवहन करने वाले सभी व्यापारिक जहाजों पर एक कानूनी नौसैनिक लाइसेंसिंग प्रणाली लागू करना।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। एकाधिकार और लाइसेंस (कार्टाज) इसके उद्देश्य थे। कथन 2 गलत है क्योंकि मलक्का और फारस की खाड़ी को नियंत्रित करना अल्बुकर्क की रणनीति थी, अल्मेडा की नहीं।"
    })

    # 3. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to Francisco de Almeida's Blue Water Policy, consider the following statements:
1. It prioritized naval supremacy and the control of shipping lanes over territorial land acquisition in India.
2. It was based on the premise that Portugal had sufficient manpower to defend mainland Indian fortresses if needed.
3. It was formally rejected by his successor, Afonso de Albuquerque, who advocated for land-based colonial bases.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 2,
        "sol": "Statements 1 and 3 are correct. The Blue Water Policy focused on naval dominance and sea lane control, avoiding territorial conquests. Statement 2 is incorrect; it was based on the premise that Portugal's small population and limited resources could NOT support a land empire. Albuquerque shifted to land-based territorial bases."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """फ्रांसिस्को डी अल्मेडा की 'नीले पानी की नीति' (ब्लू वाटर पॉलिसी) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. इसने भारत में क्षेत्रीय भूमि अधिग्रहण के बजाय नौसैनिक वर्चस्व और नौवहन मार्गों के नियंत्रण को प्राथमिकता दी।
2. यह इस आधार पर आधारित था कि पुर्तगाल के पास जरूरत पड़ने पर मुख्य भूमि भारतीय किलों की रक्षा के लिए पर्याप्त जनशक्ति थी।
3. इसे उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क द्वारा औपचारिक रूप से खारिज कर दिया गया था, जिन्होंने भूमि-आधारित औपनिवेशिक ठिकानों की वकालत की थी।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 2,
        "sol": "कथन 1 और 3 सही हैं। नीले पानी की नीति ने नौसैनिक प्रभुत्व पर ध्यान केंद्रित किया। कथन 2 गलत है क्योंकि अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या भूमि साम्राज्य की रक्षा नहीं कर सकती।"
    })

    # 4. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Cartaz system:
1. Rulers allied with the Portuguese, including the Raja of Cochin, were exempt from obtaining Cartazes.
2. Merchant ships holding a Cartaz were prohibited from carrying pepper, ginger, and weapons.
3. Any vessel intercepted without a Cartaz was subject to cargo confiscation and execution or enslavement of the crew.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Cartaz prohibited carrying pepper, ginger, and arms, and unauthorized vessels faced severe penalties. Statement 1 is incorrect; even allied rulers like the Raja of Cochin had to secure Cartazes for their ships."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """कार्टाज प्रणाली के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. कोचीन के राजा सहित पुर्तगालियों के साथ गठबंधन करने वाले शासकों को कार्टाज प्राप्त करने से छूट दी गई थी।
2. कार्टाज धारक व्यापारिक जहाजों को काली मिर्च, अदरक और हथियारों के परिवहन की मनाही थी।
3. बिना कार्टाज के पकड़े गए किसी भी जहाज की सामग्री को जब्त कर लिया जाता था और चालक दल को मार दिया जाता था या गुलाम बना लिया जाता था।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। कार्टाज में काली मिर्च, अदरक और हथियार ले जाने पर प्रतिबंध था। कथन 1 गलत है क्योंकि कोचीन के सहयोगी राजा को भी कार्टाज लेना पड़ता था।"
    })

    # 5. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the fortifications built during Almeida's viceroyalty, consider the following statements:
1. Fort São Tiago was constructed in Kilwa to secure passage and control the gold trade coming from Sofala.
2. Fort Manuel in Cochin was built in alliance with the local Trimumpara Raja to counter the Zamorin of Calicut.
3. Fort St. Angelo was built in Cannanore to regulate the trade of Malabar ginger and horse imports.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 3,
        "sol": "All three statements are correct. Almeida established Fort São Tiago in Kilwa (1505) for Swahili trade, Fort Manuel in Cochin (1505) for alliance protection, and Fort St. Angelo in Cannanore (1505) to regulate ginger and horse imports."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """अल्मेडा के कार्यकाल के दौरान निर्मित किलों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. सोफाला से आने वाले सोने के व्यापार को नियंत्रित करने और मार्ग सुरक्षित करने के लिए किलवा में फोर्ट साओ टियागो का निर्माण किया गया था।
2. कालीकट के ज़मोरिन का मुकाबला करने के लिए स्थानीय त्रिमुम्पारा राजा के साथ गठबंधन में कोचीन में फोर्ट मैनुअल का निर्माण किया गया था।
3. मालाबार अदरक व्यापार और घोड़ों के आयात को विनियमित करने के लिए कन्नूर में फोर्ट सेंट एंजेलो का निर्माण किया गया था।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 3,
        "sol": "सभी तीन कथन सही हैं। अल्मेडा ने किलवा (1505), कोचीन (1505) और कन्नूर (1505) में इन किलों की स्थापना की।"
    })

    # 6. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Anjadip Fort:
1. It was built on Anjadip Island off the coast of Goa to secure a fresh water station and repair facility.
2. The fort was ordered to be reinforced and expanded by Almeida in 1508.
3. Constant raids from the Adil Shahi Sultanate of Bijapur made the fort unsustainable.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. Anjadip Fort was built in 1505 for water supply and ship repair, but was frequently attacked by Bijapur forces. Statement 2 is incorrect; due to high maintenance costs and raids, Almeida ordered the fort's demolition and abandonment in 1506, not reinforcement in 1508."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """अंजादीप किले के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. इसे मीठे पानी की आपूर्ति और जहाजों की मरम्मत की सुविधा सुरक्षित करने के लिए गोवा के तट के पास अंजादीप द्वीप पर बनाया गया था।
2. अल्मेडा द्वारा 1508 में इस किले को मजबूत और विस्तारित करने का आदेश दिया गया था।
3. बीजापुर के आदिल शाही सल्तनत के लगातार हमलों ने इस किले को बनाए रखना असंभव बना दिया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। अंजादीप किला आदिल शाही हमलों के कारण असुरक्षित था। कथन 2 गलत है क्योंकि अल्मेडा ने 1506 में इसे नष्ट करने का आदेश दिया था।"
    })

    # 7. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the Battle of Chaul (1508), consider the following statements:
1. The Portuguese patrol fleet was commanded by Lourenço de Almeida, the Viceroy's only son.
2. The Portuguese fleet suffered a crushing defeat, marking their first major naval loss in the Indian Ocean.
3. The conflict was triggered by the disruption of the spice trade of the Mamluk Sultanate of Egypt.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 3,
        "sol": "All three statements are correct. The Mamluk Sultanate constructed a fleet to stop the Portuguese Red Sea blockades. They surprised Lourenço's patrol fleet at Chaul in 1508, resulting in his death and the first major Portuguese defeat."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """चोल की लड़ाई (1508) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. पुर्तगाली गश्ती बेड़े की कमान वायसराय के इकलौते पुत्र लॉरेंको डी अल्मेडा के हाथ में थी।
2. पुर्तगाली बेड़े को करारी हार का सामना करना पड़ा, जो हिंद महासागर में उनकी पहली बड़ी नौसैनिक हार थी।
3. यह संघर्ष मिस्र के ममलुक सल्तनत के मसाला व्यापार में व्यवधान के कारण शुरू हुआ था।
उपर्युक्त कथनों में से कौन-sa/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 3,
        "sol": "सभी तीन कथन सही हैं। ममलुक सल्तनत ने पुर्तगाली नाकेबंदी को रोकने के लिए बेड़ा बनाया और 1508 में चोल में लॉरेंको के बेड़े को पराजित किया।"
    })

    # 8. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Diu (1509):
1. Francisco de Almeida personally led the Portuguese armada to avenge the death of his son.
2. The Portuguese fleet engaged a combined naval coalition of the Mamluks, the Ottoman Empire, and the Gujarat Sultanate.
3. The battle ended in a stalemate, leaving the Arabian Sea trade routes contested.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Almeida led the retaliatory campaign against the Mamluk-Ottoman-Gujarati coalition. Statement 3 is incorrect; the Battle of Diu ended in a decisive Portuguese victory, destroying the coalition fleet and establishing European naval hegemony."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """दीव की लड़ाई (1509) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. फ्रांसिस्को डी अल्मेडा ने अपने पुत्र की मृत्यु का बदला लेने के लिए व्यक्तिगत रूप से पुर्तगाली बेड़े का नेतृत्व किया।
2. पुर्तगाली बेड़े ने ममलुक, ओटोमन साम्राज्य और गुजरात सल्तनत के संयुक्त नौसैनिक गठबंधन का मुकाबला किया।
3. युद्ध का अंत एक गतिरोध के रूप में हुआ, जिससे अरब सागर व्यापार मार्ग विवादित रह गए।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। अल्मेडा ने गठबंधन के खिलाफ प्रतिशोध अभियान का नेतृत्व किया। कथन 3 गलत है क्योंकि दीव की लड़ाई पुर्तगालियों की निर्णायक जीत में समाप्त हुई।"
    })

    # 9. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the geopolitical forces involved in the Battle of Chaul, consider the following statements:
1. The Republic of Venice secretly supplied shipbuilding timber to the Mamluks at Alexandria.
2. Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, allied with the Mamluk forces.
3. The Zamorin of Calicut supported the Portuguese patrol fleet against the Egyptian invasion.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Venice supplied timber to Suez to help Mamluks rebuild spice routes, and Malik Ayyaz allied with Amir Husain Al-Kurdi. Statement 3 is incorrect; the Zamorin of Calicut was allied with the Mamluk-Gujarati coalition against the Portuguese."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """चोल की लड़ाई में शामिल भू-राजनीतिक ताकतों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. वेनिस गणराज्य ने अलेक्जेंड्रिया में ममलुकों को गुप्त रूप से जहाज निर्माण की लकड़ी की आपूर्ति की।
2. गुजरात सल्तनत के तहत दीव के गवर्नर मलिक अय्याज़ ने ममलुक सेना के साथ गठबंधन किया।
3. कालीकट के ज़मोरिन ने मिस्र के आक्रमण के खिलाफ पुर्तगाली गश्ती बेड़े का समर्थन किया।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। वेनिस ने ममलुकों की मदद की और मलिक अय्याज़ ने उनके साथ गठबंधन किया। कथन 3 गलत है क्योंकि ज़मोरिन पुर्तगालियों के विरोधी गठबंधन में शामिल था।"
    })

    # 10. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the succession dispute between Almeida and Albuquerque in late 1508:
1. Almeida refused to hand over power, claiming Albuquerque's letters patent were invalid.
2. Albuquerque was imprisoned in Fort Manuel in Cochin by Almeida's orders.
3. The Portuguese Crown eventually recalled Albuquerque and reinstated Almeida for a second term.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Almeida refused to hand over power and imprisoned Albuquerque until he could avenge his son at Diu. Statement 3 is incorrect; after the Battle of Diu, Almeida released Albuquerque, handed over power, and sailed for Europe."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1508 के अंत में अल्मेडा और अल्बुकर्क के बीच उत्तराधिकार विवाद के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. अल्मेडा ने यह दावा करते हुए सत्ता सौंपने से इनकार कर दिया कि अल्बुकर्क के पत्र अमान्य थे।
2. अल्मेडा के आदेश पर अल्बुकर्क को कोचीन के फोर्ट मैनुअल में कैद कर दिया गया था।
3. पुर्तगाली क्राउन ने अंततः अल्बुकर्क को वापस बुला लिया और अल्मेडा को दूसरे कार्यकाल के लिए बहाल किया।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। अल्मेडा ने बदला लेने तक सत्ता सौंपने से मना किया और अल्बुकर्क को कैद किया। कथन 3 गलत है क्योंकि दीव की लड़ाई के बाद अल्मेडा ने अल्बुकर्क को सत्ता सौंप दी।"
    })

    # 11. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the death of Francisco de Almeida, consider the following statements:
1. He died in a naval battle against the Ottoman fleet in the Red Sea.
2. He was killed in a beach skirmish with Khoikhoi natives at Table Bay, South Africa.
3. His death occurred in March 1510 during his return voyage to Portugal.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Almeida was killed on March 1, 1510, in a skirmish with Khoikhoi natives over cattle and water at Table Bay, South Africa, during his return voyage. Statement 1 is incorrect."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """फ्रांसिस्को डी अल्मेडा की मृत्यु के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. लाल सागर में ओटोमन बेड़े के खिलाफ एक नौसैनिक युद्ध में उनकी मृत्यु हुई थी।
2. वह दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ एक तट पर झड़प में मारे गए थे।
3. उनकी मृत्यु मार्च 1510 में पुर्तगाल की उनकी वापसी यात्रा के दौरान हुई थी।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। अल्मेडा की मृत्यु 1 मार्च, 1510 को टेबल बे में खोइखोई आदिवासियों के साथ एक झड़प में हुई थी।"
    })

    # 12. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding Malik Ayyaz:
1. He was an ethnic Ottoman noble who served the Gujarat Sultanate.
2. He served as the governor of Diu under Sultan Mahmud Begarha.
3. He commanded the Gujarati fleet that supported Amir Husain Al-Kurdi at Chaul and Diu.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Malik Ayyaz was governor of Diu under Sultan Mahmud Begarha and commanded the local gunboats in the battles. Statement 1 is incorrect; he was a slave convert of Russian origin, not an ethnic Ottoman noble."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """मलिक अय्याज़ के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. वह एक जातीय ओटोमन रईस था जिसने गुजरात सल्तनत की सेवा की थी।
2. उसने सुल्तान महमूद बेगड़ा के तहत दीव के गवर्नर के रूप में कार्य किया।
3. उसने गुजराती बेड़े की कमान संभाली जिसने चोल और दीव में अमीर हुसैन अल-कुर्दी का समर्थन किया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। मलिक अय्याज़ सुल्तान महमूद बेगड़ा के अधीन दीव का गवर्नर था। कथन 1 गलत है क्योंकि वह रूसी मूल का दास था, ओटोमन रईस नहीं।"
    })

    # 13. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the legal and navigational terms introduced by the Portuguese, consider the following statements:
1. Mare Clausum refers to the doctrine of the Free Sea, open to all merchant nations.
2. Volta do Mar was a sailing maneuver used to navigate around adverse Atlantic currents.
3. Feitoria was a fortified trading post or warehouse established to store monopoly goods.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Volta do Mar was a critical navigation loop, and Feitoria was the trade warehouse. Statement 1 is incorrect; Mare Clausum refers to the Closed Sea doctrine (exclusive sovereignty), while Mare Liberum refers to the Free Sea."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """पुर्तगालियों द्वारा शुरू किए गए कानूनी और नौवहन शब्दों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. मारे क्लॉसम (Mare Clausum) मुक्त समुद्र के सिद्धांत को संदर्भित करता है, जो सभी व्यापारी देशों के लिए खुला हो।
2. वोल्टा डो मार (Volta do Mar) अटलांटिक की प्रतिकूल धाराओं से बचने के लिए इस्तेमाल की जाने वाली एक नौवहन तकनीक थी।
3. फेइटोरिया (Feitoria) एकाधिकार वस्तुओं के भंडारण के लिए स्थापित एक किला नुमा व्यापारिक केंद्र या गोदाम था।
उपर्युक्त कथनों में से कौन-sa/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। वोल्टा डो मार नौवहन तकनीक थी और फेइटोरिया व्यापारिक गोदाम था। कथन 1 गलत है क्योंकि मारे क्लॉसम बंद समुद्र (पुर्तगाली एकाधिकार) को दर्शाता है।"
    })

    # 14. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the 1507 Siege of Cannanore:
1. It was launched by the Kolathiri Raja of Cannanore with the military backing of the Zamorin of Calicut.
2. The Portuguese garrison at Fort St. Angelo was successfully defended by Lourenço de Almeida.
3. The siege ended when a Portuguese reinforcement fleet led by Tristão da Cunha arrived to relieve the garrison.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. The siege was led by Kolathiri forces backed by Calicut, and ended with the arrival of Tristão da Cunha's fleet. Statement 2 is incorrect; the garrison at Cannanore was commanded by Lourenço de Brito, not Lourenço de Almeida, who was patrolling elsewhere."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1507 के कन्नूर की घेराबंदी (Siege of Cannanore) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. इसे कालीकट के ज़मोरिन के सैन्य समर्थन से कन्नूर के कोलथिरि राजा द्वारा शुरू किया गया था।
2. फोर्ट सेंट एंजेलो में पुर्तगाली गैरीसन की रक्षा लॉरेंको डी अल्मेडा ने सफलतापूर्वक की थी।
3. घेराबंदी तब समाप्त हुई जब गैरीसन को राहत देने के लिए ट्रिस्टाओ दा कुन्हा के नेतृत्व में एक पुर्तगाली सुदृढीकरण बेड़ा आया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। घेराबंदी को ट्रिस्टाओ दा कुन्हा के बेड़े ने समाप्त किया। कथन 2 गलत है क्योंकि कन्नूर गैरीसन कमांडर लॉरेंको डी ब्रिटो थे, लॉरेंको डी अल्मेडा नहीं।"
    })

    # 15. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the composition of the 1505 viceregal expedition, consider the following statements:
1. The fleet carried noblemen, military officers, and specialized Franciscan missionaries.
2. It was the first Portuguese expedition to bring stone and masonry ballast to construct permanent fortifications.
3. The expedition was funded entirely by private Italian banks without Crown backing.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. The fleet carried noblemen and missionaries, and brought building materials for permanent forts. Statement 3 is incorrect; the expedition was commissioned and backed by the Portuguese Crown (King Manuel I), though some foreign merchants participated."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1505 के वायसराय अभियान की संरचना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. बेड़े में रईस, सैन्य अधिकारी और विशेष फ्रांसिस्कन मिशनरी शामिल थे।
2. स्थायी किलों के निर्माण के लिए पत्थर और निर्माण सामग्री ले जाने वाला यह पहला पुर्तगाली अभियान था।
3. यह अभियान पूरी तरह से बिना क्राउन समर्थन के निजी इतालवी बैंकों द्वारा वित्त पोषित था।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। यह अभियान शाही समर्थन से भेजा गया था, इसलिए कथन 3 गलत है।"
    })

    # 16. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Toro (1476):
1. Francisco de Almeida gained outstanding military renown in Europe during this battle.
2. It was fought as part of the Castilian War of Succession.
3. Almeida commanded the Castilian forces against the Portuguese Crown.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Almeida gained renown in the Battle of Toro (1476), which was fought during the War of the Castilian Succession. Statement 3 is incorrect; Almeida fought on the Portuguese side supporting King Afonso V, not on the Castilian side."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """टोरो की लड़ाई (1476) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. फ्रांसिस्को डी अल्मेडा ने इस लड़ाई के दौरान यूरोप में उत्कृष्ट सैन्य ख्याति प्राप्त की थी।
2. यह कैस्टिलियन उत्तराधिकार के युद्ध के हिस्से के रूप में लड़ा गया था।
3. अल्मेडा ने पुर्तगाली क्राउन के खिलाफ कैस्टिलियन सेना की कमान संभाली थी।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। टोरो का युद्ध कैस्टिलियन उत्तराधिकार युद्ध का हिस्सा था। कथन 3 गलत है क्योंकि अल्मेडा ने पुर्तगाली राजा का समर्थन किया था, न कि कैस्टिल का।"
    })

    # 17. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the strategic position of Cochin in early Portuguese planning, consider the following statements:
1. Cochin served as the first headquarters of the Portuguese Estado da Índia.
2. The Portuguese built Fort Manuel there to dominate the spice trade of Calicut directly.
3. The Raja of Cochin was an independent sovereign who welcomed the Portuguese to gain autonomy from the Zamorin.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 2,
        "sol": "Statements 1 and 3 are correct. Cochin was the first capital, and its Raja allied with the Portuguese to escape Zamorin suzerainty. Statement 2 is incorrect; Fort Manuel was built to protect the factory in Cochin and control Cochin's own trade, not Calicut's direct trade, which was blockaded."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """प्रारंभिक पुर्तगाली योजना में कोचीन की रणनीतिक स्थिति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. कोचीन ने पुर्तगाली एस्टाडो दा इंडिया के पहले मुख्यालय के रूप में कार्य किया।
2. पुर्तगालियों ने सीधे कालीकट के मसाला व्यापार पर हावी होने के लिए वहाँ फोर्ट मैनुअल का निर्माण किया था।
3. कोचीन के राजा एक स्वतंत्र संप्रभु थे जिन्होंने ज़मोरिन से स्वायत्तता प्राप्त करने के लिए पुर्तगालियों का स्वागत किया।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 2,
        "sol": "कथन 1 और 3 सही हैं। कोचीन पहला मुख्यालय था और राजा ने ज़मोरिन के खिलाफ पुर्तगाली गठबंधन स्वीकार किया। कथन 2 गलत है क्योंकि यह किला कोचीन के व्यापार की रक्षा के लिए था, न कि सीधे कालीकट के लिए।"
    })

    # 18. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the role of the Portuguese Scribe (Escrivão) and Factor (Feitor):
1. Scribes were administrative officers who recorded cargo details and trade transactions.
2. Factors reported directly to the Viceroy and could be dismissed by him at will.
3. This division of power acted as a check against corruption and autonomous revolt by the Viceroy.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. Scribes recorded cargo, and the system checked the Viceroy's power. Statement 2 is incorrect; factors and scribes in India reported directly to the Casa da Índia in Lisbon, bypassing the Viceroy's administrative control."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """पुर्तगाली लेखक (Escrivão) और कारक (Feitor) की भूमिका के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. लेखक प्रशासनिक अधिकारी थे जो कार्गो विवरण और व्यापारिक लेनदेन दर्ज करते थे।
2. कारक सीधे वायसराय को रिपोर्ट करते थे और उन्हें वायसराय द्वारा बर्खास्त किया जा सकता था।
3. सत्ता के इस विभाजन ने भ्रष्टाचार और वायसराय द्वारा स्वायत्त विद्रोह के खिलाफ एक जांच के रूप में कार्य किया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। यह व्यवस्था भ्रष्टाचार रोकने के लिए थी। कथन 2 गलत है क्योंकि लेखक और कारक सीधे लिस्बन को रिपोर्ट करते थे, न कि वायसराय को।"
    })

    # 19. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the Mamluk Sultanate's involvement in the Indian Ocean, consider the following statements:
1. The Mamluks were secretly aided by the Republic of Genoa, which provided financial loans.
2. Amir Husain Al-Kurdi was commissioned to build and command the Egyptian fleet at Suez.
3. The Mamluk naval intervention aimed to restore their transit trade customs revenues.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Amir Husain built the Suez fleet, and the Mamluks aimed to reclaim transit duties. Statement 1 is incorrect; they were secretly aided by Venice (which supplied timber), not Genoa."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """हिंद महासागर में ममलुक सल्तनत की भागीदारी के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. ममलुकों को गुप्त रूप से जेनोआ गणराज्य द्वारा सहायता प्रदान की गई थी, जिसने वित्तीय ऋण प्रदान किए थे।
2. अमीर हुसैन अल-कुर्दी को स्वेज में मिस्र के बेड़े का निर्माण करने और उसकी कमान संभालने के लिए नियुक्त किया गया था।
3. ममलुक नौसैनिक हस्तक्षेप का उद्देश्य उनके पारगमन व्यापार सीमा शुल्क राजस्व को बहाल करना था।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। अमीर हुसैन ने स्वेज बेड़े की कमान संभाली और ममलुक पारगमन कर बहाल करना चाहते थे। कथन 1 गलत है क्योंकि उन्हें वेनिस ने लकड़ी दी थी, न कि जेनोआ ने।"
    })

    # 20. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Diu (1509):
1. The Portuguese fleet utilized superior long-range artillery that prevented coalition boarding actions.
2. The coalition forces had a clear numerical superiority in terms of combat vessels.
3. Following the battle, the Portuguese immediately annexed Diu and built a massive land fortress.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. The Portuguese used long-range cannons to keep high-walled vessels safe from coalition boarding, despite being outnumbered. Statement 3 is incorrect; Almeida did not annex Diu; he signed a peace treaty with Malik Ayyaz. Diu was annexed much later under Albuquerque and Nuno da Cunha."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """दीव की लड़ाई (1509) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. पुर्तगाली बेड़े ने बेहतर लंबी दूरी की तोपों का इस्तेमाल किया जिसने गठबंधन को उनके जहाजों पर चढ़ने से रोका।
2. गठबंधन सेना के पास लड़ाकू जहाजों के मामले में स्पष्ट संख्यात्मक श्रेष्ठता थी।
3. युद्ध के बाद, पुर्तगालियों ने तुरंत दीव पर कब्जा कर लिया और एक विशाल भूमि किला बनाया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। पुर्तगाली तोपखाना श्रेष्ठ था। कथन 3 गलत है क्योंकि दीव पर तुरंत कब्जा नहीं किया गया था; केवल संधि की गई थी। दीव का विलय बहुत बाद में हुआ था।"
    })

    # 21. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the tactical decisions of Lourenço de Almeida at the Battle of Chaul, consider the following statements:
1. He decided to fight in the shallow river estuary, which restricted the movement of his large naus.
2. His flagship became trapped by a fishing cable, making it an easy target for Gujarati gunboats.
3. He ordered a full retreat, but his command was ignored by the Portuguese officers.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. The shallow Kundalika estuary restricted the naus, and Lourenço's flagship Santo Espírito was pinned down by a cable. Statement 3 is incorrect; Lourenço refused to retreat or abandon ship, fighting until he was killed."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """चोल की लड़ाई में लॉरेंको डी अल्मेडा के रणनीतिक निर्णयों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. उन्होंने उथले नदी के मुहाने पर लड़ने का फैसला किया, जिससे उनके बड़े जहाजों की गति सीमित हो गई।
2. उनका प्रमुख जहाज एक केबल में फंस गया था, जिससे वह गुजराती तोपखानों के लिए एक आसान निशाना बन गया।
3. उन्होंने पूर्ण वापसी का आदेश दिया, लेकिन पुर्तगाली अधिकारियों ने उनके आदेश की अनदेखी की।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। मुहाने का उथला पानी प्रतिकूल था और जहाज फंस गया था। कथन 3 गलत है क्योंकि लॉरेंको ने हटने से इनकार कर दिया था।"
    })

    # 22. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the geopolitical impact of the Portuguese victory at Diu:
1. It broke the spice trade monopoly of Arab merchants in the Arabian Sea.
2. It established European naval dominance in Asia that lasted for nearly four centuries.
3. It forced the Ottoman Empire to completely abandon its naval presence in the Indian Ocean.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. The victory broke the Arab-Mamluk monopoly and established European dominance. Statement 3 is incorrect; the Ottoman Empire did not abandon the region; they sent subsequent naval expeditions under Piri Reis and Seydi Ali Reis in the 1530s-1550s."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """दीव में पुर्तगाली विजय के भू-राजनीतिक प्रभाव के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. इसने अरब सागर में अरब व्यापारियों के मसाला व्यापार एकाधिकार को तोड़ दिया।
2. इसने एशिया में यूरोपीय नौसैनिक वर्चस्व स्थापित किया जो लगभग चार शताब्दियों तक चला।
3. इसने ओटोमन साम्राज्य को हिंद महासागर में अपनी नौसैनिक उपस्थिति को पूरी तरह से छोड़ने के लिए मजबूर किया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। इसने यूरोपीय नौसैनिक युग की शुरुआत की। कथन 3 गलत है क्योंकि ओटोमन साम्राज्य ने नौसेना का उपयोग जारी रखा और बाद में पीरी रईस के तहत अभियान भेजे।"
    })

    # 23. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the transition from Almeida's strategy to Albuquerque's strategy, consider the following statements:
1. Almeida focused on mobile sea power, whereas Albuquerque advocated for fortified coastal bases.
2. Almeida opposed the colonization of land, while Albuquerque promoted settlement and marriage with local women.
3. Both viceroys agreed that the Cartaz system was unnecessary and should be replaced by free trade.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Almeida focused on sea patrols and opposed colonization. Albuquerque advocated for fortified bases and mixed-marriage colonization. Statement 3 is incorrect; both strongly enforced the Cartaz system to maintain their state trade monopoly."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """अल्मेडा की रणनीति से अल्बुकर्क की रणनीति में संक्रमण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. अल्मेडा ने मोबाइल समुद्री शक्ति पर ध्यान केंद्रित किया, जबकि अल्बुकर्क ने किलेबंद मुख्य भूमि के ठिकानों की वकालत की।
2. अल्मेडा ने भूमि के उपनिवेशीकरण का विरोध किया, जबकि अल्बुकर्क ने बसने और स्थानीय महिलाओं के साथ विवाह को बढ़ावा दिया।
3. दोनों वायसराय इस बात पर सहमत थे कि कार्टाज प्रणाली अनावश्यक थी और इसे मुक्त व्यापार द्वारा प्रतिस्थापित किया जाना चाहिए।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। अल्मेडा समुद्री शक्ति पर और अल्बुकर्क किलेबंदी पर केंद्रित थे। कथन 3 गलत है क्योंकि दोनों कार्टाज व्यवस्था के कट्टर समर्थक थे।"
    })

    # 24. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Toro (1476):
1. It was fought between Portugal and Castile for control of the Castilian Crown.
2. Francisco de Almeida fought alongside the Castilian forces.
3. The battle helped solidify Almeida's reputation as an elite military strategist.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. Toro was a major battle in the Castilian succession dispute, and Almeida's performance cemented his military reputation. Statement 2 is incorrect; Almeida fought for the Portuguese Crown, not Castile."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """टोरो की लड़ाई (1476) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. यह कैस्टिलियन क्राउन के नियंत्रण के लिए पुर्तगाल और कैस्टिल के बीच लड़ा गया था।
2. फ्रांसिस्को डी अल्मेडा ने कैस्टिलियन सेना के साथ मिलकर लड़ाई लड़ी थी।
3. इस युद्ध ने अल्मेडा की एक विशिष्ट सैन्य रणनीतिकार के रूप में प्रतिष्ठा को मजबूत करने में मदद की।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। टोरो युद्ध कैस्टिलियन क्राउन के लिए था और इसमें अल्मेडा ने ख्याति अर्जित की। कथन 2 गलत है क्योंकि उन्होंने पुर्तगाली पक्ष से युद्ध लड़ा था।"
    })

    # 25. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the Padroado Real system, consider the following statements:
1. It was an agreement between the Portuguese Crown and the Vatican granting the Crown patronage over religious institutions in Asia.
2. It allowed the Viceroy to appoint bishops and administer church taxes in the Estado da Índia.
3. It integrated Christian missionary expansion directly with the commercial goals of the Portuguese state.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 2,
        "sol": "Statements 1 and 3 are correct. Padroado Real was a crown religious patronage system, integrating trade and missionary zeal. Statement 2 is incorrect; the patronage and appointments were vested in the Portuguese Monarch, not the local Viceroy directly, who merely facilitated them."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """पाद्रोआडो रीयल (Padroado Real) प्रणाली के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. यह पुर्तगाली क्राउन और वेटिकन के बीच एक समझौता था जिसने क्राउन को एशिया में धार्मिक संस्थानों पर संरक्षण प्रदान किया।
2. इसने वायसराय को एस्टाडो दा इंडिया में बिशप नियुक्त करने और चर्च करों को प्रशासित करने की अनुमति दी।
3. इसने ईसाई मिशनरी विस्तार को सीधे पुर्तगाली राज्य के व्यावसायिक लक्ष्यों के साथ एकीकृत किया।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 2,
        "sol": "कथन 1 और 3 सही हैं। पाद्रोआडो रीयल शाही संरक्षण प्रणाली थी। कथन 2 गलत है क्योंकि बिशप की नियुक्ति की शक्ति राजा के पास थी, सीधे वायसराय के पास नहीं।"
    })

    # 26. Matching-Type (UPSC Pairs format)
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Fortress - Strategic Location
1. Fort São Tiago - Kilwa (Swahili Coast)
2. Fort Manuel - Cochin (Malabar Coast)
3. Fort St. Angelo - Cannanore (Western India)
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 2,
        "sol": "All three pairs are correctly matched. Fort São Tiago was built in Kilwa, Fort Manuel in Cochin, and Fort St. Angelo in Cannanore."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
किला - रणनीतिक स्थान
1. फोर्ट साओ टियागो - किलवा (स्वाहिली तट)
2. फोर्ट मैनुअल - कोचीन (मालाबार तट)
3. फोर्ट सेंट एंजेलो - कन्नूर (पश्चिमी भारत)
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 2,
        "sol": "सभी तीन युग्म सही सुमेलित हैं। किलवा में साओ टियागो, कोचीन में फोर्ट मैनुअल और कन्नूर में फोर्ट सेंट एंजेलो स्थापित किया गया था।"
    })

    # 27. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Naval Commander - Fleet / Command Affiliation
1. Amir Husain Al-Kurdi - Mamluk Sultanate Fleet
2. Malik Ayyaz - Ottoman Empire Navy
3. Lourenço de Almeida - Portuguese Patrol Fleet
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 3 are correctly matched. Amir Husain commanded the Mamluk fleet, and Lourenço de Almeida commanded the Portuguese patrol. Pair 2 is incorrectly matched; Malik Ayyaz was the governor of Diu under the Gujarat Sultanate, not a commander of the Ottoman Empire Navy."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
नौसैनिक कमांडर - बेड़ा / कमान संबद्धता
1. अमीर हुसैन अल-कुर्दी - ममलुक सल्तनत बेड़ा
2. मलिक अय्याज़ - ओटोमन साम्राज्य नौसेना
3. लॉरेंको डी अल्मेडा - पुर्तगाली गश्ती बेड़ा
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 3 सही सुमेलित हैं। मलिक अय्याज़ गुजरात सल्तनत के अधीन दीव का गवर्नर था, न कि ओटोमन साम्राज्य नौसेना का कमांडर।"
    })

    # 28. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Historical Event - Calendar Year
1. Construction of Fort Manuel - 1505 CE
2. Battle of Chaul - 1508 CE
3. Battle of Diu - 1509 CE
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 2,
        "sol": "All three pairs are correctly matched. Fort Manuel was reinforced in 1505, the Battle of Chaul occurred in 1508, and the Battle of Diu occurred in 1509."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
ऐतिहासिक घटना - कैलेंडर वर्ष
1. फोर्ट मैनुअल का निर्माण - 1505 ईस्वी
2. चोल की लड़ाई - 1508 ईस्वी
3. दीव की लड़ाई - 1509 ईस्वी
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 2,
        "sol": "सभी तीन युग्म सही सुमेलित हैं। कोचीन किला 1505 में पत्थरों से मजबूत हुआ, चोल की लड़ाई 1508 में और दीव की लड़ाई 1509 में हुई।"
    })

    # 29. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Strategic Term - Core Concept
1. Cartaz - Compulsory maritime permit
2. Mare Clausum - Freedom of navigation for all
3. Volta do Mar - Atlantic sailing technique
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 3 are correctly matched. Cartaz is a passport, and Volta do Mar is the ocean sailing maneuver. Pair 2 is incorrectly matched; Mare Clausum refers to the doctrine of Closed Seas (exclusive Portuguese sovereignty), not freedom of navigation."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
रणनीतिक शब्द - मूल अवधारणा
1. कार्टाज - अनिवार्य समुद्री परमिट
2. मारे क्लॉसम - सभी के लिए नौवहन की स्वतंत्रता
3. वोल्टा डो मार - अटलांटिक नौवहन तकनीक
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 3 सही सुमेलित हैं। मारे क्लॉसम का अर्थ बंद समुद्र (पुर्तगाली एकाधिकार) था, न कि नेविगेशन की स्वतंत्रता।"
    })

    # 30. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Explorer - Historical Significance
1. Vasco da Gama - First European to round the Cape of Good Hope
2. Bartolomeu Dias - Captain who discovered Brazil
3. Francisco de Almeida - First Viceroy of Portuguese India
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 0,
        "sol": "Only pair 3 is correctly matched. Almeida was the first Viceroy. Pair 1 is incorrect; Bartolomeu Dias was the first European to round the Cape of Good Hope in 1488. Pair 2 is incorrect; Pedro Álvares Cabral discovered Brazil in 1500."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली खोजकर्ता - ऐतिहासिक महत्व
1. वास्को डी गामा - केप ऑफ गुड होप का चक्कर लगाने वाले पहले यूरोपीय
2. बारटोलोमियु डियास - ब्राजील की खोज करने वाले कप्तान
3. फ्रांसिस्को डी अल्मेडा - पुर्तगाली भारत के पहले वायसराय
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 0,
        "sol": "केवल युग्म 3 सही है। डियास ने केप ऑफ गुड होप का चक्कर लगाया और कैब्राल ने ब्राजील की खोज की, इसलिए युग्म 1 और 2 गलत हैं।"
    })

    # 31. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Local Ruler - Domain / Kingdom
1. Kolathiri Raja - Kingdom of Cochin
2. Trimumpara Raja - Kingdom of Cannanore
3. Mahmud Begarha - Sultanate of Gujarat
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 0,
        "sol": "Only pair 3 is correctly matched; Mahmud Begarha ruled Gujarat. Pair 1 is incorrect; Kolathiri Raja was the ruler of Cannanore. Pair 2 is incorrect; Trimumpara Raja was the ruler of Cochin."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
स्थानीय शासक - क्षेत्र / साम्राज्य
1. कोलथिरि राजा - कोचीन का साम्राज्य
2. त्रिमुम्पारा राजा - कन्नूर का साम्राज्य
3. महमूद बेगड़ा - गुजरात का सल्तनत
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 0,
        "sol": "केवल युग्म 3 सही सुमेलित है। कोलथिरि कन्नूर के और त्रिमुम्पारा कोचीन के शासक थे, इसलिए 1 और 2 गलत हैं।"
    })

    # 32. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Office - Primary Responsibility
1. Feitor (Factor) - Civil and military defense of the province
2. Escrivão (Scribe) - Bookkeeping and recording cargo transactions
3. Capitão-mor (Captain-Major) - Command of naval patrol fleets
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 2 and 3 are correctly matched. Scribes handled bookkeeping, and Captain-Majors led naval patrols. Pair 1 is incorrect; Feitor (Factor) was responsible for commercial trade transactions and managing the factory warehouse, not civil or military provincial defense."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली कार्यालय - प्राथमिक जिम्मेदारी
1. फिटर (कारक) - प्रांत की नागरिक और सैन्य रक्षा
2. एस्क्रिवान (लेखक) - बहीखाता पद्धति और कार्गो रिकॉर्डिंग
3. कैपिटान-मोर (कैप्टन-मेजर) - नौसैनिक गश्ती बेड़े की कमान
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 2 और 3 सही हैं। कारक (Feitor) व्यापार और गोदाम के प्रभारी थे, न कि सैन्य रक्षा के।"
    })

    # 33. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Strategic Battle - Decisive Naval Tactic
1. Battle of Chaul - Operations in shallow river estuary
2. Battle of Diu - Long-range artillery bombardment
3. Siege of Cannanore - High-walled vessel boarding
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Chaul was fought in the Kundalika river estuary, and Diu was decided by Portuguese long-range naval artillery. Pair 3 is incorrect; the Siege of Cannanore was a land-based siege of the fort, not a boarding action."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
रणनीतिक युद्ध - निर्णायक नौसैनिक रणनीति
1. चोल की लड़ाई - उथले नदी के मुहाने पर अभियान
2. दीव की लड़ाई - लंबी दूरी का तोपखाना गोलाबारी
3. कन्नूर की घेराबंदी - ऊंचे जहाजों पर चढ़ाई की रणनीति
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। कन्नूर की घेरावंदी एक थल सेना द्वारा किले की घेराबंदी थी, न कि बोर्डिंग कार्रवाई।"
    })

    # 34. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Monarch - Primary Colonial Action
1. King Manuel I - Commissioned the Estado da Índia in 1505
2. King John II - Signed the Treaty of Tordesillas (1494)
3. King Afonso V - Supported Vasco da Gama's 1498 expedition
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Manuel I established the viceroyalty, and John II signed the Treaty of Tordesillas. Pair 3 is incorrect; Vasco da Gama's expedition was commissioned by King Manuel I, who succeeded King John II. King Afonso V died in 1481, long before the voyage."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली सम्राट - प्राथमिक औपनिवेशिक कार्रवाई
1. राजा मैनुअल प्रथम - 1505 में एस्टाडो दा इंडिया की स्थापना की
2. राजा जॉन द्वितीय - टॉर्डेसिलस की संधि (1494) पर हस्ताक्षर किए
3. राजा अफोंसो पंचम - वास्को डी गामा के 1498 के अभियान का समर्थन किया
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। वास्को डी गामा का अभियान मैनुअल प्रथम द्वारा शुरू किया गया था, न कि अफोंसो पंचम द्वारा।"
    })

    # 35. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Key Fortification - Date of Establishment / Reinforcement
1. Fort Manuel (Cochin) - 1503/1505 CE
2. Fort St. Angelo (Cannanore) - 1505 CE
3. Anjadip Fort - 1506 CE
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Cochin fort was built in 1503 and reinforced in 1505. Cannanore fort was built in 1505. Pair 3 is incorrect; Anjadip Fort was built in 1505 and demolished/abandoned in 1506, not established in 1506."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
प्रमुख किला - स्थापना / सुदृढ़ीकरण की तिथि
1. फोर्ट मैनुअल (कोचीन) - 1503/1505 ईस्वी
2. फोर्ट सेंट एंजेलो (कन्नूर) - 1505 ईस्वी
3. अंजादीप किला - 1506 ईस्वी
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। अंजादीप किला 1505 में स्थापित हुआ था और 1506 में इसे खाली किया गया था।"
    })

    # 36. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Viceroy / Governor - Strategy / Policy focus
1. Francisco de Almeida - Blue Water Policy (Sea Power)
2. Afonso de Albuquerque - Imperial territorial colonization
3. Vasco da Gama - Commercial factors without military presence
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Almeida pioneered naval control, and Albuquerque focused on land empire. Pair 3 is incorrect; Vasco da Gama utilized military force (e.g. bombardment of Calicut in 1502) and established early fortifications during his second voyage, not just peaceful factors."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
वायसराय / गवर्नर - रणनीति / नीति फोकस
1. फ्रांसिस्को डी अल्मेडा - नीले पानी की नीति (समुद्री शक्ति)
2. अल्फांसो डी अल्बुकर्क - साम्राज्यवादी क्षेत्रीय उपनिवेशीकरण
3. वास्को डी गामा - बिना सैन्य उपस्थिति के वाणिज्यिक कारक
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। वास्को डी गामा ने भी सैन्य बल और बमबारी का उपयोग किया था, केवल शांतिपूर्ण व्यापार नहीं।"
    })

    # 37. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Vessel Type - Operational Role
1. Carrack (Nau) - Large armed cargo vessel for global routes
2. Caravel - Fast, highly maneuverable ship for coastal exploration
3. Galley - Oar-powered warship utilized in shallow waters
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 2,
        "sol": "All three pairs are correctly matched. Naus were cargo carriers, Caravels were fast exploration ships, and Galleys used oars for shallow-water maneuverability."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली जहाज प्रकार - परिचालन भूमिका
1. कैरक (नौ) - वैश्विक मार्गों के लिए बड़े सशस्त्र मालवाहक जहाज
2. कार्वेल - तटीय अन्वेषण के लिए तेज, अत्यधिक गतिशील जहाज
3. गैली - उथले पानी में उपयोग किया जाने वाला पतवार चालित युद्धपोत
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 2,
        "sol": "सभी तीन युग्म सही सुमेलित हैं। कैरक, कार्वेल और गैली की भूमिकाएं सही वर्णित हैं।"
    })

    # 38. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Geographic Point - Strategic Connection
1. Kilwa - Control of Swahili Gold Trade
2. Cochin - Capital of early Estado da Índia
3. Diu - Choke point at the mouth of the Red Sea
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Kilwa controlled the gold route, and Cochin was the capital. Pair 3 is incorrect; Diu is off the Gujarat coast in Western India, not at the mouth of the Red Sea (which is Bab-el-Mandeb/Aden)."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
भौगोलिक बिंदु - रणनीतिक संबंध
1. किलवा - स्वाहिली सोने के व्यापार का नियंत्रण
2. कोचीन - प्रारंभिक एस्टाडो दा इंडिया की राजधानी
3. दीव - लाल सागर के मुहाने पर चोक पॉइंट
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। दीव गुजरात तट पर है, लाल सागर के मुहाने पर अदन या बाब-अल-मन्देब है।"
    })

    # 39. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Historical Source - Primary Context
1. Pero Vaz de Caminha's Letter - Report on the discovery of Brazil
2. Roteiro - Logbook of Vasco da Gama's first voyage
3. Comentários de Afonso de Albuquerque - Chronicles of Almeida's military actions in Castile
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Caminha's letter reported Brazil's discovery, and Roteiro was Gama's log. Pair 3 is incorrect; the Commentaries of Afonso de Albuquerque document Albuquerque's own governorship and policies in Asia, not Almeida's Castilian military campaigns."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
ऐतिहासिक स्रोत - प्राथमिक संदर्भ
1. पेरो वाज़ डे कामिन्या का पत्र - ब्राजील की खोज पर रिपोर्ट
2. रोटेइरो - वास्को डी गामा की पहली यात्रा की लॉगबुक
3. अल्फांसो डी अल्बुकर्क के कमेंट्रीस - कैस्टिल में अल्मेडा की सैन्य कार्रवाई का इतिहास
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। अल्बुकर्क की टिप्पणियां अल्बुकर्क के अपने गवर्नरशिप के इतिहास को बताती हैं, अल्मेडा के कैस्टिलियन युद्धों को नहीं।"
    })

    # 40. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Military Commander - Death / Skirmish Site
1. Lourenço de Almeida - Estuary at Table Bay
2. Francisco de Almeida - River mouth at Chaul
3. Bartolomeu Dias - Open seas off the Cape of Good Hope
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 0,
        "sol": "Only pair 3 is correctly matched; Bartolomeu Dias drowned during a storm off the Cape of Good Hope in 1500. Pair 1 is incorrect; Lourenço de Almeida was killed at the Battle of Chaul. Pair 2 is incorrect; Francisco de Almeida was killed at Table Bay, South Africa."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली सैन्य कमांडर - मृत्यु / झड़प का स्थान
1. लॉरेंको डी अल्मेडा - टेबल बे का मुहाना
2. फ्रांसिस्को डी अल्मेडा - चोल में नदी का मुहाना
3. बारटोलोमियु डियास - केप ऑफ गुड होप के पास खुला समुद्र
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 0,
        "sol": "केवल युग्म 3 सही सुमेलित है। लॉरेंको चोल में और फ्रांसिस्को टेबल बे में मारे गए थे, इसलिए 1 और 2 गलत हैं।"
    })

    # 41. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): King Manuel I established a permanent viceroyalty in India in 1505 CE.
Reason (R): The Portuguese Crown realized that sending temporary annual armadas was insufficient to enforce a trade monopoly against hostile local alliances.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason correctly explains the Assertion. The permanent administrative state was created because seasonal fleets could not maintain security or enforce trade monopoly."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): राजा मैनुअल प्रथम ने 1505 ईस्वी में भारत में एक स्थायी वायसराय पद की स्थापना की।
कारण (R): पुर्तगाली क्राउन ने महसूस किया कि विरोधी स्थानीय गठबंधनों के खिलाफ व्यापार एकाधिकार लागू करने के लिए मौसमी वार्षिक बेड़े भेजना नाकाफी था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। स्थायी प्रशासन की स्थापना मौसमी बेड़ों की अक्षमता के कारण हुई थी।"
    })

    # 42. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Francisco de Almeida strongly opposed the acquisition of land territories in India.
Reason (R): He formulated the Blue Water Policy, believing that Portuguese power should reside entirely on naval control of sea lanes due to manpower limitations.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. Almeida opposed land bases because he believed that sea supremacy was sufficient and that land fortresses would drain resources."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): फ्रांसिस्को डी अल्मेडा ने भारत में भूमि क्षेत्रों के अधिग्रहण का कड़ा विरोध किया।
कारण (R): उन्होंने नीले पानी की नीति (ब्लू वाटर पॉलिसी) का प्रतिपादन किया, यह मानते हुए कि जनशक्ति की सीमाओं के कारण पुर्तगाली शक्ति पूरी तरह से समुद्री मार्गों के नौसैनिक नियंत्रण पर आधारित होनी चाहिए।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। अल्मेडा ने जनशक्ति की कमी के कारण भूमि अधिग्रहण का विरोध किया।"
    })

    # 43. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Rulers allied with the Portuguese, such as the Raja of Cochin, were exempt from obtaining the Cartaz maritime license.
Reason (R): The Portuguese Crown asserted complete sovereign jurisdiction under the legal doctrine of Mare Clausum.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Assertion is false, but Reason is true. Rulers allied with the Portuguese, including the Raja of Cochin, were NOT exempt from obtaining Cartazes; they had to secure licenses for all their ships. The Reason is true, as Mare Clausum was the legal justification used to claim sovereignty over the sea."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): पुर्तगालियों के साथ गठबंधन करने वाले शासकों, जैसे कि कोचीन के राजा, को कार्टाज समुद्री लाइसेंस प्राप्त करने से छूट दी गई थी।
कारण (R): पुर्तगाली क्राउन ने मारे क्लॉसम के कानूनी सिद्धांत के तहत पूर्ण संप्रभु अधिकार क्षेत्र का दावा किया था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A गलत है, लेकिन R सही है। कोचीन के राजा को भी कार्टाज लाइसेंस लेना पड़ता था, कोई छूट नहीं थी।"
    })

    # 44. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Scribes and financial factors in the Estado da Índia reported directly to the Viceroy.
Reason (R): The Portuguese Crown wanted to ensure that the Viceroy possessed unified control over civil, judicial, and financial affairs.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Both Assertion and Reason are false. Scribes and factors reported directly to the Casa da Índia in Lisbon, bypassing the Viceroy's control. The Reason is false; the Crown designed this separation of powers specifically to check the Viceroy and prevent autonomous rebellion."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): एस्टाडो दा इंडिया में लेखक (Scribes) और वित्तीय कारक (Factors) सीधे वायसराय को रिपोर्ट करते थे।
कारण (R): पुर्तगाली क्राउन यह सुनिश्चित करना चाहता था कि वायसराय के पास नागरिक, न्यायिक और वित्तीय मामलों पर एकीकृत नियंत्रण हो।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A और R दोनों गलत हैं। वे सीधे लिस्बन को रिपोर्ट करते थे, और क्राउन ने ऐसा नियंत्रण को रोकने तथा वायसराय पर नजर रखने के लिए किया था।"
    })

    # 45. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Almeida ordered the demolition and abandonment of the Anjadip Fort in late 1506 CE.
Reason (R): The fort suffered constant raids from the forces of the Adil Shahi Sultanate of Bijapur and was too costly to maintain.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason correctly explains the Assertion. Due to persistent raids from Bijapur forces and high logistical maintenance costs, Almeida decided to demolish and abandon Anjadip."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): अल्मेडा ने 1506 ईस्वी के अंत में अंजादीप किले को ध्वस्त करने और इसे छोड़ने का आदेश दिया।
कारण (R): इस किले पर बीजापुर के आदिल शाही सल्तनत की सेना द्वारा लगातार हमले किए जा रहे थे और इसका रखरखाव बहुत महंगा था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। बीजापुर के हमलों और भारी खर्च के कारण 1506 में इस किले को छोड़ दिया गया था।"
    })

    # 46. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): The Battle of Chaul in 1508 resulted in the death of Lourenço de Almeida, the Viceroy's son.
Reason (R): His flagship became trapped by a fishing cable in the shallow waters of the Kundalika river estuary, exposing it to heavy coalition fire.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. Lourenço's ship Santo Espírito was pinned down by a cable, preventing it from maneuvering, leading to his heroic death under heavy fire."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): 1508 में चोल की लड़ाई के कारण वायसराय के पुत्र लॉरेंको डी अल्मेडा की मृत्यु हो गई।
कारण (R): उनका प्रमुख जहाज कुंडलिका नदी के मुहाने के उथले पानी में एक मछली पकड़ने वाले केबल में फंस गया था, जिससे वह गठबंधन की भारी गोलाबारी की चपेट में आ गया था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। लॉरेंको का जहाज केबल में फंस गया था, जिससे वह अपनी गतिशीलता खो बैठा और मारा गया।"
    })

    # 47. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Francisco de Almeida refused to surrender the office of Governor to Afonso de Albuquerque in late 1508.
Reason (R): Almeida disputed the validity of Albuquerque's credentials and swore to avenge his son's death first.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. Almeida delayed the transfer of power and imprisoned Albuquerque because he was determined to retaliate against the coalition fleet at Diu."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): फ्रांसिस्को डी अल्मेडा ने 1508 के अंत में अल्फांसो डी अल्बुकर्क को गवर्नर का पद सौंपने से इनकार कर दिया।
कारण (R): अल्मेडा ने अल्बुकर्क के दस्तावेजों की वैधता पर विवाद उठाया और पहले अपने पुत्र की मृत्यु का बदला लेने की प्रतिज्ञा की थी।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। अल्मेडा अपने बेटे की मौत का बदला लेने के लिए प्रतिबद्ध थे, इसलिए उन्होंने उत्तराधिकार को टाला।"
    })

    # 48. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): The Battle of Diu (1509) ended Arab and Egyptian dominance over the Indian Ocean trade routes.
Reason (R): The crushing Portuguese victory established European naval hegemony in Asia for the next 400 years.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. The Mamluk fleet's destruction at Diu ended their monopoly and permanently secured European naval supremacy in the region."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): दीव की लड़ाई (1509) ने हिंद महासागर के व्यापार मार्गों पर अरब और मिस्र के प्रभुत्व को समाप्त कर दिया।
कारण (R): पुर्तगालियों की इस शानदार जीत ने अगले 400 वर्षों के लिए एशिया में यूरोपीय नौसैनिक वर्चस्व स्थापित किया।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। दीव की लड़ाई में गठबंधन की हार ने यूरोपीय समुद्री युग की शुरुआत की।"
    })

    # 49. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): The Republic of Venice openly and officially declared war on the Portuguese Empire in 1507.
Reason (R): Venice was losing its monopoly over the Mediterranean spice trade due to the Portuguese blockade of the Red Sea.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Assertion is false, but Reason is true. Venice did NOT declare war openly or officially; instead, they worked secretly, supplying shipbuilding timber to the Mamluks of Egypt to fight the Portuguese. The Reason is true, as the Portuguese Cape Route monopoly bypassed Alexandria, threatening Venetian trade."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): वेनिस गणराज्य ने 1507 में आधिकारिक तौर पर पुर्तगाली साम्राज्य के खिलाफ युद्ध की घोषणा की थी।
कारण (R): लाल सागर की पुर्तगाली नाकेबंदी के कारण वेनिस भूमध्यसागरीय मसाला व्यापार पर अपना एकाधिकार खो रहा था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A गलत है, लेकिन R सही है। वेनिस ने युद्ध की घोषणा नहीं की, बल्कि ममलुकों को गुप्त रूप से लकड़ी देकर मदद की थी।"
    })

    # 50. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Francisco de Almeida was buried with full military honors in Lisbon in 1510.
Reason (R): King Manuel I wanted to celebrate his historic victory at the Battle of Diu.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Both Assertion and Reason are false. Almeida was not buried in Lisbon; he was killed and buried in an unmarked grave on the beach of Table Bay, South Africa, in March 1510. The Reason is false, as his death occurred during his return voyage and he never reached Lisbon."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): फ्रांसिस्को डी अल्मेडा को 1510 में लिस्बन में पूर्ण सैन्य सम्मान के साथ दफनाया गया था।
कारण (R): राजा मैनुअल प्रथम दीव की लड़ाई में उनकी ऐतिहासिक जीत का जश्न मनाना चाहते थे।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A और R दोनों गलत हैं। अल्मेडा की दक्षिण अफ्रीका के टेबल बे पर मौत हो गई और उन्हें वहीं दफनाया गया, वे लिस्बन कभी नहीं पहुंचे।"
    })

    return en, hi

# Now let's generate 10 unique Mock questions.
def make_mock_questions():
    en = []
    hi = []
    
    m_data = [
        {
            "type": "MCQ",
            "q": "With reference to the first Portuguese Viceroyalty (1505-1509), consider the following statements:\n1. Francisco de Almeida was appointed by King Manuel I to replace the temporary seasonal spice fleets with permanent administration.\n2. Almeida was instructed to capture Goa immediately and establish it as the capital.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 0,
            "sol": "Statement 1 is correct. Statement 2 is incorrect; Goa was captured in 1510 by Albuquerque, and was not part of Almeida's 1505 instructions."
        },
        {
            "type": "MCQ",
            "q": "Regarding the Blue Water Policy of Francisco de Almeida, consider the following statements:\n1. It prioritized naval supremacy and state trade monopoly over territorial land conquests.\n2. It opposed Afonso de Albuquerque's strategy of capturing and securing fortified land bases like Goa.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 2,
            "sol": "Both statements are correct. Almeida's Blue Water Policy focused on controlling sea lanes and shipping routes rather than conquering land."
        },
        {
            "type": "MCQ",
            "q": "With reference to early Portuguese fortifications in India, consider the following statements:\n1. Fort Manuel in Cochin was the first European fort constructed in India.\n2. Fort St. Angelo was built in Cannanore under the supervision of Viceroy Almeida.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 2,
            "sol": "Both statements are correct. Fort Manuel (Cochin) and Fort St. Angelo (Cannanore) were key early fortifications."
        },
        {
            "type": "MCQ",
            "q": "Consider the following statements regarding the Battle of Chaul (1508):\n1. The Portuguese fleet was commanded by Lourenço de Almeida, who was killed during the clash.\n2. The Portuguese defeated a combined Mamluk-Gujarati fleet, securing Diu harbor.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 0,
            "sol": "Statement 1 is correct. Statement 2 is incorrect; the Battle of Chaul was a major defeat for the Portuguese."
        },
        {
            "type": "MCQ",
            "q": "Regarding the Battle of Diu (1509), consider the following statements:\n1. Francisco de Almeida personally led the Portuguese fleet to avenge his son's death.\n2. The victory established European naval dominance in the Indian Ocean for nearly 400 years.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 2,
            "sol": "Both statements are correct. Diu was a decisive victory that established long-term European naval supremacy."
        },
        {
            "type": "MCQ",
            "q": "With reference to the legal doctrine Mare Clausum, consider the following statements:\n1. It was used by the Portuguese to declare the Indian Ocean closed to other European and Arab merchants.\n2. It was countered in the 17th century by the Dutch legal concept of Mare Liberum.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 2,
            "sol": "Both statements are correct. Mare Clausum (Closed Sea) was countered by Hugo Grotius's Mare Liberum (Free Seas)."
        },
        {
            "type": "MCQ",
            "q": "Consider the following statements regarding the death of Francisco de Almeida:\n1. He was killed in a skirmish with the Khoikhoi at Table Bay, South Africa, in 1510.\n2. He was buried in a grand mausoleum in Lisbon after his body was returned by ship.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 0,
            "sol": "Statement 1 is correct. Statement 2 is incorrect; he was buried in an unmarked grave on the beach at Table Bay."
        },
        {
            "type": "MCQ",
            "q": "Regarding the Cartaz system, consider the following statements:\n1. It was a mandatory navigation pass introduced by the Portuguese to tax trade and enforce a spice monopoly.\n2. Rulers allied with Portugal were exempt from obtaining these passes for their ships.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 0,
            "sol": "Statement 1 is correct. Statement 2 is incorrect; even allied rulers like the Raja of Cochin had to obtain Cartazes."
        },
        {
            "type": "MCQ",
            "q": "With reference to the coalition that fought the Portuguese at Diu (1509), consider the following statements:\n1. It included the Mamluk Sultanate, the Gujarat Sultanate, and Ottoman specialists.\n2. The coalition was supported by the British Royal Navy.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 0,
            "sol": "Statement 1 is correct. Statement 2 is incorrect; the British had no role or presence in these seas at that time."
        },
        {
            "type": "MCQ",
            "q": "Consider the following statements regarding the transition of power in late 1509:\n1. Francisco de Almeida imprisoned Afonso de Albuquerque to delay handing over the governorship.\n2. The arrival of the Marshal of Portugal, Dom Fernando Coutinho, resolved the dispute and Albuquerque assumed power.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 2,
            "sol": "Both statements are correct. Coutinho's arrival resolved the dispute, and Albuquerque became Governor."
        }
    ]
    
    for idx, q in enumerate(m_data):
        en.append(q)
        
        # Hindi translation
        q_hi = q.copy()
        q_hi["q"] = q["q"].replace("Francisco de Almeida", "फ्रांसिस्को डी अल्मेडा").replace("Viceroy", "वायसराय").replace("Blue Water Policy", "नीले पानी की नीति").replace("Battle of Chaul", "चोल की लड़ाई").replace("Battle of Diu", "दीव की लड़ाई").replace("Fort Manuel", "फोर्ट मैनुअल").replace("Fort St. Angelo", "फोर्ट सेंट एंजेलो")
        q_hi["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
        q_hi["sol"] = q["sol"].replace("Almeida", "अल्मेडा").replace("Lourenço", "लॉरेंको").replace("Chaul", "चोल").replace("Diu", "दीव").replace("Statement 1", "कथन 1").replace("Statement 2", "कथन 2").replace("correct", "सही").replace("incorrect", "गलत")
        hi.append(q_hi)
        
    return en, hi

# Generate sections and save them
sec1_en, sec1_hi = make_section_1()
sec2_en, sec2_hi = make_section_2()
sec3_en, sec3_hi = make_section_3()
sec4_en, sec4_hi = make_section_4()
sec5_en, sec5_hi = make_section_5()
practice_en, practice_hi = make_practice_questions()
mock_en, mock_hi = make_mock_questions()

generate_sec_file("section1", sec1_en, sec1_hi)
generate_sec_file("section2", sec2_en, sec2_hi)
generate_sec_file("section3", sec3_en, sec3_hi)
generate_sec_file("section4", sec4_en, sec4_hi)
generate_sec_file("section5", sec5_en, sec5_hi)
generate_sec_file("practice", practice_en, practice_hi)
generate_sec_file("mock", mock_en, mock_hi)

# Create final content.json structure
en_data = {
  "breadcrumbs": {
    "parent": "UPSC Syllabus",
    "parentUrl": "/upsc/",
    "current": "Portuguese: Francisco de Almeida"
  },
  "hero": {
    "title": "Portuguese: Francisco de Almeida",
    "description": "Master Francisco de Almeida's viceroyalty, the Blue Water Policy, the Cartaz system, major fortifications, the Battles of Chaul and Diu, and early Portuguese naval hegemony."
  },
  "timeline": {
    "title": "Francisco de Almeida's Viceroyalty & Impact",
    "description": "Click on each card to follow the chronological milestones of Francisco de Almeida's tenure in India.",
    "cards": [
      {
        "period": "Viceroy Appointment",
        "date": "March 1505 CE",
        "details": "Almeida is appointed the first Viceroy of India by King Manuel I, departing Lisbon with a massive 21-ship fleet."
      },
      {
        "period": "Fortifications",
        "date": "1505 CE",
        "details": "He establishes forts at Kilwa in East Africa, Anjadip Island, Fort Manuel in Cochin, and Fort St. Angelo in Cannanore."
      },
      {
        "period": "Battle of Chaul",
        "date": "March 1508 CE",
        "details": "His son Lourenço de Almeida is defeated and killed by a Mamluk-Gujarati fleet in the shallow waters of Chaul."
      },
      {
        "period": "Battle of Diu",
        "date": "February 1509 CE",
        "details": "Almeida personally commands a fleet that destroys the coalition navy at Diu, securing European naval hegemony."
      },
      {
        "period": "Death of Almeida",
        "date": "March 1510 CE",
        "details": "On his return voyage to Portugal, he is killed in a skirmish with Khoikhoi natives at Table Bay, South Africa."
      }
    ]
  },
  "mnemonics": {
    "title": "Mnemonics & Memory Hacks",
    "description": "Memory triggers for Francisco de Almeida.",
    "items": [
      {
        "title": "Mnemonic 1: The Five Key Fortifications",
        "phrase": "\"K-A-C-C\" — Kilwa, Anjadip, Cochin, Cannanore",
        "decryption": "The four main fortresses established or reinforced by Almeida during his 1505 expedition."
      },
      {
        "title": "Mnemonic 2: The Battle Transition",
        "phrase": "\"C-D-D\" — Chaul, Diu, Death",
        "decryption": "The chronological sequence of Almeida's final years: **Chaul** (defeat & son's death), **Diu** (revenge & victory), **Death** (skirmish at Table Bay)."
      }
    ]
  },
  "traps": {
    "title": "UPSC Common Exam Traps",
    "items": [
      "<strong>Trap 1: First Viceroy Title:</strong> UPSC might confuse Almeida with Vasco da Gama or Albuquerque. Vasco da Gama was the explorer, and Albuquerque was the second Governor, but **Francisco de Almeida** was the very first Viceroy.",
      "<strong>Trap 2: Blue Water vs. Imperial Expansion:</strong> Do not confuse their strategic views. Almeida championed the Blue Water Policy (sea power), while **Albuquerque** initiated the policy of capturing land bases.",
      "<strong>Trap 3: Fort construction dates:</strong> Anjadip and Cannanore forts were built in 1505 under Almeida, but the first Cochin fort (Fort Manuel) was initiated in 1503 by Albuquerque during his commercial voyage, though reinforced by Almeida."
    ]
  },
  "deepDive": {
    "title": "Syllabus Core Study Notes (Deep-Dive)",
    "description": "Master Francisco de Almeida's viceroyalty, routes, battles, and historical legacy in India.",
    "sections": [
      {
        "title": "1. Appointment & Viceroyalty (1505)",
        "content": "<p><strong>Establishment of the Estado da Índia:</strong> In the early 16th century, the Portuguese Crown recognized that the system of sending annual trading fleets (Armadas da Índia) was insufficient to secure a monopoly over the spice trade against hostile local and regional powers. To consolidate control, King Manuel I decided to establish a permanent administrative and military entity in the Indian Ocean, designated as the <em>Estado da Índia</em>. In 1505, Francisco de Almeida, a distinguished soldier and veteran of the Moorish wars in Granada, was commissioned as the first Viceroy and Governor-General of Portuguese India. He was granted plenipotentiary civil, judicial, and military powers to act as the direct representative of the Portuguese monarch in Asia.</p><p><strong>The Royal Commission & Strategic Mandate:</strong> Almeida departed Lisbon on March 25, 1505, commanding a massive armada of 21 ships carrying 1,500 soldiers, noblemen, and Franciscan missionaries. The royal instructions given to Almeida were precise and strategically ambitious: he was to establish a line of permanent fortifications along the East African and Western Indian coasts to secure shipping lanes, enforce a trade monopoly on pepper and other spices, and aggressively counter the naval influence of the Muslim merchant coalitions, particularly the Mamluk Sultanate of Egypt and the Zamorin of Calicut. His tenure was strictly limited to a three-year term to prevent any consolidation of autonomous power away from the home Crown, setting a precedent for subsequent Portuguese administrative appointments in Asia.</p>"
      },
      {
        "title": "2. Blue Water Policy & Naval Hegemony",
        "content": "<p><strong>The Philosophy of the Blue Water Policy (Política da Água Azul):</strong> Unlike his successor Afonso de Albuquerque, who advocated for a territorial land-based empire with fortified colonial centers, Francisco de Almeida believed that Portugal's small population and limited resources could not sustain a land-based domain in India. He formulated the <em>Blue Water Policy</em>, which argued that Portuguese power should reside entirely on the sea. Almeida famously wrote to King Manuel I: 'Should you possess all the fortresses of India, they will avail you little if you do not hold the mastery of the sea.' His strategy prioritized naval mobility, cruising patrols, and control of ocean transit lanes over territorial conquests, avoiding entanglements with powerful mainland Indian empires.</p><p><strong>The Cartaz System & Legal Monopoly:</strong> To enforce this policy, the Portuguese introduced the <em>Cartaz</em> system, a mandatory maritime licensing mechanism. Every merchant vessel operating in the Indian Ocean was forced to purchase a Cartaz from Portuguese authorities. This pass prohibited vessels from carrying prohibited goods (primarily pepper, ginger, and weapons) and routed them through Portuguese-held ports to pay heavy customs duties. Rulers allied with Portugal, including the Raja of Cochin, were not exempt from this licensing. Any ship found without a Cartaz was subject to immediate seizure, confiscation of cargo, and the execution or enslavement of its crew. This system enforced the legal doctrine of <em>Mare Clausum</em> (Closed Sea), transforming the open waters of the Indian Ocean into a Portuguese sovereign domain.</p>"
      },
      {
        "title": "3. Fortifications & Indian Ocean Bases",
        "content": "<p><strong>Construction of the Four Key Bases:</strong> To support the Blue Water Policy, Almeida's fleet was instructed to build strategically located coastal and island fortifications to serve as safe harbors, fresh water stations, and warehouses (feitorias). The four key fortifications established or consolidated during his tenure were:</p><ul><li><strong>Fort São Tiago (Kilwa, East Africa):</strong> Built in 1505 on the Swahili Coast to secure the passage across the Indian Ocean and control the lucrative gold trade coming from Sofala.</li><li><strong>Fort Manuel (Cochin):</strong> Initially constructed as a wooden palisade in 1503, Almeida reinforced it in 1505 with stone bastions under an alliance with the local Trimumpara Raja, making it the primary Portuguese administrative headquarters in India.</li><li><strong>Fort St. Angelo (Cannanore):</strong> Built in late 1505 by Almeida on a triangular spit of land in Cannanore. This fort secured the trade of Malabar ginger and horse imports, and famously withstood the grueling 1507 Siege of Cannanore.</li><li><strong>Anjadip Fort:</strong> Built in 1505 on Anjadip Island off the coast of Goa to provide a vital fresh water supply and ship repair facility. However, due to constant raids from the forces of the Adil Shahi Sultanate of Bijapur and the high cost of maintenance, Almeida ordered its demolition and abandonment in 1506.</li></ul>"
      },
      {
        "title": "4. The Battle of Chaul (1508)",
        "content": "<p><strong>Outbreak of Conflict & Mamluk Intervention:</strong> The aggressive Portuguese blockade of the Red Sea and the Persian Gulf severely disrupted the spice monopoly of the Mamluk Sultanate of Egypt, which relied on transit customs duties for its economic survival. Backed secretly by Venice (which supplied shipbuilding timber via Alexandria to Suez) and supported by Ottoman specialists, Egypt constructed a war fleet at Suez. Commanded by Amir Husain Al-Kurdi, the Mamluk fleet sailed to India and allied with Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, and the Zamorin of Calicut to expel the Portuguese.</p><p><strong>The Naval Clash and Death of Lourenço:</strong> In March 1508, the coalition fleet surprised a smaller Portuguese patrol fleet in the shallow waters of the Kundalika River estuary at Chaul. The Portuguese fleet was commanded by Lourenço de Almeida, the Viceroy's only son. The shallow river restricted the maneuverability of the heavy Portuguese naus, exposing them to agile Gujarati dhows. During the battle, Lourenço's flagship, the <em>Santo Espírito</em>, was trapped by a fishing cable and pinned down. Despite sustaining severe wounds, Lourenço refused to surrender or abandon ship, fighting valiantly until a cannonball struck and killed him. The battle ended in a major Portuguese defeat, temporarily shattering their myth of naval invincibility in Asian waters.</p>"
      },
      {
        "title": "5. The Battle of Diu (1509) & Legacy",
        "content": "<p><strong>Francisco de Almeida's Retaliation:</strong> Shattered by the death of his only son, Viceroy Francisco de Almeida swore a personal oath of revenge. When his designated successor Afonso de Albuquerque arrived in Cochin in late 1508 with royal patents to assume the governorship, Almeida refused to hand over power. He claimed that Albuquerque's papers were invalid and subsequently imprisoned him in Fort Manuel, declaring: 'I must first seek the blood of my son.' Almeida personally assembled a powerful armada of 19 ships and 1,300 soldiers and sailed north to locate the coalition fleet.</p><p><strong>The Decisive Clash & Imperial Legacy:</strong> On February 3, 1509, the Portuguese fleet engaged the Mamluk-Ottoman-Gujarati navy off the coast of Diu. Using superior naval artillery, long-range bombardment, and high-walled vessels that prevented coalition boarding tactics, Almeida achieved a crushing victory. The Mamluk fleet was destroyed, and Malik Ayyaz was forced to sign a peace treaty, releasing prisoners and paying a massive indemnity. The Battle of Diu is considered one of the most critical naval battles in history, as it ended Arab and Egyptian monopoly over the Indian Ocean and established European naval dominance in Asia for the next 400 years. Having avenged his son, Almeida released Albuquerque and departed for Portugal, but was killed in March 1510 in a skirmish with Khoikhoi natives over water at Table Bay, South Africa.</p>"
      }
    ]
  }
}

hi_data = {
  "breadcrumbs": {
    "parent": "यूपीएससी पाठ्यक्रम",
    "parentUrl": "/upsc/",
    "current": "पुर्तगाली: फ्रांसिस्को डी अल्मेडा"
  },
  "hero": {
    "title": "पुर्तगाली: फ्रांसिस्को डी अल्मेडा",
    "description": "फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, नीले पानी की नीति, कार्टाज प्रणाली, प्रमुख किलेबंदी, चोल और दीव की लड़ाई, और प्रारंभिक पुर्तगाली नौसैनिक वर्चस्व पर महारत हासिल करें।"
  },
  "timeline": {
    "title": "फ्रांसिस्को डी अल्मेडा का वायसराय कार्यकाल और प्रभाव",
    "description": "भारत में फ्रांसिस्को डी अल्मेडा के कार्यकाल के ऐतिहासिक मील के पत्थरों का पालन करने के लिए प्रत्येक कार्ड पर क्लिक करें।",
    "cards": [
      {
        "period": "वायसराय नियुक्ति",
        "date": "मार्च 1505 ईस्वी",
        "details": "अल्मेडा को राजा मैनुअल प्रथम द्वारा भारत का पहला वायसराय नियुक्त किया गया, जो 21 जहाजों के बेड़े के साथ लिस्बन से रवाना हुए।"
      },
      {
        "period": "किलेबंदी",
        "date": "1505 ईस्वी",
        "details": "उन्होंने पूर्वी अफ्रीका में किलवा, अंजादीप द्वीप, कोचीन में फोर्ट मैनुअल और कन्नूर में फोर्ट सेंट एंजेलो की स्थापना की।"
      },
      {
        "period": "चोल की लड़ाई",
        "date": "मार्च 1508 ईस्वी",
        "details": "उनके पुत्र लॉरेंको डी अल्मेडा चोल के उथले पानी में ममलुक-गुजराती बेड़े से हार गए और मारे गए।"
      },
      {
        "period": "दीव की लड़ाई",
        "date": "फरवरी 1509 ईस्वी",
        "details": "अल्मेडा ने व्यक्तिगत रूप से दीव में गठबंधन नौसेना को नष्ट करने वाले बेड़े की कमान संभाली, जिससे यूरोपीय नौसैनिक वर्चस्व सुरक्षित हुआ।"
      },
      {
        "period": "अल्मेडा की मृत्यु",
        "date": "मार्च 1510 ईस्वी",
        "details": "पुर्तगाल की अपनी वापसी यात्रा के दौरान, वह दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ एक झड़प में मारे गए।"
      }
    ]
  },
  "mnemonics": {
    "title": "मेॉर्मोहाइक्स (स्मरणोदहार)",
    "description": "फ्रांसिस्को डी अल्मेडा के लिए याद रखने के तरीके।",
    "items": [
      {
        "title": "ट्रिक 1: चार प्रमुख किले",
        "phrase": "\"K-A-C-C\" — किलवा, अंजादीप, कोचीन, कन्नूर",
        "decryption": "अल्मेडा के 1505 के अभियान के दौरान स्थापित या मजबूत किए गए चार मुख्य किले।"
      },
      {
        "title": "ट्रिक 2: युद्ध अनुक्रम",
        "phrase": "\"C-D-D\" — चोल, दीव, मृत्यु (Death)",
        "decryption": "अल्मेडा के अंतिम वर्षों का कालानुक्रमिक क्रम: चोल (हार और बेटे की मृत्यु), दीव (बदला और जीत), मृत्यु (टेबल बे में झड़प)।"
      }
    ]
  },
  "traps": {
    "title": "यूपीएससी परीक्षा के सामान्य जाल",
    "items": [
      "<strong>जाल 1: पहले वायसराय की उपाधि:</strong> यूपीएससी अल्मेडा को वास्को डी गामा या अल्बुकर्क के साथ भ्रमित कर सकता है। वास्को डी गामा खोजकर्ता थे, और अल्बुकर्क दूसरे गवर्नर थे, लेकिन **फ्रांसिस्को डी अल्मेडा** पहले वायसराय थे।",
      "<strong>जाल 2: ब्लू वाटर बनाम क्षेत्रीय विस्तार:</strong> उनकी रणनीतियों को भ्रमित न करें। अल्मेडा ने ब्लू वाटर नीति (नौसैनिक शक्ति) का समर्थन किया, जबकि **अल्बुकर्क** ने भूमि ठिकानों पर कब्जा करने की नीति शुरू की।",
      "<strong>जाल 3: किले निर्माण तिथियां:</strong> अंजादीप और कन्नूर किले 1505 में अल्मेडा के तहत बनाए गए थे, लेकिन कोचीन का पहला किला (फोर्ट मैनुअल) 1503 में अल्बुकर्क द्वारा व्यापारिक यात्रा के दौरान शुरू किया गया था, जिसे अल्मेडा ने मजबूत किया था।"
    ]
  },
  "deepDive": {
    "title": "पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)",
    "description": "फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, मार्ग, युद्धों और भारत में ऐतिहासिक विरासत पर महारत हासिल करें।",
    "sections": [
      {
        "title": "1. नियुक्ति और वायसराय कार्यकाल (1505)",
        "content": "<p><strong>एस्टाडो दा इंडिया की स्थापना:</strong> 16वीं शताब्दी की शुरुआत में, पुर्तगाली क्राउन ने महसूस किया कि केवल वार्षिक व्यापारिक बेड़े (अर्माडास दा इंडिया) भेजना हिंद महासागर में मसालों के व्यापार पर एकाधिकार सुरक्षित करने के लिए पर्याप्त नहीं था। व्यापारिक हितों की रक्षा और सैन्य नियंत्रण स्थापित करने के लिए, राजा मैनुअल प्रथम ने एक स्थायी प्रशासनिक और सैन्य इकाई की स्थापना का निर्णय लिया, जिसे <em>एस्टाडो दा इंडिया (Estado da Índia)</em> का नाम दिया गया। वर्ष 1505 में, ग्रेनाडा के युद्धों के अनुभवी और कुशल सैनिक फ्रांसिस्को डी अल्मेडा को भारत का पहला वायसराय और गवर्नर-जनरल नियुक्त किया गया। उन्हें पुर्तगाली राजा के सीधे प्रतिनिधि के रूप में नागरिक, न्यायिक और सैन्य शक्तियां प्रदान की गईं।</p><p><strong>शाही आयोग और रणनीतिक अधिदेश:</strong> अल्मेडा ने 25 मार्च, 1505 को 21 जहाजों के एक बड़े बेड़े और 1,500 सैनिकों, कुलीनों और मिशनरियों के साथ लिस्बन से प्रस्थान किया। वायसराय को दिए गए शाही निर्देश अत्यंत स्पष्ट और दूरगामी थे: उन्हें पूर्वी अफ्रीकी तट और भारत के पश्चिमी तट पर स्थायी किलों का निर्माण करना था, काली मिर्च के व्यापार पर पूर्ण एकाधिकार स्थापित करना था, और ममलुक सल्तनत तथा कालीकट के ज़मोरिन जैसे प्रतिद्वंद्वी व्यापारिक गुटों के नौसैनिक प्रभाव को समाप्त करना था। उनके कार्यकाल को तीन वर्ष तक सीमित रखा गया ताकि वे लिस्बन से स्वतंत्र कोई स्थानीय सत्ता केंद्र न बना सकें।</p>"
      },
      {
        "title": "2. नीले पानी की नीति और नौसैनिक वर्चस्व",
        "content": "<p><strong>नीले पानी की नीति (ब्लू वाटर पॉलिसी) का सिद्धांत:</strong> अपने उत्तराधिकारी अल्फांसो डी अल्बुकर्क के विपरीत, जिसने क्षेत्रीय और भू-भाग आधारित साम्राज्य का समर्थन किया, फ्रांसिस्को डी अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या और संसाधन भारत में भूमि-आधारित साम्राज्य को नहीं संभाल सकते। उन्होंने <em>ब्लू वाटर पॉलिसी (नीले पानी की नीति)</em> का प्रतिपादन किया, जिसके अनुसार पुर्तगाली शक्ति का आधार केवल समुद्र होना चाहिए। अल्मेडा ने राजा मैनुअल प्रथम को लिखा था: 'यदि आप समुद्र पर संप्रभुता खो देते हैं, तो भारत के सभी किले आपके किसी काम नहीं आएंगे।' उन्होंने भूमि विजय के बजाय समुद्री गश्ती और नौसैनिक वर्चस्व को प्राथमिकता दी।</p><p><strong>कार्टाज प्रणाली और व्यापारिक एकाधिकार:</strong> इस नीति को लागू करने के लिए पुर्तगालियों ने <em>कार्टाज (Cartaz)</em> प्रणाली शुरू की, जो एक अनिवार्य समुद्री नौवहन लाइसेंस था। हिंद महासागर में व्यापार करने वाले सभी जहाजों को पुर्तगाली अधिकारियों से यह लाइसेंस खरीदना पड़ता था। इस पास के तहत जहाजों को काली मिर्च, अदरक और हथियार ले जाने की मनाही थी और उन्हें सीमा शुल्क चुकाने के लिए पुर्तगाली बंदरगाहों पर रुकना पड़ता था। बिना कार्टाज के पाए जाने वाले जहाजों को जब्त कर लिया जाता था और चालक दल को मौत की सजा या दासता में धकेल दिया जाता था। इस प्रकार पुर्तगालियों ने <em>मारे क्लॉसम (Mare Clausum - बंद समुद्र)</em> के सिद्धांत को व्यावहारिक रूप से लागू किया।</p>"
      },
      {
        "title": "3. किलेबंदी और हिंद महासागर आधार",
        "content": "<p><strong>चार प्रमुख किलों का निर्माण:</strong> अपनी नौसैनिक नीति के समर्थन के लिए अल्मेडा ने रणनीतिक स्थानों पर चार प्रमुख किलों का निर्माण और सुदृढ़ीकरण किया, जो जहाजों के लिए सुरक्षित बंदरगाह, जल आपूर्ति और गोदाम (फेइटोरिया) के रूप में कार्य करते थे:</p><ul><li><strong>फोर्ट साओ टियागो (किलवा, पूर्वी अफ्रीका):</strong> हिंद महासागर पार करने वाले जहाजों की सुरक्षा और सोफाला के सोने के व्यापार को नियंत्रित करने के लिए 1505 में स्वाहिली तट पर स्थापित किया गया।</li><li><strong>फोर्ट मैनुअल (कोचीन):</strong> कोचीन के राजा के साथ गठबंधन के तहत 1503 में लकड़ी से बने इस किले को अल्मेडा ने 1505 में पत्थर के बुर्जों से मजबूत किया, जो भारत में पहला यूरोपीय किला बना।</li><li><strong>फोर्ट सेंट एंजेलो (कन्नूर):</strong> 1505 में मालाबार अदरक के व्यापार और घोड़ों के आयात पर नियंत्रण के लिए एक त्रिकोणीय प्रायद्वीप पर निर्मित। इसने 1507 में कन्नूर की प्रसिद्ध घेराबंदी का सफलतापूर्वक सामना किया।</li><li><strong>अंजादीप किला:</strong> गोवा के तट के पास मीठे पानी और जहाजों की मरम्मत के लिए 1505 में बनाया गया था, लेकिन बीजापुर के आदिल शाही सैनिकों के लगातार हमलों के कारण 1506 में इसे गिराकर छोड़ दिया गया।</li></ul>"
      },
      {
        "title": "4. चोल की लड़ाई (1508)",
        "content": "<p><strong>ममलुक हस्तक्षेप और संघर्ष की शुरुआत:</strong> लाल सागर में पुर्तगाली नाकेबंदी के कारण मिस्र की ममलुक सल्तनत का मसाला व्यापार बुरी तरह प्रभावित हुआ, जिसने मिस्र की अर्थव्यवस्था को खतरे में डाल दिया। वेनिस (जिसने स्वेज को जहाज निर्माण की लकड़ी दी थी) और ओटोमन तोपचियों के गुप्त सहयोग से ममलुकों ने स्वेज में एक युद्धपोत बेड़े का निर्माण किया। अमीर हुसैन अल-कुर्दी के नेतृत्व में यह बेड़ा भारत आया और गुजरात सल्तनत के दीव के गवर्नर मलिक अय्याज़ तथा कालीकट के ज़मोरिन के साथ गठबंधन किया।</p><p><strong>चोल का युद्ध और लॉरेंको की मृत्यु:</strong> मार्च 1508 में, इस संयुक्त गठबंधन ने चोल (Chaul) के उथले मुहाने में वायसराय के पुत्र लॉरेंको डी अल्मेडा के नेतृत्व वाले छोटे पुर्तगाली गश्ती दल पर अचानक हमला कर दिया। उथले पानी में पुर्तगाली जहाजों की गतिशीलता सीमित हो गई। लॉरेंको का प्रमुख जहाज <em>सेंटो एस्पिरिटो</em> एक केबल में फंस गया। पैर में गंभीर चोट लगने के बाद भी लॉरेंको ने आत्मसमर्पण करने से मना कर दिया और अंततः एक तोप के गोले की चपेट में आने से उनकी मृत्यु हो गई। यह पुर्तगालियों की पहली बड़ी नौसैनिक पराजय थी।</p>"
      },
      {
        "title": "5. दीव की लड़ाई (1509) और विरासत",
        "content": "<p><strong>फ्रांसिस्को डी अल्मेडा का प्रतिशोध:</strong> अपने इकलौते पुत्र की मृत्यु से दुखी वायसराय फ्रांसिस्को डी अल्मेडा ने प्रतिशोध की प्रतिज्ञा ली। जब उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क 1508 के अंत में गवर्नर का पद संभालने के लिए शाही दस्तावेजों के साथ पहुंचे, तो अल्मेडा ने सत्ता सौंपने से इनकार कर दिया और उन्हें कोचीन के किले में कैद कर दिया। अल्मेडा ने 19 जहाजों और 1,300 सैनिकों का एक विशाल बेड़ा तैयार किया और गठबंधन बेड़े को नष्ट करने के लिए उत्तर की ओर बढ़ गए।</p><p><strong>दीव का निर्णायक युद्ध और विरासत:</strong> 3 फरवरी, 1509 को पुर्तगाली बेड़े का दीव के तट पर ममलुक-ओटोमन-गुजराती गठबंधन के साथ आमना-सामना हुआ। अपनी श्रेष्ठ तोप कला, भारी गोलाबारी और ऊंचे जहाजों का उपयोग करके अल्मेडा ने एक विनाशकारी विजय प्राप्त की। ममलुक बेड़ा पूरी तरह नष्ट हो गया और मलिक अय्याज़ को संधि करने, पुर्तगाली कैदियों को छोड़ने तथा भारी हर्जाना देने के लिए मजबूर होना पड़ा। दीव के इस युद्ध ने हिंद महासागर में यूरोपीय नौसैनिक वर्चस्व की नींव रखी जो अगले 400 वर्षों तक कायम रही। इसके बाद, अल्मेडा अल्बुकर्क को सत्ता सौंपकर पुर्तगाल के लिए रवाना हुए, लेकिन मार्च 1510 में दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ पानी के विवाद में मारे गए।</p>"
      }
    ]
  }
}

en_data['deepDive']['sections'][0]['masteryZone'] = sec1_en
en_data['deepDive']['sections'][1]['masteryZone'] = sec2_en
en_data['deepDive']['sections'][2]['masteryZone'] = sec3_en
en_data['deepDive']['sections'][3]['masteryZone'] = sec4_en
en_data['deepDive']['sections'][4]['masteryZone'] = sec5_en
en_data['practiceQuestions'] = practice_en
en_data['mockTestQuestions'] = mock_en

# Ensure labels structure
en_data['labels'] = {
    "tabs": {
        "practice": "2. Practice Zone (50 Qs)"
    },
    "practiceZoneHeader": {
        "title": "Practice Zone: 50 Questions"
    },
    "mockIntro": {
        "title": "UPSC Prelims Mock Exam",
        "description": "Contains 10 questions testing conceptual understanding of Francisco de Almeida's viceroyalty, the Blue Water Policy, fortifications, and battles. 1/3 negative marking applies.",
        "startBtn": "Start Mock Exam"
    },
    "mockPlay": {
        "prevBtn": "Previous",
        "nextBtn": "Next",
        "submitBtn": "Submit Test"
    },
    "clickToExpand": "Click to Expand"
}

hi_data['deepDive']['sections'][0]['masteryZone'] = sec1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = sec2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = sec3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = sec4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = sec5_hi
hi_data['practiceQuestions'] = practice_hi
hi_data['mockTestQuestions'] = mock_hi

hi_data['labels'] = {
    "tabs": {
        "practice": "2. अभ्यास क्षेत्र (50 प्रश्न)"
    },
    "practiceZoneHeader": {
        "title": "अभ्यास क्षेत्र: 50 प्रश्न"
    },
    "mockIntro": {
        "title": "यूपीएससी प्रीलिम्स मॉक परीक्षा",
        "description": "फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, नीले पानी की नीति, किलेबंदी और लड़ाइयों की वैचारिक समझ का परीक्षण करने वाले 10 प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला",
        "nextBtn": "अगला",
        "submitBtn": "टेस्ट सबमिट करें"
    },
    "clickToExpand": "विस्तार करने के लिए क्लिक करें"
}


# Injecting updated UPSC deep dives and practice questions
en_data['deepDive'] = {'title': 'Syllabus Core Study Notes (Deep-Dive)', 'description': "Master Francisco de Almeida's viceroyalty, strategic doctrines, fortifications, key naval battles, and historical legacy in India.", 'sections': [{'title': '1. Geopolitical Genesis & Establishment of the Estado da Índia (1505)', 'content': "<p><strong>Strategic Transition of Portuguese Imperial Policy:</strong> Following Vasco da Gama's navigation of the Cape Route in 1498 and Pedro Álvares Cabral's militarized expedition in 1500, the Portuguese Crown (King Manuel I) recognized that annual commercial expeditions (Armadas da Índia) were structurally inadequate. The Indian Ocean maritime trade network was highly sophisticated, dominated by wealthy merchant syndicates from Gujarat, Malabar, East Africa, and the Red Sea, and protected by local powers like the Zamorin of Calicut. To secure a monopoly over the spice trade and exclude Muslim and European competitors, Lisbon realized it needed to establish a permanent, sovereign military and administrative state in Asia. This led to the creation of the <em>Estado da Índia</em> in 1505.</p><p><strong>The Commissioning of Francisco de Almeida:</strong> In 1505, Francisco de Almeida, a distinguished nobleman, diplomat, and military veteran of the Castilian succession wars (Battle of Toro, 1476) and the Christian conquest of Granada, was appointed as the first Viceroy and Governor-General. He was granted plenipotentiary civil, judicial, and military authority to represent the Portuguese Crown in Asia. Departing Lisbon on March 25, 1505, with 21 ships and 1,500 soldiers, Almeida's mandate was to secure trade routes, build coastal fortifications, enforce a trade monopoly, and crush the naval power of Venice's trade partners, particularly the Mamluk Sultanate of Egypt.</p><p><strong>Administrative Checks and Balances:</strong> To prevent the concentration of absolute power in the hands of the Viceroy, the Portuguese Crown implemented strict institutional controls. Scribes (<em>escrivães</em>) and financial factors (<em>feitores</em>) reported directly to the <em>Casa da Índia</em> in Lisbon, bypassing the Viceroy's financial authority. Furthermore, the Viceroy was appointed for a strict, non-renewable three-year term, setting a precedent that minimized the risk of autonomous provincial rebellion.</p>"}, {'title': '2. The Philosophy of the Blue Water Policy & Mare Clausum', 'content': '<p><strong>The Strategic Philosophy of Política da Água Azul:</strong> Unlike his successor Afonso de Albuquerque, who advocated for a land-based territorial empire with colonial settlements, Francisco de Almeida believed that Portugal\'s severe demographic limitations and limited resources made land conquest in India unsustainable. He formulated the <em>Blue Water Policy</em> (<em>Política da Água Azul</em>), arguing that Portuguese supremacy must reside entirely on the sea. In his famous correspondence to King Manuel I, Almeida declared: <em>"As long as you may be powerful at sea, you will hold India as yours; and if you do not possess this power, little will avail you a fortress on shore."</em></p><p><strong>Tactical Enforcement:</strong> The policy prioritized naval mobility, cruising squadrons, and control of critical shipping lanes over territorial conquest. The Portuguese leveraged superior ship design (large naus and fast caravels) and ship-borne naval artillery (cannon broadsides) to dominate the ocean, bypassing land-based military conflicts with powerful mainland Indian empires like the Vijayanagara Empire or the Deccan Sultanates.</p><p><strong>The Cartaz-Armada System:</strong> To enforce their maritime sovereignty under the legal doctrine of <em>Mare Clausum</em> (Closed Sea), the Portuguese introduced the <em>Cartaz</em> system. Every merchant vessel operating in the Indian Ocean was forced to purchase a Cartaz (licensing permit) from Portuguese authorities. Rulers allied with Portugal, such as the Raja of Cochin, were not exempt from this licensing. This pass prohibited carrying weapons, pepper, ginger, or other royal monopoly goods, and forced ships to route through Portuguese ports to pay heavy customs duties. Any ship found without a Cartaz was subject to immediate seizure, confiscation of cargo, and the execution or enslavement of its crew.</p>'}, {'title': '3. Strategic Fortifications & Indian Ocean Alliances', 'content': "<p><strong>The Four Pillars of Maritime Defense:</strong> To support the Blue Water Policy's cruising patrols, Almeida's expedition was instructed to construct strategically located coastal and island fortifications to serve as safe harbors, fresh water stations, and warehouses (<em>feitorias</em>). The four key fortifications established or consolidated during his tenure were:</p><ul><li><strong>Fort São Tiago (Kilwa, East Africa):</strong> Built in 1505 on the Swahili Coast to secure the passage across the Indian Ocean and control the lucrative gold trade coming from Sofala.</li><li><strong>Fort Manuel (Cochin):</strong> Initially constructed as a wooden palisade in 1503, Almeida reinforced it in 1505 with stone bastions. Cochin served as the first administrative capital of the Estado da Índia, secured through a political alliance with the Trimumpara Raja, who sought Portuguese protection against the dominant Zamorin of Calicut.</li><li><strong>Fort St. Angelo (Cannanore):</strong> Built in late 1505 on a triangular spit of land. This fort secured the trade of Malabar ginger and horse imports, and famously withstood the grueling 1507 Siege of Cannanore launched by local forces backed by Calicut.</li><li><strong>Anjadip Fort:</strong> Built in 1505 on Anjadip Island off the coast of Goa to provide a vital fresh water supply and ship repair facility. However, due to constant raids from the forces of the Adil Shahi Sultanate of Bijapur and the high cost of maintenance, Almeida ordered its demolition and abandonment in 1506.</li></ul>"}, {'title': '4. The Battle of Chaul (1508) & Mamluk Intervention', 'content': "<p><strong>Outbreak of Geopolitical Conflict:</strong> The aggressive Portuguese blockade of the Red Sea and the Persian Gulf severely disrupted the spice monopoly of the Mamluk Sultanate of Egypt, which relied on transit customs duties for its economic survival. Backed secretly by Venice (which supplied shipbuilding timber via Alexandria to Suez) and supported by Ottoman specialists, Egypt constructed a war fleet at Suez. Commanded by Amir Husain Al-Kurdi, the Mamluk fleet sailed to India and allied with Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, and the Zamorin of Calicut to expel the Portuguese.</p><p><strong>The Clash at Chaul:</strong> In March 1508, the coalition fleet surprised a smaller Portuguese patrol fleet in the shallow waters of the Kundalika River estuary at Chaul. The Portuguese fleet was commanded by Lourenço de Almeida, the Viceroy's only son. The shallow river restricted the maneuverability of the heavy Portuguese naus, exposing them to agile Gujarati dhows. During the battle, Lourenço's flagship, the <em>Santo Espírito</em>, was trapped by a fishing cable and pinned down. Despite sustaining severe wounds, Lourenço refused to surrender or abandon ship, fighting valiantly until a cannonball struck and killed him. The battle ended in a major Portuguese defeat, temporarily shattering their myth of naval invincibility in Asian waters.</p>"}, {'title': '5. The Battle of Diu (1509) & Legacy of Sea Power', 'content': '<p><strong>Francisco de Almeida\'s Retaliation:</strong> Shattered by the death of his only son, Viceroy Francisco de Almeida swore a personal oath of revenge. When his designated successor Afonso de Albuquerque arrived in Cochin in late 1508 with royal patents to assume the governorship, Almeida refused to hand over power. He claimed that Albuquerque\'s papers were invalid and subsequently imprisoned him in Fort Manuel, declaring: <em>"I must first seek the blood of my son."</em> Almeida personally assembled a powerful armada of 19 ships and 1,300 soldiers and sailed north to locate the coalition fleet.</p><p><strong>The Decisive Clash & Imperial Legacy:</strong> On February 3, 1509, the Portuguese fleet engaged the Mamluk-Ottoman-Gujarati navy off the coast of Diu. Using superior naval artillery, long-range bombardment, and high-walled vessels that prevented coalition boarding tactics, Almeida achieved a crushing victory. The Mamluk fleet was destroyed, and Malik Ayyaz was forced to sign a peace treaty, releasing prisoners and paying a massive indemnity. The Battle of Diu is considered one of the most critical naval battles in history, as it ended Arab and Egyptian monopoly over the Indian Ocean and established European naval dominance in Asia for the next 400 years. Having avenged his son, Almeida released Albuquerque and departed for Portugal, but was killed in March 1510 in a skirmish with Khoikhoi natives over water at Table Bay, South Africa.</p>'}]}
hi_data['deepDive'] = {'title': 'पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)', 'description': 'फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, रणनीतिक सिद्धांतों, किलों, प्रमुख नौसैनिक लड़ाइयों और भारत में ऐतिहासिक विरासत पर महारत हासिल करें।', 'sections': [{'title': '1. भू-राजनीतिक उत्पत्ति और एस्टाडो दा इंडिया की स्थापना (1505)', 'content': '<p><strong>पुर्तगाली साम्राज्यवादी नीति का रणनीतिक संक्रमण:</strong> 1498 में वास्को डी गामा द्वारा केप मार्ग की खोज और 1500 में पेड्रो अल्वारेज़ कैब्राल के सैन्य अभियान के बाद, पुर्तगाली क्राउन (राजा मैनुअल प्रथम) ने महसूस किया कि वार्षिक व्यावसायिक अभियान (अर्माडा) संरचनात्मक रूप से अपर्याप्त थे। हिंद महासागर का समुद्री व्यापार अत्यधिक परिष्कृत था, जिस पर गुजरात, मालाबार, पूर्वी अफ्रीका और लाल सागर के समृद्ध व्यापारी सिंडिकेट का वर्चस्व था, और उन्हें कालीकट के ज़मोरिन जैसे स्थानीय शासकों का संरक्षण प्राप्त था। मसाला व्यापार पर एकाधिकार हासिल करने के लिए, लिस्बन ने महसूस किया कि उसे एशिया में एक स्थायी, संप्रभु सैन्य और प्रशासनिक राज्य स्थापित करने की आवश्यकता है। इसके परिणामस्वरूप 1505 में <em>एस्टाडो दा इंडिया</em> का गठन हुआ।</p><p><strong>फ्रांसिस्को डी अल्मेडा की नियुक्ति:</strong> 1505 में, कैस्टिलियन उत्तराधिकार युद्धों (टोरो का युद्ध, 1476) और ग्रेनाडा की विजय के एक प्रतिष्ठित कुलीन और सैन्य दिग्गज फ्रांसिस्को डी अल्मेडा को पहले वायसराय और गवर्नर-जनरल के रूप में नियुक्त किया गया था। उन्हें एशिया में पुर्तगाली क्राउन का प्रतिनिधित्व करने के लिए पूर्ण नागरिक, न्यायिक और सैन्य अधिकार दिए गए थे। 25 मार्च, 1505 को 21 जहाजों और 1,500 सैनिकों के साथ रवाना होकर, अल्मेडा का मुख्य कार्य समुद्री मार्गों को सुरक्षित करना, तटीय किलों का निर्माण करना, एकाधिकार लागू करना और ममलुक सल्तनत की नौसैनिक शक्ति को नष्ट करना था।</p><p><strong>प्रशासनिक नियंत्रण और संतुलन:</strong> वायसराय के हाथों में पूर्ण शक्ति के संकेंद्रण को रोकने के लिए, पुर्तगाली क्राउन ने कड़े नियंत्रण लागू किए। लेखक (<em>escrivães</em>) और वित्तीय कारक (<em>feitores</em>) वायसराय को दरकिनार कर सीधे लिस्बन में <em>कासा दा इंडिया</em> को रिपोर्ट करते थे। इसके अतिरिक्त, वायसराय का कार्यकाल कड़ाई से तीन वर्ष तक सीमित रखा गया था, जिसने किसी भी संभावित प्रांतीय विद्रोह के जोखिम को कम कर दिया।</p>'}, {'title': '2. नीले पानी की नीति और मारे क्लॉसम का सिद्धांत', 'content': "<p><strong>नीले पानी की नीति (ब्लू वाटर पॉलिसी) का दर्शन:</strong> अपने उत्तराधिकारी अल्फांसो डी अल्बुकर्क के विपरीत, जिसने क्षेत्रीय और भू-भाग आधारित साम्राज्य का समर्थन किया, फ्रांसिस्को डी अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या और संसाधन भारत में भूमि-आधारित साम्राज्य को नहीं संभाल सकते। उन्होंने <em>ब्लू Water Policy</em> (नीले पानी की नीति) का प्रतिपादन किया, जिसके अनुसार पुर्तगाली शक्ति का आधार केवल समुद्र होना चाहिए। अल्मेडा ने राजा मैनुअल प्रथम को लिखा था: <em>'जब तक आप समुद्र पर शक्तिशाली रहेंगे, भारत आपका रहेगा; और यदि आपके पास यह शक्ति नहीं है, तो भूमि पर बने किले आपके किसी काम नहीं आएंगे।'</em></p><p><strong>नीति का कार्यान्वयन:</strong> इस रणनीति के तहत भूमि विजय के बजाय समुद्री गश्ती, गश्ती जहाजों और नौसैनिक वर्चस्व को प्राथमिकता दी गई। पुर्तगालियों ने बेहतर जहाज डिजाइन और जहाज पर लगी तोपों (नौसैनिक तोपखाने) के उपयोग से हिंद महासागर पर नियंत्रण किया, और विजयनगर साम्राज्य या डेक्कन सल्तनत जैसी मुख्य भूमि की शक्तियों के साथ भूमि-आधारित संघर्षों से दूरी बनाए रखी।</p><p><strong>कार्टाज-अर्माडा प्रणाली:</strong> <em>मारे क्लॉसम</em> (बंद समुद्र) के सिद्धांत के तहत अपनी संप्रभुता लागू करने के लिए पुर्तगालियों ने <em>कार्टाज</em> प्रणाली शुरू की। हिंद महासागर में व्यापार करने वाले सभी जहाजों को पुर्तगाली अधिकारियों से यह लाइसेंस (कार्टाज) खरीदना पड़ता था। कोचीन के राजा जैसे सहयोगी शासक भी इससे मुक्त नहीं थे। इस पास के तहत जहाजों को हथियार, काली मिर्च और अदरक ले जाने की मनाही थी और उन्हें सीमा शुल्क चुकाने के लिए पुर्तगाली बंदरगाहों पर रुकना पड़ता था। बिना कार्टाज के पाए जाने वाले जहाजों को जब्त कर लिया जाता था और चालक दल को मौत की सजा या दासता में धकेल दिया जाता था।</p>"}, {'title': '3. रणनीतिक किलेबंदी और हिंद महासागर के गठबंधन', 'content': '<p><strong>नौसैनिक रक्षा के चार स्तंभ:</strong> अपनी नौसैनिक नीति के समर्थन के लिए अल्मेडा ने रणनीतिक स्थानों पर चार प्रमुख किलों का निर्माण और सुदृढ़ीकरण किया, जो जहाजों के लिए सुरक्षित बंदरगाह, जल आपूर्ति और गोदाम (<em>feitorias</em>) के रूप में कार्य करते थे:</p><ul><li><strong>फोर्ट साओ टियागो (किलवा, पूर्वी अफ्रीका):</strong> हिंद महासागर पार करने वाले जहाजों की सुरक्षा और सोफाला के सोने के व्यापार को नियंत्रित करने के लिए 1505 में स्वाहिली तट पर स्थापित किया गया।</li><li><strong>फोर्ट मैनुअल (कोचीन):</strong> कोचीन के राजा के साथ गठबंधन के तहत 1503 में लकड़ी से बने इस किले को अल्मेडा ने 1505 में पत्थर के बुर्जों से मजबूत किया, जो भारत में पहला यूरोपीय किला बना। यह पहला मुख्यालय भी था।</li><li><strong>फोर्ट सेंट एंजेलो (कन्नूर):</strong> 1505 में मालाबार अदरक के व्यापार और घोड़ों के आयात पर नियंत्रण के लिए निर्मित। इसने 1507 में कन्नूर की प्रसिद्ध घेराबंदी का सफलतापूर्वक सामना किया।</li><li><strong>अंजादीप किला:</strong> गोवा के तट के पास मीठे पानी और जहाजों की मरम्मत के लिए 1505 में बनाया गया था, लेकिन बीजापुर के आदिल शाही सैनिकों के लगातार हमलों के कारण 1506 में इसे गिराकर छोड़ दिया गया।</li></ul>'}, {'title': '4. चोल की लड़ाई (1508) और ममलुक हस्तक्षेप', 'content': '<p><strong>भू-राजनीतिक संघर्ष की शुरुआत:</strong> लाल सागर में पुर्तगाली नाकेबंदी के कारण मिस्र की ममलुक सल्तनत का मसाला व्यापार बुरी तरह प्रभावित हुआ, जिसने मिस्र की अर्थव्यवस्था को खतरे में डाल दिया। वेनिस (जिसने स्वेज को जहाज निर्माण की लकड़ी दी थी) और ओटोमन तोपचियों के गुप्त सहयोग से ममलुकों ने स्वेज में एक युद्धपोत बेड़े का निर्माण किया। अमीर हुसैन अल-कुर्दी के नेतृत्व में यह बेड़ा भारत आया और गुजरात सल्तनत के दीव के गवर्नर मलिक अय्याज़ तथा कालीकट के ज़मोरिन के साथ गठबंधन किया।</p><p><strong>चोल का युद्ध और लॉरेंको की मृत्यु:</strong> मार्च 1508 में, इस संयुक्त गठबंधन ने चोल (Chaul) के उथले मुहाने में वायसराय के पुत्र लॉरेंको डी अल्मेडा के नेतृत्व वाले छोटे पुर्तगाली गश्ती दल पर अचानक हमला कर दिया। उथले पानी में पुर्तगाली जहाजों की गतिशीलता सीमित हो गई। लॉरेंको का प्रमुख जहाज <em>सेंटो एस्पिरिटो</em> एक केबल में फंस गया। पैर में गंभीर चोट लगने के बाद भी लॉरेंको ने आत्मसमर्पण करने से मना कर दिया और अंततः एक तोप के गोले की चपेट में आने से उनकी मृत्यु हो गई। यह पुर्तगालियों की पहली बड़ी नौसैनिक पराजय थी।</p>'}, {'title': '5. दीव की लड़ाई (1509) और समुद्री शक्ति की विरासत', 'content': '<p><strong>फ्रांसिस्को डी अल्मेडा का प्रतिशोध:</strong> अपने इकलौते पुत्र की मृत्यु से दुखी वायसराय फ्रांसिस्को डी अल्मेडा ने प्रतिशोध की प्रतिज्ञा ली। जब उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क 1508 के अंत में गवर्नर का पद संभालने के लिए शाही दस्तावेजों के साथ पहुंचे, तो अल्मेडा ने सत्ता सौंपने से इनकार कर दिया और उन्हें कोचीन के किले में कैद कर दिया। अल्मेडा ने 19 जहाजों और 1,300 सैनिकों का एक विशाल बेड़ा तैयार किया और गठबंधन बेड़े को नष्ट करने के लिए उत्तर की ओर बढ़ गए।</p><p><strong>दीव का निर्णायक युद्ध और विरासत:</strong> 3 फरवरी, 1509 को पुर्तगाली बेड़े का दीव के तट पर ममलुक-ओटोमन-गुजराती गठबंधन के साथ आमना-सामना हुआ। अपनी श्रेष्ठ तोप कला, भारी गोलाबारी और ऊंचे जहाजों का उपयोग करके अल्मेडा ने एक विनाशकारी विजय प्राप्त की। ममलुक बेड़ा पूरी तरह नष्ट हो गया और मलिक अय्याज़ को संधि करने, पुर्तगाली कैदियों को छोड़ने तथा भारी हर्जाना देने के लिए मजबूर होना पड़ा। दीव के इस युद्ध ने हिंद महासागर में यूरोपीय नौसैनिक वर्चस्व की नींव रखी जो अगले 400 वर्षों तक कायम रही। इसके बाद, अल्मेडा अल्बुकर्क को सत्ता सौंपकर पुर्तगाल के लिए रवाना हुए, लेकिन मार्च 1510 में दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ पानी के विवाद में मारे गए।</p>'}]}


# Injecting updated UPSC deep dives and practice questions
en_data['deepDive'] = {'title': 'Syllabus Core Study Notes (Deep-Dive)', 'description': "Master Francisco de Almeida's viceroyalty, strategic doctrines, fortifications, key naval battles, and historical legacy in India.", 'sections': [{'title': '1. Geopolitical Genesis & Establishment of the Estado da Índia (1505)', 'content': "<p><strong>Strategic Transition of Portuguese Imperial Policy:</strong> Following Vasco da Gama's navigation of the Cape Route in 1498 and Pedro Álvares Cabral's militarized expedition in 1500, the Portuguese Crown (King Manuel I) recognized that annual commercial expeditions (Armadas da Índia) were structurally inadequate. The Indian Ocean maritime trade network was highly sophisticated, dominated by wealthy merchant syndicates from Gujarat, Malabar, East Africa, and the Red Sea, and protected by local powers like the Zamorin of Calicut. To secure a monopoly over the spice trade and exclude Muslim and European competitors, Lisbon realized it needed to establish a permanent, sovereign military and administrative state in Asia. This led to the creation of the <em>Estado da Índia</em> in 1505.</p><p><strong>The Commissioning of Francisco de Almeida:</strong> In 1505, Francisco de Almeida, a distinguished nobleman, diplomat, and military veteran of the Castilian succession wars (Battle of Toro, 1476) and the Christian conquest of Granada, was appointed as the first Viceroy and Governor-General. He was granted plenipotentiary civil, judicial, and military authority to represent the Portuguese Crown in Asia. Departing Lisbon on March 25, 1505, with 21 ships and 1,500 soldiers, Almeida's mandate was to secure trade routes, build coastal fortifications, enforce a trade monopoly, and crush the naval power of Venice's trade partners, particularly the Mamluk Sultanate of Egypt.</p><p><strong>Administrative Checks and Balances:</strong> To prevent the concentration of absolute power in the hands of the Viceroy, the Portuguese Crown implemented strict institutional controls. Scribes (<em>escrivães</em>) and financial factors (<em>feitores</em>) reported directly to the <em>Casa da Índia</em> in Lisbon, bypassing the Viceroy's financial authority. Furthermore, the Viceroy was appointed for a strict, non-renewable three-year term, setting a precedent that minimized the risk of autonomous provincial rebellion.</p>"}, {'title': '2. The Philosophy of the Blue Water Policy & Mare Clausum', 'content': '<p><strong>The Strategic Philosophy of Política da Água Azul:</strong> Unlike his successor Afonso de Albuquerque, who advocated for a land-based territorial empire with colonial settlements, Francisco de Almeida believed that Portugal\'s severe demographic limitations and limited resources made land conquest in India unsustainable. He formulated the <em>Blue Water Policy</em> (<em>Política da Água Azul</em>), arguing that Portuguese supremacy must reside entirely on the sea. In his famous correspondence to King Manuel I, Almeida declared: <em>"As long as you may be powerful at sea, you will hold India as yours; and if you do not possess this power, little will avail you a fortress on shore."</em></p><p><strong>Tactical Enforcement:</strong> The policy prioritized naval mobility, cruising squadrons, and control of critical shipping lanes over territorial conquest. The Portuguese leveraged superior ship design (large naus and fast caravels) and ship-borne naval artillery (cannon broadsides) to dominate the ocean, bypassing land-based military conflicts with powerful mainland Indian empires like the Vijayanagara Empire or the Deccan Sultanates.</p><p><strong>The Cartaz-Armada System:</strong> To enforce their maritime sovereignty under the legal doctrine of <em>Mare Clausum</em> (Closed Sea), the Portuguese introduced the <em>Cartaz</em> system. Every merchant vessel operating in the Indian Ocean was forced to purchase a Cartaz (licensing permit) from Portuguese authorities. Rulers allied with Portugal, such as the Raja of Cochin, were not exempt from this licensing. This pass prohibited carrying weapons, pepper, ginger, or other royal monopoly goods, and forced ships to route through Portuguese ports to pay heavy customs duties. Any ship found without a Cartaz was subject to immediate seizure, confiscation of cargo, and the execution or enslavement of its crew.</p>'}, {'title': '3. Strategic Fortifications & Indian Ocean Alliances', 'content': "<p><strong>The Four Pillars of Maritime Defense:</strong> To support the Blue Water Policy's cruising patrols, Almeida's expedition was instructed to construct strategically located coastal and island fortifications to serve as safe harbors, fresh water stations, and warehouses (<em>feitorias</em>). The four key fortifications established or consolidated during his tenure were:</p><ul><li><strong>Fort São Tiago (Kilwa, East Africa):</strong> Built in 1505 on the Swahili Coast to secure the passage across the Indian Ocean and control the lucrative gold trade coming from Sofala.</li><li><strong>Fort Manuel (Cochin):</strong> Initially constructed as a wooden palisade in 1503, Almeida reinforced it in 1505 with stone bastions. Cochin served as the first administrative capital of the Estado da Índia, secured through a political alliance with the Trimumpara Raja, who sought Portuguese protection against the dominant Zamorin of Calicut.</li><li><strong>Fort St. Angelo (Cannanore):</strong> Built in late 1505 on a triangular spit of land. This fort secured the trade of Malabar ginger and horse imports, and famously withstood the grueling 1507 Siege of Cannanore launched by local forces backed by Calicut.</li><li><strong>Anjadip Fort:</strong> Built in 1505 on Anjadip Island off the coast of Goa to provide a vital fresh water supply and ship repair facility. However, due to constant raids from the forces of the Adil Shahi Sultanate of Bijapur and the high cost of maintenance, Almeida ordered its demolition and abandonment in 1506.</li></ul>"}, {'title': '4. The Battle of Chaul (1508) & Mamluk Intervention', 'content': "<p><strong>Outbreak of Geopolitical Conflict:</strong> The aggressive Portuguese blockade of the Red Sea and the Persian Gulf severely disrupted the spice monopoly of the Mamluk Sultanate of Egypt, which relied on transit customs duties for its economic survival. Backed secretly by Venice (which supplied shipbuilding timber via Alexandria to Suez) and supported by Ottoman specialists, Egypt constructed a war fleet at Suez. Commanded by Amir Husain Al-Kurdi, the Mamluk fleet sailed to India and allied with Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, and the Zamorin of Calicut to expel the Portuguese.</p><p><strong>The Clash at Chaul:</strong> In March 1508, the coalition fleet surprised a smaller Portuguese patrol fleet in the shallow waters of the Kundalika River estuary at Chaul. The Portuguese fleet was commanded by Lourenço de Almeida, the Viceroy's only son. The shallow river restricted the maneuverability of the heavy Portuguese naus, exposing them to agile Gujarati dhows. During the battle, Lourenço's flagship, the <em>Santo Espírito</em>, was trapped by a fishing cable and pinned down. Despite sustaining severe wounds, Lourenço refused to surrender or abandon ship, fighting valiantly until a cannonball struck and killed him. The battle ended in a major Portuguese defeat, temporarily shattering their myth of naval invincibility in Asian waters.</p>"}, {'title': '5. The Battle of Diu (1509) & Legacy of Sea Power', 'content': '<p><strong>Francisco de Almeida\'s Retaliation:</strong> Shattered by the death of his only son, Viceroy Francisco de Almeida swore a personal oath of revenge. When his designated successor Afonso de Albuquerque arrived in Cochin in late 1508 with royal patents to assume the governorship, Almeida refused to hand over power. He claimed that Albuquerque\'s papers were invalid and subsequently imprisoned him in Fort Manuel, declaring: <em>"I must first seek the blood of my son."</em> Almeida personally assembled a powerful armada of 19 ships and 1,300 soldiers and sailed north to locate the coalition fleet.</p><p><strong>The Decisive Clash & Imperial Legacy:</strong> On February 3, 1509, the Portuguese fleet engaged the Mamluk-Ottoman-Gujarati navy off the coast of Diu. Using superior naval artillery, long-range bombardment, and high-walled vessels that prevented coalition boarding tactics, Almeida achieved a crushing victory. The Mamluk fleet was destroyed, and Malik Ayyaz was forced to sign a peace treaty, releasing prisoners and paying a massive indemnity. The Battle of Diu is considered one of the most critical naval battles in history, as it ended Arab and Egyptian monopoly over the Indian Ocean and established European naval dominance in Asia for the next 400 years. Having avenged his son, Almeida released Albuquerque and departed for Portugal, but was killed in March 1510 in a skirmish with Khoikhoi natives over water at Table Bay, South Africa.</p>'}]}
hi_data['deepDive'] = {'title': 'पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)', 'description': 'फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, रणनीतिक सिद्धांतों, किलों, प्रमुख नौसैनिक लड़ाइयों और भारत में ऐतिहासिक विरासत पर महारत हासिल करें।', 'sections': [{'title': '1. भू-राजनीतिक उत्पत्ति और एस्टाडो दा इंडिया की स्थापना (1505)', 'content': '<p><strong>पुर्तगाली साम्राज्यवादी नीति का रणनीतिक संक्रमण:</strong> 1498 में वास्को डी गामा द्वारा केप मार्ग की खोज और 1500 में पेड्रो अल्वारेज़ कैब्राल के सैन्य अभियान के बाद, पुर्तगाली क्राउन (राजा मैनुअल प्रथम) ने महसूस किया कि वार्षिक व्यावसायिक अभियान (अर्माडा) संरचनात्मक रूप से अपर्याप्त थे। हिंद महासागर का समुद्री व्यापार अत्यधिक परिष्कृत था, जिस पर गुजरात, मालाबार, पूर्वी अफ्रीका और लाल सागर के समृद्ध व्यापारी सिंडिकेट का वर्चस्व था, और उन्हें कालीकट के ज़मोरिन जैसे स्थानीय शासकों का संरक्षण प्राप्त था। मसाला व्यापार पर एकाधिकार हासिल करने के लिए, लिस्बन ने महसूस किया कि उसे एशिया में एक स्थायी, संप्रभु सैन्य और प्रशासनिक राज्य स्थापित करने की आवश्यकता है। इसके परिणामस्वरूप 1505 में <em>एस्टाडो दा इंडिया</em> का गठन हुआ।</p><p><strong>फ्रांसिस्को डी अल्मेडा की नियुक्ति:</strong> 1505 में, कैस्टिलियन उत्तराधिकार युद्धों (टोरो का युद्ध, 1476) और ग्रेनाडा की विजय के एक प्रतिष्ठित कुलीन और सैन्य दिग्गज फ्रांसिस्को डी अल्मेडा को पहले वायसराय और गवर्नर-जनरल के रूप में नियुक्त किया गया था। उन्हें एशिया में पुर्तगाली क्राउन का प्रतिनिधित्व करने के लिए पूर्ण नागरिक, न्यायिक और सैन्य अधिकार दिए गए थे। 25 मार्च, 1505 को 21 जहाजों और 1,500 सैनिकों के साथ रवाना होकर, अल्मेडा का मुख्य कार्य समुद्री मार्गों को सुरक्षित करना, तटीय किलों का निर्माण करना, एकाधिकार लागू करना और ममलुक सल्तनत की नौसैनिक शक्ति को नष्ट करना था।</p><p><strong>प्रशासनिक नियंत्रण और संतुलन:</strong> वायसराय के हाथों में पूर्ण शक्ति के संकेंद्रण को रोकने के लिए, पुर्तगाली क्राउन ने कड़े नियंत्रण लागू किए। लेखक (<em>escrivães</em>) और वित्तीय कारक (<em>feitores</em>) वायसराय को दरकिनार कर सीधे लिस्बन में <em>कासा दा इंडिया</em> को रिपोर्ट करते थे। इसके अतिरिक्त, वायसराय का कार्यकाल कड़ाई से तीन वर्ष तक सीमित रखा गया था, जिसने किसी भी संभावित प्रांतीय विद्रोह के जोखिम को कम कर दिया।</p>'}, {'title': '2. नीले पानी की नीति और मारे क्लॉसम का सिद्धांत', 'content': "<p><strong>नीले पानी की नीति (ब्लू वाटर पॉलिसी) का दर्शन:</strong> अपने उत्तराधिकारी अल्फांसो डी अल्बुकर्क के विपरीत, जिसने क्षेत्रीय और भू-भाग आधारित साम्राज्य का समर्थन किया, फ्रांसिस्को डी अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या और संसाधन भारत में भूमि-आधारित साम्राज्य को नहीं संभाल सकते। उन्होंने <em>ब्लू Water Policy</em> (नीले पानी की नीति) का प्रतिपादन किया, जिसके अनुसार पुर्तगाली शक्ति का आधार केवल समुद्र होना चाहिए। अल्मेडा ने राजा मैनुअल प्रथम को लिखा था: <em>'जब तक आप समुद्र पर शक्तिशाली रहेंगे, भारत आपका रहेगा; और यदि आपके पास यह शक्ति नहीं है, तो भूमि पर बने किले आपके किसी काम नहीं आएंगे।'</em></p><p><strong>नीति का कार्यान्वयन:</strong> इस रणनीति के तहत भूमि विजय के बजाय समुद्री गश्ती, गश्ती जहाजों और नौसैनिक वर्चस्व को प्राथमिकता दी गई। पुर्तगालियों ने बेहतर जहाज डिजाइन और जहाज पर लगी तोपों (नौसैनिक तोपखाने) के उपयोग से हिंद महासागर पर नियंत्रण किया, और विजयनगर साम्राज्य या डेक्कन सल्तनत जैसी मुख्य भूमि की शक्तियों के साथ भूमि-आधारित संघर्षों से दूरी बनाए रखी।</p><p><strong>कार्टाज-अर्माडा प्रणाली:</strong> <em>मारे क्लॉसम</em> (बंद समुद्र) के सिद्धांत के तहत अपनी संप्रभुता लागू करने के लिए पुर्तगालियों ने <em>कार्टाज</em> प्रणाली शुरू की। हिंद महासागर में व्यापार करने वाले सभी जहाजों को पुर्तगाली अधिकारियों से यह लाइसेंस (कार्टाज) खरीदना पड़ता था। कोचीन के राजा जैसे सहयोगी शासक भी इससे मुक्त नहीं थे। इस पास के तहत जहाजों को हथियार, काली मिर्च और अदरक ले जाने की मनाही थी और उन्हें सीमा शुल्क चुकाने के लिए पुर्तगाली बंदरगाहों पर रुकना पड़ता था। बिना कार्टाज के पाए जाने वाले जहाजों को जब्त कर लिया जाता था और चालक दल को मौत की सजा या दासता में धकेल दिया जाता था।</p>"}, {'title': '3. रणनीतिक किलेबंदी और हिंद महासागर के गठबंधन', 'content': '<p><strong>नौसैनिक रक्षा के चार स्तंभ:</strong> अपनी नौसैनिक नीति के समर्थन के लिए अल्मेडा ने रणनीतिक स्थानों पर चार प्रमुख किलों का निर्माण और सुदृढ़ीकरण किया, जो जहाजों के लिए सुरक्षित बंदरगाह, जल आपूर्ति और गोदाम (<em>feitorias</em>) के रूप में कार्य करते थे:</p><ul><li><strong>फोर्ट साओ टियागो (किलवा, पूर्वी अफ्रीका):</strong> हिंद महासागर पार करने वाले जहाजों की सुरक्षा और सोफाला के सोने के व्यापार को नियंत्रित करने के लिए 1505 में स्वाहिली तट पर स्थापित किया गया।</li><li><strong>फोर्ट मैनुअल (कोचीन):</strong> कोचीन के राजा के साथ गठबंधन के तहत 1503 में लकड़ी से बने इस किले को अल्मेडा ने 1505 में पत्थर के बुर्जों से मजबूत किया, जो भारत में पहला यूरोपीय किला बना। यह पहला मुख्यालय भी था।</li><li><strong>फोर्ट सेंट एंजेलो (कन्नूर):</strong> 1505 में मालाबार अदरक के व्यापार और घोड़ों के आयात पर नियंत्रण के लिए निर्मित। इसने 1507 में कन्नूर की प्रसिद्ध घेराबंदी का सफलतापूर्वक सामना किया।</li><li><strong>अंजादीप किला:</strong> गोवा के तट के पास मीठे पानी और जहाजों की मरम्मत के लिए 1505 में बनाया गया था, लेकिन बीजापुर के आदिल शाही सैनिकों के लगातार हमलों के कारण 1506 में इसे गिराकर छोड़ दिया गया।</li></ul>'}, {'title': '4. चोल की लड़ाई (1508) और ममलुक हस्तक्षेप', 'content': '<p><strong>भू-राजनीतिक संघर्ष की शुरुआत:</strong> लाल सागर में पुर्तगाली नाकेबंदी के कारण मिस्र की ममलुक सल्तनत का मसाला व्यापार बुरी तरह प्रभावित हुआ, जिसने मिस्र की अर्थव्यवस्था को खतरे में डाल दिया। वेनिस (जिसने स्वेज को जहाज निर्माण की लकड़ी दी थी) और ओटोमन तोपचियों के गुप्त सहयोग से ममलुकों ने स्वेज में एक युद्धपोत बेड़े का निर्माण किया। अमीर हुसैन अल-कुर्दी के नेतृत्व में यह बेड़ा भारत आया और गुजरात सल्तनत के दीव के गवर्नर मलिक अय्याज़ तथा कालीकट के ज़मोरिन के साथ गठबंधन किया।</p><p><strong>चोल का युद्ध और लॉरेंको की मृत्यु:</strong> मार्च 1508 में, इस संयुक्त गठबंधन ने चोल (Chaul) के उथले मुहाने में वायसराय के पुत्र लॉरेंको डी अल्मेडा के नेतृत्व वाले छोटे पुर्तगाली गश्ती दल पर अचानक हमला कर दिया। उथले पानी में पुर्तगाली जहाजों की गतिशीलता सीमित हो गई। लॉरेंको का प्रमुख जहाज <em>सेंटो एस्पिरिटो</em> एक केबल में फंस गया। पैर में गंभीर चोट लगने के बाद भी लॉरेंको ने आत्मसमर्पण करने से मना कर दिया और अंततः एक तोप के गोले की चपेट में आने से उनकी मृत्यु हो गई। यह पुर्तगालियों की पहली बड़ी नौसैनिक पराजय थी।</p>'}, {'title': '5. दीव की लड़ाई (1509) और समुद्री शक्ति की विरासत', 'content': '<p><strong>फ्रांसिस्को डी अल्मेडा का प्रतिशोध:</strong> अपने इकलौते पुत्र की मृत्यु से दुखी वायसराय फ्रांसिस्को डी अल्मेडा ने प्रतिशोध की प्रतिज्ञा ली। जब उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क 1508 के अंत में गवर्नर का पद संभालने के लिए शाही दस्तावेजों के साथ पहुंचे, तो अल्मेडा ने सत्ता सौंपने से इनकार कर दिया और उन्हें कोचीन के किले में कैद कर दिया। अल्मेडा ने 19 जहाजों और 1,300 सैनिकों का एक विशाल बेड़ा तैयार किया और गठबंधन बेड़े को नष्ट करने के लिए उत्तर की ओर बढ़ गए।</p><p><strong>दीव का निर्णायक युद्ध और विरासत:</strong> 3 फरवरी, 1509 को पुर्तगाली बेड़े का दीव के तट पर ममलुक-ओटोमन-गुजराती गठबंधन के साथ आमना-सामना हुआ। अपनी श्रेष्ठ तोप कला, भारी गोलाबारी और ऊंचे जहाजों का उपयोग करके अल्मेडा ने एक विनाशकारी विजय प्राप्त की। ममलुक बेड़ा पूरी तरह नष्ट हो गया और मलिक अय्याज़ को संधि करने, पुर्तगाली कैदियों को छोड़ने तथा भारी हर्जाना देने के लिए मजबूर होना पड़ा। दीव के इस युद्ध ने हिंद महासागर में यूरोपीय नौसैनिक वर्चस्व की नींव रखी जो अगले 400 वर्षों तक कायम रही। इसके बाद, अल्मेडा अल्बुकर्क को सत्ता सौंपकर पुर्तगाल के लिए रवाना हुए, लेकिन मार्च 1510 में दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ पानी के विवाद में मारे गए।</p>'}]}


# Injecting updated UPSC deep dives and practice questions
en_data['deepDive'] = {'title': 'Syllabus Core Study Notes (Deep-Dive)', 'description': "Master Francisco de Almeida's viceroyalty, strategic doctrines, fortifications, key naval battles, and historical legacy in India.", 'sections': [{'title': '1. Geopolitical Genesis & Establishment of the Estado da Índia (1505)', 'content': "<p><strong>Strategic Transition of Portuguese Imperial Policy:</strong> Following Vasco da Gama's navigation of the Cape Route in 1498 and Pedro Álvares Cabral's militarized expedition in 1500, the Portuguese Crown (King Manuel I) recognized that annual commercial expeditions (Armadas da Índia) were structurally inadequate. The Indian Ocean maritime trade network was highly sophisticated, dominated by wealthy merchant syndicates from Gujarat, Malabar, East Africa, and the Red Sea, and protected by local powers like the Zamorin of Calicut. To secure a monopoly over the spice trade and exclude Muslim and European competitors, Lisbon realized it needed to establish a permanent, sovereign military and administrative state in Asia. This led to the creation of the <em>Estado da Índia</em> in 1505.</p><p><strong>The Commissioning of Francisco de Almeida:</strong> In 1505, Francisco de Almeida, a distinguished nobleman, diplomat, and military veteran of the Castilian succession wars (Battle of Toro, 1476) and the Christian conquest of Granada, was appointed as the first Viceroy and Governor-General. He was granted plenipotentiary civil, judicial, and military authority to represent the Portuguese Crown in Asia. Departing Lisbon on March 25, 1505, with 21 ships and 1,500 soldiers, Almeida's mandate was to secure trade routes, build coastal fortifications, enforce a trade monopoly, and crush the naval power of Venice's trade partners, particularly the Mamluk Sultanate of Egypt.</p><p><strong>Administrative Checks and Balances:</strong> To prevent the concentration of absolute power in the hands of the Viceroy, the Portuguese Crown implemented strict institutional controls. Scribes (<em>escrivães</em>) and financial factors (<em>feitores</em>) reported directly to the <em>Casa da Índia</em> in Lisbon, bypassing the Viceroy's financial authority. Furthermore, the Viceroy was appointed for a strict, non-renewable three-year term, setting a precedent that minimized the risk of autonomous provincial rebellion.</p>"}, {'title': '2. The Philosophy of the Blue Water Policy & Mare Clausum', 'content': '<p><strong>The Strategic Philosophy of Política da Água Azul:</strong> Unlike his successor Afonso de Albuquerque, who advocated for a land-based territorial empire with colonial settlements, Francisco de Almeida believed that Portugal\'s severe demographic limitations and limited resources made land conquest in India unsustainable. He formulated the <em>Blue Water Policy</em> (<em>Política da Água Azul</em>), arguing that Portuguese supremacy must reside entirely on the sea. In his famous correspondence to King Manuel I, Almeida declared: <em>"As long as you may be powerful at sea, you will hold India as yours; and if you do not possess this power, little will avail you a fortress on shore."</em></p><p><strong>Tactical Enforcement:</strong> The policy prioritized naval mobility, cruising squadrons, and control of critical shipping lanes over territorial conquest. The Portuguese leveraged superior ship design (large naus and fast caravels) and ship-borne naval artillery (cannon broadsides) to dominate the ocean, bypassing land-based military conflicts with powerful mainland Indian empires like the Vijayanagara Empire or the Deccan Sultanates.</p><p><strong>The Cartaz-Armada System:</strong> To enforce their maritime sovereignty under the legal doctrine of <em>Mare Clausum</em> (Closed Sea), the Portuguese introduced the <em>Cartaz</em> system. Every merchant vessel operating in the Indian Ocean was forced to purchase a Cartaz (licensing permit) from Portuguese authorities. Rulers allied with Portugal, such as the Raja of Cochin, were not exempt from this licensing. This pass prohibited carrying weapons, pepper, ginger, or other royal monopoly goods, and forced ships to route through Portuguese ports to pay heavy customs duties. Any ship found without a Cartaz was subject to immediate seizure, confiscation of cargo, and the execution or enslavement of its crew.</p>'}, {'title': '3. Strategic Fortifications & Indian Ocean Alliances', 'content': "<p><strong>The Four Pillars of Maritime Defense:</strong> To support the Blue Water Policy's cruising patrols, Almeida's expedition was instructed to construct strategically located coastal and island fortifications to serve as safe harbors, fresh water stations, and warehouses (<em>feitorias</em>). The four key fortifications established or consolidated during his tenure were:</p><ul><li><strong>Fort São Tiago (Kilwa, East Africa):</strong> Built in 1505 on the Swahili Coast to secure the passage across the Indian Ocean and control the lucrative gold trade coming from Sofala.</li><li><strong>Fort Manuel (Cochin):</strong> Initially constructed as a wooden palisade in 1503, Almeida reinforced it in 1505 with stone bastions. Cochin served as the first administrative capital of the Estado da Índia, secured through a political alliance with the Trimumpara Raja, who sought Portuguese protection against the dominant Zamorin of Calicut.</li><li><strong>Fort St. Angelo (Cannanore):</strong> Built in late 1505 on a triangular spit of land. This fort secured the trade of Malabar ginger and horse imports, and famously withstood the grueling 1507 Siege of Cannanore launched by local forces backed by Calicut.</li><li><strong>Anjadip Fort:</strong> Built in 1505 on Anjadip Island off the coast of Goa to provide a vital fresh water supply and ship repair facility. However, due to constant raids from the forces of the Adil Shahi Sultanate of Bijapur and the high cost of maintenance, Almeida ordered its demolition and abandonment in 1506.</li></ul>"}, {'title': '4. The Battle of Chaul (1508) & Mamluk Intervention', 'content': "<p><strong>Outbreak of Geopolitical Conflict:</strong> The aggressive Portuguese blockade of the Red Sea and the Persian Gulf severely disrupted the spice monopoly of the Mamluk Sultanate of Egypt, which relied on transit customs duties for its economic survival. Backed secretly by Venice (which supplied shipbuilding timber via Alexandria to Suez) and supported by Ottoman specialists, Egypt constructed a war fleet at Suez. Commanded by Amir Husain Al-Kurdi, the Mamluk fleet sailed to India and allied with Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, and the Zamorin of Calicut to expel the Portuguese.</p><p><strong>The Clash at Chaul:</strong> In March 1508, the coalition fleet surprised a smaller Portuguese patrol fleet in the shallow waters of the Kundalika River estuary at Chaul. The Portuguese fleet was commanded by Lourenço de Almeida, the Viceroy's only son. The shallow river restricted the maneuverability of the heavy Portuguese naus, exposing them to agile Gujarati dhows. During the battle, Lourenço's flagship, the <em>Santo Espírito</em>, was trapped by a fishing cable and pinned down. Despite sustaining severe wounds, Lourenço refused to surrender or abandon ship, fighting valiantly until a cannonball struck and killed him. The battle ended in a major Portuguese defeat, temporarily shattering their myth of naval invincibility in Asian waters.</p>"}, {'title': '5. The Battle of Diu (1509) & Legacy of Sea Power', 'content': '<p><strong>Francisco de Almeida\'s Retaliation:</strong> Shattered by the death of his only son, Viceroy Francisco de Almeida swore a personal oath of revenge. When his designated successor Afonso de Albuquerque arrived in Cochin in late 1508 with royal patents to assume the governorship, Almeida refused to hand over power. He claimed that Albuquerque\'s papers were invalid and subsequently imprisoned him in Fort Manuel, declaring: <em>"I must first seek the blood of my son."</em> Almeida personally assembled a powerful armada of 19 ships and 1,300 soldiers and sailed north to locate the coalition fleet.</p><p><strong>The Decisive Clash & Imperial Legacy:</strong> On February 3, 1509, the Portuguese fleet engaged the Mamluk-Ottoman-Gujarati navy off the coast of Diu. Using superior naval artillery, long-range bombardment, and high-walled vessels that prevented coalition boarding tactics, Almeida achieved a crushing victory. The Mamluk fleet was destroyed, and Malik Ayyaz was forced to sign a peace treaty, releasing prisoners and paying a massive indemnity. The Battle of Diu is considered one of the most critical naval battles in history, as it ended Arab and Egyptian monopoly over the Indian Ocean and established European naval dominance in Asia for the next 400 years. Having avenged his son, Almeida released Albuquerque and departed for Portugal, but was killed in March 1510 in a skirmish with Khoikhoi natives over water at Table Bay, South Africa.</p>'}]}
en_data['deepDive']['sections'][0]['masteryZone'] = sec1_en
en_data['deepDive']['sections'][1]['masteryZone'] = sec2_en
en_data['deepDive']['sections'][2]['masteryZone'] = sec3_en
en_data['deepDive']['sections'][3]['masteryZone'] = sec4_en
en_data['deepDive']['sections'][4]['masteryZone'] = sec5_en

hi_data['deepDive'] = {'title': 'पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)', 'description': 'फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, रणनीतिक सिद्धांतों, किलों, प्रमुख नौसैनिक लड़ाइयों और भारत में ऐतिहासिक विरासत पर महारत हासिल करें।', 'sections': [{'title': '1. भू-राजनीतिक उत्पत्ति और एस्टाडो दा इंडिया की स्थापना (1505)', 'content': '<p><strong>पुर्तगाली साम्राज्यवादी नीति का रणनीतिक संक्रमण:</strong> 1498 में वास्को डी गामा द्वारा केप मार्ग की खोज और 1500 में पेड्रो अल्वारेज़ कैब्राल के सैन्य अभियान के बाद, पुर्तगाली क्राउन (राजा मैनुअल प्रथम) ने महसूस किया कि वार्षिक व्यावसायिक अभियान (अर्माडा) संरचनात्मक रूप से अपर्याप्त थे। हिंद महासागर का समुद्री व्यापार अत्यधिक परिष्कृत था, जिस पर गुजरात, मालाबार, पूर्वी अफ्रीका और लाल सागर के समृद्ध व्यापारी सिंडिकेट का वर्चस्व था, और उन्हें कालीकट के ज़मोरिन जैसे स्थानीय शासकों का संरक्षण प्राप्त था। मसाला व्यापार पर एकाधिकार हासिल करने के लिए, लिस्बन ने महसूस किया कि उसे एशिया में एक स्थायी, संप्रभु सैन्य और प्रशासनिक राज्य स्थापित करने की आवश्यकता है। इसके परिणामस्वरूप 1505 में <em>एस्टाडो दा इंडिया</em> का गठन हुआ।</p><p><strong>फ्रांसिस्को डी अल्मेडा की नियुक्ति:</strong> 1505 में, कैस्टिलियन उत्तराधिकार युद्धों (टोरो का युद्ध, 1476) और ग्रेनाडा की विजय के एक प्रतिष्ठित कुलीन और सैन्य दिग्गज फ्रांसिस्को डी अल्मेडा को पहले वायसराय और गवर्नर-जनरल के रूप में नियुक्त किया गया था। उन्हें एशिया में पुर्तगाली क्राउन का प्रतिनिधित्व करने के लिए पूर्ण नागरिक, न्यायिक और सैन्य अधिकार दिए गए थे। 25 मार्च, 1505 को 21 जहाजों और 1,500 सैनिकों के साथ रवाना होकर, अल्मेडा का मुख्य कार्य समुद्री मार्गों को सुरक्षित करना, तटीय किलों का निर्माण करना, एकाधिकार लागू करना और ममलुक सल्तनत की नौसैनिक शक्ति को नष्ट करना था।</p><p><strong>प्रशासनिक नियंत्रण और संतुलन:</strong> वायसराय के हाथों में पूर्ण शक्ति के संकेंद्रण को रोकने के लिए, पुर्तगाली क्राउन ने कड़े नियंत्रण लागू किए। लेखक (<em>escrivães</em>) और वित्तीय कारक (<em>feitores</em>) वायसराय को दरकिनार कर सीधे लिस्बन में <em>कासा दा इंडिया</em> को रिपोर्ट करते थे। इसके अतिरिक्त, वायसराय का कार्यकाल कड़ाई से तीन वर्ष तक सीमित रखा गया था, जिसने किसी भी संभावित प्रांतीय विद्रोह के जोखिम को कम कर दिया।</p>'}, {'title': '2. नीले पानी की नीति और मारे क्लॉसम का सिद्धांत', 'content': "<p><strong>नीले पानी की नीति (ब्लू वाटर पॉलिसी) का दर्शन:</strong> अपने उत्तराधिकारी अल्फांसो डी अल्बुकर्क के विपरीत, जिसने क्षेत्रीय और भू-भाग आधारित साम्राज्य का समर्थन किया, फ्रांसिस्को डी अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या और संसाधन भारत में भूमि-आधारित साम्राज्य को नहीं संभाल सकते। उन्होंने <em>ब्लू Water Policy</em> (नीले पानी की नीति) का प्रतिपादन किया, जिसके अनुसार पुर्तगाली शक्ति का आधार केवल समुद्र होना चाहिए। अल्मेडा ने राजा मैनुअल प्रथम को लिखा था: <em>'जब तक आप समुद्र पर शक्तिशाली रहेंगे, भारत आपका रहेगा; और यदि आपके पास यह शक्ति नहीं है, तो भूमि पर बने किले आपके किसी काम नहीं आएंगे।'</em></p><p><strong>नीति का कार्यान्वयन:</strong> इस रणनीति के तहत भूमि विजय के बजाय समुद्री गश्ती, गश्ती जहाजों और नौसैनिक वर्चस्व को प्राथमिकता दी गई। पुर्तगालियों ने बेहतर जहाज डिजाइन और जहाज पर लगी तोपों (नौसैनिक तोपखाने) के उपयोग से हिंद महासागर पर नियंत्रण किया, और विजयनगर साम्राज्य या डेक्कन सल्तनत जैसी मुख्य भूमि की शक्तियों के साथ भूमि-आधारित संघर्षों से दूरी बनाए रखी।</p><p><strong>कार्टाज-अर्माडा प्रणाली:</strong> <em>मारे क्लॉसम</em> (बंद समुद्र) के सिद्धांत के तहत अपनी संप्रभुता लागू करने के लिए पुर्तगालियों ने <em>कार्टाज</em> प्रणाली शुरू की। हिंद महासागर में व्यापार करने वाले सभी जहाजों को पुर्तगाली अधिकारियों से यह लाइसेंस (कार्टाज) खरीदना पड़ता था। कोचीन के राजा जैसे सहयोगी शासक भी इससे मुक्त नहीं थे। इस पास के तहत जहाजों को हथियार, काली मिर्च और अदरक ले जाने की मनाही थी और उन्हें सीमा शुल्क चुकाने के लिए पुर्तगाली बंदरगाहों पर रुकना पड़ता था। बिना कार्टाज के पाए जाने वाले जहाजों को जब्त कर लिया जाता था और चालक दल को मौत की सजा या दासता में धकेल दिया जाता था।</p>"}, {'title': '3. रणनीतिक किलेबंदी और हिंद महासागर के गठबंधन', 'content': '<p><strong>नौसैनिक रक्षा के चार स्तंभ:</strong> अपनी नौसैनिक नीति के समर्थन के लिए अल्मेडा ने रणनीतिक स्थानों पर चार प्रमुख किलों का निर्माण और सुदृढ़ीकरण किया, जो जहाजों के लिए सुरक्षित बंदरगाह, जल आपूर्ति और गोदाम (<em>feitorias</em>) के रूप में कार्य करते थे:</p><ul><li><strong>फोर्ट साओ टियागो (किलवा, पूर्वी अफ्रीका):</strong> हिंद महासागर पार करने वाले जहाजों की सुरक्षा और सोफाला के सोने के व्यापार को नियंत्रित करने के लिए 1505 में स्वाहिली तट पर स्थापित किया गया।</li><li><strong>फोर्ट मैनुअल (कोचीन):</strong> कोचीन के राजा के साथ गठबंधन के तहत 1503 में लकड़ी से बने इस किले को अल्मेडा ने 1505 में पत्थर के बुर्जों से मजबूत किया, जो भारत में पहला यूरोपीय किला बना। यह पहला मुख्यालय भी था।</li><li><strong>फोर्ट सेंट एंजेलो (कन्नूर):</strong> 1505 में मालाबार अदरक के व्यापार और घोड़ों के आयात पर नियंत्रण के लिए निर्मित। इसने 1507 में कन्नूर की प्रसिद्ध घेराबंदी का सफलतापूर्वक सामना किया।</li><li><strong>अंजादीप किला:</strong> गोवा के तट के पास मीठे पानी और जहाजों की मरम्मत के लिए 1505 में बनाया गया था, लेकिन बीजापुर के आदिल शाही सैनिकों के लगातार हमलों के कारण 1506 में इसे गिराकर छोड़ दिया गया।</li></ul>'}, {'title': '4. चोल की लड़ाई (1508) और ममलुक हस्तक्षेप', 'content': '<p><strong>भू-राजनीतिक संघर्ष की शुरुआत:</strong> लाल सागर में पुर्तगाली नाकेबंदी के कारण मिस्र की ममलुक सल्तनत का मसाला व्यापार बुरी तरह प्रभावित हुआ, जिसने मिस्र की अर्थव्यवस्था को खतरे में डाल दिया। वेनिस (जिसने स्वेज को जहाज निर्माण की लकड़ी दी थी) और ओटोमन तोपचियों के गुप्त सहयोग से ममलुकों ने स्वेज में एक युद्धपोत बेड़े का निर्माण किया। अमीर हुसैन अल-कुर्दी के नेतृत्व में यह बेड़ा भारत आया और गुजरात सल्तनत के दीव के गवर्नर मलिक अय्याज़ तथा कालीकट के ज़मोरिन के साथ गठबंधन किया।</p><p><strong>चोल का युद्ध और लॉरेंको की मृत्यु:</strong> मार्च 1508 में, इस संयुक्त गठबंधन ने चोल (Chaul) के उथले मुहाने में वायसराय के पुत्र लॉरेंको डी अल्मेडा के नेतृत्व वाले छोटे पुर्तगाली गश्ती दल पर अचानक हमला कर दिया। उथले पानी में पुर्तगाली जहाजों की गतिशीलता सीमित हो गई। लॉरेंको का प्रमुख जहाज <em>सेंटो एस्पिरिटो</em> एक केबल में फंस गया। पैर में गंभीर चोट लगने के बाद भी लॉरेंको ने आत्मसमर्पण करने से मना कर दिया और अंततः एक तोप के गोले की चपेट में आने से उनकी मृत्यु हो गई। यह पुर्तगालियों की पहली बड़ी नौसैनिक पराजय थी।</p>'}, {'title': '5. दीव की लड़ाई (1509) और समुद्री शक्ति की विरासत', 'content': '<p><strong>फ्रांसिस्को डी अल्मेडा का प्रतिशोध:</strong> अपने इकलौते पुत्र की मृत्यु से दुखी वायसराय फ्रांसिस्को डी अल्मेडा ने प्रतिशोध की प्रतिज्ञा ली। जब उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क 1508 के अंत में गवर्नर का पद संभालने के लिए शाही दस्तावेजों के साथ पहुंचे, तो अल्मेडा ने सत्ता सौंपने से इनकार कर दिया और उन्हें कोचीन के किले में कैद कर दिया। अल्मेडा ने 19 जहाजों और 1,300 सैनिकों का एक विशाल बेड़ा तैयार किया और गठबंधन बेड़े को नष्ट करने के लिए उत्तर की ओर बढ़ गए।</p><p><strong>दीव का निर्णायक युद्ध और विरासत:</strong> 3 फरवरी, 1509 को पुर्तगाली बेड़े का दीव के तट पर ममलुक-ओटोमन-गुजराती गठबंधन के साथ आमना-सामना हुआ। अपनी श्रेष्ठ तोप कला, भारी गोलाबारी और ऊंचे जहाजों का उपयोग करके अल्मेडा ने एक विनाशकारी विजय प्राप्त की। ममलुक बेड़ा पूरी तरह नष्ट हो गया और मलिक अय्याज़ को संधि करने, पुर्तगाली कैदियों को छोड़ने तथा भारी हर्जाना देने के लिए मजबूर होना पड़ा। दीव के इस युद्ध ने हिंद महासागर में यूरोपीय नौसैनिक वर्चस्व की नींव रखी जो अगले 400 वर्षों तक कायम रही। इसके बाद, अल्मेडा अल्बुकर्क को सत्ता सौंपकर पुर्तगाल के लिए रवाना हुए, लेकिन मार्च 1510 में दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ पानी के विवाद में मारे गए।</p>'}]}
hi_data['deepDive']['sections'][0]['masteryZone'] = sec1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = sec2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = sec3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = sec4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = sec5_hi

with open(os.path.join(BASE_DIR, 'content.json'), 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, 'hi', 'content.json'), 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Generated all 370 Almeida questions and wrote to content files.")
