import os
import re
import json

# All categories we need to process
CATEGORIES = [
    "upsc/geography/Human-Economic-Geography",
    "upsc/geography/Climate-Soils-Vegetation",
    "upsc/geography/Physiography-Drainage",
    "upsc/polity/Governance-Welfare-Schemes",
    "upsc/polity/Political-Dynamics",
    "upsc/polity/Constitutional-Extra-Constitutional-Bodies",
    "upsc/polity/The-Judiciary-Supreme-Court-High-Court-Lok-Adalat",
    "upsc/polity/Local-Government-UTs-Special-Areas",
    "upsc/polity/State-Executive-State-Legislature",
    "upsc/polity/Union-Executive-Legislature-Parliament",
    "upsc/polity/System-of-Governance-Emergency-Provisions",
    "upsc/polity/Fundamental-Rights-DPSP-Fundamental-Duties"
]

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'nhrc', 'cag', 'upsc', 'spsc', 'sfc', 'fin', 'com'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Helper function to generate topic-wise custom branch structure
def get_custom_branches(folder_name, cat_basename):
    folder_lower = folder_name.lower()
    clean_title = get_clean_title(folder_name)
    
    # 1. Fundamental Rights, DPSP, & Duties
    if cat_basename == "Fundamental-Rights-DPSP-Fundamental-Duties":
        if 'article-12' in folder_lower:
            return [
                {"label": "Constitutional Scope", "type": "branch", "date": "Art 12 State", "children": [
                    {"label": "Includes Union Govt/Parliament, State Govt/Legislatures,\nlocal bodies, & other statutory/non-statutory agencies", "type": "leaf"},
                    {"label": "Statutory bodies (LIC, ONGC, SAIL) and private bodies\nacting as state instruments are covered", "type": "leaf"}
                ]},
                {"label": "Judicial Tests & Limits", "type": "branch", "date": "SC Rulings", "children": [
                    {"label": "BCCI Case: Not state, but performs public duties;\nJudiciary is State only in administrative role", "type": "leaf"},
                    {"label": "FRs only enforceable against State; protects citizens\nfrom executive and legislative overreach", "type": "leaf"}
                ]}
            ]
        elif 'article-13' in folder_lower:
            return [
                {"label": "Inconsistency Rules", "type": "branch", "date": "Art 13", "children": [
                    {"label": "Art 13(1): Pre-constitutional laws inconsistent with FRs\nare void; Art 13(2): Post-constitutional law limits", "type": "leaf"},
                    {"label": "Doctrinal Tools: Severability (only invalid part is void)\n& Eclipse (inconsistent law stays dormant)", "type": "leaf"}
                ]},
                {"label": "Definition of Law", "type": "branch", "date": "Art 13(3) & (4)", "children": [
                    {"label": "Includes ordinances, orders, bye-laws, rules,\nregulations, notifications, custom or usage", "type": "leaf"},
                    {"label": "Kesavananda (1973): Constitutional amendments are not\n'laws', but cannot violate the Basic Structure", "type": "leaf"}
                ]}
            ]
        elif 'equality' in folder_lower:
            return [
                {"label": "Equality Rights (Art 14-18)", "type": "branch", "date": "Part III Core", "children": [
                    {"label": "Art 14: Equality before law & equal protection;\nArt 15: Non-discrimination on 5 specific grounds", "type": "leaf"},
                    {"label": "Art 16: Equal opportunity in public employment;\nArt 17: Abolition of untouchability; Art 18: Abolition of titles", "type": "leaf"}
                ]},
                {"label": "Exceptions & Reservations", "type": "branch", "date": "Reasonable Class", "children": [
                    {"label": "Art 14 permits reasonable classification; bans class legislation;\nArt 15 & 16 permit reservations for backward classes/women", "type": "leaf"}
                ]}
            ]
        elif 'freedom' in folder_lower and 'religion' not in folder_lower:
            return [
                {"label": "Six Liberties (Art 19)", "type": "branch", "date": "Democratic Pillars", "children": [
                    {"label": "Freedom of speech & expression, peaceful assembly, association,\nmovement, residence, and profession/trade", "type": "leaf"},
                    {"label": "Reasonable restrictions: Sovereignty, security, public order,\ndecency, morality, and contempt of court", "type": "leaf"}
                ]},
                {"label": "Protection Articles (20-22)", "type": "branch", "date": "Personal Liberties", "children": [
                    {"label": "Art 20: No ex-post facto laws, double jeopardy, or self-incrimination;\nArt 21: Protection of life & personal liberty", "type": "leaf"},
                    {"label": "Art 21A: Right to free & compulsory education;\nArt 22: Protection against arbitrary arrest & detention", "type": "leaf"}
                ]}
            ]
        elif 'exploitation' in folder_lower:
            return [
                {"label": "Articles 23 & 24", "type": "branch", "date": "Human Dignity", "children": [
                    {"label": "Art 23: Prohibits human trafficking, begar (forced labor),\nand other similar forms of compulsory labor", "type": "leaf"},
                    {"label": "Art 24: Prohibits employment of children below 14 years\nin factories, mines, & other hazardous jobs", "type": "leaf"}
                ]}
            ]
        elif 'religion' in folder_lower:
            return [
                {"label": "Religious Freedom (Art 25-28)", "type": "branch", "date": "Secular Fabric", "children": [
                    {"label": "Art 25: Conscience, free profession, practice, & propagation;\nArt 26: Right to manage religious affairs/institutions", "type": "leaf"},
                    {"label": "Art 27: Freedom from taxation for promoting religion;\nArt 28: Freedom from religious instruction in state schools", "type": "leaf"}
                ]}
            ]
        elif 'remedies' in folder_lower or 'article-32' in folder_lower:
            return [
                {"label": "Constitutional Remedies", "type": "branch", "date": "Art 32", "children": [
                    {"label": "Heart & Soul of Constitution; provides direct access to\nSupreme Court for enforcement of Fundamental Rights", "type": "leaf"},
                    {"label": "Five Writs: Habeas Corpus (release), Mandamus (perform),\nProhibition (stay), Certiorari (quash), Quo Warranto (office)", "type": "leaf"}
                ]}
            ]
        elif 'dpsp' in folder_lower or 'principles' in folder_lower:
            return [
                {"label": "DPSP Pillars & Features", "type": "branch", "date": "Part IV (Art 36-51)", "children": [
                    {"label": "Non-justiciable welfare directives; Socialistic (Art 38, 39, 41);\nGandhian (Art 40, 43, 47, 48); Liberal-Intellectual (Art 44, 48A, 50)", "type": "leaf"},
                    {"label": "Minerva Mills (1980): Harmony between FRs & DPSPs is basic structure;\n42nd Amendment added Art 39A (free aid) & 48A (environment)", "type": "leaf"}
                ]}
            ]
        elif 'duty' in folder_lower or 'duties' in folder_lower:
            return [
                {"label": "Duties & Verma Panel", "type": "branch", "date": "Part IVA (Art 51A)", "children": [
                    {"label": "Swaran Singh Committee (1976); 10 duties originally, 11th added\nby 86th Amendment; Verma Committee (1999) lists enforcement laws", "type": "leaf"},
                    {"label": "Duties apply only to citizens; non-justiciable but used\nby courts to determine constitutional validity of laws", "type": "leaf"}
                ]}
            ]
        elif 'judicial-review' in folder_lower:
            return [
                {"label": "Judicial Review Concept", "type": "branch", "date": "Syllabus Core", "children": [
                    {"label": "Power of judiciary to review legislative acts & executive orders;\ndeclares them void if they violate constitutional limits", "type": "leaf"},
                    {"label": "L. Chandra Kumar Case: Judicial review under Art 32/226\nis part of the unamendable Basic Structure", "type": "leaf"}
                ]}
            ]
        elif 'rule-of-law' in folder_lower:
            return [
                {"label": "Rule of Law Principles", "type": "branch", "date": "AV Dicey Concept", "children": [
                    {"label": "Absence of arbitrary power (supremacy of law);\nequality before law; constitutional spirit is result of common law", "type": "leaf"},
                    {"label": "Kesavananda Case: Rule of Law is a fundamental pillar\nof India's Basic Structure doctrine", "type": "leaf"}
                ]}
            ]
        elif 'due-process' in folder_lower or 'procedure-established' in folder_lower:
            return [
                {"label": "Legal Standards", "type": "branch", "date": "Art 21 Test", "children": [
                    {"label": "Procedure Established: Law must be validly enacted;\nDue Process: Law must also be just, fair, & reasonable", "type": "leaf"},
                    {"label": "Maneka Gandhi Case (1978): Read Due Process into Article 21;\nprotects citizens from both executive & legislative arbitrariness", "type": "leaf"}
                ]}
            ]
            
    # 2. System of Governance & Emergency
    elif cat_basename == "System-of-Governance-Emergency-Provisions":
        if 'national-emergency' in folder_lower:
            return [
                {"label": "Article 352 Setup", "type": "branch", "date": "National Threat", "children": [
                    {"label": "Grounds: War, external aggression, or armed rebellion;\nrequires written recommendation of Union Cabinet", "type": "leaf"},
                    {"label": "Approved within 1 month by special majority; auto-suspends\nArt 19 under Art 358; others suspended under Art 359", "type": "leaf"}
                ]}
            ]
        elif 'presidents-rule' in folder_lower:
            return [
                {"label": "Article 356 & 365", "type": "branch", "date": "State Breakdown", "children": [
                    {"label": "Grounds: Failure of state constitutional machinery (Art 356)\nor failure to comply with Union directions (Art 365)", "type": "leaf"},
                    {"label": "SR Bommai (1994): Subject to judicial review; floor test\nmandatory; state assembly cannot be dissolved before approval", "type": "leaf"}
                ]}
            ]
        elif 'financial-emergency' in folder_lower:
            return [
                {"label": "Article 360 Setup", "type": "branch", "date": "Fiscal Instability", "children": [
                    {"label": "Grounds: Threat to financial stability or credit of India;\napproved by simple majority in 2 months; no maximum duration", "type": "leaf"},
                    {"label": "Effects: Reduction of salaries of public servants & judges;\nstate money bills reserved for Presidential assent", "type": "leaf"}
                ]}
            ]
        elif 'centre-state-relations-legislative' in folder_lower:
            return [
                {"label": "Legislative Relations", "type": "branch", "date": "Art 245-255", "children": [
                    {"label": "Territorial jurisdiction; division of subjects (7th Schedule);\nParliament's power to legislate on State List (Art 249-253)", "type": "leaf"},
                    {"label": "Residuary powers under Art 248; Union law supremacy\nin case of conflict (repugnancy under Art 254)", "type": "leaf"}
                ]}
            ]
        elif 'centre-state-relations-financial' in folder_lower:
            return [
                {"label": "Financial Relations", "type": "branch", "date": "Art 268-293", "children": [
                    {"label": "Tax distribution post-GST; grants-in-aid (Art 275 statutory,\nArt 282 discretionary); borrowing limits under Art 293", "type": "leaf"},
                    {"label": "Finance Commission (Art 280) acts as balancing wheel;\ndecides tax devolution shares to states", "type": "leaf"}
                ]}
            ]
        elif 'water-dispute' in folder_lower:
            return [
                {"label": "Water Disputes (Art 262)", "type": "branch", "date": "Inter-State", "children": [
                    {"label": "Parliament creates tribunals to adjudicate river disputes;\nbars Supreme Court & other court jurisdiction on matters", "type": "leaf"},
                    {"label": "Inter-State Water Disputes Act 1956; issues: delays\nin setting up tribunals & enforcing awards", "type": "leaf"}
                ]}
            ]
        elif 'councils' in folder_lower:
            return [
                {"label": "Federal Councils", "type": "branch", "date": "Interstate Platforms", "children": [
                    {"label": "Inter-State Council (Art 263): Chaired by PM; constitutional;\nZonal Councils: Statutory (States Reorganisation Act); chaired by HM", "type": "leaf"}
                ]}
            ]
            
    # 3. Union Executive & Parliament
    elif cat_basename == "Union-Executive-Legislature-Parliament":
        if 'president' in folder_lower and 'vice' not in folder_lower:
            return [
                {"label": "President (Art 52-62)", "type": "branch", "date": "State Head", "children": [
                    {"label": "Elected by electoral college: elected MPs & MLAs;\nno nominated members participate (Art 54)", "type": "leaf"},
                    {"label": "Pardoning powers (Art 72); Veto powers (Art 111);\nOrdinance power (Art 123); Impeachment under Art 61", "type": "leaf"}
                ]}
            ]
        elif 'prime-minister' in folder_lower or 'council-of-minister' in folder_lower:
            return [
                {"label": "PM & CoM (Art 74-75)", "type": "branch", "date": "Government Head", "children": [
                    {"label": "Art 74: Advice to President is binding; Art 75: Ministers\nhold office during pleasure, collective responsibility to LS", "type": "leaf"},
                    {"label": "91st Amendment: Cabinet strength limited to 15% of LS;\nCabinet Committees: headed by PM (ACC, CCS, CCPA)", "type": "leaf"}
                ]}
            ]
        elif 'speaker' in folder_lower:
            return [
                {"label": "Presiding Speaker", "type": "branch", "date": "LS Presider", "children": [
                    {"label": "Elected by Lok Sabha; decides money bills; decider\nof anti-defection cases under 10th Schedule", "type": "leaf"},
                    {"label": "Speaker Pro Tem: Administers oaths to new house;\nresigns to Deputy Speaker (not President)", "type": "leaf"}
                ]}
            ]
        elif 'privileges' in folder_lower:
            return [
                {"label": "Privileges (Art 105)", "type": "branch", "date": "Immunities", "children": [
                    {"label": "Collective: Right to publish debates, exclude strangers;\nIndividual: Freedom of speech, civil arrest immunity", "type": "leaf"}
                ]}
            ]
        elif 'sessions' in folder_lower:
            return [
                {"label": "Sessions & Devices", "type": "branch", "date": "Chamber Meetings", "children": [
                    {"label": "Summoned by President (max 6-month gap); Adjournment\nvs Prorogation vs Dissolution", "type": "leaf"},
                    {"label": "Question Hour (Starred/Unstarred), Zero Hour;\nCensure vs No-Confidence Motions (LS only)", "type": "leaf"}
                ]}
            ]
        elif 'funds' in folder_lower:
            return [
                {"label": "Parliamentary Funds", "type": "branch", "date": "Art 266 & 267", "children": [
                    {"label": "Consolidated Fund (Art 266(1)): revenues/loans; Contingency\nFund (Art 267): President's disposal; Public Account (Art 266(2))", "type": "leaf"}
                ]}
            ]
            
    # 4. State Executive & State Legislature
    elif cat_basename == "State-Executive-State-Legislature":
        if 'governor' in folder_lower:
            return [
                {"label": "Governor (Art 153-162)", "type": "branch", "date": "State Head", "children": [
                    {"label": "Appointed by President; dual role: state head & Center agent;\nArt 213 Ordinance power; Art 161 pardoning power", "type": "leaf"},
                    {"label": "Art 163 constitutional discretion; reserving bills under Art 200;\nSarkaria & Punchhi recommendations on office reforms", "type": "leaf"}
                ]}
            ]
        elif 'legislative-assembly' in folder_lower or 'legislative-council' in folder_lower:
            return [
                {"label": "State Legislative Chambers", "type": "branch", "date": "Vidhan Sabha / Parishad", "children": [
                    {"label": "Assembly (Sabha): Direct election; 5-yr term; max 500/min 60;\nCouncil (Parishad): Permanent; Art 169 creation/abolition", "type": "leaf"},
                    {"label": "Council composition: 1/3rd local bodies, 1/3rd MLAs,\n1/12th graduates, 1/12th teachers, 1/6th Governor nominated", "type": "leaf"}
                ]}
            ]
            
    # 5. Local Government & UTs
    elif cat_basename == "Local-Government-UTs-Special-Areas":
        if '73rd' in folder_lower or 'panchayati' in folder_lower:
            return [
                {"label": "Panchayati Raj (73rd CA)", "type": "branch", "date": "Part IX", "children": [
                    {"label": "Added Part IX & 11th Schedule (29 functions); Gram Sabha\nfoundation; 3-tier structure; 33% reservation for women", "type": "leaf"},
                    {"label": "State Finance Commission & State Election Commission;\nCompulsory (3-tier, elections) vs Voluntary provisions", "type": "leaf"}
                ]}
            ]
        elif '74th' in folder_lower or 'urban-local' in folder_lower or 'urban-government' in folder_lower:
            return [
                {"label": "Urban Local Gov (74th CA)", "type": "branch", "date": "Part IXA", "children": [
                    {"label": "Added Part IXA & 12th Schedule (18 functions); Nagar Panchayat,\nMunicipal Council, Municipal Corporation; Wards Committees", "type": "leaf"},
                    {"label": "DPC (District Planning Committee) under Art 243ZD;\nMPC (Metropolitan Planning) under Art 243ZE", "type": "leaf"}
                ]}
            ]
        elif 'pesa' in folder_lower:
            return [
                {"label": "PESA Act 1996", "type": "branch", "date": "Scheduled Areas", "children": [
                    {"label": "Extends Part IX to 5th Schedule areas; empowers Gram\nSabha over minor forest produce, land acquisition, & resources", "type": "leaf"}
                ]}
            ]
        elif 'schedule' in folder_lower or 'tribal' in folder_lower:
            return [
                {"label": "5th & 6th Schedules", "type": "branch", "date": "Tribal Administration", "children": [
                    {"label": "5th Schedule: Tribes Advisory Councils (TAC) in 10 states;\n6th Schedule: Autonomous District Councils (ADC) in AMTM", "type": "leaf"}
                ]}
            ]
            
    # 6. The Judiciary
    elif cat_basename == "The-Judiciary-Supreme-Court-High-Court-Lok-Adalat":
        if 'supreme-court' in folder_lower:
            return [
                {"label": "Supreme Court Setup", "type": "branch", "date": "Art 124-147", "children": [
                    {"label": "Appointed by President (Collegium system); Art 129 court\nof record; Art 141 law declared by SC is binding on all courts", "type": "leaf"},
                    {"label": "Jurisdictions: Original (Art 131), Writ (Art 32), Appellate\n(Art 132-136), & Advisory (Art 143; binding on none)", "type": "leaf"}
                ]}
            ]
        elif 'high-court' in folder_lower:
            return [
                {"label": "High Court Setup", "type": "branch", "date": "Art 214-231", "children": [
                    {"label": "Appointed by President in consultation with CJI & Governor;\nArt 226 writ jurisdiction (wider than SC, includes legal rights)", "type": "leaf"},
                    {"label": "Art 227 power of superintendence over all subordinate\ncourts within its territorial jurisdiction", "type": "leaf"}
                ]}
            ]
        elif 'subordinate' in folder_lower:
            return [
                {"label": "Subordinate Judiciary", "type": "branch", "date": "Art 233-237", "children": [
                    {"label": "District Judges appointed by Governor in consultation with High\nCourt; other judges appointed via State Public Service commission", "type": "leaf"}
                ]}
            ]
        elif 'adalat' in folder_lower or 'adr' in folder_lower:
            return [
                {"label": "ADR & Lok Adalats", "type": "branch", "date": "Alternative Redressal", "children": [
                    {"label": "Lok Adalats: Statutory status under Legal Services Authorities\nAct; award has force of civil decree; no appeal lies anywhere", "type": "leaf"},
                    {"label": "ADR mechanisms: Arbitration, Mediation, & Conciliation;\nspeedy justice; reduction of pending court cases", "type": "leaf"}
                ]}
            ]
            
    # 7. Constitutional & Extra Constitutional Bodies
    elif cat_basename == "Constitutional-Extra-Constitutional-Bodies":
        if 'cag' in folder_lower or 'comptroller' in folder_lower:
            return [
                {"label": "CAG (Art 148-151)", "type": "branch", "date": "Guardian of Purse", "children": [
                    {"label": "Appointed by President; 6 yr/65 age term; removed\nlike SC judge; audits all Union/State expenses", "type": "leaf"},
                    {"label": "Submits audit reports to President/Governor;\nexamines proprietary and efficiency of government spending", "type": "leaf"}
                ]}
            ]
        elif 'finance' in folder_lower and 'commission' in folder_lower:
            return [
                {"label": "Finance Commission", "type": "branch", "date": "Article 280", "children": [
                    {"label": "Quasi-judicial body appointed by President every 5 years;\nrecommends net tax proceeds distribution between Center/States", "type": "leaf"},
                    {"label": "Grants-in-aid criteria; principles to augment resources\nof local panchayats/municipalities", "type": "leaf"}
                ]}
            ]
        elif 'election' in folder_lower:
            return [
                {"label": "Election Commission", "type": "branch", "date": "Article 324", "children": [
                    {"label": "Conducts elections for Parliament, State Legislatures,\nand offices of President & Vice President", "type": "leaf"}
                ]}
            ]
        elif 'upsc' in folder_lower or 'public-service' in folder_lower:
            return [
                {"label": "Public Service Commissions", "type": "branch", "date": "Art 315-323", "children": [
                    {"label": "UPSC & SPSC: Independent recruitment bodies; advice is advisory;\nUPSC members removed by President on reference to SC", "type": "leaf"}
                ]}
            ]
        elif 'niti' in folder_lower or 'planning' in folder_lower:
            return [
                {"label": "NITI Aayog (Extra-Const)", "type": "branch", "date": "Cabinet Resolution", "children": [
                    {"label": "Cooperative Federalism; think tank; bottom-up planning;\nchaired by PM; replaced Planning Commission in 2015", "type": "leaf"}
                ]}
            ]
            
    # 8. Climate, Soils, & Vegetation
    elif cat_basename == "Climate-Soils-Vegetation":
        if 'monsoon' in folder_lower or 'climate' in folder_lower:
            return [
                {"label": "Monsoon Dynamics", "type": "branch", "date": "Monsoon", "children": [
                    {"label": "Thermal contrast; Flohn's ITCZ shift; Westerly Jet retreat;\nTropical Easterly Jet heating; Somali Jet moisture feed", "type": "leaf"},
                    {"label": "Köppen classification: Amw (Malabar), Aw (Savanna),\nCwg (Gangetic), Bshw (Steppe), Dfc (Arunachal)", "type": "leaf"}
                ]}
            ]
        elif 'soil' in folder_lower:
            return [
                {"label": "Soil Taxonomy", "type": "branch", "date": "ICAR Taxonomy", "children": [
                    {"label": "Alluvial (Khadar/Bhangar, potash rich); Regur/Black (cotton,\nmoisture holding); Laterite (rain leached, iron rich)", "type": "leaf"},
                    {"label": "Erosion: Splash -> Sheet -> Rill -> Gully (Chambal ravines);\nRestoration: Contour bunding, strip cropping, shelterbelts", "type": "leaf"}
                ]}
            ]
        elif 'vegetation' in folder_lower or 'forest' in folder_lower:
            return [
                {"label": "Forest Ecosystems", "type": "branch", "date": "Vegetation", "children": [
                    {"label": "Tropical Evergreen (high rain, ebony/rosewood); Deciduous\n(teak/sal, dry season leaf drop); Montane (coniferous)", "type": "leaf"},
                    {"label": "Mangroves (Littoral/Swamp, Sundarbans, pneumatophores);\nNational Forest Policy target: 33% geographical area forest cover", "type": "leaf"}
                ]}
            ]
            
    # 9. Physiography & Drainage
    elif cat_basename == "Physiography-Drainage":
        if 'drainage' in folder_lower or 'river' in folder_lower:
            return [
                {"label": "River Systems", "type": "branch", "date": "Himalayan vs Peninsular", "children": [
                    {"label": "Himalayan: Antecedent, perennial, high erosion, gorges;\nIndus (tributaries JCSB), Ganga, & Brahmaputra", "type": "leaf"},
                    {"label": "Peninsular: Non-perennial, graded profiles, deltas;\nEast flowing: Mahanadi, Godavari, Krishna, Cauvery", "type": "leaf"},
                    {"label": "West flowing: Narmada, Tapi (rift valley flows without deltas);\nDrainage patterns: Dendritic, Radial, Trellis, Centripetal", "type": "leaf"}
                ]}
            ]
        elif 'physiography' in folder_lower or 'himalaya' in folder_lower or 'plains' in folder_lower or 'plateau' in folder_lower:
            return [
                {"label": "Physiographic Zones", "type": "branch", "date": "Geomorphology", "children": [
                    {"label": "Himalayas: Himadri (inner), Himachal (middle), Shiwalik (outer);\nNorthern Plains: Bhabar (pebbles), Terai (marshy), Bhangar, Khadar", "type": "leaf"},
                    {"label": "Peninsular Plateau: Oldest landmass, Deccan Trap, Western\n& Eastern Ghats; Coastal Plains & island territories", "type": "leaf"}
                ]}
            ]

    # 10. Human & Economic Geography
    elif cat_basename == "Human-Economic-Geography":
        if 'agriculture' in folder_lower or 'crop' in folder_lower or 'farming' in folder_lower:
            return [
                {"label": "Agricultural Systems", "type": "branch", "date": "Syllabus Core", "children": [
                    {"label": "Farming types: Subsistence, intensive, commercial, plantation;\nSeasons: Kharif (rice), Rabi (wheat), Zaid (melons)", "type": "leaf"},
                    {"label": "Green Revolution (HYV, fertilizers, irrigation impacts);\nAllied: Blue (fish), Yellow (oilseeds), Golden (horticulture)", "type": "leaf"}
                ]}
            ]
        elif 'mineral' in folder_lower or 'resource' in folder_lower or 'energy' in folder_lower:
            return [
                {"label": "Mineral & Energy", "type": "branch", "date": "Resources", "children": [
                    {"label": "Metallic: Iron ore (Singhbhum, Bailadila), Bauxite;\nNon-metallic: Mica; Coal fields: Gondwana (Damodar valley)", "type": "leaf"},
                    {"label": "Energy: Solar (ISA, Khavda park), Wind (Muppandal),\nGeothermal, Nuclear power stations in India", "type": "leaf"}
                ]}
            ]
        elif 'industry' in folder_lower or 'industrial' in folder_lower:
            return [
                {"label": "Industrial Sectors", "type": "branch", "date": "Location Factors", "children": [
                    {"label": "Weber's Industrial Location: weight-losing raw materials;\nIron & Steel (Jamshedpur, Bhilai); Cotton Textile clusters", "type": "leaf"}
                ]}
            ]
        elif 'population' in folder_lower or 'demographic' in folder_lower or 'census' in folder_lower:
            return [
                {"label": "Demographic Factors", "type": "branch", "date": "Census 2011", "children": [
                    {"label": "Population density, distribution; Demographic Dividend;\nSex ratio, literacy rates; rural-urban migration factors", "type": "leaf"}
                ]}
            ]

    # GENERAL FALLBACK (Customized to topic name to ensure NO REPETITION)
    return [
        {"label": "Core Dimensions", "type": "branch", "date": clean_title, "children": [
            {"label": f"Definition, fundamental scope, & boundaries of {clean_title}", "type": "leaf"},
            {"label": f"Historical evolution, milestones, & modern governance structural framework", "type": "leaf"}
        ]}
]

