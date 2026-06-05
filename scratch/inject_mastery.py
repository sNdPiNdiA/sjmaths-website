import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Phases-of-Evolution-of-Harappan-Civilisation\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Phases-of-Evolution-of-Harappan-Civilisation\hi\content.json"

mcq_opts = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
ar_opts = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]

hin_mcq_opts = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
hin_ar_opts = [
    "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
    "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
    "A सत्य है लेकिन R असत्य है",
    "A असत्य है लेकिन R सत्य है"
]

# ----------------- SECTION 1: EARLY HARAPPAN (ENGLISH) -----------------
early_mastery_eng = []

# MCQs (5)
for q, opts, ans, sol in [
    ("Which of the following sites represents the earliest Hakra Ware phase of the Harappan evolution?", ["Bhirrana", "Mohenjo-daro", "Lothal", "Chanhudaro"], 0, "Bhirrana represents the oldest Hakra Ware phase (dating back to the 4th millennium BCE)."),
    ("The famous pre-mature agricultural ploughed field showing criss-cross furrows was discovered at:", ["Kalibangan", "Banawali", "Harappa", "Kot Diji"], 0, "Kalibangan yielded a unique pre-mature (Early Harappan) ploughed agricultural field."),
    ("The pre-Harappan settlement of Amri in Sindh is famous for yielding which of the following specific findings?", ["Pottery painted with gazelle/antelope motifs", "A large stone dockyard", "Terracotta horse figurines", "Lapis Lazuli seals"], 0, "Amri is famous for its pre-Harappan levels showing a distinct pottery style painted with gazelles."),
    ("Two silver crowns and precious ornaments representing early social stratification were excavated at:", ["Kunal", "Bhirrana", "Amri", "Banawali"], 0, "Kunal yielded two silver crowns and gold ornaments, representing early social stratification."),
    ("The Ravi Phase (c. 3300-2800 BCE) represents the earliest occupation level at which major site?", ["Harappa", "Mohenjo-daro", "Kalibangan", "Dholavira"], 0, "The Ravi Phase represents the earliest occupation level at Harappa, showing the first graffiti marks.")
]:
    early_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("Which of the following elements characterize the Early Harappan phase? (Select all that apply)", ["Emergence of defensive fortifications", "Standardization of wheel-made pottery", "Early copper and bronze working", "Use of standardized grid-planned city streets"], [0, 1, 2], "Early Harappan is marked by fortifications, wheel-made pottery, and early metallurgy. Grid streets are Mature phase features."),
    ("Identify the sites associated with the Early Harappan phase: (Select all that apply)", ["Bhirrana", "Kot Diji", "Amri", "Surkotada"], [0, 1, 2], "Bhirrana, Kot Diji, and Amri contain Early Harappan phases. Surkotada is Mature/Late."),
    ("Which features are associated with the Ravi Phase of Harappa? (Select all that apply)", ["Potters' marks and early scripts on pottery", "Bead manufacturing", "Use of potter's wheel", "Construction of the Great Bath"], [0, 1, 2], "The Ravi Phase shows potters' marks, bead-making, and wheel-made pottery. The Great Bath is Mature."),
    ("Select the Early Harappan sites that show evidence of early fortifications: (Select all that apply)", ["Kot Diji", "Kalibangan", "Bhirrana", "Lothal"], [0, 1, 2], "Kot Diji, Kalibangan, and Bhirrana show Early Harappan fortifications. Lothal is Mature."),
    ("Identify the characteristics of Hakra Ware: (Select all that apply)", ["Primarily handmade ceramic style", "Thick-walled pottery with chocolate slip", "Found in Cholistan and Haryana region", "Extensive use of iron oxide painting"], [0, 1, 2], "Hakra Ware is handmade, thick-walled with chocolate slips, and found in Cholistan/Haryana. Iron was unknown.")
]:
    early_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Hakra Ware phase represents a transition stage that predates the Ravi phase at Harappa.", True, "True. The Hakra phase (c. 3800-3200 BCE) predates the Ravi phase (c. 3300-2800 BCE)."),
    ("The Kot Diji phase represents the Mature Harappan urban peak.", False, "False. Kot Diji represents the Early Harappan proto-urban stage."),
    ("Prehistoric humans used iron tools during the Early Harappan phase.", False, "False. The entire Harappan trajectory was pre-Iron."),
    ("Kalibangan's ploughed field belongs to the Mature Harappan phase.", False, "False. It belongs to the pre-mature Early Harappan phase."),
    ("M.R. Mughal was the archaeologist who first systematically defined the 'Early Harappan' phase.", True, "True. Rafique Mughal systematically defined this phase based on excavations in Cholistan."),
    ("Early Harappan potters were completely unaware of the potter's wheel.", False, "False. Wheel-made pottery (Ravi and Kot Diji ware) was highly developed."),
    ("Bhirrana in Haryana is recognized as the oldest Harappan site by the ASI.", True, "True. Bhirrana has yielded the oldest Hakra ware levels."),
    ("Social stratification is completely absent in the Early Harappan phase.", False, "False. Discoveries like the silver crowns at Kunal indicate early social hierarchies.")
]:
    early_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The Early Harappan phase is also known as the __________ Era of the Indus Valley Civilisation.", "Regionalisation", "The Early Harappan phase represents the Regionalisation Era."),
    ("The oldest Harappan site according to the ASI is __________.", "Bhirrana", "Bhirrana in Haryana is the oldest site."),
    ("Two silver crowns representing early social stratification were found at __________.", "Kunal", "Kunal yielded the silver crowns."),
    ("Horned deity motifs painted on pottery are characteristic of the __________ phase.", "Kot Diji", "Kot Diji ware is famous for horned deity paintings."),
    ("The Ravi phase was first identified at the site of __________.", "Harappa", "The Ravi phase is the earliest level at Harappa."),
    ("The agricultural field showing criss-cross ploughed furrows is situated at __________.", "Kalibangan", "Kalibangan has the ploughed field."),
    ("The Hakra Ware phase dates back to the __________ millennium BCE.", "fourth", "Hakra Ware dates to c. 3800-3200 BCE (4th millennium BCE)."),
    ("The pre-mature phase of Sindh is typified by the site of __________.", "Amri", "Amri is the type site for pre-mature Sindh levels.")
]:
    early_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
early_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the Early Harappan sites with their respective modern Indian states/provinces:",
        "items": [{"left": "I. Bhirrana", "key": "A"}, {"left": "II. Kalibangan", "key": "B"}, {"left": "III. Kot Diji", "key": "C"}],
        "options": [{"val": "A", "text": "A. Haryana"}, {"val": "B", "text": "B. Rajasthan"}, {"val": "C", "text": "C. Sindh (Pakistan)"}],
        "sol": "Bhirrana is in Haryana, Kalibangan in Rajasthan, and Kot Diji in Sindh."
    },
    {
        "type": "Match the Following",
        "q": "Match the Early Harappan cultural phases with their approximate chronological ranges:",
        "items": [{"left": "I. Hakra Ware Phase", "key": "A"}, {"left": "II. Ravi Phase", "key": "B"}, {"left": "III. Kot Diji Phase", "key": "C"}],
        "options": [{"val": "A", "text": "A. c. 3800 BCE – 3200 BCE"}, {"val": "B", "text": "B. c. 3300 BCE – 2800 BCE"}, {"val": "C", "text": "C. c. 2800 BCE – 2600 BCE"}],
        "sol": "These represent the chronological progression of the Early Harappan period."
    },
    {
        "type": "Match the Following",
        "q": "Match the Early Harappan site with its unique archaeological discovery:",
        "items": [{"left": "I. Kunal", "key": "A"}, {"left": "II. Kalibangan", "key": "B"}, {"left": "III. Amri", "key": "C"}],
        "options": [{"val": "A", "text": "A. Silver crowns and gold ornaments"}, {"val": "B", "text": "B. Criss-cross ploughed agricultural field"}, {"val": "C", "text": "C. Gazelle and geometric painted pottery"}],
        "sol": "Kunal has silver crowns, Kalibangan has ploughed fields, and Amri has gazelle motifs."
    }
])

# One-Liner (8)
for q, sol in [
    ("Name the archaeologist who systematically defined the 'Early Harappan' phase.", "M.R. Mughal systematically mapped and defined this phase based on his surveys in Cholistan."),
    ("Which Early Harappan site in Sindh shows a thick layer of ash indicating destruction by fire before the Mature rebuild?", "Kot Diji shows a distinct fire/destruction layer separating the Early and Mature phases."),
    ("Name the river along which the pre-mature site of Amri is situated.", "The Indus River (on its right bank, opposite Mohenjo-daro)."),
    ("Which site represents the oldest agricultural field in the Indian subcontinent?", "Kalibangan (the Early Harappan phase ploughed field)."),
    ("What are the earliest script-like markings found on Ravi phase pottery called?", "Potters' marks or graffiti marks."),
    ("What metal was primarily used for tools in the Early Harappan phase?", "Copper (and its low-grade alloy bronze)."),
    ("Which region in Pakistan contains the largest density of Hakra and Early Harappan sites?", "The Cholistan Desert region (Ghaggar-Hakra valley)."),
    ("What is the name of the oldest pre-mature phase pottery style found in Haryana?", "Hakra Ware.")
]:
    early_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Lower alluvial Ganga plains were completely devoid of Early Harappan settlements.\nReason (R): Early farmers avoided the Ganga plains due to a complete lack of stone resources needed for tools.", 0, "Both A and R are true and R explains A. Stone tools required outcrops which were absent in the alluvial plain."),
    ("Assertion (A): The transition from Hakra to Ravi phase represents agricultural stabilization.\nReason (R): Wheel-made pottery and script-like potters' marks start appearing during the Ravi phase.", 0, "Ravi phase marks high technological and social organization."),
    ("Assertion (A): Defensive walls were constructed at Kot Diji and Kalibangan during the Early phase.\nReason (R): Early Harappan communities faced threats from local floods and conflicts with neighboring pastoralists.", 0, "Walls served both defensive and flood protection roles."),
    ("Assertion (A): The Early Harappan phase is called the Regionalisation Era.\nReason (R): Localized ceramic fabrics and regional styles dominated before pan-regional integration.", 0, "Regionalisation represents localized growth before Mature Harappan integration."),
    ("Assertion (A): Kunal represents an early stage of social hierarchy.\nReason (R): Archaeologists excavated two silver crowns and massive jewelry hoards from the site.", 0, "Silver crowns are clear indicators of elite ruling structures."),
    ("Assertion (A): The ploughed field at Kalibangan shows advanced agricultural knowledge.\nReason (R): The field exhibits criss-cross furrows, showing that two different crops were grown together.", 0, "Double-cropping layout is visible in the furrow spacing."),
    ("Assertion (A): Early Harappans did not practice long-distance maritime trade with Mesopotamia.\nReason (R): Direct Meluhha trade documents and Harappan seals in Mesopotamia are strictly limited to the Mature Harappan phase.", 0, "Mesopotamian trade consolidated only during mature urbanization."),
    ("Assertion (A): Brick sizes in the Early phase were already standardized to the Mature 1:2:4 ratio.\nReason (R): Early phase brick ratios were often irregular (e.g., 1:2:3) and only consolidated into 1:2:4 during the Mature transition.", 3, "Assertion is false: early brick ratios were mostly 1:2:3. Reason is true.")
]:
    early_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Hakra Ware phase:\n1. It represents the earliest chalcolithic farming communities in the Ghaggar-Hakra basin.\n2. It has been discovered at sites like Bhirrana and Kunal in India.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding early fortifications:\n1. Kot Diji is the only Early Harappan site that shows a defensive fortification wall.\n2. Kalibangan-I (Early phase) also had a fortified wall dividing the settlement.\nWhich of the statements given above is/are correct?", 1, "Kot Diji is not the only fortified site (Kunal, Kalibangan, Bhirrana are also fortified)."),
    ("Consider the following statements regarding the Ravi Phase:\n1. It is the earliest occupation layer excavated at the site of Harappa.\n2. Writing was already fully developed during this phase with long inscriptions.\nWhich of the statements given above is/are correct?", 0, "Only short potter graffiti exist, not fully developed script."),
    ("Consider the following statements regarding agricultural practices:\n1. The ploughed field at Kalibangan belongs to the Early Harappan phase.\n2. Wooden plowshares were used instead of iron plowshares.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Iron was completely unknown."),
    ("Consider the following statements regarding early social hierarchies:\n1. Kunal yielded silver crowns and gold ornaments, indicating early elites.\n2. Early Harappan houses were completely uniform in size with no differences.\nWhich of the statements given above is/are correct?", 0, "Houses had size and room variation, showing social stratification.")
]:
    early_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for qtype, q, sol in [
    ("Why", "Why did defensive fortifications emerge during the Early Harappan phase?", "Fortifications emerged for protection against seasonal floods and cattle raids by nomadic tribes, indicating political coordination."),
    ("Why", "Why is the Early Harappan phase referred to as the 'Regionalisation Era' by modern historians?", "Because material culture was divided into distinct localized styles (Kot Dijian, Sothi-Siswal) rather than a uniform integrated style."),
    ("Why", "Why is the discovery of Hakra Ware at Bhirrana significant for Indus Valley chronology?", "It pushes the roots of Harappan agriculture back into the 5th millennium BCE, confirming gradual indigenous development."),
    ("How", "How did Early Harappan potters' marks evolve into the Mature Harappan script?", "Marks on pottery representing owners or guilds became standardized and sequenced, developing into the logosyllabic script."),
    ("How", "How did agricultural surplus trigger the transition from the Early to Mature Harappan phase?", "Silt deposits and flood irrigation yielded surplus grain, supporting specialized craft guilds, metal industries, and administrators."),
    ("How", "How did Early Harappan construction techniques prepare for Mature Harappan city planning?", "They pioneered brick ratios, early street alignments, and defensive walls, which consolidated into grid-planned urban metropolises."),
    ("Case Study", "Case Study: The Destruction Layer at Kot Diji", "A thick ash layer divides early and mature levels at Kot Diji. This suggests a massive fire, indicating either warfare, conquest, or intentional burning to clear land for a planned Mature city layout."),
    ("Case Study", "Case Study: Kalibangan-I Agricultural Layout", "The pre-mature field shows criss-cross furrows (closer north-south, wider east-west). This design is still used in Rajasthan to grow two crops simultaneously without light competition."),
    ("Case Study", "Case Study: Social Stratification at Kunal", "A jar containing silver crowns and gold ornaments was found under a house floor, indicating an early chiefdom or elite class who controlled luxury metals."),
    ("Teach the Concept", "Teach the Concept: The Ravi Phase of Harappa", "Explain: (1) earliest layer at Harappa (c. 3300-2800 BCE), (2) transition to sedentary brick houses, (3) early wheel-made pottery, (4) early graffiti marks."),
    ("Teach the Concept", "Teach the Concept: Regionalisation Era vs Integration Era", "Explain that the Regionalisation Era represents diverse regional styles (Kot Diji, Amri) whereas the Integration Era represents uniform standard systems (seals, script, grid layouts)."),
    ("Teach the Concept", "Teach the Concept: Hakra Ware and its geographical distribution", "Hakra Ware refers to early Ghaggar-Hakra basin pottery (handmade, mud-applied). It represents the geographical cradle of Harappan culture in Haryana/Punjab/Cholistan.")
]:
    early_mastery_eng.append({"type": qtype, "q": q, "sol": sol})


