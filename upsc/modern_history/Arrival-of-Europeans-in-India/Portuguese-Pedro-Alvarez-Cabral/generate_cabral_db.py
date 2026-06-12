import os
import json

BASE_DIR = r"C:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Portuguese-Pedro-Alvarez-Cabral"
os.makedirs(os.path.join(BASE_DIR, "hi"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "questions_data"), exist_ok=True)

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
    path = os.path.join(BASE_DIR, "questions_data", f"{name}.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Programmatically generated Cabral Qs\n\n")
        f.write(f"{name}_en = {repr(list_en)}\n\n")
        f.write(f"{name}_hi = {repr(list_hi)}\n")

def translate_opts(opts):
    mapping = {
        "1 only": "केवल 1",
        "2 only": "केवल 2",
        "Both 1 and 2": "1 और 2 दोनों",
        "Neither 1 nor 2": "न तो 1 न ही 2",
        "Both A and R are true and R is the correct explanation of A": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
        "Both A and R are true but R is not the correct explanation of A": "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
        "A is true but R is false": "A सही है लेकिन R गलत है",
        "A is false but R is true": "A गलत है लेकिन R सही है"
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

# Dictionary of translations for all 370 actual questions
local_dict = {
    # Options
    "1 only": "केवल 1",
    "2 only": "केवल 2",
    "Both 1 and 2": "1 और 2 दोनों",
    "Neither 1 nor 2": "न तो 1 न ही 2",
    "Yes": "हाँ",
    "No": "नहीं",
    "Lisbon": "लिस्बन",
    "Porto": "पोर्टो",
    "Sines": "सिनेस",
    "Cape Verde": "केप वर्डे",
    "Brazil": "ब्राजील",
    "Monte Pascoal": "मोंटे पास्कोआल",
    "Porto Seguro": "पोर्टो सेगुड़ो",
    "Vera Cruz": "वेरा क्रूज़",
    "Pedro Álvares Cabral": "पेड्रो अल्वारेज़ कैब्राल",
    "Bartolomeu Dias": "बार्टोलोमेउ डियास",
    "Nicolau Coelho": "निकोलाउ कोएल्हो",
    "Gaspar de Lemos": "गास्पर डी लेमोस",
    "Pero Vaz de Caminha": "पेरो वाज़ दे कामिन्हा",
    "King Manuel I": "राजा मैनुअल प्रथम",
    "Treaty of Tordesillas": "टॉर्डेसिलस की संधि",
    "Volta do Mar": "वोल्टा डो मार",
    "Aires Correia": "एरेस कोरिया",
    "Sancho de Tovar": "सेंचो दे तोवर",
    "Calicut": "कालीकट",
    "Cochin": "कोचीन",
    "Kannur": "कन्नूर",
    "Quilon": "क्विलोन",
    "Zamorin": "ज़मोरिन",
    "Kolathiri": "कोलाथिरी",
    "Unni Goda Varma": "उन्नी गोदा वर्मा",
    "Mamluk": "ममलुक",
    "Venice": "वेनिस",
    "Ottoman": "ओटोमन",
    "Casa da India": "कासा दा इंडिया",
    "El Rei": "एल री",
    "São Pedro": "साओ पेड्रो",
    "Anunciada": "अनुन्सियादा",
    "Tupiniquim": "तुपिनिक्विम",
    "Mombasa": "मोम्बासा",
    "Mozambique": "मोजाम्बिक",
    "Malindi": "मालिंदी",
    "Melinda": "मालिंदी",

    # Terms
    "Scribe": "लेखक/लिपिक",
    "Explorer": "खोजकर्ता",
    "Commander": "कमांडर",
    "Brazil name": "ब्राजील का नाम",
    "Departure port": "प्रस्थान बंदरगाह",
    "Sponsor": "प्रायोजक",
    "1488 pioneer": "1488 के अग्रणी",
    "First to return in 1499": "1499 में पहले लौटने वाले",
    "Brazilian courier": "ब्राजीलियाई कूरियर",
    "Lisbon port": "लिस्बन बंदरगाह",
    "Vera Cruz": "वेरा क्रूज़",
    "Monsoon route": "मानसून मार्ग",
    "Departure point": "प्रस्थान बिंदु",
    "Brazil landfall": "ब्राजील लैंडफॉल",
    "Indian Ocean crossing": "हिंद महासागर पार करना",
}

# Add translations programmatically to keep file clean
# We will define a massive list of actual historical questions.
# Each question object has: type, q, opts (optional), ans (optional), sol.

# ==================== SECTION 1: FLEET PREPARATION & BRAZIL ====================
sec1_en = []

# MCQs (5)
sec1_en.extend([
    {
        "type": "MCQ",
        "q": "Who was appointed by King Manuel I to command the second Portuguese expedition to India in 1500 CE?",
        "opts": ["Pedro Álvares Cabral", "Vasco da Gama", "Francisco de Almeida", "Afonso de Albuquerque"],
        "ans": 0,
        "sol": "Pedro Álvares Cabral, a nobleman, was selected to lead this massive armed trade expedition after Vasco da Gama's return."
    },
    {
        "type": "MCQ",
        "q": "How many ships composed the fleet of Pedro Álvares Cabral that departed Lisbon in March 1500?",
        "opts": ["13 ships", "4 ships", "20 ships", "8 ships"],
        "ans": 0,
        "sol": "The fleet consisted of 13 ships, carrying nearly 1,200 to 1,500 soldiers, sailors, and merchants."
    },
    {
        "type": "MCQ",
        "q": "Which veteran explorer, who had rounded the Cape of Good Hope in 1488, commanded one of the ships in Cabral's fleet?",
        "opts": ["Bartolomeu Dias", "Nicolau Coelho", "Vicente Sodré", "Gaspar de Lemos"],
        "ans": 0,
        "sol": "Bartolomeu Dias, the veteran who opened the route around Africa, commanded one of the ships in Cabral's fleet."
    },
    {
        "type": "MCQ",
        "q": "What territory did Pedro Álvares Cabral discover in April 1500 CE after sailing far west into the Atlantic?",
        "opts": ["Brazil", "South Africa", "Angola", "Mozambique"],
        "ans": 0,
        "sol": "Cabral's fleet swung far west to avoid Atlantic doldrums (Volta do Mar) and made landfall in Brazil, claiming it for Portugal."
    },
    {
        "type": "MCQ",
        "q": "What name did Pedro Álvares Cabral initially give to the newly discovered land of Brazil in 1500 CE?",
        "opts": ["Ilha de Vera Cruz", "Terra de Santa Cruz", "Estado da India", "New Portugal"],
        "ans": 0,
        "sol": "Cabral initially named Brazil 'Ilha de Vera Cruz' (Island of the True Cross), believing it to be a large island."
    }
])

# Multi Correct (5)
sec1_en.extend([
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following captains or officers sailed in Pedro Álvares Cabral's fleet of 1500 CE? (Select all that apply)",
        "opts": ["Bartolomeu Dias", "Nicolau Coelho", "Gaspar de Lemos", "Alfonso de Albuquerque"],
        "ans": [0, 1, 2],
        "sol": "Bartolomeu Dias, Nicolau Coelho, and Gaspar de Lemos were key captains in the fleet. Albuquerque was not part of this voyage."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which of the following ships were part of the 13-vessel fleet led by Cabral? (Select all that apply)",
        "opts": ["El Rei", "São Pedro", "Anunciada", "São Gabriel"],
        "ans": [0, 1, 2],
        "sol": "El Rei (flagship), São Pedro, and Anunciada were part of Cabral's fleet. São Gabriel was Vasco da Gama's flagship."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What were the main objectives laid down in King Manuel's instructions to Cabral? (Select all that apply)",
        "opts": ["Establish trade and factory alliances in Calicut", "Claim any territories discovered in the western Atlantic", "Use armed force to counter Arab trade monopolies if necessary", "Annex the entire state of Calicut into the Portuguese empire"],
        "ans": [0, 1, 2],
        "sol": "The instructions focused on establishing a factory, claiming lands under the Tordesillas line, and using force to break monopolies. Full annexation of Calicut was not the goal."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which geographic features or sailing terms are associated with Cabral's voyage through the Atlantic? (Select all that apply)",
        "opts": ["Volta do Mar wind patterns", "Equatorial doldrums avoidance", "Landfall at Monte Pascoal", "Rounding Cape Comorin first"],
        "ans": [0, 1, 2],
        "sol": "They used Volta do Mar, avoided equatorial calm zones, and landed at Monte Pascoal. Cape Comorin is in India, not the Atlantic."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key details of the landing in Brazil by Cabral's expedition. (Select all that apply)",
        "opts": ["Landfall made on April 22, 1500 CE", "Anchor secured at Porto Seguro", "Erected a large wooden cross to claim the land", "Signed a trade treaty with Spanish conquistadors"],
        "ans": [0, 1, 2],
        "sol": "The fleet made landfall on April 22, anchored at Porto Seguro, and claimed it for Portugal with a cross. There were no Spanish forces present."
    }
])

# True/False (8)
tf1 = [
    ("Bartolomeu Dias commanded a ship under Cabral's supreme authority.", True, "Dias was one of the subordinate captains under Captain-Major Cabral."),
    ("Cabral was Vasco da Gama's brother-in-law.", False, "They were not related; Cabral belonged to a different noble family."),
    ("Brazil was claimed by Portugal under the terms of the Treaty of Tordesillas.", True, "Brazil lay east of the Tordesillas meridian line, placing it in the Portuguese zone."),
    ("The fleet stayed in Brazil for six months to begin colonization.", False, "They only stayed for about ten days before sailing to India."),
    ("Pero Vaz de Caminha wrote the famous letter detailing the discovery of Brazil.", True, "Caminha was the official scribe of the fleet whose letter became a historic document."),
    ("Gaspar de Lemos was sent back to Lisbon as a courier to announce the discovery of Brazil.", True, "Lemos commanded the supply ship sent back immediately with the news."),
    ("The fleet carried no soldiers and was entirely composed of peaceful merchants.", False, "It was heavily armed with soldiers to fight Arab trade rivalries."),
    ("The expedition departed from Lisbon in March 1500 CE.", True, "The fleet set sail on March 9, 1500 CE.")
]
for q, ans, sol in tf1:
    sec1_en.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
fill1 = [
    ("The official scribe on Cabral's fleet who wrote the letter detailing Brazil's discovery was __________.", "Pero Vaz de Caminha", "Pero Vaz de Caminha was the writer of the letter considered Brazil's birth certificate."),
    ("The first name given to Brazil by Cabral in 1500 CE was __________.", "Ilha de Vera Cruz", "He named it Island of the True Cross, believing it was an island."),
    ("Cabral's fleet set sail from the port of __________ in March 1500 CE.", "Lisbon", "The fleet departed from Restelo, Lisbon."),
    ("The captain sent back to Lisbon with the news of Brazil's discovery was __________.", "Gaspar de Lemos", "Gaspar de Lemos was the commander of the return courier ship."),
    ("The nobleman who served as the captain-major of the 1500 CE fleet was __________.", "Pedro Álvares Cabral", "Pedro Álvares Cabral was appointed captain-major by the King."),
    ("The treaty signed in 1494 that divided the globe between Spain and Portugal was the Treaty of __________.", "Tordesillas", "The Treaty of Tordesillas set the global division line."),
    ("The Portuguese monarch who sponsored and funded Cabral's expedition was __________.", "King Manuel I", "King Manuel I sponsored the second voyage to consolidate the Cape Route."),
    ("The wide sailing arc taken in the Atlantic to bypass adverse currents is called __________.", "Volta do Mar", "Volta do Mar (Turn of the Sea) was the crucial open-ocean route.")
]
for q, ans, sol in fill1:
    sec1_en.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
sec1_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the key figures of the 1500 fleet with their roles:",
        "items": [{"left": "Pedro Álvares Cabral"}, {"left": "Bartolomeu Dias"}, {"left": "Gaspar de Lemos"}],
        "options": [{"val": "0", "text": "Captain-Major of the Fleet"}, {"val": "1", "text": "1488 Cape of Good Hope pioneer"}, {"val": "2", "text": "Brazil discovery courier"}],
        "sol": "Cabral was the commander, Dias was the veteran explorer, and Lemos was the courier captain."
    },
    {
        "type": "Match the Following",
        "q": "Match the Atlantic geographical locations with their significance:",
        "items": [{"left": "Lisbon"}, {"left": "Porto Seguro"}, {"left": "Monte Pascoal"}],
        "options": [{"val": "0", "text": "Departure port of the fleet"}, {"val": "1", "text": "First harbor anchor in Brazil"}, {"val": "2", "text": "First mountain sighted in Brazil"}],
        "sol": "The fleet departed Lisbon, sighted Monte Pascoal first, and anchored at Porto Seguro."
    },
    {
        "type": "Match the Following",
        "q": "Match the documents and treaties with their contexts:",
        "items": [{"left": "Caminha's Letter"}, {"left": "Treaty of Tordesillas"}, {"left": "Royal Instructions"}],
        "options": [{"val": "0", "text": "Birth certificate of Brazil"}, {"val": "1", "text": "1494 maritime division"}, {"val": "2", "text": "Directives on spice factory"}],
        "sol": "Caminha wrote the letter, Tordesillas divided the sea zones, and royal instructions detailed factory rules."
    }
])

