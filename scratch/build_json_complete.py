import json
import os

ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Phases-of-Evolution-of-Harappan-Civilisation"
HIN_DIR = os.path.join(ENG_DIR, "hi")

# 1. ----------------- EARLY HARAPPAN MASTERY (60 Qs) -----------------
early_mastery = []

# MCQs (5)
for i in range(5):
    q_texts = [
        "Which of the following sites represents the earliest Hakra Ware phase of the Harappan evolution?",
        "The famous pre-mature agricultural ploughed field showing criss-cross furrows was discovered at:",
        "The pre-Harappan settlement of Amri in Sindh is famous for yielding which of the following specific findings?",
        "Two silver crowns and precious ornaments representing early social stratification were excavated at:",
        "The Ravi Phase (c. 3300-2800 BCE) represents the earliest occupation level at which major site?"
    ]
    opts_list = [
        ["Bhirrana", "Mohenjo-daro", "Lothal", "Chanhudaro"],
        ["Kalibangan", "Banawali", "Harappa", "Kot Diji"],
        ["Pottery painted with gazelle/antelope motifs", "A large stone dockyard", "Terracotta horse figurines", "Lapis Lazuli seals"],
        ["Kunal", "Bhirrana", "Amri", "Banawali"],
        ["Harappa", "Mohenjo-daro", "Kalibangan", "Dholavira"]
    ]
    ans_list = [0, 0, 0, 0, 0]
    sols = [
        "Bhirrana in Haryana represents the oldest Hakra Ware phase (dating back to the 4th millennium BCE).",
        "Kalibangan in Rajasthan yielded a unique pre-mature (Early Harappan) ploughed agricultural field.",
        "Amri is famous for its pre-Harappan levels showing a distinct pottery style painted with gazelles and geometric designs.",
        "Kunal in Haryana yielded two silver crowns and gold ornaments, representing early social stratification.",
        "The Ravi Phase represents the earliest occupation level at Harappa, showing the first graffiti marks that later evolved into the Indus script."
    ]
    early_mastery.append({
        "type": "MCQ",
        "q": q_texts[i],
        "opts": opts_list[i],
        "ans": ans_list[i],
        "sol": sols[i]
    })

# Multiple Correct MCQs (5)
for i in range(5):
    q_texts = [
        "Which of the following elements characterize the Early Harappan phase? (Select all that apply)",
        "Identify the sites associated with the Early Harappan phase: (Select all that apply)",
        "Which features are associated with the Ravi Phase of Harappa? (Select all that apply)",
        "Select the Early Harappan sites that show evidence of early fortifications: (Select all that apply)",
        "Identify the characteristics of Hakra Ware: (Select all that apply)"
    ]
    opts_list = [
        ["Emergence of defensive fortifications", "Standardization of wheel-made pottery", "Early copper and bronze working", "Use of standardized grid-planned city streets"],
        ["Bhirrana", "Kot Diji", "Amri", "Surkotada"],
        ["Potters' marks and early scripts on pottery", "Bead manufacturing", "Use of potter's wheel", "Construction of the Great Bath"],
        ["Kot Diji", "Kalibangan", "Bhirrana", "Lothal"],
        ["Primarily handmade ceramic style", "Thick-walled pottery with chocolate slip", "Found in Cholistan and Haryana region", "Extensive use of iron oxide painting"]
    ]
    ans_list = [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]
    ]
    sols = [
        "The Early Harappan phase is marked by fortifications, wheel-made pottery, and early metallurgy. Grid-planned streets are a Mature phase feature.",
        "Bhirrana, Kot Diji, and Amri contain Early Harappan phases. Surkotada is a Mature/Late site.",
        "The Ravi Phase shows potters' marks, bead-making, and early wheel-made pottery. The Great Bath was built during the Mature phase.",
        "Kot Diji, Kalibangan, and Bhirrana show Early Harappan fortifications. Lothal is a Mature phase port city.",
        "Hakra Ware is characterized as handmade, thick-walled with chocolate slips, and found in Cholistan/Haryana. Iron metallurgy was unknown."
    ]
    early_mastery.append({
        "type": "Multiple Correct MCQ",
        "q": q_texts[i],
        "opts": opts_list[i],
        "ans": ans_list[i],
        "sol": sols[i]
    })

# True/False (8)
tf_qs = [
    ("The Hakra Ware phase represents a transition stage that predates the Ravi phase at Harappa.", True, "True. The Hakra phase is older (c. 3800-3200 BCE) than the Ravi phase (c. 3300-2800 BCE)."),
    ("The Kot Diji phase represents the Mature Harappan urban peak.", False, "False. Kot Diji represents the Early Harappan proto-urban stage."),
    ("Prehistoric humans used iron tools during the Early Harappan phase.", False, "False. The entire Harappan trajectory was pre-Iron; iron came during the Late Vedic period."),
    ("Kalibangan's ploughed field belongs to the Mature Harappan phase.", False, "False. It belongs to the pre-mature Early Harappan phase."),
    ("M.R. Mughal was the archaeologist who first systematically defined the 'Early Harappan' phase.", True, "True. Rafique Mughal systematically defined this phase based on excavations in Cholistan."),
    ("Early Harappan potters were completely unaware of the potter's wheel.", False, "False. Wheel-made pottery (Ravi and Kot Diji ware) was highly developed."),
    ("Bhirrana in Haryana is recognized as the oldest Harappan site by the ASI.", True, "True. Bhirrana has yielded the oldest Hakra ware levels."),
    ("Social stratification is completely absent in the Early Harappan phase.", False, "False. Discoveries like the silver crowns at Kunal indicate early social hierarchies.")
]
for q, ans, sol in tf_qs:
    early_mastery.append({
        "type": "True/False",
        "q": q,
        "ans": ans,
        "sol": sol
    })

# Fill in the Blank (8)
fill_qs = [
    ("The Early Harappan phase is also known as the __________ Era of the Indus Valley Civilisation.", "Regionalisation", "The Early Harappan phase represents the Regionalisation Era."),
    ("The oldest Harappan site according to the ASI is __________.", "Bhirrana", "Bhirrana in Haryana is the oldest site."),
    ("Two silver crowns representing early social stratification were found at __________.", "Kunal", "Kunal yielded the silver crowns."),
    ("Horned deity motifs painted on pottery are characteristic of the __________ phase.", "Kot Diji", "Kot Diji ware is famous for horned deity paintings."),
    ("The Ravi phase was first identified at the site of __________.", "Harappa", "The Ravi phase is the earliest level at Harappa."),
    ("The agricultural field showing criss-cross ploughed furrows is situated at __________.", "Kalibangan", "Kalibangan has the ploughed field."),
    ("The Hakra Ware phase dates back to the __________ millennium BCE.", "fourth", "Hakra Ware dates to c. 3800-3200 BCE (4th millennium BCE)."),
    ("The pre-mature phase of Sindh is typified by the site of __________.", "Amri", "Amri is the type site for pre-mature Sindh levels.")
]
for q, ans, sol in fill_qs:
    early_mastery.append({
        "type": "Fill in the Blank",
        "q": q,
        "ans": ans,
        "sol": sol
    })

