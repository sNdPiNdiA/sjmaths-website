import os
import re
import json

# Predefined mindmap data for all 38 Chemistry topics to cover ~90% of UPSC syllabus content.
MINDMAPS = {
    "Acids-and-Bases": {
        "label": "Acids and\nBases",
        "type": "root",
        "children": [
            {
                "label": "Key Theories",
                "type": "branch",
                "date": "Definitions",
                "children": [
                    {"label": "Arrhenius Concept", "type": "sub", "date": "Aqueous only", "children": [
                        {"label": "Acids release H+\n(hydronium H3O+) ions", "type": "leaf"},
                        {"label": "Bases release OH-\n(hydroxyl) ions", "type": "leaf"}
                    ]},
                    {"label": "Brønsted-Lowry", "type": "sub", "date": "Proton transfer", "children": [
                        {"label": "Acids: Proton (H+)\ndonors", "type": "leaf"},
                        {"label": "Bases: Proton (H+)\nacceptors", "type": "leaf"},
                        {"label": "Conjugate pairs differ\nby a single proton", "type": "leaf"}
                    ]},
                    {"label": "Lewis Concept", "type": "sub", "date": "Electron transfer", "children": [
                        {"label": "Acids: Electron-pair\nacceptors (e.g. BF3, AlCl3)", "type": "leaf"},
                        {"label": "Bases: Electron-pair\ndonors (e.g. NH3, H2O)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "pH Scale &\nStrength",
                "type": "branch",
                "date": "Quantitative",
                "children": [
                    {"label": "pH Scale", "type": "sub", "date": "Sørensen (0-14)", "children": [
                        {"label": "pH = -log10[H+];\npOH = -log10[OH-]", "type": "leaf"},
                        {"label": "pH + pOH = 14\nat 25°C", "type": "leaf"},
                        {"label": "pH < 7 Acidic;\npH > 7 Basic;\npH = 7 Neutral", "type": "leaf"}
                    ]},
                    {"label": "Electrolytes", "type": "sub", "date": "Ionization", "children": [
                        {"label": "Strong: Fully dissociate\n(HCl, HNO3, NaOH)", "type": "leaf"},
                        {"label": "Weak: Partially dissociate\n(CH3COOH, NH4OH)", "type": "leaf"}
                    ]},
                    {"label": "Buffer Solutions", "type": "sub", "date": "pH resistance", "children": [
                        {"label": "Resist pH change on adding\nsmall acid/base amounts", "type": "leaf"},
                        {"label": "Human blood pH: ~7.4\n(Carbonic acid/bicarbonate)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Daily Life &\nIndustrial Uses",
                "type": "branch",
                "date": "Applications",
                "children": [
                    {"label": "Household Acids", "type": "sub", "date": "Organic", "children": [
                        {"label": "Acetic: Vinegar;\nCitric: Citrus fruits", "type": "leaf"},
                        {"label": "Tartaric: Tamarind;\nLactic: Curd/sour milk", "type": "leaf"},
                        {"label": "Formic: Ant stings;\nOxalic: Tomatoes/ink removal", "type": "leaf"}
                    ]},
                    {"label": "Household Bases", "type": "sub", "date": "Antacids/Soap", "children": [
                        {"label": "Mg(OH)2: Milk of Magnesia\n(neutralizes stomach acid)", "type": "leaf"},
                        {"label": "NaHCO3: Baking soda;\nNa2CO3: Washing soda", "type": "leaf"},
                        {"label": "NaOH: Caustic soda;\nKOH: Soft liquid soaps", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Atom": {
        "label": "The Atom",
        "type": "root",
        "children": [
            {
                "label": "Subatomic\nParticles",
                "type": "branch",
                "date": "Discovery",
                "children": [
                    {"label": "Electrons (e-)", "type": "sub", "date": "J.J. Thomson (1897)", "children": [
                        {"label": "Charge: -1.6 x 10^-19 C\nMass: 9.1 x 10^-31 kg", "type": "leaf"},
                        {"label": "Cathode ray tube\nexperiments", "type": "leaf"}
                    ]},
                    {"label": "Protons (p+)", "type": "sub", "date": "Goldstein/Rutherford", "children": [
                        {"label": "Charge: +1.6 x 10^-19 C\nMass: 1.672 x 10^-27 kg", "type": "leaf"},
                        {"label": "Anode rays / Canal rays\nchannel positive charge", "type": "leaf"}
                    ]},
                    {"label": "Neutrons (n)", "type": "sub", "date": "J. Chadwick (1932)", "children": [
                        {"label": "Charge: 0 (Neutral);\nMass: 1.674 x 10^-27 kg", "type": "leaf"},
                        {"label": "Beryllium bombardment\nwith alpha particles", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Core Nuclear\nConcepts",
                "type": "branch",
                "date": "Classifications",
                "children": [
                    {"label": "Atomic Number (Z)", "type": "sub", "date": "Proton count", "children": [
                        {"label": "Number of protons;\ndefines element identity", "type": "leaf"},
                        {"label": "Equal to electrons\nin a neutral atom", "type": "leaf"}
                    ]},
                    {"label": "Mass Number (A)", "type": "sub", "date": "Protons + Neutrons", "children": [
                        {"label": "Total number of nucleons\nin nucleus", "type": "leaf"},
                        {"label": "A = Z + Neutrons", "type": "leaf"}
                    ]},
                    {"label": "Nuclear Variations", "type": "sub", "date": "Relations", "children": [
                        {"label": "Isotopes: Same Z, Diff A\n(e.g., Protium, Deuterium)", "type": "leaf"},
                        {"label": "Isobars: Same A, Diff Z\n(e.g., Argon-40 & Calcium-40)", "type": "leaf"},
                        {"label": "Isotones: Same Neutrons\n(e.g., C-14, N-15, O-16)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Atomic-Structure": {
        "label": "Atomic\nStructure",
        "type": "root",
        "children": [
            {
                "label": "Atomic Models",
                "type": "branch",
                "date": "Chronology",
                "children": [
                    {"label": "Dalton's Theory", "type": "sub", "date": "1808", "children": [
                        {"label": "Atoms are indivisible,\nindestructible spheres", "type": "leaf"}
                    ]},
                    {"label": "Rutherford Model", "type": "sub", "date": "1911", "children": [
                        {"label": "Alpha particle scattering;\nshows tiny dense nucleus", "type": "leaf"},
                        {"label": "Failed to explain orbit\nstability (Maxwell's theory)", "type": "leaf"}
                    ]},
                    {"label": "Bohr's Orbit Model", "type": "sub", "date": "1913", "children": [
                        {"label": "Electrons orbit in quantized,\nnon-radiating energy levels", "type": "leaf"},
                        {"label": "Angular momentum:\nmvr = nh / 2pi", "type": "leaf"}
                    ]},
                    {"label": "Quantum Model", "type": "sub", "date": "Modern Wave Mech", "children": [
                        {"label": "de Broglie: Dual nature\n(lambda = h/mv)", "type": "leaf"},
                        {"label": "Heisenberg: Uncertainty\n(delta_x * delta_p >= h/4pi)", "type": "leaf"},
                        {"label": "Schrödinger: Wave equation;\norbitals as probability clouds", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Quantum Numbers",
                "type": "branch",
                "date": "Electron Coordinates",
                "children": [
                    {"label": "Principal (n)", "type": "sub", "date": "Energy Shell", "children": [
                        {"label": "n = 1, 2, 3, 4...\n(K, L, M, N shells)", "type": "leaf"},
                        {"label": "Determines size and main\nenergy level of orbital", "type": "leaf"}
                    ]},
                    {"label": "Azimuthal (l)", "type": "sub", "date": "Orbital Shape", "children": [
                        {"label": "l = 0 to (n-1);\ns(0), p(1), d(2), f(3)", "type": "leaf"},
                        {"label": "Defines subshell geometry", "type": "leaf"}
                    ]},
                    {"label": "Magnetic (ml)", "type": "sub", "date": "Orientation", "children": [
                        {"label": "ml = -l to +l;\norbital spatial direction", "type": "leaf"}
                    ]},
                    {"label": "Spin (ms)", "type": "sub", "date": "Electron Spin", "children": [
                        {"label": "ms = +1/2 (up) or\n-1/2 (down) spin direction", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Filling Rules",
                "type": "branch",
                "date": "Configurations",
                "children": [
                    {"label": "Aufbau Principle", "type": "sub", "date": "Energy order", "children": [
                        {"label": "Electrons enter lowest\nenergy orbital first (n+l rule)", "type": "leaf"}
                    ]},
                    {"label": "Pauli Exclusion", "type": "sub", "date": "Spin limit", "children": [
                        {"label": "No two electrons can have\nsame four quantum numbers", "type": "leaf"},
                        {"label": "An orbital holds max 2 e-\nwith opposite spins", "type": "leaf"}
                    ]},
                    {"label": "Hund's Rule", "type": "sub", "date": "Multiplicity", "children": [
                        {"label": "Degenerate orbitals filled\nsingly before pairing up", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Baking-agents": {
        "label": "Baking\nAgents",
        "type": "root",
        "children": [
            {
                "label": "Chemical\nLeaveners",
                "type": "branch",
                "date": "Baking Soda & Powder",
                "children": [
                    {"label": "Baking Soda", "type": "sub", "date": "Pure NaHCO3", "children": [
                        {"label": "Sodium Bicarbonate;\nrequires acid to react", "type": "leaf"},
                        {"label": "Reaction: NaHCO3 + H+\n-> Na+ + H2O + CO2", "type": "leaf"},
                        {"label": "Releases CO2 gas;\nneutralizes acidic batter", "type": "leaf"}
                    ]},
                    {"label": "Baking Powder", "type": "sub", "date": "Combined formula", "children": [
                        {"label": "Contains baking soda,\nacid salt, & starch", "type": "leaf"},
                        {"label": "Acid salt: Cream of tartar\nor sodium aluminum sulfate", "type": "leaf"},
                        {"label": "Starch: Absorbs moisture;\nprevents premature reaction", "type": "leaf"},
                        {"label": "Double-acting: Reacts on\nwetting & during heating", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Biological\nLeaveners",
                "type": "branch",
                "date": "Fermentation",
                "children": [
                    {"label": "Yeast", "type": "sub", "date": "Saccharomyces cerevisiae", "children": [
                        {"label": "Fungi ferments sugars\nto alcohol & CO2", "type": "leaf"},
                        {"label": "C6H12O6 -> 2C2H5OH + 2CO2;\nslower than chemical leavening", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Base": {
        "label": "Bases",
        "type": "root",
        "children": [
            {
                "label": "Properties",
                "type": "branch",
                "date": "Characteristics",
                "children": [
                    {"label": "Physical", "type": "sub", "date": "Senses", "children": [
                        {"label": "Bitter taste;\nslippery or soapy touch", "type": "leaf"},
                        {"label": "Turns red litmus paper blue", "type": "leaf"}
                    ]},
                    {"label": "Chemical", "type": "sub", "date": "Reactivity", "children": [
                        {"label": "Neutralizes acids:\nBase + Acid -> Salt + Water", "type": "leaf"},
                        {"label": "Reacts with metals (Zn, Al)\nto release H2 gas", "type": "leaf"},
                        {"label": "Reacts with non-metal oxides\nto form salts (Ca(OH)2 + CO2)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Classifications",
                "type": "branch",
                "date": "Solubility & Ions",
                "children": [
                    {"label": "Alkalis", "type": "sub", "date": "Soluble Bases", "children": [
                        {"label": "Bases soluble in water;\nall alkalis are bases", "type": "leaf"},
                        {"label": "Not all bases are alkalis\n(e.g. Fe(OH)3 is insoluble)", "type": "leaf"}
                    ]},
                    {"label": "Strength", "type": "sub", "date": "Dissociation", "children": [
                        {"label": "Strong: Fully dissociate\n(NaOH, KOH, Ca(OH)2)", "type": "leaf"},
                        {"label": "Weak: Partially dissociate\n(NH4OH, Mg(OH)2)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Key Uses",
                "type": "branch",
                "date": "Applications",
                "children": [
                    {"label": "Sodium Hydroxide", "type": "sub", "date": "Caustic Soda (NaOH)", "children": [
                        {"label": "Soap, paper, rayon, &\npetroleum refining", "type": "leaf"}
                    ]},
                    {"label": "Calcium Hydroxide", "type": "sub", "date": "Slaked Lime (Ca(OH)2)", "children": [
                        {"label": "Manufacture of bleaching powder;\nneutralizes acidic soil", "type": "leaf"}
                    ]},
                    {"label": "Magnesium Hydroxide", "type": "sub", "date": "Milk of Magnesia", "children": [
                        {"label": "Antacid to neutralize\nstomach acidity", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Bioluminescence": {
        "label": "Biolumi-\nnescence",
        "type": "root",
        "children": [
            {
                "label": "Chemical\nReaction",
                "type": "branch",
                "date": "Mechanism",
                "children": [
                    {"label": "Luciferin", "type": "sub", "date": "Light Emitter", "children": [
                        {"label": "The substrate pigment\nthat oxidizes to emit light", "type": "leaf"}
                    ]},
                    {"label": "Luciferase", "type": "sub", "date": "Catalyst", "children": [
                        {"label": "Enzyme that speeds up\nthe oxidation reaction", "type": "leaf"}
                    ]},
                    {"label": "Reaction Steps", "type": "sub", "date": "Involves ATP", "children": [
                        {"label": "Luciferin + ATP + O2\n-Luciferase-> Oxyluciferin + Light", "type": "leaf"},
                        {"label": "Cold Light: 98% efficiency;\nalmost zero heat generated", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Biological\nFunctions",
                "type": "branch",
                "date": "Evolutionary",
                "children": [
                    {"label": "Survival", "type": "sub", "date": "Adaptations", "children": [
                        {"label": "Defense: Startle predators;\ncamouflage (counterillumination)", "type": "leaf"},
                        {"label": "Offense: Lure prey\n(e.g., Anglerfish lure)", "type": "leaf"},
                        {"label": "Communication: Mating signals\n(e.g., Firefly flashing codes)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Carbon-Allotropes-Hydrocarbon": {
        "label": "Carbon &\nCompounds",
        "type": "root",
        "children": [
            {
                "label": "Allotropes of\nCarbon",
                "type": "branch",
                "date": "Structural Forms",
                "children": [
                    {"label": "Crystalline", "type": "sub", "date": "Definite geometry", "children": [
                        {"label": "Diamond: 3D tetrahedral,\nsp3 hybridized, insulator", "type": "leaf"},
                        {"label": "Graphite: 2D hexagonal layers,\nsp2, conducts electricity", "type": "leaf"},
                        {"label": "Fullerenes: C60 buckyball;\nhollow soccer-ball cage", "type": "leaf"}
                    ]},
                    {"label": "Amorphous", "type": "sub", "date": "No long-range order", "children": [
                        {"label": "Coal, charcoal, coke,\ncarbon black, gas carbon", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Hydrocarbons",
                "type": "branch",
                "date": "Organic Chemistry",
                "children": [
                    {"label": "Saturated", "type": "sub", "date": "Alkanes (CnH2n+2)", "children": [
                        {"label": "Single covalent bonds only;\nundergo substitution reactions", "type": "leaf"}
                    ]},
                    {"label": "Unsaturated", "type": "sub", "date": "Multiple bonds", "children": [
                        {"label": "Alkenes (CnH2n): Double bond;\nAlkynes (CnH2n-2): Triple bond", "type": "leaf"},
                        {"label": "Highly reactive;\nundergo addition reactions", "type": "leaf"}
                    ]},
                    {"label": "Aromatic", "type": "sub", "date": "Benzene ring", "children": [
                        {"label": "Cyclic structures with alternating\ndouble bonds (Huckel's Rule)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Chemical-Explosives": {
        "label": "Chemical\nExplosives",
        "type": "root",
        "children": [
            {
                "label": "Classification",
                "type": "branch",
                "date": "Properties",
                "children": [
                    {"label": "Low Explosives", "type": "sub", "date": "Deflagration", "children": [
                        {"label": "Burn slowly; propellants;\nsubsonic reaction speed", "type": "leaf"},
                        {"label": "Gunpowder (charcoal, sulfur,\nKNO3); Smokeless powder", "type": "leaf"}
                    ]},
                    {"label": "High Explosives", "type": "sub", "date": "Detonation", "children": [
                        {"label": "Supersonic shockwave;\ninstant decomposition", "type": "leaf"},
                        {"label": "Primary: Highly sensitive;\ninitiators (Lead azide, mercury fulminate)", "type": "leaf"},
                        {"label": "Secondary: Less sensitive;\nneed booster (TNT, RDX, PETN)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Common High\nExplosives",
                "type": "branch",
                "date": "Chemical details",
                "children": [
                    {"label": "TNT", "type": "sub", "date": "Trinitrotoluene", "children": [
                        {"label": "Stable, melted & poured;\nmilitary standard benchmark", "type": "leaf"}
                    ]},
                    {"label": "RDX", "type": "sub", "date": "Research Dept Explosive", "children": [
                        {"label": "Cyclonite; highly powerful;\nbase for plastic explosives (C-4)", "type": "leaf"}
                    ]},
                    {"label": "Dynamite", "type": "sub", "date": "Alfred Nobel (1867)", "children": [
                        {"label": "Nitroglycerin absorbed in\nkieselguhr (diatomaceous earth)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Down-Quark-13-charge": {
        "label": "Down Quark\n(-1/3 Charge)",
        "type": "root",
        "children": [
            {
                "label": "Properties",
                "type": "branch",
                "date": "Fundamental Particle",
                "children": [
                    {"label": "Mass & Spin", "type": "sub", "date": "Standard Model", "children": [
                        {"label": "Mass: ~4.7 MeV/c2;\nsecond-lightest quark", "type": "leaf"},
                        {"label": "Spin: 1/2 h-bar (Fermion);\nsubject to Pauli Exclusion", "type": "leaf"}
                    ]},
                    {"label": "Charge", "type": "sub", "date": "Fractional", "children": [
                        {"label": "Electric Charge: -1/3 e;\nbaryon number: +1/3", "type": "leaf"},
                        {"label": "Weak Isospin: -1/2;\nflavour: Down", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Hadronic States",
                "type": "branch",
                "date": "Compositions",
                "children": [
                    {"label": "Baryons", "type": "sub", "date": "3-Quark Hadrons", "children": [
                        {"label": "Proton (uud): Contains\none down quark", "type": "leaf"},
                        {"label": "Neutron (udd): Contains\ntwo down quarks", "type": "leaf"}
                    ]},
                    {"label": "Mesons", "type": "sub", "date": "Quark-Antiquark", "children": [
                        {"label": "Pion (pi-): d and anti-u;\nPion (pi0): u-anti-u & d-anti-d", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Efflorescence": {
        "label": "Efflores-\ncence",
        "type": "root",
        "children": [
            {
                "label": "Mechanism",
                "type": "branch",
                "date": "Dehydration",
                "children": [
                    {"label": "Vapor Pressure", "type": "sub", "date": "Driving Force", "children": [
                        {"label": "Salt vapor pressure >\natmospheric moisture pressure", "type": "leaf"},
                        {"label": "Spontaneous loss of water of\ncrystallization to dry air", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Key Examples",
                "type": "branch",
                "date": "Hydrated Salts",
                "children": [
                    {"label": "Washing Soda", "type": "sub", "date": "Na2CO3.10H2O", "children": [
                        {"label": "Sodium carbonate decahydrate;\nloses 9 water molecules in air", "type": "leaf"},
                        {"label": "Na2CO3.10H2O -> Na2CO3.H2O\n+ 9H2O (monohydrate powder)", "type": "leaf"}
                    ]},
                    {"label": "Glauber's Salt", "type": "sub", "date": "Na2SO4.10H2O", "children": [
                        {"label": "Sodium sulfate decahydrate;\nturns into anhydrous powder", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Fluorescence": {
        "label": "Fluores-\ncence",
        "type": "root",
        "children": [
            {
                "label": "Physical\nMechanism",
                "type": "branch",
                "date": "Jablonski Diagram",
                "children": [
                    {"label": "Absorption", "type": "sub", "date": "Shortwave UV", "children": [
                        {"label": "Electrons absorb high-energy photon\n& transition to excited singlet state", "type": "leaf"}
                    ]},
                    {"label": "Relaxation", "type": "sub", "date": "Internal conversion", "children": [
                        {"label": "Vibrational relaxation loses\nsome energy as heat", "type": "leaf"}
                    ]},
                    {"label": "Emission", "type": "sub", "date": "Longer wavelength", "children": [
                        {"label": "Radiative decay emits photon;\nStokes Shift: Emitted wavelength > absorbed", "type": "leaf"},
                        {"label": "Instantaneous: Occurs within\n10^-8 seconds; stops with source", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Applications",
                "type": "branch",
                "date": "Technological Uses",
                "children": [
                    {"label": "Lighting & Bio", "type": "sub", "date": "Lamps & Markers", "children": [
                        {"label": "Fluorescent tubes: UV hits phosphor\nlining emitting visible light", "type": "leaf"},
                        {"label": "GFP (Green Fluorescent Protein):\nBiological imaging tracer", "type": "leaf"}
                    ]},
                    {"label": "Analytical", "type": "sub", "date": "Dyes & Security", "children": [
                        {"label": "Fluorescein dye tracking;\ncurrency note validation", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Graphite": {
        "label": "Graphite",
        "type": "root",
        "children": [
            {
                "label": "Structure &\nBonding",
                "type": "branch",
                "date": "Planar sheets",
                "children": [
                    {"label": "Hybridization", "type": "sub", "date": "Sp2 Carbon", "children": [
                        {"label": "Each carbon bonded to 3 others\nin hexagonal rings", "type": "leaf"},
                        {"label": "Bond angle: 120°;\ntrigonal planar geometry", "type": "leaf"}
                    ]},
                    {"label": "Interlayer Forces", "type": "sub", "date": "Weak binding", "children": [
                        {"label": "Sheets held by weak van der Waals\nforces; easily slide over each other", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Properties &\nApplications",
                "type": "branch",
                "date": "Unique features",
                "children": [
                    {"label": "Conductivity", "type": "sub", "date": "Electrical & Thermal", "children": [
                        {"label": "Fourth valence electron remains\ndelocalized in pi cloud; conducts", "type": "leaf"}
                    ]},
                    {"label": "Uses", "type": "sub", "date": "Industrial", "children": [
                        {"label": "Solid dry lubricant;\npencil leads (mixed with clay)", "type": "leaf"},
                        {"label": "Electrodes in batteries;\nmoderator in nuclear reactors", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Half-life": {
        "label": "Half-Life\n(t 1/2)",
        "type": "root",
        "children": [
            {
                "label": "Kinetics &\nMathematics",
                "type": "branch",
                "date": "Calculations",
                "children": [
                    {"label": "Radioactive Decay", "type": "sub", "date": "First Order", "children": [
                        {"label": "Decay rate proportional to\nnumber of active nuclei", "type": "leaf"},
                        {"label": "N(t) = N0 * (1/2)^(t / t_1/2);\nexponential decay curve", "type": "leaf"}
                    ]},
                    {"label": "Constant Value", "type": "sub", "date": "Independent", "children": [
                        {"label": "t_1/2 = ln(2) / lambda\n= 0.693 / lambda", "type": "leaf"},
                        {"label": "Independent of pressure,\ntemperature, or chemical state", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Applications",
                "type": "branch",
                "date": "Real-world uses",
                "children": [
                    {"label": "Dating methods", "type": "sub", "date": "Chronology", "children": [
                        {"label": "Carbon-14 (t_1/2 = 5730 yr):\nDating organic archaeological finds", "type": "leaf"},
                        {"label": "Uranium-Lead (t_1/2 = 4.5 billion yr):\nDating Earth's oldest rocks", "type": "leaf"}
                    ]},
                    {"label": "Nuclear Medicine", "type": "sub", "date": "Tracers", "children": [
                        {"label": "Technetium-99m (t_1/2 = 6 hr):\nImaging with minimal radiation dose", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Halogen-Family": {
        "label": "Halogens\n(Group 17)",
        "type": "root",
        "children": [
            {
                "label": "Elements &\nStates",
                "type": "branch",
                "date": "Group Trends",
                "children": [
                    {"label": "Physical States", "type": "sub", "date": "Gradation", "children": [
                        {"label": "F2 (pale yellow gas);\nCl2 (greenish-yellow gas)", "type": "leaf"},
                        {"label": "Br2 (red-brown volatile liquid);\nI2 (shiny violet solid)", "type": "leaf"}
                    ]},
                    {"label": "Electronic", "type": "sub", "date": "ns2 np5", "children": [
                        {"label": "7 valence electrons;\nvalency of 1 (form X- halides)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Chemical\nProperties",
                "type": "branch",
                "date": "Reactivity",
                "children": [
                    {"label": "Electronegativity", "type": "sub", "date": "F is highest", "children": [
                        {"label": "Fluorine is most electronegative\nelement in periodic table", "type": "leaf"}
                    ]},
                    {"label": "Oxidizing Power", "type": "sub", "date": "F2 > Cl2 > Br2 > I2", "children": [
                        {"label": "Fluorine oxidizes water to\noxygen gas spontaneously", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Key Compounds",
                "type": "branch",
                "date": "Applications",
                "children": [
                    {"label": "Uses", "type": "sub", "date": "Industrial", "children": [
                        {"label": "Chlorine: Disinfectant, PVC;\nFluorine: Teflon, tooth protection", "type": "leaf"},
                        {"label": "Silver bromide (AgBr):\nUsed in photographic film emulsions", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Isotopes": {
        "label": "Isotopes",
        "type": "root",
        "children": [
            {
                "label": "Nuclear Concept",
                "type": "branch",
                "date": "Atomic Anatomy",
                "children": [
                    {"label": "Definition", "type": "sub", "date": "Same Z, Diff A", "children": [
                        {"label": "Same atomic number Z (protons);\nsame chemical properties", "type": "leaf"},
                        {"label": "Different mass number A (neutrons);\ndifferent physical properties", "type": "leaf"}
                    ]},
                    {"label": "Hydrogen", "type": "sub", "date": "Examples", "children": [
                        {"label": "Protium (1H): 1p, 0n;\nDeuterium (2H/D): 1p, 1n", "type": "leaf"},
                        {"label": "Tritium (3H/T): 1p, 2n\n(radioactive beta emitter)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Practical Uses",
                "type": "branch",
                "date": "Industrial & Medical",
                "children": [
                    {"label": "Energy & Fuel", "type": "sub", "date": "Nuclear", "children": [
                        {"label": "Uranium-235: Fissile fuel;\nDeuterium oxide (D2O): Heavy water moderator", "type": "leaf"}
                    ]},
                    {"label": "Medicine", "type": "sub", "date": "Radiotherapy", "children": [
                        {"label": "Cobalt-60: Cancer radiation therapy;\nIodine-131: Goitre & thyroid cancer", "type": "leaf"}
                    ]},
                    {"label": "Industry", "type": "sub", "date": "Tracing", "children": [
                        {"label": "Carbon-14: Organic dating;\nCobalt-60: Weld inspection", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Luminescence": {
        "label": "Lumines-\ncence",
        "type": "root",
        "children": [
            {
                "label": "Mechanism",
                "type": "branch",
                "date": "Emission of Light",
                "children": [
                    {"label": "Definition", "type": "sub", "date": "Cold Light", "children": [
                        {"label": "Light emission not caused by\nheating (unlike incandescence)", "type": "leaf"}
                    ]},
                    {"label": "Energy Change", "type": "sub", "date": "Electron decay", "children": [
                        {"label": "Electrons absorb energy,\nexcited state -> ground state emits photon", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Types",
                "type": "branch",
                "date": "Excitation Source",
                "children": [
                    {"label": "Photoluminescence", "type": "sub", "date": "Light absorbed", "children": [
                        {"label": "Fluorescence: Nanosecond emission;\nPhosphorescence: Slow triplet emission", "type": "leaf"}
                    ]},
                    {"label": "Chemiluminescence", "type": "sub", "date": "Chemical energy", "children": [
                        {"label": "Glowsticks: Hydrogen peroxide\nreaction excites dye molecule", "type": "leaf"},
                        {"label": "Bioluminescence: Biochemical\n(fireflies, dinoflagellates)", "type": "leaf"}
                    ]},
                    {"label": "Electroluminescence", "type": "sub", "date": "Electric field", "children": [
                        {"label": "LEDs: Recombination of\nelectrons and holes in semiconductor", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Matter": {
        "label": "Matter",
        "type": "root",
        "children": [
            {
                "label": "States of Matter",
                "type": "branch",
                "date": "Physical Forms",
                "children": [
                    {"label": "Solid", "type": "sub", "date": "Rigid", "children": [
                        {"label": "Definite shape and volume;\nleast particle motion", "type": "leaf"}
                    ]},
                    {"label": "Liquid", "type": "sub", "date": "Fluid", "children": [
                        {"label": "Definite volume, shape of container;\nmoderate particle packing", "type": "leaf"}
                    ]},
                    {"label": "Gas", "type": "sub", "date": "Compressible", "children": [
                        {"label": "No definite shape or volume;\nmaximum kinetic energy", "type": "leaf"}
                    ]},
                    {"label": "Plasma", "type": "sub", "date": "Ionized Gas", "children": [
                        {"label": "High temperature, positive ions\nand free electrons, conducts", "type": "leaf"}
                    ]},
                    {"label": "Bose-Einstein", "type": "sub", "date": "BEC (Superatom)", "children": [
                        {"label": "Near absolute zero (-273.15°C);\natoms merge into single quantum wave", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Classification",
                "type": "branch",
                "date": "Chemical Composition",
                "children": [
                    {"label": "Pure Substances", "type": "sub", "date": "Constant properties", "children": [
                        {"label": "Elements: One atom type (O2, Au);\nCompounds: Bound elements (H2O, NaCl)", "type": "leaf"}
                    ]},
                    {"label": "Mixtures", "type": "sub", "date": "Variable ratio", "children": [
                        {"label": "Homogeneous: Uniform (alloys, saltwater);\nHeterogeneous: Non-uniform (colloids, soil)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Metal-and-Non-Metals": {
        "label": "Metals &\nNon-Metals",
        "type": "root",
        "children": [
            {
                "label": "Metals",
                "type": "branch",
                "date": "Electropositive Elements",
                "children": [
                    {"label": "Physical Properties", "type": "sub", "date": "Ductile/Lustrous", "children": [
                        {"label": "High electrical & thermal conductivity;\nmalleable (sheets) & ductile (wires)", "type": "leaf"},
                        {"label": "Mercury: Liquid at room temp;\nSodium/Potassium: Soft, cut with knife", "type": "leaf"}
                    ]},
                    {"label": "Chemical", "type": "sub", "date": "Lose electrons", "children": [
                        {"label": "Form basic oxides (e.g. Na2O);\nreact with dilute acid to evolve H2", "type": "leaf"},
                        {"label": "Rusting: Fe + O2 + H2O\n-> hydrated Fe2O3", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Non-Metals",
                "type": "branch",
                "date": "Electronegative Elements",
                "children": [
                    {"label": "Physical Properties", "type": "sub", "date": "Insulators/Brittle", "children": [
                        {"label": "Poor conductors (graphite is exception);\nnon-malleable, brittle solids", "type": "leaf"},
                        {"label": "Bromine: Only liquid non-metal;\nDiamond: Hardest natural substance", "type": "leaf"}
                    ]},
                    {"label": "Chemical", "type": "sub", "date": "Gain/Share electrons", "children": [
                        {"label": "Form acidic or neutral oxides\n(CO2, SO2; H2O, CO is neutral)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Metalloids",
                "type": "branch",
                "date": "Semiconductors",
                "children": [
                    {"label": "Silicon & Germanium", "type": "sub", "date": "Metalloid group", "children": [
                        {"label": "Properties of both metals &\nnon-metals; electronic chips", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Neutrinos": {
        "label": "Neutrinos",
        "type": "root",
        "children": [
            {
                "label": "Properties",
                "type": "branch",
                "date": "Leptons",
                "children": [
                    {"label": "Mass & Charge", "type": "sub", "date": "Subatomic", "children": [
                        {"label": "Charge: 0 (Neutral);\nMass: Nearly zero, > 0", "type": "leaf"},
                        {"label": "Spin: 1/2 h-bar (Fermion)", "type": "leaf"}
                    ]},
                    {"label": "Interactions", "type": "sub", "date": "Weak Force", "children": [
                        {"label": "Interact only via weak force\nand gravity; hard to detect", "type": "leaf"},
                        {"label": "Pass through the Earth\nwithout any deflection", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Flavors & Oscillations",
                "type": "branch",
                "date": "Quantum States",
                "children": [
                    {"label": "Three Flavors", "type": "sub", "date": "Generations", "children": [
                        {"label": "Electron neutrino (v_e);\nMuon neutrino (v_mu)", "type": "leaf"},
                        {"label": "Tau neutrino (v_tau)", "type": "leaf"}
                    ]},
                    {"label": "Oscillations", "type": "sub", "date": "Pontecorvo", "children": [
                        {"label": "Change flavors as they travel;\nproves neutrinos possess mass", "type": "leaf"},
                        {"label": "Solves Solar Neutrino Problem\n(observed vs predicted flux)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Nuclear-fusion-Nuclear-fission": {
        "label": "Nuclear\nReactions",
        "type": "root",
        "children": [
            {
                "label": "Nuclear Fission",
                "type": "branch",
                "date": "Splitting Heavy Nuclei",
                "children": [
                    {"label": "Mechanism", "type": "sub", "date": "Neutron induced", "children": [
                        {"label": "235_92U + 1_0n -> 141_56Ba\n+ 92_36Kr + 3 1_0n + Energy", "type": "leaf"},
                        {"label": "Mass defect converts to energy\nvia E = mc^2", "type": "leaf"}
                    ]},
                    {"label": "Reactors", "type": "sub", "date": "Controlled", "children": [
                        {"label": "Moderator (D2O/Graphite): Slows neutrons;\nControl Rods (Cd/B): Absorb neutrons", "type": "leaf"},
                        {"label": "Coolant (Water/Liquid Sodium):\nTransfers thermal energy to turbine", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Nuclear Fusion",
                "type": "branch",
                "date": "Fusing Light Nuclei",
                "children": [
                    {"label": "Mechanism", "type": "sub", "date": "Thermonuclear", "children": [
                        {"label": "2_1H (Deuterium) + 3_1H (Tritium)\n-> 4_2He + 1_0n + 17.6 MeV", "type": "leaf"},
                        {"label": "Requires high temp (10^7 K)\nto overcome Coulomb repulsion", "type": "leaf"}
                    ]},
                    {"label": "Occurrences", "type": "sub", "date": "Stellar", "children": [
                        {"label": "Sun's core energy generator;\nHydrogen bomb (triggered by fission)", "type": "leaf"},
                        {"label": "Tokamaks/ITER: Magnetic confinement\nto achieve controlled fusion on Earth", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Nuclear-fusion-Nuclear-fission-CosmicGeneral-Chemistry": {
        "label": "Cosmic Nuclear\nChemistry",
        "type": "root",
        "children": [
            {
                "label": "Stellar Engines",
                "type": "branch",
                "date": "Star Fusion",
                "children": [
                    {"label": "Proton-Proton Chain", "type": "sub", "date": "Sun-like stars", "children": [
                        {"label": "Main fusion reaction in Sun;\nconverts hydrogen to helium", "type": "leaf"}
                    ]},
                    {"label": "CNO Cycle", "type": "sub", "date": "Hot stars", "children": [
                        {"label": "Carbon-Nitrogen-Oxygen cycle;\nfuels stars heavier than Sun", "type": "leaf"}
                    ]},
                    {"label": "Triple-Alpha", "type": "sub", "date": "Red Giants", "children": [
                        {"label": "Fuses three helium nuclei\nto create carbon", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Nucleosynthesis",
                "type": "branch",
                "date": "Element Origin",
                "children": [
                    {"label": "Primordial", "type": "sub", "date": "Big Bang", "children": [
                        {"label": "Created H, He, Li;\nfirst 3 minutes of universe", "type": "leaf"}
                    ]},
                    {"label": "Stellar & Supernova", "type": "sub", "date": "Heavy Elements", "children": [
                        {"label": "S-process (slow neutron capture)\nin asymptotic giant stars", "type": "leaf"},
                        {"label": "R-process (rapid capture) in\nsupernovae/neutron star mergers", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Ozone": {
        "label": "Ozone\n(O3)",
        "type": "root",
        "children": [
            {
                "label": "Atmospheric\nDistribution",
                "type": "branch",
                "date": "Two Layers",
                "children": [
                    {"label": "Stratospheric", "type": "sub", "date": "Good Ozone", "children": [
                        {"label": "Ozone layer (15-30 km);\nabsorbs UV-B & UV-C radiation", "type": "leaf"},
                        {"label": "Protects life from skin cancer\nand genetic damage", "type": "leaf"}
                    ]},
                    {"label": "Tropospheric", "type": "sub", "date": "Bad Ozone", "children": [
                        {"label": "Ground level pollutant;\ncreates photochemical smog", "type": "leaf"},
                        {"label": "Formed by NOx + VOCs + sunlight;\nharmful to lungs and crops", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Depletion & Policy",
                "type": "branch",
                "date": "Ozone Hole",
                "children": [
                    {"label": "Chemistry", "type": "sub", "date": "Chlorine Catalysis", "children": [
                        {"label": "CFCl3 -UV-> CFCl2 + Cl;\nCl + O3 -> ClO + O2", "type": "leaf"},
                        {"label": "Single Cl radical can destroy\n100,000 ozone molecules", "type": "leaf"},
                        {"label": "Polar Stratospheric Clouds (PSCs):\nProvide surface for chlorine activation", "type": "leaf"}
                    ]},
                    {"label": "Treaties", "type": "sub", "date": "Global accords", "children": [
                        {"label": "Vienna Convention (1985):\nFramework for ozone protection", "type": "leaf"},
                        {"label": "Montreal Protocol (1987):\nPhasing out CFCs/halons", "type": "leaf"},
                        {"label": "Kigali Amendment (2016):\nPhasing down HFCs (greenhouse gases)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Periodic-Table": {
        "label": "Periodic\nTable",
        "type": "root",
        "children": [
            {
                "label": "Layout & Laws",
                "type": "branch",
                "date": "Organization",
                "children": [
                    {"label": "Mendeleev's Law", "type": "sub", "date": "1869", "children": [
                        {"label": "Properties are periodic function\nof atomic masses", "type": "leaf"},
                        {"label": "Left gaps for undiscovered elements\n(e.g., Eka-boron, Eka-silicon)", "type": "leaf"}
                    ]},
                    {"label": "Modern Periodic Law", "type": "sub", "date": "Moseley", "children": [
                        {"label": "Properties are periodic function\nof atomic numbers (Z)", "type": "leaf"}
                    ]},
                    {"label": "Grid Setup", "type": "sub", "date": "18 Groups, 7 Periods", "children": [
                        {"label": "s-block (1-2), p-block (13-18),\nd-block (3-12), f-block (lanthanides/actinides)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Periodic Trends",
                "type": "branch",
                "date": "Patterns",
                "children": [
                    {"label": "Atomic Radius", "type": "sub", "date": "Size", "children": [
                        {"label": "Decreases left to right\n(increasing nuclear charge)", "type": "leaf"},
                        {"label": "Increases top to bottom\n(new shells added)", "type": "leaf"}
                    ]},
                    {"label": "Ionization Energy", "type": "sub", "date": "Removing electron", "children": [
                        {"label": "Increases left to right;\ndecreases top to bottom", "type": "leaf"}
                    ]},
                    {"label": "Electronegativity", "type": "sub", "date": "Attracting pair", "children": [
                        {"label": "Increases left to right;\ndecreases top to bottom (F is max)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorescence": {
        "label": "Phosphores-\ncence",
        "type": "root",
        "children": [
            {
                "label": "Mechanism",
                "type": "branch",
                "date": "Triplet State Transition",
                "children": [
                    {"label": "Excitation", "type": "sub", "date": "Singlet State", "children": [
                        {"label": "Electrons absorb photon to enter\nexcited singlet state (S1)", "type": "leaf"}
                    ]},
                    {"label": "Spin Flip", "type": "sub", "date": "Intersystem Crossing", "children": [
                        {"label": "Non-radiative transition from\nS1 to excited triplet state (T1)", "type": "leaf"},
                        {"label": "Electron spins become parallel;\nT1 is lower energy than S1", "type": "leaf"}
                    ]},
                    {"label": "Delayed Emission", "type": "sub", "date": "Glow in the dark", "children": [
                        {"label": "T1 -> S0 transition is spin-forbidden;\noccurs very slowly (milliseconds to hours)", "type": "leaf"},
                        {"label": "Glow persists after light\nsource is turned off", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Applications",
                "type": "branch",
                "date": "Technological Uses",
                "children": [
                    {"label": "Glow products", "type": "sub", "date": "Materials", "children": [
                        {"label": "Zinc sulfide & strontium aluminate\nused in dials, safety signs, toys", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorous-Black-P": {
        "label": "Black\nPhosphorus",
        "type": "root",
        "children": [
            {
                "label": "Synthesis & Types",
                "type": "branch",
                "date": "Thermodynamics",
                "children": [
                    {"label": "Preparation", "type": "sub", "date": "High Pressure", "children": [
                        {"label": "Heating white phosphorus at 473 K\nunder high pressure (12,000 atm)", "type": "leaf"}
                    ]},
                    {"label": "Forms", "type": "sub", "date": "Alpha & Beta", "children": [
                        {"label": "Alpha-black: Sublimes in air;\nBeta-black: Does not burn in air", "type": "leaf"}
                    ]},
                    {"label": "Stability", "type": "sub", "date": "Most stable", "children": [
                        {"label": "Thermodynamically most stable\nallotrope of phosphorus", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Structure",
                "type": "branch",
                "date": "2D Sheets",
                "children": [
                    {"label": "Phosphorene", "type": "sub", "date": "Layered layout", "children": [
                        {"label": "Puckered hexagonal layers;\nhas bandgap, unlike graphene", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorous-Black-P-good-conductor": {
        "label": "Black P\nConductor",
        "type": "root",
        "children": [
            {
                "label": "Conductivity",
                "type": "branch",
                "date": "Electrical properties",
                "children": [
                    {"label": "Semiconductor", "type": "sub", "date": "Band Gap", "children": [
                        {"label": "Only allotrope of P that\nconducts electricity", "type": "leaf"},
                        {"label": "Direct bandgap varies with layer count;\nhighly useful in transistors", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Structural Base",
                "type": "branch",
                "date": "Anisotropy",
                "children": [
                    {"label": "Puckered lattices", "type": "sub", "date": "Directions", "children": [
                        {"label": "Electrical conductivity differs\nalong armchair vs zigzag directions", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorous-Red-P": {
        "label": "Red\nPhosphorus",
        "type": "root",
        "children": [
            {
                "label": "Structure &\nPreparation",
                "type": "branch",
                "date": "Polymeric Allotrope",
                "children": [
                    {"label": "Synthesis", "type": "sub", "date": "From White P", "children": [
                        {"label": "Heating white phosphorus at 573 K\nin inert atmosphere for several days", "type": "leaf"}
                    ]},
                    {"label": "Polymer Chain", "type": "sub", "date": "Linked P4", "children": [
                        {"label": "Polymeric structure; chains of\nlinked P4 tetrahedra", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Properties",
                "type": "branch",
                "date": "Stability & Safety",
                "children": [
                    {"label": "Reactivity", "type": "sub", "date": "Stable", "children": [
                        {"label": "Iron grey luster; odorless;\nnon-toxic (unlike white P)", "type": "leaf"},
                        {"label": "Does not catch fire in air at\nroom temp; ignition temp: 533 K", "type": "leaf"},
                        {"label": "Does not exhibit chemiluminescence", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorous-Red-P-used-in-matchstick": {
        "label": "Red P in\nMatchsticks",
        "type": "root",
        "children": [
            {
                "label": "Matchstick Chemistry",
                "type": "branch",
                "date": "Friction & Ignition",
                "children": [
                    {"label": "Friction Strike", "type": "sub", "date": "Reaction start", "children": [
                        {"label": "Match head has potassium chlorate (KClO3)\n& antimony trisulfide (Sb2S3)", "type": "leaf"},
                        {"label": "Strike surface has red P, glass\npowder, & binder", "type": "leaf"}
                    ]},
                    {"label": "Conversion", "type": "sub", "date": "Initiation", "children": [
                        {"label": "Striking converts some red P\nto white P via friction heat", "type": "leaf"},
                        {"label": "White P ignites KClO3,\nsetting fire to Sb2S3 fuel", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorous-White-P": {
        "label": "White\nPhosphorus",
        "type": "root",
        "children": [
            {
                "label": "Structure &\nReactivity",
                "type": "branch",
                "date": "Monomeric P4",
                "children": [
                    {"label": "Discrete P4", "type": "sub", "date": "Tetrahedral", "children": [
                        {"label": "P4 geometry; 60° bond angles;\nhigh angular strain causes reactivity", "type": "leaf"}
                    ]},
                    {"label": "Stability", "type": "sub", "date": "Very unstable", "children": [
                        {"label": "Ignites spontaneously in air at\n303 K; stored under water", "type": "leaf"},
                        {"label": "Highly toxic; garlic-like odor;\nexhibits glow in dark (chemiluminescence)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Phosphorous-White-P-used-in-matchstick": {
        "label": "White P &\nMatches",
        "type": "root",
        "children": [
            {
                "label": "Historical Matches",
                "type": "branch",
                "date": "Lucifers",
                "children": [
                    {"label": "White P heads", "type": "sub", "date": "Strike anywhere", "children": [
                        {"label": "White P mixed directly on match head;\ncould ignite on any rough surface", "type": "leaf"}
                    ]},
                    {"label": "Health Hazards", "type": "sub", "date": "Phossy Jaw", "children": [
                        {"label": "Match workers developed phosphorus necrosis;\ndestroyed jawbones, highly toxic", "type": "leaf"},
                        {"label": "Banned globally in 1906\n(Bern Convention)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Plasma": {
        "label": "Plasma",
        "type": "root",
        "children": [
            {
                "label": "Definition &\nProperties",
                "type": "branch",
                "date": "4th State of Matter",
                "children": [
                    {"label": "Ionization", "type": "sub", "date": "Charged gas", "children": [
                        {"label": "Gas heated until atoms lose\nelectrons, forming ions & e-", "type": "leaf"}
                    ]},
                    {"label": "Behavior", "type": "sub", "date": "Electromagnetic", "children": [
                        {"label": "Good electrical conductor;\nresponds strongly to magnetic fields", "type": "leaf"},
                        {"label": "Exhibits collective behavior\n(waves, light emission)", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Sources & Uses",
                "type": "branch",
                "date": "Occurrences",
                "children": [
                    {"label": "Natural", "type": "sub", "date": "99% of visible universe", "children": [
                        {"label": "Sun and stars; lightning;\nionosphere; auroras", "type": "leaf"}
                    ]},
                    {"label": "Artificial", "type": "sub", "date": "Technology", "children": [
                        {"label": "Fluorescent bulbs; neon signs;\nfusion test reactors (Tokamaks)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Quarks-and-their-Types": {
        "label": "Quarks",
        "type": "root",
        "children": [
            {
                "label": "Flavors & Properties",
                "type": "branch",
                "date": "Elementary Particles",
                "children": [
                    {"label": "Generations", "type": "sub", "date": "6 flavors", "children": [
                        {"label": "Gen 1: Up (+2/3e) & Down (-1/3e);\nmakeup all stable matter", "type": "leaf"},
                        {"label": "Gen 2: Charm (+2/3e) & Strange (-1/3e)", "type": "leaf"},
                        {"label": "Gen 3: Top (+2/3e) & Bottom (-1/3e)", "type": "leaf"}
                    ]},
                    {"label": "Color Charge", "type": "sub", "date": "Strong interaction", "children": [
                        {"label": "Quarks carry color charge:\nRed, Green, Blue", "type": "leaf"},
                        {"label": "Strong force mediated by gluons", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Confinement",
                "type": "branch",
                "date": "Hadrons",
                "children": [
                    {"label": "Asymptotic Freedom", "type": "sub", "date": "Bound states", "children": [
                        {"label": "Quarks cannot be isolated;\nforce increases with distance", "type": "leaf"},
                        {"label": "Hadrons: Baryons (3q: Proton/Neutron);\nMesons (q-anti-q: Pions)", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Radioactivity-AlphaBetaGamma-decay": {
        "label": "Radioactive\nDecay",
        "type": "root",
        "children": [
            {
                "label": "Alpha (a) Decay",
                "type": "branch",
                "date": "Helium nucleus emission",
                "children": [
                    {"label": "Reaction", "type": "sub", "date": "4_2He particle", "children": [
                        {"label": "A decreases by 4, Z decreases by 2;\ne.g. U-238 -> Th-234 + Alpha", "type": "leaf"}
                    ]},
                    {"label": "Properties", "type": "sub", "date": "Highly ionizing", "children": [
                        {"label": "High mass, high ionizing power;\nstopped by a sheet of paper", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Beta (b) Decay",
                "type": "branch",
                "date": "Electron/Positron release",
                "children": [
                    {"label": "Types", "type": "sub", "date": "Beta-minus & plus", "children": [
                        {"label": "Beta-minus: n -> p + e- + antineutrino;\nZ increases by 1", "type": "leaf"},
                        {"label": "Beta-plus: p -> n + e+ + neutrino;\nZ decreases by 1", "type": "leaf"}
                    ]},
                    {"label": "Properties", "type": "sub", "date": "Moderate", "children": [
                        {"label": "Stopped by aluminum foil;\nmoderate ionizing power", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Gamma (g) Decay",
                "type": "branch",
                "date": "Photon emission",
                "children": [
                    {"label": "Mechanism", "type": "sub", "date": "Electromagnetic", "children": [
                        {"label": "Excited nucleus relaxes to ground state;\nemits high-energy gamma photon", "type": "leaf"},
                        {"label": "No change in Z or A", "type": "leaf"}
                    ]},
                    {"label": "Properties", "type": "sub", "date": "Highly penetrating", "children": [
                        {"label": "Lowest ionizing power, highest penetration;\nrequires thick lead or concrete to block", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Rare-Earth-Elements-and-Applications": {
        "label": "Rare Earth\nElements",
        "type": "root",
        "children": [
            {
                "label": "Classification",
                "type": "branch",
                "date": "Group 3 & Lanthanides",
                "children": [
                    {"label": "The 17 Metals", "type": "sub", "date": "List", "children": [
                        {"label": "15 Lanthanides (Z=57 to 71: La to Lu)", "type": "leaf"},
                        {"label": "Scandium (Sc) & Yttrium (Y) (similar chemistry)", "type": "leaf"}
                    ]},
                    {"label": "Abundance", "type": "sub", "date": "Not actually rare", "children": [
                        {"label": "Common in crust, but difficult to find\nin economically extractable concentrations", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Strategic Applications",
                "type": "branch",
                "date": "Technology Drivers",
                "children": [
                    {"label": "Modern Tech", "type": "sub", "date": "Electronics & Defense", "children": [
                        {"label": "Neodymium (Nd): Super-strong magnets\nfor hard drives and EV motors", "type": "leaf"},
                        {"label": "Europium (Eu): Red phosphors in LEDs;\nCerium (Ce): Catalytic converters", "type": "leaf"}
                    ]},
                    {"label": "Geopolitics", "type": "sub", "date": "Monopoly", "children": [
                        {"label": "China controls >70% of production;\ncritical risk for global supply chains", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Soaps-and-Detergents-chemistry-of-Surfactants": {
        "label": "Soaps &\nDetergents",
        "type": "root",
        "children": [
            {
                "label": "Soaps",
                "type": "branch",
                "date": "Natural Fatty Salts",
                "children": [
                    {"label": "Saponification", "type": "sub", "date": "Preparation", "children": [
                        {"label": "Fat/Oil + NaOH -> Glycerol + Soap;\nSodium/Potassium salts of long fatty acids", "type": "leaf"}
                    ]},
                    {"label": "Hard Water Issue", "type": "sub", "date": "Scum formation", "children": [
                        {"label": "React with Ca2+/Mg2+ to form\ninsoluble scum; wastes soap", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Detergents",
                "type": "branch",
                "date": "Synthetic Surfactants",
                "children": [
                    {"label": "Composition", "type": "sub", "date": "Hydrocarbon chains", "children": [
                        {"label": "Sodium alkylbenzene sulfonates;\ndo not form scum in hard water", "type": "leaf"}
                    ]},
                    {"label": "Eco Impact", "type": "sub", "date": "Biodegradability", "children": [
                        {"label": "Branched chain detergents resist bacteria;\ncause water pollution & foaming", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Cleansing Action",
                "type": "branch",
                "date": "Micelle formation",
                "children": [
                    {"label": "Dual Nature", "type": "sub", "date": "Surfactant molecule", "children": [
                        {"label": "Hydrophobic tail (hydrocarbon) binds dirt;\nHydrophilic head (polar) binds water", "type": "leaf"},
                        {"label": "Micelles trap oil at center;\nwashed away during rinsing", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "The-Noble-Gases": {
        "label": "Noble Gases\n(Group 18)",
        "type": "root",
        "children": [
            {
                "label": "Group Members &\nProperties",
                "type": "branch",
                "date": "Aerogens",
                "children": [
                    {"label": "Elements", "type": "sub", "date": "Inert", "children": [
                        {"label": "Helium, Neon, Argon,\nKrypton, Xenon, Radon (radioactive)", "type": "leaf"}
                    ]},
                    {"label": "Chemical Inertness", "type": "sub", "date": "Stable configuration", "children": [
                        {"label": "ns2 np6 octet (He is 1s2);\nvery high ionization energies", "type": "leaf"},
                        {"label": "Monoatomic, colorless, odorless gases", "type": "leaf"}
                    ]},
                    {"label": "Exceptions", "type": "sub", "date": "Xenon Chemistry", "children": [
                        {"label": "Xenon reacts with highly electronegative\nF & O to form XeF2, XeF4, XeO3", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Applications",
                "type": "branch",
                "date": "Industrial Uses",
                "children": [
                    {"label": "Helium (He)", "type": "sub", "date": "Cryogenics", "children": [
                        {"label": "Liquid He: Coolant for MRI superconducting\nmagnets; non-flammable balloon gas", "type": "leaf"}
                    ]},
                    {"label": "Neon & Argon", "type": "sub", "date": "Commercial", "children": [
                        {"label": "Neon: Glow signs; Argon: Inert filling\nin incandescent bulbs & metallurgy", "type": "leaf"}
                    ]},
                    {"label": "Radon (Rn)", "type": "sub", "date": "Cancer therapy", "children": [
                        {"label": "Used in radiotherapy for cancer treatment", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Types-of-Acids-Organic-Acid-Formic-acid-Acetic-acid-Inorganic-Acid": {
        "label": "Types of\nAcids",
        "type": "root",
        "children": [
            {
                "label": "Organic Acids",
                "type": "branch",
                "date": "Carbon-Containing",
                "children": [
                    {"label": "Characteristics", "type": "sub", "date": "Weak Acids", "children": [
                        {"label": "Derived from plant/animal matter;\npartially ionize in water", "type": "leaf"}
                    ]},
                    {"label": "Common Examples", "type": "sub", "date": "Sources", "children": [
                        {"label": "Formic Acid (Methanoic): Ant stings;\nAcetic Acid (Ethanoic): Vinegar (5-8%)", "type": "leaf"},
                        {"label": "Citric Acid: Oranges/lemons;\nLactic Acid: Sour milk/curd", "type": "leaf"},
                        {"label": "Tartaric Acid: Tamarind/grapes;\nOxalic Acid: Tomato/rust removal", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Inorganic Acids",
                "type": "branch",
                "date": "Mineral Acids",
                "children": [
                    {"label": "Characteristics", "type": "sub", "date": "Strong Acids", "children": [
                        {"label": "Derived from minerals; fully dissociate\nin water (highly corrosive)", "type": "leaf"}
                    ]},
                    {"label": "Common Examples", "type": "sub", "date": "Mineral base", "children": [
                        {"label": "Hydrochloric Acid (HCl): Gastric juice;\nSulphuric Acid (H2SO4): Battery acid, industrial base", "type": "leaf"},
                        {"label": "Nitric Acid (HNO3): Explosives, fertilizers;\nCarbonic Acid (H2CO3): Weak mineral acid in soda", "type": "leaf"}
                    ]}
                ]
            }
        ]
    },
    "Up-Quark-23-charge": {
        "label": "Up Quark\n(+2/3 Charge)",
        "type": "root",
        "children": [
            {
                "label": "Properties",
                "type": "branch",
                "date": "Elementary fermion",
                "children": [
                    {"label": "Mass & Spin", "type": "sub", "date": "Standard Model", "children": [
                        {"label": "Mass: ~2.2 MeV/c2;\nlightest of all quarks", "type": "leaf"},
                        {"label": "Spin: 1/2 h-bar (Fermion)", "type": "leaf"}
                    ]},
                    {"label": "Charge", "type": "sub", "date": "Fractional", "children": [
                        {"label": "Electric Charge: +2/3 e;\nbaryon number: +1/3", "type": "leaf"},
                        {"label": "Flavour: Up", "type": "leaf"}
                    ]}
                ]
            },
            {
                "label": "Hadronic States",
                "type": "branch",
                "date": "Compositions",
                "children": [
                    {"label": "Baryons", "type": "sub", "date": "3-Quark Hadrons", "children": [
                        {"label": "Proton (uud): Contains\ntwo up quarks", "type": "leaf"},
                        {"label": "Neutron (udd): Contains\none up quark", "type": "leaf"}
                    ]},
                    {"label": "Mesons", "type": "sub", "date": "Quark-Antiquark", "children": [
                        {"label": "Pion (pi+): u and anti-d;\nPion (pi0): u-anti-u & d-anti-d", "type": "leaf"}
                    ]}
                ]
            }
        ]
    }
}

BASE_DIR = r"upsc/science_and_tech/Chemistry"

# Patching Logic
def patch_html(filepath, tree_data, title_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to overwrite the script block if it exists, or insert fresh.
    # Let's strip any existing injected mindmap elements to prevent duplication.
    # Remove CSS link
    html = html.replace('    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n', '')
    
    # Remove Mindmap div
    mindmap_div_pattern = r'            <!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->'
    html = re.sub(mindmap_div_pattern, '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    
    # Remove Script tags
    script_pattern = r'    <!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>'
    html = re.sub(script_pattern, '', html, flags=re.DOTALL)

    # Re-inject CSS
    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
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
        # Fallback: insert after notes-panel opening
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    # Re-inject script
    tree_json = json.dumps(tree_data)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
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
            
        topic_name = folder.replace('-', ' ')
        if os.path.exists(content_path):
            try:
                with open(content_path, 'r', encoding='utf-8') as f:
                    content_data = json.load(f)
                    topic_name = content_data.get('hero', {}).get('title', topic_name)
            except Exception:
                pass
        
        mindmap_key = folder
        if mindmap_key not in MINDMAPS:
            print(f"[{idx+1}/{len(folders)}] WARNING: Key {mindmap_key} not in pre-defined list. Creating default.")
            MINDMAPS[mindmap_key] = {
                "label": topic_name.replace(" ", "\n"),
                "type": "root",
                "children": [
                    {"label": "Overview", "type": "branch", "date": "Concept", "children": [
                        {"label": "Definition", "type": "sub", "children": [
                            {"label": "Key features", "type": "leaf"}
                        ]}
                    ]}
                ]
            }
            
        mindmap_data = MINDMAPS[mindmap_key]
        title_text = f"{topic_name} &mdash; Interactive Mindmap"
        success = patch_html(html_path, mindmap_data, title_text)
        if success:
            print(f"[{idx+1}/{len(folders)}] Processed {folder}")
        else:
            print(f"[{idx+1}/{len(folders)}] Failed to patch {folder}")

if __name__ == '__main__':
    main()
