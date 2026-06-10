import os
import shutil

def create_socio_religious_reforms_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "socio-religious-reforms")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_of_Socio_Religious_Reforms": [
            "Colonial_Impact",
            "Western_Education",
            "Christian_Missionary_Challenge",
            "Indian_Society_in_19th_Century",
            "Social_Evils",
            "Religious_Orthodoxy",
            "Intellectual_Awakening",
            "Need_for_Reforms"
        ],

        "02_Nature_and_Characteristics": [
            "Religious_Reform",
            "Social_Reform",
            "Revivalism",
            "Reformism",
            "Rationalism",
            "Humanism",
            "Modernization",
            "Impact_on_Nationalism"
        ],

        "03_Raja_Rammohan_Roy": [
            "Life_and_Career",
            "Religious_Ideas",
            "Social_Reforms",
            "Opposition_to_Sati",
            "Educational_Views",
            "Journalism",
            "Political_Thought",
            "Legacy"
        ],

        "04_Brahmo_Samaj": [
            "Foundation",
            "Principles",
            "Debendranath_Tagore",
            "Keshab_Chandra_Sen",
            "Religious_Reforms",
            "Social_Reforms",
            "Educational_Activities",
            "Historical_Assessment"
        ],

        "05_Young_Bengal_Movement": [
            "Henry_Derozio",
            "Rationalism",
            "Free_Thought",
            "Academic_Association",
            "Social_Criticism",
            "Intellectual_Influence",
            "Limitations",
            "Legacy"
        ],

        "06_Ishwar_Chandra_Vidyasagar": [
            "Life_and_Work",
            "Widow_Remarriage",
            "Women_Education",
            "Social_Reforms",
            "Educational_Reforms",
            "Sanskrit_College",
            "Legislative_Efforts",
            "Legacy"
        ],

        "07_Arya_Samaj": [
            "Swami_Dayananda",
            "Satyarth_Prakash",
            "Back_to_Vedas",
            "Religious_Reforms",
            "Social_Reforms",
            "Shuddhi_Movement",
            "Educational_Work",
            "Historical_Assessment"
        ],

        "08_Swami_Dayananda_Saraswati": [
            "Life_and_Career",
            "Philosophy",
            "Vedic_Revivalism",
            "Critique_of_Orthodoxy",
            "Social_Reforms",
            "Religious_Ideas",
            "Political_Influence",
            "Legacy"
        ],

        "09_Ramakrishna_Tradition": [
            "Ramakrishna_Paramahamsa",
            "Spiritual_Teachings",
            "Religious_Universalism",
            "Vedanta",
            "Mysticism",
            "Disciples",
            "Religious_Influence",
            "Legacy"
        ],

        "10_Swami_Vivekananda": [
            "Life_and_Career",
            "Chicago_Parliament_1893",
            "Practical_Vedanta",
            "Nationalism",
            "Social_Service",
            "Religious_Thought",
            "Youth_Inspiration",
            "Legacy"
        ],

        "11_Ramakrishna_Mission": [
            "Foundation",
            "Objectives",
            "Educational_Work",
            "Social_Service",
            "Relief_Activities",
            "Spiritual_Activities",
            "National_Impact",
            "Historical_Assessment"
        ],

        "12_Theosophical_Movement": [
            "Madame_Blavatsky",
            "Colonel_Olcott",
            "Theosophical_Society",
            "Adyar_Centre",
            "Ancient_Wisdom",
            "Religious_Synthesis",
            "Educational_Activities",
            "Historical_Impact"
        ],

        "13_Annie_Besant": [
            "Life_and_Career",
            "Theosophy",
            "Educational_Activities",
            "Central_Hindu_College",
            "Nationalism",
            "Home_Rule_Movement",
            "Political_Thought",
            "Legacy"
        ],

        "14_Prarthana_Samaj": [
            "Foundation",
            "M_G_Ranade",
            "R_G_Bhandarkar",
            "Religious_Reforms",
            "Social_Reforms",
            "Women's_Issues",
            "Educational_Work",
            "Historical_Assessment"
        ],

        "15_Satyashodhak_Samaj": [
            "Jyotirao_Phule",
            "Anti_Caste_Movement",
            "Social_Equality",
            "Education_for_Depressed_Classes",
            "Women's_Reforms",
            "Critique_of_Brahmanism",
            "Organizational_Work",
            "Historical_Impact"
        ],

        "16_Jyotirao_and_Savitribai_Phule": [
            "Life_and_Career",
            "Girls_Education",
            "Social_Justice",
            "Anti_Caste_Struggle",
            "Schools_for_Marginalized",
            "Women's_Rights",
            "Reform_Ideology",
            "Legacy"
        ],

        "17_Aligarh_Movement": [
            "Sir_Syed_Ahmad_Khan",
            "Scientific_Society",
            "Mohammedan_Anglo_Oriental_College",
            "Muslim_Modernization",
            "Educational_Reforms",
            "Political_Views",
            "Social_Reforms",
            "Historical_Assessment"
        ],

        "18_Sir_Syed_Ahmad_Khan": [
            "Life_and_Career",
            "Religious_Interpretation",
            "Educational_Thought",
            "Political_Views",
            "Social_Reforms",
            "Scientific_Approach",
            "Muslim_Society",
            "Legacy"
        ],

        "19_Deoband_and_Islamic_Reforms": [
            "Darul_Uloom_Deoband",
            "Religious_Education",
            "Islamic_Reformism",
            "Ulama_Tradition",
            "Educational_Network",
            "Political_Attitudes",
            "Religious_Influence",
            "Historical_Impact"
        ],

        "20_Sikh_Reform_Movements": [
            "Singh_Sabha_Movement",
            "Khalsa_Identity",
            "Religious_Reforms",
            "Educational_Work",
            "Gurdwara_Reforms",
            "Community_Organization",
            "Modernization",
            "Historical_Assessment"
        ],

        "21_Parsi_and_Other_Reform_Movements": [
            "Rahnumai_Mazdayasan_Sabha",
            "Parsi_Reforms",
            "Religious_Modernization",
            "Community_Leadership",
            "Educational_Activities",
            "Social_Reforms",
            "Minority_Communities",
            "Historical_Impact"
        ],

        "22_Women_Reform_Movements": [
            "Abolition_of_Sati",
            "Widow_Remarriage",
            "Women_Education",
            "Age_of_Consent",
            "Female_Upliftment",
            "Women_Organizations",
            "Social_Legislation",
            "Historical_Impact"
        ],

        "23_Caste_and_Social_Equality_Movements": [
            "Anti_Caste_Reforms",
            "Depressed_Class_Upliftment",
            "Temple_Entry",
            "Social_Justice",
            "Equality_Movements",
            "Regional_Initiatives",
            "Reform_Strategies",
            "Historical_Impact"
        ],

        "24_Educational_Reforms": [
            "Modern_Education",
            "Vernacular_Education",
            "Women's_Education",
            "Religious_Education",
            "National_Education",
            "Educational_Institutions",
            "Literacy_and_Awareness",
            "Long_Term_Impact"
        ],

        "25_Contribution_to_Nationalism": [
            "Political_Awakening",
            "Social_Awakening",
            "National_Identity",
            "Modern_Values",
            "Leadership_Development",
            "Public_Sphere",
            "Intellectual_Foundation",
            "National_Movement_Linkages"
        ],

        "26_Historiography": [
            "Nationalist_View",
            "Marxist_Interpretation",
            "Subaltern_Perspective",
            "Colonial_View",
            "Feminist_Interpretation",
            "Revivalism_vs_Reformism",
            "Modern_Debates",
            "Comparative_Assessment"
        ],

        "27_Sources": [
            "Reform_Literature",
            "Pamphlets_and_Books",
            "Newspapers",
            "Institutional_Records",
            "Personal_Writings",
            "Government_Reports",
            "Missionary_Accounts",
            "Source_Criticism"
        ],

        "28_Legacy_and_Historical_Significance": [
            "Social_Modernization",
            "Religious_Reinterpretation",
            "Women's_Advancement",
            "Educational_Progress",
            "Democratic_Values",
            "National_Awakening",
            "Contemporary_Relevance",
            "Long_Term_Legacy"
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

    print(f"Creating Socio-Religious Reforms structure in: {target_base}")
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
    create_socio_religious_reforms_structure()