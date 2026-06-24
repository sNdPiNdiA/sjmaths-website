# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "types-of-farming"
TOPIC_DISPLAY = "Types of Farming"
TOPIC_DISPLAY_HI = "कृषि के प्रकार"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\agriculture-commerce-trade\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "Agriculture, Commerce & Trade",
    "parentUrl": "../",
    "current": "Types of Farming"
}

hero_en = {
    "title": "Types of Farming",
    "description": "Master the classification of agricultural systems, from subsistence (shifting, nomadic, intensive) to commercial (plantation, mixed, extensive) and sustainable farming models."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Types of Farming Mock Test",
        "description": "Test your knowledge of agricultural systems, shifting cultivation terms, intensive vs extensive features, and modern farming methods. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Evolution of Farming Systems",
    "description": "How farming systems transitioned from ancient subsistence to modern technology-driven methods.",
    "cards": [
        {
            "period": "Neolithic Revolution",
            "date": "10,000 BCE",
            "details": "Transition from hunting-gathering to settled primitive subsistence farming. Domestication of crops and animals begins."
        },
        {
            "period": "Traditional Shifting Cultivation",
            "date": "Pre-Colonial Era",
            "details": "Widespread practice of slash-and-burn agriculture (Jhuming) across forest communities globally, adapted to low population densities."
        },
        {
            "period": "Colonial Plantation Era",
            "date": "17th-19th Century",
            "details": "European colonizers introduce commercial plantation agriculture (tea, coffee, rubber, cotton) in tropical colonies for export markets."
        },
        {
            "period": "Green Revolution",
            "date": "1960s-1970s",
            "details": "Introduction of High-Yielding Varieties (HYV), synthetic fertilizers, and mechanical inputs, giving rise to intensive commercial and subsistence farming."
        },
        {
            "period": "Precision & Sustainable Agriculture",
            "date": "2000s-Present",
            "details": "Rise of organic farming, vertical hydroponics, and precision farming using IoT, GPS, and drones to optimize resource efficiency."
        }
    ]
}

