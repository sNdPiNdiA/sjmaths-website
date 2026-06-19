import os
import re

# Define the output path
HTML_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\index.html"

# Ensure directory exists
os.makedirs(os.path.dirname(HTML_PATH), exist_ok=True)

# Data structures for micro-topics
ancient_history = [
    {
        "subsection": "Prehistory",
        "items": [
            "Prehistoric Time Periods",
            "Sources of Information of Pre-History",
            "History of Paleolithic or Old Stone Age",
            "History of Mesolithic or Middle Stone Age",
            "History of Neolithic Age or New Stone Age",
            "History of Chalcolithic Age",
            "History of Early Iron Age",
            "Geographical Distribution and Characteristics of Pre-History"
        ]
    },
    {
        "subsection": "Harappan/Indus Valley Civilisation",
        "items": [
            "Phases of Evolution of Harappan Civilisation",
            "Geography and Archaeological Findings of Indus Valley Civilisation",
            "Important Urban Towns",
            "Town Planning",
            "Socio-Cultural Aspects of Indus Valley Civilisation",
            "Script and Language",
            "Crafts",
            "Religions",
            "Seals and Images",
            "Economic Aspects of Indus Valley Civilisation",
            "Harappan Trade",
            "Agriculture",
            "Domestication of animals",
            "Weights and Measures",
            "Decline of Harappan Civilisation",
            "Theories on Causes of Decline"
        ]
    },
    {
        "subsection": "History of Early Vedic/Rigvedic Period",
        "items": [
            "Sources for Information about Vedic Society and Culture",
            "Extent and Geography of the Rig Vedic Period",
            "Evolution of Political Organisation",
            "Societal Setup",
            "Economic Aspects",
            "Issues Concerning Religion and Culture"
        ]
    },
    {
        "subsection": "History of Later Vedic Period",
        "items": [
            "Extent and Geography of the Later Vedic Period",
            "Development of Early Political Organisation",
            "Social Organisation and Hierarchy",
            "Economic Activities",
            "Issues Concerning Religion and Culture"
        ]
    },
    {
        "subsection": "History of South India: The Sangam Dynasties",
        "items": [
            "Sangam Literature",
            "Cholas",
            "Cheras",
            "Pandyas",
            "Aspects of Sangam Administration",
            "Aspects of Sangam Society",
            "Aspects of Sangam Economy",
            "Aspects of Sangam Religion",
            "Aspects of Sangam Culture",
            "Dynasties of Foreign Origin",
            "Trade and Commerce with the Outside World",
            "Art and Architecture"
        ]
    },
    {
        "subsection": "Jainism and Buddhism",
        "items": [
            "Factors Responsible for their Advent",
            "Jainism: Birth and Life of Mahavira (540- 468 B.C.)",
            "Tirthankaras of Jainism",
            "Teachings of Mahavira",
            "Important Tenets of Jainism",
            "Five Doctrines of Jainism",
            "Three Jewels of Jainism",
            "Organizational Setup and Sects of Jainism",
            "Jain Councils",
            "Literature of Jainism",
            "Jain Architecture",
            "Associated Terminology",
            "Overall Contribution",
            "Buddhism: Birth and Life of Buddha (563-483 BC) & Great Events",
            "Teachings of Buddha",
            "3 Jewels (Buddhism)",
            "4 Noble Truths (Buddhism)",
            "5 Principles (Buddhism)",
            "8-fold Path (Buddhism)",
            "Concept of Bodhisattvas",
            "Organisation (Sangha) and Sects of Buddhism",
            "Buddhist Councils",
            "Spread of Buddhism and Royal Patronage",
            "Literary Sources of Buddhism",
            "3 Pittakas",
            "Causes for the Decline (Buddhism)",
            "Overall Contribution of Buddhism"
        ]
    },
    {
        "subsection": "Age of Mahajanapadas (Pre-Mauryan Period)",
        "items": [
            "Polity: Republics and Monarchies",
            "The 16 Mahajanapadas",
            "Rise of Magadha",
            "Haryanka dynasty",
            "Shishunaga Dynasty",
            "Nanda Dynasty",
            "Persian Invasions",
            "Alexander’s Invasion",
            "Society and Rise of Cities/Towns",
            "Economy during Mahajanapadas Period",
            "Administrative Setup"
        ]
    },
    {
        "subsection": "Mauryan Empire",
        "items": [
            "Sources of Information: Inscriptions",
            "Sources of Information: Coins and Sites",
            "Sources of Information: Literary Sources (Indian Texts and Travellers Account)",
            "Political History of the Mauryas",
            "Chandragupta",
            "Bindusara",
            "Ashoka and His Successors",
            "Ashoka’s Inscriptions and Sites",
            "Ashokan Reign",
            "Ashoka and Buddhism",
            "Ashoka Policy of Dhamma",
            "Aspects of Mauryan Economy",
            "Aspects of Mauryan Polity",
            "Administration (Important Offices)",
            "Society",
            "Foreign Relations",
            "Decline of the Mauryas"
        ]
    },
    {
        "subsection": "History of Post Mauryan Period",
        "items": [
            "Shungas",
            "Kanvas",
            "Chedis",
            "Satavahanas",
            "Indo-Greeks",
            "Parthians",
            "Sakas",
            "Kushans (Kanishka’s Rule)"
        ]
    },
    {
        "subsection": "History of Gupta Age (Golden Age)",
        "items": [
            "Sources of Information about Gupta Period",
            "Important Gupta Kings: Srigupta",
            "Important Gupta Kings: Chandragupta I",
            "Important Gupta Kings: Samudragupta",
            "Important Gupta Kings: Chandragupta II",
            "Important Gupta Kings: Kumaragupta I",
            "Important Gupta Kings: Skandagupta",
            "Decline of Guptas",
            "Aspects of Gupta Rule: Administration",
            "Aspects of Gupta Rule: Economy",
            "Aspects of Gupta Rule: Society",
            "Aspects of Gupta Rule: Religion and Culture",
            "Aspects of Gupta Rule: Art and Architecture",
            "Aspects of Gupta Rule: Literature",
            "Foreign Travellers and their Accounts",
            "Urban centers in Gupta Period",
            "Development of Science and Technology",
            "Later Guptas",
            "Other Important Dynasties"
        ]
    },
    {
        "subsection": "Harshvardhan and Southern Dynasties in 7th Century India",
        "items": [
            "Military Conquests of Harshvardhan",
            "Administration (Harsha)",
            "Economy (Harsha)",
            "Society and Culture (Harsha)",
            "Religion (Harsha)",
            "Harsha and Buddhism",
            "Art and Architecture (Harsha)",
            "Pallavas of Kanchi and Chalukyas of Badami",
            "Administration (Pallavas & Chalukyas)",
            "Economy (Pallavas & Chalukyas)",
            "Society and Culture (Pallavas & Chalukyas)",
            "Religion (Pallavas & Chalukyas)",
            "Art and Architecture (Pallavas & Chalukyas)"
        ]
    }
]

medieval_history = [
    {
        "subsection": "Early Medieval Period (750-1200) and Dynasties",
        "items": [
            "The Pratiharas",
            "The Palas",
            "The Tripartite Conflict",
            "The Senas",
            "The Rajputs",
            "Rashtrakutas",
            "Indian Feudalism",
            "Administration",
            "Economy",
            "Society and Culture",
            "Art and Architecture",
            "Cholas Dynasty",
            "The Cheras",
            "The Yadavas",
            "Contact with South-East Asia"
        ]
    },
    {
        "subsection": "Islamic Invasions",
        "items": [
            "Invasion of Mohd Bin Qasim",
            "Invasion of Mahmud of Ghazni",
            "Invasion of Muhammad Ghuri"
        ]
    },
    {
        "subsection": "The Delhi Sultanate",
        "items": [
            "Slave Dynasty: Qutubuddin Aibak",
            "Slave Dynasty: Iltutmish",
            "Slave Dynasty: Rajia Sultan",
            "Slave Dynasty: Ghiyasuddin Balban",
            "Various Aspects of Rule under Slaves",
            "Khilji Dynasty: Jalaluddin Khilji",
            "Khilji Dynasty: Alauddin Khilji",
            "Various Aspects of Rule under Khiljis",
            "Tughlaq Dynasty: Ghiyasuddin Tughlaq",
            "Tughlaq Dynasty: Mohd. Bin Tughlaq",
            "Tughlaq Dynasty: Firuz Shah Tughlaq",
            "Various Aspects of Rule under Tughlaqs",
            "Provincial Kingdoms and Resistance by Indian Chiefs",
            "Sayyid Dynasty (1414-1451 AD)",
            "Lodhi Dynasty: Behlul Lodhi",
            "Lodhi Dynasty: Sikander Lodhi",
            "Lodhi Dynasty: Ibrahim Lodhi",
            "Administration under Delhi Sultanate",
            "Economy: Various Initiative by Different Kings",
            "Military and Attacks by Mongols and other Turks",
            "Society and Culture (Delhi Sultanate)",
            "Decline of the Sultanate"
        ]
    },
    {
        "subsection": "Mughal Rule",
        "items": [
            "Babur: First Battle of Panipat",
            "Babur: Challenges after the Battle of Panipat",
            "Babur: Struggle with Rana Sanga",
            "Babur: Problems of the Eastern Areas and the Afghans",
            "Babur’s Contribution and Significance of his Advent",
            "Humayun and the Afghans",
            "Humayun: Early Activities and Tussle with Bahadur Shah",
            "Humayun: The Gujarat Campaign",
            "Humayun: The Bengal Campaign and Struggle with Sher Khan",
            "Social and Political Background of Bihar and Rise of Sher Shah",
            "The Sur Empire (1540-56)",
            "Sher Shah Suri Contribution: Coinage",
            "Sher Shah Suri Contribution: Architecture",
            "Akbar: Conflict with the Afghans - Hemu",
            "Akbar: 2nd Battle of Panipat",
            "Akbar: Battle of Haldighati",
            "Akbar Early Expansion: Early Expansion of the Empire (1560-76)",
            "Akbar Expansion: Relations with the Rajputs",
            "Akbar Expansion: Rebellions and Northwest Expansion",
            "Akbar Expansion: Concept of Suzerainty",
            "Akbar Administration: Central and Provincial Administration",
            "Akbar Administration: Land-Revenue System",
            "Akbar Administration: The Dahsala System",
            "Akbar Administration: The Mansabdari System",
            "Akbar Administration: Other Aspects of Administration",
            "Akbar Administration: Concept of Navaratnas",
            "Akbar Socio-Religious Initiatives: Relations with the Ulama and Social Reforms",
            "Akbar Socio-Religious: The First Phase (1556-73)",
            "Akbar Socio-Religious: The Second Phase (1573-80) - the Ibadat Khana",
            "Akbar Socio-Religious: The Final Phase - Din-i-Ilahi",
            "Jahangir: Territorial Consolidation and Expansion (Mewar, East India, Kangra)",
            "Jahangir: Arrival of British Envoys in Jahangir’s Court",
            "Jahangir: State and Religion in the First Half of the 17th Century",
            "Shah Jahan: Development of Art and Architecture",
            "Shah Jahan: Evolution of the Mughal Ruling Class and the Mansabdari System",
            "Aurangzeb: Expansion of Empire",
            "Aurangzeb and the Deccani States (1658-87)",
            "Aurangzeb Deccani States: Treaty of Purandar (1665)",
            "Aurangzeb: Marathas and the Deccan (1687-1707)",
            "Aurangzeb: Assessment of Aurangzeb and the Jagirdari Crisis",
            "Later Mughals: Bahadur Shah (Shah-i-Bekhabar)",
            "Later Mughals: Jahandar Shah",
            "Later Mughals: Farrukhsiyar",
            "Later Mughals: Rafi-ud-Darajat",
            "Later Mughals: Rafi-ud-Daula (Shah Jahan II)",
            "Later Mughals: Muhammad Shah (Rangeela)",
            "Later Mughals: Ahmad Shah",
            "Later Mughals: Alamgir II",
            "Later Mughals: Shah Jahan III",
            "Later Mughals: Shah Alam II",
            "Later Mughals: Akbar II",
            "Later Mughals: Bahadur Shah II/ Zafar",
            "Later Mughals: Rise of Regional States and Foreign Invasions (1725-48)",
            "Mughal Economy: Inland Trade",
            "Mughal Economy: Overseas Trade and Role of Foreign Trading Companies",
            "Mughal Economy: Overland Trade",
            "Mughal Economy: The Mughal State and Commerce",
            "Mughal Economy: Trend of India’s Economy in First Half of 18th Century",
            "Mughal Society: Rural Society",
            "Mughal Society: Towns and Town Life",
            "Mughal Society: Artisans and Master-Craftsmen",
            "Mughal Society: Women",
            "Mughal Society: Servants and Slaves",
            "Mughal Society: Standard of Living",
            "Mughal Society: The Ruling Classes",
            "Mughal Society: The Middle Strata",
            "Mughal Society: The Commercial Classes"
        ]
    },
    {
        "subsection": "Rise of the Marathas",
        "items": [
            "The Marathas and their Policy of Expansion",
            "The Marathas and Nizam-ul-Mulk",
            "The Maratha Advance into Gujarat and Malwa",
            "The Maratha Advance into Doab and Punjab: First Phase (1741-52)",
            "The Maratha Advance into Doab and Punjab: Second Phase (1752-61)",
            "Third Battle of Panipat",
            "Chhatrapati Shivaji",
            "The Peshwas (1713-1818)",
            "The Bhonsles",
            "The Gaekwads",
            "The Holkars",
            "The Sindhias",
            "Economy in 18th Century",
            "Social and Cultural Life (Marathas)"
        ]
    },
    {
        "subsection": "Vijaynagar Empire",
        "items": [
            "Sources of Information about Vijayanagar Empire",
            "Vijayanagar Dynasties: Sangama",
            "Vijayanagar Dynasties: Suluva",
            "Vijayanagar Dynasties: Tuluva",
            "Vijayanagar Dynasties: Aravidu",
            "Vijayanagar Administration",
            "Vijayanagar Economy",
            "Vijayanagar Social Aspects",
            "Vijayanagar Art and Architecture",
            "Vijayanagar Literature",
            "Vijayanagar: Foreign Travelers and their Accounts"
        ]
    },
    {
        "subsection": "Bahmani Kingdom",
        "items": [
            "Conflicts of the Bahmani Successor States with Vijayanagar",
            "Bahmani Social and Cultural Aspects",
            "Bahmani Art and Architecture",
            "Successor States of Bahmani Kingdom: Ahmednagar",
            "Successor States of Bahmani Kingdom: Bijapur",
            "Successor States of Bahmani Kingdom: Golconda",
            "Successor States of Bahmani Kingdom: Berar",
            "Successor States of Bahmani Kingdom: Bidar",
            "Bahmani Economy",
            "Bahmani Military"
        ]
    },
    {
        "subsection": "Bhakti and Sufi Movements",
        "items": [
            "Bhakti Movement: What was the movement about?",
            "Bhakti Movement: Causes for its formation",
            "Bhakti Movement: Features of the Movement",
            "Bhakti Movement: Associated Literature",
            "Bhakti Movement Groups: Sagun",
            "Bhakti Movement Groups: Nirgun",
            "Bhakti Movement Groups: Nayanars",
            "Bhakti Movement Groups: Alvars",
            "Bhakti Saints (Acharyas): Shankaracharya",
            "Bhakti Saints (Acharyas): Ramanujacharya",
            "Bhakti Saints (Acharyas): Nimbark",
            "Bhakti Saints (Acharyas): Madhvacharya",
            "Bhakti Saints (Acharyas): Nathpanthis (Siddhas and Yogis)",
            "Vaishnavism Saints: Ramananda",
            "Vaishnavism Saints: Kabir Das",
            "Vaishnavism Saints: Gurunanak Dev",
            "Vaishnavism Saints: Purandar Das",
            "Vaishnavism Saints: Dadu Dayal",
            "Vaishnavism Saints: Chaitanya Mahaprabhu",
            "Vaishnavism Saints: Shankardeva",
            "Vaishnavism Saints: Vallabhacharya",
            "Vaishnavism Saints: Guru Ghasidas",
            "Vaishnavism Saints: Surdas",
            "Vaishnavism Saints: Meerabai",
            "Vaishnavism Saints: Haridas",
            "Vaishnavism Saints: Namdev",
            "Vaishnavism Saints: Dhaneswar",
            "Vaishnavism Saints: Eknath",
            "Vaishnavism Saints: Tukaram",
            "Vaishnavism Saints: Ramdas",
            "Impact of Bhakti Movement",
            "Sufi Movement: Causes of Creation",
            "Sufi Movement: Features (Characteristics and Stages)",
            "Sufi Movement: Pir-Murid Tradition",
            "Sufi Movement: Use of Music in Sufism",
            "Sufi Orders (Silsila): Chisti",
            "Sufi Orders (Silsila): Suhrawardi",
            "Sufi Orders (Silsila): Naqshbandi",
            "Impact of Sufi Movement"
        ]
    }
]

