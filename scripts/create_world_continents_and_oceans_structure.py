import os
import shutil

def create_world_continents_and_oceans_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "world-continents-and-oceans"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Asia": [
            "Physical_Features",
            "Countries",
            "Major_Rivers",
            "Major_Mountains",
            "Climate",
            "Natural_Resources",
            "Population",
            "Important_Facts"
        ],

        "02_Africa": [
            "Physical_Features",
            "Countries",
            "Major_Rivers",
            "Major_Lakes",
            "Climate",
            "Natural_Resources",
            "Population",
            "Important_Facts"
        ],

        "03_Europe": [
            "Physical_Features",
            "Countries",
            "Major_Rivers",
            "Major_Mountains",
            "Climate",
            "Resources",
            "Population",
            "Important_Facts"
        ],

        "04_North_America": [
            "Physical_Features",
            "Countries",
            "Major_Rivers",
            "Major_Lakes",
            "Climate",
            "Resources",
            "Population",
            "Important_Facts"
        ],

        "05_South_America": [
            "Physical_Features",
            "Countries",
            "Amazon_Basin",
            "Andes_Mountains",
            "Climate",
            "Resources",
            "Population",
            "Important_Facts"
        ],

        "06_Australia_and_Oceania": [
            "Australia",
            "Melanesia",
            "Micronesia",
            "Polynesia",
            "Climate",
            "Resources",
            "Population",
            "Important_Facts"
        ],

        "07_Antarctica": [
            "Location",
            "Physical_Features",
            "Climate",
            "Research_Stations",
            "Treaty_System",
            "Resources",
            "Wildlife",
            "Important_Facts"
        ],

        "08_Pacific_Ocean": [
            "Location",
            "Islands",
            "Currents",
            "Deepest_Points",
            "Resources",
            "Marine_Life",
            "Trade_Routes",
            "Important_Facts"
        ],

        "09_Atlantic_Ocean": [
            "Location",
            "Currents",
            "Resources",
            "Marine_Life",
            "Trade_Routes",
            "Important_Ports",
            "Strategic_Importance",
            "Important_Facts"
        ],

        "10_Indian_Ocean": [
            "Location",
            "Currents",
            "Resources",
            "Marine_Life",
            "Trade_Routes",
            "Strategic_Importance",
            "Indian_Ocean_Region",
            "Important_Facts"
        ],

        "11_Arctic_Ocean": [
            "Location",
            "Climate",
            "Resources",
            "Shipping_Routes",
            "Marine_Life",
            "Arctic_Council",
            "Strategic_Importance",
            "Important_Facts"
        ],

        "12_Southern_Ocean": [
            "Location",
            "Currents",
            "Climate",
            "Marine_Life",
            "Resources",
            "Research",
            "Strategic_Importance",
            "Important_Facts"
        ],

        "13_Continents_Comparison": [
            "Area",
            "Population",
            "Countries",
            "Density",
            "Resources",
            "Climate",
            "Development",
            "Important_Facts"
        ],

        "14_Oceans_Comparison": [
            "Area",
            "Depth",
            "Resources",
            "Currents",
            "Marine_Life",
            "Trade_Routes",
            "Strategic_Importance",
            "Important_Facts"
        ],

        "15_Map_Based_Geography": [
            "Continents_Map",
            "Oceans_Map",
            "Important_Locations",
            "Bordering_Seas",
            "Island_Groups",
            "Major_Ports",
            "Navigation",
            "Important_Facts"
        ],

        "16_Continents_and_Countries": [
            "Asian_Countries",
            "African_Countries",
            "European_Countries",
            "American_Countries",
            "Oceanian_Countries",
            "Transcontinental_Countries",
            "Island_Nations",
            "Important_Facts"
        ],

        "17_Climate_and_Biomes": [
            "Tropical",
            "Desert",
            "Temperate",
            "Polar",
            "Grasslands",
            "Forests",
            "Tundra",
            "Important_Facts"
        ],

        "18_Current_Affairs_Geography": [
            "Arctic_Developments",
            "Ocean_Research",
            "Climate_Updates",
            "Marine_Conservation",
            "Geopolitical_Developments",
            "Research_Expeditions",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Continents_PYQ",
            "Oceans_PYQ",
            "Map_Based_PYQ",
            "Climate_PYQ",
            "Resource_PYQ",
            "Trade_Route_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Facts",
            "Map_Mnemonics",
            "Memory_Hooks",
            "Flashcards",
            "Common_Mistakes",
            "Concept_Traps",
            "Rapid_Revision",
            "Expected_Questions"
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

    print("\n✅ World Continents & Oceans structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_world_continents_and_oceans_structure()