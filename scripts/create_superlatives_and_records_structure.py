import os
import shutil

def create_superlatives_and_records_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "superlatives-and-records"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_World_Geographical_Superlatives": [
            "Highest_Mountain",
            "Longest_River",
            "Largest_Desert",
            "Largest_Ocean",
            "Deepest_Ocean_Trench",
            "Largest_Island",
            "Largest_Lake",
            "Important_Facts"
        ],

        "02_Indian_Geographical_Superlatives": [
            "Highest_Peak_India",
            "Longest_River_India",
            "Largest_State",
            "Smallest_State",
            "Largest_District",
            "Highest_Waterfall",
            "Longest_Dam",
            "Important_Facts"
        ],

        "03_World_Countries_Records": [
            "Largest_Country",
            "Smallest_Country",
            "Most_Populous_Country",
            "Richest_Country",
            "Highest_GDP",
            "Largest_Democracy",
            "Highest_Life_Expectancy",
            "Important_Facts"
        ],

        "04_Indian_States_Records": [
            "Largest_State_Area",
            "Most_Populous_State",
            "Highest_Literacy",
            "Lowest_Literacy",
            "Highest_Sex_Ratio",
            "Lowest_Sex_Ratio",
            "Highest_Forest_Cover",
            "Important_Facts"
        ],

        "05_Monuments_and_Architecture": [
            "Tallest_Statue",
            "Largest_Temple",
            "Largest_Palace",
            "Largest_Mosque",
            "Largest_Church",
            "Highest_Monument",
            "Longest_Wall",
            "Important_Facts"
        ],

        "06_Transport_and_Infrastructure": [
            "Longest_Highway",
            "Longest_Railway_Platform",
            "Longest_Bridge",
            "Highest_Railway_Station",
            "Largest_Airport",
            "Busiest_Airport",
            "Longest_Tunnel",
            "Important_Facts"
        ],

        "07_Science_and_Space_Records": [
            "Largest_Telescope",
            "Largest_Particle_Accelerator",
            "Most_Powerful_Rocket",
            "Largest_Satellite",
            "Longest_Space_Mission",
            "Highest_Space_Station",
            "Fastest_Spacecraft",
            "Important_Facts"
        ],

        "08_Defence_Records": [
            "Largest_Army",
            "Largest_Navy",
            "Largest_Air_Force",
            "Fastest_Missile",
            "Largest_Aircraft_Carrier",
            "Largest_Submarine",
            "Highest_Battlefield",
            "Important_Facts"
        ],

        "09_Sports_Records_World": [
            "Most_Olympic_Medals",
            "Most_World_Cups",
            "Highest_Run_Scorer",
            "Most_Goals",
            "Fastest_100m",
            "Highest_Individual_Score",
            "Most_Grand_Slams",
            "Important_Facts"
        ],

        "10_Sports_Records_India": [
            "Most_International_Centuries",
            "Highest_Test_Score",
            "Most_Olympic_Medals_India",
            "Most_National_Awards",
            "Highest_Individual_Achievements",
            "Longest_Career",
            "Most_Matches",
            "Important_Facts"
        ],

        "11_Economic_Records": [
            "Largest_Economy",
            "Highest_GDP_Growth",
            "Largest_Stock_Exchange",
            "Largest_Company",
            "Highest_Market_Capitalization",
            "Richest_Individual",
            "Largest_Bank",
            "Important_Facts"
        ],

        "12_Environmental_Records": [
            "Largest_National_Park",
            "Largest_Biosphere_Reserve",
            "Largest_Coral_Reef",
            "Largest_Rainforest",
            "Wettest_Place",
            "Driest_Place",
            "Hottest_Place",
            "Important_Facts"
        ],

        "13_Cultural_and_Literary_Records": [
            "Oldest_Book",
            "Largest_Library",
            "Most_Translated_Book",
            "Oldest_Language",
            "Largest_Festival",
            "Largest_Religious_Gathering",
            "Oldest_University",
            "Important_Facts"
        ],

        "14_Political_Records": [
            "Largest_Parliament",
            "Longest_Written_Constitution",
            "Largest_Democracy",
            "Youngest_Leader",
            "Longest_Serving_Leader",
            "Largest_Election",
            "Most_Voters",
            "Important_Facts"
        ],

        "15_Human_Achievement_Records": [
            "Youngest_Nobel_Laureate",
            "Oldest_Person",
            "Highest_Mountain_Climber",
            "Most_Awards",
            "Longest_Journey",
            "Most_Books_Written",
            "Most_Medals",
            "Important_Facts"
        ],

        "16_Guinness_World_Records": [
            "Largest_Human_Gathering",
            "Largest_Flag",
            "Longest_Dance",
            "Longest_Speech",
            "Largest_Cake",
            "Largest_Pizza",
            "Largest_Artwork",
            "Important_Facts"
        ],

        "17_Indian_Record_Holders": [
            "National_Record_Holders",
            "Indian_Guinness_Records",
            "Indian_Achievements",
            "Indian_Sports_Records",
            "Indian_Cultural_Records",
            "Indian_Scientific_Records",
            "Indian_Infrastructure_Records",
            "Important_Facts"
        ],

        "18_Current_Affairs_Records": [
            "Recent_World_Records",
            "Recent_Indian_Records",
            "Recent_Sports_Records",
            "Recent_Economic_Records",
            "Recent_Science_Records",
            "Recent_Environment_Records",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Geography_Records_PYQ",
            "Sports_Records_PYQ",
            "Political_Records_PYQ",
            "Science_Records_PYQ",
            "Infrastructure_Records_PYQ",
            "Indian_Records_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Records",
            "One_Liner_Revision",
            "Memory_Hooks",
            "Flashcards",
            "Common_Mistakes",
            "Concept_Traps",
            "Rapid_Revision",
            "Expected_Questions"
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

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for filename in leaf_files:

                file_path = os.path.join(topic_path, filename)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ Superlatives & Records structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_superlatives_and_records_structure()