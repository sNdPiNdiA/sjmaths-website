import os
import shutil

def create_dams_lakes_and_waterfalls_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "dams-lakes-and-waterfalls"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Major_Dams_of_India": [
            "Bhakra_Nangal_Dam",
            "Hirakud_Dam",
            "Tehri_Dam",
            "Sardar_Sarovar_Dam",
            "Nagarjuna_Sagar_Dam",
            "Indira_Sagar_Dam",
            "Rihand_Dam",
            "Important_Facts"
        ],

        "02_Dams_State_Wise_North_India": [
            "Jammu_and_Kashmir",
            "Himachal_Pradesh",
            "Punjab",
            "Haryana",
            "Uttarakhand",
            "Uttar_Pradesh",
            "Delhi",
            "Important_Facts"
        ],

        "03_Dams_State_Wise_South_India": [
            "Andhra_Pradesh",
            "Telangana",
            "Tamil_Nadu",
            "Karnataka",
            "Kerala",
            "Puducherry",
            "Lakshadweep",
            "Important_Facts"
        ],

        "04_Dams_State_Wise_East_West_India": [
            "West_Bengal",
            "Odisha",
            "Bihar",
            "Jharkhand",
            "Maharashtra",
            "Gujarat",
            "Goa",
            "Important_Facts"
        ],

        "05_Dams_State_Wise_Central_Northeast": [
            "Madhya_Pradesh",
            "Chhattisgarh",
            "Assam",
            "Arunachal_Pradesh",
            "Meghalaya",
            "Manipur",
            "Nagaland",
            "Important_Facts"
        ],

        "06_Important_Lakes_of_India": [
            "Wular_Lake",
            "Chilika_Lake",
            "Loktak_Lake",
            "Pulicat_Lake",
            "Vembanad_Lake",
            "Sambhar_Lake",
            "Kolleru_Lake",
            "Important_Facts"
        ],

        "07_Natural_Lakes_of_India": [
            "Freshwater_Lakes",
            "Saltwater_Lakes",
            "Tectonic_Lakes",
            "Glacial_Lakes",
            "Lagoon_Lakes",
            "Crater_Lakes",
            "Oxbow_Lakes",
            "Important_Facts"
        ],

        "08_Artificial_Lakes_and_Reservoirs": [
            "Gobind_Sagar",
            "Indira_Sagar_Reservoir",
            "Nagarjuna_Sagar_Reservoir",
            "Ukai_Reservoir",
            "Mettur_Reservoir",
            "Tehri_Reservoir",
            "Maharana_Pratap_Sagar",
            "Important_Facts"
        ],

        "09_Ramsar_Lakes_and_Wetlands": [
            "Chilika_Ramsar",
            "Loktak_Ramsar",
            "Wular_Ramsar",
            "Vembanad_Ramsar",
            "Sambhar_Ramsar",
            "Ashtamudi_Ramsar",
            "East_Kolkata_Wetlands",
            "Important_Facts"
        ],

        "10_Major_Waterfalls_of_India": [
            "Jog_Falls",
            "Dudhsagar_Falls",
            "Athirappilly_Falls",
            "Nohkalikai_Falls",
            "Shivanasamudra_Falls",
            "Chitrakote_Falls",
            "Hundru_Falls",
            "Important_Facts"
        ],

        "11_Waterfalls_State_Wise": [
            "Karnataka_Waterfalls",
            "Kerala_Waterfalls",
            "TamilNadu_Waterfalls",
            "Meghalaya_Waterfalls",
            "Jharkhand_Waterfalls",
            "Chhattisgarh_Waterfalls",
            "Maharashtra_Waterfalls",
            "Important_Facts"
        ],

        "12_World_Famous_Dams": [
            "Three_Gorges_Dam",
            "Aswan_High_Dam",
            "Hoover_Dam",
            "Itaipu_Dam",
            "Tarbela_Dam",
            "Grand_Coulee_Dam",
            "Kariba_Dam",
            "Important_Facts"
        ],

        "13_World_Famous_Lakes": [
            "Lake_Baikal",
            "Caspian_Sea",
            "Lake_Superior",
            "Lake_Victoria",
            "Dead_Sea",
            "Lake_Tanganyika",
            "Lake_Titicaca",
            "Important_Facts"
        ],

        "14_World_Famous_Waterfalls": [
            "Angel_Falls",
            "Victoria_Falls",
            "Niagara_Falls",
            "Iguazu_Falls",
            "Kaieteur_Falls",
            "Yosemite_Falls",
            "Tugela_Falls",
            "Important_Facts"
        ],

        "15_Hydroelectric_Projects": [
            "Bhakra_Project",
            "Tehri_Project",
            "Koyna_Project",
            "Sharavathi_Project",
            "Nathpa_Jhakri",
            "Sardar_Sarovar_Project",
            "Subansiri_Project",
            "Important_Facts"
        ],

        "16_Dam_River_Matching": [
            "North_India_Matching",
            "South_India_Matching",
            "East_India_Matching",
            "West_India_Matching",
            "Hydro_Projects",
            "Reservoir_Matching",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "17_Lake_River_State_Matching": [
            "Lake_State_Matching",
            "Lake_River_Matching",
            "Wetland_State_Matching",
            "Reservoir_State_Matching",
            "Lagoon_Matching",
            "Salt_Lake_Matching",
            "PYQ_Focus",
            "Important_Facts"
        ],

        "18_Current_Affairs_Dams_Lakes": [
            "New_Dam_Projects",
            "Wetland_Updates",
            "Ramsar_Updates",
            "Hydro_Power_Updates",
            "Lake_Conservation",
            "Water_Resource_Projects",
            "Monthly_Updates",
            "Important_Facts"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Dam_PYQ",
            "Lake_PYQ",
            "Waterfall_PYQ",
            "Reservoir_PYQ",
            "Ramsar_PYQ",
            "Hydro_Power_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Dams",
            "Top_100_Lakes",
            "Top_100_Waterfalls",
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

    print("\n✅ Dams, Lakes & Waterfalls structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_dams_lakes_and_waterfalls_structure()