# ----------------- SECTION 2: MATURE HARAPPAN (ENGLISH) -----------------
mature_mastery_eng = []

# MCQs (5)
for q, opts, ans, sol in [
    ("The Mature Harappan brick dimensions followed a highly standardized ratio of (Thickness : Width : Length):", ["1 : 2 : 4", "1 : 3 : 9", "2 : 4 : 8", "1 : 2 : 3"], 0, "The standard ratio of bricks used in the Mature Harappan phase was strictly 1:2:4."),
    ("Which of the following Mature Harappan sites is famous for its unique three-tier division of the town instead of the typical two-tier division?", ["Dholavira", "Lothal", "Chanhudaro", "Rakhigarhi"], 0, "Dholavira is unique because it is divided into three sections: Citadel, Middle Town, and Lower Town."),
    ("In which Mature Harappan site is there a complete absence of defensive fortifications or a citadel?", ["Chanhudaro", "Kalibangan", "Lothal", "Mohenjo-daro"], 0, "Chanhudaro in Sindh is the only major Mature Harappan town without a fortified citadel structure."),
    ("The trade relations between Mature Harappan cities and Mesopotamia are mentioned in cuneiform texts. What term is used in Mesopotamian records to refer to the Indus region?", ["Meluhha", "Dilmun", "Magan", "Sumer"], 0, "Mesopotamian inscriptions refer to the Indus Valley region as 'Meluhha'."),
    ("Which of the following was the major source of Lapis Lazuli, a semi-precious blue stone imported by Mature Harappans?", ["Shortughai (Afghanistan)", "Khetri (Rajasthan)", "Badakhshan (Iran)", "Lothal (Gujarat)"], 0, "Shortughai in Afghanistan was a Harappan trading colony established near Badakhshan to directly control Lapis Lazuli.")
]:
    mature_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("Which of the following elements characterize the Mature Harappan civic architecture? (Select all that apply)", ["Grid layout of streets intersecting at right angles", "Underground covered drainage systems with soak pits", "Separation of settlements into a Citadel and a Lower Town", "Use of massive stone pillars to support palaces"], [0, 1, 2], "Mature Harappan architecture featured grids, drainage, and division into citadel/lower town. Massive stone pillars were not a feature."),
    ("Identify the major Mature Harappan cities located in modern-day India: (Select all that apply)", ["Dholavira", "Rakhigarhi", "Lothal", "Harappa"], [0, 1, 2], "Dholavira, Rakhigarhi, and Lothal are in India. Harappa is in Punjab, Pakistan."),
    ("Select the archaeological findings associated with Mohenjo-daro: (Select all that apply)", ["The Great Bath", "The Great Granary", "Bronze Dancing Girl statue", "Artificial brick dockyard"], [0, 1, 2], "Mohenjo-daro yielded the Great Bath, Great Granary, and Dancing Girl. Lothal contains the dockyard."),
    ("Identify the primary imports of the Mature Harappan trade network: (Select all that apply)", ["Lapis Lazuli from Badakhshan", "Copper from Khetri mines", "Tin from Afghanistan/Iran", "Silk from China"], [0, 1, 2], "Lapis Lazuli, Copper, and Tin were major imports. Chinese silk was not part of their system."),
    ("Which features are associated with Mature Harappan religious practices? (Select all that apply)", ["Depiction of a proto-Shiva/Pashupati figure on seals", "Worship of Mother Goddess clay figurines", "Worship of pipal tree and bull", "Construction of large temples with stone idols"], [0, 1, 2], "Religion featured Pashupati seals, mother goddess clay figurines, and tree/bull worship. No temples were built.")
]:
    mature_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Mature Harappans built monumental temples with stone statues to worship their gods.", False, "False. No temples have been found; worship was domestic or centered in public baths."),
    ("The standard unit of weight was based on a binary progression of 16 for lighter weights.", True, "True. Lighter weights followed binary ratios (1, 2, 4, 8, 16, 32...) with 16 being the base unit."),
    ("Rakhigarhi is currently recognized as the largest geographic site of the Indus Valley Civilisation.", True, "True. Rakhigarhi is the largest site by area, exceeding Mohenjo-daro."),
    ("The Harappan script has been fully deciphered by Indian epigraphists.", False, "False. The script remains undeciphered due to lack of a bilingual text."),
    ("Lothal contains an artificial brick basin identified by archaeologists as a dockyard.", True, "True. Lothal has a large brick dockyard connected to a river channel."),
    ("Harappans used iron weapons to defend their cities.", False, "False. The Harappans were a Bronze Age civilization and had no knowledge of iron."),
    ("Dholavira is unique for its extensive stone-cut water reservoirs.", True, "True. Dholavira has spectacular stone water reservoirs and dams."),
    ("Steatite was the primary material used to manufacture Harappan seals.", True, "True. Most Harappan seals are made of steatite (soapstone).")
]:
    mature_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The Mature Harappan phase is also known as the __________ Era.", "Integration", "It is known as the Integration Era."),
    ("The largest site of the Indus Valley Civilisation by geographic area is __________.", "Rakhigarhi", "Rakhigarhi is the largest site."),
    ("The artificial brick dockyard of the Harappans was excavated at __________.", "Lothal", "Lothal contains the brick dock."),
    ("The Harappan trading colony established in Afghanistan for Lapis Lazuli is __________.", "Shortughai", "Shortughai was the trading outpost."),
    ("The ratio of brick sizes in the Mature phase was strictly __________.", "1:2:4", "Bricks followed the 1:2:4 ratio."),
    ("The raised part of the Harappan city containing public and administrative buildings is called the __________.", "Citadel", "Citadel was the raised administrative zone."),
    ("Cuneiform texts of Mesopotamia refer to the Indus region as __________.", "Meluhha", "Meluhha is the Mesopotamian term for the Indus region."),
    ("Most Harappan seals were made of a soft stone called __________.", "steatite", "Steatite (soapstone) was primarily used.")
]:
    mature_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
mature_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the Mature Harappan site with its unique architectural feature/discovery:",
        "items": [{"left": "I. Dholavira", "key": "A"}, {"left": "II. Mohenjo-daro", "key": "B"}, {"left": "III. Chanhudaro", "key": "C"}],
        "options": [{"val": "A", "text": "A. Three-tier town division and stone reservoirs"}, {"val": "B", "text": "B. The Great Bath and Great Granary"}, {"val": "C", "text": "C. Bead factory and lack of a fortified citadel"}],
        "sol": "Dholavira has stone reservoirs, Mohenjo-daro has the Great Bath, and Chanhudaro has bead factories."
    },
    {
        "type": "Match the Following",
        "q": "Match the import items of the Mature Harappans with their primary source regions:",
        "items": [{"left": "I. Copper", "key": "A"}, {"left": "II. Lapis Lazuli", "key": "B"}, {"left": "III. Tin", "key": "C"}],
        "options": [{"val": "A", "text": "A. Khetri mines (Rajasthan)"}, {"val": "B", "text": "B. Badakhshan (Afghanistan)"}, {"val": "C", "text": "C. Iran / Afghanistan"}],
        "sol": "Copper was imported from Khetri, Lapis Lazuli from Badakhshan, and Tin from Iran/Afghanistan."
    },
    {
        "type": "Match the Following",
        "q": "Match the Harappan religious symbols with their modern academic interpretations:",
        "items": [{"left": "I. Pashupati Seal", "key": "A"}, {"left": "II. Fire Altars", "key": "B"}, {"left": "III. Terracotta Figurines", "key": "C"}],
        "options": [{"val": "A", "text": "A. Proto-Shiva / Lord of Animals"}, {"val": "B", "text": "B. Ritual sacrifices (found at Lothal/Kalibangan)"}, {"val": "C", "text": "C. Mother Goddess worship"}],
        "sol": "Pashupati represents Proto-Shiva, fire altars represent rituals, and figurines represent Mother Goddess."
    }
])

# One-Liner (8)
for q, sol in [
    ("Name the only Mature Harappan site without a citadel.", "Chanhudaro in Sindh."),
    ("Which site yielded a signboard containing ten large gypsum symbols?", "Dholavira in Kutch, Gujarat."),
    ("What was the primary function of the stone reservoirs discovered at Dholavira?", "Water harvesting and conservation to sustain the city during dry seasons."),
    ("Name the animal most commonly depicted on Mature Harappan seals.", "The Unicorn (a mythical one-horned animal)."),
    ("Which metal alloy is the famous 'Dancing Girl' statue made of?", "Bronze (using the lost-wax casting technique)."),
    ("Which river basin hosted the maximum density of Mature Harappan settlements?", "The Ghaggar-Hakra river basin (often identified as the Sarasvati system)."),
    ("Name the Mesopotamian king who recorded trade lists with Meluhha.", "Sargon of Akkad (c. 2334–2279 BCE)."),
    ("What is the name of the southernmost trading port site of the Mature phase in Gujarat?", "Lothal.")
]:
    mature_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The streets of Mature Harappan cities were strictly planned in a grid pattern.\nReason (R): The municipal authority enforced strict regulations prohibiting building construction over public pathways.", 0, "Both A and R are true and R explains A. Rigid alignment indicates municipal oversight."),
    ("Assertion (A): Lothal acted as a major trade conduit between Gujarat and Mesopotamia.\nReason (R): Archaeologists excavated a large brick basin connected to the Sabarmati river and a bead-making factory at Lothal.", 0, "The dockyard and bead factory prove its port and manufacturing role."),
    ("Assertion (A): Harappans did not worship their gods in large congregational temples.\nReason (R): No monumental temple ruins, sanctuaries, or large stone statues have been discovered at any Harappan site.", 0, "Lack of temples indicates domestic and naturalistic religious forms."),
    ("Assertion (A): The Harappan civilization was a cohesive empire ruled by a single all-powerful priest-king.\nReason (R): There is a complete lack of evidence for weapons, standing armies, or royal palace burials at Harappan sites.", 3, "A is false because a single priest-king is a speculatory theory, and lack of weapons suggests peaceful/decentralized networks. R is true."),
    ("Assertion (A): The Harappans established a trading outpost at Shortughai in northern Afghanistan.\nReason (R): Shortughai provided direct administrative control over the mining and transport of Lapis Lazuli from Badakhshan.", 0, "Shortughai was specifically situated to exploit Lapis Lazuli deposits."),
    ("Assertion (A): Bricks of uniform sizes were used across all Mature Harappan settlements.\nReason (R): The standard ratio of 1:2:4 ensured structural stability for double-storey houses and municipal fortifications.", 0, "Bricks were modular and highly standardized to the 1:2:4 ratio."),
    ("Assertion (A): The Harappan script was logosyllabic in nature.\nReason (R): It contains between 400 and 600 distinct symbols, which is too many for an alphabet and too few for a true pictographic writing system.", 0, "It represents a logosyllabic system where symbols stand for words/syllables."),
    ("Assertion (A): Steatite seals were used strictly as currency in local markets.\nReason (R): Seals were primarily used as commercial stamps to authenticate clay sealings on trade cargo exported to distant lands.", 3, "Assertion is false: seals were not currency. Reason is true.")
]:
    mature_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Citadel:\n1. It was always located in the eastern part of the city and was heavily populated.\n2. It housed public structures like the Great Bath and administrative offices.\nWhich of the statements given above is/are correct?", 1, "The Citadel was located in the western part of the city, not eastern. Statement 2 is correct."),
    ("Consider the following statements regarding the Harappan drainage system:\n1. Drains were covered with brick slabs or stone slabs that could be removed for cleaning.\n2. Household waste water flowed directly into streets without any soakage pits.\nWhich of the statements given above is/are correct?", 0, "Houses had soak pits/sumps to settle solid waste before water entered public drains."),
    ("Consider the following statements regarding the weight system:\n1. The weights were made of chert and were primarily cubical in shape.\n2. The system followed decimal multiples for higher weights.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Lighter weights were binary, while higher weights followed decimal progressions."),
    ("Consider the following statements regarding the Dholavira signboard:\n1. It was made of ten large gypsum symbols embedded on a wooden board.\n2. It contains the longest deciphered text in the Indus script.\nWhich of the statements given above is/are correct?", 0, "It remains undeciphered, though it is the longest single sign representation."),
    ("Consider the following statements regarding the Pashupati seal:\n1. The deity is seated in a yogic posture and is surrounded by animals.\n2. The animals include an elephant, tiger, rhinoceros, buffalo, and deer.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Pashupati is surrounded by these five animals.")
]:
    mature_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for qtype, q, sol in [
    ("Why", "Why is there a complete absence of massive stone palaces and temples in Harappa compared to Egypt?", "The sociopolitical system prioritized public utility (sanitation, grain storage, water systems) over monumental tombs or divine rulers."),
    ("Why", "Why did the Harappans establish their colony at Shortughai in northern Afghanistan?", "To secure and control the Lapis Lazuli trade route from Badakhshan, showing calculated merchant statecraft."),
    ("Why", "Why did the binary unit of 16 serve as the base weight for the Harappan commercial system?", "The weight (13.63g) was highly practical for small exchanges. Its legacy survived in the Indian currency system (16 annas = 1 rupee) for millennia."),
    ("How", "How did the Harappan script and seals facilitate long-distance trade with Mesopotamia?", "Steatite seals were pressed into clay knots on cargo, creating a seal that verified origin and ensured contents were untampered with."),
    ("How", "How did Dholavira manage its water resources in the arid climate of Kutch?", "By constructing dams across seasonal streams and channeling water into massive rock-cut reservoirs surrounding the Citadel."),
    ("How", "How did the standardized 1:2:4 brick ratio contribute to the uniformity of Harappan cities?", "It allowed consistent building guides. Combined with the English bond laying system, it created sturdy public walls across the subcontinent."),
    ("Case Study", "Case Study: The Great Bath of Mohenjo-daro", "A bitumen-sealed brick pool measuring 12m x 7m x 2.4m, containing changing rooms and drainage channels. It indicates a culture that valued ritual purity and public bathing."),
    ("Case Study", "Case Study: The Lost-Wax Casting of the Dancing Girl", "The 10.5 cm bronze statue was cast using the lost-wax process (wax model covered in clay, melted out, filled with bronze), showing advanced metallurgical mastery."),
    ("Case Study", "Case Study: The Meluhha Inscriptions of Mesopotamia", "Cuneiform tablets from Sargon of Akkad state that ships from Meluhha (Indus) docked at Akkadian ports, carrying Carnelian beads, gold, and ivory."),
    ("Teach the Concept", "Teach the Concept: The Grid System and Sanitation", "Explain: (1) straight intersecting roads (90 degrees), (2) covered street drains, (3) private household connections, and (4) manholes for waste removal."),
    ("Teach the Concept", "Teach the Concept: The Harappan Weights and Measures", "Explain: (1) cubical chert weights, (2) binary progression (1, 2, 4, 8, 16, 32...) for light goods, (3) decimal progression for heavy goods, (4) 1:2:4 brick standards."),
    ("Teach the Concept", "Teach the Concept: Pashupati and Mother Goddess Worship", "Explain: (1) Pashupati seal showing horned yogic figure surrounded by animals, (2) clay Mother Goddess figurines, (3) worship of pipal trees, bulls, and water.")
]:
    mature_mastery_eng.append({"type": qtype, "q": q, "sol": sol})


