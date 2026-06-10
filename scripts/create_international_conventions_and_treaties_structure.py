import os
import shutil

def create_international_conventions_and_treaties_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "international-conventions-and-treaties"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Global_Environmental_Governance": [
            "Evolution_of_Environmental_Governance",
            "Stockholm_Conference_1972",
            "Rio_Earth_Summit_1992",
            "Johannesburg_Summit_2002",
            "Rio_Plus_20",
            "Global_Environmental_Agenda",
            "Multilateral_Environmental_Agreements",
            "Principles_of_Global_Cooperation"
        ],

        "02_United_Nations_Environment_Programme": [
            "Establishment_of_UNEP",
            "Objectives_of_UNEP",
            "Governance_Structure",
            "Major_Initiatives",
            "Global_Environment_Outlook",
            "Role_in_International_Treaties",
            "Funding_and_Partnerships",
            "Recent_Developments"
        ],

        "03_Stockholm_Conference_1972": [
            "Background_of_Conference",
            "Stockholm_Declaration",
            "Action_Plan_for_Human_Environment",
            "Environmental_Rights",
            "Institutional_Outcomes",
            "Creation_of_UNEP",
            "Impact_on_Environmental_Law",
            "Significance_for_Developing_Countries"
        ],

        "04_Rio_Earth_Summit_1992": [
            "Rio_Declaration",
            "Agenda_21",
            "Forest_Principles",
            "Sustainable_Development_Concept",
            "Climate_Change_Framework",
            "Biodiversity_Framework",
            "Institutional_Outcomes",
            "Global_Impact"
        ],

        "05_UNFCCC": [
            "Objectives_of_UNFCCC",
            "Principles_of_UNFCCC",
            "Conference_of_Parties",
            "Common_But_Differentiated_Responsibilities",
            "National_Communications",
            "Financial_Mechanisms",
            "Technology_Transfer",
            "Implementation_Framework"
        ],

        "06_Kyoto_Protocol": [
            "Background_of_Kyoto_Protocol",
            "Emission_Reduction_Targets",
            "Annex_I_Countries",
            "Clean_Development_Mechanism",
            "Joint_Implementation",
            "Emission_Trading",
            "Commitment_Periods",
            "Achievements_and_Limitations"
        ],

        "07_Paris_Agreement": [
            "Objectives_of_Paris_Agreement",
            "Nationally_Determined_Contributions",
            "Global_Stocktake",
            "Temperature_Goals",
            "Climate_Finance",
            "Adaptation_Framework",
            "Loss_and_Damage",
            "India_and_Paris_Agreement"
        ],

        "08_Conference_of_Parties_COP": [
            "COP_Mechanism",
            "COP21_Paris",
            "COP26_Glasgow",
            "COP27_Sharm_El_Sheikh",
            "COP28_Dubai",
            "Climate_Negotiations",
            "Key_Decisions",
            "Recent_Outcomes"
        ],

        "09_Convention_on_Biological_Diversity": [
            "Objectives_of_CBD",
            "Conservation_of_Biodiversity",
            "Sustainable_Use",
            "Benefit_Sharing",
            "Conference_of_Parties_CBD",
            "National_Biodiversity_Strategies",
            "Implementation_Framework",
            "India_and_CBD"
        ],

        "10_Cartagena_Protocol": [
            "Biosafety_Framework",
            "Living_Modified_Organisms",
            "Risk_Assessment",
            "Advance_Informed_Agreement",
            "Information_Sharing",
            "Compliance_Mechanism",
            "Implementation_Issues",
            "India_and_Cartagena_Protocol"
        ],

        "11_Nagoya_Protocol": [
            "Access_to_Genetic_Resources",
            "Benefit_Sharing_Framework",
            "Traditional_Knowledge",
            "Compliance_Measures",
            "International_Cooperation",
            "Implementation_Mechanisms",
            "National_Obligations",
            "India_and_Nagoya_Protocol"
        ],

        "12_Ramsar_Convention": [
            "Wetland_Conservation",
            "Wise_Use_Principle",
            "Ramsar_Sites",
            "Montreux_Record",
            "Wetland_Designation_Criteria",
            "International_Cooperation",
            "Ramsar_Sites_in_India",
            "Recent_Developments"
        ],

        "13_CITES": [
            "Objectives_of_CITES",
            "Appendix_I",
            "Appendix_II",
            "Appendix_III",
            "Wildlife_Trade_Regulation",
            "Permit_System",
            "Implementation_Mechanisms",
            "India_and_CITES"
        ],

        "14_Convention_on_Migratory_Species": [
            "Objectives_of_CMS",
            "Appendix_I_Species",
            "Appendix_II_Species",
            "Migratory_Species_Conservation",
            "International_Cooperation",
            "Species_Action_Plans",
            "India_and_CMS",
            "Recent_Developments"
        ],

        "15_Vienna_Convention_and_Montreal_Protocol": [
            "Ozone_Layer_Protection",
            "Vienna_Convention",
            "Montreal_Protocol",
            "Ozone_Depleting_Substances",
            "Phase_Out_Schedules",
            "Multilateral_Fund",
            "Kigali_Amendment",
            "India_and_Ozone_Regime"
        ],

        "16_UNCCD": [
            "Objectives_of_UNCCD",
            "Land_Degradation",
            "Desertification_Control",
            "Land_Degradation_Neutrality",
            "National_Action_Programmes",
            "Conference_of_Parties_UNCCD",
            "India_and_UNCCD",
            "Recent_Initiatives"
        ],

        "17_Basel_Convention": [
            "Hazardous_Waste_Movement",
            "Prior_Informed_Consent",
            "Waste_Trade_Regulation",
            "Environmentally_Sound_Management",
            "Basel_Ban_Amendment",
            "Compliance_Mechanisms",
            "India_and_Basel_Convention",
            "Recent_Developments"
        ],

        "18_Rotterdam_Convention": [
            "Hazardous_Chemicals",
            "Prior_Informed_Consent_Procedure",
            "Chemical_Trade_Regulation",
            "Information_Exchange",
            "Implementation_Framework",
            "Compliance_Measures",
            "India_and_Rotterdam_Convention",
            "Recent_Updates"
        ],

        "19_Stockholm_Convention_on_POPs": [
            "Persistent_Organic_Pollutants",
            "Elimination_of_POPs",
            "Restriction_Measures",
            "Monitoring_Framework",
            "Chemical_Management",
            "Implementation_Mechanisms",
            "India_and_Stockholm_Convention",
            "Recent_Developments"
        ],

        "20_India_Led_Global_Environmental_Initiatives": [
            "International_Solar_Alliance",
            "Coalition_for_Disaster_Resilient_Infrastructure",
            "Mission_LiFE",
            "Global_Biofuel_Alliance",
            "Mission_Innovation",
            "One_Sun_One_World_One_Grid",
            "India_Climate_Leadership",
            "Current_Affairs_and_UPSC_Topics"
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

    print(f"Creating International Conventions and Treaties structure in: {target_base}")

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
    create_international_conventions_and_treaties_structure()