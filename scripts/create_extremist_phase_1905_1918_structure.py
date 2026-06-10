import os
import shutil

def create_extremist_phase_1905_1918_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "extremist-phase-1905-1918")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_of_Extremist_Phase": [
            "Limitations_of_Moderates",
            "Growth_of_Nationalism",
            "Economic_Discontent",
            "Political_Dissatisfaction",
            "International_Influences",
            "Rise_of_New_Leadership",
            "Curzons_Policies",
            "Transition_from_Moderate_Phase"
        ],

        "02_Ideology_of_Extremists": [
            "Swaraj",
            "Self_Reliance",
            "National_Dignity",
            "Passive_Resistance",
            "Boycott",
            "Mass_Participation",
            "National_Education",
            "Extremist_Worldview"
        ],

        "03_Methods_of_Extremists": [
            "Boycott",
            "Swadeshi",
            "Passive_Resistance",
            "National_Education",
            "Public_Mobilization",
            "Political_Agitation",
            "Economic_Nationalism",
            "Mass_Awakening"
        ],

        "04_Bal_Gangadhar_Tilak": [
            "Political_Philosophy",
            "Kesari_and_Mahratta",
            "Ganapati_Festival",
            "Shivaji_Festival",
            "Swaraj_is_My_Birthright",
            "Political_Campaigns",
            "Congress_Role",
            "Legacy"
        ],

        "05_Bipin_Chandra_Pal": [
            "Political_Ideology",
            "Journalism",
            "Swadeshi_Advocacy",
            "National_Education",
            "Congress_Role",
            "Public_Speeches",
            "Nationalist_Contribution",
            "Legacy"
        ],

        "06_Lala_Lajpat_Rai": [
            "Punjab_Nationalism",
            "Political_Leadership",
            "Educational_Work",
            "Nationalist_Activities",
            "Congress_Role",
            "Public_Mobilization",
            "Political_Writings",
            "Legacy"
        ],

        "07_Aurobindo_Ghosh": [
            "Political_Philosophy",
            "Bande_Mataram",
            "Spiritual_Nationalism",
            "Revolutionary_Connections",
            "Political_Writings",
            "Nationalist_Thought",
            "Withdrawal_from_Politics",
            "Legacy"
        ],

        "08_Lal_Bal_Pal": [
            "Formation_of_Trio",
            "Common_Objectives",
            "Regional_Strengths",
            "Mass_Mobilization",
            "Political_Influence",
            "Nationalist_Leadership",
            "Congress_Impact",
            "Historical_Assessment"
        ],

        "09_Partition_of_Bengal": [
            "Curzons_Decision",
            "Administrative_Arguments",
            "Nationalist_Opposition",
            "Public_Reaction",
            "Political_Consequences",
            "Anti_Partition_Campaign",
            "Growth_of_Nationalism",
            "Historical_Significance"
        ],

        "10_Swadeshi_Movement": [
            "Objectives",
            "Boycott_of_Foreign_Goods",
            "Promotion_of_Indigenous_Industry",
            "Public_Participation",
            "Economic_Impact",
            "Political_Impact",
            "Regional_Spread",
            "Historical_Assessment"
        ],

        "11_National_Education_Movement": [
            "National_Council_of_Education",
            "Bengal_National_College",
            "Alternative_Education",
            "Educational_Nationalism",
            "Student_Participation",
            "Institution_Building",
            "Cultural_Revival",
            "Impact"
        ],

        "12_Boycott_and_Passive_Resistance": [
            "Economic_Boycott",
            "Political_Boycott",
            "Social_Boycott",
            "Passive_Resistance_Strategy",
            "Mass_Participation",
            "Regional_Experiments",
            "Challenges",
            "Historical_Impact"
        ],

        "13_Congress_and_Extremists": [
            "Rise_within_INC",
            "Conflict_with_Moderates",
            "Leadership_Disputes",
            "Organizational_Issues",
            "Political_Differences",
            "Congress_Sessions",
            "Factional_Politics",
            "Historical_Assessment"
        ],

        "14_Surat_Split_1907": [
            "Background",
            "Session_of_1907",
            "Moderate_Extremist_Conflict",
            "Leadership_Question",
            "Split_in_Congress",
            "Immediate_Consequences",
            "Long_Term_Impact",
            "Historical_Debates"
        ],

        "15_Revolutionary_Nationalism_Background": [
            "Origins",
            "Influence_of_Extremism",
            "International_Inspirations",
            "Secret_Societies",
            "Youth_Politics",
            "Political_Radicalization",
            "Nationalist_Militancy",
            "Historical_Context"
        ],

        "16_Revolutionary_Organizations": [
            "Anushilan_Samiti",
            "Jugantar",
            "Abhinav_Bharat",
            "Secret_Networks",
            "Recruitment",
            "Training",
            "Organization_Structure",
            "Activities"
        ],

        "17_Revolutionary_Activities": [
            "Alipore_Bomb_Case",
            "Muzaffarpur_Incident",
            "Political_Assassinations",
            "Bomb_Manufacture",
            "Armed_Resistance",
            "British_Response",
            "Trials",
            "Impact"
        ],

        "18_Revolutionaries_in_India": [
            "Khudiram_Bose",
            "Prafulla_Chaki",
            "Barindra_Ghosh",
            "Rashbehari_Bose",
            "Sachindranath_Sanyal",
            "Jatin_Mukherjee",
            "Regional_Networks",
            "Contribution"
        ],

        "19_Revolutionaries_Abroad": [
            "Shyamji_Krishna_Varma",
            "India_House",
            "Madam_Cama",
            "V_D_Savarkar",
            "International_Propaganda",
            "Expatriate_Nationalism",
            "Foreign_Networks",
            "Impact"
        ],

        "20_Ghadar_Movement": [
            "Origins",
            "Lala_Hardayal",
            "Ghadar_Party",
            "Overseas_Indians",
            "World_War_I_Context",
            "Revolutionary_Plans",
            "Failure_of_Uprising",
            "Historical_Significance"
        ],

        "21_Home_Rule_Movement": [
            "Background",
            "Annie_Besant",
            "Bal_Gangadhar_Tilak",
            "Home_Rule_Leagues",
            "Methods_of_Agitation",
            "Public_Response",
            "Government_Reaction",
            "Historical_Impact"
        ],

        "22_Reunion_of_Congress": [
            "Need_for_Unity",
            "Moderate_Extremist_Reconciliation",
            "Political_Circumstances",
            "Leadership_Role",
            "Congress_Reorganization",
            "Nationalist_Strategy",
            "Outcome",
            "Historical_Significance"
        ],

        "23_Lucknow_Pact_1916": [
            "Congress_League_Cooperation",
            "Background",
            "Terms_of_Pact",
            "Separate_Electorates",
            "Political_Compromise",
            "Nationalist_Expectations",
            "Historical_Assessment",
            "Long_Term_Consequences"
        ],

        "24_World_War_I_and_Nationalism": [
            "Indian_Support_for_Britain",
            "Economic_Impact",
            "Political_Expectations",
            "Recruitment",
            "War_Time_Policies",
            "Nationalist_Reaction",
            "Growth_of_Discontent",
            "Historical_Impact"
        ],

        "25_British_Response": [
            "Repressive_Laws",
            "Deportations",
            "Press_Restrictions",
            "Surveillance",
            "Arrests",
            "Political_Control",
            "Administrative_Strategy",
            "Impact_on_Nationalism"
        ],

        "26_Historiography": [
            "Nationalist_View",
            "Cambridge_School",
            "Marxist_Interpretation",
            "Extremists_vs_Moderates",
            "Role_of_Revolutionaries",
            "Mass_Politics_Debate",
            "Revisionist_Views",
            "Modern_Assessment"
        ],

        "27_Sources": [
            "Congress_Records",
            "Nationalist_Newspapers",
            "Government_Reports",
            "Private_Correspondence",
            "Revolutionary_Literature",
            "Memoirs",
            "Foreign_Sources",
            "Source_Criticism"
        ],

        "28_Legacy_and_Historical_Significance": [
            "Preparation_for_Gandhian_Era",
            "Mass_Politics",
            "Growth_of_Swaraj_Idea",
            "Economic_Nationalism",
            "Political_Radicalization",
            "National_Unity",
            "Influence_on_Freedom_Struggle",
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

    print(f"Creating Extremist Phase (1905-1918) structure in: {target_base}")
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
    create_extremist_phase_1905_1918_structure()