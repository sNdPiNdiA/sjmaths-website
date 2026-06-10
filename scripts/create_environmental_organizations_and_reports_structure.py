import os
import shutil

def create_environmental_organizations_and_reports_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "environmental-organizations-and-reports"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Global_Environmental_Organizations": [
            "International_Environmental_Governance",
            "UN_System_and_Environment",
            "Multilateral_Organizations",
            "Intergovernmental_Organizations",
            "Global_Environmental_Cooperation",
            "Environmental_Policy_Networks",
            "Global_Environmental_Funding",
            "Institutional_Framework"
        ],

        "02_UNEP": [
            "Formation_of_UNEP",
            "Objectives_of_UNEP",
            "Governance_Structure",
            "UNEA",
            "Major_Environmental_Programmes",
            "Global_Environment_Outlook",
            "Role_in_Treaties",
            "Recent_Initiatives"
        ],

        "03_IPCC": [
            "Formation_of_IPCC",
            "Objectives_of_IPCC",
            "Working_Group_I",
            "Working_Group_II",
            "Working_Group_III",
            "Assessment_Reports",
            "Synthesis_Reports",
            "Recent_Findings"
        ],

        "04_IUCN": [
            "Formation_of_IUCN",
            "Objectives_of_IUCN",
            "IUCN_Red_List",
            "Protected_Area_Categories",
            "Species_Assessment",
            "Conservation_Programmes",
            "Global_Network",
            "Recent_Updates"
        ],

        "05_WWF": [
            "Formation_of_WWF",
            "Objectives_of_WWF",
            "Global_Conservation_Projects",
            "Living_Planet_Index",
            "Species_Conservation",
            "Climate_Programmes",
            "India_and_WWF",
            "Recent_Initiatives"
        ],

        "06_UNESCO_MAB_Programme": [
            "Man_and_Biosphere_Programme",
            "Objectives_of_MAB",
            "World_Network_of_Biosphere_Reserves",
            "Biosphere_Reserve_Criteria",
            "Core_Buffer_Transition_Zones",
            "Indian_Biosphere_Reserves",
            "Research_and_Monitoring",
            "Recent_Developments"
        ],

        "07_Global_Environment_Facility": [
            "Formation_of_GEF",
            "Objectives_of_GEF",
            "Funding_Mechanism",
            "Focal_Areas",
            "GEF_Projects",
            "Partnerships",
            "India_and_GEF",
            "Recent_Programmes"
        ],

        "08_Green_Climate_Fund": [
            "Formation_of_GCF",
            "Objectives_of_GCF",
            "Climate_Finance",
            "Mitigation_Funding",
            "Adaptation_Funding",
            "Funding_Approval_Process",
            "India_and_GCF",
            "Recent_Developments"
        ],

        "09_FAO_and_Environment": [
            "FAO_Formation",
            "Objectives_of_FAO",
            "Forestry_Programmes",
            "Sustainable_Agriculture",
            "Food_Security_and_Environment",
            "Global_Forest_Resources_Assessment",
            "FAO_Reports",
            "India_and_FAO"
        ],

        "10_CBD_and_Ramsar_Secretariats": [
            "CBD_Secretariat",
            "Ramsar_Secretariat",
            "Treaty_Administration",
            "Conference_of_Parties_Support",
            "Implementation_Monitoring",
            "International_Coordination",
            "Reporting_Frameworks",
            "Recent_Developments"
        ],

        "11_Indian_Environmental_Institutions": [
            "MoEFCC",
            "Environmental_Governance_in_India",
            "Policy_Formulation",
            "Regulatory_Framework",
            "Conservation_Administration",
            "Research_Institutions",
            "Implementation_Agencies",
            "Institutional_Coordination"
        ],

        "12_CPCB_and_SPCB": [
            "Central_Pollution_Control_Board",
            "State_Pollution_Control_Boards",
            "Functions_and_Powers",
            "Pollution_Monitoring",
            "Air_Quality_Management",
            "Water_Quality_Management",
            "Compliance_and_Enforcement",
            "Recent_Initiatives"
        ],

        "13_National_Biodiversity_Authority": [
            "Formation_of_NBA",
            "Objectives_of_NBA",
            "Access_and_Benefit_Sharing",
            "Biodiversity_Management_Committees",
            "People_Biodiversity_Registers",
            "State_Biodiversity_Boards",
            "Conservation_Framework",
            "Recent_Developments"
        ],

        "14_NTCA": [
            "Formation_of_NTCA",
            "Objectives_of_NTCA",
            "Project_Tiger_Governance",
            "Tiger_Reserve_Management",
            "Tiger_Census",
            "Conservation_Strategies",
            "Monitoring_Mechanisms",
            "Recent_Initiatives"
        ],

        "15_Wildlife_Institute_of_India": [
            "Formation_of_WII",
            "Research_Programmes",
            "Wildlife_Training",
            "Species_Conservation_Projects",
            "Ecological_Monitoring",
            "Capacity_Building",
            "Policy_Support",
            "Recent_Studies"
        ],

        "16_Botanical_Survey_of_India": [
            "Formation_of_BSI",
            "Floral_Diversity_Assessment",
            "Plant_Taxonomy",
            "Plant_Exploration",
            "Rare_and_Endemic_Plants",
            "Herbaria",
            "Research_Activities",
            "Recent_Projects"
        ],

        "17_Zoological_Survey_of_India": [
            "Formation_of_ZSI",
            "Faunal_Diversity_Assessment",
            "Animal_Taxonomy",
            "Species_Documentation",
            "Endangered_Species_Research",
            "Faunal_Surveys",
            "Research_Activities",
            "Recent_Projects"
        ],

        "18_Forest_Survey_of_India": [
            "Formation_of_FSI",
            "Forest_Cover_Assessment",
            "India_State_of_Forest_Report",
            "Forest_Inventory",
            "Remote_Sensing",
            "Forest_Fire_Monitoring",
            "Carbon_Stock_Assessment",
            "Recent_Findings"
        ],

        "19_Major_Environmental_Reports_and_Indices": [
            "Living_Planet_Report",
            "Global_Environment_Outlook",
            "Emissions_Gap_Report",
            "Adaptation_Gap_Report",
            "Global_Biodiversity_Outlook",
            "State_of_Forest_Report",
            "Environmental_Performance_Index",
            "World_Air_Quality_Report"
        ],

        "20_Current_Affairs_and_Environmental_Reports": [
            "Latest_IPCC_Reports",
            "Latest_UNEP_Reports",
            "Latest_IUCN_Updates",
            "Latest_Forest_Report",
            "Latest_Biodiversity_Report",
            "Latest_Climate_Finance_Updates",
            "Environmental_Rankings",
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

    print(f"Creating Environmental Organizations and Reports structure in: {target_base}")

    for category, topics in structure.items():
        category_path = os.path.join(category_path := os.path.join(target_base, category))
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
    create_environmental_organizations_and_reports_structure()