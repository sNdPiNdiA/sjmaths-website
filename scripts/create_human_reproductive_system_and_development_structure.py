import os
import shutil

def create_human_reproductive_system_and_development_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "human-reproductive-system-and-development"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Reproduction": [
            "Need_for_Reproduction",
            "Types_of_Reproduction",
            "Asexual_Reproduction",
            "Sexual_Reproduction"
        ],

        "02_Male_Reproductive_System": [
            "Testes",
            "Accessory_Glands",
            "Male_Genital_Ducts",
            "Functions"
        ],

        "03_Female_Reproductive_System": [
            "Ovaries",
            "Fallopian_Tubes",
            "Uterus",
            "Functions"
        ],

        "04_Gametogenesis": [
            "Spermatogenesis",
            "Oogenesis",
            "Gamete_Formation",
            "Important_Facts"
        ],

        "05_Reproductive_Hormones": [
            "Testosterone",
            "Estrogen",
            "Progesterone",
            "Hormonal_Control"
        ],

        "06_Menstrual_Cycle": [
            "Menstrual_Phase",
            "Follicular_Phase",
            "Ovulation",
            "Luteal_Phase"
        ],

        "07_Fertilization": [
            "Fusion_of_Gametes",
            "Zygote_Formation",
            "Site_of_Fertilization",
            "Important_Facts"
        ],

        "08_Embryonic_Development": [
            "Cleavage",
            "Blastocyst",
            "Implantation",
            "Gastrulation"
        ],

        "09_Pregnancy_and_Gestation": [
            "Pregnancy",
            "Placenta",
            "Foetal_Development",
            "Gestation_Period"
        ],

        "10_Parturition_and_Lactation": [
            "Childbirth",
            "Parturition",
            "Milk_Production",
            "Lactation"
        ],

        "11_Twins_and_Multiple_Births": [
            "Identical_Twins",
            "Fraternal_Twins",
            "Multiple_Pregnancy",
            "Important_Facts"
        ],

        "12_Reproductive_Health": [
            "Maternal_Health",
            "Adolescent_Health",
            "Reproductive_Hygiene",
            "Awareness"
        ],

        "13_Contraceptive_Methods": [
            "Natural_Methods",
            "Barrier_Methods",
            "Hormonal_Methods",
            "Surgical_Methods"
        ],

        "14_Family_Planning": [
            "Population_Control",
            "Family_Welfare_Programs",
            "Government_Initiatives",
            "Important_Facts"
        ],

        "15_Assisted_Reproductive_Technologies": [
            "IVF",
            "Test_Tube_Baby",
            "ICSI",
            "Surrogacy"
        ],

        "16_Stem_Cells_and_Development": [
            "Stem_Cells",
            "Embryonic_Stem_Cells",
            "Applications",
            "Research"
        ],

        "17_Human_Growth_and_Development": [
            "Infancy",
            "Childhood",
            "Adolescence",
            "Adulthood"
        ],

        "18_Reproduction_in_Animals": [
            "Oviparous",
            "Viviparous",
            "External_Fertilization",
            "Internal_Fertilization"
        ],

        "19_Reproduction_in_Humans_Exam_Facts": [
            "Important_Diagrams",
            "Frequently_Asked_Facts",
            "NCERT_Facts",
            "High_Yield_Topics"
        ],

        "20_Population_and_Demography": [
            "Population_Growth",
            "Birth_Rate",
            "Death_Rate",
            "Demographic_Transition"
        ],

        "21_National_Programs": [
            "Family_Planning_Program",
            "RMNCHA",
            "Maternal_Health_Schemes",
            "Population_Policies"
        ],

        "22_Scientists_and_Discoveries": [
            "Robert_Edwards",
            "Patrick_Steptoe",
            "Karl_Ernst_von_Baer",
            "Important_Contributions"
        ],

        "23_Previous_Year_Question_Themes": [
            "UPSC_Themes",
            "SSC_Themes",
            "Railway_Themes",
            "State_PCS_Themes"
        ],

        "24_Revision_and_Exam_Preparation": [
            "One_Liner_Revision",
            "Flash_Revision",
            "Concept_Traps",
            "Common_Mistakes"
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

    print("\n✅ Human Reproductive System and Development structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_human_reproductive_system_and_development_structure()