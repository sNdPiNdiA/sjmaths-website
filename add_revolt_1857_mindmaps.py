#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/The-Revolt-of-1857"

MINDMAP_DATA = {
    "causes-of-failure-of-the-revolt": {
        "en": [
            {"label": "Organization Issues", "type": "branch", "date": "1857", "children": [
                {"label": "Lack of unified planning, central coordination, and single military leadership among rebels", "type": "leaf"},
                {"label": "Sepoys were poorly equipped compared to British troops armed with Enfield rifles & electric telegraph network", "type": "leaf"}]},
            {"label": "Social Isolation", "type": "branch", "date": "1857", "children": [
                {"label": "Revolt remained localized; South India, Punjab, Rajputana, and Bengal remained largely peaceful", "type": "leaf"},
                {"label": "Princely states (Scindia, Holkar, Nizam) and educated middle class actively supported or remained loyal to the British", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संगठन की कमी", "type": "branch", "date": "1857", "children": [
                {"label": "विद्रोहियों में एकीकृत योजना, केंद्रीय समन्वय और एकल सैन्य नेतृत्व का पूर्ण अभाव था", "type": "leaf"},
                {"label": "इनफील्ड राइफलों और इलेक्ट्रिक टेलीग्राफ नेटवर्क से लैस ब्रिटिश सैनिकों की तुलना में सिपाही कमजोर थे", "type": "leaf"}]},
            {"label": "सामाजिक अलगाव", "type": "branch", "date": "1857", "children": [
                {"label": "विद्रोह स्थानीय रहा; दक्षिण भारत, पंजाब, राजपूताना और बंगाल बड़े पैमाने पर शांत रहे", "type": "leaf"},
                {"label": "देशी रियासतें (सिंधिया, होल्कर, निजाम) और शिक्षित मध्यम वर्ग ने अंग्रेजों का समर्थन किया या तटस्थ रहे", "type": "leaf"}]}
        ]
    },
    "changes-in-socio-cultural-stance": {
        "en": [
            {"label": "Policy Shift", "type": "branch", "date": "Post-1857", "children": [
                {"label": "British abandoned active social reform policy (e.g. Sati, widow remarriage) to avoid offending religious orthodoxy", "type": "leaf"},
                {"label": "Switched to patronizing conservative elements and feudal landlords to secure social stability", "type": "leaf"}]},
            {"label": "Divide & Rule", "type": "branch", "date": "Communal", "children": [
                {"label": "Adopted deliberate 'Divide and Rule' policy, systematically widening the Hindu-Muslim communal rift", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नीतिगत बदलाव", "type": "branch", "date": "1857 के बाद", "children": [
                {"label": "धार्मिक रूढ़िवादिता को नाराज करने से बचने के लिए अंग्रेजों ने सामाजिक सुधारों (जैसे सती, विधवा पुनर्विवाह) की नीति छोड़ दी", "type": "leaf"},
                {"label": "सामाजिक स्थिरता सुनिश्चित करने के लिए रूढ़िवादी तत्वों और सामंती जमींदारों को संरक्षण देना शुरू किया", "type": "leaf"}]},
            {"label": "फूट डालो और राज करो", "type": "branch", "date": "सांप्रदायिक", "children": [
                {"label": "जानबूझकर 'फूट डालो और राज करो' की नीति अपनाई, जिससे हिंदू-मुस्लिम सांप्रदायिक दरार को बढ़ावा मिला", "type": "leaf"}]}
        ]
    },
    "changes-in-the-army-peel-commission": {
        "en": [
            {"label": "Army Reorganization", "type": "branch", "date": "Peel Commission", "children": [
                {"label": "Peel Commission (1857) set up to restructure the army; increased ratio of European soldiers", "type": "leaf"},
                {"label": "Set European-to-Indian ratio at 1:2 in Bengal and 1:3 in Madras and Bombay presidencies", "type": "leaf"},
                {"label": "Monopolized artillery branches exclusively for European troops; disbanded native artillery units", "type": "leaf"},
                {"label": "Shifted recruitment away from Awadh/Bihar to Gurkhas, Sikhs, and Pathans ('martial races' concept)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सेना का पुनर्गठन", "type": "branch", "date": "पील आयोग", "children": [
                {"label": "सेना के पुनर्गठन हेतु पील आयोग (1857) गठित; यूरोपीय सैनिकों के अनुपात में वृद्धि की गई", "type": "leaf"},
                {"label": "बंगाल में यूरोपीय से भारतीय सैनिक अनुपात 1:2 और मद्रास व बॉम्बे प्रेसीडेंसी में 1:3 निर्धारित किया", "type": "leaf"},
                {"label": "तोपखाने की शाखाओं पर केवल यूरोपीय सैनिकों का एकाधिकार किया; देशी तोपखाना इकाइयों को भंग किया", "type": "leaf"},
                {"label": "अवध/बिहार से भर्ती कम कर गोरखा, सिख और पठानों ('मार्शल रेस' की अवधारणा) की भर्ती शुरू की", "type": "leaf"}]}
        ]
    },
    "foreign-policy": {
        "en": [
            {"label": "Imperial Defense", "type": "branch", "date": "Foreign Policy", "children": [
                {"label": "Post-1857 foreign policy was guided by defending the Indian empire and securing British trade interests", "type": "leaf"},
                {"label": "Pushed territorial borders to natural geographic frontiers (Afghan buffer state policy, Burmese annexations)", "type": "leaf"},
                {"label": "Avoided entanglements in European wars while maintaining supremacy in the Indian Ocean & Suez route", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "साम्राज्यवादी रक्षा", "type": "branch", "date": "विदेश नीति", "children": [
                {"label": "1857 के बाद की विदेश नीति भारतीय साम्राज्य की रक्षा और ब्रिटिश व्यापारिक हितों को सुरक्षित करने से निर्देशित थी", "type": "leaf"},
                {"label": "क्षेत्रीय सीमाओं को प्राकृतिक भौगोलिक सीमाओं तक बढ़ाया (अफगान बफर स्टेट नीति, बर्मा का विलय)", "type": "leaf"},
                {"label": "हिंद महासागर और स्वेज मार्ग में अपना दबदबा बनाए रखते हुए यूरोपीय युद्धों में शामिल होने से परहेज किया", "type": "leaf"}]}
        ]
    },
    "foreign-policy-post-1857": {
        "en": [
            {"label": "Buffer States", "type": "branch", "date": "Post-1857 Policy", "children": [
                {"label": "Focused on creating protective buffer states around India's northern borders to counter Russian expansion", "type": "leaf"},
                {"label": "Forward policy implemented in Baluchistan and Afghanistan; Tibetan expedition led by Younghusband (1904)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "बफर राज्य", "type": "branch", "date": "1857 के बाद की नीति", "children": [
                {"label": "रूसी विस्तार का मुकाबला करने के लिए भारत की उत्तरी सीमाओं के चारों ओर सुरक्षात्मक बफर राज्य बनाने पर ध्यान केंद्रित किया", "type": "leaf"},
                {"label": "बलूचिस्तान और अफगानिस्तान में फॉरवर्ड नीति लागू की गई; यंगहसबैंड के नेतृत्व में तिब्बती अभियान (1904)", "type": "leaf"}]}
        ]
    },
    "important-british-officers-during-suppression-of-revolt": {
        "en": [
            {"label": "Key Commanders", "type": "branch", "date": "Suppression", "children": [
                {"label": "John Nicholson: Led British assault and siege of Delhi; died of wounds during the battle", "type": "leaf"},
                {"label": "Colin Campbell: Commander-in-Chief; suppressed revolt at Kanpur and Lucknow", "type": "leaf"},
                {"label": "Hugh Rose: Led campaigns in Central India; captured Jhansi and defeated Rani Laxmibai", "type": "leaf"},
                {"label": "William Taylor: Suppressed the uprisings in Arrah and Bihar region against Kunwar Singh", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख सेनापति", "type": "branch", "date": "दमन", "children": [
                {"label": "जॉन निकोलसन: दिल्ली पर ब्रिटिश हमले और घेराबंदी का नेतृत्व किया; युद्ध के दौरान घावों से मृत्यु हुई", "type": "leaf"},
                {"label": "कॉलिन कैंपबेल: कमांडर-इन-चीफ; कानपुर और लखनऊ में विद्रोह का क्रूरता से दमन किया", "type": "leaf"},
                {"label": "ह्यू रोज़: मध्य भारत में अभियानों का नेतृत्व किया; झांसी पर कब्जा किया और रानी लक्ष्मीबाई को हराया", "type": "leaf"},
                {"label": "William Taylor: कुंवर सिंह के खिलाफ आरा और बिहार क्षेत्र में विद्रोह को दबाया", "type": "leaf"}]}
        ]
    },
    "important-places-and-associated-leaders-of-the-revolt": {
        "en": [
            {"label": "Centers & Rebels", "type": "branch", "date": "1857 Centers", "children": [
                {"label": "Delhi: Bahadur Shah Zafar (titular emperor), General Bakht Khan (actual military leader)", "type": "leaf"},
                {"label": "Kanpur: Nana Sahib (Peshwa Baji Rao II's adopted son), Tantia Tope, Azimullah Khan", "type": "leaf"},
                {"label": "Lucknow: Begum Hazrat Mahal (on behalf of minor son Birjis Qadr)", "type": "leaf"},
                {"label": "Bihar (Jagdishpur): Kunwar Singh (80-year-old landlord) and his brother Amar Singh", "type": "leaf"},
                {"label": "Faizabad: Maulvi Ahmadullah; Bareilly: Khan Bahadur Khan", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "केंद्र और विद्रोही", "type": "branch", "date": "1857 के केंद्र", "children": [
                {"label": "दिल्ली: Bahadur Shah Zafar (नाममात्र के सम्राट), General Bakht Khan (वास्तविक सैन्य नेता)", "type": "leaf"},
                {"label": "कानपूर: Nana Sahib (पेशवा बाजीराव द्वितीय के दत्तक पुत्र), Tantia Tope, Azimullah Khan", "type": "leaf"},
                {"label": "लखनऊ: Begum Hazrat Mahal (अपने अल्पवयस्क पुत्र बिरजिस काद्र की ओर से)", "type": "leaf"},
                {"label": "बिहार (जगदीशपुर): Kunwar Singh (80 वर्षीय जमींदार) और उनके भाई Amar Singh", "type": "leaf"},
                {"label": "Faizabad: Maulvi Ahmadullah; Bareilly: Khan Bahadur Khan", "type": "leaf"}]}
        ]
    },
    "labour-law-related-changes": {
        "en": [
            {"label": "Factory Acts", "type": "branch", "date": "Labour reforms", "children": [
                {"label": "Indian Factories Act 1881 (Lord Ripon): First act; restricted employment of children under 7; max 9 hours work for children under 12", "type": "leaf"},
                {"label": "Indian Factories Act 1891: Provided weekly holiday; restricted female work hours to 11 per day", "type": "leaf"},
                {"label": "Enacted under pressure from British textile manufacturers wishing to curb Indian competitive advantage", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कारखाना अधिनियम", "type": "branch", "date": "श्रम सुधार", "children": [
                {"label": "भारतीय कारखाना अधिनियम 1881 (लॉर्ड रिपन): पहला अधिनियम; 7 वर्ष से कम उम्र के बच्चों के रोजगार पर प्रतिबंध; 12 वर्ष से कम के बच्चों हेतु अधिकतम 9 घंटे कार्य", "type": "leaf"},
                {"label": "भारतीय कारखाना अधिनियम 1891: साप्ताहिक अवकाश प्रदान किया; महिलाओं हेतु कार्य के घंटे प्रति दिन 11 तक सीमित किए", "type": "leaf"},
                {"label": "भारतीय वस्त्र उद्योग की प्रतिस्पर्धात्मक क्षमता को कम करने की इच्छा रखने वाले ब्रिटिश निर्माताओं के दबाव में पारित", "type": "leaf"}]}
        ]
    },
    "local-government-goi-act-1935-and-after": {
        "en": [
            {"label": "Provincial Subject", "type": "branch", "date": "1935 Act", "children": [
                {"label": "Local self-government was marked as a provincial subject; provincial autonomy allowed expansion of local board activities", "type": "leaf"},
                {"label": "Democratized municipal bodies and reduced official interventions; increased elected representatives", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रांतीय विषय", "type": "branch", "date": "1935 का अधिनियम", "children": [
                {"label": "स्थानीय स्वशासन को प्रांतीय सूची में रखा गया; प्रांतीय स्वायत्तता ने स्थानीय बोर्डों की गतिविधियों के विस्तार की अनुमति दी", "type": "leaf"},
                {"label": "नगरपालिका निकायों का लोकतंत्रीकरण किया और सरकारी हस्तक्षेप को कम किया; निर्वाचित प्रतिनिधियों की संख्या बढ़ाई", "type": "leaf"}]}
        ]
    },
    "local-government-mayos-resolution": {
        "en": [
            {"label": "Financial Decentralization", "type": "branch", "date": "Mayo 1870", "children": [
                {"label": "Lord Mayo's Resolution (1870) initiated financial decentralization by transferring local interest services", "type": "leaf"},
                {"label": "Transferred education, sanitation, and roads to provinces, giving first real impetus to municipal administration", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "वित्तीय विकेंद्रीकरण", "type": "branch", "date": "मेयो 1870", "children": [
                {"label": "लॉर्ड मेयो के प्रस्ताव (1870) ने स्थानीय हित की सेवाओं को स्थानांतरित करके वित्तीय विकेंद्रीकरण की शुरुआत की", "type": "leaf"},
                {"label": "शिक्षा, स्वच्छता और सड़कों को प्रांतों को हस्तांतरित किया, जिससे नगरपालिका प्रशासन को पहला वास्तविक प्रोत्साहन मिला", "type": "leaf"}]}
        ]
    },
    "local-government-resolution-of-may-1918-and-dyarchy-1919": {
        "en": [
            {"label": "Dyarchy Phase", "type": "branch", "date": "1919", "children": [
                {"label": "Local self-government became a Transferred Subject under Indian ministers in the provinces under Dyarchy", "type": "leaf"},
                {"label": "Faced severe financial shortage because finance remained a Reserved Subject under British control", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "द्वैध शासन चरण", "type": "branch", "date": "1919", "children": [
                {"label": "स्थानीय स्वशासन द्वैध शासन के तहत प्रांतों में भारतीय मंत्रियों के अधीन एक हस्तांतरित विषय बन गया", "type": "leaf"},
                {"label": "गंभीर वित्तीय कमी का सामना करना पड़ा क्योंकि वित्त विभाग ब्रिटिश नियंत्रण के अधीन एक आरक्षित विषय था", "type": "leaf"}]}
        ]
    },
    "local-government-resolution-of-may-and-dyarchy": {
        "en": [
            {"label": "Local Boards", "type": "branch", "date": "May 1918", "children": [
                {"label": "Re-emphasized the importance of making local boards representative bodies rather than bureaucratic wings", "type": "leaf"},
                {"label": "Proposed reducing official members and expanding the elective franchise for municipal bodies", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थानीय बोर्ड", "type": "branch", "date": "मई 1918", "children": [
                {"label": "स्थानीय बोर्डों को नौकरशाही शाखाओं के बजाय प्रतिनिधि निकाय बनाने के महत्व पर पुनः बल दिया", "type": "leaf"},
                {"label": "सरकारी सदस्यों को कम करने और नगरपालिका निकायों के लिए चुनावी मताधिकार का विस्तार करने का प्रस्ताव रखा", "type": "leaf"}]}
        ]
    },
    "local-government-ripons-resolution": {
        "en": [
            {"label": "Magna Carta of Local Gov", "type": "branch", "date": "1882", "children": [
                {"label": "Lord Ripon's Resolution (1882) recommended establishing district boards with non-official majority", "type": "leaf"},
                {"label": "Advocated local bodies as instruments of political education rather than administrative efficiency", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थानीय स्वशासन का मैग्ना कार्टा", "type": "branch", "date": "1882", "children": [
                {"label": "लॉर्ड रिपन के प्रस्ताव (1882) ने गैर-सरकारी बहुमत वाले जिला बोर्डों की स्थापना की सिफारिश की", "type": "leaf"},
                {"label": "स्थानीय निकायों को प्रशासनिक दक्षता के बजाय राजनीतिक शिक्षा के उपकरणों के रूप में वकालत की", "type": "leaf"}]}
        ]
    },
    "local-government-ripons-resolution-1882": {
        "en": [
            {"label": "Non-Official Chairpersons", "type": "branch", "date": "Ripon 1882", "children": [
                {"label": "Recommended that local boards be chaired by non-officials wherever possible instead of government officers", "type": "leaf"},
                {"label": "Laid the foundation for modern urban and rural self-government systems in India", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "गैर-सरकारी अध्यक्ष", "type": "branch", "date": "रिपन 1882", "children": [
                {"label": "सिफारिश की कि जहां तक संभव हो स्थानीय बोर्डों की अध्यक्षता सरकारी अधिकारियों के बजाय गैर-सरकारी लोगों द्वारा की जाए", "type": "leaf"},
                {"label": "भारत में आधुनिक शहरी और ग्रामीण स्वशासन प्रणालियों की आधारशिला रखी", "type": "leaf"}]}
        ]
    },
    "local-government-royal-commission-on-decentralization": {
        "en": [
            {"label": "Decentralization Inquiry", "type": "branch", "date": "1908", "children": [
                {"label": "Royal Commission examined financial and administrative relations between central and provincial governments", "type": "leaf"},
                {"label": "Recommended establishing village panchayats with executive and financial powers to manage local disputes", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विकेंद्रीकरण जांच", "type": "branch", "date": "1908", "children": [
                {"label": "रॉयल कमीशन ने केंद्रीय और प्रांतीय सरकारों के बीच वित्तीय और प्रशासनिक संबंधों की जांच की", "type": "leaf"},
                {"label": "स्थानीय विवादों के प्रबंधन के लिए कार्यकारी और वित्तीय शक्तियों के साथ ग्राम पंचायतों की स्थापना की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "local-government-royal-commission-on-decentralization-1908": {
        "en": [
            {"label": "Hobhouse Commission", "type": "branch", "date": "1908 Report", "children": [
                {"label": "Chaired by C.E.H. Hobhouse; pointed out that the lack of village-level organizations weakened local government", "type": "leaf"},
                {"label": "Urged the government to revitalize the local panchayat system as the foundation of rural administration", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "हॉबहाउस आयोग", "type": "branch", "date": "1908 की रिपोर्ट", "children": [
                {"label": "सी.ई.एच. हॉबहाउस की अध्यक्षता में; बताया कि ग्राम-स्तर के संगठनों की कमी ने स्थानीय सरकार को कमजोर किया है", "type": "leaf"},
                {"label": "सरकार से ग्रामीण प्रशासन की नींव के रूप में स्थानीय पंचायत प्रणाली को पुनर्जीवित करने का आग्रह किया", "type": "leaf"}]}
        ]
    },
    "nature-and-impact-of-the-revolt": {
        "en": [
            {"label": "Nature of 1857", "type": "branch", "date": "Revolt Nature", "children": [
                {"label": "British Historians: Characterized as a mere 'Sepoy Mutiny' driven by grease cartridge grievance", "type": "leaf"},
                {"label": "V.D. Savarkar: First to call it 'The Indian War of Independence 1857' in his 1909 book", "type": "leaf"},
                {"label": "RC Majumdar: Stated it was 'neither First, nor National, nor a War of Independence'", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "1857 का स्वरूप", "type": "branch", "date": "विद्रोह का स्वरूप", "children": [
                {"label": "ब्रिटिश इतिहासकार: इसे केवल चर्बी वाले कारतूस के मुद्दे से उत्पन्न 'सिपाही विद्रोह' के रूप में देखा", "type": "leaf"},
                {"label": "वी.डी. सावरकर: अपनी 1909 की पुस्तक में इसे पहली बार '1857 का भारतीय स्वतंत्रता समर' कहा", "type": "leaf"},
                {"label": "आर.सी. मजूमदार: कहा कि यह 'न तो प्रथम, न ही राष्ट्रीय और न ही स्वतंत्रता संग्राम था'", "type": "leaf"}]}
        ]
    },
    "policy-of-equal-federation": {
        "en": [
            {"label": "Equal Federation Policy", "type": "branch", "date": "Post-1935", "children": [
                {"label": "Aimed to link British provinces and princely states in a federal assembly under the 1935 Act", "type": "leaf"},
                {"label": "Princely states wanted to maintain paramountcy ties directly with the Crown rather than a future Indian legislature", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "समान संघ की नीति", "type": "branch", "date": "1935 के बाद", "children": [
                {"label": "1935 के अधिनियम के तहत ब्रिटिश प्रांतों और रियासतों को एक संघीय सभा में जोड़ने का लक्ष्य रखा गया था", "type": "leaf"},
                {"label": "रियासतें भविष्य की भारतीय विधायिका के बजाय सीधे क्राउन के साथ सर्वोच्चता के संबंध बनाए रखना चाहती थीं", "type": "leaf"}]}
        ]
    },
    "princely-states": {
        "en": [
            {"label": "Princely Policy", "type": "branch", "date": "Loyalty", "children": [
                {"label": "Doctrine of Lapse withdrawn; adoption rights of native rulers officially recognized", "type": "leaf"},
                {"label": "Native states treated as 'breakwaters in the storm' to prevent future mass uprisings", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "रियासतों के प्रति नीति", "type": "branch", "date": "वफादारी", "children": [
                {"label": "व्यपगत का सिद्धांत (हड़प नीति) वापस लिया; देशी शासकों के दत्तक अधिकारों को आधिकारिक मान्यता मिली", "type": "leaf"},
                {"label": "भविष्य के जन विद्रोहों को रोकने के लिए देशी रियासतों को 'तूफान में बांध' (ब्रेकवाटर्स) के रूप में माना गया", "type": "leaf"}]}
        ]
    },
    "public-services-ilbert-bill-controversy": {
        "en": [
            {"label": "Ilbert Bill Controversy", "type": "branch", "date": "1883", "children": [
                {"label": "Ilbert Bill introduced under Ripon to allow Indian sessions judges to try European offenders in criminal cases", "type": "leaf"},
                {"label": "Met with fierce resistance from Anglo-Indian community ('White Mutiny') claiming racial superiority", "type": "leaf"},
                {"label": "Compromise: European offenders given right to be tried by jury containing at least 50% Europeans", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "इल्बर्ट बिल विवाद", "type": "branch", "date": "1883", "children": [
                {"label": "लॉर्ड रिपन के समय भारतीय न्यायाधीशों को यूरोपीय अपराधियों के मुकदमों की सुनवाई का अधिकार देने हेतु इल्बर्ट बिल लाया गया", "type": "leaf"},
                {"label": "नस्लीय श्रेष्ठता का दावा करने वाले एंग्लो-इंडियन समुदाय द्वारा तीव्र विरोध ('श्वेत विद्रोह') किया गया", "type": "leaf"},
                {"label": "समझौता: यूरोपीय अपराधियों को ऐसी जूरी द्वारा परीक्षण का अधिकार मिला जिसमें कम से कम 50% सदस्य यूरोपीय हों", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-causes-administrative-causes": {
        "en": [
            {"label": "Administrative Causes", "type": "branch", "date": "1857 Causes", "children": [
                {"label": "Loss of jobs for Indian administrative elites; exclusion of Indians from high-level posts", "type": "leaf"},
                {"label": "Corruption at lower levels of administration (police, petty courts) alienated the common people", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रशासनिक कारण", "type": "branch", "date": "1857 के कारण", "children": [
                {"label": "भारतीय प्रशासनिक अभिजात वर्ग के लिए नौकरियों का नुकसान; भारतीयों को उच्च पदों से बाहर रखा जाना", "type": "leaf"},
                {"label": "प्रशासन के निचले स्तरों (पुलिस, छोटी अदालतों) में भ्रष्टाचार ने आम लोगों को अलग-थलग कर दिया", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-causes-discontent-among-sepoys": {
        "en": [
            {"label": "Sepoy Grievances", "type": "branch", "date": "1857 Causes", "children": [
                {"label": "General Service Enlistment Act 1856: Mandated overseas service crossing black waters (Kala Pani)", "type": "leaf"},
                {"label": "Greased Cartridges: Introduction of Enfield rifle with cartridges greased with cow/pig fat", "type": "leaf"},
                {"label": "Discriminatory pay and promotion policies compared to European counterparts", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सिपाहियों का असंतोष", "type": "branch", "date": "1857 के कारण", "children": [
                {"label": "सामान्य सेवा भर्ती अधिनियम 1856: समुद्र पार यात्रा (काला पानी) को अनिवार्य किया, जो धार्मिक नियमों के विरुद्ध थी", "type": "leaf"},
                {"label": "चर्बी वाले कारतूस: गाय और सुअर की चर्बी से लिन कारतूसों वाली इनफील्ड राइफल का आगमन", "type": "leaf"},
                {"label": "यूरोपीय सैनिकों की तुलना में भेदभावपूर्ण वेतन और पदोन्नति की नीतियां", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-causes-economic-causes": {
        "en": [
            {"label": "Economic Ruin", "type": "branch", "date": "1857 Causes", "children": [
                {"label": "Heavy land revenue systems (Zamindari, Ryotwari) led to peasant indebtedness and loss of lands", "type": "leaf"},
                {"label": "Destruction of traditional handicrafts and weavers due to discriminatory British tariff policies", "type": "leaf"},
                {"label": "De-industrialization of India transformed the country into a mere raw material exporter", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आर्थिक तबाही", "type": "branch", "date": "1857 के कारण", "children": [
                {"label": "अत्यधिक भू-राजस्व प्रणालियों (जमींदारी, रैयतवाड़ी) ने किसानों को कर्ज में डुबोया और उनकी जमीनें छीन लीं", "type": "leaf"},
                {"label": "भेदभावपूर्ण ब्रिटिश टैरिफ नीतियों के कारण पारंपरिक हस्तशिल्प और बुनकरों का विनाश हुआ", "type": "leaf"},
                {"label": "भारत के वि-औद्योगिकीकरण ने देश को केवल कच्चे माल के निर्यातक में बदल दिया", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-causes-influence-of-outside-events": {
        "en": [
            {"label": "Outside Events", "type": "branch", "date": "1857 Causes", "children": [
                {"label": "British defeats in First Afghan War (1838-42), Punjab Wars (1845-49), and Crimean War (1854-56)", "type": "leaf"},
                {"label": "Shattered the myth of British invincibility, encouraging Indian rebels to rise up", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "बाहरी घटनाओं का प्रभाव", "type": "branch", "date": "1857 के कारण", "children": [
                {"label": "प्रथम अफगान युद्ध (1838-42), पंजाब युद्धों (1845-49) और क्रीमिया युद्ध (1854-56) में ब्रिटिश सेना की हार", "type": "leaf"},
                {"label": "ब्रिटिश सेना के अजेय होने के भ्रम को तोड़ा, जिससे भारतीय विद्रोहियों को उठ खड़े होने का प्रोत्साहन मिला", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-causes-political-causes": {
        "en": [
            {"label": "Political Annexations", "type": "branch", "date": "1857 Causes", "children": [
                {"label": "Dalhousie's Doctrine of Lapse annexed Satara, Jhansi, Nagpur, Sambalpur, and Jaitpur", "type": "leaf"},
                {"label": "Annexation of Awadh (1856) on grounds of misgovernance deeply hurt the sepoys (mostly from Awadh)", "type": "leaf"},
                {"label": "Suspension of Peshwa pensions (Nana Sahib) and decision to strip Mughal titles angered elites", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजनीतिक विलय", "type": "branch", "date": "1857 के कारण", "children": [
                {"label": "डलहौजी की हड़प नीति (व्यपगत का सिद्धांत) के तहत सतारा, झांसी, नागपुर, संबलपुर और जैतपुर का विलय किया गया", "type": "leaf"},
                {"label": "कुशासन के आधार पर अवध का विलय (1856) सिपाहियों (मुख्य रूप से अवध से) के स्वाभिमान पर गहरा आघात था", "type": "leaf"},
                {"label": "पेशवा पेंशन (नाना साहब) का निलंबन और मुगल उपाधियों को समाप्त करने के निर्णय से कुलीन वर्ग में आक्रोश था", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-causes-socio-religious-causes": {
        "en": [
            {"label": "Socio-Religious Grievances", "type": "branch", "date": "1857 Causes", "children": [
                {"label": "Interference in traditional customs: Sati abolition (1829), Hindu Widow Remarriage Act (1856)", "type": "leaf"},
                {"label": "Aggressive activities of Christian missionaries supported by British officials created conversion fears", "type": "leaf"},
                {"label": "Religious Disabilities Act (1850) preserved inheritance rights after conversion, angered Hindus", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सामाजिक-धार्मिक शिकायतें", "type": "branch", "date": "1857 के कारण", "children": [
                {"label": "पारंपरिक रीति-रिवाजों में हस्तक्षेप: सती उन्मूलन (1829), हिंदू विधवा पुनर्विवाह अधिनियम (1856)", "type": "leaf"},
                {"label": "ब्रिटिश अधिकारियों द्वारा समर्थित ईसाई मिशनरियों की आक्रामक गतिविधियों से जबरन धर्म परिवर्तन का भय पैदा हुआ", "type": "leaf"},
                {"label": "धार्मिक अयोग्यता अधिनियम (1850) ने धर्म परिवर्तन के बाद भी पैतृक संपत्ति के अधिकार को सुरक्षित रखा, जिससे हिंदू नाराज हुए", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-events-fall-of-delhi": {
        "en": [
            {"label": "Delhi Captivity", "type": "branch", "date": "Sept 1857", "children": [
                {"label": "Bahadur Shah Zafar captured at Humayun's Tomb by Lieutenant Hodson", "type": "leaf"},
                {"label": "Hodson shot dead Zafar's sons and grandson at Delhi Gate (Khooni Darwaza)", "type": "leaf"},
                {"label": "Bahadur Shah Zafar put on trial and exiled to Rangoon (Burma) where he died in 1862", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दिल्ली का पतन", "type": "branch", "date": "सितंबर 1857", "children": [
                {"label": "बहादुर शाह जफर को लेफ्टिनेंट हडसन द्वारा हुमायूं के मकबरे से गिरफ्तार किया गया", "type": "leaf"},
                {"label": "हडसन ने दिल्ली गेट (खूनी दरवाजा) पर जफर के बेटों और पोते को गोली मार दी", "type": "leaf"},
                {"label": "बहादुर शाह जफर पर मुकदमा चलाया गया और उन्हें रंगून (बर्मा) निर्वासित किया गया जहां 1862 में उनकी मृत्यु हो गई", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-events-meerut-mutiny": {
        "en": [
            {"label": "Meerut Uprising", "type": "branch", "date": "May 10, 1857", "children": [
                {"label": "Sepoys at Meerut cantonment refused to touch greased cartridges, leading to court-martial & imprisonment", "type": "leaf"},
                {"label": "On May 10, remaining sepoys mutinied, killed officers, released prisoners, and marched to Delhi", "type": "leaf"},
                {"label": "Arrived in Delhi on May 11, setting off the nationwide rebellion against Company rule", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मेरठ का विद्रोह", "type": "branch", "date": "10 मई 1857", "children": [
                {"label": "मेरठ छावनी के सिपाहियों ने चर्बी वाले कारतूस छूने से इनकार कर दिया, जिससे उन्हें कोर्ट-मार्शल और जेल हुई", "type": "leaf"},
                {"label": "10 मई को शेष सिपाहियों ने विद्रोह कर दिया, अधिकारियों को मार डाला, कैदियों को छुड़ाया और दिल्ली कूच किया", "type": "leaf"},
                {"label": "11 मई को दिल्ली पहुंचे, जिससे कंपनी शासन के खिलाफ राष्ट्रव्यापी विद्रोह भड़क उठा", "type": "leaf"}]}
        ]
    },
    "revolt-of-1857-events-siege-of-delhi": {
        "en": [
            {"label": "Delhi Siege", "type": "branch", "date": "Summer 1857", "children": [
                {"label": "Rebels fortified Delhi; British forces besieged the city from the ridge outside", "type": "leaf"},
                {"label": "Recapture of Delhi led by John Nicholson (mortally wounded) and Archdale Wilson", "type": "leaf"},
                {"label": "City fell to the British in September 1857 after months of heavy casualties on both sides", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दिल्ली की घेराबंदी", "type": "branch", "date": "गर्मियां 1857", "children": [
                {"label": "विद्रोहियों ने दिल्ली की किलेबंदी की; ब्रिटिश सेना ने बाहर रिज (पहाड़ी) से शहर की घेराबंदी की", "type": "leaf"},
                {"label": "दिल्ली पर पुनः कब्जा करने का नेतृत्व जॉन निकोलसन (घातक रूप से घायल) और अर्चडेल विल्सन ने किया", "type": "leaf"},
                {"label": "दोनों पक्षों को भारी नुकसान होने के बाद सितंबर 1857 में शहर पर अंततः अंग्रेजों का नियंत्रण हुआ", "type": "leaf"}]}
        ]
    },
    "various-outcomes-of-the-revolt": {
        "en": [
            {"label": "Administrative outcomes", "type": "branch", "date": "1858 Act", "children": [
                {"label": "Government of India Act 1858: East India Company rule ended; power transferred to the Crown", "type": "leaf"},
                {"label": "Office of Secretary of State for India created with a 15-member advisory Council of India", "type": "leaf"},
                {"label": "Dual government system (Board of Control and Court of Directors) abolished", "type": "leaf"},
                {"label": "Viceroy promised to respect adoption rights and native states' territories (Queen's Proclamation)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रशासनिक परिणाम", "type": "branch", "date": "1858 का एक्ट", "children": [
                {"label": "भारत सरकार अधिनियम 1858: ईस्ट इंडिया कंपनी का शासन समाप्त; सत्ता ब्रिटिश क्राउन को हस्तांतरित", "type": "leaf"},
                {"label": "15 सदस्यीय सलाहकार परिषद (काउंसिल ऑफ इंडिया) के साथ भारत सचिव (Secretary of State) का पद बनाया", "type": "leaf"},
                {"label": "दोहरी सरकार प्रणाली (बोर्ड ऑफ कंट्रोल और कोर्ट ऑफ डायरेक्टर्स) को समाप्त कर दिया गया", "type": "leaf"},
                {"label": "वायसराय ने शासकों के दत्तक अधिकारों और देशी रियासतों के क्षेत्रों का सम्मान करने का वादा किया (महारानी का घोषणापत्र)", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "causes-of-failure-of-the-revolt": "causes-of-failure-of-the-revolt",
    "changes-in-socio-cultural-stance": "changes-in-socio-cultural-stance",
    "changes-in-the-army-peel-commission": "changes-in-the-army-peel-commission",
    "foreign-policy": "foreign-policy",
    "foreign-policy-post-1857": "foreign-policy-post-1857",
    "important-british-officers-during-suppression-of-revolt": "important-british-officers-during-suppression-of-revolt",
    "important-places-and-associated-leaders-of-the-revolt": "important-places-and-associated-leaders-of-the-revolt",
    "labour-law-related-changes": "labour-law-related-changes",
    "local-government-goi-act-1935-and-after": "local-government-goi-act-1935-and-after",
    "local-government-mayos-resolution": "local-government-mayos-resolution",
    "local-government-resolution-of-may-1918-and-dyarchy-1919": "local-government-resolution-of-may-1918-and-dyarchy-1919",
    "local-government-resolution-of-may-and-dyarchy": "local-government-resolution-of-may-and-dyarchy",
    "local-government-ripons-resolution": "local-government-ripons-resolution",
    "local-government-ripons-resolution-1882": "local-government-ripons-resolution-1882",
    "local-government-royal-commission-on-decentralization": "local-government-royal-commission-on-decentralization",
    "local-government-royal-commission-on-decentralization-1908": "local-government-royal-commission-on-decentralization-1908",
    "nature-and-impact-of-the-revolt": "nature-and-impact-of-the-revolt",
    "policy-of-equal-federation": "policy-of-equal-federation",
    "princely-states": "princely-states",
    "public-services-ilbert-bill-controversy": "public-services-ilbert-bill-controversy",
    "revolt-of-1857-causes-administrative-causes": "revolt-of-1857-causes-administrative-causes",
    "revolt-of-1857-causes-discontent-among-sepoys": "revolt-of-1857-causes-discontent-among-sepoys",
    "revolt-of-1857-causes-economic-causes": "revolt-of-1857-causes-economic-causes",
    "revolt-of-1857-causes-influence-of-outside-events": "revolt-of-1857-causes-influence-of-outside-events",
    "revolt-of-1857-causes-political-causes": "revolt-of-1857-causes-political-causes",
    "revolt-of-1857-causes-socio-religious-causes": "revolt-of-1857-causes-socio-religious-causes",
    "revolt-of-1857-events-fall-of-delhi": "revolt-of-1857-events-fall-of-delhi",
    "revolt-of-1857-events-meerut-mutiny": "revolt-of-1857-events-meerut-mutiny",
    "revolt-of-1857-events-siege-of-delhi": "revolt-of-1857-events-siege-of-delhi",
    "various-outcomes-of-the-revolt": "various-outcomes-of-the-revolt"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('GoI', 'GoI (Government of India)')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "causes-of-failure-of-the-revolt")
    
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
