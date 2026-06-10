import os
import shutil

def create_british_expansion_and_policies_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "british-expansion-and-policies")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Foundation_of_British_Power": [
            "Battle_of_Plassey",
            "Mir_Jafar",
            "Battle_of_Buxar",
            "Treaty_of_Allahabad",
            "Diwani_Rights",
            "Dual_Government_in_Bengal",
            "Rise_of_Company_State",
            "Historical_Significance"
        ],
        "02_Robert_Clive": [
            "Early_Career",
            "Bengal_Politics",
            "Military_Strategy",
            "Dual_Government",
            "Administrative_Measures",
            "Relations_with_Nawabs",
            "Second_Governorship",
            "Historical_Assessment"
        ],
        "03_Warren_Hastings": [
            "Administrative_Reforms",
            "Judicial_Reforms",
            "Revenue_Reforms",
            "Regulating_Act_1773",
            "Rohilla_War",
            "Relations_with_Indian_States",
            "Impeachment",
            "Historical_Assessment"
        ],
        "04_Cornwallis": [
            "Cornwallis_Code",
            "Judicial_Reforms",
            "Police_Reforms",
            "Civil_Service_Reforms",
            "Permanent_Settlement",
            "Administrative_Reorganization",
            "Relations_with_Indian_States",
            "Historical_Assessment"
        ],
        "05_Wellesley": [
            "Subsidiary_Alliance",
            "Expansionist_Policy",
            "Fort_William_College",
            "Diplomatic_Strategy",
            "Control_of_Indian_States",
            "Military_Expansion",
            "Political_Influence",
            "Historical_Assessment"
        ],
        "06_Anglo_Mysore_Wars": [
            "Hyder_Ali",
            "First_Anglo_Mysore_War",
            "Second_Anglo_Mysore_War",
            "Third_Anglo_Mysore_War",
            "Tipu_Sultan",
            "Fourth_Anglo_Mysore_War",
            "Treaties_and_Results",
            "Historical_Impact"
        ],
        "07_Anglo_Maratha_Wars": [
            "First_Anglo_Maratha_War",
            "Treaty_of_Salbai",
            "Second_Anglo_Maratha_War",
            "Treaty_of_Bassein",
            "Third_Anglo_Maratha_War",
            "Defeat_of_Peshwas",
            "Annexations",
            "Historical_Consequences"
        ],
        "08_Anglo_Sikh_Wars": [
            "Ranjit_Singh_Legacy",
            "First_Anglo_Sikh_War",
            "Treaty_of_Lahore",
            "Second_Anglo_Sikh_War",
            "Annexation_of_Punjab",
            "British_Punjab_Administration",
            "Military_Impact",
            "Historical_Significance"
        ],
        "09_Other_Conquests_and_Annexations": [
            "Sindh_Annexation",
            "Afghan_Policy",
            "Burma_Wars",
            "Assam_Annexation",
            "Coorg",
            "Awadh_Relations",
            "Frontier_Expansion",
            "Territorial_Growth"
        ],
        "10_Dalhousie": [
            "Doctrine_of_Lapse",
            "Railway_Policy",
            "Telegraph",
            "Postal_Reforms",
            "Public_Works",
            "Administrative_Centralization",
            "Territorial_Annexations",
            "Historical_Assessment"
        ],
        "11_Company_Administration": [
            "Court_of_Directors",
            "Board_of_Control",
            "Governor_General",
            "Presidency_System",
            "Central_Administration",
            "Provincial_Administration",
            "Bureaucracy",
            "Administrative_Structure"
        ],
        "12_Constitutional_Development": [
            "Regulating_Act_1773",
            "Pitts_India_Act_1784",
            "Charter_Act_1793",
            "Charter_Act_1813",
            "Charter_Act_1833",
            "Charter_Act_1853",
            "Government_of_India_Act_1858",
            "Constitutional_Impact"
        ],
        "13_Judicial_Administration": [
            "Supreme_Court_Calcutta",
            "Adalat_System",
            "Civil_Courts",
            "Criminal_Courts",
            "Cornwallis_Code",
            "Legal_Reforms",
            "Judicial_Hierarchy",
            "Impact_on_Indian_Society"
        ],
        "14_Civil_Services_and_Police": [
            "Civil_Service_System",
            "Covenanted_Service",
            "Police_Reforms",
            "District_Administration",
            "Collector",
            "Magistrate",
            "Recruitment_Policies",
            "Administrative_Control"
        ],
        "15_Revenue_Policies": [
            "Permanent_Settlement",
            "Ryotwari_System",
            "Mahalwari_System",
            "Land_Assessment",
            "Revenue_Collection",
            "Peasant_Impact",
            "Zamindari_Class",
            "Economic_Consequences"
        ],
        "16_Agrarian_Changes": [
            "Commercialization_of_Agriculture",
            "Cash_Crops",
            "Indigo_Cultivation",
            "Opium_Trade",
            "Peasant_Conditions",
            "Rural_Indebtedness",
            "Land_Alienation",
            "Agrarian_Crisis"
        ],
        "17_Trade_and_Economic_Policies": [
            "Free_Trade_Policy",
            "Deindustrialization",
            "Drain_of_Wealth",
            "Trade_Monopoly",
            "Import_Export_Patterns",
            "Indian_Industries",
            "Economic_Exploitation",
            "Economic_Critique"
        ],
        "18_Transport_and_Communication": [
            "Railways",
            "Roads",
            "Canals",
            "Telegraph",
            "Postal_System",
            "Ports",
            "Commercial_Integration",
            "Economic_Impact"
        ],
        "19_Education_Policy": [
            "Orientalist_Anglicist_Controversy",
            "Macaulays_Minute",
            "English_Education_Act",
            "Woods_Despatch",
            "Universities_1857",
            "Missionary_Education",
            "Educational_Institutions",
            "Impact_of_Education"
        ],
        "20_Social_and_Religious_Policies": [
            "Sati_Abolition",
            "Widow_Remarriage",
            "Female_Education",
            "Missionary_Activities",
            "Social_Legislation",
            "Religious_Interference_Debate",
            "Reform_Policies",
            "Indian_Response"
        ],
        "21_Army_and_Military_Policies": [
            "Company_Army",
            "Recruitment_Patterns",
            "European_Officers",
            "Sepoys",
            "Military_Organization",
            "Military_Reforms",
            "Artillery",
            "Strategic_Control"
        ],
        "22_Indian_States_and_Paramountcy": [
            "Subsidiary_Alliance_System",
            "Doctrine_of_Lapse_Impact",
            "Princely_States",
            "Resident_System",
            "British_Paramountcy",
            "Awadh",
            "Hyderabad",
            "Political_Control"
        ],
        "23_Tribal_and_Peasant_Resistance": [
            "Sanyasi_Rebellion",
            "Chuar_Rebellion",
            "Kol_Uprising",
            "Santhal_Rebellion",
            "Paika_Rebellion",
            "Tribal_Resistance",
            "Peasant_Resistance",
            "Causes_and_Impact"
        ],
        "24_Pre_1857_Military_Revolts": [
            "Vellore_Mutiny",
            "Barrackpore_Incident",
            "Sepoy_Discontent",
            "Military_Grievances",
            "Religious_Factors",
            "Administrative_Factors",
            "Warning_Signs",
            "Historical_Importance"
        ],
        "25_Foreign_and_Frontier_Policy": [
            "North_West_Frontier",
            "Afghanistan_Policy",
            "Great_Game",
            "Burma_Policy",
            "Tibet_Relations",
            "Persia_Relations",
            "Strategic_Concerns",
            "Imperial_Defence"
        ],
        "26_Sources_and_Historiography": [
            "Company_Records",
            "Official_Correspondence",
            "Parliamentary_Papers",
            "Indian_Sources",
            "Colonial_Historiography",
            "Nationalist_Historiography",
            "Marxist_Interpretations",
            "Modern_Research"
        ],
        "27_Impact_of_British_Expansion": [
            "Political_Transformation",
            "Administrative_Changes",
            "Economic_Transformation",
            "Social_Changes",
            "Military_Changes",
            "Cultural_Impact",
            "Regional_Consequences",
            "Long_Term_Effects"
        ],
        "28_Legacy_and_Historical_Assessment": [
            "Colonial_State_Formation",
            "Modern_Administration",
            "Infrastructure_Legacy",
            "Economic_Legacy",
            "Educational_Legacy",
            "Social_Legacy",
            "Debates_on_Colonialism",
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

    print(f"Creating British Expansion and Policies structure in: {target_base}")
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
    create_british_expansion_and_policies_structure()