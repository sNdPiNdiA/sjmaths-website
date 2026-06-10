import os
import shutil

def create_foreign_trade_and_bop_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "foreign-trade-and-bop"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_International_Trade_Fundamentals": [
            "Meaning_of_International_Trade",
            "Need_for_Trade",
            "Domestic_vs_International_Trade",
            "Trade_Specialization",
            "Trade_Gains",
            "Trade_Patterns",
            "Trade_Flows",
            "Importance_for_India"
        ],

        "02_Theories_of_International_Trade": [
            "Absolute_Advantage",
            "Comparative_Advantage",
            "Heckscher_Ohlin_Theory",
            "Factor_Endowment",
            "Opportunity_Cost_Theory",
            "New_Trade_Theory",
            "Product_Cycle_Theory",
            "Theory_Applications"
        ],

        "03_India_External_Sector_Overview": [
            "External_Sector_Concept",
            "Trade_Openness",
            "Global_Integration",
            "External_Competitiveness",
            "Trade_Indicators",
            "Export_Orientation",
            "Import_Dependency",
            "Sectoral_Profile"
        ],

        "04_Exports_of_India": [
            "Merchandise_Exports",
            "Services_Exports",
            "Engineering_Goods",
            "Petroleum_Products",
            "Pharmaceutical_Exports",
            "Agricultural_Exports",
            "IT_Exports",
            "Export_Trends"
        ],

        "05_Imports_of_India": [
            "Crude_Oil_Imports",
            "Gold_Imports",
            "Electronics_Imports",
            "Capital_Goods_Imports",
            "Defense_Imports",
            "Industrial_Inputs",
            "Import_Composition",
            "Import_Trends"
        ],

        "06_Trade_Policy_of_India": [
            "Foreign_Trade_Policy",
            "Export_Promotion",
            "Import_Regulation",
            "Trade_Facilitation",
            "Trade_Competitiveness",
            "Market_Diversification",
            "Trade_Targets",
            "Policy_Evolution"
        ],

        "07_Export_Promotion_Institutions": [
            "DGFT",
            "Export_Promotion_Councils",
            "Commodity_Boards",
            "Export_Houses",
            "Trade_Promotion_Organizations",
            "Export_Assistance",
            "Institutional_Framework",
            "Capacity_Building"
        ],

        "08_Special_Economic_Zones": [
            "SEZ_Concept",
            "SEZ_Act",
            "Export_Processing_Zones",
            "Investment_Promotion",
            "Infrastructure_Benefits",
            "Export_Generation",
            "SEZ_Performance",
            "Policy_Challenges"
        ],

        "09_Free_Trade_Agreements": [
            "FTA_Concept",
            "Bilateral_Agreements",
            "Regional_Agreements",
            "Tariff_Reduction",
            "Market_Access",
            "Trade_Negotiations",
            "Economic_Integration",
            "FTA_Assessment"
        ],

        "10_Regional_Trade_Blocks": [
            "ASEAN",
            "EU",
            "RCEP",
            "SAFTA",
            "APEC",
            "Regionalism",
            "Trade_Cooperation",
            "India_Relations"
        ],

        "11_World_Trade_Organization": [
            "WTO_Formation",
            "WTO_Functions",
            "Trade_Rules",
            "Dispute_Settlement",
            "Ministerial_Conferences",
            "Trade_Negotiations",
            "India_and_WTO",
            "Current_Challenges"
        ],

        "12_Tariffs_and_Non_Tariff_Barriers": [
            "Tariff_Barriers",
            "Import_Duties",
            "Quotas",
            "Subsidies_in_Trade",
            "Technical_Barriers",
            "Sanitary_Standards",
            "Protectionism",
            "Trade_Restrictions"
        ],

        "13_Balance_of_Payments_Fundamentals": [
            "BoP_Concept",
            "BoP_Structure",
            "Double_Entry_System",
            "External_Transactions",
            "BoP_Accounting",
            "Surplus_and_Deficit",
            "Economic_Significance",
            "Indicators"
        ],

        "14_Current_Account": [
            "Trade_Balance",
            "Services_Balance",
            "Primary_Income",
            "Secondary_Income",
            "Current_Transfers",
            "Remittances",
            "Current_Account_Deficit",
            "Current_Account_Surplus"
        ],

        "15_Capital_Account": [
            "Capital_Transfers",
            "Capital_Flows",
            "External_Assets",
            "External_Liabilities",
            "Investment_Flows",
            "Capital_Transactions",
            "Capital_Mobility",
            "Capital_Account_Analysis"
        ],

        "16_Financial_Account": [
            "Foreign_Direct_Investment",
            "Foreign_Portfolio_Investment",
            "External_Commercial_Borrowings",
            "NRI_Deposits",
            "Banking_Capital",
            "Reserve_Assets",
            "Financial_Flows",
            "Investment_Trends"
        ],

        "17_Current_Account_Deficit": [
            "CAD_Concept",
            "Causes_of_CAD",
            "CAD_Financing",
            "External_Vulnerability",
            "Trade_Imbalances",
            "Policy_Responses",
            "CAD_Trends",
            "Economic_Impact"
        ],

        "18_Foreign_Exchange_Market": [
            "Forex_Market_Concept",
            "Currency_Trading",
            "Exchange_Rate_System",
            "Forex_Participants",
            "Spot_Market",
            "Forward_Market",
            "Forex_Operations",
            "Market_Dynamics"
        ],

        "19_Exchange_Rate_Mechanism": [
            "Fixed_Exchange_Rate",
            "Floating_Exchange_Rate",
            "Managed_Float",
            "Currency_Appreciation",
            "Currency_Depreciation",
            "Exchange_Rate_Determination",
            "External_Competitiveness",
            "Policy_Issues"
        ],

        "20_Foreign_Exchange_Reserves": [
            "Reserve_Components",
            "Reserve_Adequacy",
            "Gold_Reserves",
            "SDRs",
            "Reserve_Tranche_Position",
            "Reserve_Management",
            "Strategic_Importance",
            "Reserve_Trends"
        ],

        "21_Foreign_Direct_Investment": [
            "FDI_Concept",
            "Greenfield_Investment",
            "Brownfield_Investment",
            "FDI_Policy",
            "Sectoral_Limits",
            "Investment_Promotion",
            "Economic_Impact",
            "FDI_Trends"
        ],

        "22_External_Debt": [
            "External_Debt_Concept",
            "Sovereign_Debt",
            "Commercial_Borrowings",
            "Debt_Indicators",
            "Debt_Sustainability",
            "Debt_Service_Ratio",
            "External_Vulnerability",
            "Debt_Trends"
        ],

        "23_Remittances_and_Diaspora": [
            "Worker_Remittances",
            "NRI_Contributions",
            "Diaspora_Economics",
            "Foreign_Earnings",
            "Remittance_Flows",
            "Economic_Impact",
            "Global_Migration",
            "Trends"
        ],

        "24_Trade_Logistics_and_Connectivity": [
            "Port_Infrastructure",
            "Shipping",
            "Logistics_Performance",
            "Trade_Corridors",
            "Supply_Chains",
            "Export_Connectivity",
            "Trade_Costs",
            "Infrastructure_Development"
        ],

        "25_Export_Competitiveness": [
            "Productivity",
            "Quality_Standards",
            "Innovation",
            "Market_Diversification",
            "Global_Value_Chains",
            "Brand_India",
            "Competitiveness_Indicators",
            "Export_Strategy"
        ],

        "26_Trade_and_Geopolitics": [
            "Trade_Wars",
            "Economic_Sanctions",
            "Supply_Chain_Resilience",
            "Strategic_Trade",
            "Energy_Trade",
            "Geopolitical_Risks",
            "Global_Power_Shifts",
            "India_Strategy"
        ],

        "27_Current_Affairs_and_External_Sector": [
            "Trade_Deficit_Trends",
            "FTA_Developments",
            "WTO_Issues",
            "FDI_Updates",
            "Forex_Reserve_Changes",
            "Export_Performance",
            "Global_Trade_Events",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Trade_Statistics",
            "BoP_Data",
            "FDI_Data",
            "Forex_Data",
            "Export_Import_Data",
            "Economic_Survey_External_Sector",
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

    print(f"Creating Foreign Trade and Balance of Payments structure in: {target_base}")

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
    create_foreign_trade_and_bop_structure()