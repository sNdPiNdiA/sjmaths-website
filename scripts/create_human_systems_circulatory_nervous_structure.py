import os
import shutil

def create_human_systems_circulatory_nervous_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "human-systems-circulatory-nervous"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Human_Body_Systems": [
            "Levels_of_Organization",
            "Organ_Systems",
            "Homeostasis",
            "Body_Coordination"
        ],

        "02_Blood": [
            "Composition_of_Blood",
            "RBC",
            "WBC",
            "Platelets"
        ],

        "03_Blood_Groups": [
            "ABO_System",
            "Rh_Factor",
            "Blood_Transfusion",
            "Important_Facts"
        ],

        "04_Heart": [
            "Structure_of_Heart",
            "Heart_Chambers",
            "Valves",
            "Cardiac_Cycle"
        ],

        "05_Blood_Vessels": [
            "Arteries",
            "Veins",
            "Capillaries",
            "Circulation_Pathway"
        ],

        "06_Circulatory_System": [
            "Double_Circulation",
            "Pulmonary_Circulation",
            "Systemic_Circulation",
            "Functions"
        ],

        "07_Lymphatic_System": [
            "Lymph",
            "Lymph_Nodes",
            "Lymphatic_Vessels",
            "Functions"
        ],

        "08_Nervous_System_Overview": [
            "Neuron",
            "Nerve_Impulse",
            "Organization",
            "Functions"
        ],

        "09_Central_Nervous_System": [
            "Brain",
            "Cerebrum",
            "Cerebellum",
            "Medulla"
        ],

        "10_Spinal_Cord": [
            "Structure",
            "Functions",
            "Reflex_Actions",
            "Important_Facts"
        ],

        "11_Peripheral_Nervous_System": [
            "Cranial_Nerves",
            "Spinal_Nerves",
            "Somatic_System",
            "Functions"
        ],

        "12_Autonomic_Nervous_System": [
            "Sympathetic_System",
            "Parasympathetic_System",
            "Autonomic_Control",
            "Functions"
        ],

        "13_Sense_Organs_Eye": [
            "Human_Eye",
            "Retina",
            "Vision",
            "Eye_Defects"
        ],

        "14_Sense_Organs_Ear": [
            "Human_Ear",
            "Hearing",
            "Balance",
            "Ear_Parts"
        ],

        "15_Sense_Organs_Others": [
            "Skin",
            "Tongue",
            "Nose",
            "Sensory_Receptors"
        ],

        "16_Endocrine_System": [
            "Hormones",
            "Endocrine_Glands",
            "Functions",
            "Coordination"
        ],

        "17_Pituitary_and_Thyroid": [
            "Pituitary_Gland",
            "Thyroid_Gland",
            "Hormones",
            "Important_Facts"
        ],

        "18_Adrenal_and_Pancreas": [
            "Adrenal_Gland",
            "Pancreas",
            "Insulin",
            "Hormonal_Control"
        ],

        "19_Excretory_System": [
            "Kidneys",
            "Nephron",
            "Urine_Formation",
            "Functions"
        ],

        "20_Excretory_Organs": [
            "Ureter",
            "Urinary_Bladder",
            "Urethra",
            "Excretion_Pathway"
        ],

        "21_Homeostasis": [
            "Water_Balance",
            "Salt_Balance",
            "Temperature_Regulation",
            "Internal_Environment"
        ],

        "22_Common_Disorders": [
            "Hypertension",
            "Heart_Disease",
            "Kidney_Disorders",
            "Neurological_Disorders"
        ],

        "23_Scientists_and_Discoveries": [
            "William_Harvey",
            "Ivan_Pavlov",
            "Camillo_Golgi",
            "Santiago_Ramon_y_Cajal"
        ],

        "24_Exam_Focused_Human_Systems": [
            "Important_Diagrams",
            "Frequently_Asked_Facts",
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

    print("\n✅ Human Systems (Circulatory & Nervous) structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_human_systems_circulatory_nervous_structure()