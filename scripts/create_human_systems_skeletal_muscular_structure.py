import os
import shutil

def create_human_systems_skeletal_muscular_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "human-systems-skeletal-muscular"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Skeletal_System": [
            "Overview",
            "Functions_of_Skeleton",
            "Human_Skeleton",
            "Important_Facts"
        ],

        "02_Bones": [
            "Bone_Structure",
            "Types_of_Bones",
            "Bone_Composition",
            "Functions"
        ],

        "03_Axial_Skeleton": [
            "Skull",
            "Vertebral_Column",
            "Rib_Cage",
            "Functions"
        ],

        "04_Appendicular_Skeleton": [
            "Pectoral_Girdle",
            "Pelvic_Girdle",
            "Upper_Limbs",
            "Lower_Limbs"
        ],

        "05_Joints": [
            "Fibrous_Joints",
            "Cartilaginous_Joints",
            "Synovial_Joints",
            "Examples"
        ],

        "06_Cartilage_and_Ligaments": [
            "Cartilage",
            "Ligaments",
            "Tendons",
            "Functions"
        ],

        "07_Muscular_System": [
            "Overview",
            "Functions_of_Muscles",
            "Muscle_Organization",
            "Important_Facts"
        ],

        "08_Types_of_Muscles": [
            "Skeletal_Muscles",
            "Smooth_Muscles",
            "Cardiac_Muscles",
            "Comparison"
        ],

        "09_Muscle_Contraction": [
            "Sliding_Filament_Theory",
            "Actin_and_Myosin",
            "Neuromuscular_Junction",
            "Mechanism"
        ],

        "10_Locomotion_and_Movement": [
            "Movement",
            "Locomotion",
            "Role_of_Bones",
            "Role_of_Muscles"
        ],

        "11_Posture_and_Body_Mechanics": [
            "Posture",
            "Balance",
            "Coordination",
            "Body_Mechanics"
        ],

        "12_Bone_Formation_and_Growth": [
            "Ossification",
            "Bone_Growth",
            "Bone_Remodeling",
            "Important_Facts"
        ],

        "13_Mineral_Homeostasis": [
            "Calcium",
            "Phosphorus",
            "Vitamin_D",
            "Regulation"
        ],

        "14_Common_Skeletal_Disorders": [
            "Arthritis",
            "Osteoporosis",
            "Rickets",
            "Fractures"
        ],

        "15_Common_Muscular_Disorders": [
            "Muscular_Dystrophy",
            "Cramps",
            "Myasthenia_Gravis",
            "Common_Disorders"
        ],

        "16_Sports_and_Human_Movement": [
            "Exercise",
            "Physical_Fitness",
            "Sports_Injuries",
            "Performance"
        ],

        "17_Comparative_Locomotion": [
            "Fish",
            "Birds",
            "Mammals",
            "Adaptations"
        ],

        "18_Scientists_and_Discoveries": [
            "Andreas_Vesalius",
            "William_Harvey",
            "Important_Contributions",
            "Historical_Facts"
        ],

        "19_Previous_Year_Themes": [
            "UPSC",
            "SSC",
            "Railway",
            "State_PCS"
        ],

        "20_Revision_and_Exam_Preparation": [
            "One_Liner_Revision",
            "Important_Diagrams",
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

    print("\n✅ Human Systems (Skeletal & Muscular) structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_human_systems_skeletal_muscular_structure()