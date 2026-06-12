import os
import json

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Portuguese-Vasco-Da-Gama\questions_data"
os.makedirs(BASE_DIR, exist_ok=True)

# Helper lists
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

def generate_sec_file(name, list_en, list_hi):
    path = os.path.join(BASE_DIR, f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Programmatically generated Vasco da Gama Qs\n\n")
        f.write(f"{name}_en = {repr(list_en)}\n\n")
        f.write(f"{name}_hi = {repr(list_hi)}\n")


# ==================== SECTION 1: FIRST VOYAGE ====================
sec1_en = [
    # MCQs
    {
        "type": "MCQ",
        "q": "Which ship served as Vasco da Gama's flagship during his historic first voyage to India in 1497-1499 CE?",
        "opts": ["São Gabriel", "São Rafael", "Bérrio", "São Miguel"],
        "ans": 0,
        "sol": "The São Gabriel was the flagship, commanded by Vasco da Gama himself. His brother Paulo commanded the São Rafael."
    },
    {
        "type": "MCQ",
        "q": "Who was the legendary pilot who guided Vasco da Gama's fleet from Malindi across the Arabian Sea to Calicut?",
        "opts": ["Ahmad Ibn Mājid", "Al-Masudi", "Ibn Battuta", "Al-Idrisi"],
        "ans": 0,
        "sol": "Ahmad Ibn Mājid (often identified as a Gujarati or Arab navigator) guided the fleet using his expertise of monsoon winds."
    },
    {
        "type": "MCQ",
        "q": "Which Portuguese monarch sponsored and commissioned Vasco da Gama's first voyage to find a direct sea route to India?",
        "opts": ["King Manuel I", "King John II", "Prince Henry the Navigator", "King Afonso V"],
        "ans": 0,
        "sol": "King Manuel I ('The Fortunate') sponsored the voyage. King John II had made initial plans but died before execution."
    },
    {
        "type": "MCQ",
        "q": "Where exactly did Vasco da Gama first set foot on Indian soil in May 1498 CE?",
        "opts": ["Kappad near Calicut", "Cochin beach", "Anjadip Island", "Dona Paula beach, Goa"],
        "ans": 0,
        "sol": "Vasco da Gama landed at Kappad beach, located about 15 km north of Calicut (Kozhikode)."
    },
    {
        "type": "MCQ",
        "q": "What major disaster befell Vasco da Gama's fleet on the return journey from India to Portugal?",
        "opts": ["Destruction of São Rafael due to crew loss from scurvy", "Total loss of spice cargo in a storm near Madagascar", "Capture of the flagship by Arab pirates off Mombasa", "Mutiny by Nicolau Coelho"],
        "ans": 0,
        "sol": "Scurvy decimated the crew on the return leg, forcing Gama to burn the São Rafael near East Africa due to a lack of sailors."
    },
    # Multi Correct
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following ships were part of Vasco da Gama's original four-vessel fleet that left Lisbon in 1497? (Select all that apply)",
        "opts": ["São Gabriel", "São Rafael", "Bérrio", "São Salvador"],
        "ans": [0, 1, 2],
        "sol": "The fleet comprised São Gabriel (flagship), São Rafael, Bérrio, and an unnamed storage ship."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which East African coastal settlements did Vasco da Gama visit before crossing the Indian Ocean? (Select all that apply)",
        "opts": ["Mozambique", "Mombasa", "Malindi", "Zanzibar"],
        "ans": [0, 1, 2],
        "sol": "Vasco da Gama visited Mozambique, Mombasa (where he faced hostility), and Malindi (where he was warmly received)."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What were the main commercial objectives of Vasco da Gama's first expedition? (Select all that apply)",
        "opts": ["Securing direct access to the spice trade", "Bypassing Ottoman and Venetian middlemen", "Establishing direct royal diplomacy in India", "Immediate territorial acquisition of Goa"],
        "ans": [0, 1, 2],
        "sol": "The first voyage sought trade and routes, not territorial conquests, which occurred later under Albuquerque."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which factors contributed to the high mortality rate among the crew of the first voyage? (Select all that apply)",
        "opts": ["Outbreak of scurvy during the long crossings", "Lack of fresh water and proper provisions", "Hostile skirmishes along the East African coast", "Malaria outbreak in the Cape Verde islands"],
        "ans": [0, 1, 2],
        "sol": "Scurvy, dietary deficiency, and hostile clashes killed nearly half of the original 170 crew members."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the cargo Vasco da Gama successfully brought back to Lisbon in 1499. (Select all that apply)",
        "opts": ["Pepper and cinnamon", "Ginger and cloves", "Precious stones and porcelain", "Heavy quantities of Indian cotton textiles"],
        "ans": [0, 1, 2],
        "sol": "He brought back spices (pepper, cinnamon, cloves, ginger) and fine Asian goods like porcelain and gems."
    },
    # True/False
    {"type": "True/False", "q": "True or False: Ahmad Ibn Mājid was a Portuguese officer who plotted the route using advanced European charts.", "ans": False, "sol": "He was a local Indian Ocean pilot (Gujarati/Arab) who possessed traditional navigation knowledge."},
    {"type": "True/False", "q": "True or False: Vasco da Gama was named Viceroy of India immediately upon his return in 1499.", "ans": False, "sol": "He was given titles like 'Admiral of the Seas of Arabia' but only became Viceroy in 1524."},
    {"type": "True/False", "q": "True or False: The first voyage sailed through the Mediterranean Sea and Suez Canal to reach India.", "ans": False, "sol": "The Suez Canal did not exist; they sailed around the Cape of Good Hope."},
    {"type": "True/False", "q": "True or False: The spice cargo returned by Gama was sold for roughly 60 times the cost of the entire expedition.", "ans": True, "sol": "Despite losing two ships and half the crew, the spice cargo proved immensely profitable."},
    {"type": "True/False", "q": "True or False: The São Rafael flagship returned safely to Lisbon port.", "ans": False, "sol": "São Rafael was burned because there were not enough surviving crew members to sail it."},
    {"type": "True/False", "q": "True or False: The entire outbound and inbound journey took less than 12 months to complete.", "ans": False, "sol": "It took more than two years, departing in July 1497 and returning in August 1499."},
    {"type": "True/False", "q": "True or False: King Manuel I was known as 'The Fortunate' due to the wealth brought by the direct route.", "ans": True, "sol": "The opening of the route brought tremendous wealth and prestige to his reign."},
    {"type": "True/False", "q": "True or False: Vasco da Gama was killed by the Zamorin's forces during his first voyage.", "ans": False, "sol": "He returned safely to Lisbon and died decades later in Cochin during his third voyage."}
]

# Fill Blanks
for idx, qtext in enumerate([
    "The name of the beach near Calicut where Vasco da Gama landed in 1498 was __________.",
    "The Portuguese fleet departed from the port of __________ in July 1497.",
    "Vasco da Gama's brother, __________ da Gama, commanded the São Rafael.",
    "The sea route discovered by rounding the southern tip of Africa is known as the __________ Route.",
    "The southern tip of Africa rounded by the fleet was named the Cape of __________.",
    "Vasco da Gama was assisted by a navigator from the East African city of __________.",
    "The deficiency disease __________ killed a large portion of the Portuguese crew.",
    "The command of the ship Bérrio was held by Nicolau __________."
]):
    ans_list = ["Kappad", "Lisbon", "Paulo", "Cape", "Good Hope", "Malindi", "scurvy", "Coelho"]
    sec1_en.append({
        "type": "Fill in the Blank",
        "q": qtext,
        "ans": ans_list[idx],
        "sol": "Correctly identifies crucial timeline details of Vasco da Gama's first voyage."
    })

# Match
sec1_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the ships of Vasco da Gama's first voyage with their commanders:",
        "items": [{"left": "São Gabriel"}, {"left": "São Rafael"}, {"left": "Bérrio"}],
        "options": [{"val": "0", "text": "Vasco da Gama"}, {"val": "1", "text": "Paulo da Gama"}, {"val": "2", "text": "Nicolau Coelho"}],
        "sol": "São Gabriel was commanded by Vasco, São Rafael by his brother Paulo, and Bérrio by Nicolau Coelho."
    },
    {
        "type": "Match the Following",
        "q": "Match the ports visited on the East African coast with their characteristics:",
        "items": [{"left": "Mozambique"}, {"left": "Mombasa"}, {"left": "Malindi"}],
        "options": [{"val": "0", "text": "Conflict and expulsion"}, {"val": "1", "text": "Hostility and ambush plans"}, {"val": "2", "text": "Warm welcome and pilot provision"}],
        "sol": "Gama faced conflict in Mozambique, hostile plotting in Mombasa, and a helpful ally in Malindi."
    },
    {
        "type": "Match the Following",
        "q": "Match the key dates of the first voyage with their corresponding events:",
        "items": [{"left": "July 1497"}, {"left": "May 1498"}, {"left": "August 1499"}],
        "options": [{"val": "0", "text": "Departure from Lisbon"}, {"val": "1", "text": "Arrival at Kappad, Calicut"}, {"val": "2", "text": "Return of the first ship Bérrio"}],
        "sol": "The fleet departed in July 1497, arrived at Calicut in May 1498, and Bérrio returned first in July/August 1499."
    }
])

# One-Liners
for idx, qtext in enumerate([
    "What was the direct financial return ratio of the spice cargo brought back by Vasco da Gama?",
    "Who commanded the ship Bérrio during the first voyage?",
    "Which maritime route did Vasco da Gama's voyage establish between Europe and Asia?",
    "How many ships returned to Lisbon out of the original four that set sail?",
    "In which African city did Gama secure the services of a pilot to cross the Arabian Sea?",
    "Why did Vasco da Gama order the destruction of the São Rafael?",
    "Which group of merchants held a monopoly over Calicut's spice trade before Gama's arrival?",
    "Where did Paulo da Gama die and get buried on the return voyage?"
]):
    sols = [
        "The cargo sold for approximately 60 times the total cost of the expedition.",
        "Nicolau Coelho commanded the Bérrio.",
        "The Cape Route (sailing around the Cape of Good Hope).",
        "Only two ships (São Gabriel and Bérrio) returned safely.",
        "Malindi (in modern-day Kenya).",
        "Scurvy had reduced the crew size to the point where there weren't enough men to operate all three remaining ships.",
        "Arab and Muslim merchants.",
        "He died and was buried in Terceira Island in the Azores."
    ]
    sec1_en.append({"type": "One-Liner", "q": qtext, "sol": sols[idx]})

# Assertion-Reason
sec1_en.extend([
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The first Portuguese voyage bypassed traditional Mediterranean trade routes.\nReason: Vasco da Gama sailed around the southern tip of Africa to open a direct ocean route.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The Cape Route completely bypassed Mediterranean routes controlled by Venice and Egypt."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama was forced to destroy the São Rafael off East Africa.\nReason: More than half of his crew had died from scurvy and exhaustion, making it impossible to man three vessels.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The extreme crew losses forced the consolidation of the remaining sailors onto São Gabriel and Bérrio."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Zamorin of Calicut initially welcomed the Portuguese expedition.\nReason: Traditional Indian ocean commerce welcomed diverse merchants, and the Zamorin saw potential new revenues.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The Hindu ruler (Zamorin) was open to trade and expected substantial trade duties and gifts."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The voyage took over two years to complete.\nReason: The fleet spent several months waiting for correct monsoon winds in both directions.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "Understanding and waiting for the monsoon wind cycles was critical for sailing across the Arabian Sea."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: King Manuel I was highly pleased with the outcome of the voyage.\nReason: The voyage proved that a direct route was viable and promised massive commercial profits.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The profitability of the spices and the proof of the route delighted the Portuguese crown."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Portuguese fleet sailed far west into the Atlantic Ocean before turning south.\nReason: They wanted to avoid the calm zones and counter-currents of the Gulf of Guinea.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "This sailing maneuver, known as 'Volta do Mar', utilized winds to clear the African coast."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The first voyage did not immediately establish a military fortress in India.\nReason: Vasco da Gama's primary mission was exploration, mapping, and securing trade treaties rather than territorial conquest.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "Military conquest and fortification were later policies initiated under Almeida and Albuquerque."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama was awarded the title 'Dom' by the Portuguese King.\nReason: He successfully completed the voyage and established the first European colony in India in 1498.",
        "opts": EN_AR_OPTS, "ans": 2, "sol": "Assertion is true. Reason is false because he did not establish a colony in 1498; that occurred years later."
    }
])

# Statement-Based
sec1_en.extend([
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding Vasco da Gama's fleet:\n1. It consisted of three standard caravels and one supply ship.\n2. The São Rafael was the largest ship and served as the flagship.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 3, "sol": "São Gabriel was the flagship. The ships were square-rigged naus, not standard caravels."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the navigation of the first voyage:\n1. Vasco da Gama used astronomical navigation using the astrolabe.\n2. The fleet used Arabic navigational charts purchased in Lisbon.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "They used astrolabes and solar declination tables. Arabic charts were only obtained later in East Africa."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the return journey of the first voyage, consider these statements:\n1. The crossing of the Arabian Sea took three months due to lack of wind.\n2. Nicolau Coelho's ship Bérrio arrived back in Portugal before Vasco da Gama's flagship.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "The crossing took 3 months (vs 23 days outbound) due to calm winds, causing severe scurvy. Bérrio arrived in July 1499, while Gama delayed at Azores."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding pilot Ibn Majid:\n1. He was a native of Malindi who wanted to migrate to India.\n2. He possessed precise knowledge of the seasonal monsoon wind changes.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "He was a Gujarati/Arab pilot hired in Malindi who knew the monsoon winds of the Indian Ocean."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the commercial impact of the first voyage, consider these statements:\n1. Spices brought back were sold at the Lisbon spice market (Casa da India).\n2. Venice immediately declared war on Portugal to protect its trade route.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "The spices were sold through Casa da Índia. Venice did not declare war immediately, though they suffered commercial decline."
    }
])

# Open Questions
for idx, qtype in enumerate(["Why", "Why", "Why", "How", "How", "How", "Case Study", "Case Study", "Case Study", "Teach the Concept", "Teach the Concept", "Teach the Concept"]):
    qtexts = [
        "Why did Vasco da Gama perform a wide westward arc in the Atlantic Ocean during the outbound journey?",
        "Why was the return crossing of the Arabian Sea so catastrophic compared to the outward journey?",
        "Why did the Sultan of Malindi welcome Vasco da Gama while Mozambique and Mombasa expelled him?",
        "How did the discovery of the Cape Route affect the prices of spices in Western Europe?",
        "How did Vasco da Gama's crew navigate without sight of land during the Atlantic crossing?",
        "How did the loss of crew members affect the fleet's composition on the return voyage?",
        "Examine the role of Malindi as a strategic junction in the Portuguese maritime network.",
        "Analyze the impact of scurvy on the viability of early long-distance Portuguese voyages.",
        "Discuss the significance of the return of the ship Bérrio under Nicolau Coelho.",
        "Explain the concept of 'Volta do Mar' (Turn of the Sea) to a student.",
        "Describe how monsoon wind patterns dictated trade schedules in the Indian Ocean.",
        "Explain the structure and command hierarchy of Vasco da Gama's first fleet."
    ]
    sols = [
        "He executed the 'Volta do mar' maneuver to catch the prevailing westerly winds, thereby bypassing the adverse currents and doldrums of the Gulf of Guinea.",
        "Gama sailed against the summer monsoon winds in August. Lacking favorable winds, the crossing took 3 months, leading to extreme scurvy and starvation.",
        "Malindi was in a regional rivalry with Mombasa and saw the well-armed Portuguese as potential allies to balance local power.",
        "It bypassed the heavy taxation imposed by Ottoman, Mamluk, and Venetian middlemen, eventually lowering wholesale spice costs while concentrating trade wealth in Lisbon.",
        "They used celestial navigation, measuring the altitude of the sun and stars (like the Pole Star) using brass astrolabes and quadrant instruments.",
        "With around half the crew dead, Gama was forced to abandon and burn the São Rafael near Mombasa, distributing the survivors onto the São Gabriel and Bérrio.",
        "Malindi served as a safe haven providing fresh water, provisions, and pilots. This alliance remained a cornerstone of Portuguese navigation along the Swahili coast for decades.",
        "Scurvy caused massive crew loss (often 50%+). It highlights the physiological limits of early modern exploration before the connection between fresh citrus fruits and preventing the disease was established.",
        "Bérrio was a caravel and the fastest ship. It separated from the flagship and arrived first in Lisbon, delivering the first proof that the route to India was open.",
        "It is a sailing technique where navigators sail in a wide circle to find favorable winds rather than sailing directly against head-winds. Gama sailed far west near Brazil to round Africa successfully.",
        "Winds blow from the southwest in summer (May-Sept) aiding travel to India, and from the northeast in winter (Oct-April) aiding return voyages. Sailing against these caused long delays.",
        "The fleet was state-commissioned, combining heavy naus (ships) with a fast caravel (Bérrio) and a supply ship, commanded by Gama as captain-major, with experienced pilots."
    ]
    sec1_en.append({"type": qtype, "q": qtexts[idx], "sol": sols[idx]})


