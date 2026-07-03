#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Form-of-Administration-before-1857"

MINDMAP_DATA = {
    "british-indian-army": {
        "en": [
            {"label": "Structure & Composition", "type": "branch", "date": "Pre-1857 Army", "children": [
                {"label": "Three separate Presidency Armies: Bengal Army (largest), Bombay Army, Madras Army — each under its own Commander-in-Chief", "type": "leaf"},
                {"label": "Composed of European officers commanding Indian Sepoys; Europeans held all commissioned officer ranks", "type": "leaf"},
                {"label": "Bengal Army largely recruited from high-caste Brahmins and Rajputs of Awadh and Bihar", "type": "leaf"}]},
            {"label": "Recruitment Policy", "type": "branch", "date": "Pre-1857 Army", "children": [
                {"label": "Earlier relied heavily on Awadhi upper-caste soldiers; led to caste-based solidarity and collective grievances", "type": "leaf"},
                {"label": "General Service Enlistment Act 1856 (Lord Canning) mandated overseas service, violating caste norms", "type": "leaf"}]},
            {"label": "Post-1857 Reforms", "type": "branch", "date": "Pre-1857 Army", "children": [
                {"label": "Peel Commission (1858) reorganized army; artillery monopolized by Europeans; martial races theory adopted", "type": "leaf"},
                {"label": "Recruitment switched to Gurkhas, Sikhs, Pathans — deemed more loyal after 1857 revolt", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संरचना और संरचना", "type": "branch", "date": "1857 से पहले की सेना", "children": [
                {"label": "तीन अलग प्रेसीडेंसी सेनाएं: बंगाल सेना (सबसे बड़ी), बॉम्बे सेना, मद्रास सेना — प्रत्येक अपने कमांडर-इन-चीफ के अधीन", "type": "leaf"},
                {"label": "यूरोपीय अधिकारियों के नेतृत्व में भारतीय सिपाहियों से मिलकर बनी; यूरोपीयों के पास सभी कमीशन प्राप्त अधिकारी पद थे", "type": "leaf"},
                {"label": "बंगाल सेना मुख्य रूप से अवध और बिहार के उच्च जाति के ब्राह्मणों और राजपूतों से भर्ती की जाती थी", "type": "leaf"}]},
            {"label": "भर्ती नीति", "type": "branch", "date": "1857 से पहले की सेना", "children": [
                {"label": "पहले अवधी उच्च जाति के सैनिकों पर भारी निर्भरता थी; जाति-आधारित एकजुटता और सामूहिक शिकायतें पैदा हुईं", "type": "leaf"},
                {"label": "सामान्य सेवा भर्ती अधिनियम 1856 (लॉर्ड कैनिंग) ने विदेशी सेवा को अनिवार्य बनाया, जिससे जाति के नियमों का उल्लंघन हुआ", "type": "leaf"}]},
            {"label": "1857 के बाद के सुधार", "type": "branch", "date": "1857 से पहले की सेना", "children": [
                {"label": "पील आयोग (1858) ने सेना का पुनर्गठन किया; तोपखाना यूरोपीयों द्वारा एकाधिकार किया गया; 'मार्शल रेस' सिद्धांत अपनाया गया", "type": "leaf"},
                {"label": "1857 के विद्रोह के बाद अधिक वफादार समझे जाने वाले गोरखाओं, सिखों और पठानों की भर्ती शुरू हुई", "type": "leaf"}]}
        ]
    },
    "developments-of-civil-services": {
        "en": [
            {"label": "Origins under EIC", "type": "branch", "date": "Civil Services", "children": [
                {"label": "Initially servants of EIC involved in trade; gradually shifted to administrative roles with territorial acquisition", "type": "leaf"},
                {"label": "Lord Cornwallis (1786-93) separated revenue and commercial functions; banned private trade for civil servants", "type": "leaf"},
                {"label": "Cornwallis Code (1793): Established principle of rule of law and separated revenue, judicial, and commercial branches", "type": "leaf"}]},
            {"label": "Competitive Entry", "type": "branch", "date": "Civil Services", "children": [
                {"label": "Haileybury College (1806) established to train EIC civil servants with Indian language and administrative subjects", "type": "leaf"},
                {"label": "Charter Act 1853: Abolished patronage; introduced open competitive examinations for ICS appointments", "type": "leaf"}]},
            {"label": "Indian Exclusion", "type": "branch", "date": "Civil Services", "children": [
                {"label": "ICS exams held only in London with maximum age of 23; effectively excluded Indians from senior positions", "type": "leaf"},
                {"label": "Satyendranath Tagore (1863): First Indian to pass the ICS examination despite structural barriers", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "EIC के अंतर्गत उत्पत्ति", "type": "branch", "date": "सिविल सेवाएं", "children": [
                {"label": "शुरुआत में व्यापार में लगे EIC के सेवक थे; क्षेत्रीय अधिग्रहण के साथ धीरे-धीरे प्रशासनिक भूमिकाओं में बदल गए", "type": "leaf"},
                {"label": "लॉर्ड कॉर्नवालिस (1786-93) ने राजस्व और वाणिज्यिक कार्यों को अलग किया; सिविल सेवकों के लिए निजी व्यापार पर प्रतिबंध लगाया", "type": "leaf"},
                {"label": "कॉर्नवालिस कोड (1793): कानून के शासन का सिद्धांत स्थापित किया और राजस्व, न्यायिक और वाणिज्यिक शाखाओं को अलग किया", "type": "leaf"}]},
            {"label": "प्रतिस्पर्धी प्रवेश", "type": "branch", "date": "सिविल सेवाएं", "children": [
                {"label": "EIC के सिविल सेवकों को भारतीय भाषा और प्रशासनिक विषयों में प्रशिक्षित करने के लिए हेलीबरी कॉलेज (1806) की स्थापना", "type": "leaf"},
                {"label": "चार्टर अधिनियम 1853: संरक्षण समाप्त किया; ICS नियुक्तियों के लिए खुली प्रतियोगी परीक्षाएं शुरू कीं", "type": "leaf"}]},
            {"label": "भारतीयों का बहिष्कार", "type": "branch", "date": "सिविल सेवाएं", "children": [
                {"label": "ICS परीक्षाएं केवल लंदन में अधिकतम 23 वर्ष की आयु के साथ आयोजित होती थीं; भारतीयों को प्रभावी रूप से वरिष्ठ पदों से बाहर रखा गया", "type": "leaf"},
                {"label": "सत्येंद्रनाथ टैगोर (1863): संरचनात्मक बाधाओं के बावजूद ICS परीक्षा उत्तीर्ण करने वाले पहले भारतीय", "type": "leaf"}]}
        ]
    },
    "evolution-of-modern-judicial-system": {
        "en": [
            {"label": "Cornwallis Reforms", "type": "branch", "date": "Judicial Evolution", "children": [
                {"label": "Cornwallis separated executive and judiciary; District Collector lost his judicial powers over criminal cases", "type": "leaf"},
                {"label": "Established circuit courts for criminal cases and Sadar Nizamat Adalat as the apex criminal court", "type": "leaf"}]},
            {"label": "Bentinck's Reforms", "type": "branch", "date": "Judicial Evolution", "children": [
                {"label": "Abolished provincial courts of appeal and circuit courts (1829-33); delegated powers to District Collectors", "type": "leaf"},
                {"label": "Recombined offices of Magistrate and Collector; appointed Sadr Amins and Munsiffs as subordinate Indian judges", "type": "leaf"}]},
            {"label": "Law Commissions", "type": "branch", "date": "Judicial Evolution", "children": [
                {"label": "First Law Commission (1834-35): Chaired by Thomas Macaulay; recommended codification of Indian law", "type": "leaf"},
                {"label": "Indian Penal Code (IPC) drafted by Macaulay Commission but enacted only in 1860; CrPC codified in 1861", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कॉर्नवालिस के सुधार", "type": "branch", "date": "न्यायिक विकास", "children": [
                {"label": "कॉर्नवालिस ने कार्यपालिका और न्यायपालिका को अलग किया; जिला कलेक्टर ने आपराधिक मामलों पर अपनी न्यायिक शक्तियां खो दीं", "type": "leaf"},
                {"label": "आपराधिक मामलों के लिए सर्किट अदालतें और सर्वोच्च आपराधिक अदालत के रूप में सदर निजामत अदालत स्थापित की", "type": "leaf"}]},
            {"label": "बेंटिक के सुधार", "type": "branch", "date": "न्यायिक विकास", "children": [
                {"label": "प्रांतीय अपील अदालतें और सर्किट अदालतें समाप्त कीं (1829-33); जिला कलेक्टरों को अधिकार सौंपे", "type": "leaf"},
                {"label": "मजिस्ट्रेट और कलेक्टर के कार्यालयों को फिर से जोड़ा; सदर अमीनों और मुंसिफों को अधीनस्थ भारतीय न्यायाधीश नियुक्त किया", "type": "leaf"}]},
            {"label": "विधि आयोग", "type": "branch", "date": "न्यायिक विकास", "children": [
                {"label": "प्रथम विधि आयोग (1834-35): थॉमस मैकाले की अध्यक्षता में; भारतीय कानून के संहिताकरण की सिफारिश की", "type": "leaf"},
                {"label": "भारतीय दंड संहिता (IPC) मैकाले आयोग द्वारा तैयार की गई लेकिन 1860 में ही अधिनियमित हुई; CrPC 1861 में संहिताबद्ध हुई", "type": "leaf"}]}
        ]
    },
    "impact-of-british-administration": {
        "en": [
            {"label": "Positive Impacts", "type": "branch", "date": "Administrative Impact", "children": [
                {"label": "Unified legal system replacing arbitrary local customs; introduction of rule of law and equality before courts", "type": "leaf"},
                {"label": "Modern transportation (railways, telegraph, postal) and communication networks created national integration", "type": "leaf"},
                {"label": "Establishment of modern educational institutions and spread of English — basis of nationalist consciousness", "type": "leaf"}]},
            {"label": "Negative Impacts", "type": "branch", "date": "Administrative Impact", "children": [
                {"label": "Systematic de-industrialization: destruction of Indian crafts and handicrafts by cheap British imports", "type": "leaf"},
                {"label": "Drain of wealth through Home Charges, trade surplus, and railway guarantees depleted Indian capital", "type": "leaf"}]},
            {"label": "Institutional Legacy", "type": "branch", "date": "Administrative Impact", "children": [
                {"label": "Legacy institutions: ICS, legal codes (IPC, CrPC), organized police and army were inherited by independent India", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सकारात्मक प्रभाव", "type": "branch", "date": "प्रशासनिक प्रभाव", "children": [
                {"label": "मनमाने स्थानीय रीति-रिवाजों की जगह एकीकृत कानूनी प्रणाली; कानून के शासन और अदालतों में समानता की शुरुआत", "type": "leaf"},
                {"label": "आधुनिक परिवहन (रेलवे, टेलीग्राफ, डाक) और संचार नेटवर्क ने राष्ट्रीय एकीकरण बनाया", "type": "leaf"},
                {"label": "आधुनिक शैक्षणिक संस्थानों की स्थापना और अंग्रेजी का प्रसार — राष्ट्रवादी चेतना का आधार बना", "type": "leaf"}]},
            {"label": "नकारात्मक प्रभाव", "type": "branch", "date": "प्रशासनिक प्रभाव", "children": [
                {"label": "व्यवस्थित वि-औद्योगिकीकरण: सस्ते ब्रिटिश आयातों से भारतीय शिल्प और हस्तकला का विनाश", "type": "leaf"},
                {"label": "गृह प्रभारों, व्यापार अधिशेष और रेलवे गारंटियों से धन की निकासी ने भारतीय पूंजी को कम किया", "type": "leaf"}]},
            {"label": "संस्थागत विरासत", "type": "branch", "date": "प्रशासनिक प्रभाव", "children": [
                {"label": "विरासती संस्थाएं: ICS, कानूनी संहिताएं (IPC, CrPC), संगठित पुलिस और सेना स्वतंत्र भारत को विरासत में मिलीं", "type": "leaf"}]}
        ]
    },
    "judicial-system-law-commission": {
        "en": [
            {"label": "First Law Commission (1834)", "type": "branch", "date": "Law Commissions", "children": [
                {"label": "Chaired by Lord Macaulay; drafted the Indian Penal Code (IPC) and recommended a unified Civil Procedure Code", "type": "leaf"},
                {"label": "Recommended replacing differing Hindu and Muslim personal laws with a uniform civil code for non-religious matters", "type": "leaf"}]},
            {"label": "Subsequent Commissions", "type": "branch", "date": "Law Commissions", "children": [
                {"label": "Second (1853): Prepared Code of Civil Procedure; Third (1861): Criminal Procedure Code", "type": "leaf"},
                {"label": "Fourth Law Commission (1879-82): Resulted in Transfer of Property Act (1882) and Easements Act (1882)", "type": "leaf"}]},
            {"label": "Key Outcomes", "type": "branch", "date": "Law Commissions", "children": [
                {"label": "IPC (1860), CrPC (1861), Civil Procedure Code — formed the enduring backbone of Indian criminal and civil law", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम विधि आयोग (1834)", "type": "branch", "date": "विधि आयोग", "children": [
                {"label": "लॉर्ड मैकाले की अध्यक्षता में; भारतीय दंड संहिता (IPC) का मसौदा तैयार किया और एक एकीकृत सिविल प्रक्रिया संहिता की सिफारिश की", "type": "leaf"},
                {"label": "गैर-धार्मिक मामलों के लिए अलग-अलग हिंदू और मुस्लिम व्यक्तिगत कानूनों की जगह एक समान नागरिक संहिता की सिफारिश की", "type": "leaf"}]},
            {"label": "बाद के आयोग", "type": "branch", "date": "विधि आयोग", "children": [
                {"label": "दूसरा (1853): सिविल प्रक्रिया संहिता तैयार की; तीसरा (1861): आपराधिक प्रक्रिया संहिता तैयार की", "type": "leaf"},
                {"label": "चौथा विधि आयोग (1879-82): संपत्ति हस्तांतरण अधिनियम (1882) और सुखाधिकार अधिनियम (1882) का परिणाम रहा", "type": "leaf"}]},
            {"label": "प्रमुख परिणाम", "type": "branch", "date": "विधि आयोग", "children": [
                {"label": "IPC (1860), CrPC (1861), सिविल प्रक्रिया संहिता — भारतीय आपराधिक और दीवानी कानून की स्थायी रीढ़ बनी", "type": "leaf"}]}
        ]
    },
    "pitts-india-act": {
        "en": [
            {"label": "Background & Need", "type": "branch", "date": "1784", "children": [
                {"label": "Previous Regulating Act (1773) had failed to adequately control EIC's corrupt and arbitrary governance", "type": "leaf"},
                {"label": "Warren Hastings' trial and Bengal scandals made parliamentary oversight urgent for British government", "type": "leaf"}]},
            {"label": "Key Provisions", "type": "branch", "date": "1784", "children": [
                {"label": "Established a 'Board of Control' of 6 members (including Secretaries of State and Chancellor of Exchequer) for political supervision", "type": "leaf"},
                {"label": "Court of Directors retained commercial powers; political/military decisions needed Board of Control approval", "type": "leaf"},
                {"label": "Governor-General given sweeping override powers over other presidencies; war/treaty without London approval forbidden", "type": "leaf"}]},
            {"label": "Significance", "type": "branch", "date": "1784", "children": [
                {"label": "Created the 'double government' system that lasted until 1858; laid foundation for Parliamentary supremacy over India", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और आवश्यकता", "type": "branch", "date": "1784", "children": [
                {"label": "पिछला विनियमन अधिनियम (1773) EIC के भ्रष्ट और मनमाने शासन को पर्याप्त रूप से नियंत्रित करने में विफल रहा था", "type": "leaf"},
                {"label": "वारेन हेस्टिंग्स के मुकदमे और बंगाल घोटालों ने ब्रिटिश सरकार के लिए संसदीय निगरानी को जरूरी बना दिया", "type": "leaf"}]},
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1784", "children": [
                {"label": "राजनीतिक पर्यवेक्षण के लिए 6 सदस्यों का 'बोर्ड ऑफ कंट्रोल' (राज्य सचिव और चांसलर ऑफ एक्सचेकर सहित) स्थापित किया", "type": "leaf"},
                {"label": "कोर्ट ऑफ डायरेक्टर्स ने वाणिज्यिक शक्तियां बनाए रखीं; राजनीतिक/सैन्य निर्णयों के लिए बोर्ड ऑफ कंट्रोल की मंजूरी जरूरी थी", "type": "leaf"},
                {"label": "गवर्नर-जनरल को अन्य प्रेसीडेंसियों पर व्यापक ओवरराइड शक्तियां दी गईं; लंदन की मंजूरी के बिना युद्ध/संधि वर्जित की", "type": "leaf"}]},
            {"label": "महत्व", "type": "branch", "date": "1784", "children": [
                {"label": "1858 तक चली 'दोहरी सरकार' प्रणाली बनाई; भारत पर संसदीय सर्वोच्चता की नींव रखी", "type": "leaf"}]}
        ]
    },
    "regulating-act": {
        "en": [
            {"label": "Background", "type": "branch", "date": "1773", "children": [
                {"label": "First Parliamentary intervention in EIC affairs; triggered by Bengal Famine (1770) and EIC's financial crisis", "type": "leaf"},
                {"label": "EIC had to request a £1.4 million loan from the British government, making Parliamentary oversight unavoidable", "type": "leaf"}]},
            {"label": "Key Provisions", "type": "branch", "date": "1773", "children": [
                {"label": "Bengal Governor made 'Governor-General of Bengal' with a 4-member Executive Council — first step towards centralized authority", "type": "leaf"},
                {"label": "Supreme Court established at Calcutta (1774) with a Chief Justice (Sir Elijah Impey) and 3 puisne judges", "type": "leaf"},
                {"label": "Governors of Bombay and Madras became subordinate to the Governor-General of Bengal", "type": "leaf"}]},
            {"label": "Shortcomings", "type": "branch", "date": "1773", "children": [
                {"label": "Governor-General could be overruled by his own Council — led to deadlock during Warren Hastings' tenure", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि", "type": "branch", "date": "1773", "children": [
                {"label": "EIC मामलों में पहला संसदीय हस्तक्षेप; बंगाल अकाल (1770) और EIC के वित्तीय संकट से उत्प्रेरित", "type": "leaf"},
                {"label": "EIC को ब्रिटिश सरकार से £14 लाख का ऋण मांगना पड़ा, जिससे संसदीय निगरानी अनिवार्य हो गई", "type": "leaf"}]},
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1773", "children": [
                {"label": "बंगाल के गवर्नर को 4 सदस्यीय कार्यकारी परिषद के साथ 'गवर्नर-जनरल ऑफ बंगाल' बनाया — केंद्रीकृत प्राधिकरण की दिशा में पहला कदम", "type": "leaf"},
                {"label": "कलकत्ता में सर्वोच्च न्यायालय (1774) की स्थापना मुख्य न्यायाधीश (सर एलिजा इम्पी) और 3 न्यायाधीशों के साथ की गई", "type": "leaf"},
                {"label": "बॉम्बे और मद्रास के गवर्नर बंगाल के गवर्नर-जनरल के अधीनस्थ हो गए", "type": "leaf"}]},
            {"label": "कमियां", "type": "branch", "date": "1773", "children": [
                {"label": "गवर्नर-जनरल को उसकी अपनी परिषद द्वारा ओवरराइड किया जा सकता था — वारेन हेस्टिंग्स के कार्यकाल के दौरान गतिरोध पैदा हुआ", "type": "leaf"}]}
        ]
    },
    "the-charter-acts": {
        "en": [
            {"label": "Charter Act 1793", "type": "branch", "date": "Charter Acts", "children": [
                {"label": "Extended EIC's monopoly for 20 years; gave Governor-General overriding powers over Council", "type": "leaf"},
                {"label": "Provided that Company's commercial and territorial revenues be kept separate; home charges codified", "type": "leaf"}]},
            {"label": "Charter Act 1813", "type": "branch", "date": "Charter Acts", "children": [
                {"label": "EIC's trade monopoly ended except tea and China trade; India opened to private British merchants", "type": "leaf"},
                {"label": "Rs 1 lakh allocated annually for promoting education and local literature; missionary activities allowed", "type": "leaf"}]},
            {"label": "Charter Act 1833", "type": "branch", "date": "Charter Acts", "children": [
                {"label": "EIC's commercial trading functions ended; became purely an administrative body governing India on behalf of Crown", "type": "leaf"},
                {"label": "Governor-General of Bengal became Governor-General of India; Laws to be uniform across India", "type": "leaf"}]},
            {"label": "Charter Act 1853", "type": "branch", "date": "Charter Acts", "children": [
                {"label": "Open competitive examination for ICS; Legislative Council separated from Executive Council — first step towards legislature", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "चार्टर अधिनियम 1793", "type": "branch", "date": "चार्टर अधिनियम", "children": [
                {"label": "EIC का एकाधिकार 20 वर्षों के लिए बढ़ाया; गवर्नर-जनरल को परिषद पर ओवरराइडिंग शक्तियां दी गईं", "type": "leaf"},
                {"label": "कंपनी के वाणिज्यिक और क्षेत्रीय राजस्व को अलग रखने का प्रावधान; गृह प्रभार संहिताबद्ध किए गए", "type": "leaf"}]},
            {"label": "चार्टर अधिनियम 1813", "type": "branch", "date": "चार्टर अधिनियम", "children": [
                {"label": "चाय और चीन व्यापार को छोड़कर EIC का व्यापार एकाधिकार समाप्त; भारत निजी ब्रिटिश व्यापारियों के लिए खुला", "type": "leaf"},
                {"label": "शिक्षा और स्थानीय साहित्य को बढ़ावा देने के लिए सालाना 1 लाख रुपये आवंटित; मिशनरी गतिविधियों की अनुमति दी", "type": "leaf"}]},
            {"label": "चार्टर अधिनियम 1833", "type": "branch", "date": "चार्टर अधिनियम", "children": [
                {"label": "EIC के वाणिज्यिक व्यापार कार्य समाप्त हुए; क्राउन की ओर से भारत पर शासन करने वाली विशुद्ध प्रशासनिक संस्था बन गई", "type": "leaf"},
                {"label": "बंगाल के गवर्नर-जनरल को भारत का गवर्नर-जनरल बनाया; पूरे भारत में कानून एकसमान होने की बात कही गई", "type": "leaf"}]},
            {"label": "चार्टर अधिनियम 1853", "type": "branch", "date": "चार्टर अधिनियम", "children": [
                {"label": "ICS के लिए खुली प्रतियोगी परीक्षा; विधान परिषद को कार्यकारी परिषद से अलग किया — विधायिका की दिशा में पहला कदम", "type": "leaf"}]}
        ]
    },
    "the-dual-system": {
        "en": [
            {"label": "Clive's Dual System", "type": "branch", "date": "1765-1772", "children": [
                {"label": "Established by Robert Clive after Battle of Buxar (1764) and Treaty of Allahabad (1765)", "type": "leaf"},
                {"label": "EIC held Diwani (revenue collection rights) over Bengal, Bihar, Orissa from Mughal Emperor Shah Alam II", "type": "leaf"},
                {"label": "Nawab retained Nizamat (administrative and judicial authority) but with no revenue to sustain it", "type": "leaf"}]},
            {"label": "Failures", "type": "branch", "date": "1765-1772", "children": [
                {"label": "EIC collected revenues but refused to bear administrative expenses — caused severe administrative breakdown", "type": "leaf"},
                {"label": "Great Bengal Famine of 1770: killed 1/3 of Bengal's population; EIC continued grain exports even during famine", "type": "leaf"}]},
            {"label": "Abolition", "type": "branch", "date": "1772", "children": [
                {"label": "Warren Hastings abolished dual system in 1772; EIC took direct charge of revenue and civil administration", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "क्लाइव की दोहरी प्रणाली", "type": "branch", "date": "1765-1772", "children": [
                {"label": "बक्सर के युद्ध (1764) और इलाहाबाद की संधि (1765) के बाद रॉबर्ट क्लाइव द्वारा स्थापित", "type": "leaf"},
                {"label": "EIC ने मुगल सम्राट शाह आलम द्वितीय से बंगाल, बिहार, उड़ीसा पर दीवानी (राजस्व संग्रह अधिकार) प्राप्त की", "type": "leaf"},
                {"label": "नवाब ने निजामत (प्रशासनिक और न्यायिक प्राधिकरण) बनाए रखा लेकिन उसे बनाए रखने के लिए कोई राजस्व नहीं था", "type": "leaf"}]},
            {"label": "विफलताएं", "type": "branch", "date": "1765-1772", "children": [
                {"label": "EIC ने राजस्व एकत्र किया लेकिन प्रशासनिक खर्च वहन करने से इनकार किया — गंभीर प्रशासनिक टूटन का कारण बना", "type": "leaf"},
                {"label": "1770 का महान बंगाल अकाल: बंगाल की 1/3 आबादी की मृत्यु; अकाल के दौरान भी EIC अनाज का निर्यात जारी रखा", "type": "leaf"}]},
            {"label": "उन्मूलन", "type": "branch", "date": "1772", "children": [
                {"label": "वारेन हेस्टिंग्स ने 1772 में दोहरी प्रणाली को समाप्त किया; EIC ने राजस्व और नागरिक प्रशासन का सीधा प्रभार लिया", "type": "leaf"}]}
        ]
    }
}

MINDMAP_MAPPINGS = {
    "british-indian-army": "british-indian-army",
    "developments-of-civil-services": "developments-of-civil-services",
    "evolution-of-modern-judicial-system": "evolution-of-modern-judicial-system",
    "impact-of-british-administration": "impact-of-british-administration",
    "judicial-system-law-commission": "judicial-system-law-commission",
    "pitts-india-act": "pitts-india-act",
    "regulating-act": "regulating-act",
    "the-charter-acts": "the-charter-acts",
    "the-dual-system": "the-dual-system"
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
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, "regulating-act")

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