# ----------------- SECTION 3: LATE HARAPPAN (ENGLISH) -----------------
late_mastery_eng = []

# MCQs (5)
for q, opts, ans, sol in [
    ("The Late Harappan phase in Sindh is archaeologically characterized by which localized culture?", ["Jhukar Culture", "Cemetery H Culture", "Malwa Culture", "Ahar-Banas Culture"], 0, "The Jhukar culture represents the post-urban, Late Harappan phase in Sindh."),
    ("Which of the following outposts of the Late Harappan phase is located in western Uttar Pradesh, marking the easternmost limit of the civilization?", ["Alamgirpur", "Daimabad", "Manda", "Sutkagendor"], 0, "Alamgirpur in Meerut district (UP) represents the easternmost Late Harappan site, situated on the Hindon River."),
    ("At which of the following sites in Haryana have archaeologists excavated structures showing an overlap of Late Harappan and Painted Grey Ware (PGW) cultures?", ["Bhagwanpura", "Rakhigarhi", "Banawali", "Kunal"], 0, "Bhagwanpura in Haryana shows clear stratigraphic evidence of an overlap between the Late Harappan and the early Painted Grey Ware (associated with Vedic culture) users."),
    ("Which Late Harappan site in Gujarat has yielded extensive Lustrous Red Ware (LRW) pottery but lacks a Mature Harappan level?", ["Rangpur", "Lothal", "Dholavira", "Surkotada"], 0, "Rangpur in Gujarat represents the Late Harappan Lustrous Red Ware phase and lacks a Mature Harappan level."),
    ("The southernmost outpost of the Late Harappan phase, famous for yielding the Daimabad Bronzes (chariot, elephant, bull), is situated along which river?", ["Pravara River", "Narmada River", "Tapti River", "Godavari River"], 0, "Daimabad is situated on the Pravara River, a tributary of the Godavari, in Maharashtra.")
]:
    late_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("What major changes occurred during the transition from Mature to Late Harappan phases? (Select all that apply)", ["Disappearance of the Harappan script and steatite seals", "Abandonment of the standardized cubical weights and measures", "Abandonment of the central municipal drainage system", "Widespread introduction of iron metallurgy"], [0, 1, 2], "The transition saw the loss of script, seals, standardized weights, and municipal drainage. Iron tools were NOT introduced; iron came to India around 1000 BCE."),
    ("Identify the regional sub-cultures of the Late Harappan Localisation Era: (Select all that apply)", ["Jhukar Culture in Sindh", "Cemetery H Culture in Punjab", "Lustrous Red Ware in Gujarat", "Malwa Culture in Madhya Pradesh"], [0, 1, 2], "Jhukar, Cemetery H, and Lustrous Red Ware are Late Harappan sub-cultures. Malwa is a distinct chalcolithic culture."),
    ("Which Late Harappan outposts represent the peripheral expansion of the late phase? (Select all that apply)", ["Daimabad in Maharashtra", "Alamgirpur in Uttar Pradesh", "Hulas in Uttar Pradesh", "Sutkagendor in Balochistan"], [0, 1, 2], "Daimabad, Alamgirpur, and Hulas are Late Harappan outposts. Sutkagendor was a Mature phase trading outpost in Balochistan."),
    ("Select the correct statements regarding the Cemetery H culture: (Select all that apply)", ["It represents the post-urban Late Harappan phase in Punjab", "It features painted urn burials with geometric/bird motifs", "It shows a complete lack of writing and standard weights", "It introduced horse-drawn chariots to India"], [0, 1, 2], "Cemetery H represents the Late phase in Punjab with urn burials and no writing. Chariots were not part of this culture."),
    ("Identify the factors that modern historians attribute to the decline of the Mature Harappan phase: (Select all that apply)", ["Gradual environmental drying and monsoonal shifts", "Tectonic changes causing river course diversions", "Drying of the Ghaggar-Hakra river system", "A sudden, bloody invasion by nomadic Aryan tribes"], [0, 1, 2], "Modern historians agree on environmental, tectonic, and river changes as causes. The Aryan invasion theory is rejected due to lack of skeletons and archaeological proof.")
]:
    late_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Late Harappan phase represents the sudden and complete extinction of the Indus population.", False, "False. It represents de-urbanization and ruralisation, not extinction; people migrated eastward and southward."),
    ("Daimabad in Maharashtra yielded a set of four heavy bronze sculptures representing late-phase metallurgy.", True, "True. The Daimabad Bronzes include a chariot driver, bull, elephant, and rhinoceros."),
    ("The Painted Grey Ware (PGW) culture overlaps with the Late Harappan phase at Bhagwanpura.", True, "True. Bhagwanpura shows a stratigraphic overlap between the two cultures."),
    ("Iron metallurgy was extensively used during the Late Harappan phase.", False, "False. Late Harappan remained pre-Iron; iron tools were introduced later in the Vedic period."),
    ("Late Harappan houses were built using old, reused bricks laid out in a haphazard manner.", True, "True. Civic standards collapsed, and people built homes over older roads using recycled bricks."),
    ("Direct maritime trade with Mesopotamia peaked during the Late Harappan phase.", False, "False. The Meluhhan trade collapsed completely during the Late Harappan phase."),
    ("Rangpur in Gujarat is a major site of the Lustrous Red Ware culture.", True, "True. Rangpur is a type site for LRW in Gujarat."),
    ("Steatite seals and the Indus script continued to be used during the Cemetery H phase.", False, "False. Script and seals disappeared during the post-urban Late Harappan phase.")
]:
    late_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The Late Harappan phase is also known as the __________ Era.", "Localisation", "It is known as the Localisation Era."),
    ("The post-urban culture of the Late phase in Sindh is known as the __________ Culture.", "Jhukar", "Jhukar is the Sindh post-urban culture."),
    ("The easternmost limit of the Late Harappan phase is situated at __________.", "Alamgirpur", "Alamgirpur in UP represents the eastern limit."),
    ("A stratigraphic overlap of Late Harappan and PGW cultures was excavated at __________ in Haryana.", "Bhagwanpura", "Bhagwanpura contains the overlap layer."),
    ("The southernmost Late Harappan site on the Pravara River is __________.", "Daimabad", "Daimabad is the southernmost outpost."),
    ("The ceramic style representing Late Harappan Gujarat is __________ Ware.", "Lustrous Red", "Lustrous Red Ware represents post-urban Gujarat."),
    ("Late Harappans migrated away from the Indus basin towards the __________ valley.", "Ganga", "They migrated towards the Ganga-Yamuna Doab."),
    ("The post-urban burial culture discovered at Harappa is called __________.", "Cemetery H", "Cemetery H is the post-urban culture at Harappa.")
]:
    late_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
late_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the Late Harappan regional cultures with their primary geographic locations:",
        "items": [{"left": "I. Jhukar Culture", "key": "A"}, {"left": "II. Cemetery H Culture", "key": "B"}, {"left": "III. Lustrous Red Ware", "key": "C"}],
        "options": [{"val": "A", "text": "A. Sindh (Pakistan)"}, {"val": "B", "text": "B. Punjab (Harappa)"}, {"val": "C", "text": "C. Gujarat (Rangpur/Rojdi)"}],
        "sol": "Jhukar is in Sindh, Cemetery H in Punjab, and Lustrous Red Ware in Gujarat."
    },
    {
        "type": "Match the Following",
        "q": "Match the Late Harappan outposts with their respective geographic directions relative to the core zone:",
        "items": [{"left": "I. Alamgirpur", "key": "A"}, {"left": "II. Daimabad", "key": "B"}, {"left": "III. Manda", "key": "C"}],
        "options": [{"val": "A", "text": "A. Easternmost outpost (Uttar Pradesh)"}, {"val": "B", "text": "B. Southernmost outpost (Maharashtra)"}, {"val": "C", "text": "C. Northernmost outpost (Jammu & Kashmir)"}],
        "sol": "Alamgirpur is east, Daimabad is south, and Manda is north."
    },
    {
        "type": "Match the Following",
        "q": "Match the academic theories of the Harappan decline with their primary proponents:",
        "items": [{"left": "I. Aryan Invasion", "key": "A"}, {"left": "II. Tectonic Uplift & Flooding", "key": "B"}, {"left": "III. Drying of Ghaggar River", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mortimer Wheeler"}, {"val": "B", "text": "B. Robert L. Raikes"}, {"val": "C", "text": "C. D.P. Agrawal / M.R. Mughal"}],
        "sol": "Wheeler proposed Aryan invasion, Raikes proposed tectonic flooding, and Agrawal linked it to the drying Ghaggar."
    }
])

# One-Liner (8)
for q, sol in [
    ("Name the easternmost outpost of the Late Harappan phase, located on the Hindon River.", "Alamgirpur in Uttar Pradesh."),
    ("Which site shows a continuous overlap of Late Harappan and PGW (Vedic) levels?", "Bhagwanpura in Haryana."),
    ("Name the southernmost Late Harappan outpost, situated in Maharashtra.", "Daimabad in Ahmednagar district."),
    ("What are the post-urban ceramic styles of late-phase Gujarat called?", "Lustrous Red Ware (LRW)."),
    ("Which metal was completely absent from the Late Harappan tool kit?", "Iron (they remained in the Bronze/Copper Age)."),
    ("What was the primary direction of population migration during the Late Harappan decline?", "Eastward (into the Ganga-Yamuna Doab) and Southward (into Gujarat)."),
    ("Which post-urban culture in Sindh is named after a site near Chanhudaro?", "The Jhukar Culture."),
    ("What is the name of the Late Harappan site in Uttar Pradesh known for lack of civic drains?", "Hulas.")
]:
    late_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Late Harappan phase represents de-urbanization and civic regression.\nReason (R): Standardized scripts, seals, and grid city layouts disappeared, replaced by rural agricultural hamlets.", 0, "Both A and R are true and R explains A. De-urbanization led directly to rural fragmentation."),
    ("Assertion (A): Daimabad is recognized as the southernmost limit of the Late Harappan expansion.\nReason (R): Archaeologists excavated heavy bronze figures of a chariot, bull, and rhinoceros on the Pravara River.", 0, "The Daimabad Bronzes prove its late metal workshops and peripheral status."),
    ("Assertion (A): The Cemetery H culture shows an overlap with Painted Grey Ware.\nReason (R): Cemetery H represents the post-urban phase at Harappa, whereas the PGW overlap is excavated at Bhagwanpura in Haryana.", 1, "Both statements are correct but R does not explain A (they are different geographic markers)."),
    ("Assertion (A): Late Harappan populations migrated away from the Indus basin.\nReason (R): Shifting monsoons and tectonic diversions dried up major perennial rivers like the Ghaggar-Hakra, making agriculture difficult.", 0, "Drying of main rivers was the primary driver of eastward migration."),
    ("Assertion (A): Late Harappan builders used stone columns to reinforce their houses.\nReason (R): Civic standards collapsed, and homes were built using recycled, old bricks in a haphazard layout over older streets.", 3, "A is false because stone columns were not used. R is true."),
    ("Assertion (A): Direct trade with Mesopotamia collapsed during the Late Harappan phase.\nReason (R): Mesopotamian records of the post-2000 BCE period show a complete absence of references to Meluhha imports.", 0, "Trade breakdown is confirmed by Akkadian/Babylonian tablets."),
    ("Assertion (A): The Ochre Coloured Pottery (OCP) culture is contemporary with Late Harappans in the Gangetic valley.\nReason (R): OCP communities were associated with copper hoards and overlapped with late-phase Harappan outposts.", 0, "OCP represents the local chalcolithic context that interacted with Late Harappans."),
    ("Assertion (A): The Aryan invasion theory is the most widely accepted cause of the Harappan decline today.\nReason (R): Archaeological excavations show a complete lack of evidence for weapons, massacres, or burnt fortifications at Mohenjo-daro.", 3, "A is false (invasion is rejected). R is true.")
]:
    late_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Late Harappan pottery:\n1. It shows a complete loss of the stylized painting of Mature Harappan ceramics.\n2. Localized styles like Lustrous Red Ware (LRW) emerged in Gujarat.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding outposts:\n1. Alamgirpur in Uttar Pradesh represents the easternmost outpost of the Late Harappan phase.\n2. Daimabad in Maharashtra represents the northernmost outpost.\nWhich of the statements given above is/are correct?", 0, "Daimabad is the southernmost limit, not northern."),
    ("Consider the following statements regarding the overlap phase:\n1. Bhagwanpura in Haryana shows a stratigraphic overlap of Late Harappan and PGW.\n2. Iron tools are found alongside bronze tools in this overlap layer.\nWhich of the statements given above is/are correct?", 0, "No iron is found in the Bhagwanpura overlap, showing Late Harappans remained pre-Iron."),
    ("Consider the following statements regarding the Jhukar culture:\n1. It represents the post-urban Late Harappan phase in Sindh.\n2. Steatite seals with script were replaced by circular geometric button seals.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements regarding decline theories:\n1. Mortimer Wheeler proposed the Aryan Invasion theory based on skeletal remains at Mohenjo-daro.\n2. Modern DNA studies of Harappan skeletons show no genetic markers of sudden Central Asian invasions during the decline.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. DNA disproves Wheeler.")
]:
    late_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for qtype, q, sol in [
    ("Why", "Why did the Harappans abandon their grid layouts and underground drains during the Late phase?", "The breakdown of municipal authorities and loss of agricultural trade surplus ended grid planning and drain maintenance."),
    ("Why", "Why did the long-distance trade with Mesopotamia collapse after 1900 BCE?", "River drying and loss of craft standards ended the export surplus, while Mesopotamia redirected trade to Mediterranean networks."),
    ("Why", "Why is the Late Harappan phase called the 'Localisation Era'?", "Because uniform pan-regional styles disintegrated into localized regional cultures (Jhukar, Cemetery H, Lustrous Red Ware)."),
    ("How", "How did tectonic shifts in the Ghaggar-Hakra river system contribute to the decline?", "Tectonic activity diverted water channels (Sutlej to Indus, Yamuna to Ganga), drying up the Ghaggar-Hakra basin and forcing migrations."),
    ("How", "How did the Late Harappan metallurgy differ from the Mature Harappan metallurgy?", "Lost-wax complex casting declined; metalwork focused on heavy, utilitarian copper tools. Tin importing collapsed, but it remained pre-Iron."),
    ("How", "How did the transition from urban to rural settlements affect Harappan social structure?", "Loss of writing, seals, and central storage indicates the collapse of the merchant and ruling elites, reverting to decentralized chiefdoms."),
    ("Case Study", "Case Study: The Daimabad Bronzes cache", "Daimabad yielded 60kg of heavy copper castings (chariot, rhinoceros, elephant, bull), proving that metallurgy survived in remote outposts during de-urbanization."),
    ("Case Study", "Case Study: The Overlap at Bhagwanpura", "Stratigraphy reveals Late Harappan houses overlapping with Painted Grey Ware (PGW), proving peaceful coexistence during the transition to the Vedic period."),
    ("Case Study", "Case Study: The Jhukar Button Seals", "In Sindh, steatite script seals were replaced by circular geometric button seals, indicating the end of formal administrations and the rise of local tokens."),
    ("Teach the Concept", "Teach the Concept: De-urbanization vs Extinction", "Explain that the end of Harappa was a civic collapse, not a population extinction; the people migrated to Ganga/Gujarat, preserving agricultural traditions."),
    ("Teach the Concept", "Teach the Concept: The Late Harappan Regional Cultures", "Explain: (1) Jhukar (Sindh) with button seals, (2) Cemetery H (Punjab) with urn burials, and (3) Lustrous Red Ware (Gujarat) with red ceramics."),
    ("Teach the Concept", "Teach the Concept: The Overlap of Late Harappan and Vedic Cultures", "Explain that Vedic transition was peaceful; sites like Bhagwanpura show late-phase Bronze Age and early Iron Age (PGW) peoples coexisting.")
]:
    late_mastery_eng.append({"type": qtype, "q": q, "sol": sol})


