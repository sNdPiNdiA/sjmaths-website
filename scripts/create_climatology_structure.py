import os
import shutil

def create_climatology_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "physical-geography",
        "climatology"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Climatology_Fundamentals": [
            "Meaning_of_Climate",
            "Weather_and_Climate",
            "Elements_of_Climate",
            "Scope_of_Climatology",
            "Atmosphere_and_Climate",
            "Climate_System",
            "Importance_of_Climate",
            "Sources_of_Study"
        ],

        "02_Atmosphere_Composition_and_Structure": [
            "Composition_of_Atmosphere",
            "Troposphere",
            "Stratosphere",
            "Mesosphere",
            "Thermosphere",
            "Exosphere",
            "Atmospheric_Gases",
            "Atmospheric_Structure"
        ],

        "03_Solar_Radiation_and_Insolation": [
            "Solar_Constant",
            "Insolation",
            "Heat_Budget",
            "Latitudinal_Variation",
            "Earth_Sun_Relations",
            "Seasonal_Changes",
            "Radiation_Balance",
            "Distribution_of_Insolation"
        ],

        "04_Heat_Budget_and_Temperature": [
            "Earth_Heat_Budget",
            "Temperature_Distribution",
            "Isotherms",
            "Diurnal_Range",
            "Annual_Range",
            "Temperature_Inversion",
            "Factors_Affecting_Temperature",
            "Global_Patterns"
        ],

        "05_Atmospheric_Pressure": [
            "Pressure_Belts",
            "Measurement_of_Pressure",
            "Isobars",
            "Pressure_Gradient",
            "Vertical_Pressure_Changes",
            "Global_Pressure_Belts",
            "Pressure_Systems",
            "Weather_Implications"
        ],

        "06_Winds_and_Circulation": [
            "Planetary_Winds",
            "Trade_Winds",
            "Westerlies",
            "Polar_Winds",
            "Pressure_Gradient_Force",
            "Coriolis_Force",
            "Global_Circulation",
            "Wind_Systems"
        ],

        "07_Local_Winds": [
            "Land_and_Sea_Breeze",
            "Mountain_and_Valley_Breeze",
            "Loo",
            "Chinook",
            "Foehn",
            "Mistral",
            "Sirocco",
            "Local_Wind_Characteristics"
        ],

        "08_Jet_Streams": [
            "Subtropical_Jet_Stream",
            "Polar_Front_Jet",
            "Tropical_Easterly_Jet",
            "Jet_Stream_Formation",
            "Weather_Influence",
            "Indian_Monsoon_Linkage",
            "Upper_Air_Circulation",
            "Seasonal_Variation"
        ],

        "09_Humidity_and_Condensation": [
            "Absolute_Humidity",
            "Relative_Humidity",
            "Dew_Point",
            "Condensation",
            "Fog",
            "Mist",
            "Cloud_Formation",
            "Atmospheric_Moisture"
        ],

        "10_Clouds_and_Precipitation": [
            "Cloud_Classification",
            "Cirrus",
            "Cumulus",
            "Stratus",
            "Rainfall_Types",
            "Snowfall",
            "Hail",
            "Precipitation_Mechanisms"
        ],

        "11_Air_Masses": [
            "Continental_Air_Masses",
            "Maritime_Air_Masses",
            "Polar_Air_Masses",
            "Tropical_Air_Masses",
            "Air_Mass_Modification",
            "Source_Regions",
            "Characteristics",
            "Weather_Conditions"
        ],

        "12_Fronts_and_Frontal_Weather": [
            "Warm_Front",
            "Cold_Front",
            "Occluded_Front",
            "Stationary_Front",
            "Frontal_Formation",
            "Weather_Changes",
            "Cyclogenesis",
            "Front_Characteristics"
        ],

        "13_Tropical_Cyclones": [
            "Cyclone_Formation",
            "Structure_of_Cyclone",
            "Tropical_Cyclones",
            "Cyclone_Tracking",
            "Storm_Surge",
            "Regional_Distribution",
            "Impacts",
            "Disaster_Management"
        ],

        "14_Temperate_Cyclones": [
            "Extratropical_Cyclones",
            "Polar_Front_Theory",
            "Cyclogenesis",
            "Cyclone_Life_Cycle",
            "Weather_Associated",
            "Regional_Distribution",
            "Characteristics",
            "Comparison_with_Tropical_Cyclones"
        ],

        "15_Anticyclones": [
            "Anticyclone_Formation",
            "High_Pressure_Systems",
            "Weather_Conditions",
            "Subtropical_Highs",
            "Polar_Highs",
            "Characteristics",
            "Seasonal_Variations",
            "Global_Distribution"
        ],

        "16_Thunderstorms_and_Severe_Weather": [
            "Thunderstorm_Formation",
            "Lightning",
            "Tornadoes",
            "Waterspouts",
            "Hailstorms",
            "Cloudbursts",
            "Severe_Weather",
            "Hazards"
        ],

        "17_Climate_Classification": [
            "Koppen_Classification",
            "Thornthwaite_Classification",
            "Trewartha_Classification",
            "Climate_Regions",
            "Classification_Criteria",
            "Global_Climate_Zones",
            "Applications",
            "Comparisons"
        ],

        "18_World_Climate_Regions": [
            "Equatorial_Climate",
            "Monsoon_Climate",
            "Mediterranean_Climate",
            "Desert_Climate",
            "Temperate_Climate",
            "Polar_Climate",
            "Distribution",
            "Characteristics"
        ],

        "19_Monsoon_System": [
            "Monsoon_Concept",
            "Southwest_Monsoon",
            "Northeast_Monsoon",
            "Monsoon_Mechanism",
            "Onset_and_Withdrawal",
            "Monsoon_Branches",
            "Rainfall_Distribution",
            "Variability"
        ],

        "20_Indian_Climate": [
            "Factors_Affecting_Climate",
            "Seasonal_Changes",
            "Winter_Season",
            "Summer_Season",
            "Rainy_Season",
            "Retreating_Monsoon",
            "Regional_Variations",
            "Climate_Characteristics"
        ],

        "21_El_Nino_La_Nina_and_ENSO": [
            "El_Nino",
            "La_Nina",
            "Southern_Oscillation",
            "ENSO",
            "Ocean_Atmosphere_Interaction",
            "Monsoon_Impact",
            "Global_Climate_Impact",
            "Recent_Events"
        ],

        "22_Climate_Change": [
            "Global_Warming",
            "Greenhouse_Effect",
            "Climate_Forcing",
            "Temperature_Trends",
            "Sea_Level_Rise",
            "Extreme_Weather",
            "Observed_Changes",
            "Future_Projections"
        ],

        "23_Greenhouse_Gases_and_Carbon_Cycle": [
            "Carbon_Dioxide",
            "Methane",
            "Nitrous_Oxide",
            "Carbon_Cycle",
            "Carbon_Sinks",
            "Carbon_Budget",
            "Anthropogenic_Emissions",
            "Mitigation"
        ],

        "24_Climate_Policies_and_International_Agreements": [
            "UNFCCC",
            "Kyoto_Protocol",
            "Paris_Agreement",
            "COP_Meetings",
            "Nationally_Determined_Contributions",
            "Climate_Governance",
            "Global_Cooperation",
            "Policy_Challenges"
        ],

        "25_Climate_Impacts_and_Adaptation": [
            "Agriculture_Impacts",
            "Water_Resources",
            "Health_Impacts",
            "Biodiversity_Impacts",
            "Disaster_Risk",
            "Adaptation_Strategies",
            "Resilience",
            "Sustainable_Development"
        ],

        "26_Agrometeorology_and_Applied_Climatology": [
            "Agricultural_Weather",
            "Crop_Climate_Relationships",
            "Weather_Forecasting",
            "Climate_Services",
            "Drought_Monitoring",
            "Frost",
            "Agroclimatic_Zones",
            "Applications"
        ],

        "27_Current_Affairs_and_Climate_Issues": [
            "Recent_COP_Summits",
            "Climate_Finance",
            "Carbon_Markets",
            "Extreme_Weather_Events",
            "Heat_Waves",
            "Cyclone_Updates",
            "Policy_Developments",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Pressure_Belt_Maps",
            "Wind_System_Maps",
            "Climate_Region_Maps",
            "Monsoon_Maps",
            "Cyclone_Tracks",
            "Climate_Data",
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

    print(f"Creating Climatology structure in: {target_base}")
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
    create_climatology_structure()