import os
import shutil

def create_agriculture_and_animal_husbandry_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography", "agriculture-and-animal-husbandry")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Agricultural_Geography_Fundamentals": [
            "Meaning_of_Agricultural_Geography",
            "Importance_of_Agriculture",
            "Role_in_Indian_Economy",
            "Agricultural_Land_Use",
            "Agricultural_Regions",
            "Agricultural_Diversity",
            "Characteristics_of_Indian_Agriculture",
            "Sources_of_Study"
        ],

        "02_Factors_Affecting_Agriculture": [
            "Climate",
            "Relief",
            "Soils",
            "Water_Availability",
            "Technology",
            "Land_Holdings",
            "Socio_Economic_Factors",
            "Government_Policies"
        ],

        "03_Agro_Climatic_Regions": [
            "Planning_Commission_Regions",
            "Agro_Ecological_Regions",
            "Humid_Regions",
            "Semi_Arid_Regions",
            "Arid_Regions",
            "Mountain_Agriculture",
            "Regional_Specialization",
            "Agricultural_Significance"
        ],

        "04_Land_Resources_and_Holdings": [
            "Land_Use_Pattern",
            "Operational_Holdings",
            "Marginal_Farmers",
            "Small_Farmers",
            "Land_Fragmentation",
            "Land_Reforms",
            "Tenancy",
            "Land_Resource_Challenges"
        ],

        "05_Irrigation_in_India": [
            "Canal_Irrigation",
            "Tank_Irrigation",
            "Well_Irrigation",
            "Tube_Wells",
            "Major_Irrigation_Projects",
            "Command_Area_Development",
            "Micro_Irrigation",
            "Irrigation_Challenges"
        ],

        "06_Cropping_Patterns": [
            "Kharif_Crops",
            "Rabi_Crops",
            "Zaid_Crops",
            "Mixed_Cropping",
            "Multiple_Cropping",
            "Crop_Rotation",
            "Cropping_Intensity",
            "Regional_Variations"
        ],

        "07_Foodgrain_Crops": [
            "Rice",
            "Wheat",
            "Maize",
            "Millets",
            "Barley",
            "Pulses",
            "Production_Patterns",
            "Major_Producing_States"
        ],

        "08_Commercial_Crops": [
            "Cotton",
            "Jute",
            "Sugarcane",
            "Tobacco",
            "Oilseeds",
            "Rubber",
            "Commercial_Agriculture",
            "Production_Regions"
        ],

        "09_Plantation_Crops": [
            "Tea",
            "Coffee",
            "Rubber",
            "Coconut",
            "Arecanut",
            "Spices",
            "Plantation_Regions",
            "Export_Importance"
        ],

        "10_Horticulture": [
            "Fruits",
            "Vegetables",
            "Floriculture",
            "Medicinal_Plants",
            "Aromatic_Plants",
            "Protected_Cultivation",
            "Horticulture_Missions",
            "Economic_Importance"
        ],

        "11_Green_Revolution": [
            "Background",
            "HYV_Seeds",
            "Technology_Package",
            "Regional_Impact",
            "Achievements",
            "Limitations",
            "Second_Green_Revolution",
            "Contemporary_Debates"
        ],

        "12_Agricultural_Inputs": [
            "Seeds",
            "Fertilizers",
            "Manures",
            "Pesticides",
            "Farm_Machinery",
            "Precision_Farming",
            "Extension_Services",
            "Input_Challenges"
        ],

        "13_Agricultural_Research_and_Education": [
            "ICAR",
            "Agricultural_Universities",
            "Krishi_Vigyan_Kendras",
            "Research_Institutions",
            "Seed_Development",
            "Crop_Improvement",
            "Technology_Transfer",
            "Innovation"
        ],

        "14_Agricultural_Marketing": [
            "APMC",
            "Mandis",
            "eNAM",
            "Storage",
            "Warehousing",
            "Cold_Chains",
            "Supply_Chain",
            "Marketing_Reforms"
        ],

        "15_Agricultural_Finance_and_Insurance": [
            "Institutional_Credit",
            "NABARD",
            "Kisan_Credit_Card",
            "Crop_Insurance",
            "PMFBY",
            "Rural_Banking",
            "Agricultural_Financing",
            "Credit_Challenges"
        ],

        "16_Agricultural_Policies_and_Schemes": [
            "National_Agricultural_Policy",
            "PM_KISAN",
            "Soil_Health_Card",
            "PMKSY",
            "National_Food_Security_Mission",
            "RKVY",
            "Government_Interventions",
            "Policy_Impact"
        ],

        "17_Food_Security_and_Buffer_Stocks": [
            "Food_Security",
            "FCI",
            "Procurement_System",
            "MSP",
            "Public_Distribution_System",
            "Buffer_Stocks",
            "Nutritional_Security",
            "Challenges"
        ],

        "18_Sustainable_Agriculture": [
            "Organic_Farming",
            "Natural_Farming",
            "Integrated_Farming",
            "Climate_Smart_Agriculture",
            "Conservation_Agriculture",
            "Agroforestry",
            "Sustainability_Challenges",
            "Future_Prospects"
        ],

        "19_Agricultural_Challenges": [
            "Climate_Change",
            "Water_Stress",
            "Soil_Degradation",
            "Farmer_Distress",
            "Price_Volatility",
            "Low_Productivity",
            "Regional_Disparities",
            "Structural_Problems"
        ],

        "20_Livestock_Geography": [
            "Livestock_Population",
            "Cattle",
            "Buffalo",
            "Sheep",
            "Goats",
            "Pigs",
            "Regional_Distribution",
            "Economic_Importance"
        ],

        "21_Dairy_Development": [
            "Milk_Production",
            "Operation_Flood",
            "White_Revolution",
            "Cooperative_Model",
            "Dairy_Processing",
            "Milk_Producing_States",
            "NDDB",
            "Challenges"
        ],

        "22_Poultry_Development": [
            "Broiler_Farming",
            "Layer_Farming",
            "Egg_Production",
            "Poultry_Clusters",
            "Feed_Management",
            "Commercial_Poultry",
            "Regional_Patterns",
            "Challenges"
        ],

        "23_Sheep_Goat_and_Pastoralism": [
            "Wool_Production",
            "Pastoral_Communities",
            "Nomadic_Herding",
            "Goat_Rearing",
            "Sheep_Rearing",
            "Pasture_Resources",
            "Livelihoods",
            "Challenges"
        ],

        "24_Fisheries_and_Aquaculture": [
            "Marine_Fisheries",
            "Inland_Fisheries",
            "Aquaculture",
            "Blue_Revolution",
            "Fish_Producing_States",
            "Fishing_Harbours",
            "Exports",
            "Challenges"
        ],

        "25_Animal_Health_and_Breeding": [
            "Veterinary_Services",
            "Artificial_Insemination",
            "Breed_Improvement",
            "Disease_Control",
            "Vaccination",
            "Indigenous_Breeds",
            "Livestock_Missions",
            "Productivity_Enhancement"
        ],

        "26_Agriculture_and_Environment": [
            "Land_Degradation",
            "Desertification",
            "Groundwater_Depletion",
            "Agrochemical_Pollution",
            "Biodiversity",
            "Crop_Residue_Burning",
            "Environmental_Impacts",
            "Mitigation_Strategies"
        ],

        "27_Agricultural_Geography_of_States": [
            "Punjab_and_Haryana",
            "Gangetic_Plains",
            "Deccan_Plateau",
            "North_Eastern_Region",
            "Coastal_Agriculture",
            "Mountain_Agriculture",
            "Regional_Case_Studies",
            "State_Wise_Patterns"
        ],

        "28_Legacy_Current_Affairs_and_Future": [
            "Agricultural_Transformation",
            "Digital_Agriculture",
            "Agri_Startups",
            "Farmer_Producer_Organizations",
            "Emerging_Technologies",
            "Current_Affairs_Themes",
            "Future_of_Agriculture",
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

    print(f"Creating Agriculture and Animal Husbandry structure in: {target_base}")
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
    create_agriculture_and_animal_husbandry_structure()