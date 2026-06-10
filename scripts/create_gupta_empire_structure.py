import os
import shutil

def create_gupta_empire_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "gupta-empire")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_and_Rise": [
            "Historical_Background", "Post_Kushan_Period", "Post_Satavahana_Period",
            "Political_Conditions", "Rise_of_Guptas", "Origin_of_Guptas",
            "Homeland_of_Guptas", "Gupta_Lineage", "Sources_of_Gupta_History",
            "Importance_of_Gupta_Empire"
        ],
        "02_Early_Gupta_Rulers": [
            "Sri_Gupta", "Ghatotkacha", "Chandragupta_I",
            "Lichchhavi_Marriage_Alliance", "Gupta_Era", "Expansion_of_Early_Guptas"
        ],
        "03_Samudragupta": [
            "Accession", "Prayaga_Prasasti", "Allahabad_Pillar_Inscription",
            "Aryavarta_Campaigns", "Dakshinapatha_Campaigns", "Frontier_States",
            "Foreign_Relations", "Ashvamedha_Yajna", "Administration",
            "Coins_of_Samudragupta", "Napoleon_of_India"
        ],
        "04_Chandragupta_II_Vikramaditya": [
            "Accession", "Western_Kshatrapas", "Conquests", "Ujjain",
            "Vikramaditya", "Trade_and_Commerce", "Fa_Hien",
            "Coins_of_Chandragupta_II", "Administration", "Cultural_Achievements"
        ],
        "05_Kumaragupta_I": [
            "Reign", "Administration", "Coinage", "Nalanda_University", "Achievements"
        ],
        "06_Skandagupta": [
            "Accession", "Hun_Invasions", "Junagadh_Inscription",
            "Military_Achievements", "Administration", "Decline_Begins"
        ],
        "07_Later_Guptas": [
            "Purugupta", "Narasimhagupta", "Kumaragupta_II", "Budhagupta",
            "Weak_Successors", "End_of_Gupta_Rule"
        ],
        "08_Political_History": [
            "Territorial_Expansion", "Military_Organization", "Foreign_Policy",
            "Diplomatic_Relations", "Frontier_Policy", "Political_Unification"
        ],
        "09_Administration": [
            "Kingship", "Central_Administration", "Provincial_Administration",
            "District_Administration", "Village_Administration", "Officials",
            "Feudal_Tendencies", "Revenue_System", "Judicial_System",
            "Military_Administration"
        ],
        "10_Economy": [
            "Agriculture", "Land_Revenue", "Irrigation", "Trade",
            "Internal_Trade", "Foreign_Trade", "Guilds", "Coinage",
            "Taxation", "Economic_Prosperity"
        ],
        "11_Society": [
            "Varna_System", "Caste_System", "Position_of_Women", "Marriage",
            "Education", "Social_Life", "Food_and_Dress", "Urban_Life",
            "Rural_Life", "Social_Changes"
        ],
        "12_Religion": [
            "Brahmanism", "Vaishnavism", "Shaivism", "Buddhism", "Jainism",
            "Religious_Tolerance", "Temple_Worship", "Bhakti_Tradition",
            "Religious_Developments"
        ],
        "13_Literature": [
            "Sanskrit_Literature", "Kalidasa", "Raghuvamsha", "Kumarasambhava",
            "Meghaduta", "Abhijnanasakuntalam", "Vishakhadatta", "Mudrarakshasa",
            "Puranas", "Smritis", "Literary_Achievements"
        ],
        "14_Science_and_Technology": [
            "Aryabhata", "Aryabhatiya", "Decimal_System", "Concept_of_Zero",
            "Astronomy", "Mathematics", "Varahamihira", "Brihat_Samhita",
            "Medicine", "Metallurgy", "Iron_Pillar_of_Delhi", "Scientific_Achievements"
        ],
        "15_Art_and_Architecture": [
            "Gupta_Art", "Gupta_Sculpture", "Gupta_Temples", "Dashavatara_Temple",
            "Deogarh_Temple", "Cave_Architecture", "Ajanta_Paintings",
            "Sarnath_School", "Mathura_School", "Temple_Architecture",
            "Artistic_Achievements"
        ],
        "16_Education_and_Universities": [
            "Nalanda", "Taxila", "Buddhist_Education", "Brahmanical_Education",
            "Gurukul_System", "Learning_Centers"
        ],
        "17_Important_Sources": [
            "Allahabad_Pillar_Inscription", "Mehrauli_Iron_Pillar",
            "Junagadh_Inscription", "Bhitari_Inscription", "Eran_Inscription",
            "Coins", "Seals", "Fa_Hien_Accounts", "Literary_Sources",
            "Archaeological_Sources"
        ],
        "18_Foreign_Travellers": [
            "Fa_Hien", "Observations_of_Fa_Hien", "Society_Through_Fa_Hien",
            "Religion_Through_Fa_Hien", "Economy_Through_Fa_Hien"
        ],
        "19_Decline_of_Gupta_Empire": [
            "Hun_Invasions", "Weak_Successors", "Administrative_Decentralization",
            "Feudalism", "Economic_Problems", "Regional_Kingdoms", "Causes_of_Decline"
        ],
        "20_Golden_Age_Debate": [
            "Why_Golden_Age", "Arguments_in_Favour", "Arguments_Against",
            "Historiographical_Debate", "Legacy_of_Gupta_Age"
        ],
        "21_Comparative_Studies": [
            "Maurya_vs_Gupta", "Gupta_vs_Harsha", "Samudragupta_vs_Ashoka",
            "Gupta_Administration_Comparison", "Gupta_Economy_Comparison",
            "Gupta_Cultural_Achievements"
        ],
        "22_Modern_Relevance": [
            "Scientific_Legacy", "Mathematical_Contributions", "Cultural_Legacy",
            "Heritage_Sites", "Gupta_Art_in_Modern_India",
            "Relevance_in_History_Education"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq.json", "multiple_statement.json",
        "assertion_reason.json", "match_following.json", "fill_blanks.json",
        "true_false.json", "chronology.json", "pair_matching.json",
        "odd_one_out.json", "source_based.json", "map_based.json",
        "short_answer.json", "long_answer.json", "case_study.json",
        "pyq_inspired.json", "interview.json"
    ]

    print(f"Creating Gupta Empire structure in: {target_base}")
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
    create_gupta_empire_structure()