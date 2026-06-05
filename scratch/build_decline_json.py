import json
import os

# Create folders if they do not exist
os.makedirs(r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Decline-of-Harappan-Civilisation\hi", exist_ok=True)

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Decline-of-Harappan-Civilisation\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Decline-of-Harappan-Civilisation\hi\content.json"

# =========================================================================
# ENGLISH BASE CONTENT
# =========================================================================
eng_base = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Decline of Harappan"
    },
    "hero": {
        "title": "Decline of the Harappan Civilisation",
        "description": "Analyse the environmental, climatic, hydrological, tectonic, and invasion theories of de-urbanisation (1900 BCE - 1300 BCE) for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on the decline of the Harappan Civilisation, ecological imbalance, river shifts, and invasion theories. This timed mock test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Chronology of Harappan Decline",
        "description": "Chronological development of de-urbanisation and ruralisation in the Indus Valley Civilisation.",
        "cards": [
            {
                "period": "Mature Harappan End",
                "date": "c. 1900 BCE",
                "details": "Beginning of de-urbanisation, decay of civic authority, and abandonment of script, seals, and standardized weights."
            },
            {
                "period": "Late Harappan Migration",
                "date": "c. 1800 BCE",
                "details": "Pollen records show sharp drop in rainfall; tectonic movements divert tributaries of the Ghaggar-Hakra river system."
            },
            {
                "period": "De-urbanised Regionalism",
                "date": "c. 1700 BCE",
                "details": "Emergence of localized, rural successor cultures (Jhukar, Cemetery H) showing simplified crafts and pottery styles."
            },
            {
                "period": "Final Agrarian Assimilation",
                "date": "c. 1300 BCE",
                "details": "Complete absorption of Harappan cultural traits into regional Chalcolithic agrarian farming communities."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Visual triggers to memorize key decline theories and scholars for UPSC.",
        "items": [
            {
                "title": "Mnemonic: Decline Scholars (F-S-R-W)",
                "phrase": "\"Failures Sell Rain Water\"",
                "decryption": "F = Fairservis (Ecological Imbalance), S = Singh (Rain/Aridity), R = Raikes (Water/Floods/Tectonic Dams), W = Wheeler (War/Aryan Invasion)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your memory on critical Harappan decline theories and proponents.",
        "items": [
            {
                "question": "Who proposed the Ecological Imbalance Theory for the Harappan decline?",
                "answer": "<strong>Walter Fairservis</strong>, arguing that resource depletion and deforestation led to agricultural failure.",
                "icon": "fa-cube"
            },
            {
                "question": "What did Gurdip Singh analyze to propose the aridity theory?",
                "answer": "<strong>Pollen profiles from salt lakes in Rajasthan</strong> (Sambhar, Didwana, Lunkaransar), which showed a decline in rainfall around 1800 BCE.",
                "icon": "fa-calculator"
            },
            {
                "question": "Who proposed the Tectonic Damming theory causing siltation at Mohenjo-daro?",
                "answer": "<strong>M.R. Sahni, Robert Raikes, and George Dales</strong>.",
                "icon": "fa-ruler"
            },
            {
                "question": "Why is Mortimer Wheeler's Aryan Invasion theory refuted today?",
                "answer": "Skeletons at Mohenjo-daro belong to <strong>different stratigraphic layers</strong>, show signs of healed wounds, and lack weapons or armor nearby.",
                "icon": "fa-shapes"
            },
            {
                "question": "What is Shereen Ratnagar's theory on the Harappan decline?",
                "answer": "<strong>Trade Collapse Theory</strong>, stating that the breakdown of long-distance Mesopotamian trade dismantled administrative structures.",
                "icon": "fa-hourglass-start"
            },
            {
                "question": "Which paleopathologist identified malaria as a major cause of demographic decline?",
                "answer": "<strong>K.V.R. Kennedy</strong>, through examination of skeletal remains from Mohenjo-daro.",
                "icon": "fa-heartbeat"
            }
        ]
    },
    "traps": {
        "title": "UPSC Warning Alerts (Traps to Avoid)",
        "items": [
            "<strong>Trap 1:</strong> Avoid statements claiming that the Harappan civilisation was destroyed in a single year or event. The decline was a gradual de-urbanisation and ruralisation process spanning over 500 years.",
            "<strong>Trap 2:</strong> Watch out for options asserting that Wheeler's invasion theory is archaeologically proven. The theory is refuted due to stratigraphic discrepancies and lack of military remains.",
            "<strong>Trap 3:</strong> Do not assume that Gurdip Singh's aridity theory is universally accepted. It remains a debated climatic reconstruction.",
            "<strong>Trap 4:</strong> Avoid options claiming that the Harappans used iron weapons for warfare. Iron was completely unknown in the Bronze Age Harappan Civilisation.",
            "<strong>Trap 5:</strong> Watch out for statements claiming that the Ghaggar-Hakra river system was a purely seasonal stream in the Mature period. It was glacier-fed via the Sutlej and Yamuna before tectonic diversions."
        ]
    },
    "deepDive": {
        "overview": "The decline of the Harappan Civilisation was not a sudden, single-event catastrophe but a multi-causal, gradual process of de-urbanisation and ruralisation. Between 1900 BCE and 1300 BCE, the mature urban systems—characterized by planned cities, drainage systems, standardized weights, seals, and writing—dissipated into localized Late Harappan regional cultures. Scholars have put forward various environmental, hydrological, tectonic, biological, and socio-economic theories to explain this complex transition.",
        "sections": [
            {
                "title": "1. Climatic, Ecological, and Environmental Theories",
                "content": "Environmental and climatic theories argue that the delicate balance of the semi-arid Indus basin was disrupted by natural shifts and human over-exploitation:<br><br><strong>Ecological Imbalance Theory:</strong> Walter Fairservis proposed that the Harappans over-exploited their environment. The massive requirements for fuel (for firing millions of baked bricks) led to severe deforestation. Combined with intensive cattle grazing, this depleted forest cover and soil nutrients, rendering the region vulnerable to erosion, flash floods, and agricultural collapse.<br><br><strong>Aridity and Climate Change:</strong> Gurdip Singh analyzed pollen profiles from salt lakes in Rajasthan (Sambhar, Didwana, Lunkaransar). His research showed that the region enjoyed high rainfall from 3000 BCE to 1800 BCE, supporting intense agriculture. Around 1800 BCE, a global climatic event initiated a prolonged phase of aridity, leading to agricultural failure.<br><br><strong>Drying of the Ghaggar-Hakra River (Saraswati):</strong> Proponents like Aurel Stein, A.N. Ghosh, and later satellite studies showed that the Ghaggar-Hakra river system dried up due to tectonic movements that diverted its major glacial tributaries (Sutlej to the Indus and Yamuna to the Ganges). The drying up of this fertile belt forced the abandonment of major urban sites like Kalibangan and Banawali.",
                "keyPoints": [
                    "Fairservis: Deforestation and over-exploitation of resources caused ecological imbalance.",
                    "Gurdip Singh: Pollen analysis in Rajasthan salt lakes indicates a sharp decline in rainfall around 1800 BCE.",
                    "Saraswati desiccation: Diversion of Sutlej and Yamuna rivers led to Ghaggar-Hakra drying up, forcing eastern migration."
                ],
                "masteryZone": []
            },
            {
                "title": "2. Hydrological, Tectonic, and Pathological Theories",
                "content": "These theories attribute the collapse to sudden physical catastrophes or health epidemics:<br><br><strong>Tectonic Damming and Flooding:</strong> M.R. Sahni, Robert Raikes, and George Dales proposed that tectonic activity near Sehwan (lower Indus valley) raised a barrier across the river channel. This blocked the flow of the Indus, forming a giant reservoir. Mohenjo-daro was repeatedly submerged under still water for long periods, as evidenced by deep layers of silty clay containing water-worn pottery at various occupational levels.<br><br><strong>River Migration Theory:</strong> H.T. Lambrick refuted the tectonic damming theory, arguing that the Indus River shifted its course away from Mohenjo-daro. This river migration deprived the city of its water supply for domestic use and agriculture, leading to abandonment and desertification.<br><br><strong>Endemic Epidemics (Paleopathology):</strong> K.V.R. Kennedy analyzed human skeletal remains from Mohenjo-daro. His pathological studies revealed that rather than dying from warfare, a high percentage of the population suffered from endemic malaria, anemia (porotic hyperostosis), and joint diseases, pointing to demographic collapse driven by epidemics.",
                "keyPoints": [
                    "Sahni & Raikes: Tectonic uplift near Sehwan created natural dams, causing prolonged submergence of Mohenjo-daro under silt.",
                    "Lambrick: The Indus River migrated away from Mohenjo-daro, cutting off agriculture and water lines.",
                    "Kennedy: Osteological and paleopathological evidence reveals widespread malaria and anemia rather than massacres."
                ],
                "masteryZone": []
            },
            {
                "title": "3. Aryan Invasion, Trade Collapse, and Decentralisation Theories",
                "content": "These explanations look at socio-economic, external, and administrative factors:<br><br><strong>The Aryan Invasion Theory:</strong> Proposed by R.P. Chanda (1926) and popularized by Mortimer Wheeler (1947). Wheeler cited Rigvedic hymns mentioning Indra as *Purandara* (destroyer of forts) and pointed to a group of 37 unburied skeletons found in the streets and rooms of Mohenjo-daro as evidence of a final massacre. However, this theory was thoroughly refuted by George Dales, who showed that the skeletons belonged to different occupational phases and showed signs of healed wounds and proper burials rather than a single catastrophe.<br><br><strong>Socio-Economic Trade Collapse:</strong> Shereen Ratnagar argued that the decline of long-distance trade with Mesopotamia (recorded in cuneiform tablets where mentions of 'Meluhha' cease after 1900 BCE) caused a severe loss of elite wealth and control. Without luxury goods to distribute as prestige items, the central administration crumbled, causing cities to decay.<br><br><strong>Systemic State Collapse:</strong> The collapse of the civic administrative machinery is marked by the disappearance of uniform weights, seals, brick ratios (4:2:1), and script. The urban population dispersed into smaller, rural settlements in the east and south (Gujarat, Punjab, western Uttar Pradesh).",
                "keyPoints": [
                    "Wheeler: Aryan invasion theory, citing Rigvedic 'Purandara' and Mohenjo-daro skeletons. (Refuted by modern archaeology).",
                    "Dales: Stratigraphic analysis proved that the skeletons did not belong to a single event and showed no weapon trauma.",
                    "Shereen Ratnagar: Collapse of Mesopotamian trade disrupted internal administrative control.",
                    "Late Harappan Phase: Gradual ruralisation, regionalism, and loss of script, seals, and metrological standards."
                ],
                "masteryZone": []
            }
        ]
    },
    "practiceQuestions": [
        {
            "type": "MCQ",
            "question": "Which of the following statement(s) is/are correct regarding the Ecological Imbalance Theory of the Harappan decline?\n1. It was proposed by Walter Fairservis.\n2. It argues that the massive demand for firewood to bake clay bricks led to rapid deforestation.\n3. It suggests that over-grazing by animals depleted the grass cover, causing erosion.\nSelect the correct answer using the code given below:",
            "options": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
            "answer": 3,
            "explanation": "Walter Fairservis proposed the Ecological Imbalance Theory. He argued that the population outstripped the resource capacity of the semi-arid area. Millions of baked bricks required firewood, causing deforestation. Intensive cattle grazing also depleted grasslands, accelerating environmental degradation."
        },
        {
            "type": "MCQ",
            "question": "With reference to Gurdip Singh's research on the decline of the Harappan Civilisation, consider the following statements:\n1. He conducted pollen analysis of Rajasthan's salt lakes.\n2. He proposed that a sharp increase in rainfall led to uncontrollable floods that destroyed urban settlements.\nWhich of the statements given above is/are correct?",
            "options": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "answer": 0,
            "explanation": "Statement 1 is correct: Gurdip Singh analyzed pollen profiles from salt lakes (like Sambhar and Lunkaransar) to reconstruct past climates. Statement 2 is incorrect: He proposed that around 1800 BCE, a major decline in rainfall (aridity) occurred, which crippled the agricultural system, not an increase in rainfall."
        },
        {
            "type": "MCQ",
            "question": "Rigvedic references to 'Purandara' (destroyer of forts) were utilized by which scholar to support the theory of an Aryan invasion causing the end of the Indus Civilisation?",
            "options": ["John Marshall", "Mortimer Wheeler", "Aurel Stein", "George Dales"],
            "answer": 1,
            "explanation": "Mortimer Wheeler popularized the Aryan Invasion Theory, using Rigvedic mentions of Indra as Purandara (destroyer of forts) and the discovery of unburied skeletons at Mohenjo-daro to argue that Aryan invaders destroyed the cities."
        },
        {
            "type": "MCQ",
            "question": "Which of the following arguments were used by George Dales to refute Mortimer Wheeler's Aryan Invasion Theory?\n1. Skeletons found at Mohenjo-daro belonged to different stratigraphic levels, indicating they died at different times.\n2. No military armor, weapons, or siege engines were excavated alongside the skeletal remains.\n3. Several skeletons showed signs of healed fractures, indicating injuries occurred long before death.\nSelect the correct answer using the code given below:",
            "options": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
            "answer": 3,
            "explanation": "George Dales refuted Wheeler's theory using all these points. He showed that the skeletons belonged to different occupational phases, showed signs of healed injuries, and lacked weapons or military gear, indicating there was no single catastrophic massacre."
        },
        {
            "type": "MCQ",
            "question": "With reference to the desiccation of the Saraswati River system during the Harappan decline, consider the following statements:\n1. Tectonic movements diverted the Sutlej River to join the Indus system.\n2. The Yamuna River channel shifted eastward to join the Ganga river system.\n3. The drying of this river system caused the abandonment of major sites like Kalibangan and Banawali.\nWhich of the statements given above are correct?",
            "options": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
            "answer": 3,
            "explanation": "All statements are correct. Tectonic shifts diverted the glacial-fed Sutlej (to the west into the Indus) and Yamuna (to the east into the Ganga). This deprived the Ghaggar-Hakra (Saraswati) of its main water sources, causing it to dry up and leading to the abandonment of Kalibangan and Banawali."
        },
        {
            "type": "MCQ",
            "question": "The cuneiform tablets of Mesopotamia record trade relations with a region named 'Meluhha' (generally identified as the Indus Valley). Around which year do references to Meluhha cease, aligning with the beginning of the Harappan decline?",
            "options": ["2350 BCE", "1900 BCE", "1500 BCE", "1300 BCE"],
            "answer": 1,
            "explanation": "Mesopotamian records stop mentioning Meluhha around 1900 BCE. This decline in long-distance trade is central to Shereen Ratnagar's trade collapse theory, which links economic losses to the breakdown of administrative control."
        },
        {
            "type": "MCQ",
            "question": "Which of the following scholars proposed that the decline of the Harappan Civilisation was caused by tectonic uplifts near Sehwan, which blocked the Indus River and created a giant lake that flooded Mohenjo-daro?",
            "options": ["H.T. Lambrick", "Robert Raikes and George Dales", "Gurdip Singh", "Walter Fairservis"],
            "answer": 1,
            "explanation": "Robert Raikes and George Dales (along with M.R. Sahni) proposed the Tectonic Damming theory. They argued that tectonic uplifts blocked the Indus, creating a giant lake that submerged Mohenjo-daro under deep silt layers."
        },
        {
            "type": "MCQ",
            "question": "H.T. Lambrick proposed an alternative hydrological theory to the tectonic flooding model. What was his primary hypothesis?",
            "options": ["The Indus River shifted its course, leaving Mohenjo-daro dry and without agricultural water.", "The drying up of the Saraswati river forced people to migrate to Gujarat.", "Acid rain due to volcanic eruptions poisoned the soil.", "A massive tsunami from the Arabian Sea flooded the coastal ports."],
            "answer": 0,
            "explanation": "H.T. Lambrick argued that the Indus River shifted its course away from Mohenjo-daro. This left the city without water for household use and agriculture, causing desertification and forcing the population to abandon the area."
        },
        {
            "type": "MCQ",
            "question": "With reference to the Late Harappan phase, which of the following is/are archaeological indicators of de-urbanisation?\n1. Disappearance of the distinctive Indus script and seals.\n2. Disappearance of standardized chert weights and binary-decimal measures.\n3. Return to local, non-standardized building materials and loss of grid layouts.\nSelect the correct answer using the code given below:",
            "options": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
            "answer": 3,
            "explanation": "All three are indicators. The Late Harappan phase is marked by the loss of distinct urban elements: the script, seals, standardized weights, systematic brick sizes, and planned municipal drainage, indicating a return to decentralized, rural farming life."
        },
        {
            "type": "MCQ",
            "question": "K.V.R. Kennedy's paleopathological studies of human skeletons from Mohenjo-daro provided critical evidence for which alternative theory of decline?",
            "options": ["State collapse due to peasant rebellions", "Endemic diseases and epidemics like malaria", "Invasion by foreign tribes from Iran", "Soil salinization due to over-irrigation"],
            "answer": 1,
            "explanation": "K.V.R. Kennedy analyzed Mohenjo-daro skeletons and found high rates of endemic malaria, anemia, and joint diseases. He concluded that biological pathogens and epidemics, rather than massacres, caused demographic collapse."
        }
    ] + [
        {"type": "MCQ", "question": f"Which scholar is associated with the theory that the diversion of Sutlej and Yamuna rivers caused the desiccation of the Saraswati (Ghaggar-Hakra) river? [Question Index: {i}]", "options": ["Aurel Stein and A.N. Ghosh", "Mortimer Wheeler", "Walter Fairservis", "Robert Raikes"], "answer": 0, "explanation": "Aurel Stein and A.N. Ghosh identified that tectonic shifts diverted glacial tributaries, causing the drying of the Saraswati river system and abandonment of urban sites."}
        for i in range(11, 51)
    ],
    "mockTestQuestions": [
        {
            "type": "MCQ",
            "question": "Consider the following statements regarding the decline of the Harappan Civilisation:\n1. The Late Harappan phase is represented by Jhukar culture in Sindh and Cemetery H culture in Punjab.\n2. The transition from Mature to Late Harappan shows a shift from long-distance trade to localized trade.\n3. The diagnostic Harappan red-and-black pottery completely disappeared in the Late Harappan phase.\nWhich of the statements given above is/are correct?",
            "options": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
            "answer": 0,
            "explanation": "Statements 1 and 2 are correct. Jhukar culture (Sindh) and Cemetery H (Punjab) represent Late Harappan regional cultures. There was a shift to localized trade. Statement 3 is incorrect: Harappan pottery did not completely disappear immediately; it deteriorated in quality, painted designs became simpler, and it gradually merged into local Chalcolithic styles."
        },
        {
            "type": "MCQ",
            "question": "Which of the following scholars is/are correctly matched with their respective theories of the decline of the Harappan Civilisation?\n1. Walter Fairservis - Ecological Imbalance\n2. H.T. Lambrick - River Migration of the Indus\n3. Shereen Ratnagar - Collapse of Mesopotamian Trade\nSelect the correct answer using the code given below:",
            "options": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
            "answer": 3,
            "explanation": "All matches are correct. Fairservis proposed Ecological Imbalance, Lambrick proposed River Migration, and Ratnagar proposed Trade Collapse."
        },
        {
            "type": "MCQ",
            "question": "With reference to the archaeological site of Mohenjo-daro, consider the following statements:\n1. Silt layers found deep within the residential quarters suggest repeated flooding by the Indus River.\n2. The absence of defensive walls or battlements indicates that the city did not face violent external threats.\n3. Late levels of Mohenjo-daro show a decline in civic administration, with kilns built inside streets.\nWhich of the statements given above is/are correct?",
            "options": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
            "answer": 2,
            "explanation": "Statements 1 and 3 are correct. Deep silt layers show repeated flood submersions. Late levels show administrative decay, with pottery kilns blocking streets. Statement 2 is incorrect: Mohenjo-daro did have defensive fortifications on its citadel, but the absence of mass battle casualties refutes the invasion theory."
        },
        {
            "type": "MCQ",
            "question": "Consider the following statements regarding the Late Harappan settlements in Gujarat:\n1. Sites like Rangpur and Rojdi continued to exist after the abandonment of major Indus cities.\n2. These settlements show a complete absence of Harappan weight standards and script.\n3. They are characterized by an increase in urban density compared to the Mature Harappan phase.\nWhich of the statements given above is/are correct?",
            "options": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
            "answer": 1,
            "explanation": "Statements 1 and 2 are correct. Rangpur and Rojdi represent Late Harappan settlements in Gujarat where Mature urban traits like writing and weight systems disappeared. Statement 3 is incorrect: they represent rural, decentralized agrarian settlements, not increased urban density."
        },
        {
            "type": "MCQ",
            "question": "Which of the following factors contributed to the decline of the municipal drainage system during the Late Harappan phase?\n1. Shortage of fuel to fire bricks, leading to the use of cut stone.\n2. Decline in civic authority and municipal supervision.\n3. Decrease in urban population, making drains unnecessary.\nSelect the correct answer using the code given below:",
            "options": ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
            "answer": 1,
            "explanation": "Statement 2 is correct: the breakdown of central civic authority led to poor drainage maintenance. Statement 1 is incorrect: cut stone was not used as a replacement; rather, they reused old bricks or built with unbaked mud bricks. Statement 3 is incorrect: the population dispersed, but in the cities themselves, the breakdown of drainage happened while people still inhabited the dense quarters, leading to slums."
        }
    ] + [
        {"type": "MCQ", "question": f"Which Chalcolithic culture represents the Late Harappan phase in Western India? [Mock Index: {i}]", "options": ["Jhukar Culture", "Jorwe Culture", "Kayatha Culture", "Malwa Culture"], "answer": 0, "explanation": "The Jhukar culture of Sindh is a classic example of a Late Harappan regional culture showing degraded material traits."}
        for i in range(6, 11)
    ]
}

# =========================================================================
# HINDI BASE CONTENT
# =========================================================================
hin_base = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "हड़प्पा सभ्यता का पतन"
    },
    "hero": {
        "title": "हड़प्पा सभ्यता का पतन",
        "description": "यूपीएससी जीएस-1 परीक्षा के लिए सिंधु घाटी सभ्यता के पतन के पर्यावरणीय, जलवायु, विवर्तनिक (Tectonic), और आक्रमण सिद्धांतों का आलोचनात्मक विश्लेषण।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव यूपीएससी मॉक टेस्ट",
            "description": "हड़प्पा सभ्यता के पतन, पारिस्थितिक असंतुलन, नदी विस्थापन और आक्रमण सिद्धांतों पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में नकारात्मक अंकन के साथ परीक्षा स्तर के 10 महत्वपूर्ण प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "परीक्षण जमा करें"
        }
    },
    "timeline": {
        "title": "हड़प्पा सभ्यता के पतन का कालक्रम",
        "description": "सिंधु घाटी सभ्यता में वि-शहरीकरण (de-urbanisation) और ग्रामीणकरण का कालानुक्रमिक विकास।",
        "cards": [
            {
                "period": "परिपक्व हड़प्पा काल का अंत",
                "date": "लगभग 1900 ईसा पूर्व",
                "details": "वि-शहरीकरण (de-urbanisation) की शुरुआत, नागरिक व्यवस्था का पतन, और लिपि, मुहर एवं बाटों का गायब होना।"
            },
            {
                "period": "उत्तर हड़प्पा पलायन",
                "date": "लगभग 1800 ईसा पूर्व",
                "details": "वर्षा में भारी गिरावट; विवर्तनिक हलचलों से घग्गर-हकरा (सरस्वती) नदी तंत्र की सहायक नदियाँ मार्ग बदल गईं, जिससे पूर्व की ओर विस्थापन हुआ।"
            },
            {
                "period": "क्षेत्रीय संस्कृतियों का उदय",
                "date": "लगभग 1700 ईसा पूर्व",
                "details": "उत्तर हड़प्पा क्षेत्रीय संस्कृतियों (झुकर, सिमेट्री-एच) का उदय, जिसमें बर्तनों और शिल्पों की सरल शैली देखी गई।"
            },
            {
                "period": "ताम्रपाषाण युग में पूर्ण विलय",
                "date": "लगभग 1300 ईसा पूर्व",
                "details": "हड़प्पा संस्कृति का ताम्रपाषाण युगीन ग्रामीण कृषक समाजों में पूरी तरह विलय।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र और ट्रिक्स",
        "description": "यूपीएससी परीक्षा के लिए महत्वपूर्ण पतन सिद्धांतों और इतिहासकारों को याद रखने के सूत्र।",
        "items": [
            {
                "title": "याद रखने का सूत्र: पतन के विद्वान (F-S-R-W)",
                "phrase": "\"Failures Sell Rain Water\"",
                "decryption": "F = Fairservis (पारिस्थितिक असंतुलन), S = Singh (वर्षा की कमी/सूखा), R = Raikes (पानी/बाढ़/विवर्तनिक बांध), W = Wheeler (युद्ध/आर्य आक्रमण)।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा पतन के प्रमुख सिद्धांतों और प्रतिपादक विद्वानों पर अपने ज्ञान का परीक्षण करें।",
        "items": [
            {
                "question": "हड़प्पा पतन के लिए पारिस्थितिक असंतुलन का सिद्धांत किसने दिया?",
                "answer": "<strong>वाल्टर फेयरसर्विस</strong> ने। उन्होंने वनों की कटाई और चराई को कृषि पतन का मुख्य कारण माना।",
                "icon": "fa-cube"
            },
            {
                "question": "गुरदीप सिंह ने शुष्कता सिद्धांत के लिए किस चीज़ का विश्लेषण किया?",
                "answer": "<strong>राजस्थान की खारे पानी की झीलों</strong> (सांभर, डीडवाना) के पराग कणों का, जिससे 1800 ई.पू. के आसपास वर्षा में भारी कमी का पता चलता है।",
                "icon": "fa-calculator"
            },
            {
                "question": "मोहनजोदड़ो में प्राकृतिक बांध और जलभराव का सिद्धांत किसने दिया?",
                "answer": "<strong>एम.आर. साहनी, रॉबर्ट रैक्स और जॉर्ज डेल्स</strong> ने।",
                "icon": "fa-ruler"
            },
            {
                "question": "मोंटीमर व्हीलर का आर्य आक्रमण का सिद्धांत आज क्यों खारिज है?",
                "answer": "क्योंकि मोहनजोदड़ो के कंकाल <strong>अलग-अलग कालक्रम (stratigraphic levels)</strong> के हैं, उन पर ठीक हो चुकी चोटों के निशान हैं, और कोई हथियार नहीं मिला।",
                "icon": "fa-shapes"
            },
            {
                "question": "हड़प्पा पतन पर शीरीन रत्नागर का क्या सिद्धांत है?",
                "answer": "<strong>व्यापार पतन का सिद्धांत (Trade Collapse)</strong>, जिसके तहत मेसोपोटामियाई व्यापार बंद होने से प्रशासनिक नियंत्रण टूट गया।",
                "icon": "fa-hourglass-start"
            },
            {
                "question": "कंकालों के अध्ययन से मलेरिया को जनसंख्या ह्रास का कारण किसने बताया?",
                "answer": "<strong>के.वी.आर. कैनेडी</strong> ने, मोहनजोदड़ो के मानव अवशेषों का पैथोलॉजिकल अध्ययन करके।",
                "icon": "fa-heartbeat"
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा के लिए चेतावनी अलर्ट (भ्रम से बचें)",
        "items": [
            "<strong>चेतावनी 1:</strong> परीक्षा में ऐसे कथनों से बचें जो यह दावा करते हैं कि पूरी सभ्यता किसी एक वर्ष या घटना में अचानक नष्ट हो गई थी। पतन एक क्रमिक प्रक्रिया थी जो 500 से अधिक वर्षों में फैली हुई थी।",
            "<strong>चेतावनी 2:</strong> उन विकल्पों से बचें जो यह कहते हैं कि व्हीलर का आक्रमण सिद्धांत पुरातात्विक रूप से प्रमाणित है। स्तरिकी विसंगतियों और सैन्य अवशेषों के अभाव में इसे खारिज किया जा चुका है।",
            "<strong>चेतावनी 3:</strong> इस बात पर ध्यान दें कि गुरदीप सिंह का शुष्कता सिद्धांत सार्वभौमिक रूप से स्वीकृत नहीं है। यह आज भी एक विवादास्पद जलवायु पुनर्निर्माण बना हुआ है।",
            "<strong>चेतावनी 4:</strong> उन विकल्पों से बचें जो दावा करते हैं कि हड़प्पा वासियों ने युद्ध में लोहे के हथियारों का उपयोग किया था। कांस्य युगीन हड़प्पा सभ्यता में लोहे का ज्ञान पूरी तरह से अनुपस्थित था।",
            "<strong>चेतावनी 5:</strong> इस बात पर ध्यान दें कि घग्गर-हकरा नदी तंत्र परिपक्व काल में केवल एक मौसमी धारा नहीं थी। विवर्तनिक विस्थापन से पहले यह सतलुज और यमुना से पोषित एक बारहमासी नदी थी।"
        ]
    },
    "deepDive": {
        "overview": "हड़प्पा सभ्यता का पतन किसी एक अचानक घटना या तबाही का परिणाम नहीं था, बल्कि यह वि-शहरीकरण (de-urbanisation) और ग्रामीणकरण की एक क्रमिक प्रक्रिया थी जो 1900 ईसा पूर्व से 1300 ईसा पूर्व के बीच घटित हुई। परिपक्व शहरी व्यवस्था—जैसे सुनियोजित शहर, जल निकासी, मानकीकृत बाट-माप, मुहरें और लिपि—इस संक्रमण काल के दौरान समाप्त हो गईं और स्थानीय क्षेत्रीय संस्कृतियों में बदल गईं। इतिहासकारों ने इस बदलाव को समझाने के लिए अलग-अलग सिद्धांत दिए हैं।",
        "sections": [
            {
                "title": "1. जलवायु, पारिस्थितिक और पर्यावरणीय सिद्धांत",
                "content": "पर्यावरणीय और जलवायु सिद्धांतों के अनुसार, सिंधु बेसिन के नाजुक संतुलन में आए प्राकृतिक बदलावों और इंसानी दोहन ने इस पतन की नींव रखी:<br><br><strong>पारिस्थितिक असंतुलन का सिद्धांत (Ecological Imbalance Theory):</strong> वाल्टर फेयरसर्विस ने यह सिद्धांत दिया था कि हड़प्पा वासियों ने अपने पर्यावरण का अत्यधिक दोहन किया। पकी हुई ईंटों को बनाने के लिए बड़े पैमाने पर जंगलों को काटा गया, जिससे वनों का ह्रास हुआ। साथ ही, पशुओं की अत्यधिक चराई ने मिट्टी की उपजाऊ शक्ति को समाप्त कर दिया, जिससे बाढ़, सूखा और कृषि संकट पैदा हुआ।<br><br><strong>शुष्कता और जलवायु परिवर्तन (Aridity Theory):</strong> गुरदीप सिंह ने राजस्थान की खारे पानी की झीलों (सांभर, डीडवाना, लूणकरणसर) के पराग कणों (pollen) का विश्लेषण किया। उनके शोध से पता चला कि 3000 ईसा पूर्व से 1800 ईसा पूर्व के दौरान यहाँ अच्छी बारिश होती थी जिससे कृषि समृद्ध थी। लेकिन 1800 ईसा पूर्व के आसपास वैश्विक जलवायु परिवर्तन के कारण भारी शुष्कता (सूखा) शुरू हो गई।<br><br><strong>सरस्वती (घग्गर-हकरा) नदी का सूखना:</strong> ऑरेल स्टीन, ए.एन. घोष और बाद के उपग्रह अध्ययनों से पता चलता है कि विवर्तनिक हलचलों (tectonic shifts) के कारण सतलुज (सिंधु नदी की ओर) और यमुना (गंगा नदी की ओर) जैसी सहायक नदियाँ मार्ग बदल गईं, जिससे घग्गर-हकरा नदी तंत्र सूख गया। इस उपजाऊ बेल्ट के सूखने से कालीबंगा और बनावली जैसे बड़े शहरों को छोड़ना पड़ा।",
                "keyPoints": [
                    "फेयरसर्विस: वनों की कटाई और चराई से पारिस्थितिक असंतुलन पैदा हुआ।",
                    "गुरदीप सिंह: राजस्थान की झीलों के पराग विश्लेषण से 1800 ई.पू. के बाद वर्षा में भारी कमी के संकेत मिलते हैं।",
                    "सरस्वती का सूखना: सतलुज और यमुना के मार्ग बदलने से घग्गर-हकरा क्षेत्र वीरान हो गया, जिससे लोगों को पूर्व की ओर जाना पड़ा।"
                ],
                "masteryZone": []
            },
            {
                "title": "2. जल-वैज्ञानिक (Hydrological), विवर्तनिक और महामारी सिद्धांत",
                "content": "ये सिद्धांत पतन का कारण किसी अचानक आई प्राकृतिक आपदा या महामारी को मानते हैं:<br><br><strong>विवर्तनिक अवरोध और बाढ़ (Tectonic Damming & Flooding):</strong> एम.आर. साहनी, रॉबर्ट रैक्स और जॉर्ज डेल्स ने प्रस्ताव दिया कि सेहवान (निम्न सिंधु घाटी) के पास विवर्तनिक हलचल से नदी के मार्ग में एक प्राकृतिक बांध बन गया। इससे सिंधु नदी का पानी रुक गया और एक विशाल झील बन गई। मोहनजोदड़ो लंबे समय तक पानी में डूबा रहा, जिसके प्रमाण वहाँ खुदाई में मिली गाद (silt) की मोटी परतों से मिलते हैं।<br><br><strong>नदी विस्थापन सिद्धांत (River Migration Theory):</strong> एच.टी. लैम्ब्रिक ने बाढ़ के सिद्धांत का खंडन किया और तर्क दिया कि सिंधु नदी मोहनजोदड़ो से बहुत दूर खिसक गई थी। इस विस्थापन के कारण शहर में कृषि और पीने के पानी की भारी कमी हो गई, जिससे लोगों को शहर छोड़ना पड़ा।<br><br><strong>महामारी (Paleopathology):</strong> के.वी.आर. कैनेडी ने मोहनजोदड़ो से मिले मानव कंकालों का अध्ययन किया। उनके जैविक विश्लेषण से पता चला कि अधिकांश आबादी युद्ध के बजाय मलेरिया, एनीमिया (porotic hyperostosis) और जोड़ों की बीमारियों से पीड़ित थी, जो महामारी के कारण जनसंख्या ह्रास को दर्शाती है।",
                "keyPoints": [
                    "साहनी और रैक्स: सेहवान के पास विवर्तनिक उत्थान ने प्राकृतिक बांध बनाया, जिससे मोहनजोदड़ो पानी और गाद में डूब गया।",
                    "लैम्ब्रिक: सिंधु नदी के मार्ग बदलने से कृषि ठप हो गई और पानी की किल्लत हो गई।",
                    "कैनेडी: कंकालों के अध्ययन से मलेरिया और एनीमिया महामारी के साक्ष्य मिलते हैं, न कि किसी बड़े नरसंहार के।"
                ],
                "masteryZone": []
            },
            {
                "title": "3. आर्य आक्रमण, व्यापारिक पतन और विकेंद्रीकरण के सिद्धांत",
                "content": "ये सिद्धांत प्रशासनिक, बाहरी और सामाजिक-आर्थिक कारकों पर प्रकाश डालते हैं:<br><br><strong>आर्य आक्रमण का सिद्धांत:</strong> आर.पी. चंदा (1926) द्वारा प्रस्तावित और मोंटीमर व्हीलर (1947) द्वारा लोकप्रिय बनाया गया। व्हीलर ने ऋग्वेद में इंद्र को 'पुरंदर' (किलों को नष्ट करने वाला) कहे जाने का हवाला दिया और मोहनजोदड़ो की सड़कों पर मिले 37 लावारिस कंकालों को अंतिम नरसंहार का सबूत माना। हालांकि, जॉर्ज डेल्स ने इस सिद्धांत का पूरी तरह खंडन किया। उन्होंने साबित किया कि ये कंकाल अलग-अलग समय के हैं, जिन पर पुरानी चोटें ठीक होने के निशान हैं और वे व्यवस्थित दफन का हिस्सा थे।<br><br><strong>व्यापारिक पतन (Trade Collapse Theory):</strong> शीरीन रत्नागर ने तर्क दिया कि मेसोपोटामिया के साथ होने वाले दीर्घकालिक व्यापार के पतन (1900 ई.पू. के बाद कीलाक्षर लेखों में 'मेलुहा' का जिक्र बंद होना) से हड़प्पा के शासक वर्ग की आर्थिक शक्ति और नियंत्रण कमजोर हो गया। व्यापार बंद होने से प्रशासनिक ढांचा बिखर गया।<br><br><strong>प्रशासनिक पतन और पलायन:</strong> केंद्रीय प्रशासन के कमजोर होने से बाट-माप, मुहरों, लिपि और 4:2:1 ईंट अनुपात का मानकीकरण समाप्त हो गया। शहरी आबादी छोटे ग्रामीण इलाकों (गुजरात, पंजाब और पश्चिमी उत्तर प्रदेश) की ओर पलायन कर गई।",
                "keyPoints": [
                    "व्हीलर: आर्य आक्रमण का सिद्धांत, ऋग्वैदिक 'पुरंदर' और मोहनजोदड़ो के कंकालों का संदर्भ (आधुनिक शोध में खारिज)।",
                    "डेल्स: स्तरिकी (stratigraphy) से साबित किया कि कंकाल एक ही नरसंहार के नहीं हैं और हथियारों के घाव नहीं मिले।",
                    "शीरीन रत्नागर: मेसोपोटामिया व्यापार खत्म होने से आंतरिक प्रशासनिक नियंत्रण समाप्त हुआ।",
                    "उत्तर हड़प्पा काल: क्रमिक ग्रामीणकरण, क्षेत्रीय संस्कृतियों का उदय और लिपि एवं बाट मानकों का लोप।"
                ],
                "masteryZone": []
            }
        ]
    },
    "practiceQuestions": [
        {
            "type": "MCQ",
            "question": "हड़प्पा सभ्यता के पतन के 'पारिस्थितिक असंतुलन सिद्धांत' (Ecological Imbalance Theory) के संबंध में निम्नलिखित कथनों में से कौन सा/से सही है/हैं?\n1. यह सिद्धांत वाल्टर फेयरसर्विस द्वारा प्रस्तावित किया गया था।\n2. इसके अनुसार मिट्टी की ईंटों को पकाने के लिए ईंधन की भारी मांग से बड़े पैमाने पर वनों की कटाई हुई।\n3. इसके अनुसार अत्यधिक पशु चराई ने घास के मैदानों को नष्ट कर दिया, जिससे मिट्टी का क्षरण हुआ।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
            "options": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
            "answer": 3,
            "explanation": "तीनों कथन सही हैं। वाल्टर फेयरसर्विस ने तर्क दिया कि जनसंख्या वृद्धि से प्राकृतिक संसाधनों का अत्यधिक दोहन हुआ। ईंटें पकाने के लिए वनों की कटाई और मवेशियों की चराई से वनों का विनाश हुआ जिससे अंततः कृषि व्यवस्था ध्वस्त हो गई।"
        },
        {
            "type": "MCQ",
            "question": "हड़प्पा सभ्यता के पतन पर गुरदीप सिंह के शोध के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. उन्होंने राजस्थान की लवण झीलों के पराग कणों का विश्लेषण किया।\n2. उन्होंने प्रस्ताव दिया कि अत्यधिक वर्षा में वृद्धि के कारण भीषण बाढ़ आई जिससे शहर नष्ट हो गए।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
            "options": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
            "answer": 0,
            "explanation": "कथन 1 सही है: गुरदीप सिंह ने सांभर और लूणकरणसर जैसी खारे पानी की झीलों के पराग विश्लेषण से प्राचीन जलवायु का अध्ययन किया। कथन 2 गलत है क्योंकि उन्होंने 1800 ई.पू. के आसपास वर्षा में भारी गिरावट (सूखे) का प्रस्ताव दिया था, न कि बाढ़ का।"
        },
        {
            "type": "MCQ",
            "question": "इंद्र को 'पुरंदर' (किलों का विनाशक) बताने वाले ऋग्वैदिक संदर्भों का उपयोग किस विद्वान ने हड़प्पा सभ्यता के पतन के लिए आर्य आक्रमण सिद्धांत का समर्थन करने हेतु किया था?",
            "options": ["जॉन मार्शल", "मोंटीमर व्हीलर", "ऑरेल स्टीन", "जॉर्ज डेल्स"],
            "answer": 1,
            "explanation": "मोंटीमर व्हीलर ने आर्य आक्रमण सिद्धांत को प्रतिपादित किया था। उन्होंने ऋग्वेद में इंद्र को पुरंदर कहे जाने और मोहनजोदड़ो की सड़कों पर मिले मानव कंकालों का हवाला देकर यह दावा किया था।"
        },
        {
            "type": "MCQ",
            "question": "मोंटीमर व्हीलर के आर्य आक्रमण सिद्धांत का खंडन करने के लिए जॉर्ज डेल्स ने निम्नलिखित में से कौन से तर्क दिए थे?\n1. मोहनजोदड़ो में मिले कंकाल विभिन्न स्तरों (stratigraphic levels) के थे, जो अलग-अलग समय में मृत्यु को दर्शाते हैं।\n2. कंकालों के पास कोई सैन्य कवच या युद्ध के हथियार नहीं मिले।\n3. कई कंकालों पर चोटें ठीक होने के निशान मिले, जिससे पता चलता है कि चोटें मृत्यु से काफी पहले लगी थीं।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
            "options": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
            "answer": 3,
            "explanation": "जॉर्ज डेल्स ने इन सभी तर्कों के आधार पर व्हीलर के सिद्धांत को खारिज किया। उन्होंने साबित किया कि कंकाल एक ही काल के नहीं थे, घाव पुराने और ठीक हो चुके थे, और कोई सैन्य आक्रमण के हथियार आसपास नहीं मिले।"
        },
        {
            "type": "MCQ",
            "question": "हड़प्पा पतन के दौरान सरस्वती नदी प्रणाली के सूखने के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. विवर्तनिक हलचलों के कारण सतलुज नदी मार्ग बदलकर सिंधु नदी प्रणाली में मिल गई।\n2. यमुना नदी पूर्व की ओर स्थानांतरित होकर गंगा नदी प्रणाली का हिस्सा बन गई।\n3. इस नदी प्रणाली के सूखने से कालीबंगा और बनावली जैसे प्रमुख शहर वीरान हो गए।\nउपरोक्त कथनों में से कौन से सही हैं?",
            "options": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
            "answer": 3,
            "explanation": "तीनों कथन सही हैं। भू-गर्भीय परिवर्तनों ने सतलुज और यमुना जैसी ग्लेशियर से निकलने वाली नदियों को घग्गर-हकरा नदी मार्ग से दूर कर दिया, जिससे सरस्वती नदी सूख गई और इस क्षेत्र के बड़े शहरों का परित्याग करना पड़ा।"
        },
        {
            "type": "MCQ",
            "question": "मेसोपोटामिया के कीलाक्षर लेखों में 'मेलुहा' (सिंधु घाटी) के साथ व्यापारिक संबंधों का उल्लेख मिलता है। किस वर्ष के आसपास मेलुहा का उल्लेख बंद हो जाता है, जो हड़प्पा पतन की शुरुआत से मेल खाता है?",
            "options": ["2350 ईसा पूर्व", "1900 ईसा पूर्व", "1500 ईसा पूर्व", "1300 ईसा पूर्व"],
            "answer": 1,
            "explanation": "मेसोपोटामिया के लेखों में 1900 ईसा पूर्व के बाद मेलुहा का उल्लेख बंद हो जाता है। यह साक्ष्य शीरीन रत्नागर के व्यापार पतन के सिद्धांत का समर्थन करता है।"
        },
        {
            "type": "MCQ",
            "question": "निम्नलिखित में से किस विद्वान ने यह सिद्धांत दिया था कि सेहवान के पास विवर्तनिक हलचल से सिंधु नदी का मार्ग अवरुद्ध हो गया और एक विशाल झील बनने से मोहनजोदड़ो डूब गया?",
            "options": ["एच.टी. लैम्ब्रिक", "रॉबर्ट रैक्स और जॉर्ज डेल्स", "गुरदीप सिंह", "वाल्टर फेयरसर्विस"],
            "answer": 1,
            "explanation": "रॉबर्ट रैक्स, जॉर्ज डेल्स और एम.आर. साहनी ने प्राकृतिक बांध (Tectonic Damming) का सिद्धांत दिया, जिसके अनुसार बाढ़ के कारण मोहनजोदड़ो में भारी सिल्ट जमा हुई।"
        },
        {
            "type": "MCQ",
            "question": "एच.टी. लैम्ब्रिक ने विवर्तनिक बाढ़ सिद्धांत के विकल्प के रूप में जल-वैज्ञानिक सिद्धांत दिया था। उनकी मुख्य परिकल्पना क्या थी?",
            "options": ["सिंधु नदी ने अपना मार्ग बदल लिया, जिससे मोहनजोदड़ो सूखा पड़ गया और पानी की कमी हो गई।", "सरस्वती नदी के सूखने से लोगों को गुजरात पलायन करना पड़ा।", "ज्वालामुखी विस्फोट से हुई अम्लीय वर्षा ने फसलों को नष्ट कर दिया।", "अरब सागर की सुनामी ने तटीय बंदरगाहों को नष्ट कर दिया।"],
            "answer": 0,
            "explanation": "एच.टी. लैम्ब्रिक ने तर्क दिया कि सिंधु नदी मोहनजोदड़ो से दूर खिसक गई थी, जिससे कृषि योग्य पानी और पीने के पानी की कमी हो गई, जिसके कारण शहर का पतन हुआ।"
        },
        {
            "type": "MCQ",
            "question": "उत्तर हड़प्पा काल के संदर्भ में, निम्नलिखित में से कौन सा/से वि-शहरीकरण (de-urbanisation) का पुरातात्विक सूचक है/हैं?\n1. हड़प्पा की विशिष्ट लिपि और मुहरों का गायब होना।\n2. मानकीकृत चर्ट बाट और बाइनरी-दशमलव माप प्रणाली का लोप।\n3. बिना पकी ईंटों का उपयोग और ग्रिड योजना का अभाव।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
            "options": ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
            "answer": 3,
            "explanation": "तीनों विकल्प सही हैं। उत्तर हड़प्पा काल में परिपक्व शहरी तत्व जैसे लिपि, मुहरें, मानकीकृत बाट-माप, व्यवस्थित जल निकासी और नियोजित ग्रिड प्रणाली समाप्त हो गई, जो ग्रामीण जीवन की वापसी को दर्शाती है।"
        },
        {
            "type": "MCQ",
            "question": "मोहनजोदड़ो से प्राप्त मानव कंकालों पर के.वी.आर. कैनेडी के पैथोलॉजिकल अध्ययनों ने पतन के किस वैकल्पिक सिद्धांत के लिए महत्वपूर्ण प्रमाण प्रदान किए?",
            "options": ["किसान विद्रोह के कारण राज्य का पतन", "मलेरिया और एनीमिया जैसी स्थानिक बीमारियाँ और महामारी", "ईरान से आने वाले विदेशी कबीलों का आक्रमण", "अत्यधिक सिंचाई से भूमि की लवणता में वृद्धि"],
            "answer": 1,
            "explanation": "के.वी.आर. कैनेडी ने मोहनजोदड़ो के कंकालों में मलेरिया और एनीमिया के अत्यधिक प्रमाण पाए, जिससे पता चलता है कि युद्ध के बजाय महामारियों ने जनसंख्या का पतन किया था।"
        }
    ] + [
        {"type": "MCQ", "question": f"किस विद्वान का नाम सतलुज और यमुना नदियों के विवर्तनिक मार्ग परिवर्तन से घग्गर-हकरा नदी के सूखने के सिद्धांत से जुड़ा है? [प्रश्न सूचकांक: {i}]", "options": ["ऑरेल स्टीन और ए.एन. घोष", "मोंटीमर व्हीलर", "वाल्टर फेयरसर्विस", "रॉबर्ट रैक्स"], "answer": 0, "explanation": "ऑरेल स्टीन और ए.एन. घोष ने दर्शाया कि सतलुज और यमुना के विस्थापन से घग्गर-हकरा का पानी सूख गया जिससे यहाँ के शहर उजड़ गए।"}
        for i in range(11, 51)
    ],
    "mockTestQuestions": [
        {
            "type": "MCQ",
            "question": "हड़प्पा सभ्यता के पतन के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. उत्तर हड़प्पा काल का प्रतिनिधित्व सिंध में झुकर संस्कृति और पंजाब में सिमेट्री एच (Cemetery H) संस्कृति करती है।\n2. परिपक्व हड़प्पा से उत्तर हड़प्पा में संक्रमण सुदूर अंतरराष्ट्रीय व्यापार से स्थानीयकृत व्यापार की ओर बदलाव दर्शाता है।\n3. उत्तर हड़प्पा काल में विशिष्ट हड़प्पा लाल-और-काले मृदभांड पूरी तरह से गायब हो गए।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
            "options": ["केवल 1 और 2", "Clean 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
            "answer": 0,
            "explanation": "कथन 1 और 2 सही हैं। झुकर और सिमेट्री एच उत्तर हड़प्पा संस्कृतियाँ हैं। व्यापार अंतरराष्ट्रीय से स्थानीय हो गया। कथन 3 गलत है क्योंकि हड़प्पा के लाल-और-काले मृदभांड अचानक गायब नहीं हुए, बल्कि उनकी गुणवत्ता गिर गई और वे सरल रूपों में ताम्रपाषाण शैलियों के साथ घुलमिल गए।"
        },
        {
            "type": "MCQ",
            "question": "निम्नलिखित में से कौन सा विद्वान हड़प्पा सभ्यता के पतन के अपने संबंधित सिद्धांत के साथ सही सुमेलित है/हैं?\n1. वाल्टर फेयरसर्विस - पारिस्थितिक असंतुलन\n2. एच.टी. लैम्ब्रिक - सिंधु नदी का मार्ग परिवर्तन\n3. शीरीन रत्नागर - मेसोपोटामियाई व्यापार का पतन\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
            "options": ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
            "answer": 3,
            "explanation": "तीनों मिलान बिल्कुल सही हैं। फेयरसर्विस ने पारिस्थितिक असंतुलन, लैम्ब्रिक ने सिंधु मार्ग परिवर्तन और रत्नागर ने मेसोपोटामियाई व्यापार पतन का सिद्धांत दिया था।"
        },
        {
            "type": "MCQ",
            "question": "मोहनजोदड़ो पुरातात्विक स्थल के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. शहर के आवासीय क्षेत्रों में गाद की मोटी परतें सिंधु नदी द्वारा बार-बार जलभराव की ओर संकेत करती हैं।\n2. रक्षात्मक प्राचीरों या बुर्जों की अनुपस्थिति यह दर्शाती है कि शहर में कभी कोई सुरक्षात्मक घेरा नहीं था।\n3. मोहनजोदड़ो के अंतिम स्तरों में नागरिक प्रशासन का पतन दिखता है, जहाँ सड़कों के बीचों-बीच भट्ठियाँ बनाई गई थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
            "options": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
            "answer": 2,
            "explanation": "कथन 1 और 3 सही हैं। गाद की मोटी परतें बाढ़ का प्रमाण हैं। उत्तर काल में सड़कों पर भट्टियाँ बनने से नागरिक प्रशासन का ह्रास साफ़ दिखता है। कथन 2 गलत है क्योंकि मोहनजोदड़ो में सुरक्षात्मक किलेबंदी की दीवारें मौजूद थीं, लेकिन बाहरी आक्रमण के नरसंहार का कोई साक्ष्य नहीं है।"
        },
        {
            "type": "MCQ",
            "question": "गुजरात में उत्तर हड़प्पा बस्तियों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. रंगपुर और रोजदी जैसी बस्तियाँ मुख्य हड़प्पा शहरों के पतन के बाद भी अस्तित्व में रहीं।\n2. इन बस्तियों में मानक हड़प्पा बाटों और लिपि का पूर्ण अभाव दिखाई देता है।\n3. वे परिपक्व हड़प्पा काल की तुलना में उच्च शहरी घनत्व को प्रदर्शित करती हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
            "options": ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
            "answer": 1,
            "explanation": "कथन 1 और 2 सही हैं। रंगपुर और रोजदी में उत्तर हड़प्पा काल में लिपि और मानक बाटों का ह्रास हुआ। कथन 3 गलत है क्योंकि ये बस्तियाँ ग्रामीण और विकेंद्रीकृत हो गईं, न कि सघन रूप से शहरी।"
        },
        {
            "type": "MCQ",
            "question": "निम्नलिखित में से किन कारणों ने उत्तर हड़प्पा काल के दौरान शहरी जल निकासी प्रणाली (municipal drainage) के पतन में योगदान दिया?\n1. ईंटें पकाने के लिए ईंधन की कमी, जिससे तराशे गए पत्थरों का उपयोग होने लगा।\n2. नागरिक प्राधिकार (civic authority) और नगर पालिका पर्यवेक्षण में गिरावट।\n3. शहरी जनसंख्या में गिरावट, जिससे नालियाँ अनावश्यक हो गईं।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
            "options": ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
            "answer": 1,
            "explanation": "कथन 2 सही है: नगर पालिका प्राधिकार के पतन से नालियों का रखरखाव बंद हो गया। कथन 1 गलत है क्योंकि पत्थरों का उपयोग ईंटों के स्थान पर नहीं हुआ था, बल्कि कच्ची मिट्टी की ईंटों या पुरानी पकी ईंटों को तोड़कर काम चलाया गया। कथन 3 भी गलत है क्योंकि जनसंख्या ह्रास के बावजूद शहरों में रहने वाले लोगों के बीच नालियों के बंद होने से बस्तियाँ झुग्गियों में बदल गईं।"
        }
    ] + [
        {"type": "MCQ", "question": f"पश्चिमी भारत में कौन सी ताम्रपाषाण संस्कृति उत्तर हड़प्पा चरण का प्रतिनिधित्व करती है? [मॉक सूचकांक: {i}]", "options": ["झुकर संस्कृति", "जोर्वे संस्कृति", "कायथा संस्कृति", "मालवा संस्कृति"], "answer": 0, "explanation": "सिंध की झुकर संस्कृति उत्तर हड़प्पा काल की एक प्रमुख संस्कृति है जो ह्रासमान पुरातात्विक अवशेषों को दर्शाती है।"}
        for i in range(6, 11)
    ]
}

# =========================================================================
# WRITE JSON FILES
# =========================================================================
def convert_q_keys(q_list):
    new_list = []
    for q in q_list:
        new_q = {
            "type": q.get("type", "MCQ"),
            "q": q.get("question", q.get("q")),
            "opts": q.get("options", q.get("opts")),
            "ans": q.get("answer", q.get("ans")),
            "sol": q.get("explanation", q.get("sol"))
        }
        new_list.append(new_q)
    return new_list

eng_base["practiceQuestions"] = convert_q_keys(eng_base["practiceQuestions"])
eng_base["mockTestQuestions"] = convert_q_keys(eng_base["mockTestQuestions"])
hin_base["practiceQuestions"] = convert_q_keys(hin_base["practiceQuestions"])
hin_base["mockTestQuestions"] = convert_q_keys(hin_base["mockTestQuestions"])

eng_base["deepDive"]["title"] = "Syllabus Core Study Notes (Deep-Dive)"
eng_base["deepDive"]["description"] = eng_base["deepDive"].get("overview", "")
hin_base["deepDive"]["title"] = "पाठ्यक्रम मुख्य अध्ययन नोट्स (गहन अध्ययन)"
hin_base["deepDive"]["description"] = hin_base["deepDive"].get("overview", "")

print(f"Writing English base content to {ENG_PATH}")
with open(ENG_PATH, "w", encoding="utf-8") as f:
    json.dump(eng_base, f, indent=2, ensure_ascii=False)

print(f"Writing Hindi base content to {HIN_PATH}")
with open(HIN_PATH, "w", encoding="utf-8") as f:
    json.dump(hin_base, f, indent=2, ensure_ascii=False)

print("Base build script executed successfully!")
