import os
import shutil

def create_basics_and_national_income_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "basics-and-national-income"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Macroeconomics_Fundamentals": [
    "Meaning_of_Macroeconomics",
    "Scope_of_Macroeconomics",
    "Micro_vs_Macro",
    "Aggregate_Variables",
    "Macroeconomic_Goals",
    "Economic_System",
    "Policy_Relevance",
    "Importance_of_Macroeconomics"
],

"02_Economic_Activities": [
    "Production",
    "Consumption",
    "Exchange",
    "Distribution",
    "Economic_Agents",
    "Circular_Flow_Basics",
    "Factor_Payments",
    "Economic_Transactions"
],

"03_National_Income_Concepts": [
    "National_Income",
    "Domestic_Income",
    "Personal_Income",
    "Disposable_Income",
    "Private_Income",
    "Factor_Income",
    "Transfer_Income",
    "Income_Flow"
],

"04_GDP_Concept": [
    "Gross_Domestic_Product",
    "GDP_Definition",
    "Domestic_Territory",
    "Production_Boundary",
    "GDP_Measurement",
    "GDP_Significance",
    "Nominal_Output",
    "Economic_Size"
],

"05_GNP_Concept": [
    "Gross_National_Product",
    "Net_Factor_Income_From_Abroad",
    "Resident_Concept",
    "Nationality_vs_Residence",
    "External_Factor_Income",
    "National_Output",
    "GNP_Estimation",
    "Comparative_Analysis"
],

"06_NDP_and_NNP": [
    "Depreciation",
    "Capital_Consumption",
    "Net_Domestic_Product",
    "Net_National_Product",
    "Net_Output",
    "Asset_Wear_and_Tear",
    "Net_Income_Concept",
    "Income_Adjustment"
],

"07_Market_Price_and_Factor_Cost": [
    "Market_Price",
    "Factor_Cost",
    "Indirect_Taxes",
    "Subsidies",
    "Price_Adjustments",
    "Income_Valuation",
    "Cost_Concepts",
    "National_Income_Conversion"
],

"08_National_Income_Aggregates": [
    "GDP_at_MP",
    "GDP_at_FC",
    "GNP_at_MP",
    "GNP_at_FC",
    "NNP_at_MP",
    "NNP_at_FC",
    "Aggregate_Relationships",
    "Income_Accounting"
],

"09_Circular_Flow_of_Income": [
    "Two_Sector_Model",
    "Households",
    "Firms",
    "Income_Flow",
    "Expenditure_Flow",
    "Real_Flow",
    "Money_Flow",
    "Circular_Flow_Equilibrium"
],

"10_Three_and_Four_Sector_Models": [
    "Government_Sector",
    "Foreign_Sector",
    "Taxes",
    "Government_Expenditure",
    "Exports",
    "Imports",
    "Leakages",
    "Injections"
],

"11_Production_Method": [
    "Value_Added_Method",
    "Output_Method",
    "Intermediate_Goods",
    "Final_Goods",
    "Value_Addition",
    "Production_Accounting",
    "Sectoral_Output",
    "Estimation_Process"
],

"12_Income_Method": [
    "Compensation_of_Employees",
    "Rent",
    "Interest",
    "Profit",
    "Mixed_Income",
    "Factor_Payments",
    "Income_Generation",
    "Income_Accounting"
],

"13_Expenditure_Method": [
    "Private_Consumption",
    "Government_Consumption",
    "Gross_Capital_Formation",
    "Inventory_Changes",
    "Exports",
    "Imports",
    "Aggregate_Demand",
    "Expenditure_Accounting"
],

"14_National_Income_Measurement_in_India": [
    "CSO_History",
    "NSO",
    "MOSPI",
    "Base_Year",
    "Data_Sources",
    "National_Accounts_Statistics",
    "Measurement_Framework",
    "Methodological_Changes"
],

        "15_Nominal_and_Real_National_Income": [
    "Nominal_GDP",
    "Real_GDP",
    "GDP_Deflator",
    "Price_Changes",
    "Inflation_Adjustment",
    "Constant_Prices",
    "Current_Prices",
    "Growth_Comparison"
],

