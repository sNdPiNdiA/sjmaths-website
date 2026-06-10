import os
import shutil

def create_literature_philosophy_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "art-and-culture", "literature-and-philosophy")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Fundamentals": [
            "Meaning_of_Indian_Literature", "Meaning_of_Indian_Philosophy", "Literary_Traditions",
            "Philosophical_Traditions", "Oral_Tradition", "Written_Tradition",
            "Languages_of_Ancient_India", "Sources_of_Study"
        ],
        "02_Vedic_Literature": [
            "Rigveda", "Samaveda", "Yajurveda", "Atharvaveda", "Brahmanas",
            "Aranyakas", "Upanishads", "Vedangas", "Sutra_Literature", "Vedic_Thought"
        ],
        "03_Epics": [
            "Ramayana", "Mahabharata", "Bhagavad_Gita", "Evolution_of_Epics",
            "Themes_of_Ramayana", "Themes_of_Mahabharata", "Cultural_Influence",
            "Epic_Tradition"
        ],
        "04_Puranic_Literature": [
            "Major_Puranas", "Minor_Puranas", "Vishnu_Purana", "Shiva_Purana",
            "Bhagavata_Purana", "Genealogies", "Cosmology", "Puranic_Tradition"
        ],
        "05_Buddhist_Literature": [
            "Tripitaka", "Vinaya_Pitaka", "Sutta_Pitaka", "Abhidhamma_Pitaka",
            "Jataka_Tales", "Milindapanha", "Mahayana_Texts", "Pali_Literature",
            "Buddhist_Scholasticism"
        ],
        "06_Jain_Literature": [
            "Agamas", "Angas", "Upangas", "Kalpasutra", "Tattvartha_Sutra",
            "Prakrit_Literature", "Jain_Commentaries", "Jain_Scholasticism"
        ],
        "07_Sangam_Literature": [
            "Ettuthokai", "Pattuppattu", "Tolkappiyam", "Pathinenkilkanakku",
            "Sangam_Poets", "Society_in_Sangam_Texts", "Economy_in_Sangam_Texts",
            "Sangam_Culture"
        ],
        "08_Classical_Sanskrit_Literature": [
            "Classical_Sanskrit", "Court_Literature", "Sanskrit_Drama",
            "Sanskrit_Poetry", "Mahakavya_Tradition", "Prose_Literature",
            "Literary_Styles", "Literary_Criticism"
        ],
        "09_Kalidasa": [
            "Raghuvamsha", "Kumarasambhava", "Meghaduta", "Ritusamhara",
            "Abhijnanasakuntalam", "Vikramorvashiyam", "Malavikagnimitram",
            "Literary_Contribution"
        ],
        "10_Other_Sanskrit_Authors": [
            "Bhasa", "Shudraka", "Vishakhadatta", "Bharavi", "Magha",
            "Banabhatta", "Dandin", "Bhavabhuti"
        ],
        "11_Tamil_and_Regional_Literature": [
            "Bhakti_Literature", "Alvars", "Nayanars", "Early_Tamil_Texts",
            "Kannada_Literature", "Telugu_Literature", "Malayalam_Literature",
            "Regional_Literary_Traditions"
        ],
        "12_Medieval_Literature": [
            "Bhakti_Poetry", "Sufi_Literature", "Persian_Literature",
            "Court_Histories", "Vernacular_Literature", "Devotional_Texts",
            "Literary_Syncretism", "Literary_Developments"
        ],
        "13_Modern_Indian_Literature": [
            "Bengal_Renaissance_Literature", "Nationalist_Literature",
            "Hindi_Literature", "Urdu_Literature", "Regional_Modern_Literature",
            "Literary_Reform_Movements", "Freedom_Movement_Literature",
            "Contemporary_Developments"
        ],
        "14_Indian_Philosophy_Fundamentals": [
            "Meaning_of_Darshana", "Concepts_of_Atman", "Brahman", "Karma",
            "Dharma", "Moksha", "Rebirth", "Philosophical_Methods"
        ],
        "15_Orthodox_Philosophical_Schools": [
            "Nyaya", "Vaisheshika", "Samkhya", "Yoga", "Mimamsa",
            "Vedanta", "Advaita_Vedanta", "Vishishtadvaita"
        ],
        "16_Heterodox_Philosophical_Schools": [
            "Buddhism", "Jainism", "Charvaka", "Ajivika", "Materialism",
            "Skepticism", "Non_Vedic_Traditions"
        ],
        "17_Buddhist_Philosophy": [
            "Four_Noble_Truths", "Eightfold_Path", "Dependent_Origination",
            "Anatman", "Anitya", "Sunyata", "Madhyamaka", "Yogachara"
        ],
        "18_Jain_Philosophy": [
            "Ahimsa", "Anekantavada", "Syadvada", "Aparigraha", "Jiva",
            "Ajiva", "Triratna", "Kevala_Jnana"
        ],
        "19_Bhakti_and_Sufi_Philosophy": [
            "Bhakti_Philosophy", "Nirguna_Tradition", "Saguna_Tradition",
            "Sufi_Philosophy", "Wahdat_al_Wujud", "Chishti_Thought",
            "Bhakti_Sufi_Interactions", "Social_Impact"
        ],
        "20_Important_Philosophers": [
            "Yajnavalkya", "Buddha", "Mahavira", "Nagarjuna", "Shankaracharya",
            "Ramanujacharya", "Madhvacharya", "Vallabhacharya"
        ],
        "21_Literary_and_Philosophical_Concepts": [
            "Rasa_Theory", "Dhvani_Theory", "Alankara", "Natya_Theory",
            "Aesthetics", "Ethics", "Metaphysics", "Epistemology"
        ],
        "22_Historiography_and_Scholarship": [
            "Literary_Historiography", "Philosophical_Historiography",
            "Colonial_Interpretations", "Nationalist_Interpretations",
            "Modern_Research", "Textual_Criticism", "Source_Analysis"
        ],
        "23_Legacy_and_Significance": [
            "Literary_Legacy", "Philosophical_Legacy", "Cultural_Influence",
            "Religious_Influence", "Educational_Influence", "Global_Impact",
            "Contemporary_Relevance"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "author_work_matching.json", "quotation_based.json",
        "passage_based.json", "source_based.json", "case_study.json",
        "short_answer.json", "long_answer.json", "mains_10m.json",
        "mains_15m.json", "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "pyq_teaching.json",
        "interview.json", "flashcards.json", "revision_questions.json",
        "concept_traps.json", "common_mistakes.json", "memory_hooks.json"
    ]

    print(f"Creating Literature and Philosophy structure in: {target_base}")
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
    create_literature_philosophy_structure()