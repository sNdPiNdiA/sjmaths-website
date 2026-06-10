import os
import shutil

def create_early_medieval_rajputs_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "medieval-india", "early-medieval-and-rajputs")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Transition_to_Early_Medieval_India": [
            "End_of_Gupta_Empire",
            "Post_Gupta_Political_Fragmentation",
            "Rise_of_Regional_Kingdoms",
            "Feudalism_Debate",
            "Land_Grant_System",
            "Agrarian_Expansion",
            "Urban_Decline_Debate",
            "Sources_for_Early_Medieval_India"
        ],
        "02_Rajput_Origins": [
            "Meaning_of_Rajput",
            "Agnikula_Theory",
            "Foreign_Origin_Theory",
            "Indigenous_Origin_Theory",
            "Mixed_Origin_Theory",
            "Rajput_Clan_System",
            "Rajput_Social_Structure",
            "Historiography_of_Rajput_Origins"
        ],
        "03_Political_Structure": [
            "Kingship",
            "Administration",
            "Feudatories_and_Samantas",
            "Revenue_System",
            "Military_Organization",
            "Justice_System",
            "Provincial_Administration",
            "Local_Government"
        ],
        "04_Gurjara_Pratiharas": [
            "Rise_of_Pratiharas",
            "Nagabhata_I",
            "Vatsaraja",
            "Nagabhata_II",
            "Mihira_Bhoja",
            "Mahendrapala_I",
            "Decline_of_Pratiharas",
            "Pratihara_Administration"
        ],
        "05_Palas": [
            "Rise_of_Palas",
            "Gopala",
            "Dharmapala",
            "Devapala",
            "Mahipala",
            "Pala_Administration",
            "Pala_Culture",
            "Decline_of_Palas"
        ],
        "06_Rashtrakutas": [
            "Rise_of_Rashtrakutas",
            "Dantidurga",
            "Krishna_I",
            "Dhruva",
            "Govinda_III",
            "Amoghavarsha_I",
            "Rashtrakuta_Administration",
            "Decline_of_Rashtrakutas"
        ],
        "07_Tripartite_Struggle": [
            "Background",
            "Kanauj_as_Prize",
            "Pratihara_Role",
            "Pala_Role",
            "Rashtrakuta_Role",
            "Major_Conflicts",
            "Political_Impact",
            "Historical_Significance"
        ],
        "08_Chahamanas_Chauhans": [
            "Origin_of_Chauhans",
            "Ajayaraja",
            "Arnoraja",
            "Vigraharaja_IV",
            "Prithviraja_III",
            "Chauhan_Administration",
            "Chauhan_Culture",
            "Decline_of_Chauhans"
        ],
        "09_Gahadavalas": [
            "Origin_of_Gahadavalas",
            "Chandradeva",
            "Govindachandra",
            "Vijayachandra",
            "Jayachandra",
            "Administration",
            "Culture_and_Patronage",
            "Decline"
        ],
        "10_Chandelas": [
            "Origin_of_Chandelas",
            "Yashovarman",
            "Dhanga",
            "Vidyadhara",
            "Khajuraho_Group",
            "Administration",
            "Art_and_Culture",
            "Decline"
        ],
        "11_Paramaras": [
            "Origin_of_Paramaras",
            "Siyaka_II",
            "Vakpati_Munja",
            "Bhoja",
            "Later_Paramaras",
            "Administration",
            "Literary_Patronage",
            "Decline"
        ],
        "12_Solankis_Chaulukyas": [
            "Origin_of_Solankis",
            "Mularaja",
            "Bhimadeva_I",
            "Siddharaja_Jayasimha",
            "Kumarapala",
            "Administration",
            "Temple_Patronage",
            "Decline"
        ],
        "13_Tomaras": [
            "Origin_of_Tomaras",
            "Anangapala_I",
            "Anangapala_II",
            "Delhi_Under_Tomaras",
            "Political_Role",
            "Administration",
            "Cultural_Contribution",
            "Decline"
        ],
        "14_Kalachuris": [
            "Origin_of_Kalachuris",
            "Kokalla_I",
            "Gangeyadeva",
            "Karna",
            "Territorial_Expansion",
            "Administration",
            "Culture",
            "Decline"
        ],
        "15_Kashmir_and_Northwest_Kingdoms": [
            "Karkota_Dynasty",
            "Lalitaditya_Muktapida",
            "Utpala_Dynasty",
            "Hindu_Shahis",
            "Jayapala",
            "Anandapala",
            "Regional_Politics",
            "Decline"
        ],
        "16_South_Indian_Powers": [
            "Imperial_Cholas",
            "Rajaraja_I",
            "Rajendra_I",
            "Later_Cholas",
            "Western_Chalukyas",
            "Hoysalas",
            "Yadavas_of_Devagiri",
            "Relations_with_Rajput_States"
        ],
        "17_Society": [
            "Caste_System",
            "Rajput_Clans",
            "Women_in_Society",
            "Marriage_Practices",
            "Education",
            "Social_Customs",
            "Rural_Society",
            "Urban_Society"
        ],
        "18_Economy": [
            "Agriculture",
            "Irrigation",
            "Land_Revenue",
            "Trade_and_Commerce",
            "Guilds",
            "Coinage",
            "Craft_Production",
            "Economic_Changes"
        ],
        "19_Religion": [
            "Shaivism",
            "Vaishnavism",
            "Shaktism",
            "Jainism",
            "Buddhism",
            "Temple_Worship",
            "Pilgrimage_Centres",
            "Religious_Tolerance"
        ],
        "20_Architecture": [
            "Nagara_Style",
            "Khajuraho_Temples",
            "Sun_Temple_Modhera",
            "Osian_Temples",
            "Dilwara_Temples",
            "Temple_Planning",
            "Temple_Sculpture",
            "Regional_Variations"
        ],
        "21_Art_and_Literature": [
            "Court_Literature",
            "Sanskrit_Literature",
            "Regional_Literature",
            "Kalhana",
            "Bilhana",
            "Hemachandra",
            "Raja_Bhoja_as_Scholar",
            "Artistic_Patronage"
        ],
        "22_Military_and_Warfare": [
            "Rajput_Warfare",
            "Fortifications",
            "Cavalry",
            "Infantry",
            "Elephant_Corps",
            "Weapons",
            "Battle_Tactics",
            "Military_Limitations"
        ],
        "23_Arab_Invasions": [
            "Arab_Expansion",
            "Muhammad_bin_Qasim",
            "Sindh_Campaign",
            "Resistance_to_Arabs",
            "Nagabhata_I_and_Arabs",
            "Political_Impact",
            "Economic_Impact",
            "Historical_Assessment"
        ],
        "24_Turkish_Invasions": [
            "Sabuktigin",
            "Mahmud_of_Ghazni",
            "Ghaznavid_Raids",
            "Muhammad_Ghori",
            "Battles_of_Tarain",
            "Rajput_Response",
            "Political_Consequences",
            "Transition_to_Delhi_Sultanate"
        ],
        "25_Important_Battles": [
            "Battle_of_Rajasthan_Against_Arabs",
            "Battle_of_Peshawar",
            "First_Battle_of_Tarain",
            "Second_Battle_of_Tarain",
            "Battle_of_Chandawar",
            "Regional_Conflicts",
            "Strategic_Analysis",
            "Historical_Impact"
        ],
        "26_Historiography": [
            "Colonial_View",
            "Nationalist_View",
            "Marxist_View",
            "Feudalism_Debate",
            "Romantic_View_of_Rajputs",
            "Modern_Research",
            "Source_Criticism",
            "Recent_Scholarship"
        ],
        "27_Legacy_and_Significance": [
            "Rajput_Identity",
            "Cultural_Legacy",
            "Political_Legacy",
            "Architectural_Legacy",
            "Military_Legacy",
            "Regional_Traditions",
            "Memory_and_Folklore",
            "Contemporary_Relevance"
        ]
    }

    # Standard dataset files for every leaf folder
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

    print(f"Creating Early Medieval and Rajputs structure in: {target_base}")
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
    create_early_medieval_rajputs_structure()