mnemonics_en = {
    "title": "Farming Systems Mnemonics",
    "description": "Quick memory aids for regional names of shifting agriculture and key distinctions.",
    "items": [
        {
            "title": "Mnemonic 1: Shifting Cultivation Global Names",
            "phrase": "\"MILPA is in MEXICO, LADANG in MALAYSIA, ROCA in BRAZIL\"",
            "decryption": "Remember the regional terms for slash-and-burn farming:<br>1. **Milpa** — Mexico & Central America<br>2. **Ladang** — Malaysia & Indonesia<br>3. **Roca** — Brazil<br>4. **Jhum** — Northeast India"
        },
        {
            "title": "Mnemonic 2: Shifting Cultivation Indian Names",
            "phrase": "\"P-M-D-K (Podu - Andhra, Mashan - MP, Dahiya - MP, Kumari - Western Ghats)\"",
            "decryption": "Local Indian names for shifting cultivation:<br>• **Podu / Penda** — Andhra Pradesh<br>• **Bewar / Dahiya / Mashan** — Madhya Pradesh<br>• **Kumari** — Western Ghats (Kerala/Karnataka)<br>• **Kuruwa** — Jharkhand"
        },
        {
            "title": "Mnemonic 3: Mixed Farming vs Mixed Cropping",
            "phrase": "\"MIXED FARMING = Crops + Cow\"",
            "decryption": "Never confuse mixed cropping (growing two crops together) with **Mixed Farming**. Mixed farming strictly means growing **crops** AND rearing **livestock** (cows, sheep, poultry) on the same agricultural holding."
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What is the primary objective of subsistence farming?",
            "answer": "To meet the consumption needs of the **farmer's family**, with little or no surplus left for sale in the market.",
            "icon": "fa-house-user"
        },
        {
            "question": "Which agricultural system is characterized by a single cash crop on a massive estate?",
            "answer": "**Plantation Agriculture**. Examples include tea in Assam, coffee in Brazil, and rubber in Malaysia.",
            "icon": "fa-tree"
        },
        {
            "question": "What is Nomadic Herding (Pastoral Nomadism)?",
            "answer": "A primitive subsistence system where herders move from place to place with their animals for fodder and water along defined routes (e.g. Bhotiyas/Gujjars in Himalayas).",
            "icon": "fa-cow"
        },
        {
            "question": "Why is Shifting Cultivation highly criticized in modern environmental science?",
            "answer": "Because it causes **deforestation**, loss of biodiversity, and severe **soil erosion** due to the continuous clearing of forest patches.",
            "icon": "fa-fire"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing Mixed Farming with Mixed Cropping. Mixed farming is crop production + animal husbandry. Mixed cropping is simply growing two or more crops simultaneously on the same land.",
        "<strong>Trap 2:</strong> Believing Extensive Commercial Grain Cultivation has high yield per hectare. In extensive farming, yield per hectare is **low** (due to huge farm sizes and less intensive input per unit area), but yield per worker is **very high**.",
        "<strong>Trap 3:</strong> Assuming plantation crops are food crops for local subsistence. Plantation agriculture is entirely commercial, capital-intensive, export-oriented, and usually run as an industrial estate.",
        "<strong>Trap 4:</strong> Thinking shifting cultivation is permanently settled. It is a migratory form of farming where the fields shift every 2-3 years, while the farmer's settlement may or may not move."
    ]
}

deep_dive_en = [
    {
        "title": "1. Subsistence Farming Systems",
        "content": """<p>Subsistence farming is categorized into primitive and intensive systems, depending on the level of technology and land availability.</p>
        <ul>
          <li><strong>Primitive Subsistence (Shifting Cultivation & Nomadic Herding):</strong> Characterized by small plots, use of primitive tools (hoe, dao, digging sticks), and reliance on monsoon/natural fertility. Also known as slash-and-burn or <em>Jhuming</em> in Northeast India.</li>
          <li><strong>Intensive Subsistence:</strong> Found in densely populated regions of monsoon Asia. Farms are small, but high inputs of labor, manures, and irrigation are used to get maximum yield from the limited land. Double or triple cropping is common.</li>
        </ul>
        
        <!-- SVG Farming Classification Diagram -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .title-svg{font-family:'Outfit',sans-serif;font-weight:bold;fill:var(--text-dark,#2c3e50);font-size:15px;}
            .box-main{fill:rgba(142,68,173,0.1);stroke:#8e44ad;stroke-width:2;}
            .box-sub{fill:rgba(52,152,219,0.1);stroke:#3498db;stroke-width:1.5;}
            .box-hl{fill:rgba(46,204,113,0.1);stroke:#2ecc71;stroke-width:1.5;}
            .text-main{font-family:'Inter',sans-serif;font-size:11px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .text-desc{font-family:'Inter',sans-serif;font-size:10px;fill:#666;}
            .line-connect{stroke:#7f8c8d;stroke-width:1.5;fill:none;}
            
            
            
            
            
            
          </style>
          <text x="400" y="25" class="title-svg" text-anchor="middle">Classification of Farming Systems</text>
          
          <!-- Center Node -->
          <rect x="300" y="45" width="200" height="40" class="box-main" rx="20" />
          <text x="400" y="69" class="text-main" text-anchor="middle">Types of Farming</text>
          
          <!-- Lines -->
          <path d="M 400,85 L 400,110 L 180,110 L 180,130" class="line-connect" />
          <path d="M 400,85 L 400,110 L 620,110 L 620,130" class="line-connect" />
          
          <!-- Subsistence Node -->
          <rect x="80" y="130" width="200" height="60" class="box-sub" rx="6" />
          <text x="180" y="152" class="text-main" text-anchor="middle">Subsistence Farming</text>
          <text x="180" y="170" class="text-desc" text-anchor="middle">1. Primitive (Shifting, Nomadic)</text>
          <text x="180" y="182" class="text-desc" text-anchor="middle">2. Intensive (High labor, small land)</text>
          
          <!-- Commercial Node -->
          <rect x="520" y="130" width="200" height="60" class="box-hl" rx="6" />
          <text x="620" y="152" class="text-main" text-anchor="middle">Commercial Farming</text>
          <text x="620" y="170" class="text-desc" text-anchor="middle">1. Plantation (Tea, Coffee, Rubber)</text>
          <text x="620" y="182" class="text-desc" text-anchor="middle">2. Extensive Grain / Mixed Farming</text>
        </svg>"""
    },
    {
        "title": "2. Commercial Farming Systems",
        "content": """<p>Commercial farming uses modern inputs like HYV seeds, chemical fertilizers, and insecticides to achieve higher yields for sale in national or international markets.</p>
        <ul>
          <li><strong>Commercial Grain Cultivation:</strong> Practiced in temperate grasslands (Prairies, Steppes, Pampas). Farms are massive (hundreds of hectares), highly mechanized, and specialize in single grains like wheat or maize.</li>
          <li><strong>Mixed Farming:</strong> Common in Europe and North America. Crops (wheat, barley, oats, fodder) are grown alongside animal husbandry. Crop rotation is strictly followed to maintain soil fertility.</li>
          <li><strong>Plantation Agriculture:</strong> Introduced by Europeans in the tropics. Characterized by large estates, single-crop specialization, heavy capital investment, scientific methods, and processing facilities on or near the estate.</li>
        </ul>"""
    },
    {
        "title": "3. Shifting Cultivation: Regional & Global Nomenclature",
        "content": """<p>Shifting cultivation is known by different local names globally and within India. It is a frequent area of questioning in competitive exams:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Region</th>
                <th>Local Name</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Northeast India (Assam, Meghalaya, Mizoram)</strong></td>
                <td>Jhum / Jhuming</td>
              </tr>
              <tr>
                <td><strong>Madhya Pradesh</strong></td>
                <td>Bewar, Dahiya, Mashan</td>
              </tr>
              <tr>
                <td><strong>Andhra Pradesh / Odisha</strong></td>
                <td>Podu, Penda</td>
              </tr>
              <tr>
                <td><strong>Western Ghats (Kerala, Karnataka)</strong></td>
                <td>Kumari</td>
              </tr>
              <tr>
                <td><strong>Mexico & Central America</strong></td>
                <td>Milpa</td>
              </tr>
              <tr>
                <td><strong>Venezuela</strong></td>
                <td>Conuco</td>
              </tr>
              <tr>
                <td><strong>Brazil</strong></td>
                <td>Roca</td>
              </tr>
              <tr>
                <td><strong>Central Africa</strong></td>
                <td>Masole</td>
              </tr>
              <tr>
                <td><strong>Malaysia & Indonesia</strong></td>
                <td>Ladang</td>
              </tr>
              <tr>
                <td><strong>Vietnam</strong></td>
                <td>Ray</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "4. Modern & Sustainable Farming Methods",
        "content": """<p>To feed growing populations while preserving ecosystems, agriculture is adopting sustainable farming systems:</p>
        <ul>
          <li><strong>Organic Farming:</strong> Replaces chemical inputs with organic manures, bio-fertilizers, and natural pest control to maintain eco-health.</li>
          <li><strong>Precision Agriculture:</strong> Uses technology (GPS, remote sensing, drones) to supply exact amounts of water, seeds, and nutrients, avoiding wastage.</li>
          <li><strong>Dryland Farming:</strong> Adopted in regions with less than 75 cm annual rainfall. Focuses on moisture conservation and drought-resistant crops (millets, pulses).</li>
          <li><strong>Vertical Farming & Hydroponics:</strong> Cultivating plants indoors in stacked layers, using nutrient-rich water solutions without soil. Highly space and water efficient.</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "कृषि, वाणिज्य और व्यापार",
    "parentUrl": "../",
    "current": "कृषि के प्रकार"
}

hero_hi = {
    "title": "कृषि के प्रकार",
    "description": "जीविका कृषि (स्थानांतरित, खानाबदोश, गहन) से लेकर वाणिज्यिक (रोपड़, मिश्रित, विस्तृत) और सतत कृषि मॉडलों तक, विभिन्न कृषि प्रणालियों के वर्गीकरण पर महारत हासिल करें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव कृषि प्रकार मॉक टेस्ट",
        "description": "कृषि प्रणालियों, झूम खेती के क्षेत्रीय नाम, गहन बनाम विस्तृत कृषि विशेषताओं और आधुनिक कृषि विधियों पर अपने ज्ञान का परीक्षण करें। समयबद्ध 15-प्रश्न मॉक टेस्ट।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "कृषि प्रणालियों का विकास",
    "description": "प्राचीन जीविका कृषि से आधुनिक प्रौद्योगिकी आधारित विधियों तक कृषि का सफर।",
    "cards": [
        {
            "period": "नवपाषाण क्रांति (Neolithic)",
            "date": "10,000 ईसा पूर्व",
            "details": "शिकार और भोजन संग्रह से निकलकर स्थिर आदिम जीविका कृषि की शुरुआत। फसलों और पशुओं का पालतूकरण शुरू हुआ।"
        },
        {
            "period": "पारंपरिक स्थानांतरित कृषि",
            "date": "पूर्व-औपनिवेशिक काल",
            "details": "कम जनसंख्या घनत्व वाले क्षेत्रों में वन समुदायों द्वारा बड़े पैमाने पर 'काटो और जलाओ' (स्लैश-एंड-बर्न) कृषि का उपयोग किया गया।"
        },
        {
            "period": "औपनिवेशिक रोपण युग",
            "date": "17वीं-19वीं शताब्दी",
            "details": "यूरोपीय औपनिवेशिक ताकतों ने उष्णकटिबंधीय क्षेत्रों में निर्यात के लिए वाणिज्यिक रोपण कृषि (चाय, कॉफी, रबर, कपास) की शुरुआत की।"
        },
        {
            "period": "हरित क्रांति",
            "date": "1960s-1970s",
            "details": "उच्च उपज देने वाली किस्मों (HYV बीज), रासायनिक उर्वरकों और मशीनीकृत उपकरणों की मदद से गहन कृषि का तेजी से विकास हुआ।"
        },
        {
            "period": "सटीक और सतत कृषि",
            "date": "2000s-वर्तमान",
            "details": "जैविक खेती, हाइड्रोपोनिक्स और आईओटी, जीपीएस तथा ड्रोन के उपयोग से संसाधन दक्षता बढ़ाने पर ध्यान केंद्रित किया गया।"
        }
    ]
}

mnemonics_hi = {
    "title": "कृषि प्रकार के स्मृति सूत्र",
    "description": "क्षेत्रीय झूम खेती के नामों और महत्वपूर्ण अंतरों को जल्दी याद रखने के लिए आसान ट्रिक्स।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: स्थानांतरित कृषि के वैश्विक नाम",
            "phrase": "\"MILPA is in MEXICO, LADANG in MALAYSIA, ROCA in BRAZIL\"",
            "decryption": "विश्व में स्थानांतरित कृषि के विभिन्न क्षेत्रीय नामों को याद करें:<br>1. **Milpa (मिल्पा)** — मेक्सिको और मध्य अमेरिका<br>2. **Ladang (लदांग)** — मलेशिया और इंडोनेशिया<br>3. **Roca (रोका)** — ब्राजील<br>4. **Jhum (झूम)** — उत्तर-पूर्वी भारत"
        },
        {
            "title": "स्मृति सूत्र 2: स्थानांतरित कृषि के भारतीय नाम",
            "phrase": "\"P-M-D-K (पोडू - आंध्र, माशान - एमपी, दहिया - एमपी, कुमारी - पश्चिमी घाट)\"",
            "decryption": "भारत में झूम खेती के क्षेत्रीय नाम:<br>• **Podu (पोडू) / Penda (पेंडा)** — आंध्र प्रदेश<br>• **Bewar (बेवार) / Dahiya (दहिया) / Mashan (माशान)** — मध्य प्रदेश<br>• **Kumari (कुमारी)** — पश्चिमी घाट (केरल/कर्नाटक)<br>• **Kuruwa (कुरुवा)** — झारखंड"
        },
        {
            "title": "स्मृति सूत्र 3: मिश्रित खेती और मिश्रित फसल में अंतर",
            "phrase": "\"मिश्रित खेती (Mixed Farming) = फसलें + गाय/पशु\"",
            "decryption": "मिश्रित फसल (एक साथ दो फसलें उगाना) को **मिश्रित खेती** के साथ भ्रमित न करें। मिश्रित खेती का सीधा अर्थ है एक ही खेत पर **फसल उत्पादन** के साथ-साथ **पशुपालन** (गाय, भेड़, मुर्गी पालन आदि) करना।"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "जीविका कृषि का प्राथमिक उद्देश्य क्या होता है?",
            "answer": "किसान के **परिवार की उपभोग आवश्यकताओं** को पूरा करना, जिसमें बाजार में बेचने के लिए बहुत कम या कोई अधिशेष (surplus) नहीं बचता है।",
            "icon": "fa-house-user"
        },
        {
            "question": "किस कृषि प्रणाली में एक बड़े क्षेत्र पर केवल एक ही नकदी फसल उगाई जाती है?",
            "answer": "**रोपण कृषि (Plantation Agriculture)**। उदाहरण के लिए असम में चाय, ब्राजील में कॉफी और मलेशिया में रबर की खेती।",
            "icon": "fa-tree"
        },
        {
            "question": "चलवासी पशुचारण (Nomadic Herding) क्या है?",
            "answer": "यह एक आदिम जीविका प्रणाली है जिसमें पशुचारक चारे और पानी की खोज में अपने पशुओं के साथ निश्चित मार्गों पर घूमते हैं (जैसे हिमालय के भोटिया/गुज्जर)।",
            "icon": "fa-cow"
        },
        {
            "question": "आधुनिक पर्यावरण विज्ञान में स्थानांतरित कृषि (झूम खेती) की आलोचना क्यों की जाती है?",
            "answer": "क्योंकि इसके कारण वनों की कटाई (**Deforestation**), जैव विविधता का नुकसान और लगातार जंगल साफ करने से **मृदा अपरदन** (Soil Erosion) होता है।",
            "icon": "fa-fire"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> मिश्रित खेती (Mixed Farming) को मिश्रित फसल (Mixed Cropping) समझना। मिश्रित खेती = फसल उत्पादन + पशुपालन। मिश्रित फसल = एक ही भूमि पर एक साथ दो या अधिक फसलें उगाना।",
        "<strong>भ्रम 2:</strong> यह मानना कि विस्तृत वाणिज्यिक अनाज कृषि में प्रति हेक्टेयर उपज बहुत अधिक होती है। विस्तृत कृषि में प्रति हेक्टेयर उपज **कम** होती है (बड़े खेत आकार के कारण), लेकिन प्रति श्रमिक उत्पादकता **बहुत अधिक** होती है।",
        "<strong>भ्रम 3:</strong> रोपण फसलों को स्थानीय जीविका के लिए खाद्य फसल मानना। रोपण कृषि पूरी तरह से वाणिज्यिक, पूंजी-प्रधान, निर्यात-उन्मुख और औद्योगिक रूप से प्रबंधित होती है।",
        "<strong>भ्रम 4:</strong> स्थानांतरित खेती को पूरी तरह स्थायी समझना। यह खेती का एक प्रवासी रूप है जहां खेत हर 2-3 साल में बदल जाते हैं, जबकि किसानों की बस्ती बदल भी सकती है और नहीं भी।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. जीविका कृषि प्रणालियां (Subsistence Farming)",
        "content": """<p>भूमि की उपलब्धता और तकनीकी स्तर के आधार पर जीविका कृषि को आदिम और गहन प्रणालियों में वर्गीकृत किया जाता है।</p>
        <ul>
          <li><strong>आदिम जीविका कृषि (स्थानांतरित खेती और चलवासी पशुचारण):</strong> छोटे भूखंडों, आदिम औजारों (कुदाल, दाव, खुदाई करने वाली छड़ें) के उपयोग और मानसूनी वर्षा व प्राकृतिक मिट्टी की उर्वरता पर निर्भरता इसकी विशेषता है। इसे भारत के उत्तर-पूर्व में 'झूम खेती' भी कहा जाता है।</li>
          <li><strong>गहन जीविका कृषि (Intensive Subsistence):</strong> यह मानसून एशिया के घने बसे हुए क्षेत्रों में पाई जाती है। भूखंड छोटे होते हैं, लेकिन सीमित भूमि से अधिकतम उपज प्राप्त करने के लिए श्रम, खाद और सिंचाई का उच्च स्तर पर उपयोग किया जाता है। एक वर्ष में दो या तीन फसलें उगाना आम बात है।</li>
        </ul>
        
        <!-- SVG Farming Classification Diagram -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .title-svg{font-family:'Outfit',sans-serif;font-weight:bold;fill:var(--text-dark,#2c3e50);font-size:15px;}
            .box-main{fill:rgba(142,68,173,0.1);stroke:#8e44ad;stroke-width:2;}
            .box-sub{fill:rgba(52,152,219,0.1);stroke:#3498db;stroke-width:1.5;}
            .box-hl{fill:rgba(46,204,113,0.1);stroke:#2ecc71;stroke-width:1.5;}
            .text-main{font-family:'Inter',sans-serif;font-size:11px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .text-desc{font-family:'Inter',sans-serif;font-size:10px;fill:#666;}
            .line-connect{stroke:#7f8c8d;stroke-width:1.5;fill:none;}
            
            
            
            
            
            
          </style>
          <text x="400" y="25" class="title-svg" text-anchor="middle">कृषि प्रणालियों का वर्गीकरण</text>
          
          <!-- Center Node -->
          <rect x="300" y="45" width="200" height="40" class="box-main" rx="20" />
          <text x="400" y="69" class="text-main" text-anchor="middle">कृषि के प्रकार</text>
          
          <!-- Lines -->
          <path d="M 400,85 L 400,110 L 180,110 L 180,130" class="line-connect" />
          <path d="M 400,85 L 400,110 L 620,110 L 620,130" class="line-connect" />
          
          <!-- Subsistence Node -->
          <rect x="80" y="130" width="200" height="60" class="box-sub" rx="6" />
          <text x="180" y="152" class="text-main" text-anchor="middle">जीविका कृषि (Subsistence)</text>
          <text x="180" y="170" class="text-desc" text-anchor="middle">1. आदिम (स्थानांतरित, चलवासी)</text>
          <text x="180" y="182" class="text-desc" text-anchor="middle">2. गहन (अधिक श्रम, छोटा भूखंड)</text>
          
          <!-- Commercial Node -->
          <rect x="520" y="130" width="200" height="60" class="box-hl" rx="6" />
          <text x="620" y="152" class="text-main" text-anchor="middle">वाणिज्यिक कृषि (Commercial)</text>
          <text x="620" y="170" class="text-desc" text-anchor="middle">1. रोपण (चाय, कॉफी, रबर)</text>
          <text x="620" y="182" class="text-desc" text-anchor="middle">2. विस्तृत अनाज / मिश्रित कृषि</text>
        </svg>"""
    },
    {
        "title": "2. वाणिज्यिक कृषि प्रणालियां (Commercial Farming)",
        "content": """<p>वाणिज्यिक कृषि में राष्ट्रीय या अंतर्राष्ट्रीय बाजारों में बिक्री के लिए अधिक पैदावार प्राप्त करने हेतु आधुनिक इनपुट जैसे HYV बीजों, रासायनिक उर्वरकों और कीटनाशकों का उपयोग किया जाता है।</p>
        <ul>
          <li><strong>विस्तृत वाणिज्यिक अनाज कृषि (Commercial Grain Farming):</strong> समशीतोष्ण घास के मैदानों (प्रेयरी, स्टेपीज़, पंपास) में की जाती है। खेत बहुत बड़े होते हैं (सैकड़ों हेक्टेयर), अत्यधिक यंत्रीकृत होते हैं, और गेहूं या मक्का जैसी एकल फसलों पर ध्यान केंद्रित करते हैं।</li>
          <li><strong>मिश्रित कृषि (Mixed Farming):</strong> यूरोप और उत्तरी अमेरिका में आम है। इसमें फसल उत्पादन (गेहूं, जौ, जई, चारा) के साथ-साथ पशुपालन भी किया जाता है। मिट्टी की उर्वरता बनाए रखने के लिए फसल चक्र (Crop Rotation) का कड़ाई से पालन किया जाता है।</li>
          <li><strong>रोपण कृषि (Plantation Agriculture):</strong> यह उष्णकटिबंधीय क्षेत्रों में औपनिवेशिक ताकतों द्वारा शुरू की गई थी। इसकी विशेषताओं में बड़े बागान, एकल-फसल विशेषज्ञता, भारी पूंजी निवेश, वैज्ञानिक विधियां और प्रसंस्करण सुविधाएं शामिल हैं।</li>
        </ul>"""
    },
    {
        "title": "3. स्थानांतरित कृषि: क्षेत्रीय और वैश्विक नामकरण",
        "content": """<p>स्थानांतरित कृषि को भारत और विश्व में विभिन्न स्थानीय नामों से जाना जाता है। प्रतियोगी परीक्षाओं में इससे अक्सर मिलान वाले प्रश्न पूछे जाते हैं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>क्षेत्र / देश</th>
                <th>स्थानीय नाम</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>उत्तर-पूर्वी भारत (असम, मेघालय, मिजोरम)</strong></td>
                <td>झूम / झूमिंग</td>
              </tr>
              <tr>
                <td><strong>मध्य प्रदेश</strong></td>
                <td>बेवार, दहिया, माशान</td>
              </tr>
              <tr>
                <td><strong>आंध्र प्रदेश / ओडिशा</strong></td>
                <td>पोडू, पेंडा</td>
              </tr>
              <tr>
                <td><strong>पश्चिमी घाट (केरल, कर्नाटक)</strong></td>
                <td>कुमारी</td>
              </tr>
              <tr>
                <td><strong>मेक्सिको और मध्य अमेरिका</strong></td>
                <td>मिल्पा</td>
              </tr>
              <tr>
                <td><strong>वेनेजुएला</strong></td>
                <td>कोनुको</td>
              </tr>
              <tr>
                <td><strong>ब्राजील</strong></td>
                <td>रोका</td>
              </tr>
              <tr>
                <td><strong>मध्य अफ्रीका</strong></td>
                <td>मसोले</td>
              </tr>
              <tr>
                <td><strong>मलेशिया और इंडोनेशिया</strong></td>
                <td>लदांग</td>
              </tr>
              <tr>
                <td><strong>वियतनाम</strong></td>
                <td>रे</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "4. आधुनिक और सतत कृषि विधियां",
        "content": """<p>पारिस्थितिकी तंत्र को संरक्षित करते हुए बढ़ती आबादी का पेट भरने के लिए आधुनिक कृषि में कई सतत प्रणालियां अपनाई जा रही हैं:</p>
        <ul>
          <li><strong>जैविक खेती (Organic Farming):</strong> पारिस्थितिक स्वास्थ्य को बनाए रखने के लिए रासायनिक इनपुट के स्थान पर जैविक खादों, जैव-उर्वरकों और प्राकृतिक कीट नियंत्रण विधियों का उपयोग करती है।</li>
          <li><strong>सटीक कृषि (Precision Agriculture):</strong> प्रौद्योगिकी (जीपीएस, रिमोट सेंसिंग, ड्रोन) का उपयोग करके पानी, बीज और पोषक तत्वों की सटीक मात्रा प्रदान करती है जिससे संसाधनों की बर्बादी रुकती है।</li>
          <li><strong>शुष्क भूमि कृषि (Dryland Farming):</strong> वार्षिक वर्षा 75 सेमी से कम वाले क्षेत्रों में अपनाई जाती है। इसका मुख्य ध्यान नमी संरक्षण और सूखा-प्रतिरोधी फसलों (बाजरा, दालें) पर होता है।</li>
          <li><strong>ऊर्ध्वाधर खेती (Vertical Farming) और हाइड्रोपोनिक्स:</strong> पौधों को बिना मिट्टी के पोषक तत्वों से भरपूर पानी के घोल में ऊर्ध्वाधर रूप से इनडोर परतों में उगाना। यह तकनीक पानी और स्थान दोनों की भारी बचत करती है।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "What is the primary characteristic of subsistence farming?",
        "q_hi": "जीविका कृषि (Subsistence Farming) की प्राथमिक विशेषता क्या है?",
        "opts": [
            "Use of high level of machinery and export of crops",
            "Production primarily for the self-consumption of the farmer's family",
            "Cultivation of single cash crops on giant industrial estates",
            "Relying entirely on chemical pesticides"
        ],
        "opts_hi": [
            "मशीनरी के उच्च स्तर का उपयोग और फसलों का निर्यात",
            "मुख्य रूप से किसान के परिवार के स्वयं के उपभोग के लिए उत्पादन",
            "विशाल औद्योगिक क्षेत्रों में एकल नकदी फसलों की खेती",
            "पूरी तरह से रासायनिक कीटनाशकों पर निर्भर होना"
        ],
        "ans": 1,
        "sol": "Subsistence farming is focused on meeting the dietary needs of the family, with little or no commercial sales.",
        "sol_hi": "जीविका कृषि मुख्य रूप से परिवार की पोषण संबंधी आवश्यकताओं को पूरा करने पर केंद्रित होती है, जिसमें व्यावसायिक बिक्री बहुत कम या नहीं होती है।"
    },
    {
        "q": "By what name is shifting cultivation known in Mexico and Central America?",
        "q_hi": "मेक्सिको और मध्य अमेरिका में स्थानांतरित कृषि को किस नाम से जाना जाता है?",
        "opts": ["Ladang", "Milpa", "Roca", "Ray"],
        "opts_hi": ["लदांग", "मिल्पा", "रोका", "रे"],
        "ans": 1,
        "sol": "Shifting cultivation is locally termed 'Milpa' in Mexico and Central American countries.",
        "sol_hi": "स्थानांतरित कृषि को मेक्सिको और मध्य अमेरिकी देशों में स्थानीय रूप से 'मिल्पा' कहा जाता है।"
    },
    {
        "q": "What type of agricultural practice involves growing crops and rearing livestock simultaneously on the same farm?",
        "q_hi": "एक ही खेत पर एक साथ फसलें उगाने और पशुधन पालने की कृषि पद्धति को क्या कहा जाता है?",
        "opts": ["Mixed Cropping", "Mixed Farming", "Dairy Farming", "Intensive Subsistence Farming"],
        "opts_hi": ["मिश्रित फसल", "मिश्रित खेती (Mixed Farming)", "डेयरी फार्मिंग", "गहन जीविका कृषि"],
        "ans": 1,
        "sol": "Mixed farming is characterized by the combination of crop cultivation and animal husbandry on the same landholding.",
        "sol_hi": "मिश्रित खेती की विशेषता एक ही भू-भाग पर फसल की खेती और पशुपालन के संयोजन से है।"
    },
    {
        "q": "The local name of shifting cultivation in Brazil is:",
        "q_hi": "ब्राजील में स्थानांतरित कृषि का स्थानीय नाम क्या है?",
        "opts": ["Conuco", "Masole", "Roca", "Ray"],
        "opts_hi": ["कोनुको", "मसोले", "रोका", "रे"],
        "ans": 2,
        "sol": "In Brazil, shifting cultivation is called 'Roca'.",
        "sol_hi": "ब्राजील में स्थानांतरित कृषि को 'रोका' कहा जाता है।"
    },
    {
        "q": "Which type of farming is characterized by large estates, single cash-crop focus, and heavy capital investment?",
        "q_hi": "बड़े बागानों, एकल नकदी फसल और भारी पूंजी निवेश वाली खेती की मुख्य विशेषता क्या है?",
        "opts": ["Intensive Subsistence", "Nomadic Herding", "Plantation Agriculture", "Dryland Farming"],
        "opts_hi": ["गहन जीविका कृषि", "चलवासी पशुचारण", "रोपण कृषि (Plantation Agriculture)", "शुष्क भूमि कृषि"],
        "ans": 2,
        "sol": "Plantation agriculture is a form of commercial farming where crops like tea, coffee, cocoa, and rubber are grown on large scale estates.",
        "sol_hi": "रोपण कृषि वाणिज्यिक कृषि का एक रूप है जहां बड़े पैमाने पर चाय, कॉफी, कोको और रबर जैसी फसलें उगाई जाती हैं।"
    },
    {
        "q": "What is the term for shifting cultivation in Malaysia and Indonesia?",
        "q_hi": "मलेशिया और इंडोनेशिया में स्थानांतरित कृषि के लिए क्या शब्द प्रयोग किया जाता है?",
        "opts": ["Ladang", "Ray", "Milpa", "Masole"],
        "opts_hi": ["लदांग", "रे", "मिल्पा", "मसोले"],
        "ans": 0,
        "sol": "Shifting cultivation is known as 'Ladang' in Malaysia and Indonesia.",
        "sol_hi": "स्थानांतरित कृषि को मलेशिया और इंडोनेशिया में 'लदांग' के नाम से जाना जाता है।"
    },
    {
        "q": "Which type of farming is extensively practiced in the temperate grasslands like the North American Prairies?",
        "q_hi": "उत्तरी अमेरिकी प्रेयरी जैसे समशीतोष्ण घास के मैदानों में किस प्रकार की खेती व्यापक रूप से की जाती है?",
        "opts": ["Intensive Subsistence Farming", "Extensive Commercial Grain Cultivation", "Plantation Farming", "Nomadic Herding"],
        "opts_hi": ["गहन जीविका कृषि", "विस्तृत वाणिज्यिक अनाज कृषि", "रोपण खेती", "चलवासी पशुचारण"],
        "ans": 1,
        "sol": "Temperate grasslands utilize extensive commercial grain farming where single crops (mostly wheat) are cultivated on massive farms.",
        "sol_hi": "समशीतोष्ण घास के मैदान विस्तृत वाणिज्यिक अनाज कृषि का उपयोग करते हैं जहां विशाल खेतों में एकल फसलें (ज्यादातर गेहूं) उगाई जाती हैं।"
    },
    {
        "q": "In which state of India is shifting cultivation widely known as 'Kumari'?",
        "q_hi": "भारत के किस राज्य/क्षेत्र में स्थानांतरित खेती को व्यापक रूप से 'कुमारी' के नाम से जाना जाता है?",
        "opts": ["Western Ghats", "Madhya Pradesh", "Northeast India", "Jharkhand"],
        "opts_hi": ["पश्चिमी घाट", "मध्य प्रदेश", "उत्तर-पूर्वी भारत", "झारखंड"],
        "ans": 0,
        "sol": "In the Western Ghats region (Kerala/Karnataka), shifting cultivation is locally called Kumari.",
        "sol_hi": "पश्चिमी घाट क्षेत्र (केरल/कर्नाटक) में स्थानांतरित खेती को स्थानीय रूप से 'कुमारी' कहा जाता है।"
    },
    {
        "q": "Which farming system is defined by growing crops in soil-less nutrient-rich water solutions?",
        "q_hi": "मिट्टी के बिना पोषक तत्वों से भरपूर पानी के घोल में फसल उगाने की कृषि पद्धति को क्या कहा जाता है?",
        "opts": ["Dryland Farming", "Hydroponics", "Vertical Farming", "Jhum Cultivation"],
        "opts_hi": ["शुष्क भूमि कृषि", "हाइड्रोपोनिक्स (Hydroponics)", "ऊर्ध्वाधर खेती", "झूम खेती"],
        "ans": 1,
        "sol": "Hydroponics is the technique of growing plants in water solvent containing essential nutrients, without soil.",
        "sol_hi": "हाइड्रोपोनिक्स बिना मिट्टी के, आवश्यक पोषक तत्वों वाले पानी के घोल में पौधे उगाने की तकनीक है।"
    },
    {
        "q": "In dryland farming, the annual rainfall is typically less than:",
        "q_hi": "शुष्क भूमि कृषि में वार्षिक वर्षा सामान्यतः किससे कम होती है?",
        "opts": ["150 cm", "75 cm", "200 cm", "100 cm"],
        "opts_hi": ["150 सेमी", "75 सेमी", "200 सेमी", "100 सेमी"],
        "ans": 1,
        "sol": "Dryland farming is practiced in dry regions where annual rainfall is less than 75 cm.",
        "sol_hi": "शुष्क भूमि कृषि उन शुष्क क्षेत्रों में की जाती है जहाँ वार्षिक वर्षा 75 सेमी से कम होती है।"
    },
    {
        "q": "What is 'Jhuming'?",
        "q_hi": "'झूमिंग' (Jhuming) क्या है?",
        "opts": ["A type of terrace farming", "A method of commercial fruit cultivation", "Shifting cultivation practiced in Northeast India", "A technique of fish breeding"],
        "opts_hi": ["सोपान कृषि (सीढ़ीदार खेती) का एक प्रकार", "वाणिज्यिक फल खेती की एक विधि", "उत्तर-पूर्वी भारत में की जाने वाली स्थानांतरित कृषि", "मछली पालन की एक तकनीक"],
        "ans": 2,
        "sol": "Jhuming is the traditional term for shifting cultivation (slash-and-burn) in North-Eastern states like Assam and Meghalaya.",
        "sol_hi": "झूमिंग असम और मेघालय जैसे उत्तर-पूर्वी राज्यों में स्थानांतरित खेती (काटो और जलाओ) का पारंपरिक नाम है।"
    },
    {
        "q": "Which of the following is NOT a characteristic of Extensive Commercial Grain Cultivation?",
        "q_hi": "निम्नलिखित में से कौन सी विस्तृत वाणिज्यिक अनाज कृषि की विशेषता नहीं है?",
        "opts": [
            "Large farm sizes",
            "High yield per hectare",
            "High degree of mechanization",
            "Monoculture of wheat or maize"
        ],
        "opts_hi": [
            "बड़े आकार के खेत",
            "प्रति हेक्टेयर उच्च उपज",
            "मशीनीकरण का उच्च स्तर",
            "गेहूं या मक्के की एकल फसल"
        ],
        "ans": 1,
        "sol": "Extensive commercial grain farming has low yield per hectare but very high yield per worker due to huge farm areas.",
        "sol_hi": "विस्तृत वाणिज्यिक अनाज कृषि में खेतों के विशाल आकार के कारण प्रति हेक्टेयर उपज कम होती है लेकिन प्रति श्रमिक उत्पादकता बहुत अधिक होती है।"
    },
    {
        "q": "In which region of India is the shifting cultivation known as 'Podu'?",
        "q_hi": "भारत के किस क्षेत्र में स्थानांतरित खेती को 'पोडू' कहा जाता है?",
        "opts": ["Western Ghats", "Andhra Pradesh and Odisha", "Madhya Pradesh", "Rajasthan"],
        "opts_hi": ["पश्चिमी घाट", "आंध्र प्रदेश और ओडिशा", "मध्य प्रदेश", "राजस्थान"],
        "ans": 1,
        "sol": "Podu is the local name for shifting agriculture in Andhra Pradesh and Odisha.",
        "sol_hi": "आंध्र प्रदेश और ओडिशा में स्थानांतरित कृषि का स्थानीय नाम 'पोडू' है।"
    },
    {
        "q": "What is the local name of shifting cultivation in Madhya Pradesh?",
        "q_hi": "मध्य प्रदेश में स्थानांतरित कृषि का स्थानीय नाम क्या है?",
        "opts": ["Kumari", "Podu", "Bewar", "Kuruwa"],
        "opts_hi": ["कुमारी", "पोडू", "बेवार", "कुरुवा"],
        "ans": 2,
        "sol": "In Madhya Pradesh, shifting agriculture is locally termed Bewar or Dahiya.",
        "sol_hi": "मध्य प्रदेश में स्थानांतरित कृषि को स्थानीय रूप से 'बेवार' या 'दहिया' कहा जाता है।"
    },
    {
        "q": "Plantation agriculture is a type of:",
        "q_hi": "रोपण कृषि (Plantation Agriculture) किस प्रकार की कृषि है?",
        "opts": ["Subsistence Farming", "Commercial Farming", "Nomadic Farming", "Primitive Farming"],
        "opts_hi": ["जीविका कृषि", "वाणिज्यिक कृषि", "चलवासी कृषि", "आदिम कृषि"],
        "ans": 1,
        "sol": "Plantation farming is a specialized, capital-intensive form of commercial agriculture aimed entirely at sales.",
        "sol_hi": "रोपण कृषि वाणिज्यिक कृषि का एक विशिष्ट, पूंजी-प्रधान रूप है जो पूरी तरह से बाजार बिक्री के लिए लक्षित होता है।"
    },
    {
        "q": "Rearing of animals like sheep, goats, and yaks in search of fodder along defined routes is called:",
        "q_hi": "चारे की तलाश में निश्चित मार्गों पर भेड़, बकरी और याक जैसे जानवरों को पालने की क्रिया क्या कहलाती है?",
        "opts": ["Dairy Farming", "Commercial Livestock Rearing", "Nomadic Herding", "Mixed Farming"],
        "opts_hi": ["डेयरी फार्मिंग", "वाणिज्यिक पशुधन पालन", "चलवासी पशुचारण (Nomadic Herding)", "मिश्रित खेती"],
        "ans": 2,
        "sol": "Nomadic herding involves herders moving with animals for pastures and water along defined migration routes.",
        "sol_hi": "चलवासी पशुचारण में पशुचारक अपने पशुओं के साथ चारे और पानी के लिए निश्चित मौसमी मार्गों पर प्रवास करते हैं।"
    },
    {
        "q": "Which of the following countries is famous for coffee plantations called 'Fazendas'?",
        "q_hi": "निम्नलिखित में से कौन सा देश कॉफी बागानों के लिए प्रसिद्ध है जिन्हें 'फजेंडा' (Fazendas) कहा जाता है?",
        "opts": ["India", "Brazil", "Vietnam", "Malaysia"],
        "opts_hi": ["भारत", "ब्राजील", "वियतनाम", "मलेशिया"],
        "ans": 1,
        "sol": "In Brazil, large coffee plantations are referred to as Fazendas.",
        "sol_hi": "ब्राजील में बड़े पैमाने पर बनाए गए कॉफी बागानों को 'फजेंडा' कहा जाता है।"
    },
    {
        "q": "The primary input that distinguishes Intensive Subsistence farming from Primitive Subsistence is:",
        "q_hi": "गहन जीविका कृषि को आदिम जीविका कृषि से अलग करने वाला मुख्य कारक क्या है?",
        "opts": [
            "Absence of manual labor",
            "High use of organic manure, fertilizers, and irrigation on smaller plots",
            "Migratory lifestyle of farmers",
            "Total reliance on rain without any tools"
        ],
        "opts_hi": [
            "शारीरिक श्रम की अनुपस्थिति",
            "छोटे भूखंडों पर जैविक खाद, उर्वरकों और सिंचाई का उच्च उपयोग",
            "किसानों की प्रवासी जीवन शैली",
            "बिना किसी उपकरण के पूरी तरह से बारिश पर निर्भर रहना"
        ],
        "ans": 1,
        "sol": "Intensive subsistence farming employs high labor and modern input tools like fertilizers and irrigation to maximize crop yield from tiny landholdings.",
        "sol_hi": "गहन जीविका कृषि में छोटे भूखंडों से अधिकतम उपज प्राप्त करने के लिए उच्च श्रम तथा उर्वरक और सिंचाई जैसे इनपुट का उपयोग किया जाता है।"
    },
    {
        "q": "What is the key environmental issue associated with shifting cultivation?",
        "q_hi": "स्थानांतरित कृषि से जुड़ी प्रमुख पर्यावरणीय समस्या क्या है?",
        "opts": ["Excessive water logging", "Deforestation and soil erosion", "Salinization of soil", "Air pollution from chemical sprays"],
        "opts_hi": ["अत्यधिक जलभराव", "वनों की कटाई और मृदा अपरदन", "मिट्टी का लवणीकरण", "रासायनिक छिड़काव से वायु प्रदूषण"],
        "ans": 1,
        "sol": "Since forest patches are cleared and burned continuously, it causes severe forest loss and exposes soil to erosion.",
        "sol_hi": "चूंकि वनों के हिस्सों को लगातार काटा और जलाया जाता है, इसलिए यह गंभीर वन विनाश का कारण बनता है और मिट्टी को अपरदन के प्रति संवेदनशील बनाता है।"
    },
    {
        "q": "Which crop is most commonly associated with intensive subsistence agriculture in Southeast Asia?",
        "q_hi": "दक्षिण-पूर्व एशिया में गहन जीविका कृषि के साथ कौन सी फसल सबसे सामान्यतः जुड़ी हुई है?",
        "opts": ["Wheat", "Wet Paddy (Rice)", "Maize", "Cotton"],
        "opts_hi": ["गेहूं", "धान (चावल)", "मक्का", "कपास"],
        "ans": 1,
        "sol": "Wet paddy (rice) is the dominant crop in intensive subsistence agriculture in densely populated Asian regions.",
        "sol_hi": "घनी आबादी वाले एशियाई क्षेत्रों में गहन जीविका कृषि में धान (चावल) प्रमुख फसल है।"
    },
    {
        "q": "In which system of farming is 'Crop Rotation' critically used to maintain soil health without chemical fertilizers?",
        "q_hi": "रासायनिक उर्वरकों के बिना मिट्टी के स्वास्थ्य को बनाए रखने के लिए किस कृषि प्रणाली में 'फसल चक्र' (Crop Rotation) का महत्वपूर्ण उपयोग किया जाता है?",
        "opts": ["Shifting Cultivation", "Organic Farming", "Mono-cropping", "Nomadic Herding"],
        "opts_hi": ["स्थानांतरित कृषि", "जैविक खेती (Organic Farming)", "एकल कृषि", "चलवासी पशुचारण"],
        "ans": 1,
        "sol": "Organic farming heavily relies on crop rotation, green manures, and biological pest control to sustain soil health.",
        "sol_hi": "जैविक खेती मिट्टी के स्वास्थ्य को बनाए रखने के लिए फसल चक्र, हरी खाद और जैविक कीट नियंत्रण पर अत्यधिक निर्भर करती है।"
    },
    {
        "q": "The agricultural system where trees/shrubs are grown around or among crops is called:",
        "q_hi": "वह कृषि प्रणाली जिसमें फसलों के बीच या उसके चारों ओर पेड़/झाड़ियाँ उगाई जाती हैं, कहलाती है:",
        "opts": ["Agro-forestry", "Plantation", "Mixed Farming", "Extensive Agriculture"],
        "opts_hi": ["कृषि-वानिकी (Agro-forestry)", "रोपण कृषि", "मिश्रित खेती", "विस्तृत कृषि"],
        "ans": 0,
        "sol": "Agro-forestry is a land management system where trees are grown around or among crops to improve ecological benefits.",
        "sol_hi": "कृषि-वानिकी एक भूमि प्रबंधन प्रणाली है जहां पारिस्थितिक लाभों को बढ़ाने के लिए फसलों के साथ-साथ पेड़ों को उगाया जाता है।"
    },
    {
        "q": "Which type of commercial farming specializes in dairy animals and is highly capital-intensive?",
        "q_hi": "कौन सी व्यावसायिक कृषि डेयरी पशुओं में विशेषज्ञता रखती है और अत्यधिक पूंजी-प्रधान होती है?",
        "opts": ["Nomadic Herding", "Dairy Farming", "Mixed Farming", "Shifting Cultivation"],
        "opts_hi": ["चलवासी पशुचारण", "डेयरी फार्मिंग (Dairy Farming)", "मिश्रित खेती", "स्थानांतरित कृषि"],
        "ans": 1,
        "sol": "Dairy farming is the commercial rearing of milch animals, requiring specialized machinery and cold chain logistics.",
        "sol_hi": "डेयरी फार्मिंग दुधारू पशुओं का व्यावसायिक पालन है, जिसके लिए विशेष मशीनरी और कोल्ड चेन लॉजिस्टिक्स की आवश्यकता होती है।"
    },
    {
        "q": "In Jharkhand, the local form of shifting cultivation is known as:",
        "q_hi": "झारखंड में स्थानांतरित कृषि के स्थानीय रूप को किस नाम से जाना जाता है?",
        "opts": ["Kumari", "Podu", "Kuruwa", "Dahiya"],
        "opts_hi": ["कुमारी", "पोडू", "कुरुवा (Kuruwa)", "दहिया"],
        "ans": 2,
        "sol": "In Jharkhand, shifting cultivation is called 'Kuruwa'.",
        "sol_hi": "झारखंड में स्थानांतरित कृषि को 'कुरुवा' कहा जाता है।"
    },
    {
        "q": "The concept of 'Precision Agriculture' focuses on:",
        "q_hi": "'सटीक कृषि' (Precision Agriculture) का मुख्य ध्यान किस पर होता है?",
        "opts": [
            "Maximizing the total agricultural land area",
            "Using technology to apply precise inputs for optimum crop growth",
            "Returning to 100% manual farming methods",
            "Growing only one type of crop globally"
        ],
        "opts_hi": [
            "कुल कृषि भूमि क्षेत्र को अधिकतम करना",
            "इष्टतम फसल विकास के लिए सटीक इनपुट लागू करने हेतु तकनीक का उपयोग करना",
            "100% पारंपरिक शारीरिक खेती विधियों पर वापस लौटना",
            "वैश्विक स्तर पर केवल एक ही प्रकार की फसल उगाना"
        ],
        "ans": 1,
        "sol": "Precision farming uses technologies like GPS and sensors to ensure crops receive exactly what they need, minimizing wastage.",
        "sol_hi": "सटीक खेती जीपीएस और सेंसर जैसी तकनीकों का उपयोग करती है ताकि फसलों को वही मिले जिसकी उन्हें आवश्यकता है, जिससे संसाधनों की बर्बादी न्यूनतम होती है।"
    },
    {
        "q": "Which of the following is a plantation crop?",
        "q_hi": "निम्नलिखित में से कौन सी एक रोपण फसल (Plantation Crop) है?",
        "opts": ["Wheat", "Rice", "Rubber", "Bajra"],
        "opts_hi": ["गेहूं", "चावल", "रबर (Rubber)", "बाजरा"],
        "ans": 2,
        "sol": "Rubber, tea, coffee, and sugarcane are classic examples of plantation crops.",
        "sol_hi": "रबर, चाय, कॉफी और गन्ना रोपण फसलों के उत्कृष्ट उदाहरण हैं।"
    },
    {
        "q": "The slash and burn agriculture is known as 'Masole' in:",
        "q_hi": "काटो और जलाओ कृषि को 'मसोले' (Masole) कहा जाता है:",
        "opts": ["Mexico", "Central Africa / Congo", "Brazil", "Indonesia"],
        "opts_hi": ["मेक्सिको में", "मध्य अफ्रीका / कांगो में", "ब्राजील में", "इंडोनेशिया में"],
        "ans": 1,
        "sol": "In Central Africa, especially Congo basin, shifting cultivation is known as Masole.",
        "sol_hi": "मध्य अफ्रीका, विशेष रूप से कांगो बेसिन में, स्थानांतरित कृषि को 'मसोले' कहा जाता है।"
    },
    {
        "q": "What is 'Truck Farming'?",
        "q_hi": "'ट्रक फार्मिंग' (Truck Farming) क्या है?",
        "opts": [
            "Farming done on trucks",
            "Specialization in the cultivation of vegetables for urban markets",
            "Rearing of horses for transport",
            "Farming of biofuel crops"
        ],
        "opts_hi": [
            "ट्रकों पर की जाने वाली खेती",
            "शहरी बाजारों के लिए सब्जियों की खेती में विशेषज्ञता",
            "परिवहन के लिए घोड़ों का पालन",
            "जैव ईंधन फसलों की खेती"
        ],
        "ans": 1,
        "sol": "Truck farming is a form of commercial gardening specializing in vegetables, which are transported overnight to urban centers.",
        "sol_hi": "ट्रक फार्मिंग व्यावसायिक बागवानी का एक रूप है जो सब्जियों में विशेषज्ञता रखती है, जिन्हें रात भर में ट्रकों द्वारा शहरी केंद्रों तक पहुँचाया जाता है।"
    },
    {
        "q": "Which of the following is NOT correct about Nomadic Herding?",
        "q_hi": "चलवासी पशुचारण के बारे में निम्नलिखित में से कौन सा कथन सही नहीं है?",
        "opts": [
            "Herders move along defined routes",
            "Herders do not have permanent settlements",
            "It is highly commercialized and mechanized",
            "Animals kept depend on the local geography (e.g. camels, yaks)"
        ],
        "opts_hi": [
            "पशुचारक निश्चित मार्गों पर चलते हैं",
            "पशुचारकों की स्थायी बस्तियां नहीं होती हैं",
            "यह अत्यधिक व्यावसायिक और यंत्रीकृत है",
            "पाले जाने वाले पशु स्थानीय भूगोल पर निर्भर करते हैं (जैसे ऊंट, याक)"
        ],
        "ans": 2,
        "sol": "Nomadic herding is a primitive subsistence activity, not commercial or mechanized.",
        "sol_hi": "चलवासी पशुचारण एक आदिम जीविका गतिविधि है, यह व्यावसायिक या यंत्रीकृत नहीं है।"
    },
    {
        "q": "The concept of 'Sustainable Agriculture' primary aims to:",
        "q_hi": "'सतत कृषि' (Sustainable Agriculture) का प्राथमिक उद्देश्य क्या है?",
        "opts": [
            "Produce maximum output regardless of environment damage",
            "Meet present food needs without compromising environmental quality for future generations",
            "Migrate farming completely to space stations",
            "Rely only on imported seeds"
        ],
        "opts_hi": [
            "पर्यावरण क्षति की परवाह किए बिना अधिकतम उत्पादन प्राप्त करना",
            "भविष्य की पीढ़ियों के लिए पर्यावरण गुणवत्ता से समझौता किए बिना वर्तमान भोजन की आवश्यकताओं को पूरा करना",
            "खेती को पूरी तरह से अंतरिक्ष स्टेशनों पर स्थानांतरित करना",
            "केवल आयातित बीजों पर निर्भर रहना"
        ],
        "ans": 1,
        "sol": "Sustainable agriculture integrates ecological health, economic profitability, and social equity.",
        "sol_hi": "सतत कृषि पारिस्थितिक स्वास्थ्य, आर्थिक लाभप्रदता और सामाजिक समानता का समन्वय करती है।"
    },
    {
        "q": "In mixed farming, which of the following is grown along with food crops to feed livestock?",
        "q_hi": "मिश्रित खेती में, पशुओं को खिलाने के लिए खाद्य फसलों के साथ निम्नलिखित में से क्या उगाया जाता है?",
        "opts": ["Fodder Crops", "Cotton", "Tobacco", "Coffee"],
        "opts_hi": ["चारा फसलें (Fodder Crops)", "कपास", "तंबाकू", "कॉफी"],
        "ans": 0,
        "sol": "Fodder crops are an essential component of mixed farming to feed cattle, sheep, and other livestock.",
        "sol_hi": "पशुओं को खिलाने के लिए मिश्रित खेती में चारा फसलें एक आवश्यक घटक होती हैं।"
    },
    {
        "q": "The local name of shifting cultivation in Vietnam is:",
        "q_hi": "वियतनाम में स्थानांतरित कृषि का स्थानीय नाम क्या है?",
        "opts": ["Ray", "Milpa", "Masole", "Ladang"],
        "opts_hi": ["रे (Ray)", "मिल्पा", "मसोले", "लदांग"],
        "ans": 0,
        "sol": "In Vietnam, shifting cultivation is locally known as 'Ray'.",
        "sol_hi": "वियतनाम में स्थानांतरित कृषि को स्थानीय रूप से 'रे' (Ray) कहा जाता है।"
    },
    {
        "q": "Which type of farming requires huge tracts of land and uses low labor input per acre?",
        "q_hi": "किस प्रकार की खेती के लिए विशाल भूमि की आवश्यकता होती है और प्रति एकड़ कम श्रम का उपयोग होता है?",
        "opts": ["Intensive Subsistence Farming", "Extensive Commercial Grain Cultivation", "Terrace Farming", "Mixed Farming"],
        "opts_hi": ["गहन जीविका कृषि", "विस्तृत वाणिज्यिक अनाज कृषि", "सोपान कृषि", "मिश्रित खेती"],
        "ans": 1,
        "sol": "Extensive commercial grain farming uses massive farms with highly mechanized processes and low labor inputs per unit area.",
        "sol_hi": "विस्तृत वाणिज्यिक अनाज कृषि में अत्यधिक यंत्रीकृत प्रक्रियाओं के साथ विशाल खेतों का उपयोग किया जाता है, जिससे प्रति इकाई क्षेत्र में कम श्रम लगता है।"
    },
    {
        "q": "What is 'Collective Farming'?",
        "q_hi": "'सामूहिक कृषि' (Collective Farming) क्या है?",
        "opts": [
            "Farming done by a single family",
            "Joint agricultural production where assets are owned by the collective community/state",
            "Farming only on state boundaries",
            "Cultivation of crops by corporate companies only"
        ],
        "opts_hi": [
            "एक ही परिवार द्वारा की जाने वाली खेती",
            "संयुक्त कृषि उत्पादन जहां संपत्तियां सामूहिक समुदाय/राज्य के स्वामित्व में होती हैं",
            "केवल राज्य की सीमाओं पर की जाने वाली खेती",
            "केवल कॉर्पोरेट कंपनियों द्वारा फसलों की खेती"
        ],
        "ans": 1,
        "sol": "Collective farming involves joint farming operations where land and capital are owned collectively by members or the state (e.g. Kolkhoz in USSR).",
        "sol_hi": "सामूहिक कृषि में संयुक्त कृषि संचालन शामिल होता है जहाँ भूमि और पूंजी सामूहिक रूप से सदस्यों या राज्य के स्वामित्व में होती है (जैसे सोवियत संघ में कोलखोज़)।"
    },
    {
        "q": "The farming system where crops are grown in vertical stacked layers, often integrated with building designs, is:",
        "q_hi": "वह कृषि प्रणाली जिसमें फसलों को ऊर्ध्वाधर परतों में उगाया जाता है, जो अक्सर इमारतों के डिजाइनों के साथ एकीकृत होती है, कहलाती है:",
        "opts": ["Terrace Farming", "Vertical Farming", "Mixed Farming", "Extensive Farming"],
        "opts_hi": ["सोपान कृषि", "ऊर्ध्वाधर खेती (Vertical Farming)", "मिश्रित खेती", "विस्तृत कृषि"],
        "ans": 1,
        "sol": "Vertical farming grows plants vertically in layers indoors, maximizing space utilization.",
        "sol_hi": "ऊर्ध्वाधर खेती में पौधों को बंद कमरों में लंबवत परतों में उगाया जाता है, जिससे स्थान का अधिकतम उपयोग होता है।"
    },
    {
        "q": "The nomadic herding tribe 'Gujjars' are primarily found in:",
        "q_hi": "चलवासी पशुचारक जनजाति 'गुज्जर' मुख्य रूप से कहाँ पाई जाती है?",
        "opts": ["Deccan Plateau", "Western Himalayas", "Thar Desert", "Western Ghats"],
        "opts_hi": ["दक्कन का पठार", "पश्चिमी हिमालय (Western Himalayas)", "थार मरुस्थल", "पश्चिमी घाट"],
        "ans": 1,
        "sol": "Gujjars and Bakarwals are nomadic pastoralists residing in the Himalayan regions of Jammu & Kashmir and Himachal Pradesh.",
        "sol_hi": "गुज्जर और बकरवाल जम्मू-कश्मीर और हिमाचल प्रदेश के पर्वतीय क्षेत्रों में रहने वाले चलवासी पशुचारक हैं।"
    },
    {
        "q": "Which type of agriculture uses slash and burn techniques?",
        "q_hi": "किस प्रकार की कृषि में 'काटो और जलाओ' तकनीकों का उपयोग किया जाता है?",
        "opts": ["Intensive Subsistence Agriculture", "Shifting Cultivation", "Commercial Grain Cultivation", "Plantation Agriculture"],
        "opts_hi": ["गहन जीविका कृषि", "स्थानांतरित कृषि (Shifting Cultivation)", "वाणिज्यिक अनाज कृषि", "रोपण कृषि"],
        "ans": 1,
        "sol": "Shifting cultivation is characterized by clearing forest patches via cutting and burning trees, cultivating for a few years, and moving to a new plot.",
        "sol_hi": "स्थानांतरित कृषि की विशेषता जंगलों को काटकर और जलाकर साफ करना, कुछ वर्षों तक खेती करना और फिर नए भूखंड पर चले जाना है।"
    },
    {
        "q": "In mixed farming, crop rotation is crucial to:",
        "q_hi": "मिश्रित खेती में, फसल चक्र (Crop Rotation) किसके लिए आवश्यक है?",
        "opts": ["Maintain and replenish soil fertility naturally", "Grow only one crop throughout the decade", "Save cost of purchasing seeds", "Reduce the working hours of livestock"],
        "opts_hi": ["प्राकृतिक रूप से मिट्टी की उर्वरता बनाए रखने और उसे बढ़ाने के लिए", "पूरे दशक में केवल एक ही फसल उगाने के लिए", "बीज खरीदने की लागत बचाने के लिए", "पशुओं के काम के घंटों को कम करने के लिए"],
        "ans": 0,
        "sol": "Crop rotation helps maintain soil nutrients by alternating nitrogen-fixing crops (like pulses) with cereal crops.",
        "sol_hi": "फसल चक्र नाइट्रोजन-स्थिरीकरण करने वाली फसलों (जैसे दालों) को अनाज फसलों के साथ बदलकर मिट्टी के पोषक तत्वों को बनाए रखने में मदद करता है।"
    },
    {
        "q": "The commercial growing of flowers is called:",
        "q_hi": "फूलों की व्यावसायिक खेती को क्या कहा जाता है?",
        "opts": ["Floriculture", "Horticulture", "Apiculture", "Sericulture"],
        "opts_hi": ["फ्लोरीकल्चर (Floriculture)", "हॉर्टिकल्चर", "एपीकल्चर", "सेरीकल्चर"],
        "ans": 0,
        "sol": "Floriculture is the cultivation of flowering and ornamental plants for cosmetic, decorative, and industrial purposes.",
        "sol_hi": "फ्लोरीकल्चर सौंदर्य प्रसाधन, सजावट और औद्योगिक उद्देश्यों के लिए फूलों और सजावटी पौधों की खेती है।"
    },
    {
        "q": "Which agricultural term describes a farming system in which plants are grown in an air or mist environment without soil or water?",
        "q_hi": "कौन सा कृषि शब्द उस खेती प्रणाली का वर्णन करता है जिसमें पौधों को बिना मिट्टी या पानी के, हवा या धुंध के वातावरण में उगाया जाता है?",
        "opts": ["Hydroponics", "Aeroponics", "Aquaponics", "Dryland Farming"],
        "opts_hi": ["हाइड्रोपोनिक्स", "एयरोपोनिक्स (Aeroponics)", "एक्वापोनिक्स", "शुष्क भूमि कृषि"],
        "ans": 1,
        "sol": "Aeroponics is the process of growing plants suspended in an air or mist environment, supplying nutrients directly to the exposed roots.",
        "sol_hi": "एयरोपोनिक्स पौधों को हवा या धुंध के वातावरण में लटकाकर उगाने की प्रक्रिया है, जिसमें उजागर जड़ों को सीधे पोषक तत्व प्रदान किए जाते हैं।"
    },
    {
        "q": "What is the primary constraint of intensive subsistence farming?",
        "q_hi": "गहन जीविका कृषि की प्राथमिक बाधा क्या है?",
        "opts": ["Lack of human labor", "Huge surplus crops with no buyers", "Small and fragmented landholdings due to high population density", "Excessive mechanization"],
        "opts_hi": ["मानव श्रम की कमी", "बिना किसी खरीदार के भारी मात्रा में अधिशेष फसलें होना", "उच्च जनसंख्या घनत्व के कारण छोटे और खंडित भूखंड", "अत्यधिक यंत्रीकरण"],
        "ans": 2,
        "sol": "High population density in monsoon Asia leads to tiny, fragmented farms, limiting mechanization and requiring intensive manual labor.",
        "sol_hi": "मानसून एशिया में उच्च जनसंख्या घनत्व के कारण खेत बहुत छोटे और खंडित होते हैं, जिससे यंत्रीकरण सीमित हो जाता है और गहन शारीरिक श्रम की आवश्यकता होती।"
    },
    {
        "q": "Plantations require a well-developed network of transport because:",
        "q_hi": "रोपण बागानों को परिवहन के एक अच्छी तरह से विकसित नेटवर्क की आवश्यकता होती है क्योंकि:",
        "opts": [
            "Workers need to travel to cities daily",
            "Crops need to be processed quickly and sent to markets/factories",
            "Animals need to be transported for grazing",
            "Fertilizers are only made in foreign countries"
        ],
        "opts_hi": [
            "श्रमिकों को प्रतिदिन शहरों की यात्रा करने की आवश्यकता होती है",
            "फसलों को जल्दी से संसाधित करने और बाजारों/कारखानों में भेजने की आवश्यकता होती है",
            "चराई के लिए जानवरों का परिवहन आवश्यक है",
            "उर्वरक केवल विदेशों में बनाए जाते हैं"
        ],
        "ans": 1,
        "sol": "Since plantation crops are highly commercial and perishable or require industrial processing (like tea leaves), a quick transport link is essential.",
        "sol_hi": "चूंकि रोपण फसलें अत्यधिक व्यावसायिक होती हैं और जल्दी खराब हो सकती हैं या उनके प्रसंस्करण की आवश्यकता होती है (जैसे चाय की पत्तियां), इसलिए त्वरित परिवहन लिंक आवश्यक है।"
    },
    {
        "q": "Nomadic herders in Rajasthan are commonly known as:",
        "q_hi": "राजस्थान में चलवासी पशुचारकों को सामान्यतः किस नाम से जाना जाता है?",
        "opts": ["Gujjars", "Bakarwals", "Raikas", "Bhotiyas"],
        "opts_hi": ["गुज्जर", "बकरवाल", "रैका (Raikas)", "भोटिया"],
        "ans": 2,
        "sol": "Raikas are nomadic pastoralists of Rajasthan, herding camels, sheep, and goats.",
        "sol_hi": "रैका राजस्थान के चलवासी पशुचारक हैं जो मुख्य रूप से ऊंट, भेड़ और बकरियां पालते हैं।"
    },
    {
        "q": "The integration of fish farming with hydroponic crop production is known as:",
        "q_hi": "मछली पालन को हाइड्रोपोनिक फसल उत्पादन के साथ एकीकृत करने को क्या कहा जाता है?",
        "opts": ["Aquaponics", "Aeroponics", "Pisciculture", "Mixed Farming"],
        "opts_hi": ["एक्वापोनिक्स (Aquaponics)", "एयरोपोनिक्स", "मत्स्य पालन (Pisciculture)", "मिश्रित खेती"],
        "ans": 0,
        "sol": "Aquaponics combines aquaculture (raising aquatic animals) with hydroponics (cultivating plants in water) in a symbiotic environment.",
        "sol_hi": "एक्वापोनिक्स एक सहजीवी वातावरण में जलीय कृषि (मछली पालन) को हाइड्रोपोनिक्स (पानी में पौधे उगाना) के साथ एकीकृत करता है।"
    },
    {
        "q": "Which type of agriculture is also referred to as 'Slash and Burn' farming?",
        "q_hi": "किस प्रकार की कृषि को 'काटो और जलाओ' (Slash and Burn) खेती भी कहा जाता है?",
        "opts": ["Mixed Farming", "Shifting Cultivation", "Commercial Grain Agriculture", "Dryland Agriculture"],
        "opts_hi": ["मिश्रित खेती", "स्थानांतरित कृषि", "वाणिज्यिक अनाज कृषि", "शुष्क भूमि कृषि"],
        "ans": 1,
        "sol": "Shifting cultivation is called slash-and-burn farming because land is cleared by cutting vegetation and burning the debris.",
        "sol_hi": "स्थानांतरित कृषि को काटो और जलाओ खेती इसलिए कहा जाता है क्योंकि वनस्पतियों को काटकर और मलबे को जलाकर भूमि को साफ किया जाता है।"
    },
    {
        "q": "Which continent has the most extensive belts of Commercial Grain Cultivation?",
        "q_hi": "किस महाद्वीप में विस्तृत वाणिज्यिक अनाज कृषि की सबसे व्यापक पट्टियाँ हैं?",
        "opts": ["Africa", "North America", "South America", "Asia"],
        "opts_hi": ["अफ्रीका", "उत्तरी अमेरिका", "दक्षिणी अमेरिका", "एशिया"],
        "ans": 1,
        "sol": "North America contains vast Prairie belts dedicated to extensive wheat and maize cultivation.",
        "sol_hi": "उत्तरी अमेरिका में गेहूं और मक्के की विस्तृत खेती के लिए समर्पित विशाल प्रेयरी पट्टियाँ स्थित हैं।"
    },
    {
        "q": "What is 'Ley Farming'?",
        "q_hi": "'ले फार्मिंग' (Ley Farming) क्या है?",
        "opts": [
            "Growing grass in rotation with grain crops to restore soil health",
            "Farming only on hilly slopes",
            "Rearing poultry on a large scale",
            "Cultivation of fruit crops exclusively"
        ],
        "opts_hi": [
            "मिट्टी के स्वास्थ्य को बहाल करने के लिए अनाज फसलों के साथ चक्र में घास उगाना",
            "केवल पहाड़ी ढलानों पर खेती करना",
            "बड़े पैमाने पर मुर्गी पालन करना",
            "विशेष रूप से फल फसलों की खेती करना"
        ],
        "ans": 0,
        "sol": "Ley farming is the agricultural practice of rotating crop production with pasture/grass to allow the soil to regain organic matter.",
        "sol_hi": "ले फार्मिंग मिट्टी में कार्बनिक पदार्थों को पुनः प्राप्त करने के लिए फसल उत्पादन को चरागाह/घास के साथ चक्रित करने की कृषि पद्धति है।"
    },
    {
        "q": "In which farming system is the yield per unit area high, but yield per worker relatively low?",
        "q_hi": "किस कृषि प्रणाली में प्रति इकाई क्षेत्र में उपज अधिक होती है, लेकिन प्रति श्रमिक उत्पादकता अपेक्षाकृत कम होती है?",
        "opts": ["Extensive Commercial Agriculture", "Intensive Subsistence Agriculture", "Plantation Agriculture", "Nomadic Rearing"],
        "opts_hi": ["विस्तृत वाणिज्यिक कृषि", "गहन जीविका कृषि (Intensive Subsistence)", "रोपण कृषि", "चलवासी पशुपालन"],
        "ans": 1,
        "sol": "Intensive subsistence has high per-hectare yield due to heavy manual inputs, but low per-worker output because of massive labor pressure.",
        "sol_hi": "गहन जीविका कृषि में अत्यधिक मानव श्रम के उपयोग के कारण प्रति हेक्टेयर उपज अधिक होती है, लेकिन अत्यधिक जन दबाव के कारण प्रति श्रमिक उत्पादकता कम होती है।"
    },
    {
        "q": "Which type of farming is highly prevalent in the state of Sikkim, making it India's first fully certified state of this kind?",
        "q_hi": "सिक्किम राज्य में किस प्रकार की खेती अत्यधिक प्रचलित है, जिसने इसे भारत का पहला पूर्णतः प्रमाणित राज्य बनाया है?",
        "opts": ["Hydroponic Farming", "Organic Farming", "Precision Farming", "Dryland Farming"],
        "opts_hi": ["हाइड्रोपोनिक खेती", "जैविक खेती (Organic Farming)", "सटीक खेती", "शुष्क भूमि कृषि"],
        "ans": 1,
        "sol": "Sikkim became India's first 100% organic state, utilizing biological processes and banishing synthetic chemicals.",
        "sol_hi": "सिक्किम कृत्रिम रसायनों को प्रतिबंधित करके और जैविक प्रक्रियाओं का उपयोग करके भारत का पहला 100% जैविक राज्य बना है।"
    },
    {
        "q": "The commercial rearing of silkworms for production of silk is known as:",
        "q_hi": "रेशम के उत्पादन के लिए रेशम के कीड़ों का व्यावसायिक पालन क्या कहलाता है?",
        "opts": ["Apiculture", "Pisciculture", "Sericulture", "Horticulture"],
        "opts_hi": ["एपीकल्चर", "मत्स्य पालन", "सेरीकल्चर (Sericulture)", "हॉर्टिकल्चर"],
        "ans": 2,
        "sol": "Sericulture is the commercial production of raw silk by rearing silkworms.",
        "sol_hi": "रेशम के कीड़ों को पालकर कच्चे रेशम का व्यावसायिक उत्पादन करना सेरीकल्चर कहलाता है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which agricultural system is characterized by the migration of herders across highlands and lowlands in search of pasture during different seasons?",
        "q_hi": "विभिन्न मौसमों के दौरान चरागाह की तलाश में पर्वतीय और मैदानी क्षेत्रों के बीच पशुचारकों के प्रवास की विशेषता वाली कृषि प्रणाली कौन सी है?",
        "opts": ["Shifting Cultivation", "Transhumance", "Extensive Grain Farming", "Mixed Farming"],
        "opts_hi": ["स्थानांतरित कृषि", "ऋतुप्रवास (Transhumance)", "विस्तृत अनाज कृषि", "मिश्रित खेती"],
        "ans": 1,
        "sol": "Transhumance is the seasonal movement of pastoral herders and their livestock between summer and winter pastures.",
        "sol_hi": "ऋतुप्रवास (Transhumance) गर्मियों और सर्दियों के चरागाहों के बीच पशुचारकों और उनके पशुधन का मौसमी प्रवास है।"
    },
    {
        "q": "The local name of slash and burn farming in Central Africa (specifically Congo basin) is:",
        "q_hi": "मध्य अफ्रीका (विशेष रूप से कांगो बेसिन) में काटो और जलाओ कृषि का स्थानीय नाम क्या है?",
        "opts": ["Milpa", "Masole", "Roca", "Ladang"],
        "opts_hi": ["मिल्पा", "मसोले (Masole)", "रोका", "लदांग"],
        "ans": 1,
        "sol": "Masole is the local term for shifting cultivation in the Congo basin of Central Africa.",
        "sol_hi": "मध्य अफ्रीका के कांगो बेसिन में स्थानांतरित कृषि का स्थानीय नाम मसोले है।"
    },
    {
        "q": "Which of the following is the primary ecological hazard of continuous wet paddy intensive subsistence farming without rotation?",
        "q_hi": "बिना फसल चक्र के लगातार धान की गहन जीविका कृषि करने का प्राथमिक पारिस्थितिक खतरा निम्नलिखित में से कौन सा है?",
        "opts": ["Soil erosion by wind", "Methane emission and water logging", "Salinization due to dry weather", "Deforestation"],
        "opts_hi": ["हवा द्वारा मृदा अपरदन", "मीथेन उत्सर्जन और जलभराव", "शुष्क मौसम के कारण लवणीकरण", "वनों की कटाई"],
        "ans": 1,
        "sol": "Wet paddy cultivation creates anaerobic conditions, leading to significant methane gas release (a potent greenhouse gas) and waterlogging.",
        "sol_hi": "धान की खेती मिट्टी में अवायवीय परिस्थितियां उत्पन्न करती है, जिससे मीथेन गैस (एक शक्तिशाली ग्रीनहाउस गैस) का उत्सर्जन और जलभराव होता है।"
    },
    {
        "q": "The combination of crop production with livestock farming is called mixed farming. In which region is it most highly developed?",
        "q_hi": "पशुपालन के साथ फसल उत्पादन के संयोजन को मिश्रित खेती कहा जाता है। यह किस क्षेत्र में सबसे अधिक विकसित है?",
        "opts": ["South-East Asia", "Western Europe", "Northern Africa", "Western Australia"],
        "opts_hi": ["दक्षिण-पूर्व एशिया", "पश्चिमी यूरोप (Western Europe)", "उत्तरी अफ्रीका", "पश्चिमी ऑस्ट्रेलिया"],
        "ans": 1,
        "sol": "Mixed farming is highly developed and practiced in Western Europe, parts of North America, and temperate parts of Southern continents.",
        "sol_hi": "मिश्रित खेती मुख्य रूप से पश्चिमी यूरोप, उत्तरी अमेरिका के कुछ हिस्सों और दक्षिणी महाद्वीपों के समशीतोष्ण भागों में अत्यधिक विकसित और प्रचलित है।"
    },
    {
        "q": "The cultivation of crops on permanent fields where the fields are kept fallow for a year or two to recover nutrients is:",
        "q_hi": "स्थायी खेतों पर फसलों की खेती जहां पोषक तत्वों को पुनः प्राप्त करने के लिए खेतों को एक या दो वर्ष के लिए परती (fallow) छोड़ दिया जाता है, कहलाती है:",
        "opts": ["Fallow-rotation Farming", "Shifting Agriculture", "Precision Agriculture", "Mono-cropping"],
        "opts_hi": ["परती-चक्रण खेती", "स्थानांतरित कृषि", "सटीक कृषि", "एकल फसल खेती"],
        "ans": 0,
        "sol": "In fallow rotation systems, fields are left uncultivated (fallow) periodically to recover soil nutrients naturally.",
        "sol_hi": "परती चक्रण प्रणालियों में, मिट्टी के पोषक तत्वों को प्राकृतिक रूप से पुनः प्राप्त करने के लिए खेतों को समय-समय पर बिना बोए (परती) छोड़ दिया जाता है।"
    },
    {
        "q": "Who introduced tea plantations in India during the colonial period?",
        "q_hi": "औपनिवेशिक काल के दौरान भारत में चाय बागानों (Plantations) की शुरुआत किसने की थी?",
        "opts": ["The French", "The Portuguese", "The British", "The Dutch"],
        "opts_hi": ["फ्रांसीसी", "पुर्तगाली", "ब्रिटिश (The British)", "डच"],
        "ans": 2,
        "sol": "The British introduced commercial tea plantations in regions like Assam and Darjeeling in the 19th century.",
        "sol_hi": "ब्रिटिश शासन ने 19वीं शताब्दी में असम और दार्जिलिंग जैसे क्षेत्रों में व्यावसायिक चाय बागानों की शुरुआत की थी।"
    },
    {
        "q": "What is the local term for shifting cultivation in Venezuela?",
        "q_hi": "वेनेजुएला में स्थानांतरित कृषि के लिए स्थानीय शब्द क्या है?",
        "opts": ["Conuco", "Roca", "Ray", "Masole"],
        "opts_hi": ["कोनुको (Conuco)", "रोका", "रे", "मसोले"],
        "ans": 0,
        "sol": "In Venezuela, shifting agriculture is locally known as Conuco.",
        "sol_hi": "वेनेजुएला में स्थानांतरित कृषि को स्थानीय रूप से 'कोनुको' कहा जाता है।"
    },
    {
        "q": "Which type of agriculture uses minimal inputs, relies on rainfall, and is practiced in areas with annual rainfall between 75 cm and 110 cm?",
        "q_hi": "कौन सी कृषि प्रणाली न्यूनतम इनपुट का उपयोग करती है, वर्षा पर निर्भर करती है, और 75 सेमी से 110 सेमी वार्षिक वर्षा वाले क्षेत्रों में की जाती है?",
        "opts": ["Dryland Farming", "Wetland Farming", "Rainfed Farming", "Precision Farming"],
        "opts_hi": ["शुष्क भूमि कृषि", "आर्द्रभूमि कृषि", "वर्षा-आधारित खेती (Rainfed Farming)", "सटीक खेती"],
        "ans": 2,
        "sol": "Rainfed farming (dryland farming is < 75 cm) operates in sub-humid zones with rainfall between 75-110 cm, focusing on soil conservation.",
        "sol_hi": "वर्षा-आधारित खेती 75-110 सेमी वर्षा वाले उप-आर्द्र क्षेत्रों में की जाती है (जबकि शुष्क खेती 75 सेमी से कम वर्षा में होती है)।"
    },
    {
        "q": "Which of the following is FALSE about plantation agriculture?",
        "q_hi": "रोपण कृषि के बारे में निम्नलिखित में से कौन सा कथन असत्य है?",
        "opts": [
            "It is highly capital-intensive",
            "It focuses on a single cash crop",
            "It is developed primarily for local subsistence consumption",
            "It uses scientific methods and skilled management"
        ],
        "opts_hi": [
            "यह अत्यधिक पूंजी-प्रधान है",
            "यह एक ही नकदी फसल पर ध्यान केंद्रित करती है",
            "यह मुख्य रूप से स्थानीय जीविका उपभोग के लिए विकसित की जाती है",
            "यह वैज्ञानिक तरीकों और कुशल प्रबंधन का उपयोग करती है"
        ],
        "ans": 2,
        "sol": "Plantations are commercial and export-oriented, not meant for local subsistence consumption.",
        "sol_hi": "रोपण कृषि व्यावसायिक और निर्यात-उन्मुख होती है, यह स्थानीय जीविका उपभोग के लिए नहीं बनाई जाती है।"
    },
    {
        "q": "The type of farming where crops are grown in water enriched with nutrients, and integrated with terrestrial animal rearing is: ",
        "q_hi": "वह कृषि प्रणाली जिसमें पोषक तत्वों से भरपूर पानी में फसलें उगाई जाती हैं, और स्थलीय पशु पालन के साथ एकीकृत की जाती हैं, कहलाती है: ",
        "opts": ["Aquaponics", "Integrated Farming System", "Mixed Farming", "Dairy Farming"],
        "opts_hi": ["एक्वापोनिक्स", "एकीकृत कृषि प्रणाली (Integrated Farming System)", "मिश्रित खेती", "डेयरी फार्मिंग"],
        "ans": 1,
        "sol": "Integrated Farming System (IFS) combines crops, horticulture, and livestock to optimize energy flows and income.",
        "sol_hi": "एकीकृत कृषि प्रणाली (IFS) ऊर्जा प्रवाह और आय को अनुकूलित करने के लिए फसलों, बागवानी और पशुपालन को एकीकृत करती है।"
    },
    {
        "q": "In which type of agricultural system is the labor productivity per person highest?",
        "q_hi": "किस प्रकार की कृषि प्रणाली में प्रति व्यक्ति श्रम उत्पादकता (labor productivity) सबसे अधिक होती है?",
        "opts": ["Intensive Subsistence Farming", "Extensive Commercial Grain Farming", "Terrace Cultivation", "Nomadic Herding"],
        "opts_hi": ["गहन जीविका कृषि", "विस्तृत वाणिज्यिक अनाज कृषि (Extensive Commercial)", "सोपान कृषि", "चलवासी पशुचारण"],
        "ans": 1,
        "sol": "Because of massive farm sizes and near-total mechanization, extensive grain farming yields very high output per worker.",
        "sol_hi": "विशाल खेतों के आकार और लगभग पूर्ण यंत्रीकरण के कारण, विस्तृत अनाज कृषि में प्रति श्रमिक उत्पादकता बहुत अधिक होती है।"
    },
    {
        "q": "Which state of India is known as the 'Organic State of India'?",
        "q_hi": "भारत के किस राज्य को 'भारत का जैविक राज्य' कहा जाता है?",
        "opts": ["Kerala", "Sikkim", "Uttarakhand", "Himachal Pradesh"],
        "opts_hi": ["केरल", "सिक्किम (Sikkim)", "उत्तराखंड", "हिमाचल प्रदेश"],
        "ans": 1,
        "sol": "Sikkim was formally declared India's first 100% organic state in 2016.",
        "sol_hi": "सिक्किम को 2016 में औपचारिक रूप से भारत का पहला 100% जैविक राज्य घोषित किया गया था।"
    },
    {
        "q": "What is 'Ley farming'?",
        "q_hi": "'ले फार्मिंग' (Ley farming) क्या है?",
        "opts": [
            "Rotating cereal crops with grass or pasture to restore soil nitrogen",
            "Cultivation of tea on slopes",
            "Farming done in water bodies",
            "Growing vegetables in urban areas"
        ],
        "opts_hi": [
            "मिट्टी के नाइट्रोजन को बहाल करने के लिए अनाज की फसलों के साथ घास या चरागाह को चक्रित करना",
            "ढलानों पर चाय की खेती",
            "जल निकायों में की जाने वाली खेती",
            "शहरी क्षेत्रों में सब्जियां उगाना"
        ],
        "ans": 0,
        "sol": "Ley farming is the cultivation of temporary pastures in rotation with crop production to naturally build soil organic matter.",
        "sol_hi": "ले फार्मिंग अनाज की फसलों के साथ चरागाह/घास को बारी-बारी से उगाकर मिट्टी में कार्बनिक तत्वों को प्राकृतिक रूप से बढ़ाने की पद्धति है।"
    },
    {
        "q": "Shifting cultivation is called 'Podu' in Andhra Pradesh. What is it called in Odisha?",
        "q_hi": "आंध्र प्रदेश में स्थानांतरित खेती को 'पोडू' कहा जाता है। ओडिशा में इसे क्या कहा जाता है?",
        "opts": ["Podu", "Kuruwa", "Dahiya", "Kumari"],
        "opts_hi": ["पोडू (Podu)", "कुरुवा", "दहिया", "कुमारी"],
        "ans": 0,
        "sol": "Shifting cultivation is referred to as Podu in both Andhra Pradesh and Odisha.",
        "sol_hi": "आंध्र प्रदेश और ओडिशा दोनों राज्यों में स्थानांतरित कृषि को 'पोडू' कहा जाता है।"
    },
    {
        "q": "Which type of farming focuses heavily on growing fruits, vegetables, and flowers for high value markets?",
        "q_hi": "कौन सी कृषि प्रणाली मूल्यवान बाजारों के लिए फलों, सब्जियों और फूलों को उगाने पर अत्यधिक ध्यान केंद्रित करती है?",
        "opts": ["Dairy Farming", "Horticulture / Market Gardening", "Mixed Farming", "Shifting Cultivation"],
        "opts_hi": ["डेयरी फार्मिंग", "बागवानी / बाजार बागवानी (Horticulture)", "मिश्रित खेती", "स्थानांतरित कृषि"],
        "ans": 1,
        "sol": "Horticulture and market gardening specialize in high-value fruits, vegetables, and ornamental plants near urban centers.",
        "sol_hi": "बागवानी (Horticulture) और बाजार बागवानी शहरी केंद्रों के पास फल, सब्जियां और सजावटी पौधों को उगाने में विशेषज्ञता रखती है।"
    }
]

def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Review the classification of agriculture systems including subsistence and commercial models.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Subsistence Farming",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is the primary target of intensive subsistence farming?", "opts": ["Exports", "Family self-consumption", "State storage", "Animal feed"], "ans": 1, "sol": "Intensive subsistence focuses on feeding the local farm family."},
                    {"type": "MCQ", "q": "Nomadic herding is a type of which agricultural system?", "opts": ["Commercial Farming", "Primitive Subsistence", "Intensive Subsistence", "Precision Agriculture"], "ans": 1, "sol": "Nomadic herding is a primitive subsistence activity."},
                    {"type": "True/False", "q": "True or False: Shifting cultivation is settled farming.", "ans": False, "sol": "False. Shifting cultivation involves moving fields every few years."},
                    {"type": "One-Liner", "q": "What is the seasonal migration of herders between mountain pastures and valleys called?", "sol": "Transhumance"}
                ]
            },
            {
                "title": "2. Commercial Farming",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which crop is most commonly grown in plantation agriculture?", "opts": ["Wheat", "Millets", "Tea", "Pulses"], "ans": 2, "sol": "Tea, coffee, and rubber are typical plantation crops."},
                    {"type": "MCQ", "q": "What characterizes Mixed Farming?", "opts": ["Growing two crops together", "Crops + Livestock rearing", "Farming in water", "Chemical-free farming"], "ans": 1, "sol": "Mixed farming combines crop cultivation with animal husbandry on the same farm."},
                    {"type": "True/False", "q": "True or False: Extensive commercial grain farming has high yield per hectare.", "ans": False, "sol": "False. Extensive farming has low yield per hectare but high yield per worker."},
                    {"type": "MCQ", "q": "Large coffee estates in Brazil are known as:", "opts": ["Ray", "Fazendas", "Masole", "Kolkhoz"], "ans": 1, "sol": "Large Brazilian coffee estates are called Fazendas."}
                ]
            },
            {
                "title": "3. Regional & Global Nomenclature",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is shifting cultivation called in Mexico?", "opts": ["Ladang", "Roca", "Milpa", "Masole"], "ans": 2, "sol": "It is called Milpa in Mexico and Central America."},
                    {"type": "MCQ", "q": "Shifting cultivation is known as 'Ray' in which country?", "opts": ["Brazil", "Vietnam", "Malaysia", "Congo"], "ans": 1, "sol": "It is called Ray in Vietnam."},
                    {"type": "True/False", "q": "True or False: In Western Ghats of India, shifting cultivation is called Kumari.", "ans": True, "sol": "True. In Kerala and Western Ghats it is called Kumari."},
                    {"type": "True/False", "q": "True or False: Shifting cultivation is called Podu in Jharkhand.", "ans": False, "sol": "False. It is called Kuruwa in Jharkhand. It is called Podu in Andhra Pradesh/Odisha."}
                ]
            },
            {
                "title": "4. Modern & Sustainable Methods",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which state of India is fully certified organic?", "opts": ["Kerala", "Sikkim", "Punjab", "Haryana"], "ans": 1, "sol": "Sikkim is the first fully organic state of India."},
                    {"type": "MCQ", "q": "Growing crops in stacked layers indoors is known as:", "opts": ["Dryland Farming", "Terrace Farming", "Vertical Farming", "Mixed Farming"], "ans": 2, "sol": "This vertical arrangement is called Vertical Farming."},
                    {"type": "True/False", "q": "True or False: Hydroponics requires rich organic soil.", "ans": False, "sol": "False. Hydroponics is soil-less cultivation in water solution."},
                    {"type": "True/False", "q": "True or False: Precision farming aims to optimize resource use using modern sensors/GPS.", "ans": True, "sol": "True. Precision agriculture uses technology to deliver exact inputs to crops."}
                ]
            }
        ]
    }

