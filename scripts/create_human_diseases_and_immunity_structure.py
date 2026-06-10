import os
import shutil

def create_human_diseases_and_immunity_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "human-diseases-and-immunity"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Diseases": [
            "Disease_Classification",
            "Communicable_Diseases",
            "Non_Communicable_Diseases",
            "Disease_Causation"
        ],

        "02_Pathogens": [
            "Bacteria",
            "Viruses",
            "Fungi",
            "Protozoa"
        ],

        "03_Parasitic_Diseases": [
            "Helminths",
            "Roundworms",
            "Tapeworms",
            "Parasitic_Infections"
        ],

        "04_Bacterial_Diseases": [
            "Tuberculosis",
            "Typhoid",
            "Cholera",
            "Leprosy"
        ],

        "05_Viral_Diseases": [
            "COVID_19",
            "Influenza",
            "Rabies",
            "Polio"
        ],

        "06_Viral_Diseases_II": [
            "Dengue",
            "Japanese_Encephalitis",
            "Hepatitis",
            "AIDS"
        ],

        "07_Protozoan_Diseases": [
            "Malaria",
            "Amoebiasis",
            "Kala_Azar",
            "Sleeping_Sickness"
        ],

        "08_Fungal_Diseases": [
            "Ringworm",
            "Candidiasis",
            "Athletes_Foot",
            "Common_Fungal_Infections"
        ],

        "09_Vector_Borne_Diseases": [
            "Mosquito_Borne",
            "Housefly_Borne",
            "Tick_Borne",
            "Vector_Control"
        ],

        "10_Water_Borne_Diseases": [
            "Cholera",
            "Typhoid",
            "Diarrhoea",
            "Prevention"
        ],

        "11_Air_Borne_Diseases": [
            "Tuberculosis",
            "Influenza",
            "COVID_19",
            "Control_Measures"
        ],

        "12_Sexually_Transmitted_Diseases": [
            "HIV_AIDS",
            "Syphilis",
            "Gonorrhoea",
            "Prevention"
        ],

        "13_Non_Communicable_Diseases": [
            "Cancer",
            "Diabetes",
            "Hypertension",
            "Cardiovascular_Diseases"
        ],

        "14_Deficiency_Diseases": [
            "Vitamin_Deficiencies",
            "Mineral_Deficiencies",
            "Anaemia",
            "Goitre"
        ],

        "15_Allergies_and_Autoimmune_Disorders": [
            "Allergy",
            "Asthma",
            "Autoimmune_Diseases",
            "Hypersensitivity"
        ],

        "16_Introduction_to_Immunity": [
            "Immunity_Basics",
            "Innate_Immunity",
            "Acquired_Immunity",
            "Immune_System"
        ],

        "17_Immune_System_Components": [
            "White_Blood_Cells",
            "Lymphocytes",
            "Antibodies",
            "Antigens"
        ],

        "18_Types_of_Immunity": [
            "Active_Immunity",
            "Passive_Immunity",
            "Natural_Immunity",
            "Artificial_Immunity"
        ],

        "19_Vaccines_and_Vaccination": [
            "Vaccines",
            "Immunization",
            "Booster_Doses",
            "Vaccination_Programs"
        ],

        "20_Public_Health_and_Epidemiology": [
            "Epidemics",
            "Pandemics",
            "Endemics",
            "Disease_Surveillance"
        ],

        "21_National_Health_Programs": [
            "TB_Control_Program",
            "Universal_Immunization",
            "National_AIDS_Control",
            "Public_Health_Missions"
        ],

        "22_Disease_Prevention": [
            "Personal_Hygiene",
            "Sanitation",
            "Nutrition_and_Health",
            "Preventive_Measures"
        ],

        "23_Scientists_and_Discoveries": [
            "Edward_Jenner",
            "Louis_Pasteur",
            "Robert_Koch",
            "Alexander_Fleming"
        ],

        "24_Exam_Focused_Diseases_and_Immunity": [
            "Frequently_Asked_Diseases",
            "Disease_Agent_Matching",
            "One_Liner_Revision",
            "Previous_Year_Themes"
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
        "diagram_based.json",
        "statement_based.json",
        "odd_one_out.json",
        "pair_matching.json",
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
        "common_mistakes.json"
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

    print("\n✅ Human Diseases and Immunity structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_human_diseases_and_immunity_structure()