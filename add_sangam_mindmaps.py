#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/ancient_history/History-of-South-India-The-Sangam-Dynasties"

MINDMAP_DATA = {
    "sangam-literature": {
        "en": [
            {"label": "Grammar & Poetics", "type": "branch", "date": "Tolkappiyam", "children": [
                {"label": "Tolkappiyam: Authored by Tolkappiyar (disciple of Agastya)", "type": "leaf"},
                {"label": "3 Sections (Eluttadikaram-Letters, Colladikaram-Words, Poruladikaram-Subject matter)", "type": "leaf"},
                {"label": "Poruladikaram outlines the social, political, and love life of Sangam Tamil land", "type": "leaf"}]},
            {"label": "Melkanakku (Major Works)", "type": "branch", "date": "Poetry", "children": [
                {"label": "Ettutogai (8 Anthologies): Includes Purananuru (war/heroism) and Akananuru (love)", "type": "leaf"},
                {"label": "Pattupattu (10 Idylls): Long narrative poems including Maduraikkanchi and Pattinappalai", "type": "leaf"}]},
            {"label": "Kilkanakku (Minor Works)", "type": "branch", "date": "Didactic", "children": [
                {"label": "Pathinenkilkanakku: 18 minor works focused on moral, ethical, and social codes", "type": "leaf"},
                {"label": "Tirukkural: Authored by Thiruvalluvar, dealing with Aram (Virtue), Porul (Wealth), and Inbam (Love)", "type": "leaf"},
                {"label": "Naladiyar: Collection of moral verses compiled by Jain monks", "type": "leaf"}]},
            {"label": "Five Great Epics", "type": "branch", "date": "Epics", "children": [
                {"label": "Silappadikaram: Ilango Adigal (story of Kannagi, Kovalan, Madhavi, and the Anklet)", "type": "leaf"},
                {"label": "Manimekalai: Sathanar (sequel to Silappadikaram; explains Buddhist philosophy)", "type": "leaf"},
                {"label": "Civaka Cintamani: Tiruttakkadevar (infused with Jain mythology)", "type": "leaf"}]},
            {"label": "Poetic Classifications", "type": "branch", "date": "Styles", "children": [
                {"label": "Akam: Subjective poetry dealing with love, domestic life, and inner emotions", "type": "leaf"},
                {"label": "Puram: Objective poetry dealing with public life, war, royal praise, and hero stones", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "व्याकरण और काव्यशास्त्र", "type": "branch", "date": "तोल्काप्पियम", "children": [
                {"label": "तोल्काप्पियम: तोल्काप्पियर (ऋषि अगस्त्य के शिष्य) द्वारा रचित", "type": "leaf"},
                {"label": "3 भाग (एळुत्तादिकारम-अक्षर, चोल्लादिकारम-शब्द, पोरुलादिकारम-विषयवस्तु)", "type": "leaf"},
                {"label": "पोरुलादिकारम संगम तमिल क्षेत्र के सामाजिक, राजनीतिक और वैवाहिक जीवन को रेखांकित करता है", "type": "leaf"}]},
            {"label": "मेलकणक्कु (प्रमुख कृतियाँ)", "type": "branch", "date": "काव्य", "children": [
                {"label": "एट्टुत्तोगई (आठ संकलन): पुरनानूरू (युद्ध/वीरता) और अकनानूरू (प्रेम) शामिल हैं", "type": "leaf"},
                {"label": "पत्तुप्पाट्टु (दस गीत): दस लंबी कथात्मक कविताएँ जिनमें मदुरैक्कांची और पत्तिनप्पालै शामिल हैं", "type": "leaf"}]},
            {"label": "कीलकणक्कु (लघु कृतियाँ)", "type": "branch", "date": "नीतिशास्त्र", "children": [
                {"label": "पतिनेनकीलकणक्कु: नैतिक, आचार और सामाजिक संहिताओं पर केंद्रित 18 लघु कृतियाँ", "type": "leaf"},
                {"label": "तिरुक्कुरल: तिरुवल्लुवर द्वारा रचित; अराम (धर्म), पोरुल (अर्थ) और इनबम (काम) से संबंधित", "type": "leaf"},
                {"label": "नालदियार: जैन मुनियों द्वारा संकलित नैतिक छंदों का संग्रह", "type": "leaf"}]},
            {"label": "पाँच महाकाव्य", "type": "branch", "date": "महाकाव्य", "children": [
                {"label": "शिलप्पादिकारम: इलांगो आदिगल द्वारा रचित (कन्नगी, कोवलन, माधवी और पायल की कहानी)", "type": "leaf"},
                {"label": "मणिमेकलै: शीतलै सतनार द्वारा रचित (शिलप्पादिकारम का अगला भाग; बौद्ध दर्शन का प्रतिपादन)", "type": "leaf"},
                {"label": "जीवक चिंतामणि: तिरुत्तक्कदेवर द्वारा रचित (जैन दर्शन और कथाओं से ओतप्रोत)", "type": "leaf"}]},
            {"label": "काव्य वर्गीकरण", "type": "branch", "date": "शैलियाँ", "children": [
                {"label": "अकम: आंतरिक भावनाओं, गृहस्थ जीवन और प्रेम पर आधारित व्यक्तिपरक कविताएँ", "type": "leaf"},
                {"label": "पुरम: सार्वजनिक जीवन, युद्ध, वीरता, राजकीय स्तुति और वीर पत्थरों पर आधारित वस्तुपरक कविताएँ", "type": "leaf"}]}
        ]
    },
    "cholas": {
        "en": [
            {"label": "Political Geography", "type": "branch", "date": "Region", "children": [
                {"label": "Core: Cauvery delta and northeastern Tamil Nadu (Cholamandalam)", "type": "leaf"},
                {"label": "Inland Capital: Uraiyur (famous cotton weaving hub)", "type": "leaf"},
                {"label": "Coastal Capital & Port: Kaveripattinam / Puhar", "type": "leaf"},
                {"label": "Royal Emblem: Tiger", "type": "leaf"}]},
            {"label": "King Karikala", "type": "branch", "date": "Ruler", "children": [
                {"label": " Karikala Chola: Most prominent Sangam Chola king", "type": "leaf"},
                {"label": "Battle of Venni: Defeated combined forces of Cheras, Pandyas, and 11 chieftains", "type": "leaf"},
                {"label": "Constructed the Kallanai (Grand Anicut) dam on Cauvery river using war prisoners", "type": "leaf"},
                {"label": "Patronized Pattinappalai, an epic describing Puhar's trade", "type": "leaf"}]},
            {"label": "Decline", "type": "branch", "date": "Decline", "children": [
                {"label": "Weak successors led to decline under pressure from Pandyas & Kalabhras", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजनीतिक भूगोल", "type": "branch", "date": "क्षेत्र", "children": [
                {"label": "केंद्र: कावेरी डेल्टा और पूर्वोत्तर तमिलनाडु (चोलमंडलम)", "type": "leaf"},
                {"label": "आंतरिक राजधानी: उरैयूर (सूती वस्त्र बुनाई का प्रसिद्ध केंद्र)", "type": "leaf"},
                {"label": "तटीय राजधानी और बंदरगाह: कावेरीपट्टनम / पुहार", "type": "leaf"},
                {"label": "राजकीय प्रतीक: बाघ", "type": "leaf"}]},
            {"label": "राजा करिकाल", "type": "branch", "date": "शासक", "children": [
                {"label": "करिकाल चोल: संगम काल के सबसे प्रतापी चोल शासक", "type": "leaf"},
                {"label": "वेन्नी का युद्ध: चेर, पाण्ड्य और 11 छोटे सामंतों की संयुक्त सेना को पराजित किया", "type": "leaf"},
                {"label": "युद्धबंदियों की सहायता से कावेरी नदी पर कल्लानाई (ग्रैंड अनिकट) बांध का निर्माण कराया", "type": "leaf"},
                {"label": "पत्तिनप्पालै महाकाव्य को संरक्षण दिया, जिसमें पुहार के समृद्ध व्यापार का वर्णन है", "type": "leaf"}]},
            {"label": "पतन", "type": "branch", "date": "पतन", "children": [
                {"label": "कमजोर उत्तराधिकारियों के कारण पाण्ड्यों और कलभ्रों के दबाव में चोल शक्ति का ह्रास हुआ", "type": "leaf"}]}
        ]
    },
    "cheras": {
        "en": [
            {"label": "Political Geography", "type": "branch", "date": "Region", "children": [
                {"label": "Core: Modern Kerala and western parts of Tamil Nadu (Kongu region)", "type": "leaf"},
                {"label": "Capital: Vanji (Karur); Ports: Muziris (major Roman trade port) and Tondi", "type": "leaf"},
                {"label": "Royal Emblem: Bow and Arrow", "type": "leaf"}]},
            {"label": "Key Rulers", "type": "branch", "date": "Rulers", "children": [
                {"label": "Udiyanjeral: Earliest ruler; myth says he fed both armies of Mahabharata war", "type": "leaf"},
                {"label": "Nedunjeral Adan: Defeated Yavanas; claimed boundaries up to Himalayas", "type": "leaf"},
                {"label": "Senguttuvan (Red Chera): Main hero of Silappadikaram; established Pattini cult", "type": "leaf"}]},
            {"label": "Socio-Economic", "type": "branch", "date": "Trade", "children": [
                {"label": "Monopolized black pepper and spice trade with the Roman Empire", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजनीतिक भूगोल", "type": "branch", "date": "क्षेत्र", "children": [
                {"label": "केंद्र: आधुनिक केरल और तमिलनाडु के पश्चिमी हिस्से (कोंगु क्षेत्र)", "type": "leaf"},
                {"label": "राजधानी: वंजी (करूर); बंदरगाह: मुज़िरिस (मुख्य रोमन व्यापार केंद्र) और तोंडी", "type": "leaf"},
                {"label": "राजकीय प्रतीक: धनुष और बाण", "type": "leaf"}]},
            {"label": "प्रमुख शासक", "type": "branch", "date": "शासक", "children": [
                {"label": "उदियनजेरल: प्रथम शासक; मान्यता है कि उन्होंने महाभारत युद्ध की दोनों सेनाओं को भोजन कराया था", "type": "leaf"},
                {"label": "नेदुनजेरल आदान: यवनों को पराजित किया; हिमालय तक सीमा विस्तार का दावा किया", "type": "leaf"},
                {"label": "सेंगट्टुवन (लाल चेर): शिलप्पादिकारम के मुख्य नायक; पत्तिनी (कन्नगी) पूजा की शुरुआत की", "type": "leaf"}]},
            {"label": "सामाजिक-आर्थिक", "type": "branch", "date": "व्यापार", "children": [
                {"label": "रोमन साम्राज्य के साथ काली मिर्च और मसालों के व्यापार पर पूर्ण एकाधिकार था", "type": "leaf"}]}
        ]
    },
    "pandyas": {
        "en": [
            {"label": "Political Geography", "type": "branch", "date": "Region", "children": [
                {"label": "Core: Southern Tamil Nadu (Vaigai and Tamraparni basins)", "type": "leaf"},
                {"label": "Capital: Madurai (host of all three Tamil Sangam assemblies)", "type": "leaf"},
                {"label": "Port: Korkai (famous for its pearl fishery)", "type": "leaf"},
                {"label": "Royal Emblem: Fish (or Twin Fish)", "type": "leaf"}]},
            {"label": "Key Rulers", "type": "branch", "date": "Rulers", "children": [
                {"label": "Nedunjeliyan I: Executed Kovalan by mistake; died of grief when Kannagi proved innocence", "type": "leaf"},
                {"label": "Nedunjeliyan II: Defeated Chera, Chola, and 5 chieftains at Battle of Talaiyalanganam", "type": "leaf"}]},
            {"label": "Socio-Economic", "type": "branch", "date": "Trade", "children": [
                {"label": "Enriched by Roman pearl trade; mentioned by Megasthenes (ruled by Herakles' daughter)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजनीतिक भूगोल", "type": "branch", "date": "क्षेत्र", "children": [
                {"label": "केंद्र: दक्षिणी तमिलनाडु (वैगई और ताम्रपर्णी नदियाँ)", "type": "leaf"},
                {"label": "राजधानी: मदुरै (तीनों तमिल संगम परिषदों का आयोजन स्थल)", "type": "leaf"},
                {"label": "बंदरगाह: कोरकई (उत्कृष्ट मोतियों के उत्पादन के लिए प्रसिद्ध)", "type": "leaf"},
                {"label": "राजकीय प्रतीक: मछली (या जुड़वां मछली)", "type": "leaf"}]},
            {"label": "प्रमुख शासक", "type": "branch", "date": "शासक", "children": [
                {"label": "नेडुंजेलियन प्रथम: कोवलन को गलती से फाँसी दी; कन्नगी द्वारा बेगुनाही साबित करने पर आघात से मृत्यु", "type": "leaf"},
                {"label": "नेडुंजेलियन द्वितीय: तलैयालंगानम के युद्ध में चेर, चोल और 5 सामंतों की संयुक्त सेना को हराया", "type": "leaf"}]},
            {"label": "सामाजिक-आर्थिक", "type": "branch", "date": "व्यापार", "children": [
                {"label": "रोमन मोती व्यापार से समृद्ध हुए; मेगस्थनीज ने भी इनके राज्य का उल्लेख किया है (हेराक्लीज की पुत्री का शासन)", "type": "leaf"}]}
        ]
    },
    "aspects-of-sangam-administration": {
        "en": [
            {"label": "Monarch & Court", "type": "branch", "date": "Polity", "children": [
                {"label": "Hereditary monarchy (King: Vendan, Ko, Mannan); titles like Adhiraja", "type": "leaf"},
                {"label": "Royal Court: Avai (dispensed justice; center of political deliberations)", "type": "leaf"}]},
            {"label": "Aimperungulu (5 Assemblies)", "type": "branch", "date": "Council", "children": [
                {"label": "Amaichar: Ministers assisting in state decisions", "type": "leaf"},
                {"label": "Purohitar: Priests guiding religious duties", "type": "leaf"},
                {"label": "Senapatiyar: Commanders leading the military forces", "type": "leaf"},
                {"label": "Thuthar: Envoys/Diplomats managing foreign relations", "type": "leaf"},
                {"label": "Orrar: Spies gathering internal and external intelligence", "type": "leaf"}]},
            {"label": "Revenue Administration", "type": "branch", "date": "Taxes", "children": [
                {"label": "Karai: Land tax; Ulgu: Customs duties on trade; Irai: Tributes paid by chieftains", "type": "leaf"},
                {"label": "Kollai: War booty seized from defeated kingdoms", "type": "leaf"}]},
            {"label": "Military & Police", "type": "branch", "date": "Force", "children": [
                {"label": "Fourfold army: Chariots, Elephants, Cavalry, Infantry; weapons: swords, spears, bows", "type": "leaf"},
                {"label": "Hero stones erected for fallen soldiers; capital guarded by Yavanas", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजा और राजदरबार", "type": "branch", "date": "राजव्यवस्था", "children": [
                {"label": "वंशानुगत राजतंत्र (राजा: वेंदम, को, मन्नम); अधिराज जैसी उपाधियाँ ग्रहण कीं", "type": "leaf"},
                {"label": "राजसभा: अवई (न्याय का सर्वोच्च केंद्र और राजनीतिक चर्चाओं का मुख्य स्थल)", "type": "leaf"}]},
            {"label": "अइम्पेरुंगुलु (पंच परिषद)", "type": "branch", "date": "सलाहकार", "children": [
                {"label": "अमैच्चर: मंत्रियों का समूह जो शासन कार्यों में सहयोग करता था", "type": "leaf"},
                {"label": "पुरोहितर: धार्मिक अनुष्ठानों और नीति निर्धारण में सहायक पुरोहित", "type": "leaf"},
                {"label": "सेनापतियर: सेना प्रमुख जो सैन्य बलों का नेतृत्व करते थे", "type": "leaf"},
                {"label": "तूतार: राजदूत जो बाह्य राज्यों के साथ संबंधों का संचालन करते थे", "type": "leaf"},
                {"label": "ओर्रार: गुप्तचर जो आंतरिक सुरक्षा और बाह्य योजनाओं की जानकारी लाते थे", "type": "leaf"}]},
            {"label": "राजस्व प्रशासन", "type": "branch", "date": "कर", "children": [
                {"label": "करई: भूमि कर; उल्गु: व्यापार पर सीमा शुल्क; इरै: सामंतों द्वारा दी जाने वाली भेंट", "type": "leaf"},
                {"label": "कोल्लै: पराजित राज्यों से लूटा गया युद्ध का माल", "type": "leaf"}]},
            {"label": "सेना और सुरक्षा", "type": "branch", "date": "सुरक्षा बल", "children": [
                {"label": "चतुरंगिणी सेना: रथ, गज, अश्व और पैदल सेना; शस्त्र: तलवार, भाला, धनुष", "type": "leaf"},
                {"label": "शहीद सैनिकों के लिए वीरगाथा पत्थर (नडुगल); राजधानी की सुरक्षा हेतु यवन नियुक्त", "type": "leaf"}]}
        ]
    },
    "aspects-of-sangam-society": {
        "en": [
            {"label": "Tinais (5 Physiographic Zones)", "type": "branch", "date": "Tinaic System", "children": [
                {"label": "Kurinji (Hills): Hunting & gathering; Murugan worship", "type": "leaf"},
                {"label": "Mullai (Pastoral): Shifting cultivation & cattle rearing; Mayon (Vishnu)", "type": "leaf"},
                {"label": "Marutam (Riverine): Wet paddy agriculture; Vendan (Indra)", "type": "leaf"},
                {"label": "Neithal (Coastal): Fishing & salt extraction; Varunan", "type": "leaf"},
                {"label": "Palai (Parched land): Robbery & plunder; Korravai (goddess)", "type": "leaf"}]},
            {"label": "Social Structure", "type": "branch", "date": "Classes", "children": [
                {"label": "Absence of strict Varna; classes based on occupation & land ownership", "type": "leaf"},
                {"label": "Arasar: Ruling class; Vellalar: Landowning class (Rich: Velir, Poor: Uzhavar)", "type": "leaf"},
                {"label": "Panar and Viraliyar: Traveling musicians & bards of high social standing", "type": "leaf"}]},
            {"label": "Position of Women", "type": "branch", "date": "Women", "children": [
                {"label": "Allowed intellectual pursuit (female poets like Avvaiyar and Nachchellaiyar)", "type": "leaf"},
                {"label": "Love marriage (Kalavu) was accepted; Sati (Tipappudal) practiced among elites", "type": "leaf"},
                {"label": "Life of widows was extremely ascetic and miserable", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "तिनै (पांच भौगोलिक परिदृश्य)", "type": "branch", "date": "तिनै व्यवस्था", "children": [
                {"label": "कुरिंजी (पर्वतीय क्षेत्र): शिकार और खाद्य संग्रह; मुरुगन (सेयोन) की पूजा", "type": "leaf"},
                {"label": "मुल्लई (चारगाह): पशुपालन और झूम कृषि; मायोन (विष्णु) की पूजा", "type": "leaf"},
                {"label": "मरुतम (मैदानी कृषि क्षेत्र): धान की सघन खेती; वेंदम (इंद्र) की पूजा", "type": "leaf"},
                {"label": "नेथल (तटीय क्षेत्र): मछली पकड़ना और नमक बनाना; वरुणन की पूजा", "type": "leaf"},
                {"label": "पालै (मरुभूमि/शुष्क क्षेत्र): लूटपाट और चोरी; कोर्रवई (विजय की देवी) की पूजा", "type": "leaf"}]},
            {"label": "सामाजिक संरचना", "type": "branch", "date": "वर्ग", "children": [
                {"label": "कठोर वर्ण व्यवस्था का अभाव; वर्ग विभाजन भूमि और व्यवसाय पर आधारित", "type": "leaf"},
                {"label": "अरासर: शासक वर्ग; वेल्लालर: कृषक/भूमिपति वर्ग (धनी: वेलिर, निर्धन: उझावर)", "type": "leaf"},
                {"label": "पानर और विरलियर: समाज में उच्च स्थान प्राप्त घुमंतू संगीतकार और कवि", "type": "leaf"}]},
            {"label": "महिला की स्थिति", "type": "branch", "date": "स्त्रियां", "children": [
                {"label": "बौद्धिक स्वतंत्रता: अव्वैयार और नच्चेल्लैयार जैसी कवयित्रियों का उल्लेख", "type": "leaf"},
                {"label": "गंधर्व विवाह (कलवु) स्वीकृत था; उच्च वर्गों में सती प्रथा (तीप्पाय्पुदल) का प्रचलन", "type": "leaf"},
                {"label": "विधवाओं का जीवन अत्यंत कष्टकारी और तपस्यापूर्ण होता था", "type": "leaf"}]}
        ]
    },
    "aspects-of-sangam-economy": {
        "en": [
            {"label": "Agriculture", "type": "branch", "date": "Agrarian", "children": [
                {"label": "Paddy was staple crop; sugarcane, ragi, pepper, ginger, turmeric grown", "type": "leaf"},
                {"label": "Cauvery delta was highly fertile ('equal to space occupied by a sleeping elephant')", "type": "leaf"}]},
            {"label": "Industry & Crafts", "type": "branch", "date": "Industry", "children": [
                {"label": "Cotton and Silk weaving reached high levels (Uraiyur weaving described as thin as snake's skin)", "type": "leaf"},
                {"label": "Shipbuilding, carpentry, metallurgy, pottery, and Korkai pearl diving", "type": "leaf"}]},
            {"label": "Internal Trade", "type": "branch", "date": "Markets", "children": [
                {"label": "Barter system was dominant; paddy and salt functioned as medium of exchange", "type": "leaf"},
                {"label": "Markets (Angadi) divided into Nalangadi (morning) and Allangadi (evening)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कृषि अर्थव्यवस्था", "type": "branch", "date": "कृषि", "children": [
                {"label": "धान मुख्य फसल थी; गन्ना, रागी, काली मिर्च, अदरक, हल्दी भी उगाई जाती थी", "type": "leaf"},
                {"label": "कावेरी डेल्टा की सघन उर्वरता का सुंदर वर्णन (सोते हुए हाथी की जगह के समान)", "type": "leaf"}]},
            {"label": "उद्योग और शिल्प", "type": "branch", "date": "शिल्प", "children": [
                {"label": "सूती और रेशमी बुनाई उत्कृष्ट स्तर पर (उरैयूर के कपड़ों की तुलना साँप की केंचुल से)", "type": "leaf"},
                {"label": "जहाज निर्माण, बढ़ईगीरी, धातु कर्म, कुम्हार कला और कोरकई की मोती खोज प्रणाली", "type": "leaf"}]},
            {"label": "आंतरिक व्यापार", "type": "branch", "date": "बाजार", "children": [
                {"label": "वस्तु विनिमय व्यवस्था प्रमुख; धान और नमक का विनिमय माध्यम के रूप में उपयोग", "type": "leaf"},
                {"label": "बाजार (अंगड़ी) दो भागों में विभाजित: नालंगड़ी (प्रातःकालीन) और अल्लंगड़ी (सायंकालीन)", "type": "leaf"}]}
        ]
    },
    "aspects-of-sangam-religion": {
        "en": [
            {"label": "Indigenous Beliefs", "type": "branch", "date": "Deities", "children": [
                {"label": "Murugan/Seyon: Patron deity of hills; associated with red color & Vel (spear)", "type": "leaf"},
                {"label": "Hero Stone (Nadukal) Worship: Commemorating brave soldiers; treated as living deity", "type": "leaf"},
                {"label": "Anangu concept: Spiritual, sacred power inherent in objects and places", "type": "leaf"}]},
            {"label": "Vedic Synthesis", "type": "branch", "date": "Integration", "children": [
                {"label": "Mayon (Krishna/Vishnu) and Vendan (Indra) integrated into the Tamil pantheon", "type": "leaf"},
                {"label": "Performance of Vedic sacrifices by kings (Pandya Mudukudumi)", "type": "leaf"}]},
            {"label": "Heterodox Sects", "type": "branch", "date": "Sects", "children": [
                {"label": "Buddhism and Jainism were popular in major trading cities like Puhar & Madurai", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मूल स्थानीय मान्यताएं", "type": "branch", "date": "देवता", "children": [
                {"label": "मुरुगन/सेयोन: पहाड़ियों के अधिपति देव; लाल रंग और वेल (भाला) से संबंधित", "type": "leaf"},
                {"label": "वीरगाथा पत्थर (नडुगल) पूजा: वीर सैनिकों की स्मृति में; बलि और मदिरा अर्पण", "type": "leaf"},
                {"label": "अणंगु की अवधारणा: प्राकृतिक वस्तुओं में निहित रहस्यमयी और पवित्र दैवीय शक्ति", "type": "leaf"}]},
            {"label": "वैदिक समन्वय", "type": "branch", "date": "एकीकरण", "children": [
                {"label": "मायोन (कृष्ण/विष्णु) और वेंदम (इंद्र) का तमिल देवमंडल में विलय हुआ", "type": "leaf"},
                {"label": "तमिल राजाओं (जैसे पाण्ड्य मुदुकुडुमी) द्वारा वैदिक यज्ञों का अनुष्ठान", "type": "leaf"}]},
            {"label": "नास्तिक/श्रमण संप्रदाय", "type": "branch", "date": "संप्रदाय", "children": [
                {"label": "पुहार और मदुरै जैसे बड़े व्यापारिक केंद्रों में बौद्ध और जैन धर्म का गहरा प्रभाव", "type": "leaf"}]}
        ]
    },
    "aspects-of-sangam-culture": {
        "en": [
            {"label": "Fine Arts", "type": "branch", "date": "Arts", "children": [
                {"label": "Music: Yazh (lute/harp) and Kuzhal (flute) were prominent", "type": "leaf"},
                {"label": "Dance: Koothu (folk dance-dramas); Viraliyar were professional dancers", "type": "leaf"}]},
            {"label": "Food & Life", "type": "branch", "date": "Daily Life", "children": [
                {"label": "Diet: Rice, fish, meat (venison, pork), fermented toddy (liquor)", "type": "leaf"},
                {"label": "Dress: Minimal cotton/silk; use of flowers for battle context (Vetchi, Karanjai)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "ललित कलाएं", "type": "branch", "date": "कला", "children": [
                {"label": "संगीत: याझ (वीणा/हर्प) और कुझल (बांसुरी) वाद्य यंत्रों का व्यापक प्रचलन", "type": "leaf"},
                {"label": "नृत्य: कूथू (नृत्य-नाटक); विरलियर व्यावसायिक नर्तकियों का समूह था", "type": "leaf"}]},
            {"label": "भोजन और जीवन", "type": "branch", "date": "दैनिक जीवन", "children": [
                {"label": "आहार: चावल, मछली, मांस (हिरण, सूअर) और ताड़ी (ताड़ की शराब) का सेवन", "type": "leaf"},
                {"label": "पोशाक: हल्के सूती/रेशमी वस्त्र; युद्ध स्थितियों के अनुसार फूलों के आभूषण", "type": "leaf"}]}
        ]
    },
    "dynasties-of-foreign-origin": {
        "en": [
            {"label": "Yavanas in Tamil Land", "type": "branch", "date": "Foreigners", "children": [
                {"label": "Yavana: Collective term for Greeks, Romans, and West Asians", "type": "leaf"},
                {"label": "Settled in port cities (Yavana Cheris) under agreement with Tamil kings", "type": "leaf"}]},
            {"label": "Military & Tech Roles", "type": "branch", "date": "Employment", "children": [
                {"label": "Yavanas employed as fierce palace guards, royal bodyguards, and city night watchmen", "type": "leaf"},
                {"label": "Worked as engineers to construct fortress walls, siege weapons, and lighthouses", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "तमिल क्षेत्र में यवन", "type": "branch", "date": "विदेशी", "children": [
                {"label": "यवन: यूनानियों, रोमनों और पश्चिमी एशियाई लोगों के लिए प्रयुक्त सामूहिक शब्द", "type": "leaf"},
                {"label": "बंदरगाह शहरों में अलग बस्तियों (यवन चेरी) में निवास करते थे", "type": "leaf"}]},
            {"label": "सैन्य और तकनीकी भूमिका", "type": "branch", "date": "रोजगार", "children": [
                {"label": "क्रूर और लंबे यवनों को राजमहल के अंगरक्षक और रात्रि प्रहरी के रूप में नियुक्त किया गया", "type": "leaf"},
                {"label": "किला निर्माण, युद्ध यंत्रों और प्रकाशस्तंभों (लाइटहाउस) के निर्माण में वास्तुकार के रूप में कार्य", "type": "leaf"}]}
        ]
    },
    "trade-and-commerce-with-the-outside-world": {
        "en": [
            {"label": "Exports", "type": "branch", "date": "Outflow", "children": [
                {"label": "Pepper ('Black Gold' or Yavanapriya), Cardamom, Cinnamon", "type": "leaf"},
                {"label": "Korkai Pearls, Beryl, Muslin (fine cotton), Sandalwood, Ivory", "type": "leaf"}]},
            {"label": "Imports", "type": "branch", "date": "Inflow", "children": [
                {"label": "Gold and Silver coins (Roman coin hoards in Coimbatore & Madurai)", "type": "leaf"},
                {"label": "Italian wine (amphorae found), lead, copper, tin, glass", "type": "leaf"}]},
            {"label": "Major Ports", "type": "branch", "date": "Logistics", "children": [
                {"label": "Muziris & Tondi (West coast - Chera ports); Arikamedu (East coast - Poduke)", "type": "leaf"},
                {"label": "Kaveripattinam/Puhar (East coast - Chola port); Korkai (East coast - Pandya port)", "type": "leaf"}]},
            {"label": "Monsoon Discovery", "type": "branch", "date": "Hippalus", "children": [
                {"label": "Hippalus (45 CE) discovered monsoon winds, cutting voyage time to 40 days", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "निर्यात की वस्तुएं", "type": "branch", "date": "निर्यात", "children": [
                {"label": "काली मिर्च ('काला सोना' या यवनप्रिय), इलायची, दालचीनी", "type": "leaf"},
                {"label": "कोरकई के मोती, वैदूर्य (बेरिल), महीन सूती मलमल, चंदन, हाथी दांत", "type": "leaf"}]},
            {"label": "आयात की वस्तुएं", "type": "branch", "date": "आयात", "children": [
                {"label": "सोने और चांदी के सिक्के (कोयंबटूर और मदुरै में भारी मात्रा में रोमन खजाने मिले)", "type": "leaf"},
                {"label": "इतालवी शराब (एम्फोरा अवशेष), सीसा, तांबा, रांगा, काँच", "type": "leaf"}]},
            {"label": "प्रमुख बंदरगाह", "type": "branch", "date": "रसद", "children": [
                {"label": "मुज़िरिस और तोंडी (पश्चिमी तट - चेर); अरिकामेदु (पूर्वी तट - पोडुके)", "type": "leaf"},
                {"label": "कावेरीपट्टनम/पुहार (पूर्वी तट - चोल); कोरकई (पूर्वी तट - पाण्ड्य)", "type": "leaf"}]},
            {"label": "मानसून की खोज", "type": "branch", "date": "हिप्पलस", "children": [
                {"label": "हिप्पलस (45 ईस्वी) ने मानसूनी हवाओं की खोज की, जिससे समुद्री यात्रा मात्र 40 दिनों की रह गई", "type": "leaf"}]}
        ]
    },
    "art-and-architecture": {
        "en": [
            {"label": "Architecture", "type": "branch", "date": "Structures", "children": [
                {"label": "Used perishable materials (brick, timber, clay); no temples survived", "type": "leaf"},
                {"label": "Lighthouses (Sudar-yangu) built at Kaveripattinam to guide ships", "type": "leaf"}]},
            {"label": "Megaliths & Burials", "type": "branch", "date": "Archaeology", "children": [
                {"label": "Megalithic sites: Dolmens, cist burials, urn burials marked by stone circles", "type": "leaf"},
                {"label": "Adichanallur excavations yielded iron weapons, gold diadems, bronze bowls", "type": "leaf"}]},
            {"label": "Sculptural Art", "type": "branch", "date": "Arts", "children": [
                {"label": "Nadukal: Hero stones carved with warrior figures and eulogistic scripts", "type": "leaf"},
                {"label": "Terracotta art and clay toys were popular in urban households", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "वास्तुकला", "type": "branch", "date": "निर्माण", "children": [
                {"label": "नष्ट होने वाले माध्यमों (ईंट, लकड़ी, मिट्टी) का उपयोग; संगम काल के मंदिर अवशेष नहीं मिले", "type": "leaf"},
                {"label": "जहाजों के मार्गदर्शन हेतु कावेरीपट्टनम में ऊंचे प्रकाशस्तंभ (सुदर-इळंगु) निर्मित थे", "type": "leaf"}]},
            {"label": "महापाषाण और शवाधान", "type": "branch", "date": "पुरातत्व", "children": [
                {"label": "महापाषाण स्थल: पत्थरों से घिरे कलश शवाधान, सिस्ट और डोलमेन्स कब्रें", "type": "leaf"},
                {"label": "आदिचनल्लूर उत्खनन से लोहे के हथियार, सोने के मुकुट और कांस्य के कटोरे प्राप्त हुए", "type": "leaf"}]},
            {"label": "मूर्तिकला", "type": "branch", "date": "कला", "children": [
                {"label": "नडुगल: वीरगाथा पत्थर जिनपर सैनिक की छवि और यशोगान का संक्षिप्त आलेख खुदा था", "type": "leaf"},
                {"label": "शहरी घरों में पक्की मिट्टी (टेराकोटा) की मूर्तियाँ और मिट्टी के खिलौने लोकप्रिय थे", "type": "leaf"}]}
        ]
    }
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
    
    branches = MINDMAP_DATA.get(key, {}).get(lang, [])
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
