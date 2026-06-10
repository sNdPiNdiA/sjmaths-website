import os
import shutil

def create_paintings_handicrafts_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "art-and-culture", "paintings-and-handicrafts")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Fundamentals": [
            "Meaning_of_Painting", "Meaning_of_Handicrafts", "Visual_Arts_in_India",
            "Artistic_Traditions", "Sources_of_Study", "Materials_and_Techniques",
            "Patronage_of_Arts", "Cultural_Significance"
        ],
        "02_Prehistoric_and_Rock_Art": [
            "Bhimbetka_Paintings", "Rock_Shelter_Art", "Hunting_Scenes",
            "Animal_Depictions", "Symbolism", "Painting_Techniques",
            "Prehistoric_Culture", "Archaeological_Significance"
        ],
        "03_Ancient_Painting_Traditions": [
            "Ajanta_Paintings", "Bagh_Caves", "Badami_Paintings",
            "Sittanavasal_Paintings", "Ellora_Paintings", "Buddhist_Paintings",
            "Jain_Paintings", "Ancient_Murals"
        ],
        "04_Ajanta_and_Bagh_School": [
            "Ajanta_Themes", "Ajanta_Techniques", "Jataka_Depictions",
            "Royal_Life", "Bagh_Murals", "Stylistic_Features",
            "Patronage", "Artistic_Legacy"
        ],
        "05_Mural_Painting_Traditions": [
            "Kerala_Murals", "Lepakshi_Murals", "Tanjore_Murals",
            "Temple_Murals", "Palace_Murals", "Religious_Themes",
            "Regional_Styles", "Preservation"
        ],
        "06_Pala_and_Jain_Paintings": [
            "Pala_School", "Buddhist_Manuscripts", "Palm_Leaf_Paintings",
            "Jain_Manuscripts", "Western_Indian_Style", "Miniature_Traditions",
            "Religious_Art", "Artistic_Features"
        ],
        "07_Mughal_Painting": [
            "Origins_of_Mughal_Painting", "Akbar_Period", "Jahangir_Period",
            "Shahjahan_Period", "Portraiture", "Naturalism",
            "Manuscript_Illustration", "Decline_of_Mughal_Painting"
        ],
        "08_Mughal_Masters": [
            "Basawan", "Daswanth", "Abdul_Samad", "Mir_Sayyid_Ali",
            "Ustad_Mansur", "Bichitr", "Govardhan", "Important_Works"
        ],
        "09_Rajput_Painting": [
            "Origins", "Characteristics", "Religious_Themes", "Court_Scenes",
            "Nature_Depictions", "Krishna_Themes", "Regional_Variations", "Legacy"
        ],
        "10_Mewar_School": [
            "History", "Themes", "Style", "Patronage", "Krishna_Tradition",
            "Important_Works", "Artists", "Significance"
        ],
        "11_Marwar_and_Bikaner_School": [
            "Marwar_Style", "Bikaner_Style", "Themes", "Influences",
            "Patronage", "Artistic_Features", "Important_Works", "Legacy"
        ],
        "12_Bundi_and_Kota_School": [
            "Bundi_Style", "Kota_Style", "Hunting_Scenes", "Nature_Depictions",
            "Court_Life", "Techniques", "Patronage", "Legacy"
        ],
        "13_Kishangarh_and_Jaipur_School": [
            "Kishangarh_Style", "Bani_Thani", "Jaipur_Style", "Court_Paintings",
            "Religious_Themes", "Artists", "Patronage", "Legacy"
        ],
        "14_Pahari_Painting": [
            "Origins", "Basohli_School", "Guler_School", "Kangra_School",
            "Garhwal_School", "Bhakti_Themes", "Nature_Depictions", "Legacy"
        ],
        "15_Deccani_Painting": [
            "Ahmadnagar_School", "Bijapur_School", "Golconda_School",
            "Hyderabad_School", "Persian_Influence", "Court_Culture", "Themes", "Legacy"
        ],
        "16_Company_and_Modern_Painting": [
            "Company_School", "Colonial_Influence", "Raja_Ravi_Varma",
            "Bengal_School", "Abanindranath_Tagore", "Nandalal_Bose",
            "Modern_Indian_Art", "Nationalism_and_Art"
        ],
        "17_Folk_Paintings": [
            "Madhubani", "Warli", "Pattachitra", "Kalamkari", "Phad",
            "Pithora", "Sohrai", "Regional_Folk_Art"
        ],
        "18_Madhubani_Painting": [
            "History", "Themes", "Techniques", "Natural_Colours", "Styles",
            "Artists", "Cultural_Significance", "GI_Tag"
        ],
        "19_Warli_and_Tribal_Paintings": [
            "Warli_Art", "Saura_Art", "Gond_Painting", "Bhil_Painting",
            "Pithora_Art", "Tribal_Symbolism", "Materials", "Preservation"
        ],
        "20_Pattachitra_and_Kalamkari": [
            "Pattachitra_Odisha", "Pattachitra_Bengal", "Kalamkari_Srikalahasti",
            "Kalamkari_Machilipatnam", "Themes", "Techniques", "Natural_Dyes",
            "GI_Recognition"
        ],
        "21_Handicrafts_Fundamentals": [
            "Meaning_of_Handicrafts", "Craft_Traditions", "Artisan_Communities",
            "Traditional_Techniques", "Materials", "Patronage",
            "Economic_Importance", "Cultural_Value"
        ],
        "22_Textile_Handicrafts": [
            "Banarasi_Silk", "Kanchipuram_Silk", "Chanderi", "Patola",
            "Pashmina", "Bandhani", "Ikat", "Traditional_Embroidery"
        ],
        "23_Handloom_and_Weaving": [
            "Handloom_Tradition", "Jamdani", "Baluchari", "Muga_Silk",
            "Eri_Silk", "Paithani", "Tangail", "Regional_Weaving"
        ],
        "24_Pottery_and_Ceramics": [
            "Terracotta", "Blue_Pottery", "Black_Pottery", "Red_Ware",
            "Ceramic_Traditions", "Regional_Pottery", "Techniques", "Modern_Challenges"
        ],
        "25_Wood_Metal_and_Stone_Crafts": [
            "Wood_Carving", "Sandalwood_Crafts", "Bidriware", "Dhokra_Art",
            "Bell_Metal_Crafts", "Stone_Carving", "Marble_Inlay", "Regional_Crafts"
        ],
        "26_Jewellery_and_Decorative_Crafts": [
            "Meenakari", "Kundan", "Thewa", "Filigree_Work", "Lac_Crafts",
            "Ivory_Traditions", "Decorative_Arts", "Regional_Specialties"
        ],
        "27_Bamboo_Cane_and_Natural_Fibre_Crafts": [
            "Bamboo_Crafts", "Cane_Crafts", "Jute_Crafts", "Coir_Crafts",
            "Grass_Crafts", "Leaf_Crafts", "North_East_Traditions", "Sustainable_Crafts"
        ],
        "28_GI_Tags_and_Craft_Clusters": [
            "GI_Tag_Concept", "Craft_Clusters", "Madhubani_GI", "Pochampally_GI",
            "Kanchipuram_GI", "Banarasi_GI", "Regional_GI_Products", "Legal_Protection"
        ],
        "29_Institutions_and_Promotion": [
            "Lalit_Kala_Akademi", "Handicrafts_Board", "Crafts_Council_of_India",
            "Development_Commissioner_Handicrafts", "Museums", "Exhibitions",
            "Government_Schemes", "Export_Promotion"
        ],
        "30_Historiography_and_Scholarship": [
            "Art_Historiography", "Colonial_Interpretations", "Nationalist_Interpretations",
            "Modern_Research", "Archaeological_Evidence", "Source_Criticism",
            "Museum_Studies", "Conservation_Studies"
        ],
        "31_Legacy_and_Contemporary_Relevance": [
            "Cultural_Identity", "Tourism", "Creative_Economy", "Contemporary_Artists",
            "Digital_Preservation", "Global_Recognition", "Challenges", "Future_Prospects"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "image_based.json", "artist_work_matching.json",
        "passage_based.json", "source_based.json", "case_study.json",
        "short_answer.json", "long_answer.json", "mains_10m.json",
        "mains_15m.json", "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "pyq_teaching.json",
        "interview.json", "flashcards.json", "revision_questions.json",
        "concept_traps.json", "common_mistakes.json", "memory_hooks.json"
    ]

    print(f"Creating Paintings and Handicrafts structure in: {target_base}")
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
    create_paintings_handicrafts_structure()