# ==================== SECTION 2: ENCOUNTERS WITH ZAMORIN ====================
sec2_en = [
    {
        "type": "MCQ",
        "q": "What was the hereditary title held by the Hindu ruler of Calicut who received Vasco da Gama in 1498 CE?",
        "opts": ["Zamorin (Samudiri)", "Adil Shah", "Kolathiri", "Nayaka"],
        "ans": 0,
        "sol": "The ruler of Calicut held the title Zamorin, a Portuguese corruption of the Malayalam word 'Samudiri' meaning Lord of the Sea."
    },
    {
        "type": "MCQ",
        "q": "How did the Zamorin of Calicut react to the gifts presented by Vasco da Gama during their first audience?",
        "opts": ["He was disappointed and unimpressed by their low quality", "He immediately accepted them as high tribute", "He imprisoned Gama for insulting the crown", "He traded them for gold coins"],
        "ans": 0,
        "sol": "The gifts (hats, cloth, sugar, honey) were cheap merchant items. The Zamorin and his court ridiculed them as unfit for a king."
    },
    {
        "type": "MCQ",
        "q": "Which faction of merchants in Calicut strongly opposed Vasco da Gama and tried to sabotage his trade negotiations?",
        "opts": ["Arab and Muslim merchants", "Gujarati Bania merchants", "Chinese junk traders", "Syrian Christian traders"],
        "ans": 0,
        "sol": "Arab merchants held a monopoly on spice exports in Calicut and rightly feared Portuguese naval armed competition."
    },
    {
        "type": "MCQ",
        "q": "What did the Zamorin demand from Vasco da Gama before allowing him to depart Calicut with his cargo?",
        "opts": ["Payment of port customs duties in gold/silver", "Surrender of the flagship São Gabriel", "Conversion of the Portuguese crew to Hinduism", "An alliance against the ruler of Cochin"],
        "ans": 0,
        "sol": "The Zamorin demanded standard port customs duties. Gama refused, claiming exemption as an ambassador, leading to a standoff."
    },
    {
        "type": "MCQ",
        "q": "How did Vasco da Gama retaliate when the Zamorin temporarily detained some Portuguese factors and goods?",
        "opts": ["He seized local hostages and sailed away with them", "He launched a full naval invasion of Calicut city", "He paid the custom duties double in value", "He burned down the local temple"],
        "ans": 0,
        "sol": "To force the release of his men and goods, Gama captured several Calicut citizens and took them back to Lisbon."
    },
    # Multi
    {
        "type": "Multiple Correct MCQ",
        "q": "Why were the Arab merchants of Calicut hostile towards the arrival of Vasco da Gama? (Select all that apply)",
        "opts": ["They feared losing their lucrative monopoly on spice exports", "They wanted to protect their religious influence at court", "They realized the Portuguese intended to enforce a monopoly by naval force", "They were allied with the British East India Company"],
        "ans": [0, 1, 2],
        "sol": "The Arab traders recognized that Portuguese armed ships aimed to seize the Indian Ocean trade by force and exclude other merchants."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following items did Vasco da Gama present to the Zamorin that were rejected as tribute? (Select all that apply)",
        "opts": ["Cheap woolen cloth", "Coral beads and hats", "Jars of oil and honey", "Fine gold coins and silver plates"],
        "ans": [0, 1, 2],
        "sol": "The gifts were simple trade goods of low value, lacking the gold, silver, or fine gems expected by an Indian king."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which factors made Calicut a major trading hub on the Malabar Coast? (Select all that apply)",
        "opts": ["Strategic location midway along the Indian Ocean trade network", "Abundant local cultivation of high-quality black pepper", "Open port policy welcoming merchants of all nationalities", "Heavy Portuguese naval protection since the 14th century"],
        "ans": [0, 1, 2],
        "sol": "Calicut grew wealthy due to its location, pepper production, and tolerant commercial policy, long before Europeans arrived."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What were the main grievances of the Zamorin against Vasco da Gama during the first visit? (Select all that apply)",
        "opts": ["The insultingly cheap gifts presented to the throne", "Gama's refusal to pay standard port customs duties", "The hostile abduction of Calicut citizens", "The establishment of a fort without permission"],
        "ans": [0, 1, 2],
        "sol": "The Zamorin was offended by the poor gifts, the tax evasion, and the hostage-taking. No fort was established in 1498."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the languages used to translate communications between Vasco da Gama and the Zamorin. (Select all that apply)",
        "opts": ["Arabic", "Malayalam", "Portuguese", "Sanskrit"],
        "ans": [0, 1, 2],
        "sol": "Portuguese was translated to Arabic (by bilingual convicts or merchants), which was then translated to Malayalam for the Zamorin."
    },
    # T/F
    {"type": "True/False", "q": "True or False: The Zamorin of Calicut was a Muslim Sultan belonging to the Adil Shahi dynasty.", "ans": False, "sol": "The Zamorin was a Hindu monarch belonging to the Nair/Samantaclan."},
    {"type": "True/False", "q": "True or False: The Zamorin granted Vasco da Gama a written treaty giving Portugal a monopoly on spice exports.", "ans": False, "sol": "He refused, stating Calicut was a free port open to all traders."},
    {"type": "True/False", "q": "True or False: The Arab merchants successfully persuaded the Zamorin to execute Vasco da Gama on his first visit.", "ans": False, "sol": "They urged execution or arrest, but the Zamorin only demanded taxes and let him leave after cargo exchanges."},
    {"type": "True/False", "q": "True or False: Vasco da Gama's gifts included fine European mechanical clocks that fascinated the court.", "ans": False, "sol": "No, his gifts were rudimentary items like brass basins and oil jars, which were laughed at."},
    {"type": "True/False", "q": "True or False: Calicut was valued as a transit center where spices from Southeast Asia were transshipped.", "ans": True, "sol": "It was an entropic port where spices from Malacca were traded alongside local Malabar pepper."},
    {"type": "True/False", "q": "True or False: Vasco da Gama departed Calicut with a cargo of spices that he obtained without paying any duties.", "ans": False, "sol": "He loaded spices but left behind some factors and seized hostages in lieu of confiscated Portuguese goods."},
    {"type": "True/False", "q": "True or False: The title Samudiri literally translates to 'Lord of the Sea'.", "ans": True, "sol": "Samudiri Raja means the king who rules the sea, emphasizing Calicut's maritime dependence."},
    {"type": "True/False", "q": "True or False: Calicut was heavily fortified by the Portuguese during Vasco da Gama's first visit in 1498.", "ans": False, "sol": "No fortification took place during the first visit. Tensions were too high."}
]

# Fill Blanks
for idx, qtext in enumerate([
    "The hereditary title of the ruler of Calicut was the __________.",
    "The primary language used as an intermediary for translation at Calicut was __________.",
    "The court officials of the Zamorin mocked the Portuguese gifts as being fit only for __________.",
    "The Zamorin belonged to the __________ religion.",
    "Vasco da Gama retaliated against the Zamorin by taking several __________.",
    "The Malabar Coast was famous worldwide for the trade of black __________.",
    "The Arab traders of Calicut were concerned about the Portuguese violating their __________.",
    "The Malayalam word from which 'Zamorin' is corrupted is __________."
]):
    ans_list = ["Zamorin", "Arabic", "merchants", "Hindu", "hostages", "pepper", "monopoly", "Samudiri"]
    sec2_en.append({
        "type": "Fill in the Blank",
        "q": qtext,
        "ans": ans_list[idx],
        "sol": "Details key aspects of the diplomatic encounter in Calicut."
    })

# Match
sec2_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the entities in Calicut with their roles:",
        "items": [{"left": "Zamorin"}, {"left": "Arab merchants"}, {"left": "Monzaide"}],
        "options": [{"val": "0", "text": "Hindu sovereign of Calicut"}, {"val": "1", "text": "Monopolists of spice trade"}, {"val": "2", "text": "North African translator who assisted Gama"}],
        "sol": "Zamorin was the ruler, Arab merchants held trade, and Monzaide (or Temudo) acted as translator."
    },
    {
        "type": "Match the Following",
        "q": "Match the gifts with their reception by the Calicut court:",
        "items": [{"left": "Brass washbasins"}, {"left": "Gold and silver"}, {"left": "Fine silks"}],
        "options": [{"val": "0", "text": "Mocked by the officials"}, {"val": "1", "text": "Expected by the Zamorin but absent"}, {"val": "2", "text": "Demanded by court for trade prestige"}],
        "sol": "Brass basins were actually presented and mocked. Gold and silver were expected but not brought."
    },
    {
        "type": "Match the Following",
        "q": "Match the disputes between Gama and the Zamorin with their causes:",
        "items": [{"left": "Tax dispute"}, {"left": "Gifts dispute"}, {"left": "Hostage crisis"}],
        "options": [{"val": "0", "text": "Demand for customs duties in gold"}, {"val": "1", "text": "Inadequacy of European trade items"}, {"val": "2", "text": "Detention of Portuguese factor Duarte Barbosa"}],
        "sol": "Taxes were about custom duties, gifts about low-value goods, and hostages about the detained factor."
    }
])

# One-Liners
for idx, qtext in enumerate([
    "Why did the Zamorin's officials laugh at the gifts brought by Vasco da Gama?",
    "What Malayalam term is the source of the name Zamorin?",
    "Name the North African Muslim who helped translate for Gama at Calicut.",
    "Which merchant community held the dominant position in the Calicut port administration?",
    "How did the Zamorin respond to the Portuguese request for a monopoly treaty?",
    "What did Gama do to force the release of his trade goods?",
    "Why was Calicut considered an open port before 1498?",
    "What was the main spice exported from Calicut?"
]):
    sols = [
        "They were cheap goods like hats and washbasins, unfit for a sovereign ruler.",
        "Samudiri (or Samutiri).",
        "Monzaide (who spoke Spanish/Arabic).",
        "The Arab/Mappila Muslim merchants.",
        "He rejected it, maintaining that Calicut was open to all nations.",
        "He kidnapped several Calicut citizens as hostages.",
        "It did not enforce exclusive monopolies and welcomed traders from all countries.",
        "Black pepper."
    ]
    sec2_en.append({"type": "One-Liner", "q": qtext, "sol": sols[idx]})

# Assertion-Reason
sec2_en.extend([
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Zamorin refused to grant the Portuguese a monopoly on pepper exports.\nReason: The Zamorin did not want to alienate the Arab merchants who generated the bulk of Calicut's revenues.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The Arab trade was vital for Calicut's prosperity, making the Zamorin reluctant to favor the Portuguese."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama took hostages from Calicut before his departure.\nReason: The Zamorin had seized Portuguese merchandise and held a factor, demanding customs duties.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The hostage-taking was a direct reaction to the detention of the Portuguese factor and goods."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Communication between Vasco da Gama and the Zamorin was highly direct and clear.\nReason: Several Portuguese officers were fluent in Malayalam and acted as interpreters.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "Communication was convoluted, going through multiple translations (Portuguese to Arabic, and then to Malayalam)."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Arab merchants viewed the Portuguese arrival as a threat to their survival.\nReason: The Portuguese did not intend to trade peacefully but to use armed naval power to monopolize routes.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The Portuguese policy of armed mercantilism was designed to forcefully destroy competitor trade."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Zamorin's court treated Gama with absolute royal honor.\nReason: They expected the Portuguese to bring massive treasures of European gold.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "The initial reception was respectful, but the court soon mocked the cheap gifts, leading to a loss of prestige for Gama."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Calicut was a major transit point for Chinese silk and porcelain.\nReason: Calicut lay at the convergence of Chinese shipping routes and Western Indian Ocean routes.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "Calicut's geographical location made it a major global transshipment hub."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama paid the customs duties demanded by the Zamorin.\nReason: The Portuguese crown had instructed Gama to strictly follow all local tax laws to secure long-term treaties.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "Gama refused to pay the duties, claiming he was an ambassador and not a merchant, which caused the tax dispute."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The relationship between the Zamorin and the Portuguese remained hostile after 1499.\nReason: The Portuguese returned on subsequent voyages with heavy naval armaments to punish Calicut.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The mutual distrust of the first voyage escalated into open war in subsequent years."
    }
])

# Statement-Based
sec2_en.extend([
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the Zamorin's administration:\n1. The port officer (Shahbandar) of Calicut was traditionally an Arab merchant.\n2. The administration relied heavily on customs duties (export taxes) on spices.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Arab merchants held key administrative posts related to trade, and customs duties were the crown's primary revenue."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the gifts presented by Gama, consider these statements:\n1. The gifts were chosen by the King of Portugal, who underestimated Indian royal wealth.\n2. The Zamorin suggested that Gama should have brought gold or silver instead of washbasins.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are correct. The cheap items were standard for West African trade but insulted the wealthy Zamorin."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:\n1. Calicut was the capital of the Vijayanagara Empire.\n2. The Zamorin was subordinate to the Bahmani Sultan.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 3, "sol": "Calicut was an independent kingdom ruled by the Zamorin. It was not part of Vijayanagara or Bahmani empires."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the Arab merchants at Calicut, consider these statements:\n1. They were led by a wealthy merchant family known as the Koya family.\n2. They controlled the shipping vessels but did not interfere with local politics.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "The Koyas and Shabhandars exercised huge political influence over the Zamorin to protect their trade interests."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the hostages taken by Vasco da Gama:\n1. The hostages were members of the Zamorin's own family.\n2. They were taken to Lisbon and presented to the King of Portugal.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "The hostages were local merchants and fishermen, not the Zamorin's family. They were taken to Lisbon as proof of the voyage."
    }
])

# Open Questions
for idx, qtype in enumerate(["Why", "Why", "Why", "How", "How", "How", "Case Study", "Case Study", "Case Study", "Teach the Concept", "Teach the Concept", "Teach the Concept"]):
    qtexts = [
        "Why did the Zamorin refuse to give the Portuguese exclusive trading rights?",
        "Why were the gifts Vasco da Gama brought considered an insult to the Zamorin?",
        "Why did the Arab merchants have so much influence over the Calicut administration?",
        "How did the linguistic barrier affect the initial meetings between Gama and the Zamorin?",
        "How did Vasco da Gama use hostage-taking as a tool of coercion during his first visit?",
        "How did the trade rivalry at Calicut shape the future alliances of the Portuguese on the Malabar Coast?",
        "Analyze the administrative role of Arab merchants in the port city of Calicut.",
        "Examine the gift-giving ritual in Indian courts as a study of cross-cultural diplomatic failure.",
        "Evaluate the Zamorin's policy of maintaining Calicut as a free-trade zone.",
        "Explain the origin and meaning of the title 'Zamorin' to a student.",
        "Describe the mechanisms of custom duty collection at Calicut port.",
        "Explain how the Portuguese threat altered the traditional trade rules in the Indian Ocean."
    ]
    sols = [
        "The Zamorin followed a free-port policy. Granting a monopoly to Portugal would alienate Arab merchants and destroy Calicut's commercial foundation.",
        "They consisted of cheap items (cloth, hats, honey) suited for primitive African trade, whereas Indian rulers were accustomed to receiving precious metals, gems, and fine goods.",
        "They generated the vast majority of Calicut's tax revenue through shipping, and held key administrative posts like Shahbandar (port officer).",
        "It created deep mistrust. Since no Portuguese spoke Malayalam and no local spoke Portuguese, messages went through multiple translations, leading to misinterpretations.",
        "Gama kidnapped local citizens to leverage the release of Portuguese factors and goods detained by the Zamorin over unpaid taxes, establishing a precedent of force.",
        "The hostility of Calicut forced the Portuguese to seek alliances with Calicut's rivals, notably the ruler of Cochin, which became the main Portuguese base.",
        "Arab traders acted as financial backers, tax collectors, and diplomats for the Zamorin, integrating trade directly with the political structure.",
        "The Portuguese failure to provide appropriate prestige gifts showed a lack of diplomatic preparation, ruining their credibility in the eyes of the Zamorin.",
        "The Zamorin allowed all merchants (Arabs, Gujaratis, Chinese) to trade on equal terms, which ensured high cargo volumes and port duties.",
        "It comes from the Malayalam 'Samudiri Raja', meaning 'Lord of the Sea', which highlights the maritime nature of his authority.",
        "Goods were inspected by the port officers, and taxes were levied based on cargo volume and value, typically paid in gold or silver coins.",
        "Before 1498, trade was largely unarmed and open. The Portuguese introduced armed ships and the Cartaz system, forcing merchants to buy protection."
    ]
    sec2_en.append({"type": qtype, "q": qtexts[idx], "sol": sols[idx]})


# ==================== SECTION 3: SECOND VOYAGE ====================
sec3_en = [
    {
        "type": "MCQ",
        "q": "In which year did Vasco da Gama return to India for his highly militarized second voyage?",
        "opts": ["1502 CE", "1500 CE", "1505 CE", "1510 CE"],
        "ans": 0,
        "sol": "Vasco da Gama returned in 1502 CE with a fleet of 20 heavily armed ships to establish dominance."
    },
    {
        "type": "MCQ",
        "q": "Which explorer commanded the intermediate Portuguese expedition to India (1500 CE) between Gama's first and second voyages?",
        "opts": ["Pedro Álvares Cabral", "Bartolomeu Dias", "Francisco de Almeida", "Afonso de Albuquerque"],
        "ans": 0,
        "sol": "Pedro Álvares Cabral commanded the second Portuguese expedition in 1500, discovering Brazil along the way."
    },
    {
        "type": "MCQ",
        "q": "With which regional rival of the Zamorin did Vasco da Gama establish a crucial alliance during his second voyage?",
        "opts": ["The Raja of Cochin (Kochi)", "The Sultan of Bijapur", "The Kolathiri of Kannur", "The King of Vijayanagara"],
        "ans": 0,
        "sol": "Gama allied with the Raja of Cochin, who welcomed the Portuguese to counter Calicut's hegemony."
    },
    {
        "type": "MCQ",
        "q": "What violent act did Vasco da Gama commit against Calicut during his second voyage in 1502 CE?",
        "opts": ["He bombarded the city and destroyed Calicut's merchant fleet", "He captured and occupied the Zamorin's palace", "He executed the Zamorin during negotiations", "He poisoned the city's water supply"],
        "ans": 0,
        "sol": "Gama bombarded Calicut, captured merchant ships, and cut off the ears and hands of captured sailors to terrify the Zamorin."
    },
    {
        "type": "MCQ",
        "q": "Where did Vasco da Gama establish the first permanent Portuguese factory (trading post) in India during his second expedition?",
        "opts": ["Cochin (Kochi)", "Calicut", "Goa", "Pulicat"],
        "ans": 0,
        "sol": "He established the first factory at Cochin in 1503 (completed after his arrival/alliance), which became their first headquarters."
    },
    # Multi
    {
        "type": "Multiple Correct MCQ",
        "q": "What were the primary mandates given to Vasco da Gama for his second voyage in 1502? (Select all that apply)",
        "opts": ["To avenge the massacre of Portuguese factors left by Cabral", "To enforce the crown monopoly over the spice trade", "To establish trading factories at Cochin and Cannur", "To capture Goa and make it the capital of Portuguese India"],
        "ans": [0, 1, 2],
        "sol": "Gama's 1502 mission was to punish Calicut (avenging the factory massacre), enforce the monopoly, and set up posts at Cochin and Cannur. Goa was captured later in 1510."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following ports became key nodes in the early Portuguese trade network established during the second voyage? (Select all that apply)",
        "opts": ["Cochin", "Kannur (Cannanore)", "Quilon (Kollam)", "Madras (Chennai)"],
        "ans": [0, 1, 2],
        "sol": "Cochin, Kannur, and Quilon were all early trading partners and factory locations for the Portuguese. Madras was British."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the extreme measures taken by Vasco da Gama to terrorize Calicut merchants in 1502. (Select all that apply)",
        "opts": ["Plundering and burning the Pilgrim ship Miri with passengers on board", "Bombarding Calicut port and destroying harbor structures", "Mutilating captured crew members and sending them to the Zamorin", "Bribing the Zamorin's chief priest to assassinate him"],
        "ans": [0, 1, 2],
        "sol": "Gama committed brutal acts, including burning the Miri (killing hundreds), bombarding Calicut, and mutilating captives."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What benefits did the Raja of Cochin gain from allying with the Portuguese? (Select all that apply)",
        "opts": ["Military protection against the expansionist Zamorin of Calicut", "Access to modern European firearms and naval support", "Enhanced trade revenue through the Portuguese factory", "Direct annexation of the Vijayanagara territories"],
        "ans": [0, 1, 2],
        "sol": "Cochin was a vassal of Calicut. Allying with the Portuguese gave them independence and defense against the Zamorin."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which ship types were part of Vasco da Gama's 1502 armed armada? (Select all that apply)",
        "opts": ["Heavily armed Naus (carracks)", "Fast sailing Caravels", "Armed supply ships", "Steam ironclads"],
        "ans": [0, 1, 2],
        "sol": "The fleet consisted of carracks (naus) and caravels equipped with heavy artillery. Steamships did not exist."
    },
    # T/F
    {"type": "True/False", "q": "True or False: Pedro Álvares Cabral's factors in Calicut were massacred by local riots before Gama's second voyage.", "ans": True, "sol": "Yes, a conflict between Cabral's men and Muslim merchants led to a riot where the Portuguese factory was destroyed and factors killed."},
    {"type": "True/False", "q": "True or False: Vasco da Gama demanded that the Zamorin expel all Muslim merchants from Calicut as a condition for peace in 1502.", "ans": True, "sol": "Gama demanded the complete expulsion of all Arab/Muslim traders, which the Zamorin refused."},
    {"type": "True/False", "q": "True or False: The Raja of Cochin was a close relative and loyal vassal of the Zamorin of Calicut.", "ans": False, "sol": "He was a bitter rival who resented Calicut's domination and eagerly allied with the Portuguese."},
    {"type": "True/False", "q": "True or False: Vasco da Gama established the Cartaz system during his first voyage in 1498.", "ans": False, "sol": "The Cartaz (shipping license) system was developed during and after the second voyage in 1502 to enforce control."},
    {"type": "True/False", "q": "True or False: The pilgrim ship Miri was carrying passengers returning from Mecca when Vasco da Gama captured and burned it.", "ans": True, "sol": "Yes, this was one of the most controversial and brutal incidents of Gama's career, killing over 300 pilgrims."},
    {"type": "True/False", "q": "True or False: Vasco da Gama captured Goa in 1502 and established the Estado da Índia capital there.", "ans": False, "sol": "Albuquerque captured Goa in 1510. During 1502, Cochin was the primary Portuguese base."},
    {"type": "True/False", "q": "True or False: The Kolathiri Raja of Kannur refused to allow the Portuguese to establish a factory in his territory.", "ans": False, "sol": "The Kolathiri welcomed them and allowed a factory at Kannur to counter Calicut."},
    {"type": "True/False", "q": "True or False: Vasco da Gama returned to Portugal in 1503 with a massive cargo of spices and left a permanent naval patrol.", "ans": True, "sol": "He left behind a coastal patrol fleet under Vicente Sodré to protect Cochin and blockade Calicut."}
]