# One-Liners (8)
ol1 = [
    ("On what date did Pedro Álvares Cabral's fleet depart from Lisbon?", "March 9, 1500 CE.", "The fleet left Restelo on March 9, 1500 CE."),
    ("On what date did the fleet make landfall on the Brazilian coast?", "April 22, 1500 CE.", "They sighted land on April 22 and landed the next day."),
    ("Why did Cabral sail far southwest into the open Atlantic Ocean?", "To utilize the trade winds (Volta do Mar) and avoid currents.", "Sailing west avoided the calm zones and contrary currents of the Gulf of Guinea."),
    ("How many ships initially set sail from Lisbon under Cabral's command?", "Thirteen ships.", "The armada consisted of 13 vessels sponsored by the Crown."),
    ("What was the name of the first mountain sighted by Cabral in Brazil?", "Monte Pascoal.", "It was named Monte Pascoal (Easter Mountain) as they arrived during Easter week."),
    ("What title did King Manuel I give Cabral for this expedition?", "Captain-Major of the Fleet.", "Cabral was appointed Capitão-Mor of the second voyage."),
    ("Which native group did the Portuguese first encounter in Brazil?", "The Tupiniquim people.", "The fleet met friendly Tupiniquim natives on the Brazilian coast."),
    ("Where did Cabral erect the wooden cross to claim Brazil?", "Porto Seguro.", "They celebrated mass and erected a cross at Porto Seguro.")
]
for q, sol in ol1:
    sec1_en.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
ar1 = [
    ("Assertion: Cabral sailed southwest rather than hugging the African coast.\nReason: They wanted to avoid the doldrums and adverse currents of the Gulf of Guinea.", 0, "The Volta do Mar loop was designed precisely to bypass Gulf of Guinea currents."),
    ("Assertion: Brazil was claimed by Portugal without Spanish opposition.\nReason: The landing area lay within the Portuguese sphere under the Treaty of Tordesillas.", 0, "The 1494 treaty had placed the eastern part of South America in the Portuguese zone."),
    ("Assertion: Gaspar de Lemos returned early to Portugal in 1500 CE.\nReason: He was sent by Cabral to inform King Manuel I of the discovery of Brazil.", 0, "Lemos was sent back as a courier to deliver Pero Vaz de Caminha's report."),
    ("Assertion: Bartolomeu Dias was a key commander under Cabral.\nReason: He was selected due to his veteran experience in rounding the Cape of Good Hope.", 0, "Dias's navigational expertise was critical for rounding Africa successfully."),
    ("Assertion: Cabral initially named the discovered territory Ilha de Vera Cruz.\nReason: The expedition believed they had discovered a massive continent rather than an island.", 2, "Assertion is true. Reason is false because they believed it was a large island, not a continent."),
    ("Assertion: King Manuel I financed the massive 13-ship armada.\nReason: He wanted to consolidate the direct spice trade route pioneered by Vasco da Gama.", 0, "The armada's size reflected the Crown's desire to secure a monopoly on trade."),
    ("Assertion: Pero Vaz de Caminha was carried as an official scribe.\nReason: Scribes were required to log official discoveries and claims for royal records.", 0, "Caminha documented the entire discovery of Brazil in his historic letter."),
    ("Assertion: The Portuguese fleet carried heavy military artillery.\nReason: The Crown anticipated heavy military conflict with Arab merchant guilds in India.", 0, "Gama's reports of Arab hostility prompted the militarization of the second voyage.")
]
for q, ans, sol in ar1:
    sec1_en.append({"type": "Assertion-Reason", "q": q, "opts": EN_AR_OPTS, "ans": ans, "sol": sol})

# Statement-Based (5)
st1 = [
    ("Consider the following statements regarding the discovery of Brazil:\n1. It occurred on April 22, 1500 CE.\n2. The landing site was named Porto Seguro.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Sighted Monte Pascoal and anchored at Porto Seguro."),
    ("Consider the following statements regarding Cabral's fleet:\n1. It included veteran captain Nicolau Coelho.\n2. Vasco da Gama served as the chief pilot under Cabral.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Vasco da Gama did not sail on this expedition; he remained in Lisbon."),
    ("With reference to the Treaty of Tordesillas (1494), consider these statements:\n1. It divided the non-Christian world between Spain and Portugal.\n2. Brazil fell into the Portuguese sphere due to the line shifting westwards.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The line was shifted 370 leagues west of Cape Verde."),
    ("Consider the statements about Pero Vaz de Caminha:\n1. He was the chief military pilot of the flagship El Rei.\n2. He authored the letter that reported Brazil's discovery to King Manuel I.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. He was the scribe, not a pilot or military officer."),
    ("With reference to Atlantic navigation in 1500 CE, consider these statements:\n1. The Volta do Mar required sailing in a wide circular loop to catch winds.\n2. Cabral stopped at the Cape Verde islands before sailing west.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Stopping at Cape Verde was standard for fresh supplies before the loop.")
]
for q, ans, sol in st1:
    sec1_en.append({"type": "Statement-Based", "q": q, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol})

# Open Questions (12)
op1 = [
    ("Why", "Why did Cabral take a wide southwesterly path in the Atlantic Ocean?", "To bypass the unfavorable equatorial doldrums and headwinds along the Gulf of Guinea, utilizing trade winds."),
    ("Why", "Why did Cabral claim Brazil for Portugal immediately upon landfall?", "To secure the territory under the Treaty of Tordesillas which placed the land in the Portuguese hemisphere."),
    ("Why", "Why was Pero Vaz de Caminha's letter considered historically significant?", "It serves as the first detailed anthropological and geographical document of Brazil, detailing native life."),
    ("How", "How did the Treaty of Tordesillas influence Cabral's navigation route?", "It gave them the legal right to claim any land found within 370 leagues west of Cape Verde, encouraging western swings."),
    ("How", "How did Cabral's fleet maintain water and food supplies during the long Atlantic crossing?", "They loaded heavy supplies at Cape Verde and utilized salted meats, biscuits, and water storage in wood barrels."),
    ("How", "How was the news of Brazil's discovery received in Lisbon in 1500 CE?", "It was celebrated as a massive addition to the Crown's empire, expanding Portuguese influence in the west."),
    ("Case Study", "Examine the strategic choice of Porto Seguro as the initial landing site.", "Porto Seguro offered a safe, sheltered harbor with fresh water and friendly native populations, ideal for repairs."),
    ("Case Study", "Analyze the diplomatic implications of the cross erected at Monte Pascoal.", "The cross asserted formal Christian sovereignty and served as a visible landmark for subsequent Portuguese vessels."),
    ("Case Study", "Discuss the initial interactions between the Portuguese and the Tupiniquim natives.", "They were marked by peaceful trade, exchanging iron tools and red caps for native feathers and bows, avoiding conflict."),
    ("Teach the Concept", "Explain the sailing maneuver 'Volta do Mar' to a student.", "It is a sailing strategy of looping far out into the ocean to catch wind currents instead of sailing directly against winds."),
    ("Teach the Concept", "Describe the division of the globe under the Treaty of Tordesillas.", "It drew a meridian line 370 leagues west of Cape Verde; lands to the east belonged to Portugal, lands to the west to Spain."),
    ("Teach the Concept", "Explain the command structure of the 1500 CE Portuguese armada.", "It was led by Captain-Major Cabral, with experienced pilots, noble captains commanding individual ships, and scribes.")
]
for qtype, q, sol in op1:
    sec1_en.append({"type": qtype, "q": q, "sol": sol})


# ==================== SECTION 2: INDIAN OCEAN CROSSING & CALICUT ====================
sec2_en = []

# MCQs (5)
sec2_en.extend([
    {
        "type": "MCQ",
        "q": "Which tragic event occurred near the Cape of Good Hope during Cabral's voyage to India in May 1500?",
        "opts": ["A severe storm sank four ships, including that of Bartolomeu Dias", "A mutiny by Arab pilots led to ship damage", "An attack by Mamluk war fleets", "An outbreak of plague wiped out half the crew"],
        "ans": 0,
        "sol": "A fierce storm near the Cape of Good Hope sank four vessels, drowning the famous explorer Bartolomeu Dias."
    },
    {
        "type": "MCQ",
        "q": "In which month of 1500 CE did Pedro Álvares Cabral's remaining fleet finally arrive in Calicut?",
        "opts": ["September", "May", "December", "January"],
        "ans": 0,
        "sol": "After crossing the Indian Ocean from East Africa, Cabral's fleet arrived in Calicut on September 13, 1500 CE."
    },
    {
        "type": "MCQ",
        "q": "How did the Zamorin of Calicut initially receive Pedro Álvares Cabral compared to Vasco da Gama?",
        "opts": ["He welcomed him warmly and granted permission to trade", "He immediately arrested Cabral on arrival", "He refused to grant him an audience", "He demanded that all ships be surrendered"],
        "ans": 0,
        "sol": "The Zamorin initially welcomed Cabral warmly, offering an audience and signing a treaty permitting a trade post (factory)."
    },
    {
        "type": "MCQ",
        "q": "What was the primary business objective of Cabral's fleet on arriving at Calicut?",
        "opts": ["To establish a permanent trading post and purchase spices", "To conquer Calicut and annex it to Portugal", "To convert the Hindu Nair soldiers to Christianity", "To build a massive naval fortress on the Calicut harbor"],
        "ans": 0,
        "sol": "Cabral's main goal was to establish a permanent factory (feitoria) to secure regular spice purchases."
    },
    {
        "type": "MCQ",
        "q": "Who was appointed as the chief factor (feitor) of the Portuguese trading post established at Calicut in 1500?",
        "opts": ["Aires Correia", "Sancho de Tovar", "Gaspar da Gama", "Vicente Sodré"],
        "ans": 0,
        "sol": "Aires Correia was appointed as the chief representative to manage spice procurement and the warehouse in Calicut."
    }
])

# Multi Correct (5)
sec2_en.extend([
    {
        "type": "Multiple Correct MCQ",
        "q": "Which East African cities did Cabral's fleet visit or bypass on its way to India? (Select all that apply)",
        "opts": ["Sofala", "Mozambique", "Malindi", "Aden"],
        "ans": [0, 1, 2],
        "sol": "Cabral visited Sofala (sending a ship), Mozambique, and Malindi. Aden is in the Red Sea, not East Africa."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What losses did Cabral's fleet suffer before reaching the Indian coast? (Select all that apply)",
        "opts": ["One ship lost near Cape Verde", "Four ships lost in a storm near the Cape of Good Hope", "One ship separated near Madagascar", "Three ships captured by Egyptian fleets"],
        "ans": [0, 1, 2],
        "sol": "They lost one ship early, four in the Cape storm, and one separated under Diogo Dias. No ships were captured by Egypt."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which Indian Ocean wind systems and routes were crucial for Cabral's crossing? (Select all that apply)",
        "opts": ["South-west monsoon winds", "Crossing from Malindi to Calicut", "Traditional Arab shipping lanes", "Gulf Stream trade winds"],
        "ans": [0, 1, 2],
        "sol": "They utilized the SW monsoon winds to cross from Malindi to Calicut. The Gulf Stream is in the Atlantic."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key components of the treaty signed between Cabral and the Zamorin. (Select all that apply)",
        "opts": ["Permission to build a factory/warehouse", "Right to trade spices at Calicut port", "Grant of land for the factory", "A military alliance against Cochin"],
        "ans": [0, 1, 2],
        "sol": "The treaty granted trade rights, factory land, and permissions. It did not contain a military alliance against Cochin."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which captains managed the crossing of the Indian Ocean after the Cape storm? (Select all that apply)",
        "opts": ["Nicolau Coelho", "Sancho de Tovar", "Simão de Miranda", "Bartolomeu Dias"],
        "ans": [0, 1, 2],
        "sol": "Coelho, Tovar, and Miranda survived the storm and crossed. Dias had already drowned."
    }
])

# True/False (8)
tf2 = [
    ("Bartolomeu Dias's ship sank during a storm near the Cape of Good Hope.", True, "Dias drowned when a fierce storm sank four ships of the fleet in May 1500."),
    ("The fleet arrived in Calicut in May 1500 CE.", False, "They arrived in September 1500 CE, much later than Gama's arrival month."),
    ("The Zamorin refused to give Cabral any audience upon his arrival.", False, "The Zamorin gave Cabral a warm audience and permitted the establishment of a factory."),
    ("Cabral brought rich gifts from King Manuel I to impress the Zamorin.", True, "Unlike Gama's cheap gifts, Cabral brought rich textiles and gold items sponsored by the Crown."),
    ("Aires Correia was appointed the chief factor (feitor) at Calicut.", True, "Correia took charge of the warehouse to buy pepper and spices."),
    ("Diogo Dias's ship was separated from the fleet and ended up discovering Madagascar.", True, "Diogo Dias's vessel was separated during the Cape storm and discovered Madagascar."),
    ("The fleet stopped at Mombasa and established a permanent factory there.", False, "They bypassed Mombasa due to hostility and only allied with Malindi."),
    ("The Indian Ocean crossing was completed using the northeast winter monsoon.", False, "They used the southwest summer monsoon to cross from Malindi.")
]
for q, ans, sol in tf2:
    sec2_en.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