# Generate and patch mindmaps
def process_folder(category_path, folder_name):
    html_path = os.path.join(category_path, folder_name, "index.html")
    content_json_path = os.path.join(category_path, folder_name, "content.json")
    
    if not os.path.exists(html_path):
        return False
        
    cat_basename = os.path.basename(category_path)
    clean_title = get_clean_title(folder_name)
    
    # Read content.json if exists to get exact hero title
    topic_name = clean_title
    if os.path.exists(content_json_path):
        try:
            with open(content_json_path, 'r', encoding='utf-8') as f:
                c_data = json.load(f)
                topic_name = c_data.get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    # Build unique mindmap data
    branches = get_custom_branches(folder_name, cat_basename)
    mindmap_data = {
        "label": clean_title,
        "type": "root",
        "children": branches
    }
    
    # Clean previous mindmap tags to prevent duplicates
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n', '')
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    # Re-inject Mindmap Div
    instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
    title_text = f"{topic_name} &mdash; Interactive Mindmap"
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
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script
    tree_json = json.dumps(mindmap_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, 'en');
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return True

def main():
    total_processed = 0
    for cat in CATEGORIES:
        if not os.path.exists(cat):
            print(f"Skipping missing category path: {cat}")
            continue
        folders = [f for f in os.listdir(cat) if os.path.isdir(os.path.join(cat, f))]
        print(f"Processing category: {cat} ({len(folders)} topics)")
        
        for f in folders:
            success = process_folder(cat, f)
            if success:
                total_processed += 1
                
    print(f"\nCompleted! Successfully patched {total_processed} files with topic-specific mindmaps.")

if __name__ == '__main__':
    main()
