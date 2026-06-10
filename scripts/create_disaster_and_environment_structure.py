import os
import shutil

def create_disaster_and_environment_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "disaster-and-environment"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Disaster_Fundamentals": [
            "Meaning_of_Disaster",
            "Hazard_and_Disaster",
            "Disaster_Risk",
            "Vulnerability",
            "Exposure",
            "Resilience",
            "Disaster_Classification",
            "Disaster_Management_Cycle"
        ],

        "02_Natural_Disasters": [
            "Geological_Disasters",
            "Hydrological_Disasters",
            "Meteorological_Disasters",
            "Climatological_Disasters",
            "Biological_Disasters",
            "Environmental_Disasters",
            "Complex_Disasters",
            "Disaster_Trends"
        ],

        "03_Earthquakes": [
            "Earthquake_Fundamentals",
            "Causes_of_Earthquakes",
            "Seismic_Waves",
            "Earthquake_Measurement",
            "Seismic_Zones_of_India",
            "Earthquake_Impacts",
            "Preparedness_and_Mitigation",
            "Major_Case_Studies"
        ],

        "04_Tsunamis": [
            "Tsunami_Formation",
            "Causes_of_Tsunamis",
            "Tsunami_Waves",
            "Indian_Ocean_Tsunami",
            "Warning_Systems",
            "Risk_Assessment",
            "Preparedness_Measures",
            "Case_Studies"
        ],

        "05_Volcanoes": [
            "Volcanic_Activity",
            "Types_of_Volcanoes",
            "Volcanic_Eruptions",
            "Volcanic_Materials",
            "Environmental_Impacts",
            "Volcanic_Hazards",
            "Monitoring_Systems",
            "Case_Studies"
        ],

        "06_Landslides": [
            "Landslide_Fundamentals",
            "Causes_of_Landslides",
            "Slope_Instability",
            "Rainfall_Induced_Landslides",
            "Earthquake_Induced_Landslides",
            "Landslide_Zones_in_India",
            "Mitigation_Strategies",
            "Case_Studies"
        ],

        "07_Floods": [
            "Riverine_Floods",
            "Flash_Floods",
            "Urban_Floods",
            "Coastal_Floods",
            "Causes_of_Flooding",
            "Flood_Prone_Areas",
            "Flood_Management",
            "Case_Studies"
        ],

        "08_Droughts": [
            "Meteorological_Drought",
            "Hydrological_Drought",
            "Agricultural_Drought",
            "Socioeconomic_Drought",
            "Causes_of_Drought",
            "Drought_Prone_Areas",
            "Mitigation_Strategies",
            "Case_Studies"
        ],

        "09_Cyclones": [
            "Tropical_Cyclones",
            "Cyclone_Formation",
            "Cyclone_Structure",
            "Cyclone_Classification",
            "Cyclones_in_India",
            "Early_Warning_Systems",
            "Preparedness_and_Response",
            "Case_Studies"
        ],

        "10_Heat_Waves_and_Cold_Waves": [
            "Heat_Waves",
            "Cold_Waves",
            "Causes",
            "Impacts_on_Health",
            "Climate_Linkages",
            "Warning_Systems",
            "Adaptation_Strategies",
            "Recent_Events"
        ],

        "11_Forest_Fires": [
            "Forest_Fire_Fundamentals",
            "Natural_Causes",
            "Human_Induced_Causes",
            "Fire_Ecology",
            "Impacts_on_Biodiversity",
            "Forest_Fire_Monitoring",
            "Fire_Management",
            "Case_Studies"
        ],

        "12_Avalanches_and_Glacial_Hazards": [
            "Avalanches",
            "Glacial_Lake_Outburst_Floods",
            "Snow_Hazards",
            "Mountain_Risks",
            "Himalayan_Vulnerability",
            "Monitoring_Systems",
            "Preparedness",
            "Case_Studies"
        ],

        "13_Biological_Disasters": [
            "Pandemics",
            "Epidemics",
            "Zoonotic_Diseases",
            "Locust_Attacks",
            "Invasive_Species",
            "Public_Health_Emergencies",
            "Response_Strategies",
            "Case_Studies"
        ],

        "14_Industrial_and_Chemical_Disasters": [
            "Industrial_Disasters",
            "Chemical_Accidents",
            "Oil_Spills",
            "Gas_Leaks",
            "Nuclear_Accidents",
            "Environmental_Consequences",
            "Safety_Frameworks",
            "Major_Case_Studies"
        ],

        "15_Climate_Change_and_Disasters": [
            "Climate_Extremes",
            "Disaster_Frequency",
            "Disaster_Intensity",
            "Sea_Level_Rise_Risks",
            "Heatwave_Trends",
            "Flood_Risks",
            "Adaptation_Strategies",
            "Resilience_Building"
        ],

        "16_Disaster_Risk_Reduction": [
            "Risk_Assessment",
            "Hazard_Mapping",
            "Vulnerability_Assessment",
            "Risk_Mitigation",
            "Community_Based_DRR",
            "Capacity_Building",
            "Resilience_Planning",
            "Best_Practices"
        ],

        "17_Disaster_Management_in_India": [
            "Disaster_Management_Act_2005",
            "NDMA",
            "SDMA",
            "NDRF",
            "National_Policy_on_Disaster_Management",
            "Incident_Response_System",
            "Institutional_Framework",
            "Recent_Reforms"
        ],

        "18_Global_Frameworks_for_Disaster_Management": [
            "Sendai_Framework",
            "Hyogo_Framework",
            "UNDRR",
            "International_Cooperation",
            "Disaster_Risk_Governance",
            "Global_Targets",
            "Monitoring_Framework",
            "Implementation_Challenges"
        ],

        "19_Disaster_Preparedness_and_Response": [
            "Early_Warning_Systems",
            "Emergency_Response",
            "Search_and_Rescue",
            "Relief_and_Rehabilitation",
            "Evacuation_Planning",
            "Disaster_Communication",
            "Recovery_Strategies",
            "Build_Back_Better"
        ],

        "20_Current_Affairs_and_Disaster_Management": [
            "Recent_Disasters",
            "Climate_Related_Disasters",
            "NDMA_Updates",
            "Sendai_Framework_Developments",
            "Disaster_Reports",
            "Government_Initiatives",
            "International_Developments",
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

    print(f"Creating Disaster and Environment structure in: {target_base}")

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
    create_disaster_and_environment_structure()