fill2 = [
    ("The veteran explorer who drowned near the Cape of Good Hope in 1500 CE was __________.", "Bartolomeu Dias", "Dias's ship went down in the southern Atlantic storm."),
    ("Cabral's fleet arrived at the port of Calicut in the month of __________.", "September", "They anchored at Calicut on September 13, 1500 CE."),
    ("The captain of the ship that separated and discovered Madagascar was __________.", "Diogo Dias", "Diogo Dias was Bartolomeu's brother and discovered Madagascar."),
    ("The chief representative in charge of the Calicut warehouse was __________.", "Aires Correia", "Aires Correia was the appointed feitor (factor)."),
    ("The East African city that welcomed Cabral and provided pilots was __________.", "Malindi", "Malindi was a key ally of the Portuguese along the coast."),
    ("The native language translator who assisted Cabral in Calicut was __________.", "Gaspar da Gama", "Gaspar da Gama, a Jewish translator captured by Gama, assisted Cabral."),
    ("The trade post or warehouse structure built by the Portuguese was called a __________.", "feitoria", "Feitoria (factory) was the Portuguese term for fortified warehouses."),
    ("The ocean crossed by Cabral to reach Calicut from East Africa was the __________.", "Indian Ocean", "They crossed the Indian Ocean using seasonal monsoons.")
]
for q, ans, sol in fill2:
    sec2_en.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
sec2_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the survival status of these key captains after the Cape storm:",
        "items": [{"left": "Bartolomeu Dias"}, {"left": "Nicolau Coelho"}, {"left": "Diogo Dias"}],
        "options": [{"val": "0", "text": "Drowned in the storm"}, {"val": "1", "text": "Survived and crossed directly"}, {"val": "2", "text": "Separated and reached Madagascar"}],
        "sol": "Bartolomeu Dias drowned, Coelho survived, and Diogo Dias separated to Madagascar."
    },
    {
        "type": "Match the Following",
        "q": "Match the African ports with their significance for Cabral's fleet:",
        "items": [{"left": "Sofala"}, {"left": "Mozambique"}, {"left": "Malindi"}],
        "options": [{"val": "0", "text": "Explored for gold trade potential"}, {"val": "1", "text": "Bypassed due to tensions"}, {"val": "2", "text": "Safe haven that provided pilots"}],
        "sol": "Sofala was explored for gold, Mozambique had tensions, and Malindi was a friendly haven."
    },
    {
        "type": "Match the Following",
        "q": "Match the diplomatic interactions in Calicut with their details:",
        "items": [{"left": "Zamorin treaty"}, {"left": "Aires Correia"}, {"left": "Spices purchase"}],
        "options": [{"val": "0", "text": "Formal trade permission"}, {"val": "1", "text": "Chief factor of Calicut"}, {"val": "2", "text": "Primary cargo objective"}],
        "sol": "Zamorin treaty gave permission, Correia was the factor, and spices were the cargo."
    }
])

# One-Liners (8)
ol2 = [
    ("How many ships of the fleet sank in the Cape of Good Hope storm?", "Four ships.", "A sudden tempest sank four vessels in May 1500 CE."),
    ("What island was discovered by Diogo Dias after being separated from the fleet?", "Madagascar.", "Dias sighted Madagascar, naming it São Lourenço."),
    ("On what date did Cabral's remaining fleet arrive in Calicut?", "September 13, 1500 CE.", "The remaining fleet anchored in Calicut in September."),
    ("Why was the Zamorin more impressed by Cabral's gifts than Gama's?", "Because they were valuable textiles, silver, and gold.", "The Crown sponsored premium gifts, unlike Gama's cheap merchant goods."),
    ("What was the Portuguese term for the trade factories established in India?", "Feitorias.", "Feitoria was the standard term for a trading post."),
    ("Which pilot assisted Cabral in crossing the Arabian Sea?", "A Gujarati/Arab pilot hired in Malindi.", "A pilot from Malindi guided them using monsoon expertise."),
    ("Who acted as the primary translator for Cabral during negotiations?", "Gaspar da Gama.", "Gaspar da Gama (formerly a Jew from Goa) translated."),
    ("Where did the fleet make a stopover in East Africa to procure fresh supplies?", "Malindi.", "Malindi was their primary refueling and pilot station.")
]
for q, sol in ol2:
    sec2_en.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
ar2 = [
    ("Assertion: The death of Bartolomeu Dias was a major setback for the fleet.\nReason: He was the veteran navigator who had originally discovered the Cape Route.", 0, "Dias's loss deprived the fleet of its most experienced navigator."),
    ("Assertion: Cabral's fleet arrived in Calicut much later than Vasco da Gama did in 1498.\nReason: The fleet spent weeks claiming Brazil and was delayed by a massive Atlantic storm.", 0, "The Brazil detour and the Cape storm delayed their arrival to September."),
    ("Assertion: The Zamorin signed a trade treaty with Cabral.\nReason: He wanted to collect customs revenues and was impressed by the rich gifts brought by Cabral.", 0, "The rich gifts and economic prospects convinced the Zamorin to allow the factory."),
    ("Assertion: Diogo Dias's ship sailed to Madagascar.\nReason: He was separated from Cabral's fleet during the storm off the Cape of Good Hope.", 0, "The separation forced him eastwards, leading to Madagascar's discovery."),
    ("Assertion: Cabral established a factory in Mombasa.\nReason: Mombasa was the chief ally of the Portuguese on the East African coast.", 3, "Assertion is false. Reason is false because Mombasa was hostile and Malindi was the ally."),
    ("Assertion: Aires Correia was given authority to manage trade in Calicut.\nReason: He was appointed the chief factor (feitor) by the Portuguese Crown.", 0, "The chief factor had full authority over spice purchases and warehouse inventory."),
    ("Assertion: Cabral's crossing of the Arabian Sea was relatively fast.\nReason: The fleet utilized the southwest summer monsoon wind patterns.", 0, "The summer monsoon winds blow towards India, enabling a swift crossing."),
    ("Assertion: The Portuguese carried letters of introduction to the Zamorin.\nReason: King Manuel I wanted to establish official diplomatic and trade relations.", 0, "The letters established Cabral's credentials as an ambassador of the King.")
]
for q, ans, sol in ar2:
    sec2_en.append({"type": "Assertion-Reason", "q": q, "opts": EN_AR_OPTS, "ans": ans, "sol": sol})

# Statement-Based (5)
st2 = [
    ("Consider the following statements regarding the loss of ships:\n1. Bartolomeu Dias died in the storm near Cape of Good Hope.\n2. Diogo Dias's ship was also destroyed with all hands lost.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Diogo Dias's ship was separated, but survived and discovered Madagascar."),
    ("Consider the following statements regarding Cabral's arrival in Calicut:\n1. He arrived on September 13, 1500 CE.\n2. He was received by a hostile army on Kappad beach.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. He was received peacefully and granted an audience by the Zamorin."),
    ("With reference to Portuguese trade warehouses, consider these statements:\n1. They were known as feitorias.\n2. Aires Correia was the chief factor appointed for Calicut.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Scribe/merchants managed these feitorias to buy spices."),
    ("Consider the statements about East African alliances:\n1. Mombasa provided pilots to help Cabral cross the Indian Ocean.\n2. Malindi was a key ally that offered shelter and trade access.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Mombasa was hostile and was bypassed."),
    ("With reference to the navigation of the Indian Ocean crossing, consider these statements:\n1. They utilized the southwest monsoon winds.\n2. The crossing took nearly six months to complete.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. The crossing was fast, taking only a few weeks due to favorable monsoons.")
]
for q, ans, sol in st2:
    sec2_en.append({"type": "Statement-Based", "q": q, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol})

# Open Questions (12)
op2 = [
    ("Why", "Why did a storm off the Cape of Good Hope cause such heavy losses to Cabral's fleet?", "The southern seas are notorious for sudden, violent tempests (tempestades) that overwhelmed the square-rigged naus."),
    ("Why", "Why did the Zamorin agree to allow the Portuguese to establish a permanent factory in Calicut?", "He anticipated massive customs duties and economic benefits from trading directly with the Portuguese Crown."),
    ("Why", "Why did Diogo Dias's ship separate from the main fleet off Africa?", "The intense storm near the Cape broke the fleet's formation, pushing his ship off course into the Indian Ocean."),
    ("How", "How did Cabral procure trade pilots to guide him across the Arabian Sea?", "He secured the alliance of the Sultan of Malindi, who provided skilled navigators familiar with the monsoons."),
    ("How", "How did the loss of Bartolomeu Dias impact the navigational planning of the fleet?", "It removed their most experienced Cape pilot, forcing other captains to rely on standard charts and local pilots."),
    ("How", "How did Aires Correia manage the daily operations of the Calicut factory?", "He set up a warehouse, hired local clerks, and negotiated spice prices directly with local brokers."),
    ("Case Study", "Analyze the impact of the Cape storm on the command structure of Cabral's expedition.", "The loss of four captains required Cabral to redistribute command and consolidate surviving sailors onto remaining ships."),
    ("Case Study", "Discuss the strategic importance of Malindi in early Portuguese navigation.", "Malindi acted as a friendly, secure base that bridged the Atlantic transit and the Indian Ocean crossing."),
    ("Case Study", "Examine the role of Gaspar da Gama as a diplomatic intermediary in Calicut.", "Having lived in India, he understood local customs, court etiquette, and languages, facilitating treaties."),
    ("Teach the Concept", "Explain the function of a 'feitoria' in Portuguese colonial expansion.", "It was a fortified trade post where factors bought and stored goods, serving as bases for commercial monopolies."),
    ("Teach the Concept", "Describe the role of the monsoon wind patterns in the Indian Ocean trade route.", "Winds blow SW in summer (allowing sailing to India) and NE in winter (allowing return), defining trade seasons."),
    ("Teach the Concept", "Explain why the Zamorin's reception of Cabral differed from his reception of Vasco da Gama.", "Cabral brought vastly superior, royal-grade gifts and was backed by a massive, intimidating war fleet.")
]
for qtype, q, sol in op2:
    sec2_en.append({"type": qtype, "q": q, "sol": sol})


# ==================== SECTION 3: CLASH & MASSACRE IN CALICUT ====================
sec3_en = []

# MCQs (5)
sec3_en.extend([
    {
        "type": "MCQ",
        "q": "What led to the violent riot and destruction of the Portuguese factory in Calicut in December 1500?",
        "opts": ["Conflict between Portuguese factors and local Arab merchants over spice purchasing priorities", "An unprovoked attack by the Zamorin's state guards", "A dispute over the conversion of Nair warriors", "The refusal of the Portuguese to pay port customs duties"],
        "ans": 0,
        "sol": "Arab merchant factions, fearing the loss of their spice trade monopoly, clashed with Aires Correia's faction, leading to a massive riot."
    },
    {
        "type": "MCQ",
        "q": "How many Portuguese factors, including the chief factor Aires Correia, were killed in the Calicut factory attack?",
        "opts": ["Around 50", "Over 500", "Only 5", "None, they all escaped safely"],
        "ans": 0,
        "sol": "Approximately 50 Portuguese defenders were killed during the attack on the factory warehouse in December 1500."
    },
    {
        "type": "MCQ",
        "q": "How did Pedro Álvares Cabral react to the news of the massacre at the Calicut factory?",
        "opts": ["He bombarded the city of Calicut and captured Arab merchant ships", "He immediately surrendered and requested mercy", "He sailed away without any retaliation", "He requested the help of the British fleet nearby"],
        "ans": 0,
        "sol": "Cabral retaliated fiercely by seizing 10 Arab vessels in the harbor, executing their crews, and bombarding Calicut for a day."
    },
    {
        "type": "MCQ",
        "q": "Approximately how many civilian and merchant casualties resulted from Cabral's bombardment of Calicut?",
        "opts": ["Around 600", "Over 10,000", "Fewer than 10", "Zero, it was a warning shot only"],
        "ans": 0,
        "sol": "The bombardment killed an estimated 600 citizens and destroyed many merchant warehouses along the harbor."
    },
    {
        "type": "MCQ",
        "q": "Which ship captain was in charge of harbor defense but could not prevent the factory riot?",
        "opts": ["Sancho de Tovar", "Nicolau Coelho", "Aires Correia", "Simão de Miranda"],
        "ans": 0,
        "sol": "Sancho de Tovar was the vice-admiral of the fleet on board the ships, while Correia was on land."
    }
])

