import os
import shutil

def create_maratha_empire_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "medieval-india", "maratha-empire")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Historical_Background": [
            "Deccan_Political_Situation",
            "Decline_of_Ahmadnagar",
            "Bijapur_Sultanate",
            "Mughal_Expansion_in_Deccan",
            "Socio_Economic_Conditions",
            "Bhakti_Movement_Influence",
            "Maratha_Identity",
            "Sources_of_Study"
        ],
        "02_Rise_of_Marathas": [
            "Shahaji_Bhosale",
            "Jijabai",
            "Early_Life_of_Shivaji",
            "Maval_Region",
            "Capture_of_First_Forts",
            "Formation_of_Political_Base",
            "Early_Alliances",
            "Historical_Significance"
        ],
        "03_Shivaji_Establishment_Phase": [
            "Conquest_of_Torna",
            "Conquest_of_Rajgad",
            "Conflict_with_Bijapur",
            "Afzal_Khan_Episode",
            "Siege_of_Panhala",
            "Expansion_in_Konkan",
            "Military_Consolidation",
            "Rise_of_Swarajya"
        ],
        "04_Shivaji_and_Mughals": [
            "Shaista_Khan_Campaign",
            "Surat_Raid",
            "Treaty_of_Purandar",
            "Visit_to_Agra",
            "Escape_from_Agra",
            "Renewed_Conflict",
            "Territorial_Recovery",
            "Political_Impact"
        ],
        "05_Shivaji_Coronation_and_Legacy": [
            "Coronation_1674",
            "Concept_of_Hindavi_Swarajya",
            "Royal_Titles",
            "State_Formation",
            "Religious_Policy",
            "Administrative_Vision",
            "Final_Years",
            "Historical_Assessment"
        ],
        "06_Maratha_Administration": [
            "Ashtapradhan_Council",
            "Central_Administration",
            "Provincial_Administration",
            "Revenue_Administration",
            "Judicial_System",
            "Village_Administration",
            "Bureaucracy",
            "Administrative_Legacy"
        ],
        "07_Maratha_Revenue_System": [
            "Land_Revenue",
            "Chauth",
            "Sardeshmukhi",
            "Assessment_Methods",
            "Revenue_Officials",
            "Agrarian_Policies",
            "Financial_Resources",
            "Economic_Impact"
        ],
        "08_Maratha_Military_System": [
            "Guerrilla_Warfare",
            "Fort_Administration",
            "Infantry",
            "Cavalry",
            "Navy",
            "Military_Command",
            "Intelligence_System",
            "Military_Strengths"
        ],
        "09_Maratha_Forts": [
            "Raigad",
            "Pratapgad",
            "Sinhagad",
            "Panhala",
            "Sindhudurg",
            "Purandar",
            "Strategic_Importance",
            "Fort_Management"
        ],
        "10_Successors_of_Shivaji": [
            "Sambhaji", "Rajaram", "Tarabai", "Shahu",
            "Succession_Disputes", "Mughal_Conflict",
            "Political_Reorganization", "Transition_to_Peshwa_Era"
        ],
        "11_Maratha_Mughal_Struggle": [
            "Aurangzeb_in_Deccan", "Capture_of_Sambhaji", "Maratha_Resistance",
            "Guerrilla_Campaigns", "War_of_27_Years", "Mughal_Exhaustion",
            "Maratha_Revival", "Historical_Consequences"
        ],
        "12_Rise_of_Peshwas": [
            "Office_of_Peshwa", "Balaji_Vishwanath", "Peshwa_Authority",
            "Political_Centralization", "Relations_with_Shahu",
            "Administrative_Changes", "Expansion_Policies", "Historical_Significance"
        ],
        "13_Baji_Rao_I": [
            "Military_Genius", "Northern_Expansion", "Campaigns_against_Nizam",
            "Battle_of_Palkhed", "Bundelkhand_Policy", "Delhi_Expedition",
            "Confederacy_Formation", "Historical_Assessment"
        ],
        "14_Nana_Saheb_Peshwa": [
            "Balaji_Baji_Rao", "Territorial_Expansion", "Administrative_Management",
            "Northern_Politics", "Relations_with_Mughals", "Confederacy_Strengthening",
            "Challenges", "Legacy"
        ],
        "15_Third_Battle_of_Panipat": [
            "Background", "Maratha_Expansion_in_North", "Ahmad_Shah_Abdali",
            "Campaign_Preparation", "Course_of_Battle", "Defeat_of_Marathas",
            "Immediate_Consequences", "Historical_Significance"
        ],
        "16_Post_Panipat_Revival": [
            "Madhav_Rao_I", "Administrative_Reforms", "Military_Reorganization",
            "Recovery_of_Power", "Northern_Politics", "Economic_Recovery",
            "Internal_Stability", "Legacy"
        ],
        "17_Later_Peshwas": [
            "Narayan_Rao", "Raghunath_Rao", "Sawai_Madhav_Rao", "Baji_Rao_II",
            "Court_Politics", "Factionalism", "Declining_Authority", "End_of_Peshwa_Rule"
        ],
        "18_Maratha_Confederacy": [
            "Concept_of_Confederacy", "Scindias", "Holkars", "Gaekwads",
            "Bhonsles_of_Nagpur", "Power_Sharing", "Regional_Autonomy", "Political_Impact"
        ],
        "19_Scindias": [
            "Ranoji_Scindia", "Mahadji_Scindia", "Daulat_Rao_Scindia",
            "North_Indian_Politics", "Military_Reforms", "Diplomacy",
            "Territorial_Control", "Legacy"
        ],
        "20_Holkars": [
            "Malhar_Rao_Holkar", "Ahilyabai_Holkar", "Yashwantrao_Holkar",
            "Administration", "Military_Affairs", "Regional_Expansion",
            "Patronage", "Legacy"
        ],
        "21_Bhonsles_and_Gaekwads": [
            "Nagpur_Bhonsles", "Raghuji_Bhonsle", "Eastern_Expansion",
            "Gaekwad_Family", "Baroda_State", "Administration",
            "Economic_Activities", "Legacy"
        ],
        "22_Maratha_Economy": [
            "Agriculture", "Trade_and_Commerce", "Ports", "Internal_Trade",
            "Craft_Production", "Coinage", "Urban_Centres", "Economic_Structure"
        ],
        "23_Maratha_Society": [
            "Social_Hierarchy", "Role_of_Women", "Village_Communities",
            "Education", "Customs_and_Traditions", "Urban_Society",
            "Peasant_Life", "Social_Changes"
        ],
        "24_Religion_and_Culture": [
            "Bhakti_Tradition", "Religious_Policy", "Temples_and_Patronage",
            "Literature", "Art_and_Architecture", "Festivals",
            "Language_and_Literature", "Cultural_Identity"
        ],
        "25_Maratha_Foreign_Relations": [
            "Relations_with_Mughals", "Relations_with_Nizam", "Relations_with_Mysore",
            "Relations_with_Rajputs", "Relations_with_Jats", "Relations_with_Sikhs",
            "Diplomatic_Policies", "Strategic_Alliances"
        ],
        "26_Anglo_Maratha_Relations": [
            "British_East_India_Company", "First_Anglo_Maratha_War", "Second_Anglo_Maratha_War",
            "Third_Anglo_Maratha_War", "Treaty_of_Bassein", "Military_Conflicts",
            "Political_Consequences", "End_of_Empire"
        ],
        "27_Sources_and_Historiography": [
            "Bakhar_Literature", "Persian_Sources", "European_Accounts",
            "Official_Records", "Colonial_Historiography", "Nationalist_Interpretations",
            "Modern_Research", "Source_Criticism"
        ],
        "28_Legacy_and_Significance": [
            "Political_Legacy", "Administrative_Legacy", "Military_Legacy",
            "Economic_Legacy", "Cultural_Legacy", "Role_in_Indian_History",
            "Influence_on_Nationalism", "Contemporary_Relevance"
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

    print(f"Creating Maratha Empire structure in: {target_base}")
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
    create_maratha_empire_structure()