modern_history = [
    {
        "subsection": "Arrival of Europeans in India",
        "items": [
            "Responsible Factors for Arrival of Europeans",
            "The Portuguese in India",
            "Portuguese: Vasco Da Gama",
            "Portuguese: Pedro Alvarez Cabral",
            "Portuguese: De Almeida",
            "Portuguese: Albuquerque",
            "Portuguese: Nino Da Cunha",
            "Causes of Failure of Portuguese empire in India",
            "The Dutch in India ( settlements, personalities, decline)",
            "The Danes in India ( settlements, personalities, decline)",
            "The English: Farrukhsiyar 's Farman",
            "The English: Causes of English Success",
            "The French ( settlements, personalities, decline)",
            "Anglo-French Rivalry",
            "First Carnatic War",
            "Rise of the Hyderabad State",
            "The Second Carnatic War",
            "The Third Carnatic War",
            "The Columbian Exchange"
        ]
    },
    {
        "subsection": "Expansion of East India Company",
        "items": [
            "Settlements at Various Places",
            "British Conquest of Bengal",
            "Bengal: Battle of Plassey",
            "Bengal: Battle of Buxar",
            "Bengal: Treaty of Allahabad",
            "Bengal: Dual Polity in Bengal (Diwani and Nizamat)",
            "4 Anglo - Mysore Wars",
            "3 Anglo - Maratha Wars",
            "Prominent Maratha Families Ruling from Different Places",
            "EIC Treaties: Surat, Purandar, Salbai, Bassein, Poona, Gwalior and Mandsor",
            "Marathas Defeat and its reasons",
            "The Subsidiary Alliance System and its Impact"
        ]
    },
    {
        "subsection": "Second Phase of British Expansion In India",
        "items": [
            "2 Anglo-Sikh Wars",
            "Doctrine of Lapse and its Victim States",
            "Annexation of Oudh",
            "EIC’s Relations with Neighboring Countries",
            "Doctrine of Ring Fence",
            "Doctrine of Masterly Inactivity",
            "Policy of Proud Reserve"
        ]
    },
    {
        "subsection": "Form of Administration before 1857",
        "items": [
            "The Dual System",
            "Regulating Act",
            "Pitt’s India Act",
            "The Charter Acts",
            "Evolution of Modern Judicial System",
            "Judicial System: Law Commission",
            "Developments of Civil Services",
            "British Indian Army",
            "Impact of British Administration"
        ]
    },
    {
        "subsection": "Economic Policies of The British",
        "items": [
            "Colonialism: Phase of Mercantilism (1757-1813)",
            "Colonialism: Phase of Free Trade (1813-1858)",
            "Colonialism: Phase of Finance Imperialism (1858 onwards)",
            "Land Revenue: Ryotwari",
            "Land Revenue: Mahalwari",
            "Land Revenue: Permanent Settlement",
            "Associated Terms of British Revenue System",
            "Impact of British Policy on Indian Economy",
            "Drain of Wealth Theory"
        ]
    },
    {
        "subsection": "Broader Impact of British Administration",
        "items": [
            "Industrialization—Ruin of Artisans and Handicrafts men",
            "Impoverishment of Peasantry",
            "Emergence of New Land Relations, Ruin of Old Zamindars",
            "Stagnation and Deterioration of Agriculture",
            "Commercialization of Indian Agriculture",
            "Development of Modern Industry",
            "Rise of Indian Bourgeoisie",
            "Critique of The Colonial Economy",
            "Critique: Economic Drain",
            "Famine and Poverty",
            "Nationalist Critique of Colonial Economy",
            "Abolition of the Dual System",
            "Changes in Social Setup"
        ]
    },
    {
        "subsection": "The Revolt of 1857",
        "items": [
            "Revolt of 1857 Causes: Economic Causes",
            "Revolt of 1857 Causes: Political Causes",
            "Revolt of 1857 Causes: Administrative Causes",
            "Revolt of 1857 Causes: Socio-Religious Causes",
            "Revolt of 1857 Causes: Influence of Outside Events",
            "Revolt of 1857 Causes: Discontent Among Sepoys",
            "Revolt of 1857 Events: Meerut Mutiny",
            "Revolt of 1857 Events: Siege of Delhi",
            "Revolt of 1857 Events: Fall of Delhi",
            "Important Places and Associated Leaders of the Revolt",
            "Important British Officers during Suppression of Revolt",
            "Causes of Failure of the Revolt",
            "Nature and Impact of the Revolt",
            "Various Outcomes of the Revolt",
            "Changes in the Army: Peel Commission",
            "Public Services: Ilbert Bill Controversy",
            "Policy of Equal Federation",
            "Princely States",
            "Foreign Policy (Post 1857)",
            "Local Government: Mayo’s Resolution",
            "Local Government: Ripon’s Resolution (1882)",
            "Local Government: Royal Commission on Decentralization (1908)",
            "Local Government: Resolution of May (1918) and Dyarchy (1919)",
            "Local Government: GoI Act, 1935 and After",
            "Labour Law Related Changes",
            "Changes in Socio-Cultural Stance"
        ]
    },
    {
        "subsection": "Evolution of Administrative and Police Services",
        "items": [
            "Proclamation of 1858",
            "Indian Civil Services Act, 1861",
            "Aitchison Committee on Public Services (1886)",
            "Islington Commission (1912)",
            "Montford Reforms (1919)",
            "Lee Commission (1924)",
            "Government of India Act, 1935",
            "Evolution of Police 1791",
            "Police Commission of 1860",
            "William Bentinck’s Contribution"
        ]
    },
    {
        "subsection": "Education during British Rule",
        "items": [
            "Changed Government Post 1857",
            "Acts between 1858-1947",
            "Administration - Central, Provincial, Local (Education)",
            "Charter Act of 1813",
            "General Committee of Public Instruction",
            "Orientalist-Anglicist Controversy",
            "Wood’s Dispatch (1854)",
            "Hunter Education Commission (1882-83)",
            "Indian Universities Act, 1904",
            "Government Resolution on Education Policy—1913",
            "Saddler University Commission (1917-19)",
            "Education Under Dyarchy",
            "Hartog Committee (1929)",
            "Wardha Scheme of Basic Education (1937)",
            "Sergeant Plan of Education",
            "Kothari Education Commission (1964-66)",
            "Development of Vernacular Education",
            "Development of Technical Education",
            "Evaluation of British Policy on Education"
        ]
    },
    {
        "subsection": "Press during British Rule",
        "items": [
            "James Augustus Hickey’s Bengal Gazette",
            "Different Publications and Journals",
            "Censorship of Act, 1799",
            "Licensing Regulations, 1823",
            "Press Act/Metcalfe Act, 1835",
            "Licensing Act, 1857",
            "Registration Act, 1867",
            "Vernacular Press Act, 1878",
            "Newspaper (Incitement to Offences) Act, 1908",
            "Indian Press Act, 1910",
            "Indian Press (Emergency Powers) Act, 1931",
            "Press regulating Act, 1942",
            "Struggle by Early Nationalists to Secure Press Freedom",
            "Various Newspapers/Journals and Their Authors",
            "Press During and After the First World War",
            "Press During the Second World War",
            "Press Post Independence",
            "Press Inquiry Committee, 1947"
        ]
    },
    {
        "subsection": "Socio-Religious Reform Movements",
        "items": [
            "Factors leading to Reform Movements",
            "Directions of Reforms",
            "Hindu Reform Movements",
            "Reform Movements Among Muslims",
            "Sikh Reform Movement",
            "Parsi Reform Movement",
            "Significance of Reform Movements",
            "Impact of Reform Movements"
        ]
    },
    {
        "subsection": "Important Personalities",
        "items": [
            "Raja Ram Mohan Roy",
            "Swami Vivekananda",
            "Swami Dayananda Saraswati",
            "Ishwar Chandra Vidyasagar",
            "Keshab Chandra Sen",
            "Sri Ramakrishna Paramahamsa",
            "Mahadev Govind Ranade",
            "Annie Besant–Theosophical Society",
            "Syed Ahmad Khan",
            "Baba Dayal Das",
            "Pandita Ramabai",
            "Sarojini Naidu",
            "Jyotiba Phule",
            "Dr. Bhimrao Ramji Ambedkar",
            "Aspects of Women Emancipation: Legislation and Women Organisation",
            "Aspects of Women Emancipation: Education",
            "Aspects of Women Emancipation: Widow Remarriage"
        ]
    },
    {
        "subsection": "Struggles of the Working Class",
        "items": [
            "Initial Efforts for Working Class’s Conditions",
            "All India Trade Union Congress (AITUC)",
            "Trade Union Act, 1926",
            "Trade Disputes Act, 1929",
            "Meerut Conspiracy Case (1929)"
        ]
    },
    {
        "subsection": "Peasant and Tribal Uprisings",
        "items": [
            "Responsible Factors for Tribal Revolts",
            "Tribal Movements: Bhil Uprising",
            "Tribal Movements: Kol Uprising",
            "Tribal Movements: Santhal Rebellion",
            "Tribal Movements: Singphos Rebellion",
            "Tribal Movements: Jaintia and Garo Rebellion",
            "Tribal Movements: Rampa Rebellion",
            "Tribal Movements: Chuar Uprising",
            "Tribal Movements: Munda Rebellion",
            "Tribal Movements: Khonda Dora Uprisings",
            "Tribal Movements: Tana Bhagat Movement",
            "Peasant Movements: Reasons of Resistance among Peasants",
            "Peasant Movements: Champaran Satyagraha",
            "Peasant Movements: Kheda Peasant Struggle",
            "Peasant Movements: Bardoli Movement",
            "Peasant Movements: Tebhaga Movement",
            "Peasant Movements: Telangana Movement",
            "Revolts: Sanyasi Revolt",
            "Revolts: Wahabi Movement",
            "Revolts: Pagal Panthis",
            "Revolts: Faraizi Revolt",
            "Revolts: Kuka Movement",
            "Revolts: Moplah Uprisings",
            "Military Discontent Uprisings: Paika Rebellion",
            "Military Discontent Uprisings: Ramosi Uprising",
            "Military Discontent Uprisings: Sawantwadi Revolt",
            "Reasons for Limited Success of the Uprisings"
        ]
    },
    {
        "subsection": "First Phase of National Movement (1905-1917)",
        "items": [
            "Pre-INC Organisations",
            "Pre-INC Campaigns and their Objectives",
            "Early Phase Indian National Congress",
            "Key Sessions of the Indian National Congress (INC)",
            "Debate over INC being a Safety Valve",
            "The Moderate Congress (1885-1905)",
            "Success and Limitations with Moderate Approach",
            "Moderate Opinion Against Economic Exploitation",
            "Moderate Campaign for Administrative Reforms",
            "Moderate Campaign for Constitutional Reforms",
            "Economic Critique of Imperialism",
            "Constitutional Reforms and Propaganda in Legislature",
            "Campaign for General Administrative Reforms",
            "Government’s Response towards INC",
            "Militant Nationalism (1905 to 1918)",
            "Important INC Sessions (Extremist Phase)",
            "Movement Under Extremist Leadership",
            "Mass Participation (Extremist Phase)",
            "Government Repression",
            "Movements of All India Muslim League (1906)",
            "Swadeshi Movement and Associated Leaders",
            "Morley Minto Reforms (1909)",
            "Comparative Account of Moderates and Extremists",
            "National Movement in Light of First World War",
            "Revolutionary Activities",
            "Hindustan Republican Association",
            "Chittagong Revolt Group",
            "Revolutionary Activities Abroad",
            "Differences between the Moderates and the Extremists",
            "Annulment of Partition of Bengal",
            "Home Rule League Movement (1916)",
            "Developments that led to Home Rule League",
            "Limitations with Home Rule Leagues",
            "Lucknow Session of INC (1916): Lucknow Pact",
            "Reasons of Readmission of Extremists",
            "Reasons of Muslim League pact with Congress",
            "Montague Statement of August (1917)"
        ]
    },
    {
        "subsection": "Second Phase of National Movement (1918-1929)",
        "items": [
            "Gandhi Ji in South Africa (1894-1914)",
            "Gandhi Ji in India (1915 Onwards)",
            "Highlight: Champaran Satyagraha (1917)",
            "Highlight: Ahmedabad Mill Strike (1918)",
            "Highlight: Kheda Satyagraha (1918)",
            "Montague-Chelmsford Reforms (1919)",
            "Rowlatt Satyagraha and Jallianwala Bagh Massacre (April 13, 1919)",
            "Non-Cooperation Movement (1920-22)",
            "Khilafat Movement (1919-20)",
            "Chauri Chaura Incident (5th Feb 1922)",
            "Congress-Khilafat Swaraj Party",
            "Swarajists and ‘No Changers'",
            "The Constructive Programme",
            "Indian Statutory Commission/ Simon Commission (1927)",
            "Nehru Report (1928)",
            "INC: Lahore Session, 1929",
            "INC: Allahabad Address (1930)",
            "Jinnah’s Fourteen Points Demand (1929)",
            "Leaders in this phase and their Contribution"
        ]
    },
    {
        "subsection": "Third Phase of National Movement",
        "items": [
            "Civil Disobedience Movement",
            "Extent of Participation and Possibility of Settlement",
            "Leaders in this Phase and their Role",
            "Gandhi-Irwin Pact",
            "Comparing NCM and CDM",
            "The Three Round Table Conferences (RTCs)",
            "Karachi Session of INC (1931)",
            "Communal Awards (1932)",
            "Poona Pact (1932)",
            "Government of India Act, 1935",
            "Congress Ministries after Provincial Elections of 1937",
            "Resignation of Congress Ministries (1939)",
            "Congress Working Committee at Wardha",
            "Decision on Mass Struggle",
            "Pakistan Resolution (23 Mar 1940)",
            "August Offer (1940)",
            "Individual Satyagraha (1941)",
            "Cripps Mission (1942)",
            "Quit India Movement (August Revolution) (1942)",
            "AICC Meeting (Gowalia Tank, Bombay)",
            "Parallel Governments",
            "Netaji Subhash Chandra Bose and INA",
            "Tokyo Conference: March 1942",
            "Bangkok Conference- June 1942",
            "Neta Ji in Japan (1943)",
            "Provisional Government of Free India, Singapore (October 1943)",
            "C. Rajagopalachari Formula (1944)",
            "Desai Liaquat Pact (1945)",
            "ML/Congress Response to Desai Liaquat",
            "General Elections, 1945",
            "Rin Mutiny (1946)",
            "Cabinet Mission Plan (1946)",
            "Direct Action Day (August 16th, 1946)",
            "Interim Government",
            "Constituent Assembly",
            "Objective Resolution",
            "Atlee’s Declaration and Transfer of Power",
            "Mountbatten Plan (June 3, 1947)",
            "India Independence Act (1947)",
            "Integration of States",
            "Governor Generals of India (1832-1858)",
            "Viceroy and Governor Generals of India (1858-1947)"
        ]
    },
    {
        "subsection": "Important Committees and Commissions",
        "items": [
            "Famine: Campbell Commission",
            "Famine: Stratchy Commission",
            "Famine: Lyall Commission",
            "Famine: MacDonnell Commission",
            "Law: First Law Commission, 1834, TB Macaulay",
            "Law: Second Pre-Independence Law Commission, 1853 – Sir John Romilly",
            "Law: Third Pre-Independence Law Commission, 1862 - Sir John Romilly",
            "Law: Fourth Pre-Independence Law Commission, 1879 – Dr Whitley Stokes",
            "Currency: Mansfield Commission",
            "Currency: Fowler Commission",
            "Currency: Babington Smith Commission",
            "Currency: Hilton Young Commission",
            "Other Important Commissions"
        ]
    },
    {
        "subsection": "Constitutional Development In India",
        "items": [
            "Governor of Bengal (Before 1773)",
            "Governor Generals of Bengal (1773-1833)",
            "Regulating Act 1773",
            "Pitt's India Act of 1784",
            "Charter Act of 1793",
            "Charter Act of 1813",
            "Charter Act of 1833",
            "Charter Act of 1853",
            "Government of India Act 1858",
            "The Indian Councils Act 1861",
            "Indian Councils Act 1892",
            "Indian Councils Act 1909",
            "Government of India Act 1919",
            "Government of India Act 1935",
            "Indian Independence Act, 1947"
        ]
    }
]