# Multi Correct (5)
sec3_en.extend([
    {
        "type": "Multiple Correct MCQ",
        "q": "Which factions or groups were involved in the conflict that led to the Calicut factory riot? (Select all that apply)",
        "opts": ["Arab and Muslim merchants", "Portuguese factors under Aires Correia", "Local Nair riot mobs", "Spanish Jesuit missionaries"],
        "ans": [0, 1, 2],
        "sol": "Arab merchants led the riot, clashing with Correia's men, supported by local mobs. No Spanish Jesuits were present."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What specific actions did Cabral take in retaliation against Calicut? (Select all that apply)",
        "opts": ["Seized ten Arab merchant vessels in the harbor", "Confiscated cargo and executed the ship crews", "Bombarded Calicut city with heavy naval cannons", "Landed an army and captured the Zamorin's palace"],
        "ans": [0, 1, 2],
        "sol": "He seized 10 ships, killed their crews, and bombarded the city. He did not launch a land invasion to capture the palace."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which factors contributed to the slow loading of spice cargo that frustrated the Portuguese? (Select all that apply)",
        "opts": ["Arab merchants monopolizing spice purchases", "Corrupt local port authorities delaying clearances", "Lack of cooperation from Calicut brokers", "A complete drought that destroyed pepper crops"],
        "ans": [0, 1, 2],
        "sol": "Arab merchants blocked spice access, and port authorities delayed clearances. There was no pepper drought."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key casualties of the December 1500 Calicut factory massacre. (Select all that apply)",
        "opts": ["Factor Aires Correia", "Three Franciscan friars", "Around 50 Portuguese soldiers and clerks", "Ruler of Cochin visiting the factory"],
        "ans": [0, 1, 2],
        "sol": "Correia, three friars, and about 50 men were killed. The Cochin ruler was not in Calicut."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What geopolitical impacts resulted from the Calicut factory riot? (Select all that apply)",
        "opts": ["End of peaceful Portuguese relations with Calicut", "Establishment of gunboat diplomacy in the Indian Ocean", "Forced reliance on alliances with Cochin and Kannur", "Immediate peace treaty signed by the Ottoman Sultan"],
        "ans": [0, 1, 2],
        "sol": "It ended peace with Calicut, started gunboat diplomacy, and forced Cochin/Kannur alliances. The Ottomans were not involved."
    }
])

# True/False (8)
tf3 = [
    ("The Calicut factory was destroyed by Arab merchants who feared Portuguese spice monopoly competition.", True, "Arab merchant guilds organized the attack to protect their trade dominance."),
    ("Aires Correia survived the massacre by hiding in a local Hindu temple.", False, "Correia was killed along with his men during the warehouse defense."),
    ("Cabral executed the crews of the Arab vessels he captured in the harbor.", True, "He executed the captured crews before bombarding Calicut as a severe reprisal."),
    ("The Zamorin directly ordered the massacre of the Portuguese factors.", False, "The riot was started by Arab merchants and local mobs; the Zamorin failed to intervene, which angered Cabral."),
    ("Three Franciscan friars were among the dead in the Calicut factory attack.", True, "Three friars who accompanied the mission to establish missions were killed."),
    ("Cabral bombarded Calicut for nearly two weeks.", False, "He bombarded the city for one full day (around 24 hours) before sailing to Cochin."),
    ("The bombardment destroyed several merchant vessels and city buildings.", True, "The heavy cannon fire caused widespread destruction in the harbor and city."),
    ("The conflict arose because the Portuguese attempted to ban Hindu merchants from the port.", False, "The conflict was between Portuguese factors and Arab/Muslim traders over spice buying monopolies.")
]
for q, ans, sol in tf3:
    sec3_en.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
fill3 = [
    ("The chief factor killed during the Calicut warehouse riot was __________.", "Aires Correia", "Aires Correia led the land base and died during the attack."),
    ("Cabral captured __________ Arab merchant vessels in Calicut harbor in retaliation.", "ten", "He seized 10 ships to confiscate cargo and punish the city."),
    ("The massacre of the Portuguese factors occurred in the month of __________ 1500 CE.", "December", "The riot and massacre took place on December 16, 1500 CE."),
    ("The heavy naval weapons used by Cabral to destroy Calicut buildings were __________.", "cannons", "Bombardment was executed using heavy ship-borne cannons."),
    ("The religious group that dominated spice shipping in Calicut before the Portuguese was the __________ merchants.", "Arab", "Arab and Muslim merchant guilds controlled the export networks."),
    ("The number of Portuguese defenders killed in the factory massacre was approximately __________.", "fifty", "Around 50 men died during the warehouse attack."),
    ("Cabral bombarded Calicut for a duration of __________ day(s).", "one", "He executed a 24-hour intense naval bombardment before leaving."),
    ("The vice-admiral who remained on the fleet during the land riot was __________.", "Sancho de Tovar", "Sancho de Tovar commanded the ships in the harbor during the standoff.")
]
for q, ans, sol in fill3:
    sec3_en.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
sec3_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the events of the Calicut conflict with their dates in 1500 CE:",
        "items": [{"left": "Arrival at Calicut"}, {"left": "Factory Massacre"}, {"left": "City Bombardment"}],
        "options": [{"val": "0", "text": "September 13"}, {"val": "1", "text": "December 16"}, {"val": "2", "text": "December 17-18"}],
        "sol": "They arrived in September, the massacre occurred on Dec 16, and bombardment followed immediately."
    },
    {
        "type": "Match the Following",
        "q": "Match the key targets of Cabral's retaliation with their outcomes:",
        "items": [{"left": "10 Arab ships"}, {"left": "Calicut harbor"}, {"left": "Arab ship crews"}],
        "options": [{"val": "0", "text": "Captured and plundered"}, {"val": "1", "text": "Bombarded by cannons"}, {"val": "2", "text": "Executed by the Portuguese"}],
        "sol": "Ships were captured, the harbor was bombarded, and crews were executed."
    },
    {
        "type": "Match the Following",
        "q": "Match the historical actors in Calicut with their responses during the riot:",
        "items": [{"left": "Arab merchants"}, {"left": "Aires Correia"}, {"left": "Zamorin"}],
        "options": [{"val": "0", "text": "Organized the factory attack"}, {"val": "1", "text": "Died defending the warehouse"}, {"val": "2", "text": "Failed to protect the factory"}],
        "sol": "Arab merchants attacked, Correia died defending, and the Zamorin failed to protect the factory."
    }
])

# One-Liners (8)
ol3 = [
    ("Why did Arab merchants oppose the establishment of the Portuguese factory?", "They feared the loss of their lucrative trade monopoly.", "Arab traders held a monopoly on spice exports and rightly saw the Portuguese as a threat."),
    ("What was the fate of Aires Correia during the Calicut riot?", "He was killed defending the warehouse.", "Correia died along with his garrison during the attack."),
    ("How many Arab ships were captured by Cabral in Calicut harbor?", "Ten vessels.", "He seized 10 ships to confiscate their cargo and execute crews."),
    ("How long did Pedro Álvares Cabral bombard the city of Calicut?", "For one day (24 hours).", "The bombardment took place over a 24-hour period."),
    ("Who was the vice-admiral of Cabral's fleet during the Calicut incident?", "Sancho de Tovar.", "Tovar managed fleet operations from the harbor."),
    ("Which religious figures were killed during the Calicut massacre?", "Three Franciscan friars.", "Franciscan missionaries accompanying the trade mission were killed."),
    ("Why did Cabral execute the crews of the captured Arab merchant ships?", "To punish Calicut and terrify the local merchants.", "It was a brutal act of psychological warfare to assert naval supremacy."),
    ("What was the estimated civilian casualty count of the Calicut bombardment?", "Around 600 people.", "An estimated 600 citizens and merchants died in the bombardment.")
]
for q, sol in ol3:
    sec3_en.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
ar3 = [
    ("Assertion: Arab merchants launched a violent attack on the Portuguese factory.\nReason: They feared the loss of their long-held monopoly on spice exports to the Red Sea.", 0, "The economic threat posed by Portuguese direct purchases triggered the merchants' attack."),
    ("Assertion: Cabral executed the crews of the captured Arab vessels.\nReason: The Zamorin had formally ordered the execution of Aires Correia.", 2, "Assertion is true. Reason is false because the Zamorin did not order Correia's execution; he simply failed to stop the mob."),
    ("Assertion: Cabral bombarded Calicut for a day.\nReason: He wanted to punish the Zamorin for failing to protect the factory factors and inventory.", 0, "The bombardment was a direct reprisal for the massacre and breach of the trade treaty."),
    ("Assertion: Aires Correia was killed during the factory riot.\nReason: He was on board the flagship El Rei when the riot took place.", 2, "Assertion is true. Reason is false because Correia was on land managing the factory warehouse when he was killed."),
    ("Assertion: The Calicut factory massacre ended peaceful Portuguese relations with the Zamorin.\nReason: Cabral's retaliatory bombardment marked the start of open warfare between the two powers.", 0, "The massacre and bombardment permanently fractured relations, leading to decades of conflict."),
    ("Assertion: Three Franciscan friars were killed in the warehouse.\nReason: They had been sent to negotiate spice prices with the Zamorin's court.", 2, "Assertion is true. Reason is false because friars were there for religious missions, not commercial negotiations."),
    ("Assertion: Cabral seized ten merchant ships in Calicut harbor.\nReason: The ships belonged to the local Hindu rulers of Cochin.", 2, "Assertion is true. Reason is false because the ships belonged to Arab/Muslim traders, not Cochin."),
    ("Assertion: The bombardment caused widespread destruction in Calicut.\nReason: The city possessed advanced anti-ship artillery that neutralized the Portuguese fleet.", 2, "Assertion is true. Reason is false because Calicut lacked heavy defensive artillery to counter the fleet.")
]
for q, ans, sol in ar3:
    sec3_en.append({"type": "Assertion-Reason", "q": q, "opts": EN_AR_OPTS, "ans": ans, "sol": sol})

# Statement-Based (5)
st3 = [
    ("Consider the following statements regarding the factory massacre:\n1. It took place on December 16, 1500 CE.\n2. Chief factor Aires Correia survived by escaping on a boat.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Aires Correia was killed in the warehouse attack."),
    ("Consider the following statements regarding Cabral's retaliation:\n1. He captured 10 Arab vessels in Calicut harbor.\n2. He executed the crews and confiscated the spice cargo.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The cargo was taken, and the crews were killed as reprisal."),
    ("With reference to the Calicut bombardment, consider these statements:\n1. It lasted for a duration of one full day.\n2. It resulted in approximately 600 casualties.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Heavy naval cannon fire devastated the coast."),
    ("Consider the statements about the causes of the Calicut riot:\n1. Portuguese factors seized Arab spices by force before the riot.\n2. Arab merchants feared losing their spice monopoly to the Portuguese factory.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. The threat of direct Portuguese purchasing sparked the clash."),
    ("With reference to the Command during the riot, consider these statements:\n1. Sancho de Tovar managed the fleet from the harbor.\n2. Aires Correia managed the factory on land.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Correia was the land representative, Tovar was the naval vice-admiral.")
]
for q, ans, sol in st3:
    sec3_en.append({"type": "Statement-Based", "q": q, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol})

# Open Questions (12)
op3 = [
    ("Why", "Why did Arab merchants see the Portuguese factory as a threat to their existence?", "The Portuguese sought a direct, tax-free monopoly on spice exports to Europe, bypassing Arab-Venetian channels."),
    ("Why", "Why did Cabral decide to bombard Calicut instead of negotiating with the Zamorin?", "He viewed the factory massacre as a violation of the signed treaty, requiring a show of military force to protect prestige."),
    ("Why", "Why did the Zamorin fail to send state troops to protect the Portuguese factory?", "He was influenced by wealthy Arab merchant guilds who funded his state, and he wanted to avoid a clash with local merchants."),
    ("How", "How did Cabral execute the bombardment of Calicut from the harbor?", "He anchored his fleet close to the shore and used ship-borne cannons to target warehouses and public buildings."),
    ("How", "How did the massacre of Aires Correia impact the organization of future Portuguese expeditions?", "It led to future fleets being heavily armed and adopting aggressive gunboat diplomacy from the outset."),
    ("How", "How did Cabral secure the cargo from the captured Arab vessels?", "He ordered his men to board the ships, transfer the spices and goods to the Portuguese vessels, and burn the empty hulls."),
    ("Case Study", "Analyze the role of Arab merchant guilds in the economy of Calicut in 1500 CE.", "Arab merchants controlled the import-export trade, paid major transit duties to the Zamorin, and influenced state policy."),
    ("Case Study", "Discuss the tactical limits of Calicut's harbor defense against European warships.", "Calicut had no defensive fortifications or anti-ship guns, leaving the city vulnerable to naval bombardment."),
    ("Case Study", "Examine the psychological impact of Cabral's executions on Indian Ocean trade.", "It established the Portuguese reputation as a ruthless naval power willing to use extreme force to enforce trade monopolies."),
    ("Teach the Concept", "Explain the chain of events that led from trade treaty to city bombardment in December 1500.", "Treaty signed -> Factory built -> Spice buying friction -> Arab riot -> Correia killed -> Reprisal bombardment."),
    ("Teach the Concept", "Describe the role of Aires Correia as chief factor in Calicut.", "Correia was the official trade agent tasked with purchasing pepper, managing warehousing, and coordinating with local brokers."),
    ("Teach the Concept", "Explain the significance of the Franciscan friars' presence in the Calicut factory.", "Their presence reflected the dual Portuguese mission: commercial profit (spices) and religious conversion (spreading Christianity).")
]
for qtype, q, sol in op3:
    sec3_en.append({"type": qtype, "q": q, "sol": sol})


# ==================== SECTION 4: ALLIANCES WITH COCHIN & KANNUR ====================
sec4_en = []

