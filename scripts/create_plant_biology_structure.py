import os
import shutil

def create_plant_biology_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "plant-biology"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Plant_Biology": [
            "Characteristics_of_Plants",
            "Importance_of_Plants",
            "Plant_Diversity",
            "Basic_Concepts"
        ],

        "02_Plant_Morphology": [
            "Root",
            "Stem",
            "Leaf",
            "Morphological_Modifications"
        ],

        "03_Root_System": [
            "Tap_Root",
            "Fibrous_Root",
            "Adventitious_Root",
            "Root_Modifications"
        ],

        "04_Stem_System": [
            "Stem_Structure",
            "Underground_Stems",
            "Aerial_Modifications",
            "Functions"
        ],

        "05_Leaf": [
            "Leaf_Structure",
            "Venation",
            "Phyllotaxy",
            "Leaf_Modifications"
        ],

        "06_Flower": [
            "Flower_Structure",
            "Floral_Whorls",
            "Inflorescence",
            "Functions"
        ],

        "07_Fruit_and_Seed": [
            "Fruit_Formation",
            "Types_of_Fruits",
            "Seed_Structure",
            "Seed_Dispersal"
        ],

        "08_Plant_Anatomy": [
            "Tissues",
            "Tissue_Systems",
            "Internal_Structure",
            "Important_Facts"
        ],

        "09_Plant_Tissues": [
            "Meristematic_Tissues",
            "Permanent_Tissues",
            "Simple_Tissues",
            "Complex_Tissues"
        ],

        "10_Xylem_and_Phlem": [
            "Xylem",
            "Phloem",
            "Transport_in_Plants",
            "Functions"
        ],

        "11_Photosynthesis": [
            "Photosynthesis_Process",
            "Chlorophyll",
            "Light_Reaction",
            "Dark_Reaction"
        ],

        "12_Plant_Nutrition": [
            "Autotrophic_Nutrition",
            "Mineral_Nutrition",
            "Macronutrients",
            "Micronutrients"
        ],

        "13_Transpiration": [
            "Transpiration_Process",
            "Stomata",
            "Factors_Affecting",
            "Importance"
        ],

        "14_Transport_in_Plants": [
            "Water_Transport",
            "Mineral_Transport",
            "Translocation",
            "Ascent_of_Sap"
        ],

        "15_Plant_Hormones": [
            "Auxins",
            "Gibberellins",
            "Cytokinins",
            "Abscisic_Acid"
        ],

        "16_Plant_Movements": [
            "Tropic_Movements",
            "Nastic_Movements",
            "Phototropism",
            "Geotropism"
        ],

        "17_Plant_Respiration": [
            "Aerobic_Respiration",
            "Anaerobic_Respiration",
            "Respiratory_Quotient",
            "Importance"
        ],

        "18_Reproduction_in_Plants": [
            "Asexual_Reproduction",
            "Vegetative_Propagation",
            "Sexual_Reproduction",
            "Life_Cycle"
        ],

        "19_Pollination_and_Fertilization": [
            "Pollination",
            "Agents_of_Pollination",
            "Double_Fertilization",
            "Post_Fertilization"
        ],

        "20_Economic_Botany": [
            "Food_Crops",
            "Cash_Crops",
            "Medicinal_Plants",
            "Industrial_Plants"
        ],

        "21_Plant_Diseases": [
            "Fungal_Diseases",
            "Bacterial_Diseases",
            "Viral_Diseases",
            "Disease_Control"
        ],

        "22_Plant_Adaptations": [
            "Desert_Plants",
            "Aquatic_Plants",
            "Epiphytes",
            "Special_Adaptations"
        ],

        "23_Scientists_and_Discoveries": [
            "Jagadish_Chandra_Bose",
            "Julius_von_Sachs",
            "Stephen_Hales",
            "Important_Contributions"
        ],

        "24_Exam_Focused_Plant_Biology": [
            "Important_Diagrams",
            "NCERT_Facts",
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

    print("\n✅ Plant Biology structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_plant_biology_structure()