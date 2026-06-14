import json
import os
import re

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\history-of-india\indus-valley-civilization"

def highlight_bold(text):
    if not isinstance(text, str):
        return text
    # Replaces **text** with <strong style="color: #e74c3c; font-weight: 800;">text</strong> to highlight key terms
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
# Diagram 1: IVC Town Planning Concept (Citadel vs Lower Town)
town_planning_svg = """<svg viewBox="0 0 800 340" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 15px;">
<style>
  .svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: var(--text-dark, #2c3e50); font-size: 16px; }
  .citadel-node { fill: rgba(142, 68, 173, 0.08); stroke: #8e44ad; stroke-width: 2.5px; rx: 8px; ry: 8px; }
  .lower-town-node { fill: rgba(52, 152, 219, 0.05); stroke: #3498db; stroke-width: 2.5px; rx: 8px; ry: 8px; }
  .text-header { font-family: 'Outfit', sans-serif; font-size: 13px; fill: var(--primary, #1a5276); font-weight: 700; }
  .text-body { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-light, #555); }
  .street-line { fill: none; stroke: #e67e22; stroke-width: 6px; stroke-linecap: round; }
  .drain-line { fill: none; stroke: #95a5a6; stroke-width: 2.5px; stroke-dasharray: 4,3; }
</style>
<text x="20" y="25" class="svg-title">Harappan Urban Infrastructure &amp; Town Planning Grid</text>

<!-- CITADEL (West - Elevated Platform) -->
<rect x="30" y="60" width="220" height="240" class="citadel-node" />
<text x="140" y="85" class="text-header" text-anchor="middle" fill="#8e44ad">📍 WESTERN CITADEL (ACROPOLIS)</text>
<line x1="45" y1="95" x2="235" y2="95" stroke="#d7bde2" stroke-width="1"/>
<text x="50" y="120" class="text-body" style="font-weight:bold;">• Elevated Mud-brick Platform</text>
<text x="50" y="140" class="text-body">• Fortified Retaining Wall</text>
<text x="50" y="160" class="text-body">• Great Bath (Mohenjo-daro)</text>
<text x="50" y="180" class="text-body">• Great Granary (Storage hub)</text>
<text x="50" y="200" class="text-body">• Assembly Halls / Administrative centers</text>
<text x="50" y="220" class="text-body">• Houses of ruling elite class</text>
<text x="140" y="270" class="text-header" text-anchor="middle" fill="#8e44ad">🛡️ Fortified / Restricted Access</text>

<!-- GRID STREET SYSTEM (Center/Right Grid Lines) -->
<line x1="280" y1="60" x2="280" y2="300" class="street-line" />
<line x1="530" y1="60" x2="530" y2="300" class="street-line" />
<line x1="260" y1="120" x2="770" y2="120" class="street-line" />
<line x1="260" y1="240" x2="770" y2="240" class="street-line" />

<!-- Under-street Covered Drains -->
<line x1="285" y1="65" x2="285" y2="295" class="drain-line" />
<line x1="535" y1="65" x2="535" y2="295" class="drain-line" />
<line x1="265" y1="125" x2="765" y2="125" class="drain-line" />

<text x="405" y="112" class="text-body" style="fill: #d35400; font-weight: bold; font-size: 10px;">Grid Streets Intersect at 90° (Right Angles)</text>
<text x="295" y="295" class="text-body" style="fill: #7f8c8d; font-size: 10px;">Covered Drains with Inspection Manholes</text>

<!-- LOWER TOWN (East - Residential Area) -->
<rect x="560" y="60" width="210" height="240" class="lower-town-node" />
<text x="665" y="85" class="text-header" text-anchor="middle" fill="#3498db">🏡 EASTERN LOWER TOWN</text>
<line x1="575" y1="95" x2="755" y2="95" stroke="#aed6f1" stroke-width="1"/>
<text x="580" y="120" class="text-body" style="font-weight:bold;">• Residential Sector</text>
<text x="580" y="140" class="text-body">• Standardized Burnt Bricks (4:2:1)</text>
<text x="580" y="160" class="text-body">• Multi-room Courtyard Houses</text>
<text x="580" y="180" class="text-body">• Private Wells &amp; Baths in houses</text>
<text x="580" y="200" class="text-body">• Commercial Craft Shops / Bazars</text>
<text x="580" y="220" class="text-body">• Houses opened to lanes, not main road</text>
<text x="665" y="270" class="text-header" text-anchor="middle" fill="#3498db">👥 Common Citizens / Artisans</text>
</svg>"""

# Diagram 2: IVC Trade Routes Map Concept
trade_routes_svg = """<svg viewBox="0 0 800 320" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); box-shadow: inset 0 0 10px rgba(0,0,0,0.05); padding: 15px;">
<style>
  .svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: var(--text-dark, #2c3e50); font-size: 16px; }
  .hub-node { fill: #ffffff; stroke: #27ae60; stroke-width: 2px; rx: 5px; ry: 5px; }
  .hub-highlight { fill: rgba(39, 174, 96, 0.06); stroke: #2ecc71; stroke-width: 2px; rx: 6px; ry: 6px; }
  .text-hub { font-family: 'Outfit', sans-serif; font-size: 13px; fill: #27ae60; font-weight: bold; }
  .text-desc { font-family: 'Inter', sans-serif; font-size: 10.5px; fill: var(--text-light, #555); }
  .trade-arrow { fill: none; stroke: #e74c3c; stroke-width: 1.5px; stroke-dasharray: 4,3; marker-end: url(#trade-head); }
</style>
<defs>
  .svg-title { fill: var(--text-dark, #2c3e50) !important; }
  <marker id="trade-head" markerWidth="8" markerHeight="6" refX="6" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#e74c3c" />
  </marker>
</defs>
<text x="20" y="25" class="svg-title">Indus Valley Civilisation: Raw Material Imports &amp; External Trade Networks</text>

<!-- Import Source: Afghanistan/Persia -->
<rect x="20" y="60" width="210" height="230" class="hub-node" />
<text x="125" y="85" class="text-hub" text-anchor="middle">🏔️ AFGHANISTAN &amp; PERSIA</text>
<line x1="35" y1="95" x2="215" y2="95" stroke="#abebc6" stroke-width="1"/>
<text x="40" y="120" class="text-desc" style="font-weight:bold; fill: #196f3d;">Badakhshan (Afghanistan)</text>
<text x="40" y="135" class="text-desc">• LAPIS LAZULI (Precious Blue Gem)</text>
<text x="40" y="155" class="text-desc" style="font-weight:bold; fill: #196f3d;">Iran / Persia</text>
<text x="40" y="170" class="text-desc">• TURQUOISE &amp; Silver</text>
<text x="40" y="195" class="text-desc" style="font-weight:bold; fill: #196f3d;">Sogdiana / Central Asia</text>
<text x="40" y="210" class="text-desc">• TIN (for Bronze-making alloy)</text>

<!-- Core IVC Core Nodes -->
<rect x="290" y="60" width="220" height="230" class="hub-highlight" />
<text x="400" y="85" class="text-hub" text-anchor="middle" fill="#d35400">🏭 INDUS PRODUCTION HUBS</text>
<line x1="305" y1="95" x2="495" y2="95" stroke="#f5cba7" stroke-width="1"/>
<text x="310" y="120" class="text-desc" style="font-weight:bold;">Harappa &amp; Mohenjo-daro</text>
<text x="310" y="135" class="text-desc">• Standardized seals, shell items, crafts</text>
<text x="310" y="160" class="text-desc" style="font-weight:bold;">Chanhudaro &amp; Lothal</text>
<text x="310" y="175" class="text-desc">• BEAD-MAKING Factories (Carnelian/jasper)</text>
<text x="310" y="200" class="text-desc" style="font-weight:bold;">Meluhha Trade (Sumerian Records)</text>
<text x="310" y="215" class="text-desc">• Ivory, Lapis Lazuli, Gold, Cotton</text>
<text x="310" y="230" class="text-desc">• Dilmun (Bahrain) acting as middle agent</text>

<!-- Import Source: Rajasthan & South India -->
<rect x="570" y="60" width="210" height="230" class="hub-node" />
<text x="675" y="85" class="text-hub" text-anchor="middle">🇮🇳 SUB-CONTINENTAL SOURCES</text>
<line x1="585" y1="95" x2="765" y2="95" stroke="#abebc6" stroke-width="1"/>
<text x="590" y="120" class="text-desc" style="font-weight:bold; fill: #196f3d;">Khetri Mines (Rajasthan)</text>
<text x="590" y="135" class="text-desc" fill="#b03a2e" style="font-weight: bold;">• COPPER (Primary Metal Source)</text>
<text x="590" y="160" class="text-desc" style="font-weight:bold; fill: #196f3d;">Kolar (Karnataka, South India)</text>
<text x="590" y="175" class="text-desc">• GOLD</text>
<text x="590" y="200" class="text-desc" style="font-weight:bold; fill: #196f3d;">Gujarat coast / Kathiawar</text>
<text x="590" y="215" class="text-desc">• Shells, Steatite, Carnelian beads</text>

<!-- Trade Flow Arrows -->
<path d="M 235 150 L 280 150" class="trade-arrow" />
<path d="M 565 150 L 520 150" class="trade-arrow" />
</svg>"""


