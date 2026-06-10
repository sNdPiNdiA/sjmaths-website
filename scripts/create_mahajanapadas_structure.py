import os
import shutil

def create_mahajanapadas_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "mahajanapadas")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Background": [
            "Meaning_of_Mahajanapada", "Origin_of_Mahajanapadas", "Historical_Background",
            "Transition_from_Vedic_Age", "Second_Urbanization", "Sources_of_Information",
            "Buddhist_Sources", "Jain_Sources", "Literary_Sources", "Archaeological_Sources"
        ],
        "02_The_Sixteen_Mahajanapadas": [
            "Anga", "Magadha", "Kasi", "Kosala", "Vajji", "Malla", "Chedi", "Vatsa",
            "Kuru", "Panchala", "Matsya", "Surasena", "Assaka", "Avanti", "Gandhara", "Kamboja"
        ],
        "03_Geography": [
            "Geographical_Distribution", "Northern_Mahajanapadas", "Eastern_Mahajanapadas",
            "Western_Mahajanapadas", "Southern_Mahajanapadas", "River_Systems",
            "Trade_Routes", "Strategic_Locations"
        ],
        "04_Political_System": [
            "Monarchy", "Republics", "Gana_Sanghas", "Kingship", "Administration",
            "Assemblies", "Taxation", "Military_Organization"
        ],
        "05_Society": [
            "Social_Structure", "Varna_System", "Urban_Society", "Rural_Society",
            "Position_of_Women", "Family_System", "Education", "Social_Changes"
        ],
        "06_Economy": [
            "Agriculture", "Iron_Technology", "Trade", "Commerce", "Guilds",
            "Coinage", "Taxation", "Urbanization", "Economic_Growth"
        ],
        "07_Religion_and_Philosophy": [
            "Brahmanism", "Rise_of_Buddhism", "Rise_of_Jainism", "Shramana_Movements",
            "Religious_Changes", "Philosophical_Developments", "Religious_Tolerance"
        ],
        "08_Important_Republics": [
            "Vajji_Confederacy", "Licchavis", "Mallas", "Sakyas",
            "Republican_Institutions", "Gana_Rajya_System", "Importance_of_Republics"
        ],
        "09_Inter_State_Relations": [
            "Rivalries", "Alliances", "Territorial_Expansion", "Diplomatic_Relations",
            "Military_Conflicts", "Balance_of_Power"
        ],
        "10_Rise_of_Magadha": [
            "Geographical_Advantages", "Natural_Resources", "Political_Leadership",
            "Military_Strength", "Economic_Factors", "Expansion_Policy", "Importance_of_Magadha"
        ],
        "11_Archaeology_and_Sources": [
            "Literary_Evidence", "Buddhist_Texts", "Jain_Texts", "Puranic_References",
            "Archaeological_Findings", "Coins", "Material_Culture"
        ],
        "12_Comparative_Studies": [
            "Monarchy_vs_Republic", "Kosala_vs_Magadha", "Avanti_vs_Magadha",
            "Vajji_vs_Magadha", "Mahajanapadas_vs_Vedic_States", "Political_Comparisons"
        ],
        "13_Legacy_and_Significance": [
            "Political_Legacy", "Economic_Legacy", "Urbanization_Legacy",
            "Religious_Legacy", "Foundation_of_Empires", "Historical_Significance"
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

    print(f"Creating Mahajanapadas structure in: {target_base}")
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
    create_mahajanapadas_structure()