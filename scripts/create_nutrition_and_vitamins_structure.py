import os
import shutil

def create_nutrition_and_vitamins_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "nutrition-and-vitamins"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Nutrition": [
            "Nutrition_Basics",
            "Importance_of_Nutrition",
            "Types_of_Nutrition",
            "Nutritional_Requirements"
        ],

        "02_Macronutrients": [
            "Carbohydrates",
            "Proteins",
            "Fats",
            "Functions"
        ],

        "03_Carbohydrates": [
            "Simple_Carbohydrates",
            "Complex_Carbohydrates",
            "Sources",
            "Functions"
        ],

        "04_Proteins": [
            "Protein_Structure",
            "Essential_Amino_Acids",
            "Sources",
            "Functions"
        ],

        "05_Fats_and_Lipids": [
            "Saturated_Fats",
            "Unsaturated_Fats",
            "Cholesterol",
            "Functions"
        ],

        "06_Micronutrients": [
            "Vitamins",
            "Minerals",
            "Trace_Elements",
            "Functions"
        ],

        "07_Vitamins_Overview": [
            "Classification",
            "Functions",
            "Sources",
            "Deficiency_Diseases"
        ],

        "08_Fat_Soluble_Vitamins": [
            "Vitamin_A",
            "Vitamin_D",
            "Vitamin_E",
            "Vitamin_K"
        ],

        "09_Water_Soluble_Vitamins": [
            "Vitamin_B_Complex",
            "Vitamin_B12",
            "Vitamin_C",
            "Functions"
        ],

        "10_Vitamin_Deficiency_Diseases": [
            "Night_Blindness",
            "Scurvy",
            "Beriberi",
            "Rickets"
        ],

        "11_Minerals": [
            "Calcium",
            "Phosphorus",
            "Iron",
            "Iodine"
        ],

        "12_Trace_Elements": [
            "Zinc",
            "Copper",
            "Selenium",
            "Fluorine"
        ],

        "13_Balanced_Diet": [
            "Balanced_Diet_Concept",
            "Food_Groups",
            "Daily_Requirements",
            "Diet_Planning"
        ],

        "14_Malnutrition": [
            "Undernutrition",
            "Overnutrition",
            "Causes",
            "Prevention"
        ],

        "15_Protein_Energy_Malnutrition": [
            "Kwashiorkor",
            "Marasmus",
            "Symptoms",
            "Prevention"
        ],

        "16_Food_and_Health": [
            "Healthy_Eating",
            "Lifestyle_Diseases",
            "Obesity",
            "Dietary_Guidelines"
        ],

        "17_Food_Preservation": [
            "Drying",
            "Pasteurization",
            "Refrigeration",
            "Chemical_Methods"
        ],

        "18_Food_Adulteration": [
            "Common_Adulterants",
            "Detection_Methods",
            "Food_Safety",
            "Consumer_Awareness"
        ],

        "19_Public_Nutrition_Programs": [
            "Mid_Day_Meal",
            "POSHAN_Abhiyaan",
            "ICDS",
            "Food_Security_Programs"
        ],

        "20_Nutritional_Diseases": [
            "Anaemia",
            "Goitre",
            "Osteoporosis",
            "Deficiency_Disorders"
        ],

        "21_Special_Diets": [
            "Infant_Nutrition",
            "Pregnancy_Nutrition",
            "Sports_Nutrition",
            "Geriatric_Nutrition"
        ],

        "22_Food_Safety_and_Standards": [
            "FSSAI",
            "Food_Labels",
            "Food_Standards",
            "Important_Facts"
        ],

        "23_Previous_Year_Themes": [
            "UPSC",
            "SSC",
            "Railway",
            "State_PCS"
        ],

        "24_Revision_and_Exam_Preparation": [
            "One_Liner_Revision",
            "Frequently_Asked_Facts",
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

    print("\n✅ Nutrition and Vitamins structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_nutrition_and_vitamins_structure()