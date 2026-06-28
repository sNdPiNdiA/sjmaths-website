import os
import re
import json

BASE_DIR = r"ssc-cgl/general-awareness/history-and-culture"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'ivc', 'inc', 'pj', 'aj', 'ssc', 'cgl', 'goi', 'inc', 'hra', 'hsra', 'sbi', 'lic', 'gsi', 'ibm', 'help', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between', 'or', 'life', 'major', 'era', 'sects', 'teachings', 'councils', 'findings', 'trade', 'sites', 'rig', 'later']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Fully separated, 100% unique custom mindmap branches for all 22 folders
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. INDUS VALLEY CIVILIZATION (General & Planning)
    if fl == 'indus-valley-civilization':
        return [
            {
                "label": "Origin & Chronology", "type": "branch", "date": "2500 - 1750 BC",
                "children": [
                    {
                        "label": "Discovery & Naming", "type": "sub", "date": "John Marshall",
                        "children": [
                            {"label": "Named 'Indus Valley Civilization' by John Marshall in 1924; first site Harappa found in 1921 by Daya Ram Sahni", "type": "leaf"},
                            {"label": "Also called Harappan Civilization (after type-site) or Bronze Age Civilization", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Geographical Range", "type": "sub", "date": "Boundaries",
                        "children": [
                            {"label": "Manda (J&K) in North; Daimabad (Maharashtra) in South; Alamgirpur (UP) in East; Sutkagan Dor (Baluchistan) in West", "type": "leaf"},
                            {"label": "Centered around Indus and Ghaggar-Hakra river valleys; covered ~1.3 million sq km", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Town Planning & Architecture", "type": "branch", "date": "Urban Design",
                "children": [
                    {
                        "label": "Grid System Layout", "type": "sub", "date": "Street Network",
                        "children": [
                            {"label": "Streets cut at right angles forming a gridiron pattern; houses built of standardized burnt bricks (ratio 1:2:4)", "type": "leaf"},
                            {"label": "Cities divided into an elevated western Citadel (for public buildings) and a Lower Town (residential)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Sanitation & Drainage", "type": "sub", "date": "Public Health",
                        "children": [
                            {"label": "Every house connected to street drains; drains covered with stone slabs or bricks and had manholes", "type": "leaf"},
                            {"label": "Water resources: Houses had private wells and bathrooms; extensive soak pits and cesspools installed", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. INDUS VALLEY CIVILIZATION (Major Sites, Findings, Trade)
    elif fl == 'indus-valley-civilization-major-sites-findings-trade':
        return [
            {
                "label": "Major Sites & Excavators", "type": "branch", "date": "Discoveries",
                "children": [
                    {
                        "label": "Harappa & Mohenjo-Daro", "type": "sub", "date": "1921 - 1922",
                        "children": [
                            {"label": "Harappa: Located on Ravi river (Pakistan); found 6 granaries in a row, coffin burial (R-37), clay mother goddess", "type": "leaf"},
                            {"label": "Mohenjo-Daro (Mound of the Dead): Located on Indus; found Great Bath, Great Granary, Assembly Hall, Bronze Dancing Girl, bearded priest", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Port Cities & Crafts", "type": "sub", "date": "Commercial Sites",
                        "children": [
                            {"label": "Lothal (Gujarat, Bhogava river): Dockyard (artificial tidal basin), double burials, fire altars, rice husk, ivory scale", "type": "leaf"},
                            {"label": "Chanhudaro (Sindh): Bead makers shop, inkwell, copper toy carts, only city without a citadel", "type": "leaf"},
                            {"label": "Surkotada (Gujarat): Unique stone fortifications, first actual horse bone remains found in IVC", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Ploughed Fields & Water Harvesters", "type": "sub", "date": "Agricultural Sites",
                        "children": [
                            {"label": "Kalibangan (Rajasthan): Pre-Harappan ploughed field, fire altars, wooden furrow, decorated brick floors, camel bones", "type": "leaf"},
                            {"label": "Dholavira (Kutch): Giant water reservoirs, check dams, stadium, unique 3-part city division, 10-sign inscription", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Trade & Seals", "type": "branch", "date": "Economic Life",
                "children": [
                    {
                        "label": "External Trade", "type": "sub", "date": "Mesopotamia",
                        "children": [
                            {"label": "Exports: Ivory, cotton (Sindon), copper, gold, beads; Imports: Lapis Lazuli (Badakhshan), Jade (Central Asia)", "type": "leaf"},
                            {"label": "Cuneiform tablets refer to Meluha (IVC) and trade stops at Dilmun (Bahrain) and Makan (Oman)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Seals & Script", "type": "sub", "date": "Archaeology",
                        "children": [
                            {"label": "Seals: Made of Steatite, rectangular or square; most famous is Pashupati Mahadeva (proto-Shiva) surrounded by animals", "type": "leaf"},
                            {"label": "Script: Pictographic and undeciphered; written in Boustrophedon style (right-to-left, then left-to-right)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. VEDIC AGE (General & Polity)
    elif fl == 'vedic-age':
        return [
            {
                "label": "Aryan Migration & Settlements", "type": "branch", "date": "1500 - 600 BC",
                "children": [
                    {
                        "label": "Origins & Theories", "type": "sub", "date": "Historiography",
                        "children": [
                            {"label": "Central Asian origin: Proposed by Max Muller (most accepted); Arctic home theory: Bal Gangadhar Tilak", "type": "leaf"},
                            {"label": "Tibet theory: Swami Dayanand Saraswati; original settlement region was Saptasindhu (land of 7 rivers)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Rig Vedic Rivers", "type": "sub", "date": "Geography",
                        "children": [
                            {"label": "Saraswati was the most sacred river (Nditarna); Sindhu (Indus) was the most mentioned river", "type": "leaf"},
                            {"label": "Modern equivalents: Vitasta (Jhelum), Asikni (Chenab), Parushni (Ravi), Vipasa (Beas), Sutudri (Sutlej)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Political Organization", "type": "branch", "date": "Polity",
                "children": [
                    {
                        "label": "Rig Vedic Polity", "type": "sub", "date": "Tribal Democracy",
                        "children": [
                            {"label": "Tribal state: Rajan (king) aided by Senani (commander), Purohita (priest), and Spas (spies)", "type": "leaf"},
                            {"label": "Democratic Assemblies: Sabha (select elders), Samiti (folk assembly), Vidatha (distributes spoils)", "type": "leaf"},
                            {"label": "Battle of Ten Kings (Dasrajan): Fought on Parushni; King Sudas defeated alliance of 10 tribes", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Later Vedic Polity", "type": "sub", "date": "Territorial States",
                        "children": [
                            {"label": "Kingship became hereditary; assemblies declined; emergence of Janapadas (territorial kingdoms)", "type": "leaf"},
                            {"label": "Emergence of permanent taxes: Bhaga (share of produce) and Bali; tax collectors called Bhagadugha", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. VEDIC AGE (Rig Vedic and Later Vedic Society, Literature)
    elif fl == 'vedic-age-rig-vedic-and-later-vedic-society-literature':
        return [
            {
                "label": "Vedic Society & Culture", "type": "branch", "date": "Society",
                "children": [
                    {
                        "label": "Rig Vedic Society", "type": "sub", "date": "Pastoralist Life",
                        "children": [
                            {"label": "Patriarchal, but women had high status: attended Sabha/Vidatha, composed hymns (Apala, Ghosha, Lopamudra)", "type": "leaf"},
                            {"label": "Wealth: Measured in cattle (Gau); guest called Goghana; no child marriage, sati, or purdah", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Later Vedic Society", "type": "sub", "date": "Shifts",
                        "children": [
                            {"label": "Varna system: Rig Veda 10th Mandala Purusha Sukta describes origin; later became rigid and birth-based", "type": "leaf"},
                            {"label": "Stages of Life: Gotra system emerged; Ashrama system defined (Brahmacharya, Grihastha, Vanaprastha, Sannyasa)", "type": "leaf"},
                            {"label": "Declining women status: Women barred from assemblies, child marriage begins, women equated to misery in texts", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Vedic Literature", "type": "branch", "date": "Literature",
                "children": [
                    {
                        "label": "Shruti & Smriti Texts", "type": "sub", "date": "Sacred Texts",
                        "children": [
                            {"label": "Rig Veda (10 Mandalas, 1028 hymns); Sama Veda (melodies/music); Yajur Veda (sacrificial rituals)", "type": "leaf"},
                            {"label": "Atharva Veda: Focuses on charms, spells, medicine; Brahmanas: Prose explanations of Vedic rituals", "type": "leaf"},
                            {"label": "Aranyakas: Forest books on mysticism; Upanishads: 108 philosophical dialogues (Vedanta)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Vedangas & Upavedas", "type": "sub", "date": "Auxiliaries",
                        "children": [
                            {"label": "Vedangas (six): Shiksha, Kalpa, Vyakarana, Nirukta, Chhanda, Jyotisha", "type": "leaf"},
                            {"label": "Upavedas: Ayurveda (medicine - Rig), Dhanurveda (archery - Yajur), Gandharvaveda (music - Sama), Shilpaveda (Atharva)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. BUDDHISM (General)
    elif fl == 'buddhism':
        return [
            {
                "label": "Buddha's Life Summary", "type": "branch", "date": "563 - 483 BC",
                "children": [
                    {
                        "label": "Chronology", "type": "sub", "date": "Siddhartha",
                        "children": [
                            {"label": "Born in Lumbini (Nepal) to Shuddhodana (Shakya king) & Mahamaya; raised by Gautami", "type": "leaf"},
                            {"label": "Left home at 29 (Mahabhinishkramana); attained Bodhi at Bodh Gaya; died at Kushinagar", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Philosophy & Doctrines", "type": "branch", "date": "Philosophies",
                "children": [
                    {
                        "label": "Core Doctrines", "type": "sub", "date": "Tenets",
                        "children": [
                            {"label": "Pratityasamutpada: Law of dependent origination (cause and effect); core of Buddhist logic", "type": "leaf"},
                            {"label": "Anatta (non-self/no soul), Anicca (impermanence of all things), and Nirvana (liberation from cycle)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "The Eightfold Path", "type": "sub", "date": "Ashtangika Marga",
                        "children": [
                            {"label": "Right view, right resolve, right speech, right action, right livelihood, right effort, right mindfulness, right concentration", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Sects of Buddhism", "type": "branch", "date": "Schools",
                "children": [
                    {
                        "label": "Hinayana & Mahayana", "type": "sub", "date": "Schisms",
                        "children": [
                            {"label": "Hinayana: Orthodox, Pali, self-discipline, views Buddha as teacher, individual salvation", "type": "leaf"},
                            {"label": "Mahayana: Progressive, Sanskrit, idol worship, views Buddha as god, Bodhisattva concept", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Vajrayana & Theravada", "type": "sub", "date": "Other Sects",
                        "children": [
                            {"label": "Vajrayana: Tantric form, rituals, magic spells; patronized by Pala rulers of Bengal", "type": "leaf"},
                            {"label": "Theravada: Oldest surviving branch; widespread in Sri Lanka, Myanmar, Thailand", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. BUDDHISM (Life, Teachings, Councils)
    elif fl == 'buddhism-life-of-buddha-teachings-councils':
        return [
            {
                "label": "Life Events & Symbols", "type": "branch", "date": "Symbols",
                "children": [
                    {
                        "label": "Five Great Events", "type": "sub", "date": "Panchamahasthana",
                        "children": [
                            {"label": "Birth: Symbolized by Lotus and Bull; Great Renunciation: Symbolized by Horse", "type": "leaf"},
                            {"label": "Enlightenment: Bodhi Tree; First Sermon: Dharma Chakra (Wheel); Death: Stupa", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Buddhist Councils", "type": "branch", "date": "Councils",
                "children": [
                    {
                        "label": "Councils 1 & 2", "type": "sub", "date": "483 - 383 BC",
                        "children": [
                            {"label": "1st Council (Rajgriha, Ajatashatru): Presided by Mahakassapa; compiled Sutta (Ananda) & Vinaya (Upali) Pitakas", "type": "leaf"},
                            {"label": "2nd Council (Vaishali, Kalasoka): Presided by Sabakami; split into Sthaviravadins & Mahasanghikas", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Councils 3 & 4", "type": "sub", "date": "250 BC - 72 AD",
                        "children": [
                            {"label": "3rd Council (Pataliputra, Ashoka): Presided by Moggaliputta Tissa; compiled Abhidhamma Pitaka", "type": "leaf"},
                            {"label": "4th Council (Kashmir, Kanishka): Presided by Vasumitra (deputy Ashvaghosa); compiled Vibhashashastras; split Hinayana/Mahayana", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Canon & Royal Patrons", "type": "branch", "date": "Patronage",
                "children": [
                    {
                        "label": "Tripitaka Literature", "type": "sub", "date": "Pali",
                        "children": [
                            {"label": "Sutta Pitaka (discourses), Vinaya Pitaka (monastic discipline), Abhidhamma Pitaka (philosophical analysis)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Royal Patrons", "type": "sub", "date": "Kings",
                        "children": [
                            {"label": "Bimbisara, Ajatashatru, Ashoka, Kanishka, Harshavardhana, and Pala rulers (Dharmapala)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. JAINISM (General)
    elif fl == 'jainism':
        return [
            {
                "label": "Mahavira & Tirthankaras", "type": "branch", "date": "Historical",
                "children": [
                    {
                        "label": "Tirthankaras", "type": "sub", "date": "Founders",
                        "children": [
                            {"label": "Jainism has 24 Tirthankaras; 1st Rishabhadev (symbol Bull); 23rd Parshvanath (symbol Snake)", "type": "leaf"},
                            {"label": "24th Vardhamana Mahavira (symbol Lion): Added Brahmacharya vow to Parshvanath's four vows", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Jain Philosophies", "type": "branch", "date": "Doctrines",
                "children": [
                    {
                        "label": "Core Doctrines", "type": "sub", "date": "Tenets",
                        "children": [
                            {"label": "Anekantavada: Theory of multi-sidedness of reality (non-absolutism)", "type": "leaf"},
                            {"label": "Syadvada: Theory of relativity of judgments (conditional statements beginning with 'Maybe')", "type": "leaf"},
                            {"label": "Triratnas: Samyak Darshana (Faith), Samyak Jnana (Knowledge), Samyak Charitra (Conduct)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Jain Concepts", "type": "sub", "date": "Terms",
                        "children": [
                            {"label": "Asrava: Inflow of karma into soul; Bandha: Bondage of soul; Samvara: Stopping inflow", "type": "leaf"},
                            {"label": "Nirjara: Wearing out/shedding of karma; Moksha: Liberation; Santhara/Sallekhana: Fasting to death", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. JAINISM (Mahavira, Philosophy, Sects)
    elif fl == 'jainism-mahavira-philosophy-sects':
        return [
            {
                "label": "Mahavira's Biography", "type": "branch", "date": "540 - 468 BC",
                "children": [
                    {
                        "label": "Key Milestones", "type": "sub", "date": "Vardhamana",
                        "children": [
                            {"label": "Born at Kundagrama (Vaishali) to Siddhartha (Jnatrika head) and Trishala (Lichchhavi princess)", "type": "leaf"},
                            {"label": "Attained Kaivalya at age 42 under Sal tree on Rijupalika river near Jrimbhikagrama", "type": "leaf"},
                            {"label": "Died at Pavapuri (Patna) at age 72; patronized by Magadha rulers like Bimbisara", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Sects & Divisions", "type": "branch", "date": "Jain Sects",
                "children": [
                    {
                        "label": "Shvetambaras & Digambaras", "type": "sub", "date": "Schism",
                        "children": [
                            {"label": "Shvetambaras: Led by Sthulabhadra, white clad, progressive, believed women can attain liberation", "type": "leaf"},
                            {"label": "Digambaras: Led by Bhadrabahu, sky clad (naked), orthodox, believed women must be reborn as men", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Jain Councils & Literature", "type": "branch", "date": "Canon",
                "children": [
                    {
                        "label": "Two Councils", "type": "sub", "date": "Councils",
                        "children": [
                            {"label": "1st Council (Pataliputra, 3rd Century BC): Sthulabhadra presided; compiled the 12 Angas", "type": "leaf"},
                            {"label": "2nd Council (Vallabhi, 5th Century AD): Devardhi Kshamashramana presided; final codification of 12 Upangas", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Jain Literature", "type": "sub", "date": "Texts",
                        "children": [
                            {"label": "Written in Prakrit (Ardhamagadhi) language; canonical books include Angas, Upangas, Prakirnas, Sutras", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. DELHI SULTANATE
    elif fl == 'delhi-sultanate':
        return [
            {
                "label": "Slave & Khilji Dynasties", "type": "branch", "date": "1206 - 1320 AD",
                "children": [
                    {
                        "label": "Slave Dynasty (1206-90)", "type": "sub", "date": "Mamluk",
                        "children": [
                            {"label": "Qutubuddin Aibak: Founded; built Quwwat-ul-Islam, Adhai Din Ka Jhopra, started Qutub Minar", "type": "leaf"},
                            {"label": "Iltutmish: Real consolidator; introduced Turkan-i-Chahalgani, silver Tanka, copper Jital, Iqta system", "type": "leaf"},
                            {"label": "Razia Sultana: First and only female Muslim ruler of Delhi; Balban: Policy of Blood & Iron, Sijda/Paibos", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Khilji Dynasty (1290-1320)", "type": "sub", "date": "Khiljis",
                        "children": [
                            {"label": "Jalaluddin: Founded; Alauddin Khilji: Market reforms, price control, Alai Darwaza, Siri Fort, Dag & Chehra", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Tughlaq, Sayyid, & Lodi", "type": "branch", "date": "1320 - 1526 AD",
                "children": [
                    {
                        "label": "Tughlaq Dynasty (1320-1414)", "type": "sub", "date": "Tughlaqs",
                        "children": [
                            {"label": "Muhammad bin Tughlaq: Token copper currency, Delhi-Daulatabad capital shift, Diwan-i-Amir Kohi (agri)", "type": "leaf"},
                            {"label": "Firoz Shah Tughlaq: Canals (Sutlej/Yamuna), Jizya on Brahmins, founded Jaunpur, Hisar, Firozabad", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Sayyid & Lodi Dynasties", "type": "sub", "date": "Sayyid & Lodi",
                        "children": [
                            {"label": "Sayyid (1414-51): Founded by Khizr Khan; Lodi (1451-1526): First Afghan dynasty, founded by Bahlul Lodi", "type": "leaf"},
                            {"label": "Sikandar Lodi: Founded Agra in 1504, wrote poems under 'Gulrukhi', introduced Gaz-i-Sikandari yard", "type": "leaf"},
                            {"label": "Ibrahim Lodi: Defeated by Babur in the First Battle of Panipat (1526), ending Delhi Sultanate", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Administration & Offices", "type": "branch", "date": "Offices",
                "children": [
                    {
                        "label": "Diwans", "type": "sub", "date": "Departments",
                        "children": [
                            {"label": "Diwan-i-Wizarat (Finance), Diwan-i-Arz (Military), Diwan-i-Insha (Chancery), Diwan-i-Rasalat (Foreign)", "type": "leaf"},
                            {"label": "Diwan-i-Kohi (Agri under MbT), Diwan-i-Mustakhraj (Alauddin's tax arrears department)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. MAURYAN EMPIRE
    elif fl == 'mauryan-empire':
        return [
            {
                "label": "Mauryan Dynasty", "type": "branch", "date": "322 - 185 BC",
                "children": [
                    {
                        "label": "The Kings", "type": "sub", "date": "Mauryans",
                        "children": [
                            {"label": "Chandragupta: Defeated Seleucus Nicator (305 BC); adopted Jainism under Bhadrabahu; starved to death at Shravanabelagola", "type": "leaf"},
                            {"label": "Bindusara: Known to Greeks as Amitraghata (slayer of foes); received Greek ambassador Deimachus", "type": "leaf"},
                            {"label": "Brihadratha: Last Mauryan king; assassinated by commander-in-chief Pushyamitra Shunga in 185 BC", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Ashoka the Great (273-232 BC)", "type": "sub", "date": "Ashoka",
                        "children": [
                            {"label": "Kalinga War (261 BC, 9th regnal year): Mentioned in Major Rock Edict XIII; switched from Bherighosha to Dhammaghosha", "type": "leaf"},
                            {"label": "Dhamma policy: Non-sectarian ethical code; appointed Dhamma Mahamattas to spread social harmony", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Administration & Sources", "type": "branch", "date": "Mauryan State",
                "children": [
                    {
                        "label": "Kautilya & Megasthenes", "type": "sub", "date": "Sources",
                        "children": [
                            {"label": "Arthashastra: 15 books on statecraft; details Saptanga theory (Swami, Amatya, Janapada, Durga, Kosha, Danda, Mitra)", "type": "leaf"},
                            {"label": "Indica (Megasthenes): Details municipal administration of Pataliputra (6 committees of 5 members) and 7-caste system", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Edicts & Inscriptions", "type": "sub", "date": "Epigraphy",
                        "children": [
                            {"label": "Languages: Mostly Prakrit (Brahmi script); North-west edicts in Greek/Aramaic and Kharosthi script", "type": "leaf"},
                            {"label": "Decipherment: James Prinsep in 1837 deciphered Brahmi script; identified Ashoka by title 'Devanampiya Piyadassi'", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. GUPTA EMPIRE
    elif fl == 'gupta-empire':
        return [
            {
                "label": "Sovereigns & Conquests", "type": "branch", "date": "319 - 540 AD",
                "children": [
                    {
                        "label": "Chandragupta I & Samudragupta", "type": "sub", "date": "Early Kings",
                        "children": [
                            {"label": "Chandragupta I: Started Gupta Era (319-320 AD), married Lichchhavi princess Kumaradevi, Maharajadhiraja", "type": "leaf"},
                            {"label": "Samudragupta: Court poet Harishena wrote Prayag Prashasti (Allahabad pillar); called Napoleon of India", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Vikramaditya & Successors", "type": "sub", "date": "Later Kings",
                        "children": [
                            {"label": "Chandragupta II (Vikramaditya): Defeated Shakas; court had Navaratnas; visited by Fa-Hien", "type": "leaf"},
                            {"label": "Kumaragupta I: Founded Nalanda University; Skandagupta: Repelled the Hunas, repaired Sudarshana lake", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Golden Age Culture", "type": "branch", "date": "Contributions",
                "children": [
                    {
                        "label": "Navaratnas & Literature", "type": "sub", "date": "Authors",
                        "children": [
                            {"label": "Kalidasa: Abhijanasakuntalam, Meghaduta, Raghuvamsa; Vishnusharma: Panchatantra", "type": "leaf"},
                            {"label": "Shudraka: Mricchakatika; Vishakhadatta: Mudrarakshasa and Devichandraguptam", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Science & Mathematics", "type": "sub", "date": "Scientists",
                        "children": [
                            {"label": "Aryabhata: Wrote Aryabhatiyam; calculated Pi, explained solar/lunar eclipses, discovered Zero", "type": "leaf"},
                            {"label": "Varahamihira: Brihat Samhita and Panchasiddhantika; Brahmagupta: Brahmasphutasiddhanta (gravity)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Architecture & Art", "type": "sub", "date": "Structures",
                        "children": [
                            {"label": "Dashavatara Temple (Deogarh, UP): Earliest stone temple in Panchayatana style; Bhitargaon brick temple", "type": "leaf"},
                            {"label": "Metallurgy: Mehrauli Iron Pillar (Delhi) has remained rust-free for 1600+ years", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. MUGHAL EMPIRE
    elif fl == 'mughal-empire':
        return [
            {
                "label": "The Great Emperors", "type": "branch", "date": "1526 - 1707 AD",
                "children": [
                    {
                        "label": "Babur to Akbar", "type": "sub", "date": "1526 - 1605 AD",
                        "children": [
                            {"label": "Babur: Won Panipat (1526), Khanwa (1527), Chanderi (1528), Ghaghra (1529); wrote Baburnama", "type": "leaf"},
                            {"label": "Humayun: Defeated by Sher Shah Suri (Battle of Chausa 1539, Bilgram 1540); Humayunnama by Gulbadan Begum", "type": "leaf"},
                            {"label": "Akbar: Won 2nd Panipat (1556), Haldighati (1576 against Maharana Pratap); Din-i-Ilahi (1582), Ibadat Khana", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Jahangir to Aurangzeb", "type": "sub", "date": "1605 - 1707 AD",
                        "children": [
                            {"label": "Jahangir: Adorned with paintings (Mansur, Bishandas); executed Guru Arjan Dev; hosted Captain Hawkins", "type": "leaf"},
                            {"label": "Shah Jahan: Architecture golden age; Taj Mahal, Red Fort, Jama Masjid, Peacock Throne, Moti Masjid", "type": "leaf"},
                            {"label": "Aurangzeb (Alamgir): Reimposed Jizya, banned music, executed Guru Tegh Bahadur; peak territorial size", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Administration & Literature", "type": "branch", "date": "Systems",
                "children": [
                    {
                        "label": "Administrative Core", "type": "sub", "date": "Mansab & Dahsala",
                        "children": [
                            {"label": "Mansabdari: Zat (rank & salary) and Sawar (number of cavalrymen); non-hereditary nobility", "type": "leaf"},
                            {"label": "Dahsala Land Revenue (Todar Mal): 10-year average yield and prices calculated for land tax", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Mughal Works & Translations", "type": "sub", "date": "Literature",
                        "children": [
                            {"label": "Ain-i-Akbari & Akbarnama: Written by Abul Fazl; Tuzuk-i-Jahangiri written by Jahangir", "type": "leaf"},
                            {"label": "Razmnama: Persian translation of Mahabharata; Ramayana translated under Akbar's patronage", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 12. POST-GUPTA PERIOD
    elif fl == 'post-gupta-period':
        return [
            {
                "label": "Kannauj & Harsha", "type": "branch", "date": "606 - 647 AD",
                "children": [
                    {
                        "label": "Harshavardhana", "type": "sub", "date": "Kannauj Ruler",
                        "children": [
                            {"label": "Sovereignty: Shifted capital from Thanesar to Kannauj; defeated by Pulakeshin II on Narmada banks", "type": "leaf"},
                            {"label": "Literature: Banabhatta wrote Harshacharita & Kadambari; Harsha wrote Ratnavali, Priyadarshika, Nagananda", "type": "leaf"},
                            {"label": "Chinese pilgrims: Hiuen Tsang attended Kannauj assembly and Prayag Maha Moksha Parishad", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Tripartite Struggle", "type": "sub", "date": "Magadha Contest",
                        "children": [
                            {"label": "Fought between Gurjara-Pratiharas, Palas of Bengal, and Rashtrakutas for control of Kannauj", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Southern Kingdoms", "type": "branch", "date": "Deccan & South",
                "children": [
                    {
                        "label": "Chalukyas & Pallavas", "type": "sub", "date": "Dynasties",
                        "children": [
                            {"label": "Chalukyas of Badami: Pulakeshin II; built Aihole temples and Pattadakal rock-cut complexes", "type": "leaf"},
                            {"label": "Pallavas of Kanchi: Narasimhavarman I built the shore temple and rathas at Mahabalipuram", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 13. PRE-HISTORIC PERIOD
    elif fl == 'pre-historic-period-paleolithic-neolithic-ages':
        return [
            {
                "label": "Stone Age Cultures", "type": "branch", "date": "Evolution",
                "children": [
                    {
                        "label": "Paleolithic Age", "type": "sub", "date": "Old Stone Age",
                        "children": [
                            {"label": "Quartzite stone tools; hunter-gatherers; Bhimbetka cave rock shelters (MP) show prehistoric paintings", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Mesolithic Age", "type": "sub", "date": "Middle Stone Age",
                        "children": [
                            {"label": "Microlith (tiny stone) tools; domestication of animals starts; Adamgarh (MP) & Bagor (Rajasthan) sites", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Neolithic Age", "type": "sub", "date": "New Stone Age",
                        "children": [
                            {"label": "Settled agriculture, invention of wheel and pottery; Burzahom (J&K) pit dwellings & bone tools", "type": "leaf"},
                            {"label": "Mehrgarh (Baluchistan): Earliest Neolithic site showing wheat and barley cultivation (~7000 BC)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 14. ADVENT OF EUROPEAN POWERS & EXPANSION POLICIES
    elif fl == 'advent-of-european-powers-british-expansion-policies':
        return [
            {
                "label": "European Arrivals", "type": "branch", "date": "1498 - 1664 AD",
                "children": [
                    {
                        "label": "Arrival Chronology", "type": "sub", "date": "Factories",
                        "children": [
                            {"label": "Chronology: Portuguese (1498) -> Dutch (1602) -> English (1608) -> French (1664)", "type": "leaf"},
                            {"label": "Portuguese: Vasco da Gama; Governor Francisco de Almeida (Blue Water Policy); Albuquerque captured Goa (1510)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Carnatic Wars", "type": "sub", "date": "Anglo-French",
                        "children": [
                            {"label": "1st War (1746-48): Aix-la-Chapelle Treaty; 2nd War (1749-54): Pondicherry Treaty; 3rd War (1758-63): Paris Treaty", "type": "leaf"},
                            {"label": "Battle of Wandiwash (1760): Sir Eyre Coote defeated French General Lally, ending French power in India", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Expansion Devices", "type": "branch", "date": "Annexations",
                "children": [
                    {
                        "label": "Subsidiary & Lapse", "type": "sub", "date": "Policies",
                        "children": [
                            {"label": "Subsidiary Alliance (Wellesley): Nizam of Hyderabad (1798) first; Mysore, Tanjore, Awadh followed", "type": "leaf"},
                            {"label": "Doctrine of Lapse (Dalhousie): Annexed Satara (1848), Sambalpur, Jhansi, Nagpur; Awadh annexed in 1856 on charges of misgovernance", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 15. REVOLT OF 1857
    elif fl == 'revolt-of-1857':
        return [
            {
                "label": "Causes & Outbreak", "type": "branch", "date": "1857 Mutiny",
                "children": [
                    {
                        "label": "Causes & Triggers", "type": "sub", "date": "Background",
                        "children": [
                            {"label": "Causes: Doctrine of Lapse, high land tax, exclusion of Indians from high posts, religious conversion fears", "type": "leaf"},
                            {"label": "Spark: Mangal Pandey (34th NI) mutinied at Barrackpore (March 29, 1857) over greased Enfield cartridges", "type": "leaf"},
                            {"label": "Outbreak: Meerut sepoys mutinied on May 10, 1857; marched to Delhi, declared Bahadur Shah II emperor", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Rebellion & Suppressions", "type": "branch", "date": "Leaders",
                "children": [
                    {
                        "label": "Centers & Leaders", "type": "sub", "date": "Leaders",
                        "children": [
                            {"label": "Delhi: Bakht Khan; Kanpur: Nana Sahib & Tantia Tope; Lucknow: Begum Hazrat Mahal", "type": "leaf"},
                            {"label": "Jhansi: Rani Laxmibai; Bihar: Kunwar Singh (Jagdishpur); Bareilly: Khan Bahadur Khan", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Suppression & Outcomes", "type": "sub", "date": "Suppression",
                        "children": [
                            {"label": "Suppression: Delhi retaken by John Nicholson; Kanpur & Lucknow retaken by Colin Campbell", "type": "leaf"},
                            {"label": "Government of India Act 1858: Dissolved East India Company; Secretary of State & Viceroy posts created", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 16. SOCIAL-RELIGIOUS REFORMS & LAND REVENUE SYSTEMS
    elif fl == 'social-religious-reforms-land-revenue-systems':
        return [
            {
                "label": "Social Reforms", "type": "branch", "date": "19th Century",
                "children": [
                    {
                        "label": "Reformers & Associations", "type": "sub", "date": "Organizations",
                        "children": [
                            {"label": "Raja Ram Mohan Roy: Brahmo Samaj (1828); Sati Abolition Act (1829, Bentinck); father of Indian Renaissance", "type": "leaf"},
                            {"label": "Ishwar Chandra Vidyasagar: Efforts led to Hindu Widow Remarriage Act 1856 (passed by Canning)", "type": "leaf"},
                            {"label": "Swami Dayanand: Arya Samaj (1875); 'Go Back to Vedas'; Shuddhi movement; Satyarth Prakash book", "type": "leaf"},
                            {"label": "Jyotiba Phule: Satyashodhak Samaj (1873) in Pune; wrote Gulamgiri; opened schools for lower castes & girls", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Land Revenue Systems", "type": "branch", "date": "Tax Systems",
                "children": [
                    {
                        "label": "Colonial Tax Models", "type": "sub", "date": "Land Tax",
                        "children": [
                            {"label": "Permanent Settlement (Cornwallis, 1793): Bengal, Bihar, Odisha; Zamindars made owners; Sunset Law applied", "type": "leaf"},
                            {"label": "Ryotwari (Munro & Reed, 1820): Madras, Bombay; direct settlement with peasants; high rates (50-60%)", "type": "leaf"},
                            {"label": "Mahalwari (Holt Mackenzie, 1822): Punjab, UP, Central India; revenue collected from village (Mahal) unit", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 17. MODERATE & EXTREMIST PHASES (INC)
    elif fl == 'national-movement-moderate-extremist-phases':
        return [
            {
                "label": "Moderate Phase", "type": "branch", "date": "1885 - 1905",
                "children": [
                    {
                        "label": "INC Foundation & Methods", "type": "sub", "date": "1885 INC",
                        "children": [
                            {"label": "Foundation: Dec 1885 by A.O. Hume; 1st session at Bombay (W.C. Bonnerjee, 72 delegates, Lord Dufferin Viceroy)", "type": "leaf"},
                            {"label": "Moderate Leaders: Dadabhai Naoroji (Drain of Wealth theory), W.C. Bonnerjee, Pherozeshah Mehta, Gokhale", "type": "leaf"},
                            {"label": "Methodology: 3Ps (Petition, Prayer, Protest) within British constitutional frameworks", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Extremist Phase", "type": "branch", "date": "1905 - 1919",
                "children": [
                    {
                        "label": "Bengal Partition & Split", "type": "sub", "date": "Extremists",
                        "children": [
                            {"label": "Partition of Bengal (Curzon, 1905): Led to Swadeshi and Boycott Movement; Vande Mataram became theme song", "type": "leaf"},
                            {"label": "Extremist Leaders: Lal-Bal-Pal (Lala Lajpat Rai, Tilak, Bipin Chandra Pal) & Aurobindo Ghosh", "type": "leaf"},
                            {"label": "Surat Split (1907): Split in INC over presidency; Lucknow Pact (1916): Extremists reunited; INC-League pact", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 18. GANDHIAN ERA & REVOLUTIONARY ACTS
    elif fl == 'national-movement-gandhian-era-revolutionary-acts':
        return [
            {
                "label": "Gandhian Leadership", "type": "branch", "date": "1915 - 1947",
                "children": [
                    {
                        "label": "Early Satyagrahas", "type": "sub", "date": "1917 - 1918",
                        "children": [
                            {"label": "Champaran (1917): 1st Satyagraha, indigo Tinkathia system; Raj Kumar Shukla invited Gandhi", "type": "leaf"},
                            {"label": "Ahmedabad (1918): 1st hunger strike over plague bonus; Kheda (1918): 1st Non-Cooperation over tax relief", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Mass Movements", "type": "sub", "date": "Non-Cooperation to Quit India",
                        "children": [
                            {"label": "Non-Cooperation (1920-22): Launched after Jallianwala Bagh (1919); called off after Chauri Chaura incident (Feb 1922)", "type": "leaf"},
                            {"label": "Civil Disobedience (1930): Dandi Salt March (Sabarmati to Dandi, March 12-April 6); Gandhi-Irwin Pact (1931)", "type": "leaf"},
                            {"label": "Quit India (Aug 1942): 'Do or Die' slogan; arrest of all top leaders (Operation Hourglass/Thunderbolt)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Revolutionary Phase", "type": "branch", "date": "Armed Rebellion",
                "children": [
                    {
                        "label": "HRA & HSRA", "type": "sub", "date": "Actions",
                        "children": [
                            {"label": "HRA (1924, Bismil, Chatterjee): Kakori Train Action (1925); HSRA (1928, Azad, Bhagat Singh) in Feroz Shah Kotla", "type": "leaf"},
                            {"label": "Actions: Saunders Murder (1928), Central Assembly Bombing (1929 by Bhagat Singh & Batukeshwar Dutt)", "type": "leaf"},
                            {"label": "Chittagong Armoury Raid (1930): Led by Surya Sen (Masterda) in Bengal", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 19. ART & CULTURE (Dance, Music, Temple Architecture, Festivals)
    elif fl == 'art-culture-dance-music-temple-architecture-festivals':
        return [
            {
                "label": "Performing Arts", "type": "branch", "date": "Dances & Music",
                "children": [
                    {
                        "label": "Classical Dances", "type": "sub", "date": "Sangeet Natak Akademi",
                        "children": [
                            {"label": "Eight Dances: Bharatnatyam (TN), Kathak (North India), Kathakali & Mohiniyattam (Kerala), Kuchipudi (AP), Odissi, Manipuri, Sattriya (Assam)", "type": "leaf"},
                            {"label": "Natyashastra (Bharata Muni) and Abhinaya Darpana (Nandikesvara) are the primary sources", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Indian Classical Music", "type": "sub", "date": "Hindustani & Carnatic",
                        "children": [
                            {"label": "Hindustani (North): Gharana system (Gwalior, Kirana, etc.); Dhrupad, Khayal, Thumri styles; Persian influence", "type": "leaf"},
                            {"label": "Carnatic (South): Structured, kirtan style, Purandara Dasa (father); Trinity (Tyagaraja, Muthuswami, Syama Sastri)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Architecture & Heritage", "type": "branch", "date": "Monuments",
                "children": [
                    {
                        "label": "Temple Styles", "type": "sub", "date": "Nagara & Dravida",
                        "children": [
                            {"label": "Nagara (North): Shikhara, Garbhagriha, Amalaka, Kalasha, Panchayatana style; e.g., Sun Temple (Konark), Kandariya Mahadeva", "type": "leaf"},
                            {"label": "Dravida (South): Gopuram (gateways), Vimana (tower), Assembly Hall (Mandapa), Temple tank; e.g., Brihadisvara", "type": "leaf"},
                            {"label": "Vesara (Deccan hybrid): Combined Nagara and Dravida styles; e.g., temples built by Chalukyas & Hoysalas", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 20. VIJAYANAGARA, BAHMANI, & BHAKTI-SUFI
    elif fl == 'vijayanagara-bahmani-kingdoms-bhakti-sufi-movements':
        return [
            {
                "label": "Deccan & Southern Kingdoms", "type": "branch", "date": "1336 - 1565 AD",
                "children": [
                    {
                        "label": "Vijayanagara Empire", "type": "sub", "date": "Hampi",
                        "children": [
                            {"label": "Founders: Harihara and Bukka in 1336; Sangama, Saluva, Tuluva, and Aravidu dynasties", "type": "leaf"},
                            {"label": "Krishna Deva Raya (Tuluva): Wrote Amuktamalyada (Telugu); court had Ashtadiggajas (Allasani Peddana)", "type": "leaf"},
                            {"label": "Battle of Talikota (1565): Vijayanagara defeated by joint coalition of Deccan Sultanates", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Bahmani Kingdom", "type": "sub", "date": "Deccan",
                        "children": [
                            {"label": "Founded in 1347 by Alauddin Hasan Bahman Shah; broke up into Bijapur, Golconda, Ahmednagar, Bidar, Berar", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Foreign Travelers", "type": "sub", "date": "Accounts",
                        "children": [
                            {"label": "Nicolo Conti (Italian, Deva Raya I); Abdur Razzaq (Persian, Deva Raya II); Domingo Paes (Portuguese, KDR)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Bhakti & Sufi Movements", "type": "branch", "date": "Religious Renaissance",
                "children": [
                    {
                        "label": "Bhakti Saints", "type": "sub", "date": "Saints",
                        "children": [
                            {"label": "Origins: Tamil Nadu (Alvars - Vishnu, Nayanars - Shiva); Adi Shankara (Advaita philosophy)", "type": "leaf"},
                            {"label": "Sadhus: Kabir (Bijak), Guru Nanak (Adi Granth), Mirabai, Tulsidas (Ramcharitmanas), Chaitanya (Kirtan)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Sufism In India", "type": "sub", "date": "Silsilas",
                        "children": [
                            {"label": "Chishti: Moinuddin Chishti (Ajmer Dargah); Nizamuddin Auliya (Delhi); Salim Chishti (Fatehpur Sikri)", "type": "leaf"},
                            {"label": "Suhrawardi (orthodox, rich); Naqshbandi (very orthodox, Aurangzeb followed, banned music)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 21. RISE OF MAHAJANAPADAS & MAGADHA EMPIRE (Duplicate/Variant name)
    elif fl == 'rise-of-mahajanapadas-magadha-empire':
        return [
            {
                "label": "Sixteen States", "type": "branch", "date": "6th Century BC",
                "children": [
                    {
                        "label": "Geography & Texts", "type": "sub", "date": "Syllabus Core",
                        "children": [
                            {"label": "Sources: Anguttara Nikaya (Buddhist) and Bhagavati Sutra (Jain) list the 16 Mahajanapadas", "type": "leaf"},
                            {"label": "Capitals: Magadha (Rajgriha/Pataliputra), Kosala (Shravasti), Vatsa (Kausambi), Avanti (Ujjain)", "type": "leaf"},
                            {"label": "Ganasanghas (Republics): Vajji (Vaishali, world's first republic), Malla (Kushinagar)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Magadhan Dynasties", "type": "branch", "date": "Magadha Rise",
                "children": [
                    {
                        "label": "Haryanka Dynasty (544-412 BC)", "type": "sub", "date": "Founders",
                        "children": [
                            {"label": "Bimbisara: Matrimonial alliances (Kosala, Madra, Lichchhavi); sent physician Jivaka to Avanti", "type": "leaf"},
                            {"label": "Ajatashatru: Patronized 1st Buddhist council; used war weapons Mahashilakantaka & Rathamusala", "type": "leaf"},
                            {"label": "Udayin: Founded new capital Pataliputra at the confluence of Ganga and Son rivers", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Shishunaga & Nanda Dynasties", "type": "sub", "date": "412-322 BC",
                        "children": [
                            {"label": "Kalasoka (Shishunaga): Shifted capital permanently to Pataliputra; convened 2nd Buddhist council", "type": "leaf"},
                            {"label": "Mahapadma Nanda: First empire builder of India; assumed titles 'Ekarat' and 'Sarvakshatrantaka'", "type": "leaf"},
                            {"label": "Dhana Nanda: Contemporary of Alexander; Alexander's army refused to cross Beas (Vipasa) in 326 BC due to Nanda force", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 22. DIASPORA / EXTRA FALLBACK FOLDER MATCH
    raise Exception(f"Folder '{folder_name}' has no custom mindmap branch mapped!")

# Patching Logic
def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Clean previous mindmap tags to prevent duplicates (using ?v=3 to force cache bypass)
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->
'''
    # We find "<!-- Prep Tracker -->" or fallback
    prep_tracker = "        <!-- Prep Tracker -->"
    if prep_tracker in html:
        html = html.replace(prep_tracker, mindmap_card + "\n" + prep_tracker, 1)
    else:
        # Fallback to checklist
        checklist_marker = '<div class="card-premium">'
        # Let's replace the first one that comes after Key Concepts
        pos = html.find('Self-Evaluation Checklist')
        if pos != -1:
            # find the card-premium preceding it
            card_pos = html.rfind('<div class="card-premium">', 0, pos)
            if card_pos != -1:
                html = html[:card_pos] + mindmap_card + "\n" + html[card_pos:]

    # Re-inject script with ?v=3 to force reload of wrapping logic
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=3"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Successfully patched: {filepath}")
    return True

# Main execution
def main():
    folders = sorted([f for f in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, f))])
    print(f"Found {len(folders)} topics to process.")
    
    for idx, folder in enumerate(folders):
        folder_path = os.path.join(BASE_DIR, folder)
        html_path = os.path.join(folder_path, 'index.html')
        content_path = os.path.join(folder_path, 'content.json')
        
        if not os.path.exists(html_path):
            print(f"[{idx+1}/{len(folders)}] Skipping {folder} (index.html not found)")
            continue
            
        topic_name = get_clean_title(folder)
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        # Build custom, 3-tier deep-dive topic-specific mindmap data
        branches = get_custom_branches(folder)
        mindmap_data = {
            "label": get_clean_title(folder),
            "type": "root",
            "children": branches
        }
        
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()