art_and_culture = [
    {
        "subsection": "Visual Arts",
        "items": [
            "Harappan: Sculptures",
            "Harappan: Seals",
            "Harappan: Pottery",
            "Harappan: Architecture-Town Planning",
            "Mauryan: Pottery (NBPW)",
            "Mauryan: Cave Architecture",
            "Mauryan: Pillars",
            "Mauryan: Stupas",
            "Post-Mauryan: Caves and Their Types",
            "Post-Mauryan: Stupa",
            "Post-Mauryan: Sculpture (Gandhara, Mathura, Amravati School)",
            "Gupta: Sculpture",
            "Gupta: Cave architecture",
            "Gupta: Sarnath Style of Sculpture",
            "Gupta: Fresco Mural Painting",
            "Buddhist and Jaina Influence",
            "Medieval School of Sculpture",
            "Modern Indian Sculpture"
        ]
    },
    {
        "subsection": "Temple Architecture",
        "items": [
            "Evolution of Temple Architecture- Separately in North and South India",
            "Types of Temple Architecture (Nagara, Dravida, Vesara, Hoysala) and subtypes",
            "Indo-Islamic: Imperial Style (Delhi Sultanate)",
            "Indo-Islamic: Provincial Style (Malwa or Pathan Style)",
            "Indo-Islamic: Mughal Style",
            "Indo-Islamic: Sikh Style of Architecture",
            "Indo-Islamic: Avadh (Oudh) Style",
            "Indo-Islamic: Rajput Architecture",
            "Modern Architecture",
            "European Influence (Modern Architecture)",
            "Indo-Gothic Architecture",
            "Neo-Roman Style",
            "Post-Independence Period (Architecture)",
            "Notable Architects"
        ]
    },
    {
        "subsection": "Paintings",
        "items": [
            "Cave Paintings",
            "Tradition of Mural Paintings in India",
            "Tradition of Miniature Paintings in India",
            "Paintings in the Deccan",
            "Mughal Painting",
            "Regional Paintings",
            "Miniature Painting in South India",
            "Modern Paintings",
            "Contemporary Paintings"
        ]
    },
    {
        "subsection": "Pottery Tradition",
        "items": [
            "Ochre Coloured Pottery (OCP)",
            "Black and Red Ware (BRW)",
            "Painted Grey Ware (PGW)",
            "Northern Black Polished Ware (NBPW)",
            "Glazed and Unglazed Pottery"
        ]
    },
    {
        "subsection": "Performing Arts",
        "items": [
            "Music: Classical Indian Music",
            "Music: Hindustani Music",
            "Music: Different Gharanas or Schools",
            "Music: Carnatic Music",
            "Music: Main Pillars of Indian Music",
            "Music: Forms of Indian Music",
            "Music: Musical Instruments",
            "Music: Institutions Related to Music in India",
            "Music: Folk Music",
            "Dances: Concept of Dance in India",
            "Dances: Concept of Ashta Nayika",
            "Dances: Rasa and Bhava",
            "Dances: Eight Classical Dance Forms in India",
            "Dances: Folk Dances",
            "Dances: Modern Dances",
            "Sports: Various Type of Sports",
            "Sports: Genesis of Martial Arts",
            "Sports: Forms of Traditional Martial Arts",
            "Sports: Animal Sports",
            "Theatre: History of Theatre in India",
            "Theatre: Classical Sanskrit Theatre",
            "Theatre: Traditional Theatre",
            "Theatre: Regional Theatre",
            "Theatre: Modern Theatre in India",
            "Theatre: Renaissance of Indian Theatre",
            "Cinema in India",
            "Puppetry: String Puppets",
            "Puppetry: Shadow Puppets"
        ]
    },
    {
        "subsection": "Religion, Language and Literature",
        "items": [
            "Religions: Pre-Vedic Religion",
            "Religions: Hinduism",
            "Religions: Buddhism",
            "Religions: Jainism",
            "Religions: Sikhism",
            "Religions: Islam",
            "Religions: Christianity",
            "Religions: Zoroastrianism",
            "Religions: Judaism",
            "Philosophy in India",
            "Bhakti Movement (Religions)",
            "Saints of Bhakti Movement",
            "Languages: Classical Language",
            "Literature: Sanskrit Literature",
            "Literature: Other Important Literatures",
            "Literature: Influence/Contribution of foreign languages"
        ]
    },
    {
        "subsection": "Miscellaneous",
        "items": [
            "Government Cultural Institutions in India",
            "UNESCO’s List of Cultural Heritage in India",
            "Protection and Promotion of Indian Culture and Heritage",
            "Schemes and Awards",
            "Personalities Related to Culture",
            "Places of Cultural Interest",
            "The Calendar & the Eras",
            "Science and Technology in Ancient India",
            "Recent Developments related to Art & Culture",
            "Schemes for Monument Development",
            "GI Tags"
        ]
    }
]

physical_geography = [
    {
        "subsection": "Universe & Earth Evolution",
        "items": [
            "Theories of development of Universe",
            "Galaxy",
            "Star formation",
            "Planet formation",
            "Solar system",
            "Geological History of Earth",
            "Evolution of the Layered Structure of Earth",
            "Latitude and Longitude including important Parallels and Meridians",
            "Motions of the Earth - Rotation, Revolution, and their effects",
            "Eclipses",
            "Earth’s magnetic field",
            "Earth’s Geological time scale",
            "Origin of Life on Earth"
        ]
    },
    {
        "subsection": "Geomorphology",
        "items": [
            "Crust",
            "Mantle",
            "Core",
            "Direct and Indirect Sources of Information",
            "Theories – Suess Theory",
            "Physical Characteristics–Crystal Form, Cleavage Fracture, Lusture, Color, Streak",
            "Transparency, Structure, Hardness, Specific Gravity",
            "Major Elements of the Earth’s Crust",
            "Metallic minerals – precious Ferrous, Non Ferrous",
            "Non-metallic Minerals – Sulphur, Phosphates, Cement",
            "Rocks (Aggregate of Minerals)",
            "Earth’s Surface (Geomorphic Processes)",
            "Endogenic Forces",
            "Exogenic Forces",
            "Earthquakes & their Types of Earthquakes",
            "Frequency and Intensity",
            "Ring of Fire",
            "Volcanism (Types and Associated Concepts)",
            "Theories (Distribution of Continents & Oceans)",
            "Continental Drift Theory",
            "Evidence in support of Continental Drift Theory",
            "Isostasy",
            "Sea Floor Spreading",
            "Forces of Drifting",
            "Post Drift Studies",
            "Convectional Current Theory",
            "Mapping of the Ocean Floor",
            "Plate Tectonics",
            "Plate Boundaries – Divergent – Convergent – Transform",
            "Rates of Plate Movements",
            "Force of plate movement",
            "Indian Plate",
            "Causes (Geomorphic Processes) of Landform Evolution",
            "Geomorphic Agents",
            "Agents and their Impacts",
            "Erosional Landforms",
            "Depositional Landforms",
            "Ground Water (Karst Topography)",
            "Impact of Waves and Currents",
            "Factors (Weathering)",
            "Geological Weathering",
            "Climatic Weathering",
            "Topographic Weathering",
            "Vegetative Weathering",
            "Chemical Weathering Major Processes",
            "Physical or Mechanical Weathering Major Processes",
            "Biological Weathering Major Processes",
            "Chemical Weathering – Forces and Chemical Action",
            "Physical Weathering Forces - Gravitational, Expansion, Water Pressure",
            "Biological Weathering (Processes)",
            "Rivers and lakes of the World",
            "Mountain and Peaks of the World",
            "Plateaus of the World"
        ]
    },
    {
        "subsection": "Oceanography",
        "items": [
            "Water on the Surface of the Earth",
            "Hydrological Cycle",
            "Component & Processes (Hydrological Cycle)",
            "Oceans & Relief of the Ocean floor",
            "Continental Shelf",
            "Continental Slope",
            "Deep sea plain",
            "Oceanic deep and Trenches",
            "Minor relief features",
            "Factors affecting Temperature distribution",
            "Density of Ocean Waters",
            "Waves, Ocean Currents, Tides",
            "Movements of ocean Water",
            "Terrigenous Deposits",
            "Volcanic Deposits",
            "Biotic deposits",
            "Abiotic Deposits",
            "Coral Reefs",
            "Great Barrier Reef",
            "Underground water resource",
            "Surface water resources",
            "Inland water resources",
            "Oceanic Water Resources",
            "Water consumption patterns",
            "Conservation of Water Resources",
            "Techniques of Water Conservation"
        ]
    },
    {
        "subsection": "Climatology",
        "items": [
            "Atmosphere Composition",
            "Atmosphere Gases",
            "Atmosphere Water Vapour",
            "Atmosphere Dust Particles",
            "Atmosphere Structure",
            "Troposphere",
            "Stratosphere",
            "Mesosphere",
            "Thermosphere",
            "Exosphere",
            "Altitude vs. Temperature",
            "Concept of Inversion of Temperature",
            "Solar Radiation Heat Balance",
            "Temperature Insolation",
            "Variability of Insolation at the surface of the Earth",
            "Heating and cooling of atmosphere",
            "Conduction, Convection, Advection",
            "Terrestrial Radiation",
            "Heat Budget of the Planet Earth",
            "Atmospheric Circulation and Weather Systems",
            "Atmospheric Pressure",
            "Factors affecting the velocity and direction of the Wind",
            "Pressure Gradient Force",
            "Frictional Force & Coriolis Force",
            "Pressure and Wind (Cyclonic & Anticyclonic)",
            "General Circulation of the Atmosphere – Pattern of Planetary Winds",
            "Latitudinal Variation of Atmospheric Heating",
            "Emergence of Pressure Belts",
            "Distribution of continents & Oceans",
            "Various Types of Wind (Seasonal, Local Wind etc.)",
            "Air Mass, Fronts, Cyclones and Jet Stream",
            "Thunderstorms",
            "Tornadoes",
            "Monsoons",
            "Water in the Atmosphere",
            "Water Vapour (Precipitation)",
            "Precipitation and its types",
            "World Distribution of Rainfall",
            "Clouds",
            "Various Types of Clouds",
            "Development of Clouds",
            "Koppen’s Classification Climatic Zones",
            "World Climate",
            "The Hot, Wet Equatorial Climate",
            "The Tropical Monsoon and Tropical Marine Climates",
            "The Savanna or Sudan Climate",
            "The Hot Desert and Mid-Latitude Desert Climates",
            "The Warm Temperate Western Margin (Mediterranean) Climate",
            "The Temperate Continental (Steppe Climate)",
            "The Warm Temperate Eastern Margin (China Type Climate)",
            "The Cool Temperate Western Margin (British Type Climate)",
            "The Cool Temperate Continental (Siberian) Climate",
            "The Cool Temperate Eastern Margin (Laurentian) Climate",
            "The Arctic or Polar Climate"
        ]
    },
    {
        "subsection": "Biogeography",
        "items": [
            "Types of natural vegetation",
            "Forests & its Various Aspects",
            "Deforestation",
            "Afforestation",
            "Reforestation",
            "Monoculture plantation",
            "Factors Responsible for Soil Formation",
            "Stages of Soil Formation",
            "Soil Forming Processes",
            "Soil Profiles and Horizons",
            "Soil Classification",
            "Soil Erosion and Conservation"
        ]
    }
]

indian_geography = [
    {
        "subsection": "Physiography & Drainage",
        "items": [
            "Geological Region",
            "Physiographic Sub-Units",
            "Himalayas",
            "The Peninsular - Peninsular Plateaus",
            "Plains - Northern Plains of India",
            "Lakes",
            "Deserts",
            "Indian Coasts and Islands",
            "Classification of Drainage",
            "Himalayan Drainage",
            "Indus river system",
            "Ganga River System",
            "Brahmaputra river system",
            "Peninsular River System"
        ]
    },
    {
        "subsection": "Climate, Soils & Vegetation",
        "items": [
            "Factors influencing the climate of India",
            "Monsoon",
            "Mechanism of the Monsoon",
            "El Nino and La Nina",
            "Koppen’s Climatic classification",
            "Soil Acidity & textures",
            "Minerals of Soil",
            "Soil Erosion",
            "Soil Conservation",
            "Vegetation (Natural)",
            "Mangroves",
            "Distribution of Forest Area"
        ]
    },
    {
        "subsection": "Human & Economic Geography",
        "items": [
            "Size, growth rate and distribution of population",
            "India in World Population",
            "Demographic transition (India)",
            "Census in India",
            "National Population Policy",
            "Literacy (India)",
            "Gender composition of the Population",
            "Health Indicators",
            "Rural & Urban Settlements",
            "Factors affecting settlement patterns",
            "Settlement types",
            "Land-use",
            "Causes & Impact of Land Degradation",
            "Sustainable Land Management",
            "Types of minerals: Metallic minerals & Non-metallic mineral",
            "Distribution of minerals and mining regions",
            "Distribution, production and international trade of minerals",
            "Conservation of mineral resources",
            "Classification of energy",
            "Production of conventional energy",
            "General trends of energy production and consumption",
            "Reserves and sources of energy",
            "Exploration",
            "International trade (Energy)",
            "OPEC and its role in oil trade",
            "Atomic (nuclear) energy",
            "Production of Atomic (Nuclear) Energy",
            "Nuclear Energy",
            "Alternative (non-conventional) sources of energy",
            "Performance of the agriculture sector",
            "Types of farming in India",
            "Cropping Pattern in India",
            "Agriculture regionalization",
            "Infrastructure factors: Seeds; Fertilizers; Irrigation",
            "Land use pattern in India",
            "Green Revolution",
            "Agricultural marketing",
            "Major schemes in agricultural sector",
            "National Policy for farmers",
            "Impact of climate change on agriculture",
            "Sustainable agriculture",
            "Use of IT in agriculture",
            "Agriculture Issues and Challenges",
            "Developments in Agriculture Field",
            "Productivity of Crops",
            "Industrial development",
            "Iron and Steel Industry",
            "Textile Industry",
            "Engineering Industries",
            "Fertilizer industry: Nitrogen fertilizers",
            "Cement industry",
            "Industrial Regions",
            "Characteristics of industrial regions",
            "Delimitation of an industrial region",
            "Principal industrial regions of the world",
            "Importance and development of transport",
            "Means of transport",
            "Transport costs and economic distance",
            "Operating costs in transport",
            "Government’s transport policy",
            "Ocean transport routes",
            "Inland waterways",
            "Pipeline transport",
            "Petroleum (oil) pipelines",
            "Gas pipelines",
            "New Development in Transport Sector",
            "Rural electrification corporation",
            "Time and costs overruns of infrastructure projects",
            "National Infrastructure Investment Fund",
            "Industrial Sector and New Initiatives",
            "Disinvestment of PSUs"
        ]
    },
    {
        "subsection": "World Regional Geography",
        "items": [
            "Continents and Important Cities of the World",
            "Important Cities Situated on the Banks of Rivers",
            "Changed Names of Some Cities, States, and Countries",
            "Distinctive Names of Countries/Towns— Geographical Epithets",
            "Regional Grouping of Countries of the World",
            "Economic Classification of Countries of the World"
        ]
    }
]

