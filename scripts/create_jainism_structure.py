import os
import shutil

def create_jainism_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "jainism")

    # Delete older folders if they exist
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of subfolders to their respective files
    structure = {
        "01_Origins_and_Background": [
            "Meaning_of_Jainism", "Jina_and_Tirthankara", "Historical_Background",
            "Shramana_Tradition", "Religious_Conditions", "Social_Conditions",
            "Economic_Conditions", "Rise_of_Jainism", "Causes_of_Popularity",
            "Spread_of_Jainism", "Decline_of_Jainism", "Legacy_of_Jainism"
        ],
        "02_Tirthankaras": [
            "Overview_24_Tirthankaras", "Rishabhanatha", "Ajitanatha", "Sambhavanatha",
            "Abhinandananatha", "Sumatinatha", "Padmaprabha", "Suparshvanatha",
            "Chandraprabha", "Pushpadanta", "Shitalanatha", "Shreyansanatha",
            "Vasupujya", "Vimalanatha", "Anantanatha", "Dharmanatha", "Shantinatha",
            "Kunthunatha", "Aranatha", "Mallinatha", "Munisuvrata", "Naminatha",
            "Neminatha", "Parshvanatha", "Mahavira"
        ],
        "03_Mahavira": [
            "Birth_and_Family", "Early_Life", "Renunciation", "Penance",
            "Kevala_Jnana", "Teachings", "Five_Vows", "Sangha",
            "Mahavira_and_Contemporaries", "Nirvana", "Contribution"
        ],
        "04_Parshvanatha": [
            "Life_of_Parshvanatha", "Four_Vows", "Teachings",
            "Historical_Significance", "Parshvanatha_vs_Mahavira"
        ],
        "05_Core_Doctrines": [
            "Ahimsa", "Aparigraha", "Anekantavada", "Syadvada", "Nayavada",
            "Karma", "Moksha", "Triratna", "Jiva", "Ajiva", "Jiva_Ajiva",
            "Mahavratas", "Anuvratas", "Sallekhana", "Kevala_Jnana", "Tattvas",
            "Dravya_Theory", "Gunasthanas", "Jain_Ethics", "Jain_Epistemology"
        ],
        "06_Sects_and_Schools": [
            "Digambara", "Shvetambara", "Sthanakvasi", "Terapanthi",
            "Digambara_vs_Shvetambara", "Sectarian_Differences", "Evolution_of_Sects"
        ],
        "07_Councils_and_Assemblies": [
            "Pataliputra_Council", "Vallabhi_Council", "Council_Chronology",
            "Preservation_of_Scriptures", "Causes_of_Councils", "Outcomes_of_Councils"
        ],
        "08_Literature_and_Texts": [
            "Agamas", "Angas", "Upangas", "Kalpasutra", "Tattvartha_Sutra",
            "Prakrit_Literature", "Sanskrit_Literature", "Hemachandra",
            "Jain_Authors", "Literary_Contributions"
        ],
        "09_Art_and_Architecture": [
            "Jain_Temple_Architecture", "Dilwara_Temples", "Ranakpur_Temple",
            "Palitana", "Shatrunjaya", "Shravanabelagola", "Gommateshwara",
            "Udayagiri_Khandagiri", "Jain_Caves", "Jain_Sculpture",
            "Jain_Paintings", "Architectural_Contributions"
        ],
        "10_Patronage_and_Rulers": [
            "Chandragupta_Maurya", "Bhadrabahu", "Samprati", "Kharavela",
            "Western_Ganga_Dynasty", "Rashtrakutas", "Chalukyas", "Hoysalas",
            "Merchant_Communities", "Royal_Patronage", "Regional_Patronage"
        ],
        "11_Sacred_Geography": [
            "Pavapuri", "Kundagrama", "Rajgir", "Girnar", "Shatrunjaya",
            "Palitana", "Shravanabelagola", "Mount_Abu", "Sammed_Shikharji",
            "Major_Pilgrimage_Sites", "Sacred_Geography"
        ],
        "12_Spread_of_Jainism": [
            "Bihar", "Gujarat", "Rajasthan", "Karnataka", "Maharashtra",
            "Tamil_Nadu", "North_India", "South_India", "Western_India", "Global_Spread"
        ],
        "13_Society_and_Culture": [
            "Jain_Monastic_System", "Lay_Followers", "Festivals", "Paryushana",
            "Mahavir_Jayanti", "Jain_Dietary_Practices", "Vegetarianism",
            "Education", "Social_Impact"
        ],
        "14_Comparative_Studies": [
            "Jainism_vs_Buddhism", "Jainism_vs_Hinduism", "Mahavira_vs_Buddha",
            "Karma_Comparison", "Liberation_Comparison", "Ahimsa_Comparison",
            "Soul_Concept_Comparison", "Philosophical_Comparison"
        ],
        "15_Modern_Relevance": [
            "Ahimsa_and_Peace", "Environmental_Ethics", "Sustainable_Living",
            "Aparigraha_and_Consumerism", "Conflict_Resolution",
            "Jainism_in_Modern_India", "Jain_Communities_Today", "Global_Relevance"
        ]
    }

    leaf_files = [
        "facts.json", "one_liner.json", "mcq.json", "multiple_statement.json",
        "assertion_reason.json", "match_following.json", "fill_blanks.json",
        "true_false.json", "chronology.json", "pair_matching.json",
        "odd_one_out.json", "short_answer.json", "long_answer.json",
        "pyq_inspired.json", "interview.json"
    ]

    print(f"Creating Jainism structure in: {target_base}")
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
    create_jainism_structure()