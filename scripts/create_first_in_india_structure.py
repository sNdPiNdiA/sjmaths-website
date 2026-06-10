import os
import shutil

def create_first_in_india_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "first-in-india"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_First_Presidents_and_Governors": [
            "First_President",
            "First_Vice_President",
            "First_Governor_General",
            "First_Indian_Governor_General",
            "First_Female_Governor",
            "First_State_Governor",
            "First_Chief_Election_Commissioner",
            "Important_Facts"
        ],

        "02_First_Prime_Ministers_and_Ministers": [
            "First_Prime_Minister",
            "First_Deputy_Prime_Minister",
            "First_Home_Minister",
            "First_Finance_Minister",
            "First_Defence_Minister",
            "First_Foreign_Minister",
            "First_Cabinet",
            "Important_Facts"
        ],

        "03_First_Parliament_and_Judiciary": [
            "First_Lok_Sabha_Speaker",
            "First_Rajya_Sabha_Chairman",
            "First_Chief_Justice",
            "First_Female_Judge",
            "First_Female_Chief_Justice_HC",
            "First_Attorney_General",
            "First_Solicitor_General",
            "Important_Facts"
        ],

        "04_First_Women_in_India": [
            "First_Woman_President",
            "First_Woman_Prime_Minister",
            "First_Woman_Governor",
            "First_Woman_Chief_Minister",
            "First_Woman_Justice",
            "First_Woman_IPS",
            "First_Woman_IAFS",
            "Important_Facts"
        ],

        "05_First_Civil_Services_and_Administration": [
            "First_ICS_Officer",
            "First_Indian_ICS",
            "First_Cabinet_Secretary",
            "First_Chief_Election_Commissioner",
            "First_CAG",
            "First_UPSC_Chairman",
            "First_Chief_Information_Commissioner",
            "Important_Facts"
        ],

        "06_First_Defence_Personalities": [
            "First_Field_Marshal",
            "First_CDS",
            "First_Army_Chief",
            "First_Navy_Chief",
            "First_Air_Chief",
            "First_Param_Vir_Chakra",
            "First_Female_Army_Officer",
            "Important_Facts"
        ],

        "07_First_Science_and_Technology": [
            "First_Indian_Scientist",
            "First_Indian_Nobel_Laureate",
            "First_Satellite",
            "First_Missile",
            "First_Nuclear_Test",
            "First_Supercomputer",
            "First_Space_Mission",
            "Important_Facts"
        ],

        "08_First_Space_and_Aviation": [
            "First_Indian_In_Space",
            "First_Indian_Woman_In_Space",
            "First_Indian_Astronaut",
            "First_Commercial_Flight",
            "First_Airport",
            "First_Airline",
            "First_Helicopter_Pilot",
            "Important_Facts"
        ],

        "09_First_Sports_Personalities": [
            "First_Olympic_Medal",
            "First_Individual_Olympic_Medal",
            "First_Olympic_Gold",
            "First_Cricket_Captain",
            "First_Test_Captain",
            "First_Chess_Grandmaster",
            "First_Paralympic_Medal",
            "Important_Facts"
        ],

        "10_First_Literature_and_Arts": [
            "First_Jnanpith_Awardee",
            "First_Bharat_Ratna",
            "First_Oscar_Winner",
            "First_Booker_Winner",
            "First_Sahitya_Akademi_Awardee",
            "First_Dadasaheb_Phalke_Awardee",
            "First_Grammy_Winner",
            "Important_Facts"
        ],

        "11_First_Mountains_and_Expeditions": [
            "First_Everest_Climber",
            "First_Indian_Everest_Climber",
            "First_Indian_Woman_Everest",
            "First_Antarctica_Expedition",
            "First_Arctic_Expedition",
            "First_Himalayan_Expedition",
            "Mountaineering_Records",
            "Important_Facts"
        ],

        "12_First_Education_and_Academics": [
            "First_University",
            "First_Modern_University",
            "First_IIT",
            "First_IIM",
            "First_Medical_College",
            "First_Engineering_College",
            "First_Open_University",
            "Important_Facts"
        ],

        "13_First_Media_and_Communication": [
            "First_Newspaper",
            "First_English_Newspaper",
            "First_Hindi_Newspaper",
            "First_Radio_Broadcast",
            "First_Doorshan_Telecast",
            "First_Private_Channel",
            "First_Internet_Service",
            "Important_Facts"
        ],

        "14_First_Transport_and_Infrastructure": [
            "First_Railway_Line",
            "First_Metro_Rail",
            "First_Expressway",
            "First_National_Highway",
            "First_Port",
            "First_International_Airport",
            "First_Smart_City",
            "Important_Facts"
        ],

        "15_First_Banking_and_Economy": [
            "First_Bank",
            "First_Indian_Bank",
            "First_Stock_Exchange",
            "First_Mutual_Fund",
            "First_Insurance_Company",
            "First_SEBI_Chairman",
            "First_RBI_Governor",
            "Important_Facts"
        ],

        "16_First_States_and_Politics": [
            "First_Linguistic_State",
            "First_Chief_Minister",
            "First_State_Reorganization",
            "First_Elected_Government",
            "First_Coalition_Government",
            "First_Municipal_Corporation",
            "First_Panchayat",
            "Important_Facts"
        ],

        "17_First_Environment_and_Conservation": [
            "First_National_Park",
            "First_Biosphere_Reserve",
            "First_Tiger_Reserve",
            "First_Ramsar_Site",
            "First_Marine_Park",
            "First_Eco_Sensitive_Zone",
            "First_Wildlife_Sanctuary",
            "Important_Facts"
        ],

        "18_First_Current_Affairs_Milestones": [
            "Recent_Firsts",
            "Technological_Firsts",
            "Space_Firsts",
            "Sports_Firsts",
            "Administrative_Firsts",
            "Women_Firsts",
            "Economic_Firsts",
            "Monthly_Updates"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Political_Firsts",
            "Scientific_Firsts",
            "Sports_Firsts",
            "Women_Firsts",
            "Historical_Firsts",
            "Institutional_Firsts",
            "PYQ_Analysis",
            "Revision"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Firsts",
            "One_Liner_Revision",
            "Memory_Hooks",
            "Flashcard_Themes",
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

        print(f"[+] {category}")

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            print(f"    [+] {topic}")

            for filename in leaf_files:

                file_path = os.path.join(topic_path, filename)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ First in India structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_first_in_india_structure()