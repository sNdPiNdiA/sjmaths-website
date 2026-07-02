#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json, shutil

BASES = [
    r"upsc/ancient_history/Jainism",
    r"upsc/ancient_history/Buddhism",
    r"upsc/ancient_history/Jainism-and-Buddhism"
]

MINDMAP_DATA = {
    # ── JAINISM AND BUDDHISM COMMON ──
    "factors-responsible-for-their-advent": {
        "en": [
            {"label": "Socio-Economic", "type": "branch", "date": "Context", "children": [
                {"label": "Rigid Varna system dominated by Brahmanas", "type": "leaf"},
                {"label": "Agricultural transition required cattle preservation (opposed Vedic animal sacrifices)", "type": "leaf"},
                {"label": "Rise of Vaishyas (merchants) seeking status matching economic power", "type": "leaf"}]},
            {"label": "Religious-Cultural", "type": "branch", "date": "Context", "children": [
                {"label": "Extremely complex, expensive Vedic rituals & superstitions", "type": "leaf"},
                {"label": "Sanskrit was language of elites; masses wanted vernacular teachings", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सामाजिक-आर्थिक", "type": "branch", "date": "संदर्भ", "children": [
                {"label": "ब्राह्मणों के प्रभुत्व वाली कठोर वर्ण व्यवस्था से असंतोष", "type": "leaf"},
                {"label": "कृषि अर्थव्यवस्था में पशुधन संरक्षण की आवश्यकता (पशु बलि का विरोध)", "type": "leaf"},
                {"label": "वैश्यों (व्यापारियों) का उदय जो आर्थिक शक्ति के अनुसार सामाजिक सम्मान चाहते थे", "type": "leaf"}]},
            {"label": "धार्मिक-सांस्कृतिक", "type": "branch", "date": "संदर्भ", "children": [
                {"label": "अत्यंत जटिल, खर्चीले वैदिक कर्मकांड और अंधविश्वास", "type": "leaf"},
                {"label": "संस्कृत कुलीन वर्ग की भाषा थी; जनता जनभाषा में उपदेश चाहती थी", "type": "leaf"}]}
        ]
    },

    # ── JAINISM ──
    "birth-and-life-of-mahavira-540-468-bc": {
        "en": [
            {"label": "Early Life", "type": "branch", "date": "Birth", "children": [
                {"label": "Born 540 BCE at Kundagrama near Vaishali, Bihar", "type": "leaf"},
                {"label": "Father Siddhartha (Jnatrika Kshatriya clan), Mother Trishala (Lichchhavi princess)", "type": "leaf"},
                {"label": "Original name: Vardhamana; married Yashoda", "type": "leaf"}]},
            {"label": "Renunciation & Kevalya", "type": "branch", "date": "Spiritual", "children": [
                {"label": "Left home at age 30; wandered for 12 years", "type": "leaf"},
                {"label": "Attained Kevalya (supreme knowledge) under a Sal tree on Rijupalika river bank", "type": "leaf"},
                {"label": "Died 468 BCE at Pavapuri near Rajgir (age 72)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक जीवन", "type": "branch", "date": "जन्म", "children": [
                {"label": "540 ई.पू. में वैशाली (बिहार) के निकट कुंडग्राम में जन्म", "type": "leaf"},
                {"label": "पिता सिद्धार्थ (ज्ञातृक क्षत्रिय कुल), माता त्रिशला (लिच्छवि राजकुमारी)", "type": "leaf"},
                {"label": "मूल नाम: वर्धमान; यशोदा से विवाह हुआ", "type": "leaf"}]},
            {"label": "संन्यास और कैवल्य", "type": "branch", "date": "आध्यात्मिक", "children": [
                {"label": "30 वर्ष की आयु में गृहत्याग; 12 वर्षों तक कठोर तपस्या", "type": "leaf"},
                {"label": "ऋजुपालिका नदी के तट पर साल वृक्ष के नीचे कैवल्य (परम ज्ञान) प्राप्त किया", "type": "leaf"},
                {"label": "468 ई.पू. में पावापुरी (राजगीर के पास) में 72 वर्ष की आयु में निर्वाण", "type": "leaf"}]}
        ]
    },

    "tirthankaras-of-jainism": {
        "en": [
            {"label": "Origin", "type": "branch", "date": "Concept", "children": [
                {"label": "Jainism has 24 Tirthankaras (spiritual teachers)", "type": "leaf"},
                {"label": "First Tirthankara: Rishabhanatha (Symbol: Bull)", "type": "leaf"}]},
            {"label": "Later Teachers", "type": "branch", "date": "History", "children": [
                {"label": "23rd Tirthankara: Parshvanatha (Symbol: Serpent; lived in Varanasi)", "type": "leaf"},
                {"label": "24th Tirthankara: Vardhamana Mahavira (Symbol: Lion)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति", "type": "branch", "date": "अवधारणा", "children": [
                {"label": "जैन धर्म में 24 तीर्थंकर (आध्यात्मिक गुरु) हुए हैं", "type": "leaf"},
                {"label": "प्रथम तीर्थंकर: ऋषभनाथ (प्रतीक: बैल/वृषभ)", "type": "leaf"}]},
            {"label": "अंतिम गुरु", "type": "branch", "date": "इतिहास", "children": [
                {"label": "23वें तीर्थंकर: पार्श्वनाथ (प्रतीक: सर्प; वाराणसी के ऐतिहासिक पुरुष)", "type": "leaf"},
                {"label": "24वें तीर्थंकर: वर्धमान महावीर (प्रतीक: सिंह)", "type": "leaf"}]}
        ]
    },

    "teachings-of-mahavira": {
        "en": [
            {"label": "Core Beliefs", "type": "branch", "date": "Philosophies", "children": [
                {"label": "Rejected authority of Vedas and efficacy of Vedic rituals", "type": "leaf"},
                {"label": "Universe has two components: Jiva (soul) and Ajiva (matter)", "type": "leaf"},
                {"label": "Believed in Karma and reincarnation based on actions", "type": "leaf"}]},
            {"label": "Methodology", "type": "branch", "date": "Practice", "children": [
                {"label": "Advocated extreme asceticism and self-mortification", "type": "leaf"},
                {"label": "Ahimsa (non-injury) applied to all living & non-living entities", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य दर्शन", "type": "branch", "date": "सिद्धांत", "children": [
                {"label": "वेदों की सत्ता और यज्ञीय कर्मकांडों का पूर्ण विरोध किया", "type": "leaf"},
                {"label": "सृष्टि दो तत्वों से बनी है: जीव (चेतन) और अजीव (जड़)", "type": "leaf"},
                {"label": "कर्मवाद और पुनर्जन्म में विश्वास; कर्म बंधनों से मुक्ति ही मोक्ष है", "type": "leaf"}]},
            {"label": "साधना पद्धति", "type": "branch", "date": "अभ्यास", "children": [
                {"label": "कठोर तपस्या और कायाक्लेश (आत्म-पीड़न) पर अत्यधिक बल दिया", "type": "leaf"},
                {"label": "अहिंसा का अत्यंत सूक्ष्म पालन (सजीव और निर्जीव दोनों के प्रति)", "type": "leaf"}]}
        ]
    },

    "important-tenets-of-jainism": {
        "en": [
            {"label": "Philosophical Views", "type": "branch", "date": "Metaphysics", "children": [
                {"label": "Anekantavada: Theory of many-sidedness of reality & truth", "type": "leaf"},
                {"label": "Syadvada: All judgments are relative and conditional", "type": "leaf"},
                {"label": "Nayavada: Theory of partial viewpoints", "type": "leaf"}]},
            {"label": "God & Universe", "type": "branch", "date": "Cosmology", "children": [
                {"label": "Atheistic: Universe is eternal, runs on cosmic laws, not created by God", "type": "leaf"},
                {"label": "Equal potential of all souls to attain divinity (Siddha)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दार्शनिक दृष्टिकोण", "type": "branch", "date": "तत्वमीमांसा", "children": [
                {"label": "अनेकांतवाद: सत्य की बहुआयामी प्रकृति का सिद्धांत", "type": "leaf"},
                {"label": "स्यादवाद: सभी ज्ञान और निर्णय सापेक्ष होते हैं ('शायद' का सिद्धांत)", "type": "leaf"},
                {"label": "नयवाद: आंशिक सत्य या दृष्टिकोण का सिद्धांत", "type": "leaf"}]},
            {"label": "ईश्वर और ब्रह्मांड", "type": "branch", "date": "सृष्टि विज्ञान", "children": [
                {"label": "निरीश्वरवादी: ब्रह्मांड शाश्वत है, इसका कोई सृष्टिकर्ता ईश्वर नहीं है", "type": "leaf"},
                {"label": "सभी जीवों में देवत्व (सिद्ध अवस्था) प्राप्त करने की समान क्षमता", "type": "leaf"}]}
        ]
    },

    "five-doctrines-of-jainism": {
        "en": [
            {"label": "First Four (Parshvanatha)", "type": "branch", "date": "Pre-Mahavira", "children": [
                {"label": "Ahimsa: Non-violence (not hurting any living creature)", "type": "leaf"},
                {"label": "Satya: Truthfulness", "type": "leaf"},
                {"label": "Asteya: Non-stealing", "type": "leaf"},
                {"label": "Aparigraha: Non-possession / Non-attachment to wealth", "type": "leaf"}]},
            {"label": "Fifth Doctrine (Mahavira)", "type": "branch", "date": "Mahavira", "children": [
                {"label": "Brahmacharya: Celibacy / Chastity (added by Mahavira)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम चार व्रत (पार्श्वनाथ)", "type": "branch", "date": "महावीर-पूर्व", "children": [
                {"label": "अहिंसा: मन, वचन और कर्म से किसी जीव को कष्ट न देना", "type": "leaf"},
                {"label": "सत्य: सदा मधुर और सत्य बोलना", "type": "leaf"},
                {"label": "अस्तेय: चोरी न करना (बिना पूछे किसी की वस्तु न लेना)", "type": "leaf"},
                {"label": "अपरिग्रह: धन या भौतिक वस्तुओं का संग्रह न करना", "type": "leaf"}]},
            {"label": "पाँचवाँ व्रत (महावीर)", "type": "branch", "date": "महावीर", "children": [
                {"label": "ब्रह्मचर्य: इंद्रिय संयम और पवित्रता (महावीर द्वारा जोड़ा गया)", "type": "leaf"}]}
        ]
    },

    "three-jewels-of-jainism": {
        "en": [
            {"label": "The Path to Liberation", "type": "branch", "date": "Triratna", "children": [
                {"label": "Samyak Darshana: Right Faith (belief in Jain truths)", "type": "leaf"},
                {"label": "Samyak Jnana: Right Knowledge (unbiased understanding)", "type": "leaf"},
                {"label": "Samyak Charitra: Right Conduct (acting according to vows)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मोक्ष का मार्ग", "type": "branch", "date": "त्रिरत्न", "children": [
                {"label": "सम्यक दर्शन: जैन सिद्धांतों में सच्चा विश्वास और श्रद्धा", "type": "leaf"},
                {"label": "सम्यक ज्ञान: शंका रहित और वास्तविक ज्ञान की प्राप्ति", "type": "leaf"},
                {"label": "सम्यक चरित्र: पंच महाव्रतों के अनुसार आचरण करना", "type": "leaf"}]}
        ]
    },

    "organizational-setup-and-sects-of-jainism": {
        "en": [
            {"label": "Schism (1st Century CE)", "type": "branch", "date": "Division", "children": [
                {"label": "Digambaras (Sky-clad): Led by Bhadrabahu; absolute nudity, reject women attaining Moksha, strict rules", "type": "leaf"},
                {"label": "Shvetambaras (White-clad): Led by Sthulabhadra; white garments, accept women's liberation, moderate rules", "type": "leaf"}]},
            {"label": "Subsects", "type": "branch", "date": "Later Sects", "children": [
                {"label": "Terapanthis and Samaiyas (among Digambaras)", "type": "leaf"},
                {"label": "Sthanakvasi and Terapanth (non-image worshippers among Shvetambaras)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विभाजन (प्रथम शताब्दी ई.)", "type": "branch", "date": "संप्रदाय", "children": [
                {"label": "दिगंबर: भद्रबाहु के नेतृत्व में; नग्नता अनिवार्य, महिलाओं के सीधे मोक्ष का निषेध, कठोर नियम", "type": "leaf"},
                {"label": "श्वेतांबर: स्थूलभद्र के नेतृत्व में; श्वेत वस्त्र धारण, स्त्रियों के मोक्ष को स्वीकार करना, उदार नियम", "type": "leaf"}]},
            {"label": "उप-संप्रदाय", "type": "branch", "date": "परवर्ती विकास", "children": [
                {"label": "तेरापंथी और समैया (दिगंबरों में प्रमुख)", "type": "leaf"},
                {"label": "स्थानकवासी और तेरापंथ (श्वेतांबरों में मूर्ति पूजा विरोधी शाखाएँ)", "type": "leaf"}]}
        ]
    },

    "jain-councils": {
        "en": [
            {"label": "First Council", "type": "branch", "date": "300 BCE", "children": [
                {"label": "Held at Pataliputra, Bihar; presided by Sthulabhadra", "type": "leaf"},
                {"label": "Resulted in compilation of 12 Angas", "type": "leaf"}]},
            {"label": "Second Council", "type": "branch", "date": "512 CE", "children": [
                {"label": "Held at Vallabhi, Gujarat; presided by Devardhi Kshamashramana", "type": "leaf"},
                {"label": "Final collection & written codification of Shvetambara Agamas", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम बौद्ध/जैन संगीति", "type": "branch", "date": "300 ई.पू.", "children": [
                {"label": "पाटलिपुत्र (बिहार) में आयोजित; स्थूलभद्र की अध्यक्षता में", "type": "leaf"},
                {"label": "परिणाम: जैन धर्म के 12 अंगों का संकलन हुआ", "type": "leaf"}]},
            {"label": "द्वितीय संगीति", "type": "branch", "date": "512 ई.", "children": [
                {"label": "वल्लभी (गुजरात) में आयोजित; देवर्धि क्षमाश्रमण की अध्यक्षता में", "type": "leaf"},
                {"label": "परिणाम: श्वेतांबर जैन आगमों का अंतिम रूप से लेखन और संहिताकरण", "type": "leaf"}]}
        ]
    },

    "literature-of-jainism": {
        "en": [
            {"label": "Agamas (Canonical)", "type": "branch", "date": "Texts", "children": [
                {"label": "Written in Ardhamagadhi Prakrit language", "type": "leaf"},
                {"label": "Includes 12 Angas, 12 Upangas, 10 Prakirnas, 6 Chedasutras", "type": "leaf"}]},
            {"label": "Non-Canonical Texts", "type": "branch", "date": "Texts", "children": [
                {"label": "Bhadrabahu Charita: Story of Chandragupta Maurya & Bhadrabahu", "type": "leaf"},
                {"label": "Parishishtaparvan by Hemachandra: History of Jain monks", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आगम साहित्य (प्रामाणिक)", "type": "branch", "date": "ग्रंथ", "children": [
                {"label": "अर्धमागधी प्राकृत भाषा में लिखे गए मूल धर्मग्रंथ", "type": "leaf"},
                {"label": "इसके अंतर्गत 12 अंग, 12 उपांग, 10 प्रकीर्ण और 6 छेदसूत्र शामिल हैं", "type": "leaf"}]},
            {"label": "गैर-आगम साहित्य", "type": "branch", "date": "ग्रंथ", "children": [
                {"label": "भद्रबाहु चरित: चंद्रगुप्त मौर्य और भद्रबाहु के दक्षिण प्रवास का विवरण", "type": "leaf"},
                {"label": "हेमचंद्र द्वारा रचित परिशिष्टपर्वन्: शलाका पुरुषों का इतिहास", "type": "leaf"}]}
        ]
    },

    "jain-architecture": {
        "en": [
            {"label": "Cave Architecture", "type": "branch", "date": "Structures", "children": [
                {"label": "Udayagiri and Khandagiri Caves near Bhubaneswar (Kharavela patronage)", "type": "leaf"},
                {"label": "Ellora Caves (Jain section, Maharashtra)", "type": "leaf"}]},
            {"label": "Temples & Statues", "type": "branch", "date": "Structures", "children": [
                {"label": "Dilwara Jain Temples at Mt. Abu, Rajasthan (White marble)", "type": "leaf"},
                {"label": "Bahubali/Gomateshwara Monolithic Statue at Shravanabelagola, Karnataka (Chamundaraya)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "गुफा वास्तुकला", "type": "branch", "date": "संरचनाएं", "children": [
                {"label": "उदयगिरि और खंडगिरि गुफाएं, ओडिशा (कलिंग नरेश खारवेल का संरक्षण)", "type": "leaf"},
                {"label": "एलोरा गुफाएं (महाराष्ट्र में जैन धर्म से संबंधित गुफा समूह)", "type": "leaf"}]},
            {"label": "मंदिर और प्रतिमाएं", "type": "branch", "date": "संरचनाएं", "children": [
                {"label": "दिलवाड़ा जैन मंदिर, माउंट आबू (सफेद संगमरमर का बेहतरीन कार्य)", "type": "leaf"},
                {"label": "श्रवणबेलगोला (कर्नाटक) में गोमतेश्वर/बाहुबली की विशाल अखंड प्रतिमा", "type": "leaf"}]}
        ]
    },

    "associated-terminology": {
        "en": [
            {"label": "Spiritual States", "type": "branch", "date": "Terms", "children": [
                {"label": "Kevalin: Perfect soul who has achieved Kevalya", "type": "leaf"},
                {"label": "Tirthankara: Ford-maker across the ocean of rebirth", "type": "leaf"},
                {"label": "Sallekhana / Santhara: Fasting unto death (ritual exit)", "type": "leaf"}]},
            {"label": "Ethics & Soul", "type": "branch", "date": "Terms", "children": [
                {"label": "Pudgala: Karmic matter which binds the soul", "type": "leaf"},
                {"label": "Jina: Spiritual conqueror who defeated passions", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आध्यात्मिक अवस्थाएं", "type": "branch", "date": "शब्दावली", "children": [
                {"label": "केवलिन: सर्वोच्च ज्ञान (कैवल्य) प्राप्त मुक्त आत्मा", "type": "leaf"},
                {"label": "तीर्थंकर: संसार सागर पार कराने वाले आध्यात्मिक पथ-प्रदर्शक", "type": "leaf"},
                {"label": "सल्लेखना / संथारा: मोक्ष प्राप्ति हेतु मौन व्रत रख उपवास द्वारा प्राण त्यागना", "type": "leaf"}]},
            {"label": "नीति और आत्मा", "type": "branch", "date": "शब्दावली", "children": [
                {"label": "पुद्गल: अजीव या जड़ पदार्थ जो कर्म बंधनों का कारण है", "type": "leaf"},
                {"label": "जिन: इंद्रियों और राग-द्वेष पर विजय पाने वाला विजेता", "type": "leaf"}]}
        ]
    },

    "overall-contribution": {
        "en": [
            {"label": "Language & Literature", "type": "branch", "date": "Impact", "children": [
                {"label": "Enriched regional languages (Prakrit, early Kannada, Tamil)", "type": "leaf"},
                {"label": "Introduced dynamic systems of logic (Anekantavada)", "type": "leaf"}]},
            {"label": "Socio-Political", "type": "branch", "date": "Impact", "children": [
                {"label": "Strict non-violence influenced vegetarianism & modern leaders like Mahatma Gandhi", "type": "leaf"},
                {"label": "Boosted trade and commerce (as agriculture was avoided due to Ahimsa)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "भाषा और साहित्य", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "क्षेत्रीय भाषाओं (प्राकृत, प्रारंभिक कन्नड़, तमिल) का विकास किया", "type": "leaf"},
                {"label": "तर्कशास्त्र में नए सिद्धांतों (अनेकांतवाद और स्यादवाद) का योगदान", "type": "leaf"}]},
            {"label": "सामाजिक-राजनीतिक", "type": "branch", "date": "प्रभाव", "children": [
                {"label": "अहिंसा के कठोर सिद्धांत ने शाकाहार और महात्मा गांधी को प्रभावित किया", "type": "leaf"},
                {"label": "व्यापार और वाणिज्य को बढ़ावा मिला (कृषि में जीव हत्या के भय से व्यापार अपनाया)", "type": "leaf"}]}
        ]
    },

    # ── BUDDHISM ──
    "birth-and-life-of-buddha-563-483-bc-great-events": {
        "en": [
            {"label": "Early Life", "type": "branch", "date": "Birth", "children": [
                {"label": "Born 563 BCE at Lumbini (Nepal); named Siddhartha Shakya", "type": "leaf"},
                {"label": "Father Shuddhodana (Kapilavastu Shakya King), Mother Mahamaya", "type": "leaf"},
                {"label": "Left home at age 29 (Mahabhinishkramana) after seeing Four Sights", "type": "leaf"}]},
            {"label": "Enlightenment & Death", "type": "branch", "date": "Events", "children": [
                {"label": "Nirvana: At age 35 under Bodhi tree in Bodh Gaya on Nilanjan river bank", "type": "leaf"},
                {"label": "Dharmachakrapravartana: First Sermon at Sarnath to 5 disciples", "type": "leaf"},
                {"label": "Mahaparinirvana: Passed away 483 BCE at Kushinagar (age 80)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक जीवन", "type": "branch", "date": "जन्म", "children": [
                {"label": "563 ई.पू. में लुंबिनी (नेपाल) में जन्म; मूल नाम: सिद्धार्थ", "type": "leaf"},
                {"label": "पिता शुद्धोधन (शाक्य गणराज्य प्रमुख), माता महामाया (कोलिय वंश)", "type": "leaf"},
                {"label": "चार दृश्यों को देखकर 29 वर्ष की आयु में गृहत्याग (महाभिनिष्क्रमण)", "type": "leaf"}]},
            {"label": "ज्ञान और महापरिनिर्वाण", "type": "branch", "date": "घटनाएं", "children": [
                {"label": "निर्वाण: 35 वर्ष की आयु में बोधगया में पीपल वृक्ष के नीचे ज्ञान की प्राप्ति", "type": "leaf"},
                {"label": "धर्मचक्रप्रवर्तन: सारनाथ (ऋषिपत्तन) में 5 भिक्षुओं को प्रथम उपदेश", "type": "leaf"},
                {"label": "महापरिनिर्वाण: 483 ई.पू. में कुशीनगर (मल्ल राज्य) में 80 वर्ष की आयु में देहत्याग", "type": "leaf"}]}
        ]
    },

    "teachings-of-buddha": {
        "en": [
            {"label": "Philosophies", "type": "branch", "date": "Principles", "children": [
                {"label": "Madhyama Pratipada: Middle Path between extreme asceticism & luxury", "type": "leaf"},
                {"label": "Anatta & Anicca: Impermanence of world; non-existence of soul", "type": "leaf"},
                {"label": "Pratityasamutpada: Law of Dependent Origination (Cause and effect)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दार्शनिक सिद्धांत", "type": "branch", "date": "धम्म", "children": [
                {"label": "मध्यम प्रतिपदा: अत्यधिक विलासिता और कठोर तपस्या के बीच का मध्यम मार्ग", "type": "leaf"},
                {"label": "अनात्मवाद और अनित्यवाद: संसार क्षणभंगुर है; आत्मा जैसी कोई शाश्वत सत्ता नहीं", "type": "leaf"},
                {"label": "प्रतीत्यसमुत्पाद: 'इसके होने से यह होता है' (कारण-कार्य का सिद्धांत)", "type": "leaf"}]}
        ]
    },

    "3-jewels-buddhism": {
        "en": [
            {"label": "Triratna", "type": "branch", "date": "Foundations", "children": [
                {"label": "Buddha: The Enlightened One / Teacher", "type": "leaf"},
                {"label": "Dhamma: The Teachings / Cosmic Law", "type": "leaf"},
                {"label": "Sangha: The Monastic Order of monks and nuns", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "त्रिरत्न", "type": "branch", "date": "आधार", "children": [
                {"label": "बुद्ध: जागृत या प्रबुद्ध मार्गदर्शक (शिक्षक)", "type": "leaf"},
                {"label": "धम्म: बुद्ध के नैतिक उपदेश और सिद्धांत (नियम)", "type": "leaf"},
                {"label": "संघ: भिक्षुओं और भिक्षुणियों का अनुशासित समुदाय", "type": "leaf"}]}
        ]
    },

    "4-noble-truths-buddhism": {
        "en": [
            {"label": "Arya Satyani", "type": "branch", "date": "Truths", "children": [
                {"label": "Dukkha: Life is full of suffering (every phase brings sorrow)", "type": "leaf"},
                {"label": "Dukkha Samudaya: Desire (Tanha) is the root cause of suffering", "type": "leaf"},
                {"label": "Dukkha Nirodha: Suffering ceases when desire is eliminated", "type": "leaf"},
                {"label": "Dukkha Nirodha Gamini Pratipada: The path (Eightfold Path) leading to end of suffering", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "चार आर्य सत्य", "type": "branch", "date": "सत्य", "children": [
                {"label": "दुख: संसार दुखमय है (जन्म, बुढ़ापा, मृत्यु सब दुख के रूप हैं)", "type": "leaf"},
                {"label": "दुख समुदाय: तृष्णा (लालसा/कामना) ही दुखों का मूल कारण है", "type": "leaf"},
                {"label": "दुख निरोध: तृष्णा का सर्वथा त्याग करने से दुख का अंत संभव है", "type": "leaf"},
                {"label": "दुख निरोध मार्ग: अष्टांगिक मार्ग पर चलकर दुखों से मुक्ति पाई जा सकती है", "type": "leaf"}]}
        ]
    },

    "5-principles-buddhism": {
        "en": [
            {"label": "Panchasheela", "type": "branch", "date": "Ethics", "children": [
                {"label": "Avoid killing / harm to living beings", "type": "leaf"},
                {"label": "Avoid stealing (taking what is not given)", "type": "leaf"},
                {"label": "Avoid sexual misconduct / adultery", "type": "leaf"},
                {"label": "Avoid false speech / lying", "type": "leaf"},
                {"label": "Avoid taking fermented and distilled intoxicants", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पंचशील", "type": "branch", "date": "नैतिकता", "children": [
                {"label": "प्राणातिपात विरति: जीव हत्या से दूर रहना (अहिंसा)", "type": "leaf"},
                {"label": "अदत्तादान विरति: चोरी न करना (बिना दी हुई वस्तु न लेना)", "type": "leaf"},
                {"label": "काममिथ्याचार विरति: व्यभिचार या अनुचित आचरण न करना", "type": "leaf"},
                {"label": "मृषावाद विरति: झूठ बोलने और कड़वा बोलने से बचना", "type": "leaf"},
                {"label": "सुरामेरय मज्जप्पमादट्ठाना विरति: मदिरा और नशीले द्रव्यों से दूर रहना", "type": "leaf"}]}
        ]
    },

    "8-fold-path-buddhism": {
        "en": [
            {"label": "Pragya (Wisdom)", "type": "branch", "date": "Steps", "children": [
                {"label": "Right Understanding (Samyak Drishti)", "type": "leaf"},
                {"label": "Right Resolve/Intention (Samyak Sankalpa)", "type": "leaf"}]},
            {"label": "Sheela (Conduct)", "type": "branch", "date": "Steps", "children": [
                {"label": "Right Speech (Samyak Vak)", "type": "leaf"},
                {"label": "Right Action (Samyak Karmanta)", "type": "leaf"},
                {"label": "Right Livelihood (Samyak Ajiva)", "type": "leaf"}]},
            {"label": "Samadhi (Meditation)", "type": "branch", "date": "Steps", "children": [
                {"label": "Right Effort (Samyak Vyayama)", "type": "leaf"},
                {"label": "Right Mindfulness (Samyak Smriti)", "type": "leaf"},
                {"label": "Right Concentration (Samyak Samadhi)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रज्ञा (ज्ञान)", "type": "branch", "date": "चरण", "children": [
                {"label": "सम्यक दृष्टि: चार आर्य सत्यों की सही समझ", "type": "leaf"},
                {"label": "सम्यक संकल्प: वासना, क्रोध और हिंसा से दूर रहने का संकल्प", "type": "leaf"}]},
            {"label": "शील (आचरण)", "type": "branch", "date": "चरण", "children": [
                {"label": "सम्यक वाक: सदा सत्य, प्रिय और कल्याणकारी बोलना", "type": "leaf"},
                {"label": "सम्यक कर्मांत: अहिंसक और नैतिक कर्म करना", "type": "leaf"},
                {"label": "सम्यक आजीव: ईमानदारी और धर्मपूर्ण आजीविका कमाना", "type": "leaf"}]},
            {"label": "समाधि (एकाग्रता)", "type": "branch", "date": "चरण", "children": [
                {"label": "सम्यक व्यायाम: मन में अच्छे विचारों को लाने का प्रयत्न करना", "type": "leaf"},
                {"label": "सम्यक स्मृति: सचेत रहकर सम्यक जागरूकता बनाए रखना", "type": "leaf"},
                {"label": "सम्यक समाधि: चित्त की एकाग्रता और ध्यान साधना", "type": "leaf"}]}
        ]
    },

    "concept-of-bodhisattvas": {
        "en": [
            {"label": "Key Bodhisattvas", "type": "branch", "date": "Mahayana", "children": [
                {"label": "Avalokiteshvara: Lord of Compassion; holds lotus (Padmapani)", "type": "leaf"},
                {"label": "Maitreya: The Future Buddha who will descend to earth", "type": "leaf"},
                {"label": "Manjushri: Personification of wisdom; holds sword", "type": "leaf"},
                {"label": "Vajrapani: Wielder of thunderbolt; represents power", "type": "leaf"},
                {"label": "Amitabha: Buddha of Infinite Light; resides in pure land", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख बोधिसत्व", "type": "branch", "date": "महायान", "children": [
                {"label": "अवलोकितेश्वर: परम करुणा के सागर; हाथ में कमल (पद्मपाणि) लिए हुए", "type": "leaf"},
                {"label": "मैत्रेय: भविष्य के बुद्ध जो पृथ्वी पर अवतरित होंगे", "type": "leaf"},
                {"label": "मंजुश्री: बुद्धि और ज्ञान के प्रतीक; हाथ में चमकती तलवार लिए हुए", "type": "leaf"},
                {"label": "वज्रपाणि: वज्र धारण करने वाले रक्षक; बुद्ध की शक्ति के प्रतीक", "type": "leaf"},
                {"label": "अमिताभ: असीम प्रकाश के बुद्ध; सुखवती (स्वर्ग) के अधिपति", "type": "leaf"}]}
        ]
    },

    "organisation-sangha-and-sects-of-buddhism": {
        "en": [
            {"label": "The Sangha", "type": "branch", "date": "Order", "children": [
                {"label": "Democratic assembly; strict rules codifed in Vinaya Pitaka", "type": "leaf"},
                {"label": "Fortnightly meeting of Uposatha for confession of sins", "type": "leaf"}]},
            {"label": "Major Sects", "type": "branch", "date": "Sects", "children": [
                {"label": "Hinayana (Theravada): Orthodox, believe in self-effort, no idol worship, Pali language", "type": "leaf"},
                {"label": "Mahayana: Progressive, deified Buddha, icon worship, Sanskrit language, believe in Bodhisattvas", "type": "leaf"},
                {"label": "Vajrayana: Tantric form; magical practices, female deities (Tara), centered in Eastern India", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "बौद्ध संघ व्यवस्था", "type": "branch", "date": "संगठन", "children": [
                {"label": "लोकतांत्रिक सभा प्रणाली; नियम विनय पिटक में संकलित हैं", "type": "leaf"},
                {"label": "पाक्षिक उपोसथ सभा जिसमें भिक्षु अपने अपराध स्वीकार करते थे", "type": "leaf"}]},
            {"label": "प्रमुख संप्रदाय", "type": "branch", "date": "शाखाएँ", "children": [
                {"label": "हीनयान (थेरवाद): रूढ़िवादी, बुद्ध को महापुरुष मानते हैं, मूर्ति पूजा नहीं, पाली ग्रंथ", "type": "leaf"},
                {"label": "महायान: प्रगतिशील, बुद्ध को ईश्वर मानकर मूर्ति पूजा, संस्कृत ग्रंथ, बोधिसत्व में आस्था", "type": "leaf"},
                {"label": "वज्रयान: तांत्रिक बौद्ध शाखा; मंत्र-तंत्र और तारा देवी की पूजा, पूर्वी भारत में उदय", "type": "leaf"}]}
        ]
    },

    "buddhist-councils": {
        "en": [
            {"label": "First & Second", "type": "branch", "date": "Councils", "children": [
                {"label": "1st Council: 483 BCE Rajgir (Ajatashatru patronage; led by Mahakassapa; compiled Sutta & Vinaya)", "type": "leaf"},
                {"label": "2nd Council: 383 BCE Vaishali (Kalasoka patronage; Sabakami presiding; first split of Sangha)", "type": "leaf"}]},
            {"label": "Third & Fourth", "type": "branch", "date": "Councils", "children": [
                {"label": "3rd Council: 250 BCE Pataliputra (Ashoka patronage; Moggaliputta Tissa; Abhidhamma compiled)", "type": "leaf"},
                {"label": "4th Council: 72 CE Kashmir (Kanishka patronage; Vasumitra presiding; Hinayana & Mahayana split)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम और द्वितीय संगीति", "type": "branch", "date": "संगीति", "children": [
                {"label": "प्रथम: 483 ई.पू. राजगृह (अजातशत्रु का संरक्षण; महाकश्यप अध्यक्ष; सुत्त और विनय संकलन)", "type": "leaf"},
                {"label": "द्वितीय: 383 ई.पू. वैशाली (कालाशोक का संरक्षण; साबाकामी अध्यक्ष; संघ में पहला मतभेद)", "type": "leaf"}]},
            {"label": "तृतीय और चतुर्थ संगीति", "type": "branch", "date": "संगीति", "children": [
                {"label": "तृतीय: 250 ई.पू. पाटलिपुत्र (अशोक का संरक्षण; मोग्गलिपुत्त तिस्स अध्यक्ष; अभिधम्म संकलन)", "type": "leaf"},
                {"label": "चतुर्थ: 72 ई. कश्मीर (कनिष्क का संरक्षण; वसुमित्र अध्यक्ष; हीनयान और महायान का विभाजन)", "type": "leaf"}]}
        ]
    },

    "spread-of-buddhism-and-royal-patronage": {
        "en": [
            {"label": "Internal & External", "type": "branch", "date": "Expansion", "children": [
                {"label": "Ashoka made it state religion; sent Mahinda & Sanghamitta to Sri Lanka", "type": "leaf"},
                {"label": "Kanishka popularized Mahayana across Central Asia and China", "type": "leaf"},
                {"label": "Pala kings of Bengal patronized Vajrayana; funded Vikramashila university", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आंतरिक और बाह्य प्रसार", "type": "branch", "date": "विस्तार", "children": [
                {"label": "अशोक ने इसे राजधर्म बनाया; श्रीलंका में महिंदा और संघमित्रा को भेजा", "type": "leaf"},
                {"label": "कनिष्क ने मध्य एशिया और चीन में महायान संप्रदाय को लोकप्रिय बनाया", "type": "leaf"},
                {"label": "बंगाल के पाल शासकों ने वज्रयान को संरक्षण दिया; विक्रमशिला विश्वविद्यालय की स्थापना", "type": "leaf"}]}
        ]
    },

    "literary-sources-of-buddhism": {
        "en": [
            {"label": "Pali Canon", "type": "branch", "date": "Tripitaka", "children": [
                {"label": "Sutta Pitaka: Buddha's discourses on Dhamma", "type": "leaf"},
                {"label": "Vinaya Pitaka: Monastic discipline & codes of conduct", "type": "leaf"},
                {"label": "Abhidhamma Pitaka: Philosophical analysis of teachings", "type": "leaf"}]},
            {"label": "Non-Canonical Pali/Sanskrit", "type": "branch", "date": "Later Texts", "children": [
                {"label": "Milinda Panha: Dialogues between Greek King Menander & Sage Nagasena", "type": "leaf"},
                {"label": "Buddhacharita: Sanskrit epic biography of Buddha by Ashvaghosha", "type": "leaf"},
                {"label": "Lalitavistara and Divyavadana: Mahayana Sanskrit texts", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पाली तिपिटक (मूल)", "type": "branch", "date": "त्रिपिटक", "children": [
                {"label": "सुत्त पिटक: बुद्ध के नैतिक प्रवचन और उपदेशों का संग्रह", "type": "leaf"},
                {"label": "विनय पिटक: बौद्ध संघ के अनुशासन और आचरण के नियम", "type": "leaf"},
                {"label": "अभिधम्म पिटक: बौद्ध दर्शन और सिद्धांतों का दार्शनिक विश्लेषण", "type": "leaf"}]},
            {"label": "अनुपिटक और संस्कृत साहित्य", "type": "branch", "date": "परवर्ती ग्रंथ", "children": [
                {"label": "मिलिंदपन्ह: यूनानी राजा मिनेंडर और बौद्ध भिक्षु नागसेन का संवाद", "type": "leaf"},
                {"label": "बुद्धचरित: अश्वघोष द्वारा संस्कृत भाषा में लिखित बुद्ध की महाकाव्यात्मक जीवनी", "type": "leaf"},
                {"label": "ललितविस्तर और दिव्यावदान: महायान शाखा के संस्कृत ग्रंथ", "type": "leaf"}]}
        ]
    },

    "3-pittakas": {
        "en": [
            {"label": "Sutta Pitaka", "type": "branch", "date": "Discourses", "children": [
                {"label": "Divided into 5 Nikayas (Digha, Majjhima, Samyutta, Anguttara, Khuddaka)", "type": "leaf"},
                {"label": "Includes Dhammapada and Jataka tales", "type": "leaf"}]},
            {"label": "Vinaya & Abhidhamma", "type": "branch", "date": "Rules & Philosophy", "children": [
                {"label": "Vinaya contains Suttavibhanga, Khandhaka, and Parivara", "type": "leaf"},
                {"label": "Abhidhamma is written in question-answer catechism format", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सुत्त पिटक", "type": "branch", "date": "प्रवचन", "children": [
                {"label": "5 निकायों में विभाजित (दीघ, मज्झिम, संयुत्त, अंगुत्तर, खुद्दक निकाय)", "type": "leaf"},
                {"label": "इसी के अंतर्गत धम्मपद और जातक कथाएं शामिल हैं", "type": "leaf"}]},
            {"label": "विनय और अभिधम्म पिटक", "type": "branch", "date": "नियम और दर्शन", "children": [
                {"label": "विनय पिटक में सुत्तविभंग, खंधक और परिवार शामिल हैं", "type": "leaf"},
                {"label": "अभिधम्म पिटक प्रश्नोत्तर शैली और दार्शनिक रूप में लिखा गया है", "type": "leaf"}]}
        ]
    },

    "causes-for-the-decline-buddhism": {
        "en": [
            {"label": "Internal Decay", "type": "branch", "date": "Decline", "children": [
                {"label": "Degeneration of Buddhist Sangha; corruption and accumulation of wealth", "type": "leaf"},
                {"label": "Vajrayana tantric practices alienated common masses", "type": "leaf"}]},
            {"label": "External Factors", "type": "branch", "date": "Decline", "children": [
                {"label": "Revival of Brahmanical Hinduism (Adi Shankara, Bhakti movement)", "type": "leaf"},
                {"label": "Destruction of monastic universities (Nalanda) by Bakhtiyar Khilji's invasion", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आंतरिक गिरावट", "type": "branch", "date": "पतन", "children": [
                {"label": "बौद्ध संघों का नैतिक पतन; विलासिता और अत्यधिक धन संचय", "type": "leaf"},
                {"label": "वज्रयान की तांत्रिक क्रियाओं से आम जनता का धर्म से विमुख होना", "type": "leaf"}]},
            {"label": "बाह्य कारक", "type": "branch", "date": "पतन", "children": [
                {"label": "ब्राह्मणवादी हिंदू धर्म का पुनरुत्थान (आदि शंकराचार्य का प्रचार, भक्ति आंदोलन)", "type": "leaf"},
                {"label": "बख्तियार खिलजी के आक्रमण से नालंदा, विक्रमशिला जैसे विश्वविद्यालयों का विनाश", "type": "leaf"}]}
        ]
    },

    "overall-contribution-of-buddhism": {
        "en": [
            {"label": "Social & Education", "type": "branch", "date": "Legacy", "children": [
                {"label": "Strong critique of caste system; promoted social equality", "type": "leaf"},
                {"label": "Led to residential universities (Nalanda, Taxila, Odantapuri)", "type": "leaf"}]},
            {"label": "Art, Architecture & Global", "type": "branch", "date": "Legacy", "children": [
                {"label": "Introduced Stupas (Sanchi), rock-cut caves (Ajanta, Karle), Viharas & Chaityas", "type": "leaf"},
                {"label": "Gandhara and Mathura school of art created iconic representations of Buddha", "type": "leaf"},
                {"label": "Globalized Indian culture across Central Asia, East Asia, and SE Asia", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सामाजिक और शैक्षणिक योगदान", "type": "branch", "date": "धरोहर", "children": [
                {"label": "जाति व्यवस्था की कड़ी आलोचना; सामाजिक समानता का प्रचार", "type": "leaf"},
                {"label": "विश्व प्रसिद्ध आवासीय विश्वविद्यालयों (नालंदा, तक्षशिला, ओदंतपुरी) की स्थापना", "type": "leaf"}]},
            {"label": "कला, वास्तुकला और वैश्विक प्रभाव", "type": "branch", "date": "धरोहर", "children": [
                {"label": "स्तूपों (सांची), शैलकृत गुफाओं (अजंता, कार्ला), विहारों और चैत्यों का निर्माण", "type": "leaf"},
                {"label": "गांधार और मथुरा कला शैलियों में बुद्ध की सुंदर मूर्तियों का निर्माण", "type": "leaf"},
                {"label": "मध्य एशिया, पूर्वी एशिया और दक्षिण-पूर्व एशिया में भारतीय संस्कृति का विस्तार", "type": "leaf"}]}
        ]
    }
}

# Add fallback mappings for variations of folder names
MINDMAP_MAPPINGS = {
    # Jainism
    "associated-terminology": "associated-terminology",
    "birth-and-life-of-mahavira": "birth-and-life-of-mahavira-540-468-bc",
    "birth-and-life-of-mahavira-540-468-bc": "birth-and-life-of-mahavira-540-468-bc",
    "five-doctrines-of-jainism": "five-doctrines-of-jainism",
    "important-tenets-of-jainism": "important-tenets-of-jainism",
    "jain-architecture": "jain-architecture",
    "jain-councils": "jain-councils",
    "literature-of-jainism": "literature-of-jainism",
    "organizational-setup-and-sects-of-jainism": "organizational-setup-and-sects-of-jainism",
    "overall-contribution": "overall-contribution",
    "teachings-of-mahavira": "teachings-of-mahavira",
    "three-jewels-of-jainism": "three-jewels-of-jainism",
    "tirthankaras-of-jainism": "tirthankaras-of-jainism",

    # Buddhism
    "3-jewels-buddhism": "3-jewels-buddhism",
    "3-jewels": "3-jewels-buddhism",
    "3-pittakas": "3-pittakas",
    "4-noble-truths-buddhism": "4-noble-truths-buddhism",
    "4-noble-truths": "4-noble-truths-buddhism",
    "5-principles-buddhism": "5-principles-buddhism",
    "5-principles": "5-principles-buddhism",
    "8-fold-path-buddhism": "8-fold-path-buddhism",
    "8-fold-path": "8-fold-path-buddhism",
    "birth-and-life-of-buddha": "birth-and-life-of-buddha-563-483-bc-great-events",
    "great-events": "birth-and-life-of-buddha-563-483-bc-great-events",
    "birth-and-life-of-buddha-563-483-bc-great-events": "birth-and-life-of-buddha-563-483-bc-great-events",
    "birth-and-life-of-buddha-great-events": "birth-and-life-of-buddha-563-483-bc-great-events",
    "buddhist-councils": "buddhist-councils",
    "causes-for-the-decline": "causes-for-the-decline-buddhism",
    "causes-for-the-decline-buddhism": "causes-for-the-decline-buddhism",
    "concept-of-bodhisattvas": "concept-of-bodhisattvas",
    "literary-sources-of-buddhism": "literary-sources-of-buddhism",
    "organisation-sangha-and-sects-of-buddhism": "organisation-sangha-and-sects-of-buddhism",
    "overall-contribution-of-buddhism": "overall-contribution-of-buddhism",
    "spread-of-buddhism-and-royal-patronage": "spread-of-buddhism-and-royal-patronage",
    "teachings-of-buddha": "teachings-of-buddha",

    # Common
    "factors-responsible-for-their-advent": "factors-responsible-for-their-advent"
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

    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    
    # Map variation keys to canonical keys
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, key)
    
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
    
    for base in BASES:
        if not os.path.exists(base):
            continue

        for root_dir, dirs, files in os.walk(base):
            dirs[:] = [d for d in dirs if d != 'hi']
            folder_name = os.path.basename(root_dir)
            
            if root_dir == base:
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
