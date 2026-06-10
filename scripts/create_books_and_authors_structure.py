import os
import shutil

def create_books_and_authors_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "culture-and-awards",
        "books-and-authors"
    )

    # Clean existing structure
    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Ancient_Indian_Literature": [
            "Vedas",
            "Upanishads",
            "Brahmanas",
            "Aranyakas",
            "Ramayana",
            "Mahabharata",
            "Puranas",
            "Sangam_Literature"
        ],

        "02_Vedic_and_Epic_Texts": [
            "Rigveda",
            "Yajurveda",
            "Samaveda",
            "Atharvaveda",
            "Valmiki_Ramayana",
            "Vyasa_Mahabharata",
            "Bhagavad_Gita",
            "Epic_Traditions"
        ],

        "03_Buddhist_and_Jain_Texts": [
            "Tripitaka",
            "Vinaya_Pitaka",
            "Sutta_Pitaka",
            "Abhidhamma_Pitaka",
            "Jain_Agamas",
            "Kalpa_Sutra",
            "Jain_Literature",
            "Religious_Texts"
        ],

        "04_Medieval_Indian_Literature": [
            "Bhakti_Literature",
            "Sufi_Literature",
            "Tulsidas",
            "Kabir",
            "Surdas",
            "Malik_Muhammad_Jayasi",
            "Persian_Works",
            "Regional_Literature"
        ],

        "05_Modern_Indian_Literature": [
            "Bankim_Chandra",
            "Rabindranath_Tagore",
            "Premchand",
            "Saratchandra",
            "RK_Narayan",
            "Mulk_Raj_Anand",
            "Indian_English_Writers",
            "Modern_Works"
        ],

        "06_Constitution_and_Political_Books": [
            "Constitution_of_India",
            "Discovery_of_India",
            "India_Wins_Freedom",
            "Why_I_Am_An_Atheist",
            "Annihilation_of_Caste",
            "Hind_Swaraj",
            "Political_Writings",
            "Nation_Building_Texts"
        ],

        "07_Famous_Indian_Authors": [
            "Rabindranath_Tagore",
            "Premchand",
            "RK_Narayan",
            "Chetan_Bhagat",
            "Amish_Tripathi",
            "Ruskin_Bond",
            "Khushwant_Singh",
            "Indian_Writers"
        ],

        "08_Famous_International_Authors": [
            "William_Shakespeare",
            "Leo_Tolstoy",
            "Charles_Dickens",
            "George_Orwell",
            "JK_Rowling",
            "Mark_Twain",
            "Ernest_Hemingway",
            "Global_Writers"
        ],

        "09_Autobiographies": [
            "My_Experiments_With_Truth",
            "Wings_of_Fire",
            "Playing_It_My_Way",
            "Long_Walk_to_Freedom",
            "Toward_Freedom",
            "An_Undocumented_Wonder",
            "Autobiographical_Works",
            "Important_Facts"
        ],

        "10_Biographies": [
            "Gandhi",
            "Subhas_Bose",
            "Vivekananda",
            "Ambedkar",
            "APJ_Abdul_Kalam",
            "Sardar_Patel",
            "Bhagat_Singh",
            "Biographical_Works"
        ],

        "11_Books_and_Authors_Static_GK": [
            "Famous_Book_Author_Pairs",
            "Indian_Book_Author_Pairs",
            "International_Book_Author_Pairs",
            "Frequently_Asked",
            "Exam_Favorites",
            "Memory_Tricks",
            "Revision_Set",
            "PYQ_Focus"
        ],

        "12_Bestselling_Books": [
            "Global_Bestsellers",
            "Indian_Bestsellers",
            "Modern_Bestsellers",
            "Classic_Bestsellers",
            "Fiction_Bestsellers",
            "Non_Fiction_Bestsellers",
            "Popular_Writers",
            "Important_Facts"
        ],

        "13_Important_Novels": [
            "Godan",
            "Gitanjali",
            "Malgudi_Days",
            "Train_to_Pakistan",
            "Midnights_Children",
            "The_Guide",
            "A_Suitable_Boy",
            "Novel_Themes"
        ],

        "14_Important_Non_Fiction": [
            "Discovery_of_India",
            "India_After_Gandhi",
            "Ignited_Minds",
            "The_Argumentative_Indian",
            "Freedom_at_Midnight",
            "Everybody_Loves_A_Good_Drought",
            "Important_Non_Fiction_Works",
            "Exam_Relevance"
        ],

        "15_Books_in_Current_Affairs": [
            "Recent_Book_Releases",
            "Government_Publications",
            "Awarded_Books",
            "International_Releases",
            "Author_Launches",
            "Annual_Compilations",
            "Current_Affairs_Books",
            "Monthly_Updates"
        ],

        "16_UPSC_PYQ_Themes": [
            "Ancient_Texts",
            "Authors_and_Works",
            "Autobiographies",
            "Biographies",
            "Book_Author_Matching",
            "Literary_History",
            "PYQ_Analysis",
            "Revision"
        ],

        "17_SSC_High_Yield": [
            "One_Liners",
            "Most_Asked_Books",
            "Most_Asked_Authors",
            "Quick_Revision",
            "SSC_Previous_Questions",
            "Memory_Hacks",
            "High_Frequency_Areas",
            "Practice_Set"
        ],

        "18_Railway_High_Yield": [
            "Popular_Books",
            "Popular_Authors",
            "Railway_PYQ",
            "Revision_Notes",
            "One_Liners",
            "Quick_Practice",
            "Expected_Questions",
            "High_Yield_Areas"
        ],

        "19_State_PCS_High_Yield": [
            "State_Exam_Favorites",
            "Regional_Literature",
            "Important_Writers",
            "Classic_Books",
            "State_PCS_PYQ",
            "Revision_Set",
            "Expected_Questions",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Book_Author_Mnemonics",
            "Flashcard_Themes",
            "Rapid_Revision",
            "Top_100_Books",
            "Top_100_Authors",
            "Common_Mistakes",
            "Concept_Traps",
            "Last_Minute_Revision"
        ]
    }

    leaf_files = [
        "facts.json",
        "one_liner.json",
        "mcq_easy.json",
        "mcq_medium.json",
        "mcq_hard.json",
        "multiple_statement.json",
        "assertion_reason.json",
        "match_following.json",
        "fill_blanks.json",
        "true_false.json",
        "chronology.json",
        "arrange_sequence.json",
        "pair_matching.json",
        "odd_one_out.json",
        "statement_based.json",
        "source_based.json",
        "passage_based.json",
        "case_study.json",
        "short_answer.json",
        "long_answer.json",
        "pyq_upsc.json",
        "pyq_ssc.json",
        "pyq_railway.json",
        "pyq_state_pcs.json",
        "interview.json",
        "flashcards.json",
        "revision_questions.json",
        "concept_traps.json",
        "common_mistakes.json",
        "memory_hooks.json"
    ]

    print(f"Creating structure in: {target_base}")

    for category, topics in structure.items():

        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        print(f"[+] {category}")

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            print(f"    [+] {topic}")

            for filename in leaf_files:

                file_path = os.path.join(topic_path, filename)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ Books & Authors structure created successfully.")
    print(f"📁 Location: {target_base}")


if __name__ == "__main__":
    create_books_and_authors_structure()