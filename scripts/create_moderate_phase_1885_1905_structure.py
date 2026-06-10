import os
import shutil

def create_moderate_phase_1885_1905_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "moderate-phase-1885-1905")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_of_Indian_Nationalism": [
            "Political_Unification",
            "Western_Education",
            "Press_and_Public_Opinion",
            "Socio_Religious_Reforms",
            "Economic_Exploitation",
            "Rise_of_Middle_Class",
            "Political_Associations",
            "National_Consciousness"
        ],

        "02_Pre_Congress_Political_Associations": [
            "British_Indian_Association",
            "Poona_Sarvajanik_Sabha",
            "Indian_Association",
            "Madras_Mahajan_Sabha",
            "Bombay_Presidency_Association",
            "Regional_Political_Bodies",
            "Political_Awakening",
            "Contribution_to_Nationalism"
        ],

        "03_Foundation_of_Indian_National_Congress": [
            "A_O_Hume",
            "First_Congress_Session_1885",
            "Womesh_Chandra_Bonnerjee",
            "Objectives_of_INC",
            "Safety_Valve_Theory",
            "Early_Organization",
            "British_Attitude",
            "Historical_Assessment"
        ],

        "04_Ideology_of_Moderates": [
            "Faith_in_British_Justice",
            "Constitutionalism",
            "Gradual_Reforms",
            "Political_Education",
            "Loyalty_to_Crown",
            "Liberal_Influence",
            "National_Unity",
            "Moderate_Worldview"
        ],

        "05_Methods_of_Moderates": [
            "Prayers",
            "Petitions",
            "Protests",
            "Memoranda",
            "Public_Meetings",
            "Delegations_to_Britain",
            "Press_Campaigns",
            "Constitutional_Agitation"
        ],

        "06_Dadabhai_Naoroji": [
            "Life_and_Career",
            "Drain_Theory",
            "Poverty_and_UnBritish_Rule",
            "Congress_Leadership",
            "British_Parliament",
            "Economic_Critique",
            "Nationalist_Contribution",
            "Legacy"
        ],

        "07_Surendranath_Banerjee": [
            "Political_Career",
            "Indian_Association",
            "Civil_Service_Agitation",
            "Public_Mobilization",
            "Congress_Role",
            "Nationalism",
            "Political_Education",
            "Legacy"
        ],

        "08_Pherozeshah_Mehta": [
            "Bombay_Politics",
            "Municipal_Reforms",
            "Congress_Role",
            "Constitutional_Methods",
            "Political_Leadership",
            "Public_Service",
            "Moderate_Thought",
            "Legacy"
        ],

        "09_Gopal_Krishna_Gokhale": [
            "Political_Ideology",
            "Servants_of_India_Society",
            "Legislative_Work",
            "Economic_Reforms",
            "Educational_Reforms",
            "Congress_Leadership",
            "Mentorship_of_Gandhi",
            "Legacy"
        ],

        "10_Other_Moderate_Leaders": [
            "M_G_Ranade",
            "Ananda_Charlu",
            "Dinshaw_Wacha",
            "R_C_Dutt",
            "Madan_Mohan_Malaviya",
            "Badruddin_Tyabji",
            "Subramania_Iyer",
            "Collective_Contribution"
        ],

        "11_Economic_Critique_of_Colonialism": [
            "Drain_of_Wealth",
            "Deindustrialization",
            "Land_Revenue_Criticism",
            "Military_Expenditure",
            "Home_Charges",
            "Economic_Nationalism",
            "Poverty_Analysis",
            "Impact_on_Nationalism"
        ],

        "12_Political_Demands": [
            "Indianization_of_Services",
            "Legislative_Reforms",
            "Expansion_of_Councils",
            "Representative_Government",
            "Civil_Liberties",
            "Separation_of_Judiciary",
            "Administrative_Reforms",
            "Political_Rights"
        ],

        "13_Social_and_Educational_Demands": [
            "Expansion_of_Education",
            "Primary_Education",
            "Technical_Education",
            "Social_Reforms",
            "Women's_Education",
            "Public_Health",
            "Administrative_Access",
            "Social_Progress"
        ],

        "14_Congress_Sessions_1885_1890": [
            "Bombay_1885",
            "Calcutta_1886",
            "Madras_1887",
            "Allahabad_1888",
            "Bombay_1889",
            "Calcutta_1890",
            "Key_Resolutions",
            "Organizational_Growth"
        ],

        "15_Congress_Sessions_1891_1895": [
            "Nagpur_1891",
            "Allahabad_1892",
            "Lahore_1893",
            "Madras_1894",
            "Poona_1895",
            "Major_Debates",
            "Political_Resolutions",
            "Growth_of_Nationalism"
        ],

        "16_Congress_Sessions_1896_1900": [
            "Calcutta_1896",
            "Amraoti_1897",
            "Madras_1898",
            "Lucknow_1899",
            "Lahore_1900",
            "Economic_Issues",
            "Political_Questions",
            "National_Awareness"
        ],

        "17_Congress_Sessions_1901_1905": [
            "Calcutta_1901",
            "Ahmedabad_1902",
            "Madras_1903",
            "Bombay_1904",
            "Banaras_1905",
            "Changing_Political_Climate",
            "Rise_of_New_Ideas",
            "Transition_Period"
        ],

        "18_British_Response_to_Moderates": [
            "Official_Attitude",
            "Indian_Councils_Act_1892",
            "Limited_Reforms",
            "Administrative_Resistance",
            "Political_Surveillance",
            "Concessions_and_Constraints",
            "Government_Strategy",
            "Historical_Assessment"
        ],

        "19_Indian_Councils_Act_1892": [
            "Background",
            "Provisions",
            "Indirect_Elections",
            "Council_Expansion",
            "Limitations",
            "Moderate_Reaction",
            "Political_Impact",
            "Historical_Significance"
        ],

        "20_Press_and_Public_Opinion": [
            "Nationalist_Newspapers",
            "The_Hindu",
            "Kesari",
            "Bengalee",
            "Public_Debates",
            "Political_Awareness",
            "Role_of_Journalism",
            "Nationalist_Communication"
        ],

        "21_Moderates_and_British_Parliament": [
            "British_Committee_of_INC",
            "Parliamentary_Lobbying",
            "Delegations_to_England",
            "Liberal_Party_Connections",
            "Political_Advocacy",
            "Limitations",
            "Achievements",
            "Historical_Impact"
        ],

        "22_Growth_of_National_Consciousness": [
            "Political_Education",
            "National_Unity",
            "Public_Participation",
            "Regional_Integration",
            "Rise_of_Political_Identity",
            "National_Discourse",
            "Awakening_of_Masses",
            "Historical_Importance"
        ],

        "23_Limitations_of_Moderates": [
            "Elite_Character",
            "Limited_Mass_Base",
            "Faith_in_British_Rule",
            "Slow_Methods",
            "Organizational_Weaknesses",
            "Political_Constraints",
            "Internal_Criticism",
            "Historical_Debates"
        ],

        "24_Rise_of_Extremist_Criticism": [
            "Tilaks_Critique",
            "Assertive_Nationalism",
            "Demand_for_Swaraj",
            "Criticism_of_Petitions",
            "Generational_Differences",
            "Political_Radicalization",
            "New_Leadership",
            "Ideological_Conflict"
        ],

        "25_Partition_of_Bengal_and_Transition": [
            "Curzons_Policies",
            "Partition_of_Bengal_1905",
            "Administrative_Justification",
            "Nationalist_Response",
            "Anti_Partition_Agitation",
            "Birth_of_Swadeshi",
            "Political_Turning_Point",
            "Transition_to_Extremist_Phase"
        ],

        "26_Historiography": [
            "Nationalist_View",
            "Cambridge_School",
            "Marxist_Interpretation",
            "Liberal_Interpretation",
            "Revisionist_Views",
            "Contribution_Debates",
            "Moderates_vs_Extremists",
            "Modern_Assessment"
        ],

        "27_Sources": [
            "Congress_Records",
            "Proceedings_of_Sessions",
            "Political_Writings",
            "Newspapers",
            "Personal_Correspondence",
            "Government_Reports",
            "British_Records",
            "Source_Criticism"
        ],

        "28_Legacy_and_Historical_Significance": [
            "Foundation_of_National_Movement",
            "Political_Training",
            "Economic_Nationalism",
            "Democratic_Traditions",
            "Institution_Building",
            "National_Unity",
            "Influence_on_Later_Phases",
            "Contemporary_Relevance"
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

    print(f"Creating Moderate Phase (1885-1905) structure in: {target_base}")
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
    create_moderate_phase_1885_1905_structure()