# ----------------- HINDI LISTS DEFINITION -----------------
early_mastery_hin = []

# MCQs (5)
for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन सा स्थल हड़प्पा विकास के सबसे प्रारंभिक हाकड़ा मृदभांड चरण का प्रतिनिधित्व करता है?", ["भिरड़ाना", "मोहनजोदड़ो", "लोथल", "चन्हुदड़ो"], 0, "हरियाणा का भिरड़ाना सबसे पुराना हाकड़ा मृदभांड चरण (चौथी सहस्राब्दी ईसा पूर्व) का प्रतिनिधित्व करता है।"),
    ("आड़े-तिरछे जुते हुए खेत का प्रसिद्ध पूर्व-परिपक्व साक्ष्य कहाँ से खोजा गया था?", ["कालीबंगन", "बनावली", "हड़प्पा", "कोट दीजी"], 0, "राजस्थान के कालीबंगन से एक अद्वितीय पूर्व-परिपक्व (प्रारंभिक हड़प्पा) जुता हुआ खेत मिला है।"),
    ("सिंध में आमरी की पूर्व-हड़प्पा बस्ती किस विशिष्ट खोज के लिए प्रसिद्ध है?", ["हिरण/एंटेलोप रूपांकनों से रंगे मिट्टी के बर्तन", "एक विशाल पत्थर का गोदीवाड़ा (dockyard)", "टेराकोटा घोड़े की मूर्तियाँ", "लाजवर्त (Lapis Lazuli) की मुहरें"], 0, "आमरी अपने पूर्व-हड़प्पा स्तरों के लिए प्रसिद्ध है जो हिरण रूपांकनों वाले मृदभांड दर्शाते हैं।"),
    ("प्रारंभिक सामाजिक स्तरीकरण को दर्शाने वाले दो चांदी के मुकुट और सोने के आभूषण कहाँ से मिले हैं?", ["कुणाल", "भिरड़ाना", "आमरी", "बनावली"], 0, "हरियाणा के कुणाल से चांदी के दो मुकुट और आभूषण मिले हैं।"),
    ("रावी चरण (लगभग 3300-2800 ईसा पूर्व) किस प्रमुख स्थल पर सबसे प्रारंभिक स्तर का प्रतिनिधित्व करता है?", ["हड़प्पा", "मोहनजोदड़ो", "कालीबंगन", "धोलावीरा"], 0, "रावी चरण हड़प्पा में सबसे पहले रहने वाले स्तर का प्रतिनिधित्व करता है।")
]:
    early_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("प्रारंभिक हड़प्पा चरण की विशेषताएँ क्या हैं? (लागू होने वाले सभी विकल्प चुनें)", ["रक्षात्मक किलेबंदी का उदय", "चाक-निर्मित बर्तनों का मानकीकरण", "प्रारंभिक तांबे और कांस्य का धातु कर्म", "मानकीकृत ग्रिड-नियोजित सड़कों का उपयोग"], [0, 1, 2], "प्रारंभिक हड़प्पा में किलेबंदी, चाक के बर्तन और धातु कर्म था। ग्रिड सड़कें परिपक्व चरण में आईं।"),
    ("प्रारंभिक हड़प्पा चरण से जुड़े स्थलों की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)", ["भिरड़ाना", "कोट दीजी", "आमरी", "सुरकोटदा"], [0, 1, 2], "भिरड़ाना, कोट दीजी और आमरी प्रारंभिक स्थल हैं। सुरकोटदा परिपक्व/उत्तर काल का है।"),
    ("हड़प्पा के रावी चरण से कौन सी विशेषताएं जुड़ी हैं? (लागू होने वाले सभी विकल्प चुनें)", ["मिट्टी के बर्तनों पर कुम्हार के निशान और शुरुआती लिपि", "मनके (bead) बनाने का उद्योग", "कुम्हार के चाक का उपयोग", "विशाल स्नानागार का निर्माण"], [0, 1, 2], "रावी चरण में निशान, मनके और चाक का उपयोग था। स्नानागार परिपक्व काल का है।"),
    ("उन प्रारंभिक हड़प्पा स्थलों को चुनें जहाँ किलेबंदी के साक्ष्य मिले हैं: (लागू होने वाले सभी विकल्प चुनें)", ["कोट दीजी", "कालीबंगन", "भिरड़ाना", "लोथल"], [0, 1, 2], "कोट दीजी, कालीबंगन और भिरड़ाना में प्रारंभिक किलेबंदी है। लोथल परिपक्व चरण का बंदरगाह है।"),
    ("हाकड़ा मृदभांड की विशेषताएं पहचानें: (लागू होने वाले सभी विकल्प चुनें)", ["मुख्य रूप से हाथ से बनी मिट्टी के बर्तनों की शैली", "चॉकलेट स्लिप वाले मोटे दीवार के बर्तन", "चोलिस्तान और हरियाणा क्षेत्र में पाए गए", "लोहे के उपयोग वाले बर्तन"], [0, 1, 2], "हाकड़ा बर्तन हाथ से बने, चॉकलेट स्लिप वाले और चोलिस्तान/हरियाणा में मिले थे। लोहा अज्ञात था।")
]:
    early_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("हाकड़ा मृदभांड चरण हड़प्पा के रावी चरण से पुराना है।", True, "सत्य। हाकड़ा चरण (3800-3200 ईसा पूर्व) रावी चरण (3300-2800 ईसा पूर्व) से पुराना है।"),
    ("कोट दीजी चरण परिपक्व हड़प्पा के शहरी चरम का प्रतिनिधित्व करता है।", False, "असत्य। कोट दीजी प्रारंभिक हड़प्पा के प्रोटो-शहरी चरण का प्रतिनिधित्व करता है।"),
    ("प्रारंभिक हड़प्पा चरण के दौरान मनुष्यों ने लोहे के उपकरणों का उपयोग किया था।", False, "असत्य। संपूर्ण हड़प्पा सभ्यता कांस्य युगीन (लौह-पूर्व) थी।"),
    ("कालीबंगन का जुता हुआ खेत परिपक्व हड़प्पा काल का है।", False, "असत्य। यह पूर्व-परिपक्व प्रारंभिक हड़प्पा चरण का है।"),
    ("एम.आर. मुगल पहले पुरातत्वविद् थे जिन्होंने प्रारंभिक हड़प्पा चरण को व्यवस्थित रूप से परिभाषित किया।", True, "सत्य। रफीक मुगल ने चोलिस्तान के सर्वेक्षणों के आधार पर इसे परिभाषित किया।"),
    ("प्रारंभिक हड़प्पा के कुम्हार चाक के उपयोग से पूरी तरह अनजान थे।", False, "असत्य। चाक-निर्मित बर्तनों (रावी और कोट दीजी बर्तन) का विकास हो चुका था।"),
    ("हरियाणा के भिरड़ाना को एएसआई द्वारा सबसे पुराना हड़प्पा स्थल माना गया है।", True, "सत्य। भिरड़ाना से सबसे पुराने हाकड़ा मृदभांड स्तर मिले हैं।"),
    ("प्रारंभिक हड़प्पा चरण में सामाजिक स्तरीकरण पूरी तरह से अनुपस्थित था।", False, "असत्य। कुणाल से मिले चांदी के मुकुट सामाजिक भिन्नता के संकेत हैं।")
]:
    early_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("प्रारंभिक हड़प्पा चरण को सिंधु घाटी सभ्यता के __________ युग के रूप में भी जाना जाता है।", "क्षेत्रीयकरण", "इसे क्षेत्रीयकरण का युग (Regionalisation Era) कहा जाता है।"),
    ("एएसआई के अनुसार सबसे पुराना हड़प्पा स्थल __________ है।", "भिरड़ाना", "हरियाणा का भिरड़ाना सबसे पुराना स्थल है।"),
    ("प्रारंभिक सामाजिक स्तरीकरण को दर्शाने वाले दो चांदी के मुकुट __________ से मिले हैं।", "कुणाल", "कुणाल से चांदी के मुकुट मिले हैं।"),
    ("बर्तनों पर चित्रित सींग वाले देवता के चित्र __________ चरण की विशेषता हैं।", "कोट दीजी", "कोट दीजी के बर्तनों पर सींग वाले देवता चित्रित हैं।"),
    ("रावी चरण की पहचान सबसे पहले __________ स्थल पर की गई थी।", "हड़प्पा", "रावी चरण हड़प्पा का सबसे प्रारंभिक स्तर है।"),
    ("आड़े-तिरछे जुते हुए खेत का साक्ष्य __________ में स्थित है।", "कालीबंगन", "कालीबंगन में जुता हुआ खेत मिला है।"),
    ("हाकड़ा मृदभांड चरण __________ सहस्राब्दी ईसा पूर्व का है।", "चौथी", "हाकड़ा बर्तन चौथी सहस्राब्दी ईसा पूर्व (3800-3200 ईसा पूर्व) के हैं।"),
    ("सिंध के पूर्व-परिपक्व स्तरों को __________ स्थल द्वारा दर्शाया जाता है।", "आमरी", "आमरी सिंध के पूर्व-परिपक्व स्तरों का प्रकार-स्थल है।")
]:
    early_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
early_matching = [
    {
        "type": "Match the Following",
        "q": "प्रारंभिक हड़प्पा स्थलों को उनके संबंधित आधुनिक भारतीय राज्यों/प्रांतों से सुमेलित करें:",
        "items": [{"left": "I. भिरड़ाना", "key": "A"}, {"left": "II. कालीबंगन", "key": "B"}, {"left": "III. कोट दीजी", "key": "C"}],
        "options": [{"val": "A", "text": "A. हरियाणा"}, {"val": "B", "text": "B. राजस्थान"}, {"val": "C", "text": "C. सिंध (पाकिस्तान)"}],
        "sol": "भिरड़ाना हरियाणा में, कालीबंगन राजस्थान में, और कोट दीजी सिंध में है।"
    },
    {
        "type": "Match the Following",
        "q": "प्रारंभिक हड़प्पा सांस्कृतिक चरणों को उनके अनुमानित कालक्रम से सुमेलित करें:",
        "items": [{"left": "I. हाकड़ा मृदभांड चरण", "key": "A"}, {"left": "II. रावी चरण", "key": "B"}, {"left": "III. कोट दीजी चरण", "key": "C"}],
        "options": [{"val": "A", "text": "A. लगभग 3800 ईसा पूर्व – 3200 ईसा पूर्व"}, {"val": "B", "text": "B. लगभग 3300 ईसा पूर्व – 2800 ईसा पूर्व"}, {"val": "C", "text": "C. लगभग 2800 ईसा पूर्व – 2600 ईसा पूर्व"}],
        "sol": "ये प्रारंभिक हड़प्पा काल के कालानुक्रमिक विकास को दर्शाते हैं।"
    },
    {
        "type": "Match the Following",
        "q": "प्रारंभिक हड़प्पा स्थलों को उनकी अनूठी पुरातात्विक खोजों से सुमेलित करें:",
        "items": [{"left": "I. कुणाल", "key": "A"}, {"left": "II. कालीबंगन", "key": "B"}, {"left": "III. आमरी", "key": "C"}],
        "options": [{"val": "A", "text": "A. चांदी के मुकुट और सोने के आभूषण"}, {"val": "B", "text": "B. आड़े-तिरछे जुते हुए खेत का साक्ष्य"}, {"val": "C", "text": "C. हिरण और ज्यामितीय चित्रों वाले मृदभांड"}],
        "sol": "कुणाल में मुकुट, कालीबंगन में जुते खेत, और आमरी में हिरण के चित्र मिले हैं।"
    }
]
early_mastery_hin.extend(early_matching)

