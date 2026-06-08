import re
import json

# Read the HTML content
with open('c:/Users/sande/Documents/GitHub/sjmaths-website/ahc-ro-aro/syllabus/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

top_match = re.search(r'(.*?)<!-- ==================== STAGE 1 PANEL ==================== -->', content, re.DOTALL)
bottom_match = re.search(r'(</main>.*)', content, re.DOTALL)

if not top_match or not bottom_match:
    print("Error: Could not find split points in HTML.")
    exit(1)

top_html = top_match.group(1)
bottom_html = bottom_match.group(1)

data = {
    "stage1": {
        "alert": "The Stage I (Prelims) Exam is objective-type, testing candidates' overall awareness, analytical ability, and subject knowledge. Duration: 180 Minutes. Total Questions: 200. Total Marks: 200. No negative marking.",
        "subjects": [
            {
                "title": "General Science", "link": "../general-science/", "icon": "fa-flask", "prefix": "s1c1",
                "subs": [
                    {"title": "Basic physical sciences", "items": ["Basic physical sciences (Overview)", "Units & Measurements", "Motion & Forces", "Work, Energy & Power", "Sound & Light", "Electricity & Magnetism"]},
                    {"title": "Chemical concepts", "items": ["Chemical concepts (Overview)", "Matter & its States", "Atomic Structure", "Acids, Bases & Salts", "Metals & Non-metals", "Carbon & its compounds"]},
                    {"title": "Biological processes", "items": ["Biological processes (Overview)", "Cell Biology", "Human Body Systems", "Diseases & Nutrition", "Plant Biology", "Genetics"]},
                    {"title": "Scientific applications", "items": ["Scientific applications (Overview)", "Space Technology", "Defense Technology", "Biotechnology", "IT & Communication"]}
                ]
            },
            {
                "title": "History of India", "link": "../history-of-india/", "icon": "fa-landmark-dome", "prefix": "s1c2",
                "subs": [
                    {"title": "Ancient Indian history", "items": ["Ancient Indian history (Overview)", "Pre-historic Period", "Indus Valley Civilization", "Vedic Period", "Buddhism & Jainism", "Mauryan & Gupta Empires"]},
                    {"title": "Medieval Indian era", "items": ["Medieval Indian era (Overview)", "Early Medieval India", "Delhi Sultanate", "Mughal Empire", "Vijayanagara & Bahmani", "Bhakti & Sufi Movements"]},
                    {"title": "Modern history details", "items": ["Modern history details (Overview)", "Advent of Europeans", "British Expansion", "1857 Revolt", "Social & Religious Reforms", "Economic Impact of British Rule"]},
                    {"title": "Social-economic historical milestones", "items": ["Social-economic historical milestones (Overview)", "Land Revenue Systems", "Industrialization under British", "Development of Press & Education"]}
                ]
            },
            {
                "title": "Indian National Movement", "link": "../indian-national-movement/", "icon": "fa-flag-india", "prefix": "s1c3",
                "subs": [
                    {"title": "Freedom struggle steps", "items": ["Freedom struggle steps (Overview)", "Formation of INC", "Moderate & Extremist Phases", "Swadeshi Movement", "Home Rule League"]},
                    {"title": "Key national figures", "items": ["Key national figures (Overview)", "Mahatma Gandhi", "Subhash Chandra Bose", "Bhagat Singh", "B.R. Ambedkar", "Sardar Patel", "J.L. Nehru"]},
                    {"title": "Anti-colonial campaigns", "items": ["Anti-colonial campaigns (Overview)", "Non-Cooperation Movement", "Civil Disobedience Movement", "Quit India Movement", "INA & RIN Mutiny"]},
                    {"title": "Rise of nationalism", "items": ["Rise of nationalism (Overview)", "Role of Press & Literature", "Impact of Western Education", "Peasant & Tribal Uprisings"]}
                ]
            },
            {
                "title": "Indian Polity, Economy & Culture", "link": "../polity-economy-culture/", "icon": "fa-building-columns", "prefix": "s1c4",
                "subs": [
                    {"title": "Constitutional framework", "items": ["Constitutional framework (Overview)", "Constituent Assembly", "Preamble", "Fundamental Rights & Duties", "DPSP", "Amendment Process"]},
                    {"title": "Administrative structures", "items": ["Administrative structures (Overview)", "Union Executive & Legislature", "State Executive & Legislature", "Supreme & High Courts", "Panchayati Raj & Municipalities"]},
                    {"title": "Economic development models", "items": ["Economic development models (Overview)", "Five Year Plans", "NITI Aayog", "Poverty Alleviation Programs", "Banking & RBI"]},
                    {"title": "Cultural arts & heritage", "items": ["Cultural arts & heritage (Overview)", "Indian Architecture (Temple & Islamic)", "Classical & Folk Dances", "Indian Music & Paintings", "UNESCO World Heritage Sites"]}
                ]
            },
            {
                "title": "Agriculture, Commerce & Trade", "link": "../agriculture-commerce-trade/", "icon": "fa-tractor", "prefix": "s1c5",
                "subs": [
                    {"title": "Agricultural systems", "items": ["Agricultural systems (Overview)", "Types of Farming", "Major Crops (Food, Cash, Plantation)", "Green Revolution", "Allied Revolutions"]},
                    {"title": "Crop production patterns", "items": ["Crop production patterns (Overview)", "Kharif, Rabi, & Zaid Seasons", "Soil Types of India", "Irrigation Systems"]},
                    {"title": "Internal & external trade", "items": ["Internal & external trade (Overview)", "Foreign Trade Policy", "Balance of Payments", "Major Exports & Imports", "Trade Corridors"]},
                    {"title": "Commercial sectors", "items": ["Commercial sectors (Overview)", "MSMEs", "Heavy Industries", "Special Economic Zones (SEZs)", "E-commerce & Digital Economy"]}
                ]
            },
            {
                "title": "Population & Ecology", "link": "../population-ecology-urbanisation/", "icon": "fa-tree-city", "prefix": "s1c6",
                "subs": [
                    {"title": "Indian population dynamics", "items": ["Indian population dynamics (Overview)", "Census 2011 Highlights", "Population Growth Trends", "Demographic Dividend", "Literacy & Sex Ratio"]},
                    {"title": "Ecological balances", "items": ["Ecological balances (Overview)", "Ecosystems & Biomes", "Biodiversity Hotspots in India", "Food Chains & Webs"]},
                    {"title": "Environmental protection trends", "items": ["Environmental protection trends (Overview)", "Climate Change & Global Warming", "Pollution Control", "National Parks & Sanctuaries", "International Treaties"]},
                    {"title": "Urban planning challenges", "items": ["Urban planning challenges (Overview)", "Smart Cities Mission", "Slum Redevelopment", "Solid & E-Waste Management", "Urban Transport"]}
                ]
            },
            {
                "title": "World & Indian Geography", "link": "../geography/", "icon": "fa-earth-americas", "prefix": "s1c7",
                "subs": [
                    {"title": "Physical features of world", "items": ["Physical features of world (Overview)", "Continents & Major Oceans", "Mountains, Plateaus & Plains", "Major Rivers & Lakes", "Climatology"]},
                    {"title": "Natural resources of India", "items": ["Natural resources of India (Overview)", "Mineral Resources (Coal, Iron, Bauxite)", "Energy Resources (Solar, Wind, Fossil)"]},
                    {"title": "Indian geographical divisions", "items": ["Indian geographical divisions (Overview)", "The Himalayas", "Northern Plains", "Peninsular Plateau", "Coastal Plains & Islands"]},
                    {"title": "Resource utilization schemes", "items": ["Resource utilization schemes (Overview)", "Multipurpose River Valley Projects", "Water Conservation Schemes", "Interlinking of Rivers"]}
                ]
            },
            {
                "title": "Current Affairs", "link": "../current-affairs/", "icon": "fa-newspaper", "prefix": "s1c8",
                "subs": [
                    {"title": "National current events", "items": ["National current events (Overview)", "Important Government Schemes", "National Summits & Conferences", "Bills & Acts Passed"]},
                    {"title": "International bilateral events", "items": ["International bilateral events (Overview)", "India's Foreign Relations", "International Organizations (UN, G20, BRICS)", "Global Treaties"]},
                    {"title": "Key administrative appointments", "items": ["Key administrative appointments (Overview)", "Constitutional Posts (CAG, CEC)", "Heads of National Institutions", "Chief Justices & Ambassadors"]},
                    {"title": "Sports and awards", "items": ["Sports and awards (Overview)", "Olympics & Paralympics", "Asian Games & World Cups", "Nobel Prizes", "Bharat Ratna & Padma Awards"]}
                ]
            },
            {
                "title": "General Aptitude", "link": "../general-aptitude/", "icon": "fa-brain", "prefix": "s1c9",
                "subs": [
                    {"title": "Logical reasoning steps", "items": ["Logical reasoning steps (Overview)", "Syllogism", "Blood Relations", "Direction Sense", "Coding-Decoding", "Order & Ranking"]},
                    {"title": "Analytical interpretation", "items": ["Analytical interpretation (Overview)", "Statement & Assumptions", "Data Sufficiency", "Venn Diagrams", "Non-Verbal Reasoning"]},
                    {"title": "Mathematical puzzles", "items": ["Mathematical puzzles (Overview)", "Number Series", "Alphabet Series", "Missing Characters", "Seating Arrangement"]},
                    {"title": "Problem-solving metrics", "items": ["Problem-solving metrics (Overview)", "Time & Work", "Speed, Distance & Time", "Percentages & Averages", "Profit & Loss"]}
                ]
            },
            {
                "title": "UP Special Knowledge", "link": "../up-special-knowledge/", "icon": "fa-map-location-dot", "prefix": "s1c10",
                "subs": [
                    {"title": "UP state educational systems", "items": ["UP state educational systems (Overview)", "Major Universities & Institutes", "Primary & Secondary Schemes", "Literacy rate in UP"]},
                    {"title": "Cultural traditions of UP", "items": ["Cultural traditions of UP (Overview)", "Fairs & Festivals (Kumbh, Taj Mahotsav)", "Folk Dances & Songs", "Historical Monuments & Tourism"]},
                    {"title": "UP agricultural profiles", "items": ["UP agricultural profiles (Overview)", "Major Crops & Fruits of UP", "Irrigation Canals & Rivers", "Soil Profile of UP"]},
                    {"title": "Industry, trade & living standards", "items": ["Industry, trade & living standards (Overview)", "One District One Product (ODOP)", "Major Industrial Corridors", "UP Budget & Economy", "MSMEs in UP"]}
                ]
            },
            {
                "title": "Graduation Level English & Hindi", "link": "../english/", "icon": "fa-language", "prefix": "s1c11",
                "subs": [
                    {"title": "General English grammar", "items": ["General English grammar (Overview)", "Parts of Speech", "Tenses & Conditionals", "Active & Passive Voice", "Direct & Indirect Speech"]},
                    {"title": "General Hindi syntax", "items": ["General Hindi syntax (Overview)", "वर्णमाला (Varnamala)", "संधि (Sandhi) व समास (Samas)", "कारक (Karak)", "वाक्य शुद्धि (Sentence Correction)"]},
                    {"title": "Vocabulary usage", "items": ["Vocabulary usage (Overview)", "Synonyms & Antonyms (पर्यायवाची/विलोम)", "Idioms & Phrases (मुहावरे)", "One-word Substitution", "Spellings"]},
                    {"title": "Comprehension abilities", "items": ["Comprehension abilities (Overview)", "Reading Comprehension (English)", "अपठित गद्यांश (Hindi)", "Cloze Test"]}
                ]
            },
            {
                "title": "Computer Knowledge", "link": "../computer-knowledge/", "icon": "fa-desktop", "prefix": "s1c12",
                "subs": [
                    {"title": "Hardware configurations", "items": ["Hardware configurations (Overview)", "Input/Output Devices", "CPU Architecture & Registers", "Memory Types (RAM/ROM/Storage)"]},
                    {"title": "Software system types", "items": ["Software system types (Overview)", "Operating Systems (Windows/Linux)", "Utility & System Software", "Application Software"]},
                    {"title": "Internet applications", "items": ["Internet applications (Overview)", "Web Browsers & Search Engines", "Email Protocols (SMTP/POP/IMAP)", "Networking Basics (LAN/WAN)"]},
                    {"title": "Basic processing units", "items": ["Basic processing units (Overview)", "MS Office Suite (Word, Excel, PowerPoint)", "Shortcut Keys", "Basic Cyber Security & Viruses"]}
                ]
            }
        ]
    },
    "stage2": {
        "alert": "<strong>Stage II (Mains) Syllabus:</strong> A descriptive test conducted to evaluate candidates' writing ability, language proficiency, comprehension skills, and analytical thinking. Max marks: 150. Minimum qualifying marks: 50.",
        "subjects": [
            {
                "title": "Section A: Essay Writing", "link": "../mains-essay/", "icon": "fa-pen-nib", "prefix": "s2c1",
                "subs": [
                    {"title": "Essay Categories", "items": ["Constitutional & Legal Topics", "Socio-Economic Issues (Poverty, Unemployment)", "Current National & International Affairs", "Science, Tech & Environmental Issues"]},
                    {"title": "Evaluation Parameters", "items": ["Constitutional accuracy checks", "Conceptual clarity parameters", "Coherent logical layouts", "Language proficiency flow"]}
                ]
            },
            {
                "title": "Section B: Precis Writing", "link": "../mains-precis/", "icon": "fa-compress", "prefix": "s2c2",
                "subs": [
                    {"title": "Writing Techniques", "items": ["Title Formulation & Central Theme", "Skimming & Keyword Extraction", "Maintaining one-third length"]},
                    {"title": "Evaluation Parameters", "items": ["Core idea extraction", "Symmetry and conciseness", "Proportional paragraph reduction", "Grammar & clarity checks"]}
                ]
            },
            {
                "title": "Section C: Translation", "link": "../mains-translation/", "icon": "fa-language", "prefix": "s2c3",
                "subs": [
                    {"title": "Translation Types", "items": ["English to Hindi translation", "Hindi to English translation", "Drafting official letters & circulars"]},
                    {"title": "Evaluation Parameters", "items": ["English to Hindi mapping", "Hindi to English mapping", "Exact terminology usage", "Formal translation tone"]}
                ]
            },
            {
                "title": "Section D: Comprehension", "link": "../mains-comprehension/", "icon": "fa-book-open", "prefix": "s2c4",
                "subs": [
                    {"title": "Question Types", "items": ["Answering specific factual questions", "Theme & Inference identification", "Vocabulary & Synonym matching"]},
                    {"title": "Evaluation Parameters", "items": ["Response accuracy metrics", "Analytical context extraction", "Clear expressive statements"]}
                ]
            }
        ]
    },
    "stage3": {
        "alert": "<strong>Stage III (Computer Knowledge Test)</strong> assesses candidates' practical computer skills and typing proficiency. The test focuses on speed, accuracy, formatting, and efficient text reproduction. Max marks: 50. Minimum qualifying marks: 25. Time: 20 Minutes.",
        "subjects": [
            {
                "title": "Computer Typing Skill", "link": "../computer-knowledge/", "icon": "fa-keyboard", "prefix": "s3c1",
                "subs": [
                    {"title": "Skill Requirements", "items": ["Touch Typing basics & Home Row Practice", "Punctuation & Shift key efficiency", "Handling special characters & numbers"]},
                    {"title": "Evaluation Metrics", "items": ["Reproducing 500-word text", "Formatting preservation guidelines", "Keyboard layout precision", "Target typing speed metrics"]}
                ]
            }
        ]
    }
}

def generate_html():
    html = top_html
    
    stages = [
        ("stage1", "STAGE 1 PANEL", "active"),
        ("stage2", "STAGE 2 PANEL", ""),
        ("stage3", "STAGE 3 PANEL", "")
    ]
    
    for stage_id, panel_comment, active_class in stages:
        stage_data = data[stage_id]
        active_str = f" {active_class}" if active_class else ""
        html += f"\n<!-- ==================== {panel_comment} ==================== -->\n"
        html += f'<div class="tab-panel{active_str}" id="panel-{stage_id}">\n'
        html += f'<div class="syllabus-intro-alert">\n<i class="fas fa-circle-info"></i>\n<div>\n{stage_data["alert"]}\n</div>\n</div>\n'
        html += '<div class="subjects-grid">\n\n'
        
        for subj in stage_data["subjects"]:
            html += f'<!-- {subj["title"]} -->\n'
            html += '<div class="subject-card">\n'
            html += f'<h2 class="subject-title">\n<a href="{subj["link"]}">{subj["title"]} <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>\n<i class="fas {subj["icon"]}"></i>\n</h2>'
            html += '<div class="card-scrollable">\n'
            
            for idx, sub in enumerate(subj["subs"]):
                open_attr = " open" if idx == 0 else ""
                html += f'<details class="syllabus-subsection" data-grp-idx="{idx}" data-prefix="{subj["prefix"]}"{open_attr}><summary class="subsection-summary"><span class="subsection-title">{sub["title"]}</span><div class="subsection-meta"><span class="subsection-progress" id="{subj["prefix"]}-prog-{idx}">0/0</span><i class="fas fa-chevron-down toggle-icon"></i></div></summary><ul class="syllabus-list">\n'
                
                for item_idx, item in enumerate(sub["items"]):
                    cb_id = f'{subj["prefix"]}-cb-{idx}-{item_idx}'
                    html += f'<li class="syllabus-item"><input class="syllabus-checkbox" id="{cb_id}" type="checkbox"/><span class="syllabus-text"><a class="syllabus-link" href="{subj["link"]}" style="color: inherit; text-decoration: none; border-bottom: 1px dashed rgba(142, 68, 173, 0.3); transition: all 0.2s;">{item}</a></span></li>\n'
                    
                html += '</ul>\n</details>\n'
            
            html += '</div></div>\n\n'
            
        html += '</div>\n</div>\n'
        
    html += bottom_html
    return html

final_html = generate_html()
with open('c:/Users/sande/Documents/GitHub/sjmaths-website/ahc-ro-aro/syllabus/index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print("Successfully updated index.html with explicitly restored microtopics!")