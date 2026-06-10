import os
import shutil

def create_industries_and_transport_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "indian-geography",
        "industries-and-transport"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Industries_and_Transport_Geography_Fundamentals": [
            "Meaning_of_Industry",
            "Meaning_of_Transport",
            "Economic_Importance",
            "Industrialization_in_India",
            "Transport_Networks",
            "Industrial_Geography",
            "Transport_Geography",
            "Sources_of_Study"
        ],

        "02_Factors_Affecting_Industrial_Location": [
            "Raw_Materials",
            "Power",
            "Labour",
            "Capital",
            "Market",
            "Transport_Facilities",
            "Government_Policies",
            "Agglomeration_Economies"
        ],

        "03_Industrialization_in_India": [
            "Historical_Background",
            "Colonial_Industrial_Pattern",
            "Post_Independence_Industrialization",
            "Liberalization_Impact",
            "Industrial_Growth",
            "Regional_Development",
            "Industrial_Policies",
            "Current_Trends"
        ],

        "04_Classification_of_Industries": [
            "Basic_Industries",
            "Consumer_Industries",
            "Heavy_Industries",
            "Light_Industries",
            "Agro_Based_Industries",
            "Mineral_Based_Industries",
            "Ownership_Based_Classification",
            "Classification_Systems"
        ],

        "05_Iron_and_Steel_Industry": [
            "Importance",
            "Raw_Material_Base",
            "Integrated_Steel_Plants",
            "Major_Steel_Centres",
            "Public_Sector_Plants",
            "Private_Sector_Plants",
            "Production_Trends",
            "Challenges"
        ],

        "06_Cotton_Textile_Industry": [
            "Historical_Development",
            "Raw_Material_Availability",
            "Major_Centres",
            "Ahmedabad",
            "Mumbai",
            "Powerloom_Sector",
            "Exports",
            "Challenges"
        ],

        "07_Jute_Textile_Industry": [
            "Raw_Material_Base",
            "Hugli_Belt",
            "Major_Centres",
            "Production",
            "Exports",
            "Competition",
            "Modernization",
            "Challenges"
        ],

        "08_Sugar_Industry": [
            "Sugarcane_Regions",
            "Major_Producing_States",
            "Cooperative_Sector",
            "Production_Trends",
            "Location_Factors",
            "Industrial_Linkages",
            "Exports",
            "Challenges"
        ],

        "09_Cement_Industry": [
            "Raw_Materials",
            "Limestone_Belts",
            "Major_Producing_States",
            "Location_Factors",
            "Production_Trends",
            "Infrastructure_Linkages",
            "Exports",
            "Challenges"
        ],

        "10_Petrochemical_Industry": [
            "Raw_Material_Base",
            "Refinery_Linkages",
            "Major_Complexes",
            "Downstream_Industries",
            "Production",
            "Industrial_Corridors",
            "Exports",
            "Future_Prospects"
        ],

        "11_Automobile_Industry": [
            "Major_Hubs",
            "Chennai",
            "Pune",
            "Gurugram_Manesar",
            "Electric_Vehicles",
            "Production_Trends",
            "Exports",
            "Industrial_Clusters"
        ],

        "12_Information_Technology_Industry": [
            "Software_Industry",
            "IT_Hubs",
            "Bengaluru",
            "Hyderabad",
            "Pune",
            "Digital_Economy",
            "Exports",
            "Emerging_Trends"
        ],

        "13_Chemical_and_Fertilizer_Industry": [
            "Chemical_Industry",
            "Fertilizer_Industry",
            "Raw_Material_Base",
            "Major_Centres",
            "Production_Trends",
            "Industrial_Linkages",
            "Environmental_Issues",
            "Challenges"
        ],

        "14_Pharmaceutical_Industry": [
            "Major_Clusters",
            "Hyderabad",
            "Ahmedabad",
            "Mumbai",
            "Generic_Medicines",
            "Exports",
            "Research_and_Development",
            "Global_Position"
        ],

        "15_Food_Processing_Industry": [
            "Agro_Based_Processing",
            "Dairy_Industry",
            "Meat_Processing",
            "Marine_Products",
            "Food_Parks",
            "Value_Addition",
            "Exports",
            "Challenges"
        ],

        "16_MSMEs_and_Cottage_Industries": [
            "MSME_Sector",
            "Village_Industries",
            "Khadi_and_Village_Industries",
            "Employment_Generation",
            "Industrial_Clusters",
            "Government_Support",
            "Challenges",
            "Future_Prospects"
        ],

        "17_Industrial_Regions_of_India": [
            "Mumbai_Pune_Region",
            "Hugli_Region",
            "Ahmedabad_Vadodara_Region",
            "Chotanagpur_Region",
            "Bengaluru_Chennai_Region",
            "National_Capital_Region",
            "Industrial_Clusters",
            "Regional_Characteristics"
        ],

        "18_Industrial_Corridors": [
            "Delhi_Mumbai_Industrial_Corridor",
            "Chennai_Bengaluru_Corridor",
            "Amritsar_Kolkata_Corridor",
            "East_Coast_Corridor",
            "Industrial_Nodes",
            "Logistics_Hubs",
            "Infrastructure_Development",
            "Economic_Impact"
        ],

        "19_Industrial_Policies_and_Reforms": [
            "Industrial_Policy_Resolution",
            "Liberalization",
            "Make_in_India",
            "Production_Linked_Incentives",
            "FDI_Policy",
            "Ease_of_Doing_Business",
            "Policy_Reforms",
            "Future_Directions"
        ],

        "20_Transport_Geography_Fundamentals": [
            "Meaning_of_Transport",
            "Modes_of_Transport",
            "Transport_Networks",
            "Economic_Importance",
            "Connectivity",
            "Regional_Development",
            "Transport_Corridors",
            "Geographical_Patterns"
        ],

        "21_Road_Transport": [
            "National_Highways",
            "Expressways",
            "State_Highways",
            "Rural_Roads",
            "Bharatmala_Project",
            "Road_Density",
            "Freight_Transport",
            "Challenges"
        ],

        "22_Rail_Transport": [
            "Indian_Railways",
            "Railway_Zones",
            "Freight_Corridors",
            "High_Speed_Rail",
            "Metro_Rail",
            "Rail_Network",
            "Modernization",
            "Challenges"
        ],

        "23_Water_Transport": [
            "Inland_Waterways",
            "National_Waterways",
            "River_Transport",
            "Coastal_Shipping",
            "Waterway_Development",
            "Cargo_Movement",
            "Economic_Advantages",
            "Challenges"
        ],

        "24_Major_Ports_of_India": [
            "Mumbai_Port",
            "JNPT",
            "Kandla_Port",
            "Chennai_Port",
            "Visakhapatnam_Port",
            "Paradip_Port",
            "Port_Development",
            "Sagarmala"
        ],

        "25_Air_Transport": [
            "Airport_Network",
            "Major_Airports",
            "International_Airports",
            "Regional_Connectivity_Scheme",
            "UDAN",
            "Cargo_Transport",
            "Aviation_Growth",
            "Challenges"
        ],

        "26_Logistics_and_Multimodal_Transport": [
            "Logistics_Sector",
            "Multimodal_Transport",
            "Freight_Corridors",
            "Logistics_Parks",
            "Supply_Chains",
            "PM_Gati_Shakti",
            "Infrastructure_Integration",
            "Economic_Impact"
        ],

        "27_Transport_Policies_and_Current_Affairs": [
            "National_Logistics_Policy",
            "PM_Gati_Shakti",
            "Bharatmala",
            "Sagarmala",
            "Dedicated_Freight_Corridors",
            "High_Speed_Rail_Projects",
            "Recent_Policy_Changes",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Industrial_Region_Maps",
            "Industrial_Corridor_Maps",
            "Port_Maps",
            "Railway_Maps",
            "Highway_Maps",
            "Transport_Data",
            "Map_Based_Questions",
            "PYQ_Themes"
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

    print(f"Creating Industries and Transport structure in: {target_base}")
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
    create_industries_and_transport_structure()