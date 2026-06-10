import os
import shutil

def create_public_finance_and_budget_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "public-finance-and-budget"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Public_Finance_Fundamentals": [
            "Meaning_of_Public_Finance",
            "Scope_of_Public_Finance",
            "Role_of_Government",
            "Public_vs_Private_Finance",
            "Functions_of_Public_Finance",
            "Allocation_Function",
            "Distribution_Function",
            "Stabilization_Function"
        ],

        "02_Government_Budget_Basics": [
            "Meaning_of_Budget",
            "Budget_Objectives",
            "Budget_Process",
            "Budget_Documents",
            "Annual_Financial_Statement",
            "Budget_Cycle",
            "Fiscal_Management",
            "Budget_Significance"
        ],

        "03_Constitutional_Provisions": [
            "Article_112",
            "Consolidated_Fund",
            "Contingency_Fund",
            "Public_Account",
            "Money_Bill",
            "Finance_Bill",
            "Parliamentary_Control",
            "Budget_Approval"
        ],

        "04_Budget_Formulation": [
            "Budget_Preparation",
            "Revenue_Estimation",
            "Expenditure_Planning",
            "Ministry_of_Finance",
            "Departmental_Inputs",
            "Fiscal_Framework",
            "Budget_Consultations",
            "Budget_Finalization"
        ],

        "05_Revenue_Receipts": [
            "Tax_Revenue",
            "Non_Tax_Revenue",
            "Direct_Taxes",
            "Indirect_Taxes",
            "Dividends_and_Profits",
            "Fees_and_Fines",
            "Interest_Receipts",
            "Revenue_Trends"
        ],

        "06_Capital_Receipts": [
            "Borrowings",
            "Disinvestment_Receipts",
            "Recovery_of_Loans",
            "Small_Savings",
            "External_Borrowings",
            "Asset_Monetization",
            "Capital_Mobilization",
            "Receipt_Analysis"
        ],

        "07_Revenue_Expenditure": [
            "Administrative_Expenses",
            "Subsidies",
            "Interest_Payments",
            "Pensions",
            "Grants_in_Aid",
            "Maintenance_Expenditure",
            "Welfare_Spending",
            "Expenditure_Trends"
        ],

        "08_Capital_Expenditure": [
            "Infrastructure_Investment",
            "Asset_Creation",
            "Capital_Outlay",
            "Loan_Disbursement",
            "Economic_Development",
            "Public_Investment",
            "Growth_Impact",
            "Capex_Strategy"
        ],

        "09_Fiscal_Deficit": [
            "Fiscal_Deficit_Concept",
            "Calculation_Method",
            "Deficit_Financing",
            "Borrowing_Requirement",
            "Macroeconomic_Impact",
            "Fiscal_Discipline",
            "Deficit_Trends",
            "Policy_Debates"
        ],

        "10_Revenue_Deficit": [
            "Revenue_Deficit_Concept",
            "Revenue_Gap",
            "Current_Expenditure",
            "Fiscal_Health",
            "Deficit_Indicators",
            "Correction_Strategies",
            "Trend_Analysis",
            "Economic_Implications"
        ],

        "11_Primary_Deficit": [
            "Primary_Deficit_Concept",
            "Interest_Payments",
            "Debt_Burden",
            "Fiscal_Sustainability",
            "Deficit_Measurement",
            "Trend_Analysis",
            "Policy_Relevance",
            "Fiscal_Assessment"
        ],

        "12_Public_Debt": [
            "Internal_Debt",
            "External_Debt",
            "Debt_Management",
            "Debt_Sustainability",
            "Government_Securities",
            "Debt_to_GDP_Ratio",
            "Debt_Indicators",
            "Debt_Challenges"
        ],

        "13_FRBM_Framework": [
            "FRBM_Act",
            "Fiscal_Targets",
            "Debt_Targets",
            "Fiscal_Responsibility",
            "Escape_Clause",
            "Fiscal_Rules",
            "Amendments",
            "Implementation"
        ],

        "14_Taxation_and_Revenue_System": [
            "Tax_Structure",
            "Tax_Base",
            "Tax_Compliance",
            "Tax_Efficiency",
            "Tax_Administration",
            "Revenue_Mobilization",
            "Tax_Reforms",
            "Fiscal_Capacity"
        ],

        "15_Centre_State_Financial_Relations": [
            "Fiscal_Federalism",
            "Tax_Devolution",
            "Grants_in_Aid",
            "Vertical_Imbalance",
            "Horizontal_Imbalance",
            "State_Finances",
            "Revenue_Sharing",
            "Fiscal_Coordination"
        ],

        "16_Finance_Commission": [
            "Constitutional_Status",
            "Functions",
            "Recommendations",
            "Tax_Sharing",
            "Grants",
            "Fiscal_Transfers",
            "Recent_Finance_Commissions",
            "Importance"
        ],

        "17_Public_Expenditure_Management": [
            "Outcome_Budgeting",
            "Performance_Budgeting",
            "Expenditure_Control",
            "Public_Accountability",
            "Financial_Management",
            "Efficiency_Measures",
            "Audit_Linkages",
            "Governance_Reforms"
        ],

        "18_Subsidies": [
            "Food_Subsidy",
            "Fertilizer_Subsidy",
            "Petroleum_Subsidy",
            "Subsidy_Targeting",
            "DBT",
            "Fiscal_Cost",
            "Subsidy_Reforms",
            "Welfare_Impact"
        ],

        "19_Disinvestment_and_Privatization": [
            "Disinvestment_Policy",
            "Strategic_Sale",
            "Asset_Monetization",
            "Public_Sector_Reforms",
            "Privatization",
            "Revenue_Generation",
            "Government_Ownership",
            "Recent_Developments"
        ],

        "20_Public_Sector_Finances": [
            "PSU_Finances",
            "Government_Investment",
            "Dividend_Policy",
            "Capital_Infusion",
            "Financial_Performance",
            "Public_Enterprises",
            "Fiscal_Impact",
            "Reform_Measures"
        ],

        "21_Local_Government_Finance": [
            "Panchayat_Finance",
            "Municipal_Finance",
            "Own_Source_Revenue",
            "Local_Body_Grants",
            "Fiscal_Decentralization",
            "Urban_Finance",
            "Rural_Finance",
            "Challenges"
        ],

        "22_Public_Accountability_and_Audit": [
            "CAG",
            "Audit_Process",
            "Parliamentary_Committees",
            "PAC",
            "Financial_Transparency",
            "Accountability_Mechanisms",
            "Compliance_Audit",
            "Performance_Audit"
        ],

        "23_Gender_and_Child_Budgeting": [
            "Gender_Budgeting",
            "Child_Budgeting",
            "Inclusive_Budgeting",
            "Social_Sector_Allocation",
            "Equity_Approach",
            "Outcome_Assessment",
            "Policy_Integration",
            "Best_Practices"
        ],

        "24_Green_Budgeting_and_Climate_Finance": [
            "Green_Budgeting",
            "Climate_Finance",
            "Sustainable_Expenditure",
            "Carbon_Related_Funding",
            "Environmental_Accounting",
            "Green_Investments",
            "Climate_Adaptation_Funds",
            "Future_Strategies"
        ],

        "25_Budget_Reforms_and_Digital_Finance": [
            "Digital_Budgeting",
            "Public_Financial_Management_System",
            "E_Governance",
            "Budget_Transparency",
            "Data_Driven_Finance",
            "Financial_Technology",
            "Process_Reforms",
            "Innovation"
        ],

        "26_Economic_Survey_and_Fiscal_Policy": [
            "Economic_Survey",
            "Fiscal_Policy",
            "Counter_Cyclical_Policy",
            "Public_Investment",
            "Fiscal_Stimulus",
            "Policy_Assessment",
            "Growth_Strategy",
            "Government_Priorities"
        ],

        "27_Current_Affairs_and_Budget_Issues": [
            "Union_Budget",
            "Fiscal_Deficit_Trends",
            "Tax_Revenue_Trends",
            "Subsidy_Debates",
            "Public_Debt_Issues",
            "Finance_Commission_Updates",
            "Recent_Fiscal_Reforms",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Budget_Data",
            "Fiscal_Indicators",
            "Debt_Statistics",
            "Economic_Survey_Data",
            "Finance_Commission_Data",
            "Government_Reports",
            "PYQ_Themes",
            "Assertion_Reason_Topics"
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

    print(f"Creating Public Finance and Budget structure in: {target_base}")

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
    create_public_finance_and_budget_structure()