#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Second-Phase-of-British-Expansion-In-India"

MINDMAP_DATA = {
    "2-anglo-sikh-wars": {
        "en": [
            {"label": "First Anglo-Sikh War (1845-46)", "type": "branch", "date": "1845-1846", "children": [
                {"label": "Triggered by Sikh army crossing Sutlej; EIC had been positioning troops since Ranjit Singh's death (1839)", "type": "leaf"},
                {"label": "Key battles: Mudki (Dec 1845), Ferozeshah (Dec 1845), Aliwal (Jan 1846), Sobraon (Feb 1846) — all decisive EIC victories", "type": "leaf"},
                {"label": "Treaty of Lahore (1846): Sikhs ceded Jalandhar Doab, paid Rs 1.5 cr indemnity; Maharaja Dalip Singh made ruler under British Resident", "type": "leaf"},
                {"label": "Treaty of Bhairowal (Dec 1846): Eight Sikh chiefs formed Council of Regency; Henry Lawrence as Resident with supreme authority", "type": "leaf"}
            ]},
            {"label": "Second Anglo-Sikh War (1848-49)", "type": "branch", "date": "1848-1849", "children": [
                {"label": "Sparked by Multan revolt (Diwan Mulraj) and Hazara revolt (Chattar Singh Atariwala); Sikh army joined rebels", "type": "leaf"},
                {"label": "Key battles: Ramnagar (Nov 1848), Chillianwala (Jan 1849 — British tactical defeat), Gujrat (Feb 1849 — decisive British win)", "type": "leaf"},
                {"label": "Lord Dalhousie annexed Punjab in March 1849; Dalip Singh pensioned off to England; Koh-i-Noor diamond seized", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1849", "children": [
                {"label": "Annexation of Punjab was the last major territorial expansion of British India — completed the subcontinent's conquest", "type": "leaf"},
                {"label": "Punjab Board of Administration (John Lawrence, Henry Lawrence, Mansel) created highly efficient direct administration", "type": "leaf"},
                {"label": "Sikh soldiers actively recruited into British Indian Army post-1857 as 'martial race' — legacy of Punjab conquest", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रथम आंग्ल-सिख युद्ध (1845-46)", "type": "branch", "date": "1845-1846", "children": [
                {"label": "सिख सेना द्वारा सतलज नदी पार करने से उत्प्रेरित; रणजीत सिंह की मृत्यु (1839) के बाद से EIC ने सैनिक तैनात करने शुरू किए थे", "type": "leaf"},
                {"label": "मुख्य युद्ध: मुदकी (दिसं. 1845), फिरोजशाह (दिसं. 1845), अलीवाल (जन. 1846), सोब्राओं (फर. 1846) — सभी EIC की निर्णायक जीत", "type": "leaf"},
                {"label": "लाहौर संधि (1846): सिखों ने जालंधर दोआब सौंपा, 1.5 करोड़ रु. क्षतिपूर्ति; महाराजा दलीप सिंह को ब्रिटिश रेजिडेंट के अधीन शासक बनाया", "type": "leaf"},
                {"label": "भैरोवाल संधि (दिसं. 1846): आठ सिख सरदारों ने रीजेंसी परिषद बनाई; हेनरी लॉरेंस सर्वोच्च प्राधिकार के साथ रेजिडेंट बने", "type": "leaf"}
            ]},
            {"label": "द्वितीय आंग्ल-सिख युद्ध (1848-49)", "type": "branch", "date": "1848-1849", "children": [
                {"label": "मुल्तान विद्रोह (दीवान मूलराज) और हजारा विद्रोह (चत्तर सिंह अटारीवाला) से भड़का; सिख सेना विद्रोहियों से मिली", "type": "leaf"},
                {"label": "मुख्य युद्ध: रामनगर (नवं. 1848), चिलियांवाला (जन. 1849 — ब्रिटिश सामरिक हार), गुजरात (फर. 1849 — निर्णायक ब्रिटिश जीत)", "type": "leaf"},
                {"label": "लॉर्ड डलहौजी ने मार्च 1849 में पंजाब को हड़पा; दलीप सिंह को इंग्लैंड भेजा; कोहिनूर हीरा जब्त किया", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1849 के बाद", "children": [
                {"label": "पंजाब का विलय ब्रिटिश भारत का अंतिम प्रमुख क्षेत्रीय विस्तार था — उपमहाद्वीप की विजय पूर्ण हुई", "type": "leaf"},
                {"label": "पंजाब प्रशासन बोर्ड (जॉन लॉरेंस, हेनरी लॉरेंस, मैन्सेल) ने अत्यंत कुशल प्रत्यक्ष प्रशासन बनाया", "type": "leaf"},
                {"label": "1857 के बाद सिख सैनिकों को 'मार्शल रेस' के रूप में ब्रिटिश भारतीय सेना में सक्रिय रूप से भर्ती किया गया", "type": "leaf"}
            ]}
        ]
    },
    "annexation-of-oudh": {
        "en": [
            {"label": "Background & Pretext", "type": "branch", "date": "1856", "children": [
                {"label": "Awadh was a buffer state maintaining EIC's North-Indian frontiers; Nawab Wajid Ali Shah accused of misrule", "type": "leaf"},
                {"label": "Subsidiary Alliance (1801): Awadh was already reduced to dependency; Resident had effective control over internal affairs", "type": "leaf"},
                {"label": "Lord Dalhousie submitted 'Condition of Oudh' report in 1854; declared misgovernance as justification for annexation", "type": "leaf"}
            ]},
            {"label": "Annexation (1856)", "type": "branch", "date": "1856", "children": [
                {"label": "Lord Dalhousie (succeeded by Canning) formally annexed Awadh in February 1856 on grounds of misrule — not Doctrine of Lapse", "type": "leaf"},
                {"label": "Nawab Wajid Ali Shah deported to Calcutta; his pension was fixed at Rs 12 lakh per year — seen as humiliating", "type": "leaf"},
                {"label": "Land revenue directly administered by EIC — disrupted Taluqdars (feudal lords) who lost their estates and power", "type": "leaf"}
            ]},
            {"label": "Impact on 1857 Revolt", "type": "branch", "date": "1856-1857", "children": [
                {"label": "Awadh was the epicentre of 1857 revolt; dispossessed Taluqdars and Nawab's army (unemployed sepoys) joined uprising", "type": "leaf"},
                {"label": "Begum Hazrat Mahal led Lucknow resistance; Birjis Qadr proclaimed King; revolt lasted longest here — suppressed June 1858", "type": "leaf"},
                {"label": "After revolt, Taluqdars' estates partially restored under Canning's 'Clemency Policy' — basis of landlord class in UP", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और बहाना", "type": "branch", "date": "1856", "children": [
                {"label": "अवध EIC की उत्तर-भारतीय सीमाओं को बनाए रखने वाला एक बफर राज्य था; नवाब वाजिद अली शाह पर कुशासन का आरोप लगाया गया", "type": "leaf"},
                {"label": "सहायक संधि (1801): अवध पहले से ही निर्भरता में था; रेजिडेंट का आंतरिक मामलों पर प्रभावी नियंत्रण था", "type": "leaf"},
                {"label": "लॉर्ड डलहौजी ने 1854 में 'अवध की स्थिति' रिपोर्ट प्रस्तुत की; विलय के औचित्य के रूप में कुशासन घोषित किया", "type": "leaf"}
            ]},
            {"label": "विलय (1856)", "type": "branch", "date": "1856", "children": [
                {"label": "लॉर्ड डलहौजी (कैनिंग के उत्तराधिकारी) ने फरवरी 1856 में कुशासन के आधार पर औपचारिक रूप से अवध का विलय किया — व्यपगत सिद्धांत नहीं", "type": "leaf"},
                {"label": "नवाब वाजिद अली शाह को कलकत्ता निर्वासित किया; उनकी पेंशन 12 लाख रु. वार्षिक निर्धारित — अपमानजनक मानी गई", "type": "leaf"},
                {"label": "भूमि राजस्व सीधे EIC द्वारा प्रशासित — तालुकदारों (सामंत वर्ग) को बाधित किया जिन्होंने अपनी जागीरें और शक्ति खो दी", "type": "leaf"}
            ]},
            {"label": "1857 विद्रोह पर प्रभाव", "type": "branch", "date": "1856-1857", "children": [
                {"label": "अवध 1857 विद्रोह का केंद्र था; बेदखल तालुकदार और नवाब की सेना (बेरोजगार सिपाही) विद्रोह में शामिल हुए", "type": "leaf"},
                {"label": "बेगम हजरत महल ने लखनऊ प्रतिरोध का नेतृत्व किया; बिरजिस कद्र को राजा घोषित किया; विद्रोह यहाँ सबसे लंबे समय तक चला — जून 1858 में दबाया गया", "type": "leaf"},
                {"label": "विद्रोह के बाद कैनिंग की 'क्षमा नीति' के तहत तालुकदारों की जागीरें आंशिक रूप से बहाल की गईं — यूपी में जमींदार वर्ग का आधार", "type": "leaf"}
            ]}
        ]
    },
    "doctrine-of-lapse-and-its-victim-states": {
        "en": [
            {"label": "Doctrine Explained", "type": "branch", "date": "Dalhousie Era", "children": [
                {"label": "Lord Dalhousie's (1848-56) policy: if an Indian ruler died without a natural heir, the state 'lapsed' to British paramountcy", "type": "leaf"},
                {"label": "Denied rulers the right to adopt heirs — violating long-standing Hindu custom of adoption to perpetuate lineage", "type": "leaf"},
                {"label": "Applicable only to 'dependent' states (subsidiary alliance); not applicable to Mughal Emperor or Nizam of Hyderabad", "type": "leaf"}
            ]},
            {"label": "Victim States", "type": "branch", "date": "1848-1856", "children": [
                {"label": "Satara (1848): First state to lapse; Chhatrapati's adopted son's claim rejected", "type": "leaf"},
                {"label": "Jaitpur, Sambalpur (1849); Baghat (1850); Udaipur (1852); Jhansi (1853) — Rani Lakshmibai's husband Gangadhar Rao had no natural heir", "type": "leaf"},
                {"label": "Nagpur (1854): Bhonsle raja's adopted son's claim rejected; EIC took over large Maratha state", "type": "leaf"}
            ]},
            {"label": "Impact & Criticism", "type": "branch", "date": "Post-1856", "children": [
                {"label": "Angered Indian rulers and aristocracy; feeling of insecurity drove many to support 1857 revolt", "type": "leaf"},
                {"label": "Rani Lakshmibai of Jhansi became a symbol of resistance — 'Meri Jhansi nahin dungi' became rallying cry", "type": "leaf"},
                {"label": "After 1857, Queen's Proclamation (1858) guaranteed Indian princes' right of adoption — doctrine formally abandoned", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सिद्धांत की व्याख्या", "type": "branch", "date": "डलहौजी काल", "children": [
                {"label": "लॉर्ड डलहौजी (1848-56) की नीति: यदि कोई भारतीय शासक बिना प्राकृतिक उत्तराधिकारी के मरे, तो राज्य ब्रिटिश परमाधिकार में 'व्यपगत' हो जाएगा", "type": "leaf"},
                {"label": "शासकों को उत्तराधिकारी गोद लेने के अधिकार से वंचित किया — वंश को बनाए रखने की सदियों पुरानी हिंदू प्रथा का उल्लंघन", "type": "leaf"},
                {"label": "केवल 'आश्रित' राज्यों (सहायक संधि) पर लागू; मुगल सम्राट या हैदराबाद के निजाम पर नहीं", "type": "leaf"}
            ]},
            {"label": "पीड़ित राज्य", "type": "branch", "date": "1848-1856", "children": [
                {"label": "सतारा (1848): व्यपगत होने वाला पहला राज्य; छत्रपति के गोद लिए पुत्र का दावा अस्वीकार", "type": "leaf"},
                {"label": "जैतपुर, संबलपुर (1849); बघाट (1850); उदयपुर (1852); झाँसी (1853) — रानी लक्ष्मीबाई के पति गंगाधर राव का कोई प्राकृतिक उत्तराधिकारी नहीं था", "type": "leaf"},
                {"label": "नागपुर (1854): भोंसले राजा के गोद लिए पुत्र का दावा अस्वीकार; EIC ने बड़े मराठा राज्य का अधिग्रहण किया", "type": "leaf"}
            ]},
            {"label": "प्रभाव और आलोचना", "type": "branch", "date": "1856 के बाद", "children": [
                {"label": "भारतीय शासकों और अभिजात वर्ग को क्रोधित किया; असुरक्षा की भावना ने कई लोगों को 1857 विद्रोह में शामिल होने के लिए प्रेरित किया", "type": "leaf"},
                {"label": "झाँसी की रानी लक्ष्मीबाई प्रतिरोध का प्रतीक बनीं — 'मेरी झाँसी नहीं दूंगी' नारा बन गया", "type": "leaf"},
                {"label": "1857 के बाद, रानी की उद्घोषणा (1858) ने भारतीय राजकुमारों को गोद लेने का अधिकार गारंटी दिया — सिद्धांत औपचारिक रूप से त्यागा गया", "type": "leaf"}
            ]}
        ]
    },
    "doctrine-of-masterly-inactivity": {
        "en": [
            {"label": "Origin & Proponent", "type": "branch", "date": "1865-1876", "children": [
                {"label": "Associated with Lord John Lawrence (Viceroy 1864-69) and Sir Henry Rawlinson; reaction against Forward Policy", "type": "leaf"},
                {"label": "Held that British India should not intervene in Afghan internal affairs or push towards Central Asia — avoid costly wars", "type": "leaf"},
                {"label": "Afghanistan should be left as a buffer state between British India and Russian expansion into Central Asia", "type": "leaf"}
            ]},
            {"label": "Arguments For", "type": "branch", "date": "Policy Debate", "children": [
                {"label": "First Anglo-Afghan War (1839-42) was a military disaster costing thousands of lives — never repeat it", "type": "leaf"},
                {"label": "Maintaining neutrality maintained goodwill of Afghan tribes; any intervention would push Afghans towards Russia", "type": "leaf"},
                {"label": "India's resources better spent on internal development (railways, irrigation, education) than frontier wars", "type": "leaf"}
            ]},
            {"label": "Failure & Replacement", "type": "branch", "date": "1876-1878", "children": [
                {"label": "Lord Lytton replaced Masterly Inactivity with 'Forward Policy'; led to Second Anglo-Afghan War (1878-80)", "type": "leaf"},
                {"label": "Lytton wanted Amir Sher Ali to accept British Resident at Kabul; Sher Ali's refusal triggered invasion", "type": "leaf"},
                {"label": "Gandamak Treaty (1879): Afghanistan's foreign policy controlled by British; British resident at Kabul — partial Forward Policy success", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उत्पत्ति और समर्थक", "type": "branch", "date": "1865-1876", "children": [
                {"label": "लॉर्ड जॉन लॉरेंस (वायसराय 1864-69) और सर हेनरी रॉलिन्सन से जुड़ा; अग्रवर्ती नीति के विरुद्ध प्रतिक्रिया", "type": "leaf"},
                {"label": "यह मत था कि ब्रिटिश भारत को अफगान आंतरिक मामलों में हस्तक्षेप नहीं करना चाहिए — महंगे युद्धों से बचना", "type": "leaf"},
                {"label": "अफगानिस्तान को ब्रिटिश भारत और मध्य एशिया में रूसी विस्तार के बीच बफर राज्य के रूप में छोड़ा जाए", "type": "leaf"}
            ]},
            {"label": "समर्थन में तर्क", "type": "branch", "date": "नीति बहस", "children": [
                {"label": "प्रथम आंग्ल-अफगान युद्ध (1839-42) हजारों जीवन की लागत वाली सैन्य तबाही था — इसे दोहराना नहीं", "type": "leaf"},
                {"label": "तटस्थता बनाए रखने से अफगान कबीलों की शुभेच्छा बनी रही; कोई भी हस्तक्षेप अफगानों को रूस की ओर धकेलता", "type": "leaf"},
                {"label": "भारत के संसाधन सीमांत युद्धों की बजाय आंतरिक विकास (रेलवे, सिंचाई, शिक्षा) पर बेहतर खर्च किए जाएं", "type": "leaf"}
            ]},
            {"label": "विफलता और प्रतिस्थापन", "type": "branch", "date": "1876-1878", "children": [
                {"label": "लॉर्ड लिटन ने शानदार निष्क्रियता की जगह 'अग्रवर्ती नीति' लाई; द्वितीय आंग्ल-अफगान युद्ध (1878-80) हुआ", "type": "leaf"},
                {"label": "लिटन चाहते थे कि अमीर शेर अली काबुल में ब्रिटिश रेजिडेंट स्वीकार करें; शेर अली के इनकार से आक्रमण हुआ", "type": "leaf"},
                {"label": "गंडामक संधि (1879): अफगानिस्तान की विदेश नीति ब्रिटिश नियंत्रण में; काबुल में ब्रिटिश रेजिडेंट — आंशिक सफलता", "type": "leaf"}
            ]}
        ]
    },
    "doctrine-of-ring-fence": {
        "en": [
            {"label": "Concept", "type": "branch", "date": "Warren Hastings Era", "children": [
                {"label": "Policy associated with Warren Hastings: create a buffer zone of protected states around British India's borders", "type": "leaf"},
                {"label": "Aimed to limit EIC's military commitments while safeguarding Bengal's territorial gains post-Battle of Buxar", "type": "leaf"},
                {"label": "British would defend buffer states against external enemies but not interfere in internal affairs — unlike Wellesley's Subsidiary Alliance", "type": "leaf"}
            ]},
            {"label": "Application", "type": "branch", "date": "1765-1813", "children": [
                {"label": "Awadh (Oudh) was the primary buffer state — maintained as an ally against Maratha and Afghan threats from the north", "type": "leaf"},
                {"label": "EIC provided military defense to Nawab of Awadh in exchange for annual payments and non-alliance with other powers", "type": "leaf"},
                {"label": "Hyderabad used as eastern buffer against Mysore; EIC supported Nizam militarily against Tipu Sultan", "type": "leaf"}
            ]},
            {"label": "Transition to Forward Policy", "type": "branch", "date": "Post-1798", "children": [
                {"label": "Wellesley (1798) replaced Ring Fence with Subsidiary Alliance — more interventionist, demanded internal compliance", "type": "leaf"},
                {"label": "Ring Fence failed because buffer states remained sources of intrigue and instability — direct control seemed preferable", "type": "leaf"},
                {"label": "Concept revived in North-West with Afghanistan policy — Masterly Inactivity (1864-76) echoed Ring Fence principle", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अवधारणा", "type": "branch", "date": "वारेन हेस्टिंग्स काल", "children": [
                {"label": "वारेन हेस्टिंग्स से जुड़ी नीति: ब्रिटिश भारत की सीमाओं के चारों ओर संरक्षित राज्यों का बफर क्षेत्र बनाना", "type": "leaf"},
                {"label": "बक्सर की लड़ाई के बाद बंगाल के क्षेत्रीय लाभों की रक्षा करते हुए EIC की सैन्य प्रतिबद्धताओं को सीमित करने का लक्ष्य", "type": "leaf"},
                {"label": "ब्रिटिश बाहरी शत्रुओं के खिलाफ बफर राज्यों की रक्षा करेंगे लेकिन आंतरिक मामलों में हस्तक्षेप नहीं — वेलेजली की सहायक संधि से भिन्न", "type": "leaf"}
            ]},
            {"label": "अनुप्रयोग", "type": "branch", "date": "1765-1813", "children": [
                {"label": "अवध (उत्तर से मराठा और अफगान खतरों के खिलाफ) प्राथमिक बफर राज्य था — एक सहयोगी के रूप में बनाए रखा गया", "type": "leaf"},
                {"label": "EIC ने वार्षिक भुगतान और अन्य शक्तियों के साथ गठबंधन न करने के बदले में अवध के नवाब को सैन्य रक्षा प्रदान की", "type": "leaf"},
                {"label": "हैदराबाद को मैसूर के खिलाफ पूर्वी बफर के रूप में उपयोग किया; EIC ने टीपू सुल्तान के खिलाफ निजाम का सैन्य समर्थन किया", "type": "leaf"}
            ]},
            {"label": "अग्रवर्ती नीति की ओर संक्रमण", "type": "branch", "date": "1798 के बाद", "children": [
                {"label": "वेलेजली (1798) ने रिंग फेंस की जगह सहायक संधि ली — अधिक हस्तक्षेपवादी, आंतरिक अनुपालन की मांग की", "type": "leaf"},
                {"label": "रिंग फेंस विफल रही क्योंकि बफर राज्य साजिश और अस्थिरता के स्रोत बने रहे — प्रत्यक्ष नियंत्रण बेहतर लगा", "type": "leaf"},
                {"label": "अवधारणा उत्तर-पश्चिम में अफगानिस्तान नीति में पुनर्जीवित हुई — शानदार निष्क्रियता (1864-76) ने रिंग फेंस सिद्धांत को दोहराया", "type": "leaf"}
            ]}
        ]
    },
    "eics-relations-with-neighboring-countries": {
        "en": [
            {"label": "Relations with Nepal", "type": "branch", "date": "Anglo-Nepalese", "children": [
                {"label": "Anglo-Nepalese War (1814-16): Gurkha expansion into northern India clashed with EIC's Terai territories", "type": "leaf"},
                {"label": "Treaty of Sagauli (1816): Nepal ceded Sikkim, Kumaon, Garhwal; Terai regions; British Resident at Kathmandu", "type": "leaf"},
                {"label": "Gurkhas thereafter recruited into British Indian Army — became the celebrated 'martial race' troops used globally", "type": "leaf"}
            ]},
            {"label": "Relations with Burma", "type": "branch", "date": "Anglo-Burmese Wars", "children": [
                {"label": "First Anglo-Burmese War (1824-26): Burma annexed Assam and Manipur; EIC launched naval campaign; Treaty of Yandabo gave Arakan and Tenasserim", "type": "leaf"},
                {"label": "Second Anglo-Burmese War (1852): Dalhousie annexed Lower Burma (Pegu) after commercial disputes — no formal peace treaty", "type": "leaf"},
                {"label": "Third Anglo-Burmese War (1885): Lord Dufferin annexed Upper Burma; King Thibaw exiled; entire Burma under British India by 1886", "type": "leaf"}
            ]},
            {"label": "Relations with Afghanistan", "type": "branch", "date": "Anglo-Afghan Wars", "children": [
                {"label": "First Anglo-Afghan War (1839-42): British tried to install Shah Shuja; catastrophic retreat from Kabul — 16,000 killed", "type": "leaf"},
                {"label": "Second Anglo-Afghan War (1878-80): Lytton's Forward Policy; Gandamak Treaty gave British control of Afghanistan's foreign policy", "type": "leaf"},
                {"label": "Third Anglo-Afghan War (1919): Afghanistan won independence of foreign relations under Treaty of Rawalpindi", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नेपाल के साथ संबंध", "type": "branch", "date": "आंग्ल-नेपाली", "children": [
                {"label": "आंग्ल-नेपाली युद्ध (1814-16): गोरखा विस्तार उत्तरी भारत में EIC के तराई क्षेत्रों से टकराया", "type": "leaf"},
                {"label": "सगौली की संधि (1816): नेपाल ने सिक्किम, कुमाऊं, गढ़वाल; तराई क्षेत्र सौंपे; काठमांडू में ब्रिटिश रेजिडेंट", "type": "leaf"},
                {"label": "इसके बाद गोरखाओं को ब्रिटिश भारतीय सेना में भर्ती किया गया — वैश्विक स्तर पर उपयोग किए जाने वाले प्रसिद्ध 'मार्शल रेस' सैनिक बने", "type": "leaf"}
            ]},
            {"label": "बर्मा के साथ संबंध", "type": "branch", "date": "आंग्ल-बर्मी युद्ध", "children": [
                {"label": "प्रथम आंग्ल-बर्मी युद्ध (1824-26): बर्मा ने असम और मणिपुर पर कब्जा किया; EIC ने नौसैनिक अभियान चलाया; यंदाबू संधि से अराकान और टेनासेरिम मिले", "type": "leaf"},
                {"label": "द्वितीय आंग्ल-बर्मी युद्ध (1852): डलहौजी ने व्यावसायिक विवादों के बाद निचले बर्मा (पेगू) का विलय किया — कोई औपचारिक शांति संधि नहीं", "type": "leaf"},
                {"label": "तृतीय आंग्ल-बर्मी युद्ध (1885): लॉर्ड डफरिन ने ऊपरी बर्मा का विलय किया; राजा थीबॉ निर्वासित; 1886 तक पूरा बर्मा ब्रिटिश भारत के अधीन", "type": "leaf"}
            ]},
            {"label": "अफगानिस्तान के साथ संबंध", "type": "branch", "date": "आंग्ल-अफगान युद्ध", "children": [
                {"label": "प्रथम आंग्ल-अफगान युद्ध (1839-42): अंग्रेजों ने शाह शुजा को स्थापित करने की कोशिश की; काबुल से विनाशकारी वापसी — 16,000 मारे गए", "type": "leaf"},
                {"label": "द्वितीय आंग्ल-अफगान युद्ध (1878-80): लिटन की अग्रवर्ती नीति; गंडामक संधि ने अफगानिस्तान की विदेश नीति पर ब्रिटिश नियंत्रण दिया", "type": "leaf"},
                {"label": "तृतीय आंग्ल-अफगान युद्ध (1919): अफगानिस्तान ने रावलपिंडी संधि के तहत विदेश संबंधों की स्वतंत्रता जीती", "type": "leaf"}
            ]}
        ]
    },
    "policy-of-proud-reserve": {
        "en": [
            {"label": "Concept", "type": "branch", "date": "1880-1884", "children": [
                {"label": "Policy associated with Viceroy Lord Ripon (1880-84) and Secretary of State Lord Hartington — a middle path", "type": "leaf"},
                {"label": "Rejected both extreme Forward Policy (Lytton's aggressive expansion) and passive Masterly Inactivity", "type": "leaf"},
                {"label": "Britain would maintain 'proud reserve' — firm in its position, not seeking confrontation but not retreating either", "type": "leaf"}
            ]},
            {"label": "Context: Great Game", "type": "branch", "date": "1880s Context", "children": [
                {"label": "Russia had been advancing in Central Asia: Tashkent (1865), Samarkand (1868), Khiva (1873), Merv (1884)", "type": "leaf"},
                {"label": "British feared Russian presence in Afghanistan would give direct access to India's North-West Frontier", "type": "leaf"},
                {"label": "Ripon's policy: maintain Abdur Rahman (new Afghan Amir) as a strong buffer without British troops in Afghanistan", "type": "leaf"}
            ]},
            {"label": "Outcomes", "type": "branch", "date": "1880s Onwards", "children": [
                {"label": "Abdur Rahman proved an effective buffer king — kept Russians out while accepting British control of foreign policy", "type": "leaf"},
                {"label": "Demarcation of Afghan border: Durand Line (1893) drawn by Mortimer Durand under Viceroy Lansdowne — 2,640 km frontier", "type": "leaf"},
                {"label": "Policy essentially continued under Lansdowne and Elgin — neither provoking Russia nor retreating from frontier gains", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अवधारणा", "type": "branch", "date": "1880-1884", "children": [
                {"label": "वायसराय लॉर्ड रिपन (1880-84) और भारत सचिव लॉर्ड हार्टिंगटन से जुड़ी नीति — एक मध्यम मार्ग", "type": "leaf"},
                {"label": "अत्यधिक अग्रवर्ती नीति (लिटन का आक्रामक विस्तार) और निष्क्रिय शानदार निष्क्रियता दोनों को अस्वीकार किया", "type": "leaf"},
                {"label": "ब्रिटेन 'गर्वित आरक्षण' बनाए रखेगा — अपनी स्थिति में दृढ़, टकराव नहीं खोजना लेकिन पीछे भी नहीं हटना", "type": "leaf"}
            ]},
            {"label": "संदर्भ: महान खेल", "type": "branch", "date": "1880 का दशक", "children": [
                {"label": "रूस मध्य एशिया में आगे बढ़ रहा था: ताशकंद (1865), समरकंद (1868), खीवा (1873), मर्व (1884)", "type": "leaf"},
                {"label": "ब्रिटिश डरते थे कि अफगानिस्तान में रूस की उपस्थिति भारत की उत्तर-पश्चिम सीमा तक सीधी पहुंच देगी", "type": "leaf"},
                {"label": "रिपन की नीति: अफगानिस्तान में ब्रिटिश सैनिकों के बिना अब्दुर रहमान (नए अफगान अमीर) को एक मजबूत बफर के रूप में बनाए रखना", "type": "leaf"}
            ]},
            {"label": "परिणाम", "type": "branch", "date": "1880 के दशक से", "children": [
                {"label": "अब्दुर रहमान एक प्रभावी बफर राजा साबित हुए — रूसियों को बाहर रखा जबकि विदेश नीति पर ब्रिटिश नियंत्रण स्वीकार किया", "type": "leaf"},
                {"label": "अफगान सीमा निर्धारण: डूरंड रेखा (1893) वायसराय लैंसडाउन के तहत मोर्टिमर डूरंड द्वारा खींची गई — 2,640 कि.मी. सीमा", "type": "leaf"},
                {"label": "नीति अनिवार्य रूप से लैंसडाउन और एल्गिन के अधीन जारी रही — न रूस को उकसाना न सीमांत लाभ से पीछे हटना", "type": "leaf"}
            ]}
        ]
    }
}

MINDMAP_MAPPINGS = {
    "2-anglo-sikh-wars": "2-anglo-sikh-wars",
    "annexation-of-oudh": "annexation-of-oudh",
    "doctrine-of-lapse-and-its-victim-states": "doctrine-of-lapse-and-its-victim-states",
    "doctrine-of-masterly-inactivity": "doctrine-of-masterly-inactivity",
    "doctrine-of-ring-fence": "doctrine-of-ring-fence",
    "eics-relations-with-neighboring-countries": "eics-relations-with-neighboring-countries",
    "policy-of-proud-reserve": "policy-of-proud-reserve"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about', 's'}
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
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, "2-anglo-sikh-wars")

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
