import os
import shutil

def create_world_rivers_and_lakes_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "world-rivers-and-lakes"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Asian_Rivers": [
            "Yangtze",
            "Yellow_River",
            "Mekong",
            "Amur",
            "Ob",
            "Yenisei",
            "Lena",
            "Important_Facts"
        ],

        "02_South_Asian_Rivers": [
            "Indus",
            "Ganga",
            "Brahmaputra",
            "Irrawaddy",
            "Salween",
            "Kabul",
            "Teesta",
            "Important_Facts"
        ],

        "03_European_Rivers": [
            "Danube",
            "Rhine",
            "Volga",
            "Seine",
            "Thames",
            "Po",
            "Dnieper",
            "Important_Facts"
        ],

        "04_African_Rivers": [
            "Nile",
            "Congo",
            "Niger",
            "Zambezi",
            "Orange",
            "Limpopo",
            "Senegal",
            "Important_Facts"
        ],

        "05_North_American_Rivers": [
            "Mississippi",
            "Missouri",
            "Colorado",
            "Yukon",
            "Mackenzie",
            "Rio_Grande",
            "St_Lawrence",
            "Important_Facts"
        ],

        "06_South_American_Rivers": [
            "Amazon",
            "Parana",
            "Orinoco",
            "Paraguay",
            "Uruguay",
            "Madeira",
            "Tocantins",
            "Important_Facts"
        ],

        "07_Australian_Rivers": [
            "Murray",
            "Darling",
            "Murrumbidgee",
            "Cooper_Creek",
            "Fitzroy",
            "Burdekin",
            "Victoria_River",
            "Important_Facts"
        ],

        "08_Transboundary_Rivers": [
            "Nile_Basin",
            "Danube_Basin",
            "Mekong_Basin",
            "Indus_Basin",
            "Ganga_Basin",
            "Amazon_Basin",
            "Congo_Basin",
            "Important_Facts"
        ],

        "09_World_Famous_Lakes": [
            "Lake_Baikal",
            "Lake_Superior",
            "Lake_Victoria",
            "Lake_Tanganyika",
            "Lake_Michigan",
            "Lake_Huron",
            "Lake_Erie",
            "Important_Facts"
        ],

        "10_Salt_Lakes": [
            "Dead_Sea",
            "Caspian_Sea",
            "Great_Salt_Lake",
            "Aral_Sea",
            "Lake_Urmia",
            "Lake_Assal",
            "Sambhar_Comparison",
            "Important_Facts"
        ],

        "11_Glacial_Lakes": [
            "Lake_Ladoga",
            "Lake_Onega",
            "Great_Bear_Lake",
            "Great_Slave_Lake",
            "Lake_Winnipeg",
            "Lake_Vostok",
            "Glacial_Features",
            "Important_Facts"
        ],

        "12_Rift_Valley_Lakes": [
            "Lake_Tanganyika",
            "Lake_Malawi",
            "Lake_Turkana",
            "Lake_Kivu",
            "Lake_Albert",
            "Lake_Edward",
            "Rift_System",
            "Important_Facts"
        ],

        "13_Artificial_Lakes_and_Reservoirs": [
            "Lake_Nasser",
            "Volta_Lake",
            "Kariba_Reservoir",
            "Mead",
            "Powell",
            "Three_Gorges_Reservoir",
            "Itaipu_Reservoir",
            "Important_Facts"
        ],

        "14_River_Valleys_and_Basins": [
            "Amazon_Basin",
            "Nile_Basin",
            "Mississippi_Basin",
            "Congo_Basin",
            "Danube_Basin",
            "Mekong_Basin",
            "Yangtze_Basin",
            "Important_Facts"
        ],

        "15_River_Mouths_and_Deltas": [
            "Ganga_Brahmaputra_Delta",
            "Nile_Delta",
            "Mississippi_Delta",
            "Mekong_Delta",
            "Niger_Delta",
            "Danube_Delta",
            "Amazon_Estuary",
            "Important_Facts"
        ],

        "16_Map_Based_Rivers_and_Lakes": [
            "Asia_Map",
            "Europe_Map",
            "Africa_Map",
            "America_Map",
            "Australia_Map",
            "River_Matching",
            "Lake_Matching",
            "Important_Facts"
        ],

        "17_River_Lake_Country_Matching": [
            "River_Country_Matching",
            "Lake_Country_Matching",
            "River_Source_Matching",
            "River_Mouth_Matching",
            "Lake_Type_Matching",
            "Basin_Matching",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "18_Current_Affairs_Rivers_and_Lakes": [
            "Water_Disputes",
            "Lake_Conservation",
            "River_Projects",
            "Drought_Issues",
            "Flood_Issues",
            "International_Agreements",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "River_PYQ",
            "Lake_PYQ",
            "Delta_PYQ",
            "Basin_PYQ",
            "Map_PYQ",
            "Country_Matching_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Rivers",
            "Top_100_Lakes",
            "Memory_Hooks",
            "River_Mnemonics",
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

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for filename in leaf_files:

                with open(
                    os.path.join(topic_path, filename),
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write("[]")

    print("\n✅ World Rivers & Lakes structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_world_rivers_and_lakes_structure()