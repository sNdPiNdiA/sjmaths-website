const fs = require('fs');
const path = require('path');
const { GoogleGenAI, Type } = require('@google/genai');

const baseDir = path.resolve(__dirname, '..');
const gsHistoryDir = path.join(baseDir, 'gs-question-bank', 'history', 'modern-india', 'advent-of-europeans');

// Retrieve the Gemini API key from the environment, or check for a local .env file
let apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    const dotenvPath = path.join(baseDir, '.env');
    if (fs.existsSync(dotenvPath)) {
        const dotenvContent = fs.readFileSync(dotenvPath, 'utf8');
        const match = dotenvContent.match(/GEMINI_API_KEY\s*=\s*([^\s#]+)/);
        if (match) {
            apiKey = match[1].trim().replace(/['"]/g, '');
        }
    }
}

let ai = null;
if (apiKey) {
    ai = new GoogleGenAI({ apiKey });
    console.log('✨ Running with Gemini API Key.');
} else {
    console.log('⚠️  No GEMINI_API_KEY found. Running in Local Seed Mode for Category 1.');
}

// Local Database of 40 Real Questions for Category 1 (01_Background_of_European_Expansion)
const LOCAL_QUESTIONS = {
    "Age_of_Discovery": {
        easy: [
            {
                question: "Which country initiated the Age of Discovery under the patronage of Prince Henry the Navigator?",
                options: ["Spain", "Portugal", "England", "France"],
                correct_index: 1,
                explanation: "Portugal was the pioneer of the Age of Discovery in the 15th century, heavily sponsored by Prince Henry the Navigator, who founded a school of navigation.",
                difficulty: "easy",
                tags: ["Portugal", "Prince Henry", "Age of Discovery"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            },
            {
                question: "Which navigator's expedition completed the first circumnavigation of the globe?",
                options: ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Bartolomeu Dias"],
                correct_index: 2,
                explanation: "Ferdinand Magellan's expedition completed the first circumnavigation of the Earth between 1519 and 1522, though Magellan himself died in the Philippines.",
                difficulty: "easy",
                tags: ["Magellan", "Circumnavigation", "Age of Discovery"],
                exam_tags: ["UPSC", "SSC", "Railway"]
            }
        ],
        medium: [
            {
                question: "Consider the following statements about the Treaty of Tordesillas (1494):\n1. It was brokered by Pope Alexander VI.\n2. It divided the non-Christian world between Spain and Portugal.\nWhich of the statements given above is/are correct?",
                options: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
                correct_index: 2,
                explanation: "The Treaty of Tordesillas was brokered by Pope Alexander VI and signed in 1494. It divided the newly discovered lands outside Europe between Spain and Portugal along a meridian line.",
                difficulty: "medium",
                tags: ["Treaty of Tordesillas", "Pope Alexander VI", "Spain", "Portugal"],
                exam_tags: ["UPSC", "State PCS"]
            },
            {
                question: "What was the primary economic motivation behind the European Age of Discovery?",
                options: ["To establish democratic states in the East", "To find direct sea routes to the spice-rich East and bypass Middle East monopolies", "To spread industrial machinery to Africa", "To export European finished cotton to India"],
                correct_index: 1,
                explanation: "The search for a direct maritime trade route to Asia to bypass Ottoman and Italian trade monopolies was the key driver of the Age of Discovery.",
                difficulty: "medium",
                tags: ["Spice Trade", "Maritime Route", "Motivations"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            }
        ],
        hard: [
            {
                question: "Which of the following was a key consequence of the Columbian Exchange initiated during the Age of Discovery?",
                options: ["The instant rise of democratic states in Asia", "The global transfer of crops, animals, and diseases between the Eastern and Western hemispheres", "The elimination of maritime piracy in the Atlantic", "The immediate colonization of Australia by Spain"],
                correct_index: 1,
                explanation: "The Columbian Exchange refers to the massive transfer of plants (potatoes, maize), animals (horses), and diseases (smallpox) between the Americas and Afro-Eurasia, shaping global agriculture and demography.",
                difficulty: "hard",
                tags: ["Columbian Exchange", "Consequences", "Global Trade"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ]
    },
    "Renaissance_and_Exploration": {
        easy: [
            {
                question: "Which Italian city is widely regarded as the birthplace of the Renaissance?",
                options: ["Rome", "Venice", "Florence", "Milan"],
                correct_index: 2,
                explanation: "Florence is famous as the cradle of the Renaissance, fostering art, science, and humanism in the 14th-15th centuries.",
                difficulty: "easy",
                tags: ["Renaissance", "Florence", "Italy"],
                exam_tags: ["SSC", "Railway"]
            },
            {
                question: "The intellectual movement of the Renaissance that focused on human potential and achievements is called:",
                options: ["Scholasticism", "Humanism", "Feudalism", "Mercantilism"],
                correct_index: 1,
                explanation: "Renaissance Humanism emphasized the value and agency of human beings, preferring critical thinking and evidence over medieval dogma.",
                difficulty: "easy",
                tags: ["Humanism", "Renaissance"],
                exam_tags: ["UPSC", "State PCS", "Teaching"]
            }
        ],
        medium: [
            {
                question: "How did the Renaissance directly impact the era of maritime exploration?",
                options: ["It discouraged curiosity about the physical world", "It fostered a scientific spirit of inquiry, astronomy, and improved geographical knowledge", "It led to the decline of shipbuilding industries", "It promoted isolationist policies in European kingdoms"],
                correct_index: 1,
                explanation: "The Renaissance encouraged observation, mapping, astronomy, and critical study of classical geography, which directly enabled long-distance voyages.",
                difficulty: "medium",
                tags: ["Renaissance Impact", "Scientific Inquiry", "Exploration"],
                exam_tags: ["UPSC", "State PCS"]
            },
            {
                question: "Which Renaissance technological invention played the most critical role in disseminating geographic maps and travel logs?",
                options: ["The Astrolabe", "The Printing Press", "The Magnetic Compass", "The Gunter's Scale"],
                correct_index: 1,
                explanation: "Johannes Gutenberg's printing press (c. 1440) allowed rapid copying of maps, navigational charts, and explorers' journals (like Marco Polo's travels).",
                difficulty: "medium",
                tags: ["Printing Press", "Gutenberg", "Maps"],
                exam_tags: ["State PCS", "SSC"]
            }
        ],
        hard: [
            {
                question: "Which of the following scholars revived the ancient Greek geographer Ptolemy’s 'Geographia' in Europe during the early Renaissance, influencing Columbus?",
                options: ["Leonardo da Vinci", "Jacopo d'Angelo", "Erasmus", "Nicolaus Copernicus"],
                correct_index: 1,
                explanation: "Jacopo d'Angelo translated Ptolemy's Geographia into Latin in 1406, reviving classical cartography and calculation of the Earth's circumference.",
                difficulty: "hard",
                tags: ["Ptolemy", "Cartography", "Geographia"],
                exam_tags: ["UPSC"]
            }
        ]
    },
    "Search_for_Sea_Route_to_India": {
        easy: [
            {
                question: "Who was the first European explorer to sail around the southern tip of Africa (Cape of Good Hope) in 1488?",
                options: ["Vasco da Gama", "Bartolomeu Dias", "Christopher Columbus", "Amerigo Vespucci"],
                correct_index: 1,
                explanation: "Bartolomeu Dias of Portugal was the first to round the Cape of Good Hope in 1488, opening the passage to the Indian Ocean.",
                difficulty: "easy",
                tags: ["Bartolomeu Dias", "Cape of Good Hope", "Portugal"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            },
            {
                question: "Which ocean did the European powers need to cross to reach India from the southern tip of Africa?",
                options: ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
                correct_index: 1,
                explanation: "After rounding the southern tip of Africa, ships sailed north-east through the Indian Ocean to reach the western coast of India.",
                difficulty: "easy",
                tags: ["Indian Ocean", "Maritime Route"],
                exam_tags: ["SSC", "Railway"]
            }
        ],
        medium: [
            {
                question: "Why was the Cape of Good Hope originally named the 'Cape of Storms' (Cabo das Tormentas) by Bartolomeu Dias?",
                options: ["Due to active underwater volcanic eruptions", "Due to the violent storms and strong currents encountered there", "Because it was ruled by a hostile local king", "Because of frequent pirate attacks"],
                correct_index: 1,
                explanation: "The region is famous for rough seas and unpredictable weather, which led Dias to name it the Cape of Storms before King John II of Portugal renamed it Cape of Good Hope to signify the route to India.",
                difficulty: "medium",
                tags: ["Cape of Storms", "Bartolomeu Dias", "King John II"],
                exam_tags: ["State PCS", "SSC"]
            },
            {
                question: "What crucial geographical aid helped Vasco da Gama navigate from Malindi on the African coast to Calicut, India?",
                options: ["A Spanish military escort", "The guidance of a Gujarati pilot named Majid/Kanha", "A newly invented GPS system", "A map provided by the Ottoman Sultan"],
                correct_index: 1,
                explanation: "Vasco da Gama hired an experienced Gujarati pilot (often identified as Ibn Majid or Kanji Malam) at Malindi, who knew the monsoon winds of the Indian Ocean.",
                difficulty: "medium",
                tags: ["Gujarati Pilot", "Ibn Majid", "Monsoon Winds"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ],
        hard: [
            {
                question: "Which of the following factors significantly delayed the Portuguese search for the sea route to India between Bartolomeu Dias's return (1488) and Vasco da Gama's departure (1497)?",
                options: ["The complete lack of funds in the Portuguese treasury", "The death of King John II and disputes over succession/treaties with Spain", "An invasion of Portugal by France", "A direct ban on exploration issued by the Pope"],
                correct_index: 1,
                explanation: "The period was marked by domestic political changes, negotiations resulting in the Treaty of Tordesillas (1494), and administrative planning under the new King Manuel I.",
                difficulty: "hard",
                tags: ["King John II", "King Manuel I", "Treaty of Tordesillas"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ]
    },
    "Fall_of_Constantinople": {
        easy: [
            {
                question: "In which year did the Ottoman Empire capture Constantinople, bringing an end to the Byzantine Empire?",
                options: ["1215", "1348", "1453", "1526"],
                correct_index: 2,
                explanation: "Constantinople fell to the Ottoman forces led by Sultan Mehmed II on May 29, 1453.",
                difficulty: "easy",
                tags: ["Constantinople", "1453", "Ottoman Empire"],
                exam_tags: ["UPSC", "State PCS", "SSC", "Railway"]
            },
            {
                question: "Who was the Ottoman Sultan responsible for the capture of Constantinople?",
                options: ["Mehmed II (The Conqueror)", "Suleiman the Magnificent", "Selim I", "Osman I"],
                correct_index: 0,
                explanation: "Sultan Mehmed II commanded the Ottoman army during the siege and capture of Constantinople in 1453.",
                difficulty: "easy",
                tags: ["Mehmed II", "Ottoman Empire"],
                exam_tags: ["SSC", "Railway"]
            }
        ],
        medium: [
            {
                question: "How did the fall of Constantinople directly trigger the European age of exploration?",
                options: ["It made land-based Silk Road routes completely safe for Europeans", "It blocked or heavily taxed traditional land-based trade routes to Asia, forcing Europeans to seek new maritime routes", "It led to the destruction of all shipyards in Europe", "It caused European kings to lose interest in spices"],
                correct_index: 1,
                explanation: "With the Ottomans controlling the Bosporus and land routes, European merchants faced exorbitant duties and hostility, necessitating direct sea routes to bypass them.",
                difficulty: "medium",
                tags: ["Silk Road", "Trade Routes", "Ottoman Control"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            },
            {
                question: "The flight of Greek scholars and classical manuscripts from Constantinople to Western Europe after 1453 directly contributed to:",
                options: ["The rise of the Feudal system", "The birth and acceleration of the Renaissance", "The beginning of the French Revolution", "The Industrial Revolution"],
                correct_index: 1,
                explanation: "Scholars fleeing the city brought rare Greek and Roman manuscripts to Italy, fueling humanism and the intellectual revival of the Renaissance.",
                difficulty: "medium",
                tags: ["Greek Scholars", "Byzantine Empire", "Renaissance"],
                exam_tags: ["UPSC", "State PCS", "Teaching"]
            }
        ],
        hard: [
            {
                question: "Which Byzantine Emperor was ruling Constantinople when it fell to the Ottomans?",
                options: ["Justinian I", "Constantine XI Palaiologos", "Basil II", "Alexios I Komnenos"],
                correct_index: 1,
                explanation: "Constantine XI Palaiologos was the final reigning Byzantine Emperor, dying in battle during the fall of the city on May 29, 1453.",
                difficulty: "hard",
                tags: ["Constantine XI", "Byzantine Empire"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ]
    },
    "Mercantilism": {
        easy: [
            {
                question: "Mercantilism was an economic theory that measured a nation's wealth primarily by:",
                options: ["The amount of gold and silver (bullion) it possessed", "The total population of its cities", "The level of agricultural freedom of its peasants", "The number of democratic reforms enacted"],
                correct_index: 0,
                explanation: "Mercantilism emphasized accumulating bullion through a favorable balance of trade (exporting more than importing).",
                difficulty: "easy",
                tags: ["Mercantilism", "Bullion", "Balance of Trade"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            },
            {
                question: "Under mercantilist theory, colonies were viewed primarily as:",
                options: ["Independent trading partners", "Sources of raw materials and exclusive markets for the mother country's manufactured goods", "Areas for spreading democratic values", "Tourist destinations"],
                correct_index: 1,
                explanation: "Colonies existed solely to enrich the home country by supplying raw materials and purchasing finished products.",
                difficulty: "easy",
                tags: ["Colonies", "Mercantilism"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ],
        medium: [
            {
                question: "Which of the following is a key policy advocated by mercantilist thinkers?",
                options: ["Zero tariffs on all foreign imports", "High tariffs on imports and subsidies for domestic industries", "The complete abolition of state-chartered monopolies", "Promoting free trade across all nations"],
                correct_index: 1,
                explanation: "To protect domestic industries and prevent the outflow of gold/silver, mercantilist governments imposed protectionist tariffs.",
                difficulty: "medium",
                tags: ["Tariffs", "Protectionism", "Mercantilist Policy"],
                exam_tags: ["State PCS", "SSC"]
            },
            {
                question: "How did mercantilism influence the behavior of European charter companies in India?",
                options: ["It encouraged them to cooperate and share profits", "It drove them to establish monopolies, use military force to eliminate rivals, and capture trading centers", "It led to a complete focus on cultural charity", "It discouraged companies from trading in spices"],
                correct_index: 1,
                explanation: "Mercantilism was a zero-sum theory: one nation's gain was another's loss. This fostered intense rivalry, fortifications, and naval wars in India.",
                difficulty: "medium",
                tags: ["Trade Monopolies", "Charter Companies", "Rivalry"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ],
        hard: [
            {
                question: "Which of the following laws passed by the British Parliament in the 17th century represents a classic example of mercantilist regulation?",
                options: ["The Magna Carta", "The Navigation Acts", "The Bill of Rights", "The Regulating Act of 1773"],
                correct_index: 1,
                explanation: "The English Navigation Acts restricted colonial trade to English ships and ports, a quintessential mercantilist policy designed to maximize English shipping profits.",
                difficulty: "hard",
                tags: ["Navigation Acts", "British Parliament", "Mercantilism"],
                exam_tags: ["UPSC"]
            }
        ]
    },
    "Spice_Trade": {
        easy: [
            {
                question: "Which spice was known as 'Black Gold' in ancient and medieval Europe due to its extremely high value?",
                options: ["Cardamom", "Cinnamon", "Black Pepper", "Cloves"],
                correct_index: 2,
                explanation: "Black pepper was highly prized for food preservation and seasoning, and was traded at values comparable to gold.",
                difficulty: "easy",
                tags: ["Black Gold", "Black Pepper", "Spices"],
                exam_tags: ["UPSC", "State PCS", "SSC", "Railway"]
            },
            {
                question: "Which region on the western coast of India was the primary hub of the spice trade and the destination of early European navigators?",
                options: ["Coromandel Coast", "Malabar Coast", "Konkan Coast", "Bengal Coast"],
                correct_index: 1,
                explanation: "The Malabar Coast (especially ports like Calicut, Cochin, and Cannanore) was the epicenter of pepper and cardamom cultivation and export.",
                difficulty: "easy",
                tags: ["Malabar Coast", "Calicut", "Spice Trade"],
                exam_tags: ["SSC", "Railway"]
            }
        ],
        medium: [
            {
                question: "Before the discovery of the direct sea route by the Portuguese, which two groups controlled the transit of spice trade from India to Europe?",
                options: ["Chinese and Spanish merchants", "Arab/Muslim merchants in the Indian Ocean and Italian city-states (Venice/Genoa) in Europe", "English and French companies", "Danish and Dutch traders"],
                correct_index: 1,
                explanation: "Arab merchants managed the maritime and land routes across the Middle East, while Venice and Genoa monopolized the distribution within Europe.",
                difficulty: "medium",
                tags: ["Venice", "Genoa", "Arab Merchants", "Monopoly"],
                exam_tags: ["UPSC", "State PCS"]
            },
            {
                question: "Why were spices so critical to Europeans in the medieval and early modern era?",
                options: ["They were used to manufacture early maritime vessels", "They were essential for preserving meat during winters and masking the taste of spoiled food", "They were used as primary building materials", "They were a major source of fresh drinking water"],
                correct_index: 1,
                explanation: "Lack of refrigeration meant livestock was slaughtered in autumn, and spices (salt, pepper, cloves) were vital to preserve meat and make it palatable.",
                difficulty: "medium",
                tags: ["Food Preservation", "Meat Preservation"],
                exam_tags: ["State PCS", "SSC"]
            }
        ],
        hard: [
            {
                question: "Which archipelago in modern Indonesia was historically known as the 'Spice Islands' due to its exclusive production of nutmeg and cloves?",
                options: ["Sumatra", "Java", "Moluccas (Maluku Islands)", "Philippines"],
                correct_index: 2,
                explanation: "The Moluccas were the only source of highly valuable cloves, nutmeg, and mace in the world, leading to intense wars between the Portuguese, Dutch, and English.",
                difficulty: "hard",
                tags: ["Spice Islands", "Moluccas", "Nutmeg", "Cloves"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ]
    },
    "Navigation_Technology": {
        easy: [
            {
                question: "Which navigational instrument, adopted from Arab mariners, allowed sailors to determine their latitude by measuring the angle of the sun or stars?",
                options: ["Telescope", "Astrolabe", "Barometer", "Chronometer"],
                correct_index: 1,
                explanation: "The astrolabe (and later sextant) measured the altitude of celestial bodies to calculate a ship's latitude.",
                difficulty: "easy",
                tags: ["Astrolabe", "Latitude", "Navigation Instruments"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            },
            {
                question: "What type of fast, highly maneuverable Portuguese ship, developed in the 15th century, used lateen (triangular) sails to sail against the wind?",
                options: ["Galleon", "Caravel", "Frigate", "Junk"],
                correct_index: 1,
                explanation: "The Caravel was a shallow-draft vessel with lateen sails that allowed sailing close to the wind (tacking), making open-ocean voyages possible.",
                difficulty: "easy",
                tags: ["Caravel", "Lateen Sails", "Shipbuilding"],
                exam_tags: ["UPSC", "SSC", "Railway"]
            }
        ],
        medium: [
            {
                question: "The introduction of the magnetic compass to European mariners originally originated from which civilization?",
                options: ["Ancient Egypt", "China", "Maya", "Mesoamerica"],
                correct_index: 1,
                explanation: "The magnetic compass was invented in China during the Han Dynasty and spread to Europe via the Silk Road and Arab merchants by the 12th-13th centuries.",
                difficulty: "medium",
                tags: ["Magnetic Compass", "China", "Navigation History"],
                exam_tags: ["State PCS", "SSC"]
            },
            {
                question: "What does the nautical practice of 'tacking' refer to?",
                options: ["Throwing cargo overboard to save weight", "Sailing in a zigzag pattern to move forward against an oncoming wind", "Drawing map lines using ink", "Fastening sails using iron nails"],
                correct_index: 1,
                explanation: "Lateen-rigged caravels could sail at an angle to the wind, enabling ships to return home against prevailing trade winds.",
                difficulty: "medium",
                tags: ["Tacking", "Lateen Sails", "Wind Patterns"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ],
        hard: [
            {
                question: "The invention of which instrument in the 18th century finally solved the critical problem of calculating longitude at sea?",
                options: ["The Magnetic Compass", "The Marine Chronometer", "The Lead Line", "The Traverse Board"],
                correct_index: 1,
                explanation: "John Harrison invented the marine chronometer, an extremely accurate clock that kept Greenwich Mean Time (GMT) at sea, allowing sailors to calculate longitude.",
                difficulty: "hard",
                tags: ["Marine Chronometer", "John Harrison", "Longitude"],
                exam_tags: ["UPSC"]
            }
        ]
    },
    "Political_Conditions_in_India": {
        easy: [
            {
                question: "Which major empire was dominant in Northern India when the Portuguese arrived in 1498?",
                options: ["Mughal Empire", "Delhi Sultanate (Lodi Dynasty)", "Gupta Empire", "Maurya Empire"],
                correct_index: 1,
                explanation: "In 1498, Sikandar Lodi was ruling the Delhi Sultanate. The Mughal Empire was established later in 1526 by Babur.",
                difficulty: "easy",
                tags: ["Delhi Sultanate", "Sikandar Lodi", "1498"],
                exam_tags: ["UPSC", "State PCS", "SSC", "Railway"]
            },
            {
                question: "The ruler of Calicut who welcomed Vasco da Gama in 1498 held the hereditary title of:",
                options: ["Zamorin (Samutiri)", "Peshwa", "Nizam", "Nawab"],
                correct_index: 0,
                explanation: "The Zamorin (ruler of Calicut) received Vasco da Gama and allowed him to trade, though disputes arose soon after.",
                difficulty: "easy",
                tags: ["Zamorin", "Calicut", "1498"],
                exam_tags: ["SSC", "Railway"]
            }
        ],
        medium: [
            {
                question: "Which independent kingdom in Southern India was the main rival of the Bahmani Sultanate when the Europeans arrived?",
                options: ["Maratha Kingdom", "Vijayanagara Empire", "Chola Empire", "Chera Kingdom"],
                correct_index: 1,
                explanation: "The Vijayanagara Empire (then under the Tuluva dynasty) ruled most of South India and was the dominant political and military force in the region.",
                difficulty: "medium",
                tags: ["Vijayanagara Empire", "South India"],
                exam_tags: ["UPSC", "State PCS"]
            },
            {
                question: "What was the political state of the Deccan region in India during the late 15th and early 16th centuries?",
                options: ["It was unified under a single emperor", "The Bahmani Kingdom had fractured into five independent Deccan Sultanates", "It was completely uninhabited", "It was under direct rule of the King of Portugal"],
                correct_index: 1,
                explanation: "The collapse of Bahmani power led to the rise of Ahmadnagar, Bijapur, Golconda, Bidar, and Berar, creating local rivalries that Europeans exploited.",
                difficulty: "medium",
                tags: ["Bahmani Sultanate", "Deccan Sultanates", "Bijapur"],
                exam_tags: ["UPSC", "State PCS", "SSC"]
            }
        ],
        hard: [
            {
                question: "Which local ruler of Goa did Afonso de Albuquerque defeat in 1510 to capture the port city for Portugal?",
                options: ["Yusuf Adil Shah of Bijapur", "Krishnadevaraya of Vijayanagara", "Nizam-ul-Mulk of Ahmadnagar", "Bahadur Shah of Gujarat"],
                correct_index: 0,
                explanation: "Albuquerque allied with the Hindu pirate/admiral Timoja to capture Goa from the Sultan of Bijapur, Yusuf Adil Shah, in 1510.",
                difficulty: "hard",
                tags: ["Yusuf Adil Shah", "Bijapur", "Goa Capture 1510", "Albuquerque"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ]
    }
};

// Helper to format topic/folder names into readable text
function formatTopicName(folderName) {
    return folderName.replace(/_/g, ' ');
}

// Find all categories and topics
function getTopicsList() {
    const list = [];
    if (!fs.existsSync(gsHistoryDir)) {
        console.error(`Base directory does not exist: ${gsHistoryDir}`);
        return list;
    }

    const categories = fs.readdirSync(gsHistoryDir).filter(name => {
        const fullPath = path.join(gsHistoryDir, name);
        return fs.statSync(fullPath).isDirectory() && /^\d+_/.test(name);
    });

    categories.forEach(cat => {
        const catPath = path.join(gsHistoryDir, cat);
        const topics = fs.readdirSync(catPath).filter(name => {
            const fullPath = path.join(catPath, name);
            return fs.statSync(fullPath).isDirectory();
        });

        topics.forEach(topic => {
            list.push({
                categoryFolder: cat,
                categoryName: formatTopicName(cat.replace(/^\d+_/, '')),
                topicFolder: topic,
                topicName: formatTopicName(topic),
                fullPath: path.join(catPath, topic)
            });
        });
    });

    return list;
}

// Generate placeholder questions when API is missing
function generatePlaceholders(topicInfo, syllabusRef) {
    const formatted = topicInfo.topicName;
    return {
        easy: [
            {
                question: `Which of the following is a primary fact related to the history of ${formatted}?`,
                options: ["Option A (Correct answer)", "Option B (Incorrect)", "Option C (Incorrect)", "Option D (Incorrect)"],
                correct_index: 0,
                explanation: `This is a sample explanation for the easy question on ${formatted}.`,
                difficulty: "easy",
                tags: [formatted, topicInfo.categoryName],
                exam_tags: ["SSC", "Railway"],
                syllabus_ref: syllabusRef
            },
            {
                question: `In what century did the major events of ${formatted} take place?`,
                options: ["15th Century (Correct)", "12th Century", "19th Century", "20th Century"],
                correct_index: 0,
                explanation: `Most events of the Advent of Europeans took place starting from the late 15th century.`,
                difficulty: "easy",
                tags: [formatted],
                exam_tags: ["SSC"],
                syllabus_ref: syllabusRef
            }
        ],
        medium: [
            {
                question: `Consider the following statements regarding ${formatted}:\n1. It had a major impact on the trade of Western India.\n2. It led to rivalries among the European powers.\nWhich of the statements given above is/are correct?`,
                options: ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
                correct_index: 2,
                explanation: `Both statements are correct. These events had significant economic impacts and triggered European rivalries.`,
                difficulty: "medium",
                tags: [formatted, "European Trade"],
                exam_tags: ["UPSC", "State PCS"]
            },
            {
                question: `Which of the following was a primary cause that led to the development of ${formatted}?`,
                options: ["The search for new trade routes", "A decrease in international demand", "The complete collapse of local empires", "A direct command by the United Nations"],
                correct_index: 0,
                explanation: `The search for alternative trade routes was the main driver for the advent of Europeans.`,
                difficulty: "medium",
                tags: [formatted],
                exam_tags: ["State PCS", "SSC"]
            }
        ],
        hard: [
            {
                question: `Analyze the geopolitical shift in the Indian Ocean region caused by the rise of ${formatted}. Which statement represents the most accurate analysis?`,
                options: ["It established a century-long naval dominance for regional players", "It shifted maritime trade hegemony from Arab/Gujarati networks to European armed trade monopolies", "It had zero impact on the inland rulers of India", "It caused a complete cessation of all agricultural production in Southern India"],
                correct_index: 1,
                explanation: `The arrival of Europeans, especially starting with the Portuguese Estado da India, replaced peaceful trade routes with fortified, armed monopolies and cartaz systems.`,
                difficulty: "hard",
                tags: [formatted, "Naval Supremacy", "Geopolitics"],
                exam_tags: ["UPSC", "State PCS"]
            }
        ]
    };
}

// Generate the question set for a given topic
async function generateForTopic(topicInfo) {
    const syllabusRef = `history/modern-india/advent-of-europeans/${topicInfo.categoryFolder}/${topicInfo.topicFolder}`;

    // Skip if already populated with real questions
    const easyPath = path.join(topicInfo.fullPath, 'mcq_easy.json');
    if (fs.existsSync(easyPath)) {
        try {
            const content = JSON.parse(fs.readFileSync(easyPath, 'utf8'));
            if (content.length > 0 && content[0].question) {
                const firstQ = content[0].question;
                if (!firstQ.includes('primary fact related to the history of') && !firstQ.includes('Option A (Correct answer)')) {
                    console.log(`\n⏭️  [SKIPPING] ${topicInfo.categoryName} -> ${topicInfo.topicName} (already has real questions)`);
                    return;
                }
            }
        } catch (e) {
            // Proceed to generate if file is corrupt or empty
        }
    }

    console.log(`\n--------------------------------------------------`);
    console.log(`[PROCESSING] ${topicInfo.categoryName} -> ${topicInfo.topicName}`);
    console.log(`Syllabus Ref: ${syllabusRef}`);

    let data = null;

    // Check if we have pre-written real questions for this topic
    if (LOCAL_QUESTIONS[topicInfo.topicFolder]) {
        console.log('📦 Found pre-written questions in Local Database.');
        data = LOCAL_QUESTIONS[topicInfo.topicFolder];
    } else if (ai) {
        // Run with Gemini API
        console.log('🤖 Requesting Gemini API...');
        const prompt = `
        You are an expert historian and exam paper designer for elite civil services examinations (like UPSC Civil Services and State PCS) and major SSC/Railway exams.
        Your task is to generate exactly 5 high-quality, syllabus-aligned Multiple Choice Questions (MCQs) for the microtopic: "${topicInfo.topicName}" under the broader topic: "${topicInfo.categoryName}".
        
        You must generate:
        - Exactly 2 "easy" difficulty questions (primarily factual but conceptually clear).
        - Exactly 2 "medium" difficulty questions (requiring analytical deduction or multiple statements).
        - Exactly 1 "hard" difficulty question (challenging, requiring deep historical analysis, multi-statement evaluation, or assertion-reason style).

        Guidelines:
        1. Ensure all options are realistic and plausible.
        2. Provide a detailed, historically accurate explanation for the correct answer.
        3. Include metadata tags for each question:
           - tags: array of strings containing relevant entities (e.g., historical personalities, treaties, battles, acts, locations).
           - exam_tags: array of strings indicating target exams (choose from: ['UPSC', 'State PCS', 'SSC', 'Railway', 'Teaching']).
           - difficulty: 'easy', 'medium', or 'hard'.
           - syllabus_ref: "${syllabusRef}".
        4. Provide the result in the exact JSON format specified by the response schema.
        `;

        try {
            const response = await ai.models.generateContent({
                model: 'gemini-2.5-flash',
                contents: prompt,
                config: {
                    responseMimeType: "application/json",
                    responseSchema: {
                        type: Type.OBJECT,
                        properties: {
                            easy: {
                                type: Type.ARRAY,
                                description: "Exactly 2 easy difficulty questions",
                                items: {
                                    type: Type.OBJECT,
                                    properties: {
                                        id: { type: Type.STRING },
                                        question: { type: Type.STRING },
                                        options: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        correct_index: { type: Type.INTEGER },
                                        explanation: { type: Type.STRING },
                                        difficulty: { type: Type.STRING },
                                        tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        exam_tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        syllabus_ref: { type: Type.STRING }
                                    },
                                    required: ["id", "question", "options", "correct_index", "explanation", "difficulty", "tags", "exam_tags", "syllabus_ref"]
                                }
                            },
                            medium: {
                                type: Type.ARRAY,
                                description: "Exactly 2 medium difficulty questions",
                                items: {
                                    type: Type.OBJECT,
                                    properties: {
                                        id: { type: Type.STRING },
                                        question: { type: Type.STRING },
                                        options: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        correct_index: { type: Type.INTEGER },
                                        explanation: { type: Type.STRING },
                                        difficulty: { type: Type.STRING },
                                        tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        exam_tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        syllabus_ref: { type: Type.STRING }
                                    },
                                    required: ["id", "question", "options", "correct_index", "explanation", "difficulty", "tags", "exam_tags", "syllabus_ref"]
                                }
                            },
                            hard: {
                                type: Type.ARRAY,
                                description: "Exactly 1 hard difficulty question",
                                items: {
                                    type: Type.OBJECT,
                                    properties: {
                                        id: { type: Type.STRING },
                                        question: { type: Type.STRING },
                                        options: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        correct_index: { type: Type.INTEGER },
                                        explanation: { type: Type.STRING },
                                        difficulty: { type: Type.STRING },
                                        tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        exam_tags: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        syllabus_ref: { type: Type.STRING }
                                    },
                                    required: ["id", "question", "options", "correct_index", "explanation", "difficulty", "tags", "exam_tags", "syllabus_ref"]
                                }
                            }
                        },
                        required: ["easy", "medium", "hard"]
                    }
                }
            });

            data = JSON.parse(response.text);
        } catch (err) {
            console.error(`❌ Gemini API error for topic ${topicInfo.topicFolder}:`, err.message);
            console.log('Falling back to schema placeholders for this topic...');
            data = generatePlaceholders(topicInfo, syllabusRef);
        }
    } else {
        // Fallback: local placeholders
        console.log('📝 Generating schema placeholders (Local Fallback).');
        data = generatePlaceholders(topicInfo, syllabusRef);
    }

    if (data) {
        // Adjust IDs and inject proper syllabus_ref
        const cleanData = (qList, prefix) => {
            return qList.map((q, idx) => ({
                ...q,
                id: `${prefix}-${topicInfo.topicFolder.toLowerCase()}-${idx + 1}`,
                syllabus_ref: syllabusRef
            }));
        };

        const easyQs = cleanData(data.easy || [], 'mcq-easy');
        const mediumQs = cleanData(data.medium || [], 'mcq-medium');
        const hardQs = cleanData(data.hard || [], 'mcq-hard');

        // Write files
        fs.writeFileSync(path.join(topicInfo.fullPath, 'mcq_easy.json'), JSON.stringify(easyQs, null, 2), 'utf8');
        fs.writeFileSync(path.join(topicInfo.fullPath, 'mcq_medium.json'), JSON.stringify(mediumQs, null, 2), 'utf8');
        fs.writeFileSync(path.join(topicInfo.fullPath, 'mcq_hard.json'), JSON.stringify(hardQs, null, 2), 'utf8');

        console.log(`✅ Success: Generated and saved 5 tagged MCQs to ${topicInfo.topicFolder}`);
    }
}

// Main execution function
async function main() {
    const topics = getTopicsList();
    console.log(`Found ${topics.length} total topics under Modern India: Advent of Europeans.`);

    // Check arguments for filtering
    const categoryFilter = process.argv[2]; // e.g., "01_Background_of_European_Expansion"
    const limitArg = process.argv[3];       // e.g., limit to 3 topics
    
    let filteredTopics = topics;
    if (categoryFilter) {
        filteredTopics = topics.filter(t => t.categoryFolder === categoryFilter);
        console.log(`Filtering by category "${categoryFilter}". Match count: ${filteredTopics.length}`);
    }

    if (limitArg) {
        const limit = parseInt(limitArg, 10);
        filteredTopics = filteredTopics.slice(0, limit);
        console.log(`Limiting generation to first ${limit} topics.`);
    }

    for (const topic of filteredTopics) {
        await generateForTopic(topic);
        if (ai && filteredTopics.length > 1) {
            // Wait 1.5 seconds between requests only when calling the API to respect quotas
            await new Promise(resolve => setTimeout(resolve, 1500));
        }
    }

    console.log('\nAll targeted questions generated and tagged successfully.');
}

main().catch(console.error);
