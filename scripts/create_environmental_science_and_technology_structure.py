import os
import shutil

def create_environmental_science_and_technology_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "environmental-science-and-technology"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Environmental_Science_Fundamentals": [
            "Scope_of_Environmental_Science",
            "Interdisciplinary_Nature",
            "Environmental_Systems",
            "Human_Environment_Interaction",
            "Environmental_Challenges",
            "Scientific_Approach",
            "Environmental_Indicators",
            "Sustainability_Linkages"
        ],

        "02_Environmental_Biotechnology": [
            "Environmental_Biotechnology_Concept",
            "Biological_Processes",
            "Biotechnology_Applications",
            "Bioremediation",
            "Bioaugmentation",
            "Biosensors",
            "Environmental_Benefits",
            "Future_Prospects"
        ],

        "03_Genetic_Engineering_and_Environment": [
            "Genetic_Engineering",
            "Recombinant_DNA_Technology",
            "Gene_Editing",
            "CRISPR_Technology",
            "Environmental_Applications",
            "Risk_Assessment",
            "Regulatory_Framework",
            "Ethical_Issues"
        ],

        "04_Genetically_Modified_Crops": [
            "GM_Crop_Concept",
            "Bt_Cotton",
            "Golden_Rice",
            "GM_Mustard",
            "Advantages_of_GM_Crops",
            "Environmental_Concerns",
            "Biosafety_Issues",
            "Indian_Regulatory_Framework"
        ],

        "05_Biofertilizers_and_Biopesticides": [
            "Biofertilizers",
            "Nitrogen_Fixing_Bacteria",
            "Mycorrhiza",
            "Biopesticides",
            "Biological_Pest_Control",
            "Sustainable_Agriculture",
            "Advantages",
            "Limitations"
        ],

        "06_Biofuels": [
            "First_Generation_Biofuels",
            "Second_Generation_Biofuels",
            "Third_Generation_Biofuels",
            "Ethanol_Blending",
            "Biodiesel",
            "Sustainable_Aviation_Fuel",
            "National_Biofuel_Policy",
            "Environmental_Impacts"
        ],

        "07_Hydrogen_Economy": [
            "Hydrogen_Fuel",
            "Green_Hydrogen",
            "Blue_Hydrogen",
            "Grey_Hydrogen",
            "Hydrogen_Production",
            "Storage_and_Transport",
            "National_Green_Hydrogen_Mission",
            "Challenges_and_Prospects"
        ],

        "08_Renewable_Energy_Technologies": [
            "Solar_Energy",
            "Wind_Energy",
            "Hydropower",
            "Biomass_Energy",
            "Geothermal_Energy",
            "Ocean_Energy",
            "Hybrid_Energy_Systems",
            "Technology_Trends"
        ],

        "09_Energy_Storage_Technologies": [
            "Battery_Technologies",
            "Lithium_Ion_Batteries",
            "Sodium_Ion_Batteries",
            "Flow_Batteries",
            "Hydrogen_Storage",
            "Pumped_Hydro_Storage",
            "Grid_Storage",
            "Future_Developments"
        ],

        "10_Carbon_Capture_and_Storage": [
            "Carbon_Capture",
            "Carbon_Utilization",
            "Carbon_Storage",
            "Direct_Air_Capture",
            "Carbon_Sequestration",
            "Industrial_Applications",
            "Climate_Relevance",
            "Challenges"
        ],

        "11_Waste_to_Energy_Technologies": [
            "Waste_to_Energy_Concept",
            "Incineration",
            "Pyrolysis",
            "Gasification",
            "Anaerobic_Digestion",
            "Biogas_Production",
            "Refuse_Derived_Fuel",
            "Environmental_Considerations"
        ],

        "12_Solid_Waste_Management_Technologies": [
            "Waste_Segregation",
            "Recycling_Technologies",
            "Composting",
            "Vermicomposting",
            "Material_Recovery_Facilities",
            "Landfill_Engineering",
            "Smart_Waste_Management",
            "Emerging_Technologies"
        ],

        "13_Wastewater_Treatment_Technologies": [
            "Primary_Treatment",
            "Secondary_Treatment",
            "Tertiary_Treatment",
            "Activated_Sludge_Process",
            "Membrane_Technologies",
            "Industrial_Effluent_Treatment",
            "Water_Recycling",
            "Zero_Liquid_Discharge"
        ],

        "14_Air_Pollution_Control_Technologies": [
            "Electrostatic_Precipitators",
            "Cyclone_Separators",
            "Bag_Filters",
            "Scrubbers",
            "Catalytic_Converters",
            "Flue_Gas_Desulfurization",
            "Emission_Control",
            "Monitoring_Systems"
        ],

        "15_Environmental_Monitoring_Technologies": [
            "Environmental_Sensors",
            "Remote_Sensing",
            "GIS_Applications",
            "Satellite_Monitoring",
            "Air_Quality_Monitoring",
            "Water_Quality_Monitoring",
            "Real_Time_Data_Systems",
            "Decision_Support_Tools"
        ],

        "16_Green_Building_and_Sustainable_Infrastructure": [
            "Green_Building_Concept",
            "Energy_Efficient_Design",
            "Green_Materials",
            "Water_Efficiency",
            "LEED_Certification",
            "GRIHA_Rating",
            "Smart_Infrastructure",
            "Sustainable_Urban_Design"
        ],

        "17_Geoengineering_and_Climate_Technologies": [
            "Geoengineering_Concept",
            "Solar_Radiation_Management",
            "Carbon_Dioxide_Removal",
            "Ocean_Fertilization",
            "Weather_Modification",
            "Climate_Intervention",
            "Risks_and_Ethics",
            "Policy_Debates"
        ],

        "18_Green_Transportation_Technologies": [
            "Electric_Vehicles",
            "Fuel_Cell_Vehicles",
            "Hybrid_Vehicles",
            "Battery_Swapping",
            "Sustainable_Mobility",
            "Charging_Infrastructure",
            "Alternative_Fuels",
            "Environmental_Benefits"
        ],

        "19_Emerging_Environmental_Technologies": [
            "Artificial_Intelligence_in_Environment",
            "Internet_of_Things",
            "Digital_Twins",
            "Blockchain_for_Sustainability",
            "Nanotechnology",
            "Green_Chemistry",
            "Nature_Based_Technologies",
            "Future_Innovations"
        ],

        "20_Current_Affairs_and_Environmental_Technology": [
            "Recent_Green_Technologies",
            "Green_Hydrogen_Developments",
            "Renewable_Energy_Updates",
            "Carbon_Capture_Projects",
            "EV_Policy_Developments",
            "Waste_Management_Innovations",
            "Scientific_Breakthroughs",
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

    print(f"Creating Environmental Science and Technology structure in: {target_base}")

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
    create_environmental_science_and_technology_structure()