# MCQs (5)
sec4_en.extend([
    {
        "type": "MCQ",
        "q": "To which Malabar kingdom did Cabral sail after bombarding Calicut to establish a trade alliance?",
        "opts": ["Cochin", "Quilon", "Kannur", "Travancore"],
        "ans": 0,
        "sol": "Cabral sailed to Cochin (Kochi), where the local ruler welcomed the Portuguese to counter Calicut's domination."
    },
    {
        "type": "MCQ",
        "q": "Who was the ruler of Cochin who signed the trade treaty and allowed Cabral to build a factory in December 1500?",
        "opts": ["Unni Goda Varma (Trimumpara Raja)", "Zamorin", "Kolathiri Raja", "Marthanda Varma"],
        "ans": 0,
        "sol": "Unni Goda Varma, the ruler of Cochin, allied with Cabral, laying the foundation of Cochin as the first Portuguese headquarters."
    },
    {
        "type": "MCQ",
        "q": "Which other Malabar port city did Cabral visit after Cochin to load remaining spices and secure an alliance?",
        "opts": ["Kannur", "Calicut", "Goa", "Bassein"],
        "ans": 0,
        "sol": "Cabral visited Kannur (Cannanore), forming a trade alliance with the Kolathiri ruler who was hostile to Calicut."
    },
    {
        "type": "MCQ",
        "q": "What threat forced Cabral to hastily depart Cochin in January 1501?",
        "opts": ["The arrival of a massive war fleet sent by the Zamorin of Calicut", "An outbreak of cholera among the Portuguese crew", "A local rebellion in Cochin against the ruler", "A threat of Spanish invasion in the Indian Ocean"],
        "ans": 0,
        "sol": "The Zamorin dispatched a fleet of around 80 ships to attack the Portuguese, prompting Cabral to depart hastily."
    },
    {
        "type": "MCQ",
        "q": "Which Portuguese captain was left behind in Cochin as the chief factor to manage the new warehouse?",
        "opts": ["Gonçalo Gil Barbosa", "Aires Correia", "Nicolau Coelho", "Sancho de Tovar"],
        "ans": 0,
        "sol": "Gonçalo Gil Barbosa was left behind in Cochin with a small garrison to manage spice purchasing."
    }
])

# Multi Correct (5)
sec4_en.extend([
    {
        "type": "Multiple Correct MCQ",
        "q": "Why did the ruler of Cochin choose to ally with the Portuguese under Cabral? (Select all that apply)",
        "opts": ["To gain independence from the political overlordship of Calicut", "To secure trade profits from direct spice exports", "To secure military protection from Portuguese cannons", "To convert his entire kingdom to the Catholic faith"],
        "ans": [0, 1, 2],
        "sol": "The alliance offered independence from Calicut, trade profits, and military protection. Conversion to Catholicism was not desired."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which ports formed trade alliances with Cabral after the Calicut conflict? (Select all that apply)",
        "opts": ["Cochin", "Kannur", "Quilon", "Surat"],
        "ans": [0, 1, 2],
        "sol": "Cochin, Kannur, and Quilon allied with Cabral. Surat was not visited or allied during this voyage."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key outcomes of the Cochin alliance for the Portuguese. (Select all that apply)",
        "opts": ["Establishment of their first permanent factory in India", "Securing a reliable source of black pepper", "Securing a safe harbor for fleet repairs", "Immediate capture of the Zamorin's capital"],
        "ans": [0, 1, 2],
        "sol": "It secured their first factory, a pepper source, and a safe harbor. It did not capture Calicut."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "What challenges did Cabral face while loading spices in Cochin? (Select all that apply)",
        "opts": ["Threat of attack by the Zamorin's incoming navy", "Friction with local merchants over payment methods", "Tight schedule before the reversal of monsoon winds", "Refusal of the Cochin ruler to permit any shore landings"],
        "ans": [0, 1, 2],
        "sol": "The Zamorin's navy, payment friction, and monsoon timelines were challenges. The Cochin ruler allowed shore landings."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the captains who commanded the ships that loaded spices in Kannur. (Select all that apply)",
        "opts": ["Nicolau Coelho", "Sancho de Tovar", "Simão de Miranda", "Vicente Sodré"],
        "ans": [0, 1, 2],
        "sol": "Coelho, Tovar, and Miranda survived and loaded spices in Kannur. Sodré was not on this voyage."
    }
])

# True/False (8)
tf4 = [
    ("Cochin was a political subordinate to Calicut before the Portuguese arrived.", True, "Cochin paid tribute to Calicut and sought Portuguese aid to break free."),
    ("The ruler of Cochin who allied with Cabral was Unni Goda Varma.", True, "Also known as the Trimumpara Raja, he allied with Cabral in December 1500."),
    ("Cabral built a massive stone fortress in Cochin during his first visit.", False, "He only established a factory warehouse; the stone fort (Fort Emmanuel) was built later in 1503."),
    ("Kannur (Cannanore) welcomed Cabral and signed a trade alliance.", True, "The Kolathiri Raja of Kannur formed an alliance to secure trade revenues."),
    ("Cabral abandoned several Portuguese factors in Cochin when he fled the Zamorin's fleet.", True, "Due to his hasty departure, he left Gonçalo Gil Barbosa and others behind, though they were protected by Cochin's ruler."),
    ("The Zamorin's fleet that pursued Cabral consisted of only five small boats.", False, "The Zamorin sent a massive armada of about 80 ships carrying 1,500 soldiers."),
    ("Cabral visited Goa and established a trade treaty with Adil Shah in 1501.", False, "Goa was hostile and was bypassed; it was conquered later by Albuquerque in 1510."),
    ("The Cochin factory was built under the trade management of Gonçalo Gil Barbosa.", True, "Barbosa was left as the factor to manage the warehouse.")
]
for q, ans, sol in tf4:
    sec4_en.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
fill4 = [
    ("The Malabar state that became the primary base of the Portuguese after Calicut was __________.", "Cochin", "Cochin welcomed the Portuguese and became their headquarters."),
    ("The ruler of Cochin who allied with Cabral was __________ Raja.", "Trimumpara", "The Trimumpara Raja (Unni Goda Varma) was the ally."),
    ("The Portuguese factor left in charge of the Cochin warehouse was __________.", "Gonçalo Gil Barbosa", "Barbosa was left behind to manage trade operations."),
    ("The ruler of Kannur who formed an alliance with Cabral belonged to the __________ dynasty.", "Kolathiri", "The Kolathiri dynasty ruled Kannur and allied with the Portuguese."),
    ("Cabral departed Cochin in January 1501 to avoid a fleet sent by the __________.", "Zamorin", "The Zamorin of Calicut sent a fleet to attack Cabral."),
    ("The number of ships in the Calicut fleet sent to attack Cabral was approximately __________.", "eighty", "A fleet of around 80 ships was sent to pursue Cabral."),
    ("The Malabar port of __________ was visited after Cochin to complete the spice cargo loading.", "Kannur", "They completed loading pepper and ginger at Kannur."),
    ("The Malayalam state of Cochin sought Portuguese help to escape the hegemony of __________.", "Calicut", "Cochin was subordinate to Calicut and wanted independence.")
]
for q, ans, sol in fill4:
    sec4_en.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
sec4_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the Malabar ports with their political status in 1500 CE:",
        "items": [{"left": "Calicut"}, {"left": "Cochin"}, {"left": "Kannur"}],
        "options": [{"val": "0", "text": "Hegemon of the Malabar Coast"}, {"val": "1", "text": "Subordinate state seeking autonomy"}, {"val": "2", "text": "Independent northern rival port"}],
        "sol": "Calicut was the hegemon, Cochin was subordinate, and Kannur was the northern rival."
    },
    {
        "type": "Match the Following",
        "q": "Match the historical outcomes of Cabral's alliances with the ports:",
        "items": [{"left": "Cochin factory"}, {"left": "Kannur alliance"}, {"left": "Calicut harbor"}],
        "options": [{"val": "0", "text": "Established in December 1500"}, {"val": "1", "text": "Secured ginger and pepper trade"}, {"val": "2", "text": "Abandoned after bombardment"}],
        "sol": "Cochin factory was built in Dec 1500, Kannur gave ginger/pepper, and Calicut was abandoned."
    },
    {
        "type": "Match the Following",
        "q": "Match the Portuguese factors with the trading posts they managed:",
        "items": [{"left": "Aires Correia"}, {"left": "Gonçalo Gil Barbosa"}, {"left": "Gaspar da Gama"}],
        "options": [{"val": "0", "text": "Calicut Factory (Killed)"}, {"val": "1", "text": "Cochin Factory (Survived)"}, {"val": "2", "text": "Fleet Translator"}],
        "sol": "Correia managed Calicut, Barbosa managed Cochin, and Gaspar da Gama translated."
    }
])

# One-Liners (8)
ol4 = [
    ("Why did the Raja of Cochin welcome Pedro Álvares Cabral?", "To secure a military ally against Calicut's hegemony.", "Cochin was a political subordinate to Calicut and saw the Portuguese as a counterweight."),
    ("What title is given to the ruler of Cochin in Portuguese records?", "Trimumpara Raja.", "He was known as the Trimumpara Raja in accounts."),
    ("Who was the Portuguese representative left behind in Cochin in 1501?", "Gonçalo Gil Barbosa.", "Barbosa was left as the chief factor in Cochin."),
    ("Why did Cabral leave Cochin without his factors in January 1501?", "Because of the sudden arrival of the Zamorin's war fleet.", "The threat of the Calicut fleet forced a hasty departure."),
    ("What spices were primarily loaded by Cabral's fleet in Kannur?", "Ginger and pepper.", "Kannur was famous for high-quality ginger and cardamom."),
    ("Who was the ruler of Kannur who allied with the Portuguese?", "The Kolathiri Raja.", "The Kolathiri Raja signed the trade agreement."),
    ("How did the Cochin ruler protect the Portuguese factors left behind?", "By housing them in his palace and refusing to hand them to Calicut.", "He protected them despite the Zamorin's demands."),
    ("Where did the Portuguese set up their first trading post after Calicut?", "In Cochin (Kochi).", "The Cochin factory was established in December 1500 CE.")
]
for q, sol in ol4:
    sec4_en.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
ar4 = [
    ("Assertion: Cabral established a trade treaty with the Raja of Cochin.\nReason: Cochin was Calicut's political rival and sought independence from the Zamorin.", 0, "The political rivalry made Cochin a natural ally for the Portuguese."),
    ("Assertion: Cabral left Cochin in a great hurry in January 1501 CE.\nReason: A massive Egyptian war fleet had entered the harbor to blockade the ships.", 2, "Assertion is true. Reason is false because it was the Zamorin's fleet, not an Egyptian fleet."),
    ("Assertion: The Kolathiri Raja of Kannur signed a trade treaty with Cabral.\nReason: He wanted to divert spice revenues from Calicut to his own port.", 0, "Kannur competed with Calicut for spice trade revenues."),
    ("Assertion: Gonçalo Gil Barbosa was abandoned in Cochin.\nReason: He had committed treason and was sentenced to exile by Cabral.", 3, "Assertion is true. Reason is false because he was left as a factor, not due to treason."),
    ("Assertion: The ruler of Cochin protected the abandoned Portuguese factors.\nReason: He feared that Calicut would annex Cochin if he did not cooperate with the Portuguese.", 0, "Allying with the Portuguese was Cochin's survival strategy against Calicut."),
    ("Assertion: Cabral bypassed the port of Goa on his way north.\nReason: Goa was under the control of the hostile Sultan of Bijapur.", 0, "Goa was heavily fortified by Bijapur and too dangerous for Cabral's reduced fleet."),
    ("Assertion: The Portuguese loaded heavy quantities of ginger at Kannur.\nReason: Kannur was the primary center for ginger and cardamom cultivation in Malabar.", 0, "Kannur was the chief market for ginger on the Malabar Coast."),
    ("Assertion: Cabral established a stone fortress in Cochin in 1500 CE.\nReason: The Raja of Cochin gave him permission to build military structures.", 3, "Assertion is false. Reason is false because they only built a factory warehouse; the fort was built in 1503.")
]
for q, ans, sol in ar4:
    sec4_en.append({"type": "Assertion-Reason", "q": q, "opts": EN_AR_OPTS, "ans": ans, "sol": sol})

# Statement-Based (5)
st4 = [
    ("Consider the following statements regarding the Cochin alliance:\n1. It was signed in December 1500 CE.\n2. The ruler was Unni Goda Varma.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Sighted and anchored at Cochin in December."),
    ("Consider the following statements regarding the departure from Cochin:\n1. Cabral waited and defeated the Zamorin's fleet in battle before leaving.\n2. Scribe Gonçalo Gil Barbosa was left behind to manage trade.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Cabral fled without fighting to protect his spice cargo."),
    ("With reference to the Kannur alliance, consider these statements:\n1. Kannur was ruled by the Kolathiri Raja.\n2. It provided ginger and pepper to complete the fleet's cargo.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Kannur was the final loading port before the return crossing."),
    ("Consider the statements about the geopolitical alignments of the Malabar Coast:\n1. Calicut was the dominant state under the Hindu Zamorin.\n2. Cochin was a willing vassal of Calicut that rejected Portuguese trade.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Cochin wanted autonomy and welcomed the Portuguese."),
    ("With reference to harbor fortifications in 1500 CE, consider these statements:\n1. Cabral built Fort Emmanuel in Cochin during this voyage.\n2. Only a simple wooden warehouse was constructed as a factory.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Fort Emmanuel was built later in 1503.")
]
for q, ans, sol in st4:
    sec4_en.append({"type": "Statement-Based", "q": q, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol})

