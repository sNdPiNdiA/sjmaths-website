import os
import shutil

def create_prehistory_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "prehistory")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Fundamentals": [
            "Meaning_of_Prehistory", "Scope_of_Prehistory", "Sources_of_Prehistory",
            "Archaeology", "Dating_Methods", "Carbon_14_Dating", "Relative_Dating",
            "Absolute_Dating", "Importance_of_Prehistory"
        ],
        "02_Human_Evolution": [
            "Evolution_of_Humans", "Australopithecus", "Homo_Habilis", "Homo_Erectus",
            "Neanderthals", "Homo_Sapiens", "Migration_of_Humans", "Human_Adaptation",
            "Fossil_Evidence"
        ],
        "03_Stone_Age_Overview": [
            "Stone_Age", "Classification_of_Stone_Age", "Characteristics_of_Stone_Age",
            "Stone_Tool_Traditions"
        ],
        "04_Paleolithic_Period": [
            "Paleolithic_Overview", "Lower_Paleolithic", "Middle_Paleolithic",
            "Upper_Paleolithic", "Paleolithic_Tools", "Paleolithic_Economy",
            "Paleolithic_Society", "Paleolithic_Sites", "Paleolithic_Lifestyle"
        ],
        "05_Mesolithic_Period": [
            "Mesolithic_Overview", "Microliths", "Mesolithic_Tools", "Mesolithic_Economy",
            "Mesolithic_Society", "Domestication_Beginnings", "Mesolithic_Sites",
            "Mesolithic_Lifestyle"
        ],
        "06_Neolithic_Period": [
            "Neolithic_Overview", "Neolithic_Revolution", "Agriculture",
            "Animal_Husbandry", "Polished_Stone_Tools", "Pottery",
            "Permanent_Settlements", "Neolithic_Society", "Neolithic_Sites",
            "Neolithic_Lifestyle"
        ],
        "07_Chalcolithic_Period": [
            "Chalcolithic_Overview", "Copper_Usage", "Chalcolithic_Tools",
            "Chalcolithic_Pottery", "Chalcolithic_Settlements", "Chalcolithic_Economy",
            "Chalcolithic_Society", "Chalcolithic_Cultures", "Chalcolithic_Sites"
        ],
        "08_Prehistoric_Technology": [
            "Stone_Tools", "Tool_Manufacturing", "Blade_Technology",
            "Microlithic_Technology", "Bone_Tools", "Copper_Technology",
            "Pottery_Technology", "Technological_Development"
        ],
        "09_Prehistoric_Economy": [
            "Hunting", "Gathering", "Fishing", "Food_Production",
            "Agriculture_Evolution", "Animal_Domestication", "Trade_Beginnings",
            "Economic_Transition"
        ],
        "10_Prehistoric_Society": [
            "Family_Structure", "Clan_System", "Tribal_Organization", "Gender_Roles",
            "Social_Cooperation", "Settlement_Patterns", "Community_Life",
            "Social_Evolution"
        ],
        "11_Prehistoric_Religion_and_Beliefs": [
            "Animism", "Ancestor_Worship", "Burial_Practices", "Megalithic_Beliefs",
            "Ritual_Practices", "Totemism", "Fertility_Cults", "Religious_Evolution"
        ],
        "12_Rock_Art_and_Culture": [
            "Rock_Art", "Cave_Paintings", "Bhimbetka", "Artistic_Themes",
            "Symbolism", "Dance_and_Music", "Cultural_Expressions", "Artistic_Development"
        ],
        "13_Megalithic_Culture": [
            "Megalithic_Overview", "Menhirs", "Dolmens", "Cairns", "Cists",
            "Megalithic_Burials", "Megalithic_Sites", "Megalithic_Society"
        ],
        "14_Important_Prehistoric_Sites": [
            "Bhimbetka", "Hunsgi", "Kurnool_Caves", "Belan_Valley", "Burzahom",
            "Mehrgarh", "Chirand", "Hallur", "Inamgaon", "Paiyampalli"
        ],
        "15_Regional_Prehistory": [
            "North_India", "South_India", "East_India", "West_India",
            "Central_India", "Kashmir", "Deccan", "Regional_Variations"
        ],
        "16_Archaeological_Evidence": [
            "Stone_Tools_Evidence", "Fossils", "Pottery_Evidence", "Burial_Evidence",
            "Settlement_Evidence", "Rock_Art_Evidence", "Ecofacts", "Artefacts"
        ],
        "17_Comparative_Studies": [
            "Paleolithic_vs_Mesolithic", "Mesolithic_vs_Neolithic",
            "Neolithic_vs_Chalcolithic", "Food_Gathering_vs_Food_Production",
            "Stone_Age_vs_Metal_Age", "Technological_Comparisons"
        ],
        "18_Legacy_and_Significance": [
            "Agricultural_Revolution", "Rise_of_Settlements", "Technological_Legacy",
            "Cultural_Legacy", "Historical_Significance", "Contribution_to_Civilization"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "map_based.json", "image_based.json",
        "source_based.json", "case_study.json", "short_answer.json",
        "long_answer.json", "mains_10m.json", "mains_15m.json",
        "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "interview.json",
        "flashcards.json", "revision_questions.json", "concept_traps.json"
    ]

    print(f"Creating Prehistory structure in: {target_base}")
    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)
        print(f"  [+] Category: {category}")

        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)
            print(f"    [+] Topic: {topic}")

            for filename in leaf_files:
                file_path = os.path.join(topic_path, filename)
                if not os.path.exists(file_path):
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write("[]")
                    print(f"      - Created: {filename}")
                else:
                    print(f"      - Exists: {filename}")

if __name__ == "__main__":
    create_prehistory_structure()