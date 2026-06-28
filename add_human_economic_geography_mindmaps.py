import os
import re
import json

BASE_DIR = r"upsc/geography/Human-Economic-Geography"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'dpsp', 'pri', 'ut', 'uts', 'sc', 'hc', 'cm', 'com', 'arc', 'inc', 'ias', 'sec', 'sfc', 'pej', 'tej', 'mjo', 'enso', 'iod', 'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'msp', 'cacp', 'nam', 'fci', 'hyv', 'niif', 'dfc', 'opec', 'sez', 'msme', 'npp', 'spr', 'apmc', 'zbnf', 'pkvy', 'pmksy', 'fbr', 'phwr', 'ahwr', 'isa', 'ppp', 'pmgsy'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Factual database mapping keywords to rich UPSC fact strings
FACTS = {
    "marketing": [
        "APMC monopoly: Farmers forced to sell via licensed brokers, leading to high commission charges (up to 10%) & price deduction",
        "e-NAM (Electronic National Agriculture Market): Integrates mandis; provides online bidding, assaying facilities, & unified licensing",
        "Infrastructure gaps: Only ~7,000 regulated markets exist vs required 22,000; cold storage shortage leads to 30%+ perishable waste",
        "Contract farming reforms: Model Contract Farming Act 2018; shields farmers from price risks; integrates corporate buyers"
    ],
    "pricing": [
        "MSP (Minimum Support Price): Calculated by CACP based on A2 (actual paid-out costs) + FL (family labor value) & C2 comprehensive costs",
        "Crop bias: Skewed heavily toward wheat & rice; leads to monoculture, depletion of water table, and negligence of pulses & millets",
        "FCI reforms: Shanta Kumar Committee (2015) recommended PDS digitization, FCI restructuring, and direct cash transfers for leaks",
        "WTO green box limits: Subsidies debate; peace clause protects India's MSP procurement under National Food Security Act (NFSA)"
    ],
    "productivity": [
        "Yield gap: India's average yields for rice (~2.4 t/ha) & wheat (~3.1 t/ha) are 30-50% below global giants like China & US",
        "Land fragmentation: Average farm size shrunk to 1.08 hectares; prevents adoption of heavy farm machinery & economies of scale",
        "Technology lag: Low seed replacement rates; poor mechanization (40-45% compared to 95% in US); high dependency on rainfed farming",
        "Mitigation: Soil Health Card diagnostics; custom hiring centers for tractors; laser land levelers to improve water use efficiency"
    ],
    "irrigation": [
        "Water sources: Skewed heavily to groundwater (tubewells ~62%), leading to rapid aquifer depletion; canal systems (~26%)",
        "PMKSY (Krishi Sinchayee Yojana): Aim of 'Har Khet Ko Pani' (water to every field) & 'Per Drop More Crop' precision systems",
        "Micro-irrigation: Drip & sprinkler systems save up to 40% water; reduces fertilizer leaching; prevents soil salinization",
        "Command Area Dev: Resolves gap between created irrigation potential and actual utilized capacity via field channels"
    ],
    "green-revolution": [
        "Phase 1 (1966-72): Centered on High Yielding Variety (HYV) Wheat seeds (Lerma Rojo, Sonora 64); limited to Punjab, Haryana & West UP",
        "Input package: Assured tubewell irrigation + NPK chemical fertilizers + pesticides; led to rapid foodgrain self-sufficiency",
        "Soil degradation: Over-irrigation caused soil salinization (usar lands); NPK ratio skewed (6.7:2.4:1 vs optimal 4:2:1)",
        "Groundwater depletion: Water table in Punjab dropping at ~0.5m per year due to continuous double cropping of wheat & paddy"
    ],
    "sustainable": [
        "ZBNF (Zero Budget Natural Farming): Promotes Jivamrita (microbial inoculant), Bijamrita (seed treatment), & Acchadana (mulching)",
        "Organic farming: PKVY scheme; Sikkim declared 100% organic state; improves soil organic carbon and commands export premiums",
        "Conservation agriculture: Focuses on minimal soil tillage, permanent crop residue cover, and crop rotation to preserve soil structure",
        "SLM (Sustainable Land Management): Agro-forestry integration, contour bunding, & windbreaks to halt desertification"
    ],
    "coal": [
        "Gondwana Coal (98%): Carboniferous age; found in Damodar, Mahanadi, Sone basins; Jharia, Raniganj; low sulphur, high ash content",
        "Tertiary Coal: Lignite type; found in Neyveli (Tamil Nadu), Rajasthan, & Jammu Kashmir; high moisture & lower thermal output",
        "Sector reforms: Commercial coal mining introduced; coal gasification target of 100 MT by 2030; reducing coking coal imports",
        "Environmental checks: Fly ash utilization rules; coal washeries mandated to reduce ash transport emissions"
    ],
    "oil": [
        "Onshore reserves: Digboi (Assam, oldest operational), Cambay (Gujarat), and major recent discoveries in Barmer (Rajasthan)",
        "Offshore reserves: Mumbai High (largest), Bassein; deepwater exploration in KG Basin; high dependence on crude imports (~85%)",
        "SPR (Strategic Petroleum Reserves): Storage caverns in Visakhapatnam, Mangaluru, & Padur (total ~5.33 MT) for energy security",
        "Refinement capacity: India is a net exporter of refined products; Jamnagar refinery (Reliance) is world's largest complex"
    ],
    "gas": [
        "KG Basin D6: Major deepwater gas reserves; Reliance gas extraction; disputes over gas pricing & production targets",
        "HBJ Pipeline: Hazira-Bijaypur-Jagdishpur; trunk pipeline network feeding gas to major inland urea fertilizer complexes",
        "City Gas Distribution: Piped Natural Gas (PNG) and Compressed Natural Gas (CNG) network expansion to reduce urban pollution",
        "LNG terminals: Dahej, Hazira, Kochi, Dabhol; importing liquefied natural gas to meet industrial and fuel shortages"
    ],
    "solar": [
        "National target: 280 GW by 2030; ISA (International Solar Alliance) headquarters in Gurugram, India; grid integration challenges",
        "Mega parks: Bhadla (Rajasthan, world's largest, ~2,245 MW), Pavagada (Karnataka, ~2,050 MW), Kurnool (Andhra Pradesh)",
        "PM-KUSUM: Solarization of farm pumps; grid connected pumps let farmers sell surplus power; reduces diesel fuel expenses",
        "Rooftop solar: Subsidies under PM Surya Ghar Yojana; challenges in net metering approvals by state discom companies"
    ],
    "wind": [
        "Resource centers: Tamil Nadu (Muppandal, largest onshore wind farm in India), Gujarat, Maharashtra, Karnataka, Rajasthan",
        "Offshore wind: Vast potential along Gujarat & Tamil Nadu coasts (~70 GW); national policy supports viability gap funding",
        "Technology: Grid integration issues due to seasonal and hourly variability; hybrid solar-wind parks to stabilize power output",
        "NIWE (National Institute of Wind Energy): Apex body for resource mapping, wind turbine testing, & certification"
    ],
    "nuclear": [
        "Stage 1: Pressurized Heavy Water Reactors (PHWRs); uses natural Uranium fuel & heavy water moderator; generates Plutonium-239",
        "Stage 2: Fast Breeder Reactors (FBRs); uses Plutonium-239 & Uranium-238; Kalpakkam PFBR; breeds more fuel than consumed",
        "Stage 3: Advanced Heavy Water Reactors (AHWRs); utilizes Thorium-232 & Uranium-233 to tap India's massive monazite sand reserves",
        "Active plants: Tarapur (MH), Rawatbhata (RJ), Kudankulam (TN, largest capacity), Kakrapar (GJ), Kaiga (KA)"
    ],
    "iron": [
        "Location factors: Raw-material oriented (weight-losing); requires 2 tons of iron ore + 1.5 tons of coal + limestone per ton of steel",
        "Major regions: Chhotanagpur plateau; Jamshedpur (TISCO, private), Bhilai, Rourkela, Durgapur, Bokaro (public, SAIL)",
        "Port-based plants: Visakhapatnam steel plant; utilizes coastal import-export advantages for raw materials & steel shipping",
        "Iron ore belts: Barabil-Koira (Odisha), Singhbhum (Jharkhand), Bailadila (Chhattisgarh), Bellary-Hospet (Karnataka)"
    ],
    "textile": [
        "Cotton location: Originally humid Mumbai/Ahmedabad; now dispersed to Coimbatore (South Manchester), Ludhiana, & Solapur",
        "Jute concentration: Hooghly basin (West Bengal); abundant soft water for retting, cheap labor, & dense transport networks",
        "Sector challenges: Technological obsolescence in powerlooms; high raw material price volatility; Jute packaging mandates",
        "TUFS (Technology Upgradation Fund Scheme): Financial support to modernize weaving, spinning, and processing machinery"
    ],
    "fertilizer": [
        "Urea sector: Highly subsidized; Neem-coated urea introduced to check diversion to chemical industries & slow nitrogen release",
        "P&K fertilizers: Heavy import dependence for raw materials (rock phosphate, phosphoric acid, potash); NBS pricing scheme",
        "Nano Urea: Developed by IFFCO; liquid spray system; drastically reduces transport costs, storage space, & fertilizer runoff",
        "PM PRANAM scheme: Incentivizes states to promote alternative fertilizers and reduce overall chemical fertilizer consumption"
    ],
    "industrial-regions": [
        "Hooghly region: Oldest; jute, paper, engineering; declined due to partition, labor issues, and lack of modernization",
        "Mumbai-Pune corridor: Cotton, chemicals, automobiles, IT; high market access, capital availability, & port connectivity",
        "Bengaluru-Tamil Nadu: Aircraft, electronics, heavy engineering, IT; skilled labor, public sector investments, & climate",
        "New initiatives: Industrial Corridors (DMIC, AKIC), Special Economic Zones (SEZs), and National Investment & Manufacturing Zones (NIMZs)"
    ],
    "dividend": [
        "Age structure: working-age population (15-59) exceeds 60% of total; dependency ratio drop; window open till ~2040s",
        "Prerequisites: Requires matching job creation + skill training (Skill India) + health infrastructure to reap benefits",
        "State disparity: South states (Kerala, TN) aging faster; north states (UP, Bihar) entering peak dividend phase",
        "Risks: Demographic disaster if youth remain unemployed, unskilled, or face poor health & lack of formal jobs"
    ],
    "census": [
        "Census 2011 stats: Total population 1.21 billion; average density 382 per sq km; Bihar highest density (1,106 per sq km)",
        "Decadal growth: 17.7% (2001-2011); growth rate declining; Year of Great Divide (1921) when growth rate turned negative",
        "Literacy: National average 74.04% (Male 82.14%, Female 65.46%); Kerala highest (94%), Bihar lowest (61.8%)",
        "Urbanization: 31.16% population lives in urban areas; rapid growth in class-I cities and metropolitan agglomerations"
    ],
    "gender": [
        "Sex Ratio 2011: 943 females per 1000 males; child sex ratio (0-6 years) dropped to 919 (severe concern)",
        "Regional skew: Haryana (879) & Punjab lowest sex ratios; Kerala (1084) and Puducherry highest female ratios",
        "Socio-cultural causes: Son meta-preference, female foeticide, unequal access to nutrition, & poor health indicators",
        "Interventions: Beti Bachao Beti Padhao; Pre-Conception & Pre-Natal Diagnostic Techniques (PCPNDT) Act strict enforcement"
    ],
    "settlement": [
        "Rural settlements: Clustered/nucleated (fertile Indo-Gangetic plains), semi-clustered, hamleted, and dispersed (hills/deserts)",
        "Urban classification: Statutory towns (notified by municipality) vs Census towns (5,000+ pop, 75% non-farm male labor, 400/sq km)",
        "Urban issues: Slums (Dharavi), water crisis, urban flooding (poor drainage), solid waste management, and traffic congestion",
        "Government schemes: AMRUT (urban rejuvenation), Smart Cities Mission, PM Awas Yojana (Urban), & Swachh Bharat Urban"
    ],
    "road": [
        "Bharatmala Pariyojana: Development of national highways, economic corridors, border roads, & port connectivity links",
        "PMGSY (Gram Sadak Yojana): All-weather road connectivity to eligible unconnected habitations in rural areas",
        "Logistics impact: Golden Quadrilateral (Delhi-Mumbai-Chennai-Kolkata); FASTag toll systems; reducing high logistics costs (~14% of GDP)",
        "Overrun issues: Land acquisition disputes, environmental clearances, utility shifting, and concessionaire debt issues"
    ],
    "railway": [
        "DFCs (Dedicated Freight Corridors): Eastern (Ludhiana-Dankuni) & Western (Dadri-JNPT); decouples freight from passenger lines",
        "Modernization: High-speed rail (Mumbai-Ahmedabad Bullet Train), Vande Bharat trains, and station redevelopment under Amrit Bharat",
        "Operational issues: Cross-subsidization (high freight rates subsidize passenger tickets); safety issues; land acquisition delays",
        "National Rail Plan 2030: Aims to increase share of rail in freight logistics from current 27% to 45%"
    ],
    "waterways": [
        "National Waterways: 111 declared NWs; NW1 (Ganga: Prayagraj-Haldia, 1620km), NW2 (Brahmaputra: Sadiya-Dhubri)",
        "Sagarmala project: Port modernization, port-led industrialization, coastal shipping development, & community development",
        "Challenges: Inadequate draft in rivers due to siltation; lack of terminal infrastructure; environmental impact on river ecosystems",
        "Economic benefits: Water transport is fuel-efficient, environment friendly, & has lower operational costs per ton-km"
    ],
    "pipeline": [
        "Major networks: HBJ gas pipeline, Kandla-Bhatinda oil pipeline, Barauni-Kanpur pipeline, and cross-border gas pipelines",
        "Logistics advantage: Safest, cleanest, and most economical mode for bulk liquids and gases; eliminates tanker road traffic",
        "Infrastructure: High initial capital cost; right of use (RoU) acquisition hurdles; monitoring of leaks & pilferage"
    ],
    "infrastructure": [
        "NIIF (National Investment & Infrastructure Fund): Quasi-sovereign wealth fund; mobilizes long-term institutional capital",
        "PPP models: BOT (Build-Operate-Transfer), HAM (Hybrid Annuity Model), and EPC (Engineering-Procurement-Construction)",
        "Project delays: Average delay of central infrastructure projects exceeds 3 years; land acquisition & environment clearances",
        "National Infrastructure Pipeline (NIP): Target of Rs 111 lakh crore investments across energy, roads, urban, and rail sectors"
    ]
}