environment = [
    {
        "subsection": "Basic Concepts of Ecology & Ecosystems",
        "items": [
            "Basic Concepts: Types of Ecology",
            "Basic Concepts: Ecological Hierarchy",
            "Basic Concepts: Scope of Ecology",
            "Basic Concepts: Habitat & Ecological Niche",
            "Basic Concepts: Deep vs Shallow Ecology",
            "Basic Concepts: Ecological Principles",
            "Basic Concepts: Ecological Community",
            "Structure and Characteristics of a Community",
            "Ecology stratification",
            "Ecotone",
            "Ecological Dominance",
            "Seasonal and Diurnal Fluctuation",
            "Periodicity",
            "Turnover",
            "Interdependence",
            "Ecological Succession",
            "Types and Process of Succession",
            "Climax Community",
            "Range of Tolerance, Maximum Range",
            "Difference between Ecology, Environment and Ecosystem",
            "Biological Control",
            "Population Ecology",
            "Population Ecology: Types of species",
            "Population Growth Models",
            "Tiger Census and Lion Census",
            "Adaptation of Species and Interactions",
            "Ecosystem Definitions",
            "Functions and Properties of Ecosystem",
            "The Structure/Components of Ecosystem: Abiotic Components",
            "The Structure/Components of Ecosystem: Biotic Components",
            "Ecosystem Dynamics",
            "Flow of Energy in Ecosystem",
            "Trophic Levels",
            "Food Chain",
            "Types & Significance of Food Chain",
            "Food Web",
            "Models for Energy Flow",
            "Ecological Productivity",
            "Ecological Pyramid",
            "Biomagnifications"
        ]
    },
    {
        "subsection": "Terrestrial & Aquatic Ecosystems",
        "items": [
            "Forest Ecosystem in India",
            "Forests: Tropical Evergreen and Semi Evergreen Forests",
            "Forests: Tropical Deciduous Forests",
            "Forests: Dry deciduous Forest",
            "Forests: Tropical Thorn Forests",
            "Forests: Montane Forests",
            "Forests: Littoral and Swamp Forests",
            "Grasslands (Savanna and Steppe)",
            "Tundra",
            "Deserts",
            "Mountains",
            "Factors affecting the productivity of aquatic ecosystems: Sunlight",
            "Factors affecting productivity: Photic Zone",
            "Factors affecting productivity: Aphotic Zone",
            "Factors affecting productivity: Temperature and Oxygen Concentration",
            "Factors affecting productivity: Turbidity and Transparency",
            "Freshwater ecosystem",
            "Marine Ecosystem",
            "Marine Organisms",
            "Plankton",
            "Phytoplankton",
            "Zooplankton",
            "Sea-grass",
            "Seaweeds",
            "Eutrophication",
            "Algal Bloom",
            "Estuaries",
            "Types of Estuaries",
            "Importance of estuaries",
            "Threats to estuaries",
            "Conservation of Estuaries",
            "Mangroves",
            "Mangroves in India",
            "Importance of Mangroves",
            "Mangroves under threats",
            "Legal and Regulatory Approaches for Mangrove Protection",
            "Community based mangrove regeneration",
            "Coral Reef",
            "Types Of Coral Reefs",
            "Uses of coral reefs",
            "Threats to Coral reefs",
            "Conservation of coral reef",
            "Wetlands",
            "Types of wetlands",
            "Wetlands in India",
            "Importance of wetlands",
            "Threats to wetland ecosystems",
            "Conservation of Wetlands",
            "About Ramsar Convention",
            "About Asian Water bird Census",
            "Human Modified Ecosystems"
        ]
    },
    {
        "subsection": "Nutrient Cycling & Biodiversity",
        "items": [
            "Concept of Biogeochemical Cycle",
            "Carbon Cycle",
            "Hydrological Cycle",
            "Nitrogen Cycle",
            "Oxygen Cycle",
            "Sulfur Cycle",
            "Phosphorus Cycle",
            "Basics of Biodiversity",
            "Biogeographical classification of World",
            "Bio-geographical classification of India",
            "Functions of biodiversity",
            "Hotspots of biodiversity",
            "Bioinformatics",
            "Role of Traditional Knowledge in Biodiversity",
            "Biopiracy",
            "Animal and Plant Diversity",
            "Plant and Animal Kingdom",
            "Marine Mammals",
            "Egg laying Mammals",
            "Marsupials",
            "Threats to biodiversity",
            "Causes of Biodiversity losses",
            "Effects of Loss of Biodiversity",
            "Extinction of species",
            "Mass Extinction",
            "IUCN Red List and Classification Scheme",
            "Biodiversity Conservation",
            "Scheduled Animals in the Wildlife Protection Act",
            "Protected Area Categories",
            "Forms of Protected Areas",
            "Biosphere reserves",
            "Sacred forests and sacred lakes",
            "World Heritage sites",
            "Geo-heritage sites",
            "Advantages of In-situ conservation",
            "Disadvantages of In-situ conservation",
            "In-situ & Ex-situ methods of Conservation: Advantages & Disadvantages",
            "Zoological Parks",
            "Botanical Gardens",
            "Seed banks",
            "National Parks",
            "Wildlife Sanctuaries",
            "Important Coastal and marine Biodiversity Areas",
            "Biomes of India",
            "Plant Diversity of India",
            "Wildlife Diversity of India",
            "Wildlife Protection Act (WPA) (1972)",
            "International Union for Conservation of Nature (IUCN)",
            "Conservation Priorities"
        ]
    },
    {
        "subsection": "Species-Related Terminologies & Conservation Programs",
        "items": [
            "Flagship Species",
            "Keystone Species",
            "Priority Species",
            "Indicator Species",
            "Foundation Species",
            "Charismatic Species",
            "Umbrella Species",
            "Invasive/Alien Species",
            "Project Tiger",
            "Petersburg Tiger Summit 2010 (TX2)",
            "Conservation Assured (CA) | Tiger Standards (TS) Asia",
            "Project Elephant and Elephant Census",
            "Elephant Corridors",
            "Project Snow Leopard",
            "Project Secure Himalaya",
            "Vulture Conservation",
            "Action Plan for Vulture Conservation (2020 -2025)",
            "Crocodile conservation project",
            "Ganges dolphin project",
            "Indian (One Horn) Rhino Vision (IRV) 2020",
            "Project Sea Turtle",
            "Project Crocodile",
            "Project Hangul (Kashmir Stag)",
            "Dolphin Conservation",
            "India Adopted South Asia Wildlife Enforcement Network (SAWEN)",
            "State of Protected Areas in the World",
            "MAB – Man and Biosphere Programme",
            "World network of Biosphere Reserves",
            "Biodiversity Hotspots (International)",
            "CBD – Convention of Biological Diversity",
            "Cartagena Protocol",
            "Nagoya Protocol",
            "Aichi Biodiversity Diversity Targets"
        ]
    },
    {
        "subsection": "Resources, Energy & Pollution",
        "items": [
            "Land Resource",
            "Causes of land degradation",
            "Impact of land degradation",
            "Desertification",
            "Sustainable Land Management",
            "Forest Resource",
            "Types of Forests In India",
            "Deforestation",
            "Strategies for Reducing Deforestation",
            "Government Programmes for Conservation of Forests",
            "Soil Resource",
            "Soil Characteristics and Soil formation process",
            "Soil Profiles and Horizons",
            "Type of Soils",
            "Soils in India & World",
            "Soil Erosion",
            "Problems due to excessive irrigation",
            "Soil Conservation",
            "Soil health card scheme",
            "Organic Farming",
            "Water Pollution (Resource Aspects)",
            "Surface Water Resource",
            "Groundwater Resources",
            "Sources of Water Pollution",
            "Measurement of Water pollution",
            "Causes of Water Pollution",
            "Harmful effects of water pollution",
            "Algal Bloom (Water Pollution)",
            "Eutrophication (Water Pollution)",
            "Arsenic contamination of water",
            "Mercury Pollution",
            "Oxygen Stratification",
            "Energy Resources",
            "Ocean Thermal Energy Conversion (OTEC)",
            "Tidal Energy",
            "Geothermal Energy",
            "Solar Energy",
            "New Energy Resources",
            "Renewable Energy and Development",
            "National Policy on Biofuels",
            "New Energy Policy"
        ]
    },
    {
        "subsection": "Pollution & Occupational Hazards",
        "items": [
            "Basics of Pollution",
            "Sources of pollution",
            "Classification of pollutants",
            "Pollution Indicator species",
            "Water Pollution: Comparing Dissolved Oxygen, BOD and COD",
            "Mining and Pollution",
            "Mining and Environment",
            "Sustainable Mining",
            "Air Pollution",
            "Causes of air pollution",
            "Respirable Suspended Particulate Matter (RSPM)",
            "Fly Ash",
            "The Air (Prevention & Control of Pollution) Act 1981",
            "National Air Quality Index (NAQI) and National Ambient Air Quality Standards (NAAQS)",
            "Air Quality Early Warning System (AQEWS) and Graded Response Action Plan (GRAP)",
            "Continuous Ambient Air Quality Monitoring System (CAAQMS)",
            "Occupational Health Hazards",
            "Occupational Hazard: Black Lung Disease",
            "Occupational Hazard: Silicosis",
            "Occupational Hazard: Pneumoconiosis",
            "Occupational Hazard: Byssinosis",
            "Occupational Hazard: Asbestosis",
            "Marine Pollution",
            "Sources of marine pollution",
            "Effects of marine pollution",
            "Concept of dead zone",
            "Concept of Ocean acidification",
            "Oil spill",
            "Trash and Other Debris in ocean",
            "Microplastics and its impact",
            "Noise Pollution",
            "Causes of Noise pollution",
            "Noise Levels",
            "Effects of Noise Pollution on human health",
            "Noise Pollution: Corrective actions",
            "Biological Pollution",
            "Sources of biological pollution",
            "Harmful effects from biological contaminants",
            "Biological Pollution: Corrective actions",
            "Radioactive Pollution",
            "Sources of Radioactive Pollution",
            "Harmful effects of Radioactive Pollution",
            "Radioactive Pollution: Corrective actions",
            "Thermal Pollution",
            "Causes of Thermal Pollution",
            "Effect of Thermal Pollution",
            "Control of Thermal Pollution"
        ]
    },
    {
        "subsection": "Waste Management",
        "items": [
            "Solid waste management",
            "Types of Solid Waste",
            "Issues in solid waste management in India",
            "Technologies for the Generation of Energy from Waste",
            "Policy on Promotion of City Compost",
            "Salient features of SWM Rules, 2016",
            "E-Waste Management",
            "Pollutants and their health impacts",
            "E-waste status in India",
            "Importance of the E-waste management",
            "Steps taken for combating mounting E-Waste",
            "E-waste (Management & Handling) Rules, 2016",
            "Stockholm Convention on Persistent Organic Pollutants",
            "Basel Convention",
            "Rotterdam Convention",
            "Plastics Pollution",
            "Effects of Plastic Waste",
            "The Global Tourism Plastics Initiative",
            "Biomedical Waste Management",
            "Hazards associated with waste management",
            "Bio-Medical Waste Management Rules, 2016",
            "Hazardous waste and its Characteristics",
            "Hazardous and Other Wastes (Management & Trans-boundary Movement) Rules, 2016",
            "Hazardous waste treatment",
            "Treatments/ Methods in Waste Management"
        ]
    },
    {
        "subsection": "Climate Change & Environmental Administration",
        "items": [
            "Climate Change Basics",
            "Factors Affecting Climate Change",
            "Urbanization and climate change",
            "Urban Heat Island",
            "Impact of agriculture on climate",
            "Agriculture increases Carbon Dioxide Emissions",
            "Monoculture practice impacts biodiversity",
            "Pollution due to use of chemical fertilizers",
            "Soil-related effects (Agriculture)",
            "Sustainable Agriculture Techniques (Climate)",
            "Greenhouse effect",
            "Ecological footprint",
            "Carbon footprint",
            "Global Warming Potential (GWP)",
            "Impacts of the Climate Change",
            "Global Warming & Health",
            "Ozone depletion and human health",
            "Strategies to Address Climate Change",
            "Constitutional Provisions related to environment",
            "Wildlife Protection Act 1972 (EPA Aspects)",
            "Environmental Protection Act",
            "National Forest Policy",
            "Biological Diversity Act 2002",
            "Schedule Tribes and Other Forest Dwellers Act 2006",
            "Coastal Regulation Zone",
            "Wetland Rules 2010",
            "National Green Tribunal",
            "Ozone Depleting Substance Rules",
            "Environment Impact Assessment (EIA)",
            "Brief History of EIA in India",
            "EIA Process in India",
            "Drawback in EIA Process",
            "Recommendations for Improvement of EIA",
            "International Environmental Governance",
            "UNEP",
            "UNDP (Governance)",
            "Centre for Biological Diversity",
            "WWF for Nature",
            "IUCN - Red List (Governance)",
            "Birdlife International",
            "International Conventions / Protocols & their Objectives",
            "Sustainable Development Goals (Environmental)",
            "Various Indices relate to Environment",
            "Climate Change Governance",
            "United Nations Conference on the Human Environment (Stockholm Conference)",
            "Montreal Protocol and Kigali Agreement",
            "The Earth Summit",
            "Commission on Sustainable Development (CSD)",
            "United Nations Convention to Combat Desertification (UNCCD)",
            "United Nations Framework Convention on Climate Change (UNFCCC): 1992",
            "Global Climate Finance Architecture",
            "Global Environment Facility (GEF)",
            "REDD+",
            "Intergovernmental Panel on Climate Change (IPCC)",
            "National Greenhouse Gas Inventories Programme (NGGIP)",
            "The Economics of Ecosystems and Biodiversity (TEEB)",
            "Special Climate Change Fund (SCCF)",
            "Least Developed Countries Fund (LDCF)",
            "Climate Investment Fund (World Bank as Trustee)",
            "Green Climate Fund (GCF)",
            "Adaptation Fund (AF)",
            "Biocarbon Fund",
            "EU Initiatives (Climate)",
            "Clean Technology Fund",
            "World Meteorological Organization (WMO)",
            "United Nations Programmes and Assemblies",
            "United Nations Environment Programme (UNEP) Governance",
            "Forest Carbon Partnership Facility",
            "Climate and Clean Air Coalition (CCAC)",
            "Arctic Council",
            "India and Climate Change",
            "India’s Position with regards to policy on Climate Change",
            "Observed Climate and Weather Changes in India",
            "Indian Climate Change Assessment",
            "Actions for Adaptation & Mitigation",
            "National Action Plan for Climate Change (NAPCC)",
            "NAPCC: National Solar Mission",
            "NAPCC: National Mission for Enhanced Energy Efficiency (NMEEE)",
            "NAPCC: National Mission on Sustainable Habitat",
            "NAPCC: National Water Mission",
            "NAPCC: National Mission for Sustaining Himalayan Ecosystems",
            "NAPCC: National Mission for a Green India",
            "NAPCC: National Mission on Sustainable Agriculture",
            "NAPCC: National Mission on Strategic Knowledge for Climate Change",
            "National Bioenergy Mission",
            "National Communication (NATCOM)",
            "National Action Programme to Combat Desertification",
            "Green Buildings",
            "Net Zero Energy Buildings (NZEB)",
            "Standard and Labeling Programme (BEE Star Label)",
            "Energy Conservation Building Code (ECBC)",
            "Green Rating for Integrated Habitat Assessment (GRIHA)",
            "National Initiative on Climate Resilient Agriculture (NICRA)",
            "BSE - GREENEX",
            "FAME - India Programme",
            "Long Term Ecological Observatories (LTEO)",
            "National Adaptation Fund for Climate Change (NAFCC)",
            "National Policy on Biofuels, 2018",
            "Environment related Institutions in India",
            "Pollution Control Boards",
            "National Green Tribunal (Inst)",
            "National Board for Wildlife (NBWL)",
            "Animal Welfare Board",
            "Central Zoo Authority (CZA)",
            "National Biodiversity Authority",
            "Central Water Commission",
            "Animal Welfare Board of India (AWBI)",
            "Zoological Survey of India (ZSI)",
            "Forest Survey of India (FSI)",
            "India State of Forest Report",
            "Botanical Survey of India (BSI)",
            "Wildlife Crime Control Bureau (WCCB)",
            "National Biodiversity Authority (NBA)",
            "National Ganga River Basin Authority",
            "National Tiger Conservation Authority (NTCA)",
            "Bombay Natural History Society",
            "Schemes in India regarding Environmental Protection",
            "National Wildlife Action Plan",
            "CAMPA",
            "Joint Forest Management",
            "Social Forestry",
            "Ganga Rejuvenation Plan",
            "Benefits of River Ganga (Facts about Ganga River Pollution and its impacts)",
            "Eco mark Scheme",
            "Swachh Bharat Mission",
            "Bharat Stage Norms",
            "Corporate Social Responsibility and Environment Protection"
        ]
    },
    {
        "subsection": "Relevant Environmental Data Lists",
        "items": [
            "Data List: National Parks",
            "Data List: Tiger Reserves of India",
            "Data List: Elephant Reserves in India",
            "Data List: Mike Sites in India",
            "Data List: Biosphere Reserves",
            "Data List: Biosphere Reserves in UNESCO’s Map List",
            "Data List: Ramsar Wetland Sites",
            "Data List: Natural World Heritage Sites",
            "Data List: List of Sacred Groves",
            "Data List: Mangrove Sites in India"
        ]
    }
]