# Fill Blanks
for idx, qtext in enumerate([
    "The commander of the 1500 CE Portuguese voyage was Pedro Álvares __________.",
    "Vasco da Gama returned in 1502 with a fleet of __________ ships.",
    "The Portuguese established their first factory at the port of __________.",
    "Gama captured and burned the pilgrim vessel named __________.",
    "The ruler of Cochin welcomed the Portuguese to counter the power of the __________ of Calicut.",
    "The Portuguese naval patrol left behind in 1503 was commanded by Vicente __________.",
    "Gama demanded the complete expulsion of all __________ merchants from Calicut.",
    "The first Portuguese fortress built in India (1503) was Fort Emmanuel in __________."
]):
    ans_list = ["Cabral", "20", "Cochin", "Miri", "Zamorin", "Sodre", "Muslim", "Cochin"]
    sec3_en.append({
        "type": "Fill in the Blank",
        "q": qtext,
        "ans": ans_list[idx],
        "sol": "Identifies key details of the militarized second voyage."
    })

# Match
sec3_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the Portuguese expeditions with their years:",
        "items": [{"left": "Vasco da Gama (1st)"}, {"left": "Pedro Álvares Cabral"}, {"left": "Vasco da Gama (2nd)"}],
        "options": [{"val": "0", "text": "1497 - 1499 CE"}, {"val": "1", "text": "1500 - 1501 CE"}, {"val": "2", "text": "1502 - 1503 CE"}],
        "sol": "Gama's first was 1497-99, Cabral's was 1500-01, and Gama's second was 1502-03."
    },
    {
        "type": "Match the Following",
        "q": "Match the Indian ports with their Portuguese status in 1503:",
        "items": [{"left": "Cochin"}, {"left": "Kannur"}, {"left": "Calicut"}],
        "options": [{"val": "0", "text": "Main ally and first fortress"}, {"val": "1", "text": "Secondary factory and trade post"}, {"val": "2", "text": "Hostile port under blockade"}],
        "sol": "Cochin was the main ally, Kannur had a secondary factory, and Calicut was blockaded."
    },
    {
        "type": "Match the Following",
        "q": "Match the historical actions of the second voyage with their targets:",
        "items": [{"left": "Miri ship incident"}, {"left": "Vicente Sodré patrol"}, {"left": "Fort Emmanuel"}],
        "options": [{"val": "0", "text": "Burning of Muslim pilgrims"}, {"val": "1", "text": "Blockade of the Red Sea route"}, {"val": "2", "text": "Defense of Cochin factory"}],
        "sol": "Miri was the pilgrim ship, Sodré blockaded the Red Sea, and Fort Emmanuel defended Cochin."
    }
])

# One-Liners
for idx, qtext in enumerate([
    "Why did Gama return to India with a large military fleet in 1502?",
    "Which European nation pioneered the use of ship-borne cannons in the Indian Ocean?",
    "Who was the leader of the Cochin alliance that supported Gama?",
    "What was the name of the pilgrim ship destroyed by Gama in 1502?",
    "Where was the first Portuguese fortress built in India?",
    "What was the main purpose of the Cartaz system introduced during the second voyage?",
    "Why was Vicente Sodré's patrol left in Indian waters?",
    "What terms did Gama demand from the Zamorin for peace in 1502?"
]):
    sols = [
        "To enforce the spice monopoly by force and avenge the massacre of Portuguese factors.",
        "Portugal.",
        "The Raja of Cochin (Unni Goda Varma).",
        "The Miri.",
        "Cochin (Fort Emmanuel).",
        "To force all merchant ships to pay taxes and obtain license from the Portuguese.",
        "To protect the Cochin factory and blockade Muslim trade routes.",
        "The expulsion of all Muslim merchants and exclusive trading rights."
    ]
    sec3_en.append({"type": "One-Liner", "q": qtext, "sol": sols[idx]})

# Assertion-Reason
sec3_en.extend([
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama bombarded Calicut and mutilated prisoners during his second voyage.\nReason: He wanted to establish absolute naval terror to break the Zamorin's resistance to the spice monopoly.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The extreme violence was part of a calculated strategy of gunboat diplomacy."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Portuguese established their main base in Cochin rather than Calicut.\nReason: The Raja of Cochin was a rival of the Zamorin and offered land and support to the Portuguese.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The political fragmentation of the Malabar Coast allowed the Portuguese to exploit rivalries."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Pedro Álvares Cabral succeeded in maintaining peace in Calicut.\nReason: He reached an agreement with the Arab merchants to share spice exports.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "Cabral's voyage ended in conflict, and his factors were massacred, leading to Gama's retaliatory mission."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The burning of the ship Miri caused outrage across the Indian Ocean.\nReason: The ship was unarmed and carried over 300 civilian pilgrims, including women and children.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The destruction of the Miri was seen as a brutal act of piracy even by Portuguese contemporary standards."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Cartaz system was accepted voluntarily by all Indian Ocean merchants.\nReason: It guaranteed protection against pirates without any cost or restrictions.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "The Cartaz was an enforced license system that forced merchants to pay protection money or face capture."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Gama left a permanent naval force in India in 1503.\nReason: The Portuguese realized that a seasonal presence was insufficient to enforce their monopoly against Arab merchant networks.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "Leaving Sodré's patrol was the beginning of permanent European naval presence in Asia."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Fort Emmanuel was constructed in Cochin in 1503.\nReason: It was built to protect the Portuguese factory from attacks by the Zamorin's forces.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The fort was crucial in defending the Cochin factory during subsequent wars with Calicut."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama was appointed Governor-General of India in 1502.\nReason: He successfully defeated the Zamorin's navy at the Battle of Cochin.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "Gama was not appointed Governor-General or Viceroy in 1502. Almeida was the first Viceroy in 1505."
    }
])

# Statement-Based
sec3_en.extend([
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the Second Voyage of Vasco da Gama:\n1. The fleet consisted of 20 ships, divided into three squadrons.\n2. The expedition was funded partly by private merchant syndicates in Lisbon.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "The 1502 fleet was highly organized and combined royal ships with private merchant backing."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the Cochin alliance, consider these statements:\n1. Cochin was Cochin's attempt to liberate itself from Calicut's political dominance.\n2. The Portuguese built Fort Emmanuel using stone shipped directly from Lisbon.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "Cochin sought independence from Calicut. The fort was built using local materials (mainly coconut trunks and earth)."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the pilgrim ship Miri:\n1. The ship belonged to the Sultan of Egypt.\n2. Gama plundered the ship's cargo before setting it on fire.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "The Miri belonged to a rich Calicut merchant, though it carried pilgrims. Gama plundered it before burning it."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to early Portuguese factories, consider these statements:\n1. A factory was a manufacturing unit producing gunpowder.\n2. A factor (feitor) was a royal commercial agent responsible for buying spices.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Factories were trading posts (warehouses), not manufacturing units. Factors managed purchase and storage."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:\n1. The Portuguese patrol under Vicente Sodré sailed to the Red Sea but abandoned Cochin.\n2. The Zamorin occupied Cochin in 1503 after the patrol left.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Sodré sailed to the Red Sea to plunder, leaving Cochin vulnerable. The Zamorin invaded Cochin, forcing the Raja to flee."
    }
])

# Open Questions
for idx, qtype in enumerate(["Why", "Why", "Why", "How", "How", "How", "Case Study", "Case Study", "Case Study", "Teach the Concept", "Teach the Concept", "Teach the Concept"]):
    qtexts = [
        "Why did the Portuguese factory in Calicut get destroyed in 1500 CE?",
        "Why did Gama demand the expulsion of all Muslims from Calicut during his second voyage?",
        "Why did the Raja of Cochin continue his alliance with the Portuguese despite the Zamorin's invasions?",
        "How did Vasco da Gama use naval artillery to change the nature of Indian Ocean warfare in 1502?",
        "How did the Cartaz system work to enforce the Portuguese trade monopoly?",
        "How did the Portuguese secure their factories physically against land attacks?",
        "Analyze the Battle of Calicut (1502) as a study in early modern gunboat diplomacy.",
        "Examine the destruction of the ship Miri as a case study of religious and economic warfare.",
        "Evaluate the role of the Sodré patrol in establishing the Portuguese naval blockade.",
        "Explain the function of a 'factory' (feitoria) in the Portuguese commercial system.",
        "Describe the geopolitical rivalry between Calicut and Cochin and how the Portuguese exploited it.",
        "Explain the strategic purpose of Fort Emmanuel in Kochi."
    ]
    sols = [
        "Pedro Álvares Cabral seized an Arab merchant vessel. In retaliation, Muslim merchants and local riots attacked and burned the Portuguese factory, killing the factor Aires Correia.",
        "Gama wanted to eliminate his commercial rivals and establish a complete monopoly for the Portuguese crown. He also blamed them for the 1500 CE massacre.",
        "The Raja of Cochin was a vassal of Calicut and sought independence. Breaking the alliance would mean surrender to the Zamorin, who wanted to depose him.",
        "Traditional trade ships were unarmed. Gama used heavily armed carracks with cannons to destroy Calicut's fleet from a distance, initiating naval gun warfare.",
        "Every merchant vessel was required to buy a Cartaz (license) from a Portuguese factory, pay customs duties, and agree not to carry prohibited items (like spices or weapons). Ships without it were captured.",
        "They constructed fortified warehouses with stone walls, bastions, and artillery, which evolved into military fortresses like Fort Emmanuel.",
        "It showed that superior naval artillery could force local rulers to yield or suffer massive economic destruction, redefining diplomacy in Asia.",
        "Gama's actions against the Miri combined commercial warfare (seizing competitor goods) with crusading zeal (destroying Islamic pilgrim shipping), worsening conflicts.",
        "The patrol blockaded the mouth of the Red Sea to stop spice shipments to Egypt, forcing trade to redirect through the Portuguese Cape Route.",
        "It was a fortified trading post and warehouse where factors bought spices from local brokers and stored them until the annual Portuguese fleet arrived.",
        "Cochin was economically and politically subordinate to Calicut. The Portuguese offered Cochin military protection in exchange for exclusive trade, dividing local rulers.",
        "It was the first European fort in India, securing the Portuguese presence in Cochin against land invasions by the Zamorin's superior forces."
    ]
    sec3_en.append({"type": qtype, "q": qtexts[idx], "sol": sols[idx]})


# ==================== SECTION 4: THIRD VOYAGE & VICEROYALTY ====================
sec4_en = [
    {
        "type": "MCQ",
        "q": "In which year did Vasco da Gama return to India for his third and final voyage?",
        "opts": ["1524 CE", "1515 CE", "1530 CE", "1508 CE"],
        "ans": 0,
        "sol": "Vasco da Gama was sent back to India in 1524 CE by King John III."
    },
    {
        "type": "MCQ",
        "q": "What official title was bestowed upon Vasco da Gama for his third voyage to India in 1524 CE?",
        "opts": ["Viceroy of India", "Captain-Major of the Seas", "Governor of Goa", "High Commissioner of Cochin"],
        "ans": 0,
        "sol": "He was appointed the second Viceroy of India (following Francisco de Almeida and Albuquerque, who were Governors/Viceroys)."
    },
    {
        "type": "MCQ",
        "q": "Who was the Portuguese King who appointed Vasco da Gama as Viceroy in 1524 CE?",
        "opts": ["King John III", "King Manuel I", "King Sebastian", "King Afonso VI"],
        "ans": 0,
        "sol": "King John III succeeded King Manuel I and appointed Gama to clean up the corrupt administration."
    },
    {
        "type": "MCQ",
        "q": "What was the primary administrative objective of Vasco da Gama's final mission to India?",
        "opts": ["To curb rampant corruption among Portuguese officials", "To conquer the Kingdom of Vijayanagara", "To shift the capital from Goa to Cochin", "To convert the Zamorin to Christianity"],
        "ans": 0,
        "sol": "The Portuguese administration in India had become highly corrupt. Gama was sent as a strict disciplinarian to restore order."
    },
    {
        "type": "MCQ",
        "q": "Where in India did Vasco da Gama die on Christmas Eve, 1524 CE?",
        "opts": ["Cochin (Kochi)", "Goa", "Calicut", "Diu"],
        "ans": 0,
        "sol": "Vasco da Gama contracted malaria and died in Cochin on December 24, 1524."
    },
    # Multi
    {
        "type": "Multiple Correct MCQ",
        "q": "What problems did Vasco da Gama face when he arrived in India as Viceroy in 1524? (Select all that apply)",
        "opts": ["Rampant corruption and embezzlement by Portuguese officials", "Insubordination and lack of discipline in the military", "Declining royal revenues due to illegal private trading", "A massive invasion by the Mughal Emperor Babur"],
        "ans": [0, 1, 2],
        "sol": "Gama faced administrative decay, embezzlement, and private trade by officials. Babur's invasion was in North India and did not affect them."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following are true regarding Vasco da Gama's death and burial? (Select all that apply)",
        "opts": ["He died of malaria in Cochin on Christmas Eve, 1524", "He was initially buried in St. Francis Church in Cochin", "His remains were exhumed and returned to Portugal in 1539", "He was buried in the Basilica of Bom Jesus in Goa"],
        "ans": [0, 1, 2],
        "sol": "Gama died of malaria, was buried at St. Francis Church in Kochi, and his remains were later moved to Portugal. Bom Jesus holds St. Francis Xavier."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What reforms did Vasco da Gama attempt to implement during his brief viceroyalty? (Select all that apply)",
        "opts": ["Replacing corrupt officials with loyal administrators", "Strict auditing of factory accounts and spice storage", "Enforcing prohibitions on illegal private trade by soldiers", "Abolishing the Cartaz system to encourage free trade"],
        "ans": [0, 1, 2],
        "sol": "Gama focused on audits, replacing corrupt staff, and banning private trade. He kept the Cartaz system."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key Portuguese governors of India who ruled between Vasco da Gama's second and third voyages. (Select all that apply)",
        "opts": ["Francisco de Almeida", "Afonso de Albuquerque", "Lopo Soares de Albergaria", "Nino da Cunha"],
        "ans": [0, 1, 2],
        "sol": "Almeida (1505-09), Albuquerque (1509-15), and Albergaria (1515-18) ruled before Gama's return in 1524. Nino da Cunha ruled later (1529-38)."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which locations in India have monuments or historical sites directly associated with Vasco da Gama's life or death? (Select all that apply)",
        "opts": ["Kappad beach monument, Kozhikode", "St. Francis Church, Fort Kochi", "Vasco da Gama town, Goa", "St. Angelo Fort, Kannur"],
        "ans": [0, 1, 2],
        "sol": "Kappad (landing), St. Francis (burial), and Vasco town (named after him) are directly associated with him."
    },
    # T/F
    {"type": "True/False", "q": "True or False: Vasco da Gama was the first official Viceroy of Portuguese India.", "ans": False, "sol": "Francisco de Almeida was the first Viceroy in 1505. Gama was the second Viceroy, appointed in 1524."},
    {"type": "True/False", "q": "True or False: Vasco da Gama died of wounds sustained in a battle against the Zamorin's navy.", "ans": False, "sol": "He died of malaria (or illness) in Cochin, not from battle wounds."},
    {"type": "True/False", "q": "True or False: Vasco da Gama's remains are currently located in the Jerónimos Monastery in Lisbon.", "ans": True, "sol": "His body was returned to Portugal in 1539 and eventually interred in the Jerónimos Monastery."},
    {"type": "True/False", "q": "True or False: Gama served as Viceroy of India for over ten years before returning to Portugal.", "ans": False, "sol": "He served for only three months in 1524 before his sudden death."},
    {"type": "True/False", "q": "True or False: King John III sent Gama because of his reputation for being harsh and unyielding.", "ans": True, "sol": "Gama's stern reputation was seen as necessary to control the corrupt Portuguese factions in India."},
    {"type": "True/False", "q": "True or False: The St. Francis Church in Kochi where Gama was buried is the oldest European church in India.", "ans": True, "sol": "Built by the Portuguese in 1503, St. Francis Church is indeed the oldest European-built church in India."},
    {"type": "True/False", "q": "True or False: Gama shifted the official capital of Portuguese India from Goa back to Cochin in 1524.", "ans": False, "sol": "The capital remained in Goa (which was made capital by Albuquerque). Gama only died in Cochin during an administrative tour."},
    {"type": "True/False", "q": "True or False: Vasco da Gama was succeeded as Governor by Duarte de Menezes, whom he had suspended for corruption.", "ans": False, "sol": "Gama actually replaced Duarte de Menezes due to his corruption, and was succeeded after his death by Lopo Vaz de Sampaio."}
]

# Fill Blanks
for idx, qtext in enumerate([
    "Vasco da Gama was appointed Viceroy of India by King __________ of Portugal.",
    "Gama arrived in India for his third voyage in the year __________ CE.",
    "Gama died in the town of __________ on the Malabar Coast.",
    "The church where Gama was first buried was __________ Church in Kochi.",
    "Vasco da Gama's body was exhumed and returned to Portugal in the year __________.",
    "Gama replaced the corrupt governor Duarte de __________ in 1524.",
    "Vasco da Gama died on the evening of Christmas __________ in 1524.",
    "The major city in Goa named after the explorer is __________ da Gama."
]):
    ans_list = ["John III", "1524", "Cochin", "St. Francis", "1539", "Menezes", "Eve", "Vasco"]
    sec4_en.append({
        "type": "Fill in the Blank",
        "q": qtext,
        "ans": ans_list[idx],
        "sol": "Identifies key details of the third voyage and death."
    })

