#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Education-during-British-Rule"

MINDMAP_DATA = {
    "charter-act-of-1813": {
        "en": [
            {"label": "State Funding", "type": "branch", "date": "1813", "children": [
                {"label": "Charter Act of 1813 incorporated first official state initiative for education in India", "type": "leaf"},
                {"label": "Mandated East India Company spend Rs 1 lakh annually to promote literature and encourage sciences", "type": "leaf"},
                {"label": "Funding delayed for years due to disputes over the medium of instruction & type of literature", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राज्य वित्त पोषण", "type": "branch", "date": "1813", "children": [
                {"label": "1813 के चार्टर अधिनियम ने भारत में शिक्षा के लिए पहला आधिकारिक राज्य वित्त पोषित कदम उठाया", "type": "leaf"},
                {"label": "ईस्ट इंडिया कंपनी को साहित्य के प्रचार और विज्ञान को बढ़ावा देने हेतु सालाना 1 लाख रुपये खर्च करने का आदेश दिया", "type": "leaf"},
                {"label": "शिक्षा के माध्यम और पाठ्यक्रम के प्रकार को लेकर विवादों के कारण कई वर्षों तक धन जारी नहीं हो सका", "type": "leaf"}]}
        ]
    },
    "orientalist-anglicist-controversy": {
        "en": [
            {"label": "The Split", "type": "branch", "date": "1820s-30s", "children": [
                {"label": "Orientalists (H.T. Prinsep): Supported classical Indian learning (Sanskrit, Arabic, Persian) & traditional schools", "type": "leaf"},
                {"label": "Anglicists: Advocated modern western education and science taught through the English medium", "type": "leaf"},
                {"label": "Macaulay's Minute (1835): Resolved in favor of Anglicists, declaring English as the official educational medium", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विवाद", "type": "branch", "date": "1820-30 का दशक", "children": [
                {"label": "प्राच्यविद (एच.टी. प्रिंसेप): पारंपरिक भारतीय शिक्षा (संस्कृत, अरबी, फारसी) और गुरुकुलों/मदरसों के समर्थक थे", "type": "leaf"},
                {"label": "आंग्लविद: अंग्रेजी माध्यम के जरिए आधुनिक पश्चिमी शिक्षा और विज्ञान सिखाने की वकालत कर रहे थे", "type": "leaf"},
                {"label": "मैकाले का मिनट (1835): आंग्लविदों के पक्ष में विवाद सुलझाया और अंग्रेजी को आधिकारिक शिक्षा का माध्यम घोषित किया", "type": "leaf"}]}
        ]
    },
    "general-committee-of-public-instruction": {
        "en": [
            {"label": "The Committee", "type": "branch", "date": "1823", "children": [
                {"label": "Formed in 1823 to take charge of public instruction in Bengal presidency & allocate educational funds", "type": "leaf"},
                {"label": "Paralyzed by internal conflict between the Orientalist and Anglicist factions over resource spending", "type": "leaf"},
                {"label": "Reorganized after Macaulay's 1835 decision, implementing the 'Downward Filtration' theory", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "समिति का गठन", "type": "branch", "date": "1823", "children": [
                {"label": "बंगाल प्रेसीडेंसी में सार्वजनिक शिक्षा का कार्यभार संभालने और शैक्षिक धन आवंटित करने हेतु 1823 में गठित", "type": "leaf"},
                {"label": "संसाधनों के खर्च को लेकर प्राच्यविदों और आंग्लविदों के आंतरिक मतभेदों के कारण लंबे समय तक निष्क्रिय रही", "type": "leaf"},
                {"label": "1835 के मैकाले के निर्णय के बाद पुनर्गठित हुई और 'अधोमुखी निस्यंदन' सिद्धांत (फिल्ट्रेशन थ्योरी) को लागू किया", "type": "leaf"}]}
        ]
    },
    "woods-dispatch": {
        "en": [
            {"label": "Magna Carta", "type": "branch", "date": "1854", "children": [
                {"label": "Wood's Despatch (1854) by Charles Wood (President of Board of Control); laid systematic educational plan", "type": "leaf"},
                {"label": "Recommended English for Higher Education (universities) and Vernacular languages for primary schools", "type": "leaf"},
                {"label": "Urged setting up departments of public instruction in all provinces and universities in presidency towns", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मैग्ना कार्टा", "type": "branch", "date": "1854", "children": [
                {"label": "चार्ल्स वुड (बोर्ड ऑफ कंट्रोल के अध्यक्ष) द्वारा वुड का डिस्पैच (1854); व्यवस्थित शैक्षिक योजना तैयार की", "type": "leaf"},
                {"label": "उच्च शिक्षा (विश्वविद्यालयों) हेतु अंग्रेजी और प्राथमिक स्तर हेतु स्थानीय भाषाओं (मातृभाषा) की सिफारिश की", "type": "leaf"},
                {"label": "सभी प्रांतों में जन शिक्षा विभाग और प्रेसीडेंसी शहरों में विश्वविद्यालयों की स्थापना करने की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "hunter-commission": {
        "en": [
            {"label": "Primary Focus", "type": "branch", "date": "1882-1883", "children": [
                {"label": "Hunter Commission (1882-83) under W.W. Hunter appointed to review progress since Wood's Despatch", "type": "leaf"},
                {"label": "Recommended state should prioritize expansion of primary education and drop direct control of secondary schools", "type": "leaf"},
                {"label": "Urged transfer of primary school administration to newly created District and Municipal Boards", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्राथमिक ध्यान", "type": "branch", "date": "1882-1883", "children": [
                {"label": "वुड डिस्पैच के बाद प्रगति की समीक्षा हेतु डब्ल्यू.डब्ल्यू. हंटर के अधीन हंटर आयोग (1882-83) नियुक्त", "type": "leaf"},
                {"label": "सिफारिश की कि राज्य को प्राथमिक शिक्षा के विस्तार को प्राथमिकता देनी चाहिए और माध्यमिक विद्यालयों से सीधा नियंत्रण हटाना चाहिए", "type": "leaf"},
                {"label": "प्राथमिक शिक्षा का प्रशासन नवगठित जिला और नगर पालिका बोर्डों को स्थानांतरित करने का सुझाव दिया", "type": "leaf"}]}
        ]
    },
    "indian-universities-act-1904": {
        "en": [
            {"label": "Curzon's Reforms", "type": "branch", "date": "1904 Act", "children": [
                {"label": "Passed by Lord Curzon based on Raleigh Commission (1902) to centralize higher education control", "type": "leaf"},
                {"label": "Increased government veto power over senate regulations and restricted affiliation conditions for colleges", "type": "leaf"},
                {"label": "Aimed to curb nationalist activities and radical student political mobilization on university campuses", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कर्जन के सुधार", "type": "branch", "date": "1904 का एक्ट", "children": [
                {"label": "उच्च शिक्षा नियंत्रण को केंद्रीकृत करने हेतु लॉर्ड कर्जन द्वारा रैले आयोग (1902) के आधार पर पारित", "type": "leaf"},
                {"label": "सीनेट के नियमों पर सरकार की वीटो शक्ति बढ़ाई और कॉलेजों के संबद्धता नियमों को अत्यंत कड़ा किया", "type": "leaf"},
                {"label": "विश्वविद्यालय परिसरों में राष्ट्रवादी गतिविधियों और क्रांतिकारी छात्र राजनीतिक लामबंदी को दबाना मुख्य उद्देश्य था", "type": "leaf"}]}
        ]
    },
    "resolution-on-education-policy-1913": {
        "en": [
            {"label": "Compulsory Issue", "type": "branch", "date": "1913", "children": [
                {"label": "Government Resolution refused to accept G.K. Gokhale's demand for free compulsory primary education", "type": "leaf"},
                {"label": "Stated that universal compulsory education was premature, instead promising expansion of schools", "type": "leaf"},
                {"label": "Proposed establishing a teaching university in every province and improving secondary school standards", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अनिवार्यता का मुद्दा", "type": "branch", "date": "1913", "children": [
                {"label": "सरकारी प्रस्ताव ने मुफ़्त और अनिवार्य प्राथमिक शिक्षा की जी.के. गोखले की ऐतिहासिक मांग को खारिज कर दिया", "type": "leaf"},
                {"label": "कहा कि सार्वभौमिक अनिवार्य शिक्षा समय से पहले है, हालांकि स्कूलों के विस्तार का वादा किया गया", "type": "leaf"},
                {"label": "प्रत्येक प्रांत में एक शिक्षण विश्वविद्यालय स्थापित करने और माध्यमिक विद्यालयों के स्तर में सुधार का प्रस्ताव रखा", "type": "leaf"}]}
        ]
    },
    "saddler-commission": {
        "en": [
            {"label": "Sadler Commission", "type": "branch", "date": "1917-1919", "children": [
                {"label": "Sadler University Commission under Michael Sadler appointed to investigate Calcutta University's problems", "type": "leaf"},
                {"label": "Recommended a 12-year school course; intermediate stage separated from university entry", "type": "leaf"},
                {"label": "Proposed establishing Boards of Secondary and Intermediate Education in all provinces", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सैडलर आयोग", "type": "branch", "date": "1917-1919", "children": [
                {"label": "कलकत्ता विश्वविद्यालय की समस्याओं की जांच हेतु माइकल सैडलर के अधीन सैडलर विश्वविद्यालय आयोग नियुक्त", "type": "leaf"},
                {"label": "12 वर्षीय स्कूली पाठ्यक्रम की सिफारिश की; इंटरमीडिएट स्तर को विश्वविद्यालय प्रवेश से अलग किया गया", "type": "leaf"},
                {"label": "सभी प्रांतों में माध्यमिक और इंटरमीडिएट शिक्षा बोर्ड स्थापित करने का प्रस्ताव दिया", "type": "leaf"}]}
        ]
    },
    "education-under-dyarchy": {
        "en": [
            {"label": "Transferred Subject", "type": "branch", "date": "1919-1937", "children": [
                {"label": "Under Montagu-Chelmsford reforms, education was transferred to elected provincial Indian ministers", "type": "leaf"},
                {"label": "Faced severe financial starvation as finance remained a 'Reserved' subject under British council control", "type": "leaf"},
                {"label": "Indian ministers still managed to expand primary school networks using limited municipal taxes", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "हस्तांतरित विषय", "type": "branch", "date": "1919-1937", "children": [
                {"label": "मोंटेग्यू-चेम्सफोर्ड सुधारों के तहत, शिक्षा को निर्वाचित प्रांतीय भारतीय मंत्रियों को सौंप दिया गया था", "type": "leaf"},
                {"label": "गंभीर वित्तीय कमी का सामना करना पड़ा क्योंकि वित्त विभाग ब्रिटिश काउंसिल नियंत्रण के तहत 'आरक्षित' विषय था", "type": "leaf"},
                {"label": "इसके बावजूद भारतीय मंत्रियों ने स्थानीय नगर पालिका करों का उपयोग कर प्राथमिक स्कूलों के नेटवर्क का विस्तार किया", "type": "leaf"}]}
        ]
    },
    "hartog-committee": {
        "en": [
            {"label": "Wastage & Stagnation", "type": "branch", "date": "1929", "children": [
                {"label": "Hartog Committee (1929) appointed to report on growth and standard of education in British India", "type": "leaf"},
                {"label": "Pointed out high wastage (dropping out before finishing primary school) and stagnation (staying in same class)", "type": "leaf"},
                {"label": "Recommended consolidation and quality improvement rather than rapid expansion of primary schools", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अपव्यय और अवरोधन", "type": "branch", "date": "1929", "children": [
                {"label": "ब्रिटिश भारत में शिक्षा के विकास और स्तर पर रिपोर्ट प्रस्तुत करने हेतु हरटोग समिति (1929) नियुक्त", "type": "leaf"},
                {"label": "प्राथमिक स्तर पर भारी अपव्यय (बीच में स्कूल छोड़ना) और अवरोधन (एक ही कक्षा में रुके रहना) को रेखांकित किया", "type": "leaf"},
                {"label": "प्राथमिक स्कूलों के अंधाधुंध विस्तार के बजाय गुणवत्ता में सुधार और सुदृढ़ीकरण की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "wardha-scheme": {
        "en": [
            {"label": "Basic Education", "type": "branch", "date": "1937", "children": [
                {"label": "Wardha Scheme formulated by Gandhi (Harijan articles); detailed by Zakir Hussain Committee", "type": "leaf"},
                {"label": "Promoted 'Nai Talim' (learning through handicrafts); instruction in mother tongue; free compulsory education (7-14 years)", "type": "leaf"},
                {"label": "Aimed to make education self-supporting through sale of handicrafts produced by students", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "बुनियादी शिक्षा", "type": "branch", "date": "1937", "children": [
                {"label": "गांधीजी के हरिजन लेखों पर आधारित वर्धा योजना; डॉ. जाकिर हुसैन समिति द्वारा विस्तृत रिपोर्ट तैयार की गई", "type": "leaf"},
                {"label": "व्यवसाय-उन्मुख 'नई तालीम' (हस्तशिल्प आधारित शिक्षा), मातृभाषा माध्यम और 7-14 वर्ष के बच्चों हेतु मुफ़्त अनिवार्य शिक्षा", "type": "leaf"},
                {"label": "छात्रों द्वारा निर्मित हस्तशिल्प की बिक्री के माध्यम से शिक्षा को आत्मनिर्भर बनाना लक्ष्य था", "type": "leaf"}]}
        ]
    },
    "sergeant-plan": {
        "en": [
            {"label": "Sargent Plan", "type": "branch", "date": "1944", "children": [
                {"label": "Post-war educational development plan formulated by John Sargent (Educational Advisor to GoI)", "type": "leaf"},
                {"label": "Aimed to raise India's educational standards to Britain's level within a 40-year period", "type": "leaf"},
                {"label": "Proposed free compulsory education for ages 6-14; intermediate stage abolished; 3-year university course", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सार्जेंट योजना", "type": "branch", "date": "1944", "children": [
                {"label": "भारत सरकार के शैक्षिक सलाहकार जॉन सार्जेंट द्वारा तैयार युद्धोत्तर शैक्षिक विकास योजना", "type": "leaf"},
                {"label": "40 वर्षों की अवधि के भीतर भारत के शैक्षिक स्तर को ब्रिटेन के स्तर के बराबर लाने का लक्ष्य रखा", "type": "leaf"},
                {"label": "6-14 वर्ष के बच्चों हेतु मुफ़्त शिक्षा, इंटरमीडिएट स्तर की समाप्ति और 3 वर्षीय विश्वविद्यालय पाठ्यक्रम का प्रस्ताव", "type": "leaf"}]}
        ]
    },
    "kothari-commission": {
        "en": [
            {"label": "National Pattern", "type": "branch", "date": "1964-1966", "children": [
                {"label": "Kothari Education Commission chaired by Daulat Singh Kothari; first comprehensive policy in independent India", "type": "leaf"},
                {"label": "Recommended the 10+2+3 educational structure and spending 6% of GDP on education", "type": "leaf"},
                {"label": "Emphasized science education, vocationalization of schools, and standardizing teacher training", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राष्ट्रीय स्वरूप", "type": "branch", "date": "1964-1966", "children": [
                {"label": "दौलत सिंह कोठारी की अध्यक्षता में कोठारी शिक्षा आयोग; स्वतंत्र भारत की पहली व्यापक नीतिगत रूपरेखा", "type": "leaf"},
                {"label": "10+2+3 शैक्षिक संरचना और शिक्षा पर सकल घरेलू उत्पाद (GDP) का 6% खर्च करने की सिफारिश की", "type": "leaf"},
                {"label": "विज्ञान शिक्षा, स्कूलों के व्यावसायीकरण और शिक्षक प्रशिक्षण के मानकीकरण पर विशेष जोर दिया", "type": "leaf"}]}
        ]
    },
    "technical-education": {
        "en": [
            {"label": "Engineering & Medicine", "type": "branch", "date": "Institutions", "children": [
                {"label": "First engineering college set up at Roorkee (Thomason College, 1847) to train canal works engineers", "type": "leaf"},
                {"label": "Medical College Calcutta (1835) established by Lord William Bentinck; Bengal Engineering College Shibpur (1856)", "type": "leaf"},
                {"label": "Technical growth was slow, focusing only on lower administrative technical support", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "इंजीनियरिंग और चिकित्सा", "type": "branch", "date": "संस्थान", "children": [
                {"label": "नहर कार्यों हेतु इंजीनियरों को प्रशिक्षित करने के लिए रुड़की में पहला इंजीनियरिंग कॉलेज (थॉमसन कॉलेज, 1847) स्थापित", "type": "leaf"},
                {"label": "लॉर्ड विलियम बेंटिक द्वारा कलकत्ता मेडिकल कॉलेज (1835) की स्थापना; बंगाल इंजीनियरिंग कॉलेज शिबपुर (1856)", "type": "leaf"},
                {"label": "तकनीकी शिक्षा की गति अत्यंत धीमी थी, जिसका ध्यान केवल निचले प्रशासनिक तकनीकी सहयोग पर था", "type": "leaf"}]}
        ]
    },
    "vernacular-education": {
        "en": [
            {"label": "Local Initiatives", "type": "branch", "date": "Vernaculars", "children": [
                {"label": "William Adam's reports (1835-38) highlighted extensive network of traditional village schools (Pathshalas/Madrasas)", "type": "leaf"},
                {"label": "Wood's Despatch (1854) recommended regular inspection and system of grants-in-aid to boost local vernacular schools", "type": "leaf"},
                {"label": "Lord Curzon prioritized vernacular education; Hunter Commission (1882) transferred primary schools to local bodies", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थानीय पहल", "type": "branch", "date": "मातृभाषा", "children": [
                {"label": "विलियम एडम की रिपोर्ट (1835-38) ने पारंपरिक ग्रामीण स्कूलों (पाठशालाओं/मदरसों) के विस्तृत नेटवर्क को दर्शाया", "type": "leaf"},
                {"label": "वुड डिस्पैच (1854) ने स्थानीय स्कूलों को बढ़ावा देने हेतु सहायता अनुदान प्रणाली व नियमित निरीक्षण की सिफारिश की", "type": "leaf"},
                {"label": "लॉर्ड कर्जन ने स्थानीय शिक्षा को प्राथमिकता दी; हंटर कमीशन (1882) ने प्राथमिक विद्यालयों को स्थानीय निकायों को सौंपा", "type": "leaf"}]}
        ]
    },
    "british-policy-evaluation": {
        "en": [
            {"label": "Critical Analysis", "type": "branch", "date": "Evaluation", "children": [
                {"label": "Neglected Mass Education: Downward Filtration theory failed, leaving over 80% of Indians illiterate in 1947", "type": "leaf"},
                {"label": "Bureaucratic Focus: Aimed to produce English-speaking clerks to run low-cost colonial administration", "type": "leaf"},
                {"label": "Neglected Female Education: Ignored due to orthodoxy fears and lack of direct administrative utility", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आलोचनात्मक विश्लेषण", "type": "branch", "date": "मूल्यांकन", "children": [
                {"label": "जन-शिक्षा की उपेक्षा: अधोमुखी निस्यंदन (फिल्ट्रेशन) सिद्धांत विफल रहा, जिससे 1947 में 80% से अधिक आबादी निरक्षर थी", "type": "leaf"},
                {"label": "प्रशासनिक दृष्टिकोण: कम लागत वाली औपनिवेशिक मशीनरी चलाने हेतु अंग्रेजी बोलने वाले क्लर्क तैयार करना मुख्य उद्देश्य था", "type": "leaf"},
                {"label": "महिला शिक्षा की उपेक्षा: सामाजिक रूढ़िवादिता के भय और सीधे प्रशासनिक उपयोग न होने के कारण उपेक्षित रही", "type": "leaf"}]}
        ]
    },
    "administration-decentralization": {
        "en": [
            {"label": "Devolution of Control", "type": "branch", "date": "1854-1935", "children": [
                {"label": "Departments of Public Instruction created in all provinces after Wood's Despatch (1854)", "type": "leaf"},
                {"label": "Local bodies (District Boards/Municipalities) given control of primary schools under Hunter Commission (1882)", "type": "leaf"},
                {"label": "Provincial Autonomy (1935 Act) completed devolution, handing education entirely to provincial governments", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नियंत्रण का हस्तांतरण", "type": "branch", "date": "1854-1935", "children": [
                {"label": "वुड डिस्पैच (1854) के बाद सभी प्रांतों में जन शिक्षा विभागों (DPI) की स्थापना की गई थी", "type": "leaf"},
                {"label": "हंटर आयोग (1882) के तहत प्राथमिक विद्यालयों का नियंत्रण स्थानीय निकायों (जिला बोर्डों/नगर पालिकाओं) को दिया गया", "type": "leaf"},
                {"label": "प्रांतीय स्वायत्तता (1935 अधिनियम) ने इस प्रक्रिया को पूरा कर शिक्षा को पूरी तरह प्रांतीय सरकारों के अधीन किया", "type": "leaf"}]}
        ]
    },
    "post-1857-changes": {
        "en": [
            {"label": "Crown Takeover", "type": "branch", "date": "Post-1857", "children": [
                {"label": "Universities of Calcutta, Bombay, and Madras established in late 1857 modeled on London University", "type": "leaf"},
                {"label": "Shift from EIC patronage to direct Crown control; promotion of grant-in-aid system for private colleges", "type": "leaf"},
                {"label": "Increased government intervention to regulate political activity among Indian intelligentsia", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "क्राउन का नियंत्रण", "type": "branch", "date": "1857 के बाद", "children": [
                {"label": "लंदन विश्वविद्यालय की तर्ज पर 1857 के उत्तरार्ध में कलकत्ता, बॉम्बे और मद्रास विश्वविद्यालयों की स्थापना हुई", "type": "leaf"},
                {"label": "ईस्ट इंडिया कंपनी के संरक्षण से हटकर सीधे क्राउन के नियंत्रण में बदलाव; निजी कॉलेजों हेतु सहायता अनुदान को बढ़ावा", "type": "leaf"},
                {"label": "भारतीय बुद्धिजीवियों के बीच राजनीतिक गतिविधियों को नियंत्रित करने के लिए सरकारी हस्तक्षेप में वृद्धि हुई", "type": "leaf"}]}
        ]
    }
}

# Mapping all 26 folders to the canonical keys
MINDMAP_MAPPINGS = {
    "charter-act-of-1813": "charter-act-of-1813",
    "orientalist-anglicist-controversy": "orientalist-anglicist-controversy",
    "general-committee-of-public-instruction": "general-committee-of-public-instruction",
    "woods-dispatch": "woods-dispatch",
    "woods-dispatch-1854": "woods-dispatch",
    "hunter-education-commission": "hunter-commission",
    "hunter-education-commission-1882-83": "hunter-commission",
    "indian-universities-act-1904": "indian-universities-act-1904",
    "government-resolution-on-education-policy1913": "resolution-on-education-policy-1913",
    "saddler-university-commission": "saddler-commission",
    "saddler-university-commission-1917-19": "saddler-commission",
    "education-under-dyarchy": "education-under-dyarchy",
    "hartog-committee": "hartog-committee",
    "hartog-committee-1929": "hartog-committee",
    "wardha-scheme-of-basic-education": "wardha-scheme",
    "wardha-scheme-of-basic-education-1937": "wardha-scheme",
    "sergeant-plan-of-education": "sergeant-plan",
    "kothari-education-commission": "kothari-commission",
    "kothari-education-commission-1964-66": "kothari-commission",
    "development-of-technical-education": "technical-education",
    "development-of-vernacular-education": "vernacular-education",
    "evaluation-of-british-policy-on-education": "british-policy-evaluation",
    "administration-central-provincial-local": "administration-decentralization",
    "administration-central-provincial-local-education": "administration-decentralization",
    "changed-government-post-1857": "post-1857-changes",
    "acts-between-1858-1947": "post-1857-changes"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('EIC', 'EIC (East India Company)')
    title = title.replace('policy1913', 'Policy 1913')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, "charter-act-of-1813")
    
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
