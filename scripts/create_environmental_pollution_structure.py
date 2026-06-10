import os
import shutil

def create_environmental_pollution_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "environmental-pollution"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Pollution_Fundamentals": [
            "Meaning_of_Pollution",
            "Types_of_Pollution",
            "Sources_of_Pollution",
            "Natural_Pollution",
            "Anthropogenic_Pollution",
            "Pollutants_and_Contaminants",
            "Environmental_Impact",
            "Pollution_Indicators"
        ],

        "02_Air_Pollution": [
            "Air_Pollution_Concept",
            "Primary_Pollutants",
            "Secondary_Pollutants",
            "Sources_of_Air_Pollution",
            "Urban_Air_Pollution",
            "Industrial_Air_Pollution",
            "Indoor_Air_Pollution",
            "Health_Impacts"
        ],

        "03_Air_Pollutants": [
            "Particulate_Matter_PM10",
            "Particulate_Matter_PM25",
            "Sulphur_Dioxide",
            "Nitrogen_Oxides",
            "Carbon_Monoxide",
            "Ground_Level_Ozone",
            "Lead_Pollution",
            "Volatile_Organic_Compounds"
        ],

        "04_Smog_and_Acid_Rain": [
            "Classical_Smog",
            "Photochemical_Smog",
            "Acid_Rain_Formation",
            "Sulphur_Emissions",
            "Nitrogen_Emissions",
            "Environmental_Impacts",
            "Control_Measures",
            "Case_Studies"
        ],

        "05_Water_Pollution": [
            "Water_Pollution_Concept",
            "Surface_Water_Pollution",
            "Groundwater_Pollution",
            "Point_Source_Pollution",
            "Non_Point_Source_Pollution",
            "Industrial_Effluents",
            "Sewage_Pollution",
            "Health_Impacts"
        ],

        "06_Water_Quality_Indicators": [
            "Biological_Oxygen_Demand",
            "Chemical_Oxygen_Demand",
            "Dissolved_Oxygen",
            "Total_Dissolved_Solids",
            "pH_Level",
            "Coliform_Bacteria",
            "Water_Quality_Index",
            "Monitoring_Methods"
        ],

        "07_Marine_and_Coastal_Pollution": [
            "Marine_Pollution",
            "Oil_Spills",
            "Plastic_Pollution",
            "Coastal_Eutrophication",
            "Ballast_Water_Issues",
            "Microplastics",
            "Marine_Debris",
            "Control_Measures"
        ],

        "08_Soil_Pollution": [
            "Soil_Pollution_Concept",
            "Agricultural_Chemicals",
            "Industrial_Waste",
            "Heavy_Metal_Contamination",
            "Land_Degradation",
            "Soil_Quality_Decline",
            "Health_Impacts",
            "Remediation_Techniques"
        ],

        "09_Noise_Pollution": [
            "Noise_Pollution_Concept",
            "Sources_of_Noise",
            "Urban_Noise",
            "Industrial_Noise",
            "Transportation_Noise",
            "Health_Effects",
            "Noise_Standards",
            "Control_Measures"
        ],

        "10_Thermal_Pollution": [
            "Thermal_Pollution_Concept",
            "Power_Plant_Discharges",
            "Aquatic_Ecosystem_Impacts",
            "Temperature_Changes",
            "Dissolved_Oxygen_Decline",
            "Biodiversity_Impacts",
            "Monitoring",
            "Control_Strategies"
        ],

        "11_Radioactive_Pollution": [
            "Radioactive_Pollution_Concept",
            "Natural_Radiation",
            "Nuclear_Accidents",
            "Radioactive_Waste",
            "Radiation_Exposure",
            "Health_Impacts",
            "Environmental_Impacts",
            "Safety_Measures"
        ],

        "12_Plastic_Pollution": [
            "Plastic_Waste_Generation",
            "Single_Use_Plastics",
            "Microplastics",
            "Marine_Plastic_Pollution",
            "Plastic_Waste_Management",
            "Recycling",
            "Extended_Producer_Responsibility",
            "Government_Initiatives"
        ],

        "13_E_Waste_Pollution": [
            "Electronic_Waste",
            "Sources_of_E_Waste",
            "Hazardous_Components",
            "Informal_Recycling",
            "Environmental_Impacts",
            "Health_Impacts",
            "E_Waste_Rules",
            "Management_Strategies"
        ],

        "14_Biomedical_and_Hazardous_Waste": [
            "Biomedical_Waste",
            "Hazardous_Waste",
            "Waste_Categorization",
            "Treatment_Methods",
            "Disposal_Methods",
            "Health_Risks",
            "Regulatory_Framework",
            "Best_Practices"
        ],

        "15_Agricultural_Pollution": [
            "Fertilizer_Runoff",
            "Pesticide_Contamination",
            "Agricultural_Residues",
            "Stubble_Burning",
            "Nutrient_Loading",
            "Water_Contamination",
            "Soil_Degradation",
            "Sustainable_Practices"
        ],

        "16_Industrial_Pollution": [
            "Industrial_Emissions",
            "Industrial_Effluents",
            "Mining_Pollution",
            "Chemical_Industries",
            "Thermal_Power_Plants",
            "Environmental_Compliance",
            "Cleaner_Production",
            "Pollution_Control_Technologies"
        ],

        "17_Urban_Pollution": [
            "Urbanization_and_Pollution",
            "Vehicular_Emissions",
            "Construction_Dust",
            "Solid_Waste_Issues",
            "Urban_Water_Pollution",
            "Urban_Heat_Island",
            "Public_Health_Impacts",
            "Urban_Management"
        ],

        "18_Eutrophication": [
            "Meaning_of_Eutrophication",
            "Nutrient_Enrichment",
            "Algal_Blooms",
            "Hypoxia",
            "Dead_Zones",
            "Freshwater_Ecosystems",
            "Marine_Ecosystems",
            "Control_Measures"
        ],

        "19_Pollution_Monitoring_and_Control": [
            "Environmental_Monitoring",
            "Air_Quality_Monitoring",
            "Water_Quality_Monitoring",
            "Pollution_Control_Devices",
            "Emission_Standards",
            "Environmental_Auditing",
            "Compliance_Assessment",
            "Data_Management"
        ],

        "20_Air_Quality_Index_and_Standards": [
            "Air_Quality_Index",
            "AQI_Categories",
            "National_Ambient_Air_Quality_Standards",
            "Pollutant_Thresholds",
            "Monitoring_Networks",
            "Forecasting_Systems",
            "Public_Advisories",
            "Recent_Updates"
        ],

        "21_Pollution_Control_Programmes_in_India": [
            "National_Clean_Air_Programme",
            "GRAP",
            "Namami_Gange",
            "Swachh_Bharat_Mission",
            "Waste_Management_Initiatives",
            "Plastic_Ban_Initiatives",
            "Pollution_Control_Schemes",
            "Performance_Assessment"
        ],

        "22_Current_Affairs_and_Pollution_Issues": [
            "Delhi_Air_Pollution",
            "Stubble_Burning_Issues",
            "River_Pollution_Cases",
            "Plastic_Pollution_Developments",
            "Industrial_Disasters",
            "Environmental_Reports",
            "Government_Actions",
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

    print(f"Creating Environmental Pollution structure in: {target_base}")

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
    create_environmental_pollution_structure()