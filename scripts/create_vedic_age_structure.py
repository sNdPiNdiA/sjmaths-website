import os
import shutil

def create_vedic_age_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "vedic-age")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Sources": [
            "Meaning_of_Vedic_Age", "Discovery_of_Vedic_Culture",
            "Sources_of_Vedic_History", "Literary_Sources",
            "Archaeological_Sources", "Vedic_Literature_Overview",
            "Chronology_of_Vedic_Age", "Importance_of_Vedic_Age"
        ],
        "02_Aryans_and_Origin_Debate": [
            "Aryans", "Aryan_Homeland_Theory", "Aryan_Migration_Theory",
            "Indigenous_Aryan_Theory", "Aryan_Invasion_Debate",
            "Linguistic_Evidence", "Archaeological_Evidence", "Modern_Debates"
        ],
        "03_Rig_Vedic_Period": [
            "Rig_Vedic_Chronology", "Geography_of_Rig_Vedic_Age",
            "Political_Life", "Social_Life", "Economic_Life",
            "Religious_Life", "Family_System", "Assemblies",
            "Tribal_Organization", "Characteristics_of_Rig_Vedic_Age"
        ],
        "04_Later_Vedic_Period": [
            "Expansion_to_Ganga_Valley", "Political_Changes", "Social_Changes",
            "Economic_Changes", "Religious_Changes", "Rise_of_Kingdoms",
            "Territorial_States", "Iron_Usage", "Characteristics_of_Later_Vedic_Age"
        ],
        "05_Vedic_Literature": [
            "Rigveda", "Samaveda", "Yajurveda", "Atharvaveda",
            "Brahmanas", "Aranyakas", "Upanishads", "Vedangas",
            "Sutra_Literature", "Epics_and_Vedic_Tradition", "Literary_Significance"
        ],
        "06_Political_Organization": [
            "Rajan", "Kingship", "Sabha", "Samiti", "Vidatha", "Gana",
            "Jana", "Tribal_Administration", "Taxation", "Evolution_of_State"
        ],
        "07_Society": [
            "Family", "Patriarchal_System", "Position_of_Women", "Marriage",
            "Education", "Varna_System", "Ashrama_System", "Social_Divisions",
            "Social_Changes", "Daily_Life"
        ],
        "08_Economy": [
            "Pastoral_Economy", "Agriculture", "Cattle_Wealth", "Trade",
            "Barter_System", "Crafts", "Occupations", "Land_Ownership",
            "Economic_Changes", "Iron_and_Economy"
        ],
        "09_Religion_and_Philosophy": [
            "Nature_Worship", "Indra", "Agni", "Varuna", "Soma", "Rudra",
            "Vishnu", "Prajapati", "Yajnas", "Sacrifices", "Concept_of_Rita",
            "Concept_of_Dharma", "Concept_of_Karma", "Concept_of_Moksha",
            "Philosophical_Development"
        ],
        "10_Upanishadic_Thought": [
            "Brahman", "Atman", "Tat_Tvam_Asi", "Karma_Doctrine", "Rebirth",
            "Moksha", "Knowledge_and_Liberation", "Major_Upanishads",
            "Philosophical_Significance"
        ],
        "11_Science_and_Knowledge": [
            "Mathematics", "Astronomy", "Medicine", "Geometry",
            "Sulba_Sutras", "Calendar_System", "Knowledge_System",
            "Scientific_Contributions"
        ],
        "12_Art_and_Culture": [
            "Music", "Dance", "Oral_Tradition", "Education_System",
            "Gurukul_System", "Cultural_Practices", "Festivals", "Cultural_Legacy"
        ],
        "13_Geography_of_Vedic_Age": [
            "Sapta_Sindhu", "Saraswati", "Indus_Region", "Ganga_Yamuna_Doab",
            "Expansion_Eastward", "Rivers_in_Vedas", "Regions_Mentioned_in_Vedas",
            "Geographical_Changes"
        ],
        "14_Important_Battles_and_Events": [
            "Battle_of_Ten_Kings", "Tribal_Conflicts", "Expansion_of_Aryans",
            "Political_Developments", "Major_Historical_Events"
        ],
        "15_Archaeology_and_Material_Culture": [
            "Painted_Grey_Ware", "Black_and_Red_Ware", "Iron_Artifacts",
            "Settlement_Patterns", "Material_Culture", "Archaeological_Sites",
            "Archaeological_Debates"
        ],
        "16_Transition_and_Transformation": [
            "Rig_Vedic_to_Later_Vedic", "Rise_of_Mahajanapadas",
            "Urbanization_Process", "Religious_Transformation",
            "Social_Transformation", "Political_Transformation"
        ],
        "17_Comparative_Studies": [
            "Rig_Vedic_vs_Later_Vedic", "Vedic_vs_Harappan",
            "Vedic_vs_Buddhist", "Vedic_vs_Jain", "Political_Comparison",
            "Religious_Comparison", "Social_Comparison"
        ],
        "18_Historiography": [
            "Interpretations_of_Vedic_Age", "Aryan_Debate",
            "Literary_vs_Archaeological_Evidence", "Colonial_Historiography",
            "Nationalist_Historiography", "Contemporary_Research"
        ],
        "19_Legacy_and_Significance": [
            "Legacy_of_Vedas", "Foundation_of_Indian_Culture", "Social_Legacy",
            "Religious_Legacy", "Political_Legacy", "Philosophical_Legacy",
            "Contribution_to_Indian_Civilization"
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

    print(f"Creating Vedic Age structure in: {target_base}")
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
    create_vedic_age_structure()