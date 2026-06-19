# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "continents-major-oceans"
TOPIC_DISPLAY = "Continents and Major Oceans"
TOPIC_DISPLAY_HI = "महाद्वीप और प्रमुख महासागर"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\geography\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "Geography",
    "parentUrl": "../",
    "current": "Continents & Oceans"
}

hero_en = {
    "title": "Continents and Major Oceans",
    "description": "Master the physical geography of the Earth's 7 continents and 5 major oceans, highlighting highest peaks, major trenches, tectonic frameworks, and crucial RO/ARO exam details."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Geography Mock Test",
        "description": "Evaluate your understanding of continental landforms, ocean trenches, currents, and geographical extremes. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Evolution of Earth's Continents & Oceans",
    "description": "Major geological milestones in the formation of modern continents and oceans.",
    "cards": [
        {
            "period": "Supercontinent Pangaea",
            "date": "300 Mya",
            "details": "All landmasses clustered into a single supercontinent surrounded by the massive ocean Panthalassa."
        },
        {
            "period": "Triassic Drift",
            "date": "200 Mya",
            "details": "Pangaea split into Laurasia (Northern landmass) and Gondwanaland (Southern landmass) with the Tethys Sea in between."
        },
        {
            "period": "Opening of the Atlantic",
            "date": "150 Mya",
            "details": "The separation of South America from Africa and North America from Eurasia initiated the birth of the Atlantic Ocean."
        },
        {
            "period": "Himalayan Orogeny",
            "date": "50 Mya",
            "details": "The collision of the Indian Plate with the Eurasian Plate closed the Tethys Sea, elevating the Himalayas."
        },
        {
            "period": "Modern Epoch",
            "date": "Present",
            "details": "Seven distinct continents and five interconnected oceans define the current global map, constantly modified by plate tectonics."
        }
    ]
}

mnemonics_en = {
    "title": "Geography Mnemonics",
    "description": "Memory hooks to recall continental sizes and oceanic features.",
    "items": [
        {
            "title": "Mnemonic 1: Continents by Size (Descending)",
            "phrase": "\"AS-AF-NA-SA-AN-EU-AU (As If No Same Animal Eated Ants)\"",
            "decryption": "Recalls the order of continents from largest to smallest by land area:<br>1. **AS** — Asia<br>2. **AF** — Africa<br>3. **NA** — North America<br>4. **SA** — South America<br>5. **AN** — Antarctica<br>6. **EU** — Europe<br>7. **AU** — Australia"
        },
        {
            "title": "Mnemonic 2: Oceans by Size (Descending)",
            "phrase": "\"PA-AT-IN-SO-AR (PAISA)\"",
            "decryption": "Recalls the order of oceans from largest to smallest by surface area:<br>• **P** — Pacific Ocean<br>• **A** — Atlantic Ocean<br>• **I** — Indian Ocean<br>• **S** — Southern Ocean<br>• **A** — Arctic Ocean"
        },
        {
            "title": "Mnemonic 3: Deepest Ocean Trenches",
            "phrase": "\"M-P-S-S (Mariana - Puerto Rico - Sunda - South Sandwich)\"",
            "decryption": "Recalls the deepest trenches of major oceans in order:<br>• **M** — Mariana Trench (Pacific Ocean)<br>• **P** — Puerto Rico Trench (Atlantic Ocean)<br>• **S** — Sunda / Java Trench (Indian Ocean)<br>• **S** — South Sandwich Trench (Southern Ocean)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "Which continent is known as the 'Dark Continent' and why?",
            "answer": "**Africa**. It was called so because its interior regions remained largely unexplored and unknown to the outside world until the 19th century.",
            "icon": "fa-map"
        },
        {
            "question": "Which is the smallest continent, and what is its highest peak?",
            "answer": "**Australia** (often called Oceania). Its highest peak is **Mount Kosciuszko** (2,228 meters).",
            "icon": "fa-mountain"
        },
        {
            "question": "Which ocean has an 'S' shape and features the Mid-Atlantic Ridge?",
            "answer": "The **Atlantic Ocean**. It is the second-largest ocean and acts as the busiest trade waterway globally.",
            "icon": "fa-water"
        },
        {
            "question": "What is the Ring of Fire and where is it located?",
            "answer": "A horseshoe-shaped belt of high volcanic activity and earthquakes lining the basin of the **Pacific Ocean**, caused by subduction of tectonic plates.",
            "icon": "fa-fire"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing the highest peak of Europe with Asia. Europe's highest peak is **Mount Elbrus** (5,642m) in the Caucasus range, not Mont Blanc (which is only the highest in Western Europe).",
        "<strong>Trap 2:</strong> Mistaking the largest island for a continent. **Greenland** is the largest island on Earth, belonging politically to Denmark and geographically to North America, but it is not a continent itself (Australia is the smallest continent).",
        "<strong>Trap 3:</strong> Confusing Java Trench with Puerto Rico Trench. The **Java (Sunda) Trench** is the deepest point of the Indian Ocean, whereas the **Puerto Rico Trench** is the deepest point of the Atlantic Ocean.",
        "<strong>Trap 4:</strong> Believing the Southern Ocean is just a generic name. In 2000, the IHO officially demarcated the **Southern Ocean** as the waters surrounding Antarctica south of 60°S latitude."
    ]
}

deep_dive_en = [
    {
        "title": "1. Continents of the World: Detailed Physical & Political Analysis",
        "content": """<p>Continents cover 29.2% of the Earth's surface. Here is a high-yield breakdown of geographic features heavily tested in RO/ARO exams:</p>
        
        <h3>A. Asia</h3>
        <ul>
          <li><strong>Relief & Peaks:</strong> Mount Everest (8,848.86m) in the Himalayas (Nepal-Tibet border). Contains the **Pamir Knot** ('Roof of the World'), the Karakoram, Kunlun, and Tien Shan ranges.</li>
          <li><strong>Deserts:</strong> **Gobi Desert** (cold desert, China/Mongolia), **Taklamakan** (China), **Thar** (India/Pakistan), and **Karakum** (Turkmenistan).</li>
          <li><strong>Rivers & Basins:</strong> **Yangtze** (longest in Asia, China), **Mekong** ('Danube of the East'), **Ob-Irtysh**, **Yenisey**, and **Lena** (north-flowing rivers forming vast swamps in Siberia).</li>
          <li><strong>Lakes & Seas:</strong> **Caspian Sea** (largest lake on Earth by area), **Lake Baikal** (deepest lake, Siberia), **Dead Sea** (lowest point on land, -430m, Jordan-Israel border), and **Aral Sea** (rapidly shrinking lake in Central Asia).</li>
        </ul>

        <h3>B. Africa</h3>
        <ul>
          <li><strong>Unique Geography:</strong> The only continent crossed by the **Equator**, **Tropic of Cancer**, and **Tropic of Capricorn**. It is bounded by the Mediterranean Sea (North), Red Sea and Indian Ocean (East), and Atlantic Ocean (West).</li>
          <li><strong>Peaks & Mountains:</strong> **Mount Kilimanjaro** (5,895m, Tanzania) is a dormant volcanic peak. **Atlas Mountains** in the northwest (Morocco, Algeria, Tunisia) and **Drakensberg** in the south.</li>
          <li><strong>Rivers:</strong> 
            <ul>
              <li>**Nile River:** Longest river in the world, originating near **Lake Victoria** (crossed by Equator) and flowing north into the Mediterranean.</li>
              <li>**Congo (Zaire) River:** Second largest river by volume; **crosses the Equator twice**.</li>
              <li>**Limpopo River:** Flows through southern Africa; **crosses the Tropic of Capricorn twice**.</li>
              <li>**Zambezi River:** Famous for **Victoria Falls** and Kariba Dam.</li>
            </ul>
          </li>
          <li><strong>Deserts & Graben:</strong> **Sahara Desert** (largest hot desert), **Kalahari** and **Namib** deserts. Features the **Great Rift Valley** (stretching from Lebanon to Mozambique) filled with deep lakes like Tanganyika, Malawi, and Albert (Note: Lake Victoria is NOT in the rift valley system).</li>
        </ul>

        <h3>C. North America</h3>
        <ul>
          <li><strong>Mountains:</strong> **Rocky Mountains** (western fold belt) and **Appalachians** (geologically older, eastern belt, highest peak: **Mount Mitchell**, 2,037m). Highest peak of continent is **Denali** (Mount McKinley, 6,190m) in Alaska.</li>
          <li><strong>The Great Lakes:</strong> A chain of 5 freshwater lakes: **Superior** (largest by area), **Michigan** (the only Great Lake situated **entirely within the USA**), **Huron**, **Erie**, and **Ontario**. Connected to the Atlantic via the St. Lawrence River.</li>
          <li><strong>Rivers:</strong> **Mississippi-Missouri** river system (forms a bird's-foot delta), **Colorado River** (famous for carving the Grand Canyon), and **Mackenzie River** (longest in Canada).</li>
          <li><strong>Lowest Point:</strong> **Death Valley** (-86m) in California, Mojave Desert (hottest place in North America).</li>
        </ul>

        <h3>D. South America</h3>
        <ul>
          <li><strong>Mountains & Peaks:</strong> **Andes Range** (longest continental mountain range, stretching over 7,000 km along the west coast). Highest peak is **Mount Aconcagua** (6,961m, Argentina).</li>
          <li><strong>Rivers:</strong> **Amazon River** (largest river in the world by water discharge/volume, second longest; originates in Peru and empties into the Atlantic). **Orinoco River** (hosts Angel Falls, the world's highest waterfall, on its tributary Churun).</li>
          <li><strong>Lakes & Deserts:</strong> **Lake Titicaca** (highest navigable lake, Peru-Bolivia border). **Atacama Desert** (driest non-polar desert on Earth, located in Chile, caused by rain-shadow and the cold Humboldt/Peru Current). **Patagonian Desert** (cold rain-shadow desert in Argentina).</li>
          <li><strong>Grasslands:</strong> **Pampas** (fertile temperate grasslands of Argentina/Uruguay) and **Llanos** (tropical grasslands of Orinoco basin).</li>
        </ul>

        <h3>E. Europe</h3>
        <ul>
          <li><strong>Physical Boundaries:</strong> Separated from Asia by the **Ural Mountains**, **Caucasus Mountains**, **Caspian Sea**, and the **Ural River**. Coastline is highly indented, making it ideal for natural harbors. **No deserts exist in Europe**.</li>
          <li><strong>Mountains & Peaks:</strong> **Mount Elbrus** (5,642m) in the Caucasus is Europe's highest peak. **Alps Range** (highest peak: **Mont Blanc**, 4,810m, border of France and Italy), **Apennines** (Italy), **Pyrenees** (France-Spain border).</li>
          <li><strong>Rivers:</strong> **Volga River** (longest in Europe, drains into Caspian Sea). **Danube River** (second longest, passes through 4 capital cities: Vienna, Bratislava, Budapest, Belgrade, and empties into the Black Sea). **Rhine River** (busiest commercial river, forming a delta with the Meuse).</li>
        </ul>

        <h3>F. Australia / Oceania</h3>
        <ul>
          <li><strong>Topography:</strong> Smallest and flattest continent. Bounded by the Indian Ocean (West) and Pacific Ocean (East). Home to the **Great Barrier Reef** (world's largest coral reef system, off Queensland's coast).</li>
          <li><strong>Mountains & Rivers:</strong> **Great Dividing Range** running north-south on the east coast. Highest peak is **Mount Kosciuszko** (2,228m). Major river system is the **Murray-Darling**.</li>
          <li><strong>Deserts & Lakes:</strong> High proportion of arid land ('The Outback'). Deserts include **Great Sandy**, **Gibson**, **Great Victoria**, and **Simpson**. Bounded to the south by the Great Australian Bight. **Lake Eyre** is the lowest point (-15m).</li>
          <li><strong>Grasslands:</strong> **Downs** (temperate grasslands).</li>
        </ul>

        <h3>G. Antarctica</h3>
        <ul>
          <li><strong>Physical features:</strong> Fifth largest continent, completely frozen. Covered by an ice sheet averaging 1.9 km in thickness, containing 70% of Earth's fresh water. Transantarctic Mountains divide it into East and West. Highest peak is **Vinson Massif** (4,892m). Contains **Mount Erebus**, the southern-most active volcano on Earth.</li>
          <li><strong>Indian Antarctic Program:</strong> India has established three research stations here:
            <ul>
              <li>**Dakshin Gangotri** (1983) - India's first station, now decommissioned and buried in ice.</li>
              <li>**Maitri** (1989) - Second active station, near Schirmacher Oasis.</li>
              <li>**Bharati** (2012) - Third active, state-of-the-art station located in Larsmann Hills.</li>
            </ul>
          </li>
        </ul>"""
    },
    {
        "title": "2. The Five Oceans: Profiles, Trenches & Marginal Seas",
        "content": """<p>Oceans cover 70.8% of the Earth's surface. Here is a comparative analysis of the five oceans:</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Ocean</th>
                <th>Size Rank</th>
                <th>Deepest Point (Trench)</th>
                <th>Key Currents & Marginal Seas</th>
                <th>Distinct Features</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Pacific Ocean</strong></td>
                <td>1st (Largest)</td>
                <td>Mariana Trench (Challenger Deep, 10,994m)</td>
                <td>Kuroshio (Warm), Oyashio (Cold), Humboldt (Cold). Seas: South China Sea, Coral Sea, Sea of Japan.</td>
                <td>Covers over 30% of Earth's surface. Ring of Fire lines its basin (high seismicity). Almost circular.</td>
              </tr>
              <tr>
                <td><strong>Atlantic Ocean</strong></td>
                <td>2nd</td>
                <td>Puerto Rico Trench (Milwaukee Deep, 8,376m)</td>
                <td>Gulf Stream (Warm), Labrador (Cold), Canary (Cold). Seas: Caribbean Sea, Mediterranean Sea, North Sea.</td>
                <td>S-shaped basin. Busiest ocean for trade. Features the **Sargasso Sea** (bound by currents, no land borders) and **Grand Banks** (Labrador and Gulf Stream meet, causing thick fog and rich fishing).</td>
              </tr>
              <tr>
                <td><strong>Indian Ocean</strong></td>
                <td>3rd</td>
                <td>Sunda / Java Trench (7,290m)</td>
                <td>Agulhas (Warm), West Australian (Cold), Monsoonal drift. Seas: Red Sea, Arabian Sea, Andaman Sea.</td>
                <td>Only ocean named after a country. Bounded by Asia on the north (a landlocked 'half ocean'). Key islands: Madagascar, Diego Garcia, Sri Lanka.</td>
              </tr>
              <tr>
                <td><strong>Southern Ocean</strong></td>
                <td>4th</td>
                <td>South Sandwich Trench (Factorian Deep, 7,434m)</td>
                <td>Antarctic Circumpolar Current (West Wind Drift - strongest current on Earth).</td>
                <td>Surrounds Antarctica south of 60°S latitude. Formed by merger of Pacific, Atlantic, and Indian waters. Very cold and nutrient-rich.</td>
              </tr>
              <tr>
                <td><strong>Arctic Ocean</strong></td>
                <td>5th (Smallest)</td>
                <td>Fram Basin (Eurasian Basin, 5,550m)</td>
                <td>Transpolar Drift Current. Seas: Barents Sea, Beaufort Sea, East Siberian Sea.</td>
                <td>Located around the North Pole. Smallest and shallowest. Connected to the Pacific via the shallow Bering Strait. Mostly ice-locked.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. Ocean Bottom Relief & Topography",
        "content": """<p>The ocean floor features diverse geomorphological zones, analogous to land reliefs:</p>
        <ul>
          <li><strong>Continental Shelf:</strong> The gently sloping seaward extension of the continental block (average slope is 1°). Depths rarely exceed 200 meters. Widest shelf is the Siberian Shelf in the Arctic Ocean. **Holds 20% of the world's petroleum and natural gas resources**.</li>
          <li><strong>Continental Slope:</strong> Connects the shelf to the deep ocean floor. Average gradient is between 2° and 5°. Characterized by deep **submarine canyons** carved by turbidity currents.</li>
          <li><strong>Continental Rise:</strong> A gentle slope of sediment accumulation at the base of the continental slope, sloping at 0.5° to 1°.</li>
          <li><strong>Deep Ocean Floor / Abyssal Plains:</strong> Extremely flat, sediment-covered plains located between 3,000m and 6,000m depth. They cover about 40% of the ocean floor and host features like **seamounts** (underwater volcanoes) and **guyots** (flat-topped seamounts).</li>
          <li><strong>Ocean Deeps / Trenches:</strong> Deep, narrow depressions representing plate boundaries (subduction zones). They are seismically active and lack sediment cover due to steep slopes.</li>
        </ul>"""
    },
    {
        "title": "4. Continental Drift & Plate Tectonics",
        "content": """<p>Two major theories explain the present layout of land and sea:</p>
        
        <h3>A. Continental Drift Theory (Alfred Wegener, 1912)</h3>
        <ul>
          <li>Proposed that during the Carboniferous period, all continents were joined as a supercontinent named **Pangaea** (All Earth), surrounded by a super-ocean named **Panthalassa** (All Water).</li>
          <li>Pangaea later split into **Laurasia** (or Angaraland, Northern landmass) and **Gondwanaland** (Southern landmass) with the **Tethys Sea** forming between them.</li>
          <li>**Evidence:** Matching coastlines of South America and Africa (Jigsaw fit), geological rock age correlations, fossil distribution (e.g., *Glossopteris* fern, *Mesosaurus* reptile), and glacial deposits (tillite) across Gondwana continents.</li>
        </ul>

        <h3>B. Plate Tectonics Theory (1960s)</h3>
        <ul>
          <li>Formulated by McKenzie, Parker, and Morgan, building on Harry Hess's **Seafloor Spreading** concept. The Earth's lithosphere is divided into 7 major and several minor rigid plates floating over the asthenosphere.</li>
          <li><strong>7 Major Plates:</strong> 1. Pacific Plate (largest, oceanic), 2. North American, 3. South American, 4. Eurasian, 5. African, 6. Indo-Australian, 7. Antarctic.</li>
          <li><strong>Key Minor Plates:</strong> **Nazca Plate** (between South America & Pacific), **Cocos Plate** (between Central America & Pacific), **Arabian Plate**, **Philippine Plate**, and **Caribbean Plate**.</li>
          <li><strong>Plate Boundaries:</strong>
            <ul>
              <li>**Divergent Boundaries (Constructive):** Plates pull apart, magma rises to form new crust (e.g., Mid-Atlantic Ridge, East African Rift).</li>
              <li>**Convergent Boundaries (Destructive):** Plates collide, one subducts under the other, forming fold mountains and trenches (e.g., Himalayas, Mariana Trench).</li>
              <li>**Transform Boundaries (Conservative):** Plates slide horizontally past each other, crust is neither created nor destroyed (e.g., San Andreas Fault in California).</li>
            </ul>
          </li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "भूगोल",
    "parentUrl": "../",
    "current": "महाद्वीप और महासागर"
}

hero_hi = {
    "title": "महाद्वीप और प्रमुख महासागर",
    "description": "पृथ्वी के 7 महाद्वीपों और 5 प्रमुख महासागरों के भौतिक भूगोल को विस्तार से समझें, जिसमें सर्वोच्च पर्वत शिखर, महासागरीय गर्त, विवर्तनिकी ढांचा और महत्वपूर्ण परीक्षा तथ्य शामिल हैं।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव भूगोल मॉक टेस्ट",
        "description": "महाद्वीपीय स्थलाकृतियों, महासागरीय गर्तों, धाराओं और भौगोलिक चरम सीमाओं पर आधारित 15-प्रश्न मॉक टेस्ट।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "पृथ्वी के महाद्वीपों और महासागरों का विकास",
    "description": "आधुनिक महाद्वीपों और महासागरों के निर्माण में प्रमुख भूगर्भीय मील के पत्थर।",
    "cards": [
        {
            "period": "महामहाद्वीप पैंजिया (Pangaea)",
            "date": "30 करोड़ वर्ष पूर्व",
            "details": "सभी भूभाग मिलकर एक एकल विशाल भूखंड पैंजिया के रूप में थे, जो पैंथालसा नामक महासागर से घिरा था।"
        },
        {
            "period": "ट्रियासिक विभाजन",
            "date": "20 करोड़ वर्ष पूर्व",
            "details": "पैंजिया दो भागों में विभाजित हुआ: लारेशिया (उत्तरी भूखंड) और गोंडवानालैंड (दक्षिणी भूखंड), जिसके बीच में टेथिस सागर का जन्म हुआ।"
        },
        {
            "period": "अटलांटिक महासागर का उदय",
            "date": "15 करोड़ वर्ष पूर्व",
            "details": "अफ्रीका से दक्षिण अमेरिका और यूरेशिया से उत्तरी अमेरिका के पृथक्करण के साथ अटलांटिक महासागर की शुरुआत हुई।"
        },
        {
            "period": "हिमालयी पर्वत निर्माण",
            "date": "5 करोड़ वर्ष पूर्व",
            "details": "भारतीय प्लेट और यूरेशियाई प्लेट के आपस में टकराने से टेथिस सागर बंद हो गया और विशाल हिमालय पर्वत का उत्थान हुआ।"
        },
        {
            "period": "आधुनिक काल",
            "date": "वर्तमान",
            "details": "आज की सात विशिष्ट महाद्वीप और पांच परस्पर जुड़े महासागर प्लेट विवर्तनिकी की निरंतर गतिविधियों से आकार पा रहे हैं।"
        }
    ]
}

mnemonics_hi = {
    "title": "भूगोल के स्मृति सूत्र (Mnemonics)",
    "description": "महाद्वीपों और महासागरों के आकार और विशिष्टताओं को याद रखने की आसान ट्रिक्स।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: क्षेत्रफल के अनुसार महाद्वीप (अवरोही क्रम)",
            "phrase": "\"AS-AF-NA-SA-AN-EU-AU\"",
            "decryption": "महाद्वीपों का घटता हुआ आकार:<br>1. **AS** — एशिया (Asia)<br>2. **AF** — अफ्रीका (Africa)<br>3. **NA** — उत्तरी अमेरिका (North America)<br>4. **SA** — दक्षिणी अमेरिका (South America)<br>5. **AN** — अंटार्कटिका (Antarctica)<br>6. **EU** — यूरोप (Europe)<br>7. **AU** — ऑस्ट्रेलिया (Australia)"
        },
        {
            "title": "स्मृति सूत्र 2: आकार के अनुसार महासागर (अवरोही क्रम)",
            "phrase": "\"PAISA (पैसा)\"",
            "decryption": "महासागरों का घटता हुआ क्षेत्रफल:<br>• **P** — प्रशांत महासागर (Pacific)<br>• **A** — अटलांटिक महासागर (Atlantic)<br>• **I** — हिंद महासागर (Indian)<br>• **S** — दक्षिणी महासागर (Southern)<br>• **A** — आर्कटिक महासागर (Arctic)"
        },
        {
            "title": "स्मृति सूत्र 3: प्रमुख महासागरीय गर्त (गहरे बिंदु)",
            "phrase": "\"M-P-S-S (मारियाना - प्यूर्टो रिको - सुंडा - साउथ सैंडविच)\"",
            "decryption": "विभिन्न महासागरों के सबसे गहरे गर्तों का क्रम:<br>• **M** — मारियाना गर्त (प्रशांत महासागर)<br>• **P** — प्यूर्टो रिको गर्त (अटलांटिक महासागर)<br>• **S** — सुंडा/जावा गर्त (हिंद महासागर)<br>• **S** — साउथ सैंडविच गर्त (दक्षिणी महासागर)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "किस महाद्वीप को 'अंध महाद्वीप' (Dark Continent) कहा जाता था और क्यों?",
            "answer": "**अफ्रीका** को। क्योंकि 19वीं शताब्दी तक इसका आंतरिक भाग बाहरी दुनिया के लिए काफी हद तक अज्ञात और दुर्गम बना रहा था।",
            "icon": "fa-map"
        },
        {
            "question": "विश्व का सबसे छोटा महाद्वीप कौन सा है और उसका सर्वोच्च बिंदु क्या है?",
            "answer": "**ASCII/ऑस्ट्रेलिया** (ओशिनिया)। इसका सर्वोच्च पर्वत शिखर **माउंट कोसिअस्को** (2,228 मीटर) है।",
            "icon": "fa-mountain"
        },
        {
            "question": "अंग्रेजी के 'S' आकार में फैला हुआ महासागर कौन सा है जिसमें मध्य-अटलांटिक कटक स्थित है?",
            "answer": "**अटलांटिक महासागर** (अंध महासागर)। यह व्यापारिक दृष्टिकोण से दुनिया का सबसे व्यस्त महासागर है।",
            "icon": "fa-water"
        },
        {
            "question": "प्रशांत महासागर के किनारों पर स्थित सक्रिय भूकंपीय एवं ज्वालामुखीय क्षेत्र को क्या कहते हैं?",
            "answer": "**रिंग ऑफ फायर (अग्नि वलय)**, जो प्लेटों के अभिसरण के कारण उत्पन्न होता है।",
            "icon": "fa-fire"
        }
    ]
}

