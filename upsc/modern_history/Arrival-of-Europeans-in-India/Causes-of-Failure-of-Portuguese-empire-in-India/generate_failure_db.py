import os
import json

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Causes-of-Failure-of-Portuguese-empire-in-India"
os.makedirs(os.path.join(BASE_DIR, "hi"), exist_ok=True)

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

en_data = {
  "breadcrumbs": {
    "parent": "UPSC Syllabus",
    "parentUrl": "/upsc/",
    "current": "Causes of Failure of Portuguese Empire"
  },
  "hero": {
    "title": "Causes of Failure of the Portuguese Empire in India",
    "description": "Master the strategic, political, and socio-religious factors that led to the decline of Portuguese power in India, including the rise of rival European powers, religious intolerance, the Iberian Union, the discovery of Brazil, and administrative corruption."
  },
  "timeline": {
    "title": "Chronology of Portuguese Decline in India",
    "description": "Key events marking the transition from dominance to decline of the Portuguese Eastern Empire.",
    "cards": [
      {
        "period": "Goa Inquisition",
        "date": "1560 CE",
        "details": "Establishment of the Inquisition in Goa, leading to mass religious persecution, destruction of temples, and the flight of wealthy local merchants."
      },
      {
        "period": "Iberian Union",
        "date": "1580–1640 CE",
        "details": "Portuguese crown is annexed by Spain, dragging Portugal into Spain's European wars and inviting attacks on Portuguese colonies by the Dutch and English."
      },
      {
        "period": "Battle of Swally",
        "date": "1612 CE",
        "details": "English Captain Thomas Best defeats a Portuguese fleet near Surat, destroying the myth of Portuguese naval invincibility in Mughal eyes."
      },
      {
        "period": "Loss of Hugli",
        "date": "1632 CE",
        "details": "Mughal Emperor Shah Jahan orders the siege and capture of Hugli, expelling the Portuguese from Bengal due to piracy and slave trading."
      },
      {
        "period": "Loss of Bassein",
        "date": "1739 CE",
        "details": "Maratha forces under Chimaji Appa capture the fortified city of Bassein, stripping the Portuguese of their fertile Northern Province."
      }
    ]
  },
  "mnemonics": {
    "title": "Mnemonics for Portuguese Decline",
    "description": "Use these memory aids to retain key concepts.",
    "items": [
      {
        "title": "Five Pillars of Decline",
        "phrase": "\"R-R-I-B-C\" — Rivals, Religion, Iberian Union, Brazil, Corruption",
        "decryption": "Rival powers, Religious intolerance, Iberian Union impact, Brazil diversion, and Corruption."
      },
      {
        "title": "Loss of Key Territories",
        "phrase": "\"H-O-M-B\" — Hugli, Ormuz, Malacca, Bassein",
        "decryption": "The sequence of major territorial losses that crippled the Estado da Índia."
      }
    ]
  },
  "traps": {
    "title": "Common UPSC Exam Traps",
    "items": [
      "<strong>Trap 1: The Timeline of Sati Ban vs. Inquisition:</strong> Do not confuse the early ban on Sati by Albuquerque (1510) with the tolerant phase. The establishment of the Goa Inquisition in 1560 marked a hard turn toward religious persecution.",
      "<strong>Trap 2: Iberian Union Cause:</strong> Do not assume Spain conquered Portugal by force due to a resource war. The personal union arose from the death of young King Sebastian without heirs in 1578.",
      "<strong>Trap 3: Hugli Expulsion:</strong> Remember that Hugli was captured by the Mughals (Shah Jahan in 1632), not the British. The British only established trading dominance later."
    ]
  },
  "deepDive": {
    "title": "Syllabus Core Study Notes (Deep-Dive)",
    "description": "Detailed notes on the causes of the failure of the Portuguese empire in India.",
    "sections": []
  }
}

hi_data = {
  "breadcrumbs": {
    "parent": "यूपीएससी पाठ्यक्रम",
    "parentUrl": "/upsc/",
    "current": "पुर्तगाली साम्राज्य के पतन के कारण"
  },
  "hero": {
    "title": "भारत में पुर्तगाली साम्राज्य के पतन के कारण",
    "description": "भारत में पुर्तगाली सत्ता के पतन के रणनीतिक, राजनीतिक और सामाजिक-धार्मिक कारणों को समझें, जिनमें प्रतिद्वंद्वी यूरोपीय शक्तियों का उदय, धार्मिक असहिष्णुता, इबेरियन यूनियन, ब्राजील की खोज और प्रशासनिक भ्रष्टाचार शामिल हैं।"
  },
  "timeline": {
    "title": "भारत में पुर्तगाली पतन का कालक्रम",
    "description": "पुर्तगाली पूर्वी साम्राज्य के वर्चस्व से पतन की ओर संक्रमण को दर्शाने वाली प्रमुख घटनाएं।",
    "cards": [
      {
        "period": "गोवा इनक्विजिशन",
        "date": "1560 ई.",
        "details": "गोवा में इनक्विजिशन (धर्माधिकरण) की स्थापना, जिससे बड़े पैमाने पर धार्मिक उत्पीड़न हुआ, मंदिर नष्ट किए गए और स्थानीय हिंदू व्यापारी भागने को विवश हुए।"
      },
      {
        "period": "इबेरियन यूनियन",
        "date": "1580–1640 ई.",
        "details": "पुर्तगाली क्राउन का स्पेन में विलय हुआ, जिससे पुर्तगाल स्पेन के यूरोपीय युद्धों में घसीट लिया गया और डच तथा अंग्रेजों ने पुर्तगाली बस्तियों पर हमले किए।"
      },
      {
        "period": "स्वाली का युद्ध",
        "date": "1612 ई.",
        "details": "अंग्रेज कैप्टन थॉमस बेस्ट ने सूरत के पास पुर्तगाली बेड़े को हराया, जिससे मुगलों की नजर में पुर्तगाली नौसैनिक अजेयता का मिथक टूट गया।"
      },
      {
        "period": "हुगली का पतन",
        "date": "1632 ई.",
        "details": "मुगल सम्राट शाहजहां ने हुगली की घेराबंदी और कब्जा करने का आदेश दिया, पुर्तगालियों को उनकी डकैती और दास व्यापार के कारण बंगाल से निष्कासित कर दिया।"
      },
      {
        "period": "वसई (बसीन) का पतन",
        "date": "1739 ई.",
        "details": "चिमाजी अप्पा के नेतृत्व में मराठा सेना ने वसई के किले पर कब्जा कर लिया, जिससे पुर्तगालियों के हाथ से उनका उपजाऊ उत्तरी प्रांत निकल गया।"
      }
    ]
  },
  "mnemonics": {
    "title": "पुर्तगाली पतन को याद रखने के लिए निमोनिक्स",
    "description": "प्रमुख अवधारणाओं को याद रखने के लिए इन स्मृति साधनों का उपयोग करें।",
    "items": [
      {
        "title": "पतन के पांच स्तंभ",
        "phrase": "\"R-R-I-B-C\" — प्रतिद्वंद्वी, धर्म, इबेरियन यूनियन, ब्राजील, भ्रष्टाचार",
        "decryption": "प्रतिद्वंद्वी शक्तियां, धार्मिक असहिष्णुता, इबेरियन यूनियन का प्रभाव, ब्राजील की ओर ध्यान भटकाना, और भ्रष्टाचार।"
      },
      {
        "title": "प्रमुख क्षेत्रों का नुकसान",
        "phrase": "\"H-O-M-B\" — हुगली, होर्मुज, मलक्का, बसीन",
        "decryption": "प्रमुख क्षेत्रीय नुकसानों का क्रम जिसने एस्टाडो दा इंडिया को पंगु बना दिया।"
      }
    ]
  },
  "traps": {
    "title": "सामान्य यूपीएससी परीक्षा के जाल",
    "items": [
      "<strong>जाल 1: सती प्रतिबंध बनाम इनक्विजिशन का कालक्रम:</strong> अल्बुकर्क (1510) द्वारा सती प्रथा पर शुरुआती प्रतिबंध को सहिष्णु चरण समझने की भूल न करें। 1560 में गोवा इनक्विजिशन की स्थापना ने धार्मिक उत्पीड़न की ओर एक कठोर मोड़ का संकेत दिया।",
      "<strong>जाल 2: इबेरियन यूनियन का कारण:</strong> यह न मानें कि स्पेन ने पुर्तगाल को सैन्य युद्ध के माध्यम से जीता था। यह व्यक्तिगत संघ 1578 में युवा राजा सेबेस्टियन की बिना किसी वारिस के मृत्यु के कारण उत्पन्न हुआ था।",
      "<strong>जाल 3: हुगली से निष्कासन:</strong> याद रखें कि हुगली पर मुगलों (1632 में शाहजहां) ने कब्जा किया था, न कि अंग्रेजों ने। अंग्रेजों ने केवल बाद में व्यापारिक वर्चस्व स्थापित किया था।"
    ]
  },
  "deepDive": {
    "title": "पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)",
    "description": "भारत में पुर्तगाली साम्राज्य के पतन के कारणों पर विस्तृत नोट्स।",
    "sections": []
  }
}

