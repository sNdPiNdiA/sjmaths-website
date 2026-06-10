import os
import shutil

def create_oceanography_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "physical-geography",
        "oceanography"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Oceanography_Fundamentals": [
            "Meaning_of_Oceanography",
            "Nature_and_Scope",
            "Branches_of_Oceanography",
            "Importance_of_Oceans",
            "Ocean_Basins",
            "Marine_Environment",
            "Human_Ocean_Interactions",
            "Sources_of_Study"
        ],

        "02_Origin_and_Evolution_of_Oceans": [
            "Origin_of_Oceans",
            "Evolution_of_Oceans",
            "Hydrosphere_Formation",
            "Continental_Drift_and_Oceans",
            "Sea_Floor_Spreading",
            "Ocean_Basin_Evolution",
            "Geological_History",
            "Major_Theories"
        ],

        "03_Distribution_of_Land_and_Water": [
            "Land_Water_Ratio",
            "Northern_Hemisphere",
            "Southern_Hemisphere",
            "Continental_Distribution",
            "Oceanic_Distribution",
            "Global_Patterns",
            "Hemispheric_Contrasts",
            "Geographical_Significance"
        ],

        "04_Ocean_Basins_and_Submarine_Relief": [
            "Continental_Shelf",
            "Continental_Slope",
            "Continental_Rise",
            "Abyssal_Plains",
            "Oceanic_Trenches",
            "Mid_Oceanic_Ridges",
            "Seamounts",
            "Guyots"
        ],

        "05_Pacific_Ocean": [
            "Location_and_Extent",
            "Submarine_Relief",
            "Oceanic_Trenches",
            "Island_Groups",
            "Ocean_Currents",
            "Marine_Resources",
            "Economic_Importance",
            "Geopolitical_Significance"
        ],

        "06_Atlantic_Ocean": [
            "Location_and_Extent",
            "Mid_Atlantic_Ridge",
            "Ocean_Currents",
            "Marine_Resources",
            "Trade_Routes",
            "Economic_Importance",
            "Oceanic_Features",
            "Geopolitical_Role"
        ],

        "07_Indian_Ocean": [
            "Location_and_Extent",
            "Monsoon_Influence",
            "Ocean_Currents",
            "Marine_Resources",
            "Strategic_Importance",
            "Island_Groups",
            "Trade_Routes",
            "Geopolitical_Significance"
        ],

        "08_Arctic_and_Southern_Oceans": [
            "Arctic_Ocean",
            "Southern_Ocean",
            "Polar_Conditions",
            "Sea_Ice",
            "Marine_Ecosystems",
            "Climate_Influence",
            "Resources",
            "Environmental_Concerns"
        ],

        "09_Sea_Floor_Spreading_and_Plate_Tectonics": [
            "Sea_Floor_Spreading",
            "Mid_Oceanic_Ridges",
            "Magnetic_Stripes",
            "Plate_Movements",
            "Ocean_Basin_Formation",
            "Evidence",
            "Geological_Processes",
            "Modern_Theories"
        ],

        "10_Properties_of_Sea_Water": [
            "Temperature",
            "Salinity",
            "Density",
            "Pressure",
            "Chemical_Composition",
            "Physical_Properties",
            "Oceanic_Variations",
            "Significance"
        ],

        "11_Ocean_Temperature": [
            "Horizontal_Distribution",
            "Vertical_Distribution",
            "Thermocline",
            "Factors_Affecting_Temperature",
            "Seasonal_Variation",
            "Latitudinal_Variation",
            "Marine_Climate",
            "Temperature_Profiles"
        ],

        "12_Ocean_Salinity": [
            "Distribution_of_Salinity",
            "Factors_Affecting_Salinity",
            "Evaporation",
            "Precipitation",
            "River_Discharge",
            "Salinity_Patterns",
            "Regional_Variations",
            "Importance"
        ],

        "13_Ocean_Density_and_Pressure": [
            "Density_Variation",
            "Pressure_Changes",
            "Factors_Affecting_Density",
            "Thermohaline_Circulation",
            "Vertical_Structure",
            "Ocean_Dynamics",
            "Deep_Water_Masses",
            "Significance"
        ],

        "14_Ocean_Deposits": [
            "Terrigenous_Deposits",
            "Pelagic_Deposits",
            "Red_Clay",
            "Ooze",
            "Marine_Sediments",
            "Distribution",
            "Formation",
            "Economic_Importance"
        ],

        "15_Waves": [
            "Wave_Formation",
            "Wave_Characteristics",
            "Wave_Motion",
            "Types_of_Waves",
            "Tsunamis",
            "Wave_Energy",
            "Coastal_Impacts",
            "Ocean_Dynamics"
        ],

        "16_Tides": [
            "Origin_of_Tides",
            "Spring_Tides",
            "Neap_Tides",
            "Tidal_Theory",
            "Tidal_Bores",
            "Tidal_Energy",
            "Coastal_Impacts",
            "Applications"
        ],

        "17_Ocean_Currents_Fundamentals": [
            "Meaning_of_Ocean_Currents",
            "Factors_Affecting_Currents",
            "Surface_Currents",
            "Deep_Currents",
            "Ocean_Circulation",
            "Current_Systems",
            "Importance",
            "Global_Patterns"
        ],

        "18_Pacific_Atlantic_and_Indian_Ocean_Currents": [
            "Pacific_Currents",
            "Atlantic_Currents",
            "Indian_Ocean_Currents",
            "Warm_Currents",
            "Cold_Currents",
            "Monsoon_Currents",
            "Current_Interactions",
            "Climate_Influence"
        ],

        "19_El_Nino_La_Nina_and_Ocean_Atmosphere_Interactions": [
            "El_Nino",
            "La_Nina",
            "ENSO",
            "Southern_Oscillation",
            "Ocean_Atmosphere_Coupling",
            "Climate_Impacts",
            "Monsoon_Linkages",
            "Recent_Events"
        ],

        "20_Marine_Ecosystems": [
            "Coral_Reefs",
            "Mangroves",
            "Estuaries",
            "Marine_Biodiversity",
            "Food_Chains",
            "Ocean_Productivity",
            "Threats",
            "Conservation"
        ],

        "21_Marine_Resources": [
            "Fisheries",
            "Mineral_Resources",
            "Petroleum_and_Gas",
            "Polymetallic_Nodules",
            "Marine_Biotechnology",
            "Renewable_Energy",
            "Resource_Utilization",
            "Economic_Importance"
        ],

        "22_Coral_Reefs_and_Mangroves": [
            "Coral_Reef_Formation",
            "Types_of_Coral_Reefs",
            "Mangrove_Ecosystems",
            "Distribution",
            "Ecological_Role",
            "Threats",
            "Conservation",
            "Case_Studies"
        ],

        "23_Coastal_Geomorphology_and_Processes": [
            "Coastal_Erosion",
            "Coastal_Deposition",
            "Beaches",
            "Spits",
            "Bars",
            "Lagoons",
            "Sea_Cliffs",
            "Coastal_Landforms"
        ],

        "24_Sea_Level_Change_and_Coastal_Hazards": [
            "Sea_Level_Rise",
            "Coastal_Flooding",
            "Storm_Surges",
            "Tsunamis",
            "Climate_Change_Impacts",
            "Vulnerability",
            "Adaptation",
            "Risk_Management"
        ],

        "25_Ocean_Governance_and_Law_of_the_Sea": [
            "UNCLOS",
            "Exclusive_Economic_Zone",
            "Continental_Shelf_Rights",
            "Marine_Boundaries",
            "Ocean_Governance",
            "Maritime_Disputes",
            "Blue_Economy",
            "International_Cooperation"
        ],

        "26_Blue_Economy_and_Marine_Policies": [
            "Blue_Economy",
            "Sustainable_Ocean_Use",
            "Marine_Spatial_Planning",
            "Ocean_Resources",
            "Economic_Growth",
            "India_Blue_Economy",
            "Policy_Framework",
            "Future_Prospects"
        ],

        "27_Current_Affairs_and_Ocean_Issues": [
            "Marine_Pollution",
            "Ocean_Warming",
            "Coral_Bleaching",
            "Blue_Economy_Initiatives",
            "Deep_Sea_Mining",
            "Marine_Conservation",
            "Recent_Research",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Ocean_Current_Maps",
            "Ocean_Basin_Maps",
            "Coral_Reef_Maps",
            "Marine_Resource_Maps",
            "Tidal_Maps",
            "Oceanographic_Data",
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

    print(f"Creating Oceanography structure in: {target_base}")

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
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write("[]")
                    print(f"      - Created: {filename}")
                else:
                    print(f"      - Exists: {filename}")

if __name__ == "__main__":
    create_oceanography_structure()