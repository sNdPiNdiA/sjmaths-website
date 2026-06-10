import os
import shutil

def create_national_parks_and_sanctuaries_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "national-parks-and-sanctuaries"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_National_Parks_India": [
            "Jim_Corbett_National_Park",
            "Kaziranga_National_Park",
            "Ranthambore_National_Park",
            "Kanha_National_Park",
            "Bandipur_National_Park",
            "Sundarbans_National_Park",
            "Gir_National_Park",
            "Important_Facts"
        ],

        "02_Northern_India_Protected_Areas": [
            "Jammu_Kashmir_Parks",
            "Himachal_Parks",
            "Uttarakhand_Parks",
            "Punjab_Protected_Areas",
            "Haryana_Protected_Areas",
            "Delhi_Protected_Areas",
            "UP_Protected_Areas",
            "Important_Facts"
        ],

        "03_Southern_India_Protected_Areas": [
            "Andhra_Protected_Areas",
            "Telangana_Protected_Areas",
            "TamilNadu_Protected_Areas",
            "Karnataka_Protected_Areas",
            "Kerala_Protected_Areas",
            "Puducherry_Protected_Areas",
            "Lakshadweep_Protected_Areas",
            "Important_Facts"
        ],

        "04_Eastern_and_Northeastern_Protected_Areas": [
            "WestBengal_Protected_Areas",
            "Odisha_Protected_Areas",
            "Bihar_Protected_Areas",
            "Jharkhand_Protected_Areas",
            "Assam_Protected_Areas",
            "Arunachal_Protected_Areas",
            "Meghalaya_Protected_Areas",
            "Important_Facts"
        ],

        "05_Western_and_Central_Protected_Areas": [
            "Rajasthan_Protected_Areas",
            "Gujarat_Protected_Areas",
            "Maharashtra_Protected_Areas",
            "Goa_Protected_Areas",
            "MadhyaPradesh_Protected_Areas",
            "Chhattisgarh_Protected_Areas",
            "Central_India_Parks",
            "Important_Facts"
        ],

        "06_Wildlife_Sanctuaries": [
            "Keoladeo",
            "Gahirmatha",
            "National_Chambal",
            "Kumbhalgarh",
            "Bhadra",
            "Nal_Sarovar",
            "Vedanthangal",
            "Important_Facts"
        ],

        "07_Tiger_Reserves": [
            "Corbett_Tiger_Reserve",
            "Bandhavgarh_Tiger_Reserve",
            "Kanha_Tiger_Reserve",
            "Ranthambore_Tiger_Reserve",
            "Sundarbans_Tiger_Reserve",
            "Nagarhole_Tiger_Reserve",
            "Periyar_Tiger_Reserve",
            "Important_Facts"
        ],

        "08_Biosphere_Reserves": [
            "Nilgiri_Biosphere",
            "Nanda_Devi",
            "Gulf_of_Mannar",
            "Sundarbans_Biosphere",
            "Pachmarhi",
            "Simlipal",
            "Great_Nicobar",
            "Important_Facts"
        ],

        "09_Ramsar_Sites": [
            "Chilika_Lake",
            "Loktak_Lake",
            "Wular_Lake",
            "Keoladeo",
            "Sambhar_Lake",
            "East_Kolkata_Wetlands",
            "Ashtamudi_Lake",
            "Important_Facts"
        ],

        "10_Elephant_Reserves": [
            "Singhbhum",
            "Nilgiri",
            "Mayurjharna",
            "Periyar",
            "Anamalai",
            "Mysore",
            "Kameng",
            "Important_Facts"
        ],

        "11_Bird_Sanctuaries": [
            "Bharatpur",
            "Nal_Sarovar",
            "Vedanthangal",
            "Ranganathittu",
            "Sultanpur",
            "Kumarakom",
            "Chilika_Bird_Areas",
            "Important_Facts"
        ],

        "12_Marine_Protected_Areas": [
            "Gulf_of_Kutch",
            "Gulf_of_Mannar",
            "Sundarbans_Mangroves",
            "Mahatma_Gandhi_Marine_Park",
            "Rani_Jhansi_Marine_Park",
            "Marine_Sanctuaries",
            "Coastal_Ecosystems",
            "Important_Facts"
        ],

        "13_Endangered_Species_Habitats": [
            "Asiatic_Lion",
            "Royal_Bengal_Tiger",
            "One_Horned_Rhino",
            "Snow_Leopard",
            "Red_Panda",
            "Hangul",
            "Great_Indian_Bustard",
            "Important_Facts"
        ],

        "14_UNESCO_and_Global_Recognition": [
            "UNESCO_Natural_Heritage",
            "UNESCO_Mixed_Sites",
            "World_Heritage_Parks",
            "Biosphere_Network",
            "Ramsar_Convention",
            "Global_Recognition",
            "International_Status",
            "Important_Facts"
        ],

        "15_Map_Based_Protected_Areas": [
            "North_India_Map",
            "South_India_Map",
            "East_India_Map",
            "West_India_Map",
            "Northeast_Map",
            "Island_Map",
            "River_Map",
            "Important_Facts"
        ],

        "16_Park_River_State_Matching": [
            "Park_State_Matching",
            "Park_River_Matching",
            "Reserve_State_Matching",
            "Sanctuary_State_Matching",
            "Wetland_State_Matching",
            "Species_Park_Matching",
            "Map_Matching",
            "Important_Facts"
        ],

        "17_Protected_Area_Conservation": [
            "Project_Tiger",
            "Project_Elephant",
            "Project_Snow_Leopard",
            "Crocodile_Conservation",
            "Rhino_Conservation",
            "Vulture_Conservation",
            "Lion_Conservation",
            "Important_Facts"
        ],

        "18_Current_Affairs_Protected_Areas": [
            "New_Ramsar_Sites",
            "New_Tiger_Reserves",
            "New_National_Parks",
            "UNESCO_Updates",
            "Conservation_Updates",
            "Species_Updates",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "National_Park_PYQ",
            "Tiger_Reserve_PYQ",
            "Ramsar_PYQ",
            "Biosphere_PYQ",
            "Species_PYQ",
            "Map_Based_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Parks",
            "Top_100_Sanctuaries",
            "Top_100_Ramsar_Sites",
            "Memory_Hooks",
            "Flashcards",
            "Common_Mistakes",
            "Concept_Traps",
            "Rapid_Revision"
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

    print("\n✅ National Parks, Sanctuaries, Tiger Reserves, Biosphere Reserves & Ramsar Sites structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_national_parks_and_sanctuaries_structure()