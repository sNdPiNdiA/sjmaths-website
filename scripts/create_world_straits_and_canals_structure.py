import os
import shutil

def create_world_straits_and_canals_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "world-straits-and-canals"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Asian_Straits": [
            "Strait_of_Malacca",
            "Strait_of_Hormuz",
            "Bab_el_Mandeb",
            "Taiwan_Strait",
            "Korea_Strait",
            "Tsushima_Strait",
            "Sunda_Strait",
            "Important_Facts"
        ],

        "02_European_Straits": [
            "Strait_of_Gibraltar",
            "Bosporus",
            "Dardanelles",
            "Skagerrak",
            "Kattegat",
            "Messina_Strait",
            "Dover_Strait",
            "Important_Facts"
        ],

        "03_African_Straits": [
            "Bab_el_Mandeb",
            "Mozambique_Channel",
            "Sicily_Channel",
            "Mandeb_Region",
            "Red_Sea_Connections",
            "Mediterranean_Connections",
            "Trade_Routes",
            "Important_Facts"
        ],

        "04_American_Straits": [
            "Bering_Strait",
            "Florida_Strait",
            "Davis_Strait",
            "Hudson_Strait",
            "Magellan_Strait",
            "Drake_Passage",
            "Yucatan_Channel",
            "Important_Facts"
        ],

        "05_Oceanic_Straits": [
            "Torres_Strait",
            "Cook_Strait",
            "Bass_Strait",
            "Murray_Channel",
            "New_Zealand_Straits",
            "Australia_Connections",
            "Pacific_Routes",
            "Important_Facts"
        ],

        "06_Indian_Ocean_Straits": [
            "Malacca",
            "Hormuz",
            "Bab_el_Mandeb",
            "Palk_Strait",
            "Mozambique_Channel",
            "Sunda",
            "Lombok",
            "Important_Facts"
        ],

        "07_Atlantic_Ocean_Straits": [
            "Gibraltar",
            "Florida",
            "Davis",
            "Denmark_Strait",
            "English_Channel",
            "Hudson_Strait",
            "Iceland_Faroe_Gap",
            "Important_Facts"
        ],

        "08_Pacific_Ocean_Straits": [
            "Bering",
            "Taiwan",
            "Korea",
            "Tsugaru",
            "Tsushima",
            "Torres",
            "Cook",
            "Important_Facts"
        ],

        "09_Arctic_and_Polar_Straits": [
            "Bering",
            "Davis",
            "Denmark",
            "Nares",
            "Fram",
            "Hudson",
            "Arctic_Routes",
            "Important_Facts"
        ],

        "10_Major_World_Canals": [
            "Suez_Canal",
            "Panama_Canal",
            "Kiel_Canal",
            "Corinth_Canal",
            "White_Sea_Baltic_Canal",
            "Volga_Don_Canal",
            "Manchester_Ship_Canal",
            "Important_Facts"
        ],

        "11_Asian_Canals": [
            "Suez_Canal",
            "Bangkok_Canal_Projects",
            "Grand_Canal_China",
            "Indira_Gandhi_Canal",
            "Pakistan_Canals",
            "Irrigation_Canals",
            "Navigation_Canals",
            "Important_Facts"
        ],

        "12_European_Canals": [
            "Kiel_Canal",
            "Corinth_Canal",
            "Volga_Don_Canal",
            "Rhine_Main_Danube",
            "Manchester_Ship_Canal",
            "European_Waterways",
            "Navigation_Routes",
            "Important_Facts"
        ],

        "13_American_Canals": [
            "Panama_Canal",
            "Welland_Canal",
            "Erie_Canal",
            "St_Lawrence_Seaway",
            "American_Waterways",
            "Trade_Routes",
            "Navigation",
            "Important_Facts"
        ],

        "14_Strategic_Chokepoints": [
            "Hormuz",
            "Malacca",
            "Bab_el_Mandeb",
            "Suez",
            "Panama",
            "Gibraltar",
            "Bosporus",
            "Important_Facts"
        ],

        "15_International_Trade_Routes": [
            "Europe_Asia_Route",
            "Atlantic_Pacific_Route",
            "Indian_Ocean_Route",
            "Arctic_Route",
            "Mediterranean_Route",
            "Cape_Route",
            "Global_Shipping",
            "Important_Facts"
        ],

        "16_Map_Based_Straits_and_Canals": [
            "Asia_Map",
            "Europe_Map",
            "Africa_Map",
            "America_Map",
            "Ocean_Map",
            "Trade_Route_Map",
            "Location_Matching",
            "Important_Facts"
        ],

        "17_Strait_Sea_Ocean_Matching": [
            "Strait_Ocean_Matching",
            "Canal_Sea_Matching",
            "Country_Matching",
            "Trade_Route_Matching",
            "Location_Matching",
            "PYQ_Focus",
            "Map_Practice",
            "Important_Facts"
        ],

        "18_Current_Affairs_Straits_and_Canals": [
            "Red_Sea_Crisis",
            "Suez_Developments",
            "Panama_Updates",
            "Arctic_Routes",
            "Global_Shipping",
            "Strategic_Developments",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Strait_PYQ",
            "Canal_PYQ",
            "Map_PYQ",
            "Trade_Route_PYQ",
            "Strategic_PYQ",
            "Location_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Straits",
            "Top_100_Canals",
            "Memory_Hooks",
            "Map_Mnemonics",
            "Flashcards",
            "Common_Mistakes",
            "Concept_Traps",
            "Rapid_Revision"
        ]
    }

    leaf_files = [
        "facts.json",
        "one_liner.json",
        "mcq_easy.json",
        "mcq_medium.json",
        "mcq_hard.json",
        "multiple_statement.json",
        "assertion_reason.json",
        "match_following.json",
        "fill_blanks.json",
        "true_false.json",
        "chronology.json",
        "arrange_sequence.json",
        "pair_matching.json",
        "odd_one_out.json",
        "statement_based.json",
        "source_based.json",
        "passage_based.json",
        "case_study.json",
        "short_answer.json",
        "long_answer.json",
        "mains_10m.json",
        "mains_15m.json",
        "mains_20m.json",
        "pyq_upsc.json",
        "pyq_ssc.json",
        "pyq_railway.json",
        "pyq_state_pcs.json",
        "interview.json",
        "flashcards.json",
        "revision_questions.json",
        "concept_traps.json",
        "common_mistakes.json",
        "memory_hooks.json"
    ]

    print(f"Creating structure in: {target_base}")

    for category, topics in structure.items():

        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        print(f"[+] {category}")

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            print(f"    [+] {topic}")

            for filename in leaf_files:

                file_path = os.path.join(topic_path, filename)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ World Straits & Canals structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_world_straits_and_canals_structure()