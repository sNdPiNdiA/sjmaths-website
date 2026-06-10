import os
import shutil

def create_environmental_geography_and_biomes_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "environmental-geography-and-biomes"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Biomes_Fundamentals": [
            "Meaning_of_Biomes",
            "Characteristics_of_Biomes",
            "Biome_Classification",
            "Climate_and_Biomes",
            "Latitude_and_Biomes",
            "Altitude_and_Biomes",
            "Biome_Distribution",
            "Ecological_Significance"
        ],

        "02_Tropical_Rainforests": [
            "Climate_Characteristics",
            "Vegetation_Structure",
            "Biodiversity",
            "Nutrient_Cycling",
            "Global_Distribution",
            "Indian_Examples",
            "Threats",
            "Conservation"
        ],

        "03_Tropical_Deciduous_Forests": [
            "Moist_Deciduous_Forests",
            "Dry_Deciduous_Forests",
            "Rainfall_Requirements",
            "Major_Species",
            "Indian_Distribution",
            "Economic_Importance",
            "Threats",
            "Conservation"
        ],

        "04_Coniferous_and_Taiga_Forests": [
            "Taiga_Biome",
            "Climate_Conditions",
            "Coniferous_Species",
            "Adaptations",
            "Wildlife",
            "Global_Distribution",
            "Economic_Value",
            "Threats"
        ],

        "05_Temperate_Forests": [
            "Climate_Characteristics",
            "Temperate_Deciduous_Forests",
            "Temperate_Evergreen_Forests",
            "Vegetation",
            "Wildlife",
            "Distribution",
            "Human_Impact",
            "Conservation"
        ],

        "06_Grassland_Biomes": [
            "Tropical_Grasslands",
            "Temperate_Grasslands",
            "Savanna",
            "Prairies",
            "Steppes",
            "Pampas",
            "Grassland_Biodiversity",
            "Threats"
        ],

        "07_Desert_Biomes": [
            "Hot_Deserts",
            "Cold_Deserts",
            "Desert_Climate",
            "Xerophytic_Adaptations",
            "Desert_Fauna",
            "Global_Deserts",
            "Indian_Deserts",
            "Desertification"
        ],

        "08_Tundra_Biomes": [
            "Arctic_Tundra",
            "Alpine_Tundra",
            "Permafrost",
            "Vegetation",
            "Wildlife",
            "Climate_Conditions",
            "Global_Distribution",
            "Climate_Change_Impacts"
        ],

        "09_Mountain_Ecosystems": [
            "Mountain_Environment",
            "Altitudinal_Zonation",
            "Mountain_Biodiversity",
            "Himalayan_Ecosystems",
            "Western_Ghats_Ecosystems",
            "Mountain_Services",
            "Threats",
            "Conservation"
        ],

        "10_Himalayan_Ecology": [
            "Trans_Himalaya",
            "Western_Himalaya",
            "Central_Himalaya",
            "Eastern_Himalaya",
            "Himalayan_Biodiversity",
            "Glacial_Ecosystems",
            "Threats",
            "Conservation_Issues"
        ],

        "11_Wetland_Ecosystems": [
            "Wetland_Definition",
            "Types_of_Wetlands",
            "Ecological_Functions",
            "Wetland_Biodiversity",
            "Carbon_Storage",
            "Indian_Wetlands",
            "Threats",
            "Conservation"
        ],

        "12_Ramsar_Sites_of_India": [
            "Ramsar_Convention_Linkage",
            "Designation_Criteria",
            "Major_Ramsar_Sites",
            "State_Wise_Distribution",
            "Wetland_Management",
            "Biodiversity_Value",
            "Current_Affairs",
            "Conservation_Challenges"
        ],

        "13_Mangrove_Ecosystems": [
            "Mangrove_Characteristics",
            "Mangrove_Adaptations",
            "Indian_Mangroves",
            "Sundarbans",
            "Mangrove_Biodiversity",
            "Coastal_Protection",
            "Threats",
            "Conservation"
        ],

        "14_Coral_Reef_Ecosystems": [
            "Coral_Polyps",
            "Coral_Formation",
            "Types_of_Coral_Reefs",
            "Fringing_Reefs",
            "Barrier_Reefs",
            "Atolls",
            "Coral_Bleaching",
            "Conservation"
        ],

        "15_Coastal_and_Marine_Ecosystems": [
            "Coastal_Zones",
            "Estuaries",
            "Lagoons",
            "Salt_Marshes",
            "Marine_Productivity",
            "Marine_Biodiversity",
            "Blue_Economy",
            "Threats"
        ],

        "16_Island_Ecosystems": [
            "Island_Biogeography",
            "Andaman_and_Nicobar",
            "Lakshadweep",
            "Endemism",
            "Island_Biodiversity",
            "Coral_Islands",
            "Threats",
            "Conservation"
        ],

        "17_Indian_Biogeographic_Zones": [
            "Trans_Himalaya",
            "Himalaya",
            "Desert",
            "Semi_Arid",
            "Western_Ghats",
            "Deccan_Peninsula",
            "Gangetic_Plains",
            "Coasts_and_Islands"
        ],

        "18_Ecologically_Sensitive_Areas": [
            "Ecologically_Sensitive_Zones",
            "Western_Ghats_ESA",
            "Eco_Sensitive_Areas",
            "Buffer_Zones",
            "Protected_Landscapes",
            "Conservation_Importance",
            "Policy_Framework",
            "Current_Issues"
        ],

        "19_Biogeography_and_Species_Distribution": [
            "Species_Distribution",
            "Endemism",
            "Dispersal",
            "Vicariance",
            "Biogeographic_Barriers",
            "Island_Biogeography",
            "Range_Shifts",
            "Climate_Influence"
        ],

        "20_Current_Affairs_and_Biomes": [
            "New_Ramsar_Sites",
            "Coral_Bleaching_Events",
            "Mangrove_Assessments",
            "Forest_Survey_Reports",
            "Wetland_Reports",
            "Mountain_Ecology_Reports",
            "Government_Initiatives",
            "UPSC_High_Yield_Topics"
        ]

    }

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

    print(f"Creating Environmental Geography and Biomes structure in: {target_base}")

    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for filename in leaf_files:
                file_path = os.path.join(topic_path, filename)

                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("[]")

if __name__ == "__main__":
    create_environmental_geography_and_biomes_structure()