polity = [
    {
        "subsection": "Historical Background & Making of Constitution",
        "items": [
            "The Company Rule (1773-1858)",
            "Regulating Act, 1773",
            "Amending Act, 1781",
            "Pitt’s India Act, 1784",
            "Amending Act of 1786",
            "Charter Act, 1793",
            "Charter Act, 1813",
            "Charter Act, 1833",
            "Charter Act, 1853",
            "The Crown Rule (1858-1947)",
            "Government of India Act, 1858",
            "Indian Councils Act, 1861",
            "Indian Councils Act, 1892",
            "Indian Councils Act, 1909",
            "Government of India Act, 1919",
            "Simon Commission",
            "Government of India Act, 1935",
            "Indian Independence Act, 1947",
            "Making of Indian Constitution",
            "Sources of the Constitution",
            "Important Committees of the Constituent Assembly",
            "Working of the Constituent Assembly",
            "Objective Resolution",
            "Changes by the Independence Act, 1947",
            "Functions Performed by Constituent Assembly",
            "Drafting Committee",
            "Enactment and enforcement of the Constitution",
            "Important Facts about Indian Constitution",
            "Types of Constitution",
            "Functions of the Constitution",
            "Historical evolution of the Constitution",
            "Types of Political System",
            "Constitutional Government",
            "Parliamentary form of government",
            "Distinction between Indian and British Models",
            "Features of the Presidential System",
            "Features of Semi-Presidential System",
            "Preamble and Values in the Constitution",
            "Objectives as per the Preamble",
            "Ideals (as mentioned in the Preamble)",
            "Amendment of the Constitution",
            "Types of Majorities",
            "Evolution of Basic Structure Doctrine",
            "Important Doctrines and Concepts",
            "Other Constitutional Dimensions",
            "Schedules and Subjects",
            "Official Languages"
        ]
    },
    {
        "subsection": "Union, Territory, Citizenship & Salient Features",
        "items": [
            "Union and Its Territory",
            "Article 1-4",
            "Committee/commission for State Re-organization",
            "The State Reorganization Commission (SRC) 1953",
            "Delimitation Commission",
            "Citizenship: Constitutional Provisions (Article 6-11)",
            "Constitutional provisions of citizenship",
            "Citizenship Act, 1955",
            "The Citizenship (Amendment) Act, 2016",
            "Citizenship Amendment Act, 2019",
            "Methodology of Acquisition of Citizenship",
            "Modes of Losing the Citizenship of India",
            "Comparison between NRI, PIO, and OCI Cardholder",
            "Indian Diaspora",
            "Pravasi Bhartiya Divas",
            "Non-Resident Indians",
            "Salient Features of Indian Constitution",
            "Constitution and Types"
        ]
    },
    {
        "subsection": "Fundamental Rights, DPSP & Fundamental Duties",
        "items": [
            "Fundamental Rights Part III: Meaning, Objectives, Evolution, Importance",
            "Reasonable Restriction on Fundamental Rights",
            "Article 12: Definition of state",
            "Article 13: Laws Inconsistent with Fundamental Rights",
            "Concept of Judicial Review",
            "Equality Rights",
            "Concept of Rule of Law",
            "Due Process of Law",
            "Procedure Established by Law",
            "Right to Freedom",
            "Legal, Constitutional and Fundamental Rights: Right to Property, Right to Vote etc.",
            "Right against Exploitation",
            "Right to Freedom of Religion",
            "Cultural and Educational Rights",
            "Right to Constitutional Remedies (Article 32)",
            "Other Dimensions of FR’s",
            "DPSP Part IV: Evolution, objectives, and features",
            "DPSP Basic Features",
            "Different Types of Principles (DPSP)",
            "DPSP Amendments",
            "DPSP Implementation",
            "Socialistic Principles",
            "Gandhian Principles",
            "Liberal-Intellectual Principles",
            "Directive Principle Outside Part IV",
            "Fundamental Duties: Features",
            "List of Fundamental Duties",
            "Other Recent Developments in Fundamental Duties"
        ]
    },
    {
        "subsection": "System of Governance & Emergency Provisions",
        "items": [
            "Centre-State Relations: Legislative Relations",
            "Centre-State Relations: Territorial Powers",
            "Centre-State Relations: Administrative Relations",
            "Centre-State Relations: Financial Relations",
            "National Integration Council",
            "Inter State Relation and Related Issues",
            "Interstate water dispute",
            "Interstate councils",
            "Interstate trade and commerce",
            "Zonal Councils",
            "Special Provisions for some States",
            "Types of Emergencies",
            "National Emergency",
            "Constitutional/State Emergency / President’s Rule",
            "Financial Emergency"
        ]
    },
    {
        "subsection": "Union Executive & Legislature (Parliament)",
        "items": [
            "Union Executive: President",
            "Union Executive: Vice President",
            "Union Executive: The Prime Minister",
            "Union Executive: Union Council of Minister",
            "Union Executive: Role of Bureaucracy",
            "Organisation of Parliament",
            "Functions of the Parliament",
            "Functioning of the Parliament",
            "Sessions of Parliament",
            "Devices of Parliamentary Proceedings",
            "Parliamentary Privileges and Immunities",
            "Collective Privileges of the House",
            "Individual Privileges",
            "Houses of the Parliament",
            "Parliament (Lok Sabha, Rajya Sabha and President)",
            "Lok Sabha Composition",
            "Rajya Sabha Composition",
            "Presiding Officers of the Parliament",
            "Speaker",
            "Powers & Functions of the speaker",
            "Deputy Speaker",
            "Panel of Chairpersons of Lok Sabha",
            "Speaker Pro Tem",
            "Chairman of Rajya Sabha",
            "Deputy Chairman of Rajya Sabha",
            "Panel of Vice-Chairpersons of Rajya Sabha",
            "Chairman and Deputy chairman of the Council of States",
            "Membership of the Parliament",
            "Secretariat of Parliament",
            "Leaders in Parliament and Whip",
            "Devices of Parliamentary Proceedings (Duplicate in prompt)",
            "Comparison between different types of Funds",
            "Role and powers of Parliament",
            "Special Power of Rajya Sabha",
            "Position of Rajya Sabha with respect to Lok Sabha",
            "Parliamentary Privileges",
            "Sovereignty of Parliament",
            "Legislative Procedure and Committees of Parliament"
        ]
    },
    {
        "subsection": "State Executive & State Legislature",
        "items": [
            "State Executive: Governor",
            "Governor Powers: Executive power",
            "Governor Powers: Legislative power",
            "Governor Powers: Financial Power",
            "Governor Powers: Judicial Power",
            "Governor Powers: Discretionary power",
            "Recommendations on the office of Governor",
            "ARC (Administrative Reforms Commission)",
            "Sarkaria Commission",
            "National Commission to Review the working of the Constitution",
            "The Chief Minister and the CoM",
            "Powers and Functions of Chief Minister",
            "Other Powers and Functions of CM/CoM",
            "Composition of the Council of Ministers",
            "Responsibility of Ministers",
            "Advocate-General for the State",
            "State Legislature: Legislative Assembly",
            "Legislative Assembly: Powers and Functions",
            "Legislative Assembly: Speaker & Deputy Speaker",
            "Parliament’s Control over State Legislature",
            "State Legislature: Legislative Council",
            "Legislative Council: Qualifications",
            "Legislative Council: Powers and Functions"
        ]
    },
    {
        "subsection": "Local Government, UTs & Special Areas",
        "items": [
            "Local Government: Panchayati Raj",
            "Evolution of the Panchayati Raj Institution (PRI)",
            "73rd Amendment Act of 1992",
            "Compulsory and Voluntary Provisions",
            "Urban Local Government",
            "74th Constitutional Amendment Act",
            "Types of Urban Governments In India",
            "PESA Act, 1996",
            "Union Territories: Creation of Union Territories",
            "Administration of UT's",
            "Special provisions for Delhi",
            "Special Category Status",
            "Scheduled and Tribal Areas",
            "Administration of Schedule Areas",
            "Administration of Tribal areas",
            "Fifth Schedule and Sixth Schedule"
        ]
    },
    {
        "subsection": "The Judiciary (Supreme Court, High Court & Lok Adalat)",
        "items": [
            "Supreme Court: Chief Justice of India",
            "SC: Acting Chief Justice of India",
            "SC: Appointment of Supreme Court Judges",
            "SC: Qualifications for Supreme Court Judges",
            "SC: Removal of a Supreme Court Judges",
            "SC: Process of Impeachment",
            "SC: Ad hoc and Retired Judges",
            "SC: Salaries and allowances of Supreme Court Judges",
            "Chief Justices of India (Since 1951)",
            "Jurisdiction of the Supreme Court",
            "Judicial Independence",
            "Judiciary Executive Relations",
            "Difference between Indian and American Judiciary",
            "Concurrence Vs Consultation",
            "Judicial Review and Judicial Activism",
            "Concept of Public Interest Litigation (PIL)",
            "The High Courts",
            "Jurisdiction of the High Courts",
            "Subordinate Courts",
            "Gram Nyayalayas Act, 2008",
            "Alternative dispute Resolution",
            "Lok Adalat",
            "All India Judicial Service",
            "E-governance in Judiciary",
            "Judicial Impact Assessment",
            "Judges Standards and Accountability Bill, 2010",
            "National Legal Services Authority (NALSA)"
        ]
    },
    {
        "subsection": "Constitutional & Extra-Constitutional Bodies",
        "items": [
            "Finance Commission: Constitution",
            "Finance Commission: Functions",
            "Comptroller And Auditor General of India",
            "Attorney-General of India: Appointment",
            "Attorney-General: Functions and Responsibilities",
            "Election Commission: Universal Adult Franchise, Right to Vote",
            "Elections and Electoral System in India",
            "Electoral Reforms Since 1988",
            "All India Services",
            "Union Public Service Commission (UPSC)",
            "State Public Service Commission (SPSC)",
            "Joint State public Service Commission (JSPSC)",
            "National Commission For SCs",
            "National Commission For STs",
            "Special Officer for Linguistic Minority",
            "The Advocate General",
            "Extra-Constitutional Bodies: Special officer for linguistic Minorities",
            "Central Information Commission",
            "State Information Commission",
            "Lokpal and Lokayukta",
            "National Human Rights Commission",
            "State Human Right Commission",
            "CVC (Central Vigilance Commission)",
            "NITI Aayog (National Institution for Transforming India)",
            "NITI Aayog Vs the Planning Commission"
        ]
    },
    {
        "subsection": "Political Dynamics",
        "items": [
            "Political Parties and Election",
            "Salient features of Representation of Peoples Act, 1951",
            "Criminalization of politics",
            "State funding of Election",
            "Party System in India",
            "10th Schedule and Anti-defection measures",
            "Pressure Groups: Meaning and Techniques",
            "Types of Pressure Groups in India",
            "Role of pressure group in developing countries",
            "Functions of pressure groups in India",
            "Pressure groups methods",
            "Criticism of pressure groups"
        ]
    },
    {
        "subsection": "Governance & Welfare Schemes",
        "items": [
            "Governing Institutions in India",
            "Structure of Ministries/departments",
            "Functions of attached and subordinate office",
            "Other organizations",
            "Public sector undertakings",
            "The Executive organization",
            "Advantages of the separation of secretariat and executive organization",
            "Strengths and weaknesses of the existing structure",
            "Recommendations for improving the Organizational structure",
            "Audit & Transparency: CVC",
            "Audit & Transparency: CAG",
            "Audit & Transparency: Lokpal",
            "Audit & Transparency: Lokayukta",
            "Role of SHG, NGOs, Civil Society",
            "Welfare Schemes: Health (Various Mission and Schemes by GoI)",
            "Welfare Schemes: Education",
            "Welfare Schemes: Vulnerable Sector",
            "Welfare Schemes: Social Security",
            "Welfare Schemes: Women and Child Development",
            "Welfare Schemes: Disability",
            "Welfare Schemes: Rural and Urban Development",
            "Smart Cities Mission",
            "Welfare Schemes: Inclusive growth",
            "Welfare Schemes: Digital India"
        ]
    }
]

economy = [
    {
        "subsection": "Fundamental Concepts & National Income",
        "items": [
            "Meaning of Economics",
            "Types of Economies",
            "Sectors of an Economy",
            "Microeconomic Concepts",
            "National Income Concepts and Methods of Calculation",
            "Economic Growth Vs Economic Development",
            "Measures of Economic Growth",
            "Procyclical and Counter Cyclical Economic policies",
            "Methods of GDP calculations",
            "Business Cycle",
            "Inflation",
            "Inflation Reports & Indices",
            "Concepts and Types of Inflation",
            "Causes of Inflation",
            "Effects of Inflation",
            "Measures of Inflation"
        ]
    },
    {
        "subsection": "Money and Banking",
        "items": [
            "Money Function and Classification",
            "Money Concept",
            "Measures of Money Supply in India",
            "Broad and Narrow Money",
            "Money multiplier",
            "Digital Money",
            "Monetary Policy",
            "Banking in India: Scheduled Commercial Banks",
            "Nationalized Banks",
            "Public Sector Banks",
            "State Bank of India",
            "Private Banks",
            "Foreign Banks",
            "Regional Rural Banks",
            "Scheduled Co-operative Banks",
            "Reserve Bank of India (RBI)",
            "Methods of Credit Control: Quality & Quantity Control Measures",
            "Cash Reserve Ratio (CRR)",
            "Statutory Liquidity Ratio (SLR)",
            "Repo Rate",
            "Reverse Repo Rate, etc.",
            "Banking Sector Reforms in India: Basel Norms",
            "Banking Ombudsman",
            "Development Financial Institutions",
            "Insurance Companies",
            "New Developments in Economic Sector",
            "Financial Market and its Instruments: Concept and functions",
            "Importance of money market",
            "Types of capital market",
            "Capital market vs money market",
            "Nature and functions of a stock exchange",
            "Insurance Industry and Reforms",
            "Role of Financial Regulators"
        ]
    },
    {
        "subsection": "Public Finance & Taxation",
        "items": [
            "Union Budget",
            "Revenue Receipts: Tax Revenue Receipts",
            "Revenue Receipts: Non-Tax Revenue Receipts",
            "Fiscal Policy",
            "Fiscal Responsibility and Budget Management (FRBM) Act, 2003",
            "Revenue Deficit, Fiscal Deficit, Primary Deficit",
            "Deficit and Surplus Budget",
            "Deficit Financing",
            "Centre State Distribution: Finance Commission (Article 280)",
            "Tax Structure in India: Important concepts",
            "Methods of Taxation (Progressive, Regressive, Proportional)",
            "Types of Taxes (Direct Tax, Indirect Tax)",
            "Value Added Tax – VAT in India",
            "Goods and Services Tax – GST, GST Council",
            "Service Tax",
            "DTC – Direct Tax Code",
            "Comparison between Surcharge and Cess",
            "Distribution of Tax Revenues",
            "Taxation: Important Institutions",
            "Steps taken to reduce Tax Avoidance in India",
            "Taxation related terms and terminologies",
            "Government Debt"
        ]
    },
    {
        "subsection": "Planning & Economic Reforms",
        "items": [
            "Decentralized Planning",
            "Multi-Level Planning",
            "Central sector and Centrally Sponsored Schemes",
            "Planning Institutions: Planning Commission",
            "NITI Aayog",
            "National Development Council (NDC)",
            "Five Year Plans in India: 12th Five Year Plan (2012-2017)",
            "Alternative Scenarios During 12th Plan",
            "Economic Planning: Meaning, Objectives, Strategies",
            "Harrod Domar strategy",
            "Nehru Mahalanobis strategy",
            "Gandhian strategy",
            "LPG strategy",
            "Regional and National Planning",
            "Imperative and Indicative Planning",
            "History of Planning in India",
            "Visvesvaraya Plan, Gandhian Plan, FICCI Proposal, Congress Plan, Bombay Plan",
            "Planning Commission and National Development Council (NDC) History"
        ]
    },
    {
        "subsection": "External Sector & International Organizations",
        "items": [
            "Balance of Payments (BOP)",
            "Foreign Capital – FDI, FPI, FII, QFI",
            "Foreign Exchange–Exchange Rate, NEER & REER, ETF",
            "FERA & FEMA",
            "Capital Account Convertibility in India",
            "India's External Debt",
            "NRI Deposits",
            "Trade Composition",
            "Import/Export Controls",
            "Export Promotion",
            "General Agreement on Tariffs and Trade (GATT)",
            "Exchange Rate Policy",
            "United Nations",
            "Food and Agriculture Organization (FAO)",
            "International Civil Aviation Organization (ICAO)",
            "International Fund for Agricultural Development (IFAD)",
            "International Labour Organization (ILO)",
            "International Maritime Organization (IMO)",
            "International Monetary Fund (IMF)",
            "International Telecommunication Union (ITU)",
            "United Nations Educational, Scientific and Cultural Organization (UNESCO)",
            "United Nations Industrial Development Organization (UNIDO)",
            "Universal Postal Union (UPU)",
            "World Bank Group (WBG)",
            "International Bank for Reconstruction and Development (IBRD)",
            "International Finance Corporation (IFC)",
            "International Development Association (IDA)",
            "World Health Organization (WHO)",
            "World Intellectual Property Organization (WIPO)",
            "World Meteorological Organization (WMO)",
            "World Tourism Organization (UNWTO)",
            "World Trade Organization (WTO)",
            "Asian Development Bank",
            "Asian Infrastructure Investment Bank (AIIB)",
            "New Development Bank",
            "African Development Bank",
            "Various Trade Agreements",
            "Global Foreign Exchange Committee",
            "New Developments in External Sector"
        ]
    },
    {
        "subsection": "Human Development, Poverty & Employment",
        "items": [
            "Human Development: Concepts and Approaches",
            "UNDP Human Development Report (HDR)",
            "Gender Inequality Index, Global Gender Gap Index, Gender Parity Index Comparison",
            "World Happiness Report",
            "World Bank - Human Capital Project",
            "Sustainable Development Goals (SDGs) 2030",
            "Poverty: Definition and Indices",
            "Poverty in India",
            "Human Poverty Index (HPI)",
            "Expert Groups for Estimating Poverty",
            "Multidimensional Poverty",
            "Socio Economic and Caste Census (SECC)",
            "Employment and Unemployment Concepts",
            "Poverty Eradication and Employment Related programs",
            "Government Schemes and Programs (Economic Development)",
            "Various Committees on Poverty and Employment"
        ]
    },
    {
        "subsection": "Agriculture Sector in Indian Economy",
        "items": [
            "Agriculture Key statistics",
            "Economic Survey on Agriculture",
            "Union Budgets on Agriculture",
            "Important terminologies related to Cropping",
            "Agricultural System",
            "Sustainable Agriculture",
            "Important Agriculture and Income Support Schemes",
            "Committees related to Agriculture",
            "Other Agriculture related Institutions",
            "Major Agreements and concepts under WTO (World Trade Organization)",
            "Rainbow Revolution in Agriculture",
            "Animal Husbandry",
            "Land Reforms"
        ]
    },
    {
        "subsection": "Industry & Infrastructure in Indian Economy",
        "items": [
            "Classification Of Industries",
            "Index of Industrial Production (IIP)",
            "Eight Core Sectors",
            "Economic Survey on Industry",
            "Important Industrial Locations",
            "Strategic and Critical Minerals",
            "Economic Reforms related to Industries",
            "Disinvestment of PSEs",
            "Types of Public Sector Enterprises (PSEs)",
            "Special Economic Zones (SEZ)",
            "National Investment & Manufacturing Zones (NIMZ)",
            "Production Linked Incentive (PLI) Scheme",
            "Industrial Corridors",
            "Dedicated Freight Corridor (DFC)",
            "Industry Related Schemes and Initiatives",
            "National Infrastructure Pipeline (NIP)",
            "Micro, Small, and Medium Enterprises (MSMEs)",
            "Intellectual Property Rights (IPR)",
            "Important Industrial Reports"
        ]
    },
    {
        "subsection": "Service Sector in Indian Economy",
        "items": [
            "Spread of Service Sector",
            "Service Sector Performance",
            "National Investment and Infrastructure Fund (NIIF)",
            "Purchasing Managers Index (PMI)",
            "Logistics Performance Index (LPI)",
            "Logistics Ease Across Different States (LEADS) Report, 2022",
            "Champion Services Sector (CSS)",
            "WTO and Services",
            "Service Sector Government Schemes & Initiatives",
            "Services: Economic Survey 2021-22",
            "IT and Telecom Services"
        ]
    }
]