en_sections = [
  {
    "title": "1. Rise of Rival European Powers (Naval Dominance of Dutch & English)",
    "content": "<p><strong>Financial Models:</strong> The establishment of the English East India Company (EIC) in 1600 and the Dutch East India Company (VOC) in 1602 introduced a superior joint-stock corporation model. Unlike the Portuguese crown-controlled monopoly, which was slow, highly centralized, and plagued by bureaucratic inefficiency, the Dutch and English companies mobilized massive capital from public shareholders. This separated business operations from state politics, allowed shared risk, and provided continuous funding even during military conflicts.</p><p><strong>Naval Technology:</strong> The Dutch and English fleets featured significant technological advantages. The Dutch designed the <em>Fluyt</em>, a highly cost-efficient cargo ship with a broad hull and cheap construction, requiring a small crew to handle large cargo volumes. The English constructed faster, more maneuverable <em>Galleons</em> with lower silhouettes, less vulnerable to broadsides, and carrying heavier, long-range naval artillery. The Portuguese <em>Carracks</em>, by contrast, were top-heavy, slow, and designed primarily for cargo transport rather than combat, making them easy targets for agile enemy warships.</p>"
  },
  {
    "title": "2. Religious Intolerance, Persecution, and the Goa Inquisition",
    "content": "<p><strong>The Inquisition:</strong> Established in 1560 on the petition of the Jesuit missionary Francis Xavier, the Goa Inquisition marked a sharp turn away from the pragmatic, initial tolerance of Portuguese rule. The Inquisition sought to punish heresy and enforce Catholic orthodoxy. It targeted not only indigenous residents but particularly 'New Christians' (Jewish and Hindu converts) suspected of secretly practicing their ancestral faiths (Crypto-Jews and Crypto-Hindus).</p><p><strong>Economic Consequences:</strong> The intolerant policies included the destruction of Hindu and Buddhist temples, the prohibition of public non-Christian rituals, marriages, and festivals, and the suppression of the local Konkani language (banned in official use in 1684). This institutional intolerance alienated the local population and destroyed local alliances. Crucially, it triggered a massive migration of wealthy Saraswat Brahmin merchants, skilled artisans, and agriculturalists to neighboring territories like Vengurla (under the Dutch) and the Canara coast. This flight of capital and labor severely damaged Goa's tax base and local trade networks.</p>"
  },
  {
    "title": "3. Iberian Union (1580–1640) and Spanish Neglect of Eastern Trade",
    "content": "<p><strong>The Personal Union:</strong> In 1578, the young Portuguese King Sebastian was killed during a disastrous military expedition in Morocco (the Battle of Alcácer Quibir), leaving no heirs. This triggered a succession crisis, resulting in the annexation of Portugal by King Philip II of Spain in 1580, forming the Iberian Union. Although Portugal retained its administration, its foreign policy was subsumed under the Spanish Habsburg monarchy.</p><p><strong>Imperial Neglect:</strong> The Iberian Union dragged Portugal into Spain's global conflicts, particularly the Eighty Years' War against the Dutch Republic and the Anglo-Spanish War. Consequently, Portuguese shipping and colonies in Asia became legitimate targets for the aggressive Dutch and English navies. Furthermore, Spanish monarchs prioritized American silver mines (Potosí) and European land campaigns, neglecting Lisbon's eastern spice trade. The Portuguese Estado da Índia was starved of naval reinforcements, capital, and shipbuilding supplies, leading to the decay of its maritime defense system and the loss of key forts like Ormuz (1622).</p>"
  },
  {
    "title": "4. Discovery of Brazil and Diversion of Portuguese Resources",
    "content": "<p><strong>The Brazil Diversion:</strong> Discovered by Pedro Álvares Cabral in 1500, Brazil initially remained secondary to the spice-rich Indian Ocean trade. However, in the late 16th and 17th centuries, the development of massive sugarcane plantations (the <em>Engenhos</em> system) and the Atlantic slave trade made Brazil highly profitable. Later, the discovery of gold in Minas Gerais in the late 1690s cemented Brazil's economic dominance.</p><p><strong>Demographic Limits:</strong> Portugal was a small nation with a total domestic population of barely 1 million in the 16th century. It suffered from severe demographic constraints and could not sustain two global empires simultaneously. Given the intense military challenges from the Dutch and English in Asia, the Portuguese Crown and merchant classes chose to divert their limited manpower, capital, and naval fleets to Brazil. The Atlantic route to Brazil was significantly shorter (2-3 months) and safer than the hazardous Cape Route to India (6-8 months), and South America offered vast, contiguous lands with far less military resistance than the powerful states of India.</p>"
  },
  {
    "title": "5. Internal Corruption, Administrative Decay, and Resurgence of Regional Powers",
    "content": "<p><strong>Internal Decay:</strong> The administration of the Estado da Índia suffered from systemic corruption. Portuguese governors, captains, and officials routinely engaged in <em>trato particular</em> (unauthorized private trade) for personal enrichment, bypassing the royal customs house and starving the Crown of revenues. The short three-year tenure of Viceroys encouraged quick plunder rather than long-term infrastructure investment. The Crown was forced to sell administrative and military offices to the highest bidders to cover debts.</p><p><strong>Resurgence of Regional Powers:</strong> Simultaneously, regional Indian powers grew stronger and pushed back against Portuguese territorial claims. In 1632, the Mughal Emperor Shah Jahan, angered by Portuguese piracy, slave raids, and refusal to pay imperial custom duties, ordered the governor Qasim Khan to capture the Portuguese trading post at Hugli in Bengal. In the Deccan, the Marathas launched campaigns to reclaim territories. In 1737-1739, Chimaji Appa, the brother of Peshwa Baji Rao I, led a successful siege of the heavily fortified city of Bassein (Vasai), stripping the Portuguese of their fertile Northern Province and restricting their presence to Goa, Daman, and Diu.</p>"
  }
]

