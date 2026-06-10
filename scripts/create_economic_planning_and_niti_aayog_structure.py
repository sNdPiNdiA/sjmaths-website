import os
import shutil

def create_economic_planning_and_niti_aayog_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "economic-planning-and-niti-aayog"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Economic_Planning_Fundamentals": [
            "Meaning_of_Economic_Planning",
            "Objectives_of_Planning",
            "Need_for_Planning",
            "Planning_Models",
            "Planned_Development",
            "Mixed_Economy_Framework",
            "Planning_in_Developing_Countries",
            "Evolution_of_Planning"
        ],

        "02_History_of_Planning_in_India": [
            "National_Planning_Committee",
            "Bombay_Plan",
            "People_Plan",
            "Gandhian_Plan",
            "Sarvodaya_Plan",
            "Pre_Independence_Initiatives",
            "Constituent_Debates",
            "Planning_Background"
        ],

        "03_Planning_Commission": [
            "Establishment",
            "Composition",
            "Functions",
            "Planning_Process",
            "Resource_Allocation",
            "Centre_State_Relations",
            "Achievements",
            "Criticisms"
        ],

        "04_Five_Year_Plans_Overview": [
            "Plan_Periods",
            "Growth_Strategy",
            "Plan_Priorities",
            "Public_Sector_Role",
            "Resource_Mobilization",
            "Plan_Financing",
            "Plan_Performance",
            "Plan_Evaluation"
        ],

        "05_First_to_Third_Five_Year_Plans": [
            "First_Plan",
            "Second_Plan",
            "Mahalanobis_Model",
            "Third_Plan",
            "Agricultural_Focus",
            "Industrial_Focus",
            "Plan_Outcomes",
            "Major_Challenges"
        ],

        "06_Fourth_to_Seventh_Five_Year_Plans": [
            "Fourth_Plan",
            "Fifth_Plan",
            "Rolling_Plan",
            "Sixth_Plan",
            "Seventh_Plan",
            "Garibi_Hatao",
            "Poverty_Reduction",
            "Growth_Performance"
        ],

        "07_Eighth_to_Twelfth_Five_Year_Plans": [
            "Eighth_Plan",
            "Ninth_Plan",
            "Tenth_Plan",
            "Eleventh_Plan",
            "Twelfth_Plan",
            "Inclusive_Growth",
            "Sustainable_Growth",
            "Plan_Assessment"
        ],

        "08_Plan_Holidays_and_Rolling_Plans": [
            "Plan_Holiday",
            "Annual_Plans",
            "Rolling_Plans",
            "Economic_Crises",
            "Policy_Adjustments",
            "Interim_Strategies",
            "Historical_Context",
            "Lessons_Learned"
        ],

        "09_Mahalanobis_Strategy": [
            "Heavy_Industry_Model",
            "Capital_Goods_Focus",
            "Investment_Strategy",
            "Growth_Assumptions",
            "Industrialization",
            "Model_Limitations",
            "Long_Term_Impact",
            "Economic_Debates"
        ],

        "10_Green_Revolution_and_Planning": [
            "Agricultural_Modernization",
            "HYV_Seeds",
            "Food_Self_Sufficiency",
            "Regional_Imbalances",
            "Agricultural_Productivity",
            "Policy_Support",
            "Planning_Linkages",
            "Long_Term_Impact"
        ],

        "11_Public_Sector_in_Planning": [
            "Public_Sector_Enterprises",
            "Commanding_Heights",
            "Industrial_Policy",
            "Infrastructure_Development",
            "Investment_Role",
            "Strategic_Sectors",
            "Performance_Issues",
            "Reforms"
        ],

        "12_Liberalization_and_Planning_Reforms": [
            "Economic_Reforms_1991",
            "Market_Orientation",
            "Private_Sector_Role",
            "Globalization",
            "Deregulation",
            "Structural_Adjustment",
            "Planning_Transformation",
            "New_Economic_Policy"
        ],

        "13_Decentralized_Planning": [
            "District_Planning",
            "Local_Governance",
            "Panchayati_Raj",
            "Urban_Local_Bodies",
            "Participatory_Planning",
            "Bottom_Up_Approach",
            "Planning_Committees",
            "Challenges"
        ],

        "14_Cooperative_Federalism": [
            "Federal_Structure",
            "Centre_State_Coordination",
            "Policy_Coordination",
            "Fiscal_Federalism",
            "Institutional_Mechanisms",
            "Inter_State_Council",
            "Collaborative_Governance",
            "Policy_Consensus"
        ],

        "15_NITI_Aayog_Foundation": [
            "Formation_of_NITI_Aayog",
            "Objectives",
            "Vision",
            "Institutional_Structure",
            "Governing_Council",
            "Policy_Think_Tank",
            "Replacement_of_Planning_Commission",
            "Core_Principles"
        ],

        "16_Structure_of_NITI_Aayog": [
            "Chairperson",
            "Vice_Chairperson",
            "CEO",
            "Full_Time_Members",
            "Part_Time_Members",
            "Special_Invitees",
            "Regional_Councils",
            "Organizational_Framework"
        ],

        "17_Functions_of_NITI_Aayog": [
            "Policy_Formulation",
            "Strategic_Planning",
            "Cooperative_Federalism",
            "Monitoring_and_Evaluation",
            "Innovation_Promotion",
            "Knowledge_Sharing",
            "Best_Practices",
            "Capacity_Building"
        ],

        "18_NITI_Aayog_Action_Agenda": [
            "Three_Year_Action_Agenda",
            "Medium_Term_Strategy",
            "Long_Term_Vision",
            "Sectoral_Reforms",
            "Policy_Priorities",
            "Implementation_Framework",
            "Outcome_Focus",
            "Development_Goals"
        ],

        "19_Strategy_for_New_India": [
            "New_India_2022",
            "Economic_Growth",
            "Employment",
            "Infrastructure",
            "Agriculture_Reforms",
            "Human_Development",
            "Governance_Reforms",
            "Implementation_Plan"
        ],

        "20_SDGs_and_NITI_Aayog": [
            "Sustainable_Development_Goals",
            "SDG_Index",
            "Localization_of_SDGs",
            "Monitoring_Framework",
            "State_Performance",
            "Global_Benchmarks",
            "Policy_Integration",
            "Reporting_Mechanisms"
        ],

        "21_Aspirational_Districts_Programme": [
            "Programme_Design",
            "Health_Indicators",
            "Education_Indicators",
            "Agriculture_and_Water",
            "Financial_Inclusion",
            "Skill_Development",
            "Delta_Ranking",
            "Impact_Assessment"
        ],

        "22_Atal_Innovation_Mission": [
            "Innovation_Ecosystem",
            "Atal_Tinkering_Labs",
            "Atal_Incubation_Centres",
            "Startups",
            "Entrepreneurship",
            "Technology_Innovation",
            "Research_Promotion",
            "Innovation_Challenges"
        ],

        "23_Development_Monitoring_and_Evaluation": [
            "Outcome_Budgeting",
            "Performance_Monitoring",
            "Data_Driven_Governance",
            "Policy_Evaluation",
            "Impact_Assessment",
            "Evidence_Based_Policy",
            "Real_Time_Monitoring",
            "Feedback_Mechanisms"
        ],

        "24_Competitive_Federalism": [
            "State_Rankings",
            "Ease_of_Doing_Business",
            "Export_Preparedness_Index",
            "Innovation_Index",
            "School_Education_Index",
            "Health_Index",
            "Performance_Competition",
            "Policy_Outcomes"
        ],

        "25_Economic_Planning_and_Inclusive_Growth": [
            "Inclusive_Development",
            "Regional_Balance",
            "Poverty_Reduction",
            "Employment_Generation",
            "Social_Justice",
            "Human_Capital",
            "Sustainable_Development",
            "Equity_Concerns"
        ],

        "26_Recent_Policy_Initiatives": [
            "Digital_Economy",
            "Green_Growth",
            "Energy_Transition",
            "Manufacturing_Strategy",
            "Logistics_Reforms",
            "Urban_Transformation",
            "Rural_Development",
            "Future_Roadmap"
        ],

        "27_Current_Affairs_and_Policy_Issues": [
            "NITI_Aayog_Reports",
            "SDG_Rankings",
            "State_Performance",
            "Policy_Debates",
            "Economic_Strategy",
            "Development_Indicators",
            "Recent_Reforms",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "NITI_Indexes",
            "Economic_Indicators",
            "Planning_Data",
            "Growth_Trends",
            "State_Comparisons",
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

    print(f"Creating Economic Planning and NITI Aayog structure in: {target_base}")

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
    create_economic_planning_and_niti_aayog_structure()