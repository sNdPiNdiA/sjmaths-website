import os
import shutil

def create_countries_capitals_currencies_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "geography-static",
        "countries-capitals-currencies"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_Asia": [
            "South_Asia",
            "East_Asia",
            "Southeast_Asia",
            "Central_Asia",
            "West_Asia",
            "Capitals_of_Asia",
            "Currencies_of_Asia",
            "Important_Facts"
        ],

        "02_Europe": [
            "Western_Europe",
            "Eastern_Europe",
            "Northern_Europe",
            "Southern_Europe",
            "European_Union_Countries",
            "Capitals_of_Europe",
            "Currencies_of_Europe",
            "Important_Facts"
        ],

        "03_Africa": [
            "North_Africa",
            "West_Africa",
            "East_Africa",
            "Central_Africa",
            "Southern_Africa",
            "Capitals_of_Africa",
            "Currencies_of_Africa",
            "Important_Facts"
        ],

        "04_North_America": [
            "North_American_Countries",
            "Central_America",
            "Caribbean_Countries",
            "Dependent_Territories",
            "Major_Countries",
            "Capitals_of_North_America",
            "Currencies_of_North_America",
            "Important_Facts"
        ],

        "05_South_America": [
            "Andean_Countries",
            "Southern_Cone",
            "Amazon_Basin_Countries",
            "Major_Countries",
            "Regional_Groupings",
            "Capitals_of_South_America",
            "Currencies_of_South_America",
            "Important_Facts"
        ],

        "06_Oceania": [
            "Australia",
            "New_Zealand",
            "Melanesia",
            "Micronesia",
            "Polynesia",
            "Capitals_of_Oceania",
            "Currencies_of_Oceania",
            "Important_Facts"
        ],

        "07_Countries_and_Capitals": [
            "World_Capitals_A_M",
            "World_Capitals_N_Z",
            "Capital_City_Changes",
            "Planned_Capitals",
            "Largest_Capitals",
            "Smallest_Capitals",
            "Frequently_Asked_Capitals",
            "Important_Facts"
        ],

        "08_Countries_and_Currencies": [
            "World_Currencies_A_M",
            "World_Currencies_N_Z",
            "Dollar_Using_Countries",
            "Euro_Using_Countries",
            "Common_Currency_Names",
            "Currency_Changes",
            "Frequently_Asked_Currencies",
            "Important_Facts"
        ],

        "09_Countries_and_Nationalities": [
            "Asian_Nationalities",
            "European_Nationalities",
            "African_Nationalities",
            "American_Nationalities",
            "Oceanian_Nationalities",
            "Demonyms",
            "Frequently_Asked",
            "Important_Facts"
        ],

        "10_Countries_and_Codes": [
            "ISO_Country_Codes",
            "Internet_Country_Codes",
            "Vehicle_Codes",
            "Olympic_Country_Codes",
            "UN_Country_Codes",
            "Airline_Country_Codes",
            "Exam_Focused_Codes",
            "Important_Facts"
        ],

        "11_Bordering_Countries": [
            "Asian_Borders",
            "European_Borders",
            "African_Borders",
            "American_Borders",
            "Indian_Neighbours",
            "Landlocked_Countries",
            "Island_Countries",
            "Important_Facts"
        ],

        "12_Countries_and_Continents": [
            "Asian_Countries",
            "European_Countries",
            "African_Countries",
            "North_American_Countries",
            "South_American_Countries",
            "Oceanian_Countries",
            "Transcontinental_Countries",
            "Important_Facts"
        ],

        "13_Countries_and_Languages": [
            "Official_Languages",
            "Most_Spoken_Languages",
            "Multilingual_Countries",
            "Language_Families",
            "Regional_Languages",
            "UN_Languages",
            "Exam_Focused_Facts",
            "Important_Facts"
        ],

        "14_Countries_and_Flags": [
            "Asian_Flags",
            "European_Flags",
            "African_Flags",
            "American_Flags",
            "Oceanian_Flags",
            "Flag_Symbolism",
            "Similar_Flags",
            "Important_Facts"
        ],

        "15_Countries_and_National_Symbols": [
            "National_Animals",
            "National_Birds",
            "National_Flowers",
            "National_Trees",
            "National_Emblems",
            "National_Mottos",
            "National_Anthems",
            "Important_Facts"
        ],

        "16_International_Groupings": [
            "G7_Countries",
            "G20_Countries",
            "BRICS_Countries",
            "SAARC_Countries",
            "ASEAN_Countries",
            "EU_Members",
            "Commonwealth_Countries",
            "Important_Facts"
        ],

        "17_Country_Superlatives": [
            "Largest_Countries",
            "Smallest_Countries",
            "Most_Populous_Countries",
            "Richest_Countries",
            "Highest_Literacy_Countries",
            "Island_Nations",
            "Landlocked_Nations",
            "Important_Facts"
        ],

        "18_Current_Affairs_Country_Facts": [
            "Capital_Changes",
            "Currency_Changes",
            "Country_Name_Changes",
            "New_Country_Facts",
            "Border_Changes",
            "International_Recognition",
            "Recent_Developments",
            "Monthly_Updates"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "Capital_Based_PYQ",
            "Currency_Based_PYQ",
            "Border_Based_PYQ",
            "Country_Code_PYQ",
            "Flag_Based_PYQ",
            "Language_Based_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Top_100_Capitals",
            "Top_100_Currencies",
            "Memory_Hooks",
            "Country_Capital_Mnemonics",
            "Flashcards",
            "Common_Mistakes",
            "Concept_Traps",
            "Rapid_Revision"
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
        "mains_10m.json",
        "mains_15m.json",
        "mains_20m.json",
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

    print(f"Creating structure in: {target_base}")

    for category, topics in structure.items():

        category_path = os.path.join(target_base, category)
        os.makedirs(category_path, exist_ok=True)

        print(f"[+] {category}")

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            print(f"    [+] {topic}")

            for filename in leaf_files:

                file_path = os.path.join(topic_path, filename)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ Countries, Capitals & Currencies structure created successfully.")
    print(f"📁 Location: {target_base}")

if __name__ == "__main__":
    create_countries_capitals_currencies_structure()