hi_sections = [
  {
    "title": "1. प्रतिद्वंद्वी यूरोपीय शक्तियों का उदय (डच और अंग्रेजों का नौसैनिक वर्चस्व)",
    "content": "<p><strong>वित्तीय मॉडल:</strong> 1600 में ब्रिटिश ईस्ट इंडिया कंपनी (EIC) और 1602 में डच ईस्ट इंडिया कंपनी (VOC) की स्थापना ने एक बेहतर संयुक्त-पूंजी (joint-stock) निगम मॉडल पेश किया। पुर्तगाली क्राउन (शाही) नियंत्रित एकाधिकार के विपरीत, जो धीमा, अत्यधिक केंद्रीकृत और प्रशासनिक अक्षमता से ग्रस्त था, डच और ब्रिटिश कंपनियों ने आम शेयरधारकों से भारी मात्रा में पूंजी जुटाई। इसने व्यापारिक कार्यों को राज्य की राजनीति से अलग कर दिया, जोखिमों को साझा करने की अनुमति दी, और सैन्य संघर्षों के दौरान भी निरंतर धन की आपूर्ति सुनिश्चित की।</p><p><strong>नौसेना तकनीक:</strong> डच और अंग्रेजी बेड़े में महत्वपूर्ण तकनीकी लाभ थे। डचों ने <em>फ्लूट (Fluyt)</em> का निर्माण किया, जो एक अत्यधिक किफायती मालवाहक जहाज था, जिसमें व्यापक माल स्थान और सस्ता निर्माण शामिल था, जिसे बड़े माल की मात्रा को संभालने के लिए बहुत कम चालक दल (crew) की आवश्यकता होती थी। अंग्रेजों ने तेजी से चलने वाले, अधिक गतिशील <em>गैलियन (Galleons)</em> का निर्माण किया, जिनका निचला प्रोफ़ाइल था, जो तोपों के हमलों के प्रति कम संवेदनशील थे और जिनमें भारी, लंबी दूरी की नौसैनिक तोपें लगी थीं। इसके विपरीत, पुर्तगाली <em>कैरक (Carracks)</em> शीर्ष-भारी, धीमे और मुख्य रूप से युद्ध के बजाय माल परिवहन के लिए डिजाइन किए गए थे, जिससे वे दुश्मन के फुर्तीले युद्धपोतों के लिए आसान शिकार बन गए।</p>"
  },
  {
    "title": "2. धार्मिक असहिष्णुता, उत्पीड़न और गोवा का इनक्विजिशन (धर्माधिकरण)",
    "content": "<p><strong>इनक्विजिशन (धर्माधिकरण):</strong> जेसुइट मिशनरी फ्रांसिस जेवियर की याचिका पर 1560 में स्थापित, गोवा इनक्विजिशन ने पुर्तगाली शासन की व्यावहारिक और शुरुआती सहिष्णुता से एक कठोर बदलाव को चिह्नित किया। इनक्विजिशन का उद्देश्य पाखंड को दंडित करना और कैथोलिक कट्टरता को लागू करना था। इसने न केवल स्वदेशी निवासियों को बल्कि विशेष रूप से 'नए ईसाइयों' (यहूदी और हिंदू धर्म परिवर्तित लोग) को निशाना बनाया, जिन पर गुप्त रूप से अपने पूर्वजों के धर्म (Crypto-Jews और Crypto-Hindus) का अभ्यास करने का संदेह था।</p><p><strong>आर्थिक परिणाम:</strong> असहिष्णु नीतियों में हिंदू और बौद्ध मंदिरों का विनाश, गैर-ईसाई धार्मिक संस्कारों, विवाहों और त्योहारों पर प्रतिबंध, और स्थानीय कोंकणी भाषा का दमन (1684 में आधिकारिक उपयोग में प्रतिबंधित) शामिल था। इस संस्थागत असहिष्णुता ने स्थानीय आबादी को अलग-थलग कर दिया और स्थानीय गठबंधनों को नष्ट कर दिया। महत्वपूर्ण रूप से, इसने समृद्ध सारस्वत ब्राह्मण व्यापारियों, कुशल कारीगरों और कृषकों के पड़ोसी क्षेत्रों जैसे वेनगुर्ला (डचों के अधीन) और कनारा तट पर बड़े पैमाने पर पलायन को प्रेरित किया। पूंजी और श्रम के इस पलायन ने गोवा के कर आधार और स्थानीय व्यापार नेटवर्क को गंभीर रूप से नुकसान पहुंचाया।</p>"
  },
  {
    "title": "3. इबेरियन यूनियन (1580–1640) और पूर्वी व्यापार की स्पैनिश उपेक्षा",
    "content": "<p><strong>व्यक्तिगत संघ (Personal Union):</strong> 1578 में, युवा पुर्तगाली राजा सेबेस्टियन मोरक्को में एक विनाशकारी सैन्य अभियान (अलकासर क्विबीर का युद्ध) के दौरान मारे गए, जिससे कोई उत्तराधिकारी नहीं बचा। इसने एक उत्तराधिकार संकट को जन्म दिया, जिसके परिणामस्वरूप 1580 में स्पेन के राजा फिलिप द्वितीय द्वारा पुर्तगाल का विलय कर लिया गया, जिससे इबेरियन यूनियन का गठन हुआ। यद्यपि पुर्तगाल ने अपना प्रशासन बनाए रखा, लेकिन उसकी विदेश नीति स्पेनिश हैब्सबर्ग राजशाही के अधीन कर दी गई थी।</p><p><strong>साम्राज्यवादी उपेक्षा:</strong> इबेरियन यूनियन ने पुर्तगाल को स्पेन के वैश्विक संघर्षों में घसीट लिया, विशेष रूप से डच गणराज्य के खिलाफ अस्सी साल के युद्ध और एंग्लो-स्पैनिश युद्ध में। इसके परिणामस्वरूप, एशिया में पुर्तगाली जहाज और बस्तियां आक्रामक डच और अंग्रेजी नौसेनाओं के वैध लक्ष्य बन गए। इसके अलावा, स्पेनिश राजाओं ने अमेरिकी चांदी की खानों (पोटोसी) और यूरोपीय भूमि अभियानों को प्राथमिकता दी, जिससे लिस्बन के पूर्वी मसाले के व्यापार की उपेक्षा हुई। पुर्तगाली एस्टाडो दा इंडिया को नौसैनिक सुदृढ़ीकरण, पूंजी और जहाज निर्माण सामग्री की कमी का सामना करना पड़ा, जिससे उसकी समुद्री रक्षा प्रणाली का पतन हो गया और होर्मुज (1622) जैसे प्रमुख किलों को खोना पड़ा।</p>"
  },
  {
    "title": "4. ब्राजील की खोज और पुर्तगाली संसाधनों का विचलन",
    "content": "<p><strong>ब्राजील विचलन:</strong> 1500 में पेड्रो अल्वारेस कैब्राल द्वारा खोजा गया, ब्राजील शुरू में मसाले से समृद्ध हिंद महासागर के व्यापार की तुलना में गौण रहा। हालांकि, 16वीं सदी के अंत और 17वीं सदी में, विशाल चीनी बागानों (<em>Engenhos</em> प्रणाली) के विकास और अटलांटिक दास व्यापार ने ब्राजील को अत्यधिक लाभदायक बना दिया। बाद में, 1690 के दशक के अंत में मिनस गेरैस में सोने की खोज ने ब्राजील के आर्थिक प्रभुत्व को मजबूत कर दिया।</p><p><strong>जनसांख्यिकीय सीमाएं:</strong> पुर्तगाल 16वीं शताब्दी में बमुश्किल 10 लाख की कुल घरेलू आबादी वाला एक छोटा देश था। यह गंभीर जनसांख्यिकीय बाधाओं से पीड़ित था और एक साथ दो वैश्विक साम्राज्यों को बनाए नहीं रख सकता था। एशिया में डच और अंग्रेजों की ओर से तीव्र सैन्य चुनौतियों को देखते हुए, पुर्तगाली क्राउन और व्यापारी वर्गों ने अपनी सीमित जनशक्ति, पूंजी और नौसैनिक बेड़े को ब्राजील की ओर मोड़ने का फैसला किया। ब्राजील के लिए अटलांटिक मार्ग भारत के खतरनाक केप मार्ग (6-8 महीने) की तुलना में काफी छोटा (2-3 महीने) और सुरक्षित था, और दक्षिण अमेरिका ने भारत के शक्तिशाली राज्यों की तुलना में बहुत कम सैन्य प्रतिरोध के साथ विशाल भूमि की पेशकश की थी।</p>"
  },
  {
    "title": "5. आंतरिक भ्रष्टाचार, प्रशासनिक पतन और क्षेत्रीय शक्तियों का पुनरुत्थान",
    "content": "<p><strong>आन्तरिक गिरावट:</strong> एस्टाडो दा इंडिया का प्रशासन प्रणालीगत भ्रष्टाचार से ग्रस्त था। पुर्तगाली गवर्नर, कैप्टन और अधिकारी नियमित रूप से व्यक्तिगत संवर्धन के लिए <em>त्रातो पर्टिकुलर (trato particular)</em> (अनाधिकृत निजी व्यापार) में संलग्न रहते थे, जिससे शाही सीमा शुल्क गृह की उपेक्षा होती थी और क्राउन राजस्व से वंचित हो जाता था। वायसरायों के छोटे तीन साल के कार्यकाल ने दीर्घकालिक बुनियादी ढांचे के निवेश के बजाय त्वरित लूट को प्रोत्साहित किया। क्राउन को ऋण चुकाने के लिए उच्चतम बोलीदाताओं को प्रशासनिक और सैन्य पद बेचने के लिए मजबूर होना पड़ा।</p><p><strong>क्षेत्रीय शक्तियों का पुनरुत्थान:</strong> साथ ही, भारतीय क्षेत्रीय शक्तियां मजबूत हुईं और पुर्तगाली क्षेत्रीय दावों का विरोध किया। 1632 में, पुर्तगाली डकैती, गुलामी और शाही कर चुकाने से इनकार करने से नाराज मुगल सम्राट शाहजहां ने गवर्नर कासिम खान को बंगाल में हुगली के पुर्तगाली व्यापारिक केंद्र पर कब्जा करने का आदेश दिया। दक्कन में, मराठों ने क्षेत्रों पर पुनः दावा करने के लिए अभियान शुरू किया। 1737-1739 में, पेशवा बाजीराव प्रथम के भाई चिमाजी अप्पा ने वसई (बसीन) के किले की सफल घेराबंदी की, जिससे पुर्तगालियों से उनका उपजाऊ उत्तरी प्रांत छीन लिया गया और उनकी उपस्थिति गोवा, दमन और दीव तक सीमित रह गई।</p>"
  }
]

for idx, sec in enumerate(en_sections):
    en_data["deepDive"]["sections"].append({
        "title": sec["title"],
        "content": sec["content"],
        "masteryZone": []
    })

for idx, sec in enumerate(hi_sections):
    hi_data["deepDive"]["sections"].append({
        "title": sec["title"],
        "content": sec["content"],
        "masteryZone": []
    })

