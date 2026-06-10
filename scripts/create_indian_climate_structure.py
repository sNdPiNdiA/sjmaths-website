import os
import shutil

def create_indian_climate_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography", "climate")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Climate_Fundamentals": [
            "Meaning_of_Climate",
            "Weather_vs_Climate",
            "Characteristics_of_Indian_Climate",
            "Monsoon_Type_Climate",
            "Diversity_of_Climate",
            "Tropical_Location",
            "Seasonality",
            "Sources_of_Study"
        ],

        "02_Climate_Controls": [
            "Latitude",
            "Altitude",
            "Distance_from_Sea",
            "Pressure_and_Winds",
            "Relief_Features",
            "Himalayan_Barrier",
            "Oceanic_Influence",
            "Physiographic_Factors"
        ],

        "03_Atmospheric_Circulation": [
            "Global_Circulation",
            "Trade_Winds",
            "Subtropical_High_Pressure",
            "ITCZ",
            "Pressure_Belts",
            "Seasonal_Shifts",
            "Cross_Equatorial_Flow",
            "Atmospheric_Dynamics"
        ],

        "04_Jet_Streams_and_Upper_Air_Circulation": [
            "Subtropical_Westerly_Jet",
            "Tropical_Easterly_Jet",
            "Jet_Stream_Shifts",
            "Role_in_Monsoon",
            "Upper_Air_Circulation",
            "Rossby_Waves",
            "Blocking_Patterns",
            "Weather_Influence"
        ],

        "05_Origin_of_Indian_Monsoon": [
            "Thermal_Theory",
            "Dynamic_Theory",
            "Land_Sea_Contrast",
            "Tibetan_Plateau",
            "Mascarene_High",
            "Cross_Equatorial_Winds",
            "Monsoon_Onset_Mechanism",
            "Modern_Explanations"
        ],

        "06_South_West_Monsoon": [
            "Onset_of_Monsoon",
            "Arabian_Sea_Branch",
            "Bay_of_Bengal_Branch",
            "Advance_of_Monsoon",
            "Rainfall_Mechanism",
            "Break_in_Monsoon",
            "Spatial_Variation",
            "Monsoon_Progress"
        ],

        "07_Retreating_Monsoon": [
            "Withdrawal_of_Monsoon",
            "October_Heat",
            "Retreating_Monsoon_Season",
            "North_East_Monsoon",
            "Tamil_Nadu_Rainfall",
            "Seasonal_Transition",
            "Cyclonic_Activity",
            "Regional_Impact"
        ],

        "08_Seasonal_Climate_of_India": [
            "Cold_Weather_Season",
            "Hot_Weather_Season",
            "South_West_Monsoon_Season",
            "Retreating_Monsoon_Season",
            "Seasonal_Characteristics",
            "Temperature_Changes",
            "Pressure_Changes",
            "Seasonal_Cycle"
        ],

        "09_Rainfall_Distribution": [
            "Spatial_Distribution",
            "High_Rainfall_Areas",
            "Low_Rainfall_Areas",
            "Orographic_Rainfall",
            "Rain_Shadow_Regions",
            "Rainfall_Gradient",
            "Regional_Variations",
            "Rainfall_Statistics"
        ],

        "10_Temperature_Distribution": [
            "Annual_Temperature",
            "Seasonal_Temperature",
            "Temperature_Gradient",
            "Continentality",
            "Maritime_Influence",
            "Heat_Waves",
            "Cold_Waves",
            "Regional_Patterns"
        ],

        "11_Monsoon_Variability": [
            "Normal_Monsoon",
            "Weak_Monsoon",
            "Excess_Monsoon",
            "Monsoon_Fluctuations",
            "Intra_Seasonal_Variability",
            "Monsoon_Prediction",
            "Long_Range_Forecast",
            "Recent_Trends"
        ],

        "12_ENSO_IOD_and_Global_Influences": [
            "El_Nino",
            "La_Nina",
            "Southern_Oscillation",
            "ENSO_Monsoon_Relationship",
            "Indian_Ocean_Dipole",
            "Madden_Julian_Oscillation",
            "Pacific_Influence",
            "Global_Teleconnections"
        ],

        "13_Climatic_Regions_of_India": [
            "Koppen_Classification",
            "Thornthwaite_Classification",
            "Humid_Regions",
            "Semi_Arid_Regions",
            "Arid_Regions",
            "Mountain_Climate",
            "Regional_Climate_Types",
            "Classification_Methods"
        ],

        "14_Western_Disturbances": [
            "Origin",
            "Mediterranean_Source",
            "Winter_Rainfall",
            "North_Indian_Weather",
            "Snowfall_in_Himalayas",
            "Agricultural_Importance",
            "Seasonal_Influence",
            "Recent_Trends"
        ],

        "15_Local_Weather_Phenomena": [
            "Loo",
            "Mango_Showers",
            "Kal_Baisakhi",
            "Coffee_Blossom_Showers",
            "Norwesters",
            "Dust_Storms",
            "Fog",
            "Local_Weather_Events"
        ],

        "16_Tropical_Cyclones": [
            "Cyclone_Formation",
            "Bay_of_Bengal_Cyclones",
            "Arabian_Sea_Cyclones",
            "Cyclone_Tracks",
            "Cyclone_Seasons",
            "Storm_Surge",
            "Cyclone_Warnings",
            "Impact_on_India"
        ],

        "17_Thunderstorms_and_Extreme_Events": [
            "Thunderstorms",
            "Lightning",
            "Cloudbursts",
            "Hailstorms",
            "Extreme_Rainfall",
            "Convective_Activity",
            "Localized_Disasters",
            "Hazard_Assessment"
        ],

        "18_Droughts_in_India": [
            "Meteorological_Drought",
            "Agricultural_Drought",
            "Hydrological_Drought",
            "Drought_Prone_Areas",
            "Causes_of_Drought",
            "Drought_Monitoring",
            "Mitigation_Strategies",
            "Historical_Droughts"
        ],

        "19_Floods_in_India": [
            "Riverine_Floods",
            "Flash_Floods",
            "Urban_Floods",
            "Flood_Prone_Regions",
            "Monsoon_Floods",
            "Flood_Management",
            "Flood_Control_Projects",
            "Major_Flood_Events"
        ],

        "20_Climate_and_Agriculture": [
            "Monsoon_Dependence",
            "Cropping_Seasons",
            "Rainfed_Agriculture",
            "Agricultural_Productivity",
            "Climate_Risks",
            "Drought_and_Crops",
            "Weather_Based_Farming",
            "Agro_Climatic_Influence"
        ],

        "21_Climate_and_Water_Resources": [
            "Rainfall_and_Rivers",
            "Groundwater_Recharge",
            "Water_Availability",
            "Reservoirs",
            "Hydrological_Cycle",
            "Water_Stress",
            "Inter_Regional_Variations",
            "Water_Security"
        ],

        "22_Climate_and_Economy": [
            "Agriculture",
            "Hydropower",
            "Transport",
            "Tourism",
            "Fisheries",
            "Industry",
            "Livelihoods",
            "Economic_Impacts"
        ],

        "23_Climate_Change_in_India": [
            "Temperature_Rise",
            "Changing_Rainfall",
            "Glacier_Retreat",
            "Sea_Level_Rise",
            "Extreme_Events",
            "Observed_Trends",
            "Scientific_Assessments",
            "Future_Projections"
        ],

        "24_Climate_Adaptation_and_Mitigation": [
            "National_Action_Plan_on_Climate_Change",
            "State_Action_Plans",
            "Climate_Resilience",
            "Adaptation_Strategies",
            "Disaster_Risk_Reduction",
            "Renewable_Energy",
            "Carbon_Mitigation",
            "Policy_Framework"
        ],

        "25_Weather_Observation_and_Forecasting": [
            "India_Meteorological_Department",
            "Weather_Stations",
            "Satellites",
            "Doppler_Radar",
            "Forecasting_Models",
            "Monsoon_Forecasting",
            "Early_Warning_Systems",
            "Meteorological_Technology"
        ],

        "26_Regional_Climate_Case_Studies": [
            "Western_Ghats",
            "Thar_Desert",
            "North_East_India",
            "Indo_Gangetic_Plain",
            "Himalayan_Region",
            "Coastal_India",
            "Deccan_Plateau",
            "Regional_Comparisons"
        ],

        "27_Current_Affairs_and_Contemporary_Issues": [
            "Recent_Monsoon_Trends",
            "Cyclone_Case_Studies",
            "Heat_Wave_Events",
            "Extreme_Rainfall_Events",
            "Climate_Reports",
            "IMD_Updates",
            "Disaster_Statistics",
            "UPSC_High_Yield_Themes"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Rainfall_Maps",
            "Temperature_Maps",
            "Monsoon_Maps",
            "Cyclone_Tracks",
            "Climate_Data_Interpretation",
            "Assertion_Reason_Themes",
            "Map_Based_Questions",
            "PYQ_Patterns"
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

    print(f"Creating Indian Climate structure in: {target_base}")
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
    create_indian_climate_structure()