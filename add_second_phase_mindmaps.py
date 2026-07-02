#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Second-Phase-of-National-Movement-1918-1929"

MINDMAP_DATA = {
    "chauri-chaura-incident-5th-feb-1922": {
        "en": [
            {"label": "The Clash", "type": "branch", "date": "Feb 5, 1922", "children": [
                {"label": "Gorakhpur (UP): Clash between police and Congress-Khilafat volunteers protesting food prices", "type": "leaf"},
                {"label": "Police fired on protestors; angry crowd set fire to Chauri Chaura police station, killing 22 policemen", "type": "leaf"}]},
            {"label": "Gandhi's Action", "type": "branch", "date": "Withdrawal", "children": [
                {"label": "Gandhi called off Non-Cooperation Movement on Feb 12, 1922 (Bardoli Resolution) citing rise in violence", "type": "leaf"},
                {"label": "Suspended all offensive activities; decision criticized by Motilal Nehru, Subhas Bose, Lajpat Rai", "type": "leaf"}]},
            {"label": "Legal Aftermath", "type": "branch", "date": "Trial", "children": [
                {"label": "Gandhi arrested on March 10, 1922; sentenced to 6 years by Judge C.N. Broomfield for sedition", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "हिंसक झड़प", "type": "branch", "date": "5 फरवरी 1922", "children": [
                {"label": "गोरखपुर (यूपी): महंगाई का विरोध कर रहे कांग्रेस-खिलाफत स्वयंसेवकों और पुलिस के बीच संघर्ष", "type": "leaf"},
                {"label": "पुलिस गोलीबारी के बाद क्रोधित भीड़ ने पुलिस थाने में आग लगा दी, जिससे 22 पुलिसकर्मी जिंदा जल गए", "type": "leaf"}]},
            {"label": "गांधीजी का निर्णय", "type": "branch", "date": "वापसी", "children": [
                {"label": "गांधीजी ने आंदोलन हिंसक होने के कारण 12 फरवरी 1922 (बारडोली प्रस्ताव) को असहयोग आंदोलन समाप्त घोषित किया", "type": "leaf"},
                {"label": "मोतीलाल नेहरू, सुभाष बोस और लाला लाजपत राय द्वारा गांधीजी के इस निर्णय की कड़ी आलोचना", "type": "leaf"}]},
            {"label": "कानूनी परिणाम", "type": "branch", "date": "मुकदमा", "children": [
                {"label": "गांधीजी को 10 मार्च 1922 को गिरफ्तार किया गया; न्यायाधीश सी.एन. ब्रूमफील्ड ने 6 वर्ष के कारावास की सजा सुनाई", "type": "leaf"}]}
        ]
    },
    "congress-khilafat-swaraj-party": {
        "en": [
            {"label": "Origin", "type": "branch", "date": "Jan 1, 1923", "children": [
                {"label": "Gaya Session (1922) split: C.R. Das resigned as INC president after council entry proposal was defeated", "type": "leaf"},
                {"label": "Swaraj Party formed on Jan 1, 1923; C.R. Das (President) and Motilal Nehru (Secretary)", "type": "leaf"}]},
            {"label": "Philosophy", "type": "branch", "date": "Debate", "children": [
                {"label": "Pro-Changers (Swarajists): Wanted legislative entry to obstruct British administration from within", "type": "leaf"},
                {"label": "No-Changers: Opposed council entry; C. Rajagopalachari, Patel, Prasad advocated constructive work & boycott", "type": "leaf"}]},
            {"label": "Achievements", "type": "branch", "date": "Legacy", "children": [
                {"label": "Won 42 out of 101 elected seats in 1923 Central Legislative Assembly elections", "type": "leaf"},
                {"label": "Vithalbhai Patel elected as Speaker (President) of Assembly in 1925; blocked Public Safety Bill (1928)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति", "type": "branch", "date": "1 जनवरी 1923", "children": [
                {"label": "गया अधिवेशन (1922) विभाजन: परिषद प्रवेश प्रस्ताव खारिज होने पर सी.आर. दास ने कांग्रेस अध्यक्ष पद से त्यागपत्र दिया", "type": "leaf"},
                {"label": "1 जनवरी 1923 को स्वराज पार्टी का गठन; सी.आर. दास (अध्यक्ष) और मोतीलाल नेहरू (सचिव)", "type": "leaf"}]},
            {"label": "विचारधारा", "type": "branch", "date": "बहस", "children": [
                {"label": "परिवर्तनवादी (स्वराजवादी): विधानमंडलों में प्रवेश कर अंदर से ब्रिटिश सरकार की अड़ंगा नीति के पक्षधर", "type": "leaf"},
                {"label": "अपरिवर्तनवादी: परिषद प्रवेश के विरोधी; सी. राजगोपालाचारी, पटेल, राजेंद्र प्रसाद रचनात्मक कार्यों के पक्षधर", "type": "leaf"}]},
            {"label": "उपलब्धियां", "type": "branch", "date": "विरासत", "children": [
                {"label": "1923 के केंद्रीय विधानसभा चुनावों में 101 निर्वाचित सीटों में से 42 सीटों पर ऐतिहासिक विजय दर्ज की", "type": "leaf"},
                {"label": "विट्ठलभाई पटेल 1925 में केंद्रीय विधानसभा के प्रथम भारतीय अध्यक्ष निर्वाचित; पब्लिक सेफ्टी बिल (1928) को खारिज किया", "type": "leaf"}]}
        ]
    },
    "gandhi-ji-in-india-1915-onwards": {
        "en": [
            {"label": "Arrival", "type": "branch", "date": "Jan 1915", "children": [
                {"label": "Returned to India on Jan 9, 1915 (Pravasi Bharatiya Divas) from South Africa", "type": "leaf"},
                {"label": "Mentor G.K. Gokhale advised him to tour India for a year to observe socio-political realities", "type": "leaf"},
                {"label": "Established Satyagraha Ashram at Kochrab (1915); shifted to Sabarmati banks in 1917", "type": "leaf"}]},
            {"label": "Initial Satyagrahas", "type": "branch", "date": "Local Struggles", "children": [
                {"label": "Champaran Satyagraha (1917) in Bihar against Tinkathia system; first Civil Disobedience", "type": "leaf"},
                {"label": "Ahmedabad Mill Strike (1918) - first hunger strike; secured 35% wage raise for mill workers", "type": "leaf"},
                {"label": "Kheda Satyagraha (1918) - first Non-Cooperation; tax relief for famine-stricken peasants", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आगमन", "type": "branch", "date": "जनवरी 1915", "children": [
                {"label": "9 जनवरी 1915 को दक्षिण अफ्रीका से भारत वापसी (प्रवासी भारतीय दिवस के रूप में मनाया जाता है)", "type": "leaf"},
                {"label": "गुरु जी.के. गोखले की सलाह पर वास्तविक जनजीवन को समझने हेतु एक वर्ष देश का भ्रमण किया", "type": "leaf"},
                {"label": "कोचरब में सत्याग्रह आश्रम (1915) स्थापित; 1917 में साबरमती नदी के किनारे स्थानांतरित", "type": "leaf"}]},
            {"label": "प्रारंभिक सत्याग्रह", "type": "branch", "date": "स्थानीय संघर्ष", "children": [
                {"label": "चंपारण सत्याग्रह (1917): तिनकठिया प्रणाली के विरुद्ध बिहार में; प्रथम सविनय अवज्ञा आंदोलन", "type": "leaf"},
                {"label": "अहमदाबाद मिल हड़ताल (1918): प्रथम भूख हड़ताल; मिल मजदूरों हेतु 35% वेतन वृद्धि हासिल की", "type": "leaf"},
                {"label": "खेड़ा सत्याग्रह (1918): प्रथम असहयोग; अकाल पीड़ित किसानों हेतु कर छूट आंदोलन", "type": "leaf"}]}
        ]
    },
    "gandhi-ji-in-south-africa-1894-1914": {
        "en": [
            {"label": "Early Phase", "type": "branch", "date": "1893-1906", "children": [
                {"label": "Arrived in 1893 for Dada Abdulla's legal case; thrown off train at Pietermaritzburg", "type": "leaf"},
                {"label": "Natal Indian Congress (1894) founded to organize Indian settlers against discrimination", "type": "leaf"},
                {"label": "Indian Opinion (1903) weekly newspaper launched; Phoenix Settlement (1904) established near Durban", "type": "leaf"}]},
            {"label": "Satyagraha Phase", "type": "branch", "date": "1906-1914", "children": [
                {"label": "Passive Resistance Association (1906) against Asiatic Registration Act (Black Act)", "type": "leaf"},
                {"label": "Tolstoy Farm (1910) set up near Johannesburg to house and train Satyagrahis", "type": "leaf"},
                {"label": "Smuts-Gandhi Agreement (1914) repealed poll tax (£3) and validated Indian marriages", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक चरण", "type": "branch", "date": "1893-1906", "children": [
                {"label": "1893 में दादा अब्दुल्ला के मुकदमे हेतु आगमन; पीटरमैरिट्सबर्ग स्टेशन पर ट्रेन से बाहर फेंके गए", "type": "leaf"},
                {"label": "भेदभाव के खिलाफ भारतीयों को संगठित करने हेतु नटाल भारतीय कांग्रेस (1894) की स्थापना", "type": "leaf"},
                {"label": "साप्ताहिक 'इंडियन ओपिनियन' (1903) का प्रकाशन; डरबन के पास फीनिक्स सेटलमेंट (1904) स्थापित", "type": "leaf"}]},
            {"label": "सत्याग्रह चरण", "type": "branch", "date": "1906-1914", "children": [
                {"label": "एशियाई पंजीकरण अधिनियम (ब्लैक एक्ट) के खिलाफ पैसिव रेजिस्टेंस एसोसिएशन (1906) का गठन", "type": "leaf"},
                {"label": "सत्याग्रहियों को प्रशिक्षित करने हेतु जोहान्सबर्ग के पास टॉल्स्टॉय फार्म (1910) की स्थापना", "type": "leaf"},
                {"label": "स्मट्स-गांधी समझौता (1914): £3 पोल टैक्स समाप्त और गैर-ईसाई विवाहों को मान्यता दी गई", "type": "leaf"}]}
        ]
    },
    "highlight-ahmedabad-mill-strike-1918": {
        "en": [
            {"label": "Dispute", "type": "branch", "date": "1918 Mill", "children": [
                {"label": "Mill owners withdrew plague bonus post-epidemic; inflation caused severe worker distress", "type": "leaf"},
                {"label": "Gandhi urged workers to demand a 35% wage increase (owners offered only 20%)", "type": "leaf"},
                {"label": "Gandhi undertook his first fast-unto-death in India to strengthen workers' resolve", "type": "leaf"},
                {"label": "Outcome: Matter referred to arbitration tribunal which awarded the full 35% increase", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विवाद", "type": "branch", "date": "1918 मिल", "children": [
                {"label": "प्लेग समाप्ति पर बोनस बंद किया गया; विश्व युद्ध के कारण बढ़ी महंगाई से मजदूर संकट में थे", "type": "leaf"},
                {"label": "गांधीजी ने मजदूरों से 35% वेतन वृद्धि की मांग करने को कहा (मालिक केवल 20% देने को तैयार थे)", "type": "leaf"},
                {"label": "मजदूरों के संकल्प को बनाए रखने हेतु गांधीजी ने भारत में अपनी पहली भूख हड़ताल की", "type": "leaf"},
                {"label": "परिणाम: मामला मध्यस्थता न्यायाधिकरण को सौंपा गया जिसने पूर्ण 35% वृद्धि को स्वीकार किया", "type": "leaf"}]}
        ]
    },
    "highlight-champaran-satyagraha-1917": {
        "en": [
            {"label": "Indigo Grievance", "type": "branch", "date": "1917 Bihar", "children": [
                {"label": "Tinkathia system required peasants to cultivate indigo on 3/20th of their land", "type": "leaf"},
                {"label": "Peasant Rajkumar Shukla invited Gandhi to investigate the exploitation by European planters", "type": "leaf"},
                {"label": "Gandhi defied court orders to leave; first Civil Disobedience campaign in India", "type": "leaf"},
                {"label": "Champaran Agrarian Committee abolished Tinkathia and refunded 25% of illegal taxes", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नील समस्या", "type": "branch", "date": "1917 बिहार", "children": [
                {"label": "तिनकठिया प्रथा के अंतर्गत किसानों को भूमि के 3/20वें भाग पर नील उगाना अनिवार्य था", "type": "leaf"},
                {"label": "किसान राजकुमार शुक्ल ने यूरोपीय बागान मालिकों के शोषण की जांच हेतु गांधीजी को आमंत्रित किया", "type": "leaf"},
                {"label": "गांधीजी ने चंपारण छोड़ने के अदालती आदेश की अवहेलना की; भारत में प्रथम सविनय अवज्ञा अभियान", "type": "leaf"},
                {"label": "चंपारण कृषि समिति ने तिनकठिया प्रथा समाप्त की और 25% अवैध वसूली वापस कराई", "type": "leaf"}]}
        ]
    },
    "highlight-kheda-satyagraha-1918": {
        "en": [
            {"label": "Tax Standoff", "type": "branch", "date": "1918 Gujarat", "children": [
                {"label": "Drought caused crop failure; revenue code allowed suspension if yield was under 25%, but British refused", "type": "leaf"},
                {"label": "Gandhi and Patel organized revenue boycott; government seized peasants' cattle and properties", "type": "leaf"},
                {"label": "Agreement reached: Secret instructions issued to collect revenue only from those who could pay", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कर विवाद", "type": "branch", "date": "1918 गुजरात", "children": [
                {"label": "सूखे से फसलें नष्ट; राजस्व संहिता के अनुसार 25% से कम फसल होने पर छूट का नियम था, परंतु अंग्रेजों ने कर वसूला", "type": "leaf"},
                {"label": "गांधीजी और पटेल ने कर न देने का आंदोलन चलाया; ब्रिटिश अधिकारियों ने संपत्ति और मवेशियों को कुर्क किया", "type": "leaf"},
                {"label": "सहमति: सरकार ने गुप्त रूप से निर्देश दिए कि केवल समर्थ किसानों से ही कर लिया जाए", "type": "leaf"}]}
        ]
    },
    "inc-allahabad-address-1930": {
        "en": [
            {"label": "Iqbal's Proposition", "type": "branch", "date": "Dec 1930", "children": [
                {"label": "Sir Muhammad Iqbal presided over All India Muslim League session at Allahabad", "type": "leaf"},
                {"label": "Proposed a separate consolidated Muslim state in northwestern India (Punjab, NWFP, Sindh, Baluchistan)", "type": "leaf"},
                {"label": "Laid ideological base of Two-Nation Theory, paving way for Pakistan demand", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "इकबाल का प्रस्ताव", "type": "branch", "date": "दिसंबर 1930", "children": [
                {"label": "सर मुहम्मद इकबाल ने इलाहाबाद में ऑल इंडिया मुस्लिम लीग अधिवेशन की अध्यक्षता की", "type": "leaf"},
                {"label": "उत्तर-पश्चिम भारत (पंजाब, एनडब्ल्यूएफपी, सिंध, बलूचिस्तान) में एक पृथक एकीकृत मुस्लिम राज्य का प्रस्ताव दिया", "type": "leaf"},
                {"label": "द्वि-राष्ट्र सिद्धांत की वैचारिक नींव रखी, जिससे पाकिस्तान की मांग का मार्ग प्रशस्त हुआ", "type": "leaf"}]}
        ]
    },
    "inc-lahore-session-1929": {
        "en": [
            {"label": "Complete Independence", "type": "branch", "date": "Dec 1929", "children": [
                {"label": "Presided by Jawaharlal Nehru; passed historic resolution for 'Poorna Swaraj' (Complete Independence) instead of Dominion Status", "type": "leaf"},
                {"label": "Decided to boycott Round Table Conference & authorized Civil Disobedience", "type": "leaf"}]},
            {"label": "Symbols", "type": "branch", "date": "Action", "children": [
                {"label": "Tricolour flag hoisted on the banks of Ravi river on midnight of Dec 31, 1929", "type": "leaf"},
                {"label": "Jan 26, 1930 declared as Independence Day to be celebrated with pledge", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पूर्ण स्वतंत्रता", "type": "branch", "date": "दिसंबर 1929", "children": [
                {"label": "जवाहरलाल नेहरू की अध्यक्षता; डोमिनियन स्टेटस के बजाय 'पूर्ण स्वराज' (पूर्ण स्वतंत्रता) का ऐतिहासिक प्रस्ताव पारित किया", "type": "leaf"},
                {"label": "गोलमेज सम्मेलन के बहिष्कार और सविनय अवज्ञा शुरू करने का निर्णय लिया गया", "type": "leaf"}]},
            {"label": "प्रतीक", "type": "branch", "date": "कार्रवाई", "children": [
                {"label": "31 दिसंबर 1929 की मध्यरात्रि को रावी नदी के तट पर तिरंगा झंडा फहराया गया", "type": "leaf"},
                {"label": "26 जनवरी 1930 को प्रथम स्वतंत्रता दिवस घोषित किया गया, जिसे प्रतिज्ञा के साथ मनाया जाना था", "type": "leaf"}]}
        ]
    },
    "indian-statutory-commission-simon-commission-1927": {
        "en": [
            {"label": "The Commission", "type": "branch", "date": "Simon Commission", "children": [
                {"label": "7-member all-white statutory commission appointed under John Simon to review GoI Act 1919 reforms", "type": "leaf"},
                {"label": "No Indian members included, which united Indian parties in opposition & protest", "type": "leaf"}]},
            {"label": "Boycott & Tragedy", "type": "branch", "date": "Protests", "children": [
                {"label": "Boycotted by Congress, Jinnah faction of Muslim League, Hindu Mahasabha, Liberal Federation", "type": "leaf"},
                {"label": "Lala Lajpat Rai brutally lathi-charged during peaceful protests in Lahore; died of injuries on Nov 17, 1928", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आयोग", "type": "branch", "date": "साइमन कमीशन", "children": [
                {"label": "1919 के अधिनियम के सुधारों की समीक्षा हेतु जॉन साइमन के नेतृत्व में 7 सदस्यीय सर्व-श्वेत वैधानिक आयोग", "type": "leaf"},
                {"label": "किसी भी भारतीय को शामिल न करने से भारतीय दलों में आक्रोश उत्पन्न हुआ और उन्होंने विरोध किया", "type": "leaf"}]},
            {"label": "बहिष्कार और त्रासदी", "type": "branch", "date": "विरोध", "children": [
                {"label": "कांग्रेस, मुस्लिम लीग (जिन्ना गुट), हिंदू महासभा, लिबरल फेडरेशन द्वारा पूर्ण बहिष्कार किया गया", "type": "leaf"},
                {"label": "लाहौर में प्रदर्शन के दौरान लाला लाजपत राय पर क्रूरतापूर्वक लाठीचार्ज; 17 नवंबर 1928 को चोटों के कारण निधन", "type": "leaf"}]}
        ]
    },
    "jinnahs-fourteen-points-demand-1929": {
        "en": [
            {"label": "Key Demands", "type": "branch", "date": "March 1929", "children": [
                {"label": "Proposed by Jinnah at Delhi League session; rejected joint electorate proposal of Nehru Report", "type": "leaf"},
                {"label": "Demanded federal constitution with residuary powers given to provinces; provincial autonomy", "type": "leaf"},
                {"label": "1/3rd Muslim representation in Central Legislature; separate electorates; separation of Sindh from Bombay", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य मांगें", "type": "branch", "date": "मार्च 1929", "children": [
                {"label": "जिन्ना द्वारा दिल्ली लीग अधिवेशन में प्रस्तावित; नेहरू रिपोर्ट के संयुक्त निर्वाचन प्रस्ताव को खारिज किया", "type": "leaf"},
                {"label": "प्रांतों को अवशिष्ट शक्तियों के साथ संघीय संविधान और प्रांतीय स्वायत्तता की मांग की", "type": "leaf"},
                {"label": "केंद्रीय विधानमंडल में मुसलमानों हेतु 1/3 प्रतिनिधित्व; पृथक निर्वाचन; बॉम्बे से सिंध को अलग करने की मांग", "type": "leaf"}]}
        ]
    },
    "khilafat-movement-1919-20": {
        "en": [
            {"label": "Origins", "type": "branch", "date": "1919-1920", "children": [
                {"label": "Indian Muslim protest against harsh Treaty of Sevres dismantling Ottoman Caliph (Khalifa)", "type": "leaf"},
                {"label": "Led by Ali Brothers (Shaukat & Mohammad Ali), Maulana Azad, Hasrat Mohani", "type": "leaf"}]},
            {"label": "Gandhi's Role", "type": "branch", "date": "Alliance", "children": [
                {"label": "Gandhi elected president of All India Khilafat Conference (1919); linked it to Non-Cooperation for Hindu-Muslim unity", "type": "leaf"},
                {"label": "Collapsed in 1922 when Kemal Pasha declared Turkey a secular republic & abolished Caliphate", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उत्पत्ति", "type": "branch", "date": "1919-1920", "children": [
                {"label": "तुर्की के ऑटोमन खलीफा के विभाजन के विरुद्ध भारतीय मुसलमानों द्वारा सेवर्स की संधि के खिलाफ विरोध", "type": "leaf"},
                {"label": "अली बंधुओं (शौकत और मोहम्मद अली), मौलाना आज़ाद, हकीम अजमल खान द्वारा नेतृत्व", "type": "leaf"}]},
            {"label": "गांधीजी की भूमिका", "type": "branch", "date": "गठबंधन", "children": [
                {"label": "गांधीजी अखिल भारतीय खिलाफत सम्मेलन (1919) के अध्यक्ष चुने गए; हिंदू-मुस्लिम एकता हेतु इसे असहयोग से जोड़ा", "type": "leaf"},
                {"label": "1922 में मुस्तफा कमाल पाशा द्वारा तुर्की को धर्मनिरपेक्ष घोषित करने व खिलाफत समाप्त करने से आंदोलन समाप्त", "type": "leaf"}]}
        ]
    },
    "leaders-in-this-phase-and-their-contribution": {
        "en": [
            {"label": "Leaders", "type": "branch", "date": "Contributions", "children": [
                {"label": "Sardar Patel: Led Kheda (1918) and Bardoli (1928) satyagrahas; earned title 'Sardar' from Bardoli women", "type": "leaf"},
                {"label": "Motilal Nehru: Chaired committee that drafted Nehru Report (1928), first native constitutional framework", "type": "leaf"},
                {"label": "Deshbandhu C.R. Das: Presided Gaya session (1922); Mayor of Calcutta; co-founded Swaraj Party", "type": "leaf"},
                {"label": "Lala Lajpat Rai: Sher-e-Punjab; first president of AITUC (1920); died resisting Simon Commission (1928)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नेता", "type": "branch", "date": "योगदान", "children": [
                {"label": "सरदार पटेल: खेड़ा (1918) और बारडोली (1928) सत्याग्रह का नेतृत्व; बारडोली की महिलाओं द्वारा 'सरदार' उपाधि", "type": "leaf"},
                {"label": "मोतीलाल नेहरू: नेहरू रिपोर्ट (1928) तैयार करने वाली समिति के अध्यक्ष, जो पहला भारतीय संवैधानिक ढांचा था", "type": "leaf"},
                {"label": "देशबंधु सी.आर. दास: गया अधिवेशन (1922) के अध्यक्ष; कलकत्ता के मेयर; स्वराज पार्टी के सह-संस्थापक", "type": "leaf"},
                {"label": "लाला लाजपत राय: शेर-ए-पंजाब; AITUC (1920) के प्रथम अध्यक्ष; साइंटिफिक कमीशन के विरोध में शहीद", "type": "leaf"}]}
        ]
    },
    "montague-chelmsford-reforms-1919": {
        "en": [
            {"label": "Provincial Dyarchy", "type": "branch", "date": "1919 Act", "children": [
                {"label": "Reserved subjects: Administered by Governor & Executive Council (Finance, Land Revenue, Police)", "type": "leaf"},
                {"label": "Transferred subjects: Administered by Ministers responsible to Legislative Council (Education, Health)", "type": "leaf"}]},
            {"label": "Central Legislature", "type": "branch", "date": "Center", "children": [
                {"label": "Bicameral legislature introduced: Council of State (Upper) and Legislative Assembly (Lower)", "type": "leaf"},
                {"label": "Communal representation extended to Sikhs, Anglo-Indians, and Europeans; franchise expanded", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रांतीय द्वैध शासन", "type": "branch", "date": "1919 का एक्ट", "children": [
                {"label": "आरक्षित विषय: गवर्नर और उसकी कार्यकारी परिषद द्वारा शासित (वित्त, भू-राजस्व, पुलिस)", "type": "leaf"},
                {"label": "हस्तांतरित विषय: विधायी परिषद के प्रति उत्तरदायी मंत्रियों द्वारा शासित (शिक्षा, स्वास्थ्य)", "type": "leaf"}]},
            {"label": "केंद्रीय विधानमंडल", "type": "branch", "date": "केंद्र", "children": [
                {"label": "द्विसदनीय विधायिका की शुरुआत: राज्य परिषद (उच्च सदन) और विधानसभा (निम्न सदन)", "type": "leaf"},
                {"label": "सांप्रदायिक प्रतिनिधित्व का सिखों, एंग्लो-इंडियंस और यूरोपीय लोगों तक विस्तार; मताधिकार बढ़ाया गया", "type": "leaf"}]}
        ]
    },
    "nehru-report-1928": {
        "en": [
            {"label": "Key Proposals", "type": "branch", "date": "Nehru Report", "children": [
                {"label": "Drafted by Motilal Nehru committee to answer Lord Birkenhead's challenge on consensus", "type": "leaf"},
                {"label": "Demanded Dominion Status; joint electorates with reservation for minorities instead of separate electorates", "type": "leaf"},
                {"label": "Proposed 19 fundamental rights (universal suffrage), linguistic provinces, secular state", "type": "leaf"}]},
            {"label": "Factions", "type": "branch", "date": "Oppositions", "children": [
                {"label": "Jawaharlal Nehru & Bose formed Independence for India League, rejecting Dominion Status for Poorna Swaraj", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य प्रस्ताव", "type": "branch", "date": "नेहरू रिपोर्ट", "children": [
                {"label": "भारतीयों में आम सहमति न होने की लॉर्ड बर्कनहेड की चुनौती का जवाब देने हेतु मोतीलाल नेहरू समिति द्वारा तैयार", "type": "leaf"},
                {"label": "डोमिनियन स्टेटस की मांग; पृथक निर्वाचन के बजाय अल्पसंख्यकों हेतु सीटों के आरक्षण के साथ संयुक्त निर्वाचन", "type": "leaf"},
                {"label": "19 मौलिक अधिकारों (सार्वभौमिक मताधिकार), भाषाई प्रांतों और धर्मनिरपेक्ष राज्य का प्रस्ताव", "type": "leaf"}]},
            {"label": "विरोधी गुट", "type": "branch", "date": "विरोध", "children": [
                {"label": "जवाहरलाल नेहरू और सुभाष बोस ने डोमिनियन स्टेटस का विरोध कर पूर्ण स्वराज हेतु 'इंडिपेंडेंस फॉर इंडिया लीग' बनाई", "type": "leaf"}]}
        ]
    },
    "non-cooperation-movement-1920-22": {
        "en": [
            {"label": "Provisions", "type": "branch", "date": "1920-1922", "children": [
                {"label": "Boycott of British schools, colleges, courts, foreign goods; surrender of titles", "type": "leaf"},
                {"label": "Promotion of Swadeshi, hand spinning (Charkha), Hindu-Muslim unity, abolition of untouchability", "type": "leaf"},
                {"label": "Tilak Swaraj Fund created, collecting over Rs 1 crore in a short span", "type": "leaf"}]},
            {"label": "Resolution", "type": "branch", "date": "Nagpur 1920", "children": [
                {"label": "Ratified at Nagpur session (Dec 1920) under C. Vijayaraghavachariar; goal became Swaraj through peaceful means", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रावधान", "type": "branch", "date": "1920-1922", "children": [
                {"label": "सरकारी स्कूलों, कॉलेजों, न्यायालयों, विदेशी वस्तुओं का बहिष्कार; सरकारी उपाधियों का त्याग", "type": "leaf"},
                {"label": "स्वदेशी को बढ़ावा, चरखा कताई, हिंदू-मुस्लिम एकता, अस्पृश्यता निवारण", "type": "leaf"},
                {"label": "तिलक स्वराज फंड का गठन, जिसने अल्प समय में 1 करोड़ रुपये से अधिक एकत्रित किए", "type": "leaf"}]},
            {"label": "प्रस्ताव", "type": "branch", "date": "नागपुर 1920", "children": [
                {"label": "नागपुर अधिवेशन (दिसंबर 1920) में सी. विजयाराघवाचार्य की अध्यक्षता में अनुमोदित; लक्ष्य शांतिपूर्ण तरीकों से स्वराज हुआ", "type": "leaf"}]}
        ]
    },
    "rowlatt-satyagraha-and-jallianwala-bagh-massacre-april-13-1919": {
        "en": [
            {"label": "Rowlatt Act", "type": "branch", "date": "1919 Act", "children": [
                {"label": "Anarchical and Revolutionary Crimes Act 1919 allowed detention of political suspects without trial for 2 years", "type": "leaf"},
                {"label": "Gandhi formed Satyagraha Sabha; called for countrywide strike on April 6, 1919", "type": "leaf"}]},
            {"label": "Massacre", "type": "branch", "date": "April 13, 1919", "children": [
                {"label": "Arrest of Amritsar leaders Saifuddin Kitchlew & Satyapal triggered protests", "type": "leaf"},
                {"label": "Gen. Dyer ordered troops to open fire on unarmed gathering at Jallianwala Bagh on Baisakhi, killing hundreds", "type": "leaf"},
                {"label": "Rabindranath Tagore renounced Knighthood; Hunter Commission appointed for inquiry", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "रॉलेट एक्ट", "type": "branch", "date": "1919 का अधिनियम", "children": [
                {"label": "अराजक और क्रांतिकारी अपराध अधिनियम 1919 ने बिना मुकदमे के संदिग्धों को 2 साल तक कैद करने की अनुमति दी", "type": "leaf"},
                {"label": "गांधीजी ने सत्याग्रह सभा की स्थापना की; 6 अप्रैल 1919 को देशव्यापी हड़ताल का आह्वान किया", "type": "leaf"}]},
            {"label": "नरसंहार", "type": "branch", "date": "13 अप्रैल 1919", "children": [
                {"label": "अमृतसर के नेताओं सैफुद्दीन किचलू और सत्यपाल की गिरफ्तारी के बाद विरोध प्रदर्शन", "type": "leaf"},
                {"label": "जनरल डायर ने बैसाखी के दिन जलियांवाला बाग में निहत्थे जनसमूह पर गोलीबारी का आदेश दिया, जिसमें सैकड़ों मारे गए", "type": "leaf"},
                {"label": "रवींद्रनाथ टैगोर ने नाइटहुड (सर) की उपाधि का त्याग किया; जांच हेतु हंटर आयोग नियुक्त", "type": "leaf"}]}
        ]
    },
    "the-constructive-programme": {
        "en": [
            {"label": "Pillars", "type": "branch", "date": "Constructive Work", "children": [
                {"label": "Khadi & Village Industries: Promoted economic self-reliance and boycotted foreign goods", "type": "leaf"},
                {"label": "Harijan Upliftment: Campaign against untouchability and for social equality", "type": "leaf"},
                {"label": "National Education: Setting up Vidyapeeths independent of government control", "type": "leaf"},
                {"label": "Significance: Kept nationalist workers engaged during inactive phases of movements", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य स्तंभ", "type": "branch", "date": "रचनात्मक कार्य", "children": [
                {"label": "खादी और ग्रामोद्योग: आर्थिक आत्मनिर्भरता को बढ़ावा दिया और विदेशी माल का बहिष्कार किया", "type": "leaf"},
                {"label": "हरिजन उत्थान: अस्पृश्यता के खिलाफ और सामाजिक समानता के लिए राष्ट्रव्यापी अभियान", "type": "leaf"},
                {"label": "राष्ट्रीय शिक्षा: सरकारी नियंत्रण से मुक्त विद्यापीठों और स्कूलों की स्थापना", "type": "leaf"},
                {"label": "महत्व: आंदोलनों के निष्क्रिय दौर में राष्ट्रवादी कार्यकर्ताओं और जनता को सक्रिय बनाए रखा", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "chauri-chaura-incident-5th-feb-1922": "chauri-chaura-incident-5th-feb-1922",
    "congress-khilafat-swaraj-party": "congress-khilafat-swaraj-party",
    "swarajists-and-no-changers": "congress-khilafat-swaraj-party",
    "gandhi-ji-in-india-1915-onwards": "gandhi-ji-in-india-1915-onwards",
    "gandhi-ji-in-south-africa-1894-1914": "gandhi-ji-in-south-africa-1894-1914",
    "highlight-ahmedabad-mill-strike-1918": "highlight-ahmedabad-mill-strike-1918",
    "highlight-champaran-satyagraha-1917": "highlight-champaran-satyagraha-1917",
    "highlight-kheda-satyagraha-1918": "highlight-kheda-satyagraha-1918",
    "inc-allahabad-address-1930": "inc-allahabad-address-1930",
    "inc-lahore-session-1929": "inc-lahore-session-1929",
    "indian-statutory-commission-simon-commission-1927": "indian-statutory-commission-simon-commission-1927",
    "jinnahs-fourteen-points-demand-1929": "jinnahs-fourteen-points-demand-1929",
    "khilafat-movement-1919-20": "khilafat-movement-1919-20",
    "leaders-in-this-phase-and-their-contribution": "leaders-in-this-phase-and-their-contribution",
    "montague-chelmsford-reforms-1919": "montague-chelmsford-reforms-1919",
    "nehru-report-1928": "nehru-report-1928",
    "non-cooperation-movement-1920-22": "non-cooperation-movement-1920-22",
    "rowlatt-satyagraha-and-jallianwala-bagh-massacre-april-13-1919": "rowlatt-satyagraha-and-jallianwala-bagh-massacre-april-13-1919",
    "the-constructive-programme": "the-constructive-programme"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "generic-topic")
    
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
