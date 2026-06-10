import os

def create_buddhism_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "buddhism")

    # Mapping of subfolders to their respective files
    structure = {
        "01_Origins_and_Background": [
            "Meaning_of_Buddhism", "Historical_Background", "Shramana_Tradition", 
            "Religious_Conditions", "Social_Conditions", "Economic_Conditions", 
            "Mahajanapadas", "Rise_of_Buddhism", "Causes_of_Popularity", 
            "Spread_of_Buddhism", "Decline_of_Buddhism", "Legacy_of_Buddhism"
        ],
        "02_Gautama_Buddha": [
            "Birth_and_Family", "Early_Life", "Four_Sights", "Great_Renunciation", 
            "Enlightenment", "Bodhi_Tree", "First_Sermon", "Teachings", "Sangha", 
            "Mahaparinirvana", "Important_Dates", "Contribution"
        ],
        "03_Core_Doctrines": [
            "Four_Noble_Truths", "Noble_Eightfold_Path", "Middle_Path", 
            "Dependent_Origination", "Karma", "Rebirth", "Nirvana", "Three_Jewels", 
            "Three_Marks_of_Existence", "Five_Precepts", "Ten_Precepts", 
            "Brahmaviharas", "Buddhist_Ethics", "Compassion_and_Metta"
        ],
        "04_Buddhist_Philosophy": [
            "Dukkha", "Anatman", "Anitya", "Pratityasamutpada", "Skandhas", 
            "Sunyata", "Madhyamaka", "Yogachara", "Abhidhamma", "Kshanikavada", 
            "Buddhist_Logic", "Buddhist_Epistemology"
        ],
        "05_Sects_and_Schools": [
            "Theravada", "Mahayana", "Vajrayana", "Hinayana", "Mahasanghika", 
            "Sarvastivada", "Zen", "Tibetan_Buddhism", "Theravada_vs_Mahayana", 
            "Mahayana_vs_Hinayana", "Evolution_of_Sects"
        ],
        "06_Councils": [
            "First_Council", "Second_Council", "Third_Council", "Fourth_Council", 
            "Council_Chronology", "Outcomes", "Preservation_of_Tripitaka"
        ],
        "07_Literature": [
            "Tripitaka", "Vinaya_Pitaka", "Sutta_Pitaka", "Abhidhamma_Pitaka", 
            "Jataka_Tales", "Milinda_Panha", "Mahavastu", "Lalitavistara", 
            "Pali_Literature", "Sanskrit_Buddhist_Texts", "Literary_Contributions"
        ],
        "08_Art_and_Architecture": [
            "Stupas", "Chaityas", "Viharas", "Sanchi", "Bharhut", "Amaravati", 
            "Dhamek_Stupa", "Ajanta", "Ellora", "Gandhara_School", "Mathura_School", 
            "Bamiyan_Buddhas", "Sculpture", "Paintings", "Architecture"
        ],
        "09_Patronage_and_Rulers": [
            "Ashoka", "Kanishka", "Harsha", "Menander", "Kushanas", "Satavahanas", 
            "Palas", "Merchant_Patronage", "Royal_Patronage", "Foreign_Patronage"
        ],
        "10_Sacred_Geography": [
            "Lumbini", "Bodh_Gaya", "Sarnath", "Kushinagar", "Rajgir", "Vaishali", 
            "Nalanda", "Vikramashila", "Buddhist_Circuit", "Sacred_Sites"
        ],
        "11_Spread_of_Buddhism": [
            "India", "Sri_Lanka", "Myanmar", "Thailand", "Cambodia", "Vietnam", 
            "China", "Korea", "Japan", "Tibet", "Nepal", "Central_Asia", "Global_Spread"
        ],
        "12_Universities_and_Monasteries": [
            "Nalanda", "Vikramashila", "Odantapuri", "Somapura", "Monastic_System", "Education_System"
        ],
        "13_Comparative_Studies": [
            "Buddhism_vs_Jainism", "Buddhism_vs_Hinduism", "Buddha_vs_Mahavira", 
            "Karma_Comparison", "Liberation_Comparison", "Ahimsa_Comparison", 
            "Soul_Concept_Comparison", "Philosophical_Comparison"
        ]
    }

    leaf_files = [
        "facts.json", "mcq.json", "statement_based.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "short_answer.json", "long_answer.json",
        "pyq_inspired.json", "interview.json"
    ]

    print(f"Creating Buddhism deep structure in: {target_base}")
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
    create_buddhism_structure()