# Dynamic Branch Generator based on keyword matching
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # Check if we have exact match keywords in our FACTS database
    matched_facts = []
    matched_key = None
    for key, f_list in FACTS.items():
        if key in fl:
            matched_facts = f_list
            matched_key = key
            break
            
    if matched_facts and len(matched_facts) >= 4:
        # Build an extremely detailed 3-tier mindmap using specific database facts
        return [
            {
                "label": "Core Dimensions & Infrastructure",
                "type": "branch",
                "date": f"{matched_key.upper()} Profile",
                "children": [
                    {
                        "label": "Structural Parameters", "type": "sub", "date": "Foundational Facts", "children": [
                            {"label": matched_facts[0], "type": "leaf"},
                            {"label": matched_facts[1], "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Socio-Economic & Policy Review",
                "type": "branch",
                "date": "Applied Analysis",
                "children": [
                    {
                        "label": "Challenges & Regulations", "type": "sub", "date": "Critical Study", "children": [
                            {"label": matched_facts[2], "type": "leaf"},
                            {"label": matched_facts[3], "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # --- DOMAIN TEMPLATES ---
    
    # 1. Agriculture fallback
    if any(k in fl for k in ['agri', 'crop', 'farm', 'cultivation', 'land-use', 'green-rev']):
        return [
            {
                "label": "Agricultural Systems",
                "type": "branch",
                "date": "Syllabus Core",
                "children": [
                    {
                        "label": "Cropping Patterns", "type": "sub", "date": "Seasons & Types", "children": [
                            {"label": f"Kharif, Rabi, & Zaid seasons; crop requirements (Rice needs >100cm rain, Wheat needs cool climate & 75cm) for {t}", "type": "leaf"},
                            {"label": "Farming types: Subsistence (intensive/extensive), commercial, plantation, and shifting cultivation (Jhum)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Modernization & Tech", "type": "sub", "date": "Inputs", "children": [
                            {"label": f"Green Revolution package: HYV seeds, NPK chemical fertilizers, & tubewell/canal irrigation inputs for {t}", "type": "leaf"},
                            {"label": "IT in agriculture: GIS mapping, remote sensing, AgriStack, & mKisan portals for precision farming", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Policy & Challenges",
                "type": "branch",
                "date": "Sustainability",
                "children": [
                    {
                        "label": "Government Schemes", "type": "sub", "date": "Support Systems", "children": [
                            {"label": f"e-NAM digital market integration; PM-KISAN income support; PM Fasal Bima Yojana crop insurance for {t}", "type": "leaf"},
                            {"label": "Soil Health Cards; PM Krishi Sinchayee Yojana for micro-irrigation (drip & sprinkler systems)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Ecological Issues", "type": "sub", "date": "Degradation", "children": [
                            {"label": "Groundwater depletion from intensive tube-wells; soil salinization due to over-irrigation; NPK imbalances", "type": "leaf"},
                            {"label": "Climate change impacts (monsoon shifts, dry spells), land degradation, & farm indebtedness", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]
        
    # 2. Mineral & Energy fallback
    elif any(k in fl for k in ['mineral', 'resource', 'energy', 'coal', 'oil', 'gas', 'pipeline', 'atomic', 'nuclear', 'power', 'electrification']):
        return [
            {
                "label": "Conventional Resources",
                "type": "branch",
                "date": "Fossil Fuels",
                "children": [
                    {
                        "label": "Coal Fields", "type": "sub", "date": "Solid Energy", "children": [
                            {"label": f"Gondwana coal (98% of reserves, Jharia, Raniganj, low sulphur); Tertiary coal (Lignite in Neyveli TN) for {t}", "type": "leaf"},
                            {"label": "Coal gasification targets (100 MT by 2030) & commercial mining reforms to cut metallurgical imports", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Oil & Gas Networks", "type": "sub", "date": "Hydrocarbons", "children": [
                            {"label": f"Onshore (Digboi, Barmer) & offshore (Mumbai High, KG Basin deepwater gas blocks) distribution for {t}", "type": "leaf"},
                            {"label": "Cross-country pipelines (HBJ) feeding fertilizers; OPEC import dependence (~85% crude vulnerability)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Renewable & Nuclear",
                "type": "branch",
                "date": "Clean Energy",
                "children": [
                    {
                        "label": "Green Energy Mix", "type": "sub", "date": "Transition", "children": [
                            {"label": "Solar parks (Bhadla, Pavagada) & International Solar Alliance; coastal wind farms (Muppandal TN)", "type": "leaf"},
                            {"label": "Small hydro, biomass, geothermal (Puga Valley), & tidal potential (Gulf of Khambhat)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Nuclear Program", "type": "sub", "date": "3-Stage Model", "children": [
                            {"label": f"Stage 1 PHWRs (natural Uranium); Stage 2 FBRs (Plutonium-239); Stage 3 AHWRs (Thorium monazite sands) for {t}", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. Industries fallback
    elif any(k in fl for k in ['industry', 'industrial', 'manufacturing', 'textile', 'steel', 'fertilizer', 'location']):
        return [
            {
                "label": "Heavy Industries",
                "type": "branch",
                "date": "Sectors",
                "children": [
                    {
                        "label": "Iron & Steel", "type": "sub", "date": "Location Factors", "children": [
                            {"label": f"Location factors (weight-losing materials, located near coal/ore fields like Damodar basin) for {t}", "type": "leaf"},
                            {"label": "Major complexes: Jamshedpur (private), Bhilai, Rourkela, Bokaro (public), & Vizag (port-based)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Cotton & Jute", "type": "sub", "date": "Textile Hubs", "children": [
                            {"label": f"Cotton: Dispersed from Gujarat/Mumbai (moist climate) to Tamil Nadu/Coimbatore & Punjab (market) for {t}", "type": "leaf"},
                            {"label": "Jute: Concentrated in Hooghly basin (West Bengal) due to retting water & cheap river transport", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Location & Development",
                "type": "branch",
                "date": "Weber Theory",
                "children": [
                    {
                        "label": "Weber's Theory", "type": "sub", "date": "Material Index", "children": [
                            {"label": f"Material Index (MI): MI > 1 locates at raw material source; MI < 1 locates near market hubs for {t}", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Industrial Regions", "type": "sub", "date": "Major Clusters", "children": [
                            {"label": "Major clusters: Hooghly belt, Mumbai-Pune, Gujarat corridor, Bengaluru-TN, & Gurgaon-Delhi", "type": "leaf"},
                            {"label": "New initiatives: Special Economic Zones (SEZs), MSME clusters, and Make in India corridors", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. Population & Settlements fallback
    elif any(k in fl for k in ['population', 'demographic', 'dividend', 'census', 'growth', 'distribution', 'settlement', 'gender', 'sex-ratio', 'literacy', 'health']):
        return [
            {
                "label": "Demographic Dynamics",
                "type": "branch",
                "date": "Census Data",
                "children": [
                    {
                        "label": "Growth & Density", "type": "sub", "date": "Census 2011", "children": [
                            {"label": f"Census 2011 indicators; growth phases (explosion 1951-81, division 1921); spatial densities of {t}", "type": "leaf"},
                            {"label": "Demographic Dividend: working-age population (15-59) boom; requires skill training & jobs", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Social Indicators", "type": "sub", "date": "Development", "children": [
                            {"label": f"Sex Ratio (943) & declining Child Sex Ratio (919); Beti Bachao Beti Padhao interventions for {t}", "type": "leaf"},
                            {"label": "Literacy disparities, health indicators, and National Population Policy (NPP) 2000 targets", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Settlement Geography",
                "type": "branch",
                "date": "Urbanization",
                "children": [
                    {
                        "label": "Settlement Types", "type": "sub", "date": "Patterns", "children": [
                            {"label": f"Rural: Nucleated (plains), dispersed (hills), hamleted, and linear canal settlements for {t}", "type": "leaf"},
                            {"label": "Urban: Functional classification (admin, industrial, transport, ports) & Class I-VI cities", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Urban Issues", "type": "sub", "date": "Infrastructure", "children": [
                            {"label": f"Urban sprawl, slums, waste management, & Smart Cities infrastructure planning for {t}", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. Transport, Trade & Infrastructure fallback
    elif any(k in fl for k in ['transport', 'waterways', 'port', 'ocean', 'road', 'railway', 'highway', 'infrastructure', 'niif', 'overrun', 'cost']):
        return [
            {
                "label": "Modes of Transport",
                "type": "branch",
                "date": "Logistics",
                "children": [
                    {
                        "label": "Land Transport", "type": "sub", "date": "Roads & Rails", "children": [
                            {"label": f"Highways: Bharatmala Pariyojana; expressways; PM Gram Sadak Yojana for rural road connectivity for {t}", "type": "leaf"},
                            {"label": "Railways: Network modernization & Dedicated Freight Corridors (DFCs) for high-speed cargo transit", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Water & Pipelines", "type": "sub", "date": "Alternative Modes", "children": [
                            {"label": f"Inland Waterways: National Waterways Act (111 NWs; NW1 Ganga, NW2 Brahmaputra); Sagarmala port-led dev for {t}", "type": "leaf"},
                            {"label": "Pipelines for oil & gas transit; reduces overland transport costs & logistics times", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Project Management",
                "type": "branch",
                "date": "Finance & Execution",
                "children": [
                    {
                        "label": "Financing Infrastructure", "type": "sub", "date": "Capital", "children": [
                            {"label": f"NIIF (National Investment & Infrastructure Fund) funding; PPP (Public Private Partnership) models for {t}", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Execution Bottlenecks", "type": "sub", "date": "Delays", "children": [
                            {"label": f"Project bottlenecks: Land acquisition hurdles, environment clearances, & time/cost overruns for {t}", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. Land Degradation
    elif 'land-degradation' in fl:
        return [
            {
                "label": "Land Degradation",
                "type": "branch",
                "date": "Environmental Issue",
                "children": [
                    {
                        "label": "Causes & Impacts", "type": "sub", "date": "Degradation Forces", "children": [
                            {"label": "Causes: Soil erosion, deforestation, overgrazing, shifting cultivation, salinization, and excessive chemical fertilizer use", "type": "leaf"},
                            {"label": "Impacts: Loss of soil fertility, desertification, decline in agricultural productivity, and biodiversity loss", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. Disinvestment of PSUs
    elif 'disinvestment' in fl:
        return [
            {
                "label": "PSU Disinvestment",
                "type": "branch",
                "date": "Reforms & Policy",
                "children": [
                    {
                        "label": "Disinvestment Modes", "type": "sub", "date": "Public Assets", "children": [
                            {"label": "Modes: Minority stake sale, strategic disinvestment (transfer of management control; e.g., Air India), and asset monetization", "type": "leaf"},
                            {"label": "DIPAM: Department of Investment and Public Asset Management supervises all public sector disinvestment policies", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. Engineering Industries
    elif 'engineering-industries' in fl:
        return [
            {
                "label": "Engineering Industries",
                "type": "branch",
                "date": "Heavy & Light",
                "children": [
                    {
                        "label": "Industrial Clusters", "type": "sub", "date": "Manufacturing", "children": [
                            {"label": "Heavy: Machine tools, heavy electricals (BHEL), industrial machinery, automobiles (Pune, Chennai clusters)", "type": "leaf"},
                            {"label": "Light: Precision instruments, medical electronics, consumer durables; critical for manufacturing GDP share", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. Mineral Exploration
    elif 'exploration' in fl:
        return [
            {
                "label": "Mineral Exploration",
                "type": "branch",
                "date": "Surveys & Licences",
                "children": [
                    {
                        "label": "Agencies & Methods", "type": "sub", "date": "Resource Mapping", "children": [
                            {"label": "Geological Survey of India (GSI) & Indian Bureau of Mines (IBM) map and license mineral resource blocks", "type": "leaf"},
                            {"label": "Offshore exploration managed by ONGC and OIL under Hydrocarbon Exploration and Licensing Policy (HELP)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 11. International Trade
    elif 'international-trade' in fl:
        return [
            {
                "label": "International Trade",
                "type": "branch",
                "date": "Trade Profile",
                "children": [
                    {
                        "label": "Balance of Trade", "type": "sub", "date": "Exim Profile", "children": [
                            {"label": "Major exports: Refined petroleum, gems/jewelry, chemicals, pharmaceuticals; imports: Crude oil, gold, electronic goods", "type": "leaf"},
                            {"label": "Trade Balance: Structural trade deficit; managed via foreign trade policy (FTP), free trade agreements (FTAs), and SEZs", "type": "leaf"}
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
        # Fallback
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

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
        # Fallback
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

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

