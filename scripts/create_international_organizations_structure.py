import os
import shutil

def create_international_organizations_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "international-organizations"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Global_Economic_Governance": [
            "Global_Economic_Order",
            "Multilateralism",
            "International_Cooperation",
            "Global_Institutions",
            "Economic_Governance",
            "Policy_Coordination",
            "Globalization",
            "Institutional_Framework"
        ],

        "02_Bretton_Woods_System": [
            "Bretton_Woods_Conference",
            "Post_War_Order",
            "Fixed_Exchange_System",
            "Dollar_System",
            "Institution_Creation",
            "Global_Reconstruction",
            "Economic_Stability",
            "Historical_Significance"
        ],

        "03_International_Monetary_Fund": [
            "IMF_Formation",
            "IMF_Objectives",
            "Membership",
            "Quota_System",
            "Voting_Power",
            "Financial_Assistance",
            "Surveillance_Function",
            "Technical_Assistance"
        ],

        "04_IMF_Lending_and_Reforms": [
            "Balance_of_Payments_Support",
            "Structural_Adjustment",
            "Conditionalities",
            "Extended_Fund_Facility",
            "Poverty_Reduction_Facility",
            "Special_Drawing_Rights",
            "Reform_Debates",
            "India_and_IMF"
        ],

        "05_World_Bank_Group": [
            "World_Bank_Formation",
            "IBRD",
            "IDA",
            "IFC",
            "MIGA",
            "ICSID",
            "Development_Finance",
            "Project_Assistance"
        ],

        "06_World_Bank_Operations": [
            "Infrastructure_Funding",
            "Social_Sector_Projects",
            "Poverty_Reduction",
            "Development_Policy_Loans",
            "Knowledge_Services",
            "Capacity_Building",
            "Country_Strategies",
            "India_Partnership"
        ],

        "07_World_Trade_Organization": [
            "WTO_Formation",
            "Trade_Governance",
            "Trade_Rules",
            "Dispute_Settlement",
            "Ministerial_Conference",
            "Trade_Liberalization",
            "Multilateral_Trade_System",
            "India_and_WTO"
        ],

        "08_WTO_Agreements": [
            "GATT",
            "GATS",
            "TRIPS",
            "Agriculture_Agreement",
            "Subsidies_Agreement",
            "Trade_Facilitation",
            "Doha_Round",
            "Negotiation_Issues"
        ],

        "09_United_Nations_Economic_Agencies": [
            "UNDP",
            "UNCTAD",
            "UNIDO",
            "ECOSOC",
            "UNEP",
            "Economic_Coordination",
            "Development_Programmes",
            "Global_Initiatives"
        ],

        "10_UNDP_and_Human_Development": [
            "Human_Development_Report",
            "HDI",
            "Inclusive_Growth",
            "Sustainable_Development",
            "Capacity_Building",
            "Poverty_Alleviation",
            "Governance_Support",
            "India_Engagement"
        ],

        "11_UNCTAD": [
            "Trade_and_Development",
            "Developing_Countries",
            "Investment_Analysis",
            "Commodity_Markets",
            "Global_Trade_Data",
            "Policy_Research",
            "South_South_Cooperation",
            "India_Perspective"
        ],

        "12_Asian_Development_Bank": [
            "ADB_Formation",
            "Membership",
            "Infrastructure_Finance",
            "Regional_Cooperation",
            "Development_Assistance",
            "Project_Funding",
            "Technical_Assistance",
            "India_and_ADB"
        ],

        "13_Asian_Infrastructure_Investment_Bank": [
            "AIIB_Formation",
            "Infrastructure_Development",
            "Multilateral_Financing",
            "Project_Portfolio",
            "Regional_Connectivity",
            "Investment_Framework",
            "India_Membership",
            "Governance_Structure"
        ],

        "14_New_Development_Bank": [
            "BRICS_Bank",
            "Sustainable_Development",
            "Infrastructure_Finance",
            "Local_Currency_Financing",
            "Project_Assistance",
            "Emerging_Economies",
            "Institutional_Structure",
            "India_Role"
        ],

        "15_BRICS_Economic_Cooperation": [
            "BRICS_Formation",
            "Economic_Coordination",
            "Development_Priorities",
            "Trade_Cooperation",
            "Financial_Collaboration",
            "Institution_Building",
            "Expansion_of_BRICS",
            "India_Engagement"
        ],

        "16_G20": [
            "G20_Formation",
            "Global_Economic_Coordination",
            "Financial_Stability",
            "Development_Agenda",
            "Summit_Process",
            "Consensus_Building",
            "India_Presidency",
            "Global_Impact"
        ],

        "17_OECD_and_Global_Standards": [
            "OECD_Structure",
            "Policy_Research",
            "Tax_Cooperation",
            "Economic_Indicators",
            "Governance_Standards",
            "Global_Benchmarks",
            "BEPS_Framework",
            "India_Collaboration"
        ],

        "18_FATF": [
            "Financial_Action_Task_Force",
            "Money_Laundering",
            "Terror_Financing",
            "Grey_List",
            "Black_List",
            "Compliance_Standards",
            "Monitoring_Framework",
            "India_Participation"
        ],

        "19_International_Finance_Corporation": [
            "Private_Sector_Development",
            "Investment_Support",
            "Advisory_Services",
            "SME_Finance",
            "Sustainable_Investments",
            "Development_Impact",
            "Emerging_Markets",
            "India_Projects"
        ],

        "20_Multilateral_Development_Banks": [
            "MDB_Concept",
            "Development_Lending",
            "Infrastructure_Financing",
            "Regional_Banks",
            "Global_Financing",
            "Project_Evaluation",
            "Development_Priorities",
            "Institutional_Comparison"
        ],

        "21_International_Debt_Institutions": [
            "Debt_Sustainability",
            "Paris_Club",
            "London_Club",
            "Debt_Restructuring",
            "Debt_Relief",
            "Sovereign_Debt",
            "Financial_Assistance",
            "Global_Coordination"
        ],

        "22_SDG_and_Global_Development_Framework": [
            "Sustainable_Development_Goals",
            "Agenda_2030",
            "Global_Targets",
            "Development_Indicators",
            "Monitoring_Mechanisms",
            "International_Cooperation",
            "Financing_for_Development",
            "India_Progress"
        ],

        "23_Climate_Finance_Institutions": [
            "Green_Climate_Fund",
            "Climate_Adaptation_Funds",
            "Global_Environment_Facility",
            "Climate_Financing",
            "Carbon_Finance",
            "Sustainable_Investments",
            "Developing_Country_Support",
            "India_Access"
        ],

        "24_Regional_Economic_Organizations": [
            "ASEAN",
            "SAARC",
            "BIMSTEC",
            "APEC",
            "Regional_Cooperation",
            "Economic_Integration",
            "Connectivity_Initiatives",
            "India_Relations"
        ],

        "25_India_and_Global_Economic_Institutions": [
            "India_IMF_Relations",
            "India_World_Bank_Relations",
            "India_WTO_Position",
            "India_G20_Role",
            "India_BRICS_Role",
            "Development_Partnerships",
            "Global_Leadership",
            "Strategic_Engagement"
        ],

        "26_Reforms_in_Global_Institutions": [
            "IMF_Reforms",
            "World_Bank_Reforms",
            "WTO_Reforms",
            "Governance_Changes",
            "Representation_Issues",
            "Emerging_Economy_Demands",
            "Institutional_Adaptation",
            "Future_Directions"
        ],

        "27_Current_Affairs_and_Global_Economy": [
            "G20_Developments",
            "IMF_Updates",
            "World_Bank_Reports",
            "WTO_Issues",
            "BRICS_Expansion",
            "Global_Economic_Challenges",
            "International_Summits",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "World_Economic_Outlook",
            "Global_Economic_Prospects",
            "Human_Development_Report",
            "World_Development_Report",
            "Trade_Statistics",
            "Institutional_Reports",
            "PYQ_Themes",
            "Assertion_Reason_Topics"
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

    print(f"Creating International Organizations structure in: {target_base}")

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
    create_international_organizations_structure()