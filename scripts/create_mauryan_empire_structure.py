import os
import shutil

def create_mauryan_empire_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "mauryan-empire")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Background": [
            "Meaning_of_Mauryan_Empire", "Historical_Background", "Fall_of_Nandas",
            "Rise_of_Mauryas", "Sources_of_Mauryan_History", "Literary_Sources",
            "Archaeological_Sources", "Foreign_Accounts", "Importance_of_Mauryan_Empire"
        ],
        "02_Foundation_of_Empire": [
            "Chandragupta_Maurya", "Chanakya", "Kautilya", "Overthrow_of_Nandas",
            "Establishment_of_Empire", "Early_Expansion", "Mauryan_Capital",
            "Formation_of_Centralized_State"
        ],
        "03_Chandragupta_Maurya": [
            "Early_Life", "Conquests", "Seleucus_Conflict", "Indo_Greek_Relations",
            "Administration", "Empire_Expansion", "Jain_Tradition", "Bhadrabahu",
            "Shravanabelagola", "Legacy"
        ],
        "04_Bindusara": [
            "Accession", "Expansion_Policy", "Administration", "Foreign_Relations",
            "Greek_Contacts", "Internal_Affairs", "Achievements"
        ],
        "05_Ashoka": [
            "Early_Life", "Accession", "Kalinga_War", "Conversion_to_Buddhism",
            "Dhamma", "Administration", "Foreign_Policy", "Missionary_Activities",
            "Third_Buddhist_Council", "Legacy"
        ],
        "06_Ashokan_Dhamma": [
            "Meaning_of_Dhamma", "Principles_of_Dhamma", "Moral_Values",
            "Religious_Tolerance", "Welfare_Measures", "Dhamma_Mahamatras",
            "Criticism_of_Dhamma", "Significance_of_Dhamma", "Dhamma_vs_Buddhism"
        ],
        "07_Mauryan_Administration": [
            "Nature_of_State", "Kingship", "Central_Administration", "Council_of_Ministers",
            "Provincial_Administration", "District_Administration", "Village_Administration",
            "Bureaucracy", "Espionage_System", "Administrative_Efficiency"
        ],
        "08_Economy": [
            "Agriculture", "Land_Revenue", "Irrigation", "Trade", "Internal_Trade",
            "Foreign_Trade", "Taxation", "Coinage", "Guilds", "Economic_Organization"
        ],
        "09_Society": [
            "Social_Structure", "Varna_System", "Position_of_Women", "Slavery",
            "Marriage", "Education", "Urban_Life", "Rural_Life", "Daily_Life"
        ],
        "10_Religion": [
            "Buddhism", "Jainism", "Brahmanism", "Ajivikas", "Religious_Tolerance",
            "Ashoka_and_Buddhism", "Buddhist_Missions", "Religious_Patronage", "Religious_Life"
        ],
        "11_Arthashastra": [
            "Kautilya", "Authorship_Debate", "Structure_of_Arthashastra",
            "Political_Theory", "Economic_Ideas", "Administration", "Diplomacy",
            "Warfare", "Historical_Importance"
        ],
        "12_Megasthenes_and_Indica": [
            "Megasthenes", "Indica", "Society_According_to_Indica",
            "Administration_According_to_Indica", "Economy_According_to_Indica",
            "Reliability_of_Indica", "Historical_Significance"
        ],
        "13_Edicts_and_Inscriptions": [
            "Major_Rock_Edicts", "Minor_Rock_Edicts", "Major_Pillar_Edicts",
            "Minor_Pillar_Edicts", "Separate_Edicts", "Kalinga_Edicts",
            "Languages_of_Edicts", "Scripts_of_Edicts", "Historical_Importance"
        ],
        "14_Art_and_Architecture": [
            "Mauryan_Art", "Mauryan_Polish", "Pillars", "Lion_Capital", "Stupas",
            "Barabar_Caves", "Rock_Cut_Architecture", "Sculpture", "Architecture",
            "Artistic_Legacy"
        ],
        "15_Science_and_Technology": [
            "Engineering", "Irrigation_Technology", "Road_Networks", "Urban_Planning",
            "Metallurgy", "Measurement_Systems", "Technological_Developments"
        ],
        "16_Foreign_Relations": [
            "Seleucid_Empire", "Hellenistic_World", "Sri_Lanka_Relations",
            "Central_Asia", "Diplomatic_Relations", "Trade_Relations", "International_Influence"
        ],
        "17_Military_System": [
            "Army", "Infantry", "Cavalry", "Chariots", "War_Elephants",
            "Military_Administration", "Defense_System", "Warfare_Strategies"
        ],
        "18_Important_Cities": [
            "Pataliputra", "Taxila", "Ujjain", "Tosali", "Suvarnagiri",
            "Administrative_Centers", "Urban_Development", "City_Life"
        ],
        "19_Decline_of_Mauryan_Empire": [
            "Weak_Successors", "Economic_Factors", "Administrative_Factors",
            "Provincial_Revolts", "Foreign_Pressures", "Historiographical_Debates",
            "Brihadratha", "Causes_of_Decline"
        ],
        "20_Post_Mauryan_Transition": [
            "Sungas", "Kanvas", "Regional_Kingdoms", "Political_Fragmentation",
            "Legacy_of_Mauryas", "Transition_to_Post_Mauryan_Age"
        ],
        "21_Important_Personalities": [
            "Chandragupta_Maurya", "Chanakya", "Bindusara", "Ashoka", "Mahinda",
            "Sanghamitta", "Megasthenes", "Brihadratha"
        ],
        "22_Comparative_Studies": [
            "Maurya_vs_Magadha", "Chandragupta_vs_Ashoka", "Arthashastra_vs_Indica",
            "Mauryan_vs_Gupta_Administration", "Mauryan_vs_Harappan_Urbanization",
            "Comparative_Imperial_Systems"
        ],
        "23_Historiography": [
            "Sources_Debate", "Ashoka_Debate", "Mauryan_State_Debate",
            "Economic_Interpretations", "Nationalist_Historiography",
            "Marxist_Interpretations", "Modern_Research"
        ],
        "24_Legacy_and_Significance": [
            "Political_Unification", "Administrative_Legacy", "Cultural_Legacy",
            "Buddhist_Legacy", "Art_and_Architecture_Legacy", "International_Influence",
            "Contribution_to_Indian_History"
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

    print(f"Creating Mauryan Empire structure in: {target_base}")
    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)
            for filename in leaf_files:
                with open(os.path.join(topic_path, filename), 'w', encoding='utf-8') as f:
                    f.write("[]")

if __name__ == "__main__":
    create_mauryan_empire_structure()