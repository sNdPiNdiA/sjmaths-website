import os
import shutil

def create_magadha_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "magadha")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction": [
            "Meaning_of_Magadha", "Location_of_Magadha", "Sources_of_Magadha_History",
            "Historical_Background", "Importance_of_Magadha", "Geography_of_Magadha"
        ],
        "02_Rise_of_Magadha": [
            "Geographical_Factors", "Iron_Resources", "Fertile_Land", "River_Network",
            "Forest_Resources", "Elephant_Resources", "Strategic_Location", "Causes_of_Rise"
        ],
        "03_Haryanka_Dynasty": [
            "Bimbisara", "Expansion_Policy", "Matrimonial_Alliances", "Administration",
            "Ajatashatru", "Wars_with_Vajji", "Military_Innovations", "Achievements"
        ],
        "04_Shishunaga_Dynasty": [
            "Shishunaga", "Capital_Shift", "Avanti_Annexation", "Administration", "Achievements"
        ],
        "05_Nanda_Dynasty": [
            "Mahapadma_Nanda", "Expansion_of_Empire", "Administration", "Economy",
            "Military_Power", "Dhana_Nanda", "Decline_of_Nandas"
        ],
        "06_Magadha_Administration": [
            "Kingship", "Bureaucracy", "Revenue_System", "Taxation", "Justice_System",
            "Provincial_Administration", "Military_Administration"
        ],
        "07_Magadha_Economy": [
            "Agriculture", "Trade", "Commerce", "Guilds", "Coinage",
            "Urbanization", "Resource_Base", "Economic_Prosperity"
        ],
        "08_Society_and_Culture": [
            "Social_Structure", "Varna_System", "Urban_Life", "Rural_Life",
            "Position_of_Women", "Education", "Cultural_Life"
        ],
        "09_Religion_and_Philosophy": [
            "Buddhism_in_Magadha", "Jainism_in_Magadha", "Brahmanism",
            "Religious_Patronage", "Shramana_Traditions", "Religious_Developments"
        ],
        "10_Capitals_of_Magadha": [
            "Rajagriha", "Pataliputra", "Strategic_Importance", "Urban_Development", "Political_Importance"
        ],
        "11_Military_and_Expansion": [
            "Army", "War_Elephants", "Weapons", "Conquests", "Annexation_of_Anga",
            "Wars_with_Kosala", "Wars_with_Vajji", "Expansion_Strategies"
        ],
        "12_Important_Personalities": [
            "Bimbisara", "Ajatashatru", "Shishunaga", "Kalashoka",
            "Mahapadma_Nanda", "Dhana_Nanda", "Chanakya_and_Magadha"
        ],
        "13_Sources_and_Archaeology": [
            "Buddhist_Sources", "Jain_Sources", "Greek_Accounts",
            "Archaeological_Evidence", "Excavations", "Coins", "Material_Culture"
        ],
        "14_Transition_to_Mauryan_Empire": [
            "Fall_of_Nandas", "Chandragupta_Maurya", "Chanakya",
            "Foundation_of_Mauryan_Empire", "Historical_Transition"
        ],
        "15_Comparative_Studies": [
            "Magadha_vs_Kosala", "Magadha_vs_Avanti", "Bimbisara_vs_Ajatashatru",
            "Haryanka_vs_Nanda", "Republics_vs_Magadha", "Political_Comparisons"
        ],
        "16_Legacy_and_Significance": [
            "Political_Unification", "Imperial_Tradition", "Economic_Legacy",
            "Religious_Legacy", "Foundation_of_Mauryan_Empire", "Historical_Significance"
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
        "pyq_railway.json", "pyq_state_pcs.json", "interview.json",
        "flashcards.json", "revision_questions.json", "concept_traps.json"
    ]

    print(f"Creating Magadha structure in: {target_base}")
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
    create_magadha_structure()