import os
import shutil

def create_monetary_policy_and_rbi_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
    project_root,
    "gs-question-bank",
    "economy",
    "indian-economy",
    "monetary-policy-and-rbi"
)
    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

        # Mapping of categories to their respective topics
    structure = {

        "01_Monetary_Economics_Fundamentals": [
            "Meaning_of_Monetary_Policy",
            "Objectives_of_Monetary_Policy",
            "Price_Stability",
            "Growth_Objective",
            "Employment_Objective",
            "Financial_Stability",
            "Monetary_Transmission",
            "Policy_Framework"
        ],

        "02_History_of_Central_Banking_in_India": [
            "Hilton_Young_Commission",
            "RBI_Act_1934",
            "RBI_Establishment",
            "Nationalization_of_RBI",
            "Evolution_of_Central_Banking",
            "Post_Independence_Role",
            "Financial_Reforms",
            "Modern_Central_Bank"
        ],

        "03_Reserve_Bank_of_India": [
            "Organization_Structure",
            "Central_Board",
            "Governor",
            "Deputy_Governors",
            "Departments_of_RBI",
            "Regional_Offices",
            "Autonomy_and_Accountability",
            "Institutional_Framework"
        ],

        "04_Functions_of_RBI": [
            "Banker_to_Government",
            "Bankers_Bank",
            "Currency_Authority",
            "Credit_Controller",
            "Custodian_of_Reserves",
            "Developmental_Functions",
            "Regulatory_Functions",
            "Promotional_Functions"
        ],

        "05_Monetary_Policy_Committee": [
            "MPC_Formation",
            "Composition",
            "Voting_Mechanism",
            "Inflation_Targeting",
            "Policy_Decisions",
            "Meeting_Process",
            "Transparency",
            "Accountability"
        ],

        "06_Inflation_Targeting_Framework": [
            "Flexible_Inflation_Targeting",
            "CPI_Target",
            "Tolerance_Band",
            "Policy_Objectives",
            "Monetary_Policy_Agreement",
            "Target_Failure",
            "Policy_Response",
            "International_Practices"
        ],

        "07_Quantitative_Monetary_Tools": [
            "Bank_Rate",
            "Repo_Rate",
            "Reverse_Repo_Rate",
            "MSF",
            "CRR",
            "SLR",
            "Liquidity_Adjustment_Facility",
            "Standing_Deposit_Facility"
        ],

        "08_Open_Market_Operations": [
            "OMO_Concept",
            "Government_Securities",
            "Liquidity_Management",
            "Bond_Purchases",
            "Bond_Sales",
            "Yield_Management",
            "Market_Impact",
            "Policy_Use"
        ],

        "09_Qualitative_Monetary_Tools": [
            "Moral_Suasion",
            "Credit_Rationing",
            "Margin_Requirements",
            "Selective_Credit_Control",
            "Directives",
            "Consumer_Credit_Regulation",
            "Persuasion_Mechanisms",
            "Policy_Applications"
        ],

        "10_Liquidity_Management": [
            "System_Liquidity",
            "Liquidity_Deficit",
            "Liquidity_Surplus",
            "Variable_Rate_Repo",
            "Variable_Rate_Reverse_Repo",
            "Fine_Tuning_Operations",
            "Liquidity_Forecasting",
            "Liquidity_Framework"
        ],

        "11_Monetary_Transmission": [
            "Interest_Rate_Channel",
            "Credit_Channel",
            "Exchange_Rate_Channel",
            "Asset_Price_Channel",
            "Expectations_Channel",
            "Transmission_Lags",
            "Transmission_Challenges",
            "Effectiveness"
        ],

        "12_Inflation_and_Monetary_Policy": [
            "Demand_Pull_Inflation",
            "Cost_Push_Inflation",
            "Core_Inflation",
            "Headline_Inflation",
            "Inflation_Expectations",
            "Policy_Tradeoffs",
            "Price_Stability",
            "Inflation_Control"
        ],

        "13_Credit_Policy": [
            "Credit_Growth",
            "Sectoral_Credit",
            "Priority_Credit_Linkages",
            "Credit_Regulation",
            "Lending_Conditions",
            "Macroprudential_Measures",
            "Credit_Cycles",
            "Policy_Objectives"
        ],

        "14_Forex_Management_by_RBI": [
            "Foreign_Exchange_Reserves",
            "Exchange_Rate_Management",
            "Forex_Intervention",
            "Reserve_Adequacy",
            "Currency_Stability",
            "External_Shocks",
            "Reserve_Diversification",
            "Forex_Market_Operations"
        ],

        "15_Currency_Management": [
            "Currency_Issue",
            "Clean_Note_Policy",
            "Currency_Chests",
            "Withdrawal_of_Notes",
            "Counterfeit_Detection",
            "Cash_Management",
            "Digital_Currency",
            "Currency_Circulation"
        ],

        "16_Digital_Currency_and_CBDC": [
            "CBDC_Concept",
            "Digital_Rupee",
            "Wholesale_CBDC",
            "Retail_CBDC",
            "Benefits",
            "Risks",
            "Pilot_Projects",
            "Future_Prospects"
        ],

        "17_Financial_Stability": [
            "Systemic_Risk",
            "Macroprudential_Regulation",
            "Financial_Stability_Report",
            "Stress_Testing",
            "Risk_Monitoring",
            "Contagion_Risk",
            "Crisis_Prevention",
            "Institutional_Coordination"
        ],

        "18_RBI_and_Banking_Regulation": [
            "Bank_Supervision",
            "Licensing",
            "Prompt_Corrective_Action",
            "Governance_Standards",
            "Risk_Based_Supervision",
            "Inspection_Framework",
            "Regulatory_Compliance",
            "Enforcement_Actions"
        ],

        "19_Payment_and_Settlement_Systems": [
            "Payment_Regulation",
            "Settlement_Systems",
            "RTGS_Oversight",
            "Digital_Payment_Regulation",
            "NPCI_Coordination",
            "Cyber_Security",
            "Payment_Innovation",
            "System_Stability"
        ],

        "20_Developmental_Role_of_RBI": [
            "Financial_Inclusion",
            "Rural_Credit_Promotion",
            "Institution_Building",
            "Priority_Sector_Support",
            "Financial_Literacy",
            "Development_Finance",
            "Market_Development",
            "Capacity_Building"
        ],

        "21_RBI_and_Government_Relations": [
            "Debt_Management",
            "Ways_and_Means_Advances",
            "Fiscal_Monetary_Coordination",
            "Government_Borrowing",
            "Policy_Coordination",
            "Autonomy_Issues",
            "Institutional_Balance",
            "Accountability"
        ],

        "22_Monetary_Policy_in_Crisis": [
            "Global_Financial_Crisis",
            "COVID_Response",
            "Emergency_Liquidity",
            "Special_Windows",
            "Unconventional_Policies",
            "Economic_Stabilization",
            "Lessons_Learned",
            "Future_Preparedness"
        ],

        "23_Unconventional_Monetary_Policy": [
            "Quantitative_Easing",
            "Operation_Twist",
            "Yield_Curve_Management",
            "Long_Term_Repo_Operations",
            "Targeted_LTRO",
            "Liquidity_Injections",
            "Global_Experiences",
            "Indian_Applications"
        ],

        "24_Monetary_Policy_and_Growth": [
            "Growth_Inflation_Tradeoff",
            "Investment_Impact",
            "Consumption_Impact",
            "Employment_Linkages",
            "Business_Cycles",
            "Economic_Recovery",
            "Policy_Coordination",
            "Long_Term_Growth"
        ],

        "25_International_Central_Banking": [
            "US_Federal_Reserve",
            "European_Central_Bank",
            "Bank_of_England",
            "Bank_of_Japan",
            "Central_Bank_Comparisons",
            "Policy_Frameworks",
            "Global_Trends",
            "Lessons_for_India"
        ],

        "26_Committees_and_Reforms": [
            "Urjit_Patel_Committee",
            "Narasimham_Committee",
            "Financial_Sector_Reforms",
            "Monetary_Reforms",
            "Regulatory_Changes",
            "Expert_Recommendations",
            "Implementation_Status",
            "Future_Reforms"
        ],

        "27_Current_Affairs_and_RBI_Updates": [
            "Latest_MPC_Decisions",
            "Repo_Rate_Changes",
            "Inflation_Trends",
            "Digital_Rupee_Updates",
            "RBI_Reports",
            "Financial_Stability_Issues",
            "Recent_Circulars",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Monetary_Policy_Report",
            "Financial_Stability_Report",
            "Annual_Report",
            "Inflation_Data",
            "Liquidity_Data",
            "Forex_Reserve_Data",
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

    print(f"Creating Monetary Policy and RBI structure in: {target_base}")

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
    create_monetary_policy_and_rbi_structure()