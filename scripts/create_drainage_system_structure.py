import os
import shutil

def create_drainage_system_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography", "drainage-system")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Drainage_System_Fundamentals": [
            "Meaning_of_Drainage",
            "Drainage_Basin",
            "Watershed",
            "Drainage_Patterns",
            "River_System",
            "Importance_of_Rivers",
            "Drainage_Characteristics_of_India",
            "Sources_of_Study"
        ],

        "02_Evolution_of_Indian_Drainage": [
            "Geological_History",
            "River_Capture",
            "Antecedent_Drainage",
            "Consequent_Drainage",
            "Superimposed_Drainage",
            "Drainage_Evolution_Theories",
            "Tectonic_Influences",
            "Historical_Changes"
        ],

        "03_Drainage_Patterns_of_India": [
            "Dendritic",
            "Trellis",
            "Radial",
            "Rectangular",
            "Parallel",
            "Centripetal",
            "Annular",
            "Pattern_Distribution"
        ],

        "04_Himalayan_River_System_Overview": [
            "Characteristics",
            "Perennial_Rivers",
            "Youthful_Stage",
            "Sediment_Load",
            "Flood_Plains",
            "Drainage_Features",
            "Economic_Importance",
            "Comparative_Features"
        ],

        "05_Indus_River_System": [
            "Indus_River",
            "Jhelum",
            "Chenab",
            "Ravi",
            "Beas",
            "Sutlej",
            "Indus_Waters_Treaty",
            "Basin_Characteristics"
        ],

        "06_Ganga_River_System": [
            "Ganga_Origin",
            "Bhagirathi",
            "Alaknanda",
            "Upper_Ganga",
            "Middle_Ganga",
            "Lower_Ganga",
            "Ganga_Basin",
            "River_Characteristics"
        ],

        "07_Ganga_Tributaries": [
            "Yamuna",
            "Ghaghara",
            "Gandak",
            "Kosi",
            "Son",
            "Ramganga",
            "Major_Tributaries",
            "Basin_Contribution"
        ],

        "08_Brahmaputra_River_System": [
            "Tsangpo",
            "Dihang",
            "Assam_Valley",
            "Major_Tributaries",
            "River_Islands",
            "Braided_Channel",
            "Floods",
            "Basin_Characteristics"
        ],

        "09_Northern_Plains_and_Rivers": [
            "Alluvial_Plains",
            "Meanders",
            "Oxbow_Lakes",
            "Natural_Levees",
            "Flood_Plains",
            "River_Deposition",
            "Channel_Shifts",
            "Geomorphic_Features"
        ],

        "10_Peninsular_River_System_Overview": [
            "Characteristics",
            "Seasonal_Rivers",
            "Mature_Stage",
            "Hard_Rock_Terrain",
            "East_Flowing_Rivers",
            "West_Flowing_Rivers",
            "Drainage_Features",
            "Comparative_Analysis"
        ],

        "11_Godavari_River_System": [
            "Origin",
            "Tributaries",
            "Basin_Area",
            "Delta",
            "Irrigation_Importance",
            "River_Projects",
            "Economic_Importance",
            "River_Characteristics"
        ],

        "12_Krishna_River_System": [
            "Origin",
            "Bhima",
            "Tungabhadra",
            "Tributaries",
            "Delta",
            "River_Projects",
            "Basin_Features",
            "Economic_Importance"
        ],

        "13_Kaveri_River_System": [
            "Origin",
            "Tributaries",
            "Delta",
            "Water_Disputes",
            "River_Projects",
            "Agricultural_Importance",
            "Basin_Characteristics",
            "Economic_Role"
        ],

        "14_Mahanadi_and_Pennar_Systems": [
            "Mahanadi",
            "Pennar",
            "Subarnarekha",
            "Brahmani",
            "Baitarani",
            "East_Flowing_Rivers",
            "Delta_Formation",
            "Regional_Importance"
        ],

        "15_Narmada_and_Tapi_Systems": [
            "Narmada",
            "Tapi",
            "Rift_Valley",
            "Estuaries",
            "West_Flowing_Rivers",
            "Tributaries",
            "River_Projects",
            "Geomorphic_Significance"
        ],

        "16_Western_Coastal_Rivers": [
            "Short_Rivers",
            "Mandovi",
            "Zuari",
            "Periyar",
            "Sharavathi",
            "Fast_Flowing_Rivers",
            "Hydropower_Potential",
            "Regional_Importance"
        ],

        "17_Inland_Drainage": [
            "Luni",
            "Sambhar_Basin",
            "Desert_Drainage",
            "Ephemeral_Streams",
            "Endorheic_Basins",
            "Arid_Region_Drainage",
            "Drainage_Characteristics",
            "Regional_Importance"
        ],

        "18_Lakes_of_India": [
            "Natural_Lakes",
            "Artificial_Lakes",
            "Freshwater_Lakes",
            "Saltwater_Lakes",
            "Tectonic_Lakes",
            "Glacial_Lakes",
            "Lagoon_Lakes",
            "Lake_Classification"
        ],

        "19_Important_Lakes_and_Lagoons": [
            "Wular",
            "Dal",
            "Chilika",
            "Pulicat",
            "Loktak",
            "Sambhar",
            "Vembanad",
            "Regional_Features"
        ],

        "20_Wetlands_of_India": [
            "Wetland_Ecosystems",
            "Ramsar_Sites",
            "Marshes",
            "Mangrove_Wetlands",
            "Floodplain_Wetlands",
            "Conservation",
            "Biodiversity",
            "Ecological_Importance"
        ],

        "21_River_Deltas_and_Estuaries": [
            "Delta_Formation",
            "Ganga_Brahmaputra_Delta",
            "Mahanadi_Delta",
            "Godavari_Delta",
            "Krishna_Delta",
            "Kaveri_Delta",
            "Estuarine_Systems",
            "Comparative_Features"
        ],

        "22_River_Projects_and_Multipurpose_Projects": [
            "Bhakra_Nangal",
            "Hirakud",
            "Damodar_Valley",
            "Nagarjuna_Sagar",
            "Sardar_Sarovar",
            "Tehri",
            "Multipurpose_Projects",
            "Benefits_and_Issues"
        ],

        "23_Water_Resources_and_Management": [
            "Surface_Water",
            "Groundwater",
            "Water_Conservation",
            "Watershed_Management",
            "Rainwater_Harvesting",
            "Water_Use_Efficiency",
            "Water_Policies",
            "Resource_Management"
        ],

        "24_Interlinking_of_Rivers": [
            "National_River_Linking_Project",
            "Himalayan_Component",
            "Peninsular_Component",
            "Benefits",
            "Challenges",
            "Environmental_Issues",
            "Economic_Implications",
            "Policy_Debates"
        ],

        "25_River_Disputes_and_Governance": [
            "Kaveri_Dispute",
            "Krishna_Dispute",
            "Ravi_Beas_Dispute",
            "Inter_State_Water_Issues",
            "River_Boards",
            "Tribunals",
            "Water_Governance",
            "Policy_Framework"
        ],

        "26_Drainage_and_Environment": [
            "River_Pollution",
            "Ganga_Cleaning",
            "Wetland_Degradation",
            "Sand_Mining",
            "Flow_Regulation",
            "Biodiversity_Threats",
            "Environmental_Management",
            "Conservation_Strategies"
        ],

        "27_Floods_Droughts_and_River_Hazards": [
            "Riverine_Floods",
            "Flash_Floods",
            "Bank_Erosion",
            "Channel_Shifts",
            "Drought_and_Rivers",
            "Flood_Control",
            "Disaster_Management",
            "Case_Studies"
        ],

        "28_Maps_Current_Affairs_and_UPSC_Themes": [
            "River_Map_Work",
            "Tributary_Mapping",
            "Lake_Locations",
            "Wetland_Locations",
            "Recent_Water_Disputes",
            "Current_Affairs",
            "PYQ_Themes",
            "Map_Based_Questions"
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

    print(f"Creating Drainage System structure in: {target_base}")
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
    create_drainage_system_structure()