# One-Liner (8)
for q, sol in [
    ("प्रारंभिक हड़प्पा चरण को व्यवस्थित रूप से परिभाषित करने वाले पुरातत्वविद् का नाम बताएं।", "एम.आर. मुगल (रफीक मुगल) ने चोलिस्तान में विस्तृत सर्वेक्षणों के आधार पर इसे परिभाषित किया।"),
    ("सिंध के किस प्रारंभिक हड़प्पा स्थल से परिपक्व चरण से पहले भीषण आग से तबाही के साक्ष्य मिले हैं?", "कोट दीजी से राख की एक मोटी परत मिली है जो विनाश दर्शाती है।"),
    ("आमरी की पूर्व-परिपक्व बस्ती किस नदी के किनारे स्थित है?", "सिंधु नदी (बाएं तट पर, मोहनजोदड़ो के विपरीत)।"),
    ("भारतीय उपमहाद्वीप में सबसे पुराने जुते हुए खेत का साक्ष्य कहाँ मिला है?", "कालीबंगन में।"),
    ("रावी चरण के बर्तनों पर मिले शुरुआती लिपि-जैसे निशानों को क्या कहा जाता है?", "कुम्हार के निशान या भित्तिचित्र (graffiti) निशान।"),
    ("प्रारंभिक हड़प्पा काल में मुख्य रूप से किस धातु का उपयोग किया जाता था?", "तांबा (और कांस्य का प्रारंभिक उपयोग)।"),
    ("पाकिस्तान के किस क्षेत्र में हाकड़ा और प्रारंभिक हड़प्पा बस्तियों का सबसे अधिक घनत्व है?", "चोलिस्तान रेगिस्तान (घग्गर-हाकड़ा घाटी)।"),
    ("हरियाणा में पाए जाने वाले सबसे पुराने पूर्व-परिपक्व मृदभांड का नाम क्या है?", "हाकड़ा मृदभांड।")
]:
    early_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("कथन (A): गंगा के मैदानी इलाकों में प्रारंभिक हड़प्पा बस्तियों का पूर्ण अभाव था।\nकारण (R): शुरुआती किसानों ने गंगा के मैदानों से परहेज किया क्योंकि वहाँ पत्थर के संसाधनों (औजारों के लिए) की भारी कमी थी।", 0, "दोनों कथन सत्य हैं और कारण कथन की सही व्याख्या है। मैदानी भाग में पत्थरों की कमी थी."),
    ("कथन (A): हाकड़ा से रावी चरण में संक्रमण कृषि स्थिरता को दर्शाता है।\nReason (R): रावी चरण के दौरान चाक-निर्मित बर्तनों और लिपि-जैसे चिह्नों का उदय शुरू हो गया था।", 0, "रावी चरण उच्च स्तर के संगठन को दर्शाता है।"),
    ("कथन (A): प्रारंभिक चरण में कोट दीजी और कालीबंगन में रक्षात्मक दीवारें बनाई गई थीं।\nReason (R): प्रारंभिक हड़प्पा समुदायों को बाढ़ और चरवाहा समूहों से पशु चोरी का खतरा था।", 0, "दीवारें सुरक्षा और बाढ़ दोनों से बचाव करती थीं।"),
    ("कथन (A): प्रारंभिक हड़प्पा चरण को क्षेत्रीयकरण का युग कहा जाता है।\nReason (R): अखिल भारतीय एकीकरण से पहले इस समय स्थानीय मृदभांड और क्षेत्रीय शैलियों का प्रभुत्व था।", 0, "क्षेत्रीय शैलियाँ विभिन्न हिस्सों में स्वतंत्र रूप से विकसित हो रही थीं।"),
    ("कथन (A): कुणाल में सामाजिक स्तरीकरण के प्रारंभिक लक्षण दिखते हैं।\nReason (R): यहाँ से चांदी के दो मुकुट और सोने के आभूषणों का भंडार मिला है।", 0, "चांदी के मुकुट शासक वर्ग की उपस्थिति के साक्ष्य हैं।"),
    ("कथन (A): कालीबंगन के जुते हुए खेत उन्नत कृषि ज्ञान को दर्शाते हैं।\nReason (R): खेत में आड़े-तिरछे जुताई के निशान हैं, जो दो अलग-अलग फसलें एक साथ उगाने का संकेत हैं।", 0, "दोहरी फसल प्रणाली कालीबंगन-I में दिखती है।"),
    ("कथन (A): प्रारंभिक हड़प्पावासियों का मेसोपोटामिया के साथ कोई सीधा समुद्री व्यापार नहीं था।\nReason (R): मेसोपोटामिया में मिले हड़प्पा मुहरों के साक्ष्य पूरी तरह से केवल परिपक्व चरण के हैं।", 0, "लंबी दूरी का व्यापार परिपक्व काल में ही शुरू हुआ था।"),
    ("कथन (A): प्रारंभिक चरण में ईंटों के आकार परिपक्व काल के 1:2:4 अनुपात में मानकीकृत हो चुके थे।\nReason (R): प्रारंभिक चरण में ईंटों के अनुपात अक्सर अनियमित (जैसे 1:2:3) थे और केवल परिपक्व काल में 1:2:4 हुए।", 3, "कथन असत्य है क्योंकि प्रारंभिक ईंटें 1:2:3 थीं। कारण सत्य है।")
]:
    early_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("हाकड़ा मृदभांड चरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह घग्गर-हाकड़ा घाटी में सबसे प्रारंभिक ताम्रपाषाण कृषि समुदायों को दर्शाता है।\n2. भारत में भिरड़ाना और कुणाल जैसे स्थलों पर इसके साक्ष्य मिले हैं।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं।"),
    ("किलेबंदी के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कोट दीजी एकमात्र प्रारंभिक हड़प्पा स्थल है जहाँ सुरक्षात्मक दीवार मिली है।\n2. कालीबंगन-I (प्रारंभिक चरण) में भी किलेबंदी की दीवार मिली है।\nसही कथन चुनें:", 1, "कोट दीजी एकमात्र स्थल नहीं है; कालीबंगन और भिरड़ाना में भी दीवारें थीं।"),
    ("रावी चरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह हड़प्पा स्थल पर खोजा गया सबसे प्रारंभिक स्तर है।\n2. इस चरण के दौरान लंबी लिपियों के साथ पूर्ण विकसित लेखन प्रणाली मौजूद थी।\nसही कथन चुनें:", 0, "केवल छोटे निशान मौजूद थे, लंबी लिपियां नहीं।"),
    ("कृषि प्रथाओं के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कालीबंगन का जुता हुआ खेत प्रारंभिक हड़प्पा चरण का है।\n2. इस समय लोहे के हल के स्थान पर लकड़ी के हलों का उपयोग किया जाता था।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं। लोहा अज्ञात था।"),
    ("प्रारंभिक सामाजिक स्तरीकरण के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. कुणाल से मिले चांदी के मुकुट संभ्रांत वर्ग की उपस्थिति का संकेत देते हैं।\n2. प्रारंभिक हड़प्पा के घर आकार में पूरी तरह समान थे और कोई अंतर नहीं था।\nसही कथन चुनें:", 0, "घरों के आकार में काफी अंतर थे, जो असमानता को दर्शाते हैं।")
]:
    early_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for qtype, q, sol in [
    ("Why", "प्रारंभिक हड़प्पा चरण में सुरक्षात्मक किलेबंदी की दीवारें क्यों बनाई गईं?", "ये दीवारें बाढ़ के पानी से सुरक्षा और पड़ोसी चरवाहा समूहों द्वारा पशुओं की चोरी से बचाव के लिए बनाई गई थीं, जो प्रारंभिक प्रशासनिक व्यवस्था दर्शाती हैं।"),
    ("Why", "आधुनिक इतिहासकारों द्वारा प्रारंभिक हड़प्पा चरण को 'क्षेत्रीयकरण का युग' क्यों कहा जाता है?", "क्योंकि इस समय सामग्री संस्कृति (मृदभांड, आभूषण) पूरे क्षेत्र में एक समान होने के बजाय अलग-अलग स्थानीय शैलियों (कोटदीजियन, सोथी) में बंटी हुई थी।"),
    ("Why", "भिरड़ाना में हाकड़ा मृदभांड की खोज हड़प्पा कालक्रम के लिए क्यों महत्वपूर्ण है?", "यह हड़प्पा सभ्यता की जड़ों को 5वीं सहस्राब्दी ईसा पूर्व तक पीछे ले जाती है, जिससे यह सिद्ध होता है कि यह सभ्यता अचानक उत्पन्न नहीं हुई बल्कि स्थानीय ग्रामीण जड़ों से विकसित हुई थी।"),
    ("How", "प्रारंभिक हड़प्पा के कुम्हारों के निशान परिपक्व हड़प्पा लिपि में कैसे विकसित हुए?", "मिट्टी के बर्तनों पर स्वामित्व या पहचान के लिए बनाए गए शुरुआती निशान धीरे-धीरे मानकीकृत हुए और बाद में वाणिज्यिक लेनदेन के लिए एक पूर्ण विकसित लिपि बन गए।"),
    ("How", "कृषि अधिशेष ने प्रारंभिक से परिपक्व हड़प्पा चरण में संक्रमण को कैसे प्रेरित किया?", "नदियों के subi उपजाऊ मिट्टी के कारण फसलों का भारी अधिशेष हुआ। इसने आबादी के एक हिस्से को खेती से मुक्त कर दिया, जिससे शिल्प, धातु कर्म और व्यापारिक वर्गों का उदय हुआ।"),
    ("How", "प्रारंभिक हड़प्पा की निर्माण तकनीकों ने परिपक्व नगर नियोजन की तैयारी कैसे की?", "उन्होंने मिट्टी की ईंटों के घर, किलेबंदी और सड़कों के शुरुआती संरेखण का विकास किया, जो परिपक्व काल में ग्रिड-आधारित नगर नियोजन में तब्दील हो गए।"),
    ("Case Study", "केस स्टडी: कोट दीजी में विनाश की परत", "कोट दीजी में प्रारंभिक और परिपक्व स्तरों के बीच राख और कोयले की एक मोटी परत मिली है। यह आग से तबाही को दर्शाती है, जिसे युद्ध, आक्रमण या नियोजित परिपक्व शहर के निर्माण के लिए किया गया परित्याग माना जाता है।"),
    ("Case Study", "केस स्टडी: कालीबंगन-I का कृषि पैटर्न", "कालीबंगन का खेत दर्शाता है कि जुताई आड़े-तिरछे पैटर्न (कम दूरी और अधिक दूरी पर) में की गई थी। राजस्थान में आज भी इसी तकनीक का उपयोग सरसों और चने को एक साथ उगाने के लिए किया जाता है।"),
    ("Case Study", "केस स्टडी: कुणाल में सामाजिक स्तरीकरण", "हरियाणा के कुणाल से एक घर के फर्श के नीचे चांदी के दो मुकुट और सोने के आभूषणों से भरा घड़ा मिला है। यह शुरुआती शासक वर्ग या संभ्रांत वर्ग की उपस्थिति का ठोस साक्ष्य है।"),
    ("Teach the Concept", "अवधारणा समझाएं: हड़प्पा का रावी चरण", "समझाएं: (1) हड़प्पा में सबसे पहला रहने वाला स्तर (3300-2800 ईसा पूर्व), (2) ईंट के घरों की शुरुआत, (3) चाक-निर्मित बर्तन, (4) बर्तनों पर लिपि के शुरुआती निशान।"),
    ("Teach the Concept", "अवधारणा समझाएं: क्षेत्रीयकरण युग बनाम एकीकरण युग", "समझाएं कि क्षेत्रीयकरण (प्रारंभिक चरण) में विभिन्न हिस्सों में अलग शैलियां थीं, जबकि एकीकरण (परिपक्व चरण) में पूरे क्षेत्र में मुहर, लिपि, ईंट आकार और बाट पूरी तरह समान हो गए।"),
    ("Teach the Concept", "अवधारणा समझाएं: हाकड़ा मृदभांड और इसका भौगोलिक वितरण", "हाकड़ा मृदभांड घग्गर-हाकड़ा बेसिन की सबसे प्रारंभिक ताम्रपाषाण शैली (हाथ से निर्मित, मिट्टी-लेपित) है। इसका वितरण हरियाणा और चोलिस्तान में है, जो सभ्यता का उद्गम स्थल दर्शाता है।")
]:
    early_mastery_hin.append({"type": qtype, "q": q, "sol": sol})


# ----------------- SECTION 2: MATURE HARAPPAN (HINDI) -----------------
mature_mastery_hin = []

# MCQs (5)
for q, opts, ans, sol in [
    ("परिपक्व हड़प्पा ईंट आयामों का अनुपात (मोटाई : चौड़ाई : लंबाई) क्या था?", ["1 : 2 : 4", "1 : 3 : 9", "2 : 4 : 8", "1 : 2 : 3"], 0, "परिपक्व हड़प्पा चरण में प्रयुक्त ईंटों का मानक अनुपात कड़ाई से 1:2:4 था।"),
    ("निम्नलिखित में से कौन सा परिपक्व हड़प्पा स्थल अपने नगर के विशिष्ट तीन-स्तरीय विभाजन (दो-स्तरीय के बजाय) के लिए प्रसिद्ध है?", ["धोलावीरा", "लोथल", "चन्हुदड़ो", "राखीगढ़ी"], 0, "धोलावीरा तीन भागों (गढ़, मध्यम नगर, निचला नगर) में विभाजित था।"),
    ("किस परिपक्व हड़प्पा स्थल से सुरक्षात्मक किलेबंदी या गढ़ के साक्ष्य नहीं मिले हैं?", ["चन्हुदड़ो", "कालीबंगन", "लोथल", "मोहनजोदड़ो"], 0, "सिंध का चन्हुदड़ो बिना किलेबंदी वाला एकमात्र औद्योगिक केंद्र था।"),
    ("परिपक्व हड़प्पा शहरों और मेसोपोटामिया के बीच व्यापार संबंधों का उल्लेख कीलाक्षर अभिलेखों में मिलता है। सिंधु क्षेत्र को मेसोपोटामिया के रिकॉर्ड में क्या कहा गया है?", ["मेलुहा", "दिलमुन", "मगन", "सुमेर"], 0, "मेसोपोटामिया के अभिलेखों में सिंधु क्षेत्र को 'मेलुहा' कहा गया है।"),
    ("लाजवर्त (Lapis Lazuli) का मुख्य स्रोत क्या था, जिसे परिपक्व हड़प्पावासी आयात करते थे?", ["शॉर्टुघई (अफगानिस्तान)", "खेतड़ी (राजस्थान)", "बदख्शां (ईरान)", "लोथल (गुजरात)"], 0, "शॉर्टुघई लाजवर्त के व्यापार को नियंत्रित करने के लिए स्थापित हड़प्पा चौकी थी।")
]:
    mature_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("परिपक्व हड़प्पा नगर नियोजन की विशेषताएं क्या हैं? (लागू होने वाले सभी विकल्प चुनें)", ["समकोण पर काटने वाली सड़कें (ग्रिड पैटर्न)", "नालियों का भूमिगत ढका हुआ होना", "बस्ती का गढ़ और निचले शहर में विभाजन", "महलों को सहारा देने के लिए बड़े नक्काशीदार पत्थर के खंभे"], [0, 1, 2], "ग्रिड पैटर्न, ढकी नालियां और गढ़/निचले शहर का विभाजन मुख्य विशेषताएं थीं। खंभे नहीं थे।"),
    ("आधुनिक भारत में स्थित प्रमुख परिपक्व हड़प्पा शहर कौन से हैं? (लागू होने वाले सभी विकल्प चुनें)", ["धोलावीरा", "राखीगढ़ी", "लोथल", "हड़प्पा"], [0, 1, 2], "धोलावीरा, राखीगढ़ी और लोथल भारत में हैं। हड़प्पा पाकिस्तान में है।"),
    ("मोहनजोदड़ो से कौन सी पुरातात्विक खोजें संबंधित हैं? (लागू होने वाले सभी विकल्प चुनें)", ["विशाल स्नानागार", "विशाल अन्नागार", "कांस्य की नर्तकी की मूर्ति", "ईंटों का गोदीवाड़ा (dockyard)"], [0, 1, 2], "मोहनजोदड़ो से स्नानागार, अन्नागार और नर्तकी मिली है। गोदीवाड़ा लोथल में है।"),
    ("परिपक्व हड़प्पा व्यापारिक नेटवर्क के मुख्य आयात क्या थे? (लागू होने वाले सभी विकल्प चुनें)", ["बदख्शां से लाजवर्त (Lapis Lazuli)", "खेतड़ी से तांबा", "अफगानिस्तान/ईरान से टिन", "चीन से रेशम"], [0, 1, 2], "लाजवर्त, तांबा और टिन मुख्य आयात थे। रेशम नहीं आयात होता था।"),
    ("परिपक्व हड़प्पा की धार्मिक प्रथाओं से कौन सी विशेषताएं जुड़ी हैं? (लागू होने वाले सभी विकल्प चुनें)", ["मुहरों पर पशुपति/आद्य-शिव का चित्रण", "मातृदेवी की मिट्टी की मूर्तियों की पूजा", "पीपल के पेड़ और कूबड़ वाले सांड की पूजा", "भव्य पत्थर के मंदिरों का निर्माण"], [0, 1, 2], "पशुपति, मातृदेवी और पीपल/सांड की पूजा मुख्य थीं। कोई मंदिर नहीं मिला।")
]:
    mature_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("हड़प्पावासियों ने अपने देवताओं की पूजा के लिए भव्य मंदिरों का निर्माण किया था।", False, "असत्य। हड़प्पा सभ्यता से कोई मंदिर या मूर्तियों वाले देवालय नहीं मिले हैं।"),
    ("हड़प्पा की बाट प्रणाली में छोटे बाटों के लिए 16 का द्विआधारी (binary) आधार था।", True, "सत्य। छोटे बाट 16 के अनुपात में थे (जैसे 1, 2, 4, 8, 16...)"),
    ("राखीगढ़ी को वर्तमान में क्षेत्रफल की दृष्टि से सबसे बड़ा हड़प्पा स्थल माना जाता है।", True, "सत्य। राखीगढ़ी का क्षेत्रफल मोहनजोदड़ो से भी बड़ा आंका गया है।"),
    ("हड़प्पा लिपि को भारतीय पुरातत्वविदों द्वारा पूरी तरह से पढ़ लिया गया है।", False, "असत्य। हड़प्पा लिपि अभी तक अपठित है।"),
    ("लोथल में एक विशाल ईंट की संरचना मिली है जिसे गोदीवाड़ा माना गया है।", True, "सत्य। लोथल से कृत्रिम गोदीवाड़ा मिला है जो भोगवा नदी के माध्यम से खाड़ी से जुड़ा था।"),
    ("हड़प्पावासी अपनी रक्षा के लिए लोहे के हथियारों का उपयोग करते थे।", False, "असत्य। हड़प्पा सभ्यता कांस्य युगीन थी और लोहे से सर्वथा अपरिचित थी।"),
    ("धोलावीरा अपनी विशाल जल संरक्षण प्रणालियों (जलाशयों) के लिए प्रसिद्ध है।", True, "सत्य। धोलावीरा से उत्कृष्ट जल संचयन प्रणालियाँ और बांध मिले हैं।"),
    ("हड़प्पा की मुहरें बनाने में मुख्य रूप से सेलखड़ी (steatite) का उपयोग किया जाता था।", True, "सत्य। अधिकांश मुहरें मुलायम पत्थर सेलखड़ी से बनी हैं।")
]:
    mature_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("परिपक्व हड़प्पा चरण को सिंधु सभ्यता के __________ युग के रूप में भी जाना जाता है।", "एकीकरण", "इसे एकीकरण का युग (Integration Era) कहा जाता है।"),
    ("क्षेत्रफल के हिसाब से सिंधु घाटी सभ्यता का सबसे बड़ा स्थल __________ है।", "राखीगढ़ी", "राखीगढ़ी सबसे बड़ा स्थल है।"),
    ("हड़प्पा सभ्यता का प्रसिद्ध कृत्रिम ईंटों का गोदीवाड़ा __________ से मिला है।", "लोथल", "लोथल से गोदीवाड़ा मिला है।"),
    ("लाजवर्त के आयात के लिए अफगानिस्तान में स्थापित हड़प्पा व्यापारिक चौकी __________ थी।", "शॉर्टुघई", "शॉर्टुघई अफगानिस्तान में स्थित चौकी थी।"),
    ("परिपक्व हड़प्पा काल में ईंटों का अनुपात कड़ाई से __________ था।", "1:2:4", "ईंटों का अनुपात 1:2:4 था।"),
    ("शहर का उठा हुआ पश्चिमी भाग जहाँ प्रशासनिक इमारतें थीं, __________ कहलाता है।", "गढ़", "उठे हुए हिस्से को गढ़ (Citadel) कहते थे।"),
    ("मेसोपोटामिया के रिकॉर्ड में सिंधु घाटी के लिए प्रयुक्त शब्द __________ है।", "मेलुहा", "मेलुहा सिंधु क्षेत्र का नाम था।"),
    ("हड़प्पा की अधिकांश मुहरें एक नरम पत्थर से बनी थीं जिसे __________ कहा जाता है।", "सेलखड़ी", "सेलखड़ी (steatite) मुहरों के लिए प्रयुक्त होता था।")
]:
    mature_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
