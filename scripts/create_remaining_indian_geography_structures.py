import os
import shutil

def create_remaining_indian_geography_structures():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    indian_geo_base = os.path.join(project_root, "gs-question-bank", "geography", "indian-geography")

    structures = {
        "location-and-physiography": {
            "01_Location_and_Extent": [
                "Latitudinal_and_Longitudinal_Extent", "India_and_the_World", "Borders_and_Neighbors", "Standard_Meridian", "Geopolitical_Significance"
            ],
            "02_Geological_Structure": [
                "Rock_Systems_of_India", "Archaean_and_Dharwar", "Cuddapah_and_Vindhyan", "Gondwana_System", "Deccan_Traps", "Tertiary_System"
            ],
            "03_The_Himalayas": [
                "Origin_and_Formation", "Trans_Himalayas", "Greater_Himalayas", "Middle_Himalayas", "Shiwaliks", "Regional_Divisions_of_Himalayas", "Purvanchal_Hills"
            ],
            "04_The_Northern_Plains": [
                "Formation_of_Plains", "Bhabar_and_Terai", "Bhangar_and_Khadar", "Punjab_Plains", "Ganga_Plains", "Brahmaputra_Plains"
            ],
            "05_The_Peninsular_Plateau": [
                "Central_Highlands", "Deccan_Plateau", "Malwa_and_Chotanagpur", "Meghalaya_Plateau", "Aravallis_and_Vindhyas", "Satpuras"
            ],
            "06_The_Coastal_Plains": [
                "Western_Coastal_Plains", "Eastern_Coastal_Plains", "Comparison_of_Coasts", "Estuaries_and_Deltas", "Economic_Significance"
            ],
            "07_The_Islands": [
                "Andaman_and_Nicobar", "Lakshadweep", "Formation_of_Islands", "Coral_Reefs", "Strategic_Importance"
            ],
            "08_Mountain_Passes_and_Peaks": [
                "Himalayan_Passes", "Peninsular_Passes", "Highest_Peaks", "Strategic_Passes", "Map_Locations"
            ],
            "09_Important_Valleys": [
                "Kashmir_Valley", "Kullu_and_Kangra", "Doon_Valleys", "Silent_Valley", "Other_Significant_Valleys"
            ]
        },
        "drainage-system": {
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
        },
        "soils-and-natural-vegetation": {
            "01_Soil_Formation_and_Profiles": [
                "Factors_of_Soil_Formation", "Soil_Profile", "Soil_Horizons", "Physical_and_Chemical_Properties", "ICAR_Classification"
            ],
            "02_Alluvial_and_Black_Soils": [
                "Distribution_of_Alluvial_Soil", "Characteristics_of_Alluvial", "Distribution_of_Black_Soil", "Characteristics_of_Black_Soil", "Crops_Grown"
            ],
            "03_Red_Laterite_and_Other_Soils": [
                "Red_and_Yellow_Soils", "Laterite_Soils", "Arid_and_Desert_Soils", "Saline_and_Alkaline_Soils", "Peaty_and_Forest_Soils"
            ],
            "04_Soil_Degradation_and_Conservation": [
                "Soil_Erosion", "Types_of_Erosion", "Causes_of_Degradation", "Conservation_Methods", "Government_Schemes"
            ],
            "05_Natural_Vegetation_Types": [
                "Factors_Affecting_Vegetation", "Classification_of_Forests", "Forest_Cover_in_India", "ISFR_Report", "Endemic_Species"
            ],
            "06_Tropical_Forests": [
                "Evergreen_and_Semi_Evergreen", "Moist_Deciduous", "Dry_Deciduous", "Thorn_Forests", "Economic_Value"
            ],
            "07_Montane_and_Mangrove_Forests": [
                "Himalayan_Vegetation", "Peninsular_Hills_Vegetation", "Alpine_Forests", "Mangrove_Forests", "Sunderbans"
            ],
            "08_Forest_Conservation_and_Policies": [
                "Deforestation", "National_Forest_Policy", "Social_Forestry", "Agroforestry", "Joint_Forest_Management"
            ],
            "09_Biosphere_Reserves_and_National_Parks": [
                "Wildlife_Sanctuaries", "National_Parks", "Biosphere_Reserves", "Project_Tiger_and_Elephant", "Conservation_Efforts"
            ]
        },
        "mineral-and-energy-resources": {
            "01_Classification_of_Minerals": [
                "Metallic_and_Non_Metallic", "Ferrous_and_Non_Ferrous", "Mineral_Belts_of_India", "Mining_Methods", "Geological_Distribution"
            ],
            "02_Iron_Ore_and_Manganese": [
                "Types_of_Iron_Ore", "Distribution_of_Iron", "Export_and_Trade", "Manganese_Distribution", "Uses_and_Reserves"
            ],
            "03_Bauxite_and_Copper": [
                "Bauxite_Distribution", "Aluminum_Industry", "Copper_Distribution", "Uses_of_Copper", "Other_Non_Ferrous_Minerals"
            ],
            "04_Non_Metallic_Minerals": [
                "Mica", "Limestone", "Dolomite", "Other_Industrial_Minerals", "Building_Stones"
            ],
            "05_Conventional_Energy_Coal_Petroleum": [
                "Gondwana_Coal", "Tertiary_Coal", "Coal_Distribution", "Petroleum_and_Refineries", "Oil_Fields"
            ],
            "06_Natural_Gas_and_Nuclear_Energy": [
                "Natural_Gas_Reserves", "Pipelines", "Nuclear_Minerals_Uranium_Thorium", "Nuclear_Power_Plants", "Atomic_Energy_Commission"
            ],
            "07_Non_Conventional_Energy_Solar_Wind": [
                "Solar_Energy_Potential", "Wind_Energy_Farms", "Biogas_and_Biomass", "Geothermal_Energy", "Tidal_and_Wave_Energy"
            ],
            "08_Conservation_of_Resources": [
                "Sustainable_Mining", "Environmental_Impact_of_Mining", "National_Mineral_Policy", "Energy_Conservation", "Future_Prospects"
            ]
        },
        "industries-and-transport": {
            "01_Industrial_Location_Factors": [
                "Raw_Materials", "Power_and_Labor", "Market_and_Transport", "Government_Policies", "Weber_Theory_Application"
            ],
            "02_Agro_Based_Industries": [
                "Cotton_Textiles", "Jute_Industry", "Sugar_Industry", "Food_Processing", "Silk_and_Woolen"
            ],
            "03_Mineral_Based_Industries": [
                "Iron_and_Steel", "Aluminum_Smelting", "Cement_Industry", "Chemical_and_Fertilizers", "Automobile_Industry"
            ],
            "04_Manufacturing_and_IT_Industries": [
                "Make_in_India", "Electronics_Manufacturing", "IT_and_Software_Parks", "Pharmaceutical_Industry", "MSME_Sector"
            ],
            "05_Industrial_Regions_of_India": [
                "Mumbai_Pune_Region", "Hugli_Region", "Bengaluru_Tamil_Nadu_Region", "Gujarat_Region", "Other_Major_Regions"
            ],
            "06_Road_Transport": [
                "National_Highways", "State_Highways", "Golden_Quadrilateral", "North_South_East_West_Corridor", "Bharatmala_Pariyojana"
            ],
            "07_Railways": [
                "Railway_Zones", "Dedicated_Freight_Corridors", "High_Speed_Rail", "Modernization", "Gauge_Conversion"
            ],
            "08_Waterways_and_Ports": [
                "National_Waterways", "Major_Ports", "Minor_Ports", "Sagarmala_Project", "Inland_Water_Transport"
            ],
            "09_Air_Transport_and_Pipelines": [
                "Aviation_Sector", "UDAN_Scheme", "Major_Airports", "Gas_and_Oil_Pipelines", "Logistics_Infrastructure"
            ]
        },
        "demography-and-census": {
            "01_Population_Distribution_and_Density": [
                "Spatial_Distribution", "Factors_Affecting_Distribution", "Population_Density", "Physiological_Density", "Agricultural_Density"
            ],
            "02_Population_Growth_and_Trends": [
                "Phases_of_Growth", "Birth_Rate_and_Death_Rate", "Natural_Growth_Rate", "Regional_Variations_in_Growth", "Future_Projections"
            ],
            "03_Demographic_Transition": [
                "Theory_Application_to_India", "Demographic_Dividend", "Age_Structure", "Dependency_Ratio", "Aging_Population"
            ],
            "04_Sex_Ratio_and_Literacy": [
                "Trends_in_Sex_Ratio", "Child_Sex_Ratio", "Factors_for_Low_Sex_Ratio", "Literacy_Rate_Trends", "Male_Female_Literacy_Gap"
            ],
            "05_Rural_and_Urban_Population": [
                "Rural_Urban_Composition", "Urbanization_Trends", "Smart_Cities", "Slums_and_Urban_Issues", "Rural_Settlement_Patterns"
            ],
            "06_Migration_Types_and_Causes": [
                "Internal_Migration", "International_Migration", "Push_and_Pull_Factors", "Streams_of_Migration", "Impact_of_Migration"
            ],
            "07_Human_Development_Index": [
                "India_Ranking", "State_Level_Variations", "Health_Indicators", "Education_Indicators", "Poverty_and_Inequality"
            ],
            "08_Population_Policies": [
                "National_Population_Policy", "Family_Planning", "Women_Empowerment", "Health_Missions", "Two_Child_Norm_Debate"
            ],
            "09_Tribes_and_Races": [
                "Major_Tribes", "Distribution_of_Tribes", "PVTGs", "Racial_Groups", "Linguistic_Diversity"
            ],
            "10_Census_Data_Analysis": [
                "Historical_Background", "Census_2011_Highlights", "SECC_2011", "Delimitation", "Current_Affairs_Census"
            ]
        }
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

    for folder, structure in structures.items():
        target_base = os.path.join(indian_geo_base, folder)
        
        if os.path.exists(target_base):
            print(f"Cleaning up older folders in: {target_base}")
            shutil.rmtree(target_base)
            
        print(f"Creating structure in: {target_base}")
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

if __name__ == "__main__":
    create_remaining_indian_geography_structures()
