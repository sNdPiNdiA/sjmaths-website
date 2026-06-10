import os
import shutil

def create_indus_valley_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "ancient-india", "indus-valley")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Introduction_and_Discovery": [
            "Meaning_of_Indus_Civilization", "Discovery_of_Harappan_Civilization",
            "John_Marshall", "Dayaram_Sahni", "Rakhaldas_Banerji",
            "Sources_of_Information", "Chronology", "Geographical_Extent",
            "Importance_of_Discovery"
        ],
        "02_Origin_and_Development": [
            "Pre_Harappan_Cultures", "Early_Harappan_Phase", "Mature_Harappan_Phase",
            "Late_Harappan_Phase", "Urbanization_Process", "Regional_Variations",
            "Development_of_Civilization"
        ],
        "03_Geographical_Extent": [
            "Northern_Extent", "Southern_Extent", "Eastern_Extent", "Western_Extent",
            "River_Systems", "Ghaggar_Hakra", "Indus_System", "Distribution_of_Sites"
        ],
        "04_Major_Sites": [
            "Harappa", "Mohenjo_Daro", "Dholavira", "Lothal", "Kalibangan",
            "Rakhigarhi", "Banawali", "Chanhudaro", "Surkotada", "Ropar",
            "Alamgirpur", "Sutkagendor", "Kot_Diji", "Rangpur", "Desalpur"
        ],
        "05_Town_Planning": [
            "Urban_Planning", "Grid_Pattern", "Citadel", "Lower_Town",
            "Roads_and_Streets", "Drainage_System", "Houses", "Wells",
            "Public_Buildings", "Sanitation_System"
        ],
        "06_Architecture": [
            "Great_Bath", "Granaries", "Assembly_Hall", "Dockyard",
            "Fortifications", "Residential_Buildings", "Brick_Technology",
            "Architectural_Features"
        ],
        "07_Economy": [
            "Agriculture", "Crops", "Irrigation", "Animal_Husbandry",
            "Trade", "Internal_Trade", "Foreign_Trade", "Weights_and_Measures",
            "Standardization", "Economic_Organization"
        ],
        "08_Crafts_and_Industries": [
            "Bead_Making", "Pottery", "Metallurgy", "Shell_Industry",
            "Textile_Industry", "Seal_Making", "Jewelry", "Terracotta_Objects",
            "Craft_Specialization"
        ],
        "09_Social_Life": [
            "Social_Structure", "Family_System", "Position_of_Women", "Food_Habits",
            "Dress_and_Ornaments", "Recreation", "Toys_and_Games", "Daily_Life"
        ],
        "10_Religion_and_Beliefs": [
            "Mother_Goddess", "Pashupati_Seal", "Tree_Worship", "Animal_Worship",
            "Fire_Worship", "Fertility_Cults", "Burial_Practices", "Religious_Symbols",
            "Nature_of_Religion"
        ],
        "11_Art_and_Culture": [
            "Sculpture", "Dancing_Girl", "Priest_King", "Terracotta_Art",
            "Seals", "Seal_Iconography", "Pottery_Art", "Music_and_Dance",
            "Cultural_Achievements"
        ],
        "12_Script_and_Language": [
            "Harappan_Script", "Characteristics_of_Script", "Decipherment_Attempts",
            "Writing_System", "Seal_Inscriptions", "Language_Debate"
        ],
        "13_Science_and_Technology": [
            "Mathematics", "Geometry", "Measurement_System", "Metallurgical_Knowledge",
            "Engineering", "Water_Management", "Navigation", "Technological_Achievements"
        ],
        "14_Political_Organization": [
            "Nature_of_State", "Centralization_Debate", "Administration",
            "Governance_Model", "Authority_Structures", "Political_Theories"
        ],
        "15_Harappan_Trade_Networks": [
            "Mesopotamia_Trade", "Persian_Gulf_Trade", "Oman_Connections", "Dilmun",
            "Meluhha", "Trade_Routes", "Export_Items", "Import_Items"
        ],
        "16_Decline_of_Civilization": [
            "Climate_Change_Theory", "River_Shift_Theory", "Flood_Theory",
            "Ecological_Theory", "Aryan_Invasion_Theory", "Multi_Causal_Theory",
            "Post_Harappan_Cultures", "Legacy_of_Harappans"
        ],
        "17_Important_Archaeological_Findings": [
            "Great_Bath_Findings", "Dockyard_Findings", "Granary_Findings",
            "Fire_Altars", "Seals_and_Sealings", "Burials", "Skeletons", "Artefacts"
        ],
        "18_Comparative_Studies": [
            "Harappa_vs_Mesopotamia", "Harappa_vs_Egypt", "Harappa_vs_Vedic_Culture",
            "Harappa_vs_Mauryan_Urbanization", "Site_Comparisons", "Urbanization_Comparisons"
        ],
        "19_Historiography": [
            "Archaeological_Interpretations", "Debates_on_Origin", "Debates_on_Script",
            "Debates_on_Religion", "Debates_on_Politics", "Modern_Research"
        ],
        "20_Legacy_and_Significance": [
            "Urban_Legacy", "Cultural_Legacy", "Technological_Legacy",
            "Historical_Significance", "Contribution_to_Indian_History",
            "World_Civilization_Context"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "map_based.json", "image_based.json",
        "artifact_based.json", "source_based.json", "case_study.json",
        "short_answer.json", "long_answer.json", "mains_10m.json",
        "mains_15m.json", "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "interview.json",
        "flashcards.json", "revision_questions.json", "concept_traps.json"
    ]

    print(f"Creating Indus Valley Civilization structure in: {target_base}")
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
    create_indus_valley_structure()