mature_matching = [
    {
        "type": "Match the Following",
        "q": "परिपक्व हड़प्पा स्थलों को उनकी अनूठी पुरातात्विक संरचनाओं से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा", "key": "A"}, {"left": "II. मोहनजोदड़ो", "key": "B"}, {"left": "III. चन्हुदड़ो", "key": "C"}],
        "options": [{"val": "A", "text": "A. तीन-स्तरीय नगर नियोजन और जल जलाशय"}, {"val": "B", "text": "B. विशाल स्नानागार और विशाल अन्नागार"}, {"val": "C", "text": "C. मनके बनाने का कारखाना और बिना गढ़ का शहर"}],
        "sol": "धोलावीरा में जलाशय, मोहनजोदड़ो में स्नानागार, और चन्हुदड़ो में मनके का कारखाना मिला है।"
    },
    {
        "type": "Match the Following",
        "q": "परिपक्व हड़प्पावासियों के आयात स्रोतों को उनकी वस्तुओं से सुमेलित करें:",
        "items": [{"left": "I. तांबा", "key": "A"}, {"left": "II. लाजवर्त", "key": "B"}, {"left": "III. टिन", "key": "C"}],
        "options": [{"val": "A", "text": "A. खेतड़ी खदानें (राजस्थान)"}, {"val": "B", "text": "B. बदख्शां (अफगानिस्तान)"}, {"val": "C", "text": "C. ईरान / अफगानिस्तान"}],
        "sol": "तांबा खेतड़ी से, लाजवर्त बदख्शां से, and टिन ईरान/अफगानिस्तान से आता था।"
    },
    {
        "type": "Match the Following",
        "q": "हड़प्पा के धार्मिक प्रतीकों को उनके आधुनिक ऐतिहासिक अर्थों से सुमेलित करें:",
        "items": [{"left": "I. पशुपति मुहर", "key": "A"}, {"left": "II. अग्निकुंड", "key": "B"}, {"left": "III. मिट्टी की मूर्तियाँ", "key": "C"}],
        "options": [{"val": "A", "text": "A. आद्य-शिव / पशुओं के देवता"}, {"val": "B", "text": "B. कर्मकांडीय पूजा (लोथल/कालीबंगन में)"}, {"val": "C", "text": "C. मातृदेवी की पूजा"}],
        "sol": "पशुपति आद्य-शिव हैं, अग्निकुंड कर्मकांड दर्शाते हैं, और मूर्तियां मातृदेवी पूजा की प्रतीक हैं।"
    }
]
mature_mastery_hin.extend(mature_matching)

# One-Liner (8)
for q, sol in [
    ("गढ़ (citadel) के बिना एकमात्र परिपक्व हड़प्पा शहर कौन सा था?", "चन्हुदड़ो (सिंध)।"),
    ("किस हड़प्पा स्थल से दस बड़े अक्षरों वाला जिप्सम का 'साइनबोर्ड' मिला है?", "धोलावीरा (गुजरात) से।"),
    ("धोलावीरा से प्राप्त विशाल जलाशयों का मुख्य कार्य क्या था?", "शुष्क क्षेत्र में वर्षा जल का संचयन और संरक्षण।"),
    ("हड़प्पा की मुहरों पर सबसे अधिक किस जानवर का चित्र मिलता है?", "एक-शृंगी पशु (Unicorn)।"),
    ("मोहनजोदड़ो की प्रसिद्ध 'नर्तकी की मूर्ति' किस धातु से बनी है?", "कांस्य (खोया-मोम विधि द्वारा निर्मित)।"),
    ("सिंधु घाटी सभ्यता के स्थलों का सर्वाधिक घनत्व किस नदी बेसिन में है?", "घग्गर-हाकड़ा (प्राचीन सरस्वती नदी) बेसिन में।"),
    ("मेसोपोटामिया के किस शासक ने मेलुहा के साथ व्यापारिक अभिलेख छोड़े हैं?", "अक्कड़ के सारगोन ने।"),
    ("गुजरात में स्थित परिपक्व काल के प्रमुख गोदीवाड़ा (dockyard) पत्तन का नाम क्या है?", "लोथल।")
]:
    mature_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("कथन (A): परिपक्व हड़प्पा शहरों की सड़कें कड़ाई से ग्रिड पैटर्न में व्यवस्थित थीं।\nReason (R): नगर प्रशासन ने मुख्य मार्गों पर किसी भी अतिक्रमण या अनधिकृत निर्माण पर कड़ा प्रतिबंध लगा रखा था।", 0, "दोनों कथन सत्य हैं और कारण सही व्याख्या है। कठोर नियंत्रण योजनाबद्धता दर्शाता है।"),
    ("कथन (A): लोथल मेसोपोटामिया के व्यापार का प्रमुख केंद्र था।\nReason (R): पुरातत्वविदों ने लोथल से एक कृत्रिम ईंट की गोदी और मनके बनाने का कारखाना खोजा है।", 0, "गोदी और कारखाना इसकी व्यापारिक स्थिति की पुष्टि करते हैं।"),
    ("कथन (A): हड़प्पा के लोग विशाल मंदिर बनाकर अपने देवताओं की पूजा नहीं करते थे।\nReason (R): हड़प्पा सभ्यता से किसी भी बड़े मंदिर, वेदियों या बड़ी धार्मिक मूर्तियों के साक्ष्य नहीं मिले हैं।", 0, " temples का अभाव प्राकृतिक पूजा और घरेलू अनुष्ठान की ओर संकेत करता है।"),
    ("कथन (A): हड़प्पा सभ्यता पर एक छत्र पुरोहित-राजा का शासन था जो एक विशाल साम्राज्य चलाता था।\nReason (R): हड़प्पा स्थलों से अस्त्र-शस्त्र, सेना या राजसी कब्रों के साक्ष्य पूरी तरह से अनुपस्थित हैं।", 3, "कथन असत्य है क्योंकि पुरोहित-राजा केवल एक अनुमान है। कारण सत्य है।"),
    ("कथन (A): हड़प्पावासियों ने उत्तरी अफगानिस्तान में शॉर्टुघई में एक व्यापारिक उपनिवेश स्थापित किया था।\nReason (R): शॉर्टुघई ने बदख्शां से लाजवर्त (Lapis Lazuli) के निष्कर्षण और परिवहन पर सीधा प्रशासनिक नियंत्रण प्रदान किया।", 0, "लाजवर्त की प्राप्ति शॉर्टुघई की स्थापना का मुख्य कारण थी।"),
    ("कथन (A): पूरे परिपक्व हड़प्पा क्षेत्र में समान आकार की ईंटों का उपयोग किया जाता था।\nReason (R): 1:2:4 का मानक अनुपात मकानों और विशाल नगर दीवारों को मजबूती प्रदान करता था।", 0, "ईंटों का मानकीकरण (1:2:4) पूरे क्षेत्र में लागू था।"),
    ("कथन (A): हड़प्पा की लिपि एक भावचित्रात्मक (logosyllabic) लिपि थी।\nReason (R): इसमें लगभग 400 से 600 प्रतीक हैं, जो वर्णमाला से अधिक और शुद्ध चित्रों से कम हैं।", 0, "यह शब्दों और शब्दांशों (syllables) को दर्शाने वाली प्रणाली थी।"),
    ("कथन (A): सेलखड़ी की मुहरों का उपयोग स्थानीय बाजारों में मुद्रा के रूप में किया जाता था।\nReason (R): मुहरों का मुख्य उपयोग निर्यात होने वाले माल पर स्वामियों की पहचान और सुरक्षा के लिए गीली मिट्टी पर छाप लगाने के लिए होता था।", 3, "कथन असत्य है क्योंकि मुहरें मुद्रा नहीं थीं। कारण सत्य है।")
]:
    mature_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("गढ़ (Citadel) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह हमेशा शहर के पूर्वी भाग में स्थित होता था और यहाँ घनी आबादी रहती थी।\n2. यहाँ सार्वजनिक इमारतें जैसे विशाल स्नानागार और प्रशासनिक कार्यालय स्थित थे।\nसही कथन चुनें:", 1, "गढ़ पश्चिमी भाग में होता था, न कि पूर्वी भाग में। कथन 2 सत्य है।"),
    ("हड़प्पा की जल निकासी प्रणाली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. नालियां ईंटों या पत्थरों की पट्टियों से ढकी होती थीं जिन्हें सफाई के लिए हटाया जा सकता था।\n2. घरों का गंदा पानी बिना किसी सोख्ता गड्ढे (soak pit) के सीधे सड़कों पर बहता था।\nसही कथन चुनें:", 0, "घरों में पहले कचरा जमा होने का गड्ढा होता था, फिर पानी सड़कों की ढकी नाली में जाता था।"),
    ("बाट प्रणाली के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बाट मुख्य रूप से चर्ट पत्थर से बने चौकोर (cubical) आकार के थे।\n2. उच्च श्रेणी के बाटों के लिए दशमलव प्रणाली का पालन किया जाता था।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं। छोटे बाटों के लिए द्विआधारी और बड़े बाटों के लिए दशमलव व्यवस्था थी।"),
    ("धोलावीरा साइनबोर्ड के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह जिप्सम के दस बड़े अक्षरों से बनी एक लकड़ी की पट्टिका थी।\n2. यह सिंधु लिपि का सबसे लंबा और पढ़ा जा चुका पाठ है।\nसही कथन चुनें:", 0, "यह अभी तक अपठित है, हालांकि यह सबसे लंबा एकल अभिलेख है।"),
    ("पशुपति मुहर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसमें एक देवता योग मुद्रा में बैठे हैं और जानवरों से घिरे हैं।\n2. इन जानवरों में हाथी, बाघ, गैंडा, भैंसा और हिरण शामिल हैं।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं। पशुपति के चारों ओर ये पांचों जानवर मौजूद हैं।")
]:
    mature_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for qtype, q, sol in [
    ("Why", "मिस्र की तुलना में हड़प्पा में विशाल महलों और मंदिरों का पूर्ण अभाव क्यों है?", "क्योंकि हड़प्पा का समाज धार्मिक दिखावे या राजाओं की महिमा के बजाय नागरिक सुविधाओं (नाली, स्वच्छता, अन्न भंडारण, सार्वजनिक स्नानागार) और व्यापार पर केंद्रित था।"),
    ("Why", "हड़प्पावासियों ने उत्तरी अफगानिस्तान में शॉर्टुघई में अपनी व्यापारिक चौकी क्यों स्थापित की?", "ताकि मेसोपोटामिया में अत्यधिक लोकप्रिय लाजवर्त (Lapis Lazuli) के व्यापार और खदानों पर सीधा नियंत्रण स्थापित किया जा सके।"),
    ("Why", "16 का मान ही हड़प्पा बाट प्रणाली का मुख्य आधार क्यों बना?", "क्योंकि यह वजन (13.63 ग्राम) दैनिक आदान-प्रदान और शिल्प वस्तुओं के लेन-देन के लिए सबसे अनुकूल था। भारत की मुद्रा प्रणाली में हाल ही तक इसका प्रभाव (1 रुपया = 16 आना) रहा।"),
    ("How", "हड़प्पा की मुहरों और लिपि ने मेसोपोटामिया के साथ लंबी दूरी के व्यापार को कैसे सुगम बनाया?", "कपड़े में लिपटे माल की गांठ पर गीली मिट्टी लगाकर उस पर मुहर दबाई जाती थी। मुहर की छाप गंतव्य पर यह प्रमाणित करती थी कि माल से छेड़छाड़ नहीं हुई है और निर्यातक की पहचान बताती थी।"),
    ("How", "धोलावीरा ने कच्छ की शुष्क जलवायु में अपने जल संसाधनों का प्रबंधन कैसे किया?", "उन्होंने मनहर और मनसर बरसाती नदियों पर बांध बनाए और पानी को शहर के चारों ओर चट्टान काटकर बनाए गए विशाल जलाशयों में जमा किया।"),
    ("How", "1:2:4 के मानकीकृत ईंट अनुपात ने हड़प्पा शहरों की एकरूपता में कैसे योगदान दिया?", "इसने पूरे 15 लाख वर्ग किमी में निर्माण नियमों को आसान बना दिया। इंग्लिश बॉन्ड (interlocking) चिनाई प्रणाली से दो मंजिला घरों और मजबूत नगर दीवारों का निर्माण संभव हुआ।"),
    ("Case Study", "केस स्टडी: मोहनजोदड़ो का विशाल स्नानागार", "यह 12 मी x 7 मी x 2.4 मी का जलाशय है जिसके किनारों पर ईंटों और डामर (bitumen) का लेप किया गया था ताकि पानी न रिस सके। इसके निकट कुआँ और नालियाँ थीं। इसका उपयोग धार्मिक स्नानों के लिए किया जाता था, जो पवित्रता के धार्मिक महत्व को दर्शाता है।"),
    ("Case Study", "केस स्टडी: कांस्य नर्तकी की मूर्ति का धातु कर्म", "10.5 सेमी की यह मूर्ति खोया-मोम (lost-wax) विधि से बनी है। पहले मोम की मूर्ति बनाई गई, फिर मिट्टी से ढककर गर्म कर मोम बाहर निकाल दिया गया, और खोखले सांचे में कांस्य धातु भरी गई। यह धातु कर्म की उच्च कोटि को दर्शाता है।"),
    ("Case Study", "केस स्टडी: मेसोपोटामिया में मेलुहा का उल्लेख", "उर से प्राप्त कीलाक्षर पट्टियों पर मेलुहा (सिंधु क्षेत्र) से आने वाले हाथीदांत, सोने और मनकों के आयात का उल्लेख है। राजा सारगोन ने दावा किया कि उनके बंदरगाह पर मेलुहा के जहाज खड़े होते थे, जो सीधे समुद्री व्यापार का प्रमाण है।"),
    ("Teach the Concept", "अवधारणा समझाएं: ग्रिड प्रणाली और नागरिक स्वच्छता", "समझाएं: (1) सड़कें समकोण पर काटती थीं, (2) हर गली में ढकी हुई नाली थी, (3) हर घर का पानी नाली से जुड़ा था, (4) नालियों की सफाई के लिए मैनहोल और सोखने वाले गड्ढे थे, जो प्राचीन काल में अद्वितीय थे।"),
    ("Teach the Concept", "अवधारणा समझाएं: हड़प्पा के बाट और माप", "समझाएं: (1) चर्ट पत्थर के चौकोर बाट, (2) हल्के सामान के लिए द्विआधारी प्रणाली (1, 2, 4, 8, 16...), (3) भारी सामान के लिए दशमलव व्यवस्था, (4) ईंटों का सर्वव्यापी अनुपात 1:2:4।"),
    ("Teach the Concept", "अवधारणा समझाएं: पशुपति और मातृदेवी की पूजा", "समझाएं: (1) पशुपति मुहर पर योग मुद्रा में बैठे तीन सींग वाले देवता जो जानवरों से घिरे हैं, (2) मिट्टी की मातृदेवी की मूर्तियां जो उर्वरता का प्रतीक हैं, (3) पीपल, सांड और जल जैसे प्राकृतिक प्रतीकों की पूजा।")
]:
    mature_mastery_hin.append({"type": qtype, "q": q, "sol": sol})


