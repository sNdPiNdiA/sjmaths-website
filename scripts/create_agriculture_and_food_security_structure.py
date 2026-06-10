import os
import shutil

def create_agriculture_and_food_security_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "agriculture-and-food-security"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Agriculture_Fundamentals": [
            "Meaning_of_Agriculture",
            "Role_in_Indian_Economy",
            "Agricultural_Seasons",
            "Cropping_Patterns",
            "Agricultural_Regions",
            "Agricultural_Statistics",
            "Contribution_to_GDP",
            "Employment_Structure"
        ],

        "02_History_of_Indian_Agriculture": [
            "Pre_Green_Revolution",
            "Green_Revolution",
            "Evergreen_Revolution",
            "White_Revolution",
            "Yellow_Revolution",
            "Blue_Revolution",
            "Post_Reform_Agriculture",
            "Recent_Trends"
        ],

        "03_Land_Resources_and_Holdings": [
            "Land_Utilization",
            "Operational_Holdings",
            "Marginal_Farmers",
            "Small_Farmers",
            "Land_Reforms",
            "Tenancy_Reforms",
            "Consolidation_of_Holdings",
            "Land_Record_Modernization"
        ],

        "04_Soil_and_Agricultural_Inputs": [
            "Soil_Health",
            "Soil_Health_Card",
            "Fertilizers",
            "Bio_Fertilizers",
            "Pesticides",
            "Integrated_Nutrient_Management",
            "Seed_Quality",
            "Input_Efficiency"
        ],

        "05_Irrigation_and_Water_Management": [
            "Major_Irrigation",
            "Minor_Irrigation",
            "Canal_Irrigation",
            "Groundwater_Irrigation",
            "Drip_Irrigation",
            "Sprinkler_Irrigation",
            "PMKSY",
            "Water_Use_Efficiency"
        ],

        "06_Agricultural_Credit": [
            "Institutional_Credit",
            "Cooperative_Credit",
            "Commercial_Banks",
            "Regional_Rural_Banks",
            "Kisan_Credit_Card",
            "NABARD",
            "Interest_Subvention",
            "Credit_Challenges"
        ],

        "07_Agricultural_Insurance": [
            "Crop_Insurance",
            "PMFBY",
            "Weather_Based_Insurance",
            "Yield_Based_Insurance",
            "Claim_Settlement",
            "Risk_Management",
            "Insurance_Coverage",
            "Challenges"
        ],

        "08_Agricultural_Marketing": [
            "APMC",
            "Agricultural_Markets",
            "Market_Reforms",
            "Direct_Marketing",
            "Contract_Farming",
            "Farmer_Producer_Organizations",
            "National_Agriculture_Market",
            "Price_Discovery"
        ],

        "09_Minimum_Support_Price": [
            "MSP_Concept",
            "CACP",
            "Procurement_System",
            "MSP_Crops",
            "Price_Support",
            "Farmer_Income",
            "Regional_Imbalances",
            "Debates_and_Reforms"
        ],

        "10_Food_Grains_Production": [
            "Rice",
            "Wheat",
            "Coarse_Cereals",
            "Millets",
            "Pulses",
            "Production_Trends",
            "Yield_Levels",
            "Foodgrain_Security"
        ],

        "11_Commercial_Crops": [
            "Cotton",
            "Sugarcane",
            "Jute",
            "Tobacco",
            "Oilseeds",
            "Plantation_Crops",
            "Export_Crops",
            "Production_Challenges"
        ],

        "12_Horticulture": [
            "Fruits",
            "Vegetables",
            "Spices",
            "Flowers",
            "Medicinal_Plants",
            "Protected_Cultivation",
            "Horticulture_Missions",
            "Export_Potential"
        ],

        "13_Dairy_Sector": [
            "Milk_Production",
            "Operation_Flood",
            "Cooperative_Model",
            "Dairy_Infrastructure",
            "Breed_Improvement",
            "Animal_Health",
            "Value_Addition",
            "Export_Potential"
        ],

        "14_Livestock_Sector": [
            "Cattle",
            "Buffalo",
            "Sheep",
            "Goat",
            "Poultry",
            "Pig_Farming",
            "Livestock_Economy",
            "Sector_Challenges"
        ],

        "15_Fisheries_and_Aquaculture": [
            "Marine_Fisheries",
            "Inland_Fisheries",
            "Aquaculture",
            "Blue_Revolution",
            "Fish_Production",
            "Fish_Exports",
            "PMMSY",
            "Sustainable_Fisheries"
        ],

        "16_Food_Processing": [
            "Food_Processing_Industry",
            "Mega_Food_Parks",
            "Cold_Chain",
            "Value_Addition",
            "Agri_Logistics",
            "Food_Exports",
            "Processing_Levels",
            "Government_Schemes"
        ],

        "17_Storage_and_Warehousing": [
            "FCI",
            "Warehousing",
            "Cold_Storage",
            "Buffer_Stocks",
            "Food_Storage",
            "Supply_Chain",
            "Storage_Losses",
            "Infrastructure_Gaps"
        ],

        "18_Public_Distribution_System": [
            "PDS",
            "TPDS",
            "NFSA",
            "Food_Subsidy",
            "Beneficiary_Coverage",
            "One_Nation_One_Ration_Card",
            "Leakages",
            "Reforms"
        ],

        "19_Food_Security_Concepts": [
            "Availability",
            "Accessibility",
            "Affordability",
            "Nutrition",
            "Food_Security_Index",
            "Household_Food_Security",
            "Global_Food_Security",
            "Food_Security_Challenges"
        ],

        "20_Nutrition_and_Malnutrition": [
            "Undernutrition",
            "Stunting",
            "Wasting",
            "Anemia",
            "Micronutrient_Deficiency",
            "Poshan_Abhiyaan",
            "Mid_Day_Meal",
            "Nutrition_Indicators"
        ],

        "21_Agricultural_Trade": [
            "Agri_Exports",
            "Agri_Imports",
            "Export_Policy",
            "WTO_Agreement_on_Agriculture",
            "Export_Incentives",
            "Sanitary_Standards",
            "Global_Competitiveness",
            "Trade_Challenges"
        ],

        "22_Agricultural_Subsidies": [
            "Fertilizer_Subsidy",
            "Food_Subsidy",
            "Power_Subsidy",
            "Irrigation_Subsidy",
            "Input_Subsidies",
            "WTO_Issues",
            "Fiscal_Burden",
            "Reform_Proposals"
        ],

        "23_Agricultural_Technology": [
            "Mechanization",
            "Precision_Farming",
            "Digital_Agriculture",
            "Drones_in_Agriculture",
            "AI_in_Agriculture",
            "Farm_Advisory",
            "Agri_Startups",
            "Innovation_Ecosystem"
        ],

        "24_Biotechnology_and_GM_Crops": [
            "GM_Crops",
            "Bt_Cotton",
            "Gene_Editing",
            "Biofortification",
            "Regulatory_Framework",
            "Biosafety",
            "Research_Institutions",
            "Policy_Debates"
        ],

        "25_Climate_Change_and_Agriculture": [
            "Climate_Risk",
            "Drought",
            "Floods",
            "Heat_Stress",
            "Climate_Smart_Agriculture",
            "Adaptation_Strategies",
            "Crop_Resilience",
            "Sustainability"
        ],

        "26_Government_Schemes": [
            "PM_KISAN",
            "PMFBY",
            "PMKSY",
            "eNAM",
            "PMMSY",
            "Agriculture_Infrastructure_Fund",
            "National_Food_Security_Mission",
            "Recent_Initiatives"
        ],

        "27_Current_Affairs_and_Policy_Issues": [
            "MSP_Debate",
            "Food_Inflation",
            "Farmer_Income",
            "Agricultural_Reforms",
            "Global_Food_Crisis",
            "Supply_Chain_Disruptions",
            "Recent_Committee_Reports",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Crop_Distribution_Maps",
            "Irrigation_Maps",
            "Foodgrain_Data",
            "Agricultural_Statistics",
            "Production_Trends",
            "Statewise_Rankings",
            "PYQ_Themes",
            "Assertion_Reason_Topics"
        ]

            # PASTE THE COMPLETE 28-CATEGORY STRUCTURE
            # I PROVIDED IN THE PREVIOUS MESSAGE HERE

        }

    # Standard dataset files for every leaf folder
    leaf_files: list[str] = [
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
        "map_based.json",
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
        "pyq_teaching.json",
        "interview.json",
        "flashcards.json",
        "revision_questions.json",
        "concept_traps.json",
        "common_mistakes.json",
        "memory_hooks.json"
    ]

    print(f"Creating Agriculture and Food Security structure in: {target_base}")

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
    create_agriculture_and_food_security_structure()