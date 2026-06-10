import os
import shutil

def create_defense_and_space_technology_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "defense-and-space-technology"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Indian_Missile_Programme": [
            "Integrated_Guided_Missile_Programme",
            "Agni_Series",
            "Prithvi_Series",
            "Akash",
            "Nag",
            "Trishul",
            "BrahMos",
            "Missile_Modernization"
        ],

        "02_Ballistic_Missiles": [
            "Short_Range_Ballistic_Missiles",
            "Medium_Range_Ballistic_Missiles",
            "Intermediate_Range_Ballistic_Missiles",
            "Intercontinental_Ballistic_Missiles",
            "Agni_I",
            "Agni_II",
            "Agni_III_to_V",
            "Strategic_Role"
        ],

        "03_Cruise_Missiles": [
            "BrahMos",
            "Nirbhay",
            "Hypersonic_Cruise_Missiles",
            "Subsonic_Cruise_Missiles",
            "Land_Attack_Cruise_Missiles",
            "Ship_Launched_Cruise_Missiles",
            "Air_Launched_Cruise_Missiles",
            "Future_Developments"
        ],

        "04_Air_Defence_Systems": [
            "S400",
            "Akash_Air_Defence",
            "Barak_8",
            "QRSAM",
            "MRSAM",
            "XR_SAM",
            "Ballistic_Missile_Defence",
            "Integrated_Air_Defence"
        ],

        "05_Indian_Fighter_Aircraft": [
            "Tejas",
            "Tejas_Mk2",
            "Rafale",
            "Su30MKI",
            "Mirage_2000",
            "MiG_29",
            "AMCA",
            "Twin_Engine_Deck_Based_Fighter"
        ],

        "06_Military_Transport_and_Helicopters": [
            "C17_Globemaster",
            "C130J_Super_Hercules",
            "Chinook",
            "Apache",
            "ALH_Dhruv",
            "LUH",
            "Mi17_V5",
            "Transport_Modernization"
        ],

        "07_Naval_Platforms": [
            "Aircraft_Carriers",
            "Destroyers",
            "Frigates",
            "Corvettes",
            "Patrol_Vessels",
            "Amphibious_Ships",
            "Naval_Modernization",
            "Blue_Water_Navy"
        ],

        "08_Submarines_and_Underwater_Warfare": [
            "INS_Arihant",
            "SSBN",
            "SSN",
            "Kalvari_Class",
            "Project_75",
            "Project_75I",
            "Underwater_Drones",
            "Anti_Submarine_Warfare"
        ],

        "09_Tanks_and_Armoured_Vehicles": [
            "Arjun_Tank",
            "T90_Bhishma",
            "T72",
            "Future_Ready_Combat_Vehicle",
            "Infantry_Combat_Vehicle",
            "Light_Tanks",
            "Armoured_Recovery_Vehicles",
            "Modernization"
        ],

        "10_Drones_and_UAVs": [
            "Rustom",
            "TAPAS",
            "Heron",
            "Predator",
            "Swarm_Drones",
            "Combat_Drones",
            "Surveillance_Drones",
            "Drone_Warfare"
        ],

        "11_Electronic_Warfare": [
            "Radar_Systems",
            "Electronic_Attack",
            "Electronic_Protection",
            "Electronic_Support",
            "Jamming",
            "Signal_Intelligence",
            "Communication_Warfare",
            "Future_EW"
        ],

        "12_Cyber_and_Network_Warfare": [
            "Cyber_Command",
            "Cyber_Security",
            "Network_Centric_Warfare",
            "Military_Networks",
            "Cyber_Defence",
            "Cyber_Attacks",
            "Information_Warfare",
            "Digital_Battlefield"
        ],

        "13_Military_Satellites": [
            "GSAT_Series",
            "RISAT_Series",
            "Cartosat_Series",
            "Communication_Satellites",
            "Reconnaissance_Satellites",
            "Navigation_Satellites",
            "Military_Space_Assets",
            "Satellite_Security"
        ],

        "14_Indian_Space_Missions": [
            "Chandrayaan",
            "Mangalyaan",
            "Aditya_L1",
            "Gaganyaan",
            "AstroSat",
            "XPoSat",
            "Future_Missions",
            "Mission_Achievements"
        ],

        "15_Launch_Vehicles": [
            "PSLV",
            "GSLV",
            "LVM3",
            "SSLV",
            "Reusable_Launch_Vehicle",
            "Cryogenic_Engine",
            "Launch_Pads",
            "Future_Launch_Systems"
        ],

        "16_Anti_Satellite_and_Strategic_Systems": [
            "Mission_Shakti",
            "ASAT_Weapons",
            "Directed_Energy_Weapons",
            "Hypersonic_Systems",
            "Strategic_Forces",
            "Space_Security",
            "Emerging_Technologies",
            "Future_Capabilities"
        ],

        "17_Nuclear_Command_and_Deterrence": [
            "Nuclear_Doctrine",
            "No_First_Use",
            "Nuclear_Triad",
            "Strategic_Forces_Command",
            "Deterrence",
            "Command_Control",
            "Second_Strike_Capability",
            "Strategic_Stability"
        ],

        "18_Defence_Exercises": [
            "Yudh_Abhyas",
            "Malabar",
            "Garuda",
            "Varuna",
            "Mitra_Shakti",
            "Hand_in_Hand",
            "INDRA",
            "Exercise_Trends"
        ],

        "19_Current_Affairs_Defence_and_Space": [
            "Recent_Missile_Tests",
            "Recent_Defence_Deals",
            "Recent_Space_Missions",
            "Satellite_Developments",
            "Military_Technology_Updates",
            "Joint_Exercises",
            "Defence_Production",
            "Monthly_Current_Affairs"
        ],

        "20_UPSC_SSC_Railway_PYQ_Themes": [
            "Missile_PYQs",
            "Aircraft_PYQs",
            "Satellite_PYQs",
            "Space_Mission_PYQs",
            "Defence_Exercise_PYQs",
            "Technology_PYQs",
            "Revision_Themes",
            "High_Yield_Topics"
        ]
    }

    leaf_files = [
        "facts.json",
        "one_liner.json",
        "mcq_easy.json",
        "mcq_medium.json",
        "mcq_hard.json",
        "multiple_statement.json",
        "assertion_reason.json",
        "match_following.json",
        "fill_blanks.json",
        "true_false.json",
        "chronology.json",
        "arrange_sequence.json",
        "pair_matching.json",
        "odd_one_out.json",
        "statement_based.json",
        "source_based.json",
        "passage_based.json",
        "case_study.json",
        "short_answer.json",
        "long_answer.json",
        "pyq_upsc.json",
        "pyq_ssc.json",
        "pyq_railway.json",
        "pyq_state_pcs.json",
        "interview.json",
        "flashcards.json",
        "revision_questions.json",
        "concept_traps.json",
        "common_mistakes.json",
        "memory_hooks.json"
    ]

    os.makedirs(target_base, exist_ok=True)

    for category, topics in structure.items():

        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        print(f"[+] {category}")

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for file_name in leaf_files:

                file_path = os.path.join(topic_path, file_name)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ Defense & Space Technology structure created successfully.")
    print(f"📁 {target_base}")

if __name__ == "__main__":
    create_defense_and_space_technology_structure()