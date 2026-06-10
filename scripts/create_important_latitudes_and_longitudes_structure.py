import os
import shutil

def create_important_latitudes_and_longitudes_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "important-latitudes-and-longitudes"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Equator": [
            "Location",
            "Countries_On_Equator",
            "Climate",
            "Day_Night_Duration",
            "Physical_Features",
            "Importance",
            "Map_Based_Questions",
            "Important_Facts"
        ],

        "02_Tropic_of_Cancer": [
            "Location",
            "Countries_Crossed",
            "Indian_States_Crossed",
            "Climate_Impact",
            "Solar_Influence",
            "Map_Based_Questions",
            "Exam_Facts",
            "Important_Facts"
        ],

        "03_Tropic_of_Capricorn": [
            "Location",
            "Countries_Crossed",
            "Climate_Impact",
            "Solar_Influence",
            "Southern_Hemisphere",
            "Map_Based_Questions",
            "Exam_Facts",
            "Important_Facts"
        ],

        "04_Arctic_Circle": [
            "Location",
            "Countries_Crossed",
            "Polar_Day",
            "Polar_Night",
            "Climate",
            "Resources",
            "Map_Based_Questions",
            "Important_Facts"
        ],

        "05_Antarctic_Circle": [
            "Location",
            "Antarctica",
            "Polar_Day",
            "Polar_Night",
            "Climate",
            "Research_Stations",
            "Map_Based_Questions",
            "Important_Facts"
        ],

        "06_Prime_Meridian": [
            "Greenwich",
            "Longitude_Zero",
            "GMT",
            "Countries_Crossed",
            "Time_Calculation",
            "Navigation",
            "Map_Based_Questions",
            "Important_Facts"
        ],

        "07_International_Date_Line": [
            "Location",
            "Date_Changes",
            "Pacific_Ocean",
            "IDL_Deviations",
            "Countries_Affected",
            "Time_Calculation",
            "Map_Based_Questions",
            "Important_Facts"
        ],

        "08_Latitudes_Basics": [
            "Definition",
            "Parallels",
            "Measurement",
            "Northern_Hemisphere",
            "Southern_Hemisphere",
            "Climate_Influence",
            "Map_Practice",
            "Important_Facts"
        ],

        "09_Longitudes_Basics": [
            "Definition",
            "Meridians",
            "Measurement",
            "Eastern_Hemisphere",
            "Western_Hemisphere",
            "Time_Calculation",
            "Map_Practice",
            "Important_Facts"
        ],

        "10_Time_Zones": [
            "World_Time_Zones",
            "GMT",
            "UTC",
            "Time_Difference",
            "Standard_Time",
            "International_Date_Line",
            "Practice_Questions",
            "Important_Facts"
        ],

        "11_Indian_Standard_Time": [
            "IST",
            "82_5_East_Longitude",
            "Mirzapur",
            "Time_Calculation",
            "Indian_Time_Zone",
            "State_Impacts",
            "Map_Based_Questions",
            "Important_Facts"
        ],

        "12_Heat_Zones_of_Earth": [
            "Torrid_Zone",
            "Temperate_Zone_North",
            "Temperate_Zone_South",
            "Frigid_Zone_North",
            "Frigid_Zone_South",
            "Climate",
            "Map_Practice",
            "Important_Facts"
        ],

        "13_Latitudes_and_Climate": [
            "Temperature",
            "Rainfall",
            "Pressure_Belts",
            "Wind_Systems",
            "Climate_Zones",
            "Vegetation",
            "Map_Practice",
            "Important_Facts"
        ],

        "14_Longitudes_and_Time": [
            "Local_Time",
            "Standard_Time",
            "Time_Difference",
            "GMT_Calculations",
            "UTC_Calculations",
            "IDL_Calculations",
            "Practice_Questions",
            "Important_Facts"
        ],

        "15_Map_Based_Latitudes": [
            "Equator_Map",
            "Cancer_Map",
            "Capricorn_Map",
            "Arctic_Map",
            "Antarctic_Map",
            "Country_Matching",
            "Practice",
            "Important_Facts"
        ],

        "16_Map_Based_Longitudes": [
            "Prime_Meridian_Map",
            "IDL_Map",
            "Time_Zone_Map",
            "World_Map",
            "Country_Matching",
            "Navigation",
            "Practice",
            "Important_Facts"
        ],

        "17_Countries_Crossed": [
            "Equator_Countries",
            "Cancer_Countries",
            "Capricorn_Countries",
            "Prime_Meridian_Countries",
            "Arctic_Countries",
            "Antarctic_Region",
            "Matching_Questions",
            "Important_Facts"
        ],

        "18_Current_Affairs_Geography": [
            "Arctic_Developments",
            "Antarctic_Research",
            "Time_Zone_Changes",
            "Navigation_Updates",
            "Satellite_Mapping",
            "Climate_Research",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Latitude_PYQ",
            "Longitude_PYQ",
            "Time_Zone_PYQ",
            "Map_PYQ",
            "Climate_PYQ",
            "IST_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Facts",
            "Latitude_Mnemonics",
            "Longitude_Mnemonics",
            "Map_Hacks",
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

    print("\n✅ Important Latitudes & Longitudes structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_important_latitudes_and_longitudes_structure()