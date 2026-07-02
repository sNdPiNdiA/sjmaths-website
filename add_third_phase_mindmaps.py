#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Third-Phase-of-National-Movement"

MINDMAP_DATA = {
    "civil-disobedience-movement": {
        "en": [
            {"label": "Dandi March", "type": "branch", "date": "March 12 - April 6, 1930", "children": [
                {"label": "Gandhi walked from Sabarmati to Dandi (240 miles/385 km) with 78 chosen satyagrahis", "type": "leaf"},
                {"label": "Broke salt law on April 6, 1930 at Dandi beach, starting Civil Disobedience", "type": "leaf"}]},
            {"label": "Regional Centres", "type": "branch", "date": "Campaigns", "children": [
                {"label": "Peshawar: Khan Abdul Ghaffar Khan (Badshah Khan) led 'Red Shirts' (Khudai Khidmatgars); Garhwal Rifles refused to fire on protestors", "type": "leaf"},
                {"label": "Madras: C. Rajagopalachari led salt march from Trichinopoly to Vedaranyam", "type": "leaf"},
                {"label": "Kerala: K. Kelappan led march from Calicut to Payyanur", "type": "leaf"},
                {"label": "Dharasana: Sarojini Naidu, Imam Saheb, and Manilal Gandhi led salt depot raid; faced brutal police lathi charge", "type": "leaf"}]},
            {"label": "NCM vs CDM", "type": "branch", "date": "Comparison", "children": [
                {"label": "NCM (1920) sought Swaraj (self-rule); CDM (1930) demanded Poorna Swaraj (complete independence)", "type": "leaf"},
                {"label": "NCM focused on non-cooperation; CDM focused on active violation of laws (salt, forest, chowkidari taxes)", "type": "leaf"},
                {"label": "NCM had higher Muslim participation; CDM saw unprecedented women and business class involvement", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दांडी मार्च", "type": "branch", "date": "12 मार्च - 6 अप्रैल 1930", "children": [
                {"label": "गांधीजी साबरमती से दांडी (240 मील/385 किमी) तक 78 चुनिंदा सत्याग्रहियों के साथ चले", "type": "leaf"},
                {"label": "6 अप्रैल 1930 को दांडी तट पर नमक कानून तोड़ा, जिससे सविनय अवज्ञा की शुरुआत हुई", "type": "leaf"}]},
            {"label": "क्षेत्रीय केंद्र", "type": "branch", "date": "अभियान", "children": [
                {"label": "पेशावर: खान अब्दुल गफ्फार खान (बादशाह खान) ने 'लाल कुर्ती' (खुदाई खिदमतगार) का नेतृत्व किया; गढ़वाल राइफल्स के सैनिकों ने निहत्थों पर गोली चलाने से मना किया", "type": "leaf"},
                {"label": "मद्रास: सी. राजगोपालाचारी ने त्रिचिनोपोली से वेदारण्यम तक नमक मार्च का नेतृत्व किया", "type": "leaf"},
                {"label": "केरल: के. केलप्पन ने कालीकट से पय्यानूर तक मार्च का नेतृत्व किया", "type": "leaf"},
                {"label": "धरासणा: सरोजिनी नायडू, इमाम साहब और मणिलाल गांधी ने नमक डिपो छापे का नेतृत्व किया; क्रूर लाठीचार्ज का सामना किया", "type": "leaf"}]},
            {"label": "NCM बनाम CDM", "type": "branch", "date": "तुलना", "children": [
                {"label": "असहयोग (1920) का लक्ष्य स्वराज था; सविनय अवज्ञा (1930) ने पूर्ण स्वराज (पूर्ण स्वतंत्रता) की मांग की", "type": "leaf"},
                {"label": "असहयोग केवल असहयोग पर केंद्रित था; सविनय अवज्ञा में कानूनों (नमक, वन, चौकीदारी कर) का सक्रिय उल्लंघन शामिल था", "type": "leaf"},
                {"label": "असहयोग में मुस्लिम भागीदारी अधिक थी; सविनय अवज्ञा में महिलाओं और व्यापारी वर्ग की अभूतपूर्व भागीदारी देखी गई", "type": "leaf"}]}
        ]
    },
    "gandhi-irwin-pact": {
        "en": [
            {"label": "The Pact", "type": "branch", "date": "March 5, 1931", "children": [
                {"label": "Delhi Pact signed between Gandhi and Viceroy Lord Irwin; brokered by Tej Bahadur Sapru & M.R. Jayakar", "type": "leaf"},
                {"label": "Suspended Civil Disobedience; Congress agreed to participate in Second Round Table Conference", "type": "leaf"}]},
            {"label": "Concessions", "type": "branch", "date": "Terms", "children": [
                {"label": "Release of political prisoners not convicted of violence; return of unsold confiscated land", "type": "leaf"},
                {"label": "Right to collect and manufacture salt for domestic use in coastal villages", "type": "leaf"},
                {"label": "Government refused inquiry into police excesses & rejected commutation of Bhagat Singh, Sukhdev, and Rajguru's death sentence", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दिल्ली समझौता", "type": "branch", "date": "5 मार्च 1931", "children": [
                {"label": "गांधीजी और वायसराय लॉर्ड इरविन के बीच हस्ताक्षरित; तेज बहादुर सप्रू और एम.आर. जयकर ने मध्यस्थता की", "type": "leaf"},
                {"label": "सविनय अवज्ञा को स्थगित किया गया; कांग्रेस द्वितीय गोलमेज सम्मेलन में भाग लेने पर सहमत हुई", "type": "leaf"}]},
            {"label": "रियायतें", "type": "branch", "date": "शर्तें", "children": [
                {"label": "अहिंसक राजनीतिक कैदियों की तत्काल रिहाई; बिना बिकी जब्त जमीनों की वापसी", "type": "leaf"},
                {"label": "तटीय गांवों में स्थानीय लोगों को घरेलू उपयोग के लिए नमक बनाने और एकत्र करने का अधिकार मिला", "type": "leaf"},
                {"label": "सरकार ने पुलिस ज्यादतियों की जांच और भगत सिंह, सुखदेव व राजगुरु की फांसी की सजा बदलने की मांग खारिज की", "type": "leaf"}]}
        ]
    },
    "karachi-session": {
        "en": [
            {"label": "Context", "type": "branch", "date": "March 1931", "children": [
                {"label": "Presided by Sardar Vallabhbhai Patel; delegates wore black bands to protest Bhagat Singh's execution", "type": "leaf"},
                {"label": "Endorsed the Gandhi-Irwin Delhi Pact", "type": "leaf"}]},
            {"label": "Resolutions", "type": "branch", "date": "Landmarks", "children": [
                {"label": "Fundamental Rights: Resolution drafted by Nehru; guaranteed free speech, equality, religious neutrality, adult suffrage", "type": "leaf"},
                {"label": "National Economic Program: Drafted by Nehru; demanded state ownership of key industries/mines, rent reduction, labor protection", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संदर्भ", "type": "branch", "date": "मार्च 1931", "children": [
                {"label": "सरदार वल्लभभाई पटेल की अध्यक्षता; भगत सिंह की फांसी के विरोध में प्रतिनिधियों ने काली पट्टियां बांधी", "type": "leaf"},
                {"label": "गांधी-इरविन दिल्ली समझौते को मंजूरी दी गई", "type": "leaf"}]},
            {"label": "ऐतिहासिक प्रस्ताव", "type": "branch", "date": "प्रस्ताव", "children": [
                {"label": "मौलिक अधिकार: नेहरू द्वारा प्रारूपित प्रस्ताव; अभिव्यक्ति की स्वतंत्रता, समानता, धार्मिक तटस्थता, वयस्क मताधिकार की गारंटी", "type": "leaf"},
                {"label": "राष्ट्रीय आर्थिक कार्यक्रम: नेहरू द्वारा प्रारूपित; मुख्य उद्योगों/खदानों के राष्ट्रीयकरण, लगान में कमी, श्रम संरक्षण की मांग", "type": "leaf"}]}
        ]
    },
    "round-table-conferences": {
        "en": [
            {"label": "First RTC (1930)", "type": "branch", "date": "No Congress", "children": [
                {"label": "Boycotted by INC; attended by Muslim League (Jinnah), Liberals (Sapru), Depressed Classes (Ambedkar)", "type": "leaf"},
                {"label": "Discussed federal structure for India; ended without major breakthrough", "type": "leaf"}]},
            {"label": "Second RTC (1931)", "type": "branch", "date": "Gandhi Attends", "children": [
                {"label": "Gandhi attended as sole Congress representative; deadlock over minority representation & electorates", "type": "leaf"},
                {"label": "Ambedkar demanded separate electorates for Dalits, strongly opposed by Gandhi who went on fast later", "type": "leaf"}]},
            {"label": "Third RTC (1932)", "type": "branch", "date": "No Congress", "children": [
                {"label": "Boycotted again by Congress; only 46 delegates attended; led to the White Paper outlining reforms", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम गोलमेज (1930)", "type": "branch", "date": "कांग्रेस रहित", "children": [
                {"label": "कांग्रेस द्वारा बहिष्कार; मुस्लिम लीग (जिन्ना), उदारवादियों (सप्रू), दलित वर्ग (अंबेडकर) ने भाग लिया", "type": "leaf"},
                {"label": "भारत के लिए संघीय ढांचे पर चर्चा; बिना किसी बड़े समझौते के समाप्त", "type": "leaf"}]},
            {"label": "द्वितीय गोलमेज (1931)", "type": "branch", "date": "गांधीजी शामिल", "children": [
                {"label": "गांधीजी कांग्रेस के एकमात्र प्रतिनिधि के रूप में शामिल हुए; अल्पसंख्यकों और निर्वाचन मंडलों पर गतिरोध", "type": "leaf"},
                {"label": "अंबेडकर ने दलितों के लिए पृथक निर्वाचन की मांग की, जिसका गांधीजी ने कड़ा विरोध किया", "type": "leaf"}]},
            {"label": "तृतीय गोलमेज (1932)", "type": "branch", "date": "कांग्रेस रहित", "children": [
                {"label": "कांग्रेस द्वारा पुनः बहिष्कार; केवल 46 प्रतिनिधि शामिल हुए; सुधारों की रूपरेखा वाला श्वेत पत्र जारी", "type": "leaf"}]}
        ]
    },
    "communal-award": {
        "en": [
            {"label": "The Award", "type": "branch", "date": "August 16, 1932", "children": [
                {"label": "Announced by British PM Ramsay MacDonald; extended separate electorates to Depressed Classes (treating Dalits as minorities)", "type": "leaf"},
                {"label": "Maintained separate electorates for Muslims, Sikhs, Christians, Anglo-Indians", "type": "leaf"}]},
            {"label": "Gandhi's Fast", "type": "branch", "date": "Yerwada Jail", "children": [
                {"label": "Gandhi opposed treating Dalits as separate from Hindu fold; started fast-unto-death in Yerwada Jail on Sept 20, 1932", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सांप्रदायिक पंचाट", "type": "branch", "date": "16 अगस्त 1932", "children": [
                {"label": "ब्रिटिश पीएम रैमसे मैकडोनाल्ड द्वारा घोषित; दलित वर्गों (दलितों को अल्पसंख्यक मानते हुए) के लिए पृथक निर्वाचन लागू किया", "type": "leaf"},
                {"label": "मुसलमानों, सिखों, ईसाइयों, एंग्लो-इंडियंस के लिए पृथक निर्वाचन मंडल बनाए रखे", "type": "leaf"}]},
            {"label": "गांधीजी का अनशन", "type": "branch", "date": "यरवदा जेल", "children": [
                {"label": "दलितों को हिंदू समाज से अलग करने के विरोध में गांधीजी ने 20 सितंबर 1932 को यरवदा जेल में आमरण अनशन शुरू किया", "type": "leaf"}]}
        ]
    },
    "poona-pact": {
        "en": [
            {"label": "The Agreement", "type": "branch", "date": "Sept 24, 1932", "children": [
                {"label": "Signed between B.R. Ambedkar (for Dalits) and Madan Mohan Malaviya (for caste Hindus) to end Gandhi's fast", "type": "leaf"},
                {"label": "Abandoned separate electorates for depressed classes in favor of joint electorates with reserved seats", "type": "leaf"}]},
            {"label": "Seat Reservation", "type": "branch", "date": "Seats", "children": [
                {"label": "Reserved seats in provincial legislatures increased from 71 (Communal Award) to 147", "type": "leaf"},
                {"label": "Secured 18% reservation in Central Legislature; government accepted the pact, modifying the Communal Award", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पूना समझौता", "type": "branch", "date": "24 सितंबर 1932", "children": [
                {"label": "गांधीजी का अनशन समाप्त कराने हेतु बी.आर. अंबेडकर (दलितों के लिए) और मदन मोहन मालवीय (सनातनी हिंदुओं के लिए) के बीच हस्ताक्षरित", "type": "leaf"},
                {"label": "आरक्षित सीटों के साथ संयुक्त निर्वाचन के पक्ष में दलित वर्गों के लिए पृथक निर्वाचन की मांग छोड़ दी गई", "type": "leaf"}]},
            {"label": "सीटों का आरक्षण", "type": "branch", "date": "सीटें", "children": [
                {"label": "प्रांतीय विधानसभाओं में आरक्षित सीटें 71 (सांप्रदायिक पंचाट) से बढ़ाकर 147 कर दी गईं", "type": "leaf"},
                {"label": "केंद्रीय विधानमंडल में 18% आरक्षण प्रदान किया गया; ब्रिटिश सरकार ने समझौते को स्वीकार कर पंचाट में संशोधन किया", "type": "leaf"}]}
        ]
    },
    "goi-act-1935": {
        "en": [
            {"label": "Federal Proposal", "type": "branch", "date": "Federation", "children": [
                {"label": "Proposed All-India Federation of British provinces & Princely States (failed due to non-accession of princes)", "type": "leaf"},
                {"label": "Three lists: Federal, Provincial, Concurrent; residuary powers vested in Governor-General", "type": "leaf"}]},
            {"label": "Provincial Reforms", "type": "branch", "date": "Provinces", "children": [
                {"label": "Abolished Dyarchy in provinces; introduced Provincial Autonomy (responsible governments)", "type": "leaf"}]},
            {"label": "Central Reforms & Institutions", "type": "branch", "date": "Center", "children": [
                {"label": "Introduced Dyarchy at the Center; Reserved subjects (Defense, External Affairs) under Governor-General", "type": "leaf"},
                {"label": "Established Federal Court (1937) and Reserve Bank of India (1935)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संघीय प्रस्ताव", "type": "branch", "date": "संघ", "children": [
                {"label": "ब्रिटिश प्रांतों और रियासतों को मिलाकर एक अखिल भारतीय संघ का प्रस्ताव (रियासतों के शामिल न होने से विफल)", "type": "leaf"},
                {"label": "तीन सूचियाँ: संघीय, प्रांतीय, समवर्ती; अवशिष्ट शक्तियां गवर्नर-जनरल में निहित", "type": "leaf"}]},
            {"label": "प्रांतीय सुधार", "type": "branch", "date": "प्रांत", "children": [
                {"label": "प्रांतों में द्वैध शासन समाप्त; प्रांतीय स्वायत्तता (उत्तरदायी सरकारें) की शुरुआत की गई", "type": "leaf"}]},
            {"label": "केंद्रीय सुधार और संस्थाएं", "type": "branch", "date": "केंद्र", "children": [
                {"label": "केंद्र में द्वैध शासन की शुरुआत; आरक्षित विषय (रक्षा, विदेश मामले) गवर्नर-जनरल के अधीन", "type": "leaf"},
                {"label": "संघीय न्यायालय (1937) और भारतीय रिजर्व बैंक (1935) की स्थापना के प्रावधान", "type": "leaf"}]}
        ]
    },
    "congress-ministries": {
        "en": [
            {"label": "1937 Elections", "type": "branch", "date": "Elections", "children": [
                {"label": "Congress won absolute majority in 5 provinces and formed ministries in 8 provinces", "type": "leaf"},
                {"label": "Reforms: Reduced land rents, regulated moneylending, released political prisoners, lifted press bans", "type": "leaf"}]},
            {"label": "Resignation (1939)", "type": "branch", "date": "WWI protest", "children": [
                {"label": "Ministries resigned in October 1939 protesting India being dragged into WWI without consulting legislatures", "type": "leaf"},
                {"label": "Muslim League celebrated Resignation Day as 'Deliverance Day' (Day of Deliverance) on Dec 22, 1939", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "1937 के चुनाव", "type": "branch", "date": "चुनाव", "children": [
                {"label": "कांग्रेस ने 5 प्रांतों में पूर्ण बहुमत प्राप्त किया और कुल 8 प्रांतों में अपनी सरकारें बनाईं", "type": "leaf"},
                {"label": "सुधार: लगान में कमी, साहूकारी पर नियंत्रण, राजनीतिक कैदियों की रिहाई, प्रेस पर से प्रतिबंध हटाए", "type": "leaf"}]},
            {"label": "इस्तीफा (1939)", "type": "branch", "date": "युद्ध विरोध", "children": [
                {"label": "बिना सहमति भारत को द्वितीय विश्व युद्ध में शामिल करने के विरोध में अक्टूबर 1939 में मंत्रालयों ने इस्तीफा दिया", "type": "leaf"},
                {"label": "मुस्लिम लीग ने 22 दिसंबर 1939 को इस इस्तीफे को 'मुक्ति दिवस' (डे ऑफ डिलीवरेंस) के रूप में मनाया", "type": "leaf"}]}
        ]
    },
    "august-offer": {
        "en": [
            {"label": "The Offer", "type": "branch", "date": "August 1940", "children": [
                {"label": "Announced by Viceroy Linlithgow to secure Indian cooperation in World War II", "type": "leaf"},
                {"label": "Promised Dominion Status after war; representative constituent assembly", "type": "leaf"},
                {"label": "Minority Veto: Stated no constitution would be accepted without consent of large minorities", "type": "leaf"}]},
            {"label": "Rejection", "type": "branch", "date": "Rejection", "children": [
                {"label": "Congress rejected it; Nehru stated: 'Dominion status concept is dead as a doornail'", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रस्ताव", "type": "branch", "date": "अगस्त 1940", "children": [
                {"label": "द्वितीय विश्व युद्ध में भारतीय सहयोग प्राप्त करने हेतु वायसराय लिनलिथगो द्वारा घोषित", "type": "leaf"},
                {"label": "युद्ध के बाद डोमिनियन स्टेटस और एक प्रतिनिधि संविधान सभा के गठन का वादा", "type": "leaf"},
                {"label": "अल्पसंख्यकों को वीटो: घोषित किया कि किसी भी बड़े अल्पसंख्यक वर्ग की असहमति पर संविधान स्वीकार नहीं होगा", "type": "leaf"}]},
            {"label": "अस्वीकृति", "type": "branch", "date": "अस्वीकृति", "children": [
                {"label": "कांग्रेस द्वारा अस्वीकृत; नेहरू ने कहा: 'डोमिनियन स्टेटस का विचार दीवार में गड़ी कील की तरह मृत है'", "type": "leaf"}]}
        ]
    },
    "individual-satyagraha": {
        "en": [
            {"label": "Launch & Aims", "type": "branch", "date": "Oct 1940", "children": [
                {"label": "Launched by Gandhi to assert right to free speech against war; to show India's patience was not weakness", "type": "leaf"}]},
            {"label": "Satyagrahis", "type": "branch", "date": "Leaders", "children": [
                {"label": "Vinoba Bhave (1st Satyagrahi), Jawaharlal Nehru (2nd), Brahma Datt (3rd)", "type": "leaf"},
                {"label": "Popularly called 'Delhi Chalo' movement; over 25,000 satyagrahis courted arrest", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "शुरुआत और उद्देश्य", "type": "branch", "date": "अक्टूबर 1940", "children": [
                {"label": "युद्ध विरोधी भाषण के अधिकार को जताने और यह दिखाने के लिए कि भारत का धैर्य कमजोरी नहीं है, गांधीजी द्वारा शुरू", "type": "leaf"}]},
            {"label": "सत्याग्रही", "type": "branch", "date": "नेता", "children": [
                {"label": "विनोबा भावे (प्रथम सत्याग्रही), जवाहरलाल नेहरू (द्वितीय), ब्रह्म दत्त (तृतीय)", "type": "leaf"},
                {"label": "इसे 'दिल्ली चलो' आंदोलन भी कहा गया; 25,000 से अधिक सत्याग्रहियों ने गिरफ्तारियां दीं", "type": "leaf"}]}
        ]
    },
    "cripps-mission": {
        "en": [
            {"label": "Proposals", "type": "branch", "date": "March 1942", "children": [
                {"label": "Led by Stafford Cripps to secure Indian support as Japan occupied Rangoon and advanced towards India", "type": "leaf"},
                {"label": "Dominion Status after war; provinces allowed to opt out of the union (blueprint for partition)", "type": "leaf"}]},
            {"label": "Rejection", "type": "branch", "date": "Rejection", "children": [
                {"label": "Gandhi called it a 'post-dated cheque on a crashing bank'", "type": "leaf"},
                {"label": "Rejected because it did not offer immediate transfer of power or cabinet responsibility", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रस्ताव", "type": "branch", "date": "मार्च 1942", "children": [
                {"label": "जापान के रंगून पर कब्जे और भारत की ओर बढ़ने पर सहयोग प्राप्त करने हेतु स्टैफ़ोर्ड क्रिप्स के नेतृत्व में मिशन", "type": "leaf"},
                {"label": "युद्ध के बाद डोमिनियन स्टेटस; प्रांतों को संघ से अलग होने की छूट (विभाजन की रूपरेखा)", "type": "leaf"}]},
            {"label": "अस्वीकृति", "type": "branch", "date": "अस्वीकृति", "children": [
                {"label": "गांधीजी ने इसे 'दिवालिया होने वाले बैंक का उत्तर-दिनांकित चेक' (पोस्ट-डेटेड चेक) कहा", "type": "leaf"},
                {"label": "अस्वीकृत किया गया क्योंकि इसमें तत्काल वास्तविक सत्ता हस्तांतरण या वास्तविक कैबिनेट जिम्मेदारी नहीं थी", "type": "leaf"}]}
        ]
    },
    "quit-india-movement": {
        "en": [
            {"label": "Resolution & Slogan", "type": "branch", "date": "August 1942", "children": [
                {"label": "Drafted at Wardha; ratified at Gowalia Tank (Bombay) on Aug 8, 1942; Gandhi's slogan 'Do or Die'", "type": "leaf"}]},
            {"label": "Repression & Resistance", "type": "branch", "date": "Aug 9", "children": [
                {"label": "Operation Zero Hour: All top leaders arrested early morning Aug 9; Congress declared illegal", "type": "leaf"},
                {"label": "Underground leaders: Usha Mehta (illegal radio), Aruna Asaf Ali, JP Narayan, Achyut Patwardhan", "type": "leaf"}]},
            {"label": "Parallel Governments", "type": "branch", "date": "1942-44", "children": [
                {"label": "Ballia (UP): Under Chittu Pandey; Tamluk (Bengal): Jatiya Sarkar; Satara (Maharashtra): Prati Sarkar (Nana Patil)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रस्ताव और नारा", "type": "branch", "date": "अगस्त 1942", "children": [
                {"label": "वर्धा में तैयार; 8 अगस्त 1942 को बम्बई के ग्वालिया टैंक में अनुमोदित; गांधीजी का नारा 'करो या मरो'", "type": "leaf"}]},
            {"label": "दमन और प्रतिरोध", "type": "branch", "date": "9 अगस्त", "children": [
                {"label": "ऑपरेशन जीरो ऑवर: 9 अगस्त की सुबह सभी बड़े नेता गिरफ्तार; कांग्रेस को अवैध घोषित किया गया", "type": "leaf"},
                {"label": "भूमिगत नेता: उषा मेहता (अवैध रेडियो संचालक), अरुणा आसफ अली, जे.पी. नारायण, अच्युत पटवर्धन", "type": "leaf"}]},
            {"label": "समानांतर सरकारें", "type": "branch", "date": "1942-44", "children": [
                {"label": "बलिया (यूपी): चित्तू पांडे के नेतृत्व में; तामलुक (बंगाल): जातीय सरकार; सतारा (महाराष्ट्र): प्रति सरकार (नाना पाटिल)", "type": "leaf"}]}
        ]
    },
    "bose-and-ina": {
        "en": [
            {"label": "INA Origins", "type": "branch", "date": "1942-43", "children": [
                {"label": "First phase formed by Mohan Singh in Malaya; Tokyo (March 1942) & Bangkok (June 1942) conferences decided setup", "type": "leaf"},
                {"label": "Rash Behari Bose handed over leadership to Subhas Chandra Bose in Singapore (July 1943)", "type": "leaf"}]},
            {"label": "Provisional Government & Action", "type": "branch", "date": "1943-45", "children": [
                {"label": "Arzi Hukumat-i-Azad Hind formed in Singapore in Oct 1943; recognized by Axis powers", "type": "leaf"},
                {"label": "Slogans: 'Chalo Delhi' and 'Jai Hind'; Rani of Jhansi women's regiment under Lakshmi Swaminathan", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आजाद हिंद फौज", "type": "branch", "date": "1942-43", "children": [
                {"label": "मोहन सिंह द्वारा मलाया में प्रथम चरण का गठन; टोक्यो (मार्च 1942) और बैंकॉक (जून 1942) सम्मेलनों में रूपरेखा तय", "type": "leaf"},
                {"label": "रास बिहारी बोस ने जुलाई 1943 में सिंगापुर में सुभाष चंद्र बोस को नेतृत्व सौंपा", "type": "leaf"}]},
            {"label": "अस्थायी सरकार और कार्रवाई", "type": "branch", "date": "1943-45", "children": [
                {"label": "अक्टूबर 1943 में सिंगापुर में आरज़ी हुक़ूमत-ए-आज़ाद हिंद (अस्थायी सरकार) का गठन किया गया", "type": "leaf"},
                {"label": "नारे: 'दिल्ली चलो' और 'जय हिंद'; लक्ष्मी स्वामीनाथन के नेतृत्व में रानी झांसी रेजीमेंट का गठन", "type": "leaf"}]}
        ]
    },
    "c-r-formula": {
        "en": [
            {"label": "The Formula", "type": "branch", "date": "1944", "children": [
                {"label": "Proposed by C. Rajagopalachari to resolve Congress-League deadlock over partition", "type": "leaf"},
                {"label": "League to endorse Congress demand for independence; cooperate in forming interim government", "type": "leaf"},
                {"label": "After war, plebiscite in Muslim-majority districts of NW & East India to decide separation", "type": "leaf"}]},
            {"label": "Jinnah's Veto", "type": "branch", "date": "Rejection", "children": [
                {"label": "Jinnah rejected it; wanted Congress to accept the Two-Nation Theory first, opposing common center setup", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सीआर फार्मूला", "type": "branch", "date": "1944", "children": [
                {"label": "विभाजन पर कांग्रेस-लीग गतिरोध को दूर करने हेतु सी. राजगोपालाचारी द्वारा प्रस्तावित", "type": "leaf"},
                {"label": "लीग द्वारा कांग्रेस की स्वतंत्रता की मांग का समर्थन; अंतरिम सरकार के गठन में सहयोग की बात", "type": "leaf"},
                {"label": "कहा गया कि युद्ध के बाद, उत्तर-पश्चिम और पूर्वी भारत के मुस्लिम-बहुल जिलों में विभाजन पर जनमत संग्रह हो", "type": "leaf"}]},
            {"label": "जिन्ना की अस्वीकृति", "type": "branch", "date": "अस्वीकृति", "children": [
                {"label": "जिन्ना ने खारिज किया; वे चाहते थे कि कांग्रेस पहले द्वि-राष्ट्र सिद्धांत स्वीकार करे; साझा केंद्र का विरोध किया", "type": "leaf"}]}
        ]
    },
    "desai-liaquat-pact": {
        "en": [
            {"label": "Proposals", "type": "branch", "date": "1945", "children": [
                {"label": "Drafted by Bhulabhai Desai (Congress) and Liaquat Ali Khan (Muslim League) to form interim government", "type": "leaf"},
                {"label": "Proposed equal representation for Congress & League in central executive (40% each; 20% minorities)", "type": "leaf"},
                {"label": "No official endorsement received from either party high commands; pact failed", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रस्ताव", "type": "branch", "date": "1945", "children": [
                {"label": "अंतरिम सरकार गठन हेतु भूलाभाई देसाई (कांग्रेस) और लियाकत अली खान (मुस्लिम लीग) द्वारा तैयार प्रारूप", "type": "leaf"},
                {"label": "केंद्रीय कार्यकारिणी में कांग्रेस और लीग के लिए समान प्रतिनिधित्व का प्रस्ताव (40-40% दोनों; 20% अल्पसंख्यक)", "type": "leaf"},
                {"label": "दोनों दलों के शीर्ष नेतृत्व द्वारा औपचारिक मंजूरी न मिलने के कारण समझौता विफल रहा", "type": "leaf"}]}
        ]
    },
    "rin-mutiny": {
        "en": [
            {"label": "The Revolt", "type": "branch", "date": "Feb 1946", "children": [
                {"label": "Royal Indian Navy ratings on HMIS Talwar (Bombay) went on strike protesting bad food and racial abuse", "type": "leaf"},
                {"label": "Led by BC Dutt; ratings hoisted Congress, League, and Communist flags on naval ships", "type": "leaf"},
                {"label": "Spread to Karachi, Calcutta; Sardar Patel and Jinnah intervened to advise surrender (Feb 23, 1946)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नौसेना विद्रोह", "type": "branch", "date": "फरवरी 1946", "children": [
                {"label": "बॉम्बे में आईएनएस तलवार (HMIS Talwar) के नाविकों ने खराब भोजन और नस्लीय दुर्व्यवहार के खिलाफ हड़ताल शुरू की", "type": "leaf"},
                {"label": "बी.सी. दत्त के नेतृत्व में; नाविकों ने नौसैनिक जहाजों पर कांग्रेस, लीग और कम्युनिस्ट झंडे फहराए", "type": "leaf"},
                {"label": "कराची, कलकत्ता तक प्रसार; सरदार पटेल और जिन्ना के हस्तक्षेप पर नाविकों ने आत्मसमर्पण किया (23 फरवरी 1946)", "type": "leaf"}]}
        ]
    },
    "cabinet-mission": {
        "en": [
            {"label": "Proposals", "type": "branch", "date": "1946", "children": [
                {"label": "Sent under Pethick-Lawrence, Stafford Cripps, and A.V. Alexander; rejected separate Pakistan state", "type": "leaf"},
                {"label": "Proposed a loose federal union of India with three sections/groups of provinces (Grouping System)", "type": "leaf"},
                {"label": "Group A (Hindu majority), Group B (Muslim majority NW), Group C (Muslim majority East)", "type": "leaf"},
                {"label": "Proposed a Constituent Assembly elected by provincial assemblies; interim government setup", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कैबिनेट मिशन प्रस्ताव", "type": "branch", "date": "1946", "children": [
                {"label": "पैथिक लॉरेंस, स्टैफ़ोर्ड क्रिप्स और ए.वी. अलेक्जेंडर के नेतृत्व में; पृथक पाकिस्तान राज्य की मांग खारिज की", "type": "leaf"},
                {"label": "प्रांतों के तीन समूहों/खंडों (ग्रुपिंग सिस्टम) के साथ भारत के एक ढीले संघीय संघ का प्रस्ताव दिया", "type": "leaf"},
                {"label": "ग्रुप A (हिंदू बहुल), ग्रुप B (मुस्लिम बहुल उत्तर-पश्चिम), ग्रुप C (मुस्लिम बहुल पूर्व)", "type": "leaf"},
                {"label": "प्रांतीय विधानसभाओं द्वारा चुनी गई संविधान सभा और अंतरिम सरकार के गठन का प्रस्ताव", "type": "leaf"}]}
        ]
    },
    "direct-action-day": {
        "en": [
            {"label": "Direct Action", "type": "branch", "date": "Aug 16, 1946", "children": [
                {"label": "Called by Jinnah after League withdrew acceptance of Cabinet Mission Plan to force Pakistan demand", "type": "leaf"},
                {"label": "Led to massive communal riots (Great Calcutta Killings) in Bengal under H.S. Suhrawardy administration", "type": "leaf"},
                {"label": "Communal violence spread to Noakhali (Bihar) and Punjab, cementing partition inevitability", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रत्यक्ष कार्रवाई", "type": "branch", "date": "16 अगस्त 1946", "children": [
                {"label": "कैबिनेट मिशन योजना की स्वीकृति वापस लेने के बाद जिन्ना द्वारा पाकिस्तान की मांग मनवाने हेतु आह्वान", "type": "leaf"},
                {"label": "बंगाल में एच.एस. सुहरावर्दी प्रशासन के तहत भयानक सांप्रदायिक दंगे (ग्रेट कलकत्ता किलिंग्स) भड़के", "type": "leaf"},
                {"label": "सांस्कृतिक हिंसा नोआखली (बिहार) और पंजाब में फैली, जिससे विभाजन अपरिहार्य हो गया", "type": "leaf"}]}
        ]
    },
    "interim-government": {
        "en": [
            {"label": "Formation", "type": "branch", "date": "Sept 1946", "children": [
                {"label": "Formed on Sept 2, 1946; Jawaharlal Nehru headed as Vice President of Executive Council", "type": "leaf"},
                {"label": "Muslim League initially boycotted; joined in Oct 1946 with Liaquat Ali Khan getting Finance portfolio", "type": "leaf"}]},
            {"label": "Constituent Assembly", "type": "branch", "date": "Assembly", "children": [
                {"label": "First meeting on Dec 9, 1946; Dr. Sachchidanand Sinha was temporary president; Rajendra Prasad elected permanent president on Dec 11", "type": "leaf"},
                {"label": "Objective Resolution introduced by Jawaharlal Nehru on Dec 13, 1946; adopted Jan 22, 1947", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "गठन", "type": "branch", "date": "सितंबर 1946", "children": [
                {"label": "2 सितंबर 1946 को गठित; जवाहरलाल नेहरू कार्यकारी परिषद के उपाध्यक्ष के रूप में प्रमुख बने", "type": "leaf"},
                {"label": "मुस्लिम लीग ने शुरू में बहिष्कार किया; अक्टूबर 1946 में शामिल हुई और लियाकत अली को वित्त मंत्रालय मिला", "type": "leaf"}]},
            {"label": "संविधान सभा", "type": "branch", "date": "सभा", "children": [
                {"label": "9 दिसंबर 1946 को प्रथम बैठक; डॉ. सच्चिदानंद सिन्हा अस्थायी अध्यक्ष; 11 दिसंबर को राजेंद्र प्रसाद स्थायी अध्यक्ष बने", "type": "leaf"},
                {"label": "जवाहरलाल नेहरू द्वारा 13 दिसंबर 1946 को उद्देश्य प्रस्ताव पेश किया गया; 22 जनवरी 1947 को स्वीकृत हुआ", "type": "leaf"}]}
        ]
    },
    "partition-and-independence": {
        "en": [
            {"label": "Mountbatten Plan", "type": "branch", "date": "June 3, 1947", "children": [
                {"label": "Viceroy Lord Mountbatten proposed partition of Bengal & Punjab; boundary commission (Radcliffe)", "type": "leaf"},
                {"label": "Congress & League accepted; princely states allowed to join India, Pakistan, or remain independent", "type": "leaf"}]},
            {"label": "Independence Act", "type": "branch", "date": "July 1947", "children": [
                {"label": "Indian Independence Act 1947 passed by British Parliament; fixed Aug 15, 1947 as independence date", "type": "leaf"},
                {"label": "Created two independent Dominions: India and Pakistan", "type": "leaf"}]},
            {"label": "Integration", "type": "branch", "date": "States", "children": [
                {"label": "Sardar Patel and V.P. Menon managed integration of 562 princely states; Junagadh, Hyderabad, Jammu & Kashmir resolved later", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "माउंटबेटन योजना", "type": "branch", "date": "3 जून 1947", "children": [
                {"label": "वायसराय लॉर्ड माउंटबेटन ने बंगाल और पंजाब के विभाजन तथा सीमा आयोग (रैडक्लिफ) का प्रस्ताव दिया", "type": "leaf"},
                {"label": "कांग्रेस और लीग ने स्वीकार किया; रियासतों को भारत या पाकिस्तान में शामिल होने अथवा स्वतंत्र रहने की छूट मिली", "type": "leaf"}]},
            {"label": "स्वतंत्रता अधिनियम", "type": "branch", "date": "जुलाई 1947", "children": [
                {"label": "ब्रिटिश संसद द्वारा भारतीय स्वतंत्रता अधिनियम 1947 पारित; 15 अगस्त 1947 को स्वतंत्रता की तिथि नियत की गई", "type": "leaf"},
                {"label": "दो स्वतंत्र डोमिनियन: भारत और पाकिस्तान का सृजन किया गया", "type": "leaf"}]},
            {"label": "एकीकरण", "type": "branch", "date": "रियासतें", "children": [
                {"label": "सरदार पटेल और वी.पी. मेनन ने 562 रियासतों का विलय कराया; जूनागढ़, हैदराबाद, जम्मू-कश्मीर का समाधान बाद में हुआ", "type": "leaf"}]}
        ]
    },
    "viceroys": {
        "en": [
            {"label": "Governor-Generals (1832-58)", "type": "branch", "date": "GGs", "children": [
                {"label": "William Bentinck: First GG of India (Charter Act 1833); abolished Sati; English education", "type": "leaf"},
                {"label": "Dalhousie (1848-56): Introduced Doctrine of Lapse, Railways (1853), Telegraph, Wood's Despatch", "type": "leaf"}]},
            {"label": "Viceroys (1858-1947)", "type": "branch", "date": "Viceroys", "children": [
                {"label": "Canning: First Viceroy (GoI Act 1858); suppressed 1857 revolt; portfolio system", "type": "leaf"},
                {"label": "Lytton (1876-80): Vernacular Press Act, Arms Act; Curzon (1899-1905): Partition of Bengal", "type": "leaf"},
                {"label": "Irwin: Gandhi-Irwin Pact (1931); Linlithgow (1936-43): Longest tenure, WWII, Quit India", "type": "leaf"},
                {"label": "Mountbatten: Last Viceroy; oversaw partition and transfer of power", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "गवर्नर-जनरल (1832-58)", "type": "branch", "date": "जीजी", "children": [
                {"label": "विलियम बेंटिक: भारत के प्रथम जीजी (1833 एक्ट); सती प्रथा का अंत; अंग्रेजी शिक्षा प्रणाली", "type": "leaf"},
                {"label": "डलहौजी (1848-56): हड़प नीति (व्यपगत सिद्धांत), रेलवे की शुरुआत (1853), तार सेवा, वुड्स डिस्पैच", "type": "leaf"}]},
            {"label": "वायसराय (1858-1947)", "type": "branch", "date": "वायसराय", "children": [
                {"label": "कैनिंग: प्रथम वायसराय (1858 एक्ट); 1857 के विद्रोह का दमन; पोर्टफोलियो प्रणाली की शुरुआत", "type": "leaf"},
                {"label": "लिटन (1876-80): वर्नाक्यूलर प्रेस एक्ट, आर्म्स एक्ट; कर्जन (1899-1905): बंगाल विभाजन", "type": "leaf"},
                {"label": "इरविन: Gandhi-Irwin Pact (1931); लिनलिथगो (1936-43): सबसे लंबा कार्यकाल, द्वितीय विश्व युद्ध, भारत छोड़ो", "type": "leaf"},
                {"label": "माउंटबेटन: अंतिम वायसराय; विभाजन और सत्ता के हस्तांतरण का संचालन किया", "type": "leaf"}]}
        ]
    },
    "pakistan-resolution": {
        "en": [
            {"label": "Lahore Resolution", "type": "branch", "date": "March 23, 1940", "children": [
                {"label": "Passed at the Lahore session of All India Muslim League presided by M.A. Jinnah", "type": "leaf"},
                {"label": "Drafted by Sikandar Hayat Khan; moved by Fazlul Huq (Sher-e-Bangla)", "type": "leaf"},
                {"label": "Demanded geographically contiguous units in NW and East India to be grouped as independent states", "type": "leaf"},
                {"label": "Word 'Pakistan' was not explicitly used in resolution, but became popular name", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लाहौर प्रस्ताव", "type": "branch", "date": "23 मार्च 1940", "children": [
                {"label": "एम.ए. जिन्ना की अध्यक्षता में ऑल इंडिया मुस्लिम लीग के लाहौर अधिवेशन में पारित किया गया", "type": "leaf"},
                {"label": "सिकंदर हयात खान द्वारा प्रारूप तैयार; फजलुल हक (शेर-ए-बंगाल) द्वारा प्रस्तुत किया गया", "type": "leaf"},
                {"label": "उत्तर-पश्चिम और पूर्वी भारत की भौगोलिक रूप से निकट इकाइयों को स्वतंत्र राज्यों के रूप में गठित करने की मांग", "type": "leaf"},
                {"label": "प्रस्ताव में 'पाकिस्तान' शब्द का स्पष्ट उल्लेख नहीं था, लेकिन यह लोकप्रिय नाम बन गया", "type": "leaf"}]}
        ]
    },
    "leaders-and-roles": {
        "en": [
            {"label": "Key Figures", "type": "branch", "date": "Leaders", "children": [
                {"label": "Mahatma Gandhi: Quit India movement organizer; fasts in Pune jail; pilgrimage to Noakhali for peace", "type": "leaf"},
                {"label": "Subhas Chandra Bose: Escape to Germany (1941), Japan (1943); formed Azad Hind Fauj & provisional govt", "type": "leaf"},
                {"label": "Sardar Patel: Integrated princely states; chaired Fundamental Rights committee in Constituent Assembly", "type": "leaf"},
                {"label": "Jawaharlal Nehru: Vice President of Interim Govt; drafted Objective Resolution; drafted Poorna Swaraj resolution", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख व्यक्तित्व", "type": "branch", "date": "नेता", "children": [
                {"label": "महात्मा गांधी: भारत छोड़ो आंदोलन के सूत्रधार; पुणे जेल में उपवास; शांति स्थापना हेतु नोआखली यात्रा", "type": "leaf"},
                {"label": "सुभाष चंद्र बोस: जर्मनी पलायन (1941), जापान (1943); आजाद हिंद फौज और अस्थायी सरकार का गठन", "type": "leaf"},
                {"label": "सरदार पटेल: रियासतों का एकीकरण कराया; संविधान सभा में मौलिक अधिकार समिति के अध्यक्ष रहे", "type": "leaf"},
                {"label": "जवाहरलाल नेहरू: अंतरिम सरकार के उपाध्यक्ष; उद्देश्य प्रस्ताव का प्रारूप तैयार किया; पूर्ण स्वराज प्रस्ताव के लेखक", "type": "leaf"}]}
        ]
    },
    "generic-topic": {
        "en": [
            {"label": "Historical Context", "type": "branch", "date": "1930-1947", "children": [
                {"label": "Third Phase of National Movement marked by final push for complete independence (Poorna Swaraj)", "type": "leaf"},
                {"label": "Mass movements like Civil Disobedience and Quit India shattered British administrative control", "type": "leaf"},
                {"label": "Negotiations under Cripps, Cabinet Mission, and Mountbatten Plan concluded with independence and partition", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "ऐतिहासिक संदर्भ", "type": "branch", "date": "1930-1947", "children": [
                {"label": "राष्ट्रीय आंदोलन का तीसरा चरण पूर्ण स्वतंत्रता (पूर्ण स्वराज) के अंतिम संघर्ष से चिह्नित था", "type": "leaf"},
                {"label": "सविनय अवज्ञा और भारत छोड़ो जैसे जन आंदोलनों ने ब्रिटिश प्रशासनिक नियंत्रण को छिन्न-भिन्न कर दिया", "type": "leaf"},
                {"label": "क्रिप्स, कैबिनेट मिशन और माउंटबेटन योजना के तहत वार्ता का अंत स्वतंत्रता और विभाजन के रूप में हुआ", "type": "leaf"}]}
        ]
    }
}

# Mapping all 64 folders to the canonical keys
MINDMAP_MAPPINGS = {
    "aicc-meeting": "quit-india-movement",
    "aicc-meeting-gowalia-tank-bombay": "quit-india-movement",
    "atlees-declaration-and-transfer-of-power": "partition-and-independence",
    "august-offer": "august-offer",
    "august-offer-1940": "august-offer",
    "bangkok-conference-june-1942": "bose-and-ina",
    "c-rajagopalachari-formula": "c-r-formula",
    "c-rajagopalachari-formula-1944": "c-r-formula",
    "cabinet-mission-plan": "cabinet-mission",
    "cabinet-mission-plan-1946": "cabinet-mission",
    "civil-disobedience-movement": "civil-disobedience-movement",
    "communal-awards": "communal-award",
    "communal-awards-1932": "communal-award",
    "comparing-ncm-and-cdm": "civil-disobedience-movement",
    "congress-ministries-after-provincial-elections-of-1937": "congress-ministries",
    "congress-working-committee-at-wardha": "quit-india-movement",
    "constituent-assembly": "interim-government",
    "cripps-mission": "cripps-mission",
    "cripps-mission-1942": "cripps-mission",
    "decision-on-mass-struggle": "quit-india-movement",
    "desai-liaquat-pact": "desai-liaquat-pact",
    "desai-liaquat-pact-1945": "desai-liaquat-pact",
    "direct-action-day": "direct-action-day",
    "direct-action-day-august-16th-1946": "direct-action-day",
    "extent-of-participation-and-possibility-of-settlement": "civil-disobedience-movement",
    "gandhi-irwin-pact": "gandhi-irwin-pact",
    "general-elections-1945": "partition-and-independence",
    "government-of-india-act-1935": "goi-act-1935",
    "governor-generals-of-india": "viceroys",
    "governor-generals-of-india-1832-1858": "viceroys",
    "india-independence-act": "partition-and-independence",
    "india-independence-act-1947": "partition-and-independence",
    "individual-satyagraha": "individual-satyagraha",
    "individual-satyagraha-1941": "individual-satyagraha",
    "integration-of-states": "partition-and-independence",
    "interim-government": "interim-government",
    "karachi-session-of-inc": "karachi-session",
    "karachi-session-of-inc-1931": "karachi-session",
    "leaders-in-this-phase-and-their-role": "leaders-and-roles",
    "mlcongress-response-to-desai-liaquat": "desai-liaquat-pact",
    "mountbatten-plan": "partition-and-independence",
    "mountbatten-plan-june-3-1947": "partition-and-independence",
    "neta-ji-in-japan": "bose-and-ina",
    "neta-ji-in-japan-1943": "bose-and-ina",
    "netaji-subhash-chandra-bose-and-ina": "bose-and-ina",
    "objective-resolution": "interim-government",
    "partition-resolution": "pakistan-resolution",
    "partition-resolution-23-mar-1940": "pakistan-resolution",
    "pakistan-resolution": "pakistan-resolution",
    "pakistan-resolution-23-mar-1940": "pakistan-resolution",
    "parallel-governments": "quit-india-movement",
    "poona-pact": "poona-pact",
    "poona-pact-1932": "poona-pact",
    "provisional-government-of-free-india-singapore": "bose-and-ina",
    "provisional-government-of-free-india-singapore-october-1943": "bose-and-ina",
    "quit-india-movement": "quit-india-movement",
    "quit-india-movement-august-revolution-1942": "quit-india-movement",
    "resignation-of-congress-ministries": "congress-ministries",
    "resignation-of-congress-ministries-1939": "congress-ministries",
    "rin-mutiny": "rin-mutiny",
    "rin-mutiny-1946": "rin-mutiny",
    "the-three-round-table-conferences": "round-table-conferences",
    "the-three-round-table-conferences-rtcs": "round-table-conferences",
    "tokyo-conference-march-1942": "bose-and-ina",
    "viceroy-and-governor-generals-of-india": "viceroys",
    "viceroy-and-governor-generals-of-india-1858-1947": "viceroys"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('NCM', 'NCM (Non-Cooperation Movement)')
    title = title.replace('CDM', 'CDM (Civil Disobedience Movement)')
    title = title.replace('AICC', 'AICC (All India Congress Committee)')
    title = title.replace('Rin', 'RIN (Royal Indian Navy)')
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
        branches = MINDMAP_DATA.get("generic-topic", {}).get(lang, [])
        
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