# Section 1 questions (already high quality and unique, tuple format conversion will be handled)
sec1_raw = [
    # 5 MCQ
    ("MCQ", "Which financial model gave the Dutch VOC and English EIC a distinct advantage over the Portuguese?", ["Joint-stock corporation with public investment", "Direct crown ownership and financing", "Feudal taxation of land revenues", "Barter trade systems"], 0, "The joint-stock model allowed the Dutch and English to raise massive capital and share risks, unlike the Portuguese crown monopoly.",
     "किस वित्तीय मॉडल ने डच वीओसी और अंग्रेजी ईआईसी को पुर्तगालियों पर एक स्पष्ट लाभ दिया?", ["सार्वजनिक निवेश के साथ संयुक्त-पूंजी निगम", "प्रत्यक्ष शाही स्वामित्व और वित्तपोषण", "भूमि राजस्व का सामंती कराधान", "वस्तु विनिमय प्रणाली"], 0, "संयुक्त-पूंजी मॉडल ने डच और अंग्रेजों को भारी पूंजी जुटाने और जोखिम साझा करने की अनुमति दी।"),
    
    ("MCQ", "What was the primary characteristic of the Dutch Fluyt ship design?", ["Cheap to build and operated by a small crew", "Heavily armored with multiple gun decks", "Built entirely of imported Indian teakwood", "Equipped with steam propulsion systems"], 0, "The Fluyt was designed as a low-cost, high-capacity cargo vessel operated by a small crew, reducing shipping rates.",
     "डच फ्लूट (Fluyt) जहाज डिजाइन की प्राथमिक विशेषता क्या थी?", ["निर्माण में सस्ता और एक छोटे चालक दल द्वारा संचालित", "एकाधिक बंदूक डेक के साथ भारी बख्तरबंद", "पूरी तरह से आयातित भारतीय सागौन की लकड़ी से निर्मित", "भाप प्रणोदन प्रणाली से लैस"], 0, "फ्लूट को एक कम लागत वाले, उच्च क्षमता वाले मालवाहक जहाज के रूप में डिजाइन किया गया था।"),

    ("MCQ", "In which battle did English Captain Thomas Best defeat a Portuguese fleet in 1612?", ["Battle of Swally Hole", "Battle of Diu", "Battle of Chaul", "Battle of Colachel"], 0, "The Battle of Swally Hole (1612) near Surat shattered the Portuguese reputation for naval supremacy in India.",
     "1612 में किस युद्ध में अंग्रेज कैप्टन थॉमस बेस्ट ने पुर्तगाली बेड़े को हराया था?", ["स्वाली होल का युद्ध", "दीव का युद्ध", "चोल का युद्ध", "कोलाचेल का युद्ध"], 0, "सूरत के पास स्वाली होल के युद्ध (1612) ने भारत में पुर्तगाली नौसैनिक वर्चस्व के मिथक को तोड़ दिया।"),

    ("MCQ", "Who governed the Dutch East India Company (VOC)?", ["Heeren XVII (Lords Seventeen)", "The Court of Directors", "The King of Spain", "The Council of India"], 0, "The Lords Seventeen (Heeren XVII) was the governing body of the Dutch VOC representing different chambers.",
     "डच ईस्ट इंडिया कंपनी (VOC) का शासन किसके द्वारा चलाया जाता था?", ["हेरेन XVII (Lords Seventeen)", "निदेशक मंडल (Court of Directors)", "स्पेन के राजा", "भारत परिषद"], 0, "लॉर्ड्स सत्रह (हेरेन XVII) डच वीओसी का शासी निकाय था जो विभिन्न मंडलों का प्रतिनिधित्व करता था।"),

    ("MCQ", "Which Portuguese stronghold in Southeast Asia fell to the Dutch in 1641 after a long siege?", ["Malacca", "Macau", "Goa", "Hormuz"], 0, "The capture of Malacca in 1641 severed the Portuguese trade route to the Spice Islands and the Far East.",
     "दक्षिण पूर्व एशिया में कौन सा पुर्तगाली गढ़ 1641 में एक लंबी घेराबंदी के बाद डचों के कब्जे में आ गया?", ["मलक्का", "मकाऊ", "गोवा", "होर्मुज"], 0, "1641 में मलक्का पर कब्जे ने स्पाइस आइलैंड्स के लिए पुर्तगाली व्यापार मार्ग को काट दिया।"),

    # 5 Multiple Correct MCQ
    ("Multiple Correct MCQ", "Which of the following were advantages of the English Galleon over Portuguese Carracks? (Select all that apply)", ["Lower profile in the water", "Heavier and faster broadside cannons", "Greater cargo capacity for agricultural goods", "Higher top-heavy castle decks"], [0, 1], "English galleons were lower, faster, and carried heavy broadside cannons, making them superior in combat.",
     "पुर्तगाली कैरैक (Carracks) की तुलना में अंग्रेजी गैलियन (Galleon) के क्या लाभ थे? (सभी लागू विकल्प चुनें)", ["पानी में निचला प्रोफाइल होना", "अधिक भारी और तेज गति से चलने वाली तोपें", "कृषि उत्पादों के लिए अधिक माल वहन क्षमता", "उच्च शीर्ष-भारी कैसल डेक"], [0, 1], "अंग्रेजी गैलियन निचले, तेज थे और भारी तोपों से लैस थे।"),

    ("Multiple Correct MCQ", "What structural weaknesses plagued the Portuguese Estado da Índia compared to the Dutch VOC? (Select all that apply)", ["Direct dependency on crown approvals", "Severe financial deficits and lack of public investment", "Frequent displacement of officials and short tenures", "Inability to recruit local Indian soldiers"], [0, 1, 2], "The Estado da India was heavily centralized under the Crown, lacked public shareholding, and suffered from high bureaucratic turnover.",
     "डच वीओसी की तुलना में पुर्तगाली एस्टाडो दा इंडिया में क्या संरचनात्मक कमजोरियां थीं? (सभी लागू विकल्प चुनें)", ["शाही मंजूरी पर प्रत्यक्ष निर्भरता", "गंभीर वित्तीय घाटा और सार्वजनिक निवेश की कमी", "अधिकारियों का बार-बार स्थानांतरण और छोटा कार्यकाल", "स्थानीय भारतीय सैनिकों की भर्ती करने में असमर्थता"], [0, 1, 2], "एस्टाडो दा इंडिया क्राउन के अधीन अत्यधिक केंद्रीकृत था, सार्वजनिक शेयरधारिता की कमी थी।"),

    ("Multiple Correct MCQ", "Which major locations were lost by the Portuguese to the Dutch in the 17th century? (Select all that apply)", ["Cochin (1663)", "Colombo (1656)", "Malacca (1641)", "Daman (1620)"], [0, 1, 2], "The Portuguese lost Cochin, Colombo, and Malacca to the Dutch, while Daman was retained.",
     "17वीं शताब्दी में पुर्तगालियों ने डचों के हाथों कौन से प्रमुख स्थान खो दिए थे? (सभी लागू विकल्प चुनें)", ["कोचीन (1663)", "कोलंबो (1656)", "मलक्का (1641)", "दमन (1620)"], [0, 1, 2], "पुर्तगाली डचों से कोचीन, कोलंबो और मलक्का हार गए थे।"),

    ("Multiple Correct MCQ", "Identify the factors that made the joint-stock company model highly resilient. (Select all that apply)", ["Limited liability for individual shareholders", "Pooling of capital from broad segments of society", "Complete insulation from all government regulations", "Continuous operations beyond the lifetimes of founders"], [0, 1, 3], "Joint-stock companies offered limited liability, broad capital pooling, and perpetual succession.",
     "उन कारकों की पहचान करें जिन्होंने संयुक्त-पूंजी कंपनी मॉडल को अत्यधिक लचीला बनाया। (सभी लागू विकल्प चुनें)", ["व्यक्तिगत शेयरधारकों के लिए सीमित दायित्व", "समाज के विस्तृत वर्गों से पूंजी जुटाना", "सभी सरकारी नियमों से पूर्ण मुक्ति", "संस्थापकों के जीवनकाल से परे निरंतर संचालन"], [0, 1, 3], "संयुक्त-पूंजी कंपनियों ने सीमित दायित्व, व्यापक पूंजी पूलिंग की पेशकश की।"),

    ("Multiple Correct MCQ", "Which measures did the English and Dutch take to bypass the Portuguese Cartaz system? (Select all that apply)", ["Escorting merchant vessels with armed warships", "Establishing direct factories at Surat and Batavia", "Purchasing Cartaz passes in bulk at discount rates", "Forming naval blockades around Goa"], [0, 1, 3], "They escorted their ships, set up alternative bases, and blockaded Goa rather than purchasing passes.",
     "पुर्तगाली कार्तज प्रणाली को दरकिनार करने के लिए अंग्रेजों और डचों ने क्या उपाय किए? (सभी लागू विकल्प चुनें)", ["सशस्त्र युद्धपोतों के साथ व्यापारिक जहाजों की सुरक्षा करना", "सूरत और बटाविया में सीधे कारखाने स्थापित करना", "डिस्काउंट दरों पर थोक में कार्तज पास खरीदना", "गोवा के चारों ओर नौसैनिक नाकेबंदी करना"], [0, 1, 3], "उन्होंने अपने जहाजों की रक्षा की, वैकल्पिक ठिकाने बनाए और गोवा की नाकेबंदी की।"),

    # 8 True/False
    ("True/False", "The English East India Company was established after the Dutch VOC.", "सत्य या असत्य: ब्रिटिश ईस्ट इंडिया कंपनी की स्थापना डच वीओसी के बाद हुई थी।", False,
     "The English EIC was established in 1600, whereas the Dutch VOC was founded in 1602.",
     "अंग्रेजी ईआईसी की स्थापना 1600 में हुई थी, जबकि डच वीओसी की स्थापना 1602 में हुई थी।"),

    ("True/False", "The Dutch Fluyt was designed specifically as an offensive warship to destroy coastal forts.", "सत्य या असत्य: डच फ्लूट को विशेष रूप से तटीय किलों को नष्ट करने के लिए एक युद्धपोत के रूप में डिजाइन किया गया था।", False,
     "The Fluyt was a low-cost merchant cargo ship, designed to maximize carrying space and minimize crew size.",
     "फ्लूट एक कम लागत वाला मालवाहक जहाज था, जिसे माल ढोने की जगह बढ़ाने के लिए डिजाइन किया गया था।"),

    ("True/False", "The Battle of Swally Hole took place near Surat on the west coast of India.", "सत्य या असत्य: स्वाली होल का युद्ध भारत के पश्चिमी तट पर सूरत के पास हुआ था।", True,
     "It was fought off the coast of Surat in November 1612 and led to English trade concessions from Jahangir.",
     "यह नवंबर 1612 में सूरत के तट पर लड़ा गया था और इसके बाद जहांगीर से अंग्रेजों को व्यापारिक रियायतें मिलीं।"),

    ("True/False", "The governing body of the Dutch VOC was called the Court of Directors.", "सत्य या असत्य: डच वीओसी के शासी निकाय को निदेशक मंडल (Court of Directors) कहा जाता था।", False,
     "The Dutch VOC was governed by the Heeren XVII, while the English EIC was governed by the Court of Directors.",
     "डच वीओसी पर हेरेन XVII का शासन था, जबकि अंग्रेजी ईआईसी पर कोर्ट ऑफ डायरेक्टर्स का शासन था।"),

    ("True/False", "Portuguese carracks were generally faster and more maneuverable than English galleons.", "सत्य या असत्य: पुर्तगाली कैरैक आम तौर पर अंग्रेजी गैलियन की तुलना में तेज और अधिक गतिशील थे।", False,
     "Carracks were bulky, top-heavy cargo carriers, making them slow and vulnerable to the more agile galleons.",
     "कैरैक भारी मालवाहक जहाज थे, जिससे वे धीमे और फुर्तीले गैलियन के सामने कमजोर हो जाते थे।"),

    ("True/False", "The Dutch successfully blockaded the harbor of Goa multiple times in the 17th century.", "सत्य या असत्य: डचों ने 17वीं शताब्दी में कई बार गोवा के बंदरगाह की सफलतापूर्वक नाकेबंदी की थी।", True,
     "The Dutch blockaded Goa during the shipping season, preventing the Portuguese from sending spices to Lisbon.",
     "डचों ने जहाजों के चलने के मौसम में गोवा की नाकेबंदी की, जिससे पुर्तगाली लिस्बन को मसाले नहीं भेज सके।"),

    ("True/False", "The Portuguese crown monopoly model encouraged active private merchant competition in Lisbon.", "सत्य या असत्य: पुर्तगाली शाही एकाधिकार मॉडल ने लिस्बन में सक्रिय निजी व्यापारिक प्रतिस्पर्धा को प्रोत्साहित किया।", False,
     "The crown monopoly restricted trade to the royal house, stifling private entrepreneurial initiative.",
     "शाही एकाधिकार ने व्यापार को शाही घराने तक सीमित कर दिया, जिससे निजी उद्यमशीलता दब गई।"),

    ("True/False", "The English EIC established its first permanent factory in Surat after the Battle of Swally.", "सत्य या असत्य: स्वाली के युद्ध के बाद अंग्रेजी ईआईसी ने सूरत में अपना पहला कारखाना स्थापित किया।", True,
     "Following the victory, Emperor Jahangir issued a farman permitting the English to establish a factory at Surat in 1613.",
     "जीत के बाद, सम्राट जहांगीर ने 1613 में अंग्रेजों को सूरत में कारखाना स्थापित करने की अनुमति दी।"),

    # 8 Fill in the Blank
    ("Fill in the Blank", "The Dutch East India Company was founded in the year __________.", "डच ईस्ट इंडिया कंपनी की स्थापना __________ वर्ष में हुई थी।", "1602",
     "The VOC was chartered in 1602 to consolidate Dutch spice trade efforts.",
     "डच मसाला व्यापार के प्रयासों को मजबूत करने के लिए 1602 में VOC को चार्टर दिया गया था।"),

    ("Fill in the Blank", "The English merchant company received its royal charter from Queen __________ I.", "अंग्रेजी व्यापारिक कंपनी को अपना शाही चार्टर रानी __________ प्रथम से प्राप्त हुआ था।", "Elizabeth",
     "Queen Elizabeth I granted the royal charter on December 31, 1600.",
     "रानी एलिजाबेथ प्रथम ने 31 दिसंबर, 1600 को शाही चार्टर प्रदान किया था।"),

    ("Fill in the Blank", "The Battle of Swally was fought in the year __________ CE.", "स्वाली का युद्ध __________ ईस्वी में लड़ा गया था।", "1612",
     "The battle was fought in late 1612 and established English influence in India.",
     "यह युद्ध 1612 के अंत में लड़ा गया था और इसने भारत में अंग्रेजी प्रभाव स्थापित किया।"),

    ("Fill in the Blank", "The administrative board of the Dutch VOC was known as the Heeren __________.", "डच वीओसी के प्रशासनिक बोर्ड को हेरेन __________ के रूप में जाना जाता था।", "XVII",
     "The Heeren XVII (Lords Seventeen) represented the different regional chambers of the VOC.",
     "हेरेन XVII (लॉर्ड्स सत्रह) वीओसी के विभिन्न क्षेत्रीय मंडलों का प्रतिनिधित्व करते थे।"),

    ("Fill in the Blank", "The specialized Dutch merchant vessel designed for cheap cargo transport was the __________.", "सस्ते माल परिवहन के लिए डिजाइन किया गया विशिष्ट डच मालवाहक जहाज __________ था।", "Fluyt",
     "The Fluyt utilized cheap construction and small crews to lower transport costs.",
     "फ्लूट ने परिवहन लागत को कम करने के लिए सस्ते निर्माण और छोटे चालक दल का उपयोग किया।"),

    ("Fill in the Blank", "Thomas __________ was the English captain who won the Battle of Swally.", "थॉमस __________ वह अंग्रेज कैप्टन था जिसने स्वाली का युद्ध जीता था।", "Best",
     "Captain Thomas Best commanded the Red Dragon and Osiander to victory.",
     "कैप्टन थॉमस बेस्ट ने रेड ड्रैगन और ओसिएंडर जहाजों का नेतृत्व कर जीत हासिल की थी।"),

    ("Fill in the Blank", "The Dutch captured the strategic port of Cochin in the year __________ CE.", "डचों ने __________ ईस्वी में कोचीन के रणनीतिक बंदरगाह पर कब्जा कर लिया था।", "1663",
     "Cochin fell to the Dutch in January 1663, ending Portuguese influence on the Malabar coast.",
     "कोचीन जनवरी 1663 में डचों के अधीन हो गया, जिससे मालाबार तट पर पुर्तगाली प्रभाव समाप्त हो गया।"),

    ("Fill in the Blank", "The English warship design characterized by speed and heavy broadside guns was the __________.", "गति और भारी तोपों की विशेषता वाला अंग्रेजी युद्धपोत डिजाइन __________ था।", "Galleon",
     "The Galleon was lower and faster, proving highly effective against bulky carracks.",
     "गैलियन निचला और तेज था, जो भारी कैरैक के खिलाफ यातनापूर्ण सिद्ध हुआ।"),

    # 3 Match the Following
    ("Match the Following", "Match the ship types with their primary nations and attributes:",
     "मिलान करें जहाजों के प्रकार को उनके देशों और विशेषताओं के साथ:",
     [{"left": "Fluyt"}, {"left": "Galleon"}, {"left": "Carrack"}],
     [{"left": "फ्लूट (Fluyt)"}, {"left": "गैलियन (Galleon)"}, {"left": "कैरक (Carrack)"}],
     [{"val": "0", "text": "Dutch cargo carrier with low crew requirement"}, {"val": "1", "text": "English fast warship with broadside guns"}, {"val": "2", "text": "Bulky Portuguese vessel built for transport"}],
     [{"val": "0", "text": "कम चालक दल की आवश्यकता वाला डच मालवाहक जहाज"}, {"val": "1", "text": "तोपों से लैस अंग्रेजी तेज गति का युद्धपोत"}, {"val": "2", "text": "परिवहन के लिए बनाया गया भारी पुर्तगाली जहाज"}],
     "Matched correctly: Fluyt (Dutch), Galleon (English), Carrack (Portuguese).",
     "सही मिलान: फ्लूट (डच), गैलियन (अंग्रेज), कैरक (पुर्तगाली)।"),

    ("Match the Following", "Match the European companies with their governing bodies:",
     "मिलान करें यूरोपीय कंपनियों को उनके शासी निकायों के साथ:",
     [{"left": "Dutch VOC"}, {"left": "English EIC"}, {"left": "Estado da Índia"}],
     [{"left": "डच VOC"}, {"left": "अंग्रेजी EIC"}, {"left": "एस्टाडो दा इंडिया"}],
     [{"val": "0", "text": "Heeren XVII (Lords Seventeen)"}, {"val": "1", "text": "Court of Directors in London"}, {"val": "2", "text": "Crown and Overseas Council in Lisbon"}],
     [{"val": "0", "text": "हेरेन XVII (लॉर्ड्स सत्रह)"}, {"val": "1", "text": "लंदन में कोर्ट ऑफ डायरेक्टर्स"}, {"val": "2", "text": "लिस्बन में क्राउन और ओवरसीज काउंसिल"}],
     "Matched correctly: VOC (Heeren XVII), EIC (Court of Directors), Estado (Crown Council).",
     "सही मिलान: VOC (हेरेन XVII), EIC (कोर्ट ऑफ डायरेक्टर्स), एस्टाडो (क्राउन काउंसिल)।"),

    ("Match the Following", "Match the battles and conquests with their respective years:",
     "मिलान करें युद्धों और जीतों को उनके संबंधित वर्षों के साथ:",
     [{"left": "Battle of Swally"}, {"left": "Fall of Malacca to Dutch"}, {"left": "Fall of Cochin to Dutch"}],
     [{"left": "स्वाली का युद्ध"}, {"left": "डचों द्वारा मलक्का विजय"}, {"left": "डचों द्वारा कोचीन विजय"}],
     [{"val": "0", "text": "1612 CE"}, {"val": "1", "text": "1641 CE"}, {"val": "2", "text": "1663 CE"}],
     [{"val": "0", "text": "1612 ईस्वी"}, {"val": "1", "text": "1641 ईस्वी"}, {"val": "2", "text": "1663 ईस्वी"}],
     "Matched correctly: Swally (1612), Malacca (1641), Cochin (1663).",
     "सही मिलान: स्वाली (1612), मलक्का (1641), कोचीन (1663)।"),

    # 8 One-Liner
    ("One-Liner", "Which English Captain won the Battle of Swally in 1612?", "1612 में स्वाली का युद्ध किस अंग्रेज कैप्टन ने जीता था?",
     "Captain Thomas Best.",
     "कैप्टन थॉमस बेस्ट।"),

    ("One-Liner", "What was the governing body of the Dutch East India Company called?", "डच ईस्ट इंडिया कंपनी के शासी निकाय को क्या कहा जाता था?",
     "The Heeren XVII (Lords Seventeen).",
     "हेरेन XVII (लॉर्ड्स सत्रह)।"),

    ("One-Liner", "Why was the Dutch Fluyt ship highly economical?", "डच फ्लूट जहाज अत्यधिक किफायती क्यों था?",
     "It maximized cargo space and required a very small crew to operate, reducing operational costs.",
     "इसमें माल रखने की जगह अधिक थी और इसे चलाने के लिए बहुत कम चालक दल की आवश्यकता थी।"),

    ("One-Liner", "In which year did the Dutch capture Portuguese Malacca?", "डचों ने पुर्तगाली मलक्का पर किस वर्ष कब्जा किया था?",
     "In 1641 CE.",
     "1641 ईस्वी में।"),

    ("One-Liner", "What was the primary difference in capital mobilization between the Portuguese and British companies?", "पुर्तगाली और ब्रिटिश कंपनियों के बीच पूंजी जुटाने में प्राथमिक अंतर क्या था?",
     "The British used a public joint-stock model, whereas the Portuguese relied on direct Crown monopoly funding.",
     "अंग्रेजों ने सार्वजनिक संयुक्त-पूंजी मॉडल का उपयोग किया, जबकि पुर्तगाली शाही वित्तपोषण पर निर्भर थे।"),

    ("One-Liner", "Which Portuguese stronghold in Sri Lanka was lost to the Dutch in 1656?", "श्रीलंका में कौन सा पुर्तगाली गढ़ 1656 में डचों के हाथों खो गया था?",
     "Colombo.",
     "कोलंबो।"),

    ("One-Liner", "Where did the English EIC set up its first factory in western India after 1612?", "1612 के बाद अंग्रेजी ईआईसी ने पश्चिमी भारत में अपना पहला कारखाना कहाँ स्थापित किया था?",
     "Surat.",
     "सूरत।"),

    ("One-Liner", "What type of guns gave English ships an advantage over bulky Portuguese carracks?", "अंग्रेजी जहाजों को पुर्तगाली कैरैक पर बढ़त दिलाने वाली किस प्रकार की तोपें थीं?",
     "Long-range broadside naval guns.",
     "लंबी दूरी की नौसैनिक तोपें (broadside guns)।"),

    # 8 Assertion-Reason
    ("Assertion-Reason", "Assertion (A): The Dutch VOC was able to lower shipping freight rates below those of the Portuguese.\nReason (R): The Dutch Fluyt ship was built cheaply and designed to be operated by a very small crew. (Variant 1)",
     "अभिकथन (A): डच वीओसी अपनी नौवहन माल ढुलाई दरों को पुर्तगालियों की तुलना में कम करने में सक्षम था।\nकारण (R): डच फ्लूट जहाज सस्ते में बनाया गया था और इसे बहुत कम चालक दल द्वारा संचालित करने के लिए डिजाइन किया गया था। (प्रकार 1)",
     0, "Both A and R are true, and R is the correct explanation of A.",
     "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है।"),

    ("Assertion-Reason", "Assertion (A): The Battle of Swally (1612) shattered the myth of Portuguese naval supremacy.\nReason (R): The Portuguese fleet was completely destroyed by a joint Mughal-English land army. (Variant 2)",
     "अभिकथन (A): स्वाली के युद्ध (1612) ने पुर्तगाली नौसैनिक वर्चस्व के मिथक को तोड़ दिया।\nकारण (R): पुर्तगाली बेड़े को एक संयुक्त मुगल-अंग्रेजी थल सेना द्वारा पूरी तरह से नष्ट कर दिया गया था। (प्रकार 2)",
     2, "A is true but R is false because the battle was purely naval and fought between English EIC and Portuguese ships.",
     "A सही है लेकिन R गलत है क्योंकि यह युद्ध पूरी तरह से नौसैनिक था और अंग्रेजी EIC और पुर्तगाली जहाजों के बीच लड़ा गया था।"),

    ("Assertion-Reason", "Assertion (A): The English EIC had greater financial flexibility than the Portuguese Estado da Índia.\nReason (R): The English EIC was structured as a joint-stock company backed by merchant capital, while the Portuguese trade was a Crown monopoly. (Variant 3)",
     "अभिकथन (A): अंग्रेजी ईआईसी के पास पुर्तगाली एस्टाडो दा इंडिया की तुलना में अधिक वित्तीय लचीलापन था।\nकारण (R): अंग्रेजी ईआईसी को व्यापारी पूंजी द्वारा समर्थित एक संयुक्त-पूंजी कंपनी के रूप में संरचित किया गया था, जबकि पुर्तगाली व्यापार एक शाही एकाधिकार था। (प्रकार 3)",
     0, "Both A and R are true, and R is the correct explanation of A.",
     "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है।"),

    ("Assertion-Reason", "Assertion (A): The Dutch VOC established its headquarters at Batavia (Jakarta).\nReason (R): They wanted to secure a centralized hub to coordinate their spice monopoly in Southeast Asia. (Variant 4)",
     "अभिकथन (A): डच वीओसी ने अपना मुख्यालय बटाविया (जकार्ता) में स्थापित किया।\nकारण (R): वे दक्षिण पूर्व एशिया में अपने मसाला एकाधिकार के समन्वय के लिए एक केंद्रीकृत केंद्र हासिल करना चाहते थे। (प्रकार 4)",
     0, "Both A and R are true, and R is the correct explanation of A.",
     "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है।"),

    ("Assertion-Reason", "Assertion (A): Portuguese carracks were highly effective in pursuing fast enemy ships.\nReason (R): Carracks were heavy, top-heavy vessels built primarily to maximize cargo carrying capacity rather than speed. (Variant 5)",
     "अभिकथन (A): पुर्तगाली कैरैक तेज गति वाले दुश्मन जहाजों का पीछा करने में अत्यधिक प्रभावी थे।\nकारण (R): कैरैक भारी, शीर्ष-भारी जहाज थे जो मुख्य रूप से गति के बजाय माल ले जाने की क्षमता बढ़ाने के लिए बनाए गए थे। (प्रकार 5)",
     3, "A is false but R is true, as carracks were slow and clumsy in combat.",
     "A गलत है लेकिन R सही है, क्योंकि कैरैक धीमे थे और युद्ध में गतिहीन साबित हुए।"),

    ("Assertion-Reason", "Assertion (A): The English EIC was a department of the British Government in 1600.\nReason (R): The Crown had no financial interest or shareholding in the company's early voyages. (Variant 6)",
     "अभिकथन (A): अंग्रेजी ईआईसी 1600 में ब्रिटिश सरकार का एक विभाग था।\nकारण (R): कंपनी की शुरुआती यात्राओं में क्राउन की कोई वित्तीय रुचि या हिस्सेदारी नहीं थी। (प्रकार 6)",
     3, "A is false because EIC was a private joint-stock corporation, while R is true.",
     "A गलत है क्योंकि EIC एक निजी संयुक्त-पूंजी निगम था, जबकि R सही है।"),

    ("Assertion-Reason", "Assertion (A): The Portuguese lost control over Malacca in 1641.\nReason (R): The Dutch VOC maintained a long blockade and partnered with the Sultan of Johor to capture the fort. (Variant 7)",
     "अभिकथन (A): पुर्तगालियों ने 1641 में मलक्का पर नियंत्रण खो दिया।\nकारण (R): डच वीओसी ने एक लंबी नाकेबंदी बनाए रखी और किले पर कब्जा करने के लिए जोहोर के सुल्तान के साथ भागीदारी की। (प्रकार 7)",
     0, "Both A and R are true, and R is the correct explanation of A.",
     "A और R दोनों सही हैं, और R, A की सही व्याख्या करता है।"),

    ("Assertion-Reason", "Assertion (A): The Portuguese Cartaz system remained completely unchallenged until the 19th century.\nReason (R): The English and Dutch routinely escorted their merchant fleets and engaged in naval warfare against Portuguese patrol vessels. (Variant 8)",
     "अभिकथन (A): पुर्तगाली कार्तज प्रणाली 19वीं शताब्दी तक पूरी तरह से निर्विवाद रही।\nकारण (R): अंग्रेज और डच नियमित रूप से अपने व्यापारिक बेड़े की रक्षा करते थे और पुर्तगाली गश्ती जहाजों के खिलाफ नौसैनिक युद्ध में शामिल होते थे। (प्रकार 8)",
     3, "A is false because the Cartaz was broken in the 17th century, while R is true.",
     "A गलत है क्योंकि कार्तज प्रणाली 17वीं सदी में टूट गई थी, जबकि R सही है।"),

    # 5 Statement-Based
    ("Statement-Based", "Consider the following statements regarding the Battle of Swally Hole:\n1. It was won by English Captain Thomas Best in 1612.\n2. It convinced the Mughal Emperor Jahangir to grant trading rights to the English.\nWhich of the statements given above is/are correct?",
     "स्वाली होल के युद्ध के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसे 1612 में अंग्रेज कैप्टन थॉमस बेस्ट ने जीता था।\n2. इसने मुगल सम्राट जहांगीर को अंग्रेजों को व्यापारिक अधिकार देने के लिए आश्वस्त किया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
     ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], 2,
     "Both statements are correct. The victory impressed the Mughals and led to a royal farman in 1613.",
     "दोनों कथन सही हैं। जीत ने मुगलों को प्रभावित किया और 1613 में एक शाही फरमान जारी हुआ।"),

    ("Statement-Based", "Consider the following statements regarding early European trade companies:\n1. The Dutch VOC was the first company to offer public shares to raise capital.\n2. The Portuguese Estado da Índia was funded primarily by public equity markets in Lisbon.\nWhich of the statements given above is/are correct?",
     "प्रारंभिक यूरोपीय व्यापार कंपनियों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. डच VOC पूंजी जुटाने के लिए सार्वजनिक शेयर पेश करने वाली पहली कंपनी थी।\n2. पुर्तगाली एस्टाडो दा इंडिया को मुख्य रूप से लिस्बन में सार्वजनिक शेयर बाजारों द्वारा वित्तपोषित किया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
     ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], 0,
     "Statement 1 is correct. Statement 2 is incorrect because the Estado was a crown-controlled monopoly.",
     "कथन 1 सही है। कथन 2 गलत है क्योंकि एस्टाडो दा इंडिया एक शाही एकाधिकार था।"),

    ("Statement-Based", "Consider the following statements regarding Dutch naval actions in India:\n1. The Dutch successfully captured Cochin from the Portuguese in 1663.\n2. The Dutch failed to capture Colombo, leaving it under Portuguese control.\nWhich of the statements given above is/are correct?",
     "भारत में डच नौसैनिक कार्रवाइयों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. डचों ने 1663 में पुर्तगालियों से कोचीन को सफलतापूर्वक छीन लिया।\n2. डच कोलंबो पर कब्जा करने में विफल रहे, जिससे यह पुर्तगाली नियंत्रण में रह गया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
     ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], 0,
     "Statement 1 is correct. Statement 2 is incorrect because Colombo was captured by the Dutch in 1656.",
     "कथन 1 सही है। कथन 2 गलत है क्योंकि डचों ने 1656 में कोलंबो पर कब्जा कर लिया था।"),

    ("Statement-Based", "Consider the following statements regarding ship designs:\n1. The Dutch Fluyt carried heavy guns on upper decks for naval protection.\n2. English Galleons were lower, faster, and more maneuverable than Portuguese Carracks.\nWhich of the statements given above is/are correct?",
     "जहाज डिजाइनों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. डच फ्लूट नौसैनिक सुरक्षा के लिए ऊपरी डेक पर भारी तोपें ले जाता था।\n2. अंग्रेजी गैलियन पुर्तगाली कैरैक की तुलना में निचले, तेज और अधिक गतिशील थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
     ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], 1,
     "Statement 1 is incorrect because the Fluyt was lightly armed to maximize cargo. Statement 2 is correct.",
     "कथन 1 गलत है क्योंकि फ्लूट माल रखने की जगह बढ़ाने के लिए हल्का बख्तरबंद था। कथन 2 सही है।"),

    ("Statement-Based", "Consider the following statements regarding Portuguese trade administration:\n1. The Cartaz was a fee-based passport that all merchant ships in the Indian Ocean were forced to buy.\n2. The Portuguese used the Cartaz to extract duties from rival local Indian merchants.\nWhich of the statements given above is/are correct?",
     "पुर्तगाली व्यापार प्रशासन के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कार्तज एक सशुल्क पासपोर्ट था जिसे हिंद महासागर के सभी जहाजों को खरीदने के लिए मजबूर किया जाता था।\n2. पुर्तगाली भारतीय व्यापारियों से शुल्क वसूलने के लिए कार्तज का उपयोग करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
     ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"], 2,
     "Both statements are correct. The Cartaz was an effective economic extraction tool.",
     "दोनों कथन सही हैं। कार्तज एक प्रभावी आर्थिक दोहन उपकरण था।"),

    # 12 Open
    ("Why", "Why did the joint-stock model of the Dutch VOC give it a financial advantage over the Portuguese Crown monopoly?",
     "डच वीओसी का संयुक्त-पूंजी (joint-stock) मॉडल पुर्तगाली शाही एकाधिकार की तुलना में वित्तीय रूप से क्यों बेहतर था?",
     "The joint-stock model allowed the Dutch VOC to mobilize huge capital from public shareholders, separating business operations from state finances. The Portuguese Crown monopoly, by contrast, suffered from chronic deficits, political instability in Lisbon, and rigid bureaucratic control.",
     "संयुक्त-पूंजी मॉडल ने डच वीओसी को सार्वजनिक शेयरधारकों से बड़ी मात्रा में पूंजी जुटाने की अनुमति दी, जिससे व्यापारिक कार्य सरकारी खजाने से अलग रहे। इसके विपरीत, पुर्तगाली शाही एकाधिकार वित्तीय कमी और राजनीतिक अस्थिरता से ग्रस्त था।"),

    ("Why", "Why did English naval technology outperform Portuguese naval technology in the 17th century?",
     "17वीं शताब्दी में अंग्रेजी नौसैनिक तकनीक पुर्तगाली नौसैनिक तकनीक से क्यों बेहतर साबित हुई?",
     "English galleons were designed with a lower silhouette, making them faster and less vulnerable to broadsides. They carried long-range broadside artillery, whereas Portuguese carracks were heavy, top-heavy, and built primarily for cargo capacity rather than speed and combat.",
     "अंग्रेजी गैलियन का निचला प्रोफाइल था, जिससे वे तेज थे और तोपों के हमले से बचे रहे। वे लंबी दूरी की तोपों से लैस थे, जबकि पुर्तगाली कैरैक भारी, शीर्ष-भारी थे और केवल माल ढुलाई के लिए उपयुक्त थे।"),

    ("Why", "Why did the Mughal Empire shift its patronage toward the English EIC after 1612?",
     "मुगल साम्राज्य ने 1612 के बाद अपना संरक्षण अंग्रेजी ईआईसी की ओर क्यों स्थानांतरित कर दिया?",
     "The English victory at the Battle of Swally Hole (1612) demonstrated their superior naval strength, shattering the myth of Portuguese invincibility. Emperor Jahangir recognized that the English could protect Mughal shipping from Portuguese piracy.",
     "स्वाली होल के युद्ध (1612) में अंग्रेजी जीत ने उनकी नौसैनिक ताकत का प्रदर्शन किया, जिससे पुर्तगाली अजेयता का मिथक टूट गया। सम्राट जहांगीर ने महसूस किया कि अंग्रेज पुर्तगाली डकैती से मुगलों के जहाजों की रक्षा कर सकते हैं।"),

    ("How", "How did the Dutch VOC systematically dismantle the Portuguese spice trade monopoly in the East?",
     "डच वीओसी ने पूर्व में पुर्तगाली मसाले के व्यापार के एकाधिकार को व्यवस्थित रूप से कैसे समाप्त किया?",
     "The Dutch captured key Portuguese choke points like Malacca (1641), Cochin (1663), and Colombo (1656). They established alternative trade networks at Batavia and used naval blockades around Goa during the shipping season to disrupt exports.",
     "डचों ने मलक्का (1641), कोचीन (1663) और कोलंबो (1656) जैसे प्रमुख पुर्तगाली चोक पॉइंट्स पर कब्जा कर लिया। उन्होंने बटाविया में वैकल्पिक व्यापार नेटवर्क स्थापित किया और गोवा की नाकेबंदी की।"),

    ("How", "How did the Battle of Swally Hole impact the geopolitical balance of power on India's west coast?",
     "स्वाली होल के युद्ध ने भारत के पश्चिमी तट पर भू-राजनीतिक शक्ति संतुलन को कैसे प्रभावित किया?",
     "The battle marked the entry of the English EIC into Indian politics. It forced the Mughals to permit the first English factory at Surat in 1613 and began the long decline of Portuguese naval hegemony in the Arabian Sea.",
     "इस युद्ध ने भारतीय राजनीति में अंग्रेजी ईआईसी के प्रवेश को चिह्नित किया। इसने मुगलों को 1613 में सूरत में पहला अंग्रेजी कारखाना खोलने की अनुमति देने के लिए मजबूर किया और पुर्तगाली वर्चस्व का अंत शुरू हुआ।"),

    ("How", "How did the administrative flexibility of the English EIC compare to the rigid bureaucracy of the Portuguese Estado da Índia?",
     "अंग्रेजी ईआईसी के प्रशासनिक लचीलेपन की तुलना पुर्तगाली एस्टाडो दा इंडिया की नौकरशाही से कैसे की जा सकती है?",
     "The EIC was managed by a professional Court of Directors in London answerable to shareholders, allowing rapid decisions based on market changes. The Estado da India required direct approvals from the Lisbon crown, which took months due to distance.",
     "ईआईसी का प्रबंधन लंदन में पेशेवरों के एक बोर्ड द्वारा किया जाता था जो शेयरधारकों के प्रति जवाबदेह थे। इसके विपरीत एस्टाडो दा इंडिया को लिस्बन क्राउन से सीधे अनुमोदन की आवश्यकता होती थी, जिसमें महीनों लगते थे।"),

    ("Case Study", "Case Study: The Dutch Siege of Malacca (1641) and its military implications.",
     "केस स्टडी: डचों द्वारा मलक्का की घेराबंदी (1641) और इसके सैन्य निहितार्थ।",
     "The Dutch blockaded Malacca for over five months, cooperating with the local Sultan of Johor. This case study demonstrates the transition of spice routes control from the Portuguese to the Dutch VOC, illustrating the importance of regional alliances and economic endurance.",
     "डचों ने जोहोर के सुल्तान के साथ मिलकर पांच महीने से अधिक समय तक मलक्का की नाकेबंदी की। यह केस स्टडी पुर्तगालियों से डच वीओसी के हाथ में मसाले के व्यापार के नियंत्रण के हस्तांतरण को दर्शाती है।"),

    ("Case Study", "Case Study: The Battle of Swally (1612) and its tactical naval maneuvers.",
     "केस स्टडी: स्वाली का युद्ध (1612) और उसकी रणनीतिक नौसैनिक चालें।",
     "English Captain Thomas Best utilized the shallow waters of Swally Hole near Surat to outmaneuver heavy Portuguese galleons. This study shows how maneuverability and superior artillery placement overcame larger fleets.",
     "अंग्रेज कैप्टन थॉमस बेस्ट ने भारी पुर्तगाली जहाजों को हराने के लिए सूरत के पास स्वाली होल के उथले पानी का उपयोग किया। यह दर्शाता है कि कैसे गतिशीलता और बेहतर तोपखाने ने बड़े जहाजों को हराया।"),

    ("Case Study", "Case Study: The Dutch Blockades of Goa and their economic toll on Portuguese trade.",
     "केस स्टडी: गोवा का डच घेराव और पुर्तगाली व्यापार पर इसका आर्थिक प्रभाव।",
     "Between 1636 and 1644, the Dutch VOC blockaded Goa's harbor annually during the sailing season. This case study shows how economic starvation via maritime blockade could weaken an empire without direct land assaults.",
     "1636 और 1644 के बीच, डच वीओसी ने नौकायन के मौसम के दौरान सालाना गोवा के बंदरगाह की नाकेबंदी की। यह दर्शाता है कि कैसे नौसैनिक नाकेबंदी ने बिना थल सेना के भी पुर्तगाली व्यापारिक रीढ़ को कमजोर कर दिया।"),

    ("Teach the Concept", "Teach the Concept: Joint-Stock Company vs. Crown Monopoly.",
     "अवधारणा समझाएं: संयुक्त-पूंजी कंपनी (Joint-Stock Company) बनाम शाही एकाधिकार (Crown Monopoly)।",
     "Explain the differences in funding: joint-stock companies pooled capital from public investors with limited liability, spreading risk and ensuring continuous funds. A crown monopoly relied entirely on the state budget, which suffered from deficits and political changes.",
     "फंडिंग में अंतर समझाएं: संयुक्त-पूंजी कंपनियों ने सीमित दायित्व के साथ सार्वजनिक निवेशकों से पूंजी जुटाई, जिससे जोखिम कम हुआ। शाही एकाधिकार पूरी तरह से राज्य के बजट पर निर्भर था, जो घाटे से ग्रस्त रहता था।"),

    ("Teach the Concept", "Teach the Concept: Broadside Naval Gunnery and Ship design evolution.",
     "अवधारणा समझाएं: ब्रॉडसाइड नौसैनिक तोपखाने (Broadside Naval Gunnery) और जहाज डिजाइन का विकास।",
     "Explain how the shift from troop transport ships (like Carracks) to dedicated artillery platforms (like Galleons) altered naval warfare, emphasizing broadside firing capacity, ship profile height, and speed.",
     "समझाएं कि कैसे सेना के परिवहन जहाजों (जैसे कैरक) से समर्पित तोपखाने प्लेटफार्मों (जैसे गैलियन) में बदलाव ने नौसैनिक युद्ध को बदल दिया, जिसमें गति और गोलाबारी क्षमता को प्राथमिकता दी गई।"),

    ("Teach the Concept", "Teach the Concept: The Cartaz System and its challenging by rival European mercantilists.",
     "अवधारणा समझाएं: कार्तज प्रणाली और प्रतिद्वंद्वी यूरोपीय व्यापारियों द्वारा इसे दी गई चुनौती।",
     "Explain the Portuguese protectionist license system (Cartaz) and show how the arrival of armed Dutch and English fleets, which refused to pay these fees, systematically undermined this primary source of revenue.",
     "पुर्तगाली सुरक्षात्मक लाइसेंस प्रणाली (कार्तज) को समझाएं और दिखाएं कि कैसे सशस्त्र डच और अंग्रेजी बेड़ों के आगमन ने, जिन्होंने शुल्क देने से इनकार कर दिया था, इस राजस्व के मुख्य स्रोत को कमजोर कर दिया।")
]

