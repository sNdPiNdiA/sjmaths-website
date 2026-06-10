import os
import shutil

def create_economic_geography_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "world-geography",
        "economic-geography"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Economic_Geography_Fundamentals": [
            "Meaning_of_Economic_Geography",
            "Nature_and_Scope",
            "Economic_Activities",
            "Primary_Secondary_Tertiary_Sectors",
            "Resource_Utilization",
            "Spatial_Patterns",
            "Importance_of_Study",
            "Sources_of_Study"
        ],

        "02_World_Resources": [
            "Natural_Resources",
            "Renewable_Resources",
            "Non_Renewable_Resources",
            "Resource_Distribution",
            "Resource_Regions",
            "Resource_Conservation",
            "Resource_Utilization",
            "Global_Patterns"
        ],

        "03_Agricultural_Geography": [
            "Agricultural_Systems",
            "Subsistence_Agriculture",
            "Commercial_Agriculture",
            "Plantation_Agriculture",
            "Mixed_Farming",
            "Shifting_Cultivation",
            "Agricultural_Regions",
            "Global_Patterns"
        ],

        "04_World_Crop_Production": [
            "Rice",
            "Wheat",
            "Maize",
            "Soybean",
            "Cotton",
            "Sugarcane",
            "Coffee",
            "Tea"
        ],

        "05_Livestock_and_Dairy_Farming": [
            "Pastoralism",
            "Ranching",
            "Dairy_Farming",
            "Livestock_Regions",
            "Wool_Production",
            "Meat_Industry",
            "Poultry_Farming",
            "Global_Trends"
        ],

        "06_Fisheries_and_Aquaculture": [
            "Marine_Fisheries",
            "Inland_Fisheries",
            "Aquaculture",
            "Fishing_Grounds",
            "Fish_Production",
            "Fishing_Technology",
            "Challenges",
            "Global_Trends"
        ],

        "07_Forestry_and_Forest_Resources": [
            "Forest_Resources",
            "Timber_Production",
            "Softwood_Forests",
            "Hardwood_Forests",
            "Forest_Based_Industries",
            "Deforestation",
            "Conservation",
            "Global_Patterns"
        ],

        "08_Mineral_Resources": [
            "Iron_Ore",
            "Copper",
            "Bauxite",
            "Gold",
            "Silver",
            "Rare_Earth_Minerals",
            "Mineral_Distribution",
            "Mining_Regions"
        ],

        "09_Energy_Resources": [
            "Coal",
            "Petroleum",
            "Natural_Gas",
            "Hydropower",
            "Nuclear_Energy",
            "Renewable_Energy",
            "Energy_Regions",
            "Global_Trends"
        ],

        "10_Industrial_Geography": [
            "Industrialization",
            "Industrial_Location",
            "Industrial_Regions",
            "Manufacturing",
            "Industrial_Clusters",
            "Industrial_Development",
            "Agglomeration",
            "Global_Patterns"
        ],

        "11_Major_Industries_of_the_World": [
            "Iron_and_Steel",
            "Textile_Industry",
            "Automobile_Industry",
            "Chemical_Industry",
            "Electronics_Industry",
            "IT_Industry",
            "Pharmaceuticals",
            "Food_Processing"
        ],

        "12_Transport_Geography": [
            "Road_Transport",
            "Rail_Transport",
            "Air_Transport",
            "Water_Transport",
            "Pipelines",
            "Transport_Networks",
            "Logistics",
            "Connectivity"
        ],

        "13_World_Trade": [
            "International_Trade",
            "Exports",
            "Imports",
            "Balance_of_Trade",
            "Trade_Routes",
            "Trade_Blocs",
            "Globalization",
            "Trade_Patterns"
        ],

        "14_Major_Sea_Routes": [
            "North_Atlantic_Route",
            "Suez_Route",
            "Panama_Route",
            "Cape_Route",
            "Pacific_Routes",
            "Arctic_Routes",
            "Maritime_Trade",
            "Strategic_Importance"
        ],

        "15_Major_Air_Routes": [
            "Trans_Atlantic_Routes",
            "Trans_Pacific_Routes",
            "European_Air_Network",
            "Asian_Air_Network",
            "Cargo_Aviation",
            "Passenger_Flows",
            "Aviation_Hubs",
            "Global_Connectivity"
        ],

        "16_Trade_Blocs_and_Economic_Organizations": [
            "WTO",
            "European_Union",
            "USMCA",
            "ASEAN",
            "BRICS",
            "SAARC",
            "APEC",
            "Economic_Cooperation"
        ],

        "17_Globalization_and_Economic_Integration": [
            "Globalization",
            "FDI",
            "Multinational_Corporations",
            "Global_Value_Chains",
            "Economic_Integration",
            "Benefits",
            "Challenges",
            "Future_Trends"
        ],

        "18_Human_Development_and_Economy": [
            "HDI",
            "Quality_of_Life",
            "Income_Levels",
            "Development_Indicators",
            "Regional_Disparities",
            "Social_Development",
            "Economic_Growth",
            "Human_Capital"
        ],

        "19_Population_and_Economic_Development": [
            "Labour_Force",
            "Demographic_Dividend",
            "Urbanization",
            "Migration",
            "Employment",
            "Economic_Productivity",
            "Population_Pressure",
            "Development_Patterns"
        ],

        "20_Urban_Economic_Geography": [
            "Cities",
            "Urban_Economy",
            "Central_Business_District",
            "Industrial_Cities",
            "Megacities",
            "Urban_Services",
            "Urban_Growth",
            "Challenges"
        ],

        "21_Tourism_Geography": [
            "Tourism_Resources",
            "Ecotourism",
            "Cultural_Tourism",
            "Adventure_Tourism",
            "Tourism_Regions",
            "Economic_Impact",
            "Sustainable_Tourism",
            "Global_Trends"
        ],

        "22_Blue_Economy": [
            "Marine_Resources",
            "Ocean_Trade",
            "Fisheries",
            "Offshore_Energy",
            "Maritime_Economy",
            "Coastal_Development",
            "Blue_Growth",
            "Sustainability"
        ],

        "23_Green_Economy_and_Sustainability": [
            "Sustainable_Development",
            "Green_Energy",
            "Circular_Economy",
            "Climate_Economics",
            "Carbon_Markets",
            "Resource_Efficiency",
            "Environmental_Policies",
            "Future_Prospects"
        ],

        "24_Regional_Economic_Geography": [
            "North_America",
            "Europe",
            "Asia_Pacific",
            "Africa",
            "Latin_America",
            "Middle_East",
            "Australia",
            "Regional_Comparisons"
        ],

        "25_Geography_of_Development_and_Underdevelopment": [
            "Developed_Countries",
            "Developing_Countries",
            "Least_Developed_Countries",
            "North_South_Divide",
            "Dependency_Theory",
            "Modernization_Theory",
            "Regional_Disparities",
            "Development_Models"
        ],

        "26_Economic_Corridors_and_Connectivity": [
            "Belt_and_Road_Initiative",
            "International_North_South_Corridor",
            "Economic_Corridors",
            "Trade_Connectivity",
            "Logistics_Hubs",
            "Infrastructure_Development",
            "Regional_Integration",
            "Strategic_Projects"
        ],

        "27_Current_Affairs_and_Economic_Issues": [
            "Global_Recession",
            "Supply_Chain_Disruptions",
            "Energy_Crisis",
            "Food_Security",
            "Trade_Wars",
            "Climate_Economics",
            "Emerging_Markets",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Agricultural_Maps",
            "Industrial_Maps",
            "Mineral_Maps",
            "Energy_Maps",
            "Trade_Route_Maps",
            "Economic_Data",
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

    print(f"Creating Economic Geography structure in: {target_base}")

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
    create_economic_geography_structure()