import os
import shutil

def create_economic_impact_of_british_rule_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "economic-impact-of-british-rule")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Pre_Colonial_Indian_Economy": [
            "Agrarian_Structure",
            "Village_Economy",
            "Handicraft_Industries",
            "Textile_Production",
            "Internal_Trade",
            "Overseas_Trade",
            "Guild_System",
            "Economic_Prosperity"
        ],

        "02_Colonial_Economic_Framework": [
            "Mercantilism",
            "Colonialism",
            "Economic_Objectives_of_Britain",
            "Company_to_Crown_Transition",
            "Economic_Administration",
            "Resource_Extraction",
            "Imperial_Priorities",
            "Nature_of_Colonial_Economy"
        ],

        "03_Land_Revenue_Policies": [
            "Permanent_Settlement",
            "Ryotwari_System",
            "Mahalwari_System",
            "Revenue_Assessment",
            "Land_Ownership_Changes",
            "Revenue_Collection",
            "Colonial_Objectives",
            "Comparative_Analysis"
        ],

        "04_Agrarian_Transformation": [
            "Commercialization_of_Agriculture",
            "Cash_Crops",
            "Indigo_Cultivation",
            "Opium_Cultivation",
            "Plantation_Economy",
            "Agricultural_Specialization",
            "Changing_Cropping_Patterns",
            "Rural_Consequences"
        ],

        "05_Peasant_Economy_and_Rural_Distress": [
            "Peasant_Indebtedness",
            "Moneylenders",
            "Land_Alienation",
            "Rural_Poverty",
            "Tenant_Problems",
            "Agrarian_Crisis",
            "Peasant_Vulnerability",
            "Economic_Hardships"
        ],

        "06_Traditional_Industries": [
            "Indian_Textiles",
            "Handloom_Industry",
            "Metal_Industries",
            "Artisan_Production",
            "Craft_Organization",
            "Regional_Industries",
            "Employment_Patterns",
            "Industrial_Structure"
        ],

        "07_Deindustrialization": [
            "Decline_of_Handicrafts",
            "Machine_Made_Imports",
            "Collapse_of_Textiles",
            "Artisan_Displacement",
            "Loss_of_Employment",
            "Industrial_Decay",
            "Economic_Consequences",
            "Historical_Debates"
        ],

        "08_Trade_Policies": [
            "Free_Trade_Policy",
            "Tariff_Policies",
            "Export_Orientation",
            "Import_Patterns",
            "Trade_Imbalance",
            "British_Commercial_Interests",
            "Colonial_Market_System",
            "Economic_Consequences"
        ],

        "09_Foreign_Trade_and_Commerce": [
            "Export_Commodities",
            "Import_Commodities",
            "Port_Cities",
            "Trade_Networks",
            "Shipping",
            "Commercial_Integration",
            "Global_Economic_Links",
            "Trade_Expansion"
        ],

        "10_Drain_of_Wealth_Theory": [
            "Dadabhai_Naoroji",
            "Home_Charges",
            "Unrequited_Exports",
            "Remittances",
            "Economic_Drain",
            "Nationalist_Critique",
            "Drain_Mechanisms",
            "Historical_Assessment"
        ],

        "11_Nationalist_Economic_Critics": [
            "Dadabhai_Naoroji",
            "R_C_Dutt",
            "M_G_Ranade",
            "G_V_Joshi",
            "Economic_Nationalism",
            "Colonial_Criticism",
            "Economic_Writings",
            "Influence_on_Nationalism"
        ],

        "12_Modern_Industries": [
            "Cotton_Textile_Industry",
            "Jute_Industry",
            "Coal_Mining",
            "Iron_and_Steel",
            "Tea_Industry",
            "Industrial_Entrepreneurs",
            "Industrial_Growth",
            "Limitations"
        ],

        "13_Indian_Entrepreneurship": [
            "Parsi_Entrepreneurs",
            "Marwari_Businesses",
            "Tata_Group",
            "Birla_Group",
            "Indigenous_Capital",
            "Industrial_Investment",
            "Business_Communities",
            "Economic_Contribution"
        ],

        "14_Railways": [
            "Railway_Policy",
            "Guaranteed_System",
            "Railway_Expansion",
            "Freight_Movement",
            "Market_Integration",
            "Colonial_Objectives",
            "Economic_Impact",
            "Historical_Debates"
        ],

        "15_Transport_and_Communication": [
            "Roads",
            "Canals",
            "Ports",
            "Telegraph",
            "Postal_System",
            "Communication_Networks",
            "Administrative_Control",
            "Economic_Integration"
        ],

        "16_Finance_and_Banking": [
            "Presidency_Banks",
            "Paper_Currency",
            "Exchange_Rate_Policies",
            "Imperial_Bank",
            "Credit_Structure",
            "Financial_Institutions",
            "Colonial_Finances",
            "Banking_Development"
        ],

        "17_Fiscal_and_Monetary_Policies": [
            "Taxation",
            "Public_Debt",
            "Currency_System",
            "Silver_and_Gold_Standards",
            "Budgetary_Policies",
            "Government_Expenditure",
            "Fiscal_Control",
            "Economic_Implications"
        ],

        "18_Famines_and_Food_Security": [
            "Major_Famines",
            "Causes_of_Famines",
            "Famine_Commissions",
            "Government_Response",
            "Food_Exports",
            "Mortality",
            "Economic_Consequences",
            "Historical_Debates"
        ],

        "19_Labour_and_Working_Class": [
            "Industrial_Workers",
            "Plantation_Labour",
            "Migrant_Labour",
            "Working_Conditions",
            "Wages",
            "Labour_Organization",
            "Labour_Legislation",
            "Social_Consequences"
        ],

        "20_Urbanization_and_Cities": [
            "Colonial_Cities",
            "Port_Cities",
            "Industrial_Towns",
            "Municipal_Development",
            "Urban_Economy",
            "Migration",
            "Changing_Urban_Society",
            "Economic_Role"
        ],

        "21_Forest_Policies_and_Resources": [
            "Forest_Acts",
            "Commercial_Forestry",
            "Timber_Extraction",
            "Impact_on_Tribal_Economy",
            "Resource_Management",
            "Environmental_Consequences",
            "Colonial_Interests",
            "Economic_Impact"
        ],

        "22_Tribal_Economy_and_Colonialism": [
            "Traditional_Tribal_Economy",
            "Forest_Restrictions",
            "Land_Alienation",
            "Commercial_Penetration",
            "Labour_Exploitation",
            "Economic_Displacement",
            "Resistance",
            "Long_Term_Impact"
        ],

        "23_Economic_Impact_on_Different_Classes": [
            "Peasants",
            "Landlords",
            "Artisans",
            "Merchants",
            "Industrialists",
            "Workers",
            "Tribal_Communities",
            "Comparative_Impact"
        ],

        "24_Economic_Impact_and_Nationalism": [
            "Economic_Nationalism",
            "Swadeshi_Economics",
            "Protectionism",
            "Industrial_Development_Demands",
            "Economic_Grievances",
            "Political_Mobilization",
            "Congress_Economic_Demands",
            "Nationalist_Programme"
        ],

        "25_Economic_Historiography": [
            "Nationalist_Interpretation",
            "Imperialist_Interpretation",
            "Marxist_View",
            "Cambridge_School",
            "Dependency_Theory",
            "Revisionist_Views",
            "Recent_Scholarship",
            "Comparative_Debates"
        ],

        "26_Economic_Statistics_and_Data": [
            "National_Income_Estimates",
            "Agricultural_Data",
            "Trade_Statistics",
            "Industrial_Data",
            "Population_and_Economy",
            "Price_Trends",
            "Revenue_Data",
            "Use_of_Statistics"
        ],

        "27_Sources": [
            "Government_Reports",
            "Famine_Commission_Reports",
            "Economic_Surveys",
            "Nationalist_Writings",
            "Parliamentary_Papers",
            "Business_Records",
            "Contemporary_Accounts",
            "Source_Criticism"
        ],

        "28_Legacy_and_Historical_Significance": [
            "Colonial_Underdevelopment",
            "Infrastructure_Legacy",
            "Industrial_Foundations",
            "Agrarian_Legacy",
            "Regional_Disparities",
            "Economic_Nationalism",
            "Post_Independence_Challenges",
            "Contemporary_Relevance"
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

    print(f"Creating Economic Impact of British Rule structure in: {target_base}")
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
    create_economic_impact_of_british_rule_structure()