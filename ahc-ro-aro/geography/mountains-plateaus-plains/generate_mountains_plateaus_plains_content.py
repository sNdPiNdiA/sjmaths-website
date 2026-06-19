# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "mountains-plateaus-plains"
TOPIC_DISPLAY = "Mountains, Plateaus and Plains"
TOPIC_DISPLAY_HI = "पर्वत, पठार और मैदान"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\geography\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "Geography",
    "parentUrl": "../",
    "current": "Mountains, Plateaus & Plains"
}

hero_en = {
    "title": "Mountains, Plateaus and Plains",
    "description": "Master the geomorphology of the Earth's primary landforms. Understand the classification of fold, block, and volcanic mountains, the economic significance of mineral-rich plateaus, and depositional plain formations."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Landforms Mock Test",
        "description": "Test your knowledge on global mountain ranges, tectonic block structures, plateau types, and plain classifications. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Geological Orogenies (Mountain Building)",
    "description": "Key phases of mountain building and landform evolution in Earth's history.",
    "cards": [
        {
            "period": "Pre-Cambrian Orogeny",
            "date": "> 570 Mya",
            "details": "Oldest mountain building phase. Formed residual ranges like the Aravallis in India and Laurentian shields."
        },
        {
            "period": "Caledonian Orogeny",
            "date": "400 Mya",
            "details": "Silurian-Devonian periods. Formed the Appalachian Mountains of North America and Scottish Highlands."
        },
        {
            "period": "Hercynian Orogeny",
            "date": "300 Mya",
            "details": "Permocarboniferous period. Formed the Ural Mountains, Pennines (UK), and Tien Shan range in Central Asia."
        },
        {
            "period": "Alpine Orogeny",
            "date": "60 Mya to Present",
            "details": "Tertiary period. Formed the highest young fold mountains: Himalayas, Andes, Rockies, Alps, and Caucasus."
        }
    ]
}

mnemonics_en = {
    "title": "Landform Mnemonics",
    "description": "Memory hooks to quickly identify landform types and global ranges.",
    "items": [
        {
            "title": "Mnemonic 1: Major Young Fold Mountains",
            "phrase": "\"U-R-A-A-H-M (U Are A Huge Mountain)\"",
            "decryption": "Recalls the young fold mountains formed during the Alpine phase:<br>• **U** — Urals (often grouped with Hercynian but has Alpine roots)<br>• **R** — Rockies (North America)<br>• **A** — Andes (South America)<br>• **A** — Alps (Europe)<br>• **H** — Himalayas (Asia)<br>• **M** — Atlas (Africa)"
        },
        {
            "title": "Mnemonic 2: Block Mountains vs Rift Valleys",
            "phrase": "\"H-U-G-D (Horst Up, Graben Down)\"",
            "decryption": "Recalls tectonic block terms:<br>• **Horst** is the **Upthrown** block (forming Block Mountains).<br>• **Graben** is the **Downthrown** block (forming Rift Valleys)."
        },
        {
            "title": "Mnemonic 3: Intermontane Plateaus",
            "phrase": "\"T-A-C-B (Tibet-Anatolia-Colorado-Bolivia)\"",
            "decryption": "Recalls plateaus surrounded by mountain ranges on all sides:<br>• **T** — Tibet (surrounded by Himalayas & Kunlun)<br>• **A** — Anatolia (Turkey; surrounded by Pontic & Taurus)<br>• **C** — Colorado (USA; surrounded by Rockies)<br>• **B** — Bolivian Plateau (surrounded by Andes)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What is the difference between a Horst and a Graben?",
            "answer": "A **Horst** is an uplifted block of crust between two faults (Block Mountain), while a **Graben** is a subsided block between two faults (Rift Valley).",
            "icon": "fa-layer-group"
        },
        {
            "question": "Which plateau is known as the 'Ruhr of India' and why?",
            "answer": "The **Chhota Nagpur Plateau**. It is extremely rich in mineral resources like coal, iron ore, and mica, resembling the Ruhr industrial region of Germany.",
            "icon": "fa-gem"
        },
        {
            "question": "What are Loess plains and how are they formed?",
            "answer": "They are depositional plains formed by the accumulation of windblown silt/dust (usually yellow in color, highly fertile, prominent in Northern China).",
            "icon": "fa-wind"
        },
        {
            "question": "What is the difference between Peneplains and Pediplains?",
            "answer": "**Peneplains** are formed by water erosion (fluvial cycle of Davis) in humid areas, whereas **Pediplains** are formed by wind erosion and scarp retreat (King's cycle) in arid/semi-arid regions.",
            "icon": "fa-water"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Classifying the Ural Mountains as young fold mountains. While they are fold mountains, they are **old fold mountains** formed during the Hercynian orogeny (300 Mya), similar to the Appalachians, and are highly denuded.",
        "<strong>Trap 2:</strong> Believing the Deccan Plateau is an intermontane plateau. The **Deccan Plateau** is a volcanic/lava plateau (Deccan Traps) and a continental plateau, not bounded by fold ranges like Tibet.",
        "<strong>Trap 3:</strong> Confusing Vosges and Black Forest block mountains. The **Black Forest** (Germany) and **Vosges** (France) are horsts separated by the Rhine Rift Valley (graben). Don't mix their locations.",
        "<strong>Trap 4:</strong> Assuming all plains are formed by rivers. Plains can also be structural (crustal uplift), erosional (glaciated/karst peneplains), or wind-deposited (loess plains)."
    ]
}

deep_dive_en = [
    {
        "title": "1. Mountains: Classification & Major Ranges",
        "content": """<p>Mountains are elevated landforms rising abruptly above the surrounding terrain. Based on origin, they are classified into four main types:</p>
        
        <h3>A. Fold Mountains</h3>
        <p>Formed by compressional forces at convergent plate boundaries. Earth's crust folds into synclines (troughs) and anticlines (crests).</p>
        <ul>
          <li><strong>Young Fold Mountains:</strong> Characterized by high, rugged peaks and deep valleys. Examples: Himalayas (Asia), Alps (Europe), Rockies (North America), Andes (South America), Atlas (Africa).</li>
          <li><strong>Old Fold Mountains:</strong> Geologically older, low height, rounded peaks due to millions of years of erosion. Examples: Urals (Russia), Appalachians (USA), Aravallis (India). *The Aravallis are the oldest fold mountains in the world.*</li>
        </ul>

        <h3>B. Block Mountains (Horst & Graben)</h3>
        <p>Formed when the Earth's crust fractures due to tensional or compressional forces, causing blocks to move vertically.</p>
        <ul>
          <li>The uplifted blocks are called **Horsts** (Block Mountains), and the subsided blocks are called **Grabens** (Rift Valleys).</li>
          <li><strong>Examples:</strong> Black Forest (Germany) and Vosges (France) separated by the Rhine Rift Valley; Salt Range (Pakistan); Satpura and Vindhya ranges in India separated by the Narmada Rift Valley; Sierra Nevada (USA - largest block mountain in the world).</li>
        </ul>

        <h3>C. Volcanic Mountains</h3>
        <p>Formed by the accumulation of lava and pyroclastic materials around a volcanic vent.</p>
        <ul>
          <li><strong>Examples:</strong> Mount Fuji (Japan), Mount Kilimanjaro (Tanzania), Mount Cotopaxi (Ecuador), Mount Vesuvius (Italy), Mount Popa (Myanmar), Krakatoa (Indonesia).</li>
        </ul>

        <h3>D. Residual / Relict Mountains</h3>
        <p>Formed by the denudation of existing mountains or plateaus by erosional agents (water, wind) leaving resistant rocks standing.</p>
        <ul>
          <li><strong>Examples:</strong> Aravallis, Nilgiris, Parasnath, Rajmahal, and Western/Eastern Ghats in India; Catskill Mountains in the USA.</li>
        </ul>"""
    },
    {
        "title": "2. Plateaus: Types & Economic Significance",
        "content": """<p>Plateaus are elevated, flat-topped tablelands rising steeply from surrounding areas. They cover about 33% of the land surface. Based on geographical location, they are classified as:</p>
        
        <h3>A. Classification of Plateaus</h3>
        <ul>
          <li><strong>Intermontane Plateaus:</strong> Highest and most extensive, surrounded by fold mountains on all sides. Examples: **Tibetan Plateau** (highest on Earth, ~4500m, bounded by Himalayas and Kunlun), **Anatolia Plateau** (Turkey, Pontic and Taurus ranges), **Bolivian Plateau** (Andes), **Colorado Plateau** (Rockies).</li>
          <li><strong>Piedmont Plateaus:</strong> Bordered by mountains on one side and plains or oceans on the other. Example: **Patagonian Plateau** (Argentina), **Piedmont Plateau** (USA).</li>
          <li><strong>Continental Plateaus:</strong> Rise abruptly from plains or oceans, far from mountain belts. Examples: **Deccan Plateau** (India), **Canadian Shield**, **Katanga Plateau** (Central Africa).</li>
          <li><strong>Volcanic / Lava Plateaus:</strong> Formed by quiet fissure eruptions of highly fluid basaltic lava. Examples: Deccan Traps (India), Columbia-Snake Plateau (USA).</li>
        </ul>

        <h3>B. Major Global Plateaus & Mineral Wealth</h3>
        <p>Plateaus are geological storehouses of minerals, making them highly significant economically:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Plateau Name</th>
                <th>Location</th>
                <th>Major Mineral Resources</th>
                <th>RO/ARO Key Fact</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Chhota Nagpur Plateau</strong></td>
                <td>Eastern India (Jharkhand/West Bengal)</td>
                <td>Coal, Iron Ore, Mica, Bauxite</td>
                <td>Known as the 'Ruhr of India' due to massive industrial concentration.</td>
              </tr>
              <tr>
                <td><strong>Katanga Plateau</strong></td>
                <td>Democratic Republic of Congo</td>
                <td>Copper, Cobalt, Uranium</td>
                <td>Crucial source of global cobalt for rechargeable batteries.</td>
              </tr>
              <tr>
                <td><strong>Kimberley Plateau</strong></td>
                <td>Western Australia</td>
                <td>Diamonds, Gold, Iron Ore</td>
                <td>Hosts the Argyle diamond mine, famous for pink diamonds.</td>
              </tr>
              <tr>
                <td><strong>Laurentian Plateau (Canadian Shield)</strong></td>
                <td>Canada</td>
                <td>Nickel, Copper, Iron, Gold</td>
                <td>One of the oldest geological shields on Earth.</td>
              </tr>
              <tr>
                <td><strong>Potwar Plateau</strong></td>
                <td>Pakistan</td>
                <td>Rock salt, Petroleum, Limestone</td>
                <td>Bounded by the Salt Range block mountains.</td>
              </tr>
              <tr>
                <td><strong>Loess Plateau</strong></td>
                <td>Northern China</td>
                <td>Highly fertile windblown soil</td>
                <td>Formed by deposition of yellow dust from the Gobi desert.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. Plains: Structural, Erosional & Depositional Forms",
        "content": """<p>Plains are relatively low-lying, flat or gently undulating land surfaces. They are divided into three categories based on origin:</p>
        
        <h3>A. Structural Plains</h3>
        <p>Formed by the upliftment of a portion of the seafloor or continental shelf, or by horizontal bedding of rocks.</p>
        <ul>
          <li><strong>Examples:</strong> Great Plains of the USA, Russian Platform, Central Lowlands of Australia.</li>
        </ul>

        <h3>B. Erosional Plains (Peneplains & Pediplains)</h3>
        <p>Formed when agents of erosion wear down elevated landforms over long periods.</p>
        <ul>
          <li><strong>Peneplain:</strong> A nearly flat featureless plain formed in humid regions by river erosion (W.M. Davis model). Residual hills left behind are called **Monadnocks**.</li>
          <li><strong>Pediplain:</strong> Formed in arid or semi-arid regions by wind action and scarp retreat (L.C. King model). Residual hills are called **Inselbergs**.</li>
          <li><strong>Karst Plain:</strong> Formed by limestone dissolution.</li>
        </ul>

        <h3>C. Depositional Plains</h3>
        <p>Formed by the deposition of sediments transported by wind, water, glaciers, or lakes.</p>
        <ul>
          <li><strong>Alluvial / Flood Plains:</strong> Deposited by rivers. Example: Indo-Gangetic Plains.
            <ul>
              <li>*Bhabar:* Porous gravelly belt at foothills where streams disappear.</li>
              <li>*Terai:* Marshy, damp belt next to Bhabar with dense forest.</li>
              <li>*Bhangar:* Older alluvial soil, dry, less fertile, containing calcareous nodules (Kankar).</li>
              <li>*Kadar (Khadar):* Newer, highly fertile alluvial soil replenished annually by floods.</li>
            </ul>
          </li>
          <li><strong>Loess Plains:</strong> Deposited by wind-borne fine silt. Highly fertile. Example: Loess Plain of North China.</li>
          <li><strong>Lacustrine Plains:</strong> Formed when lakes are filled with sediments and dry up. Example: Kashmir Valley, Manipur Basin.</li>
          <li><strong>Glacial Plains:</strong> Formed by outwash deposits of melting glaciers.</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "भूगोल",
    "parentUrl": "../",
    "current": "पर्वत, पठार और मैदान"
}

hero_hi = {
    "title": "पर्वत, पठार और मैदान",
    "description": "पृथ्वी के प्राथमिक उच्चावचों के भू-आकृति विज्ञान को समझें। वलित, ब्लॉक और ज्वालामुखी पर्वतों का वर्गीकरण, खनिज समृद्ध पठारों का आर्थिक महत्व और विभिन्न मैदानी संरचनाओं का विवरण।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव स्थलाकृति मॉक टेस्ट",
        "description": "वैश्विक पर्वत श्रेणियों, ब्लॉक संरचनाओं, पठार प्रकारों और मैदानी वर्गीकरण पर आधारित 15-प्रश्न मॉक टेस्ट।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "भूगर्भीय पर्वत निर्माण काल (Orogenies)",
    "description": "पृथ्वी के इतिहास में पर्वत निर्माण और स्थलाकृतियों के विकास के प्रमुख चरण।",
    "cards": [
        {
            "period": "प्री-कैम्ब्रियन काल",
            "date": "57 करोड़ वर्ष पूर्व",
            "details": "सबसे पुराना पर्वत निर्माण चरण। इससे भारत में अरावली जैसी अवशिष्ट पर्वत श्रृंखलाओं का निर्माण हुआ।"
        },
        {
            "period": "कैलेडोनियन काल",
            "date": "40 करोड़ वर्ष पूर्व",
            "details": "सिलूरियन-डेवोनियन युग। इससे उत्तरी अमेरिका के अप्पलाचियन पर्वत और स्कॉटिश हाइलैंड्स का निर्माण हुआ।"
        },
        {
            "period": "हर्सिनियन काल",
            "date": "30 करोड़ वर्ष पूर्व",
            "details": "परमोकार्बोनिफेरस युग। यूरेशिया में यूराल पर्वत, ब्रिटेन के पेनाइंस और मध्य एशिया के तियान शान का निर्माण हुआ।"
        },
        {
            "period": "अल्पाइन काल",
            "date": "6 करोड़ वर्ष पूर्व से वर्तमान",
            "details": "टर्शियरी युग। इसके तहत दुनिया के सबसे ऊंचे नवीन वलित पर्वत: हिमालय, एंडीज, रॉकीज, आल्प्स और काकेशस बने।"
        }
    ]
}

mnemonics_hi = {
    "title": "स्थलाकृति याद रखने के सूत्र",
    "description": "विभिन्न श्रेणियों, पर्वतों और पठार प्रकारों को आसानी से याद रखने की ट्रिक्स।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: प्रमुख नवीन वलित पर्वत (Young Fold Mountains)",
            "phrase": "\"U-R-A-A-H-M (यू आर ए ह्यूज माउंटेन)\"",
            "decryption": "अल्पाइन युग में निर्मित नवीन वलित पर्वत:<br>• **U** — यूराल (Urals - अल्पाइन और हर्सिनियन मिश्रित)<br>• **R** — रॉकीज (Rockies - उत्तरी अमेरिका)<br>• **A** — एंडीज (Andes - दक्षिणी अमेरिका)<br>• **A** — आल्प्स (Alps - यूरोप)<br>• **H** — हिमालय (Himalayas - एशिया)<br>• **M** — एटलस (Atlas - अफ्रीका)"
        },
        {
            "title": "स्मृति सूत्र 2: ब्लॉक पर्वत और भ्रंश घाटी",
            "phrase": "\"H-U-G-D (Horst Up, Graben Down)\"",
            "decryption": "विवर्तनिकी ब्लॉक के सिद्धांत:<br>• **Horst (हॉर्स्ट)** — ऊपर उठा हुआ खंड (ब्लॉक पर्वत बनाता है)।<br>• **Graben (ग्राबेन)** — नीचे धंसा हुआ खंड (भ्रंश घाटी बनाता है)।"
        },
        {
            "title": "स्मृति सूत्र 3: अंतर-पर्वतीय पठार (Intermontane Plateaus)",
            "phrase": "\"T-A-C-B (तिब्बत-अनातोलिया-कोलोराडो-बोलीविया)\"",
            "decryption": "चारों ओर से पर्वतों से घिरे पठार:<br>• **T** — तिब्बत (हिमालय और कुनलुन के बीच)<br>• **A** — अनातोलिया (तुर्की, पोंटिक और टॉरस के बीच)<br>• **C** — कोलोराडो (यूएसए, रॉकीज के बीच)<br>• **B** — बोलीवियन पठार (एंडीज के बीच)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "हॉर्स्ट (Horst) और ग्राबेन (Graben) में क्या अंतर है?",
            "answer": "भ्रंशन के कारण ऊपर उठे हुए ब्लॉक को **हॉर्स्ट** (ब्लॉक पर्वत) कहते हैं, जबकि नीचे धंसे हुए खंड को **ग्राबेन** (भ्रंश घाटी) कहा जाता है।",
            "icon": "fa-layer-group"
        },
        {
            "question": "भारत के किस पठार को 'भारत का रूर' (Ruhr of India) कहा जाता है?",
            "answer": "**छोटा नागपुर पठार** को। कोयला, लोहा और अभ्रक जैसे खनिजों की प्रचुरता के कारण इसे जर्मनी के रूर औद्योगिक क्षेत्र के सादृश्य माना जाता है।",
            "icon": "fa-gem"
        },
        {
            "question": "लोएस (Loess) मैदान क्या हैं और इनका निर्माण कैसे होता है?",
            "answer": "हवा द्वारा उड़ाकर लाई गई बारीक धूल और मिट्टी के जमाव से बने पीले रंग के अत्यंत उपजाऊ मैदान (जैसे उत्तरी चीन का लोएस मैदान)।",
            "icon": "fa-wind"
        },
        {
            "question": "पेनीप्लेन (Peneplain) और पेडीप्लेन (Pediplain) में क्या अंतर है?",
            "answer": "आर्द्र क्षेत्रों में नदियों के अपरदन से बनी समतल भूमि **पेनीप्लेन** (डेविस) कहलाती है, जबकि शुष्क क्षेत्रों में पवन अपरदन से निर्मित मैदान **पेडीप्लेन** (किंग) कहलाता है।",
            "icon": "fa-water"
        }
    ]
}