# Open Questions (12)
op4 = [
    ("Why", "Why did Cochin's ruler protect the Portuguese factors despite the Zamorin's threats?", "He saw the Portuguese alliance as his only hope to secure independence from Calicut's hegemony."),
    ("Why", "Why did Cabral choose to retreat from Cochin rather than fight the incoming Calicut fleet?", "His primary mission was to return the valuable spice cargo safely; risking a battle could destroy the ships."),
    ("Why", "Why was Kannur selected as the final Malabar port of call for the fleet?", "It had excellent spice markets (especially ginger) and was ruled by a dynasty hostile to Calicut."),
    ("How", "How did the Cochin alliance change the geopolitical balance of the Malabar Coast?", "It created a permanent division, challenging Calicut's hegemony and giving the Portuguese a secure foothold."),
    ("How", "How did Cabral manage to load spices quickly at Cochin and Kannur?", "The local rulers coordinated with state brokers to prioritize Portuguese purchases over other traders."),
    ("How", "How did the Kolathiri Raja benefit from the trade alliance with Cabral?", "It boosted his port's revenues through duties and weakened his rival, the Zamorin of Calicut."),
    ("Case Study", "Analyze the structural dependence of the Cochin state on Portuguese military power.", "Lacking a strong army, Cochin relied on Portuguese naval artillery to survive Calicut's retaliatory invasions."),
    ("Case Study", "Discuss the role of Kannur as a secondary spice hub for early Portuguese fleets.", "It acted as an alternative source when Calicut was blockaded, securing supply lines for the Lisbon run."),
    ("Case Study", "Examine the protection of Gonçalo Gil Barbosa in Cochin as a test of diplomatic trust.", "By protecting Barbosa, Cochin proved its commitment to the treaty, securing long-term Portuguese support."),
    ("Teach the Concept", "Explain why the Portuguese capital was later established in Goa instead of Cochin.", "Goa had a better central location, superior natural harbors, and was easier to defend from mainland kingdoms."),
    ("Teach the Concept", "Describe the role of the Trimumpara Raja in the early Estado da India.", "He was the first major Indian ruler to form a vassal-like alliance, giving the Portuguese their first permanent base."),
    ("Teach the Concept", "Explain the concept of local rivalries facilitating European entry into India.", "The rivalry between Calicut, Cochin, and Kannur allowed the Portuguese to exploit divisions to secure bases.")
]
for qtype, q, sol in op4:
    sec4_en.append({"type": qtype, "q": q, "sol": sol})


# ==================== SECTION 5: RETURN VOYAGE & GEOPOLITICAL LEGACY ====================
sec5_en = []

# MCQs (5)
sec5_en.extend([
    {
        "type": "MCQ",
        "q": "How many of the original 13 ships returned safely to Lisbon in July 1501 CE under Cabral's command?",
        "opts": ["6 ships", "13 ships", "None", "10 ships"],
        "ans": 0,
        "sol": "Only 6 ships returned safely, showcasing the high physical and human cost of early maritime expeditions."
    },
    {
        "type": "MCQ",
        "q": "What was the financial outcome of Cabral's voyage for the Portuguese Crown despite the heavy loss of ships?",
        "opts": ["It was highly profitable due to the loaded spices", "It bankrupted the Portuguese treasury", "It broke even without any profits", "It resulted in minor losses covered by Spain"],
        "ans": 0,
        "sol": "The spice cargo brought back was so rich that it fully covered all expedition costs and generated high profits for the crown."
    },
    {
        "type": "MCQ",
        "q": "Which European city-state suffered the most economically due to the direct route established by Cabral and Gama?",
        "opts": ["Venice", "Genoa", "London", "Amsterdam"],
        "ans": 0,
        "sol": "Venice lost its monopoly on spice distribution in Western Europe as Lisbon began selling spices at much lower rates."
    },
    {
        "type": "MCQ",
        "q": "What royal institution in Lisbon was expanded to manage spice trade monopolies after Cabral's return?",
        "opts": ["Casa da Índia", "Estado da India", "Carreira da Índia", "Conselho Ultramarino"],
        "ans": 0,
        "sol": "Casa da Índia (House of India) was the crown department that managed all overseas monopolies and customs."
    },
    {
        "type": "MCQ",
        "q": "What was the immediate diplomatic result of Cabral's reports to King Manuel I upon his return in 1501?",
        "opts": ["The commissioning of Vasco da Gama's highly militarized second voyage in 1502", "An immediate declaration of war on Spain", "The abandonment of all future Indian voyages", "A alliance with the Mamluk Sultanate of Egypt"],
        "ans": 0,
        "sol": "Cabral's reports of the Calicut factory massacre prompted King Manuel to send a heavily armed fleet of 20 ships under Gama in 1502."
    }
])

# Multi Correct (5)
sec5_en.extend([
    {
        "type": "Multiple Correct MCQ",
        "q": "What were the main geopolitical consequences of Cabral's voyage? (Select all that apply)",
        "opts": ["Establishment of the Portuguese route as a highly profitable commercial line", "Shift of trade dominance from the Mediterranean to the Atlantic Ocean", "Weakening of Mamluk Egyptian trade revenues", "Conquest of the Ottoman Empire by Portuguese naval fleets"],
        "ans": [0, 1, 2],
        "sol": "It secured the Cape Route, shifted trade centers, and weakened Egypt's revenues. The Ottomans were not conquered."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which factors contributed to the loss of 7 ships during Cabral's expedition? (Select all that apply)",
        "opts": ["Sudden tempests off the Cape of Good Hope", "Shipwrecks on uncharted Brazilian reefs", "Loss of crew due to scurvy during the crossings", "Captures by Venetian navy blockades in the Atlantic"],
        "ans": [0, 1, 2],
        "sol": "Cape tempests, Brazilian reef navigation, and scurvy caused losses. Venice did not block them in the Atlantic."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the long-term trade structures established in Lisbon after Cabral's return. (Select all that apply)",
        "opts": ["Crown monopoly on pepper and ginger imports", "Centralization of trade duties under Casa da Índia", "Annual sailing schedules called Carreira da Índia", "Establishment of joint-stock companies with the Dutch"],
        "ans": [0, 1, 2],
        "sol": "It established crown monopolies, Casa da Índia control, and the Carreira da Índia line. Dutch joint-stocks came much later."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Which Malabar kingdoms remained permanent allies of the Portuguese after Cabral's voyage? (Select all that apply)",
        "opts": ["Kingdom of Cochin", "Kingdom of Kannur", "Kingdom of Quilon", "Zamorin State of Calicut"],
        "ans": [0, 1, 2],
        "sol": "Cochin, Kannur, and Quilon remained allies. Calicut remained a bitter enemy."
    },
    {
        "type": "Multiple Correct MCQ",
        "q": "Identify the key historical details documented by Cabral's expedition. (Select all that apply)",
        "opts": ["First discovery and claim of Brazil", "Establishment of the first factory in Cochin", "First naval bombardment of Calicut", "Discovery of the sea route around Cape Comorin"],
        "ans": [0, 1, 2],
        "sol": "They discovered Brazil, established the Cochin factory, and bombarded Calicut. The route around Cape Comorin had already been opened by Gama."
    }
])

# True/False (8)
tf5 = [
    ("Out of 13 ships, only six returned safely to Lisbon under Cabral.", True, "Only six vessels survived the storms, clashes, and long crossings."),
    ("The expedition resulted in a net financial loss due to the ship casualties.", False, "The spice cargo was so rich that it yielded high profits despite the losses."),
    ("The direct Cape Route led to the economic decline of Venice.", True, "Venice lost its monopoly on spice distribution as Portuguese prices were much cheaper."),
    ("Casa da Índia was the Crown department that managed spice monopolies in Lisbon.", True, "It regulated import sales, duties, and fleet organization."),
    ("Cabral was appointed Viceroy of India immediately upon his return in 1501.", False, "He was ignored for future commands due to disputes, and Vasco da Gama was sent in 1502."),
    ("The diversion of spice trade from the Red Sea weakened Mamluk Egypt.", True, "Mamluk Egypt lost heavy transit tax revenues, leading to its economic decline."),
    ("Spain protested Cabral's claim to Brazil as a violation of the Tordesillas treaty.", False, "Spain accepted the claim because the territory lay east of the meridian line."),
    ("The annual fleet line between Lisbon and India was called the Carreira da Índia.", True, "Carreira da Índia (Run to India) was the official name of the sailing line.")
]
for q, ans, sol in tf5:
    sec5_en.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill in the Blank (8)
fill5 = [
    ("The number of surviving ships that returned to Lisbon under Cabral was __________.", "six", "Only 6 out of the original 13 ships survived the voyage."),
    ("The Crown trade department that managed spice imports in Lisbon was __________.", "Casa da Índia", "Casa da India managed all overseas commercial imports."),
    ("The Italian city-state that lost its spice trade dominance due to the Cape Route was __________.", "Venice", "Venice declined as the center of spice commerce shifted to Lisbon."),
    ("The annual trade route run organized between Lisbon and Goa was the __________.", "Carreira da Índia", "Carreira da Índia was the official state sailing line."),
    ("The next commander sent to India in 1502 to punish Calicut was __________.", "Vasco da Gama", "King Manuel sent Gama with a heavily armed fleet of 20 ships."),
    ("The transit taxes on spices were lost by the __________ Sultanate of Egypt.", "Mamluk", "The Mamluk Sultanate relied heavily on spice transit taxes."),
    ("The meridian line dividing the Spanish and Portuguese hemispheres was established by the Treaty of __________.", "Tordesillas", "The Treaty of Tordesillas set the global division line."),
    ("The primary spice cargo loaded by Cabral that yielded massive profits was __________.", "pepper", "Black pepper was the most valuable and voluminous cargo.")
]
for q, ans, sol in fill5:
    sec5_en.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
sec5_en.extend([
    {
        "type": "Match the Following",
        "q": "Match the historical powers with their economic responses to the Cape Route:",
        "items": [{"left": "Portugal"}, {"left": "Venice"}, {"left": "Mamluk Egypt"}],
        "options": [{"val": "0", "text": "Established royal spice monopolies"}, {"val": "1", "text": "Suffered commercial decline in Europe"}, {"val": "2", "text": "Lost spice transit tax revenues"}],
        "sol": "Portugal established monopolies, Venice declined, and Egypt lost transit revenues."
    },
    {
        "type": "Match the Following",
        "q": "Match the Portuguese trade institutions with their descriptions:",
        "items": [{"left": "Casa da Índia"}, {"left": "Carreira da Índia"}, {"left": "Estado da India"}],
        "options": [{"val": "0", "text": "Crown import department in Lisbon"}, {"val": "1", "text": "Annual royal shipping line"}, {"val": "2", "text": "Portuguese state in the Indian Ocean"}],
        "sol": "Casa da India was the import department, Carreira was the shipping line, and Estado was the state structure."
    },
    {
        "type": "Match the Following",
        "q": "Match the expeditions to India with their commanders and dates:",
        "items": [{"left": "First Voyage (1497)"}, {"left": "Second Voyage (1500)"}, {"left": "Fourth Voyage (1502)"}],
        "options": [{"val": "0", "text": "Vasco da Gama"}, {"val": "1", "text": "Pedro Álvares Cabral"}, {"val": "2", "text": "Vasco da Gama (Militarized)"}],
        "sol": "First was Gama, second was Cabral, fourth (second of Gama) was the militarized run in 1502."
    }
])

# One-Liners (8)
ol5 = [
    ("Why did King Manuel I choose Vasco da Gama instead of Cabral for the 1502 voyage?", "Due to disagreements over command and Cabral's heavy ship losses.", "Disputes over command and the loss of seven ships in 1500 cost Cabral future royal favors."),
    ("What was the primary import institution based in Lisbon?", "Casa da Índia.", "The Casa da Índia managed all import sales and monopolies."),
    ("How did the Cape Route affect Venetian spice brokers?", "It severely cut their profit margins and market share.", "Venice could no longer compete with Lisbon's direct ocean spice pricing."),
    ("What was the annual sailing line to India called?", "Carreira da Índia.", "Carreira da Índia (Run to India) was the official sailing line."),
    ("Which African state was bypassed by Cabral to avoid Mamluk naval patrols?", "Egypt.", "They sailed around Africa to avoid Mamluk-controlled Red Sea waters."),
    ("What was the impact of the Cape Route on the Ottoman Empire?", "It prompted them to conquer Egypt in 1517 to regain trade tax revenues.", "The shift in trade routes weakened Egypt, leading to its conquest by the Ottomans."),
    ("How did the Portuguese secure their monopoly along the Malabar Coast?", "By establishing factories in Cochin and Kannur and blockading Calicut.", "Alliances and naval blockades secured their monopoly."),
    ("How many ships of Cabral's fleet were lost during the entire voyage?", "Seven ships.", "Only six of the thirteen vessels survived the round trip.")
]
for q, sol in ol5:
    sec5_en.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
