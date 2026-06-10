import os
import shutil

def create_governors_general_and_viceroys_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "governors-general-and-viceroys")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Evolution": [
            "East_India_Company_Administration",
            "Governor_of_Presidencies",
            "Governor_General_System",
            "Viceroy_System",
            "Government_of_India_Act_1858",
            "Administrative_Evolution",
            "Powers_and_Functions",
            "Sources_of_Study"
        ],

        "02_Robert_Clive": [
            "Battle_of_Plassey",
            "Battle_of_Buxar",
            "Dual_Government",
            "Diwani_Rights",
            "Military_Reforms",
            "Administrative_Measures",
            "Relations_with_Nawabs",
            "Historical_Assessment"
        ],

        "03_Warren_Hastings": [
            "Regulating_Act_1773",
            "Judicial_Reforms",
            "Revenue_Reforms",
            "Rohilla_War",
            "First_Anglo_Maratha_War",
            "Second_Anglo_Mysore_War",
            "Administrative_Reorganization",
            "Impeachment"
        ],

        "04_Cornwallis": [
            "Cornwallis_Code",
            "Permanent_Settlement",
            "Civil_Service_Reforms",
            "Police_Reforms",
            "Judicial_Reforms",
            "Third_Anglo_Mysore_War",
            "Administrative_Policies",
            "Historical_Assessment"
        ],

        "05_John_Shore_and_Wellesley": [
            "Policy_of_Non_Intervention",
            "Subsidiary_Alliance",
            "Fourth_Anglo_Mysore_War",
            "Second_Anglo_Maratha_War",
            "Expansion_of_British_Power",
            "Fort_William_College",
            "Diplomatic_Policies",
            "Historical_Assessment"
        ],

        "06_Hastings_and_Amherst": [
            "Gurkha_War",
            "Third_Anglo_Maratha_War",
            "Pindari_Campaign",
            "First_Burmese_War",
            "Territorial_Expansion",
            "Administrative_Policies",
            "Foreign_Policy",
            "Historical_Impact"
        ],

        "07_Bentinck": [
            "Abolition_of_Sati",
            "English_Education",
            "Macaulays_Minute",
            "Financial_Reforms",
            "Judicial_Reforms",
            "Suppression_of_Thuggee",
            "Administrative_Efficiency",
            "Historical_Assessment"
        ],

        "08_Auckland_to_Hardinge": [
            "First_Afghan_War",
            "Ellenborough_Policies",
            "Sindh_Annexation",
            "First_Anglo_Sikh_War",
            "Treaty_of_Lahore",
            "Military_Developments",
            "Expansionist_Policies",
            "Historical_Impact"
        ],

        "09_Dalhousie": [
            "Doctrine_of_Lapse",
            "Railways",
            "Telegraph",
            "Postal_System",
            "Public_Works",
            "Second_Anglo_Sikh_War",
            "Annexation_of_Awadh",
            "Historical_Assessment"
        ],

        "10_1857_and_Canning": [
            "Revolt_of_1857",
            "Causes_of_Revolt",
            "Suppression_of_Revolt",
            "Government_of_India_Act_1858",
            "Queens_Proclamation",
            "Army_Reorganization",
            "Administrative_Changes",
            "Historical_Significance"
        ],

        "11_Elgin_to_Mayo": [
            "Wahabi_Movement",
            "Frontier_Policy",
            "Mayo_College",
            "Financial_Decentralization",
            "Administrative_Reforms",
            "Provincial_Administration",
            "Statistical_Surveys",
            "Historical_Assessment"
        ],

        "12_Northbrook_and_Lytton": [
            "Second_Afghan_War",
            "Delhi_Durbar_1877",
            "Vernacular_Press_Act",
            "Arms_Act",
            "Famine_Policy",
            "Imperialism",
            "Economic_Policies",
            "Historical_Assessment"
        ],

        "13_Ripon": [
            "Local_Self_Government",
            "Ilbert_Bill",
            "Factory_Act_1881",
            "Press_Freedom",
            "Educational_Reforms",
            "Administrative_Liberalism",
            "Relations_with_Indians",
            "Historical_Assessment"
        ],

        "14_Dufferin_and_Lansdowne": [
            "Formation_of_INC",
            "Third_Burmese_War",
            "Indian_Councils_Act_1892",
            "Frontier_Policy",
            "Durand_Line",
            "Administrative_Reforms",
            "Imperial_Defence",
            "Historical_Impact"
        ],

        "15_Elgin_II_and_Curzon": [
            "Partition_of_Bengal",
            "Universities_Act_1904",
            "Police_Commission",
            "Ancient_Monuments_Act",
            "Calcutta_Corporation_Act",
            "North_West_Frontier_Province",
            "Administrative_Centralization",
            "Historical_Assessment"
        ],

        "16_Minto_and_Hardinge": [
            "Morley_Minto_Reforms",
            "Separate_Electorates",
            "Delhi_Durbar_1911",
            "Transfer_of_Capital_to_Delhi",
            "Annulment_of_Bengal_Partition",
            "Revolutionary_Activities",
            "Political_Reforms",
            "Historical_Impact"
        ],

        "17_Chelmsford": [
            "Montagu_Chelmsford_Reforms",
            "Government_of_India_Act_1919",
            "Dyarchy",
            "Rowlatt_Act",
            "Jallianwala_Bagh",
            "Khilafat_Background",
            "Administrative_Reforms",
            "Historical_Assessment"
        ],

        "18_Reading": [
            "Non_Cooperation_Aftermath",
            "Chauri_Chaura",
            "Swarajists",
            "Communal_Developments",
            "Economic_Issues",
            "Political_Negotiations",
            "Administrative_Policies",
            "Historical_Impact"
        ],

        "19_Irwin": [
            "Simon_Commission_Context",
            "Irwin_Declaration",
            "Civil_Disobedience_Movement",
            "Dandi_March_Context",
            "Gandhi_Irwin_Pact",
            "First_Round_Table_Conference",
            "Political_Negotiations",
            "Historical_Assessment"
        ],

        "20_Willingdon": [
            "Civil_Disobedience_Suppression",
            "Second_Round_Table_Conference",
            "Third_Round_Table_Conference",
            "Communal_Award",
            "Poona_Pact_Context",
            "Repressive_Measures",
            "Political_Control",
            "Historical_Impact"
        ],

        "21_Linlithgow": [
            "Government_of_India_Act_1935_Implementation",
            "Provincial_Autonomy",
            "Second_World_War",
            "August_Offer",
            "Individual_Satyagraha",
            "Cripps_Mission",
            "Quit_India_Background",
            "Historical_Assessment"
        ],

        "22_Wavell": [
            "Quit_India_Aftermath",
            "Wavell_Plan",
            "Shimla_Conference",
            "INA_Trials",
            "Post_War_Politics",
            "Communal_Tensions",
            "Administrative_Challenges",
            "Historical_Impact"
        ],

        "23_Mountbatten": [
            "Cabinet_Mission_Context",
            "Mountbatten_Plan",
            "Indian_Independence_Act_1947",
            "Partition_of_India",
            "Transfer_of_Power",
            "Princely_States_Context",
            "Administrative_Transition",
            "Historical_Assessment"
        ],

        "24_Administrative_and_Constitutional_Acts": [
            "Regulating_Act_1773",
            "Pitts_India_Act_1784",
            "Charter_Acts",
            "Government_of_India_Acts",
            "Indian_Councils_Acts",
            "Constitutional_Evolution",
            "Centralization_and_Decentralization",
            "Administrative_Legacy"
        ],

        "25_Economic_and_Revenue_Policies": [
            "Permanent_Settlement",
            "Ryotwari_System",
            "Mahalwari_System",
            "Commercialization_of_Agriculture",
            "Drain_of_Wealth",
            "Industrial_Impact",
            "Infrastructure_Development",
            "Economic_Legacy"
        ],

        "26_Education_and_Social_Reforms": [
            "English_Education",
            "Woods_Despatch",
            "Universities",
            "Social_Legislation",
            "Women_Reforms",
            "Missionary_Influence",
            "Educational_Expansion",
            "Social_Impact"
        ],

        "27_Sources_and_Historiography": [
            "Official_Records",
            "Parliamentary_Papers",
            "Administrative_Correspondence",
            "Colonial_Historiography",
            "Nationalist_Historiography",
            "Marxist_Interpretations",
            "Cambridge_School",
            "Modern_Research"
        ],

        "28_Legacy_and_Historical_Assessment": [
            "Colonial_State_Formation",
            "Administrative_Legacy",
            "Political_Legacy",
            "Economic_Legacy",
            "Educational_Legacy",
            "Social_Legacy",
            "Nationalist_Critique",
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

    print(f"Creating Governors General and Viceroys structure in: {target_base}")
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
    create_governors_general_and_viceroys_structure()