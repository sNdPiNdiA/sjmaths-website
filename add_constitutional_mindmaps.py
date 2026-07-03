#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Constitutional-Development-In-India"

MINDMAP_DATA = {
    "charter-act-of-1793": {
        "en": [
            {"label": "Key Provisions", "type": "branch", "date": "1793", "children": [
                {"label": "Extended EIC's trade monopoly for 20 more years; renewed the company's charter to operate in India and Asia", "type": "leaf"},
                {"label": "Governor-General given overriding powers over his own Council — resolved the deadlock problem of the 1773 Act", "type": "leaf"},
                {"label": "Salaries of the Board of Control members to be paid from Indian revenues — first time Indian revenue used for British administrative costs", "type": "leaf"},
                {"label": "Command of the Indian army firmly vested in Governor-General rather than shared with Commanders-in-Chief of Presidencies", "type": "leaf"}
            ]},
            {"label": "Administrative Changes", "type": "branch", "date": "1793", "children": [
                {"label": "Cornwallis Code implemented under this Act: Permanent Settlement with zamindars (1793); fixed land revenue for zamindars permanently", "type": "leaf"},
                {"label": "Separated revenue and judicial functions at district level; banned civil servants from private trade; raised their salaries instead", "type": "leaf"},
                {"label": "ICS covenanted service established — all senior civil servants required to sign a covenant (contract) with EIC", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "1793", "children": [
                {"label": "Established rule of law principles in Bengal administration; set template for subsequent Charter Acts", "type": "leaf"},
                {"label": "Permanent Settlement with zamindars created a loyal landlord class — long-term political consequence for Bengal till independence", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1793", "children": [
                {"label": "EIC के व्यापार एकाधिकार को 20 वर्षों के लिए बढ़ाया; भारत और एशिया में कंपनी के चार्टर को नवीनीकृत किया", "type": "leaf"},
                {"label": "गवर्नर-जनरल को अपनी परिषद पर ओवरराइडिंग शक्तियां दी गईं — 1773 के अधिनियम की गतिरोध समस्या हल", "type": "leaf"},
                {"label": "बोर्ड ऑफ कंट्रोल के सदस्यों के वेतन भारतीय राजस्व से देय — पहली बार भारतीय राजस्व का ब्रिटिश प्रशासनिक लागतों के लिए उपयोग", "type": "leaf"},
                {"label": "भारतीय सेना की कमान गवर्नर-जनरल को दृढ़ता से सौंपी — प्रेसीडेंसियों के कमांडर-इन-चीफ के साथ साझा करने की बजाय", "type": "leaf"}
            ]},
            {"label": "प्रशासनिक बदलाव", "type": "branch", "date": "1793", "children": [
                {"label": "इस अधिनियम के तहत कॉर्नवालिस कोड लागू: जमींदारों के साथ स्थायी बंदोबस्त (1793); जमींदारों के लिए भूमि राजस्व स्थायी रूप से निर्धारित", "type": "leaf"},
                {"label": "जिला स्तर पर राजस्व और न्यायिक कार्यों को अलग किया; सिविल सेवकों के निजी व्यापार पर प्रतिबंध; उनके वेतन बढ़ाए", "type": "leaf"},
                {"label": "ICS अनुबंध सेवा स्थापित — सभी वरिष्ठ सिविल सेवकों को EIC के साथ एक अनुबंध (कॉवनेंट) पर हस्ताक्षर करना आवश्यक", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1793", "children": [
                {"label": "बंगाल प्रशासन में कानून के शासन के सिद्धांत स्थापित किए; बाद के चार्टर अधिनियमों के लिए टेम्पलेट तैयार किया", "type": "leaf"},
                {"label": "जमींदारों के साथ स्थायी बंदोबस्त ने एक वफादार जमींदार वर्ग बनाया — स्वतंत्रता तक बंगाल के लिए दीर्घकालिक राजनीतिक परिणाम", "type": "leaf"}
            ]}
        ]
    },
    "charter-act-of-1813": {
        "en": [
            {"label": "End of Trade Monopoly", "type": "branch", "date": "1813", "children": [
                {"label": "Ended EIC's monopoly over Indian trade (except tea and China trade); India opened to all British private merchants", "type": "leaf"},
                {"label": "Context: Industrial Revolution in Britain; British manufacturers demanded open Indian markets for their cotton goods — EIC monopoly was obstacle", "type": "leaf"},
                {"label": "EIC retained the China trade monopoly and continued as political administrator of India; lost commercial trading character", "type": "leaf"}
            ]},
            {"label": "Education & Religion", "type": "branch", "date": "1813", "children": [
                {"label": "Rs 1 lakh annually allocated for 'revival and improvement of literature and encouragement of learned natives' — first state education grant in India", "type": "leaf"},
                {"label": "Christian missionaries allowed to enter and preach in India — reversing earlier EIC policy of barring missionaries to avoid conflict", "type": "leaf"},
                {"label": "Debate: Orientalists vs Anglicists on how to spend education funds (Sanskrit/Persian vs English) — resolved by Macaulay's Minute 1835", "type": "leaf"}
            ]},
            {"label": "Administrative Impact", "type": "branch", "date": "1813", "children": [
                {"label": "Crown's sovereignty over British Indian territories explicitly asserted — EIC acknowledged as agent of the Crown, not independent sovereign", "type": "leaf"},
                {"label": "Opening of trade sparked rapid growth of British commercial presence in India; Indian textile industry faced increasing competition", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "व्यापार एकाधिकार का अंत", "type": "branch", "date": "1813", "children": [
                {"label": "भारतीय व्यापार पर EIC का एकाधिकार समाप्त (चाय और चीन व्यापार छोड़कर); भारत सभी ब्रिटिश निजी व्यापारियों के लिए खुला", "type": "leaf"},
                {"label": "संदर्भ: ब्रिटेन में औद्योगिक क्रांति; ब्रिटिश निर्माताओं ने अपने सूती माल के लिए खुले भारतीय बाजारों की मांग की — EIC एकाधिकार बाधा था", "type": "leaf"},
                {"label": "EIC ने चीन व्यापार एकाधिकार बनाए रखा और भारत के राजनीतिक प्रशासक के रूप में जारी रहा; वाणिज्यिक व्यापारिक चरित्र खो दिया", "type": "leaf"}
            ]},
            {"label": "शिक्षा और धर्म", "type": "branch", "date": "1813", "children": [
                {"label": "'साहित्य के पुनरुद्धार और सुधार तथा विद्वान भारतीयों को प्रोत्साहन' के लिए 1 लाख रु. वार्षिक — भारत में पहला राज्य शिक्षा अनुदान", "type": "leaf"},
                {"label": "ईसाई मिशनरियों को भारत में प्रवेश और उपदेश देने की अनुमति — पहले की EIC नीति उलटी जो संघर्ष से बचने के लिए मिशनरियों को रोकती थी", "type": "leaf"},
                {"label": "बहस: ओरिएंटलिस्ट बनाम एंग्लिसिस्ट पर शिक्षा निधि कैसे खर्च करें (संस्कृत/फारसी बनाम अंग्रेजी) — मैकाले के मिनट 1835 से हल", "type": "leaf"}
            ]},
            {"label": "प्रशासनिक प्रभाव", "type": "branch", "date": "1813", "children": [
                {"label": "ब्रिटिश भारतीय क्षेत्रों पर क्राउन की संप्रभुता स्पष्ट रूप से जताई — EIC को स्वतंत्र संप्रभु नहीं बल्कि क्राउन का एजेंट माना गया", "type": "leaf"},
                {"label": "व्यापार खुलने से भारत में ब्रिटिश वाणिज्यिक उपस्थिति में तेजी से वृद्धि हुई; भारतीय कपड़ा उद्योग को बढ़ती प्रतिस्पर्धा का सामना", "type": "leaf"}
            ]}
        ]
    },
    "charter-act-of-1833": {
        "en": [
            {"label": "End of EIC as Commercial Body", "type": "branch", "date": "1833", "children": [
                {"label": "EIC's China trade monopoly and tea trade monopoly abolished; EIC ceased to be a trading body altogether — became purely administrative", "type": "leaf"},
                {"label": "EIC to pay dividends to shareholders at 10.5% from Indian revenues — shareholders compensated for losing commercial profits", "type": "leaf"},
                {"label": "Governor-General of Bengal became Governor-General of India — first time a single authority for all of British India created", "type": "leaf"}
            ]},
            {"label": "Legislative Centralisation", "type": "branch", "date": "1833", "children": [
                {"label": "Governor-General's Council given supreme legislative authority for all of British India; Bombay and Madras Councils lost legislative powers", "type": "leaf"},
                {"label": "4th member (Law Member) added to Governor-General's Executive Council — Macaulay appointed as first Law Member (1834)", "type": "leaf"},
                {"label": "First Law Commission established (1834-35) under Macaulay to codify Indian laws — led to IPC (1860), CrPC (1861)", "type": "leaf"}
            ]},
            {"label": "Indian Representation", "type": "branch", "date": "1833", "children": [
                {"label": "Declared that 'no native of British India shall be disabled from holding any office by reason of religion, birth, descent or colour' — theoretical equality", "type": "leaf"},
                {"label": "Actual implementation blocked by patronage system and practical barriers; Satyendranath Tagore (1863) first Indian to pass ICS", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "EIC का व्यावसायिक संस्था के रूप में अंत", "type": "branch", "date": "1833", "children": [
                {"label": "EIC का चीन व्यापार और चाय व्यापार एकाधिकार समाप्त; EIC पूरी तरह एक व्यापारिक निकाय बनना बंद हुआ — विशुद्ध प्रशासनिक बना", "type": "leaf"},
                {"label": "EIC को भारतीय राजस्व से शेयरधारकों को 10.5% लाभांश देना था — वाणिज्यिक लाभ खोने के लिए शेयरधारकों को मुआवजा", "type": "leaf"},
                {"label": "बंगाल के गवर्नर-जनरल को भारत के गवर्नर-जनरल का पद मिला — पहली बार सम्पूर्ण ब्रिटिश भारत के लिए एकल प्राधिकरण बना", "type": "leaf"}
            ]},
            {"label": "विधायी केंद्रीकरण", "type": "branch", "date": "1833", "children": [
                {"label": "गवर्नर-जनरल की परिषद को सम्पूर्ण ब्रिटिश भारत के लिए सर्वोच्च विधायी अधिकार दिया; बॉम्बे और मद्रास परिषदों ने विधायी शक्तियां खोईं", "type": "leaf"},
                {"label": "गवर्नर-जनरल की कार्यकारी परिषद में चौथा सदस्य (विधि सदस्य) जोड़ा — मैकाले पहले विधि सदस्य नियुक्त (1834)", "type": "leaf"},
                {"label": "भारतीय कानूनों को संहिताबद्ध करने के लिए मैकाले के तहत प्रथम विधि आयोग (1834-35) स्थापित — IPC (1860), CrPC (1861) का आधार", "type": "leaf"}
            ]},
            {"label": "भारतीय प्रतिनिधित्व", "type": "branch", "date": "1833", "children": [
                {"label": "घोषित किया कि 'ब्रिटिश भारत का कोई भी निवासी धर्म, जन्म, वंश या रंग के कारण किसी पद से वंचित नहीं होगा' — सैद्धांतिक समानता", "type": "leaf"},
                {"label": "संरक्षण प्रणाली और व्यावहारिक बाधाओं से वास्तविक क्रियान्वयन रोका गया; सत्येंद्रनाथ टैगोर (1863) ICS पास करने वाले पहले भारतीय", "type": "leaf"}
            ]}
        ]
    },
    "charter-act-of-1853": {
        "en": [
            {"label": "Key Provisions", "type": "branch", "date": "1853", "children": [
                {"label": "No fixed term given to EIC's renewed charter — Parliament could revoke it at any time; effectively EIC on probation as India's administrator", "type": "leaf"},
                {"label": "Open competitive examination for ICS appointments (replacing patronage/nomination); exam held in London — still practically excluded Indians", "type": "leaf"},
                {"label": "Legislative Council enlarged: 6 additional members from provincial governments added — first step towards separate legislature", "type": "leaf"}
            ]},
            {"label": "Separation of Powers", "type": "branch", "date": "1853", "children": [
                {"label": "Legislative Council separated from Executive Council for first time — Governor-General's Council split into distinct legislative and executive wings", "type": "leaf"},
                {"label": "Legislative Council functioned like a mini-Parliament: introduced bills, debated legislation; but no elected members or popular representation", "type": "leaf"},
                {"label": "This structural separation was a precursor to the Legislative Council system under Indian Councils Acts of 1861, 1892, 1909", "type": "leaf"}
            ]},
            {"label": "Historical Context", "type": "branch", "date": "1853", "children": [
                {"label": "Last Charter Act before 1857 revolt; only 4 years later EIC was abolished by Government of India Act 1858", "type": "leaf"},
                {"label": "Satyendranath Tagore used the new ICS examination system (1863) to become the first Indian to pass — despite the London location barrier", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1853", "children": [
                {"label": "EIC के नवीनीकृत चार्टर को कोई निश्चित अवधि नहीं दी — संसद इसे कभी भी रद्द कर सकती थी; प्रभावी रूप से EIC परिवीक्षा पर भारत का प्रशासक", "type": "leaf"},
                {"label": "ICS नियुक्तियों के लिए खुली प्रतियोगी परीक्षा (संरक्षण/नामांकन की जगह); लंदन में परीक्षा — फिर भी व्यावहारिक रूप से भारतीयों को बाहर रखा", "type": "leaf"},
                {"label": "विधान परिषद विस्तारित: प्रांतीय सरकारों से 6 अतिरिक्त सदस्य जोड़े — अलग विधायिका की दिशा में पहला कदम", "type": "leaf"}
            ]},
            {"label": "शक्तियों का पृथक्करण", "type": "branch", "date": "1853", "children": [
                {"label": "पहली बार विधान परिषद को कार्यकारी परिषद से अलग किया — गवर्नर-जनरल की परिषद विशिष्ट विधायी और कार्यकारी विंग में विभाजित", "type": "leaf"},
                {"label": "विधान परिषद ने एक मिनी-संसद की तरह कार्य किया: विधेयक पेश किए, कानून पर बहस की; लेकिन कोई निर्वाचित सदस्य या लोकप्रिय प्रतिनिधित्व नहीं", "type": "leaf"},
                {"label": "यह संरचनात्मक पृथक्करण 1861, 1892, 1909 के भारतीय परिषद अधिनियमों के तहत विधान परिषद प्रणाली का अग्रदूत था", "type": "leaf"}
            ]},
            {"label": "ऐतिहासिक संदर्भ", "type": "branch", "date": "1853", "children": [
                {"label": "1857 विद्रोह से पहले अंतिम चार्टर अधिनियम; केवल 4 वर्ष बाद भारत सरकार अधिनियम 1858 द्वारा EIC समाप्त", "type": "leaf"},
                {"label": "सत्येंद्रनाथ टैगोर ने नई ICS परीक्षा प्रणाली (1863) का उपयोग पास करने वाले पहले भारतीय बनने के लिए किया — लंदन स्थान की बाधा के बावजूद", "type": "leaf"}
            ]}
        ]
    },
    "government-of-india-act-1858": {
        "en": [
            {"label": "Abolition of EIC", "type": "branch", "date": "1858", "children": [
                {"label": "EIC (East India Company) abolished; Crown took direct control of India; British Government assumed the empire", "type": "leaf"},
                {"label": "Board of Control and Court of Directors abolished; replaced by Secretary of State for India + 15-member India Council in London", "type": "leaf"},
                {"label": "Secretary of State for India had full authority over Indian affairs; first Secretary of State was Lord Stanley", "type": "leaf"}
            ]},
            {"label": "New Governance Structure", "type": "branch", "date": "1858", "children": [
                {"label": "Governor-General renamed Viceroy — direct representative of the Crown; Lord Canning became first Viceroy (1858-62)", "type": "leaf"},
                {"label": "Queen's Proclamation (November 1858): Promised to respect Indian treaties, customs, and rights of adoption for rulers; equality for all subjects", "type": "leaf"},
                {"label": "ICS covenanted service continued; all EIC officers retained their positions under direct Crown service", "type": "leaf"}
            ]},
            {"label": "Political Significance", "type": "branch", "date": "1858", "children": [
                {"label": "India directly under British Parliament for first time; ended 100-year EIC experiment; began true Crown Raj period (1858-1947)", "type": "leaf"},
                {"label": "Queen's Proclamation renounced doctrine of Lapse; guaranteed religious freedom — responses to 1857 revolt's causes", "type": "leaf"},
                {"label": "Indirect effect: Began the policy of 'divide and rule' more systematically — consolidating Muslim and Hindu interests separately", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "EIC का उन्मूलन", "type": "branch", "date": "1858", "children": [
                {"label": "EIC (ईस्ट इंडिया कंपनी) समाप्त; क्राउन ने भारत का प्रत्यक्ष नियंत्रण लिया; ब्रिटिश सरकार ने साम्राज्य ग्रहण किया", "type": "leaf"},
                {"label": "बोर्ड ऑफ कंट्रोल और कोर्ट ऑफ डायरेक्टर्स समाप्त; लंदन में भारत के राज्य सचिव + 15-सदस्यीय इंडिया काउंसिल द्वारा प्रतिस्थापित", "type": "leaf"},
                {"label": "भारत के राज्य सचिव को भारतीय मामलों पर पूर्ण अधिकार था; पहले राज्य सचिव लॉर्ड स्टेनली थे", "type": "leaf"}
            ]},
            {"label": "नई शासन संरचना", "type": "branch", "date": "1858", "children": [
                {"label": "गवर्नर-जनरल का नाम बदलकर वायसराय — क्राउन का प्रत्यक्ष प्रतिनिधि; लॉर्ड कैनिंग पहले वायसराय बने (1858-62)", "type": "leaf"},
                {"label": "रानी की उद्घोषणा (नवंबर 1858): भारतीय संधियों, रीति-रिवाजों और शासकों के गोद लेने के अधिकारों का सम्मान करने का वादा; सभी प्रजा के लिए समानता", "type": "leaf"},
                {"label": "ICS अनुबंध सेवा जारी रही; सभी EIC अधिकारियों ने सीधे क्राउन सेवा के तहत अपने पद बनाए रखे", "type": "leaf"}
            ]},
            {"label": "राजनीतिक महत्व", "type": "branch", "date": "1858", "children": [
                {"label": "पहली बार भारत सीधे ब्रिटिश संसद के अधीन; 100 वर्षीय EIC प्रयोग समाप्त; वास्तविक क्राउन राज काल शुरू (1858-1947)", "type": "leaf"},
                {"label": "रानी की उद्घोषणा ने व्यपगत सिद्धांत त्यागा; धार्मिक स्वतंत्रता की गारंटी दी — 1857 विद्रोह के कारणों के प्रति प्रतिक्रिया", "type": "leaf"},
                {"label": "अप्रत्यक्ष प्रभाव: 'फूट डालो और राज करो' नीति को अधिक व्यवस्थित रूप से शुरू किया — मुस्लिम और हिंदू हितों को अलग-अलग मजबूत करना", "type": "leaf"}
            ]}
        ]
    },
    "government-of-india-act-1919": {
        "en": [
            {"label": "Montagu-Chelmsford Reforms", "type": "branch", "date": "1919", "children": [
                {"label": "Based on Montagu-Chelmsford Report (1918); Edwin Montagu (Secretary of State) and Lord Chelmsford (Viceroy) authored the reforms", "type": "leaf"},
                {"label": "Announced objective: 'increasing association of Indians in every branch of the administration and the gradual development of self-governing institutions'", "type": "leaf"},
                {"label": "Context: Lucknow Pact (1916) showed Congress-League unity; Home Rule Movement; Montagu's August Declaration (1917) promising responsible government", "type": "leaf"}
            ]},
            {"label": "Dyarchy System", "type": "branch", "date": "1919", "children": [
                {"label": "Dyarchy introduced at provincial level: subjects divided into 'reserved' (law, finance, police — with Governor) and 'transferred' (education, health, local bodies — with Indian ministers)", "type": "leaf"},
                {"label": "Central Legislature bicameral: Council of State (upper) and Legislative Assembly (lower); limited franchise (3% of population could vote)", "type": "leaf"},
                {"label": "Communal electorates expanded beyond Muslims; now included Sikhs, Christians, Anglo-Indians, Europeans — entrenched communal representation", "type": "leaf"}
            ]},
            {"label": "Significance & Criticism", "type": "branch", "date": "1919", "children": [
                {"label": "Dyarchy criticised as 'unworkable' — Indian ministers given responsibility without resources; revenue and police stayed with Governor", "type": "leaf"},
                {"label": "Simon Commission (1927) appointed to review; Congress boycotted it as no Indians included; 'Simon Go Back' protests", "type": "leaf"},
                {"label": "Act came alongside Rowlatt Act (1919) and Jallianwala Bagh massacre — contradicted reform spirit; fuelled Non-Cooperation Movement", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मोंटेगु-चेम्सफोर्ड सुधार", "type": "branch", "date": "1919", "children": [
                {"label": "मोंटेगु-चेम्सफोर्ड रिपोर्ट (1918) पर आधारित; एडविन मोंटेगु (राज्य सचिव) और लॉर्ड चेम्सफोर्ड (वायसराय) ने सुधार तैयार किए", "type": "leaf"},
                {"label": "घोषित उद्देश्य: 'प्रशासन की हर शाखा में भारतीयों की बढ़ती भागीदारी और स्व-शासी संस्थाओं का क्रमिक विकास'", "type": "leaf"},
                {"label": "संदर्भ: लखनऊ समझौता (1916) ने कांग्रेस-लीग एकता दिखाई; होम रूल आंदोलन; मोंटेगु की अगस्त घोषणा (1917) जिम्मेदार सरकार का वादा", "type": "leaf"}
            ]},
            {"label": "द्वैध शासन प्रणाली", "type": "branch", "date": "1919", "children": [
                {"label": "प्रांतीय स्तर पर द्वैध शासन: विषयों को 'आरक्षित' (कानून, वित्त, पुलिस — गवर्नर के साथ) और 'हस्तांतरित' (शिक्षा, स्वास्थ्य, स्थानीय निकाय — भारतीय मंत्रियों के साथ) में बांटा", "type": "leaf"},
                {"label": "केंद्रीय विधायिका द्विसदनीय: राज्य परिषद (उच्च) और विधान सभा (निम्न); सीमित मताधिकार (3% जनसंख्या मत दे सकती थी)", "type": "leaf"},
                {"label": "सांप्रदायिक निर्वाचन क्षेत्र मुसलमानों से आगे बढ़ाए; अब सिख, ईसाई, एंग्लो-इंडियन, यूरोपीय शामिल — सांप्रदायिक प्रतिनिधित्व जड़ें जमाई", "type": "leaf"}
            ]},
            {"label": "महत्व और आलोचना", "type": "branch", "date": "1919", "children": [
                {"label": "द्वैध शासन को 'अव्यावहारिक' कहा गया — भारतीय मंत्रियों को संसाधनों के बिना जिम्मेदारी दी; राजस्व और पुलिस गवर्नर के पास रहे", "type": "leaf"},
                {"label": "साइमन कमीशन (1927) समीक्षा के लिए नियुक्त; कांग्रेस ने बहिष्कार किया क्योंकि कोई भारतीय शामिल नहीं; 'साइमन गो बैक' विरोध", "type": "leaf"},
                {"label": "अधिनियम रॉलेट एक्ट (1919) और जलियांवाला बाग हत्याकांड के साथ आया — सुधार भावना से विरोधाभास; असहयोग आंदोलन को बल मिला", "type": "leaf"}
            ]}
        ]
    },
    "government-of-india-act-1935": {
        "en": [
            {"label": "Federal Structure", "type": "branch", "date": "1935", "children": [
                {"label": "Proposed All-India Federation of British India provinces + Princely States — federation never came into force as princes refused to join", "type": "leaf"},
                {"label": "Three Lists: Federal (Centre), Provincial, Concurrent — model adopted almost verbatim by Indian Constitution (1950)", "type": "leaf"},
                {"label": "Federal Court of India established (forerunner of Supreme Court); Privy Council in London retained as highest appellate court", "type": "leaf"}
            ]},
            {"label": "Provincial Autonomy", "type": "branch", "date": "1935", "children": [
                {"label": "Dyarchy at Centre introduced; abolished dyarchy at provinces; provinces given full autonomy in provincial subjects", "type": "leaf"},
                {"label": "Congress formed governments in 7 of 11 provinces after 1937 elections — first experiment in democratic provincial governance", "type": "leaf"},
                {"label": "Governors retained special powers (special responsibilities) to override elected ministers — remained safeguards for British interests", "type": "leaf"}
            ]},
            {"label": "Constitutional Legacy", "type": "branch", "date": "1935", "children": [
                {"label": "253 of 395 Articles in Indian Constitution 1950 are directly derived from GOI Act 1935 — the single most influential colonial constitutional document", "type": "leaf"},
                {"label": "Bicameral legislature at Centre; franchise extended to 14% of population; separate electorates for 8 communities (deeply controversial)", "type": "leaf"},
                {"label": "Reserve Bank of India, Federal Public Service Commission — major institutions created by this Act that survived independence", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संघीय संरचना", "type": "branch", "date": "1935", "children": [
                {"label": "ब्रिटिश भारत के प्रांतों + रियासतों के अखिल भारतीय संघ का प्रस्ताव — संघ कभी लागू नहीं हुआ क्योंकि राजकुमारों ने शामिल होने से मना किया", "type": "leaf"},
                {"label": "तीन सूचियाँ: संघीय (केंद्र), प्रांतीय, समवर्ती — मॉडल भारतीय संविधान (1950) ने लगभग हूबहू अपनाया", "type": "leaf"},
                {"label": "भारत का संघीय न्यायालय स्थापित (सर्वोच्च न्यायालय का अग्रदूत); लंदन में प्रिवी काउंसिल सर्वोच्च अपीलीय न्यायालय के रूप में बनी रही", "type": "leaf"}
            ]},
            {"label": "प्रांतीय स्वायत्तता", "type": "branch", "date": "1935", "children": [
                {"label": "केंद्र में द्वैध शासन पेश; प्रांतों में द्वैध शासन समाप्त; प्रांतीय विषयों में प्रांतों को पूर्ण स्वायत्तता", "type": "leaf"},
                {"label": "1937 चुनावों के बाद कांग्रेस ने 11 में से 7 प्रांतों में सरकार बनाई — लोकतांत्रिक प्रांतीय शासन का पहला प्रयोग", "type": "leaf"},
                {"label": "गवर्नरों ने निर्वाचित मंत्रियों को ओवरराइड करने के लिए विशेष शक्तियां (विशेष उत्तरदायित्व) बनाए रखीं — ब्रिटिश हितों के लिए सुरक्षा उपाय", "type": "leaf"}
            ]},
            {"label": "संवैधानिक विरासत", "type": "branch", "date": "1935", "children": [
                {"label": "भारतीय संविधान 1950 के 395 अनुच्छेदों में से 253 GOI अधिनियम 1935 से सीधे व्युत्पन्न — सबसे प्रभावशाली औपनिवेशिक संवैधानिक दस्तावेज", "type": "leaf"},
                {"label": "केंद्र में द्विसदनीय विधायिका; मताधिकार 14% जनसंख्या तक बढ़ाया; 8 समुदायों के लिए अलग निर्वाचन क्षेत्र (अत्यंत विवादास्पद)", "type": "leaf"},
                {"label": "भारतीय रिजर्व बैंक, संघीय लोक सेवा आयोग — इस अधिनियम द्वारा बनाई गई प्रमुख संस्थाएं जो स्वतंत्रता के बाद भी बची रहीं", "type": "leaf"}
            ]}
        ]
    },
    "governor-generals-of-bengal": {
        "en": [
            {"label": "Early Governor-Generals (1773-1813)", "type": "branch", "date": "1773-1813", "children": [
                {"label": "Warren Hastings (1773-85): First Governor-General; abolished dual polity; reformed judiciary; impeached in England but acquitted after 7-year trial", "type": "leaf"},
                {"label": "Lord Cornwallis (1786-93): Cornwallis Code; Permanent Settlement 1793; separated judicial and revenue; refused to involve Indians in senior posts", "type": "leaf"},
                {"label": "Sir John Shore (1793-98): Non-interventionist; watched Oudh decline; Nizam-Maratha war without interfering; succeeded by Wellesley", "type": "leaf"}
            ]},
            {"label": "Expansion Era (1798-1833)", "type": "branch", "date": "1798-1833", "children": [
                {"label": "Lord Wellesley (1798-1805): Subsidiary Alliance; defeated Tipu Sultan (1799); Second Maratha War (1803); most expansionist GG of Bengal era", "type": "leaf"},
                {"label": "Lord Minto (1807-13): Sent Malcolm to Persia, Elphinstone to Afghanistan, Metcalfe to Ranjit Singh — diplomatic missions securing frontiers", "type": "leaf"},
                {"label": "Lord Moira/Hastings (1813-23): Third Anglo-Maratha War (1817-19); annexed Maratha territories; suppressed Pindari bands; Ryotwari introduced in Madras", "type": "leaf"}
            ]},
            {"label": "Reform Era (1823-1833)", "type": "branch", "date": "1823-1833", "children": [
                {"label": "Lord William Bentinck (1828-33): Major social reformer; abolished Sati (1829); suppressed Thuggee; Macaulay's education minute (1835 after his tenure); English as official language", "type": "leaf"},
                {"label": "Became India's first Governor-General under Charter Act 1833 — last GG of Bengal and first of India; abolished provincial appeal courts", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रारंभिक गवर्नर-जनरल (1773-1813)", "type": "branch", "date": "1773-1813", "children": [
                {"label": "वारेन हेस्टिंग्स (1773-85): पहले गवर्नर-जनरल; द्वैध शासन समाप्त; न्यायपालिका में सुधार; इंग्लैंड में महाभियोग लेकिन 7 वर्षीय मुकदमे के बाद बरी", "type": "leaf"},
                {"label": "लॉर्ड कॉर्नवालिस (1786-93): कॉर्नवालिस कोड; स्थायी बंदोबस्त 1793; न्यायिक और राजस्व का पृथक्करण; वरिष्ठ पदों पर भारतीयों को शामिल करने से मना किया", "type": "leaf"},
                {"label": "सर जॉन शोर (1793-98): गैर-हस्तक्षेपवादी; अवध के पतन को देखा; बिना हस्तक्षेप के निजाम-मराठा युद्ध; वेलेजली का उत्तराधिकार", "type": "leaf"}
            ]},
            {"label": "विस्तार काल (1798-1833)", "type": "branch", "date": "1798-1833", "children": [
                {"label": "लॉर्ड वेलेजली (1798-1805): सहायक संधि; टीपू सुल्तान को हराया (1799); द्वितीय मराठा युद्ध (1803); बंगाल काल का सबसे विस्तारवादी GG", "type": "leaf"},
                {"label": "लॉर्ड मिंटो (1807-13): मैल्कम को फारस, एल्फिंस्टोन को अफगानिस्तान, मेटकाफ को रणजीत सिंह के पास भेजा — सीमाएं सुरक्षित करने के राजनयिक मिशन", "type": "leaf"},
                {"label": "लॉर्ड मोइरा/हेस्टिंग्स (1813-23): तृतीय आंग्ल-मराठा युद्ध (1817-19); मराठा क्षेत्र हड़पे; पिंडारी बैंड दबाए; मद्रास में रैयतवारी पेश", "type": "leaf"}
            ]},
            {"label": "सुधार काल (1823-1833)", "type": "branch", "date": "1823-1833", "children": [
                {"label": "लॉर्ड विलियम बेंटिक (1828-33): प्रमुख सामाजिक सुधारक; सती प्रथा समाप्त (1829); ठगी दबाई; मैकाले का शिक्षा मिनट (उनके कार्यकाल के बाद 1835); अंग्रेजी आधिकारिक भाषा", "type": "leaf"},
                {"label": "चार्टर अधिनियम 1833 के तहत भारत के पहले गवर्नर-जनरल बने — बंगाल के अंतिम GG और भारत के पहले; प्रांतीय अपील अदालतें समाप्त कीं", "type": "leaf"}
            ]}
        ]
    },
    "governor-generals-of-bengal-1773-1833": {
        "en": [
            {"label": "Warren Hastings (1773-85)", "type": "branch", "date": "1773-1785", "children": [
                {"label": "First Governor-General under Regulating Act; abolished Dual Polity (1772); created District Collectors; reorganised courts — Diwani Adalat and Faujdari Adalat", "type": "leaf"},
                {"label": "Created Calcutta as administrative capital; defeated Rohillas (1774); managed First Anglo-Maratha War through Treaty of Salbai (1782)", "type": "leaf"},
                {"label": "Impeached by Parliament (1787) under Burke and Fox for alleged corruption; acquitted 1795 after 7-year trial; died honoured in 1818", "type": "leaf"}
            ]},
            {"label": "Cornwallis (1786-93) & Shore (1793-98)", "type": "branch", "date": "1786-1798", "children": [
                {"label": "Cornwallis: Permanent Settlement (1793); Third Anglo-Mysore War (Treaty of Seringapatam 1792); Cornwallis Code; banned Indian senior posts", "type": "leaf"},
                {"label": "Shore: Passive; Nizam-Maratha conflict without intervention; Treaty of Amritsar with Ranjit Singh's predecessor; left India chaotic but peaceful", "type": "leaf"}
            ]},
            {"label": "Wellesley to Hastings (1798-1823)", "type": "branch", "date": "1798-1823", "children": [
                {"label": "Wellesley (1798-1805): Subsidiary Alliance; 4th Mysore War; 2nd Maratha War; founded Fort William College (1800) for ICS training", "type": "leaf"},
                {"label": "Cornwallis 2nd (1805, died in office); Minto (1807-13); Lord Hastings (1813-23): Third Maratha War; Pindari suppression; Ryotwari (Munro)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वारेन हेस्टिंग्स (1773-85)", "type": "branch", "date": "1773-1785", "children": [
                {"label": "विनियमन अधिनियम के तहत पहले गवर्नर-जनरल; द्वैध शासन समाप्त (1772); जिला कलेक्टर बनाए; अदालतें पुनर्गठित — दीवानी अदालत और फौजदारी अदालत", "type": "leaf"},
                {"label": "कलकत्ता को प्रशासनिक राजधानी बनाया; रोहिल्लों को हराया (1774); सालबाई की संधि (1782) के माध्यम से प्रथम आंग्ल-मराठा युद्ध संभाला", "type": "leaf"},
                {"label": "बर्क और फॉक्स द्वारा कथित भ्रष्टाचार के लिए संसद ने महाभियोग चलाया (1787); 7 वर्षीय मुकदमे के बाद 1795 में बरी; 1818 में सम्मानित होकर मृत्यु", "type": "leaf"}
            ]},
            {"label": "कॉर्नवालिस (1786-93) और शोर (1793-98)", "type": "branch", "date": "1786-1798", "children": [
                {"label": "कॉर्नवालिस: स्थायी बंदोबस्त (1793); तृतीय आंग्ल-मैसूर युद्ध (श्रीरंगपट्टनम की संधि 1792); कॉर्नवालिस कोड; भारतीय वरिष्ठ पदों पर प्रतिबंध", "type": "leaf"},
                {"label": "शोर: निष्क्रिय; बिना हस्तक्षेप के निजाम-मराठा संघर्ष; रणजीत सिंह के पूर्ववर्ती के साथ अमृतसर की संधि; भारत को अव्यवस्थित लेकिन शांतिपूर्ण छोड़ा", "type": "leaf"}
            ]},
            {"label": "वेलेजली से हेस्टिंग्स (1798-1823)", "type": "branch", "date": "1798-1823", "children": [
                {"label": "वेलेजली (1798-1805): सहायक संधि; चौथा मैसूर युद्ध; दूसरा मराठा युद्ध; ICS प्रशिक्षण के लिए फोर्ट विलियम कॉलेज (1800) की स्थापना", "type": "leaf"},
                {"label": "कॉर्नवालिस द्वितीय (1805, कार्यालय में मृत्यु); मिंटो (1807-13); लॉर्ड हेस्टिंग्स (1813-23): तृतीय मराठा युद्ध; पिंडारी दमन; रैयतवारी (मुनरो)", "type": "leaf"}
            ]}
        ]
    },
    "governor-of-bengal": {
        "en": [
            {"label": "Pre-Regulating Act Governors", "type": "branch", "date": "1757-1772", "children": [
                {"label": "Robert Clive (1757-60, 1765-67): Won Plassey; installed Mir Jafar; established Diwani rights; introduced dual polity after Treaty of Allahabad", "type": "leaf"},
                {"label": "Henry Vansittart (1760-64): Conflict with Mir Jafar; installed Mir Qasim; led to Battle of Buxar (1764)", "type": "leaf"},
                {"label": "John Cartier (1769-72): Bengal Famine (1770) during his tenure — devastating failure of colonial administration; 10 million died", "type": "leaf"}
            ]},
            {"label": "Warren Hastings as Governor (1772-73)", "type": "branch", "date": "1772-1773", "children": [
                {"label": "Appointed Governor of Bengal (not yet GG) in 1772; immediately abolished dual polity; took direct charge of revenue", "type": "leaf"},
                {"label": "Created five provincial divisions for revenue administration; established District Collectors as primary revenue authorities", "type": "leaf"}
            ]},
            {"label": "Transition to Governor-General", "type": "branch", "date": "1773", "children": [
                {"label": "Regulating Act 1773 elevated position to Governor-General with authority over Bombay and Madras Presidencies", "type": "leaf"},
                {"label": "Warren Hastings became the first Governor-General of Bengal (1773-85) under the new constitutional framework", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विनियमन अधिनियम से पहले के गवर्नर", "type": "branch", "date": "1757-1772", "children": [
                {"label": "रॉबर्ट क्लाइव (1757-60, 1765-67): प्लासी जीता; मीर जाफर को स्थापित किया; दीवानी अधिकार स्थापित; इलाहाबाद की संधि के बाद द्वैध शासन पेश", "type": "leaf"},
                {"label": "हेनरी वांसिटार्ट (1760-64): मीर जाफर के साथ संघर्ष; मीर कासिम को स्थापित किया; बक्सर की लड़ाई (1764) का कारण", "type": "leaf"},
                {"label": "जॉन कार्टियर (1769-72): उनके कार्यकाल के दौरान बंगाल अकाल (1770) — औपनिवेशिक प्रशासन की विनाशकारी विफलता; 1 करोड़ मृत", "type": "leaf"}
            ]},
            {"label": "वारेन हेस्टिंग्स गवर्नर के रूप में (1772-73)", "type": "branch", "date": "1772-1773", "children": [
                {"label": "1772 में बंगाल के गवर्नर (अभी तक GG नहीं) नियुक्त; तुरंत द्वैध शासन समाप्त किया; राजस्व का प्रत्यक्ष प्रभार लिया", "type": "leaf"},
                {"label": "राजस्व प्रशासन के लिए पांच प्रांतीय डिवीजन बनाए; जिला कलेक्टरों को प्राथमिक राजस्व प्राधिकरण के रूप में स्थापित किया", "type": "leaf"}
            ]},
            {"label": "गवर्नर-जनरल में संक्रमण", "type": "branch", "date": "1773", "children": [
                {"label": "विनियमन अधिनियम 1773 ने बॉम्बे और मद्रास प्रेसीडेंसियों पर अधिकार के साथ पद को गवर्नर-जनरल तक उन्नत किया", "type": "leaf"},
                {"label": "वारेन हेस्टिंग्स नई संवैधानिक रूपरेखा के तहत बंगाल के पहले गवर्नर-जनरल (1773-85) बने", "type": "leaf"}
            ]}
        ]
    },
    "governor-of-bengal-before-1773": {
        "en": [
            {"label": "Early Presidents/Governors", "type": "branch", "date": "1600-1757", "children": [
                {"label": "Madras Presidency and Bombay Presidency each had Presidents; Bengal had Agent, then President, then Governor — titles evolved with EIC's growing power", "type": "leaf"},
                {"label": "Roger Drake (Governor 1752-58): Fled Calcutta when Siraj ud Daula attacked (1756); his cowardice was blamed for loss of Calcutta", "type": "leaf"},
                {"label": "Robert Clive: Recaptured Calcutta (Jan 1757); won Battle of Plassey (June 1757); first governor to exercise real political power in Bengal", "type": "leaf"}
            ]},
            {"label": "Mir Jafar & Mir Qasim Era", "type": "branch", "date": "1757-1765", "children": [
                {"label": "Henry Vansittart (1760-64): Replaced Mir Jafar with Mir Qasim (1760) to resolve corruption; Mir Qasim proved too independent — conflict led to Buxar", "type": "leaf"},
                {"label": "John Zephaniah Holwell (acting 1760): Claimed to have survived Black Hole of Calcutta — his account shaped British perception of Siraj ud Daula", "type": "leaf"}
            ]},
            {"label": "Path to Regulating Act", "type": "branch", "date": "1765-1773", "children": [
                {"label": "After Buxar: EIC directors in London unhappy with corruption and conflicts; Clive's second tenure (1765-67) tried to reform — but private trade continued", "type": "leaf"},
                {"label": "Bengal Famine (1770): Parliament alarmed; Select Committee and Secret Committee investigated EIC; led directly to Regulating Act 1773", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रारंभिक अध्यक्ष/गवर्नर", "type": "branch", "date": "1600-1757", "children": [
                {"label": "मद्रास प्रेसीडेंसी और बॉम्बे प्रेसीडेंसी में प्रत्येक के अध्यक्ष थे; बंगाल में एजेंट, फिर अध्यक्ष, फिर गवर्नर था — EIC की बढ़ती शक्ति के साथ पदनाम विकसित हुए", "type": "leaf"},
                {"label": "रॉजर ड्रेक (गवर्नर 1752-58): सिराज उद दौला के हमले (1756) पर कलकत्ता से भागा; उनकी कायरता को कलकत्ता के नुकसान के लिए दोषी ठहराया गया", "type": "leaf"},
                {"label": "रॉबर्ट क्लाइव: कलकत्ता वापस जीता (जन. 1757); प्लासी की लड़ाई जीती (जून 1757); बंगाल में वास्तविक राजनीतिक शक्ति का प्रयोग करने वाले पहले गवर्नर", "type": "leaf"}
            ]},
            {"label": "मीर जाफर और मीर कासिम काल", "type": "branch", "date": "1757-1765", "children": [
                {"label": "हेनरी वांसिटार्ट (1760-64): भ्रष्टाचार हल करने के लिए मीर जाफर की जगह मीर कासिम (1760) को स्थापित किया; मीर कासिम बहुत स्वतंत्र निकला — संघर्ष बक्सर की ओर ले गया", "type": "leaf"},
                {"label": "जॉन जेफनिया होलवेल (कार्यकारी 1760): कलकत्ता के ब्लैक होल से बचने का दावा — उनके विवरण ने सिराज उद दौला के बारे में ब्रिटिश धारणा को आकार दिया", "type": "leaf"}
            ]},
            {"label": "विनियमन अधिनियम की राह", "type": "branch", "date": "1765-1773", "children": [
                {"label": "बक्सर के बाद: लंदन में EIC निदेशक भ्रष्टाचार और संघर्षों से नाखुश; क्लाइव का दूसरा कार्यकाल (1765-67) सुधार की कोशिश — लेकिन निजी व्यापार जारी रहा", "type": "leaf"},
                {"label": "बंगाल अकाल (1770): संसद चिंतित; सिलेक्ट कमेटी और सीक्रेट कमेटी ने EIC की जांच की; सीधे विनियमन अधिनियम 1773 की ओर ले गया", "type": "leaf"}
            ]}
        ]
    },
    "indian-councils-act-1892": {
        "en": [
            {"label": "Key Provisions", "type": "branch", "date": "1892", "children": [
                {"label": "Increased number of additional (non-official) members in Imperial Legislative Council and Provincial Councils — but still no elections", "type": "leaf"},
                {"label": "Nominated members could represent interest groups: district boards, municipalities, universities, trade associations — indirect representation", "type": "leaf"},
                {"label": "Members given limited right to discuss budget and ask questions about public matters — first time this legislative right conceded to Indians", "type": "leaf"}
            ]},
            {"label": "Political Context", "type": "branch", "date": "1892", "children": [
                {"label": "Indian National Congress (founded 1885) had been demanding expanded councils and Indian representation; this Act was British response — limited concession", "type": "leaf"},
                {"label": "Congress demanded elected councils; British offered nominated representatives from interest groups — fell far short of nationalist demands", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1892", "children": [
                {"label": "First step towards representative institutions; established principle that Indians could question executive on public affairs", "type": "leaf"},
                {"label": "Dissatisfaction with 1892 Act fuelled more intense Congress demands — led eventually to Morley-Minto Reforms (Indian Councils Act 1909)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1892", "children": [
                {"label": "इंपीरियल लेजिस्लेटिव काउंसिल और प्रांतीय परिषदों में अतिरिक्त (गैर-आधिकारिक) सदस्यों की संख्या बढ़ाई — लेकिन अभी भी कोई चुनाव नहीं", "type": "leaf"},
                {"label": "नामांकित सदस्य हित समूहों का प्रतिनिधित्व कर सकते थे: जिला बोर्ड, नगरपालिकाएं, विश्वविद्यालय, व्यापार संघ — अप्रत्यक्ष प्रतिनिधित्व", "type": "leaf"},
                {"label": "सदस्यों को बजट पर चर्चा करने और सार्वजनिक मामलों पर सवाल पूछने का सीमित अधिकार — पहली बार यह विधायी अधिकार भारतीयों को दिया गया", "type": "leaf"}
            ]},
            {"label": "राजनीतिक संदर्भ", "type": "branch", "date": "1892", "children": [
                {"label": "भारतीय राष्ट्रीय कांग्रेस (1885 में स्थापित) विस्तारित परिषदों और भारतीय प्रतिनिधित्व की मांग कर रही थी; यह अधिनियम ब्रिटिश प्रतिक्रिया थी — सीमित रियायत", "type": "leaf"},
                {"label": "कांग्रेस ने निर्वाचित परिषदों की मांग की; ब्रिटिश ने हित समूहों से नामांकित प्रतिनिधि दिए — राष्ट्रवादी मांगों से बहुत कम", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1892 के बाद", "children": [
                {"label": "प्रतिनिधि संस्थाओं की दिशा में पहला कदम; स्थापित किया कि भारतीय सार्वजनिक मामलों पर कार्यपालिका से सवाल कर सकते हैं", "type": "leaf"},
                {"label": "1892 अधिनियम से असंतोष ने अधिक तीव्र कांग्रेस मांगों को बल दिया — अंततः मोर्ले-मिंटो सुधार (भारतीय परिषद अधिनियम 1909) की ओर ले गया", "type": "leaf"}
            ]}
        ]
    },
    "indian-councils-act-1909": {
        "en": [
            {"label": "Morley-Minto Reforms", "type": "branch", "date": "1909", "children": [
                {"label": "Named after Lord Morley (Secretary of State) and Lord Minto (Viceroy); context of Swadeshi Movement and Partition of Bengal (1905)", "type": "leaf"},
                {"label": "Imperial Legislative Council enlarged to 60 members; Provincial Councils also enlarged; increased elected (non-official) members", "type": "leaf"},
                {"label": "For the first time, an Indian appointed to Governor-General's Executive Council: Satyendra Prasanna Sinha (Law Member, 1909)", "type": "leaf"}
            ]},
            {"label": "Separate Electorates", "type": "branch", "date": "1909", "children": [
                {"label": "Most controversial provision: introduced separate Muslim electorate — Muslims would elect their own representatives exclusively", "type": "leaf"},
                {"label": "Based on Simla Deputation (1906) when Aga Khan led Muslim delegation demanding separate electorates — British conceded to divide Hindu-Muslim unity", "type": "leaf"},
                {"label": "Nationalist criticism: Gokhale called it 'a poisonous seed' — laid foundation for communal politics; Congress opposed it but could not prevent it", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1909", "children": [
                {"label": "Introduced the principle of representation though not responsible government; elected members still a minority; Viceroy had veto", "type": "leaf"},
                {"label": "Separate electorates proved to be the most consequential provision — eventually contributed to Partition of India in 1947", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मोर्ले-मिंटो सुधार", "type": "branch", "date": "1909", "children": [
                {"label": "लॉर्ड मोर्ले (राज्य सचिव) और लॉर्ड मिंटो (वायसराय) के नाम पर; स्वदेशी आंदोलन और बंगाल विभाजन (1905) का संदर्भ", "type": "leaf"},
                {"label": "इंपीरियल लेजिस्लेटिव काउंसिल 60 सदस्यों तक बड़ी की; प्रांतीय परिषदें भी बड़ी कीं; निर्वाचित (गैर-आधिकारिक) सदस्य बढ़ाए", "type": "leaf"},
                {"label": "पहली बार गवर्नर-जनरल की कार्यकारी परिषद में एक भारतीय नियुक्त: सत्येंद्र प्रसाद सिन्हा (विधि सदस्य, 1909)", "type": "leaf"}
            ]},
            {"label": "अलग निर्वाचन क्षेत्र", "type": "branch", "date": "1909", "children": [
                {"label": "सबसे विवादास्पद प्रावधान: अलग मुस्लिम निर्वाचन क्षेत्र पेश किया — मुसलमान विशेष रूप से अपने प्रतिनिधि चुनेंगे", "type": "leaf"},
                {"label": "शिमला प्रतिनिधिमंडल (1906) पर आधारित जब आगा खान ने अलग निर्वाचन क्षेत्रों की मांग करते हुए मुस्लिम प्रतिनिधिमंडल का नेतृत्व किया — ब्रिटिश ने हिंदू-मुस्लिम एकता तोड़ने के लिए स्वीकार किया", "type": "leaf"},
                {"label": "राष्ट्रवादी आलोचना: गोखले ने इसे 'जहरीला बीज' कहा — सांप्रदायिक राजनीति की नींव रखी; कांग्रेस ने विरोध किया लेकिन रोक नहीं सकी", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1909 के बाद", "children": [
                {"label": "जिम्मेदार सरकार नहीं बल्कि प्रतिनिधित्व का सिद्धांत पेश किया; निर्वाचित सदस्य अभी भी अल्पसंख्यक; वायसराय के पास वीटो", "type": "leaf"},
                {"label": "अलग निर्वाचन क्षेत्र सबसे परिणामी प्रावधान साबित हुए — अंततः 1947 में भारत के विभाजन में योगदान किया", "type": "leaf"}
            ]}
        ]
    },
    "indian-independence-act-1947": {
        "en": [
            {"label": "Key Provisions", "type": "branch", "date": "18 July 1947", "children": [
                {"label": "Passed by British Parliament 18 July 1947; created two independent dominions: India and Pakistan from 15 August 1947", "type": "leaf"},
                {"label": "Partition of Punjab and Bengal: Boundary Commissions under Sir Cyril Radcliffe drew borders — Radcliffe Line announced 17 August 1947", "type": "leaf"},
                {"label": "Princely States given choice: accede to India or Pakistan or remain independent — 565 states eventually integrated into India by 1950", "type": "leaf"}
            ]},
            {"label": "Constitutional Provisions", "type": "branch", "date": "1947", "children": [
                {"label": "Constituent Assemblies of both dominions given full legislative authority; Governor-General appointed by Crown on advice of dominion PM", "type": "leaf"},
                {"label": "GOI Act 1935 (with modifications) became interim Constitution of both dominions until new constitutions adopted", "type": "leaf"},
                {"label": "Lord Mountbatten became first Governor-General of India (accepted on Nehru's invitation); Jinnah became first Governor-General of Pakistan", "type": "leaf"}
            ]},
            {"label": "Significance & Partition", "type": "branch", "date": "Post-1947", "children": [
                {"label": "Largest migration in human history: 12-15 million displaced; 200,000-2 million killed in communal violence during Partition", "type": "leaf"},
                {"label": "Integration of Princely States: Sardar Vallabhbhai Patel (Home Minister) integrated 552 of 565 states; Hyderabad (1948) and Junagadh via police action", "type": "leaf"},
                {"label": "India adopted its own Constitution on 26 January 1950 — Republic Day; transformed from dominion to sovereign republic", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "18 जुलाई 1947", "children": [
                {"label": "18 जुलाई 1947 को ब्रिटिश संसद द्वारा पारित; 15 अगस्त 1947 से दो स्वतंत्र अधिराज्य बनाए: भारत और पाकिस्तान", "type": "leaf"},
                {"label": "पंजाब और बंगाल का विभाजन: सर सिरिल रैडक्लिफ के तहत सीमा आयोगों ने सीमाएं खींचीं — रैडक्लिफ रेखा 17 अगस्त 1947 को घोषित", "type": "leaf"},
                {"label": "रियासतों को विकल्प दिया: भारत या पाकिस्तान में शामिल हों या स्वतंत्र रहें — 565 राज्य अंततः 1950 तक भारत में एकीकृत", "type": "leaf"}
            ]},
            {"label": "संवैधानिक प्रावधान", "type": "branch", "date": "1947", "children": [
                {"label": "दोनों अधिराज्यों की संविधान सभाओं को पूर्ण विधायी अधिकार दिया; गवर्नर-जनरल अधिराज्य PM की सलाह पर क्राउन द्वारा नियुक्त", "type": "leaf"},
                {"label": "GOI अधिनियम 1935 (संशोधनों के साथ) नए संविधान अपनाने तक दोनों अधिराज्यों का अंतरिम संविधान बना", "type": "leaf"},
                {"label": "लॉर्ड माउंटबेटन भारत के पहले गवर्नर-जनरल बने (नेहरू के निमंत्रण पर स्वीकार); जिन्ना पाकिस्तान के पहले गवर्नर-जनरल बने", "type": "leaf"}
            ]},
            {"label": "महत्व और विभाजन", "type": "branch", "date": "1947 के बाद", "children": [
                {"label": "मानव इतिहास में सबसे बड़ा प्रवासन: 1.2-1.5 करोड़ विस्थापित; विभाजन के दौरान सांप्रदायिक हिंसा में 2-20 लाख मारे गए", "type": "leaf"},
                {"label": "रियासतों का एकीकरण: सरदार वल्लभभाई पटेल (गृह मंत्री) ने 565 में से 552 राज्यों का एकीकरण किया; हैदराबाद (1948) और जूनागढ़ पुलिस कार्रवाई से", "type": "leaf"},
                {"label": "भारत ने 26 जनवरी 1950 को अपना संविधान अपनाया — गणतंत्र दिवस; अधिराज्य से संप्रभु गणराज्य में रूपांतरण", "type": "leaf"}
            ]}
        ]
    },
    "pitts-india-act-of-1784": {
        "en": [
            {"label": "Background", "type": "branch", "date": "1784", "children": [
                {"label": "Regulating Act 1773 had failed to control EIC adequately; Governor-General overruled by Council; Warren Hastings' conflicts with Council highlighted structural flaws", "type": "leaf"},
                {"label": "William Pitt the Younger's government passed the Act; created a fundamentally different relationship between Parliament and EIC", "type": "leaf"}
            ]},
            {"label": "Key Provisions", "type": "branch", "date": "1784", "children": [
                {"label": "Board of Control created: 6 members (2 Secretaries of State, Chancellor of Exchequer + 3 Privy Councillors); controlled political/military/revenue matters", "type": "leaf"},
                {"label": "Court of Directors retained control over commercial affairs and appointment of EIC staff; Board of Control overrode on political matters", "type": "leaf"},
                {"label": "Governor-General given sweeping powers over other Presidencies; Secret Committee of 3 Directors could send secret dispatches without full board", "type": "leaf"},
                {"label": "First time India's affairs designated as 'the affairs of a nation' — recognised India's governance as matter of national importance, not mere commerce", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1784", "children": [
                {"label": "Created 'double government' of Crown (Board) + EIC (Directors) that lasted until 1858's Government of India Act abolished EIC", "type": "leaf"},
                {"label": "Made British Cabinet ultimately responsible for India — direct line from Pitt's Act to Government of India Act 1858 to Independence 1947", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि", "type": "branch", "date": "1784", "children": [
                {"label": "विनियमन अधिनियम 1773 EIC को पर्याप्त रूप से नियंत्रित करने में विफल रहा; परिषद ने गवर्नर-जनरल को ओवरराइड किया; परिषद के साथ वारेन हेस्टिंग्स के संघर्षों ने संरचनात्मक खामियां उजागर कीं", "type": "leaf"},
                {"label": "विलियम पिट द यंगर की सरकार ने अधिनियम पारित किया; संसद और EIC के बीच मूलतः भिन्न संबंध बनाया", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1784", "children": [
                {"label": "बोर्ड ऑफ कंट्रोल बनाया: 6 सदस्य (2 राज्य सचिव, चांसलर ऑफ एक्सचेकर + 3 प्रिवी काउंसिलर); राजनीतिक/सैन्य/राजस्व मामले नियंत्रित", "type": "leaf"},
                {"label": "कोर्ट ऑफ डायरेक्टर्स ने वाणिज्यिक मामलों और EIC कर्मचारियों की नियुक्ति पर नियंत्रण बनाए रखा; बोर्ड ऑफ कंट्रोल ने राजनीतिक मामलों पर ओवरराइड किया", "type": "leaf"},
                {"label": "गवर्नर-जनरल को अन्य प्रेसीडेंसियों पर व्यापक शक्तियां; 3 डायरेक्टरों की गुप्त समिति पूरे बोर्ड के बिना गुप्त प्रेषण भेज सकती थी", "type": "leaf"},
                {"label": "पहली बार भारत के मामलों को 'एक राष्ट्र के मामले' कहा गया — भारत के शासन को केवल वाणिज्य नहीं बल्कि राष्ट्रीय महत्व का मामला माना", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1784 के बाद", "children": [
                {"label": "क्राउन (बोर्ड) + EIC (डायरेक्टर्स) की 'दोहरी सरकार' बनाई जो 1858 के भारत सरकार अधिनियम द्वारा EIC के उन्मूलन तक चली", "type": "leaf"},
                {"label": "ब्रिटिश कैबिनेट को भारत के लिए अंततः जिम्मेदार बनाया — पिट के अधिनियम से भारत सरकार अधिनियम 1858 से 1947 स्वतंत्रता तक सीधी रेखा", "type": "leaf"}
            ]}
        ]
    },
    "regulating-act-1773": {
        "en": [
            {"label": "Background & Need", "type": "branch", "date": "1773", "children": [
                {"label": "Bengal Famine (1770): EIC's misrule led to death of ~10 million; Parliament could not ignore; corruption of EIC servants causing scandals", "type": "leaf"},
                {"label": "EIC's financial crisis: company had to request £1.4 million government loan; Parliamentary oversight became inevitable", "type": "leaf"},
                {"label": "Robert Clive's reforms had failed; Dual Government created administrative vacuum; London directors unable to control Bengal presidency", "type": "leaf"}
            ]},
            {"label": "Key Provisions", "type": "branch", "date": "1773", "children": [
                {"label": "Bengal's Governor elevated to 'Governor-General of Bengal' with a 4-member Executive Council; first step towards centralised administration", "type": "leaf"},
                {"label": "Governor-General could be overruled by majority of Council — Warren Hastings' tenure showed this was unworkable (Regulating Act's main flaw)", "type": "leaf"},
                {"label": "Supreme Court of Judicature established at Calcutta (1774): Sir Elijah Impey as Chief Justice; 3 puisne judges; exercised jurisdiction over British subjects", "type": "leaf"},
                {"label": "Governors of Bombay and Madras became subordinate to Bengal Governor-General in matters of war and peace", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1773", "children": [
                {"label": "First Parliamentary legislation to directly control EIC's territorial possessions — beginning of Parliamentary sovereignty over India", "type": "leaf"},
                {"label": "Supreme Court created a parallel judicial authority that clashed with Governor-General (Nandakumar affair, 1775) — exposed constitutional ambiguity", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पृष्ठभूमि और आवश्यकता", "type": "branch", "date": "1773", "children": [
                {"label": "बंगाल अकाल (1770): EIC के कुशासन से ~1 करोड़ की मृत्यु; संसद नजरअंदाज नहीं कर सकती थी; EIC सेवकों के भ्रष्टाचार से कांड", "type": "leaf"},
                {"label": "EIC का वित्तीय संकट: कंपनी को 14 लाख पाउंड सरकारी ऋण मांगना पड़ा; संसदीय निगरानी अनिवार्य हो गई", "type": "leaf"},
                {"label": "रॉबर्ट क्लाइव के सुधार विफल रहे; द्वैध सरकार ने प्रशासनिक शून्य बनाया; लंदन निदेशक बंगाल प्रेसीडेंसी नियंत्रित नहीं कर सके", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1773", "children": [
                {"label": "बंगाल के गवर्नर को 4-सदस्यीय कार्यकारी परिषद के साथ 'बंगाल के गवर्नर-जनरल' तक उन्नत किया; केंद्रीकृत प्रशासन की दिशा में पहला कदम", "type": "leaf"},
                {"label": "परिषद के बहुमत से गवर्नर-जनरल को ओवरराइड किया जा सकता था — वारेन हेस्टिंग्स के कार्यकाल ने दिखाया यह अव्यावहारिक था (विनियमन अधिनियम की मुख्य खामी)", "type": "leaf"},
                {"label": "कलकत्ता में उच्चतम न्यायालय (1774): सर एलिजा इम्पी मुख्य न्यायाधीश; 3 न्यायाधीश; ब्रिटिश प्रजा पर क्षेत्राधिकार", "type": "leaf"},
                {"label": "बॉम्बे और मद्रास के गवर्नर युद्ध और शांति के मामलों में बंगाल गवर्नर-जनरल के अधीनस्थ बने", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1773 के बाद", "children": [
                {"label": "EIC के क्षेत्रीय अधिकारों को सीधे नियंत्रित करने वाला पहला संसदीय कानून — भारत पर संसदीय संप्रभुता की शुरुआत", "type": "leaf"},
                {"label": "सर्वोच्च न्यायालय ने एक समानांतर न्यायिक प्राधिकरण बनाया जो गवर्नर-जनरल से टकराया (नंदकुमार मामला, 1775) — संवैधानिक अस्पष्टता उजागर", "type": "leaf"}
            ]}
        ]
    },
    "the-indian-councils-act-1861": {
        "en": [
            {"label": "Context: Post-1857 Reconstruction", "type": "branch", "date": "1861", "children": [
                {"label": "Passed after 1857 revolt; British needed to accommodate moderate Indians who had stayed loyal; part of 'carrot and stick' post-revolt policy", "type": "leaf"},
                {"label": "Queen's Proclamation (1858) had promised more inclusive governance; 1861 Act partially delivered on this promise", "type": "leaf"},
                {"label": "Viceroy Lord Canning ('Clemency Canning') initiated the reforms; seen as conciliatory gesture to Indian elites", "type": "leaf"}
            ]},
            {"label": "Key Provisions", "type": "branch", "date": "1861", "children": [
                {"label": "Provincial Legislatures restored to Bombay and Madras (Centralization reversed from 1833 Act); portfolio system introduced for Viceroy's Council", "type": "leaf"},
                {"label": "Legislative Councils could include additional (non-official) members — Indians nominated for first time to legislative bodies", "type": "leaf"},
                {"label": "Viceroy given power to issue Ordinances (emergency legislation) lasting 6 months without prior approval of Legislative Council", "type": "leaf"}
            ]},
            {"label": "Significance", "type": "branch", "date": "Post-1861", "children": [
                {"label": "Indians like Dinkar Rao, Narayan Ramachandra Ranade nominated to Legislative Councils — first Indian participation in legislation", "type": "leaf"},
                {"label": "Portfolio system: each Council member made responsible for a specific department — precursor to Cabinet system in modern India", "type": "leaf"},
                {"label": "Decentralisation of legislative power to provinces — important step that eventually led to federalism in GOI Act 1935", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संदर्भ: 1857 के बाद पुनर्निर्माण", "type": "branch", "date": "1861", "children": [
                {"label": "1857 विद्रोह के बाद पारित; ब्रिटिश को उन मध्यमार्गी भारतीयों को समायोजित करना था जो वफादार रहे; विद्रोह के बाद 'गाजर और छड़ी' नीति का हिस्सा", "type": "leaf"},
                {"label": "रानी की उद्घोषणा (1858) ने अधिक समावेशी शासन का वादा किया था; 1861 अधिनियम ने इस वादे को आंशिक रूप से पूरा किया", "type": "leaf"},
                {"label": "वायसराय लॉर्ड कैनिंग ('क्लेमेंसी कैनिंग') ने सुधार शुरू किए; भारतीय अभिजात वर्ग के प्रति सुलह की भावना देखी गई", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्रावधान", "type": "branch", "date": "1861", "children": [
                {"label": "बॉम्बे और मद्रास को प्रांतीय विधायिकाएं बहाल (1833 अधिनियम से केंद्रीकरण उलटा); वायसराय की परिषद के लिए विभाग प्रणाली पेश", "type": "leaf"},
                {"label": "विधान परिषदों में अतिरिक्त (गैर-आधिकारिक) सदस्य शामिल हो सकते थे — पहली बार भारतीयों को विधायी निकायों के लिए नामांकित किया गया", "type": "leaf"},
                {"label": "वायसराय को विधान परिषद की पूर्व अनुमोदन के बिना 6 महीने तक चलने वाले अध्यादेश (आपातकालीन कानून) जारी करने की शक्ति दी", "type": "leaf"}
            ]},
            {"label": "महत्व", "type": "branch", "date": "1861 के बाद", "children": [
                {"label": "दिनकर राव, नारायण रामचंद्र रानाडे जैसे भारतीयों को विधान परिषदों के लिए नामांकित किया — कानून बनाने में पहली भारतीय भागीदारी", "type": "leaf"},
                {"label": "विभाग प्रणाली: प्रत्येक परिषद सदस्य को एक विशिष्ट विभाग के लिए जिम्मेदार बनाया — आधुनिक भारत में कैबिनेट प्रणाली का अग्रदूत", "type": "leaf"},
                {"label": "प्रांतों को विधायी शक्ति का विकेंद्रीकरण — महत्वपूर्ण कदम जो अंततः GOI अधिनियम 1935 में संघवाद की ओर ले गया", "type": "leaf"}
            ]}
        ]
    }
}

MINDMAP_MAPPINGS = {
    "charter-act-of-1793": "charter-act-of-1793",
    "charter-act-of-1813": "charter-act-of-1813",
    "charter-act-of-1833": "charter-act-of-1833",
    "charter-act-of-1853": "charter-act-of-1853",
    "government-of-india-act-1858": "government-of-india-act-1858",
    "government-of-india-act-1919": "government-of-india-act-1919",
    "government-of-india-act-1935": "government-of-india-act-1935",
    "governor-generals-of-bengal": "governor-generals-of-bengal",
    "governor-generals-of-bengal-1773-1833": "governor-generals-of-bengal-1773-1833",
    "governor-of-bengal": "governor-of-bengal",
    "governor-of-bengal-before-1773": "governor-of-bengal-before-1773",
    "indian-councils-act-1892": "indian-councils-act-1892",
    "indian-councils-act-1909": "indian-councils-act-1909",
    "indian-independence-act-1947": "indian-independence-act-1947",
    "pitts-india-act-of-1784": "pitts-india-act-of-1784",
    "regulating-act-1773": "regulating-act-1773",
    "the-indian-councils-act-1861": "the-indian-councils-act-1861"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'at', 'its', 'from', 'before'}
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
    <title>{clean_title} - UPSC Study Guide | SJMaths</title>
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
                      f'<title>{clean_title} (Hindi) - UPSC Study Guide | SJMaths</title>',
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "regulating-act-1773")

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
