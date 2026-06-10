import os
import shutil

def create_national_laws_and_policies_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
"environment",
"national-laws-and-policies"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

    "01_Constitutional_Provisions_and_Environment": [
        "Article_48A",
        "Article_51A_g",
        "Right_to_Life_and_Environment",
        "Directive_Principles_and_Environment",
        "Fundamental_Duties_and_Environment",
        "Environmental_Federalism",
        "Legislative_Powers",
        "Constitutional_Amendments_and_Environment"
    ],

    "02_Environment_Protection_Act_1986": [
        "Background_of_EPA_1986",
        "Objectives_of_EPA",
        "Key_Definitions",
        "Central_Government_Powers",
        "Environmental_Standards",
        "Hazardous_Substances_Regulation",
        "Inspection_and_Enforcement",
        "Penalties_and_Offences"
    ],

    "03_Water_Prevention_and_Control_of_Pollution_Act_1974": [
        "Objectives_of_Water_Act",
        "Water_Pollution_Definition",
        "CPCB_and_SPCB_Under_Water_Act",
        "Consent_to_Establish",
        "Consent_to_Operate",
        "Monitoring_and_Sampling",
        "Penalties",
        "Implementation_Issues"
    ],

    "04_Air_Prevention_and_Control_of_Pollution_Act_1981": [
        "Objectives_of_Air_Act",
        "Air_Pollution_Control_Areas",
        "Emission_Standards",
        "Industrial_Regulation",
        "Monitoring_Mechanisms",
        "Inspection_Powers",
        "Penalties",
        "Recent_Amendments"
    ],

    "05_Forest_Conservation_Act": [
        "Objectives_of_FCA",
        "Forest_Diversion",
        "Central_Approval_Requirement",
        "Compensatory_Afforestation",
        "Forest_Clearance_Procedure",
        "Protected_Forest_Lands",
        "Amendments",
        "Implementation_Challenges"
    ],

    "06_Indian_Forest_Act_1927": [
        "Reserved_Forests",
        "Protected_Forests",
        "Village_Forests",
        "Forest_Offences",
        "Transit_of_Forest_Produce",
        "Forest_Administration",
        "Forest_Revenue",
        "Criticism_and_Reforms"
    ],

    "07_Wildlife_Protection_Act_1972": [
        "Objectives_of_WPA",
        "Protected_Areas",
        "Schedules_Under_WPA",
        "Wildlife_Crime_Control",
        "National_Board_for_Wildlife",
        "Conservation_Reserves",
        "Community_Reserves",
        "Recent_Amendments"
    ],

    "08_Biological_Diversity_Act_2002": [
        "Objectives_of_BDA",
        "Access_and_Benefit_Sharing",
        "National_Biodiversity_Authority",
        "State_Biodiversity_Boards",
        "Biodiversity_Management_Committees",
        "People_Biodiversity_Register",
        "Traditional_Knowledge_Protection",
        "Recent_Changes"
    ],

    "09_Forest_Rights_Act_2006": [
        "Historical_Background",
        "Individual_Forest_Rights",
        "Community_Forest_Rights",
        "Community_Forest_Resource_Rights",
        "Forest_Dwelling_Communities",
        "Gram_Sabha_Role",
        "Recognition_Process",
        "Implementation_Status"
    ],

    "10_Environment_Impact_Assessment": [
        "EIA_Concept",
        "EIA_Notification_2006",
        "Project_Categorization",
        "Screening",
        "Scoping",
        "Public_Hearing",
        "Environmental_Clearance",
        "Post_Clearance_Monitoring"
    ],

    "11_Coastal_Regulation_Zone": [
        "CRZ_Background",
        "CRZ_I",
        "CRZ_II",
        "CRZ_III",
        "CRZ_IV",
        "Permitted_Activities",
        "Restricted_Activities",
        "CRZ_Notifications"
    ],

    "12_Waste_Management_Rules": [
        "Solid_Waste_Management_Rules",
        "Plastic_Waste_Management_Rules",
        "E_Waste_Management_Rules",
        "Biomedical_Waste_Rules",
        "Hazardous_Waste_Rules",
        "Construction_and_Demolition_Waste_Rules",
        "Battery_Waste_Management_Rules",
        "Extended_Producer_Responsibility"
    ],

    "13_Pollution_Control_Institutions": [
        "Central_Pollution_Control_Board",
        "State_Pollution_Control_Boards",
        "Functions_of_CPCB",
        "Functions_of_SPCB",
        "Pollution_Monitoring",
        "Compliance_and_Enforcement",
        "Environmental_Data_Management",
        "Institutional_Challenges"
    ],

    "14_National_Green_Tribunal": [
        "NGT_Act_2010",
        "Jurisdiction_of_NGT",
        "Powers_of_NGT",
        "Environmental_Principles",
        "Compensation_and_Relief",
        "Landmark_Judgements",
        "Appeals_Process",
        "Recent_Developments"
    ],

    "15_Climate_Change_Policies": [
        "National_Action_Plan_on_Climate_Change",
        "State_Action_Plans_on_Climate_Change",
        "Climate_Mitigation",
        "Climate_Adaptation",
        "Carbon_Reduction_Strategies",
        "Net_Zero_Targets",
        "Green_Finance",
        "Policy_Challenges"
    ],

    "16_NAPCC_Missions": [
        "National_Solar_Mission",
        "National_Water_Mission",
        "Green_India_Mission",
        "Sustainable_Agriculture_Mission",
        "Sustainable_Habitat_Mission",
        "Energy_Efficiency_Mission",
        "Himalayan_Ecosystem_Mission",
        "Strategic_Knowledge_Mission"
    ],

    "17_Forest_and_Afforestation_Policies": [
        "National_Forest_Policy_1988",
        "National_Forest_Policy_Reforms",
        "Afforestation_Programmes",
        "Compensatory_Afforestation_Fund",
        "CAMPA",
        "Green_India_Mission",
        "Agroforestry_Policy",
        "Forest_Cover_Targets"
    ],

    "18_Wetland_and_River_Policies": [
        "Wetlands_Rules",
        "National_Wetland_Conservation",
        "Ramsar_Site_Management",
        "Namami_Gange",
        "National_River_Conservation_Plan",
        "Lake_Conservation",
        "Ecological_Flow",
        "River_Rejuvenation"
    ],

    "19_Energy_and_Environmental_Policies": [
        "Renewable_Energy_Policy",
        "National_Biofuel_Policy",
        "National_Green_Hydrogen_Mission",
        "Energy_Efficiency_Framework",
        "Clean_Energy_Transition",
        "Emission_Reduction_Strategies",
        "Carbon_Markets",
        "Green_Finance_Framework"
    ],

    "20_Current_Affairs_and_Policy_Updates": [
        "Recent_Environmental_Amendments",
        "Supreme_Court_Judgements",
        "NGT_Judgements",
        "Parliamentary_Developments",
        "Government_Initiatives",
        "Economic_Survey_Environment",
        "India_Environment_Report",
        "UPSC_High_Yield_Current_Affairs"
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

    print(f"Creating National Laws and Policies structure in: {target_base}")

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
    create_national_laws_and_policies_structure()