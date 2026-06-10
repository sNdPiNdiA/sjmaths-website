import os
import shutil

def create_gandhian_era_1919_1947_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "gandhian-era-1919-1947")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Gandhi_Arrival_and_Background": [
            "Return_from_South_Africa",
            "Political_Context_1919",
            "Champaran_Satyagraha",
            "Ahmedabad_Mill_Strike",
            "Kheda_Satyagraha",
            "Rise_of_Gandhi",
            "Mass_Politics",
            "Historical_Significance"
        ],

        "02_Gandhian_Ideology": [
            "Satyagraha",
            "Ahimsa",
            "Truth",
            "Non_Violence",
            "Sarvodaya",
            "Trusteeship",
            "Constructive_Programme",
            "Political_Philosophy"
        ],

        "03_Rowlatt_Act_and_Jallianwala_Bagh": [
            "Rowlatt_Act",
            "Nationwide_Protests",
            "Punjab_Crisis",
            "General_Dyer",
            "Jallianwala_Bagh_Massacre",
            "Hunter_Commission",
            "National_Reaction",
            "Historical_Impact"
        ],

        "04_Khilafat_Movement": [
            "Background",
            "Ali_Brothers",
            "Ottoman_Issue",
            "Congress_Khilafat_Alliance",
            "Mass_Mobilization",
            "Religious_Dimensions",
            "Decline_of_Movement",
            "Historical_Assessment"
        ],

        "05_Non_Cooperation_Movement": [
            "Launch_of_Movement",
            "Programme_of_Action",
            "Boycott_of_Institutions",
            "Mass_Participation",
            "Role_of_Students",
            "Role_of_Women",
            "Achievements",
            "Historical_Assessment"
        ],

        "06_Chauri_Chaura_and_Aftermath": [
            "Chauri_Chaura_Incident",
            "Withdrawal_of_Movement",
            "National_Reaction",
            "Criticism_of_Gandhi",
            "Political_Consequences",
            "Congress_Debates",
            "Strategic_Shift",
            "Historical_Impact"
        ],

        "07_Swarajists_and_No_Changers": [
            "Formation_of_Swaraj_Party",
            "C_R_Das",
            "Motilal_Nehru",
            "Council_Entry_Debate",
            "No_Changers",
            "Legislative_Politics",
            "Achievements",
            "Historical_Assessment"
        ],

        "08_Constructive_Work_and_Social_Reforms": [
            "Khadi",
            "Village_Industries",
            "Harijan_Welfare",
            "Women_Upliftment",
            "Basic_Education",
            "Communal_Harmony",
            "Temperance",
            "Constructive_Programme"
        ],

        "09_Simon_Commission": [
            "Appointment",
            "Boycott",
            "All_India_Protests",
            "Lala_Lajpat_Rai",
            "Political_Reactions",
            "Constitutional_Debate",
            "Impact_on_Nationalism",
            "Historical_Significance"
        ],

        "10_Nehru_Report_and_Response": [
            "Motilal_Nehru",
            "Constitutional_Proposals",
            "Dominion_Status",
            "Jinnahs_Objections",
            "Fourteen_Points",
            "Political_Debates",
            "Congress_Response",
            "Historical_Impact"
        ],

        "11_Purna_Swaraj_Resolution": [
            "Lahore_Session_1929",
            "Jawaharlal_Nehru",
            "Declaration_of_Independence",
            "26_January_1930",
            "National_Flag",
            "Congress_Strategy",
            "Mass_Mobilization",
            "Historical_Significance"
        ],

        "12_Civil_Disobedience_Movement": [
            "Launch_of_Movement",
            "Salt_Satyagraha",
            "Dandi_March",
            "Nationwide_Protests",
            "Mass_Participation",
            "Regional_Variations",
            "Government_Repression",
            "Historical_Assessment"
        ],

        "13_Gandhi_Irwin_Pact_and_Round_Table": [
            "Gandhi_Irwin_Pact",
            "First_Round_Table_Conference",
            "Second_Round_Table_Conference",
            "Third_Round_Table_Conference",
            "London_Negotiations",
            "Political_Expectations",
            "Outcomes",
            "Historical_Assessment"
        ],

        "14_Communal_Award_and_Poona_Pact": [
            "Communal_Award",
            "Separate_Electorates",
            "Ambedkar_Position",
            "Gandhi_Fast",
            "Poona_Pact",
            "Depressed_Classes",
            "Political_Consequences",
            "Historical_Significance"
        ],

        "15_Government_of_India_Act_1935": [
            "Background",
            "Federal_Scheme",
            "Provincial_Autonomy",
            "Dyarchy_Abolition",
            "Electoral_Provisions",
            "Limitations",
            "Political_Response",
            "Historical_Importance"
        ],

        "16_Congress_Ministries_1937_1939": [
            "Provincial_Elections",
            "Congress_Governments",
            "Administrative_Reforms",
            "Mass_Contact",
            "Achievements",
            "Limitations",
            "Resignation_1939",
            "Historical_Assessment"
        ],

        "17_National_Movement_and_World_War_II": [
            "Outbreak_of_War",
            "Congress_Response",
            "Muslim_League_Response",
            "August_Offer",
            "Political_Debates",
            "War_Time_Politics",
            "Nationalist_Strategy",
            "Historical_Impact"
        ],

        "18_Individual_Satyagraha": [
            "Background",
            "Vinoba_Bhave",
            "Jawaharlal_Nehru",
            "Objectives",
            "Methodology",
            "Government_Response",
            "Political_Significance",
            "Historical_Assessment"
        ],

        "19_Cripps_Mission": [
            "Background",
            "Cripps_Proposals",
            "Congress_Response",
            "League_Response",
            "Reasons_for_Failure",
            "Constitutional_Implications",
            "Political_Impact",
            "Historical_Assessment"
        ],

        "20_Quit_India_Movement": [
            "Quit_India_Resolution",
            "Do_or_Die",
            "Mass_Uprising",
            "Parallel_Governments",
            "Underground_Activities",
            "Government_Repression",
            "Popular_Participation",
            "Historical_Assessment"
        ],

        "21_Subhas_Chandra_Bose": [
            "Political_Career",
            "Congress_Presidency",
            "Forward_Bloc",
            "Ideological_Differences",
            "Escape_from_India",
            "International_Diplomacy",
            "Leadership",
            "Legacy"
        ],

        "22_Indian_National_Army": [
            "Rashbehari_Bose",
            "INA_Reorganization",
            "Azad_Hind_Government",
            "Military_Campaigns",
            "INA_Trials",
            "Public_Reaction",
            "Military_Impact",
            "Historical_Significance"
        ],

        "23_Muslim_League_and_Pakistan_Demand": [
            "Growth_of_Muslim_League",
            "Lahore_Resolution_1940",
            "Two_Nation_Theory",
            "Jinnahs_Leadership",
            "Political_Mobilization",
            "League_Strategy",
            "Communal_Politics",
            "Historical_Assessment"
        ],

        "24_Final_Constitutional_Negotiations": [
            "Wavell_Plan",
            "Shimla_Conference",
            "Cabinet_Mission",
            "Interim_Government",
            "Constituent_Assembly",
            "Attlee_Declaration",
            "Political_Negotiations",
            "Transfer_of_Power_Background"
        ],

        "25_Partition_and_Independence": [
            "Mountbatten_Plan",
            "Indian_Independence_Act_1947",
            "Partition_of_India",
            "Boundary_Commissions",
            "Communal_Violence",
            "Refugee_Crisis",
            "Transfer_of_Power",
            "Historical_Consequences"
        ],

        "26_Historiography": [
            "Nationalist_View",
            "Cambridge_School",
            "Marxist_Interpretation",
            "Subaltern_Studies",
            "Gandhi_Debates",
            "Congress_vs_League",
            "Revisionist_Views",
            "Modern_Assessment"
        ],

        "27_Sources": [
            "Congress_Records",
            "Collected_Works_of_Gandhi",
            "Government_Records",
            "Newspapers",
            "Personal_Correspondence",
            "League_Documents",
            "Memoirs",
            "Source_Criticism"
        ],

        "28_Legacy_and_Historical_Significance": [
            "Mass_Nationalism",
            "Democratic_Traditions",
            "Non_Violent_Struggle",
            "Constitutional_Legacy",
            "Political_Mobilization",
            "Social_Transformation",
            "Global_Influence",
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

    print(f"Creating Gandhian Era (1919-1947) structure in: {target_base}")
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
    create_gandhian_era_1919_1947_structure()