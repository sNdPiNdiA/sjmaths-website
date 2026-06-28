import os
import re
import json

BASE_DIR = r"ssc-cgl/general-awareness/basic-science-awareness"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    words = []
    acronyms = {'icar', 'gst', 'dpc', 'mpc', 'adc', 'tac', 'scs', 'pesa', 'frs', 'fds', 'nri', 'pio', 'oci', 'caa', 'src', 'jvp', 'ist', 'gmt', 'utc', 'uv', 'co2', 'tisco', 'jnpt', 'cag', 'niti', 'upsc', 'spsc', 'nhrc', 'cic', 'cvc', 'sc', 'st', 'obc', 'dpsp', 'vp', 'pm', 'amtm', 'hc', 'gdp', 'gnp', 'ndp', 'nnp', 'nfia', 'pdi', 'gva', 'cso', 'nso', 'fyp', 'ndc', 'rbi', 'crr', 'slr', 'msf', 'omo', 'npa', 'ibc', 'mat', 'frbm', 'msme', 'lpg', 'fdi', 'fii', 'psu', 'bop', 'cacp', 'msp', 'frp', 'bec', 'bcg', 'atp', 'rbc', 'wbc', 'sa', 'cns', 'adh', 'kg', 'hp', 'tir', 'sonar', 'tnt', 'rdx'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'vs', 'outside', 'between', 'or', 'life', 'major', 'era', 'sects', 'teachings', 'councils', 'findings', 'trade', 'sites', 'rig', 'later']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Enhanced, highly comprehensive mindmaps for all 10 CGL Science folders
