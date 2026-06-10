import os
import shutil

def create_taxation_system_and_gst_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "taxation-system-and-gst"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

    "01_Taxation_Fundamentals": [
        "Meaning_of_Taxation",
        "Objectives_of_Taxation",
        "Canons_of_Taxation",
        "Tax_Incidence",
        "Tax_Burden",
        "Tax_Shifting",
        "Progressive_Taxation",
        "Tax_System_in_India"
    ],

    "02_Constitutional_Framework_of_Taxation": [
        "Taxation_Powers",
        "Union_List_Taxes",
        "State_List_Taxes",
        "Concurrent_Aspects",
        "Article_265",
        "Finance_Commission_Linkages",
        "Fiscal_Federalism",
        "Constitutional_Amendments"
    ],

    "03_Direct_and_Indirect_Taxes": [
        "Direct_Tax_Concept",
        "Indirect_Tax_Concept",
        "Tax_Classification",
        "Tax_Incidence_Difference",
        "Advantages_of_Direct_Taxes",
        "Advantages_of_Indirect_Taxes",
        "Limitations",
        "Comparative_Analysis"
    ],

    "04_Income_Tax_Basics": [
        "Income_Tax_Act",
        "Taxable_Income",
        "Assessment_Year",
        "Previous_Year",
        "Residential_Status",
        "Tax_Payers",
        "Tax_Slabs",
        "Income_Heads"
    ],

    "05_Personal_Income_Taxation": [
        "Salary_Income",
        "House_Property_Income",
        "Capital_Gains",
        "Business_Income",
        "Other_Sources",
        "Tax_Deductions",
        "Tax_Rebate",
        "Tax_Computation"
    ],

    "06_Corporate_Taxation": [
        "Corporate_Tax",
        "Domestic_Companies",
        "Foreign_Companies",
        "MAT",
        "Corporate_Tax_Reforms",
        "Dividend_Taxation",
        "Business_Taxation",
        "Tax_Competitiveness"
    ],

    "07_Capital_Gains_Taxation": [
        "Short_Term_Capital_Gains",
        "Long_Term_Capital_Gains",
        "Asset_Classification",
        "Indexation",
        "Securities_Taxation",
        "Property_Gains",
        "Exemptions",
        "Recent_Reforms"
    ],

    "08_Tax_Deductions_and_Exemptions": [
        "Section_80C",
        "Section_80D",
        "Tax_Saving_Investments",
        "Exemption_Provisions",
        "Tax_Planning",
        "Deductions_Framework",
        "Compliance_Benefits",
        "Recent_Changes"
    ],

    "09_Tax_Administration": [
        "CBDT",
        "Income_Tax_Department",
        "PAN",
        "TAN",
        "Tax_Returns",
        "Tax_Assessment",
        "Faceless_Assessment",
        "Administration_Reforms"
    ],

    "10_Tax_Compliance_and_Evasion": [
        "Tax_Compliance",
        "Tax_Avoidance",
        "Tax_Evasion",
        "Black_Money",
        "Anti_Avoidance_Rules",
        "Enforcement",
        "Compliance_Measures",
        "Challenges"
    ],

    "11_Goods_and_Services_Tax_Fundamentals": [
        "GST_Concept",
        "Destination_Based_Tax",
        "Value_Added_Taxation",
        "GST_Principles",
        "Need_for_GST",
        "GST_Benefits",
        "GST_Challenges",
        "GST_Architecture"
    ],

    "12_History_of_Indirect_Tax_Reforms": [
        "Excise_Duty",
        "Service_Tax",
        "VAT",
        "CENVAT",
        "Tax_Reform_Committees",
        "GST_Background",
        "Pre_GST_System",
        "Reform_Timeline"
    ],

    "13_Constitutional_Amendment_for_GST": [
        "101st_Amendment",
        "GST_Council",
        "Constitutional_Changes",
        "Centre_State_Powers",
        "Compensation_Framework",
        "Legislative_Structure",
        "Federal_Consensus",
        "Implementation_Process"
    ],

    "14_GST_Council": [
        "Composition",
        "Voting_Structure",
        "Decision_Making",
        "Functions",
        "Rate_Recommendations",
        "Federal_Cooperation",
        "Dispute_Resolution",
        "Recent_Decisions"
    ],

    "15_Structure_of_GST": [
        "CGST",
        "SGST",
        "IGST",
        "UTGST",
        "Dual_GST_Model",
        "Tax_Sharing",
        "Interstate_Supplies",
        "Intrastate_Supplies"
    ],

    "16_GST_Registration_and_Compliance": [
        "GST_Registration",
        "GSTIN",
        "Threshold_Limits",
        "Composition_Scheme",
        "GST_Returns",
        "Compliance_Framework",
        "Digital_Filing",
        "Compliance_Challenges"
    ],

    "17_Input_Tax_Credit": [
        "ITC_Concept",
        "Eligibility",
        "ITC_Utilization",
        "Blocked_Credits",
        "Invoice_Matching",
        "Credit_Chain",
        "Compliance_Issues",
        "GST_Efficiency"
    ],

    "18_GST_Rates_and_Classification": [
        "Nil_Rate",
        "Five_Percent_Slab",
        "Twelve_Percent_Slab",
        "Eighteen_Percent_Slab",
        "TwentyEight_Percent_Slab",
        "HSN_Codes",
        "Rate_Rationalization",
        "Classification_Issues"
    ],

    "19_GST_Revenue_and_Collections": [
        "GST_Collections",
        "Revenue_Trends",
        "State_Revenues",
        "Centre_Revenues",
        "Compensation_Cess",
        "Revenue_Buoyancy",
        "Tax_Base_Expansion",
        "Collection_Analysis"
    ],

    "20_Customs_Duty": [
        "Customs_Act",
        "Import_Duties",
        "Export_Duties",
        "Tariff_Policy",
        "Trade_Protection",
        "Customs_Administration",
        "Border_Taxation",
        "Recent_Reforms"
    ],

    "21_International_Taxation": [
        "Double_Taxation",
        "DTAA",
        "Transfer_Pricing",
        "BEPS",
        "Global_Minimum_Tax",
        "Cross_Border_Taxation",
        "Tax_Treaties",
        "International_Cooperation"
    ],

    "22_Tax_Reforms_in_India": [
        "Direct_Tax_Reforms",
        "Indirect_Tax_Reforms",
        "Tax_Simplification",
        "Digital_Taxation",
        "Faceless_System",
        "Compliance_Improvement",
        "Administrative_Reforms",
        "Future_Directions"
    ],

    "23_Digital_Taxation": [
        "Equalisation_Levy",
        "E_Commerce_Taxation",
        "Digital_Economy",
        "Online_Compliance",
        "Cross_Border_Digital_Tax",
        "Technology_Platforms",
        "Policy_Challenges",
        "Global_Debates"
    ],

    "24_Taxation_and_Development": [
        "Revenue_Mobilization",
        "Redistribution",
        "Economic_Growth",
        "Investment_Climate",
        "Social_Welfare",
        "Fiscal_Capacity",
        "Development_Strategy",
        "Policy_Outcomes"
    ],

    "25_Local_Taxes_and_User_Charges": [
        "Property_Tax",
        "Municipal_Revenues",
        "Local_Body_Taxation",
        "User_Fees",
        "Urban_Finance",
        "Revenue_Autonomy",
        "Local_Governance",
        "Challenges"
    ],

    "26_Tax_Committees_and_Reports": [
        "Kelkar_Committee",
        "Chelliah_Committee",
        "Tax_Reform_Reports",
        "GST_Committees",
        "Expert_Groups",
        "Policy_Recommendations",
        "Implementation_Status",
        "Future_Reforms"
    ],

    "27_Current_Affairs_and_Tax_Issues": [
        "GST_Council_Updates",
        "Tax_Revenue_Trends",
        "Direct_Tax_Collections",
        "GST_Reforms",
        "Global_Tax_Developments",
        "Compliance_Initiatives",
        "Recent_Amendments",
        "UPSC_High_Yield_Topics"
    ],

    "28_Reports_Data_and_Exam_Themes": [
        "Tax_GDP_Ratio",
        "GST_Data",
        "Direct_Tax_Data",
        "Revenue_Trends",
        "Tax_Statistics",
        "Government_Reports",
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

    print(f"Creating Taxation System and GST structure in: {target_base}")

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
    create_taxation_system_and_gst_structure()