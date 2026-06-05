import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Script-and-Language"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Script & Language"
    },
    "hero": {
        "title": "Harappan Script and Language",
        "description": "Master the logo-syllabic script, Boustrophedon writing direction, major inscriptions like the Dholavira Signboard, and linguistic theories for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your mastery on the Harappan writing system. This timed test contains 10 high-quality, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Epigraphical & Linguistic Evolution",
        "description": "Explore the components, physical distribution, and decipherment debates of the Indus script.",
        "cards": [
            {
                "period": "Writing Mechanics",
                "date": "Boustrophedon & Direction",
                "details": "Written primarily Right-to-Left, switching to Left-to-Right in subsequent lines. Proven by sign compression on the left margins of seals."
            },
            {
                "period": "Inscriptions",
                "date": "Seals, Copper & Signboard",
                "details": "Short inscriptions found on steatite seals, copper tablets, and clay pottery. The Dholavira Signboard features 10 large gypsum characters."
            },
            {
                "period": "Linguistic Models",
                "date": "Dravidian vs. Aryan Theories",
                "details": "Linguistic debates connect the script to Proto-Dravidian (Mahadevan/Parpola) or Indo-Aryan Sanskrit (S.R. Rao). It remains undeciphered."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these memory hooks to retain critical facts about the Harappan script and language for the UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: Writing Direction",
                "phrase": "\"Boustrophedon - Bull plowing the field (Right to Left, then Left to Right)\"",
                "decryption": "The writing direction alternates lines like an ox plowing: first line **Right to Left**, second line **Left to Right**."
            },
            {
                "title": "Mnemonic 2: The Signboard Count",
                "phrase": "\"Dho-10-Gypsum (Dholavira 10 gypsum signs signboard)\"",
                "decryption": "The Dholavira signboard features exactly **10 large white gypsum symbols** once mounted on a wooden frame."
            },
            {
                "title": "Mnemonic 3: Missing Key",
                "phrase": "\"No Rosetta in Indus (Missing bilingual key)\"",
                "decryption": "Decipherment is blocked because no bilingual inscription (like Egypt's Rosetta Stone) has been found in Harappan archaeology."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
        "items": [
            {
                "question": "How did archaeologists prove the right-to-left writing direction of the script?",
                "answer": "By observing the <strong>cramping/compression of signs</strong> on the left margins of seals, showing the scribe ran out of space.",
                "icon": "fa-compress"
            },
            {
                "question": "What is the estimated number of distinct signs in the logo-syllabic script?",
                "answer": "Between <strong>375 and 400 signs</strong>, indicating it is not alphabetical but logo-syllabic.",
                "icon": "fa-list-ol"
            },
            {
                "question": "Name the scholars associated with the Proto-Dravidian linguistic hypothesis.",
                "answer": "<strong>Iravatham Mahadevan</strong> (India) and <strong>Asko Parpola</strong> (Finland).",
                "icon": "fa-user-graduate"
            },
            {
                "question": "Where was the 10-symbol public signboard discovered?",
                "answer": "Near the northern gateway of the Citadel at <strong>Dholavira</strong>, Gujarat.",
                "icon": "fa-sign"
            },
            {
                "question": "What is the non-linguistic symbol hypothesis proposed by Farmer, Sproat, and Witzel?",
                "answer": "The theory that the script did not encode a spoken language but was a <strong>non-linguistic system of heraldic or ritual symbols</strong>.",
                "icon": "fa-circle-question"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the writing direction, physical inscriptions, and linguistic models of the Harappan Civilisation.",
        "sections": [
            {
                "title": "1. Characteristics, Decipherment Attempts & Writing Direction (Boustrophedon)",
                "content": """<p>The Harappan script is a highly standardized system of graphic communication. While it has not been successfully deciphered, its structural characteristics are well documented.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-arrow-left-long"></i> Boustrophedon & Direction of Writing</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Right-to-Left Start:</strong> The writing was primarily written from right to left. Scribes began on the right and compressed symbols on the left margin as they ran out of space (cramping).</li>
      <li><strong>Boustrophedon:</strong> Longer texts alternate directions. The first line runs right-to-left, the second left-to-right, mirroring the path of a plowing ox.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shapes"></i> Script Typology & Sign Count</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      The script is **logo-syllabic**, meaning each sign represents a word or a syllable. It is not alphabetical (which would have ~30 signs) nor purely pictographic (which would have thousands). It features between **375 and 400 distinct signs**. Decipherment attempts are blocked because the language family is unknown, there are no bilingual inscriptions, and the average inscription length is very short (about 5 characters).
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Key Archaeological Inscriptions (Seals, Copper Tablets & Dholavira Signboard)",
                "content": """<p>The Harappan script is found across multiple physical mediums, reflecting its administrative, trade, and civic integration in daily municipal life.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shield"></i> Steatite Seals & Copper Inscriptions</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Steatite Seals:</strong> The majority of writing is found on square steatite seals, where short texts accompany animal reliefs (unicorn, bull) to stamp clay cargo tags.</li>
      <li><strong>Copper Tablets:</strong> Small copper plates feature engraved script signs on one side and animal figures on the other, likely serving as trade tokens or amulets.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-heading"></i> The Dholavira Signboard</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Discovered at Dholavira, Gujarat, this unique inscription features **ten large symbols**, each about 37 cm high. The signs were carved out of white gypsum crystalline paste and mounted on a large wooden board that once hung over the northern gateway of the Citadel. This indicates that writing had public administrative utility, declaring civic authority to visitors.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Linguistic Affiliation Theories (Dravidian, Indo-Aryan & Other Models)",
                "content": """<p>In the absence of a decipherment key, scholars have proposed competing linguistic models to reconstruct the language spoken by the Indus people.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-language"></i> Dravidian & Indo-Aryan Hypotheses</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Dravidian Model:</strong> Championed by Iravatham Mahadevan and Asko Parpola, this theory suggests the language belonged to the Proto-Dravidian family, linking symbols like the 'fish' sign (read as *min*) to Dravidian homophones.</li>
      <li><strong>Indo-Aryan Model:</strong> Proposed by S.R. Rao, this theory claims the script represents an early form of Sanskrit/Vedic Indo-Aryan, reading the signs alphabetically.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-diagram-project"></i> Non-Linguistic & Other Theories</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      Other scholars link the language to the Munda/Austroasiatic family. A major revisionist hypothesis by Steve Farmer, Richard Sproat, and Michael Witzel argues that the script did not encode a spoken language at all, acting instead as a **non-linguistic symbol system** of heraldic, clan, or ritual signs, citing the extreme brevity of the texts and lack of repeating markers.
    </p>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Hindi base structure
hin_data = {
    "breadcrumbs": {
        "parent": "यूपीएससी पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "लिपि और भाषा"
    },
    "hero": {
        "title": "हड़प्पा लिपि और भाषा",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए लोगो-सिलेबिक लिपि, बोउस्ट्रोफेडन लेखन दिशा, धोलावीरा सूचना-पट्ट और प्रमुख भाषाई सिद्धांतों का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा लेखन प्रणाली के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "अभिलेखीय और भाषाई विकास",
        "description": "सिंधु लिपि के घटकों, उनके भौतिक वितरण और पढ़े जाने के प्रयासों से जुड़ी बहसों का अध्ययन करें।",
        "cards": [
            {
                "period": "लेखन पद्धति",
                "date": "बोउस्ट्रोफेडन और दिशा",
                "details": "लेखन मुख्य रूप से दाएं से बाएं और अगली पंक्तियों में बाएं से दाएं होता था। मुहरों के बाएं किनारे पर अक्षरों के सिकुड़ने (compression) से यह प्रमाणित होता है।"
            },
            {
                "period": "अभिलेखीय साक्ष्य",
                "date": "मुहर, तांबा और सूचना-पट्ट",
                "details": "सेलखड़ी की मुहरों, तांबे की पट्टियों और बर्तनों पर संक्षिप्त लेख। धोलावीरा से जिप्सम से बने 10 बड़े अक्षरों वाला सूचना-पट्ट मिला है।"
            },
            {
                "period": "भाषाई सिद्धांत",
                "date": "द्रविड़ बनाम आर्य मत",
                "details": "लिपि कोProto-Dravidian (महादेवन/पारपोला) या भारत-आर्य संस्कृत (एस.आर. राव) से जोड़ने वाले सिद्धांत। यह लिपि वर्तमान में अपठित है।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा लिपि और भाषा से संबंधित तथ्यों को आसानी से याद रखने के लिए इन दृश्य सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: लेखन की दिशा",
                "phrase": "\"बोउस्ट्रोफेडन - खेत जोतता बैल (दाएं से बाएं, फिर बाएं से दाएं)\"",
                "decryption": "लेखन की दिशा बारी-बारी से बदलती थी: पहली पंक्ति **दाएं से बाएं** और अगली पंक्ति **बाएं से दाएं**।"
            },
            {
                "title": "याद रखने का सूत्र 2: सूचना-पट्ट के अक्षर",
                "phrase": "\"धोला-10-जिप्सम (धोलावीरा 10 जिप्सम अक्षरों का बोर्ड)\"",
                "decryption": "धोलावीरा से लकड़ी के तख्ते पर सफेद जिप्सम से बने कुल **10 बड़े अक्षर** मिले हैं।"
            },
            {
                "title": "याद रखने का सूत्र 3: द्विभाषी कुंजी का अभाव",
                "phrase": "\"सिंधु में कोई रोसेटा नहीं (bilingual key missing)\"",
                "decryption": "हड़प्पा लिपि को पढ़ने में मुख्य बाधा यह है कि मिस्र के रोसेटा स्टोन की तरह कोई भी **द्विभाषी अभिलेख** नहीं मिला है।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "फ्लैशकार्ड्स तथ्य-प्रधान यूपीएससी प्रश्नों को याद रखने का सर्वोत्तम साधन हैं। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "पुराविदों ने कैसे सिद्ध किया कि लिपि दाएं से बाएं लिखी जाती थी?",
                "answer": "मुहरों के बाएं किनारे पर <strong>अक्षरों के संकुचन (cramping)</strong> को देखकर, जिससे पता चलता है कि लेखक के पास अंत में जगह कम पड़ गई थी।",
                "icon": "fa-compress"
            },
            {
                "question": "इस लोगो-सिलेबिक लिपि में कुल कितने विशिष्ट चिन्ह मिले हैं?",
                "answer": "लगभग <strong>375 से 400 चिन्ह</strong>, जो दर्शाते हैं कि यह वर्णमाला नहीं बल्कि अक्षरात्मक (logo-syllabic) है।",
                "icon": "fa-list-ol"
            },
            {
                "question": "लिपि को आदि-द्रविड़ (Proto-Dravidian) भाषा से जोड़ने वाले प्रमुख विद्वान कौन हैं?",
                "answer": "<strong>इरावथम महादेवन</strong> (भारत) और <strong>आस्को पारपोला</strong> (फिनलैंड)।",
                "icon": "fa-user-graduate"
            },
            {
                "question": "10 चिन्हों वाला सार्वजनिक सूचना-पट्ट (signboard) कहाँ खोजा गया था?",
                "answer": "गुजरात के <strong>धोलावीरा</strong> में किले के उत्तरी प्रवेश द्वार के समीप।",
                "icon": "fa-sign"
            },
            {
                "question": "स्टीव फार्मर, स्प्रोट और विटजेल द्वारा प्रस्तावित गैर-भाषाई प्रतीक सिद्धांत क्या है?",
                "answer": "यह सिद्धांत कि यह लिपि किसी बोली जाने वाली भाषा को नहीं दर्शाती थी, बल्कि <strong>कुल चिन्हों, धार्मिक या राजकीय प्रतीकों का गैर-भाषाई तंत्र</strong> थी।",
                "icon": "fa-circle-question"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "हड़प्पा लिपि की लेखन दिशा, पुरातात्विक साक्ष्यों और भाषाई मतभेदों का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. लक्षण, लिपियों को पढ़ने के प्रयास और लेखन दिशा (बोउस्ट्रोफेडन)",
                "content": """<p>हड़प्पा लिपि दृश्य संचार का एक अत्यधिक मानकीकृत रूप है। यद्यपि इसे अभी तक पढ़ा नहीं जा सका है, पर इसके संरचनात्मक लक्षण भली-भांति प्रलेखित हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-arrow-left-long"></i> बोउस्ट्रोफेडन और लेखन की दिशा</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>दाएं से बाएं प्रारंभ:</strong> लेखन मुख्य रूप से दाएं से बाएं होता था। लेखक दाईं ओर से लिखना शुरू करता था और मुहर के बाएं किनारे पर अक्षरों को सटाकर लिखता था (संकुचन)।</li>
      <li><strong>बोउस्ट्रोफेडन शैली:</strong> लंबे लेखों में दिशा बदलती थी। पहली पंक्ति दाएं से बाएं, दूसरी बाएं से दाएं लिखी जाती थी, जैसे खेत जोतते समय हल चलाने वाला मुड़ता है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shapes"></i> लिपि का प्रकार और चिन्हों की संख्या</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      यह लिपि **लोगो-सिलेबिक** (शब्द-अक्षरात्मक) है, जिसमें प्रत्येक चिन्ह किसी शब्द या ध्वनि का प्रतिनिधित्व करता है। यह न तो वर्णमाला है (जिसमें 30 के करीब वर्ण होते हैं) और न ही शुद्ध चित्रलिपि (जिसमें हजारों चित्र होते हैं)। इसमें **375 से 400 तक विशिष्ट चिन्ह** मिले हैं। इसे पढ़ने के प्रयासों में मुख्य बाधा भाषा परिवार का अज्ञात होना, किसी द्विभाषी शिलालेख का न होना और लेखों की औसत लंबाई का बहुत कम (लगभग 5 अक्षर) होना है।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. प्रमुख पुरातात्विक अभिलेख (मुहरें, तांबे की पट्टियां और धोलावीरा सूचना-पट्ट)",
                "content": """<p>हड़प्पा लिपि विभिन्न भौतिक माध्यमों पर अंकित मिलती है, जो व्यापारिक, नागरिक और प्रशासनिक जीवन में इसके गहरे एकीकरण को दर्शाती है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shield"></i> सेलखड़ी की मुहरें और तांबे के अभिलेख</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>सेलखड़ी मुहरें:</strong> लेखन का अधिकांश भाग वर्गाकार सेलखड़ी मुहरों पर मिला है, जहाँ जानवरों (एक सींग वाला बैल, सांड) के चित्रों के साथ व्यापारिक पहचान के लिए संक्षिप्त लेख लिखे होते थे।</li>
      <li><strong>तांबे के फलक:</strong> कांसे और तांबे के छोटे फलकों पर एक तरफ अक्षर और दूसरी तरफ पशु आकृतियाँ बनी मिली हैं, जो ताबीज या व्यापारिक पहचान टोकन रहे होंगे।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-heading"></i> धोलावीरा का सूचना-पट्ट (Signboard)</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      गुजरात के धोलावीरा में उत्खनन के दौरान **दस बड़े अक्षरों** वाला एक सूचना-पट्ट मिला है, जिसके प्रत्येक अक्षर की ऊंचाई लगभग 37 सेमी है। ये अक्षर सफेद जिप्सम के क्रिस्टलीय लेप से बने थे जिन्हें लकड़ी के बड़े बोर्ड पर लगाया गया था। यह बोर्ड कभी किले के उत्तरी प्रवेश द्वार के ऊपर टंगा था, जो प्रशासनिक निर्णयों और नागरिक सत्ता की सार्वजनिक घोषणा को दर्शाता है।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. भाषाई संबंध के सिद्धांत (द्रविड़, भारत-आर्य और अन्य परिकल्पनाएं)",
                "content": """<p>द्विभाषी कुंजी के अभाव में विद्वानों ने सिंधु वासियों द्वारा बोली जाने वाली भाषा को पुनर्निर्मित करने के लिए कई प्रतिस्पर्धी सिद्धांत दिए हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-language"></i> द्रविड़ और भारत-आर्य परिकल्पनाएँ</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>द्रविड़ सिद्धांत:</strong> इरावथम महादेवन और आस्को पारपोला इसके प्रमुख समर्थक हैं। इस मत के अनुसार यह भाषा आदि-द्रविड़ (Proto-Dravidian) परिवार की थी। जैसे मुहर पर बने 'मछली' के चिन्ह को द्रविड़ भाषा के समध्वनि शब्द *मीन* (मछली/तारा) के रूप में पढ़ा गया।</li>
      <li><strong>भारत-आर्य सिद्धांत:</strong> एस.आर. राव द्वारा प्रस्तावित इस मत के अनुसार यह लिपि संस्कृत/वैदिक आर्य भाषा का एक प्रारंभिक रूप थी, जिसे वे वर्णमाला के रूप में पढ़ते हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-diagram-project"></i> गैर-भाषाई प्रतीकवाद और अन्य मत</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      कुछ विद्वान इसे मुंडा/आस्ट्रो-एशियाई भाषा परिवार से जोड़ते हैं। एक प्रमुख वैकल्पिक परिकल्पना स्टीव फार्मर, रिचर्ड स्प्रोट और माइकल विटजेल द्वारा दी गई है। उनके अनुसार यह लिपि किसी बोली जाने वाली भाषा को नहीं दर्शाती थी, बल्कि **गैर-भाषाई राजकीय, कुल या धार्मिक प्रतीकों** का एक संग्रह थी, क्योंकि लेख बहुत छोटे हैं और उनमें व्याकरण संबंधी दोहराव का अभाव है।
    </p>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Practice Questions (50 Qs) - UPSC Prelims Multi-Statement Style
practice_data_eng = [
    (
        "Consider the following statements regarding the writing direction of the Harappan script:\n1. Scribes wrote from right to left, as evidenced by the compression of symbols on the left margin of seals.\n2. In longer inscriptions, they utilized the Boustrophedon system, where lines alternate in direction.\n3. The writing direction of Boustrophedon is unique to the Harappan civilisation and is not found in any other ancient civilisation.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Boustrophedon writing is not unique to the Harappans; it is also found in early ancient Greek and Sabaean inscriptions."
    ),
    (
        "With reference to the nature of the Harappan script, consider the following statements:\n1. It is a purely alphabetical script containing around 40 distinct characters.\n2. The script is logo-syllabic, with each sign representing a word or a syllable.\n3. The total number of identified distinct signs ranges between 375 and 400.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        1,
        "Statements 2 and 3 are correct. Statement 1 is incorrect: the script is logo-syllabic (375-400 signs), not alphabetical (which would require fewer than 40 characters)."
    ),
    (
        "Consider the following statements regarding the Dholavira Signboard finding:\n1. It features ten large pictographic signs carved out of white gypsum crystalline paste.\n2. The signs were mounted on a wooden frame and placed over the northern gateway of the Citadel.\n3. It remains undeciphered, consistent with all other inscriptions discovered in the Indus valley.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, describing the gypsum paste signs, gateway location, and undeciphered status of the Dholavira signboard."
    ),
    (
        "With reference to the physical distribution of Harappan inscriptions, consider the following statements:\n1. Script symbols are found engraved on square steatite seals, copper tablets, and clay pottery graffiti.\n2. Writing was reserved exclusively for administrative seals and is completely absent on domestic household pottery.\n3. Small copper tablets feature signs on one side and animal figures on the other, likely serving as trade tokens.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: writing is frequently found as graffiti on domestic potsherds, indicating widespread domestic use or ownership markings."
    ),
    (
        "Consider the following statements regarding the Dravidian hypothesis of the Harappan language:\n1. Iravatham Mahadevan and Asko Parpola are the primary scholars who argued that the Harappan language belongs to the Proto-Dravidian family.\n2. The 'fish' symbol is read as *min*, which represents both 'fish' and 'star' in Dravidian languages, denoting astral deities on seals.\n3. This hypothesis has been completely accepted by all linguists, resolving the decipherment debate.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the hypothesis remains a subject of intense academic debate and has not been universally accepted."
    ),
    (
        "With reference to the Indo-Aryan hypothesis of the Harappan language, consider the following statements:\n1. Scholar S.R. Rao proposed that the Harappan script represents a precursor to the Sanskrit language.\n2. Under this model, the script is read as an alphabetical system carrying Vedic phonetic sounds.\n3. S.R. Rao's decipherment has been universally accepted by the Archaeological Survey of India.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: S.R. Rao's reading has been widely rejected by mainstream linguists who point out arbitrary sign values and lack of grammatical structure in his translations."
    ),
    (
        "Consider the following statements regarding the non-linguistic symbol hypothesis of the Indus script:\n1. Steve Farmer, Richard Sproat, and Michael Witzel argued that the script did not encode a spoken language.\n2. They point out the extreme brevity of inscriptions, with the average text containing only 4 to 5 signs.\n3. They argue that the symbols served as heraldic coats-of-arms, clan emblems, or religious icons.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the core arguments of the Farmer-Sproat-Witzel non-linguistic hypothesis."
    ),
    (
        "With reference to the decipherment challenges of the Harappan script, consider the following statements:\n1. Decipherment is blocked because no bilingual inscription containing a known language has been discovered.\n2. The script lacks long texts; the longest known single inscription contains only 26 signs.\n3. Modern computer analysis has proven that the script has no statistical similarity to any human language.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: computer entropy analysis by Rajesh Rao and others showed the script's sign order behaves similarly to spoken human languages, contradicting the claim of no statistical similarity."
    ),
    (
        "Consider the following statements regarding the symbol typology of the Harappan script:\n1. The most frequently occurring sign is the 'fish' symbol, which has several variants with modifying strokes.\n2. Jar or U-shaped symbols are also highly common, often appearing at the end of inscriptions.\n3. The script completely lacks representations of human figures, focusing exclusively on geometric lines.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: signs depicting human figures carrying bows, holding sticks, or sitting in yogic postures are present in the script corpus."
    ),
    (
        "With reference to the writing instruments used by Harappan scribes, consider the following statements:\n1. Small copper styluses and bone sticks were used to carve characters into wet clay and wax molds.\n2. Large gypsum letters at Dholavira were cast in clay molds before being mounted on the wooden gate.\n3. Paper-like birch bark sheets imported from the Himalayas were used for administrative letters.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Statement 2 is incorrect: Dholavira gypsum signs were carved directly from stone or built using gypsum paste, not cast in clay molds. Statement 3 is incorrect: there is no archaeological evidence of birch bark sheets being used for writing in the IVC."
    ),
    (
        "Consider the following statements regarding the relation between Harappan script and punch-marked coins:\n1. Several symbols on Maurya punch-marked coins resemble signs from the Harappan script.\n2. This resemblance has been interpreted by some scholars as evidence of cultural and script continuity in India.\n3. The Harappan script was directly used to denote coin values during the Mature Harappan phase.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: coins did not exist in the Bronze Age Harappan economy; trade was carried out through barter and regulated weights, not coins."
    ),
    (
        "With reference to the Munda/Austroasiatic theory of the Harappan language, consider the following statements:\n1. Some linguists suggest that the language belonged to the Austroasiatic or Munda language family.\n2. This theory is supported by the presence of Munda loanwords in the early Rigveda, suggesting contacts in Northwest India.\n3. This theory has successfully deciphered the script's animal symbols as Munda clan totems.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Munda theory has not deciphered the script; it remains an unproven hypothesis."
    ),
    (
        "Consider the following statements regarding the Boustrophedon writing style:\n1. The term originates from Greek, meaning 'ox-turning', referring to the path of an ox plowing a field.\n2. The scribe starts on the right, writes to the left, then continues on the next line writing left to right.\n3. This style is also observed in early Sabaean (Yemeni) and Etruscan inscriptions.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the origin, path, and other historical occurrences of the Boustrophedon style."
    ),
    (
        "With reference to the sign compression on Harappan seals, consider the following statements:\n1. Signs are often crowded and cramped on the left margin of the seal.\n2. This cramping proves that the writing started on the right and moved leftwards.\n3. The seal carving was done in reverse (mirror image) so that the clay impression would read correctly.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the sign cramping, right-to-left direction, and mirror-image carving of seals."
    ),
    (
        "Consider the following statements regarding the undeciphered status of the Harappan script:\n1. Because it is undeciphered, we lack direct knowledge of Harappan religious mythology, names of rulers, or legal treaties.\n2. All our knowledge of Harappan socio-political organization is derived solely from material remains and archaeology.\n3. Deciphering the script would immediately clarify the relation between Harappan culture and later historical Indian traditions.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and describe the historical and archaeological consequences of the undeciphered script."
    ),
    (
        "With reference to the Dholavira Signboard gypsum letters, consider the following statements:\n1. Each symbol is approximately 37 cm high and 25 to 27 cm wide.\n2. The board was placed above a gate to declare the name of the ruling king.\n3. The wood backing of the signboard decayed over time, leaving the gypsum inlays in the soil.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: the exact text is undeciphered, and there is no evidence that it declared the name of a king, as monarchy is not proven."
    ),
    (
        "Consider the following statements regarding script signs on pottery:\n1. Signs written as post-firing graffiti on domestic pots were likely ownership or quantity marks.\n2. Pre-firing stamps on pottery indicate standardized industrial workshop markings.\n3. Writing on pottery is only found in elite Citadel quarters and is absent in Lower Towns.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: pottery graffiti containing script signs is widely found throughout the Lower Town quarters of commoners."
    ),
    (
        "With reference to the average length of Harappan texts, consider the following statements:\n1. The average inscription length is extremely short, containing only about 5 signs.\n2. The shortest inscriptions consist of a single symbol.\n3. The brevity of texts suggests they were names, titles, or trade quantities rather than narrative literature.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the brevity of inscriptions and its implications for text interpretation."
    ),
    (
        "Consider the following statements regarding the fish symbol in the Harappan script:\n1. The fish symbol is often modified with diacritical marks or strokes.\n2. In Dravidian, the word for fish (*min*) is a homophone for star (*min*), suggesting astronomical associations.\n3. The fish symbol is completely absent on copper tablets, appearing only on steatite seals.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the fish sign is present on all classes of inscriptions, including copper tablets and pottery graffiti."
    ),
    (
        "With reference to the script signs on ivory rods, consider the following statements:\n1. Engraved ivory sticks or rods have been excavated from Mohenjo-daro and Harappa.\n2. These rods carry script signs and were likely used as measuring scales or gaming dice.\n3. Ivory writing confirms the elite consumption of script-associated luxury goods.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing the ivory rod findings, usage, and social status associations."
    ),
    # Additional 30 questions
    (
        "Consider the following statements regarding the logo-syllabic nature of writing:\n1. A logo-syllabic script uses signs that represent both whole words (logograms) and phonetic syllables.\n2. Ancient Egyptian hieroglyphs and Mesopotamian cuneiform are examples of logo-syllabic scripts.\n3. The number of signs in a logo-syllabic script is typically in the hundreds, matching the Harappan sign count.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define the structural features of a logo-syllabic script."
    ),
    (
        "With reference to S.R. Rao's decipherment methodology, consider the following statements:\n1. S.R. Rao claimed that the late Harappan script evolved into the Phoenician alphabet.\n2. He assigned West Semitic phonetic values to Harappan signs to read them as Sanskrit words.\n3. S.R. Rao's Sanskrit readings have been widely accepted by international Semitic linguists.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Rao's readings are rejected for arbitrary phonetic assignments and forcing Indo-Aryan values on logo-syllabic signs."
    ),
    (
        "Consider the following statements regarding the fish symbol variants:\n1. Scribes added 'fins' or 'roofs' over the basic fish sign to create compound logograms.\n2. Asko Parpola interpreted these variants as names of planets and deities (e.g., *Pasu-min* for Halley's Comet).\n3. The variants show that the script had a highly systematic grammar of sign modification.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing sign modification, Parpola's planet readings, and systematic sign grammar."
    ),
    (
        "With reference to the writing on clay sealings, consider the following statements:\n1. Sealings are clay tags stamped with seals, used to secure cargo bags of grain and cotton.\n2. The backs of sealings often show impressions of woven reeds, mats, or leather cords.\n3. Sealings prove that the script played a central role in validating trade ownership and customs clearance.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing clay sealings, reed back-impressions, and trade validation."
    ),
    (
        "Consider the following statements regarding the script sign count:\n1. If a script has under 50 signs, it is alphabetical; if in the hundreds, it is logo-syllabic; if in the thousands, it is logo-graphic.\n2. The Harappan sign count of ~400 proves it represents a logo-syllabic system.\n3. The sign count indicates that literacy required memorizing hundreds of characters, likely restricting writing to professional scribes.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, outlining script typology, sign counts, and professional scribe status."
    ),
    (
        "With reference to the Boustrophedon direction indicator, consider the following statements:\n1. The direction of writing alternates from right-to-left in line 1, then left-to-right in line 2.\n2. This system prevented the scribe from having to return the stylus to the opposite margin, speeding up writing.\n3. The Boustrophedon style is only found in Indian languages and is absent in Europe.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Boustrophedon is a Greek term and was widely used in early Greek and Anatolian inscriptions."
    ),
    (
        "Consider the following statements regarding the steatite seals:\n1. Seals were carved in negative (reverse) relief so that the stamped clay impressions would appear in positive relief.\n2. The text on the seals reads correctly (from right-to-left) when viewed on the clay sealing itself.\n3. Scribes carved both the animal figures and the text signs with extreme precision using chert burins.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing reverse carving, correct reading on sealings, and chert tool precision."
    ),
    (
        "With reference to the longest Harappan inscription, consider the following statements:\n1. The longest single inscription contains 26 signs on a three-sided steatite baton.\n2. No tablet, seal, or pottery has yielded a long text of over 50 signs.\n3. The lack of long texts makes structural grammatical analysis of the language extremely difficult.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing the 26-sign baton, lack of long texts, and grammatical analysis blocks."
    ),
    (
        "Consider the following statements regarding the Indus script variants over time:\n1. The script remained highly static, showing little evolution over the 700 years of the mature phase.\n2. Scribes in Punjab and Gujarat used identical sign lists, proving centralized standards.\n3. The late Harappan phase shows a decline in seal quality and gradual disappearance of the script.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing script stability, identical regional signs, and late phase decline."
    ),
    (
        "With reference to the Rigveda and Harappan language, consider the following statements:\n1. The Rigveda contains several non-Indo-Aryan words identified as Proto-Dravidian loanwords.\n2. This linguistic layering suggests that Rigvedic speakers encountered Dravidian-like speakers in the Indus basin.\n3. The Rigveda directly describes the Boustrophedon writing style of the Meluhhans.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Rigveda is an oral text that does not describe the Harappan script or writing direction."
    ),
    (
        "Consider the following statements regarding the fish symbol reading *min*:\n1. *Min* is the Proto-Dravidian word for 'fish'.\n2. The homophone *min* also means 'star' or 'shining' in Dravidian languages.\n3. This homophonic reading is used to interpret fish symbols on seals as names of stars or astral deities.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the core linguistic rebus puzzle of the Dravidian reading."
    ),
    (
        "With reference to the writing on pottery jars, consider the following statements:\n1. Post-firing graffiti was scratched using sharp stone burins.\n2. Jars at Harappa show sequence numbers, likely indicating shipment counts.\n3. Writing on pots was done using ink made from charcoal and animal fat.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no archaeological evidence of charcoal-fat ink being used on pots; writing was incised or scratched, not painted with ink."
    ),
    (
        "Consider the following statements regarding the signboards at Dholavira:\n1. The wooden board was mounted over the gateway to the Citadel Castle.\n2. The gypsum characters are made of pure plaster of Paris.\n3. It represents a public declaration of civic authority and administrative literacy.\nWhich of the statements given above are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: characters were made of natural crystalline gypsum paste, which is chemically hydrous calcium sulfate, not modern processed plaster of Paris."
    ),
    (
        "With reference to S.R. Rao's alphabetical decipherment, consider the following statements:\n1. He read the signs from left to right, reversing the standard direction.\n2. He translated the text as Vedic Sanskrit names like *Aka*, *Rama*, and *Sada*.\n3. His translations have been dismissed as arbitrary and lacking phonetic consistency.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. S.R. Rao read the signs from right-to-left but forced Semitic values to extract Sanskrit words. His readings are widely dismissed."
    ),
    (
        "Consider the following statements regarding the sign cramping on the left:\n1. Scribes underestimated seal dimensions, starting on the right and squeezing letters on the left.\n2. This cramping proves that the seals were meant to be read directly, not stamped.\n3. Cramping is only observed on copper tablets and is absent on steatite seals.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Statement 2 is incorrect: cramping on the seal was mirrored, and it proved that the stamped clay tags (read right-to-left) were the primary media. Statement 3 is incorrect: cramping is common on steatite seals."
    ),
    (
        "With reference to the writing on ivory sticks, consider the following statements:\n1. Ivory sticks feature short sign inscriptions alongside geometric grid marks.\n2. They were likely used as administrative counters, luxury dice, or weavers' tools.\n3. Ivory rods were exported to Egypt, where they were placed in Pharaohs' tombs.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: there is no evidence of Harappan ivory rods being exported to Egyptian royal tombs."
    ),
    (
        "Consider the following statements regarding the undeciphered script's impact on Indian history:\n1. It prevents us from verifying if the Rigveda was written by Harappan citizens.\n2. It leaves the transition between the Indus valley and Gangetic civilisations highly debated.\n3. Deciphering the script would confirm the linguistic roots of early Indian urbanism.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the key historical debates linked to the undeciphered script."
    ),
    (
        "With reference to the sign modification system, consider the following statements:\n1. Scribes added short strokes, dots, or diagonal lines to primary signs to modify their values.\n2. Modified signs behave like vowel signs in historical Indian scripts (e.g. *matras*).\n3. This systematic modification suggests a highly structured phonology and script conventions.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct and define the sign modification system and its phonetic implications."
    ),
    (
        "Consider the following statements regarding the fish symbol variants read as planets:\n1. Asko Parpola argued that the fish symbol (*min*) represented stars or planets.\n2. The modified fish with a roof was read as *Velli-min* (Venus/White Star).\n3. S.R. Rao read the fish symbol as a letter value *ma* based on phonetic Semitic comparisons.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, detailing Parpola's planetary readings and Rao's alphabetical comparisons."
    ),
    (
        "With reference to the writing on storage jars, consider the following statements:\n1. Large black-slipped storage jars feature deeply incised script signs.\n2. These jars were used for exporting goods to Oman and the Persian Gulf.\n3. The incised signs likely indicated the exporter's seal, contents, or weights.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the export storage jars, Omani findings, and sign functions."
    )
]

practice_data_hin = [
    (
        "हड़प्पा लिपि की लेखन दिशा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखक दाएं से बाएं लिखते थे, जैसा कि मुहरों के बाएं किनारे पर प्रतीकों के संकुचन (compression) से सिद्ध होता है।\n2. लंबे अभिलेखों में उन्होंने बोउस्ट्रोफेडन प्रणाली का उपयोग किया, जहाँ पंक्तियों में लेखन की दिशा वैकल्पिक रूप से बदलती है।\n3. बोउस्ट्रोफेडन लेखन शैली केवल हड़प्पा सभ्यता की अनूठी विशेषता है और यह किसी अन्य प्राचीन सभ्यता में नहीं मिलती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: बोउस्ट्रोफेडन लेखन केवल हड़प्पा वासियों तक सीमित नहीं था; यह प्रारंभिक प्राचीन यूनानी (Greek) और सबाई (Sabaean) अभिलेखों में भी पाया जाता है।"
    ),
    (
        "हड़प्पा लिपि की प्रकृति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक विशुद्ध रूप से वर्णमाला (alphabetical) लिपि है जिसमें लगभग 40 विशिष्ट वर्ण हैं।\n2. यह लिपि लोगो-सिलेबिक (logo-syllabic) है, जिसमें प्रत्येक चिन्ह एक शब्द या शब्दांश का प्रतिनिधित्व करता है।\n3. पहचाने गए विशिष्ट चिन्हों की कुल संख्या 375 से 400 के बीच है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        1,
        "कथन 2 और 3 सही हैं। कथन 1 गलत है: यह लिपि लोगो-सिलेबिक है (375-400 चिन्ह), न कि वर्णमाला (जिसमें 40 से कम वर्णों की आवश्यकता होती)।"
    ),
    (
        "धोलावीरा के सूचना-पट्ट (Signboard) की खोज के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें सफेद जिप्सम के क्रिस्टलीय लेप से तराशे गए दस बड़े चित्रलेखीय चिन्ह हैं।\n2. इन चिन्हों को एक लकड़ी के फ्रेम पर लगाकर किले (Citadel) के उत्तरी प्रवेश द्वार के ऊपर लगाया गया था।\n3. यह अभिलेख आज तक अपठित है, जैसा कि सिंधु घाटी में मिले अन्य अभिलेखों के साथ है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो सफेद अक्षरों, किले के उत्तरी द्वार और धोलावीरा सूचना-पट्ट की अपठित स्थिति को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा अभिलेखों के भौतिक वितरण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लिपि के प्रतीक वर्गाकार सेलखड़ी मुहरों, तांबे की पट्टियों और मिट्टी के बर्तनों पर खुदे हुए मिले हैं।\n2. लेखन केवल प्रशासनिक मुहरों तक सीमित था और घरेलू मिट्टी के बर्तनों पर यह पूरी तरह अनुपस्थित है।\n3. तांबे के छोटे फलकों पर एक तरफ अक्षर और दूसरी तरफ पशु आकृतियाँ बनी हैं, जो व्यापारिक टोकन रहे होंगे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है: घरेलू बर्तनों पर भी लिपि के चिन्ह खुदे मिले हैं, जो घरेलू स्तर पर पहचान या मात्रा के चिह्नों को दर्शाते हैं।"
    ),
    (
        "हड़प्पा भाषा के द्रविड़ सिद्धांत (Dravidian hypothesis) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इरावथम महादेवन और आस्को पारपोला इसके मुख्य प्रस्तावक हैं, जिनका मानना है कि हड़प्पा भाषा आदि-द्रविड़ परिवार की थी।\n2. मछली के प्रतीक को *मीन* पढ़ा जाता है, जो द्रविड़ भाषाओं में 'मछली' और 'तारा' दोनों का समध्वनि शब्द है, जो मुहरों पर खगोलीय देवताओं को दर्शाता है।\n3. यह सिद्धांत सभी भाषाविदों द्वारा सर्वसम्मति से स्वीकार कर लिया गया है, जिससे लिपि को पढ़ने की बहस समाप्त हो गई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: यह परिकल्पना आज भी इतिहासकारों और भाषाविदों के बीच गहन विवाद का विषय है और इसे सर्वसम्मति नहीं मिली है।"
    ),
    (
        "हड़प्पा भाषा के भारत-आर्य सिद्धांत (Indo-Aryan hypothesis) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. विद्वान एस.आर. राव ने प्रस्ताव दिया कि हड़प्पा लिपि संस्कृत भाषा का एक प्रारंभिक रूप है।\n2. इस मॉडल के तहत, लिपि को वैदिक ध्वनियों वाली एक वर्णमाला प्रणाली के रूप में पढ़ा जाता है।\n3. एस.आर. राव के इस अनुवाद को भारतीय पुरातत्व सर्वेक्षण (ASI) द्वारा आधिकारिक रूप से स्वीकार कर लिया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: एस.आर. राव के अनुवाद को मुख्यधारा के भाषाविदों द्वारा खारिज कर दिया गया है क्योंकि उन्होंने मनमाने ढंग से चिन्हों के मान रखे थे।"
    ),
    (
        "सिंधु लिपि के गैर-भाषाई प्रतीक सिद्धांत (non-linguistic hypothesis) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. स्टीव फार्मर, रिचर्ड स्प्रोट और माइकल विटजेल ने तर्क दिया कि यह लिपि किसी बोली जाने वाली भाषा को कोड नहीं करती थी।\n2. वे अभिलेखों की अत्यधिक संक्षिप्तता की ओर इशारा करते हैं, जिसमें औसत लेख में केवल 4 से 5 चिन्ह ही मिलते हैं।\n3. उनका तर्क है कि ये प्रतीक कुल चिन्हों, राजकीय प्रतीकों या धार्मिक चिह्नों के रूप में कार्य करते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और फार्मर-स्प्रोट-विटजेल के गैर-भाषाई प्रतीक सिद्धांत के मूल तर्कों को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा लिपि को पढ़ने की चुनौतियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लिपि को पढ़ना इसलिए कठिन है क्योंकि किसी ज्ञात भाषा के साथ कोई भी द्विभाषी अभिलेख (bilingual inscription) नहीं मिला है।\n2. लिपि में बड़े ग्रंथों का अभाव है; सबसे लंबे ज्ञात एकल लेख में केवल 26 चिन्ह हैं।\n3. आधुनिक कंप्यूटर विश्लेषण से सिद्ध हो चुका है कि इस लिपि की किसी भी मानव भाषा से कोई सांख्यिकीय समानता नहीं है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: राजेश राव और उनके सहयोगियों द्वारा किए गए कंप्यूटर विश्लेषण से पता चला है कि चिन्हों का क्रम प्राकृतिक मानवीय भाषाओं के समान ही व्यवहार करता है।"
    ),
    (
        "हड़प्पा लिपि के प्रतीकों के प्रकार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सबसे अधिक बार दोहराया जाने वाला चिन्ह 'मछली' (fish) का प्रतीक है, जिसके कई रूप और स्ट्रोक्स हैं।\n2. जार या 'U' के आकार के प्रतीक भी बहुत आम हैं, जो अक्सर अभिलेखों के अंत में दिखाई देते हैं।\n3. इस लिपि में मानव आकृतियों का चित्रण पूर्णतः अनुपस्थित है, और केवल ज्यामितीय रेखाएँ मिलती हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि धनुष लिए, लाठी पकड़े या योगासन में बैठे मनुष्यों के चित्र भी लिपि चिन्हों में शामिल हैं।"
    ),
    (
        "हड़प्पा के लेखकों द्वारा प्रयुक्त लेखन उपकरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. गीली मिट्टी और मोम के सांचों पर अक्षरों को उकेरने के लिए तांबे की सलाइयों और हड्डियों के टुकड़ों का उपयोग किया जाता था।\n2. धोलावीरा के बड़े जिप्सम अक्षरों को लकड़ी के गेट पर लगाने से पहले मिट्टी के सांचों में ढाला गया था।\n3. हिमालय से आयातित भोजपत्र की शीट्स का उपयोग प्रशासनिक पत्रों के लिए किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 सही है। कथन 2 गलत है क्योंकि धोलावीरा के अक्षर जिप्सम पत्थर काटकर या लेप से सीधे बनाए गए थे। कथन 3 गलत है क्योंकि हड़प्पा काल में भोजपत्र पर लिखने का कोई साक्ष्य नहीं मिला है।"
    ),
    (
        "हड़प्पा लिपि और आहत सिक्कों (punch-marked coins) के बीच संबंध के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मौर्य कालीन आहत सिक्कों पर मिले कई प्रतीक हड़प्पा लिपि के चिन्हों से मेल खाते हैं।\n2. इस समानता को कुछ विद्वानों द्वारा भारत में सांस्कृतिक और लिपि निरंतरता के साक्ष्य के रूप में व्याख्यायित किया गया है।\n3. परिपक्व हड़प्पा चरण के दौरान सिक्कों के मूल्यों को दर्शाने के लिए सीधे हड़प्पा लिपि का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि कांस्य युगीन हड़प्पा अर्थव्यवस्था में सिक्के नहीं थे; व्यापार वस्तु-विनिमय (barter) और मानकीकृत बाटों द्वारा होता था।"
    ),
    (
        "हड़प्पा भाषा के मुंडा/आस्ट्रो-एशियाई सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कुछ भाषाविदों का सुझाव है कि सिंधु सभ्यता की भाषा मुंडा या आस्ट्रो-एशियाई भाषा परिवार की थी।\n2. इस सिद्धांत को ऋग्वेद में मुंडा मूल के ऋण-शब्दों (loanwords) की उपस्थिति से बल मिलता है, जो उत्तर-पश्चिम भारत में संपर्कों को दर्शाता है।\n3. इस सिद्धांत ने लिपि के पशु प्रतीकों को मुंडा कुल चिन्हों के रूप में सफलतापूर्वक पढ़ लिया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मुंडा सिद्धांत ने लिपि को पढ़ा नहीं है, यह केवल एक अपुष्ट भाषाई परिकल्पना है।"
    ),
    (
        "बोउस्ट्रोफेडन (Boustrophedon) लेखन शैली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस शब्द की उत्पत्ति ग्रीक से हुई है, जिसका अर्थ है 'बैल का मुड़ना', जो खेत जोतने वाले बैल के मार्ग को संदर्भित करता है।\n2. लेखक दाईं ओर से शुरू करता है, बाईं ओर लिखता है, और फिर अगली पंक्ति में सीधे बाएं से दाएं लिखना जारी रखता है।\n3. यह शैली प्रारंभिक सबाई (यमन) और एट्रस्कन शिलालेखों में भी देखी गई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और बोउस्ट्रोफेडन शैली की उत्पत्ति, लेखन मार्ग और अन्य ऐतिहासिक उदाहरणों को स्पष्ट करते हैं।"
    ),
    (
        "मुहरों पर अक्षरों के संकुचन (compression) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहर के बाएं किनारे पर अक्षर अक्सर बहुत सटकर और छोटे बने हुए हैं।\n2. यह संकुचन यह सिद्ध करता है कि मूल लेखन दाईं ओर से शुरू होकर बाईं ओर जाता था।\n3. मुहर की नक्काशी उल्टी (mirror image) की जाती थी ताकि गीली मिट्टी पर छाप सीधी पढ़ी जा सके।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "Clean 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो अक्षरों के संकुचन, दाएं से बाएं लेखन दिशा और दर्पण-छवि नक्काशी का विवरण देते हैं।"
    ),
    (
        "हड़प्पा लिपि के अपठित होने के ऐतिहासिक प्रभावों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसके अपठित होने के कारण हमें हड़प्पा वासियों के धार्मिक मिथकों, राजाओं के नाम या संधियों का कोई सीधा ज्ञान नहीं है।\n2. हड़प्पा के सामाजिक-राजनीतिक संगठन का हमारा संपूर्ण ज्ञान केवल भौतिक अवशेषों और पुरातत्व पर आधारित है।\n3. इस लिपि को पढ़ने से हड़प्पा संस्कृति और बाद की ऐतिहासिक भारतीय परंपराओं के बीच का भाषाई संबंध तुरंत स्पष्ट हो जाएगा।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और लिपि के न पढ़े जाने के पुरातात्विक व ऐतिहासिक परिणामों को स्पष्ट करते हैं।"
    ),
    (
        "धोलावीरा सूचना-पट्ट के जिप्सम अक्षरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. प्रत्येक अक्षर लगभग 37 सेमी ऊंचा और 25 से 27 सेमी चौड़ा है।\n2. यह बोर्ड प्रवेश द्वार के ऊपर वहां के शासक राजा के नाम की घोषणा करने के लिए लगाया गया था।\n3. सूचना-पट्ट की लकड़ी समय के साथ नष्ट हो गई, जिससे जिप्सम के अक्षर मिट्टी में दबे रह गए।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि यह लिपि अपठित है और राजा के होने का कोई ठोस पुरातात्विक साक्ष्य नहीं है।"
    ),
    (
        "मिट्टी के बर्तनों पर लिपि चिन्हों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पकाने के बाद बर्तनों पर खरोंचे गए चिन्ह (graffiti) संभवतः मालिकाना हक या मात्रा दर्शाते थे।\n2. पकाने से पहले बर्तनों पर लगाई गई मुहरें मानकीकृत औद्योगिक कार्यशालाओं के चिह्नों को दर्शाती हैं।\n3. बर्तनों पर लिखे लेख केवल किले (Citadel) के बर्तनों पर मिले हैं और निचले नगर में अनुपस्थित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि निचले नगर के आम घरों के बर्तनों पर भी खरोंचे गए चिन्ह प्रचुर मात्रा में मिले हैं।"
    ),
    (
        "हड़प्पा लेखों की औसत लंबाई के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखों की औसत लंबाई बहुत कम है, जिसमें केवल 5 के करीब चिन्ह मिलते हैं।\n2. सबसे छोटा लेख केवल एक अक्षर का है।\n3. लेखों की यह संक्षिप्तता बताती है कि ये नाम, उपाधियाँ या व्यापारिक मात्राएँ थीं, न कि कोई महाकाव्य साहित्य।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो लेखों की संक्षिप्तता और उनके संभावित अर्थों को स्पष्ट करते हैं।"
    ),
    (
        "हड़प्पा लिपि में 'मछली' (fish) के प्रतीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मछली के प्रतीक को अक्सर अतिरिक्त स्ट्रोक्स या उप-चिन्हों के साथ संशोधित किया जाता था।\n2. द्रविड़ भाषा में मछली (*मीन*) शब्द 'तारे' (*मीन*) का समध्वनि है, जो खगोलीय संबंधों की ओर इशारा करता है।\n3. मछली का प्रतीक तांबे के फलकों पर पूरी तरह अनुपस्थित है और केवल सेलखड़ी मुहरों पर मिलता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मछली का चिन्ह तांबे की पट्टियों और बर्तनों के टुकड़ों सहित सभी प्रकार के लेखों में मिलता है।"
    ),
    (
        "हाथीदांत की शलाकाओं (ivory rods) पर लिपि के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो और हड़प्पा से अक्षरों से युक्त हाथीदांत की शलाकाएँ प्राप्त हुई हैं।\n2. इन शलाकाओं पर चिन्ह बने हैं और इनका उपयोग पैमाने (scales) या पासों के रूप में किया जाता था।\n3. हाथीदांत पर लेखन यह दर्शाता है कि लिखने की कला विलासिता के साधनों से भी जुड़ी थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो हाथीदांत की शलाकाओं, उनके कार्यों और सामाजिक विलासिता संबंधों को दर्शाते हैं।"
    ),
    # Additional 30 questions
    (
        "लेखन के लोगो-सिलेबिक (logo-syllabic) स्वरूप के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एक लोगो-सिलेबिक लिपि में चिन्ह पूरे शब्द और ध्वन्यात्मक अक्षरों दोनों का प्रतिनिधित्व करते हैं।\n2. प्राचीन मिस्र की चित्रलिपि (hieroglyphs) और मेसोपोटामिया की कीलाक्षर लिपि लोगो-सिलेबिक के उदाहरण हैं।\n3. इस प्रणाली में चिन्हों की संख्या सैकड़ों में होती है, जो हड़प्पा के चिन्हों की संख्या (लगभग 400) से मेल खाती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और लोगो-सिलेबिक लेखन प्रणाली के लक्षणों को परिभाषित करते हैं।"
    ),
    (
        "एस.आर. राव की वर्णमाला अनुवाद पद्धति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एस.आर. राव ने दावा किया कि उत्तर हड़प्पा लिपि ही आगे चलकर फोनीशियन वर्णमाला में बदल गई।\n2. उन्होंने हड़प्पा चिन्हों को पश्चिमी सेमिटिक ध्वन्यात्मक मान देकर उन्हें संस्कृत शब्दों के रूप में पढ़ा।\n3. उनके इस संस्कृत अनुवाद को अंतरराष्ट्रीय भाषाविदों द्वारा व्यापक रूप से स्वीकार किया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि उनके अनुवाद को मनमाने मान रखने के कारण खारिज किया जा चुका है।"
    ),
    (
        "मछली चिन्ह के विभिन्न रूपों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखकों ने मूल मछली चिन्ह के ऊपर 'पंख' या 'छत' जोड़कर संयुक्त चित्रलेख बनाए।\n2. आस्को पारपोला ने इन रूपों को ग्रहों और देवताओं के नाम (जैसे *वेल्ली-मीन* यानी शुक्र तारा) के रूप में पढ़ा।\n3. ये रूप दर्शाते हैं कि लिपि में चिन्ह संशोधन का एक व्यवस्थित व्याकरण था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो ग्रहों के नाम, चिन्ह संशोधन और व्याकरणिक संरचना को स्पष्ट करते हैं।"
    ),
    (
        "मिट्टी के मुहरों की छापों (clay sealings) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये मिट्टी के टैग थे जिन पर मुहरों से छाप लगाई जाती थी, जिनका उपयोग अनाज और कपास की बोरियों को सुरक्षित करने के लिए होता था।\n2. इन मिट्टियों के पीछे अक्सर बुने हुए सरकंडों, चटाई या चमड़े की रस्सियों के निशान मिले हैं।\n3. ये छापें प्रमाणित करती हैं कि व्यापारिक स्वामित्व और सीमा शुल्क निकासी में लिपि की केंद्रीय भूमिका थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और मिट्टियों की छापों, रस्सियों के निशानों और व्यापार नियमन में उनकी भूमिका को दर्शाते हैं।"
    ),
    (
        "लिपि के चिन्हों की संख्या के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यदि किसी लिपि में 50 से कम चिन्ह हैं तो वह वर्णमाला है; यदि सैकड़ों में हैं तो लोगो-सिलेबिक; और हजारों में हैं तो लोगो-ग्राफिक।\n2. हड़प्पा के चिन्हों की संख्या (~400) यह प्रमाणित करती है कि यह एक लोगो-सिलेबिक प्रणाली थी।\n3. यह संख्या बताती है कि साक्षरता के लिए सैकड़ों अक्षरों को याद रखना आवश्यक था, जिससे लेखन केवल पेशेवर लिपिकों तक सीमित रहा होगा।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो वर्णमाला की तुलना, लोगो-सिलेबिक प्रणाली और पेशेवर लिपिकों की आवश्यकता को स्पष्ट करते हैं।"
    ),
    (
        "बोउस्ट्रोफेडन लेखन की दिशा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखन की दिशा पहली पंक्ति में दाएं से बाएं और अगली पंक्ति में बाएं से दाएं बदलती थी।\n2. यह प्रणाली लेखक को प्रत्येक नई पंक्ति में हाथ वापस विपरीत दिशा में ले जाने से बचाती थी, जिससे लिखने में तेजी आती थी।\n3. बोउस्ट्रोफेडन शैली केवल भारतीय भाषाओं में पाई जाती है और यूरोप में अनुपस्थित रही है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बोउस्ट्रोफेडन ग्रीक शब्द है और यह प्राचीन यूनानी व यूरोपीय अभिलेखों में प्रयुक्त होती थी।"
    ),
    (
        "सेलखड़ी की मुहरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों को उल्टे (reverse) रूप में उकेरा जाता था ताकि मिट्टी पर छापने पर अक्षर सीधे (positive) दिखाई दें।\n2. मुहरों के अक्षर मिट्टी की छापों पर सीधे (दाएं से बाएं) पढ़े जाते हैं।\n3. लेखक चर्ट के नुकीले औजारों से मुहरों पर पशु और अक्षरों को अत्यंत सूक्ष्मता से उकेरते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो उल्टी नक्काशी, सीधी छाप और चर्ट औजारों के उपयोग को स्पष्ट करते हैं।"
    ),
    (
        "सबसे लंबे हड़प्पा अभिलेख के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सबसे लंबा एकल लेख एक तीन तरफा सेलखड़ी की छड़ी पर मिला है जिसमें 26 चिन्ह हैं।\n2. किसी भी मुहर, फलक या बर्तन पर 50 से अधिक चिन्हों का कोई लंबा लेख नहीं मिला है।\n3. लंबे लेखों की कमी के कारण भाषा के व्याकरणिक विश्लेषण का कार्य अत्यंत कठिन हो गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और 26 चिन्हों के लेख, लंबे लेखों की कमी और व्याकरणिक रुकावट को स्पष्ट करते हैं।"
    ),
    (
        "समय के साथ सिंधु लिपि के रूपों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लिपि अपने 700 वर्षों के परिपक्व चरण में लगभग स्थिर रही और इसमें कोई बड़ा क्रमिक विकास नहीं दिखा।\n2. पंजाब और गुजरात के लेखकों ने बिल्कुल एक समान चिन्ह सूची का उपयोग किया, जो केंद्रीय मानकों को दर्शाता है।\n3. उत्तर हड़प्पा काल में मुहरों की गुणवत्ता में गिरावट आई और लिपि धीरे-धीरे लुप्त हो गई।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो लिपि की स्थिरता, एक समान चिन्हों और अंतिम चरण में इसके लुप्त होने को दर्शाते हैं।"
    ),
    (
        "ऋग्वेद और हड़प्पा भाषा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ऋग्वेद में कई ऐसे शब्द हैं जो भारत-आर्य मूल के नहीं हैं और उन्हें आदि-द्रविड़ ऋण-शब्द माना गया है।\n2. यह भाषाई परत संकेत करती है कि ऋग्वेद के कवियों का संपर्क सिंधु घाटी में द्रविड़ भाषी लोगों से हुआ था।\n3. ऋग्वेद में सीधे तौर पर मेलुहा के लोगों की बोउस्ट्रोफेडन लेखन शैली का वर्णन मिलता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि ऋग्वेद एक मौखिक ग्रंथ है जिसमें हड़प्पा लिपि या लेखन शैली का कोई विवरण नहीं है।"
    ),
    (
        "मछली के चिन्ह को *मीन* पढ़ने के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आदि-द्रविड़ भाषा में मछली के लिए शब्द *मीन* (min) था।\n2. द्रविड़ भाषाओं में *मीन* शब्द का एक समध्वनि शब्द 'तारा' या 'चमकना' भी है।\n3. इस समध्वनि शब्द का उपयोग मुहरों पर मछली के चिन्हों को तारों या खगोलीय देवताओं के रूप में पढ़ने के लिए किया जाता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और द्रविड़ अनुवाद पहेली के भाषाई आधार को स्पष्ट करते हैं।"
    ),
    (
        "मिट्टी के बर्तनों पर लेखन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पकाने के बाद अक्षरों को नुकीले पत्थरों (burins) से खरोंचकर लिखा जाता था।\n2. हड़प्पा से प्राप्त बर्तनों पर क्रम संख्याएँ मिली हैं जो माल के भेजने की गिनती दर्शाती हैं।\n3. बर्तनों पर लेख कोयले और मवेशियों की चर्बी से बनी स्याही से लिखे जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि बर्तनों पर लेख खरोंचकर लिखे जाते थे, स्याही से पेंट करने का कोई पुरातात्विक साक्ष्य नहीं है।"
    ),
    (
        "धोलावीरा के सूचना-पट्ट के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह लकड़ी का बोर्ड किले के महल के प्रवेश द्वार के ऊपर लगाया गया था।\n2. इसके जिप्सम के अक्षर आधुनिक प्रसंस्कृत प्लास्टर ऑफ पेरिस से बने हैं।\n3. यह सार्वजनिक साक्षरता और नागरिक सत्ता का एक भव्य प्रदर्शन था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि अक्षर प्राकृतिक जिप्सम लेप (calcium sulfate) से बने थे, न कि आधुनिक प्लास्टर ऑफ पेरिस से।"
    ),
    (
        "एस.आर. राव के वर्णमाला अनुवाद के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उन्होंने अक्षरों को मानक दिशा के विपरीत बाएं से दाएं पढ़ा।\n2. उन्होंने लेखों का अनुवाद *अक*, *राम* और *सद* जैसे वैदिक संस्कृत नामों के रूप में किया।\n3. उनके इस अनुवाद को ध्वनि मानों में निरंतरता की कमी के कारण खारिज कर दिया गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। एस.आर. राव ने अक्षरों को सेमिटिक मान देकर संस्कृत शब्द निकाले थे, जिसे भाषाविदों ने मनमाना मानकर अस्वीकार कर दिया।"
    ),
    (
        "बाईं ओर अक्षरों के सिकुड़ने (cramping) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखकों ने मुहर के आकार का गलत अनुमान लगाया और अंत में बाईं ओर अक्षरों को सटा दिया।\n2. यह संकुचन दर्शाता है कि मुहरों को सीधे पढ़ा जाता था, न कि उन्हें मिट्टी पर छापने के लिए बनाया गया था।\n3. अक्षरों का संकुचन केवल तांबे के फलकों पर देखा गया है और सेलखड़ी मुहरों पर अनुपस्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहर का संकुचन छाप लगाने पर सही सीधा पढ़ा जाता था। कथन 3 गलत है क्योंकि संकुचन सेलखड़ी मुहरों पर भी आम है।"
    ),
    (
        "हाथीदांत की शलाकाओं पर लेखन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इन शलाकाओं पर संक्षिप्त लेखों के साथ ज्यामितीय ग्रिड के निशान भी मिले हैं।\n2. इनका उपयोग प्रशासनिक गणना, पासा खेल या बुनाई के औजारों के रूप में होता था।\n3. हाथीदांत की इन शलाकाओं का निर्यात मिस्र के फिरौन की कब्रों में किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मिस्र की कब्रों में हड़प्पा के हाथीदांत के पैमाने मिलने का कोई साक्ष्य नहीं है।"
    ),
    (
        "अपठित लिपि के भारतीय इतिहास पर प्रभाव के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह हमें यह सत्यापित करने से रोकता है कि क्या ऋग्वेद के रचयिता हड़प्पा के ही नागरिक थे।\n2. यह सिंधु घाटी और गंगा घाटी की सभ्यताओं के बीच के संक्रमण को अत्यधिक विवादित बनाए रखता है।\n3. इस लिपि को पढ़ने से भारत के प्रारंभिक शहरीकरण की भाषाई जड़ें पूरी तरह स्पष्ट हो जाएंगी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और लिपि के अपठित होने के कारण भारतीय इतिहास में बने विवादों को स्पष्ट करते हैं।"
    ),
    (
        "अक्षरों के संशोधन तंत्र (sign modification) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखक मूल अक्षरों के साथ छोटे स्ट्रोक, बिंदु या तिरछी रेखाएँ जोड़कर उनके मान बदलते थे।\n2. ये संशोधित चिन्ह ऐतिहासिक भारतीय लिपियों में प्रयुक्त होने वाली मात्राओं (matras) की तरह व्यवहार करते हैं।\n3. यह संशोधन प्रणाली एक सुव्यवस्थित ध्वन्यात्मक नियमों और लेखन मानकों को दर्शाती है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो अक्षरों के संशोधन, मात्राओं की समानता और ध्वन्यात्मक संरचना का विवरण देते हैं।"
    ),
    (
        "मछली चिन्ह के ग्रह-नक्षत्रों से जुड़े होने के मत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आस्को पारपोला का तर्क था कि मछली प्रतीक (*मीन*) वास्तव में तारों या ग्रहों का प्रतिनिधित्व करता था।\n2. ऊपर छत के आकार के चिन्ह वाली मछली को *वेल्ली-मीन* (शुक्र तारा) के रूप में पढ़ा गया।\n3. एस.आर. राव ने सेमिटिक तुलना के आधार पर मछली के चिन्ह को केवल *म* (ma) वर्णमाला मान दिया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और पारपोला के ग्रह अनुवाद व राव के वर्णमाला अनुवाद मत को दर्शाते हैं।"
    ),
    (
        "भंडारण बर्तनों (storage jars) पर लेखों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. काले रंग के बड़े भंडारण जारों पर गहरे खुदे हुए लिपि चिन्ह मिले हैं।\n2. इन बर्तनों का उपयोग ओमान और फारस की खाड़ी के क्षेत्रों में वस्तुओं के निर्यात के लिए होता था।\n3. ये खुदे हुए चिन्ह संभवतः निर्यातक की मुहर, अंदर रखी सामग्री या वजन को दर्शाते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और ओमान से प्राप्त बड़े निर्यात बर्तनों, उन पर अंकित लेखों और उनके कार्यों का विवरण देते हैं।"
    )
]

# Mock Test Questions (10 Qs)
mock_data_eng = [
    (
        "Consider the following statements regarding the writing direction of the Harappan script:\n1. Scribes primarily wrote from right to left, proven by the cramping of symbols on the left of seals.\n2. In longer inscriptions, they wrote in Boustrophedon direction, alternating lines from right-to-left and left-to-right.\n3. The Boustrophedon writing style is completely unique to India and is absent in European antiquities.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Boustrophedon is a Greek term meaning 'ox-turning' and was used in early Greek and Sabaean inscriptions."
    ),
    (
        "With reference to the logo-syllabic nature of the script, consider the following statements:\n1. The script contains between 375 and 400 distinct signs, proving it is not alphabetical.\n2. Each sign represents either a whole word (logogram) or a syllable sound.\n3. The undeciphered status of the script leaves the spoken language of the IVC unknown.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, describing the logo-syllabic sign count, syllables, and language implications of the undeciphered script."
    ),
    (
        "Consider the following statements regarding S.R. Rao's Sanskrit decipherment:\n1. He read the signs alphabetically by assigning Semitic phonetic values to them.\n2. S.R. Rao's Sanskrit readings have been widely accepted by the Linguistic Society of India.\n3. His translations read Vedic Sanskrit words like 'Rama', 'Aka', and 'Sada' on trade seals.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1, 2 and 3", "2 and 3 only", "2 only"],
        0,
        "Statements 1 and 3 are correct. Statement 2 is incorrect: S.R. Rao's decipherment has been rejected by most linguists due to arbitrary sign assignments and lack of grammatical coherence."
    ),
    (
        "With reference to the Dravidian theory of the Harappan language, consider the following statements:\n1. Linguist Asko Parpola argued that the language belongs to the Proto-Dravidian family.\n2. Scribes used the rebus principle, reading the fish sign (*min*) as star/planet (*min*).\n3. This theory has been universally proven and accepted as the final decipherment key.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: the Proto-Dravidian reading remains a strong hypothesis but is not universally accepted or proven."
    ),
    (
        "Consider the following statements regarding the Dholavira Signboard:\n1. It features ten large symbols made of white crystalline gypsum paste.\n2. Scribes mounted the characters on a wooden board over the northern gate of the Citadel.\n3. It represents a public notification of civic or administrative authority.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and define the material, location, and administrative significance of the Dholavira signboard."
    ),
    (
        "With reference to the non-linguistic symbol theory of Farmer, Sproat, and Witzel, consider the following statements:\n1. They argued that the Indus script did not encode a spoken language.\n2. The extreme brevity of inscriptions (average of 5 signs) supports this theory.\n3. They suggested the signs served as heraldic emblems, clan symbols, or ritual codes.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the key arguments and symbol explanations of the non-linguistic theory."
    ),
    (
        "Consider the following statements regarding the physical writing media:\n1. Steatite seals and clay pottery graffiti carry the largest volume of script signs.\n2. Large copper plates and small copper tablets also feature script engravings.\n3. Paper-like materials made of papyrus have been excavated from Mohenjo-daro houses.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: papyrus was used in ancient Egypt, and no such paper-like organic writing sheets have survived in the Indus Valley."
    ),
    (
        "With reference to the sign modification system, consider the following statements:\n1. Scribes added auxiliary strokes, dots, and lines to main signs to change their meaning.\n2. The modification behaves similarly to the vowel markings (*matras*) in historical Indian scripts.\n3. This systematic modification suggests a highly structured script convention.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct, outlining the sign modifiers, matra-like behavior, and structured script conventions."
    ),
    (
        "Consider the following statements regarding the longest Indus text:\n1. The longest single inscription contains 26 signs on a three-sided steatite baton.\n2. No text has been recovered that exceeds 50 signs, suggesting a lack of long narrative literature.\n3. The brevity of texts makes it difficult to verify grammar, syntax, or word order.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, detailing the 26-sign record, lack of narrative texts, and grammatical analysis blocks."
    ),
    (
        "With reference to the fish symbol variants in Parpola's Dravidian readings, consider the following statements:\n1. The modified fish with a roof was read as *Velli-min* (Venus/White Star).\n2. The modified fish with a diagonal stroke was read as *Paci-min* (Green Star/Mercury).\n3. These readings provide a coherent model of Harappan astronomical calendars.",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct and represent Parpola's reconstructed astronomic readings based on Dravidian homophones."
    )
]

mock_data_hin = [
    (
        "हड़प्पा लिपि की लेखन दिशा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखक मुख्य रूप से दाएं से बाएं लिखते थे, जैसा कि मुहरों के बाएं किनारे पर अक्षरों के सिकुड़ने से सिद्ध होता है।\n2. लंबे लेखों में वे बोउस्ट्रोफेडन शैली का उपयोग करते थे, जिसमें पहली पंक्ति दाएं से बाएं और दूसरी बाएं से दाएं होती थी।\n3. बोउस्ट्रोफेडन लेखन शैली पूरी तरह से भारत की अनूठी विशेषता है और यह यूरोपीय इतिहास में अनुपस्थित है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है: बोउस्ट्रोफेडन ग्रीक शब्द है जिसका अर्थ 'बैल का मुड़ना' है और यह प्रारंभिक यूनानी व सबाई अभिलेखों में प्रयुक्त होती थी।"
    ),
    (
        "लिपि के लोगो-सिलेबिक स्वरूप के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस लिपि में 375 से 400 तक विशिष्ट चिन्ह हैं, जो सिद्ध करता है कि यह वर्णमाला नहीं है।\n2. प्रत्येक चिन्ह पूरे शब्द (logogram) या शब्दांश ध्वनि (syllable) का प्रतिनिधित्व करता है।\n3. लिपि के अपठित होने के कारण सिंधु सभ्यता के लोगों की बोली जाने वाली भाषा आज भी अज्ञात है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो चिन्हों की संख्या, ध्वनि प्रतिनिधित्व और लिपि के अपठित होने के भाषाई प्रभाव का वर्णन करते हैं।"
    ),
    (
        "एस.आर. राव के संस्कृत अनुवाद सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उन्होंने चिन्हों को वर्णमाला के रूप में पढ़ा और उन्हें सेमिटिक ध्वन्यात्मक मान दिए।\n2. एस.आर. राव के इस संस्कृत अनुवाद को भारतीय भाषा विज्ञान परिषद (LSI) द्वारा व्यापक रूप से स्वीकार किया गया है।\n3. उनके अनुवाद में मुहरों पर 'राम', 'अक' और 'सद' जैसे वैदिक संस्कृत शब्द पढ़े गए हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 3", "1, 2 और 3", "केवल 2 और 3", "केवल 2"],
        0,
        "कथन 1 और 3 सही हैं। कथन 2 गलत है क्योंकि अधिकांश भाषाविदों ने एस.आर. राव के मनमाने ध्वनि मानों के कारण उनके अनुवाद को खारिज कर दिया है।"
    ),
    (
        "हड़प्पा भाषा के द्रविड़ सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. भाषाविद् आस्को पारपोला ने तर्क दिया कि यह भाषा आदि-द्रविड़ (Proto-Dravidian) परिवार से संबंधित थी।\n2. लेखकों ने रिबस सिद्धांत (rebus principle) का उपयोग किया, जहाँ मछली चिन्ह (*मीन*) को तारा/ग्रह (*मीन*) के रूप में पढ़ा जाता है।\n3. यह सिद्धांत सार्वभौमिक रूप से प्रमाणित हो चुका है और इसे अंतिम अनुवाद कुंजी माना गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि आदि-द्रविड़ अनुवाद आज भी केवल एक मजबूत परिकल्पना है, अंतिम रूप से प्रमाणित सिद्धांत नहीं।"
    ),
    (
        "धोलावीरा के सूचना-पट्ट (Signboard) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें सफेद क्रिस्टलीय जिप्सम लेप से बने दस बड़े प्रतीक शामिल हैं।\n2. इन अक्षरों को लकड़ी के बोर्ड पर लगाकर किले के उत्तरी द्वार के ऊपर टांगा गया था।\n3. यह नागरिक या प्रशासनिक सत्ता की सार्वजनिक घोषणा का प्रतिनिधित्व करता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और धोलावीरा सूचना-पट्ट के जिप्सम अक्षरों, उसकी स्थिति और नागरिक महत्व को स्पष्ट करते हैं।"
    ),
    (
        "फार्मर, स्प्रोट और विटजेल के गैर-भाषाई प्रतीक सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उन्होंने तर्क दिया कि सिंधु लिपि किसी बोली जाने वाली भाषा को कोड नहीं करती थी।\n2. लेखों की अत्यधिक संक्षिप्तता (औसत 5 चिन्ह) इस सिद्धांत का समर्थन करती है।\n3. उन्होंने सुझाव दिया कि ये चिन्ह कुल प्रतीकों, राजकीय चिह्नों या धार्मिक कोडों का काम करते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो गैर-भाषाई प्रतीकवाद के मुख्य तर्कों और प्रतीक अर्थों को स्पष्ट करते हैं।"
    ),
    (
        "लेखन के भौतिक माध्यमों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी की मुहरों और मिट्टी के बर्तनों पर सबसे अधिक मात्रा में लिपि चिन्ह मिले हैं।\n2. तांबे के बड़े फलकों और छोटी पट्टियों पर भी लिपि उकेरी गई मिली है।\n3. मोहनजोदड़ो के घरों से पेपिरस (papyrus) से बनी कागज जैसी शीट्स उत्खनित की गई हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["केवल 1 और 2", "केवल 1", "केवल 2 और 3", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि पेपिरस का उपयोग प्राचीन मिस्र में होता था, सिंधु घाटी में ऐसी कोई लेखन शीट्स नहीं मिली हैं।"
    ),
    (
        "अक्षरों के संशोधन तंत्र (sign modifiers) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लेखक मूल अक्षरों के साथ छोटे स्ट्रोक, बिंदु और रेखाएँ जोड़कर उनके अर्थ बदलते थे।\n2. यह संशोधन ऐतिहासिक भारतीय लिपियों में प्रयुक्त होने वाली मात्राओं (matras) की तरह व्यवहार करता है।\n3. यह व्यवस्थित संशोधन दर्शाता है कि लिपि के कड़े नियम और मानक थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो अक्षरों के संशोधनों, मात्राओं की समानता और कड़े लिपि नियमों को स्पष्ट करते हैं।"
    ),
    (
        "सबसे लंबे सिंधु लेख के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सबसे लंबा एकल लेख एक तीन तरफा सेलखड़ी की छड़ी पर मिला है जिसमें 26 चिन्ह हैं।\n2. कोई भी ऐसा लेख नहीं मिला है जिसमें 50 से अधिक चिन्ह हों, जो लंबे साहित्यिक आख्यानों के अभाव को दर्शाता है।\n3. लेखों की इस संक्षिप्तता के कारण भाषा के व्याकरण, वाक्य विन्यास या शब्दों के क्रम को जाँचना कठिन है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं, जो 26 चिन्हों के लेख, साहित्यिक आख्यानों के अभाव और व्याकरणिक बाधाओं का विवरण देते हैं।"
    ),
    (
        "पारपोला के द्रविड़ अनुवाद में मछली प्रतीक के विभिन्न रूपों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ऊपर छत वाली संशोधित मछली को *वेल्ली-मीन* (शुक्र ग्रह/सफेद तारा) पढ़ा गया।\n2. तिरछी रेखा वाली संशोधित मछली को *पच्ची-मीन* (बुध ग्रह/हरा तारा) पढ़ा गया।\n3. ये अनुवाद हड़प्पा वासियों के खगोलीय पंचांग (astronomical calendar) का एक सुसंगत मॉडल प्रस्तुत करते हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        0,
        "तीनों कथन सही हैं और पारपोला द्वारा द्रविड़ समध्वनियों के आधार पर किए गए ग्रहों के अनुवाद को स्पष्ट करते हैं।"
    )
]

# Write Practice Questions
for item in practice_data_eng:
    eng_data["practiceQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

for item in practice_data_hin:
    hin_data["practiceQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

# Write Mock Test Questions
for item in mock_data_eng:
    eng_data["mockTestQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

for item in mock_data_hin:
    hin_data["mockTestQuestions"].append({
        "q": item[0],
        "opts": item[1],
        "ans": item[2],
        "sol": item[3]
    })

# Save JSON Files (Without Mastery Zone Questions for now)
with open(os.path.join(ENG_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(HIN_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Script Base JSON files built successfully!")