science_tech = [
    {
        "subsection": "Policy & Organization of S&T",
        "items": [
            "Role of S&T in the Developing World",
            "S&T Policy in India - History",
            "Awards related to Science",
            "New Initiatives Aligned with the National Agenda",
            "India and World collaboration in science projects",
            "Technology Vision Document 2035",
            "National Intellectual Property Rights Policy",
            "Policy on Synthetic Biology",
            "List of Various Centre Institutions and Bureaus",
            "Ministries and Department for science and Technology",
            "Department of Science & Technology"
        ]
    },
    {
        "subsection": "Space Technology & Missions",
        "items": [
            "Space Technology",
            "Indian Space research Programme",
            "ISRO and ANTRIX",
            "Orbits Type",
            "Satellite Launching Systems",
            "Terminologies Related to the Space Science",
            "Earth Observation Systems",
            "Satellite Communication in India",
            "Remote sensing applications - IRS Systems",
            "INSAT Satellite Application",
            "GSAT Satellite Application",
            "Launch vehicle Technology",
            "GSLV and Various Engine",
            "Recent National and International Space Missions",
            "Cryogenic rockets",
            "Chandrayaan – I & II",
            "Mars Orbiter Mission",
            "Space Organisations",
            "Space race/Space junk",
            "New Developments in the field of Space",
            "Developments in India and in the World: South Asia Satellite",
            "Developments in India and in the World: Neutrino Observatory",
            "Developments in India and in the World: Solar Mission- ADITYA",
            "Developments in India and in the World: Gravitational Waves"
        ]
    },
    {
        "subsection": "IT, Communication, AI & Robotics",
        "items": [
            "Ministry of Communication and information Technology",
            "Government initiatives in ICT",
            "Cyber Law",
            "Computer Terminology and Fundamental",
            "History of Computers",
            "Types of Computers",
            "Mobile Generations and Technology",
            "Definition and Impact of ICT on Society",
            "Evolution of Telecommunication",
            "Media Transmission technology",
            "Networking: Bluetooth, WIFI Hotspot",
            "National E Governance Plan",
            "Net Neutrality",
            "Internet of Things",
            "Big Data Initiative and Privacy",
            "Cyber crime and security",
            "Spectrum",
            "Quantum computing",
            "Application of Superconductors",
            "Types and Applications of LASERS",
            "Artificial Intelligence and Application",
            "Advantages and Disadvantages of Artificial Intelligence",
            "Classification of Robots",
            "Applications of Robotics",
            "What is Nanoscience and Nanotechnology?",
            "Origination of Nanoscience and Technology",
            "Basics of Nanoscience",
            "Nanomaterials",
            "Applications of nanotechnology"
        ]
    },
    {
        "subsection": "Defence & Nuclear Technology",
        "items": [
            "Defence Technology Organizations",
            "Missile system and classification",
            "Ballistic vs Cruise Missile",
            "Integrated Guided Missile Development Programme",
            "Unmanned Aerial Vehicle",
            "Other Government Initiatives in Defence",
            "Nuclear Energy and Nuclear Fuels",
            "Types of nuclear reactions (Fusion and Fission)",
            "Nuclear Programme in India",
            "Nuclear Organisations / Institutions",
            "Department of Atomic Energy",
            "BARC",
            "Radiation and Radioactivity",
            "Radiation Technologies and Applications",
            "Radioactive Waste and Nuclear Waste Management"
        ]
    },
    {
        "subsection": "Biotechnology & Biology",
        "items": [
            "Intellectual Property Rights (Meaning and Types)",
            "IPR and Agriculture",
            "Biotechnology in India",
            "Department of BT",
            "Various Fields of BT",
            "Genetics and Biotechnology",
            "Industrial genetics",
            "Genetic engineering",
            "DNA sequencing",
            "Biological fuel generation",
            "Global warming and the significance of fossils fuels",
            "Microbial Ecology Environmental Biotechnology",
            "Waste water and sewage treatment",
            "Landfilling technologies",
            "Microbes and the geological environment",
            "Plant and Forest biotechnology",
            "Animal and Insect biotechnology",
            "Food and Beverage Biotechnology",
            "Biotechnology and medicine",
            "Pharmaceuticals and biopharmaceuticals",
            "Protection of biotechnological inventions",
            "Patent protection Trade secrets",
            "Plant breeders’ rights",
            "Achievements of Biotechnology in different fields",
            "Designer Babies’ or Three Parents Babies",
            "Origin of Life and Cells",
            "Inheritance (Genetics)",
            "DNA, The Genetic Material",
            "Gene Expression",
            "Gene Regulation",
            "Mutation",
            "Recombinant DNA Technology",
            "Classification and Domains of Life",
            "General Biology/Classification of Living Things/Viruses",
            "Human & Animal Evolution",
            "Tissues",
            "Endocrine System: Hypothalamus",
            "Endocrine System: Pineal body (epiphysis)",
            "Endocrine System: Pituitary gland (hypophysis)",
            "Endocrine System: Thyroid",
            "Endocrine System: Adrenal glands",
            "Endocrine System: Reproductive glands",
            "Respiratory System: External and Internal Respiration",
            "Respiratory System in Humans and Animals",
            "The Transport System in Organisms",
            "Skeletal and Muscular Systems",
            "Reproductive System",
            "Excretory System",
            "Nutrition: Classification by Source of Energy and Carbon",
            "Plant & Animal Nutrition",
            "The Digestive System",
            "Photosynthesis",
            "Communicable diseases",
            "Non-Communicable diseases",
            "Economic Zoology: Beneficial animals",
            "Economic Zoology: Harmful animals"
        ]
    },
    {
        "subsection": "Physics & Cosmic Physics",
        "items": [
            "Waves",
            "Light",
            "Electromagnetic Spectrum",
            "Ray optics",
            "Reflection",
            "Refraction",
            "Dispersion",
            "Scattering of light",
            "Rayleigh scattering",
            "Raman Scattering",
            "Total Internal reflection",
            "Optical Illusions",
            "Mirage",
            "Looming",
            "Rainbow",
            "Twinkling of stars",
            "Plane Mirror",
            "Periscope",
            "Spherical mirror",
            "Concave mirror and Applications",
            "Convex mirror and Applications",
            "Concave lens and Applications",
            "Convex lens and Applications",
            "Defects of vision",
            "Myopia (nearsightedness) & Correction - concave lens",
            "Hypermetropia (farsightedness) & Correction - convex lens",
            "Astigmatism",
            "Cataract and Correction",
            "Ohm's law",
            "Type of material: Conductor",
            "Type of material: Insulators",
            "Type of material: Semiconductor",
            "Type of material: Superconductor",
            "Series and parallel connection",
            "Fuse",
            "Effects of current",
            "Chemical effect of current",
            "Electrolytic",
            "Non-electrolytic",
            "Ions (charged particles)",
            "Electroplating",
            "Galvanization",
            "Chrome plating",
            "Dynamo",
            "Motor",
            "Inverters",
            "Alternating current (AC) & Direct current (DC)",
            "Magnetic effect of current",
            "Electromagnetic induction",
            "Application of EMI",
            "Wireless charging",
            "Eddy current",
            "Latent heat",
            "Abnormal behavior of water",
            "Surface tension",
            "Cohesive force",
            "Adhesive force",
            "Applications of surface tension",
            "Capillarity",
            "Archimedes principle",
            "Gravitation",
            "Escape Velocity",
            "Galaxy",
            "Stars",
            "Planet",
            "Asteroids",
            "Satellite",
            "Comet",
            "Meteoroids, Meteors, Meteorites",
            "Chandrasekhar Limit",
            "White Dwarf",
            "Supernova Explosion",
            "Black Hole",
            "Kuiper Belt",
            "Heliosphere & Hydrogen Wall",
            "Interstellar",
            "Goldilocks Zone",
            "Force Carriers",
            "Electromagnetic Gravitation",
            "Antimatter, Dark Matter",
            "Higgs-Boson Theory",
            "Theory of General Relativity",
            "Gravitational Lensing",
            "Expansion of Universe",
            "Evidence of Dark Energy"
        ]
    },
    {
        "subsection": "Chemistry",
        "items": [
            "Matter",
            "Plasma",
            "Atom",
            "Quarks and their Types",
            "Up Quark: + 2/3 charge",
            "Down Quark: - 1/3 charge",
            "Isotopes",
            "Nuclear fusion & Nuclear fission (Cosmic/General Chemistry)",
            "Radioactivity & Alpha/Beta/Gamma decay",
            "Neutrinos",
            "Half-life",
            "Periodic Table",
            "Atomic Structure",
            "Metal and Non-Metals",
            "Acids and Bases",
            "Carbon, Allotropes, Hydrocarbon",
            "Phosphorous: Black-P (good conductor)",
            "Phosphorous: White -P (used in matchstick)",
            "Phosphorous: Red -P (used in matchstick)",
            "Graphite",
            "Ozone",
            "Halogen Family",
            "The Noble Gases",
            "Rare Earth Elements and Applications",
            "Types of Acids - Organic Acid, Formic acid, Acetic acid, Inorganic Acid",
            "Base",
            "Baking agents",
            "Chemical Explosives",
            "Soaps and Detergents: chemistry of Surfactants",
            "Important Chemistry Terms: Phosphorescence",
            "Important Chemistry Terms: Fluorescence",
            "Important Chemistry Terms: Luminescence",
            "Important Chemistry Terms: Bioluminescence",
            "Important Chemistry Terms: Efflorescence"
        ]
    }
]

csat = [
    {
        "subsection": "Basic Numeracy & Arithmetic",
        "items": [
            "Number System: Classification of Numbers",
            "Number System: Divisibility Rules",
            "Number System: Remainder Theorem",
            "Number System: Unit Digit & Number of Zeros",
            "Number System: Factors & Multiples",
            "Number System: Prime Numbers & Coprimes",
            "LCM and HCF: Basic Concepts",
            "LCM and HCF: Word Problems & Applications",
            "Fractions and Decimals: Comparison & Operations",
            "Simplification: BODMAS Rule",
            "Squares, Cubes, Square Roots & Cube Roots",
            "Surds and Indices: Laws & Comparison",
            "Percentage: Core Concepts & Successive Percentage Changes",
            "Percentage: Word Problems (Election, Population, etc.)",
            "Profit, Loss, and Discount: Basic Formulae",
            "Profit, Loss, and Discount: Marked Price & Successive Discounts",
            "Simple Interest (SI): Formula & Word Problems",
            "Compound Interest (CI): Formula & Installments",
            "Ratio and Proportion: Rules & Scaling",
            "Ratio and Proportion: Share Division & Coin Problems",
            "Partnership: Investment Ratio & Profit Distribution",
            "Mixture and Alligation: Weighted Average & Replacement Formulas",
            "Averages: Core Concept & Consecutive Numbers",
            "Averages: Weighted Average & Group Average Changes",
            "Problems on Ages & Word Problems",
            "Time and Work: Efficiency & Individual Work Rates",
            "Time and Work: Pipes and Cisterns",
            "Time, Speed, and Distance: Conversions & Relative Speed",
            "Time, Speed, and Distance: Average Speed & Train Problems",
            "Time, Speed, and Distance: Boats and Streams",
            "Time, Speed, and Distance: Circular Tracks & Races"
        ]
    },
    {
        "subsection": "Advanced Mathematics",
        "items": [
            "Algebra: Algebraic Identities & Factorization",
            "Algebra: Linear Equations in One & Two Variables",
            "Algebra: Quadratic Equations & Roots",
            "Mensuration 2D: Area and Perimeter of Triangles",
            "Mensuration 2D: Area and Perimeter of Quadrilaterals & Polygons",
            "Mensuration 2D: Circle properties, Area & Sector Area",
            "Mensuration 3D: Volume & Surface Area of Cube & Cuboid",
            "Mensuration 3D: Volume & Surface Area of Cylinder & Cone",
            "Mensuration 3D: Volume & Surface Area of Sphere & Hemisphere",
            "Permutations and Combinations (P&C): Factorial Notation",
            "Permutations and Combinations (P&C): Fundamental Principles of Counting",
            "Permutations and Combinations (P&C): Linear & Circular Arrangement",
            "Permutations and Combinations (P&C): Selection Rules",
            "Probability: Basic Terminology & Sample Space",
            "Probability: Classical, Empirical & Axiomatic Probability",
            "Probability: Independent Events & Conditional Probability",
            "Probability: Card Problems, Coin Problems & Dice Problems",
            "Set Theory: Venn Diagrams & Set Operations",
            "Progressions: Arithmetic Progression (AP) - Nth term & Sum",
            "Progressions: Geometric Progression (GP) - Nth term & Sum",
            "Clocks: Angle between Hands & Gain/Loss of Time",
            "Calendars: Odd Days Concept & Finding Day of Week"
        ]
    },
    {
        "subsection": "Data Interpretation & Sufficiency",
        "items": [
            "Data Interpretation: Reading and Analyzing Tables",
            "Data Interpretation: Simple & Grouped Bar Charts",
            "Data Interpretation: Single & Multiple Line Graphs",
            "Data Interpretation: Pie Charts & Degree-to-Percentage Conversions",
            "Data Interpretation: Caselets & Venn Diagram Interpretation",
            "Data Interpretation: Combined/Mixed Charts",
            "Data Sufficiency: Single and Multi-statement sufficiency analysis",
            "Data Sufficiency: Quantitative DS questions",
            "Data Sufficiency: Logical/Analytical DS questions"
        ]
    },
    {
        "subsection": "Logical & Verbal Reasoning",
        "items": [
            "Coding and Decoding: Letter Coding",
            "Coding and Decoding: Number Coding & Deciphering Messages",
            "Blood Relations: Family Tree Diagrams & Coded Relations",
            "Direction Sense Test: Compass points & Shadow Problems",
            "Direction Sense Test: Pythagoras theorem applications in directions",
            "Venn Diagrams: Syllogism - Two/Three/Four statement deductions",
            "Venn Diagrams: Syllogism - Possibility Cases & Reverse Syllogisms",
            "Logical Deductions: Logical Consistency and Connectives",
            "Alphabet Test: Alphabetic Order, Letter Pairs & Word Formation",
            "Alpha-Numeric Series: Missing Terms & Analogy Series",
            "Number Series: Arithmetic, Geometric, Fibonacci & Prime Pattern Series",
            "Ranking & Ordering: Position Ranking in a Row",
            "Ranking & Ordering: Comparison of Weights, Heights or Ages",
            "Mathematical Operations: Sign Substitutions & Equation Balancing",
            "Analogy and Classification: Words, Letters & Numbers",
            "Cubes and Dice: Cutting Cubes, Painted Cubes & Dice Faces"
        ]
    },
    {
        "subsection": "Analytical Reasoning & Puzzles",
        "items": [
            "Sitting Arrangement: Linear Arrangements (Facing North/South)",
            "Sitting Arrangement: Circular Arrangements (Facing Inward/Outward)",
            "Sitting Arrangement: Square and Rectangular Arrangements",
            "Puzzles: Scheduling (Days, Weeks, Months, Years)",
            "Puzzles: Grouping and Team Selection Puzzles",
            "Puzzles: Floor Puzzles & Box Puzzles",
            "Puzzles: Matrix/Grid puzzles with multiple variables",
            "Critical Reasoning: Drawing Conclusions & Inferences",
            "Critical Reasoning: Evaluating Arguments (Strong/Weak)",
            "Critical Reasoning: Identifying Assumptions",
            "Critical Reasoning: Course of Action & Decision Making scenarios",
            "Critical Reasoning: Cause and Effect, Assertion & Reason",
            "Non-Verbal Reasoning: Series, Analogy & Classification of Figures",
            "Non-Verbal Reasoning: Mirror Images and Water Images",
            "Non-Verbal Reasoning: Paper Folding and Paper Cutting",
            "Non-Verbal Reasoning: Completion of Incomplete Patterns",
            "Non-Verbal Reasoning: Counting of Figures (Triangles, Squares, Rectangles)"
        ]
    },
    {
        "subsection": "Reading Comprehension",
        "items": [
            "Comprehension: Finding the Central Theme/Main Idea of a Passage",
            "Comprehension: Drawing Critical Inferences & Conclusions",
            "Comprehension: Identifying Crucial Assumptions made by the author",
            "Comprehension: Finding Corollaries and Crux of the Passage",
            "Comprehension: Identifying Tone, Style & Author's Argumentative Structure",
            "Comprehension: Answering Direct/Factual questions from passages",
            "Comprehension: Vocabulary-based contextual questions"
        ]
    }
]


