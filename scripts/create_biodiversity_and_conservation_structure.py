import os
import shutil

def create_biodiversity_and_conservation_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "biodiversity-and-conservation"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Biodiversity_Fundamentals": [
            "Meaning_of_Biodiversity",
            "Levels_of_Biodiversity",
            "Genetic_Diversity",
            "Species_Diversity",
            "Ecosystem_Diversity",
            "Biodiversity_Values",
            "Importance_of_Biodiversity",
            "Threats_to_Biodiversity"
        ],

        "02_Origin_and_Evolution_of_Biodiversity": [
            "Evolutionary_Processes",
            "Speciation",
            "Adaptive_Radiation",
            "Natural_Selection",
            "Co_Evolution",
            "Extinction_and_Survival",
            "Evolutionary_History",
            "Biodiversity_Patterns"
        ],

        "03_Biogeographic_Classification_of_India": [
            "Trans_Himalayan_Zone",
            "Himalayan_Zone",
            "Desert_Zone",
            "Semi_Arid_Zone",
            "Western_Ghats",
            "Deccan_Plateau",
            "Gangetic_Plain",
            "Coastal_and_Island_Zones"
        ],

        "04_Biodiversity_Hotspots": [
            "Concept_of_Hotspots",
            "Criteria_for_Hotspots",
            "Himalaya_Hotspot",
            "Western_Ghats_Hotspot",
            "Indo_Burma_Hotspot",
            "Sundaland_Hotspot",
            "Global_Hotspots",
            "Conservation_Importance"
        ],

        "05_Endemism_and_Endangered_Species": [
            "Endemic_Species",
            "Endangered_Species",
            "Critically_Endangered_Species",
            "Vulnerable_Species",
            "Rare_Species",
            "Threatened_Species",
            "Species_Recovery",
            "Conservation_Priorities"
        ],

        "06_IUCN_and_Red_List": [
            "IUCN_Organization",
            "Red_List_Categories",
            "Assessment_Criteria",
            "Species_Monitoring",
            "Conservation_Status",
            "Global_Conservation_Data",
            "Red_List_Updates",
            "India_and_IUCN"
        ],

        "07_Protected_Area_Network": [
            "Protected_Area_Concept",
            "National_Parks",
            "Wildlife_Sanctuaries",
            "Conservation_Reserves",
            "Community_Reserves",
            "Protected_Area_Management",
            "Buffer_Zones",
            "Conservation_Challenges"
        ],

        "08_National_Parks_of_India": [
            "National_Park_Concept",
            "Major_National_Parks",
            "Himalayan_National_Parks",
            "Desert_National_Parks",
            "Marine_National_Parks",
            "Biodiversity_Significance",
            "Conservation_Challenges",
            "Recent_Developments"
        ],

        "09_Wildlife_Sanctuaries_of_India": [
            "Wildlife_Sanctuary_Concept",
            "Major_Wildlife_Sanctuaries",
            "Habitat_Protection",
            "Species_Conservation",
            "Community_Participation",
            "Management_Practices",
            "Challenges",
            "Current_Affairs"
        ],

        "10_Biosphere_Reserves": [
            "UNESCO_MAB_Programme",
            "Core_Zone",
            "Buffer_Zone",
            "Transition_Zone",
            "Indian_Biosphere_Reserves",
            "World_Network",
            "Conservation_and_Development",
            "Recent_Additions"
        ],

        "11_Tiger_Conservation": [
            "Project_Tiger",
            "Tiger_Reserves",
            "Tiger_Corridors",
            "Tiger_Census",
            "NTCA",
            "Tiger_Conservation_Strategies",
            "Human_Wildlife_Conflict",
            "Recent_Developments"
        ],

        "12_Elephant_Conservation": [
            "Project_Elephant",
            "Elephant_Reserves",
            "Elephant_Corridors",
            "Elephant_Census",
            "Human_Elephant_Conflict",
            "Conservation_Strategies",
            "Migration_Routes",
            "Current_Affairs"
        ],

        "13_Species_Specific_Conservation_Programmes": [
            "Asiatic_Lion_Conservation",
            "Snow_Leopard_Programme",
            "Rhino_Conservation",
            "Hangul_Conservation",
            "Vulture_Recovery",
            "Great_Indian_Bustard",
            "Dolphin_Conservation",
            "Sea_Turtle_Conservation"
        ],

        "14_Ex_Situ_Conservation": [
            "Zoo_Conservation",
            "Botanical_Gardens",
            "Seed_Banks",
            "Gene_Banks",
            "Cryopreservation",
            "Captive_Breeding",
            "Species_Reintroduction",
            "Limitations"
        ],

        "15_In_Situ_Conservation": [
            "Habitat_Protection",
            "Protected_Areas",
            "Landscape_Conservation",
            "Species_Protection",
            "Community_Involvement",
            "Ecological_Restoration",
            "Advantages",
            "Challenges"
        ],

        "16_Human_Wildlife_Conflict": [
            "Causes_of_Conflict",
            "Human_Tiger_Conflict",
            "Human_Elephant_Conflict",
            "Crop_Raiding",
            "Livestock_Predation",
            "Mitigation_Measures",
            "Compensation_Mechanisms",
            "Case_Studies"
        ],

        "17_Invasive_Alien_Species": [
            "Meaning_of_Invasive_Species",
            "Pathways_of_Introduction",
            "Ecological_Impacts",
            "Economic_Impacts",
            "Lantana",
            "Water_Hyacinth",
            "Prosopis_Juliflora",
            "Management_Strategies"
        ],

        "18_Biodiversity_Conservation_Institutions": [
            "National_Biodiversity_Authority",
            "State_Biodiversity_Boards",
            "Biodiversity_Management_Committees",
            "Wildlife_Institute_of_India",
            "Botanical_Survey_of_India",
            "Zoological_Survey_of_India",
            "Forest_Survey_of_India",
            "Institutional_Framework"
        ],

        "19_Community_Based_Conservation": [
            "Sacred_Groves",
            "Community_Reserves",
            "Traditional_Conservation_Practices",
            "Joint_Forest_Management",
            "People_Participation",
            "Indigenous_Knowledge",
            "Success_Stories",
            "Challenges"
        ],

        "20_Current_Affairs_and_Biodiversity": [
            "New_Protected_Areas",
            "New_Ramsar_Sites",
            "Species_Discoveries",
            "Species_Extinction_Reports",
            "IUCN_Updates",
            "Wildlife_Census_Reports",
            "Government_Initiatives",
            "UPSC_High_Yield_Topics"
        ]

    }

    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "map_based.json", "source_based.json",
        "passage_based.json", "case_study.json", "short_answer.json",
        "long_answer.json", "mains_10m.json", "mains_15m.json",
        "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "pyq_teaching.json",
        "interview.json", "flashcards.json", "revision_questions.json",
        "concept_traps.json", "common_mistakes.json", "memory_hooks.json"
    ]

    print(f"Creating Biodiversity and Conservation structure in: {target_base}")

    for category, topics in structure.items():
        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        for topic in topics:
            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for filename in leaf_files:
                file_path = os.path.join(topic_path, filename)

                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("[]")

if __name__ == "__main__":
    create_biodiversity_and_conservation_structure()