# ----------------- SECTION 3: LATE HARAPPAN (HINDI) -----------------
late_mastery_hin = []

# MCQs (5)
for q, opts, ans, sol in [
    ("सिंध में उत्तर हड़प्पा चरण को पुरातात्विक रूप से किस स्थानीय संस्कृति द्वारा दर्शाया गया है?", ["झुकर संस्कृति", "सिमेट्री एच संस्कृति", "मालवा संस्कृति", "आहार-बनास संस्कृति"], 0, "सिंध में झुकर संस्कृति उत्तर-शहरी, उत्तर हड़प्पा संस्कृति का प्रतिनिधित्व करती है।"),
    ("उत्तर हड़प्पा चरण का कौन सा स्थल पश्चिमी उत्तर प्रदेश में स्थित है, जो सभ्यता की सबसे पूर्वी सीमा बनाता है?", ["आलमगीरपुर", "दैमाबाद", "मांडा", "सुतकागेंडोर"], 0, "मेरठ जिला (उत्तर प्रदेश) का आलमगीरपुर सबसे पूर्वी स्थल है, जो हिंडन नदी के तट पर है।"),
    ("हरियाणा के किस स्थल पर पुरातत्वविदों ने उत्तर हड़प्पा और चित्रित धूसर मृदभांड (PGW) संस्कृतियों के मेल (overlap) वाले ढांचे खोजे हैं?", ["भगवानपुरा", "राखीगढ़ी", "बनावली", "कुणाल"], 0, "हरियाणा का भगवानपुरा उत्तर हड़प्पा और चित्रित धूसर मृदभांड (वैदिक काल) के शांतिपूर्ण सह-अस्तित्व को दर्शाता है।"),
    ("गुजरात का कौन सा उत्तर हड़प्पा स्थल चमकीले लाल मृदभांड (LRW) के लिए प्रसिद्ध है लेकिन वहाँ परिपक्व चरण के साक्ष्य नहीं मिले हैं?", ["रंगपुर", "लोथल", "धोलावीरा", "सुरकोटदा"], 0, "रंगपुर गुजरात में उत्तर-शहरी चमकीले लाल मृदभांड संस्कृति का प्रकार-स्थल है, जहाँ परिपक्व चरण नहीं मिला है।"),
    ("उत्तर हड़प्पा चरण का सबसे दक्षिणी स्थल दैमाबाद (महाराष्ट्र), जहाँ से कांस्य मूर्तियां मिली हैं, किस नदी के किनारे स्थित है?", ["प्रवरा नदी", "नर्मदा नदी", "ताप्ती नदी", "गोदावरी नदी"], 0, "दैमाबाद गोदावरी की सहायक नदी प्रवरा के तट पर अहमदनगर जिले में स्थित है।")
]:
    late_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct (5)
for q, opts, ans, sol in [
    ("परिपक्व से उत्तर हड़प्पा चरण के संक्रमण के दौरान कौन से बड़े बदलाव हुए? (लागू होने वाले सभी विकल्प चुनें)", ["लिपि और सेलखड़ी की मुहरों का गायब होना", "मानकीकृत बाटों और मापों का उपयोग बंद होना", "सार्वजनिक जल निकासी और नाली व्यवस्था का पतन", "लोहे के उपकरणों का बड़े पैमाने पर विकास"], [0, 1, 2], "संक्रमण के दौरान लिपि, बाट और नालियों का पतन हो गया। लोहा इस काल में नहीं आया था।"),
    ("उत्तर हड़प्पा काल की प्रमुख क्षेत्रीय संस्कृतियों की पहचान करें: (लागू होने वाले सभी विकल्प चुनें)", ["सिंध में झुकर संस्कृति", "पंजाब में सिमेट्री एच संस्कृति", "गुजरात में चमकीले लाल मृदभांड संस्कृति", "मध्य प्रदेश में मालवा संस्कृति"], [0, 1, 2], "झुकर, सिमेट्री एच और चमकीले लाल मृदभांड उत्तर हड़प्पा की क्षेत्रीय शैलियां हैं। मालवा अलग संस्कृति है।"),
    ("कौन से उत्तर हड़प्पा स्थल सभ्यता के बाहरी प्रसार को दर्शाते हैं? (लागू होने वाले सभी विकल्प चुनें)", ["दैमाबाद (महाराष्ट्र)", "आलमगीरपुर (उत्तर प्रदेश)", "हुलास (उत्तर प्रदेश)", "सुतकागेंडोर (बलूचिस्तान)"], [0, 1, 2], "दैमाबाद, आलमगीरपुर और हुलास उत्तर चरण के बाहरी प्रसार हैं। सुतकागेंडोर परिपक्व काल का पश्चिमी बंदरगाह था।"),
    ("सिमेट्री एच (Cemetery H) संस्कृति के संबंध में सही कथन चुनें: (लागू होने वाले सभी विकल्प चुनें)", ["यह पंजाब (हड़प्पा) में उत्तर-शहरी चरण का प्रतिनिधित्व करती है", "यहाँ चित्रित बर्तनों में पक्षियों और ज्यामितीय डिजाइनों वाले कलश शवाधान मिले हैं", "इसमें लेखन और बाट प्रणाली का पूरी तरह अभाव था", "इसने भारत में घोड़े वाले रथों की शुरुआत की"], [0, 1, 2], "सिमेट्री एच पंजाब का उत्तर चरण है जिसमें कलश शवाधान मिले हैं और लेखन का अभाव था। रथ नहीं थे।"),
    ("आधुनिक इतिहासकार परिपक्व हड़प्पा सभ्यता के पतन के लिए किन कारणों को जिम्मेदार मानते हैं? (लागू होने वाले सभी विकल्प चुनें)", ["जलवायु परिवर्तन और मानसूनी बारिश में कमी", "भूकंपीय गतिविधियों के कारण नदियों के मार्ग में बदलाव", "घग्गर-हाकड़ा नदी प्रणाली का सूखना", "आर्यों का हिंसक आक्रमण"], [0, 1, 2], "जलवायु परिवर्तन, नदी मार्ग परिवर्तन और नदी का सूखना मुख्य कारण थे। आर्य आक्रमण का सिद्धांत खारिज हो चुका है।")
]:
    late_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("उत्तर हड़प्पा चरण सिंधु घाटी की आबादी की अचानक और पूर्ण विलुप्ति का प्रतिनिधित्व करता है।", False, "Region। यह वि-शहरीकरण और ग्रामीणकरण का दौर था, जिसमें लोग पूर्व और दक्षिण की ओर चले गए।"),
    ("महाराष्ट्र के दैमाबाद से धातु शिल्प के उत्कृष्ट साक्ष्य के रूप में चार कांस्य मूर्तियां मिली हैं।", True, "सत्य। दैमाबाद कांस्य मूर्तियों में रथ हांकता मनुष्य, सांड, गेंडा और हाथी शामिल हैं।"),
    ("हरियाणा के भगवानपुरा से उत्तर हड़प्पा और चित्रित धूसर मृदभांड (PGW) संस्कृतियों का मेल (overlap) मिला है।", True, "सत्य। यहाँ दोनों संस्कृतियों के सह-अस्तित्व के स्पष्ट स्तर मिले हैं।"),
    ("उत्तर हड़प्पा चरण के दौरान लोहे के हथियारों का व्यापक रूप से उपयोग किया जाता था।", False, "असत्य। उत्तर हड़प्पा चरण पूरी तरह से लौह-पूर्व (ताम्रपाषाण) था।"),
    ("उत्तर हड़प्पा काल के मकान पुरानी ईंटों के उपयोग से बेतरतीब ढंग से सड़कों के ऊपर बने पाए गए हैं।", True, "सत्य। नागरिक प्रशासन के पतन के कारण निर्माण बेतरतीब हो गए थे।"),
    ("उत्तर हड़प्पा काल में मेसोपोटामिया के साथ समुद्री व्यापार अपने चरम पर था।", False, "असत्य। इस काल में मेसोपोटामिया के साथ प्रत्यक्ष विदेशी व्यापार पूरी तरह ठप हो गया था।"),
    ("गुजरात का रंगपुर चमकीले लाल मृदभांड (LRW) संस्कृति का प्रमुख स्थल है।", True, "सत्य। रंगपुर गुजरात में उत्तर हड़प्पा का सबसे महत्वपूर्ण स्थल है।"),
    ("सिमेट्री एच चरण के दौरान भी सेलखड़ी की मुहरों और लिपि का उपयोग जारी रहा।", False, "असत्य। उत्तर-शहरी पतन के साथ लिपि और मुहरों का उपयोग बंद हो गया था।")
]:
    late_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("उत्तर हड़प्पा चरण को सिंधु सभ्यता के __________ युग के रूप में भी जाना जाता है।", "स्थानीयकरण", "इसे स्थानीयकरण का युग (Localisation Era) कहा जाता है।"),
    ("सिंध में उत्तर-शहरी चरण की स्थानीय संस्कृति को __________ संस्कृति कहा जाता है।", "झुकर", "सिंध में झुकर संस्कृति उत्तर हड़प्पा का प्रतिनिधित्व करती है।"),
    ("उत्तर हड़प्पा चरण का सबसे पूर्वी स्थल उत्तर प्रदेश में __________ है।", "आलमगीरपुर", "आलमगीरपुर सबसे पूर्वी सीमा है।"),
    ("उत्तर हड़प्पा और चित्रित धूसर मृदभांड (PGW) संस्कृतियों का मेल हरियाणा के __________ स्थल से मिला है।", "भगवानपुरा", "भगवानपुरा में दोनों संस्कृतियों का मेल मिला है।"),
    ("प्रवरा नदी के तट पर स्थित सबसे दक्षिणी उत्तर हड़प्पा बस्ती __________ है।", "दैमाबाद", "दैमाबाद सबसे दक्षिणी बस्ती थी।"),
    ("गुजरात में उत्तर हड़प्पा चरण को दर्शाने वाली मृदभांड शैली __________ लाल मृदभांड है।", "चमकीले", "चमकीले लाल मृदभांड (Lustrous Red Ware) गुजरात की विशेषता हैं।"),
    ("पतन के बाद सिंधु बेसिन की आबादी मुख्य रूप से __________ घाटी की ओर चली गई।", "गंगा", "आबादी पूर्व की ओर गंगा-यमुना दोआब की ओर स्थानांतरित हुई।"),
    ("हड़प्पा में खोजे गए उत्तर-शहरी शवाधान स्थल को __________ कहा जाता है।", "सिमेट्री एच", "हड़प्पा में सिमेट्री एच (Cemetery H) उत्तर चरण को दर्शाता है।")
]:
    late_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matching (3)
late_matching = [
    {
        "type": "Match the Following",
        "q": "उत्तर हड़प्पा की क्षेत्रीय संस्कृतियों को उनके भौगोलिक क्षेत्रों से सुमेलित करें:",
        "items": [{"left": "I. झुकर संस्कृति", "key": "A"}, {"left": "II. सिमेट्री एच संस्कृति", "key": "B"}, {"left": "III. चमकीले लाल मृदभांड", "key": "C"}],
        "options": [{"val": "A", "text": "A. सिंध (पाकिस्तान)"}, {"val": "B", "text": "B. पंजाब (हड़प्पा)"}, {"val": "C", "text": "C. गुजरात (रंगपुर/रोजड़ी)"}],
        "sol": "झुकर सिंध में, सिमेट्री एच पंजाब में, और चमकीले लाल मृदभांड गुजरात में विकसित हुए।"
    },
    {
        "type": "Match the Following",
        "q": "उत्तर हड़प्पा की सीमाओं को उनके भौगोलिक स्थानों से सुमेलित करें:",
        "items": [{"left": "I. आलमगीरपुर", "key": "A"}, {"left": "II. दैमाबाद", "key": "B"}, {"left": "III. मांडा", "key": "C"}],
        "options": [{"val": "A", "text": "A. पूर्वी सीमा (उत्तर प्रदेश)"}, {"val": "B", "text": "B. दक्षिणी सीमा (महाराष्ट्र)"}, {"val": "C", "text": "C. उत्तरी सीमा (जम्मू और कश्मीर)"}],
        "sol": "आलमगीरपुर पूर्व में, दैमाबाद दक्षिण में, और मांडा उत्तर में सीमा बनाते थे।"
    },
    {
        "type": "Match the Following",
        "q": "हड़प्पा पतन के सिद्धांतों को उनके प्रतिपादक इतिहासकारों से सुमेलित करें:",
        "items": [{"left": "I. आर्य आक्रमण सिद्धांत", "key": "A"}, {"left": "II. विवर्तनिक (Tectonic) बाढ़ सिद्धांत", "key": "B"}, {"left": "III. घग्गर नदी का सूखना सिद्धांत", "key": "C"}],
        "options": [{"val": "A", "text": "A. मोर्टिमर व्हीलर"}, {"val": "B", "text": "B. रॉबर्ट एल. रायक्स"}, {"val": "C", "text": "C. डी.पी. अग्रवाल / एम.आर. मुगल"}],
        "sol": "व्हीलर ने आर्य आक्रमण, रायक्स ने बाढ़, और अग्रवाल ने घग्गर नदी के सूखने का सिद्धांत दिया।"
    }
]
late_mastery_hin.extend(late_matching)

