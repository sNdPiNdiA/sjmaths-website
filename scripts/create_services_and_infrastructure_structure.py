import os
import shutil

def create_services_and_infrastructure_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "economy",
        "indian-economy",
        "services-and-infrastructure"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Services_Sector_Fundamentals": [
            "Meaning_of_Services_Sector",
            "Characteristics_of_Services",
            "Service_Economy",
            "Tertiary_Sector",
            "Structural_Transformation",
            "Contribution_to_GDP",
            "Employment_Generation",
            "Economic_Importance"
        ],

        "02_Evolution_of_Service_Sector_in_India": [
            "Post_Independence_Development",
            "Liberalization_Impact",
            "Service_Led_Growth",
            "Economic_Reforms",
            "Sectoral_Expansion",
            "Growth_Patterns",
            "Global_Integration",
            "Current_Trends"
        ],

        "03_Service_Sector_Composition": [
            "Trade_Services",
            "Transport_Services",
            "Communication_Services",
            "Financial_Services",
            "Professional_Services",
            "Tourism_Services",
            "Public_Services",
            "Digital_Services"
        ],

        "04_Information_Technology_Sector": [
            "IT_Industry",
            "Software_Services",
            "IT_Exports",
            "Technology_Parks",
            "Software_Development",
            "Digital_Economy",
            "Innovation_Ecosystem",
            "Global_Competitiveness"
        ],

        "05_ITeS_and_BPO_Industry": [
            "Business_Process_Outsourcing",
            "Knowledge_Process_Outsourcing",
            "Shared_Service_Centers",
            "Global_Capability_Centers",
            "Outsourcing_Model",
            "Employment_Impact",
            "Export_Revenue",
            "Future_Trends"
        ],

        "06_Digital_Economy": [
            "Digital_Transformation",
            "Digital_Public_Infrastructure",
            "Platform_Economy",
            "Data_Economy",
            "Digital_Inclusion",
            "Digital_Governance",
            "Innovation_Platforms",
            "Economic_Impact"
        ],

        "07_E_Commerce": [
            "Online_Retail",
            "Marketplace_Model",
            "Inventory_Model",
            "Digital_Marketplaces",
            "Consumer_Commerce",
            "Business_Commerce",
            "E_Commerce_Regulation",
            "Growth_Trends"
        ],

        "08_Telecommunications": [
            "Telecom_Sector",
            "Mobile_Networks",
            "Broadband_Services",
            "Internet_Penetration",
            "Spectrum_Management",
            "Telecom_Infrastructure",
            "5G_Technology",
            "Sector_Challenges"
        ],

        "09_Tourism_Industry": [
            "Domestic_Tourism",
            "International_Tourism",
            "Cultural_Tourism",
            "Eco_Tourism",
            "Medical_Tourism",
            "Religious_Tourism",
            "Tourism_Infrastructure",
            "Economic_Contribution"
        ],

        "10_Hospitality_Sector": [
            "Hotels",
            "Restaurants",
            "Travel_Services",
            "Accommodation_Industry",
            "Hospitality_Management",
            "Service_Standards",
            "Employment_Generation",
            "Industry_Trends"
        ],

        "11_Healthcare_Services": [
            "Healthcare_Industry",
            "Hospitals",
            "Medical_Services",
            "Health_Infrastructure",
            "Private_Healthcare",
            "Public_Healthcare",
            "Telemedicine",
            "Health_Economy"
        ],

        "12_Education_Services": [
            "Education_Industry",
            "Higher_Education",
            "Skill_Development",
            "EdTech",
            "Vocational_Training",
            "Digital_Learning",
            "Human_Capital",
            "Knowledge_Economy"
        ],

        "13_Logistics_Sector": [
            "Logistics_Industry",
            "Supply_Chain_Management",
            "Warehousing",
            "Freight_Movement",
            "Distribution_Networks",
            "Logistics_Costs",
            "Multimodal_Logistics",
            "Sector_Reforms"
        ],

        "14_Road_Infrastructure": [
            "National_Highways",
            "Expressways",
            "Rural_Roads",
            "Bharatmala_Programme",
            "Road_Connectivity",
            "Transport_Efficiency",
            "PPP_Projects",
            "Infrastructure_Development"
        ],

        "15_Railway_Infrastructure": [
            "Indian_Railways",
            "Dedicated_Freight_Corridors",
            "High_Speed_Rail",
            "Rail_Modernization",
            "Passenger_Network",
            "Freight_Transport",
            "Station_Redevelopment",
            "Railway_Reforms"
        ],

        "16_Aviation_Infrastructure": [
            "Civil_Aviation",
            "Airports",
            "Regional_Connectivity",
            "UDAN_Scheme",
            "Air_Cargo",
            "Airport_Modernization",
            "Aviation_Growth",
            "Sector_Challenges"
        ],

        "17_Port_and_Shipping_Infrastructure": [
            "Major_Ports",
            "Minor_Ports",
            "Sagarmala_Programme",
            "Shipping_Industry",
            "Maritime_Logistics",
            "Port_Modernization",
            "Coastal_Shipping",
            "Blue_Economy_Linkages"
        ],

        "18_Urban_Infrastructure": [
            "Smart_Cities",
            "Urban_Transport",
            "Water_Supply",
            "Sanitation",
            "Waste_Management",
            "Urban_Planning",
            "Municipal_Infrastructure",
            "Urban_Development"
        ],

        "19_Rural_Infrastructure": [
            "Rural_Connectivity",
            "Village_Infrastructure",
            "Rural_Housing",
            "Rural_Electrification",
            "Digital_Villages",
            "Water_Access",
            "Rural_Development",
            "Infrastructure_Gaps"
        ],

        "20_Energy_Infrastructure": [
            "Power_Transmission",
            "Power_Distribution",
            "Grid_Infrastructure",
            "Renewable_Energy_Integration",
            "Energy_Access",
            "Infrastructure_Expansion",
            "Power_Reliability",
            "Energy_Security"
        ],

        "21_Digital_Infrastructure": [
            "BharatNet",
            "Data_Centers",
            "Cloud_Infrastructure",
            "Digital_Connectivity",
            "Cyber_Infrastructure",
            "Internet_Backbone",
            "Digital_Public_Goods",
            "Technology_Platforms"
        ],

        "22_Public_Private_Partnerships": [
            "PPP_Model",
            "BOT_Model",
            "HAM_Model",
            "Infrastructure_Financing",
            "Risk_Sharing",
            "Project_Implementation",
            "Private_Investment",
            "PPP_Challenges"
        ],

        "23_Infrastructure_Financing": [
            "Infrastructure_Funds",
            "Development_Finance",
            "InvITs",
            "Infrastructure_Bonds",
            "Project_Finance",
            "Long_Term_Capital",
            "Funding_Gaps",
            "Financial_Mechanisms"
        ],

        "24_Gati_Shakti_and_Integrated_Planning": [
            "PM_Gati_Shakti",
            "Multimodal_Connectivity",
            "Integrated_Infrastructure",
            "Logistics_Efficiency",
            "Infrastructure_Mapping",
            "Project_Coordination",
            "Network_Planning",
            "Economic_Benefits"
        ],

        "25_Service_Sector_Competitiveness": [
            "Global_Service_Exports",
            "Productivity",
            "Innovation",
            "Skill_Advantage",
            "Quality_Standards",
            "Digital_Capabilities",
            "Competitive_Strengths",
            "Future_Opportunities"
        ],

        "26_Infrastructure_Challenges": [
            "Financing_Gaps",
            "Land_Acquisition",
            "Project_Delays",
            "Regulatory_Bottlenecks",
            "Maintenance_Issues",
            "Capacity_Constraints",
            "Urbanization_Pressures",
            "Sustainability_Concerns"
        ],

        "27_Current_Affairs_and_Sector_Updates": [
            "Digital_Economy_Updates",
            "Infrastructure_Projects",
            "Telecom_Developments",
            "Tourism_Trends",
            "Logistics_Reforms",
            "Smart_City_Progress",
            "Recent_Policies",
            "UPSC_High_Yield_Topics"
        ],

        "28_Reports_Data_and_Exam_Themes": [
            "Service_Sector_Data",
            "Infrastructure_Statistics",
            "Logistics_Index",
            "Digital_Economy_Data",
            "Economic_Survey_Services",
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

    print(f"Creating Services and Infrastructure structure in: {target_base}")

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
    create_services_and_infrastructure_structure()