import os
import shutil

def create_post_mauryan_period_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "post-mauryan-period")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Background": [
            "Meaning_of_Post_Mauryan_Period", "Fall_of_Mauryan_Empire", "Political_Fragmentation",
            "Chronology", "Sources_of_History", "Literary_Sources",
            "Archaeological_Sources", "Foreign_Accounts", "Historical_Significance"
        ],
        "02_Sunga_Dynasty": [
            "Pushyamitra_Sunga", "Agnimitra", "Administration", "Military_Achievements",
            "Religion", "Art_and_Culture", "Foreign_Threats", "Economy", "Decline_of_Sungas"
        ],
        "03_Kanva_Dynasty": [
            "Vasudeva_Kanva", "Administration", "Political_History", "Successors",
            "Economy", "Religion", "Decline_of_Kanvas"
        ],
        "04_Indo_Greeks": [
            "Origin", "Demetrius", "Menander_Milinda", "Indo_Greek_Administration",
            "Coinage", "Religion", "Art", "Indo_Greek_Trade", "Decline"
        ],
        "05_Sakas": [
            "Origin_of_Sakas", "Western_Kshatrapas", "Rudradaman_I", "Junagadh_Inscription",
            "Administration", "Economy", "Coinage", "Culture", "Decline"
        ],
        "06_Parthians": [
            "Origin", "Gondophernes", "Administration", "Economy", "Coinage",
            "Foreign_Relations", "Decline"
        ],
        "07_Kushana_Empire": [
            "Origin_of_Kushanas", "Kujula_Kadphises", "Vima_Kadphises", "Kanishka",
            "Administration", "Economy", "Trade", "Coinage", "Religion", "Art", "Decline"
        ],
        "08_Satavahana_Dynasty": [
            "Simuka", "Gautamiputra_Satakarni", "Vashishthiputra_Pulumavi",
            "Administration", "Economy", "Trade", "Society", "Religion", "Coinage", "Decline"
        ],
        "09_Chera_Chola_Pandya": [
            "Cheras", "Cholas", "Pandyas", "Sangam_Age_Connections", "Trade",
            "Ports", "Society", "Economy", "Political_History"
        ],
        "10_Political_Developments": [
            "Regionalization_of_Power", "Foreign_Rulers_in_India", "Political_Map",
            "State_Formation", "Inter_Dynastic_Relations", "Political_Changes"
        ],
        "11_Economy_and_Trade": [
            "Internal_Trade", "Overseas_Trade", "Silk_Route", "Roman_Trade",
            "Ports", "Guilds", "Urbanization", "Coinage_System", "Economic_Prosperity"
        ],
        "12_Society": [
            "Social_Structure", "Varna_System", "Position_of_Women", "Urban_Society",
            "Rural_Society", "Social_Mobility", "Family_System", "Social_Changes"
        ],
        "13_Religion_and_Philosophy": [
            "Buddhism", "Mahayana_Buddhism", "Jainism", "Brahmanism", "Bhagavatism",
            "Shaivism", "Vaishnavism", "Religious_Syncretism", "Religious_Developments"
        ],
        "14_Buddhist_Councils": [
            "Fourth_Buddhist_Council", "Kanishka_and_Buddhism", "Mahayana_Development",
            "Buddhist_Scholars", "Historical_Impact"
        ],
        "15_Literature": [
            "Sangam_Literature", "Milindapanha", "Mahabhashya", "Gatha_Saptashati",
            "Buddhist_Texts", "Jain_Texts", "Sanskrit_Literature", "Literary_Developments"
        ],
        "16_Art_and_Architecture": [
            "Gandhara_Art", "Mathura_Art", "Amaravati_Art", "Stupas", "Chaityas",
            "Viharas", "Rock_Cut_Architecture", "Sculpture", "Artistic_Developments"
        ],
        "17_Important_Sites": [
            "Sanchi", "Bharhut", "Amaravati", "Karle", "Nasik", "Kanheri",
            "Taxila", "Mathura", "Nagarjunakonda"
        ],
        "18_Science_and_Technology": [
            "Metallurgy", "Shipbuilding", "Navigation", "Irrigation",
            "Craft_Technology", "Technological_Developments"
        ],
        "19_Foreign_Relations": [
            "Rome", "Central_Asia", "China", "Silk_Route", "Diplomatic_Contacts",
            "Cultural_Exchange", "International_Trade"
        ],
        "20_Important_Personalities": [
            "Pushyamitra_Sunga", "Menander", "Rudradaman", "Gondophernes",
            "Kanishka", "Gautamiputra_Satakarni", "Nagarjuna", "Patanjali"
        ],
        "21_Historiography": [
            "Sources_Debate", "Pushyamitra_Debate", "Roman_Trade_Debate",
            "Mahayana_Origins", "Foreign_Rulers_Debate", "Economic_Interpretations",
            "Modern_Research"
        ],
        "22_Comparative_Studies": [
            "Sunga_vs_Maurya", "Kushana_vs_Satavahana", "Gandhara_vs_Mathura",
            "Mahayana_vs_Hinayana", "Indo_Greek_vs_Saka", "Political_Comparisons"
        ],
        "23_Legacy_and_Significance": [
            "Political_Legacy", "Economic_Legacy", "Religious_Legacy",
            "Artistic_Legacy", "Trade_Legacy", "Cultural_Legacy", "Transition_to_Gupta_Age"
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

    print(f"Creating Post-Mauryan Period structure in: {target_base}")
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
    create_post_mauryan_period_structure()