import os
import shutil

def create_cell_biology_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "cell-biology"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Cell_Discovery_and_History": [
            "Cell_Theory",
            "Scientists_and_Discoveries",
            "Microscope_Development",
            "Modern_Cell_Biology"
        ],

        "02_Cell_Structure": [
            "Basic_Cell_Organization",
            "Prokaryotic_Cell",
            "Eukaryotic_Cell",
            "Cell_Size_and_Shape"
        ],

        "03_Cell_Membrane": [
            "Plasma_Membrane",
            "Fluid_Mosaic_Model",
            "Membrane_Functions",
            "Transport_Across_Membrane"
        ],

        "04_Cytoplasm_and_Cell_Inclusions": [
            "Cytoplasm",
            "Cell_Inclusions",
            "Cytosol",
            "Functions"
        ],

        "05_Nucleus": [
            "Nuclear_Membrane",
            "Nucleolus",
            "Chromatin",
            "Functions_of_Nucleus"
        ],

        "06_Cell_Organelles": [
            "Endoplasmic_Reticulum",
            "Golgi_Apparatus",
            "Lysosomes",
            "Vacuoles"
        ],

        "07_Energy_Producing_Organelles": [
            "Mitochondria",
            "ATP_Production",
            "Cellular_Respiration",
            "Mitochondrial_Facts"
        ],

        "08_Plastids_and_Chloroplasts": [
            "Plastids",
            "Chloroplast",
            "Chromoplast",
            "Leucoplast"
        ],

        "09_Ribosomes_and_Protein_Synthesis": [
            "Ribosome_Structure",
            "Protein_Synthesis_Basics",
            "Types_of_Ribosomes",
            "Functions"
        ],

        "10_Cell_Division": [
            "Cell_Cycle",
            "Mitosis",
            "Meiosis",
            "Significance_of_Cell_Division"
        ],

        "11_Cell_Transport": [
            "Diffusion",
            "Osmosis",
            "Active_Transport",
            "Endocytosis_and_Exocytosis"
        ],

        "12_Cellular_Processes": [
            "Cellular_Respiration",
            "Photosynthesis_Cell_Level",
            "ATP",
            "Metabolism_Basics"
        ],

        "13_Cell_Communication": [
            "Cell_Signalling",
            "Receptors",
            "Hormonal_Communication",
            "Chemical_Messengers"
        ],

        "14_Cell_Death_and_Ageing": [
            "Apoptosis",
            "Necrosis",
            "Cell_Ageing",
            "Important_Facts"
        ],

        "15_Comparative_Cell_Biology": [
            "Plant_vs_Animal_Cell",
            "Prokaryote_vs_Eukaryote",
            "Organelles_Comparison",
            "Frequently_Asked_Differences"
        ],

        "16_Exam_Focused_Cell_Biology": [
            "Important_Diagrams",
            "Frequently_Asked_Facts",
            "One_Liner_Revision",
            "High_Yield_Topics"
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
        "short_answer.json",
        "long_answer.json",
        "pyq_upsc.json",
        "pyq_ssc.json",
        "pyq_railway.json",
        "pyq_state_pcs.json",
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

    print("\n✅ Cell Biology structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_cell_biology_structure()