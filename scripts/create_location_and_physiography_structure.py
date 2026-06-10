import os
import shutil

def create_location_and_physiography_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography", "location-and-physiography")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_India_Location_and_Extent": [
            "Latitudinal_Extent",
            "Longitudinal_Extent",
            "Standard_Meridian",
            "Geographical_Extent",
            "Area_of_India",
            "Hemispheric_Location",
            "Strategic_Position",
            "Location_Significance"
        ],
        "02_India_and_the_World": [
            "Neighbouring_Countries",
            "Land_Boundaries",
            "Maritime_Boundaries",
            "Indian_Ocean_Position",
            "South_Asia",
            "Geostrategic_Importance",
            "International_Routes",
            "Regional_Connectivity"
        ],
        "03_Political_and_Administrative_Geography": [
            "States_and_Union_Territories",
            "Administrative_Divisions",
            "Boundary_Changes",
            "Reorganization_of_States",
            "Border_States",
            "Capital_Cities",
            "Inter_State_Boundaries",
            "Administrative_Structure"
        ],
        "04_Geological_Evolution_of_India": [
            "Gondwanaland",
            "Continental_Drift",
            "Plate_Tectonics",
            "Indian_Plate",
            "Collision_with_Eurasia",
            "Geological_Eras",
            "Tectonic_History",
            "Geological_Significance"
        ],
        "05_Geological_Structure": [
            "Archaean_Rocks",
            "Dharwar_System",
            "Vindhyan_System",
            "Gondwana_System",
            "Deccan_Traps",
            "Rock_Formations",
            "Geological_Regions",
            "Structural_Framework"
        ],
        "06_Physiographic_Divisions_Overview": [
            "Northern_Mountains",
            "Northern_Plains",
            "Peninsular_Plateau",
            "Indian_Desert",
            "Coastal_Plains",
            "Islands",
            "Classification_of_Physiography",
            "Regional_Diversity"
        ],
        "07_Himalayan_System_Overview": [
            "Extent_of_Himalayas",
            "Formation_of_Himalayas",
            "Longitudinal_Divisions",
            "Regional_Divisions",
            "Himalayan_Significance",
            "Young_Fold_Mountains",
            "Physiographic_Features",
            "Strategic_Importance"
        ],
        "08_Greater_Himalaya_Himadri": [
            "Highest_Range",
            "Major_Peaks",
            "Glaciers",
            "Snow_Cover",
            "Mountain_Passes",
            "Geomorphic_Features",
            "Settlements",
            "Importance"
        ],
        "09_Lesser_Himalaya_Himachal": [
            "Pir_Panjal",
            "Dhauladhar",
            "Mahabharat_Range",
            "Hill_Stations",
            "Valleys",
            "Human_Settlements",
            "Economic_Activities",
            "Regional_Characteristics"
        ],
        "10_Shivalik_and_Trans_Himalaya": [
            "Shivalik_Range",
            "Bhabar",
            "Terai",
            "Karakoram",
            "Ladakh_Range",
            "Zaskar_Range",
            "Cold_Desert",
            "Regional_Features"
        ],
        "11_Himalayan_Regional_Divisions": [
            "Kashmir_Himalaya",
            "Himachal_Himalaya",
            "Uttarakhand_Himalaya",
            "Darjeeling_Himalaya",
            "Arunachal_Himalaya",
            "Eastern_Hills",
            "Purvanchal",
            "Regional_Comparisons"
        ],
        "12_Northern_Plains": [
            "Formation",
            "Alluvial_Deposits",
            "Extent",
            "Physiographic_Features",
            "Population_Distribution",
            "Agricultural_Significance",
            "Regional_Differences",
            "Economic_Importance"
        ],
        "13_Regional_Divisions_of_Northern_Plains": [
            "Punjab_Plains",
            "Ganga_Plains",
            "Brahmaputra_Plains",
            "Khadar",
            "Bhangar",
            "Flood_Plains",
            "Regional_Features",
            "Comparative_Study"
        ],
        "14_Peninsular_Plateau_Overview": [
            "Ancient_Crystalline_Block",
            "Plateau_Characteristics",
            "Relief_Features",
            "Residual_Hills",
            "Plateau_Extent",
            "Structural_Stability",
            "Geomorphic_Processes",
            "Economic_Importance"
        ],
        "15_Central_Highlands": [
            "Malwa_Plateau",
            "Bundelkhand_Upland",
            "Baghelkhand",
            "Chotanagpur_Plateau",
            "Aravalli_Range",
            "Vindhyan_Range",
            "Mineral_Resources",
            "Regional_Features"
        ],
        "16_Deccan_Plateau": [
            "Maharashtra_Plateau",
            "Karnataka_Plateau",
            "Telangana_Plateau",
            "Lava_Plateau",
            "Black_Soil_Region",
            "Drainage_Characteristics",
            "Economic_Significance",
            "Regional_Features"
        ],
        "17_Western_and_Eastern_Ghats": [
            "Western_Ghats",
            "Eastern_Ghats",
            "Nilgiri_Hills",
            "Anaimalai_Hills",
            "Cardamom_Hills",
            "Ghats_Comparison",
            "Biodiversity",
            "Ecological_Importance"
        ],
        "18_Indian_Desert": [
            "Thar_Desert",
            "Arid_Climate",
            "Sand_Dunes",
            "Desert_Landforms",
            "Desertification",
            "Human_Adaptation",
            "Indira_Gandhi_Canal",
            "Regional_Characteristics"
        ],
        "19_Coastal_Plains": [
            "Western_Coastal_Plain",
            "Eastern_Coastal_Plain",
            "Konkan_Coast",
            "Kanara_Coast",
            "Malabar_Coast",
            "Northern_Circar",
            "Coromandel_Coast",
            "Comparative_Features"
        ],
        "20_Coastal_Landforms": [
            "Beaches",
            "Lagoons",
            "Backwaters",
            "Estuaries",
            "Deltas",
            "Mudflats",
            "Coastal_Erosion",
            "Coastal_Deposition"
        ],
        "21_Islands_of_India": [
            "Andaman_Islands",
            "Nicobar_Islands",
            "Lakshadweep",
            "Coral_Islands",
            "Volcanic_Islands",
            "Strategic_Importance",
            "Biodiversity",
            "Regional_Features"
        ],
        "22_Major_Mountain_Passes": [
            "Zoji_La",
            "Nathu_La",
            "Jelep_La",
            "Shipki_La",
            "Bara_Lacha_La",
            "Rohtang_Pass",
            "Lipu_Lekh",
            "Strategic_Importance"
        ],
        "23_Geographical_Regions_and_Resource_Base": [
            "Mountain_Resources",
            "Plain_Resources",
            "Plateau_Resources",
            "Coastal_Resources",
            "Island_Resources",
            "Resource_Distribution",
            "Regional_Development",
            "Economic_Linkages"
        ],
        "24_Physiography_and_Human_Activities": [
            "Settlement_Patterns",
            "Agriculture",
            "Transport",
            "Urbanization",
            "Industry",
            "Tourism",
            "Resource_Utilization",
            "Regional_Development"
        ],
        "25_Physiography_and_Environment": [
            "Biodiversity",
            "Ecosystems",
            "Deforestation",
            "Land_Degradation",
            "Mountain_Ecology",
            "Coastal_Ecology",
            "Environmental_Challenges",
            "Conservation"
        ],
        "26_Physiography_and_Natural_Hazards": [
            "Earthquakes",
            "Landslides",
            "Avalanches",
            "Floods",
            "Coastal_Hazards",
            "Desertification",
            "Hazard_Zones",
            "Disaster_Risk"
        ],
        "27_Maps_Diagrams_and_Case_Studies": [
            "Physiographic_Maps",
            "Relief_Maps",
            "Mountain_Case_Studies",
            "Plateau_Case_Studies",
            "Coastal_Case_Studies",
            "Island_Case_Studies",
            "Map_Based_Questions",
            "Regional_Analysis"
        ],
        "28_Current_Affairs_and_UPSC_Themes": [
            "Border_Infrastructure",
            "Strategic_Passes",
            "Himalayan_Changes",
            "Coastal_Zone_Management",
            "Island_Development",
            "Environmental_Issues",
            "Recent_Geographical_Developments",
            "UPSC_High_Yield_Topics"
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

    print(f"Creating Location and Physiography structure in: {target_base}")
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
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write("[]")
                    print(f"      - Created: {filename}")
                else:
                    print(f"      - Exists: {filename}")

if __name__ == "__main__":
    create_location_and_physiography_structure()