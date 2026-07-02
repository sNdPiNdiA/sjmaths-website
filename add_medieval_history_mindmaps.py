#!/usr/bin/env python3
import os
import re
import json

BASE = r"upsc/medieval_history"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'ii', 'iii', 'iv', 'v'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'between', 'or']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

def get_custom_branches(folder_name, category, is_hindi):
    fl = folder_name.lower()
    cat_lower = category.lower()
    
    # =========================================================================
    # ISLAMIC INVASIONS
    # =========================================================================
    if 'islamic-invasions' in cat_lower or 'qasim' in fl or 'ghazni' in fl or 'ghuri' in fl:
        
        # 1. Invasion of Muhammad Bin Qasim (712 AD)
        if 'qasim' in fl:
            if is_hindi:
                return [
                    {"label": "सैन्य अभियान और विजय", "type": "branch", "date": "712 ई.", "children": [
                        {"label": "मोहम्मद बिन कासिम ने 712 ई. में देबल, नेरून और सहवान पर अधिकार कर उमय्यद खिलाफत की सेना का नेतृत्व किया", "type": "leaf"},
                        {"label": "अरोर का युद्ध: राजा दाहिर को पराजित किया, जिससे सिंध पर अरबों का नियंत्रण स्थापित हुआ", "type": "leaf"},
                        {"label": "चचनामा: इस सैन्य विजय का विस्तृत इतिहास अरबी/फारसी ग्रंथ 'चचनामा' में सुरक्षित है", "type": "leaf"}
                    ]},
                    {"label": "कारण और सांस्कृतिक प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "तत्काल कारण: सिंध के समुद्री लुटेरों द्वारा खिलाफत के जहाजों की लूटपाट का प्रतिशोध लेना", "type": "leaf"},
                        {"label": "ज्ञान का आदान-प्रदान: संस्कृत वैज्ञानिक ग्रंथों (ब्रह्मगुप्त के ब्रह्म-sphuta-siddhanta) का अरबी में अनुवाद किया गया", "type": "leaf"},
                        {"label": "धार्मिक नीति: सिंध के हिंदुओं और बौद्धों को 'जिम्मी' (संरक्षित लोग) का दर्जा देकर जजिया कर लगाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Military Campaigns", "type": "branch", "date": "712 AD", "children": [
                        {"label": "Mohammad Bin Qasim led Umayyad forces, capturing strategic ports of Debal, Nerun, and Sehwan", "type": "leaf"},
                        {"label": "Battle of Aror: Defeated the Hindu ruler King Dahir, establishing Arab control over Sindh", "type": "leaf"},
                        {"label": "Chachnama: The primary historical chronicle detailing the social and military aspects of the Arab conquest", "type": "leaf"}
                    ]},
                    {"label": "Motives & Cultural Exchange", "type": "branch", "date": "Impact", "children": [
                        {"label": "Immediate cause: Retaliation against Sindh pirates looting Ceylon vessels bound for the Caliphate", "type": "leaf"},
                        {"label": "Sanskrit translations: Indian mathematics and astronomy works translated into Arabic (e.g. Brahmagupta's texts)", "type": "leaf"},
                        {"label": "Taxation policy: Declared local Hindus/Buddhists as 'Zimmis' (protected), introducing the Jizya tax", "type": "leaf"}
                    ]}
                ]

        # 2. Invasion of Mahmud of Ghazni
        elif 'ghazni' in fl:
            if is_hindi:
                return [
                    {"label": "सैन्य लूटपाट के अभियान", "type": "branch", "date": "1000-1027 ई.", "children": [
                        {"label": "उत्तर भारत में 17 बार विनाशकारी आक्रमण किए; पेशावर के युद्ध में हिंदूशाही राजा जयपाल को हराया", "type": "leaf"},
                        {"label": "सोमनाथ मंदिर लूट (1026 ई.): काठियावाड़ के प्रसिद्ध शिव मंदिर पर हमला कर भारी संपदा लूटी", "type": "leaf"},
                        {"label": "उद्देश्य: मध्य एशिया में एक शक्तिशाली साम्राज्य की स्थापना के लिए धन जुटाना; भारत में राज्य विस्तार नहीं", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक और ऐतिहासिक विरासत", "type": "branch", "date": "साहित्य", "children": [
                        {"label": "पंजाब का विलय: पंजाब और लाहौर का गजनी साम्राज्य में विलय कर उसे पूर्वी सूबा बनाया", "type": "leaf"},
                        {"label": "अल-बिरूनी: महमूद के साथ भारत आए प्रसिद्ध इतिहासकार जिन्होंने 'किताब-उल-हिंद' की रचना की", "type": "leaf"},
                        {"label": "फिरदौसी: महमूद के राजकवि जिन्होंने प्रसिद्ध महाकाव्य 'शाहनामा' लिखा", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Plunder Campaigns", "type": "branch", "date": "1000-1027 AD", "children": [
                        {"label": "Conducted 17 raids into Northern India; defeated Hindushahi rulers Jayapala and Anandapala", "type": "leaf"},
                        {"label": "Somnath Temple (1026 AD): Sacked the famous Shiva temple in Kathiwar, accumulating immense gold", "type": "leaf"},
                        {"label": "Primary motive: Fund wars in Central Asia and decorate Ghazni capital rather than permanent territorial empire", "type": "leaf"}
                    ]},
                    {"label": "Cultural & Historical Legacy", "type": "branch", "date": "Literature", "children": [
                        {"label": "Annexation of Punjab: Incorporated Punjab and Lahore into the Ghaznavid Empire as a buffer province", "type": "leaf"},
                        {"label": "Al-Biruni: Chronicler who accompanied Mahmud, writing the seminal Indological text 'Kitab-ul-Hind'", "type": "leaf"},
                        {"label": "Firdausi: Legendary court poet of Mahmud who compiled the epic Persian masterpiece 'Shahnameh'", "type": "leaf"}
                    ]}
                ]

        # 3. Invasion of Muhammad Ghuri
        elif 'ghuri' in fl:
            if is_hindi:
                return [
                    {"label": "तराइन के निर्णायक युद्ध", "type": "branch", "date": "1191-1192 ई.", "children": [
                        {"label": "तराइन का प्रथम युद्ध (1191): मुइज़ुद्दीन घोरी पृथ्वीराज चौहान के राजपूत संघ से बुरी तरह पराजित हुआ", "type": "leaf"},
                        {"label": "तराइन का द्वितीय युद्ध (1192): घोरी ने तुर्की घुड़सवार सेना के साथ पृथ्वीराज को पराजित कर दिल्ली जीता", "type": "leaf"}
                    ]},
                    {"label": "साम्राज्य विस्तार और विरासत", "type": "branch", "date": "राजनीतिक प्रभाव", "children": [
                        {"label": "चंदावर का युद्ध (1194): कन्नौज के गहड़वाल राजा जयचंद को हराकर गंगा-यमुना दोआब पर नियंत्रण किया", "type": "leaf"},
                        {"label": "कुतुबुद्दीन ऐबक: घोरी ने अपने गुलाम वायसराय ऐबक को भारत में शासन सौंपा, जिसने दिल्ली सल्तनत की नींव रखी", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Battles of Tarain", "type": "branch", "date": "1191-1192 AD", "children": [
                        {"label": "First Tarain (1191 AD): Ghuri was defeated and wounded by Prithviraj Chauhan's Rajput confederacy", "type": "leaf"},
                        {"label": "Second Tarain (1192 AD): Ghuri returned with advanced mobile horse archers, decisively defeating Chauhan", "type": "leaf"}
                    ]},
                    {"label": "Expansion & Political Legacy", "type": "branch", "date": "Establishment", "children": [
                        {"label": "Battle of Chandawar (1194 AD): Defeated King Jaichand of Kannauj, securing the rich Indo-Gangetic plains", "type": "leaf"},
                        {"label": "Aibak's Viceroyalty: Left his trusted slave general Qutb-ud-din Aibak, leading directly to Delhi Sultanate (1206)", "type": "leaf"}
                    ]}
                ]

    
    # =========================================================================
    # A. THE DELHI SULTANATE (24 UNIQUE TOPICS)
    # =========================================================================
    if 'delhi-sultanate' in cat_lower or 'sultanate' in fl or 'slave' in fl or 'khilji' in fl or 'tughlaq' in fl or 'lodhi' in fl or 'sayyid' in fl or 'sultan' in fl:
        
        # 1. Administration-under-Delhi-Sultanate
        if 'administration-under' in fl:
            if is_hindi:
                return [
                    {"label": "केंद्रीय शासन (सल्तनत मंत्रालय)", "type": "branch", "date": "मंत्रालय", "children": [
                        {"label": "दीवान-ए-विजारत: वजीर के नेतृत्व में; वित्त, कर संग्रह और लेखा परीक्षा का प्रबंधन", "type": "leaf"},
                        {"label": "दीवान-ए-अरीज़: अरीज़-ए-मुमालिक के नेतृत्व में; सैन्य भर्ती, निरीक्षण और वेतन प्रबंधन", "type": "leaf"},
                        {"label": "दीवान-ए-इंशा: शाही पत्राचार, फरमानों का प्रारूप तैयार करना और राज्य के रहस्यों का रख-रखाव", "type": "leaf"},
                        {"label": "दीवान-ए-रसालत: विदेश विभाग और धार्मिक बंदोबस्त का कार्य देखता था", "type": "leaf"}
                    ]},
                    {"label": "प्रांतीय और स्थानीय प्रशासन", "type": "branch", "date": "स्थानीय नियंत्रण", "children": [
                        {"label": "इक्ता प्रणाली: क्षेत्र को राजस्व आवंटन (इक्ता) में विभाजित किया गया, जिसे मुक्ता या वली संभालते थे", "type": "leaf"},
                        {"label": "शिक: प्रांतों को शिकदारों के नेतृत्व में शिक में विभाजित किया गया था (कानून और व्यवस्था)", "type": "leaf"},
                        {"label": "परगना: अमिल (संग्रहकर्ता) और मुशरिफ के अधीन; गाँव खूत, मुकद्दम और पटवारी के अधीन थे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Central Governance", "type": "branch", "date": "Ministries", "children": [
                        {"label": "Diwan-i-Wizarat: Led by Wazir; handled finance, revenue collection, and audit", "type": "leaf"},
                        {"label": "Diwan-i-Ariz: Led by Ariz-i-Mamalik; managed military recruitment, inspection, and salaries", "type": "leaf"},
                        {"label": "Diwan-i-Insha: Managed royal correspondence, drafting decrees, and state records", "type": "leaf"},
                        {"label": "Diwan-i-Rasalat: Managed foreign affairs, religious endowments, and humanitarian charity", "type": "leaf"}
                    ]},
                    {"label": "Provincial & Local", "type": "branch", "date": "Territorial Units", "children": [
                        {"label": "Iqta System: Revenue-assignment territories (Iqtas) administered by Muqtis/Valis", "type": "leaf"},
                        {"label": "Shiqs: Provinces split into Shiqs overseen by Shiqdar (military/police function)", "type": "leaf"},
                        {"label": "Local Units: Parganas overseen by Amils (revenue) and villages by Khuts/Muqaddams (chiefs)", "type": "leaf"}
                    ]}
                ]

        # 2. Decline-of-the-Sultanate
        elif 'decline-of' in fl:
            if is_hindi:
                return [
                    {"label": "आंतरिक कमजोरियां", "type": "branch", "date": "पतन के कारण", "children": [
                        {"label": "उत्तराधिकार के स्पष्ट नियम का अभाव: प्रत्येक सुल्तान की मृत्यु पर गृहयुद्ध छिड़ता था", "type": "leaf"},
                        {"label": "एमबीटी के सनकी प्रयोग और एफएसटी की वंशानुगत जागीर/सेना नीति से सैन्य कमजोरी आई", "type": "leaf"},
                        {"label": "अमीरों (नोबल्स) की गुटबाजी: विदेशी तुर्क बनाम भारतीय मुस्लिम सरदारों में सत्ता संघर्ष", "type": "leaf"}
                    ]},
                    {"label": "बाह्य आक्रमण और विघटन", "type": "branch", "date": "विदेशी हमले", "children": [
                        {"label": "तैमूर लंग का आक्रमण (1398 ईस्वी): दिल्ली को लूटा और सल्तनत के आर्थिक ढांचे को पूरी तरह तोड़ दिया", "type": "leaf"},
                        {"label": "प्रांतीय राज्यों का उदय: जौनपुर, मालवा, गुजरात और बंगाल सल्तनत से अलग स्वतंत्र हो गए", "type": "leaf"},
                        {"label": "पानीपत का प्रथम युद्ध (1526 ईस्वी): बाबर ने अंतिम शासक इब्राहिम लोदी को हराकर सल्तनत समाप्त की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Internal Factors", "type": "branch", "date": "Decay", "children": [
                        {"label": "Lack of definite law of succession, leading to civil wars and instability upon each ruler's death", "type": "leaf"},
                        {"label": "Muhammad bin Tughlaq's failed experiments and Firuz Tughlaq's hereditary army and Iqta policies", "type": "leaf"},
                        {"label": "Nobility conflicts: Factionalism between Turkish, Afghan, and indigenous Indian Muslim nobles", "type": "leaf"}
                    ]},
                    {"label": "External Attacks & Disintegration", "type": "branch", "date": "External Forces", "children": [
                        {"label": "Timur's Invasion (1398 AD): Devastated Delhi, depleted treasury, and destroyed central authority", "type": "leaf"},
                        {"label": "Rise of powerful regional states: Independence of Jaunpur, Bengal, Gujarat, and Malwa", "type": "leaf"},
                        {"label": "First Battle of Panipat (1526 AD): Babur defeated Ibrahim Lodi, ending Delhi Sultanate rule", "type": "leaf"}
                    ]}
                ]

        # 3. Economy-Various-Initiative-by-Different-Kings
        elif 'economy-various' in fl:
            if is_hindi:
                return [
                    {"label": "अलाउद्दीन खिलजी की पहल", "type": "branch", "date": "मूल्य नियंत्रण", "children": [
                        {"label": "दैनिक वस्तुओं (अनाज, कपड़ा, घोड़ा, दास) की कीमतें तय कीं; जमाखोरी पर पूर्ण प्रतिबंध लगाया", "type": "leaf"},
                        {"label": "शहना-ए-मंडी (बाजार अधीक्षक) की नियुक्ति की; गुप्तचरों (मुनहियान) द्वारा सूचना ली", "type": "leaf"}
                    ]},
                    {"label": "तुगलक सुल्तानों के प्रयास", "type": "branch", "date": "कृषि एवं कल्याण", "children": [
                        {"label": "गियासुद्दीन तुगलक: नहरों का निर्माण कराने वाला पहला सुल्तान; कर घटाकर 1/10 किया", "type": "leaf"},
                        {"label": "मोहम्मद बिन तुगलक: दीवान-ए-अमीर-ए-कोही (कृषि विभाग) बनाया; अकाल राहत हेतु सोंधर ऋण बांटे", "type": "leaf"},
                        {"label": "फिरोज शाह तुगलक: बड़े पैमाने पर सिंचाई नहरें बनवाईं; 24 कष्टदायक कर (अबवाब) समाप्त किए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Alauddin Khalji's Measures", "type": "branch", "date": "Price Regulation", "children": [
                        {"label": "Fixed prices of grain, cloth, horses, and slaves; banned hoarding and black marketing", "type": "leaf"},
                        {"label": "Appointed Shahna-i-Mandi (market superintendents) and used Munhiyans (secret spies) for compliance", "type": "leaf"}
                    ]},
                    {"label": "Tughlaq Reforms", "type": "branch", "date": "Agriculture & Taxation", "children": [
                        {"label": "Ghiyasuddin: Initiated state canal irrigation; reduced revenue demand to 1/10th or 1/11th", "type": "leaf"},
                        {"label": "Muhammad bin Tughlaq: Created Diwan-i-Amir-i-Kohi; distributed Sondhar/Taccavi loans to farmers", "type": "leaf"},
                        {"label": "Firuz Shah Tughlaq: Built major canals (Yamuna to Hissar); abolished 24 non-Sharia taxes (Abwabs)", "type": "leaf"}
                    ]}
                ]

        # 4. Khilji-Dynasty-Alauddin-Khilji
        elif 'khilji-dynasty-alauddin' in fl:
            if is_hindi:
                return [
                    {"label": "सैन्य सुधार", "type": "branch", "date": "सेना सुदृढ़ीकरण", "children": [
                        {"label": "सैनिकों को नकद वेतन देने की शुरुआत की; एक विशाल स्थायी सेना (खड़े बल) का गठन किया", "type": "leaf"},
                        {"label": "घोड़ों को दागने (दाग) और सैनिकों का हुलिया लिखने (चेहरा) की व्यवस्था लागू की", "type": "leaf"}
                    ]},
                    {"label": "राजस्व और कृषि नीतियां", "type": "branch", "date": "कर सुधार", "children": [
                        {"label": "कर का निर्धारण भूमि की माप (बिस्वा) के आधार पर किया; उपज का 50% हिस्सा कर तय किया", "type": "leaf"},
                        {"label": "मध्यस्थों (खूत, मुकद्दम, चौधरी) के विशेषाधिकार छीने; घराई (घर कर) और चराई (चारागाह कर) लगाए", "type": "leaf"},
                        {"label": "दीवान-ए-मुस्तखराज नामक विभाग बनाया जो बकाया राजस्व की वसूली करता था", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Military Reforms", "type": "branch", "date": "Standing Army", "children": [
                        {"label": "First sultan to pay soldiers in cash; maintained a large centralized standing army in Delhi", "type": "leaf"},
                        {"label": "Strictly enforced Dagh (branding of horses) and Chehra (descriptive rolls of soldiers)", "type": "leaf"}
                    ]},
                    {"label": "Revenue & Agrarian Policy", "type": "branch", "date": "Agrarian Control", "children": [
                        {"label": "Tax assessment based on land measurement (Biswa); fixed state demand at 50% of produce", "type": "leaf"},
                        {"label": "Abolished tax-free privileges of local headmen (Khuts/Muqaddams); levied Ghari (house) & Chari (pasture) taxes", "type": "leaf"},
                        {"label": "Established Diwan-i-Mustakhraj to collect revenue arrears and check corruption of officials", "type": "leaf"}
                    ]}
                ]

        # 5. Khilji-Dynasty-Jalaluddin-Khilji
        elif 'khilji-dynasty-jalaluddin' in fl:
            if is_hindi:
                return [
                    {"label": "खिलजी क्रांति", "type": "branch", "date": "1290 ईस्वी", "children": [
                        {"label": "गुलाम वंश के अंतिम शासक क्यूमर्स को गद्दी से हटाकर खिलजी राजवंश की नींव रखी", "type": "leaf"},
                        {"label": "तुर्की रईसों के नस्लीय एकाधिकार को समाप्त कर गैर-तुर्कों को ऊंचे पदों पर नियुक्त किया", "type": "leaf"}
                    ]},
                    {"label": "उदार नीतियां और घटनाएं", "type": "branch", "date": "उदार शासन", "children": [
                        {"label": "उदारवादी राजशाही: उपदेश दिया कि राज्य का आधार प्रजा की इच्छा और सहमति होना चाहिए", "type": "leaf"},
                        {"label": "मलिक छज्जू के विद्रोह को माफ कर दिया; षडयंत्र के संदेह में सूफी संत सीधी मौला को मृत्युदंड दिया", "type": "leaf"},
                        {"label": "1296 में अपने दामाद/भतीजे अलाउद्दीन खिलजी द्वारा कड़ा में विश्वासघात से मारे गए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Khalji Revolution", "type": "branch", "date": "1290 AD", "children": [
                        {"label": "Overthrew the Mamluk (Slave) dynasty successors, establishing the Khalji line", "type": "leaf"},
                        {"label": "Broke the racial monopoly of Turkish nobles by elevating non-Turks to high office", "type": "leaf"}
                    ]},
                    {"label": "Policies & Legacy", "type": "branch", "date": "Clemency", "children": [
                        {"label": "Benevolent Monarchy: Preached that state governance should be based on the consent of the governed", "type": "leaf"},
                        {"label": "Forgave rebels like Malik Chhajju; executed Sufi mystic Sidi Maula on conspiracy charges", "type": "leaf"},
                        {"label": "Assassinated in 1296 AD at Kara by his ambitious nephew/son-in-law, Alauddin Khalji", "type": "leaf"}
                    ]}
                ]

        # 6. Lodhi-Dynasty-Behlul-Lodhi
        elif 'lodhi-dynasty-behlul' in fl:
            if is_hindi:
                return [
                    {"label": "प्रथम अफगान राजवंश", "type": "branch", "date": "1451 ईस्वी", "children": [
                        {"label": "सैयद वंश के कमजोर शासक आलम शाह के शांतिपूर्ण आत्मसमर्पण के बाद सत्ता संभाली", "type": "leaf"},
                        {"label": "साम्राज्य का विस्तार किया और जौनपुर के शक्तिशाली शर्की साम्राज्य को जीतकर सल्तनत में मिलाया", "type": "leaf"}
                    ]},
                    {"label": "अफगान राजत्व का सिद्धांत", "type": "branch", "date": "समानता", "children": [
                        {"label": "राजशाही को 'समानों में प्रथम' (फर्स्ट अमंग इक्वल्स) माना; दरबार में सिंहासन पर बैठने के बजाय कालीन पर बैठते थे", "type": "leaf"},
                        {"label": "कबीलाई अफगान सरदारों के स्वाभिमान का सम्मान किया ताकि उनका सैन्य सहयोग बना रहे", "type": "leaf"},
                        {"label": "अपने नाम के तांबे के सिक्के 'बहलोली सिक्के' चलाए, जो काफी लोकप्रिय रहे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "First Afghan Dynasty", "type": "branch", "date": "1451 AD", "children": [
                        {"label": "Founded the Lodi dynasty after the peaceful abdication of the last Sayyid ruler, Alam Shah", "type": "leaf"},
                        {"label": "Successfully conquered and annexed the powerful Sharqi Kingdom of Jaunpur, expanding the realm", "type": "leaf"}
                    ]},
                    {"label": "Afghan Theory of Kingship", "type": "branch", "date": "Fraternity", "children": [
                        {"label": "Preached tribal equality: Considered himself 'first among equals' rather than an absolute autocrat", "type": "leaf"},
                        {"label": "Sat on carpets with his Afghan nobles instead of a high throne to respect their democratic tribal pride", "type": "leaf"},
                        {"label": "Issued 'Bahloli' copper coins, which remained the standard medium of exchange for decades", "type": "leaf"}
                    ]}
                ]

        # 7. Lodhi-Dynasty-Ibrahim-Lodhi
        elif 'lodhi-dynasty-ibrahim' in fl:
            if is_hindi:
                return [
                    {"label": "राजत्व का निरंकुश सिद्धांत", "type": "branch", "date": "कड़ा शासन", "children": [
                        {"label": "बहलोल के विपरीत, सुल्तान की पूर्ण सर्वोच्चता की मांग की; सरदारों को दरबार में खड़ा रहने का आदेश दिया", "type": "leaf"},
                        {"label": "इस नीति ने जलाल खान और दौलत खान लोदी जैसे पुराने अफगान अमीरों को नाराज कर दिया", "type": "leaf"}
                    ]},
                    {"label": "सल्तनत का अंत", "type": "branch", "date": "1526 ईस्वी", "children": [
                        {"label": "पंजाब के गवर्नर दौलत खान लोदी और मेवाड़ के राणा सांगा ने बाबर को भारत पर आक्रमण के लिए आमंत्रित किया", "type": "leaf"},
                        {"label": "पानीपत का प्रथम युद्ध (1526): बाबर की सेना से लड़ते हुए युद्ध के मैदान में मारे गए", "type": "leaf"},
                        {"label": "वह दिल्ली सल्तनत के एकमात्र ऐसे सुल्तान थे जो युद्ध के मैदान में वीरगति को प्राप्त हुए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Authoritarian Monarchy", "type": "branch", "date": "Absolute Power", "children": [
                        {"label": "Demanded absolute royal authority, forcing old Afghan nobles to stand in court as servants", "type": "leaf"},
                        {"label": "This policy alienated powerful nobles, leading to plots by governors like Daulat Khan Lodi of Punjab", "type": "leaf"}
                    ]},
                    {"label": "Fall of the Sultanate", "type": "branch", "date": "Panipat", "children": [
                        {"label": "Dissidents invited Babur of Kabul to invade India; Rana Sanga also formed alliances", "type": "leaf"},
                        {"label": "First Battle of Panipat (1526): Defeated and killed on the battlefield by Babur's forces", "type": "leaf"},
                        {"label": "Remains the only Sultan of Delhi to die directly fighting on the field of battle", "type": "leaf"}
                    ]}
                ]

        # 8. Lodhi-Dynasty-Sikander-Lodhi
        elif 'lodhi-dynasty-sikander' in fl:
            if is_hindi:
                return [
                    {"label": "प्रशासनिक कार्य", "type": "branch", "date": "सुधार", "children": [
                        {"label": "1504 में आगरा शहर की स्थापना की और इसे अपनी द्वितीय राजधानी बनाया", "type": "leaf"},
                        {"label": "भूमि मापन के लिए 'गज-ए-सिकंदरी' (32 अंगुल का पैमाना) लागू किया, जो मुगलों तक चला", "type": "leaf"},
                        {"label": "जागीरदारों के खातों की जांच के लिए एक सख्त लेखा परीक्षा प्रणाली (ऑडिट) शुरू की", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक एवं धार्मिक नीतियां", "type": "branch", "date": "धार्मिक कट्टरता", "children": [
                        {"label": "अनाजों से कर (जकात) हटाकर व्यापार को गति दी; फारसी कविताएं 'गुलरुखी' उपनाम से लिखते थे", "type": "leaf"},
                        {"label": "कंटर नीति: नागरकोट के ज्वालामुखी मंदिर की मूर्ति तोड़ी; मुस्लिम महिलाओं के मजारों पर जाने पर रोक लगाई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Administrative Milestones", "type": "branch", "date": "1489-1517 AD", "children": [
                        {"label": "Founded the city of Agra in 1504 AD and established it as his political headquarters", "type": "leaf"},
                        {"label": "Introduced 'Gaz-i-Sikandari' (32-digit unit) for standardized agrarian land measurement", "type": "leaf"},
                        {"label": "Enforced a strict system of auditing financial accounts of governors and jagirdars", "type": "leaf"}
                    ]},
                    {"label": "Culture & Religion", "type": "branch", "date": "Policies", "children": [
                        {"label": "Abolished octroi tax on grain; wrote Persian poems under the pen-name 'Gulrukhi'", "type": "leaf"},
                        {"label": "Orthodox policy: Destroyed the Jvalamukhi temple in Nagarkot; banned women from visiting Sufi graves", "type": "leaf"}
                    ]}
                ]

        # 9. Military-and-Attacks-by-Mongols-and-other-Turks
        elif 'military-and-attacks' in fl:
            if is_hindi:
                return [
                    {"label": "मंगोल आक्रमणों का खतरा", "type": "branch", "date": "मंगोल हमले", "children": [
                        {"label": "इल्तुतमिश के समय शुरू हुआ (चंगेज खान जलालुद्दीन मांगबरनी का पीछा करते हुए सिंधु तक आया)", "type": "leaf"},
                        {"label": "अलाउद्दीन खिलजी के समय हमले चरम पर थे (कादर, कुतलुग ख्वाजा, तरगी के नेतृत्व में हमले)", "type": "leaf"}
                    ]},
                    {"label": "प्रतिरक्षा रणनीतियां और तैमूर", "type": "branch", "date": "सैन्य सुरक्षा", "children": [
                        {"label": "बलबन ने सीमांत क्षेत्रों में किलों का निर्माण किया; दीवान-ए-अरीज़ के तहत विशेष सैन्य विभाग स्थापित किया", "type": "leaf"},
                        {"label": "अलाउद्दीन ने सीरी शहर की किलेबंदी की; सैनिकों की स्थायी तैनाती और रसद गोदाम बनाए", "type": "leaf"},
                        {"label": "तैमूर का आक्रमण (1398 ई.): नसीरुद्दीन महमूद तुगलक के काल में हुआ; दिल्ली को तबाह कर दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Mongol Threats", "type": "branch", "date": "Invasions", "children": [
                        {"label": "Began under Iltutmish (Genghis Khan pursued Khwarizm prince Mangabarni up to the Indus)", "type": "leaf"},
                        {"label": "Reached zenith under Alauddin Khalji (massive raids by Qutlugh Khwaja, Targhi, and Kadar)", "type": "leaf"}
                    ]},
                    {"label": "Defense Strategy & Timur", "type": "branch", "date": "Military Action", "children": [
                        {"label": "Balban built frontier fortresses and reorganized army recruitment under Ariz-i-Mamalik", "type": "leaf"},
                        {"label": "Alauddin built the fort-city of Siri, maintained a standing army, and stockpiled grain", "type": "leaf"},
                        {"label": "Timur's Sack (1398 AD): Invaded during reign of Mahmud Shah Tughlaq, dealing a fatal blow to Delhi", "type": "leaf"}
                    ]}
                ]

        # 10. Provincial-Kingdoms-and-Resistance-by-Indian-Chiefs
        elif 'provincial-kingdoms' in fl:
            if is_hindi:
                return [
                    {"label": "राजपूत प्रतिरोध", "type": "branch", "date": "मेवाड़", "children": [
                        {"label": "राणा हम्मीर ने अलाउद्दीन के बाद मेवाड़ को पुनः स्वतंत्र कराया; चित्तौड़ को केंद्र बनाया", "type": "leaf"},
                        {"label": "राणा कुम्भा: मालवा और गुजरात के खिलाफ विजय की स्मृति में चित्तौड़ में विजय स्तम्भ बनवाया", "type": "leaf"},
                        {"label": "राणा सांगा: राजपूतों को संगठित किया; खतौली के युद्ध में इब्राहिम लोदी को हराया", "type": "leaf"}
                    ]},
                    {"label": "क्षेत्रीय सल्तनतें", "type": "branch", "date": "स्वतंत्र राज्य", "children": [
                        {"label": "जौनपुर: शर्की राजवंश के तहत वास्तुकला (अटाला मस्जिद) और कला का बड़ा केंद्र बना", "type": "leaf"},
                        {"label": "गुजरात: मुजफ्फर शाह द्वारा स्वतंत्र घोषित; महमूद बेगड़ा सबसे प्रसिद्ध शासक रहा", "type": "leaf"},
                        {"label": "बंगाल: इलियास शाही वंश द्वारा दिल्ली से स्वतंत्र घोषित; अपनी अनूठी बंगाली वास्तुकला शैली विकसित की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Rajput Resistance", "type": "branch", "date": "Mewar", "children": [
                        {"label": "Rana Hamir liberated Mewar post-Alauddin's death, establishing the Sisodia dynasty", "type": "leaf"},
                        {"label": "Rana Kumbha: Built the Vijaya Stambha (Victory Tower) at Chittor after defeating Malwa/Gujarat", "type": "leaf"},
                        {"label": "Rana Sanga: Unified Rajput clans and defeated Ibrahim Lodi in the Battle of Khatoli", "type": "leaf"}
                    ]},
                    {"label": "Breakaway Sultanates", "type": "branch", "date": "Provinces", "children": [
                        {"label": "Jaunpur: Sharqi dynasty rule; famous for unique architecture like Atala Mosque", "type": "leaf"},
                        {"label": "Gujarat: Established independence under Muzaffarids; Mahmud Begarha was the most powerful ruler", "type": "leaf"},
                        {"label": "Bengal: Governed independently under Ilyas Shahi dynasty; patronized Bengali literature", "type": "leaf"}
                    ]}
                ]

        # 11. Sayyid-Dynasty
        elif fl == 'sayyid-dynasty':
            if is_hindi:
                return [
                    {"label": "सैयद वंश की उत्पत्ति", "type": "branch", "date": "1414 ईस्वी", "children": [
                        {"label": "संस्थापक खिज्र खान थे; तैमूर लंग के आक्रमण के बाद अराजकता का लाभ उठाकर गद्दी हासिल की", "type": "leaf"},
                        {"label": "खिज्र खान ने कभी सुल्तान की उपाधि नहीं ली; स्वयं को तैमूर के पुत्र शाहरुख का राज्यपाल (रैयत-ए-आला) कहा", "type": "leaf"}
                    ]},
                    {"label": "कमजोर नियंत्रण और अंत", "type": "branch", "date": "1451 ईस्वी", "children": [
                        {"label": "चार शासक: खिज्र खान, मुबारक शाह, मोहम्मद शाह, अलाउद्दीन आलम शाह", "type": "leaf"},
                        {"label": "साम्राज्य का आकार केवल दिल्ली के आसपास के कुछ जिलों तक सिमट गया था", "type": "leaf"},
                        {"label": "अंतिम शासक आलम शाह ने स्वेच्छा से बहलोल लोदी के पक्ष में सिंहासन छोड़ दिया और बदायूं चले गए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Origins & Founder", "type": "branch", "date": "1414 AD", "children": [
                        {"label": "Founded by Khizr Khan who took advantage of the chaos following Timur's invasion", "type": "leaf"},
                        {"label": "Khizr Khan ruled as Timur's deputy (Rayat-i-Ala) and did not coin money in his own name", "type": "leaf"}
                    ]},
                    {"label": "Weak Control & Fall", "type": "branch", "date": "1451 AD", "children": [
                        {"label": "Four rulers: Khizr Khan, Mubarak Shah, Muhammad Shah, and Alauddin Alam Shah", "type": "leaf"},
                        {"label": "Territory shrank drastically, jokingly called 'from Delhi to Palam'", "type": "leaf"},
                        {"label": "Last ruler Alam Shah peacefully abdicated in favor of Behlul Lodi and retired to Badaun", "type": "leaf"}
                    ]}
                ]

        # 12. Sayyid-Dynasty-1414-1451-AD
        elif 'sayyid-dynasty-1414' in fl:
            if is_hindi:
                return [
                    {"label": "मुबारक शाह और स्थिरता के प्रयास", "type": "branch", "date": "शासन", "children": [
                        {"label": "पिता खिज्र खान की मृत्यु के बाद सुल्तान घोषित; अपने नाम के सिक्के जारी किए", "type": "leaf"},
                        {"label": "जसोस खोखर के विद्रोह को दबाने के लिए पंजाब में सैन्य अभियान चलाया", "type": "leaf"},
                        {"label": "यमुना किनारे मुबारकबाद शहर बसाया; 'तारीख-ए-मुबारकशाही' के लेखक सरहिंदी को संरक्षण दिया", "type": "leaf"}
                    ]},
                    {"label": "पतन का दौर", "type": "branch", "date": "कमजोरी", "children": [
                        {"label": "मुबारक शाह की हत्या दरबारी वजीर सरवर-उल-मुल्क के षडयंत्र द्वारा की गई", "type": "leaf"},
                        {"label": "कमजोर उत्तराधिकारियों (मोहम्मद शाह और आलम शाह) के कारण जौनपुर और मालवा के हमले बढ़े", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Mubarak Shah's Reign", "type": "branch", "date": "1421-1434 AD", "children": [
                        {"label": "Succeeded his father Khizr Khan; assumed the title of Sultan and struck coins in his name", "type": "leaf"},
                        {"label": "Fought against Jasrath Khokhar of Punjab to maintain control over northern frontiers", "type": "leaf"},
                        {"label": "Founded Mubarakabad city; patronized Yahya bin Ahmad Sirhindi (Tarikh-i-Mubarak Shahi)", "type": "leaf"}
                    ]},
                    {"label": "Decline Phase", "type": "branch", "date": "Conspiracies", "children": [
                        {"label": "Mubarak Shah assassinated in a conspiracy led by his own wazir Sarwar-ul-Mulk", "type": "leaf"},
                        {"label": "Successors Muhammad Shah & Alam Shah were weak, leading to Lodi usurpation", "type": "leaf"}
                    ]}
                ]

        # 13. Slave-Dynasty-Ghiyasuddin-Balban
        elif 'slave-dynasty-ghiyasuddin-balban' in fl:
            if is_hindi:
                return [
                    {"label": "राजत्व का सिद्धांत", "type": "branch", "date": "सिद्धांत", "children": [
                        {"label": "सुल्तान को पृथ्वी पर ईश्वर की छाया (जिल-ए-इलाही) और ईश्वर का प्रतिनिधि (नियाबत-ए-खुदाई) माना", "type": "leaf"},
                        {"label": "दरबार में सिजदा (दंडवत) और पैबोस (कदम चूमना) की फारसी रस्में अनिवार्य कीं", "type": "leaf"},
                        {"label": "फारसी नववर्ष त्योहार 'नौरोज' मनाने की प्रथा शुरू की", "type": "leaf"}
                    ]},
                    {"label": "कड़े प्रशासनिक कदम", "type": "branch", "date": "लौह और रक्त", "children": [
                        {"label": "तुर्कान-ए-चिहलगानी (चालीसा दल) की शक्ति को पूरी तरह कुचलकर समाप्त कर दिया", "type": "leaf"},
                        {"label": "मेवात और अवध के विद्रोही डाकुओं के खिलाफ 'लौह और रक्त की नीति' अपनाई", "type": "leaf"},
                        {"label": "खुफिया नेटवर्क: हर इक्ता में बरीद (गुप्तचर) नियुक्त किए जो सीधे सुल्तान को रिपोर्ट देते थे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Theory of Kingship", "type": "branch", "date": "Autocracy", "children": [
                        {"label": "Advocated divine right: Zil-i-Ilahi (Shadow of God) and Niyabat-i-Khudai (Vicegerent of God)", "type": "leaf"},
                        {"label": "Introduced Persian court rituals: Sijda (prostration) and Paibos (kissing the Sultan's feet)", "type": "leaf"},
                        {"label": "Popularized the celebration of the Persian spring festival, Nauroz, to project majesty", "type": "leaf"}
                    ]},
                    {"label": "Destruction of Chahalgani & Spies", "type": "branch", "date": "Blood & Iron", "children": [
                        {"label": "Completely annihilated the Turkan-i-Chahalgani (the Forty) nobility club to secure the crown", "type": "leaf"},
                        {"label": "Adopted policy of Blood and Iron against Mewati robbers and Katehar rebels", "type": "leaf"},
                        {"label": "Established a direct intelligence network using Barids (spies) to report on all governors", "type": "leaf"}
                    ]}
                ]

        # 14. Slave-Dynasty-Iltutmish
        elif 'slave-dynasty-iltutmish' in fl:
            if is_hindi:
                return [
                    {"label": "साम्राज्य का सुदृढ़ीकरण", "type": "branch", "date": "1211-1236 ई.", "children": [
                        {"label": "मंगोलों से सुरक्षा: जलालुद्दीन मांगबरनी को शरण न देकर चंगेज खान के आक्रमण से बचाया", "type": "leaf"},
                        {"label": "1229 में बगदाद के खलीफा से अधिकारिक मान्यता (खिलअत) प्राप्त कर स्वतंत्र सुल्तान बने", "type": "leaf"},
                        {"label": "लाहौर के स्थान पर दिल्ली को सल्तनत की अधिकारिक राजधानी बनाया", "type": "leaf"}
                    ]},
                    {"label": "प्रशासनिक संस्थाएं", "type": "branch", "date": "सुधार", "children": [
                        {"label": "चांदी का 'टंका' और तांबे का 'जीतल' सिक्के जारी किए; शुद्ध अरबी सिक्के चलाने वाले पहले तुर्क बने", "type": "leaf"},
                        {"label": "इक्ता प्रणाली: अधिकारियों को वेतन के स्थान पर राजस्व भूमि (इक्ता) वितरित की", "type": "leaf"},
                        {"label": "तुर्कान-ए-चिहलगानी: अपने वफादार 40 तुर्की दासों का एक शक्तिशाली प्रशासनिक समूह बनाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Consolidation of the Realm", "type": "branch", "date": "1211-1236 AD", "children": [
                        {"label": "Mongol diplomacy: Refused asylum to Khwarizm prince Mangabarni, avoiding Genghis Khan's invasion", "type": "leaf"},
                        {"label": "Obtained formal investiture (Manshur) from Caliph of Baghdad in 1229 AD, legitimizing his rule", "type": "leaf"},
                        {"label": "Shifted the imperial capital from Lahore to Delhi, making it the true political center", "type": "leaf"}
                    ]},
                    {"label": "Administrative Foundations", "type": "branch", "date": "Institutions", "children": [
                        {"label": "Issued Tanka (silver) and Jital (copper) coins; standardized the currency weights", "type": "leaf"},
                        {"label": "Organized the Iqta system, distributing land revenue assignments in lieu of cash salaries", "type": "leaf"},
                        {"label": "Formed the Turkan-i-Chahalgani (corps of 40 Turkish slaves) to serve as a loyal advisory guard", "type": "leaf"}
                    ]}
                ]

        # 15. Slave-Dynasty-Qutubuddin-Aibak
        elif 'slave-dynasty-qutubuddin' in fl:
            if is_hindi:
                return [
                    {"label": "गुलाम वंश की स्थापना", "type": "branch", "date": "1206 ई.", "children": [
                        {"label": "मोहम्मद गोरी की मृत्यु के बाद भारतीय प्रांतों का कार्यभार संभाल स्वतंत्र सल्तनत बनाई", "type": "leaf"},
                        {"label": "उदार स्वभाव के कारण 'लाख बख्श' (लाखों का दान देने वाला) कहलाए", "type": "leaf"},
                        {"label": "कभी सुल्तान की पदवी धारण नहीं की, केवल 'मलिक' और 'सिपहसालार' के रूप में शासन किया", "type": "leaf"}
                    ]},
                    {"label": "स्थापत्य और मृत्यु", "type": "branch", "date": "कला", "children": [
                        {"label": "दिल्ली में कुवत-उल-इस्लाम और अजमेर में अढ़ाई दिन का झोपड़ा मस्जिद बनवाई", "type": "leaf"},
                        {"label": "सूफी संत कुतुबुद्दीन बख्तियार काकी के सम्मान में कुतुब मीनार की आधारशिला रखी", "type": "leaf"},
                        {"label": "1210 ई. में लाहौर में चौगान (पोलो) खेलते समय घोड़े से गिरकर मृत्यु हुई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Founding of Mamluk Rule", "type": "branch", "date": "1206 AD", "children": [
                        {"label": "Assumed control of Indian territories after Muhammad Ghori's death, ruling from Lahore", "type": "leaf"},
                        {"label": "Preached tolerance; earned the title 'Lakh Baksh' (giver of lakhs) for his generosity", "type": "leaf"},
                        {"label": "Did not strike coins or read Khutbah in his own name; ruled as Malik or Sipahsalar", "type": "leaf"}
                    ]},
                    {"label": "Architecture & Death", "type": "branch", "date": "Heritage", "children": [
                        {"label": "Built Quwwat-ul-Islam mosque in Delhi and Adhai Din Ka Jhopra mosque in Ajmer", "type": "leaf"},
                        {"label": "Laid the foundation of Qutb Minar in honor of Sufi saint Qutbuddin Bakhtiyar Kaki", "type": "leaf"},
                        {"label": "Died in 1210 AD in Lahore from injuries sustained during a fall from his horse while playing Chaugan", "type": "leaf"}
                    ]}
                ]

        # 16. Slave-Dynasty-Rajia-Sultan
        elif 'slave-dynasty-rajia' in fl:
            if is_hindi:
                return [
                    {"label": "महिला शासक", "type": "branch", "date": "1236-1240 ई.", "children": [
                        {"label": "इल्तुतमिश ने अपने बेटों को अयोग्य मानकर रजिया को अपना उत्तराधिकारी मनोनीत किया था", "type": "leaf"},
                        {"label": "पर्दा प्रथा का त्याग कर कुबा (चोगा) और कुलाह (टोपी) पहनकर पुरुषों की भांति खुले दरबार में बैठती थीं", "type": "leaf"}
                    ]},
                    {"label": "विरोध और अंत", "type": "branch", "date": "विद्रोह", "children": [
                        {"label": "अफ़्रीकी हब्शी दास जलालुद्दीन याकूत को अमीर-ए-अखूर (अश्वशाला प्रमुख) बनाकर विशेषाधिकार दिया, जिससे तुर्क रईस नाराज हो गए", "type": "leaf"},
                        {"label": "भटिंडा के सूबेदार अल्तूनिया ने विद्रोह किया; रजिया ने उससे शादी की पर 1240 में कैथल के पास मारी गईं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "First Female Monarch", "type": "branch", "date": "1236-1240 AD", "children": [
                        {"label": "Nominated directly by her father Iltutmish, who considered his sons incompetent", "type": "leaf"},
                        {"label": "Discarded the purdah (veil); wore male royal clothing (Quba and Kulah) and ruled openly", "type": "leaf"}
                    ]},
                    {"label": "Nobility Backlash & Fall", "type": "branch", "date": "Conspiracies", "children": [
                        {"label": "Elevated Abyssinian slave Yaqut to Amir-i-Akhur (Master of Stables), angering Chahalgani nobles", "type": "leaf"},
                        {"label": "Imprisoned by Altunia (Bhatinda governor); married him but both were killed near Kaithal in 1240 AD", "type": "leaf"}
                    ]}
                ]

        # 17. Society-and-Culture
        elif fl == 'society-and-culture':
            if is_hindi:
                return [
                    {"label": "मध्यकालीन समाज", "type": "branch", "date": "सामाजिक पदानुक्रम", "children": [
                        {"label": "रईस वर्ग (अमीर) सबसे ऊपर था, जिनमें तुर्क, फारसी और बाद में अफगान शामिल थे", "type": "leaf"},
                        {"label": "हिंदू समाज में जाति व्यवस्था मजबूत रही; दक्षिण में भक्ति संतों ने समानता का उपदेश दिया", "type": "leaf"},
                        {"label": "शहरों में दस्तकार (कारीगर), जुलाहे और व्यापारियों का एक नया वर्ग तेजी से उभरा", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक विकास", "type": "branch", "date": "संस्कृति", "children": [
                        {"label": "अमीर खुसरो: खड़ी बोली के विकास में योगदान; सितार और तबला का आविष्कार किया; कव्वाली के जनक", "type": "leaf"},
                        {"label": "फारसी साहित्य राजभाषा बना; संस्कृत ग्रंथों का फारसी में अनुवाद होना शुरू हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Social Hierarchy", "type": "branch", "date": "Society", "children": [
                        {"label": "Ruling class composed of foreign Turkish, Persian, and Afghan nobles at the apex", "type": "leaf"},
                        {"label": "Hindus formed the agrarian base; caste system persisted but was questioned by Bhakti reformers", "type": "leaf"},
                        {"label": "Emergence of a strong artisan, weaver, and merchant class in rapidly growing urban centers", "type": "leaf"}
                    ]},
                    {"label": "Cultural Integration", "type": "branch", "date": "Art & Lit", "children": [
                        {"label": "Amir Khusrau: Synthesized Indo-Persian culture; introduced Sitar/Tabla and popularized Qawwali", "type": "leaf"},
                        {"label": "Persian remained the court language; significant translation of Sanskrit epics into Persian", "type": "leaf"}
                    ]}
                ]

        # 18. Society-and-Culture-Delhi-Sultanate
        elif 'society-and-culture-delhi' in fl:
            if is_hindi:
                return [
                    {"label": "सल्तनत कालीन वास्तुकला", "type": "branch", "date": "इंडो-इस्लामिक स्थापत्य", "children": [
                        {"label": "वैज्ञानिक सिद्धांतों (सच्चा मेहराब, गुंबद और वाल्ट) का भारत में पहली बार बड़े पैमाने पर प्रयोग", "type": "leaf"},
                        {"label": "चूना-गारा (कंक्रीट मसाला) का उपयोग किया; अरबेस्क पद्धति (फूल-पत्ती और ज्यामितीय नक्काशी) अपनाई", "type": "leaf"},
                        {"label": "मानव आकृतियों के स्थान पर दीवारों पर कुरान की आयतें उकेरने (कैटिग्राफ़ी) की कला चली", "type": "leaf"}
                    ]},
                    {"label": "इतिहासकार और संगीत", "type": "branch", "date": "साहित्यिक स्रोत", "children": [
                        {"label": "जियाउद्दीन बरनी (तारीख-ए-फिरोजशाही) और मिन्हाज-उस-सिराज (तबाकात-ए-नासिरी) प्रमुख इतिहासकार थे", "type": "leaf"},
                        {"label": "इब्न बतूता (मोरक्को का यात्री) ने अपनी पुस्तक 'रिहला' में मोहम्मद बिन तुगलक के काल का वर्णन किया", "type": "leaf"},
                        {"label": "संगीत: रबाब और सारंगी जैसे वाद्य यंत्रों का विकास हुआ; भारतीय रागों में फारसी धुनों का मेल हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sultanate Architecture", "type": "branch", "date": "Indo-Islamic Style", "children": [
                        {"label": "First large-scale use of arcuate style (true arch, dome, and vaults) in Indian construction", "type": "leaf"},
                        {"label": "Used lime mortar as cement; decorated walls with Arabesque (geometric/floral patterns)", "type": "leaf"},
                        {"label": "Calligraphy: Avoided animal/human figures; carved Quranic verses on stone walls", "type": "leaf"}
                    ]},
                    {"label": "Historical Accounts & Music", "type": "branch", "date": "Literature", "children": [
                        {"label": "Barani's Tarikh-i-Firoz Shahi and Minhaj-us-Siraj's Tabaqat-i-Nasiri were key records", "type": "leaf"},
                        {"label": "Ibn Battuta (Moroccan traveler) documented Muhammad bin Tughlaq's court in his travelogue 'Rihla'", "type": "leaf"},
                        {"label": "Music: Fusion of Persian styles (Ghazal) with classical Indian ragas; Rabab and Sarangi introduced", "type": "leaf"}
                    ]}
                ]

        # 19. Tughlaq-Dynasty-Firuz-Shah-Tughlaq
        elif 'tughlaq-dynasty-firuz' in fl:
            if is_hindi:
                return [
                    {"label": "कल्याणकारी सुधार और शहर", "type": "branch", "date": "सुधार", "children": [
                        {"label": "दीवान-ए-खैरात (अनाथों, विधवाओं की सहायता के लिए दान विभाग) की स्थापना की", "type": "leaf"},
                        {"label": "दीवान-ए-बंदगान (दासों के लिए समर्पित विभाग) बनाया; दरबार में 1.8 लाख दास थे", "type": "leaf"},
                        {"label": "फिरोजाबाद, जौनपुर, फतेहाबाद, हिसार जैसे नए शहरों का निर्माण कराया", "type": "leaf"}
                    ]},
                    {"label": "राजस्व और सिंचाई नीतियां", "type": "branch", "date": "आर्थिक कार्य", "children": [
                        {"label": "सतलुज और यमुना से व्यापक सिंचाई नहरें निकलवाईं; राजकीय बाग-बगीचे लगवाए", "type": "leaf"},
                        {"label": "शरिया के अनुसार केवल 4 कर (खराज, खुम्स, जजिया, जकात) वसूले; शेष कर समाप्त किए", "type": "leaf"},
                        {"label": "ब्राह्मणों पर जजिया कर लगाने वाला पहला मुस्लिम शासक बना", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Welfare State & Cities", "type": "branch", "date": "1351-1388 AD", "children": [
                        {"label": "Created Diwan-i-Khairat to give financial aid to poor Muslims, widows, and orphans", "type": "leaf"},
                        {"label": "Established Diwan-i-Bandagan to manage over 1,80,000 royal slaves", "type": "leaf"},
                        {"label": "Founded cities like Jaunpur (named after cousin Jauna), Firozabad, Fatehabad, and Hissar", "type": "leaf"}
                    ]},
                    {"label": "Irrigation & Taxation", "type": "branch", "date": "Economic Policy", "children": [
                        {"label": "Constructed major irrigation canals (Yamuna to Hissar); planted 1200 state-owned orchards", "type": "leaf"},
                        {"label": "Abolished non-Sharia taxes; collected only Kharaj (land), Khums (booty), Jizya, and Zakat", "type": "leaf"},
                        {"label": "First sultan to impose Jizya on Brahmins, separating it from land revenue", "type": "leaf"}
                    ]}
                ]

        # 20. Tughlaq-Dynasty-Ghiyasuddin-Tughlaq
        elif 'tughlaq-dynasty-ghiyasuddin' in fl:
            if is_hindi:
                return [
                    {"label": "तुगलक वंश की स्थापना", "type": "branch", "date": "1320 ई.", "children": [
                        {"label": "खिलजी वंश के अंतिम शासक खुसरो खान को हराकर दिल्ली में सत्ता संभाली", "type": "leaf"},
                        {"label": "दिल्ली के पास पहाड़ी पर एक मजबूत किलेबंदी वाले शहर 'तुगलकाबाद' का निर्माण कराया", "type": "leaf"}
                    ]},
                    {"label": "कृषि सुधार और मृत्यु", "type": "branch", "date": "कृषि नीतियां", "children": [
                        {"label": "नहरों का निर्माण शुरू कराने वाला सल्तनत का प्रथम सुल्तान; भू-राजस्व घटाकर 1/10 या 1/11 किया", "type": "leaf"},
                        {"label": "अलाउद्दीन की कठोर कर नीतियों को वापस लिया और किसानों को राहत दी", "type": "leaf"},
                        {"label": "1325 ई. में अफगानपुर में लकड़ी के स्वागत मंडप के गिरने से दबकर रहस्यमयी मृत्यु हुई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Founder of Dynasty", "type": "branch", "date": "1320 AD", "children": [
                        {"label": "Defeated the usurper Khusrau Khan (last Khalji associate) to take the throne", "type": "leaf"},
                        {"label": "Built the massive fort-city of Tughlaqabad with heavy stone ramparts", "type": "leaf"}
                    ]},
                    {"label": "Agrarian Policy & Death", "type": "branch", "date": "Irregularities", "children": [
                        {"label": "First sultan to dig state canals for agriculture; limited land revenue to 1/10th or 1/11th", "type": "leaf"},
                        {"label": "Replaced Alauddin's measurement system with older crop-sharing methods", "type": "leaf"},
                        {"label": "Died in 1325 AD from the collapse of a wooden pavilion at Afghanpur (planned by son Jauna Khan)", "type": "leaf"}
                    ]}
                ]

        # 21. Tughlaq-Dynasty-Mohd-Bin-Tughlaq
        elif 'tughlaq-dynasty-mohd' in fl or 'mohd-bin-tughlaq' in fl:
            if is_hindi:
                return [
                    {"label": "महत्वपूर्ण प्रशासनिक योजनाएं", "type": "branch", "date": "1325-1351 ई.", "children": [
                        {"label": "राजधानी स्थानांतरण: मंगोलों से दूर दक्कन में नियंत्रण के लिए दिल्ली से दौलताबाद राजधानी बदली", "type": "leaf"},
                        {"label": "सांकेतिक मुद्रा (1329): तांबे और पीतल के सिक्के चलाए; घर-घर टक्साल बनने से योजना विफल रही", "type": "leaf"},
                        {"label": "दोआब कर वृद्धि: अकाल के दौरान कर बढ़ाया, जिससे किसानों ने खेती छोड़कर जंगलों की शरण ली", "type": "leaf"}
                    ]},
                    {"label": "कृषि सुधार और सैन्य योजनाएं", "type": "branch", "date": "दीवान-ए-कोही", "children": [
                        {"label": "दीवान-ए-कोही (कृषि विभाग) का गठन किया; किसानों को तकावी (कृषि ऋण) वितरित किए", "type": "leaf"},
                        {"label": "खुरासान और कराचिल (हिमालय) सैन्य अभियानों की योजना बनाई, जिससे शाही खजाना रिक्त हो गया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Radical Experiments", "type": "branch", "date": "1325-1351 AD", "children": [
                        {"label": "Capital Transfer: Relocated capital to Daulatabad (Deogiri) to rule South India; forced migration caused deaths", "type": "leaf"},
                        {"label": "Token Currency (1329): Issued copper/brass tokens equal to silver tankas; failed due to mass forging", "type": "leaf"},
                        {"label": "Doab Tax Hike: Increased land tax in fertile Doab during a severe famine, sparking agrarian rebellion", "type": "leaf"}
                    ]},
                    {"label": "Agrarian Reforms & Campaigns", "type": "branch", "date": "Reforms", "children": [
                        {"label": "Created Diwan-i-Amir-i-Kohi to bring barren land under state cultivation; gave Sondhar loans", "type": "leaf"},
                        {"label": "Envisaged massive campaigns to Khurasan and Qarachil (Himalayas) which depleted state resources", "type": "leaf"}
                    ]}
                ]

        # 22. Various-Aspects-of-Rule-under-Khiljis
        elif 'rule-under-khiljis' in fl:
            if is_hindi:
                return [
                    {"label": "केंद्रीयकरण और अमीरों पर नियंत्रण", "type": "branch", "date": "नियंत्रण", "children": [
                        {"label": "अमीरों के आपसी मेल-जोल, सामाजिक बैठकों और शादियों पर सुल्तान की पूर्व अनुमति अनिवार्य की", "type": "leaf"},
                        {"label": "मदिरापान और जुआ खेलने पर पूर्ण प्रतिबंध लगाया; रईसों की जागीरें जब्त कर लीं", "type": "leaf"},
                        {"label": "सैन्य शक्ति: एक विशाल केंद्रीयकृत सेना बनाई जो बाजार सुधारों पर आश्रित थी", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Centralization & Control of Nobles", "type": "branch", "date": "Tyranny", "children": [
                        {"label": "Banned social gatherings, marriage alliances, and drinking parties among nobles without prior permission", "type": "leaf"},
                        {"label": "Confiscated land grants (inams, waqfs) from nobles to bring them directly under Khalsa land", "type": "leaf"},
                        {"label": "Military Dominance: Maintained a massive standing army, strictly audit-controlled via market price caps", "type": "leaf"}
                    ]}
                ]

        # 23. Various-Aspects-of-Rule-under-Slaves
        elif 'rule-under-slaves' in fl:
            if is_hindi:
                return [
                    {"label": "प्रारंभिक सुदृढ़ीकरण", "type": "branch", "date": "1206-1290 ई.", "children": [
                        {"label": "विदेशी आक्रांताओं से हटकर भारत में एक स्वतंत्र सल्तनत साम्राज्य की स्थापना का संक्रमण काल", "type": "leaf"},
                        {"label": "यल्दौज और कुबाचा जैसे प्रतिद्वंद्वियों को हराकर भारतीय क्षेत्रों पर पूर्ण नियंत्रण किया", "type": "leaf"},
                        {"label": "ताज बनाम रईस: सुल्तान और तुर्क अमीरों (चालीसा) के बीच सत्ता का संघर्ष बलबन के आने तक चला", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Early Consolidation", "type": "branch", "date": "1206-1290 AD", "children": [
                        {"label": "Transition phase from transient military plunderers to permanent imperial settlers in Delhi", "type": "leaf"},
                        {"label": "Defeated competitors like Yalduz and Qubacha to protect sovereignty of Delhi Sultanate", "type": "leaf"},
                        {"label": "Crown vs Nobles: Ongoing friction between royal authority and the Turkan-i-Chahalgani clan", "type": "leaf"}
                    ]}
                ]

        # 24. Various-Aspects-of-Rule-under-Tughlaqs
        elif 'rule-under-tughlaqs' in fl:
            if is_hindi:
                return [
                    {"label": "नीतियों का विकास", "type": "branch", "date": "तुगलक नीतियां", "children": [
                        {"label": "मोहम्मद बिन तुगलक के काल में साम्राज्य अपनी अधिकतम भौगोलिक सीमा पर पहुंचा", "type": "leaf"},
                        {"label": "फिरोज तुगलक के काल में कल्याणकारी राज्य और धार्मिक कट्टरता का उदय हुआ", "type": "leaf"},
                        {"label": "इक्तादारों को रियायतें देने और जागीरों को वंशानुगत बनाने से केंद्रीय नियंत्रण कमजोर हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Agrarian Development & Decentered Rule", "type": "branch", "date": "Tughlaq Rule", "children": [
                        {"label": "Delhi Sultanate reached its maximum territorial size under Muhammad bin Tughlaq's reign", "type": "leaf"},
                        {"label": "Firuz Shah Tughlaq established a welfare state (free hospitals, charity) mixed with religious orthodoxy", "type": "leaf"},
                        {"label": "Weakened central power by making army ranks, offices, and Iqtas hereditary, leading to splits", "type": "leaf"}
                    ]}
                ]

        # Fallback for Delhi Sultanate
        else:
            if is_hindi:
                return [
                    {"label": "दिल्ली सल्तनत सामान्य", "type": "branch", "date": "सल्तनत", "children": [
                        {"label": "केंद्रीय शासन and सैन्य प्रणाली (दीवान-ए-विजारत, दीवान-ए-अरीज़)", "type": "leaf"},
                        {"label": "मंगोलों से सुरक्षा, इक्ता व्यवस्था और वास्तुकला में मेहराब/गुंबद की विशेषताएं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Delhi Sultanate Overview", "type": "branch", "date": "Overview", "children": [
                        {"label": "Five ruling dynasties: Slave, Khalji, Tughlaq, Sayyid, and Lodi kingdoms (1206-1526 AD)", "type": "leaf"},
                        {"label": "Indo-Islamic cultural synthesis, Urdu language origin, and arch/dome architecture", "type": "leaf"}
                    ]}
                ]

    # =========================================================================
    # B. MUGHAL RULE (22+ UNIQUE TOPICS)
    # =========================================================================
    elif 'mughal-rule' in cat_lower or 'mughal' in fl or 'akbar' in fl or 'aurangzeb' in fl or 'babur' in fl or 'humayun' in fl or 'jahangir' in fl or 'shah-jahan' in fl or 'later-mughals' in fl or 'sher-shah' in fl or 'sur-empire' in fl:
        
        # 1. Akbar Land Revenue & Dahsala System
        if 'akbar-administration-land-revenue' in fl or 'the-dahsala-system' in fl or 'land-revenue' in fl:
            if is_hindi:
                return [
                    {"label": "दहसाला या जब्ती प्रणाली", "type": "branch", "date": "1580 ई.", "children": [
                        {"label": "राजा टोडरमल (वित्त मंत्री) द्वारा पिछले 10 वर्षों (1570-1580) के औसत मूल्य और उपज पर तैयार", "type": "leaf"},
                        {"label": "कुल उपज का एक-तिहाई भाग कर के रूप में तय किया गया, जो आमतौर पर नकद में चुकाया जाता था", "type": "leaf"}
                    ]},
                    {"label": "भूमि वर्गीकरण और अधिकारी", "type": "branch", "date": "वर्गीकरण", "children": [
                        {"label": "पोलज: प्रतिवर्ष खेती; परौती: 1-2 वर्ष खाली; चाचर: 3-4 वर्ष खाली; बंजर: 5+ वर्ष बिना खेती", "type": "leaf"},
                        {"label": "करोड़ी (1 करोड़ दाम वसूलने वाले), आमिल (राजस्व निर्धारक), कानूनगो (भूमि रिकॉर्ड अधिकारी)", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Dahsala or Zabti System", "type": "branch", "date": "1580 AD", "children": [
                        {"label": "Designed by Finance Minister Raja Todar Mal based on 10-year yield and price averages (1570-1580)", "type": "leaf"},
                        {"label": "State share fixed at one-third of average produce, mostly collected in cash using local price schedules", "type": "leaf"}
                    ]},
                    {"label": "Land Classes & Officers", "type": "branch", "date": "Categories", "children": [
                        {"label": "Polaj: Annually cultivated; Parauti: Fallow for 1-2 years; Chachar: Fallow for 3-4 years; Banjar: Uncultivated for 5+ years", "type": "leaf"},
                        {"label": "Karoris (officers collecting 1 crore copper dams), Amils (assessors), Qanungos (record keepers)", "type": "leaf"}
                    ]}
                ]

        # 2. Akbar Mansabdari System
        elif 'the-mansabdari-system' in fl:
            if is_hindi:
                return [
                    {"label": "जात और सवार रैंक", "type": "branch", "date": "पद और पदानुक्रम", "children": [
                        {"label": "जात: व्यक्तिगत पद, प्रतिष्ठा और वेतन का निर्धारण करता था", "type": "leaf"},
                        {"label": "सवार: मनसबदार द्वारा रखे जाने वाले घुड़सवारों और घोड़ों की संख्या का निर्धारण करता था", "type": "leaf"},
                        {"label": "दह-बिस्ती नियम: प्रत्येक घुड़सवार के लिए 2 घोड़े रखना आवश्यक था (ताकि युद्ध में घोड़े बदले जा सकें)", "type": "leaf"}
                    ]},
                    {"label": "वेतन भुगतान और नियंत्रण", "type": "branch", "date": "जागीर एवं नकद", "children": [
                        {"label": "वेतन नकद (नक्दी) या भूमि राजस्व असाइनमेंट (जागीर) के माध्यम से दिया जाता था", "type": "leaf"},
                        {"label": "दाग (घोड़ों को दागना) और चेहरा (सैनिकों का हुलिया लिखना) प्रथाओं को कड़ाई से लागू किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Zat & Sawar Ranks", "type": "branch", "date": "Rank Structure", "children": [
                        {"label": "Zat: Indicated personal status, hierarchy, and salary of the Mansabdar", "type": "leaf"},
                        {"label": "Sawar: Specified the exact number of cavalrymen and horses the officer had to maintain", "type": "leaf"},
                        {"label": "Dah-Bisti rule: Mansabdars had to maintain 20 horses for every 10 cavalrymen (2:1 ratio)", "type": "leaf"}
                    ]},
                    {"label": "Payment & Accountability", "type": "branch", "date": "Jagir System", "children": [
                        {"label": "Paid either in cash (Naqdi) or through temporary land revenue assignments called Jagirs", "type": "leaf"},
                        {"label": "Strict military audits enforced via Dagh (horse branding) and Chehra (descriptive rolls)", "type": "leaf"}
                    ]}
                ]

        # 3. Akbar 2nd Battle of Panipat
        elif '2nd-battle-of-panipat' in fl or 'second-battle-of-panipat' in fl:
            if is_hindi:
                return [
                    {"label": "पानीपत का द्वितीय युद्ध", "type": "branch", "date": "1556 ई.", "children": [
                        {"label": "बैरम खान के नेतृत्व में मुगल सेना ने आदिल शाह सूर के सेनापति हेमू (विक्रमादित्य) को हराया", "type": "leaf"},
                        {"label": "एक यादृच्छिक तीर हेमू की आंख में लगा, जिससे वह बेहोश हो गया और युद्ध की दिशा बदल गई", "type": "leaf"}
                    ]},
                    {"label": "राजनीतिक प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "इस विजय से दिल्ली और आगरा पर मुगलों का नियंत्रण पुनः स्थापित हुआ और सूर वंश का खतरा समाप्त हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Battle & Strategy", "type": "branch", "date": "1556 AD", "children": [
                        {"label": "Mughal forces led by Bairam Khan defeated Hemu (Vikramaditya), the general of Adil Shah Sur", "type": "leaf"},
                        {"label": "A stray arrow hit Hemu in the eye, causing him to lose consciousness and routing his army", "type": "leaf"}
                    ]},
                    {"label": "Political Impact", "type": "branch", "date": "Impact", "children": [
                        {"label": "Restored Mughal power in Delhi and Agra, decisively ending the Afghan Sur dynasty's challenge", "type": "leaf"}
                    ]}
                ]

        # 4. Akbar Battle of Haldighati
        elif 'haldighati' in fl:
            if is_hindi:
                return [
                    {"label": "हल्दीघाटी का युद्ध", "type": "branch", "date": "1576 ई.", "children": [
                        {"label": "मान सिंह प्रथम के नेतृत्व में मुगल सेना बनाम मेवाड़ के महाराणा प्रताप के बीच भीषण संघर्ष", "type": "leaf"},
                        {"label": "राणा प्रताप के प्रसिद्ध घोड़े 'चेतक' ने घायल होने पर भी उनकी रक्षा की और उन्हें सुरक्षित निकाला", "type": "leaf"}
                    ]},
                    {"label": "सामरिक परिणाम", "type": "branch", "date": "परिणाम", "children": [
                        {"label": "मुगलों ने गोगुंदा और आसपास के क्षेत्रों पर नियंत्रण कर लिया, परंतु महाराणा प्रताप ने अधीनता स्वीकार नहीं की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Haldighati Confrontation", "type": "branch", "date": "1576 AD", "children": [
                        {"label": "Fierce battle between Mughal forces under Raja Man Singh I and Maharana Pratap of Mewar", "type": "leaf"},
                        {"label": "Rana Pratap's legendary horse Chetak carried him to safety despite being fatally injured", "type": "leaf"}
                    ]},
                    {"label": "Strategic Outcome", "type": "branch", "date": "Outcome", "children": [
                        {"label": "Mughals captured Gogunda, but Rana Pratap escaped and continued guerrilla warfare from the hills", "type": "leaf"}
                    ]}
                ]

        # 5. Akbar Concept of Navaratnas
        elif 'concept-of-navaratnas' in fl or 'navaratnas' in fl:
            if is_hindi:
                return [
                    {"label": "बौद्धिक एवं प्रशासनिक रत्न", "type": "branch", "date": "रत्न", "children": [
                        {"label": "अबुल फजल (इतिहासकार, अकबरनामा के लेखक), बीरबल (सलाहकार, हाजिरजवाब), राजा टोडरमल (राजस्व)", "type": "leaf"},
                        {"label": "तानसेन (महान संगीतकार, दरबारी गायक), मुल्ला दो-प्याजा (सलाहकार, बुद्धिमान दरबारी)", "type": "leaf"}
                    ]},
                    {"label": "सैन्य, साहित्यिक एवं चिकित्सा रत्न", "type": "branch", "date": "रत्न 2", "children": [
                        {"label": "राजा मान सिंह (कुशल सेनापति), अब्दुर्रहीम खान-ए-खाना (कवि, अनुवादक), फैजी (राजकवि, विद्वान)", "type": "leaf"},
                        {"label": "हकीम हुमाम (शाही चिकित्सक, सलाहकार)", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Intellectual & Administrative Gems", "type": "branch", "date": "Advisors", "children": [
                        {"label": "Abu'l Fazl (historian & Akbarnama author), Birbal (witty advisor), Raja Todar Mal (finance reformer)", "type": "leaf"},
                        {"label": "Tansen (virtuoso musician & singer), Mullah Do-Piyaza (witty court intellectual)", "type": "leaf"}
                    ]},
                    {"label": "Military & Literary Leaders", "type": "branch", "date": "Commanders", "children": [
                        {"label": "Raja Man Singh (trusted general), Abdul Rahim Khan-i-Khana (scholar & poet), Faizi (poet laureate)", "type": "leaf"},
                        {"label": "Hakim Humam (royal physician and advisor)", "type": "leaf"}
                    ]}
                ]

        # 6. Akbar Administration: Central, Provincial, and Other
        elif 'administration' in fl and ('akbar' in fl or 'provincial' in fl or 'central' in fl):
            if is_hindi:
                return [
                    {"label": "केंद्रीय प्रशासन", "type": "branch", "date": "केंद्र", "children": [
                        {"label": "वकील (प्रधानमंत्री), दीवान (राजस्व प्रमुख), मीर बख्शी (सैन्य प्रमुख और मनसब प्रदाता)", "type": "leaf"},
                        {"label": "सद्र-उस-सुदूर (धार्मिक एवं धर्मार्थ अनुदान प्रमुख), खान-ए-सामां (शाही घराने का प्रबंधक)", "type": "leaf"}
                    ]},
                    {"label": "प्रांतीय प्रशासन", "type": "branch", "date": "प्रांत", "children": [
                        {"label": "साम्राज्य को 12-15 सूबों (प्रांतों) में विभाजित किया गया था, जिनका शासन सूबेदार करता था", "type": "leaf"},
                        {"label": "प्रांतीय दीवान (राजस्व) और प्रांतीय बख्शी (सैन्य) स्वतंत्र रूप से रिपोर्ट करते थे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Central Administration", "type": "branch", "date": "Central", "children": [
                        {"label": "Vakil (prime minister), Diwan/Wazir (finance chief), Mir Bakshi (military head and mansab recorder)", "type": "leaf"},
                        {"label": "Sadr-us-Sudur (religious & charitable head), Khan-i-Saman (head of royal household)", "type": "leaf"}
                    ]},
                    {"label": "Provincial Structure", "type": "branch", "date": "Provincial", "children": [
                        {"label": "Empire divided into Subas (provinces) ruled by Subadars (governors) with executive power", "type": "leaf"},
                        {"label": "Provincial Diwan (finance) and Bakshi (military) reported directly to the central ministry", "type": "leaf"}
                    ]}
                ]

        # 7. Akbar Socio-Religious Initiatives (Din-i-Ilahi, Ibadat Khana, Ulama)
        elif 'socio-religious' in fl or 'din-i-ilahi' in fl or 'ibadat-khana' in fl or 'ulama' in fl:
            if is_hindi:
                return [
                    {"label": "इबादत खाना और सुलह-ए-कुल", "type": "branch", "date": "धार्मिक विमर्श", "children": [
                        {"label": "1575 ई. में फतेहपुर सीकरी में इबादत खाना बनाया; 1578 में सभी धर्मों के विद्वानों के लिए खोला", "type": "leaf"},
                        {"label": "सुलह-ए-कुल (सार्वभौमिक शांति) की नीति अपनाई, जिसमें सहिष्णुता पर बल दिया गया", "type": "leaf"}
                    ]},
                    {"label": "मजहर और दीन-ए-इलाही", "type": "branch", "date": "सुधार", "children": [
                        {"label": "1579 में मजहर (घोषणापत्र) जारी किया, जिससे विवादित धार्मिक मामलों में अकबर अंतिम मध्यस्थ बना", "type": "leaf"},
                        {"label": "दीन-ए-इलाही (1582): एक नैतिक आचार संहिता जिसने एकेश्वरवाद और सर्वधर्म समभाव पर बल दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Ibadat Khana & Sulh-i-Kul", "type": "branch", "date": "Debates", "children": [
                        {"label": "Built Ibadat Khana (1575) at Fatehpur Sikri; opened it to scholars of all religions in 1578", "type": "leaf"},
                        {"label": "Adopted Sulh-i-Kul (universal peace/harmony) emphasizing absolute tolerance among faiths", "type": "leaf"}
                    ]},
                    {"label": "Infallibility Decree & Din-i-Ilahi", "type": "branch", "date": "Reforms", "children": [
                        {"label": "Issued Mahzar Nama (1579) making Akbar the supreme arbiter in case of religious disputes", "type": "leaf"},
                        {"label": "Din-i-Ilahi (1582): Ethical code combining virtues of various sects with focus on monotheism", "type": "leaf"}
                    ]}
                ]

        # 8. Akbar Expansion & Policies (Rajputs, Suzerainty, Northwest, Rebellions)
        elif 'akbar' in fl and ('rajput' in fl or 'suzerainty' in fl or 'northwest' in fl or 'expansion' in fl or 'conflict' in fl or 'hemu' in fl):
            if is_hindi:
                return [
                    {"label": "राजपूत नीति और वैवाहिक संबंध", "type": "branch", "date": "राजपूत", "children": [
                        {"label": "आमेर (जयपुर) के साथ वैवाहिक संबंध स्थापित किए; राजपूत प्रमुखों को उच्च मनसबदार बनाया", "type": "leaf"},
                        {"label": "1564 में जजिया कर और तीर्थयात्रा कर समाप्त कर राजपूतों और हिंदुओं का विश्वास जीता", "type": "leaf"}
                    ]},
                    {"label": "साम्राज्यिक सुदृढ़ीकरण", "type": "branch", "date": "विस्तार", "children": [
                        {"label": "गुजरात (1572) और बंगाल (1576) के समृद्ध व्यापारिक क्षेत्रों को जीतकर मुगलों में मिलाया", "type": "leaf"},
                        {"label": "उत्तर-पश्चिम सीमा सुरक्षा: काबुल, कश्मीर, सिंध और बलूचिस्तान को जीतकर सीमा मजबूत की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Rajput Policy & Alliances", "type": "branch", "date": "Rajputs", "children": [
                        {"label": "Established matrimonial alliances (e.g. Amber); appointed Rajput chiefs to highest mansabs", "type": "leaf"},
                        {"label": "Abolished Jizya tax (1564) and pilgrimage taxes, winning loyalty of Hindu rulers and masses", "type": "leaf"}
                    ]},
                    {"label": "Imperial Expansion", "type": "branch", "date": "Expansion", "children": [
                        {"label": "Conquered wealthy regions of Gujarat (1572) and Bengal (1576) to secure major trade ports", "type": "leaf"},
                        {"label": "Northwest Frontier: Annexed Kabul, Kashmir, Sind, and Baluchistan to secure strategic passes", "type": "leaf"}
                    ]}
                ]

        # 9. Aurangzeb Deccani States & Maratha Conflicts (Deccan Ulcer, Purandar)
        elif 'aurangzeb' in fl and ('deccan' in fl or 'maratha' in fl or 'purandar' in fl):
            if is_hindi:
                return [
                    {"label": "दक्कन का विलय", "type": "branch", "date": "दक्कन", "children": [
                        {"label": "बीजापुर (1686) और गोलकुंडा (1687) का सीधे मुगल साम्राज्य में विलय कर दिया", "type": "leaf"},
                        {"label": "पुरंदर की संधि (1665): राजा जयसिंह ने शिवाजी को 23 किले मुगलों को सौंपने पर मजबूर किया", "type": "leaf"}
                    ]},
                    {"label": "मराठा संघर्ष (दक्कन का नासूर)", "type": "branch", "date": "नासूर", "children": [
                        {"label": "1689 में मराठा राजा संभाजी को बंदी बनाकर मृत्युदंड दिया, जिसने मराठों में विद्रोह भड़काया", "type": "leaf"},
                        {"label": "मराठों का गुरिल्ला संघर्ष 25 वर्षों तक चला, जिसने मुगलों के वित्तीय और सैन्य संसाधनों को थका दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Deccan Sultanates Annexed", "type": "branch", "date": "Deccan", "children": [
                        {"label": "Annexed Deccani kingdoms of Bijapur (1686) and Golconda (1687) directly into the empire", "type": "leaf"},
                        {"label": "Treaty of Purandar (1665): Raja Jai Singh forced Shivaji to surrender 23 of his 35 forts", "type": "leaf"}
                    ]},
                    {"label": "Maratha Guerrilla War", "type": "branch", "date": "Conflict", "children": [
                        {"label": "Executed Maratha king Sambhaji in 1689, which unified Maratha resistance against Mughals", "type": "leaf"},
                        {"label": "Deccan Ulcer: Drained Aurangzeb's treasury and military reserves during a 25-year guerrilla war", "type": "leaf"}
                    ]}
                ]

        # 10. Aurangzeb Jagirdari Crisis & Assessment of Reign
        elif 'aurangzeb' in fl and ('jagirdari' in fl or 'crisis' in fl or 'assessment' in fl):
            if is_hindi:
                return [
                    {"label": "जागीरदारी संकट", "type": "branch", "date": "बे-जागीरी", "children": [
                        {"label": "बे-जागीरी: मनसबदारों की अत्यधिक संख्या के कारण आवंटित करने योग्य उपजाऊ भूमि (जागीर) की भारी कमी", "type": "leaf"},
                        {"label": "जागीरदारों द्वारा राजस्व बढ़ाने के लिए किसानों पर भारी अत्याचार किया गया", "type": "leaf"}
                    ]},
                    {"label": "कृषि विद्रोह", "type": "branch", "date": "विद्रोह", "children": [
                        {"label": "आर्थिक शोषण और रूढ़िवादी नीतियों के कारण जाटों, सतनामियों और बुंदेलों का विद्रोह हुआ", "type": "leaf"},
                        {"label": "सिखों और राजपूतों से लंबे संघर्ष ने साम्राज्य के प्रशासनिक ढांचे को पतन की ओर धकेला", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Jagirdari Crisis (Be-jagiri)", "type": "branch", "date": "Jagirdari", "children": [
                        {"label": "Be-jagiri: Inflated number of mansabdars faced a severe lack of fertile land assignments", "type": "leaf"},
                        {"label": "Temporary jagirdars over-exploited the peasantry to extract maximum revenue during tenure", "type": "leaf"}
                    ]},
                    {"label": "Agrarian Rebellions", "type": "branch", "date": "Rebellions", "children": [
                        {"label": "Heavy fiscal demands led to rebellions by peasant groups: Jats, Satnamis, and Bundelas", "type": "leaf"},
                        {"label": "Conflicts with Rajputs and Sikhs weakened political alliances, accelerating the empire's decline", "type": "leaf"}
                    ]}
                ]

        # 11. Aurangzeb General/Other Aspects (Orthodoxy, Sikh Conflicts)
        elif 'aurangzeb' in fl:
            if is_hindi:
                return [
                    {"label": "धार्मिक नीतियां", "type": "branch", "date": "नीतियां", "children": [
                        {"label": "1679 में जजिया कर पुनः लागू किया; दरबार में संगीत, झरोखा दर्शन और नौरोज पर प्रतिबंध लगाया", "type": "leaf"},
                        {"label": "शाही मुहतसिब (नैतिक आचरण अधिकारी) नियुक्त किए ताकि सार्वजनिक नैतिकता सुनिश्चित की जा सके", "type": "leaf"}
                    ]},
                    {"label": "सिखों से संघर्ष", "type": "branch", "date": "सिख", "children": [
                        {"label": "1675 में 9वें सिख गुरु तेग बहादुर को प्राणदंड दिया; इसके परिणामस्वरूप गुरु गोविंद सिंह ने खालसा (1699) बनाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Orthodox Religious Measures", "type": "branch", "date": "Policies", "children": [
                        {"label": "Re-imposed Jizya tax in 1679; banned music, Jharokha Darshan, and Nauroz at court", "type": "leaf"},
                        {"label": "Appointed Muhtasibs (censors of public morals) to enforce Islamic law and restrict vices", "type": "leaf"}
                    ]},
                    {"label": "Sikh Confrontation", "type": "branch", "date": "Sikhs", "children": [
                        {"label": "Executed the 9th Sikh Guru, Tegh Bahadur, in 1675, leading to the formation of the military Khalsa in 1699", "type": "leaf"}
                    ]}
                ]

        # 14. Babur Challenges after Panipat & Eastern Campaigns
        elif 'babur' in fl and ('challenge' in fl or 'problem' in fl or 'eastern' in fl or 'afghan' in fl):
            if is_hindi:
                return [
                    {"label": "पानीपत के बाद की चुनौतियां", "type": "branch", "date": "चुनौतियां", "children": [
                        {"label": "महमूद लोदी के अधीन अफगानों का कड़ा विरोध और भारतीय गर्म जलवायु के कारण सैनिकों का विद्रोह टालना", "type": "leaf"},
                        {"label": "आगरा पर अधिकार मजबूत करने के लिए राजपूत और अफगान प्रमुखों के गठजोड़ को तोड़ना", "type": "leaf"}
                    ]},
                    {"label": "पूर्वी अभियान", "type": "branch", "date": "घाघरा", "children": [
                        {"label": "घाघरा का युद्ध (1529): बिहार और बंगाल की संयुक्त अफगान सेनाओं को पराजित कर पूर्वी सीमा सुरक्षित की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Post-Panipat Challenges", "type": "branch", "date": "Challenges", "children": [
                        {"label": "Faced Afghan opposition under Mahmud Lodi and hot climate; prevented mutiny of homesick troops", "type": "leaf"},
                        {"label": "Need to quickly capture fortress cities (Agra, Gwalior) to solidify his base of power", "type": "leaf"}
                    ]},
                    {"label": "Eastern Campaign", "type": "branch", "date": "Ghagra", "children": [
                        {"label": "Battle of Ghagra (1529): Defeated joint Afghan forces of Bihar and Bengal, securing the eastern flank", "type": "leaf"}
                    ]}
                ]

        # 12. Babur First Battle of Panipat
        elif 'babur' in fl and 'panipat' in fl:
            if is_hindi:
                return [
                    {"label": "पानीपत का युद्ध एवं रणनीति", "type": "branch", "date": "1526 ई.", "children": [
                        {"label": "बाबर ने दिल्ली के अंतिम सुल्तान इब्राहिम लोदी को हराकर मुगल सत्ता की नींव रखी", "type": "leaf"},
                        {"label": "तुलुगमा युद्ध नीति: सेना को विभिन्न भागों में बांटकर दुश्मन को घेरने की योजना बनाई", "type": "leaf"}
                    ]},
                    {"label": "ऐतिहासिक प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "उस्ताद अली और मुस्तफा के नेतृत्व में बारूद और तोपखाने का उत्तर भारत में पहला बड़ा प्रयोग", "type": "leaf"},
                        {"label": "लोदी वंश के साथ दिल्ली सल्तनत का पूर्ण अंत हुआ और एक नए साम्राज्य का उदय हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Battle & Strategy", "type": "branch", "date": "1526 AD", "children": [
                        {"label": "Babur defeated Ibrahim Lodi, ending Delhi Sultanate and establishing the Mughal Empire", "type": "leaf"},
                        {"label": "Tulughma flanking strategy: Divided the army into units to surround the enemy lines", "type": "leaf"}
                    ]},
                    {"label": "Historical Impact", "type": "branch", "date": "Impact", "children": [
                        {"label": "First major use of field artillery and gunpowder in North India under Ottoman gunners", "type": "leaf"},
                        {"label": "Ended the Lodi Dynasty, marking the beginning of the centralized Mughal authority", "type": "leaf"}
                    ]}
                ]

        # 13. Babur Struggle with Rana Sanga (Khanwa)
        elif 'babur' in fl and ('sanga' in fl or 'khanwa' in fl):
            if is_hindi:
                return [
                    {"label": "खानवा का युद्ध संघर्ष", "type": "branch", "date": "1527 ई.", "children": [
                        {"label": "बाबर और मेवाड़ के राणा सांगा के शक्तिशाली राजपूत गठबंधन के बीच ऐतिहासिक टकराव", "type": "leaf"},
                        {"label": "सैनिकों का मनोबल बढ़ाने के लिए बाबर ने शराब पर प्रतिबंध लगाया और इसे जिहाद घोषित किया", "type": "leaf"}
                    ]},
                    {"label": "साम्राजिक परिणाम", "type": "branch", "date": "परिणाम", "children": [
                        {"label": "जीत के बाद बाबर ने 'गाजी' की उपाधि ली; भारत में मुगलों का स्थायी नियंत्रण मजबूत हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Conflict with Sanga", "type": "branch", "date": "1527 AD", "children": [
                        {"label": "Fought against the Rajput confederacy led by Rana Sanga of Mewar at Khanwa", "type": "leaf"},
                        {"label": "Babur declared it Jihad and banned wine to motivate his outnumbered troops", "type": "leaf"}
                    ]},
                    {"label": "Strategic Legacy", "type": "branch", "date": "Result", "children": [
                        {"label": "Assumed the title of 'Ghazi' after victory, eliminating the Rajput threat to Delhi", "type": "leaf"}
                    ]}
                ]

        # 15. Babur General: Advent, Contribution & Significance
        elif 'babur' in fl:
            if is_hindi:
                return [
                    {"label": "सैनिक विस्तार", "type": "branch", "date": "अभियान", "children": [
                        {"label": "चंदेरी का युद्ध (1528): मेदिनी राय को हराया; घाघरा का युद्ध (1529): अफगान संयुक्त सेना को हराया", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक एवं सांस्कृतिक धरोहर", "type": "branch", "date": "बाबरनामा", "children": [
                        {"label": "तुजुक-ए-बाबरी: चगताई तुर्की में लिखी आत्मकथा जिसमें भारत की प्रकृति और भूगोल का विवरण है", "type": "leaf"},
                        {"label": "भारत में चारबाग शैली (ज्यामितीय रूप से विभाजित बाग-बगीचे) की शुरुआत की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Military Expansion", "type": "branch", "date": "Campaigns", "children": [
                        {"label": "Battle of Chanderi (1528) against Medini Rai; Battle of Ghagra (1529) against joint Afghan forces", "type": "leaf"}
                    ]},
                    {"label": "Literary & Cultural Legacy", "type": "branch", "date": "Tuzuk", "children": [
                        {"label": "Tuzuk-i-Baburi: Autographed memoirs in Chagatai Turkish, describing Indian flora, fauna, and society", "type": "leaf"},
                        {"label": "Introduced the symmetrical Charbagh (four-fold garden) layout style to Indian landscape", "type": "leaf"}
                    ]}
                ]

        # 16. Humayun Early Activities & Tussle with Bahadur Shah (Gujarat Campaign)
        elif 'humayun' in fl and ('bahadur' in fl or 'gujarat' in fl or 'early' in fl):
            if is_hindi:
                return [
                    {"label": "गुजरात अभियान", "type": "branch", "date": "1535-36 ई.", "children": [
                        {"label": "गुजरात के बहादुर शाह ने मालवा जीता और चित्तौड़ का घेराव किया, जो दिल्ली के लिए खतरा था", "type": "leaf"},
                        {"label": "हुमायूं ने मांडू और चंपानेर के किलों पर विजय प्राप्त की; बहादुर शाह दीव भाग गया", "type": "leaf"}
                    ]},
                    {"label": "प्रशासनिक विफलता", "type": "branch", "date": "परिणाम", "children": [
                        {"label": "विजित क्षेत्रों पर प्रशासनिक नियंत्रण स्थापित न कर पाने और पूर्व में शेर खान के विद्रोह के कारण हटना पड़ा", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Gujarat Campaign", "type": "branch", "date": "1535-36 AD", "children": [
                        {"label": "Bahadur Shah of Gujarat annexed Malwa and besieged Chittor, threatening Delhi's flank", "type": "leaf"},
                        {"label": "Humayun captured Mandu and Champaner; Bahadur Shah fled to Diu", "type": "leaf"}
                    ]},
                    {"label": "Strategic Failure", "type": "branch", "date": "Withdrawal", "children": [
                        {"label": "Failure to consolidate control led to rapid withdrawal as Sher Khan revolted in the east", "type": "leaf"}
                    ]}
                ]

        # 17. Humayun Bengal Campaign & Struggle with Sher Khan
        elif 'humayun' in fl and ('bengal' in fl or 'sher-khan' in fl or 'tussle' in fl or 'afghans' in fl):
            if is_hindi:
                return [
                    {"label": "बंगाल अभियान", "type": "branch", "date": "1538 ई.", "children": [
                        {"label": "हुमायूं ने बंगाल की राजधानी गौड़ पर अधिकार किया और उसका नाम 'जन्नतबाद' रखा", "type": "leaf"}
                    ]},
                    {"label": "चौसा और कन्नौज के युद्ध", "type": "branch", "date": "पराजित", "children": [
                        {"label": "चौसा का युद्ध (1539): शेर खान ने हुमायूं को गंगा किनारे पराजित किया; हुमायूं ने भिश्ती की मदद ली", "type": "leaf"},
                        {"label": "कन्नौज का युद्ध (1540): शेरशाह ने हुमायूं को फिर हराया; हुमायूं को 15 वर्ष के लिए निर्वासित होना पड़ा", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Bengal Occupation", "type": "branch", "date": "1538 AD", "children": [
                        {"label": "Humayun occupied Gaur (Bengal), naming it Jannatabad, while Sher Khan cut off his supply lines", "type": "leaf"}
                    ]},
                    {"label": "Decisive Defeats", "type": "branch", "date": "Losses", "children": [
                        {"label": "Battle of Chausa (1539): Decisive defeat of Humayun by Sher Khan near Buxar via night attack", "type": "leaf"},
                        {"label": "Battle of Kannauj (1540): Sher Shah defeated Humayun again, forcing him into a 15-year Safavid exile", "type": "leaf"}
                    ]}
                ]

        # 18. Humayun General (Restoration & Death)
        elif 'humayun' in fl:
            if is_hindi:
                return [
                    {"label": "मुगल सत्ता की पुनर्स्थापना", "type": "branch", "date": "1555 ई.", "children": [
                        {"label": "सरहिंद का युद्ध (1555): फारसी शाह तहमास्प की मदद से शेरशाह के कमजोर उत्तराधिकारियों को हराया", "type": "leaf"}
                    ]},
                    {"label": "मृत्यु", "type": "branch", "date": "1556 ई.", "children": [
                        {"label": "1556 ई. में दिल्ली में अपने पुस्तकालय शेर मंडल की सीढ़ियों से गिरकर हुमायूं की मृत्यु हुई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Return to Power", "type": "branch", "date": "1555 AD", "children": [
                        {"label": "Battle of Sirhind (1555): Humayun defeated Sikandar Suri with Safavid military aid to regain Delhi", "type": "leaf"}
                    ]},
                    {"label": "Tragic End", "type": "branch", "date": "1556 AD", "children": [
                        {"label": "Died in 1556 AD from a fatal fall down the stairs of his library building (Sher Mandal) in Delhi", "type": "leaf"}
                    ]}
                ]

        # 19. Sher Shah Suri Contribution: Coinage
        elif ('sher-shah' in fl or 'sur-empire' in fl) and 'coinage' in fl:
            if is_hindi:
                return [
                    {"label": "चांदी और तांबे के सिक्के", "type": "branch", "date": "मुद्रा प्रणाली", "children": [
                        {"label": "पुराने मिलावटी सिक्कों को बंद कर 178 ग्रेन का शुद्ध चांदी का सिक्का 'रुपिया' चलाया", "type": "leaf"},
                        {"label": "छोटे व्यापार के लिए तांबे का सिक्का 'दाम' चलाया; अनुपात 1 रुपिया = 64 दाम था", "type": "leaf"}
                    ]},
                    {"label": "टक्सालों का आधुनिकीकरण", "type": "branch", "date": "सुधार", "children": [
                        {"label": "टक्सालों को मानकीकृत किया और सिक्कों पर देवनागरी तथा फारसी लिपि में नाम खुदवाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Monetary Reforms", "type": "branch", "date": "Currency System", "children": [
                        {"label": "Abolished mixed-metal debased coins; introduced standard silver Rupia (178 grains)", "type": "leaf"},
                        {"label": "Issued copper coin Dam (ratio 1 Rupia = 64 Dams) for low-value daily market transactions", "type": "leaf"}
                    ]},
                    {"label": "Mint Standardization", "type": "branch", "date": "Mints", "children": [
                        {"label": "Established standard mints across the empire with legends embossed in Devanagari & Persian", "type": "leaf"}
                    ]}
                ]

        # 20. Sher Shah Suri Contribution: Architecture
        elif ('sher-shah' in fl or 'sur-empire' in fl) and 'architecture' in fl:
            if is_hindi:
                return [
                    {"label": "सासाराम मकबरा", "type": "branch", "date": "लाल बलुआ पत्थर", "children": [
                        {"label": "सासाराम (बिहार) में झील के बीच स्थित अपना शानदार अष्टकोणीय लाल बलुआ पत्थर का मकबरा बनवाया", "type": "leaf"}
                    ]},
                    {"label": "दिल्ली के स्मारक", "type": "branch", "date": "दिल्ली निर्माण", "children": [
                        {"label": "दिल्ली में पुराना किला परिसर में किला-ए-कुहना मस्जिद और शेर मंडल भवन का निर्माण कराया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sasaram Tomb", "type": "branch", "date": "Sandstone", "children": [
                        {"label": "Built his octagonal red sandstone tomb in Sasaram (Bihar), situated in the middle of an artificial lake", "type": "leaf"}
                    ]},
                    {"label": "Delhi Monuments", "type": "branch", "date": "Purana Qila", "children": [
                        {"label": "Constructed Qila-i-Kuhna Mosque and Sher Mandal pavilion inside Delhi's Purana Qila", "type": "leaf"}
                    ]}
                ]

        # 21. Sher Shah Suri Rise & Administration (Sur Empire)
        elif 'sher-shah' in fl or 'sur-empire' in fl or 'bihar' in fl:
            if is_hindi:
                return [
                    {"label": "राजस्व और पैमाइश सुधार", "type": "branch", "date": "1540-1545 ई.", "children": [
                        {"label": "सिकंदरी गज (32 अंक) से भूमि का मापन कराया और उपज के आधार पर कर अनुसूची 'रई' बनाई", "type": "leaf"},
                        {"label": "किसानों को पट्टा (भूमि स्वामित्व विलेख) और कबूलियत (अनुबंध) देने की व्यवस्था की", "type": "leaf"}
                    ]},
                    {"label": "बुनियादी ढांचा एवं सुरक्षा", "type": "branch", "date": "सड़कें", "children": [
                        {"label": "सड़क-ए-आजम (ग्रैंड ट्रंक रोड) का पुनरुद्धार कराया; यात्रियों के लिए 1700 सरायें बनवाईं", "type": "leaf"},
                        {"label": "स्थानीय पुलिस उत्तरदायित्व: स्थानीय चोरी के लिए स्थानीय मुकद्दम (मुखिया) को जिम्मेदार ठहराया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Agrarian Reforms", "type": "branch", "date": "Reforms", "children": [
                        {"label": "Measured land using Sikandari Gaz; established crop rate schedules called Ray for assessment", "type": "leaf"},
                        {"label": "Introduced Patta (title deeds) and Qabuliyat (deeds of agreement) to secure peasants", "type": "leaf"}
                    ]},
                    {"label": "Infrastructure & Security", "type": "branch", "date": "Serais", "children": [
                        {"label": "Restored Grand Trunk Road (Sadak-e-Azam); built 1700 Sarais integrated with Dak chowkis", "type": "leaf"},
                        {"label": "Enforced local police responsibility: Village headmen (Muqaddams) held liable for local thefts", "type": "leaf"}
                    ]}
                ]

        # 22. Jahangir: Arrival of British Envoys
        elif 'jahangir' in fl and ('british' in fl or 'envoy' in fl):
            if is_hindi:
                return [
                    {"label": "विलियम हॉकिन्स का आगमन", "type": "branch", "date": "1608 ई.", "children": [
                        {"label": "ईस्ट इंडिया कंपनी का दूत बनकर आगरा दरबार आया; फारसी में बात की; 400 का मनसब मिला", "type": "leaf"}
                    ]},
                    {"label": "सर थॉमस रो का मिशन", "type": "branch", "date": "1615 ई.", "children": [
                        {"label": "जेम्स प्रथम के राजदूत के रूप में आया; सूरत में फैक्ट्री खोलने का फरमान हासिल किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Hawkins Embassy", "type": "branch", "date": "1608 AD", "children": [
                        {"label": "William Hawkins: English representative who spoke Persian; granted 400 Mansab rank", "type": "leaf"}
                    ]},
                    {"label": "Sir Thomas Roe", "type": "branch", "date": "1615 AD", "children": [
                        {"label": "Ambassador of King James I; obtained royal farman to establish factory at Surat", "type": "leaf"}
                    ]}
                ]

        # 23. Jahangir Mewar, Consolidation & Expansion
        elif 'jahangir' in fl and ('mewar' in fl or 'consolidation' in fl or 'territorial' in fl or 'expansion' in fl):
            if is_hindi:
                return [
                    {"label": "मेवाड़ से संधि", "type": "branch", "date": "1615 ई.", "children": [
                        {"label": "राणा अमर सिंह के साथ ऐतिहासिक समझौता; चित्तौड़ का किला बिना मरम्मत शर्त के लौटाया", "type": "leaf"},
                        {"label": "राजपूत प्रमुखों को मुगल मनसबदारी में सम्मानजनक स्थान देकर मेवाड़ विवाद का अंत किया", "type": "leaf"}
                    ]},
                    {"label": "दक्कन अभियान", "type": "branch", "date": "दक्कन", "children": [
                        {"label": "अहमदनगर के मलिक अंबर के खिलाफ संघर्ष; मुगलों ने खुर्रम (शाहजहां) के नेतृत्व में आंशिक सफलता पाई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Treaty of Mewar", "type": "branch", "date": "1615 AD", "children": [
                        {"label": "Settled Mewar conflict peacefully with Rana Amar Singh; returned Chittor Fort under non-fortification terms", "type": "leaf"},
                        {"label": "Enlisted Mewar prince in Mansabdari structure, restoring imperial prestige without humiliation", "type": "leaf"}
                    ]},
                    {"label": "Deccan Operations", "type": "branch", "date": "Deccan", "children": [
                        {"label": "Encountered stiff resistance from Malik Ambar of Ahmadnagar who utilized Maratha light cavalry", "type": "leaf"}
                    ]}
                ]

        # 24. Jahangir General (Justice, Sikh conflict)
        elif 'jahangir' in fl:
            if is_hindi:
                return [
                    {"label": "न्याय प्रशासन", "type": "branch", "date": "न्याय की जंजीर", "children": [
                        {"label": "आगरा किले में सोने की घंटी वाली न्याय की जंजीर (जंजीर-ए-अदल) लगवाई ताकि जनता सीधे शिकायत कर सके", "type": "leaf"}
                    ]},
                    {"label": "सिखों से संघर्ष", "type": "branch", "date": "सिख", "children": [
                        {"label": "विद्रोही शहजादे खुसरो की मदद के कारण 5वें सिख गुरु अर्जुन देव को मृत्युदंड दिया, जिससे संघर्ष शुरू हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Administration of Justice", "type": "branch", "date": "Justice", "children": [
                        {"label": "Installed the Chain of Justice (Zanjir-i-Adl) with golden bells at Agra Fort for direct public petitions", "type": "leaf"}
                    ]},
                    {"label": "Sikh Conflict", "type": "branch", "date": "Sikhs", "children": [
                        {"label": "Executed the 5th Sikh Guru, Arjan Dev, for harboring rebel Prince Khusrau, alienating the Sikh community", "type": "leaf"}
                    ]}
                ]

        # 25. Shah Jahan Art & Architecture
        elif 'shah-jahan' in fl and ('art' in fl or 'architecture' in fl):
            if is_hindi:
                return [
                    {"label": "वास्तुकला की मुख्य विशेषताएं", "type": "branch", "date": "संगमरमर", "children": [
                        {"label": "सफेद संगमरमर और बहुमूल्य पत्थरों की जड़ाई (पिएट्रा ड्यूरा) का बड़े पैमाने पर प्रयोग", "type": "leaf"},
                        {"label": "सहानुभूतिपूर्ण ज्यामितीय लेआउट और चारबाग शैली का चरम विकास", "type": "leaf"}
                    ]},
                    {"label": "प्रमुख स्मारक", "type": "branch", "date": "स्मारक", "children": [
                        {"label": "ताजमहल (आगरा), दिल्ली का लाल किला, जामा मस्जिद और मयूर सिंहासन (तख्त-ए-ताऊस) का निर्माण", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Aesthetics & Inlay Work", "type": "branch", "date": "Style", "children": [
                        {"label": "Extensive use of white marble and precious gemstone inlay work (Pietra Dura)", "type": "leaf"},
                        {"label": "Zenith of symmetrical layout designs and Charbagh (four-fold garden) planning", "type": "leaf"}
                    ]},
                    {"label": "Major Monuments", "type": "branch", "date": "Buildings", "children": [
                        {"label": "Constructed Taj Mahal, Red Fort (Delhi), Jama Masjid, and the Peacock Throne (Takht-i-Tavus)", "type": "leaf"}
                    ]}
                ]

        # 26. Shah Jahan Ruling Class & Mansabdari Reforms
        elif 'shah-jahan' in fl:
            if is_hindi:
                return [
                    {"label": "माहाना जागीर प्रणाली", "type": "branch", "date": "राजस्व", "children": [
                        {"label": "माहाना प्रणाली (महीने का पैमाना): जागीर के वास्तविक राजस्व (हासिल) का अनुमानित (जमा) से मिलान किया", "type": "leaf"}
                    ]},
                    {"label": "सैन्य कोटा में कमी", "type": "branch", "date": "मनसबदारी", "children": [
                        {"label": "दूरस्थ क्षेत्रों में तैनात मनसबदारों के लिए आवश्यक घुड़सवारों का कोटा कम किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Month-Scale System", "type": "branch", "date": "Revenue", "children": [
                        {"label": "Month-Scale (Mahana system): Matched estimated revenue (Jama) with actual yield (Hasil)", "type": "leaf"}
                    ]},
                    {"label": "Mansab Military Quotas", "type": "branch", "date": "Military", "children": [
                        {"label": "Scaled down the required cavalry quotas for mansabdars stationed in distant provinces", "type": "leaf"}
                    ]}
                ]

        # 27. Later Mughals: Bahadur Shah II (Zafar) & 1857
        elif 'later-mughals' in fl and ('zafar' in fl or 'bahadur-shah-ii' in fl or 'shah-ii' in fl):
            if is_hindi:
                return [
                    {"label": "1857 का विद्रोह", "type": "branch", "date": "1857 ई.", "children": [
                        {"label": "अंतिम मुगल सम्राट; 1857 के प्रथम स्वतंत्रता संग्राम में विद्रोहियों ने इन्हें भारत का सम्राट घोषित किया", "type": "leaf"}
                    ]},
                    {"label": "निर्वासन और अंत", "type": "branch", "date": "रंगून", "children": [
                        {"label": "विद्रोह के दमन के बाद अंग्रेजों द्वारा रंगून (बर्मा) निर्वासित किया गया, जहाँ इनकी मृत्यु हुई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Revolt of 1857", "type": "branch", "date": "1857 AD", "children": [
                        {"label": "Last Mughal emperor; chosen as nominal leader of the Great Revolt of 1857 by mutinous sepoys", "type": "leaf"}
                    ]},
                    {"label": "Exile to Rangoon", "type": "branch", "date": "Rangoon", "children": [
                        {"label": "Tried for treason and exiled to Rangoon (Burma) by the British, ending the Mughal dynasty line", "type": "leaf"}
                    ]}
                ]

        # 28. Later Mughals: Farrukhsiyar
        elif 'later-mughals' in fl and 'farrukhsiyar' in fl:
            if is_hindi:
                return [
                    {"label": "शाही फरमान", "type": "branch", "date": "1717 ई.", "children": [
                        {"label": "1717 में ब्रिटिश ईस्ट इंडिया कंपनी को व्यापारिक अधिकार पत्र (शाही फरमान/दस्तक) दिया", "type": "leaf"}
                    ]},
                    {"label": "सैयद बंधुओं का प्रभाव", "type": "branch", "date": "किंग मेकर्स", "children": [
                        {"label": "सैयद बंधुओं (किंग मेकर्स) की मदद से गद्दी मिली; बाद में उन्हीं के द्वारा पदच्युत कर मारे गए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "EIC Royal Farman", "type": "branch", "date": "1717 AD", "children": [
                        {"label": "Issued the Royal Farman of 1717 to the East India Company, granting tax-free trading rights in Bengal", "type": "leaf"}
                    ]},
                    {"label": "Sayyid Brothers (King Makers)", "type": "branch", "date": "Sayyids", "children": [
                        {"label": "Placed on throne by Sayyid Brothers; eventually blinded and murdered by them", "type": "leaf"}
                    ]}
                ]

        # 29. Later Mughals: Muhammad Shah Rangeela & Nadir Shah
        elif 'later-mughals' in fl and ('rangeela' in fl or 'muhammad-shah' in fl):
            if is_hindi:
                return [
                    {"label": "साम्राज्य का पतन", "type": "branch", "date": "पतन", "children": [
                        {"label": "विलासिता पूर्ण जीवन के कारण 'रंगीला' उपनाम मिला; बंगाल, अवध और हैदराबाद स्वतंत्र हो गए", "type": "leaf"}
                    ]},
                    {"label": "नादिर शाह का आक्रमण", "type": "branch", "date": "1739 ई.", "children": [
                        {"label": "नादिर शाह का आक्रमण (1739): करनाल के युद्ध में मुगलों को हराया; कोहिनूर और तख्त-ए-ताऊस लूट ले गया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Decline & Breakup", "type": "branch", "date": "Decline", "children": [
                        {"label": "Nicknamed 'Rangeela' due to his decadent lifestyle; oversaw the independence of Hyderabad and Bengal", "type": "leaf"}
                    ]},
                    {"label": "Nadir Shah's Invasion", "type": "branch", "date": "1739 AD", "children": [
                        {"label": "Nadir Shah's Invasion (1739): Sacked Delhi, looted the Kohinoor diamond and the Peacock Throne", "type": "leaf"}
                    ]}
                ]

        # 30. Later Mughals: Shah Alam II (Buxar)
        elif 'later-mughals' in fl and ('shah-alam' in fl or 'buxar' in fl):
            if is_hindi:
                return [
                    {"label": "बक्सर का युद्ध", "type": "branch", "date": "1764 ई.", "children": [
                        {"label": "बक्सर का युद्ध (1764): अंग्रेजों के खिलाफ मीर कासिम और शुजाउद्दौला के साथ मिलकर लड़े", "type": "leaf"}
                    ]},
                    {"label": "इलाहाबाद की संधि", "type": "branch", "date": "1765 ई.", "children": [
                        {"label": "इलाहाबाद की संधि (1765): ईस्ट इंडिया कंपनी को बंगाल, बिहार और उड़ीसा के दीवानी अधिकार सौंपे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Battle of Buxar", "type": "branch", "date": "1764 AD", "children": [
                        {"label": "Battle of Buxar (1764): Fought in alliance with Shuja-ud-Daula and Mir Qasim against the British", "type": "leaf"}
                    ]},
                    {"label": "Treaty of Allahabad", "type": "branch", "date": "1765 AD", "children": [
                        {"label": "Treaty of Allahabad (1765): Granted Diwani (revenue collection rights) of Bengal, Bihar, and Odisha to EIC", "type": "leaf"}
                    ]}
                ]

        # 31. Later Mughals: Bahadur Shah I (Shah-i-Bekhabar)
        elif 'later-mughals' in fl and ('bahadur-shah' in fl or 'shah-i-bekhabar' in fl or 'shah-i' in fl):
            if is_hindi:
                return [
                    {"label": "सुलह की नीति", "type": "branch", "date": "सुलह", "children": [
                        {"label": "राजपूतों, मराठों (साहू को मुक्त किया) और सिखों के साथ शांतिपूर्ण संबंध बनाने की कोशिश की", "type": "leaf"}
                    ]},
                    {"label": "शाहे बेखबर", "type": "branch", "date": "वित्तीय पतन", "children": [
                        {"label": "अंधाधुंध जागीरों और पुरस्कारों के वितरण से खजाना खाली हुआ; वित्तीय पतन नहीं रोक पाए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Policy of Reconciliation", "type": "branch", "date": "Peace", "children": [
                        {"label": "Attempted peaceful relations with Rajputs, Sikhs (initially), and Marathas (released Shahu)", "type": "leaf"}
                    ]},
                    {"label": "Shah-i-Bekhabar", "type": "branch", "date": "Finance", "children": [
                        {"label": "Called 'Heedless King' due to reckless grant of jagirs, promoting imperial financial collapse", "type": "leaf"}
                    ]}
                ]

        # 32. Later Mughals: Other Puppet Emperors (Jahandar Shah, Alamgir II, Rafi Rulers, Akbar II)
        elif 'later-mughals' in fl and ('jahandar' in fl or 'darajat' in fl or 'daula' in fl or 'alamgir' in fl or 'ahmad' in fl or 'akbar-ii' in fl or 'shah-jahan-iii' in fl):
            if is_hindi:
                return [
                    {"label": "कठपुतली शासक", "type": "branch", "date": "दरबारी गुट", "children": [
                        {"label": "जुल्फिकार खान और सैयद बंधुओं जैसे शक्तिशाली रईसों के संरक्षण में संक्षिप्त शासन किया", "type": "leaf"}
                    ]},
                    {"label": "साम्राज्य का सिकुड़ना", "type": "branch", "date": "दुर्बलता", "children": [
                        {"label": "अकबर द्वितीय का अधिकार लाल किले तक सीमित हुआ; राजा राममोहन राय को राजदूत बनाकर भेजा", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Puppet Emperors", "type": "branch", "date": "Factions", "children": [
                        {"label": "Reigned briefly under the control of powerful nobles (e.g. Zulfiqar Khan, Sayyid Brothers)", "type": "leaf"}
                    ]},
                    {"label": "Shrinking Authority", "type": "branch", "date": "Powerless", "children": [
                        {"label": "Akbar II's authority restricted to Red Fort; sent Raja Ram Mohan Roy to England to petition for pension", "type": "leaf"}
                    ]}
                ]

        # 33. Later Mughals: Imperial Decline and Successor States
        elif 'later-mughals' in fl:
            if is_hindi:
                return [
                    {"label": "साम्राज्यिक विखंडन", "type": "branch", "date": "विखंडन", "children": [
                        {"label": "बंगाल, अवध और हैदराबाद के राज्यपालों ने व्यावहारिक रूप से स्वतंत्र रियासतें बनाईं", "type": "leaf"},
                        {"label": "पेशवा बाजीराव प्रथम के नेतृत्व में मराठा शक्ति का उत्तर भारत में व्यापक प्रसार हुआ", "type": "leaf"}
                    ]},
                    {"label": "विदेशी आक्रमण", "type": "branch", "date": "आक्रमण", "children": [
                        {"label": "अहमद शाह अब्दाली के बार-बार आक्रमणों ने साम्राज्य के उत्तरी क्षेत्रों को लूटा और पंगु कर दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Imperial Fragmentation", "type": "branch", "date": "Fragmentation", "children": [
                        {"label": "Provincial governors of Bengal, Awadh, and Hyderabad carved out autonomous successor states", "type": "leaf"},
                        {"label": "Marathas expanded into North India under Peshwa Baji Rao I, challenging Delhi's control", "type": "leaf"}
                    ]},
                    {"label": "Foreign Raids", "type": "branch", "date": "Raids", "children": [
                        {"label": "Multiple raids by Ahmad Shah Abdali devastated northern plains, draining political stability", "type": "leaf"}
                    ]}
                ]

        # 34. Mughal Economy (Trade, Commerce, Overland, Overseas)
        elif 'mughal-economy' in fl or 'economy' in fl:
            if is_hindi:
                return [
                    {"label": "आंतरिक और सीमा पार व्यापार", "type": "branch", "date": "व्यापार मार्ग", "children": [
                        {"label": "बंजारों द्वारा अनाज का अंतर्देशीय परिवहन; खैबर और बोलन दर्रों द्वारा मध्य एशिया से जुड़ाव", "type": "leaf"},
                        {"label": "Surat (पश्चिम) और Hughli (पूर्व) से लाल सागर, फारस की खाड़ी और दक्षिण-पूर्व एशिया से व्यापार", "type": "leaf"}
                    ]},
                    {"label": "राजकीय आर्थिक नीति", "type": "branch", "date": "मुद्रा", "children": [
                        {"label": "उच्च शुद्धता वाले चांदी के रुपिये और तांबे के दाम का सुचारू संचालन; हुंडी (साख पत्र) का प्रयोग", "type": "leaf"},
                        {"label": "राज्य द्वारा सड़कों पर सुरक्षा (राहदारी) सुनिश्चित की गई और सीमा शुल्क से राजस्व बढ़ाया गया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Inland & Overland Trade", "type": "branch", "date": "Routes", "children": [
                        {"label": "Bulk grain transport managed by nomadic Banjaras; overland trade via Khyber and Bolan passes", "type": "leaf"},
                        {"label": "Maritime trade flourished through ports of Surat and Hughli to Red Sea and SE Asia", "type": "leaf"}
                    ]},
                    {"label": "State Commerce Policy", "type": "branch", "date": "Monetary", "children": [
                        {"label": "High-purity silver Rupia and copper Dam backed stable currency; extensive use of Hundis (bills of exchange)", "type": "leaf"},
                        {"label": "Levied custom duties (Zakat/Rahdari) while actively protecting merchants on major highways", "type": "leaf"}
                    ]}
                ]

        # 35. Mughal Society (Artisans, Rural Classes, Ruling Elite, Middle Strata)
        elif 'mughal-society' in fl or 'society' in fl:
            if is_hindi:
                return [
                    {"label": "सामाजिक श्रेणियां", "type": "branch", "date": "श्रेणियां", "children": [
                        {"label": "शासक अभिजात वर्ग (अमीर, मनसबदार, जमींदार) जो अत्यधिक ऐश्वर्यशाली जीवन जीते थे", "type": "leaf"},
                        {"label": "व्यापारी वर्ग (सेठ, बोहरा, सर्राफ) और उभरता मध्यम वर्ग (लिपिक, लेखक, वैध)", "type": "leaf"}
                    ]},
                    {"label": "कृषक और शिल्पकार", "type": "branch", "date": "ग्रामीण एवं शहरी", "children": [
                        {"label": "खुदकाश्त (स्थायी किसान) और पाहीकाश्त (अस्थायी किसान) में बंटा ग्रामीण समाज", "type": "leaf"},
                        {"label": "शिल्पकार स्वतंत्र रूप से या शाही कारखानों में काम करते थे; दासों का घरेलू काम में उपयोग", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Social Stratification", "type": "branch", "date": "Hierarchy", "children": [
                        {"label": "Ruling class (Mansabdars/Zamindars) consumed major surplus, living in luxury", "type": "leaf"},
                        {"label": "Commercial classes (Banias, Sarrafs) managed finance; middle strata consisted of professionals & scribes", "type": "leaf"}
                    ]},
                    {"label": "Peasants & Artisans", "type": "branch", "date": "Labor", "children": [
                        {"label": "Rural society divided into Khud-kasht (proprietors) and Pahi-kasht (tenant cultivators)", "type": "leaf"},
                        {"label": "Artisans produced textiles and metalware in private workshops or state-owned Karkhanas", "type": "leaf"}
                    ]}
                ]

        # Fallback for Mughal Rule
        else:
            if is_hindi:
                return [
                    {"label": "मुगल साम्राज्य सामान्य", "type": "branch", "date": "मुगल शासन", "children": [
                        {"label": "मनसबदारी व्यवस्था और भू-राजस्व (दहसाला) प्रशासन के मुख्य स्तंभ थे", "type": "leaf"},
                        {"label": "गंगा-जमुनी तहजीब, वास्तुकला, चित्रकला और साहित्य का स्वर्णिम विकास", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Mughal Empire Overview", "type": "branch", "date": "Overview", "children": [
                        {"label": "Founded in 1526 AD; consolidated administrative machinery under Akbar and Shah Jahan", "type": "leaf"},
                        {"label": "Characterized by Mansabdari military ranks, Dahsala revenue system, and Indo-Islamic architecture", "type": "leaf"}
                    ]}
                ]
    # =========================================================================
    # C. BAHMANI KINGDOM
    # =========================================================================
    elif 'bahmani-kingdom' in cat_lower or 'bahmani' in fl:
        if 'architecture' in fl or 'art' in fl:
            if is_hindi:
                return [
                    {"label": "वास्तुकला की विशेषताएं", "type": "branch", "date": "इंडो-फारसी शैली", "children": [
                        {"label": "सैन्य और धार्मिक वास्तुकला में स्थानीय शैली के साथ तुर्की और फारसी तत्वों का अनूठा मिश्रण", "type": "leaf"},
                        {"label": "नक्काशीदार प्लास्टर, बड़े गुंबद, पतले मीनार और अर्ध-वृत्ताकार मेहराबों का प्रमुख उपयोग", "type": "leaf"}
                    ]},
                    {"label": "प्रमुख स्मारक", "type": "branch", "date": "गुलबर्गा और बीदर", "children": [
                        {"label": "गुलबर्गा किला और जामा मस्जिद (छत पर 63 छोटे गुंबद और खुला आंगन न होना इसकी विशेषता है)", "type": "leaf"},
                        {"label": "बीदर का किला और रंगीन महल; हजरत गेसू दराज दरगाह का गुंबददार मकबरा", "type": "leaf"},
                        {"label": "महमूद गवां का मदरसा (बीदर में): तीन मंजिला भवन, विशाल मीनार और चमकीली फारसी टाइलें", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Architectural Features", "type": "branch", "date": "Indo-Persian Style", "children": [
                        {"label": "Unique synthesis of local Deccani styles with Turkish and Persian military/religious designs", "type": "leaf"},
                        {"label": "Characteristic use of plasterwork, circular domes, slender minarets, and stilted arches", "type": "leaf"}
                    ]},
                    {"label": "Major Monuments", "type": "branch", "date": "Gulbarga & Bidar", "children": [
                        {"label": "Gulbarga Fort & Jama Masjid (unique for having 63 small domes and no open courtyard)", "type": "leaf"},
                        {"label": "Bidar Fort & Rangin Mahal; domed mausoleum of Sufi saint Hazrat Gesu Daraz", "type": "leaf"},
                        {"label": "Mahmud Gawan's Madrasa at Bidar: 3-storeyed college with grand minarets and glazed Persian tiles", "type": "leaf"}
                    ]}
                ]
        elif 'successor' in fl or 'ahmednagar' in fl or 'bijapur' in fl or 'golconda' in fl or 'berar' in fl or 'bidar' in fl:
            if is_hindi:
                return [
                    {"label": "साम्राज्य का विघटन", "type": "branch", "date": "16वीं शताब्दी", "children": [
                        {"label": "महमूद गवां के पतन के बाद बहमनी साम्राज्य पांच स्वतंत्र दक्कन सल्तनतों में टूट गया", "type": "leaf"},
                        {"label": "बीजापुर (आदिल शाही), गोलकुंडा (कुतुब शाही), अहमदनगर (निजाम शाही), बीदर (बरीद शाही), बरार (इमाद शाही)", "type": "leaf"}
                    ]},
                    {"label": "राजनयिक संबंध और कला", "type": "branch", "date": "ऐतिहासिक संघर्ष", "children": [
                        {"label": "तालीकोटा का युद्ध (1565): बरार को छोड़कर चार सल्तनतों ने विजयनगर को हराने के लिए गठबंधन बनाया", "type": "leaf"},
                        {"label": "बीजापुर में गोल गुंबद (विश्व का सबसे बड़ा गुंबद कक्ष) और गोलकुंडा में चारमीनार का निर्माण", "type": "leaf"},
                        {"label": "बाद में शाहजहाँ और औरंगजेब द्वारा इन दक्कन सल्तनतों को मुगलों में मिलाया गया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Disintegration of Empire", "type": "branch", "date": "16th Century", "children": [
                        {"label": "Bahmani kingdom broke into five successor states due to court factions after Gawan's death", "type": "leaf"},
                        {"label": "Bijapur (Adil Shahi), Golconda (Qutb Shahi), Ahmednagar (Nizam Shahi), Bidar (Barid Shahi), Berar (Imad Shahi)", "type": "leaf"}
                    ]},
                    {"label": "Military & Artistic Legacy", "type": "branch", "date": "Sultanates", "children": [
                        {"label": "Battle of Talikota (1565): Alliance of Deccan states (excluding Berar) defeated Vijayanagar", "type": "leaf"},
                        {"label": "Architectural marvels: Gol Gumbaz (Bijapur, whispering gallery) and Charminar (Golconda)", "type": "leaf"},
                        {"label": "Eventually absorbed into the Mughal Empire during Shah Jahan and Aurangzeb's reigns", "type": "leaf"}
                    ]}
                ]
        else:
            if is_hindi:
                return [
                    {"label": "उत्पत्ति और संस्थापक", "type": "branch", "date": "1347 ईस्वी", "children": [
                        {"label": "अलाउद्दीन हसन बहमन शाह (हसन गंगू) ने मोहम्मद बिन तुगलक के खिलाफ विद्रोह कर स्थापना की", "type": "leaf"},
                        {"label": "राजधानी: आरंभ में गुलबर्गा (अहसराबाद) थी; बाद में 1424 में अहमद शाह वली द्वारा बीदर स्थानांतरित", "type": "leaf"}
                    ]},
                    {"label": "प्रशासनिक संरचना", "type": "branch", "date": "तरफदारी प्रणाली", "children": [
                        {"label": "साम्राज्य को 'तरफ' (प्रांतों) में विभाजित किया गया था, जिनका शासन तरफदारों (गवर्नरों) द्वारा किया जाता था", "type": "leaf"},
                        {"label": "अफाकी (विदेशी रईसों) बनाम दक्कनी (स्थानीय रईसों) की आपसी कलह ने शासन को खोखला किया", "type": "leaf"}
                    ]},
                    {"label": "महमूद गवां के सुधार", "type": "branch", "date": "प्रधानमंत्री (1463-81)", "children": [
                        {"label": "भू-राजस्व सुधार: भूमि का मापन कराया, कर का निर्धारण किया और भ्रष्टाचार को नियंत्रित किया", "type": "leaf"},
                        {"label": "सैन्य सुधार: तरफदारों की ताकत कम करने के लिए सैन्य बलों पर केंद्रीय नियंत्रण स्थापित किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Origins & Founder", "type": "branch", "date": "1347 AD", "children": [
                        {"label": "Alauddin Bahman Shah (Hasan Gangu) founded the dynasty after revolting against Delhi Sultanate", "type": "leaf"},
                        {"label": "Capital: Gulbarga initially; shifted to Bidar by Ahmad Shah Wali in 1424 AD", "type": "leaf"}
                    ]},
                    {"label": "Administration & Politics", "type": "branch", "date": "Tarafs", "children": [
                        {"label": "Kingdom divided into provinces (Tarafs) governed by powerful military chiefs (Tarafdars)", "type": "leaf"},
                        {"label": "Bitter court rivalry between Afaqis (foreign nobles) and Deccanis (local nobles) weakened stability", "type": "leaf"}
                    ]},
                    {"label": "Mahmud Gawan's Reforms", "type": "branch", "date": "Wazir (1463-81)", "children": [
                        {"label": "Land revenue reforms: Measured fields, fixed state share, and paid officials in cash or jagirs", "type": "leaf"},
                        {"label": "Military: Curtailed power of Tarafdars; introduced gunpowder in artillery battles", "type": "leaf"}
                    ]}
                ]

    # =========================================================================
    # D. BHAKTI & SUFI MOVEMENTS
    # =========================================================================
    elif 'bhakti-and-sufi-movements' in cat_lower or 'bhakti' in fl or 'sufi' in fl or 'vaishnavism' in fl:
        
        # 1. Shankaracharya
        if 'shankaracharya' in fl:
            if is_hindi:
                return [
                    {"label": "अद्वैत दर्शन", "type": "branch", "date": "9वीं शताब्दी", "children": [
                        {"label": "पूर्ण अद्वैतवाद: ब्रह्म ही एकमात्र सत्य है और यह जगत मिथ्या (माया) है", "type": "leaf"},
                        {"label": "आत्मा और ब्रह्म एक ही हैं; मोक्ष की प्राप्ति ज्ञान मार्ग (ज्ञान योग) के माध्यम से होती है", "type": "leaf"},
                        {"label": "प्रस्थानत्रयी (उपनिषदों, भगवद्गीता और ब्रह्मसूत्र) पर भाष्यों (टीकाओं) की रचना की", "type": "leaf"}
                    ]},
                    {"label": "मठ और संगठन", "type": "branch", "date": "चार मठ", "children": [
                        {"label": "चार दिशाओं में मठ स्थापित किए: शृंगेरी (दक्षिण), Puri (पूर्व), द्वारका (पश्चिम), बद्रीनाथ (उत्तर)", "type": "leaf"},
                        {"label": "षण्मत पूजा प्रणाली का संश्लेषण किया, जिससे शैव, वैष्णव, शाक्त आदि संप्रदायों का समन्वय हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Advaita Vedanta Philosophy", "type": "branch", "date": "9th Century AD", "children": [
                        {"label": "Absolute monism: Brahman is the sole reality; the material world is an illusion (Maya)", "type": "leaf"},
                        {"label": "Atman is identical to Brahman; liberation (Moksha) achieved through Jnana (knowledge)", "type": "leaf"},
                        {"label": "Wrote monumental commentaries (Bhashyas) on Upanishads, Bhagavad Gita, and Brahma Sutras", "type": "leaf"}
                    ]},
                    {"label": "Mathas & Integration", "type": "branch", "date": "Monastic Order", "children": [
                        {"label": "Established 4 monastic centers: Sringeri (South), Puri (East), Dwarka (West), Badrinath (North)", "type": "leaf"},
                        {"label": "Synthesized Shanmata worship, consolidating Shaivism, Vaishnavism, Shaktism, etc.", "type": "leaf"}
                    ]}
                ]

        # 2. Ramanujacharya
        elif 'ramanujacharya' in fl:
            if is_hindi:
                return [
                    {"label": "विशिष्टाद्वैत दर्शन", "type": "branch", "date": "11-12वीं शताब्दी", "children": [
                        {"label": "विशिष्ट अद्वैतवाद: ब्रह्म सर्वोच्च है, लेकिन जीव (चित) और जगत (अचित) उसके वास्तविक अंग हैं", "type": "leaf"},
                        {"label": "विष्णु/नारायण के प्रति भक्ति (प्रपत्ति) ही मोक्ष का सर्वोच्च मार्ग है", "type": "leaf"},
                        {"label": "तमिल प्रबंधम और उपनिषदों के बीच समन्वय स्थापित करने के लिए 'श्रीभाष्य' की रचना की", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक सुधार", "type": "branch", "date": "धार्मिक समानता", "children": [
                        {"label": "वंचित समुदायों (तिरुक्कुलत्तार) के लिए मंदिर प्रवेश की अनुमति दी; आध्यात्मिक समानता का उपदेश दिया", "type": "leaf"},
                        {"label": "वैष्णव भक्ति को उत्तर भारत में फैलाया, जिससे रामानंद और उनके शिष्य प्रभावित हुए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Vishishtadvaita Philosophy", "type": "branch", "date": "11th-12th Century AD", "children": [
                        {"label": "Qualified monism: Brahman is supreme, but individual souls (chit) and matter (achit) are real parts", "type": "leaf"},
                        {"label": "Devotion (Bhakti) to Vishnu/Narayana is the path to salvation (Moksha)", "type": "leaf"},
                        {"label": "Wrote Sri Bhashya to reconcile Upanishads with Tamil Bhakti hymns (Alvar Pasurams)", "type": "leaf"}
                    ]},
                    {"label": "Social Reforms", "type": "branch", "date": "Spiritual Equality", "children": [
                        {"label": "Opened temple entry to marginalized sections (Thirukulattar); preached equality in devotion", "type": "leaf"},
                        {"label": "Brought Vaishnavism to common folk, serving as the bridge to North Indian Bhakti", "type": "leaf"}
                    ]}
                ]

        # 3. Madhvacharya
        elif 'madhvacharya' in fl:
            if is_hindi:
                return [
                    {"label": "द्वैत दर्शन", "type": "branch", "date": "13वीं शताब्दी", "children": [
                        {"label": "द्वैत सिद्धांत: ब्रह्म (ईश्वर) और जीव (आत्मा) पूरी तरह से अलग और स्वतंत्र तत्व हैं; भौतिक जगत सत्य है", "type": "leaf"},
                        {"label": "विष्णु (नारायण) को ही परम स्वतंत्र और सर्वोच्च सत्ता माना, जबकि जीव और प्रकृति उन पर आश्रित हैं", "type": "leaf"}
                    ]},
                    {"label": "पंच-भेद सिद्धांत", "type": "branch", "date": "पाँच अंतर", "children": [
                        {"label": "ईश्वर-जीव, जीव-जीव, ईश्वर-जड़, जीव-जड़, और जड़-जड़ के बीच के शाश्वत अंतरों को प्रतिपादित किया", "type": "leaf"}
                    ]},
                    {"label": "संस्थागत विरासत", "type": "branch", "date": "मठ", "children": [
                        {"label": "उडुपी (कर्नाटक) में प्रसिद्ध कृष्ण मठ की स्थापना की और प्रचार के लिए अष्ट मठों का गठन किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Dvaita Philosophy (Dualism)", "type": "branch", "date": "13th Century AD", "children": [
                        {"label": "Dvaita Vedanta: Absolute distinction between Brahman (God) and Atman (soul); the physical world is a real reality", "type": "leaf"},
                        {"label": "Proclaimed Vishnu (Narayana) as the supreme, independent deity, with souls and matter being dependent", "type": "leaf"}
                    ]},
                    {"label": "Pancha-Bheda Stance", "type": "branch", "date": "Five Differences", "children": [
                        {"label": "Propounded five eternal differences: God-soul, soul-soul, God-matter, soul-matter, and matter-matter", "type": "leaf"}
                    ]},
                    {"label": "Institutional Legacy", "type": "branch", "date": "Udupi Matha", "children": [
                        {"label": "Established the Krishna Matha at Udupi and the Ashta Mathas (eight monasteries) to train scholars", "type": "leaf"}
                    ]}
                ]

        # 4. Nimbark
        elif 'nimbark' in fl:
            if is_hindi:
                return [
                    {"label": "द्वैताद्वैत दर्शन", "type": "branch", "date": "12वीं शताब्दी", "children": [
                        {"label": "द्वैताद्वैतवाद (भेदाभेद): जीव और जगत ईश्वर से भिन्न भी हैं (अंश होने के नाते) और अभिन्न भी (आश्रित होने के नाते)", "type": "leaf"}
                    ]},
                    {"label": "राधा-कृष्ण भक्ति", "type": "branch", "date": "सनक संप्रदाय", "children": [
                        {"label": "सर्वप्रथम राधा और कृष्ण की युगल उपासना को मुख्यधारा में लाए; सनक संप्रदाय की स्थापना की", "type": "leaf"}
                    ]},
                    {"label": "दार्शनिक रचनाएँ", "type": "branch", "date": "साहित्य", "children": [
                        {"label": "ब्रह्मसूत्र पर संक्षिप्त भाष्यात्मक ग्रंथ 'वेदांत पारिजात सौरभ' की रचना की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Dvaitadvaita (Bhedabheda)", "type": "branch", "date": "12th Century AD", "children": [
                        {"label": "Dualistic Non-dualism: The soul and world are distinct from God but also identical as parts of Him", "type": "leaf"}
                    ]},
                    {"label": "Radha-Krishna Devotion", "type": "branch", "date": "Sect", "children": [
                        {"label": "First major reformer to emphasize the sweet conjugal devotion of Radha-Krishna; set up Sanak Sampradaya", "type": "leaf"}
                    ]},
                    {"label": "Theological Commentary", "type": "branch", "date": "Literature", "children": [
                        {"label": "Authored the Vedanta Parijata Saurabha, a key commentary on the Brahma Sutras from Bhedabheda view", "type": "leaf"}
                    ]}
                ]

        # 5. Nathpanthis / Siddhas / Yogis
        elif 'nathpanthis' in fl or 'siddhas' in fl or 'yogis' in fl:
            if is_hindi:
                return [
                    {"label": "नाथपंथ शिक्षाएं", "type": "branch", "date": "हठयोग", "children": [
                        {"label": "गोरखनाथ द्वारा लोकप्रिय; संसार के संन्यास और निराकार परम तत्व के ध्यान की वकालत की", "type": "leaf"},
                        {"label": "मन और शरीर के नियंत्रण के लिए हठयोग, प्राणायाम, आसन और गहन ध्यान पर बल दिया", "type": "leaf"},
                        {"label": "ब्राह्मणवादी ग्रंथों, कर्मकांडों और जाति प्रथा का कड़ा विरोध कर आम जनता में पैठ बनाई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Nathpanthi Teachings", "type": "branch", "date": "Hatha Yoga", "children": [
                        {"label": "Popularized by Gorakhnath; advocated renunciation of the world and devotion to the formless truth", "type": "leaf"},
                        {"label": "Stressed mind-body discipline through Hatha Yoga, breathing exercises (Pranayama), and meditation", "type": "leaf"},
                        {"label": "Rejected priestly orthodox rituals and caste hierarchies, attracting lower agrarian classes", "type": "leaf"}
                    ]}
                ]

        # 6. Kabir
        elif 'kabir' in fl:
            if is_hindi:
                return [
                    {"label": "शिक्षाएं और दर्शन", "type": "branch", "date": "निर्गुण संत", "children": [
                        {"label": "स्वामी रामानंद के शिष्य; निराकार, गैर-सांप्रदायिक परमेश्वर (राम/अल्लाह) की वकालत की", "type": "leaf"},
                        {"label": "जाति व्यवस्था, पुरोहित वर्ग, ग्रंथों की सर्वोच्चता और मूर्ति पूजा का पुरजोर विरोध किया", "type": "leaf"},
                        {"label": "बाहरी आडंबरों (तीर्थयात्रा, उपवास, नमाज, यज्ञ) की तीखी आलोचना की", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक विरासत", "type": "branch", "date": "बीजक", "children": [
                        {"label": "स्थानीय मिश्रित बोली (सधुक्कड़ी) में दोहों, साखियों और श्लोकों की रचना की", "type": "leaf"},
                        {"label": "शिक्षाएं 'बीजक' (रमैनी, सबद, साखी) में संकलित; कबीर पंथ संप्रदाय की स्थापना हुई", "type": "leaf"},
                        {"label": "सिखों के पवित्र ग्रंथ 'गुरु ग्रंथ साहिब' में इनके छंदों को प्रमुख स्थान प्राप्त है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Nirguna Teachings", "type": "branch", "date": "Formless Devotion", "children": [
                        {"label": "Disciple of Ramananda; advocated formless, non-sectarian Supreme God (referred as Ram/Allah)", "type": "leaf"},
                        {"label": "Denounced caste system, institutionalized priesthood, and scriptural authority", "type": "leaf"},
                        {"label": "Opposed idol worship, pilgrimages, and empty outward rituals in both Hinduism and Islam", "type": "leaf"}
                    ]},
                    {"label": "Literary Legacy", "type": "branch", "date": "The Bijak", "children": [
                        {"label": "Composed Dohas, Sakhis, and Shlokas in local dialects (Sadhukkarri)", "type": "leaf"},
                        {"label": "Teachings compiled in the Bijak (comprising Ramaini, Sabad, Sakhi) by his disciples", "type": "leaf"},
                        {"label": "A significant portion of his verses are preserved in the Guru Granth Sahib", "type": "leaf"}
                    ]}
                ]

        # 7. Nanak
        elif 'nanak' in fl:
            if is_hindi:
                return [
                    {"label": "सिख शिक्षाएं", "type": "branch", "date": "एकेश्वरवाद", "children": [
                        {"label": "इक ओंकार (एक ईश्वर) का उपदेश दिया जो निराकार (निरंकार), अकाल और सर्वव्यापी है", "type": "leaf"},
                        {"label": "जातिगत विभाजन, कर्मकांडों, संन्यास और पुरोहिती एकाधिकार को खारिज किया", "type": "leaf"},
                        {"label": "तीन स्तंभ: नाम जपना (ईश्वर स्मरण), कीरत करनी (ईमानदार काम), वंड छकना (साझा करना) पर बल", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक सुधार", "type": "branch", "date": "लंगर और संगत", "children": [
                        {"label": "लंगर (मुफ्त सामुदायिक रसोई) की स्थापना की जहाँ सभी बैठकर भोजन करते थे, जिससे जातिगत भेदभाव समाप्त हुआ", "type": "leaf"},
                        {"label": "संगत (सामूहिक प्रार्थना सभा) स्थापित की; गुरु अंगद को अपना उत्तराधिकारी घोषित किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sikh Teachings", "type": "branch", "date": "Monotheism", "children": [
                        {"label": "Preached Ik Onkar (One God) who is formless (Nirankar), timeless (Akal), and omnipresent", "type": "leaf"},
                        {"label": "Rejected caste divisions, ritualistic pilgrimages, asceticism, and scriptural monopoly", "type": "leaf"},
                        {"label": "Stressed three pillars: Naam Japna (remembering God), Kirat Karni (honest work), Vand Chhakna (sharing)", "type": "leaf"}
                    ]},
                    {"label": "Social Innovations", "type": "branch", "date": "Langar & Sangat", "children": [
                        {"label": "Langar: Free community kitchen where all sat together on the floor, breaking caste barriers", "type": "leaf"},
                        {"label": "Sangat: Congregational worship without distinction of status; nominated Guru Angad as successor", "type": "leaf"}
                    ]}
                ]

        # 8. Chaitanya
        elif 'chaitanya' in fl:
            if is_hindi:
                return [
                    {"label": "दर्शन और सिद्धांत", "type": "branch", "date": "अचिंत्य-भेदा-भेद", "children": [
                        {"label": "अचिंत्य-भेदा-भेद दर्शन: जीव और ईश्वर के बीच अकल्पनीय एकता और अंतर का प्रतिपादन किया", "type": "leaf"},
                        {"label": "कृष्ण के प्रति मधुरा भक्ति (राधा की भक्ति के मॉडल पर दांपत्य प्रेम) पर जोर दिया", "type": "leaf"}
                    ]},
                    {"label": "संकीर्तन आंदोलन", "type": "branch", "date": "सामूहिक गायन", "children": [
                        {"label": "संकीर्तन को लोकप्रिय बनाया: गलियों में पवित्र नामों (हरे कृष्ण महामंत्र) का सामूहिक गायन और नृत्य", "type": "leaf"},
                        {"label": "मुसलमानों (जैसे हरिदास) सहित सभी वर्गों का स्वागत करके भक्ति का लोकतंत्रीकरण किया", "type": "leaf"},
                        {"label": "छह गोस्वामियों को भेजकर वृंदावन को एक प्रमुख आध्यात्मिक केंद्र के रूप में फिर से स्थापित किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Philosophy", "type": "branch", "date": "Achintya-Bheda-Abheda", "children": [
                        {"label": "Advocated Achintya-Bheda-Abheda: Inconceivable simultaneous oneness and difference between soul & God", "type": "leaf"},
                        {"label": "Emphasized Madhura Bhakti (conjugal love for Krishna, modeled on Radha's devotion)", "type": "leaf"}
                    ]},
                    {"label": "Sankirtan Movement", "type": "branch", "date": "Congregational Dance", "children": [
                        {"label": "Popularized Sankirtan: Street singing and dancing of holy names (Hare Krishna Mahamantra)", "type": "leaf"},
                        {"label": "Democratized Bhakti by welcoming all classes, including Muslims (like Haridas)", "type": "leaf"},
                        {"label": "Rediscovered Vrindavan as a major spiritual center, sending the Six Goswamis to revive it", "type": "leaf"}
                    ]}
                ]

        # 9. Dadu Dayal
        elif 'dadu-dayal' in fl:
            if is_hindi:
                return [
                    {"label": "निर्गुण दर्शन", "type": "branch", "date": "16वीं शताब्दी", "children": [
                        {"label": "कबीर के विचारों से प्रभावित निर्गुण संत; राजस्थान में दादू पंथ की स्थापना की", "type": "leaf"},
                        {"label": "जाति, ग्रंथों और मूर्तिपूजा को खारिज किया; सरल लोक भाषा में उपदेश दिए", "type": "leaf"}
                    ]},
                    {"label": "दादू पंथ और निपख", "type": "branch", "date": "गैर-सांप्रदायिक", "children": [
                        {"label": "निपख (गैर-सांप्रदायिक) मार्ग का समर्थन किया, जो हिंदू और मुस्लिम दोनों रूढ़ियों से ऊपर उठने पर बल देता है", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक योगदान", "type": "branch", "date": "वाणी", "children": [
                        {"label": "इनकी शिक्षाएं 'दादू दयाल की बानी' में संकलित हैं; सरल ढुंढाड़ी (राजस्थानी) भाषा में रचनाएं कीं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Nirguna Philosophy", "type": "branch", "date": "16th Century", "children": [
                        {"label": "Nirguna reformer heavily influenced by Kabir; established the Dadu Panth in Rajasthan", "type": "leaf"},
                        {"label": "Rejected temples, formal scriptures, and caste divisions, preaching to common folk", "type": "leaf"}
                    ]},
                    {"label": "Dadu Panth & Nipakh", "type": "branch", "date": "Non-sectarian", "children": [
                        {"label": "Advocated the Nipakh (non-sectarian) path, advising followers to stay neutral from Hindu/Muslim divisions", "type": "leaf"}
                    ]},
                    {"label": "Literary Works", "type": "branch", "date": "Bani", "children": [
                        {"label": "Teachings compiled in Dadu Dayal ki Bani; composed in local Dhundhari (Rajasthani) dialect", "type": "leaf"}
                    ]}
                ]

        # 10. Eknath
        elif 'eknath' in fl:
            if is_hindi:
                return [
                    {"label": "साहित्यिक योगदान", "type": "branch", "date": "मराठी कृतियाँ", "children": [
                        {"label": "भागवत पुराण के 11वें अध्याय का मराठी में अनुवाद किया (भागवत एकादशी); भावार्थ रामायण की रचना की", "type": "leaf"},
                        {"label": "भजनों (भारुड़) के माध्यम से नैतिक और सामाजिक उपदेश दिया", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक सुधार", "type": "branch", "date": "समानता", "children": [
                        {"label": "गृहस्थ जीवन को आध्यात्मिक मार्ग के अनुकूल बताया; जातिगत भेदभाव का घोर विरोध किया", "type": "leaf"},
                        {"label": "दलितों और शोषितों के साथ भोजन करके सामाजिक समानता का अनुकरणीय उदाहरण प्रस्तुत किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Literary Contributions", "type": "branch", "date": "Marathi Texts", "children": [
                        {"label": "Translated the 11th book of Bhagavata Purana into Marathi; composed the famous Bhavartha Ramayana", "type": "leaf"},
                        {"label": "Wrote Bharud folk songs (metaphorical dramas) to convey moral and social lessons to masses", "type": "leaf"}
                    ]},
                    {"label": "Socio-Religious Reforms", "type": "branch", "date": "Social Work", "children": [
                        {"label": "Preached householder Bhakti, showing that family life is fully compatible with realization", "type": "leaf"},
                        {"label": "Actively opposed caste prejudices; dined with lower classes to challenge untouchability", "type": "leaf"}
                    ]}
                ]

        # 11. Tukaram
        elif 'tukaram' in fl:
            if is_hindi:
                return [
                    {"label": "वारकरी संप्रदाय", "type": "branch", "date": "17वीं शताब्दी", "children": [
                        {"label": "पंढरपुर के भगवान विठोबा (विष्णु का रूप) के प्रति समर्पित; मराठा शासक शिवाजी के समकालीन", "type": "leaf"},
                        {"label": "मराठी में हजारों 'अभंग' (भक्ति छंद) लिखे, जिनमें सामाजिक पाखंड पर तीखा प्रहार किया", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक सुधार", "type": "branch", "date": "समानता", "children": [
                        {"label": "कर्मकांड, पुरोहिती एकाधिकार और जातिगत असमानता का मुखर विरोध किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Varkari Devotion", "type": "branch", "date": "17th Century", "children": [
                        {"label": "Core leader of the Varkari sect centered on Lord Vitthala of Pandharpur; contemporary of Shivaji", "type": "leaf"},
                        {"label": "Composed thousands of Marathi devotional hymns called 'Abhangs' praising Vitthala", "type": "leaf"}
                    ]},
                    {"label": "Socio-Religious Teachings", "type": "branch", "date": "Social Message", "children": [
                        {"label": "Opposed formal rituals, institutional priesthood monopoly, and untouchability in society", "type": "leaf"}
                    ]}
                ]

        # 12. Vallabhacharya
        elif 'vallabhacharya' in fl:
            if is_hindi:
                return [
                    {"label": "शुद्धाद्वैत दर्शन", "type": "branch", "date": "15-16वीं शताब्दी", "children": [
                        {"label": "शुद्धाद्वैतवाद (शुद्ध अद्वैत): जीव और जगत ब्रह्म के वास्तविक अंश हैं; माया का प्रभाव नहीं है", "type": "leaf"},
                        {"label": "वल्लभाचार्य ने संस्कृत में सुबोधिनी और सिद्धांत रहस्य ग्रंथों की रचना की", "type": "leaf"}
                    ]},
                    {"label": "पुष्टि मार्ग", "type": "branch", "date": "अनुग्रह", "children": [
                        {"label": "पुष्टि मार्ग (ईश्वरीय अनुग्रह का मार्ग) की स्थापना की; कृष्ण के बाल रूप (श्रीनाथजी) की पूजा पर बल दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Shuddhadvaita Philosophy", "type": "branch", "date": "15th-16th Century", "children": [
                        {"label": "Shuddhadvaita (Pure Non-dualism): Soul and world are real parts of Brahman, without Maya's illusion", "type": "leaf"},
                        {"label": "Composed major philosophical works in Sanskrit including Subodhini and philosophical treatises", "type": "leaf"}
                    ]},
                    {"label": "Pushti Marg Sect", "type": "branch", "date": "Divine Grace", "children": [
                        {"label": "Founded the Pushti Marg (Path of Divine Grace), focusing on worship of child Krishna as Shrinathji", "type": "leaf"}
                    ]}
                ]

        # 13. Mirabai
        elif 'meerabai' in fl or 'mirabai' in fl:
            if is_hindi:
                return [
                    {"label": "सगुण कृष्ण भक्ति", "type": "branch", "date": "16वीं शताब्दी", "children": [
                        {"label": "गिरधर गोपाल (कृष्ण) के प्रति समर्पित भक्ति (माधुर्य भाव); स्वयं को कृष्ण की अर्धांगिनी माना", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक विद्रोह", "type": "branch", "date": "विरोध", "children": [
                        {"label": "मेवाड़ राजघराने के सुख-सुविधाओं और सती होने जैसी सामाजिक रूढ़ियों को मानने से इनकार किया", "type": "leaf"},
                        {"label": "बिना किसी जातिगत भेदभाव के संत रैदास (चर्मकार) को अपना गुरु स्वीकार किया", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक धरोहर", "type": "branch", "date": "पदावली", "children": [
                        {"label": "राजस्थानी और ब्रज भाषा में लिखे गए भजनों (पदावली) का संकलन भारत भर में गाया जाता है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Saguna Krishna Devotion", "type": "branch", "date": "16th Century", "children": [
                        {"label": "Deep, personal love for Lord Krishna (Madhurya Bhava), worshipping Him as her divine consort", "type": "leaf"}
                    ]},
                    {"label": "Social Rebellion & Legacy", "type": "branch", "date": "Rebellion", "children": [
                        {"label": "Rejected Mewar royal luxury, court protocols, and strictly defied the custom of Sati", "type": "leaf"},
                        {"label": "Accepted the lower-caste saint Raidas (a tanner) as her spiritual guru, challenging caste hierarchies", "type": "leaf"}
                    ]},
                    {"label": "Padavali Literature", "type": "branch", "date": "Hymns", "children": [
                        {"label": "Composed thousands of sweet bhajans in Rajasthani and Braj dialects, compiled in the Padavali", "type": "leaf"}
                    ]}
                ]

        # 14. Namdev
        elif 'namdev' in fl:
            if is_hindi:
                return [
                    {"label": "वारकरी आंदोलन के अग्रदूत", "type": "branch", "date": "13-14वीं शताब्दी", "children": [
                        {"label": "पेशे से दर्जी थे; पहले विठोबा के सगुण भक्त थे, बाद में निराकार निर्गुण ब्रह्म के उपासक बने", "type": "leaf"},
                        {"label": "मराठी में अभंग लिखे और भारत भर की यात्रा की, विशेष रूप से पंजाब में वर्षों रहे", "type": "leaf"},
                        {"label": "इनके कई हिंदी भजनों को सिखों के पवित्र ग्रंथ गुरु ग्रंथ साहिब में शामिल किया गया है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Varkari Pioneer", "type": "branch", "date": "13th-14th Century", "children": [
                        {"label": "Tailor by caste; transitioned from a Saguna Vitthala worshiper to a Nirguna (formless) philosopher", "type": "leaf"},
                        {"label": "Composed Marathi Abhangs and traveled extensively to Punjab, preaching communal unity", "type": "leaf"},
                        {"label": "More than 60 of his Hindi hymns are compiled and honored in the Guru Granth Sahib", "type": "leaf"}
                    ]}
                ]

        # 15. Ramdas
        elif 'ramdas' in fl:
            if is_hindi:
                return [
                    {"label": "धारकरी संप्रदाय", "type": "branch", "date": "17वीं शताब्दी", "children": [
                        {"label": "मराठी ग्रंथ 'दासबोध' की रचना की, जिसमें व्यावहारिक और आध्यात्मिक जीवन का समन्वय है", "type": "leaf"},
                        {"label": "शिवाजी महाराज के आध्यात्मिक गुरु माने जाते हैं; समाज में शारीरिक शक्ति और संगठन पर जोर दिया", "type": "leaf"},
                        {"label": "भारत भर में हनुमान (मारुति) मंदिरों और मठों की स्थापना कर चेतना जगाई", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Dharakari Sect & Dasbodh", "type": "branch", "date": "17th Century", "children": [
                        {"label": "Authored the Marathi text 'Dasbodh', offering guidance on both spiritual realization and practical life", "type": "leaf"},
                        {"label": "Spiritual advisor of Shivaji Maharaj; emphasized physical vigor, organization, and social duty", "type": "leaf"},
                        {"label": "Established a network of Maruti (Hanuman) temples to foster physical culture and unity", "type": "leaf"}
                    ]}
                ]

        # 16. Shankardeva
        elif 'shankardeva' in fl:
            if is_hindi:
                return [
                    {"label": "एकशरण धर्म", "type": "branch", "date": "15-16वीं शताब्दी", "children": [
                        {"label": "असम में वैष्णव सुधार आंदोलन शुरू किया; केवल भगवान कृष्ण की भक्ति (एकशरण धर्म) का प्रचार किया", "type": "leaf"},
                        {"label": "सत्र (मठ) और नामघर (सामूहिक प्रार्थना हॉल) की स्थापना की, जो असमिया समाज की रीढ़ बने", "type": "leaf"},
                        {"label": "शास्त्रीय नृत्य 'सत्रिया' और अंकिया नाट (नाटक) का विकास कर कलात्मक पुनर्जागरण किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Ekasarana Dharma", "type": "branch", "date": "Assam Reformer", "children": [
                        {"label": "Led the Vaishnavite renaissance in Assam, preaching absolute devotion to Lord Krishna (Ekasarana)", "type": "leaf"},
                        {"label": "Created Satras (monasteries) and Namghars (prayer halls) to promote social equality and education", "type": "leaf"},
                        {"label": "Developed the classical Sattriya dance drama and Bhaona theatre to convey scriptures", "type": "leaf"}
                    ]}
                ]

        # 17. Surdas
        elif 'surdas' in fl:
            if is_hindi:
                return [
                    {"label": "पुष्टि मार्ग शिष्य", "type": "branch", "date": "16वीं शताब्दी", "children": [
                        {"label": "वल्लभाचार्य के प्रमुख शिष्यों में से एक; ब्रज भाषा में भगवान कृष्ण की भक्ति पर बल दिया", "type": "leaf"}
                    ]},
                    {"label": "वात्सल्य और श्रृंगार रस", "type": "branch", "date": "भक्ति रस", "children": [
                        {"label": "कृष्ण की बाल लीलाओं (वात्सल्य रस) और गोपियों के प्रेम (श्रृंगार रस) का अनुपम वर्णन किया", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक कृतियां और अष्टछाप", "type": "branch", "date": "साहित्य", "children": [
                        {"label": "महान ग्रंथ 'सूरसागर', 'सूरसारावली' और 'साहित्य लहरी' लिखे; अष्टछाप (आठ प्रसिद्ध कवि) समूह के प्रमुख थे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Pushti Marg Devotion", "type": "branch", "date": "16th Century", "children": [
                        {"label": "Prominent disciple of Vallabhacharya; focused on intense devotional path to Lord Krishna in Braj", "type": "leaf"}
                    ]},
                    {"label": "Vatsalya & Shringar Ras", "type": "branch", "date": "Themes", "children": [
                        {"label": "Celebrated for portraying child Krishna's playfulness (Vatsalya Bhava) and separation of Gopis (Viraha Shringar)", "type": "leaf"}
                    ]},
                    {"label": "Ashtachhap Guild & Works", "type": "branch", "date": "Literature", "children": [
                        {"label": "Authored the Sursagar, Sursaravali, and Sahitya Lahiri; led the Ashtachhap (eight great Braj poets)", "type": "leaf"}
                    ]}
                ]

        # 18. Purandar Das
        elif 'purandar' in fl:
            if is_hindi:
                return [
                    {"label": "कर्नाटक संगीत के पितामह", "type": "branch", "date": "15-16वीं शताब्दी", "children": [
                        {"label": "हरिदास संप्रदाय के प्रमुख संत; कर्नाटक संगीत के बुनियादी नियमों (स्वर) को व्यवस्थित किया", "type": "leaf"},
                        {"label": "कन्नड़ भाषा में हजारों कीर्तनों (पुरंदर विट्ठल छाप के साथ) की रचना की", "type": "leaf"},
                        {"label": "अपनी रचनाओं में सामाजिक बुराइयों, दिखावटी पूजा और जाति प्रथा पर करारा प्रहार किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Pitamaha of Carnatic Music", "type": "branch", "date": "15th-16th Century", "children": [
                        {"label": "Haridas saint; standardized the Carnatic music training lessons (Mayamalavagowla raga)", "type": "leaf"},
                        {"label": "Composed thousands of Kannada Keerthanas praising Lord Vitthala under signature 'Purandara Vittala'", "type": "leaf"},
                        {"label": "Attacked ritualistic hypocrisy, greed, and untouchability through popular song verses", "type": "leaf"}
                    ]}
                ]

        # 19. Ramananda
        elif 'ramananda' in fl:
            if is_hindi:
                return [
                    {"label": "भक्ति का उत्तर भारत में प्रसार", "type": "branch", "date": "14-15वीं शताब्दी", "children": [
                        {"label": "दक्षिण की वैष्णव भक्ति परंपरा को उत्तर भारत में लाने वाले पुल बने; संस्कृत के स्थान पर हिंदी में उपदेश दिए", "type": "leaf"},
                        {"label": "जाति बंधन तोड़े: कबीर (जुलाहा), रैदास (चर्मकार), सेना (नाई) सहित सभी वर्गों को शिष्य बनाया", "type": "leaf"},
                        {"label": "विष्णु के अवतार मर्यादा पुरुषोत्तम भगवान राम की भक्ति को लोकप्रिय बनाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Bridge to North India", "type": "branch", "date": "14th-15th Century", "children": [
                        {"label": "Brought Vaishnavite Bhakti from South India (Ramanuja school) to the North, preaching in Hindi", "type": "leaf"},
                        {"label": "Abolished caste barriers in discipleship, accepting Kabir (weaver), Raidas (tanner), and Sena (barber)", "type": "leaf"},
                        {"label": "Popularized the worship of Lord Rama as the supreme manifestation of God", "type": "leaf"}
                    ]}
                ]

        # 20. Haridas
        elif 'haridas' in fl:
            if is_hindi:
                return [
                    {"label": "स्वामी हरिदास और संगीत", "type": "branch", "date": "16वीं शताब्दी", "children": [
                        {"label": "अकबर के दरबारी तानसेन और बैजू बावरा के संगीत गुरु; वृंदावन में निधिवन की स्थापना की", "type": "leaf"},
                        {"label": "ध्रुपद गायकी के महान प्रणेता; संगीत को ईश्वर प्राप्ति का सर्वोच्च साधन (नाद योग) माना", "type": "leaf"},
                        {"label": "श्री बांके बिहारी लाल की कुंज-विहार (निकुंज) पद्धति के भक्ति रस की स्थापना की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Swami Haridas & Dhrupad Music", "type": "branch", "date": "16th Century", "children": [
                        {"label": "Standardized spiritual music; guru of legendary court musicians Tansen and Baiju Bawra", "type": "leaf"},
                        {"label": "Pioneered Dhrupad singing style; considered music as Nada Yoga (spiritual union through sound)", "type": "leaf"},
                        {"label": "Established the Haridasi sampradaya centered on worship of Lord Banke Bihari in Vrindavan", "type": "leaf"}
                    ]}
                ]

        # 21. Satnami / Ghasidas / Dhaneswar
        elif 'ghasidas' in fl or 'dhaneswar' in fl or 'satnami' in fl:
            if is_hindi:
                return [
                    {"label": "सतनामी आंदोलन", "type": "branch", "date": "छत्तीसगढ़", "children": [
                        {"label": "गुरु घासीदास ने मूर्तिपूजा और सामाजिक विषमता का विरोध कर सतनाम (सत्य नाम) की उपासना पर बल दिया", "type": "leaf"},
                        {"label": "दलितों और शोषितों के मानवाधिकारों, मद्यपान निषेध और मांस भक्षण निषेध का प्रचार किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Satnami Movement", "type": "branch", "date": "Chhattisgarh", "children": [
                        {"label": "Guru Ghasidas established the Satnami sect; rejected idol worship, caste, and preached the 'Satnam' (True Name)", "type": "leaf"},
                        {"label": "Fought for human rights of marginalized castes, promoted vegetarianism and teetotalism", "type": "leaf"}
                    ]}
                ]

        # 22. Literature
        elif 'associated-literature' in fl or 'literature' in fl:
            if is_hindi:
                return [
                    {"label": "लोक भाषा भक्ति साहित्य", "type": "branch", "date": "क्षेत्रीय भाषाएं", "children": [
                        {"label": "संस्कृत के बजाय क्षेत्रीय भाषाओं में रचना: तमिल (तेवरम), हिंदी (बीजक, रामचरितमानस), बंगाली, मराठी", "type": "leaf"},
                        {"label": "सूरदास की सूरसागर, तुलसीदास की रामचरितमानस (अवधी में), मीराबाई की राजस्थानी पदावली", "type": "leaf"},
                        {"label": "मराठी में ज्ञानेश्वरी (ज्ञानेश्वर) और मराठी अभंग (तुकाराम और नामदेव); कन्नड़ में पुरंदर दास", "type": "leaf"}
                    ]},
                    {"label": "आव्याख्यान सशक्तिकरण", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "धार्मिक ग्रंथों में सीधे भागीदारी देकर वंचित जातियों और महिलाओं को सशक्त बनाया", "type": "leaf"},
                        {"label": "क्षेत्रीय भारतीय भाषाओं के विकास, व्याकरणिक स्थिरीकरण और शब्दकोश निर्माण में मदद मिली", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Vernacular Literature", "type": "branch", "date": "Regional Languages", "children": [
                        {"label": "Bypassed Sanskrit; wrote in regional languages: Tamil (Tevaram), Hindi (Bijak, Awadhi), Marathi, Kannada", "type": "leaf"},
                        {"label": "Tulsidas's Ramacharitamanas (Awadhi), Surdas's Sursagar (Braj), and Mirabai's Padavali (Rajasthani)", "type": "leaf"},
                        {"label": "Jnanadeva's Jnanesvari and Tukaram's Abhangs in Marathi; Purandara Dasa in Kannada", "type": "leaf"}
                    ]},
                    {"label": "Socio-Literary Impact", "type": "branch", "date": "Spiritual Empowerment", "children": [
                        {"label": "Empowered marginalized castes and women by giving them direct voice in religious texts", "type": "leaf"},
                        {"label": "Stimulated the growth, grammar, and literary richness of modern Indian languages", "type": "leaf"}
                    ]}
                ]

        # 23. Causes
        elif 'causes-for-its-formation' in fl or 'causes-of-creation' in fl:
            if is_hindi:
                return [
                    {"label": "भक्ति आंदोलन के उदय के कारण", "type": "branch", "date": "उदय", "children": [
                        {"label": "ब्राह्मणवादी कर्मकांडों और जाति प्रथा की कठोरता के विरुद्ध जनसामान्य का आक्रोश", "type": "leaf"},
                        {"label": "इस्लाम के आगमन: सूफीवाद के बंधुत्व और समानता के विचारों ने भारतीय समाज को प्रभावित किया", "type": "leaf"},
                        {"label": "क्षेत्रीय भाषाओं का विकास: संस्कृत के कठिन ग्रंथों के स्थान पर आम बोलचाल में धर्म की व्याख्या", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Causes of Bhakti & Sufi Rise", "type": "branch", "date": "Origins", "children": [
                        {"label": "Reaction against Brahmanical ritual rigidity and oppressive caste exclusion", "type": "leaf"},
                        {"label": "Socio-religious impact of Islam, highlighting egalitarianism and personal devotion (Tasawwuf)", "type": "leaf"},
                        {"label": "Rise of vernacular languages, allowing common masses to understand spiritual texts directly", "type": "leaf"}
                    ]}
                ]

        # 24. Features
        elif 'features-of-the-movement' in fl or 'features' in fl:
            if is_hindi:
                return [
                    {"label": "भक्ति एवं सूफी आंदोलन के लक्षण", "type": "branch", "date": "लक्षण", "children": [
                        {"label": "ईश्वर के प्रति पूर्ण समर्पण (प्रपत्ति) और प्रेम; जाति, पंथ और लिंग भेद का पूर्ण परित्याग", "type": "leaf"},
                        {"label": "सरल और स्थानीय भाषाओं में उपदेश; कर्मकांडों और पुरोहित वर्ग की मध्यस्थता का विरोध", "type": "leaf"},
                        {"label": "सूफी लक्षण: पीर-मुरीद परंपरा, रूहानी संगीत (समा) और फना (अहंकार का विनाश) का सिद्धांत", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Core Features & Stages", "type": "branch", "date": "Features", "children": [
                        {"label": "Absolute surrender (Prapatti) and pure love for God, rejecting intermediary priests", "type": "leaf"},
                        {"label": "Universal brotherhood: Overrode caste hierarchies, gender taboos, and dry rituals", "type": "leaf"},
                        {"label": "Sufi stages: Tariqat (spiritual path), Marifat (gnosis), and Haqiqat (ultimate truth)", "type": "leaf"}
                    ]}
                ]

        # 25. Pir-Murid Tradition
        elif 'pir-murid' in fl:
            if is_hindi:
                return [
                    {"label": "पीर-मुरीद संबंध", "type": "branch", "date": "अध्यात्म", "children": [
                        {"label": "पीर (गुरु) और मुरीद (शिष्य) के बीच का गहरा रूहानी रिश्ता, जो पूर्ण आत्मसमर्पण पर आधारित था", "type": "leaf"}
                    ]},
                    {"label": "खानकाह (मठ)", "type": "branch", "date": "संगठन", "children": [
                        {"label": "खानकाह: वह आश्रम या मठ जहाँ पीर अपने शिष्यों के साथ रहते थे और लंगर का संचालन करते थे", "type": "leaf"}
                    ]},
                    {"label": "उत्तराधिकार (खिलाफत)", "type": "branch", "date": "खलीफा", "children": [
                        {"label": "पीर अपने सबसे योग्य शिष्य को खिलाफतनामा (अधिकार पत्र) सौंपकर अपना उत्तराधिकारी (खलीफा) नियुक्त करते थे", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Spiritual Relationship", "type": "branch", "date": "Asceticism", "children": [
                        {"label": "Pir (spiritual master) and Murid (disciple) relationship built on complete devotion to achieve union with God", "type": "leaf"}
                    ]},
                    {"label": "Khanqah Hospice", "type": "branch", "date": "Khanqah", "children": [
                        {"label": "The monastery/monastic center acting as the hub for travelers, community kitchens, and discourses", "type": "leaf"}
                    ]},
                    {"label": "Succession & Khilafat", "type": "branch", "date": "Khalifa", "children": [
                        {"label": "The transmission of lineage via a Khilafatnama (charter of authority) to the nominated Khalifa (successor)", "type": "leaf"}
                    ]}
                ]

        # 26. Use of Music
        elif 'use-of-music' in fl:
            if is_hindi:
                return [
                    {"label": "समा (रूहानी संगीत)", "type": "branch", "date": "समा", "children": [
                        {"label": "समा: ईश्वर प्राप्ति के लिए रूहानी संगीत गोष्ठियां; संगीत को ईश्वर के प्रति दीवानगी (हाल) उत्पन्न करने का साधन माना", "type": "leaf"},
                        {"label": "रूढ़िवादी शरिया निषेधों के बावजूद चिश्ती सिलसिले ने संगीत को मान्यता प्रदान की", "type": "leaf"}
                    ]},
                    {"label": "कव्वाली और वाद्य यंत्र", "type": "branch", "date": "अमीर खुसरो", "children": [
                        {"label": "अमीर खुसरो ने फारसी और भारतीय धुनों को मिलाकर कव्वाली शैली तथा सितार व तबला वाद्य यंत्रों को जन्म दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sama Assemblies", "type": "branch", "date": "Sama", "children": [
                        {"label": "Sama: Devotional music assemblies used to induce spiritual ecstasy (Hal) and bring union with God", "type": "leaf"},
                        {"label": "Supported strongly by the Chishti Silsilah, despite orthodox Islamic legalistic prohibitions on music", "type": "leaf"}
                    ]},
                    {"label": "Qawwali & Synthesis", "type": "branch", "date": "Amir Khusrau", "children": [
                        {"label": "Amir Khusrau synthesized Persian and Indian musical systems, pioneering Qawwali, Sitar, and Tabla", "type": "leaf"}
                    ]}
                ]

        # 27. Impact
        elif 'impact-of' in fl:
            if is_hindi:
                return [
                    {"label": "आंदोलन का प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "सामाजिक सुधार: जातिगत कठोरता कम हुई; हिंदू-मुस्लिम सांस्कृतिक समन्वय (गंगा-जमुनी तहजीब) बढ़ा", "type": "leaf"},
                        {"label": "साहित्य का स्वर्ण युग: क्षेत्रीय भाषाओं (हिंदी, बंगाली, पंजाबी, मराठी) का तीव्र विकास हुआ", "type": "leaf"},
                        {"label": "सिख धर्म और कबीर पंथ जैसे नए धार्मिक समाजों की स्थापना का आधार बना", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Impact of the Reform Movements", "type": "branch", "date": "Societal Impact", "children": [
                        {"label": "Social harmonization: Diluted rigid caste boundaries and fostered Indo-Muslim syncretic values", "type": "leaf"},
                        {"label": "Literary growth: Promoted vernacular tongues, leading to golden era of regional Indian dialects", "type": "leaf"},
                        {"label": "Gave rise to new religious organizations like Sikhism, Kabir Panth, and Satnamis", "type": "leaf"}
                    ]}
                ]

        # 28. Chishti Order
        elif 'chishti' in fl or 'chisti' in fl:
            if is_hindi:
                return [
                    {"label": "चिश्ती सिलसिला", "type": "branch", "date": "सूफी संप्रदाय", "children": [
                        {"label": "मोइनुद्दीन चिश्ती द्वारा भारत में स्थापित (अजमेर दरगाह, 12वीं शताब्दी); सबसे लोकप्रिय संप्रदाय", "type": "leaf"},
                        {"label": "प्रमुख संत: निजामुद्दीन औलिया (महबूब-ए-इलाही), फरीदुद्दीन गंजशकर (बाबा फरीद), सलीम चिश्ती", "type": "leaf"},
                        {"label": "प्राणायाम (योगिक श्वास व्यायाम) को अपनाया और आम जनता के करीब रहे", "type": "leaf"}
                    ]},
                    {"label": "मुख्य आचरण", "type": "branch", "date": "जीवन शैली", "children": [
                        {"label": "तपस्या और गरीबी: साधारण मिट्टी के घरों (खानकाह) में रहते थे; उपवास (फक्र) का अभ्यास करते थे", "type": "leaf"},
                        {"label": "राजनीतिक तटस्थता: राजकीय पदों और दरबारी राजनीति से दूर रहे, शाही उपहारों को अस्वीकार किया", "type": "leaf"},
                        {"label": "समा: ईश्वर के प्रति आध्यात्मिक परमानंद (हाल) प्राप्त करने के लिए संगीत गोष्ठियों का उपयोग किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Chishti Silsilah", "type": "branch", "date": "Ascetic Sufism", "children": [
                        {"label": "Founded in India by Moinuddin Chishti (Ajmer Dargah); most popular and widespread order", "type": "leaf"},
                        {"label": "Key saints: Nizamuddin Auliya (Mehboob-e-Ilahi), Baba Farid, Salim Chishti", "type": "leaf"},
                        {"label": "Adopted yogic breathing exercises (Pranayama) and spoke in local dialects to integrate", "type": "leaf"}
                    ]},
                    {"label": "Key Practices", "type": "branch", "date": "Chishti Rule", "children": [
                        {"label": "Austerity: Lived in simple mud houses (Khanqahs); practiced voluntary poverty (Faqr)", "type": "leaf"},
                        {"label": "Political Aloofness: Stayed strictly away from state jobs and court politics, rejecting royal gifts", "type": "leaf"},
                        {"label": "Sama: Used devotional music (Qawwali) to attain a state of spiritual ecstasy (Hal)", "type": "leaf"}
                    ]}
                ]

        # 29. Suhrawardi Order
        elif 'suhrawardi' in fl:
            if is_hindi:
                return [
                    {"label": "राज्य संबंध एवं रूढ़िवादिता", "type": "branch", "date": "13वीं शताब्दी", "children": [
                        {"label": "बहाउद्दीन जकारिया द्वारा भारत में सुदृढ़ किया गया; पंजाब और सिंध में मुख्य रूप से सक्रिय", "type": "leaf"},
                        {"label": "चिश्तियों के विपरीत, राजकीय संरक्षण, अनुदान और शेख-उल-इस्लाम जैसे पदों को स्वीकार किया", "type": "leaf"}
                    ]},
                    {"label": "धन एवं संगठनात्मक दर्शन", "type": "branch", "date": "खानकाह", "children": [
                        {"label": "आलीशान और संपन्न खानकाहों का संचालन किया; तर्क दिया कि धन का उपयोग गरीबों की सेवा के लिए किया जा सकता है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "State Alignment & Orthodoxy", "type": "branch", "date": "13th Century", "children": [
                        {"label": "Consolidated in India by Baha-ud-din Zakariya; active primarily in Punjab and Sindh", "type": "leaf"},
                        {"label": "Unlike Chishtis, they did not reject the state; accepted royal titles like Sheikh-ul-Islam and grants", "type": "leaf"}
                    ]},
                    {"label": "Wealth & Khanqah Philosophy", "type": "branch", "date": "Organization", "children": [
                        {"label": "Maintained luxurious, well-endowed Khanqahs; argued that wealth is beneficial to serve the needy", "type": "leaf"}
                    ]}
                ]

        # 30. Naqshbandi Order
        elif 'naqshbandi' in fl:
            if is_hindi:
                return [
                    {"label": "रूढ़िवादी शरीयत", "type": "branch", "date": "मुगल काल", "children": [
                        {"label": "ख्वाजा बाकी बिल्लाह द्वारा भारत लाया गया; शेख अहमद सरहिंदी द्वारा व्यापक रूप से प्रसारित किया गया", "type": "leaf"},
                        {"label": "अकबर की उदार धार्मिक नीतियों और दीन-ए-इलाही के कट्टर विरोधी थे; कट्टर रूढ़िवादिता का समर्थन किया", "type": "leaf"}
                    ]},
                    {"label": "आध्यात्मिक आचरण", "type": "branch", "date": "निषेध", "children": [
                        {"label": "संगीत (समा) और गुरु के सामने साष्टांग प्रणाम पर रोक लगाई; मौन ईश्वर स्मरण (जिक्र-ए-कल्बी) पर जोर दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sharia & Orthodoxy", "type": "branch", "date": "Mughal Era", "children": [
                        {"label": "Introduced by Khwaja Baqi Billah; popularized by Sheikh Ahmad Sirhindi (Mujaddid Alif Sani)", "type": "leaf"},
                        {"label": "Strongly opposed Akbar's liberal reforms and Din-i-Ilahi; advocated revival of strict Sharia", "type": "leaf"}
                    ]},
                    {"label": "Quietist Practices", "type": "branch", "date": "Prohibitions", "children": [
                        {"label": "Banned music (Sama) and prostration before the Pir; promoted silent remembrance (Zikr-i-Qalbi)", "type": "leaf"}
                    ]}
                ]

        # 31. Alvars & Nayanars Groups
        elif 'alvars' in fl or 'nayanars' in fl:
            if is_hindi:
                return [
                    {"label": "आलवार संत (वैष्णव)", "type": "branch", "date": "6वीं-9वीं शताब्दी", "children": [
                        {"label": "12 वैष्णव संत (एकमात्र महिला संत आंडाल सहित); विष्णु/नारायण के प्रति अनन्य प्रेम का उपदेश दिया", "type": "leaf"},
                        {"label": "इनके भजनों को 'नालयिर दिव्य प्रबंधम' (तमिल वेद) के रूप में संकलित किया गया है", "type": "leaf"}
                    ]},
                    {"label": "नयनार संत (शैव)", "type": "branch", "date": "तमिलनाडु", "children": [
                        {"label": "63 शैव संत (महिला संत करैक्काल अम्मैयार सहित); शिव भक्ति का प्रचार किया", "type": "leaf"},
                        {"label": "इनकी रचनाओं को पवित्र ग्रंथ 'तिरुमुराई' (शैव संकलन) के रूप में संकलित किया गया है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Vaishnavite Alvars", "type": "branch", "date": "6th-9th Century", "children": [
                        {"label": "12 Vaishnavite saints (including female saint Andal); preached ecstatic devotion to Lord Vishnu", "type": "leaf"},
                        {"label": "Hymns compiled in the Nalayira Divya Prabandham, revered as the Tamil Veda", "type": "leaf"}
                    ]},
                    {"label": "Shaivite Nayanars", "type": "branch", "date": "Tamil Nadu", "children": [
                        {"label": "63 Shaivite saints (including female saint Karaikkal Ammaiyar) from diverse caste backgrounds", "type": "leaf"},
                        {"label": "Compositions compiled into the sacred Tirumurai, defining South Indian Shaiva Siddhanta", "type": "leaf"}
                    ]}
                ]

        # 32. Nirguna Bhakti Group
        elif 'nirgun' in fl:
            if is_hindi:
                return [
                    {"label": "मूल दार्शनिक सिद्धांत", "type": "branch", "date": "निराकार ब्रह्म", "children": [
                        {"label": "ईश्वर को निराकार, गुणहीन और सर्वव्यापी मानकर (निर्गुण ब्रह्म) उपासना करने पर बल दिया", "type": "leaf"},
                        {"label": "कबीर, गुरु नानक, रैदास और दादू दयाल इसके प्रमुख प्रणेता थे", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक सुधार एवं विरोध", "type": "branch", "date": "सुधार", "children": [
                        {"label": "मूर्तिपूजा, तीर्थयात्राओं, जटिल कर्मकांडों और पुरोहितों के एकाधिकार का खुलकर विरोध किया", "type": "leaf"},
                        {"label": "जातिगत भेदभाव और छुआछूत का खंडन कर सभी मनुष्यों की आध्यात्मिक समानता की वकालत की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Core Philosophical Tenets", "type": "branch", "date": "Formless Brahman", "children": [
                        {"label": "Worshipped formless, qualityless, omnipresent Supreme God (Nirguna Brahman) without images", "type": "leaf"},
                        {"label": "Led by saints like Kabir, Guru Nanak, Raidas, and Dadu Dayal", "type": "leaf"}
                    ]},
                    {"label": "Socio-Religious Protest", "type": "branch", "date": "Reforms", "children": [
                        {"label": "Strongly rejected idol worship, pilgrimages, complex sacrifices, and Brahmanical priesthood monopoly", "type": "leaf"},
                        {"label": "Challenged birth-based caste hierarchy and gender discrimination, promoting vernacular outreach", "type": "leaf"}
                    ]}
                ]

        # 33. Saguna Bhakti Group
        elif 'sagun' in fl:
            if is_hindi:
                return [
                    {"label": "साकार उपासना", "type": "branch", "date": "सगुण ब्रह्म", "children": [
                        {"label": "विशिष्ट गुणों, सुंदर साकार रूपों और अवतारों वाले ईश्वर (सगुण ब्रह्म) की उपासना पर बल दिया", "type": "leaf"},
                        {"label": "भगवान विष्णु के अवतारों - मुख्य रूप से राम और कृष्ण की उपासना को लोकप्रिय बनाया", "type": "leaf"}
                    ]},
                    {"label": "भक्ति मार्ग एवं प्रणेता", "type": "branch", "date": "प्रणेता", "children": [
                        {"label": "प्रमुख संत: तुलसीदास (राम भक्ति), सूरदास, मीराबाई और चैतन्य महाप्रभु (कृष्ण भक्ति)", "type": "leaf"},
                        {"label": "सामूहिक संकीर्तन, मंदिर पूजा, मूर्ति अर्चना और पवित्र तीर्थस्थलों की यात्रा को बढ़ावा दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Theology & Deities", "type": "branch", "date": "Saguna Brahman", "children": [
                        {"label": "Worshipped Supreme God with human attributes, physical forms, and incarnations (avatars)", "type": "leaf"},
                        {"label": "Focused primarily on the worship of Lord Rama (Maryada Purushottam) and Lord Krishna", "type": "leaf"}
                    ]},
                    {"label": "Devotional Pathways & Cults", "type": "branch", "date": "Saints", "children": [
                        {"label": "Key saints include Tulsidas (Ram devotion), Surdas, Mirabai, and Chaitanya Mahaprabhu (Krishna devotion)", "type": "leaf"},
                        {"label": "Advocated congregational singing (Kirtan), image worship (Murti Puja), and pilgrimages to sacred places", "type": "leaf"}
                    ]}
                ]

        # 34. What was the Movement About / Overview
        elif 'what-was-the-movement-about' in fl:
            if is_hindi:
                return [
                    {"label": "आद्यात्मिक पुनरुत्थान", "type": "branch", "date": "पुनर्जागरण", "children": [
                        {"label": "कर्मकांडों की जटिलता से सरल, प्रेम-आधारित और प्रत्यक्ष भक्ति (प्रपत्ति) की ओर आध्यात्मिक परिवर्तन", "type": "leaf"},
                        {"label": "धार्मिक एकाधिकार को तोड़ते हुए महिलाओं और शोषित वर्गों को आध्यात्मिक मुक्ति का अधिकार दिया", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक संश्लेषण", "type": "branch", "date": "समन्वय", "children": [
                        {"label": "सूफीवाद और भक्ति मार्ग के मिलाप से भारत में 'गंगा-जमुनी तहजीब' (साझा संस्कृति) का उदय हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Spiritual Renaissance", "type": "branch", "date": "Renaissance", "children": [
                        {"label": "Shifted focus from complex Vedic sacrifices to simple, personal love and self-surrender to God", "type": "leaf"},
                        {"label": "Broke religious monopoly by declaring women and marginalized castes as spiritually equal", "type": "leaf"}
                    ]},
                    {"label": "Socio-Cultural Syncretism", "type": "branch", "date": "Synthesis", "children": [
                        {"label": "Combined with Sufism to shape a syncretic cultural heritage (Ganga-Jamuni Tehzeeb) in India", "type": "leaf"}
                    ]}
                ]

        # Fallback for Bhakti & Sufi
        else:
            if is_hindi:
                return [
                    {"label": "सूफी और भक्ति", "type": "branch", "date": "मध्यकालीन आंदोलन", "children": [
                        {"label": "समानता, ईश्वर के प्रति प्रेम और धार्मिक सद्भाव की वकालत करने वाले मध्यकालीन सुधार", "type": "leaf"},
                        {"label": "सूफी सिलसिले और भक्ति संत जिन्होंने हिंदू-मुस्लिम सांस्कृतिक समन्वय में योगदान दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sufi & Bhakti Movements", "type": "branch", "date": "Medieval Reform", "children": [
                        {"label": "Medieval reform movements emphasizing love for God, equality, and syncretic culture", "type": "leaf"},
                        {"label": "Chishti, Suhrawardi, and Naqshbandi orders; Nirguna and Saguna Bhakti saints", "type": "leaf"}
                    ]}
                ]

    # =========================================================================
    # E. VIJAYANAGAR EMPIRE
    # =========================================================================
    elif 'vijaynagar-empire' in cat_lower or 'vijayanagar' in fl or 'vijaynagar' in fl:
        
        # 1. Sources of Information about Vijayanagar Empire
        if 'sources-of-information' in fl:
            if is_hindi:
                return [
                    {"label": "अभिलेखीय और पुरातात्विक स्रोत", "type": "branch", "date": "स्रोत", "children": [
                        {"label": "शिलालेख: बादामी, हम्पी और कोडागेरहल्ली शिलालेख भूमि अनुदान, करों और वंशावली की जानकारी देते हैं", "type": "leaf"},
                        {"label": "हम्पी के खंडहर: भवनों, बाज़ारों और मंदिरों के अवशेष नगर नियोजन, जल प्रबंधन और स्थापत्य कला को दर्शाते हैं", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक स्रोत", "type": "branch", "date": "साहित्य", "children": [
                        {"label": "मदुराविजयम: गंगादेवी द्वारा रचित महाकाव्य जो कुमार कंपना की मदुरै विजय का वर्णन करता है", "type": "leaf"},
                        {"label": "अमुक्तमाल्याद: कृष्णदेवराय द्वारा लिखित तेलुगु ग्रंथ जो राजनीतिक विचारों और शासन व्यवस्था को स्पष्ट करता है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Epigraphic & Archaeological Sources", "type": "branch", "date": "Sources", "children": [
                        {"label": "Inscriptions: Badami, Hampi, and Kodagerahalli copper plates recording land grants and taxation", "type": "leaf"},
                        {"label": "Hampi Ruins: Excavations detailing central royal platforms, bazaars, and sophisticated irrigation canals", "type": "leaf"}
                    ]},
                    {"label": "Literary Chronicles", "type": "branch", "date": "Literature", "children": [
                        {"label": "Madhuravijayam: Epic poem by Gangadevi describing prince Kumara Kampana's conquest of Madurai", "type": "leaf"},
                        {"label": "Amuktamalyada: Telugu text by Krishnadevaraya outlining political philosophy and administrative duties", "type": "leaf"}
                    ]}
                ]

        # 2. Vijayanagar Administration
        elif 'administration' in fl:
            if is_hindi:
                return [
                    {"label": "केंद्रीय और प्रांतीय शासन", "type": "branch", "date": "शासन ढांचा", "children": [
                        {"label": "राजशाही: राजा (राय) सर्वोच्च शासक था, जो मंत्रियों की परिषद (प्रधान) की सहायता से शासन करता था", "type": "leaf"},
                        {"label": "प्रशासनिक विभाजन: साम्राज्य का विभाजन मंडलम (प्रांत), नाडु (जिला) और ग्राम (गाँव) में किया गया था", "type": "leaf"}
                    ]},
                    {"label": "नायकर और आयगार प्रणाली", "type": "branch", "date": "स्थानीय नियंत्रण", "children": [
                        {"label": "नायकर व्यवस्था: सैन्य प्रमुखों (अमर-नायक) को उनकी सेना के रखरखाव के लिए भूमि क्षेत्र (अमरम) दिए गए थे", "type": "leaf"},
                        {"label": "आयगार व्यवस्था: ग्रामीण प्रशासन 12 वंशानुगत अधिकारियों (आयगारों) के हाथ में था, जिन्हें कर-मुक्त भूमि दी जाती थी", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Central & Provincial Setup", "type": "branch", "date": "Structure", "children": [
                        {"label": "Monarchy: The King (Raya) held absolute power, advised by a council of ministers led by the Pradhani", "type": "leaf"},
                        {"label": "Administrative Units: Empire divided into Mandalams (provinces), Nadus (districts), and Gramas (villages)", "type": "leaf"}
                    ]},
                    {"label": "Nayakara & Ayagar Systems", "type": "branch", "date": "Governance", "children": [
                        {"label": "Nayakara System: Military chiefs (Amara-Nayakas) held lands (Amaram) in lieu of maintaining royal troops", "type": "leaf"},
                        {"label": "Ayagar System: A body of 12 village officers administered locally, possessing hereditary rights over land", "type": "leaf"}
                    ]}
                ]

        # 3. Vijayanagar Art and Architecture
        elif 'art-and-architecture' in fl or 'art' in fl or 'architecture' in fl:
            if is_hindi:
                return [
                    {"label": "हम्पी की मंदिर वास्तुकला", "type": "branch", "date": "ग्रेनाइट शैली", "children": [
                        {"label": "प्रमुख मंदिर: विट्ठल मंदिर (एकाश्म पत्थर का रथ, 56 संगीतमय स्तंभ) और विरूपाक्ष मंदिर शामिल हैं", "type": "leaf"},
                        {"label": "मुख्य विशेषताएं: अलंकृत नक्काशीदार खंभे, विशाल कल्याण मंडप (विवाह कक्ष) और भव्य राय गोपुरम", "type": "leaf"}
                    ]},
                    {"label": "धर्मनिरपेक्ष और चित्रकला कला", "type": "branch", "date": "विविध", "children": [
                        {"label": "भारत-इस्लामी प्रभाव: लोटस महल, हाथियों के अस्तबल और रानी के स्नानघर में इस्लामी मेहराबों का प्रभाव दिखता है", "type": "leaf"},
                        {"label": "लेपाक्षी चित्रकला: वीरभद्र मंदिर (लेपाक्षी) की छतों पर बने भित्तिचित्र विजयनगर चित्रकला के उत्कृष्ट उदाहरण हैं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Hampi Temple Architecture", "type": "branch", "date": "Granite Style", "children": [
                        {"label": "Major Temples: Vittala Temple (monolithic stone chariot, 56 musical pillars) and the tall Virupaksha Temple", "type": "leaf"},
                        {"label": "Architectural features: Ornate carved pillars (Yali motifs), Kalyan Mandapas, and soaring Raya Gopurams", "type": "leaf"}
                    ]},
                    {"label": "Secular & Painting Legacies", "type": "branch", "date": "Arts", "children": [
                        {"label": "Indo-Islamic synthesis: Displayed in the arches of the Lotus Mahal, Queen's Bath, and Elephant Stables", "type": "leaf"},
                        {"label": "Lepakshi Murals: Ceiling paintings in the Virabhadra Temple showcasing distinct styles and Hindu themes", "type": "leaf"}
                    ]}
                ]

        # 4. Vijayanagar Dynasties: Sangama
        elif 'dynasties-sangama' in fl or 'sangama' in fl:
            if is_hindi:
                return [
                    {"label": "स्थापना और प्रारंभिक संघर्ष", "type": "branch", "date": "1336-1485 ई.", "children": [
                        {"label": "स्थापना: 1336 ई. में हरिहर प्रथम और बुक्का प्रथम द्वारा स्थापित; ऋषि विद्यारण्य से प्रेरणा ली थी", "type": "leaf"},
                        {"label": "दक्कन संघर्ष: बहमनी साम्राज्य के साथ रायचूर दोआब (कृष्णा-तुंगभद्रा के बीच उपजाऊ क्षेत्र) को लेकर संघर्ष", "type": "leaf"}
                    ]},
                    {"label": "देवराय द्वितीय का स्वर्ण युग", "type": "branch", "date": "चरम सीमा", "children": [
                        {"label": "सैन्य सुधार: सेना का आधुनिकीकरण किया, बड़े पैमाने पर मुस्लिम तीरंदाजों और घुड़सवारों को भर्ती किया", "type": "leaf"},
                        {"label": "विदेशी दूत: फारसी राजदूत अब्दुर रज्जाक ने उनके काल में विजयनगर के वैभव का आँखों देखा विवरण दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Foundation & Rivalries", "type": "branch", "date": "1336-1485 AD", "children": [
                        {"label": "Establishment: Founded in 1336 AD by Harihara I and Bukka I, inspired by the sage Vidyaranya", "type": "leaf"},
                        {"label": "Bahmani Clash: Constant warfare over the fertile Raichur Doab located between Krishna and Tungabhadra rivers", "type": "leaf"}
                    ]},
                    {"label": "Zenith under Devaraya II", "type": "branch", "date": "Peak", "children": [
                        {"label": "Military reform: Recruited skilled Muslim archers and cavalrymen to modernize the state army", "type": "leaf"},
                        {"label": "Foreign envoy: Welcomed Persian ambassador Abdur Razzak, who documented the empire's vast wealth", "type": "leaf"}
                    ]}
                ]

        # 5. Vijayanagar Dynasties: Suluva
        elif 'dynasties-suluva' in fl or 'suluva' in fl:
            if is_hindi:
                return [
                    {"label": "प्रथम बलात्हार और स्थापना", "type": "branch", "date": "1485-1505 ई.", "children": [
                        {"label": "स्थापना: सालुव नरसिंह द्वारा स्थापित; संगम वंश के कमजोर होने पर सत्ता संभाली (प्रथम बलात्हार)", "type": "leaf"},
                        {"label": "उद्देश्य: बहमनी और उड़ीसा के गजपतियों के खिलाफ राज्य की सीमाओं को सुरक्षित करना था", "type": "leaf"}
                    ]},
                    {"label": "योगदान और सेना सुधार", "type": "branch", "date": "योगदान", "children": [
                        {"label": "घोड़ों का आयात: सेना को मजबूत बनाने के लिए अरब व्यापारियों के साथ पश्चिमी तट के बंदरगाहों पर व्यापार बढ़ाया", "type": "leaf"},
                        {"label": "तुलुव वंश का उदय: सालुव वंश के अंत में वीर नरसिंह ने सत्ता हथियाई (द्वितीय बलात्हार)", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "First Usurpation & Rise", "type": "branch", "date": "1485-1505 AD", "children": [
                        {"label": "Establishment: Founded by Saluva Narasimha to replace weak Sangama rulers (First Usurpation)", "type": "leaf"},
                        {"label": "Geopolitical defense: Stabilized frontiers against Bahmani incursions and Gajapatis of Odisha", "type": "leaf"}
                    ]},
                    {"label": "Military Consolidation", "type": "branch", "date": "Impact", "children": [
                        {"label": "Cavalry Trade: Prioritized horse imports from Arabian merchants at western ports like Bhatkal", "type": "leaf"},
                        {"label": "Transition: Saluva rule ended when Tuluva Narasa Nayaka's son seized the throne (Second Usurpation)", "type": "leaf"}
                    ]}
                ]

        # 6. Vijayanagar Dynasties: Tuluva
        elif 'dynasties-tuluva' in fl or 'tuluva' in fl:
            if is_hindi:
                return [
                    {"label": "कृष्णदेवराय का महान काल", "type": "branch", "date": "1509-1529 ई.", "children": [
                        {"label": "साम्राज्य विस्तार: बीजापुर के आदिल शाह को पराजित किया और रायचूर दोआब पर पूर्ण नियंत्रण किया", "type": "leaf"},
                        {"label": "ओडिशा विजय: गजपति राजा प्रताप रुद्रदेव को पराजित किया; सीमा उदयगिरि तक बढ़ाई", "type": "leaf"},
                        {"label": "पुर्तगाली मैत्री: गवर्नर अल्बुकर्क के साथ अच्छे संबंध रखे; घोड़ों के आयात पर एकाधिकार प्राप्त किया", "type": "leaf"}
                    ]},
                    {"label": "तालीकोटा का युद्ध और पतन", "type": "branch", "date": "1565 ई.", "children": [
                        {"label": "तालीकोटा का युद्ध (1565): सदाशिवराय के काल में रामराय ने दक्कन सल्तनतों के गठबंधन से हार का सामना किया", "type": "leaf"},
                        {"label": "विनाश: युद्ध के बाद संयुक्त मुस्लिम सेनाओं ने राजधानी विजयनगर (हम्पी) को पूरी तरह लूटकर तबाह कर दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Krishna Deva Raya's Hegemony", "type": "branch", "date": "1509-1529 AD", "children": [
                        {"label": "Raichur Conquest: Defeated Adil Shah of Bijapur, permanently annexing the fertile Raichur Doab", "type": "leaf"},
                        {"label": "Gajapati Wars: Defeated Orissa's King Prataparudra; established boundary at the Udayagiri Fort", "type": "leaf"},
                        {"label": "Portuguese Alliance: Signed horse supply treaties with Albuquerque, bypassing local Muslim middlemen", "type": "leaf"}
                    ]},
                    {"label": "Battle of Talikota & Ruin", "type": "branch", "date": "1565 AD", "children": [
                        {"label": "Talikota Clash (1565 AD): Regent Rama Raya faced a combined coalition of four Deccani Sultanates", "type": "leaf"},
                        {"label": "Hampi Plunder: Defeat led to the systematic looting and complete abandonment of the capital city", "type": "leaf"}
                    ]}
                ]

        # 7. Vijayanagar Dynasties: Aravidu
        elif 'dynasties-aravidu' in fl or 'aravidu' in fl:
            if is_hindi:
                return [
                    {"label": "स्थापना और राजधानियों का परिवर्तन", "type": "branch", "date": "1570-1646 ई.", "children": [
                        {"label": "पुनर्गठन: तालीकोटा के युद्ध के बाद तिरुमल देवराय ने चंद्रगिरि और पेनुकोंडा को केंद्र बनाकर स्थापना की", "type": "leaf"},
                        {"label": "राजधानी: साम्राज्य का प्रशासनिक केंद्र अंततः पेनूकोंडा से चंद्रगिरि और फिर वेल्लोर स्थानांतरित हुआ", "type": "leaf"}
                    ]},
                    {"label": "विघटन और अंत", "type": "branch", "date": "पतन", "children": [
                        {"label": "नायकों का विद्रोह: मदुरै, तंजौर और जिंजी के स्थानीय नायकों ने स्वतंत्रता की घोषणा कर दी", "type": "leaf"},
                        {"label": "बाहरी आक्रमण: बीजापुर और गोलकुंडा के लगातार आक्रमणों ने 1646 तक साम्राज्य का पूर्ण अंत कर दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Capitals Shift & Restoration", "type": "branch", "date": "1570-1646 AD", "children": [
                        {"label": "Re-establishment: Founded by Tirumala Deva Raya, who saved royalty and moved south after Talikota", "type": "leaf"},
                        {"label": "Administrative seats: Capital shifted from Penukonda to Chandragiri, and later to Vellore", "type": "leaf"}
                    ]},
                    {"label": "Nayaka Rebellion & Disintegration", "type": "branch", "date": "Decline", "children": [
                        {"label": "Nayaka Autonomy: Semi-independent governors of Madurai, Tanjore, and Gingee declared independence", "type": "leaf"},
                        {"label": "Final Annexation: Encroachments by Bijapur and Golconda sultanates dissolved the empire by 1646 AD", "type": "leaf"}
                    ]}
                ]

        # 8. Vijayanagar Economy
        elif 'economy' in fl:
            if is_hindi:
                return [
                    {"label": "भू-राजस्व और वित्तीय प्रणाली", "type": "branch", "date": "राजस्व", "children": [
                        {"label": "भू-राजस्व (शिष्ट): राज्य की आय का प्रमुख स्रोत, जो उपज के 1/6 से 1/3 भाग तक आकलित था", "type": "leaf"},
                        {"label": "विविध कर: विवाह कर, गृह कर और सीमा शुल्क के अलावा कड़ाही (व्यावसायिक कर) लिया जाता था", "type": "leaf"}
                    ]},
                    {"label": "समुद्री व्यापार और बंदरगाह", "type": "branch", "date": "व्यापार", "children": [
                        {"label": "पश्चिमी बंदरगाह: भटकल, मंगलोर और होनावर से अरब घोड़ों, मखमल और मसालों का व्यापार होता था", "type": "leaf"},
                        {"label": "सोने के सिक्के: वराह (पैगोडा) नाम के सोने के सिक्कों का व्यापक प्रचलन उच्च मुद्रीकरण को दर्शाता है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Agrarian Fiscal System", "type": "branch", "date": "Revenue", "children": [
                        {"label": "Land Tax (Sist): Primary source of state income, generally assessed between 1/6th and 1/3rd of output", "type": "leaf"},
                        {"label": "Commercial dues: Levied duties on professions, oil mills, looms, and controversial marriage taxes", "type": "leaf"}
                    ]},
                    {"label": "Ocean Trade & Coinage", "type": "branch", "date": "Commerce", "children": [
                        {"label": "Ports: Bhatkal, Mangalore, and Honavar handled active exports of pepper, sandalwood, and textiles", "type": "leaf"},
                        {"label": "Gold coins: Widespread circulation of Varahas (also called Pagodas), depicting Hindu deities", "type": "leaf"}
                    ]}
                ]

        # 9. Vijayanagar Foreign Travelers and their Accounts
        elif 'travelers' in fl or 'accounts' in fl:
            if is_hindi:
                return [
                    {"label": "प्रारंभिक यात्री और राजदूत", "type": "branch", "date": "15वीं सदी", "children": [
                        {"label": "निकोलो दे कोंटी (इतालवी, 1420): देवराय प्रथम के काल में आया; शहर के घेरे और सती प्रथा का वर्णन किया", "type": "leaf"},
                        {"label": "अब्दुर रज्जाक (फारसी राजदूत, 1443): देवराय द्वितीय के काल में आया; हम्पी की किलाबंदी के सात स्तरों का वर्णन किया", "type": "leaf"}
                    ]},
                    {"label": "पुर्तगाली लेखक", "type": "branch", "date": "16वीं सदी", "children": [
                        {"label": "डोमिंगो पेस (1520): कृष्णदेवराय के दरबार का वर्णन किया; हम्पी के बाज़ारों और विट्ठल मंदिर की प्रशंसा की", "type": "leaf"},
                        {"label": "फर्नाओ नुनीज (1535): अच्युतदेव राय के समय आया; विजयनगर के इतिहास और अमर-नायकों के कर्तव्यों को लिखा", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Early Chroniclers & Ambassadors", "type": "branch", "date": "15th Century", "children": [
                        {"label": "Nicolo de Conti (Italian, 1420): Visited under Devaraya I; noted the city circumference and Sati", "type": "leaf"},
                        {"label": "Abdur Razzak (Persian, 1443): Visited under Devaraya II; described the seven lines of massive fort walls", "type": "leaf"}
                    ]},
                    {"label": "Portuguese Chroniclers", "type": "branch", "date": "16th Century", "children": [
                        {"label": "Domingo Paes (1520): Recorded Krishnadevaraya's appearance, Hampi's wealth, and the Mahanavami festival", "type": "leaf"},
                        {"label": "Fernao Nuniz (1535): Visited under Achyutadeva Raya; wrote detailed history of dynastic transitions", "type": "leaf"}
                    ]}
                ]

        # 10. Vijayanagar Literature
        elif 'literature' in fl:
            if is_hindi:
                return [
                    {"label": "तेलुगु साहित्य का स्वर्ण युग", "type": "branch", "date": "अष्टदिग्गज", "children": [
                        {"label": "अष्टदिग्गज: कृष्णदेवराय के दरबार के आठ कवि; अल्लसानी पेद्दन (मनुचरितम) और तेनाली राम रामकृष्ण मुख्य थे", "type": "leaf"},
                        {"label": "अमुक्तमाल्याद: कृष्णदेवराय द्वारा रचित तेलुगु ग्रंथ जो प्रशासनिक सिद्धांतों का विवरण देता है", "type": "leaf"}
                    ]},
                    {"label": "बहुभाषी विकास", "type": "branch", "date": "विविध", "children": [
                        {"label": "संस्कृत संरक्षण: वेदों के भाष्यकार सायण और उनके भाई माधव विद्यारण्य ने वैदिक व्याख्याओं की रचना की", "type": "leaf"},
                        {"label": "कन्नड़ और तमिल: चामरस (प्रभुलिंगलीले) और कुमारव्यास (कन्नड़ भारत) जैसे कवियों को संरक्षण दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Telugu Golden Age & Court", "type": "branch", "date": "Ashtadiggajas", "children": [
                        {"label": "Ashtadiggajas: Eight court poets led by Allasani Peddana (Manucharitamu) and Tenali Ramakrishna", "type": "leaf"},
                        {"label": "Amuktamalyada: Krishnadevaraya's Telugu work depicting devotion of Andal and state polity rules", "type": "leaf"}
                    ]},
                    {"label": "Sanskrit & Regional Growth", "type": "branch", "date": "Multilingual", "children": [
                        {"label": "Sanskrit: Celebrated commentator Sayana and sage Vidyaranya produced extensive Vedic reviews", "type": "leaf"},
                        {"label": "Kannada & Tamil: Patronized poets like Chamarasa (Prabhulingaleele) and Kumara Vyasa (Kannada Bharata)", "type": "leaf"}
                    ]}
                ]

        # 11. Vijayanagar Social Aspects
        elif 'social' in fl:
            if is_hindi:
                return [
                    {"label": "सामाजिक संरचना और वर्ग", "type": "branch", "date": "समाज", "children": [
                        {"label": "ब्राह्मणों का वर्चस्व: प्रशासनिक पदों और राजस्व माफी के कारण ब्राह्मणों को समाज में सर्वोच्च स्थान प्राप्त था", "type": "leaf"},
                        {"label": "जाति विभाजन: विप्र (ब्राह्मण), रेड्डी और बलिजा व्यापारियों का उदय हुआ; दलितों को पृथक रखा जाता था", "type": "leaf"}
                    ]},
                    {"label": "महिलाओं की स्थिति और धार्मिक सहिष्णुता", "type": "branch", "date": "विविध", "children": [
                        {"label": "महिलाएं: वे लिपिक, कुश्ती, ज्योतिष और राजमहल के रक्षक के रूप में कार्य करती थीं; देवदासी प्रथा का प्रचलन था", "type": "leaf"},
                        {"label": "धार्मिक नीति: शैवों (वीरशैव), वैष्णवों और जैनियों के बीच शांतिपूर्ण संबंध थे; मुसलमानों को सेना में शामिल किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Social Stratification & Castes", "type": "branch", "date": "Society", "children": [
                        {"label": "Brahminical status: Held supreme influence as ministers, priests, and owners of tax-free Brahmadeya lands", "type": "leaf"},
                        {"label": "Social division: Divided into Valangai (right-hand) and Idangai (left-hand) caste alliances", "type": "leaf"}
                    ]},
                    {"label": "Women & Religious Tolerance", "type": "branch", "date": "Socio-Cultural", "children": [
                        {"label": "Women's status: Actively worked as palace guards, chroniclers, and wrestlers; Sati and Devadasi system existed", "type": "leaf"},
                        {"label": "Tolerance: Harmonized Vaishnava-Jain disputes; recruited Muslim archers and permitted mosques", "type": "leaf"}
                    ]}
                ]

        # Fallback for Vijaynagar
        else:
            if is_hindi:
                return [
                    {"label": "विजयनगर साम्राज्य सामान्य", "type": "branch", "date": "सामान्य", "children": [
                        {"label": "हरिहर और बुक्का द्वारा 1336 ई. में स्थापित दक्षिण भारत का एक हिंदू साम्राज्य", "type": "leaf"},
                        {"label": "हम्पी (विजयनगर) इसकी विशाल राजधानी थी, जो अपनी ग्रेनाइट कला और किलाबंदी के लिए प्रसिद्ध थी", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Vijayanagar Empire Overview", "type": "branch", "date": "Overview", "children": [
                        {"label": "South Indian Hindu kingdom established in 1336 AD by brothers Harihara I and Bukka I", "type": "leaf"},
                        {"label": "Hampi served as the capital, famed for massive stone temples and active maritime horse trade", "type": "leaf"}
                    ]}
                ]
    # =========================================================================
    # F. RISE OF THE MARATHAS
    # =========================================================================
    elif 'rise-of-the-marathas' in cat_lower or 'maratha' in fl or 'peshwa' in fl or 'bhonsle' in fl or 'gaekwad' in fl or 'holkar' in fl or 'sindhia' in fl or 'shiva' in fl or 'shivaji' in fl:
        
        # 1. Chhatrapati Shivaji (Administration & Military)
        if 'chhatrapati-shivaji' in fl or 'shiva' in fl:
            if is_hindi:
                return [
                    {"label": "सैन्य रणनीति और स्वराज्य", "type": "branch", "date": "1674 ई.", "children": [
                        {"label": "गनीमी कावा (छापामार नीति): पहाड़ी इलाकों में गतिशीलता, स्थानीय भूगोल और घात लगाने की रणनीति", "type": "leaf"},
                        {"label": "नौसेना निर्माण: कोंकण तट की रक्षा और जंजीरा के सिद्दियों से निपटने के लिए कान्होजी आंग्रे के अधीन नौसेना बनाई", "type": "leaf"},
                        {"label": "राज्याभिषेक: 1674 में रायगढ़ दुर्ग में राज्याभिषेक; दुर्ग-केंद्रित प्रशासनिक रक्षा प्रणाली विकसित की", "type": "leaf"}
                    ]},
                    {"label": "अष्टप्रधान और कराधान", "type": "branch", "date": "प्रशासन", "children": [
                        {"label": "अष्टप्रधान: 8 मंत्रियों की परिषद; पेशवा (प्रधानमंत्री), अमात्य (वित्त), सुमंत (विदेश) और सेनापति सैन्य प्रमुख", "type": "leaf"},
                        {"label": "चौथ और सरदेशमुखी: सुरक्षा के बदले राजस्व का 1/4 (चौथ) और वंशानुगत प्रमुख के रूप में 10% अधिभार (सरदेशमुखी)", "type": "leaf"},
                        {"label": "भूमि सुधार: काठी प्रणाली द्वारा भूमि मापन; जागीरदारी प्रथा समाप्त कर किसानों (रैयत) से सीधा संपर्क किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Military Strategy & Swarajya", "type": "branch", "date": "1674 AD", "children": [
                        {"label": "Ganimi Kawa (Guerrilla warfare): High mobility, surprise raids, and utilization of rugged Deccan terrain", "type": "leaf"},
                        {"label": "Naval force: Established a coastal navy under Kanhoji Angre to secure Konkan against Siddis and Europeans", "type": "leaf"},
                        {"label": "Coronated at Raigad (1674); developed a network of 250+ hill forts serving as administrative bases", "type": "leaf"}
                    ]},
                    {"label": "Ashta Pradhan & Taxation", "type": "branch", "date": "Administration", "children": [
                        {"label": "Ashta Pradhan: Council of 8 ministers led by the Peshwa; Amatya (finance) and Dabir/Sumant (foreign)", "type": "leaf"},
                        {"label": "Fiscal tools: Levied Chauth (25% tax for protection from raids) and Sardeshmukhi (10% additional claim)", "type": "leaf"},
                        {"label": "Land reforms: Standardized measurement using Kathi; bypassed feudal intermediaries to contact ryots directly", "type": "leaf"}
                    ]}
                ]

        # 2. Third Battle of Panipat
        elif 'third-battle-of-panipat' in fl or 'battle-of-panipat' in fl:
            if is_hindi:
                return [
                    {"label": "युद्ध की भिड़ंत", "type": "branch", "date": "1761 ई.", "children": [
                        {"label": "सदाशिवराव भाऊ के नेतृत्व में मराठा सेना और अहमद शाह अब्दाली (अफगान) के बीच पानीपत में ऐतिहासिक युद्ध हुआ", "type": "leaf"},
                        {"label": "राजनयिक विफलता: राजपूतों, जाटों और सिखों को पहले वसूले गए भारी करों के कारण मराठों ने अलग-थलग कर दिया", "type": "leaf"},
                        {"label": "गठबंधन: अब्दाली ने रोहिल्ला प्रमुख नजीब-उद-दौला और अवध के शुजा-उद-दौला के साथ मजबूत मोर्चा बनाया", "type": "leaf"}
                    ]},
                    {"label": "पराजय के कारण और परिणाम", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "सैन्य असंतुलन: मराठा शिविर में भोजन की गंभीर कमी और अब्दाली के श्रेष्ठ तोपखाने/ऊंट-तोपों के कारण पराजय", "type": "leaf"},
                        {"label": "मराठा कुलीन वर्ग का भारी संहार (विश्वासराव, भाऊ का निधन); पेशवा बालाजी बाजीराव का शोक में निधन", "type": "leaf"},
                        {"label": "भू-राजनीतिक बदलाव: मराठा विस्तार थमा; मुगलों की कमजोरी उजागर हुई; ब्रिटिश ईस्ट इंडिया कंपनी के उदय का मार्ग खुला", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "The Panipat Confrontation", "type": "branch", "date": "1761 AD", "children": [
                        {"label": "Sadashivrao Bhau led the Marathas against the Afghan confederacy of Ahmad Shah Abdali at Panipat", "type": "leaf"},
                        {"label": "Diplomatic isolation: Prior aggressive tribute demands alienated Jats, Rajputs, and Sikhs from the campaign", "type": "leaf"},
                        {"label": "Afghan alliances: Abdali successfully recruited Rohilla chief Najib-ud-Daula and Awadh's Shuja-ud-Daula", "type": "leaf"}
                    ]},
                    {"label": "Causes of Defeat & Impact", "type": "branch", "date": "Impact", "children": [
                        {"label": "Tactical limits: Starvation in Maratha camp, poor communications, and Abdali's superior swivel gun artillery", "type": "leaf"},
                        {"label": "Decimated elite commanders: Vishwasrao and Sadashivrao Bhau fell; Peshwa Balaji Baji Rao died of shock", "type": "leaf"},
                        {"label": "Geopolitical shift: Halted Maratha northern expansion, leaving a power vacuum exploited by the British EIC", "type": "leaf"}
                    ]}
                ]

        # 3. The Peshwas (General or specific period)
        elif 'the-peshwas' in fl or 'peshwa' in fl:
            if '1713-1818' in fl:
                if is_hindi:
                    return [
                        {"label": "पेशवा सत्ता का उत्कर्ष", "type": "branch", "date": "1713-1761 ई.", "children": [
                            {"label": "बालाजी विश्वनाथ (1713-20): पेशवा पद को वंशानुगत बनाया; दिल्ली की संधि (1719) से चौथ अधिकार हासिल किए", "type": "leaf"},
                            {"label": "बाजीराव प्रथम (1720-40): महान सेनापति; मालवा, गुजरात, बुंदेलखंड जीता; हिंदू-पद-पादशाही का नारा दिया", "type": "leaf"},
                            {"label": "बालाजी बाजीराव (1740-61): सांगोला समझौते (1750) द्वारा पेशवा राज्य के वास्तविक प्रशासनिक प्रमुख बने", "type": "leaf"}
                        ]},
                        {"label": "महासंघ और पतन", "type": "branch", "date": "1761-1818 ई.", "children": [
                            {"label": "मराठा महासंघ: पेशवा की शक्ति कमजोर हुई और पांच अर्ध-स्वायत्त घरानों (सिंधिया, होल्कर आदि) का उदय हुआ", "type": "leaf"},
                            {"label": "सहायक संधि: बाजीराव द्वितीय ने वसीन की संधि (1802) पर हस्ताक्षर कर ब्रिटिश प्रभुत्व स्वीकार किया", "type": "leaf"},
                            {"label": "पतन: तीन आन्तरिक आंग्ल-मराठा युद्धों के बाद 1818 में पेशवा पद समाप्त कर कानपुर निर्वासित कर दिया गया", "type": "leaf"}
                        ]}
                    ]
                else:
                    return [
                        {"label": "Peshwaship Ascension", "type": "branch", "date": "1713-1761 AD", "children": [
                            {"label": "Balaji Vishwanath (1713-20): Secured hereditary rights; negotiated Treaty of Delhi (1719) with Sayyids", "type": "leaf"},
                            {"label": "Baji Rao I (1720-40): Master strategist; expanded into Malwa, Gujarat, and championed Hindu-pad-padshahi", "type": "leaf"},
                            {"label": "Balaji Baji Rao (1740-61): Signed Sangola Agreement (1750), shifting executive authority from Satara to Pune", "type": "leaf"}
                        ]},
                        {"label": "Confederacy & Annexation", "type": "branch", "date": "1761-1818 AD", "children": [
                            {"label": "Confederacy split: Decentralization of power to autonomous houses (Scindias, Holkars, Gaekwads, Bhonsles)", "type": "leaf"},
                            {"label": "Treaty of Bassein (1802): Baji Rao II accepted British Subsidiary Alliance, compromising independence", "type": "leaf"},
                            {"label": "Dissolution: Defeat in three Anglo-Maratha Wars led to the annexation of Peshwa domains by the British in 1818", "type": "leaf"}
                        ]}
                    ]
            else:
                if is_hindi:
                    return [
                        {"label": "प्रशासनिक सत्ता का स्थानांतरण", "type": "branch", "date": "वास्तविक शासक", "children": [
                            {"label": "साहू के काल में प्रशासनिक शक्तियां धीरे-धीरे सतारा के छत्रपति से पुणे के पेशवाओं के पास आ गईं", "type": "leaf"},
                            {"label": "हुजूर दफ्तर: पुणे में एक विशाल केंद्रीय सचिवालय की स्थापना कर कुशल अभिलेख प्रणाली शुरू की", "type": "leaf"}
                        ]}
                    ]
                else:
                    return [
                        {"label": "De Facto Governance Shift", "type": "branch", "date": "Pune Center", "children": [
                            {"label": "Shifted the center of political decision-making from Satara Chhatrapati to the Peshwa at Pune", "type": "leaf"},
                            {"label": "Huzur Daftar: Established a highly organized central secretariat in Pune for revenue records", "type": "leaf"}
                        ]}
                    ]

        # 4. The Sindhias (Scindias of Gwalior)
        elif 'sindhia' in fl or 'shinde' in fl:
            if is_hindi:
                return [
                    {"label": "ग्वालियर राज्य और महादजी", "type": "branch", "date": "सिंधिया वर्चस्व", "children": [
                        {"label": "रानोजी सिंधिया द्वारा स्थापित; महादजी शिंदे (1761-94) के अधीन उत्तर भारत में मराठा शक्ति पुनः जीवित हुई", "type": "leaf"},
                        {"label": "दिल्ली पर नियंत्रण: 1772 में भगोड़े मुगल सम्राट शाह आलम द्वितीय को पुनः दिल्ली के सिंहासन पर बैठाया", "type": "leaf"},
                        {"label": "वकील-ए-मुतलक: महादजी शिंदे ने मुगल साम्राज्य के सर्वोच्च नायब (वकील-ए-मुतलक) की उपाधि प्राप्त की", "type": "leaf"}
                    ]},
                    {"label": "सैन्य और प्रशासनिक आधुनिकीकरण", "type": "branch", "date": "सुधार", "children": [
                        {"label": "यूरोपीय ब्रिगेड: फ्रांसीसी सेनापति बेनोइट डी बोइग्ने की मदद से आधुनिक पैदल सेना ब्रिगेड तैयार की", "type": "leaf"},
                        {"label": "सालबाई की संधि (1782): प्रथम आंग्ल-मराठा युद्ध समाप्त कराया; अंग्रेजों ने महादजी को स्वतंत्र शासक माना", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Mahadji Shinde & Gwalior", "type": "branch", "date": "Scindia House", "children": [
                        {"label": "Founded by Ranoji; Mahadji Shinde (1761-94) resurrected Maratha influence in North India after Panipat", "type": "leaf"},
                        {"label": "Delhi Custody: Restored exiled Mughal Emperor Shah Alam II to the throne in Delhi in 1772", "type": "leaf"},
                        {"label": "Wakil-i-Mutlaq: Appointed as the supreme executive regent of the Mughal Empire by the Emperor", "type": "leaf"}
                    ]},
                    {"label": "Modernization & Diplomacy", "type": "branch", "date": "Reforms", "children": [
                        {"label": "European Infantry: Hired French general Benoit de Boigne to train brigades and build gun foundries", "type": "leaf"},
                        {"label": "Treaty of Salbai (1782): Mediated end to First Anglo-Maratha War; recognized as independent sovereign mediator", "type": "leaf"}
                    ]}
                ]

        # 5. The Holkars of Indore
        elif 'holkar' in fl:
            if is_hindi:
                return [
                    {"label": "अहिल्याबाई होल्कर का शासन", "type": "branch", "date": "अहिल्याबाई", "children": [
                        {"label": "मल्हार राव होल्कर ने इंदौर राज्य की नींव रखी; अहिल्याबाई (1767-95) के शासनकाल में चरम पर पहुंचा", "type": "leaf"},
                        {"label": "प्रशासन: निजी संपत्ति और राज्य के खजाने को अलग रखा; भ्रष्टाचार मुक्त न्यायप्रिय शासन किया", "type": "leaf"},
                        {"label": "आर्थिक विकास: इंदौर को एक संपन्न व्यापारिक केंद्र बनाया; महेश्वरी बुनाई उद्योग को बढ़ावा दिया", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक पुनरुद्धार और मंदिर", "type": "branch", "date": "धार्मिक कार्य", "children": [
                        {"label": "काशी विश्वनाथ मंदिर (वाराणसी), सोमनाथ मंदिर (गुजरात) और विष्णुपद मंदिर (गया) का पुनर्निर्माण कराया", "type": "leaf"},
                        {"label": "संपूर्ण भारत में धर्मशालाएं, घाट, कुएं और अन्नक्षेत्र स्थापित कर तीर्थयात्रा मार्गों को सुगम बनाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Indore State & Ahilyabai", "type": "branch", "date": "Indore", "children": [
                        {"label": "Founded by Malhar Rao; Indore flourished under the administration of Ahilyabai Holkar (1767-95)", "type": "leaf"},
                        {"label": "Clean governance: Separated personal funds from state treasury, ensuring welfare-oriented taxation", "type": "leaf"},
                        {"label": "Commerce: Developed Indore as a trading hub; patronized the Maheshwari textile handloom industry", "type": "leaf"}
                    ]},
                    {"label": "Cultural & Religious Legacy", "type": "branch", "date": "Charity", "children": [
                        {"label": "Rebuilt premier destroyed shrines nationwide (Kashi Vishwanath, Somnath, Vishnupad temple at Gaya)", "type": "leaf"},
                        {"label": "Constructed dharamshalas, river ghats, and free kitchens along all major pilgrimage routes in India", "type": "leaf"}
                    ]}
                ]

        # 6. The Gaekwads of Baroda
        elif 'gaekwad' in fl:
            if is_hindi:
                return [
                    {"label": "गुजरात में बड़ौदा राज्य", "type": "branch", "date": "गायकवाड़", "children": [
                        {"label": "पीलाजी राव गायकवाड़ ने मुगलों को हराकर बड़ौदा को राजधानी बनाया और गुजरात में अधिकार सुदृढ़ किया", "type": "leaf"},
                        {"label": "पेशवा से संबंध: पेशवा के साथ लगातार राजस्व अधिकार को लेकर संघर्ष हुआ; स्वायत्तता बनाए रखी", "type": "leaf"}
                    ]},
                    {"label": "सयाजीराव तृतीय के सुधार", "type": "branch", "date": "सुधार युग", "children": [
                        {"label": "सयाजीराव गायकवाड़ तृतीय (1875-1939) ने बड़ौदा में अनिवार्य प्राथमिक शिक्षा लागू की", "type": "leaf"},
                        {"label": "सामाजिक सुधार: बाल विवाह का विरोध, जाति-विरोधी अभियानों का समर्थन (डॉ. बी.आर. अंबेडकर को सहायता दी)", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Baroda Consolidation", "type": "branch", "date": "Baroda", "children": [
                        {"label": "Pilaji Rao Gaekwad defeated Mughal forces, establishing Baroda as the dynastic capital in Gujarat", "type": "leaf"},
                        {"label": "Peshwa relations: Regularly clashed over revenue divisions; asserted fiscal independence", "type": "leaf"}
                    ]},
                    {"label": "Progressive Reform Era", "type": "branch", "date": "Sayajirao III", "children": [
                        {"label": "Sayajirao Gaekwad III (1875-1939) pioneered free compulsory primary education in Baroda", "type": "leaf"},
                        {"label": "Social reforms: Supported anti-caste campaigns and sponsored Dr. B.R. Ambedkar's higher education", "type": "leaf"}
                    ]}
                ]

        # 7. The Bhonsles of Nagpur
        elif 'bhonsle' in fl:
            if is_hindi:
                return [
                    {"label": "नागपुर राज्य का विस्तार", "type": "branch", "date": "भोंसले", "children": [
                        {"label": "रघूजी भोंसले प्रथम (1739-1755) ने नागपुर को राजधानी बनाया; देवगढ़ और छत्तीसगढ़ का विलय किया", "type": "leaf"},
                        {"label": "पूर्व की ओर फैलाव: संबलपुर, कटक जीतकर बंगाल की सीमा तक नियंत्रण स्थापित किया", "type": "leaf"}
                    ]},
                    {"label": "बंगाल अभियान और संधि", "type": "branch", "date": "बंगाल", "children": [
                        {"label": "भास्कर पंडित के नेतृत्व में बंगाल पर (1741-51) मराठा घुड़सवारों (बरगियों) के नियमित आक्रमण हुए", "type": "leaf"},
                        {"label": "1751 की संधि: बंगाल के नवाब अलीवर्दी खान से उड़ीसा छीना और वार्षिक चौथ के रूप में 12 लाख रुपये तय किए", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Nagpur House Expansion", "type": "branch", "date": "Bhonsle", "children": [
                        {"label": "Raghuji Bhonsle I (1739-1755) made Nagpur the capital; annexed Gond kingdoms of Chanda & Devgarh", "type": "leaf"},
                        {"label": "Eastern push: Conquered Chhattisgarh, Sambalpur, and Cuttack, extending control to Bay of Bengal", "type": "leaf"}
                    ]},
                    {"label": "Bengal Campaigns", "type": "branch", "date": "Bengal", "children": [
                        {"label": "Sent annual cavalry raids (Bargis) under Bhaskar Pandit into Bengal, causing economic dislocation", "type": "leaf"},
                        {"label": "Treaty of 1751: Forced Nawab Alivardi Khan to cede Odisha and pay Rs. 12 lakhs annually as Chauth", "type": "leaf"}
                    ]}
                ]

        # 8. Economy in the 18th Century Maratha Domains
        elif 'economy' in fl and '18th' in fl:
            if is_hindi:
                return [
                    {"label": "राजस्व प्रशासन और मुद्रीकरण", "type": "branch", "date": "राजस्व", "children": [
                        {"label": "कमविस्दार: पेशवा द्वारा नियुक्त केंद्रीय अधिकारी जो गांवों का राजस्व मूल्यांकन और कर वसूली करते थे", "type": "leaf"},
                        {"label": "तगाई ऋण: कृषि संकट या अकाल के दौरान राज्य द्वारा किसानों को तगाई (कृषि ऋण) दिया जाता था", "type": "leaf"},
                        {"label": "मुद्रीकरण: चांदी के सिक्कों का बढ़ा चलन; साहूकारों (सर्राफों) का बैंकिंग नेटवर्क राजस्व का आधार बना", "type": "leaf"}
                    ]},
                    {"label": "शहरीकरण और व्यापारिक पेठ", "type": "branch", "date": "व्यापार", "children": [
                        {"label": "पेठ निर्माण: पुणे, सतारा और नासिक में नए व्यापारिक क्षेत्रों (पेठ) की स्थापना कर कारीगरों को बसाया", "type": "leaf"},
                        {"label": "अनाज आपूर्ति: बंजारों के माध्यम से अनाज और नमक का पूरे महासंघ में सुगम व्यापार सुनिश्चित किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Revenue System & Credit", "type": "branch", "date": "Revenue", "children": [
                        {"label": "Kamavisdars: Acted as key contract managers appointed by Peshwas to assess and collect rural taxes", "type": "leaf"},
                        {"label": "Tagai Loans: State provided emergency agricultural loans directly to cultivators in times of distress", "type": "leaf"},
                        {"label": "Monetization: Rising currency usage; Gujarati/Marwari Shroffs operated bills of exchange (Hundis)", "type": "leaf"}
                    ]},
                    {"label": "Markets & Urbanization", "type": "branch", "date": "Trade", "children": [
                        {"label": "Peths: Developed structured market suburbs (Peths) in cities, offering tax concessions to artisans", "type": "leaf"},
                        {"label": "Grain mobility: Leveraged Banjara transport networks to ensure cheap supply of food to urban centers", "type": "leaf"}
                    ]}
                ]

        # 9. Social and Cultural Life of Marathas
        elif 'social-and-cultural' in fl:
            if is_hindi:
                return [
                    {"label": "सामाजिक ढांचा और गतिशीलता", "type": "branch", "date": "समाज", "children": [
                        {"label": "ब्राह्मणों का वर्चस्व: चितपावन और देशस्थ ब्राह्मण प्रशासनिक पदों (दफ्तरों) पर पूरी तरह हावी थे", "type": "leaf"},
                        {"label": "कृषक सैनिक: कुनबी कृषक वर्ग मराठा सेना की घुड़सवार इकाई का मुख्य आधार था", "type": "leaf"},
                        {"label": "सामाजिक गतिशीलता: सैन्य अभियानों ने गैर-कुलीन जातियों को शासक वर्ग (जैसे होल्कर, सिंधिया) में बदला", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक एवं वास्तुकला धरोहर", "type": "branch", "date": "संस्कृति", "children": [
                        {"label": "साहित्य: मोदी लिपि का आधिकारिक प्रयोग; बखर (ऐतिहासिक इतिहास) और पोवाड़ा (वीरगाथा गीत) लोकप्रिय थे", "type": "leaf"},
                        {"label": "वास्तुकला: पुणे में विशाल बहु-आंगनों वाले काष्ठ-निर्मित वाड़ा (जैसे शनिवार वाड़ा) का निर्माण हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Social Hierarchy & Mobility", "type": "branch", "date": "Society", "children": [
                        {"label": "Bureaucratic elite: Chitpavan and Deshastha Brahmins filled treasury and administrative offices", "type": "leaf"},
                        {"label": "Peasant-warriors: Kunbi agriculturalists formed the core cavalry (Bargir) of the army", "type": "leaf"},
                        {"label": "Social mobility: Warfare enabled sub-elite pastoralist groups (e.g. Holkars) to attain dynastic status", "type": "leaf"}
                    ]},
                    {"label": "Art & Literature", "type": "branch", "date": "Culture", "children": [
                        {"label": "Literature: Official use of Modi script; growth of Bakhars (chronicles) and Powadas (heroic ballads)", "type": "leaf"},
                        {"label": "Wada Architecture: Constructed multi-courtyard wooden mansions (Wadas), e.g. Shaniwar Wada in Pune", "type": "leaf"}
                    ]}
                ]

        # 10. Maratha Advance into Gujarat and Malwa
        elif 'advance' in fl and ('gujarat' in fl or 'malwa' in fl):
            if is_hindi:
                return [
                    {"label": "मालवा विजय", "type": "branch", "date": "मालवा अभियान", "children": [
                        {"label": "अमझेरा का युद्ध (1728): चिमाजी अप्पा ने मुगल सूबेदार गिरधर बहादुर को हराया; मालवा पर कर वसूलने लगे", "type": "leaf"},
                        {"label": "दुरई सराय की संधि (1738): बाजीराव प्रथम ने मालवा क्षेत्र पर औपचारिक मुगल नायब-सूबेदारी प्राप्त की", "type": "leaf"}
                    ]},
                    {"label": "गुजरात विजय और आंतरिक संघर्ष", "type": "branch", "date": "गुजरात", "children": [
                        {"label": "डभोई का युद्ध (1731): बाजीराव प्रथम ने विद्रोही सेनापति त्रिंबक राव दाभाड़े को हराकर गुजरात राजस्व जीता", "type": "leaf"},
                        {"label": "सूरत पर कर: सूरत और भड़ौच बंदरगाहों से चौथ वसूल कर पश्चिमी व्यापारिक मार्गों पर नियंत्रण किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Conquest of Malwa", "type": "branch", "date": "Malwa", "children": [
                        {"label": "Battle of Amjhera (1728): Chimaji Appa defeated Mughal governor Girdhar Bahadur, securing Malwa taxes", "type": "leaf"},
                        {"label": "Treaty of Durai Sarai (1738): Mughal court formally ceded governorship of Malwa to Peshwa Baji Rao I", "type": "leaf"}
                    ]},
                    {"label": "Gujarat Campaign & Friction", "type": "branch", "date": "Gujarat", "children": [
                        {"label": "Battle of Dabhai (1731): Baji Rao I defeated Senapati Dabhade, ending local challenge to his authority", "type": "leaf"},
                        {"label": "Surat Customs: Imposed Chauth on Surat and Cambay trade hubs, securing rich customs tax revenues", "type": "leaf"}
                    ]}
                ]

        # 11. Marathas and Nizam-ul-Mulk
        elif 'nizam-ul-mulk' in fl or 'nizam' in fl:
            if is_hindi:
                return [
                    {"label": "पालखेड का युद्ध", "type": "branch", "date": "1728 ई.", "children": [
                        {"label": "रणनीति: बाजीराव प्रथम ने निजाम की भारी तोपों के मुकाबले गतिशीलता का उपयोग किया", "type": "leaf"},
                        {"label": "शेवगांव की संधि: निजाम ने शाहू को दक्कन के वैध छत्रपति के रूप में माना; चौथ देने पर सहमति दी", "type": "leaf"}
                    ]},
                    {"label": "भोपाल का युद्ध", "type": "branch", "date": "1737 ई.", "children": [
                        {"label": "घेराबंदी: भोपाल में मराठों ने निजाम की सेना को चारों ओर से घेर लिया और रसद मार्ग काट दिया", "type": "leaf"},
                        {"label": "दुरई सराय की संधि: निजाम ने मुगलों की ओर से मराठों को मालवा और 50 लाख रुपये हर्जाना दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Battle of Palkhed", "type": "branch", "date": "1728 AD", "children": [
                        {"label": "Tactics: Baji Rao I bypassed Nizam's heavy artillery through rapid cavalry encirclement", "type": "leaf"},
                        {"label": "Treaty of Shevgaon: Nizam recognized Shahu's claims; agreed to pay arrears of Chauth in Deccan", "type": "leaf"}
                    ]},
                    {"label": "Battle of Bhopal", "type": "branch", "date": "1737 AD", "children": [
                        {"label": "The Siege: Peshwa surrounded Nizam's army at Bhopal, cutting off all supplies and reinforcements", "type": "leaf"},
                        {"label": "Treaty of Durai Sarai: Nizam ceded entire Malwa to Marathas and secured Rs. 50 lakhs war indemnity", "type": "leaf"}
                    ]}
                ]

        # 12. Maratha Advance into Doab & Punjab: First Phase
        elif 'advance' in fl and 'first-phase' in fl:
            if is_hindi:
                return [
                    {"label": "दोआब में विस्तार", "type": "branch", "date": "1741-52 ई.", "children": [
                        {"label": "दरबारी राजनीति: मुगल वजीर सफदरजंग के निमंत्रण पर मराठा सेनाओं ने रोहिल्ला अफगानों को दोआब में हराया", "type": "leaf"},
                        {"label": "राजपूत राज्यों पर कर: जयपुर, जोधपुर और मेवाड़ के आंतरिक उत्तराधिकार युद्धों में मध्यस्थता कर चौथ ली", "type": "leaf"}
                    ]},
                    {"label": "अहमदिया संधि (1752)", "type": "branch", "date": "1752 ई.", "children": [
                        {"label": "मुगलों और मराठों के बीच सुरक्षा समझौता; मराठों को पंजाब, सिंध और दोआब की चौथ वसूलने का अधिकार मिला", "type": "leaf"},
                        {"label": "मराठों ने अहमद शाह अब्दाली के विदेशी हमलों से दिल्ली के मुगल सिंहासन की रक्षा करने का वचन दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Doab Interventions", "type": "branch", "date": "1741-52 AD", "children": [
                        {"label": "Court alignments: Invited by Mughal Wazir Safdarjung to defeat Rohilla Afghans in the Doab region", "type": "leaf"},
                        {"label": "Rajput tributes: Extracted heavy cash indemnities by intervening in succession wars of Amber & Marwar", "type": "leaf"}
                    ]},
                    {"label": "Ahmadiyya Treaty", "type": "branch", "date": "1752 AD", "children": [
                        {"label": "Defense pact: Mughals ceded Chauth rights of Punjab, Multan, and Sindh to the Peshwa in exchange for security", "type": "leaf"},
                        {"label": "Marathas pledged to protect the Mughal Emperor from foreign threats, specifically Ahmad Shah Abdali", "type": "leaf"}
                    ]}
                ]

        # 13. Maratha Advance into Doab & Punjab: Second Phase
        elif 'advance' in fl and 'second-phase' in fl:
            if is_hindi:
                return [
                    {"label": "अटक तक विस्तार और लाहौर विजय", "type": "branch", "date": "1752-61 ई.", "children": [
                        {"label": "लाहौर विजय: रघुनाथ राव और मल्हार राव होल्कर ने लाहौर पर अधिकार किया और अटक दुर्ग जीता (1758)", "type": "leaf"},
                        {"label": "अदीना बेग की नियुक्ति: पंजाब में अदीना बेग खान को मराठा करदाता गवर्नर नियुक्त किया", "type": "leaf"},
                        {"label": "तैमूर शाह का निष्कासन: अहमद शाह अब्दाली के बेटे तैमूर शाह को पंजाब से बाहर खदेड़ दिया", "type": "leaf"}
                    ]},
                    {"label": "अब्दाली से सीधा टकराव", "type": "branch", "date": "युद्ध का कारण", "children": [
                        {"label": "पंजाब में अब्दाली के क्षेत्रों पर सीधा कब्जा करने से अब्दाली ने मुगलों की रक्षा संधि को तोड़ा", "type": "leaf"},
                        {"label": "इस आक्रामक विस्तार ने अब्दाली को रोहिल्ला प्रमुखों के साथ मिलकर दिल्ली पर आक्रमण के लिए उकसाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Punjab Expedition & Attock", "type": "branch", "date": "1752-61 AD", "children": [
                        {"label": "Raghunath Rao captured Lahore and planted the saffron flag at Attock Fort near the Khyber Pass in 1758", "type": "leaf"},
                        {"label": "Vassal governor: Appointed Adina Beg Khan as the administrator of Punjab, bound to pay annual tribute", "type": "leaf"},
                        {"label": "Afghan expulsion: Forced Prince Timur Shah (Abdali's son and viceroy) to retreat across the Indus", "type": "leaf"}
                    ]},
                    {"label": "Clash with Abdali", "type": "branch", "date": "Consequences", "children": [
                        {"label": "Occupying Punjab violated Abdali's sphere of influence, prompting him to launch a counter-invasion", "type": "leaf"},
                        {"label": "Pushed Maratha forces into a direct military confrontation, culminating in the 1761 Panipat Campaign", "type": "leaf"}
                    ]}
                ]

        # 14. Maratha Policy of Expansion (Swarajya vs Mughlai)
        elif 'policy' in fl and 'expansion' in fl:
            if is_hindi:
                return [
                    {"label": "स्वराज्य बनाम मुगलाई का संक्रमण", "type": "branch", "date": "अवधारणा", "children": [
                        {"label": "स्वराज्य: शिवाजी महाराज द्वारा स्थापित मराठा गृहक्षेत्र, जहाँ स्थायी सुशासन प्रमुख था", "type": "leaf"},
                        {"label": "मुगलाई: मुगल शासित बाहरी क्षेत्र, जहाँ से केवल चौथ और सरदेशमुखी (कर संग्रह) वसूला जाता था", "type": "leaf"},
                        {"label": "परिवर्तन: महासंघ के काल में नीति गृह रक्षा से बदलकर बाह्य क्षेत्रों से कर दोहन पर आधारित हुई", "type": "leaf"}
                    ]},
                    {"label": "हिंदू-पद-पादशाही का आदर्श", "type": "branch", "date": "विचारधारा", "children": [
                        {"label": "वैचारिक लक्ष्य: बाजीराव प्रथम ने हिंदू शासकों को संगठित कर मुगलों के स्थान पर हिंदू संप्रभुता का नारा दिया", "type": "leaf"},
                        {"label": "व्यावहारिक पतन: बाद के पेशवाओं ने राजपूतों से भारी कर वसूल कर इस वैचारिक एकता को नष्ट कर दिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Swarajya vs Mughlai Shift", "type": "branch", "date": "Concept", "children": [
                        {"label": "Swarajya: Core homeland established by Shivaji, governed directly with structured civil laws", "type": "leaf"},
                        {"label": "Mughlai: Outer Mughal-ruled provinces subject to taxation (Chauth) without administrative duty", "type": "leaf"},
                        {"label": "Evolution: Transited from a defensive regional state into a tribute-extracting loose confederacy", "type": "leaf"}
                    ]},
                    {"label": "Hindu-Pad-Padshahi Ideology", "type": "branch", "date": "Ideology", "children": [
                        {"label": "Cultural appeal: Baji Rao I used the call of Hindu sovereignty to rally North Indian Rajput elites", "type": "leaf"},
                        {"label": "Pragmatic decline: Later Peshwas dropped ideological alliances, treating Rajputs as tribute-paying vassals", "type": "leaf"}
                    ]}
                ]

        # Fallback for Marathas
        else:
            if is_hindi:
                return [
                    {"label": "मराठा साम्राज्य सामान्य", "type": "branch", "date": "मराठा शासन", "children": [
                        {"label": "छत्रपति शिवाजी द्वारा स्थापित; पेशवाओं के अधीन महासंघ के रूप में विस्तार", "type": "leaf"},
                        {"label": "चौथ और सरदेशमुखी वित्तीय प्रणाली के रीढ़ थे; छापामार युद्ध मुख्य ताकत थी", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Maratha Empire Overview", "type": "branch", "date": "Overview", "children": [
                        {"label": "Founded by Shivaji Maharaj; transitioned to a powerful confederacy under Pune Peshwas", "type": "leaf"},
                        {"label": "Relied on mobile light cavalry and fiscal demands (Chauth/Sardeshmukhi) to sustain expansion", "type": "leaf"}
                    ]}
                ]
    # =========================================================================
    # G. EARLY MEDIEVAL PERIOD (750-1200) & DYNASTIES
    # =========================================================================
    elif 'early-medieval-period' in cat_lower or 'palas' in fl or 'pratiharas' in fl or 'tripartite' in fl or 'feudalism' in fl or 'senas' in fl or 'yadavas' in fl or 'cholas' in fl or 'rashtrakutas' in fl or 'rajputs' in fl or 'cheras' in fl or 'south-east-asia' in fl:
        
        # 1. The Palas
        if 'palas' in fl or 'pala' in fl:
            if is_hindi:
                return [
                    {"label": "राजवंश शासन", "type": "branch", "date": "750-1174 ई.", "children": [
                        {"label": "गोपाल (750 ई.): मात्स्यन्याय अराजकता को समाप्त करने के लिए स्थानीय प्रमुखों द्वारा निर्वाचित संस्थापकीय शासक", "type": "leaf"},
                        {"label": "धर्मपाल (770-810 ई.): पाल साम्राज्य का विस्तार किया; कन्नौज पर अधिकार के लिए त्रिपक्षीय संघर्ष शुरू किया", "type": "leaf"}
                    ]},
                    {"label": "बौद्ध धर्म और कला संरक्षण", "type": "branch", "date": "संस्कृति", "children": [
                        {"label": "महाविहार: धर्मपाल ने प्रसिद्ध विक्रमशिला विश्वविद्यालय और सोमपुर महाविहार की स्थापना की", "type": "leaf"},
                        {"label": "कांस्य कला: धीमान और वितपाल के अधीन नालंदा कांस्य मूर्तिकला और पांडुलिपि चित्रकला का विकास हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Dynastic Rule", "type": "branch", "date": "750-1174 AD", "children": [
                        {"label": "Gopala (750 AD): Elected by regional chiefs to end the internal anarchy known as Matsyanyaya", "type": "leaf"},
                        {"label": "Dharmapala (770-810 AD): Expanded domains; initiated the Tripartite struggle for Kannauj", "type": "leaf"}
                    ]},
                    {"label": "Buddhism & Art Patronage", "type": "branch", "date": "Culture", "children": [
                        {"label": "Mahaviharas: Founded the Vikramashila University and the Somapura Mahavihara in Bengal", "type": "leaf"},
                        {"label": "Bronze casting: Famed school of metal art under Dhiman and Vitapala; manuscript paintings flourished", "type": "leaf"}
                    ]}
                ]

        # 2. The Pratiharas
        elif 'pratiharas' in fl or 'pratihara' in fl:
            if is_hindi:
                return [
                    {"label": "गुर्जर-प्रतिहार", "type": "branch", "date": "8वीं-11वीं सदी", "children": [
                        {"label": "नागभट्ट प्रथम (730-760 ई.): राजवंश की नींव रखी; सिंध से होने वाले अरबों के आक्रमणों को रोका", "type": "leaf"},
                        {"label": "मिहिर भोज (836-885 ई.): सबसे महान शासक; विष्णु भक्त, 'आदिवराह' और 'प्रभास' की उपाधि ली", "type": "leaf"}
                    ]},
                    {"label": "कला और साहित्य", "type": "branch", "date": "योगदान", "children": [
                        {"label": "वास्तुकला: ओसियां (राजस्थान) में नागर शैली के अलंकृत पत्थरों वाले मंदिरों का निर्माण कराया", "type": "leaf"},
                        {"label": "साहित्य: राजशेखर (दरबारी कवि) जिन्होंने काव्यमीमांसा, कर्पूरमंजरी और बालरामायण की रचना की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Gurjara-Pratiharas", "type": "branch", "date": "8th-11th Century AD", "children": [
                        {"label": "Nagabhata I (730-760 AD): Founded the dynasty, successfully checking Arab expansion from Sindh", "type": "leaf"},
                        {"label": "Mihir Bhoja (836-885 AD): Greatest ruler; devotee of Vishnu, assuming the title 'Adivaraha'", "type": "leaf"}
                    ]},
                    {"label": "Art & Literature", "type": "branch", "date": "Legacy", "children": [
                        {"label": "Temples: Promoted Nagara style; constructed the temple complex at Osian in Rajasthan", "type": "leaf"},
                        {"label": "Patronage: Protected the Sanskrit poet Rajasekhara, author of Kavyamimamsa and Karpuramanjari", "type": "leaf"}
                    ]}
                ]

        # 3. The Tripartite Conflict
        elif 'tripartite' in fl:
            if is_hindi:
                return [
                    {"label": "कन्नौज का संघर्ष", "type": "branch", "date": "8वीं-10वीं सदी", "children": [
                        {"label": "उद्देश्य: गंगा घाटी के समृद्ध कन्नौज शहर पर नियंत्रण, जो हर्ष के बाद साम्राज्यवादी संप्रभुता का प्रतीक बना", "type": "leaf"},
                        {"label": "मुख्य प्रतिद्वंद्वी: बंगाल के पाल, पश्चिमी भारत के गुर्जर-प्रतिहार और दक्कन के राष्ट्रकूट", "type": "leaf"}
                    ]},
                    {"label": "सामरिक परिणाम", "type": "branch", "date": "परिणाम", "children": [
                        {"label": "शक्तियों का ह्रास: लगातार 200 वर्षों के संघर्ष ने तीनों राजवंशों के वित्तीय और सैन्य संसाधनों को खत्म कर दिया", "type": "leaf"},
                        {"label": "अंतिम विजय: गुर्जर-प्रतिहारों ने अंतिम दौर में कन्नौज पर अपना स्थायी नियंत्रण स्थापित किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Struggle for Kannauj", "type": "branch", "date": "8th-10th Century AD", "children": [
                        {"label": "The Prize: Control over Kannauj in the Gangetic plain, the symbol of imperial power post-Harsha", "type": "leaf"},
                        {"label": "Rivals: Triangular warfare between the Palas of Bengal, Gurjara-Pratiharas, and Deccan Rashtrakutas", "type": "leaf"}
                    ]},
                    {"label": "Strategic Impact", "type": "branch", "date": "Impact", "children": [
                        {"label": "Exhaustion: Two centuries of battles depleted armies and treasuries, leading to fragmentations", "type": "leaf"},
                        {"label": "Final control: The Gurjara-Pratiharas established control over Kannauj before their ultimate decline", "type": "leaf"}
                    ]}
                ]

        # 4. Cholas Dynasty
        elif 'cholas' in fl or 'chola' in fl:
            if is_hindi:
                return [
                    {"label": "नौसैनिक और साम्राज्यीय विस्तार", "type": "branch", "date": "द्रविड़ विस्तार", "children": [
                        {"label": "राजराज प्रथम: श्रीलंका के उत्तरी भाग को जीता; हिंद महासागर में मालदीव पर नौसैनिक अभियान चलाया", "type": "leaf"},
                        {"label": "राजेंद्र प्रथम: गंगा घाटी पर विजय प्राप्त कर गंगैकोंडचोलपुरम राजधानी बसाई; कदारम (मलय) पर नौसैनिक आक्रमण किया", "type": "leaf"}
                    ]},
                    {"label": "उत्तरमेरूर शिलालेख और स्थानीय प्रशासन", "type": "branch", "date": "प्रशासन", "children": [
                        {"label": "सभा चुनाव: उत्तरमेरूर शिलालेख (919/921 ई.) ग्रामीण स्वशासन (सभा) और चुनाव योग्यता को स्पष्ट करता है", "type": "leaf"},
                        {"label": "नायडू और वरियर: प्रांतों को वलनाडु और नाडु में विभाजित किया; कार्यकारी समितियां 'वरियम' कहलाती थीं", "type": "leaf"}
                    ]},
                    {"label": "चोल वास्तुकला और कांस्य मूर्तियां", "type": "branch", "date": "संस्कृति", "children": [
                        {"label": "बृहदीश्वर मंदिर: तंजावुर में राजराज प्रथम द्वारा निर्मित द्रविड़ विमान शैली का उत्कृष्ट मंदिर", "type": "leaf"},
                        {"label": "नटराज कांस्य: लुप्त मोम तकनीक (Lost-Wax) से निर्मित शिव की प्रसिद्ध नटराज कांस्य मूर्तियां", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Naval & Imperial Expansion", "type": "branch", "date": "Expansion", "children": [
                        {"label": "Rajaraja I: Annexed northern Sri Lanka; launched naval campaigns to Maldives to control trade routes", "type": "leaf"},
                        {"label": "Rajendra I: Led expedition to Ganges, building Gangaikondacholapuram; sent fleet to Kadaram (Southeast Asia)", "type": "leaf"}
                    ]},
                    {"label": "Local Governance & Inscriptions", "type": "branch", "date": "Uttaramerur", "children": [
                        {"label": "Uttaramerur Inscription: Details qualifications, disqualifications, and lottery system (Kudavolai) for Sabha elections", "type": "leaf"},
                        {"label": "Variyams: Village committees managing tanks, gardens, and temples, showing high decentralization", "type": "leaf"}
                    ]},
                    {"label": "Chola Art & Bronze Work", "type": "branch", "date": "Art", "children": [
                        {"label": "Brihadisvara Temple: Monumental Dravidian style vimana temple at Thanjavur built by Rajaraja I", "type": "leaf"},
                        {"label": "Nataraja Bronzes: Masterpieces of lost-wax casting technique representing cosmic dance of Shiva", "type": "leaf"}
                    ]}
                ]

        # 5. Rashtrakutas
        elif 'rashtrakutas' in fl or 'rashtrakuta' in fl:
            if is_hindi:
                return [
                    {"label": "मान्यखेट के राष्ट्रकूट", "type": "branch", "date": "753-982 ई.", "children": [
                        {"label": "स्थापना: दंतिदुर्ग (753 ई.) ने चालुक्यों को हराकर की; मान्यखेट को प्रशासनिक राजधानी बनाया", "type": "leaf"},
                        {"label": "अमोघवर्ष प्रथम: जैन धर्म के अनुयायी; कन्नड़ ग्रंथ 'कविराजमार्ग' और संस्कृत 'प्रश्नोत्तरमालिका' की रचना की", "type": "leaf"}
                    ]},
                    {"label": "कला और स्थापत्य", "type": "branch", "date": "स्मारक", "children": [
                        {"label": "एलोरा कैलाश मंदिर: कृष्ण प्रथम के अधीन निर्मित विशाल एकाश्म पाषाण मंदिर वास्तुकला", "type": "leaf"},
                        {"label": "एलीफेंटा गुफाएं: कोंकण द्वीप पर शैव गुफा मंदिर, जहाँ प्रसिद्ध 'त्रिमूर्ति' सदाशिव की प्रतिमा है", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Manyakheta Hegemony", "type": "branch", "date": "753-982 AD", "children": [
                        {"label": "Establishment: Dantidurga overthrew Badami Chalukyas, making Manyakheta the dynastic capital", "type": "leaf"},
                        {"label": "Amoghavarsha I: Famous patron of Jainism; wrote Kavirajamarga (earliest Kannada work on poetics)", "type": "leaf"}
                    ]},
                    {"label": "Ellora & Elephanta Monuments", "type": "branch", "date": "Monuments", "children": [
                        {"label": "Kailash Temple: Monolithic rock-cut Shiva temple at Ellora carved out under Krishna I", "type": "leaf"},
                        {"label": "Elephanta Caves: Rock-cut cave shrines on Gharapuri island featuring the famous Maheshmurti Trimurti", "type": "leaf"}
                    ]}
                ]

        # 6. The Rajputs
        elif 'rajputs' in fl or 'rajput' in fl:
            if is_hindi:
                return [
                    {"label": "अग्निकुल उत्पत्ति और कुलीन वंश", "type": "branch", "date": "उत्पत्ति", "children": [
                        {"label": "अग्निकुल सिद्धांत: पृथ्वीराज रासो के अनुसार वशिष्ठ के आबू पर्वत यज्ञ से चार कुलों की उत्पत्ति हुई", "type": "leaf"},
                        {"label": "प्रमुख वंश: अजमेर के चौहान, मालवा के परमार, कन्नौज के गहरवाल और बुंदेलखंड के चंदेल", "type": "leaf"}
                    ]},
                    {"label": "राजपूत कला और वास्तुकला", "type": "branch", "date": "स्थापत्य", "children": [
                        {"label": "खजुराहो मंदिर: चंदेल शासकों द्वारा निर्मित मंदिर; कंदारिया महादेव मंदिर प्रमुख है", "type": "leaf"},
                        {"label": "दुर्ग वास्तुकला: चित्तौड़गढ़, रणथंभौर और ग्वालियर जैसे अभेद्य सैन्य पहाड़ी दुर्गों का निर्माण", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Origins & Clans", "type": "branch", "date": "Origins", "children": [
                        {"label": "Agnikula Myth: Bardic tradition of origin from fire-altar at Mount Abu; listed in Prithviraj Raso", "type": "leaf"},
                        {"label": "Major Clans: Chauhans of Shakambhari, Paramaras of Dhara, and Chandelas of Jejakabhukti", "type": "leaf"}
                    ]},
                    {"label": "Art & Hill Forts", "type": "branch", "date": "Architecture", "children": [
                        {"label": "Khajuraho: Temple group built by Chandela rulers, famous for the Kandariya Mahadeva Temple", "type": "leaf"},
                        {"label": "Hill Forts: Strategic military architecture of Chittorgarh, Gwalior, and Ranthambore", "type": "leaf"}
                    ]}
                ]

        # 7. Indian Feudalism
        elif 'feudalism' in fl:
            if is_hindi:
                return [
                    {"label": "सामंतवाद का उदय", "type": "branch", "date": "सामंत प्रणाली", "children": [
                        {"label": "भूमि अनुदान: ब्राह्मणों और प्रशासनिक अधिकारियों को लगान-मुक्त भूमि (अग्रहार) देने से राजनीतिक सत्ता विभाजित हुई", "type": "leaf"},
                        {"label": "अधिकारों का स्थानांतरण: भूमि अनुदान के साथ प्रशासनिक, न्यायिक और कर वसूली अधिकार दिए गए", "type": "leaf"}
                    ]},
                    {"label": "सामाजिक-आर्थिक प्रभाव", "type": "branch", "date": "प्रभाव", "children": [
                        {"label": "कृषि का संकुचन: लंबी दूरी के व्यापार में गिरावट, सिक्कों की कमी और आत्मनिर्भर ग्रामीण व्यवस्था का उदय", "type": "leaf"},
                        {"label": "उप-सामंतवाद: मध्यस्थ सामंतों के विभिन्न स्तर उभरे, जिससे किसानों पर शोषण बढ़ा", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Rise of Feudalism", "type": "branch", "date": "Land Grants", "children": [
                        {"label": "Agraharas: Secular and religious land grants transferred fiscal and judicial rights to intermediaries", "type": "leaf"},
                        {"label": "Decentralization: Samantas emerged as hereditary barons with their own armed levies and territories", "type": "leaf"}
                    ]},
                    {"label": "Socio-Economic Impact", "type": "branch", "date": "Impact", "children": [
                        {"label": "Commercial drop: Decline in coinage, decay of urban guilds, and growth of self-sufficient villages", "type": "leaf"},
                        {"label": "Sub-infeudation: Layering of landlords between king and ryot, increasing rent burden on peasantry", "type": "leaf"}
                    ]}
                ]

        # 8. Administration (Early Medieval)
        elif 'administration' in fl:
            if is_hindi:
                return [
                    {"label": "विकेंद्रीकृत राजशाही", "type": "branch", "date": "प्रशासन", "children": [
                        {"label": "राजा: नाममात्र की सर्वोच्च उपाधियां (परमभट्टारक) लीं; सैन्य सहायता के लिए सामंतों पर निर्भर रहे", "type": "leaf"},
                        {"label": "प्रशासनिक इकाइयाँ: भुक्ति (प्रांत), विषय (जिला) और ग्राम (गाँव); गाँवों का शासन ग्रामपतियों के अधीन", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Decentralized Monarchy", "type": "branch", "date": "Administration", "children": [
                        {"label": "Imperial titles: Kings assumed titles like Maharajadhiraja but depended on feudal Samantas for military aid", "type": "leaf"},
                        {"label": "Territorial divisions: Bhuktis (provinces) under Uparikas, Vishayas (districts) under Vishayapatis", "type": "leaf"}
                    ]}
                ]

        # 9. Art and Architecture (Early Medieval)
        elif 'art-and-architecture' in fl:
            if is_hindi:
                return [
                    {"label": "मंदिर निर्माण की शैलियाँ", "type": "branch", "date": "वास्तुकला", "children": [
                        {"label": "नागर शैली: उत्तर भारत में रेखीय शिखरों, गर्भगृह और मंडप वाले मंदिरों का विकास (जैसे खजुराहो)", "type": "leaf"},
                        {"label": "द्रविड़ शैली: दक्षिण भारत में पिरामिडीय विमानों, रथों और विशाल गोपुरमो का विकास (जैसे महाबलीपुरम)", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Temple Architectural Styles", "type": "branch", "date": "Architecture", "children": [
                        {"label": "Nagara style: Curved shikharas, garbhagrihas, and mandapas popular in the north (e.g. Khajuraho)", "type": "leaf"},
                        {"label": "Dravida style: Pyramidal vimanas and pillared halls in the south (e.g. Shore Temple, Mahabalipuram)", "type": "leaf"}
                    ]}
                ]

        # 10. Economy (Early Medieval)
        elif 'economy' in fl:
            if is_hindi:
                return [
                    {"label": "कृषि का विस्तार", "type": "branch", "date": "अर्थव्यवस्था", "children": [
                        {"label": "अरघट्ट (नहर सिंचाई): सिंचाई साधनों के विकास से कृषि उत्पादन में वृद्धि हुई", "type": "leaf"},
                        {"label": "भूमि सुधार: बंजर भूमि को कृषि योग्य बनाया गया; मंदिर भूमियों को विशेष कर-मुक्त रियायतें दी गईं", "type": "leaf"}
                    ]},
                    {"label": "श्रेणी और व्यापार", "type": "branch", "date": "व्यापार", "children": [
                        {"label": "मणिग्रामम और नानादेसी: दक्षिण भारत की प्रमुख व्यापारी श्रेणियां जो समुद्री और विदेश व्यापार देखती थीं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Agrarian Development", "type": "branch", "date": "Economy", "children": [
                        {"label": "Araghatta: Growth of Persian wheel irrigation systems led to intensive agricultural production", "type": "leaf"},
                        {"label": "Land reclamation: Forest clearances and conversions of wasteland funded by temple land grants", "type": "leaf"}
                    ]},
                    {"label": "Merchant Guilds", "type": "branch", "date": "Trade", "children": [
                        {"label": "South Indian Guilds: Nanadesi and Manigramam controlled inter-regional and overseas Indian Ocean trade", "type": "leaf"}
                    ]}
                ]

        # 11. Society and Culture (Early Medieval)
        elif 'society-and-culture' in fl:
            if is_hindi:
                return [
                    {"label": "सामाजिक परिवर्तन", "type": "branch", "date": "समाज", "children": [
                        {"label": "जाति गुणा: जनजातियों के विलय और नई उप-जातियों के उभरने से जातियों की संख्या बढ़ी", "type": "leaf"},
                        {"label": "कायस्थ: प्रशासनिक कार्य और भू-अभिलेखों के लेखक के रूप में कायस्थ जाति का उदय हुआ", "type": "leaf"}
                    ]},
                    {"label": "धार्मिक भक्ति आंदोलन", "type": "branch", "date": "धर्म", "children": [
                        {"label": "अलवार और नयनार: दक्षिण भारत में शैव और वैष्णव संतों ने लोक भाषा में भक्ति आंदोलन फैलाया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Social Proliferation & Castes", "type": "branch", "date": "Society", "children": [
                        {"label": "Sub-castes: Proliferation of Jatis through assimilation of tribal and immigrant groups", "type": "leaf"},
                        {"label": "Kayasthas: Emerged as a caste of professional scribes keeping land registers and decrees", "type": "leaf"}
                    ]},
                    {"label": "Bhakti Origins", "type": "branch", "date": "Culture", "children": [
                        {"label": "Alvars & Nayanars: Tamil devotional saints spearheading popular Vaishnava/Shaiva movements", "type": "leaf"}
                    ]}
                ]

        # 12. Contact with South East Asia
        elif 'south-east-asia' in fl:
            if is_hindi:
                return [
                    {"label": "सांस्कृतिक विस्तार", "type": "branch", "date": "विस्तार", "children": [
                        {"label": "बौद्ध-हिंदू प्रसार: शैलेंद्र और श्रीविजय साम्राज्यों के साथ सांस्कृतिक संबंध; हिंदू प्रतीकों का उपयोग", "type": "leaf"},
                        {"label": "महाकाव्य: रामायण और महाभारत का दक्षिण-पूर्व एशियाई कठपुतली (वायंग कुलीत) में अनुकूलन हुआ", "type": "leaf"}
                    ]},
                    {"label": "महान स्मारक", "type": "branch", "date": "वास्तुकला", "children": [
                        {"label": "अंकोरवाट (कंबोडिया): सूर्यवर्मन द्वितीय द्वारा निर्मित विशाल हिंदू (विष्णु) मंदिर परिसर", "type": "leaf"},
                        {"label": "बोरोबुदुर (जावा): शैलेंद्र राजवंश के अधीन निर्मित विशाल महायान बौद्ध स्तूप स्मारक", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Cultural Diffusion", "type": "branch", "date": "Diffusion", "children": [
                        {"label": "Hindu-Buddhist spread: Maritime ties with Srivijaya and Sailendra empires; Sanskrit influence", "type": "leaf"},
                        {"label": "Epics: Adaptation of Ramayana/Mahabharata in Javanese wayang kulit shadow puppet plays", "type": "leaf"}
                    ]},
                    {"label": "Monumental Architecture", "type": "branch", "date": "Monuments", "children": [
                        {"label": "Angkor Wat: Built by Suryavarman II in Cambodia, the world's largest religious monument (Vishnu)", "type": "leaf"},
                        {"label": "Borobudur: Massive 9th-century Buddhist temple in Java built under the Sailendra dynasty", "type": "leaf"}
                    ]}
                ]

        # 13. The Cheras
        elif 'cheras' in fl or 'chera' in fl:
            if is_hindi:
                return [
                    {"label": "केरल के चेर", "type": "branch", "date": "महोदयपुरम", "children": [
                        {"label": "महोदयपुरम चेर: कुलशेखर राजवंश के अधीन modern केरल क्षेत्र पर शासन किया", "type": "leaf"},
                        {"label": "समुद्री व्यापार: रोमन, यहूदी, ईसाई और अरब व्यापारियों के साथ पश्चिमी तट से सक्रिय व्यापार संबंध", "type": "leaf"}
                    ]},
                    {"label": "सांस्कृतिक योगदान", "type": "branch", "date": "संस्कृति", "children": [
                        {"label": "कुडियाट्टम: संस्कृत थियेटर ड्रामा जिसे शाही संरक्षण प्राप्त था", "type": "leaf"},
                        {"label": "मलयालम: संस्कृत और तमिल के प्रभाव से एक पृथक साहित्यिक भाषा के रूप में मलयालम का विकास", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Cheras of Mahodayapuram", "type": "branch", "date": "Kerala", "children": [
                        {"label": "Mahodayapuram Cheras: Ruled modern Kerala under the Kulasekhara dynasty", "type": "leaf"},
                        {"label": "Spice trade: Maintained active maritime links with West Asian, Roman, and Jewish merchants", "type": "leaf"}
                    ]},
                    {"label": "Cultural Heritage", "type": "branch", "date": "Culture", "children": [
                        {"label": "Koodiyattam: Traditional Sanskrit temple theatre patronized by Chera royalty", "type": "leaf"},
                        {"label": "Language: Separation of Malayalam from Tamil as a distinct script and literary tongue", "type": "leaf"}
                    ]}
                ]

        # 14. The Senas
        elif 'senas' in fl or 'sena' in fl:
            if is_hindi:
                return [
                    {"label": "सेन राजवंश", "type": "branch", "date": "बंगाल", "children": [
                        {"label": "स्थापना: सामंतसेन द्वारा स्थापित; पालों के पतन के बाद बंगाल में प्रभुत्व स्थापित किया", "type": "leaf"},
                        {"label": "लक्ष्मणसेन: सबसे महान शासक, जिन्होंने साहित्य का संरक्षण किया; बख्तियार खिलजी के अचानक हमले से पतन हुआ", "type": "leaf"}
                    ]},
                    {"label": "साहित्यिक योगदान", "type": "branch", "date": "साहित्य", "children": [
                        {"label": "जयदेव: लक्ष्मणसेन के दरबारी कवि जिन्होंने अमर संस्कृत ग्रंथ 'गीत गोविंद' की रचना की", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Sena Dynasty of Bengal", "type": "branch", "date": "Bengal", "children": [
                        {"label": "Establishment: Displaced Palas in Bengal; founded by Samantasena of Karnataka origin", "type": "leaf"},
                        {"label": "Lakshmanasena: Peak patronage of letters; capital Nadiya fell to Bakhtiyar Khilji's cavalry raid", "type": "leaf"}
                    ]},
                    {"label": "Literary Achievements", "type": "branch", "date": "Literature", "children": [
                        {"label": "Jayadeva: Royal court poet who compiled the famous lyric poem Gita Govinda", "type": "leaf"}
                    ]}
                ]

        # 15. The Yadavas
        elif 'yadavas' in fl or 'yadava' in fl:
            if is_hindi:
                return [
                    {"label": "देवगिरि के यादव", "type": "branch", "date": "दक्कन", "children": [
                        {"label": "स्थापना: भिल्लम पंचम ने देवगिरि (दौलताबाद) को राजधानी बनाकर स्वतंत्र राजवंश की स्थापना की", "type": "leaf"},
                        {"label": "ज्ञानेश्वरी: संत ज्ञानेश्वर ने मराठी में प्रसिद्ध भगवद्गीता टीका 'ज्ञानेश्वरी' की रचना की", "type": "leaf"},
                        {"label": "पतन: अलाउद्दीन खिलजी और बाद में मलिक काफूर के आक्रमणों ने इस राज्य का अंत किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Yadavas of Devagiri", "type": "branch", "date": "Deccan", "children": [
                        {"label": "Establishment: Bhillama V made Devagiri (Daulatabad) the capital, asserting independence", "type": "leaf"},
                        {"label": "Marathi literature: Patronized early Marathi writers; Sant Jnaneshwar compiled the Jnaneshwari", "type": "leaf"},
                        {"label": "Conquest: Defeated by Alauddin Khilji's raids, leading to direct Delhi Sultanate control", "type": "leaf"}
                    ]}
                ]

        # Fallback for Early Medieval
        else:
            if is_hindi:
                return [
                    {"label": "पूर्व मध्यकालीन भारत", "type": "branch", "date": "750-1200 ई.", "children": [
                        {"label": "हर्ष के पतन के बाद उत्तर भारत में राजनीतिक विखंडन और नए राजवंशों का उदय", "type": "leaf"},
                        {"label": "सामंतवाद के विकास, व्यापार में गिरावट और क्षेत्रीय भाषाओं के उदय का काल", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Early Medieval India", "type": "branch", "date": "750-1200 AD", "children": [
                        {"label": "Period of political fragmentation post-Harsha, marked by regional kingdoms", "type": "leaf"},
                        {"label": "Characterized by growth of feudal land tenures and regional language developments", "type": "leaf"}
                    ]}
                ]

    # =========================================================================
    # H. BAHMANI KINGDOM & SUCCESSOR STATES
    # =========================================================================
    elif 'bahmani-kingdom' in cat_lower or 'bahmani' in fl:
        
        # 1. Bahmani Art and Architecture
        if 'architecture' in fl or 'art' in fl:
            if is_hindi:
                return [
                    {"label": "भारत-फारसी वास्तुकला", "type": "branch", "date": "गुलबर्गा व बीदर", "children": [
                        {"label": "संश्लेषण: फारसी मेहराबों/गुंबदों को स्थानीय दक्कनी पाषाण नक्काशी शैली के साथ मिश्रित किया", "type": "leaf"},
                        {"label": "गुलबर्गा जामा मस्जिद: आंगन विहीन मस्जिद, जिसमें एक विशाल गुंबद और 63 छोटे गुंबद बने हैं", "type": "leaf"},
                        {"label": "महमूद गवां का मदरसा: बीदर में निर्मित तीन मंजिला विशाल फारसी शैली का मदरसा, जिसमें चमकीली टाइलें हैं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Indo-Persian Synthesis", "type": "branch", "date": "Architecture", "children": [
                        {"label": "Stylistic blend: Merged West Asian domes/arches with Deccani masonry and granite detailing", "type": "leaf"},
                        {"label": "Gulbarga Mosque: Jamia Masjid built with no open courtyard, covered entirely by 63 small domes", "type": "leaf"},
                        {"label": "Gawan's Madrasa: Three-storied collegiate building at Bidar decorated with glazed Persian tiles", "type": "leaf"}
                    ]}
                ]

        # 2. Bahmani Economy
        elif 'economy' in fl:
            if is_hindi:
                return [
                    {"label": "राजस्व और बंदरगाह वाणिज्य", "type": "branch", "date": "अर्थव्यवस्था", "children": [
                        {"label": "भू-राजस्व: महमूद गवां ने भूमि की पैमाइश कराकर भू-राजस्व का व्यवस्थित कर मूल्यांकन किया", "type": "leaf"},
                        {"label": "पश्चिमी बंदरगाह: चौल और दाभोल बंदरगाहों के माध्यम से खाड़ी देशों से घोड़ों और रेशम का आयात किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Revenue & Port Trade", "type": "branch", "date": "Economy", "children": [
                        {"label": "Land assessment: Mahmud Gawan introduced systematic land measurement and tax rationalization", "type": "leaf"},
                        {"label": "Maritime ports: Chaul and Dabhol ports managed trade with Persia, importing war horses and silk", "type": "leaf"}
                    ]}
                ]

        # 3. Bahmani Military
        elif 'military' in fl:
            if is_hindi:
                return [
                    {"label": "सैन्य तकनीक और आग्नेयास्त्र", "type": "branch", "date": "सैन्य", "children": [
                        {"label": "बारूद का प्रयोग: दक्कन में विजयनगर के खिलाफ युद्धों में पहली बार बारूद और तोपों का इस्तेमाल किया", "type": "leaf"},
                        {"label": "किलाबंदी: गाविलगढ़ और नर्नला के मजबूत दुर्गों का निर्माण कराया, जहाँ तोपें तैनात थीं", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Firearms & Tactics", "type": "branch", "date": "Military", "children": [
                        {"label": "Gunpowder: First southern state to deploy early firearms in the battles against Vijayanagar", "type": "leaf"},
                        {"label": "Fortifications: Built stone ramparts and heavy bastions at Gawilgarh to withstand sieges", "type": "leaf"}
                    ]}
                ]

        # 4. Bahmani Social and Cultural Aspects
        elif 'social' in fl:
            if is_hindi:
                return [
                    {"label": "आफाकी और दक्कनी संघर्ष", "type": "branch", "date": "दरबारी कलह", "children": [
                        {"label": "आफाकी: फारस और मध्य एशिया से आए विदेशी मुस्लिम अमीर (जैसे महमूद गवां)", "type": "leaf"},
                        {"label": "दक्कनी: स्थानीय मूल के मुस्लिम रईस; आफाकियों के बढ़ते प्रभाव के कारण निरंतर दरबारी साजिशें रचीं", "type": "leaf"}
                    ]},
                    {"label": "सूफी संत और साहित्य", "type": "branch", "date": "संस्कृति", "children": [
                        {"label": "हजरत गेसू दराज: गुलबर्गा के प्रसिद्ध चिश्ती सूफी संत जिन्हें सुल्तानों ने अनुदान दिए", "type": "leaf"},
                        {"label": "दक्कनी भाषा: सूफी संतों ने स्थानीय भाषाओं को अपनाकर दक्कनी (उर्दू की पूर्वज) का विकास किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Afaqi vs Deccani Factionalism", "type": "branch", "date": "Factions", "children": [
                        {"label": "Afaqis: Foreign Muslim nobles arriving from Persia/Iraq (e.g. minister Mahmud Gawan)", "type": "leaf"},
                        {"label": "Deccanis: Local Deccani Muslim lords who resented foreign dominance, causing court instability", "type": "leaf"}
                    ]},
                    {"label": "Sufi Influence & Language", "type": "branch", "date": "Culture", "children": [
                        {"label": "Gesu Daraz: Famous Gulbarga Chishti saint patronized by rulers, fostering composite culture", "type": "leaf"},
                        {"label": "Deccani Urdu: Sufis wrote tracts in proto-Urdu (Deccani), bridging regional linguistic gaps", "type": "leaf"}
                    ]}
                ]

        # 5. Conflicts with Vijayanagar
        elif 'conflicts' in fl:
            if is_hindi:
                return [
                    {"label": "कृष्णा-तुंगभद्रा रायचूर संघर्ष", "type": "branch", "date": "टकराव", "children": [
                        {"label": "रायचूर दोआब: दो नदियों के बीच उपजाऊ बेल्ट और कृष्णा-गोदावरी डेल्टा के नियंत्रण पर विवाद", "type": "leaf"},
                        {"label": "बंदरगाहों पर नियंत्रण: कोंकण तट के बंदरगाहों (जैसे गोवा) पर अधिकार के लिए निरंतर युद्ध लड़े", "type": "leaf"}
                    ]},
                    {"label": "तालीकोटा गठबंधन (1565)", "type": "branch", "date": "तालीकोटा", "children": [
                        {"label": "एकता: बहमनी के पांचों उत्तराधिकारी राज्यों ने आपसी मतभेद भुलाकर विजयनगर के खिलाफ गठबंधन बनाया", "type": "leaf"},
                        {"label": "बन्नीहट्टी का युद्ध: रामराय की पराजय; विजयनगर साम्राज्य का पतन हुआ", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Raichur Doab Disputes", "type": "branch", "date": "Clashes", "children": [
                        {"label": "Raichur Doab: Constant battles over the fertile tract between Krishna and Tungabhadra rivers", "type": "leaf"},
                        {"label": "Western ports: Battles over control of trade outlets (Goa, Honavar) to monopolize horse imports", "type": "leaf"}
                    ]},
                    {"label": "Talikota Coalition (1565 AD)", "type": "branch", "date": "Talikota", "children": [
                        {"label": "Sultanates league: Successor states unified under Hussain Nizam Shah to crush Vijayanagar", "type": "leaf"},
                        {"label": "Bannihatti: Defeated regent Rama Raya, sacking Hampi and shifting Deccan balance of power", "type": "leaf"}
                    ]}
                ]

        # 6. Successor States: Ahmednagar (Nizam Shahi)
        elif 'ahmednagar' in fl:
            if is_hindi:
                return [
                    {"label": "अहमदनगर के निजाम शाही", "type": "branch", "date": "अहमदनगर", "children": [
                        {"label": "स्थापना: मलिक अहमद (1490 ई.) ने स्वतंत्र निजाम शाही राजवंश की स्थापना की", "type": "leaf"},
                        {"label": "मलिक अंबर: कुशल अफ्रीकी (हब्शी) मंत्री; गुरिल्ला युद्ध (बरगी-गीरी) और भूमि पैमाइश शुरू की", "type": "leaf"},
                        {"label": "पतन: 1633 ई. में मुगलों (शाहजहाँ के शासनकाल) ने अहमदनगर का मुगल साम्राज्य में विलय कर लिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Ahmednagar Nizam Shahis", "type": "branch", "date": "Ahmednagar", "children": [
                        {"label": "Establishment: Founded by Malik Ahmad in 1490 AD, asserting separation from Bidar central court", "type": "leaf"},
                        {"label": "Malik Ambar: Abyssinian minister who pioneered guerrilla tactics (Bargi-giri) and land assessments", "type": "leaf"},
                        {"label": "Annexation: Overrun and formally incorporated into the Mughal Empire under Shah Jahan in 1633 AD", "type": "leaf"}
                    ]}
                ]

        # 7. Successor States: Berar (Imad Shahi)
        elif 'berar' in fl:
            if is_hindi:
                return [
                    {"label": "बरार के इमाद शाही", "type": "branch", "date": "बरार", "children": [
                        {"label": "स्थापना: फतुल्लाह इमाद-उल-मुल्क द्वारा स्थापित; बहमनी से अलग होने वाला पहला राज्य", "type": "leaf"},
                        {"label": "विलय: सबसे कमजोर उत्तराधिकारी राज्य; 1574 ई. में अहमदनगर सल्तनत ने इसे जीत लिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Berar Imad Shahis", "type": "branch", "date": "Berar", "children": [
                        {"label": "Establishment: Set up by Fathullah Imad-ul-Mulk in 1490 AD, the first to break from Bahmanis", "type": "leaf"},
                        {"label": "Annexation: Conquered and absorbed by the neighboring Ahmednagar Sultanate in 1574 AD", "type": "leaf"}
                    ]}
                ]

        # 8. Successor States: Bidar (Barid Shahi)
        elif 'bidar' in fl:
            if is_hindi:
                return [
                    {"label": "बीदर के बरीद शाही", "type": "branch", "date": "बीदर", "children": [
                        {"label": "स्थापना: कासिम बरीद द्वारा स्थापित; बहमनी साम्राज्य के केंद्रीय क्षेत्र पर शासन किया", "type": "leaf"},
                        {"label": "पतन: 1619 ई. में बीजापुर के आदिल शाही सुल्तान ने बीदर को अपने राज्य में मिला लिया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Bidar Barid Shahis", "type": "branch", "date": "Bidar", "children": [
                        {"label": "Establishment: Evolved under Qasim Barid, occupying the central capital district of Bidar", "type": "leaf"},
                        {"label": "Annexation: Extinguished and annexed by Ibrahim Adil Shah II of Bijapur in 1619 AD", "type": "leaf"}
                    ]}
                ]

        # 9. Successor States: Bijapur (Adil Shahi)
        elif 'bijapur' in fl:
            if is_hindi:
                return [
                    {"label": "बीजापुर के आदिल शाही", "type": "branch", "date": "बीजापुर", "children": [
                        {"label": "स्थापना: यूसुफ आदिल शाह (1489 ई.) द्वारा स्थापित सबसे शक्तिशाली दक्कन सल्तनत", "type": "leaf"},
                        {"label": "गोल गुंबद: मुहम्मद आदिल शाह का मकबरा, जो विश्व के सबसे बड़े गुंबदों में से एक है", "type": "leaf"},
                        {"label": "सांस्कृतिक संरक्षण: इब्राहिम आदिल शाह द्वितीय ('जगतगुरु') ने संगीत पुस्तक 'किताब-ए-नवरस' लिखी", "type": "leaf"},
                        {"label": "पतन: 1686 ई. में मुगल सम्राट औरंगजेब ने बीजापुर पर विजय प्राप्त कर विलय किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Bijapur Adil Shahis", "type": "branch", "date": "Bijapur", "children": [
                        {"label": "Establishment: Founded by Yusuf Adil Shah in 1489 AD, growing into the premier Deccani sultanate", "type": "leaf"},
                        {"label": "Gol Gumbaz: Mausoleum of Muhammad Adil Shah featuring one of the largest domes in the world", "type": "leaf"},
                        {"label": "Patronage: Ibrahim Adil Shah II wrote Kitab-i-Navras, introducing Navraspur city for arts", "type": "leaf"},
                        {"label": "Annexation: Conquered by Aurangzeb in 1686 AD after a prolonged siege, ending independent rule", "type": "leaf"}
                    ]}
                ]

        # 10. Successor States: Golconda (Qutb Shahi)
        elif 'golconda' in fl:
            if is_hindi:
                return [
                    {"label": "गोलकुंडा के कुतुब शाही", "type": "branch", "date": "गोलकुंडा", "children": [
                        {"label": "स्थापना: कुली कुतुब शाह (1518 ई.) द्वारा स्थापित; समृद्ध हीरा व्यापार (कोहिनूर) के लिए प्रसिद्ध", "type": "leaf"},
                        {"label": "हैदराबाद स्थापना: मुहम्मद कुली कुतुब शाह ने 1591 ई. में हैदराबाद बसाया और चारमीनार बनवाई", "type": "leaf"},
                        {"label": "पतन: 1687 ई. में मुगल सम्राट औरंगजेब ने गोलकुंडा किले पर कब्जा कर इसका विलय किया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Golconda Qutb Shahis", "type": "branch", "date": "Golconda", "children": [
                        {"label": "Establishment: Founded by Quli Qutb Shah in 1518 AD, famed for diamond trading at Kollur mines", "type": "leaf"},
                        {"label": "Charminar: Muhammad Quli Qutb Shah shifted the capital to Hyderabad in 1591, building the Charminar", "type": "leaf"},
                        {"label": "Annexation: Annexed by Aurangzeb in 1687 AD following the bribery of Golconda fort gatekeeper", "type": "leaf"}
                    ]}
                ]

        # Fallback for Bahmani
        else:
            if is_hindi:
                return [
                    {"label": "बहमनी साम्राज्य सामान्य", "type": "branch", "date": "दक्कन शासन", "children": [
                        {"label": "अलाउद्दीन हसन बहमन शाह द्वारा 1347 ई. में स्थापित दक्कन का पहला स्वतंत्र शिया मुस्लिम राज्य", "type": "leaf"},
                        {"label": "आगे चलकर यह पांच स्वतंत्र रियासतों (बीजापुर, गोलकुंडा आदि) में विभाजित हो गया", "type": "leaf"}
                    ]}
                ]
            else:
                return [
                    {"label": "Bahmani Kingdom Overview", "type": "branch", "date": "Overview", "children": [
                        {"label": "First independent Shia Muslim kingdom of Deccan founded in 1347 AD by Hasan Gangu", "type": "leaf"},
                        {"label": "Disintegrated in 1518 AD into five successor sultanates including Bijapur and Golconda", "type": "leaf"}
                    ]}
                ]

def process_file(html_path, relative_category, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    
    # 1. Clean previous mindmap tags to prevent duplicates
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Normalize newlines
    html = html.replace('\r\n', '\n')

    # Remove any existing mindmap CSS/container/script tags
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n', '')
    
    # Match and clean existing interactive mindmap card
    mindmap_div_pattern = r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    
    # Match and clean existing mindmap engine script
    script_pattern = r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # 2. Get topic title from content.json if it exists
    folder_path = os.path.dirname(html_path)
    content_json_path = os.path.join(folder_path, "content.json")
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        # parent folder name is the real topic folder name
        parent_folder = os.path.dirname(folder_path)
        folder_name = os.path.basename(parent_folder)
        content_json_path = os.path.join(parent_folder, "hi", "content.json")
        if not os.path.exists(content_json_path):
            content_json_path = os.path.join(parent_folder, "content.json")

    clean_title = get_clean_title(folder_name)
    
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
        except Exception as e:
            print(f"  Error reading content.json: {e}")

    # 3. Build unique mindmap data using refined keyword matching on the folder_name
    branches = get_custom_branches(folder_name, relative_category, is_hindi)
    mindmap_data = {
        "label": clean_title,
        "type": "root",
        "children": branches
    }

    # 4. Re-inject CSS link before closing </head>
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # 5. Re-inject Mindmap Div before deep-dive-section
    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें — एक को खोलने पर दूसरे स्वतः बंद हो जाएंगे।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
        title_text = f"{topic_name} &mdash; Interactive Mindmap"

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
    
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback to Tab 1 notes panel
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # 6. Re-inject script before </body>
    tree_json = json.dumps(mindmap_data)
    lang_str = "'hi'" if is_hindi else "'en'"
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, {lang_str});
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    # 7. Write back
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"  Successfully patched {html_path}")

def main():
    total_processed = 0
    # Walk through the medieval_history directory
    for root, dirs, files in os.walk(BASE):
        # Determine the relative category directory name (e.g. Mughal-Rule, etc.)
        rel_path = os.path.relpath(root, BASE)
        # Skip the root base directory itself
        if rel_path == ".":
            continue
        
        # Split path parts
        parts = rel_path.split(os.sep)
        category = parts[0] if parts else ""
        
        # Check if we are inside a Hindi 'hi' directory
        is_hindi = False
        if 'hi' in parts:
            is_hindi = True
            category = parts[0]
        
        for file in files:
            if file == "index.html":
                html_path = os.path.join(root, file)
                process_file(html_path, category, is_hindi)
                total_processed += 1
                
    print(f"\nDone! Patched {total_processed} files successfully.")

if __name__ == '__main__':
    main()