# Match
sec4_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the Portuguese Viceroys/Governors with their primary achievements:",
        "items": [{"left": "Francisco de Almeida"}, {"left": "Afonso de Albuquerque"}, {"left": "Vasco da Gama (1524)"}],
        "options": [{"val": "0", "text": "Blue Water Policy and naval battles"}, {"val": "1", "text": "Capture of Goa and Malacca"}, {"val": "2", "text": "Anti-corruption reforms and administrative cleanup"}],
        "sol": "Almeida established Blue Water Policy, Albuquerque captured Goa, and Gama reformed the administration in 1524."
    },
    {
        "type": "Match the Following",
        "q": "Match the events of Vasco da Gama's life with their geographical locations:",
        "items": [{"left": "Landing of first voyage"}, {"left": "Death of third voyage"}, {"left": "Final tomb"}],
        "options": [{"val": "0", "text": "Kappad, Kozhikode"}, {"val": "1", "text": "Cochin (Kochi)"}, {"val": "2", "text": "Jerónimos Monastery, Lisbon"}],
        "sol": "Landed at Kappad, died in Cochin, and rests in Lisbon's Jerónimos Monastery."
    },
    {
        "type": "Match the Following",
        "q": "Match the Portuguese kings with their relations to Vasco da Gama:",
        "items": [{"left": "King John II"}, {"left": "King Manuel I"}, {"left": "King John III"}],
        "options": [{"val": "0", "text": "Initiated spice route plans but died before launch"}, {"val": "1", "text": "Sponsored first and second voyages"}, {"val": "2", "text": "Appointed Gama as Viceroy in 1524"}],
        "sol": "John II planned the route, Manuel I sponsored 1st and 2nd voyages, and John III appointed Gama Viceroy."
    }
])

# One-Liners
for idx, qtext in enumerate([
    "Why did King John III choose Vasco da Gama to return to India in 1524?",
    "What was the cause of Vasco da Gama's death in Kochi?",
    "Where was Vasco da Gama buried before his remains were taken to Lisbon?",
    "How long did Vasco da Gama serve as Viceroy before his death?",
    "Which governor did Vasco da Gama replace due to administrative corruption?",
    "In which year was Vasco da Gama's body returned to Portugal?",
    "What famous monastery in Lisbon houses Vasco da Gama's tomb today?",
    "What major administrative problem did Gama address as Viceroy?"
]):
    sols = [
        "Why did King John III choose Vasco da Gama to return to India in 1524?",
        "He contracted malaria shortly after his arrival.",
        "St. Francis Church, Fort Kochi.",
        "Approximately three months.",
        "Duarte de Menezes.",
        "1539 CE.",
        "Jerónimos Monastery.",
        "Embezzlement and illegal private trading by Portuguese officers."
    ]
    sec4_en.append({"type": "One-Liner", "q": qtext, "sol": sols[idx]})

# Assertion-Reason
sec4_en.extend([
    {
        "type": "Assertion-Reason",
        "q": "Assertion: King John III sent Vasco da Gama back to India in 1524 CE.\nReason: The Portuguese empire in India was suffering from severe corruption and administrative decay.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "Gama's mission was to restore discipline and secure royal revenues from corrupt officials."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama did not reside in Goa during his viceroyalty.\nReason: He died in Cochin shortly after arriving in India, before he could settle in Goa.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "His sudden death in Cochin cut short his administrative tour of the settlements."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: St. Francis Church in Kochi was built by the British.\nReason: The British controlled Cochin since 1503 CE and constructed the church to honor Vasco da Gama.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "The church was built by the Portuguese in 1503. The British only took control of Cochin much later."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama's final voyage had a commercial rather than administrative purpose.\nReason: He was sent to establish new factories in Bengal and Gujarat.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "The 1524 mission was purely political and administrative, aimed at reform and anti-corruption."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama was buried with royal honors in Portugal in 1539.\nReason: His remains were exhumed and transported from Cochin back to Lisbon.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The return of his remains was a major state event to honor the discoverer of the route."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Gama suspended Duarte de Menezes upon his arrival in India.\nReason: Menezes was accused of embezzling royal spice revenues and abusing his gubernatorial authority.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "Gama acted decisively to arrest and replace corrupt officials immediately."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Vasco da Gama was the first European explorer to die in India.\nReason: Francisco de Almeida and Afonso de Albuquerque both died in Portugal after retirement.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "Albuquerque died in Goa in 1515, and Almeida died in South Africa in 1510. Gama was not the first."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The town of Vasco da Gama in Goa was established during his lifetime.\nReason: He conquered Goa from the Adil Shahi Sultan in 1524 CE.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "The town was named after him much later. Goa was conquered by Albuquerque in 1510, not Gama."
    }
])

# Statement-Based
sec4_en.extend([
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding Vasco da Gama's third voyage:\n1. He arrived with a fleet of 14 ships and extensive administrative powers.\n2. He died in India within three months of landing.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Both statements are historically accurate. He arrived in Sept 1524 and died in Dec 1524."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to Vasco da Gama's burial, consider these statements:\n1. His gravestone can still be seen inside St. Francis Church in Kochi.\n2. His actual remains were moved to Portugal in 1539.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "The empty tomb and gravestone remain a visitor site in Kochi, while the bones are in Lisbon."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:\n1. Vasco da Gama was succeeded as Viceroy by Afonso de Albuquerque.\n2. Gama's reforms successfully eliminated corruption in Portuguese India forever.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 3, "sol": "Albuquerque died in 1515, long before 1524. Corruption returned quickly after Gama's sudden death."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the Portuguese administration in 1524, consider these statements:\n1. The headquarters of the Estado da India was situated at Goa.\n2. Vasco da Gama's administrative jurisdiction extended to Portuguese trade posts in Malacca.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "The capital was Goa, and the Viceroy controlled the entire commercial network from East Africa to Malacca."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding King John III:\n1. He was the son of King Manuel I.\n2. He reversed the monopolistic trade policies of his predecessor.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "He was Manuel's son, but he maintained and intensified the royal monopoly, sending Gama to enforce it."
    }
])

# Open Questions
for idx, qtype in enumerate(["Why", "Why", "Why", "How", "How", "How", "Case Study", "Case Study", "Case Study", "Teach the Concept", "Teach the Concept", "Teach the Concept"]):
    qtexts = [
        "Why was the Portuguese administration in India corrupt by 1524?",
        "Why did King John III choose Vasco da Gama for the viceroyalty over younger candidates?",
        "Why did Cochin remain a key location for Gama's final days instead of Goa?",
        "How did Vasco da Gama deal with Governor Duarte de Menezes in 1524?",
        "How did Vasco da Gama's death impact the administrative reforms he had started?",
        "How was Vasco da Gama's memory preserved in both India and Portugal after his death?",
        "Examine the St. Francis Church in Kochi as a monument of Indo-Portuguese history.",
        "Analyze the role of the Portuguese Viceroyalty as a administrative system under the Crown.",
        "Evaluate the effectiveness of Vasco da Gama's anti-corruption measures.",
        "Explain the administrative differences between a Governor and a Viceroy in Portuguese India.",
        "Describe the geographic scale of the Estado da Índia in 1524.",
        "Explain the significance of the exhumation of Gama's remains in 1539."
    ]
    sols = [
        "Because distance from Lisbon allowed officials to engage in illegal private trade, embezzle crown funds, and abuse their power for personal enrichment.",
        "Because Gama was a national hero with a fearsome reputation for discipline, loyalty to the crown, and ruthlessness, making him ideal for cleaning up the administration.",
        "Cochin was the primary port of arrival and a key center of spice collection. Gama fell ill shortly after arriving in Kochi and died before visiting Goa.",
        "He immediately suspended and arrested Menezes on charges of corruption, ordering him to be sent back to Portugal under arrest.",
        "His reforms were cut short. After his death, corrupt practices and private trading slowly returned among the Portuguese officials.",
        "In India, his empty tomb remains in Kochi, and a town in Goa is named after him. In Portugal, he is interred in Jerónimos Monastery alongside kings.",
        "Built in 1503, it is the oldest European church in India. It holds the gravestone of Vasco da Gama, marking the site of his original burial.",
        "The Viceroy was a direct representative of the King, holding supreme civil and military authority over all Portuguese territories in Asia.",
        "They were highly effective in the short term due to his uncompromising nature, but failed to survive his sudden death due to systemic corruption.",
        "A Viceroy was a royal representative of noble blood, while a Governor was a high official with similar powers but less court prestige.",
        "It was a maritime empire stretching from Sofala and Ormuz in the west, to Goa and Cochin in India, and Malacca in the east.",
        "It marked the recognition of Vasco da Gama's legacy by the crown, bringing his remains to Lisbon as a national symbol of the Age of Discovery."
    ]
    sec4_en.append({"type": qtype, "q": qtexts[idx], "sol": sols[idx]})


# ==================== SECTION 5: GEOPOLITICAL IMPACT ====================
sec5_en = [
    {
        "type": "MCQ",
        "q": "Which ocean did Vasco da Gama's voyages effectively open to European armed commercial navigation?",
        "opts": ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Mediterranean Sea"],
        "ans": 0,
        "sol": "Vasco da Gama's voyage opened the Indian Ocean, shifting global maritime trade patterns."
    },
    {
        "type": "MCQ",
        "q": "The discovery of the Cape Route led to the rapid commercial decline of which European city-state?",
        "opts": ["Venice", "Lisbon", "London", "Amsterdam"],
        "ans": 0,
        "sol": "Venice had a monopoly on Levant spice trade; the Portuguese Cape Route bypassed it, causing Venetian decline."
    },
    {
        "type": "MCQ",
        "q": "What term is used for the Portuguese royal shipping fleet system that traveled between Lisbon and Goa?",
        "opts": ["Carreira da Índia", "Flota de Indias", "Levant Company", "VOC"],
        "ans": 0,
        "sol": "The 'Carreira da Índia' (Run to India) was the annual line of fleets organized by the Portuguese crown."
    },
    {
        "type": "MCQ",
        "q": "How did the Portuguese crown manage the spice trade imports in Lisbon?",
        "opts": ["Through the state department Casa da Índia", "By selling trade rights to the British", "Through the Dutch VOC", "By allowing open free market trading"],
        "ans": 0,
        "sol": "Casa da Índia (House of India) was the crown organization that managed all import monopolies and duties."
    },
    {
        "type": "MCQ",
        "q": "Which empire's revenues were severely impacted by the Portuguese diversion of spice trade from the Red Sea?",
        "opts": ["Mamluk Sultanate of Egypt", "Mughal Empire", "Safavid Empire", "Ottoman Empire"],
        "ans": 0,
        "sol": "The Mamluk Sultanate of Egypt relied on transit taxes on spices. The loss of trade led to their decline and eventual Ottoman conquest."
    },
    # Multi
    {
        "type": "Multiple Correct MCQ",
        "q": "What were the primary geopolitical consequences of Vasco da Gama's maritime breakthrough? (Select all that apply)",
        "opts": ["The shift of trade supremacy from the Mediterranean to the Atlantic", "The decline of Venice and Mamluk Egypt's spice monopolies", "The introduction of militarized mercantilism in the Indian Ocean", "The immediate collapse of the Chinese Ming dynasty"],
        "ans": [0, 1, 2],
        "sol": "Gama's route shifted trade to the Atlantic, hurt Venice/Egypt, and brought naval mercantilism. Ming China was unaffected."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which trade centers suffered economic losses due to the rise of the Portuguese Cape Route? (Select all that apply)",
        "opts": ["Alexandria", "Venice", "Genoa", "Lisbon"],
        "ans": [0, 1, 2],
        "sol": "Alexandria, Venice, and Genoa lost their monopoly on spices. Lisbon, conversely, became extremely wealthy."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "How did the Portuguese enforce their commercial monopoly in the Indian Ocean? (Select all that apply)",
        "opts": ["By seizing strategic choke points like Malacca and Ormuz", "By enforcing the Cartaz licensing system on all local ships", "By destroying competitive merchant shipping through naval warfare", "By signing free-trade agreements with all local kingdoms"],
        "ans": [0, 1, 2],
        "sol": "Monopoly was enforced through choke points, the Cartaz system, and naval gun warfare, not free-trade agreements."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key components of the Portuguese 'Estado da Índia' commercial structure. (Select all that apply)",
        "opts": ["The Casa da Índia in Lisbon", "A network of fortified coastal factories (feitorias)", "The annual Carreira da Índia fleets", "The joint-stock ownership structure of the Dutch model"],
        "ans": [0, 1, 2],
        "sol": "The Estado da India was a crown monopoly system (Casa, factories, fleets), unlike the later joint-stock Dutch and British companies."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What long-term historical processes were initiated by Vasco da Gama's landing in India? (Select all that apply)",
        "opts": ["Direct European colonial expansion in Asia", "Global integration of oceanic trade networks", "The spread of Western Christianity in coastal India", "The instant destruction of the Silk Road land routes"],
        "ans": [0, 1, 2],
        "sol": "Landing initiated colonialism, global trade, and Christian missions. Silk Road routes declined but did not disappear instantly."
    },
    # T/F
    {"type": "True/False", "q": "True or False: The shift of global commerce from the Mediterranean to the Atlantic is called the Commercial Revolution.", "ans": True, "sol": "The opening of ocean routes and expansion of trade is a core part of the Commercial Revolution."},
    {"type": "True/False", "q": "True or False: Venice retained its status as the chief spice supplier of Europe throughout the 16th century.", "ans": False, "sol": "Lisbon replaced Venice as the primary distributor of spices in Western Europe."},
    {"type": "True/False", "q": "True or False: The Portuguese empire in Asia was based on vast land conquests and inland colonization.", "ans": False, "sol": "It was a thalassocracy (maritime empire) based on controlling sea lanes, ports, and choke points."},
    {"type": "True/False", "q": "True or False: The Casa da Índia was a private joint-stock corporation owned by Dutch merchants.", "ans": False, "sol": "It was a Portuguese crown institution that managed the royal spice trade."},
    {"type": "True/False", "q": "True or False: Vasco da Gama's route made Lisbon the richest city in Europe during the early 16th century.", "ans": True, "sol": "The spice monopoly brought immense wealth directly to the Portuguese crown in Lisbon."},
    {"type": "True/False", "q": "True or False: The Mamluk Sultanate of Egypt allied with the Ottoman Empire to fight the Portuguese navy.", "ans": False, "sol": "The Mamluks fought the Portuguese (e.g. Battle of Diu) but were actually conquered by the Ottomans in 1517."},
    {"type": "True/False", "q": "True or False: The discovery of the sea route directly linked Europe to the spices of the Moluccas.", "ans": True, "sol": "Opening the route to India led directly to Portuguese expansion into Malacca and the Spice Islands (Moluccas)."},
    {"type": "True/False", "q": "True or False: The Silk Road land trade route was completely closed by the Chinese because of the Portuguese sea route.", "ans": False, "sol": "The land route became less competitive but remained active; it was not closed by China."}
]

# Fill Blanks
for idx, qtext in enumerate([
    "The transition of trade centers from Mediterranean to Atlantic ports is part of the __________ Revolution.",
    "The Portuguese royal trading organization in Lisbon was the Casa da __________.",
    "The annual maritime route between Lisbon and Goa was called the Carreira da __________.",
    "The Italian city-state of __________ lost its monopoly on spice distribution.",
    "The Portuguese established a maritime empire known as a __________ rather than land empire.",
    "The Mamluk Sultanate of __________ was devastated by the loss of spice transit taxes.",
    "The Portuguese spice trade was managed as a crown __________ rather than free trade.",
    "The capture of the port of __________ in 1511 secured the route to the Pacific."
]):
    ans_list = ["Commercial", "India", "India", "Venice", "thalassocracy", "Egypt", "monopoly", "Malacca"]
    sec5_en.append({
        "type": "Fill in the Blank",
        "q": qtext,
        "ans": ans_list[idx],
        "sol": "Identifies key terms related to the geopolitical impact."
    })

# Match
sec5_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the trade regions with their dominant commercial centers in 1500:",
        "items": [{"left": "Levant trade"}, {"left": "Cape trade route"}, {"left": "Baltic trade"}],
        "options": [{"val": "0", "text": "Venice and Alexandria"}, {"val": "1", "text": "Lisbon (Casa da Índia)"}, {"val": "2", "text": "Hanseatic League ports"}],
        "sol": "Levant was Venice/Alexandria, Cape route was Lisbon, and Baltic was Hanseatic League."
    },
    {
        "type": "Match the Following",
        "q": "Match the geographic choke points with their strategic water bodies:",
        "items": [{"left": "Ormuz"}, {"left": "Malacca"}, {"left": "Aden"}],
        "options": [{"val": "0", "text": "Persian Gulf entrance"}, {"val": "1", "text": "Strait between Sumatra and Malaya"}, {"val": "2", "text": "Red Sea entrance"}],
        "sol": "Ormuz controls Persian Gulf, Malacca controls the eastern strait, and Aden controls the Red Sea."
    },
    {
        "type": "Match the Following",
        "q": "Match the empires with the impact of Vasco da Gama's discoveries on them:",
        "items": [{"left": "Mamluk Empire"}, {"left": "Portuguese Empire"}, {"left": "Venetian Republic"}],
        "options": [{"val": "0", "text": "Financial collapse and Ottoman conquest"}, {"val": "1", "text": "Rise as a global maritime thalassocracy"}, {"val": "2", "text": "Gradual loss of monopoly over Levant spices"}],
        "sol": "Mamluks collapsed, Portuguese rose to thalassocracy, and Venice lost its Levant monopoly."
    }
])

# One-Liners
for idx, qtext in enumerate([
    "Define the term 'thalassocracy' in the context of the Portuguese Empire.",
    "What was the role of the 'Casa da Índia' in Lisbon?",
    "Why did Venetian spice trade decline after 1498?",
    "What is the significance of the Battle of Diu (1509)?",
    "Which European nation became the main distributor of spices in Northern Europe after Portugal?",
    "What was the annual shipping network between Lisbon and Goa called?",
    "How did Mamluk Egypt react to Portuguese encroachment in the Indian Ocean?",
    "What strategic choke point controlled access to the Persian Gulf?"
]):
    sols = [
        "A maritime empire based on control of sea lanes and ports rather than land territories.",
        "It was the government department that managed royal monopolies on imports and customs.",
        "Because the Cape Route delivered spices directly to Europe, bypassing Venice.",
        "It established Portuguese naval supremacy over combined Mamluk-Gujarati fleets.",
        "The Netherlands (Antwerp/Amsterdam became key distribution centers).",
        "Carreira da Índia.",
        "They sent a fleet to attack the Portuguese, leading to the Battle of Diu.",
        "Ormuz."
    ]
    sec5_en.append({"type": "One-Liner", "q": qtext, "sol": sols[idx]})

