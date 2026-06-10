import os
import shutil

def create_environmental_current_affairs_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "environment",
        "environmental-current-affairs"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Species_in_News": [
            "Mammals_in_News",
            "Birds_in_News",
            "Reptiles_in_News",
            "Amphibians_in_News",
            "Fish_in_News",
            "Insects_in_News",
            "Endangered_Species_Updates",
            "IUCN_Status_Changes"
        ],

        "02_Protected_Areas_in_News": [
            "National_Parks_in_News",
            "Wildlife_Sanctuaries_in_News",
            "Tiger_Reserves_in_News",
            "Elephant_Reserves_in_News",
            "Conservation_Reserves_in_News",
            "Community_Reserves_in_News",
            "Protected_Area_Expansion",
            "Protected_Area_Management"
        ],

        "03_Biodiversity_and_Conservation_Updates": [
            "Conservation_Projects",
            "Species_Recovery_Programmes",
            "Wildlife_Censuses",
            "Biodiversity_Assessments",
            "Habitat_Restoration",
            "Human_Wildlife_Conflict_Updates",
            "Invasive_Species_Developments",
            "Conservation_Success_Stories"
        ],

        "04_Ramsar_Sites_and_Wetlands_in_News": [
            "New_Ramsar_Sites",
            "Wetland_Conservation_Projects",
            "Wetland_Restoration",
            "Wetland_Policies",
            "Wetland_Threats",
            "Montreux_Record_Updates",
            "Urban_Wetlands",
            "Wetland_Current_Affairs"
        ],

        "05_Forests_and_Tree_Cover_in_News": [
            "Forest_Survey_Reports",
            "Afforestation_Projects",
            "Deforestation_Issues",
            "Forest_Fires",
            "Forest_Rights_Developments",
            "Community_Forestry",
            "Forest_Policies",
            "Forest_Current_Affairs"
        ],

        "06_Climate_Change_Developments": [
            "Global_Warming_Updates",
            "Extreme_Weather_Events",
            "Climate_Records",
            "Climate_Research",
            "Climate_Adaptation_Initiatives",
            "Climate_Mitigation_Initiatives",
            "Carbon_Emission_Trends",
            "Climate_Current_Affairs"
        ],

        "07_COP_and_Climate_Summits": [
            "COP_Developments",
            "UNFCCC_Updates",
            "Paris_Agreement_Progress",
            "Climate_Negotiations",
            "Global_Stocktake",
            "Climate_Finance_Discussions",
            "Loss_and_Damage_Fund",
            "Major_Summit_Outcomes"
        ],

        "08_International_Environmental_Conventions_in_News": [
            "CBD_Updates",
            "Ramsar_Updates",
            "CITES_Updates",
            "CMS_Updates",
            "Montreal_Protocol_Updates",
            "UNCCD_Updates",
            "Basel_Rotterdam_Stockholm_Updates",
            "Treaty_Implementation_Updates"
        ],

        "09_Environmental_Reports_and_Indices": [
            "IPCC_Reports",
            "Emissions_Gap_Report",
            "Living_Planet_Report",
            "Global_Biodiversity_Outlook",
            "State_of_Forest_Report",
            "Environmental_Performance_Index",
            "Air_Quality_Reports",
            "Sustainability_Reports"
        ],

        "10_Environmental_Organizations_in_News": [
            "UNEP_Updates",
            "IPCC_Updates",
            "IUCN_Updates",
            "WWF_Reports",
            "GEF_Projects",
            "Green_Climate_Fund_Updates",
            "UNESCO_MAB_Updates",
            "International_Initiatives"
        ],

        "11_Pollution_and_Environmental_Health": [
            "Air_Pollution_Updates",
            "Water_Pollution_Updates",
            "Plastic_Pollution_Developments",
            "E_Waste_Developments",
            "Noise_Pollution_Issues",
            "Industrial_Pollution_Cases",
            "Environmental_Health_Studies",
            "Pollution_Control_Measures"
        ],

        "12_Green_Energy_and_Clean_Technology": [
            "Solar_Energy_Updates",
            "Wind_Energy_Updates",
            "Green_Hydrogen_Developments",
            "Battery_Technologies",
            "Electric_Vehicles",
            "Biofuel_Developments",
            "Carbon_Capture_Projects",
            "Renewable_Energy_Policies"
        ],

        "13_Sustainable_Development_and_Green_Economy": [
            "SDG_Progress",
            "Green_Growth_Updates",
            "Circular_Economy_Developments",
            "Blue_Economy_Initiatives",
            "Green_Finance_Updates",
            "ESG_Developments",
            "LiFE_Mission_Updates",
            "Sustainability_Policies"
        ],

        "14_Disasters_and_Environmental_Risks": [
            "Floods_in_News",
            "Cyclones_in_News",
            "Droughts_in_News",
            "Heatwaves_in_News",
            "Forest_Fires_in_News",
            "Landslides_in_News",
            "Glacial_Lake_Outburst_Floods",
            "Disaster_Management_Updates"
        ],

        "15_Indian_Government_Environment_Initiatives": [
            "MoEFCC_Initiatives",
            "National_Clean_Air_Programme",
            "Namami_Gange",
            "Green_India_Mission",
            "Project_Tiger_Updates",
            "Project_Elephant_Updates",
            "Mission_LiFE",
            "New_Government_Schemes"
        ],

        "16_Environmental_Laws_and_Policies_in_News": [
            "EIA_Amendments",
            "Forest_Conservation_Updates",
            "Wildlife_Protection_Updates",
            "Biodiversity_Act_Updates",
            "Waste_Management_Rules",
            "Environmental_Clearances",
            "Policy_Reforms",
            "Regulatory_Developments"
        ],

        "17_Court_Judgements_and_NGT_Cases": [
            "Supreme_Court_Judgements",
            "High_Court_Judgements",
            "NGT_Orders",
            "Environmental_Litigation",
            "Pollution_Cases",
            "Forest_Cases",
            "Wildlife_Cases",
            "Legal_Precedents"
        ],

        "18_Science_and_Technology_in_Environment": [
            "Environmental_Biotechnology",
            "GM_Crops_Updates",
            "Remote_Sensing_Applications",
            "GIS_Applications",
            "Environmental_Monitoring_Tech",
            "Geoengineering_Research",
            "AI_for_Environment",
            "Green_Innovations"
        ],

        "19_Monthly_Yearly_Environment_Compilations": [
            "Monthly_Current_Affairs",
            "Quarterly_Reviews",
            "Half_Yearly_Reviews",
            "Annual_Environment_Review",
            "Important_Environment_Persons",
            "Important_Environment_Awards",
            "Important_Environment_Days",
            "Exam_Oriented_Revision"
        ],

        "20_UPSC_High_Yield_Environment_Current_Affairs": [
            "Prelims_Focused_Topics",
            "Mains_Focused_Topics",
            "Important_Maps_and_Locations",
            "Important_Species",
            "Important_Reports",
            "Important_Organizations",
            "Important_Conventions",
            "Expected_Questions"
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

    print(f"Creating Environmental Current Affairs structure in: {target_base}")

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
    create_environmental_current_affairs_structure()