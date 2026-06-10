import os
import shutil

def create_classification_of_organisms_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "general-science",
        "biology",
        "classification-of-organisms"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Taxonomy_and_Systematics": [
            "Taxonomy",
            "Systematics",
            "Nomenclature",
            "Taxonomic_Hierarchy"
        ],

        "02_History_of_Classification": [
            "Aristotle",
            "Linnaeus",
            "Whittaker",
            "Modern_Classification"
        ],

        "03_Two_and_Three_Kingdom_Systems": [
            "Two_Kingdom_System",
            "Three_Kingdom_System",
            "Limitations",
            "Important_Facts"
        ],

        "04_Five_Kingdom_Classification": [
            "Kingdom_Monera",
            "Kingdom_Protista",
            "Kingdom_Fungi",
            "Kingdom_Plantae"
        ],

        "05_Five_Kingdom_Classification_II": [
            "Kingdom_Animalia",
            "Whittaker_Criteria",
            "Kingdom_Comparison",
            "Frequently_Asked"
        ],

        "06_Six_Kingdom_Classification": [
            "Archaebacteria",
            "Eubacteria",
            "Protists",
            "Overview"
        ],

        "07_Three_Domain_System": [
            "Domain_Archaea",
            "Domain_Bacteria",
            "Domain_Eukarya",
            "Carl_Woese"
        ],

        "08_Monera": [
            "Bacteria",
            "Cyanobacteria",
            "Mycoplasma",
            "Economic_Importance"
        ],

        "09_Protista": [
            "Protozoa",
            "Diatoms",
            "Dinoflagellates",
            "Euglenoids"
        ],

        "10_Fungi": [
            "Yeast",
            "Moulds",
            "Mushrooms",
            "Importance_of_Fungi"
        ],

        "11_Plantae_Classification": [
            "Algae",
            "Bryophytes",
            "Pteridophytes",
            "Gymnosperms"
        ],

        "12_Plantae_Classification_II": [
            "Angiosperms",
            "Monocots",
            "Dicots",
            "Plant_Groups_Comparison"
        ],

        "13_Animalia_Invertebrates": [
            "Porifera",
            "Cnidaria",
            "Platyhelminthes",
            "Nematoda"
        ],

        "14_Animalia_Invertebrates_II": [
            "Annelida",
            "Arthropoda",
            "Mollusca",
            "Echinodermata"
        ],

        "15_Animalia_Chordates": [
            "Pisces",
            "Amphibia",
            "Reptilia",
            "Aves"
        ],

        "16_Animalia_Chordates_II": [
            "Mammalia",
            "Chordate_Characteristics",
            "Vertebrate_Comparison",
            "Examples"
        ],

        "17_Taxonomic_Categories": [
            "Species",
            "Genus",
            "Family",
            "Order"
        ],

        "18_Taxonomic_Categories_II": [
            "Class",
            "Phylum",
            "Kingdom",
            "Domain"
        ],

        "19_Binomial_Nomenclature": [
            "Scientific_Names",
            "Naming_Rules",
            "ICZN",
            "ICBN"
        ],

        "20_Biological_Diversity": [
            "Biodiversity_Concept",
            "Species_Diversity",
            "Genetic_Diversity",
            "Ecosystem_Diversity"
        ],

        "21_Microorganisms": [
            "Bacteria_Overview",
            "Viruses",
            "Viroids",
            "Prions"
        ],

        "22_Viruses_and_Subviral_Particles": [
            "Virus_Structure",
            "Virus_Classification",
            "Viroids",
            "Prions"
        ],

        "23_Important_Examples_for_Exams": [
            "Scientific_Names",
            "Common_Examples",
            "Important_Species",
            "Frequently_Asked"
        ],

        "24_Exam_Focused_Classification": [
            "NCERT_Facts",
            "One_Liner_Revision",
            "High_Yield_Topics",
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
        "classification_based.json",
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

    print("\n✅ Classification of Organisms structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_classification_of_organisms_structure()