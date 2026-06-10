import os
import shutil

def create_money_and_banking_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "money-and-banking"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Money_Fundamentals": [
            "Meaning_of_Money",
            "Functions_of_Money",
            "Characteristics_of_Money",
            "Evolution_of_Money",
            "Barter_System",
            "Money_Economy",
            "Importance_of_Money",
            "Types_of_Money"
        ],

        "02_Concepts_of_Money_Supply": [
            "Money_Supply",
            "Reserve_Money",
            "High_Powered_Money",
            "Broad_Money",
            "Narrow_Money",
            "Liquidity",
            "Money_Multiplier",
            "Monetary_Aggregates"
        ],

        "03_Currency_System_in_India": [
            "Indian_Rupee",
            "Legal_Tender",
            "Currency_Management",
            "Currency_Notes",
            "Coins",
            "Security_Features",
            "Currency_Printing",
            "Currency_Circulation"
        ],

        "04_Banking_Fundamentals": [
            "Meaning_of_Banking",
            "Banking_Functions",
            "Financial_Intermediation",
            "Deposit_Mobilization",
            "Credit_Creation",
            "Banking_System",
            "Banking_History",
            "Role_in_Economy"
        ],

        "05_History_of_Banking_in_India": [
            "Presidency_Banks",
            "Imperial_Bank",
            "State_Bank_of_India",
            "Banking_Development",
            "Nationalization_Background",
            "Post_Independence_Banking",
            "Reforms_History",
            "Major_Milestones"
        ],

        "06_Commercial_Banks": [
            "Public_Sector_Banks",
            "Private_Sector_Banks",
            "Foreign_Banks",
            "Scheduled_Banks",
            "Non_Scheduled_Banks",
            "Branch_Network",
            "Banking_Operations",
            "Role_in_Credit"
        ],

        "07_Bank_Nationalization": [
            "1969_Nationalization",
            "1980_Nationalization",
            "Objectives",
            "Expansion_of_Banking",
            "Financial_Inclusion",
            "Rural_Banking",
            "Achievements",
            "Limitations"
        ],

        "08_Deposit_Accounts": [
            "Savings_Account",
            "Current_Account",
            "Fixed_Deposit",
            "Recurring_Deposit",
            "Term_Deposits",
            "Deposit_Insurance",
            "Interest_Rates",
            "Account_Features"
        ],

        "09_Lending_and_Credit": [
            "Loans_and_Advances",
            "Cash_Credit",
            "Overdraft",
            "Term_Loans",
            "Retail_Lending",
            "Corporate_Lending",
            "Priority_Sector_Lending",
            "Credit_Appraisal"
        ],

        "10_Credit_Creation_by_Banks": [
            "Credit_Creation_Process",
            "Primary_Deposits",
            "Derivative_Deposits",
            "Money_Multiplier_Process",
            "Reserve_Ratio",
            "Excess_Reserves",
            "Limitations_of_Credit_Creation",
            "Economic_Impact"
        ],

        "11_Cooperative_Banking": [
            "Cooperative_Banks",
            "Urban_Cooperative_Banks",
            "Rural_Cooperative_Credit",
            "State_Cooperative_Banks",
            "District_Central_Banks",
            "Primary_Credit_Societies",
            "Structure",
            "Challenges"
        ],

        "12_Regional_Rural_Banks": [
            "RRB_Formation",
            "Objectives",
            "Ownership_Pattern",
            "Rural_Credit",
            "Financial_Inclusion",
            "Reforms",
            "Amalgamation",
            "Current_Status"
        ],

        "13_Development_Financial_Institutions": [
            "NABARD",
            "SIDBI",
            "EXIM_Bank",
            "NHB",
            "Development_Finance",
            "Sectoral_Financing",
            "Promotional_Role",
            "Institutional_Support"
        ],

        "14_Financial_Inclusion": [
            "Financial_Inclusion_Concept",
            "Jan_Dhan_Yojana",
            "Basic_Savings_Accounts",
            "Banking_Access",
            "Digital_Access",
            "Inclusive_Finance",
            "Financial_Literacy",
            "Challenges"
        ],

        "15_Payment_Banks_and_Small_Finance_Banks": [
            "Payment_Banks",
            "Small_Finance_Banks",
            "Differentiated_Banking",
            "Licensing_Framework",
            "Target_Groups",
            "Business_Model",
            "Financial_Inclusion_Role",
            "Challenges"
        ],

        "16_Digital_Banking": [
            "Internet_Banking",
            "Mobile_Banking",
            "Digital_Payments",
            "Banking_Apps",
            "Online_Transactions",
            "Customer_Services",
            "FinTech_Integration",
            "Digital_Transformation"
        ],

        "17_Payment_Systems": [
            "UPI",
            "NEFT",
            "RTGS",
            "IMPS",
            "BHIM",
            "Payment_Gateways",
            "NPCI",
            "Payment_Infrastructure"
        ],

        "18_Banking_Technology": [
            "Core_Banking",
            "ATM_Network",
            "Micro_ATMs",
            "Aadhaar_Enabled_Payments",
            "Digital_KYC",
            "Cyber_Security",
            "FinTech",
            "Innovation"
        ],

        "19_Non_Performing_Assets": [
            "NPA_Concept",
            "Gross_NPA",
            "Net_NPA",
            "Asset_Classification",
            "Provisioning",
            "Bad_Loans",
            "Recovery_Mechanisms",
            "Economic_Impact"
        ],

        "20_Banking_Reforms": [
            "Narasimham_Committee",
            "Banking_Sector_Reforms",
            "Governance_Reforms",
            "Capital_Adequacy",
            "Consolidation",
            "PSB_Reforms",
            "Efficiency_Measures",
            "Future_Reforms"
        ],

        "21_Basel_Norms": [
            "Basel_I",
            "Basel_II",
            "Basel_III",
            "Capital_Adequacy",
            "Risk_Management",
            "Liquidity_Standards",
            "Global_Banking_Standards",
            "Indian_Implementation"
        ],

        "22_Deposit_Insurance_and_Regulation": [
            "DICGC",
            "Deposit_Insurance",
            "Banking_Regulation",
            "Customer_Protection",
            "Resolution_Framework",
            "Regulatory_Compliance",
            "Bank_Supervision",
            "Risk_Mitigation"
        ],

        "23_Banking_and_Economic_Development": [
            "Savings_Mobilization",
            "Investment_Financing",
            "Credit_and_Growth",
            "Rural_Development",
            "MSME_Financing",
            "Infrastructure_Financing",
            "Employment_Generation",
            "Economic_Impact"
        ],

        "24_Microfinance_and_SHGs": [
            "Microfinance",
            "Self_Help_Groups",
            "SHG_Bank_Linkage",
            "Women_Empowerment",
            "Micro_Credit",
            "Financial_Inclusion_Linkage",
            "Livelihood_Promotion",
            "Challenges"
        ],

        "25_FinTech_and_Innovation": [
            "Digital_Lending",
            "Peer_to_Peer_Lending",
            "Neo_Banks",
            "Blockchain_Applications",
            "Artificial_Intelligence",
            "Financial_Innovation",
            "Regulatory_Challenges",
            "Future_Trends"
        ],

        "26_Banking_Sector_Institutions": [
            "Indian_Banks_Association",
            "NPCI",
            "DICGC",
            "Bank_Boards_Bureau",
            "Credit_Information_Companies",
            "Financial_Stability_Institutions",
            "Industry_Bodies",
            "Institutional_Framework"
        ],

        "27_Current_Affairs_and_Banking_Issues": [
            "Digital_Payment_Trends",
            "Bank_Mergers",
            "Banking_Crisis_Issues",
            "Financial_Inclusion_Updates",
            "NPA_Developments",
            "FinTech_Regulations",
            "Recent_Reforms",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Banking_Statistics",
            "Financial_Inclusion_Data",
            "Credit_Growth_Data",
            "Deposit_Trends",
            "NPA_Data",
            "Committee_Reports",
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

    print(f"Creating Money and Banking structure in: {target_base}")

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
    create_money_and_banking_structure()