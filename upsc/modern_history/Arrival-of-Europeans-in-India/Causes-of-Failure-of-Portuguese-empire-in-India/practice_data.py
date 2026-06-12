# -*- coding: utf-8 -*-

EN_AR_OPTS = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]

HI_AR_OPTS = [
    "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
    "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
    "A सही है लेकिन R गलत है",
    "A गलत है लेकिन R सही है"
]

practice_raw = [
    # 25 Statement-Based (0 to 24)
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the financial models of European trading companies:\n1. The English East India Company was a joint-stock corporation that pooled capital from public shareholders.\n2. The Portuguese Estado da Índia was a crown-controlled monopoly financed and directed directly by the King.\nWhich of the statements given above is/are correct?",
        "q_hi": "यूरोपीय व्यापारिक कंपनियों के वित्तीय मॉडलों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. अंग्रेजी ईस्ट इंडिया कंपनी एक संयुक्त-पूंजी निगम थी जिसने सार्वजनिक शेयरधारकों से पूंजी जुटाई थी।\n2. पुर्तगाली एस्टाडो दा इंडिया एक शाही-नियंत्रित एकाधिकार था जिसे सीधे राजा द्वारा वित्तपोषित और निर्देशित किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. The joint-stock model gave the English EIC financial flexibility and separated it from state politics, while the Portuguese Estado was rigid and dependent on crown finances.",
        "sol_hi": "दोनों कथन सही हैं। संयुक्त-पूंजी मॉडल ने अंग्रेजी ईआईसी को वित्तीय लचीलापन दिया और इसे राज्य की राजनीति से अलग रखा, जबकि पुर्तगाली एस्टाडो शाही वित्त पर निर्भर और कठोर था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding Dutch ship design in the 17th century:\n1. The Fluyt was a Dutch cargo ship designed to carry large cargo volumes with a relatively small crew.\n2. Portuguese carracks were built with a lower center of gravity than the Dutch Fluyt, making them faster in combat.\nWhich of the statements given above is/are correct?",
        "q_hi": "17वीं शताब्दी में डच जहाज डिजाइन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. फ्लूट (Fluyt) एक डच मालवाहक जहाज था जिसे अपेक्षाकृत कम चालक दल के साथ बड़ी मात्रा में माल ले जाने के लिए डिज़ाइन किया गया था।\n2. पुर्तगाली कैरैक डच फ्लूट की तुलना में गुरुत्वाकर्षण के निचले केंद्र के साथ बनाए गए थे, जिससे वे युद्ध में तेज चलते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because Portuguese carracks were top-heavy, slow, and designed for maximum cargo rather than combat maneuverability, unlike the Dutch Fluyt which was highly cost-efficient.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि पुर्तगाली कैरैक शीर्ष-भारी, धीमे और युद्ध की गतिशीलता के बजाय अधिकतम माल ढोने के लिए डिज़ाइन किए गए थे, डच फ्लूट के विपरीत जो अत्यधिक लागत-कुशल था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the establishment of the Goa Inquisition:\n1. The Inquisition was established in 1560 on the petition of Jesuit missionary Francis Xavier.\n2. It targeted only native Hindus and Muslims who refused to convert to Christianity.\nWhich of the statements given above is/are correct?",
        "q_hi": "गोवा धर्माधिकरण (Inquisition) की स्थापना के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. धर्माधिकरण की स्थापना 1560 में जेसुइट मिशनरी फ्रांसिस जेवियर की याचिका पर की गई थी।\n2. इसने केवल उन मूल हिंदुओं और मुसलमानों को निशाना बनाया जिन्होंने ईसाई धर्म में परिवर्तित होने से इनकार कर दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the Inquisition's official jurisdiction was to check heresy among converts (New Christians/Crypto-Hindus), not unbaptized non-Christians.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि धर्माधिकरण का आधिकारिक अधिकार क्षेत्र धर्म परिवर्तित लोगों (नए ईसाई/क्रिप्टो-हिंदू) के बीच पाखंड की जांच करना था, न कि बपतिस्मा-रहित गैर-ईसाइयों की।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the religious policies of Afonso de Albuquerque:\n1. Albuquerque banned the practice of Sati immediately upon the conquest of Goa in 1510.\n2. Albuquerque ordered the destruction of all Hindu temples in Goa to enforce Catholic orthodoxy.\nWhich of the statements given above is/are correct?",
        "q_hi": "अफोंसो डी अल्बुकर्क की धार्मिक नीतियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. अल्बुकर्क ने 1510 में गोवा की विजय के तुरंत बाद सती प्रथा पर प्रतिबंध लगा दिया था।\n2. अल्बुकर्क ने कैथोलिक रूढ़िवादिता को लागू करने के लिए गोवा में सभी हिंदू मंदिरों को नष्ट करने का आदेश दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because Albuquerque followed a pragmatic policy of local alliances and did not launch temple destruction campaigns, which only began in the mid-16th century.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि अल्बुकर्क ने स्थानीय गठबंधनों की व्यावहारिक नीति का पालन किया और मंदिर विनाश अभियान शुरू नहीं किया, जो केवल 16वीं शताब्दी के मध्य में शुरू हुआ था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the succession crisis in Portugal in 1578:\n1. The crisis was triggered by the death of King Sebastian at the Battle of Alcácer Quibir in Morocco.\n2. King Philip II of Spain claimed the Portuguese throne through dynastic lineage and military force.\nWhich of the statements given above is/are correct?",
        "q_hi": "1578 में पुर्तगाल में उत्तराधिकार संकट के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. संकट मोरक्को में अलकासर क्विबीर के युद्ध में राजा सेबेस्टियन की मृत्यु के कारण शुरू हुआ था।\n2. स्पेन के राजा फिलिप द्वितीय ने वंशानुगत संबंधों और सैन्य बल के माध्यम से पुर्तगाली सिंहासन पर दावा किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. Sebastian's death without an heir left a vacuum, which Philip II filled by invading and annexing Portugal in 1580.",
        "sol_hi": "दोनों कथन सही हैं। सेबेस्टियन की बिना वारिस के मृत्यु ने एक शून्य छोड़ दिया, जिसे फिलिप द्वितीय ने 1580 में पुर्तगाल पर आक्रमण और विलय करके भर दिया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Treaty of Thomar (1581):\n1. It resolved the succession crisis by establishing a personal union of the Spanish and Portuguese crowns.\n2. It guaranteed that the Portuguese administration, laws, and colonies would remain distinct from Spain's.\nWhich of the statements given above is/are correct?",
        "q_hi": "तोमर की संधि (1581) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसने स्पेनिश और पुर्तगाली मुकुटों के व्यक्तिगत संघ की स्थापना करके उत्तराधिकार संकट को हल किया।\n2. इसने गारंटी दी कि पुर्तगाली प्रशासन, कानून और बस्तियां स्पेन से अलग रहेंगी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. The treaty established the Iberian Union under Philip II but legally preserved Portugal's administrative separateness, though Spain directed foreign policy.",
        "sol_hi": "दोनों कथन सही हैं। संधि ने फिलिप द्वितीय के तहत इबेरियन यूनियन की स्थापना की लेकिन पुर्तगाल के प्रशासनिक अलगाव को कानूनी रूप से संरक्षित रखा, हालांकि विदेश नीति स्पेन द्वारा निर्देशित थी।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the economic development of Brazil in the 17th century:\n1. The cultivation of sugarcane (Engenhos system) and the Atlantic slave trade made Brazil highly profitable for Portugal.\n2. The discovery of gold in Minas Gerais in the late 1690s further cemented Brazil's economic importance.\nWhich of the statements given above is/are correct?",
        "q_hi": "17वीं शताब्दी में ब्राजील के आर्थिक विकास के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गन्ने की खेती (Engenhos प्रणाली) और अटलांटिक दास व्यापार ने ब्राजील को पुर्तगाल के लिए अत्यधिक लाभदायक बना दिया।\n2. 1690 के दशक के अंत में मिनस गेरैस में सोने की खोज ने ब्राजील के आर्थिक महत्व को और मजबूत कर दिया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. These agricultural and mineral booms made Brazil the economic centerpiece of the empire, prompting the diversion of resources away from India.",
        "sol_hi": "दोनों कथन सही हैं। इन कृषि और खनिज उछालों ने ब्राजील को साम्राज्य का आर्थिक केंद्र बना दिया, जिससे भारत से संसाधनों का विचलन हुआ।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding Portugal's demographic constraints:\n1. In the 16th century, Portugal had a small domestic population of bare one million people.\n2. Portugal's small population made it difficult to sustain military garrisons in both Brazil and the East Indies.\nWhich of the statements given above is/are correct?",
        "q_hi": "पुर्तगाल की जनसांख्यिकीय सीमाओं के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. 16वीं शताब्दी में, पुर्तगाल की घरेलू आबादी बमुश्किल दस लाख लोगों की थी।\n2. पुर्तगाल की कम आबादी के कारण ब्राजील और ईस्ट इंडीज दोनों में सैन्य चौकियां बनाए रखना कठिन था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. The demographic limits meant that Portugal had to choose between defending its Asian or American holdings, ultimately choosing Brazil due to fewer challenges.",
        "sol_hi": "दोनों कथन सही हैं। जनसांख्यिकीय सीमाओं का मतलब था कि पुर्तगाल को अपने एशियाई या अमेरिकी क्षेत्रों की रक्षा के बीच चयन करना था, और अंततः कम चुनौतियों के कारण ब्राजील को चुना गया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the tenure of Portuguese Viceroys in Goa:\n1. The standard term of office was limited to three years to prevent viceroys from building independent local power.\n2. The short tenure encouraged viceroys to prioritize rapid personal enrichment rather than long-term defense.\nWhich of the statements given above is/are correct?",
        "q_hi": "गोवा में पुर्तगाली वायसरायों के कार्यकाल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वायसरायों को स्वतंत्र स्थानीय शक्ति बनाने से रोकने के लिए मानक कार्यकाल तीन साल तक सीमित था।\n2. छोटे कार्यकाल ने वायसरायों को दीर्घकालिक रक्षा के बजाय त्वरित व्यक्तिगत संवर्धन को प्राथमिकता देने के लिए प्रोत्साहित किया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. While the three-year limit checked rebellion, it had the unintended consequence of creating a cycle of administrative corruption and neglect of defense.",
        "sol_hi": "दोनों कथन सही हैं। जबकि तीन साल की सीमा ने विद्रोह को रोका, इसका अनपेक्षित परिणाम प्रशासनिक भ्रष्टाचार के चक्र और रक्षा की उपेक्षा के रूप में सामने आया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding 'trato particular' in the Portuguese empire:\n1. It refers to the private trade conducted by crown officials for personal profit, which bypassed royal customs.\n2. The Crown immediately legalized 'trato particular' from the beginning of the 15th century to boost local commerce.\nWhich of the statements given above is/are correct?",
        "q_hi": "पुर्तगाली साम्राज्य में 'त्रातो पर्टिकुलर' के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसका तात्पर्य शाही अधिकारियों द्वारा व्यक्तिगत लाभ के लिए किए जाने वाले निजी व्यापार से है, जिसने शाही सीमा शुल्क को दरकिनार किया।\n2. स्थानीय वाणिज्य को बढ़ावा देने के लिए क्राउन ने 15वीं शताब्दी की शुरुआत से ही 'त्रातो पर्टिकुलर' को तुरंत वैध कर दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the Crown initially banned private trade to maintain its monopolies, only tolerating it later due to empty coffers.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि क्राउन ने शुरुआत में अपने एकाधिकार को बनाए रखने के लिए निजी व्यापार पर प्रतिबंध लगा दिया था, बाद में खाली खजाने के कारण इसे सहन किया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the practice of selling offices (venda de cargos):\n1. It allowed wealthy private buyers to purchase military captaincies of key fortresses.\n2. It ensured that only the most competent and experienced naval commanders led the defense of Goa.\nWhich of the statements given above is/are correct?",
        "q_hi": "पदों को बेचने की प्रथा (वेंडा दे कार्गोस) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसने अमीर निजी खरीदारों को प्रमुख किलों की सैन्य कप्तानी खरीदने की अनुमति दी।\n2. इसने यह सुनिश्चित किया कि केवल सबसे सक्षम और अनुभवी नौसैनिक कमांडर ही गोवा की रक्षा का नेतृत्व करें।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the sale of offices sidelined competent, experienced military officers, placing defense in the hands of untrained buyers.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि पदों की बिक्री ने सक्षम, अनुभवी सैन्य अधिकारियों को दरकिनार कर दिया, जिससे रक्षा अप्रशिक्षित खरीदारों के हाथों में चली गई।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Mughal expulsion of the Portuguese from Hugli in 1632:\n1. The expulsion was ordered by Mughal Emperor Shah Jahan due to Portuguese piracy and slave trading.\n2. The Portuguese at Hugli were supported by the British Navy during the three-month siege.\nWhich of the statements given above is/are correct?",
        "q_hi": "1632 में मुगलों द्वारा हुगली से पुर्तगालियों के निष्कासन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. पुर्तगाली डकैती और दास व्यापार के कारण मुगल सम्राट शाहजहां ने निष्कासन का आदेश दिया था।\n2. तीन महीने की घेराबंदी के दौरान हुगली में पुर्तगालियों को ब्रिटिश नौसेना द्वारा सहायता प्रदान की गई थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the British did not provide any military support to the Portuguese; in fact, the British were trade rivals of the Portuguese in Bengal.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि अंग्रेजों ने पुर्तगालियों को कोई सैन्य सहायता प्रदान नहीं की थी; वास्तव में, अंग्रेज बंगाल में पुर्तगालियों के व्यापारिक प्रतिद्वंद्वी थे।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Maratha siege of Bassein (1737-1739):\n1. The Maratha forces under Chimaji Appa used gunpowder mines to breach Bassein's stone walls.\n2. The Portuguese garrison was completely evacuated by sea using French naval vessels.\nWhich of the statements given above is/are correct?",
        "q_hi": "मराठों द्वारा वसई की घेराबंदी (1737-1739) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. चिमाजी अप्पा के नेतृत्व में मराठा सेना ने वसई की पत्थरों की दीवारों को तोड़ने के लिए बारूद की सुरंगों का उपयोग किया था।\n2. पुर्तगाली गैरीसन को फ्रांसीसी नौसैनिक जहाजों का उपयोग करके समुद्र के रास्ते पूरी तरह से सुरक्षित निकाल लिया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct; the Marathas successfully mined the bastions. Statement 2 is incorrect because the French did not evacuate the garrison; the Portuguese surrendered and were allowed by the Marathas to withdraw to Goa.",
        "sol_hi": "कथन 1 सही है; मराठों ने सफलतापूर्वक बुर्जों में सुरंगें बनाईं। कथन 2 गलत है क्योंकि फ्रांसीसियों ने गैरीसन को बाहर नहीं निकाला; पुर्तगालियों ने आत्मसमर्पण किया और मराठों ने उन्हें गोवा जाने की अनुमति दी।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the role of the Keladi Nayakas in coastal Karnataka:\n1. The Keladi Nayakas captured the Portuguese fortresses of Mangalore and Honavar in the early 18th century.\n2. The Keladi rulers refused to provide sanctuary to Saraswat Brahmin refugees fleeing the Goa Inquisition.\nWhich of the statements given above is/are correct?",
        "q_hi": "तटीय कर्नाटक में केलादि नायकों की भूमिका के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. केलादि नायकों ने 18वीं शताब्दी की शुरुआत में मैंगलोर और होनावर के पुर्तगाली किलों पर कब्जा कर लिया था।\n2. केलादि शासकों ने गोवा धर्माधिकरण से भागने वाले सारस्वत ब्राह्मण शरणार्थियों को शरण देने से इनकार कर दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the Keladi Nayakas actively welcomed Saraswat merchants, offering them lands and trading rights to boost local commerce.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि केलादि नायकों ने सारस्वत व्यापारियों का सक्रिय रूप से स्वागत किया, उन्हें स्थानीय व्यापार को बढ़ावा देने के लिए भूमि और व्यापार अधिकार प्रदान किए।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Battle of Swally (1612):\n1. It was a naval encounter fought near Surat between the English EIC and the Portuguese Navy.\n2. The battle ended with a decisive victory for the Portuguese fleet, securing their monopoly at Surat.\nWhich of the statements given above is/are correct?",
        "q_hi": "स्वाली के युद्ध (1612) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह अंग्रेजी ईआईसी और पुर्तगाली नौसेना के बीच सूरत के पास लड़ा गया एक नौसैनिक मुकाबला था।\n2. युद्ध पुर्तगाली बेड़े की निर्णायक जीत के साथ समाप्त हुआ, जिससे सूरत में उनका एकाधिकार सुरक्षित हो गया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because Captain Thomas Best defeated the Portuguese, which shattered their reputation for naval superiority and allowed the English to set up trade factories.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि कैप्टन थॉमस बेस्ट ने पुर्तगालियों को हराया था, जिसने उनकी नौसैनिक अजेयता की प्रतिष्ठा को तोड़ दिया और अंग्रेजों को व्यापार कारखाने स्थापित करने की अनुमति दी।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Portuguese Cartaz system:\n1. It was a licensing pass forced on merchant vessels sailing in the Indian Ocean to extract duties.\n2. The Dutch and English fleets successfully bypassed this system by employing armed naval escorts for their merchants.\nWhich of the statements given above is/are correct?",
        "q_hi": "पुर्तगाली कार्तज (Cartaz) प्रणाली के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह सीमा शुल्क वसूलने के लिए हिंद महासागर में चलने वाले व्यापारिक जहाजों पर जबरन लागू किया जाने वाला एक लाइसेंस पास था।\n2. डच और अंग्रेजी बेड़ों ने अपने व्यापारियों के लिए सशस्त्र नौसैनिक सुरक्षा प्रदान करके इस प्रणाली को सफलतापूर्वक दरकिनार कर दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. The Cartaz was a key source of revenue that was destroyed once the Dutch and English navies began escorting merchant convoys in the 17th century.",
        "sol_hi": "दोनों कथन सही हैं। कार्तज राजस्व का एक प्रमुख स्रोत था जो तब नष्ट हो गया जब डच और अंग्रेजी नौसेनाओं ने 17वीं शताब्दी में व्यापारिक काफिलों को सुरक्षा देना शुरू किया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Treaty of Pune (1739):\n1. The treaty ended the war between the Portuguese and the Maratha Empire over the Northern Province.\n2. Under the treaty, the Portuguese were allowed to retain Bassein but surrendered Daman and Diu.\nWhich of the statements given above is/are correct?",
        "q_hi": "पुणे की संधि (1739) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इस संधि ने उत्तरी प्रांत को लेकर पुर्तगालियों और मराठा साम्राज्य के बीच युद्ध को समाप्त किया था।\n2. संधि के तहत, पुर्तगालियों को वसई बनाए रखने की अनुमति दी गई थी लेकिन उन्होंने दमन और दीव सौंप दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the Portuguese had to surrender Bassein and the entire Northern Province, but they were allowed to retain Daman, Diu, and Goa.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि पुर्तगालियों को वसई और पूरे उत्तरी प्रांत को सौंपना पड़ा था, लेकिन उन्हें दमन, दीव और गोवा रखने की अनुमति दी गई थी।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Jesuit missionary Francis Xavier:\n1. Francis Xavier died in 1552, before the formal establishment of the Goa Inquisition.\n2. He petitioned King John III of Portugal to establish the Inquisition in Goa to check religious heresy.\nWhich of the statements given above is/are correct?",
        "q_hi": "जेसुइट मिशनरी फ्रांसिस जेवियर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गोवा धर्माधिकरण की औपचारिक स्थापना से पहले 1552 में फ्रांसिस जेवियर की मृत्यु हो गई थी।\n2. उन्होंने पुर्तगाल के राजा जॉन तृतीय को गोवा में धार्मिक पाखंड की जांच के लिए धर्माधिकरण स्थापित करने की याचिका भेजी थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. Francis Xavier petitioned the king in 1546 due to concerns over conversions, but he died years before the tribunal was finally set up in 1560.",
        "sol_hi": "दोनों कथन सही हैं। फ्रांसिस जेवियर ने धर्म परिवर्तन को लेकर चिंताओं के कारण 1546 में राजा को याचिका भेजी थी, लेकिन 1560 में ट्रिब्यूनल की स्थापना से वर्षों पहले ही उनकी मृत्यु हो गई थी।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the administration of the Dutch East India Company (VOC):\n1. The VOC was governed by a central board of directors known as the Heeren XVII (Lords Seventeen).\n2. The VOC was heavily dependent on the direct military approvals of the Dutch Stadtholder for every commercial voyage.\nWhich of the statements given above is/are correct?",
        "q_hi": "डच ईस्ट इंडिया कंपनी (VOC) के प्रशासन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वीओसी का शासन एक केंद्रीय निदेशक मंडल द्वारा चलाया जाता था जिसे हेरेन XVII (Lords Seventeen) के रूप में जाना जाता था।\n2. वीओसी प्रत्येक व्यावसायिक यात्रा के लिए डच स्टैडहोल्डर की प्रत्यक्ष सैन्य मंजूरी पर अत्यधिक निर्भर थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the VOC was a private corporate body with significant autonomous powers, including declaring war and signing treaties without waiting for state approvals.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि वीओसी एक निजी कॉर्पोरेट निकाय था जिसके पास महत्वपूर्ण स्वायत्त अधिकार थे, जिसमें राज्य की मंजूरी का इंतजार किए बिना युद्ध घोषित करना और संधियां करना शामिल था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Omani Arab capture of Mombasa (1698):\n1. The Omani Arabs captured Fort Jesus in Mombasa after a grueling three-year siege.\n2. This defeat stripped the Portuguese of their primary supply hub in East Africa, weakening their network.\nWhich of the statements given above is/are correct?",
        "q_hi": "ओमानी अरबों द्वारा मोम्बासा पर कब्जे (1698) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ओमानी अरबों ने तीन साल की भीषण घेराबंदी के बाद मोम्बासा में फोर्ट जीसस पर कब्जा कर लिया था।\n2. इस हार ने पुर्तगालियों से पूर्वी अफ्रीका में उनके प्राथमिक आपूर्ति केंद्र को छीन लिया, जिससे उनका नेटवर्क कमजोर हो गया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 2,
        "sol_en": "Both statements are correct. The fall of Mombasa in 1698 signaled the retreat of Portuguese power from the East African coast, leaving them isolated in Mozambique and Goa.",
        "sol_hi": "दोनों कथन सही हैं। 1698 में मोम्बासा के पतन ने पूर्वी अफ्रीकी तट से पुर्तगाली सत्ता के पीछे हटने का संकेत दिया, जिससे वे मोज़ाम्बिक और गोवा में अलग-थलग पड़ गए।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the reforms of the Marquis de Pombal in 1774:\n1. The Marquis de Pombal suspended the operations of the Goa Inquisition as part of his secular reforms.\n2. The Inquisition was permanently abolished in Goa in the same year, 1774.\nWhich of the statements given above is/are correct?",
        "q_hi": "1774 में मार्क्विस डी पोम्बल के सुधारों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मार्क्विस डी पोम्बल ने अपने धर्मनिरपेक्ष सुधारों के हिस्से के रूप में गोवा धर्माधिकरण के संचालन को निलंबित कर दिया था।\n2. उसी वर्ष, 1774 में गोवा में धर्माधिकरण को स्थायी रूप से समाप्त कर दिया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because while Pombal suspended the Inquisition in 1774, it was reinstated in 1778 under Queen Maria I, and only permanently abolished in 1812.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि जबकि पोम्बल ने 1774 में धर्माधिकरण को निलंबित कर दिया था, इसे 1778 में रानी मारिया प्रथम के तहत बहाल कर दिया गया था, और केवल 1812 में स्थायी रूप से समाप्त किया गया था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding Portuguese shipbuilding capabilities in Goa:\n1. The shipyards of Goa (Ribeira das Naus) constructed high-quality warships using local teakwood.\n2. The Iberian Union banned all shipbuilding activities in Goa to protect Spanish shipyards in Cadiz.\nWhich of the statements given above is/are correct?",
        "q_hi": "गोवा में पुर्तगाली जहाज निर्माण क्षमताओं के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गोवा के जहाज निर्माण केंद्रों (रिबेरा दास नाउज़) ने स्थानीय सागौन की लकड़ी का उपयोग करके उच्च गुणवत्ता वाले युद्धपोतों का निर्माण किया।\n2. इबेरियन यूनियन ने काडिज़ में स्पैनिश शिपयार्ड की रक्षा के लिए गोवा में सभी जहाज निर्माण गतिविधियों पर प्रतिबंध लगा दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the Iberian Union actually utilized the Goan shipyards to build galleons due to timber shortages in Europe, rather than banning it.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि इबेरियन यूनियन ने वास्तव में यूरोप में लकड़ी की कमी के कारण गैलियन बनाने के लिए गोअन शिपयार्ड का उपयोग किया था, न कि इस पर प्रतिबंध लगाया था।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the forced conversions in Hugli prior to 1632:\n1. Portuguese priests in Hugli actively baptised orphans and sold local children into slavery.\n2. These religious activities had the official backing of the Mughal Governor of Bengal.\nWhich of the statements given above is/are correct?",
        "q_hi": "1632 से पहले हुगली में जबरन धर्म परिवर्तन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. हुगली में पुर्तगाली पादरी सक्रिय रूप से अनाथों का बपतिस्मा करते थे और स्थानीय बच्चों को गुलामी में बेचते थे।\n2. इन धार्मिक गतिविधियों को बंगाल के मुगल गवर्नर का आधिकारिक समर्थन प्राप्त था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because these aggressive conversions and slave operations angered the local Mughal governors and directly led to Shah Jahan's order to capture Hugli.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि इन आक्रामक धर्म परिवर्तनों और दास गतिविधियों ने स्थानीय मुगल गवर्नरों को नाराज कर दिया और सीधे शाहजहां के हुगली पर कब्जे के आदेश का कारण बने।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Omani resurgence in the Western Indian Ocean:\n1. The Omanis captured Muscat from the Portuguese in 1650, ending Portuguese control over the Gulf entrance.\n2. The Portuguese successfully recaptured Muscat in 1652 after sending a large naval fleet from Goa.\nWhich of the statements given above is/are correct?",
        "q_hi": "पश्चिमी हिंद महासागर में ओमानी पुनरुत्थान के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ओमानी सेना ने 1650 में पुर्तगालियों से मस्कट छीन लिया, जिससे खाड़ी के प्रवेश मार्ग पर पुर्तगाली नियंत्रण समाप्त हो गया।\n2. पुर्तगालियों ने गोवा से एक बड़ा नौसैनिक बेड़ा भेजकर 1652 में मस्कट पर सफलतापूर्वक पुनः कब्जा कर लिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the loss of Muscat was permanent; the Portuguese were never able to recover it, which marked the collapse of their Arabian Sea network.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि मस्कट का नुकसान स्थायी था; पुर्तगाली इसे कभी वापस नहीं पा सके, जिसने उनके अरब सागर नेटवर्क के पतन को चिह्नित किया।"
    },
    {
        "type": "Statement-Based",
        "q_en": "Consider the following statements regarding the Dutch VOC siege of Cochin (1663):\n1. The capture of Cochin by the Dutch VOC permanently cut off Portuguese access to Malabar pepper.\n2. The local ruler of Cochin supported the Portuguese defense during the siege to prevent Dutch entry.\nWhich of the statements given above is/are correct?",
        "q_hi": "डच वीओसी द्वारा कोचीन की घेराबंदी (1663) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. डच वीओसी द्वारा कोचीन पर कब्जे ने पुर्तगालियों का मालाबार काली मिर्च तक पहुंच को स्थायी रूप से काट दिया।\n2. कोचीन के स्थानीय शासक ने डचों के प्रवेश को रोकने के लिए घेराबंदी के दौरान पुर्तगाली रक्षा का समर्थन किया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_en": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans": 0,
        "sol_en": "Statement 1 is correct. Statement 2 is incorrect because the local Cochin factions were divided, and the Dutch placed a rival king on the throne who was friendly to them, ending Portuguese influence.",
        "sol_hi": "कथन 1 सही है। कथन 2 गलत है क्योंकि स्थानीय कोचीन गुटों में विभाजन था, और डचों ने सिंहासन पर एक प्रतिद्वंद्वी राजा को बिठाया जो उनके अनुकूल था, जिससे पुर्तगाली प्रभाव समाप्त हो गया।"
    },

    # 15 Match the Following (25 to 39)
    {
        "type": "Match the Following",
        "q_en": "Match the European merchant ship types with their primary historical descriptions:",
        "q_hi": "यूरोपीय व्यापारिक जहाजों के प्रकारों का उनके प्राथमिक ऐतिहासिक विवरणों से मिलान करें:",
        "items_en": [{"left": "Carrack"}, {"left": "Fluyt"}, {"left": "Galleon"}],
        "items_hi": [{"left": "कैरैक (Carrack)"}, {"left": "फ्लूट (Fluyt)"}, {"left": "गैलियन (Galleon)"}],
        "options_en": [{"val": "0", "text": "Large, top-heavy Portuguese cargo ship designed for Cape Route"}, {"val": "1", "text": "Broad, low-cost Dutch merchant vessel with small crew requirement"}, {"val": "2", "text": "Fast, highly maneuverable English warship with lower silhouette"}],
        "options_hi": [{"val": "0", "text": "केप मार्ग के लिए डिज़ाइन किया गया बड़ा, शीर्ष-भारी पुर्तगाली मालवाहक जहाज"}, {"val": "1", "text": "कम चालक दल की आवश्यकता वाला चौड़ा, कम लागत वाला डच व्यापारिक जहाज"}, {"val": "2", "text": "निचले प्रोफाइल वाला तेज, अत्यधिक गतिशील अंग्रेजी युद्धपोत"}],
        "sol_en": "Correct match: Carrack - Portuguese cargo; Fluyt - cheap Dutch vessel; Galleon - agile English warship.",
        "sol_hi": "सही मिलान: कैरैक - पुर्तगाली मालवाहक; फ्लूट - सस्ता डच जहाज; गैलियन - फुर्तीला अंग्रेजी युद्धपोत।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the key historical milestones of the Portuguese empire with their years:",
        "q_hi": "पुर्तगाली साम्राज्य के प्रमुख ऐतिहासिक मील के पत्थरों का उनके वर्षों से मिलान करें:",
        "items_en": [{"left": "Establishment of Goa Inquisition"}, {"left": "Annexation of Portugal by Spain"}, {"left": "Restoration of Portuguese independence"}],
        "items_hi": [{"left": "गोवा धर्माधिकरण की स्थापना"}, {"left": "स्पेन द्वारा पुर्तगाल का विलय"}, {"left": "पुर्तगाली स्वतंत्रता की बहाली"}],
        "options_en": [{"val": "0", "text": "1560 CE"}, {"val": "1", "text": "1580 CE"}, {"val": "2", "text": "1640 CE"}],
        "options_hi": [{"val": "0", "text": "1560 ईस्वी"}, {"val": "1", "text": "1580 ईस्वी"}, {"val": "2", "text": "1640 ईस्वी"}],
        "sol_en": "Correct match: Inquisition - 1560; Annexation - 1580; Restoration - 1640.",
        "sol_hi": "सही मिलान: धर्माधिकरण - 1560; विलय - 1580; बहाली - 1640।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the military commanders with the historical operations they led:",
        "q_hi": "सैन्य कमांडरों का उनके द्वारा संचालित ऐतिहासिक अभियानों से मिलान करें:",
        "items_en": [{"left": "Thomas Best"}, {"left": "Chimaji Appa"}, {"left": "Qasim Khan"}],
        "items_hi": [{"left": "थॉमस बेस्ट"}, {"left": "चिमाजी अप्पा"}, {"left": "कासिम खान"}],
        "options_en": [{"val": "0", "text": "Defeated the Portuguese fleet at the Battle of Swally Hole (1612)"}, {"val": "1", "text": "Led the Maratha siege and capture of Bassein (1739)"}, {"val": "2", "text": "Executed the Mughal siege of Portuguese Hugli (1632)"}],
        "options_hi": [{"val": "0", "text": "स्वाली होल के युद्ध (1612) में पुर्तगाली बेड़े को हराया"}, {"val": "1", "text": "वसई (1739) की मराठा घेराबंदी और उस पर कब्जे का नेतृत्व किया"}, {"val": "2", "text": "पुर्तगाली हुगली (1632) की मुगल घेराबंदी को अंजाम दिया"}],
        "sol_en": "Correct match: Thomas Best - Swally; Chimaji Appa - Bassein; Qasim Khan - Hugli.",
        "sol_hi": "सही मिलान: थॉमस बेस्ट - स्वाली; चिमाजी अप्पा - वसई; कासिम खान - हुगली।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the Portuguese trade terms with their definitions:",
        "q_hi": "पुर्तगाली व्यापारिक शब्दों का उनकी परिभाषाओं से मिलान करें:",
        "items_en": [{"left": "Trato particular"}, {"left": "Venda de cargos"}, {"left": "Cartaz"}],
        "items_hi": [{"left": "त्रातो पर्टिकुलर"}, {"left": "वेंडा दे कार्गोस"}, {"left": "कार्तज"}],
        "options_en": [{"val": "0", "text": "Private trade conducted by officials for personal profit"}, {"val": "1", "text": "The sale of administrative and military offices to raise cash"}, {"val": "2", "text": "A navigation pass forced on native merchant vessels"}],
        "options_hi": [{"val": "0", "text": "व्यक्तिगत लाभ के लिए अधिकारियों द्वारा किया जाने वाला निजी व्यापार"}, {"val": "1", "text": "नकद जुटाने के लिए प्रशासनिक और सैन्य पदों की बिक्री"}, {"val": "2", "text": "देशी व्यापारिक जहाजों पर जबरन लागू किया जाने वाला नौवहन पास"}],
        "sol_en": "Correct match: Trato particular - private trade; Venda de cargos - sale of offices; Cartaz - navigation pass.",
        "sol_hi": "सही मिलान: त्रातो पर्टिकुलर - निजी व्यापार; वेंडा दे कार्गोस - पदों की बिक्री; कार्तज - नौवहन पास।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the geographic regions with their economic values in the Portuguese Empire:",
        "q_hi": "पुर्तगाली साम्राज्य में भौगोलिक क्षेत्रों का उनके आर्थिक मूल्यों से मिलान करें:",
        "items_en": [{"left": "Northern Province"}, {"left": "Minas Gerais"}, {"left": "Goa"}],
        "items_hi": [{"left": "उत्तरी प्रांत"}, {"left": "मिनस गेरैस"}, {"left": "गोवा"}],
        "options_en": [{"val": "0", "text": "Agricultural breadbasket and source of shipbuilding timber"}, {"val": "1", "text": "Lucrative gold mining hub in colonial Brazil"}, {"val": "2", "text": "Administrative capital and hub of customs collection"}],
        "options_hi": [{"val": "0", "text": "कृषि भंडार और जहाज निर्माण के लिए लकड़ी का स्रोत"}, {"val": "1", "text": "औपनिवेशिक ब्राजील में आकर्षक सोना खनन केंद्र"}, {"val": "2", "text": "प्रशासनिक राजधानी और सीमा शुल्क संग्रह का केंद्र"}],
        "sol_en": "Correct match: Northern Province - food/timber; Minas Gerais - gold; Goa - administration/customs.",
        "sol_hi": "सही मिलान: उत्तरी प्रांत - भोजन/लकड़ी; मिनस गेरैस - सोना; गोवा - प्रशासन/सीमा शुल्क।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the Portuguese officials with their primary administrative duties:",
        "q_hi": "पुर्तगाली अधिकारियों का उनके प्राथमिक प्रशासनिक कर्तव्यों से मिलान करें:",
        "items_en": [{"left": "Vedor da Fazenda"}, {"left": "Viceroy"}, {"left": "Capitão"}],
        "items_hi": [{"left": "वेडोर दा फजेंडा"}, {"left": "वायसराय"}, {"left": "कैपिटाओ"}],
        "options_en": [{"val": "0", "text": "Chief superintendent of finances and customs"}, {"val": "1", "text": "Supreme civil and military head of the Estado da Índia"}, {"val": "2", "text": "Commander of a local fortress and customs collector"}],
        "options_hi": [{"val": "0", "text": "वित्त और सीमा शुल्क के मुख्य अधीक्षक"}, {"val": "1", "text": "एस्टाडो दा इंडिया के सर्वोच्च नागरिक और सैन्य प्रमुख"}, {"val": "2", "text": "स्थानीय किले के कमांडर और सीमा शुल्क संग्रहकर्ता"}],
        "sol_en": "Correct match: Vedor - finance; Viceroy - head; Capitão - fort commander.",
        "sol_hi": "सही मिलान: वेडोर - वित्त; वायसराय - प्रमुख; कैपिटाओ - किला कमांडर।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the trading companies with their governing bodies or controlling systems:",
        "q_hi": "व्यापारिक कंपनियों का उनके शासी निकायों या नियंत्रण प्रणालियों से मिलान करें:",
        "items_en": [{"left": "Dutch East India Company (VOC)"}, {"left": "English East India Company (EIC)"}, {"left": "Estado da Índia"}],
        "items_hi": [{"left": "डच ईस्ट इंडिया कंपनी (VOC)"}, {"left": "अंग्रेजी ईस्ट इंडिया कंपनी (EIC)"}, {"left": "एस्टाडो दा इंडिया"}],
        "options_en": [{"val": "0", "text": "Governed by the Heeren XVII (Lords Seventeen)"}, {"val": "1", "text": "Governed by the Court of Directors in London"}, {"val": "2", "text": "Controlled directly by the Conselho da Índia in Lisbon"}],
        "options_hi": [{"val": "0", "text": "हेरेन XVII (Lords Seventeen) द्वारा शासित"}, {"val": "1", "text": "लंदन में कोर्ट ऑफ डायरेक्टर्स द्वारा शासित"}, {"val": "2", "text": "लिस्बन में कौंसिलहो दा इंडिया द्वारा सीधे नियंत्रित"}],
        "sol_en": "Correct match: VOC - Heeren XVII; EIC - Court of Directors; Estado - Conselho da India.",
        "sol_hi": "सही मिलान: वीओसी - हेरेन XVII; ईआईसी - कोर्ट ऑफ डायरेक्टर्स; एस्टाडो - कौंसिलहो दा इंडिया।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the key territorial losses with their respective regions in Asia:",
        "q_hi": "प्रमुख क्षेत्रीय नुकसानों का एशिया में उनके संबंधित क्षेत्रों से मिलान करें:",
        "items_en": [{"left": "Loss of Hugli"}, {"left": "Loss of Bassein"}, {"left": "Loss of Ormuz"}],
        "items_hi": [{"left": "हुगली का नुकसान"}, {"left": "वसई का नुकसान"}, {"left": "होर्मुज का नुकसान"}],
        "options_en": [{"val": "0", "text": "Bengal Province, Eastern India"}, {"val": "1", "text": "Konkan Coast, Western India"}, {"val": "2", "text": "Persian Gulf, Western Asia"}],
        "options_hi": [{"val": "0", "text": "बंगाल प्रांत, पूर्वी भारत"}, {"val": "1", "text": "कोंकण तट, पश्चिमी भारत"}, {"val": "2", "text": "फारस की खाड़ी, पश्चिमी एशिया"}],
        "sol_en": "Correct match: Hugli - Bengal; Bassein - Konkan; Ormuz - Persian Gulf.",
        "sol_hi": "सही मिलान: हुगली - बंगाल; वसई - कोंकण; होर्मुज - फारस की खाड़ी।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the religious policies of Goa with their historical actions:",
        "q_hi": "गोवा की धार्मिक नीतियों का उनकी ऐतिहासिक कार्रवाइयों से मिलान करें:",
        "items_en": [{"left": "Goa Inquisition (1560)"}, {"left": "Anti-Hindu Decrees (1567)"}, {"left": "Konkani Language Ban (1684)"}],
        "items_hi": [{"left": "गोवा धर्माधिकरण (1560)"}, {"left": "हिंदू विरोधी आदेश (1567)"}, {"left": "कोंकणी भाषा पर प्रतिबंध (1684)"}],
        "options_en": [{"val": "0", "text": "Establishment of the tribunal to check heresy of converts"}, {"val": "1", "text": "Destruction of over 300 temples in Salcete province"}, {"val": "2", "text": "Total prohibition on the native spoken language of Goa"}],
        "options_hi": [{"val": "0", "text": "धर्म परिवर्तित लोगों के पाखंड की जांच के लिए न्यायाधिकरण की स्थापना"}, {"val": "1", "text": "साल्सेट प्रांत में 300 से अधिक मंदिरों का विनाश"}, {"val": "2", "text": "गोवा की बोली जाने वाली स्थानीय भाषा पर पूर्ण प्रतिबंध"}],
        "sol_en": "Correct match: Inquisition - tribunal; Decrees - temple destruction; Konkani ban - native language prohibition.",
        "sol_hi": "सही मिलान: धर्माधिकरण - न्यायाधिकरण; आदेश - मंदिर विनाश; कोंकणी प्रतिबंध - स्थानीय भाषा निषेध।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the historical treaties with their geopolitical outcomes:",
        "q_hi": "ऐतिहासिक संधियों का उनके भू-राजनीतिक परिणामों से मिलान करें:",
        "items_en": [{"left": "Treaty of Thomar"}, {"left": "Treaty of Pune"}, {"left": "Treaty of Lisbon"}],
        "items_hi": [{"left": "तोमर की संधि"}, {"left": "पुणे की संधि"}, {"left": "लिस्बन की संधि"}],
        "options_en": [{"val": "0", "text": "Created the Iberian Union under Spanish monarchy in 1581"}, {"val": "1", "text": "Formalised the surrender of Bassein to the Marathas in 1739"}, {"val": "2", "text": "Spanish recognition of Portuguese independence in 1668"}],
        "options_hi": [{"val": "0", "text": "1581 में स्पैनिश राजशाही के तहत इबेरियन यूनियन का निर्माण किया"}, {"val": "1", "text": "1739 में मराठों को वसई सौंपने को औपचारिक रूप दिया"}, {"val": "2", "text": "1668 में पुर्तगाली स्वतंत्रता को स्पैनिश मान्यता दी"}],
        "sol_en": "Correct match: Thomar - Iberian Union; Pune - Bassein surrender; Lisbon - Spanish recognition.",
        "sol_hi": "सही मिलान: तोमर - इबेरियन यूनियन; पुणे - वसई समर्पण; लिस्बन - स्पैनिश मान्यता।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the historical battle sites with their respective years:",
        "q_hi": "ऐतिहासिक युद्ध स्थलों का उनके संबंधित वर्षों से मिलान करें:",
        "items_en": [{"left": "Battle of Swally Hole"}, {"left": "Battle of Alcácer Quibir"}, {"left": "Siege of Bassein"}],
        "items_hi": [{"left": "स्वाली होल का युद्ध"}, {"left": "अलकासर क्विबीर का युद्ध"}, {"left": "वसई की घेराबंदी"}],
        "options_en": [{"val": "0", "text": "1612 CE"}, {"val": "1", "text": "1578 CE"}, {"val": "2", "text": "1737–1739 CE"}],
        "options_hi": [{"val": "0", "text": "1612 ईस्वी"}, {"val": "1", "text": "1578 ईस्वी"}, {"val": "2", "text": "1737–1739 ईस्वी"}],
        "sol_en": "Correct match: Swally Hole - 1612; Alcácer Quibir - 1578; Bassein - 1737-1739.",
        "sol_hi": "सही मिलान: स्वाली होल - 1612; अलकासर क्विबीर - 1578; वसई - 1737-1739।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the historical monarchs with their respective roles in empire administration:",
        "q_hi": "ऐतिहासिक सम्राटों का साम्राज्य प्रशासन में उनकी संबंधित भूमिकाओं से मिलान करें:",
        "items_en": [{"left": "King Sebastian"}, {"left": "Marquis de Pombal"}, {"left": "Queen Maria I"}],
        "items_hi": [{"left": "राजा सेबेस्टियन"}, {"left": "मार्क्विस डी पोम्बल"}, {"left": "रानी मारिया प्रथम"}],
        "options_en": [{"val": "0", "text": "Died without heirs in Morocco, causing succession crisis"}, {"val": "1", "text": "Prime Minister who suspended the Goa Inquisition in 1774"}, {"val": "2", "text": "Monarch who reinstated the Goa Inquisition in 1778"}],
        "options_hi": [{"val": "0", "text": "मोरक्को में बिना उत्तराधिकारी के मारे गए, जिससे उत्तराधिकार संकट हुआ"}, {"val": "1", "text": "प्रधानमंत्री जिन्होंने 1774 में गोवा धर्माधिकरण को निलंबित किया"}, {"val": "2", "text": "शासक जिन्होंने 1778 में गोवा धर्माधिकरण को बहाल किया"}],
        "sol_en": "Correct match: Sebastian - crisis; Pombal - suspended; Maria I - reinstated.",
        "sol_hi": "सही मिलान: सेबेस्टियन - संकट; पोम्बल - निलंबित; मारिया प्रथम - बहाल।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the regional rulers in India with their actions against the Portuguese:",
        "q_hi": "भारत के क्षेत्रीय शासकों का पुर्तगालियों के खिलाफ उनके कार्यों से मिलान करें:",
        "items_en": [{"left": "Shah Abbas I"}, {"left": "Shah Jahan"}, {"left": "Peshwa Baji Rao I"}],
        "items_hi": [{"left": "शाह अब्बास प्रथम"}, {"left": "शाहजहां"}, {"left": "पेशवा बाजीराव प्रथम"}],
        "options_en": [{"val": "0", "text": "Allied with English EIC to capture Ormuz in 1622"}, {"val": "1", "text": "Ordered the capture of Portuguese Hugli in 1632"}, {"val": "2", "text": "Authorized the military campaign to capture Bassein in 1737"}],
        "options_hi": [{"val": "0", "text": "1622 में होर्मुज पर कब्जे के लिए अंग्रेजी ईआईसी के साथ गठबंधन किया"}, {"val": "1", "text": "1632 में पुर्तगाली हुगली पर कब्जे का आदेश दिया"}, {"val": "2", "text": "1737 में वसई पर कब्जे के लिए सैन्य अभियान को अधिकृत किया"}],
        "sol_en": "Correct match: Shah Abbas I - Ormuz; Shah Jahan - Hugli; Baji Rao I - Bassein campaign.",
        "sol_hi": "सही मिलान: शाह अब्बास प्रथम - होर्मुज; शाहजहां - हुगली; बाजीराव प्रथम - वसई अभियान।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the historical migrant groups with their safe havens during the Inquisition:",
        "q_hi": "धर्माधिकरण के दौरान ऐतिहासिक प्रवासी समूहों का उनके सुरक्षित शरणस्थलों से मिलान करें:",
        "items_en": [{"left": "Saraswat Brahmin Merchants"}, {"left": "Crypto-Jews"}, {"left": "New Christians under trial"}],
        "items_hi": [{"left": "सारस्वत ब्राह्मण व्यापारी"}, {"left": "क्रिप्टो-यहूदी"}, {"left": "जांच के अधीन नए ईसाई"}],
        "options_en": [{"val": "0", "text": "Migrated to Canara Coast under Keladi Nayakas"}, {"val": "1", "text": "Fled to Netherlands and Amsterdam for religious freedom"}, {"val": "2", "text": "Imprisoned in Casa da Inquisição in Goa"}],
        "options_hi": [{"val": "0", "text": "केलादि नायकों के अधीन कनारा तट पर चले गए"}, {"val": "1", "text": "धार्मिक स्वतंत्रता के लिए नीदरलैंड और एम्स्टर्डम भाग गए"}, {"val": "2", "text": "गोवा में कासा दा इनक्विजिशन में कैद किए गए"}],
        "sol_en": "Correct match: Saraswats - Canara; Crypto-Jews - Netherlands; New Christians - Goa prisons.",
        "sol_hi": "सही मिलान: सारस्वत - कनारा; क्रिप्टो-यहूदी - नीदरलैंड; नए ईसाई - गोवा जेल।"
    },
    {
        "type": "Match the Following",
        "q_en": "Match the siege methods with the historical siege operations:",
        "q_hi": "घेराबंदी के तरीकों का ऐतिहासिक घेराबंदी अभियानों से मिलान करें:",
        "items_en": [{"left": "Tunneling and Gunpowder Mines"}, {"left": "River blockades using boats"}, {"left": "Coordinated land force and naval blockade"}],
        "items_hi": [{"left": "सुरंग बनाना और बारूद की खदानें"}, {"left": "नावों का उपयोग करके नदी नाकेबंदी"}, {"left": "समन्वित जमीनी सेना और नौसैनिक नाकेबंदी"}],
        "options_en": [{"val": "0", "text": "Used by Marathas during the Siege of Bassein (1739)"}, {"val": "1", "text": "Used by Mughals during the Siege of Hugli (1632)"}, {"val": "2", "text": "Used by Anglo-Persian forces during the capture of Ormuz (1622)"}],
        "options_hi": [{"val": "0", "text": "वसई की घेराबंदी (1739) के दौरान मराठों द्वारा उपयोग किया गया"}, {"val": "1", "text": "हुगली की घेराबंदी (1632) के दौरान मुगलों द्वारा उपयोग किया गया"}, {"val": "2", "text": "होर्मुज पर कब्जे (1622) के दौरान एंग्लो-फारसी सेनाओं द्वारा उपयोग किया गया"}],
        "sol_en": "Correct match: Tunneling - Bassein; River blockades - Hugli; Land/Sea blockade - Ormuz.",
        "sol_hi": "सही मिलान: सुरंग बनाना - वसई; नदी नाकेबंदी - हुगली; थल/जल नाकेबंदी - होर्मुज।"
    },

    # 10 Assertion-Reason (40 to 49)
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Dutch East India Company (VOC) was financially more resilient than the Portuguese Estado da Índia.\nReason (R): The VOC operated as a joint-stock company with public shareholding, whereas the Estado da Índia was a crown monopoly financed directly by the treasury.",
        "q_hi": "अभिकथन (A): डच ईस्ट इंडिया कंपनी (VOC) वित्तीय रूप से पुर्तगाली एस्टाडो दा इंडिया की तुलना में अधिक लचीली थी।\nकारण (R): वीओसी सार्वजनिक शेयरधारिता वाली एक संयुक्त-पूंजी कंपनी के रूप में काम करती थी, जबकि एस्टाडो दा इंडिया एक शाही एकाधिकार था जिसे सीधे खजाने द्वारा वित्तपोषित किया जाता था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The joint-stock structure allowed the VOC to raise massive public capital and absorb losses, whereas the Portuguese crown monopoly was plagued by state budget deficits, making R the correct explanation of A.",
        "sol_hi": "संयुक्त-पूंजी संरचना ने वीओसी को बड़े पैमाने पर सार्वजनिक पूंजी जुटाने और नुकसान को सहन करने की अनुमति दी, जबकि पुर्तगाली शाही एकाधिकार राज्य के बजट घाटे से ग्रस्त था, जिससे R, A की सही व्याख्या करता है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The establishment of the Goa Inquisition in 1560 triggered a significant economic decline in Goa.\nReason (R): The Inquisition forced wealthy Saraswat Brahmin merchants and skilled artisans to flee to neighboring territories.",
        "q_hi": "अभिकथन (A): 1560 में गोवा धर्माधिकरण की स्थापना ने गोवा में एक महत्वपूर्ण आर्थिक गिरावट को शुरू किया।\nकारण (R): धर्माधिकरण ने धनी सारस्वत ब्राह्मण व्यापारियों और कुशल कारीगरों को पड़ोसी क्षेत्रों में भागने के लिए मजबूर किया।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The migration of merchants and artisans to Canara and Vengurla drained Goa of capital and labor, crippling its tax base and port trade, which explains the economic decline.",
        "sol_hi": "व्यापारियों और कारीगरों के कनारा और वेनगुर्ला पलायन ने गोवा को पूंजी और श्रम से वंचित कर दिया, जिससे उसका कर आधार और बंदरगाह व्यापार पंगु हो गया, जो आर्थिक गिरावट की व्याख्या करता है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): Spain systematically diverted Portuguese naval resources to European theatres during the Iberian Union.\nReason (R): The Spanish Habsburg monarchs were engaged in major global conflicts like the Thirty Years' War and the Anglo-Spanish War.",
        "q_hi": "अभिकथन (A): स्पेन ने इबेरियन यूनियन के दौरान पुर्तगाली नौसैनिक संसाधनों को व्यवस्थित रूप से यूरोपीय क्षेत्रों में स्थानांतरित किया।\nकारण (R): स्पैनिश हैब्सबर्ग सम्राट तीस वर्षीय युद्ध (Thirty Years' War) और एंग्लो-स्पैनिश युद्ध जैसे बड़े वैश्विक संघर्षों में शामिल थे।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "To defend its European empire, Spain drafted Portuguese galleons and sailors (such as for the Armada of 1588), neglecting the defense of Goa, making R the correct explanation.",
        "sol_hi": "अपने यूरोपीय साम्राज्य की रक्षा के लिए, स्पेन ने पुर्तगाली गैलियन और नाविकों (जैसे 1588 के आर्मडा के लिए) की भर्ती की, जिससे गोवा की रक्षा की उपेक्षा हुई, जिससे R सही व्याख्या है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The discovery of Brazil led to the systematic neglect of Portuguese colonial interests in India.\nReason (R): Brazil sugarcane plantations and later gold mines were far more profitable and safer than the Cape Route spice trade.",
        "q_hi": "अभिकथन (A): ब्राजील की खोज ने भारत में पुर्तगाली औपनिवेशिक हितों की व्यवस्थित उपेक्षा को जन्म दिया।\nकारण (R): ब्राजील के चीनी बागान और बाद में सोने की खदानें केप मार्ग के मसाला व्यापार की तुलना में कहीं अधिक लाभदायक और सुरक्षित थीं।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "Because Brazil offered high profits with less military resistance from powerful states compared to Asia, the Crown and merchants diverted manpower and capital there, explaining the neglect of India.",
        "sol_hi": "चूंकि ब्राजील ने एशिया की तुलना में शक्तिशाली राज्यों से कम सैन्य प्रतिरोध के साथ उच्च लाभ की पेशकश की, इसलिए क्राउन और व्यापारियों ने जनशक्ति और पूंजी को वहां स्थानांतरित कर दिया, जो भारत की उपेक्षा की व्याख्या करता है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Marathas successfully captured Bassein in 1739 despite its massive stone fortifications.\nReason (R): The Marathas cut off Bassein from sea-borne reinforcements and used advanced mining techniques to breach the walls.",
        "q_hi": "अभिकथन (A): 1739 में मराठों ने वसई के भारी पत्थरों के किलों के बावजूद उस पर सफलतापूर्वक कब्जा कर लिया था।\nकारण (R): मराठों ने वसई को समुद्र के रास्ते से आने वाली कुमक से काट दिया और दीवारों को तोड़ने के लिए उन्नत खनन (सुरंग) तकनीकों का उपयोग किया।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The combination of naval blockade to stop reinforcements and gunpowder mines to blow up the stone walls allowed the Marathas to capture Bassein, making R the correct explanation.",
        "sol_hi": "कुमक को रोकने के लिए नौसैनिक नाकेबंदी और पत्थरों की दीवारों को उड़ाने के लिए बारूद की सुरंगों के संयोजन ने मराठों को वसई पर कब्जा करने की अनुमति दी, जिससे R सही व्याख्या है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): Portuguese Viceroy terms in Goa were restricted strictly to three years by the Crown.\nReason (R): The Crown wanted to prevent viceroys from establishing independent local power bases in India.",
        "q_hi": "अभिकथन (A): गोवा में पुर्तगाली वायसराय का कार्यकाल क्राउन द्वारा कड़ाई से तीन साल तक सीमित किया गया था।\nकारण (R): क्राउन भारत में वायसरायों को स्वतंत्र स्थानीय शक्ति आधार स्थापित करने से रोकना चाहता था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The fear of colonial rebellion and governors declaring independence led to the three-year restriction, making R the correct explanation of A.",
        "sol_hi": "औपनिवेशिक विद्रोह और गवर्नरों द्वारा स्वतंत्रता घोषित करने के डर के कारण तीन साल का प्रतिबंध लगाया गया था, जिससे R, A की सही व्याख्या करता है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): Shah Jahan ordered the expulsion of the Portuguese from Hugli in 1632.\nReason (R): The Portuguese at Hugli had built a strong alliance with the Dutch VOC to overthrow Mughal rule in Bengal.",
        "q_hi": "अभिकथन (A): शाहजहां ने 1632 में हुगली से पुर्तगालियों के निष्कासन का आदेश दिया था।\nकारण (R): हुगली में पुर्तगालियों ने बंगाल में मुगल शासन को उखाड़ फेंकने के लिए डच वीओसी के साथ एक मजबूत गठबंधन बनाया था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 2,
        "sol_en": "Assertion A is true, but Reason R is false. The Portuguese were expelled due to their piracy, slave trading, and forced conversions, not because of any alliance with the Dutch to overthrow the Mughals (who were actually enemies of the Portuguese).",
        "sol_hi": "अभिकथन A सही है, लेकिन कारण R गलत है। पुर्तगालियों को उनकी डकैती, दास व्यापार और जबरन धर्म परिवर्तन के कारण निकाला गया था, न कि मुगलों को उखाड़ फेंकने के लिए डचों के साथ किसी गठबंधन के कारण (जो वास्तव में पुर्तगालियों के दुश्मन थे)।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The Portuguese lost their monopoly over the Persian Gulf trade after 1622.\nReason (R): A joint Safavid Persian and English East India Company force captured the strategic island fortress of Ormuz in 1622.",
        "q_hi": "अभिकथन (A): पुर्तगालियों ने 1622 के बाद फारस की खाड़ी के व्यापार पर अपना एकाधिकार खो दिया था।\nकारण (R): एक संयुक्त सफाविद फारसी और अंग्रेजी ईस्ट इंडिया कंपनी की सेना ने 1622 में रणनीतिक होर्मुज द्वीप किले पर कब्जा कर लिया था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "The loss of Ormuz, the main choke point of the Persian Gulf, directly broke the Portuguese monopoly and allowed English merchants to enter Gulf trade, making R the correct explanation.",
        "sol_hi": "फारस की खाड़ी के मुख्य चोक पॉइंट होर्मुज के नुकसान ने सीधे पुर्तगाली एकाधिकार को तोड़ दिया और अंग्रेजी व्यापारियों को खाड़ी व्यापार में प्रवेश करने की अनुमति दी, जिससे R सही व्याख्या है।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The small population of Portugal was a major limiting factor in maintaining its global empire.\nReason (R): With a domestic population of about one million in the 16th century, Portugal lacked the manpower to recruit enough soldiers and sailors to defend both its Asian and American territories.",
        "q_hi": "अभिकथन (A): पुर्तगाल की छोटी आबादी उसके वैश्विक साम्राज्य को बनाए रखने में एक प्रमुख सीमित कारक थी।\nकारण (R): 16वीं शताब्दी में लगभग दस लाख की घरेलू आबादी के साथ, पुर्तगाल के पास अपने एशियाई और अमेरिकी दोनों क्षेत्रों की रक्षा के लिए पर्याप्त सैनिकों और नाविकों की भर्ती करने के लिए जनशक्ति की कमी थी।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 0,
        "sol_en": "Demographic limits meant that Portugal suffered chronic shortages of military personnel, directly explaining why they could not defend their scattered Asian bases against larger European and Indian forces.",
        "sol_hi": "जनसांख्यिकीय सीमाओं का मतलब था कि पुर्तगाल को सैन्य कर्मियों की पुरानी कमी का सामना करना पड़ा, जो सीधे तौर पर यह बताता है कि वे बड़ी यूरोपीय और भारतीय सेनाओं के खिलाफ अपने बिखरे हुए एशियाई ठिकानों की रक्षा क्यों नहीं कर सके।"
    },
    {
        "type": "Assertion-Reason",
        "q_en": "Assertion (A): The sale of offices (venda de cargos) in Goa helped the Portuguese Crown raise immediate funds.\nReason (R): The buyers of these offices were highly trained military officers appointed based on their combat experience in Europe.",
        "q_hi": "अभिकथन (A): गोवा में पदों की बिक्री (वेंडा दे कार्गोस) ने पुर्तगाली क्राउन को तत्काल धन जुटाने में मदद की थी।\nकारण (R): इन पदों के खरीदार अत्यधिक प्रशिक्षित सैन्य अधिकारी थे जिन्हें यूरोप में उनके युद्ध के अनुभव के आधार पर नियुक्त किया गया था।",
        "opts_en": EN_AR_OPTS,
        "opts_hi": HI_AR_OPTS,
        "ans": 2,
        "sol_en": "Assertion A is true, but Reason R is false. The offices were sold to the highest bidder regardless of their military competency or training, which led to incompetent leadership.",
        "sol_hi": "अभिकथन A सही है, लेकिन कारण R गलत है। पद सैन्य योग्यता या प्रशिक्षण की परवाह किए बिना उच्चतम बोलीदाता को बेचे गए थे, जिससे अक्षम नेतृत्व का उदय हुआ।"
    }
]
