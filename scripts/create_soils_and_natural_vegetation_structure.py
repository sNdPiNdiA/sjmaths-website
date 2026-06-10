import os
import shutil

def create_soils_and_natural_vegetation_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography", "soils-and-natural-vegetation")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Soil_Geography_Fundamentals": [
            "Meaning_of_Soil",
            "Soil_Profile",
            "Soil_Horizons",
            "Pedogenesis",
            "Importance_of_Soils",
            "Soil_as_a_Resource",
            "Characteristics_of_Indian_Soils",
            "Sources_of_Study"
        ],

        "02_Factors_of_Soil_Formation": [
            "Parent_Rock",
            "Climate",
            "Relief",
            "Organisms",
            "Time",
            "Topography",
            "Weathering",
            "Soil_Forming_Processes"
        ],

        "03_Soil_Classification_in_India": [
            "ICAR_Classification",
            "Major_Soil_Groups",
            "Zonal_Soils",
            "Azonal_Soils",
            "Intrazonal_Soils",
            "Regional_Distribution",
            "Classification_Methods",
            "Comparative_Features"
        ],

        "04_Alluvial_Soils": [
            "Formation",
            "Khadar",
            "Bhangar",
            "Distribution",
            "Physical_Properties",
            "Chemical_Properties",
            "Agricultural_Importance",
            "Regional_Variations"
        ],

        "05_Black_Soils": [
            "Regur_Soil",
            "Deccan_Traps",
            "Clay_Content",
            "Moisture_Retention",
            "Distribution",
            "Cotton_Cultivation",
            "Properties",
            "Agricultural_Importance"
        ],

        "06_Red_and_Yellow_Soils": [
            "Formation",
            "Iron_Content",
            "Distribution",
            "Physical_Properties",
            "Chemical_Properties",
            "Agricultural_Use",
            "Regional_Features",
            "Management"
        ],

        "07_Laterite_and_Lateritic_Soils": [
            "Laterization",
            "Tropical_Weathering",
            "Distribution",
            "Properties",
            "Nutrient_Status",
            "Agricultural_Use",
            "Regional_Characteristics",
            "Economic_Importance"
        ],

        "08_Arid_and_Desert_Soils": [
            "Desert_Formation",
            "Distribution",
            "Salinity",
            "Alkalinity",
            "Physical_Properties",
            "Agricultural_Limitations",
            "Management_Practices",
            "Regional_Features"
        ],

        "09_Forest_and_Mountain_Soils": [
            "Forest_Soils",
            "Mountain_Soils",
            "Altitudinal_Variation",
            "Distribution",
            "Properties",
            "Vegetation_Linkages",
            "Regional_Characteristics",
            "Land_Use"
        ],

        "10_Saline_Alkaline_and_Peat_Soils": [
            "Saline_Soils",
            "Alkaline_Soils",
            "Peaty_Soils",
            "Marshy_Soils",
            "Distribution",
            "Formation",
            "Reclamation",
            "Agricultural_Use"
        ],

        "11_Soil_Fertility_and_Productivity": [
            "Macronutrients",
            "Micronutrients",
            "Soil_Fertility",
            "Soil_Productivity",
            "Organic_Matter",
            "Nutrient_Deficiency",
            "Soil_Testing",
            "Productivity_Management"
        ],

        "12_Soil_Degradation": [
            "Soil_Erosion",
            "Water_Erosion",
            "Wind_Erosion",
            "Gully_Erosion",
            "Ravines",
            "Nutrient_Depletion",
            "Human_Impacts",
            "Environmental_Consequences"
        ],

        "13_Soil_Conservation": [
            "Contour_Bunding",
            "Terracing",
            "Shelter_Belts",
            "Afforestation",
            "Watershed_Management",
            "Check_Dams",
            "Conservation_Techniques",
            "Policy_Initiatives"
        ],

        "14_Natural_Vegetation_Fundamentals": [
            "Meaning_of_Natural_Vegetation",
            "Flora_of_India",
            "Vegetation_Classification",
            "Plant_Communities",
            "Ecological_Significance",
            "Vegetation_Regions",
            "Biogeography",
            "Sources_of_Study"
        ],

        "15_Factors_Affecting_Vegetation": [
            "Climate",
            "Relief",
            "Soils",
            "Altitude",
            "Rainfall",
            "Temperature",
            "Human_Influence",
            "Environmental_Controls"
        ],

        "16_Tropical_Evergreen_Forests": [
            "Distribution",
            "Climatic_Requirements",
            "Species_Composition",
            "Canopy_Structure",
            "Biodiversity",
            "Economic_Importance",
            "Conservation_Issues",
            "Regional_Examples"
        ],

        "17_Tropical_Deciduous_Forests": [
            "Moist_Deciduous",
            "Dry_Deciduous",
            "Distribution",
            "Species_Composition",
            "Economic_Importance",
            "Forest_Products",
            "Human_Use",
            "Regional_Examples"
        ],

        "18_Thorn_Forests_and_Scrub": [
            "Arid_Vegetation",
            "Semi_Arid_Vegetation",
            "Adaptations",
            "Distribution",
            "Species",
            "Economic_Importance",
            "Environmental_Role",
            "Regional_Examples"
        ],

        "19_Montane_Forests": [
            "Altitudinal_Zonation",
            "Temperate_Forests",
            "Coniferous_Forests",
            "Alpine_Vegetation",
            "Distribution",
            "Species",
            "Ecological_Significance",
            "Regional_Examples"
        ],

        "20_Mangrove_Forests": [
            "Mangrove_Ecosystems",
            "Tidal_Influence",
            "Sundarbans",
            "Species_Composition",
            "Coastal_Protection",
            "Carbon_Storage",
            "Threats",
            "Conservation"
        ],

        "21_Grasslands_of_India": [
            "Tropical_Grasslands",
            "Montane_Grasslands",
            "Savanna_Regions",
            "Pasture_Lands",
            "Biodiversity",
            "Livestock_Linkages",
            "Threats",
            "Conservation"
        ],

        "22_Forest_Resources_and_Products": [
            "Timber",
            "Fuelwood",
            "Bamboo",
            "Minor_Forest_Products",
            "Medicinal_Plants",
            "Forest_Based_Livelihoods",
            "Economic_Importance",
            "Resource_Management"
        ],

        "23_Forest_Conservation_and_Policies": [
            "Forest_Policy",
            "Joint_Forest_Management",
            "Social_Forestry",
            "Farm_Forestry",
            "Community_Participation",
            "Afforestation_Programmes",
            "Forest_Governance",
            "Policy_Framework"
        ],

        "24_Biodiversity_and_Hotspots": [
            "Biodiversity",
            "Western_Ghats",
            "Eastern_Himalaya",
            "Endemism",
            "Species_Richness",
            "Threatened_Species",
            "Conservation_Priorities",
            "Global_Significance"
        ],

        "25_Protected_Areas_and_Biosphere_Reserves": [
            "Biosphere_Reserves",
            "National_Parks",
            "Wildlife_Sanctuaries",
            "Conservation_Reserves",
            "Protected_Area_Network",
            "UNESCO_Recognition",
            "Management_Strategies",
            "Conservation_Outcomes"
        ],

        "26_Soils_Vegetation_and_Agriculture": [
            "Soil_Crop_Relationships",
            "Vegetation_Agriculture_Linkages",
            "Land_Capability",
            "Agro_Ecological_Zones",
            "Cropping_Patterns",
            "Sustainable_Land_Use",
            "Regional_Comparisons",
            "Agricultural_Implications"
        ],

        "27_Environmental_Challenges": [
            "Deforestation",
            "Land_Degradation",
            "Desertification",
            "Forest_Fires",
            "Invasive_Species",
            "Climate_Change_Impacts",
            "Habitat_Loss",
            "Restoration_Strategies"
        ],

        "28_Maps_Current_Affairs_and_UPSC_Themes": [
            "Soil_Distribution_Maps",
            "Forest_Type_Maps",
            "Mangrove_Locations",
            "Biosphere_Reserve_Maps",
            "Current_Affairs",
            "PYQ_Themes",
            "Map_Based_Questions",
            "High_Yield_Topics"
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

    print(f"Creating Soils and Natural Vegetation structure in: {target_base}")
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
    create_soils_and_natural_vegetation_structure()