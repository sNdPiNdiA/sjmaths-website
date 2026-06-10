import os
import shutil

def create_delhi_sultanate_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "medieval-india", "delhi-sultanate")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_and_Establishment": [
            "Decline_of_Rajput_Powers",
            "Turkish_Invasions",
            "Muhammad_Ghori",
            "Ghurid_Administration_in_India",
            "Conquest_of_North_India",
            "Foundation_of_Delhi_Sultanate",
            "Political_Conditions",
            "Sources_of_Study"
        ],
        "02_Slave_Dynasty_Foundation": [
            "Qutb_ud_din_Aibak",
            "Aram_Shah",
            "Establishment_of_Rule",
            "Early_Administration",
            "Territorial_Expansion",
            "Military_Organization",
            "Challenges_of_New_State",
            "Legacy_of_Aibak"
        ],
        "03_Iltutmish": [
            "Accession",
            "Consolidation_of_Empire",
            "Iqta_System",
            "Recognition_by_Caliph",
            "Military_Campaigns",
            "Administrative_Reforms",
            "Silver_Tanka_and_Jital",
            "Historical_Assessment"
        ],
        "04_Razia_and_Later_Slaves": [
            "Razia_Sultan",
            "Turkan_i_Chahalgani",
            "Bahram_Shah",
            "Masud_Shah",
            "Nasiruddin_Mahmud",
            "Balban_as_Naib",
            "Political_Instability",
            "End_of_Slave_Dynasty"
        ],
        "05_Balban": [
            "Theory_of_Kingship",
            "Blood_and_Iron_Policy",
            "Destruction_of_Chahalgani",
            "Military_Reforms",
            "Spy_System",
            "Frontier_Policy",
            "Court_Ceremonies",
            "Historical_Assessment"
        ],
        "06_Khalji_Revolution": [
            "Rise_of_Khaljis",
            "Jalalluddin_Khalji",
            "Nature_of_Revolution",
            "Political_Changes",
            "Nobility_and_Power",
            "Expansion_Policies",
            "Administrative_Changes",
            "Historical_Debates"
        ],
        "07_Alauddin_Khalji": [
            "Accession",
            "Market_Control_System",
            "Revenue_Reforms",
            "Military_Reforms",
            "Mongol_Policy",
            "Deccan_Campaigns",
            "Theory_of_Kingship",
            "Historical_Assessment"
        ],
        "08_Later_Khaljis": [
            "Malik_Kafur",
            "Qutbuddin_Mubarak_Shah",
            "Khusrau_Khan",
            "Succession_Crisis",
            "Political_Decline",
            "Administrative_Weaknesses",
            "Factional_Struggles",
            "End_of_Khalji_Dynasty"
        ],
        "09_Tughlaq_Foundation": [
            "Ghiyasuddin_Tughlaq",
            "Rise_of_Tughlaqs",
            "Military_Campaigns",
            "Administration",
            "Frontier_Policy",
            "Public_Works",
            "Political_Consolidation",
            "Legacy"
        ],
        "10_Muhammad_bin_Tughlaq": [
            "Transfer_of_Capital",
            "Token_Currency",
            "Doab_Taxation",
            "Khurasan_Project",
            "Qarachil_Expedition",
            "Administrative_Experiments",
            "Rebellions",
            "Historical_Assessment"
        ],
        "11_Firoz_Shah_Tughlaq": [
            "Administrative_Reforms",
            "Public_Works",
            "Canals_and_Irrigation",
            "Revenue_Policy",
            "Religious_Policy",
            "Slavery_Department",
            "Literary_Patronage",
            "Historical_Assessment"
        ],
        "12_Later_Tughlaqs_and_Timur": [
            "Succession_Problems",
            "Provincial_Revolts",
            "Weak_Rulers",
            "Decline_of_Central_Authority",
            "Timur_Invasion",
            "Impact_of_Timur",
            "Political_Fragmentation",
            "End_of_Tughlaqs"
        ],
        "13_Sayyid_Dynasty": [
            "Khizr_Khan",
            "Mubarak_Shah",
            "Muhammad_Shah",
            "Alauddin_Alam_Shah",
            "Administration",
            "Political_Weakness",
            "Regional_States",
            "Decline"
        ],
        "14_Lodi_Dynasty": [
            "Bahlul_Lodi",
            "Sikandar_Lodi",
            "Ibrahim_Lodi",
            "Afghan_Theory_of_Kingship",
            "Administrative_System",
            "Territorial_Expansion",
            "Internal_Conflicts",
            "Decline"
        ],
        "15_First_Battle_of_Panipat": [
            "Background",
            "Babur_and_Lodis",
            "Military_Technology",
            "Battle_Strategy",
            "Defeat_of_Ibrahim_Lodi",
            "Immediate_Consequences",
            "Political_Impact",
            "Historical_Significance"
        ],
        "16_Central_Administration": [
            "Sultan", "Wazir", "Diwan_i_Wizarat", "Diwan_i_Arz",
            "Diwan_i_Insha", "Diwan_i_Risalat", "Royal_Household",
            "Administrative_Hierarchy"
        ],
        "17_Provincial_Administration": [
            "Iqta_System", "Muqtis", "Provincial_Government",
            "District_Administration", "Village_Administration",
            "Revenue_Collection", "Law_and_Order", "Administrative_Challenges"
        ],
        "18_Revenue_and_Economy": [
            "Land_Revenue", "Kharaj_and_Other_Taxes", "Agriculture",
            "Irrigation", "Trade_and_Commerce", "Craft_Production",
            "Coinage", "Economic_Conditions"
        ],
        "19_Military_System": [
            "Army_Organization", "Cavalry", "Infantry", "Elephant_Forces",
            "Dagh_System", "Chehra_System", "Frontier_Defence", "Military_Efficiency"
        ],
        "20_Society": [
            "Social_Structure", "Nobility", "Ulema", "Peasants",
            "Merchants", "Women", "Slavery", "Daily_Life"
        ],
        "21_Religion_and_State": [
            "Islamic_Political_Theory", "Ulema_and_State", "Sufism",
            "Hindu_Muslim_Relations", "Religious_Taxes", "Jizya",
            "Religious_Policies", "Social_Impact"
        ],
        "22_Bhakti_and_Sufi_Influence": [
            "Spread_of_Bhakti", "Spread_of_Sufism", "Chishti_Order",
            "Suhrawardi_Order", "Nizamuddin_Auliya", "Religious_Synthesis",
            "Social_Impact", "Cultural_Influence"
        ],
        "23_Architecture": [
            "Indo_Islamic_Architecture", "Qutub_Minar", "Quwwat_ul_Islam_Mosque",
            "Alai_Darwaza", "Tughlaq_Architecture", "Lodi_Architecture",
            "Tombs_and_Mausoleums", "Architectural_Features"
        ],
        "24_Literature_and_Education": [
            "Persian_Literature", "Arabic_Learning", "Madrasas",
            "Court_Historians", "Amir_Khusrau", "Ziauddin_Barani",
            "Historical_Writings", "Educational_Institutions"
        ],
        "25_Art_and_Culture": [
            "Music", "Dance", "Painting", "Court_Culture", "Festivals",
            "Language_Development", "Cultural_Synthesis", "Patronage"
        ],
        "26_Mongol_Invasions": [
            "Background", "Major_Mongol_Attacks", "Balban_and_Mongols",
            "Alauddin_and_Mongols", "Defensive_Measures", "Military_Impact",
            "Economic_Impact", "Historical_Assessment"
        ],
        "27_Regional_Kingdoms_and_Revolts": [
            "Bengal", "Jaunpur", "Gujarat", "Malwa", "Deccan_Revolts",
            "Provincial_Autonomy", "Causes_of_Separatism", "Political_Consequences"
        ],
        "28_Sources_and_Historiography": [
            "Persian_Chronicles", "Foreign_Travellers", "Inscriptions",
            "Numismatic_Evidence", "Archaeological_Sources", "Colonial_Historiography",
            "Modern_Interpretations", "Source_Criticism"
        ],
        "29_Legacy_and_Significance": [
            "Administrative_Legacy", "Military_Legacy", "Economic_Legacy",
            "Architectural_Legacy", "Cultural_Legacy", "Religious_Legacy",
            "Transition_to_Mughal_Period", "Contemporary_Relevance"
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

    print(f"Creating Delhi Sultanate structure in: {target_base}")
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
    create_delhi_sultanate_structure()