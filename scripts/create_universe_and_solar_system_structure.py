import os
import shutil

def create_universe_and_solar_system_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "geography",
        "physical-geography",
        "universe-and-solar-system"
    )

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {

        "01_Universe_Fundamentals": [
            "Meaning_of_Universe",
            "Nature_of_Universe",
            "Components_of_Universe",
            "Scale_of_Universe",
            "Astronomy_and_Astrophysics",
            "Cosmology",
            "Importance_of_Study",
            "Sources_of_Study"
        ],

        "02_Origin_of_the_Universe": [
            "Big_Bang_Theory",
            "Steady_State_Theory",
            "Oscillating_Universe",
            "Inflation_Theory",
            "Expansion_of_Universe",
            "Evidence_for_Big_Bang",
            "Cosmic_Background_Radiation",
            "Modern_Views"
        ],

        "03_Galaxies": [
            "Meaning_of_Galaxies",
            "Types_of_Galaxies",
            "Spiral_Galaxies",
            "Elliptical_Galaxies",
            "Irregular_Galaxies",
            "Galaxy_Clusters",
            "Galaxy_Formation",
            "Examples"
        ],

        "04_Milky_Way_Galaxy": [
            "Structure_of_Milky_Way",
            "Galactic_Core",
            "Spiral_Arms",
            "Solar_System_Position",
            "Stars_in_Milky_Way",
            "Interstellar_Medium",
            "Galaxy_Dynamics",
            "Importance"
        ],

        "05_Stars": [
            "Nature_of_Stars",
            "Star_Formation",
            "Star_Classification",
            "Magnitude",
            "Luminosity",
            "Constellations",
            "Binary_Stars",
            "Variable_Stars"
        ],

        "06_Life_Cycle_of_Stars": [
            "Nebula",
            "Protostar",
            "Main_Sequence_Stars",
            "Red_Giants",
            "White_Dwarfs",
            "Neutron_Stars",
            "Supernova",
            "Black_Holes"
        ],

        "07_Celestial_Bodies": [
            "Stars",
            "Planets",
            "Dwarf_Planets",
            "Asteroids",
            "Comets",
            "Meteoroids",
            "Meteorites",
            "Natural_Satellites"
        ],

        "08_Constellations_and_Zodiac": [
            "Constellations",
            "Zodiac_Constellations",
            "Pole_Star",
            "Ursa_Major",
            "Orion",
            "Astronomical_Importance",
            "Navigation",
            "Observations"
        ],

        "09_Solar_System_Fundamentals": [
            "Origin_of_Solar_System",
            "Nebular_Hypothesis",
            "Solar_System_Components",
            "Structure",
            "Scale_of_Solar_System",
            "Planetary_Motion",
            "Solar_System_Dynamics",
            "Modern_Theories"
        ],

        "10_The_Sun": [
            "Structure_of_Sun",
            "Photosphere",
            "Chromosphere",
            "Corona",
            "Solar_Radiation",
            "Solar_Wind",
            "Sunspots",
            "Importance_of_Sun"
        ],

        "11_Inner_Planets": [
            "Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Characteristics",
            "Composition",
            "Atmospheres",
            "Comparative_Study"
        ],

        "12_Outer_Planets": [
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune",
            "Gas_Giants",
            "Ice_Giants",
            "Characteristics",
            "Comparative_Study"
        ],

        "13_Dwarf_Planets": [
            "Pluto",
            "Eris",
            "Haumea",
            "Makemake",
            "Ceres",
            "IAU_Definition",
            "Characteristics",
            "Classification"
        ],

        "14_Moons_and_Natural_Satellites": [
            "Earth_Moon",
            "Galilean_Moons",
            "Titan",
            "Triton",
            "Satellite_Formation",
            "Characteristics",
            "Orbital_Motion",
            "Importance"
        ],

        "15_Asteroids_and_Asteroid_Belt": [
            "Asteroids",
            "Asteroid_Belt",
            "Near_Earth_Asteroids",
            "Composition",
            "Origin",
            "Major_Asteroids",
            "Hazards",
            "Scientific_Importance"
        ],

        "16_Comets_and_Meteors": [
            "Comets",
            "Comet_Structure",
            "Meteor_Showers",
            "Meteoroids",
            "Meteors",
            "Meteorites",
            "Origins",
            "Importance"
        ],

        "17_Earth_as_a_Planet": [
            "Earths_Position",
            "Shape_of_Earth",
            "Size_of_Earth",
            "Rotation",
            "Revolution",
            "Unique_Features",
            "Habitability",
            "Comparative_Analysis"
        ],

        "18_Motions_of_the_Earth": [
            "Rotation",
            "Revolution",
            "Axial_Tilt",
            "Day_and_Night",
            "Seasons",
            "Leap_Year",
            "Solstices",
            "Equinoxes"
        ],

        "19_Eclipses": [
            "Solar_Eclipse",
            "Lunar_Eclipse",
            "Umbra",
            "Penumbra",
            "Types_of_Eclipses",
            "Frequency",
            "Astronomical_Significance",
            "Observations"
        ],

        "20_Time_and_Calendars": [
            "Local_Time",
            "Standard_Time",
            "Time_Zones",
            "International_Date_Line",
            "GMT",
            "UTC",
            "Calendar_Systems",
            "Applications"
        ],

        "21_Remote_Sensing_and_Satellites": [
            "Artificial_Satellites",
            "Remote_Sensing",
            "INSAT",
            "IRS_Series",
            "Communication_Satellites",
            "Navigation_Satellites",
            "Applications",
            "Space_Technology"
        ],

        "22_Space_Exploration": [
            "Space_Missions",
            "Moon_Missions",
            "Mars_Missions",
            "Space_Stations",
            "Human_Spaceflight",
            "Space_Agencies",
            "Scientific_Discoveries",
            "Future_Missions"
        ],

        "23_Indian_Space_Programme": [
            "ISRO",
            "Aryabhata",
            "Chandrayaan",
            "Mangalyaan",
            "Aditya_L1",
            "Gaganyaan",
            "Satellite_Launch_Vehicles",
            "Achievements"
        ],

        "24_Modern_Astronomy_and_Astrophysics": [
            "Dark_Matter",
            "Dark_Energy",
            "Exoplanets",
            "Gravitational_Waves",
            "Black_Holes",
            "Space_Telescopes",
            "Recent_Discoveries",
            "Future_Research"
        ],

        "25_Space_Hazards_and_Astrobiology": [
            "Space_Debris",
            "Asteroid_Impacts",
            "Solar_Storms",
            "Radiation_Hazards",
            "Astrobiology",
            "Search_for_Life",
            "Planetary_Protection",
            "Challenges"
        ],

        "26_Universe_and_Human_Civilization": [
            "Ancient_Astronomy",
            "Navigation",
            "Calendars",
            "Agriculture_and_Astronomy",
            "Scientific_Revolution",
            "Modern_Society",
            "Space_Age",
            "Future_Prospects"
        ],

        "27_Current_Affairs_and_Space_Issues": [
            "Recent_Space_Missions",
            "Space_Exploration_Updates",
            "ISRO_Missions",
            "NASA_Missions",
            "Private_Space_Companies",
            "Space_Policy",
            "Recent_Discoveries",
            "UPSC_High_Yield_Topics"
        ],

        "28_Maps_Data_and_Exam_Themes": [
            "Solar_System_Diagrams",
            "Constellation_Maps",
            "Galaxy_Maps",
            "Planetary_Data",
            "Space_Mission_Data",
            "Astronomical_Charts",
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

    print(f"Creating Universe and Solar System structure in: {target_base}")

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
    create_universe_and_solar_system_structure()