# ----------------- THEORY GENERATION -----------------
theory = {
    "breadcrumbs": {
        "parent": "History of India",
        "parentUrl": "../",
        "current": "Indus Valley Civilization"
    },
    "hero": {
        "title": "Indus Valley Civilization (IVC)",
        "description": "Comprehensive, high-yield study guide on the Bronze Age Harappan Civilization of India. Master the historiography, discovery teams, geographical boundaries, town planning, trading routes, scripts, religious structures, decline theories, and UP-specific archaeological sites for AHC RO/ARO and UPSC exams."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive Mock Test (15 Questions)",
            "description": "Evaluate your knowledge on the Indus Valley Civilization. Test your grasp on trade channels, architectural elements, and archaeological discoveries under timed test conditions.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Mock Test"
        }
    },
    "timeline": {
        "title": "Harappan Chronological Phases",
        "description": "Chronological evolution of the Indus Valley Civilization from rural origins to urban maturity and subsequent decentralization.",
        "cards": [
            {
                "period": "Pre-Harappan / Early Agricultural Phase",
                "date": "c. 7000 BC – 3300 BC",
                "details": "Dominated by early village settlements. Hand-made pottery, early crop cultivation (wheat/barley), and animal domestication. Key prototype site: **Mehrgarh** in Balochistan, showing the transition from neolithic to chalcolithic pastoralism."
            },
            {
                "period": "Early Harappan / Formative Phase",
                "date": "c. 3300 BC – 2600 BC",
                "details": "Transition from rural villages to fortified settlements. Emergence of wheel-made pottery, uniform crafts, standard weights, and initial trade networks. Significant sites: **Kot Diji** (Sindh), **Amri**, **Kalibangan** (Early Phase), and **Banawali**."
            },
            {
                "period": "Mature Harappan Phase (Peak Urbanization)",
                "date": "c. 2600 BC – 1900 BC",
                "details": "The golden age of urbanisation. Characterized by grid-planned cities, highly advanced closed drainage systems, monumental buildings (Great Bath, Great Granary), brick fortification walls, steatite seals, and decalcified bronze castings."
            },
            {
                "period": "Late Harappan Phase (Post-Urban/Decline)",
                "date": "c. 1900 BC – 1300 BC",
                "details": "Gradual decline of urban centers, disappearance of the writing system, seals, and standardized weights. Shift towards rural, decentralized regional cultures (e.g., Cemetery H, Jhukar culture, and Painted Grey Ware transition). Major shift of population eastward toward the Ganga Valley."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Quick Memory Hacks",
        "description": "Short memory triggers to remember key facts and associations under exam pressure.",
        "items": [
            {
                "title": "Major Sites & Discoverers",
                "phrase": "\"HAD M. BAN\"",
                "decryption": "<strong>HA</strong>rappa = <strong>D</strong>ayaram Sahni (1921) | <strong>M</strong>ohenjo-daro = R.D. <strong>BAN</strong>erjee (1922)."
            },
            {
                "title": "Primary Harappan Imports",
                "phrase": "\"L-A-C-R T-P-S\"",
                "decryption": "<strong>L</strong>apis Lazuli from <strong>A</strong>fghanistan | <strong>C</strong>opper from <strong>R</strong>ajasthan (Khetri) | <strong>T</strong>urquoise from <strong>P</strong>ersia | <strong>S</strong>ilver/Tin from central Asia."
            },
            {
                "title": "Unique Sites Memory Trigger",
                "phrase": "\"LOTH-DOCK & DHO-WATER\"",
                "decryption": "<strong>Loth</strong>al is famous for the artificial brick <strong>Dock</strong>yard. <strong>Dho</strong>lavira is famous for massive <strong>Water</strong> harvesting reservoirs and a 3-tier town plan."
            },
            {
                "title": "Easternmost Sites in UP",
                "phrase": "\"A-H-M (Ahmedabad - but in UP)\"",
                "decryption": "<strong>A</strong>lamgirpur (Meerut), <strong>H</strong>ulas (Saharanpur), and <strong>M</strong>andi (Muzaffarnagar). Key Late Harappan/UP-specific sites."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Use these cards to test your retention of core concepts and factual details before moving to tests.",
        "items": [
            {
                "question": "Who made the first official announcement of the discovery of the Indus Valley Civilization to the world?",
                "answer": "<strong>Sir John Marshall</strong>, the Director-General of the Archaeological Survey of India (ASI), in 1924, following excavations at Harappa and Mohenjo-daro.",
                "icon": "fa-bullhorn"
            },
            {
                "question": "Which Harappan site is characterized by the unique absence of a Citadel?",
                "answer": "<strong>Chanhudaro</strong> (Sindh, Pakistan). It was exclusively a craft center known for bead factories, seal-making, and shell-working.",
                "icon": "fa-city"
            },
            {
                "question": "Where was the famous bronze statue of the 'Dancing Girl' discovered?",
                "answer": "<strong>Mohenjo-daro</strong>. It was cast using the <em>lost-wax (cire perdue)</em> metallurgy technique, representing exceptional Bronze Age artistic craftsmanship.",
                "icon": "fa-female"
            },
            {
                "question": "Which Harappan site has yielded the oldest ploughed agricultural field?",
                "answer": "<strong>Kalibangan</strong> (Rajasthan). The early phase showed a grid of furrow marks, indicating double-cropping (sowing two crops simultaneously).",
                "icon": "fa-seedling"
            },
            {
                "question": "What is the script of the Harappans called, and how is it written?",
                "answer": "It is a <strong>Pictographic script</strong> (still undeciphered) containing 375 to 400 signs. It is written in <strong>Boustrophedon</strong> style (from right-to-left in the first line and left-to-right in the second line).",
                "icon": "fa-pen-clip"
            },
            {
                "question": "Which site provides unique evidence of a double burial (male and female buried together)?",
                "answer": "<strong>Lothal</strong> (Gujarat). This site also yielded an artificial tidal dockyard and terracotta models of horses.",
                "icon": "fa-urn-pall"
            },
            {
                "question": "Where is the largest site of the Indus Valley Civilization located in India?",
                "answer": "<strong>Rakhigarhi</strong> (Ghaggar valley, Haryana). It is the largest site in the entire civilization, surpassing Mohenjo-daro in area.",
                "icon": "fa-map-location-dot"
            },
            {
                "question": "Which Late Harappan site in UP is known for the discovery of a hoard of gold jewelry?",
                "answer": "<strong>Mandi</strong> (Muzaffarnagar district, UP). It is a late Harappan site where local villagers discovered copper and gold ornaments in 2000.",
                "icon": "fa-gem"
            }
        ]
    },
    "traps": {
        "title": "AHC RO/ARO & UPSC Traps to Avoid",
        "items": [
            "**Trap 1: Confusing Lothal and Kalibangan for Fire Altars.** Fire altars have been found at **both** Lothal and Kalibangan. Do not assume they are exclusive to Kalibangan. However, ploughed fields are strictly associated with Kalibangan.",
            "**Trap 2: Believing Harappans knew about Iron or Horses.** They were a **Bronze Age** society. They had no knowledge of Iron (which entered India around 1000 BC during the Late Vedic/Iron Age). Regarding horses, while Surkotada shows bone remains of a horse, the animal was **not** a regular part of Harappan life, and they did not domesticate horses.",
            "**Trap 3: The Citadel Location Trap.** In standard Harappan cities, the Citadel is on the **West** (elevated platform) and the Lower Town is on the **East**. Do not get confused by their positions. A major exception is **Dholavira**, which is divided into **three** parts (Citadel, Middle Town, and Lower Town).",
            "**Trap 4: Identifying the river of Harappa.** Harappa is situated on the banks of the **Ravi River** (left bank), while Mohenjo-daro is on the **Indus River** (right bank). Standard exams regularly interchange these two to create trick options."
        ]
    },
    "deepDive": {
        "title": "Comprehensive Study Notes (Deep-Dive)",
        "description": "Rigorous, high-yield analysis of the Indus Valley Civilization (IVC), sub-divided into core preparation dimensions.",
        "sections": [
            {
                "title": "1. Historiography, Discovery Teams & Decipherment Attempts",
                "content": """<p>The Indus Valley Civilization (IVC) represents India's earliest urban phase. The discovery of this Bronze Age civilization revolutionized Indian history, pushing the timeline of Indian civilization back by over two millennia. Below is a detailed sequence of its discovery and the pioneers involved:</p><ul><li><strong>Charles Masson (1826):</strong> The first European to visit the ruins of Harappa (in modern Sahiwal, Pakistan Punjab) and document the presence of ancient brick mounds.</li><li><strong>Alexander Cunningham (1853, 1873):</strong> Visited Harappa twice, collected unique steatite seals with unicorn motifs and script characters, but misidentified them as external, historic-period artifacts.</li><li><strong>Dayaram Sahni (1921):</strong> Conducted systematic excavations at <strong>Harappa</strong> under the direction of the ASI, discovering the mature Harappan layer.</li><li><strong>R.D. Banerjee (1922):</strong> Discovered <strong>Mohenjo-daro</strong> (Mound of the Dead) in Larkana, Sindh, while excavating a Kushan-period Buddhist stupa.</li><li><strong>Sir John Marshall (1924):</strong> Director-General of the ASI who officially announced the discovery of a 'new civilization in the Indus Valley' to the global academic community.</li></ul><h3>The Harappan Script &amp; Decipherment Attempts</h3><p>The Harappan script remains **undeciphered**. It is a pictographic writing system containing approximately 375 to 400 unique signs. The text is written in the <strong>Boustrophedon style</strong>—alternating directions in successive lines (right-to-left, then left-to-right). Major attempts to decipher it have been made by scholars like <em>Iravatham Mahadevan</em> and <em>Asko Parpola</em>, but no consensus has been reached. Because we lack a bilingual key (like the Rosetta Stone), our understanding of Harappan political structures remains speculative, placing the civilization in **Proto-history**.</p>"""
            },
            {
                "title": "2. Geographical Extent & Detailed Profile of Major Sites",
                "content": """<p>The Indus Valley Civilization covered a vast triangular area of over 1.3 million square kilometers, stretching across parts of modern India, Pakistan, and Afghanistan. The extreme boundary sites are essential for competitive exams:</p><ul><li><strong>Northern Boundary:</strong> Manda on the Chenab River (Jammu &amp; Kashmir).</li><li><strong>Southern Boundary:</strong> Daimabad on the Pravara River, a tributary of the Godavari (Maharashtra).</li><li><strong>Eastern Boundary:</strong> Alamgirpur on the Hindon River, a tributary of the Yamuna (Uttar Pradesh).</li><li><strong>Western Boundary:</strong> Sutkagen-dor on the Dasht River, near the Iran border (Balochistan, Pakistan).</li></ul><h3>Detailed Profile of Core Mature Harappan Sites</h3><div class="premium-table-container"><table class="premium-table"><thead><tr><th>Site Name</th><th>River Bank &amp; Location</th><th>Key Excavators</th><th>Major Discoveries &amp; Characteristics</th></tr></thead><tbody><tr><td>Harappa</td><td>Ravi (Left Bank)<br>Punjab, Pakistan</td><td>Dayaram Sahni (1921), Madho Sarup Vats</td><td>Row of 6 Granaries, Coffin Burial (Cemetery R-37), red sandstone Torso of a Male Dancer, clay models of bullock carts.</td></tr><tr><td>Mohenjo-daro</td><td>Indus (Right Bank)<br>Sindh, Pakistan</td><td>R.D. Banerjee (1922), Mackay, Marshall</td><td><strong>Great Bath</strong>, Great Granary, Assembly Hall, Bronze statue of the **Dancing Girl** (Lost-Wax technique), steatite **Bearded Priest**, Pashupati Seal.</td></tr><tr><td>Lothal</td><td>Bhogava<br>Gujarat, India</td><td>S.R. Rao (1954)</td><td>**Artificial Brick Dockyard** (world's oldest tidal dock), Double Burial (male-female in same grave), Rice Husk, Ivory scale, Fire altars.</td></tr><tr><td>Kalibangan</td><td>Ghaggar<br>Rajasthan, India</td><td>A. Ghosh (1953), B.B. Lal &amp; B.K. Thapar</td><td>**Ploughed Field** (earliest furrow marks), decorated tiles, camel bones, wooden furrow, fire altars. Name means 'Black Bangles'.</td></tr><tr><td>Chanhudaro</td><td>Indus<br>Sindh, Pakistan</td><td>N.G. Majumdar (1931), Ernest Mackay</td><td>**No Citadel** (only unfortified site), Bead-making factory, inkpot, footprints of a dog chasing a cat on a brick, bronze toy carts.</td></tr><tr><td>Dholavira</td><td>Luni / Kadir Bet<br>Kutch, Gujarat, India</td><td>R.S. Bisht (1990)</td><td>**Three-tier division** (Citadel, Middle Town, Lower Town), unique **Water Harvesting Reservoirs**, large 10-sign billboard.</td></tr><tr><td>Rakhigarhi</td><td>Ghaggar<br>Haryana, India</td><td>Amarendra Nath</td><td>**Largest Harappan site** in the subcontinent. Granary, defensive walls, bead-making lanes, and five sister mounds.</td></tr><tr><td>Surkotada</td><td>Kutch, Gujarat, India</td><td>J.P. Joshi (1964)</td><td>Evidence of **horse bones** (a rare find in late layers), pot burials with large stone slabs.</td></tr></tbody></table></div>"""
            },
            {
                "title": "3. Advanced Town Planning, Civic Infrastructure & Engineering",
                "content": """<p>The most distinctive feature of the mature Harappan civilization was its advanced **urban planning**, which was unmatched in the ancient world (including contemporary Egypt and Mesopotamia). Streets were laid out in a grid pattern, running North-South and East-West, intersecting at right angles (**Grid System**).</p>""" + town_planning_svg + """<h3>Key Dimensions of Harappan Engineering</h3><ul><li><strong>Division of Cities:</strong> Most cities were divided into a fortified **Citadel (Acropolis)** on the West (built on elevated mud-brick platforms, housing public buildings and the elite) and a larger, unfortified **Lower Town** on the East (divided into sectors, housing commoners, merchants, and artisans).</li><li><strong>Standardization of Bricks:</strong> Bricks used for construction were of uniform dimensions in a ratio of **4:2:1** (length:breadth:thickness). Both sun-dried and kiln-burnt bricks were used.</li><li><strong>Advanced Drainage System:</strong> The drainage system was a marvel of civic engineering. Every house had a bathroom connected to covered street drains via pottery pipes. The street drains ran under the main roads and were lined with bricks, covered with removable stone slabs or brick arches for regular cleaning. They featured brick-lined sump pits (inspection manholes) at regular intervals.</li><li><strong>Domestic Architecture:</strong> Houses were built around a central courtyard. Rooms opened into the courtyard rather than the main streets, maintaining privacy. Doors and windows opened into side lanes. Houses were often multi-story, with staircases made of burnt bricks. Almost every household had its own brick-lined well and bathing area.</li></ul>"""
            },
            {
                "title": "4. Economy, Crafts, Trade Routes & Weights System",
                "content": """<p>The Harappan economy was highly diversified, based on flourishing agriculture, animal husbandry, domestic craft production, and an extensive network of internal and external trade.</p>""" + trade_routes_svg + """<h3>Agricultural Achievements</h3><ul><li>The Harappans were the first in the world to cultivate **cotton** (referred to as <em>Sindon</em> by the Greeks, derived from 'Sindhu').</li><li>Major crops cultivated included wheat, barley, peas, sesamum, mustard, and lentils. Rice husks have been discovered at **Lothal** and **Rangpur**, though rice was not a staple crop.</li><li>They used wooden ploughshares (clay models found at Banawali) and harvested crops using stone sickles.</li></ul><h3>Standardized Weights and Measures</h3><p>To facilitate commerce, the Harappans developed a highly standardized, precise system of weights and measures. Weights were made of chert, jasper, and chalcedony. The weight system followed a **binary system** for lower denominations (1, 2, 4, 8, 16, 32, 64) and a **decimal system** for higher denominations. The unit of **16** (equivalent to 13.63 grams) was the base unit of measure, which persisted in India's currency and weight systems until modern times (e.g., 16 annas in a rupee).</p><h3>External Trade &amp; Raw Material Imports</h3><p>External trade was conducted via land routes through Afghanistan and sea routes across the Persian Gulf. Mesopotamian cuneiform tablets record trade with **Meluhha** (the ancient Sumerian name for the Indus region), mentioning two intermediate trading stations: **Dilmun** (modern Bahrain) and **Makan** (Oman coast). The Harappans imported crucial raw materials to support their bead and metal industries:</p><ul><li><strong>Copper:</strong> Imported from the **Khetri mines** of Rajasthan and Baluchistan.</li><li><strong>Lapis Lazuli:</strong> A brilliant blue gem imported from **Badakhshan** in northern Afghanistan (specifically the Harappan trading colony at **Shortughai**).</li><li><strong>Tin:</strong> Imported from Afghanistan or Central Asia (used to alloy copper into bronze).</li><li><strong>Gold:</strong> Imported from **Kolar** in Karnataka (South India).</li><li><strong>Turquoise:</strong> Imported from Persia (modern Iran) and Tibet.</li></ul>"""
            },
            {
                "title": "5. Religion, Artworks & Script Analysis",
                "content": """<p>The religious life of the Harappans can be reconstructed primarily from terracotta figurines, stone sculptures, and seals. Unlike Egypt or Mesopotamia, **no monumental temples** or structures dedicated to deities have been identified in the Indus Valley.</p><h3>Key Religious Elements</h3><ul><li><strong>Mother Goddess:</strong> A large number of terracotta figurines depict a female deity wearing an elaborate head-dress, representing fertility worship. A famous seal depicts a plant growing out of a woman's womb, symbolizing the Earth Goddess.</li><li><strong>Pashupati Mahadeva Seal:</strong> Discovered at Mohenjo-daro. It depicts a three-faced male deity sitting in a yogic posture, wearing horned headgear. He is surrounded by four animals: an **Elephant**, a **Tiger**, a **Rhinoceros**, and a **Buffalo** (mnemonic: *ETRB*). Two deer are shown sitting near his feet. This deity is considered a proto-form of Shiva (Proto-Shiva).</li><li><strong>Phallic and Yoni Worship:</strong> Numerous stone rings and cylindrical stones indicate the worship of Linga and Yoni, representing generative power.</li><li><strong>Tree and Animal Worship:</strong> The Pipal tree (Ficus religiosa) was considered sacred and is depicted on numerous seals. Among animals, they worshipped the **Humped Bull (Unicorn)** and other mythical composite animals.</li></ul><h3>Foundational Harappan Artworks</h3><ul><li><strong>The Dancing Girl:</strong> A 10.5 cm high bronze figurine discovered at Mohenjo-daro, cast using the **Lost-Wax (cire perdue) technique**. She is depicted wearing dozens of bangles on her left arm, in a relaxed stance with her right hand on her hip.</li><li><strong>The Bearded Priest:</strong> A steatite stone bust of a male figure wearing a shawl decorated with a trefoil pattern. His eyes are half-closed, suggesting a meditative state.</li><li><strong>Steatite Seals:</strong> Over 2000 seals have been found, mostly square or rectangular, carved from soft soapstone (steatite). Most feature an animal carving (usually a unicorn or bull) accompanied by a line of pictographic script. They were used to stamp clay tags on trade bundles to verify authenticity.</li></ul>"""
            },
            {
                "title": "6. Decline Theories & Uttar Pradesh (UP) Special Harappan Sites",
                "content": """<p>Around 1900 BC, the mature Harappan phase began to decline, leading to the abandonment of major cities and the disappearance of the script, seals, and long-distance trade. Historians and archaeologists have proposed several theories to explain this decline, suggesting it was likely a combination of factors rather than a single event:</p><div class="premium-table-container"><table class="premium-table"><thead><tr><th>Proposed Theory</th><th>Key Proponents / Scholars</th><th>Archaeological Arguments &amp; Evidence</th></tr></thead><tbody><tr><td>Aryan Invasion Theory</td><td>Sir Mortimer Wheeler, Stuart Piggott</td><td>Discovery of skeletons in the streets of Mohenjo-daro showing head trauma. Mention of 'Purandara' (fort-destroyer Indra) in Rigveda. (Now largely discarded due to lack of genetic/cultural continuity).</td></tr><tr><td>Massive Floods &amp; River Shifts</td><td>M.R. Sahni, Robert L. Raikes, Marshall</td><td>Thick layers of silt and clay at Mohenjo-daro, indicating tectonic shifts uplifted the Indus bed, causing massive flooding.</td></tr><tr><td>Drying of Ghaggar-Hakra (Sarasvati)</td><td>C.F. Oldham, Amalanda Ghosh, Sood</td><td>Diversion of tributaries (Sutlej and Yamuna) left the Ghaggar-Hakra river bed dry, collapsing the agricultural base of Cholistan and Haryana.</td></tr><tr><td>Ecological Imbalance &amp; Deforestation</td><td>Walter Fairservis</td><td>Over-exploitation of wood for baking millions of kiln bricks and overgrazing depleted the soil, leading to famine.</td></tr><tr><td>Epidemic / Malaria</td><td>K.A.R. Kennedy</td><td>Skeletal analysis from late layers of Mohenjo-daro showed high incidences of anemia and infectious diseases.</td></tr></tbody></table></div><h3>Uttar Pradesh (UP) Specific Harappan Focus (AHC RO/ARO Importance)</h3><p>For Allahabad High Court exams, Uttar Pradesh's connection to the Late Harappan phase is highly tested. As the Mature Harappan cities declined, populations migrated eastwards into the Ganga-Yamuna Doab, establishing numerous Late Harappan rural settlements in western UP:</p><ul><li><strong>Alamgirpur (Meerut District):</strong> Located on the Hindon River. It is the **easternmost site** of the entire Indus Valley Civilization. Excavated by Y.D. Sharma in 1958, it yielded pottery with cloth impressions, proving Harappan presence in the Ganga Valley.</li><li><strong>Hulas (Saharanpur District):</strong> A Late Harappan site that has provided valuable botanical remains of diverse crops, indicating agricultural continuity.</li><li><strong>Mandi (Muzaffarnagar District):</strong> Discovered in the year 2000. It is a highly famous Late Harappan site where local villagers unearthed a **massive hoard** of copper vessels, gold jewelry, and semi-precious beads. This is distinct from Mandi in Himachal Pradesh.</li><li><strong>Sanauli (Baghpat District):</strong> Though classified as late-protohistoric (Bronze Age Ochre Coloured Pottery/Copper Hoard culture, c. 1900 BC), excavations by the ASI revealed a massive necropolis of **126 burials**, including copper-sheathed coffins and **wooden chariots**, showing strong metallurgical ties to the late Harappan era.</li></ul>"""
            }
        ]
    }
}

# ----------------- PRACTICE ZONE (50 QUESTIONS) -----------------
practice_questions = [
    {
        "q": "Who was the Director-General of the Archaeological Survey of India (ASI) when the discovery of the Indus Valley Civilization was announced?",
        "opts": ["Alexander Cunningham", "Sir John Marshall", "Sir Mortimer Wheeler", "Dayaram Sahni"],
        "ans": 1,
        "sol": "Sir John Marshall officially announced the discovery of the Indus Valley Civilization to the world in 1924, while serving as Director-General of the ASI."
    },
    {
        "q": "At which of the following Harappan sites was the famous 'Great Bath' discovered?",
        "opts": ["Harappa", "Mohenjo-daro", "Lothal", "Kalibangan"],
        "ans": 1,
        "sol": "The Great Bath, a large brick-lined public bathhouse measuring 11.88 x 7.01 meters, was discovered in the Citadel of Mohenjo-daro."
    },
    {
        "q": "Which Harappan site has yielded the unique evidence of an artificial dockyard made of baked bricks?",
        "opts": ["Sutkagen-dor", "Chanhudaro", "Lothal", "Dholavira"],
        "ans": 2,
        "sol": "Lothal in Gujarat features a massive brick basin measuring 218 x 37 meters, identified as a tidal dockyard connected to the Bhogava River."
    },
    {
        "q": "Which is the largest site of the Indus Valley Civilization in the Indian subcontinent?",
        "opts": ["Dholavira", "Rakhigarhi", "Lothal", "Kalibangan"],
        "ans": 1,
        "sol": "Rakhigarhi in Haryana, located in the Ghaggar-Hakra river valley, is the largest Harappan site in India, spanning over 350 hectares."
    },
    {
        "q": "The Harappan civilization is geologically placed in which of the following ages?",
        "opts": ["Palaeolithic Age", "Neolithic Age", "Bronze Age", "Iron Age"],
        "ans": 2,
        "sol": "The Harappan Civilization was a Bronze Age civilization (Proto-historic) characterized by advanced copper-tin metallurgy, operating alongside stone tools."
    },
    {
        "q": "Which of the following Harappan sites is located in the Kutch region of Gujarat and is divided into three distinct parts?",
        "opts": ["Lothal", "Surkotada", "Dholavira", "Rojdi"],
        "ans": 2,
        "sol": "Dholavira is situated on Kadir Bet in the Kutch district of Gujarat. Unlike other Harappan sites, it is divided into three parts: Citadel, Middle Town, and Lower Town."
    },
    {
        "q": "Which of the following sites has provided the earliest archaeological evidence of a ploughed field in India?",
        "opts": ["Harappa", "Kalibangan", "Banawali", "Mehrgarh"],
        "ans": 1,
        "sol": "Kalibangan in Rajasthan has yielded the earliest ploughed field, showing criss-cross furrow patterns dating to the Early Harappan phase."
    },
    {
        "q": "The Harappan script is written in which of the following styles?",
        "opts": ["Kharosthi", "Brahmi", "Boustrophedon", "Hieroglyphic"],
        "ans": 2,
        "sol": "The Harappan script is written in Boustrophedon style, where writing alternates directions in successive lines (right-to-left, then left-to-right)."
    },
    {
        "q": "Which of the following metals was completely unknown to the people of the Indus Valley Civilization?",
        "opts": ["Copper", "Bronze", "Gold", "Iron"],
        "ans": 3,
        "sol": "Iron was unknown to the Harappans. Iron technology emerged in India much later, around 1000 BC during the Late Vedic period."
    },
    {
        "q": "Which Harappan site is characterized by the complete absence of a fortified Citadel?",
        "opts": ["Chanhudaro", "Kalibangan", "Lothal", "Banawali"],
        "ans": 0,
        "sol": "Chanhudaro in Sindh is the only major Harappan city that lacks a Citadel. It was primarily a craft manufacturing center."
    },
    {
        "q": "The easternmost boundary site of the Indus Valley Civilization is located at which place in Uttar Pradesh?",
        "opts": ["Sanauli", "Hulas", "Alamgirpur", "Mandi"],
        "ans": 2,
        "sol": "Alamgirpur in the Meerut district of Uttar Pradesh, situated on the Hindon River, represents the easternmost boundary of the IVC."
    },
    {
        "q": "Lapis Lazuli, a highly prized blue semi-precious stone, was imported by the Harappans primarily from which region?",
        "opts": ["Khetri (Rajasthan)", "Badakhshan (Afghanistan)", "Persia (Iran)", "Kolar (Karnataka)"],
        "ans": 1,
        "sol": "Lapis Lazuli was imported from Badakhshan in northern Afghanistan, where the Harappans established a trading post at Shortughai."
    },
    {
        "q": "Which Harappan site is famous for the discovery of a clay toy model of a plough?",
        "opts": ["Kalibangan", "Banawali", "Rakhigarhi", "Ropar"],
        "ans": 1,
        "sol": "A terracotta model of a plough was discovered at Banawali (Haryana), proving the use of ploughs in Harappan agriculture."
    },
    {
        "q": "At which site did archaeologists discover the bones of a horse, representing a rare late-phase discovery?",
        "opts": ["Surkotada", "Dholavira", "Lothal", "Chanhudaro"],
        "ans": 0,
        "sol": "Surkotada in Gujarat yielded horse bones in its upper levels, excavated by J.P. Joshi in 1964."
    },
    {
        "q": "The Harappan system of weights was based on which of the following numerical denominations?",
        "opts": ["Binary and Decimal based on 10", "Binary and Decimal based on 16", "Hexadecimal based on 12", "Duodecimal system"],
        "ans": 1,
        "sol": "The Harappan weight system followed a binary scale for lower weights (1, 2, 4, 8, 16...) and a decimal scale for higher weights, with 16 acting as the base unit."
    },
    {
        "q": "Which Mesopotamian cuneiform inscription refers to the Indus region, calling it 'Meluhha'?",
        "opts": ["Sumerian tablets", "Assyrian cylinder seals", "Egyptian papyrus", "Hittite treaties"],
        "ans": 0,
        "sol": "Sumerian cuneiform texts refer to trade relations with a land called 'Meluhha', identified as the Indus Valley Civilization."
    },
    {
        "q": "The famous steatite bust of the 'Bearded Priest' wearing a trefoil-patterned shawl was excavated at which site?",
        "opts": ["Harappa", "Mohenjo-daro", "Dholavira", "Kalibangan"],
        "ans": 1,
        "sol": "The Bearded Priest bust was excavated at Mohenjo-daro, representing high-quality stone sculpture work of the mature phase."
    },
    {
        "q": "Which animal is NOT depicted on the famous 'Pashupati Seal' discovered at Mohenjo-daro?",
        "opts": ["Elephant", "Tiger", "Rhinoceros", "Cow"],
        "ans": 3,
        "sol": "The Pashupati Seal depicts a yogic figure surrounded by an Elephant, Tiger, Rhinoceros, and Buffalo, with two deer at the base. Cow is not depicted."
    },
    {
        "q": "Who excavated the Harappan site of Lothal in Gujarat?",
        "opts": ["Dayaram Sahni", "S.R. Rao", "R.S. Bisht", "J.P. Joshi"],
        "ans": 1,
        "sol": "Lothal was excavated by S.R. Rao in 1954, uncovering the dockyard, fire altars, and double burials."
    },
    {
        "q": "Which of the following crops was first cultivated in the world by the people of the Indus Valley Civilization?",
        "opts": ["Wheat", "Barley", "Cotton", "Sugarcane"],
        "ans": 2,
        "sol": "The Harappans were pioneers in cotton cultivation. The Greeks called it 'Sindon', derived from the name of the Sindhu (Indus) River."
    },
    {
        "q": "Which Harappan site in Gujarat is famous for its elaborate water harvesting and management system containing reservoirs?",
        "opts": ["Lothal", "Surkotada", "Dholavira", "Rangpur"],
        "ans": 2,
        "sol": "Dholavira is renowned for its sophisticated water harvesting system, featuring 16 large rock-cut reservoirs built around the Citadel."
    },
    {
        "q": "Which river did the ancient site of Kalibangan stand on in Rajasthan?",
        "opts": ["Luni", "Bhogava", "Ghaggar", "Chambal"],
        "ans": 2,
        "sol": "Kalibangan is situated on the left bank of the Ghaggar-Hakra river bed (ancient Sarasvati) in Hanumangarh district, Rajasthan."
    },
    {
        "q": "What is the standard ratio of the length, breadth, and thickness of bricks used in mature Harappan constructions?",
        "opts": ["3:2:1", "4:2:1", "5:3:1", "4:3:2"],
        "ans": 1,
        "sol": "Harappan bricks were highly standardized in a ratio of 4:2:1 (length:breadth:thickness) across almost all sites."
    },
    {
        "q": "The Late Harappan site of Mandi, where a massive hoard of gold jewelry was found in 2000, is located in which district of Uttar Pradesh?",
        "opts": ["Meerut", "Saharanpur", "Muzaffarnagar", "Baghpat"],
        "ans": 2,
        "sol": "Mandi is located in the Muzaffarnagar district of UP. A huge hoard of gold ornaments was found there by farmers in 2000."
    },
    {
        "q": "Which Harappan site shows unique evidence of a dog buried in a grave along with a human master, similar to Burzahom?",
        "opts": ["Ropar", "Kalibangan", "Lothal", "Banawali"],
        "ans": 0,
        "sol": "Ropar (Punjab, India) on the Sutlej River has yielded a unique burial containing a human skeleton along with a dog skeleton."
    },
    {
        "q": "The first Harappan site to be excavated in India after independence was:",
        "opts": ["Lothal", "Ropar", "Kalibangan", "Dholavira"],
        "ans": 1,
        "sol": "Ropar was excavated by Y.D. Sharma in 1953, making it the first site excavated in independent India."
    },
    {
        "q": "In Harappan town planning, the streets intersected each other at right angles. This layout pattern is called the:",
        "opts": ["Linear System", "Grid System", "Radial System", "Circular System"],
        "ans": 1,
        "sol": "The town planning followed the Grid System (also known as chessboard pattern), dividing the city into rectangular blocks."
    },
    {
        "q": "The Harappans imported Copper primarily from which of the following regions?",
        "opts": ["Khetri Mines in Rajasthan", "Kolar Mines in Karnataka", "Badakhshan in Afghanistan", "Baluchistan coast"],
        "ans": 0,
        "sol": "Copper was imported from the Khetri mines of Rajasthan and from Baluchistan."
    },
    {
        "q": "The famous bronze Dancing Girl figurine was cast using which of the following metallurgical techniques?",
        "opts": ["Sand casting", "Lost-Wax process", "Riveting", "Forging"],
        "ans": 1,
        "sol": "The Dancing Girl was cast using the Lost-Wax (cire perdue) process, where a wax model is coated with clay, melted out, and filled with molten bronze."
    },
    {
        "q": "The Western boundary site of the Indus Valley Civilization, Sutkagen-dor, is located in which region?",
        "opts": ["Sindh", "Baluchistan", "Gujarat", "Makran Coast of Iran"],
        "ans": 1,
        "sol": "Sutkagen-dor is situated on the Dasht River in the Makran/Baluchistan region of Pakistan near the Iran border."
    },
    {
        "q": "At which Harappan site was a unique wooden coffin burial discovered?",
        "opts": ["Mohenjo-daro", "Harappa", "Lothal", "Kalibangan"],
        "ans": 1,
        "sol": "Harappa has yielded evidence of a wooden coffin burial in Cemetery R-37, showing contact with foreign burial practices."
    },
    {
        "q": "The pictographic signs of the Harappan script are mostly written on which of the following objects?",
        "opts": ["Steatite Seals", "Copper plates", "Pillar inscriptions", "Palm leaf manuscripts"],
        "ans": 0,
        "sol": "The Harappan script is mostly found stamped or carved on steatite seals used for trade."
    },
    {
        "q": "Which animal was NOT domesticated by the people of the Indus Valley Civilization?",
        "opts": ["Sheep", "Buffalo", "Pig", "Horse"],
        "ans": 3,
        "sol": "While horse remains were found at Surkotada, the horse was not a regular domesticated animal of the Harappan economy."
    },
    {
        "q": "Which Harappan site has yielded a large signboard containing ten large characters of the Indus script?",
        "opts": ["Lothal", "Dholavira", "Harappa", "Mohenjo-daro"],
        "ans": 1,
        "sol": "Dholavira yielded a wooden board containing ten large symbols, often called the 'Dholavira Signboard Inscription'."
    },
    {
        "q": "The Late Harappan site of Hulas is located in which district of Uttar Pradesh?",
        "opts": ["Meerut", "Saharanpur", "Muzaffarnagar", "Baghpat"],
        "ans": 1,
        "sol": "Hulas is located in the Saharanpur district of UP, representing a crucial Late Harappan agricultural outpost."
    },
    {
        "q": "Meluhha, the Sumerian name for the Indus region, literally meant:",
        "opts": ["Land of Gold", "Land of Seafarers", "Land of Black Soil", "Land of Rivers"],
        "ans": 1,
        "sol": "In Sumerian tablets, Meluhha is referred to as a land of seafarers, known for exporting timber, ivory, and lapis lazuli."
    },
    {
        "q": "Which of the following Harappan sites has yielded the unique evidence of double burials where a male and a female were buried together?",
        "opts": ["Harappa", "Lothal", "Kalibangan", "Mohenjo-daro"],
        "ans": 1,
        "sol": "Lothal has yielded three double burials, each containing a male and a female skeleton buried in the same grave."
    },
    {
        "q": "The Harappan civilization declined around 1900 BC. Who among the following proposed the theory that an Aryan Invasion caused the decline?",
        "opts": ["Sir Mortimer Wheeler", "Sir John Marshall", "Robert Raikes", "Amalanda Ghosh"],
        "ans": 0,
        "sol": "Sir Mortimer Wheeler proposed the Aryan Invasion theory based on skeletons found at Mohenjo-daro and Rigvedic mentions of Purandara."
    },
    {
        "q": "The Harappans imported Gold primarily from which of the following regions?",
        "opts": ["Kolar in Karnataka", "Khetri in Rajasthan", "Zanskar in Kashmir", "Tibet"],
        "ans": 0,
        "sol": "Gold was imported from the Kolar gold fields of Karnataka (South India)."
    },
    {
        "q": "Which of the following sites has yielded terracotta models of horses, despite horses not being regular features of Harappan life?",
        "opts": ["Dholavira", "Chanhudaro", "Lothal", "Ropar"],
        "ans": 2,
        "sol": "Lothal has yielded terracotta figurines of horses, indicating trade contacts or awareness of the animal."
    },
    {
        "q": "Who was the archaeologist who discovered the Harappan site of Kalibangan in 1953?",
        "opts": ["A. Ghosh", "B.B. Lal", "Dayaram Sahni", "Madho Sarup Vats"],
        "ans": 0,
        "sol": "Amalanda Ghosh (A. Ghosh) discovered Kalibangan in 1953. It was later excavated by B.B. Lal and B.K. Thapar."
    },
    {
        "q": "The Harappans maintained a trading colony at Shortughai to control the lapis lazuli trade. In which country is Shortughai located?",
        "opts": ["Pakistan", "Afghanistan", "Iran", "Uzbekistan"],
        "ans": 1,
        "sol": "Shortughai is a Harappan trading outpost located in northern Afghanistan, positioned to control lapis lazuli routes."
    },
    {
        "q": "Which of the following items was NOT exported by the Harappans to Mesopotamia?",
        "opts": ["Ivory products", "Lapis Lazuli", "Cotton textiles", "Silver vessels"],
        "ans": 3,
        "sol": "The Harappans imported Silver from Persia/Mesopotamia. They exported ivory, cotton, and lapis lazuli."
    },
    {
        "q": "Which Harappan site has yielded a brick basin identified as an inspection manhole for sewage cleaning?",
        "opts": ["Harappa", "Mohenjo-daro", "Kalibangan", "Lothal"],
        "ans": 1,
        "sol": "Mohenjo-daro features elaborate street drains with brick manholes and sump pits for clearing sewage."
    },
    {
        "q": "Which of the following was the primary building material used by Harappans in Mohenjo-daro?",
        "opts": ["Stone blocks", "Kiln-burnt bricks", "Sun-dried bricks", "Timber"],
        "ans": 1,
        "sol": "While sun-dried bricks were common, Mohenjo-daro is famous for its extensive use of kiln-burnt bricks, especially for drains and citadels."
    },
    {
        "q": "The name 'Kalibangan' literally translates to which of the following?",
        "opts": ["Mound of the Dead", "Black Bangles", "Ploughed Land", "City of Wells"],
        "ans": 1,
        "sol": "Kalibangan translates to 'Black Bangles' (Kali = Black, Bangon = Bangles) due to the abundance of black terracotta bangles found there."
    },
    {
        "q": "At which Late Harappan site in UP was a massive hoard of gold jewelry discovered by local farmers in a field?",
        "opts": ["Alamgirpur", "Mandi", "Hulas", "Sanauli"],
        "ans": 1,
        "sol": "Mandi in Muzaffarnagar district, UP, yielded a massive gold hoard in 2000 during agricultural activities."
    },
    {
        "q": "Which archaeological site has yielded a copper-sheathed coffin burial and three wooden chariots, showing late-protohistoric metallurgical advances?",
        "opts": ["Sanauli", "Alamgirpur", "Mandi", "Hulas"],
        "ans": 0,
        "sol": "Sanauli (Baghpat district, UP) yielded 126 burials, including copper coffins and solid wooden wheels/chariots dated to c. 1900 BC."
    },
    {
        "q": "The Harappan civilization is classified under which division of history?",
        "opts": ["Prehistory", "Protohistory", "Historical Period", "Post-Historical"],
        "ans": 1,
        "sol": "Since Harappans had a writing system but it remains undeciphered, it is classified under Proto-history."
    },
    {
        "q": "Which tributary of the Yamuna River did the easternmost Harappan site of Alamgirpur stand on?",
        "opts": ["Chambal", "Hindon", "Betwa", "Ken"],
        "ans": 1,
        "sol": "Alamgirpur stands on the banks of the Hindon River, a tributary of the Yamuna, in Meerut district, UP."
    }
]

# ----------------- MOCK TEST QUESTIONS (15 QUESTIONS) -----------------
mock_questions = [
    {
        "q": "Consider the following statements regarding the discovery of the Indus Valley Civilization:\n1. Charles Masson was the first European to document the ruins of Harappa in 1826.\n2. Dayaram Sahni excavated Mohenjo-daro in 1922.\n3. R.D. Banerjee discovered Harappa in 1921.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2, and 3"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statements 2 and 3 are reversed: Dayaram Sahni excavated Harappa in 1921, while R.D. Banerjee discovered Mohenjo-daro in 1922."
    },
    {
        "q": "Which of the following pairs of Harappan sites and their distinctive discoveries are correctly matched?\n1. Lothal - Artificial Tidal Dockyard\n2. Dholavira - Water Reservoirs and 3-Tier Town Plan\n3. Kalibangan - Earliest Ploughed Field\n4. Chanhudaro - Bead-making Factory\nSelect the correct answer using the codes below:",
        "opts": ["1 and 3 only", "1, 2, and 4 only", "2, 3, and 4 only", "1, 2, 3, and 4"],
        "ans": 3,
        "sol": "All four pairs are correctly matched. Lothal (dockyard), Dholavira (reservoirs/3-tier town), Kalibangan (ploughed field), and Chanhudaro (bead factory) are correct."
    },
    {
        "q": "Consider the following statements regarding Harappan town planning and architecture:\n1. The cities were divided into a Western Citadel built on elevated platforms and an Eastern Lower Town.\n2. Standardized burnt bricks in the ratio of 4:2:1 were used for construction.\n3. The houses opened directly onto the main streets to facilitate commerce.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Statement 3 is incorrect because Harappan houses opened into narrow side lanes, not onto the main streets, to maintain privacy and reduce dust."
    },
    {
        "q": "With reference to the Harappan trade and economic system, consider the following statements:\n1. The Harappans had a highly standardized weight system based on binary and decimal values.\n2. Mesopotamian cuneiform inscriptions refer to trade relations with 'Meluhha'.\n3. The Harappans imported Lapis Lazuli from Kolar in Karnataka.\nWhich of the statements given above is/are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Statement 3 is incorrect because Lapis Lazuli was imported from Badakhshan (Afghanistan); Gold was imported from Kolar (Karnataka)."
    },
    {
        "q": "What is the correct geographical sequence of the following Harappan sites from North to South?\n1. Manda\n2. Harappa\n3. Mohenjo-daro\n4. Daimabad\nSelect the correct code:",
        "opts": ["1 - 2 - 3 - 4", "2 - 1 - 3 - 4", "1 - 3 - 2 - 4", "4 - 3 - 2 - 1"],
        "ans": 0,
        "sol": "The correct North-to-South sequence is Manda (Kashmir) ➔ Harappa (Punjab) ➔ Mohenjo-daro (Sindh) ➔ Daimabad (Maharashtra) (1-2-3-4)."
    },
    {
        "q": "Which of the following items were imported by the Harappans to support their metallurgical and bead-making industries?\n1. Copper from Khetri, Rajasthan\n2. Tin from Afghanistan/Central Asia\n3. Lapis Lazuli from Badakhshan, Afghanistan\n4. Turquoise from Persia\nSelect the correct answer:",
        "opts": ["1 and 2 only", "1, 2, and 3 only", "3 and 4 only", "1, 2, 3, and 4"],
        "ans": 3,
        "sol": "All four imports are correct: Copper (Khetri), Tin (Afghanistan), Lapis (Badakhshan), Turquoise (Persia)."
    },
    {
        "q": "Consider the following statements regarding the Pashupati Seal discovered at Mohenjo-daro:\n1. The deity is depicted sitting in a yogic posture, wearing horned headgear.\n2. He is surrounded by an Elephant, a Tiger, a Rhinoceros, and a Buffalo.\n3. The cow and the horse are shown sitting near the deity's feet.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2, and 3"],
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Statement 3 is incorrect because the two animals near the feet are deer, not cows or horses."
    },
    {
        "q": "Assertion (A): The Indus Valley Civilization is categorized under Proto-history.\nReason (R): The Harappans possessed a writing system, but it remains undeciphered to this day.\nSelect the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and R is the correct explanation because proto-history is defined precisely as the period with writing that cannot yet be deciphered."
    },
    {
        "q": "Which of the following Late Harappan/Copper Hoard sites are located within the state of Uttar Pradesh?\n1. Alamgirpur\n2. Hulas\n3. Mandi\n4. Sanauli\nSelect the correct answer:",
        "opts": ["1 and 3 only", "1, 2, and 4 only", "2 and 3 only", "1, 2, 3, and 4"],
        "ans": 3,
        "sol": "All four sites are located in UP: Alamgirpur (Meerut), Hulas (Saharanpur), Mandi (Muzaffarnagar), and Sanauli (Baghpat)."
    },
    {
        "q": "Consider the following statements regarding Harappan religious practices:\n1. The Harappans built monumental brick temples to worship their gods.\n2. Fertility worship is indicated by numerous terracotta mother goddess figurines.\n3. Pipal tree and humped bull worship were widely practiced.\nWhich of the statements given above is/are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 1,
        "sol": "Statement 1 is incorrect because no temples have been found in the Indus Valley. Statements 2 and 3 are correct."
    },
    {
        "q": "Which of the following pairs of Harappan sites and their river locations is/are correctly matched?\n1. Harappa - Ravi River\n2. Mohenjo-daro - Indus River\n3. Lothal - Bhogava River\n4. Kalibangan - Ghaggar River\nSelect the correct code:",
        "opts": ["1 and 2 only", "1, 2, and 3 only", "3 and 4 only", "1, 2, 3, and 4"],
        "ans": 3,
        "sol": "All four river bank pairings are correct: Harappa (Ravi), Mohenjo-daro (Indus), Lothal (Bhogava), Kalibangan (Ghaggar)."
    },
    {
        "q": "Consider the following statements regarding the decline of the Indus Valley Civilization:\n1. Sir Mortimer Wheeler suggested an Aryan Invasion caused the sudden collapse.\n2. M.R. Sahni and Marshall argued that tectonic shifts led to devastating flooding.\n3. Amalanda Ghosh and Sood proposed that the drying of the Sarasvati/Ghaggar River dry broke the agricultural base.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 3,
        "sol": "All three theories and their proponents are correctly described, reflecting the multi-causal perspective of the decline."
    },
    {
        "q": "Which of the following is/are unique characteristics of the Harappan site of Dholavira?\n1. Complete absence of brick fortifications.\n2. Division of the town into three zones: Citadel, Middle Town, and Lower Town.\n3. The presence of massive stone-cut water reservoirs.\nSelect the correct answer:",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2, and 3"],
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Statement 1 is incorrect because Dholavira features massive stone fortifications around its Citadel and zones."
    },
    {
        "q": "Consider the following statements:\nStatement I: The Harappans were the first in the world to domesticate the horse and use it in warfare.\nStatement II: The Harappan script is written in Boustrophedon style.\nWhich of the following is correct?",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 1,
        "sol": "Statement I is incorrect because Harappans did not domesticate or regularly use horses, let alone use them in warfare (horses became prominent during the Vedic period). Statement II is correct."
    },
    {
        "q": "Consider the following statements regarding the Late Harappan hoard found at Mandi, UP:\n1. It was discovered in the year 2000 during agricultural excavation.\n2. The hoard yielded gold jewelry, copper vessels, and thousands of micro-beads.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Mandi in UP is a late Harappan site where local farmers unzipped a massive hoard of gold ornaments and beads in 2000."
    }
]

# ----------------- SECTION MASTERY ZONE GENERATION (mastery.json) -----------------
# We will create 12 high-quality questions for each of the 6 sections

# Section 1: Historiography, Discovery Teams & Decipherment Attempts
sec1_questions = [
    {
        "type": "MCQ",
        "q": "Who was the first European traveler to visit Harappa and document the presence of ancient brick mounds in 1826?",
        "opts": ["Alexander Cunningham", "Charles Masson", "John Marshall", "Dayaram Sahni"],
        "ans": 1,
        "sol": "Charles Masson visited Harappa in 1826 and described the ruins in his book, marking the first European record of the site."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following pioneers are correctly associated with their contributions to IVC discovery? (Select all that apply)",
        "opts": [
            "Dayaram Sahni - Excavation of Harappa (1921)",
            "R.D. Banerjee - Discovery of Mohenjo-daro (1922)",
            "Sir John Marshall - Announcement of the discovery of IVC (1924)",
            "Alexander Cunningham - First decipherment of the Harappan script"
        ],
        "ans": [0, 1, 2],
        "sol": "Sahni, Banerjee, and Marshall are correctly matched. The Harappan script remains undeciphered; Cunningham did not decipher it."
    },
    {
        "type": "True/False",
        "q": "True or False: The Harappan script is written from left-to-right in all lines.",
        "ans": False,
        "sol": "The Harappan script is written in Boustrophedon style, which alternates from right-to-left in the first line and left-to-right in the next."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The writing style where successive lines are written in opposite directions is known as ________.",
        "ans": "Boustrophedon",
        "sol": "Boustrophedon is a Greek term meaning 'as the ox turns' while ploughing, referring to alternating directions of text."
    },
    {
        "type": "Match the Following",
        "q": "Match the discoverers with the year of their breakthrough:",
        "items": [
            {"left": "I. Dayaram Sahni (Harappa)", "key": "A"},
            {"left": "II. R.D. Banerjee (Mohenjo-daro)", "key": "B"},
            {"left": "III. John Marshall (Official Announcement)", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "1921"},
            {"val": "B", "text": "1922"},
            {"val": "C", "text": "1924"}
        ],
        "sol": "Dayaram Sahni (I-A), R.D. Banerjee (II-B), John Marshall (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Which British geologist is known as the 'Father of Indian Prehistory' (who collected early stone tools)?",
        "sol": "Robert Bruce Foote."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Indus Valley Civilization is placed under Proto-history.<br><strong>Reason (R):</strong> The Harappan script is pictographic and remains undeciphered, preventing historians from reading direct literary accounts of the period.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are correct. Proto-history designates the phase containing undeciphered script, making R the exact explanation."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Alexander Cunningham collected the first Harappan seals in the 19th century but failed to recognize their age, thinking they were historic relics.<br>Statement II: R.D. Banerjee discovered Mohenjo-daro while excavating a medieval Hindu temple.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because R.D. Banerjee was excavating a Kushan-period Buddhist stupa, not a Hindu temple."
    },
    {
        "type": "Why",
        "q": "Why is it difficult for historians to reconstruct the political system of the Harappans?",
        "sol": "Because the Harappan script remains undeciphered. Without written administrative records, treaties, or laws, historians must rely entirely on material remains, making political interpretations hypothetical."
    },
    {
        "type": "How",
        "q": "How does the pictographic nature of the Harappan script compare to contemporary scripts in Mesopotamia?",
        "sol": "Mesopotamian cuneiform script evolved into phonetic, wedge-shaped signs representing syllables and sounds. The Harappan script remained highly pictographic (depicting fish, birds, humans, and objects) with 375 to 400 signs, suggesting a combination of logographic and syllabic writing that never fully transitioned to an alphabet."
    },
    {
        "type": "Case Study",
        "q": "An epigraphist uncovers a seal with writing. The first line runs right-to-left. The second line runs left-to-right. Identify the writing style.",
        "sol": "The writing style is Boustrophedon."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the role of Sir John Marshall in establishing the Indus Valley Civilization on the global map.",
        "sol": "Sir John Marshall, as Director-General of the ASI, coordinated the separate discoveries at Harappa (Sahni) and Mohenjo-daro (Banerjee). In 1924, he published a landmark announcement in the London Illustrated News, officially declaring the discovery of a major urban civilization, thereby placing ancient India on par with early Egypt and Mesopotamia."
    }
]

# Section 2: Geographical Extent & Detailed Site Profile
sec2_questions = [
    {
        "type": "MCQ",
        "q": "Which of the following boundary sites of the Indus Valley Civilization is correctly matched with its river?",
        "opts": [
            "Manda - River Ravi",
            "Alamgirpur - Hindon River",
            "Daimabad - Narmada River",
            "Sutkagen-dor - Indus River"
        ],
        "ans": 1,
        "sol": "Alamgirpur stands on the Hindon River (UP). Manda is on the Chenab; Daimabad is on the Pravara/Godavari; Sutkagen-dor is on the Dasht."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following mature Harappan sites are located in the state of Gujarat? (Select all that apply)",
        "opts": [
            "Lothal",
            "Dholavira",
            "Surkotada",
            "Banawali"
        ],
        "ans": [0, 1, 2],
        "sol": "Lothal, Dholavira, and Surkotada are all in Gujarat. Banawali is in Haryana."
    },
    {
        "type": "True/False",
        "q": "True or False: Rakhigarhi in Haryana is the largest Harappan site, exceeding the size of Mohenjo-daro.",
        "ans": True,
        "sol": "Recent excavations have established Rakhigarhi as the largest Harappan site, measuring over 350 hectares."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The northernmost site of the Indus Valley Civilization, Manda, is located on the banks of the ________ River.",
        "ans": "Chenab",
        "sol": "Manda in Jammu is situated on the right bank of the Chenab River."
    },
    {
        "type": "Match the Following",
        "q": "Match the Harappan sites with their primary archaeological features:",
        "items": [
            {"left": "I. Dholavira", "key": "A"},
            {"left": "II. Lothal", "key": "B"},
            {"left": "III. Kalibangan", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Three-tier town division and water reservoirs"},
            {"val": "B", "text": "Artificial brick dockyard"},
            {"val": "C", "text": "Earliest ploughed field furrow marks"}
        ],
        "sol": "Dholavira (I-A), Lothal (II-B), Kalibangan (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Name the only Harappan site located in the state of Maharashtra.",
        "sol": "Daimabad."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> Dholavira is unique among mature Harappan sites.<br><strong>Reason (R):</strong> It is divided into three parts: Citadel, Middle Town, and Lower Town, and features monumental stone-cut reservoirs.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both Assertion and Reason are true. The three-tier city planning and reservoirs make Dholavira unique compared to standard two-part cities."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Chanhudaro is the only Harappan city built without a fortified Citadel.<br>Statement II: The site of Kalibangan translates to 'Black Bangles'.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 2,
        "sol": "Both statements are correct. Chanhudaro has no citadel (artisan town); Kalibangan is named after black bangles found there."
    },
    {
        "type": "Why",
        "q": "Why is the site of Lothal referred to as a port city of the Harappan civilization?",
        "sol": "Lothal features a massive baked-brick basin connected to the Gulf of Khambhat via a river channel. It had inlet and outlet sluice gates to manage water levels during tides, allowing ships to dock, load, and unload goods, confirming its function as a tidal port."
    },
    {
        "type": "How",
        "q": "How does Dholavira's urban plan differ from typical Harappan layouts like Harappa and Mohenjo-daro?",
        "sol": "Standard cities have two parts (West Citadel, East Lower Town) built primarily of mud-brick. Dholavira has three divisions (Citadel, Middle Town, Lower Town), is built with significant amounts of locally available dressed stone, and is surrounded by a massive network of interconnected stone water reservoirs."
    },
    {
        "type": "Case Study",
        "q": "Archaeologists uncover a Harappan site containing horse bones in the upper layers and pot burials marked by large stone slabs. Identify the site.",
        "sol": "The site is Surkotada in Gujarat."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the significance of the archaeological discoveries made at Kalibangan.",
        "sol": "Kalibangan in Rajasthan provides critical insights into early agriculture and ritual life: 1) It has the earliest ploughed field furrow grid, indicating double-cropping. 2) It has brick platforms with fire altars, suggesting community ritual activity. 3) It shows unique architectural features like decorated floor tiles and a wooden drainage furrow, reflecting a distinct regional Harappan variant."
    }
]

# Section 3: Advanced Town Planning, Civic Infrastructure & Engineering
sec3_questions = [
    {
        "type": "MCQ",
        "q": "What was the standardized dimension ratio of bricks used in mature Harappan constructions?",
        "opts": ["3:2:1", "4:2:1", "5:3:1", "4:3:2"],
        "ans": 1,
        "sol": "Harappan bricks were standardized in a ratio of 4:2:1 (length:breadth:thickness) across all settlements."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following are characteristics of the Harappan drainage system? (Select all that apply)",
        "opts": [
            "Drains were covered with brick or stone slabs",
            "Inspection manholes (sumps) were provided at regular intervals",
            "Drains ran under the main streets",
            "Drains emptied directly into local drinking water wells"
        ],
        "ans": [0, 1, 2],
        "sol": "Drains were covered, had inspection sumps, and ran under streets. They did not empty into drinking wells; they led outside the city walls."
    },
    {
        "type": "True/False",
        "q": "True or False: Harappan houses typically opened their main doors and windows directly onto the wide main streets.",
        "ans": False,
        "sol": "Houses opened onto side lanes rather than main streets to ensure privacy and avoid dust/noise."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The layout system where streets intersect at right angles, forming rectangular blocks, is called the ________ system.",
        "ans": "Grid",
        "sol": "The Grid system or gridiron pattern was the hallmark of Harappan urban layouts."
    },
    {
        "type": "Match the Following",
        "q": "Match the structures with their urban locations:",
        "items": [
            {"left": "I. The Great Bath", "key": "A"},
            {"left": "II. Large Residential Blocks", "key": "B"},
            {"left": "III. Fortification Walls", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Citadel (West)"},
            {"val": "B", "text": "Lower Town (East)"},
            {"val": "C", "text": "City Boundaries / Perimeter"}
        ],
        "sol": "Great Bath (I-A), Residential Blocks (II-B), Fortification Walls (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Which type of brick (baked or sun-dried) was primarily used for constructing drains and citadels in Mohenjo-daro?",
        "sol": "Baked (kiln-burnt) bricks."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Harappan street drains represent a high degree of sanitation planning.<br><strong>Reason (R):</strong> Street Drains were built using gypsum-cement mortar, covered with slabs, and integrated with sump pits for sewage waste collection.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both A and R are correct. The precise masonry work, gypsum mortar, covers, and sumps are the direct reasons for its sanitation success."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Every major household had its own brick-lined water well and private bathing area.<br>Statement II: The houses were built around a central courtyard, with rooms opening into it.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 2,
        "sol": "Both statements are correct. Private wells/baths and courtyard-centric housing are standard Harappan features."
    },
    {
        "type": "Why",
        "q": "Why did the Harappans place sump pits (manholes) along their covered street drains?",
        "sol": "To allow solid waste to settle in the pit while liquid waste flowed away. This prevented blockages and allowed municipal workers to lift the stone covers and clean out the accumulated debris easily."
    },
    {
        "type": "How",
        "q": "How did Harappan masonry ensure that water did not leak through the brick lining of the Great Bath?",
        "sol": "The Great Bath was made water-tight by laying fine bricks on edge, sealing them with a thick layer of gypsum mortar, and applying a backup layer of natural bitumen (tar) behind the brickwork to prevent any seepage."
    },
    {
        "type": "Case Study",
        "q": "A surveyor maps a newly discovered Harappan site. The brick dimensions are 28 cm x 14 cm x 7 cm. Analyze if this follows the standard Harappan ratio.",
        "sol": "Yes, because 28:14:7 simplifies to a ratio of 4:2:1, which is the exact mature Harappan standardized brick ratio."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the concept of 'Citadel' and 'Lower Town' in Harappan urban topography.",
        "sol": "Harappan settlements were divided into two main zones: 1) The Citadel (or Acropolis) sat on a raised mud-brick platform on the West. It was fortified and contained public structures (Great Bath, Granaries) and administrative offices, serving as the seat of authority. 2) The Lower Town lay on the East, at ground level. It was much larger, laid out in a grid pattern, and housed the residential quarters, shops, and workshops of the general population."
    }
]

# Section 4: Economy, Crafts, Trade Routes & Weights System
sec4_questions = [
    {
        "type": "MCQ",
        "q": "In the Mesopotamian records, which of the following places represents the name used for the Indus region?",
        "opts": ["Dilmun", "Meluhha", "Makan", "Elam"],
        "ans": 1,
        "sol": "Mesopotamian texts refer to trade with 'Meluhha', which is the ancient Sumerian word for the Indus Civilization."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following raw materials are correctly matched with their source regions? (Select all that apply)",
        "opts": [
            "Copper - Khetri Mines, Rajasthan",
            "Lapis Lazuli - Badakhshan, Afghanistan",
            "Gold - Kolar, Karnataka",
            "Tin - Kutch, Gujarat"
        ],
        "ans": [0, 1, 2],
        "sol": "Copper (Khetri), Lapis (Badakhshan), and Gold (Kolar) are correct. Tin was imported from Afghanistan/Central Asia, not Gujarat."
    },
    {
        "type": "True/False",
        "q": "True or False: The Harappan base unit of weight was based on the binary value of 16, which is equivalent to 13.63 grams.",
        "ans": True,
        "sol": "Lower weights followed a binary scale (1, 2, 4, 8, 16...) where the unit 16 (13.63g) was the primary standard."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The Harappan trading colony established in northern Afghanistan to secure Lapis Lazuli is called ________.",
        "ans": "Shortughai",
        "sol": "Shortughai was a mature Harappan outpost located near the lapis mines in Badakhshan."
    },
    {
        "type": "Match the Following",
        "q": "Match the imported raw materials with their geographical destinations:",
        "items": [
            {"left": "I. Copper", "key": "A"},
            {"left": "II. Lapis Lazuli", "key": "B"},
            {"left": "III. Gold", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Rajasthan (Khetri)"},
            {"val": "B", "text": "Afghanistan (Badakhshan)"},
            {"val": "C", "text": "Karnataka (Kolar)"}
        ],
        "sol": "Copper (I-A), Lapis (II-B), Gold (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "What fiber did the Harappans cultivate first in the world, which the Greeks called 'Sindon'?",
        "sol": "Cotton."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Harappan trading networks extended as far as Mesopotamia.<br><strong>Reason (R):</strong> Harappan steatite seals and carnelian beads have been excavated at Mesopotamian sites like Ur and Kish.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are correct. The physical presence of Harappan seals and beads in Mesopotamia confirms the trade link described in Assertion A."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Chanhudaro and Lothal were famous centers for bead manufacturing, utilizing carnelian and steatite.<br>Statement II: The Harappans traded directly with Mesopotamia without any intermediate ports.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because trade went through intermediate hubs like Dilmun (Bahrain) and Makan (Oman)."
    },
    {
        "type": "Why",
        "q": "Why did the Harappans establish a trading colony at Shortughai in northern Afghanistan?",
        "sol": "Shortughai was located near the Oxus River, directly adjacent to the only major ancient source of Lapis Lazuli (Badakhshan). By occupying this point, the Harappans secured a monopoly over this highly valued blue gemstone for their export market."
    },
    {
        "type": "How",
        "q": "How did the Harappan weight system differ between retail trade and bulk trade?",
        "sol": "For smaller retail items (beads, gems, metals), the system used a binary progression (1, 2, 4, 8, 16, 32, 64), ensuring high precision. For larger bulk trade items (grains, timber), the system switched to decimal groupings (100, 200, 500, etc.), allowing easy counting of bulk cargo."
    },
    {
        "type": "Case Study",
        "q": "An exchange merchant in Mesopotamia receives a shipment of timber stamped with a clay seal depicting a unicorn and Indus characters. Trace the origin of the seal.",
        "sol": "The seal originated in the Indus Valley (Meluhha), as the unicorn motif and pictographic script are diagnostic marks of Harappan trade seals."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the significance of the 'Meluhha' trade in Harappan economics.",
        "sol": "Mesopotamian records describe intensive trade with Meluhha. Harappans exported luxury craft items: copper, ivory combs, carnelian beads, gold ornaments, lapis lazuli, and cotton textiles. In return, they imported silver, wool, and olive oil. This maritime trade, facilitated by coastal ports like Lothal, brought massive wealth into the Indus Valley, supporting its urban infrastructure."
    }
]

# Section 5: Religion, Artworks & Script Analysis
sec5_questions = [
    {
        "type": "MCQ",
        "q": "The famous bronze Dancing Girl figurine discovered at Mohenjo-daro is depicted wearing bangles on which arm?",
        "opts": ["Right arm", "Left arm", "Both arms equally", "No bangles are shown"],
        "ans": 1,
        "sol": "The Dancing Girl is depicted wearing 24 bangles on her left arm, while her right arm has only a couple of bands."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following animals are depicted surrounding the yogic figure in the Pashupati Seal? (Select all that apply)",
        "opts": [
            "Elephant",
            "Tiger",
            "Rhinoceros",
            "Lion"
        ],
        "ans": [0, 1, 2],
        "sol": "The seal depicts an Elephant, Tiger, Rhinoceros, and Buffalo. Lion is not depicted (mnemonic: ETRB)."
    },
    {
        "type": "True/False",
        "q": "True or False: Archaeologists have excavated three massive stone temples in Mohenjo-daro, confirming institutionalized temple worship.",
        "ans": False,
        "sol": "No temples or public shrines have ever been found in Harappan ruins. Religion was practiced domestically."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The metallurgical technique used to cast the bronze Dancing Girl is known as the ________ process.",
        "ans": "Lost-Wax",
        "sol": "The Lost-Wax (cire perdue) process was used for casting hollow and solid metal sculptures."
    },
    {
        "type": "Match the Following",
        "q": "Match the artifacts with their material composition:",
        "items": [
            {"left": "I. Dancing Girl", "key": "A"},
            {"left": "II. Bearded Priest", "key": "B"},
            {"left": "III. Standard Seals", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Bronze"},
            {"val": "B", "text": "Steatite (Soapstone)"},
            {"val": "C", "text": "Terracotta / Faience"}
        ],
        "sol": "Dancing Girl (I-A), Bearded Priest (II-B), Standard Seals (III-B)."
    },
    {
        "type": "One-Liner",
        "q": "Which tree is most commonly depicted on Harappan seals and pottery, indicating its sacred status?",
        "sol": "Pipal tree (Ficus religiosa)."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> The Harappan script has not been successfully deciphered.<br><strong>Reason (R):</strong> The inscriptions are extremely short, averaging only 4-5 signs, and there is no bilingual inscription available to decode them.<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are correct. The short text length and lack of a bilingual parallel (like the Rosetta Stone) are the exact reasons why decipherment remains unsuccessful."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: The Pashupati seal is considered a proto-form of the Hindu deity Shiva.<br>Statement II: The Bearded Priest bust is depicted wearing a shawl with a trefoil pattern.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 2,
        "sol": "Both statements are correct. Pashupati represents Proto-Shiva; the Priest's shawl features a trefoil motif."
    },
    {
        "type": "Why",
        "q": "Why did the Harappans carve animals (like bulls, elephants, rhinos) on their trade seals?",
        "sol": "The animals served a dual purpose: they acted as identifiable symbols for illiterate traders who could recognize ownership by the animal icon, and they also represented clan totems or sacred guard animals protecting the contents."
    },
    {
        "type": "How",
        "q": "How was the Lost-Wax technique executed by Harappan bronze-smiths?",
        "sol": "First, a wax model of the figure was made. This wax model was coated in clay and dried. A small hole was made in the clay, and the model was heated, causing the wax to melt and drain out. Finally, molten bronze was poured into the hollow clay mold. Once cooled, the outer clay shell was broken away, revealing the solid bronze figure."
    },
    {
        "type": "Case Study",
        "q": "An antiquities dealer presents a stone bust of a man with half-closed eyes and a trefoil shawl, claiming it was found in Egypt. Evaluate this claim.",
        "sol": "The claim is false. The bust describes the 'Bearded Priest', which is a unique and famous artwork found exclusively at Mohenjo-daro."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the main features and religious significance of the Pashupati Seal.",
        "sol": "The Pashupati Seal from Mohenjo-daro depicts a seated male deity in a yogic posture, wearing horned headgear. He is surrounded by an Elephant, Tiger, Rhinoceros, and Buffalo, with two deer at his feet. Archaeologist John Marshall identified this as 'Proto-Shiva' because Shiva in later Hinduism is known as Pashupati (Lord of Animals), is associated with yoga (Mahayogi), and wears horned symbols (trident/crescent moon)."
    }
]

# Section 6: Decline Theories & Uttar Pradesh (UP) Special Harappan Sites
sec6_questions = [
    {
        "type": "MCQ",
        "q": "Which of the following Harappan sites represents the easternmost limit of the civilization, located on the Hindon River in UP?",
        "opts": ["Hulas", "Alamgirpur", "Mandi", "Sanauli"],
        "ans": 1,
        "sol": "Alamgirpur in Meerut district represents the easternmost boundary site of the Indus Valley Civilization."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following Late Harappan/Copper Hoard sites are located in Uttar Pradesh? (Select all that apply)",
        "opts": [
            "Alamgirpur",
            "Hulas",
            "Mandi",
            "Daimabad"
        ],
        "ans": [0, 1, 2],
        "sol": "Alamgirpur, Hulas, and Mandi are in UP. Daimabad is in Maharashtra."
    },
    {
        "type": "True/False",
        "q": "True or False: The Aryan Invasion theory proposed by Sir Mortimer Wheeler is currently accepted as the primary cause of Harappan decline.",
        "ans": False,
        "sol": "The Aryan Invasion theory has been largely discarded due to lack of genetic, archaeological, or chronological continuity. Multi-causal environmental factors are favored."
    },
    {
        "type": "Fill in the Blank",
        "q": "Fill in the blank: The Late Harappan site in Muzaffarnagar district, UP, where a massive hoard of gold jewelry was found in 2000 is ________.",
        "ans": "Mandi",
        "sol": "Mandi is the Muzaffarnagar site famous for the unearthing of a gold jewelry hoard."
    },
    {
        "type": "Match the Following",
        "q": "Match the decline theories with their primary proponents:",
        "items": [
            {"left": "I. Aryan Invasion", "key": "A"},
            {"left": "II. Massive Flooding", "key": "B"},
            {"left": "III. Drying of Sarasvati", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "Sir Mortimer Wheeler"},
            {"val": "B", "text": "M.R. Sahni / Robert Raikes"},
            {"val": "C", "text": "Amalanda Ghosh / Sood"}
        ],
        "sol": "Aryan Invasion (I-A), Flooding (II-B), Sarasvati Drying (III-C)."
    },
    {
        "type": "One-Liner",
        "q": "Which site in Baghpat district, UP, yielded copper-clad coffins and three wooden wheel chariots in 2018?",
        "sol": "Sanauli."
    },
    {
        "type": "Assertion-Reason",
        "q": "<strong>Assertion (A):</strong> Post 1900 BC, there was a major eastward migration of Harappan populations.<br><strong>Reason (R):</strong> The drying up of the Indus-Ghaggar river channels collapsed western agriculture, forcing migrations into the fertile Ganga-Yamuna Doab (modern western UP).<br>Select the correct code:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are correct, and R provides the direct ecological reason for the demographic shift into UP."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:<br>Statement I: Alamgirpur in UP yielded pottery showing cloth impressions, proving Harappan presence.<br>Statement II: The Late Harappan phase is marked by the expansion of urban centers and written tablets.<br>Select the correct option:",
        "opts": [
            "Statement I is correct but Statement II is incorrect",
            "Statement II is correct but Statement I is incorrect",
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect"
        ],
        "ans": 0,
        "sol": "Statement I is correct. Statement II is incorrect because the Late Harappan phase is marked by de-urbanization (rural settlements) and the disappearance of writing."
    },
    {
        "type": "Why",
        "q": "Why was the discovery of wooden chariots at Sanauli in UP in 2018 highly significant?",
        "sol": "Because it was the first discovery of actual physical chariots (with copper reinforcement and solid wheels) in a late-protohistoric burial context in India, proving that these communities possessed advanced military technology and wheel-craft contemporaneous with late Harappan cultures."
    },
    {
        "type": "How",
        "q": "How did the shift from the Mature Harappan to the Late Harappan phase affect craft production?",
        "sol": "Craft production became localized and simplified. Long-distance trade collapsed, so exotic raw materials (lapis lazuli, conch shells) vanished. High-quality steatite seals with script and bronze castings disappeared, replaced by simple, unpainted pottery and basic copper tools for local agricultural use."
    },
    {
        "type": "Case Study",
        "q": "Local villagers in western UP dig a field and unearth copper pots and several gold rings. Classify the site phase.",
        "sol": "This represents a Late Harappan hoard site, characteristic of Mandi in Muzaffarnagar district, UP."
    },
    {
        "type": "Teach the Concept",
        "q": "Explain the environmental theories for the decline of the Indus Valley Civilization.",
        "sol": "Environmental theories suggest the decline was driven by ecological collapse: 1) **Drying of Sarasvati (Ghaggar):** River shifts left major agricultural zones dry. 2) **Tectonic Flooding:** Crustal movements blocked the Indus, turning Mohenjo-daro into a swamp. 3) **Ecological Imbalance:** Proponents like Fairservis argue that centuries of brick-baking and animal overgrazing stripped the forests and depleted the soil, making the cities unsustainable."
    }
]

mastery_sections = [
    {
        "title": "1. Historiography, Discovery Teams & Decipherment Attempts",
        "masteryZone": sec1_questions
    },
    {
        "title": "2. Geographical Extent & Detailed Site Profile",
        "masteryZone": sec2_questions
    },
    {
        "title": "3. Advanced Town Planning, Civic Infrastructure & Engineering",
        "masteryZone": sec3_questions
    },
    {
        "title": "4. Economy, Crafts, Trade Routes & Weights System",
        "masteryZone": sec4_questions
    },
    {
        "title": "5. Religion, Artworks & Script Analysis",
        "masteryZone": sec5_questions
    },
    {
        "title": "6. Decline Theories & Uttar Pradesh (UP) Special Harappan Sites",
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
print("theory.json generated successfully.")

# Save mastery.json
with open(os.path.join(BASE_DIR, "mastery.json"), "w", encoding="utf-8") as f:
    json.dump(processed_mastery, f, ensure_ascii=False, indent=4)
print("mastery.json generated successfully.")

# Save practice.json
practice_data = {
    "practiceQuestions": practice_questions,
    "mockTestQuestions": mock_questions
}
processed_practice = process_data(practice_data)
with open(os.path.join(BASE_DIR, "practice.json"), "w", encoding="utf-8") as f:
    json.dump(processed_practice, f, ensure_ascii=False, indent=4)
print("practice.json generated successfully.")
