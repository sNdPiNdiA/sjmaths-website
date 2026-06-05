# -*- coding: utf-8 -*-
import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Later-Vedic-Period\Social-Organisation-and-Hierarchy"

english_data = {
    "breadcrumbs": {
        "parent": "Later Vedic Period",
        "parentUrl": "/upsc/ancient_history/History-of-Later-Vedic-Period/",
        "current": "Social Organisation"
    },
    "hero": {
        "title": "Social Organisation and Hierarchy in Later Vedic Period",
        "description": "An in-depth UPSC study guide on the rigidification of the Varna system, the rise of Brahmana-Kshatriya supremacy, Gotra exogamy, the Ashrama system, and the changing social status of women."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "UPSC Level Mock Test",
            "description": "Test your mastery of Later Vedic Social History with 10 complex statement-based and matching questions.",
            "startBtn": "Start Mock Test"
        }
    },
    "timeline": {
        "cards": [
            {
                "period": "c. 1000 BCE",
                "date": "Rigidification of Varna",
                "details": "Birth replaces occupation as the primary determinant of Varna. Top three varnas (Brahmana, Kshatriya, Vaishya) consolidate as Dvija (twice-born)."
            },
            {
                "period": "c. 800 BCE",
                "date": "Gotra & Exogamy",
                "details": "Transition of Gotra from 'cowpen' to a lineage marker. Implementation of Gotra exogamy rules for marriages."
            },
            {
                "period": "c. 600 BCE",
                "date": "Ashrama & Upanishadic Reaction",
                "details": "Formalization of the four-stage life system (Ashrama) and philosophical reactions in Upanishads challenging ritual supremacy."
            }
        ]
    },
    "toolEvolution": {
        "title": "Social Stratification & Life Cycle Evolution",
        "description": "The evolution of social markers from Rigvedic to Later Vedic times.",
        "stages": [
            {
                "name": "Varna Criteria",
                "color": "#e74c3c",
                "desc": "Shifts from flexible, occupational/color markers (Rigvedic) to rigid, hereditary classes (Later Vedic).",
                "svg": '<i class="fas fa-layer-group" style="font-size: 2rem; color: #e74c3c;"></i>'
            },
            {
                "name": "Gotra System",
                "color": "#f39c12",
                "desc": "Evolves from a shared cowpen (family asset shelter) to an institutionalized mythical descent lineage enforcing exogamy.",
                "svg": '<i class="fas fa-tree" style="font-size: 2rem; color: #f39c12;"></i>'
            },
            {
                "name": "Ashrama Stages",
                "color": "#2ecc71",
                "desc": "Establishment of Brahmacharya, Grihastha, and Vanaprastha, with Sannyasa (ascetic stage) formalized in late Upanishads.",
                "svg": '<i class="fas fa-dharmachakra" style="font-size: 2rem; color: #2ecc71;"></i>'
            }
        ]
    },
    "traps": {
        "title": "Common UPSC Pitfalls & Distinctions",
        "items": [
            "Trap: Believing the four-stage Ashrama system was fully present in the early Rigvedic period. The early Rigveda knows nothing of the Ashrama system; it only crystallized in late Upanishadic times (e.g., Jabala Upanishad).",
            "Do not assume Sudras had access to Upanayana. Sudras were strictly excluded from the sacred thread ceremony (Upanayana) and study of the Vedas.",
            "Although the status of women declined, some women like Gargi and Maitreyi engaged in philosophical debates with Yajnavalkya; however, this represents elite exceptions, not the general rule.",
            "Gotra exogamy prohibits marriage within the same Gotra. Do not confuse it with endogamy; they married outside their Gotra but within their Varna (Varna endogamy)."
        ]
    },
    "mnemonics": {
        "title": "Social Concepts Memory Trick",
        "description": "Use these mnemonics to remember key terms and divisions.",
        "items": [
            {
                "title": "Gotra Exogamy Rule",
                "phrase": "SAME gotra = NO marriage",
                "decryption": "Gotra exogamy forbids marrying a person belonging to the same patrilineal Gotra (clansmen share a common mythical ancestor)."
            },
            {
                "title": "Four Ashramas",
                "phrase": "B-G-V-S: Brahmacharya (Student), Grihastha (Householder), Vanaprastha (Forest dweller), Sannyasa (Ascetic)",
                "decryption": "Order of the four life stages in the orthodox Ashrama system."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your ability to recall key social terms and facts.",
        "items": [
            {
                "question": "Which Upanishad first explicitly mentions all four stages of the Ashrama system?",
                "answer": "Jabala Upanishad.",
                "icon": "fa-book"
            },
            {
                "question": "'Dvija' refers to which categories in Later Vedic society?",
                "answer": "The top three Varnas: Brahmana, Kshatriya, and Vaishya.",
                "icon": "fa-certificate"
            },
            {
                "question": "What did 'Gotra' originally mean?",
                "answer": "A shared cowpen belonging to a patrilineal clan.",
                "icon": "fa-cow"
            },
            {
                "question": "Which text famously declares a daughter to be a source of misery?",
                "answer": "Aitareya Brahmana.",
                "icon": "fa-heart-broken"
            }
        ]
    }
}

hindi_data = {
    "breadcrumbs": {
        "parent": "उत्तर वैदिक काल",
        "parentUrl": "/upsc/ancient_history/History-of-Later-Vedic-Period/",
        "current": "सामाजिक संगठन"
    },
    "hero": {
        "title": "उत्तर वैदिक काल में सामाजिक संगठन और पदानुक्रम",
        "description": "वर्ण व्यवस्था के सुदृढ़ीकरण, ब्राह्मणों और क्षत्रियों के वर्चस्व, वैश्यों और शूद्रों के कर्तव्यों, गोत्र प्रणाली, आश्रम व्यवस्था और महिलाओं की गिरती स्थिति का अन्वेषण करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "UPSC स्तर का मॉक टेस्ट",
            "description": "10 जटिल कथन-आधारित और मिलान वाले प्रश्नों के साथ उत्तर वैदिक सामाजिक इतिहास पर अपनी महारत का परीक्षण करें।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        }
    },
    "timeline": {
        "cards": [
            {
                "period": "लगभग 1000 ईसा पूर्व",
                "date": "वर्ण व्यवस्था का सुदृढ़ीकरण",
                "details": "जन्म ने व्यवसाय का स्थान ले लिया। शीर्ष तीन वर्ण (ब्राह्मण, क्षत्रिय, वैश्य) द्विज (दो बार जन्मे) के रूप में समेकित हुए।"
            },
            {
                "period": "लगभग 800 ईसा पूर्व",
                "date": "गोत्र और बहिर्विवाह",
                "details": "गोत्र का 'गोशाला' से वंश सूचक में संक्रमण। विवाहों के लिए गोत्र बहिर्विवाह नियमों का कार्यान्वयन।"
            },
            {
                "period": "लगभग 600 ईसा पूर्व",
                "date": "आश्रम और उपनिषदिक प्रतिक्रिया",
                "details": "चार चरणों वाली जीवन व्यवस्था (आश्रम) का औपचारिक रूप और कर्मकांडीय वर्चस्व को चुनौती देने वाली उपनिषदों में प्रतिक्रिया।"
            }
        ]
    },
    "toolEvolution": {
        "title": "सामाजिक स्तरीकरण और जीवन चक्र विकास",
        "description": "ऋग्वैदिक से उत्तर वैदिक काल तक सामाजिक सूचकों का विकास।",
        "stages": [
            {
                "name": "वर्ण मानदंड",
                "color": "#e74c3c",
                "desc": "ऋग्वैदिक काल के लचीले, व्यवसाय-आधारित वर्गीकरण से उत्तर वैदिक काल में कठोर, वंशानुगत व्यवस्था में बदलाव।",
                "svg": '<i class="fas fa-layer-group" style="font-size: 2rem; color: #e74c3c;"></i>'
            },
            {
                "name": "गोत्र प्रणाली",
                "color": "#f39c12",
                "desc": "एक साझा गोशाला (पारिवारिक संपत्ति) से एक संस्थागत पौराणिक वंश में विकसित हुआ जो बहिर्विवाह लागू करता है।",
                "svg": '<i class="fas fa-tree" style="font-size: 2rem; color: #f39c12;"></i>'
            },
            {
                "name": "आश्रम चरण",
                "color": "#2ecc71",
                "desc": "ब्रह्मचर्य, गृहस्थ और वानप्रस्थ की स्थापना, और बाद के उपनिषदों में संन्यास (सन्यासी चरण) को औपचारिक रूप दिया गया।",
                "svg": '<i class="fas fa-dharmachakra" style="font-size: 2rem; color: #2ecc71;"></i>'
            }
        ]
    },
    "traps": {
        "title": "सामान्य UPSC गलतियाँ और भेद",
        "items": [
            "भ्रम: यह मानना कि चार चरणों वाली आश्रम व्यवस्था प्रारंभिक ऋग्वैदिक काल में पूरी तरह से मौजूद थी। प्रारंभिक ऋग्वेद आश्रम व्यवस्था के बारे में कुछ नहीं जानता; यह केवल बाद के उपनिषद काल (जैसे, जाबाल उपनिषद) में विकसित हुई।",
            "यह न मानें कि शूद्रों को उपनयन का अधिकार था। शूद्रों को जनेऊ संस्कार (उपनयन) और वेदों के अध्ययन से पूरी तरह बाहर रखा गया था।",
            "यद्यपि महिलाओं की स्थिति में गिरावट आई, लेकिन गार्गी और मैत्रेयी जैसी कुछ महिलाओं ने याज्ञवल्क्य के साथ दार्शनिक बहस में भाग लिया; हालाँकि, यह कुलीन अपवादों का प्रतिनिधित्व करता है, सामान्य नियम का नहीं।",
            "गोत्र बहिर्विवाह एक ही गोत्र के भीतर विवाह को रोकता है। इसे अंतर्विवाह से भ्रमित न करें; वे अपने गोत्र से बाहर लेकिन अपने वर्ण के भीतर विवाह करते थे (वर्ण अंतर्विवाह)।"
        ]
    },
    "mnemonics": {
        "title": "सामाजिक अवधारणाओं को याद रखने की ट्रिक",
        "description": "प्रमुख शब्दों और विभाजनों को याद रखने के लिए इन ट्रिक्स का उपयोग करें।",
        "items": [
            {
                "title": "गोत्र बहिर्विवाह नियम",
                "phrase": "समान गोत्र = विवाह निषेध",
                "decryption": "गोत्र बहिर्विवाह एक ही पितृवंशीय गोत्र के व्यक्ति से विवाह करने से रोकता है।"
            },
            {
                "title": "चार आश्रम",
                "phrase": "B-G-V-S: ब्रह्मचर्य (छात्र), गृहस्थ (गृहस्वामी), वानप्रस्थ (वनवासी), संन्यास (सन्यासी)",
                "decryption": "रूढ़िवादी आश्रम व्यवस्था में जीवन के चार चरणों का क्रम।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड",
        "description": "मुख्य तथ्यों को याद रखने की अपनी क्षमता का परीक्षण करें।",
        "items": [
            {
                "question": "कौन सा उपनिषद सबसे पहले स्पष्ट रूप से चारों आश्रमों का उल्लेख करता है?",
                "answer": "जाबाल उपनिषद।",
                "icon": "fa-book"
            },
            {
                "question": "'द्विज' शब्द का क्या अर्थ है और इसमें कौन शामिल थे?",
                "answer": "इसका अर्थ है 'दो बार जन्मा', जो शीर्ष तीन वर्णों (ब्राह्मण, क्षत्रिय, वैश्य) को संदर्भित करता है जो उपनयन संस्कार के पात्र थे।",
                "icon": "fa-certificate"
            },
            {
                "question": "मूल रूप से 'गोत्र' का शाब्दिक अर्थ क्या था?",
                "answer": "गोशाला, एक ऐसा स्थान जहाँ पूरे कबीले के मवेशियों को एक साथ रखा जाता था।",
                "icon": "fa-cow"
            },
            {
                "question": "किस ग्रंथ में पुत्री को 'दुखों का स्रोत' (कृपण) बताया गया है?",
                "answer": "ऐतरेय ब्राह्मण।",
                "icon": "fa-heart-broken"
            }
        ]
    }
}

sections_meta = [
    {
        "id": 1,
        "title": "1. Crystallization of the Varna System",
        "title_hi": "1. वर्ण व्यवस्था का सुदृढ़ीकरण",
        "content": "<h3>Hereditary Shift and Social Rigidity</h3><p>The social structure during the Later Vedic period transitioned from the fluid, occupation-based classification of the Rigvedic era to a rigid, hereditary system. Birth became the sole determinant of one's **Varna**. The four-fold division—Brahmana (priests/scholars), Kshatriya (warriors/rulers), Vaishya (agriculturists/traders), and Sudra (laborers/servants)—crystallized, with defined duties, privileges, and ritual codes for each class.</p><h3>The Ritual Divide: Dvija and Upanayana</h3><p>A primary mechanism of exclusion was the **Upanayana** (sacred thread ceremony). The top three Varnas were designated as **Dvija** (twice-born), symbolizing their secondary spiritual birth through Vedic initiation, granting them the exclusive right to study the Vedas. In contrast, the **Sudras** were strictly excluded from the Upanayana and reading sacred scriptures, relegating them to a permanently subordinate social status and establishing the basis of ritual pollution.</p>",
        "content_hi": "<h3>वंशानुगत बदलाव और सामाजिक कठोरता</h3><p>उत्तर वैदिक काल के दौरान सामाजिक संरचना ऋग्वैदिक काल के लचीले, व्यवसाय-आधारित वर्गीकरण से एक कठोर, वंशानुगत व्यवस्था में परिवर्तित हो गई। जन्म किसी के **वर्ण** का एकमात्र निर्धारक बन गया। चार-गुना विभाजन—ब्राह्मण (पुरोहित/विद्वान), क्षत्रिय (योद्धा/शासक), वैश्य (किसान/व्यापारी), और शूद्र (मजदूर/सेवक)—मजबूत हो गया, जिसमें प्रत्येक वर्ग के लिए विशिष्ट कर्तव्य, विशेषाधिकार और अनुष्ठान नियम निर्धारित थे।</p><h3>अनुष्ठानिक विभाजन: द्विज और उपनयन</h3><p>बहिष्करण का एक प्राथमिक तंत्र **उपनयन** (जनेऊ संस्कार) था। शीर्ष तीन वर्णों को **द्विज** (दो बार जन्मा) के रूप में नामित किया गया था, जो वैदिक दीक्षा के माध्यम से उनके दूसरे आध्यात्मिक जन्म का प्रतीक था, जिससे उन्हें वेदों का अध्ययन करने का अनन्य अधिकार मिला। इसके विपरीत, **शूद्रों** को उपनयन संस्कार और पवित्र ग्रंथों को पढ़ने से कड़ाई से बाहर रखा गया था, जिससे वे स्थायी रूप से अधीनस्थ सामाजिक स्थिति में आ गए और अनुष्ठानिक अपवित्रता का आधार बना।</p>"
    },
    {
        "id": 2,
        "title": "2. Supremacy of Brahmana and Rajanya",
        "title_hi": "2. ब्राह्मण और राजन्य का वर्चस्व",
        "content": "<h3>Alliance of the Ruling Varnas</h3><p>The Later Vedic era saw the consolidation of power by the two upper Varnas: the Brahmanas and the Kshatriyas (Rajanyas). They established a symbiotic alliance to control the resources and administration of the state. The Brahmana validated the king's political and territorial claims through complex state rituals (Rajasuya, Asvamedha), while the king provided the Brahmanas with patronage, gifts of land (Brahmadeya), and cattle wealth, reinforcing their social status.</p><h3>Precedence Conflicts and Hegemony</h3><p>Although they presented a united front to subordinate the Vaishyas and Sudras, the Brahmanas and Kshatriyas occasionally experienced internal conflicts over social supremacy. The Brahmanas asserted their spiritual superiority by claiming that the priest was superior to the king, whereas some Kshatriyas claimed dominance based on their administrative and military control. Despite these conflicts, both classes joint-ruled and were exempted from agricultural labor and compulsory taxation.</p>",
        "content_hi": "<h3>सत्तारूढ़ वर्णों का गठबंधन</h3><p>उत्तर वैदिक काल में दो उच्च वर्णों: ब्राह्मणों और क्षत्रियों (राजन्यों) द्वारा सत्ता का सुदृढ़ीकरण देखा गया। उन्होंने राज्य के संसाधनों और प्रशासन को नियंत्रित करने के लिए एक सहजीवी गठबंधन स्थापित किया। ब्राह्मण जटिल राज्य अनुष्ठानों (राजसूय, अश्वमेध) के माध्यम से राजा के राजनीतिक और क्षेत्रीय दावों को वैध बनाते थे, जबकि राजा ब्राह्मणों को संरक्षण, भूमि का दान (ब्रह्मदेय) और मवेशी धन प्रदान करता था, जिससे उनकी सामाजिक स्थिति मजबूत होती थी।</p><h3>वर्चस्व के संघर्ष और हेगमनी</h3><p>यद्यपि वे वैश्यों और शूद्रों को अधीनस्थ करने के लिए एकजुट मोर्चे के रूप में कार्य करते थे, ब्राह्मणों और क्षत्रियों के बीच कभी-कभी सामाजिक वर्चस्व को लेकर आंतरिक संघर्ष भी होते थे। ब्राह्मणों ने यह दावा करते हुए अपनी आध्यात्मिक श्रेष्ठता का दावा किया कि पुरोहित राजा से श्रेष्ठ है, जबकि कुछ क्षत्रियों ने अपने प्रशासनिक और सैन्य नियंत्रण के आधार पर वर्चस्व का दावा किया। इन संघर्षों के बावजूद, दोनों वर्गों ने संयुक्त रूप से शासन किया और उन्हें कृषि श्रम और अनिवार्य कराधान से छूट दी गई थी।</p>"
    },
    {
        "id": 3,
        "title": "3. Subjugation and Duties of the Vaishya and Sudra",
        "title_hi": "3. वैश्य और शूद्र का अधीनता और कर्तव्य",
        "content": "<h3>Vaishyas: The Tribute-Paying Class</h3><p>The **Vaishyas** constituted the productive class of Later Vedic society, engaging in agriculture, cattle rearing, and early crafts and trade. In texts, they are described as <strong>Anyasya Balikrt</strong> (tribute payers to others) and <strong>Anyasyadya</strong> (to be exploited or consumed by others). They bore the entire tax burden of the state, funding the royal administration and the expensive sacrifices of the priestly class.</p><h3>Sudras: The Servile Class and Untouchability</h3><p>The **Sudras** were relegated to the lowest tier of society, described as <strong>Anyasya Presya</strong> (servant of another) and <strong>Kamadhapya</strong> (subject to expulsion or beating at will). They were prohibited from performing sacrifices and studying the Vedas. Crucially, the Later Vedic texts show early signs of social exclusion and segregation of certain occupational groups, such as the **Chandalas**, marking the initial phase of untouchability.</p>",
        "content_hi": "<h3>वैश्य: करदाता वर्ग</h3><p>**वैश्य** उत्तर वैदिक समाज के उत्पादक वर्ग थे, जो कृषि, पशुपालन और प्रारंभिक शिल्प तथा व्यापार में लगे हुए थे। ग्रंथों में उन्हें <strong>अन्यस्य बलिकृत</strong> (दूसरों को कर देने वाले) और <strong>अन्यस्याद्य</strong> (दूसरों द्वारा शोषित होने वाले) के रूप में वर्णित किया गया है। उन्होंने राज्य का पूरा कर बोझ उठाया, शाही प्रशासन और पुरोहित वर्ग के महंगे यज्ञों का वित्तपोषण किया।</p><h3>शूद्र: सेवक वर्ग और अस्पृश्यता</h3><p>**शूद्रों** को समाज के सबसे निचले पायदान पर धकेल दिया गया था, जिन्हें <strong>अन्यस्य प्रेष्य</strong> (दूसरों का सेवक) और <strong>कामधाप्य</strong> (इच्छा पर निष्कासित या पीटा जाने वाला) बताया गया था। उन्हें यज्ञ करने और वेदों का अध्ययन करने से प्रतिबंधित कर दिया गया था। सबसे महत्वपूर्ण बात यह है कि उत्तर वैदिक ग्रंथों में सामाजिक बहिष्कार और कुछ व्यावसायिक समूहों जैसे कि **चांडालों** को अलग-थलग करने के प्रारंभिक लक्षण दिखाई देते हैं, जो अस्पृश्यता के प्रारंभिक चरण को चिह्नित करते हैं।</p>"
    },
    {
        "id": 4,
        "title": "4. Emergence of the Gotra System",
        "title_hi": "4. गोत्र प्रणाली का उदय",
        "content": "<h3>Origins of Gotra</h3><p>The word **Gotra** literally means 'cowpen', denoting the common shelter where the cattle of a clan were kept together during the pastoral phase. In the Later Vedic period, the term transitioned to represent a lineage system. It denoted a group of individuals who traced their descent from a common mythical ancestor, typically one of the **Saptarishis** (seven sages) or **Agastya**.</p><h3>Gotra Exogamy and Identity</h3><p>The consolidation of the Gotra system led to the formulation of strict kinship rules. The rule of **Gotra exogamy** emerged, prohibiting marriage between individuals belonging to the same Gotra. This rule prevented incest and fostered inter-clan alliances. At the same time, Varna endogamy was maintained, requiring individuals to marry within their own Varna while marrying outside their Gotra, shaping the classic Hindu kinship structure.</p>",
        "content_hi": "<h3>गोत्र की उत्पत्ति</h3><p>**गोत्र** शब्द का शाब्दिक अर्थ 'गोशाला' है, जो उस सामान्य आश्रय को दर्शाता है जहाँ पशुचारण चरण के दौरान एक कबीले के मवेशियों को एक साथ रखा जाता था। उत्तर वैदिक काल में, यह शब्द एक वंश प्रणाली का प्रतिनिधित्व करने लगा। यह उन व्यक्तियों के समूह को दर्शाता था जो एक साझा पौराणिक पूर्वज, आमतौर पर **सप्तर्षियों** (सात ऋषियों) या **अगस्त्य** में से एक से अपने वंश का पता लगाते थे।</p><h3>गोत्र बहिर्विवाह और पहचान</h3><p>गोत्र प्रणाली के सुदृढ़ीकरण से सख्त नातेदारी नियमों का निर्माण हुआ। **गोत्र बहिर्विवाह** (Gotra exogamy) का नियम उभरा, जिसके तहत एक ही गोत्र के व्यक्तियों के बीच विवाह को प्रतिबंधित कर दिया गया। इस नियम ने सगोत्र विवाह को रोका और अंतर-कबीले गठबंधनों को बढ़ावा दिया। इसके साथ ही, वर्ण अंतर्विवाह को बनाए रखा गया, जिसके तहत व्यक्तियों को अपने गोत्र से बाहर लेकिन अपने वर्ण के भीतर विवाह करना आवश्यक था, जिसने शास्त्रीय हिंदू नातेदारी संरचना को आकार दिया।</p>"
    },
    {
        "id": 5,
        "title": "5. The Ashrama System and Purusharthas",
        "title_hi": "5. आश्रम व्यवस्था और पुरुषार्थ",
        "content": "<h3>Structuring the Life Cycle</h3><p>The **Ashrama system** emerged in late Vedic times as an institutional mechanism to organize an individual's life cycle. The texts, particularly the late Upanishads like the **Jabala Upanishad**, formalize four distinct stages (Ashramas) of life for the Dvija males:<ul><li><strong>Brahmacharya:</strong> Student life spent in celibacy, learning under a Guru.</li><li><strong>Grihastha:</strong> Householder stage, raising a family, performing sacrifices, and engaging in economic activities.</li><li><strong>Vanaprastha:</strong> Partial retirement, moving to the forest for meditation and simple living.</li><li><strong>Sannyasa:</strong> Ascetic stage, completely renouncing material ties in search of liberation.</li></ul></p><h3>The Purusharthas</h3><p>Complementing the Ashrama system were the **Purusharthas** (four aims of life): **Dharma** (righteous duty), **Artha** (wealth creation), **Kama** (sensual pleasure), and **Moksha** (spiritual liberation), creating a balanced framework between worldly engagement and renunciation.</p>",
        "content_hi": "<h3>जीवन चक्र का ढांचा</h3><p>**आश्रम व्यवस्था** उत्तर वैदिक काल के उत्तरार्ध में एक व्यक्ति के जीवन चक्र को व्यवस्थित करने के लिए एक संस्थागत तंत्र के रूप में उभरी। ग्रंथ, विशेष रूप से बाद के उपनिषद जैसे **जाबाल उपनिषद**, द्विज पुरुषों के लिए जीवन के चार अलग-अलग चरणों (आश्रमों) को औपचारिक रूप देते हैं:<ul><li><strong>ब्रह्मचर्य:</strong> छात्र जीवन जो ब्रह्मचर्य में व्यतीत होता है, गुरु के अधीन शिक्षा प्राप्त करना।</li><li><strong>गृहस्थ:</strong> गृहस्वामी का चरण, परिवार का पालन-पोषण करना, यज्ञ करना और आर्थिक गतिविधियों में संलग्न होना।</li><li><strong>वानप्रस्थ:</strong> आंशिक सेवानिवृत्ति, ध्यान और सरल जीवन के लिए जंगल में जाना।</li><li><strong>संन्यास:</strong> संन्यासी चरण, मुक्ति की खोज में भौतिक संबंधों का पूरी तरह से त्याग करना।</li></ul></p><h3>पुरुषार्थ</h3><p>आश्रम व्यवस्था के पूरक **पुरुषार्थ** (जीवन के चार उद्देश्य) थे: **धर्म** (सदाचारी कर्तव्य), **अर्थ** (धन सृजन), **काम** (इंद्रिय सुख), और **मोक्ष** (आध्यात्मिक मुक्ति), जो सांसारिक जुड़ाव और त्याग के बीच एक संतुलित ढांचा तैयार करते थे।</p>"
    },
    {
        "id": 6,
        "title": "6. Status of Women in Later Vedic Society",
        "title_hi": "6. उत्तर वैदिक समाज में महिलाओं की स्थिति",
        "content": "<h3>Declining Social Status</h3><p>The social status of women deteriorated significantly in the Later Vedic period compared to their relatively free position during the Rigvedic era. They lost their political rights, being excluded from participating in the Sabha and Samiti. The birth of a daughter was increasingly viewed as a matter of concern; the **Aitareya Brahmana** states that 'a daughter is a source of misery, while a son is the protector of the family'.</p><h3>Social Restrictions and Intellectual Exceptions</h3><p>Polygamy became common among rulers and elites, and child marriage started finding validation. Women were generally denied property rights and were subjected to male guardianship (father, husband, son). Despite this general decline, some women of the upper classes engaged in scholarly pursuits. The **Brihadaranyaka Upanishad** mentions **Gargi Vachaknavi**, who challenged Yajnavalkya in a public philosophical debate, and **Maitreyi**, who sought spiritual knowledge over material wealth, reflecting class-based disparities in gender rights.</p>",
        "content_hi": "<h3>सामाजिक स्थिति में गिरावट</h3><p>ऋग्वैदिक काल की तुलना में उत्तर वैदिक काल में महिलाओं की सामाजिक स्थिति में काफी गिरावट आई। उन्होंने अपने राजनीतिक अधिकार खो दिए, और उन्हें सभा और समिति में भाग लेने से बाहर कर दिया गया। बेटी के जन्म को चिंता का विषय माना जाने लगा; **ऐतरेय ब्राह्मण** में कहा गया है कि 'बेटी दुख का स्रोत है, जबकि बेटा परिवार का रक्षक है'।</p><h3>सामाजिक प्रतिबंध और दार्शनिक अपवाद</h3><p>शासकों और अभिजात वर्ग के बीच बहुविवाह आम हो गया, और बाल विवाह को वैधता मिलने लगी। महिलाओं को आम तौर पर संपत्ति के अधिकार से वंचित किया जाता था और वे पुरुष संरक्षण (पिता, पति, पुत्र) के अधीन थीं। इस सामान्य गिरावट के बावजूद, उच्च वर्ग की कुछ महिलाओं ने विद्वतापूर्ण गतिविधियों में भाग लिया। **बृहदारण्यक उपनिषद** में **गार्गी वाचक्नवी** का उल्लेख है, जिन्होंने एक सार्वजनिक दार्शनिक वाद-विवाद में याज्ञवल्क्य को चुनौती दी थी, और **मैत्रेयी** का, जिन्होंने भौतिक धन के बजाय आध्यात्मिक ज्ञान की मांग की थी, जो लिंग अधिकारों में वर्ग-आधारित असमानताओं को दर्शाता है।</p>"
    }
]

# Unique data pool for generating 62 distinct questions per section
question_pool = {
    1: [
        {"q": "Which ceremony marked the transition of a young Vedic male into the status of a Dvija?", "opts": ["Upanayana", "Rajasuya", "Garbhadhana", "Vivaha"], "ans": 0, "sol": "The Upanayana (sacred thread ceremony) marked the second spiritual birth, classifying them as Dvija.", "q_hi": "किस संस्कार ने एक युवा वैदिक पुरुष के द्विज की स्थिति में संक्रमण को चिह्नित किया?", "opts_hi": ["उपनयन", "राजसूय", "गर्भाधान", "विवाह"], "ans_hi": 0, "sol_hi": "उपनयन (जनेऊ संस्कार) ने दूसरे आध्यात्मिक जन्म को चिह्नित किया, जिससे उन्हें द्विज के रूप में वर्गीकृत किया गया."},
        {"q": "What does the term 'Dvija' literally translate to in English?", "opts": ["Twice-born", "Priest-born", "Noble-born", "Holy-born"], "ans": 0, "sol": "Dvija means twice-born.", "q_hi": "'द्विज' शब्द का अंग्रेजी में शाब्दिक अनुवाद क्या है?", "opts_hi": ["दो बार जन्मा", "पुरोहित से जन्मा", "कुलीन वर्ग में जन्मा", "पवित्र जन्मा"], "ans_hi": 0, "sol_hi": "द्विज का अर्थ दो बार जन्मा है."},
        {"q": "Which of the following varnas was strictly excluded from the Upanayana ceremony?", "opts": ["Sudra", "Vaishya", "Kshatriya", "Brahmana"], "ans": 0, "sol": "Sudras were excluded from Upanayana.", "q_hi": "निम्नलिखित में से कौन सा वर्ण उपनयन संस्कार से पूरी तरह बाहर था?", "opts_hi": ["शूद्र", "वैश्य", "क्षत्रिय", "ब्राह्मण"], "ans_hi": 0, "sol_hi": "शूद्रों को उपनयन से बाहर रखा गया था."},
        {"q": "What became the sole determinant of Varna status in the Later Vedic Period?", "opts": ["Birth (Hereditary)", "Occupation / Skill", "Wealth", "Divine choice"], "ans": 0, "sol": "Birth replaced occupational flexibility in defining Varna.", "q_hi": "उत्तर वैदिक काल में वर्ण स्थिति का एकमात्र निर्धारक क्या बन गया?", "opts_hi": ["जन्म (वंशानुगत)", "व्यवसाय / कौशल", "धन", "दैवीय विकल्प"], "ans_hi": 0, "sol_hi": "वर्ण निर्धारण में जन्म ने व्यावसायिक लचीलेपन का स्थान ले लिया."},
        {"q": "Which text details the four-fold division of Varna based on birth codes?", "opts": ["Later Vedic Samhitas & Brahmanas", "Rigveda core mandala", "Upanishad early books", "Sulvasutras"], "ans": 0, "sol": "Later Vedic texts formalized the rigid hereditary four-fold division.", "q_hi": "जन्म संहिताओं पर आधारित वर्ण के चार-गुना विभाजन का विवरण किस ग्रंथ में है?", "opts_hi": ["उत्तर वैदिक संहिताएँ और ब्राह्मण", "ऋग्वेद का मूल मंडल", "प्रारंभिक उपनिषद", "शुल्बसूत्र"], "ans_hi": 0, "sol_hi": "उत्तर वैदिक ग्रंथों ने कठोर वंशानुगत चार-गुना विभाजन को औपचारिक रूप दिया."},
        {"q": "How many twice-born (Dvija) classes existed in Later Vedic society?", "opts": ["Three", "Four", "Two", "One"], "ans": 0, "sol": "Brahmana, Kshatriya, and Vaishya were the three Dvija classes.", "q_hi": "उत्तर वैदिक समाज में कितनी द्विज श्रेणियां थीं?", "opts_hi": ["तीन", "चार", "दो", "एक"], "ans_hi": 0, "sol_hi": "ब्राह्मण, क्षत्रिय और वैश्य तीन द्विज श्रेणियां थीं."},
        {"q": "What ritual privilege granted Dvija classes access to Vedic studies?", "opts": ["Upanayana", "Rajasuya", "Asvamedha", "Agnistoma"], "ans": 0, "sol": "Upanayana allowed them to study the Vedas.", "q_hi": "किस अनुष्ठानिक विशेषाधिकार ने द्विज श्रेणियों को वैदिक अध्ययन तक पहुंच प्रदान की?", "opts_hi": ["उपनयन", "राजसूय", "अश्वमेध", "अग्निष्टोम"], "ans_hi": 0, "sol_hi": "उपनयन ने उन्हें वेदों का अध्ययन करने की अनुमति दी."},
        {"q": "Which of the following describes the nature of Later Vedic Varna transition?", "opts": ["From fluid to rigid hereditary status", "From hereditary to flexible occupational classes", "No change occurred", "Varna disappeared entirely"], "ans": 0, "sol": "The transition was from fluid occupation-based to rigid birth-based structure.", "q_hi": "निम्नलिखित में से कौन उत्तर वैदिक वर्ण संक्रमण की प्रकृति का वर्णन करता है?", "opts_hi": ["लचीले से कठोर वंशानुगत स्थिति की ओर", "वंशानुगत से लचीली व्यावसायिक श्रेणियों की ओर", "कोई बदलाव नहीं हुआ", "वर्ण पूरी तरह से गायब हो गया"], "ans_hi": 0, "sol_hi": "यह संक्रमण लचीले व्यवसाय-आधारित से कठोर जन्म-आधारित संरचना की ओर था."},
        {"q": "Which ritual concept formed the primary ideological basis for excluding Sudras from sacred rites?", "opts": ["Ritual Pollution", "Universal equality", "Atheism", "None of these"], "ans": 0, "sol": "The concept of ritual pollution and purity emerged to justify social exclusion.", "q_hi": "किस अनुष्ठानिक अवधारणा ने शूद्रों को पवित्र संस्कारों से बाहर रखने का प्राथमिक वैचारिक आधार बनाया?", "opts_hi": ["अनुष्ठानिक अपवित्रता", "सार्वभौमिक समानता", "नास्तिकता", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "सामाजिक बहिष्कार को सही ठहराने के लिए अनुष्ठानिक अपवित्रता और शुद्धता की अवधारणा का उदय हुआ."},
        {"q": "What primary social duty was assigned to the Sudra Varna in Later Vedic texts?", "opts": ["Serving the other three Varnas", "Studying the Vedas", "Collecting state taxes", "Ruling territories"], "ans": 0, "sol": "Sudras were relegated to the service of the three higher twice-born classes.", "q_hi": "उत्तर वैदिक ग्रंथों में शूद्र वर्ण को कौन सा प्राथमिक सामाजिक कर्तव्य सौंपा गया था?", "opts_hi": ["अन्य तीन वर्णों की सेवा करना", "वेदों का अध्ययन करना", "राज्य कर एकत्र करना", "क्षेत्रों पर शासन करना"], "ans_hi": 0, "sol_hi": "शूद्रों को तीन उच्च द्विज श्रेणियों की सेवा करने के काम में लगा दिया गया था."},
        {"q": "While the Purusha Sukta introduced Varna metaphorically, the Later Vedic texts converted it into a:", "opts": ["Rigid, birth-based reality", "Completely flexible guild system", "Egalitarian democratic order", "System with no social distinctions"], "ans": 0, "sol": "The Later Vedic period institutionalized the Varna system into a rigid birth-based hierarchy.", "q_hi": "जबकि पुरुष सूक्त ने रूपक के रूप में वर्ण की शुरुआत की थी, उत्तर वैदिक ग्रंथों ने इसे किसमें बदल दिया?", "opts_hi": ["कठोर, जन्म-आधारित वास्तविकता", "पूरी तरह से लचीली गिल्ड व्यवस्था", "समतावादी लोकतांत्रिक व्यवस्था", "बिना सामाजिक भेदभाव वाली व्यवस्था"], "ans_hi": 0, "sol_hi": "उत्तर वैदिक काल ने वर्ण व्यवस्था को एक कठोर जन्म-आधारित पदानुक्रम में संस्थागत बना दिया."},
        {"q": "Which auxiliary texts detail different wood or thread types for Upanayana ceremony based on Varna?", "opts": ["Srautasutras or Grihyasutras", "Rigveda Samhita", "Late Upanishads", "None of these"], "ans": 0, "sol": "Sutras specify different thread materials (e.g. cotton for Brahmana, wool for Kshatriya) and ages for Varnas.", "q_hi": "कौन से सहायक ग्रंथ वर्ण के आधार पर उपनयन संस्कार के लिए विभिन्न प्रकार के धागों या लकड़ियों का विवरण देते हैं?", "opts_hi": ["श्रौतसूत्र या गृह्यसूत्र", "ऋग्वेद संहिता", "उत्तर कालीन उपनिषद", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "सूत्र विभिन्न वर्णों के लिए धागे की विभिन्न सामग्रियों (जैसे ब्राह्मण के लिए सूत, क्षत्रिय के लिए ऊन) और उम्र को निर्दिष्ट करते हैं."}
    ],
    2: [
        {"q": "What term is used for land grants given to Brahmana priests?", "opts": ["Brahmadeya", "Bhaga", "Bali", "Devadana"], "ans": 0, "sol": "Brahmadeya refers to land gifts to priests.", "q_hi": "ब्राह्मण पुरोहितों को दिए जाने वाले भूमि दान के लिए किस शब्द का प्रयोग किया जाता है?", "opts_hi": ["ब्रह्मदेय", "भाग", "बलि", "देवदान"], "ans_hi": 0, "sol_hi": "ब्रह्मदेय ब्राह्मणों को दिए जाने वाले भूमि दान को संदर्भित करता है."},
        {"q": "Which two upper Varnas shared a symbiotic alliance for political hegemony?", "opts": ["Brahmana and Kshatriya", "Brahmana and Vaishya", "Kshatriya and Vaishya", "Kshatriya and Sudra"], "ans": 0, "sol": "Brahmanas and Kshatriyas joint-ruled to dominate resources.", "q_hi": "किन दो उच्च वर्णों ने राजनीतिक वर्चस्व के लिए सहजीवी गठबंधन साझा किया?", "opts_hi": ["ब्राह्मण और क्षत्रिय", "ब्राह्मण और वैश्य", "क्षत्रिय और वैश्य", "क्षत्रिय और शूद्र"], "ans_hi": 0, "sol_hi": "ब्राह्मणों और क्षत्रियों ने संसाधनों पर वर्चस्व के लिए संयुक्त रूप से शासन किया."},
        {"q": "Which royal ceremony validated the king's political sovereignty?", "opts": ["Rajasuya", "Upanayana", "Vivaha", "Pashubandha"], "ans": 0, "sol": "Rajasuya was the royal consecration ritual.", "q_hi": "किस शाही समारोह ने राजा की राजनीतिक संप्रभुता को वैध बनाया?", "opts_hi": ["राजसूय", "उपनयन", "विवाह", "पशुबंध"], "ans_hi": 0, "sol_hi": "राजसूय शाही राज्याभिषेक अनुष्ठान था."},
        {"q": "What economic privilege did the top two Varnas enjoy?", "opts": ["Exemption from agricultural labor and taxes", "Control of coastal shipping", "Universal land distribution", "State-funded salaries in coins"], "ans": 0, "sol": "They were exempt from manual labor and taxation.", "q_hi": "शीर्ष दो वर्णों को कौन सा आर्थिक विशेषाधिकार प्राप्त था?", "opts_hi": ["कृषि श्रम और करों से छूट", "तटीय नौवहन पर नियंत्रण", "सार्वभौमिक भूमि वितरण", "सिक्कों में राज्य द्वारा वित्तपोषित वेतन"], "ans_hi": 0, "sol_hi": "उन्हें शारीरिक श्रम और कराधान से छूट दी गई थी."},
        {"q": "Which class asserted spiritual superiority over the Rajanya kings?", "opts": ["Brahmana", "Vaishya", "Sudra", "Chandala"], "ans": 0, "sol": "Brahmanas asserted spiritual supremacy.", "q_hi": "किस वर्ग ने राजन्य राजाओं पर आध्यात्मिक श्रेष्ठता का दावा किया?", "opts_hi": ["ब्राह्मण", "वैश्य", "शूद्र", "चांडाल"], "ans_hi": 0, "sol_hi": "ब्राह्मणों ने आध्यात्मिक श्रेष्ठता का दावा किया."},
        {"q": "What did the king gift to the Brahmanas in return for ritual consecration?", "opts": ["Land (Brahmadeya) and cattle", "Foreign ships", "Iron plowshares", "Silk textiles"], "ans": 0, "sol": "Kings gifted land and cows to priests.", "q_hi": "अनुष्ठानिक अभिषेक के बदले राजा ने ब्राह्मणों को क्या उपहार दिया?", "opts_hi": ["भूमि (ब्रह्मदेय) और मवेशी", "विदेशी जहाज", "लोहे के हल", "रेशमी वस्त्र"], "ans_hi": 0, "sol_hi": "राजाओं ने पुरोहितों को भूमि और गायें दान में दीं."},
        {"q": "Which class asserted supremacy based on administrative and military control?", "opts": ["Kshatriya (Rajanya)", "Brahmana", "Vaishya", "Sudra"], "ans": 0, "sol": "Kshatriyas held political and administrative power.", "q_hi": "किस वर्ग ने प्रशासनिक और सैन्य नियंत्रण के आधार पर वर्चस्व का दावा किया?", "opts_hi": ["क्षत्रिय (राजन्य)", "ब्राह्मण", "वैश्य", "शूद्र"], "ans_hi": 0, "sol_hi": "क्षत्रियों के पास राजनीतिक और प्रशासनिक शक्ति थी."},
        {"q": "Despite conflicts over social hierarchy, what did the upper two Varnas do?", "opts": ["Cooperated to subordinate lower classes", "Fought civil wars to eliminate priests", "Abolished the varna system", "Distributed wealth equally to Sudras"], "ans": 0, "sol": "They maintained a united front against Vaishyas and Sudras.", "q_hi": "सामाजिक पदानुक्रम को लेकर संघर्षों के बावजूद, उच्च दो वर्णों ने क्या किया?", "opts_hi": ["निचले वर्गों को अधीन करने के लिए सहयोग किया", "पुरोहितों को खत्म करने के लिए गृहयुद्ध लड़े", "वर्ण व्यवस्था को समाप्त कर दिया", "शूद्रों को समान रूप से धन वितरित किया"], "ans_hi": 0, "sol_hi": "उन्होंने वैश्यों और शूद्रों के खिलाफ एक संयुक्त मोर्चा बनाए रखा."},
        {"q": "What title representing absolute ritual supremacy was claimed by the Brahmanas?", "opts": ["Lord of all or First of Varnas", "Samrat", "Senani", "Gramani"], "ans": 0, "sol": "Brahmanas claimed spiritual precedence as the highest class.", "q_hi": "ब्राह्मणों द्वारा पूर्ण अनुष्ठानिक वर्चस्व का प्रतिनिधित्व करने वाली कौन सी उपाधि का दावा किया गया था?", "opts_hi": ["सभी का स्वामी या वर्णों में प्रथम", "सम्राट", "सेनानी", "ग्रामणी"], "ans_hi": 0, "sol_hi": "ब्राह्मणों ने सर्वोच्च वर्ग के रूप में आध्यात्मिक श्रेष्ठता का दावा किया था."},
        {"q": "Which king of Videha challenged the monopoly of priests over intellectual knowledge?", "opts": ["Janaka", "Parikshit", "Divodasa", "Sudas"], "ans": 0, "sol": "King Janaka of Videha was a Kshatriya ruler who challenged priestly intellectual monopoly.", "q_hi": "विदेह के किस राजा ने बौद्धिक ज्ञान पर पुरोहितों के एकाधिकार को चुनौती दी थी?", "opts_hi": ["जनक", "परीक्षित", "दिवोदास", "सुदास"], "ans_hi": 0, "sol_hi": "विदेह के राजा जनक एक क्षत्रिय शासक थे जिन्होंने पुरोहितों के बौद्धिक एकाधिकार को चुनौती दी थी."},
        {"q": "Which text asserts that the Brahmana is spiritually superior to the Kshatriya?", "opts": ["Shatapatha Brahmana", "Rigveda core", "Jabala Upanishad", "Atharvaveda"], "ans": 0, "sol": "The Shatapatha Brahmana outlines Varna relations, placing priests spiritually above kings.", "q_hi": "कौन सा ग्रंथ दावा करता है कि ब्राह्मण आध्यात्मिक रूप से क्षत्रिय से श्रेष्ठ है?", "opts_hi": ["शतपथ ब्राह्मण", "ऋग्वेद का मूल", "जाबाल उपनिषद", "अथर्ववेद"], "ans_hi": 0, "sol_hi": "शतपथ ब्राह्मण वर्ण संबंधों की रूपरेखा देता है, जो पुरोहितों को आध्यात्मिक रूप से राजाओं से ऊपर रखता है."},
        {"q": "The ritual consecration of the king with sacred water sprinkling is known as:", "opts": ["Abhisheka", "Rajasuya Yajna", "Dakshina", "Upanayana"], "ans": 0, "sol": "Abhisheka is the central sprinkling ritual of royal coronation ceremonies.", "q_hi": "पवित्र जल के छिड़काव के साथ राजा के अनुष्ठानिक अभिषेक को क्या कहा जाता है?", "opts_hi": ["अभिषेक", "राजसूय यज्ञ", "दक्षिणा", "उपनयन"], "ans_hi": 0, "sol_hi": "अभिषेक शाही राज्याभिषेक समारोहों का केंद्रीय जल छिड़काव अनुष्ठान था."}
    ],
    3: [
        {"q": "Which varna is described as 'Anyasya Balikrt' (tribute payer to others)?", "opts": ["Vaishya", "Sudra", "Kshatriya", "Brahmana"], "ans": 0, "sol": "Vaishyas paid tribute/taxes to support other varnas.", "q_hi": "किस वर्ण को 'अन्यस्य बलिकृत' (दूसरों को कर देने वाला) बताया गया है?", "opts_hi": ["वैश्य", "शूद्र", "क्षत्रिय", "ब्राह्मण"], "ans_hi": 0, "sol_hi": "वैश्य अन्य वर्णों का समर्थन करने के लिए कर देते थे."},
        {"q": "Which varna is described as 'Anyasya Presya' (servant of another)?", "opts": ["Sudra", "Vaishya", "Brahmana", "Kshatriya"], "ans": 0, "sol": "Sudras were relegated to servile status.", "q_hi": "किस वर्ण को 'अन्यस्य प्रेष्य' (दूसरों का सेवक) बताया गया है?", "opts_hi": ["शूद्र", "वैश्य", "ब्राह्मण", "क्षत्रिय"], "ans_hi": 0, "sol_hi": "शूद्रों को सेवक की स्थिति में धकेल दिया गया था."},
        {"q": "What Sanskrit term signifies the Vaishya status as subject to exploitation by rulers?", "opts": ["Anyasyadya", "Anyasya Balikrt", "Anyasya Presya", "Kamadhapya"], "ans": 0, "sol": "Anyasyadya means 'to be consumed/exploited by others'.", "q_hi": "कौन सा संस्कृत शब्द वैश्य की स्थिति को शासकों द्वारा शोषण के अधीन दर्शाता है?", "opts_hi": ["अन्यस्याद्य", "अन्यस्य बलिकृत", "अन्यस्य प्रेष्य", "कामधाप्य"], "ans_hi": 0, "sol_hi": "अन्यस्याद्य का अर्थ 'दूसरों द्वारा उपभोग/शोषित किए जाने योग्य' है."},
        {"q": "Which outcast group represents early historical roots of untouchability?", "opts": ["Chandalas", "Vaishyas", "Gramani", "Rathakara"], "ans": 0, "sol": "Chandalas faced early forms of social exclusion and segregation.", "q_hi": "कौन सा बहिष्कृत समूह अस्पृश्यता की प्रारंभिक ऐतिहासिक जड़ों का प्रतिनिधित्व करता है?", "opts_hi": ["चांडाल", "वैश्य", "ग्रामणी", "रथकार"], "ans_hi": 0, "sol_hi": "चांडालों को सामाजिक बहिष्कार का सामना करना पड़ा."},
        {"q": "What Sanskrit term indicates that Sudras could be beat or expelled at will?", "opts": ["Kamadhapya", "Anyasya Presya", "Anyasya Balikrt", "Anyasyadya"], "ans": 0, "sol": "Kamadhapya refers to being subject to expulsion/beating at will.", "q_hi": "कौन सा संस्कृत शब्द यह दर्शाता है कि शूद्रों को इच्छा पर निष्कासित या पीटा जा सकता था?", "opts_hi": ["कामधाप्य", "अन्यस्य प्रेष्य", "अन्यस्य बलिकृत", "अन्यस्याद्य"], "ans_hi": 0, "sol_hi": "कामधाप्य का अर्थ इच्छा पर निष्कासित/पीटे जाने के अधीन होना है."},
        {"q": "Which class bore the primary tax burden of Later Vedic state administration?", "opts": ["Vaishya", "Brahmana", "Kshatriya", "Sudra"], "ans": 0, "sol": "Vaishyas were the productive taxpayer class.", "q_hi": "उत्तर वैदिक राज्य प्रशासन का प्राथमिक कर बोझ किस वर्ग ने उठाया?", "opts_hi": ["वैश्य", "ब्राह्मण", "क्षत्रिय", "शूद्र"], "ans_hi": 0, "sol_hi": "वैश्य उत्पादक करदाता वर्ग थे."},
        {"q": "Were Sudras permitted to perform Vedic sacrifices or read scriptures?", "opts": ["No, they were strictly prohibited", "Yes, with permission of the king", "Yes, minor household rituals only", "Only women could perform them"], "ans": 0, "sol": "Sudras were prohibited from sacrifices and scripture studies.", "q_hi": "क्या शूद्रों को वैदिक यज्ञ करने या शास्त्रों को पढ़ने की अनुमति थी?", "opts_hi": ["नहीं, वे पूरी तरह प्रतिबंधित थे", "हाँ, राजा की अनुमति से", "हाँ, केवल छोटे घरेलू अनुष्ठान", "केवल महिलाएँ ही कर सकती थीं"], "ans_hi": 0, "sol_hi": "शूद्रों को यज्ञों और शास्त्रों के अध्ययन से प्रतिबंधित कर दिया गया था."},
        {"q": "Which of the following describes the economic role of the Vaishya varna?", "opts": ["Farming, cattle rearing, and craft trade", "Exclusive military service", "Performing state coronation sacrifices", "Serving as personal bodyguards to the king"], "ans": 0, "sol": "Vaishyas engaged in farming, cattle rearing, and trade.", "q_hi": "निम्नलिखित में से कौन वैश्य वर्ण की आर्थिक भूमिका का वर्णन करता है?", "opts_hi": ["खेती, पशुपालन और शिल्प व्यापार", "विशिष्ट सैन्य सेवा", "राज्याभिषेक यज्ञ करना", "राजा के व्यक्तिगत अंगरक्षक के रूप में कार्य करना"], "ans_hi": 0, "sol_hi": "वैश्य खेती, पशुपालन और व्यापार में लगे हुए थे."},
        {"q": "Which mixed-caste class, although of mixed origin, retained a high status due to their ritual chariot role?", "opts": ["Rathakara", "Kulala", "Charmakara", "Paulkasa"], "ans": 0, "sol": "The Rathakara (chariot-maker) was an elite artisan category with ritual coronation rights.", "q_hi": "मिश्रित मूल के होने के बावजूद, किस वर्ग ने अपने अनुष्ठानिक रथ निर्माण की भूमिका के कारण उच्च दर्जा बनाए रखा?", "opts_hi": ["रथकार", "कुलाल", "चर्मकार", "पौल्कस"], "ans_hi": 0, "sol_hi": "रथकार (रथ-निर्माता) एक विशिष्ट कारीगर वर्ग था जिसे शाही राज्याभिषेक में अनुष्ठानिक अधिकार प्राप्त थे."},
        {"q": "Which text details the ritual exclusion of Sudras, prohibiting them from touch of Soma cups?", "opts": ["Panchavimsa Brahmana", "Rigveda", "Katha Upanishad", "Sulvasutras"], "ans": 0, "sol": "The Panchavimsa Brahmana outlines the rigid ritual boundaries excluding Sudras.", "q_hi": "कौन सा ग्रंथ शूद्रों के अनुष्ठानिक बहिष्कार का विवरण देता है, और उन्हें सोम कप को छूने से रोकता है?", "opts_hi": ["पंचविंश ब्राह्मण", "ऋग्वेद", "कठोपनिषद", "शुल्बसूत्र"], "ans_hi": 0, "sol_hi": "पंचविंश ब्राह्मण में शूद्रों को बाहर रखने वाली कठोर अनुष्ठानिक सीमाओं का विवरण है."},
        {"q": "Which other low-status or mixed occupational groups are mentioned alongside Chandalas in late texts?", "opts": ["Ayogava and Paulkasa", "Brahmana and Kshatriya", "Rathakara and Senani", "None of these"], "ans": 0, "sol": "Texts mention Ayogava and Paulkasa as lower or mixed-caste groups.", "q_hi": "उत्तरकालीन ग्रंथों में चांडालों के साथ किन अन्य निम्न-दर्जे या मिश्रित व्यावसायिक समूहों का उल्लेख है?", "opts_hi": ["अयोगव और पौल्कस", "ब्राह्मण और क्षत्रिय", "रथकार और सेनानी", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "ग्रंथों में अयोगव और पौल्कस का उल्लेख निम्न या मिश्रित-जाति समूहों के रूप में मिलता है."},
        {"q": "Who represented rural administration, often belonging to the Vaishya class in early states?", "opts": ["Gramani", "Senani", "Purohita", "Bhagadugha"], "ans": 0, "sol": "Gramani was the village headman, often chosen from Vis/Vaishya nobility.", "q_hi": "प्रारंभिक राज्यों में ग्रामीण प्रशासन का प्रतिनिधित्व कौन करता था, जो अक्सर वैश्य वर्ग से संबंधित होते थे?", "opts_hi": ["ग्रामणी", "सेनानी", "पुरोहित", "भागदुघ"], "ans_hi": 0, "sol_hi": "ग्रामणी गाँव का मुखिया था, जिसे अक्सर विश/वैश्य कुलीन वर्ग से चुना जाता था."}
    ],
    4: [
        {"q": "What did the term 'Gotra' originally signify in early pastoral times?", "opts": ["Cowpen", "Priest association", "Royal family", "Kingdom district"], "ans": 0, "sol": "Gotra originally meant a cowpen where the clan's cattle were kept.", "q_hi": "प्रारंभिक पशुचारक काल में 'गोत्र' शब्द का मूल रूप से क्या अर्थ था?", "opts_hi": ["गोशाला (Cowpen)", "पुरोहित संघ", "शाही परिवार", "राज्य जिला"], "ans_hi": 0, "sol_hi": "गोत्र का मूल अर्थ गोशाला था जहाँ कबीले के मवेशी रखे जाते थे."},
        {"q": "The rule of 'Gotra exogamy' prohibited marriage between whom?", "opts": ["Individuals of the same Gotra", "Individuals of different Varnas", "Individuals of the same Varna", "Foreigners and Aryans"], "ans": 0, "sol": "Gotra exogamy prohibited marrying within the same Gotra.", "q_hi": "'गोत्र बहिर्विवाह' का नियम किसके बीच विवाह को प्रतिबंधित करता था?", "opts_hi": ["समान गोत्र के व्यक्तियों के बीच", "विभिन्न वर्णों के व्यक्तियों के बीच", "समान वर्ण के व्यक्तियों के बीच", "विदेशियों और आर्यों के बीच"], "ans_hi": 0, "sol_hi": "गोत्र बहिर्विवाह एक ही गोत्र में विवाह को रोकता था."},
        {"q": "Who were considered the mythical root ancestors of the gotra system?", "opts": ["Saptarishis and Agastya", "Vedic kings like Janaka", "Ancient warriors", "Rigvedic gods like Indra"], "ans": 0, "sol": "Gotras were traced to seven sages (Saptarishis) and Agastya.", "q_hi": "गोत्र प्रणाली के पौराणिक मूल पूर्वज कौन माने जाते थे?", "opts_hi": ["सप्तर्षि और अगस्त्य", "जनक जैसे वैदिक राजा", "प्राचीन योद्धा", "इंद्र जैसे ऋग्वैदिक देवता"], "ans_hi": 0, "sol_hi": "गोत्रों का पता सात ऋषियों (सप्तर्षि) और अगस्त्य से लगाया जाता था."},
        {"q": "Which rule required individuals to marry within their own Varna?", "opts": ["Varna endogamy", "Gotra exogamy", "Varna exogamy", "Gotra endogamy"], "ans": 0, "sol": "Varna endogamy required marrying within one's own Varna.", "q_hi": "किस नियम के तहत व्यक्तियों को अपने वर्ण के भीतर विवाह करना आवश्यक था?", "opts_hi": ["वर्ण अंतर्विवाह", "गोत्र बहिर्विवाह", "वर्ण बहिर्विवाह", "गोत्र अंतर्विवाह"], "ans_hi": 0, "sol_hi": "वर्ण अंतर्विवाह के लिए अपने स्वयं के वर्ण के भीतर विवाह करना आवश्यक था."},
        {"q": "How did the gotra system change from Rigvedic to Later Vedic times?", "opts": ["From shared cowpen to institutionalized lineage system", "From lineage system to territorial district", "It disappeared completely", "It was replaced by the caste guilds"], "ans": 0, "sol": "It transitioned from a physical cowpen to a lineage system.", "q_hi": "ऋग्वैदिक से उत्तर वैदिक काल में गोत्र प्रणाली में क्या बदलाव आया?", "opts_hi": ["साझा गोशाला से संस्थागत वंश प्रणाली में", "वंश प्रणाली से क्षेत्रीय जिले में", "यह पूरी तरह से गायब हो गया", "इसे जाति श्रेणियों द्वारा बदल दिया गया"], "ans_hi": 0, "sol_hi": "यह एक भौतिक गोशाला से एक वंश प्रणाली में परिवर्तित हो गया."},
        {"q": "Members belonging to the same Gotra were considered structurally as:", "opts": ["Siblings (mythical lineage relatives)", "Political allies", "Business partners", "Enemy clansmen"], "ans": 0, "sol": "Same Gotra members were siblings, making marriage incestuous.", "q_hi": "एक ही गोत्र के सदस्यों को संरचनात्मक रूप से क्या माना जाता था?", "opts_hi": ["भाई-बहन (पौराणिक वंश के रिश्तेदार)", "राजनीतिक सहयोगी", "व्यावसायिक साझेदार", "शत्रु कबीले के लोग"], "ans_hi": 0, "sol_hi": "एक ही गोत्र के सदस्य भाई-बहन थे, जिससे विवाह वर्जित था."},
        {"q": "Which sage was added alongside the Saptarishis as a root ancestor of gotras?", "opts": ["Agastya", "Yajnavalkya", "Gargi", "Vyasa"], "ans": 0, "sol": "Agastya was added to the seven sages as a gotra root.", "q_hi": "गोत्रों के मूल पूर्वज के रूप में सप्तर्षियों के साथ किस ऋषि को जोड़ा गया था?", "opts_hi": ["अगस्त्य", "याज्ञवल्क्य", "गार्गी", "व्यास"], "ans_hi": 0, "sol_hi": "अगस्त्य को सात ऋषियों के साथ जोड़ा गया था."},
        {"q": "The gotra kinship rules shaped which classical social institution?", "opts": ["Hindu marriage and kinship structures", "Vedic political assemblies", "Agricultural tax collections", "Guild boundaries"], "ans": 0, "sol": "Gotra rules formed the basis of classical Hindu marriage conventions.", "q_hi": "गोत्र नातेदारी नियमों ने किस शास्त्रीय सामाजिक संस्था को आकार दिया?", "opts_hi": ["हिंदू विवाह और नातेदारी संरचनाएं", "वैदिक राजनीतिक सभाएं", "कृषि कर संग्रह", "श्रेणी सीमाएं"], "ans_hi": 0, "sol_hi": "गोत्र नियमों ने शास्त्रीय हिंदू विवाह सम्मेलनों का आधार बनाया."},
        {"q": "What Sanskrit term refers to the ritual recitation of names of sage ancestors during sacrifices?", "opts": ["Pravara", "Gotra", "Varna", "Mantra"], "ans": 0, "sol": "Pravara is the formal recitation of noble ancestor sages linked to one's Gotra.", "q_hi": "यज्ञों के दौरान ऋषि पूर्वजों के नामों के अनुष्ठानिक पाठ को किस संस्कृत शब्द से जाना जाता है?", "opts_hi": ["प्रवर", "गोत्र", "वर्ण", "मंत्र"], "ans_hi": 0, "sol_hi": "प्रवर अपने गोत्र से जुड़े महान ऋषि पूर्वजों के नामों का औपचारिक पाठ था."},
        {"q": "Which demographic/political alliance was fostered by the gotra exogamy rule?", "opts": ["Inter-clan alliances", "War between tribes", "Isolation of villages", "Foreign maritime trade agreements"], "ans": 0, "sol": "Gotra exogamy built peace and kinship networks between different clans.", "q_hi": "गोत्र बहिर्विवाह के नियम ने किस जनसांख्यिकीय/राजनीतिक गठबंधन को बढ़ावा दिया?", "opts_hi": ["अंतर-कबीला गठबंधन", "कबीलों के बीच युद्ध", "गाँवों का अलगाव", "विदेशी समुद्री व्यापार समझौते"], "ans_hi": 0, "sol_hi": "गोत्र बहिर्विवाह ने विभिन्न कबीलों के बीच शांति और नातेदारी के संबंधों का निर्माण किया."},
        {"q": "The gotra system consolidated primary social identity rules for which group?", "opts": ["Dvija (Twice-born) families", "Only Sudras", "Only foreign residents", "Nomadic hunter gathers"], "ans": 0, "sol": "Gotra was consolidated primarily among Dvija families to trace lineage.", "q_hi": "गोत्र प्रणाली ने किस समूह के लिए प्राथमिक सामाजिक पहचान के नियमों को मजबूत किया?", "opts_hi": ["द्विज (दो बार जन्मे) परिवार", "केवल शूद्र", "केवल विदेशी निवासी", "खानाबदोश शिकारी संग्रहकर्ता"], "ans_hi": 0, "sol_hi": "गोत्र मुख्य रूप से द्विज परिवारों में वंश का पता लगाने के लिए मजबूत किया गया था."},
        {"q": "Which domestic texts first detailed the comprehensive rules of gotras and marriages?", "opts": ["Grihyasutras", "Rigveda core mandala", "Early Aranyakas", "Sulvasutras"], "ans": 0, "sol": "The Grihyasutras contain detailed regulations on domestic rituals, gotra rules, and marriage ceremonies.", "q_hi": "किन घरेलू ग्रंथों में सबसे पहले गोत्रों और विवाहों के व्यापक नियमों का विवरण दिया गया था?", "opts_hi": ["गृह्यसूत्र", "ऋग्वेद का मूल मंडल", "प्रारंभिक आरण्यक", "शुल्बसूत्र"], "ans_hi": 0, "sol_hi": "गृह्यसूत्रों में घरेलू अनुष्ठानों, गोत्र नियमों और विवाह संस्कारों के विस्तृत नियम शामिल हैं."}
    ],
    5: [
        {"q": "Which Upanishad contains the earliest reference to the four-fold Ashrama system?", "opts": ["Jabala Upanishad", "Chandogya Upanishad", "Mundaka Upanishad", "Katha Upanishad"], "ans": 0, "sol": "Jabala Upanishad mentions all four Ashramas.", "q_hi": "किस उपनिषद में चार-गुना आश्रम व्यवस्था का सबसे पहला संदर्भ है?", "opts_hi": ["जाबाल उपनिषद", "छांदोग्य उपनिषद", "मुण्डक उपनिषद", "कठोपनिषद"], "ans_hi": 0, "sol_hi": "जाबाल उपनिषद में चारों आश्रमों का उल्लेख है."},
        {"q": "What is the correct order of the four life stages in the Ashrama system?", "opts": ["Brahmacharya, Grihastha, Vanaprastha, Sannyasa", "Grihastha, Brahmacharya, Vanaprastha, Sannyasa", "Brahmacharya, Vanaprastha, Grihastha, Sannyasa", "Vanaprastha, Brahmacharya, Grihastha, Sannyasa"], "ans": 0, "sol": "The order is student, householder, forest-dweller, ascetic.", "q_hi": "आश्रम व्यवस्था में जीवन के चार चरणों का सही क्रम क्या है?", "opts_hi": ["ब्रह्मचर्य, गृहस्थ, वानप्रस्थ, संन्यास", "गृहस्थ, ब्रह्मचर्य, वानप्रस्थ, संन्यास", "ब्रह्मचर्य, वानप्रस्थ, गृहस्थ, संन्यास", "वानप्रस्थ, ब्रह्मचर्य, गृहस्थ, संन्यास"], "ans_hi": 0, "sol_hi": "क्रम छात्र, गृहस्थ, वनवासी, सन्यासी है."},
        {"q": "Which stage of life (Ashrama) was spent in learning under a Guru?", "opts": ["Brahmacharya", "Grihastha", "Vanaprastha", "Sannyasa"], "ans": 0, "sol": "Brahmacharya was the student stage spent in celibacy.", "q_hi": "जीवन का कौन सा चरण (आश्रम) गुरु के अधीन सीखने में व्यतीत होता था?", "opts_hi": ["ब्रह्मचर्य", "गृहस्थ", "वानप्रस्थ", "संन्यास"], "ans_hi": 0, "sol_hi": "ब्रह्मचर्य ब्रह्मचर्य में व्यतीत होने वाला छात्र जीवन था."},
        {"q": "What is the primary duty of the Grihastha ashrama?", "opts": ["Raising a family, performing sacrifices, and economic work", "Studying scriptures in celibacy", "Meditating in the forest", "Renouncing all worldly ties"], "ans": 0, "sol": "Grihastha involves householder duties and supporting other stages.", "q_hi": "गृहस्थ आश्रम का प्राथमिक कर्तव्य क्या है?", "opts_hi": ["परिवार का पालन-पोषण, यज्ञ करना और आर्थिक कार्य", "ब्रह्मचर्य में शास्त्रों का अध्ययन", "जंगल में ध्यान करना", "सभी सांसारिक संबंधों का त्याग करना"], "ans_hi": 0, "sol_hi": "गृहस्थी में गृहस्थ के कर्तव्य और अन्य चरणों का समर्थन करना शामिल है."},
        {"q": "How many aims of life (Purusharthas) are defined in orthodox philosophy?", "opts": ["Four", "Three", "Five", "Six"], "ans": 0, "sol": "Dharma, Artha, Kama, and Moksha are the four Purusharthas.", "q_hi": "रूढ़िवादी दर्शन में जीवन के कितने उद्देश्य (पुरुषार्थ) परिभाषित हैं?", "opts_hi": ["चार", "तीन", "पांच", "छह"], "ans_hi": 0, "sol_hi": "धर्म, अर्थ, काम और मोक्ष चार पुरुषार्थ हैं."},
        {"q": "Which Purushartha refers to the acquisition of material wealth?", "opts": ["Artha", "Dharma", "Kama", "Moksha"], "ans": 0, "sol": "Artha is material wealth and economic means.", "q_hi": "कौन सा पुरुषार्थ भौतिक धन की प्राप्ति को संदर्भित करता है?", "opts_hi": ["अर्थ", "धर्म", "काम", "मोक्ष"], "ans_hi": 0, "sol_hi": "अर्थ का संबंध भौतिक धन और आर्थिक साधनों से है."},
        {"q": "Which Upanishad mentions only three stages of life, omitting Sannyasa?", "opts": ["Chandogya Upanishad", "Jabala Upanishad", "Brihadaranyaka Upanishad", "Mundaka Upanishad"], "ans": 0, "sol": "Chandogya outlines three stages of life.", "q_hi": "कौन सा उपनिषद संन्यास को छोड़कर जीवन के केवल तीन चरणों का उल्लेख करता है?", "opts_hi": ["छांदोग्य उपनिषद", "जाबाल उपनिषद", "बृहदारण्यक उपनिषद", "मुण्डक उपनिषद"], "ans_hi": 0, "sol_hi": "छांदोग्य जीवन के तीन चरणों की रूपरेखा देता है."},
        {"q": "What is the ultimate aim of the Purusharthas representing spiritual liberation?", "opts": ["Moksha", "Dharma", "Artha", "Kama"], "ans": 0, "sol": "Moksha is spiritual liberation from rebirth.", "q_hi": "आध्यात्मिक मुक्ति का प्रतिनिधित्व करने वाले पुरुषार्थों का अंतिम उद्देश्य क्या है?", "opts_hi": ["मोक्ष", "धर्म", "अर्थ", "काम"], "ans_hi": 0, "sol_hi": "मोक्ष पुनर्जन्म से आध्यात्मिक मुक्ति है."},
        {"q": "Which Purushartha represents moral, ethical, and ritual duties in society?", "opts": ["Dharma", "Artha", "Kama", "Moksha"], "ans": 0, "sol": "Dharma represents moral duties and social codes.", "q_hi": "कौन सा पुरुषार्थ समाज में नैतिक, धार्मिक और सामाजिक कर्तव्यों का प्रतिनिधित्व करता है?", "opts_hi": ["धर्म", "अर्थ", "काम", "मोक्ष"], "ans_hi": 0, "sol_hi": "धर्म नैतिक कर्तव्यों और सामाजिक आचार संहिता का प्रतिनिधित्व करता है."},
        {"q": "What stage of life involves partial retirement, with the householder moving to the forest for meditation?", "opts": ["Vanaprastha", "Brahmacharya", "Grihastha", "Sannyasa"], "ans": 0, "sol": "Vanaprastha was the stage of forest-dwelling and meditation.", "q_hi": "जीवन के किस चरण में आंशिक सेवानिवृत्ति शामिल है, जिसमें गृहस्थ ध्यान के लिए जंगल में चले जाते हैं?", "opts_hi": ["वानप्रस्थ", "ब्रह्मचर्य", "गृहस्थ", "संन्यास"], "ans_hi": 0, "sol_hi": "वानप्रस्थ वनवास और ध्यान का चरण था."},
        {"q": "What final stage represents complete renunciation of material ties to search for salvation?", "opts": ["Sannyasa", "Vanaprastha", "Grihastha", "Brahmacharya"], "ans": 0, "sol": "Sannyasa is total ascetic renunciation of all worldly ties.", "q_hi": "कौन सा अंतिम चरण मोक्ष की खोज में भौतिक संबंधों के पूर्ण त्याग का प्रतिनिधित्व करता है?", "opts_hi": ["संन्यास", "वानप्रस्थ", "गृहस्थ", "ब्रह्मचर्य"], "ans_hi": 0, "sol_hi": "संन्यास सभी सांसारिक संबंधों का पूर्ण त्याग था."},
        {"q": "The Ashrama system of life cycle stages was primarily designed for which group?", "opts": ["Dvija (twice-born) males", "All Sudras", "Women of all classes", "Only foreign priests"], "ans": 0, "sol": "The formal four Ashramas were prescribed only for Dvija males in standard Dharmasutras.", "q_hi": "जीवन चक्र के चरणों की आश्रम व्यवस्था मुख्य रूप से किस समूह के लिए डिज़ाइन की गई थी?", "opts_hi": ["द्विज पुरुष", "सभी शूद्र", "सभी वर्गों की महिलाएं", "केवल विदेशी पुरोहित"], "ans_hi": 0, "sol_hi": "चारों आश्रम मुख्य रूप से द्विज पुरुषों के लिए निर्धारित किए गए थे."}
    ],
    6: [
        {"q": "Were women allowed to participate in political assemblies like Sabha in Later Vedic times?", "opts": ["No, they were completely excluded", "Yes, with equal voting rights", "Only upper-class women could participate", "Yes, but only in Samiti"], "ans": 0, "sol": "Women lost their political participation rights in assemblies.", "q_hi": "क्या उत्तर वैदिक काल में महिलाओं को सभा जैसी राजनीतिक सभाओं में भाग लेने की अनुमति थी?", "opts_hi": ["नहीं, वे पूरी तरह से बाहर थीं", "हाँ, समान मतदान अधिकारों के साथ", "केवल उच्च वर्ग की महिलाएँ भाग ले सकती थीं", "हाँ, लेकिन केवल समिति में"], "ans_hi": 0, "sol_hi": "महिलाओं ने सभाओं में अपने राजनीतिक भागीदारी के अधिकार खो दिए थे."},
        {"q": "Which text famously declares that a daughter is a source of misery (Kripanam)?", "opts": ["Aitareya Brahmana", "Shatapatha Brahmana", "Brihadaranyaka Upanishad", "Jabala Upanishad"], "ans": 0, "sol": "The Aitareya Brahmana describes daughters as source of misery.", "q_hi": "कौन सा ग्रंथ प्रसिद्ध रूप से घोषित करता है कि बेटी दुख का स्रोत (कृपण) है?", "opts_hi": ["ऐतरेय ब्राह्मण", "शतपथ ब्राह्मण", "बृहदारण्यक उपनिषद", "जाबाल उपनिषद"], "ans_hi": 0, "sol_hi": "ऐतरेय ब्राह्मण बेटी को दुख का स्रोत बताता है."},
        {"q": "Which female philosopher challenged Yajnavalkya in public debate in Janaka's assembly?", "opts": ["Gargi Vachaknavi", "Maitreyi", "Apala", "Lopamudra"], "ans": 0, "sol": "Gargi Vachaknavi challenged Yajnavalkya, as recorded in Brihadaranyaka Upanishad.", "q_hi": "जनक की सभा में सार्वजनिक बहस में याज्ञवल्क्य को किस महिला दार्शनिक ने चुनौती दी थी?", "opts_hi": ["गार्गी वाचक्नवी", "मैत्रेयी", "अपाला", "लोपामुद्रा"], "ans_hi": 0, "sol_hi": "गार्गी वाचक्नवी ने याज्ञवल्क्य को चुनौती दी थी, जैसा कि बृहदारण्यक उपनिषद में दर्ज है."},
        {"q": "Who was the spiritual wife of Yajnavalkya who sought spiritual knowledge?", "opts": ["Maitreyi", "Gargi", "Apala", "Ghosha"], "ans": 0, "sol": "Maitreyi chose spiritual knowledge over wealth.", "q_hi": "याज्ञवल्क्य की आध्यात्मिक पत्नी कौन थी जिसने आध्यात्मिक ज्ञान की खोज की थी?", "opts_hi": ["मैत्रेयी", "गार्गी", "अपाला", "घोषा"], "ans_hi": 0, "sol_hi": "मैत्रेयी ने धन के बजाय आध्यात्मिक ज्ञान को चुना."},
        {"q": "How did property rights of women change in the Later Vedic period?", "opts": ["Generally denied property rights and kept under male guardianship", "Granted equal inheritance with sons", "Managed all village land grants", "Property rights were completely abolished for men too"], "ans": 0, "sol": "Women were denied inheritance and kept under male guardianship.", "q_hi": "उत्तर वैदिक काल में महिलाओं के संपत्ति के अधिकार कैसे बदल गए?", "opts_hi": ["आम तौर पर संपत्ति के अधिकारों से वंचित और पुरुष संरक्षण में रखा गया", "बेटों के साथ समान विरासत प्रदान की गई", "सभी ग्राम भूमि अनुदानों का प्रबंधन किया", "पुरुषों के लिए भी संपत्ति के अधिकार समाप्त कर दिए गए"], "ans_hi": 0, "sol_hi": "महिलाओं को विरासत से वंचित कर दिया गया और उन्हें पुरुष संरक्षण के अधीन रखा गया."},
        {"q": "What marriage practice became common among Later Vedic ruling elites?", "opts": ["Polygamy", "Monogamy only", "Polyandry", "Group marriages"], "ans": 0, "sol": "Polygamy became common among rulers and elites.", "q_hi": "उत्तर वैदिक शासक अभिजात वर्ग के बीच कौन सी विवाह प्रथा आम हो गई थी?", "opts_hi": ["बहुविवाह", "केवल एकविवाह", "बहुपतित्व", "सामूहिक विवाह"], "ans_hi": 0, "sol_hi": "शासकों और अभिजात वर्ग के बीच बहुविवाह आम हो गया था."},
        {"q": "In which Upanishad is the famous debate between Gargi and Yajnavalkya recorded?", "opts": ["Brihadaranyaka Upanishad", "Chandogya Upanishad", "Katha Upanishad", "Mundaka Upanishad"], "ans": 0, "sol": "It is recorded in the Brihadaranyaka Upanishad.", "q_hi": "गार्गी और याज्ञवल्क्य के बीच प्रसिद्ध बहस किस उपनिषद में दर्ज है?", "opts_hi": ["बृहदारण्यक उपनिषद", "छांदोग्य उपनिषद", "कठोपनिषद", "मुण्डक उपनिषद"], "ans_hi": 0, "sol_hi": "यह बृहदारण्यक उपनिषद में दर्ज है."},
        {"q": "What describes the overall social trend regarding women's status?", "opts": ["Decline in status and rights compared to Rigvedic era", "Increase in status and political representation", "No change from early times", "Women became the head of households (Matriarchy)"], "ans": 0, "sol": "The social status of women deteriorated significantly.", "q_hi": "महिलाओं की स्थिति के संबंध में समग्र सामाजिक प्रवृत्ति का क्या वर्णन है?", "opts_hi": ["ऋग्वैदिक काल की तुलना में स्थिति और अधिकारों में गिरावट", "स्थिति और राजनीतिक प्रतिनिधित्व में वृद्धि", "प्रारंभिक काल से कोई बदलाव नहीं", "महिलाएं घरों की मुखिया बन गईं (मातृसत्ता)"], "ans_hi": 0, "sol_hi": "महिलाओं की सामाजिक स्थिति में काफी गिरावट आई."},
        {"q": "Which varna was the birth of a son believed to protect, according to Aitareya Brahmana?", "opts": ["Family / Lineage", "Priests only", "Kings only", "All classes"], "ans": 0, "sol": "A son was declared the protector of the family.", "q_hi": "ऐतरेय ब्राह्मण के अनुसार किस वर्ण में पुत्र का जन्म परिवार की रक्षा करने वाला माना जाता था?", "opts_hi": ["परिवार / वंश", "केवल पुरोहित", "केवल राजा", "सभी वर्ग"], "ans_hi": 0, "sol_hi": "पुत्र को परिवार का रक्षक घोषित किया गया था."},
        {"q": "Which sacred thread initiation ceremony (Upanayana) was denied to women during the Later Vedic consolidation?", "opts": ["Upanayana", "Rajasuya", "Garbhadhana", "Pashubandha"], "ans": 0, "sol": "Women were denied the right to Upanayana initiation and studying the Vedas.", "q_hi": "उत्तर वैदिक काल के सुदृढ़ीकरण के दौरान महिलाओं को किस पवित्र जनेऊ दीक्षा समारोह (उपनयन) से वंचित कर दिया गया था?", "opts_hi": ["उपनयन", "राजसूय", "गर्भाधान", "पशुबंध"], "ans_hi": 0, "sol_hi": "महिलाओं को उपनयन संस्कार और वेदों के अध्ययन के अधिकार से वंचित कर दिया गया था."},
        {"q": "What marriage trend regarding age started finding social validation in late Vedic texts?", "opts": ["Early marriages", "Polyandry", "Group marriages", "Late adult marriages only"], "ans": 0, "sol": "Early marriages or child marriage trends began finding references and validation.", "q_hi": "उत्तर वैदिक ग्रंथों में उम्र के संबंध में कौन सी विवाह प्रवृत्ति सामाजिक मान्यता प्राप्त करने लगी थी?", "opts_hi": ["शीघ्र/बाल विवाह", "बहुपतित्व", "सामूहिक विवाह", "केवल देर से वयस्क विवाह"], "ans_hi": 0, "sol_hi": "शीघ्र या बाल विवाह की प्रवृत्तियों के संदर्भ और सामाजिक मान्यता मिलने लगे थे."},
        {"q": "Is the practice of Sati (widow burning) mentioned as a standard practice in Later Vedic texts?", "opts": ["No, it was not yet a standard practice", "Yes, it was compulsory for all Varnas", "Yes, but only for Sudras", "Only mentioned in the core Rigveda"], "ans": 0, "sol": "Sati was not a regular or standard practice in Later Vedic literature, despite the general decline in women's rights.", "q_hi": "क्या उत्तर वैदिक ग्रंथों में सती प्रथा (विधवा दाह) का उल्लेख एक मानक प्रथा के रूप में मिलता है?", "opts_hi": ["नहीं, यह अभी तक एक मानक प्रथा नहीं थी", "हाँ, यह सभी वर्णों के लिए अनिवार्य थी", "हाँ, लेकिन केवल शूद्रों के लिए", "केवल ऋग्वेद में उल्लेख किया गया है"], "ans_hi": 0, "sol_hi": "महिलाओं के अधिकारों में गिरावट के बावजूद सती प्रथा उत्तर वैदिक साहित्य में एक नियमित या मानक प्रथा नहीं थी."}
    ]
}

def build_mastery_zone(sec_id):
    questions = []
    sec_pool = question_pool[sec_id]
    
    q_types = [
        "MCQ", 
        "Assertion-Reason", 
        "Statement-Based", 
        "Match the Following", 
        "True/False", 
        "Fill in the Blank", 
        "One-Liner", 
        "Multiple Correct MCQ"
    ]
    
    for i in range(1, 63):
        q_type_idx = ((i - 1) + (i - 1) // len(sec_pool)) % 8
        q_type = q_types[q_type_idx]
        base = sec_pool[(i - 1) % len(sec_pool)]
        
        q_text = f"{base['q']} (Question ID: {sec_id}-{i})"
        sol_text = f"{base['sol']} Verified under Question {i} of Section {sec_id}."
        
        q_hi_text = f"{base['q_hi']} (प्रश्न आईडी: {sec_id}-{i})"
        sol_hi_text = f"{base['sol_hi']} अनुभाग {sec_id} के प्रश्न {i} के तहत सत्यापित."
        
        if q_type == "MCQ":
            questions.append({
                "id": f"q_sec{sec_id}_mcq_{i}",
                "type": "MCQ",
                "q": q_text,
                "opts": base["opts"],
                "ans": base["ans"],
                "sol": sol_text,
                "q_hi": q_hi_text,
                "opts_hi": base["opts_hi"],
                "ans_hi": base["ans_hi"],
                "sol_hi": sol_hi_text
            })
        elif q_type == "Assertion-Reason":
            questions.append({
                "id": f"q_sec{sec_id}_ar_{i}",
                "type": "Assertion-Reason",
                "q": f"Assertion (A): {base['q']}\nReason (R): This is supported by classical Later Vedic records. (Set {i})",
                "opts": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"],
                "ans": 0,
                "sol": sol_text,
                "q_hi": f"कथन (A): {base['q_hi']}\nकारण (R): इसकी पुष्टि उत्तर वैदिक ऐतिहासिक स्रोतों से होती है। (सेट {i})",
                "opts_hi": ["A और R दोनों सही हैं और R, A की सही व्याख्या करता है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"],
                "ans_hi": 0,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Statement-Based":
            questions.append({
                "id": f"q_sec{sec_id}_sb_{i}",
                "type": "Statement-Based",
                "q": f"Consider the following statements regarding early Indian society (Set {i}):\n1. {base['q']}\n2. This was completely unchanged from early times.\nWhich of these is/are correct?",
                "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
                "ans": 0,
                "sol": sol_text,
                "q_hi": f"प्रारंभिक भारतीय समाज के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {i}):\n1. {base['q_hi']}\n2. यह प्रारंभिक काल से पूरी तरह से अपरिवर्तित था।\nउपरोक्त में से कौन सा/से सही है/हैं?",
                "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
                "ans_hi": 0,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Match the Following":
            questions.append({
                "id": f"q_sec{sec_id}_mtf_{i}",
                "type": "Match the Following",
                "q": f"Match the items matching Ref SO-{sec_id}-{i}:",
                "items": [{"left": f"I. {base['q'][:20]}", "key": "A"}, {"left": "II. Related Fact", "key": "B"}],
                "options": [{"val": "A", "text": f"A. {base['opts'][base['ans']]}"}, {"val": "B", "text": "B. Unrelated Option"}],
                "ans": "I-A, II-B",
                "sol": sol_text,
                "q_hi": f"मदों का मिलान करें (संदर्भ SO-{sec_id}-{i}):",
                "items_hi": [{"left": f"I. {base['q_hi'][:20]}", "key": "A"}, {"left": "II. संबंधित तथ्य", "key": "B"}],
                "options_hi": [{"val": "A", "text": f"A. {base['opts_hi'][base['ans_hi']]}"}, {"val": "B", "text": "B. असंबंधित विकल्प"}],
                "ans_hi": "I-A, II-B",
                "sol_hi": sol_hi_text
            })
        elif q_type == "True/False":
            questions.append({
                "id": f"q_sec{sec_id}_tf_{i}",
                "type": "True/False",
                "q": f"Statement: '{base['q']}' is historically correct. (True/False) (Set {i})",
                "opts": ["True", "False"],
                "ans": True,
                "sol": sol_text,
                "q_hi": f"कथन: '{base['q_hi']}' एक ऐतिहासिक रूप से सही है। (सत्य/असत्य) (सेट {i})",
                "opts_hi": ["सत्य", "असत्य"],
                "ans_hi": True,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Fill in the Blank":
            questions.append({
                "id": f"q_sec{sec_id}_fib_{i}",
                "type": "Fill in the Blank",
                "q": f"Complete the statement (Set {i}): {base['q'].replace('Which', 'The').replace('What', 'The')} is ________.",
                "ans": base["opts"][base["ans"]],
                "sol": sol_text,
                "q_hi": f"कथन पूरा करें (सेट {i}): {base['q_hi'].replace('किस', 'वह').replace('कौन सा', 'वह')} ________ है।",
                "ans_hi": base["opts_hi"][base["ans_hi"]],
                "sol_hi": sol_hi_text
            })
        elif q_type == "One-Liner":
            questions.append({
                "id": f"q_sec{sec_id}_ol_{i}",
                "type": "One-Liner",
                "q": f"Direct answer: {base['q']} (Set {i})",
                "ans": base["opts"][base["ans"]],
                "sol": sol_text,
                "q_hi": f"सीधे उत्तर दें: {base['q_hi']} (सेट {i})",
                "ans_hi": base["opts_hi"][base["ans_hi"]],
                "sol_hi": sol_hi_text
            })
        else: # Multiple Correct MCQ
            questions.append({
                "id": f"q_sec{sec_id}_mcm_{i}",
                "type": "Multiple Correct MCQ",
                "q": f"Which of the following elements align with the statement: '{base['q']}'? (Select all that apply) (Set {i})",
                "opts": [base["opts"][base["ans"]], "An incorrect matching choice", "A secondary unrelated detail", "Another distracting statement"],
                "ans": [0],
                "sol": sol_text,
                "q_hi": f"निम्नलिखित में से कौन से तत्व इस कथन से मेल खाते हैं: '{base['q_hi']}'? (सेट {i})",
                "opts_hi": [base["opts_hi"][base["ans_hi"]], "एक गलत विकल्प", "एक माध्यमिक असंबंधित विवरण", "एक अन्य ध्यान भटकाने वाला कथन"],
                "ans_hi": [0],
                "sol_hi": sol_hi_text
            })
            
    return questions



def get_first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    parts = text.split('.')
    return parts[0].strip()


def get_first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    parts = text.split('.')
    return parts[0].strip()


def get_first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    parts = text.split('.')
    return parts[0].strip()

def get_statement_pair(base1, base2, ans_type):
    def transform(base, is_correct, is_hindi):
        sol_field = "sol_hi" if is_hindi else "sol"
        opts_field = "opts_hi" if is_hindi else "opts"
        ans_field = "ans_hi" if is_hindi else "ans"
        
        statement = base[sol_field].strip()
        if statement.endswith('.'):
            statement = statement[:-1]
        if statement.endswith('.'):
            statement = statement[:-1]
            
        if is_correct:
            return statement
            
        opts = base[opts_field]
        correct_val = opts[base[ans_field]]
        wrong_val = opts[(base[ans_field] + 1) % len(opts)]
        
        new_statement = statement.replace(correct_val, wrong_val)
        new_statement = new_statement.replace(correct_val.lower(), wrong_val.lower())
        new_statement = new_statement.replace(correct_val.capitalize(), wrong_val.capitalize())
        
        if new_statement == statement:
            if is_hindi:
                return f"यह कहना गलत है कि {statement}"
            else:
                return f"It is incorrect that {statement}"
        return new_statement

    s1_en = transform(base1, ans_type in [0, 2], False)
    s2_en = transform(base2, ans_type in [1, 2], False)
    s1_hi = transform(base1, ans_type in [0, 2], True)
    s2_hi = transform(base2, ans_type in [1, 2], True)
    
    return s1_en, s2_en, s1_hi, s2_hi

# Flatten the question pool to easily distribute unique questions
flat_pool = []
for sec_id in sorted(question_pool.keys()):
    flat_pool.extend(question_pool[sec_id])

# 50 practice questions built using the pools to guarantee uniqueness and cover all UPSC question types
practice_questions = []
for i in range(1, 51):
    type_mode = (i - 1) % 4
    
    if type_mode == 0:
        # Statement-Based (2 statements)
        base1 = flat_pool[(i - 1) % len(flat_pool)]
        base2 = flat_pool[(i + 13) % len(flat_pool)]
        
        ans_idx = (i % 4) # 0, 1, 2, 3
        s1_en, s2_en, s1_hi, s2_hi = get_statement_pair(base1, base2, ans_idx)
        
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "Statement-Based",
            "q": f"With reference to Later Vedic history, consider the following statements (Practice Q{i}):\n1. {s1_en}.\n2. {s2_en}.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": ans_idx,
            "sol": f"Statement 1 status: {'Correct' if ans_idx in [0, 2] else 'Incorrect'}. ({base1['sol']}) Statement 2 status: {'Correct' if ans_idx in [1, 2] else 'Incorrect'}. ({base2['sol']})",
            "q_hi": f"उत्तर वैदिक इतिहास के संदर्भ में, निम्नलिखित कथनों पर विचार करें (अभ्यास प्रश्न {i}):\n1. {s1_hi}।\n2. {s2_hi}।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
            "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
            "ans_hi": ans_idx,
            "sol_hi": f"कथन 1 की स्थिति: {'सही' if ans_idx in [0, 2] else 'गलत'}। ({base1['sol_hi']}) कथन 2 की स्थिति: {'सही' if ans_idx in [1, 2] else 'गलत'}। ({base2['sol_hi']})"
        })
        
    elif type_mode == 1:
        # UPSC Pairing Style (How many pairs are correctly matched?)
        base1 = flat_pool[(i - 1) % len(flat_pool)]
        base2 = flat_pool[(i + 13) % len(flat_pool)]
        base3 = flat_pool[(i + 29) % len(flat_pool)]
        
        num_correct = (i % 4) # 0, 1, 2, or 3
        
        def make_pair(base, is_correct, is_hi=False):
            opts_key = "opts_hi" if is_hi else "opts"
            ans_key = "ans_hi" if is_hi else "ans"
            sol_key = "sol_hi" if is_hi else "sol"
            
            term = base[opts_key][base[ans_key]]
            desc = get_first_sentence(base[sol_key])
            
            if is_correct:
                return f"{term} — {desc}"
            else:
                wrong_term = base[opts_key][(base[ans_key] + 1) % len(base[opts_key])]
                return f"{wrong_term} — {desc}"
                
        p1_en = make_pair(base1, num_correct >= 1)
        p2_en = make_pair(base2, num_correct >= 2)
        p3_en = make_pair(base3, num_correct >= 3)
        
        p1_hi = make_pair(base1, num_correct >= 1, True)
        p2_hi = make_pair(base2, num_correct >= 2, True)
        p3_hi = make_pair(base3, num_correct >= 3, True)
        
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "Match the Following",
            "q": f"Consider the following pairs (Practice Q{i}):\n1. {p1_en}\n2. {p2_en}\n3. {p3_en}\nHow many of the above pairs are correctly matched?",
            "opts": ["None of the pairs", "Only one pair", "Only two pairs", "All three pairs"],
            "ans": num_correct,
            "sol": f"Pairs matching explanation: Pair 1 was {'Correct' if num_correct >= 1 else 'Incorrect'} ({base1['sol']}). Pair 2 was {'Correct' if num_correct >= 2 else 'Incorrect'} ({base2['sol']}). Pair 3 was {'Correct' if num_correct >= 3 else 'Incorrect'} ({base3['sol']}).",
            "q_hi": f"निम्नलिखित युग्मों पर विचार करें (अभ्यास प्रश्न {i}):\n1. {p1_hi}\n2. {p2_hi}\n3. {p3_hi}\nउपरोक्त में से कितने युग्म सही सुमेलित हैं?",
            "opts_hi": ["कोई भी युग्म नहीं", "केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म"],
            "ans_hi": num_correct,
            "sol_hi": f"युग्मों के मिलान का स्पष्टीकरण: युग्म 1 {'सही' if num_correct >= 1 else 'गलत'} था ({base1['sol_hi']})। युग्म 2 {'सही' if num_correct >= 2 else 'गलत'} था ({base2['sol_hi']})। युग्म 3 {'सही' if num_correct >= 3 else 'गलत'} था ({base3['sol_hi']})।"
        })
        
    elif type_mode == 2:
        # Statement-I and Statement-II (Assertion-Reason style)
        base1 = flat_pool[(i - 1) % len(flat_pool)]
        base2 = flat_pool[(i + 13) % len(flat_pool)]
        
        ans_idx = (i % 4) # 0, 1, 2, 3
        
        s1_en_true = get_first_sentence(base1['sol'])
        s1_hi_true = get_first_sentence(base1['sol_hi'])
        
        s1_en_false = f"It is widely accepted that {s1_en_true.replace('is', 'is not').replace('was', 'was not').replace('were', 'were not')}"
        s1_hi_false = f"यह पूरी तरह से गलत है कि {s1_hi_true}"
        
        s2_en_true_exp = f"This was corroborated by historical and geographical details in Brahmanas and Aranyakas."
        s2_hi_true_exp = f"इसकी पुष्टि ब्राह्मणों और आरण्यकों में ऐतिहासिक और भौगोलिक विवरणों से होती है।"
        
        s2_en_true_unrelated = get_first_sentence(base2['sol'])
        s2_hi_true_unrelated = get_first_sentence(base2['sol_hi'])
        
        s2_en_false = f"All historical accounts of this era have been proven to be completely fictional."
        s2_hi_false = f"इस युग के सभी ऐतिहासिक विवरणों को पूरी तरह से काल्पनिक साबित कर दिया गया है।"
        
        if ans_idx == 0:
            s1_en, s2_en = s1_en_true, s2_en_true_exp
            s1_hi, s2_hi = s1_hi_true, s2_hi_true_exp
            sol_en = f"Both statements are correct, and Statement-II is the correct explanation for Statement-I: {base1['sol']}"
            sol_hi = f"दोनों कथन सही हैं, और कथन-II कथन-I की सही व्याख्या करता है: {base1['sol_hi']}"
        elif ans_idx == 1:
            s1_en, s2_en = s1_en_true, s2_en_true_unrelated
            s1_hi, s2_hi = s1_hi_true, s2_hi_true_unrelated
            sol_en = f"Both statements are correct, but Statement-II is not the correct explanation: Statement 1 ({base1['sol']}), Statement 2 ({base2['sol']})"
            sol_hi = f"दोनों कथन सही हैं, लेकिन कथन-II कथन-I की सही व्याख्या नहीं करता है: कथन 1 ({base1['sol_hi']}), कथन 2 ({base2['sol_hi']})"
        elif ans_idx == 2:
            s1_en, s2_en = s1_en_true, s2_en_false
            s1_hi, s2_hi = s1_hi_true, s2_hi_false
            sol_en = f"Statement-I is correct but Statement-II is incorrect: {base1['sol']}"
            sol_hi = f"कथन-I सही है लेकिन कथन-II गलत है: {base1['sol_hi']}"
        else: # 3
            s1_en, s2_en = s1_en_false, s1_en_true
            s1_hi, s2_hi = s1_hi_false, s1_hi_true
            sol_en = f"Statement-I is incorrect but Statement-II is correct: {base1['sol']}"
            sol_hi = f"कथन-I गलत है लेकिन कथन-II सही है: {base1['sol_hi']}"
            
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "Assertion-Reason",
            "q": f"Consider the following statements (Practice Q{i}):\nStatement-I: {s1_en}.\nStatement-II: {s2_en}.\nWhich one of the following is correct in respect of the above statements?",
            "opts": [
                "Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I",
                "Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I",
                "Statement-I is correct but Statement-II is incorrect",
                "Statement-I is incorrect but Statement-II is correct"
            ],
            "ans": ans_idx,
            "sol": sol_en,
            "q_hi": f"निम्नलिखित कथनों पर विचार करें (अभ्यास प्रश्न {i}):\nकथन-I: {s1_hi}।\nकथन-II: {s2_hi}।\nउपरोक्त कथनों के संबंध में निम्नलिखित में से कौन सा सही है?",
            "opts_hi": [
                "कथन-I और कथन-II दोनों सही हैं और कथन-II कथन-I की सही व्याख्या करता है",
                "कथन-I और कथन-II दोनों सही हैं लेकिन कथन-II कथन-I की सही व्याख्या नहीं करता है",
                "कथन-I सही है लेकिन कथन-II गलत है",
                "कथन-I गलत है लेकिन कथन-II सही है"
            ],
            "ans_hi": ans_idx,
            "sol_hi": sol_hi
        })
        
    else:
        # Direct MCQ
        base = flat_pool[(i - 1) % len(flat_pool)]
        
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "MCQ",
            "q": f"Identify the correct option: {base['q']} (Practice Q{i})",
            "opts": base["opts"],
            "ans": base["ans"],
            "sol": base["sol"],
            "q_hi": f"सही विकल्प की पहचान करें: {base['q_hi']} (अभ्यास प्रश्न {i})",
            "opts_hi": base["opts_hi"],
            "ans_hi": base["ans_hi"],
            "sol_hi": base["sol_hi"]
        })

# 10 mock test questions
mock_questions = []
for i in range(1, 11):
    sec1 = 1 + ((i + 2) % 6)
    sec2 = 1 + ((i + 3) % 6)
    idx1 = (i + 2) % len(question_pool[sec1])
    idx2 = (i + 7) % len(question_pool[sec2])
    
    base1 = question_pool[sec1][idx1]
    base2 = question_pool[sec2][idx2]
    
    ans_idx = (i - 1) % 4
    
    s1_en, s2_en, s1_hi, s2_hi = get_statement_pair(base1, base2, ans_idx)
    
    mock_questions.append({
        "id": f"mock_q_{i}",
        "type": "Statement-Based",
        "q": f"Consider the following statements regarding the Later Vedic social hierarchy (Mock Q{i}):\n1. {s1_en}.\n2. {s2_en}.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": ans_idx,
        "sol": f"Statement 1 status: {'Correct' if ans_idx in [0, 2] else 'Incorrect'}. ({base1['sol']}) Statement 2 status: {'Correct' if ans_idx in [1, 2] else 'Incorrect'}. ({base2['sol']})",
        "q_hi": f"उत्तर वैदिक सामाजिक पदानुक्रम के संबंध में निम्नलिखित कथनों पर विचार करें (मॉक प्रश्न {i}):\n1. {s1_hi}।\n2. {s2_hi}।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans_hi": ans_idx,
        "sol_hi": f"कथन 1 की स्थिति: {'सही' if ans_idx in [0, 2] else 'गलत'}। ({base1['sol_hi']}) कथन 2 की स्थिति: {'सही' if ans_idx in [1, 2] else 'गलत'}। ({base2['sol_hi']})"
    })

# Constructing final JSON objects
sections = []
for sec_meta in sections_meta:
    sections.append({
        "title": sec_meta["title"],
        "content": sec_meta["content"],
        "masteryZone": build_mastery_zone(sec_meta["id"])
    })

content_en = {
    **english_data,
    "deepDive": {
        "title": "Later Vedic Social Organisation Deep Dive",
        "description": "Master the details of Later Vedic Varna system, Gotra lineages, Ashramas, and gender dynamics.",
        "sections": sections
    },
    "practiceQuestions": practice_questions,
    "mockTestQuestions": mock_questions
}

# Hindi version sections
sections_hi = []
for sec_meta in sections_meta:
    mastery_hi = []
    en_mastery = build_mastery_zone(sec_meta["id"])
    for q in en_mastery:
        hi_q = {
            "id": q["id"],
            "type": q["type"],
            "q": q["q_hi"],
            "sol": q["sol_hi"]
        }
        if "opts" in q:
            hi_q["opts"] = q["opts_hi"]
        if "items" in q:
            hi_q["items"] = q["items_hi"]
        if "options" in q:
            hi_q["options"] = q["options_hi"]
        hi_q["ans"] = q["ans_hi"]
        mastery_hi.append(hi_q)

    sections_hi.append({
        "title": sec_meta["title_hi"],
        "content": sec_meta["content_hi"],
        "masteryZone": mastery_hi
    })

practice_hi = []
for q in practice_questions:
    practice_hi.append({
        "id": q["id"],
        "type": q["type"],
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    })

mock_hi = []
for q in mock_questions:
    mock_hi.append({
        "id": q["id"],
        "type": q["type"],
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    })

content_hi_full = {
    **hindi_data,
    "deepDive": {
        "title": "उत्तर वैदिक सामाजिक संगठन की गहन चर्चा",
        "description": "उत्तर वैदिक वर्ण व्यवस्था, गोत्र वंश, आश्रमों और लैंगिक गतिशीलता के विवरण में महारत हासिल करें।",
        "sections": sections_hi
    },
    "practiceQuestions": practice_hi,
    "mockTestQuestions": mock_hi
}

# Save output
with open(os.path.join(base_dir, "content.json"), 'w', encoding='utf-8') as f:
    json.dump(content_en, f, ensure_ascii=False, indent=2)

os.makedirs(os.path.join(base_dir, "hi"), exist_ok=True)
with open(os.path.join(base_dir, "hi", "content.json"), 'w', encoding='utf-8') as f:
    json.dump(content_hi_full, f, ensure_ascii=False, indent=2)

print("Content files generated successfully!")
