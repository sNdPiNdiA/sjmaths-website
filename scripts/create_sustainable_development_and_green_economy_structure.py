import os
import shutil

def create_sustainable_development_and_green_economy_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "sustainable-development-and-green-economy"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Sustainable_Development_Fundamentals": [
            "Meaning_of_Sustainable_Development",
            "Evolution_of_Sustainable_Development",
            "Brundtland_Commission",
            "Brundtland_Report",
            "Principles_of_Sustainability",
            "Three_Pillars_of_Sustainability",
            "Intergenerational_Equity",
            "Intragenerational_Equity"
        ],

        "02_History_of_Sustainable_Development": [
            "Stockholm_Conference_1972",
            "World_Conservation_Strategy",
            "Brundtland_Report_1987",
            "Rio_Earth_Summit_1992",
            "Johannesburg_Summit_2002",
            "Rio_Plus_20",
            "Agenda_21",
            "Global_Evolution"
        ],

        "03_Principles_of_Sustainable_Development": [
            "Precautionary_Principle",
            "Polluter_Pays_Principle",
            "Public_Trust_Doctrine",
            "Sustainable_Use",
            "Carrying_Capacity",
            "Resource_Efficiency",
            "Environmental_Justice",
            "Equity_Principles"
        ],

        "04_Sustainable_Development_Goals": [
            "Background_of_SDGs",
            "Structure_of_SDGs",
            "SDG_1_No_Poverty",
            "SDG_2_Zero_Hunger",
            "SDG_3_Good_Health",
            "SDG_4_Quality_Education",
            "SDG_5_Gender_Equality",
            "SDG_Framework"
        ],

        "05_Environment_Related_SDGs": [
            "SDG_6_Clean_Water",
            "SDG_7_Clean_Energy",
            "SDG_11_Sustainable_Cities",
            "SDG_12_Responsible_Consumption",
            "SDG_13_Climate_Action",
            "SDG_14_Life_Below_Water",
            "SDG_15_Life_on_Land",
            "Environmental_Targets"
        ],

        "06_SDG_Implementation_in_India": [
            "NITI_Aayog_and_SDGs",
            "SDG_India_Index",
            "State_SDG_Performance",
            "Localization_of_SDGs",
            "Monitoring_Framework",
            "Government_Programmes",
            "Challenges",
            "Recent_Progress"
        ],

        "07_Green_Economy": [
            "Meaning_of_Green_Economy",
            "Objectives_of_Green_Economy",
            "Resource_Efficiency",
            "Low_Carbon_Development",
            "Inclusive_Growth",
            "Green_Investment",
            "Green_Jobs",
            "Green_Transition"
        ],

        "08_Circular_Economy": [
            "Meaning_of_Circular_Economy",
            "Linear_vs_Circular_Model",
            "Reduce",
            "Reuse",
            "Recycle",
            "Resource_Recovery",
            "Industrial_Symbiosis",
            "Circular_Business_Models"
        ],

        "09_Blue_Economy": [
            "Meaning_of_Blue_Economy",
            "Marine_Resources",
            "Ocean_Governance",
            "Fisheries",
            "Coastal_Economy",
            "Marine_Biodiversity",
            "Blue_Growth",
            "India_Blue_Economy"
        ],

        "10_Bioeconomy": [
            "Meaning_of_Bioeconomy",
            "Biological_Resources",
            "Biotechnology_Applications",
            "Bio_Industries",
            "Bio_Innovation",
            "Bio_Based_Products",
            "Sustainable_Production",
            "India_Bioeconomy"
        ],

        "11_Green_Growth": [
            "Meaning_of_Green_Growth",
            "Economic_Growth_and_Environment",
            "Resource_Productivity",
            "Green_Infrastructure",
            "Sustainable_Investment",
            "Policy_Framework",
            "International_Experiences",
            "India_Green_Growth"
        ],

        "12_Green_Finance": [
            "Meaning_of_Green_Finance",
            "Green_Bonds",
            "Climate_Finance",
            "Sustainable_Finance",
            "ESG_Finance",
            "Green_Banking",
            "Green_Investment_Funds",
            "India_Green_Finance"
        ],

        "13_ESG_Framework": [
            "Environmental_Criteria",
            "Social_Criteria",
            "Governance_Criteria",
            "ESG_Ratings",
            "Corporate_Sustainability",
            "Disclosure_Frameworks",
            "Responsible_Investment",
            "ESG_Challenges"
        ],

        "14_Natural_Capital_and_Ecosystem_Valuation": [
            "Natural_Capital",
            "Ecosystem_Services_Valuation",
            "Environmental_Accounting",
            "Green_GDP",
            "Natural_Resource_Accounting",
            "Wealth_Accounting",
            "Economic_Valuation",
            "Policy_Applications"
        ],

        "15_Sustainable_Consumption_and_Production": [
            "Resource_Efficiency",
            "Sustainable_Lifestyles",
            "Waste_Minimization",
            "Responsible_Consumption",
            "Cleaner_Production",
            "Eco_Labels",
            "Life_Cycle_Assessment",
            "Consumer_Awareness"
        ],

        "16_Energy_Transition": [
            "Renewable_Energy",
            "Energy_Efficiency",
            "Decarbonization",
            "Clean_Technologies",
            "Hydrogen_Economy",
            "Net_Zero_Pathways",
            "Energy_Security",
            "Transition_Challenges"
        ],

        "17_LiFE_and_Behavioural_Change": [
            "Mission_LiFE",
            "Sustainable_Lifestyles",
            "Behavioural_Change",
            "Resource_Conservation",
            "Citizen_Participation",
            "Climate_Responsibility",
            "Global_Outreach",
            "India_Initiatives"
        ],

        "18_Sustainable_Urban_Development": [
            "Smart_Cities",
            "Sustainable_Cities",
            "Urban_Transport",
            "Green_Buildings",
            "Urban_Resilience",
            "Waste_Management",
            "Water_Security",
            "Urban_Planning"
        ],

        "19_Sustainable_Agriculture_and_Rural_Development": [
            "Sustainable_Agriculture",
            "Organic_Farming",
            "Climate_Smart_Agriculture",
            "Agroecology",
            "Rural_Livelihoods",
            "Soil_Health",
            "Water_Use_Efficiency",
            "Sustainable_Rural_Development"
        ],

        "20_Current_Affairs_and_Sustainability": [
            "Recent_SDG_Reports",
            "Green_Growth_Developments",
            "Green_Finance_Updates",
            "Climate_Finance_Developments",
            "LiFE_Updates",
            "ESG_Trends",
            "Global_Sustainability_Reports",
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

    print(f"Creating Sustainable Development and Green Economy structure in: {target_base}")

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
    create_sustainable_development_and_green_economy_structure()