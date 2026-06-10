import os
import shutil

def create_bhakti_sufi_movements_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "medieval-india", "bhakti-and-sufi-movements")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Fundamentals": [
            "Meaning_of_Bhakti",
            "Meaning_of_Sufism",
            "Religious_Climate_of_Medieval_India",
            "Social_Background",
            "Political_Background",
            "Cultural_Background",
            "Sources_of_Study",
            "Historiography"
        ],
        "02_Origins_of_Bhakti_Movement": [
            "Early_Bhakti_Traditions",
            "South_Indian_Bhakti",
            "Alvars",
            "Nayanars",
            "Temple_Traditions",
            "Devotional_Literature",
            "Spread_of_Bhakti",
            "Historical_Significance"
        ],
        "03_Philosophical_Foundations": [
            "Bhakti_Philosophy",
            "Concept_of_God",
            "Saguna_Bhakti",
            "Nirguna_Bhakti",
            "Devotion_and_Salvation",
            "Role_of_Guru",
            "Concept_of_Love",
            "Spiritual_Practices"
        ],
        "04_South_Indian_Bhakti_Saints": [
            "Alvars",
            "Nayanars",
            "Andal",
            "Nammalvar",
            "Appar",
            "Sambandar",
            "Manikkavachakar",
            "Legacy"
        ],
        "05_Ramanuja_and_Vaishnavism": [
            "Life_of_Ramanuja",
            "Vishishtadvaita",
            "Sri_Vaishnavism",
            "Teachings",
            "Social_Reforms",
            "Religious_Influence",
            "Literary_Contributions",
            "Legacy"
        ],
        "06_Madhvacharya_and_Dvaita": [
            "Life_of_Madhvacharya",
            "Dvaita_Philosophy",
            "Teachings",
            "Vaishnava_Tradition",
            "Religious_Debates",
            "Influence",
            "Literary_Contribution",
            "Legacy"
        ],
        "07_Other_Bhakti_Philosophers": [
            "Nimbarka",
            "Vallabhacharya",
            "Ramananda",
            "Chaitanya_Mahaprabhu",
            "Basavanna",
            "Namdev",
            "Jnaneshwar",
            "Philosophical_Contributions"
        ],
        "08_Nirguna_Bhakti_Tradition": [
            "Concept_of_Nirguna",
            "Monotheism",
            "Critique_of_Ritualism",
            "Social_Equality",
            "Universalism",
            "Guru_Tradition",
            "Mysticism",
            "Impact"
        ],
        "09_Kabir": [
            "Life_of_Kabir",
            "Teachings",
            "Dohas",
            "Criticism_of_Orthodoxy",
            "Religious_Synthesis",
            "Social_Message",
            "Kabir_Panth",
            "Legacy"
        ],
        "10_Guru_Nanak_and_Sikhism": [
            "Life_of_Guru_Nanak",
            "Teachings",
            "Concept_of_Ik_Onkar",
            "Sangat_and_Langar",
            "Udasis",
            "Successor_Gurus",
            "Adi_Granth",
            "Legacy"
        ],
        "11_Dadu_and_Other_Nirguna_Saints": [
            "Dadu_Dayal",
            "Ravidas",
            "Sena",
            "Pipa",
            "Dhanna",
            "Malukdas",
            "Teachings",
            "Social_Impact"
        ],
        "12_Saguna_Bhakti_Tradition": [
            "Concept_of_Saguna",
            "Rama_Bhakti",
            "Krishna_Bhakti",
            "Devotional_Worship",
            "Temple_Culture",
            "Literary_Tradition",
            "Music_and_Bhakti",
            "Impact"
        ],
        "13_Rama_Bhakti_Tradition": [
            "Ramananda",
            "Tulsidas",
            "Ramcharitmanas",
            "Rama_Worship",
            "Devotional_Literature",
            "Social_Influence",
            "Religious_Impact",
            "Legacy"
        ],
        "14_Krishna_Bhakti_Tradition": [
            "Surdas",
            "Mirabai",
            "Vallabhacharya",
            "Chaitanya",
            "Bhagavata_Tradition",
            "Devotional_Poetry",
            "Vaishnava_Sects",
            "Legacy"
        ],
        "15_Mirabai": [
            "Life_of_Mirabai",
            "Poetry",
            "Devotion_to_Krishna",
            "Social_Rebellion",
            "Bhajans",
            "Spiritual_Ideals",
            "Influence",
            "Legacy"
        ],
        "16_Chaitanya_Mahaprabhu": [
            "Life",
            "Gaudiya_Vaishnavism",
            "Teachings",
            "Kirtan_Tradition",
            "Bhakti_Practices",
            "Influence_in_Bengal",
            "Literature",
            "Legacy"
        ],
        "17_Bhakti_Literature": [
            "Regional_Languages",
            "Devotional_Poetry",
            "Bhajans",
            "Kirtans",
            "Vernacular_Literature",
            "Religious_Texts",
            "Poetic_Traditions",
            "Cultural_Impact"
        ],
        "18_Sufism_Fundamentals": [
            "Meaning_of_Sufism",
            "Origins_of_Sufism",
            "Mysticism",
            "Concept_of_Love",
            "Spiritual_Path",
            "Pir_and_Murid",
            "Khanqah_System",
            "Sufi_Ethics"
        ],
        "19_Sufi_Philosophy": [
            "Tawhid",
            "Fana",
            "Baqa",
            "Zikr",
            "Sama",
            "Mystical_Experience",
            "Wahdat_al_Wujud",
            "Spiritual_Practices"
        ],
        "20_Arrival_of_Sufism_in_India": [
            "Early_Sufis",
            "Spread_in_India",
            "Political_Context",
            "Social_Context",
            "Interaction_with_Local_Culture",
            "Growth_of_Khanqahs",
            "Missionary_Activities",
            "Legacy"
        ],
        "21_Chishti_Order": [
            "Origins",
            "Khwaja_Moinuddin_Chishti",
            "Qutbuddin_Bakhtiyar_Kaki",
            "Baba_Farid",
            "Nizamuddin_Auliya",
            "Teachings",
            "Practices",
            "Influence"
        ],
        "22_Suhrawardi_Order": [
            "Origins",
            "Bahauddin_Zakariya",
            "Teachings",
            "Organization",
            "Political_Relations",
            "Practices",
            "Expansion",
            "Legacy"
        ],
        "23_Qadiri_and_Naqshbandi_Orders": [
            "Qadiri_Order",
            "Naqshbandi_Order",
            "Sheikh_Abdul_Qadir_Jilani",
            "Sheikh_Ahmad_Sirhindi",
            "Teachings",
            "Practices",
            "Influence_on_Mughals",
            "Legacy"
        ],
        "24_Prominent_Sufi_Saints": [
            "Moinuddin_Chishti",
            "Nizamuddin_Auliya",
            "Baba_Farid",
            "Gesu_Daraz",
            "Salim_Chishti",
            "Shah_Madar",
            "Ahmad_Sirhindi",
            "Contributions"
        ],
        "25_Sufi_Literature_and_Music": [
            "Sufi_Poetry",
            "Qawwali",
            "Amir_Khusrau",
            "Mystical_Literature",
            "Persian_Influence",
            "Regional_Influence",
            "Devotional_Music",
            "Cultural_Impact"
        ],
        "26_Amir_Khusrau": [
            "Life",
            "Literary_Contributions",
            "Music",
            "Qawwali",
            "Persian_Poetry",
            "Hindavi_Literature",
            "Innovations",
            "Legacy"
        ],
        "27_Bhakti_and_Sufi_Interactions": [
            "Common_Features",
            "Differences",
            "Religious_Synthesis",
            "Social_Harmony",
            "Influence_on_Culture",
            "Shared_Traditions",
            "Popular_Practices",
            "Historical_Assessment"
        ],
        "28_Social_Impact": [
            "Challenge_to_Caste",
            "Religious_Tolerance",
            "Women_and_Bhakti",
            "Social_Reforms",
            "Popular_Religion",
            "Mass_Participation",
            "Rural_Influence",
            "Urban_Influence"
        ],
        "29_Political_and_Cultural_Impact": [
            "Influence_on_Rulers",
            "Regional_Kingdoms",
            "Mughal_Policies",
            "Art_and_Architecture",
            "Music_and_Dance",
            "Language_Development",
            "Literature",
            "Cultural_Synthesis"
        ],
        "30_Historiography_and_Debates": [
            "Nationalist_View",
            "Marxist_View",
            "Communalist_View",
            "Modern_Interpretations",
            "Source_Criticism",
            "Historical_Debates",
            "Recent_Scholarship",
            "Comparative_Studies"
        ],
        "31_Legacy_and_Contemporary_Relevance": [
            "Modern_Religious_Traditions",
            "Interfaith_Harmony",
            "Cultural_Heritage",
            "Pilgrimage_Centres",
            "Festivals",
            "Popular_Culture",
            "Contemporary_Influence",
            "Future_Relevance"
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

    print(f"Creating Bhakti and Sufi Movements structure in: {target_base}")
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
    create_bhakti_sufi_movements_structure()