import os
import re
import json

BASE_DIR = r"upsc/polity/Historical-Background-Making-of-Constitution"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'pri', 'pesa', 'ncrwc', 'gst', 'adcs', 'amtm', 'cji', 'njac', 'aijs', 'adr', 'nalsa', 'pil', 'njdg', 'lsa', 'cec', 'ecs', 'spr', 'apmc', 'zbnf', 'pkvy', 'pmksy', 'fbr', 'phwr', 'ahwr', 'isa', 'ppp', 'pmgsy', 'ls', 'rs', 'vp', 'coom', 'com', 'eic', 'ca', 'goi'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'over', 'between', 'respect', 'under', 'about', 'as', 'per']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# 3-Tier Deep-Dive Mappings for Historical Background & Making of Constitution
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. Regulating Act 1773
    if 'regulating-act-1773' in fl or 'company-rule' in fl:
        return [
            {
                "label": "Governor-General Setup",
                "type": "branch",
                "date": "1773 Reforms",
                "children": [
                    {
                        "label": "Administration", "type": "sub", "date": "Bengal", "children": [
                            {"label": "Designated Governor of Bengal as Governor-General of Bengal (Warren Hastings); created 4-member Executive Council", "type": "leaf"},
                            {"label": "Subordinated Governors of Bombay and Madras presidencies under Governor-General of Bengal", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Judiciary & Control", "type": "sub", "date": "Calcutta Court", "children": [
                            {"label": "Provided for establishment of Supreme Court at Calcutta (1774) with 1 Chief Justice & 3 other judges", "type": "leaf"},
                            {"label": "Prohibited servants of East India Company (EIC) from private trade or accepting bribes/presents from natives", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. Pitts India Act 1784 & Amending Acts
    elif 'pitts' in fl or '1781' in fl or '1786' in fl:
        return [
            {
                "label": "Dual System of Control",
                "type": "branch",
                "date": "1784 Reforms",
                "children": [
                    {
                        "label": "Administrative Split", "type": "sub", "date": "Control System", "children": [
                            {"label": "Pitts India Act (1784): Distinguished between commercial (managed by Court of Directors) & political affairs of EIC", "type": "leaf"},
                            {"label": "Established 6-member Board of Control representing British Crown to supervise civil, military, and revenue affairs", "type": "leaf"},
                            {"label": "Act of 1781 (Act of Settlement): Exempted Governor-General and Council from jurisdiction of Supreme Court for official acts", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. Charter Acts 1793 & 1813
    elif '1793' in fl or '1813' in fl:
        return [
            {
                "label": "Trade Monopolies",
                "type": "branch",
                "date": "Monopolies",
                "children": [
                    {
                        "label": "1813 Trade Reforms", "type": "sub", "date": "1813 Charter", "children": [
                            {"label": "Charter Act 1813: Abolished commercial trade monopoly of EIC in India, opening trade to all British merchants", "type": "leaf"},
                            {"label": "Exception: EIC retained trade monopoly in Tea and trade with China for another 20 years", "type": "leaf"},
                            {"label": "Allotted Rs 1 lakh annually for promotion of education; allowed Christian missionaries to enter India", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Charter Act 1833
    elif '1833' in fl:
        return [
            {
                "label": "Centralization",
                "type": "branch",
                "date": "1833 Reforms",
                "children": [
                    {
                        "label": "Governor-General of India", "type": "sub", "date": "Bentinck Era", "children": [
                            {"label": "Designated Governor-General of Bengal as Governor-General of India (Lord William Bentinck); vested all civil/military powers", "type": "leaf"},
                            {"label": "Deprived Governors of Bombay and Madras of their legislative powers; laws made under this act called Acts", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Commercial & Civil Service", "type": "sub", "date": "Trade End", "children": [
                            {"label": "Ended commercial activities of EIC; made it a purely administrative body acting in trust for British Crown", "type": "leaf"},
                            {"label": "Attempted to introduce open competition for Civil Services (opposed by Court of Directors; implemented later)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. Charter Act 1853
    elif '1853' in fl:
        return [
            {
                "label": "Legislative Separation",
                "type": "branch",
                "date": "1853 Reforms",
                "children": [
                    {
                        "label": "Executive vs Legislative", "type": "sub", "date": "Mini-Parliament", "children": [
                            {"label": "Separated legislative and executive functions of Governor-General's Council for the first time", "type": "leaf"},
                            {"label": "Created 6-member Indian Legislative Council; introduced local representation (4 from Madras/Bombay/Bengal/Agra)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Covenanted Civil Service", "type": "sub", "date": "Macaulay Committee", "children": [
                            {"label": "Introduced open competition system for civil service recruitment (Macaulay Committee on Indian Civil Service appointed in 1854)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. Government of India Act 1858
    elif '1858' in fl or 'crown-rule' in fl:
        return [
            {
                "label": "Direct Crown Rule",
                "type": "branch",
                "date": "1858 Reforms",
                "children": [
                    {
                        "label": "Abolition of EIC", "type": "sub", "date": "Royal Takeover", "children": [
                            {"label": "Ended EIC rule; transferred governance powers, territories, and revenues directly to British Crown (Act for Good Govt of India)", "type": "leaf"},
                            {"label": "Abolished Board of Control and Court of Directors, ending the system of dual government in India", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Secretary of State", "type": "sub", "date": "Viceroy Setup", "children": [
                            {"label": "Created office of Secretary of State for India (member of British Cabinet) assisted by 15-member advisory Council of India", "type": "leaf"},
                            {"label": "Designated Governor-General of India as Viceroy of India (Lord Canning), the direct representative of the Crown", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. Indian Councils Acts (1861, 1892, 1909)
    elif '1861' in fl or '1892' in fl or '1909' in fl:
        return [
            {
                "label": "Legislative Expansion",
                "type": "branch",
                "date": "Communal Electorate",
                "children": [
                    {
                        "label": "1861 Portfolio & Decentralization", "type": "sub", "date": "1861 & 1892", "children": [
                            {"label": "Act of 1861: Restored legislative powers of Bombay/Madras (decentralization); recognized Portfolio System (Canning)", "type": "leaf"},
                            {"label": "Act of 1892: Expanded legislative councils; allowed discussion on budget and addressing questions to executive", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "1909 Morley-Minto Reforms", "type": "sub", "date": "Morley-Minto", "children": [
                            {"label": "Morley-Minto (1909): Introduced communal representation (separate electorates for Muslims; Minto as Father of Communal Electorate)", "type": "leaf"},
                            {"label": "Allowed association of Indians in executive councils (Satyendra Prasad Sinha joined Viceroy's Executive Council)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. Government of India Act 1919 / Simon Commission
    elif '1919' in fl or 'simon' in fl:
        return [
            {
                "label": "Montagu-Chelmsford Reforms",
                "type": "branch",
                "date": "Dyarchy",
                "children": [
                    {
                        "label": "Dyarchy & Bicameralism", "type": "sub", "date": "1919 Act", "children": [
                            {"label": "Introduced Dyarchy (rule of two) in provinces; divided provincial subjects into Transferred (ministers) & Reserved (governor)", "type": "leaf"},
                            {"label": "Introduced bicameralism at center (Legislative Assembly & Council of State) and direct elections for the first time", "type": "leaf"},
                            {"label": "Communal electorate extended to Sikhs, Indian Christians, Anglo-Indians, and Europeans; created High Commissioner for India", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Simon Commission (1927)", "type": "sub", "date": "Panel Status", "children": [
                            {"label": "Statutory panel to report on working of 1919 Act; boycotted by all Indian parties (all-white 7-member commission)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. Government of India Act 1935
    elif '1935' in fl:
        return [
            {
                "label": "Federal Structure",
                "type": "branch",
                "date": "1935 Reforms",
                "children": [
                    {
                        "label": "Federation & Dyarchy", "type": "sub", "date": "Autonomy", "children": [
                            {"label": "Proposed All-India Federation of British provinces & princely states (never joined); abolished dyarchy in provinces", "type": "leaf"},
                            {"label": "Introduced Provincial Autonomy; introduced dyarchy at the center (Federal subjects: Transferred vs Reserved)", "type": "leaf"},
                            {"label": "Divided legislative powers: Federal List (59), Provincial List (54), Concurrent List (36); residuary with Viceroy", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Federal Institutions", "type": "sub", "date": "Agencies", "children": [
                            {"label": "Provided for establishment of Federal Court (1937), Reserve Bank of India (1935), and Federal/Provincial Public Service Commissions", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. Indian Independence Act 1947
    elif '1947' in fl:
        return [
            {
                "label": "End of British Rule",
                "type": "branch",
                "date": "Independence",
                "children": [
                    {
                        "label": "Two Dominions", "type": "sub", "date": "Partition", "children": [
                            {"label": "Ended British rule on August 15, 1947; declared India and Pakistan as independent sovereign dominions", "type": "leaf"},
                            {"label": "Abolished office of Viceroy (replaced by Governor-General for each dominion) and office of Secretary of State", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Sovereign Assemblies", "type": "sub", "date": "Assemblies", "children": [
                            {"label": "Empowered Constituent Assemblies of both dominions to frame any constitution and repeal any British acts", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. Making / Working of Constituent Assembly
    elif 'making-of' in fl or 'working-of' in fl or 'assembly' in fl or 'constituent' in fl or 'committee' in fl:
        return [
            {
                "label": "Making of the Constitution",
                "type": "branch",
                "date": "Cabinet Mission",
                "children": [
                    {
                        "label": "Assembly Formation", "type": "sub", "date": "Dr. Prasad", "children": [
                            {"label": "Constituent Assembly constituted in November 1946 under Cabinet Mission Plan of 1946; total 389 strength", "type": "leaf"},
                            {"label": "First meeting: Dec 9, 1946; Dr. Sachchidananda Sinha temporary President; Dr. Rajendra Prasad elected permanent President", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Extra Functions & Committees", "type": "sub", "date": "Adoption", "children": [
                            {"label": "Adopted National Flag (July 22, 1947), National Anthem & Song (Jan 24, 1950); ratified Commonwealth membership (May 1949)", "type": "leaf"},
                            {"label": "Drafting Committee set up on August 29, 1947; 7 members chaired by Dr. B.R. Ambedkar (Father of Constitution)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 12. Objective Resolution & Preamble
    elif 'preamble' in fl or 'objective-resolution' in fl or 'ideals' in fl or 'objectives' in fl:
        return [
            {
                "label": "Objective Resolution",
                "type": "branch",
                "date": "Nehru Draft",
                "children": [
                    {
                        "label": "Nehru Resolution", "type": "sub", "date": "Jan 22, 1947", "children": [
                            {"label": "Moved by Jawaharlal Nehru on Dec 13, 1946; unanimously adopted on Jan 22, 1947; forms basis of Preamble", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Preamble Ideals", "type": "sub", "date": "Sovereignty", "children": [
                            {"label": "Declare India Sovereign, Socialist, Secular, Democratic, Republic (Socialist, Secular, Integrity added by 42nd CA 1976)", "type": "leaf"},
                            {"label": "Secures Justice (social, economic, political), Liberty, Equality, and Fraternity; Preamble is non-justiciable", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 13. Basic Structure Doctrine
    elif 'basic-structure' in fl or 'doctrines' in fl or 'doctrinal' in fl:
        return [
            {
                "label": "Basic Structure Evolution",
                "type": "branch",
                "date": "Judicial Review",
                "children": [
                    {
                        "label": "Judicial Battle", "type": "sub", "date": "Cases", "children": [
                            {"label": "Shankari Prasad (1951) & Sajjan Singh (1965): Court held Parliament can amend any part including FRs under Art 368", "type": "leaf"},
                            {"label": "Golaknath Case (1967): SC reversed stand; held FRs are transcendental; Parliament cannot take away FRs", "type": "leaf"},
                            {"label": "Kesavananda Bharati (1973): 13-judge bench established 'Basic Structure'; Parliament cannot alter core features", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 14. Amendment of Constitution / Majorities
    elif 'amendment-of' in fl or 'majorities' in fl:
        return [
            {
                "label": "Amending Constitution",
                "type": "branch",
                "date": "Article 368",
                "children": [
                    {
                        "label": "Amendment Types", "type": "sub", "date": "Art 368 Mechanisms", "children": [
                            {"label": "Special Majority: 2/3rd members present & voting + absolute majority of total strength of the house", "type": "leaf"},
                            {"label": "Federal Amendment: Special Majority of Parliament + ratification by simple majority of half the state legislatures", "type": "leaf"},
                            {"label": "Simple Majority: Outside Art 368; e.g., creation of new states, official language, citizenship rules", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
    # 15. Types of Political System
    elif 'political-system' in fl:
        return [
            {
                "label": "Democratic Systems",
                "type": "branch",
                "date": "Democracy",
                "children": [
                    {
                        "label": "Direct Democracy Features", "type": "sub", "date": "Swiss Model", "children": [
                            {"label": "Referendum: Direct vote by the electorate on a single political question proposed to them", "type": "leaf"},
                            {"label": "Initiative: Citizens can propose a constitutional amendment or a law by obtaining a minimum number of signatures", "type": "leaf"},
                            {"label": "Recall: Empowering voters to remove an elected official from office before their term expires", "type": "leaf"},
                            {"label": "Plebiscite: Direct vote of all members of an electorate on an important public question (e.g., sovereignty change)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Indirect & Representative", "type": "sub", "date": "Representative", "children": [
                            {"label": "Parliamentary Democracy: Executive is drawn from and held accountable to the Legislature (e.g., India, UK)", "type": "leaf"},
                            {"label": "Presidential Democracy: Strict separation of powers; Executive is independent of the Legislature (e.g., USA)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Non-Democratic Regimes",
                "type": "branch",
                "date": "Authoritarianism",
                "children": [
                    {
                        "label": "Autocracy & Oligarchy", "type": "sub", "date": "Regime Types", "children": [
                            {"label": "Absolute Monarchy: Hereditary ruler holds supreme autocratic authority (not limited by laws or constitution)", "type": "leaf"},
                            {"label": "Constitutional Monarchy: Monarch acts as non-party head of state within limits of constitution (e.g., UK, Japan)", "type": "leaf"},
                            {"label": "Oligarchy & Totalitarianism: Rule by a small group of elites (oligarchy) or total state domination of public/private life", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 16. Constitutional Government & Constitutionalism
    elif 'constitutional-government' in fl or 'functions-of-the-constitution' in fl:
        return [
            {
                "label": "Constitutionalism Doctrines",
                "type": "branch",
                "date": "Limited Govt",
                "children": [
                    {
                        "label": "Core Constitutionalism", "type": "sub", "date": "Definition", "children": [
                            {"label": "Doctrine of Limited Government: Vests legal limits on government power to prevent arbitrary rule and protect rights", "type": "leaf"},
                            {"label": "Rule of Law (A.V. Dicey): Absence of arbitrary power, equality before law, and constitution as result of ordinary law", "type": "leaf"},
                            {"label": "Judicial Review: Supremacy of the Constitution enforced by an independent judiciary acting as its ultimate arbiter", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Institutional Mechanisms", "type": "sub", "date": "Checks & Balances", "children": [
                            {"label": "Separation of Powers: Montesquieu theory splitting state into Executive, Legislative, and Judicial branches", "type": "leaf"},
                            {"label": "Fundamental Rights: Constitutional limits on legislative and executive overreach against citizens", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 17. Presidential / Semi-Presidential / Parliamentary Form
    elif 'presidential-system' in fl or 'semi-presidential' in fl or 'parliamentary-form' in fl or 'indian-and-british' in fl:
        return [
            {
                "label": "Parliamentary vs Presidential",
                "type": "branch",
                "date": "Constitutional Systems",
                "children": [
                    {
                        "label": "Parliamentary System (Westminster)", "type": "sub", "date": "Westminster Model", "children": [
                            {"label": "Executive-Legislative Fusion: Cabinet is drawn from and directly responsible to Parliament; collective responsibility", "type": "leaf"},
                            {"label": "UK Sovereignty vs Indian Review: UK Parliament is legally supreme; Indian Parliament is limited by written constitution", "type": "leaf"},
                            {"label": "Shadow Cabinet (UK): Official opposition designates alternative ministers; no counterpart in India", "type": "leaf"},
                            {"label": "Ministerial Membership: Ministers must be MPs (India allows non-MPs for a maximum of 6 consecutive months)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Presidential & Semi-Presidential", "type": "sub", "date": "Non-Westminster", "children": [
                            {"label": "Presidential Model (US): Strict separation of powers; President is independent of Congress; cabinet are advisors", "type": "leaf"},
                            {"label": "Semi-Presidential (France): Dual executive where directly elected President shares domestic admin with PM", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 18. Types of Constitution
    elif 'types-of-constitution' in fl:
        return [
            {
                "label": "Constitutional Typologies",
                "type": "branch",
                "date": "Codification",
                "children": [
                    {
                        "label": "Written vs Unwritten", "type": "sub", "date": "Codification", "children": [
                            {"label": "Written Constitutions: Codified in a single document framed by a constituent assembly; supreme law (e.g., US, India)", "type": "leaf"},
                            {"label": "Unwritten Constitutions: Uncodified; based on constitutional conventions, statutes, and judicial judgments (e.g., UK)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Rigidity vs Flexibility", "type": "sub", "date": "Amendment Method", "children": [
                            {"label": "Rigid Constitutions: Require special amendment procedures distinct from ordinary legislation (e.g., USA)", "type": "leaf"},
                            {"label": "Flexible Constitutions: Can be altered or amended by ordinary legislative acts like regular laws (e.g., UK)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 19. Schedules and Subjects
    elif 'schedules' in fl:
        return [
            {
                "label": "Constitutional Schedules",
                "type": "branch",
                "date": "Schedules",
                "children": [
                    {
                        "label": "Schedules 1 to 6 (Admin)", "type": "sub", "date": "1st to 6th", "children": [
                            {"label": "1st Schedule: Names and territorial jurisdictions of States and Union Territories", "type": "leaf"},
                            {"label": "2nd & 3rd Schedules: Emoluments/salaries of high officials; forms of oaths and solemn affirmations", "type": "leaf"},
                            {"label": "4th Schedule: Allocation of seats in the Rajya Sabha (Council of States) to States and UTs", "type": "leaf"},
                            {"label": "5th & 6th Schedules: Administration of Scheduled Areas (5th) and tribal districts of Assam, Meghalaya, Tripura, Mizoram (6th)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Schedules 7 to 12 (Powers)", "type": "sub", "date": "7th to 12th", "children": [
                            {"label": "7th Schedule: Division of legislative lists (Union List 100 items, State List 61 items, Concurrent List 52 items)", "type": "leaf"},
                            {"label": "8th Schedule: List of 22 officially recognized regional languages in the Indian Republic", "type": "leaf"},
                            {"label": "9th Schedule: Validation of certain land reform acts; subject to judicial review post-2007 I.R. Coelho ruling", "type": "leaf"},
                            {"label": "10th Schedule: Provisions as to disqualification on ground of defection (inserted by 52nd Amendment 1985)", "type": "leaf"},
                            {"label": "11th & 12th Schedules: Municipalities (18 functional matters) and Panchayats (29 functional matters) powers", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 20. Sources of the Constitution
    elif 'sources' in fl:
        return [
            {
                "label": "Constitutional Sources",
                "type": "branch",
                "date": "Sources",
                "children": [
                    {
                        "label": "Government of India Act 1935", "type": "sub", "date": "GOI Act 1935", "children": [
                            {"label": "Federal Scheme: Formed the basic structural blueprint of the federal setup and list divisions", "type": "leaf"},
                            {"label": "Administrative Provisions: Governor office, judiciary structure, Public Service Commissions, and emergency setups", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Major Global Borrowings", "type": "sub", "date": "International", "children": [
                            {"label": "United Kingdom: Parliamentary government, rule of law, legislative procedure, single citizenship, cabinet system", "type": "leaf"},
                            {"label": "United States: Fundamental Rights, independent judiciary, judicial review, President impeachment procedure", "type": "leaf"},
                            {"label": "Ireland & South Africa: Directive Principles (Ireland); Amendment procedure & Rajya Sabha member elections (South Africa)", "type": "leaf"},
                            {"label": "USSR & Weimar: Fundamental Duties, justice ideals (USSR); Suspension of Fundamental Rights during Emergency (Weimar)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 21. Official Languages
    elif 'official-languages' in fl:
        return [
            {
                "label": "Language Administration",
                "type": "branch",
                "date": "Part XVII",
                "children": [
                    {
                        "label": "Union & State Languages", "type": "sub", "date": "Article 343-351", "children": [
                            {"label": "Article 343: Official language of the Union is Hindi in Devanagari script; English continued as associate language", "type": "leaf"},
                            {"label": "8th Schedule Languages: Expanded via 21st (Sindhi), 71st (Konkani, Manipuri, Nepali), and 92nd (Bodo, Dogri, Maithili, Santhali) Amendments", "type": "leaf"},
                            {"label": "Official Languages Commission: Appointed under Article 344 by President to recommend Hindi integration", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Classical Languages", "type": "sub", "date": "Classical Status", "children": [
                            {"label": "Criteria: High antiquity of early texts (1500-2000 years); valuable heritage; original literary tradition", "type": "leaf"},
                            {"label": "6 Classical Languages: Tamil (2004), Sanskrit (2005), Telugu (2008), Kannada (2008), Malayalam (2013), Odia (2014)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 22. Enactment & Facts
    elif 'enactment' in fl or 'facts-about' in fl:
        return [
            {
                "label": "Assembly Facts & Timeline",
                "type": "branch",
                "date": "Historical Milestones",
                "children": [
                    {
                        "label": "Drafting Timeline", "type": "sub", "date": "Key Timelines", "children": [
                            {"label": "Sessions: Took 2 years, 11 months, and 18 days across 11 sessions; adopted Nov 26, 1949; enforced Jan 26, 1950", "type": "leaf"},
                            {"label": "Cost & Scope: Visited constitutions of ~60 countries; draft was considered for 114 days; total cost Rs 64 lakh", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Key Officers & Symbols", "type": "sub", "date": "Officers", "children": [
                            {"label": "Assembly Symbol: Elephant was adopted as the official seal of the Constituent Assembly", "type": "leaf"},
                            {"label": "Constitutional Advisor: Sir B.N. Rau appointed as legal advisor; S.N. Mukherjee as chief draftsman", "type": "leaf"},
                            {"label": "Calligrapher: Prem Behari Narain Raizada handwritten the original constitution in flowing italic style", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]


    # 13. Historical evolution of the Constitution
    elif 'historical-evolution' in fl:
        return [
            {
                "label": "Evolution of Constitution",
                "type": "branch",
                "date": "Historical Development",
                "children": [
                    {
                        "label": "Key Phases", "type": "sub", "date": "1773-1947", "children": [
                            {"label": "Company Rule (1773-1858): Regulating Act 1773 established Governor-General of Bengal; Charter Act 1833 centralized power to Governor-General of India", "type": "leaf"},
                            {"label": "Crown Rule (1858-1947): Government of India Act 1858 introduced direct British Crown rule; GoI Act 1935 proposed federation; Independence Act 1947 partition", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 14. Other Constitutional Dimensions
    elif 'other-constitutional-dimensions' in fl:
        return [
            {
                "label": "Constitutional Dimensions",
                "type": "branch",
                "date": "Constitution Scope",
                "children": [
                    {
                        "label": "Key Aspects", "type": "sub", "date": "Features", "children": [
                            {"label": "Preamble, 395 Articles (originally), 8 original Schedules (now 12); longest written constitution in the world; blend of rigidity & flexibility", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

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
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback 1: tab1_marker with aria-labelledby
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)
        else:
            # Fallback 2: tab1_marker without aria-labelledby
            tab1_marker_no_aria = '<div class="tab-panel active" id="notes-panel" role="tabpanel">'
            if tab1_marker_no_aria in html:
                html = html.replace(tab1_marker_no_aria, tab1_marker_no_aria + '\n' + mindmap_card, 1)
            else:
                # Fallback 3: look for id="deep-dive-section"
                deep_dive_div = '<div class="card-premium" id="deep-dive-section">'
                if deep_dive_div in html:
                    html = html.replace(deep_dive_div, mindmap_card + '\n            ' + deep_dive_div, 1)

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
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        # Fallback 1: tab1_marker with aria-labelledby
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)
        else:
            # Fallback 2: tab1_marker without aria-labelledby
            tab1_marker_no_aria = '<div class="tab-panel active" id="notes-panel" role="tabpanel">'
            if tab1_marker_no_aria in html:
                html = html.replace(tab1_marker_no_aria, tab1_marker_no_aria + '\n' + mindmap_card, 1)
            else:
                # Fallback 3: look for id="deep-dive-section"
                deep_dive_div = '<div class="card-premium" id="deep-dive-section">'
                if deep_dive_div in html:
                    html = html.replace(deep_dive_div, mindmap_card + '\n            ' + deep_dive_div, 1)

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