# Assertion-Reason
sec5_en.extend([
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The center of gravity of European commerce shifted to Atlantic ports in the 16th century.\nReason: Vasco da Gama's discovery of the Cape Route allowed direct oceanic trade with Asia, bypassing Mediterranean ports.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The assertion is correct and the reason explain the shift to Lisbon and Antwerp."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Portuguese empire did not attempt to conquer the interior of India.\nReason: Their military resources were limited, and their economic goal was controlling maritime trade routes, not agriculture.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The thalassocratic model relied on sea power and coastal factories rather than land conquests."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: Venice and Mamluk Egypt formed an alliance to fight the Portuguese in the Indian Ocean.\nReason: Both states suffered severe revenue losses due to the diversion of the spice trade to the Cape Route.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The economic impact united traditional rivals in Egypt and Italy against the Portuguese."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Portuguese spice monopoly was run as a free-market enterprise.\nReason: The Portuguese crown allowed private English and French merchants to buy spices directly in Goa.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "It was a royal monopoly (monopólio régio). Foreign ships were strictly excluded from trading directly."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Battle of Diu in 1509 CE secured Portuguese dominance for a century.\nReason: It resulted in the destruction of the combined Muslim naval fleet, establishing Portuguese supremacy.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The victory at Diu eliminated organized naval resistance to Portuguese hegemony."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Cape Route was safer than the overland Silk Road.\nReason: Overland routes faced constant threats from wars, bandits, and heavy taxes by regional rulers.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The ocean route was long but avoided multiple transshipment costs and political instability."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Ottomans conquered Egypt in 1517 CE partly due to Mamluk weakness.\nReason: The Mamluk treasury was bankrupt due to the loss of transit duties on the spice trade.",
        "opts": EN_AR_OPTS, "ans": 0, "sol": "The economic drain caused by the Portuguese blockade weakened the Mamluks, allowing Ottoman conquest."
    },
    {
        "type": "Assertion-Reason",
        "q": "Assertion: The Dutch VOC copied the Portuguese crown monopoly system exactly.\nReason: The Dutch crown owned all shares of the VOC and managed its Asian factories directly.",
        "opts": EN_AR_OPTS, "ans": 3, "sol": "The Dutch VOC was a private joint-stock company, unlike the Portuguese crown-owned system."
    }
])

# Statement-Based
sec5_en.extend([
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the Commercial Revolution:\n1. It led to the rise of joint-stock companies in Spain and Portugal first.\n2. It shifted the financial capital of Europe from Italy to the Low Countries (Antwerp/Amsterdam).\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Spain and Portugal relied on crown monopolies. Joint-stock models arose in England and Netherlands. Capital did shift to northern Europe."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the thalassocratic empire, consider these statements:\n1. It focuses on control of naval pathways and strategic coastal fortresses.\n2. The Portuguese Estado da India did not claim sovereignty over the open sea.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 0, "sol": "They did claim absolute sovereignty over the Indian Ocean (Mare Clausum) and forced all ships to carry Cartaz."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements:\n1. The Portuguese route entirely destroyed the overland Silk Road trade by 1550.\n2. Levant spice imports in Venice actually recovered in the late 16th century.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 1, "sol": "Overland trade survived. Venice saw a partial recovery in spice trade later due to Portuguese corruption and Ottoman protection."
    },
    {
        "type": "Statement-Based",
        "q": "With reference to the Casa da India, consider these statements:\n1. It was established in Lisbon to regulate overseas trade.\n2. It fixed the selling prices of pepper and spices in Europe.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "The Casa was the center of the royal monopoly, handling logistics, duties, and price-fixing."
    },
    {
        "type": "Statement-Based",
        "q": "Consider the following statements regarding the Portuguese naval strategy:\n1. It relied on securing key choke points like Aden, Ormuz, and Malacca.\n2. The Portuguese failed to capture Aden, leaving the Red Sea route partially vulnerable.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": 2, "sol": "Albuquerque captured Ormuz and Malacca but failed to take Aden, which allowed some Levant trade to persist."
    }
])

# Open Questions
for idx, qtype in enumerate(["Why", "Why", "Why", "How", "How", "How", "Case Study", "Case Study", "Case Study", "Teach the Concept", "Teach the Concept", "Teach the Concept"]):
    qtexts = [
        "Why did the discovery of the Cape Route lead to the decline of Venice?",
        "Why did the Portuguese establish a maritime thalassocracy instead of a land-based empire in Asia?",
        "Why was the control of choke points like Ormuz and Malacca critical to the Portuguese monopoly?",
        "How did the Portuguese crown organize and fund the annual fleets (Carreira da India)?",
        "How did the diversion of spice trade impact the Mamluk Sultanate of Egypt?",
        "How did Northern European cities like Antwerp benefit from Portuguese discoveries?",
        "Analyze the Battle of Diu (1509) as a turning point in global naval history.",
        "Examine the functioning of the Casa da India as a model of early modern mercantilism.",
        "Evaluate the concept of 'Mare Clausum' (Closed Sea) enforced by the Portuguese.",
        "Explain the term 'Thalassocracy' to a beginner, using the Portuguese empire as an example.",
        "Describe how the Portuguese Cape Route impacted Venice's overland connections.",
        "Explain why Portugal failed to maintain its monopoly in the face of Dutch competition."
    ]
    sols = [
        "Venice relied on trade through Egypt and the Levant. The direct sea route bypassed these areas, allowing Portugal to sell spices cheaper in Western Europe.",
        "They lacked the manpower and army to conquer large land empires like Vijayanagara or the Deccan Sultanates. Controlling key ports and sea routes was far more profitable and sustainable.",
        "These ports were narrow straits that acted as gateways for Indian Ocean shipping. Controlling them allowed the Portuguese to block competitor vessels and enforce the Cartaz system.",
        "The crown financed the fleets, commissioned royal ships, and controlled the logistics. They also allowed private merchants to purchase cargo space in exchange for duties.",
        "It deprived the Mamluk treasury of vital tax revenues from spice transit, causing a severe economic crisis that contributed to their conquest by the Ottoman Empire in 1517.",
        "Antwerp became the primary distribution center where Portuguese spices were sold to Northern European markets, boosting its financial sector.",
        "The victory established Portuguese naval supremacy over combined Mamluk, Gujarati, and Ottoman fleets, securing European control of Indian Ocean trade routes.",
        "It was the royal warehouse and customs house that held a monopoly on spice sales, managed shipping logs, and processed all incoming treasures.",
        "It was the legal claim that Portugal owned the Indian Ocean and had the right to seize any foreign vessel that did not purchase a license.",
        "A thalassocracy is an empire based on naval supremacy. Instead of conquering land, Portugal built small forts in ports like Goa, Cochin, and Ormuz to control sea lanes.",
        "It cut off the Venetian brokers from their traditional sources, forcing them to buy spices at higher rates or wait for erratic caravan routes.",
        "The Dutch VOC was a private corporation with superior funding, larger fleets, and joint-stock efficiency, whereas the Portuguese crown monopoly suffered from corruption and royal debt."
    ]
    sec5_en.append({"type": qtype, "q": qtexts[idx], "sol": sols[idx]})


# ==================== TRANSLATE SECTIONS TO HINDI ====================
def translate_opts(opts):
    mapping = {
        "Both A and R are true and R is the correct explanation of A": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
        "Both A and R are true but R is not the correct explanation of A": "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
        "A is true but R is false": "A सही है लेकिन R गलत है",
        "A is false but R is true": "A गलत है लेकिन R सही है",
        "1 only": "केवल 1",
        "2 only": "केवल 2",
        "Both 1 and 2": "1 और 2 दोनों",
        "Neither 1 nor 2": "न तो 1 न ही 2"
    }
    return [mapping.get(o, o) for o in opts]

def translate_section(sec_en, title_mapping):
    sec_hi = []
    for q in sec_en:
        q_hi = q.copy()
        q_hi["q"] = title_mapping.get(q["q"], q["q"])
        if "opts" in q:
            q_hi["opts"] = translate_opts([title_mapping.get(o, o) for o in q["opts"]])
        if "ans" in q:
            if isinstance(q["ans"], str):
                q_hi["ans"] = title_mapping.get(q["ans"], q["ans"])
        if "sol" in q:
            q_hi["sol"] = title_mapping.get(q["sol"], q["sol"])
        if "items" in q:
            q_hi["items"] = [{"left": title_mapping.get(item["left"], item["left"])} for item in q["items"]]
        if "options" in q:
            q_hi["options"] = [{"val": opt["val"], "text": title_mapping.get(opt["text"], opt["text"])} for opt in q["options"]]
        sec_hi.append(q_hi)
    return sec_hi

local_dict = {
    "Which ship served as Vasco da Gama's flagship during his historic first voyage to India in 1497-1499 CE?": "1497-1499 ईस्वी में भारत की ऐतिहासिक पहली यात्रा के दौरान वास्को डी गामा के ध्वजपोत (फ्लैगशिप) के रूप में किस जहाज ने काम किया था?",
    "São Gabriel": "साओ गेब्रियल (São Gabriel)", "São Rafael": "साओ राफेल (São Rafael)", "Bérrio": "बेरियो (Bérrio)", "São Miguel": "साओ मिगुएल (São Miguel)",
    "The São Gabriel was the flagship, commanded by Vasco da Gama himself. His brother Paulo commanded the São Rafael.": "साओ गेब्रियल ध्वजपोत था, जिसकी कमान स्वयं वास्को डी गामा के पास थी। उनके भाई पाउलो ने साओ राफेल की कमान संभाली थी।",
    "Who was the legendary pilot who guided Vasco da Gama's fleet from Malindi across the Arabian Sea to Calicut?": "उस प्रसिद्ध नाविक का नाम क्या था जिसने वास्को डी गामा के बेड़े को मालिंदी से अरब सागर पार कराकर कालीकट तक पहुँचाया?",
    "Ahmad Ibn Mājid": "अहमद इब्न मजीद", "Al-Masudi": "अल-मसूदी", "Ibn Battuta": "इब्न बतूता", "Al-Idrisi": "अल-इदरीसी",
    "Ahmad Ibn Mājid (often identified as a Gujarati or Arab navigator) guided the fleet using his expertise of monsoon winds.": "अहमद इब्न मजीद (अक्सर एक गुजराती या अरब नाविक के रूप में पहचाने जाने वाले) ने मानसून हवाओं के ज्ञान का उपयोग करके बेड़े का मार्गदर्शन किया।",
    "Which Portuguese monarch sponsored and commissioned Vasco da Gama's first voyage to find a direct sea route to India?": "किस पुर्तगाली सम्राट ने भारत के लिए सीधा समुद्री मार्ग खोजने के लिए वास्को डी गामा की पहली यात्रा को प्रायोजित किया था?",
    "King Manuel I": "राजा मैनुअल प्रथम", "King John II": "राजा जॉन द्वितीय", "Prince Henry the Navigator": "प्रिंस हेनरी द नेविगेटर", "King Afonso V": "राजा अफोंसो पंचम",
    "King Manuel I ('The Fortunate') sponsored the voyage. King John II had made initial plans but died before execution.": "राजा मैनुअल प्रथम ('द फॉर्च्युनेट') ने इस यात्रा को प्रायोजित किया था। राजा जॉन द्वितीय ने प्रारंभिक योजनाएँ बनाई थीं लेकिन क्रियान्वयन से पहले उनका निधन हो गया था।",
    "Where exactly did Vasco da Gama first set foot on Indian soil in May 1498 CE?": "मई 1498 ईस्वी में वास्को डी गामा ने पहली बार भारतीय धरती पर कहाँ कदम रखा था?",
    "Kappad near Calicut": "कालीकट के पास कप्पड़", "Cochin beach": "कोचीन तट", "Anjadip Island": "अंजादीप द्वीप", "Dona Paula beach, Goa": "डोना पाउला तट, गोवा",
    "Vasco da Gama landed at Kappad beach, located about 15 km north of Calicut (Kozhikode).": "वास्को डी गामा कालीकट (कोझिकोड) से लगभग 15 किमी उत्तर में स्थित कप्पड़ तट पर उतरे थे।",
    "What major disaster befell Vasco da Gama's fleet on the return journey from India to Portugal?": "भारत से पुर्तगाल की वापसी यात्रा पर वास्को डी गामा के बेड़े पर कौन सी बड़ी आपदा आई थी?",
    "Destruction of São Rafael due to crew loss from scurvy": "स्कर्वी के कारण चालक दल की कमी से साओ राफेल का विनाश", "Total loss of spice cargo in a storm near Madagascar": "मेडागास्कर के पास एक तूफान में मसाले के कार्गो का पूर्ण नुकसान", "Capture of the flagship by Arab pirates off Mombasa": "मोम्बासा के पास अरब समुद्री लुटेरों द्वारा ध्वजपोत पर कब्जा", "Mutiny by Nicolau Coelho": "निकोलाउ कोएल्हो द्वारा विद्रोह",
    "Scurvy decimated the crew on the return leg, forcing Gama to burn the São Rafael near East Africa due to a lack of sailors.": "वापसी के दौरान स्कर्वी ने चालक दल को तबाह कर दिया, जिससे गामा को नाविकों की कमी के कारण पूर्वी अफ्रीका के पास साओ राफेल को जलाने के लिए मजबूर होना पड़ा।",
    "What was the hereditary title held by the Hindu ruler of Calicut who received Vasco da Gama in 1498 CE?": "कालीकट के उस हिंदू शासक की वंशानुगत उपाधि क्या थी जिसने 1498 ईस्वी में वास्को डी गामा का स्वागत किया था?",
    "Zamorin (Samudiri)": "ज़मोरिन (समुद्रि/सामुदिरी)", "Adil Shah": "आदिल शाह", "Kolathiri": "कोलाथिरि", "Nayaka": "नायक",
    "The ruler of Calicut held the title Zamorin, a Portuguese corruption of the Malayalam word 'Samudiri' meaning Lord of the Sea.": "कालीकट के शासक के पास ज़मोरिन की उपाधि थी, जो मलयालम शब्द 'सामुदिरी' (समुद्र का स्वामी) का पुर्तगाली अपभ्रंश है।",
    "How did the Zamorin of Calicut react to the gifts presented by Vasco da Gama during their first audience?": "कालीकट के ज़मोरिन ने अपनी पहली मुलाकात के दौरान वास्को डी गामा द्वारा प्रस्तुत उपहारों पर क्या प्रतिक्रिया दी थी?",
    "He was disappointed and unimpressed by their low quality": "वे उनकी कम गुणवत्ता से निराश हुए और बिल्कुल भी प्रभावित नहीं हुए", "He immediately accepted them as high tribute": "उन्होंने तुरंत उन्हें उच्च श्रद्धांजलि के रूप में स्वीकार कर लिया", "He imprisoned Gama for insulting the crown": "उन्होंने मुकुट का अपमान करने के लिए गामा को जेल में डाल दिया", "He traded them for gold coins": "उन्होंने सोने के सिक्कों के लिए उनका व्यापार किया",
    "The gifts (hats, cloth, sugar, honey) were cheap merchant items. The Zamorin and his court ridiculed them as unfit for a king.": "उपहार (टोपी, कपड़ा, चीनी, शहद) सस्ते व्यापारिक सामान थे। ज़मोरिन और उनके दरबार ने उन्हें एक राजा के लिए अनुपयुक्त बताकर उनका मज़ाक उड़ाया।",
    "Which faction of merchants in Calicut strongly opposed Vasco da Gama and tried to sabotage his trade negotiations?": "कालीकट में व्यापारियों के किस गुट ने वास्को डी गामा का कड़ा विरोध किया और उनकी व्यापारिक वार्ताओं को विफल करने का प्रयास किया?",
    "Arab and Muslim merchants": "अरब और मुस्लिम व्यापारी", "Gujarati Bania merchants": "Gujarati Bania merchants", "Chinese junk traders": "चीनी जंक व्यापारी", "Syrian Christian traders": "सीरियाई ईसाई व्यापारी",
    "Arab merchants held a monopoly on spice exports in Calicut and rightly feared Portuguese naval armed competition.": "अरब व्यापारियों का कालीकट में मसाला निर्यात पर एकाधिकार था और वे पुर्तगाली नौसैनिक सशस्त्र प्रतिस्पर्धा से आशंकित थे।",
    "What did the Zamorin demand from Vasco da Gama before allowing him to depart Calicut with his cargo?": "ज़मोरिन ने वास्को डी गामा से अपना माल लेकर कालीकट से जाने देने से पहले क्या मांग की थी?",
    "Payment of port customs duties in gold/silver": "सोने/चांदी में बंदरगाह सीमा शुल्क का भुगतान", "Surrender of the flagship São Gabriel": "ध्वजपोत साओ गेब्रियल का आत्मसमर्पण", "Conversion of the Portuguese crew to Hinduism": "पुर्तगाली चालक दल का हिंदू धर्म में परिवर्तन", "An alliance against the ruler of Cochin": "कोचीन के शासक के खिलाफ गठबंधन",
    "The Zamorin demanded standard port customs duties. Gama refused, claiming exemption as an ambassador, leading to a standoff.": "ज़मोरिन ने मानक बंदरगाह सीमा शुल्क की मांग की थी। गामा ने एक राजदूत के रूप में छूट का दावा करते हुए इनकार कर दिया, जिससे गतिरोध पैदा हो गया।",
    "How did Vasco da Gama retaliate when the Zamorin temporarily detained some Portuguese factors and goods?": "जब ज़मोरिन ने अस्थायी रूप से कुछ पुर्तगाली एजेंटों और सामानों को हिरासत में लिया, तो वास्को डी गामा ने क्या जवाबी कार्रवाई की?",
    "He seized local hostages and sailed away with them": "उन्होंने स्थानीय लोगों को बंधक बना लिया और उन्हें अपने साथ ले गए", "He launched a full naval invasion of Calicut city": "उन्होंने कालीकट शहर पर पूर्ण नौसैनिक आक्रमण शुरू कर दिया", "He paid the custom duties double in value": "उन्होंने सीमा शुल्क का दोगुना भुगतान किया", "He burned down the local temple": "उन्होंने स्थानीय मंदिर को जला दिया",
    "To force the release of his men and goods, Gama captured several Calicut citizens and took them back to Lisbon.": "अपने लोगों और सामानों की रिहाई के लिए मजबूर करने के लिए, गामा ने कालीकट के कई नागरिकों को पकड़ लिया और उन्हें लिस्बन ले गए।",
    "In which year did Vasco da Gama return to India for his highly militarized second voyage?": "वास्को डी गामा अपनी अत्यधिक सैन्यीकृत दूसरी यात्रा के लिए किस वर्ष भारत लौटे थे?",
    "1502 CE": "1502 ईस्वी", "1500 CE": "1500 ईस्वी", "1505 CE": "1505 ईस्वी", "1510 CE": "1510 ईस्वी",
    "Vasco da Gama returned in 1502 CE with a fleet of 20 heavily armed ships to establish dominance.": "वास्को डी गामा 1502 ईस्वी में अपना प्रभुत्व स्थापित करने के लिए 20 भारी सशस्त्र जहाजों के बेड़े के साथ लौटे थे।",
    "Which explorer commanded the intermediate Portuguese expedition to India (1500 CE) between Gama's first and second voyages?": "गामा की पहली और दूसरी यात्राओं के बीच भारत के लिए मध्यवर्ती पुर्तगाली अभियान (1500 ईस्वी) की कमान किस खोजकर्ता ने संभाली थी?",
    "Pedro Álvares Cabral": "पेड्रो अल्वारेस कैब्राल", "Bartolomeu Dias": "बार्टोलोमेउ डियास", "Francisco de Almeida": "फ्रांसिस्को डी अल्मेडा", "Afonso de Albuquerque": "अल्फांसो डी अल्बुकर्क",
    "Pedro Álvares Cabral commanded the second Portuguese expedition in 1500, discovering Brazil along the way.": "पेड्रो अल्वारेस कैब्राल ने 1500 में दूसरे पुर्तगाली अभियान की कमान संभाली और रास्ते में ब्राजील की खोज की।",
    "With which regional rival of the Zamorin did Vasco da Gama establish a crucial alliance during his second voyage?": "वास्को डी गामा ने अपनी दूसरी यात्रा के दौरान ज़मोरिन के किस क्षेत्रीय प्रतिद्वंद्वी के साथ एक महत्वपूर्ण गठबंधन स्थापित किया था?",
    "The Raja of Cochin (Kochi)": "कोचीन के राजा (कोच्चि)", "The Sultan of Bijapur": "बीजापुर के सुल्तान", "The Kolathiri of Kannur": "कन्नूर के कोलाथिरी", "The King of Vijayanagara": "विजयनगर के राजा",
    "Gama allied with the Raja of Cochin, who welcomed the Portuguese to counter Calicut's hegemony.": "गामा ने कोचीन के राजा के साथ गठबंधन किया, जिन्होंने कालीकट के आधिपत्य का मुकाबला करने के लिए पुर्तगालियों का स्वागत किया।",
    "What violent act did Vasco da Gama commit against Calicut during his second voyage in 1502 CE?": "वास्को डी गामा ने 1502 ईस्वी में अपनी दूसरी यात्रा के दौरान कालीकट के खिलाफ कौन सा हिंसक कार्य किया था?",
    "He bombarded the city and destroyed Calicut's merchant fleet": "उन्होंने शहर पर बमबारी की और कालीकट के व्यापारिक बेड़े को नष्ट कर दिया", "He captured and occupied the Zamorin's palace": "उन्होंने ज़मोरिन के महल पर कब्जा कर लिया", "He executed the Zamorin during negotiations": "उन्होंने बातचीत के दौरान ज़मोरिन को मार डाला", "He poisoned the city's water supply": "उन्होंने शहर की जलापूर्ति को जहरीला बना दिया",
    "Gama bombarded Calicut, captured merchant ships, and cut off the ears and hands of captured sailors to terrify the Zamorin.": "गामा ने कालीकट पर बमबारी की, व्यापारिक जहाजों पर कब्जा कर लिया और ज़मोरिन को डराने के लिए पकड़े गए नाविकों के कान और हाथ काट दिए।",
    "Where did Vasco da Gama establish the first permanent Portuguese factory (trading post) in India during his second expedition?": "वास्को डी गामा ने अपने दूसरे अभियान के दौरान भारत में पहली स्थायी पुर्तगाली फैक्ट्री (व्यापारिक चौकी) कहाँ स्थापित की थी?",
    "Cochin (Kochi)": "कोचीन (कोच्चि)", "Calicut": "कालीकट", "Goa": "गोवा", "Pulicat": "पुलिकट",
    "He established the first factory at Cochin in 1503 (completed after his arrival/alliance), which became their first headquarters.": "उन्होंने 1503 में कोचीन में पहली फैक्ट्री स्थापित की (उनके आगमन/गठबंधन के बाद पूरी हुई), जो उनका पहला मुख्यालय बन गया।",
    "In which year did Vasco da Gama return to India for his third and final voyage?": "वास्को डी गामा अपनी तीसरी और अंतिम यात्रा के लिए किस वर्ष भारत लौटे थे?",
    "1524 CE": "1524 ईस्वी", "1515 CE": "1515 ईस्वी", "1530 CE": "1530 ईस्वी", "1508 CE": "1508 ईस्वी",
    "Vasco da Gama was sent back to India in 1524 CE by King John III.": "वास्को डी गामा को 1524 ईस्वी में राजा जॉन तृतीय द्वारा भारत वापस भेजा गया था।",
    "What official title was bestowed upon Vasco da Gama for his third voyage to India in 1524 CE?": "1524 ईस्वी में वास्को डी गामा को भारत की तीसरी यात्रा के लिए कौन सी आधिकारिक उपाधि दी गई थी?",
    "Viceroy of India": "भारत के वायसराय", "Captain-Major of the Seas": "समुद्र के कैप्टन-मेजर", "Governor of Goa": "गोवा के गवर्नर", "High Commissioner of Cochin": "कोचीन के उच्चायुक्त",
    "He was appointed the second Viceroy of India (following Francisco de Almeida and Albuquerque, who were Governors/Viceroys).": "उन्हें भारत का दूसरा वायसराय नियुक्त किया गया था (फ्रांसिस्को डी अल्मेडा और अल्बुकर्क के बाद, जो गवर्नर/वायसराय थे)।",
    "Who was the Portuguese King who appointed Vasco da Gama as Viceroy in 1524 CE?": "1524 ईस्वी में वास्को डी गामा को वायसराय नियुक्त करने वाला पुर्तगाली राजा कौन था?",
    "King John III": "राजा जॉन तृतीय", "King Manuel I": "राजा मैनुअल प्रथम", "King Sebastian": "राजा सेबस्टियन", "King Afonso VI": "राजा अफोंसो VI",
    "King John III succeeded King Manuel I and appointed Gama to clean up the corrupt administration.": "राजा जॉन तृतीय ने राजा मैनुअल प्रथम का उत्तराधिकार संभाला और भ्रष्ट प्रशासन को साफ करने के लिए गामा को नियुक्त किया।",
    "What was the primary administrative objective of Vasco da Gama's final mission to India?": "भारत में वास्को डी गामा के अंतिम मिशन का प्राथमिक प्रशासनिक उद्देश्य क्या था?",
    "To curb rampant corruption among Portuguese officials": "पुर्तगाली अधिकारियों के बीच बड़े पैमाने पर फैले भ्रष्टाचार पर लगाम लगाना", "To conquer the Kingdom of Vijayanagara": "विजयनगर साम्राज्य पर विजय प्राप्त करना", "To shift the capital from Goa to Cochin": "राजधानी को गोवा से कोचीन स्थानांतरित करना", "To convert the Zamorin to Christianity": "ज़मोरिन को ईसाई धर्म में परिवर्तित करना",
    "The Portuguese administration in India had become highly corrupt. Gama was sent as a strict disciplinarian to restore order.": "भारत में पुर्तगाली प्रशासन अत्यधिक भ्रष्ट हो गया था। व्यवस्था बहाल करने के लिए गामा को एक सख्त अनुशासक के रूप में भेजा गया था।",
    "Where in India did Vasco da Gama die on Christmas Eve, 1524 CE?": "क्रिसमस की पूर्व संध्या (Christmas Eve), 1524 ईस्वी में भारत में वास्को डी गामा की मृत्यु कहाँ हुई थी?",
    "Cochin (Kochi)": "कोचीन (कोच्चि)", "Goa": "गोवा", "Calicut": "कालीकट", "Diu": "दीव",
    "Vasco da Gama contracted malaria and died in Cochin on December 24, 1524.": "वास्को डी गामा मलेरिया से पीड़ित हो गए और 24 दिसंबर 1524 को कोचीन में उनका निधन हो गया।",
    "Which ocean did Vasco da Gama's voyages effectively open to European armed commercial navigation?": "वास्को डी गामा की यात्राओं ने किस महासागर को यूरोपीय सशस्त्र व्यापारिक नौवहन के लिए प्रभावी ढंग से खोल दिया?",
    "Indian Ocean": "हिंद महासागर", "Atlantic Ocean": "अटलांटिक महासागर", "Pacific Ocean": "प्रशांत महासागर", "Mediterranean Sea": "भूमध्य सागर",
    "Vasco da Gama's voyage opened the Indian Ocean, shifting global maritime trade patterns.": "वास्को डी गामा की यात्रा ने हिंद महासागर का मार्ग खोल दिया, जिससे वैश्विक समुद्री व्यापार का ढांचा बदल गया।",
    "The discovery of the Cape Route led to the rapid commercial decline of which European city-state?": "केप मार्ग की खोज से किस यूरोपीय नगर-राज्य का तेजी से व्यावसायिक पतन हुआ?",
    "Venice": "वेनिस", "Lisbon": "लिस्बन", "London": "लंदन", "Amsterdam": "एम्स्टर्डम",
    "Venice had a monopoly on Levant spice trade; the Portuguese Cape Route bypassed it, causing Venetian decline.": "वेनिस का लेवंत मसाला व्यापार पर एकाधिकार था; पुर्तगाली केप मार्ग ने इसे बायपास कर दिया, जिससे वेनिस का पतन हुआ।",
    "What term is used for the Portuguese royal shipping fleet system that traveled between Lisbon and Goa?": "लिस्बन और गोवा के बीच यात्रा करने वाले पुर्तगाली शाही जहाजरानी बेड़े की प्रणाली के लिए किस शब्द का उपयोग किया जाता है?",
    "Carreira da Índia": "कैरियर दा इंडिया (Carreira da Índia)", "Flota de Indias": "फ्लोटा डी इंडियास", "Levant Company": "लेवंत कंपनी", "VOC": "वीओसी (VOC)",
    "The 'Carreira da Índia' (Run to India) was the annual line of fleets organized by the Portuguese crown.": "'कैरियर दा इंडिया' (भारत की यात्रा) पुर्तगाली क्राउन द्वारा आयोजित जहाजों का वार्षिक बेड़ा था।",
    "How did the Portuguese crown manage the spice trade imports in Lisbon?": "पुर्तगाली क्राउन ने लिस्बन में मसाला व्यापार आयात का प्रबंधन कैसे किया?",
    "Through the state department Casa da Índia": "राज्य विभाग कासा दा इंडिया (Casa da Índia) के माध्यम से", "By selling trade rights to the British": "अंग्रेजों को व्यापारिक अधिकार बेचकर", "Through the Dutch VOC": "डच वीओसी के माध्यम से", "By allowing open free market trading": "खुले मुक्त बाजार व्यापार की अनुमति देकर",
    "Casa da Índia (House of India) was the crown organization that managed all import monopolies and duties.": "कासा दा इंडिया (हाउस ऑफ इंडिया) एक शाही संगठन था जो सभी आयात एकाधिकार और करों का प्रबंधन करता था।",
    "Which empire's revenues were severely impacted by the Portuguese diversion of spice trade from the Red Sea?": "लाल सागर से मसाला व्यापार के पुर्तगाली मार्ग परिवर्तन से किस साम्राज्य के राजस्व पर गंभीर प्रभाव पड़ा?",
    "Mamluk Sultanate of Egypt": "मिस्र का ममलुक सल्तनत", "Mughal Empire": "मुगल साम्राज्य", "Safavid Empire": "सफाविद साम्राज्य", "Ottoman Empire": "ओटोमन साम्राज्य",
    "The Mamluk Sultanate of Egypt relied on transit taxes on spices. The loss of trade led to their decline and eventual Ottoman conquest.": "मिस्र का ममलुक सल्तनत मसालों पर पारगमन करों पर निर्भर था। व्यापार के नुकसान से उनका पतन हुआ और अंततः ओटोमन्स ने उन पर विजय प्राप्त कर ली।"
}

