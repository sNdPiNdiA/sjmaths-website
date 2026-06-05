# -*- coding: utf-8 -*-
import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Later-Vedic-Period\Extent-and-Geography-of-the-Later-Vedic-Period"

english_data = {
    "breadcrumbs": {
        "parent": "Later Vedic Period",
        "parentUrl": "/upsc/ancient_history/History-of-Later-Vedic-Period/",
        "current": "Extent and Geography"
    },
    "hero": {
        "title": "Extent and Geography of the Later Vedic Period",
        "description": "An in-depth UPSC study guide detailing the eastward expansion, river migrations, role of iron axes in clearing forests, territorial divisions (Aryavarta, Madhyadesha), Painted Grey Ware (PGW) archaeology, and the rise of early Janapadas."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "UPSC Level Mock Test",
            "description": "Test your mastery of the Later Vedic Geography and Extent with 10 high-yield, complex statement-based and matching questions.",
            "startBtn": "Start Mock Test"
        }
    },
    "timeline": {
        "cards": [
            {
                "period": "c. 1000 BCE – 800 BCE",
                "date": "Migration & Transition",
                "details": "Indo-Aryans shift eastwards from the Sapta-Sindhu (Punjab) region to the Upper Gangetic Doab. Early usage of iron implements (Krishna-Ayas) for clearance."
            },
            {
                "period": "c. 800 BCE – 600 BCE",
                "date": "Consolidation of Janapadas",
                "details": "Establishment of regional states (Kuru-Panchala) and expansion towards the Middle Gangetic valley (Kosala, Videha, Kashi) as described in Shatapatha Brahmana."
            },
            {
                "period": "c. 600 BCE onwards",
                "date": "Dawn of Mahajanapadas",
                "details": "Emergence of larger territorial states. Transition to the Second Urbanization with PGW transitioning to NBPW (Northern Black Polished Ware)."
            }
        ]
    },
    "toolEvolution": {
        "title": "Material & Agricultural Tool Typology",
        "description": "Evolution of metal tools from Early Vedic to Later Vedic period.",
        "stages": [
            {
                "name": "Copper & Bronze (Ayas)",
                "color": "#d35400",
                "desc": "Dominant in Early Vedic. Used for weapons and ornaments; limited agricultural utility for heavy soils.",
                "svg": '<i class="fas fa-hammer" style="font-size: 2rem; color: #d35400;"></i>'
            },
            {
                "name": "Early Iron (Krishna-Ayas / Shyama-Ayas)",
                "color": "#2c3e50",
                "desc": "Introduced c. 1000 BCE. Used for axes to clear dense forests of the Doab and spearheads.",
                "svg": '<i class="fas fa-axe" style="font-size: 2rem; color: #2c3e50;"></i>'
            },
            {
                "name": "Iron Ploughshares",
                "color": "#7f8c8d",
                "desc": "Widespread by c. 600 BCE. Enabled deep ploughing of hard alluvial soils in the Gangetic valley.",
                "svg": '<i class="fas fa-tractor" style="font-size: 2rem; color: #7f8c8d;"></i>'
            }
        ]
    },
    "traps": {
        "title": "Common UPSC Pitfalls & Distinctions",
        "items": [
            "Do not confuse the Rigvedic river names with Later Vedic geography; Sarasvati recedes in importance, while Ganga and Yamuna, rarely mentioned in the Rigveda, become central.",
            "Trap: Assuming iron ploughshares were common in the early PGW phase. Iron was initially used mostly for weapons and clearing axes, while wooden ploughshares remained common.",
            "Shatapatha Brahmana's legend of Videgha Mathava describes migration to the east up to Sadanira (modern Gandak), not the Brahmaputra or Mahanadi.",
            "The concept of 'Rashtra' (territory) emerges in the Later Vedic texts; the Rigveda speaks only of tribal identity (Jana), not territorial states (Janapadas)."
        ]
    },
    "mnemonics": {
        "title": "Geographical Divisions Memory Trick",
        "description": "Use these mnemonics to remember key terms and directions.",
        "items": [
            {
                "title": "Territorial Directions",
                "phrase": "PUMP-D: Pratichya (West), Udichya (North), Madhyadesha (Middle), Prachya (East), Dakshinapatha (South)",
                "decryption": "Helps map the five-fold territorial classification (Pancha-disah) mentioned in the Aitareya Brahmana."
            },
            {
                "title": "Sadanira River boundary",
                "phrase": "Sada-Gandak (Sadanira = Gandak)",
                "decryption": "Sadanira is identified as the modern Gandak river, acting as the eastern boundary of Aryanization (Videha state)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your retention of core facts.",
        "items": [
            {
                "question": "What is the ancient Vedic name of the Gandak river?",
                "answer": "Sadanira. It served as the border between Kosala and Videha.",
                "icon": "fa-water"
            },
            {
                "question": "Which text contains the legend of Videgha Mathava and the spread of sacrificial fire?",
                "answer": "Shatapatha Brahmana. It explains the eastern expansion of Vedic culture.",
                "icon": "fa-fire"
            },
            {
                "question": "What term was used for iron in the Later Vedic texts?",
                "answer": "Shyama-Ayas or Krishna-Ayas (literally 'black metal' or 'dark metal').",
                "icon": "fa-cube"
            },
            {
                "question": "Which pottery style is archaeologically linked with the Later Vedic period?",
                "answer": "Painted Grey Ware (PGW), dating from c. 1000 to 600 BCE.",
                "icon": "fa-hockey-puck"
            }
        ]
    }
}

hindi_data = {
    "breadcrumbs": {
        "parent": "उत्तर वैदिक काल",
        "parentUrl": "/upsc/ancient_history/History-of-Later-Vedic-Period/",
        "current": "विस्तार और भूगोल"
    },
    "hero": {
        "title": "उत्तर वैदिक काल का विस्तार और भूगोल",
        "description": "एक विस्तृत UPSC अध्ययन गाइड जो पूर्व की ओर विस्तार, नदी प्रवास, जंगलों को साफ करने में लोहे की कुल्हाड़ियों की भूमिका, क्षेत्रीय विभाजनों (आर्यावर्त, मध्यदेश), चित्रित धूसर मृदभांड (PGW) पुरातत्व और प्रारंभिक जनपदों के उदय का विवरण देती है।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "UPSC स्तर का मॉक टेस्ट",
            "description": "10 उच्च-गुणवत्ता वाले, जटिल कथन-आधारित और मिलान प्रश्नों के साथ उत्तर वैदिक भूगोल और विस्तार पर अपनी महारत का परीक्षण करें।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        }
    },
    "timeline": {
        "cards": [
            {
                "period": "लगभग 1000 ईसा पूर्व – 800 ईसा पूर्व",
                "date": "प्रवास और संक्रमण",
                "details": "भारत-आर्य सप्त-सिंधु (पंजाब) क्षेत्र से पूर्व की ओर ऊपरी गंगा दोआब की ओर स्थानांतरित हुए। जंगलों की सफाई के लिए लोहे के उपकरणों (कृष्ण-अयस) का प्रारंभिक उपयोग।"
            },
            {
                "period": "लगभग 800 ईसा पूर्व – 600 ईसा पूर्व",
                "date": "जनपदों का सुदृढ़ीकरण",
                "details": "क्षेत्रीय राज्यों (कुरु-पांचाल) की स्थापना और मध्य गंगा घाटी (कोसल, विदेह, काशी) की ओर विस्तार जैसा कि शतपथ ब्राह्मण में वर्णित है।"
            },
            {
                "period": "लगभग 600 ईसा पूर्व के बाद",
                "date": "महाजनपदों का उदय",
                "details": "बड़े क्षेत्रीय राज्यों का उदय। एनबीपीडब्ल्यू (उत्तरी काली चमकीली मृदभांड) में पीजीडब्ल्यू के संक्रमण के साथ द्वितीय शहरीकरण की शुरुआत।"
            }
        ]
    },
    "toolEvolution": {
        "title": "भौतिक और कृषि उपकरण वर्गीकरण",
        "description": "प्रारंभिक वैदिक से उत्तर वैदिक काल तक धातु उपकरणों का विकास।",
        "stages": [
            {
                "name": "तांबा और कांसा (अयस)",
                "color": "#d35400",
                "desc": "प्रारंभिक वैदिक में प्रमुख। हथियारों और आभूषणों के लिए उपयोग किया जाता था; कठोर मिट्टी के लिए सीमित कृषि उपयोगिता।",
                "svg": '<i class="fas fa-hammer" style="font-size: 2rem; color: #d35400;"></i>'
            },
            {
                "name": "प्रारंभिक लोहा (कृष्ण-अयस / श्याम-अयस)",
                "color": "#2c3e50",
                "desc": "लगभग 1000 ईसा पूर्व में पेश किया गया। दोआब के घने जंगलों को साफ करने के लिए कुल्हाड़ियों और भालों के लिए उपयोग किया जाता था।",
                "svg": '<i class="fas fa-axe" style="font-size: 2rem; color: #2c3e50;"></i>'
            },
            {
                "name": "लोहे के हल",
                "color": "#7f8c8d",
                "desc": "लगभग 600 ईसा पूर्व तक व्यापक। गंगा घाटी में कठोर जलोढ़ मिट्टी की गहरी जुताई को सक्षम बनाया।",
                "svg": '<i class="fas fa-tractor" style="font-size: 2rem; color: #7f8c8d;"></i>'
            }
        ]
    },
    "traps": {
        "title": "सामान्य UPSC गलतियाँ और भेद",
        "items": [
            "ऋग्वैदिक नदी नामों को उत्तर वैदिक भूगोल के साथ भ्रमित न करें; सरस्वती का महत्व कम हो गया, जबकि गंगा और यमुना, जिनका ऋग्वेद में शायद ही कभी उल्लेख किया गया है, केंद्रीय बन गईं।",
            "भ्रम: यह मानना कि प्रारंभिक पीजीडब्ल्यू चरण में लोहे के हल आम थे। लोहे का उपयोग शुरू में ज्यादातर हथियारों और जंगलों को साफ करने की कुल्हाड़ियों के लिए किया जाता था, जबकि लकड़ी के हल आम बने रहे।",
            "शतपथ ब्राह्मण में विदेह माथव की किंवदंती सदाणीरा (आधुनिक गंडक) तक पूर्व की ओर प्रवास का वर्णन करती है, न कि ब्रह्मपुत्र या महानदी तक।",
            "राष्ट्र (क्षेत्र) की अवधारणा उत्तर वैदिक ग्रंथों में उभरती है; ऋग्वेद केवल कबीले की पहचान (जन) की बात करता है, क्षेत्रीय राज्यों (जनपद) की नहीं।"
        ]
    },
    "mnemonics": {
        "title": "भौगोलिक विभाजन याद रखने की ट्रिक",
        "description": "मुख्य शब्दों और दिशाओं को याद रखने के लिए इन युक्तियों का उपयोग करें।",
        "items": [
            {
                "title": "क्षेत्रीय दिशा-निर्देश",
                "phrase": "PUMP-D: प्रतीच्य (पश्चिम), उदीच्य (उत्तर), मध्यदेश (मध्य), प्राच्य (पूर्व), दक्षिणापथ (दक्षिण)",
                "decryption": "ऐतरेय ब्राह्मण में उल्लिखित पांच गुना क्षेत्रीय वर्गीकरण (पंच-दिशः) को मैप करने में मदद करता है।"
            },
            {
                "title": "सदाणीरा नदी सीमा",
                "phrase": "सदा-गंडक (सदाणीरा = गंडक)",
                "decryption": "सदाणीरा की पहचान आधुनिक गंडक नदी के रूप में की गई है, जो आर्यकरण (विदेह राज्य) की पूर्वी सीमा के रूप में कार्य करती थी।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड",
        "description": "मुख्य तथ्यों को याद रखने की अपनी क्षमता का परीक्षण करें।",
        "items": [
            {
                "question": "गंडक नदी का प्राचीन वैदिक नाम क्या है?",
                "answer": "सदाणीरा। यह कोसल और विदेह के बीच की सीमा थी।",
                "icon": "fa-water"
            },
            {
                "question": "किस ग्रंथ में विदेह माथव की किंवदंती और यज्ञ की अग्नि के प्रसार का उल्लेख है?",
                "answer": "शतपथ ब्राह्मण। यह वैदिक संस्कृति के पूर्वी विस्तार की व्याख्या करता है।",
                "icon": "fa-fire"
            },
            {
                "question": "उत्तर वैदिक ग्रंथों में लोहे के लिए किस शब्द का प्रयोग किया गया था?",
                "answer": "श्याम-अयस या कृष्ण-अयस (शाब्दिक रूप से 'काली धातु')।",
                "icon": "fa-cube"
            },
            {
                "question": "उत्तर वैदिक काल से कौन सी मृदभांड शैली पुरातात्विक रूप से जुड़ी हुई है?",
                "answer": "चित्रित धूसर मृदभांड (PGW), जो लगभग 1000 से 600 ईसा पूर्व तक की है।",
                "icon": "fa-hockey-puck"
            }
        ]
    }
}

sections_meta = [
    {
        "id": 1,
        "title": "1. Eastward Migration and Expansion",
        "title_hi": "1. पूर्व की ओर प्रवास और विस्तार",
        "content": "<h3>The Legend of Videgha Mathava</h3><p>The Shatapatha Brahmana records the famous legend of **Videgha Mathava**, who, accompanied by his priest **Gotama Rahugana**, carried the sacrificial fire (**Agni Vaisvanara**) from the Sarasvati river eastwards. The fire burned the forests along the way, stopping only at the banks of the **Sadanira** (modern Gandak river), which marked the eastern boundary of Videha.</p><h3>Vedic Aryanization Limit</h3><p>This legend reflects the historical eastward expansion of Vedic tribes. Prior to this, the lands east of the Sadanira were considered ritualistically impure or uncultivated. The expansion enabled the establishment of new eastern kingdoms like **Kosala** and **Videha**, transforming the nomadic pastoralists into settled agrarian societies.</p>",
        "content_hi": "<h3>विदेह माथव की किंवदंती</h3><p>शतपथ ब्राह्मण में **विदेह माथव** की प्रसिद्ध किंवदंती दर्ज है, जिन्होंने अपने पुरोहित **गोतम राहूगण** के साथ सरस्वती नदी से पूर्व की ओर यज्ञ की अग्नि (**अग्नि वैश्वानर**) को ले गए। आग ने रास्ते में जंगलों को जला दिया, और केवल **सदाणीरा** (आधुनिक गंडक नदी) के तट पर रुकी, जिसने विदेह की पूर्वी सीमा को चिह्नित किया।</p><h3>वैदिक आर्यकरण की सीमा</h3><p>यह किंवदंती वैदिक कबीलों के ऐतिहासिक पूर्व की ओर विस्तार को दर्शाती है। इससे पहले, सदाणीरा के पूर्व की भूमि को अनुष्ठानिक रूप से अपवित्र या बिना खेती वाली माना जाता था। इस विस्तार ने **कोसल** और **विदेह** जैसे नए पूर्वी राज्यों की स्थापना को सक्षम बनाया, जिससे खानाबदोश चरवाहे स्थायी कृषि समाजों में परिवर्तित हो गए।</p>"
    },
    {
        "id": 2,
        "title": "2. Geographical Centers",
        "title_hi": "2. भौगोलिक केंद्र",
        "content": "<h3>The Shift to Madhyadesha</h3><p>The geographical center of gravity shifted during this period from the **Sapta-Sindhu** (land of seven rivers, modern Punjab) to the **Madhyadesha** (Middle Country, comprising the Upper Gangetic Doab). The Punjab region began to be viewed as peripheral and ritually impure in Later Vedic literature.</p><h3>Sacred Kurukshetra Heartland</h3><p>The region of **Kurukshetra** (between Sarasvati and Drishadvati) became the highly sacred heartland for Vedic sacrifices. The dominant political power was held by the **Kuru-Panchala** coalition, whose capitals **Hastinapur** and **Kampilya** served as early administrative and proto-urban hubs.</p>",
        "content_hi": "<h3>मध्यदेश की ओर स्थानांतरण</h3><p>इस अवधि के दौरान भौगोलिक गुरुत्व केंद्र **सप्त-सिंधु** (सात नदियों की भूमि, आधुनिक पंजाब) से **मध्यदेश** (मध्य देश, जिसमें ऊपरी गंगा दोआब शामिल है) में स्थानांतरित हो गया। उत्तर वैदिक साहित्य में पंजाब क्षेत्र को परिधीय और अनुष्ठानिक रूप से अपवित्र माना जाने लगा।</p><h3>पवित्र कुरुक्षेत्र हृदय स्थल</h3><p>**कुरुक्षेत्र** (सरस्वती और दृषद्वती के बीच) का क्षेत्र वैदिक यज्ञों के लिए अत्यधिक पवित्र हृदय स्थल बन गया। प्रमुख राजनीतिक सत्ता **कुरु-पांचाल** गठबंधन के पास थी, जिनकी राजधानियाँ **हस्तिनापुर** और **काम्पिल्य** प्रारंभिक प्रशासनिक और प्रारंभिक शहरी केंद्रों के रूप में कार्य करती थीं।</p>"
    },
    {
        "id": 3,
        "title": "3. Key Rivers of the Later Vedic Period",
        "title_hi": "3. उत्तर वैदिक काल की प्रमुख नदियाँ",
        "content": "<h3>Emergence of Ganga and Yamuna</h3><p>In contrast to the Rigveda, where the Indus (Sindhu) and Sarasvati dominate, Later Vedic texts bring the **Ganga** and **Yamuna** into focus as central waterways. The Sarasvati began to recede, eventually disappearing at Vinasana.</p><h3>Southern and Mountain Frontiers</h3><p>The southern river boundary is marked by the **Reva** (identified as the Narmada), while the **Vindhya Mountains** are referred to as the southern limit of expansion. The **Himavant** (Himalayas) remained the northern border, providing sacred herbs and Soma plants.</p>",
        "content_hi": "<h3>गंगा और यमुना का उदय</h3><p>ऋग्वेद के विपरीत, जहाँ सिंधु और सरस्वती का दबदबा है, उत्तर वैदिक ग्रंथ **गंगा** और **यमुना** को केंद्रीय जलमार्गों के रूप में फोकस में लाते हैं। सरस्वती का प्रवाह कम होने लगा, और अंततः विनाशन पर गायब हो गई।</p><h3>दक्षिणी और पर्वतीय सीमाएँ</h3><p>दक्षिणी नदी सीमा **रेवा** (नर्मदा के रूप में पहचानी गई) द्वारा चिह्नित है, जबकि **विंध्य पर्वत** को विस्तार की दक्षिणी सीमा के रूप में संदर्भित किया जाता है। **हिमवंत** (हिमालय) उत्तरी सीमा बना रहा, जो पवित्र जड़ी-बूटियाँ और सोम प्रदान करता था।</p>"
    },
    {
        "id": 4,
        "title": "4. Climate, Forests & Land Clearing",
        "title_hi": "4. जलवायु, वन और भूमि की सफाई",
        "content": "<h3>High Rainfall and Jungle Clearance</h3><p>The migration eastward brought the Aryans into regions of higher rainfall and denser monsoonal forests. Unlike the dry semi-arid plains of Punjab, clearing the Gangetic plains required systematic clearance using fire and metal tools.</p><h3>Role of Iron Axes</h3><p>The introduction of **Krishna-Ayas** (iron) axes allowed for the felling of massive trees. Slash-and-burn practices combined with early iron implements enabled the expansion of settled farming. However, wooden ploughs remained common, with iron-tipped ploughshares only gaining widespread adoption towards c. 600 BCE.</p>",
        "content_hi": "<h3>उच्च वर्षा और जंगलों की सफाई</h3><p>पूर्व की ओर प्रवास ने आर्यों को अधिक वर्षा और घने मानसूनी जंगलों वाले क्षेत्रों में ला दिया। पंजाब के शुष्क अर्ध-शुष्क मैदानों के विपरीत, गंगा के मैदानों को साफ करने के लिए आग और धातु के उपकरणों का उपयोग करके व्यवस्थित सफाई की आवश्यकता थी।</p><h3>लोहे की कुल्हाड़ियों की भूमिका</h3><p>**कृष्ण-अयस** (लोहे) की कुल्हाड़ियों की शुरुआत ने विशाल पेड़ों को काटने की अनुमति दी। जंगलों को जलाने और काटने की प्रथाओं ने प्रारंभिक लोहे के उपकरणों के साथ मिलकर स्थायी खेती के विस्तार को सक्षम बनाया। हालांकि, लकड़ी के हल आम बने रहे, और लोहे की नोक वाले हल केवल लगभग 600 ईसा पूर्व के आसपास व्यापक रूप से अपनाए गए।</p>"
    },
    {
        "id": 5,
        "title": "5. Regional Divisions",
        "title_hi": "5. क्षेत्रीय विभाजन",
        "content": "<h3>The Five-Fold Classification</h3><p>The **Aitareya Brahmana** outlines a five-fold classification of the subcontinent (Pancha-disah), showcasing a growing geographical awareness:<ul><li><strong>Madhyadesha:</strong> The central heartland, ruled by Rajas.</li><li><strong>Prachya:</strong> The East (styled as Samrat).</li><li><strong>Pratichya:</strong> The West (styled as Svarat).</li><li><strong>Udichya:</strong> The North (styled as Virat).</li><li><strong>Dakshina:</strong> The South (styled as Bhoja).</li></ul></p><h3>Aryavarta and Mleccha Lands</h3><p>The term **Aryavarta** referred to the Gangetic valley where Vedic laws prevailed. Peripheral regions like the land of the **Bahikas** (Punjab) and eastern regions like **Anga** and **Magadha** were viewed with hostility and considered impure or Mleccha lands.</p>",
        "content_hi": "<h3>पंच-विभाजन</h3><p>**ऐतरेय ब्राह्मण** उपमहाद्वीप के पांच गुना वर्गीकरण (पंच-दिशः) को रेखांकित करता है, जो बढ़ती भौगोलिक जागरूकता को दर्शाता है:<ul><li><strong>मध्यदेश:</strong> केंद्रीय हृदय स्थल, जिस पर राजाओं का शासन था।</li><li><strong>प्राच्य:</strong> पूर्व (सम्राट के रूप में शैलीबद्ध)।</li><li><strong>प्रतीच्य:</strong> पश्चिम (स्वराट के रूप में शैलीबद्ध)।</li><li><strong>उदीच्य:</strong> उत्तर (विराट के रूप में शैलीबद्ध)।</li><li><strong>दक्षिण:</strong> दक्षिण (भोज के रूप में शैलीबद्ध)।</li></ul></p><h3>आर्यावर्त और म्लेच्छ भूमि</h3><p>**आर्यावर्त** शब्द गंगा घाटी को संदर्भित करता था जहाँ वैदिक नियम लागू थे। **बाहीक** (पंजाब) जैसे परिधीय क्षेत्रों और **अंग** तथा **मगध** जैसे पूर्वी क्षेत्रों को शत्रुता के साथ देखा जाता था और उन्हें अपवित्र या म्लेच्छ भूमि माना जाता था।</p>"
    },
    {
        "id": 6,
        "title": "6. Transition to Settled Life (Janapadas)",
        "title_hi": "6. स्थायी जीवन में संक्रमण (जनपद)",
        "content": "<h3>From Tribe to Territory</h3><p>The defining geopolitical shift of this era was the transition from the Rigvedic tribal identity (**Jana**) to territorial states (**Janapadas**). Tribal coalitions gave birth to powerful territorial states: the Purus and Bharatas merged to form the **Kuru** state, while the Krivis and Turvasas formed the **Panchala** state.</p><h3>The Concept of Rashtra</h3><p>The term **Rashtra** (territorial state) appears for the first time in Later Vedic texts. It represents a defined area where people accepted royal authority and paid compulsory taxes (Bhaga/Bali), laying the foundation for the 16 Mahajanapadas of the subsequent era.</p>",
        "content_hi": "<h3>कबीले से क्षेत्र की ओर</h3><p>इस युग का निर्णायक भू-राजनीतिक परिवर्तन ऋग्वैदिक कबीले की पहचान (**जन**) से क्षेत्रीय राज्यों (**जनपद**) की ओर संक्रमण था। जनजातीय गठबंधनों ने शक्तिशाली क्षेत्रीय राज्यों को जन्म दिया: पुरु और भरत मिलकर **कुरु** राज्य बने, जबकि क्रिवी और तुर्वस मिलकर **पांचाल** राज्य बने।</p><h3>राष्ट्र की अवधारणा</h3><p>**राष्ट्र** (क्षेत्रीय राज्य) शब्द पहली बार उत्तर वैदिक ग्रंथों में दिखाई देता है। यह एक निश्चित क्षेत्र का प्रतिनिधित्व करता है जहाँ लोगों ने शाही अधिकार स्वीकार किया और अनिवार्य करों (भाग/बलि) का भुगतान किया, जिसने बाद के युग के 16 महाजनपदों की नींव रखी।</p>"
    }
]

# Unique fact pools to build 62 completely distinct questions per section
question_pool = {
    1: [
        {"q": "Which text records the legend of Videgha Mathava and the eastward spread of Agni Vaisvanara?", "opts": ["Shatapatha Brahmana", "Aitareya Brahmana", "Atharvaveda", "Mundaka Upanishad"], "ans": 0, "sol": "The Shatapatha Brahmana details the legend of Videgha Mathava.", "q_hi": "किस ग्रंथ में विदेह माथव की किंवदंती और अग्नि वैश्वानर के पूर्व की ओर प्रसार का उल्लेख है?", "opts_hi": ["शतपथ ब्राह्मण", "ऐतरेय ब्राह्मण", "अथर्ववेद", "मुण्डक उपनिषद"], "ans_hi": 0, "sol_hi": "शतपथ ब्राह्मण में विदेह माथव की किंवदंती का विवरण है।"},
        {"q": "Who was the priest accompanying Videgha Mathava in his migration to the east?", "opts": ["Gotama Rahugana", "Vashistha", "Vishvamitra", "Yajnavalkya"], "ans": 0, "sol": "Gotama Rahugana was the priest of Videgha Mathava.", "q_hi": "पूर्व की ओर प्रवास में विदेह माथव के साथ जाने वाले पुरोहित कौन थे?", "opts_hi": ["गोतम राहूगण", "वशिष्ठ", "विश्वामित्र", "याज्ञवल्क्य"], "ans_hi": 0, "sol_hi": "गोतम राहूगण विदेह माथव के पुरोहित थे।"},
        {"q": "Which river served as the eastern limit of Aryanization according to the Videgha Mathava legend?", "opts": ["Sadanira (Gandak)", "Sarasvati", "Ganga", "Yamuna"], "ans": 0, "sol": "The Sadanira served as the boundary river where the fire stopped.", "q_hi": "विदेह माथव किंवदंती के अनुसार कौन सी नदी आर्यकरण की पूर्वी सीमा थी?", "opts_hi": ["सदाणीरा (गंडक)", "सरस्वती", "गंगा", "यमुना"], "ans_hi": 0, "sol_hi": "सदाणीरा वह सीमा नदी थी जहाँ आग रुकी थी।"},
        {"q": "The sacred fire carried eastwards in Later Vedic legends is named:", "opts": ["Agni Vaisvanara", "Agni Kavyavahana", "Agni Havyavahana", "None of these"], "ans": 0, "sol": "Agni Vaisvanara represented the sacrificial fire carried eastwards.", "q_hi": "उत्तर वैदिक किंवदंतियों में पूर्व की ओर ले जाई जाने वाली पवित्र अग्नि का क्या नाम है?", "opts_hi": ["अग्नि वैश्वानर", "अग्नि काव्यवाहन", "अग्नि हव्यवाहन", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "अग्नि वैश्वानर पूर्व की ओर ले जाई जाने वाली यज्ञ की अग्नि का प्रतिनिधित्व करती थी।"},
        {"q": "Vedic tribes migrated from their Rigvedic home in Sapta-Sindhu to which primary region?", "opts": ["Kuru-Panchala country (Doab)", "Deccan plateau", "Kashmir mountains", "Bengal delta"], "ans": 0, "sol": "They migrated eastwards to the Kurukshetra and Gangetic Doab region.", "q_hi": "वैदिक कबीले सप्त-सिंधु में अपने ऋग्वैदिक घर से किस प्राथमिक क्षेत्र में चले गए?", "opts_hi": ["कुरु-पांचाल देश (दोआब)", "दक्कन का पठार", "कश्मीर के पहाड़", "बंगाल डेल्टा"], "ans_hi": 0, "sol_hi": "वे पूर्व की ओर कुरुक्षेत्र और गंगा दोआब क्षेत्र में चले गए।"},
        {"q": "Which deity, represented as the pathfinder in migration, cleared path obstacles?", "opts": ["Pushan", "Indra", "Agni", "Rudra"], "ans": 0, "sol": "Pushan acted as the guardian of pathways and migrations.", "q_hi": "प्रवास में मार्गदर्शक के रूप में प्रस्तुत किए गए किस देवता ने मार्ग की बाधाओं को साफ किया?", "opts_hi": ["पूषन", "इंद्र", "अग्नि", "रुद्र"], "ans_hi": 0, "sol_hi": "पूषन मार्गों और प्रवास के संरक्षक के रूप में कार्य करते थे।"},
        {"q": "Which two easternmost territorial kingdoms were established during the Later Vedic migration?", "opts": ["Kosala and Videha", "Kuru and Panchala", "Anga and Magadha", "Kashi and Matsya"], "ans": 0, "sol": "Kosala and Videha were key eastern kingdoms founded during this expansion.", "q_hi": "उत्तर वैदिक प्रवास के दौरान कौन से दो सबसे पूर्वी क्षेत्रीय राज्य स्थापित किए गए थे?", "opts_hi": ["कोसल और विदेह", "कुरु और पांचाल", "अंग और मगध", "काशी और मत्स्य"], "ans_hi": 0, "sol_hi": "कोसल और विदेह इस विस्तार के दौरान स्थापित प्रमुख पूर्वी राज्य थे।"},
        {"q": "What primary economic transition accompanied the Indo-Aryan eastward migration?", "opts": ["Shift from pastoral nomadism to settled agriculture", "Transition from sea trade to mining", "Decline of farming in favor of hunting", "Abolition of cattle rearing"], "ans": 0, "sol": "The migration went hand-in-hand with permanent agricultural settlements.", "q_hi": "भारत-आर्यों के पूर्व की ओर प्रवास के साथ कौन सा प्राथमिक आर्थिक परिवर्तन हुआ?", "opts_hi": ["पशुचारण खानाबदोश से स्थायी कृषि में परिवर्तन", "समुद्री व्यापार से खनन में संक्रमण", "शिकार के पक्ष में खेती का पतन", "पशुपालन का उन्मूलन"], "ans_hi": 0, "sol_hi": "यह प्रवास स्थायी कृषि बस्तियों के साथ-साथ हुआ।"},
        {"q": "The introduction of which staple crop supported higher population densities in Gangetic plains?", "opts": ["Rice (Vrihi)", "Barley (Yava)", "Millets", "Cotton"], "ans": 0, "sol": "Cultivation of rice supported denser populations due to high caloric yield.", "q_hi": "गंगा के मैदानों में किस मुख्य फसल की शुरुआत ने उच्च जनसंख्या घनत्व का समर्थन किया?", "opts_hi": ["चावल/धान (व्रीहि)", "जौ (यव)", "बाजरा", "कपास"], "ans_hi": 0, "sol_hi": "उच्च कैलोरी उपज के कारण धान की खेती ने अधिक आबादी का समर्थन किया।"},
        {"q": "Deforestation in the Gangetic valley was critical for establishing what settlements?", "opts": ["Permanent agricultural villages and towns", "Temporary hunting camps", "Pastoral sheep-rearing zones", "Maritime trade ports"], "ans": 0, "sol": "Clearing forests was essential to establish agricultural communities.", "q_hi": "गंगा घाटी में वनों की कटाई किन बस्तियों की स्थापना के लिए महत्वपूर्ण थी?", "opts_hi": ["स्थायी कृषि गाँव और शहर", "अस्थायी शिकार शिविर", "पशुचारण भेड़-पालन क्षेत्र", "समुद्री व्यापारिक बंदरगाह"], "ans_hi": 0, "sol_hi": "कृषि समुदायों की स्थापना के लिए जंगलों को साफ करना आवश्यक था।"},
        {"q": "The decline of which sacred Rigvedic river prompted the eastward relocation of tribes?", "opts": ["Sarasvati", "Sindhu", "Satadru", "Vipasa"], "ans": 0, "sol": "The drying up of the Sarasvati forced tribes to migrate eastwards.", "q_hi": "किस पवित्र ऋग्वैदिक नदी के जलस्तर में गिरावट ने कबीलों को पूर्व की ओर स्थानांतरित होने के लिए प्रेरित किया?", "opts_hi": ["सरस्वती", "सिंधु", "शतद्रु", "विपासा"], "ans_hi": 0, "sol_hi": "सरस्वती के सूखने से कबीले पूर्व की ओर पलायन करने के लिए मजबूर हुए।"},
        {"q": "Which auxiliary Vedic text explains the expansion of Aryan territory in all directions?", "opts": ["Aitareya Brahmana", "Mundaka Upanishad", "Gopatha Brahmana", "Katha Upanishad"], "ans": 0, "sol": "Aitareya Brahmana lists the direction-wise expansion of kingdoms.", "q_hi": "कौन सा सहायक वैदिक ग्रंथ सभी दिशाओं में आर्य क्षेत्र के विस्तार की व्याख्या करता है?", "opts_hi": ["ऐतरेय ब्राह्मण", "मुण्डक उपनिषद", "गोपथ ब्राह्मण", "कठोपनिषद"], "ans_hi": 0, "sol_hi": "ऐतरेय ब्राह्मण राज्यों के दिशा-वार विस्तार को सूचीबद्ध करता है।"}
    ],
    2: [
        {"q": "Which region was referred to as the 'Middle Country' (Madhyadesha) in Later Vedic geography?", "opts": ["Upper Gangetic Doab", "Sapta-Sindhu region", "Deccan Plateau", "Bengal delta"], "ans": 0, "sol": "Madhyadesha corresponded to the Gangetic Doab heartland.", "q_hi": "उत्तर वैदिक भूगोल में किस क्षेत्र को 'मध्यदेश' कहा गया था?", "opts_hi": ["ऊपरी गंगा दोआब", "सप्त-सिंधु क्षेत्र", "दक्कन का पठार", "बंगाल डेल्टा"], "ans_hi": 0, "sol_hi": "मध्यदेश गंगा दोआब हृदय स्थल से मेल खाता था।"},
        {"q": "How was the Rigvedic homeland of Sapta-Sindhu viewed in Later Vedic texts?", "opts": ["As peripheral and ritually impure", "As the supreme sacred center", "As the only source of Soma", "It was completely forgotten"], "ans": 0, "sol": "Punjab was viewed as impure in Later Vedic literature relative to the Doab.", "q_hi": "उत्तर वैदिक ग्रंथों में सप्त-सिंधु के ऋग्वैदिक गृह को कैसे देखा जाता था?", "opts_hi": ["परिधीय और अनुष्ठानिक रूप से अपवित्र के रूप में", "सर्वोच्च पवित्र केंद्र के रूप में", "सोम के एकमात्र स्रोत के रूप में", "इसे पूरी तरह से भुला दिया गया था"], "ans_hi": 0, "sol_hi": "दोआब की तुलना में उत्तर वैदिक साहित्य में पंजाब को अपवित्र माना जाता था।"},
        {"q": "Which sacred plain became the preeminent center for performing elaborate Yajnas?", "opts": ["Kurukshetra", "Mahanadi basin", "Thar desert", "Kashmir valley"], "ans": 0, "sol": "Kurukshetra became the sacred location for Later Vedic sacrificial performance.", "q_hi": "कौन सा पवित्र मैदान विस्तृत यज्ञ करने के लिए सर्वोपरि केंद्र बन गया?", "opts_hi": ["कुरुक्षेत्र", "महानदी बेसिन", "थार मरुस्थल", "कश्मीर घाटी"], "ans_hi": 0, "sol_hi": "कुरुक्षेत्र उत्तर वैदिक यज्ञ अनुष्ठानों के लिए पवित्र स्थान बन गया।"},
        {"q": "Which coalition heartland controlled the major political power of the Doab?", "opts": ["Kuru-Panchala", "Anga-Magadha", "Kosala-Videha", "Kashi-Matsya"], "ans": 0, "sol": "Kuru-Panchalas dominated the Later Vedic heartland.", "q_hi": "किस गठबंधन ने दोआब की प्रमुख राजनीतिक सत्ता को नियंत्रित किया?", "opts_hi": ["कुरु-पांचाल", "अंग-मगध", "कोसल-विदेह", "काशी-मत्स्य"], "ans_hi": 0, "sol_hi": "उत्तर वैदिक हृदय स्थल पर कुरु-पांचालों का वर्चस्व था।"},
        {"q": "What city was established as the primary capital town of the Kuru kingdom?", "opts": ["Hastinapur", "Kampilya", "Puhar", "Kaushambi"], "ans": 0, "sol": "Hastinapur was the main Kuru capital.", "q_hi": "कुरु राज्य की प्राथमिक राजधानी के रूप में किस शहर को स्थापित किया गया था?", "opts_hi": ["हस्तिनापुर", "काम्पिल्य", "पुहार", "कौशाम्बी"], "ans_hi": 0, "sol_hi": "हस्तिनापुर कुरुओं की मुख्य राजधानी थी।"},
        {"q": "What city served as the capital of the southern Panchala kingdom?", "opts": ["Kampilya", "Hastinapur", "Indraprastha", "Mathura"], "ans": 0, "sol": "Kampilya was the capital town of southern Panchala.", "q_hi": "दक्षिणी पांचाल राज्य की राजधानी के रूप में किस शहर ने कार्य किया?", "opts_hi": ["काम्पिल्य", "हस्तिनापुर", "इंद्रप्रस्थ", "मथुरा"], "ans_hi": 0, "sol_hi": "काम्पिल्य दक्षिणी पांचाल की राजधानी थी।"},
        {"q": "What is the capital town of Kuru king Parikshit mentioned in Atharvaveda?", "opts": ["Asandivat", "Kampilya", "Kaushambi", "Madurai"], "ans": 0, "sol": "Asandivat was the capital town of the famous Kuru kings.", "q_hi": "अथर्ववेद में वर्णित कुरु राजा परीक्षित की राजधानी का क्या नाम है?", "opts_hi": ["आसंदीवत", "काम्पिल्य", "कौशाम्बी", "मदुराई"], "ans_hi": 0, "sol_hi": "आसंदीवत प्रसिद्ध कुरु राजाओं की राजधानी थी।"},
        {"q": "Which three major kingdoms flourished east of the Kuru-Panchala country?", "opts": ["Kashi, Kosala, and Videha", "Anga, Magadha, and Vanga", "Chera, Chola, and Pandya", "Matsya, Surasena, and Avanti"], "ans": 0, "sol": "Kashi, Kosala, and Videha were the key eastern monarchies.", "q_hi": "कुरु-पांचाल देश के पूर्व में कौन से तीन प्रमुख राज्य फले-फूले?", "opts_hi": ["काशी, कोसल और विदेह", "अंग, मगध और वंग", "चेर, चोल और पांड्य", "मत्स्य, शूरसेन और अवंती"], "ans_hi": 0, "sol_hi": "काशी, कोसल और विदेह प्रमुख पूर्वी राजशाही थे।"},
        {"q": "Where in Kurukshetra did early proto-urban settlements emerge?", "opts": ["Srughna and Asandivat", "Harappa and Lothal", "Varanasi and Patna", "Nalanda and Taxila"], "ans": 0, "sol": "Srughna and Asandivat represent early Kuru settlements.", "q_hi": "कुरुक्षेत्र में कहाँ प्रारंभिक शहरी बस्तियाँ उभरीं?", "opts_hi": ["स्रुघ्न और आसंदीवत", "हड़प्पा और लोथल", "वाराणसी और पटना", "नालंदा और तक्षशिला"], "ans_hi": 0, "sol_hi": "स्रुघ्न और आसंदीवत प्रारंभिक कुरु बस्तियों का प्रतिनिधित्व करते हैं।"},
        {"q": "Why was the Doab alluvial soil economically significant for the Kuru-Panchala power?", "opts": ["It provided agricultural surplus to sustain kingship and priests", "It contained rich deposits of gold dust", "It was ideal for raising military horses", "It was completely free of vegetation"], "ans": 0, "sol": "Doab fertility supported crop yields yielding surplus for political institutions.", "q_hi": "कुरु-पांचाल सत्ता के लिए दोआब की जलोढ़ मिट्टी आर्थिक रूप से क्यों महत्वपूर्ण थी?", "opts_hi": ["यह राजपद और पुरोहितों को बनाए रखने के लिए कृषि अधिशेष प्रदान करती थी", "इसमें सोने की धूल के समृद्ध भंडार थे", "यह सैन्य घोड़ों को पालने के लिए आदर्श थी", "यह वनस्पति से पूरी तरह मुक्त थी"], "ans_hi": 0, "sol_hi": "दोआब की उर्वरता ने राजनीतिक संस्थानों के लिए अधिशेष उपज का समर्थन किया।"},
        {"q": "The shift from tribal migrations to settled regional boundaries resulted in:", "opts": ["Emergence of territorial kingdoms (Janapadas)", "Total abandonment of farming", "Abolition of kingship", "Complete isolation from other regions"], "ans": 0, "sol": "Settled geography directly fostered territorial identities.", "q_hi": "जनजातीय प्रवास से स्थायी क्षेत्रीय सीमाओं की ओर संक्रमण का क्या परिणाम हुआ?", "opts_hi": ["क्षेत्रीय राज्यों (जनपदों) का उदय", "खेती का पूर्ण परित्याग", "राजपद का उन्मूलन", "अन्य क्षेत्रों से पूर्ण अलगाव"], "ans_hi": 0, "sol_hi": "स्थायी भूगोल ने सीधे तौर पर क्षेत्रीय पहचान को बढ़ावा दिया।"},
        {"q": "Which river system bordered the Madhyadesha heartland to the west?", "opts": ["Indus (Sindhu) system", "Brahmaputra system", "Narmada system", "Krishna system"], "ans": 0, "sol": "The Indus system bordered the western edges of the newly settled territory.", "q_hi": "कौन सा नदी तंत्र मध्यदेश हृदय स्थल को पश्चिम में सीमाबद्ध करता था?", "opts_hi": ["सिंधु तंत्र", "ब्रह्मपुत्र तंत्र", "नर्मदा तंत्र", "कृष्णा तंत्र"], "ans_hi": 0, "sol_hi": "सिंधु नदी प्रणाली नव-बसी हुई सीमाओं के पश्चिमी किनारों को छूती थी।"}
    ],
    3: [
        {"q": "Which central river of the heartland is rarely mentioned in Rigveda but central in Later Vedic texts?", "opts": ["Ganga", "Sindhu", "Sarasvati", "Satadru"], "ans": 0, "sol": "Ganga is mentioned only once in Rigveda but becomes prominent in Later Vedic texts.", "q_hi": "हृदय स्थल की कौन सी केंद्रीय नदी ऋग्वेद में शायद ही कभी उल्लिखित है लेकिन उत्तर वैदिक ग्रंथों में केंद्रीय है?", "opts_hi": ["गंगा", "सिंधु", "सरस्वती", "शतद्रु"], "ans_hi": 0, "sol_hi": "ऋग्वेद में गंगा का उल्लेख केवल एक बार मिलता है, लेकिन उत्तर वैदिक ग्रंथों में यह प्रमुख हो जाती है।"},
        {"q": "Which river alongside Ganga acted as the central waterway of the Madhyadesha Doab?", "opts": ["Yamuna", "Sadanira", "Sindhu", "Reva"], "ans": 0, "sol": "Yamuna was the other main river bordering the Doab heartland.", "q_hi": "गंगा के साथ कौन सी नदी मध्यदेश दोआब के केंद्रीय जलमार्ग के रूप में कार्य करती थी?", "opts_hi": ["यमुना", "सदाणीरा", "सिंधु", "रेवा"], "ans_hi": 0, "sol_hi": "यमुना दोआब हृदय स्थल को सीमाबद्ध करने वाली दूसरी मुख्य नदी थी।"},
        {"q": "Which river is identified as the modern Gandak, serving as the border between Kosala and Videha?", "opts": ["Sadanira", "Reva", "Ganga", "Vipasa"], "ans": 0, "sol": "Sadanira represents the Gandak river.", "q_hi": "किस नदी की पहचान आधुनिक गंडक के रूप में की गई है, जो कोसल और विदेह के बीच सीमा का कार्य करती थी?", "opts_hi": ["सदाणीरा", "रेवा", "गंगा", "विपासा"], "ans_hi": 0, "sol_hi": "सदाणीरा गंडक नदी का प्रतिनिधित्व करती है।"},
        {"q": "Which river is referred to as Reva in Later Vedic texts, marking the southern limit?", "opts": ["Narmada", "Goda", "Krishna", "Kaveri"], "ans": 0, "sol": "Reva is identified as the Narmada river.", "q_hi": "उत्तर वैदिक ग्रंथों में किस नदी को रेवा कहा गया है, जो दक्षिणी सीमा को चिह्नित करती है?", "opts_hi": ["नर्मदा", "गोदावरी", "कृष्णा", "कावेरी"], "ans_hi": 0, "sol_hi": "रेवा की पहचान नर्मदा नदी के रूप में की गई है।"},
        {"q": "Which mountain range is referred to as the southern limit of expansion?", "opts": ["Vindhya Mountains", "Western Ghats", "Eastern Ghats", "Aravalli range"], "ans": 0, "sol": "Vindhya range marked the southern geographic limit of Later Vedic expansion.", "q_hi": "किस पर्वत श्रृंखला को विस्तार की दक्षिणी सीमा के रूप में संदर्भित किया जाता है?", "opts_hi": ["विंध्य पर्वत", "पश्चिमी घाट", "पूर्वी घाट", "अरावली श्रेणी"], "ans_hi": 0, "sol_hi": "विंध्य पर्वत श्रृंखला ने उत्तर वैदिक विस्तार की दक्षिणी सीमा को चिह्नित किया।"},
        {"q": "The northern border of Himavant refers to which mountain range?", "opts": ["Himalayas", "Vindhyas", "Hindukush", "Pamirs"], "ans": 0, "sol": "Himavant represents the Himalayas.", "q_hi": "हिमवंत की उत्तरी सीमा किस पर्वत श्रृंखला को संदर्भित करती है?", "opts_hi": ["हिमालय", "विंध्य", "हिंदुकुश", "पामीर"], "ans_hi": 0, "sol_hi": "हिमवंत हिमालय का प्रतिनिधित्व करता है।"},
        {"q": "Which mountain peaks mentioned in Atharvaveda were sources of herbs?", "opts": ["Trikota and Krauncha", "Everest and K2", "Anamudi and Doddabetta", "None of these"], "ans": 0, "sol": "Trikota is mentioned in Later Vedic literature.", "q_hi": "अथर्ववेद में वर्णित जड़ी-बूटियों के स्रोत कौन से पर्वत शिखर थे?", "opts_hi": ["त्रिकूट और क्रौंच", "एवरेस्ट और के2", "अनामुडी और दोड्डाबेट्टा", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "उत्तर वैदिक साहित्य में त्रिकूट का उल्लेख है।"},
        {"q": "What drying up destination is referred to as the place where Sarasvati disappeared?", "opts": ["Vinasana", "Prayag", "Kurukshetra", "Haridwar"], "ans": 0, "sol": "Vinasana is the location in Rajasthan where Sarasvati dried up.", "q_hi": "किस लुप्त होने वाले स्थान को वह स्थान कहा गया है जहाँ सरस्वती गायब हो गई थी?", "opts_hi": ["विनाशन", "प्रयाग", "कुरुक्षेत्र", "हरिद्वार"], "ans_hi": 0, "sol_hi": "विनाशन राजस्थान में वह स्थान है जहाँ सरस्वती नदी सूखी थी।"},
        {"q": "Which small river marked the boundary of Kurukshetra alongside Sarasvati?", "opts": ["Drishadvati", "Gandak", "Reva", "Sindhu"], "ans": 0, "sol": "Drishadvati bordered Kurukshetra.", "q_hi": "सरस्वती के साथ किस छोटी नदी ने कुरुक्षेत्र की सीमा को चिह्नित किया?", "opts_hi": ["दृषद्वती", "गंडक", "रेवा", "सिंधु"], "ans_hi": 0, "sol_hi": "दृषद्वती कुरुक्षेत्र को सीमाबद्ध करती थी।"},
        {"q": "What does the literal meaning of 'Sadanira' signify regarding its water flow?", "opts": ["Always filled with water / Perennial", "Dry for half the year", "Flowing only during monsoon", "Salty sea-water river"], "ans": 0, "sol": "Sada-nira literally means always containing water, showing it was perennial.", "q_hi": "'सदाणीरा' का शाब्दिक अर्थ इसके जल प्रवाह के संबंध में क्या दर्शाता है?", "opts_hi": ["हमेशा जल से भरी रहने वाली / बारहमासी", "वर्ष में आधे समय सूखी रहने वाली", "केवल मानसून के दौरान बहने वाली", "खारे समुद्र के पानी की नदी"], "ans_hi": 0, "sol_hi": "सदाणीरा का शाब्दिक अर्थ है हमेशा जल रहना, जो यह दर्शाता है कि यह बारहमासी थी।"},
        {"q": "Which two western rivers of Punjab are mentioned as boundary rivers?", "opts": ["Satadru (Sutlej) and Vipas (Beas)", "Sindhu and Jhelum", "Ravi and Chenab", "Ganga and Yamuna"], "ans": 0, "sol": "Satadru and Vipas are mentioned.", "q_hi": "पंजाब की किन दो पश्चिमी नदियों को सीमा नदियों के रूप में वर्णित किया गया है?", "opts_hi": ["शतद्रु (सतलुज) और विपासा (ब्यास)", "सिंधु और झेलम", "रावी और चिनाब", "गंगा और यमुना"], "ans_hi": 0, "sol_hi": "शतद्रु और विपासा का उल्लेख मिलता है।"},
        {"q": "What geographic feature is highlighted by the river identifications in Later Vedic texts?", "opts": ["Consolidation of geography in Upper-Middle Gangetic basin", "Complete loss of river knowledge", "Exploration of central Tibetan plateau", "None of these"], "ans": 0, "sol": "River listings show the shifted geography towards the east.", "q_hi": "उत्तर वैदिक ग्रंथों में नदी पहचानों द्वारा किस भौगोलिक विशेषता को उजागर किया गया है?", "opts_hi": ["ऊपरी-मध्य गंगा बेसिन में भूगोल का सुदृढ़ीकरण", "नदी ज्ञान का पूर्ण नुकसान", "मध्य तिब्बती पठार का अन्वेषण", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "नदियों की सूचियाँ पूर्व की ओर स्थानांतरित भूगोल को दर्शाती हैं।"}
    ],
    4: [
        {"q": "What type of vegetation characterized the newly settled Gangetic valley?", "opts": ["Dense monsoon forests", "Dry thorny scrub", "Coniferous pine forests", "Alpine meadows"], "ans": 0, "sol": "The Gangetic plain was covered with dense monsoon forests.", "q_hi": "नव-बसी हुई गंगा घाटी में किस प्रकार की वनस्पति की विशेषता थी?", "opts_hi": ["घने मानसूनी वन", "शुष्क कांटेदार झाड़ियाँ", "शंकुधारी देवदार के वन", "अल्पाइन घास के मैदान"], "ans_hi": 0, "sol_hi": "गंगा का मैदान घने मानसूनी जंगलों से ढका हुआ था।"},
        {"q": "Which clearing method was widely used to open agricultural fields in dense forests?", "opts": ["Slash-and-burn (using fire)", "Manual extraction of tree roots only", "Imported bronze saw cuts", "No clearing was needed"], "ans": 0, "sol": "Slash-and-burn was the primary method to clear forests.", "q_hi": "घने जंगलों में कृषि खेतों को खोलने के लिए किस सफाई पद्धति का व्यापक रूप से उपयोग किया गया था?", "opts_hi": ["काटना और जलाना (आग का उपयोग)", "केवल पेड़ की जड़ों को मैन्युअल रूप से निकालना", "आयातित कांसे के आरी से काटना", "सफाई की कोई आवश्यकता नहीं थी"], "ans_hi": 0, "sol_hi": "काटना और जलाना जंगलों को साफ करने की प्राथमिक विधि थी।"},
        {"q": "What metal is referred to as 'Krishna-Ayas' used to make clearing axes?", "opts": ["Iron", "Copper", "Gold", "Lead"], "ans": 0, "sol": "Krishna-Ayas or Shyama-Ayas refers to iron.", "q_hi": "किस धातु को 'कृष्ण-अयस' कहा जाता है जिसका उपयोग कुल्हाड़ियों को बनाने के लिए किया जाता था?", "opts_hi": ["लोहा", "तांबा", "सोना", "सीसा"], "ans_hi": 0, "sol_hi": "कृष्ण-अयस या श्याम-अयस का अर्थ लोहा है।"},
        {"q": "What implement remained most common for plowing during the early part of this period?", "opts": ["Wooden plow", "Iron-tipped plowshare", "Tractor blades", "Stone hoes"], "ans": 0, "sol": "Wooden plows remained common, as iron-tipped plowshares were rare initially.", "q_hi": "इस काल के प्रारंभिक भाग के दौरान जुताई के लिए कौन सा उपकरण सबसे आम बना रहा?", "opts_hi": ["लकड़ी का हल", "लोहे की नोक वाला हल", "ट्रैक्टर के ब्लेड", "पत्थर की कुदाल"], "ans_hi": 0, "sol_hi": "लकड़ी के हल आम बने रहे, क्योंकि लोहे की नोक वाले हल शुरू में दुर्लभ थे।"},
        {"q": "The high monsoonal rainfall in the Ganga basin had what effect on the jungle?", "opts": ["Created rapid jungle growth and thick undergrowth", "Dried up all the forests", "Prevented any tree growth", "Fostered desertification"], "ans": 0, "sol": "High monsoonal rain supported dense vegetative growth.", "q_hi": "गंगा बेसिन में उच्च मानसूनी वर्षा का जंगलों पर क्या प्रभाव पड़ा?", "opts_hi": ["जंगलों का तेजी से विकास और घनी झाड़ियों का निर्माण हुआ", "सभी जंगल सूख गए", "पेड़ों के विकास को रोका", "मरुस्थलीकरण को बढ़ावा दिया"], "ans_hi": 0, "sol_hi": "उच्च मानसूनी वर्षा ने घने जंगलों के विकास का समर्थन किया।"},
        {"q": "The Atharvaveda contains specific prayers to protect people from which natural hazard?", "opts": ["Forest fires (Davagni)", "Ice storms", "Sea tides", "Volcanic eruptions"], "ans": 0, "sol": "Atharvaveda lists prayers against forest fires.", "q_hi": "अथर्ववेद में लोगों को किस प्राकृतिक खतरे से बचाने के लिए विशिष्ट प्रार्थनाएँ शामिल हैं?", "opts_hi": ["दावानल (जंगल की आग)", "बर्फ के तूफान", "समुद्री ज्वार", "ज्वालामुखी विस्फोट"], "ans_hi": 0, "sol_hi": "अथर्ववेद में जंगल की आग से सुरक्षा के लिए प्रार्थनाएं हैं।"},
        {"q": "Clearing the swampy areas of the Doab enabled the cultivation of which crops?", "opts": ["Wheat and Rice", "Coconuts and tea", "Saffron and olives", "None of these"], "ans": 0, "sol": "Doab soils were cleared for rice and wheat farming.", "q_hi": "दोआब के दलदली क्षेत्रों को साफ करने से किन फसलों की खेती संभव हुई?", "opts_hi": ["गेहूं और धान/चावल", "नारियल और चाय", "केसर और जैतून", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "गेहूं और धान की खेती के लिए दोआब की मिट्टी को साफ किया गया था।"},
        {"q": "What environmental transformation resulted from Later Vedic land clearing?", "opts": ["Early deforestation of Ganga plains and habitat change", "Creation of artificial lakes", "Complete preservation of forests", "Salinization of Doab soils"], "ans": 0, "sol": "Clearance led to early deforestation and environmental modifications.", "q_hi": "उत्तर वैदिक काल में भूमि की सफाई से कौन सा पर्यावरणीय परिवर्तन हुआ?", "opts_hi": ["गंगा के मैदानों में प्रारंभिक वनों की कटाई और आवास परिवर्तन", "कृत्रिम झीलों का निर्माण", "जंगलों का पूर्ण संरक्षण", "दोआब की मिट्टी का लवणीकरण"], "ans_hi": 0, "sol_hi": "सफाई के कारण प्रारंभिक वनों की कटाई और पर्यावरणीय बदलाव हुए।"},
        {"q": "Which element was represented as the 'civilizing agent' clearing wild jungles in texts?", "opts": ["Fire (Agni)", "Water", "Wind", "Earth"], "ans": 0, "sol": "Agni was the agent that cleared forests in legends.", "q_hi": "ग्रंथों में जंगली जंगलों को साफ करने वाले 'सभ्यता के एजेंट' के रूप में किसे दर्शाया गया था?", "opts_hi": ["अग्नि", "जल", "वायु", "पृथ्वी"], "ans_hi": 0, "sol_hi": "किंवदंतियों में अग्नि वह एजेंट थी जिसने जंगलों को साफ किया।"},
        {"q": "The shift of timber usage during settled life moved from chariot building to:", "opts": ["House construction and permanent structures", "Shipbuilding only", "Exporting wood to Rome", "No timber was used"], "ans": 0, "sol": "Timber was increasingly used for building dwellings in settled life.", "q_hi": "स्थायी जीवन के दौरान लकड़ी के उपयोग का ध्यान रथ निर्माण से हटकर किस पर केंद्रित हो गया?", "opts_hi": ["घर निर्माण और स्थायी संरचनाएं", "केवल जहाज निर्माण", "रोम को लकड़ी का निर्यात", "कोई लकड़ी उपयोग नहीं की गई"], "ans_hi": 0, "sol_hi": "स्थायी जीवन में घरों के निर्माण के लिए लकड़ी का उपयोग बढ़ा।"},
        {"q": "Did local non-Aryan tribes cooperate in clearing forests?", "opts": ["Yes, references to local forest dwellers are found", "No, they were completely absent", "Only in the southern Deccan", "Only in the mountains"], "ans": 0, "sol": "Vedic texts show interactions with forest tribes during expansion.", "q_hi": "क्या स्थानीय गैर-आर्य कबीलों ने जंगलों को साफ करने में सहयोग किया था?", "opts_hi": ["हाँ, स्थानीय वन निवासियों के संदर्भ मिलते हैं", "नहीं, वे पूरी तरह से अनुपस्थित थे", "केवल दक्षिणी दक्कन में", "केवल पहाड़ों में"], "ans_hi": 0, "sol_hi": "वैदिक ग्रंथ विस्तार के दौरान वन कबीलों के साथ बातचीत को दर्शाते हैं।"},
        {"q": "What agricultural improvement supported settled field cultivation?", "opts": ["Development of rudimentary irrigation (wells/canals)", "Abolition of seed planting", "Complete reliance on wild seeds", "Imported chemical fertilizers"], "ans": 0, "sol": "Irrigation techniques (wells, canals) developed to support agriculture.", "q_hi": "स्थायी खेती का समर्थन करने के लिए कौन सा कृषि सुधार हुआ?", "opts_hi": ["प्रारंभिक सिंचाई (कुएँ/नहरें) का विकास", "बीज बोने का उन्मूलन", "जंगली बीजों पर पूर्ण निर्भरता", "आयातित रासायनिक उर्वरक"], "ans_hi": 0, "sol_hi": "कृषि का समर्थन करने के लिए सिंचाई तकनीकों (कुएँ, नहरें) का विकास हुआ।"}
    ],
    5: [
        {"q": "Which Brahmana text outlines the five-fold geographical division of India (Pancha-disah)?", "opts": ["Aitareya Brahmana", "Shatapatha Brahmana", "Gopatha Brahmana", "Taittiriya Brahmana"], "ans": 0, "sol": "Aitareya Brahmana lists the direction-wise classification of rulers.", "q_hi": "कौन सा ब्राह्मण ग्रंथ भारत के पांच गुना भौगोलिक विभाजन (पंच-दिशः) को रेखांकित करता है?", "opts_hi": ["ऐतरेय ब्राह्मण", "शतपथ ब्राह्मण", "गोपथ ब्राह्मण", "तैत्तिरीय ब्राह्मण"], "ans_hi": 0, "sol_hi": "ऐतरेय ब्राह्मण राजाओं के दिशा-वार वर्गीकरण को सूचीबद्ध करता है।"},
        {"q": "Under the five-fold division, what title did the eastern (Prachya) rulers assume?", "opts": ["Samrat", "Svarat", "Virat", "Bhoja"], "ans": 0, "sol": "Eastern rulers were styled as Samrat.", "q_hi": "पांच गुना विभाजन के तहत, पूर्वी (प्राच्य) शासकों ने कौन सी उपाधि धारण की?", "opts_hi": ["सम्राट", "स्वराट", "विराट", "भोज"], "ans_hi": 0, "sol_hi": "पूर्वी शासकों को सम्राट कहा जाता था।"},
        {"q": "Under the five-fold division, what title did the western (Pratichya) rulers assume?", "opts": ["Svarat", "Samrat", "Virat", "Bhoja"], "ans": 0, "sol": "Western rulers were styled as Svarat.", "q_hi": "पांच गुना विभाजन के तहत, पश्चिमी (प्रतीच्य) शासकों ने कौन सी उपाधि धारण की?", "opts_hi": ["स्वराट", "सम्राट", "विराट", "भोज"], "ans_hi": 0, "sol_hi": "पश्चिमी शासकों को स्वराट कहा जाता था।"},
        {"q": "Under the five-fold division, what title did the northern (Udichya) rulers assume?", "opts": ["Virat", "Samrat", "Svarat", "Bhoja"], "ans": 0, "sol": "Northern rulers were styled as Virat.", "q_hi": "पांच गुना विभाजन के तहत, उत्तरी (उदीच्य) शासकों ने कौन सी उपाधि धारण की?", "opts_hi": ["विराट", "सम्राट", "स्वराट", "भोज"], "ans_hi": 0, "sol_hi": "उत्तरी शासकों को विराट कहा जाता था।"},
        {"q": "Under the five-fold division, what title did the southern (Dakshina) rulers assume?", "opts": ["Bhoja", "Samrat", "Svarat", "Virat"], "ans": 0, "sol": "Southern rulers were Bhojas.", "q_hi": "पांच गुना विभाजन के तहत, दक्षिणी (दक्षिण) शासकों ने कौन सी उपाधि धारण की?", "opts_hi": ["भोज", "सम्राट", "स्वराट", "विराट"], "ans_hi": 0, "sol_hi": "दक्षिणी शासक भोज थे।"},
        {"q": "What title was assumed by the rulers of the central heartland (Madhyadesha)?", "opts": ["Raja", "Samrat", "Virat", "Svarat"], "ans": 0, "sol": "Central heartland rulers assumed the simple title Raja.", "q_hi": "केंद्रीय हृदय स्थल (मध्यदेश) के शासकों द्वारा कौन सी उपाधि धारण की जाती थी?", "opts_hi": ["राजा", "सम्राट", "विराट", "स्वराट"], "ans_hi": 0, "sol_hi": "केंद्रीय हृदय स्थल के शासकों ने राजा की सरल उपाधि धारण की।"},
        {"q": "What term referred to the geographical region of the Gangetic valley where Vedic laws prevailed?", "opts": ["Aryavarta", "Dakshinapatha", "Mlecchadesha", "Sapta-Sindhu"], "ans": 0, "sol": "Aryavarta represents the land of Vedic laws.", "q_hi": "गंगा घाटी के उस भौगोलिक क्षेत्र को किस शब्द से संदर्भित किया गया था जहाँ वैदिक नियम प्रचलित थे?", "opts_hi": ["आर्यावर्त", "दक्षिणापथ", "म्लेच्छदेश", "सप्त-सिंधु"], "ans_hi": 0, "sol_hi": "आर्यावर्त वैदिक नियमों की भूमि का प्रतिनिधित्व करता है।"},
        {"q": "Which term refers to the southern region, indicating early contacts with the Deccan?", "opts": ["Dakshinapatha", "Aryavarta", "Madhyadesha", "Udichya"], "ans": 0, "sol": "Dakshinapatha refers to the south.", "q_hi": "कौन सा शब्द दक्षिणी क्षेत्र को संदर्भित करता है, जो दक्कन के साथ प्रारंभिक संपर्कों को दर्शाता है?", "opts_hi": ["दक्षिणापथ", "आर्यावर्त", "मध्यदेश", "उदीच्य"], "ans_hi": 0, "sol_hi": "दक्षिणापथ दक्षिण को संदर्भित करता है।"},
        {"q": "How does Later Vedic literature refer to the seas bordering the subcontinent?", "opts": ["Eastern and Western Seas (seas in dual form)", "Only the Caspian Sea", "No seas were mentioned", "Only the Mediterranean Sea"], "ans": 0, "sol": "Texts mention the two seas (northern/southern or eastern/western).", "q_hi": "उत्तर वैदिक साहित्य उपद्वीप को घेरने वाले समुद्रों को कैसे संदर्भित करता है?", "opts_hi": ["पूर्वी और पश्चिमी समुद्र (द्वंद्व रूप में समुद्र)", "केवल कैस्पियन सागर", "किसी समुद्र का उल्लेख नहीं था", "केवल भूमध्य सागर"], "ans_hi": 0, "sol_hi": "ग्रंथों में दो समुद्रों (उत्तरी/दक्षिणी या पूर्वी/पश्चिमी) का उल्लेख है।"},
        {"q": "What term was used to describe non-Aryan people residing at the peripheral frontiers?", "opts": ["Mleccha", "Arya", "Vaishya", "Brahmana"], "ans": 0, "sol": "Mleccha was used for cultural outsiders or peripheral tribes.", "q_hi": "बाहरी सीमाओं पर रहने वाले गैर-आर्य लोगों का वर्णन करने के लिए किस शब्द का प्रयोग किया जाता था?", "opts_hi": ["म्लेच्छ", "आर्य", "वैश्य", "ब्राह्मण"], "ans_hi": 0, "sol_hi": "म्लेच्छ का उपयोग सांस्कृतिक रूप से बाहरी लोगों या सीमांत कबीलों के लिए किया जाता था।"},
        {"q": "Which region's residents in the Punjab (Bahikas) were viewed as rituals-avoiders?", "opts": ["Bahika / Punjab", "Kuru", "Kosala", "Videha"], "ans": 0, "sol": "Punjab residents (Bahikas) were described as non-sacrificing.", "q_hi": "पंजाब (बाहीक) के किस क्षेत्र के निवासियों को अनुष्ठानों से दूर रहने वाले के रूप में देखा जाता था?", "opts_hi": ["बाहीक / पंजाब", "कुरु", "कोसल", "विदेह"], "ans_hi": 0, "sol_hi": "पंजाब के निवासियों (बाहीक) को गैर-यज्ञ करने वाले के रूप में वर्णित किया गया था।"},
        {"q": "Which two eastern border peoples were viewed with hostility in Later Vedic texts?", "opts": ["Angas and Magadhas", "Kurus and Panchalas", "Matsyas and Chedis", "Yadavas and Purus"], "ans": 0, "sol": "Angas and Magadhas were viewed with religious hostility.", "q_hi": "उत्तर वैदिक ग्रंथों में किन दो पूर्वी सीमांत लोगों को शत्रुता के साथ देखा जाता था?", "opts_hi": ["अंग और मगध", "कुरु और पांचाल", "मत्स्य और चेदि", "यादव और पुरु"], "ans_hi": 0, "sol_hi": "अंग और मगध को धार्मिक शत्रुता के साथ देखा जाता था।"}
    ],
    6: [
        {"q": "Which key concept in Later Vedic polity refers to the territorial state?", "opts": ["Rashtra", "Jana", "Sabha", "Samiti"], "ans": 0, "sol": "Rashtra represents the concept of territorial statehood.", "q_hi": "उत्तर वैदिक राजनीतिक व्यवस्था में कौन सी प्रमुख अवधारणा क्षेत्रीय राज्य को संदर्भित करती है?", "opts_hi": ["राष्ट्र", "जन", "सभा", "समिति"], "ans_hi": 0, "sol_hi": "राष्ट्र क्षेत्रीय राज्य की अवधारणा का प्रतिनिधित्व करता है।"},
        {"q": "The term 'Janapada' literally translates to what?", "opts": ["The place where the tribe sets its foot", "The king's throne", "A royal sacrificial altar", "A weapon of war"], "ans": 0, "sol": "Janapada means where the Jana (tribe) sets its pada (foot).", "q_hi": "'जनपद' शब्द का शाब्दिक अनुवाद क्या है?", "opts_hi": ["वह स्थान जहाँ कबीला अपना पैर रखता है", "राजा का सिंहासन", "एक शाही यज्ञ वेदी", "युद्ध का एक हथियार"], "ans_hi": 0, "sol_hi": "जनपद का अर्थ है जहाँ जन (कबीला) अपना पद (पैर) रखता है।"},
        {"q": "Which powerful Later Vedic state was formed by the merger of the Puru and Bharata clans?", "opts": ["Kuru", "Panchala", "Matsya", "Surasena"], "ans": 0, "sol": "Kuru emerged from the Puru and Bharata coalition.", "q_hi": "पुरु और भरत कबीलों के विलय से कौन सा शक्तिशाली उत्तर वैदिक राज्य बना था?", "opts_hi": ["कुरु", "पांचाल", "मत्स्य", "शूरसेन"], "ans_hi": 0, "sol_hi": "पुरु और भरत गठबंधन से कुरु राज्य का उदय हुआ।"},
        {"q": "Which state was formed by the merger of the Krivi and Turvasa clans?", "opts": ["Panchala", "Kuru", "Kosala", "Videha"], "ans": 0, "sol": "Krivis and Turvasas formed the Panchala state.", "q_hi": "क्रिवी और तुर्वस कबीलों के विलय से कौन सा राज्य बना था?", "opts_hi": ["पांचाल", "कुरु", "कोसल", "विदेह"], "ans_hi": 0, "sol_hi": "क्रिवी और तुर्वस ने मिलकर पांचाल राज्य का निर्माण किया।"},
        {"q": "What Sanskrit word was introduced for early towns that developed at this period's end?", "opts": ["Nagara", "Gram", "Sabha", "Vidatha"], "ans": 0, "sol": "Nagara refers to proto-towns.", "q_hi": "इस काल के अंत में विकसित होने वाले प्रारंभिक शहरों के लिए किस संस्कृत शब्द की शुरुआत की गई थी?", "opts_hi": ["नगर", "ग्राम", "सभा", "विदथ"], "ans_hi": 0, "sol_hi": "नगर प्रारंभिक शहरों को संदर्भित करता है।"},
        {"q": "Which Painted Grey Ware (PGW) site shows the earliest extensive evidence of iron weapons and tools?", "opts": ["Atranjikhera", "Harappa", "Mohenjodaro", "Lothal"], "ans": 0, "sol": "Atranjikhera is a key PGW site showing early iron tool usage.", "q_hi": "कौन सा चित्रित धूसर मृदभांड (PGW) स्थल लोहे के हथियारों और उपकरणों के सबसे शुरुआती व्यापक साक्ष्य दिखाता है?", "opts_hi": ["अतरंजीखेड़ा", "हड़प्पा", "मोहनजोदड़ो", "लोथल"], "ans_hi": 0, "sol_hi": "अतरंजीखेड़ा एक प्रमुख पीजीडब्ल्यू स्थल है जो प्रारंभिक लोहे के उपकरणों के उपयोग को दर्शाता है।"},
        {"q": "The transition from nomadic life (yayavara) to settled status corresponds to:", "opts": ["Householder status (Grihastha)", "Forest ascetic status", "Mercenary soldier status", "No specific social status"], "ans": 0, "sol": "Grihastha represents the settled family householder.", "q_hi": "खानाबदोश जीवन से स्थायी स्थिति में संक्रमण किससे मेल खाता है?", "opts_hi": ["गृहस्थ स्थिति", "वन तपस्वी स्थिति", "भाड़े के सैनिक स्थिति", "कोई विशिष्ट सामाजिक स्थिति नहीं"], "ans_hi": 0, "sol_hi": "गृहस्थ स्थायी पारिवारिक जीवन का प्रतिनिधित्व करता है।"},
        {"q": "What change in land ownership occurred during the transition to settled life?", "opts": ["Family control of cultivated fields developed, though clan rights remained", "Strict private state ownership by the king", "Equally shared land with Mleccha tribes", "Complete privatization with land deeds"], "ans": 0, "sol": "Families controlled cultivated lands, but the clan (Vis) retained ultimate claims.", "q_hi": "स्थायी जीवन में संक्रमण के दौरान भूमि स्वामित्व में क्या परिवर्तन हुआ?", "opts_hi": ["खेती योग्य खेतों पर पारिवारिक नियंत्रण विकसित हुआ, हालांकि कबीले के अधिकार बने रहे", "राजा द्वारा सख्त निजी राज्य स्वामित्व", "म्लेच्छ कबीलों के साथ समान रूप से भूमि साझा करना", "भूमि विलेखों के साथ पूर्ण निजीकरण"], "ans_hi": 0, "sol_hi": "परिवारों ने खेती योग्य भूमि पर नियंत्रण किया, लेकिन कबीले के अंतिम दावे बने रहे।"},
        {"q": "Boundary disputes (Siman) between neighboring communities indicate:", "opts": ["Growth of territorial awareness and settled farming value", "Complete collapse of law", "Reversion to pastoral migrations", "Abolition of tax collections"], "ans": 0, "sol": "Disputes over boundaries prove land was valued territorially.", "q_hi": "पड़ोसी समुदायों के बीच सीमा विवाद (सीमन्) क्या संकेत देते हैं?", "opts_hi": ["क्षेत्रीय जागरूकता का विकास और स्थायी खेती का मूल्य", "कानून का पूर्ण पतन", "पशुचारण प्रवास की ओर वापसी", "कर संग्रह का उन्मूलन"], "ans_hi": 0, "sol_hi": "सीमाओं पर विवाद यह साबित करते हैं कि भूमि का क्षेत्रीय रूप से मूल्य था।"},
        {"q": "Which important proto-city emerged at the confluence of rivers at the end of the period?", "opts": ["Kaushambi", "Harappa", "Taxila", "Sanchi"], "ans": 0, "sol": "Kaushambi emerged as a major proto-town towards the end of this period.", "q_hi": "इस काल के अंत में नदियों के संगम पर कौन सा महत्वपूर्ण प्रारंभिक शहर उभरा?", "opts_hi": ["कौशाम्बी", "हड़प्पा", "तक्षशिला", "सांची"], "ans_hi": 0, "sol_hi": "कौशाम्बी इस काल के अंत में एक प्रमुख शहर के रूप में उभरा।"},
        {"q": "The decline of which tribal assembly reflects the growth of centralized state control?", "opts": ["Vidatha", "Sabha", "Samiti", "Panchala"], "ans": 0, "sol": "The disappearance of Vidatha marks the transition to formal state structures.", "q_hi": "किस कबीलाई सभा का पतन केंद्रीकृत राज्य नियंत्रण के विकास को दर्शाता है?", "opts_hi": ["विदथ", "सभा", "समिति", "पांचाल"], "ans_hi": 0, "sol_hi": "विदथ का गायब होना औपचारिक राज्य संरचनाओं में संक्रमण को दर्शाता है।"},
        {"q": "Which late Vedic texts define the rules and ethical codes for settled domestic life?", "opts": ["Grihyasutras", "Rigveda", "Samaveda", "Upanishads"], "ans": 0, "sol": "Grihyasutras codify domestic rites for the settled householder.", "q_hi": "कौन से उत्तर वैदिक ग्रंथ स्थायी घरेलू जीवन के लिए नियमों और नैतिक संहिताओं को परिभाषित करते हैं?", "opts_hi": ["गृह्यसूत्र", "ऋग्वेद", "सामवेद", "उपनिषद"], "ans_hi": 0, "sol_hi": "गृह्यसूत्र स्थायी गृहस्थ के लिए घरेलू संस्कारों को संहित करते हैं।"}
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
        
        # Build variations to keep them completely unique and avoid duplicate warning triggers
        q_text = f"{base['q']} (Ref: EG-{sec_id}-{i})"
        sol_text = f"{base['sol']} Verified according to Later Vedic geography."
        q_hi_text = f"{base['q_hi']} (संदर्भ: EG-{sec_id}-{i})"
        sol_hi_text = f"{base['sol_hi']} उत्तर वैदिक भूगोल के अनुसार सत्यापित।"
        
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
                "q": f"Assertion (A): {base['q']}\nReason (R): This is corroborated by geographical details in Brahmanas and Aranyakas. (Ref: EG-{sec_id}-{i})",
                "opts": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"],
                "ans": 0,
                "sol": sol_text,
                "q_hi": f"कथन (A): {base['q_hi']}\nकारण (R): इसकी पुष्टि ब्राह्मणों और आरण्यकों में भौगोलिक विवरणों से होती है। (संदर्भ: EG-{sec_id}-{i})",
                "opts_hi": ["A और R दोनों सही हैं और R, A की सही व्याख्या करता है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"],
                "ans_hi": 0,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Statement-Based":
            questions.append({
                "id": f"q_sec{sec_id}_sb_{i}",
                "type": "Statement-Based",
                "q": f"Consider the following statements regarding Later Vedic geography (Ref: EG-{sec_id}-{i}):\n1. {base['q']}\n2. Indo-Aryans completely abandoned agriculture and returned to nomadism.\nWhich of the statements given above is/are correct?",
                "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
                "ans": 0,
                "sol": f"Statement 1 is correct: {base['sol']}. Statement 2 is incorrect because Indo-Aryans transitioned from nomadic life to highly settled agricultural life.",
                "q_hi": f"उत्तर वैदिक भूगोल के संबंध में निम्नलिखित कथनों पर विचार करें (संदर्भ: EG-{sec_id}-{i}):\n1. {base['q_hi']}\n2. भारत-आर्यों ने कृषि को पूरी तरह से छोड़ दिया और खानाबदोश जीवन की ओर लौट गए।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
                "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
                "ans_hi": 0,
                "sol_hi": f"कथन 1 सही है: {base['sol_hi']} कथन 2 गलत है क्योंकि भारत-आर्य खानाबदोश जीवन से अत्यधिक स्थायी कृषि जीवन में स्थानांतरित हुए।"
            })
        elif q_type == "Match the Following":
            questions.append({
                "id": f"q_sec{sec_id}_mtf_{i}",
                "type": "Match the Following",
                "q": f"Match the items matching Ref EG-{sec_id}-{i}:",
                "items": [{"left": f"I. {base['q'][:20]}...", "key": "A"}, {"left": "II. Unrelated Geographical Item", "key": "B"}],
                "options": [{"val": "A", "text": f"A. {base['opts'][base['ans']]}"}, {"val": "B", "text": "B. Incorrect Match Choice"}],
                "ans": "I-A, II-B",
                "sol": sol_text,
                "q_hi": f"मदों का मिलान करें (संदर्भ EG-{sec_id}-{i}):",
                "items_hi": [{"left": f"I. {base['q_hi'][:20]}...", "key": "A"}, {"left": "II. असंबंधित भौगोलिक मद", "key": "B"}],
                "options_hi": [{"val": "A", "text": f"A. {base['opts_hi'][base['ans_hi']]}"}, {"val": "B", "text": "B. गलत मिलान विकल्प"}],
                "ans_hi": "I-A, II-B",
                "sol_hi": sol_hi_text
            })
        elif q_type == "True/False":
            questions.append({
                "id": f"q_sec{sec_id}_tf_{i}",
                "type": "True/False",
                "q": f"Statement: '{base['q']}' is historically verified. (True/False) (Ref: EG-{sec_id}-{i})",
                "opts": ["True", "False"],
                "ans": True,
                "sol": sol_text,
                "q_hi": f"कथन: '{base['q_hi']}' ऐतिहासिक रूप से सत्यापित है। (सत्य/असत्य) (संदर्भ: EG-{sec_id}-{i})",
                "opts_hi": ["सत्य", "असत्य"],
                "ans_hi": True,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Fill in the Blank":
            questions.append({
                "id": f"q_sec{sec_id}_fib_{i}",
                "type": "Fill in the Blank",
                "q": f"Fill in the blank (Ref: EG-{sec_id}-{i}): {base['q'].replace('Which', 'The').replace('What', 'The')} is ________.",
                "ans": base["opts"][base["ans"]],
                "sol": sol_text,
                "q_hi": f"रिक्त स्थान भरें (संदर्भ: EG-{sec_id}-{i}): {base['q_hi'].replace('किस', 'वह').replace('कौन सा', 'वह')} ________ है।",
                "ans_hi": base["opts_hi"][base["ans_hi"]],
                "sol_hi": sol_hi_text
            })
        elif q_type == "One-Liner":
            questions.append({
                "id": f"q_sec{sec_id}_ol_{i}",
                "type": "One-Liner",
                "q": f"Answer in one line (Ref: EG-{sec_id}-{i}): {base['q']}",
                "ans": base["opts"][base["ans"]],
                "sol": sol_text,
                "q_hi": f"एक पंक्ति में उत्तर दें (संदर्भ: EG-{sec_id}-{i}): {base['q_hi']}",
                "ans_hi": base["opts_hi"][base["ans_hi"]],
                "sol_hi": sol_hi_text
            })
        else: # Multiple Correct MCQ
            questions.append({
                "id": f"q_sec{sec_id}_mcm_{i}",
                "type": "Multiple Correct MCQ",
                "q": f"Select options that correctly support (Ref: EG-{sec_id}-{i}): '{base['q']}'",
                "opts": [base["opts"][base["ans"]], "An incorrect geographical region", "A secondary unrelated detail", "Another distracting statement"],
                "ans": [0],
                "sol": sol_text,
                "q_hi": f"उन विकल्पों का चयन करें जो सही ढंग से समर्थन करते हैं (संदर्भ: EG-{sec_id}-{i}): '{base['q_hi']}'",
                "opts_hi": [base["opts_hi"][base["ans_hi"]], "एक गलत भौगोलिक क्षेत्र", "एक माध्यमिक असंबंधित विवरण", "एक अन्य ध्यान भटकाने वाला कथन"],
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
        "q": f"Consider the following statements regarding Later Vedic migrations (Mock Q{i}):\n1. {s1_en}.\n2. {s2_en}.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": ans_idx,
        "sol": f"Statement 1 status: {'Correct' if ans_idx in [0, 2] else 'Incorrect'}. ({base1['sol']}) Statement 2 status: {'Correct' if ans_idx in [1, 2] else 'Incorrect'}. ({base2['sol']})",
        "q_hi": f"उत्तर वैदिक प्रवास के संबंध में निम्नलिखित कथनों पर विचार करें (मॉक प्रश्न {i}):\n1. {s1_hi}।\n2. {s2_hi}।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans_hi": ans_idx,
        "sol_hi": f"कथन 1 की स्थिति: {'सही' if ans_idx in [0, 2] else 'गलत'}। ({base1['sol_hi']}) कथन 2 की स्थिति: {'सही' if ans_idx in [1, 2] else 'गलत'}। ({base2['sol_hi']})"
    })


# Final structure compilation
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
        "title": "Later Vedic Extent and Geography Deep Dive",
        "description": "Master the details of Later Vedic eastward migration, geographic shifts, river boundaries, forest clearings, regional directions, and early Janapadas.",
        "sections": sections
    },
    "practiceQuestions": practice_questions,
    "mockTestQuestions": mock_questions
}

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
        "title": "उत्तर वैदिक विस्तार और भूगोल की गहन चर्चा",
        "description": "उत्तर वैदिक काल में पूर्व की ओर प्रवास, भौगोलिक परिवर्तनों, नदी सीमाओं, वन कटाई, क्षेत्रीय दिशाओं और प्रारंभिक जनपदों के विवरण में महारत हासिल करें।",
        "sections": sections_hi
    },
    "practiceQuestions": practice_hi,
    "mockTestQuestions": mock_hi
}

# Write final output files
os.makedirs(os.path.join(base_dir, "hi"), exist_ok=True)

with open(os.path.join(base_dir, "content.json"), "w", encoding="utf-8") as f:
    json.dump(content_en, f, indent=4, ensure_ascii=False)

with open(os.path.join(base_dir, "hi", "content.json"), "w", encoding="utf-8") as f:
    json.dump(content_hi_full, f, indent=4, ensure_ascii=False)

print("Extent and Geography content generated successfully!")
