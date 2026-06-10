import os
import shutil

def create_architecture_sculpture_structure():
    # Calculate target path relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    target_base = os.path.join(project_root, "gs-question-bank", "history", "art-and-culture", "architecture-and-sculpture")

    # Delete older folders if they exist to ensure a clean state
    if os.path.exists(target_base):
        print(f"Cleaning up older folders in: {target_base}")
        shutil.rmtree(target_base)

    # Mapping of categories to their respective topics
    structure = {
        "01_Fundamentals": [
            "Meaning_of_Architecture", "Meaning_of_Sculpture", "Evolution_of_Indian_Architecture",
            "Evolution_of_Indian_Sculpture", "Building_Materials", "Architectural_Terminology",
            "Sculptural_Terminology", "Sources_of_Study"
        ],
        "02_Indus_Valley_Architecture": [
            "Urban_Planning", "Great_Bath", "Granaries", "Dockyard_of_Lothal",
            "Drainage_System", "Residential_Architecture", "Public_Buildings",
            "Architectural_Legacy"
        ],
        "03_Mauryan_Architecture": [
            "Mauryan_Polish", "Ashokan_Pillars", "Lion_Capital", "Barabar_Caves",
            "Rock_Cut_Architecture", "Stupa_Beginnings", "Palace_Architecture",
            "Mauryan_Legacy"
        ],
        "04_Stupa_Architecture": [
            "Components_of_Stupa", "Sanchi_Stupa", "Bharhut_Stupa", "Amaravati_Stupa",
            "Dhamek_Stupa", "Evolution_of_Stupas", "Symbolism", "Stupa_Tradition"
        ],
        "05_Chaitya_and_Vihara": [
            "Chaitya_Architecture", "Vihara_Architecture", "Karle_Chaitya",
            "Bhaja_Caves", "Ajanta_Viharas", "Buddhist_Monastic_Architecture",
            "Evolution_of_Chaityas"
        ],
        "06_Rock_Cut_Architecture": [
            "Ajanta", "Ellora", "Elephanta", "Udayagiri_Caves", "Badami_Caves",
            "Kanheri_Caves", "Cave_Temple_Tradition", "Rock_Cut_Techniques"
        ],
        "07_Temple_Architecture_Fundamentals": [
            "Temple_Components", "Garbhagriha", "Mandapa", "Shikhara",
            "Vimana", "Gopuram", "Temple_Symbolism", "Temple_Planning"
        ],
        "08_Nagara_Style": [
            "Characteristics", "Latina_Type", "Sekhari_Type", "Bhumija_Type",
            "Khajuraho_Group", "Sun_Temple_Konark", "Lingaraja_Temple",
            "Nagara_Evolution"
        ],
        "09_Dravida_Style": [
            "Characteristics", "Pallava_Architecture", "Chola_Architecture",
            "Brihadeeswara_Temple", "Shore_Temple", "Meenakshi_Temple",
            "Gopuram_Tradition", "Dravida_Evolution"
        ],
        "10_Vesara_Style": [
            "Characteristics", "Chalukya_Architecture", "Pattadakal",
            "Hoysala_Architecture", "Belur_Temple", "Halebidu_Temple",
            "Hybrid_Features", "Vesara_Evolution"
        ],
        "11_Buddhist_Architecture": [
            "Buddhist_Monuments", "Monasteries", "Universities", "Nalanda",
            "Vikramashila", "Mahabodhi_Temple", "Buddhist_Sacred_Architecture",
            "Legacy"
        ],
        "12_Jain_Architecture": [
            "Dilwara_Temples", "Ranakpur_Temple", "Palitana", "Shravanabelagola",
            "Jain_Caves", "Temple_Features", "Jain_Sacred_Sites", "Architectural_Legacy"
        ],
        "13_Indo_Islamic_Architecture": [
            "Characteristics", "Arches", "Domes", "Minarets", "Calligraphy",
            "Decorative_Features", "Structural_Innovations", "Evolution"
        ],
        "14_Sultanate_Architecture": [
            "Slave_Dynasty", "Khalji_Architecture", "Tughlaq_Architecture",
            "Sayyid_Architecture", "Lodi_Architecture", "Qutub_Minar",
            "Alai_Darwaza", "Architectural_Legacy"
        ],
        "15_Mughal_Architecture": [
            "Humayun_Tomb", "Fatehpur_Sikri", "Agra_Fort", "Taj_Mahal",
            "Red_Fort", "Gardens", "Mughal_Characteristics", "Mughal_Legacy"
        ],
        "16_Regional_Architecture": [
            "Kashmir_Architecture", "Bengal_Architecture", "Assam_Architecture",
            "Kerala_Architecture", "Maratha_Architecture", "Rajput_Architecture",
            "Ahom_Architecture", "Regional_Variations"
        ],
        "17_Sculpture_Fundamentals": [
            "Types_of_Sculpture", "Materials", "Techniques", "Iconography",
            "Symbolism", "Religious_Themes", "Secular_Themes", "Evolution_of_Sculpture"
        ],
        "18_Mauryan_Sculpture": [
            "Lion_Capital_Sculpture", "Yaksha_Sculptures", "Yakshi_Sculptures",
            "Pillar_Sculptures", "Mauryan_Style", "Artistic_Legacy"
        ],
        "19_Gandhara_School": [
            "Characteristics", "Greco_Buddhist_Influence", "Buddha_Images",
            "Materials", "Themes", "Major_Centers", "Legacy"
        ],
        "20_Mathura_School": [
            "Characteristics", "Buddha_Images", "Jain_Images", "Brahmanical_Images",
            "Materials", "Major_Centers", "Legacy"
        ],
        "21_Amaravati_School": [
            "Characteristics", "Narrative_Panels", "Buddhist_Themes",
            "Materials", "Artistic_Style", "Legacy"
        ],
        "22_Gupta_Sculpture": [
            "Characteristics", "Sarnath_School", "Buddha_Images",
            "Hindu_Sculpture", "Iconographic_Development", "Legacy"
        ],
        "23_Chola_Bronze_Sculpture": [
            "Lost_Wax_Technique", "Nataraja", "Bronze_Tradition",
            "Shaiva_Themes", "Vaishnava_Themes", "Legacy"
        ],
        "24_Iconography": [
            "Hindu_Iconography", "Buddhist_Iconography", "Jain_Iconography",
            "Mudras", "Attributes", "Symbolism", "Iconographic_Texts"
        ],
        "25_Archaeological_Sites_and_Monuments": [
            "UNESCO_Sites", "Protected_Monuments", "Excavated_Sites",
            "Conservation", "Restoration", "Heritage_Management", "Cultural_Significance"
        ],
        "26_Historiography": [
            "Architectural_Studies", "Sculptural_Studies", "Art_Historical_Methods",
            "Colonial_Scholarship", "Modern_Research", "Interpretation_Debates"
        ],
        "27_Legacy_and_Significance": [
            "Cultural_Legacy", "Religious_Legacy", "Artistic_Legacy",
            "Architectural_Legacy", "Global_Influence", "Heritage_Value"
        ]
    }

    # Standard dataset files for every leaf folder
    leaf_files = [
        "facts.json", "one_liner.json", "mcq_easy.json", "mcq_medium.json",
        "mcq_hard.json", "multiple_statement.json", "assertion_reason.json",
        "match_following.json", "fill_blanks.json", "true_false.json",
        "chronology.json", "arrange_sequence.json", "pair_matching.json",
        "odd_one_out.json", "map_based.json", "image_based.json",
        "monument_based.json", "sculpture_based.json", "source_based.json",
        "passage_based.json", "case_study.json", "short_answer.json",
        "long_answer.json", "mains_10m.json", "mains_15m.json",
        "mains_20m.json", "pyq_upsc.json", "pyq_ssc.json",
        "pyq_railway.json", "pyq_state_pcs.json", "pyq_teaching.json",
        "interview.json", "flashcards.json", "revision_questions.json",
        "concept_traps.json", "common_mistakes.json", "memory_hooks.json"
    ]

    print(f"Creating Architecture and Sculpture structure in: {target_base}")
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
    create_architecture_sculpture_structure()