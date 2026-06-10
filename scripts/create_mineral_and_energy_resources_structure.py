import os
import shutil

def create_mineral_and_energy_resources_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography", "mineral-and-energy-resources")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Mineral_and_Energy_Geography_Fundamentals": [
            "Meaning_of_Minerals",
            "Meaning_of_Energy_Resources",
            "Resource_Classification",
            "Economic_Importance",
            "Distribution_Patterns",
            "Resource_Base_of_India",
            "Resource_Geography",
            "Sources_of_Study"
        ],

        "02_Geological_Basis_of_Mineral_Resources": [
            "Rock_Types",
            "Mineral_Formation",
            "Ore_Deposits",
            "Geological_Structures",
            "Shield_Areas",
            "Sedimentary_Basins",
            "Tectonic_Control",
            "Mineralization_Processes"
        ],

        "03_Mineral_Classification": [
            "Metallic_Minerals",
            "Non_Metallic_Minerals",
            "Energy_Minerals",
            "Ferrous_Minerals",
            "Non_Ferrous_Minerals",
            "Atomic_Minerals",
            "Strategic_Minerals",
            "Classification_Systems"
        ],

        "04_Iron_Ore_Resources": [
            "Hematite",
            "Magnetite",
            "Major_Deposits",
            "Iron_Ore_Belts",
            "Leading_States",
            "Mining_Regions",
            "Industrial_Importance",
            "Export_and_Trade"
        ],

        "05_Manganese_and_Chromite": [
            "Manganese_Deposits",
            "Chromite_Deposits",
            "Distribution",
            "Uses_in_Industry",
            "Leading_States",
            "Mining_Regions",
            "Export_Potential",
            "Economic_Importance"
        ],

        "06_Bauxite_and_Aluminium": [
            "Bauxite_Formation",
            "Major_Deposits",
            "Aluminium_Industry_Linkages",
            "Leading_States",
            "Mining_Regions",
            "Processing",
            "Industrial_Uses",
            "Economic_Importance"
        ],

        "07_Copper_Lead_Zinc_and_Nickel": [
            "Copper_Deposits",
            "Lead_Deposits",
            "Zinc_Deposits",
            "Nickel_Resources",
            "Major_Mining_Areas",
            "Industrial_Applications",
            "Production_Trends",
            "Strategic_Importance"
        ],

        "08_Gold_Silver_and_Precious_Minerals": [
            "Gold_Deposits",
            "Kolar_Gold_Fields",
            "Hutti_Gold_Mines",
            "Silver_Resources",
            "Precious_Minerals",
            "Mining_History",
            "Economic_Importance",
            "Production_Trends"
        ],

        "09_Non_Metallic_Minerals": [
            "Limestone",
            "Mica",
            "Gypsum",
            "Dolomite",
            "Phosphorite",
            "Kaolin",
            "Industrial_Uses",
            "Distribution"
        ],

        "10_Rare_Earth_and_Critical_Minerals": [
            "Rare_Earth_Elements",
            "Lithium",
            "Cobalt",
            "Graphite",
            "Titanium",
            "Critical_Mineral_Policy",
            "Strategic_Importance",
            "Emerging_Demand"
        ],

        "11_Mineral_Belts_of_India": [
            "North_Eastern_Peninsular_Belt",
            "South_Western_Belt",
            "North_Western_Belt",
            "Central_Belt",
            "Coastal_Mineral_Belt",
            "Spatial_Distribution",
            "Regional_Characteristics",
            "Comparative_Analysis"
        ],

        "12_Mining_in_India": [
            "Mining_Methods",
            "Open_Cast_Mining",
            "Underground_Mining",
            "Mining_Regions",
            "Mineral_Extraction",
            "Labour_and_Mining",
            "Mining_Technology",
            "Production_Challenges"
        ],

        "13_Coal_Resources": [
            "Gondwana_Coal",
            "Tertiary_Coal",
            "Coalfields",
            "Jharia",
            "Raniganj",
            "Singrauli",
            "Coal_Production",
            "Coal_Quality"
        ],

        "14_Petroleum_Resources": [
            "Assam_Oilfields",
            "Mumbai_High",
            "Krishna_Godavari_Basin",
            "Cambay_Basin",
            "Onshore_Resources",
            "Offshore_Resources",
            "Exploration",
            "Production"
        ],

        "15_Natural_Gas_Resources": [
            "Conventional_Gas",
            "Shale_Gas",
            "CBM",
            "Gas_Basins",
            "KG_D6",
            "Production_Regions",
            "Gas_Infrastructure",
            "Energy_Importance"
        ],

        "16_Petroleum_and_Gas_Infrastructure": [
            "Refineries",
            "Pipelines",
            "LNG_Terminals",
            "Strategic_Petroleum_Reserves",
            "Distribution_Network",
            "Downstream_Industry",
            "Energy_Logistics",
            "Infrastructure_Development"
        ],

        "17_Thermal_Power": [
            "Coal_Based_Power",
            "Gas_Based_Power",
            "Thermal_Power_Stations",
            "Installed_Capacity",
            "Fuel_Supply",
            "Regional_Distribution",
            "Challenges",
            "Future_Trends"
        ],

        "18_Hydropower_Resources": [
            "Hydropower_Potential",
            "Major_Hydel_Projects",
            "River_Basin_Potential",
            "Run_of_River_Projects",
            "Multipurpose_Projects",
            "Regional_Distribution",
            "Advantages",
            "Challenges"
        ],

        "19_Nuclear_Energy": [
            "Uranium",
            "Thorium",
            "Nuclear_Power_Stations",
            "Three_Stage_Nuclear_Programme",
            "Atomic_Minerals",
            "Fuel_Cycle",
            "Strategic_Significance",
            "Challenges"
        ],

        "20_Solar_Energy": [
            "Solar_Potential",
            "Solar_Parks",
            "Photovoltaics",
            "Rooftop_Solar",
            "National_Solar_Mission",
            "Regional_Distribution",
            "Technological_Developments",
            "Challenges"
        ],

        "21_Wind_Energy": [
            "Wind_Corridors",
            "Tamil_Nadu",
            "Gujarat",
            "Karnataka",
            "Offshore_Wind",
            "Installed_Capacity",
            "Technological_Progress",
            "Challenges"
        ],

        "22_Other_Renewable_Energy": [
            "Biomass_Energy",
            "Biogas",
            "Small_Hydel",
            "Geothermal_Energy",
            "Tidal_Energy",
            "Wave_Energy",
            "Waste_to_Energy",
            "Emerging_Technologies"
        ],

        "23_Energy_Security_of_India": [
            "Energy_Demand",
            "Import_Dependence",
            "Energy_Mix",
            "Strategic_Reserves",
            "Supply_Security",
            "Energy_Transition",
            "Geopolitical_Dimensions",
            "Future_Challenges"
        ],

        "24_Energy_Policies_and_Institutions": [
            "National_Energy_Policy",
            "Ministry_of_Power",
            "MNRE",
            "Coal_India",
            "ONGC",
            "Energy_Governance",
            "Regulatory_Framework",
            "Policy_Reforms"
        ],

        "25_Mineral_and_Energy_Conservation": [
            "Resource_Efficiency",
            "Mineral_Conservation",
            "Energy_Efficiency",
            "Recycling",
            "Circular_Economy",
            "Demand_Management",
            "Conservation_Policies",
            "Sustainable_Use"
        ],

        "26_Environmental_Impacts": [
            "Mining_Degradation",
            "Land_Subsidence",
            "Air_Pollution",
            "Water_Pollution",
            "Thermal_Pollution",
            "Carbon_Emissions",
            "Environmental_Management",
            "Restoration"
        ],

        "27_Current_Affairs_and_Strategic_Issues": [
            "Critical_Mineral_Missions",
            "Lithium_Discoveries",
            "Green_Hydrogen",
            "Energy_Transition",
            "Rare_Earth_Strategy",
            "International_Cooperation",
            "Recent_Policy_Changes",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Mineral_Distribution_Maps",
            "Coalfield_Maps",
            "Oilfield_Maps",
            "Power_Project_Maps",
            "Energy_Data",
            "Map_Based_Questions",
            "PYQ_Themes",
            "Assertion_Reason_Topics"
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

    print(f"Creating Mineral and Energy Resources structure in: {target_base}")
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
    create_mineral_and_energy_resources_structure()