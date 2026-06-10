import os
import shutil

def create_demography_and_census_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
    project_root,
    "gs-question-bank",
    "geography",
    "indian-geography",
    "demography-and-census"
)

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = structure = {

    "01_Demography_Fundamentals": [
        "Meaning_of_Demography",
        "Population_Geography",
        "Population_Studies",
        "Demographic_Concepts",
        "Population_as_a_Resource",
        "Population_Dynamics",
        "Importance_of_Demographic_Studies",
        "Sources_of_Study"
    ],

    "02_Census_and_Population_Data": [
        "Meaning_of_Census",
        "History_of_Census_in_India",
        "Census_Organization",
        "Data_Collection_Methods",
        "Population_Register",
        "Census_Operations",
        "Data_Interpretation",
        "Importance_of_Census"
    ],

    "03_History_of_Population_Growth_in_India": [
        "Colonial_Period",
        "Population_Explosion",
        "Demographic_Transition",
        "Post_Independence_Growth",
        "Growth_Phases",
        "Population_Trends",
        "Historical_Analysis",
        "Future_Projections"
    ],

    "04_Distribution_of_Population": [
        "Spatial_Distribution",
        "Regional_Patterns",
        "Population_Concentration",
        "Sparse_Population_Areas",
        "Density_Regions",
        "Population_Clusters",
        "Geographical_Factors",
        "Distribution_Trends"
    ],

    "05_Population_Density": [
        "Meaning_of_Density",
        "Arithmetic_Density",
        "Physiological_Density",
        "Agricultural_Density",
        "Statewise_Density",
        "Regional_Variations",
        "Factors_Affecting_Density",
        "Recent_Trends"
    ],

    "06_Population_Growth": [
        "Absolute_Growth",
        "Decadal_Growth",
        "Natural_Growth",
        "Growth_Rates",
        "Regional_Differences",
        "Population_Explosion",
        "Growth_Trends",
        "Future_Challenges"
    ],

    "07_Demographic_Transition_Model": [
        "Stage_One",
        "Stage_Two",
        "Stage_Three",
        "Stage_Four",
        "Stage_Five",
        "Indian_Experience",
        "Population_Change",
        "Comparative_Analysis"
    ],

    "08_Birth_Rate_and_Fertility": [
        "Crude_Birth_Rate",
        "General_Fertility_Rate",
        "Total_Fertility_Rate",
        "Replacement_Level",
        "Regional_Variations",
        "Determinants_of_Fertility",
        "Recent_Trends",
        "Policy_Implications"
    ],

    "09_Death_Rate_and_Mortality": [
        "Crude_Death_Rate",
        "Infant_Mortality_Rate",
        "Maternal_Mortality_Rate",
        "Life_Expectancy",
        "Mortality_Trends",
        "Regional_Differences",
        "Health_Indicators",
        "Demographic_Implications"
    ],

    "10_Sex_Ratio": [
        "Meaning_of_Sex_Ratio",
        "Child_Sex_Ratio",
        "Statewise_Patterns",
        "Regional_Disparities",
        "Gender_Issues",
        "Declining_Sex_Ratio",
        "Government_Initiatives",
        "Recent_Trends"
    ],

    "11_Age_Composition": [
        "Age_Structure",
        "Youth_Population",
        "Working_Age_Population",
        "Elderly_Population",
        "Dependency_Ratio",
        "Demographic_Dividend",
        "Population_Ageing",
        "Challenges"
    ],

    "12_Literacy_and_Education": [
        "Literacy_Rate",
        "Male_Literacy",
        "Female_Literacy",
        "Educational_Attainment",
        "Regional_Differences",
        "Census_Data",
        "Human_Development",
        "Recent_Trends"
    ],

    "13_Rural_and_Urban_Population": [
        "Rural_Population",
        "Urban_Population",
        "Urbanization",
        "Rural_Urban_Distribution",
        "Census_Definitions",
        "Migration_Linkages",
        "Population_Trends",
        "Challenges"
    ],

    "14_Urbanization_in_India": [
        "Urban_Growth",
        "Metropolitan_Cities",
        "Million_Plus_Cities",
        "Urban_Corridors",
        "Smart_Cities",
        "Urban_Challenges",
        "Regional_Patterns",
        "Future_Trends"
    ],

    "15_Migration_Fundamentals": [
        "Meaning_of_Migration",
        "Types_of_Migration",
        "Internal_Migration",
        "International_Migration",
        "Migration_Streams",
        "Migration_Patterns",
        "Migration_Data",
        "Concepts_and_Terminology"
    ],

    "16_Internal_Migration_in_India": [
        "Rural_to_Urban",
        "Urban_to_Urban",
        "Rural_to_Rural",
        "Urban_to_Rural",
        "Seasonal_Migration",
        "Inter_State_Migration",
        "Migration_Corridors",
        "Recent_Trends"
    ],

    "17_Causes_and_Impacts_of_Migration": [
        "Push_Factors",
        "Pull_Factors",
        "Economic_Causes",
        "Social_Causes",
        "Demographic_Impacts",
        "Urbanization_Impact",
        "Regional_Development",
        "Challenges"
    ],

    "18_Population_Policies": [
        "National_Population_Policy",
        "Family_Planning",
        "Population_Control",
        "Reproductive_Health",
        "Policy_Evolution",
        "Government_Programmes",
        "Achievements",
        "Challenges"
    ],

    "19_Human_Development_and_Population": [
        "Human_Development_Index",
        "Quality_of_Life",
        "Health_Indicators",
        "Education_Indicators",
        "Income_Indicators",
        "Regional_Disparities",
        "Demographic_Linkages",
        "Development_Challenges"
    ],

    "20_Demographic_Dividend": [
        "Working_Age_Population",
        "Economic_Growth",
        "Skill_Development",
        "Employment",
        "Youth_Bulge",
        "Opportunities",
        "Challenges",
        "Policy_Responses"
    ],

    "21_Population_Ageing": [
        "Elderly_Population",
        "Ageing_Trends",
        "Social_Security",
        "Health_Care",
        "Dependency_Burden",
        "Regional_Patterns",
        "Policy_Challenges",
        "Future_Projections"
    ],

    "22_Tribal_and_Vulnerable_Populations": [
        "Scheduled_Tribes",
        "Demographic_Profile",
        "Geographical_Distribution",
        "Population_Trends",
        "Socioeconomic_Indicators",
        "Development_Issues",
        "Government_Programmes",
        "Challenges"
    ],

    "23_Religious_and_Linguistic_Composition": [
        "Religious_Groups",
        "Language_Groups",
        "Census_Data",
        "Regional_Patterns",
        "Demographic_Trends",
        "Cultural_Diversity",
        "Population_Characteristics",
        "Recent_Changes"
    ],

    "24_Census_Indicators_and_Data_Analysis": [
        "Population_Pyramid",
        "Dependency_Ratio",
        "Sex_Ratio_Analysis",
        "Literacy_Analysis",
        "Growth_Rate_Analysis",
        "Demographic_Indicators",
        "Data_Interpretation",
        "Statistical_Tools"
    ],

    "25_Population_and_Development": [
        "Population_Resource_Relationship",
        "Economic_Development",
        "Human_Capital",
        "Employment",
        "Poverty",
        "Regional_Development",
        "Sustainable_Development",
        "Future_Challenges"
    ],

    "26_Population_and_Environment": [
        "Carrying_Capacity",
        "Resource_Pressure",
        "Environmental_Degradation",
        "Climate_Change",
        "Urban_Stress",
        "Land_Use_Change",
        "Sustainability",
        "Policy_Responses"
    ],

    "27_Current_Affairs_and_Policy_Issues": [
        "Latest_Census_Issues",
        "Population_Policies",
        "Migration_Trends",
        "Urbanization_Trends",
        "Demographic_Dividend",
        "Ageing_Population",
        "Recent_Government_Initiatives",
        "UPSC_High_Yield_Topics"
    ],

    "28_Maps_Data_and_Exam_Themes": [
        "Population_Density_Maps",
        "Migration_Maps",
        "Urbanization_Maps",
        "Literacy_Maps",
        "Sex_Ratio_Maps",
        "Census_Data_Analysis",
        "Map_Based_Questions",
        "PYQ_Themes"
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

    print(f"Creating Demography and Census structure in: {target_base}")
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
    create_demography_and_census_structure()