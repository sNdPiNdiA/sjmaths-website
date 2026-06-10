import os
import shutil

def create_revolt_of_1857_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "modern-india", "revolt-of-1857")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Background_of_the_Revolt": [
            "British_Expansion",
            "Company_Rule",
            "Administrative_Changes",
            "Economic_Transformation",
            "Social_Changes",
            "Religious_Concerns",
            "Military_Changes",
            "Historical_Background"
        ],

        "02_Political_Causes": [
            "Doctrine_of_Lapse",
            "Annexation_of_Awadh",
            "Subsidiary_Alliance_Impact",
            "Displacement_of_Rulers",
            "Loss_of_Privileges",
            "Political_Dissatisfaction",
            "British_Paramountcy",
            "Political_Grievances"
        ],

        "03_Economic_Causes": [
            "Revenue_Policies",
            "Peasant_Distress",
            "Decline_of_Handicrafts",
            "Commercialization_of_Agriculture",
            "Drain_of_Wealth",
            "Zamindar_Grievances",
            "Economic_Exploitation",
            "Economic_Discontent"
        ],

        "04_Social_and_Religious_Causes": [
            "Missionary_Activities",
            "Social_Reforms",
            "Religious_Fears",
            "Conversion_Apprehensions",
            "Westernization",
            "Education_Policies",
            "Traditional_Institutions",
            "Social_Grievances"
        ],

        "05_Military_Causes": [
            "Sepoy_Discontent",
            "Pay_and_Allowances",
            "Promotion_Policies",
            "General_Service_Enlistment_Act",
            "Racial_Discrimination",
            "Military_Reforms",
            "Greased_Cartridge_Issue",
            "Military_Grievances"
        ],

        "06_Immediate_Cause": [
            "Enfield_Rifle",
            "Greased_Cartridges",
            "Barrackpore_Incident",
            "Mangal_Pandey",
            "Meerut_Cantonment",
            "Court_Martials",
            "Sepoy_Reaction",
            "Outbreak_of_Revolt"
        ],

        "07_Outbreak_and_Spread": [
            "Meerut_Revolt",
            "March_to_Delhi",
            "Capture_of_Delhi",
            "Spread_to_North_India",
            "Communication_Networks",
            "Popular_Participation",
            "Regional_Extension",
            "Chronology_of_Events"
        ],

        "08_Delhi_Centre": [
            "Bahadur_Shah_II",
            "Bakht_Khan",
            "Delhi_Administration",
            "Military_Operations",
            "Siege_of_Delhi",
            "British_Recapture",
            "Leadership_Issues",
            "Historical_Significance"
        ],

        "09_Kanpur_Centre": [
            "Nana_Sahib",
            "Azimullah_Khan",
            "Tatya_Tope_in_Kanpur",
            "Siege_of_Kanpur",
            "British_Response",
            "Military_Events",
            "Collapse_of_Resistance",
            "Historical_Assessment"
        ],

        "10_Lucknow_Centre": [
            "Begum_Hazrat_Mahal",
            "Birjis_Qadr",
            "Awadh_Rebellion",
            "Residency_Siege",
            "Popular_Participation",
            "British_Operations",
            "Suppression",
            "Historical_Impact"
        ],

        "11_Jhansi_Centre": [
            "Rani_Lakshmibai",
            "Doctrine_of_Lapse_Context",
            "Organization_of_Resistance",
            "Military_Campaigns",
            "Alliance_with_Tatya_Tope",
            "Siege_of_Jhansi",
            "Fall_of_Jhansi",
            "Legacy"
        ],

        "12_Gwalior_Centre": [
            "Tatya_Tope",
            "Capture_of_Gwalior",
            "Scindia_Position",
            "Military_Strategy",
            "Final_Campaigns",
            "British_Recapture",
            "Resistance_Efforts",
            "Historical_Significance"
        ],

        "13_Bihar_Centre": [
            "Kunwar_Singh",
            "Jagdishpur",
            "Military_Operations",
            "Local_Support",
            "Resistance_Strategies",
            "British_Response",
            "Campaigns_in_Bihar",
            "Historical_Assessment"
        ],

        "14_Rohilkhand_and_Bareilly": [
            "Khan_Bahadur_Khan",
            "Regional_Leadership",
            "Military_Operations",
            "Popular_Support",
            "British_Campaigns",
            "Suppression",
            "Regional_Impact",
            "Historical_Significance"
        ],

        "15_Other_Centres_of_Revolt": [
            "Faizabad",
            "Allahabad",
            "Banaras",
            "Farrukhabad",
            "Arrah",
            "Central_India",
            "Minor_Centres",
            "Regional_Variations"
        ],

        "16_Leaders_of_the_Revolt": [
            "Bahadur_Shah_Zafar",
            "Nana_Sahib",
            "Rani_Lakshmibai",
            "Tatya_Tope",
            "Kunwar_Singh",
            "Begum_Hazrat_Mahal",
            "Bakht_Khan",
            "Comparative_Assessment"
        ],

        "17_Participants_and_Social_Base": [
            "Sepoys",
            "Peasants",
            "Zamindars",
            "Talukdars",
            "Princes",
            "Artisans",
            "Religious_Groups",
            "Social_Composition"
        ],

        "18_Regions_Remaining_Quiet": [
            "Punjab",
            "Bengal",
            "Bombay_Presidency",
            "Madras_Presidency",
            "Sikh_Response",
            "Gurkha_Response",
            "Princely_States",
            "Reasons_for_Non_Participation"
        ],

        "19_British_Suppression": [
            "Military_Reinforcements",
            "Punjab_Base",
            "Role_of_Sikhs",
            "Role_of_Gurkhas",
            "British_Strategy",
            "Major_Campaigns",
            "Repression",
            "Restoration_of_Control"
        ],

        "20_Reasons_for_Failure": [
            "Lack_of_Central_Leadership",
            "Limited_Geographical_Spread",
            "Poor_Coordination",
            "Military_Weaknesses",
            "Resource_Limitations",
            "Support_for_British",
            "Strategic_Disadvantages",
            "Historical_Debates"
        ],

        "21_Administrative_Consequences": [
            "End_of_Company_Rule",
            "Government_of_India_Act_1858",
            "Secretary_of_State",
            "Viceroy_System",
            "Administrative_Reorganization",
            "Civil_Service_Changes",
            "Centralization",
            "Political_Consequences"
        ],

        "22_Military_Consequences": [
            "Army_Reorganization",
            "Recruitment_Policies",
            "Ratio_of_Forces",
            "Artillery_Control",
            "Martial_Race_Theory",
            "Military_Policies",
            "Security_Measures",
            "Long_Term_Impact"
        ],

        "23_Social_and_Political_Consequences": [
            "Policy_Towards_Princes",
            "Policy_Towards_Landlords",
            "Communal_Policies",
            "Social_Changes",
            "Conservative_Shift",
            "Political_Reorientation",
            "British_Attitudes",
            "Long_Term_Effects"
        ],

        "24_Historiography": [
            "Sepoy_Mutiny_Theory",
            "Nationalist_Interpretation",
            "First_War_of_Independence",
            "Marxist_View",
            "Revisionist_Interpretations",
            "Subaltern_Studies",
            "Modern_Debates",
            "Comparative_Assessment"
        ],

        "25_Sources": [
            "Official_Records",
            "Government_Reports",
            "Personal_Memoirs",
            "Indian_Accounts",
            "Newspapers",
            "Military_Records",
            "Contemporary_Writings",
            "Source_Criticism"
        ],

        "26_Memory_and_Legacy": [
            "Nationalist_Memory",
            "Popular_Culture",
            "Literature_and_Poetry",
            "Memorials",
            "Regional_Memories",
            "Freedom_Movement_Influence",
            "Public_History",
            "Legacy_in_Modern_India"
        ],

        "27_Comparative_Study": [
            "Comparison_with_Tribal_Revolts",
            "Comparison_with_Peasant_Movements",
            "Comparison_with_European_Revolutions",
            "Nature_of_Revolt",
            "Military_vs_Popular_Revolt",
            "Regional_Differences",
            "Leadership_Patterns",
            "Historical_Uniqueness"
        ],

        "28_UPSC_and_Exam_Themes": [
            "Nature_of_the_Revolt",
            "Causes_vs_Immediate_Cause",
            "Role_of_Leaders",
            "Reasons_for_Failure",
            "Consequences",
            "Historiographical_Debates",
            "PYQ_Themes",
            "Mains_Answer_Frameworks"
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

    print(f"Creating Revolt of 1857 structure in: {target_base}")
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
    create_revolt_of_1857_structure()