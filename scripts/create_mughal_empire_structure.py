import os
import shutil

def create_mughal_empire_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "medieval-india", "mughal-empire")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_and_Foundation": [
            "Timurid_Legacy",
            "Babur_in_Central_Asia",
            "Political_Condition_of_India",
            "Lodi_Dynasty",
            "Babur_Invasions",
            "Gunpowder_Technology",
            "Sources_of_Study",
            "Foundation_of_Mughal_Empire"
        ],
        "02_Babur": [
            "First_Battle_of_Panipat",
            "Battle_of_Khanwa",
            "Battle_of_Chanderi",
            "Battle_of_Ghaghra",
            "Military_Innovations",
            "Baburnama",
            "Administration",
            "Historical_Assessment"
        ],
        "03_Humayun": [
            "Early_Reign",
            "Conflict_with_Afghans",
            "Sher_Shah_Challenge",
            "Exile_in_Persia",
            "Restoration_of_Empire",
            "Administrative_Policies",
            "Cultural_Influence",
            "Legacy"
        ],
        "04_Sur_Interregnum": [
            "Sher_Shah_Suri",
            "Islam_Shah",
            "Administrative_Reforms",
            "Revenue_System",
            "Roads_and_Communication",
            "Currency_Reforms",
            "Military_System",
            "Impact_on_Mughals"
        ],
        "05_Akbar_Expansion": [
            "Second_Battle_of_Panipat",
            "Conquest_of_Malwa",
            "Conquest_of_Gujarat",
            "Rajput_Policy",
            "Conquest_of_Bengal",
            "North_West_Frontier",
            "Deccan_Policy",
            "Territorial_Expansion"
        ],
        "06_Akbar_Administration": [
            "Central_Administration",
            "Provincial_Administration",
            "Suba_System",
            "Mansabdari_System",
            "Jagirdari_System",
            "Revenue_Administration",
            "Military_Administration",
            "Administrative_Innovations"
        ],
        "07_Akbar_Religion_and_Policy": [
            "Sulh_i_Kul",
            "Ibadat_Khana",
            "Din_i_Ilahi",
            "Religious_Debates",
            "Policy_Towards_Hindus",
            "Jizya_Abolition",
            "Relations_with_Ulema",
            "Historical_Assessment"
        ],
        "08_Akbar_Culture_and_Court": [
            "Navratnas",
            "Abul_Fazl",
            "Faizi",
            "Birbal",
            "Todar_Mal",
            "Court_Culture",
            "Translation_Project",
            "Literary_Patronage"
        ],
        "09_Jahangir": [
            "Accession",
            "Nur_Jahan",
            "Chain_of_Justice",
            "Mewar_Policy",
            "Kangra_Campaign",
            "Relations_with_British",
            "Memoirs_Tuzuk_i_Jahangiri",
            "Historical_Assessment"
        ],
        "10_Shah_Jahan": [
            "Succession",
            "Military_Campaigns",
            "Centralization_of_Power",
            "Relations_with_Deccan",
            "Kandahar_Policy",
            "Court_Culture",
            "Economic_Conditions",
            "Historical_Assessment"
        ],
        "11_Aurangzeb": [
            "War_of_Succession",
            "Deccan_Campaigns",
            "Religious_Policy",
            "Maratha_Conflict",
            "North_West_Frontier",
            "Administrative_Challenges",
            "Expansion_of_Empire",
            "Historical_Assessment"
        ],
        "12_Later_Mughals": [
            "Bahadur_Shah_I",
            "Jahandar_Shah",
            "Farrukhsiyar",
            "Muhammad_Shah",
            "Ahmad_Shah",
            "Shah_Alam_II",
            "Weakening_of_Empire",
            "Political_Fragmentation"
        ],
        "13_Central_Administration": [
            "Padshah",
            "Wakil",
            "Wazir",
            "Diwan",
            "Mir_Bakshi",
            "Sadr_us_Sudur",
            "Royal_Household",
            "Administrative_Hierarchy"
        ],
        "14_Provincial_Administration": [
            "Suba",
            "Sarkar",
            "Pargana",
            "Village_Administration",
            "Subahdar",
            "Provincial_Revenue",
            "Law_and_Order",
            "Local_Government"
        ],
        "15_Mansabdari_and_Jagirdari": [
            "Mansab_Ranks",
            "Zat_and_Sawar",
            "Jagir_Assignment",
            "Jagirdari_Crisis",
            "Military_Obligations",
            "Salary_System",
            "Administrative_Functions",
            "Historical_Debates"
        ],
        "16_Revenue_and_Economy": [
            "Todar_Mal_System",
            "Zabt_System",
            "Land_Revenue",
            "Agriculture",
            "Trade_and_Commerce",
            "Coinage",
            "Craft_Production",
            "Economic_Structure"
        ],
        "17_Military_System": [
            "Army_Organization",
            "Cavalry",
            "Infantry",
            "Artillery",
            "Navy",
            "Fortifications",
            "Military_Technology",
            "Military_Limitations"
        ],
        "18_Society": [
            "Social_Hierarchy",
            "Nobility",
            "Zamindars",
            "Peasants",
            "Merchants",
            "Women",
            "Urban_Life",
            "Rural_Life"
        ],
        "19_Religion_and_Philosophy": [
            "Islam_in_Mughal_India",
            "Sufism",
            "Bhakti_Movement",
            "Religious_Sects",
            "Interfaith_Relations",
            "Orthodoxy_and_Liberalism",
            "Religious_Institutions",
            "Social_Impact"
        ],
        "20_Mughal_Architecture": [
            "Humayuns_Tomb",
            "Fatehpur_Sikri",
            "Agra_Fort",
            "Red_Fort",
            "Taj_Mahal",
            "Jama_Masjid",
            "Architectural_Features",
            "Architectural_Legacy"
        ],
        "21_Mughal_Painting": [
            "Origins_of_Mughal_Painting",
            "Akbar_School",
            "Jahangir_School",
            "Portraiture",
            "Naturalistic_Art",
            "Important_Artists",
            "Manuscript_Illustration",
            "Legacy"
        ],
        "22_Literature_and_Education": [
            "Persian_Literature",
            "Court_Histories",
            "Akbarnama",
            "Ain_i_Akbari",
            "Baburnama",
            "Educational_Institutions",
            "Translation_Movement",
            "Intellectual_Life"
        ],
        "23_Music_and_Culture": [
            "Court_Music",
            "Tansen",
            "Dance",
            "Festivals",
            "Language_Development",
            "Cultural_Synthesis",
            "Court_Ceremonies",
            "Patronage_of_Arts"
        ],
        "24_Foreign_Relations_and_Travellers": [
            "Portuguese",
            "British_East_India_Company",
            "Dutch",
            "French",
            "Bernier",
            "Tavernier",
            "Manucci",
            "Traveller_Accounts"
        ],
        "25_Regional_Powers_and_Challenges": [
            "Rajputs",
            "Sikhs",
            "Jats",
            "Satnamis",
            "Marathas",
            "Afghan_Challenges",
            "Regional_Rebellions",
            "Political_Consequences"
        ],
        "26_Invasions_and_Crisis": [
            "Nadir_Shah_Invasion",
            "Ahmad_Shah_Abdali",
            "Economic_Crisis",
            "Military_Weakness",
            "Administrative_Decay",
            "Court_Factionalism",
            "Loss_of_Authority",
            "Imperial_Crisis"
        ],
        "27_Decline_of_Mughal_Empire": [
            "Causes_of_Decline",
            "Jagirdari_Crisis",
            "Succession_Disputes",
            "Regionalization",
            "Foreign_Invasions",
            "Economic_Factors",
            "Administrative_Factors",
            "Historical_Debates"
        ],
        "28_Sources_and_Historiography": [
            "Persian_Chronicles",
            "Autobiographies",
            "European_Accounts",
            "Inscriptions",
            "Numismatic_Evidence",
            "Colonial_Historiography",
            "Nationalist_View",
            "Modern_Interpretations"
        ],
        "29_Legacy_and_Significance": [
            "Administrative_Legacy",
            "Architectural_Legacy",
            "Economic_Legacy",
            "Cultural_Legacy",
            "Religious_Legacy",
            "Political_Legacy",
            "Impact_on_Modern_India",
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

    print(f"Creating Mughal Empire structure in: {target_base}")
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
    create_mughal_empire_structure()