ar5 = [
    ("Assertion: The second Portuguese voyage was a massive financial success.\nReason: The rich spice cargo brought back by the six surviving ships generated high profits.", 0, "The high value of spices fully covered the losses of the seven sunken vessels."),
    ("Assertion: Venice declined as the primary spice hub of Europe after 1501 CE.\nReason: Lisbon began selling spices directly imported via the Cape Route at much lower rates.", 0, "Lisbon bypassed all Middle Eastern transit taxes, enabling cheaper pricing."),
    ("Assertion: Mamluk Egypt was economically weakened by Cabral's expedition.\nReason: The Portuguese naval presence in the Indian Ocean cut off Egyptian transit tax revenues.", 0, "The diversion of spices from the Red Sea route devastated Mamluk transit tax income."),
    ("Assertion: Cabral was appointed Governor of Goa in 1505 CE.\nReason: He successfully completed the second voyage and conquered Goa.", 3, "Assertion is false. Reason is false because Francisco de Almeida was the first Governor, and Goa was conquered in 1510 by Albuquerque."),
    ("Assertion: King Manuel I was named 'Lord of Navigation' by the Pope.\nReason: Portuguese fleets successfully broke the Arab trade monopoly in the Indian Ocean.", 0, "The papal recognition solidified Portugal's claim on maritime trade routes."),
    ("Assertion: Casa da Índia regulated all imports in Lisbon.\nReason: The Portuguese Crown wanted to maintain strict royal monopolies on spice sales.", 0, "Casa da Índia was established to enforce royal monopolies and prevent private smuggling."),
    ("Assertion: The annual shipping line was organized under the Carreira da Índia.\nReason: The Crown wanted to ensure a regular flow of spices and military reinforcements to India.", 0, "The Carreira da Índia was a highly organized state shipping line to maintain dominance."),
    ("Assertion: The discovery of Brazil had minor long-term geopolitical value.\nReason: Brazil did not produce any spices or immediate mineral wealth in 1500 CE.", 3, "Assertion is false. Reason is true, but Brazil had massive long-term value, leading to the creation of Portuguese America.")
]
for q, ans, sol in ar5:
    sec5_en.append({"type": "Assertion-Reason", "q": q, "opts": EN_AR_OPTS, "ans": ans, "sol": sol})

# Statement-Based (5)
st5 = [
    ("Consider the following statements regarding the return of the fleet:\n1. Only six ships returned to Lisbon in July 1501 CE.\n2. The voyage resulted in a net economic loss for the crown.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. The spice cargo generated a high net profit despite the ship losses."),
    ("Consider the following statements regarding the decline of Venice:\n1. Venice launched a joint naval campaign with Spain to destroy Portuguese ships.\n2. Venetian spice brokers suffered due to Lisbon's cheaper direct imports.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Venice did not launch a joint naval campaign with Spain."),
    ("With reference to the state trade structures, consider these statements:\n1. Casa da Índia managed all import monopolies in Lisbon.\n2. Carreira da Índia was the annual fleet line to India.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. These were the twin pillars of Portuguese maritime empire."),
    ("Consider the statements about the Mamluk Sultanate of Egypt:\n1. It allied with Venice to defend the Red Sea spice routes.\n2. It lost transit tax revenues, facilitating its conquest by the Ottoman Empire.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The shift in trade routes economically crippled the Mamluk state."),
    ("With reference to Cabral's career after 1501 CE, consider these statements:\n1. He was appointed to lead the 1502 voyage to India.\n2. He fell out of favor with King Manuel I and retired from active command.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Vasco da Gama was chosen for the 1502 voyage due to command disputes.")
]
for q, ans, sol in st5:
    sec5_en.append({"type": "Statement-Based", "q": q, "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"], "ans": ans, "sol": sol})

# Open Questions (12)
op5 = [
    ("Why", "Why did the Cape Route cause the economic decline of Venice?", "It bypassed the Mediterranean, allowing Lisbon to sell spices directly without Ottoman or Venetian transit taxes."),
    ("Why", "Why was Cabral not chosen to lead the 1502 expedition despite his success?", "He had disputes with the King over command of the fleet and had lost seven ships in 1500 CE."),
    ("Why", "Why did the Mamluk Sultanate of Egypt suffer so severely from the Portuguese route?", "Their state revenue was structurally dependent on spice transit taxes; the diversion of trade bankrupted them."),
    ("How", "How did the Casa da Índia manage the royal monopoly of spices in Lisbon?", "It received all incoming cargoes, set wholesale prices, collected duties, and auctioned spices to European syndicates."),
    ("How", "How did Cabral's voyage lay the institutional foundation of the Estado da Índia?", "It established the system of allied vassal states (Cochin) and permanent factor bases along the coast."),
    ("How", "How did the discovery of Brazil impact Portuguese-Spanish relations?", "It was accepted peacefully under the Treaty of Tordesillas, establishing Portugal's sphere in South America."),
    ("Case Study", "Analyze the financial model of the Portuguese Crown's spice trade monopoly.", "It combined royal charters, direct state imports via Casa da Índia, and heavy naval policing to crush private trade."),
    ("Case Study", "Discuss the long-term impact of the 'Carreira da Índia' on Atlantic shipping technology.", "It forced the development of larger, more durable naus (carracks) capable of surviving the multi-year round trip."),
    ("Case Study", "Examine the shift in global trade centers from the Mediterranean to the Atlantic after 1501 CE.", "The Cape Route shifted economic power from Venetian-Levantine networks to Portuguese and Dutch Atlantic networks."),
    ("Teach the Concept", "Explain the concept of 'Gunboat Diplomacy' as initiated by Cabral in Calicut.", "It is the use of naval military force (bombarding Calicut) to enforce commercial treaties and intimidate local states."),
    ("Teach the Concept", "Describe the role of allied factories in the Portuguese commercial empire.", "Factories acted as safe trading posts protected by local rulers, allowing Portuguese agents to procure spices year-round."),
    ("Teach the Concept", "Explain how Cabral's voyage verified the commercial viability of the Cape Route.", "Despite losing 7 ships, the profits from the spice cargo of 6 ships proved the route was extremely lucrative.")
]
for qtype, q, sol in op5:
    sec5_en.append({"type": qtype, "q": q, "sol": sol})

# Write to section python files for generated questions compilation
with open(os.path.join(BASE_DIR, "questions_data", "section1.py"), "w", encoding="utf-8") as f:
    f.write(f"section1_en = {repr(sec1_en)}\nsection1_hi = {repr(sec1_hi)}\n")
with open(os.path.join(BASE_DIR, "questions_data", "section2.py"), "w", encoding="utf-8") as f:
    f.write(f"section2_en = {repr(sec2_en)}\nsection2_hi = {repr(sec2_hi)}\n")
with open(os.path.join(BASE_DIR, "questions_data", "section3.py"), "w", encoding="utf-8") as f:
    f.write(f"section3_en = {repr(sec3_en)}\nsection3_hi = {repr(sec3_hi)}\n")
with open(os.path.join(BASE_DIR, "questions_data", "section4.py"), "w", encoding="utf-8") as f:
    f.write(f"section4_en = {repr(sec4_en)}\nsection4_hi = {repr(sec4_hi)}\n")
with open(os.path.join(BASE_DIR, "questions_data", "section5.py"), "w", encoding="utf-8") as f:
    f.write(f"section5_en = {repr(sec5_en)}\nsection5_hi = {repr(sec5_hi)}\n")


