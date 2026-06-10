import os
import shutil

def create_ecology_and_ecosystems_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "ecology-and-ecosystems"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Ecology_Fundamentals": [
            "Meaning_of_Ecology",
            "Scope_of_Ecology",
            "Branches_of_Ecology",
            "Levels_of_Organization",
            "Ecological_Hierarchy",
            "Ecological_Interactions",
            "Ecological_Principles",
            "Importance_of_Ecology"
        ],

        "02_Ecosystem_Fundamentals": [
            "Meaning_of_Ecosystem",
            "Structure_of_Ecosystem",
            "Functions_of_Ecosystem",
            "Components_of_Ecosystem",
            "Natural_Ecosystems",
            "Artificial_Ecosystems",
            "Ecosystem_Dynamics",
            "Ecosystem_Services"
        ],

        "03_Biotic_Components": [
            "Producers",
            "Primary_Consumers",
            "Secondary_Consumers",
            "Tertiary_Consumers",
            "Omnivores",
            "Decomposers",
            "Detritivores",
            "Keystone_Species"
        ],

        "04_Abiotic_Components": [
            "Sunlight",
            "Temperature",
            "Water",
            "Air",
            "Soil",
            "Nutrients",
            "Climate",
            "Topography"
        ],

        "05_Habitat_and_Niche": [
            "Habitat_Concept",
            "Types_of_Habitat",
            "Ecological_Niche",
            "Fundamental_Niche",
            "Realized_Niche",
            "Niche_Overlap",
            "Niche_Differentiation",
            "Habitat_Fragmentation"
        ],

        "06_Population_Ecology": [
            "Population_Characteristics",
            "Population_Density",
            "Population_Growth",
            "Natality",
            "Mortality",
            "Age_Structure",
            "Carrying_Capacity",
            "Population_Regulation"
        ],

        "07_Community_Ecology": [
            "Community_Structure",
            "Species_Diversity",
            "Dominance",
            "Stratification",
            "Ecotone",
            "Edge_Effect",
            "Ecological_Communities",
            "Community_Dynamics"
        ],

        "08_Ecological_Interactions": [
            "Mutualism",
            "Commensalism",
            "Parasitism",
            "Predation",
            "Competition",
            "Amensalism",
            "Neutralism",
            "Symbiosis"
        ],

        "09_Food_Chain": [
            "Grazing_Food_Chain",
            "Detritus_Food_Chain",
            "Trophic_Levels",
            "Energy_Transfer",
            "Food_Chain_Length",
            "Food_Chain_Stability",
            "Examples_of_Food_Chains",
            "Ecological_Importance"
        ],

        "10_Food_Web": [
            "Food_Web_Concept",
            "Complex_Feeding_Relationships",
            "Interconnected_Food_Chains",
            "Energy_Pathways",
            "Ecosystem_Stability",
            "Species_Interactions",
            "Examples_of_Food_Webs",
            "Ecological_Significance"
        ],

        "11_Ecological_Pyramids": [
            "Pyramid_of_Numbers",
            "Pyramid_of_Biomass",
            "Pyramid_of_Energy",
            "Upright_Pyramids",
            "Inverted_Pyramids",
            "Ecological_Efficiency",
            "Limitations",
            "Applications"
        ],

        "12_Energy_Flow_in_Ecosystems": [
            "Unidirectional_Energy_Flow",
            "Lindemans_Ten_Percent_Law",
            "Primary_Productivity",
            "Secondary_Productivity",
            "Gross_Primary_Productivity",
            "Net_Primary_Productivity",
            "Energy_Budget",
            "Ecological_Efficiency"
        ],

        "13_Biogeochemical_Cycles": [
            "Concept_of_Biogeochemical_Cycles",
            "Nutrient_Cycling",
            "Reservoir_Pools",
            "Gaseous_Cycles",
            "Sedimentary_Cycles",
            "Human_Impacts",
            "Cycle_Disruptions",
            "Ecological_Importance"
        ],

        "14_Carbon_Cycle": [
            "Carbon_Reservoirs",
            "Photosynthesis",
            "Respiration",
            "Decomposition",
            "Oceanic_Carbon_Storage",
            "Carbon_Sequestration",
            "Carbon_Emissions",
            "Climate_Linkages"
        ],

        "15_Nitrogen_Cycle": [
            "Nitrogen_Fixation",
            "Nitrification",
            "Assimilation",
            "Ammonification",
            "Denitrification",
            "Nitrogen_Reservoirs",
            "Human_Interference",
            "Ecological_Importance"
        ],

        "16_Water_Cycle": [
            "Evaporation",
            "Transpiration",
            "Condensation",
            "Precipitation",
            "Infiltration",
            "Runoff",
            "Groundwater_Recharge",
            "Hydrological_Balance"
        ],

        "17_Ecological_Succession": [
            "Meaning_of_Succession",
            "Primary_Succession",
            "Secondary_Succession",
            "Successional_Stages",
            "Pioneer_Community",
            "Climax_Community",
            "Hydrarch_Succession",
            "Xerarch_Succession"
        ],

        "18_Ecosystem_Productivity": [
            "Primary_Productivity",
            "Secondary_Productivity",
            "Factors_Affecting_Productivity",
            "Terrestrial_Productivity",
            "Aquatic_Productivity",
            "Measurement_of_Productivity",
            "Global_Patterns",
            "Ecological_Significance"
        ],

        "19_Ecosystem_Services": [
            "Provisioning_Services",
            "Regulating_Services",
            "Supporting_Services",
            "Cultural_Services",
            "Economic_Value",
            "Natural_Capital",
            "Ecosystem_Valuation",
            "Conservation_Relevance"
        ],

        "20_Biomes_of_the_World": [
            "Tropical_Rainforest",
            "Savanna",
            "Desert_Biome",
            "Temperate_Forest",
            "Taiga",
            "Tundra",
            "Grasslands",
            "Mediterranean_Biome"
        ],

        "21_Aquatic_Ecosystems": [
            "Freshwater_Ecosystems",
            "Lentic_Ecosystems",
            "Lotic_Ecosystems",
            "Wetland_Ecosystems",
            "Marine_Ecosystems",
            "Estuarine_Ecosystems",
            "Coral_Reef_Ecosystems",
            "Mangrove_Ecosystems"
        ],

        "22_Current_Affairs_and_Ecology": [
            "Ecosystem_Restoration",
            "UN_Decade_on_Restoration",
            "Blue_Carbon_Ecosystems",
            "Nature_Based_Solutions",
            "Ecological_Reports",
            "Government_Initiatives",
            "International_Initiatives",
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

    print(f"Creating Ecology and Ecosystems structure in: {target_base}")

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
    create_ecology_and_ecosystems_structure()