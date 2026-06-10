import os
import shutil

def create_important_dates_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "important-dates"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_National_Days_of_India": [
            "Republic_Day",
            "Independence_Day",
            "Constitution_Day",
            "National_Unity_Day",
            "National_Voters_Day",
            "National_Science_Day",
            "National_Mathematics_Day",
            "Important_Facts"
        ],

        "02_International_Days_UN": [
            "UN_Day",
            "Human_Rights_Day",
            "International_Peace_Day",
            "World_Population_Day",
            "International_Womens_Day",
            "International_Youth_Day",
            "International_Literacy_Day",
            "Important_Facts"
        ],

        "03_Environment_Days": [
            "World_Environment_Day",
            "Earth_Day",
            "World_Water_Day",
            "World_Wildlife_Day",
            "International_Forest_Day",
            "Ozone_Day",
            "Biodiversity_Day",
            "Important_Facts"
        ],

        "04_Health_and_Medical_Days": [
            "World_Health_Day",
            "World_AIDS_Day",
            "World_TB_Day",
            "World_Blood_Donor_Day",
            "Mental_Health_Day",
            "Anti_Tobacco_Day",
            "Yoga_Day",
            "Important_Facts"
        ],

        "05_Education_and_Literacy_Days": [
            "International_Literacy_Day",
            "Teachers_Day",
            "National_Education_Day",
            "World_Book_Day",
            "Student_Day",
            "Reading_Day",
            "Education_Observances",
            "Important_Facts"
        ],

        "06_Women_and_Child_Days": [
            "International_Womens_Day",
            "National_Girl_Child_Day",
            "Childrens_Day",
            "International_Day_of_Girl_Child",
            "Mothers_Day",
            "National_Child_Day",
            "Women_Empowerment_Days",
            "Important_Facts"
        ],

        "07_Science_and_Technology_Days": [
            "National_Science_Day",
            "National_Technology_Day",
            "World_Telecommunication_Day",
            "World_Space_Week",
            "National_Mathematics_Day",
            "Engineers_Day",
            "Innovation_Day",
            "Important_Facts"
        ],

        "08_Defence_and_Patriotic_Days": [
            "Army_Day",
            "Navy_Day",
            "Air_Force_Day",
            "Kargil_Vijay_Diwas",
            "Armed_Forces_Flag_Day",
            "Param_Vir_Chakra_Day",
            "National_War_Memorial_Day",
            "Important_Facts"
        ],

        "09_Agriculture_and_Food_Days": [
            "World_Food_Day",
            "National_Farmers_Day",
            "Soil_Day",
            "Milk_Day",
            "Fisheries_Day",
            "Cooperation_Day",
            "Agriculture_Observances",
            "Important_Facts"
        ],

        "10_Labour_and_Economic_Days": [
            "Labour_Day",
            "Consumer_Rights_Day",
            "MSME_Day",
            "Statistics_Day",
            "World_Tourism_Day",
            "Savings_Day",
            "Economic_Observances",
            "Important_Facts"
        ],

        "11_Human_Rights_and_Social_Justice_Days": [
            "Human_Rights_Day",
            "Social_Justice_Day",
            "Anti_Corruption_Day",
            "Democracy_Day",
            "Peace_Day",
            "Tolerance_Day",
            "Social_Development_Day",
            "Important_Facts"
        ],

        "12_Culture_and_Language_Days": [
            "Hindi_Diwas",
            "Mother_Language_Day",
            "World_Heritage_Day",
            "Culture_Day",
            "Sanskrit_Day",
            "Language_Observances",
            "Art_And_Culture_Days",
            "Important_Facts"
        ],

        "13_Sports_Days": [
            "National_Sports_Day",
            "Olympic_Day",
            "Chess_Day",
            "Cricket_Day",
            "International_Sports_Events",
            "Fit_India_Movement",
            "Sports_Observances",
            "Important_Facts"
        ],

        "14_Disaster_and_Safety_Days": [
            "Disaster_Reduction_Day",
            "Road_Safety_Week",
            "Fire_Service_Day",
            "Civil_Defence_Day",
            "Safety_Day",
            "Emergency_Preparedness_Day",
            "Risk_Reduction_Days",
            "Important_Facts"
        ],

        "15_Important_Weeks_and_Years": [
            "National_Weeks",
            "International_Weeks",
            "UN_Decades",
            "International_Years",
            "Commemorative_Years",
            "Awareness_Weeks",
            "Theme_Based_Years",
            "Important_Facts"
        ],

        "16_Month_Wise_Observances_January_to_March": [
            "January_Observances",
            "February_Observances",
            "March_Observances",
            "Month_Wise_Revision",
            "Important_Dates",
            "One_Liners",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "17_Month_Wise_Observances_April_to_June": [
            "April_Observances",
            "May_Observances",
            "June_Observances",
            "Month_Wise_Revision",
            "Important_Dates",
            "One_Liners",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "18_Month_Wise_Observances_July_to_September": [
            "July_Observances",
            "August_Observances",
            "September_Observances",
            "Month_Wise_Revision",
            "Important_Dates",
            "One_Liners",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "19_Month_Wise_Observances_October_to_December": [
            "October_Observances",
            "November_Observances",
            "December_Observances",
            "Month_Wise_Revision",
            "Important_Dates",
            "One_Liners",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "20_UPSC_SSC_Railway_PYQ_Themes": [
            "National_Days_PYQ",
            "International_Days_PYQ",
            "Environment_Days_PYQ",
            "Science_Days_PYQ",
            "Sports_Days_PYQ",
            "Month_Wise_PYQ",
            "Revision",
            "High_Yield_Areas"
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

    print("\n✅ Important Dates structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_important_dates_structure()