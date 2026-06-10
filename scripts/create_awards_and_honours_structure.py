import os
import shutil

def create_awards_and_honours_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "culture-and-awards",
        "awards-and-honours"
    )

    if os.path.exists(target_base):
        shutil.rmtree(target_base)

    structure = {
        "01_Indian_Civilian_Awards": [
            "Bharat_Ratna",
            "Padma_Vibhushan",
            "Padma_Bhushan",
            "Padma_Shri",
            "Award_Hierarchy",
            "Eligibility",
            "Selection_Process",
            "Recent_Awardees"
        ],

        "02_Indian_Gallantry_Awards": [
            "Param_Vir_Chakra",
            "Maha_Vir_Chakra",
            "Vir_Chakra",
            "Ashoka_Chakra",
            "Kirti_Chakra",
            "Shaurya_Chakra",
            "Military_Honours",
            "Recent_Recipients"
        ],

        "03_Indian_National_Awards": [
            "National_Awards_Overview",
            "National_Bravery_Awards",
            "National_Youth_Awards",
            "National_Teachers_Award",
            "National_Child_Award",
            "National_Service_Awards",
            "Government_Honours",
            "Recent_Updates"
        ],

        "04_Sports_Awards": [
            "Major_Dhyan_Chand_Khel_Ratna",
            "Arjuna_Award",
            "Dronacharya_Award",
            "Dhyan_Chand_Award",
            "Rashtriya_Khel_Protsahan",
            "Sports_Honours",
            "Awardees",
            "Recent_Updates"
        ],

        "05_Literary_Awards": [
            "Jnanpith_Award",
            "Sahitya_Akademi_Award",
            "Vyas_Samman",
            "Saraswati_Samman",
            "Moorti_Devi_Award",
            "Literary_Honours",
            "Awardees",
            "Recent_Developments"
        ],

        "06_Film_and_Entertainment_Awards": [
            "National_Film_Awards",
            "Dadasaheb_Phalke_Award",
            "Filmfare_Awards",
            "IIFA_Awards",
            "Entertainment_Honours",
            "Award_Categories",
            "Awardees",
            "Recent_Developments"
        ],

        "07_Science_and_Technology_Awards": [
            "Shanti_Swarup_Bhatnagar_Prize",
            "Infosys_Prize",
            "Bhatnagar_Awardees",
            "Scientific_Honours",
            "Research_Awards",
            "Technology_Awards",
            "Innovation_Awards",
            "Recent_Winners"
        ],

        "08_International_Awards": [
            "Global_Awards",
            "Prestigious_World_Awards",
            "International_Honours",
            "World_Recognition",
            "Awarding_Bodies",
            "Major_Recipients",
            "Trends",
            "Recent_Developments"
        ],

        "09_UN_and_Global_Awards": [
            "UN_Champions_of_the_Earth",
            "UNEP_Awards",
            "UNESCO_Prizes",
            "UN_Human_Rights_Awards",
            "Global_Sustainability_Awards",
            "International_Recognition",
            "Awardees",
            "Recent_Updates"
        ],

        "10_Padma_Awards_Winners": [
            "Padma_Vibhushan_Winners",
            "Padma_Bhushan_Winners",
            "Padma_Shri_Winners",
            "Notable_Awardees",
            "Current_Year",
            "Historical_Data",
            "Important_Facts",
            "PYQ_Focus"
        ],

        "11_Bharat_Ratna_Winners": [
            "Recipients",
            "Chronology",
            "Posthumous_Awards",
            "Women_Recipients",
            "Foreign_Recipients",
            "Important_Facts",
            "Recent_Discussions",
            "PYQ_Focus"
        ],

        "12_Nobel_Prize": [
            "Physics",
            "Chemistry",
            "Medicine",
            "Literature",
            "Peace",
            "Economics",
            "Indian_Nobel_Laureates",
            "Recent_Winners"
        ],

        "13_Booker_Prize": [
            "History",
            "Categories",
            "Indian_Winners",
            "International_Booker",
            "Selection_Process",
            "Recent_Winners",
            "Important_Facts",
            "PYQ_Focus"
        ],

        "14_Oscar_Awards": [
            "Academy_Awards",
            "Categories",
            "Indian_Oscar_Winners",
            "Historic_Wins",
            "Recent_Winners",
            "Important_Facts",
            "Current_Affairs",
            "PYQ_Focus"
        ],

        "15_Grammy_Awards": [
            "Music_Awards",
            "Indian_Winners",
            "Categories",
            "Historic_Winners",
            "Recent_Winners",
            "Important_Facts",
            "Current_Affairs",
            "PYQ_Focus"
        ],

        "16_Pulitzer_Prize": [
            "History",
            "Categories",
            "Journalism",
            "Literature",
            "Notable_Winners",
            "Recent_Winners",
            "Important_Facts",
            "PYQ_Focus"
        ],

        "17_Magsaysay_Award": [
            "History",
            "Categories",
            "Indian_Recipients",
            "Notable_Winners",
            "Recent_Winners",
            "Important_Facts",
            "Current_Affairs",
            "PYQ_Focus"
        ],

        "18_Templeton_Prize": [
            "History",
            "Purpose",
            "Recipients",
            "Selection_Process",
            "Recent_Winners",
            "Important_Facts",
            "Global_Recognition",
            "PYQ_Focus"
        ],

        "19_Current_Affairs_Awards": [
            "National_Awards_Current",
            "International_Awards_Current",
            "Sports_Awards_Current",
            "Science_Awards_Current",
            "Literary_Awards_Current",
            "Film_Awards_Current",
            "Monthly_Updates",
            "Exam_Focus"
        ],

        "20_UPSC_PYQ_Themes": [
            "Award_Matching",
            "Award_Institutions",
            "Award_Winners",
            "Award_Categories",
            "Static_vs_Current",
            "Previous_Year_Questions",
            "High_Yield_Areas",
            "Revision"
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
        "pair_matching.json",
        "odd_one_out.json",
        "statement_based.json",
        "short_answer.json",
        "long_answer.json",
        "pyq_upsc.json",
        "pyq_ssc.json",
        "pyq_railway.json",
        "pyq_state_pcs.json",
        "flashcards.json",
        "revision_questions.json",
        "concept_traps.json"
    ]

    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for file_name in leaf_files:
                with open(
                    os.path.join(topic_path, file_name),
                    "w",
                    encoding="utf-8"
                ) as f:
                    f.write("[]")

    print("Awards & Honours structure created successfully.")

if __name__ == "__main__":
    create_awards_and_honours_structure()