sec1_hi = translate_section(sec1_en, local_dict)
sec2_hi = translate_section(sec2_en, local_dict)
sec3_hi = translate_section(sec3_en, local_dict)
sec4_hi = translate_section(sec4_en, local_dict)
sec5_hi = translate_section(sec5_en, local_dict)

generate_sec_file("section1", sec1_en, sec1_hi)
generate_sec_file("section2", sec2_en, sec2_hi)
generate_sec_file("section3", sec3_en, sec3_hi)
generate_sec_file("section4", sec4_en, sec4_hi)
generate_sec_file("section5", sec5_en, sec5_hi)


# ==================== 50 COMPLETELY UNIQUE PRACTICE QUESTIONS ====================
practice_pool_en = [
    # 1-10
    ("In which year did Vasco da Gama first reach India?", "1498 CE", ["1498 CE", "1502 CE", "1492 CE", "1510 CE"], "He landed at Kappad near Calicut in May 1498."),
    ("Who was the Portuguese King during Gama's first voyage?", "King Manuel I", ["King Manuel I", "King John III", "King Sebastian", "King Afonso V"], "King Manuel I sponsored and funded the historic voyage."),
    ("Which Malabar port welcomed the Portuguese and formed the first factory alliance?", "Cochin", ["Cochin", "Calicut", "Goa", "Surat"], "Cochin formed a secure alliance and factory with the Portuguese."),
    ("What was the flagship of Vasco da Gama's first fleet?", "São Gabriel", ["São Gabriel", "São Rafael", "Bérrio", "São Salvador"], "The São Gabriel was commanded directly by Vasco da Gama."),
    ("Which disease was the leading cause of death during the first voyage?", "Scurvy", ["Scurvy", "Malaria", "Cholera", "Yellow Fever"], "Scurvy resulted from lack of Vitamin C on long voyages."),
    ("Who commanded the intermediate Portuguese fleet of 1500 CE?", "Pedro Álvares Cabral", ["Pedro Álvares Cabral", "Afonso de Albuquerque", "Francisco de Almeida", "Vasco da Gama"], "Pedro Álvares Cabral led the second voyage and discovered Brazil."),
    ("What pilgrim ship was captured and burned by Vasco da Gama in 1502 CE?", "Miri", ["Miri", "São Rafael", "Flor de la Mar", "Santa Maria"], "Gama plundered and burned the ship Miri with over 300 passengers."),
    ("What title did Vasco da Gama receive on his third voyage in 1524 CE?", "Viceroy of India", ["Viceroy of India", "Governor-General", "Admiral of the Seas", "High Commissioner"], "Gama was appointed the second Viceroy of India in 1524 by King John III."),
    ("Where in India did Vasco da Gama pass away in 1524 CE?", "Cochin", ["Cochin", "Goa", "Calicut", "Diu"], "Gama died of malaria in Cochin on Christmas Eve, 1524."),
    ("In which church was Vasco da Gama initially buried in India?", "St. Francis Church", ["St. Francis Church", "Basilica of Bom Jesus", "Sé Cathedral", "St. Cajetan Church"], "He was buried in St. Francis Church in Fort Kochi before being moved to Portugal in 1539."),
    # 11-20
    ("Who commanded the São Rafael during the first voyage?", "Paulo da Gama", ["Paulo da Gama", "Nicolau Coelho", "Afonso de Albuquerque", "Vasco da Gama"], "Paulo da Gama was Vasco's brother and commanded São Rafael."),
    ("Who commanded the fast caravel Bérrio during the first voyage?", "Nicolau Coelho", ["Nicolau Coelho", "Paulo da Gama", "Vicente Sodré", "Gaspar da Gama"], "Nicolau Coelho commanded Bérrio and was the first to return to Portugal."),
    ("What tip of Africa did Vasco da Gama round in November 1497?", "Cape of Good Hope", ["Cape of Good Hope", "Cape Horn", "Cape Comorin", "Cape Verde"], "Rounding the Cape of Good Hope opened the ocean path to India."),
    ("From which port did Vasco da Gama depart in July 1497?", "Lisbon", ["Lisbon", "Porto", "Sines", "Lagos"], "The expedition set sail from Lisbon (Restelo)."),
    ("In which year did Gama's first voyage return to Lisbon?", "1499 CE", ["1499 CE", "1498 CE", "1500 CE", "1502 CE"], "Gama returned in August 1499 after a two-year journey."),
    ("Which Malayalam term was corrupted by the Portuguese to 'Zamorin'?", "Samudiri", ["Samudiri", "Samanta", "Nair", "Nayaka"], "Samudiri Raja means the Lord of the Sea in Malayalam."),
    ("What did Vasco da Gama demand the Zamorin do to Muslim merchants in 1502?", "Expel them completely", ["Expel them completely", "Tax them at double rates", "Convert them to Christianity", "Forbid them from speaking Malayalam"], "Gama demanded the complete expulsion of all Muslim traders to secure a monopoly."),
    ("Where did the Portuguese construct their first fortress, Fort Emmanuel?", "Cochin", ["Cochin", "Goa", "Cannur", "Anjadip"], "Fort Emmanuel was built in Cochin in 1503 to protect the factory."),
    ("Where did the Portuguese establish their second factory on the Malabar Coast?", "Cannur (Kannur)", ["Cannur (Kannur)", "Cochin", "Quilon", "Calicut"], "The second factory was established at Cannur under Kolathiri protection."),
    ("What North African translator assisted Vasco da Gama in Calicut?", "Monzaide", ["Monzaide", "Ibn Majid", "Gaspar da Gama", "Ahmad bin Majid"], "Monzaide was an Arabic-speaking North African who helped interpret."),
    # 21-30
    ("What was the religion of the Zamorin of Calicut?", "Hinduism", ["Hinduism", "Islam", "Buddhism", "Christianity"], "The Zamorin was a Hindu Nair ruler who followed traditional practices."),
    ("Why did the Zamorin reject the gifts brought by Vasco da Gama?", "They were cheap, low-value items", ["They were cheap, low-value items", "They contained forbidden items", "They were damaged by sea water", "They were stolen from other ports"], "The gifts (hats, cloth, honey) were laughed at by court officials as unfit for a king."),
    ("Which European city-state suffered the most due to the Cape Route?", "Venice", ["Venice", "Genoa", "Florence", "Pisa"], "Venice lost its monopoly on spice distribution in Western Europe."),
    ("What was the Portuguese crown department that managed spice monopolies?", "Casa da Índia", ["Casa da Índia", "Estado da Índia", "Carreira da Índia", "Mesa da Consciência"], "Casa da Índia (House of India) regulated all overseas trade and duties in Lisbon."),
    ("What licensing system did the Portuguese introduce to tax Indian Ocean shipping?", "Cartaz", ["Cartaz", "Feitoria", "Estado", "Carreira"], "The Cartaz was a mandatory sailing pass that forced merchants to pay duties."),
    ("What was the annual line of fleets between Lisbon and Goa called?", "Carreira da Índia", ["Carreira da Índia", "Casa da Índia", "Flota de Indias", "VOC"], "The 'Carreira da Índia' was the state-run sailing line to India."),
    ("Which battle in 1509 CE secured Portuguese naval supremacy in the Indian Ocean?", "Battle of Diu", ["Battle of Diu", "Battle of Cochin", "Battle of Chaul", "Battle of Swally"], "Francisco de Almeida defeated a joint Egyptian-Gujarati fleet at Diu."),
    ("In which year did the exhumation of Vasco da Gama's remains occur?", "1539 CE", ["1539 CE", "1524 CE", "1550 CE", "1600 CE"], "His remains were returned to Portugal in 1539 CE."),
    ("Which Portuguese King appointed Vasco da Gama as Viceroy in 1524?", "King John III", ["King John III", "King Manuel I", "King Sebastian", "King Afonso VI"], "King John III succeeded King Manuel and sent Gama to clean up corruption."),
    ("Which corrupt governor was suspended and replaced by Vasco da Gama in 1524?", "Duarte de Menezes", ["Duarte de Menezes", "Lopo Vaz de Sampaio", "Afonso de Albuquerque", "Nino da Cunha"], "Duarte de Menezes was arrested by Gama on charges of embezzlement."),
    # 31-40
    ("Where did Vasco da Gama face hostility first along the East African coast?", "Mozambique", ["Mozambique", "Mombasa", "Malindi", "Sofala"], "Gama was expelled from Mozambique after conflicts with the Sultan."),
    ("Which East African city provided Vasco da Gama with a pilot to cross the Arabian Sea?", "Malindi", ["Malindi", "Mozambique", "Mombasa", "Kilwa"], "The Sultan of Malindi welcomed Gama and provided a skilled pilot."),
    ("Which ship was burned by Vasco da Gama near Mombasa due to lack of crew?", "São Rafael", ["São Rafael", "São Gabriel", "Bérrio", "São Salvador"], "São Rafael was destroyed because scurvy left too few crew to sail it."),
    ("What sailing technique involves a wide ocean arc to catch favorable winds?", "Volta do Mar", ["Volta do Mar", "Carreira", "Cartaz", "Feitoria"], "Volta do Mar (Turn of the Sea) was crucial for rounding Africa."),
    ("In which month did Vasco da Gama arrive at Kappad beach near Calicut?", "May", ["May", "July", "August", "December"], "He landed at Calicut on May 20, 1498 CE."),
    ("In which month did Vasco da Gama depart Calicut for his return voyage in 1498?", "August", ["August", "May", "October", "December"], "Gama departed in August 1498, facing poor monsoon winds on the return leg."),
    ("What Malayalam-speaking local region was Calicut located in?", "Malabar", ["Malabar", "Coromandel", "Konkan", "Gujarat"], "Calicut was the chief port city of the Malabar Coast."),
    ("How many crew members returned safely out of the 170 that started in 1497?", "Around 55", ["Around 55", "Around 120", "All 170", "None"], "Only about 55 survivors returned to Portugal due to scurvy and clashes."),
    ("What was the first European trading post (factory) structure in India?", "Cochin factory", ["Cochin factory", "Calicut factory", "Goa factory", "Surat factory"], "The Cochin trading post was established in 1503 CE."),
    ("Which ocean did Vasco da Gama cross to reach India from Malindi?", "Indian Ocean", ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Southern Ocean"], "The fleet crossed the Indian Ocean using the southwest monsoon winds."),
    # 41-50
    ("What Malayalam term represents the port officer of the Zamorin?", "Shahbandar", ["Shahbandar", "Samudiri", "Kolathiri", "Adil Shah"], "The Shahbandar was the Arabic-origin title for the port master of Calicut."),
    ("Which pope issued the bull that divided the undiscovered world between Spain and Portugal?", "Pope Alexander VI", ["Pope Alexander VI", "Pope Julius II", "Pope Leo X", "Pope Clement VII"], "Pope Alexander VI brokered the Treaty of Tordesillas in 1494."),
    ("In which year was the Treaty of Tordesillas signed?", "1494 CE", ["1494 CE", "1498 CE", "1500 CE", "1510 CE"], "Signed in 1494, it divided the world's oceans between Spain and Portugal."),
    ("Who commanded the patrol fleet left behind by Gama in 1503?", "Vicente Sodré", ["Vicente Sodré", "Nicolau Coelho", "Paulo da Gama", "Duarte Barbosa"], "Vicente Sodré commanded the first Portuguese patrol in Indian waters."),
    ("Which Portuguese nobleman took over Goa in 1510?", "Afonso de Albuquerque", ["Afonso de Albuquerque", "Francisco de Almeida", "Vasco da Gama", "Nino da Cunha"], "Afonso de Albuquerque captured Goa and made it the capital."),
    ("Where was Vasco da Gama born?", "Sines", ["Sines", "Lisbon", "Porto", "Coimbra"], "Gama was born in the coastal town of Sines, Portugal."),
    ("What was the name of Vasco da Gama's father?", "Estêvão da Gama", ["Estêvão da Gama", "Paulo da Gama", "Manuel da Gama", "Afonso da Gama"], "Estêvão da Gama was also a knight and explorer."),
    ("Which group of islands in the Atlantic did Gama's fleet pass first?", "Cape Verde", ["Cape Verde", "Azores", "Canary Islands", "Madeira"], "The fleet passed Cape Verde before swinging west into the open Atlantic."),
    ("Which Malayalam state was Cochin's traditional overlord?", "Calicut", ["Calicut", "Kannur", "Venad", "Travancore"], "Cochin was a political subordinate to Calicut before the Portuguese arrived."),
    ("What Malayalam term denotes the local Nair warriors of Calicut?", "Lokharas", ["Lokharas", "Samantas", "Nair army", "Marakkars"], "The Nair fighters served as the infantry forces for the Zamorin.")
]

practice_en = []
for idx, data in enumerate(practice_pool_en):
    qtext, ans_val, opts, sol = data
    practice_en.append({
        "type": "MCQ",
        "q": qtext,
        "opts": opts,
        "ans": opts.index(ans_val),
        "sol": sol
    })

# Add multi-correct items specifically into practice to maintain variety
practice_en[0] = {
    "type": "Multiple Correct MCQ",
    "q": "Which ships returned safely to Lisbon out of the original first fleet? (Select all that apply)",
    "opts": ["São Gabriel", "Bérrio", "São Rafael", "São Salvador"],
    "ans": [0, 1],
    "sol": "São Gabriel and Bérrio returned safely. São Rafael was burned due to crew loss."
}
practice_en[10] = {
    "type": "Multiple Correct MCQ",
    "q": "Identify the Malabar ports that formed trade alliances or factories with the Portuguese in the early 1500s. (Select all that apply)",
    "opts": ["Cochin", "Kannur", "Quilon", "Calicut"],
    "ans": [0, 1, 2],
    "sol": "Cochin, Kannur, and Quilon allied with the Portuguese, whereas Calicut remained hostile."
}
practice_en[20] = {
    "type": "Multiple Correct MCQ",
    "q": "Which kingdoms or states opposed the Portuguese monopoly on the spice trade? (Select all that apply)",
    "opts": ["Mamluk Sultanate of Egypt", "Zamorin of Calicut", "Gujarat Sultanate", "Kingdom of Cochin"],
    "ans": [0, 1, 2],
    "sol": "Mamluk Egypt, Calicut, and Gujarat formed coalitions to fight the Portuguese. Cochin was their primary ally."
}

# Translate practice to Hindi
practice_pool_hi = [
    # 1-10
    ("वास्को डी गामा पहली बार किस वर्ष भारत पहुंचे थे?", "1498 ईस्वी", ["1498 ईस्वी", "1502 ईस्वी", "1492 ईस्वी", "1510 ईस्वी"], "वे मई 1498 में कालीकट के पास कप्पड़ में उतरे थे।"),
    ("गामा की पहली यात्रा के दौरान पुर्तगाली राजा कौन थे?", "राजा मैनुअल प्रथम", ["राजा मैनुअल प्रथम", "राजा जॉन तृतीय", "राजा सेबस्टियन", "राजा अफोंसो पंचम"], "राजा मैनुअल प्रथम ने इस ऐतिहासिक यात्रा को प्रायोजित और वित्त पोषित किया था।"),
    ("किस मालाबार बंदरगाह ने पुर्तगालियों का स्वागत किया और पहला फैक्ट्री गठबंधन बनाया?", "कोचीन", ["कोचीन", "कालीकट", "गोवा", "सूरत"], "कोचीन ने पुर्तगालियों के साथ एक सुरक्षित गठबंधन और फैक्ट्री बनाई।"),
    ("वास्को डी गामा के पहले बेड़े का ध्वजपोत (फ्लैगशिप) कौन सा था?", "साओ गेब्रियल", ["साओ गेब्रियल", "साओ राफेल", "बेरियो", "साओ साल्वाडोर"], "साओ गेब्रियल की कमान सीधे वास्को डी गामा के पास थी।"),
    ("पहली यात्रा के दौरान मृत्यु का मुख्य कारण कौन सी बीमारी थी?", "स्कर्वी", ["स्कर्वी", "मलेरिया", "हैजा", "पीला बुखार"], "स्कर्वी लंबी यात्राओं के दौरान विटामिन सी की कमी के कारण हुआ था।"),
    ("1500 ईस्वी के मध्यवर्ती पुर्तगाली बेड़े की कमान किसने संभाली थी?", "पेड्रो अल्वारेस कैब्राल", ["पेड्रो अल्वारेस कैब्राल", "अल्फांसो डी अल्बुकर्क", "फ्रांसिस्को डी अल्मेडा", "वास्को डी गामा"], "पेड्रो अल्वारेस कैब्राल ने दूसरे अभियान का नेतृत्व किया और रास्ते में ब्राजील की खोज की।"),
    ("1502 ईस्वी में वास्को डी गामा द्वारा किस तीर्थयात्री जहाज पर कब्जा कर लिया गया और उसे जला दिया गया था?", "मिरी", ["मिरी", "साओ राफेल", "फ्लोर डी ला मार", "सांता मारिया"], "गामा ने 300 से अधिक यात्रियों के साथ मिरी जहाज को लूटा और जला दिया।"),
    ("1524 ईस्वी में वास्को डी गामा को उनकी तीसरी यात्रा पर क्या आधिकारिक उपाधि मिली थी?", "भारत के वायसराय", ["भारत के वायसराय", "गवर्नर-जनरल", "समुद्र के एडमिरल", "उच्चायुक्त"], "गामा को 1524 में राजा जॉन तृतीय द्वारा भारत का दूसरा वायसराय नियुक्त किया गया था।"),
    ("1524 ईस्वी में भारत में वास्को डी गामा का निधन कहाँ हुआ था?", "कोचीन", ["कोचीन", "गोवा", "कालीकट", "दीव"], "गामा का निधन 24 दिसंबर 1524 को कोचीन में मलेरिया के कारण हुआ था।"),
    ("भारत में वास्को डी गामा को शुरू में किस चर्च में दफनाया गया था?", "सेंट फ्रांसिस चर्च", ["सेंट फ्रांसिस चर्च", "बेसिलिका ऑफ बॉम जीसस", "से कैथेड्रल", "सेंट केजेटन चर्च"], "उन्हें 1539 में पुर्तगाल ले जाने से पहले फोर्ट कोच्चि के सेंट फ्रांसिस चर्च में दफनाया गया था।"),
    # 11-20
    ("पहली यात्रा के दौरान साओ राफेल की कमान किसने संभाली थी?", "पाउलो डी गामा", ["पाउलो डी गामा", "निकोलाउ कोएल्हो", "अल्फांसो डी अल्बुकर्क", "वास्को डी गामा"], "पाउलो डी गामा वास्को के भाई थे और उन्होंने साओ राफेल की कमान संभाली थी।"),
    (" पहली यात्रा के दौरान बेरियो जहाज की कमान किसने संभाली थी?", "निकोलाउ कोएल्हो", ["निकोलाउ कोएल्हो", "पाउलो डी गामा", "विसेन्टे सोद्रे", "गास्पर डी गामा"], "निकोलाउ कोएल्हो ने बेरियो की कमान संभाली और वे पुर्तगाल लौटने वाले पहले व्यक्ति थे।"),
    ("नवंबर 1497 में वास्को डी गामा ने अफ्रीका के किस सिरे का चक्कर लगाया था?", "केप ऑफ गुड होप", ["केप ऑफ गुड होप", "केप हॉर्न", "केप कोमोरिन", "केप वर्डे"], "केप ऑफ गुड होप का चक्कर लगाने से भारत के लिए महासागरीय मार्ग खुल गया।"),
    ("जुलाई 1497 में वास्को डी गामा किस बंदरगाह से रवाना हुए थे?", "लिस्बन", ["लिस्बन", "पोर्टो", "सिनेस", "लागोस"], "अभियान लिस्बन (रेस्टेलो) से रवाना हुआ था।"),
    ("गामा की पहली यात्रा किस वर्ष लिस्बन लौटी थी?", "1499 ईस्वी", ["1499 ईस्वी", "1498 ईस्वी", "1500 ईस्वी", "1502 ईस्वी"], "गामा दो साल की यात्रा के बाद अगस्त 1499 में लौटे।"),
    ("पुर्तगालियों ने किस मलयालम शब्द को बिगाड़कर 'ज़मोरिन' कर दिया था?", "सामुदिरी", ["सामुदिरी", "सामंत", "नायर", "नायक"], "सामुदिरी राजा का मतलब मलयालम में समुद्र का स्वामी होता है।"),
    ("वास्को डी गामा ने 1502 में ज़मोरिन से मुस्लिम व्यापारियों के साथ क्या करने की मांग की थी?", "उन्हें पूरी तरह निष्कासित करें", ["उन्हें पूरी तरह निष्कासित करें", "उन पर दोगुना कर लगाएं", "उन्हें ईसाई धर्म में परिवर्तित करें", "उन्हें मलयालम बोलने से रोकें"], "गामा ने एकाधिकार सुरक्षित करने के लिए सभी मुस्लिम व्यापारियों को निष्कासित करने की मांग की।"),
    ("पुर्तगालियों ने अपने पहले किले, फोर्ट इमैनुएल का निर्माण कहाँ किया था?", "कोचीन", ["कोचीन", "गोवा", "कन्नूर", "अंजादीप"], "फोर्ट इमैनुएल का निर्माण 1503 में कोचीन में फैक्ट्री की सुरक्षा के लिए किया गया था।"),
    ("पुर्तगालियों ने मालाबार तट पर अपनी दूसरी फैक्ट्री कहाँ स्थापित की थी?", "कन्नूर", ["कन्नूर", "कोचीन", "क्विलोन", "कालीकट"], "दूसरी फैक्ट्री कन्नूर में कोलाथिरी के संरक्षण में स्थापित की गई थी।"),
    ("कालीकट में वास्को डी गामा की सहायता किस उत्तरी अफ्रीकी अनुवादक ने की थी?", "मोन्ज़ैदे", ["मोन्ज़ैदे", "इब्न मजीद", "गास्पर डी गामा", "अहमद बिन मजीद"], "मोन्ज़ैदे एक अरबी भाषी उत्तरी अफ्रीकी थे जिन्होंने अनुवाद में सहायता की थी।"),
    # 21-30
    ("कालीकट के ज़मोरिन का धर्म क्या था?", "हिंदू धर्म", ["हिंदू धर्म", "इस्लाम", "बौद्ध धर्म", "ईसाई धर्म"], "ज़मोरिन एक हिंदू नायर शासक थे जो पारंपरिक प्रथाओं का पालन करते थे।"),
    ("ज़मोरिन ने वास्को डी गामा द्वारा लाए गए उपहारों को क्यों खारिज कर दिया था?", "वे कम मूल्य की सस्ती वस्तुएं थीं", ["वे कम मूल्य की सस्ती वस्तुएं थीं", "उनमें वर्जित वस्तुएं शामिल थीं", "वे समुद्र के पानी से क्षतिग्रस्त हो गए थे", "वे अन्य बंदरगाहों से चुराए गए थे"], "उपहारों (कपड़े, टोपी, शहद) को दरबारी अधिकारियों ने एक राजा के लिए अनुपयुक्त बताकर मज़ाक उड़ाया।"),
    ("केप मार्ग के कारण किस यूरोपीय नगर-राज्य को सबसे अधिक नुकसान हुआ?", "वेनिस", ["वेनिस", "जेनोआ", "फ्लोरेंस", "पीसा"], "वेनिस ने पश्चिमी यूरोप में मसाला वितरण पर अपना एकाधिकार खो दिया।"),
    ("पुर्तगाली क्राउन का वह कौन सा विभाग था जो मसाला एकाधिकार का प्रबंधन करता था?", "कासा दा इंडिया", ["कासा दा इंडिया", "एस्टाडो दा इंडिया", "कैरियर दा इंडिया", "मेसा दा कॉन्सिनेशिया"], "कासा दा इंडिया ने लिस्बन में सभी विदेशी व्यापार और करों को विनियमित किया।"),
    ("पुर्तगालियों ने हिंद महासागर के नौवहन पर कर लगाने के लिए कौन सी लाइसेंस प्रणाली शुरू की थी?", "कार्टाज", ["कार्टाज", "फेइटोरिया", "एस्टाडो", "कैरियर"], "कार्टाज एक अनिवार्य नौवहन पास था जिसने व्यापारियों को कर देने के लिए मजबूर किया।"),
    ("लिस्बन और गोवा के बीच जहाजों के वार्षिक मार्ग को क्या कहा जाता था?", "कैरियर दा इंडिया", ["कैरियर दा इंडिया", "कासा दा इंडिया", "फ्लोटा डी इंडियास", "वीओसी"], "'कैरियर दा इंडिया' भारत के लिए राज्य द्वारा संचालित नौवहन मार्ग था।"),
    ("1509 ईस्वी में किस युद्ध ने हिंद महासागर में पुर्तगाली नौसैनिक वर्चस्व सुरक्षित किया था?", "दीव का युद्ध", ["दीव का युद्ध", "कोचीन का युद्ध", "चौल का युद्ध", "स्वाली का युद्ध"], "फ्रांसिस्को डी अल्मेडा ने दीव में मिस्र-गुजराती संयुक्त बेड़े को हराया था।"),
    ("वास्को डी गामा के अवशेषों को वापस पुर्तगाल भेजने का कार्य किस वर्ष हुआ था?", "1539 ईस्वी", ["1539 ईस्वी", "1524 ईस्वी", "1550 ईस्वी", "1600 ईस्वी"], "उनके अवशेष 1539 ईस्वी में पुर्तगाल लौटाए गए थे।"),
    ("किस पुर्तगाली राजा ने 1524 में वास्को डी गामा को वायसराय नियुक्त किया था?", "राजा जॉन तृतीय", ["राजा जॉन तृतीय", "राजा मैनुअल प्रथम", "राजा सेबस्टियन", "राजा अफोंसो VI"], "राजा जॉन तृतीय ने भ्रष्टाचार को समाप्त करने के लिए गामा को भेजा था।"),
    ("1524 में वास्को डी गामा द्वारा किस भ्रष्ट गवर्नर को निलंबित और प्रतिस्थापित किया गया था?", "दुआर्ते दे मेनेजेस", ["दुआर्ते दे मेनेजेस", "लोपो वाज दे सम्पायो", "अल्फांसो डी अल्बुकर्क", "नीनो दा कुन्हा"], "दुआर्ते दे मेनेजेस को भ्रष्टाचार के आरोप में गामा ने गिरफ्तार किया था।"),
    # 31-40
    ("पूर्वी अफ्रीकी तट पर वास्को डी गामा को सबसे पहले कहाँ शत्रुता का सामना करना पड़ा?", "मोजाम्बिक", ["मोजाम्बिक", "मोम्बासा", "मालिंदी", "सोफाला"], "मोजाम्बिक के सुल्तान के साथ संघर्ष के बाद गामा को वहां से निकाल दिया गया था।"),
    ("किस पूर्वी अफ्रीकी शहर ने वास्को डी गामा को अरब सागर पार करने के लिए नाविक प्रदान किया था?", "मालिंदी", ["मालिंदी", "मोजाम्बिक", "मोम्बासा", "किल्वा"], "मालिंदी के सुल्तान ने गामा का स्वागत किया और एक कुशल पायलट प्रदान किया।"),
    ("चालक दल की कमी के कारण वास्को डी गामा ने मोम्बासा के पास किस जहाज को जला दिया था?", "साओ राफेल", ["साओ राफेल", "साओ गेब्रियल", "बेरियो", "साओ साल्वाडोर"], "साओ राफेल को नष्ट कर दिया गया था क्योंकि चालक दल बहुत कम बचा था।"),
    ("अनुकूल हवाओं को पकड़ने के लिए समुद्र में एक विस्तृत मार्ग बनाने की तकनीक क्या कहलाती है?", "वोल्टा डो मार", ["वोल्टा डो मार", "कैरियर", "कार्टाज", "फेइटोरिया"], "वोल्टा डो मार (समुद्र का घुमाव) अफ्रीका का चक्कर लगाने के लिए महत्वपूर्ण था।"),
    ("वास्को डी गामा किस महीने में कालीकट के पास कप्पड़ तट पर पहुंचे थे?", "मई", ["मई", "जुलाई", "अगस्त", "दिसंबर"], "वे 20 मई 1498 ईस्वी को कालीकट पहुंचे थे।"),
    ("1498 में वास्को डी गामा किस महीने में अपनी वापसी यात्रा के लिए कालीकट से रवाना हुए थे?", "अगस्त", ["अगस्त", "मई", "अक्टूबर", "दिसंबर"], "गामा अगस्त 1498 में रवाना हुए, और वापसी में विपरीत मानसूनी हवाओं का सामना किया।"),
    ("कालीकट किस मलयालम भाषी स्थानीय क्षेत्र में स्थित था?", "मालाबार", ["मालाबार", "कोरोमंडल", "कोंकण", "गुजरात"], "कालीकट मालाबार तट का मुख्य बंदरगाह शहर था।"),
    ("1497 में शुरू हुए 170 सदस्यों में से कितने चालक दल सुरक्षित लौटे?", "लगभग 55", ["लगभग 55", "लगभग 120", "सभी 170", "कोई नहीं"], "स्कर्वी और झड़पों के कारण केवल 55 नाविक ही जीवित पुर्तगाल लौट सके।"),
    ("भारत में पहला यूरोपीय व्यापारिक केंद्र (फैक्ट्री) कौन सा था?", "कोचीन फैक्ट्री", ["कोचीन फैक्ट्री", "कालीकट फैक्ट्री", "गोवा फैक्ट्री", "सूरत फैक्ट्री"], "कोचीन व्यापारिक केंद्र की स्थापना 1503 ईस्वी में हुई थी।"),
    ("वास्को डी गामा ने मालिंदी से भारत पहुँचने के लिए किस महासागर को पार किया था?", "हिंद महासागर", ["हिंद महासागर", "अटलांटिक महासागर", "प्रशांत महासागर", "दक्षिणी महासागर"], "बेड़े ने दक्षिण-पश्चिम मानसून हवाओं का उपयोग करके हिंद महासागर को पार किया।"),
    # 41-50
    ("ज़मोरिन के बंदरगाह अधिकारी को किस मलयालम/अरबी शब्द से जाना जाता था?", "शाहबंदर", ["शाहबंदर", "सामुदिरी", "कोलाथिरी", "आदिल शाह"], "शाहबंदर कालीकट के बंदरगाह मास्टर का अरबी मूल का शीर्षक था।"),
    ("किस पोप ने उस आदेश को जारी किया जिसने अनपेक्षित दुनिया को स्पेन और पुर्तगाल के बीच विभाजित किया?", "पोप अलेक्जेंडर VI", ["पोप अलेक्जेंडर VI", "पोप जूलियस द्वितीय", "पोप लियो X", "पोप क्लेमेंट VII"], "पोप अलेक्जेंडर VI ने 1494 में टॉर्डेसिलस की संधि की मध्यस्थता की।"),
    ("टॉर्डेसिलस की संधि पर किस वर्ष हस्ताक्षर किए गए थे?", "1494 ईस्वी", ["1494 ईस्वी", "1498 ईस्वी", "1500 ईस्वी", "1510 ईस्वी"], "1494 में हस्ताक्षरित इस संधि ने स्पेन और पुर्तगाल के बीच महासागरों को विभाजित किया।"),
    ("1503 में गामा द्वारा पीछे छोड़े गए गश्ती बेड़े की कमान किसने संभाली थी?", "विसेन्टे सोद्रे", ["विसेन्टे सोद्रे", "निकोलाउ कोएल्हो", "पाउलो डी गामा", "दुआर्ते बारबोसा"], "विसेन्टे सोद्रे ने भारतीय जल क्षेत्र में पहले पुर्तगाली गश्ती बेड़े की कमान संभाली।"),
    ("किस पुर्तगाली रईस ने 1510 में गोवा पर अधिकार कर लिया था?", "अल्फांसो डी अल्बुकर्क", ["अल्फांसो डी अल्बुकर्क", "फ्रांसिस्को डी अल्मेडा", "वास्को डी गामा", "नीनो दा कुन्हा"], "अल्फांसो डी अल्बुकर्क ने गोवा पर कब्जा कर लिया और इसे राजधानी बनाया।"),
    ("वास्को डी गामा का जन्म कहाँ हुआ था?", "सिनेस", ["सिनेस", "लिस्बन", "पोर्टो", "कोइम्ब्रा"], "गामा का जन्म पुर्तगाल के तटीय शहर सिनेस में हुआ था।"),
    ("वास्को डी गामा के पिता का नाम क्या था?", "एस्टेवाओ डी गामा", ["एस्टेवाओ डी गामा", "पाउलो डी गामा", "मैनुअल डी गामा", "अफांसो डी गामा"], "एस्टेवाओ डी गामा भी एक शूरवीर और खोजकर्ता थे।"),
    ("अटलांटिक में गामा के बेड़े ने सबसे पहले किस द्वीप समूह को पार किया था?", "केप वर्डे", ["केप वर्डे", "एज़ोरेस", "कैनरी द्वीप", "मदीरा"], "बेड़े ने खुले अटलांटिक में पश्चिम की ओर जाने से पहले केप वर्डे को पार किया।"),
    ("कौन सा मलयालम राज्य कोचीन का पारंपरिक अधिपति था?", "कालीकट", ["कालीकट", "कन्नूर", "वेनाड", "त्रावणकोर"], "पुर्तगालियों के आने से पहले कोचीन राजनीतिक रूप से कालीकट के अधीन था।"),
    ("कालीकट के स्थानीय नायर योद्धाओं को क्या कहा जाता था?", "लोखरा", ["लोखरा", "सामंत", "नायर सेना", "मरक्कड़"], "नायर योद्धा ज़मोरिन के पैदल सैनिक बल के रूप में कार्य करते थे।")
]

practice_hi = []
for idx, data in enumerate(practice_pool_hi):
    qtext, ans_val, opts, sol = data
    practice_hi.append({
        "type": "MCQ",
        "q": qtext,
        "opts": opts,
        "ans": opts.index(ans_val),
        "sol": sol
    })

# Local replacements for Hindi multi-correct
practice_hi[0] = {
    "type": "Multiple Correct MCQ",
    "q": "मूल पहले बेड़े में से कौन से जहाज सुरक्षित रूप से लिस्बन लौटे? (सभी लागू विकल्प चुनें)",
    "opts": ["साओ गेब्रियल", "बेरियो", "साओ राफेल", "साओ साल्वाडोर"],
    "ans": [0, 1],
    "sol": "साओ गेब्रियल और बेरियू सुरक्षित लौटे। चालक दल के नुकसान के कारण साओ राफेल को जला दिया गया था।"
}
practice_hi[10] = {
    "type": "Multiple Correct MCQ",
    "q": "उन मालाबार बंदरगाहों की पहचान करें जिन्होंने 1500 के दशक की शुरुआत में पुर्तगालियों के साथ व्यापारिक गठबंधन या फैक्ट्रियां बनाईं। (सभी लागू विकल्प चुनें)",
    "opts": ["कोचीन", "कन्नूर", "क्विलोन", "कालीकट"],
    "ans": [0, 1, 2],
    "sol": "कोचीन, कन्नूर और क्विलोन ने पुर्तगालियों के साथ गठबंधन किया, जबकि कालीकट शत्रुतापूर्ण बना रहा।"
}
practice_hi[20] = {
    "type": "Multiple Correct MCQ",
    "q": "किन साम्राज्यों या राज्यों ने मसाला व्यापार पर पुर्तगाली एकाधिकार का विरोध किया? (सभी लागू विकल्प चुनें)",
    "opts": ["मिस्र का ममलुक सल्तनत", "कालीकट के ज़मोरिन", "गुजरात सल्तनत", "कोचीन साम्राज्य"],
    "ans": [0, 1, 2],
    "sol": "ममलुक मिस्र, कालीकट और गुजरात ने पुर्तगालियों से लड़ने के लिए गठबंधन बनाया। कोचीन उनका मुख्य सहयोगी था।"
}

generate_sec_file("practice", practice_en, practice_hi)


# ==================== 10 COMPLETELY UNIQUE MOCK QUESTIONS ====================
mock_en = [
    {
        "type": "MCQ",
        "q": "With reference to Vasco da Gama's first voyage (1497-1499 CE), consider the following statements:\n1. The fleet sailed entirely through the Mediterranean Sea and Mamluk Egyptian ports to reach Calicut.\n2. The expedition secured the services of Gujarati navigator Ahmad Ibn Mājid at Malindi to cross the Arabian Sea.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect as they sailed around the Cape of Good Hope (Atlantic Route). Statement 2 is correct as they secured pilot Ahmad Ibn Majid in Malindi."
    },
    {
        "type": "MCQ",
        "q": "With reference to the encounters between Vasco da Gama and the Zamorin of Calicut, consider the following statements:\n1. The Zamorin held the title of Samudiri Raja, signifying Hindu sovereign status over the Malabar seas.\n2. Vasco da Gama presented gold bullion and silver coinage, which was highly appreciated by the Calicut court.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the gifts presented (cloth, hats, oil) were cheap and mocked by the court."
    },
    {
        "type": "MCQ",
        "q": "With reference to Vasco da Gama's second voyage in 1502 CE, consider the following statements:\n1. He arrived with a heavily armed fleet of 20 ships to punish Calicut and enforce a crown monopoly.\n2. He allied with the ruler of Cochin, which became the main base of the Portuguese Estado da India in its early phase.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Gama used 20 ships for gunboat diplomacy and allied with Cochin, establishing their first Indian factory/base."
    },
    {
        "type": "MCQ",
        "q": "Regarding Vasco da Gama's final voyage and viceroyalty in 1524 CE, consider the following statements:\n1. He was appointed Viceroy by King Manuel I to expand territory into the Deccan region.\n2. He died in Cochin due to malaria and was initially buried in St. Francis Church.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect; he was appointed by King John III to clean up administrative corruption. Statement 2 is correct; he died of malaria in Cochin."
    },
    {
        "type": "MCQ",
        "q": "With reference to the Portuguese commercial regulation system in the Indian Ocean, consider the following statements:\n1. The Cartaz was a mandatory licensing pass that forced merchant ships to pay duties at Portuguese customs houses.\n2. Foreign vessels carrying spices or weapons without a Cartaz were liable to capture and confiscation.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. The Cartaz system was enforced strictly to control trade routes and monopolize spice transport."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding early Portuguese navigation techniques:\n1. The 'Volta do Mar' technique involved sailing in a wide Atlantic loop to catch favorable winds.\n2. Navigators used astrolabes to calculate longitude directly from solar angles.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect; astrolabes were used to measure latitude (declination), not longitude directly."
    },
    {
        "type": "MCQ",
        "q": "With reference to the intermediate voyages, consider the following statements:\n1. Pedro Álvares Cabral established the first Portuguese factory in Calicut, which was subsequently destroyed in 1500 CE.\n2. Vasco da Gama was the commander of the patrol fleet left behind by Cabral to blockade the Red Sea.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect; the Red Sea patrol was left by Gama himself in 1503 and commanded by Vicente Sodré."
    },
    {
        "type": "MCQ",
        "q": "Regarding the geopolitical impact of the Cape Route, consider the following statements:\n1. It led to the financial rise of Venetian spice brokers who distributed Cape spices in Northern Europe.\n2. The diversion of spice trade weakened Mamluk Egypt, indirectly facilitating its conquest by the Ottoman Empire in 1517.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect; Venice declined while Lisbon rose. Statement 2 is correct; Egypt lost transit duties, weakening them before the Ottoman conquest."
    },
    {
        "type": "MCQ",
        "q": "With reference to the administration of the Portuguese Estado da India, consider the following statements:\n1. The capital of the Estado da India was shifted from Cochin to Goa in 1530 by Nino da Cunha.\n2. Vasco da Gama arrested and sent Duarte de Menezes back to Portugal on charges of corruption in 1524.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Capital was shifted to Goa in 1530. Gama suspended Menezes for corruption in 1524."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding the pilgrim ship Miri incident in 1502 CE:\n1. The Miri was an armed Egyptian warship sent to attack Portuguese factories in Malabar.\n2. Vasco da Gama plundered and set the ship on fire, leading to the death of hundreds of civilian passengers.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect; it was an unarmed civilian passenger/pilgrim ship. Statement 2 is correct; it was plundered and burned by Gama."
    }
]

# Translate mock to Hindi
mock_hi = []
for idx, q in enumerate(mock_en):
    q_hi = q.copy()
    hi_questions = [
        "वास्को डी गामा की पहली यात्रा (1497-1499 ईस्वी) के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. कालीकट पहुंचने के लिए बेड़े ने पूरी तरह से भूमध्य सागर और ममलुक मिस्र के बंदरगाहों से यात्रा की।\n2. इस अभियान ने अरब सागर पार करने के लिए मालिंदी में गुजराती नाविक अहमद इब्न मजीद की सेवाएं लीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "वास्को डी गामा और कालीकट के ज़मोरिन के बीच मुठभेड़ों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. ज़मोरिन के पास समुद्रि राजा की उपाधि थी, जो मालाबार समुद्र पर हिंदू संप्रभु स्थिति का प्रतीक थी।\n2. वास्को डी गामा ने सोने और चांदी के सिक्के भेंट किए, जिनकी कालीकट दरबार द्वारा अत्यधिक सराहना की गई।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "1502 ईस्वी में वास्को डी गामा की दूसरी यात्रा के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. वे कालीकट को दंडित करने और शाही एकाधिकार लागू करने के लिए 20 भारी सशस्त्र जहाजों के बेड़े के साथ पहुंचे।\n2. उन्होंने कोचीन के शासक के साथ गठबंधन किया, जो पुर्तगाली एस्टाडो दा इंडिया के शुरुआती चरण में मुख्य आधार बन गया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "1524 ईस्वी में वास्को डी गामा की अंतिम यात्रा और वायसराय पद के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. दक्कन क्षेत्र में क्षेत्र का विस्तार करने के लिए उन्हें राजा मैनुअल प्रथम द्वारा वायसराय नियुक्त किया गया था।\n2. कोचीन में मलेरिया के कारण उनकी मृत्यु हो गई और उन्हें शुरू में सेंट फ्रांसिस चर्च में दफनाया गया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "हिंद महासागर में पुर्तगाली व्यापार विनियमन प्रणाली के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. कार्टाज एक अनिवार्य लाइसेंसिंग पास था जिसने व्यापारिक जहाजों को पुर्तगाली सीमा शुल्क गृहों में शुल्क का भुगतान करने के लिए मजबूर किया।\n2. बिना कार्टाज के मसाले या हथियार ले जाने वाले विदेशी जहाज जब्त किए जाने योग्य थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "शुरुआती पुर्तगाली नौवहन तकनीकों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. 'वोल्टा डो मार' तकनीक में अनुकूल हवाओं को पकड़ने के लिए अटलांटिक के एक विस्तृत चक्कर में यात्रा करना शामिल था।\n2. नाविक सीधे सौर कोणों से देशांतर (longitude) की गणना करने के लिए एस्ट्रोलैब का उपयोग करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "मध्यवर्ती यात्राओं के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. पेड्रो अल्वारेस कैब्राल ने कालीकट में पहली पुर्तगाली फैक्ट्री स्थापित की, जिसे बाद में 1500 ईस्वी में नष्ट कर दिया गया।\n2. वास्को डी गामा लाल सागर की नाकेबंदी करने के लिए कैब्राल द्वारा पीछे छोड़े गए गश्ती बेड़े के कमांडर थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "केप मार्ग के भू-राजनीतिक प्रभाव के संबंध में, निम्नलिखित कथनों पर विचार करें:\n1. इससे वेनिस के मसाला दलालों का वित्तीय उत्थान हुआ, जिन्होंने उत्तरी यूरोप में केप मसालों का वितरण किया।\n2. मसाला व्यापार के मार्ग परिवर्तन ने ममलुक मिस्र को कमजोर कर दिया, जिससे अप्रत्यक्ष रूप से 1517 में ओटोमन साम्राज्य द्वारा उसकी विजय आसान हो गई।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "पुर्तगाली एस्टाडो दा इंडिया के प्रशासन के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. एस्टाडो दा इंडिया की राजधानी को 1530 में नीनो दा कुन्हा द्वारा कोचीन से गोवा स्थानांतरित किया गया था।\n2. वास्को डी गामा ने 1524 में भ्रष्टाचार के आरोपों में दुआर्ते दे मेनेजेस को गिरफ्तार कर पुर्तगाल वापस भेज दिया।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "1502 ईस्वी में तीर्थयात्री जहाज मिरी घटना के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मिरी एक सशस्त्र मिस्र का युद्धपोत था जिसे मालाबार में पुर्तगाली फैक्ट्रियों पर हमला करने के लिए भेजा गया था।\n2. वास्को डी गामा ने जहाज को लूटा और उसमें आग लगा दी, जिससे सैकड़ों नागरिक यात्रियों की मौत हो गई।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?"
    ]
    q_hi["q"] = hi_questions[idx]
    q_hi["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
    
    hi_sols = [
        "कथन 1 गलत है क्योंकि उन्होंने केप ऑफ गुड होप (अटलांटिक मार्ग) का चक्कर लगाया था। कथन 2 सही है क्योंकि उन्होंने मालिंदी में नाविक अहमद इब्न मजीद की सेवाएं ली थीं।",
        "कथन 1 सही है। कथन 2 गलत है क्योंकि प्रस्तुत उपहार (कपड़े, टोपी, तेल) सस्ते थे और दरबार द्वारा उनका मज़ाक उड़ाया गया था।",
        "दोनों कथन सही हैं। गामा ने नौसैनिक कूटनीति के लिए 20 जहाजों का उपयोग किया और कोचीन के साथ गठबंधन किया, जिससे उनका पहला भारतीय आधार स्थापित हुआ।",
        "कथन 1 गलत है; प्रशासनिक भ्रष्टाचार को साफ करने के लिए उन्हें राजा जॉन तृतीय द्वारा नियुक्त किया गया था। कथन 2 सही है; कोचीन में मलेरिया से उनका निधन हो गया था।",
        "दोनों कथन सही हैं। व्यापारिक मार्गों को नियंत्रित करने और मसाला परिवहन को एकाधिकार में रखने के लिए कार्टाज प्रणाली को सख्ती से लागू किया गया था।",
        "कथन 1 सही है। कथन 2 गलत है; एस्ट्रोलैब का उपयोग अक्षांश (latitude) को मापने के लिए किया जाता था, देशांतर (longitude) की सीधे गणना के लिए नहीं।",
        "कथन 1 सही है। कथन 2 गलत है; लाल सागर गश्ती दल को स्वयं गामा ने 1503 में पीछे छोड़ा था और इसकी कमान विसेन्टे सोद्रे के पास थी।",
        "कथन 1 गलत है; वेनिस का पतन हुआ जबकि लिस्बन का उत्थान हुआ। कथन 2 सही है; मिस्र ने पारगमन कर खो दिए, जिससे ओटोमन विजय से पहले वे कमजोर हो गए।",
        "दोनों कथन सही हैं। राजधानी 1530 में गोवा स्थानांतरित की गई थी। गामा ने 1524 में भ्रष्टाचार के आरोप में मेनेजेस को निलंबित कर दिया था।",
        "कथन 1 गलत है; यह एक निहत्था नागरिक यात्री/तीर्थयात्री जहाज था। कथन 2 सही है; इसे गामा द्वारा लूटा और जला दिया गया था।"
    ]
    q_hi["sol"] = hi_sols[idx]
    mock_hi.append(q_hi)

generate_sec_file("mock", mock_en, mock_hi)

print("SUCCESS: Programmatically generated all Vasco da Gama questions.")
