import os
import shutil

def create_industrial_sector_and_msme_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "industrial-sector-and-msme"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Industrial_Economics_Fundamentals": [
            "Meaning_of_Industry",
            "Industrialization",
            "Industrial_Sector_Role",
            "Structural_Transformation",
            "Industrial_Growth",
            "Industrial_Development",
            "Manufacturing_Base",
            "Economic_Importance"
        ],

        "02_Industrial_Development_in_India": [
            "Colonial_Industrialization",
            "Post_Independence_Industry",
            "Industrial_Policy_Evolution",
            "Public_Sector_Led_Growth",
            "Liberalization_Impact",
            "Manufacturing_Expansion",
            "Industrial_Reforms",
            "Growth_Trends"
        ],

        "03_Industrial_Policy_Resolution_1948": [
            "Objectives",
            "Industrial_Categories",
            "Public_Sector_Role",
            "Private_Sector_Role",
            "Strategic_Industries",
            "Regulatory_Framework",
            "Industrial_Direction",
            "Policy_Significance"
        ],

        "04_Industrial_Policy_Resolution_1956": [
            "Socialistic_Pattern",
            "Schedule_A_Industries",
            "Schedule_B_Industries",
            "Schedule_C_Industries",
            "Public_Sector_Expansion",
            "Industrial_Licensing",
            "State_Control",
            "Policy_Impact"
        ],

        "05_Industrial_Licensing_System": [
            "License_Raj",
            "Capacity_Regulation",
            "Industrial_Approvals",
            "Entry_Barriers",
            "Industrial_Control",
            "Administrative_System",
            "Economic_Effects",
            "Abolition_of_Licensing"
        ],

        "06_New_Industrial_Policy_1991": [
            "Delicensing",
            "Liberalization",
            "Privatization",
            "Globalization",
            "Competition",
            "Foreign_Investment",
            "Industrial_Reforms",
            "Economic_Transformation"
        ],

        "07_Public_Sector_Enterprises": [
            "Central_PSEs",
            "State_PSEs",
            "Maharatna",
            "Navratna",
            "Miniratna",
            "Public_Ownership",
            "Strategic_Sectors",
            "Performance_Evaluation"
        ],

        "08_Disinvestment_and_Privatization": [
            "Disinvestment_Policy",
            "Strategic_Sale",
            "Asset_Monetization",
            "Ownership_Transfer",
            "Privatization_Models",
            "Efficiency_Gains",
            "Government_Revenue",
            "Recent_Developments"
        ],

        "09_Industrial_Infrastructure": [
            "Industrial_Parks",
            "Industrial_Corridors",
            "Logistics_Infrastructure",
            "Power_Supply",
            "Transport_Networks",
            "Plug_and_Play_Facilities",
            "Infrastructure_Gaps",
            "Development_Strategies"
        ],

        "10_Industrial_Corridors": [
            "DMIC",
            "CBIC",
            "AKIC",
            "VCIC",
            "Industrial_Clusters",
            "Freight_Corridors",
            "Smart_Industrial_Cities",
            "Regional_Development"
        ],

        "11_Manufacturing_Sector": [
            "Manufacturing_GDP",
            "Factory_Production",
            "Industrial_Output",
            "Value_Addition",
            "Production_Linkages",
            "Supply_Chains",
            "Manufacturing_Competitiveness",
            "Growth_Challenges"
        ],

        "12_Make_in_India": [
            "Policy_Objectives",
            "Target_Sectors",
            "Investment_Promotion",
            "Manufacturing_Expansion",
            "Ease_of_Doing_Business",
            "Job_Creation",
            "Technology_Transfer",
            "Progress_Assessment"
        ],

        "13_MSME_Fundamentals": [
            "MSME_Definition",
            "Classification_Criteria",
            "Micro_Enterprises",
            "Small_Enterprises",
            "Medium_Enterprises",
            "Economic_Contribution",
            "Employment_Generation",
            "Sector_Profile"
        ],

        "14_MSME_Policies_and_Institutions": [
            "MSME_Ministry",
            "MSME_Development_Act",
            "Institutional_Framework",
            "Support_Agencies",
            "Policy_Implementation",
            "Sector_Governance",
            "Promotion_Mechanisms",
            "Reform_Initiatives"
        ],

        "15_MSME_Finance": [
            "Priority_Sector_Lending",
            "Credit_Guarantee_Scheme",
            "MUDRA",
            "Working_Capital",
            "Term_Loans",
            "Credit_Access",
            "Financing_Challenges",
            "Financial_Inclusion"
        ],

        "16_MSME_Competitiveness": [
            "Technology_Upgradation",
            "Productivity",
            "Quality_Certification",
            "Innovation",
            "Skill_Development",
            "Digitalization",
            "Market_Access",
            "Global_Competitiveness"
        ],

        "17_Startups_and_Entrepreneurship": [
            "Startup_India",
            "Entrepreneurship",
            "Innovation_Ecosystem",
            "Incubators",
            "Accelerators",
            "Venture_Support",
            "Business_Development",
            "Startup_Funding"
        ],

        "18_Industrial_Finance_Institutions": [
            "SIDBI",
            "State_Finance_Corporations",
            "Industrial_Finance",
            "Development_Institutions",
            "Credit_Support",
            "Refinance_Schemes",
            "Institutional_Assistance",
            "Sector_Development"
        ],

        "19_Industrial_Labour_and_Skills": [
            "Industrial_Workforce",
            "Labour_Productivity",
            "Skill_India",
            "Apprenticeship",
            "Industrial_Relations",
            "Labour_Reforms",
            "Workforce_Development",
            "Employment_Linkages"
        ],

        "20_Industrial_Clusters": [
            "Cluster_Development",
            "Textile_Clusters",
            "Auto_Clusters",
            "Leather_Clusters",
            "Pharma_Clusters",
            "MSME_Clusters",
            "Agglomeration_Effects",
            "Regional_Specialization"
        ],

        "21_Industrial_Technology_and_Innovation": [
            "Industry_4_0",
            "Automation",
            "Artificial_Intelligence",
            "Robotics",
            "Research_and_Development",
            "Technology_Adoption",
            "Innovation_Policy",
            "Future_Manufacturing"
        ],

        "22_Industrial_Sustainability": [
            "Green_Manufacturing",
            "Energy_Efficiency",
            "Resource_Efficiency",
            "Waste_Management",
            "Circular_Economy",
            "Environmental_Compliance",
            "Sustainable_Industry",
            "ESG_Practices"
        ],

        "23_Production_Linked_Incentive_Scheme": [
            "PLI_Concept",
            "Target_Sectors",
            "Domestic_Manufacturing",
            "Investment_Attraction",
            "Scale_Efficiency",
            "Export_Potential",
            "Implementation_Status",
            "Economic_Impact"
        ],

        "24_Industrial_Disputes_and_Regulation": [
            "Industrial_Disputes",
            "Collective_Bargaining",
            "Labour_Courts",
            "Industrial_Relations_Code",
            "Compliance_Framework",
            "Worker_Welfare",
            "Conflict_Resolution",
            "Industrial_Peace"
        ],

        "25_Ease_of_Doing_Business": [
            "Business_Reforms",
            "Regulatory_Simplification",
            "Single_Window_System",
            "Compliance_Reduction",
            "Investment_Climate",
            "Business_Environment",
            "Reform_Measures",
            "Competitiveness"
        ],

        "26_Industrial_Challenges": [
            "Infrastructure_Gaps",
            "High_Logistics_Costs",
            "Technology_Gap",
            "Credit_Constraints",
            "Import_Dependence",
            "Global_Competition",
            "Low_Productivity",
            "Policy_Challenges"
        ],

        "27_Current_Affairs_and_Industrial_Issues": [
            "PLI_Updates",
            "Manufacturing_Trends",
            "MSME_Developments",
            "Startup_Ecosystem",
            "Industrial_Output_Data",
            "Policy_Reforms",
            "Investment_Announcements",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "IIP_Data",
            "MSME_Statistics",
            "Manufacturing_Data",
            "Industrial_Growth_Rates",
            "Economic_Survey_Industry",
            "Government_Reports",
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

    print(f"Creating Industrial Sector and MSME structure in: {target_base}")

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
    create_industrial_sector_and_msme_structure()