traps_hi = {
    "title": "परीक्षा में बचाव योग्य सामान्य भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> यूरोप के सर्वोच्च शिखर को आल्प्स की पहाड़ियों में ढूंढना। यूरोप का सबसे ऊंचा पर्वत शिखर काकेशस श्रेणी में स्थित **माउंट एल्ब्रस** (5,642 मीटर) है, न कि आल्प्स का माउंट ब्लांक (जो केवल पश्चिमी यूरोप का सबसे ऊंचा है)।",
        "<strong>भ्रम 2:</strong> सबसे बड़े द्वीप को महाद्वीप समझना। **ग्रीनलैंड** दुनिया का सबसे बड़ा द्वीप है, जो भौगोलिक रूप से उत्तरी अमेरिका में है और राजनीतिक रूप से डेनमार्क के अधीन है, लेकिन यह कोई महाद्वीप नहीं है। ऑस्ट्रेलिया सबसे छोटा महाद्वीप है।",
        "<strong>भ्रम 3:</strong> सुंडा (जावा) गर्त और प्यूर्टो रिको गर्त में उलझना। **प्यूर्टो रिको गर्त** अटलांटिक महासागर का सबसे गहरा बिंदु है, जबकि **सुंडा गर्त** हिंद महासागर का सबसे गहरा बिंदु है।",
        "<strong>भ्रम 4:</strong> दक्षिणी महासागर को काल्पनिक मान लेना। अंतर्राष्ट्रीय जल सर्वेक्षण संगठन (IHO) ने वर्ष 2000 में अंटार्कटिका महाद्वीप के चारों ओर 60 डिग्री दक्षिणी अक्षांश तक के जल क्षेत्र को आधिकारिक तौर पर **दक्षिणी महासागर** का दर्जा दिया है।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. विश्व के महाद्वीप: विस्तृत भौतिक और राजनीतिक विश्लेषण",
        "content": """<p>महाद्वीप पृथ्वी की सतह के लगभग 29.2% भाग को कवर करते हैं। परीक्षाओं की दृष्टि से अत्यंत महत्वपूर्ण भौगोलिक तत्वों का विवरण निम्नलिखित है:</p>
        
        <h3>A. एशिया</h3>
        <ul>
          <li><strong>पर्वत और शिखर:</strong> माउंट एवरेस्ट (8,848.86 मी) नेपाल-तिब्बत सीमा पर स्थित है। यहाँ **पामीर की गांठ** ('विश्व की छत'), कराकोरम, कुनलुन और तियान शान श्रेणियां स्थित हैं।</li>
          <li><strong>मरुस्थल:</strong> **गोबी मरुस्थल** (ठंडा मरुस्थल, चीन/मंगोलिया), **तकलामकान** (चीन), **थार** (भारत/पाकिस्तान) और **कराकुम** (तुर्कमेनिस्तान)।</li>
          <li><strong>नदियाँ:</strong> **यांग्त्ज़ी** (एशिया की सबसे लंबी नदी, चीन), **मेकांग** ('पूर्व की डेन्यूब'), **ओब-इर्तिश**, **येनिसि** और **लीना** (साइबेरिया से उत्तर की ओर बहने वाली नदियाँ)।</li>
          <li><strong>झीलें और सागर:</strong> **कैस्पियन सागर** (विश्व की क्षेत्रफल में सबसे बड़ी झील), **बैकाल झील** (विश्व की सबसे गहरी झील, साइबेरिया), **मृत सागर** (-430 मी, सबसे निचला स्थल बिंदु) और **अरल सागर** (तेजी से सिकुड़ रही झील)।</li>
        </ul>

        <h3>B. अफ्रीका</h3>
        <ul>
          <li><strong>विशिष्ट भूगोल:</strong> यह एकमात्र महाद्वीप है जिससे **भूमध्य रेखा**, **कर्क रेखा** और **मकर रेखा** तीनों गुजरती हैं।</li>
          <li><strong>पर्वत और शिखर:</strong> **माउंट किलिमंजारो** (5,895 मी, तंजानिया) एक शांत ज्वालामुखी पर्वत है। उत्तर-पश्चिम में **एटलस पर्वत** (मोरक्को, अल्जीरिया) और दक्षिण में **ड्रैकेन्सबर्ग पर्वत** स्थित हैं।</li>
          <li><strong>नदियाँ:</strong> 
            <ul>
              <li>**नील नदी:** विश्व की सबसे लंबी नदी, जो **विक्टोरिया झील** से निकलती है और उत्तर की ओर बहती हुई भूमध्य सागर में गिरती है।</li>
              <li>**कांगो (जायरे) नदी:** जल अपवाह में अफ्रीका की सबसे बड़ी नदी; **भूमध्य रेखा को दो बार पार करती है**।</li>
              <li>**लिम्पोपो नदी:** दक्षिणी अफ्रीका में बहती है; **मकर रेखा को दो बार पार करती है**।</li>
              <li>**जाम्बेजी नदी:** इस पर प्रसिद्ध **विक्टोरिया जलप्रपात** और करिबा बांध स्थित हैं।</li>
            </ul>
          </li>
          <li><strong>भ्रंश घाटी और मरुस्थल:</strong> **सहारा मरुस्थल** (सबसे बड़ा गर्म मरुस्थल), **कालाहारी** और **नामिब** मरुस्थल। यहाँ **महान भ्रंश घाटी (Great Rift Valley)** स्थित है जिसमें तांगानिका, मलावी जैसी गहरी झीलें हैं (ध्यान दें: विक्टोरिया झील भ्रंश घाटी का हिस्सा नहीं है)।</li>
        </ul>

        <h3>C. उत्तरी अमेरिका</h3>
        <ul>
          <li><strong>पर्वत श्रृंखलाएं:</strong> **रॉकी पर्वत** (पश्चिम) और **अप्पलाचियन पर्वत** (पूर्व, प्राचीन पर्वत, सबसे ऊंची चोटी: **माउंट मिशेल**, 2,037 मी)। महाद्वीप का सर्वोच्च शिखर **डेनाली** (माउंट मैककिनले, 6,190 मी) अलास्का में है।</li>
          <li><strong>महान झीलें (Great Lakes):</strong> 5 झीलों की श्रृंखला: **सुपीरियर** (क्षेत्रफल में सबसे बड़ी मीठे पानी की झील), **मिशिगन** (एकमात्र ऐसी महान झील जो **पूरी तरह से अमेरिका में स्थित है**), **ह्यूरन**, **इरी** और **ओंटारियो**।</li>
          <li><strong>नदियाँ:</strong> **मिसिसिपी-मिसौरी** नदी तंत्र (पक्षी-पाद डेल्टा बनाता है), **कोलोराडो नदी** (ग्रैंड कैन्यन का निर्माण करती है)।</li>
          <li><strong>न्यूनतम बिंदु:</strong> **डेथ वैली** (मृत घाटी, -86 मी) कैलिफोर्निया में मोजावे मरुस्थल में स्थित है।</li>
        </ul>

        <h3>D. दक्षिणी अमेरिका</h3>
        <ul>
          <li><strong>पर्वत और शिखर:</strong> **एंडीज पर्वत श्रृंखला** (विश्व की सबसे लंबी महाद्वीपीय पर्वत श्रृंखला, 7,000 किमी से अधिक)। सर्वोच्च शिखर **माउंट अकोंकागुआ** (6,961 मी, अर्जेंटीना) है।</li>
          <li><strong>नदियाँ:</strong> **अमेज़न नदी** (अपवाह क्षेत्र और जल आयतन में विश्व की सबसे बड़ी नदी)। **ओरिनोको नदी** (जिसकी सहायक नदी पर विश्व का सबसे ऊंचा जलप्रपात एंजेल प्रपात स्थित है)।</li>
          <li><strong>झीलें और मरुस्थल:</strong> **टिटिकाका झील** (विश्व की सबसे ऊंची नौगम्य झील, पेरू-बोलीविया सीमा)। **अटाकामा मरुस्थल** (विश्व का सबसे शुष्क मरुस्थल, चिली में, ठंडी पेरू धारा के प्रभाव से निर्मित)। **पैटागोनिया मरुस्थल** (शीतोष्ण मरुस्थल, अर्जेंटीना)।</li>
          <li><strong>घास के मैदान:</strong> **पम्पास** (अर्जेंटीना के उपजाऊ शीतोष्ण घास के मैदान) और **लानोस** (वेनेजुएला के उष्णकटिबंधीय घास के मैदान)।</li>
        </ul>

        <h3>E. यूरोप</h3>
        <ul>
          <li><strong>भौगोलिक सीमा:</strong> एशिया से **यूराल पर्वत**, **काकेशस पर्वत** और **कैस्पियन सागर** द्वारा अलग होता है। यूरोप में **एक भी मरुस्थल नहीं पाया जाता है**।</li>
          <li><strong>पर्वत और चोटियाँ:</strong> **माउंट एल्ब्रस** (5,642 मी) यूरोप की सबसे ऊंची चोटी है जो काकेशस श्रेणी में स्थित है। **आल्प्स पर्वत श्रृंखला** (सर्वोच्च चोटी: **माउंट ब्लांक**, 4,810 मी), **पायरेनीस पर्वत** (फ्रांस-स्पेन सीमा)।</li>
          <li><strong>नदियाँ:</strong> **वोल्गा नदी** (यूरोप की सबसे लंबी नदी, कैस्पियन सागर में गिरती है)। **डेन्यूब नदी** (यूरोप की दूसरी सबसे लंबी नदी, जो 4 देशों की राजधानियों से होकर गुजरती है और काला सागर में गिरती है)। **राइन नदी** (सबसे व्यस्त व्यापारिक नदी)।</li>
        </ul>

        <h3>F. ऑस्ट्रेलिया / ओशिनिया</h3>
        <ul>
          <li><strong>धरातल:</strong> सबसे छोटा और सबसे समतल महाद्वीप। यहाँ पूर्व में उत्तर से दक्षिण तक फैली **ग्रेट डिवाइडिंग रेंज** स्थित है। सर्वोच्च शिखर **माउंट कोसिअस्को** (2,228 मी) है। मुख्य नदी तंत्र **मरे-डार्लिंग** है।</li>
          <li><strong>मरुस्थल और झीलें:</strong> इसे प्यासी भूमि का देश भी कहते हैं। प्रमुख मरुस्थल: **ग्रेट सैंडी**, **गिब्सन**, **ग्रेट विक्टोरिया** और **सिम्पसन**। **आयर झील** सबसे निचला बिंदु (-15 मी) है। पूर्वोत्तर तट पर विश्व की सबसे बड़ी मूंगे की चट्टान **ग्रेट बैरियर रीफ** स्थित है।</li>
          <li><strong>घास के मैदान:</strong> **डाउंस** (शीतोष्ण घास के मैदान)।</li>
        </ul>

        <h3>G. अंटार्कटिका</h3>
        <ul>
          <li><strong>भौगोलिक विशेषताएं:</strong> पाँचवाँ सबसे बड़ा महाद्वीप, पूरी तरह बर्फ से ढका है (औसत मोटाई 1.9 किमी)। सर्वोच्च शिखर **विंसन मैसिफ** (4,892 मी) है। पृथ्वी का सबसे दक्षिणी सक्रिय ज्वालामुखी **माउंट इरेबस** यहीं स्थित है।</li>
          <li><strong>भारतीय अंटार्कटिक कार्यक्रम:</strong> भारत ने यहाँ तीन अनुसंधान केंद्र स्थापित किए हैं:
            <ul>
              <li>**दक्षिण गंगोत्री** (1983) - भारत का पहला स्टेशन, जो अब बर्फ में दबकर निष्क्रिय हो चुका है।</li>
              <li>**मैत्री** (1989) - दूसरा सक्रिय अनुसंधान स्टेशन।</li>
              <li>**भारती** (2012) - तीसरा और अत्याधुनिक सक्रिय स्टेशन।</li>
            </ul>
          </li>
        </ul>"""
    },
    {
        "title": "2. पांच महासागर: प्रोफ़ाइल, गर्त और सीमांत सागर",
        "content": """<p>महासागर पृथ्वी की सतह के लगभग 70.8% भाग को कवर करते हैं। पाँचों महासागरों का तुलनात्मक विश्लेषण इस प्रकार है:</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>महासागर</th>
                <th>आकार रैंक</th>
                <th>सबसे गहरा गर्त (Trench)</th>
                <th>प्रमुख धाराएँ और सीमांत सागर</th>
                <th>विशिष्टताएँ</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>प्रशांत महासागर</strong></td>
                <td>1 (सबसे बड़ा)</td>
                <td>मारियाना गर्त (चैलेंजर डीप, 10,994 मी)</td>
                <td>क्यूरोशियो (गर्म), ओयाशियो (ठंडी), पेरू/हम्बोल्ट (ठंडी)। सीमांत सागर: दक्षिण चीन सागर, कोरल सागर, जापान सागर।</td>
                <td>पृथ्वी की सतह के 30% से अधिक भाग पर फैला है। इसके किनारों पर भूकंपीय पेटी 'रिंग ऑफ फायर' स्थित है। आकार लगभग गोलाकार है।</td>
              </tr>
              <tr>
                <td><strong>अटलांटिक महासागर</strong></td>
                <td>2</td>
                <td>प्यूर्टो रिको गर्त (मिल्वौकी डीप, 8,376 मी)</td>
                <td>गल्फ स्ट्रीम (गर्म), लैब्राडोर (ठंडी), कनारी (ठंडी)। सीमांत सागर: कैरेबियन सागर, भूमध्य सागर, उत्तर सागर।</td>
                <td>अंग्रेजी के 'S' आकार का है। व्यापार की दृष्टि से सबसे व्यस्त महासागर। इसमें तटहीन **सारगासो सागर** और समृद्ध मत्स्य क्षेत्र **ग्रैंड बैंक** (गर्म और ठंडी धाराओं का मिलन स्थल) स्थित हैं।</td>
              </tr>
              <tr>
                <td><strong>हिंद महासागर</strong></td>
                <td>3</td>
                <td>सुंडा / जावा गर्त (7,290 मी)</td>
                <td>अगुलहास (गर्म), पश्चिम ऑस्ट्रेलियाई (ठंडी)। सीमांत सागर: लाल सागर, अरब सागर, अंडमान सागर।</td>
                <td>एकमात्र महासागर जिसका नाम किसी देश के नाम पर है। उत्तर में भू-आबद्ध होने के कारण इसे 'अर्ध महासागर' कहते हैं। प्रमुख द्वीप: मेडागास्कर, डिएगो गार्सिया।</td>
              </tr>
              <tr>
                <td><strong>दक्षिणी महासागर</strong></td>
                <td>4</td>
                <td>साउथ सैंडविच गर्त (फैक्टोरियन डीप, 7,434 मी)</td>
                <td>अंटार्कटिक ध्रुवीय प्रवाह (विश्व की सबसे शक्तिशाली जलधारा)।</td>
                <td>अंटार्कटिका महाद्वीप को 60° दक्षिणी अक्षांश तक घेरता है। तीनों प्रमुख महासागरों के मिलने से बनता है। अत्यधिक ठंडा और पोषक तत्वों से भरपूर है।</td>
              </tr>
              <tr>
                <td><strong>आर्कटिक महासागर</strong></td>
                <td>5 (सबसे छोटा)</td>
                <td>फ्रैम बेसिन (यूरेशियाई बेसिन, 5,550 मी)</td>
                <td>ट्रांसपोलर ड्रिफ्ट। सीमांत सागर: बैरेंट्स सागर, ब्यूफोर्ट सागर।</td>
                <td>उत्तरी ध्रुव के चारों ओर स्थित सबसे छोटा और उथला महासागर। प्रशांत महासागर से बेरिंग जलसंधि द्वारा जुड़ा है। अधिकांश समय बर्फ से ढका रहता है।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. महासागरीय नितल के उच्चावच (Ocean Bottom Relief)",
        "content": """<p>महासागरीय नितल में स्थलीय उच्चावच की भांति विभिन्न राहत क्षेत्र पाए जाते हैं:</p>
        <ul>
          <li><strong>महाद्वीपीय मग्नतट (Continental Shelf):</strong> महाद्वीपीय खंड का जलमग्न हिस्सा (औसत ढाल 1°)। इसकी गहराई आमतौर पर 200 मीटर तक होती है। विश्व का सबसे चौड़ा मग्नतट आर्कटिक महासागर का साइबेरियाई मग्नतट है। **यहाँ विश्व के लगभग 20% पेट्रोलियम और प्राकृतिक गैस के भंडार पाए जाते हैं**।</li>
          <li><strong>महाद्वीपीय ढाल (Continental Slope):</strong> मग्नतट और गहरे नितल के बीच का तीव्र ढाल वाला क्षेत्र (2° से 5°)। यहाँ जलमग्न **महासागरीय कंदराएँ (Submarine Canyons)** पाई जाती हैं।</li>
          <li><strong>महाद्वीपीय उत्थान (Continental Rise):</strong> ढाल के आधार पर मलबे के जमाव से निर्मित मंद ढाल (0.5° से 1°) वाला क्षेत्र।</li>
          <li><strong>गहन सागरीय मैदान (Abyssal Plains):</strong> 3,000 से 6,000 मीटर की गहराई पर फैले विस्तृत समतल मैदान। ये कुल नितल का 40% भाग कवर करते हैं। इनमें गुयोट (सपाट शीर्ष वाले जलमग्न पर्वत) और सीमाउंट पाए जाते हैं।</li>
          <li><strong>महासागरीय गर्त (Trenches):</strong> प्लेट सीमाओं (अभिसरण क्षेत्रों) पर स्थित संकीर्ण और गहरे गड्ढे। ये भूकंपीय रूप से सक्रिय होते हैं और ढाल तीव्र होने के कारण यहाँ अवसादों का अभाव होता है।</li>
        </ul>"""
    },
    {
        "title": "4. महाद्वीपीय विस्थापन और प्लेट विवर्तनिकी",
        "content": """<p>महाद्वीपों और महासागरों की वर्तमान स्थिति को स्पष्ट करने वाले दो मुख्य सिद्धांत निम्नलिखित हैं:</p>
        
        <h3>A. महाद्वीपीय विस्थापन सिद्धांत (अल्फ्रेड वेगनर, 1912)</h3>
        <ul>
          <li>इन्होंने बताया कि कार्बोनिफेरस काल में सभी महाद्वीप एक एकल भूखंड के रूप में जुड़े थे जिसे **पैंजिया** (Pangaea) कहा गया, जो **पैंथालसा** (Panthalassa) नामक विशाल महासागर से घिरा था।</li>
          <li>पैंजिया बाद में दो भागों में बंटा: उत्तरी भाग **लॉरेशिया** (या अंगारालैंड) और दक्षिणी भाग **गोंडवानालैंड**। इनके बीच में **टेथिस सागर** का जन्म हुआ।</li>
          <li>**विस्थापन के प्रमाण:** दक्षिणी अमेरिका और अफ्रीका की तटरेखाओं का आपस में मेल खाना (जिग-सॉ फिट), चट्टानों की आयु में समानता, जीवाश्म वितरण (जैसे *Glossopteris* वनस्पति और *Mesosaurus* सरीसृप) और हिमानी जमाव (Tillite)।</li>
        </ul>

        <h3>B. प्लेट विवर्तनिकी सिद्धांत (Plate Tectonics Theory, 1960 के दशक)</h3>
        <ul>
          <li>हैरी हेस के **सागरीय नितल प्रसरण** विचार पर आधारित इस सिद्धांत का प्रतिपादन मैकेंज़ी, पार्कर और मॉर्गन ने किया। इसके अनुसार पृथ्वी का स्थलमंडल 7 मुख्य और कई छोटी कठोर प्लेटों में विभाजित है जो दुर्बलतामंडल (Asthenosphere) पर तैर रही हैं।</li>
          <li><strong>7 मुख्य प्लेटें:</strong> 1. प्रशांत प्लेट (सबसे बड़ी, महासागरीय), 2. उत्तरी अमेरिकी प्लेट, 3. दक्षिणी अमेरिकी प्लेट, 4. यूरेशियाई प्लेट, 5. अफ्रीकी प्लेट, 6. भारत-ऑस्ट्रेलियाई प्लेट, 7. अंटार्कटिका प्लेट।</li>
          <li><strong>प्रमुख लघु प्लेटें:</strong> **नाज़का प्लेट** (दक्षिणी अमेरिका और प्रशांत प्लेट के बीच), **कोकोस प्लेट** (मध्य अमेरिका के पास), **अरेबियन प्लेट**, **फिलीपीन प्लेट** और **कैरेबियन प्लेट**।</li>
          <li><strong>प्लेट सीमाएं:</strong>
            <ul>
              <li>**अपसारी सीमा (Divergent):** प्लेटें एक-दूसरे से दूर जाती हैं जिससे नया क्रस्ट बनता है (जैसे: मध्य-अटलांटिक कटक)।</li>
              <li>**अभिसारी सीमा (Convergent):** प्लेटें टकराती हैं, जिससे वलित पर्वतों और गर्तों का निर्माण होता है (जैसे: हिमालय, मारियाना गर्त)।</li>
              <li>**रूपांतर सीमा (Transform):** प्लेटें एक-दूसरे के समानांतर फिसलती हैं, क्रस्ट का न तो निर्माण होता है न विनाश (जैसे: सैन एंड्रियास भ्रंश)।</li>
            </ul>
          </li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Which of the following is the correct order of continents by land area in descending order?",
        "q_hi": "भौगोलिक क्षेत्रफल के अनुसार निम्नलिखित महाद्वीपों का सही अवरोही क्रम (घटता क्रम) कौन सा है?",
        "opts": [
            "Asia - Africa - South America - North America - Antarctica",
            "Asia - Africa - North America - South America - Antarctica",
            "Asia - North America - Africa - South America - Europe",
            "Asia - Africa - South America - Antarctica - North America"
        ],
        "opts_hi": [
            "एशिया - अफ्रीका - दक्षिणी अमेरिका - उत्तरी अमेरिका - अंटार्कटिका",
            "एशिया - अफ्रीका - उत्तरी अमेरिका - दक्षिणी अमेरिका - अंटार्कटिका",
            "एशिया - उत्तरी अमेरिका - अफ्रीका - दक्षिणी अमेरिका - यूरोप",
            "एशिया - अफ्रीका - दक्षिणी अमेरिका - अंटार्कटिका - उत्तरी अमेरिका"
        ],
        "ans": 1,
        "sol": "The correct descending order of continents by land area is: Asia (1st) > Africa (2nd) > North America (3rd) > South America (4th) > Antarctica (5th) > Europe (6th) > Australia (7th).",
        "sol_hi": "भौगोलिक क्षेत्रफल के अनुसार महाद्वीपों का सही अवरोही क्रम इस प्रकार है: एशिया (पहला) > अफ्रीका (दूसरा) > उत्तरी अमेरिका (तीसरा) > दक्षिणी अमेरिका (चौथा) > अंटार्कटिका (पांचवां) > यूरोप (छठा) > ऑस्ट्रेलिया (सातवां)।"
    },
    {
        "q": "Which ocean has the 'Ring of Fire', characterized by active volcanoes and frequent earthquakes, surrounding its basin?",
        "q_hi": "किस महासागर के बेसिन के चारों ओर सक्रिय ज्वालामुखियों और भूकंपीय गतिविधियों वाला क्षेत्र 'रिंग ऑफ फायर' स्थित है?",
        "opts": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "opts_hi": ["अटलांटिक महासागर", "हिंद महासागर", "प्रशांत महासागर", "आर्कटिक महासागर"],
        "ans": 2,
        "sol": "The Pacific Ring of Fire is a major area in the basin of the Pacific Ocean where many earthquakes and volcanic eruptions occur.",
        "sol_hi": "प्रशांत महासागर के बेसिन के चारों ओर स्थित एक विशाल ज्वालामुखीय एवं भूकंपीय पेटी को 'रिंग ऑफ फायर' (अग्नि वलय) कहा जाता है।"
    },
    {
        "q": "Which is the highest mountain peak in the continent of Europe?",
        "q_hi": "यूरोप महाद्वीप का सर्वोच्च पर्वत शिखर कौन सा है?",
        "opts": ["Mount Blanc", "Mount Elbrus", "Mount Kilimanjaro", "Mount Kosciuszko"],
        "opts_hi": ["माउंट ब्लांक", "माउंट एल्ब्रस", "माउंट किलिमंजारो", "माउंट कोसिअस्को"],
        "ans": 1,
        "sol": "Mount Elbrus (5,642 meters) located in the Caucasus Mountains in Russia is the highest peak in Europe.",
        "sol_hi": "रूस में काकेशस पर्वत श्रृंखला में स्थित माउंट एल्ब्रस (5,642 मीटर) यूरोप महाद्वीप का सर्वोच्च पर्वत शिखर है।"
    },
    {
        "q": "Which ocean is S-shaped and has the Mid-Atlantic Ridge running through its center?",
        "q_hi": "कौन सा महासागर अंग्रेजी के 'S' आकार का है जिसके मध्य में मध्य-अटलांटिक कटक स्थित है?",
        "opts": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Southern Ocean"],
        "opts_hi": ["हिंद महासागर", "प्रशांत महासागर", "अटलांटिक महासागर", "दक्षिणी महासागर"],
        "ans": 2,
        "sol": "The Atlantic Ocean is S-shaped. Its central relief feature is the Mid-Atlantic Ridge, a giant underwater mountain range.",
        "sol_hi": "अटलांटिक महासागर (अंध महासागर) अंग्रेजी के S आकार का है। इसके मध्य में उत्तर से दक्षिण तक फैली एक विशाल पर्वत श्रेणी को मध्य-अटलांटिक कटक कहा जाता है।"
    },
    {
        "q": "Which continent is crossed by all three major latitude lines: Equator, Tropic of Cancer, and Tropic of Capricorn?",
        "q_hi": "किस महाद्वीप से तीनों प्रमुख अक्षांश रेखाएँ: भूमध्य रेखा, कर्क रेखा और मकर रेखा गुजरती हैं?",
        "opts": ["Asia", "South America", "Africa", "Australia"],
        "opts_hi": ["एशिया", "दक्षिणी अमेरिका", "अफ्रीका", "ऑस्ट्रेलिया"],
        "ans": 2,
        "sol": "Africa is the only continent that is intersected by the Equator, the Tropic of Cancer, and the Tropic of Capricorn.",
        "sol_hi": "अफ्रीका विश्व का एकमात्र ऐसा महाद्वीप है जिससे कर्क रेखा, मकर रेखा और भूमध्य रेखा (विषुवत रेखा) तीनों गुजरती हैं।"
    },
    {
        "q": "Which of the following is the deepest point in the Indian Ocean?",
        "q_hi": "निम्नलिखित में से कौन सा हिंद महासागर का सबसे गहरा बिंदु (गर्त) है?",
        "opts": ["Mariana Trench", "Puerto Rico Trench", "Sunda (Java) Trench", "South Sandwich Trench"],
        "opts_hi": ["मारियाना गर्त", "प्यूर्टो रिको गर्त", "सुंडा (जावा) गर्त", "साउथ सैंडविच गर्त"],
        "ans": 2,
        "sol": "The Sunda Trench, formerly known as the Java Trench, is the deepest trench in the Indian Ocean, reaching depths of around 7,290 meters.",
        "sol_hi": "जावा या सुंडा गर्त हिंद महासागर का सबसे गहरा बिंदु है, जिसकी गहराई लगभग 7,290 मीटर है।"
    },
    {
        "q": "In which continent is the longest mountain range in the world, the Andes, located?",
        "q_hi": "विश्व की सबसे लंबी पर्वत श्रृंखला 'एंडीज' (Andes) किस महाद्वीप में स्थित है?",
        "opts": ["North America", "South America", "Asia", "Europe"],
        "opts_hi": ["उत्तरी अमेरिका", "दक्षिणी अमेरिका", "एशिया", "यूरोप"],
        "ans": 1,
        "sol": "The Andes is the longest continental mountain range in the world, running along the western coast of South America.",
        "sol_hi": "एंडीज पर्वत श्रृंखला विश्व की सबसे लंबी महाद्वीपीय पर्वत श्रृंखला है जो दक्षिणी अमेरिका के पश्चिमी तट के समानांतर विस्तृत है।"
    },
    {
        "q": "Which strait connects the Pacific Ocean to the Arctic Ocean?",
        "q_hi": "कौन सी जलसंधि (Strait) प्रशांत महासागर को आर्कटिक महासागर से जोड़ती है?",
        "opts": ["Gibraltar Strait", "Bering Strait", "Malacca Strait", "Strait of Magellan"],
        "opts_hi": ["जिब्राल्टर जलसंधि", "बेरिंग जलसंधि", "मलक्का जलसंधि", "मैगलन जलसंधि"],
        "ans": 1,
        "sol": "The Bering Strait connects the Pacific Ocean (Bering Sea) to the Arctic Ocean (Chukchi Sea).",
        "sol_hi": "बेरिंग जलसंधि उत्तरी प्रशांत महासागर (बेरिंग सागर) को आर्कटिक महासागर (चुक्ची सागर) से जोड़ती है।"
    },
    {
        "q": "Which continent has no desert?",
        "q_hi": "निम्नलिखित में से किस महाद्वीप में एक भी मरुस्थल (Desert) नहीं पाया जाता है?",
        "opts": ["Europe", "Australia", "North America", "South America"],
        "opts_hi": ["यूरोप", "ऑस्ट्रेलिया", "उत्तरी अमेरिका", "दक्षिणी अमेरिका"],
        "ans": 0,
        "sol": "Europe is the only continent that has no major deserts, owing to its geographical position and ocean current influences.",
        "sol_hi": "यूरोप विश्व का एकमात्र ऐसा महाद्वीप है जिसमें कोई विस्तृत रेगिस्तान या मरुस्थल नहीं पाया जाता है।"
    },
    {
        "q": "Which continent is known as the 'Continent of Science' or 'White Continent'?",
        "q_hi": "किस महाद्वीप को 'विज्ञान के लिए समर्पित महाद्वीप' या 'श्वेत महाद्वीप' कहा जाता है?",
        "opts": ["Antarctica", "Asia", "Europe", "North America"],
        "opts_hi": ["अटलांतिक", "एशिया", "यूरोप", "उत्तरी अमेरिका"], # corrected typo in translation
        "opts_hi": ["अंटार्कटिका", "एशिया", "यूरोप", "उत्तरी अमेरिका"],
        "ans": 0,
        "sol": "Antarctica is called the 'White Continent' because it is covered in ice year-round, and the 'Continent of Science' because it is used strictly for scientific research.",
        "sol_hi": "अंटार्कटिका महाद्वीप वर्ष भर बर्फ की चादर से ढके रहने के कारण 'श्वेत महाद्वीप' कहलाता है, तथा यहाँ वैश्विक वैज्ञानिकों द्वारा केवल शोध किए जाने के कारण इसे 'विज्ञान के लिए समर्पित महाद्वीप' कहते हैं।"
    },
    {
        "q": "Consider the following statements:\n1. The Southern Ocean completely surrounds the continent of Antarctica.\n2. In 2000, the International Hydrographic Organization officially defined the Southern Ocean limit at 60°S latitude.\nWhich of the statements given above is/are correct?",
        "q_hi": "निम्नलिखित कथनों पर विचार करें:\n1. दक्षिणी महासागर पूरी तरह से अंटार्कटिका महाद्वीप को घेरता है।\n2. वर्ष 2000 में, अंतर्राष्ट्रीय जल सर्वेक्षण संगठन ने आधिकारिक तौर पर दक्षिणी महासागर की उत्तरी सीमा 60° दक्षिणी अक्षांश निर्धारित की।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "Both statements are correct. The Southern Ocean encircles Antarctica and its boundary was defined south of 60°S by the IHO.",
        "sol_hi": "दोनों कथन सही हैं। दक्षिणी महासागर अंटार्कटिका महाद्वीप को पूरी तरह घेरे हुए है और IHO ने 2000 में इसकी उत्तरी सीमा 60° दक्षिणी अक्षांश तय की थी।"
    },
    {
        "q": "Which island is the largest island in the world, and to which continent does it belong geographically?",
        "q_hi": "विश्व का सबसे बड़ा द्वीप कौन सा है, और यह भौगोलिक रूप से किस महाद्वीप का हिस्सा है?",
        "opts": ["Madagascar - Africa", "Greenland - North America", "Sumatra - Asia", "Great Britain - Europe"],
        "opts_hi": ["मेडागास्कर - अफ्रीका", "ग्रीनलैंड - उत्तरी अमेरिका", "सुमात्रा - एशिया", "ग्रेट ब्रिटेन - यूरोप"],
        "ans": 1,
        "sol": "Greenland is the world's largest island. Geographically, it is part of the North American continent, although politically it is an autonomous territory of Denmark (Europe).",
        "sol_hi": "ग्रीनलैंड विश्व का सबसे बड़ा द्वीप है। यह भौगोलिक रूप से उत्तरी अमेरिका का हिस्सा है, लेकिन राजनीतिक तौर पर डेनमार्क (यूरोप) के नियंत्रण में है।"
    },
    {
        "q": "Which continent has the lowest point on land, the Dead Sea, which is about 430 meters below sea level?",
        "q_hi": "पृथ्वी का सबसे निचला भू-भाग 'मृत सागर' (Dead Sea, -430 मीटर) किस महाद्वीप में स्थित है?",
        "opts": ["Africa", "Asia", "Europe", "Australia"],
        "opts_hi": ["अफ्रीका", "एशिया", "यूरोप", "ऑस्ट्रेलिया"],
        "ans": 1,
        "sol": "The Dead Sea, the lowest land point on Earth (-430 meters), is located in Asia (on the border of Israel, Palestine, and Jordan).",
        "sol_hi": "मृत सागर (समुद्र तल से लगभग 430 मीटर नीचे) एशिया महाद्वीप में इसराइल, फिलिस्तीन और जॉर्डन की सीमा पर स्थित है।"
    },
    {
        "q": "What is the name of the deepest point of the Atlantic Ocean?",
        "q_hi": "अटलांटिक महासागर के सबसे गहरे बिंदु का नाम क्या है?",
        "opts": ["Mariana Trench", "Puerto Rico Trench (Milwaukee Deep)", "Sunda Trench", "Kermadec Trench"],
        "opts_hi": ["मारियाना गर्त", "प्यूर्टो रिको गर्त (मिल्वौकी डीप)", "सुंडा गर्त", "केर्माडेक गर्त"],
        "ans": 1,
        "sol": "The Puerto Rico Trench is the deepest trench in the Atlantic Ocean, with a maximum depth of 8,376 meters at the Milwaukee Deep.",
        "sol_hi": "प्यूर्टो रिको गर्त अटलांटिक महासागर का सबसे गहरा गर्त है, जिसके मिल्वौकी डीप की गहराई लगभग 8,376 मीटर है।"
    },
    {
        "q": "Which continent is known as the 'Island Continent'?",
        "q_hi": "निम्नलिखित में से किस महाद्वीप को 'द्वीपीय महाद्वीप' (Island Continent) कहा जाता है?",
        "opts": ["Antarctica", "Australia", "South America", "Europe"],
        "opts_hi": ["अंटार्कटिका", "ऑस्ट्रेलिया", "दक्षिणी अमेरिका", "यूरोप"],
        "ans": 1,
        "sol": "Australia is called the 'Island Continent' because it is surrounded by water on all sides but is large enough to be classified as a continent.",
        "sol_hi": "ऑस्ट्रेलिया को चारों तरफ से महासागरों से घिरे होने और आकार में छोटा होने के कारण 'द्वीपीय महाद्वीप' कहा जाता है।"
    },
    {
        "q": "Who proposed the 'Continental Drift Theory' in 1912 to explain the position of continents and oceans?",
        "q_hi": "महाद्वीपों और महासागरों की स्थिति स्पष्ट करने वाले 'महाद्वीपीय विस्थापन सिद्धांत' का प्रतिपादन 1912 में किसने किया था?",
        "opts": ["Harry Hess", "Alfred Wegener", "Arthur Holmes", "John Tuzo Wilson"],
        "opts_hi": ["हैरी हेस", "अल्फ्रेड वेगनर", "आर्थर होम्स", "जॉन टूजो विल्सन"],
        "ans": 1,
        "sol": "Alfred Wegener, a German meteorologist, proposed the Continental Drift Theory in 1912.",
        "sol_hi": "जर्मन मौसमविद् अल्फ्रेड वेगनर ने वर्ष 1912 में महाद्वीपीय विस्थापन सिद्धांत का प्रतिपादन किया था।"
    },
    {
        "q": "Which is the highest peak in North America?",
        "q_hi": "उत्तरी अमेरिका महाद्वीप का सर्वोच्च पर्वत शिखर कौन सा है?",
        "opts": ["Mount Elbrus", "Mount Aconcagua", "Denali (Mount McKinley)", "Mount Mitchell"],
        "opts_hi": ["माउंट एल्ब्रस", "माउंट अकोंकागुआ", "डेनाली (माउंट मैककिनले)", "माउंट मिशेल"],
        "ans": 2,
        "sol": "Denali (formerly known as Mount McKinley) in Alaska, rising to 6,190 meters, is the highest peak in North America.",
        "sol_hi": "डेनाली (पूर्व नाम: माउंट मैककिनले), जो अलास्का रेंज में स्थित है (6,190 मीटर), उत्तरी अमेरिका का सर्वोच्च शिखर है।"
    },
    {
        "q": "Which continent is known as the 'Continent of Plateaus' because a major part of it is occupied by tablelands?",
        "q_hi": "किस महाद्वीप को 'पठारों का महाद्वीप' कहा जाता है क्योंकि इसका अधिकांश भाग पठारों से घिरा है?",
        "opts": ["Asia", "Africa", "Europe", "South America"],
        "opts_hi": ["एशिया", "अफ्रीका", "यूरोप", "दक्षिणी अमेरिका"],
        "ans": 1,
        "sol": "Africa is often called the 'Continent of Plateaus' because its average elevation is high, consisting of vast tablelands.",
        "sol_hi": "अफ्रीका महाद्वीप को पठारों का महाद्वीप कहा जाता है क्योंकि इसका अधिकांश भाग ऊंचे पठारी भूखंडों से निर्मित है।"
    },
    {
        "q": "Which ocean is bounded by Asia on the west, North and South America on the east, and Antarctica on the south?",
        "q_hi": "कौन सा महासागर पश्चिम में एशिया, पूर्व में उत्तरी और दक्षिणी अमेरिका और दक्षिण में अंटार्कटिका से घिरा हुआ है?",
        "opts": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Southern Ocean"],
        "opts_hi": ["अटलांटिक महासागर", "हिंद महासागर", "प्रशांत महासागर", "दक्षिणी महासागर"],
        "ans": 2,
        "sol": "The Pacific Ocean is bounded by Asia and Australia on the west, and the Americas on the east.",
        "sol_hi": "प्रशांत महासागर पश्चिम में एशिया और ऑस्ट्रेलिया तथा पूर्व में उत्तरी एवं दक्षिणी अमेरिका से घिरा हुआ विश्व का सबसे बड़ा महासागर है।"
    },
    {
        "q": "What is the highest mountain peak in the continent of South America?",
        "q_hi": "दक्षिणी अमेरिका महाद्वीप का सर्वोच्च पर्वत शिखर कौन सा है?",
        "opts": ["Mount Aconcagua", "Mount Chimborazo", "Mount Cotopaxi", "Mount Mitchell"],
        "opts_hi": ["माउंट अकोंकागुआ", "माउंट चिम्बोरैजो", "माउंट कोटोपैक्सी", "माउंट मिशेल"],
        "ans": 0,
        "sol": "Mount Aconcagua (6,961 meters) in the Andes range in Argentina is the highest peak in South America.",
        "sol_hi": "माउंट अकोंकागुआ (6,961 मीटर) एंडीज पर्वत श्रेणी में अर्जेंटीना में स्थित दक्षिणी अमेरिका का सबसे ऊंचा पर्वत शिखर है।"
    },
    {
        "q": "What percentage of the Earth's surface is covered by oceans?",
        "q_hi": "पृथ्वी के धरातल का लगभग कितना प्रतिशत भाग महासागरों से आच्छादित है?",
        "opts": ["29%", "50%", "71%", "80%"],
        "opts_hi": ["29%", "50%", "71%", "80%"],
        "ans": 2,
        "sol": "Oceans cover approximately 70.8% (commonly rounded to 71%) of the Earth's surface, while land covers about 29%.",
        "sol_hi": "पृथ्वी की सतह का लगभग 71% भाग जल (महासागरों) से ढका हुआ है और 29% भाग थल (स्थल) है।"
    },
    {
        "q": "Which is the highest peak in Africa, and in which country is it located?",
        "q_hi": "अफ्रीका महाद्वीप का सर्वोच्च शिखर कौन सा है, और यह किस देश में स्थित है?",
        "opts": ["Mount Kenya - Kenya", "Mount Kilimanjaro - Tanzania", "Mount Stanley - Uganda", "Ras Dashen - Ethiopia"],
        "opts_hi": ["माउंट केन्या - केन्या", "माउंट किलिमंजारो - तंजानिया", "माउंट स्टेनली - युगांडा", "रास दाशेन - इथियोपिया"],
        "ans": 1,
        "sol": "Mount Kilimanjaro (5,895m) is the highest peak in Africa, situated in Tanzania. It is a dormant stratovolcano.",
        "sol_hi": "माउंट किलिमंजारो (5,895 मीटर) अफ्रीका का सबसे ऊंचा शिखर है जो तंजानिया में स्थित एक शांत ज्वालामुखी पर्वत है।"
    },
    {
        "q": "Which is the smallest ocean in the world?",
        "q_hi": "विश्व का सबसे छोटा महासागर कौन सा है?",
        "opts": ["Indian Ocean", "Southern Ocean", "Arctic Ocean", "Atlantic Ocean"],
        "opts_hi": ["हिंद महासागर", "दक्षिणी महासागर", "आर्कटिक महासागर", "अटलांटिक महासागर"],
        "ans": 2,
        "sol": "The Arctic Ocean is the smallest, shallowest, and coldest of the world's five major oceans.",
        "sol_hi": "आर्कटिक महासागर विश्व का सबसे छोटा, सबसे ठंडा और सबसे उथला महासागर है।"
    },
    {
        "q": "Which continent is also known as the 'Continent of Extremes' due to its diverse climates, physical reliefs, and cultures?",
        "q_hi": "भौतिक विविधताओं, विशाल जलवायु और विविध संस्कृतियों के कारण किस महाद्वीप को 'विषमताओं का महाद्वीप' कहा जाता है?",
        "opts": ["Africa", "Asia", "South America", "Europe"],
        "opts_hi": ["अफ्रीका", "एशिया", "दक्षिणी अमेरिका", "यूरोप"],
        "ans": 1,
        "sol": "Asia is known as the 'Continent of Extremes' because it features the highest point (Mount Everest) and the lowest point (Dead Sea), as well as extreme climatic variations.",
        "sol_hi": "एशिया महाद्वीप को 'विषमताओं का महाद्वीप' कहा जाता है क्योंकि यहाँ दुनिया का सबसे ऊंचा शिखर (एवरेस्ट) और सबसे नीचा बिंदु (मृत सागर) तथा अत्यधिक विविध जलवायु पाई जाती है।"
    },
    {
        "q": "Which lake has the highest salinity in the world?",
        "q_hi": "विश्व में सर्वाधिक लवणता वाली झील कौन सी है?",
        "opts": ["Dead Sea", "Lake Van (Turkey)", "Great Salt Lake", "Lake Baikal"],
        "opts_hi": ["मृत सागर", "वॉन झील (तुर्की)", "ग्रेट साल्ट लेक", "बैकाल झील"],
        "ans": 1,
        "sol": "Lake Van in Turkey has the highest salinity (about 330‰) among major saline lakes (excluding hyper-saline ponds in Antarctica).",
        "sol_hi": "तुर्की की वॉन झील (Lake Van) में सर्वाधिक लवणता (लगभग 330‰) पाई जाती है।"
    },
    {
        "q": "The Suez Canal connects which two water bodies?",
        "q_hi": "स्वेज नहर (Suez Canal) किन दो जल निकायों को आपस में जोड़ती है?",
        "opts": [
            "Mediterranean Sea and Red Sea",
            "Mediterranean Sea and Black Sea",
            "Red Sea and Arabian Sea",
            "Atlantic Ocean and Mediterranean Sea"
        ],
        "opts_hi": [
            "भूमध्य सागर और लाल सागर",
            "भूमध्य सागर और काला सागर",
            "लाल सागर और अरब सागर",
            "अटलांटिक महासागर और भूमध्य सागर"
        ],
        "ans": 0,
        "sol": "The Suez Canal is an artificial sea-level waterway in Egypt connecting the Mediterranean Sea to the Red Sea.",
        "sol_hi": "मिस्र में स्थित स्वेज नहर भूमध्य सागर को लाल सागर से जोड़ती है, जो यूरेशिया और अफ्रीका के व्यापारिक मार्गों को छोटा करती है।"
    },
    {
        "q": "Which is the highest peak in the continent of Antarctica?",
        "q_hi": "अंटार्कटिका महाद्वीप का सर्वोच्च पर्वत शिखर कौन सा है?",
        "opts": ["Mount Erebus", "Vinson Massif", "Mount Kosciuszko", "Mount Mitchell"],
        "opts_hi": ["माउंट इरेबस", "विंसन मैसिफ", "माउंट कोसिअस्को", "माउंट मिशेल"],
        "ans": 1,
        "sol": "Vinson Massif (4,892 meters) is the highest mountain peak in Antarctica, situated in the Sentinel Range.",
        "sol_hi": "विंसन मैसिफ (4,892 मीटर) अंटार्कटिका महाद्वीप का सबसे ऊंचा पर्वत शिखर है।"
    },
    {
        "q": "Which ocean has the longest coastline in the world?",
        "q_hi": "विश्व में सबसे लंबी तटरेखा वाला महासागर कौन सा है?",
        "opts": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "opts_hi": ["प्रशांत महासागर", "अटलांटिक महासागर", "हिंद महासागर", "आर्कटिक महासागर"],
        "ans": 1,
        "sol": "The Atlantic Ocean has the longest and most indented coastline due to its highly irregular shape, which makes it ideal for ports.",
        "sol_hi": "कटी-फटी और अनियमित 'S' आकृति के कारण अटलांटिक महासागर की तटरेखा सबसे लंबी और बंदरगाहों के लिए सर्वाधिक उपयुक्त है।"
    },
    {
        "q": "Which is the largest country in South America by land area?",
        "q_hi": "क्षेत्रफल की दृष्टि से दक्षिणी अमेरिका महाद्वीप का सबसे बड़ा देश कौन सा है?",
        "opts": ["Argentina", "Colombia", "Brazil", "Peru"],
        "opts_hi": ["अर्जेंटीना", "कोलंबिया", "ब्राजील", "पेरू"],
        "ans": 2,
        "sol": "Brazil is the largest country in South America by both land area and population.",
        "sol_hi": "ब्राजील दक्षिणी अमेरिका का क्षेत्रफल और जनसंख्या दोनों ही दृष्टि से सबसे बड़ा देश है।"
    },
    {
        "q": "What is the name of the cold ocean current that flows off the western coast of South America?",
        "q_hi": "दक्षिणी अमेरिका के पश्चिमी तट के सहारे बहने वाली ठंडी महासागरीय धारा का क्या नाम है?",
        "opts": ["Gulf Stream", "Humboldt (Peru) Current", "Brazil Current", "Kuroshio Current"],
        "opts_hi": ["गल्फ स्ट्रीम", "हम्बोल्ट (पेरू) धारा", "ब्राजील धारा", "क्यूरोशियो धारा"],
        "ans": 1,
        "sol": "The Humboldt Current, also called the Peru Current, is a cold, low-salinity ocean current that flows north along the western coast of South America.",
        "sol_hi": "पेरू या हम्बोल्ट की धारा एक प्रमुख ठंडी जलधारा है, जो दक्षिणी अमेरिका के पश्चिमी तट के सहारे दक्षिण से उत्तर की ओर प्रवाहित होती है।"
    },
    # --- ADDITIONAL 20 QUESTIONS TO REACH EXACTLY 50 ---
    {
        "q": "Consider the following statements regarding the continents:\n1. Asia is separated from Europe by the Ural Mountains, Caucasus Mountains, and Caspian Sea.\n2. Africa is separated from Europe by the Mediterranean Sea and Strait of Gibraltar.\nWhich of the statements given above is/are correct?",
        "q_hi": "महाद्वीपों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. एशिया यूरेशियाई भूखंड में यूराल पर्वत, काकेशस पर्वत और कैस्पियन सागर द्वारा यूरोप से अलग होता है।\n2. अफ्रीका भूमध्य सागर और जिब्राल्टर जलसंधि द्वारा यूरोप से अलग होता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "Both statements are geographically correct. These land and water bodies form the natural boundaries separating these continents.",
        "sol_hi": "दोनों कथन सही हैं। यूराल, काकेशस और कैस्पियन सागर एशिया और यूरोप की सीमा बनाते हैं, जबकि भूमध्य सागर और जिब्राल्टर अफ्रीका और यूरोप को अलग करते हैं।"
    },
    {
        "q": "Which ocean contains the island of Madagascar, the fourth largest island in the world?",
        "q_hi": "विश्व का चौथा सबसे बड़ा द्वीप 'मेडागास्कर' किस महासागर में स्थित है?",
        "opts": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Southern Ocean"],
        "opts_hi": ["अटलांटिक महासागर", "प्रशांत महासागर", "हिंद महासागर", "दक्षिणी महासागर"],
        "ans": 2,
        "sol": "Madagascar is situated in the Indian Ocean off the southeastern coast of Africa.",
        "sol_hi": "मेडागास्कर द्वीप हिंद महासागर में अफ्रीका के दक्षिण-पूर्वी तट के पास स्थित है।"
    },
    {
        "q": "Which is the highest peak in Australia / Oceania?",
        "q_hi": "ऑस्ट्रेलिया / ओशिनिया महाद्वीप का सर्वोच्च शिखर कौन सा है?",
        "opts": ["Mount Kosciuszko", "Mount Cook (Aoraki)", "Mount Wilhelm", "Mount Vinson"],
        "opts_hi": ["माउंट कोसिअस्को", "माउंट कुक (अओराकी)", "माउंट विल्हेम", "माउंट विंसन"],
        "ans": 0,
        "sol": "Mount Kosciuszko (2,228m) in New South Wales is the highest peak of mainland Australia.",
        "sol_hi": "मुख्य भूमि ऑस्ट्रेलिया का सबसे ऊंचा पर्वत शिखर माउंट कोसिअस्को (2,228 मीटर) है, जो न्यू साउथ वेल्स में स्थित है।"
    },
    {
        "q": "Which sea is located between the northeastern coast of Africa and the Arabian Peninsula?",
        "q_hi": "कौन सा सागर अफ्रीका के उत्तर-पूर्वी तट और अरब प्रायद्वीप के बीच स्थित है?",
        "opts": ["Mediterranean Sea", "Red Sea", "Caspian Sea", "Black Sea"],
        "opts_hi": ["भूमध्य सागर", "लाल सागर", "कैस्पियन सागर", "काला सागर"],
        "ans": 1,
        "sol": "The Red Sea lies between Africa and the Arabian Peninsula. It is connected to the Indian Ocean through the Bab-el-Mandeb strait.",
        "sol_hi": "लाल सागर अफ्रीका और अरब प्रायद्वीप के बीच स्थित है। यह बाब-अल-मंडेब जलसंधि द्वारा हिंद महासागर से जुड़ता है।"
    },
    {
        "q": "Which continent contains the Amazon Rainforest, often referred to as the 'lungs of the planet'?",
        "q_hi": "विश्व के सबसे बड़े वर्षावन 'अमेज़न वर्षावन' किस महाद्वीप में स्थित हैं?",
        "opts": ["Africa", "Asia", "South America", "North America"],
        "opts_hi": ["अफ्रीका", "एशिया", "दक्षिणी अमेरिका", "उत्तरी अमेरिका"],
        "ans": 2,
        "sol": "The Amazon Rainforest is located in South America, covering parts of Brazil, Peru, Colombia, and other nations.",
        "sol_hi": "अमेज़न वर्षावन दक्षिणी अमेरिका महाद्वीप में स्थित हैं, जिसका सर्वाधिक भाग ब्राजील में आता है।"
    },
    {
        "q": "Arrange the following oceans in descending order of their depth:\n1. Pacific Ocean\n2. Atlantic Ocean\n3. Indian Ocean\n4. Arctic Ocean\nSelect the correct code:",
        "q_hi": "निम्नलिखित महासागरों को उनकी औसत गहराई के अनुसार अवरोही क्रम (घटते क्रम) में व्यवस्थित करें:\n1. प्रशांत महासागर\n2. अटलांटिक महासागर\n3. हिंद महासागर\n4. आर्कटिक महासागर\nसही कोड चुनें:",
        "opts": ["1-2-3-4", "1-3-2-4", "2-1-3-4", "1-2-4-3"],
        "opts_hi": ["1-2-3-4", "1-3-2-4", "2-1-3-4", "1-2-4-3"],
        "ans": 1,
        "sol": "By average depth, Pacific is the deepest (~3970m), followed by Indian Ocean (~3741m), then Atlantic Ocean (~3646m), and Arctic is the shallowest. Hence 1-3-2-4 is correct.",
        "sol_hi": "औसत गहराई के अनुसार सही अवरोही क्रम है: प्रशांत महासागर (~3970 मी) > हिंद महासागर (~3741 मी) > अटलांटिक महासागर (~3646 मी) > आर्कटिक महासागर। अतः विकल्प B सही है।"
    },
    {
        "q": "The Mariana Trench, the deepest point on Earth, is located near which island group?",
        "q_hi": "पृथ्वी का सबसे गहरा बिंदु 'मारियाना गर्त' किस द्वीप समूह के निकट स्थित है?",
        "opts": ["Philippine Islands", "Japanese Archipelago", "Hawaiian Islands", "Marshall Islands"],
        "opts_hi": ["फिलिपिंस द्वीप समूह", "जापानी द्वीप समूह", "हवाई द्वीप समूह", "मार्शल द्वीप समूह"],
        "ans": 0,
        "sol": "The Mariana Trench is located in the western Pacific Ocean, just east of the Mariana and Philippine Islands.",
        "sol_hi": "मारियाना गर्त पश्चिमी प्रशांत महासागर में फिलीपींस और मारियाना द्वीपों के पूर्व में स्थित है।"
    },
    {
        "q": "Which continent is characterized by the Great Rift Valley, a giant geological fault line stretching thousands of kilometers?",
        "q_hi": "महान भ्रंश घाटी (Great Rift Valley), जो हजारों किलोमीटर लंबी एक विशाल भूगर्भीय दरार है, किस महाद्वीप की मुख्य विशेषता है?",
        "opts": ["Asia", "Africa", "North America", "South America"],
        "opts_hi": ["एशिया", "अफ्रीका", "उत्तरी अमेरिका", "दक्षिणी अमेरिका"],
        "ans": 1,
        "sol": "The Great Rift Valley is a continuous geographic trench running from Lebanon in Asia to Mozambique in southeastern Africa, but its most prominent and extensive part lies in Africa.",
        "sol_hi": "महान भ्रंश घाटी का मुख्य और सबसे विस्तृत भाग अफ्रीका महाद्वीप में स्थित है, जो लेबनान (एशिया) से शुरू होकर मोज़ाम्बिक तक फैला है।"
    },
    {
        "q": "Which ocean is entirely landlocked from the north and does not open into the Arctic Ocean?",
        "q_hi": "कौन सा महासागर उत्तर दिशा से पूरी तरह भू-आबद्ध (Landlocked) है और आर्कटिक महासागर में नहीं खुलता?",
        "opts": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"],
        "opts_hi": ["प्रशांत महासागर", "अटलांटिक महासागर", "हिंद महासागर", "दक्षिणी महासागर"],
        "ans": 2,
        "sol": "The Indian Ocean is landlocked to the north by the Asian continent and does not connect to the Arctic Ocean, earning it the title of a 'Half Ocean'.",
        "sol_hi": "हिंद महासागर उत्तर में यूरेशियाई भूभाग द्वारा पूरी तरह से आबद्ध है, जिस कारण इसे 'अर्ध महासागर' भी कहा जाता है।"
    },
    {
        "q": "Which is the highest peak in the Appalachian Mountain range in North America?",
        "q_hi": "उत्तरी अमेरिका की अप्पलाचियन (Appalachian) पर्वत श्रृंखला का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Mount Mitchell", "Denali", "Mount Rainier", "Mount Whitney"],
        "opts_hi": ["माउंट मिशेल", "डेनाली", "माउंट रेनियर", "माउंट व्हिटनी"],
        "ans": 0,
        "sol": "Mount Mitchell (2,037 meters) in North Carolina is the highest peak of the Appalachian Mountains.",
        "sol_hi": "माउंट मिशेल (2,037 मीटर) संयुक्त राज्य अमेरिका के उत्तरी कैरोलिना में स्थित अप्पलाचियन श्रेणी का सबसे ऊंचा शिखर है।"
    },
    {
        "q": "Which continent has the highest average elevation above sea level?",
        "q_hi": "किस महाद्वीप की औसत ऊंचाई समुद्र तल से सर्वाधिक है?",
        "opts": ["Asia", "Africa", "Antarctica", "North America"],
        "opts_hi": ["एशिया", "अफ्रीका", "अंटार्कटिका", "उत्तरी अमेरिका"],
        "ans": 2,
        "sol": "Antarctica is the highest continent on Earth in terms of average elevation (about 2,300 meters) due to its massive, thick ice sheet.",
        "sol_hi": "अंटार्कटिका महाद्वीप की औसत ऊंचाई (लगभग 2,300 मीटर) बर्फ की मोटी चादरों के कारण सभी महाद्वीपों में सर्वाधिक है।"
    },
    {
        "q": "Which of the following is the deepest lake in the world, located in Asia?",
        "q_hi": "निम्नलिखित में से कौन सी विश्व की सबसे गहरी झील है, जो एशिया में स्थित है?",
        "opts": ["Lake Superior", "Lake Baikal", "Caspian Sea", "Lake Tanganyika"],
        "opts_hi": ["सुपीरियर झील", "बैकाल झील", "कैस्पियन सागर", "तांगानिका झील"],
        "ans": 1,
        "sol": "Lake Baikal in southern Siberia, Russia (Asia) is the deepest lake in the world with a depth of 1,642 meters.",
        "sol_hi": "रूस के साइबेरिया (एशिया) में स्थित बैकाल झील विश्व की सबसे गहरी (1,642 मीटर) और सबसे बड़ी मीठे पानी की झील (आयतन में) है।"
    },
    {
        "q": "The Drake Passage is a body of water located between which two landmasses?",
        "q_hi": "ड्रेक पैसेज (Drake Passage) किन दो भूखंडों के बीच स्थित एक जलमार्ग है?",
        "opts": [
            "South America and Antarctica",
            "North America and Asia",
            "Africa and Europe",
            "Australia and New Zealand"
        ],
        "opts_hi": [
            "दक्षिणी अमेरिका और अंटार्कटिका",
            "उत्तरी अमेरिका और एशिया",
            "अफ्रीका और यूरोप",
            "ऑस्ट्रेलिया और न्यूजीलैंड"
        ],
        "ans": 0,
        "sol": "The Drake Passage connects the southwestern part of the Atlantic Ocean with the southeastern part of the Pacific Ocean, separating South America from Antarctica.",
        "sol_hi": "ड्रेक पैसेज दक्षिणी अमेरिका के हॉर्न अंतरीप को अंटार्कटिका के शेटलैंड द्वीपों से अलग करने वाला एक अत्यंत अशांत जलमार्ग है।"
    },
    {
        "q": "Which canal connects the Pacific Ocean to the Caribbean Sea (and Atlantic Ocean)?",
        "q_hi": "कौन सी नहर प्रशांत महासागर को कैरेबियन सागर (और अटलांटिक महासागर) से जोड़ती है?",
        "opts": ["Suez Canal", "Kiel Canal", "Panama Canal", "Erie Canal"],
        "opts_hi": ["स्वेज नहर", "कील नहर", "पनामा नहर", "इरी नहर"],
        "ans": 2,
        "sol": "The Panama Canal is an artificial 82 km waterway in Panama that connects the Atlantic Ocean (via the Caribbean Sea) to the Pacific Ocean.",
        "sol_hi": "पनामा नहर मध्य अमेरिका में पनामा जलडमरूमध्य को काटते हुए बनाई गई कृत्रिम नहर है जो अटलांटिक और प्रशांत महासागर को जोड़ती है।"
    },
    {
        "q": "The deepest point of the Southern Ocean, the South Sandwich Trench, is also known as what deep?",
        "q_hi": "दक्षिणी महासागर का सबसे गहरा बिंदु 'साउथ सैंडविच गर्त' किस नाम से भी जाना जाता है?",
        "opts": ["Factorian Deep", "Challenger Deep", "Milwaukee Deep", "Valdivia Deep"],
        "opts_hi": ["फैक्टोरियन डीप", "चैलेंजर डीप", "मिल्वौकी डीप", "वाल्डिविया डीप"],
        "ans": 0,
        "sol": "The deepest point in the Southern Ocean is the Factorian Deep in the South Sandwich Trench, which is 7,434 meters deep.",
        "sol_hi": "दक्षिणी महासागर के साउथ सैंडविच गर्त के सबसे गहरे बिंदु को फैक्टोरियन डीप (Factorian Deep, 7,434 मीटर) कहा जाता है।"
    },
    {
        "q": "Which continent has the lowest percentage of mountainous land and is largely composed of flat plains and plateaus?",
        "q_hi": "किस महाद्वीप में पर्वतीय क्षेत्रों का प्रतिशत सबसे कम है और यह मुख्य रूप से मैदानी व पठारी भागों से निर्मित है?",
        "opts": ["Europe", "Africa", "Australia", "North America"],
        "opts_hi": ["यूरोप", "अफ्रीका", "ऑस्ट्रेलिया", "उत्तरी अमेरिका"],
        "ans": 2,
        "sol": "Australia is the flattest continent on Earth, with the lowest percentage of mountainous terrain.",
        "sol_hi": "ऑस्ट्रेलिया सबसे सपाट महाद्वीप है, जहाँ बहुत ही कम पर्वत श्रृंखलाएं (मुख्यतः ग्रेट डिवाइडिंग रेंज) पाई जाती हैं।"
    },
    {
        "q": "Which ocean has the famous Sargasso Sea, characterized by a lack of currents and abundance of brown seaweed, located in it?",
        "q_hi": "किस महासागर में प्रसिद्ध 'सारगासो सागर' (Sargasso Sea) स्थित है, जो धाराओं की अनुपस्थिति और समुद्री घास (Sargassum) के लिए प्रसिद्ध है?",
        "opts": ["North Pacific Ocean", "North Atlantic Ocean", "South Indian Ocean", "Mediterranean Sea"],
        "opts_hi": ["उत्तरी प्रशांत महासागर", "उत्तरी अटलांटिक महासागर", "दक्षिणी हिंद महासागर", "भूमध्य सागर"],
        "ans": 1,
        "sol": "The Sargasso Sea is located in the North Atlantic Ocean, bounded by four currents forming an ocean gyre.",
        "sol_hi": "सारगासो सागर उत्तरी अटलांटिक महासागर में स्थित एक शांत और स्थिर जल का क्षेत्र है, जो चारों ओर से घूमती महासागरीय जलधाराओं से घिरा है।"
    },
    {
        "q": "Which is the highest waterfall in the world, and on which continent is it located?",
        "q_hi": "विश्व का सबसे ऊंचा जलप्रपात कौन सा है, और यह किस महाद्वीप में स्थित है?",
        "opts": ["Niagara Falls - North America", "Angel Falls - South America", "Victoria Falls - Africa", "Jog Falls - Asia"],
        "opts_hi": ["नियाग्रा जलप्रपात - उत्तरी अमेरिका", "एंजेल जलप्रपात - दक्षिणी अमेरिका", "विक्टोरिया जलप्रपात - अफ्रीका", "जोग जलप्रपात - एशिया"],
        "ans": 1,
        "sol": "Angel Falls in Venezuela (South America) is the world's highest uninterrupted waterfall, with a height of 979 meters.",
        "sol_hi": "वेनेजुएला (दक्षिणी अमेरिका) में स्थित एंजेल जलप्रपात (Angel Falls) विश्व का सबसे ऊंचा निर्बाध जलप्रपात है (979 मीटर)।"
    },
    {
        "q": "Which is the largest gulf in the world by area?",
        "q_hi": "क्षेत्रफल के अनुसार विश्व की सबसे बड़ी खाड़ी (Gulf) कौन सी है?",
        "opts": ["Persian Gulf", "Gulf of Mexico", "Gulf of Aden", "Gulf of California"],
        "opts_hi": ["फारस की खाड़ी", "मेक्सिको की खाड़ी", "अदन की खाड़ी", "कैलिफोर्निया की खाड़ी"],
        "ans": 1,
        "sol": "The Gulf of Mexico is the largest gulf in the world, bounded by the United States, Mexico, and Cuba.",
        "sol_hi": "मेक्सिको की खाड़ी विश्व की सबसे बड़ी खाड़ी (Gulf) है, जो उत्तरी अमेरिका में स्थित है।"
    },
    {
        "q": "Which continent is separated from Asia by the Bering Strait?",
        "q_hi": "कौन सा महाद्वीप बेरिंग जलडमरूमध्य द्वारा एशिया से अलग होता है?",
        "opts": ["Europe", "Africa", "North America", "Australia"],
        "opts_hi": ["यूरोप", "अफ्रीका", "उत्तरी अमेरिका", "ऑस्ट्रेलिया"],
        "ans": 2,
        "sol": "The Bering Strait separates Asia (Siberia) from North America (Alaska).",
        "sol_hi": "बेरिंग जलडमरूमध्य एशिया (साइबेरिया) को उत्तरी अमेरिका (अलास्का) से अलग करता है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which of the following mountain ranges separates Europe from Asia?",
        "q_hi": "निम्नलिखित में से कौन सी पर्वत श्रृंखला यूरोप को एशिया से अलग करती है?",
        "opts": ["Ural Mountains", "Alps Mountains", "Pyrenees Mountains", "Appalachian Mountains"],
        "opts_hi": ["यूराल पर्वत", "आल्प्स पर्वत", "पायरेनीस पर्वत", "अप्पलाचियन पर्वत"],
        "ans": 0,
        "sol": "The Ural Mountains run from north to south through western Russia and form a natural boundary between Europe and Asia.",
        "sol_hi": "यूराल पर्वत श्रृंखला एशिया और यूरोप महाद्वीप के बीच प्राकृतिक सीमा बनाती है।"
    },
    {
        "q": "The deepest point of the Pacific Ocean and the Earth, Challenger Deep, reaches a depth of approximately:",
        "q_hi": "प्रशांत महासागर और संपूर्ण पृथ्वी का सबसे गहरा बिंदु 'चैलेंजर डीप' लगभग कितनी गहराई पर है?",
        "opts": ["8,848 meters", "9,120 meters", "11,000 meters", "12,500 meters"],
        "opts_hi": ["8,848 मीटर", "9,120 मीटर", "11,000 मीटर (लगभग)", "12,500 मीटर"],
        "ans": 2,
        "sol": "The Challenger Deep in the Mariana Trench reaches a depth of approximately 10,994 meters (roughly 11 km).",
        "sol_hi": "मारियाना गर्त का चैलेंजर डीप लगभग 10,994 मीटर (लगभग 11 किलोमीटर) गहरा है।"
    },
    {
        "q": "Which ocean is sometimes called the 'Half Ocean' because of its landlocked northern boundary?",
        "q_hi": "उत्तरी सीमा भू-आबद्ध होने के कारण किस महासागर को कभी-कभी 'अर्ध महासागर' भी कहा जाता है?",
        "opts": ["Arctic Ocean", "Southern Ocean", "Indian Ocean", "Atlantic Ocean"],
        "opts_hi": ["आर्कटिक महासागर", "दक्षिणी महासागर", "हिंद महासागर", "अटलांटिक महासागर"],
        "ans": 2,
        "sol": "The Indian Ocean is bounded on three sides by landmasses (Africa, Asia, Australia) and has no connection to the Arctic Ocean at the north, hence called a half ocean.",
        "sol_hi": "हिंद महासागर उत्तर में एशिया महाद्वीप से पूरी तरह घिरा है, इसलिए इसे अर्ध महासागर कहा जाता है।"
    },
    {
        "q": "Which of the following is the deepest trench in the Atlantic Ocean?",
        "q_hi": "निम्नलिखित में से कौन सा अटलांटिक महासागर का सबसे गहरा गर्त है?",
        "opts": ["Puerto Rico Trench", "Mariana Trench", "Java Trench", "Tonga Trench"],
        "opts_hi": ["प्यूर्टो रिको गर्त (Puerto Rico Trench)", "मारियाना गर्त", "जावा गर्त", "टोंगा गर्त"],
        "ans": 0,
        "sol": "The Puerto Rico Trench contains the Milwaukee Deep, which is the deepest point in the Atlantic Ocean at 8,376 meters.",
        "sol_hi": "प्यूर्टो रिको गर्त में अटलांटिक महासागर का सबसे गहरा बिंदु (8,376 मीटर) स्थित है।"
    },
    {
        "q": "Which is the highest peak in the Caucasus Mountain range, separating Europe and Asia?",
        "q_hi": "काकेशस पर्वत श्रृंखला, जो यूरोप और एशिया को विभाजित करती है, का सबसे ऊंचा शिखर कौन सा है?",
        "opts": ["Mount Blanc", "Mount Elbrus", "Mount Vesuvius", "Mount Ararat"],
        "opts_hi": ["माउंट ब्लांक", "माउंट एल्ब्रस (Mount Elbrus)", "माउंट विसुवियस", "माउंट अराफात"],
        "ans": 1,
        "sol": "Mount Elbrus is the highest peak of the Caucasus range and the continent of Europe.",
        "sol_hi": "माउंट एल्ब्रस काकेशस श्रेणी का सबसे ऊंचा शिखर होने के साथ यूरोप का भी सर्वोच्च बिंदु है।"
    },
    {
        "q": "Which ocean current is a warm current flowing along the eastern coast of North America?",
        "q_hi": "कौन सी महासागरीय जलधारा उत्तरी अमेरिका के पूर्वी तट के सहारे बहने वाली एक गर्म धारा है?",
        "opts": ["California Current", "Gulf Stream", "Labrador Current", "Canary Current"],
        "opts_hi": ["कैलिफोर्निया धारा", "गल्फ स्ट्रीम (Gulf Stream)", "लैब्राडोर धारा", "कनारी धारा"],
        "ans": 1,
        "sol": "The Gulf Stream is a powerful, warm Atlantic ocean current that originates in the Gulf of Mexico and stretches to the tip of Florida, flowing along the US east coast.",
        "sol_hi": "गल्फ स्ट्रीम उत्तरी अटलांटिक महासागर की एक प्रमुख गर्म जलधारा है जो अमेरिका के पूर्वी तट के सहारे बहती है।"
    },
    {
        "q": "Which continent is known for having the highest proportion of its area under the tropical zone?",
        "q_hi": "किस महाद्वीप का सर्वाधिक भाग उष्णकटिबंधीय क्षेत्र (Tropical Zone) के अंतर्गत आता है?",
        "opts": ["Asia", "South America", "Africa", "Australia"],
        "opts_hi": ["एशिया", "दक्षिणी अमेरिका", "अफ्रीका (Africa)", "ऑस्ट्रेलिया"],
        "ans": 2,
        "sol": "Africa lies majorly within the tropics, bordered by the Tropic of Cancer in the north and the Tropic of Capricorn in the south.",
        "sol_hi": "अफ्रीका महाद्वीप का सबसे बड़ा हिस्सा उष्णकटिबंध में स्थित है क्योंकि कर्क रेखा और मकर रेखा दोनों इसके मध्य भागों से होकर गुजरती हैं।"
    },
    {
        "q": "Which is the largest bay/gulf in the world in terms of shoreline length?",
        "q_hi": "तटरेखा की लंबाई के मामले में विश्व की सबसे बड़ी खाड़ी (Bay/Gulf) कौन सी है?",
        "opts": ["Hudson Bay", "Bay of Bengal", "Gulf of Mexico", "Persian Gulf"],
        "opts_hi": ["हडसन की खाड़ी (Hudson Bay)", "बंगाल की खाड़ी", "मेक्सिको की खाड़ी", "फारस की खाड़ी"],
        "ans": 0,
        "sol": "Hudson Bay in Canada has the longest shoreline of any bay in the world, while the Bay of Bengal is the largest bay by surface area.",
        "sol_hi": "कनाडा की हडसन की खाड़ी (Hudson Bay) की तटरेखा विश्व की सभी खाड़ियों में सबसे लंबी है, जबकि बंगाल की खाड़ी क्षेत्रफल में सबसे बड़ी खाड़ी है।"
    },
    {
        "q": "Which continent has the largest freshwater lake by surface area (Lake Superior) located on it?",
        "q_hi": "समीपवर्ती देशों की सीमा पर स्थित क्षेत्रफल में विश्व की सबसे बड़ी मीठे पानी की झील (सुपीरियर झील) किस महाद्वीप में है?",
        "opts": ["North America", "Asia", "Africa", "Europe"],
        "opts_hi": ["उत्तरी अमेरिका (North America)", "एशिया", "अफ्रीका", "यूरोप"],
        "ans": 0,
        "sol": "Lake Superior, the largest freshwater lake by surface area, is located in North America on the border between the USA and Canada.",
        "sol_hi": "सुपीरियर झील उत्तरी अमेरिका में कनाडा और संयुक्त राज्य अमेरिका की सीमा पर स्थित विश्व की सबसे बड़ी मीठे पानी की झील है।"
    },
    {
        "q": "What is the name of the cold ocean current that flows near the northwestern coast of Africa?",
        "q_hi": "अफ्रीका के उत्तर-पश्चिमी तट के निकट प्रवाहित होने वाली ठंडी महासागरीय जलधारा का क्या नाम है?",
        "opts": ["Benguela Current", "Agulhas Current", "Canary Current", "Guinea Current"],
        "opts_hi": ["बेंगुएला धारा", "अगुलहास धारा", "कनारी धारा (Canary Current)", "गिनी धारा"],
        "ans": 2,
        "sol": "The Canary Current is a wind-driven cold surface current that flows southwards along the northwest coast of Africa.",
        "sol_hi": "कनारी धारा एक ठंडी जलधारा है जो उत्तरी अटलांटिक महासागर में अफ्रीका के उत्तर-पश्चिमी तट के सहारे बहती है।"
    },
    {
        "q": "Which continent is completely surrounded by the Southern Ocean?",
        "q_hi": "कौन सा महाद्वीप पूरी तरह से दक्षिणी महासागर से घिरा हुआ है?",
        "opts": ["Australia", "South America", "Antarctica", "Africa"],
        "opts_hi": ["ऑस्ट्रेलिया", "दक्षिणी अमेरिका", "अंटार्कटिका (Antarctica)", "अफ्रीका"],
        "ans": 2,
        "sol": "Antarctica is the southern-most continent, centered around the South Pole and completely surrounded by the Southern Ocean.",
        "sol_hi": "अंटार्कटिका महाद्वीप पूरी तरह से दक्षिणी गोलार्ध में स्थित है और इसे दक्षिणी महासागर चारों ओर से घेरता है।"
    },
    {
        "q": "Which is the longest river in Europe?",
        "q_hi": "यूरोप महाद्वीप की सबसे लंबी नदी कौन सी है?",
        "opts": ["Danube", "Volga", "Rhine", "Ural"],
        "opts_hi": ["डेन्यूब", "वोल्गा (Volga)", "राइन", "यूराल"],
        "ans": 1,
        "sol": "The Volga River, flowing through Russia into the Caspian Sea, is the longest river in Europe.",
        "sol_hi": "रूस में बहने वाली वोल्गा नदी यूरोप महाद्वीप की सबसे लंबी नदी है जो कैस्पियन सागर में गिरती है।"
    },
    {
        "q": "Which island group is separated from mainland Australia by the Bass Strait?",
        "q_hi": "कौन सा द्वीप समूह बास जलडमरूमध्य (Bass Strait) द्वारा मुख्य भूमि ऑस्ट्रेलिया से अलग होता है?",
        "opts": ["New Zealand", "Tasmania", "Papua New Guinea", "Fiji"],
        "opts_hi": ["न्यूजीलैंड", "तस्मानिया (Tasmania)", "पापुआ न्यू गिनी", "फिजी"],
        "ans": 1,
        "sol": "The Bass Strait is a sea strait separating Tasmania from the Australian mainland.",
        "sol_hi": "बास जलडमरूमध्य मुख्य भूमि ऑस्ट्रेलिया को तस्मानिया द्वीप से अलग करने वाला जलमार्ग है।"
    },
    {
        "q": "In which ocean is the deep Puerto Rico Trench located?",
        "q_hi": "गहरी प्यूर्टो रिको गर्त किस महासागर में स्थित है?",
        "opts": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean"],
        "opts_hi": ["अटलांटिक महासागर (Atlantic Ocean)", "प्रशांत महासागर", "हिंद महासागर", "आर्कटिक महासागर"],
        "ans": 0,
        "sol": "The Puerto Rico Trench is located on the boundary between the Caribbean Sea and the Atlantic Ocean.",
        "sol_hi": "प्यूर्टो रिको गर्त अटलांटिक महासागर में स्थित है जो इस महासागर का सबसे गहरा गर्त है।"
    },
    {
        "q": "The ocean current 'Kuroshio' is a:",
        "q_hi": "महासागरीय जलधारा 'क्यूरोशियो' (Kuroshio) एक:",
        "opts": ["Cold current in Pacific", "Warm current in Pacific", "Cold current in Atlantic", "Warm current in Indian Ocean"],
        "opts_hi": ["प्रशांत महासागर की ठंडी धारा", "प्रशांत महासागर की गर्म धारा (Warm current)", "अटलांटिक महासागर की ठंडी धारा", "हिंद महासागर की गर्म धारा"],
        "ans": 1,
        "sol": "The Kuroshio Current, also known as the Black Current, is a warm North Pacific ocean current flowing along the eastern coast of Japan.",
        "sol_hi": "क्यूरोशियो प्रशांत महासागर की एक प्रमुख गर्म जलधारा है जो जापान के पूर्वी तट के सहारे बहती है।"
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
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Comprehensive review of 7 continents and 5 oceans.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Continental Relief & Peaks",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which is the highest peak in Europe?", "opts": ["Mount Blanc", "Mount Elbrus", "Mount Everest", "Mount McKinley"], "ans": 1, "sol": "Mount Elbrus is the highest peak of Europe, located in the Caucasus range."},
                    {"type": "MCQ", "q": "Which is the highest peak in South America?", "opts": ["Mount Aconcagua", "Mount Cotopaxi", "Mount Kilimanjaro", "Mount Denali"], "ans": 0, "sol": "Mount Aconcagua is the highest peak in South America."},
                    {"type": "True/False", "q": "True or False: Mount Kosciuszko is the highest peak of mainland Australia.", "ans": True, "sol": "True. It stands at 2,228 meters."},
                    {"type": "One-Liner", "q": "What is the highest mountain peak in Antarctica?", "sol": "Vinson Massif"}
                ]
            },
            {
                "title": "2. Oceans & Trenches",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which is the deepest trench in the Atlantic Ocean?", "opts": ["Mariana Trench", "Puerto Rico Trench", "Sunda Trench", "South Sandwich Trench"], "ans": 1, "sol": "The Puerto Rico Trench is the deepest in the Atlantic."},
                    {"type": "MCQ", "q": "Which ocean is bounded by the volcanic Ring of Fire?", "opts": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Southern Ocean"], "ans": 2, "sol": "The Pacific Ocean contains the Ring of Fire."},
                    {"type": "True/False", "q": "True or False: The Sunda Trench is the deepest point in the Indian Ocean.", "ans": True, "sol": "True. It reaches about 7,290 meters."},
                    {"type": "MCQ", "q": "Which is the smallest and shallowest ocean?", "opts": ["Indian Ocean", "Southern Ocean", "Arctic Ocean", "Pacific Ocean"], "ans": 2, "sol": "The Arctic Ocean is the smallest and shallowest."}
                ]
            },
            {
                "title": "3. Straits & Canals",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which canal connects the Red Sea to the Mediterranean Sea?", "opts": ["Panama Canal", "Suez Canal", "Kiel Canal", "Erie Canal"], "ans": 1, "sol": "The Suez Canal connects them."},
                    {"type": "MCQ", "q": "Which strait connects the Pacific and Arctic Oceans?", "opts": ["Strait of Gibraltar", "Bering Strait", "Strait of Malacca", "Bass Strait"], "ans": 1, "sol": "The Bering Strait connects them."},
                    {"type": "True/False", "q": "True or False: The Panama Canal connects the Atlantic and Pacific Oceans.", "ans": True, "sol": "True. It cuts through Central America."},
                    {"type": "One-Liner", "q": "Which strait separates Tasmania from mainland Australia?", "sol": "Bass Strait"}
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
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "7 महाद्वीपों और 5 महासागरों की गहन समीक्षा।", "sections": deep_dive_hi}
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
                "title": "1. महाद्वीपीय उच्चावच और चोटियाँ",
                "masteryZone": [
                    {"type": "MCQ", "q": "यूरोप की सबसे ऊंची चोटी कौन सी है?", "opts": ["माउंट ब्लांक", "माउंट एल्ब्रस", "माउंट एवरेस्ट", "माउंट मैककिनले"], "ans": 1, "sol": "माउंट एल्ब्रस यूरोप का सर्वोच्च शिखर है, जो काकेशस श्रेणी में है।"},
                    {"type": "MCQ", "q": "दक्षिणी अमेरिका की सबसे ऊंची चोटी कौन सी है?", "opts": ["माउंट अकोंकागुआ", "माउंट कोटोपैक्सी", "माउंट किलिमंजारो", "माउंट डेनाली"], "ans": 0, "sol": "माउंट अकोंकागुआ दक्षिणी अमेरिका का सर्वोच्च शिखर है।"},
                    {"type": "True/False", "q": "सही या गलत: माउंट कोसिअस्को मुख्य भूमि ऑस्ट्रेलिया का सबसे ऊंचा शिखर है।", "ans": True, "sol": "सही। यह 2,228 मीटर ऊंचा है।"},
                    {"type": "One-Liner", "q": "अंटार्कटिका महाद्वीप का सबसे ऊंचा पर्वत शिखर कौन सा है?", "sol": "विंसन मैसिफ"}
                ]
            },
            {
                "title": "2. महासागर और गर्त",
                "masteryZone": [
                    {"type": "MCQ", "q": "अटलांटिक महासागर का सबसे गहरा गर्त कौन सा है?", "opts": ["मारियाना गर्त", "प्यूर्टो रिको गर्त", "सुंडा गर्त", "साउथ सैंडविच गर्त"], "ans": 1, "sol": "प्यूर्टो रिको गर्त अटलांटिक महासागर का सबसे गहरा बिंदु है।"},
                    {"type": "MCQ", "q": "किस महासागर के चारों ओर ज्वालामुखीय रिंग ऑफ फायर स्थित है?", "opts": ["अटलांटिक महासागर", "हिंद महासागर", "प्रशांत महासागर", "दक्षिणी महासागर"], "ans": 2, "sol": "प्रशांत महासागर में रिंग ऑफ फायर स्थित है।"},
                    {"type": "True/False", "q": "सही या गलत: सुंडा गर्त हिंद महासागर का सबसे गहरा बिंदु है।", "ans": True, "sol": "सही। यह लगभग 7,290 मीटर गहरा है।"},
                    {"type": "MCQ", "q": "विश्व का सबसे छोटा और सबसे उथला महासागर कौन सा है?", "opts": ["हिंद महासागर", "दक्षिणी महासागर", "आर्कटिक महासागर", "प्रशांत महासागर"], "ans": 2, "sol": "आर्कटिक महासागर सबसे छोटा और सबसे उथला है।"}
                ]
            },
            {
                "title": "3. जलसंधियाँ और नहरें",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सी नहर लाल सागर को भूमध्य सागर से जोड़ती है?", "opts": ["पनामा नहर", "स्वेज नहर", "कील नहर", "इरी नहर"], "ans": 1, "sol": "स्वेज नहर दोनों जल निकायों को जोड़ती है।"},
                    {"type": "MCQ", "q": "कौन सी जलसंधि प्रशांत और आर्कटिक महासागर को जोड़ती है?", "opts": ["जिब्राल्टर जलसंधि", "बेरिंग जलसंधि", "मलक्का जलसंधि", "बास जलसंधि"], "ans": 1, "sol": "बेरिंग जलसंधि दोनों को जोड़ती है।"},
                    {"type": "True/False", "q": "सही या गलत: पनामा नहर अटलांटिक और प्रशांत महासागर को जोड़ती है।", "ans": True, "sol": "सही। यह मध्य अमेरिका में पनामा जलडमरूमध्य को काटती है।"},
                    {"type": "One-Liner", "q": "तस्मानिया को मुख्य भूमि ऑस्ट्रेलिया से कौन सी जलसंधि अलग करती है?", "sol": "बास जलसंधि"}
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