# Standard converter for Section 1 tuple-based questions
def convert_sec1_question(q_tuple, lang="en"):
    qtype = q_tuple[0]
    res = {"type": qtype}
    if qtype in ["MCQ", "Multiple Correct MCQ"]:
        if lang == "en":
            res["q"] = q_tuple[1]
            res["opts"] = q_tuple[2]
            res["ans"] = q_tuple[3]
            res["sol"] = q_tuple[4]
        else:
            res["q"] = q_tuple[5]
            res["opts"] = q_tuple[6]
            res["ans"] = q_tuple[7]
            res["sol"] = q_tuple[8]
    elif qtype == "Statement-Based":
        if lang == "en":
            res["q"] = q_tuple[1]
            res["opts"] = q_tuple[3]
            res["ans"] = q_tuple[5]
            res["sol"] = q_tuple[6]
        else:
            res["q"] = q_tuple[2]
            res["opts"] = q_tuple[4]
            res["ans"] = q_tuple[5]
            res["sol"] = q_tuple[7]
    elif qtype in ["True/False", "Fill in the Blank"]:
        if lang == "en":
            res["q"] = q_tuple[1]
            res["ans"] = q_tuple[3]
            res["sol"] = q_tuple[4]
        else:
            res["q"] = q_tuple[2]
            res["ans"] = q_tuple[3]
            res["sol"] = q_tuple[5]
    elif qtype == "Match the Following":
        if lang == "en":
            res["q"] = q_tuple[1]
            res["items"] = q_tuple[3]
            res["options"] = q_tuple[5]
            res["sol"] = q_tuple[7]
        else:
            res["q"] = q_tuple[2]
            res["items"] = q_tuple[4]
            res["options"] = q_tuple[6]
            res["sol"] = q_tuple[8]
    elif qtype in ["One-Liner", "Why", "How", "Case Study", "Teach the Concept"]:
        if lang == "en":
            res["q"] = q_tuple[1]
            res["sol"] = q_tuple[3]
        else:
            res["q"] = q_tuple[2]
            res["sol"] = q_tuple[4]
    elif qtype == "Assertion-Reason":
        if lang == "en":
            res["q"] = q_tuple[1]
            res["opts"] = EN_AR_OPTS
            res["ans"] = q_tuple[3]
            res["sol"] = q_tuple[4]
        else:
            res["q"] = q_tuple[2]
            res["opts"] = HI_AR_OPTS
            res["ans"] = q_tuple[3]
            res["sol"] = q_tuple[5]
    return res

