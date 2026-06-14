import json
import os
import re

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\history-of-india\pre-historic-period"

def highlight_bold(text):
    if not isinstance(text, str):
        return text
    # Replaces **text** with <strong style="color: #e74c3c; font-weight: 800;">text</strong>
    # We use a beautiful warning/accent color (like #e74c3c or #d35400) to make it stand out!
    return re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #e74c3c; font-weight: 800;">\1</strong>', text)

def process_data(data):
    if isinstance(data, dict):
        return {k: process_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [process_data(item) for item in data]
    elif isinstance(data, str):
        return highlight_bold(data)
    else:
        return data

# ----------------- SVG DIAGRAMS -----------------
# Diagram 1: Tool Evolution (Palaeolithic to Neolithic)
tool_evolution_svg = """<svg viewBox="0 0 800 320" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 15px;">
<style>
  .svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: var(--text-dark, #2c3e50); font-size: 16px; }
  .tool-node { fill: var(--bg-card, #fdfefe); stroke: #3498db; stroke-width: 2px; rx: 6px; ry: 6px; }
  .tool-node-highlight { fill: rgba(46, 204, 113, 0.08); stroke: #2ecc71; stroke-width: 2.5px; rx: 6px; ry: 6px; }
  .text-title { font-family: 'Outfit', sans-serif; font-size: 12px; fill: var(--primary, #1a5276); font-weight: 700; }
  .text-desc { font-family: 'Inter', sans-serif; font-size: 10.5px; fill: var(--text-light, #555); }
  .svg-arrow { fill: none; stroke: #bdc3c7; stroke-width: 2px; marker-end: url(#arrowhead); }
</style>
<defs>
  <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="6" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#bdc3c7" />
  </marker>
</defs>
<text x="20" y="25" class="svg-title">Evolution of Prehistoric Stone Tool Technologies</text>
 
<!-- Lower Palaeolithic -->
<rect x="20" y="60" width="130" height="220" class="tool-node" />
<path d="M 85 90 C 60 110, 60 170, 85 190 C 110 170, 110 110, 85 90 Z" fill="#eaecee" stroke="#7f8c8d" stroke-width="1.5"/>
<line x1="85" y1="90" x2="85" y2="190" stroke="#7f8c8d" stroke-dasharray="2,2" />
<text x="85" y="210" class="text-title" text-anchor="middle">Lower Palaeolithic</text>
<text x="85" y="230" class="text-desc" text-anchor="middle">Pebble &amp; Core Tools</text>
<text x="85" y="245" class="text-desc" text-anchor="middle">Handaxes, Cleavers</text>
<text x="85" y="260" class="text-desc" text-anchor="middle">e.g., Pallavaram</text>
 
<path d="M 155 170 L 175 170" class="svg-arrow" />
 
<!-- Middle Palaeolithic -->
<rect x="180" y="60" width="130" height="220" class="tool-node" />
<path d="M 245 100 L 210 150 L 235 180 L 270 170 L 280 130 Z" fill="#eaecee" stroke="#7f8c8d" stroke-width="1.5"/>
<text x="245" y="210" class="text-title" text-anchor="middle">Middle Palaeolithic</text>
<text x="245" y="230" class="text-desc" text-anchor="middle">Flake Tools</text>
<text x="245" y="245" class="text-desc" text-anchor="middle">Scrapers, Borers, Points</text>
<text x="245" y="260" class="text-desc" text-anchor="middle">e.g., Nevasa</text>
 
<path d="M 315 170 L 335 170" class="svg-arrow" />
 
<!-- Upper Palaeolithic -->
<rect x="340" y="60" width="130" height="220" class="tool-node" />
<path d="M 405 90 L 395 180 L 405 190 L 415 180 Z" fill="#eaecee" stroke="#7f8c8d" stroke-width="1.5"/>
<text x="405" y="210" class="text-title" text-anchor="middle">Upper Palaeolithic</text>
<text x="405" y="230" class="text-desc" text-anchor="middle">Blades &amp; Bone Tools</text>
<text x="405" y="245" class="text-desc" text-anchor="middle">Burins, Harpoons</text>
<text x="405" y="260" class="text-desc" text-anchor="middle">e.g., Lohanda Nala</text>
 
<path d="M 475 170 L 495 170" class="svg-arrow" />
 
<!-- Mesolithic -->
<rect x="500" y="60" width="130" height="220" class="tool-node-highlight" />
<polygon points="560 110, 545 140, 565 140" fill="#fcf3cf" stroke="#f39c12" stroke-width="1.5"/>
<polygon points="580 120, 570 145, 580 140" fill="#fcf3cf" stroke="#f39c12" stroke-width="1.5"/>
<text x="565" y="210" class="text-title" text-anchor="middle" fill="#d35400">Mesolithic</text>
<text x="565" y="230" class="text-desc" text-anchor="middle">Microliths (&lt; 5cm)</text>
<text x="565" y="245" class="text-desc" text-anchor="middle">Composite Tools</text>
<text x="565" y="260" class="text-desc" text-anchor="middle">e.g., Pratapgarh Sites</text>
 
<path d="M 635 170 L 655 170" class="svg-arrow" />
 
<!-- Neolithic -->
<rect x="660" y="60" width="130" height="220" class="tool-node" />
<path d="M 725 90 C 715 110, 715 170, 725 185 L 710 185 L 710 90 Z" fill="#d5dbdb" stroke="#7f8c8d" stroke-width="1.5"/>
<text x="725" y="210" class="text-title" text-anchor="middle">Neolithic</text>
<text x="725" y="230" class="text-desc" text-anchor="middle">Polished Celts</text>
<text x="725" y="245" class="text-desc" text-anchor="middle">Ground Stone Axes</text>
<text x="725" y="260" class="text-desc" text-anchor="middle">e.g., Burzahom</text>
</svg>"""

# Diagram 2: UP Prehistoric Sites Mapping
up_prehistoric_sites_svg = """<svg viewBox="0 0 800 340" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 15px;">
<style>
  .svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: var(--text-dark, #2c3e50); font-size: 16px; }
  .up-node { fill: var(--bg-card, #fdfefe); stroke: #8e44ad; stroke-width: 2px; rx: 6px; ry: 6px; }
  .up-node-highlight { fill: rgba(142, 68, 173, 0.08); stroke: #9b59b6; stroke-width: 2px; rx: 8px; ry: 8px; }
  .text-district { font-family: 'Outfit', sans-serif; font-size: 12px; fill: var(--primary, #7d3c98); font-weight: 700; }
  .text-site { font-family: 'Outfit', sans-serif; font-size: 13px; fill: var(--text-dark, #2c3e50); font-weight: bold; }
  .text-feature { font-family: 'Inter', sans-serif; font-size: 10.5px; fill: var(--text-light, #555); }
  .svg-connector { fill: none; stroke: #b03a2e; stroke-width: 1.5px; stroke-dasharray: 4,4; }
  .map-box { fill: #ebf5fb; stroke: #2980b9; stroke-width: 1px; }
  .map-text { font-family: 'Outfit', sans-serif; font-size: 11px; fill: #1b4f72; font-weight: bold; }
</style>
<text x="20" y="25" class="svg-title">Key Prehistoric &amp; Archaeological Sites of Uttar Pradesh</text>
 
<!-- District: Pratapgarh (Mesolithic Hub) -->
<rect x="20" y="60" width="230" height="230" class="up-node-highlight" />
<text x="135" y="85" class="text-district" text-anchor="middle">📍 PRATAPGARH DISTRICT</text>
<line x1="35" y1="95" x2="235" y2="95" stroke="#d7bde2" stroke-width="1"/>
<text x="40" y="115" class="text-site">Sarai Nahar Rai</text>
<text x="40" y="130" class="text-feature">• Earliest burials &amp; hearths inside huts</text>
<text x="40" y="145" class="text-feature">• Earliest war evidence (embedded arrowhead)</text>
<text x="40" y="170" class="text-site">Mahadaha</text>
<text x="40" y="185" class="text-feature">• Double burials (male &amp; female together)</text>
<text x="40" y="200" class="text-feature">• Ornaments made of deer antler &amp; bone</text>
<text x="40" y="225" class="text-site">Damdama</text>
<text x="40" y="240" class="text-feature">• 41 human graves; unique triple burial</text>
<text x="40" y="255" class="text-feature">• Extensive bone points &amp; tools</text>
 
<!-- District: Prayagraj / Belan Valley -->
<rect x="280" y="60" width="240" height="230" class="up-node" />
<text x="400" y="85" class="text-district" text-anchor="middle">BELAN VALLEY (PRAYAGRAJ/MIRZAPUR)</text>
<line x1="295" y1="95" x2="510" y2="95" stroke="#ebc2f5" stroke-width="1"/>
<text x="300" y="115" class="text-site">Continuous Cultural Sequence</text>
<text x="300" y="130" class="text-feature">• Only valley showing sequence from Palaeolithic,</text>
<text x="300" y="145" class="text-feature">  through Mesolithic, to Neolithic layers</text>
<text x="300" y="170" class="text-site">Lohanda Nala</text>
<text x="300" y="185" class="text-feature">• Bone Mother Goddess figurine (or harpoon)</text>
<text x="300" y="210" class="text-site">Koldihwa</text>
<text x="300" y="225" class="text-feature">• Early agricultural site (rice husks: ~6000 BC)</text>
<text x="300" y="250" class="text-site">Chopani Mando</text>
<text x="300" y="265" class="text-feature">• Earliest handmade pottery in the world</text>
 
<!-- District: Sant Kabir Nagar -->
<rect x="550" y="60" width="230" height="230" class="up-node" />
<text x="665" y="85" class="text-district" text-anchor="middle">SANT KABIR NAGAR</text>
<line x1="565" y1="95" x2="765" y2="95" stroke="#ebc2f5" stroke-width="1"/>
<text x="570" y="120" class="text-site">Lahuradewa</text>
<text x="570" y="145" class="text-feature" fill="#b03a2e" style="font-weight: bold;">Rice Cultivation: ~9000 BC</text>
<text x="570" y="170" class="text-feature">• Oldest evidence of rice in the world</text>
<text x="570" y="190" class="text-feature">• Pushed back agricultural timeline in Asia</text>
<text x="570" y="210" class="text-feature">• Older than Koldihwa &amp; Mehrgarh wheat</text>
<text x="570" y="235" class="text-feature">• Excavations by UP State Archaeology</text>
</svg>"""


# ----------------- THEORY GENERATION (ENGLISH) -----------------
theory = {
    "breadcrumbs": {
        "parent": "History of India",
        "parentUrl": "../",
        "current": "Pre-Historic Period"
    },
    "hero": {
        "title": "Pre-Historic Period & Sources of Information",
        "description": "Exhaustive study guide on the Pre-historic era of India. Master the Palaeolithic, Mesolithic, Neolithic, Chalcolithic, and Iron Ages, including key archaeological sites, tool technologies, fossil records, and UP-specific developments for AHC RO/ARO and UPSC exams."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive Mock Test (15 Questions)",
            "description": "Assess your conceptual clarity of Pre-historic India. Test your knowledge on archaeological sites, tool technologies, and chronological sequences under timed conditions.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Mock Test"
        }
    },
    "timeline": {
        "title": "Prehistoric Timeline & Chronological Development",
        "description": "Key evolutionary and technological milestones of pre-historic India.",
        "cards": [
            {
                "period": "Palaeolithic Age (Old Stone Age)",
                "date": "2 Million BC – 10,000 BC",
                "details": "Divided into Lower, Middle, and Upper Palaeolithic. Characterized by Pleistocene Ice Age, nomadic hunting-gathering, quartzite tools, and the discovery of fire (late phase). Earliest hominid fossil found at Hathnora."
            },
            {
                "period": "Mesolithic Age (Middle Stone Age)",
                "date": "10,000 BC – 6,000 BC",
                "details": "Coincides with Holocene warming. Characterized by microliths (tiny stone tools under 5cm), hunting smaller game, and early animal domestication (Bagor, Adamgarh). Human burials and bone ornaments appear in UP (Pratapgarh)."
            },
            {
                "period": "Neolithic Age (New Stone Age)",
                "date": "6,000 BC – 1,000 BC",
                "details": "The 'Neolithic Revolution' (V. Gordon Childe). Development of settled agriculture, pottery, discovery of the wheel, and polished stone celts. Major sites: Mehrgarh, Burzahom, Koldihwa, Lahuradewa."
            },
            {
                "period": "Chalcolithic Age (Copper-Stone Age)",
                "date": "3,000 BC – 500 BC",
                "details": "First metal age using copper alongside stone. Rural farming communities, painted Black-and-Red Ware, regional cultures (Ahar, Malwa, Jorwe). Fortified sites like Inamgaon and Daimabad. High infant mortality."
            },
            {
                "period": "Iron Age & Megalithic Culture",
                "date": "1,000 BC – Historical Period",
                "details": "Introduction of iron metallurgy, transition to Painted Grey Ware (PGW) in the north, and Megalithic burials (large stone circle graves) in South India (Adichanallur, Hire Benakal)."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Triggers",
        "description": "Hacks to retain key terms and concepts for competitive exams.",
        "items": [
            {
                "title": "Chronological Sequence",
                "phrase": "\"P-M-N-C-I\"",
                "decryption": "<strong>P</strong>lease <strong>M</strong>ake <strong>N</strong>ew <strong>C</strong>opper <strong>I</strong>tems ➔ <strong>P</strong>aleolithic ➔ <strong>M</strong>esolithic ➔ <strong>N</strong>eolithic ➔ <strong>C</strong>halcolithic ➔ <strong>I</strong>ron Age."
            },
            {
                "title": "Pratapgarh Mesolithic Sites (UP)",
                "phrase": "\"S-M-D\"",
                "decryption": "<strong>S</strong>uper <strong>M</strong>edical <strong>D</strong>epartment ➔ <strong>S</strong>arai Nahar Rai, <strong>M</strong>ahadaha, <strong>D</strong>amdama (Pratapgarh district, UP). Key Mesolithic burial sites."
            },
            {
                "title": "Bhimbetka Discoverer",
                "phrase": "\"WAK-AN-KAR\"",
                "decryption": "Sounds like 'Walk in Car'. Dr. V.S. Wakankar drove and walked to discover Bhimbetka caves in 1957."
            },
            {
                "title": "Hathnora Fossil Discoverer",
                "phrase": "\"SON-AKIA\"",
                "decryption": "Arun Sonakia discovered the skull of the 'Son' of Narmada (Homo erectus hominid fossil) in 1982."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flick through these cards for quick memory reinforcement before testing yourself.",
        "items": [
            {
                "question": "Who is the Father of Indian Prehistory?",
                "answer": "<strong>Robert Bruce Foote</strong>. He discovered the first Palaeolithic tool in India (an Acheulean handaxe/cleaver) at Pallavaram, Chennai, in 1863.",
                "icon": "fa-user-tie"
            },
            {
                "question": "Which site yielded the earliest hominid fossil in India?",
                "answer": "<strong>Hathnora</strong> (Narmada Valley, MP). Arun Sonakia discovered the <em>Homo erectus</em> skull cap (Narmada Human) here in 1982.",
                "icon": "fa-skull"
            },
            {
                "question": "Where is the earliest evidence of agriculture in the subcontinent?",
                "answer": "<strong>Mehrgarh</strong> (Balochistan, Pakistan). Dates back to ~7000 BC, showing cultivation of wheat, barley, and cotton.",
                "icon": "fa-seedling"
            },
            {
                "question": "Which site provides the oldest evidence of rice cultivation in the world?",
                "answer": "<strong>Lahuradewa</strong> (Sant Kabir Nagar, UP). Excavations show rice cultivation dating to ~9000 BC, older than Koldihwa (~6000 BC).",
                "icon": "fa-bowl-rice"
            },
            {
                "question": "What are Ash Mounds in the context of Indian prehistory?",
                "answer": "Accumulations of burnt cow dung found at South Indian Neolithic sites like <strong>Piklihal</strong>, <strong>Utnur</strong>, and <strong>Kupgal</strong>, indicating cattle penning.",
                "icon": "fa-fire"
            },
            {
                "question": "Which Mesolithic site in UP has a triple burial?",
                "answer": "<strong>Damdama</strong> (Pratapgarh, UP). It contains a single grave containing three human skeletons buried together.",
                "icon": "fa-users"
            },
            {
                "question": "What is unique about the Ahar Chalcolithic culture?",
                "answer": "Also known as <strong>Tambavati</strong> (place of copper) in Rajasthan. It lacks a stone-blade/microlith industry; tools were exclusively copper.",
                "icon": "fa-cubes"
            },
            {
                "question": "Where was the famous Daimabad bronze hoard found?",
                "answer": "<strong>Daimabad</strong> (Maharashtra), a Jorwe culture site. It yielded exquisite bronze sculptures of a chariot with driver, rhino, elephant, and buffalo.",
                "icon": "fa-gem"
            }
        ]
    },
    "traps": {
        "title": "AHC RO/ARO & UPSC Traps to Avoid",
        "items": [
            "<strong>Trap 1: Confusing Koldihwa and Lahuradewa for Rice.</strong> Koldihwa (~6000 BC) was long considered the oldest, but recent excavations at Lahuradewa (UP) pushed it back to ~9000 BC. If both are in options, Lahuradewa is correct.",
            "<strong>Trap 2: Assuming Palaeolithic people had agriculture or pottery.</strong> They were strictly hunter-gatherers. Pottery and agriculture only emerged in the Neolithic period (with the unique exception of Mesolithic Chopani Mando having the earliest handmade pottery).",
            "<strong>Trap 3: Believing Megaliths are only found in South India.</strong> While most famous in South India (associated with the Iron Age), early Megalithic structures have also been found in Kashmir, UP, and Rajasthan.",
            "<strong>Trap 4: Conflating 'Father of Indian Prehistory' with 'Father of Indian Archaeology'.</strong> Robert Bruce Foote is the Father of Indian Prehistory (discovered Pallavaram tool in 1863). Alexander Cunningham is the Father of Indian Archaeology (founded ASI in 1861)."
        ]
    },
    "deepDive": {
        "title": "Comprehensive Study Notes (Deep-Dive)",
        "description": "Detailed analysis of Pre-historic India, sub-divided by phase and including crucial geographic and historiographical markers.",
        "sections": [
            {
                "title": "1. Historiography, Pioneers & Classifications",
                "content": "<p>Indian prehistory is the study of the human past before the advent of written records. The classification of human cultural history is broadly tripartite:</p><ul><li><strong>Prehistory:</strong> No written records. Relies 100% on archaeological remains (e.g., Palaeolithic, Mesolithic, Neolithic).</li><li><strong>Protohistory:</strong> Writing exists but is either not deciphered (e.g., Indus Valley Civilization) or lacks direct archaeological corroboration (e.g., Vedic period).</li><li><strong>History:</strong> Written records are available and deciphered (begins around 6th Century BC with Mahajanapadas and Ashokan inscriptions).</li></ul><h3>Pioneers of Indian Prehistory</h3><p>The systematic study of Indian prehistory began in the 19th century. Below are the key figures whose discoveries are frequently asked in competitive exams:</p><ul><li><strong>Robert Bruce Foote:</strong> A British geologist who discovered the first Palaeolithic tool in India (an Acheulean handaxe/cleaver) at <strong>Pallavaram</strong> near Chennai in May 1863. Hence, he is called the <em>Father of Indian Prehistory</em>.</li><li><strong>Alexander Cunningham:</strong> A British Army engineer who became the first Director-General of the Archaeological Survey of India (ASI) in 1861. He is known as the <em>Father of Indian Archaeology</em>.</li><li><strong>Dr. V.S. Wakankar:</strong> An Indian archaeologist who discovered the world-famous <strong>Bhimbetka rock shelters</strong> in Madhya Pradesh in 1957.</li><li><strong>Arun Sonakia:</strong> Discovered the fossilized skull cap of <strong>Homo erectus</strong> (Narmada Human) at <strong>Hathnora</strong> (MP) in 1982.</li><li><strong>H.D. Sankalia:</strong> Conducted extensive scientific excavations across India (Nevasa, Langhnaj, Navdatoli) and structured prehistoric studies.</li><li><strong>Sir Mortimer Wheeler:</strong> D-G of ASI who introduced scientific stratigraphy in excavations, allowing precise relative dating of archaeological layers.</li></ul>"
            },
            {
                "title": "2. Palaeolithic Age (Old Stone Age): 2 Million BC – 10,000 BC",
                "content": "<p>The Palaeolithic Age developed during the <strong>Pleistocene epoch</strong> (Ice Age), during which major portions of the earth were covered in ice, forcing early humans to live in cave shelters and hunt large game. Humans were completely nomadic hunter-gatherers, with no knowledge of agriculture or pottery. Because they used rough, unpolished quartzite stones for tools, they are often referred to as <strong>'Quartzite Men'</strong>.</p><h3>Sub-Divisions of the Palaeolithic Age</h3><p>Based on tool technology and climatic changes, the Palaeolithic is divided into three phases:</p>" + tool_evolution_svg + """<div class="premium-table-container"><table class="premium-table"><thead><tr><th>Phase &amp; Period</th><th>Tool Technology</th><th>Key Climatic Features</th><th>Major Indian Sites</th></tr></thead><tbody><tr><td>Lower Palaeolithic</td><td>Handaxes, cleavers, choppers (heavy pebble core tools). Acheulean &amp; Soanian cultures.</td><td>Severe Ice Age. Extreme cold and dry conditions.</td><td>Bori (MH - oldest, ~1.4 Ma), Attirampakkam (TN), Didwana (RJ), Hunsgi (KA), Belan Valley (UP).</td></tr><tr><td>Middle Palaeolithic</td><td>Flake-based tools (scrapers, borers, points). Nevasan culture.</td><td>Slight warming, flake tradition replaces core tools.</td><td>Nevasa (MH), Didwana (RJ), Bhimbetka (MP), Belan Valley (UP).</td></tr><tr><td>Upper Palaeolithic</td><td>Blades, burins, bone tools. Emergence of modern <em>Homo sapiens</em>.</td><td>Warmer, end of Pleistocene. Less ice cover.</td><td>Kurnool Caves (AP - ash/fire), Patne (MH - ostrich shells), Lohanda Nala (UP - Mother Goddess figurine), Baghor I (MP).</td></tr></tbody></table></div><h3>Critical Discoveries &amp; Sites</h3><ul><li><strong>Hathnora (MP):</strong> Located on the banks of the Narmada River. Yielded the skull cap of <em>Homo erectus</em> (Narmada Human), the **only pre-Homo sapiens human fossil** found in the entire Indian subcontinent.</li><li><strong>Kurnool Caves (AP):</strong> Provided the earliest evidence of the **use of fire** in the Indian subcontinent, indicated by thick deposits of ash.</li><li><strong>Patne (Maharashtra):</strong> Yielded fragments of ostrich eggshells engraved with geometric designs and turned into beads, proving Upper Palaeolithic art.</li><li><strong>Baghor I (MP):</strong> Excavations in the Son Valley revealed a stone platform with a triangular stone in the center, interpreted as the **earliest prehistoric shrine** (worship of Mother Goddess) dating back to ~10,000 BC.</li><li><strong>Lohanda Nala (Belan Valley, UP):</strong> Yielded a carved bone object identified as a **Mother Goddess figurine** (some scholars interpret it as a bone harpoon), representing one of the earliest bone sculptures in the world.</li></ul>"""
            },
            {
                "title": "3. Mesolithic Age (Middle Stone Age): 10,000 BC – 6,000 BC",
                "content": "<p>The Mesolithic Age was a transitional phase between the Palaeolithic and Neolithic. It coincided with the onset of the <strong>Holocene epoch</strong>, bringing a warmer, wetter climate, which led to the expansion of flora and fauna. Humans adapted by hunting smaller, faster animals (rabbits, birds), fishing, and fowling.</p><h3>Key Feature: Microliths</h3><p>The primary technological marker of this period is the **Microlith**—tiny, sharp, geometric stone tools (like triangles, trapezes, crescents) usually ranging from 1 to 5 cm in size. These were hafted onto wooden or bone handles to make composite tools like arrows, spears, and sickles.</p><h3>Major Mesolithic Sites &amp; Discoveries</h3><ul><li><strong>Bagor (Rajasthan):</strong> Located on the Kothari River. It is the **largest Mesolithic site** in India and, along with **Adamgarh** (MP), provides the **earliest evidence of animal domestication** (dogs, sheep, goats, cattle) dating back to ~5000 BC.</li><li><strong>Chopani Mando (UP):</strong> Located in the Belan Valley, Prayagraj. It shows a sequence from Mesolithic to Neolithic and has yielded the **earliest handmade pottery in the world**.</li><li><strong>Pratapgarh District Sites (UP):</strong> These sites are crucial for UP exams:<ul><li><strong>Sarai Nahar Rai:</strong> Yielded the earliest evidence of human burials (intentional graves) and structural hearths inside huts. It also shows the **earliest evidence of human conflict/war** (a skeleton with a stone arrowhead embedded in its rib).</li><li><strong>Mahadaha:</strong> Famous for double burials (male and female buried together in the same grave) and ornaments made of bone and deer antlers (ear rings, necklaces).</li><li><strong>Damdama:</strong> Yielded 41 human graves, including a unique **triple burial** (three individuals in one grave) and several double burials.</li></ul></li><li><strong>Langhnaj (Gujarat):</strong> Provided microliths, animal bones, and 14 human skeletons, indicating a sandy dune hunting camp.</li></ul>"
            },
            {
                "title": "4. Neolithic Age (New Stone Age): 6,000 BC – 1,000 BC",
                "content": "<p>The Neolithic Age represents a massive socio-economic transformation in human history, famously termed the <strong>'Neolithic Revolution'</strong> by archaeologist V. Gordon Childe. Early humans transitioned from being nomadic food-gatherers to settled food-producers. The defining characteristics of this age are:</p><ol><li>Introduction of settled agriculture.</li><li>Domestication of animals on a large scale.</li><li>Invention of pottery (first hand-made, then wheel-made) to store surplus food.</li><li>Use of polished, ground stone tools (celts) with sharp cutting edges.</li><li>Discovery of the wheel for transport and pottery.</li></ol><h3>Crucial Neolithic Sites in India</h3><ul><li><strong>Mehrgarh (Balochistan, Pakistan):</strong> Located near the Bolan Pass. It is the **earliest Neolithic settlement** in the subcontinent, dating to ~7000 BC. It provides the earliest evidence of wheat and barley cultivation, sheep/goat domestication, and **the earliest cotton cultivation in the world**. It also has evidence of early dentistry (teeth drilled with flint drills).</li><li><strong>Burzahom (Kashmir):</strong> Meaning 'place of birch'. Famous for **pit-dwellings** (subterranean pits dug into the soil to protect against cold). Pit walls were plastered with mud and had post-holes for roofs. Burzahom is unique for the **burial of domestic dogs along with their masters** in human graves. Microliths are completely absent here.</li><li><strong>Gufkral (Kashmir):</strong> Meaning 'cave of the potter'. A major site showing pit-dwellings, bone tools, and a transition from a pre-ceramic to a ceramic neolithic phase.</li><li><strong>Lahuradewa (Sant Kabir Nagar, UP):</strong> Recent excavations have revolutionized prehistoric timelines. It has yielded the **earliest evidence of rice cultivation in the world**, dating back to ~9000 BC. This makes it older than both Koldihwa and Mehrgarh.</li><li><strong>Koldihwa (Belan Valley, UP):</strong> Long considered the oldest rice-growing site, Koldihwa yielded rice husks embedded in pottery clay dated to ~6000 BC.</li><li><strong>Chirand (Bihar):</strong> Located at the confluence of rivers, Chirand is remarkable for a **massive collection of bone tools made of deer antlers**, which is unique in Northern India outside Kashmir.</li><li><strong>Ash Mounds of South India:</strong> Neolithic sites like **Piklihal**, **Utnur**, **Kupgal**, **Kodekal**, and **Hallur** are famous for large Ash Mounds. These are heaps of accumulated cow dung that were ceremonially burnt, indicating pastoralism and cattle penning.</li></ul>"
            },
            {
                "title": "5. Chalcolithic Age (Copper-Stone Age): 3,000 BC – 500 BC",
                "content": """<p>The Chalcolithic Age marked the transition from the Stone Age to the Metal Age. **Copper** was the first metal used by humans, along with stone tools. These communities were primarily rural, unlike the contemporary urban Harappan Civilization (which was Bronze Age). They lived in mud-brick or wattle-and-daub houses and made painted pottery, especially **Black-and-Red Ware (BRW)**.</p><h3>Major Chalcolithic Cultures &amp; Sites</h3><div class="premium-table-container"><table class="premium-table"><thead><tr><th>Culture</th><th>Region &amp; Period</th><th>Key Features &amp; Discoveries</th><th>Major Sites</th></tr></thead><tbody><tr><td>Ahar-Banas Culture</td><td>SE Rajasthan<br>(~2100 BC – 1500 BC)</td><td>Exclusively copper tools, **complete absence of microliths**. Ahar is known as <em>Tambavati</em> (place of copper). Gilund has stone-blade industry and kiln-burnt bricks.</td><td>Ahar, Gilund, Balathal.</td></tr><tr><td>Kayatha Culture</td><td>Chambal Valley, MP<br>(~2400 BC – 2000 BC)</td><td>Mud houses, copper axes, beads of semi-precious stones (carnelian, steatite). Early contact with Harappans.</td><td>Kayatha.</td></tr><tr><td>Malwa Culture</td><td>Central India, MP<br>(~1700 BC – 1200 BC)</td><td>Rich, painted pottery. **Navdatoli** is the largest site, yielding the richest variety of food grains in prehistoric India (wheat, barley, rice, pulses, excavated by H.D. Sankalia).</td><td>Navdatoli, Eran, Nagda.</td></tr><tr><td>Jorwe Culture</td><td>Maharashtra<br>(~1400 BC – 700 BC)</td><td>Fortified settlements, child burials in urns under house floors. **Daimabad** is the largest site, famous for a hoard of Harappan-influenced bronze sculptures.</td><td>Daimabad, Inamgaon, Nevasa, Chandoli.</td></tr></tbody></table></div><h3>Key Social and Technological Insights</h3><ul><li><strong>Urn Burials &amp; High Infant Mortality:</strong> A large number of child burials in urns under the floors of houses (especially in the Jorwe culture) indicates high infant mortality and deep-seated burial customs.</li><li><strong>Burial Orientations:</strong> In Northern India, bodies were buried in a North-South orientation, while in Southern India, they were buried East-West.</li><li><strong>Daimabad Bronze Hoard:</strong> Discovered in 1974, this hoard includes four exquisite solid bronze figures: a chariot driven by a man, a rhinoceros, an elephant, and a buffalo. They are believed to be imports or late Harappan influences.</li><li><strong>Inamgaon (MH):</strong> A large, fortified Jorwe settlement with a granary, jetty, and houses arranged in a planned layout. Yielded evidence of mother goddess worship.</li></ul>"""
            },
            {
                "title": "6. Uttar Pradesh (UP) Special Focus & Megaliths",
                "content": "<p>For AHC RO/ARO and state-level exams, Uttar Pradesh's prehistoric sites hold massive weightage. The state features key sites from all prehistoric phases, demonstrating a rich and continuous evolution of early human cultures.</p>" + up_prehistoric_sites_svg + """<div class="premium-table-container"><table class="premium-table"><thead><tr><th>UP Site</th><th>District Location</th><th>Prehistoric Phase</th><th>Significance / Discoveries</th></tr></thead><tbody><tr><td>Belan Valley</td><td>Mirzapur / Sonbhadra / Prayagraj</td><td>Palaeolithic, Mesolithic, Neolithic</td><td>Continuous cultural sequence. Lohanda Nala bone Mother Goddess figurine (Palaeolithic). Excavated under G.R. Sharma.</td></tr><tr><td>Chopani Mando</td><td>Prayagraj (Belan Valley)</td><td>Mesolithic to Neolithic</td><td>Earliest evidence of handmade pottery in the world. Transition to settled life.</td></tr><tr><td>Koldihwa</td><td>Prayagraj (Belan Valley)</td><td>Neolithic to Chalcolithic</td><td>Pioneering evidence of rice cultivation (~6000 BC) in the form of grain husks embedded in pottery clay.</td></tr><tr><td>Lahuradewa</td><td>Sant Kabir Nagar</td><td>Neolithic</td><td style="font-weight: bold; color: #b03a2e;">Oldest rice cultivation in the world (~9000 BC). Pushed back Neolithic agriculture timelines in Asia.</td></tr><tr><td>Sarai Nahar Rai</td><td>Pratapgarh</td><td>Mesolithic</td><td>Earliest burials in India. Skeletons showing death by combat/embedded arrowheads. Hearths built inside circular huts.</td></tr><tr><td>Mahadaha</td><td>Pratapgarh</td><td>Mesolithic</td><td>Double burials (male-female buried together). Bone &amp; antler ornaments (necklaces, earrings).</td></tr><tr><td>Damdama</td><td>Pratapgarh</td><td>Mesolithic</td><td>41 burials. Unique triple burial (three skeletons in one grave), double burials, and intensive bone points.</td></tr></tbody></table></div><h3>Megalithic Burials &amp; Iron Age in South India</h3><p>While UP is rich in Stone and Copper age sites, Southern India transitioned from the Neolithic directly into the **Iron Age**, bypassing a major Chalcolithic phase. The Southern Iron Age is characterized by **Megaliths**—graves and memorials constructed using large boulders. Iron implements (daggers, arrowheads, sickles, lances) and Black-and-Red pottery were buried with the dead as grave goods. Key Megalithic sites include **Adichanallur** (TN), **Hire Benakal** (KA), and **Hallur** (KA).</p>"""
            }
        ]
    }
}

# ----------------- PRACTICE ZONE & MOCK TEST GENERATION (50 + 15 QUESTIONS) -----------------
practice_questions = [
    {
        "q": "Who is considered the Father of Indian Prehistory?",
        "opts": ["Sir Mortimer Wheeler", "Robert Bruce Foote", "Alexander Cunningham", "H.D. Sankalia"],
        "ans": 1,
        "sol": "Robert Bruce Foote discovered the first Paleolithic tool in India (a handaxe/cleaver) at Pallavaram near Chennai in 1863."
    },
    {
        "q": "Which of the following sites yielded the earliest hominid fossil in the Indian subcontinent?",
        "opts": ["Bhimbetka", "Hathnora", "Didwana", "Pallavaram"],
        "ans": 1,
        "sol": "The Narmada Human (Homo erectus) skull cap was found at Hathnora (Madhya Pradesh) by Arun Sonakia in 1982."
    },
    {
        "q": "Which site provides the earliest evidence of settled agriculture in the Indian subcontinent?",
        "opts": ["Mehrgarh", "Lahuradewa", "Koldihwa", "Burzahom"],
        "ans": 0,
        "sol": "Mehrgarh (Balochistan, Pakistan) dates back to ~7000 BC and represents the earliest Neolithic agricultural settlement in the subcontinent."
    },
    {
        "q": "Which of the following sites has yielded the earliest evidence of rice cultivation in the world?",
        "opts": ["Koldihwa", "Mehrgarh", "Lahuradewa", "Chopani Mando"],
        "ans": 2,
        "sol": "Recent excavations at Lahuradewa (Sant Kabir Nagar, UP) show rice cultivation dating to ~9000 BC, making it older than Koldihwa (~6000 BC)."
    },
    {
        "q": "Which phase of the Stone Age is widely characterized by the use of 'Microliths'?",
        "opts": ["Palaeolithic", "Mesolithic", "Neolithic", "Chalcolithic"],
        "ans": 1,
        "sol": "The Mesolithic Age is characterized by microliths, which are tiny, geometric stone tools under 5cm hafted to wood/bone handles."
    },
    {
        "q": "In which year did Robert Bruce Foote discover the first Palaeolithic tool in India?",
        "opts": ["1857", "1861", "1863", "1885"],
        "ans": 2,
        "sol": "Robert Bruce Foote discovered the first Palaeolithic tool at Pallavaram in May 1863."
    },
    {
        "q": "Who is known as the Father of Indian Archaeology?",
        "opts": ["John Marshall", "Alexander Cunningham", "Robert Bruce Foote", "Mortimer Wheeler"],
        "ans": 1,
        "sol": "Alexander Cunningham was the first Director-General of the Archaeological Survey of India (ASI) founded in 1861, and is the Father of Indian Archaeology."
    },
    {
        "q": "Which geographical valley in Uttar Pradesh shows a continuous sequence of Palaeolithic, Mesolithic, and Neolithic phases?",
        "opts": ["Soan Valley", "Belan Valley", "Narmada Valley", "Ganga Valley"],
        "ans": 1,
        "sol": "The Belan Valley (Mirzapur/Prayagraj region in UP) is famous for showing a continuous stratigraphic sequence of all three Stone Age phases."
    },
    {
        "q": "The carved bone Mother Goddess figurine (or bone harpoon) of the Upper Palaeolithic period was found at which UP site?",
        "opts": ["Sarai Nahar Rai", "Koldihwa", "Lohanda Nala", "Chopani Mando"],
        "ans": 2,
        "sol": "The bone Mother Goddess figurine was discovered in the Upper Palaeolithic layer at Lohanda Nala in the Belan Valley, UP."
    },
    {
        "q": "Which Mesolithic site in Uttar Pradesh is famous for yielding double burials (male and female in the same grave) and deer antler ornaments?",
        "opts": ["Sarai Nahar Rai", "Mahadaha", "Damdama", "Chopani Mando"],
        "ans": 1,
        "sol": "Mahadaha (Pratapgarh, UP) yielded double burials and personal ornaments made of bone and deer antler."
    },
    {
        "q": "At which Mesolithic site in UP did archaeologists discover a single grave containing three human skeletons buried together (triple burial)?",
        "opts": ["Sarai Nahar Rai", "Mahadaha", "Damdama", "Lahuradewa"],
        "ans": 2,
        "sol": "Damdama (Pratapgarh, UP) yielded 41 human graves, including one unique triple burial and several double burials."
    },
    {
        "q": "Which Neolithic site in Kashmir is famous for subterranean pit-dwellings and the practice of burying domestic dogs with their masters?",
        "opts": ["Gufkral", "Burzahom", "Martand", "Piklihal"],
        "ans": 1,
        "sol": "Burzahom (Kashmir) is famous for pit-dwellings and unique burials where domestic dogs were interred with their masters."
    },
    {
        "q": "Which Neolithic site in Bihar is highly unique for its rich assemblage of bone tools made of deer antlers?",
        "opts": ["Chirand", "Senuwar", "Taradih", "Chechar"],
        "ans": 0,
        "sol": "Chirand (Saran district, Bihar) is a Neolithic riverine site that yielded a massive collection of bone tools made from deer antlers."
    },
    {
        "q": "Which Palaeolithic cave site provides the earliest evidence of the use of fire in the form of ash deposits?",
        "opts": ["Bhimbetka", "Kurnool Caves", "Attirampakkam", "Hunsgi"],
        "ans": 1,
        "sol": "Kurnool Caves (Andhra Pradesh) contain thick ash deposits, indicating the earliest evidence of the use of fire by Palaeolithic humans."
    },
    {
        "q": "Bhimbetka rock shelters, famous for prehistoric cave paintings, were discovered in 1957 by whom?",
        "opts": ["H.D. Sankalia", "V.S. Wakankar", "Arun Sonakia", "Alexander Cunningham"],
        "ans": 1,
        "sol": "V.S. Wakankar discovered the Bhimbetka Caves in Madhya Pradesh in 1957."
    },
    {
        "q": "The largest Mesolithic site in India, which has yielded the earliest evidence of animal domestication on the Kothari River, is:",
        "opts": ["Bagor", "Adamgarh", "Langhnaj", "Sarai Nahar Rai"],
        "ans": 0,
        "sol": "Bagor (Rajasthan) on the Kothari River is the largest Mesolithic site in India and provides the earliest animal domestication evidence along with Adamgarh."
    },
    {
        "q": "Along with Bagor in Rajasthan, which site in Madhya Pradesh provides the earliest evidence of animal domestication?",
        "opts": ["Bhimbetka", "Adamgarh", "Hathnora", "Navdatoli"],
        "ans": 1,
        "sol": "Adamgarh (MP) and Bagor (Rajasthan) provide the earliest evidence of animal domestication in India, dating to around 5000 BC."
    },
    {
        "q": "Which site provides the earliest evidence of handmade pottery in the world, transitioning from Mesolithic to Neolithic?",
        "opts": ["Chopani Mando", "Koldihwa", "Lahuradewa", "Mehrgarh"],
        "ans": 0,
        "sol": "Chopani Mando (Belan Valley, UP) provides the earliest evidence of handmade pottery in the world."
    },
    {
        "q": "Ash Mounds found at Neolithic sites in South India (e.g., Piklihal, Utnur) represent:",
        "opts": ["Volcanic ash deposits from the Pleistocene", "Sites where human bodies were cremated", "Accumulated cow dung from cattle pens that was burnt", "Ruins of ancient industrial furnaces"],
        "ans": 2,
        "sol": "Ash mounds represent accumulated cow dung heaps from Neolithic cattle pens that were ceremonially burnt."
    },
    {
        "q": "Which was the first metal to be used by humans in the Indian subcontinent?",
        "opts": ["Gold", "Bronze", "Copper", "Iron"],
        "ans": 2,
        "sol": "Copper was the first metal used by humans in the Indian subcontinent, marking the start of the Chalcolithic period."
    },
    {
        "q": "The Ahar Chalcolithic culture of Rajasthan is also known as what due to the abundance of copper tools and lack of microliths?",
        "opts": ["Tambavati", "Kunchi", "Lohagaon", "Kanchipuram"],
        "ans": 0,
        "sol": "Ahar is known as Tambavati (place of copper) because copper was abundant and stone tools were completely absent."
    },
    {
        "q": "Which is the largest site of the Jorwe culture in Maharashtra, famous for its bronze hoard containing a chariot, rhino, and elephant?",
        "opts": ["Inamgaon", "Daimabad", "Nevasa", "Chandoli"],
        "ans": 1,
        "sol": "Daimabad is the largest Jorwe site and is famous for a spectacular hoard of solid bronze sculptures found in 1974."
    },
    {
        "q": "The Daimabad bronze hoard consists of solid bronze sculptures of which animals?",
        "opts": ["Lion, Tiger, Leopard", "Elephant, Rhinoceros, Buffalo, and a Chariot", "Bull, Horse, Deer", "Cow, Goat, Sheep"],
        "ans": 1,
        "sol": "The Daimabad hoard includes four bronze figures: a chariot driven by a man, a rhinoceros, an elephant, and a buffalo."
    },
    {
        "q": "Which Chalcolithic site excavated by H.D. Sankalia has yielded the richest variety of food grains in prehistoric India?",
        "opts": ["Navdatoli", "Inamgaon", "Kayatha", "Ahar"],
        "ans": 0,
        "sol": "Navdatoli (on the Narmada in MP) yielded the richest variety of food grains (wheat, barley, rice, pulses, lentils) of any Chalcolithic site."
    },
    {
        "q": "Skeletons showing evidence of conflict and death by stone arrowheads embedded in bones were found at which UP Mesolithic site?",
        "opts": ["Sarai Nahar Rai", "Mahadaha", "Damdama", "Koldihwa"],
        "ans": 0,
        "sol": "Sarai Nahar Rai (Pratapgarh, UP) provides the earliest archaeological evidence of human conflict/warfare in India."
    },
    {
        "q": "Geologically, the Palaeolithic Age in India developed during which epoch?",
        "opts": ["Pliocene", "Pleistocene", "Holocene", "Miocene"],
        "ans": 1,
        "sol": "The Palaeolithic Age developed during the Pleistocene epoch (Ice Age), while the Mesolithic marks the start of the Holocene."
    },
    {
        "q": "The Mesolithic Age coincides with the onset of which warm geological epoch?",
        "opts": ["Pleistocene", "Holocene", "Oligocene", "Eocene"],
        "ans": 1,
        "sol": "The Mesolithic Age coincides with the post-glacial Holocene epoch, which brought a warmer and wetter climate."
    },
    {
        "q": "Palaeolithic humans are often referred to as 'Quartzite Men' because:",
        "opts": ["They wore clothes made of quartz crystals", "They worshipped quartzite stones as deities", "They primarily used quartzite stone for making tools", "They lived exclusively in quartzite mines"],
        "ans": 2,
        "sol": "They are called 'Quartzite Men' because they used tough quartzite stone for making their crude, unpolished stone tools."
    },
    {
        "q": "Which site in Madhya Pradesh yielded a stone platform shrine with a triangular stone, considered the oldest prehistoric shrine in India?",
        "opts": ["Bhimbetka", "Baghor I", "Adamgarh", "Hathnora"],
        "ans": 1,
        "sol": "Baghor I in the Son Valley (MP) revealed a stone platform shrine with a triangular stone, dating to ~10,000 BC (Upper Palaeolithic/Mesolithic transition)."
    },
    {
        "q": "Patne in Maharashtra is highly significant in Indian prehistory because it yielded:",
        "opts": ["The earliest evidence of iron smelting", "Fragments of engraved ostrich eggshells and beads", "A complete skeleton of Homo sapiens", "The oldest polished stone axes"],
        "ans": 1,
        "sol": "Patne yielded fragments of engraved ostrich eggshells and beads, proving artistic expression in the Upper Palaeolithic."
    },
    {
        "q": "Who coined the term 'Neolithic Revolution' to describe the radical transition to agriculture and settled life?",
        "opts": ["V. Gordon Childe", "Mortimer Wheeler", "John Lubbock", "Robert Bruce Foote"],
        "ans": 0,
        "sol": "Australian archaeologist V. Gordon Childe coined the term 'Neolithic Revolution' in his book 'Man Makes Himself'."
    },
    {
        "q": "The name of which Neolithic site in Kashmir translates to the 'place of birch'?",
        "opts": ["Gufkral", "Burzahom", "Pampore", "Anantnag"],
        "ans": 1,
        "sol": "Burzahom in Kashmiri translates to the 'place of birch', referencing the birch trees whose bark was used by pit-dwellers."
    },
    {
        "q": "The name of which Kashmir Neolithic site translates to the 'cave of the potter'?",
        "opts": ["Burzahom", "Gufkral", "Martand", "Harwan"],
        "ans": 1,
        "sol": "Gufkral translates to the 'cave of the potter' (Guf = Cave, Kral = Potter)."
    },
    {
        "q": "At which of the following Neolithic sites are South Indian 'Ash Mounds' NOT found?",
        "opts": ["Piklihal", "Utnur", "Kupgal", "Chirand"],
        "ans": 3,
        "sol": "Chirand is a Neolithic site in Bihar, whereas ash mounds are strictly located in South Indian pastoral neolithic sites."
    },
    {
        "q": "The Chalcolithic communities in India were primarily:",
        "opts": ["Urban and trading civilizations", "Nomadic pastoralists only", "Rural farming communities", "Forest hunter-gatherers"],
        "ans": 2,
        "sol": "Unlike the urban Harappan Bronze Age, Chalcolithic cultures (Ahar, Jorwe, Malwa) were rural farming communities."
    },
    {
        "q": "Which type of pottery is most diagnostic and characteristic of the Chalcolithic period?",
        "opts": ["Ochre Coloured Pottery (OCP)", "Painted Grey Ware (PGW)", "Black-and-Red Ware (BRW)", "Northern Black Polished Ware (NBPW)"],
        "ans": 2,
        "sol": "Painted Black-and-Red Ware (BRW) is the most characteristic pottery type of the Chalcolithic period."
    },
    {
        "q": "In Northern India, Chalcolithic graves show that the dead were buried in which orientation?",
        "opts": ["East-West", "North-South", "West-East", "South-North"],
        "ans": 1,
        "sol": "In Northern India, particularly Maharashtra (Jorwe), the dead were buried in a North-South orientation."
    },
    {
        "q": "In South India, the Iron Age is distinguished by which type of archaeological remains?",
        "opts": ["Painted Grey Ware houses", "Megalithic burials marked by large stones", "Terracotta temples", "Burnt brick cities"],
        "ans": 1,
        "sol": "In South India, the Iron Age is characterized by Megaliths, which are large stone circles or tables marking burial chambers."
    },
    {
        "q": "Which site in Karnataka is a UNESCO heritage candidate famous for its vast field of megalithic dolmens?",
        "opts": ["Hire Benakal", "Brahmagiri", "Maski", "Hallur"],
        "ans": 0,
        "sol": "Hire Benakal in Karnataka is famous for its hundreds of megalithic dolmens and portal chambers."
    },
    {
        "q": "Who deciphered the Ashokan Brahmi script in 1837, establishing the first firm baseline for historical records in India?",
        "opts": ["William Jones", "James Prinsep", "Alexander Cunningham", "Max Muller"],
        "ans": 1,
        "sol": "James Prinsep deciphered the Brahmi script in 1837 while serving as an officer in the Calcutta Mint."
    },
    {
        "q": "Which tool type is completely absent in the Lower Palaeolithic phase?",
        "opts": ["Handaxe", "Cleaver", "Chopper", "Microlith"],
        "ans": 3,
        "sol": "Microliths belong to the Mesolithic phase; they did not exist in the Lower Palaeolithic."
    },
    {
        "q": "The Soanian culture of pebble tools flourished in which river valley?",
        "opts": ["Indus River Valley", "Soan River Valley (tributary of Indus)", "Son River Valley (tributary of Ganga)", "Belan River Valley"],
        "ans": 1,
        "sol": "The Soanian culture flourished in the valley of the Soan River (now in Pakistan), characterized by pebble choppers."
    },
    {
        "q": "The Nevasan culture of Middle Palaeolithic flake tools is named after the type site Nevasa on which river?",
        "opts": ["Narmada", "Pravara (tributary of Godavari)", "Krishna", "Tapi"],
        "ans": 1,
        "sol": "Nevasa is located on the Pravara River, a tributary of the Godavari in Maharashtra."
    },
    {
        "q": "In which year was the famous Narmada Human skull cap discovered at Hathnora?",
        "opts": ["1957", "1974", "1982", "1991"],
        "ans": 2,
        "sol": "The Narmada Human skull cap was discovered by Arun Sonakia on 5th December 1982."
    },
    {
        "q": "The earliest evidence of cotton cultivation in the world, dating to ~5000 BC, comes from:",
        "opts": ["Mehrgarh", "Harappa", "Mohenjo-daro", "Koldihwa"],
        "ans": 0,
        "sol": "Mehrgarh in Balochistan provides the earliest evidence of cotton cultivation in the world."
    },
    {
        "q": "Which Mesolithic site in Gujarat yielded microliths, wild animal bones, and 14 human skeletons?",
        "opts": ["Langhnaj", "Lothal", "Rangpur", "Rojdi"],
        "ans": 0,
        "sol": "Langhnaj (Mehsana district, Gujarat) is a key Mesolithic site that yielded microliths and human skeletal remains."
    },
    {
        "q": "Under which Director-General did the Archaeological Survey of India introduce the scientific stratigraphy system?",
        "opts": ["John Marshall", "Mortimer Wheeler", "Alexander Cunningham", "James Burgess"],
        "ans": 1,
        "sol": "Sir Mortimer Wheeler introduced the stratigraphic system of excavation to ASI in 1944."
    },
    {
        "q": "In which year was the Archaeological Survey of India (ASI) formally established?",
        "opts": ["1857", "1861", "1885", "1904"],
        "ans": 1,
        "sol": "The ASI was established in 1861 during the viceroyalty of Lord Canning, with Alexander Cunningham as Surveyor."
    },
    {
        "q": "Which site in Maharashtra provides the earliest accepted evidence of human presence (~1.4 million years ago) in the subcontinent?",
        "opts": ["Nevasa", "Bori", "Daimabad", "Inamgaon"],
        "ans": 1,
        "sol": "Bori in Pune district, Maharashtra, provides the earliest accepted evidence of human presence in India."
    },
    {
        "q": "The prehistoric cave paintings at Bhimbetka primarily belong to which Stone Age phase?",
        "opts": ["Lower Palaeolithic", "Mesolithic", "Neolithic", "Iron Age"],
        "ans": 1,
        "sol": "Although Bhimbetka paintings span multiple periods, the majority of the prehistoric rock art belongs to the Mesolithic period."
    }
]

mock_questions = [
    {
        "q": "Consider the following statements regarding the historiography of Pre-historic India:\n1. Robert Bruce Foote discovered the first Palaeolithic tool in India at Pallavaram in 1863.\n2. Alexander Cunningham was the first Director-General of the Archaeological Survey of India.\n3. V.S. Wakankar discovered the Bhimbetka Caves in 1957.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "All three statements are correct. Foote discovered the Pallavaram handaxe in 1863; Cunningham was the first D-G of ASI; Wakankar discovered Bhimbetka in 1957."
    },
    {
        "q": "Which of the following pairs of prehistoric sites and discoveries is/are correctly matched?\n1. Hathnora - Earliest hominid fossil in India\n2. Kurnool Caves - Earliest evidence of fire\n3. Patne - Engraved ostrich eggshells\nSelect the correct answer:",
        "opts": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "All three pairs are correct. Hathnora yielded the Narmada Human fossil; Kurnool Caves yielded ash deposits (fire); Patne yielded engraved ostrich eggshells."
    },
    {
        "q": "Consider the following statements regarding the Mesolithic sites in Uttar Pradesh:\n1. Sarai Nahar Rai yielded the earliest evidence of war/conflict.\n2. Mahadaha is known for double burials and bone ornaments.\n3. Damdama yielded a grave containing three human skeletons buried together.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "All three statements are correct. These Pratapgarh sites are key Mesolithic records: Sarai Nahar Rai (conflict), Mahadaha (double burials/antler ornaments), Damdama (triple burial)."
    },
    {
        "q": "With reference to the Neolithic Age in India, consider the following statements:\n1. Mehrgarh represents the earliest agricultural settlement in Balochistan.\n2. Burzahom is famous for pit-dwellings and burying dogs with masters.\n3. Lahuradewa has pushed back the earliest date of rice cultivation in the world to ~9000 BC.\nWhich of the statements given above is/are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1, 2, and 3", "3 only"],
        "ans": 2,
        "sol": "All three statements are correct. Lahuradewa (~9000 BC) is older than Koldihwa (~6000 BC) and Mehrgarh (~7000 BC)."
    },
    {
        "q": "What is the correct chronological sequence of the following pre-historic phases in India?\n1. Palaeolithic\n2. Neolithic\n3. Chalcolithic\n4. Mesolithic\n5. Iron Age\nSelect the correct code:",
        "opts": ["1 - 2 - 4 - 3 - 5", "1 - 4 - 2 - 3 - 5", "1 - 4 - 3 - 2 - 5", "4 - 1 - 2 - 3 - 5"],
        "ans": 1,
        "sol": "The correct sequence is Palaeolithic ➔ Mesolithic ➔ Neolithic ➔ Chalcolithic ➔ Iron Age (1-4-2-3-5)."
    },
    {
        "q": "Which of the following Chalcolithic cultures is correctly matched with its geographical region?\n1. Ahar Culture - Southeast Rajasthan\n2. Jorwe Culture - Maharashtra\n3. Malwa Culture - Central India (MP)\nSelect the correct answer:",
        "opts": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "All three matches are correct: Ahar (Rajasthan), Jorwe (Maharashtra), Malwa (Madhya Pradesh/Central India)."
    },
    {
        "q": "Consider the following statements regarding the Chalcolithic period:\n1. Copper was the first metal to be used alongside stone tools.\n2. The Ahar culture is characterized by a complete absence of microliths.\n3. Daimabad is the largest Jorwe site, famous for a hoard of bronze sculptures.\nWhich of the statements given above is/are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1, 2, and 3", "1 and 3 only"],
        "ans": 2,
        "sol": "All statements are correct. Copper was the first metal used; Ahar (Tambavati) had no microliths; Daimabad is the largest Jorwe site and yielded the bronze hoard."
    },
    {
        "q": "Assertion (A): The Neolithic period is often described as the 'Neolithic Revolution'.\nReason (R): It marked a radical transition from a nomadic food-gathering lifestyle to a settled food-producing (agricultural) lifestyle.\nSelect the correct code:",
        "opts": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The shift to agriculture and settled life is the direct reason why V. Gordon Childe termed it a 'Revolution'."
    },
    {
        "q": "Which of the following Neolithic sites is famous for 'Ash Mounds' formed by burnt cow dung heaps?\n1. Piklihal\n2. Utnur\n3. Kupgal\n4. Chopani Mando\nSelect the correct answer:",
        "opts": ["1 and 2 only", "1, 2, and 3 only", "3 and 4 only", "1, 2, 3, and 4"],
        "ans": 1,
        "sol": "Piklihal, Utnur, and Kupgal are South Indian pastoral Neolithic sites with ash mounds. Chopani Mando is a UP site famous for early pottery, not ash mounds."
    },
    {
        "q": "Consider the following statements regarding burial practices in pre-historic India:\n1. In Chalcolithic Maharashtra, children were buried in urns under house floors.\n2. In Northern India, graves were generally oriented North-South.\n3. In Southern India, Megalithic graves were generally oriented East-West.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "All three statements are correct. Child urn burials under house floors were common in Jorwe culture; North India oriented graves North-South; South India oriented them East-West."
    },
    {
        "q": "Which UP-specific site has yielded the earliest evidence of pottery in the world, dating to the transition between Mesolithic and Neolithic?\n1. Sarai Nahar Rai\n2. Chopani Mando\n3. Koldihwa\n4. Lahuradewa\nSelect the correct answer:",
        "opts": ["1 only", "2 only", "3 only", "4 only"],
        "ans": 1,
        "sol": "Chopani Mando in the Belan Valley, UP, yielded the oldest handmade pottery in the world, representing the Mesolithic-Neolithic transition."
    },
    {
        "q": "Assertion (A): Palaeolithic humans in India are often referred to as 'Quartzite Men'.\nReason (R): They lived in shelters made of pure quartzite minerals.\nSelect the correct code:",
        "opts": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"],
        "ans": 2,
        "sol": "The Assertion is true, but the Reason is false because they are called 'Quartzite Men' because they made their stone tools out of quartzite, not because they lived in pure quartzite shelters."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding the Upper Palaeolithic shrine at Baghor I:\n1. It is located in the Son Valley of Madhya Pradesh.\n2. It features a circular stone platform with a triangular stone in the center.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Baghor I (MP) features a circular stone platform with a triangular stone in the center, representing the earliest prehistoric shrine."
    },
    {
        "q": "The Megalithic culture of South India is primarily characterized by burials marked by large stones. Which of the following is/are Megalithic burial types?\n1. Cists (stone coffins)\n2. Dolmens (stone tables)\n3. Menhirs (single standing stones)\nSelect the correct answer:",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "Cists, Dolmens, and Menhirs are all common Megalithic burial types found in South India."
    },
    {
        "q": "Consider the following statements:\nStatement I: The first Palaeolithic tool in India was discovered by Alexander Cunningham at Pallavaram.\nStatement II: Robert Bruce Foote was a British geologist who is called the Father of Indian Prehistory.\nWhich of the following is correct?",
        "opts": ["Statement I is correct but Statement II is incorrect", "Statement II is correct but Statement I is incorrect", "Both Statement I and Statement II are correct", "Both Statement I and Statement II are incorrect"],
        "ans": 1,
        "sol": "Statement I is incorrect because the first Palaeolithic tool at Pallavaram was discovered by Robert Bruce Foote, not Alexander Cunningham. Statement II is correct."
    }
]

# Save practice.json
practice_data = {
    "practiceQuestions": practice_questions,
    "mockTestQuestions": mock_questions
}
processed_practice = process_data(practice_data)
with open(os.path.join(BASE_DIR, "practice.json"), "w", encoding="utf-8") as f:
    json.dump(processed_practice, f, ensure_ascii=False, indent=4)

print("practice.json generated and processed successfully.")

# ----------------- SECTION MASTERY ZONE GENERATION (mastery.json) -----------------
# We will create 12 distinct, high-quality questions for each of the 6 sections
# representing MCQ, Multiple Correct MCQ, True/False, Fill in the Blank, Match the Following,
# One-Liner, Assertion-Reason, Statement-Based, Why, How, Case Study, and Teach the Concept.

# Section 1: Historiography, Pioneers & Classifications
sec1_questions = [
    {
        "type": "MCQ",
        "q": "Who is the Father of Indian Prehistory?",
        "opts": ["Alexander Cunningham", "Robert Bruce Foote", "John Marshall", "Mortimer Wheeler"],
        "ans": 1,
        "sol": "Robert Bruce Foote discovered the first Palaeolithic tool in India (a handaxe/cleaver) at Pallavaram near Chennai in May 1863, earning him this title."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following pioneers are correctly matched with their discoveries? (Select all that apply)",
        "opts": [
            "Robert Bruce Foote - First Palaeolithic tool (Pallavaram)",
            "V.S. Wakankar - Bhimbetka Caves (1957)",
            "Arun Sonakia - Narmada Human Homo erectus skull cap (1982)",
            "Alexander Cunningham - Decipherment of Ashokan Brahmi (1837)"
        ],
        "ans": [0, 1, 2],
        "sol": "Foote, Wakankar, and Sonakia are correctly matched. James Prinsep deciphered the Brahmi script in 1837; Alexander Cunningham was the first Director-General of ASI."
    },
    {
        "type": "True/False",
        "q": "True or False: Alexander Cunningham was the first Director-General of the Archaeological Survey of India (ASI) in 1861.",
        "ans": True,
        "sol": "Alexander Cunningham was appointed as the first Archaeological Surveyor and later became the first Director-General of the ASI."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The historical phase for which written records exist but are not yet deciphered (e.g., the Harappan script) is classified as ________.",
        "ans": "Protohistory",
        "sol": "Protohistory refers to the period between prehistory and history where writing is present but cannot yet be read."
    },
    {
        "type": "Match the Following",
        "q": "Match the pioneers with their key contribution to Indian archaeology:",
        "items": [
            {"left": "I. Robert Bruce Foote", "key": "A"},
            {"left": "II. Sir Mortimer Wheeler", "key": "B"},
            {"left": "III. James Prinsep", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Father of Indian Prehistory"},
            {"val": "B", "text": "Introduced stratigraphic system in Indian excavations"},
            {"val": "C", "text": "Deciphered the Brahmi script in 1837"}
        ],
        "sol": "Foote (I-A), Wheeler (II-B), Prinsep (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Identify the historical phase described: The period during which written records are available and fully deciphered.",
        "sol": "Historical Period."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Vedic Period is categorized under Protohistory.<br><strong>Reason (R):</strong> The Vedic texts were preserved orally for centuries through Sruti tradition and lack contemporary deciphered written archaeological records.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are correct. The Vedic period is protohistoric because direct contemporary deciphered writing is absent, relying on oral texts and indirect archaeology."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: H.D. Sankalia is considered the pioneer of modern scientific prehistoric archaeology in India, having excavated Langhnaj and Navdatoli.<br>Statement II: The Archaeological Survey of India (ASI) was established during the Viceroyalty of Lord Curzon.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because the ASI was established in 1861 under Lord Canning, not Curzon (though Curzon passed the Ancient Monuments Preservation Act in 1904)."
    },
    {
        "type": "Why",
        "q": "Why is Robert Bruce Foote's discovery in 1863 considered the starting point of Indian prehistory?",
        "sol": "Because it was the first time an actual Palaeolithic stone tool (Acheulean handaxe/cleaver) was discovered in situ in India, proving the existence of prehistoric humans in the subcontinent."
    },
    {
        "type": "How",
        "q": "How does protohistory differ from prehistory and history in the Indian context?",
        "sol": "Prehistory has zero written records (Stone Age); Protohistory has writing that is undeciphered (Indus Valley) or lack of written records despite advanced culture (Vedic); History begins with deciphered writing (Ashokan Brahmi, ~3rd Century BC)."
    },
    {
        "type": "Case Study",
        "q": "An archaeologist discovers a new site containing advanced metal objects, settled houses, and clay seals with pictographic symbols that no scholar can read. Determine the cultural phase of this site.",
        "sol": "The site belongs to Protohistory, because it contains writing (pictographs) that remains undeciphered, similar to the Indus Valley Civilization."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the significance of Sir Mortimer Wheeler's introduction of the stratigraphic method of excavation to the Archaeological Survey of India.",
        "sol": "Wheeler replaced arbitrary horizontal digging with stratigraphy (excavating layer by layer based on soil changes). This allowed archaeologists to date artifacts relatively based on their layer, ensuring that older items at lower layers were not mixed with newer items at upper layers."
    }
]

# Section 2: Palaeolithic Age
sec2_questions = [
    {
        "type": "MCQ",
        "q": "The only pre-Homo sapiens human fossil found in the entire Indian subcontinent is the Narmada Human, representing which hominid species?",
        "opts": ["Homo habilis", "Homo erectus", "Homo sapiens neanderthalensis", "Australopithecus"],
        "ans": 1,
        "sol": "The Narmada Human skull cap found at Hathnora represents the species Homo erectus."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following discoveries are correctly associated with their respective Palaeolithic sites? (Select all that apply)",
        "opts": [
            "Kurnool Caves - Ash deposits indicating fire use",
            "Lohanda Nala - Bone Mother Goddess figurine",
            "Patne - Engraved ostrich eggshells and beads",
            "Didwana - Domesticated wheat grains"
        ],
        "ans": [0, 1, 2],
        "sol": "Kurnool (fire/ash), Lohanda Nala (bone Mother Goddess), and Patne (ostrich shells) are correct Palaeolithic discoveries. Didwana is a Palaeolithic stone tool site; agriculture did not exist."
    },
    {
        "type": "True/False",
        "q": "True or False: The Bori site in Pune district, Maharashtra, is considered to provide the earliest accepted evidence of human presence in India, dating back to approximately 1.4 million years ago.",
        "ans": True,
        "sol": "Bori has yielded Lower Palaeolithic stone tools in a tuff layer dated to ~1.4 Ma, marking the earliest accepted human presence in the subcontinent."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: Palaeolithic humans in India are often called ________ Men because they made their unpolished tools primarily out of this specific type of rock.",
        "ans": "Quartzite",
        "sol": "They are called 'Quartzite Men' due to their exclusive reliance on quartzite stone for heavy core tools."
    },
    {
        "type": "Match the Following",
        "q": "Match the Palaeolithic phases with their characteristic stone tool technology:",
        "items": [
            {"left": "I. Lower Palaeolithic", "key": "A"},
            {"left": "II. Middle Palaeolithic", "key": "B"},
            {"left": "III. Upper Palaeolithic", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Core tools (Handaxes, Cleavers, Choppers)"},
            {"val": "B", "text": "Flake tools (Scrapers, Borers, Points)"},
            {"val": "C", "text": "Blade and Burin tools (emergence of Homo sapiens)"}
        ],
        "sol": "Lower (I-A), Middle (II-B), Upper (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Name the Upper Palaeolithic site in the Son Valley, Madhya Pradesh, which has yielded a circular stone platform with a triangular stone, interpreted as the earliest shrine in India.",
        "sol": "Baghor I."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> Middle Palaeolithic tools are called flake tools.<br><strong>Reason (R):</strong> They were manufactured by knocking off small pieces (flakes) from a parent core stone, which were then retouched into scrapers and borers.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The flake technology is characterized by using flakes chipped off a core stone, which explains why they are called flake tools."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: The Palaeolithic Age in India developed entirely during the Pleistocene epoch (Ice Age).<br>Statement II: The first evidence of the use of fire in the subcontinent comes from the Bhimbetka caves in Madhya Pradesh.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because the earliest ash/fire deposits were found in the Kurnool Caves in Andhra Pradesh, not Bhimbetka."
    },
    {
        "type": "Why",
        "q": "Why did Palaeolithic humans live in caves and rock shelters rather than open plains?",
        "sol": "Because the Pleistocene Ice Age was characterized by extreme cold and dry conditions. Caves and rock shelters (like Bhimbetka) provided natural protection from severe weather, wild predators, and cold winds."
    },
    {
        "type": "How",
        "q": "How did tool technology evolve from the Lower Palaeolithic to the Upper Palaeolithic?",
        "sol": "Lower Palaeolithic utilized heavy pebble core tools (handaxes, cleavers). Middle Palaeolithic saw a shift to lighter flake tools (scrapers, borers) chipped off a core. Upper Palaeolithic refined this into long, narrow blade-and-burin tools alongside bone implements."
    },
    {
        "type": "Case Study",
        "q": "Archaeologists excavating a cave in Southern India discover a thick layer of consolidated ash. Analyze what this indicates about the residents of the cave.",
        "sol": "The presence of a thick ash layer (similar to Kurnool Caves) indicates that the Palaeolithic residents had mastered the use of fire for warmth, cooking food, and warding off wild beasts."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the significance of the Narmada Human discovery at Hathnora.",
        "sol": "Discovered by Arun Sonakia in 1982, the Hathnora fossil (a skull cap) belongs to Homo erectus (Narmada Human). It is the oldest and only human ancestor fossil discovered in India, proving that Homo erectus inhabited the Narmada Valley during the Middle Pleistocene."
    }
]

# Section 3: Mesolithic Age
sec3_questions = [
    {
        "type": "MCQ",
        "q": "Which Mesolithic site in India, located on the Kothari River in Rajasthan, is the largest Mesolithic site and provides the earliest animal domestication evidence?",
        "opts": ["Adamgarh", "Bagor", "Langhnaj", "Sarai Nahar Rai"],
        "ans": 1,
        "sol": "Bagor in Rajasthan is the largest Mesolithic site in India, yielding early animal domestication evidence along with Adamgarh."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following Mesolithic sites in Uttar Pradesh are associated with the Pratapgarh district? (Select all that apply)",
        "opts": [
            "Sarai Nahar Rai",
            "Mahadaha",
            "Damdama",
            "Chopani Mando"
        ],
        "ans": [0, 1, 2],
        "sol": "Sarai Nahar Rai, Mahadaha, and Damdama are Mesolithic sites in Pratapgarh. Chopani Mando is in Prayagraj district."
    },
    {
        "type": "True/False",
        "q": "True or False: Chopani Mando in the Belan Valley has yielded the earliest evidence of handmade pottery in the world, dating to the Mesolithic-Neolithic transition.",
        "ans": True,
        "sol": "Chopani Mando provides the earliest evidence of handmade pottery, marking the transition towards food storage."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The tiny, sharp geometric stone tools (usually less than 5cm) that define the Mesolithic period are called ________.",
        "ans": "Microliths",
        "sol": "Microliths are the defining tool category of the Mesolithic Age."
    },
    {
        "type": "Match the Following",
        "q": "Match the Mesolithic sites with their unique archaeological feature:",
        "items": [
            {"left": "I. Sarai Nahar Rai", "key": "A"},
            {"left": "II. Mahadaha", "key": "B"},
            {"left": "III. Damdama", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Earliest graves and hearths inside huts; skeleton with embedded arrowhead"},
            {"val": "B", "text": "Double burials and bone antler ornaments"},
            {"val": "C", "text": "41 burials, including one unique triple burial"}
        ],
        "sol": "Sarai Nahar Rai (I-A), Mahadaha (II-B), Damdama (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Along with Bagor in Rajasthan, which Mesolithic site in Madhya Pradesh yielded the earliest evidence of animal domestication?",
        "sol": "Adamgarh."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Mesolithic Age witnessed a transition from hunting large animals to hunting smaller game, birds, and fish.<br><strong>Reason (R):</strong> The Holocene epoch brought a warmer and wetter climate, leading to the disappearance of Ice Age megafauna and an increase in small, fast animals.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are true. The climatic shift to Holocene warming altered the fauna, which necessitated microlithic projectile weapons for small game."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Skeletons found at Sarai Nahar Rai indicate the earliest archaeological evidence of human warfare in India.<br>Statement II: Langhnaj in Gujarat has yielded microliths, wild animal bones, and several human skeletons.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 2,
        "sol": "Both statements are correct. Sarai Nahar Rai has a skeleton with an embedded arrowhead (warfare), and Langhnaj is a key Mesolithic site in Gujarat with human remains."
    },
    {
        "type": "Why",
        "q": "Why were microliths hafted onto bone or wooden shafts instead of being used directly by hand?",
        "sol": "Because microliths were extremely small (under 5cm). Hafting them onto wooden or bone handles allowed humans to create highly effective composite tools like arrows, spears, and sickles for hunting small, fast animals from a distance."
    },
    {
        "type": "How",
        "q": "How did the burial practice at Damdama differ from that of Mahadaha?",
        "sol": "While both Pratapgarh sites show double burials, Damdama is unique for containing a triple burial (three individuals in one grave), representing a distinct mortuary event among its 41 graves."
    },
    {
        "type": "Case Study",
        "q": "During excavations of a Mesolithic layer at Pratapgarh, an archaeologist finds a grave containing two skeletons side by side, wearing rings and necklaces made of polished deer antler. Identify the most likely site.",
        "sol": "The site is Mahadaha, which is famous for its double burials and unique ornaments made of bone and deer antlers."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the ecological reasons that triggered the shift from the Palaeolithic to the Mesolithic lifestyle in India.",
        "sol": "Around 10,000 BC, the transition from the Pleistocene (Ice Age) to the Holocene brought warmer, wetter climates. Glaciers retreated, forests expanded, and giant Ice Age mammals were replaced by smaller, swifter animals. Humans had to adapt by making smaller, composite tools (microliths) and domesticating animals, transitioning towards a settled life."
    }
]

# Section 4: Neolithic Age
sec4_questions = [
    {
        "type": "MCQ",
        "q": "Which Neolithic site in India has yielded the oldest evidence of rice cultivation in the world, dating to ~9000 BC?",
        "opts": ["Koldihwa", "Mehrgarh", "Lahuradewa", "Chirand"],
        "ans": 2,
        "sol": "Lahuradewa (Sant Kabir Nagar, UP) has yielded rice grains dating back to ~9000 BC, pushing back Koldihwa's date (~6000 BC)."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following Neolithic features are associated with Burzahom in Kashmir? (Select all that apply)",
        "opts": [
            "Pit-dwellings dug into the soil with post-holes for roofs",
            "Burial of domestic dogs along with their masters",
            "Coarse grey pottery and complete absence of microliths",
            "Vast fields of ash mounds from cow dung burning"
        ],
        "ans": [0, 1, 2],
        "sol": "Burzahom is famous for pit-dwellings, dog burials, and lack of microliths. Ash mounds are found in South Indian Neolithic sites, not Kashmir."
    },
    {
        "type": "True/False",
        "q": "True or False: Mehrgarh in Balochistan is the earliest known Neolithic agricultural settlement in the Indian subcontinent, dating back to ~7000 BC.",
        "ans": True,
        "sol": "Mehrgarh is the oldest Neolithic agricultural settlement, showing early wheat, barley, and cotton cultivation."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The Neolithic site of Chirand, famous for a massive assemblage of bone tools made of deer antlers, is located in the state of ________.",
        "ans": "Bihar",
        "sol": "Chirand is located in the Saran district of Bihar."
    },
    {
        "type": "Match the Following",
        "q": "Match the Neolithic sites with their unique discovery:",
        "items": [
            {"left": "I. Burzahom", "key": "A"},
            {"left": "II. Piklihal", "key": "B"},
            {"left": "III. Lahuradewa", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Subterranean pit-dwellings and dog burials"},
            {"val": "B", "text": "Ash mounds from cattle penning"},
            {"val": "C", "text": "Earliest rice cultivation in the world (~9000 BC)"}
        ],
        "sol": "Burzahom (I-A), Piklihal (II-B), Lahuradewa (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "What name did V. Gordon Childe give to the transition of humans from food-gatherers to food-producers during the Neolithic period?",
        "sol": "Neolithic Revolution."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> South Indian Neolithic sites like Piklihal and Utnur are famous for Ash Mounds.<br><strong>Reason (R):</strong> The Neolithic pastoralists accumulated cow dung inside cattle pens and periodically set it on fire, creating massive mounds of ash.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The Ash Mounds were formed by the ceremonial burning of accumulated cow dung in pastoral cattle pens."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Mehrgarh provides the earliest evidence of cotton cultivation in the world, dating to ~5000 BC.<br>Statement II: Gufkral is a major Neolithic site in Kashmir whose name translates to the 'place of birch'.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because Gufkral means 'cave of the potter'; Burzahom is the site that translates to 'place of birch'."
    },
    {
        "type": "Why",
        "q": "Why is the invention of pottery considered a key feature of the Neolithic Revolution?",
        "sol": "Because the development of agriculture produced a surplus of grains. Humans needed durable, pest-proof containers to store the surplus harvest, leading to the invention of clay pottery (first handmade, then wheel-made)."
    },
    {
        "type": "How",
        "q": "How did Neolithic stone tools differ from Palaeolithic stone tools?",
        "sol": "Palaeolithic tools were crude, rough, and unpolished core/flake flints. Neolithic tools were polished and ground (celts/axes) with sharp, refined cutting edges, designed for woodworking, forest clearing, and farming."
    },
    {
        "type": "Case Study",
        "q": "An excavation team in Kashmir uncovers a subterranean circular pit dug into the loess soil. Inside, they find ash, bone tools, and a skeleton of a dog alongside a human skeleton. Which site is this?",
        "sol": "The site is Burzahom, which is unique for subterranean pit-dwellings and domestic dog burials alongside humans."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the significance of the Lahuradewa excavations for agricultural history.",
        "sol": "Before Lahuradewa was excavated, Koldihwa (~6000 BC) and Mehrgarh (~7000 BC) were considered the oldest agricultural sites in India. Lahuradewa yielded carbonized rice grains dated to ~9000 BC. This proved that rice domestication was independent and occurred much earlier in the Ganga Valley, making it the oldest record of agriculture in the subcontinent and rewriting global Neolithic history."
    }
]

# Section 5: Chalcolithic Age
sec5_questions = [
    {
        "type": "MCQ",
        "q": "Which Chalcolithic culture, located in Madhya Pradesh, is famous for Navdatoli (yielding the richest variety of food grains) and high-quality painted pottery?",
        "opts": ["Ahar Culture", "Jorwe Culture", "Malwa Culture", "Kayatha Culture"],
        "ans": 2,
        "sol": "The Malwa Culture is famous for high-quality painted pottery and the site of Navdatoli, excavated by H.D. Sankalia."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following Chalcolithic sites are located in Maharashtra under the Jorwe culture? (Select all that apply)",
        "opts": [
            "Daimabad",
            "Inamgaon",
            "Nevasa",
            "Gilund"
        ],
        "ans": [0, 1, 2],
        "sol": "Daimabad, Inamgaon, and Nevasa are Jorwe culture sites. Gilund belongs to the Ahar culture in Rajasthan."
    },
    {
        "type": "True/False",
        "q": "True or False: The Chalcolithic cultures in India were urban societies contemporaneous with the Harappan Civilization and lived in large cities built of kiln-burnt bricks.",
        "ans": False,
        "sol": "They were rural farming communities living in mud/wattle-and-daub houses, unlike the urban Harappan Bronze Age."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The Chalcolithic site of Ahar in Rajasthan was known as ________ in ancient times due to the abundance of copper tools found there.",
        "ans": "Tambavati",
        "sol": "Ahar was called Tambavati, meaning 'place of copper'."
    },
    {
        "type": "Match the Following",
        "q": "Match the Chalcolithic cultures with their geographical location:",
        "items": [
            {"left": "I. Ahar Culture", "key": "A"},
            {"left": "II. Malwa Culture", "key": "B"},
            {"left": "III. Jorwe Culture", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Southeast Rajasthan (Banas River Valley)"},
            {"val": "B", "text": "Central India / Madhya Pradesh"},
            {"val": "C", "text": "Maharashtra (Deccan Plateau)"}
        ],
        "sol": "Ahar (I-A), Malwa (II-B), Jorwe (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Name the largest Jorwe culture site in Maharashtra, which has yielded a spectacular hoard of solid bronze sculptures.",
        "sol": "Daimabad."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> Jorwe culture sites like Inamgaon show evidence of a high infant mortality rate.<br><strong>Reason (R):</strong> Large numbers of children's skeletal remains have been found buried in clay urns beneath the floors of houses.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are true. The discovery of numerous child burials in urns under house floors directly corroborates high infant mortality."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: The Ahar culture of Rajasthan is characterized by a complete absence of microliths (stone tools).<br>Statement II: In Northern India, Chalcolithic graves show that the dead were buried in an East-West orientation.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because Chalcolithic graves in Northern India (e.g. Maharashtra) were oriented North-South (East-West was common in South India)."
    },
    {
        "type": "Why",
        "q": "Why is the Ahar culture called 'Tambavati'?",
        "sol": "Because of the unique abundance of copper tools and metallurgy in the region. Unlike other Chalcolithic cultures, they did not use stone blades, relying entirely on copper."
    },
    {
        "type": "How",
        "q": "How did the Daimabad bronze hoard differ from typical Chalcolithic metallurgy?",
        "sol": "The Daimabad hoard consisted of solid bronze (copper-tin alloy) sculptures (chariot with driver, rhino, elephant, buffalo) weighing several kilograms, indicating advanced Harappan metalwork or direct trade contact, whereas typical Chalcolithic tools were thin, flat copper axes and chisels."
    },
    {
        "type": "Case Study",
        "q": "An archaeologist uncovers a planned mud settlement in Maharashtra. The houses contain a granary, a jetty, clay mother goddess figurines, and child burials under the floors. Identify this Jorwe site.",
        "sol": "The site is Inamgaon, a major fortified and planned settlement of the Jorwe culture."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the main differences between the Bronze Age Harappan Civilization and the contemporary Chalcolithic cultures.",
        "sol": "The Harappan Civilization was highly urbanized, built planned cities of kiln-burnt bricks, possessed a writing system, and used bronze (alloy). Chalcolithic cultures were rural, lived in mud-brick/wattle-and-daub huts, had no writing system, used copper (unalloyed) alongside stone tools, and had distinct painted pottery traditions."
    }
]

# Section 6: Uttar Pradesh (UP) Special Focus & Megaliths
sec6_questions = [
    {
        "type": "MCQ",
        "q": "At which UP site in the Belan Valley was the oldest evidence of pottery in the world discovered?",
        "opts": ["Koldihwa", "Sarai Nahar Rai", "Chopani Mando", "Lahuradewa"],
        "ans": 2,
        "sol": "Chopani Mando yielded the earliest evidence of handmade pottery in the world, dating to the transition from Mesolithic to Neolithic."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following statements are correct regarding the Belan Valley sites in UP? (Select all that apply)",
        "opts": [
            "It was excavated under the guidance of Prof. G.R. Sharma of Allahabad University.",
            "Lohanda Nala yielded a bone Mother Goddess figurine.",
            "Koldihwa yielded early evidence of rice cultivation.",
            "It is situated completely in the Pratapgarh district."
        ],
        "ans": [0, 1, 2],
        "sol": "G.R. Sharma excavated the valley; Lohanda Nala yielded the bone Mother Goddess; Koldihwa yielded rice. The valley is in Mirzapur/Sonbhadra/Prayagraj districts, not Pratapgarh."
    },
    {
        "type": "True/False",
        "q": "True or False: Lahuradewa in Sant Kabir Nagar district is famous for pushing back the timeline of rice cultivation in South Asia to ~9000 BC.",
        "ans": True,
        "sol": "Lahuradewa yielded carbonized rice grains dated to ~9000 BC, making it the oldest rice cultivation site in the world."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: In Southern India, the Iron Age is characterized by burials marked by huge stone structures called ________.",
        "ans": "Megaliths",
        "sol": "Megaliths are large stone monuments marking Iron Age graves in South India."
    },
    {
        "type": "Match the Following",
        "q": "Match the Pratapgarh Mesolithic sites of UP with their key feature:",
        "items": [
            {"left": "I. Sarai Nahar Rai", "key": "A"},
            {"left": "II. Mahadaha", "key": "B"},
            {"left": "III. Damdama", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Hearth sites, earliest burials, war injury skeleton"},
            {"val": "B", "text": "Double burials and bone antler ornaments"},
            {"val": "C", "text": "Triple burial and 41 graves"}
        ],
        "sol": "Sarai Nahar Rai (I-A), Mahadaha (II-B), Damdama (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Which Megalithic candidate site in Karnataka is famous for its hundreds of prehistoric dolmens?",
        "sol": "Hire Benakal."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Pratapgarh Mesolithic sites (Sarai Nahar Rai, Mahadaha, Damdama) are crucial for studying early human biology in India.<br><strong>Reason (R):</strong> They have yielded the oldest large group of human skeletal remains (burials) in the subcontinent, preserved in old oxbow lake environments.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are true. These sites provide the earliest group of well-preserved human skeletons in India, enabling bio-archaeological research."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Southern Indian Megalithic builders buried their dead along with iron implements and Painted Grey Ware pottery.<br>Statement II: The bone Mother Goddess figurine found at Lohanda Nala belongs to the Upper Palaeolithic phase.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 1,
        "sol": "Statement I is incorrect because Megalithic builders used Painted Black-and-Red Ware (BRW) pottery, not Painted Grey Ware (which is Northern Iron Age). Statement II is correct."
    },
    {
        "type": "Why",
        "q": "Why did the Megalithic builders place iron weapons (daggers, arrowheads) inside the graves of the deceased?",
        "sol": "Because they believed in life after death. Iron tools and weapons were placed to help the deceased protect themselves or hunt in the afterlife, reflecting their spiritual and religious beliefs."
    },
    {
        "type": "How",
        "q": "How did the introduction of iron metallurgy affect the agricultural layout of Northern India?",
        "sol": "Iron tools (axes and heavy iron-tipped ploughshares) enabled the clearing of dense tropical forests in the Ganga Valley and the deep tilling of heavy alluvial soils. This produced massive agricultural surpluses, leading to settled village clusters and the emergence of early states (Mahajanapadas)."
    },
    {
        "type": "Case Study",
        "q": "An excavation team in South India discovers an underground stone-lined chamber containing human bones, a black-and-red clay pot, and an iron trident. Classify the burial type and age.",
        "sol": "This is a Cist burial belonging to the Megalithic / Iron Age of South India (~1000 BC onwards)."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the significance of the Pratapgarh district sites for the prehistory of Uttar Pradesh.",
        "sol": "Located on the banks of ancient oxbow lakes of the Ganga, the Pratapgarh sites (Sarai Nahar Rai, Mahadaha, Damdama) represent the oldest Mesolithic settlements in UP. They contain the earliest systematic human burials, double and triple graves, circular huts with hearths, and extensive bone-working technology, providing a window into Holocene hunter-gatherer societies."
    }
]

mastery_sections = [
    {
        "title": "1. Historiography, Pioneers & Classifications",
        "masteryZone": sec1_questions
    },
    {
        "title": "2. Palaeolithic Age (Old Stone Age): 2 Million BC – 10,000 BC",
        "masteryZone": sec2_questions
    },
    {
        "title": "3. Mesolithic Age (Middle Stone Age): 10,000 BC – 6,000 BC",
        "masteryZone": sec3_questions
    },
    {
        "title": "4. Neolithic Age (New Stone Age): 6,000 BC – 1,000 BC",
        "masteryZone": sec4_questions
    },
    {
        "title": "5. Chalcolithic Age (Copper-Stone Age): 3,000 BC – 500 BC",
        "masteryZone": sec5_questions
    },
    {
        "title": "6. Uttar Pradesh (UP) Special Focus & Megaliths",
        "masteryZone": sec6_questions
    }
]

mastery_data = {
    "sections": mastery_sections
}

# Run processing to highlight bold strings
processed_theory = process_data(theory)
processed_mastery = process_data(mastery_data)

# Save theory.json
with open(os.path.join(BASE_DIR, "theory.json"), "w", encoding="utf-8") as f:
    json.dump(processed_theory, f, ensure_ascii=False, indent=4)

print("theory.json generated and processed successfully.")

# Save mastery.json
with open(os.path.join(BASE_DIR, "mastery.json"), "w", encoding="utf-8") as f:
    json.dump(processed_mastery, f, ensure_ascii=False, indent=4)

print("mastery.json generated and processed successfully.")