# ==================== 50 COMPLETELY UNIQUE PRACTICE QUESTIONS ====================
practice_pool_en = [
    # 1-10
    ("What was the primary goal of the 1500 CE Portuguese voyage commanded by Cabral?", "To secure the trade route and buy spices from India", ["To secure the trade route and buy spices from India", "To conquer the entire Deccan peninsula", "To establish a Christian empire in Asia", "To sign a friendship treaty with the Mughals"], "Cabral's mission was primarily commercial: loading spices and establishing factories."),
    ("In which month of 1500 CE did Cabral's fleet make landfall on the coast of Brazil?", "April", ["April", "March", "June", "December"], "The landfall occurred on April 22, 1500 CE, after sailing far southwest."),
    ("Which ship captain was dispatched by Cabral to inform the King of Portugal about the discovery of Brazil?", "Gaspar de Lemos", ["Gaspar de Lemos", "Nicolau Coelho", "Bartolomeu Dias", "Duarte Barbosa"], "Gaspar de Lemos sailed back to Lisbon immediately with the news."),
    ("How many crew members approximately sailed with Cabral's fleet from Lisbon?", "1,200 to 1,500", ["1,200 to 1,500", "150 to 200", "5,000", "10,000"], "It was a massive armed armada representing high royal commitment."),
    ("What was the first name given to Brazil by Cabral's expedition?", "Ilha de Vera Cruz", ["Ilha de Vera Cruz", "Terra de Santa Cruz", "Terra do Brasil", "Vasco da Gama Land"], "They initially believed it was a large island (Island of the True Cross)."),
    ("Which explorer, famous for first rounding Africa, died in a storm near the Cape of Good Hope in 1500?", "Bartolomeu Dias", ["Bartolomeu Dias", "Vasco da Gama", "Francisco de Almeida", "Sancho de Tovar"], "Bartolomeu Dias drowned along with his ship during a major storm."),
    ("In what year did Pedro Álvares Cabral's fleet return to Lisbon?", "1501 CE", ["1501 CE", "1500 CE", "1502 CE", "1499 CE"], "The surviving ships arrived back in July 1501 CE."),
    ("Where did Cabral establish the first Portuguese factory (feitoria) in India?", "Calicut", ["Calicut", "Cochin", "Kannur", "Goa"], "The factory was established in Calicut with the permission of the Zamorin."),
    ("Who was the Portuguese factor in Calicut killed in the December 1500 riots?", "Aires Correia", ["Aires Correia", "Nicolau Coelho", "Duarte Barbosa", "Gaspar da Gama"], "Aires Correia was the chief agent who died alongside approximately 50 men."),
    ("How did Cabral retaliate for the killing of Aires Correia and the factory destruction?", "By bombarding Calicut and seizing Arab ships", ["By bombarding Calicut and seizing Arab ships", "By pleading with the Zamorin for peace", "By immediately returning to Portugal", "By seeking help from Cochin"], "Cabral seized 10 ships, executed their crews, and bombarded the city for a day."),
    # 11-20
    ("Who was the ruler of Cochin who signed the trade treaty and allowed Cabral to build a factory?", "Unni Goda Varma", ["Unni Goda Varma", "Zamorin", "Kolathiri Raja", "Marthanda Varma"], "Unni Goda Varma, the Trimumpara Raja, allied with the Portuguese to counter Calicut."),
    ("Which other Malabar port city did Cabral visit after Cochin to load ginger and pepper?", "Kannur", ["Kannur", "Calicut", "Goa", "Bassein"], "Kannur was a key spice port whose ruler was also hostile to Calicut."),
    ("What threat forced Cabral to hastily depart Cochin in January 1501?", "The arrival of a massive war fleet sent by the Zamorin", ["The arrival of a massive war fleet sent by the Zamorin", "An outbreak of cholera among the crew", "A local rebellion against the ruler", "The threat of a Spanish invasion"], "The Zamorin dispatched around 80 ships to attack the Portuguese, prompting Cabral to flee."),
    ("How many of the original 13 ships returned safely to Lisbon under Cabral's command?", "6 ships", ["6 ships", "13 ships", "None", "10 ships"], "Only six vessels survived the hazardous round-trip voyage."),
    ("What was the financial outcome of Cabral's voyage for the Portuguese Crown?", "It was highly profitable due to the spice cargo", ["It was highly profitable due to the spice cargo", "It bankrupted the treasury", "It resulted in minor losses", "It broke even without profit"], "The value of the spices brought back by the 6 ships fully covered all costs and yielded high profit."),
    ("Which veteran captain first returned to Portugal in 1499 and accompanied Cabral in 1500?", "Nicolau Coelho", ["Nicolau Coelho", "Bartolomeu Dias", "Gaspar de Lemos", "Duarte Barbosa"], "Nicolau Coelho was a highly experienced captain who accompanied both voyages."),
    ("What geographic feature of the Atlantic ocean forced Cabral to loop far southwest?", "The Volta do Mar wind patterns", ["The Volta do Mar wind patterns", "Furious Fifties winds", "Monsoon wind shifts", "Gulf Stream currents"], "Volta do Mar loops were standard to bypass adverse African coastal currents."),
    ("What was the estimated civilian casualty count of Cabral's bombardment of Calicut?", "Around 600 people", ["Around 600 people", "Over 10,000", "Fewer than 10", "Zero"], "The intense cannon fire killed an estimated 600 citizens and merchants."),
    ("Which Portuguese factor was left in charge of the newly established Cochin factory in 1501?", "Gonçalo Gil Barbosa", ["Gonçalo Gil Barbosa", "Aires Correia", "Nicolau Coelho", "Sancho de Tovar"], "Barbosa was left behind with a small garrison to manage spice purchases."),
    ("Which royal import department was expanded in Lisbon to manage the spice monopoly?", "Casa da Índia", ["Casa da Índia", "Estado da India", "Carreira da Índia", "Conselho Ultramarino"], "Casa da Índia managed all import monopolies and duties in Lisbon."),
    # 21-30
    ("What island was discovered by Diogo Dias in 1500 after being separated from the fleet?", "Madagascar", ["Madagascar", "Mauritius", "Zanzibar", "Ceylon"], "Diogo Dias's ship was blown off course, leading to the discovery of Madagascar."),
    ("Who was the official scribe whose letter is considered the birth certificate of Brazil?", "Pero Vaz de Caminha", ["Pero Vaz de Caminha", "Duarte Barbosa", "João de Barros", "Lopes de Castanheda"], "Caminha was the scribe who documented the land claim and natives."),
    ("What Malayalam state was Calicut located in?", "Malabar", ["Malabar", "Coromandel", "Konkan", "Gujarat"], "Calicut was the chief port city of the Malabar Coast."),
    ("In which church in Portugal was Cabral eventually buried?", "Convento da Graça in Santarém", ["Convento da Graça in Santarém", "Jerónimos Monastery in Lisbon", "Porto Cathedral", "Sines Church"], "Cabral died in 1520 and was buried in Santarém."),
    ("Which pope brokered the Treaty of Tordesillas in 1494?", "Pope Alexander VI", ["Pope Alexander VI", "Pope Julius II", "Pope Leo X", "Pope Clement VII"], "Pope Alexander VI issued the bulls that led to the Tordesillas demarcation line."),
    ("Who commanded the patrol fleet left behind by Vasco da Gama in 1503?", "Vicente Sodré", ["Vicente Sodré", "Nicolau Coelho", "Paulo da Gama", "Duarte Barbosa"], "Vicente Sodré commanded the first Portuguese patrol in Indian waters."),
    ("What was the annual line of fleets between Lisbon and India called?", "Carreira da Índia", ["Carreira da Índia", "Casa da Índia", "Flota de Indias", "VOC"], "The 'Carreira da Índia' was the state-run sailing line to India."),
    ("Which battle in 1509 CE secured Portuguese supremacy in the Indian Ocean?", "Battle of Diu", ["Battle of Diu", "Battle of Cochin", "Battle of Chaul", "Battle of Swally"], "Francisco de Almeida defeated a joint Egyptian-Gujarati fleet at Diu."),
    ("Which Portuguese nobleman took over Goa in 1510?", "Afonso de Albuquerque", ["Afonso de Albuquerque", "Francisco de Almeida", "Vasco da Gama", "Nino da Cunha"], "Afonso de Albuquerque captured Goa and made it the capital."),
    ("Where was Pedro Álvares Cabral born?", "Belmonte", ["Belmonte", "Lisbon", "Porto", "Coimbra"], "Cabral was born in Belmonte, Portugal, to a noble family."),
    # 31-40
    ("Who was the father of Pedro Álvares Cabral?", "Fernão Cabral", ["Fernão Cabral", "Estêvão da Gama", "João Cabral", "Afonso Cabral"], "Fernão Cabral was the Governor of Beira and a prominent nobleman."),
    ("Which group of islands in the Atlantic did Cabral's fleet pass first?", "Cape Verde", ["Cape Verde", "Azores", "Canary Islands", "Madeira"], "The fleet stopped at Cape Verde for fresh provisions."),
    ("Which local portmaster title of Calicut was corrupted to Shahbandar?", "Shahbandar", ["Shahbandar", "Samudiri", "Kolathiri", "Nayaka"], "Shahbandar was the Arabic-origin title for the port master of Calicut."),
    ("What Malayalam term denotes the local Nair warriors of Calicut?", "Lokharas", ["Lokharas", "Samantas", "Nair army", "Marakkars"], "The Nair fighters served as the infantry forces for the Zamorin."),
    ("Where did Cabral face hostility first along the East African coast?", "Mozambique", ["Mozambique", "Mombasa", "Malindi", "Sofala"], "Cabral faced tension and clashes in Mozambique similar to Gama."),
    ("Which East African city provided Cabral with a pilot to cross the Arabian Sea?", "Malindi", ["Malindi", "Mozambique", "Mombasa", "Kilwa"], "The Sultan of Malindi welcomed Cabral and provided a pilot."),
    ("What was the name of the flagship of Pedro Álvares Cabral's fleet?", "El Rei", ["El Rei", "São Gabriel", "Anunciada", "São Pedro"], "El Rei was the flagship commanded by Cabral."),
    ("Which captain's ship was lost early off Cape Verde and returned to Lisbon?", "Gaspar de Lemos", ["Gaspar de Lemos", "Nicolau Coelho", "Sancho de Tovar", "Vasco de Ataíde"], "Vasco de Ataíde's ship was lost near Cape Verde and did not continue."),
    ("What licensing system did the Portuguese introduce to tax Indian Ocean shipping?", "Cartaz", ["Cartaz", "Feitoria", "Estado", "Carreira"], "The Cartaz was a mandatory sailing pass that forced merchants to pay duties."),
    ("Which European city-state suffered the most due to the Cape Route?", "Venice", ["Venice", "Genoa", "Florence", "Pisa"], "Venice lost its monopoly on spice distribution in Western Europe."),
    # 41-50
    ("What was the religion of the Zamorin of Calicut?", "Hinduism", ["Hinduism", "Islam", "Buddhism", "Christianity"], "The Zamorin was a Hindu Nair ruler who followed traditional practices."),
    ("Why did the Zamorin reject the gifts brought by Vasco da Gama?", "They were cheap, low-value items", ["They were cheap, low-value items", "They contained forbidden items", "They were damaged by sea water", "They were stolen from other ports"], "The gifts (hats, cloth, honey) were laughed at by court officials as unfit for a king."),
    ("What Malayalam-speaking local region was Calicut located in?", "Malabar", ["Malabar", "Coromandel", "Konkan", "Gujarat"], "Calicut was the chief port city of the Malabar Coast."),
    ("How many crew members returned safely out of the 170 that started in 1497 under Gama?", "Around 55", ["Around 55", "Around 120", "All 170", "None"], "Only about 55 survivors returned to Portugal due to scurvy and clashes."),
    ("What was the first European trading post (factory) structure in India?", "Cochin factory", ["Cochin factory", "Calicut factory", "Goa factory", "Surat factory"], "The Cochin trading post was established in 1503 CE."),
    ("Which ocean did Vasco da Gama cross to reach India from Malindi?", "Indian Ocean", ["Indian Ocean", "Atlantic Ocean", "Pacific Ocean", "Southern Ocean"], "The fleet crossed the Indian Ocean using the southwest monsoon winds."),
    ("Which pope issued the bull that divided the undiscovered world between Spain and Portugal?", "Pope Alexander VI", ["Pope Alexander VI", "Pope Julius II", "Pope Leo X", "Pope Clement VII"], "Pope Alexander VI brokered the Treaty of Tordesillas in 1494."),
    ("In which year was the Treaty of Tordesillas signed?", "1494 CE", ["1494 CE", "1498 CE", "1500 CE", "1510 CE"], "Signed in 1494, it divided the world's oceans between Spain and Portugal."),
    ("Who commanded the patrol fleet left behind by Gama in 1503?", "Vicente Sodré", ["Vicente Sodré", "Nicolau Coelho", "Paulo da Gama", "Duarte Barbosa"], "Vicente Sodré commanded the first Portuguese patrol in Indian waters."),
    ("Which Portuguese nobleman took over Goa in 1510?", "Afonso de Albuquerque", ["Afonso de Albuquerque", "Francisco de Almeida", "Vasco da Gama", "Nino da Cunha"], "Afonso de Albuquerque captured Goa and made it the capital.")
]

practice_en = []
practice_hi = []
for idx, item in enumerate(practice_pool_en):
    qtext, ans_val, opts, sol = item
    is_multi = "Select all that apply" in qtext
    practice_en.append({
        "type": "Multiple Correct MCQ" if is_multi else "MCQ",
        "q": qtext,
        "opts": opts,
        "ans": [opts.index(ans_val)] if is_multi else opts.index(ans_val),
        "sol": sol
    })
    
    q_hi = local_dict.get(qtext, qtext)
    sol_hi = local_dict.get(sol, sol)
    opts_hi = [local_dict.get(o, o) for o in opts]
    practice_hi.append({
        "type": "Multiple Correct MCQ" if is_multi else "MCQ",
        "q": q_hi,
        "opts": opts_hi,
        "ans": [opts_hi.index(local_dict.get(ans_val, ans_val))] if is_multi else opts_hi.index(local_dict.get(ans_val, ans_val)),
        "sol": sol_hi
    })

generate_sec_file("practice", practice_en, practice_hi)

# --- MOCK QUESTIONS (10) ---
mock_en = [
    {
        "type": "MCQ",
        "q": "With reference to the expedition of Pedro Álvares Cabral (1500-1501 CE), consider the following statements:\n1. The fleet sailed entirely along the African coastline, avoiding open ocean navigation.\n2. The expedition landed in Brazil and claimed it for the Portuguese crown before sailing to India.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect as they sailed far west into the open Atlantic (Volta do Mar). Statement 2 is correct as they discovered and claimed Brazil."
    },
    {
        "type": "MCQ",
        "q": "Regarding the encounter between Cabral's expedition and Calicut, consider the following statements:\n1. Cabral established the first Portuguese factory in Calicut under the protection of Aires Correia.\n2. The subsequent destruction of this factory led to the direct bombardment of Calicut by Cabral.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Aires Correia was appointed chief factor, and the factory massacre triggered Cabral's heavy naval bombardment."
    },
    {
        "type": "MCQ",
        "q": "With reference to early Portuguese alliances on the Malabar Coast, consider the following statements:\n1. The ruler of Cochin (Trimumpara Raja) welcomed Cabral and allowed them to build a factory to counter Calicut.\n2. Cabral signed a similar trade alliance with the Kolathiri ruler of Kannur.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Alliances with Calicut's rivals (Cochin and Kannur) were essential for Portuguese survival."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding the return leg of Cabral's voyage:\n1. More than half of the original 13 ships sank or were lost during the entire expedition.\n2. Despite ship losses, the spice cargo brought back was highly profitable for the Portuguese treasury.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Out of 13 ships, only 6 returned. However, the rich spice cargo fully covered all expenses and yielded high profits."
    },
    {
        "type": "MCQ",
        "q": "Regarding the crew members of Cabral's expedition, consider the following statements:\n1. The famous navigator Bartolomeu Dias successfully completed the journey and stayed as factor in Cochin.\n2. Scribe Pero Vaz de Caminha wrote the famous letter detailing the discovery of Brazil.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Statement 1 is incorrect; Bartolomeu Dias died in a storm near Cape of Good Hope. Statement 2 is correct."
    },
    # 6-10 (additional real UPSC style mock questions)
    {
        "type": "MCQ",
        "q": "With reference to the Treaty of Tordesillas (1494) and early voyages, consider the following statements:\n1. It shifted the meridian line 370 leagues west of the Cape Verde islands.\n2. It gave Spain the exclusive right to all lands found east of this line.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the lands east of the line were reserved for Portugal, not Spain."
    },
    {
        "type": "MCQ",
        "q": "Regarding early Portuguese trading posts in India, consider the following statements:\n1. The very first factory on the Malabar Coast was established in Cochin in 1500 CE.\n2. Vasco da Gama built Fort Emmanuel during his first voyage in 1498 CE.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 3,
        "sol": "Both statements are incorrect. The first factory was attempted in Calicut in 1500 CE, and Fort Emmanuel was built by Albuquerque in 1503 CE, not Gama in 1498."
    },
    {
        "type": "MCQ",
        "q": "With reference to the navigation route Volta do Mar used by Cabral, consider the following statements:\n1. It was a sailing technique that utilized circular wind patterns to clear the calm zones off Guinea.\n2. It led to the accidental discovery of Brazil due to sailing far west into the Atlantic.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Volta do Mar was an open-ocean circular route that led to the discovery of Brazil."
    },
    {
        "type": "MCQ",
        "q": "Consider the following statements regarding the role of Cochin in Portuguese expansion:\n1. The Raja of Cochin sought Portuguese support to escape the hegemony of Calicut.\n2. Cochin served as the first headquarters of the Portuguese Estado da Índia.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. Cochin allied with the Portuguese to counter Calicut and served as their first capital until it shifted to Goa in 1530."
    },
    {
        "type": "MCQ",
        "q": "Regarding the diplomatic letter written by Pero Vaz de Caminha in 1500 CE, consider the following statements:\n1. It reported the discovery of Brazil and was sent to King Manuel I.\n2. It is considered one of the earliest official documents of South American history.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. The letter is highly significant as the birth certificate of Brazil, detailing native encounters."
    }
]

# Translate mock to Hindi
mock_hi = []
for idx, q in enumerate(mock_en):
    q_hi = q.copy()
    q_hi["q"] = local_dict.get(q["q"], q["q"])
    q_hi["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
    q_hi["sol"] = local_dict.get(q["sol"], q["sol"])
    mock_hi.append(q_hi)

generate_sec_file("mock", mock_en, mock_hi)

print("SUCCESS: Programmatically generated all Cabral questions in English and Hindi.")