# Import data from section-specific files
from sec2_data import sec2_raw
from sec3_data import sec3_raw
from sec4_data import sec4_raw
from sec5_data import sec5_raw
from practice_data import practice_raw
from mock_data import mock_raw


# Master formatter for the output databases
def format_question(q, lang="en"):
    qtype = q["type"]
    formatted = {"type": qtype}
    
    if lang == "en":
        formatted["q"] = q["q_en"]
        if qtype in ["MCQ", "Multiple Correct MCQ", "Statement-Based"]:
            formatted["opts"] = q["opts_en"]
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_en"]
        elif qtype == "True/False":
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_en"]
        elif qtype == "Fill in the Blank":
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_en"]
        elif qtype == "Match the Following":
            formatted["items"] = q["items_en"]
            formatted["options"] = q["options_en"]
            formatted["sol"] = q["sol_en"]
        elif qtype in ["One-Liner", "Why", "How", "Case Study", "Teach the Concept"]:
            formatted["sol"] = q["sol_en"]
        elif qtype == "Assertion-Reason":
            formatted["opts"] = EN_AR_OPTS
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_en"]
    else: # lang == "hi"
        formatted["q"] = q["q_hi"]
        if qtype in ["MCQ", "Multiple Correct MCQ", "Statement-Based"]:
            formatted["opts"] = q["opts_hi"]
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_hi"]
        elif qtype == "True/False":
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_hi"]
        elif qtype == "Fill in the Blank":
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_hi"]
        elif qtype == "Match the Following":
            formatted["items"] = q["items_hi"]
            formatted["options"] = q["options_hi"]
            formatted["sol"] = q["sol_hi"]
        elif qtype in ["One-Liner", "Why", "How", "Case Study", "Teach the Concept"]:
            formatted["sol"] = q["sol_hi"]
        elif qtype == "Assertion-Reason":
            formatted["opts"] = HI_AR_OPTS
            formatted["ans"] = q["ans"]
            formatted["sol"] = q["sol_hi"]
            
    return formatted

