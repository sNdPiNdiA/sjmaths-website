import os
import shutil

def create_advent_of_europeans_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "advent-of-europeans")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_of_European_Expansion": [
            "Age_of_Discovery",
            "Renaissance_and_Exploration",
            "Search_for_Sea_Route_to_India",
            "Fall_of_Constantinople",
            "Mercantilism",
            "Spice_Trade",
            "Navigation_Technology",
            "Political_Conditions_in_India"
        ],

        "02_Portuguese_Arrival": [
            "Vasco_da_Gama",
            "Calicut_Landing",
            "Zamorin_of_Calicut",
            "Early_Trade_Relations",
            "Portuguese_Objectives",
            "Initial_Challenges",
            "Commercial_Activities",
            "Historical_Significance"
        ],

        "03_Portuguese_Empire_in_India": [
            "Francisco_de_Almeida",
            "Blue_Water_Policy",
            "Afonso_de_Albuquerque",
            "Capture_of_Goa",
            "Portuguese_Administration",
            "Estado_da_India",
            "Expansion_of_Trade_Network",
            "Portuguese_Strengths"
        ],

        "04_Portuguese_Decline": [
            "Religious_Intolerance",
            "Goa_Inquisition",
            "Corruption",
            "Competition_from_Other_Europeans",
            "Limited_Resources",
            "Naval_Weakness",
            "Loss_of_Monopoly",
            "Causes_of_Decline"
        ],

        "05_Dutch_Arrival_and_Expansion": [
            "Dutch_East_India_Company",
            "Arrival_in_India",
            "Dutch_Trading_Centres",
            "Commercial_Objectives",
            "Trade_in_Spices",
            "Relations_with_Indian_Rulers",
            "Maritime_Activities",
            "Dutch_Influence"
        ],

        "06_Dutch_Decline": [
            "Focus_on_Indonesia",
            "Anglo_Dutch_Competition",
            "Commercial_Limitations",
            "Military_Weakness",
            "Loss_of_Trading_Posts",
            "European_Rivalries",
            "Decline_in_India",
            "Historical_Assessment"
        ],

        "07_English_East_India_Company_Foundation": [
            "Charter_of_1600",
            "Formation_of_Company",
            "Early_Voyages",
            "Captain_Hawkins",
            "William_Hawkins_Mission",
            "Commercial_Objectives",
            "First_Trading_Contacts",
            "Historical_Background"
        ],

        "08_English_Factories_and_Trade": [
            "Surat_Factory",
            "Masulipatnam",
            "Madras",
            "Bombay",
            "Calcutta",
            "Trade_Commodities",
            "Factory_System",
            "Growth_of_English_Trade"
        ],

        "09_English_Relations_with_Mughals": [
            "Jahangir_and_English",
            "Sir_Thomas_Roe",
            "Farmans_and_Privileges",
            "Trade_Concessions",
            "Relations_with_Mughal_Officials",
            "Commercial_Expansion",
            "Political_Neutrality",
            "Historical_Impact"
        ],

        "10_French_East_India_Company": [
            "Foundation_of_French_Company",
            "French_Arrival",
            "Pondicherry",
            "Chandernagore",
            "French_Trading_Centres",
            "Commercial_Objectives",
            "French_Strategy",
            "Growth_of_French_Influence"
        ],

        "11_French_Leadership": [
            "Francois_Martin",
            "Dumas",
            "Dupleix",
            "French_Administrative_Policies",
            "Diplomatic_Approach",
            "Military_Innovations",
            "Expansion_of_Influence",
            "Historical_Assessment"
        ],

        "12_Danish_and_Other_Europeans": [
            "Danish_East_India_Company",
            "Tranquebar",
            "Serampore",
            "Austrian_Company",
            "Swedish_Company",
            "Minor_European_Powers",
            "Commercial_Activities",
            "Historical_Significance"
        ],

        "13_European_Trading_Centres": [
            "Goa",
            "Surat",
            "Madras",
            "Bombay",
            "Calcutta",
            "Pondicherry",
            "Chandernagore",
            "Masulipatnam"
        ],

        "14_Trade_and_Commerce": [
            "Spice_Trade",
            "Textile_Trade",
            "Indigo_Trade",
            "Saltpetre_Trade",
            "Bullion_Flow",
            "Export_Items",
            "Import_Items",
            "Commercial_Impact"
        ],

        "15_European_Naval_Power": [
            "Naval_Technology",
            "Portuguese_Navy",
            "Dutch_Navy",
            "English_Navy",
            "French_Navy",
            "Sea_Control",
            "Maritime_Strategy",
            "Naval_Supremacy"
        ],

        "16_Anglo_French_Rivalry_Background": [
            "European_Wars",
            "Colonial_Competition",
            "Strategic_Importance_of_India",
            "French_Ambitions",
            "British_Ambitions",
            "Political_Context",
            "Commercial_Rivalry",
            "Road_to_Carnatic_Wars"
        ],

        "17_First_Carnatic_War": [
            "Background",
            "Course_of_War",
            "Battle_of_St_Thome",
            "Role_of_Dupleix",
            "British_Response",
            "Treaty_of_Aix_la_Chapelle",
            "Results",
            "Historical_Significance"
        ],

        "18_Second_Carnatic_War": [
            "Succession_Disputes",
            "Chanda_Sahib",
            "Muhammad_Ali",
            "Robert_Clive",
            "Siege_of_Arcot",
            "French_British_Competition",
            "Results",
            "Historical_Impact"
        ],

        "19_Third_Carnatic_War": [
            "Seven_Years_War",
            "Count_de_Lally",
            "British_Strategy",
            "Battle_of_Wandiwash",
            "French_Defeat",
            "Treaty_of_Paris_1763",
            "End_of_French_Ambitions",
            "Historical_Significance"
        ],

        "20_Robert_Clive_Pre_Plassey": [
            "Early_Career",
            "Arcot_Campaign",
            "Military_Leadership",
            "Political_Strategy",
            "Role_in_Carnatic_Wars",
            "Rise_of_Influence",
            "British_Position",
            "Historical_Assessment"
        ],

        "21_European_Administration_and_Governance": [
            "Factory_Administration",
            "Governor_System",
            "Commercial_Management",
            "Judicial_Arrangements",
            "Military_Organization",
            "Revenue_Sources",
            "Administrative_Differences",
            "Governance_Practices"
        ],

        "22_Europeans_and_Indian_States": [
            "Relations_with_Mughals",
            "Relations_with_Deccan_States",
            "Relations_with_Carnatic",
            "Diplomatic_Practices",
            "Military_Alliances",
            "Commercial_Treaties",
            "Political_Influence",
            "Regional_Dynamics"
        ],

        "23_Socio_Cultural_Impact": [
            "Missionary_Activities",
            "Printing_Press",
            "Education",
            "Religious_Interactions",
            "Cultural_Exchange",
            "Language_Influence",
            "Art_and_Architecture",
            "Social_Changes"
        ],

        "24_Economic_Impact_on_India": [
            "Trade_Pattern_Changes",
            "Commercialization",
            "Impact_on_Indian_Merchants",
            "Port_City_Growth",
            "Export_Economy",
            "Monetary_Changes",
            "Regional_Effects",
            "Long_Term_Consequences"
        ],

        "25_British_Supremacy_Established": [
            "Reasons_for_British_Success",
            "Weakness_of_Rivals",
            "Naval_Superiority",
            "Financial_Strength",
            "Military_Organization",
            "Political_Diplomacy",
            "Commercial_Advantages",
            "Historical_Debates"
        ],

        "26_Important_Personalities": [
            "Vasco_da_Gama",
            "Almeida",
            "Albuquerque",
            "Thomas_Roe",
            "Dupleix",
            "Francois_Martin",
            "Robert_Clive",
            "Count_de_Lally"
        ],

        "27_Sources_and_Historiography": [
            "European_Records",
            "Company_Documents",
            "Travel_Accounts",
            "Indian_Sources",
            "Colonial_Historiography",
            "Nationalist_Interpretations",
            "Modern_Scholarship",
            "Source_Criticism"
        ],

        "28_Legacy_and_Significance": [
            "Beginning_of_Colonialism",
            "Commercial_Transformation",
            "Political_Consequences",
            "Military_Changes",
            "Administrative_Influence",
            "Cultural_Interactions",
            "Prelude_to_British_Rule",
            "Historical_Relevance"
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

    print(f"Creating Advent of Europeans structure in: {target_base}")
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
    create_advent_of_europeans_structure()