# One-Liner (8)
for q, sol in [
    ("हिंडन नदी के तट पर स्थित उत्तर हड़प्पा काल की सबसे पूर्वी बस्ती का नाम बताएं।", "आलमगीरपुर (मेरठ, उत्तर प्रदेश)।"),
    ("किस स्थल पर उत्तर हड़प्पा और चित्रित धूसर मृदभांड (वैदिक काल) के स्तरों का मेल मिला है?", "भगवानपुरा (हरियाणा) में।"),
    ("महाराष्ट्र के अहमदनगर जिले में स्थित सबसे दक्षिणी उत्तर हड़प्पा स्थल का नाम क्या है?", "दैमाबाद।"),
    ("गुजरात में उत्तर-शहरी चरण के विशिष्ट मृदभांड का नाम क्या है?", "चमकीले लाल मृदभांड (Lustrous Red Ware)।"),
    ("उत्तर हड़प्पा के औजारों में किस धातु का पूर्ण अभाव था?", "लोहा (वे केवल तांबे और कांस्य का उपयोग करते थे)।"),
    ("पतन के समय हड़प्पा आबादी के प्रवास की मुख्य दिशा क्या थी?", "पूर्व की ओर (गंगा घाटी) और दक्षिण की ओर (गुजरात)।"),
    ("सिंध में चन्हुदड़ो के निकट खोजी गई उत्तर-शहरी संस्कृति का नाम क्या है?", "झुकर संस्कृति।"),
    ("उत्तर प्रदेश के किस स्थल से नाली व्यवस्था के अभाव वाली उत्तर हड़प्पा बस्ती मिली है?", "हुलास।")
]:
    late_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("कथन (A): उत्तर हड़प्पा चरण वि-शहरीकरण और नागरिक पतन को दर्शाता है।\nReason (R): इस काल में मानकीकृत मुहरें, बाट और ग्रिड नगर नियोजन पूरी तरह गायब हो गए तथा छोटे ग्रामीण कृषि गांवों का उदय हुआ।", 0, "दोनों कथन सत्य हैं और कारण सही व्याख्या है। नागरिक मानकों की समाप्ति ही वि-शहरीकरण है।"),
    ("कथन (A): दैमाबाद को उत्तर हड़प्पा के प्रसार की सबसे दक्षिणी सीमा माना जाता है।\nReason (R): पुरातत्वविदों ने प्रवरा नदी के तट पर स्थित दैमाबाद से कांस्य के रथ, गेंडे और हाथी की मूर्तियाँ प्राप्त की हैं।", 0, "दैमाबाद की मूर्तियां इसकी धातु कला और दक्षिणी सीमा की पुष्टि करती हैं।"),
    ("कथन (A): सिमेट्री एच संस्कृति चित्रित धूसर मृदभांड (PGW) के साथ मेल खाती है।\nReason (R): सिमेट्री एच हड़प्पा में उत्तर-शहरी चरण को दर्शाता है, जबकि PGW के साथ मेल का साक्ष्य हरियाणा के भगवानपुरा से मिला है।", 1, "दोनों कथन सत्य हैं लेकिन कारण सही व्याख्या नहीं है।"),
    ("कथन (A): उत्तर हड़प्पा काल में आबादी सिंधु क्षेत्र से पलायन कर गई।\nReason (R): मानसून के कमजोर होने और नदियों के मार्ग बदलने से घग्गर-हाकड़ा जैसी नदियां सूख गईं, जिससे कृषि असंभव हो गई।", 0, "नदियों का सूखना और शुष्कता ही पलायन का मुख्य कारण था।"),
    ("कथन (A): उत्तर हड़प्पा के लोगों ने अपने घरों को मजबूत बनाने के लिए नक्काशीदार पत्थर के खंभों का उपयोग किया।\nReason (R): नागरिक नियमों के पतन के कारण लोग पुरानी सड़कों के ऊपर बेतरतीब ढंग से पुरानी ईंटों के मकान बनाने लगे थे।", 3, "कथन असत्य है क्योंकि खंभों का उपयोग नहीं किया गया था। कारण सत्य है।"),
    ("कथन (A): उत्तर हड़प्पा काल में मेसोपोटामिया के साथ सीधा व्यापार ठप हो गया।\nReason (R): मेसोपोटामिया की 2000 ईसा पूर्व के बाद की पट्टिकाओं पर मेलुहा से आने वाले आयातों का कोई उल्लेख नहीं मिलता है।", 0, "मेसोपोटामिया के रिकॉर्ड सीधे व्यापार पतन की पुष्टि करते हैं।"),
    ("कथन (A): गेरुए रंग के मृदभांड (OCP) संस्कृति गंगा घाटी में उत्तर हड़प्पा के समकालीन थी।\nReason (R): OCP समुदाय तांबे के भंडारों (copper hoards) से जुड़े थे और उनके बस्तियों के स्तर उत्तर हड़प्पा के साथ मेल खाते हैं।", 0, "OCP और उत्तर हड़प्पा के लोगों के बीच संपर्क के प्रमाण मिले हैं।"),
    ("कथन (A): आर्यों का आक्रमण आज भी हड़प्पा सभ्यता के पतन का सबसे स्वीकृत कारण माना जाता है।\nReason (R): मोहनजोदड़ो से मिले नरकंकालों पर हथियारों से हमले, आगजनी या सामूहिक नरसंहार के कोई साक्ष्य नहीं मिले हैं।", 3, "कथन असत्य है क्योंकि आर्य आक्रमण सिद्धांत पूरी तरह खारिज हो चुका है। कारण सत्य है।")
]:
    late_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("उत्तर हड़प्पा मृदभांडों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें परिपक्व हड़प्पा काल के बर्तनों पर मिलने वाले जटिल चित्रों का अभाव है।\n2. गुजरात में स्थानीय रूप से चमकीले लाल मृदभांड (LRW) शैली का विकास हुआ।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं। चित्रकारी साधारण हो गई और LRW शैली गुजरात की विशेषता बनी।"),
    ("बस्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्तर प्रदेश का आलमगीरपुर उत्तर हड़प्पा चरण की सबसे पूर्वी बस्ती है।\n2. महाराष्ट्र का दैमाबाद सबसे उत्तरी बस्ती है।\nसही कथन चुनें:", 0, "दैमाबाद सबसे दक्षिणी बस्ती है, उत्तरी नहीं। कथन 1 सत्य है।"),
    ("संक्रमण काल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. हरियाणा के भगवानपुरा से उत्तर हड़प्पा और चित्रित धूसर मृदभांड (PGW) का स्तरिक मेल मिला है।\n2. इस मेल वाले स्तर से कांस्य के साथ लोहे के औजार भी भारी मात्रा में मिले हैं।\nसही कथन चुनें:", 0, "यहाँ भी लोहा अनुपस्थित है, जो दर्शाता है कि उत्तर हड़प्पावासी लौह-पूर्व थे।"),
    ("झुकर संस्कृति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह सिंध में उत्तर-शहरी उत्तर हड़प्पा संस्कृति का प्रतिनिधित्व करती है।\n2. सेलखड़ी की मुहरों के स्थान पर यहाँ गोल ज्यामितीय बटन मुहरें मिली हैं।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं।"),
    ("पतन के सिद्धांतों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मोर्टिमर व्हीलर ने मोहनजोदड़ो के नरकंकालों के आधार पर आर्य आक्रमण का सिद्धांत दिया था।\n2. आधुनिक डीएनए अध्ययनों (जैसे राखीगढ़ी) से पतन के काल में किसी बाहरी आनुवंशिक आक्रमण के साक्ष्य नहीं मिले हैं।\nसही कथन चुनें:", 2, "दोनों कथन सही हैं।")
]:
    late_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for qtype, q, sol in [
    ("Why", "उत्तर हड़प्पा काल में लोगों ने व्यवस्थित ग्रिड योजना और नालियों का निर्माण क्यों बंद कर दिया?", "नगर निकायों के प्रशासनिक पतन और व्यापारिक अधिशेष के समाप्त होने के कारण सार्वजनिक नालियों और सड़कों की सफाई संभव नहीं रही। लोग बेतरतीब घर बनाने लगे।"),
    ("Why", "1900 ईसा पूर्व के बाद मेसोपोटामिया के साथ व्यापारिक पतन क्यों हुआ?", "नदियों के सूखने और प्रशासनिक ह्रास के कारण निर्यात योग्य अधिशेष (मनके, सोना) एकत्र कर भेजना संभव नहीं रहा। मेसोपोटामिया का ध्यान भी आंतरिक व्यापार पर केंद्रित हो गया।"),
    ("Why", "उत्तर हड़प्पा चरण को 'स्थानीयकरण का युग' क्यों कहा जाता है?", "क्योंकि परिपक्व काल की एकीकृत सामग्री संस्कृति बिखर गई और इसके स्थान पर झुकर, सिमेट्री एच जैसी भिन्न-भिन्न स्थानीय संस्कृतियाँ उदित हुईं।"),
    ("How", "घग्गर-हाकड़ा नदी तंत्र में विवर्तनिक (tectonic) बदलावों ने पतन में कैसे योगदान दिया?", "विवर्तनिक हलचलों के कारण सतलज नदी सिंधु की ओर और यमुना नदी गंगा की ओर मुड़ गई, जिससे घग्गर-हाकड़ा सूखी नदी बन गई और बस्तियों का विनाश हुआ।"),
    ("How", "उत्तर हड़प्पा धातु कर्म परिपक्व काल के धातु कर्म से किस प्रकार भिन्न था?", "खोया-मोम जैसी जटिल कलात्मक ढलाई कम हो गई और मुख्य ध्यान भारी तांबे के औजारों (जैसे दैमाबाद कांस्य) पर केंद्रित हुआ। टिन की कमी हो गई पर वे लौह-पूर्व ही रहे।"),
    ("How", "शहरों से ग्रामीण बस्तियों में बदलाव ने हड़प्पा के सामाजिक ढांचे को कैसे प्रभावित किया?", "लिपि, मुहर और अनाज भंडारों के नष्ट होने से शासक और व्यापारी वर्ग का अंत हो गया, और समाज स्थानीय स्तर पर छोटे किसानों और कबीलों में बंट गया।"),
    ("Case Study", "केस स्टडी: दैमाबाद की कांस्य मूर्तियाँ", "दैमाबाद से 60 किलो ठोस तांबे की मूर्तियां मिली हैं (रथ, बैल, गेंडा, हाथी)। यह दर्शाता है कि नागरिक पतन के बावजूद दूरदराज के क्षेत्रों में भारी धातु ढलाई और ढलाई कौशल अभी भी जीवित थे।"),
    ("Case Study", "केस स्टडी: भगवानपुरा में ओवरलैप (Overlap)", "स्तरिकी से पता चलता है कि उत्तर हड़प्पा और चित्रित धूसर मृदभांड (PGW) के लोग शांतिपूर्वक एक साथ रहते थे, जो दर्शाता है कि हड़प्पा और वैदिक काल के बीच हिंसक संघर्ष नहीं हुआ था।"),
    ("Case Study", "केस स्टडी: झुकर की बटन मुहरें", "सिंध में लिपि वाली चौकोर सेलखड़ी मुहरें बंद हो गईं और मध्य एशिया जैसी गोल ज्यामितीय बटन मुहरें उभरीं। यह दर्शाता है कि आधिकारिक प्रशासन समाप्त हो गया था और अनौपचारिक व्यापारिक प्रतीक उभरे थे।"),
    ("Teach the Concept", "अवधारणा समझाएं: वि-शहरीकरण बनाम पूर्ण विनाश", "समझाएं कि हड़प्पा सभ्यता पूरी तरह समाप्त नहीं हुई थी; शहरों का पतन हुआ पर लोग सुरक्षित पूर्वी (गंगा) और दक्षिणी (गुजरात) कृषि क्षेत्रों में चले गए, जिससे आनुवंशिक और सांस्कृतिक निरंतरता बनी रही।"),
    ("Teach the Concept", "अवधारणा समझाएं: उत्तर हड़प्पा की क्षेत्रीय संस्कृतियाँ", "समझाएं: (1) झुकर संस्कृति (सिंध) बटन मुहरों के साथ, (2) सिमेट्री एच (पंजाब) कलश समाधान के साथ, और (3) चमकीले लाल मृदभांड (गुजरात) लाल बर्तनों के साथ।"),
    ("Teach the Concept", "अवधारणा समझाएं: हड़प्पा और वैदिक संस्कृतियों का संक्रमण", "समझाएं कि यह संक्रमण शांतिपूर्ण था; भगवानपुरा जैसे स्थल दिखाते हैं कि उत्तर हड़प्पावासी और वैदिक काल के मृदभांड उपयोगकर्ता एक ही बस्ती में साथ रहते थे, जिससे संस्कृतियों का समन्वय हुआ।")
]:
    late_mastery_hin.append({"type": qtype, "q": q, "sol": sol})


# ----------------- INJECT AND WRITE ENGLISH & HINDI -----------------
# Inject English
with open(ENG_PATH, "r", encoding="utf-8") as f:
    eng_data = json.load(f)

eng_data["deepDive"]["sections"][0]["masteryZone"] = early_mastery_eng
eng_data["deepDive"]["sections"][1]["masteryZone"] = mature_mastery_eng
eng_data["deepDive"]["sections"][2]["masteryZone"] = late_mastery_eng

with open(ENG_PATH, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

print("English content updated successfully with 186 questions!")

# Inject Hindi
with open(HIN_PATH, "r", encoding="utf-8") as f:
    hin_data = json.load(f)

hin_data["deepDive"]["sections"][0]["masteryZone"] = early_mastery_hin
hin_data["deepDive"]["sections"][1]["masteryZone"] = mature_mastery_hin
hin_data["deepDive"]["sections"][2]["masteryZone"] = late_mastery_hin

with open(HIN_PATH, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Hindi content updated successfully with 186 questions!")
print(f"Lengths verified: {len(early_mastery_eng)} | {len(mature_mastery_eng)} | {len(late_mastery_eng)}")

