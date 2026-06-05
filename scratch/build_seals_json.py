import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Seals-and-Images"
HIN_DIR = os.path.join(ENG_DIR, "hi")
os.makedirs(HIN_DIR, exist_ok=True)

# English base structure
eng_data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Seals and Images"
    },
    "hero": {
        "title": "Seals, Sculptures & Images of the Indus Valley Civilisation",
        "description": "Master the metallurgical achievements, steatite seal technologies, stone sculpture forms, and terracotta traditions of the Harappan Civilisation for UPSC GS-1."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Evaluate your understanding of Harappan seals, stone/bronze sculptures, terracottas, and painted pottery. This timed test contains 10 high-yield, exam-standard questions with negative marking.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Technological & Artistic Evolution",
        "description": "Track the evolution of engraving, metallurgy, stone carving, and pottery painted motifs across the Harappan periods.",
        "cards": [
            {
                "period": "Glyptic Art & Seal Craft",
                "date": "Steatite Carving & Glazing",
                "details": "High-precision engraving of intaglio animal forms and undeciphered script on soft steatite, fired to create white glazed enstatite seals."
            },
            {
                "period": "Metallurgy & Stone Carving",
                "date": "Lost-Wax Casting & Sandstone Modular Sculptures",
                "details": "Development of lost-wax bronze casting (Dancing Girl) and highly naturalistic stone carvings (Priest-King, male sandstone torso with socket attachments)."
            },
            {
                "period": "Domestic Terracotta & Pottery",
                "date": "Hand-Modeled Clay & Wheel-Made Painted Ware",
                "details": "Mass production of hand-modeled terracotta toys and fertility figurines, alongside standard red-and-black painted pottery with geometric/nature motifs."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Use these visual memory hooks to retain critical facts about Harappan seals, sculptures, and art locations.",
        "items": [
            {
                "title": "Mnemonic 1: Priest-King Sculpture Details",
                "phrase": "\"Be-Tre-Fil-A (Bearded, Trefoil shawl, Fillet headband, Armlet)\"",
                "decryption": "Remember the key iconographic elements of the steatite Priest-King: **Be**arded face (shaved upper lip), **Tre**foil patterned shawl, **Fil**let (headband) with a central disc, and **A**rmlet on the right arm."
            },
            {
                "title": "Mnemonic 2: Dancing Girl Characteristics",
                "phrase": "\"Mo-Tri-Ban-Wax (Mohenjo-daro, Tribhanga, Bangles, Lost-Wax)\"",
                "decryption": "The Dancing Girl is from **Mo**henjo-daro, is depicted in the **Tri**bhanga (triple-bend) posture, has her left arm loaded with **Ban**gles (24-25 bangles), and was cast using the Lost-**Wax** (cire perdue) process."
            },
            {
                "title": "Mnemonic 3: Modular Male Torso Site",
                "phrase": "\"Red-Torso-Ha (Red Sandstone Torso from Harappa)\"",
                "decryption": "The naturalistic **Red** sandstone male **Torso** with socket holes for detachable limbs was excavated at **Ha**rappa (not Mohenjo-daro)."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Use these active recall cards to reinforce technical details of Harappan art and crafts.",
        "items": [
            {
                "question": "What chemical transformation occurs when a steatite seal is fired in a kiln?",
                "answer": "Firing converts the soft mineral <strong>steatite (talc)</strong> into a much harder, durable silicate mineral called <strong>enstatite</strong>, creating a glossy white glazed surface.",
                "icon": "fa-fire-burner"
            },
            {
                "question": "Which metallurgical technique was used to cast the bronze 'Dancing Girl' of Mohenjo-daro?",
                "answer": "The <strong>'Lost-Wax' casting technique</strong> (also known as <strong>cire perdue</strong>), where a clay mold is created around a wax model, the wax is melted out, and molten bronze is poured in.",
                "icon": "fa-flask-pot"
            },
            {
                "question": "Describe the distinct features of the Priest-King shawl decoration.",
                "answer": "The shawl is draped over the left shoulder and carved with a <strong>trefoil pattern</strong> (three-lobed clover design), which was originally filled with a <strong>red pigment</strong>.",
                "icon": "fa-shirt"
            },
            {
                "question": "What unique design element is found on the red sandstone male torso from Harappa?",
                "answer": "It features <strong>socket holes</strong> at the neck and shoulders, indicating that the head and arms were made separately and attached as <strong>detachable parts</strong>.",
                "icon": "fa-puzzle-piece"
            },
            {
                "question": "What pigment combination characterizes standard Harappan painted pottery?",
                "answer": "A <strong>red slip (iron oxide)</strong> was applied as the background base, and designs were painted over it using a <strong>black pigment (manganese dioxide)</strong>.",
                "icon": "fa-paint-brush"
            }
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the materials, processes, iconography, and functions of Harappan glyptic and plastic arts for UPSC GS-1.",
        "sections": [
            {
                "title": "1. Harappan Seals & Copper Tablets",
                "content": """<p>Harappan glyptic art is represented by thousands of small seals and copper tablets, serving commercial, administrative, and ritual purposes.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-stamp"></i> Seal Materiality & Firing Technology</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Composition:</strong> Most seals are made of soft talcose soapstone known as <strong>steatite</strong>. Terracotta, chert, agate, copper, and faience seals also exist.</li>
      <li><strong>Kiln Firing:</strong> Firing the carved steatite seal at high temperatures (above 900°C) dehydrated the talc, converting it into a harder enstatite mineral phase and producing a durable, glazed white surface.</li>
      <li><strong>Anatomy:</strong> Square or rectangular (typically 2x2 to 5x5 cm). The reverse features a raised boss (button) pierced with a suspension hole to run a carrying cord.</li>
      <li><strong>Iconography:</strong> Features animal motifs (primarily the Unicorn before a censer standard, humped bull, tiger, elephant, rhino) and brief inscriptions. Engravings are in <strong>intaglio</strong> (carved into the surface), so they leave a raised positive impression on clay.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-boxes-packing"></i> Functions of Seals & Copper Tablets</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>Trade & Verification:</strong> Seals were pressed onto wet clay tags (sealings) tied over trade package knots. A matching sealing proved that the cargo arrived untampered and verified the merchant's identity/guild.
      <br><strong>Social Markers:</strong> Carried as personal signatures, status symbols, or administrative credentials of elite traders and officials.
      <br><strong>Amulets & Tablets:</strong> Many seals and copper tablets (flat rectangular pieces showing a deity/animal on one side and text on the reverse) were worn as protective amulets to ward off evil.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. Stone and Bronze Sculptures",
                "content": """<p>The plastic arts of the Indus Valley Civilisation exhibit an advanced understanding of metal casting and highly realistic stone carving.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-person-dress"></i> Bronze Metallurgy & Lost-Wax Casting</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Cire Perdue (Lost-Wax):</strong> The primary method for metal casting. A wax model was covered in clay, heated to drain the melted wax, and filled with molten copper-tin bronze. The clay shell was broken after cooling.</li>
      <li><strong>The Dancing Girl:</strong> Found at Mohenjo-daro, this 10.5 cm bronze figurine depicts a young woman standing in a relaxed, rhythmic <em>tribhanga</em> (triple-bend) pose. Her right hand rests on her hip, and her left arm is completely covered in 24 to 25 bangles, holding a small bowl.</li>
      <li><strong>Other Bronzes:</strong> Realistic cast bronze bulls (from Kalibangan) and dogs reflect acute observation of animal forms.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-monument"></i> Steatite Priest-King & Modular Sandstone Torso</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>Priest-King Bust:</strong> A 17.5 cm high steatite bust discovered at Mohenjo-daro. Features half-closed, meditative eyes (possibly inlaid with shell), a neatly trimmed beard, a shaved upper lip, and a shawl draped over the left shoulder decorated with a trefoil pattern (originally inlaid with red paste). He wears a circular headband (fillet) and a matching right-armlet.
      <br><strong>Red Sandstone Torso:</strong> Excavated at Harappa, this small male torso is carved with astonishing anatomical realism, showing abdominal musculature. It features drilled socket holes at the neck and shoulders for attaching a detachable head and arms.
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. Terracotta Figurines & Painted Pottery",
                "content": """<p>Terracotta figurines and standardized painted wheel-made pottery represent the popular domestic arts of Harappan society.</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-baby-carriage"></i> Terracotta Artistry & Domestic Cults</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>Manufacturing:</strong> Mostly hand-modeled using the pinching technique. Details like hair, jewelry, and belts were added using clay strips (appliqué method) before baking.</li>
      <li><strong>Mother Goddess:</strong> Standing female figurines with fan-shaped headdresses containing cup-like panniers. Soot stains inside these cups indicate their use in household incense or oil lamp rituals.</li>
      <li><strong>Playful Toys:</strong> Toy carts with clay wheels, terracotta bulls with movable heads controlled by strings, sliding clay monkeys, whistles shaped like birds, and rattles.</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-wine-glass"></i> Standardized Black-on-Red Pottery</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>Pottery Technology:</strong> Sturdy wheel-made pottery baked in updraft kilns. The base is coated with a bright red iron-oxide slip, over which designs are painted in black manganese-based pigment.
      <br><strong>Motifs:</strong> Geometric (intersecting circles, checkers), vegetal (Pipal leaf, palm trees), zoomorphic (birds, fish, deer), and fish-scale patterns.
      <br><strong>Special Forms:</strong> Tall storage jars, offering stands, and perforated cylindrical vessels (likely used for straining beverages or burning incense).
    </p>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "traps": {
        "title": "UPSC Warning Alerts (Traps to Avoid)",
        "items": [
            "<strong>Trap 1:</strong> Do not assume Harappan seals were used as a form of currency or coins. They were strictly commercial security tags, administrative markers, and amulets. Copper tablets were also tokens/amulets, not currency.",
            "<strong>Trap 2:</strong> Watch out for statements claiming the Priest-King bust is made of bronze or terracotta. It is carved from <strong>steatite (soapstone)</strong>. Conversely, the Dancing Girl is made of <strong>bronze</strong>, not stone.",
            "<strong>Trap 3:</strong> The naturalistic red sandstone male torso with socket holes was found at <strong>Harappa</strong>, not Mohenjo-daro. The Priest-King and Dancing Girl were both found at <strong>Mohenjo-daro</strong>.",
            "<strong>Trap 4:</strong> Terracotta figurines were NOT cast in molds. They were entirely hand-modeled (pinching and appliqué methods). Only metal bronzes used mold-based lost-wax casting.",
            "<strong>Trap 5:</strong> Iron was completely unknown to the Harappans. Do not select options that list iron tools or iron backing in seal manufacturing."
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
        "current": "मुहरें और मूर्तियाँ"
    },
    "hero": {
        "title": "सिंधु घाटी सभ्यता की मुहरें, मूर्तियाँ और कलाकृतियाँ",
        "description": "यूपीएससी परीक्षा (GS-1) के लिए हड़प्पा सभ्यता की धातु ढलाई तकनीक, सेलखड़ी की मुहरों, प्रस्तर मूर्तियों और मिट्टी के बर्तनों की विशेषताओं का अध्ययन करें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव परीक्षा मॉक टेस्ट",
            "description": "हड़प्पा सभ्यता की मुहरों, प्रस्तर व कांस्य मूर्तियों, मिट्टी के खिलौनों और बर्तनों के संबंध में अपनी तैयारी का मूल्यांकन करें। इस समयबद्ध परीक्षण में 10 उच्च-स्तरीय यूपीएससी मानक के प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "कलात्मक और तकनीकी विकास",
        "description": "हड़प्पा काल में नक्काशी, धातु कर्म, पत्थर की तराशी और बर्तनों पर चित्रकारी के क्रमिक विकास को समझें।",
        "cards": [
            {
                "period": "मुहर कला और उत्कीर्णन",
                "date": "सेलखड़ी की नक्काशी और चमकाना",
                "details": "मुलायम सेलखड़ी पत्थर पर पशुओं की आकृतियों और अपठित सिंधु लिपि का बारीक अंकन, जिसे भट्टी में पकाकर सफेद चमकीली मुहरें बनाई जाती थीं।"
            },
            {
                "period": "धातु कर्म और प्रस्तर कला",
                "date": "लुप्त मोम ढलाई और जोड़दार प्रस्तर मूर्तियाँ",
                "details": "कांस्य ढलाई की 'लुप्त मोम' (Lost-Wax) तकनीक का विकास (नर्तकी) और अत्यधिक यथार्थवादी पत्थर की मूर्तियाँ (पुरोहित राजा, अलग होने वाले अंगों वाले जोड़दार धड़)।"
            },
            {
                "period": "घरेलू मिट्टी की मूर्तियाँ और मृदभांड",
                "date": "हाथ से निर्मित खिलौने और चक्र-निर्मित चित्रित बर्तन",
                "details": "हाथ से गढ़ी मिट्टी के खिलौनों व मातृदेवी की मूर्तियों का व्यापक निर्माण, साथ ही काले रेखाचित्रों से सजे मानक लाल मृदभांडों का प्रचलन।"
            }
        ]
    },
    "mnemonics": {
        "title": "याद रखने के सूत्र (Mnemonics)",
        "description": "यूपीएससी परीक्षा के लिए हड़प्पा कला और मूर्तियों की विशेषताओं को आसानी से याद रखने के लिए इन सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "याद रखने का सूत्र 1: पुरोहित राजा (Priest-King) की विशेषताएं",
                "phrase": "\"दा-ति-बा-बा (दाढ़ी, तिपतिया शाल, बाजूबंद, पट्टीदार सिर)\"",
                "decryption": "सेलखड़ी के पुरोहित राजा की पहचान: घनी **दा**ढ़ी (मूंछ साफ), **ति**पतिया पैटर्न वाली शाल, दाहिनी बांह पर **बा**जूबंद, और सिर पर गोल **बा**ंधने वाली पट्टी।"
            },
            {
                "title": "याद रखने का सूत्र 2: कांस्य नर्तकी (Dancing Girl) के साक्ष्य",
                "phrase": "\"मो-त्रि-का-मो (मोहनजोदड़ो, त्रिभंग मुद्रा, कांस्य, मोम ढलाई)\"",
                "decryption": "कांस्य नर्तकी की मूर्ति **मो**हनजोदड़ो से मिली है, वह **त्रि**भंग मुद्रा में है, **का**ंस्य से निर्मित है और लुप्त **मो**म तकनीक (cire perdue) से ढाली गई है।"
            },
            {
                "title": "याद रखने का सूत्र 3: लाल बलुआ पत्थर का धड़",
                "phrase": "\"लाल-धड़-हड़ (लाल बलुआ पत्थर का धड़ हड़प्पा से)\"",
                "decryption": "अंगों को जोड़ने के लिए सॉकेट छेद वाला अत्यंत यथार्थवादी **लाल** बलुआ पत्थर का **धड़** **हड़**प्पा से मिला है (मोहनजोदड़ो से नहीं)।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
        "description": "हड़प्पा कालीन कला और शिल्प के तकनीकी तथ्यों को याद रखने के लिए इन फ्लैशकार्ड्स का उपयोग करें। उत्तर देखने के लिए नीचे दिए गए कार्ड्स पर क्लिक करें।",
        "items": [
            {
                "question": "सेलखड़ी (Steatite) की मुहरों को भट्टी में पकाने पर कौन सा रासायनिक परिवर्तन होता था?",
                "answer": "भट्टी में पकाने से मुलायम खनिज <strong>सेलखड़ी (talc)</strong> निर्जलीकृत होकर एक अत्यंत कठोर सिलिकेट खनिज <strong>एन्सटाइट (enstatite)</strong> में बदल जाता था, जिससे मुहर को सफेद और टिकाऊ glazed सतह मिलती थी।",
                "icon": "fa-fire-burner"
            },
            {
                "question": "मोहनजोदड़ो की कांस्य 'नर्तकी' को ढालने के लिए किस तकनीकी विधि का उपयोग किया गया था?",
                "answer": "<strong>'लुप्त मोम' ढलाई तकनीक</strong> (जिसे <strong>cire perdue</strong> या Lost-Wax भी कहा जाता है)। इसमें मोम की मूर्ति पर मिट्टी का लेप लगाकर गर्म किया जाता था, पिघला मोम निकालकर उसमें पिघला कांसा भरा जाता था।",
                "icon": "fa-flask-pot"
            },
            {
                "question": "पुरोहित राजा (Priest-King) की शाल पर बने तिपतिया (Trefoil) अलंकरण की क्या विशेषता थी?",
                "answer": "यह शाल बाएं कंधे पर ओढ़ी गई है और इस पर <strong>तिपतिया आकार (तीन पत्तियों वाला डिज़ाइन)</strong> खुदा है, जो मूल रूप से <strong>लाल रंग के पेस्ट</strong> से भरा हुआ था।",
                "icon": "fa-shirt"
            },
            {
                "question": "हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ में कौन सी अनूठी डिजाइन विशेषता है?",
                "answer": "इसमें गर्दन और कंधों पर <strong>सॉकेट छेद (socket holes)</strong> बने हैं, जो दर्शाते हैं कि सिर और हाथ अलग से बनाकर जोड़े जाने वाले <strong>(detachable)</strong> अंग थे।",
                "icon": "fa-puzzle-piece"
            },
            {
                "question": "मानक हड़प्पा बर्तनों पर किस रंग संयोजन का उपयोग किया जाता था?",
                "answer": "बर्तन पर पृष्ठभूमि के रूप में <strong>लाल रंग का लेप (लोहा ऑक्साइड)</strong> लगाया जाता था और उसके ऊपर <strong>काले रंग (मैंगनीज ऑक्साइड)</strong> से चित्रकारी की जाती थी।",
                "icon": "fa-paint-brush"
            }
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम मुख्य नोट्स (गहन अध्ययन)",
        "description": "सिंधु घाटी सभ्यता की मुहर कला, धातु ढलाई, प्रस्तर मूर्तिकला और मिट्टी के मृदभांडों की विशेषताओं का गहन अध्ययन करें।",
        "sections": [
            {
                "title": "1. हड़प्पा की मुहरें और तांबे की पट्टिकाएं",
                "content": """<p>हड़प्पा की मुहरें और तांबे की पट्टिकाएं व्यापारिक, प्रशासनिक और व्यक्तिगत पहचान के महत्वपूर्ण माध्यम थे।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-stamp"></i> मुहर निर्माण और पकाने की तकनीक</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>सामग्री:</strong> अधिकांश मुहरें मुलायम सोपस्टोन यानी <strong>सेलखड़ी (steatite)</strong> से बनी थीं। मिट्टी, चर्ट, अगेट, तांबे और फेयॉन्स की मुहरें भी मिली हैं।</li>
      <li><strong>भट्टी में पकाना:</strong> उत्कीर्णन के बाद मुहर को उच्च तापमान (900°C से ऊपर) पर पकाया जाता था। इससे सेलखड़ी खनिज निर्जलित होकर कठोर 'एन्सटाइट' में बदल जाता था, जिससे मुहर सफेद और चमकदार हो जाती थी।</li>
      <li><strong>संरचना:</strong> चौकोर या आयताकार मुहरों के पीछे एक उभरा हुआ बटन (boss) होता था, जिसमें एक छेद होता था ताकि उन्हें धागे से बांधकर ले जाया जा सके।</li>
      <li><strong>आकृतियाँ:</strong> मुहरों पर पशुओं (एक सींग वाला Unicorn, कूबड़ वाला बैल, हाथी, बाघ) और सिंधु लिपि का अंकन होता था। उत्कीर्णन <strong>अंतर्गठित (intaglio)</strong> था, जिससे गीली मिट्टी पर उभरी हुई आकृति छपती थी।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-boxes-packing"></i> मुहरों और तांबे की पट्टिकाओं के कार्य</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>व्यापार और सुरक्षा:</strong> व्यापारिक बोरियों के मुंह पर बांधी गई गांठ पर गीली मिट्टी लगाकर उस पर मुहर दबाई जाती थी। सीलबंद गांठ यह सुनिश्चित करती थी कि रास्ते में सामान से छेड़छाड़ नहीं की गई है।
      <br><strong>पहचान और पद:</strong> व्यापारियों और अधिकारियों द्वारा व्यक्तिगत हस्ताक्षर या प्रशासनिक अधिकारों के प्रतीक के रूप में मुहरों को धारण किया जाता था।
      <br><strong>ताबीज और तांबे की पट्टियां:</strong> तांबे की सपाट पट्टियों पर एक तरफ कोई जानवर या देवता और दूसरी तरफ लेख खुदा होता था। इनका उपयोग शायद सुरक्षात्मक ताबीज के रूप में किया जाता था।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "2. प्रस्तर और कांस्य मूर्तियां",
                "content": """<p>सिंधु घाटी के शिल्पकारों को धातु विज्ञान की उच्च समझ और प्रस्तर नक्काशी में असाधारण निपुणता प्राप्त थी।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-person-dress"></i> कांस्य धातु विज्ञान और लुप्त मोम तकनीक</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>लुप्त मोम विधि (Lost-Wax/Cire Perdue):</strong> मोम की मूर्ति बनाकर उसे मिट्टी से ढका जाता था। गर्म करके पिघला मोम बाहर निकाल लिया जाता था, फिर उस खाली मिट्टी के सांचे में पिघला कांसा भरा जाता था। ठंडा होने पर मिट्टी हटा दी जाती थी।</li>
      <li><strong>कांस्य नर्तकी:</strong> मोहनजोदड़ो से प्राप्त 10.5 सेमी ऊंची यह कांस्य मूर्ति त्रिभंग मुद्रा में खड़ी एक किशोरी को दर्शाती है। उसकी बाईं बांह 24-25 चूड़ियों से भरी है, और वह हाथ में एक छोटा कटोरा लिए हुए है, जबकि उसका दायां हाथ उसकी कमर पर है।</li>
      <li><strong>पशु मूर्तियां:</strong> कालीबंगन से प्राप्त कांस्य का सांड और लोथल से प्राप्त कुत्ते की आकृतियां उनकी यथार्थवादी कला को दर्शाती हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-monument"></i> सेलखड़ी का पुरोहित राजा और जोड़दार पुरुष धड़</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>पुरोहित राजा (Priest-King):</strong> मोहनजोदड़ो से प्राप्त 17.5 सेमी ऊंची सेलखड़ी की अर्ध-प्रतिमा। इसके नेत्र आधे बंद हैं (संभवतः शंख की नक्काशी वाले), मूंछें साफ हैं लेकिन दाढ़ी करीने से संवारी हुई है। उनके बाएं कंधे पर तिपतिया डिज़ाइन (trefoil pattern) वाली शाल है, जो कभी लाल रंग से भरी थी। सिर पर उन्होंने गोल पट्टी (fillet) पहनी है।
      <br><strong>लाल बलुआ पत्थर का पुरुष धड़:</strong> हड़प्पा से प्राप्त यह छोटा धड़ मांसपेशियों के अत्यंत सजीव चित्रण को दर्शाता है। इसके गर्दन और कंधों पर सॉकेट छेद बने हैं ताकि अलग से बने सिर और हाथ जोड़े जा सकें।
    </p>
  </div>
</div>""",
                "masteryZone": []
            },
            {
                "title": "3. मिट्टी की मूर्तियां (Terracottas) और चित्रित मृदभांड",
                "content": """<p>पकी हुई मिट्टी की मूर्तियाँ (Terracottas) और चाक पर बने सुंदर लाल-काले मृदभांड हड़प्पा सभ्यता की लोकप्रिय लोक कला के उदाहरण हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-baby-carriage"></i> मिट्टी की मूर्तियां और खिलौने</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);">
      <li><strong>निर्माण विधि:</strong> अधिकांश मूर्तियां हाथ से बनाई जाती थीं, जिसमें उंगलियों से मिट्टी पिंच करने (pinching) और आभूषण व वस्त्र दर्शाने के लिए मिट्टी की पट्टियां अलग से चिपकाने (appliqué) की विधि का उपयोग होता था।</li>
      <li><strong>मातृदेवी की मूर्तियां:</strong> सिर पर पंखे जैसे मुकुट और दोनों तरफ प्यालेनुमा आकृतियां बनी होती थीं। प्यालों में मिली कालिख दर्शाती है कि इनमें धूप या दीप जलाए जाते थे।</li>
      <li><strong>खिलौने:</strong> पहियों वाली बैलगाड़ियां, धागे से हिलने वाले सिर वाले सांड, रस्सी पर सरकने वाले बंदर, पक्षी के आकार की सीटियां और झुनझुने शामिल हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-wine-glass"></i> काले और लाल मृदभांड तकनीक</div>
    <p style="font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;">
      <strong>मृदभांड निर्माण:</strong> चाक पर बने मजबूत मिट्टी के बर्तन जो भट्टियों में पकाए जाते थे। बर्तनों पर लाल रंग (लाल गेरू) का लेप लगाकर उसके ऊपर काले रंग (मैंगनीज ऑक्साइड) से चित्रकारी की जाती थी।
      <br><strong>चित्रकारी के रूप:</strong> ज्यामितीय आकृतियाँ (एक-दूसरे को काटते वृत्त, चौखाने), वनस्पति (पीपल के पत्ते, ताड़ के पेड़), पशु-पक्षी (हिरण, मछलियाँ) और मछली के शल्क (scales) का डिज़ाइन।
      <br><strong>विशिष्ट बर्तन:</strong> अनाज भंडारण के बड़े जार, छिद्रित बर्तन (perforated jars - संभवतः पेय छानने के काम आते थे) और प्याले।
    </p>
  </div>
</div>""",
                "masteryZone": []
            }
        ]
    },
    "traps": {
        "title": "यूपीएससी परीक्षा के लिए प्रमुख जाल (Traps to Avoid)",
        "items": [
            "<strong>जाल 1:</strong> यह न मानें कि हड़प्पा की मुहरों का उपयोग सिक्कों या मुद्रा के रूप में किया जाता था। वे केवल वाणिज्यिक सुरक्षा टैग, प्रशासनिक पहचान पत्र या ताबीज थीं।",
            "<strong>जाल 2:</strong> पुरोहित राजा की मूर्ति सेलखड़ी (steatite) से बनी है, न कि कांस्य या मिट्टी से। इसके विपरीत, नर्तकी कांस्य (bronze) से बनी है, पत्थर से नहीं।",
            "<strong>जाल 3:</strong> सॉकेट छेद वाला लाल बलुआ पत्थर का धड़ **हड़प्पा** से मिला था, मोहनजोदड़ो से नहीं। पुरोहित राजा और नर्तकी दोनों **मोहनजोदड़ो** से मिले थे।",
            "<strong>जाल 4:</strong> मिट्टी की मूर्तियां (terracotta) सांचे में ढालकर नहीं बनाई जाती थीं। वे हाथ से बनाई जाती थीं। केवल धातुओं के लिए सांचे वाली लुप्त मोम तकनीक का उपयोग किया जाता था।",
            "<strong>जाल 5:</strong> हड़प्पा वासियों को लोहे (iron) का कोई ज्ञान नहीं था। मुहर या कलाकृतियों के निर्माण में लोहे के औजारों के उपयोग वाले कथन हमेशा गलत होंगे।"
        ]
    },
    "practiceQuestions": [],
    "mockTestQuestions": []
}

# Define the 50 Practice Questions in English and Hindi
# Structured as tuples: (question_text, option_list, correct_option_index, explanation_text)
# We will create English and Hindi counterparts with identical options and answer keys.

# 1-15: Seals & Tablets
# 16-30: Stone & Bronze
# 31-45: Terracotta & Pottery
# 46-50: Misc & Comparative

practice_raw_eng = [
    # Q1
    (
        "Consider the following statements regarding the manufacturing of Mature Harappan seals:\n1. The vast majority of the seals were made from steatite, a soft soapstone easily carved with copper tools.\n2. Firing the seals in a kiln chemically altered the steatite, turning it into a harder enstatite mineral phase.\n3. The white, lustrous glazed finish was achieved by coating the seals in a talc-based paste prior to firing.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct. Steatite is a soft talc mineral. Firing it above 900°C converts it to enstatite (a magnesium silicate), which is much harder. Coating with a talc slip before firing gives it a white glazed finish."
    ),
    # Q2
    (
        "With reference to the physical anatomy of Harappan seals, which of the following statements is/are correct?\n1. Square seals are the most common type, featuring animal motifs along with a brief script.\n2. The reverse side of square seals is typically plain, with no carving or projections to ensure a flat stamping surface.\n3. Rectangular seals contain only script inscriptions and completely lack animal motifs.\nSelect the correct answer using the code given below:",
        ["1 only", "1 and 3 only", "2 only", "1, 2 and 3"],
        1,
        "Statements 1 and 3 are correct. Rectangular/bar seals typically carry only script and no animals. Statement 2 is incorrect: the reverse of square seals features a raised boss (button) pierced with a hole for a suspension cord."
    ),
    # Q3
    (
        "Consider the following statements regarding the functions of Harappan seals in trade and administration:\n1. Clay impressions (sealings) on knots of trade cargo secured the package and verified its origin.\n2. Seals functioned as a standardized form of state-guaranteed monetary currency in markets.\n3. The seals served as official credentials and status markers carried by merchants and administrative elites.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 3 are correct. Seals were trade tags and status markers. Statement 2 is incorrect: Harappans did not use seals as currency; their economy relied on barter and weight-regulated trade."
    ),
    # Q4
    (
        "With reference to the copper tablets discovered in the Indus Valley Civilisation, consider the following statements:\n1. They are flat, rectangular copper pieces with animal or deity motifs on one side and script on the other.\n2. Unlike steatite seals, copper tablets do not have a perforated boss on the reverse for suspension.\n3. They were discovered in large numbers at Kalibangan and Lothal but are absent at Mohenjo-daro.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Copper tablets have no reverse boss. Statement 3 is incorrect: copper tablets are highly concentrated at Mohenjo-daro and Harappa, and are rare or absent at Kalibangan and Lothal."
    ),
    # Q5
    (
        "Consider the following statements:\n1. The Unicorn is the most frequently depicted animal on Mature Harappan seals.\n2. The Unicorn is almost always depicted standing in front of a double-tiered censer or standard, interpreted as a ritual object.\n3. Seals depicting real animals like tigers and elephants are completely absent in Harappan art.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The Unicorn is the most common motif and stands before a censer standard. Statement 3 is incorrect: real animals like elephants, tigers, rhinos, and humped bulls are frequently depicted on seals."
    ),
    # Q6
    (
        "With reference to the engraving technique of Harappan seals, which of the following is correct?",
        ["Seals were carved in intaglio (sunken relief) so that they produced raised impressions on clay.", "Seals were carved in high cameo relief to print ink onto papyrus sheets.", "The inscriptions were painted with natural pigments rather than carved into the stone.", "The script was engraved from left to right exclusively on all square seals."],
        0,
        "Harappan seals were carved in intaglio (sunken relief) so that when pressed into soft clay, they left a raised positive image. Inscriptions were carved, not painted, and the script was boustrophedon (usually right to left on the seal to print left to right, or vice versa)."
    ),
    # Q7
    (
        "Consider the following statements regarding the raw materials used in Harappan seals:\n1. Steatite was the primary material, but seals were also made of terracotta, chert, agate, and copper.\n2. Faience, a synthetic glazed ceramic material made of silica and gum, was also used for making miniature seals.\n3. Iron-backed stone seals have been discovered at Dholavira, indicating advanced metallurgy.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Materials included steatite, chert, agate, terracotta, copper, and faience. Statement 3 is incorrect: iron was completely unknown to the Harappan civilization."
    ),
    # Q8
    (
        "With reference to Harappan clay sealings (seal impressions), consider the following statements:\n1. Several sealings have been found at Lothal containing impressions of cords and packing materials on their reverse.\n2. A single piece of wet clay could receive impressions from multiple different seals, indicating joint transactions.\n3. Most of the clay sealings found were baked in kilns immediately after stamping to preserve them as receipts.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Lothal sealings show cord and mat impressions. Multiple stampings on a single clay sealing indicate multiple merchants or officials. Statement 3 is incorrect: sealings were air-dried and survived because they were accidentally baked in fires that destroyed warehouses."
    ),
    # Q9
    (
        "Consider the following statements regarding the 'Pashupati Seal' of Mohenjo-daro:\n1. It is a square steatite seal depicting a seated, three-faced horned deity surrounded by animals.\n2. The script on the seal consists of a single line of six characters engraved above the horned crown.\n3. Sir John Marshall's interpretation of this figure as 'Proto-Shiva' has been fully accepted by all modern historians without dispute.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The seal depicts a seated three-faced horned figure surrounded by animals, with a short inscription above the head. Statement 3 is incorrect: Marshall's Proto-Shiva interpretation is hotly debated, with critics suggesting it represents a pre-Aryan bovine deity or animal guardian."
    ),
    # Q10
    (
        "Which of the following animal motifs is NEVER depicted on Mature Harappan seals?",
        ["Lion", "Tiger", "Rhinoceros", "Humped Bull"],
        0,
        "The lion is completely absent from Harappan seal iconography and painted pottery, whereas the tiger, rhino, elephant, humped bull, and unicorn are common."
    ),
    # Q11
    (
        "With reference to the rectangular seals of the Indus Valley Civilisation, consider the following statements:\n1. They are typically smaller than square seals and have a flat reverse without a pierced boss.\n2. They rarely depict animal motifs, carrying only script characters.\n3. They were made exclusively of copper, whereas square seals were made of steatite.\nWhich of the statements given above is/are correct?",
        ["2 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 2 is correct. Rectangular seals carry script only. Statement 1 is incorrect: rectangular seals usually have a convex reverse with a pierced hole, or are flat but not boss-less. Statement 3 is incorrect: rectangular seals were also primarily made of steatite."
    ),
    # Q12
    (
        "Consider the following statements regarding the role of seals as amulets:\n1. Many seals feature suspension holes, suggesting they were worn around the neck or arm as protective charms.\n2. Some seals depict narrative scenes of heroes fighting beasts or deities emerging from trees, suggesting mythological protection.\n3. Small, thin steatite tablets with no reverse boss were likely used as magical amulets rather than commercial stamps.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct. Suspension holes, mythological narrative depictions, and small thin tablets indicate that many seals and tablets served as protective amulets."
    ),
    # Q13
    (
        "With reference to the Indus Valley copper tablets, which of the following statements is/are correct?\n1. They feature a high degree of standardization in shape and size compared to steatite seals.\n2. The engravings on copper tablets are typically shallow and cursive, unlike the deep intaglio of steatite seals.\n3. They are believed to have been used as temple votive tokens to record cash donations.\nSelect the correct answer using the code given below:",
        ["2 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        1,
        "Statements 1 and 2 are correct. Copper tablets are highly standardized in size and shape, and their inscriptions are shallow-engraved or chased. Statement 3 is incorrect: there are no temples or cash systems in Harappan cities."
    ),
    # Q14
    (
        "Consider the following statements regarding Harappan glyptic art motifs:\n1. The humped bull (Zebu) is rendered with high artistic precision, showing pronounced humps and dewlaps.\n2. The composite animal motifs combine features of different beasts, such as a three-headed animal (bull, unicorn, ibex).\n3. Human figures are frequently depicted on seals engaged in agricultural ploughing.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The Zebu bull is rendered beautifully, and composite animals are common. Statement 3 is incorrect: human figures are rarely depicted, and scenes of agricultural ploughing are never shown on seals."
    ),
    # Q15
    (
        "With reference to the discovery of Harappan seals outside the Indus region, consider the following statements:\n1. Harappan-style square seals have been excavated at Mesopotamian sites like Kish, Ur, and Susa.\n2. Circular 'Persian Gulf' style seals found at Lothal confirm maritime trade links between the regions.\n3. The foreign seals found in the Indus Valley were made of local Indian steatite and carved by Harappan apprentices.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Square seals in Mesopotamia and Persian Gulf circular seals at Lothal prove trade. Statement 3 is incorrect: foreign seals found in the Indus were imported and made of non-local materials."
    ),

    # 16-30: Stone & Bronze
    # Q16
    (
        "Consider the following statements regarding the bronze 'Dancing Girl' of Mohenjo-daro:\n1. It is a small, 10.5 cm high bronze figurine representing a young female dancer.\n2. She is depicted standing in a relaxed pose with her right hand on her hip and left arm covered in bangles.\n3. The figure is characterized by stylized, elongated limbs and a facial expression showing self-confidence.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. The Dancing Girl is 10.5 cm tall, stands in tribhanga with her right hand on her hip and left arm loaded with bangles, and has elongated limbs and a proud facial expression."
    ),
    # Q17
    (
        "With reference to the Lost-Wax casting technique (cire perdue) used by Harappan metalworkers, consider the following statements:\n1. A solid clay model of the figure was directly coated with molten bronze in a single step.\n2. The wax model was melted and drained out of a heated clay shell, leaving a cavity for molten metal.\n3. This technique was used to cast both hollow human figurines and solid animal figures like the Kalibangan bull.\nWhich of the statements given above is/are correct?",
        ["2 and 3 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. The lost-wax process involves creating a wax model, coating it with clay, melting out the wax (hence 'lost' wax), and pouring in molten metal. Hollow castings used a clay core, while smaller animals were cast solid."
    ),
    # Q18
    (
        "Consider the following statements regarding the steatite 'Priest-King' bust from Mohenjo-daro:\n1. The figure is depicted with half-closed eyes, suggesting a meditative state of dhyana.\n2. The beard is neatly trimmed and styled, whereas the upper lip is completely shaved.\n3. A shawl decorated with a trefoil pattern is draped over his left shoulder, leaving his right arm free.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All three statements are correct, detailing the meditative pose, trimmed beard, shaved upper lip, and trefoil-patterned shawl draped over the left shoulder."
    ),
    # Q19
    (
        "With reference to the red sandstone male torso discovered at Harappa, consider the following statements:\n1. It is carved with high anatomical realism, highlighting abdominal muscles and physical volume.\n2. It features socket holes at the neck and shoulders for attaching a detachable head and arms.\n3. The sculpture is a monumental life-sized public statue placed at the gateway of the Citadel.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The red sandstone torso is small (about 9.5 cm) but shows high realism and has socket holes for detachable limbs. Statement 3 is incorrect: it is tiny and was a domestic or portable piece, not a monumental public statue."
    ),
    # Q20
    (
        "Consider the following statements regarding the bronze metallurgy of the Indus Valley Civilisation:\n1. The bronze alloy used was a mixture of copper with tin and occasionally arsenic to improve casting flow.\n2. Harappan metalware was primarily decorative, with a complete absence of bronze tools or weapons.\n3. Copper and tin ores were sourced locally from the alluvial plains of the Indus Valley.\nWhich of the statements given above is/are correct?",
        ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statement 1 is correct. Arsenic-bronze was common. Statement 2 is incorrect: they made many bronze tools like axes, chisels, saws, and fish-hooks. Statement 3 is incorrect: metals were imported; copper from Rajasthan/Oman and tin from Afghanistan."
    ),
    # Q21
    (
        "The famous bronze sculpture of a 'Charging Bull' was excavated at which Mature Harappan site?",
        ["Kalibangan", "Lothal", "Mohenjo-daro", "Harappa"],
        0,
        "A highly realistic, expressive bronze figure of a charging bull was discovered at Kalibangan. (Bronze models are also known from Lothal and Mohenjo-daro, but the famous charging bull is from Kalibangan)."
    ),
    # Q22
    (
        "With reference to the stone sculpture of the 'Male Dancer' (grey steatite/sandstone) from Harappa, consider the following statements:\n1. The figure is depicted standing on one leg with the other leg raised in a dynamic dance posture.\n2. Like the red sandstone torso, it features socket holes for attaching a head and limbs.\n3. It has been interpreted by some scholars as an early representation of Nataraja (Shiva as Lord of Dance).\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct. The grey dancer shows a dynamic pose, features socket holes for head/limbs, and was compared by John Marshall to Nataraja."
    ),
    # Q23
    (
        "Consider the following statements regarding the ornaments and details of the Priest-King bust:\n1. He wears a plain circular woven headband (fillet) with a central disc decoration.\n2. A matching circular ornament is worn as an armlet on his right upper arm.\n3. His ears feature small holes on the sides, suggesting he wore detachable ear ornaments or earrings.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct, describing the headband, armlet, and pierced ears of the Priest-King."
    ),
    # Q24
    (
        "Which of the following statements is/are correct regarding the bronze 'Dancing Girl'?\n1. Her hair is tied in a neat bun, held by a woven band or cloth.\n2. She wears a total of four bangles on her right arm and a neck pendant.\n3. The sculpture was found inside the Great Bath of Mohenjo-daro.\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Her hair is tied in a bun. She wears 4 bangles on her right arm (and 24-25 on her left arm) and a triple-drop pendant. Statement 3 is incorrect: it was found in a residential house in Mohenjo-daro, not inside the Great Bath."
    ),
    # Q25
    (
        "With reference to the stone carving traditions of the Indus Valley, consider the following statements:\n1. Stone sculptures are extremely rare compared to terracotta figurines, suggesting stone was scarce and prized.\n2. Statues were carved using high-quality imported marble and granite exclusively.\n3. The eyes of stone sculptures were often inlaid with shell, faience, or colored stone to create a lifelike appearance.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Stone sculptures are rare (only about a dozen stone pieces have been found in total). Statement 2 is incorrect: they used steatite, sandstone, limestone, and alabaster, not granite or marble exclusively."
    ),
    # Q26
    (
        "Consider the following statements regarding the trefoil pattern on the Priest-King's shawl:\n1. The trefoil is a design of three overlapping circles or lobes.\n2. Similar trefoil decorative motifs are found in contemporary Mesopotamian and Egyptian royal art.\n3. The red paste that once filled the pattern was made of crushed carnelian beads.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Trefoils are three-lobed circles, also found in Mesopotamian and Egyptian arts, indicating cultural contacts. Statement 3 is incorrect: the red inlay was a clay/ochre paste, not crushed carnelian."
    ),
    # Q27
    (
        "With reference to the bronze casting centers of the Indus Valley Civilisation, which of the following is correct?",
        ["Bronze casting was practiced at almost all major urban centers, including Mohenjo-daro, Harappa, Lothal, and Kalibangan.", "Bronze casting was a secret monopoly restricted to the mountaintops of Baluchistan.", "No bronze casting facilities have been found; all bronze objects were imported from Mesopotamia.", "Only human figurines were cast in bronze, while animals were carved in stone."],
        0,
        "Bronze casting was widespread across major urban centers, as evidenced by crucibles, slag, and copper-bronze items found at Mohenjo-daro, Harappa, Lothal, and Kalibangan."
    ),
    # Q28
    (
        "Consider the following statements regarding the physical characteristics of the stone Priest-King:\n1. The nose is straight and pointed, reflecting classic Mediterranean facial characteristics.\n2. The lips are thick and the upper lip is shaved, with a neatly combed beard.\n3. The forehead is unusually low and sloping, which some scholars suggest represents a specific head-binding practice.\nWhich of the statements given above is/are correct?",
        ["2 and 3 only", "2 only", "1 and 2 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. The Priest-King has thick lips, shaved upper lip, and a low, sloping forehead. Statement 1 is incorrect: the nose is broad and slightly broken, and facial features are indigenous/local."
    ),
    # Q29
    (
        "With reference to the bronze figurines of animals, which of the following statements is correct?",
        ["They show highly expressive postures, such as a dog turning its head or a bull charging.", "They are heavily stylized and look like geometric blocks rather than real animals.", "They were used as standardized weights for trading precious metals.", "They were cast in iron molds to ensure identical dimensions."],
        0,
        "Harappan bronze animals show highly expressive and realistic postures (e.g. charging bull from Kalibangan, standing dog). They are not stylized blocks, weights, or cast in iron."
    ),
    # Q30
    (
        "Consider the following statements regarding the classification of Harappan stone sculptures:\n1. The majority of the stone sculptures represent seated or standing male figures.\n2. Female stone sculptures are extremely common, outnumbering male figures ten to one.\n3. Limestone and steatite were the preferred stones due to their relative softness.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Most stone sculptures represent male busts or figures, whereas female representations are abundant in terracotta but rare in stone. Limestone and steatite were preferred soft stones."
    ),

    # 31-45: Terracotta & Pottery
    # Q31
    (
        "Consider the following statements regarding Harappan terracotta art:\n1. Terracotta figurines were hand-modeled using pinching and appliqué techniques rather than cast in molds.\n2. Terracotta figurines are found in much larger quantities than stone or bronze sculptures.\n3. They represent a popular, domestic folk art tradition rather than elite administrative art.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. Terracottas were hand-modeled (pinching/appliqué), abundant (thousands found), and represent domestic, popular folk art."
    ),
    # Q32
    (
        "With reference to the terracotta Mother Goddess figurines, consider the following statements:\n1. They are standing female figures decorated with elaborate fan-shaped headdresses.\n2. The headdresses contain cup-like panniers on either side, which show soot staining.\n3. They have been found in large numbers at all major sites in Sindh, Punjab, Rajasthan, and Gujarat.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Mother Goddess figurines are abundant in Sindh and Punjab (Mohenjo-daro/Harappa) but are virtually absent at sites in Rajasthan (Kalibangan) and Gujarat (Lothal, Dholavira)."
    ),
    # Q33
    (
        "Consider the following statements regarding Harappan terracotta toys:\n1. Clay models of wheeled carts are the earliest archaeological evidence of wheeled transport in South Asia.\n2. Several bull figurines feature movable heads controlled by a thread run through the neck.\n3. A unique toy depicts a monkey that could slide up and down a vertical string.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct. Toy carts, movable-head bulls, and sliding monkeys reflect the ingenuity of Harappan toy makers."
    ),
    # Q34
    (
        "With reference to the Painted Pottery of the Indus Valley Civilisation, consider the following statements:\n1. Harappan pottery is primarily wheel-made, manufactured on a fast-spinning potter's wheel.\n2. Standard pottery is red-and-black ware, with black designs painted over a red iron-slip background.\n3. The black paint used was organic charcoal paste, which faded away easily over time.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Harappan pottery was wheel-made red-and-black ware. Statement 3 is incorrect: the black paint was manganese-based, which baked permanently into the clay and did not fade."
    ),
    # Q35
    (
        "Which of the following decorative motifs is NOT painted on Mature Harappan pottery?",
        ["Lions chasing gazelles", "Pipal leaves and palm trees", "Fish-scale patterns", "Intersecting circles and geometric grids"],
        0,
        "Lions chasing gazelles is not a Harappan motif (lions are absent). Pipal leaves, fish scales, intersecting circles, peacock motifs, and geometric grids are very common."
    ),
    # Q36
    (
        "Consider the following statements regarding the terracotta masks found in the Indus Valley:\n1. Small, hollow terracotta masks of humans and horned deities have been found at Mohenjo-daro and Harappa.\n2. These masks feature detailed facial features and were cast in precise two-part bronze molds.\n3. They feature small holes on the sides, indicating they were tied to faces or worn as amulets.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. Terracotta masks of horned deities or humans with suspension holes have been found. Statement 2 is incorrect: they were hand-modeled or pressed in clay molds, not bronze molds."
    ),
    # Q37
    (
        "With reference to the function of perforated pottery jars in Harappan archaeology, consider the following statements:\n1. They are tall, cylindrical jars containing numerous small holes drilled all over the body.\n2. They are believed to have been used as strainers for brewing alcoholic/fermented beverages or straining curds.\n3. They were used exclusively as protective guards to keep grain dry from rats.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Perforated jars are cylindrical vessels with holes all over, likely used for straining beverages, making cheese, or burning incense. They were not grain guards against rats."
    ),
    # Q38
    (
        "Consider the following statements regarding the terracotta figurines of animals:\n1. The humped bull (Zebu) is the most common terracotta animal figurine, modeled with realistic vigor.\n2. Figurine representations of dogs, pigs, monkeys, and birds are common in domestic houses.\n3. Terracotta horses are found in thousands at all Harappan sites, outnumbering bulls.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Humped bulls, dogs, pigs, monkeys, and birds are common. Statement 3 is incorrect: horse figurines are extremely rare (only contested specimens like Lothal exist) and do not outnumber bulls."
    ),
    # Q39
    (
        "With reference to the technical aspects of Harappan pottery kilns, which of the following is correct?",
        ["Pottery was fired in advanced updraft kilns with separate fuel chambers and perforated floors for heat circulation.", "Pottery was simply baked in open campfires, resulting in uneven black smudges.", "Kilns were fueled exclusively by imported Mesopotamian coal to achieve high temperatures.", "All pottery kilns were located inside residential bedrooms to keep houses warm."],
        0,
        "Harappan pottery was baked in advanced updraft kilns with fuel chambers beneath a perforated floor, allowing heat to circulate evenly. They did not use coal or locate kilns in bedrooms."
    ),
    # Q40
    (
        "Consider the following statements regarding the applique technique in terracotta figurines:\n1. Applique involves attaching separately shaped clay coils, discs, or strips onto the main body to represent ornaments.\n2. In Mother Goddess figurines, the eyes, necklaces, and headdress cup-panniers were attached using applique.\n3. Applique was only used on large public stone monuments and never on small clay items.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Applique is a clay attachment technique used extensively on hand-modeled terracotta figurines for jewelry, eyes, and headdress parts. It was not a stone technique."
    ),
    # Q41
    (
        "With reference to the 'Dish-on-Stand' pottery type of the Indus Valley, consider the following statements:\n1. It consists of a shallow dish supported by a central hollow pillar on a broad base.\n2. It was used as a standard table stand for offering food or burning incense in rituals.\n3. It was made exclusively of polished bronze, and clay versions were cheap replicas.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The dish-on-stand is a classic Harappan pottery shape, used for offerings or domestic display. It was primarily wheel-made of clay; bronze versions are virtually non-existent."
    ),
    # Q42
    (
        "Consider the following statements regarding the depictions of human figures in Harappan terracottas:\n1. Female figurines outnumber male figurines, with a strong focus on fertility and maternity representations.\n2. Seated male figures with hands on knees (in a posture resembling yogic meditation) have been found.\n3. Both male and female figures are shown wearing elaborate stitched trousers and jackets.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Females outnumber males in terracotta, and some seated male figures resemble yogic poses. Statement 3 is incorrect: figures are shown mostly bare-chested, wearing loincloths, skirts, and heavy ornaments, not stitched trousers/jackets."
    ),
    # Q43
    (
        "With reference to the black-on-red pottery painting process, consider the following statements:\n1. The red slip was made from a suspension of iron-rich red clay (ochre) applied before firing.\n2. The black paintings were executed after the pottery had been fired and cooled in the kiln.\n3. Firing the painted vessel at high temperatures bonded both slip and pigment permanently to the clay body.\nWhich of the statements given above is/are correct?",
        ["1 and 3 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 3 are correct. The red slip and black paint (manganese-based) were applied *before* firing. Firing them together at high temperatures bonded the slip and pigments permanently into the clay. Painting was not done post-firing."
    ),
    # Q44
    (
        "Which Mature Harappan site has yielded a unique terracotta model of a ship with a mast and sail rigging?",
        ["Lothal", "Kalibangan", "Dholavira", "Harappa"],
        0,
        "Lothal, the major port town, yielded a terracotta model of a ship with a mast socket, confirming maritime trade and shipbuilding technology."
    ),
    # Q45
    (
        "Consider the following statements regarding the regional differences in Harappan pottery:\n1. The pottery corpus is highly standardized across the vast geography, showing a unified technological guild system.\n2. Gujarat sites show a distinct regional style called 'Micaceous Red Ware' alongside standard Harappan wares.\n3. Painted pottery was entirely banned in the northern outposts like Shortughai.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Harappan pottery is highly standardized, but Gujarat has a local 'Micaceous Red Ware' tradition. Statement 3 is incorrect: Shortughai has standard Harappan painted pottery."
    ),

    # 46-50: Misc & Comparative
    # Q46
    (
        "Compare the seals of the Indus Valley Civilisation with those of contemporary Mesopotamia:\n1. Harappan seals are primarily square or rectangular steatite stamps, whereas Mesopotamian seals are mostly stone cylinders rolled over clay.\n2. Mesopotamian seals depict complex mythological battles and royal banquets, whereas Harappan seals focus on animal motifs and brief scripts.\n3. Both civilisations used their seals to stamp papyrus documents rather than clay packaging.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Harappan seals are square/rectangular stamps; Mesopotamian seals are cylinders. Mesopotamian seals show complex royal/divine scenes; Harappans show animal-centric motifs. Statement 3 is incorrect: both used seals on wet clay taggings/tags for packages, not on papyrus documents."
    ),
    # Q47
    (
        "With reference to the representation of the 'Priest-King' and Mesopotamian rulers, consider the following statements:\n1. Unlike the monumental stone statues of Mesopotamian Gudea of Lagash, the Harappan Priest-King is a tiny 17.5 cm bust.\n2. The Priest-King shawl has trefoil motifs similar to those associated with divine garments in Mesopotamia.\n3. The Priest-King bust was found inside a massive royal palace tomb at Mohenjo-daro.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The Priest-King is small (17.5 cm), unlike Mesopotamian monumental statues. The trefoil motif has parallels in Mesopotamian stars/divine symbols. Statement 3 is incorrect: no palaces or royal tombs have ever been found in the Indus Valley; the bust was found in a small residential house."
    ),
    # Q48
    (
        "Consider the following statements regarding the socio-cultural inferences drawn from Harappan art:\n1. The presence of toys like wheeled carts and sliding monkeys reflects a peaceful, stable society with leisure time.\n2. The high uniformity of seals and weights points to a centralized administration or strong merchant guild system.\n3. The abundance of defensive weapons depicted on seals indicates a highly militaristic empire.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Toys reflect a stable society with child-rearing and leisure. Standard seals/weights show central coordination. Statement 3 is incorrect: seals show animals and deities, never weapons or warfare scenes."
    ),
    # Q49
    (
        "With reference to the stylistic differences between the 'Dancing Girl' and the 'Priest-King', which of the following is correct?",
        ["The Dancing Girl is bronze and shows fluid, dynamic movements, while the Priest-King is stone and represents static, formal rigidity.", "The Dancing Girl is a clay terracotta and the Priest-King is a metal casting.", "Both sculptures show identical rigid posture and were carved by the same royal artist.", "The Dancing Girl shows Mesopotamian facial features while the Priest-King is purely Indian in style."],
        0,
        "The bronze Dancing Girl displays fluid movement (tribhanga pose), whereas the steatite Priest-King bust exhibits formal, static rigidity. The other options are incorrect."
    ),
    # Q50
    (
        "Consider the following statements regarding the preservation of Harappan art objects:\n1. Metal and stone sculptures survived well in the soil, while organic wood and textile arts have mostly decayed.\n2. Unbaked clay sealings survived because they were accidentally fired when warehouses burned down.\n3. All stone sculptures were defaced and broken by invaders during the Late Harappan phase.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Wood/textiles decayed due to the humid monsoon environment. Clay sealings survived because warehouses caught fire, baking the clay. Statement 3 is incorrect: there is no evidence of widespread systematic defacement of stone sculptures by invaders."
    )
]

# Define 10 Mock Test Questions in English
# Structured as tuples: (question_text, option_list, correct_option_index, explanation_text)
mock_raw_eng = [
    # M1
    (
        "Consider the following statements regarding the steatite 'Priest-King' bust of Mohenjo-daro:\n1. He wears a fillet headband with a central circular disc ornament.\n2. His shawl is decorated with a trefoil pattern that was originally filled with red pigment.\n3. The figure depicts a clean-shaven upper lip combined with a neatly groomed beard.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        3,
        "All statements are correct. The Priest-King has a fillet headband, trefoil shawl inlays, a shaved upper lip, and a groomed beard."
    ),
    # M2
    (
        "With reference to the bronze 'Dancing Girl' from Mohenjo-daro, consider the following statements:\n1. The sculpture was cast in bronze using the Lost-Wax (cire perdue) technique.\n2. She stands in the 'Tribhanga' posture, showing three bends in her body.\n3. Her right arm is adorned with 24 to 25 bangles, while her left arm has only 4 bangles.\nWhich of the statements given above are correct?",
        ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Statement 3 is incorrect: she wears 24-25 bangles on her *left* arm, and only 4 bangles/armlet on her *right* arm."
    ),
    # M3
    (
        "Consider the following statements regarding Harappan seals:\n1. Steatite seals were chemically glazed and hardened through kiln firing, turning talc into enstatite.\n2. Square seals feature animal motifs and script, while rectangular seals carry only script.\n3. Seals were used as standardized metallic currency in international trade.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Steatite converts to enstatite upon firing. Rectangular seals carry script only. Statement 3 is incorrect: seals were security tags and credentials, not metal currency."
    ),
    # M4
    (
        "With reference to the red sandstone male torso from Harappa, which of the following statements is/are correct?\n1. It exhibits highly realistic abdominal and muscular rendering, unlike typical archaic art.\n2. It features socket holes at the neck and shoulders to attach detachable limbs.\n3. It is a large, life-sized stone monument located in the central assembly hall.\nSelect the correct answer using the code given below:",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. The red sandstone torso is realistic and features socket holes for detachable pieces. Statement 3 is incorrect: it is a miniature piece (9.5 cm), not a life-sized monument."
    ),
    # M5
    (
        "Consider the following statements regarding Harappan terracotta Mother Goddess figurines:\n1. They were cast using double-sided clay molds to achieve high structural uniformity.\n2. They feature elaborate fan-shaped headdresses with cup-like panniers on the sides.\n3. Soot stains inside the headdress panniers suggest their use as lamps or incense burners in domestic rituals.\nWhich of the statements given above are correct?",
        ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        0,
        "Statements 2 and 3 are correct. They have fan headdresses with soot-stained cup panniers used in domestic rituals. Statement 1 is incorrect: terracottas were hand-modeled, not mold-cast."
    ),
    # M6
    (
        "With reference to Mature Harappan painted pottery, consider the following statements:\n1. The base color is red, achieved by applying an iron-rich slip prior to firing.\n2. Painted motifs are in black, using manganese-rich pigments.\n3. The most common painted designs include geometric intersecting circles, Pipal leaves, and fish scales.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All three statements are correct. The pottery is wheel-made red-and-black ware, with black manganese designs (intersecting circles, Pipal leaves, fish scales) painted on a red slip base."
    ),
    # M7
    (
        "Which of the following sites has yielded a bronze model of a charging bull and clay-lined fire altars?",
        ["Kalibangan", "Lothal", "Mohenjo-daro", "Harappa"],
        0,
        "Kalibangan yielded a realistic bronze charging bull, along with clay-lined fire altars."
    ),
    # M8
    (
        "Consider the following statements regarding Harappan copper tablets:\n1. They contain engravings of animals or deities on one face and inscriptions on the other.\n2. They are found in large quantities at Mohenjo-daro and Harappa.\n3. They were used as coins for retail trade in the urban markets.\nWhich of the statements given above is/are correct?",
        ["1 and 2 only", "1 only", "2 and 3 only", "1, 2 and 3"],
        0,
        "Statements 1 and 2 are correct. Copper tablets depict animals/deities on one side and text on the other. They are concentrated at Mohenjo-daro and Harappa. Statement 3 is incorrect: they were likely worn as amulets or tokens, not used as coins."
    ),
    # M9
    (
        "With reference to the representations of animals in Harappan art, which of the following is correct?",
        ["The lion is completely absent from seals and pottery, while the tiger is depicted.", "The horse is the most common animal carved on square steatite seals.", "Bows and arrows are frequently shown being used to hunt elephants on copper tablets.", "All animals on seals are mythical composite monsters with three heads."],
        0,
        "The lion is completely absent, while the tiger is depicted on seals and pottery. The unicorn, not the horse, is the most common seal animal. Hunt scenes are extremely rare, and most animals on seals are real (except the unicorn and composite beasts)."
    ),
    # M10
    (
        "Consider the following statements regarding the clay sealings found at Lothal:\n1. They contain impressions of seals on one side and impressions of packing cords or mats on the reverse.\n2. They survived because they were accidentally baked in fires that destroyed the storehouses.\n3. They prove that Lothal was an active trading port engaged in packaging and shipping goods.\nWhich of the statements given above are correct?",
        ["1, 2 and 3", "1 and 2 only", "2 and 3 only", "1 and 3 only"],
        0,
        "All statements are correct. Lothal sealings show seal stamps and packaging textures (cords/mats), survived via warehouse fires, and verify Lothal's role as a major maritime trade and packaging depot."
    )
]

# We will map these questions to Hindi equivalents.
# To keep translations high-yield and accurate, let's write Hindi questions list.

practice_raw_hin = [
    # Q1
    (
        "परिपक्व हड़प्पा मुहरों के निर्माण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश मुहरें सेलखड़ी (steatite) से बनी थीं, जो एक नरम साबुन पत्थर (soapstone) है और तांबे के उपकरणों से आसानी से काटा जा सकता था।\n2. मुहरों को भट्टी में पकाने से सेलखड़ी रासायनिक रूप से बदल जाती थी, जिससे वह अधिक कठोर एन्सटाइट (enstatite) खनिज में परिवर्तित हो जाती थी।\n3. पकाने से पहले मुहरों पर सेलखड़ी (talc) पर आधारित लेप लगाने से उन पर सफेद, चमकदार परत (glazed finish) प्राप्त होती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। सेलखड़ी एक नरम खनिज है। इसे 900 डिग्री सेल्सियस से ऊपर पकाने पर यह एन्सटाइट (मैग्नीशियम सिलिकेट) में बदल जाती है जो काफी कठोर होता है। पकाने से पहले इस पर टैल्क का घोल लगाने से सफेद चमकीली सतह मिलती थी।"
    ),
    # Q2
    (
        "हड़प्पा मुहरों की शारीरिक संरचना के संदर्भ में, निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. चौकोर मुहरें सबसे आम प्रकार हैं, जिनमें पशुओं की आकृतियों के साथ एक संक्षिप्त लिपि होती है।\n2. चौकोर मुहरों का पिछला हिस्सा आमतौर पर सपाट होता है, जिस पर कोई उभार या छेद नहीं होता ताकि छपाई की सतह समतल रहे।\n3. आयताकार मुहरों पर केवल लिपि अंकित होती है और उनमें पशुओं की आकृतियों का पूर्ण अभाव होता है।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["1 केवल", "1 और 3 केवल", "2 केवल", "1, 2 और 3"],
        1,
        "कथन 1 और 3 सही हैं। आयताकार/छड़ मुहरों पर केवल लिपि होती है, पशु नहीं। कथन 2 गलत है क्योंकि चौकोर मुहरों के पीछे एक उभरा हुआ बटन (boss) होता था जिसमें धागा पिरोने के लिए छेद होता था।"
    ),
    # Q3
    (
        "व्यापार और प्रशासन में हड़प्पा मुहरों के कार्यों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. व्यापारिक माल की गांठों पर गीली मिट्टी लगाकर लगाई गई मुहर की छाप (सील) पैकेट को सुरक्षित रखती थी और उसके उद्गम को सत्यापित करती थी।\n2. मुहरों ने बाजारों में राज्य द्वारा गारंटीकृत मानकीकृत मौद्रिक मुद्रा (coins) के रूप में कार्य किया।\n3. मुहरें व्यापारियों और प्रशासनिक संभ्रांत वर्ग द्वारा धारण की जाने वाली आधिकारिक पहचान और सामाजिक प्रतिष्ठा के प्रतीक थीं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "1 और 3 केवल", "2 और 3 केवल", "1, 2 और 3"],
        1,
        "कथन 1 और 3 सही हैं। मुहरें व्यापारिक सुरक्षा और प्रतिष्ठा के प्रतीक थे। कथन 2 गलत है क्योंकि हड़प्पा वासी मुद्रा का उपयोग नहीं करते थे; उनका व्यापार वस्तु विनिमय और मानकीकृत बाटों पर आधारित था।"
    ),
    # Q4
    (
        "सिंधु घाटी सभ्यता से प्राप्त तांबे की पट्टिकाओं (copper tablets) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये तांबे के सपाट, आयताकार टुकड़े हैं जिनके एक तरफ पशु या देवता की आकृति और दूसरी तरफ लिपि उत्कीर्ण है।\n2. सेलखड़ी की मुहरों के विपरीत, तांबे की पट्टिकाओं के पीछे लटकने के लिए छेद वाला कोई उभार (boss) नहीं होता है।\n3. ये कालीबंगन और लोथल में बड़ी संख्या में खोजे गए हैं लेकिन मोहनजोदड़ो में पूरी तरह से अनुपस्थित हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। तांबे की पट्टियों पर पीछे कोई उभार नहीं होता। कथन 3 गलत है क्योंकि ये मुख्य रूप से मोहनजोदड़ो और हड़प्पा से मिली हैं, कालीबंगन और लोथल में ये अत्यंत दुर्लभ या अनुपस्थित हैं।"
    ),
    # Q5
    (
        "निम्नलिखित कथनों पर विचार करें:\n1. एक सींग वाला काल्पनिक पशु (Unicorn) हड़प्पा मुहरों पर सबसे अधिक चित्रित होने वाला जीव है।\n2. यूनिकॉर्न को लगभग हमेशा एक दो-स्तरीय धूपदानी या पात्र (censer standard) के सामने खड़ा दिखाया गया है, जिसे धार्मिक वस्तु माना जाता है।\n3. बाघ और हाथी जैसे वास्तविक पशुओं के चित्रण वाली मुहरें हड़प्पा कला में पूरी तरह अनुपस्थित हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। यूनिकॉर्न सबसे आम आकृति है और वह धूप पात्र के सामने खड़ा है। कथन 3 गलत है क्योंकि बाघ, हाथी, गैंडा और कूबड़ वाले बैल जैसे वास्तविक पशुओं का मुहरों पर प्रचुरता से चित्रण मिलता है।"
    ),
    # Q6
    (
        "हड़प्पा मुहरों के उत्कीर्णन तकनीक के संदर्भ में निम्नलिखित में से कौन सा सही है?",
        ["मुहरों को अंतर्गठित नक्काशी (intaglio) में उकेरा गया था ताकि वे मिट्टी पर उभरी हुई छापें तैयार कर सकें।", "मुहरों को उभरी हुई नक्काशी (cameo) में उकेरा गया था ताकि पपीरस के पत्तों पर स्याही से छपाई की जा सके।", "शिलालेखों को पत्थर पर तराशने के बजाय प्राकृतिक रंगों से रंगा गया था।", "सभी चौकोर मुहरों पर लिपि को केवल बाएं से दाएं उत्कीर्ण किया गया था।"],
        0,
        "हड़प्पा मुहरें अंतर्गठित (intaglio) नक्काशी में काटी जाती थीं ताकि गीली मिट्टी पर दबाने पर वे उभरी हुई सकारात्मक छवि छोड़ें। लिपि उत्कीर्ण की जाती थी, रंगी नहीं जाती थी।"
    ),
    # Q7
    (
        "हड़प्पा मुहरों में प्रयुक्त कच्चे माल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी मुख्य सामग्री थी, लेकिन मुहरें पकी मिट्टी, चर्ट, अगेट और तांबे से भी बनाई जाती थीं।\n2. फेयॉन्स (faience), जो सिलिका और गोंद से बना एक कृत्रिम चमकदार चीनी मिट्टी जैसा पदार्थ है, का उपयोग भी छोटी मुहरें बनाने के लिए किया जाता था।\n3. धोलावीरा से लोहे के आवरण वाली पत्थर की मुहरें मिली हैं, जो उन्नत धातु कर्म का संकेत देती हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। सामग्री में सेलखड़ी, चर्ट, अगेट, मिट्टी, तांबा और फेयॉन्स शामिल थे। कथन 3 गलत है क्योंकि हड़प्पा सभ्यता में लोहा अज्ञात था।"
    ),
    # Q8
    (
        "हड़प्पा की मिट्टी की मुहरों (clay sealings) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लोथल से कई ऐसी मिट्टी की सीलें मिली हैं जिनके पीछे रस्सी और पैकिंग सामग्री के निशान बने हैं।\n2. गीली मिट्टी के एक ही टुकड़े पर कई अलग-अलग मुहरों की छाप लगाई जा सकती थी, जो संयुक्त लेनदेन को दर्शाती है।\n3. खोजे गए अधिकांश मिट्टी के सील को रसीद के रूप में सुरक्षित रखने के लिए लगाने के तुरंत बाद भट्टी में पकाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। लोथल की सीलें रस्सी और बोरे के निशान दिखाती हैं। एक मिट्टी पर कई छापें संयुक्त व्यापारिक जिम्मेदारी दर्शाती हैं। कथन 3 गलत है क्योंकि ये धूप में सुखाई जाती थीं और केवल उन गोदामों में लगी आग के कारण पक गईं जो नष्ट हो गए थे।"
    ),
    # Q9
    (
        "मोहनजोदड़ो की 'पशुपति मुहर' के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह सेलखड़ी की एक चौकोर मुहर है जिस पर ध्यानमग्न मुद्रा में बैठे तीन मुख वाले सींग युक्त देवता को दिखाया गया है जो पशुओं से घिरे हैं।\n2. मुहर पर लिपि में छह अक्षरों की एक पंक्ति उनके सींग वाले मुकुट के ठीक ऊपर उत्कीर्ण है।\n3. सर जॉन मार्शल द्वारा इस आकृति को 'आदि-शिव' (Proto-Shiva) कहने की व्याख्या को सभी आधुनिक इतिहासकारों ने बिना किसी विवाद के स्वीकार कर लिया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। पशुपति मुहर में सींग वाले तीन मुखी देवता हैं जिनके ऊपर छह अक्षरों का लेख है। कथन 3 गलत है क्योंकि मार्शल की थ्योरी विवादित है; कई विद्वान इसे बैल रूपी उर्वरता का देवता मानते हैं।"
    ),
    # Q10
    (
        "निम्नलिखित में से कौन सा पशु परिपक्व हड़प्पा मुहरों पर कभी चित्रित नहीं किया गया है?",
        ["शेर", "बाघ", "गैंडा", "कूबड़ वाला बैल"],
        0,
        "शेर का चित्रण हड़प्पा मुहरों या मिट्टी के बर्तनों पर कभी नहीं मिला है, जबकि बाघ, गैंडा, हाथी और सांड आम हैं।"
    ),
    # Q11
    (
        "सिंधु घाटी सभ्यता की आयताकार मुहरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये आमतौर पर चौकोर मुहरों से छोटी होती हैं और इनके पीछे छेद वाला कोई उभार नहीं होता।\n2. इन पर सामान्यतः पशुओं के चित्र नहीं होते, केवल लिपि के अक्षर खुदे होते हैं।\n3. ये केवल तांबे से बनाई जाती थीं, जबकि चौकोर मुहरें सेलखड़ी से बनती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 सही है। आयताकार मुहरों पर केवल लेख होता है। कथन 1 गलत है क्योंकि इनके पीछे भी धागा पिरोने का छेद या उत्तलता होती थी। कथन 3 गलत है क्योंकि ये भी सेलखड़ी से ही बनती थीं।"
    ),
    # Q12
    (
        "ताबीज के रूप में मुहरों की भूमिका के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कई मुहरों में लटकने के लिए छेद होते हैं, जिससे संकेत मिलता है कि वे सुरक्षात्मक ताबीज के रूप में गले या बांह में पहनी जाती थीं।\n2. कुछ मुहरों पर राक्षसों से लड़ते नायकों या पेड़ों से निकलते देवताओं के दृश्य हैं, जो पौराणिक संरक्षण को दर्शाते हैं।\n3. पीछे बिना उभार वाली सेलखड़ी की पतली पट्टियों का उपयोग व्यावसायिक छाप के बजाय जादुई ताबीज के रूप में किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं। छेद वाले आकार, पौराणिक दृश्य और पतली पट्टियां दर्शाती हैं कि मुहरें और पट्टियां ताबीज के रूप में भी काम करती थीं।"
    ),
    # Q13
    (
        "सिंधु घाटी की तांबे की पट्टिकाओं के संदर्भ में निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. सेलखड़ी की मुहरों की तुलना में इनके आकार और माप में बहुत अधिक मानकीकरण पाया जाता है।\n2. तांबे की पट्टिकाओं पर नक्काशी आमतौर पर उथली और रेखाचित्र जैसी होती है, न कि सेलखड़ी मुहरों जैसी गहरी।\n3. ऐसा माना जाता है कि इनका उपयोग मंदिरों में नकद दान दर्ज करने के लिए किया जाता था।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["2 केवल", "1 और 2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        1,
        "कथन 1 और 2 सही हैं। तांबे की पट्टियां अत्यधिक मानकीकृत हैं और उन पर उथली नक्काशी है। कथन 3 गलत है क्योंकि हड़प्पा में मंदिर या नकद सिक्के का अस्तित्व नहीं था।"
    ),
    # Q14
    (
        "हड़प्पा मुहरों के रूपांकनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कूबड़ वाले बैल (Zebu) को बहुत कलात्मक बारीकी से उकेरा गया है, जिसमें उसके बड़े कूबड़ और लटकती गलकंबल को दर्शाया गया है।\n2. मिश्रित पशु आकृतियों में विभिन्न जानवरों के अंगों को जोड़ा गया है, जैसे तीन सिरों वाला पशु (सांड, यूनिकॉर्न, बकरा)।\n3. मुहरों पर मानव आकृतियों को अक्सर खेतों में हल चलाते हुए दिखाया गया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कूबड़ वाला सांड बहुत सजीव है और मिश्रित पशु आम हैं। कथन 3 गलत है क्योंकि मुहरों पर कभी भी हल चलाते हुए इंसान का चित्रण नहीं मिला है।"
    ),
    # Q15
    (
        "सिंधु क्षेत्र के बाहर हड़प्पा मुहरों की खोज के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के स्थलों जैसे किश, उर और सूसा से हड़प्पा शैली की वर्गाकार मुहरें प्राप्त हुई हैं।\n2. लोथल से प्राप्त गोल 'फारस की खाड़ी' शैली की मुहरें दोनों क्षेत्रों के बीच समुद्री व्यापार संपर्कों की पुष्टि करती हैं।\n3. सिंधु घाटी में मिली विदेशी मुहरें स्थानीय भारतीय सेलखड़ी से बनी थीं जिन्हें हड़प्पा के कलाकारों ने तराशा था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। मेसोपोटामिया में वर्गाकार मुहरें और लोथल में फारस की खाड़ी की मुहरें व्यापारिक संपर्क दर्शाती हैं। कथन 3 गलत है क्योंकि विदेशी मुहरें आयातित थीं और गैर-स्थानीय पत्थरों से बनी थीं।"
    ),

    # 16-30: Stone & Bronze
    # Q16
    (
        "मोहनजोदड़ो की कांस्य 'नर्तकी' (Dancing Girl) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह 10.5 सेमी ऊंची कांस्य की लघु मूर्ति है जो एक युवा महिला नर्तक का प्रतिनिधित्व करती है।\n2. उसे दाहिना हाथ अपनी कमर पर रखे और बाईं बांह को चूड़ियों से पूरी तरह ढके हुए एक शिथिल मुद्रा में दिखाया गया है।\n3. इस मूर्ति की विशेषता इसके लंबे हाथ-पैर और आत्मविश्वास से भरा चेहरा है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। नर्तकी की ऊंचाई 10.5 सेमी है, त्रिभंग मुद्रा में है, दाहिना हाथ कमर पर और बायां हाथ चूड़ियों (24-25) से भरा है, हाथ-पैर लंबे हैं और चेहरा गर्वित है।"
    ),
    # Q17
    (
        "हड़प्पा के धातुकारों द्वारा प्रयुक्त लुप्त मोम ढलाई तकनीक (cire perdue) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मूर्ति के ठोस मिट्टी के मॉडल पर सीधे पिघला हुआ कांसा चढ़ा दिया जाता था।\n2. मोम के मॉडल को गर्म मिट्टी के सांचे से पिघलाकर बाहर निकाल लिया जाता था, जिससे सांचे के भीतर खाली जगह बचती थी।\n3. इस तकनीक का उपयोग खोखली मानव मूर्तियों और ठोस पशु मूर्तियों (जैसे कालीबंगन के सांड) दोनों को ढालने के लिए किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 और 3 केवल", "2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। लुप्त मोम विधि में मोम पिघलाकर बाहर निकाला जाता था और उसमें धातु भरी जाती थी। छोटे जानवरों को ठोस और मानव आकृतियों को खोखला ढाला जाता था।"
    ),
    # Q18
    (
        "मोहनजोदड़ो से प्राप्त सेलखड़ी की 'पुरोहित राजा' (Priest-King) की प्रतिमा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस आकृति को अधखुले नेत्रों के साथ दिखाया गया है, जो ध्यानमग्न मुद्रा (ध्यान) का संकेत देते हैं।\n2. इनकी दाढ़ी करीने से संवारी हुई है, जबकि ऊपरी होंठ (मूंछ) पूरी तरह से साफ है।\n3. इनके बाएं कंधे पर तिपतिया (trefoil) डिज़ाइन से सजी शाल ओढ़ाई गई है, जिससे दायां हाथ स्वतंत्र रहता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं, जो पुरोहित राजा के अधखुले नेत्रों, संवारी दाढ़ी, साफ मूंछों और बाएं कंधे पर तिपतिया शाल के चित्रण का वर्णन करते हैं।"
    ),
    # Q19
    (
        "हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ (Male Torso) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे अत्यधिक यथार्थवादी शारीरिक गठन के साथ तराशा गया है, जिसमें पेट की मांसपेशियों और शारीरिक उभारों को दर्शाया गया है।\n2. इसके गर्दन और कंधों पर सॉकेट छेद बने हैं ताकि अलग से बने सिर और हाथ जोड़े जा सकें।\n3. यह मूर्ति नगर के मुख्य द्वार पर स्थापित एक विशाल सार्वजनिक प्रतिमा थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। लाल बलुआ पत्थर का धड़ बहुत छोटा है (लगभग 9.5 सेमी) लेकिन अत्यंत यथार्थवादी है और इसमें सॉकेट छेद हैं। कथन 3 गलत है क्योंकि यह एक छोटी घरेलू वस्तु थी, कोई विशाल सार्वजनिक स्मारक नहीं।"
    ),
    # Q20
    (
        "सिंधु घाटी सभ्यता के कांस्य धातु कर्म के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. प्रयुक्त कांस्य मिश्र धातु तांबे के साथ टिन और कभी-कभी आर्सेनिक का मिश्रण थी ताकि धातु का प्रवाह बेहतर हो सके।\n2. हड़प्पा के धातु के बर्तन मुख्य रूप से सजावटी थे, और कांस्य के औजारों या हथियारों का पूर्ण अभाव था।\n3. तांबा और टिन के अयस्क सिंधु घाटी के मैदानी इलाकों से स्थानीय स्तर पर प्राप्त किए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 केवल", "1 और 2 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 सही है। आर्सेनिक-कांसा प्रयुक्त होता था। कथन 2 गलत है क्योंकि वे कुल्हाड़ी, आरी, छेनी जैसे औजार भी बनाते थे। कथन 3 गलत है क्योंकि धातुएं बाहर से आयात की जाती थीं (तांबा राजस्थान/ओमान से और टिन अफगानिस्तान से)।"
    ),
    # Q21
    (
        "एक 'आक्रमण करते सांड' (Charging Bull) की प्रसिद्ध कांस्य मूर्ति किस परिपक्व हड़प्पा स्थल से खोजी गई थी?",
        ["कालीबंगन", "लोथल", "मोहनजोदड़ो", "हड़प्पा"],
        0,
        "एक अत्यंत जीवंत और आक्रामक कांस्य सांड की मूर्ति कालीबंगन से खोजी गई थी।"
    ),
    # Q22
    (
        "हड़प्पा से प्राप्त 'पुरुष नर्तक' (धूसर सेलखड़ी/बलुआ पत्थर) की प्रस्तर मूर्ति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस आकृति को एक पैर पर खड़े होकर दूसरे पैर को ऊपर उठाए हुए एक गतिशील नृत्य मुद्रा में दिखाया गया है।\n2. लाल बलुआ पत्थर के धड़ की तरह, इसमें भी सिर और हाथ-पैर जोड़ने के लिए सॉकेट छेद बने हैं।\n3. कुछ विद्वानों ने इसे नटराज (नृत्य के देवता शिव) के प्रारंभिक रूप के रूप में व्याख्यायित किया है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं। धूसर नर्तक नृत्य मुद्रा में है, सॉकेट छेद युक्त है और जॉन मार्शल ने इसकी तुलना नटराज से की थी।"
    ),
    # Q23
    (
        "पुरोहित राजा की मूर्ति के आभूषणों और विवरणों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. वे सिर पर एक साधारण पट्टी (fillet) पहने हैं जिसके केंद्र में एक गोल चक्र बना है।\n2. उनके दाहिने हाथ की ऊपरी बांह पर एक वैसा ही गोल बाजूबंद (armlet) बंधा हुआ है।\n3. उनके कानों के दोनों तरफ छोटे छेद बने हैं, जिससे संकेत मिलता है कि वे अलग से कान के आभूषण पहनते थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं, जो पुरोहित राजा के सिर की पट्टी, बाजूबंद और कान के छेदों का विवरण देते हैं।"
    ),
    # Q24
    (
        "कांस्य 'नर्तकी' (Dancing Girl) के संदर्भ में निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. उसके बाल एक साफ जूड़े में बंधे हैं जिसे एक कपड़े या पट्टी से बांधा गया है।\n2. वह अपने दाहिने हाथ में कुल चार चूड़ियाँ और गले में एक पेंडेंट पहने हुए है।\n3. यह मूर्ति मोहनजोदड़ो के विशाल स्नानागार के भीतर से प्राप्त हुई थी।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। उसके बाल जूड़े में हैं। दाहिने हाथ में 4 चूड़ियाँ (बाएं हाथ में 24-25) और गले में हार है। कथन 3 गलत है क्योंकि यह मोहनजोदड़ो के एक सामान्य रिहायशी घर से मिली थी, न कि विशाल स्नानागार से।"
    ),
    # Q25
    (
        "सिंधु घाटी की प्रस्तर मूर्तिकला परंपराओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की मूर्तियों की तुलना में पत्थर की मूर्तियाँ अत्यंत दुर्लभ हैं, जिससे पता चलता है कि पत्थर दुर्लभ और मूल्यवान था।\n2. मूर्तियाँ केवल आयातित उच्च गुणवत्ता वाले संगमरमर और ग्रेनाइट से बनाई जाती थीं।\n3. सजीव रूप देने के लिए पत्थर की मूर्तियों की आँखों में अक्सर शंख, फेयॉन्स या रंगीन पत्थर जड़े जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। पत्थर की मूर्तियाँ बहुत कम मिली हैं (कुल मिलाकर लगभग 12 मूर्तियाँ)। कथन 2 गलत है क्योंकि वे सेलखड़ी, बलुआ पत्थर, चूना पत्थर और अलाबास्टर का उपयोग करते थे, न कि केवल संगमरमर या ग्रेनाइट का।"
    ),
    # Q26
    (
        "पुरोहित राजा की शाल पर बने तिपतिया (trefoil) डिज़ाइन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. तिपतिया डिज़ाइन एक-दूसरे को काटते तीन वृत्तों या पत्तियों का डिज़ाइन है।\n2. इसी तरह के तिपतिया सजावटी डिज़ाइन तत्कालीन मेसोपोटामिया और मिस्र की शाही कला में भी पाए जाते हैं।\n3. इस तिपतिया आकृति में जो लाल रंग भरा गया था वह कुचले हुए कार्नेलियन मोतियों से बनाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। तिपतिया तीन पत्तियों वाला डिज़ाइन है जो मेसोपोटामिया और मिस्र में भी मिलता है। कथन 3 गलत है क्योंकि लाल रंग गेरू या मिट्टी का पेस्ट था, न कि कीमती कार्नेलियन का चूर्ण।"
    ),
    # Q27
    (
        "सिंधु घाटी सभ्यता के कांस्य ढलाई केंद्रों के संदर्भ में निम्नलिखित में से कौन सा सही है?",
        ["कांस्य ढलाई का काम मोहनजोदड़ो, हड़प्पा, लोथल और कालीबंगन सहित लगभग सभी प्रमुख शहरी केंद्रों में किया जाता था।", "कांस्य ढलाई एक गुप्त तकनीक थी जो केवल बलूचिस्तान के पर्वतों तक सीमित थी।", "कांस्य ढलाई का कोई कारखाना नहीं मिला है; सभी कांस्य वस्तुएं मेसोपोटामिया से आयात की जाती थीं।", "कांस्य में केवल इंसानों की मूर्तियां ढाली जाती थीं, जबकि जानवरों की मूर्तियां पत्थर में बनाई जाती थीं।"],
        0,
        "कांस्य ढलाई का कार्य सभी बड़े शहरों में फैला था, जिसके साक्ष्य भट्टी की राख, क्रूसिबल और कांसा धातु के टुकड़ों से मिलते हैं।"
    ),
    # Q28
    (
        "प्रस्तर पुरोहित राजा की शारीरिक विशेषताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इनकी नाक तीखी और नुकीली है, जो भूमध्यसागरीय नस्ल की विशिष्ट विशेषता है।\n2. होंठ मोटे हैं, ऊपरी होंठ साफ है और दाढ़ी को संवारा गया है।\n3. माथा असामान्य रूप से छोटा और ढलुआ है, जो सिर को बांधने की किसी विशिष्ट प्रथा को दर्शा सकता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["2 और 3 केवल", "2 केवल", "1 और 2 केवल", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। होंठ मोटे हैं, मूंछ साफ है और माथा ढलुआ है। कथन 1 गलत है क्योंकि नाक चौड़ी और थोड़ी टूटी हुई है, और चेहरे की विशेषताएं स्थानीय शैली की हैं।"
    ),
    # Q29
    (
        "कांस्य की पशु मूर्तियों के संदर्भ में निम्नलिखित में से कौन सा कथन सही है?",
        ["वे अत्यधिक जीवंत मुद्राएं दर्शाती हैं, जैसे सिर घुमाता कुत्ता या हमला करता सांड।", "वे बहुत ही अमूर्त और ज्यामितीय ब्लॉकों जैसी दिखती हैं, असली जानवरों जैसी नहीं।", "उनका उपयोग कीमती धातुओं के व्यापार के लिए मानक बाटों के रूप में किया जाता था।", "समान आकार सुनिश्चित करने के लिए उन्हें लोहे के सांचों में ढाला जाता था।"],
        0,
        "हड़प्पा के कांस्य पशु बहुत जीवंत मुद्राएं दर्शाते हैं (जैसे कालीबंगन का सांड या खड़ा कुत्ता)। वे ज्यामितीय आकार या बाट नहीं थे।"
    ),
    # Q30
    (
        "हड़प्पा की प्रस्तर मूर्तियों के वर्गीकरण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. अधिकांश प्रस्तर मूर्तियां बैठे या खड़े पुरुष आकृतियों को दर्शाती हैं।\n2. महिला प्रस्तर मूर्तियां बहुत आम हैं और पुरुषों की तुलना में दस गुना अधिक हैं।\n3. चूना पत्थर और सेलखड़ी पसंदीदा पत्थर थे क्योंकि वे तुलनात्मक रूप से मुलायम होते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। पत्थर की मूर्तियाँ अधिकांशतः पुरुष हैं, जबकि महिलाओं की प्रचुरता मिट्टी की मूर्तियों में है। मुलायम होने के कारण सेलखड़ी और चूना पत्थर अधिक पसंद किए जाते थे।"
    ),

    # 31-45: Terracotta & Pottery
    # Q31
    (
        "हड़प्पा कालीन मिट्टी की मूर्तियों (Terracotta) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मिट्टी की मूर्तियां सांचे में ढालने के बजाय उंगलियों से दबाने (pinching) और चिपकाने (appliqué) की तकनीकों से हाथ से बनाई जाती थीं।\n2. मिट्टी की मूर्तियां पत्थर या कांस्य मूर्तियों की तुलना में बहुत अधिक मात्रा में पाई जाती हैं।\n3. ये मूर्तियां कुलीन प्रशासनिक कला के बजाय आम जनता की घरेलू कला परंपरा का प्रतिनिधित्व करती हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। मिट्टी की मूर्तियां हाथ से बनी हैं (पिंचिंग/चिपकाने की विधि), बहुत बड़ी संख्या में मिली हैं और लोकप्रिय लोक कला को दर्शाती हैं।"
    ),
    # Q32
    (
        "मिट्टी की मातृदेवी की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये खड़ी हुई नारी मूर्तियां हैं जो सिर पर पंखे जैसे बड़े मुकुट से सजी हैं।\n2. इनके मुकुट के दोनों तरफ प्यालेनुमा आकृतियां हैं जिनमें कालिख के निशान मिले हैं।\n3. ये सिंध, पंजाब, राजस्थान और गुजरात के सभी प्रमुख स्थलों पर समान रूप से बड़ी संख्या में पाई गई हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि मातृदेवी की मूर्तियां सिंध और पंजाब (मोहनजोदड़ो/हड़प्पा) में तो प्रचुर हैं लेकिन राजस्थान (कालीबंगन) और गुजरात (लोथल, धोलावीरा) में इनका लगभग पूर्ण अभाव है।"
    ),
    # Q33
    (
        "हड़प्पा के मिट्टी के खिलौनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पहियों वाली गाड़ियों के मिट्टी के मॉडल दक्षिण एशिया में पहिएदार परिवहन के प्राचीनतम पुरातात्विक साक्ष्य हैं।\n2. कई बैलों की मूर्तियों में धागा पिरोकर उनका सिर हिलाने की व्यवस्था की गई है।\n3. एक अनूठे खिलौने में एक बंदर को दर्शाया गया है जो रस्सी पर ऊपर-नीचे सरक सकता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं। खिलौना गाड़ियां, धागे से हिलने वाले सिर वाले सांड और सरकने वाले बंदर हड़प्पा शिल्पकारों की खिलौना निर्माण कुशलता को दर्शाते हैं।"
    ),
    # Q34
    (
        "सिंधु घाटी सभ्यता के चित्रित मृदभांडों (Painted Pottery) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा के मृदभांड मुख्य रूप से चाक पर बने हैं, जिनका निर्माण तेज गति से घूमने वाले चाक पर किया जाता था।\n2. मानक बर्तन लाल और काले रंग के हैं, जिनमें लाल रंग के लेप की पृष्ठभूमि पर काले रंग से चित्रकारी की जाती थी।\n3. काले रंग के लिए कोयले के पेस्ट का उपयोग किया जाता था जो समय के साथ आसानी से मिट जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। हड़प्पा के बर्तन चाक पर बने लाल-काले मृदभांड हैं। कथन 3 गलत है क्योंकि काला रंग मैंगनीज ऑक्साइड से बनता था जो भट्टी में पकने के बाद पक्का हो जाता था और कभी नहीं मिटता था।"
    ),
    # Q35
    (
        "निम्नलिखित में से कौन सा सजावटी रूप हड़प्पा बर्तनों पर चित्रित नहीं मिलता है?",
        ["गैंडों का पीछा करते शेर", "पीपल के पत्ते और ताड़ के पेड़", "मछली के शल्क (fish scales) का पैटर्न", "एक-दूसरे को काटते वृत्त और ज्यामितीय चौखाने"],
        0,
        "शेर का चित्रण हड़प्पा बर्तनों पर नहीं मिलता (शेर अनुपस्थित था)। पीपल के पत्ते, मछली के शल्क, वृत्त और ज्यामितीय ग्रिड बहुत आम हैं।"
    ),
    # Q36
    (
        "हड़प्पा सभ्यता से प्राप्त मिट्टी के मुखौटों (masks) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो और हड़प्पा से इंसानों और सींग वाले देवताओं के छोटे खोखले मुखौटे मिले हैं।\n2. ये मुखौटे बारीक नक्काशी युक्त हैं और इन्हें कांसे के सांचों में ढाला जाता था।\n3. इनके किनारों पर छोटे छेद बने हैं, जो दर्शाते हैं कि इन्हें चेहरे पर बांधा जाता था या ताबीज की तरह पहना जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। छेद वाले मिट्टी के मुखौटे मिले हैं। कथन 2 गलत है क्योंकि ये हाथ से या मिट्टी के सांचे से बनते थे, कांसे के सांचे से नहीं।"
    ),
    # Q37
    (
        "छिद्रित बर्तनों (perforated jars) के कार्यों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ये लंबे, बेलनाकार बर्तन होते हैं जिनके पूरे शरीर पर कई छोटे छेद होते हैं।\n2. ऐसा माना जाता है कि इनका उपयोग पेय पदार्थों को छानने या धूप जलाने के लिए किया जाता था।\n3. इनका उपयोग केवल अनाजों को चूहों से बचाने के लिए ढाल के रूप में किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। छिद्रित बर्तन बेलनाकार होते हैं जिन पर छेद होते हैं, जिनका उपयोग पेय छानने या धूप जलाने में होता था। ये चूहों से बचाने वाली रक्षक ढाल नहीं थे।"
    ),
    # Q40
    (
        "मिट्टी की मूर्तियों में आवरण (appliqué) तकनीक के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आवरण तकनीक में अलग से बनाई गई मिट्टी की पट्टियों, गोलियों या डिस्क को मुख्य शरीर पर चिपकाकर आभूषण दर्शाए जाते थे।\n2. मातृदेवी की मूर्तियों में आंखें, गले के हार और सिर के प्याले आवरण विधि से चिपकाए जाते थे।\n3. आवरण तकनीक का उपयोग केवल बड़े पत्थरों के स्मारकों पर होता था, छोटी मिट्टी पर नहीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। आवरण (appliqué) तकनीक मिट्टी की मूर्तियों पर आंखें और आभूषण चिपकाने की विधि है। यह पत्थर की तकनीक नहीं है।"
    ),
    # Q41
    (
        "सिंधु घाटी के बर्तनों के 'डिश-ऑन-स्टैंड' (Dish-on-Stand) प्रकार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक छिछली थाली (dish) होती है जो एक चौड़े आधार वाले खोखले खंभे (stand) पर टिकी होती है।\n2. इसका उपयोग अनुष्ठानों में नैवेद्य (प्रसाद) चढ़ाने या धूप जलाने के लिए किया जाता था।\n3. यह केवल कांसे से बनता था और मिट्टी वाले इसके सस्ते क्लोन थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 and 2 सही हैं। डिश-ऑन-स्टैंड एक प्रमुख मृदभांड रूप है, जो मिट्टी से बनाया जाता था। कांसे के ऐसे बर्तन नगण्य हैं।"
    ),
    # Q42
    (
        "मिट्टी की मानव मूर्तियों में लिंगीय अनुपात के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. महिलाओं की मूर्तियां पुरुषों की तुलना में बहुत अधिक हैं, जिनमें मातृत्व और उर्वरता को दर्शाया गया है।\n2. योगासन मुद्रा में बैठे पुरुषों की मूर्तियां भी मिली हैं जिनके हाथ घुटनों पर टिके हैं।\n3. पुरुष और महिला दोनों को सिलाई किए हुए चुस्त पतलून और जैकेट पहने दिखाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। महिलाओं की संख्या अधिक है और योगासन मुद्रा के पुरुष भी मिले हैं। कथन 3 गलत है क्योंकि अधिकांश आकृतियाँ बिना सिले वस्त्र, घाघरे और आभूषण पहने हैं।"
    ),
    # Q43
    (
        "मृदभांडों पर लाल और काले रंग की चित्रकारी की प्रक्रिया के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लाल रंग का लेप (गेरू) पकाने से पहले गीले बर्तन पर चढ़ाया जाता था।\n2. काली चित्रकारी तब की जाती थी जब बर्तन भट्टी में पककर पूरी तरह ठंडा हो चुका होता था।\n3. बर्तन को उच्च तापमान पर पकाने से लेप और काले रंग के पिगमेंट दोनों मिट्टी के साथ हमेशा के लिए बंध जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 3 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 3 सही हैं। लाल लेप और काली चित्रकारी दोनों पकाने से पहले की जाती थीं। पकाने से ये स्थायी रूप से मिट्टी में समा जाते थे।"
    ),
    # Q44
    (
        "किस परिपक्व हड़प्पा स्थल से मस्तूल और पाल वाले जहाज का एक अनूठा मिट्टी का खिलौना मॉडल मिला है?",
        ["लोथल", "कालीबंगन", "धोलावीरा", "हड़प्पा"],
        0,
        "लोथल बंदरगाह शहर से जहाज का मिट्टी का मॉडल प्राप्त हुआ है जो उनकी नौवहन क्षमता को प्रमाणित करता है।"
    ),
    # Q45
    (
        "हड़प्पा बर्तनों में क्षेत्रीय भिन्नताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बर्तनों का आकार और तकनीक संपूर्ण भौगोलिक क्षेत्र में अत्यधिक मानकीकृत है जो एक संगठित गिल्ड दर्शाता है।\n2. गुजरात के स्थलों से सामान्य बर्तनों के साथ-साथ 'माइकेसियस रेड वेयर' (चमकीले लाल बर्तन) नामक एक स्थानीय शैली भी मिली है।\n3. उत्तरी चौकी शोरतुघई में चित्रित बर्तनों पर पूर्ण प्रतिबंध लगा दिया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। बर्तनों में भारी मानकीकरण है लेकिन गुजरात में स्थानीय 'माइकेसियस रेड वेयर' भी मिलता है। कथन 3 गलत है क्योंकि शोरतुघई से सामान्य हड़प्पा बर्तन मिले हैं।"
    ),
    # Q38 (missed index shift corrected)
    (
        "मिट्टी के पशुओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कूबड़ वाला बैल (Zebu) मिट्टी के जानवरों में सबसे आम है जिसे सजीव रूप में बनाया गया है।\n2. घरों में कुत्ते, सूअर, बंदर और पक्षियों की मिट्टी की मूर्तियाँ मिलना आम बात थी।\n3. मिट्टी के घोड़े सभी स्थलों से हजारों की संख्या में मिले हैं जो बैलों से भी अधिक हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। बैल, कुत्ते, सूअर और बंदर आम हैं। कथन 3 गलत है क्योंकि घोड़े की मूर्तियाँ अत्यंत दुर्लभ हैं (लोथल आदि से अपवादस्वरूप प्राप्त) और ये बैलों से अधिक नहीं हैं।"
    ),
    # Q39
    (
        "हड़प्पा के बर्तनों के भट्टों (kilns) के तकनीकी पहलुओं के संदर्भ में, निम्नलिखित में से कौन सा सही है?",
        ["बर्तनों को उन्नत ऊर्ध्वप्रवाह (updraft) भट्टों में पकाया जाता था, जिनमें अलग ईंधन कक्ष और गर्मी के संचलन के लिए छिद्रित फर्श होते थे।", "बर्तनों को केवल खुली अलाव की आग में पकाया जाता था, जिसके परिणामस्वरूप असमान काले धब्बे बन जाते थे।", "उच्च तापमान प्राप्त करने के लिए भट्टों में विशेष रूप से आयातित मेसोपोटामिया के कोयले का उपयोग किया जाता था।", "घरों को गर्म रखने के लिए सभी बर्तनों के भट्टे आवासीय शयनकक्षों के अंदर स्थित थे।"],
        0,
        "हड़प्पा के मृदभांडों को उन्नत ऊर्ध्वप्रवाह (updraft) भट्टियों में पकाया जाता था, जिनमें छिद्रित फर्श के नीचे ईंधन कक्ष बने होते थे, जिससे गर्मी समान रूप से फैलती थी। वे कोयले या बेडरूम में भट्टियों का उपयोग नहीं करते थे।"
    ),
    # Q48
    (
        "हड़प्पा कला से सामाजिक-सांस्कृतिक निष्कर्षों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पहियों वाली गाड़ियाँ और सरकने वाले बंदर जैसे खिलौनों की उपस्थिति एक शांत और स्थिर समाज को दर्शाती है जहाँ फुर्सत का समय था।\n2. मुहरों और बाटों की उच्च एकरूपता एक मजबूत केंद्रीय प्रशासन या व्यापारी संघ (गिल्ड) प्रणाली की ओर इशारा करती है।\n3. मुहरों पर रक्षात्मक हथियारों के प्रचुर चित्रण से एक अत्यधिक सैन्यवादी साम्राज्य का पता चलता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। खिलौने फुर्सत और शांति को दर्शाते हैं। बाटों की एकरूपता गिल्ड दर्शाती है। कथन 3 गलत है क्योंकि मुहरों पर कभी भी हथियारों या युद्ध के दृश्यों का चित्रण नहीं मिला है।"
    ),
    # Q49
    (
        "कांस्य 'नर्तकी' और प्रस्तर 'पुरोहित राजा' के बीच शैलीगत अंतर के संदर्भ में निम्नलिखित में से कौन सा सही है?",
        ["नर्तकी कांस्य की है और उसमें लचीलापन व गतिशीलता है, जबकि पुरोहित राजा पत्थर की प्रतिमा है और उसमें स्थिरता व औपचारिक कठोरता है।", "नर्तकी मिट्टी की मूर्ति है और पुरोहित राजा धातु की ढलाई है।", "दोनों मूर्तियाँ एक जैसी कठोर मुद्रा दर्शाती हैं और इन्हें एक ही राजा के कलाकार ने बनाया था।", "नर्तकी मेसोपोटामिया की शैली की है जबकि पुरोहित राजा विशुद्ध भारतीय शैली का है।"],
        0,
        "कांस्य नर्तकी त्रिभंग में लचीलापन और गति दर्शाती है, जबकि सेलखड़ी पुरोहित राजा में औपचारिक स्थिरता और कठोरता है।"
    ),
    # Q50
    (
        "हड़प्पा कलाकृतियों के संरक्षण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. धातु और पत्थर की मूर्तियाँ मिट्टी में सुरक्षित रहीं, जबकि लकड़ी और कपड़ों जैसी जैविक वस्तुएँ नष्ट हो गईं।\n2. मिट्टी की कच्ची सीलें (sealings) इसलिए बच गईं क्योंकि गोदामों में आग लगने से वे दुर्घटनावश पक गईं।\n3. उत्तर-हड़प्पा काल में आक्रमणकारियों ने योजनाबद्ध तरीके से पत्थर की सभी मूर्तियों को विकृत और नष्ट कर दिया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कपड़ों और लकड़ी का विनाश हुआ। मिट्टी की सीलें आग लगने से पकने के कारण बची रहीं। कथन 3 गलत है क्योंकि आक्रमणकारियों द्वारा मूर्तियों को बड़े पैमाने पर तोड़े जाने का कोई पुरातात्विक साक्ष्य नहीं है।"
    ),
    # Q46
    (
        "सिंधु घाटी की मुहरों की तुलना समकालीन मेसोपोटामिया की मुहरों से करें:\n1. हड़प्पा की मुहरें मुख्य रूप से चौकोर या आयताकार सेलखड़ी की स्टैम्प हैं, जबकि मेसोपोटामिया की मुहरें बेलनाकार (cylinder) हैं जिन्हें मिट्टी पर घुमाया जाता था।\n2. मेसोपोटामिया की मुहरों पर जटिल युद्धों और शाही भोजों का अंकन है, जबकि हड़प्पा मुहरों पर केवल पशु और संक्षिप्त लिपि है।\n3. दोनों सभ्यताओं में मुहरों का उपयोग मिट्टी के पार्सल के बजाय पपीरस के दस्तावेजों पर मोहर लगाने के लिए किया जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। हड़प्पा की मुहरें वर्गाकार हैं और मेसोपोटामिया की बेलनाकार। मेसोपोटामिया में जटिल दृश्य और हड़प्पा में पशु केंद्रित दृश्य हैं। कथन 3 गलत है क्योंकि दोनों जगह इनका उपयोग मिट्टी के पार्सल पर होता था, पपीरस पर नहीं।"
    ),
    # Q47
    (
        "पुरोहित राजा और मेसोपोटामिया के शासकों के चित्रण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मेसोपोटामिया के गुड़िया (Gudea of Lagash) की विशाल मूर्तियों के विपरीत, हड़प्पा का पुरोहित राजा केवल 17.5 सेमी की छोटी प्रतिमा है।\n2. पुरोहित राजा की शाल पर तिपतिया डिज़ाइन मेसोपोटामिया के दिव्य परिधानों के समान है।\n3. पुरोहित राजा की प्रतिमा मोहनजोदड़ो में एक विशाल शाही महलनुमा कब्र के अंदर से मिली थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। पुरोहित राजा बहुत छोटा है, और तिपतिया डिज़ाइन मेसोपोटामिया के समान है। कथन 3 गलत है क्योंकि हड़प्पा में कोई राजसी कब्र या महल नहीं मिला है; यह प्रतिमा एक साधारण रिहायशी घर से मिली थी।"
    )
]

mock_raw_hin = [
    # M1
    (
        "मोहनजोदड़ो से प्राप्त सेलखड़ी के 'पुरोहित राजा' (Priest-King) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उन्होंने सिर पर एक गोल पट्टी (fillet) पहनी है जिसके केंद्र में एक गोल चक्र बना है।\n2. उनकी शाल पर तिपतिया (trefoil) डिज़ाइन बना है जो मूल रूप से लाल रंग से भरा था।\n3. मूर्ति में मूंछें साफ की गई हैं और दाढ़ी करीने से संवारी हुई है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        3,
        "तीनों कथन सही हैं। पुरोहित राजा के सिर पर पट्टी, शाल पर लाल तिपतिया डिज़ाइन और संवारी दाढ़ी व साफ ऊपरी होंठ हैं।"
    ),
    # M2
    (
        "मोहनजोदड़ो की कांस्य 'नर्तकी' (Dancing Girl) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इस लघु मूर्ति को लुप्त मोम (cire perdue) तकनीक से कांसे में ढाला गया था।\n2. वह त्रिभंग मुद्रा में खड़ी है, जिसमें उसके शरीर में तीन झुकाव दिखाई देते हैं।\n3. उसका दायां हाथ 24-25 चूड़ियों से ढका है जबकि बाएं हाथ में केवल 4 चूड़ियां हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि वह अपनी *बाईं* बांह में 24-25 चूड़ियां और *दाहिनी* बांह पर केवल 4 चूड़ियां/बाजूबंद पहने हुए है।"
    ),
    # M3
    (
        "हड़प्पा मुहरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सेलखड़ी की मुहरों को भट्टी में पकाने से वे कठोर होकर एन्सटाइट में बदल जाती थीं।\n2. चौकोर मुहरों पर पशु और लिपि दोनों होते हैं, जबकि आयताकार मुहरों पर केवल लिपि होती है।\n3. मुहरों का उपयोग अंतर्राष्ट्रीय व्यापार में मानक धातु मुद्रा (coins) के रूप में किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। पकाने पर सेलखड़ी एन्सटाइट में बदलती है। आयताकार मुहरों पर केवल लेख होता है। कथन 3 गलत है क्योंकि मुहरें मुद्रा नहीं थीं, वे व्यापारिक सुरक्षा पहचान पत्र थीं।"
    ),
    # M4
    (
        "हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ के संदर्भ में निम्नलिखित में से कौन सा/से कथन सही है/हैं?\n1. यह पेट और छाती की मांसपेशियों के सजीव चित्रण को दर्शाता है जो प्राचीन काल की विशिष्ट कला से भिन्न है।\n2. इसके गर्दन और कंधों पर सॉकेट छेद बने हैं ताकि हाथ-पैर जोड़े जा सकें।\n3. यह नगर के केंद्रीय सार्वजनिक हॉल में स्थापित एक आदमकद (life-sized) प्रतिमा है।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। यह अत्यंत यथार्थवादी लघु धड़ है जिसमें अलग होने वाले अंग लगाने के लिए सॉकेट हैं। कथन 3 गलत है क्योंकि यह एक छोटी (9.5 सेमी) मूर्ति है, कोई विशाल स्मारक नहीं।"
    ),
    # M5
    (
        "हड़प्पा की मिट्टी की मातृदेवी की मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इन्हें अत्यधिक समानता प्राप्त करने के लिए दो तरफा मिट्टी के सांचों में ढाला जाता था।\n2. इनके सिर पर पंखे जैसा बड़ा मुकुट और दोनों तरफ प्यालेनुमा आकृतियां होती थीं।\n3. प्यालों के अंदर मिली कालिख दर्शाती है कि घरेलू अनुष्ठानों में इनमें तेल के दीये या धूप जलाई जाती थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["2 और 3 केवल", "1 और 2 केवल", "1 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 2 और 3 सही हैं। इनके सिर पर पंखे जैसा मुकुट और कालिख वाले प्याले हैं जिनका उपयोग पूजा में होता था। कथन 1 गलत है क्योंकि ये हाथ से गढ़ी जाती थीं, सांचे से नहीं।"
    ),
    # M6
    (
        "परिपक्व हड़प्पा कालीन चित्रित मृदभांडों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बर्तनों का मूल रंग लाल होता था जो पकाने से पहले लोहे के लाल लेप (गेरू) से प्राप्त किया जाता था।\n2. चित्रकारी के लिए काले रंग का उपयोग किया जाता था जो मैंगनीज आधारित पिगमेंट से बनता था।\n3. सबसे आम आकृतियों में ज्यामितीय वृत्त, पीपल के पत्ते और मछली के शल्क शामिल हैं।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं। हड़प्पा के बर्तन चाक पर बने लाल-काले बर्तन हैं जिन पर मैंगनीज काले रंग से वृत्त, पीपल पत्ते और मछली शल्क के डिज़ाइन उकेरे जाते थे।"
    ),
    # M7
    (
        "निम्नलिखित में से किस स्थल से कांस्य का आक्रामक सांड और ईंटों से बनी अग्नि वेदियाँ मिली हैं?",
        ["कालीबंगन", "लोथल", "मोहनजोदड़ो", "हड़प्पा"],
        0,
        "कालीबंगन से कांस्य का सांड और यज्ञ कुंड (अग्नि वेदियाँ) दोनों प्राप्त हुए हैं।"
    ),
    # M8
    (
        "हड़प्पा कालीन तांबे की पट्टिकाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इनके एक तरफ पशु या देवता का चित्र और दूसरी तरफ लिपि उत्कीर्ण होती है।\n2. ये मोहनजोदड़ो और हड़प्पा में प्रचुर मात्रा में पाई गई हैं।\n3. इनका उपयोग बाजार में खुदरा व्यापार के सिक्कों के रूप में होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        ["1 और 2 केवल", "1 केवल", "2 और 3 केवल", "1, 2 और 3"],
        0,
        "कथन 1 और 2 सही हैं। तांबे की पट्टिकाओं पर एक तरफ जानवर/देवता और दूसरी तरफ लेख है। ये मोहनजोदड़ो और हड़प्पा से मिली हैं। कथन 3 गलत है क्योंकि इनका उपयोग सुरक्षात्मक ताबीज के रूप में होता था, सिक्कों की तरह नहीं।"
    ),
    # M9
    (
        "हड़प्पा कला में पशुओं के चित्रण के संदर्भ में निम्नलिखित में से कौन सा सही है?",
        ["मुहरों और बर्तनों पर शेर का चित्रण पूरी तरह से अनुपस्थित है, जबकि बाघ का चित्रण मिलता है।", "वर्गाकार सेलखड़ी की मुहरों पर चित्रित होने वाला सबसे आम पशु घोड़ा है।", "तांबे की पट्टियों पर हाथियों का शिकार करने के दृश्यों का व्यापक अंकन है।", "मुहरों पर सभी पशु तीन सिरों वाले काल्पनिक जीव हैं।"],
        0,
        "शेर का चित्रण पूरी तरह अनुपस्थित है, जबकि बाघ का चित्रण मिलता है। सबसे आम जीव यूनिकॉर्न है, घोड़ा नहीं। शिकार के दृश्य दुर्लभ हैं, और अधिकांश पशु वास्तविक हैं।"
    ),
    # M10
    (
        "लोथल से प्राप्त मिट्टी की सील (clay sealings) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इनके एक तरफ मुहरों की छाप और दूसरी तरफ पैकिंग रस्सियों या चटाई के निशान बने हैं।\n2. ये इसलिए बची रहीं क्योंकि गोदामों में लगी आग में ये दुर्घटनावश पक गई थीं।\n3. ये प्रमाणित करती हैं कि लोथल एक सक्रिय व्यापारिक बंदरगाह था जहाँ सामान पैक और भेजा जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        ["1, 2 और 3", "1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल"],
        0,
        "तीनों कथन सही हैं। लोथल की सीलें रस्सियों/चटाइयों के निशान दिखाती हैं, आग लगने से पकीं और बंदरगाह की व्यापारिक पैकिंग गतिविधियों को साबित करती हैं।"
    )
]

# We need to compile these lists into practiceQuestions and mockTestQuestions arrays inside eng_data and hin_data respectively.
# We also have to handle formatting and indexing correctly.
# Let's map practiceQuestions and mockTestQuestions

# Convert raw practice list into expected dict format
for item in practice_raw_eng:
    q, opts, ans, sol = item
    eng_data["practiceQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for item in practice_raw_hin:
    q, opts, ans, sol = item
    hin_data["practiceQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Convert raw mock list into expected dict format
for item in mock_raw_eng:
    q, opts, ans, sol = item
    eng_data["mockTestQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

for item in mock_raw_hin:
    q, opts, ans, sol = item
    hin_data["mockTestQuestions"].append({
        "q": q,
        "opts": opts,
        "ans": ans,
        "sol": sol
    })

# Paths to output files
eng_out = os.path.join(ENG_DIR, "content.json")
hin_out = os.path.join(HIN_DIR, "content.json")

print(f"Writing English base content to {eng_out}")
with open(eng_out, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

print(f"Writing Hindi base content to {hin_out}")
with open(hin_out, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Base build script executed successfully!")
