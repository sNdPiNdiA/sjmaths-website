#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/modern_history/Important-Committees-and-Commissions"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'upsc', 'ad', 'bc', 'tb', 'dr', 'sir'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'between', 'or']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Currency Babington-Smith Commission
    if 'babington' in fl:
        if is_hindi:
            return [
                {"label": "पृष्ठभूमि और उद्देश्य", "type": "branch", "date": "1913-14 ई.", "children": [
                    {"label": "गठन: प्रथम विश्व युद्ध की पूर्व संध्या पर भारतीय मुद्रा और वित्त की जांच के लिए हेनरी बबिंगटन-स्मिथ की अध्यक्षता में गठित", "type": "leaf"},
                    {"label": "फाउलर की सिफारिशों की समीक्षा: इस आयोग ने मुख्य रूप से 1898 के फाउलर आयोग की विनिमय दर की सिफारिशों की समीक्षा की", "type": "leaf"}
                ]},
                {"label": "प्रमुख निष्कर्ष और सिफारिशें", "type": "branch", "date": "सिफारिशें", "children": [
                    {"label": "गोल्ड स्टैंडर्ड का समर्थन: सोने के सिक्के के प्रचलन का समर्थन किया; 1s. 4d. की विनिमय दर (16 पेंस) बनाए रखने की सिफारिश की", "type": "leaf"},
                    {"label": "केंद्रीय बैंक: एक केंद्रीय राज्य बैंक की स्थापना की आवश्यकता पर बल दिया, जो भारत के लिए मुद्रा जारी करे", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Background & Formation", "type": "branch", "date": "1913-14 AD", "children": [
                    {"label": "Set up under Henry Babington-Smith to examine the Indian currency system on the eve of World War I", "type": "leaf"},
                    {"label": "Reviewed the Fowler Commission recommendations of 1898 on exchange rates for Indian rupee/gold linkage", "type": "leaf"}
                ]},
                {"label": "Key Recommendations", "type": "branch", "date": "Findings", "children": [
                    {"label": "Gold Standard: Supported the gold-exchange standard and recommended maintaining the 1s. 4d. (16 pence) rupee parity", "type": "leaf"},
                    {"label": "Central Bank: Recommended establishing a central State Bank to oversee note issue and monetary management", "type": "leaf"}
                ]}
            ]

    # 2. Currency Fowler Commission
    elif 'fowler' in fl:
        if is_hindi:
            return [
                {"label": "पृष्ठभूमि (1898)", "type": "branch", "date": "1898 ई.", "children": [
                    {"label": "गठन: 1893 के मुद्रा संकट (रुपये की गिरती कीमत) के बाद सर ईवार्ट फाउलर की अध्यक्षता में गठित", "type": "leaf"},
                    {"label": "संकट: चांदी की कीमत गिरने से रुपया कमजोर हुआ; 1893 में सरकार ने चांदी का मुक्त टकसाल बंद कर दिया", "type": "leaf"}
                ]},
                {"label": "प्रमुख सिफारिशें", "type": "branch", "date": "सिफारिशें", "children": [
                    {"label": "विनिमय दर: 1s. 4d. (16 पेंस) की निश्चित विनिमय दर की सिफारिश की; भारतीय मुद्रा को सोने से जोड़ा", "type": "leaf"},
                    {"label": "स्वर्ण मानक की नींव: भारत में 'गोल्ड-एक्सचेंज स्टैंडर्ड' की नींव रखी जहाँ रुपया पाउंड स्टर्लिंग के माध्यम से सोने से जुड़ा था", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Background (1898)", "type": "branch", "date": "1898 AD", "children": [
                    {"label": "Formed after the rupee depreciation crisis; falling silver prices led to 1893 suspension of free silver coinage", "type": "leaf"},
                    {"label": "Chaired by Sir Everard im Thurn Fowler to establish a stable exchange rate for Indian currency", "type": "leaf"}
                ]},
                {"label": "Major Recommendations", "type": "branch", "date": "Recommendations", "children": [
                    {"label": "Exchange Rate: Fixed the rupee-sterling ratio at 1s. 4d. (16 pence), restoring monetary confidence", "type": "leaf"},
                    {"label": "Gold-Exchange Standard: Established India's gold-exchange standard, linking the rupee to pound sterling", "type": "leaf"}
                ]}
            ]

    # 3. Currency Hilton-Young Commission
    elif 'hilton' in fl:
        if is_hindi:
            return [
                {"label": "गठन (1926) और उद्देश्य", "type": "branch", "date": "1926 ई.", "children": [
                    {"label": "अध्यक्ष: सर एडविन हिल्टन यंग; भारतीय मुद्रा और वित्त पर रॉयल आयोग (Royal Commission on Indian Currency & Finance)", "type": "leaf"},
                    {"label": "पृष्ठभूमि: प्रथम विश्व युद्ध के बाद भारत में मौद्रिक संरचना में अव्यवस्था थी; केंद्रीय बैंक की मांग तेज हो रही थी", "type": "leaf"}
                ]},
                {"label": "ऐतिहासिक सिफारिशें", "type": "branch", "date": "सिफारिशें", "children": [
                    {"label": "भारतीय रिज़र्व बैंक (RBI): एक स्वतंत्र, अलग केंद्रीय बैंक की स्थापना की सिफारिश की (RBI अंततः 1935 में स्थापित हुआ)", "type": "leaf"},
                    {"label": "मुद्रा विभाजन: सरकार के ऋण प्रबंधन और मुद्रा जारी करने के कार्यों को नए बैंक को सौंपने की सिफारिश की", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Formation & Purpose (1926)", "type": "branch", "date": "1926 AD", "children": [
                    {"label": "Royal Commission on Indian Currency & Finance, chaired by Sir Edwin Hilton Young", "type": "leaf"},
                    {"label": "Convened to bring monetary stability post-WWI and address widespread calls for an independent central bank", "type": "leaf"}
                ]},
                {"label": "Historic Recommendations", "type": "branch", "date": "Recommendations", "children": [
                    {"label": "Reserve Bank of India: Strongly recommended creating an independent central bank, leading to RBI's founding in 1935", "type": "leaf"},
                    {"label": "Separation of Functions: Proposed separating currency management and debt management from the Finance Department", "type": "leaf"}
                ]}
            ]

    # 4. Currency Mansfield Commission
    elif 'mansfield' in fl:
        if is_hindi:
            return [
                {"label": "पृष्ठभूमि (1866)", "type": "branch", "date": "1866 ई.", "children": [
                    {"label": "पृष्ठभूमि: 1865-66 के वित्तीय संकट और इलाहाबाद बैंक के पतन के बाद वित्तीय नियमन की जांच के लिए गठित", "type": "leaf"},
                    {"label": "मुख्य प्रश्न: क्या भारत में एक एकल राज्य बैंक (State Bank) की स्थापना होनी चाहिए?", "type": "leaf"}
                ]},
                {"label": "परिणाम और विरासत", "type": "branch", "date": "विरासत", "children": [
                    {"label": "बैंकिंग संकट: 1866 के बंगाल में वाणिज्यिक बैंकों के व्यापक पतन ने भारत में मौद्रिक सुधार की मांग को जन्म दिया", "type": "leaf"},
                    {"label": "एकीकृत बैंकिंग बहस: इस आयोग ने केंद्रीय बैंक बनाम विकेंद्रीकृत बैंकिंग की बहस को आगे बढ़ाया, जो बाद के आयोगों का विषय बना", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Background (1866)", "type": "branch", "date": "1866 AD", "children": [
                    {"label": "Established after the 1865-66 financial crash and bank failures to examine colonial monetary arrangements", "type": "leaf"},
                    {"label": "Central question: whether a unitary State Bank of India should be created to regularize note issue", "type": "leaf"}
                ]},
                {"label": "Outcome & Legacy", "type": "branch", "date": "Legacy", "children": [
                    {"label": "Banking Crisis root: Collapse of Agra & United Service Bank and Bank of Bombay triggered the inquiry", "type": "leaf"},
                    {"label": "Centralization debate: Helped frame the long-running debate on whether India needed a unified central bank", "type": "leaf"}
                ]}
            ]

    # 5. Famine Campbell Commission
    elif 'campbell' in fl:
        if is_hindi:
            return [
                {"label": "1866 के अकाल की पृष्ठभूमि", "type": "branch", "date": "1866 ई.", "children": [
                    {"label": "ओडिशा का भयंकर अकाल: 1866 में ओडिशा (तत्कालीन उड़ीसा) में भीषण अकाल; अनुमानित 10 लाख लोगों की मृत्यु", "type": "leaf"},
                    {"label": "सरकारी विफलता: अकाल से निपटने में ब्रिटिश सरकार की लापरवाही और देरी की व्यापक आलोचना हुई", "type": "leaf"}
                ]},
                {"label": "प्रमुख निष्कर्ष", "type": "branch", "date": "निष्कर्ष", "children": [
                    {"label": "प्रारंभिक चेतावनी: फसल की बर्बादी के शुरुआती संकेतों को समय पर पहचानने में विफलता को प्रमुख कारण माना गया", "type": "leaf"},
                    {"label": "राहत कार्य: अकाल पीड़ितों के लिए राहत कार्यों (Public Works) को अधिक कुशल और व्यापक बनाने की सिफारिश की गई", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Orissa Famine Crisis (1866)", "type": "branch", "date": "1866 AD", "children": [
                    {"label": "Orissa Famine: 1866 famine caused by crop failure and British administrative neglect, killing ~1 million people", "type": "leaf"},
                    {"label": "State Failure: Commission was formed because delayed government action worsened mortality outcomes", "type": "leaf"}
                ]},
                {"label": "Key Findings", "type": "branch", "date": "Findings", "children": [
                    {"label": "Early Warning: Failure to detect early distress signs of crop shortfall identified as the key systemic failure", "type": "leaf"},
                    {"label": "Relief Works: Recommended expanding public works employment (roads, canals) as organized famine relief mechanism", "type": "leaf"}
                ]}
            ]

    # 6. Famine Lyall Commission
    elif 'lyall' in fl:
        if is_hindi:
            return [
                {"label": "1896-97 के अकाल और गठन", "type": "branch", "date": "1896-97 ई.", "children": [
                    {"label": "पृष्ठभूमि: 1896-97 के व्यापक मध्य भारतीय अकाल (मध्य प्रांत और संयुक्त प्रांत) के बाद गठित", "type": "leaf"},
                    {"label": "अध्यक्ष: सर जेम्स लियाल (James Lyall); मैकडॉनेल आयोग के समानांतर काम किया", "type": "leaf"}
                ]},
                {"label": "सिफारिशें और अकाल संहिता", "type": "branch", "date": "सुधार", "children": [
                    {"label": "क्षेत्रीय अकाल कोड: क्षेत्र विशेष के लिए अकाल संहिता तैयार करने की सिफारिश; राहत के लिए जिला-स्तरीय ढांचा", "type": "leaf"},
                    {"label": "भूमि राजस्व राहत: प्रभावित जिलों में भूमि राजस्व की वसूली को स्थगित करने या कम करने की सिफारिश की", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "1896-97 Famine Context", "type": "branch", "date": "1896-97 AD", "children": [
                    {"label": "Formed after the severe Central India famine of 1896-97, which affected the United Provinces and Central Provinces", "type": "leaf"},
                    {"label": "Chaired by Sir James Lyall; ran parallel to the MacDonnell Commission examining different regions", "type": "leaf"}
                ]},
                {"label": "Recommendations & Famine Codes", "type": "branch", "date": "Reforms", "children": [
                    {"label": "Regional Famine Codes: Recommended drafting region-specific famine codes for systematic relief administration", "type": "leaf"},
                    {"label": "Revenue Suspension: Suggested suspending or reducing land revenue collection in officially declared famine areas", "type": "leaf"}
                ]}
            ]

    # 7. Famine MacDonnell Commission
    elif 'macdonnell' in fl:
        if is_hindi:
            return [
                {"label": "1898 अकाल जांच", "type": "branch", "date": "1898 ई.", "children": [
                    {"label": "गठन: 1896-97 के अकाल के बाद ए.पी. मैकडॉनेल (A.P. MacDonnell) की अध्यक्षता में गठित; मुख्यतः बंगाल प्रेसीडेंसी की स्थितियों की जांच", "type": "leaf"},
                    {"label": "व्यापक दायरा: बड़े पैमाने पर यह पता लगाना कि अकाल के समय की प्रशासनिक नीति क्या होनी चाहिए", "type": "leaf"}
                ]},
                {"label": "दीर्घकालिक नीति प्रभाव", "type": "branch", "date": "नीति प्रभाव", "children": [
                    {"label": "अकाल बीमा निधि: सार्वजनिक कार्यों के वित्तपोषण और अकाल राहत के लिए एक अलग 'अकाल राहत कोष' का सुझाव दिया", "type": "leaf"},
                    {"label": "परीक्षण और पात्रता: 'परीक्षण' (Means Test) के आधार पर राहत कार्यों में भर्ती करने की व्यवस्था को परिष्कृत किया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Post-1896 Famine Investigation", "type": "branch", "date": "1898 AD", "children": [
                    {"label": "Chaired by A.P. MacDonnell; investigated the administrative failures during the 1896-97 famines primarily in Bengal", "type": "leaf"},
                    {"label": "Broad mandate: To codify guidelines for relief administration and identify systemic improvement opportunities", "type": "leaf"}
                ]},
                {"label": "Long-term Policy Impact", "type": "branch", "date": "Policy Impact", "children": [
                    {"label": "Famine Insurance Fund: Proposed dedicated budgetary allocation for public works and famine relief programs", "type": "leaf"},
                    {"label": "Means Testing: Helped refine the eligibility criteria ('task work' system) used in government famine camps", "type": "leaf"}
                ]}
            ]

    # 8. Famine Strachey Commission
    elif 'stratchy' in fl or 'strachey' in fl:
        if is_hindi:
            return [
                {"label": "1880 अकाल आयोग (सर्वाधिक महत्वपूर्ण)", "type": "branch", "date": "1880 ई.", "children": [
                    {"label": "गठन: 1876-78 के भीषण मद्रास और बंबई अकाल के बाद लॉर्ड लिटन ने सर रिचर्ड स्ट्रैची की अध्यक्षता में गठित", "type": "leaf"},
                    {"label": "सर्वाधिक व्यापक: इसे भारतीय अकाल इतिहास का सबसे महत्वपूर्ण और व्यापक आयोग माना जाता है", "type": "leaf"}
                ]},
                {"label": "ऐतिहासिक सिफारिशें", "type": "branch", "date": "विरासत", "children": [
                    {"label": "अखिल भारतीय अकाल संहिता: पहली बार एक समन्वित 'अकाल संहिता' (Famine Code) बनाने की सिफारिश, जो बाद के सभी प्रांतीय अकाल संहिताओं का आधार बनी", "type": "leaf"},
                    {"label": "राहत के तीन सिद्धांत: (1) सस्ते भोजन की उपलब्धता, (2) परीक्षण-आधारित रोजगार, (3) निराश्रितों को मुफ्त सहायता", "type": "leaf"},
                    {"label": "निवारक बनाम राहत: अकाल की रोकथाम के लिए सिंचाई और रेलवे के बुनियादी ढांचे के विकास पर जोर दिया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "1880 Famine Commission (Most Critical)", "type": "branch", "date": "1880 AD", "children": [
                    {"label": "Formed by Lord Lytton after the catastrophic 1876-78 Madras and Bombay famines, chaired by Sir Richard Strachey", "type": "leaf"},
                    {"label": "Most comprehensive famine inquiry in British Indian history, defining long-term relief and prevention policy", "type": "leaf"}
                ]},
                {"label": "Landmark Recommendations", "type": "branch", "date": "Legacy", "children": [
                    {"label": "All-India Famine Code: First recommended a systematic and unified Famine Code as basis for provincial codes", "type": "leaf"},
                    {"label": "Three Relief Pillars: (1) Relief works with task wages, (2) gratuitous relief for the destitute, (3) cheap food access", "type": "leaf"},
                    {"label": "Preventive Infrastructure: Emphasized irrigation canals and railways as the best long-term famine prevention tools", "type": "leaf"}
                ]}
            ]

    # 9. Law First Law Commission 1834 (TB Macaulay)
    elif 'first' in fl and 'law' in fl:
        if is_hindi:
            return [
                {"label": "प्रथम विधि आयोग (1834)", "type": "branch", "date": "1834 ई.", "children": [
                    {"label": "अध्यक्ष: थॉमस बैबिंगटन मैकॉले; 1833 के चार्टर एक्ट द्वारा स्थापित; बंगाल की कानूनी व्यवस्था को संहिताबद्ध करना इसका लक्ष्य था", "type": "leaf"},
                    {"label": "भारतीय दंड संहिता (IPC): मैकॉले ने 1837 में IPC का प्रारूप तैयार किया; यह 1860 में लागू हुई और आज भी प्रासंगिक है", "type": "leaf"}
                ]},
                {"label": "महत्वपूर्ण योगदान", "type": "branch", "date": "योगदान", "children": [
                    {"label": "सार्वभौमिक कानून संहिता: पहली बार जाति-धर्म निरपेक्ष एक समान आपराधिक कानून संहिता लागू करने का प्रयास किया गया", "type": "leaf"},
                    {"label": "मैकॉले के मिनट (1835): अंग्रेजी शिक्षा के पक्ष में प्रसिद्ध मैकॉले मिनट; इस आयोग काल का ही उत्पाद था", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "First Law Commission (1834)", "type": "branch", "date": "1834 AD", "children": [
                    {"label": "Chaired by T.B. Macaulay; established under the Charter Act of 1833 to codify laws for British India", "type": "leaf"},
                    {"label": "Indian Penal Code: Macaulay drafted the IPC in 1837; finally enacted in 1860, forming the basis of criminal law", "type": "leaf"}
                ]},
                {"label": "Key Contributions", "type": "branch", "date": "Contributions", "children": [
                    {"label": "Universal Codification: First attempt at a uniform criminal code applicable equally to all communities in India", "type": "leaf"},
                    {"label": "Macaulay's Minute (1835): His landmark advocacy for English-medium education policy was a product of this same tenure", "type": "leaf"}
                ]}
            ]

    # 10. Law Fourth Pre-Independence Law Commission 1879 (Dr Whitley Stokes)
    elif 'fourth' in fl and 'law' in fl:
        if is_hindi:
            return [
                {"label": "चतुर्थ विधि आयोग (1879)", "type": "branch", "date": "1879 ई.", "children": [
                    {"label": "अध्यक्ष: डॉ. व्हिटले स्टोक्स; 1879 में गठित; इसने पहले के तीन आयोगों के काम को पूरा करने का प्रयास किया", "type": "leaf"},
                    {"label": "पूर्ण संहिताकरण: नागरिक और फौजदारी कानूनों का व्यापक पुनरीक्षण और उन्हें एक सुसंगत रूप देने का प्रयास", "type": "leaf"}
                ]},
                {"label": "प्रमुख कार्य और विधायी विरासत", "type": "branch", "date": "विधायी विरासत", "children": [
                    {"label": "प्रमुख अधिनियम: भारतीय अनुबंध अधिनियम (1872), भारतीय संपत्ति हस्तांतरण अधिनियम, और भारतीय साक्ष्य अधिनियम को अंतिम रूप दिया", "type": "leaf"},
                    {"label": "प्रशासनिक कानून: कंपनी शासन से क्राउन शासन में संक्रमण के बाद कानूनी व्यवस्था को आधुनिक बनाने में महत्वपूर्ण भूमिका", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Fourth Law Commission (1879)", "type": "branch", "date": "1879 AD", "children": [
                    {"label": "Chaired by Dr. Whitley Stokes; established to complete the unfinished codification work of the three prior commissions", "type": "leaf"},
                    {"label": "Comprehensive revision of both civil and criminal statutes to create a consistent legal system across provinces", "type": "leaf"}
                ]},
                {"label": "Major Legislative Legacy", "type": "branch", "date": "Legacy", "children": [
                    {"label": "Key Statutes: Finalized the Indian Contract Act (1872), Transfer of Property Act, and Indian Evidence Act", "type": "leaf"},
                    {"label": "Post-1857 modernization: Reorganized colonial legal framework after the shift from Company to Crown rule", "type": "leaf"}
                ]}
            ]

    # 11. Law Second Pre-Independence Law Commission 1853 (Sir John Romilly)
    elif 'second' in fl and 'law' in fl:
        if is_hindi:
            return [
                {"label": "द्वितीय विधि आयोग (1853)", "type": "branch", "date": "1853 ई.", "children": [
                    {"label": "अध्यक्ष: सर जॉन रोमिली; 1853 के चार्टर एक्ट (अंतिम ईस्ट इंडिया कंपनी नवीकरण) के समय गठित", "type": "leaf"},
                    {"label": "उद्देश्य: प्रथम आयोग के अधूरे कार्य को आगे बढ़ाना; उच्च न्यायालयों की शक्तियों और प्रक्रियाओं का निर्धारण करना", "type": "leaf"}
                ]},
                {"label": "प्रमुख कार्य और परिणाम", "type": "branch", "date": "कार्य", "children": [
                    {"label": "उच्च न्यायालय: उच्च न्यायालयों की स्थापना के लिए प्रस्ताव दिए; 1861 में उच्च न्यायालय अधिनियम का आधार बना", "type": "leaf"},
                    {"label": "सिविल प्रक्रिया संहिता: सिविल प्रक्रिया संहिता (CPC) के शुरुआती प्रारूप पर काम किया, जिसे बाद में 1859 में अधिनियमित किया गया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Second Law Commission (1853)", "type": "branch", "date": "1853 AD", "children": [
                    {"label": "Chaired by Sir John Romilly; formed at the time of the 1853 Charter Act, the last renewal of EIC charter", "type": "leaf"},
                    {"label": "Mission: Advance incomplete codification from the first commission and define High Court jurisdictions", "type": "leaf"}
                ]},
                {"label": "Outcomes & Legislative Impact", "type": "branch", "date": "Impact", "children": [
                    {"label": "High Courts: Proposals for establishing High Courts led directly to the High Courts Act of 1861", "type": "leaf"},
                    {"label": "Civil Procedure Code: Prepared initial drafts for the Code of Civil Procedure, enacted as CPC of 1859", "type": "leaf"}
                ]}
            ]

    # 12. Law Third Pre-Independence Law Commission 1862 (Sir John Romilly)
    elif 'third' in fl and 'law' in fl:
        if is_hindi:
            return [
                {"label": "तृतीय विधि आयोग (1862)", "type": "branch", "date": "1862 ई.", "children": [
                    {"label": "अध्यक्ष: सर जॉन रोमिली (पुनः नियुक्त); 1857 के विद्रोह के बाद क्राउन शासन की स्थापना के संदर्भ में गठित", "type": "leaf"},
                    {"label": "पोस्ट-1857 सुधार: कंपनी कानून से क्राउन कानून में संक्रमण के बाद कानूनी ढांचे को अद्यतन करने का कार्य", "type": "leaf"}
                ]},
                {"label": "महत्वपूर्ण योगदान", "type": "branch", "date": "योगदान", "children": [
                    {"label": "1860 की IPC लागू करना: मैकॉले की IPC (प्रथम आयोग) को अंततः इसी काल में 1860 में क्रियान्वित किया गया", "type": "leaf"},
                    {"label": "दंड प्रक्रिया संहिता: CrPC के शुरुआती ढांचे पर काम किया; 1898 में पूर्ण CrPC का मार्ग प्रशस्त किया", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Third Law Commission (1862)", "type": "branch", "date": "1862 AD", "children": [
                    {"label": "Chaired again by Sir John Romilly; constituted after the 1857 revolt and the transfer of India to Crown rule", "type": "leaf"},
                    {"label": "Post-1857 Reform: Tasked with updating legal structures to reflect Queen's Proclamation and new governance model", "type": "leaf"}
                ]},
                {"label": "Key Contributions", "type": "branch", "date": "Contributions", "children": [
                    {"label": "IPC Enactment: Macaulay's long-pending IPC draft was finally enacted into law during this commission's era (1860)", "type": "leaf"},
                    {"label": "Code of Criminal Procedure: Laid early groundwork for CrPC, fully codified in 1898 and revised in 1973", "type": "leaf"}
                ]}
            ]

    # 13. Other Important Commissions
    elif 'other-important' in fl:
        if is_hindi:
            return [
                {"label": "शिक्षा और सामाजिक आयोग", "type": "branch", "date": "शिक्षा", "children": [
                    {"label": "हंटर आयोग (1882): लॉर्ड रिपन के समय गठित; प्राथमिक और माध्यमिक शिक्षा की समीक्षा; स्थानीय निकायों को शिक्षा का हस्तांतरण", "type": "leaf"},
                    {"label": "सैडलर आयोग (1917-19): कलकत्ता विश्वविद्यालय की समीक्षा; स्नातक शिक्षा की समस्याओं की जांच; राज्य विश्वविद्यालयों की स्वायत्तता", "type": "leaf"},
                    {"label": "साइमन आयोग (1927): भारत शासन अधिनियम 1919 की समीक्षा के लिए; 7 अंग्रेज सदस्य, कोई भारतीय नहीं; 'साइमन गो बैक' आंदोलन", "type": "leaf"}
                ]},
                {"label": "पुलिस और प्रशासनिक आयोग", "type": "branch", "date": "प्रशासन", "children": [
                    {"label": "फ्रेजर आयोग (1902-03): पुलिस सुधारों की समीक्षा; 1902 का पुलिस अधिनियम का आधार; जिला पुलिस और सीआईडी का पृथक्करण", "type": "leaf"},
                    {"label": "इस्लिंगटन आयोग (1912): भारतीय सिविल सेवा में भारतीयों की भागीदारी बढ़ाने की समीक्षा; भारतीयकरण की दिशा में प्रारंभिक प्रयास", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Education & Social Commissions", "type": "branch", "date": "Education", "children": [
                    {"label": "Hunter Commission (1882): Review of primary/secondary education; devolved control to local municipalities under Lord Ripon", "type": "leaf"},
                    {"label": "Sadler Commission (1917-19): Reviewed Calcutta University issues; recommended 12-year schooling before university", "type": "leaf"},
                    {"label": "Simon Commission (1927): Reviewed Government of India Act, 1919; all-British composition triggered 'Simon Go Back' protests", "type": "leaf"}
                ]},
                {"label": "Police & Administrative Commissions", "type": "branch", "date": "Administration", "children": [
                    {"label": "Fraser Commission (1902-03): Police reform inquiry; led to the Police Act 1902 and separation of CID from district police", "type": "leaf"},
                    {"label": "Islington Commission (1912): Reviewed Indianization of civil services; recommended limited expansion of Indian recruitment", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [
                {"label": "आयोग और समितियाँ", "type": "branch", "date": "ब्रिटिश काल", "children": [
                    {"label": "ब्रिटिश भारत में मुद्रा, अकाल राहत और कानून संहिताकरण से संबंधित प्रमुख आयोगों का विवरण", "type": "leaf"},
                    {"label": "इन आयोगों ने भारत की आधुनिक कानूनी, बैंकिंग और प्रशासनिक संरचना की नींव रखी", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "British India Commissions", "type": "branch", "date": "Colonial", "children": [
                    {"label": "Examines major currency, famine relief, and law codification commissions of British India", "type": "leaf"},
                    {"label": "These commissions collectively shaped India's modern monetary, legal, and administrative frameworks", "type": "leaf"}
                ]}
            ]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('\r\n', '\n')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n', '')

    mindmap_div_pattern = r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    folder_path = os.path.dirname(html_path)
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        parent_folder = os.path.dirname(folder_path)
        folder_name = os.path.basename(parent_folder)

    content_json_path = os.path.join(os.path.dirname(html_path), "content.json")
    clean_title = get_clean_title(folder_name)
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    branches = get_custom_branches(folder_name, is_hindi)
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
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
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

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

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Successfully patched {html_path}")

def main():
    total_processed = 0
    for root, dirs, files in os.walk(BASE):
        rel_path = os.path.relpath(root, BASE)
        parts = rel_path.split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                process_file(os.path.join(root, file), is_hindi)
                total_processed += 1
    print(f"\nDone! Patched {total_processed} files successfully.")

if __name__ == '__main__':
    main()
