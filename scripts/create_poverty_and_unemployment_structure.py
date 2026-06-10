import os
import shutil

def create_poverty_and_unemployment_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "poverty-and-unemployment"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Poverty_Fundamentals": [
            "Meaning_of_Poverty",
            "Absolute_Poverty",
            "Relative_Poverty",
            "Poverty_Concepts",
            "Poverty_Measurement",
            "Economic_Deprivation",
            "Social_Exclusion",
            "Poverty_Indicators"
        ],

        "02_History_of_Poverty_in_India": [
            "Colonial_Legacy",
            "Post_Independence_Poverty",
            "Planning_Era_Poverty",
            "Reform_Era_Changes",
            "Poverty_Trends",
            "Rural_Poverty_Evolution",
            "Urban_Poverty_Evolution",
            "Development_Experience"
        ],

        "03_Poverty_Estimation_Methods": [
            "Poverty_Line",
            "Consumption_Expenditure",
            "Calorie_Norms",
            "Income_Approach",
            "Basic_Needs_Approach",
            "Multidimensional_Approach",
            "Poverty_Ratios",
            "Measurement_Challenges"
        ],

        "04_Poverty_Line_Committees": [
            "Alagh_Committee",
            "Lakdawala_Committee",
            "Tendulkar_Committee",
            "Rangarajan_Committee",
            "Expert_Group_Methodologies",
            "Poverty_Line_Revisions",
            "Comparative_Assessment",
            "Policy_Implications"
        ],

        "05_Multidimensional_Poverty": [
            "MPI_Concept",
            "Health_Dimensions",
            "Education_Dimensions",
            "Living_Standards",
            "UNDP_Methodology",
            "NITI_Aayog_MPI",
            "Regional_Variations",
            "Policy_Relevance"
        ],

        "06_Causes_of_Poverty": [
            "Low_Income",
            "Population_Pressure",
            "Unemployment",
            "Asset_Inequality",
            "Low_Productivity",
            "Social_Disadvantages",
            "Regional_Disparities",
            "Structural_Factors"
        ],

        "07_Rural_Poverty": [
            "Agrarian_Distress",
            "Landlessness",
            "Low_Agricultural_Productivity",
            "Seasonal_Employment",
            "Rural_Indebtedness",
            "Infrastructure_Gaps",
            "Livelihood_Challenges",
            "Rural_Vulnerability"
        ],

        "08_Urban_Poverty": [
            "Urban_Slums",
            "Informal_Employment",
            "Migration_Pressures",
            "Housing_Deprivation",
            "Urban_Livelihoods",
            "Cost_of_Living",
            "Basic_Service_Access",
            "Urban_Vulnerability"
        ],

        "09_Inequality_and_Poverty": [
            "Income_Inequality",
            "Wealth_Inequality",
            "Gini_Coefficient",
            "Consumption_Inequality",
            "Regional_Inequality",
            "Social_Inequality",
            "Opportunity_Inequality",
            "Redistribution_Issues"
        ],

        "10_Unemployment_Fundamentals": [
            "Meaning_of_Unemployment",
            "Labour_Force",
            "Workforce",
            "Labour_Participation",
            "Employment_Status",
            "Unemployment_Rate",
            "Labour_Market",
            "Employment_Indicators"
        ],

        "11_Types_of_Unemployment": [
            "Open_Unemployment",
            "Disguised_Unemployment",
            "Seasonal_Unemployment",
            "Structural_Unemployment",
            "Frictional_Unemployment",
            "Cyclical_Unemployment",
            "Technological_Unemployment",
            "Educated_Unemployment"
        ],

        "12_Rural_Unemployment": [
            "Agricultural_Unemployment",
            "Seasonal_Work_Gaps",
            "Disguised_Labour",
            "Rural_Labour_Market",
            "Underemployment",
            "Employment_Diversification",
            "Migration_Linkages",
            "Policy_Responses"
        ],

        "13_Urban_Unemployment": [
            "Educated_Youth_Unemployment",
            "Job_Search_Unemployment",
            "Informal_Work",
            "Urban_Labour_Market",
            "Skill_Mismatch",
            "Employment_Quality",
            "Labour_Mobility",
            "Urban_Challenges"
        ],

        "14_Employment_and_Growth": [
            "Employment_Elasticity",
            "Jobless_Growth",
            "Labour_Intensive_Growth",
            "Inclusive_Growth",
            "Economic_Expansion",
            "Employment_Creation",
            "Growth_Linkages",
            "Development_Outcomes"
        ],

        "15_Labour_Force_Participation": [
            "LFPR",
            "Worker_Population_Ratio",
            "Female_LFPR",
            "Youth_Participation",
            "Demographic_Factors",
            "Regional_Differences",
            "Participation_Trends",
            "Policy_Implications"
        ],

        "16_Informal_Sector_Employment": [
            "Informal_Economy",
            "Unorganized_Workers",
            "Job_Security",
            "Social_Protection",
            "Wage_Conditions",
            "Informal_Enterprises",
            "Labour_Rights",
            "Formalization"
        ],

        "17_Skill_Development_and_Employment": [
            "Skill_India",
            "Vocational_Training",
            "Apprenticeships",
            "Industry_Skills",
            "Employability",
            "Human_Capital",
            "Reskilling",
            "Future_Workforce"
        ],

        "18_Poverty_Alleviation_Programmes": [
            "Integrated_Rural_Development",
            "Self_Employment_Programmes",
            "Livelihood_Missions",
            "Targeted_Interventions",
            "Community_Development",
            "Social_Assistance",
            "Programme_Evolution",
            "Impact_Assessment"
        ],

        "19_MGNREGA": [
            "Employment_Guarantee",
            "Wage_Employment",
            "Asset_Creation",
            "Rural_Livelihoods",
            "Demand_Driven_Scheme",
            "Implementation_Framework",
            "Achievements",
            "Challenges"
        ],

        "20_Food_and_Social_Security": [
            "National_Food_Security_Act",
            "Public_Distribution_System",
            "Nutritional_Support",
            "Social_Safety_Nets",
            "Food_Access",
            "Household_Security",
            "Welfare_Programmes",
            "Coverage_Mechanisms"
        ],

        "21_Direct_Benefit_Transfer": [
            "DBT_Framework",
            "Targeted_Transfers",
            "Aadhaar_Integration",
            "Leakage_Reduction",
            "Financial_Inclusion_Linkages",
            "Subsidy_Transfers",
            "Governance_Reforms",
            "Impact_Assessment"
        ],

        "22_Financial_Inclusion_and_Poverty": [
            "Jan_Dhan_Yojana",
            "Banking_Access",
            "Micro_Savings",
            "Credit_Access",
            "Insurance_Coverage",
            "Financial_Literacy",
            "Inclusive_Finance",
            "Poverty_Reduction_Linkages"
        ],

        "23_Gender_and_Poverty": [
            "Feminization_of_Poverty",
            "Women_Workforce",
            "Gender_Wage_Gap",
            "Care_Economy",
            "Women_Empowerment",
            "Gender_Exclusion",
            "Social_Protection",
            "Inclusive_Policies"
        ],

        "24_Migration_and_Livelihoods": [
            "Rural_Urban_Migration",
            "Seasonal_Migration",
            "Distress_Migration",
            "Labour_Mobility",
            "Remittances",
            "Livelihood_Strategies",
            "Urban_Integration",
            "Policy_Challenges"
        ],

        "25_SDGs_and_Inclusive_Development": [
            "No_Poverty_Goal",
            "Decent_Work_Goal",
            "Inclusive_Development",
            "Human_Development",
            "Social_Equity",
            "Sustainable_Livelihoods",
            "Global_Targets",
            "Monitoring_Framework"
        ],

        "26_Labour_Reforms_and_Social_Protection": [
            "Labour_Codes",
            "Minimum_Wages",
            "Social_Security",
            "Employee_Benefits",
            "Gig_Workers",
            "Platform_Workers",
            "Worker_Welfare",
            "Reform_Measures"
        ],

        "27_Current_Affairs_and_Social_Issues": [
            "Poverty_Estimates",
            "Employment_Data",
            "Labour_Market_Trends",
            "MGNREGA_Updates",
            "Skill_Development_Updates",
            "Social_Protection_Reforms",
            "Recent_Reports",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "PLFS_Data",
            "Poverty_Statistics",
            "MPI_Data",
            "Employment_Indicators",
            "Labour_Reports",
            "NITI_Aayog_Reports",
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

    print(f"Creating Poverty and Unemployment structure in: {target_base}")

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
    create_poverty_and_unemployment_structure()