traps_hi = {
    "title": "परीक्षा में बचाव योग्य सामान्य भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> यूराल पर्वत को नवीन वलित पर्वत समझना। यूराल पर्वत वलित पर्वत तो है, लेकिन यह **प्राचीन वलित पर्वत** है, जिसका निर्माण हर्सिनियन काल (30 करोड़ वर्ष पूर्व) में हुआ था।",
        "<strong>भ्रम 2:</strong> दक्कन के पठार को अंतर-पर्वतीय पठार समझना। **दक्कन का पठार** एक लावा/ज्वालामुखीय पठार है, यह तिब्बत की तरह चारों ओर से ऊंचे वलित पर्वतों से घिरा अंतर-पर्वतीय पठार नहीं है।",
        "<strong>भ्रम 3:</strong> ब्लैक फॉरेस्ट और वॉस्जेस की अवस्थिति में भ्रमित होना। जर्मनी में स्थित **ब्लैक फॉरेस्ट** और फ्रांस में स्थित **वॉस्जेस (Vosges)** दोनों ब्लॉक पर्वत हैं, जिनके बीच से राइन भ्रंश घाटी गुजरती है।",
        "<strong>भ्रम 4:</strong> सभी मैदानों को केवल नदियों द्वारा निर्मित मानना। मैदान संरचनात्मक (भू-उत्थान), अपरदनात्मक (हिमानी/कार्स्ट मैदान) या पवन-निक्षेपित (लोएस मैदान) भी हो सकते हैं।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. पर्वत: वर्गीकरण और प्रमुख श्रेणियां",
        "content": """<p>पर्वत अपने आस-पास के धरातल से अचानक ऊंचे उठे हुए स्थल रूप होते हैं। उत्पत्ति के आधार पर इन्हें चार मुख्य प्रकारों में वर्गीकृत किया जाता है:</p>
        
        <h3>A. वलित पर्वत (Fold Mountains)</h3>
        <p>विवर्तनिकी प्लेटों के आपस में टकराने से उत्पन्न संपीड़न बलों द्वारा धरातल में पड़ने वाले मोड़ों (वलनों) से बनते हैं।</p>
        <ul>
          <li><strong>नवीन वलित पर्वत:</strong> तीव्र ढाल, नुकीले शिखर और गहरी घाटियाँ इनकी विशेषता हैं। उदाहरण: हिमालय (एशिया), आल्प्स (यूरोप), रॉकीज (उत्तरी अमेरिका), एंडीज (दक्षिणी अमेरिका)।</li>
          <li><strong>प्राचीन वलित पर्वत:</strong> इनका निर्माण करोड़ों वर्ष पूर्व हुआ था और अपरदन के कारण ये अब कम ऊंचाई और गोलाकार शिखरों वाले रह गए हैं। उदाहरण: अरावली (भारत - विश्व की सबसे पुरानी वलित श्रृंखला), यूराल (रूस), अप्पलाचियन (यूएसए)।</li>
        </ul>

        <h3>B. ब्लॉक पर्वत (भ्रंशोत्थ पर्वत - Horst & Graben)</h3>
        <p>धरातल में खिंचाव या संपीड़न के कारण पड़े भ्रंशों (दरारों) से जब बीच का भाग ऊपर उठ जाता है या अगल-बगल के भाग नीचे धंस जाते हैं।</p>
        <ul>
          <li>ऊपर उठे हुए हिस्से को **हॉर्स्ट (Horst)** या ब्लॉक पर्वत कहते हैं, और नीचे धंसे हुए भाग को **ग्राबेन (Graben)** या भ्रंश घाटी कहते हैं।</li>
          <li><strong>उदाहरण:</strong> जर्मनी का ब्लैक फॉरेस्ट और फ्रांस का वॉस्जेस पर्वत (बीच में राइन भ्रंश घाटी); पाकिस्तान की साल्ट रेंज; भारत में नर्मदा घाटी के किनारे स्थित विंध्याचल और सतपुड़ा पर्वत श्रृंखलाएं; यूएसए का सिएरा नेवादा (विश्व का सबसे बड़ा ब्लॉक पर्वत)।</li>
        </ul>

        <h3>C. ज्वालामुखी पर्वत</h3>
        <p>ज्वालामुखी उद्गार के दौरान निकलने वाले लावे, राख और मलबे के ठंडे होकर जमा होने से बनते हैं।</p>
        <ul>
          <li><strong>उदाहरण:</strong> माउंट फुजी (जापान), माउंट किलिमंजारो (तंजानिया), माउंट कोटोपैक्सी (इक्वाडोर), माउंट वेसुवियस (इटली), माउंट पोपा (म्यांमार)।</li>
        </ul>

        <h3>D. अवशिष्ट / Relict पर्वत</h3>
        <p>पुराने पर्वतों या पठारों के बाह्य अपरदनकारी कारकों (नदी, पवन) द्वारा लंबे समय तक अपरदित होने के बाद बचे कठोर चट्टानी भाग हैं।</p>
        <ul>
          <li><strong>उदाहरण:</strong> भारत में अरावली, नीलगिरि, पारसनाथ, राजमहल की पहाड़ियाँ और पश्चिमी व पूर्वी घाट; यूएसए में कैट्सकिल पर्वत।</li>
        </ul>"""
    },
    {
        "title": "2. पठार: प्रकार और आर्थिक महत्व",
        "content": """<p>पठार ऊपर से सपाट और किनारों से तीव्र ढाल वाले विस्तृत मेजनुमा स्थल रूप होते हैं, जो भूपटल के लगभग 33% भाग को कवर करते हैं।</p>
        
        <h3>A. पठारों का वर्गीकरण</h3>
        <ul>
          <li><strong>अंतर-पर्वतीय पठार:</strong> चारों ओर से पर्वतों से घिरे सर्वाधिक ऊंचे पठार। उदाहरण: **तिब्बत का पठार** (विश्व का सबसे बड़ा और ऊंचा पठार, ~4500 मी), **अनातोलिया का पठार** (तुर्की), **बोलीविया का पठार** (एंडीज पर्वतमाला के बीच)।</li>
          <li><strong>गिरिपद पठार (Piedmont):</strong> एक तरफ पर्वत और दूसरी तरफ मैदान या समुद्र से घिरे पठार। उदाहरण: **पैटागोनिया का पठार** (अर्जेंटीना), **पीडमोंट पठार** (यूएसए)।</li>
          <li><strong>महाद्वीपीय पठार:</strong> पर्वतों से दूर स्थित विस्तृत पठार जो मैदानों से अचानक ऊंचे उठते हैं। उदाहरण: **दक्कन का पठार** (भारत), **कनाडाई शील्ड**।</li>
          <li><strong>लावा पठार (Volcanic):</strong> शांत दरारी ज्वालामुखी उद्गार के लावे के जमाव से बनते हैं। उदाहरण: दक्कन ट्रैप (काली मिट्टी का क्षेत्र), कोलंबिया-स्नेक पठार (यूएसए)।</li>
        </ul>

        <h3>B. प्रमुख वैश्विक पठार और खनिज संपदा</h3>
        <p>पठार विभिन्न मूल्यवान खनिजों के भंडार होते हैं, जिस कारण इनका अत्यधिक आर्थिक महत्व है:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>पठार का नाम</th>
                <th>अवस्थिति</th>
                <th>प्रमुख खनिज भंडार</th>
                <th>परीक्षा उपयोगी तथ्य</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>छोटा नागपुर पठार</strong></td>
                <td>पूर्वी भारत (झारखंड/पश्चिम बंगाल)</td>
                <td>कोयला, लौह अयस्क, अभ्रक, बॉक्साइट</td>
                <td>खनिजों की प्रचुरता के कारण इसे 'भारत का रूर' कहा जाता है।</td>
              </tr>
              <tr>
                <td><strong>कटंगा पठार</strong></td>
                <td>कांगो लोकतांत्रिक गणराज्य (अफ्रीका)</td>
                <td>तांबा, कोबाल्ट, यूरेनियम</td>
                <td>बैटरी निर्माण में उपयोगी कोबाल्ट का दुनिया का सबसे बड़ा स्रोत।</td>
              </tr>
              <tr>
                <td><strong>किम्बरले पठार</strong></td>
                <td>पश्चिमी ऑस्ट्रेलिया</td>
                <td>हीरा, सोना, लौह अयस्क</td>
                <td>यहाँ प्रसिद्ध आर्गिल हीरे की खदान स्थित है (गुलाबी हीरों के लिए प्रसिद्ध)।</td>
              </tr>
              <tr>
                <td><strong>कनाडाई शील्ड (लॉरेंटियन)</strong></td>
                <td>कनाडा</td>
                <td>निकल, तांबा, लोहा, सोना</td>
                <td>विश्व के सबसे पुराने भूगर्भीय शील्ड क्षेत्रों में से एक।</td>
              </tr>
              <tr>
                <td><strong>पोटवार पठार</strong></td>
                <td>पाकिस्तान</td>
                <td>सेंधा नमक, पेट्रोलियम, चूना पत्थर</td>
                <td>साल्ट रेंज ब्लॉक पर्वतों के उत्तर में स्थित है।</td>
              </tr>
              <tr>
                <td><strong>लोएस पठार</strong></td>
                <td>उत्तरी चीन</td>
                <td>अत्यंत उपजाऊ महीन मिट्टी (Loess)</td>
                <td>गोबी मरुस्थल से उड़कर आई पीली धूल के निक्षेप से बना है।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. मैदान: संरचनात्मक, अपरदनात्मक और निक्षेपण प्रकार",
        "content": """<p>मैदान समतल या बहुत कम ढाल वाले निचले भूभाग होते हैं। उत्पत्ति के आधार पर इन्हें तीन श्रेणियों में बांटा जाता है:</p>
        
        <h3>A. संरचनात्मक मैदान</h3>
        <p>समुद्री नितल या महाद्वीपीय मग्नतट के ऊपर उठने (भू-उत्थान) से या चट्टानों की क्षैतिज परतों से बनते हैं।</p>
        <ul>
          <li><strong>उदाहरण:</strong> संयुक्त राज्य अमेरिका का ग्रेट प्लेन्स, रूसी प्लेटफॉर्म, ऑस्ट्रेलिया का मध्यवर्ती मैदान।</li>
        </ul>

        <h3>B. अपरदनात्मक मैदान (पेनीप्लेन और पेडीप्लेन)</h3>
        <p>बाह्य अपरदनकारी शक्तियों द्वारा पर्वतों या पठारों को काटकर उन्हें समतल करने से बनते हैं।</p>
        <ul>
          <li><strong>पेनीप्लेन (समप्राय मैदान):</strong> आर्द्र जलवायु में नदियों के दीर्घकालिक अपरदन से बनते हैं। इनमें बची हुई प्रतिरोधी चट्टानों की पहाड़ियों को **मोनाडनॉक (Monadnock)** कहते हैं।</li>
          <li><strong>पेडीप्लेन (पाद मैदान):</strong> शुष्क या अर्ध-शुष्क क्षेत्रों में वायु अपरदन और ढाल निवर्तन से बनते हैं। बची हुई पहाड़ियों को **इन्सेलबर्ग (Inselberg)** कहते हैं।</li>
        </ul>

        <h3>C. निक्षेपात्मक मैदान</h3>
        <p>नदियों, हवा, हिमनद या झीलों द्वारा बहाकर लाए गए अवसादों के जमाव से बनते हैं।</p>
        <ul>
          <li><strong>जलोढ़ / बाढ़ के मैदान:</strong> नदियों के निक्षेपण से बनते हैं। जैसे गंगा-यमुना का मैदान।
            <ul>
              <li>*भाबर:* शिवालिक के गिरिपद में कंकड़-पत्थरों से बनी छिद्रयुक्त पट्टी जहाँ नदियाँ भूमिगत हो जाती हैं।</li>
              <li>*तराई:* भाबर के आगे का दलदली और नम क्षेत्र जहाँ नदियाँ पुनः धरातल पर प्रकट होती हैं; यह सघन वनों से युक्त है।</li>
              <li>*बांगर:* पुराना जलोढ़ क्षेत्र, जो बाढ़ की पहुंच से दूर होता है; इसमें कंकड़ पाए जाते हैं।</li>
              <li>*खादर:* नवीन जलोढ़ मिट्टी वाला क्षेत्र, जहाँ हर साल बाढ़ का नया पानी पहुंचता है; यह अत्यंत उपजाऊ होता है।</li>
            </ul>
          </li>
          <li><strong>लोएस मैदान:</strong> हवा द्वारा उड़ाकर लाई गई बारीक धूल (धूल-कणों) के जमाव से बनते हैं। जैसे उत्तरी चीन का मैदान।</li>
          <li><strong>सरोवरीय मैदान (Lacustrine):</strong> झीलों में गाद जमा होने और उनके सूखने से बनते हैं। जैसे कश्मीर की घाटी और मणिपुर का इम्फाल बेसिन।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Which of the following is the oldest fold mountain range in the world?",
        "q_hi": "निम्नलिखित में से कौन सी विश्व की सबसे प्राचीन वलित पर्वत श्रृंखला है?",
        "opts": ["Ural Mountains", "Appalachian Mountains", "Aravalli Range", "Himalayas"],
        "opts_hi": ["यूराल पर्वत", "अप्पलाचियन पर्वत", "अरावली पर्वतमाला", "हिमालय"],
        "ans": 2,
        "sol": "The Aravalli Range in India is the oldest fold mountain range in the world, now highly denuded and classified as residual mountains.",
        "sol_hi": "भारत की अरावली पर्वतमाला विश्व की सबसे पुरानी वलित पर्वत श्रृंखला है, जो वर्तमान में अत्यधिक अपरदित होकर एक अवशिष्ट पर्वत के रूप में है।"
    },
    {
        "q": "The Black Forest Mountain in Germany is an example of which type of mountain?",
        "q_hi": "जर्मनी में स्थित 'ब्लैक फॉरेस्ट' (Black Forest) पर्वत किस प्रकार के पर्वत का उदाहरण है?",
        "opts": ["Fold Mountain", "Block Mountain", "Volcanic Mountain", "Residual Mountain"],
        "opts_hi": ["वलित पर्वत", "ब्लॉक (भ्रंशोत्थ) पर्वत", "ज्वालामुखी पर्वत", "अवशिष्ट पर्वत"],
        "ans": 1,
        "sol": "The Black Forest is a classic example of a Block Mountain (horst), separated from the Vosges Mountains in France by the Rhine Rift Valley (graben).",
        "sol_hi": "ब्लैक फॉरेस्ट एक प्रमुख ब्लॉक पर्वत का उदाहरण है, जो फ्रांस के वॉस्जेस पर्वत से राइन भ्रंश घाटी द्वारा अलग होता है।"
    },
    {
        "q": "Which of the following plateaus is surrounded by mountain ranges on all sides and is classified as an intermontane plateau?",
        "q_hi": "निम्नलिखित में से कौन सा पठार चारों ओर से पर्वत श्रृंखलाओं से घिरा हुआ है और उसे अंतर-पर्वतीय पठार के रूप में वर्गीकृत किया गया है?",
        "opts": ["Deccan Plateau", "Katanga Plateau", "Tibetan Plateau", "Patagonian Plateau"],
        "opts_hi": ["दक्कन का पठार", "कटंगा पठार", "तिब्बत का पठार", "पैटागोनिया का पठार"],
        "ans": 2,
        "sol": "The Tibetan Plateau is surrounded by the Himalayas to the south and the Kunlun Range to the north, making it a classic intermontane plateau.",
        "sol_hi": "तिब्बत का पठार दक्षिण में हिमालय और उत्तर में कुनलुन श्रेणी से घिरा हुआ है, इसलिए यह एक अंतर-पर्वतीय पठार का उदाहरण है।"
    },
    {
        "q": "Which plateau is widely known as the 'Ruhr of India' due to its rich mineral deposits?",
        "q_hi": "कौन सा पठार अपने समृद्ध खनिज भंडारों के कारण 'भारत का रूर' (Ruhr of India) नाम से प्रसिद्ध है?",
        "opts": ["Malwa Plateau", "Deccan Plateau", "Chhota Nagpur Plateau", "Shillong Plateau"],
        "opts_hi": ["मालवा का पठार", "दक्कन का पठार", "छोटा नागपुर पठार", "शिलांग का पठार"],
        "ans": 2,
        "sol": "The Chhota Nagpur Plateau is called the 'Ruhr of India' because of its concentration of coal, iron, bauxite, and other heavy minerals.",
        "sol_hi": "छोटा नागपुर पठार कोयला, लोहा, बॉक्साइट और अभ्रक की प्रचुरता के कारण 'भारत का रूर' कहलाता है।"
    },
    {
        "q": "In the context of landform cycles, what is the term used for the isolated, resistant residual hills left on a Peneplain?",
        "q_hi": "स्थलाकृतिक चक्रों के संदर्भ में, समप्राय मैदान (Peneplain) पर बचे हुए प्रतिरोधी अवशिष्ट टीलों/पहाड़ियों को क्या कहा जाता है?",
        "opts": ["Inselbergs", "Monadnocks", "Horsts", "Guyots"],
        "opts_hi": ["इन्सेलबर्ग", "मोनाडनॉक (Monadnocks)", "हॉर्स्ट", "गुयोट"],
        "ans": 1,
        "sol": "According to W.M. Davis's cycle of erosion in humid regions, the residual hills left on a peneplain are called Monadnocks.",
        "sol_hi": "डब्लू.एम. डेविस के आर्द्र अपरदन चक्र के अनुसार समप्राय मैदान (पेनीप्लेन) पर बची हुई प्रतिरोधी पहाड़ियों को मोनाडनॉक कहा जाता है।"
    },
    {
        "q": "Which type of plain is formed by the deposition of windblown silt, often yellow in color and highly fertile?",
        "q_hi": "हवा द्वारा उड़ाकर लाए गए बारीक धूल-कणों (जो अक्सर पीले रंग के होते हैं) के जमाव से किस प्रकार के उपजाऊ मैदान बनते हैं?",
        "opts": ["Alluvial Plain", "Loess Plain", "Lacustrine Plain", "Karst Plain"],
        "opts_hi": ["जलोढ़ मैदान", "लोएस मैदान (Loess Plain)", "सरोवरीय मैदान", "कार्स्ट मैदान"],
        "ans": 1,
        "sol": "Loess plains are formed by wind-deposited silt. The most famous example is the Loess Plateau and Plain in Northern China.",
        "sol_hi": "हवा द्वारा जमा किए गए धूल-कणों से लोएस मैदान बनते हैं, जिसका सबसे प्रमुख उदाहरण उत्तरी चीन में पाया जाता है।"
    },
    {
        "q": "In the Indo-Gangetic Plains, the newer, younger alluvial soil deposited annually by floods is known as:",
        "q_hi": "गंगा-यमुना के मैदानों में प्रतिवर्ष बाढ़ द्वारा लाई जाने वाली नवीन जलोढ़ मिट्टी को क्या कहा जाता है?",
        "opts": ["Bhabar", "Bhangar", "Khadar", "Terai"],
        "opts_hi": ["भाबर", "बांगर", "खादर (Khadar)", "तराई"],
        "ans": 2,
        "sol": "Khadar is the newer, younger alluvium deposited by floods every year, making it highly fertile. Bhangar is the older, less fertile alluvium.",
        "sol_hi": "बाढ़ के मैदानों में प्रतिवर्ष नई जलोढ़ मिट्टी के निक्षेपण से बनने वाले क्षेत्र को खादर कहते हैं, जो अत्यधिक उपजाऊ होता है।"
    },
    {
        "q": "Which mountain range is the longest continental mountain range in the world?",
        "q_hi": "विश्व की सबसे लंबी महाद्वीपीय पर्वत श्रृंखला कौन सी है?",
        "opts": ["Himalayas", "Rocky Mountains", "Andes Mountains", "Great Dividing Range"],
        "opts_hi": ["हिमालय", "रॉकी पर्वत", "एंडीज पर्वत (Andes)", "ग्रेट डिवाइडिंग रेंज"],
        "ans": 2,
        "sol": "The Andes Mountains in South America is the longest continental mountain range in the world, stretching over 7,000 km.",
        "sol_hi": "दक्षिणी अमेरिका में स्थित एंडीज पर्वत श्रृंखला (~7,000 किमी) विश्व की सबसे लंबी महाद्वीपीय पर्वत श्रृंखला है।"
    },
    {
        "q": "Which of the following is a block mountain range in India?",
        "q_hi": "निम्नलिखित में से कौन सी भारत में एक ब्लॉक (भ्रंशोत्थ) पर्वत श्रृंखला है?",
        "opts": ["Aravalli Range", "Satpura Range", "Himalayas", "Western Ghats (as a whole plateau edge)"],
        "opts_hi": ["अरावली श्रेणी", "सतपुड़ा श्रेणी (Satpura)", "हिमालय", "पश्चिमी घाट"],
        "ans": 1,
        "sol": "The Satpura Range is a horst (block mountain) bounded by the Narmada rift valley to the north and Tapi rift valley to the south.",
        "sol_hi": "सतपुड़ा पर्वत श्रेणी एक हॉर्स्ट (ब्लॉक पर्वत) है जिसके उत्तर में नर्मदा भ्रंश घाटी और दक्षिण में तापी भ्रंश घाटी स्थित है।"
    },
    {
        "q": "The plateau of Anatolia is situated in which country?",
        "q_hi": "अनातोलिया का पठार (Anatolia Plateau) किस देश में स्थित है?",
        "opts": ["Iran", "Turkey", "Iraq", "Syria"],
        "opts_hi": ["ईरान", "तुर्की (Turkey)", "इराक", "सीरिया"],
        "ans": 1,
        "sol": "The Anatolian Plateau is located in Turkey, situated between the Pontic Mountains in the north and the Taurus Mountains in the south.",
        "sol_hi": "अनातोलिया का पठार तुर्की के मध्य भाग में पोंटिक और टॉरस पर्वतों के बीच स्थित है।"
    },
    {
        "q": "Consider the following statements:\n1. Old fold mountains have rounded peaks and lower elevations due to erosion.\n2. Young fold mountains have sharp, rugged peaks and are seismically active.\nWhich of the statements given above is/are correct?",
        "q_hi": "निम्नलिखित कथनों पर विचार करें:\n1. प्राचीन वलित पर्वतों के शिखर अपरदन के कारण गोलाकार और ऊंचाई कम होती है।\n2. नवीन वलित पर्वतों के शिखर नुकीले व ऊंचे होते हैं और ये भूकंपीय रूप से सक्रिय होते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "Both statements are correct. Erosion rounds off old fold mountains, while young fold mountains are still growing and tectonic activity causes earthquakes.",
        "sol_hi": "दोनों कथन सही हैं। अपरदन के कारण पुराने वलित पर्वत घिस जाते हैं, जबकि युवा वलित पर्वत अभी भी बढ़ रहे हैं और भूकंपीय रूप से संवेदनशील होते हैं।"
    },
    {
        "q": "The Katanga Plateau in Africa is globally famous for the deposit of which minerals?",
        "q_hi": "अफ्रीका का 'कटंगा पठार' (Katanga Plateau) वैश्विक स्तर पर किन खनिजों के निक्षेप के लिए प्रसिद्ध है?",
        "opts": ["Gold and Diamonds", "Copper and Cobalt", "Iron and Coal", "Petroleum and Natural Gas"],
        "opts_hi": ["सोना और हीरा", "तांबा और कोबाल्ट (Copper & Cobalt)", "लोहा और कोयला", "पेट्रोलियम और प्राकृतिक गैस"],
        "ans": 1,
        "sol": "The Katanga Plateau in the Democratic Republic of Congo is rich in copper and cobalt, which are critical for electronic industries.",
        "sol_hi": "कांगो का कटंगा पठार तांबे और कोबाल्ट के विशाल भंडारों के लिए दुनिया भर में प्रसिद्ध है।"
    },
    {
        "q": "Which type of plain is formed by the drying up of lakes filled with river sediments?",
        "q_hi": "नदियों के अवसादों से झीलों के भर जाने और उनके सूखने से किस प्रकार के मैदानों का निर्माण होता है?",
        "opts": ["Karst Plain", "Lacustrine Plain", "Peneplain", "Loess Plain"],
        "opts_hi": ["कार्स्ट मैदान", "सरोवरीय मैदान (Lacustrine Plain)", "समप्राय मैदान", "लोएस मैदान"],
        "ans": 1,
        "sol": "Lacustrine plains (lake plains) are formed by deposition of sediments in lakes which later dry up. Examples include Kashmir Valley.",
        "sol_hi": "झीलों में तलछट जमा होने से बने समतल मैदानों को सरोवरीय मैदान कहा जाता है, जैसे कश्मीर घाटी।"
    },
    {
        "q": "Which of the following is a volcanic mountain?",
        "q_hi": "निम्नलिखित में से कौन सा एक ज्वालामुखी पर्वत है?",
        "opts": ["Mount Kilimanjaro", "Vosges Mountain", "Mount Mitchell", "Appalachian Mountain"],
        "opts_hi": ["माउंट किलिमंजारो (Kilimanjaro)", "वॉस्जेस पर्वत", "माउंट मिशेल", "अप्पलाचियन पर्वत"],
        "ans": 0,
        "sol": "Mount Kilimanjaro in Tanzania is a volcanic mountain (stratovolcano). Vosges is block, Mitchell and Appalachians are fold mountains.",
        "sol_hi": "तंजानिया में स्थित माउंट किलिमंजारो एक प्रसिद्ध ज्वालामुखी पर्वत है।"
    },
    {
        "q": "The plateau formed due to volcanic fissure eruption of fluid basaltic lava is called:",
        "q_hi": "तरल बेसाल्टिक लावे के शांत दरारी उद्भेदन से निर्मित पठार को क्या कहा जाता है?",
        "opts": ["Intermontane Plateau", "Piedmont Plateau", "Lava Plateau", "Erosional Plateau"],
        "opts_hi": ["अंतर-पर्वतीय पठार", "गिरिपद पठार", "लावा पठार (Lava Plateau)", "अपरदनात्मक पठार"],
        "ans": 2,
        "sol": "Lava plateaus are formed by fissure eruptions of basaltic lava. Deccan traps in India and Columbia plateau in USA are key examples.",
        "sol_hi": "दरारों से शांत रूप से लावे के बहने से लावा पठारों का निर्माण होता है, जैसे भारत का दक्कन ट्रैप।"
    },
    {
        "q": "What is the term used for the flat-topped undersea volcanic mountains that rise from the ocean floor but do not reach the water surface?",
        "q_hi": "समुद्री नितल से उठने वाले उन सपाट शीर्ष वाले ज्वालामुखीय पर्वतों को क्या कहते हैं जो समुद्र की सतह तक नहीं पहुँच पाते?",
        "opts": ["Monadnocks", "Inselbergs", "Guyots", "Horsts"],
        "opts_hi": ["मोनाडनॉक", "इन्सेलबर्ग", "गुयोट (Guyots)", "हॉर्स्ट"],
        "ans": 2,
        "sol": "Guyots are flat-topped volcanic seamounts that have been eroded and submerged below the sea level.",
        "sol_hi": "समुद्र के भीतर स्थित चपटे शिखर वाले पर्वतों को गुयोट कहा जाता है।"
    },
    {
        "q": "Which mountain range separates European Russia from Asian Russia?",
        "q_hi": "कौन सी पर्वत श्रृंखला यूरोपीय रूस को एशियाई रूस से अलग करती है?",
        "opts": ["Caucasus Mountains", "Ural Mountains", "Carpathian Mountains", "Alps Mountains"],
        "opts_hi": ["काकेशस पर्वत", "यूराल पर्वत (Ural Mountains)", "कार्पेथियन पर्वत", "आल्प्स पर्वत"],
        "ans": 1,
        "sol": "The Ural Mountains run north-south through western Russia and form the boundary between Europe and Asia.",
        "sol_hi": "यूराल पर्वत श्रृंखला यूरेशिया में यूरोप और एशिया की सीमा का निर्धारण करती है।"
    },
    {
        "q": "The Piedmont Plateau of the United States lies between which two major physiographic regions?",
        "q_hi": "संयुक्त राज्य अमेरिका का 'पीडमोंट पठार' (Piedmont Plateau) किन दो प्रमुख भौतिक प्रदेशों के बीच स्थित है?",
        "opts": [
            "Appalachian Mountains and Atlantic Coastal Plain",
            "Rocky Mountains and Great Plains",
            "Sierra Nevada and Great Basin",
            "Laurentian Shield and Great Lakes"
        ],
        "opts_hi": [
            "अप्पलाचियन पर्वत और अटलांटिक तटीय मैदान",
            "रॉकी पर्वत और ग्रेट प्लेन्स",
            "सिएरा नेवादा और ग्रेट बेसिन",
            "लॉरेंटियन शील्ड और महान झीलें"
        ],
        "ans": 0,
        "sol": "The Piedmont region of the US is a plateau located between the Appalachian Mountains to the west and the Atlantic coastal plain to the east.",
        "sol_hi": "अमेरिका का पीडमोंट पठार पश्चिम में अप्पलाचियन पर्वत और पूर्व में अटलांटिक तटीय मैदान के बीच स्थित है।"
    },
    {
        "q": "In which state of India is the Parasnath Hill, a famous relict/residual mountain and Jain pilgrimage site, located?",
        "q_hi": "भारत के किस राज्य में प्रसिद्ध अवशिष्ट पर्वत और जैन तीर्थस्थल 'पारसनाथ पहाड़ी' स्थित है?",
        "opts": ["Bihar", "Jharkhand", "Odisha", "Madhya Pradesh"],
        "opts_hi": ["बिहार", "झारखंड (Jharkhand)", "ओडिशा", "मध्य प्रदेश"],
        "ans": 1,
        "sol": "Parasnath Hill is located in the Giridih district of Jharkhand, rising from the Chhota Nagpur Plateau.",
        "sol_hi": "पारसनाथ पहाड़ी छोटा नागपुर पठार के पूर्वी हिस्से में झारखंड के गिरिडीह जिले में स्थित है।"
    },
    {
        "q": "The Valley of Kashmir is a classic example of which type of plain?",
        "q_hi": "कश्मीर की घाटी किस प्रकार के मैदान का एक उत्कृष्ट उदाहरण है?",
        "opts": ["Structural Plain", "Lacustrine Plain", "Loess Plain", "Karst Plain"],
        "opts_hi": ["संरचनात्मक मैदान", "सरोवरीय मैदान (Lacustrine Plain)", "लोएस मैदान", "कार्स्ट मैदान"],
        "ans": 1,
        "sol": "The Kashmir Valley was once a lake basin which got filled with alluvial and lacustrine deposits (Karewas) and later drained out.",
        "sol_hi": "कश्मीर की घाटी प्राचीन काल में एक झील थी, जिसके निक्षेपण से सरोवरीय मैदान का निर्माण हुआ। यहाँ करेवा मिट्टी पाई जाती है।"
    },
    {
        "q": "Which is the highest peak of the Alps mountain range in Europe?",
        "q_hi": "यूरोप की आल्प्स पर्वत श्रृंखला का सर्वोच्च शिखर कौन सा है?",
        "opts": ["Mount Blanc", "Mount Elbrus", "Mount Etna", "Mount Vesuvius"],
        "opts_hi": ["माउंट ब्लांक (Mount Blanc)", "माउंट एल्ब्रस", "माउंट एटना", "माउंट विसुवियस"],
        "ans": 0,
        "sol": "Mont Blanc (4,810 meters) on the France-Italy border is the highest peak of the Alps range. (Elbrus is in the Caucasus range).",
        "sol_hi": "माउंट ब्लांक (4,810 मीटर) आल्प्स पर्वत श्रृंखला का सर्वोच्च शिखर है जो फ्रांस और इटली की सीमा पर स्थित है।"
    },
    {
        "q": "Which plateau is known as the 'Roof of the World'?",
        "q_hi": "किस पठार को 'विश्व की छत' (Roof of the World) कहा जाता है?",
        "opts": ["Tibetan Plateau", "Pamir Plateau", "Colorado Plateau", "Deccan Plateau"],
        "opts_hi": ["तिब्बत का पठार", "पामीर का पठार (Pamir Plateau)", "कोलोराडो का पठार", "दक्कन का पठार"],
        "ans": 1,
        "sol": "The Pamir Plateau is historically referred to as the 'Roof of the World' (Bam-i-Dunya) due to its high elevation and central position in Asia.",
        "sol_hi": "पामीर के पठार को उसकी अत्यधिक ऊंचाई और मध्य एशियाई पर्वत प्रणालियों के केंद्र में होने के कारण 'विश्व की छत' कहा जाता है।"
    },
    {
        "q": "In which country is the Kimberley Plateau, famous for diamond mining, located?",
        "q_hi": "हीरे की खदानों के लिए प्रसिद्ध 'किम्बरले पठार' (Kimberley Plateau) किस देश में स्थित है?",
        "opts": ["South Africa", "Australia", "Canada", "Democratic Republic of Congo"],
        "opts_hi": ["दक्षिण अफ्रीका", "ऑस्ट्रेलिया (Australia)", "कनाडा", "कांगो गणराज्य"],
        "ans": 1,
        "sol": "The Kimberley Plateau is located in Western Australia. (Note: Kimberley city/pipes are in South Africa, but the Kimberley Plateau is in Australia).",
        "sol_hi": "किम्बरले पठार पश्चिमी ऑस्ट्रेलिया में स्थित है, जबकि किम्बरली हीरे की खदान शहर दक्षिण अफ्रीका में है।"
    },
    {
        "q": "The fertile plain of Hwang Ho river, covered with windblown yellow dust, is located in which country?",
        "q_hi": "ह्वैंग-हो नदी का उपजाऊ मैदान, जो हवा द्वारा लाई गई पीली मिट्टी से ढका है, किस देश में स्थित है?",
        "opts": ["Mongolia", "China", "Vietnam", "Japan"],
        "opts_hi": ["मंगोलिया", "चीन (China)", "वियतनाम", "जापान"],
        "ans": 1,
        "sol": "The North China Plain, drained by the Yellow River (Hwang Ho), is covered by fertile loess soils blown from the Gobi Desert.",
        "sol_hi": "उत्तरी चीन का मैदान ह्वैंग-हो (पीली नदी) द्वारा सिंचित है और यह लोएस मिट्टी के जमाव से बना है।"
    },
    {
        "q": "The Salt Range in Pakistan is which type of mountain?",
        "q_hi": "पाकिस्तान में स्थित 'साल्ट रेंज' (Salt Range) किस प्रकार का पर्वत है?",
        "opts": ["Block Mountain", "Fold Mountain", "Volcanic Mountain", "Residual Mountain"],
        "opts_hi": ["ब्लॉक पर्वत (Block Mountain)", "वलित पर्वत", "ज्वालामुखी पर्वत", "अवशिष्ट पर्वत"],
        "ans": 0,
        "sol": "The Salt Range in Pakistan is a classic example of block mountains formed due to faulting.",
        "sol_hi": "पाकिस्तान की साल्ट रेंज विवर्तनिक भ्रंशन के कारण निर्मित एक ब्लॉक पर्वत का उत्कृष्ट उदाहरण है।"
    },
    {
        "q": "What name is given to the damp, marshy tract of land situated south of the Bhabar belt in Northern India?",
        "q_hi": "उत्तरी भारत में भाबर पट्टी के दक्षिण में स्थित गीले, दलदली क्षेत्र को क्या नाम दिया गया है?",
        "opts": ["Khadar", "Bhangar", "Terai", "Kankar"],
        "opts_hi": ["खादर", "बांगर", "तराई (Terai)", "कंकड़"],
        "ans": 2,
        "sol": "The Terai region lies south of Bhabar. It is a marshy, water-logged zone with clayey soil and dense vegetation.",
        "sol_hi": "भाबर के दक्षिण में स्थित घने जंगलों और दलदली मिट्टी वाले बेल्ट को तराई कहा जाता है।"
    },
    {
        "q": "Which is the highest peak of the Rocky Mountains in North America?",
        "q_hi": "उत्तरी अमेरिका के रॉकी पर्वत (Rocky Mountains) का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Mount Mitchell", "Mount Albert", "Mount Elbert", "Mount Whitney"],
        "opts_hi": ["माउंट मिशेल", "माउंट अल्बर्ट", "माउंट एल्बर्ट (Mount Elbert)", "माउंट व्हिटनी"],
        "ans": 2,
        "sol": "Mount Elbert (4,401 meters) in Colorado is the highest peak of the Rocky Mountains.",
        "sol_hi": "माउंट एल्बर्ट (4,401 मीटर) रॉकी पर्वतमाला का सबसे ऊंचा पर्वत शिखर है।"
    },
    {
        "q": "The plateau of Potwar is located in which country?",
        "q_hi": "पोटवार का पठार (Potwar Plateau) किस देश में स्थित है?",
        "opts": ["Iran", "Afghanistan", "Pakistan", "India"],
        "opts_hi": ["ईरान", "अफगानिस्तान", "पाकिस्तान (Pakistan)", "भारत"],
        "ans": 2,
        "sol": "The Potwar Plateau is located in northeastern Pakistan, bounded by the Salt Range and the Indus River.",
        "sol_hi": "पोटवार का पठार पाकिस्तान के उत्तर-पूर्वी भाग में साल्ट रेंज के निकट स्थित है।"
    },
    {
        "q": "Which type of plain is formed by the dissolution and erosion of soluble rocks like limestone by groundwater?",
        "q_hi": "भूमिगत जल द्वारा चूना पत्थर जैसी घुलनशील चट्टानों के घुलने और अपरदन से किस प्रकार के मैदान बनते हैं?",
        "opts": ["Peneplain", "Pediplain", "Karst Plain", "Loess Plain"],
        "opts_hi": ["समप्राय मैदान", "पाद मैदान", "कार्स्ट मैदान (Karst Plain)", "लोएस मैदान"],
        "ans": 2,
        "sol": "Karst plains are formed by the chemical weathering and erosion of limestone rocks, creating features like sinkholes and caves.",
        "sol_hi": "चूना पत्थर वाले क्षेत्रों में भूमिगत जल के रासायनिक विलायन से बनने वाले उबड़-खाबड़ मैदान को कार्स्ट मैदान कहते हैं।"
    },
    {
        "q": "The Vosges mountain in France is an example of which type of mountain?",
        "q_hi": "फ्रांस में स्थित 'वॉस्जेस' (Vosges) पर्वत किस प्रकार के पर्वत का उदाहरण है?",
        "opts": ["Fold Mountain", "Block Mountain", "Volcanic Mountain", "Residual Mountain"],
        "opts_hi": ["वलित पर्वत", "ब्लॉक पर्वत (Block Mountain)", "ज्वालामुखी पर्वत", "अवशिष्ट पर्वत"],
        "ans": 1,
        "sol": "The Vosges is a block mountain (horst) located in eastern France, running parallel to the Black Forest of Germany.",
        "sol_hi": "वॉस्जेस पर्वत फ्रांस में स्थित एक ब्लॉक पर्वत है, जिसके समानांतर जर्मनी का ब्लैक फॉरेस्ट स्थित है।"
    },
    # --- ADDITIONAL 20 QUESTIONS TO REACH EXACTLY 50 ---
    {
        "q": "Consider the following pairs of plateaus and their mineral associations:\n1. Katanga Plateau - Copper and Cobalt\n2. Kimberley Plateau - Diamonds\n3. Chhota Nagpur Plateau - Iron and Coal\nWhich of the pairs given above are correctly matched?",
        "q_hi": "पठारों और उनके खनिज भंडारों के निम्नलिखित जोड़ों पर विचार करें:\n1. कटंगा पठार - तांबा और कोबाल्ट\n2. किम्बरले पठार - हीरा\n3. छोटा नागपुर पठार - लोहा और कोयला\nउपरोक्त जोड़ों में से कौन सा/से सही सुमेलित है/हैं?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 3,
        "sol": "All three pairs are correctly matched. Katanga (DR Congo) is famous for copper/cobalt, Kimberley (Australia) for diamonds, and Chhota Nagpur for iron/coal.",
        "sol_hi": "तीनों जोड़े सही सुमेलित हैं। कटंगा पठार तांबे-कोबाल्ट के लिए, किम्बरले पठार हीरे के लिए और छोटा नागपुर लोहा-कोयला के लिए प्रसिद्ध है।"
    },
    {
        "q": "Which is the highest peak of the Appalachian Mountains in North America?",
        "q_hi": "उत्तरी अमेरिका के अप्पलाचियन पर्वत (Appalachian Mountains) का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Mount Mitchell", "Mount Washington", "Mount Elbert", "Denali"],
        "opts_hi": ["माउंट मिशेल (Mount Mitchell)", "माउंट वाशिंगटन", "माउंट एल्बर्ट", "डेनाली"],
        "ans": 0,
        "sol": "Mount Mitchell (2,037 meters) in North Carolina is the highest peak of the Appalachian range.",
        "sol_hi": "माउंट मिशेल अप्पलाचियन श्रेणी का सबसे ऊंचा शिखर है जो अमेरिका के उत्तरी कैरोलिना राज्य में है।"
    },
    {
        "q": "Which of the following is a volcanic mountain in Ecuador, known as one of the highest active volcanoes in the world?",
        "q_hi": "निम्नलिखित में से कौन सा इक्वाडोर में स्थित एक ज्वालामुखी पर्वत है, जो विश्व के सबसे ऊंचे सक्रिय ज्वालामुखियों में से एक माना जाता है?",
        "opts": ["Mount Cotopaxi", "Mount Kilimanjaro", "Mount Fuji", "Mount Popa"],
        "opts_hi": ["माउंट कोटोपैक्सी (Cotopaxi)", "माउंट किलिमंजारो", "माउंट फुजी", "माउंट पोपा"],
        "ans": 0,
        "sol": "Mount Cotopaxi is an active stratovolcano in the Andes Mountains, located in Ecuador.",
        "sol_hi": "माउंट कोटोपैक्सी इक्वाडोर में एंडीज पर्वतमाला में स्थित एक सक्रिय ज्वालामुखी पर्वत है।"
    },
    {
        "q": "The 'Downs' are the temperate grasslands located on which continent?",
        "q_hi": "'डाउंस' (Downs) किस महाद्वीप में पाए जाने वाले शीतोष्ण घास के मैदान हैं?",
        "opts": ["South America", "Africa", "Australia", "Europe"],
        "opts_hi": ["दक्षिणी अमेरिका", "अफ्रीका", "ऑस्ट्रेलिया (Australia)", "यूरोप"],
        "ans": 2,
        "sol": "The Downs are temperate grasslands situated in the southern part of Australia.",
        "sol_hi": "डाउंस ऑस्ट्रेलिया के शीतोष्ण कटिबंधीय घास के मैदान हैं।"
    },
    {
        "q": "Which is the highest peak of the Andes mountain range in South America?",
        "q_hi": "दक्षिणी अमेरिका की एंडीज पर्वत श्रृंखला का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Mount Aconcagua", "Mount Chimborazo", "Mount Ojos del Salado", "Mount Cotopaxi"],
        "opts_hi": ["माउंट अकोंकागुआ (Aconcagua)", "माउंट चिम्बोरैजो", "माउंट ओजोस डेल सालाडो", "माउंट कोटोपैक्सी"],
        "ans": 0,
        "sol": "Mount Aconcagua (6,961 meters) is the highest peak of the Andes and the entire Western Hemisphere.",
        "sol_hi": "माउंट अकोंकागुआ एंडीज पर्वत श्रृंखला और पूरे पश्चिमी गोलार्ध का सबसे ऊंचा पर्वत शिखर है।"
    },
    {
        "q": "The flat, featureless plains formed in arid regions by wind erosion and scarp retreat are called:",
        "q_hi": "शुष्क क्षेत्रों में पवन अपरदन और कगार निवर्तन (scarp retreat) द्वारा बने समतल मैदानों को क्या कहते हैं?",
        "opts": ["Peneplains", "Pediplains", "Karst Plains", "Loess Plains"],
        "opts_hi": ["पेनीप्लेन", "पेडीप्लेन (Pediplains)", "कार्स्ट मैदान", "लोएस मैदान"],
        "ans": 1,
        "sol": "Pediplains are formed in dry climates through the coalescence of pediments, as proposed by L.C. King.",
        "sol_hi": "शुष्क और अर्ध-शुष्क क्षेत्रों में पवन क्रिया से बनने वाले समतल मैदान पेडीप्लेन कहलाते हैं।"
    },
    {
        "q": "In which country is the Laurentian Plateau (Canadian Shield) located?",
        "q_hi": "लॉरेंटियन पठार (कनाडाई शील्ड) किस देश में स्थित है?",
        "opts": ["United States", "Canada", "Russia", "Greenland"],
        "opts_hi": ["संयुक्त राज्य अमेरिका", "कनाडा (Canada)", "रूस", "ग्रीनलैंड"],
        "ans": 1,
        "sol": "The Laurentian Plateau, also called the Canadian Shield, covers a large part of eastern and central Canada.",
        "sol_hi": "लॉरेंटियन पठार या कनाडाई शील्ड कनाडा के पूर्वी और मध्य भाग में स्थित एक अत्यंत प्राचीन पठार है।"
    },
    {
        "q": "Which of the following is a classic example of an old fold mountain range in North America?",
        "q_hi": "निम्नलिखित में से कौन सा उत्तरी अमेरिका में प्राचीन वलित पर्वत का एक उत्कृष्ट उदाहरण है?",
        "opts": ["Rocky Mountains", "Appalachian Mountains", "Cascade Range", "Sierra Nevada"],
        "opts_hi": ["रॉकी पर्वत", "अप्पलाचियन पर्वत (Appalachians)", "कैस्केड रेंज", "सिएरा नेवादा"],
        "ans": 1,
        "sol": "The Appalachian Mountains are old fold mountains formed during the Caledonian/Hercynian phases, now highly eroded.",
        "sol_hi": "अप्पलाचियन पर्वत श्रृंखला उत्तरी अमेरिका के पूर्व में स्थित एक प्राचीन वलित पर्वत है।"
    },
    {
        "q": "The process of mountain building is technically known as:",
        "q_hi": "पर्वत निर्माण की प्रक्रिया को तकनीकी रूप से किस नाम से जाना जाता है?",
        "opts": ["Orogeny", "Epeirogeny", "Weathering", "Denudation"],
        "opts_hi": ["पर्वत निर्माणकारी संचलन (Orogeny)", "महाद्वीप निर्माणकारी संचलन", "अपक्षय", "अनाच्छादन"],
        "ans": 0,
        "sol": "Orogeny is the geological term for mountain-building processes, primarily driven by plate tectonics.",
        "sol_hi": "पर्वत निर्माण की प्रक्रिया को ओरोजेनी (Orogeny) या पर्वत निर्माणकारी संचलन कहते हैं।"
    },
    {
        "q": "Which mountain range separates France and Spain?",
        "q_hi": "कौन सी पर्वत श्रृंखला फ्रांस और स्पेन की सीमा बनाती है?",
        "opts": ["Alps Mountains", "Pyrenees Mountains", "Apennines Mountains", "Carpathian Mountains"],
        "opts_hi": ["आल्प्स पर्वत", "पायरेनीस पर्वत (Pyrenees)", "अपैनाइंस पर्वत", "कार्पेथियन पर्वत"],
        "ans": 1,
        "sol": "The Pyrenees mountain range forms a high natural border between France and Spain.",
        "sol_hi": "पायरेनीस पर्वत श्रृंखला फ्रांस और स्पेन के बीच एक प्राकृतिक सीमा का निर्धारण करती है।"
    },
    {
        "q": "Which of the following plateaus is rich in rock salt and is bounded by salt-rich block mountains?",
        "q_hi": "निम्नलिखित में से कौन सा पठार सेंधा नमक के लिए समृद्ध है और नमक युक्त ब्लॉक पर्वतों से घिरा है?",
        "opts": ["Potwar Plateau", "Colorado Plateau", "Tibetan Plateau", "Anatolian Plateau"],
        "opts_hi": ["पोटवार का पठार (Potwar)", "कोलोराडो का पठार", "तिब्बत का पठार", "अनातोलिया का पठार"],
        "ans": 0,
        "sol": "The Potwar Plateau in Pakistan is bounded by the Salt Range, famous for the Khewra Salt Mines.",
        "sol_hi": "पाकिस्तान का पोटवार पठार साल्ट रेंज पहाड़ियों से घिरा है जहाँ सेंधा नमक की प्रसिद्ध खेवड़ा खदानें हैं।"
    },
    {
        "q": "The flat depositional plains formed by the accumulation of windblown glacial dust and desert silt are known as:",
        "q_hi": "हिमानी धूल या मरुस्थलीय महीन सिल्ट के निक्षेपण से बने समतल मैदानों को किस नाम से जाना जाता है?",
        "opts": ["Loess Plains", "Alluvial Plains", "Glacial Outwash Plains", "Structural Plains"],
        "opts_hi": ["लोएस मैदान (Loess)", "जलोढ़ मैदान", "हिमानी निक्षेपित मैदान", "संरचनात्मक मैदान"],
        "ans": 0,
        "sol": "Loess is wind-deposited dust that is weakly cemented. It forms extensive yellow plains in China.",
        "sol_hi": "हवा द्वारा उड़ाकर लाई गई बारीक पीली मिट्टी के जमाव को लोएस कहते हैं।"
    },
    {
        "q": "In the context of plain morphology, which zone consists of older alluvial soils with calcareous deposits?",
        "q_hi": "मैदानों की संरचना के संदर्भ में, पुरानी जलोढ़ मिट्टी और कंकड़ (कैल्शियम जमाव) वाले क्षेत्र को क्या कहते हैं?",
        "opts": ["Khadar", "Bhangar", "Bhabar", "Terai"],
        "opts_hi": ["खादर", "बांगर (Bhangar)", "भाबर", "तराई"],
        "ans": 1,
        "sol": "Bhangar is the older alluvial plain that lies above the flood level, characterized by calcareous nodules called Kankar.",
        "sol_hi": "पुराने जलोढ़ मिट्टी वाले मैदानी भाग को बांगर कहते हैं जिसमें चूना युक्त कंकड़ पाए जाते हैं।"
    },
    {
        "q": "Which is the highest peak in the Cascade Mountain range in western North America?",
        "q_hi": "पश्चिमी उत्तरी अमेरिका की कैस्केड पर्वतमाला (Cascade Range) का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Mount Rainier", "Mount Shasta", "Mount Hood", "Mount St. Helens"],
        "opts_hi": ["माउंट रेनियर (Mount Rainier)", "माउंट शास्ता", "माउंट हूड", "माउंट सेंट हेलेंस"],
        "ans": 0,
        "sol": "Mount Rainier (4,392 meters) in Washington state is the highest peak of the Cascade Range.",
        "sol_hi": "माउंट रेनियर संयुक्त राज्य अमेरिका के वाशिंगटन राज्य में स्थित कैस्केड श्रेणी का सबसे ऊंचा पर्वत शिखर है।"
    },
    {
        "q": "Which of the following is a Piedmont plateau?",
        "q_hi": "निम्नलिखित में से कौन सा एक गिरिपद पठार (Piedmont Plateau) है?",
        "opts": ["Patagonian Plateau", "Tibetan Plateau", "Anatolian Plateau", "Deccan Plateau"],
        "opts_hi": ["पैटागोनिया का पठार (Patagonian)", "तिब्बत का पठार", "अनातोलिया का पठार", "दक्कन का पठार"],
        "ans": 0,
        "sol": "The Patagonian Plateau is a piedmont plateau, bordered by the Andes mountains on the west and the Atlantic Ocean on the east.",
        "sol_hi": "एंडीज पर्वत के चरणों में स्थित अर्जेंटीना का पैटागोनिया का पठार एक गिरिपद पठार का उदाहरण है।"
    },
    {
        "q": "Which mountain range forms the boundary between the Baltic Sea basin and the Atlantic Ocean in Northern Europe?",
        "q_hi": "उत्तरी यूरोप में कौन सी पर्वत श्रृंखला बाल्टिक सागर बेसिन और अटलांटिक महासागर के बीच सीमा बनाती है?",
        "opts": ["Scandinavian Mountains", "Ural Mountains", "Pyrenees Mountains", "Alps Mountains"],
        "opts_hi": ["स्कैंडिनेवियाई पर्वत (Scandinavian)", "यूराल पर्वत", "पायरेनीस पर्वत", "आल्प्स पर्वत"],
        "ans": 0,
        "sol": "The Scandinavian Mountains run through the Scandinavian Peninsula, separating Norway and Sweden.",
        "sol_hi": "स्कैंडिनेवियाई पर्वत श्रृंखला स्कैंडिनेवियाई प्रायद्वीप में स्थित है जो नॉर्वे और स्वीडन को अलग करती है।"
    },
    {
        "q": "What name is given to the dry, hard calcareous nodules found in the Bhangar alluvial plains of India?",
        "q_hi": "भारत के बांगर जलोढ़ मैदानों में पाए जाने वाले चूना युक्त कठोर नोड्यूल (कणों) को क्या नाम दिया गया है?",
        "opts": ["Bhabar", "Kankar", "Khadar", "Terai"],
        "opts_hi": ["भाबर", "कंकड़ (Kankar)", "खादर", "तराई"],
        "ans": 1,
        "sol": "Kankar are calcium carbonate nodules found in the older alluvial soils (Bhangar).",
        "sol_hi": "बांगर जलोढ़ मिट्टी में पाए जाने वाले चूना पत्थरों के छोटे टुकड़ों को स्थानीय भाषा में कंकड़ कहा जाता है।"
    },
    {
        "q": "The plateau of Colorado in the United States is bordered by which fold mountains?",
        "q_hi": "संयुक्त राज्य अमेरिका का 'कोलोराडो पठार' किस वलित पर्वत श्रेणी से घिरा हुआ है?",
        "opts": ["Appalachian Mountains", "Rocky Mountains", "Sierra Nevada", "Cascade Range"],
        "opts_hi": ["अप्पलाचियन पर्वत", "रॉकी पर्वत (Rocky Mountains)", "सिएरा नेवादा", "कैस्केड रेंज"],
        "ans": 1,
        "sol": "The Colorado Plateau is an intermontane plateau bounded by the Rocky Mountains to the east and north.",
        "sol_hi": "कोलोराडो का पठार एक अंतर-पर्वतीय पठार है जो पूर्व और उत्तर में रॉकी पर्वत श्रेणी से घिरा हुआ है।"
    },
    {
        "q": "Which is the highest peak in the Vindhya Range in Central India?",
        "q_hi": "मध्य भारत में स्थित विंध्याचल श्रेणी (Vindhya Range) का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Dhupgarh", "Amarkantak", "Kalumar Peak (Sadbhavna Shikhar)", "Parasnath"],
        "opts_hi": ["धूपगढ़", "अमरकंटक", "कालुमार शिखर / सद्भावना शिखर", "पारसनाथ"],
        "ans": 2,
        "sol": "Kalumar Peak, also known as Sadbhavna Shikhar (Goodwill Peak), is the highest point of the Vindhya Range.",
        "sol_hi": "विंध्याचल श्रेणी का सर्वोच्च बिंदु कालुमार शिखर है जिसे सद्भावना शिखर भी कहा जाता है।"
    },
    {
        "q": "Which plain is formed by the tectonic upliftment of a continental shelf or seabed?",
        "q_hi": "कौन सा मैदान महाद्वीपीय मग्नतट या समुद्री नितल के विवर्तनिक उत्थान से बनता है?",
        "opts": ["Structural Plain", "Depositional Plain", "Erosional Plain", "Lacustrine Plain"],
        "opts_hi": ["संरचनात्मक मैदान (Structural Plain)", "निक्षेपात्मक मैदान", "अपरदनात्मक मैदान", "सरोवरीय मैदान"],
        "ans": 0,
        "sol": "Structural plains are formed by tectonic forces causing the uplift of shallow marine shelves. Example: Great Plains of USA.",
        "sol_hi": "विवर्तनिक हलचलों के कारण उथले समुद्री भागों के ऊपर उठने से संरचनात्मक मैदानों का निर्माण होता है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which of the following is correct regarding block mountains?",
        "q_hi": "ब्लॉक (भ्रंशोत्थ) पर्वतों के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "They are formed by compressional folding of rock strata",
            "The uplifted block is called Graben, and subsided is Horst",
            "The uplifted block is called Horst, and subsided is Graben",
            "They are formed solely by volcanic lava accumulation"
        ],
        "opts_hi": [
            "ये चट्टान की परतों के संपीड़न वलन द्वारा निर्मित होते हैं",
            "ऊपर उठे हुए हिस्से को ग्राबेन और नीचे धंसे हिस्से को हॉर्स्ट कहते हैं",
            "ऊपर उठे हुए हिस्से को हॉर्स्ट और नीचे धंसे हिस्से को ग्राबेन कहते हैं",
            "ये केवल ज्वालामुखी लावे के जमाव से बनते हैं"
        ],
        "ans": 2,
        "sol": "In block faulting, the uplifted block is a Horst (block mountain) and the downthrown block is a Graben (rift valley).",
        "sol_hi": "ब्लॉक पर्वतों में भ्रंशन के कारण ऊपर उठे खंड को हॉर्स्ट और नीचे धंसे हुए खंड को ग्राबेन कहा जाता है।"
    },
    {
        "q": "The Appalachian Mountains in North America and the Urals in Russia are examples of:",
        "q_hi": "उत्तरी अमेरिका के अप्पलाचियन पर्वत और रूस के यूराल पर्वत किसके उदाहरण हैं?",
        "opts": ["Young Fold Mountains", "Old Fold Mountains", "Block Mountains", "Volcanic Mountains"],
        "opts_hi": ["नवीन वलित पर्वत", "प्राचीन वलित पर्वत (Old Fold)", "ब्लॉक पर्वत", "ज्वालामुखी पर्वत"],
        "ans": 1,
        "sol": "The Appalachians and Urals are old fold mountains that have been severely eroded over geological time.",
        "sol_hi": "यूराल और अप्पलाचियन दोनों प्राचीन वलित पर्वत श्रेणियाँ हैं जो अपरदन के कारण अब काफी घिस चुकी हैं।"
    },
    {
        "q": "Which plateau is surrounded by the Pontic Mountains in the north and the Taurus Mountains in the south?",
        "q_hi": "कौन सा पठार उत्तर में पोंटिक पर्वत और दक्षिण में टॉरस पर्वत से घिरा हुआ है?",
        "opts": ["Anatolian Plateau", "Tibetan Plateau", "Iranian Plateau", "Colorado Plateau"],
        "opts_hi": ["अनातोलिया का पठार (Anatolian)", "तिब्बत का पठार", "ईरान का पठार", "कोलोराडो का पठार"],
        "ans": 0,
        "sol": "The Anatolian Plateau in Turkey is situated between the Pontic and Taurus fold ranges.",
        "sol_hi": "तुर्की का अनातोलिया पठार उत्तर में पोंटिक और दक्षिण में टॉरस पर्वत श्रेणियों के मध्य स्थित है।"
    },
    {
        "q": "The residual hills left behind on an arid/semi-arid plain (Pediplain) due to wind erosion are called:",
        "q_hi": "पवन अपरदन के कारण शुष्क/अर्ध-शुष्क मैदानों (पेडीप्लेन) पर बचे हुए अवशिष्ट टीलों को क्या कहते हैं?",
        "opts": ["Monadnocks", "Inselbergs", "Guyots", "Seamounts"],
        "opts_hi": ["मोनाडनॉक", "इन्सेलबर्ग (Inselbergs)", "गुयोट", "सी माउंट"],
        "ans": 1,
        "sol": "In L.C. King's arid cycle of erosion, the residual hills left on a pediplain are called Inselbergs.",
        "sol_hi": "शुष्क अपरदन चक्र के दौरान पेडीप्लेन पर बची प्रतिरोधी चट्टानी पहाड़ियों को इन्सेलबर्ग कहा जाता है।"
    },
    {
        "q": "The marshy, forest-covered tract in the Northern Plains of India where underground streams emerge is called:",
        "q_hi": "भारत के उत्तरी मैदानों में वह दलदली और वनाच्छादित क्षेत्र जहाँ भूमिगत नदियाँ पुनः धरातल पर प्रकट होती हैं, कहलाता है:",
        "opts": ["Bhabar", "Terai", "Bhangar", "Khadar"],
        "opts_hi": ["भाबर", "तराई (Terai)", "बांगर", "खादर"],
        "ans": 1,
        "sol": "The Terai is a wet, marshy region situated south of Bhabar, where rivers re-emerge.",
        "sol_hi": "तराई क्षेत्र भाबर के दक्षिण में स्थित दलदली क्षेत्र है जहाँ नदियाँ पुनः धरातल पर प्रकट होती हैं।"
    },
    {
        "q": "Which is the highest peak in the Vindhyan Range in Central India?",
        "q_hi": "मध्य भारत में विंध्य श्रेणी का सर्वोच्च शिखर कौन सा है?",
        "opts": ["Amarkantak", "Dhupgarh", "Kalumar Peak (Sadbhavna Shikhar)", "Guru Shikhar"],
        "opts_hi": ["अमरकंटक", "धूपगढ़", "कालुमार शिखर (Sadbhavna)", "गुरु शिखर"],
        "ans": 2,
        "sol": "Kalumar Peak, also called Sadbhavna Shikhar, is the highest peak of the Vindhyan range at 752m.",
        "sol_hi": "विंध्य श्रेणी की सबसे ऊंची चोटी कालुमार शिखर (सद्भावना शिखर, 752 मी) है।"
    },
    {
        "q": "Which of the following is NOT an intermontane plateau?",
        "q_hi": "निम्नलिखित में से कौन सा एक अंतर-पर्वतीय पठार नहीं है?",
        "opts": ["Tibetan Plateau", "Bolivian Plateau", "Patagonian Plateau", "Anatolian Plateau"],
        "opts_hi": ["तिब्बत का पठार", "बोलीविया का पठार", "पैटागोनिया का पठार (Patagonian)", "अनातोलिया का पठार"],
        "ans": 2,
        "sol": "The Patagonian Plateau is a piedmont plateau, whereas the others are intermontane plateaus surrounded by mountain ranges.",
        "sol_hi": "पैटागोनिया का पठार गिरिपद पठार है, जबकि अन्य तीनों अंतर-पर्वतीय पठार हैं।"
    },
    {
        "q": "What are the hills formed of older alluvium that contain calcareous clay nodules (Kankar) in Northern India called?",
        "q_hi": "उत्तरी भारत में पुरानी जलोढ़ मिट्टी से बने वे भाग जिनमें चूना युक्त कंकड़ पाए जाते हैं, क्या कहलाते हैं?",
        "opts": ["Khadar", "Bhangar", "Bhabar", "Terai"],
        "opts_hi": ["खादर", "बांगर (Bhangar)", "भाबर", "तराई"],
        "ans": 1,
        "sol": "Bhangar is the older alluvial plain, which is higher and contains calcium carbonate deposits called Kankar.",
        "sol_hi": "पुरानी जलोढ़ मिट्टी वाले मैदानी क्षेत्र को बांगर कहते हैं।"
    },
    {
        "q": "The Sierra Nevada mountain range in California, USA is an example of:",
        "q_hi": "कैलिफोर्निया, यूएसए में स्थित 'सिएरा नेवादा' (Sierra Nevada) पर्वत श्रेणी किसका उदाहरण है?",
        "opts": ["Block Mountain", "Fold Mountain", "Volcanic Mountain", "Residual Mountain"],
        "opts_hi": ["ब्लॉक पर्वत (Block Mountain)", "वलित पर्वत", "ज्वालामुखी पर्वत", "अवशिष्ट पर्वत"],
        "ans": 0,
        "sol": "Sierra Nevada is the largest block mountain in the world, formed by faulting of a huge crustal block.",
        "sol_hi": "सिएरा नेवादा विश्व का सबसे बड़ा ब्लॉक पर्वत है जो कैलिफोर्निया (यूएसए) में स्थित है।"
    },
    {
        "q": "Which river valley separates the Vindhyan Range from the Satpura Range in India?",
        "q_hi": "कौन सी नदी घाटी भारत में विंध्य श्रेणी को सतपुड़ा श्रेणी से अलग करती है?",
        "opts": ["Tapi Valley", "Narmada Valley", "Godavari Valley", "Son Valley"],
        "opts_hi": ["तापी घाटी", "नर्मदा घाटी (Narmada Valley)", "गोदावरी घाटी", "सोन घाटी"],
        "ans": 1,
        "sol": "The Narmada River flows in a rift valley situated between the Vindhya Range (to the north) and the Satpura Range (to the south).",
        "sol_hi": "नर्मदा नदी एक भ्रंश घाटी में बहती है जो उत्तर में विंध्याचल और दक्षिण में सतपुड़ा पर्वत श्रेणी के बीच स्थित है।"
    },
    {
        "q": "Which is the highest peak of the Satpura Range in India?",
        "q_hi": "भारत में सतपुड़ा श्रेणी का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Amarkantak", "Dhupgarh", "Parasnath", "Guru Shikhar"],
        "opts_hi": ["अमरकंटक", "धूपगढ़ (Dhupgarh)", "पारसनाथ", "गुरु शिखर"],
        "ans": 1,
        "sol": "Mount Dhupgarh (1,350m) in the Mahadeo Hills is the highest peak of the Satpura Range.",
        "sol_hi": "महादेव पहाड़ियों में स्थित धूपगढ़ शिखर (1,350 मीटर) सतपुड़ा पर्वत श्रेणी का सबसे ऊंचा शिखर है।"
    },
    {
        "q": "Which is the highest mountain peak of the Appalachian range in USA?",
        "q_hi": "यूएसए में अप्पलाचियन पर्वतमाला की सबसे ऊंची चोटी कौन सी है?",
        "opts": ["Mount Mitchell", "Mount Rainier", "Mount Washington", "Mount Elbert"],
        "opts_hi": ["माउंट मिशेल (Mount Mitchell)", "माउंट रेनियर", "माउंट वाशिंगटन", "माउंट एल्बर्ट"],
        "ans": 0,
        "sol": "Mount Mitchell is the highest peak of the Appalachian range, rising to 2,037m.",
        "sol_hi": "माउंट मिशेल अप्पलाचियन पर्वतमाला का सबसे ऊंचा शिखर है।"
    },
    {
        "q": "Which type of plain is formed by the deposition of fertile yellow dust transported by wind from the Gobi Desert?",
        "q_hi": "गोबी मरुस्थल से हवा द्वारा उड़ाकर लाए गए उपजाऊ पीले धूल कणों के जमाव से कौन सा मैदान बनता है?",
        "opts": ["Alluvial Plain", "Karst Plain", "Loess Plain", "Glacial Plain"],
        "opts_hi": ["जलोढ़ मैदान", "कार्स्ट मैदान", "लोएस मैदान (Loess Plain)", "हिमानी मैदान"],
        "ans": 2,
        "sol": "The Loess Plain of North China is formed by dust blown from the Gobi Desert.",
        "sol_hi": "उत्तरी चीन का प्रसिद्ध लोएस मैदान गोबी रेगिस्तान से हवा द्वारा उड़ाकर लाई गई पीली मिट्टी से बना है।"
    },
    {
        "q": "The plateau of Kimberley, rich in diamond reserves, is situated in which part of Australia?",
        "q_hi": "हीरे के भंडारों से समृद्ध 'किम्बरले पठार' ऑस्ट्रेलिया के किस भाग में स्थित है?",
        "opts": ["Western Australia", "Eastern Australia", "Southern Australia", "Northern Territory"],
        "opts_hi": ["पश्चिमी ऑस्ट्रेलिया (Western Australia)", "पूर्वी ऑस्ट्रेलिया", "दक्षिणी ऑस्ट्रेलिया", "उत्तरी क्षेत्र"],
        "ans": 0,
        "sol": "The Kimberley Plateau is situated in the northern part of Western Australia.",
        "sol_hi": "किम्बरले पठार पश्चिमी ऑस्ट्रेलिया के उत्तरी भाग में स्थित है।"
    },
    {
        "q": "In W.M. Davis's cycle of erosion, the nearly flat featureless erosional plain is called a Peneplain, and the residual hills are called:",
        "q_hi": "डब्ल्यू.एम. डेविस के अपरदन चक्र में समप्राय मैदान को पेनीप्लेन और उस पर बची पहाड़ियों को क्या कहते हैं?",
        "opts": ["Inselbergs", "Monadnocks", "Guyots", "Horsts"],
        "opts_hi": ["इन्सेलबर्ग", "मोनाडनॉक (Monadnocks)", "गुयोट", "हॉर्स्ट"],
        "ans": 1,
        "sol": "Monadnocks are the residual hills on a peneplain in Davis's humid cycle of erosion.",
        "sol_hi": "डेविस के आर्द्र अपरदन चक्र में पेनीप्लेन (समप्राय मैदान) पर मिलने वाली अवशिष्ट पहाड़ियों को मोनाडनॉक कहा जाता है।"
    }
]

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Comprehensive review of Mountains, Plateaus, and Plains.", "sections": deep_dive_en}
    }

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Mountain Geomorphology",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which is the oldest fold mountain range in the world?", "opts": ["Himalayas", "Appalachians", "Aravallis", "Urals"], "ans": 2, "sol": "The Aravalli Range is the oldest fold range on Earth."},
                    {"type": "MCQ", "q": "What is the uplifted block between two faults called?", "opts": ["Graben", "Horst", "Monadnock", "Guyot"], "ans": 1, "sol": "Uplifted fault block is a Horst (block mountain)."},
                    {"type": "True/False", "q": "True or False: The Black Forest of Germany is a block mountain.", "ans": True, "sol": "True. It is a horst bounded by the Rhine graben."},
                    {"type": "One-Liner", "q": "What is the highest mountain peak in South America?", "sol": "Mount Aconcagua"}
                ]
            },
            {
                "title": "2. Plateaus & Minerals",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which plateau is surrounded by Pontic and Taurus mountains?", "opts": ["Tibetan Plateau", "Anatolian Plateau", "Deccan Plateau", "Colorado Plateau"], "ans": 1, "sol": "The Anatolian Plateau in Turkey is intermontane, bounded by the Pontic and Taurus ranges."},
                    {"type": "MCQ", "q": "Which plateau is known as the Ruhr of India?", "opts": ["Deccan Plateau", "Malwa Plateau", "Chhota Nagpur Plateau", "Shillong Plateau"], "ans": 2, "sol": "The Chhota Nagpur Plateau is the 'Ruhr of India'."},
                    {"type": "True/False", "q": "True or False: The Katanga Plateau is famous for copper and cobalt.", "ans": True, "sol": "True. It is in DR Congo."},
                    {"type": "One-Liner", "q": "Where is the Kimberley Plateau located?", "sol": "Western Australia"}
                ]
            },
            {
                "title": "3. Plains & Geomorphology",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is the term for residual hills on a Peneplain?", "opts": ["Inselbergs", "Monadnocks", "Kankar", "Horsts"], "ans": 1, "sol": "Davis termed residual hills on a peneplain as Monadnocks."},
                    {"type": "MCQ", "q": "Which plain is formed by windblown yellow dust?", "opts": ["Alluvial Plain", "Loess Plain", "Lacustrine Plain", "Karst Plain"], "ans": 2, "sol": "Loess plains are formed by windblown dust, like in China."},
                    {"type": "True/False", "q": "True or False: Khadar is older alluvial soil.", "ans": False, "sol": "False. Khadar is newer fertile alluvium, Bhangar is older alluvium."},
                    {"type": "One-Liner", "q": "What region lies north of the Terai, where streams disappear?", "sol": "Bhabar"}
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
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "पर्वत, पठार और मैदानों की विस्तृत समीक्षा।", "sections": deep_dive_hi}
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
                "title": "1. पर्वत भू-आकृति विज्ञान",
                "masteryZone": [
                    {"type": "MCQ", "q": "विश्व की सबसे प्राचीन वलित पर्वत श्रृंखला कौन सी है?", "opts": ["हिमालय", "अप्पलाचियन", "अरावली", "यूराल"], "ans": 2, "sol": "अरावली पर्वत श्रृंखला पृथ्वी की सबसे प्राचीन वलित श्रेणी है।"},
                    {"type": "MCQ", "q": "दो भ्रंशों के बीच उठे हुए ब्लॉक को क्या कहते हैं?", "opts": ["ग्राबेन", "हॉर्स्ट", "मोनाडनॉक", "गुयोट"], "ans": 1, "sol": "ऊपर उठे हुए ब्लॉक को हॉर्स्ट (ब्लॉक पर्वत) कहते हैं।"},
                    {"type": "True/False", "q": "सही या गलत: जर्मनी का ब्लैक फॉरेस्ट एक ब्लॉक पर्वत है।", "ans": True, "sol": "सही। यह राइन ग्राबेन से घिरा एक हॉर्स्ट है।"},
                    {"type": "One-Liner", "q": "दक्षिणी अमेरिका का सर्वोच्च पर्वत शिखर कौन सा है?", "sol": "माउंट अकोंकागुआ"}
                ]
            },
            {
                "title": "2. पठार और खनिज",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सा पठार पोंटिक और टॉरस पर्वतों से घिरा है?", "opts": ["तिब्बत का पठार", "अनातोलिया का पठार", "दक्कन का पठार", "कोलोराडो का पठार"], "ans": 1, "sol": "तुर्की का अनातोलिया पठार पोंटिक और टॉरस श्रेणियों के बीच अंतर-पर्वतीय पठार है।"},
                    {"type": "MCQ", "q": "किस पठार को 'भारत का रूर' कहा जाता है?", "opts": ["दक्कन का पठार", "मालवा का पठार", "छोटा नागपुर पठार", "शिलांग का पठार"], "ans": 2, "sol": "छोटा नागपुर पठार को 'भारत का रूर' कहा जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: कटंगा पठार तांबे और कोबाल्ट के लिए प्रसिद्ध है।", "ans": True, "sol": "सही। यह कांगो लोकतांत्रिक गणराज्य में है।"},
                    {"type": "One-Liner", "q": "किम्बरले पठार कहाँ स्थित है?", "sol": "पश्चिमी ऑस्ट्रेलिया"}
                ]
            },
            {
                "title": "3. मैदान और भू-आकृति विज्ञान",
                "masteryZone": [
                    {"type": "MCQ", "q": "पेनीप्लेन पर मिलने वाली अवशिष्ट पहाड़ियों को क्या कहते हैं?", "opts": ["इन्सेलबर्ग", "मोनाडनॉक", "कंकड़", "हॉर्स्ट"], "ans": 1, "sol": "डेविस ने आर्द्र चक्र में पेनीप्लेन पर मिलने वाली अवशिष्ट पहाड़ियों को मोनाडनॉक कहा।"},
                    {"type": "MCQ", "q": "हवा द्वारा लाई गई पीली मिट्टी से कौन से मैदान बनते हैं?", "opts": ["जलोढ़ मैदान", "लोएस मैदान", "सरोवरीय मैदान", "कार्स्ट मैदान"], "ans": 2, "sol": "हवा द्वारा जमा पीली उपजाऊ मिट्टी से लोएस मैदान बनते हैं।"},
                    {"type": "True/False", "q": "सही या गलत: खादर पुराना जलोढ़ क्षेत्र है।", "ans": False, "sol": "गलत। खादर नवीन जलोढ़ है, बांगर पुराना जलोढ़ क्षेत्र है।"},
                    {"type": "One-Liner", "q": "तराई के उत्तर में स्थित वह क्षेत्र कौन सा है जहाँ नदियाँ विलीन हो जाती हैं?", "sol": "भाबर"}
                ]
            }
        ]
    }

# ----------------- FILE GENERATION -----------------
import re

def parse_markdown(data):
    if isinstance(data, str):
        return re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #e67e22; font-weight: 700;">\1</strong>', data)
    elif isinstance(data, dict):
        return {k: parse_markdown(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parse_markdown(item) for item in data]
    return data

def write_json(filepath, data):
    formatted_data = parse_markdown(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())
