import os
import shutil

def create_human_geography_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "world-geography",
        "human-geography"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Human_Geography_Fundamentals": [
            "Meaning_of_Human_Geography",
            "Nature_and_Scope",
            "Human_Environment_Relationship",
            "Branches_of_Human_Geography",
            "Cultural_Landscape",
            "Spatial_Organization",
            "Importance_of_Study",
            "Sources_of_Study"
        ],

        "02_Evolution_of_Human_Geography": [
            "Ancient_Geography",
            "Environmental_Determinism",
            "Possibilism",
            "Neo_Determinism",
            "Behavioral_Geography",
            "Humanistic_Geography",
            "Modern_Approaches",
            "Key_Geographers"
        ],

        "03_World_Population_Distribution": [
            "Population_Distribution",
            "Population_Density",
            "Population_Clusters",
            "Sparse_Population_Areas",
            "Factors_Affecting_Distribution",
            "Regional_Patterns",
            "Population_Trends",
            "Global_Comparisons"
        ],

        "04_Population_Growth_and_Transition": [
            "Population_Growth",
            "Demographic_Transition_Model",
            "Population_Explosion",
            "Birth_Rate",
            "Death_Rate",
            "Fertility_Rate",
            "Population_Change",
            "Future_Trends"
        ],

        "05_Population_Composition": [
            "Age_Structure",
            "Sex_Ratio",
            "Dependency_Ratio",
            "Literacy",
            "Occupational_Structure",
            "Population_Pyramids",
            "Demographic_Indicators",
            "Comparative_Analysis"
        ],

        "06_Migration": [
            "Internal_Migration",
            "International_Migration",
            "Push_Factors",
            "Pull_Factors",
            "Refugees",
            "Diaspora",
            "Migration_Patterns",
            "Impacts_of_Migration"
        ],

        "07_Human_Settlements": [
            "Rural_Settlements",
            "Urban_Settlements",
            "Settlement_Patterns",
            "Settlement_Types",
            "Site_and_Situation",
            "Functions_of_Settlements",
            "Settlement_Hierarchy",
            "Evolution"
        ],

        "08_Rural_Settlements": [
            "Compact_Settlements",
            "Dispersed_Settlements",
            "Linear_Settlements",
            "Circular_Settlements",
            "Rural_Housing",
            "Agrarian_Communities",
            "Village_Studies",
            "Characteristics"
        ],

        "09_Urbanization": [
            "Urban_Growth",
            "Urbanization_Process",
            "Megacities",
            "Metropolitan_Regions",
            "Urban_Sprawl",
            "Urban_Challenges",
            "Urban_Planning",
            "Global_Trends"
        ],

        "10_Urban_Models_and_Theories": [
            "Concentric_Zone_Model",
            "Sector_Model",
            "Multiple_Nuclei_Model",
            "Central_Place_Theory",
            "Rank_Size_Rule",
            "Primate_City",
            "Urban_Hierarchy",
            "Applications"
        ],

        "11_Cultural_Geography": [
            "Culture",
            "Cultural_Regions",
            "Cultural_Diffusion",
            "Cultural_Landscapes",
            "Traditions",
            "Globalization_and_Culture",
            "Identity",
            "Diversity"
        ],

        "12_Languages_of_the_World": [
            "Language_Families",
            "Indo_European_Languages",
            "Sino_Tibetan_Languages",
            "Afro_Asiatic_Languages",
            "Language_Distribution",
            "Lingua_Franca",
            "Language_Extinction",
            "Global_Trends"
        ],

        "13_Religions_of_the_World": [
            "Christianity",
            "Islam",
            "Hinduism",
            "Buddhism",
            "Judaism",
            "Sikhism",
            "Religious_Distribution",
            "Religious_Geography"
        ],

        "14_Ethnicity_and_Race": [
            "Ethnic_Groups",
            "Race_Concept",
            "Multiculturalism",
            "Identity",
            "Ethnic_Conflicts",
            "Minority_Groups",
            "Migration_and_Ethnicity",
            "Contemporary_Issues"
        ],

        "15_Political_Geography": [
            "Nation",
            "State",
            "Nation_State",
            "Boundaries",
            "Frontiers",
            "Territoriality",
            "Political_Regions",
            "Geopolitics"
        ],

        "16_Geopolitics_and_Geostrategy": [
            "Heartland_Theory",
            "Rimland_Theory",
            "Sea_Power_Theory",
            "Buffer_States",
            "Strategic_Locations",
            "Global_Power_Regions",
            "Modern_Geopolitics",
            "Applications"
        ],

        "17_Human_Development": [
            "Human_Development_Index",
            "Quality_of_Life",
            "Health_Indicators",
            "Education_Indicators",
            "Income_Indicators",
            "Development_Patterns",
            "Regional_Disparities",
            "Global_Comparisons"
        ],

        "18_Gender_and_Development": [
            "Gender_Geography",
            "Gender_Inequality",
            "Women_Empowerment",
            "Gender_Development_Index",
            "Labour_Participation",
            "Social_Indicators",
            "Contemporary_Issues",
            "Policy_Responses"
        ],

        "19_Health_Geography": [
            "Disease_Distribution",
            "Epidemiology",
            "Pandemics",
            "Health_Indicators",
            "Healthcare_Access",
            "Nutrition",
            "Public_Health",
            "Global_Challenges"
        ],

        "20_Economic_and_Social_Development": [
            "Development_Models",
            "Global_North_and_South",
            "Poverty",
            "Inequality",
            "Social_Development",
            "Economic_Development",
            "Regional_Differences",
            "Sustainability"
        ],

        "21_Resource_and_Human_Interactions": [
            "Resource_Use",
            "Population_Resource_Relationship",
            "Carrying_Capacity",
            "Sustainable_Development",
            "Resource_Conflicts",
            "Environmental_Impacts",
            "Adaptation",
            "Conservation"
        ],

        "22_Human_and_Environmental_Issues": [
            "Climate_Change",
            "Environmental_Degradation",
            "Deforestation",
            "Desertification",
            "Pollution",
            "Resource_Depletion",
            "Environmental_Migration",
            "Global_Responses"
        ],

        "23_Globalization_and_Human_Geography": [
            "Globalization",
            "Cultural_Globalization",
            "Economic_Globalization",
            "Migration_Flows",
            "Communication_Networks",
            "Urban_Networks",
            "Benefits",
            "Challenges"
        ],

        "24_Regional_Human_Geography": [
            "Asia",
            "Africa",
            "Europe",
            "North_America",
            "South_America",
            "Australia",
            "Polar_Regions",
            "Comparative_Analysis"
        ],

        "25_Contemporary_Human_Geography_Issues": [
            "Refugee_Crisis",
            "Population_Ageing",
            "Urban_Poverty",
            "Food_Security",
            "Water_Security",
            "Human_Rights",
            "Migration_Crises",
            "Policy_Debates"
        ],

        "26_SDGs_and_Sustainable_Human_Development": [
            "Sustainable_Development_Goals",
            "Poverty_Reduction",
            "Education_for_All",
            "Health_and_Wellbeing",
            "Gender_Equality",
            "Sustainable_Cities",
            "Climate_Action",
            "Global_Partnerships"
        ],

        "27_Current_Affairs_and_Human_Geography": [
            "Migration_Trends",
            "Urbanization_Trends",
            "Population_Changes",
            "Human_Development_Reports",
            "Refugee_Issues",
            "Geopolitical_Conflicts",
            "Recent_Research",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Population_Maps",
            "Migration_Maps",
            "Urbanization_Maps",
            "Language_Maps",
            "Religion_Maps",
            "Human_Development_Data",
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

    print(f"Creating Human Geography structure in: {target_base}")

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
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("[]")
                    print(f"      - Created: {filename}")
                else:
                    print(f"      - Exists: {filename}")

if __name__ == "__main__":
    create_human_geography_structure()