import os
import shutil

def create_vijayanagara_bahmani_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "medieval-india", "vijayanagara-and-bahmani")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Historical_Background": [
            "Decline_of_Delhi_Sultanate_in_South", "Political_Conditions_in_Deccan",
            "Rise_of_Regional_Powers", "Impact_of_Tughlaq_Policies",
            "Religious_and_Cultural_Context", "Economic_Background",
            "Sources_of_Study", "Historiography"
        ],
        "02_Foundation_of_Vijayanagara": [
            "Harihara_I", "Bukka_I", "Role_of_Vidyaranya", "Foundation_of_Empire",
            "Early_Expansion", "Capital_City_Hampi", "Sangama_Dynasty",
            "Historical_Significance"
        ],
        "03_Early_Vijayanagara_Rulers": [
            "Harihara_II", "Devaraya_I", "Devaraya_II", "Military_Reforms",
            "Territorial_Expansion", "Foreign_Relations", "Administrative_Developments",
            "Dynastic_Continuity"
        ],
        "04_Tuluva_Dynasty": [
            "Rise_of_Tuluvas", "Narasa_Nayaka", "Vira_Narasimha", "Krishnadevaraya",
            "Achyuta_Deva_Raya", "Administrative_Changes", "Military_Successes",
            "Legacy_of_Tuluvas"
        ],
        "05_Krishnadevaraya": [
            "Military_Campaigns", "Relations_with_Deccan_Sultanates", "Amuktamalyada",
            "Patronage_of_Literature", "Administrative_Policies", "Economic_Prosperity",
            "Foreign_Accounts", "Historical_Assessment"
        ],
        "06_Later_Vijayanagara": [
            "Aravidu_Dynasty", "Aliya_Rama_Raya", "Political_Challenges",
            "Succession_Issues", "Relations_with_Sultanates", "Decline_of_Central_Authority",
            "Post_Talikota_Developments", "Final_Phase"
        ],
        "07_Vijayanagara_Administration": [
            "Kingship", "Central_Administration", "Provincial_Administration",
            "Nayankara_System", "Revenue_Administration", "Judicial_System",
            "Military_Administration", "Local_Government"
        ],
        "08_Vijayanagara_Economy": [
            "Agriculture", "Irrigation", "Land_Revenue", "Trade_and_Commerce",
            "Ports_and_Maritime_Trade", "Guilds_and_Crafts", "Coinage",
            "Economic_Prosperity"
        ],
        "09_Vijayanagara_Society": [
            "Social_Structure", "Role_of_Women", "Caste_System", "Urban_Life",
            "Rural_Life", "Education", "Festivals", "Daily_Life"
        ],
        "10_Vijayanagara_Art_and_Architecture": [
            "Hampi_Monuments", "Virupaksha_Temple", "Vittala_Temple", "Royal_Centre",
            "Temple_Architecture", "Sculpture", "Urban_Planning", "Architectural_Legacy"
        ],
        "11_Vijayanagara_Literature_and_Culture": [
            "Telugu_Literature", "Kannada_Literature", "Sanskrit_Literature",
            "Ashtadiggajas", "Court_Culture", "Music_and_Dance", "Religious_Patronage",
            "Cultural_Achievements"
        ],
        "12_Foreign_Travellers_to_Vijayanagara": [
            "Nicolo_Conti", "Abdur_Razzaq", "Domingo_Paes", "Fernao_Nuniz",
            "Duarte_Barbosa", "Accounts_of_Hampi", "Economic_Observations",
            "Historical_Value_of_Accounts"
        ],
        "13_Foundation_of_Bahmani_Sultanate": [
            "Hasan_Gangu_Bahman_Shah", "Foundation_of_Kingdom", "Breakaway_from_Delhi",
            "Capital_Gulbarga", "Territorial_Expansion", "Administrative_Setup",
            "Political_Context", "Historical_Significance"
        ],
        "14_Early_Bahmani_Rulers": [
            "Muhammad_Shah_I", "Mujahid_Shah", "Firuz_Shah_Bahmani", "Ahmad_Shah_I",
            "Military_Expansion", "Political_Developments", "Relations_with_Vijayanagara",
            "Administrative_Changes"
        ],
        "15_Mahmud_Gawan": [
            "Early_Life", "Rise_to_Power", "Administrative_Reforms", "Military_Reforms",
            "Revenue_Reforms", "Madrasa_of_Bidar", "Execution", "Historical_Assessment"
        ],
        "16_Bahmani_Administration": [
            "Kingship", "Central_Government", "Taraf_System", "Revenue_System",
            "Military_Organization", "Judicial_Administration", "Provincial_Government",
            "Administrative_Challenges"
        ],
        "17_Bahmani_Economy": [
            "Agriculture", "Irrigation", "Trade_and_Commerce", "Ports_and_Trade_Routes",
            "Craft_Production", "Coinage", "Revenue_Resources", "Economic_Life"
        ],
        "18_Bahmani_Society_and_Culture": [
            "Social_Composition", "Afaqis_and_Deccanis", "Role_of_Women", "Education",
            "Persian_Influence", "Court_Culture", "Religious_Life", "Cultural_Synthesis"
        ],
        "19_Bahmani_Architecture": [
            "Gulbarga_Fort", "Bidar_Fort", "Gulbarga_Mosque", "Mahmud_Gawan_Madrasa",
            "Tombs_and_Mausoleums", "Architectural_Features", "Persian_Influence",
            "Architectural_Legacy"
        ],
        "20_Bahmani_Literature_and_Learning": [
            "Persian_Literature", "Arabic_Learning", "Educational_Institutions",
            "Court_Historians", "Religious_Scholarship", "Translation_Activities",
            "Intellectual_Life", "Literary_Patronage"
        ],
        "21_Vijayanagara_Bahmani_Relations": [
            "Raichur_Doab_Dispute", "Military_Conflicts", "Diplomatic_Relations",
            "Economic_Rivalry", "Border_Regions", "Strategic_Importance",
            "Balance_of_Power", "Historical_Impact"
        ],
        "22_Military_System_and_Warfare": [
            "Army_Organization", "Cavalry", "Infantry", "Elephant_Forces",
            "Artillery", "Fortifications", "Battle_Strategies", "Military_Technology"
        ],
        "23_Battle_of_Talikota": [
            "Background", "Formation_of_Alliance", "Course_of_Battle", "Role_of_Rama_Raya",
            "Defeat_of_Vijayanagara", "Immediate_Consequences", "Long_Term_Impact",
            "Historical_Debates"
        ],
        "24_Decline_of_Bahmani_Sultanate": [
            "Factional_Struggles", "Afaqi_Deccani_Conflict", "Weak_Rulers",
            "Provincial_Rebellions", "Administrative_Decay", "Political_Fragmentation",
            "Rise_of_Successor_States", "End_of_Bahmani_Rule"
        ],
        "25_Deccan_Sultanates": [
            "Ahmadnagar", "Bijapur", "Golconda", "Bidar", "Berar", "Political_Relations",
            "Cultural_Contributions", "Historical_Significance"
        ],
        "26_Religion_and_Society": [
            "Hindu_Religious_Institutions", "Islamic_Institutions", "Bhakti_Influence",
            "Sufi_Influence", "Religious_Tolerance", "Temple_Patronage",
            "Mosque_Patronage", "Social_Harmony_and_Conflict"
        ],
        "27_Sources_and_Historiography": [
            "Epigraphic_Sources", "Archaeological_Evidence", "Literary_Sources",
            "Persian_Chronicles", "Traveller_Accounts", "Colonial_Interpretations",
            "Modern_Historiography", "Source_Criticism"
        ],
        "28_Legacy_and_Significance": [
            "Political_Legacy", "Administrative_Legacy", "Architectural_Legacy",
            "Economic_Legacy", "Cultural_Legacy", "Religious_Legacy",
            "Influence_on_South_India", "Contemporary_Relevance"
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

    print(f"Creating Vijayanagara and Bahmani structure in: {target_base}")
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
    create_vijayanagara_bahmani_structure()