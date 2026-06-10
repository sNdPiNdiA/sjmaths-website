import os
import shutil

def create_post_gupta_period_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "post-gupta-period")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Background": [
            "Meaning_of_Post_Gupta_Period", "Chronology", "Fall_of_Gupta_Empire",
            "Political_Fragmentation", "Sources_of_History", "Literary_Sources",
            "Archaeological_Sources", "Foreign_Accounts", "Historical_Significance"
        ],
        "02_Transition_from_Guptas": [
            "Decline_of_Guptas", "Weak_Successors", "Hun_Invasions",
            "Regionalization_of_Power", "Administrative_Changes", "Economic_Changes",
            "Social_Changes", "Political_Consequences"
        ],
        "03_Huna_Invasions": [
            "Origin_of_Hunas", "Toramana", "Mihirakula", "Huna_Expansion",
            "Resistance_to_Hunas", "Yashodharman", "Impact_on_India", "Decline_of_Hunas"
        ],
        "04_Regional_Kingdoms": [
            "Rise_of_Regional_States", "Political_Map_of_India", "Regionalization",
            "Local_Dynasties", "Power_Struggles", "Territorial_Expansion", "Political_Developments"
        ],
        "05_Maukharis": [
            "Origin", "Harivarman", "Ishanavarman", "Kannauj", "Expansion",
            "Administration", "Decline"
        ],
        "06_Pushyabhuti_Dynasty": [
            "Origin", "Prabhakaravardhana", "Rajyavardhana", "Thanesar",
            "Rise_of_Dynasty", "Administration", "Importance"
        ],
        "07_Harshavardhana": [
            "Early_Life", "Accession", "Military_Campaigns", "Empire_of_Harsha",
            "Administration", "Religion", "Foreign_Relations", "Cultural_Patronage",
            "Assemblies_of_Harsha", "Legacy"
        ],
        "08_Harsha_Administration": [
            "Central_Administration", "Provincial_Administration", "Revenue_System",
            "Military_System", "Officials", "Local_Government", "Governance_Model"
        ],
        "09_Harsha_and_Xuanzang": [
            "Xuanzang", "Travels_in_India", "Account_of_Harsha",
            "Society_According_to_Xuanzang", "Religion_According_to_Xuanzang",
            "Economy_According_to_Xuanzang", "Historical_Importance"
        ],
        "10_Society": [
            "Social_Structure", "Varna_System", "Position_of_Women", "Education",
            "Urban_Life", "Rural_Life", "Social_Customs", "Social_Changes"
        ],
        "11_Economy": [
            "Agriculture", "Land_Grants", "Trade", "Guilds", "Taxation",
            "Coinage", "Economic_Decentralization", "Economic_Conditions"
        ],
        "12_Religion": [
            "Hinduism", "Buddhism", "Jainism", "Shaivism", "Vaishnavism",
            "Religious_Tolerance", "Religious_Institutions", "Religious_Developments"
        ],
        "13_Literature": [
            "Banabhatta", "Harshacharita", "Kadambari", "Harsha_as_Author",
            "Ratnavali", "Nagananda", "Priyadarshika", "Literary_Achievements"
        ],
        "14_Education_and_Universities": [
            "Nalanda", "Valabhi", "Buddhist_Education", "Brahmanical_Education",
            "Monastic_Centers", "Curriculum", "Educational_Institutions"
        ],
        "15_Art_and_Architecture": [
            "Temple_Architecture", "Sculpture", "Buddhist_Monuments",
            "Cave_Architecture", "Religious_Architecture", "Artistic_Developments",
            "Cultural_Legacy"
        ],
        "16_Land_Grant_System": [
            "Brahmadeya", "Agrahara", "Religious_Grants", "Administrative_Grants",
            "Impact_on_Economy", "Impact_on_Society", "Feudal_Tendencies"
        ],
        "17_Early_Indian_Feudalism": [
            "Concept_of_Feudalism", "Historiographical_Debate", "Landed_Intermediaries",
            "Decentralization", "Agrarian_Expansion", "Feudal_Structure", "Criticism_of_Feudal_Model"
        ],
        "18_Foreign_Relations": [
            "China_Relations", "Diplomatic_Missions", "Cultural_Exchange",
            "Central_Asia", "Buddhist_Connections", "International_Contacts"
        ],
        "19_Important_Personalities": [
            "Harshavardhana", "Banabhatta", "Xuanzang", "Mihirakula",
            "Toramana", "Yashodharman", "Prabhakaravardhana"
        ],
        "20_Post_Harsha_Political_Developments": [
            "Death_of_Harsha", "Collapse_of_Empire", "Rise_of_Regional_Powers",
            "Tripartite_Background", "Political_Fragmentation", "Transition_to_Early_Medieval_India"
        ],
        "21_Comparative_Studies": [
            "Gupta_vs_Post_Gupta", "Harsha_vs_Samudragupta", "Harsha_vs_Ashoka",
            "Gupta_vs_Harsha_Administration", "Gupta_vs_Post_Gupta_Economy", "Political_Comparisons"
        ],
        "22_Historiography": [
            "Sources_Debate", "Feudalism_Debate", "Harsha_Debate",
            "Economic_Interpretations", "Marxist_Interpretations",
            "Nationalist_Interpretations", "Modern_Research"
        ],
        "23_Legacy_and_Significance": [
            "Political_Legacy", "Religious_Legacy", "Educational_Legacy",
            "Cultural_Legacy", "Administrative_Legacy", "Transition_to_Early_Medieval_India",
            "Historical_Significance"
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

    print(f"Creating Post-Gupta Period structure in: {target_base}")
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
    create_post_gupta_period_structure()