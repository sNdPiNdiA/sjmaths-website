import os
import shutil

def create_genetics_and_evolution_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "genetics-and-evolution"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Introduction_to_Genetics": [
            "Genetics_Basics",
            "Branches_of_Genetics",
            "Importance_of_Genetics",
            "Historical_Background"
        ],

        "02_Mendelian_Genetics": [
            "Gregor_Mendel",
            "Monohybrid_Cross",
            "Dihybrid_Cross",
            "Mendels_Laws"
        ],

        "03_Heredity_and_Variation": [
            "Inherited_Traits",
            "Variation",
            "Genotype_and_Phenotype",
            "Applications"
        ],

        "04_Chromosomes": [
            "Chromosome_Structure",
            "Types_of_Chromosomes",
            "Homologous_Chromosomes",
            "Chromosome_Facts"
        ],

        "05_DNA": [
            "DNA_Structure",
            "DNA_Components",
            "Double_Helix_Model",
            "DNA_Functions"
        ],

        "06_RNA": [
            "RNA_Structure",
            "mRNA",
            "tRNA",
            "rRNA"
        ],

        "07_Genes_and_Genetic_Code": [
            "Gene_Concept",
            "Genetic_Code",
            "Codons",
            "Gene_Expression"
        ],

        "08_DNA_Replication": [
            "Replication_Process",
            "Enzymes_Involved",
            "Semi_Conservative_Model",
            "Important_Facts"
        ],

        "09_Protein_Synthesis": [
            "Transcription",
            "Translation",
            "Central_Dogma",
            "Gene_to_Protein"
        ],

        "10_Mutations": [
            "Gene_Mutations",
            "Chromosomal_Mutations",
            "Causes_of_Mutations",
            "Effects"
        ],

        "11_Human_Genetics": [
            "Human_Chromosomes",
            "Sex_Determination",
            "Pedigree_Analysis",
            "Inherited_Traits"
        ],

        "12_Genetic_Disorders": [
            "Down_Syndrome",
            "Turner_Syndrome",
            "Klinefelter_Syndrome",
            "Color_Blindness"
        ],

        "13_Blood_Groups_and_Genetics": [
            "ABO_System",
            "Rh_Factor",
            "Inheritance_Patterns",
            "Applications"
        ],

        "14_Biotechnology": [
            "Biotechnology_Basics",
            "Applications",
            "Industrial_Uses",
            "Agricultural_Uses"
        ],

        "15_Genetic_Engineering": [
            "Recombinant_DNA",
            "GM_Crops",
            "Gene_Cloning",
            "Gene_Technology"
        ],

        "16_Modern_Genetics": [
            "Human_Genome_Project",
            "DNA_Fingerprinting",
            "Gene_Therapy",
            "CRISPR"
        ],

        "17_Introduction_to_Evolution": [
            "Evolution_Concept",
            "Origin_of_Life",
            "Historical_Theories",
            "Evidence"
        ],

        "18_Theories_of_Evolution": [
            "Lamarckism",
            "Darwinism",
            "Mutation_Theory",
            "Modern_Synthetic_Theory"
        ],

        "19_Natural_Selection": [
            "Natural_Selection",
            "Adaptation",
            "Survival_of_Fittest",
            "Speciation"
        ],

        "20_Evidences_of_Evolution": [
            "Fossils",
            "Embryology",
            "Comparative_Anatomy",
            "Molecular_Evidence"
        ],

        "21_Human_Evolution": [
            "Australopithecus",
            "Homo_Habilis",
            "Homo_Erectus",
            "Homo_Sapiens"
        ],

        "22_Evolutionary_Concepts": [
            "Adaptive_Radiation",
            "Convergent_Evolution",
            "Divergent_Evolution",
            "Coevolution"
        ],

        "23_Scientists_and_Discoveries": [
            "Mendel",
            "Darwin",
            "Watson_and_Crick",
            "Morgan"
        ],

        "24_Exam_Focused_Genetics_Evolution": [
            "NCERT_Facts",
            "Frequently_Asked",
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
        "numerical_based.json",
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

    print("\n✅ Genetics and Evolution structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_genetics_and_evolution_structure()