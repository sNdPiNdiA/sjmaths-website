import os
import shutil

def create_human_systems_digestive_respiratory_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "human-systems-digestive-respiratory"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Digestion": [
            "Nutrition_and_Digestion",
            "Types_of_Nutrition",
            "Digestive_Process",
            "Overview"
        ],

        "02_Alimentary_Canal": [
            "Mouth",
            "Pharynx_and_Esophagus",
            "Stomach",
            "Intestines"
        ],

        "03_Mouth_and_Teeth": [
            "Teeth_Types",
            "Dental_Formula",
            "Salivary_Glands",
            "Functions"
        ],

        "04_Stomach": [
            "Structure",
            "Gastric_Glands",
            "Gastric_Juice",
            "Functions"
        ],

        "05_Small_Intestine": [
            "Duodenum",
            "Jejunum",
            "Ileum",
            "Absorption"
        ],

        "06_Large_Intestine": [
            "Colon",
            "Rectum",
            "Water_Absorption",
            "Functions"
        ],

        "07_Digestive_Glands": [
            "Liver",
            "Pancreas",
            "Salivary_Glands",
            "Digestive_Enzymes"
        ],

        "08_Liver": [
            "Structure",
            "Bile_Production",
            "Functions",
            "Important_Facts"
        ],

        "09_Pancreas": [
            "Exocrine_Function",
            "Digestive_Enzymes",
            "Pancreatic_Juice",
            "Functions"
        ],

        "10_Digestive_Enzymes": [
            "Carbohydrate_Digestion",
            "Protein_Digestion",
            "Fat_Digestion",
            "Important_Enzymes"
        ],

        "11_Absorption_and_Assimilation": [
            "Absorption",
            "Assimilation",
            "Villi",
            "Transport_of_Nutrients"
        ],

        "12_Digestive_Disorders": [
            "Acidity",
            "Ulcer",
            "Constipation",
            "Diarrhoea"
        ],

        "13_Introduction_to_Respiration": [
            "Respiration_Basics",
            "Breathing",
            "Cellular_Respiration",
            "Overview"
        ],

        "14_Human_Respiratory_System": [
            "Nasal_Cavity",
            "Trachea",
            "Bronchi",
            "Lungs"
        ],

        "15_Lungs": [
            "Structure_of_Lungs",
            "Alveoli",
            "Pleura",
            "Functions"
        ],

        "16_Mechanism_of_Breathing": [
            "Inhalation",
            "Exhalation",
            "Diaphragm",
            "Intercostal_Muscles"
        ],

        "17_Gas_Exchange": [
            "Alveolar_Exchange",
            "Oxygen_Transport",
            "Carbon_Dioxide_Transport",
            "Diffusion"
        ],

        "18_Respiratory_Volumes": [
            "Tidal_Volume",
            "Vital_Capacity",
            "Residual_Volume",
            "Lung_Capacities"
        ],

        "19_Cellular_Respiration": [
            "Aerobic_Respiration",
            "Anaerobic_Respiration",
            "ATP_Production",
            "Energy_Release"
        ],

        "20_Respiratory_Disorders": [
            "Asthma",
            "Bronchitis",
            "Pneumonia",
            "Tuberculosis"
        ],

        "21_Smoking_and_Health": [
            "Tobacco_Effects",
            "Lung_Damage",
            "Passive_Smoking",
            "Health_Risks"
        ],

        "22_Respiration_in_Animals": [
            "Fish",
            "Amphibians",
            "Insects",
            "Mammals"
        ],

        "23_Scientists_and_Discoveries": [
            "Antoine_Lavoisier",
            "Joseph_Priestley",
            "William_Beaumont",
            "Important_Contributions"
        ],

        "24_Exam_Focused_Digestive_Respiratory": [
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

    print("\n✅ Human Systems (Digestive & Respiratory) structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_human_systems_digestive_respiratory_structure()