def get_custom_branches(folder_name):
    fl = folder_name.lower()
    t = get_clean_title(folder_name)
    
    # 1. BIOLOGY: CELL BIOLOGY STRUCTURE & CLASSIFICATION OF ORGANISMS
    if 'biology-cell-biology' in fl:
        return [
            {
                "label": "Cell Biology & Division (Cytology)", "type": "branch", "date": "Cytology Core",
                "children": [
                    {
                        "label": "Discovery & Cell Theory", "type": "sub", "date": "Timeline",
                        "children": [
                            {"label": "Robert Hooke (1665): Dead cork cell; Leeuwenhoek (1674): First living cell; Robert Brown (1831): Discovered nucleus", "type": "leaf"},
                            {"label": "Cell Theory (Schleiden & Schwann, 1839): All living things are composed of cells; Virchow: Cells from pre-existing cells", "type": "leaf"},
                            {"label": "Prokaryotic: No nuclear membrane, 70S ribosome (Bacteria); Eukaryotic: Organelles present, 80S ribosome (Plants/Animals)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Cell Organelles & Structures", "type": "sub", "date": "Organelles",
                        "children": [
                            {"label": "Mitochondria: Powerhouse, site of ATP synthesis, contains own DNA & 70S ribosomes", "type": "leaf"},
                            {"label": "Ribosomes: Protein synthesis, non-membranous; Lysosomes: Suicide bags with hydrolytic enzymes", "type": "leaf"},
                            {"label": "Plastids: Plants only (Chloroplast photosynthesis, Chromoplast color); Cell Wall: Plants (cellulose), Fungi (chitin)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Cell Division & Non-Cells", "type": "sub", "date": "Division",
                        "children": [
                            {"label": "Mitosis: Somatic cells, 2 diploid daughter cells, growth/repair; Meiosis: Germ cells, 4 haploid daughter cells, crossing over", "type": "leaf"},
                            {"label": "Viruses: Nucleic acid (DNA/RNA) + protein coat, non-living outside host; Viroids: Naked RNA; Prions: Infectious proteins", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Classification of Organisms (Taxonomy)", "type": "branch", "date": "Taxonomy Core",
                "children": [
                    {
                        "label": "Taxonomic System", "type": "sub", "date": "Linnaeus",
                        "children": [
                            {"label": "Carolus Linnaeus: Father of Taxonomy; Binomial Nomenclature (Genus + Species) in 'Systema Naturae'", "type": "leaf"},
                            {"label": "Hierarchy: Kingdom -> Phylum (Animals) / Division (Plants) -> Class -> Order -> Family -> Genus -> Species", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Whittaker's Five Kingdoms", "type": "sub", "date": "Five Kingdoms",
                        "children": [
                            {"label": "Monera: Prokaryotic unicellular (Bacteria); Protista: Eukaryotic unicellular (Amoeba); Fungi: Decomposers (Yeast)", "type": "leaf"},
                            {"label": "Plantae: Autotrophic; Thallophyta, Bryophyta (amphibian plants), Pteridophyta, Gymnosperms, Angiosperms", "type": "leaf"},
                            {"label": "Animalia: Heterotrophic; Arthropoda (largest phylum, insects), Annelida (earthworm), Mollusca (shells), Chordata (vertebrates)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 2. BIOLOGY: HUMAN PHYSIOLOGY (DIGESTIVE, RESPIRATORY, CIRCULATORY)
    elif 'biology-human-physiology-digestive' in fl:
        return [
            {
                "label": "Human Digestive System", "type": "branch", "date": "Digestion",
                "children": [
                    {
                        "label": "Alimentary Canal & Teeth", "type": "sub", "date": " Canal",
                        "children": [
                            {"label": "Mouth: Ptyalin (salivary amylase) digests starch to maltose; Adult dental formula: 2123/2123 (32 teeth); Child: 2102/2102", "type": "leaf"},
                            {"label": "Stomach: Gastric juice (HCl, Pepsin, Renin, pH 1.5-2); Small Intestine: complete digestion & absorption via villi", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Glands & Secretions", "type": "sub", "date": "Glands",
                        "children": [
                            {"label": "Liver: Largest gland; secretes Bile (emulsifies fats, stored in Gallbladder); Pancreas: Trypsin, Amylase, Lipase", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Human Respiratory System", "type": "branch", "date": "Respiration",
                "children": [
                    {
                        "label": "Gas Exchange & Energy", "type": "sub", "date": "Lungs",
                        "children": [
                            {"label": "Organs: Trachea -> Bronchi -> Alveoli (air sacs, gas exchange); Aerobic (with O2, 38 ATP) vs. Anaerobic (without O2)", "type": "leaf"},
                            {"label": "Hemoglobin: Iron pigment in RBCs, high affinity for CO; carries oxygen as oxyhemoglobin", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Human Circulatory System", "type": "branch", "date": "Circulation",
                "children": [
                    {
                        "label": "Blood Composition & Clotting", "type": "sub", "date": "Blood",
                        "children": [
                            {"label": "Plasma (55% fluid); RBCs (lifespan 120 days, no nucleus, transport O2); WBCs (immunity); Platelets (blood clotting)", "type": "leaf"},
                            {"label": "Clotting Cascade: Thromboplastin + Prothrombin + Calcium -> Thrombin; Thrombin + Fibrinogen -> Fibrin threads", "type": "leaf"},
                            {"label": "Blood Groups: Karl Landsteiner (A, B, AB, O); AB is Universal Acceptor, O is Universal Donor; Rh factor", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Heart & Vessels", "type": "sub", "date": "Cardiac",
                        "children": [
                            {"label": "Heart: 4 chambers; SA Node (pacemaker in right auricle); Arteries (oxygenated, away) vs. Veins (deoxygenated, to)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 3. BIOLOGY: HUMAN PHYSIOLOGY (NERVOUS, ENDOCRINE, EXCRETORY, SKELETAL)
    elif 'biology-human-physiology-nervous' in fl:
        return [
            {
                "label": "Nervous System & Sense Organs", "type": "branch", "date": "Neurology",
                "children": [
                    {
                        "label": "Central Nervous System (CNS)", "type": "sub", "date": "Brain",
                        "children": [
                            {"label": "Cerebrum: Largest part of brain, controls voluntary actions, memory, intelligence, sensory perceptions", "type": "leaf"},
                            {"label": "Hypothalamus: Regulates temperature, hunger, thirst, emotions; Medulla Oblongata: Controls involuntary actions", "type": "leaf"},
                            {"label": "Cerebellum: Coordinates balance & posture; Neuron: Basic functional unit, synapse chemical transmission", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Reflex Arc & Sense Organs", "type": "sub", "date": "Sensory",
                        "children": [
                            {"label": "Reflex Arc: Receptor -> Sensory Neuron -> Spinal Cord (Interneuron) -> Motor Neuron -> Effector (muscle response)", "type": "leaf"},
                            {"label": "Eye Structure: Cornea (refraction), Iris (pupil size), Retina (rods/cones), Fovea (max acuity), Blind spot (no photoreceptors)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Endocrine Glands (Hormones)", "type": "branch", "date": "Endocrinology",
                "children": [
                    {
                        "label": "Glands & Secretions", "type": "sub", "date": "Hormones",
                        "children": [
                            {"label": "Pituitary (Master): Growth Hormone, ADH; Thyroid (Largest): Thyroxine (requires Iodine, goitre deficiency)", "type": "leaf"},
                            {"label": "Adrenal Glands: Adrenaline (emergency/fight-or-flight); Pancreas: Insulin (diabetes mellitus, beta cells)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Excretory & Skeletal", "type": "branch", "date": "Excretion & Skeleton",
                "children": [
                    {
                        "label": "Excretory System", "type": "sub", "date": "Kidneys",
                        "children": [
                            {"label": "Kidneys: Filter blood; Nephron: Functional unit; Urine: Urochrome pigment (yellow), Calcium Oxalate stones", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Skeletal System", "type": "sub", "date": "Bones",
                        "children": [
                            {"label": "Bones: 206 in adults; Femur (longest/strongest), Stapes (smallest, ear); Enamel: Hardest body substance (teeth)", "type": "leaf"},
                            {"label": "Tendon: Connects Muscle to Bone; Ligament: Connects Bone to Bone", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 4. BIOLOGY: NUTRITION, VITAMINS, HUMAN DISEASES, PLANT BIOLOGY
    elif 'biology-nutrition-vitamins' in fl:
        return [
            {
                "label": "Nutrition & Vitamins", "type": "branch", "date": "Nutrients",
                "children": [
                    {
                        "label": "Vitamin Deficiencies", "type": "sub", "date": "Vitamins",
                        "children": [
                            {"label": "Water-Soluble: B-complex, C; Fat-Soluble: A, D, E, K", "type": "leaf"},
                            {"label": "Vitamin A (Retinol): Night blindness; Vitamin B1 (Thiamine): Beriberi; Vitamin B12: Pernicious anemia (Cobalt)", "type": "leaf"},
                            {"label": "Vitamin C (Ascorbic Acid): Scurvy; Vitamin D: Rickets; Vitamin K (Phylloquinone): Delayed clotting", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Human Diseases & Vaccines", "type": "branch", "date": "Pathology",
                "children": [
                    {
                        "label": "Disease Classification", "type": "sub", "date": "Pathogens",
                        "children": [
                            {"label": "Bacterial: Tuberculosis (BCG vaccine), Cholera, Typhoid (Widal test), Tetanus, Plague", "type": "leaf"},
                            {"label": "Viral: AIDS (ELISA test), Polio (Salk dead / Sabin live), Rabies (hydrophobia), Dengue, Influenza", "type": "leaf"},
                            {"label": "Protozoan: Malaria (Plasmodium, female Anopheles), Kala-azar (sandfly), Sleeping Sickness (tsetse fly)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Plant Biology & Reproduction", "type": "branch", "date": "Botany",
                "children": [
                    {
                        "label": "Plant Tissues & Hormones", "type": "sub", "date": "Botany Core",
                        "children": [
                            {"label": "Xylem: Transports water/minerals (unidirectional); Phloem: Transports food (bidirectional)", "type": "leaf"},
                            {"label": "Hormones: Auxin (apical dominance), Gibberellin (elongation), ABA (inhibitor), Ethylene (gaseous fruit ripener)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Plant Reproduction", "type": "sub", "date": "Reproduction",
                        "children": [
                            {"label": "Double Fertilization: Unique to Angiosperms, forms diploid zygote and triploid endosperm", "type": "leaf"},
                            {"label": "Parthenocarpy: Formation of seedless fruit without fertilization (banana, pineapple)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 5. CHEMISTRY: STATES OF MATTER, ELEMENTS, COMPOUNDS & MIXTURES
    elif 'chemistry-states-of-matter' in fl:
        return [
            {
                "label": "Physical States & Gas Laws", "type": "branch", "date": "Physical States",
                "children": [
                    {
                        "label": "Five States of Matter", "type": "sub", "date": "States",
                        "children": [
                            {"label": "Solid: Fixed shape/volume; Liquid: Fixed volume, fluid; Gas: High compressibility, fills container", "type": "leaf"},
                            {"label": "Plasma: Superheated ionized gas in stars; Bose-Einstein Condensate (BEC): Super-cooled near absolute zero", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Gas Laws", "type": "sub", "date": "Gas Laws",
                        "children": [
                            {"label": "Boyle's Law: PV = constant (at constant T); Charles's Law: V/T = constant (at constant P); Ideal Gas: PV = nRT", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Phase Transitions", "type": "sub", "date": "Transitions",
                        "children": [
                            {"label": "Sublimation: Solid to gas directly; Camphor, Ammonium Chloride, Dry Ice (solid CO2)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Elements, Compounds & Mixtures", "type": "branch", "date": "Classification",
                "children": [
                    {
                        "label": "Pure Substances & Colloids", "type": "sub", "date": "Pures",
                        "children": [
                            {"label": "Elements: Single atom type (Metals, Non-metals, Metalloids like Silicon/Germanium); Compounds: chemically combined in fixed ratios", "type": "leaf"},
                            {"label": "Colloids: Aerosol (fog/smoke), Emulsion (milk), Foam (shaving cream), Sol (paint/cell fluids)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Mixtures & Separation", "type": "sub", "date": "Separation",
                        "children": [
                            {"label": "Homogeneous (Solutions, air, alloys) vs. Heterogeneous (blood, milk, sand-water)", "type": "leaf"},
                            {"label": "Fractional Distillation: Separates petroleum fractions by boiling point; Centrifugation: Cream from milk", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 6. CHEMISTRY: ATOMS, PERIODIC TABLE, ACIDS-BASES, METALS-NON METALS
    elif 'chemistry-atoms-periodic' in fl:
        return [
            {
                "label": "Atomic Structure & Periodicity", "type": "branch", "date": "Atoms",
                "children": [
                    {
                        "label": "Subatomic Particles & Bonding", "type": "sub", "date": "Particles",
                        "children": [
                            {"label": "Proton (positive, Goldstein/Rutherford), Electron (negative, J.J. Thomson), Neutron (neutral, Chadwick)", "type": "leaf"},
                            {"label": "Atomic Number (Z, protons); Mass Number (A, P+N); Isotopes (same Z, different A); Isobars (same A, different Z)", "type": "leaf"},
                            {"label": "Bonding: Ionic (electron transfer, high melting, NaCl) vs Covalent (electron sharing, lower melting, H2O)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Modern Periodic Table", "type": "sub", "date": "Periodic Table",
                        "children": [
                            {"label": "Henry Moseley (1913): Based on atomic number; 18 groups & 7 periods; Group 17 halogens, Group 18 inert gases", "type": "leaf"},
                            {"label": "Trends: Electronegativity, Ionization Energy (increase across period, decrease down group); Radius (inverse)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Acids, Bases, Salts & Redox", "type": "branch", "date": "Acids & Bases",
                "children": [
                    {
                        "label": "pH Scale & Concepts", "type": "sub", "date": "pH",
                        "children": [
                            {"label": "Acids: blue litmus to red, pH < 7, release H+; Bases: red litmus to blue, pH > 7, release OH-", "type": "leaf"},
                            {"label": "pH scale (Sorensen, 0-14); Blood pH: 7.4 (slightly basic); Gastric juice pH: 1.5-2 (highly acidic)", "type": "leaf"},
                            {"label": "Examples: Formic Acid (ant sting), Lactic Acid (curd); Baking Soda (NaHCO3), Washing Soda (Na2CO3)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Oxidation & Reduction", "type": "sub", "date": "Redox",
                        "children": [
                            {"label": "Oxidation: Loss of electrons, addition of oxygen, removal of hydrogen; Reduction: Gain of electrons, removal of oxygen, addition of hydrogen", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Metals & Non-Metals", "type": "branch", "date": "Materials",
                "children": [
                    {
                        "label": "Key Elements", "type": "sub", "date": "Elements",
                        "children": [
                            {"label": "Mercury: Only liquid metal; Bromine: Only liquid non-metal; Graphite: Non-metal that conducts electricity", "type": "leaf"},
                            {"label": "Sodium/Potassium: Highly reactive, stored in kerosene, easily cut with a knife", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 7. CHEMISTRY: CARBON COMPOUNDS, DAILY-LIFE CHEMISTRY & POLYMERS
    elif 'chemistry-carbon-compounds' in fl:
        return [
            {
                "label": "Carbon & its Compounds", "type": "branch", "date": "Carbon",
                "children": [
                    {
                        "label": "Allotropes & Hydrocarbons", "type": "sub", "date": "Allotropes",
                        "children": [
                            {"label": "Diamond: Hardest substance, 3D tetrahedral, bad conductor; Graphite: Hexagonal layers, conducts electricity", "type": "leaf"},
                            {"label": "Fullerenes (C60) Buckyballs & Graphene (single-layer carbon lattice); LPG: Butane/Propane; CNG: Methane", "type": "leaf"},
                            {"label": "Alkanes (saturated, single bond, C_nH_{2n+2}); Alkenes (double bond); Alkynes (triple bond)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Chemistry in Daily Life & Explosives", "type": "branch", "date": "Applied Chem",
                "children": [
                    {
                        "label": "Soaps, Glass & Cement", "type": "sub", "date": "Household",
                        "children": [
                            {"label": "Soaps: Sodium/potassium fatty salts; Saponification: Alkaline hydrolysis of fats/oils; Detergents: Sulfonates, hard water", "type": "leaf"},
                            {"label": "Glass: Sand (silica) + washing soda + limestone; Cement: Lime + clay + Gypsum (delays setting)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Explosive Chemistry", "type": "sub", "date": "Explosives",
                        "children": [
                            {"label": "TNT: Trinitrotoluene; RDX: Research Department Explosive (cyclonite); Dynamite: Invented by Alfred Nobel using Nitroglycerin", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Polymers & Plastics", "type": "branch", "date": "Polymers",
                "children": [
                    {
                        "label": "Synthetic Polymers", "type": "sub", "date": "Plastics",
                        "children": [
                            {"label": "Teflon (non-stick pans); PVC (polyvinyl chloride); Bakelite: Thermosetting plastic for electrical switches", "type": "leaf"},
                            {"label": "Rayon: Semi-synthetic fiber (artificial silk made from wood pulp)", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 8. PHYSICS: UNITS, MOTION, KINEMATICS, NEWTON'S LAWS & GRAVITATION
    elif 'physics-units-motion' in fl:
        return [
            {
                "label": "Units & Dimensions", "type": "branch", "date": "Measurement",
                "children": [
                    {
                        "label": "SI Units", "type": "sub", "date": "Fundamental",
                        "children": [
                            {"label": "7 Base Units: Meter, Kilogram, Second, Ampere, Kelvin, Mole, Candela", "type": "leaf"},
                            {"label": "Derived: Force (Newton), Work/Energy (Joule), Power (Watt), Pressure (Pascal); Light Year: distance unit", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Kinematics & Newton's Laws", "type": "branch", "date": "Mechanics",
                "children": [
                    {
                        "label": "Scalar vs Vector", "type": "sub", "date": "Vectors",
                        "children": [
                            {"label": "Scalar (magnitude only): Distance, Speed, Mass, Work; Vector (+ direction): Displacement, Velocity, Force", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Newton's Laws of Motion", "type": "sub", "date": "Laws of Motion",
                        "children": [
                            {"label": "1st Law (Inertia): Body resists motion change; 2nd Law (F=ma): Force equals rate of change of momentum", "type": "leaf"},
                            {"label": "3rd Law: Action-Reaction (rocket propulsion, gun recoil); Circular: Centripetal force acts towards center (mv^2/r)", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Gravitation, Orbits & Kepler", "type": "branch", "date": "Gravitation",
                "children": [
                    {
                        "label": "Gravity & Escape Velocity", "type": "sub", "date": "Gravity",
                        "children": [
                            {"label": "Newton's Law: F = G*m1*m2/r^2; g = 9.8 m/s^2 (max at poles, min at equator, zero at center)", "type": "leaf"},
                            {"label": "Escape Velocity: 11.2 km/s (Earth); Geostationary Satellites: ~36,000 km orbit, 24 hr period", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Kepler's Planetary Laws", "type": "sub", "date": "Kepler",
                        "children": [
                            {"label": "1st Law (Orbits): Elliptical; 2nd Law (Areas): Equal areas in equal times; 3rd Law (Periods): T^2 proportional to r^3", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 9. PHYSICS: WORK, ENERGY, POWER, HEAT, THERMODYNAMICS, WAVE & SOUND
    elif 'physics-work-energy' in fl:
        return [
            {
                "label": "Work, Energy & Power", "type": "branch", "date": "Power",
                "children": [
                    {
                        "label": "Mechanics Core", "type": "sub", "date": "Work/Energy",
                        "children": [
                            {"label": "Work: W = F*s*cos(theta); zero work when force perpendicular to motion (coolie carrying load)", "type": "leaf"},
                            {"label": "Kinetic Energy: 1/2*m*v^2; Potential Energy: mgh; Conservation of Energy: constant total energy", "type": "leaf"},
                            {"label": "Power: Work/Time (Watt); 1 Horsepower (HP) = 746 Watts", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Heat, Expansion & Thermodynamics", "type": "branch", "date": "Heat",
                "children": [
                    {
                        "label": "Thermal Physics", "type": "sub", "date": "Thermodynamics",
                        "children": [
                            {"label": "Temperature scales: C/5 = (F-32)/9 = (K-273)/5; Absolute Zero: -273.15 C (0 K)", "type": "leaf"},
                            {"label": "Water Anomalous Expansion: Maximum density and minimum volume at 4 C; causes frozen lakes to remain liquid below top layer", "type": "leaf"},
                            {"label": "Thermodynamics: Zeroth Law (temperature), First Law (energy conservation), Second Law (entropy flow)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Specific & Latent Heat", "type": "sub", "date": "Heat Capacity",
                        "children": [
                            {"label": "Specific Heat: Heat needed to raise temp of 1g by 1 C; Latent Heat: Heat absorbed during phase change without changing temp", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Wave & Sound", "type": "branch", "date": "Acoustics",
                "children": [
                    {
                        "label": "Wave Mechanics", "type": "sub", "date": "Waves",
                        "children": [
                            {"label": "Transverse (light, perpendicular) vs. Longitudinal (sound, parallel); Sound needs material medium (no vacuum)", "type": "leaf"},
                            {"label": "Frequency: Infrasonic (<20Hz), Audible (20-20k Hz), Ultrasonic (>20kHz, SONAR, bats)", "type": "leaf"},
                            {"label": "Speed of Sound: Max in solids (steel), min in gases (air ~344 m/s); Echo: minimum 17.2m distance needed", "type": "leaf"}
                        ]
                    }
                ]
            }
        ]

    # 10. PHYSICS: LIGHT, OPTICS, ELECTRICITY, MAGNETISM & RADIOACTIVITY
    elif 'physics-light-optics' in fl:
        return [
            {
                "label": "Light & Optics", "type": "branch", "date": "Optics",
                "children": [
                    {
                        "label": "Reflection & Refraction", "type": "sub", "date": "Refraction",
                        "children": [
                            {"label": "Total Internal Reflection (TIR): Mirage, optical fibers, diamond sparkling (critical angle exceeded)", "type": "leaf"},
                            {"label": "Concave Mirror: Converging (dentists, solar furnace); Convex Mirror: Diverging (car rear-view mirror)", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Lenses & Eye Defects", "type": "sub", "date": "Eye Lenses",
                        "children": [
                            {"label": "Myopia (short-sight): Concave Lens; Hypermetropia (long-sight): Convex Lens", "type": "leaf"},
                            {"label": "Presbyopia (aging): Bifocal Lens; Astigmatism: Cylindrical Lens", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Electromagnetic Spectrum", "type": "sub", "date": "EM Spectrum",
                        "children": [
                            {"label": "Order (highest frequency to lowest): Gamma rays -> X-rays -> UV -> Visible -> Infrared -> Microwaves -> Radio waves", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Electricity & Magnetism", "type": "branch", "date": "Electromagnetism",
                "children": [
                    {
                        "label": "Electric Currents", "type": "sub", "date": "Current",
                        "children": [
                            {"label": "Ohm's Law: V = IR; Series resistance (R1+R2) vs. Parallel (1/R1+1/R2)", "type": "leaf"},
                            {"label": "Fuse Wire: High resistance, low melting point (lead-tin alloy); Bulb Filament: Tungsten", "type": "leaf"}
                        ]
                    },
                    {
                        "label": "Magnetism", "type": "sub", "date": "Magnets",
                        "children": [
                            {"label": "Permanent magnets: Steel/Alnico; Temporary electromagnets: Soft Iron", "type": "leaf"}
                        ]
                    }
                ]
            },
            {
                "label": "Radioactivity & Nuclear Physics", "type": "branch", "date": "Nuclear Physics",
                "children": [
                    {
                        "label": "Radioactive phenomena & Dating", "type": "sub", "date": "Nuclear",
                        "children": [
                            {"label": "Henri Becquerel (1896): Radioactivity; Alpha (+), Beta (-), and Gamma (neutral) rays; Carbon dating: C-14 used for organic dating", "type": "leaf"},
                            {"label": "Nuclear Fission: Splitting; Atom bomb, reactors (heavy water moderator, cadmium control rods)", "type": "leaf"},
                            {"label": "Nuclear Fusion: Fusing; Hydrogen bomb, solar energy (extreme heat required)", "type": "leaf"}
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
    # We find "id="traps-section"" to inject the mindmap card after it
    if 'id="traps-section"' in html:
        pos = html.find('id="traps-section"')
        end_div = html.find('</div>', pos)
        if end_div != -1:
            insert_pos = end_div + len('</div>')
            html = html[:insert_pos] + "\n" + mindmap_card + "\n" + html[insert_pos:]
    elif '<!-- Prep Tracker -->' in html:
        html = html.replace('<!-- Prep Tracker -->', mindmap_card + '\n<!-- Prep Tracker -->', 1)
    else:
        # Fallback to checklist
        pos = html.find('Self-Evaluation Checklist')
        if pos != -1:
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