"16_Per_Capita_Income": [
    "Per_Capita_Income",
    "Income_Per_Person",
    "Living_Standards",
    "Population_Adjustment",
    "Income_Comparison",
    "Development_Indicator",
    "Regional_Differences",
    "Limitations"
],

"17_GDP_Growth_and_Economic_Growth": [
    "Economic_Growth",
    "Growth_Rate",
    "Output_Expansion",
    "Long_Term_Growth",
    "Growth_Indicators",
    "Productivity_Growth",
    "Growth_Drivers",
    "Growth_Trends"
],

"18_GDP_vs_Economic_Development": [
    "Economic_Development",
    "Human_Development",
    "Quality_of_Life",
    "Inclusive_Growth",
    "Development_Indicators",
    "Income_vs_Welfare",
    "Capabilities_Approach",
    "Development_Measures"
],

"19_Sectoral_Composition_of_Economy": [
    "Primary_Sector",
    "Secondary_Sector",
    "Tertiary_Sector",
    "Sectoral_Shares",
    "Structural_Change",
    "Economic_Transformation",
    "Sectoral_Growth",
    "Output_Composition"
],

"20_Savings_and_Investment": [
    "Household_Savings",
    "Corporate_Savings",
    "Public_Savings",
    "Gross_Savings",
    "Capital_Formation",
    "Investment_Rate",
    "Savings_Investment_Relationship",
    "Economic_Growth_Linkage"
],

"21_Capital_Formation": [
    "Gross_Capital_Formation",
    "Net_Capital_Formation",
    "Fixed_Capital",
    "Infrastructure_Creation",
    "Productive_Assets",
    "Investment_Expansion",
    "Capital_Accumulation",
    "Development_Impact"
],

"22_Green_GDP_and_Alternative_Measures": [
    "Green_GDP",
    "Environmental_Costs",
    "Sustainable_Income",
    "Natural_Resource_Depletion",
    "Environmental_Accounting",
    "Genuine_Progress",
    "Sustainability_Measures",
    "Alternative_Indicators"
],

"23_Human_Development_Indicators": [
    "HDI",
    "Education_Index",
    "Health_Index",
    "Income_Index",
    "Human_Capabilities",
    "Development_Rankings",
    "Social_Progress",
    "Quality_of_Life"
],

"24_National_Income_Limitations": [
    "Non_Market_Activities",
    "Underground_Economy",
    "Income_Distribution_Ignored",
    "Environmental_Damage",
    "Welfare_Limitations",
    "Data_Problems",
    "Measurement_Errors",
    "Comparability_Issues"
],

"25_Indian_Economy_Trends": [
    "GDP_Trends",
    "Sectoral_Trends",
    "Income_Trends",
    "Growth_Patterns",
    "Structural_Transformation",
    "Development_Path",
    "Emerging_Challenges",
    "Future_Prospects"
],

"26_National_Income_Data_and_Statistics": [
    "National_Accounts_Statistics",
    "GDP_Data",
    "Growth_Data",
    "Sectoral_Data",
    "Income_Data",
    "Statistical_Methods",
    "Data_Interpretation",
    "Official_Publications"
],

"27_Current_Affairs_and_Macroeconomics": [
    "GDP_Releases",
    "Growth_Estimates",
    "National_Income_Updates",
    "Economic_Survey_Findings",
    "MOSPI_Reports",
    "Development_Trends",
    "Recent_Data",
    "UPSC_High_Yield_Topics"
],

"28_Reports_Data_and_Exam_Themes": [
    "Economic_Survey",
    "National_Accounts_Statistics",
    "GDP_Series",
    "Per_Capita_Income_Data",
    "HDI_Reports",
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

    print(f"Creating Basics and National Income structure in: {target_base}")

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
    create_basics_and_national_income_structure()