#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/First-Phase-of-National-Movement-1905-1917"

MINDMAP_DATA = {
    "annulment-of-partition-of-bengal": {
        "en": [
            {"label": "The Decision", "type": "branch", "date": "1911", "children": [
                {"label": "Annulled at the Delhi Durbar in 1911 by Lord Hardinge to curb revolutionary terrorism", "type": "leaf"},
                {"label": "Capital shifted from Calcutta to Delhi in the same declaration to placate Muslims", "type": "leaf"}]},
            {"label": "Territorial Adjustments", "type": "branch", "date": "1911", "children": [
                {"label": "Bihar and Orissa separated from Bengal; Assam constituted as a separate province", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विभाजन रद्द होने का निर्णय", "type": "branch", "date": "1911", "children": [
                {"label": "क्रांतिकारी आतंकवाद पर अंकुश लगाने हेतु 1911 में दिल्ली दरबार में लॉर्ड हार्डिंग द्वारा रद्द किया गया", "type": "leaf"},
                {"label": "मुसलमानों को शांत करने हेतु इसी घोषणा में राजधानी को कलकत्ता से दिल्ली स्थानांतरित किया गया", "type": "leaf"}]},
            {"label": "क्षेत्रीय पुनर्गठन", "type": "branch", "date": "1911", "children": [
                {"label": "बिहार और उड़ीसा को बंगाल से पृथक किया गया; असम को एक अलग प्रांत घोषित किया गया", "type": "leaf"}]}
        ]
    },
    "campaign-for-general-administrative-reforms": {
        "en": [
            {"label": "Moderate Demands", "type": "branch", "date": "Demands", "children": [
                {"label": "Indianisation of government services to reduce drain of wealth on salaries/pensions", "type": "leaf"},
                {"label": "Separation of judiciary from executive functions to ensure fair trials", "type": "leaf"},
                {"label": "Opposed the gagging of press and demanded freedom of speech & association", "type": "leaf"},
                {"label": "Reduction of military expenditure to spend more on public education & health", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उदारवादी मांगें", "type": "branch", "date": "मांगें", "children": [
                {"label": "वेतन और पेंशन के रूप में होने वाले धन निष्कासन को रोकने हेतु सरकारी सेवाओं का भारतीयकरण", "type": "leaf"},
                {"label": "निष्पक्ष सुनवाई सुनिश्चित करने हेतु न्यायपालिका को कार्यपालिका से अलग करने की मांग", "type": "leaf"},
                {"label": "प्रेस पर प्रतिबंधों का विरोध और अभिव्यक्ति व संगठन बनाने की स्वतंत्रता की मांग", "type": "leaf"},
                {"label": "जन शिक्षा और स्वास्थ्य पर अधिक व्यय करने हेतु सैन्य खर्चों में कटौती की मांग", "type": "leaf"}]}
        ]
    },
    "chittagong-revolt-group": {
        "en": [
            {"label": "The Raid", "type": "branch", "date": "April 1930", "children": [
                {"label": "Led by Surya Sen (Masterda) along with Kalpana Dutt, Pritilata Wadedar, Lokenath Bal", "type": "leaf"},
                {"label": "Planned to capture two main armouries in Chittagong, cut telephone/telegraph lines, and disrupt railways", "type": "leaf"},
                {"label": "Succeeded in cutting communications and hoisted national flag, proclaiming a provisional revolutionary government", "type": "leaf"}]},
            {"label": "Aftermath", "type": "branch", "date": "Suppression", "children": [
                {"label": "Battle of Jalalabad Hills: Outnumbered revolutionaries fought British army troops", "type": "leaf"},
                {"label": "Surya Sen captured in 1933 and hanged in 1934; Pritilata consumed cyanide to avoid arrest", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "शस्त्रागार छापा", "type": "branch", "date": "अप्रैल 1930", "children": [
                {"label": "सूर्य सेन (मास्टरदा) के साथ कल्पना दत्त, प्रीतिलता वाडेदार और लोकनाथ बल के नेतृत्व में योजना", "type": "leaf"},
                {"label": "चटगाँव के दो मुख्य शस्त्रागारों पर कब्जा करने, टेलीफोन/टेलीग्राफ लाइनों को काटने और रेलवे को बाधित करने का प्रयास", "type": "leaf"},
                {"label": "संचार काटने में सफल रहे और राष्ट्रीय ध्वज फहराकर एक अस्थायी क्रांतिकारी सरकार की घोषणा की", "type": "leaf"}]},
            {"label": "परिणाम", "type": "branch", "date": "दमन", "children": [
                {"label": "जलालाबाद की पहाड़ियों का युद्ध: संख्या में कम क्रांतिकारियों ने ब्रिटिश सेना के साथ डटकर मुकाबला किया", "type": "leaf"},
                {"label": "1933 में सूर्य सेन पकड़े गए और 1934 में फांसी दी गई; प्रीतिलता ने गिरफ्तारी से बचने हेतु सायनाइड खा लिया", "type": "leaf"}]}
        ]
    },
    "comparative-account-of-moderates-and-extremists": {
        "en": [
            {"label": "Moderates", "type": "branch", "date": "1885-1905", "children": [
                {"label": "Social Base: Zamindars and upper-middle-class professionals (lawyers, doctors)", "type": "leaf"},
                {"label": "Method: Constitutional agitation within laws (3Ps - Petitions, Prayers, Protests)", "type": "leaf"},
                {"label": "Goal: Administrative reforms and self-government within the British Empire", "type": "leaf"}]},
            {"label": "Extremists", "type": "branch", "date": "1905-1917", "children": [
                {"label": "Social Base: Lower-middle class, students, and urban workers", "type": "leaf"},
                {"label": "Method: Swadeshi, Boycott, National Education, and Passive Resistance (satyagraha)", "type": "leaf"},
                {"label": "Goal: Swaraj (complete independence) and end of British rule", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उदारवादी (नरम दल)", "type": "branch", "date": "1885-1905", "children": [
                {"label": "सामाजिक आधार: जमींदार और उच्च-मध्यम वर्ग के पेशेवर (वकील, डॉक्टर)", "type": "leaf"},
                {"label": "कार्यप्रणाली: कानून के दायरे में संवैधानिक आंदोलन (3Ps - याचिका, प्रार्थना, विरोध)", "type": "leaf"},
                {"label": "लक्ष्य: ब्रिटिश साम्राज्य के भीतर प्रशासनिक सुधार और स्वशासन", "type": "leaf"}]},
            {"label": "उग्रवादी (गरम दल)", "type": "branch", "date": "1905-1917", "children": [
                {"label": "सामाजिक आधार: निम्न-मध्यम वर्ग, छात्र और शहरी श्रमिक", "type": "leaf"},
                {"label": "कार्यप्रणाली: स्वदेशी, बहिष्कार, राष्ट्रीय शिक्षा और निष्क्रिय प्रतिरोध", "type": "leaf"},
                {"label": "लक्ष्य: स्वराज (पूर्ण स्वतंत्रता) और ब्रिटिश शासन का अंत", "type": "leaf"}]}
        ]
    },
    "constitutional-reforms-and-propaganda-in-legislature": {
        "en": [
            {"label": "Early Legislatures", "type": "branch", "date": "1892 Reforms", "children": [
                {"label": "Indian Councils Act 1892 marginally expanded councils but lacked representative power", "type": "leaf"},
                {"label": "Nationalists used councils as forums for political propaganda to expose British economic exploitation", "type": "leaf"},
                {"label": "G.K. Gokhale's budget speeches systematically dissected imperial financial policies", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक विधायिकाएं", "type": "branch", "date": "1892 के सुधार", "children": [
                {"label": "भारतीय परिषद अधिनियम 1892 ने आंशिक रूप से परिषदों का विस्तार किया परंतु वास्तविक प्रतिनिधित्व का अभाव था", "type": "leaf"},
                {"label": "राष्ट्रवादियों ने परिषदों का उपयोग ब्रिटिश आर्थिक शोषण को उजागर करने और प्रचार मंच के रूप में किया", "type": "leaf"},
                {"label": "जी.के. गोखले के बजट भाषणों ने साम्राज्यवादी वित्तीय नीतियों का व्यवस्थित विश्लेषण प्रस्तुत किया", "type": "leaf"}]}
        ]
    },
    "debate-over-inc-being-a-safety-valve": {
        "en": [
            {"label": "Safety Valve Theory", "type": "branch", "date": "Conspiracy", "children": [
                {"label": "Lala Lajpat Rai propounded that INC was formed by A.O. Hume under Lord Dufferin to prevent a popular revolt", "type": "leaf"},
                {"label": "Claimed British wanted a safe forum to release rising public discontent", "type": "leaf"}]},
            {"label": "Lightning Conductor", "type": "branch", "date": "Reality", "children": [
                {"label": "G.K. Gokhale stated that early nationalists used Hume as a 'lightning conductor' to avoid government suppression", "type": "leaf"},
                {"label": "Hume acted as a shield; British wouldn't ban an organization founded by a retired British civil servant", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सेफ्टी वाल्व सिद्धांत", "type": "branch", "date": "साजिश", "children": [
                {"label": "लाला लाजपत राय ने प्रतिपादित किया कि जन विद्रोह रोकने हेतु लॉर्ड डफरिन के निर्देश पर ए.ओ. ह्यूम द्वारा कांग्रेस बनाई गई थी", "type": "leaf"},
                {"label": "दावा किया कि ब्रिटिश बढ़ते जन आक्रोश को सुरक्षित रूप से बाहर निकालने के लिए एक मंच चाहते थे", "type": "leaf"}]},
            {"label": "तड़ित चालक सिद्धांत", "type": "branch", "date": "वास्तविकता", "children": [
                {"label": "जी.के. गोखले ने कहा कि प्रारंभिक राष्ट्रवादियों ने सरकारी दमन से बचने हेतु ह्यूम का 'तड़ित चालक' के रूप में उपयोग किया", "type": "leaf"},
                {"label": "ह्यूम ने सुरक्षा कवच का काम किया; ब्रिटिश अधिकारी अपने ही एक सेवानिवृत्त अधिकारी द्वारा स्थापित संस्था को आसानी से प्रतिबंधित नहीं कर सकते थे", "type": "leaf"}]}
        ]
    },
    "developments-that-led-to-home-rule-league": {
        "en": [
            {"label": "Context of 1915", "type": "branch", "date": "Triggers", "children": [
                {"label": "Release of Bal Gangadhar Tilak in 1914 after 6 years of imprisonment in Mandalay", "type": "leaf"},
                {"label": "Discontent with Morley-Minto Reforms (1909); economic distress of WWI (high taxation/inflation)", "type": "leaf"},
                {"label": "Annie Besant proposed a movement on Irish Home Rule model to revitalize national political struggle", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "1915 का संदर्भ", "type": "branch", "date": "उत्प्रेरक", "children": [
                {"label": "मांडले जेल में 6 साल के कारावास के बाद 1914 में बाल गंगाधर तिलक की रिहाई", "type": "leaf"},
                {"label": "मार्ले-मिंटो सुधारों (1909) से असंतोष; प्रथम विश्व युद्ध के कारण उत्पन्न आर्थिक संकट (कर और मुद्रास्फीति)", "type": "leaf"},
                {"label": "राष्ट्रीय संघर्ष को पुनर्जीवित करने हेतु एनी बेसेंट द्वारा आयरिश होम रूल की तर्ज पर आंदोलन का प्रस्ताव", "type": "leaf"}]}
        ]
    },
    "differences-between-the-moderates-and-the-extemists": {
        "en": [
            {"label": "Key Differences", "type": "branch", "date": "Rift", "children": [
                {"label": "Moderates believed in loyalty to Crown and British sense of justice; Extremists rejected crown loyalty", "type": "leaf"},
                {"label": "Moderates wanted expansion of assemblies; Extremists wanted complete Swaraj (self-rule)", "type": "leaf"},
                {"label": "Moderates feared mass movements; Extremists relied on mass mobilization and youth participation", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य अंतर", "type": "branch", "date": "मतभेद", "children": [
                {"label": "उदारवादी ब्रिटिश ताज के प्रति वफादारी और न्यायप्रियता में विश्वास रखते थे; उग्रवादियों ने इसे नकारा", "type": "leaf"},
                {"label": "उदारवादी परिषदों के विस्तार पर केंद्रित थे; उग्रवादी पूर्ण स्वराज (आत्म-शासन) चाहते थे", "type": "leaf"},
                {"label": "उदारवादी जन आंदोलनों से आशंकित थे; उग्रवादी जनसमूह और युवाओं की भागीदारी पर निर्भर थे", "type": "leaf"}]}
        ]
    },
    "early-phase-indian-national-congress": {
        "en": [
            {"label": "Foundation", "type": "branch", "date": "Dec 1885", "children": [
                {"label": "First session at Gokuldas Tejpal Sanskrit College, Bombay; attended by 72 delegates", "type": "leaf"},
                {"label": "President: W.C. Bonnerjee; Founder/General Secretary: Allan Octavian Hume", "type": "leaf"},
                {"label": "Major aims: Develop national unity, present popular demands, coordinate political workers", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थापना", "type": "branch", "date": "दिसंबर 1885", "children": [
                {"label": "प्रथम अधिवेशन गोकुलदास तेजपाल संस्कृत कॉलेज, बॉम्बे में आयोजित; 72 प्रतिनिधियों ने भाग लिया", "type": "leaf"},
                {"label": "अध्यक्ष: डब्ल्यू.सी. बनर्जी; संस्थापक/महासचिव: एलन ऑक्टेवियन ह्यूम", "type": "leaf"},
                {"label": "मुख्य उद्देश्य: राष्ट्रीय एकता का विकास, लोकप्रिय मांगों को प्रस्तुत करना, राजनीतिक कार्यकर्ताओं में समन्वय", "type": "leaf"}]}
        ]
    },
    "economic-critique-of-imperialism": {
        "en": [
            {"label": "Drain of Wealth", "type": "branch", "date": "Critique", "children": [
                {"label": "Dadabhai Naoroji: Described the drain of wealth in 'Poverty and Un-British Rule in India' (1901)", "type": "leaf"},
                {"label": "R.C. Dutt: Analyzed how colonial tariffs destroyed Indian cotton and handicraft industries in 'Economic History of India'", "type": "leaf"},
                {"label": "Exposed home charges, military expenses, and guaranteed railway interest as drains on Indian tax revenue", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "धन का निष्कासन", "type": "branch", "date": "आलोचना", "children": [
                {"label": "दादाभाई नौरोजी: 'पॉवर्टी एंड अन-ब्रिटिश रूल इन इंडिया' (1901) में धन निष्कासन का व्यवस्थित विवरण दिया", "type": "leaf"},
                {"label": "आर.सी. दत्त: अपनी पुस्तक 'इकोनॉमिक हिस्ट्री ऑफ इंडिया' में विश्लेषण किया कि कैसे औपनिवेशिक शुल्कों ने भारतीय सूती और हस्तशिल्प उद्योग को नष्ट किया", "type": "leaf"},
                {"label": "गृह प्रभार, सैन्य खर्चों और गारंटीकृत रेलवे ब्याज को भारतीय राजस्व के दोहन के रूप में उजागर किया", "type": "leaf"}]}
        ]
    },
    "government-repression": {
        "en": [
            {"label": "Repressive Acts", "type": "branch", "date": "1907-1910", "children": [
                {"label": "Seditious Meetings Act (1907): Banned public meetings without prior police permission", "type": "leaf"},
                {"label": "Indian Newspapers Act (1908): Allowed confiscation of printing presses publishing objectionable material", "type": "leaf"},
                {"label": "Indian Press Act (1910): Demanded heavy security deposits from presses to suppress national publications", "type": "leaf"},
                {"label": "Mandalay Exile: Tilak was deported to Burma in 1908 for 6 years under sedition charges", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दमनकारी अधिनियम", "type": "branch", "date": "1907-1910", "children": [
                {"label": "राजद्रोहात्मक सभा अधिनियम (1907): बिना पुलिस अनुमति के सार्वजनिक सभाओं पर प्रतिबंध लगाया", "type": "leaf"},
                {"label": "भारतीय समाचार पत्र अधिनियम (1908): आपत्तिजनक सामग्री छापने वाले प्रिंटिंग प्रेसों को जब्त करने की अनुमति दी", "type": "leaf"},
                {"label": "भारतीय प्रेस अधिनियम (1910): राष्ट्रीय प्रकाशनों को दबाने के लिए प्रेसों से भारी सुरक्षा जमा राशि की मांग की", "type": "leaf"},
                {"label": "मांडले निर्वासन: राजद्रोह के आरोप में तिलक को 1908 में 6 साल के लिए बर्मा (म्यांमार) निर्वासित किया गया", "type": "leaf"}]}
        ]
    },
    "governments-response-towards-inc": {
        "en": [
            {"label": "Shift in Attitude", "type": "branch", "date": "1885-1888", "children": [
                {"label": "Initial neutrality: British officials attended early sessions as observers", "type": "leaf"},
                {"label": "Lord Dufferin (1888): Attacked INC as representing only a 'microscopic minority' of the population", "type": "leaf"},
                {"label": "George Yule session (1888): Government tried to prevent delegates from obtaining meeting venues", "type": "leaf"},
                {"label": "Official ban: Government servants banned from attending INC sessions or collecting funds", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "दृष्टिकोण में बदलाव", "type": "branch", "date": "1885-1888", "children": [
                {"label": "प्रारंभिक तटस्थता: ब्रिटिश अधिकारी शुरुआत में केवल पर्यवेक्षक के रूप में शामिल हुए", "type": "leaf"},
                {"label": "लॉर्ड डफरिन (1888): कांग्रेस पर हमला करते हुए इसे जनता के केवल 'अति सूक्ष्म अल्पसंख्यक' हिस्से का प्रतिनिधित्व करने वाला बताया", "type": "leaf"},
                {"label": "जॉर्ज यूल अधिवेशन (1888): सरकार ने प्रतिनिधियों को बैठक स्थल प्राप्त करने से रोकने का प्रयास किया", "type": "leaf"},
                {"label": "सरकारी प्रतिबंध: सरकारी कर्मचारियों के कांग्रेस सम्मेलनों में भाग लेने या धन संग्रह करने पर पूर्ण रोक लगाई गई", "type": "leaf"}]}
        ]
    },
    "hindustan-republican-association": {
        "en": [
            {"label": "Foundation", "type": "branch", "date": "1924 Kanpur", "children": [
                {"label": "Founded by Ram Prasad Bismil, Sachindra Nath Sanyal, Jogesh Chandra Chatterjee", "type": "leaf"},
                {"label": "Goal: Establish a Federal Republic of United States of India through armed revolution", "type": "leaf"}]},
            {"label": "Kakori Action", "type": "branch", "date": "Aug 1925", "children": [
                {"label": "Kakori Train Robbery: Held up 8-Down train near Kakori to secure funds for weapon purchase", "type": "leaf"},
                {"label": "Bismil, Ashfaqullah Khan, Roshan Singh, and Rajendra Lahiri hanged; Chandrashekhar Azad escaped", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थापना", "type": "branch", "date": "1924 कानपुर", "children": [
                {"label": "राम प्रसाद बिस्मिल, सचिंद्र नाथ सान्याल और योगेश चंद्र चटर्जी द्वारा स्थापित", "type": "leaf"},
                {"label": "लक्ष्य: सशस्त्र क्रांति के माध्यम से भारत के संयुक्त राज्य के एक संघीय गणराज्य की स्थापना करना", "type": "leaf"}]},
            {"label": "काकोरी कांड", "type": "branch", "date": "अगस्त 1925", "children": [
                {"label": "काकोरी ट्रेन डकैती: हथियारों की खरीद हेतु धन जुटाने के लिए काकोरी के पास 8-डाउन ट्रेन को लूटा", "type": "leaf"},
                {"label": "बिस्मिल, अशफाकउल्ला खान, रोशन सिंह और राजेंद्र लाहिड़ी को फांसी; चंद्रशेखर आजाद फरार होने में सफल रहे", "type": "leaf"}]}
        ]
    },
    "home-rule-league-movement-1916": {
        "en": [
            {"label": "Tilak's League", "type": "branch", "date": "April 1916", "children": [
                {"label": "Active in Maharashtra (excl. Bombay), Karnataka, Central Provinces, Berar; 6 branches", "type": "leaf"},
                {"label": "Propagated Swaraj using Kesari (Marathi) and Mahratta (English) newspapers", "type": "leaf"}]},
            {"label": "Besant's League", "type": "branch", "date": "Sept 1916", "children": [
                {"label": "Active across rest of India; 200 branches; coordinated by Arundale, CP Ramaswamy Aiyar", "type": "leaf"},
                {"label": "Propagated self-rule using New India and Commonweal newspapers", "type": "leaf"}]},
            {"label": "Impact", "type": "branch", "date": "Outcome", "children": [
                {"label": "Popularized demand for home rule (Swaraj) among masses; paved way for Montague declaration", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "तिलक की लीग", "type": "branch", "date": "अप्रैल 1916", "children": [
                {"label": "महाराष्ट्र (बॉम्बे को छोड़कर), कर्नाटक, मध्य प्रांत, बरार में सक्रिय; 6 शाखाएं थीं", "type": "leaf"},
                {"label": "केसरी (मराठी) और महरत्ता (अंग्रेजी) समाचार पत्रों द्वारा स्वराज का प्रचार किया", "type": "leaf"}]},
            {"label": "बेसेंट की लीग", "type": "branch", "date": "सितंबर 1916", "children": [
                {"label": "शेष भारत में सक्रिय; 200 शाखाएं; अरुंडेल और सी.पी. रामास्वामी अय्यर द्वारा समन्वित", "type": "leaf"},
                {"label": "न्यू इंडिया और कॉमनवील समाचार पत्रों के माध्यम से स्वशासन का प्रचार किया", "type": "leaf"}]},
            {"label": "प्रभाव", "type": "branch", "date": "परिणाम", "children": [
                {"label": "जनता के बीच गृह शासन (स्वराज) की मांग को लोकप्रिय बनाया; मोंटेग्यू घोषणा का मार्ग प्रशस्त किया", "type": "leaf"}]}
        ]
    },
    "important-inc-sessions-extremist-phase": {
        "en": [
            {"label": "Key Sessions", "type": "branch", "date": "1905-1907", "children": [
                {"label": "Banaras 1905 (G.K. Gokhale): Formally protested the partition of Bengal; supported Swadeshi", "type": "leaf"},
                {"label": "Calcutta 1906 (Dadabhai Naoroji): Declared goal of INC was 'Swaraj' (like UK colonies)", "type": "leaf"},
                {"label": "Surat 1907 (Rash Behari Ghosh): Surat split; Moderates suspended Extremists from the Congress", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख अधिवेशन", "type": "branch", "date": "1905-1907", "children": [
                {"label": "बनारस 1905 (जी.के. गोखले): बंगाल विभाजन का औपचारिक विरोध; स्वदेशी आंदोलन का समर्थन", "type": "leaf"},
                {"label": "कलकत्ता 1906 (दादाभाई नौरोजी): कांग्रेस का लक्ष्य 'स्वराज' घोषित किया (ब्रिटिश उपनिवेशों की तर्ज पर)", "type": "leaf"},
                {"label": "सूरत 1907 (रास बिहारी घोष): सूरत विभाजन; उदारवादियों ने उग्रवादियों को कांग्रेस से बाहर किया", "type": "leaf"}]}
        ]
    },
    "key-sessions-of-the-indian-national-congress-inc": {
        "en": [
            {"label": "Notable Sessions", "type": "branch", "date": "1885-1888", "children": [
                {"label": "Bombay 1885: 1st Session; W.C. Bonnerjee presided; 72 delegates attended", "type": "leaf"},
                {"label": "Calcutta 1886: 2nd Session; Dadabhai Naoroji presided; merged National Conference into INC", "type": "leaf"},
                {"label": "Madras 1887: 3rd Session; Badruddin Tyabji presided (first Muslim President)", "type": "leaf"},
                {"label": "Allahabad 1888: 4th Session; George Yule presided (first European President)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "महत्वपूर्ण अधिवेशन", "type": "branch", "date": "1885-1888", "children": [
                {"label": "बॉम्बे 1885: प्रथम अधिवेशन; डब्ल्यू.सी. बनर्जी ने अध्यक्षता की; 72 प्रतिनिधि शामिल हुए", "type": "leaf"},
                {"label": "कलकत्ता 1886: द्वितीय अधिवेशन; दादाभाई नौरोजी ने अध्यक्षता की; नेशनल कॉन्फ्रेंस का विलय हुआ", "type": "leaf"},
                {"label": "मद्रास 1887: तृतीय अधिवेशन; बदरुद्दीन तैयबजी ने अध्यक्षता की (पहले मुस्लिम अध्यक्ष)", "type": "leaf"},
                {"label": "इलाहाबाद 1888: चतुर्थ अधिवेशन; जॉर्ज यूल ने अध्यक्षता की (पहले यूरोपीय अध्यक्ष)", "type": "leaf"}]}
        ]
    },
    "limitations-with-home-rule-leagues": {
        "en": [
            {"label": "Weaknesses", "type": "branch", "date": "Limitations", "children": [
                {"label": "Remained confined to educated middle class & urban areas; failed to gain mass peasant support", "type": "leaf"},
                {"label": "Opposed by non-Brahmins in Madras (who feared Brahmin dominance) and Anglo-Indians", "type": "leaf"},
                {"label": "Muslims largely kept away as they demanded separate political assurances", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कमजोरियां", "type": "branch", "date": "सीमाएं", "children": [
                {"label": "केवल शिक्षित मध्यम वर्ग और शहरी क्षेत्रों तक सीमित रहा; किसानों का व्यापक समर्थन पाने में विफल", "type": "leaf"},
                {"label": "मद्रास में गैर-ब्राह्मणों (जिन्हें ब्राह्मण वर्चस्व का भय था) और एंग्लो-इंडियंस द्वारा विरोध किया गया", "type": "leaf"},
                {"label": "मुसलमान बड़े पैमाने पर दूर रहे क्योंकि वे अलग राजनीतिक आश्वासनों की मांग कर रहे थे", "type": "leaf"}]}
        ]
    },
    "lucknow-session-of-inc-1916-lucknow-pact": {
        "en": [
            {"label": "Lucknow Pact", "type": "branch", "date": "Dec 1916", "children": [
                {"label": "Presided by Ambica Charan Mazumdar; Extremists readmitted to Congress after 9-year split", "type": "leaf"},
                {"label": "Lucknow Pact signed: Congress and Muslim League agreed on joint constitutional demands", "type": "leaf"},
                {"label": "Congress accepted separate electorates for Muslims, which later legitimized two-nation theory", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लखनऊ समझौता", "type": "branch", "date": "दिसंबर 1916", "children": [
                {"label": "अंबिका चरण मजूमदार द्वारा अध्यक्षता; 9 वर्ष के अलगाव के बाद गरम दल का कांग्रेस में पुनः प्रवेश", "type": "leaf"},
                {"label": "लखनऊ पैक्ट पर हस्ताक्षर: कांग्रेस और मुस्लिम लीग संयुक्त संवैधानिक मांगों पर सहमत हुए", "type": "leaf"},
                {"label": "कांग्रेस ने मुसलमानों के लिए पृथक निर्वाचन को स्वीकार किया, जिसने बाद में द्वि-राष्ट्र सिद्धांत को वैधता दी", "type": "leaf"}]}
        ]
    },
    "mass-participation-extremist-phase": {
        "en": [
            {"label": "Key Groups", "type": "branch", "date": "1905-1908", "children": [
                {"label": "Students: Boycotted schools/colleges; formed volunteer corps (Samitis) like Swadesh Bandhab Samiti", "type": "leaf"},
                {"label": "Women: Picketed foreign cloth & liquor shops; refused to wear foreign glass bangles", "type": "leaf"},
                {"label": "Labor: Strikes in railways, government printing presses, and cotton mills in Madras & Bengal", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख समूह", "type": "branch", "date": "1905-1908", "children": [
                {"label": "छात्र: स्कूलों/कॉलेजों का बहिष्कार किया; स्वदेश बांधव समिति जैसे स्वयंसेवक दलों का गठन किया", "type": "leaf"},
                {"label": "महिलाएं: विदेशी कपड़ों व शराब की दुकानों पर धरना दिया; विदेशी कांच की चूड़ियां पहनने से मना किया", "type": "leaf"},
                {"label": "श्रमिक: मद्रास और बंगाल में रेलवे, सरकारी प्रिंटिंग प्रेसों और सूती मिलों में हड़तालें कीं", "type": "leaf"}]}
        ]
    },
    "militant-nationalism-1905-to-1918": {
        "en": [
            {"label": "Causes of Rise", "type": "branch", "date": "Factors", "children": [
                {"label": "Disillusionment with moderate methods of petitions and lack of constitutional results", "type": "leaf"},
                {"label": "Reactionary policies of Lord Curzon (Calcutta Corporation Act, Universities Act, Partition of Bengal)", "type": "leaf"},
                {"label": "International events: Japan's victory over Russia (1905) exploded myth of European invincibility", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उदय के कारण", "type": "branch", "date": "कारक", "children": [
                {"label": "याचिकाओं और संवैधानिक तरीकों के बावजूद परिणाम न मिलने से उदारवादी नीतियों से मोहभंग", "type": "leaf"},
                {"label": "लॉर्ड कर्जन की प्रतिक्रियावादी नीतियां (कलकत्ता कॉर्पोरेशन एक्ट, विश्वविद्यालय अधिनियम, बंगाल विभाजन)", "type": "leaf"},
                {"label": "अंतर्राष्ट्रीय घटनाएं: 1905 में रूस पर जापान की विजय ने यूरोपीय देशों की अजेयता के मिथक को तोड़ा", "type": "leaf"}]}
        ]
    },
    "moderate-campaign-for-administrative-reforms": {
        "en": [
            {"label": "Demands", "type": "branch", "date": "Campaign", "children": [
                {"label": "Indianisation of Civil Services (simultaneous exams in India & London)", "type": "leaf"},
                {"label": "Repeal of Arms Act 1878; demanded right to bear arms for self-defense", "type": "leaf"},
                {"label": "Increased spending on irrigation and education; reduction in military budget", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मांगें", "type": "branch", "date": "अभियान", "children": [
                {"label": "सिविल सेवाओं का भारतीयकरण (भारत और लंदन में एक साथ परीक्षा के आयोजन की मांग)", "type": "leaf"},
                {"label": "शस्त्र अधिनियम 1878 को निरस्त करना; आत्मरक्षा के लिए हथियार रखने के अधिकार की मांग", "type": "leaf"},
                {"label": "सिंचाई और शिक्षा पर खर्च में वृद्धि; सैन्य बजट में कटौती की मांग की", "type": "leaf"}]}
        ]
    },
    "moderate-campaign-for-constitutional-reforms": {
        "en": [
            {"label": "Legislative Demands", "type": "branch", "date": "Campaign", "children": [
                {"label": "Expansion and reform of Imperial and Provincial Legislative Councils", "type": "leaf"},
                {"label": "Demanded budget voting power and right to ask supplementary questions", "type": "leaf"},
                {"label": "Slogan: 'No taxation without representation', inspired by American revolution", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संवैधानिक मांगें", "type": "branch", "date": "अभियान", "children": [
                {"label": "साम्राज्यीय और प्रांतीय विधायी परिषदों का विस्तार और लोकतांत्रिक सुधार", "type": "leaf"},
                {"label": "बजट पर मतदान का अधिकार और पूरक प्रश्न पूछने की अनुमति की मांग की", "type": "leaf"},
                {"label": "नारा: अमेरिकी क्रांति से प्रेरित होकर 'बिना प्रतिनिधित्व के कोई कर नहीं' का नारा दिया", "type": "leaf"}]}
        ]
    },
    "moderate-opinion-against-economic-exploitation": {
        "en": [
            {"label": "Economic Critique", "type": "branch", "date": "Exploitation", "children": [
                {"label": "Exposed that British rule systematically drained Indian wealth and deindustrialized the country", "type": "leaf"},
                {"label": "Opposed high land revenue taxes and salt tax that burdened poor peasants", "type": "leaf"},
                {"label": "Demanded protective tariffs to safeguard nascent Indian cotton and sugar industries", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आर्थिक आलोचना", "type": "branch", "date": "शोषण", "children": [
                {"label": "उजागर किया कि ब्रिटिश शासन ने भारत के धन का दोहन किया और देश को वि-औद्योगिक बनाया", "type": "leaf"},
                {"label": "गरीब किसानों पर बोझ डालने वाले अत्यधिक भू-राजस्व और नमक कर का विरोध किया", "type": "leaf"},
                {"label": "नवजात भारतीय सूती और चीनी उद्योगों की रक्षा के लिए सुरक्षात्मक शुल्कों की मांग की", "type": "leaf"}]}
        ]
    },
    "montague-statement-of-august-1917": {
        "en": [
            {"label": "August Declaration", "type": "branch", "date": "1917", "children": [
                {"label": "Declaration by Edwin Montague stating British policy was 'gradual development of self-governing institutions'", "type": "leaf"},
                {"label": "Made to secure Indian support during World War I and cool down Home Rule agitation", "type": "leaf"},
                {"label": "Led to Government of India Act 1919 (introduction of Dyarchy in provinces)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अगस्त घोषणा", "type": "branch", "date": "1917", "children": [
                {"label": "एडविन मोंटेग्यू द्वारा घोषणा जिसमें ब्रिटिश नीति 'स्वशासी संस्थाओं का क्रमिक विकास' बताया गया", "type": "leaf"},
                {"label": "प्रथम विश्व युद्ध के दौरान भारतीय सहयोग प्राप्त करने और होम रूल आंदोलन को शांत करने के लिए किया गया", "type": "leaf"},
                {"label": "इसके परिणामस्वरूप भारत सरकार अधिनियम 1919 आया (प्रांतों में द्वैध शासन की शुरुआत)", "type": "leaf"}]}
        ]
    },
    "morley-minto-reforms-1909": {
        "en": [
            {"label": "Provisions", "type": "branch", "date": "1909 Act", "children": [
                {"label": "Introduced Separate Electorates for Muslims (voters of one religion voted for candidates of same religion)", "type": "leaf"},
                {"label": "Increased non-official majority in provincial councils; kept official majority in center", "type": "leaf"},
                {"label": "Satyendra P. Sinha appointed as first Indian to Viceroy's Executive Council", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रावधान", "type": "branch", "date": "1909 का अधिनियम", "children": [
                {"label": "मुसलमानों के लिए पृथक निर्वाचन प्रणाली लागू की (एक धर्म के मतदाता अपने ही धर्म के प्रत्याशी को वोट दे सकते थे)", "type": "leaf"},
                {"label": "प्रांतीय परिषदों में गैर-सरकारी बहुमत बढ़ाया; केंद्र में सरकारी बहुमत बनाए रखा", "type": "leaf"},
                {"label": "सत्येंद्र पी. सिन्हा वायसराय की कार्यकारी परिषद में नियुक्त होने वाले पहले भारतीय बने", "type": "leaf"}]}
        ]
    },
    "movement-under-extremist-leadership": {
        "en": [
            {"label": "Extremist Action", "type": "branch", "date": "1905-1908", "children": [
                {"label": "Pushed the Swadeshi & Boycott movement beyond Bengal into other regions (Tilak in Bombay, Lajpat Rai in Punjab)", "type": "leaf"},
                {"label": "Advocated passive resistance: Refused to assist the government, pay taxes, or attend courts", "type": "leaf"},
                {"label": "Established National Council of Education (1906) to reject English curriculum", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उग्रवादी नेतृत्व", "type": "branch", "date": "1905-1908", "children": [
                {"label": "स्वदेशी और बहिष्कार आंदोलन को बंगाल से बाहर अन्य क्षेत्रों में विस्तारित किया (तिलक बॉम्बे में, लाजपत राय पंजाब में)", "type": "leaf"},
                {"label": "निष्क्रिय प्रतिरोध की वकालत की: सरकार की सहायता करने, कर देने या अदालतों में जाने से इनकार किया", "type": "leaf"},
                {"label": "अंग्रेजी शिक्षा प्रणाली का बहिष्कार करने हेतु राष्ट्रीय शिक्षा परिषद (1906) की स्थापना की", "type": "leaf"}]}
        ]
    },
    "movements-of-all-india-muslim-league-1906": {
        "en": [
            {"label": "Foundation", "type": "branch", "date": "1906 Dacca", "children": [
                {"label": "Founded under leadership of Aga Khan, Nawab Salimullah of Dacca, and Mohsin-ul-Mulk", "type": "leaf"},
                {"label": "Aimed to protect Muslim political interests and foster loyalty to the British Crown", "type": "leaf"},
                {"label": "Supported the partition of Bengal; actively opposed Swadeshi boycott campaigns", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्थापना", "type": "branch", "date": "1906 ढाका", "children": [
                {"label": "आगा खान, ढाका के नवाब सलीमुल्लाह और मोहसिन-उल-मुल्क के नेतृत्व में स्थापित", "type": "leaf"},
                {"label": "मुस्लिम राजनीतिक हितों की रक्षा करना और ब्रिटिश ताज के प्रति वफादारी को बढ़ावा देना लक्ष्य था", "type": "leaf"},
                {"label": "बंगाल विभाजन का समर्थन किया; स्वदेशी बहिष्कार अभियानों का सक्रिय रूप से विरोध किया", "type": "leaf"}]}
        ]
    },
    "national-movement-in-light-of-first-world-war": {
        "en": [
            {"label": "Impact of War", "type": "branch", "date": "1914-1918", "children": [
                {"label": "Heavy economic burden: Defense expenditure rose, leading to high taxes & inflation in India", "type": "leaf"},
                {"label": "Forced recruitment of Indian soldiers caused widespread anger in Punjab and rural areas", "type": "leaf"},
                {"label": "Nationalists expected self-government (Home Rule) in exchange for war support; disappointment led to mass campaigns", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "युद्ध का प्रभाव", "type": "branch", "date": "1914-1918", "children": [
                {"label": "भारी आर्थिक बोझ: रक्षा व्यय बढ़ने से भारत में उच्च कर, महंगाई और खाद्य पदार्थों की कमी हुई", "type": "leaf"},
                {"label": "भारतीय सैनिकों की जबरन भर्ती ने पंजाब और ग्रामीण क्षेत्रों में व्यापक आक्रोश पैदा किया", "type": "leaf"},
                {"label": "राष्ट्रवादियों को युद्ध में सहयोग के बदले स्वशासन (होम रूल) की उम्मीद थी; निराशा ने जन अभियानों को जन्म दिया", "type": "leaf"}]}
        ]
    },
    "pre-inc-campaigns-and-their-objectives": {
        "en": [
            {"label": "Early Struggles", "type": "branch", "date": "Pre-1885", "children": [
                {"label": "Agitation against reduction of maximum age limit for ICS from 21 to 19 (1876)", "type": "leaf"},
                {"label": "Campaign against Lord Lytton's Vernacular Press Act (1878) and Arms Act (1878)", "type": "leaf"},
                {"label": "All-India campaign supporting the Ilbert Bill (1883) to allow Indian judges to try Europeans", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "शुरुआती संघर्ष", "type": "branch", "date": "1885 से पूर्व", "children": [
                {"label": "आईसीएस (ICS) परीक्षा के लिए अधिकतम आयु सीमा 21 से घटाकर 19 वर्ष करने के खिलाफ आंदोलन (1876)", "type": "leaf"},
                {"label": "लॉर्ड लिटन के वर्नाक्यूलर प्रेस एक्ट (1878) और आर्म्स एक्ट (1878) के खिलाफ अभियान", "type": "leaf"},
                {"label": "भारतीय न्यायाधीशों को यूरोपीय लोगों पर मुकदमा चलाने की अनुमति देने वाले इल्बर्ट बिल (1883) के समर्थन में अखिल भारतीय अभियान", "type": "leaf"}]}
        ]
    },
    "pre-inc-organisations": {
        "en": [
            {"label": "Early Bodies", "type": "branch", "date": "Bengal & Bombay", "children": [
                {"label": "Bangabhasha Prakasika Sabha (1836): First organized association in Bengal", "type": "leaf"},
                {"label": "Landholders' Society (1838): Formed to protect interests of landlord classes", "type": "leaf"},
                {"label": "East India Association (London, 1866) by Dadabhai Naoroji to lobby British MPs", "type": "leaf"},
                {"label": "Indian Association of Calcutta (1876) by Surendranath Banerjea & Anand Mohan Bose", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक संस्थाएं", "type": "branch", "date": "बंगाल और बॉम्बे", "children": [
                {"label": "बंगभाषा प्रकाशिका सभा (1836): बंगाल में पहला संगठित राजनीतिक संघ", "type": "leaf"},
                {"label": "लैंडहोल्डर्स सोसाइटी (1838): जमींदार वर्गों के हितों की रक्षा हेतु गठित", "type": "leaf"},
                {"label": "लंदन में दादाभाई नौरोजी द्वारा ईस्ट इंडिया एसोसिएशन (1866) की स्थापना ताकि ब्रिटिश सांसदों को प्रभावित किया जा सके", "type": "leaf"},
                {"label": "इंडियन एसोसिएशन ऑफ कलकत्ता (1876) सुरेंद्रनाथ बनर्जी और आनंद मोहन बोस द्वारा स्थापित", "type": "leaf"}]}
        ]
    },
    "reasons-of-muslim-league-pact-with-congress": {
        "en": [
            {"label": "Shift in League Policy", "type": "branch", "date": "Triggers", "children": [
                {"label": "Annulment of Bengal Partition in 1911 shocked conservative League leaders", "type": "leaf"},
                {"label": "British entry into WWI against Ottoman Empire (Turkish Caliph) angered Indian Muslims", "type": "leaf"},
                {"label": "Rise of young, nationalist Muslim leaders (Ali brothers, Abul Kalam Azad, Jinnah) who favored unity", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लीग की नीति में बदलाव", "type": "branch", "date": "उत्प्रेरक", "children": [
                {"label": "1911 में बंगाल विभाजन रद्द होने से रूढ़िवादी लीग नेताओं को गहरा आघात लगा", "type": "leaf"},
                {"label": "प्रथम विश्व युद्ध में तुर्की (ऑटोमन साम्राज्य/खलीफा) के खिलाफ अंग्रेजों के उतरने से भारतीय मुसलमान नाराज हुए", "type": "leaf"},
                {"label": "युवा, राष्ट्रवादी मुस्लिम नेताओं (अली बंधु, अबुल कलाम आजाद, जिन्ना) का उदय जो कांग्रेस के साथ एकता चाहते थे", "type": "leaf"}]}
        ]
    },
    "reasons-of-readmission-of-extemists": {
        "en": [
            {"label": "Unification Context", "type": "branch", "date": "1915-16", "children": [
                {"label": "Death of prominent moderate leaders Ferozeshah Mehta and G.K. Gokhale in 1915 removed major resistance to unification", "type": "leaf"},
                {"label": "Tilak and Annie Besant recognized that the split weakened the national movement's bargaining power", "type": "leaf"},
                {"label": "Tilak declared loyalty to the British Crown to ease moderate apprehensions", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "एकता का संदर्भ", "type": "branch", "date": "1915-16", "children": [
                {"label": "1915 में प्रमुख उदारवादी नेताओं फिरोजशाह मेहता और जी.के. गोखले की मृत्यु से एकीकरण का मुख्य अवरोध हटा", "type": "leaf"},
                {"label": "तिलक और एनी बेसेंट ने महसूस किया कि विभाजन ने राष्ट्रीय आंदोलन की मोलतोल करने की शक्ति को कमजोर कर दिया है", "type": "leaf"},
                {"label": "उदारवादियों की आशंकाओं को दूर करने के लिए तिलक ने ब्रिटिश शासन के प्रति वफादारी की घोषणा की", "type": "leaf"}]}
        ]
    },
    "revolutionary-activities": {
        "en": [
            {"label": "Assassinations & Bombings", "type": "branch", "date": "Revolutionaries", "children": [
                {"label": "Chapekar Brothers (1897): Assassinated Plague Commissioner Rand in Poona", "type": "leaf"},
                {"label": "Muzaffarpur Bombing (1908): Prafulla Chaki and Khudiram Bose targeted Magistrate Kingsford", "type": "leaf"},
                {"label": "Alipore Conspiracy Case (1908): Trial of Aurobindo & Barindra Ghosh; bomb factory in Maniktala found", "type": "leaf"},
                {"label": "Delhi-Lahore Conspiracy Case (1912): Rash Behari Bose threw bomb at Viceroy Lord Hardinge", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "हत्याएं और बमबारी", "type": "branch", "date": "क्रांतिकारी", "children": [
                {"label": "चापेकर बंधु (1897): पूना में प्लेग कमिश्नर रैंड की हत्या की", "type": "leaf"},
                {"label": "मुजफ्फरपुर बम कांड (1908): प्रफुल्ल चाकी और खुदीराम बोस ने मजिस्ट्रेट किंग्सफोर्ड पर बम फेंका", "type": "leaf"},
                {"label": "अलीपुर षड्यंत्र मामला (1908): अरविंद और बारिंद्र घोष का मुकदमा; मानिकतला में बम फैक्ट्री का पता चला", "type": "leaf"},
                {"label": "दिल्ली-लाहौर षड्यंत्र मामला (1912): रास बिहारी बोस ने वायसराय लॉर्ड हार्डिंग पर बम फेंका", "type": "leaf"}]}
        ]
    },
    "revolutionary-activities-abroad": {
        "en": [
            {"label": "Key Centres", "type": "branch", "date": "Global Sites", "children": [
                {"label": "London: Shyamji Krishna Varma established India House (1905); Madan Lal Dhingra assassinated Curzon Wyllie (1909)", "type": "leaf"},
                {"label": "Paris/Geneva: Madame Bhikaji Cama (unfurled first national flag in Stuttgart, 1907)", "type": "leaf"},
                {"label": "San Francisco: Ghadar Party (1913) formed by Lala Hardayal, Sohan Singh Bhakna; planned armed revolt in Punjab", "type": "leaf"},
                {"label": "Berlin: Berlin Committee for Indian Independence (1915) under Virendranath Chattopadhyaya", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख केंद्र", "type": "branch", "date": "वैश्विक स्थल", "children": [
                {"label": "लंदन: श्यामजी कृष्ण वर्मा ने इंडिया हाउस (1905) की स्थापना की; मदन लाल ढींगरा ने कर्जन वायली की हत्या की (1909)", "type": "leaf"},
                {"label": "पेरिस/जिनेवा: मैडम भीकाजी कामा (1907 में स्टटगार्ट में पहला राष्ट्रीय ध्वज फहराया)", "type": "leaf"},
                {"label": "सैन फ्रांसिस्को: लाला हरदयाल और सोहन सिंह भकना द्वारा गदर पार्टी (1913) का गठन; पंजाब में सशस्त्र विद्रोह की योजना", "type": "leaf"},
                {"label": "बर्लिन: वीरेंद्रनाथ चट्टोपाध्याय के नेतृत्व में 'बर्लिन कमेटी फॉर इंडियन इंडिपेंडेंस' (1915)", "type": "leaf"}]}
        ]
    },
    "success-and-limitations-with-moderate-approach": {
        "en": [
            {"label": "Successes", "type": "branch", "date": "Achievements", "children": [
                {"label": "Exposed the economic exploitation and drain of wealth by British rule (paved way for Swadeshi)", "type": "leaf"},
                {"label": "Secured the Indian Councils Act 1892; created a strong foundation for future national demands", "type": "leaf"}]},
            {"label": "Limitations", "type": "branch", "date": "Failures", "children": [
                {"label": "Confined to elites; failed to involve mass rural population and peasants", "type": "leaf"},
                {"label": "Believed in British sense of justice, which proved ineffective in securing real self-government", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सफलताएं", "type": "branch", "date": "उपलब्धियां", "children": [
                {"label": "ब्रिटिश शासन द्वारा किए जा रहे आर्थिक शोषण और धन निष्कासन को उजागर किया (स्वदेशी का मार्ग प्रशस्त किया)", "type": "leaf"},
                {"label": "भारतीय परिषद अधिनियम 1892 प्राप्त किया; भावी राष्ट्रीय मांगों के लिए एक मजबूत आधार तैयार किया", "type": "leaf"}]},
            {"label": "सीमाएं", "type": "branch", "date": "कमियां", "children": [
                {"label": "अभिजात वर्ग तक सीमित; ग्रामीण जनता और किसानों को आंदोलन में शामिल करने में विफल रहे", "type": "leaf"},
                {"label": "ब्रिटिश न्यायप्रियता में अटूट विश्वास रखा, जो वास्तविक स्वशासन प्राप्त करने में अप्रभावी साबित हुआ", "type": "leaf"}]}
        ]
    },
    "swadeshi-movement-and-associated-leaders": {
        "en": [
            {"label": "The Struggle", "type": "branch", "date": "1905-1908", "children": [
                {"label": "Protest against Partition of Bengal; formal proclamation made at Calcutta Town Hall (Aug 7, 1905)", "type": "leaf"},
                {"label": "Boycott of foreign cloth, sugar, salt; burning of foreign goods in public bonfires", "type": "leaf"},
                {"label": "Promotion of Swadeshi industries: PC Ray's Bengal Chemicals; VO Chidambaram's Swadeshi Steam Navigation", "type": "leaf"}]},
            {"label": "Key Leaders", "type": "branch", "date": "Leaders", "children": [
                {"label": "Bengal: Surendranath Banerjea, Aurobindo Ghosh, Bipin Chandra Pal, Rabindranath Tagore", "type": "leaf"},
                {"label": "Maharashtra: Bal Gangadhar Tilak; Punjab: Lala Lajpat Rai, Ajit Singh", "type": "leaf"},
                {"label": "Delhi: Syed Haider Raza; Madras: Chidambaram Pillai", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्वदेशी संघर्ष", "type": "branch", "date": "1905-1908", "children": [
                {"label": "बंगाल विभाजन का विरोध; कलकत्ता टाउन हॉल (7 अगस्त 1905) में स्वदेशी आंदोलन की औपचारिक घोषणा", "type": "leaf"},
                {"label": "विदेशी कपड़ों, चीनी, नमक का बहिष्कार; सार्वजनिक स्थानों पर विदेशी वस्तुओं की होली जलाई गई", "type": "leaf"},
                {"label": "स्वदेशी उद्योगों को बढ़ावा: पी.सी. राय द्वारा बंगाल केमिकल्स; वी.ओ. चिदंबरम द्वारा स्वदेशी स्टीम नेविगेशन की स्थापना", "type": "leaf"}]},
            {"label": "प्रमुख नेता", "type": "branch", "date": "नेता", "children": [
                {"label": "बंगाल: सुरेंद्रनाथ बनर्जी, अरविंद घोष, बिपिन चंद्र पाल, रवींद्रनाथ टैगोर", "type": "leaf"},
                {"label": "महाराष्ट्र: बाल गंगाधर तिलक; पंजाब: लाला लाजपत राय, अजीत सिंह", "type": "leaf"},
                {"label": "दिल्ली: सैयद हैदर रजा; मद्रास: चिदंबरम पिल्लै", "type": "leaf"}]}
        ]
    },
    "the-moderate-congress-1885-1905": {
        "en": [
            {"label": "Key Features", "type": "branch", "date": "Moderates", "children": [
                {"label": "Led by western-educated elites; Ferozeshah Mehta, Dinshaw Wacha, W.C. Bonnerjee", "type": "leaf"},
                {"label": "Agitated using methods of petitioning, prayer, and writing papers/articles within laws", "type": "leaf"},
                {"label": "Sought representative assemblies, higher jobs for Indians, and stopping drain of wealth", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मुख्य विशेषताएँ", "type": "branch", "date": "उदारवादी", "children": [
                {"label": "पश्चिमी शिक्षा प्राप्त अभिजात वर्ग का नेतृत्व; फिरोजशाह मेहता, दिनशा वाचा, डब्ल्यू.सी. बनर्जी", "type": "leaf"},
                {"label": "कानूनी सीमाओं के भीतर प्रार्थना, याचिका और लेख/भाषणों के माध्यम से आंदोलन किया", "type": "leaf"},
                {"label": "प्रतिनिधि सभाओं, भारतीयों के लिए उच्च नौकरियों और धन निष्कासन को रोकने की मांग की", "type": "leaf"}]}
        ]
    },
    "generic-topic": {
        "en": [
            {"label": "Historical Context", "type": "branch", "date": "1905-1917", "children": [
                {"label": "First Phase of National Movement marked by rise of militant nationalism", "type": "leaf"},
                {"label": "Swadeshi & Boycott movements shifted national target from minor reforms to complete Swaraj", "type": "leaf"},
                {"label": "Morley-Minto Reforms (1909) and Ghadar movement abroad defined global and local struggles", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "ऐतिहासिक संदर्भ", "type": "branch", "date": "1905-1917", "children": [
                {"label": "राष्ट्रीय आंदोलन का प्रथम चरण उग्र राष्ट्रवाद के उदय से परिभाषित था", "type": "leaf"},
                {"label": "स्वदेशी और बहिष्कार आंदोलनों ने राष्ट्रीय लक्ष्य को सुधारों से बदलकर पूर्ण स्वराज कर दिया", "type": "leaf"},
                {"label": "मार्ले-मिंटो सुधार (1909) और विदेशों में गदर आंदोलन ने संघर्ष को नया रूप दिया", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "annulment-of-partition-of-bengal": "annulment-of-partition-of-bengal",
    "campaign-for-general-administrative-reforms": "campaign-for-general-administrative-reforms",
    "chittagong-revolt-group": "chittagong-revolt-group",
    "comparative-account-of-moderates-and-extremists": "comparative-account-of-moderates-and-extremists",
    "constitutional-reforms-and-propaganda-in-legislature": "constitutional-reforms-and-propaganda-in-legislature",
    "debate-over-inc-being-a-safety-valve": "debate-over-inc-being-a-safety-valve",
    "developments-that-led-to-home-rule-league": "developments-that-led-to-home-rule-league",
    "differences-between-the-moderates-and-the-extremists": "differences-between-the-moderates-and-the-extemists",
    "early-phase-indian-national-congress": "early-phase-indian-national-congress",
    "economic-critique-of-imperialism": "economic-critique-of-imperialism",
    "government-repression": "government-repression",
    "governments-response-towards-inc": "governments-response-towards-inc",
    "hindustan-republican-association": "hindustan-republican-association",
    "home-rule-league-movement-1916": "home-rule-league-movement-1916",
    "important-inc-sessions-extremist-phase": "important-inc-sessions-extremist-phase",
    "key-sessions-of-the-indian-national-congress-inc": "key-sessions-of-the-indian-national-congress-inc",
    "limitations-with-home-rule-leagues": "limitations-with-home-rule-leagues",
    "lucknow-session-of-inc-1916-lucknow-pact": "lucknow-session-of-inc-1916-lucknow-pact",
    "mass-participation-extremist-phase": "mass-participation-extremist-phase",
    "militant-nationalism-1905-to-1918": "militant-nationalism-1905-to-1918",
    "moderate-campaign-for-administrative-reforms": "moderate-campaign-for-administrative-reforms",
    "moderate-campaign-for-constitutional-reforms": "moderate-campaign-for-constitutional-reforms",
    "moderate-opinion-against-economic-exploitation": "moderate-opinion-against-economic-exploitation",
    "montague-statement-of-august-1917": "montague-statement-of-august-1917",
    "morley-minto-reforms-1909": "morley-minto-reforms-1909",
    "movement-under-extremist-leadership": "movement-under-extremist-leadership",
    "movements-of-all-india-muslim-league-1906": "movements-of-all-india-muslim-league-1906",
    "national-movement-in-light-of-first-world-war": "national-movement-in-light-of-first-world-war",
    "pre-inc-campaigns-and-their-objectives": "pre-inc-campaigns-and-their-objectives",
    "pre-inc-organisations": "pre-inc-organisations",
    "reasons-of-muslim-league-pact-with-congress": "reasons-of-muslim-league-pact-with-congress",
    "reasons-of-readmission-of-extremists": "reasons-of-readmission-of-extemists",
    "revolutionary-activities": "revolutionary-activities",
    "revolutionary-activities-abroad": "revolutionary-activities-abroad",
    "success-and-limitations-with-moderate-approach": "success-and-limitations-with-moderate-approach",
    "swadeshi-movement-and-associated-leaders": "swadeshi-movement-and-associated-leaders",
    "the-moderate-congress-1885-1905": "the-moderate-congress-1885-1905"
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
