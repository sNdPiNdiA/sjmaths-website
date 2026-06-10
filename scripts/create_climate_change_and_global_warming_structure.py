import os
import shutil

def create_climate_change_and_global_warming_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "climate-change-and-global-warming"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Climate_System_Fundamentals": [
            "Weather_vs_Climate",
            "Components_of_Climate_System",
            "Atmosphere",
            "Hydrosphere",
            "Cryosphere",
            "Lithosphere",
            "Biosphere",
            "Climate_Variability"
        ],

        "02_Global_Warming_Basics": [
            "Meaning_of_Global_Warming",
            "Observed_Warming_Trends",
            "Temperature_Records",
            "Causes_of_Warming",
            "Anthropogenic_Influence",
            "Natural_Variability",
            "Evidence_of_Warming",
            "Future_Projections"
        ],

        "03_Greenhouse_Effect": [
            "Natural_Greenhouse_Effect",
            "Enhanced_Greenhouse_Effect",
            "Heat_Trapping_Mechanism",
            "Radiative_Forcing",
            "Earth_Energy_Balance",
            "Atmospheric_Warming",
            "Role_of_Gases",
            "Climate_Implications"
        ],

        "04_Greenhouse_Gases": [
            "Carbon_Dioxide",
            "Methane",
            "Nitrous_Oxide",
            "Water_Vapour",
            "Ozone",
            "Fluorinated_Gases",
            "Global_Warming_Potential",
            "Emission_Sources"
        ],

        "05_Carbon_Cycle_and_Carbon_Budget": [
            "Carbon_Reservoirs",
            "Carbon_Fluxes",
            "Carbon_Sources",
            "Carbon_Sinks",
            "Carbon_Sequestration",
            "Carbon_Budget",
            "Net_Carbon_Emissions",
            "Climate_Relevance"
        ],

        "06_Climate_Change_Drivers": [
            "Fossil_Fuel_Combustion",
            "Deforestation",
            "Land_Use_Change",
            "Industrialization",
            "Agricultural_Emissions",
            "Urbanization",
            "Aerosols",
            "Natural_Drivers"
        ],

        "07_Impacts_on_Atmosphere": [
            "Temperature_Rise",
            "Changing_Precipitation",
            "Extreme_Weather_Events",
            "Heat_Waves",
            "Cold_Waves",
            "Storm_Intensity",
            "Atmospheric_Circulation",
            "Climate_Extremes"
        ],

        "08_Impacts_on_Oceans": [
            "Ocean_Warming",
            "Ocean_Acidification",
            "Marine_Heatwaves",
            "Sea_Level_Rise",
            "Coral_Bleaching",
            "Marine_Ecosystem_Changes",
            "Ocean_Circulation",
            "Blue_Carbon"
        ],

        "09_Impacts_on_Cryosphere": [
            "Glacier_Retreat",
            "Polar_Ice_Melt",
            "Sea_Ice_Loss",
            "Permafrost_Thaw",
            "Snow_Cover_Changes",
            "Himalayan_Glaciers",
            "Cryosphere_Feedbacks",
            "Global_Consequences"
        ],

        "10_Impacts_on_Biodiversity": [
            "Species_Range_Shifts",
            "Habitat_Loss",
            "Extinction_Risk",
            "Coral_Reef_Loss",
            "Forest_Ecosystems",
            "Wetland_Ecosystems",
            "Ecosystem_Disruptions",
            "Conservation_Challenges"
        ],

        "11_Impacts_on_Agriculture": [
            "Crop_Productivity",
            "Changing_Growing_Seasons",
            "Water_Stress",
            "Pest_Outbreaks",
            "Food_Security",
            "Livestock_Impacts",
            "Climate_Resilient_Agriculture",
            "Adaptation_Strategies"
        ],

        "12_Impacts_on_Human_Society": [
            "Health_Impacts",
            "Climate_Migration",
            "Economic_Losses",
            "Disaster_Risk",
            "Water_Security",
            "Food_Security",
            "Urban_Vulnerability",
            "Social_Impacts"
        ],

        "13_Climate_Change_in_India": [
            "Indian_Temperature_Trends",
            "Monsoon_Changes",
            "Extreme_Rainfall",
            "Heatwaves_in_India",
            "Glacier_Changes",
            "Coastal_Vulnerability",
            "Agricultural_Impacts",
            "Regional_Patterns"
        ],

        "14_Climate_Modeling_and_Projections": [
            "Climate_Models",
            "Emission_Scenarios",
            "Representative_Pathways",
            "Climate_Forecasting",
            "Uncertainty_in_Models",
            "Regional_Models",
            "Projection_Methods",
            "Policy_Relevance"
        ],

        "15_IPCC": [
            "Formation_of_IPCC",
            "Assessment_Reports",
            "Working_Group_I",
            "Working_Group_II",
            "Working_Group_III",
            "Synthesis_Report",
            "Key_Findings",
            "Policy_Influence"
        ],

        "16_Climate_Mitigation": [
            "Emission_Reduction",
            "Renewable_Energy",
            "Energy_Efficiency",
            "Afforestation",
            "Carbon_Capture",
            "Sustainable_Transport",
            "Industrial_Decarbonization",
            "Mitigation_Strategies"
        ],

        "17_Climate_Adaptation": [
            "Adaptation_Concept",
            "Climate_Resilience",
            "Disaster_Preparedness",
            "Adaptive_Infrastructure",
            "Water_Management",
            "Agricultural_Adaptation",
            "Nature_Based_Adaptation",
            "Community_Adaptation"
        ],

        "18_Carbon_Markets_and_Carbon_Pricing": [
            "Carbon_Credits",
            "Carbon_Trading",
            "Compliance_Markets",
            "Voluntary_Markets",
            "Carbon_Tax",
            "Emission_Trading_Schemes",
            "Carbon_Offsetting",
            "Market_Challenges"
        ],

        "19_Climate_Justice_and_Finance": [
            "Climate_Justice",
            "Equity_Principles",
            "Loss_and_Damage",
            "Climate_Finance",
            "Green_Climate_Fund",
            "Adaptation_Fund",
            "Technology_Transfer",
            "Developing_Country_Concerns"
        ],

        "20_Net_Zero_and_Decarbonization": [
            "Net_Zero_Concept",
            "Long_Term_Strategies",
            "Sectoral_Decarbonization",
            "Energy_Transition",
            "Hydrogen_Economy",
            "Negative_Emission_Technologies",
            "National_Net_Zero_Targets",
            "India_Net_Zero_Goal"
        ],

        "21_Climate_Governance_and_Policies": [
            "National_Action_Plan_on_Climate_Change",
            "State_Action_Plans",
            "Climate_Laws",
            "National_Missions",
            "Institutional_Framework",
            "Monitoring_and_Reporting",
            "Policy_Implementation",
            "Governance_Challenges"
        ],

        "22_Current_Affairs_and_Climate_Developments": [
            "Recent_IPCC_Findings",
            "Climate_Summits",
            "Global_Emission_Trends",
            "Extreme_Weather_Events",
            "India_Climate_Initiatives",
            "Climate_Finance_Updates",
            "Scientific_Reports",
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

    print(f"Creating Climate Change and Global Warming structure in: {target_base}")

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
    create_climate_change_and_global_warming_structure()