def build_theory_hi():
    return {
        "breadcrumbs": breadcrumbs_hi,
        "hero": hero_hi,
        "labels": labels_hi,
        "timeline": timeline_hi,
        "mnemonics": mnemonics_hi,
        "flashcards": flashcards_hi,
        "traps": traps_hi,
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "जीविका और वाणिज्यिक मॉडलों सहित कृषि प्रणालियों के वर्गीकरण की समीक्षा करें।", "sections": deep_dive_hi}
    }

def build_practice_hi():
    practice_obj = {
        "practiceQuestions": [
            {"q": pq["q_hi"], "opts": pq["opts_hi"], "ans": pq["ans"], "sol": pq["sol_hi"]} for pq in practice_questions
        ],
        "mockTestQuestions": [
            {"q": mtq["q_hi"], "opts": mtq["opts_hi"], "ans": mtq["ans"], "sol": mtq["sol_hi"]} for mtq in mock_test_questions
        ]
    }
    return practice_obj

def build_mastery_hi():
    return {
        "sections": [
            {
                "title": "1. जीविका कृषि",
                "masteryZone": [
                    {"type": "MCQ", "q": "गहन जीविका कृषि का प्राथमिक लक्ष्य क्या है?", "opts": ["निर्यात", "परिवार का स्व-उपभोग", "राज्य भंडारण", "पशु चारा"], "ans": 1, "sol": "गहन जीविका कृषि स्थानीय किसान परिवार के भरण-पोषण पर केंद्रित होती है।"},
                    {"type": "MCQ", "q": "चलवासी पशुचारण किस प्रकार की कृषि प्रणाली है?", "opts": ["वाणिज्यिक कृषि", "आदिम जीविका कृषि", "गहन जीविका कृषि", "सटीक कृषि"], "ans": 1, "sol": "चलवासी पशुचारण एक आदिम जीविका गतिविधि है।"},
                    {"type": "True/False", "q": "सही या गलत: स्थानांतरित खेती स्थायी खेती है।", "ans": False, "sol": "गलत। स्थानांतरित खेती में हर कुछ वर्षों में खेत बदल दिए जाते हैं।"},
                    {"type": "One-Liner", "q": "विभिन्न मौसमों के दौरान पर्वतीय चरागाहों और घाटियों के बीच पशुचारकों के मौसमी प्रवास को क्या कहते हैं?", "sol": "ऋतुप्रवास (Transhumance)"}
                ]
            },
            {
                "title": "2. वाणिज्यिक कृषि",
                "masteryZone": [
                    {"type": "MCQ", "q": "रोपण कृषि में कौन सी फसल सबसे सामान्यतः उगाई जाती है?", "opts": ["गेहूं", "बाजरा", "चाय", "दालें"], "ans": 2, "sol": "चाय, कॉफी और रबर विशिष्ट रोपण फसलें हैं।"},
                    {"type": "MCQ", "q": "मिश्रित खेती (Mixed Farming) की क्या विशेषता है?", "opts": ["एक साथ दो फसलें उगाना", "फसलें + पशुपालन", "पानी में खेती करना", "रसायन मुक्त खेती"], "ans": 1, "sol": "मिश्रित खेती एक ही खेत पर फसल उत्पादन और पशुपालन को जोड़ती है।"},
                    {"type": "True/False", "q": "सही या गलत: विस्तृत वाणिज्यिक अनाज कृषि में प्रति हेक्टेयर उपज बहुत अधिक होती है।", "ans": False, "sol": "गलत। विस्तृत खेती में प्रति हेक्टेयर उपज कम होती है लेकिन प्रति श्रमिक उत्पादकता उच्च होती है।"},
                    {"type": "MCQ", "q": "ब्राजील में बड़े कॉफी बागानों को किस नाम से जाना जाता है?", "opts": ["रे", "फजेंडा (Fazendas)", "मसोले", "कोलखोज़"], "ans": 1, "sol": "ब्राजील के बड़े कॉफी बागानों को फजेंडा कहा जाता है।"}
                ]
            },
            {
                "title": "3. क्षेत्रीय और वैश्विक नामकरण",
                "masteryZone": [
                    {"type": "MCQ", "q": "मेक्सिको में स्थानांतरित खेती को क्या कहा जाता है?", "opts": ["लदांग", "रोका", "मिल्पा", "मसोले"], "ans": 2, "sol": "मेक्सिको और मध्य अमेरिका में इसे मिल्पा कहा जाता है।"},
                    {"type": "MCQ", "q": "किस देश में स्थानांतरित कृषि को 'रे' (Ray) कहा जाता है?", "opts": ["ब्राजील", "वियतनाम", "मलेशिया", "कांगो"], "ans": 1, "sol": "वियतनाम में इसे रे कहा जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: भारत के पश्चिमी घाट में स्थानांतरित खेती को कुमारी कहा जाता है।", "ans": True, "sol": "सही। केरल और पश्चिमी घाट क्षेत्र में इसे कुमारी कहा जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: झारखंड में स्थानांतरित खेती को पोडू कहा जाता है।", "ans": False, "sol": "गलत। झारखंड में इसे कुरुवा कहा जाता है। आंध्र प्रदेश/ओडिशा में इसे पोडू कहते हैं।"}
                ]
            },
            {
                "title": "4. आधुनिक और सतत विधियां",
                "masteryZone": [
                    {"type": "MCQ", "q": "भारत का कौन सा राज्य पूरी तरह से जैविक प्रमाणित है?", "opts": ["केरल", "सिक्किम", "पंजाब", "हरियाणा"], "ans": 1, "sol": "सिक्किम भारत का पहला पूर्णतः जैविक राज्य है।"},
                    {"type": "MCQ", "q": "बंद कमरों में परतों में फसलों को लंबवत उगाने की तकनीक कहलाती है:", "opts": ["शुष्क भूमि कृषि", "सोपान कृषि", "ऊर्ध्वाधर खेती (Vertical)", "मिश्रित खेती"], "ans": 2, "sol": "इस व्यवस्था को ऊर्ध्वाधर खेती (Vertical Farming) कहा जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: हाइड्रोपोनिक्स के लिए समृद्ध जैविक मिट्टी की आवश्यकता होती है।", "ans": False, "sol": "गलत। हाइड्रोपोनिक्स पानी के घोल में बिना मिट्टी के की जाने वाली खेती है।"},
                    {"type": "True/False", "q": "सही या गलत: सटीक कृषि का उद्देश्य आधुनिक सेंसर/जीपीएस का उपयोग करके संसाधनों के उपयोग को इष्टतम बनाना है।", "ans": True, "sol": "सही। सटीक कृषि तकनीक का उपयोग करके फसलों को आवश्यक मात्रा में इनपुट प्रदान करती है।"}
                ]
            }
        ]
    }

# ----------------- FILE GENERATION -----------------
def write_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())
