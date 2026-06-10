import os
import shutil

def create_organizations_structure():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    target_base = os.path.join(
        project_root,
        "gs-question-bank",
        "static-gk",
        "organizations"
    )

    if os.path.exists(target_base):
        print(f"Cleaning existing folder: {target_base}")
        shutil.rmtree(target_base)

    structure = {

        "01_United_Nations_System": [
            "United_Nations",
            "UNGA",
            "UNSC",
            "ECOSOC",
            "Trusteeship_Council",
            "International_Court_of_Justice",
            "UN_Secretariat",
            "Important_Facts"
        ],

        "02_UN_Specialized_Agencies": [
            "WHO",
            "UNESCO",
            "FAO",
            "ILO",
            "IMF",
            "World_Bank",
            "ICAO",
            "Important_Facts"
        ],

        "03_Global_Economic_Organizations": [
            "WTO",
            "OECD",
            "ADB",
            "AIIB",
            "NDB",
            "BIS",
            "GATT",
            "Important_Facts"
        ],

        "04_Regional_Organizations": [
            "SAARC",
            "ASEAN",
            "EU",
            "African_Union",
            "GCC",
            "OAS",
            "Pacific_Islands_Forum",
            "Important_Facts"
        ],

        "05_Strategic_and_Security_Organizations": [
            "NATO",
            "QUAD",
            "AUKUS",
            "SCO",
            "INTERPOL",
            "Collective_Security_Treaty_Organization",
            "Five_Eyes",
            "Important_Facts"
        ],

        "06_Brics_and_Groupings": [
            "BRICS",
            "G7",
            "G20",
            "IBSA",
            "BIMSTEC",
            "IORA",
            "MGC",
            "Important_Facts"
        ],

        "07_Indian_Constitutional_Bodies": [
            "Election_Commission",
            "Finance_Commission",
            "UPSC",
            "CAG",
            "Attorney_General",
            "National_Commission_SC",
            "National_Commission_ST",
            "Important_Facts"
        ],

        "08_Indian_Statutory_Bodies": [
            "NHRC",
            "NCPCR",
            "CIC",
            "Lokpal",
            "CVC",
            "NCW",
            "NCM",
            "Important_Facts"
        ],

        "09_Indian_Regulatory_Bodies": [
            "SEBI",
            "TRAI",
            "IRDAI",
            "PFRDA",
            "FSSAI",
            "CCI",
            "AERA",
            "Important_Facts"
        ],

        "10_Indian_Financial_Institutions": [
            "RBI",
            "NABARD",
            "SIDBI",
            "EXIM_Bank",
            "NHB",
            "NITI_Aayog",
            "IFCI",
            "Important_Facts"
        ],

        "11_Science_and_Space_Organizations": [
            "ISRO",
            "DRDO",
            "BARC",
            "CSIR",
            "ICMR",
            "INCOIS",
            "Antrix",
            "Important_Facts"
        ],

        "12_Defence_Organizations": [
            "Indian_Army",
            "Indian_Navy",
            "Indian_Air_Force",
            "Coast_Guard",
            "NCC",
            "Territorial_Army",
            "Strategic_Forces_Command",
            "Important_Facts"
        ],

        "13_Agriculture_and_Rural_Organizations": [
            "ICAR",
            "NDDB",
            "NAFED",
            "KVIC",
            "NCDC",
            "SFAC",
            "APEDA",
            "Important_Facts"
        ],

        "14_Environment_Organizations": [
            "UNEP",
            "IUCN",
            "WWF",
            "IPCC",
            "National_Biodiversity_Authority",
            "Forest_Survey_of_India",
            "Central_Pollution_Control_Board",
            "Important_Facts"
        ],

        "15_Media_and_Communication_Organizations": [
            "Prasar_Bharati",
            "Press_Council_of_India",
            "PTI",
            "UNI",
            "Doordarshan",
            "AIR",
            "Broadcasting_Authorities",
            "Important_Facts"
        ],

        "16_Sports_Organizations": [
            "IOC",
            "BCCI",
            "ICC",
            "FIFA",
            "AIFF",
            "SAI",
            "Olympic_Association",
            "Important_Facts"
        ],

        "17_Educational_and_Cultural_Organizations": [
            "UGC",
            "AICTE",
            "NCERT",
            "NAAC",
            "IGNOU",
            "Sahitya_Akademi",
            "Lalit_Kala_Akademi",
            "Important_Facts"
        ],

        "18_Current_Affairs_Organizations": [
            "Recent_Summits",
            "Recent_Reports",
            "New_Memberships",
            "Leadership_Changes",
            "Global_Initiatives",
            "Indian_Initiatives",
            "Recent_Developments",
            "Monthly_Updates"
        ],

        "19_UPSC_SSC_Railway_PYQ_Themes": [
            "UN_PYQ",
            "International_Organizations_PYQ",
            "Indian_Bodies_PYQ",
            "Regulatory_Bodies_PYQ",
            "Financial_Institutions_PYQ",
            "Science_Organizations_PYQ",
            "Revision",
            "High_Yield_Areas"
        ],

        "20_Revision_and_Memory_Techniques": [
            "Organization_Headquarters",
            "Founding_Years",
            "Founders",
            "Membership",
            "Memory_Hooks",
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

        for topic in topics:

            topic_path = os.path.join(category_path, topic)
            os.makedirs(topic_path, exist_ok=True)

            for filename in leaf_files:

                file_path = os.path.join(topic_path, filename)

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("[]")

    print("\n✅ Organizations structure created successfully.")
    print(f"📁 {target_base}")

if __name__ == "__main__":
    create_organizations_structure()