def clean_slug(text):
    text = re.sub(r'[\(\)]', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    text = text.strip()
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text

def get_item_slug(item):
    text = item
    for prefix in ["Buddhism:", "Jainism:", "Basic Concepts:", "Forests:", "Factors affecting productivity:", "Factors affecting the productivity of aquatic ecosystems:", "Population Ecology:", "Important Chemistry Terms:", "Number System:", "LCM and HCF:", "Fractions and Decimals:", "Simplification:", "Surds and Indices:", "Percentage:", "Profit, Loss, and Discount:", "Simple Interest (SI):", "Compound Interest (CI):", "Ratio and Proportion:", "Partnership:", "Mixture and Alligation:", "Averages:", "Time and Work:", "Time, Speed, and Distance:", "Algebra:", "Mensuration 2D:", "Mensuration 3D:", "Permutations and Combinations (P&C):", "Probability:", "Set Theory:", "Progressions:", "Clocks:", "Calendars:", "Data Interpretation:", "Data Sufficiency:", "Coding and Decoding:", "Blood Relations:", "Direction Sense Test:", "Venn Diagrams:", "Logical Deductions:", "Alphabet Test:", "Alpha-Numeric Series:", "Number Series:", "Ranking & Ordering:", "Mathematical Operations:", "Analogy and Classification:", "Cubes and Dice:", "Sitting Arrangement:", "Puzzles:", "Critical Reasoning:", "Non-Verbal Reasoning:", "Comprehension:"]:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()
            break
    return clean_slug(text)

def get_subsection_slug(subsection, item):
    if subsection == "Jainism and Buddhism":
        if item.startswith("Jainism:"):
            return "Jainism"
        elif item.startswith("Buddhism:"):
            return "Buddhism"
    return clean_slug(subsection)

def get_subject_folder(prefix):
    mapping = {
        "anc": "ancient_history",
        "med": "medieval_history",
        "mod": "modern_history",
        "art": "art_and_culture",
        "pgeo": "geography",
        "igeo": "geography",
        "env": "environment",
        "pol": "polity",
        "eco": "economy",
        "st": "science_and_tech",
        "csat": "csat"
    }
    return mapping.get(prefix, "general_studies")

def get_subject_display_name(prefix):
    mapping = {
        "anc": "Ancient Indian History",
        "med": "Medieval Indian History",
        "mod": "Modern Indian History",
        "art": "Indian Art & Culture",
        "pgeo": "Physical Geography",
        "igeo": "Geography of India",
        "env": "Environment & Ecology",
        "pol": "Polity & Constitution",
        "eco": "Economy & Social Issues",
        "st": "Science & Technology",
        "csat": "CSAT Aptitude"
    }
    return mapping.get(prefix, "General Studies")

def get_topic_template(item_name, subsection_name, subject_display_name, subject_folder, subsection_slug, item_slug):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{item_name} - UPSC Civil Services Study Guide | SJMaths</title>
    <meta name="description" content="Study guide for {item_name} (UPSC Civil Services Prelims & Mains). Access key concepts, syllabus details, prep checklist, and interactive practice questions.">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/upsc/{subject_folder}/{subsection_slug}/{item_slug}/">
    <meta name="keywords" content="{item_name}, UPSC {subject_display_name}, UPSC Prelims, Study Notes, Interactive Tracker">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=1780366323" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=1780366323"></noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=1780366323">

    <style>
        :root {{
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 10px 30px -5px rgba(212, 175, 55, 0.1);
            --accent-gradient: linear-gradient(135deg, #d4af37, #2980b9);
        }}
        body.dark-mode {{
            --glass-bg: rgba(25, 25, 25, 0.95);
            --glass-border: rgba(255, 255, 255, 0.05);
        }}
        .topic-container {{
            max-width: 900px;
            margin: 2rem auto;
            padding: 1.5rem 1.5rem 3rem;
            animation: fadeIn 0.5s ease-out;
        }}
        .breadcrumbs {{
            margin-bottom: 1.5rem;
            font-size: 0.9rem;
            color: var(--text-light);
        }}
        .breadcrumbs a {{
            color: #d4af37;
            text-decoration: none;
            font-weight: 500;
        }}
        .topic-header {{
            margin-bottom: 2rem;
            border-bottom: 1px solid rgba(0,0,0,0.05);
            padding-bottom: 1.5rem;
            text-align: center;
        }}
        body.dark-mode .topic-header {{
            border-bottom-color: rgba(255,255,255,0.05);
        }}
        .topic-header h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: clamp(1.8rem, 5vw, 2.5rem);
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            line-height: 1.2;
        }}
        .topic-header p {{
            color: var(--text-light);
            font-size: clamp(0.95rem, 2vw, 1.05rem);
            line-height: 1.6;
            max-width: 750px;
            margin: 0 auto;
        }}
        .card-premium {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 2rem;
            margin-bottom: 2rem;
        }}
        .card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            border-bottom: 2px solid #d4af37;
            padding-bottom: 0.5rem;
        }}
        .prep-checklist {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }}
        .checklist-item {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            background: rgba(0,0,0,0.01);
            border: 1px solid rgba(0,0,0,0.03);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        body.dark-mode .checklist-item {{
            background: rgba(255,255,255,0.01);
            border-color: rgba(255,255,255,0.03);
        }}
        .checklist-item:hover {{
            border-color: #d4af37;
            background: rgba(212,175,55,0.03);
        }}
        .checklist-checkbox {{
            appearance: none;
            width: 20px;
            height: 20px;
            border: 2px solid var(--text-light);
            border-radius: 6px;
            outline: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
            flex-shrink: 0;
        }}
        .checklist-checkbox::before {{
            content: "\\f00c";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            font-size: 0.75rem;
            color: #fff;
            display: none;
        }}
        .checklist-checkbox:checked {{
            background: var(--accent-gradient);
            border-color: transparent;
        }}
        .checklist-checkbox:checked::before {{
            display: block;
        }}
        .checklist-text {{
            font-size: 0.95rem;
            color: var(--text-dark);
            font-weight: 500;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body>
<div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem; margin: 0 0.4rem;"></i>
            <a href="/upsc/">UPSC Syllabus</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem; margin: 0 0.4rem;"></i>
            <span>{item_name}</span>
        </div>

        <div class="topic-header">
            <h1>{item_name}</h1>
            <p>Syllabus Reference: {subsection_name} ({subject_display_name})</p>
        </div>

        <div class="card-premium">
            <h2 class="card-title"><i class="fas fa-book-open"></i> Key Concepts & Study Notes</h2>
            <div style="line-height: 1.7; color: var(--text-dark);">
                <p>Detailed study guide and resources for <strong>{item_name}</strong> are currently being prepared. Check back soon for comprehensive explanations, summary diagrams, and expert preparation recommendations.</p>
                <h3 style="margin: 1.5rem 0 0.75rem 0; font-family: 'Outfit', sans-serif;">Key Dimensions of Study:</h3>
                <ul>
                    <li>Definition, scope, and foundational theories.</li>
                    <li>Relevance to General Studies Paper & Contemporary contexts.</li>
                    <li>Core applications and structural framework.</li>
                </ul>
            </div>
        </div>

        <div class="card-premium">
            <h2 class="card-title"><i class="fas fa-list-check"></i> Self-Evaluation Checklist</h2>
            <ul class="prep-checklist">
                <li class="checklist-item">
                    <input type="checkbox" class="checklist-checkbox" id="chk-concepts-{item_slug}">
                    <span class="checklist-text">Review and internalize core study notes</span>
                </li>
                <li class="checklist-item">
                    <input type="checkbox" class="checklist-checkbox" id="chk-pyqs-{item_slug}">
                    <span class="checklist-text">Practice previous year questions (PYQs)</span>
                </li>
                <li class="checklist-item">
                    <input type="checkbox" class="checklist-checkbox" id="chk-test-{item_slug}">
                    <span class="checklist-text">Attempt a self-evaluation mock test</span>
                </li>
            </ul>
        </div>
    </main>

    <div id="footer-container"></div>
    <button id="backToTop" class="back-to-top" aria-label="Back to Top"><i class="fas fa-arrow-up"></i></button>

    <script src="/assets/js/main.min.js?v=1780366323" defer></script>
    <script src="/assets/js/global-header.min.js?v=1780366323" defer></script>
    <script src="/assets/js/global-footer.min.js?v=1780366323" defer></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const checkboxes = document.querySelectorAll('.checklist-checkbox');
            const storageKey = 'upsc-microtopic-prep-checklist';
            const progress = JSON.parse(localStorage.getItem(storageKey)) || {{}};

            checkboxes.forEach(chk => {{
                if (progress[chk.id]) {{
                    chk.checked = true;
                }}
                chk.addEventListener('change', () => {{
                    progress[chk.id] = chk.checked;
                    localStorage.setItem(storageKey, JSON.stringify(progress));
                }});
                const parent = chk.closest('.checklist-item');
                if (parent) {{
                    parent.addEventListener('click', (e) => {{
                        if (e.target !== chk) {{
                            chk.checked = !chk.checked;
                            chk.dispatchEvent(new Event('change'));
                        }}
                    }});
                }}
            }});
        }});
    </script>