# Format and distribute Section 1 (convert from raw tuples)
for q_tuple in sec1_raw:
    en_data["deepDive"]["sections"][0]["masteryZone"].append(convert_sec1_question(q_tuple, "en"))
    hi_data["deepDive"]["sections"][0]["masteryZone"].append(convert_sec1_question(q_tuple, "hi"))

# Format and distribute Sections 2-5
sec_raw_lists = [sec2_raw, sec3_raw, sec4_raw, sec5_raw]
for sec_idx, raw_list in enumerate(sec_raw_lists):
    for q in raw_list:
        en_data["deepDive"]["sections"][sec_idx + 1]["masteryZone"].append(format_question(q, "en"))
        hi_data["deepDive"]["sections"][sec_idx + 1]["masteryZone"].append(format_question(q, "hi"))

# Format and distribute Practice
practice_en = []
practice_hi = []
for q in practice_raw:
    practice_en.append(format_question(q, "en"))
    practice_hi.append(format_question(q, "hi"))

en_data["practiceQuestions"] = practice_en
hi_data["practiceQuestions"] = practice_hi

# Format and distribute Mock
mock_en = []
mock_hi = []
for q in mock_raw:
    mock_en.append(format_question(q, "en"))
    mock_hi.append(format_question(q, "hi"))

