import os
import shutil

def create_music_dance_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "art-and-culture", "music-and-dance")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Fundamentals": [
            "Meaning_of_Music", "Meaning_of_Dance", "Performing_Arts", "Natyashastra",
            "Music_and_Dance_in_Ancient_India", "Cultural_Significance", "Sources_of_Study", "Terminology"
        ],
        "02_Origins_and_Development": [
            "Vedic_Music", "Samaveda", "Temple_Traditions", "Court_Traditions",
            "Medieval_Developments", "Colonial_Period", "Modern_Developments", "Contemporary_Trends"
        ],
        "03_Indian_Classical_Music_Fundamentals": [
            "Raga", "Tala", "Shruti", "Svara", "Laya", "Alaap", "Bandish", "Improvisation"
        ],
        "04_Hindustani_Classical_Music": [
            "History_of_Hindustani_Music", "Dhrupad", "Dhamar", "Khayal", "Tarana", "Thumri", "Tappa", "Ghazal"
        ],
        "05_Hindustani_Gharanas": [
            "Gwalior_Gharana", "Agra_Gharana", "Kirana_Gharana", "Jaipur_Atrauli_Gharana",
            "Patiala_Gharana", "Rampur_Sahaswan_Gharana", "Banaras_Gharana", "Mewati_Gharana"
        ],
        "06_Carnatic_Music": [
            "History_of_Carnatic_Music", "Melakarta_System", "Kriti", "Varnam", "Tillana", "Pallavi",
            "Ragam_Tanam_Pallavi", "Carnatic_Tradition"
        ],
        "07_Carnatic_Composers": [
            "Purandara_Dasa", "Tyagaraja", "Muthuswami_Dikshitar", "Syama_Sastri",
            "Annamacharya", "Bhadrachala_Ramadasu", "Papanasam_Sivan", "Modern_Composers"
        ],
        "08_Musical_Instruments": [
            "String_Instruments", "Wind_Instruments", "Percussion_Instruments",
            "Tat_Vadya", "Sushir_Vadya", "Avanaddha_Vadya", "Ghana_Vadya", "Instrument_Classification"
        ],
        "09_Famous_Musicians": [
            "Tansen", "Amir_Khusrau", "Bhimsen_Joshi", "Kumar_Gandharva",
            "Bismillah_Khan", "Ravi_Shankar", "M_S_Subbulakshmi", "Hariprasad_Chaurasia"
        ],
        "10_Folk_Music": [
            "Baul", "Bhatiali", "Lavani_Music", "Pandavani", "Kajri", "Chaiti", "Alha", "Regional_Folk_Music"
        ],
        "11_Sufi_and_Devotional_Music": [
            "Qawwali", "Bhajan", "Kirtan", "Abhang", "Shabad_Kirtan",
            "Sufi_Music", "Devotional_Traditions", "Religious_Influence"
        ],
        "12_Classical_Dance_Fundamentals": [
            "Natyashastra_and_Dance", "Abhinaya", "Mudras", "Rasa_Theory",
            "Costumes", "Music_in_Dance", "Stage_Traditions", "Dance_Aesthetics"
        ],
        "13_Bharatanatyam": [
            "History", "Techniques", "Costume", "Repertoire", "Important_Exponents",
            "Themes", "Music", "Modern_Development"
        ],
        "14_Kathak": [
            "History", "Lucknow_Gharana", "Jaipur_Gharana", "Banaras_Gharana",
            "Techniques", "Costume", "Music", "Important_Exponents"
        ],
        "15_Kathakali": [
            "History", "Characters", "Makeup", "Costume", "Music", "Training", "Themes", "Important_Exponents"
        ],
        "16_Kuchipudi": [
            "History", "Dance_Drama", "Techniques", "Costume", "Music", "Themes", "Traditions", "Important_Exponents"
        ],
        "17_Odissi": [
            "History", "Tribhangi", "Chauka", "Costume", "Music", "Temple_Tradition", "Themes", "Important_Exponents"
        ],
        "18_Manipuri": [
            "History", "Raslila", "Costume", "Music", "Themes", "Traditions", "Important_Exponents", "Modern_Development"
        ],
        "19_Mohiniyattam": [
            "History", "Lasya_Tradition", "Costume", "Music", "Themes", "Techniques", "Important_Exponents", "Development"
        ],
        "20_Sattriya": [
            "History", "Vaishnav_Tradition", "Costume", "Music", "Techniques", "Themes", "Satras", "Important_Exponents"
        ],
        "21_Folk_and_Tribal_Dances": [
            "Bihu", "Garba", "Dandiya_Raas", "Ghoomar", "Kalbelia", "Chhau", "Yakshagana", "Cheraw"
        ],
        "22_Major_Regional_Dances": [
            "Rouf", "Nati", "Bhangra", "Giddha", "Dollu_Kunitha", "Veeranatyam", "Karma", "Gaur"
        ],
        "23_Dance_Drama_Traditions": [
            "Yakshagana", "Bhagavata_Mela", "Ankiya_Naat", "Krishnattam", "Raslila", "Therukoothu", "Nautanki", "Jatra"
        ],
        "24_Institutions_and_Awards": [
            "Sangeet_Natak_Akademi", "Kalakshetra", "Kathak_Kendra", "SPIC_MACAY",
            "National_Awards", "Fellowships", "Training_Institutions", "Government_Initiatives"
        ],
        "25_UNESCO_and_Cultural_Heritage": [
            "Kutiyattam", "Ramlila", "Chhau_Dance", "Buddhist_Chanting", "Intangible_Cultural_Heritage",
            "UNESCO_Recognition", "Preservation_Efforts", "Global_Recognition"
        ],
        "26_Historiography_and_Scholarship": [
            "Musicology", "Dance_Historiography", "Textual_Sources", "Archaeological_Evidence",
            "Colonial_Studies", "Nationalist_Interpretations", "Modern_Research", "Source_Criticism"
        ],
        "27_Legacy_and_Contemporary_Relevance": [
            "Cultural_Identity", "Education", "Cinema_and_Music", "Global_Influence",
            "Fusion_Traditions", "Digital_Preservation", "Contemporary_Artists", "Future_Challenges"
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

    print(f"Creating Music and Dance structure in: {target_base}")
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
    create_music_dance_structure()