</body>
</html>"""

def render_list(data, prefix):
    html = ""
    idx = 1
    upsc_root = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc"
    subject_folder = get_subject_folder(prefix)
    subject_display_name = get_subject_display_name(prefix)
    
    for grp_idx, grp in enumerate(data):
        subsection_safe = grp["subsection"].replace('"', '&quot;')
        html += f'                        <details class="syllabus-subsection" data-prefix="{prefix}" data-grp-idx="{grp_idx}">\n'
        html += f'                            <summary class="subsection-summary">\n'
        html += f'                                <span class="subsection-title">{subsection_safe}</span>\n'
        html += f'                                <div class="subsection-meta">\n'
        html += f'                                    <span class="subsection-progress" id="{prefix}-prog-{grp_idx}">0/0</span>\n'
        html += f'                                    <i class="fas fa-chevron-down toggle-icon"></i>\n'
        html += f'                                </div>\n'
        html += f'                            </summary>\n'
        html += '                            <ul class="syllabus-list">\n'
        for item in grp["items"]:
            # Checkbox ID
            cb_id = f"{prefix}-mt-{idx}"
            
            # Generate slug and paths
            item_slug = get_item_slug(item)
            subsection_slug = get_subsection_slug(grp["subsection"], item)
            
            # Generate the file path and index.html file
            topic_dir = os.path.join(upsc_root, subject_folder, subsection_slug, item_slug)
            file_path = os.path.join(topic_dir, "index.html")
            
            # Check if directory exists, create if not
            if not os.path.exists(topic_dir):
                os.makedirs(topic_dir, exist_ok=True)
            
            # Create study guide template if file doesn't exist
            if not os.path.exists(file_path):
                file_content = get_topic_template(
                    item, 
                    grp["subsection"], 
                    subject_display_name, 
                    subject_folder, 
                    subsection_slug, 
                    item_slug
                )
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(file_content)
            
            # Form relative hyperlink path
            href_path = f"./{subject_folder}/{subsection_slug}/{item_slug}/"
            
            # Render syllabus-item
            html += f'                                <li class="syllabus-item"><input type="checkbox" class="syllabus-checkbox" id="{cb_id}"><a href="{href_path}" class="syllabus-link syllabus-text">{item}</a></li>\n'
            idx += 1
        html += '                            </ul>\n'
        html += '                        </details>\n'
    return html


# Build lists HTML
ancient_html = render_list(ancient_history, "anc")
medieval_html = render_list(medieval_history, "med")
modern_html = render_list(modern_history, "mod")
art_html = render_list(art_and_culture, "art")
physical_geo_html = render_list(physical_geography, "pgeo")
indian_geo_html = render_list(indian_geography, "igeo")
env_html = render_list(environment, "env")
polity_html = render_list(polity, "pol")
economy_html = render_list(economy, "eco")
science_html = render_list(science_tech, "st")
csat_html = render_list(csat, "csat")

# Create full HTML content
full_html = f"""<!DOCTYPE html><html lang="en"><head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UPSC Civil Services Syllabus 2026: Prelims Granular Micro-Topic Tracker | SJMaths</title>
    <meta name="description" content="Get the complete, exhaustive micro-topic syllabus for UPSC Civil Services Prelims (General Studies &amp; CSAT). Track every single subtopic with interactive checklists.">
    
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/upsc/">
    <meta name="keywords" content="UPSC Syllabus, UPSC Prelims Syllabus, Ancient History, Medieval History, Modern History, Geography, Indian Polity, CSAT Micro-Topics, UPSC Interactive Tracker, SJMaths">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Open Graph -->
    <meta property="og:title" content="UPSC Civil Services Exam Syllabus 2026 - Micro-Topic Tracker | SJMaths">
    <meta property="og:description" content="Access the complete micro-topic UPSC IAS syllabus with an interactive progress tracker. Cover all history, geography, polity, economy, science, and CSAT subtopics.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://sjmaths.com/upsc/">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="UPSC Civil Services Syllabus 2026 - Micro-Topic Tracker">
    <meta name="twitter:description" content="Detailed subject-wise syllabus for UPSC Prelims &amp; Mains with progress tracking.">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Outfit:wght@500;600;700;800&amp;display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=1780366323" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript>
        <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=1780366323">
    </noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=1780366323">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=1780366323">

    <style>
        /* Custom Premium Styles for UPSC Syllabus Page */
        :root {{
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 10px 30px -5px rgba(212, 175, 55, 0.1);
            --accent-gradient: linear-gradient(135deg, #d4af37, #2980b9);
        }}

        body.dark-mode {{
            --glass-bg: rgba(25, 25, 25, 0.95);
            --glass-border: rgba(255, 255, 255, 0.05);
            --shadow-lg: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
        }}

        .syllabus-container {{
            max-width: 1100px;
            margin: 2rem auto;
            padding: 2.5rem 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }}

        .syllabus-header {{
            text-align: center;
            margin-bottom: 3rem;
        }}

        .syllabus-header h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
        }}

        .syllabus-header p {{
            font-size: 1.1rem;
            color: var(--text-light);
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.6;
        }}

        /* Tabs System */
        .syllabus-tabs {{
            display: flex;
            justify-content: center;
            gap: 0.75rem;
            margin-bottom: 2.5rem;
            flex-wrap: wrap;
            border-bottom: 2px solid rgba(0, 0, 0, 0.05);
            padding-bottom: 1rem;
        }}

        body.dark-mode .syllabus-tabs {{
            border-bottom-color: rgba(255, 255, 255, 0.05);
        }}

        .tab-btn {{
            background: transparent;
            border: none;
            outline: none;
            padding: 0.75rem 1.5rem;
            font-family: 'Outfit', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            color: var(--text-light);
            cursor: pointer;
            border-radius: 30px;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .tab-btn:hover {{
            color: #d4af37;
            background: rgba(212, 175, 55, 0.05);
        }}

        .tab-btn.active {{
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        }}

        /* Tab Content Panel */
        .tab-panel {{
            display: none;
            animation: slideUp 0.4s ease-out;
        }}

        .tab-panel.active {{
            display: block;
        }}

        /* Grid Layout */
        .subjects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(48%, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }}

        @media (max-width: 768px) {{
            .subjects-grid {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Subject Card */
        .subject-card {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 1.75rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            overflow: hidden;
            max-height: 800px;
            display: flex;
            flex-direction: column;
        }}

        .subject-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 15px 35px -5px rgba(212, 175, 55, 0.15);
        }}

        .subject-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--accent-gradient);
        }}

        .subject-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-shrink: 0;
        }}

        .subject-title i {{
            color: #d4af37;
            opacity: 0.8;
        }}

        .subject-title a {{
            color: inherit;
            text-decoration: none;
            transition: color 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }}

        .subject-title a:hover {{
            color: #d4af37;
        }}

        /* Card scrollable area */
        .card-scrollable {{
            overflow-y: auto;
            flex-grow: 1;
            padding-right: 0.5rem;
        }}

        /* Custom Scrollbar for Subject Cards */
        .card-scrollable::-webkit-scrollbar {{
            width: 6px;
        }}

        .card-scrollable::-webkit-scrollbar-track {{
            background: transparent;
        }}

        .card-scrollable::-webkit-scrollbar-thumb {{
            background: rgba(212, 175, 55, 0.2);
            border-radius: 10px;
        }}

        .card-scrollable::-webkit-scrollbar-thumb:hover {{
            background: rgba(212, 175, 55, 0.4);
        }}

        /* Interactive Syllabus Checklist */
        .syllabus-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
        }}

        .syllabus-item {{
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            padding: 0.5rem 0.7rem;
            border-radius: 8px;
            transition: background-color 0.2s ease;
            cursor: pointer;
            border: 1px solid transparent;
        }}

        .syllabus-item:hover {{
            background: rgba(212, 175, 55, 0.03);
            border-color: rgba(212, 175, 55, 0.05);
        }}

        body.dark-mode .syllabus-item:hover {{
            background: rgba(255, 255, 255, 0.02);
            border-color: rgba(255, 255, 255, 0.05);
        }}

        .syllabus-checkbox {{
            appearance: none;
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border: 2px solid var(--text-light);
            border-radius: 5px;
            outline: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
            margin-top: 2px;
        }}

        .syllabus-checkbox::before {{
            content: "\\f00c";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            font-size: 0.7rem;
            color: #ffffff;
            display: none;
        }}

        .syllabus-checkbox:checked {{
            background: var(--accent-gradient);
            border-color: transparent;
        }}

        .syllabus-checkbox:checked::before {{
            display: block;
        }}

        .syllabus-text {{
            font-size: 0.9rem;
            color: var(--text-light);
            line-height: 1.4;
            transition: color 0.2s ease, text-decoration 0.2s ease;
        }}

        .syllabus-checkbox:checked + .syllabus-text {{
            color: var(--muted, #9ca3af);
            text-decoration: line-through;
        }}

        /* Tracker Progress Bar */
        .tracker-banner {{
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 1.5rem;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            flex-wrap: wrap;
        }}

        .tracker-info h2 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 0.25rem;
        }}

        .tracker-info p {{
            font-size: 0.9rem;
            color: var(--text-light);
        }}

        .tracker-progress-container {{
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-grow: 1;
            max-width: 500px;
            justify-content: flex-end;
        }}

        .progress-bar-wrapper {{
            background: rgba(0, 0, 0, 0.05);
            border-radius: 10px;
            height: 10px;
            width: 100%;
            overflow: hidden;
            position: relative;
        }}

        body.dark-mode .progress-bar-wrapper {{
            background: rgba(255, 255, 255, 0.1);
        }}

        .progress-bar-fill {{
            background: var(--accent-gradient);
            height: 100%;
            width: 0%;
            transition: width 0.4s ease-out;
            border-radius: 10px;
        }}

        .progress-percentage {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            color: #d4af37;
            min-width: 50px;
            text-align: right;
        }}

        /* Section Intro Alerts */
        .syllabus-intro-alert {{
            background: rgba(212, 175, 55, 0.05);
            border: 1px solid rgba(212, 175, 55, 0.15);
            border-radius: 12px;
            padding: 1.25rem;
            margin-bottom: 2rem;
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--text-dark);
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
        }}

        .syllabus-intro-alert i {{
            color: #d4af37;
            font-size: 1.2rem;
            margin-top: 0.2rem;
        }}

        /* Subsections - Collapsible details/summary */
        details.syllabus-subsection {{
            background: rgba(255, 255, 255, 0.4);
            border: 1px solid rgba(0, 0, 0, 0.05);
            border-radius: 8px;
            margin-bottom: 0.75rem;
            transition: all 0.3s ease;
            overflow: hidden;
        }}

        body.dark-mode details.syllabus-subsection {{
            background: rgba(255, 255, 255, 0.02);
            border-color: rgba(255, 255, 255, 0.05);
        }}

        details.syllabus-subsection[open] {{
            background: var(--glass-bg);
            border-color: rgba(212, 175, 55, 0.2);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        }}

        summary.subsection-summary {{
            padding: 0.8rem 1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            list-style: none;
            user-select: none;
        }}

        summary.subsection-summary::-webkit-details-marker {{
            display: none;
        }}

        .subsection-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-dark);
            margin: 0;
            padding: 0;
            border: none;
            text-transform: none;
            letter-spacing: normal;
            flex-grow: 1;
            padding-right: 1rem;
            text-align: left;
        }}

        .subsection-meta {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .subsection-progress {{
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.5rem;
            background: rgba(0, 0, 0, 0.05);
            color: var(--text-light);
            border-radius: 12px;
            white-space: nowrap;
            transition: all 0.2s ease;
        }}

        body.dark-mode .subsection-progress {{
            background: rgba(255, 255, 255, 0.08);
        }}

        .subsection-progress.completed {{
            background: rgba(46, 204, 113, 0.15);
            color: #2ecc71;
        }}

        .toggle-icon {{
            font-size: 0.8rem;
            color: var(--text-light);
            transition: transform 0.3s ease;
        }}

        details.syllabus-subsection[open] .toggle-icon {{
            transform: rotate(180deg);
            color: #d4af37;
        }}

        details.syllabus-subsection .syllabus-list {{
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            padding: 0.5rem;
            margin: 0;
            list-style: none;
        }}

        body.dark-mode details.syllabus-subsection .syllabus-list {{
            border-top-color: rgba(255, 255, 255, 0.05);
        }}

        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @keyframes slideUp {{
            from {{ opacity: 0; transform: translateY(15px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Badges */
        .badge-exam {{
            font-size: 0.75rem;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
            font-weight: 600;
            background: rgba(212, 175, 55, 0.1);
            color: #d4af37;
        }}

        /* Tab-specific progress badges */
        .tab-progress {{
            font-size: 0.8rem;
            margin-left: 6px;
            padding: 1px 6px;
            background: rgba(0, 0, 0, 0.06);
            border-radius: 10px;
            font-weight: 700;
            color: var(--text-light);
        }}

        .tab-btn.active .tab-progress {{
            background: rgba(255, 255, 255, 0.2);
            color: #ffffff;
        }}

        body.dark-mode .tab-progress {{
            background: rgba(255, 255, 255, 0.08);
        }}
    
        .syllabus-link:hover {{
            color: #d4af37 !important;
            border-bottom-color: #d4af37 !important;
        }}
    </style>

    <!-- Structured Data: Breadcrumbs -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://sjmaths.com/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "UPSC Syllabus",
          "item": "https://sjmaths.com/upsc/"
        }}
      ]
    }}
    </script>
</head>

<body>
    <!-- Skip to Content Link -->
<!-- Dynamic Header -->
    <div id="header-container"></div>

    <main class="syllabus-container" id="main-content">
        
        <!-- Header Section -->
        <div class="syllabus-header">
            <h1>UPSC Civil Services Syllabus</h1>
            <p>Comprehensive interactive micro-topic checklist for Prelims &amp; Mains preparation. Track, document, and master every single subtopic systematically.</p>
        </div>

        <!-- Progress Tracker Banner -->
        <div class="tracker-banner">
            <div class="tracker-info">
                <h2><span id="activeProgressTitle">History &amp; Art of India</span> Progress</h2>
                <p>Check off topics as you cover them. Your study progress is saved automatically.</p>
            </div>
            <div class="tracker-progress-container">
                <div class="progress-bar-wrapper">
                    <div class="progress-bar-fill" id="syllabusProgressBar"></div>
                </div>
                <div class="progress-percentage" id="syllabusProgressPercent">0%</div>
            </div>
        </div>

        <!-- Tabs Navigation -->
        <div class="syllabus-tabs">
            <button class="tab-btn active" data-tab="hist-culture">
                <i class="fas fa-landmark"></i> History &amp; Culture <span class="tab-progress" id="badge-hist-culture">(0%)</span>
            </button>
            <button class="tab-btn" data-tab="geography-env">
                <i class="fas fa-globe"></i> Geography &amp; Env <span class="tab-progress" id="badge-geography-env">(0%)</span>
            </button>
            <button class="tab-btn" data-tab="polity-eco">
                <i class="fas fa-scale-balanced"></i> Polity &amp; Economy <span class="tab-progress" id="badge-polity-eco">(0%)</span>
            </button>
            <button class="tab-btn" data-tab="csat-aptitude">
                <i class="fas fa-calculator"></i> CSAT Aptitude <span class="tab-progress" id="badge-csat-aptitude">(0%)</span>
            </button>
        </div>

        <!-- ==================== HISTORY & CULTURE PANEL ==================== -->
        <div class="tab-panel active" id="panel-hist-culture">
            <div class="syllabus-intro-alert">
                <i class="fas fa-circle-info"></i>
                <div>
                    Covers <strong>Ancient History, Medieval History, Modern Indian History</strong>, and <strong>Indian Art and Culture</strong> with every micro-topic mapped out.
                </div>
            </div>

            <div class="subjects-grid">
                
                <!-- Ancient History -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./ancient_history/">Ancient Indian History <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-scroll"></i>
                    </h2>
                    <div class="card-scrollable">
{ancient_html}                    </div>
                </div>

                <!-- Medieval History -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./medieval_history/">Medieval Indian History <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-tower-observation"></i>
                    </h2>
                    <div class="card-scrollable">
{medieval_html}                    </div>
                </div>

                <!-- Modern Indian History -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./modern_history/">Modern Indian History <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-hourglass-half"></i>
                    </h2>
                    <div class="card-scrollable">
{modern_html}                    </div>
                </div>

                <!-- Art and Culture -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./art_and_culture/">Indian Art &amp; Culture <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-palette"></i>
                    </h2>
                    <div class="card-scrollable">
{art_html}                    </div>
                </div>

            </div>
        </div>

        <!-- ==================== GEOGRAPHY PANEL ==================== -->
        <div class="tab-panel" id="panel-geography-env">
            <div class="syllabus-intro-alert">
                <i class="fas fa-circle-info"></i>
                <div>
                    Covers <strong>Physical Geography</strong> (Geomorphology, Oceanography, Climatology), <strong>Indian Geography</strong>, and <strong>Environment &amp; Ecology</strong>.
                </div>
            </div>

            <div class="subjects-grid">
                
                <!-- Physical Geography -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./geography/">Physical Geography <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-mountain"></i>
                    </h2>
                    <div class="card-scrollable">
{physical_geo_html}                    </div>
                </div>

                <!-- Indian Geography -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./geography/">Geography of India <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-map"></i>
                    </h2>
                    <div class="card-scrollable">
{indian_geo_html}                    </div>
                </div>

                <!-- Environment and Ecology -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./environment/">Environment &amp; Ecology <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-leaf"></i>
                    </h2>
                    <div class="card-scrollable">
{env_html}                    </div>
                </div>

            </div>
        </div>

        <!-- ==================== POLITY & ECONOMY PANEL ==================== -->
        <div class="tab-panel" id="panel-polity-eco">
            <div class="syllabus-intro-alert">
                <i class="fas fa-circle-info"></i>
                <div>
                    Covers <strong>Indian Polity and Governance</strong>, <strong>Indian Economy</strong>, and <strong>Science &amp; Technology</strong>.
                </div>
            </div>

            <div class="subjects-grid">
                
                <!-- Polity and Governance -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./polity/">Polity &amp; Constitution <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-scale-balanced"></i>
                    </h2>
                    <div class="card-scrollable">
{polity_html}                    </div>
                </div>

                <!-- Economy & Schemes -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./economy/">Economy &amp; Social Issues <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-sack-dollar"></i>
                    </h2>
                    <div class="card-scrollable">
{economy_html}                    </div>
                </div>

                <!-- Science & Technology -->
                <div class="subject-card">
                    <h2 class="subject-title">
                        <a href="./science_and_tech/">Science &amp; Technology <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-atom"></i>
                    </h2>
                    <div class="card-scrollable">
{science_html}                    </div>
                </div>

            </div>
        </div>

        <!-- ==================== CSAT & APTITUDE PANEL ==================== -->
        <div class="tab-panel" id="panel-csat-aptitude">
            <div class="syllabus-intro-alert">
                <i class="fas fa-circle-info"></i>
                <div>
                    The <strong>Civil Services Aptitude Test (CSAT)</strong> requires a qualifying score of <strong>33%</strong>. Checks basic numeracy, data interpretation, logical reasoning, and reading comprehension.
                </div>
            </div>

            <div class="subjects-grid">
                
                <!-- CSAT Section -->
                <div class="subject-card" style="grid-column: span 2;">
                    <h2 class="subject-title">
                        <a href="./csat/">CSAT Aptitude &amp; Reasoning <i class="fas fa-arrow-up-right-from-square" style="font-size: 0.8rem; opacity: 0.7;"></i></a>
                        <i class="fas fa-brain"></i>
                    </h2>
                    <div class="card-scrollable">
                        <div class="subjects-grid" style="gap: 1.5rem;">
{csat_html}                        </div>
                    </div>
                </div>

            </div>
        </div>

    </main>

    <div id="footer-container"></div>

    <button id="backToTop" class="back-to-top" aria-label="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script src="/assets/js/search.min.js?v=1780366323" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=1780366323" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=1780366323" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=1780366323" defer data-cfasync="false"></script>

    <!-- Tracker Interactive Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabPanels = document.querySelectorAll('.tab-panel');
            const activeProgressTitle = document.getElementById('activeProgressTitle');
            const progressBar = document.getElementById('syllabusProgressBar');
            const progressPercent = document.getElementById('syllabusProgressPercent');

            const tabTitles = {{
                'hist-culture': 'History &amp; Art of India',
                'geography-env': 'Geography &amp; Environment',
                'polity-eco': 'Polity &amp; Economy',
                'csat-aptitude': 'CSAT Aptitude'
            }};

            // Get current active tab ID
            function getActiveTab() {{
                const activeBtn = document.querySelector('.tab-btn.active');
                return activeBtn ? activeBtn.getAttribute('data-tab') : 'hist-culture';
            }}

            // Tab Switching
            tabButtons.forEach(button => {{
                button.addEventListener('click', () => {{
                    const targetTab = button.getAttribute('data-tab');

                    tabButtons.forEach(btn => btn.classList.remove('active'));
                    button.classList.add('active');

                    tabPanels.forEach(panel => {{
                        panel.classList.remove('active');
                        if (panel.id === `panel-${{targetTab}}`) {{
                            panel.classList.add('active');
                        }}
                    }});

                    if (activeProgressTitle) {{
                        activeProgressTitle.innerHTML = tabTitles[targetTab] || 'Syllabus';
                    }}
                    updateProgress();

                    document.querySelector('.syllabus-tabs').scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }});
            }});

            // Interactive Checkboxes & Local Storage
            const checkboxes = document.querySelectorAll('.syllabus-checkbox');
            const storedProgress = JSON.parse(localStorage.getItem('upsc-syllabus-progress')) || {{}};
            
            checkboxes.forEach(checkbox => {{
                const id = checkbox.id;
                if (storedProgress[id]) {{
                    checkbox.checked = true;
                }}

                // Save status changes
                checkbox.addEventListener('change', () => {{
                    storedProgress[checkbox.id] = checkbox.checked;
                    localStorage.setItem('upsc-syllabus-progress', JSON.stringify(storedProgress));
                    updateProgress();
                }});

                // Parent list item click logic
                const parent = checkbox.closest('.syllabus-item');
                if (parent) {{
                    parent.addEventListener('click', (e) => {{
                        if (e.target !== checkbox && e.target.tagName !== 'A') {{
                            checkbox.checked = !checkbox.checked;
                            checkbox.dispatchEvent(new Event('change'));
                        }}
                    }});
                }}
            }});

            // Recalculate percentage progress
            function updateProgress() {{
                const activeTab = getActiveTab();
                const tabs = ['hist-culture', 'geography-env', 'polity-eco', 'csat-aptitude'];
                
                tabs.forEach(tabId => {{
                    const panel = document.getElementById(`panel-${{tabId}}`);
                    if (!panel) return;
                    
                    const tabCheckboxes = panel.querySelectorAll('.syllabus-checkbox');
                    const total = tabCheckboxes.length;
                    const checked = Array.from(tabCheckboxes).filter(cb => cb.checked).length;
                    const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;
                    
                    const badge = document.getElementById(`badge-${{tabId}}`);
                    if (badge) {{
                        badge.textContent = `(${{percentage}}%)`;
                    }}
                    
                    if (tabId === activeTab) {{
                        if (progressBar) progressBar.style.width = `${{percentage}}%`;
                        if (progressPercent) progressPercent.textContent = `${{percentage}}%`;
                    }}
                }});

                // Recalculate and update sub-section checklist progress & badges
                const subsections = document.querySelectorAll('.syllabus-subsection');
                subsections.forEach(sub => {{
                    const prefix = sub.getAttribute('data-prefix');
                    const grpIdx = sub.getAttribute('data-grp-idx');
                    const subCheckboxes = sub.querySelectorAll('.syllabus-checkbox');
                    const subTotal = subCheckboxes.length;
                    const subChecked = Array.from(subCheckboxes).filter(cb => cb.checked).length;
                    
                    const progEl = document.getElementById(`${{prefix}}-prog-${{grpIdx}}`);
                    if (progEl) {{
                        progEl.textContent = `${{subChecked}}/${{subTotal}}`;
                        if (subChecked === subTotal && subTotal > 0) {{
                            progEl.classList.add('completed');
                        }} else {{
                            progEl.classList.remove('completed');
                        }}
                    }}
                }});
            }}

            updateProgress();
        }});
    </script>
</body></html>"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(full_html)

print("HTML syllabus page successfully built and written to:", HTML_PATH)
