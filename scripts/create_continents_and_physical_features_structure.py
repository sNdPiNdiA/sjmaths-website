import os
import shutil

def create_continents_and_physical_features_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "world-geography",
        "continents-and-physical-features"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_World_Geography_Fundamentals": [
            "Meaning_of_World_Geography",
            "Continents_and_Oceans",
            "Global_Physical_Features",
            "Major_Relief_Regions",
            "Geographical_Divisions",
            "Earth_Surface_Features",
            "Importance_of_Study",
            "Sources_of_Study"
        ],

        "02_Continents_Overview": [
            "Asia",
            "Africa",
            "Europe",
            "North_America",
            "South_America",
            "Australia",
            "Antarctica",
            "Comparative_Study"
        ],

        "03_Asia_Physical_Geography": [
            "Location_and_Extent",
            "Mountain_Ranges",
            "Plateaus",
            "Plains",
            "Deserts",
            "Rivers",
            "Climate_Regions",
            "Physical_Divisions"
        ],

        "04_Africa_Physical_Geography": [
            "Location_and_Extent",
            "Sahara_Desert",
            "East_African_Rift",
            "Plateaus",
            "River_Systems",
            "Great_Lakes",
            "Climate_Regions",
            "Physical_Divisions"
        ],

        "05_Europe_Physical_Geography": [
            "Location_and_Extent",
            "Alps",
            "North_European_Plain",
            "River_Systems",
            "Peninsulas",
            "Climate_Regions",
            "Physical_Divisions",
            "Major_Features"
        ],

        "06_North_America_Physical_Geography": [
            "Location_and_Extent",
            "Rocky_Mountains",
            "Appalachians",
            "Great_Plains",
            "Great_Lakes",
            "River_Systems",
            "Climate_Regions",
            "Physical_Divisions"
        ],

        "07_South_America_Physical_Geography": [
            "Location_and_Extent",
            "Andes_Mountains",
            "Amazon_Basin",
            "Brazilian_Highlands",
            "Patagonia",
            "River_Systems",
            "Climate_Regions",
            "Physical_Divisions"
        ],

        "08_Australia_Physical_Geography": [
            "Location_and_Extent",
            "Western_Plateau",
            "Central_Lowlands",
            "Eastern_Highlands",
            "Great_Barrier_Reef",
            "Deserts",
            "Climate_Regions",
            "Physical_Divisions"
        ],

        "09_Antarctica_Physical_Geography": [
            "Location_and_Extent",
            "Ice_Sheets",
            "Transantarctic_Mountains",
            "Climate",
            "Glaciers",
            "Polar_Environment",
            "Research_Stations",
            "Global_Importance"
        ],

        "10_Major_Mountain_Ranges": [
            "Himalayas",
            "Andes",
            "Rockies",
            "Alps",
            "Atlas_Mountains",
            "Ural_Mountains",
            "Great_Dividing_Range",
            "Comparative_Study"
        ],

        "11_Major_Plateaus": [
            "Tibetan_Plateau",
            "Deccan_Plateau",
            "Brazilian_Plateau",
            "Mexican_Plateau",
            "Ethiopian_Plateau",
            "Patagonian_Plateau",
            "Colorado_Plateau",
            "Characteristics"
        ],

        "12_Major_Plains": [
            "Indo_Gangetic_Plain",
            "North_European_Plain",
            "Great_Plains",
            "Amazon_Lowlands",
            "West_Siberian_Plain",
            "North_China_Plain",
            "Murray_Darling_Basin",
            "Significance"
        ],

        "13_Major_Deserts": [
            "Sahara",
            "Arabian_Desert",
            "Gobi",
            "Kalahari",
            "Atacama",
            "Great_Victoria_Desert",
            "Patagonian_Desert",
            "Characteristics"
        ],

        "14_Major_River_Systems": [
            "Nile",
            "Amazon",
            "Mississippi_Missouri",
            "Yangtze",
            "Congo",
            "Danube",
            "Volga",
            "Comparative_Analysis"
        ],

        "15_Major_Lakes": [
            "Caspian_Sea",
            "Lake_Superior",
            "Lake_Victoria",
            "Lake_Baikal",
            "Great_Lakes",
            "Dead_Sea",
            "Lake_Tanganyika",
            "Importance"
        ],

        "16_Islands_and_Archipelagos": [
            "Greenland",
            "Madagascar",
            "Japan",
            "Indonesia",
            "Philippines",
            "British_Isles",
            "New_Zealand",
            "Significance"
        ],

        "17_Peninsulas_and_Isthmuses": [
            "Arabian_Peninsula",
            "Indian_Peninsula",
            "Scandinavian_Peninsula",
            "Iberian_Peninsula",
            "Malay_Peninsula",
            "Isthmus_of_Panama",
            "Isthmus_of_Suez",
            "Geographical_Importance"
        ],

        "18_Straits_and_Canals": [
            "Strait_of_Malacca",
            "Bering_Strait",
            "Strait_of_Gibraltar",
            "Bosporus",
            "Suez_Canal",
            "Panama_Canal",
            "Kiel_Canal",
            "Strategic_Importance"
        ],

        "19_Coastal_and_Marine_Features": [
            "Bays",
            "Gulfs",
            "Fjords",
            "Estuaries",
            "Lagoons",
            "Coral_Reefs",
            "Coastal_Plains",
            "Marine_Landforms"
        ],

        "20_Volcanoes_and_Earthquake_Zones": [
            "Ring_of_Fire",
            "Mid_Oceanic_Ridges",
            "Volcanic_Belts",
            "Earthquake_Belts",
            "Major_Volcanoes",
            "Tectonic_Activity",
            "Hazard_Zones",
            "Recent_Events"
        ],

        "21_Biomes_and_Natural_Vegetation": [
            "Tropical_Rainforests",
            "Savanna",
            "Temperate_Forests",
            "Taiga",
            "Tundra",
            "Mediterranean_Vegetation",
            "Grasslands",
            "Desert_Vegetation"
        ],

        "22_Climate_Regions_of_the_World": [
            "Equatorial_Climate",
            "Monsoon_Climate",
            "Desert_Climate",
            "Mediterranean_Climate",
            "Temperate_Climate",
            "Polar_Climate",
            "Mountain_Climate",
            "Distribution"
        ],

        "23_World_Oceans_and_Seas": [
            "Pacific_Ocean",
            "Atlantic_Ocean",
            "Indian_Ocean",
            "Arctic_Ocean",
            "Southern_Ocean",
            "Marginal_Seas",
            "Oceanic_Features",
            "Importance"
        ],

        "24_Global_Environmental_Regions": [
            "Amazon_Basin",
            "Congo_Basin",
            "Arctic_Region",
            "Antarctic_Region",
            "Sahel",
            "Great_Barrier_Reef",
            "Wetlands",
            "Environmental_Significance"
        ],

        "25_World_Geographical_Superlatives": [
            "Highest_Mountain",
            "Longest_River",
            "Largest_Lake",
            "Largest_Desert",
            "Deepest_Ocean_Trench",
            "Largest_Island",
            "Largest_Peninsula",
            "Record_Features"
        ],

        "26_Human_Interaction_with_Physical_Features": [
            "Settlements",
            "Agriculture",
            "Transport",
            "Resource_Utilization",
            "Tourism",
            "Environmental_Impacts",
            "Hazards",
            "Adaptation"
        ],

        "27_Current_Affairs_and_Geographical_Issues": [
            "Climate_Change_Impacts",
            "Glacier_Melting",
            "Desertification",
            "Volcanic_Events",
            "Earthquakes",
            "Ocean_Issues",
            "Recent_Research",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "World_Physical_Map",
            "Mountain_Maps",
            "River_Maps",
            "Desert_Maps",
            "Climate_Maps",
            "Ocean_Maps",
            "Map_Based_Questions",
            "PYQ_Themes"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "map_based.json", "source_based.json",
        "passage_based.json", "case_study.json", "short_answer.json",
        "long_answer.json", "mains_10m.json", "mains_15m.json",
        "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "pyq_teaching.json",
        "interview.json", "flashcards.json", "revision_questions.json",
        "concept_traps.json", "common_mistakes.json", "memory_hooks.json"
    ]

    print(f"Creating Continents and Physical Features structure in: {target_base}")

    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)
        print(f"  [+] Category: {category}")

        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)
            print(f"    [+] Topic: {topic}")

            for filename in leaf_files:
                file_path = os.path.join(topic_path, filename)
                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("[]")
                    print(f"      - Created: {filename}")
                else:
                    print(f"      - Exists: {filename}")

if __name__ == "__main__":
    create_continents_and_physical_features_structure()