en_data["mockTestQuestions"] = mock_en
hi_data["mockTestQuestions"] = mock_hi

# UI Labels injection
en_data["labels"] = {
    "tabs": {
        "practice": "2. Practice Zone (50 Qs)"
    },
    "practiceZoneHeader": {
        "title": "Practice Zone: 50 Questions"
    },
    "mockIntro": {
        "title": "UPSC Prelims Mock Exam",
        "description": "Contains 10 questions testing conceptual understanding of the causes of failure of the Portuguese empire in India. 1/3 negative marking applies.",
        "startBtn": "Start Mock Exam"
    },
    "mockPlay": {
        "prevBtn": "Previous",
        "nextBtn": "Next",
        "submitBtn": "Submit Test"
    },
    "clickToExpand": "Click to Expand"
}

hi_data["labels"] = {
    "tabs": {
        "practice": "2. अभ्यास क्षेत्र (50 प्रश्न)"
    },
    "practiceZoneHeader": {
        "title": "अभ्यास क्षेत्र: 50 प्रश्न"
    },
    "mockIntro": {
        "title": "यूपीएससी प्रीलिम्स मॉक परीक्षा",
        "description": "भारत में पुर्तगाली साम्राज्य के पतन के कारणों की वैचारिक समझ का परीक्षण करने वाले 10 प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला",
        "nextBtn": "अगला",
        "submitBtn": "टेस्ट सबमिट करें"
    },
    "clickToExpand": "विस्तार करने के लिए क्लिक करें"
}

# Write out JSON files
with open(os.path.join(BASE_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(BASE_DIR, "hi", "content.json"), "w", encoding="utf-8") as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: JSON databases generated successfully.")
