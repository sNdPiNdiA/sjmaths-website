import os
import shutil

def create_military_exercises_and_operations_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "military-exercises-and-operations"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_India_US_Exercises": [
            "Yudh_Abhyas",
            "Vajra_Prahar",
            "Cope_India",
            "Tiger_Triumph",
            "Red_Flag",
            "RIMPAC",
            "Special_Forces_Cooperation",
            "Recent_Developments"
        ],

        "02_India_Russia_Exercises": [
            "INDRA",
            "Avia_INDRA",
            "Naval_INDRA",
            "Army_Cooperation",
            "Air_Force_Cooperation",
            "Counter_Terrorism_Drills",
            "Strategic_Coordination",
            "Recent_Developments"
        ],

        "03_India_France_Exercises": [
            "Varuna",
            "Garuda",
            "Shakti",
            "Naval_Cooperation",
            "Air_Force_Cooperation",
            "Army_Cooperation",
            "Indo_Pacific_Collaboration",
            "Recent_Developments"
        ],

        "04_India_Japan_Exercises": [
            "Dharma_Guardian",
            "JIMEX",
            "Veer_Guardian",
            "Maritime_Cooperation",
            "Army_Coordination",
            "Air_Force_Coordination",
            "Strategic_Partnership",
            "Recent_Developments"
        ],

        "05_India_Australia_Exercises": [
            "AUSTRA_HIND",
            "AUSINDEX",
            "Pitch_Black",
            "Malabar_Participation",
            "Naval_Cooperation",
            "Air_Cooperation",
            "Army_Cooperation",
            "Recent_Developments"
        ],

        "06_India_UK_Exercises": [
            "Ajeya_Warrior",
            "Konkan",
            "Cobra_Warrior",
            "Naval_Cooperation",
            "Army_Cooperation",
            "Air_Force_Cooperation",
            "Strategic_Partnership",
            "Recent_Developments"
        ],

        "07_India_Neighbourhood_Exercises": [
            "Mitra_Shakti",
            "Surya_Kiran",
            "Hand_in_Hand",
            "SAMPRITI",
            "Bongosagar",
            "SLINEX",
            "IMT_TRILAT",
            "Regional_Cooperation"
        ],

        "08_Multilateral_Exercises": [
            "Milan",
            "RIMPAC",
            "Cobra_Gold",
            "Bright_Star",
            "Kakadu",
            "Komodo",
            "AMAN",
            "Exercise_Trends"
        ],

        "09_Naval_Exercises": [
            "Malabar",
            "Varuna",
            "AUSINDEX",
            "Konkan",
            "SLINEX",
            "Bongosagar",
            "Sea_Dragon",
            "Maritime_Security"
        ],

        "10_Air_Force_Exercises": [
            "Garuda",
            "Cope_India",
            "Veer_Guardian",
            "Pitch_Black",
            "Desert_Eagle",
            "Eastern_Bridge",
            "Red_Flag",
            "Air_Power_Coordination"
        ],

        "11_Army_Exercises": [
            "Yudh_Abhyas",
            "Shakti",
            "Ajeya_Warrior",
            "AUSTRA_HIND",
            "Dharma_Guardian",
            "Mitra_Shakti",
            "Surya_Kiran",
            "Land_Warfare_Cooperation"
        ],

        "12_UN_Peacekeeping_Operations": [
            "MONUSCO",
            "UNIFIL",
            "UNDOF",
            "MINUSCA",
            "UNMISS",
            "India_in_UN_Missions",
            "Peacekeeping_Training",
            "Major_Contributions"
        ],

        "13_Indian_Military_Operations": [
            "Operation_Meghdoot",
            "Operation_Cactus",
            "Operation_Vijay",
            "Operation_Parakram",
            "Operation_Rakshak",
            "Surgical_Strikes",
            "Balakot_Airstrike",
            "Strategic_Impact"
        ],

        "14_Humanitarian_and_Evacuation_Operations": [
            "Operation_Ganga",
            "Operation_Kaveri",
            "Operation_Dost",
            "Operation_Rahat",
            "Vande_Bharat_Mission",
            "Samudra_Setu",
            "Humanitarian_Assistance",
            "Disaster_Response"
        ],

        "15_Counter_Terrorism_Operations": [
            "Operation_Black_Thunder",
            "Operation_All_Out",
            "Operation_Rakshak",
            "Counter_Insurgency",
            "Urban_Warfare",
            "Special_Forces_Operations",
            "Internal_Security",
            "Strategic_Outcomes"
        ],

        "16_Historical_Military_Operations": [
            "Operation_Polo",
            "Operation_Trident",
            "Operation_Python",
            "Operation_Jackpot",
            "Liberation_of_Goa",
            "Bangladesh_War_Operations",
            "Kargil_Operations",
            "Historic_Successes"
        ],

        "17_Current_Affairs_Exercises": [
            "Recent_Bilateral_Exercises",
            "Recent_Multilateral_Exercises",
            "Recent_Naval_Exercises",
            "Recent_Air_Exercises",
            "Recent_Army_Exercises",
            "Exercise_Outcomes",
            "Strategic_Trends",
            "Monthly_Updates"
        ],

        "18_UPSC_PYQ_Themes": [
            "Military_Exercise_Matching",
            "Country_Partner_Questions",
            "Operation_Based_PYQs",
            "UN_Mission_PYQs",
            "Exercise_Locations",
            "Strategic_Importance",
            "Previous_Year_Analysis",
            "Revision"
        ],

        "19_SSC_Railway_High_Yield": [
            "Most_Asked_Exercises",
            "Most_Asked_Operations",
            "Country_Exercise_Pairs",
            "Quick_Revision",
            "One_Liners",
            "Memory_Tricks",
            "Expected_Questions",
            "Practice_Set"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Country_Wise_Mnemonics",
            "Operation_Mnemonics",
            "Exercise_Categorization",
            "Flashcard_Themes",
            "Top_100_Facts",
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
        "mains_10m.json",
        "mains_15m.json",
        "mains_20m.json",
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

    print("\n✅ Military Exercises & Operations structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_military_exercises_and_operations_structure()