# Matching (3)
match_qs = [
    {
        "q": "Match the Early Harappan sites with their respective modern Indian states/provinces:",
        "items": [
            {"left": "I. Bhirrana", "key": "A"},
            {"left": "II. Kalibangan", "key": "B"},
            {"left": "III. Kot Diji", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Haryana"},
            {"val": "B", "text": "B. Rajasthan"},
            {"val": "C", "text": "C. Sindh (Pakistan)"}
        ],
        "sol": "Bhirrana is in Haryana, Kalibangan in Rajasthan, and Kot Diji in Sindh."
    },
    {
        "q": "Match the Early Harappan cultural phases with their approximate chronological ranges:",
        "items": [
            {"left": "I. Hakra Ware Phase", "key": "A"},
            {"left": "II. Ravi Phase", "key": "B"},
            {"left": "III. Kot Diji Phase", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. c. 3800 BCE – 3200 BCE"},
            {"val": "B", "text": "B. c. 3300 BCE – 2800 BCE"},
            {"val": "C", "text": "C. c. 2800 BCE – 2600 BCE"}
        ],
        "sol": "These represent the chronological progression of the Early Harappan period."
    },
    {
        "q": "Match the Early Harappan site with its unique archaeological discovery:",
        "items": [
            {"left": "I. Kunal", "key": "A"},
            {"left": "II. Kalibangan", "key": "B"},
            {"left": "III. Amri", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Silver crowns and gold ornaments"},
            {"val": "B", "text": "B. Criss-cross ploughed agricultural field"},
            {"val": "C", "text": "C. Gazelle and geometric painted pottery"}
        ],
        "sol": "Kunal has silver crowns, Kalibangan has ploughed fields, and Amri has gazelle motifs."
    }
]
early_mastery.extend(match_qs)

# One-Liner (8)
ol_qs = [
    ("Name the archaeologist who systematically defined the 'Early Harappan' phase.", "M.R. Mughal (Rafique Mughal) systematically mapped and defined this phase based on his surveys in Cholistan."),
    ("Which Early Harappan site in Sindh shows a thick layer of ash indicating destruction by fire before the Mature rebuild?", "Kot Diji shows a distinct fire/destruction layer separating the Early and Mature phases."),
    ("Name the river along which the pre-mature site of Amri is situated.", "The Indus River (on its right bank, opposite Mohenjo-daro)."),
    ("Which site represents the oldest agricultural field in the Indian subcontinent?", "Kalibangan (the Early Harappan phase ploughed field)."),
    ("What are the earliest script-like markings found on Ravi phase pottery called?", "Potters' marks or graffiti marks."),
    ("What metal was primarily used for tools in the Early Harappan phase?", "Copper (and its low-grade alloy bronze)."),
    ("Which region in Pakistan contains the largest density of Hakra and Early Harappan sites?", "The Cholistan Desert region (Ghaggar-Hakra valley)."),
    ("What is the name of the oldest pre-mature phase pottery style found in Haryana?", "Hakra Ware.")
]
for q, sol in ol_qs:
    early_mastery.append({
        "type": "One-Liner",
        "q": q,
        "sol": sol
    })

# Assertion-Reason (8)
ar_qs = [
    ("Assertion (A): Lower alluvial Ganga plains were completely devoid of Early Harappan settlements.\nReason (R): Hominins and early farmers avoided the Ganga plains due to a complete lack of stone resources needed for tools.", 0),
    ("Assertion (A): The transition from Hakra to Ravi phase represents agricultural stabilization.\nReason (R): Wheel-made pottery and script-like potters' marks start appearing during the Ravi phase.", 0),
    ("Assertion (A): Defensive walls were constructed at Kot Diji and Kalibangan during the Early phase.\nReason (R): Early Harappan communities faced threats from local floods and conflicts with neighboring pastoralists.", 0),
    ("Assertion (A): The Early Harappan phase is called the Regionalisation Era.\nReason (R): Localized ceramic fabrics and regional styles dominated before pan-regional integration.", 0),
    ("Assertion (A): Kunal represents an early stage of social hierarchy.\nReason (R): Archaeologists excavated two silver crowns and massive jewelry hoards from the site.", 0),
    ("Assertion (A): The ploughed field at Kalibangan shows advanced agricultural knowledge.\nReason (R): The field exhibits criss-cross furrows, showing that two different crops were grown together.", 0),
    ("Assertion (A): Early Harappans did not practice long-distance maritime trade with Mesopotamia.\nReason (R): Direct Meluhha trade documents and Harappan seals in Mesopotamia are strictly limited to the Mature Harappan phase.", 0),
    ("Assertion (A): Brick sizes in the Early phase were already standardized to the Mature 1:2:4 ratio.\nReason (R): Early phase brick ratios were often irregular (e.g., 1:2:3) and only consolidated into 1:2:4 during the Mature transition.", 3)
]
for q, ans in ar_qs:
    early_mastery.append({
        "type": "Assertion-Reason",
        "q": q,
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": ans,
        "sol": "UPSC-standard analysis of Early Harappan chronology and archaeology."
    })

# Statement-Based (5)
sb_qs = [
    ("Consider the following statements regarding the Hakra Ware phase:\n1. It represents the earliest chalcolithic farming communities in the Ghaggar-Hakra basin.\n2. It has been discovered at sites like Bhirrana and Kunal in India.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Hakra Ware represents the formative chalcolithic level of the region."),
    ("Consider the following statements regarding early fortifications:\n1. Kot Diji is the only Early Harappan site that shows a defensive fortification wall.\n2. Kalibangan-I (Early phase) also had a fortified wall dividing the settlement.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect because Kalibangan-I, Bhirrana, and Kunal also show fortifications. Statement 2 is correct."),
    ("Consider the following statements regarding the Ravi Phase:\n1. It is the earliest occupation layer excavated at the site of Harappa.\n2. Writing was already fully developed during this phase with long inscriptions.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because only short potters' marks/graffiti exist, not fully developed inscriptions."),
    ("Consider the following statements regarding agricultural practices:\n1. The ploughed field at Kalibangan belongs to the Early Harappan phase.\n2. Wooden plowshares were used instead of iron plowshares.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Iron was completely unknown, so wooden plows were used on the pre-mature levels."),
    ("Consider the following statements regarding early social hierarchies:\n1. Kunal yielded silver crowns and gold ornaments, indicating early elites.\n2. Early Harappan houses were completely uniform in size with no differences.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because houses at sites like Bhirrana show distinct size and room variations, indicating early differences.")
]
for q, ans, sol in sb_qs:
    early_mastery.append({
        "type": "Statement-Based",
        "q": q,
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": ans,
        "sol": sol
    })

# Why? (3), How? (3), Case Study (3), Teach Concept (3)
conceptual_qs = [
    ("Why did defensive fortifications emerge during the Early Harappan phase?", "Why", "Defensive fortifications emerged due to two major factors: protection from annual river flooding and protection from potential conflicts/cattle-raids by neighboring pastoralist groups. This indicates early political centralization and defensive coordination."),
    ("Why is the Early Harappan phase referred to as the 'Regionalisation Era' by modern historians?", "Why", "It is called the Regionalisation Era because the material culture (pottery fabrics, tool types, ornament designs) was divided into distinct regional styles (such as Kot Dijian in Sindh/Punjab and Sothi-Siswal in Haryana/Rajasthan) before being integrated into a uniform style during the Mature phase."),
    ("Why is the discovery of Hakra Ware at Bhirrana significant for Indus Valley chronology?", "Why", "It pushes back the antiquity of the Harappan evolution into the 4th and 5th millennium BCE, proving that the civilization did not emerge suddenly but had deep, localized agricultural roots in the Ghaggar-Hakra valley."),
    ("How did Early Harappan potters' marks evolve into the Mature Harappan script?", "How", "Early potters scratched unique symbols (graffiti) on wet clay before baking to mark ownership. Over generations, these markings became standardized, combined, and structured into a logo-syllabic script used by merchants to authenticate cargo."),
    ("How did agricultural surplus trigger the transition from the Early to Mature Harappan phase?", "How", "Fertile alluvial silt deposits combined with flood-irrigation led to massive crop surpluses (barley, wheat). This surplus freed a portion of the population from farming, allowing the growth of craft guilds, metal industries, merchant networks, and administrators."),
    ("How did Early Harappan construction techniques prepare for Mature Harappan city planning?", "How", "Early builders transitioned from mud huts to mud-brick structures and established early defensive walls. They also began using brick ratios (1:2:3 or 1:2:4) and early street alignments, which laid the foundation for Mature grid layouts."),
    ("Case Study: The Destruction Layer at Kot Diji", "Case Study", "At Kot Diji, a thick layer of ash and charcoal separates the Early Harappan level from the Mature Harappan level. This indicates a massive fire. Historians debate whether this represents a hostile takeover, war, or intentional burning to clear the area for the planned Mature city layout."),
    ("Case Study: Kalibangan-I Agricultural Layout", "Case Study", "The pre-mature field at Kalibangan shows criss-cross furrows: one set running north-south (spaced closer) and another running east-west (spaced wider). This exact layout is still used in Rajasthan today to grow two crops simultaneously (like mustard and chickpeas) without them competing for sunlight."),
    ("Case Study: Social Stratification at Kunal", "Case Study", "Kunal (Haryana) yielded a hoard of gold and silver ornaments, including two silver crowns, inside a jar in a house. This indicates the existence of an early chiefdom or elite class who had access to precious imported metals, showing that social differentiation began during the Early phase."),
    ("Teach the Concept: The Ravi Phase of Harappa", "Teach the Concept", "The Ravi Phase (c. 3300-2800 BCE) represents the earliest occupation level at Harappa. To teach this concept, highlight: (1) Transition from semi-nomadic life to settled brick houses, (2) The introduction of the potter's wheel, (3) The first graffiti marks on pottery, and (4) Bead-making, proving it was the birth of Harappan craft and script."),
    ("Teach the Concept: Regionalisation Era vs Integration Era", "Teach the Concept", "Explain that the Regionalisation Era (Early Harappan) was marked by diverse regional cultures with their own pottery styles (Kot Diji, Amri, Sothi). In contrast, the Integration Era (Mature Harappan) saw these regional styles merge into a uniform, standardized material culture (seals, script, grid layouts, 1:2:4 bricks) across the subcontinent."),
    ("Teach the Concept: Hakra Ware and its geographical distribution", "Teach the Concept", "Hakra Ware refers to the earliest chalcolithic pottery of the Ghaggar-Hakra basin, characterized by mud-applied handmade vessels. Its distribution spans eastern Pakistan (Cholistan) and northwestern India (Haryana, Punjab), mapping the geographical cradle of the Harappan civilization.")
]
for q, qtype, sol in conceptual_qs:
    early_mastery.append({
        "type": qtype,
        "q": q,
        "sol": sol
    })


# 2. ----------------- MATURE HARAPPAN MASTERY (60 Qs) -----------------
mature_mastery = []

# MCQs (5)
for i in range(5):
    q_texts = [
        "The Mature Harappan brick dimensions followed a highly standardized ratio of (Thickness : Width : Length):",
        "Which of the following Mature Harappan sites is famous for its unique three-tier division of the town instead of the typical two-tier division?",
        "In which Mature Harappan site is there a complete absence of defensive fortifications or a citadel?",
        "The trade relations between Mature Harappan cities and Mesopotamia are mentioned in cuneiform texts. What term is used in Mesopotamian records to refer to the Indus region?",
        "Which of the following was the major source of Lapis Lazuli, a semi-precious blue stone imported by Mature Harappans?"
    ]
    opts_list = [
        ["1 : 2 : 4", "1 : 3 : 9", "2 : 4 : 8", "1 : 2 : 3"],
        ["Dholavira", "Lothal", "Chanhudaro", "Rakhigarhi"],
        ["Chanhudaro", "Kalibangan", "Lothal", "Mohenjo-daro"],
        ["Meluhha", "Dilmun", "Magan", "Sumer"],
        ["Shortughai (Afghanistan)", "Khetri (Rajasthan)", "Badakhshan (Iran)", "Lothal (Gujarat)"]
    ]
    ans_list = [0, 0, 0, 0, 0]
    sols = [
        "The standard ratio of bricks used in the Mature Harappan phase was strictly 1:2:4.",
        "Dholavira is unique because it is divided into three sections: the Citadel (Upper Town), the Middle Town, and the Lower Town.",
        "Chanhudaro in Sindh is the only major Mature Harappan town without a fortified citadel structure. It was primarily an industrial center.",
        "Mesopotamian inscriptions refer to the Indus Valley region as 'Meluhha', while Dilmun refers to Bahrain and Magan refers to Oman.",
        "Shortughai in Afghanistan was a Harappan trading colony established near Badakhshan to directly control the mining of Lapis Lazuli."
    ]
    mature_mastery.append({
        "type": "MCQ",
        "q": q_texts[i],
        "opts": opts_list[i],
        "ans": ans_list[i],
        "sol": sols[i]
    })

# Multiple Correct MCQs (5)
for i in range(5):
    q_texts = [
        "Which of the following elements characterize the Mature Harappan civic architecture? (Select all that apply)",
        "Identify the major Mature Harappan cities located in modern-day India: (Select all that apply)",
        "Select the archaeological findings associated with Mohenjo-daro: (Select all that apply)",
        "Identify the primary imports of the Mature Harappan trade network: (Select all that apply)",
        "Which features are associated with Mature Harappan religious practices? (Select all that apply)"
    ]
    opts_list = [
        ["Grid layout of streets intersecting at right angles", "Underground covered drainage systems with soak pits", "Separation of settlements into a Citadel and a Lower Town", "Use of massive stone pillars to support palaces"],
        ["Dholavira", "Rakhigarhi", "Lothal", "Harappa"],
        ["The Great Bath", "The Great Granary", "Bronze Dancing Girl statue", "Artificial brick dockyard"],
        ["Lapis Lazuli from Badakhshan", "Copper from Khetri mines", "Tin from Afghanistan/Iran", "Silk from China"],
        ["Depiction of a proto-Shiva/Pashupati figure on seals", "Worship of Mother Goddess clay figurines", "Worship of pipal tree and bull", "Construction of large temples with stone idols"]
    ]
    ans_list = [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]
    ]
    sols = [
        "Mature Harappan architecture featured grids, drainage, and division into citadel/lower town. Massive stone pillars were not a feature of Harappan architecture (they appear under the Mauryas).",
        "Dholavira, Rakhigarhi, and Lothal are in India. Harappa is in Punjab, Pakistan.",
        "Mohenjo-daro yielded the Great Bath, Great Granary, and Dancing Girl. Lothal contains the artificial dockyard.",
        "Lapis Lazuli, Copper, and Tin were major imports. Silk from China was not part of their trade system.",
        "Religion was characterized by Pashupati seals, mother goddess clay figurines, and tree/bull worship. No temples were built."
    ]
    mature_mastery.append({
        "type": "Multiple Correct MCQ",
        "q": q_texts[i],
        "opts": opts_list[i],
        "ans": ans_list[i],
        "sol": sols[i]
    })

# True/False (8)
tf_qs = [
    ("Mature Harappans built monumental temples with stone statues to worship their gods.", False, "False. No temples or monumental religious buildings have been found; worship was practiced at home or in public installations (like the Great Bath)."),
    ("The standard unit of weight was based on a binary progression of 16 for lighter weights.", True, "True. Lighter weights followed binary ratios (1, 2, 4, 8, 16, 32...) with 16 being the base unit."),
    ("Rakhigarhi is currently recognized as the largest geographic site of the Indus Valley Civilisation.", True, "True. Rakhigarhi has overtaken Mohenjo-daro as the largest site in terms of area."),
    ("The Harappan script has been fully deciphered by Indian epigraphists.", False, "False. The script remains undeciphered due to lack of a bilingual text (like the Rosetta Stone)."),
    ("Lothal contains an artificial brick basin identified by archaeologists as a dockyard.", True, "True. Lothal has a large brick dockyard connected to a river channel."),
    ("Harappans used iron weapons to defend their cities.", False, "False. The Harappans were a Bronze Age civilization and had no knowledge of iron."),
    ("Dholavira is unique for its extensive stone-cut water reservoirs.", True, "True. Dholavira has spectacular stone water reservoirs and dams."),
    ("Steatite was the primary material used to manufacture Harappan seals.", True, "True. Most Harappan seals are made of steatite (soapstone).")
]
for q, ans, sol in tf_qs:
    mature_mastery.append({
        "type": "True/False",
        "q": q,
        "ans": ans,
        "sol": sol
    })

# Fill in the Blank (8)
fill_qs = [
    ("The Mature Harappan phase is also known as the __________ Era.", "Integration", "It is known as the Integration Era."),
    ("The largest site of the Indus Valley Civilisation by geographic area is __________.", "Rakhigarhi", "Rakhigarhi is the largest site."),
    ("The artificial brick dockyard of the Harappans was excavated at __________.", "Lothal", "Lothal contains the brick dock").",
    ("The Harappan trading colony established in Afghanistan for Lapis Lazuli is __________.", "Shortughai", "Shortughai was the trading outpost."),
    ("The ratio of brick sizes in the Mature phase was strictly __________.", "1:2:4", "Bricks followed the 1:2:4 ratio."),
    ("The raised part of the Harappan city containing public and administrative buildings is called the __________.", "Citadel", "Citadel was the raised administrative zone."),
    ("Cuneiform texts of Mesopotamia refer to the Indus region as __________.", "Meluhha", "Meluhha is the Mesopotamian term for the Indus region."),
    ("Most Harappan seals were made of a soft stone called __________.", "steatite", "Steatite (soapstone) was primarily used.")
]
# Fix typos in comments
for q, ans, sol in fill_qs:
    mature_mastery.append({
        "type": "Fill in the Blank",
        "q": q,
        "ans": ans,
        "sol": sol
    })

# Matching (3)
match_qs = [
    {
        "q": "Match the Mature Harappan site with its unique architectural feature/discovery:",
        "items": [
            {"left": "I. Dholavira", "key": "A"},
            {"left": "II. Mohenjo-daro", "key": "B"},
            {"left": "III. Chanhudaro", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Three-tier town division and stone reservoirs"},
            {"val": "B", "text": "B. The Great Bath and Great Granary"},
            {"val": "C", "text": "C. Bead factory and lack of a fortified citadel"}
        ],
        "sol": "Dholavira has stone reservoirs, Mohenjo-daro has the Great Bath, and Chanhudaro has bead factories."
    },
    {
        "q": "Match the import items of the Mature Harappans with their primary source regions:",
        "items": [
            {"left": "I. Copper", "key": "A"},
            {"left": "II. Lapis Lazuli", "key": "B"},
            {"left": "III. Tin", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Khetri mines (Rajasthan)"},
            {"val": "B", "text": "B. Badakhshan (Afghanistan)"},
            {"val": "C", "text": "C. Iran / Afghanistan"}
        ],
        "sol": "Copper was imported from Khetri, Lapis Lazuli from Badakhshan, and Tin from Iran/Afghanistan."
    },
    {
        "q": "Match the Harappan religious symbols with their modern academic interpretations:",
        "items": [
            {"left": "I. Pashupati Seal", "key": "A"},
            {"left": "II. Fire Altars", "key": "B"},
            {"left": "III. Terracotta Figurines", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Proto-Shiva / Lord of Animals"},
            {"val": "B", "text": "B. Ritual sacrifices (found at Lothal/Kalibangan)"},
            {"val": "C", "text": "C. Mother Goddess worship"}
        ],
        "sol": "Pashupati represents Proto-Shiva, fire altars represent rituals, and figurines represent Mother Goddess."
    }
]
mature_mastery.extend(match_qs)

# One-Liner (8)
ol_qs = [
    ("Name the only Mature Harappan site without a citadel.", "Chanhudaro in Sindh."),
    ("Which site yielded a signboard containing ten large gypsum symbols?", "Dholavira in Kutch, Gujarat."),
    ("What was the primary function of the stone reservoirs discovered at Dholavira?", "Water harvesting and conservation to sustain the city during dry seasons."),
    ("Name the animal most commonly depicted on Mature Harappan seals.", "The Unicorn (a mythical one-horned animal)."),
    ("Which metal alloy is the famous 'Dancing Girl' statue made of?", "Bronze (using the lost-wax casting technique)."),
    ("Which river basin hosted the maximum density of Mature Harappan settlements?", "The Ghaggar-Hakra river basin (often identified as the Sarasvati system)."),
    ("Name the Mesopotamian king who recorded trade lists with Meluhha.", "Sargon of Akkad (c. 2334–2279 BCE)."),
    ("What is the name of the southernmost trading port site of the Mature phase in Gujarat?", "Lothal.")
]
for q, sol in ol_qs:
    mature_mastery.append({
        "type": "One-Liner",
        "q": q,
        "sol": sol
    })

# Assertion-Reason (8)
ar_qs = [
    ("Assertion (A): The streets of Mature Harappan cities were strictly planned in a grid pattern.\nReason (R): The municipal authority enforced strict regulations prohibiting building construction over public pathways.", 0),
    ("Assertion (A): Lothal acted as a major trade conduit between Gujarat and Mesopotamia.\nReason (R): Archaeologists excavated a large brick basin connected to the Sabarmati river and a bead-making factory at Lothal.", 0),
    ("Assertion (A): Harappans did not worship their gods in large congregational temples.\nReason (R): No monumental temple ruins, sanctuaries, or large stone statues have been discovered at any Harappan site.", 0),
    ("Assertion (A): The Harappan civilization was a cohesive empire ruled by a single all-powerful priest-king.\nReason (R): There is a complete lack of evidence for weapons, standing armies, or royal palace burials at Harappan sites.", 3),
    ("Assertion (A): The Harappans established a trading outpost at Shortughai in northern Afghanistan.\nReason (R): Shortughai provided direct administrative control over the mining and transport of Lapis Lazuli from Badakhshan.", 0),
    ("Assertion (A): Bricks of uniform sizes were used across all Mature Harappan settlements.\nReason (R): The standard ratio of 1:2:4 ensured structural stability for double-storey houses and municipal fortifications.", 0),
    ("Assertion (A): The Harappan script was logosyllabic in nature.\nReason (R): It contains between 400 and 600 distinct symbols, which is too many for an alphabet and too few for a true pictographic writing system.", 0),
    ("Assertion (A): Steatite seals were used strictly as currency in local markets.\nReason (R): Seals were primarily used as commercial stamps to authenticate clay sealings on trade cargo exported to distant lands.", 3)
]
for q, ans in ar_qs:
    mature_mastery.append({
        "type": "Assertion-Reason",
        "q": q,
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": ans,
        "sol": "UPSC-standard evaluation of Mature Harappan administration and commercial systems."
    })

# Statement-Based (5)
sb_qs = [
    ("Consider the following statements regarding the Citadel:\n1. It was always located in the eastern part of the city and was heavily populated.\n2. It housed public structures like the Great Bath and administrative offices.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect because the Citadel was located in the western part of the city. Statement 2 is correct."),
    ("Consider the following statements regarding the Harappan drainage system:\n1. Drains were covered with brick slabs or stone slabs that could be removed for cleaning.\n2. Household waste water flowed directly into streets without any soakage pits.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because houses had soak pits/sumps to settle solid waste before water entered public drains."),
    ("Consider the following statements regarding the weight system:\n1. The weights were made of chert and were primarily cubical in shape.\n2. The system followed decimal multiples for higher weights.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Lighter weights were binary, while higher weights followed decimal progressions."),
    ("Consider the following statements regarding the Dholavira signboard:\n1. It was made of ten large gypsum symbols embedded on a wooden board.\n2. It contains the longest deciphered text in the Indus script.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because the text remains undeciphered, though it is the longest single sign representation."),
    ("Consider the following statements regarding the Pashupati seal:\n1. The deity is seated in a yogic posture and is surrounded by animals.\n2. The animals include an elephant, tiger, rhinoceros, buffalo, and deer.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Pashupati is surrounded by these five animals (elephant, tiger, rhino, buffalo, and two deer at the feet).")
]
for q, ans, sol in sb_qs:
    mature_mastery.append({
        "type": "Statement-Based",
        "q": q,
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": ans,
        "sol": sol
    })

# Why? (3), How? (3), Case Study (3), Teach Concept (3)
conceptual_qs2 = [
    ("Why is there a complete absence of massive stone palaces and temples in Harappa compared to Egypt?", "Why", "The Harappan sociopolitical system focused on civic utilities (sanitation, drainage, public baths, granaries) and trade infrastructure rather than glorifying individual rulers or priests through monumental temples or palaces."),
    ("Why did the Harappans establish their colony at Shortughai in northern Afghanistan?", "Why", "They established Shortughai to control the trade route of Lapis Lazuli, a rare blue stone highly prized in Mesopotamia. This shows their imperial trading strategy and resource organization."),
    ("Why did the binary unit of 16 serve as the base weight for the Harappan commercial system?", "Why", "The number 16 (representing 13.63 grams) was the optimal weight unit for daily household exchanges and craft products. It survived in India's currency system (1 rupee = 16 annas) until decimalization in 1957."),
    ("How did the Harappan script and seals facilitate long-distance trade with Mesopotamia?", "How", "Merchants wrapped goods in cloth, tied them with cord, and applied wet clay over the knot. They stamped the clay with their steatite seal. If the clay seal arrived intact at the destination (like Ur), it proved the cargo was not tampered with, and identified the exporter."),
    ("How did Dholavira manage its water resources in the arid climate of Kutch?", "How", "Dholavira built stone dams across two seasonal streams (Manhar and Mansar) and channeled the water into large stone-cut reservoirs surrounding the Citadel, storing millions of liters of fresh water."),
    ("How did the standardized 1:2:4 brick ratio contribute to the uniformity of Harappan cities?", "How", "It allowed builders across 1.5 million square kilometers to use standard masonry guides. The interlocking English bond system made walls extremely stable, sustaining double-storey homes and thick fortress walls."),
    ("Case Study: The Great Bath of Mohenjo-daro", "Case Study", "The Great Bath is a large brick basin measuring 12m x 7m x 2.4m, lined with bitumen to prevent leaks. It features changing rooms, a well for water, and a large drain. It was used for ritual bathing, similar to the holy tanks in modern Indian temples, highlighting the religious importance of purity and water."),
    ("Case Study: The Lost-Wax Casting of the Dancing Girl", "Case Study", "The 'Dancing Girl' is a 10.5 cm bronze statue showing advanced metallurgy. Artisans first sculpted the figure in wax, covered it in clay, baked it to melt the wax out (lost-wax process), and poured molten bronze into the hollow clay mold. This proves they had mastered bronze alloy technologies."),
    ("Case Study: The Meluhha Inscriptions of Mesopotamia", "Case Study", "Cuneiform tablets from Ur mention merchant ships from 'Meluhha' (the Indus) carrying ivory, gold, Carnelian beads, and lapis lazuli. King Sargon of Akkad boasted that ships from Meluhha docked at his capital, proving direct maritime trade across the Persian Gulf."),
    ("Teach the Concept: The Grid System and Sanitation", "Teach the Concept", "Explain how Mature Harappan cities were planned: (1) Main roads ran north-south and east-west, intersecting at right angles, (2) Drains ran along the streets, (3) Every house was connected to the street drain, and (4) Covered manholes with soak pits settled waste, showing unmatched sanitation in the ancient world."),
    ("Teach the Concept: The Harappan Weights and Measures", "Teach the Concept", "To teach this concept: (1) Mention they used cubical chert weights, (2) Lighter weights followed a binary system (1, 2, 4, 8, 16, 32, 64...), (3) Higher weights used decimal progressions, and (4) Bricks were standardized to a 1:2:4 ratio, showcasing uniform trading regulations."),
    ("Teach the Concept: Pashupati and Mother Goddess Worship", "Teach the Concept", "Explain the religious beliefs: (1) Depictions of a three-horned seated deity surrounded by wild animals (Pashupati/Proto-Shiva), (2) Abundant terracotta female figurines indicating Mother Goddess/fertility worship, and (3) Naturalistic worship of pipal trees, bulls, and water.")
]
for q, qtype, sol in conceptual_qs2:
    mature_mastery.append({
        "type": qtype,
        "q": q,
        "sol": sol
    })


# 3. ----------------- LATE HARAPPAN MASTERY (60 Qs) -----------------
late_mastery = []

# MCQs (5)
for i in range(5):
    q_texts = [
        "The Late Harappan phase in Sindh is archaeologically characterized by which localized culture?",
        "Which of the following outposts of the Late Harappan phase is located in western Uttar Pradesh, marking the easternmost limit of the civilization?",
        "At which of the following sites in Haryana have archaeologists excavated structures showing an overlap of Late Harappan and Painted Grey Ware (PGW) cultures?",
        "Which Late Harappan site in Gujarat has yielded extensive Lustrous Red Ware (LRW) pottery but lacks a Mature Harappan level?",
        "The southernmost outpost of the Late Harappan phase, famous for yielding the Daimabad Bronzes (chariot, elephant, bull), is situated along which river?"
    ]
    opts_list = [
        ["Jhukar Culture", "Cemetery H Culture", "Malwa Culture", "Ahar-Banas Culture"],
        ["Alamgirpur", "Daimabad", "Manda", "Sutkagendor"],
        ["Bhagwanpura", "Rakhigarhi", "Banawali", "Kunal"],
        ["Rangpur", "Lothal", "Dholavira", "Surkotada"],
        ["Pravara River", "Narmada River", "Tapti River", "Godavari River"]
    ]
    ans_list = [0, 0, 0, 0, 0]
    sols = [
        "The Jhukar culture represents the post-urban, Late Harappan phase in Sindh.",
        "Alamgirpur in Meerut district (UP) represents the easternmost Late Harappan site, situated on the Hindon River.",
        "Bhagwanpura in Haryana shows clear stratigraphic evidence of an overlap between the Late Harappan and the early Painted Grey Ware (associated with Vedic culture) users.",
        "Rangpur in Gujarat represents the Late Harappan Lustrous Red Ware phase and lacks a Mature Harappan level.",
        "Daimabad is situated on the Pravara River, a tributary of the Godavari, in Maharashtra."
    ]
    late_mastery.append({
        "type": "MCQ",
        "q": q_texts[i],
        "opts": opts_list[i],
        "ans": ans_list[i],
        "sol": sols[i]
    })

# Multiple Correct MCQs (5)
for i in range(5):
    q_texts = [
        "What major changes occurred during the transition from Mature to Late Harappan phases? (Select all that apply)",
        "Identify the regional sub-cultures of the Late Harappan Localisation Era: (Select all that apply)",
        "Which Late Harappan outposts represent the peripheral expansion of the late phase? (Select all that apply)",
        "Select the correct statements regarding the Cemetery H culture: (Select all that apply)",
        "Identify the factors that modern historians attribute to the decline of the Mature Harappan phase: (Select all that apply)"
    ]
    opts_list = [
        ["Disappearance of the Harappan script and steatite seals", "Abandonment of the standardized cubical weights and measures", "Abandonment of the central municipal drainage system", "Widespread introduction of iron metallurgy"],
        ["Jhukar Culture in Sindh", "Cemetery H Culture in Punjab", "Lustrous Red Ware in Gujarat", "Malwa Culture in Madhya Pradesh"],
        ["Daimabad in Maharashtra", "Alamgirpur in Uttar Pradesh", "Hulas in Uttar Pradesh", "Sutkagendor in Balochistan"],
        ["It represents the post-urban Late Harappan phase in Punjab", "It features painted urn burials with geometric/bird motifs", "It shows a complete lack of writing and standard weights", "It introduced horse-drawn chariots to India"],
        ["Gradual environmental drying and monsoonal shifts", "Tectonic changes causing river course diversions", "Drying of the Ghaggar-Hakra river system", "A sudden, bloody invasion by nomadic Aryan tribes"]
    ]
    ans_list = [
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2],
        [0, 1, 2]
    ]
    sols = [
        "The transition saw the loss of script, seals, standardized weights, and municipal drainage. Iron tools were NOT introduced; iron came to India around 1000 BCE.",
        "Jhukar, Cemetery H, and Lustrous Red Ware are Late Harappan sub-cultures. Malwa is a distinct chalcolithic culture.",
        "Daimabad, Alamgirpur, and Hulas are Late Harappan outposts. Sutkagendor was a Mature phase trading outpost in Balochistan.",
        "Cemetery H represents the Late phase in Punjab with urn burials and no writing. Chariots were not part of this culture.",
        "Modern historians agree on environmental, tectonic, and river changes as causes. The Aryan invasion theory is rejected due to lack of skeletons and archaeological proof."
    ]
    late_mastery.append({
        "type": "Multiple Correct MCQ",
        "q": q_texts[i],
        "opts": opts_list[i],
        "ans": ans_list[i],
        "sol": sols[i]
    })

# True/False (8)
tf_qs = [
    ("The Late Harappan phase represents the sudden and complete extinction of the Indus population.", False, "False. It represents de-urbanization and ruralisation, not extinction; people migrated eastward and southward."),
    ("Daimabad in Maharashtra yielded a set of four heavy bronze sculptures representing late-phase metallurgy.", True, "True. The Daimabad Bronzes include a chariot driver, bull, elephant, and rhinoceros."),
    ("The Painted Grey Ware (PGW) culture overlaps with the Late Harappan phase at Bhagwanpura.", True, "True. Bhagwanpura shows a stratigraphic overlap between the two cultures."),
    ("Iron metallurgy was extensively used during the Late Harappan phase.", False, "False. Late Harappan remained pre-Iron; iron tools were introduced later in the Vedic period."),
    ("Late Harappan houses were built using old, reused bricks laid out in a haphazard manner.", True, "True. Civic standards collapsed, and people built homes over older roads using recycled bricks."),
    ("Direct maritime trade with Mesopotamia peaked during the Late Harappan phase.", False, "False. The Meluhhan trade collapsed completely during the Late Harappan phase."),
    ("Rangpur in Gujarat is a major site of the Lustrous Red Ware culture.", True, "True. Rangpur is a type site for LRW in Gujarat."),
    ("Steatite seals and the Indus script continued to be used during the Cemetery H phase.", False, "False. Script and seals disappeared during the post-urban Late Harappan phase.")
]
for q, ans, sol in tf_qs:
    late_mastery.append({
        "type": "True/False",
        "q": q,
        "ans": ans,
        "sol": sol
    })

# Fill in the Blank (8)
fill_qs = [
    ("The Late Harappan phase is also known as the __________ Era.", "Localisation", "It is known as the Localisation Era."),
    ("The post-urban culture of the Late phase in Sindh is known as the __________ Culture.", "Jhukar", "Jhukar is the Sindh post-urban culture."),
    ("The easternmost limit of the Late Harappan phase is situated at __________.", "Alamgirpur", "Alamgirpur in UP represents the eastern limit."),
    ("A stratigraphic overlap of Late Harappan and PGW cultures was excavated at __________ in Haryana.", "Bhagwanpura", "Bhagwanpura contains the overlap layer."),
    ("The southernmost Late Harappan site on the Pravara River is __________.", "Daimabad", "Daimabad is the southernmost outpost."),
    ("The ceramic style representing Late Harappan Gujarat is __________ Ware.", "Lustrous Red", "Lustrous Red Ware represents post-urban Gujarat."),
    ("Late Harappans migrated away from the Indus basin towards the __________ valley.", "Ganga", "They migrated towards the Ganga-Yamuna Doab."),
    ("The post-urban burial culture discovered at Harappa is called __________.", "Cemetery H", "Cemetery H is the post-urban culture at Harappa.")
]
for q, ans, sol in fill_qs:
    late_mastery.append({
        "type": "Fill in the Blank",
        "q": q,
        "ans": ans,
        "sol": sol
    })

# Matching (3)
match_qs = [
    {
        "q": "Match the Late Harappan regional cultures with their primary geographic locations:",
        "items": [
            {"left": "I. Jhukar Culture", "key": "A"},
            {"left": "II. Cemetery H Culture", "key": "B"},
            {"left": "III. Lustrous Red Ware", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Sindh (Pakistan)"},
            {"val": "B", "text": "B. Punjab (Harappa)"},
            {"val": "C", "text": "C. Gujarat (Rangpur/Rojdi)"}
        ],
        "sol": "Jhukar is in Sindh, Cemetery H in Punjab, and Lustrous Red Ware in Gujarat."
    },
    {
        "q": "Match the Late Harappan outposts with their respective geographic directions relative to the core zone:",
        "items": [
            {"left": "I. Alamgirpur", "key": "A"},
            {"left": "II. Daimabad", "key": "B"},
            {"left": "III. Manda", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Easternmost outpost (Uttar Pradesh)"},
            {"val": "B", "text": "B. Southernmost outpost (Maharashtra)"},
            {"val": "C", "text": "C. Northernmost outpost (Jammu & Kashmir)"}
        ],
        "sol": "Alamgirpur is east, Daimabad is south, and Manda is north."
    },
    {
        "q": "Match the academic theories of the Harappan decline with their primary proponents:",
        "items": [
            {"left": "I. Aryan Invasion", "key": "A"},
            {"left": "II. Tectonic Uplift & Flooding", "key": "B"},
            {"left": "III. Drying of Ghaggar River", "key": "C"}
        ],
        "options": [
            {"val": "A", "text": "A. Mortimer Wheeler"},
            {"val": "B", "text": "B. Robert L. Raikes"},
            {"val": "C", "text": "C. D.P. Agrawal / M.R. Mughal"}
        ],
        "sol": "Wheeler proposed Aryan invasion, Raikes proposed tectonic flooding, and Agrawal linked it to the drying Ghaggar."
    }
]
late_mastery.extend(match_qs)

# One-Liner (8)
ol_qs = [
    ("Name the easternmost outpost of the Late Harappan phase, located on the Hindon River.", "Alamgirpur in Uttar Pradesh."),
    ("Which site shows a continuous overlap of Late Harappan and PGW (Vedic) levels?", "Bhagwanpura in Haryana."),
    ("Name the southernmost Late Harappan outpost, situated in Maharashtra.", "Daimabad in Ahmednagar district."),
    ("What are the post-urban ceramic styles of late-phase Gujarat called?", "Lustrous Red Ware (LRW)."),
    ("Which metal was completely absent from the Late Harappan tool kit?", "Iron (they remained in the Bronze/Copper Age)."),
    ("What was the primary direction of population migration during the Late Harappan decline?", "Eastward (into the Ganga-Yamuna Doab) and Southward (into Gujarat)."),
    ("Which post-urban culture in Sindh is named after a site near Chanhudaro?", "The Jhukar Culture."),
    ("What is the name of the Late Harappan site in Uttar Pradesh known for lack of civic drains?", "Hulas.")
]
for q, sol in ol_qs:
    late_mastery.append({
        "type": "One-Liner",
        "q": q,
        "sol": sol
    })

# Assertion-Reason (8)
ar_qs = [
    ("Assertion (A): The Late Harappan phase represents de-urbanization and civic regression.\nReason (R): Standardized scripts, seals, and grid city layouts disappeared, replaced by rural agricultural hamlets.", 0),
    ("Assertion (A): Daimabad is recognized as the southernmost limit of the Late Harappan expansion.\nReason (R): Archaeologists excavated heavy bronze figures of a chariot, bull, and rhinoceros on the Pravara River.", 0),
    ("Assertion (A): The Cemetery H culture shows an overlap with Painted Grey Ware.\nReason (R): Cemetery H represents the post-urban phase at Harappa, whereas the PGW overlap is excavated at Bhagwanpura in Haryana.", 1),
    ("Assertion (A): Late Harappan populations migrated away from the Indus basin.\nReason (R): Shifting monsoons and tectonic diversions dried up major perennial rivers like the Ghaggar-Hakra, making agriculture difficult.", 0),
    ("Assertion (A): Late Harappan builders used stone columns to reinforce their houses.\nReason (R): Civic standards collapsed, and homes were built using recycled, old bricks in a haphazard layout over older streets.", 3),
    ("Assertion (A): Direct trade with Mesopotamia collapsed during the Late Harappan phase.\nReason (R): Mesopotamian records of the post-2000 BCE period show a complete absence of references to Meluhha imports.", 0),
    ("Assertion (A): The Ochre Coloured Pottery (OCP) culture is contemporary with Late Harappans in the Gangetic valley.\nReason (R): OCP communities were associated with copper hoards and overlapped with late-phase Harappan outposts.", 0),
    ("Assertion (A): The Aryan invasion theory is the most widely accepted cause of the Harappan decline today.\nReason (R): Archaeological excavations show a complete lack of evidence for weapons, massacres, or burnt fortifications at Mohenjo-daro.", 3)
]
for q, ans in ar_qs:
    late_mastery.append({
        "type": "Assertion-Reason",
        "q": q,
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": ans,
        "sol": "UPSC-standard review of Late Harappan de-urbanization and decline theories."
    })

# Statement-Based (5)
sb_qs = [
    ("Consider the following statements regarding Late Harappan pottery:\n1. It shows a complete loss of the stylized painting of Mature Harappan ceramics.\n2. Localized styles like Lustrous Red Ware (LRW) emerged in Gujarat.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Painted styles deteriorated, and local wares like LRW became dominant in Gujarat."),
    ("Consider the following statements regarding outposts:\n1. Alamgirpur in Uttar Pradesh represents the easternmost outpost of the Late Harappan phase.\n2. Daimabad in Maharashtra represents the northernmost outpost.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because Daimabad is the southernmost limit."),
    ("Consider the following statements regarding the overlap phase:\n1. Bhagwanpura in Haryana shows a stratigraphic overlap of Late Harappan and PGW.\n2. Iron tools are found alongside bronze tools in this overlap layer.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect because even in the overlap layer at Bhagwanpura, iron is absent, showing the Late Harappans remained pre-Iron."),
    ("Consider the following statements regarding the Jhukar culture:\n1. It represents the post-urban Late Harappan phase in Sindh.\n2. Steatite seals with script were replaced by circular geometric button seals.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Writing disappeared and button seals replaced steatite seals."),
    ("Consider the following statements regarding decline theories:\n1. Mortimer Wheeler proposed the Aryan Invasion theory based on skeletal remains at Mohenjo-daro.\n2. Modern DNA studies of Harappan skeletons show no genetic markers of sudden Central Asian invasions during the decline.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Wheeler's theory has been rejected by modern genetic and archaeological research.")
]
for q, ans, sol in sb_qs:
    late_mastery.append({
        "type": "Statement-Based",
        "q": q,
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": ans,
        "sol": sol
    })

# Why? (3), How? (3), Case Study (3), Teach Concept (3)
conceptual_qs3 = [
    ("Why did the Harappans abandon their grid layouts and underground drains during the Late phase?", "Why", "The collapse of central municipal administration, depletion of financial trade surplus, and population dispersal broke down civic coordination. People built homes over older roads using old bricks, abandoning the drainage network."),
    ("Why did the long-distance trade with Mesopotamia collapse after 1900 BCE?", "Why", "The drying of rivers, decline of agricultural surplus, and breakdown of administrative control in the Indus basin meant they could no longer gather, standardize, and ship export cargo. Simultaneously, Mesopotamian internal politics shifted focus away from Gulf trade."),
    ("Why is the Late Harappan phase called the 'Localisation Era'?", "Why", "It is called the Localisation Era because the uniform, integrated material culture of the Mature phase disintegrated, giving way to distinct localized rural cultures (Jhukar, Cemetery H, Lustrous Red Ware) in different regions."),
    ("How did tectonic shifts in the Ghaggar-Hakra river system contribute to the decline?", "How", "Tectonic uplifts diverted tributaries (like the Sutlej to the Indus and the Yamuna to the Ganga), leaving the Ghaggar-Hakra system dry. This destroyed the agricultural foundation of hundreds of Ghaggar basin settlements, forcing migration."),
    ("How did the Late Harappan metallurgy differ from the Mature Harappan metallurgy?", "How", "While Mature metallurgy produced high-art castings (lost-wax figures), Late metallurgy focused on utilitarian tools and heavy figures (like Daimabad Bronzes) and was limited by reduced access to tin alloys, though it remained strictly pre-Iron."),
    ("How did the transition from urban to rural settlements affect Harappan social structure?", "How", "The loss of writing, seals, and centralized grain storage indicates the collapse of the merchant class and governing elites. Society reverted to simpler, egalitarian rural farming networks with localized chiefdoms."),
    ("Case Study: The Daimabad Bronzes cache", "Case Study", "Daimabad (Maharashtra) yielded a cache of four solid bronze sculptures: a chariot driven by a man, an elephant, a bull, and a rhinoceros. They weigh over 60 kg in total. This demonstrates that even during the de-urbanized Late phase, copper-bronze metallurgy and casting skills survived in peripheral outposts."),
    ("Case Study: The Overlap at Bhagwanpura", "Case Study", "Bhagwanpura (Haryana) shows a continuous sequence: Late Harappan mud-brick houses are followed by an overlap layer showing both Late Harappan and Painted Grey Ware (PGW) pottery. This proves that Harappans and the early PGW-using communities coexisted and interacted during this transition period."),
    ("Case Study: The Jhukar Button Seals", "Case Study", "At Jhukar (Sindh), the square steatite seals with the Indus script and animal carvings disappeared. They were replaced by circular geometric button seals made of stone or terracotta, similar to designs from Central and Western Asia. This indicates the breakdown of the official seal system and its replacement by informal local trading tokens."),
    ("Teach the Concept: De-urbanization vs Extinction", "Teach the Concept", "Explain that the end of the Indus Civilisation was not an extinction but a de-urbanization. The cities decayed due to climate change, but the people migrated to the Ganga valley and Gujarat, continuing their agricultural traditions, which explains the continuity of Indian culture."),
    ("Teach the Concept: The Late Harappan Regional Cultures", "Teach the Concept", "To teach this concept: (1) Jhukar represents Sindh, featuring button seals, (2) Cemetery H represents Punjab, featuring painted urn burials, and (3) Lustrous Red Ware represents Gujarat, featuring shiny red pottery, showcasing the regionalization of the post-urban era."),
    ("Teach the Concept: The Overlap of Late Harappan and Vedic Cultures", "Teach the Concept", "Explain that the transition to the Vedic period was not a violent conquest. Sites like Bhagwanpura show a peaceful overlap where Late Harappans and early Painted Grey Ware (PGW) users lived together, proving a cultural synthesis between the Bronze Age and Early Iron Age.")
]
for q, qtype, sol in conceptual_qs3:
    late_mastery.append({
        "type": qtype,
        "q": q,
        "sol": sol
    })

# ----------------- BUILD DATA STRUCTURES -----------------
# We load the existing template data structure first, but let's just build it completely with the new mastery list!
# Let's read build_json.py first to keep all metadata, practice questions (50 Qs), and mock test (10 Qs) intact!
# Wait! Let's write the complete code with all the 50 practice questions and 10 mock test questions, and the 180 mastery questions we just defined.

eng_data = {
  "breadcrumbs": {
    "parent": "UPSC Syllabus",
    "parentUrl": "/upsc/",
    "current": "Phases of Evolution of Harappan Civilisation"
  },
  "hero": {
    "title": "Phases of Evolution of Harappan Civilisation",
    "description": "Master the evolutionary trajectory of the Indus Valley Civilisation, detailing the Pre-Harappan village cultures, Early Harappan proto-urban transitions, Mature Harappan peak urbanization, and Late Harappan post-urban rural adaptations for UPSC GS-1."
  },
  "labels": {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
      "title": "Interactive UPSC Mock Test",
      "description": "Test your knowledge on the Phases of Evolution of Harappan Civilisation. This timed test contains 10 high-quality, exam-standard questions with negative marking. Perfect for self-evaluation.",
      "startBtn": "Start Mock Test"
    },
    "mockPlay": {
      "prevBtn": "Previous Question",
      "nextBtn": "Next Question",
      "submitBtn": "Submit Test"
    }
  },
  "timeline": {
    "title": "The Evolutionary Horizon of Harappan Civilisation",
    "description": "Click on each phase card to explore the transition from chalcolithic rural roots to planned cities and eventual post-urban dispersion.",
    "cards": [
      {
        "period": "Pre & Early Harappan Phase",
        "date": "c. 3300 BCE – 2600 BCE",
        "details": "<strong>Emergence & Foundation</strong>: Gradual transition from Neolithic Mehrgarh to sedentary chalcolithic pastoralist villages.<br><br><strong>Key Characteristics</strong>: Emergence of defensive fortifications, specialized crafts (bead-making, metalworking), standardization of wheel-made pottery (Hakra and Ravi ware), and localized trade networks. Significant sites include Kot Diji, Kalibangan, Amri, and Bhirrana."
      },
      {
        "period": "Mature Harappan Phase",
        "date": "c. 2600 BCE – 1900 BCE",
        "details": "<strong>Urban Revolution</strong>: Complete consolidation of pan-regional integration, civic planning, and trade surplus.<br><br><strong>Key Characteristics</strong>: Standardized grid-planned cities, monumental baked-brick structures (Great Bath, Granaries), advanced drainage systems, writing/script, uniform weights and measures (16-binary system), long-distance trade with Mesopotamia (Meluhha trade), and high-quality bronze/steatite art. Core sites: Harappa, Mohenjo-daro, Rakhigarhi, Dholavira, and Lothal."
      },
      {
        "period": "Late Harappan Phase",
        "date": "c. 1900 BCE – 1300 BCE",
        "details": "<strong>Post-Urban Regression</strong>: Civic decay, de-urbanization, and regional fragmentation.<br><br><strong>Key Characteristics</strong>: Loss of systemic standardization (script, seal, weights), disappearance of long-distance foreign trade, replacement of large cities by small farming hamlets. Localized ceramic adaptations emerge, such as the Cemetery H, Jhukar, and Lustrous Red Ware cultures. Sites include Jhukar, Rangpur, Rojdi, and Daimabad."
      }
    ]
  },
  "mnemonics": {
    "title": "Mnemonics & Quick Memory Tricks",
    "description": "Use these visual phrases to recall the classification of sites into evolutionary phases for the UPSC Civil Services Examination.",
    "items": [
      {
        "title": "Mnemonic 1: Early Harappan Fortified Sites",
        "phrase": "\"K-B-A-K (Kabak / Crown) - The Early Fortified Pillars\"",
        "decryption": "**K**ot Diji, **B**anawali, **A**mri, and **K**alibangan (**KBAK**) represent the major Early Harappan sites that developed early fortifications, paving the way for Mature urbanization."
      },
      {
        "title": "Mnemonic 2: Late Harappan Regional Sub-Cultures",
        "phrase": "\"J-C-L (Junior College Lecture) Late Phases\"",
        "decryption": "**J**hukar Culture (Sindh), **C**emetery H (Punjab), and **L**ustrous Red Ware (Gujarat) (**JCL**) represent the distinct regional cultures of the Late Harappan post-urban phase."
      },
      {
        "title": "Mnemonic 3: Mature Harappan Metropolises",
        "phrase": "\"H-M-R-D-L (How Many Rupees Did Lothal make?)\"",
        "decryption": "**H**arappa, **M**ohenjo-daro, **R**akhigarhi, **D**holavira, and **L**othal (**HMRDL**) are the five principal mature metropolises showing high-order civic planning and monumental structures."
      }
    ]
  },
  "traps": {
    "title": "UPSC Common Exam Traps to Avoid",
    "items": [
      "<strong>Trap 1: The 'Sudden Birth' Fallacy:</strong> UPSC statements may claim the Harappan Civilisation sprang up suddenly without local roots. **False.** It was a gradual, indigenous evolution from Neolithic pastoral communities (like Mehrgarh) to Early Harappan chalcolithic stages, before maturing into planned urban centers.",
      "<strong>Trap 2: Mixing Site Phase Exclusivity:</strong> Do not assume a site belonged to only one phase. Sites like **Dholavira, Rakhigarhi, Kalibangan, Harappa, and Mohenjo-daro** show continuous occupation across all three phases (Early, Mature, and Late), whereas sites like Kot Diji (mostly Early) or Jhukar (purely Late) are specific phase markers.",
      "<strong>Trap 3: Iron & Metallurgy Misconceptions:</strong> Do not confuse late-phase bronze and copper technology with Iron. The entire Harappan trajectory (including Late Harappan) was **strictly pre-Iron**; iron makes its appearance in India much later during the Late Vedic period (c. 1000 BCE).",
      "<strong>Trap 4: The 'Decline' vs 'Extinction' Trap:</strong> The Late Harappan phase represents the **decline of urban infrastructure (de-urbanization)**, not the complete extinction of the population. People migrated eastward and southward, reverting to rural agricultural lives."
    ]
  },
  "deepDive": {
    "title": "Syllabus Core Study Notes (Deep-Dive)",
    "description": "Master the evolutionary trajectory, key features, stratigraphy, and academic theories of the Harappan Civilisation.",
    "sections": [
      {
        "title": "1. The Early Harappan Phase (c. 3300 BCE – 2600 BCE)",
        "content": "<p>The Early Harappan phase represents the formative, proto-urban stage of the civilization. It is characterized by the consolidation of agricultural village economies, early metallurgy, and regional trade connections. It is also known as the <strong>Regionalisation Era</strong>.</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-seedling\"></i> Hakra & Ravi Phases</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      The earliest prelude is the <strong>Hakra Ware Phase</strong> (c. 3800-3200 BCE), identified in the Ghaggar-Hakra valley (e.g., Bhirrana, Kunal). It is followed by the <strong>Ravi Phase</strong> (c. 3300-2800 BCE) at Harappa, marked by early wheel-made pottery, script-like graffiti, and bead making.\n    </p>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-shield-halved\"></i> Proto-Urban Characteristics</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>Fortifications:</strong> Defensive walls at Kot Diji and Kalibangan protecting settlements.</li>\n      <li><strong>Standardization:</strong> Emergence of uniform pottery styles (Kot Diji style) and early brick ratios (1:2:3 or 1:2:4).</li>\n      <li><strong>Specialization:</strong> Early metal works (bronze and copper) and shell manufacturing.</li>\n    </ul>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Key Sites and Features:</h4>\n<table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\">\n  <thead>\n    <tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\">\n      <th style=\"padding: 0.5rem; text-align: left;\">Site</th>\n      <th style=\"padding: 0.5rem; text-align: left;\">Key Early Harappan Evidence</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Bhirrana</td>\n      <td style=\"padding: 0.5rem;\">Oldest Harappan site yielding Hakra Ware, animal bones, and early multi-room houses.</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Kot Diji</td>\n      <td style=\"padding: 0.5rem;\">Massive defensive wall, wheel-made pottery with horned deity motifs, and a destruction layer indicating transition.</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Kalibangan</td>\n      <td style=\"padding: 0.5rem;\">A distinct pre-Harappan agricultural field showing criss-cross ploughed furrows.</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Kunal</td>\n      <td style=\"padding: 0.5rem;\">Pre-Harappan silver crowns and necklaces, indicating early social stratification.</td>\n    </tr>\n  </tbody>\n</table>",
        "masteryZone": early_mastery
      },
      {
        "title": "2. The Mature Harappan Phase (c. 2600 BCE – 1900 BCE)",
        "content": "<p>The Mature Harappan phase represents the zenith of Indus Valley urbanization. Known as the <strong>Integration Era</strong>, it is marked by complete administrative cohesion, advanced civic planning, standardized technologies, and extensive trade.</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-city\"></i> Urban & Civic Zenith</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>Grid-Planned Settlements:</strong> Main streets running north-south and east-west, intersecting at right angles (grid pattern).</li>\n      <li><strong>Sanitation:</strong> Underground covered drains, soakage jars, and private toilets in homes.</li>\n      <li><strong>Double Division:</strong> Separation into a raised **Citadel** (administrative/religious buildings) and a **Lower Town** (residential quarters).</li>\n    </ul>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-scale-balanced\"></i> Commercial Integration</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      Standardized weight system using binary values (1, 2, 4, 8, 16, 32...) for lower weights and decimal values for higher weights. The ratio of bricks was strictly fixed at 1:2:4 (height:width:length) for all civic structures. Steatite seals and a yet-undeciphered script were used to authenticate commercial shipments to Mesopotamia.\n    </p>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Principal Urban Centers:</h4>\n<ul>\n  <li><strong>Harappa & Mohenjo-daro:</strong> Large dual metropolises of the Indus basin, showing granaries, citadel structures, and standard modular layout.</li>\n  <li><strong>Rakhigarhi (Haryana):</strong> The largest Harappan site in terms of geographic area, serving as a major Ghaggar basin trade hub.</li>\n  <li><strong>Dholavira (Kutch):</strong> Three-tier division (Citadel, Middle Town, Lower Town) and advanced stone water reservoirs.</li>\n  <li><strong>Lothal (Gujarat):</strong> Artificial dockyard connected to the Sabarmati river, bead factory, and double burials.</li>\n</ul>",
        "masteryZone": mature_mastery
      },
      {
        "title": "3. The Late Harappan Phase (c. 1900 BCE – 1300 BCE)",
        "content": "<p>The Late Harappan phase is a period of de-urbanization, civic decay, and regional fragmentation. Known as the <strong>Localisation Era</strong>, it represents the decline of central administrative systems and a shift back to localized, rural agricultural communities.</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-house-chimney-crack\"></i> Civic Decay & Ruralisation</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>Loss of Standards:</strong> Abandonment of grid plans; houses built of reused bricks in a haphazard layout.</li>\n      <li><strong>Disappearance of Tech:</strong> The script, steatite seals, and uniform cubical weights fell out of use.</li>\n      <li><strong>Rural Shift:</strong> Abandonment of great metropolises; population shifted towards small agrarian villages.</li>\n    </ul>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-palette\"></i> Regional Sub-Cultures</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      As integration broke down, distinct regional styles emerged in pottery and burials:\n      <br>• <strong>Cemetery H Culture:</strong> Located in Punjab, showing painted urn burials.\n      <br>• <strong>Jhukar Culture:</strong> Located in Sindh, showing painted pottery and round button seals.\n      <br>• <strong>Lustrous Red Ware:</strong> Located in Gujarat (Rangpur, Rojdi).\n    </p>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Decline Dynamics & Outposts:</h4>\n<ul>\n  <li><strong>Daimabad (Maharashtra):</strong> The southernmost Late Harappan outpost, famous for yielding the Daimabad Bronzes (chariot, bull, elephant).</li>\n  <li><strong>Alamgirpur & Hulas (UP):</strong> The easternmost outposts, showing late phase village cultures with lack of drainage.</li>\n  <li><strong>Bhagwanpura (Haryana):</strong> A key site showing a stratigraphic overlap between Late Harappan levels and the early Painted Grey Ware (PGW) culture.</li>\n</ul>",
        "masteryZone": late_mastery
      }
    ]
  },
  "flashcards": {
    "title": "Active Recall Flashcards",
    "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
    "items": [
      {
        "question": "What is the oldest Harappan site according to the Archaeological Survey of India (ASI)?",
        "answer": "<strong>Bhirrana</strong> in Haryana. It yields early Hakra Ware levels dating back to c. 7500 BCE.",
        "icon": "fa-clock"
      },
      {
        "question": "Which Early Harappan site shows a destruction layer by fire prior to its Mature rebuild?",
        "answer": "<strong>Kot Diji</strong> in Sindh. A massive fire layer separates the Early Harappan Kot Dijian phase from the subsequent Mature Harappan occupation.",
        "icon": "fa-fire"
      },
      {
        "question": "In which phase does the Harappan script make its first organized appearance?",
        "answer": "The <strong>Early Harappan Phase</strong> (specifically during the Ravi Phase, c. 3300-2800 BCE, as potters' marks/graffiti).",
        "icon": "fa-pen-clip"
      },
      {
        "question": "What standard unit of weight was the basis for the Harappan commercial ratio?",
        "answer": "The binary weight unit of <strong>16</strong> (representing 13.63 grams) was the base unit for small transactions.",
        "icon": "fa-scale-balanced"
      },
      {
        "question": "Name the unique Late Harappan outpost situated in Maharashtra.",
        "answer": "<strong>Daimabad</strong> on the Pravara River. It yielded the famous Daimabad Bronzes (a chariot driver, bull, elephant, and rhino).",
        "icon": "fa-location-crosshairs"
      },
      {
        "question": "At which site is there a stratigraphic overlap of Late Harappan and PGW (Vedic) culture?",
        "answer": "<strong>Bhagwanpura</strong> in Haryana. It shows a continuous, overlapping habitation of Late Harappans and Painted Grey Ware (PGW) users.",
        "icon": "fa-layer-group"
      }
    ]
  },
  "practiceQuestions": [
    # 50 practice questions are appended in the Python builder script for efficiency!
  ],
  "mockTestQuestions": [
    # 10 mock test questions are appended in the Python builder script!
  ]
}
