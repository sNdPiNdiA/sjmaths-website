import os
import shutil

def create_geomorphology_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "physical-geography",
        "geomorphology"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Geomorphology_Fundamentals": [
            "Meaning_of_Geomorphology",
            "Nature_and_Scope",
            "Landforms",
            "Relief_Features",
            "Geomorphic_Processes",
            "Evolution_of_Landforms",
            "Importance_of_Geomorphology",
            "Sources_of_Study"
        ],

        "02_Origin_and_Evolution_of_Earth": [
            "Big_Bang_Theory",
            "Nebular_Hypothesis",
            "Origin_of_Earth",
            "Internal_Structure",
            "Geological_Time_Scale",
            "Earth_Evolution",
            "Crust_Formation",
            "Major_Eras"
        ],

        "03_Internal_Structure_of_Earth": [
            "Crust",
            "Mantle",
            "Core",
            "Discontinuities",
            "Lithosphere",
            "Asthenosphere",
            "Seismic_Evidence",
            "Earth_Layers"
        ],

        "04_Rocks_and_Rock_Cycle": [
            "Igneous_Rocks",
            "Sedimentary_Rocks",
            "Metamorphic_Rocks",
            "Rock_Cycle",
            "Rock_Characteristics",
            "Rock_Classification",
            "Mineral_Composition",
            "Economic_Importance"
        ],

        "05_Plate_Tectonics": [
            "Continental_Drift",
            "Sea_Floor_Spreading",
            "Plate_Boundaries",
            "Convergent_Boundary",
            "Divergent_Boundary",
            "Transform_Boundary",
            "Plate_Movements",
            "Evidence_of_Plate_Tectonics"
        ],

        "06_Endogenetic_Forces": [
            "Diastrophism",
            "Orogeny",
            "Epeirogeny",
            "Crustal_Movements",
            "Mountain_Building",
            "Continental_Uplift",
            "Internal_Forces",
            "Landform_Development"
        ],

        "07_Volcanism": [
            "Volcanoes",
            "Volcanic_Eruptions",
            "Types_of_Volcanoes",
            "Volcanic_Landforms",
            "Lava_Plateaus",
            "Volcanic_Hazards",
            "Distribution_of_Volcanoes",
            "Economic_Importance"
        ],

        "08_Earthquakes": [
            "Earthquake_Origin",
            "Seismic_Waves",
            "Focus_and_Epicentre",
            "Earthquake_Zones",
            "Measurement_Scales",
            "Effects_of_Earthquakes",
            "Prediction_and_Mitigation",
            "Disaster_Management"
        ],

        "09_Weathering": [
            "Mechanical_Weathering",
            "Chemical_Weathering",
            "Biological_Weathering",
            "Weathering_Processes",
            "Factors_Affecting_Weathering",
            "Products_of_Weathering",
            "Regolith",
            "Geomorphic_Importance"
        ],

        "10_Mass_Movements": [
            "Landslides",
            "Rockfalls",
            "Soil_Creep",
            "Mudflows",
            "Slumping",
            "Avalanches",
            "Causes_of_Mass_Movement",
            "Mitigation_Measures"
        ],

        "11_Cycle_of_Erosion": [
            "Davisian_Cycle",
            "Youth_Stage",
            "Mature_Stage",
            "Old_Age_Stage",
            "Peneplain",
            "Criticism_of_Davis",
            "Modern_Concepts",
            "Geomorphic_Cycles"
        ],

        "12_Fluvial_Geomorphology": [
            "River_Erosion",
            "Transportation",
            "Deposition",
            "River_Valleys",
            "Waterfalls",
            "Flood_Plains",
            "Meanders",
            "Deltas"
        ],

        "13_Glaciers_and_Glacial_Landforms": [
            "Valley_Glaciers",
            "Continental_Glaciers",
            "Cirques",
            "Aretes",
            "Moraines",
            "Drumlins",
            "Glacial_Erosion",
            "Glacial_Deposition"
        ],

        "14_Aeolian_Landforms": [
            "Wind_Erosion",
            "Deflation",
            "Abrasion",
            "Sand_Dunes",
            "Loess",
            "Desert_Landforms",
            "Yardangs",
            "Zeugens"
        ],

        "15_Karst_Topography": [
            "Limestone_Regions",
            "Sinkholes",
            "Dolines",
            "Uvalas",
            "Poljes",
            "Caves",
            "Stalactites",
            "Stalagmites"
        ],

        "16_Coastal_Geomorphology": [
            "Wave_Erosion",
            "Sea_Cliffs",
            "Sea_Caves",
            "Sea_Arches",
            "Beaches",
            "Spits",
            "Lagoons",
            "Coastal_Deposition"
        ],

        "17_Ocean_Floor_Topography": [
            "Continental_Shelf",
            "Continental_Slope",
            "Abyssal_Plains",
            "Oceanic_Trenches",
            "Mid_Oceanic_Ridges",
            "Seamounts",
            "Guyots",
            "Ocean_Basins"
        ],

        "18_Mountain_Landforms": [
            "Fold_Mountains",
            "Block_Mountains",
            "Volcanic_Mountains",
            "Residual_Mountains",
            "Mountain_Building",
            "Major_Mountain_Systems",
            "Geomorphic_Significance",
            "Examples"
        ],

        "19_Plains_and_Plateaus": [
            "Structural_Plains",
            "Erosional_Plains",
            "Depositional_Plains",
            "Intermontane_Plateaus",
            "Volcanic_Plateaus",
            "Dissected_Plateaus",
            "Major_Examples",
            "Economic_Importance"
        ],

        "20_Geomorphic_Processes_and_Landform_Evolution": [
            "Denudation",
            "Gradation",
            "Aggradation",
            "Degradation",
            "Dynamic_Equilibrium",
            "Landscape_Evolution",
            "Process_Response_System",
            "Modern_Approaches"
        ],

        "21_Indian_Geomorphology": [
            "Himalayas",
            "Northern_Plains",
            "Peninsular_Plateau",
            "Indian_Desert",
            "Coastal_Plains",
            "Islands_of_India",
            "Relief_Features",
            "Geomorphic_Evolution"
        ],

        "22_Seismology_and_Volcanic_Belts": [
            "Ring_of_Fire",
            "Earthquake_Belts",
            "Volcanic_Belts",
            "Indian_Seismic_Zones",
            "Plate_Margins",
            "Hazard_Zones",
            "Global_Distribution",
            "Recent_Events"
        ],

        "23_Applied_Geomorphology": [
            "Engineering_Geomorphology",
            "Environmental_Geomorphology",
            "Urban_Geomorphology",
            "Resource_Management",
            "Hazard_Assessment",
            "Watershed_Management",
            "Land_Use_Planning",
            "Applications"
        ],

        "24_Remote_Sensing_and_GIS_in_Geomorphology": [
            "Satellite_Imagery",
            "Digital_Elevation_Models",
            "Terrain_Analysis",
            "Landform_Mapping",
            "GIS_Applications",
            "Geomorphic_Studies",
            "Data_Interpretation",
            "Modern_Techniques"
        ],

        "25_Geomorphic_Hazards": [
            "Earthquakes",
            "Volcanoes",
            "Landslides",
            "Tsunamis",
            "Coastal_Erosion",
            "Desertification",
            "Risk_Assessment",
            "Mitigation"
        ],

        "26_Climate_and_Geomorphology": [
            "Climatic_Geomorphology",
            "Periglacial_Processes",
            "Arid_Geomorphology",
            "Humid_Geomorphology",
            "Climate_Change_Impacts",
            "Weathering_Rates",
            "Landscape_Response",
            "Case_Studies"
        ],

        "27_Current_Affairs_and_Geomorphic_Issues": [
            "Recent_Earthquakes",
            "Volcanic_Eruptions",
            "Landslide_Events",
            "Tsunami_Studies",
            "Climate_Geomorphology",
            "Geological_Hazards",
            "Recent_Research",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Relief_Maps",
            "Plate_Boundary_Maps",
            "Earthquake_Maps",
            "Volcano_Maps",
            "Landform_Maps",
            "Geomorphic_Data",
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

    print(f"Creating Geomorphology structure in: {target_base}")

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
    create_geomorphology_structure()