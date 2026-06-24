# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "carbon-its-compounds"
TOPIC_DISPLAY = "Carbon & its Compounds"
TOPIC_DISPLAY_HI = "कार्बन और उसके यौगिक"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\general-science\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "General Science",
    "parentUrl": "../",
    "current": "Carbon & its Compounds"
}

hero_en = {
    "title": "Carbon & its Compounds",
    "description": "Master the versatile nature of carbon, catenation and tetravalency parameters, allotropes (diamond, graphite, fullerenes), functional groups, nomenclature rules, key chemical properties, and soaps & detergents cleansing action."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Carbon & its Compounds Mock Test",
        "description": "Test your knowledge of organic nomenclature, allotrope properties, homologous series, functional groups, and cleansing action of soaps. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Historical Milestones in Organic Chemistry",
    "description": "Key discoveries that shaped our understanding of carbon and its vast array of compounds.",
    "cards": [
        {
            "period": "Vital Force Theory Proposed",
            "date": "1815",
            "details": "Jöns Jacob Berzelius proposes that organic compounds can only be produced by living organisms possessing a 'vital force'."
        },
        {
            "period": "Synthesis of Urea (Demise of Vital Force)",
            "date": "1828",
            "details": "Friedrich Wöhler synthesizes urea (an organic compound) from ammonium cyanate (an inorganic salt), proving organic molecules can be created in a lab."
        },
        {
            "period": "Kekulé's Structure of Benzene",
            "date": "1865",
            "details": "August Kekulé proposes the ring structure of benzene (C₆H₆) with alternating single and double bonds, laying the foundation for aromatic chemistry."
        },
        {
            "period": "Discovery of Fullerenes",
            "date": "1985",
            "details": "Harold Kroto, Robert Curl, and Richard Smalley discover Buckminsterfullerene (C₆₀), a new carbon allotrope shaped like a soccer ball."
        },
        {
            "period": "Isolation of Graphene",
            "date": "2004",
            "details": "Andre Geim and Konstantin Novoselov isolate graphene, a single-atom-thick layer of carbon, yielding exceptional conductivity and strength."
        }
    ]
}

mnemonics_en = {
    "title": "Carbon & its Compounds Mnemonics",
    "description": "Quick memory aids for hydrocarbon prefixes and functional group nomenclature.",
    "items": [
        {
            "title": "Mnemonic 1: Organic Nomenclature Prefixes",
            "phrase": "\"Mary Eats Peaches But Prefers Homecooked Meals\"",
            "decryption": "Remember carbon chain length prefixes for C₁ to C₆:<br>• <strong>M</strong>ary &rarr; <strong>M</strong>eth- (1 Carbon)<br>• <strong>E</strong>ats &rarr; <strong>E</strong>th- (2 Carbons)<br>• <strong>P</strong>eaches &rarr; <strong>P</strong>rop- (3 Carbons)<br>• <strong>B</strong>ut &rarr; <strong>B</strong>ut- (4 Carbons)<br>• <strong>P</strong>refers &rarr; <strong>P</strong>ent- (5 Carbons)<br>• <strong>H</strong>omecooked &rarr; <strong>H</strong>ex- (6 Carbons)"
        },
        {
            "title": "Mnemonic 2: Alkane vs Alkene vs Alkyne Bonds",
            "phrase": "\"A-E-Y (Single, Double, Triple)\"",
            "decryption": "Differentiate hydrocarbon bonds in alphabetical order:<br>• Alkan<strong>a</strong> (Alkane) &rarr; Single bonds (C-C)<br>• Alken<strong>e</strong> (Alkene) &rarr; Double bonds (C=C)<br>• Alkyn<strong>e</strong> (Alkyne) &rarr; Triple bonds (C&equiv;C)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Click to flip and test your understanding of carbon chemistry.",
    "items": [
        {
            "question": "Why does Carbon form covalent bonds instead of ionic bonds?",
            "answer": "Carbon has 4 valence electrons. To gain 4 electrons (forming C⁴⁻) requires high energy due to proton-electron repulsion in a small nucleus. To lose 4 electrons (forming C⁴⁺) requires huge ionization energy. Hence, Carbon <strong>shares</strong> electrons to complete its octet.",
            "icon": "fa-circle-nodes"
        },
        {
            "question": "What are the two key reasons for the massive number of carbon compounds in nature?",
            "answer": "1. <strong>Catenation</strong>: The unique ability of carbon to form strong covalent bonds with other carbon atoms, creating long straight, branched, or cyclic chains.<br>2. <strong>Tetravalency</strong>: Having a valency of 4 allows carbon to bond with four other mono-valent, divalent, or trivalent elements.",
            "icon": "fa-sitemap"
        },
        {
            "question": "Why does Graphite conduct electricity while Diamond does not?",
            "answer": "In <strong>Diamond</strong>, each carbon is tetrahedrally bonded to 4 other carbons, leaving no free electrons. In <strong>Graphite</strong>, each carbon is bonded to 3 others in flat hexagonal layers, leaving one free valence electron per carbon atom to move and conduct electricity.",
            "icon": "fa-bolt"
        },
        {
            "question": "What is denatured alcohol and why is it prepared?",
            "answer": "Denatured alcohol is ethanol made unfit for drinking by adding poisonous substances like <strong>methanol</strong> or dyes like copper sulfate (giving it a blue color). This prevents industrial-grade alcohol from being misused for consumption.",
            "icon": "fa-skull-crossbones"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Assuming all unsaturated hydrocarbons undergo addition reactions rapidly in the presence of any reagent. Saturated hydrocarbons undergo <strong>substitution</strong> reactions (typically with chlorine in the presence of sunlight), whereas unsaturated hydrocarbons (alkenes/alkynes) undergo <strong>addition</strong> reactions (like hydrogenation using nickel/palladium catalysts).",
        "<strong>Trap 2:</strong> Confusing the chemical reactions of Ethanol and Ethanoic acid with Sodium Bicarbonate. Only Ethanoic Acid (acetic acid) reacts with sodium bicarbonate (NaHCO₃) to release CO₂ gas with brisk effervescence. Ethanol <strong>does not</strong> react with NaHCO₃.",
        "<strong>Trap 3:</strong> Misunderstanding the structural shape of Buckminsterfullerene. C₆₀ Fullerene contains <strong>20 hexagons and 12 pentagons</strong> of carbon atoms arranged like a geodesic dome. Do not confuse the counts of hexagons and pentagons.",
        "<strong>Trap 4:</strong> Assuming soap works well in all types of water. Soap reacts with calcium and magnesium ions in <strong>hard water</strong> to form an insoluble precipitate called <strong>scum</strong>, which reduces cleansing action. Detergents do not form scum because their charged ammonium/sulfonate groups do not bind insoluble salts with Ca²⁺ or Mg²⁺."
    ]
}

deep_dive_en = [
    {
        "title": "1. Versatile Nature of Carbon, Covalent Bonding & Allotropes",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Tetravalency & Catenation:</strong> Carbon's small size allows its nucleus to hold shared pairs of electrons strongly, making its bonds exceptionally stable. This stability drives the formation of massive polymer chains and rings.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Allotropes of Carbon:</strong>
            <div class="premium-table-container">
              <table class="premium-table">
                <thead>
                  <tr>
                    <th>Property</th>
                    <th>Diamond (हीरा)</th>
                    <th>Graphite (ग्रेफाइट)</th>
                    <th>Fullerene (C₆₀)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Structure</td>
                    <td>3D Tetrahedral network</td>
                    <td>2D Hexagonal layered sheets</td>
                    <td>Soccer-ball-like geodesic cage</td>
                    
                  </tr>
                  <tr>
                    <td>Hybridization</td>
                    <td>sp³ hybridized</td>
                    <td>sp² hybridized</td>
                    <td>sp² hybridized (with curvature)</td>
                  </tr>
                  <tr>
                    <td>Hardness</td>
                    <td>Hardest natural substance</td>
                    <td>Soft, slippery, and greasy</td>
                    <td>Moderately hard solid</td>
                  </tr>
                  <tr>
                    <td>Conductivity</td>
                    <td>Insulator (no free electrons)</td>
                    <td>Excellent conductor</td>
                    <td>Semiconductor at RT</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </li>
        </ul>"""
    },
    {
        "title": "2. Hydrocarbons, Nomenclature & Functional Groups",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Homologous Series:</strong> A family of organic compounds having the same functional group and similar chemical properties. Adjacent members differ by a <strong>-CH₂- unit</strong> and a molecular mass of <strong>14 u</strong>.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Functional Groups Table:</strong>
            <div class="premium-table-container">
              <table class="premium-table">
                <thead>
                  <tr>
                    <th>Class</th>
                    <th>Functional Group Formula</th>
                    <th>Prefix / Suffix</th>
                    <th>Example Structure</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Alcohol</td>
                    <td>-OH</td>
                    <td>Suffix: -ol</td>
                    <td>Ethanol (C₂H₅OH)</td>
                  </tr>
                  <tr>
                    <td>Aldehyde</td>
                    <td>-CHO (Double bonded O on end C)</td>
                    <td>Suffix: -al</td>
                    <td>Ethanal (CH₃CHO)</td>
                  </tr>
                  <tr>
                    <td>Ketone</td>
                    <td>-CO- (C=O bonded to two carbons)</td>
                    <td>Suffix: -one</td>
                    <td>Propanone (CH₃COCH₃)</td>
                  </tr>
                  <tr>
                    <td>Carboxylic Acid</td>
                    <td>-COOH</td>
                    <td>Suffix: -oic acid</td>
                    <td>Ethanoic Acid (CH₃COOH)</td>
                  </tr>
                  <tr>
                    <td>Halogen</td>
                    <td>-Cl, -Br, -I</td>
                    <td>Prefix: chloro-, bromo-</td>
                    <td>Chloromethane (CH₃Cl)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </li>
        </ul>
        
        <!-- SVG Diagram 1: Hydrocarbon Nomenclature & Bonding Structures -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .struct-line { stroke: var(--text-dark, #2c3e50); stroke-width: 2.5px; fill: none; }
            .atom-text { font-family: 'Courier New', monospace; font-weight: bold; font-size: 15px; fill: var(--primary, #8e44ad); }
            .label-head { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            .label-desc { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">Organic Bonding Structures: Alkanes, Alkenes, Alkynes</text>
          
          <!-- Ethane (Left) -->
          <g transform="translate(60, 50)">
            <text x="70" y="25" class="label-head" fill="#2980b9" text-anchor="middle">Ethane (C₂H₆)</text>
            <text x="70" y="42" class="label-desc" text-anchor="middle">Alkane: Saturated (Single Bond)</text>
            
            <!-- Structural Drawing -->
            <!-- C - C -->
            <line x1="55" y1="105" x2="85" y2="105" class="struct-line" />
            <text x="40" y="110" class="atom-text">C</text>
            <text x="90" y="110" class="atom-text">C</text>
            <!-- Left C bonds -->
            <line x1="47" y1="95" x2="47" y2="75" class="struct-line" />
            <text x="42" y="70" class="atom-text">H</text>
            <line x1="47" y1="115" x2="47" y2="135" class="struct-line" />
            <text x="42" y="148" class="atom-text">H</text>
            <line x1="33" y1="105" x2="15" y2="105" class="struct-line" />
            <text x="3" y="110" class="atom-text">H</text>
            
            <!-- Right C bonds -->
            <line x1="97" y1="95" x2="97" y2="75" class="struct-line" />
            <text x="92" y="70" class="atom-text">H</text>
            <line x1="97" y1="115" x2="97" y2="135" class="struct-line" />
            <text x="92" y="148" class="atom-text">H</text>
            <line x1="105" y1="105" x2="123" y2="105" class="struct-line" />
            <text x="128" y="110" class="atom-text">H</text>
          </g>
          
          <!-- Ethene (Middle) -->
          <g transform="translate(320, 50)">
            <text x="70" y="25" class="label-head" fill="#d35400" text-anchor="middle">Ethene (C₂H₄)</text>
            <text x="70" y="42" class="label-desc" text-anchor="middle">Alkene: Unsaturated (Double Bond)</text>
            
            <!-- Structural Drawing -->
            <!-- C = C -->
            <line x1="55" y1="101" x2="85" y2="101" class="struct-line" />
            <line x1="55" y1="109" x2="85" y2="109" class="struct-line" />
            <text x="40" y="110" class="atom-text">C</text>
            <text x="90" y="110" class="atom-text">C</text>
            <!-- Left C bonds -->
            <line x1="38" y1="95" x2="25" y2="78" class="struct-line" />
            <text x="15" y="72" class="atom-text">H</text>
            <line x1="38" y1="115" x2="25" y2="132" class="struct-line" />
            <text x="15" y="145" class="atom-text">H</text>
            
            <!-- Right C bonds -->
            <line x1="102" y1="95" x2="115" y2="78" class="struct-line" />
            <text x="118" y="72" class="atom-text">H</text>
            <line x1="102" y1="115" x2="115" y2="132" class="struct-line" />
            <text x="118" y="145" class="atom-text">H</text>
          </g>
          
          <!-- Ethyne (Right) -->
          <g transform="translate(560, 50)">
            <text x="70" y="25" class="label-head" fill="#c0392b" text-anchor="middle">Ethyne (C₂H₂)</text>
            <text x="70" y="42" class="label-desc" text-anchor="middle">Alkyne: Unsaturated (Triple Bond)</text>
            
            <!-- Structural Drawing -->
            <!-- C ≡ C -->
            <line x1="55" y1="97" x2="85" y2="97" class="struct-line" />
            <line x1="55" y1="105" x2="85" y2="105" class="struct-line" />
            <line x1="55" y1="113" x2="85" y2="113" class="struct-line" />
            <text x="40" y="110" class="atom-text">C</text>
            <text x="90" y="110" class="atom-text">C</text>
            
            <!-- Bonds -->
            <line x1="33" y1="105" x2="15" y2="105" class="struct-line" />
            <text x="3" y="110" class="atom-text">H</text>
            <line x1="105" y1="105" x2="123" y2="105" class="struct-line" />
            <text x="128" y="110" class="atom-text">H</text>
          </g>
        </svg>"""
    },
    {
        "title": "3. Chemical Reactions of Carbon Compounds, Soaps & Detergents",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Important Chemical Reactions:</strong>
            <br>• <strong>Combustion:</strong> C + O₂ &rarr; CO₂ + Heat + Light. Saturated hydrocarbons give clean blue flames, while unsaturated hydrocarbons give yellow, sooty flames due to incomplete combustion.
            <br>• <strong>Oxidation:</strong> Alkaline KMnO₄ or Acidified K₂Cr₂O₇ oxidizes Ethanol to Ethanoic Acid (C₂H₅OH &rarr; CH₃COOH).
            <br>• <strong>Addition Reaction:</strong> Unsaturated fats (vegetable oils) are converted into saturated fats (vanaspati ghee) by adding hydrogen (Hydrogenation) using nickel catalyst at 473 K.
            <br>• <strong>Substitution Reaction:</strong> Saturated hydrocarbons react with Chlorine in the presence of sunlight: CH₄ + Cl₂ &rarr; CH₃Cl + HCl.
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>Soaps vs Detergents:</strong>
            <br>• <strong>Soaps:</strong> Sodium or potassium salts of long-chain carboxylic acids (fatty acids, e.g., sodium stearate, C₁₇H₃₅COONa). Biodegradable, but form scum (insoluble salts) with hard water containing Ca²⁺ and Mg²⁺.
            <br>• <strong>Detergents:</strong> Ammonium or sulfonate salts of long-chain carboxylic acids. Work effectively in both hard and soft water because their ions do not form insoluble precipitates with Ca²⁺ or Mg²⁺.
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>Cleansing Mechanism (Micelle Formation):</strong> Soap molecules have a dual nature:
            <br>1. <strong>Hydrophilic Head:</strong> Ionic part (polar head) that dissolves in water and points outwards.
            <br>2. <strong>Hydrophobic Tail:</strong> Hydrocarbon chain that dissolves in oil/grease and points inwards.
          </li>
        </ul>
        
        <!-- SVG Diagram 2: Soap Micelle Cleansing Mechanism -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .micelle-center { fill: #f39c12; stroke: #d35400; stroke-width: 2px; }
            .micelle-tail { stroke: var(--text-dark, #2c3e50); stroke-width: 2px; fill: none; }
            .micelle-head { fill: #2980b9; }
            
          </style>
          <text x="20" y="30" class="svg-title">Soap Micelle Structure & Cleansing Action (मिसेल संरचना)</text>
          
          <!-- Soap Molecule Key (Left) -->
          <g transform="translate(50, 60)">
            <rect x="0" y="0" width="200" height="130" fill="rgba(142, 68, 173, 0.05)" rx="6" stroke="rgba(142, 68, 173, 0.2)" />
            <text x="100" y="25" class="label-head" text-anchor="middle">Single Soap Molecule</text>
            
            <!-- Tail -->
            <path d="M 30 75 L 45 65 L 60 75 L 75 65 L 90 75 L 105 65 L 120 75 L 135 65" class="micelle-tail" />
            <!-- Head -->
            <circle cx="145" cy="65" r="10" class="micelle-head" />
            <text x="145" y="68" font-size="8px" fill="#ffffff" font-weight="bold" text-anchor="middle">COO⁻</text>
            
            <text x="80" y="105" class="label-desc" font-size="10px">Hydrophobic Tail (Oil-loving)</text>
            <text x="150" y="120" class="label-desc" font-size="10px" text-anchor="middle">Hydrophilic Head</text>
          </g>
          
          <!-- Micelle Ring (Right) -->
          <g transform="translate(480, 115)">
            <!-- Central Grease Drop -->
            <circle cx="0" cy="0" r="30" class="micelle-center" />
            <text x="0" y="5" class="node-text" font-weight="bold" fill="#ffffff" text-anchor="middle">Grease / Oil</text>
            
            <!-- Soap Tails radiating out -->
            <!-- 0 Deg -->
            <path d="M 30 0 L 70 0" class="micelle-tail" /><circle cx="75" cy="0" r="6" class="micelle-head" />
            <!-- 45 Deg -->
            <path d="M 21 21 L 49 49" class="micelle-tail" /><circle cx="53" cy="53" r="6" class="micelle-head" />
            <!-- 90 Deg -->
            <path d="M 0 30 L 0 70" class="micelle-tail" /><circle cx="0" cy="75" r="6" class="micelle-head" />
            <!-- 135 Deg -->
            <path d="M -21 21 L -49 49" class="micelle-tail" /><circle cx="-53" cy="53" r="6" class="micelle-head" />
            <!-- 180 Deg -->
            <path d="M -30 0 L -70 0" class="micelle-tail" /><circle cx="-75" cy="0" r="6" class="micelle-head" />
            <!-- 225 Deg -->
            <path d="M -21 -21 L -49 -49" class="micelle-tail" /><circle cx="-53" cy="-53" r="6" class="micelle-head" />
            <!-- 270 Deg -->
            <path d="M 0 -30 L 0 -70" class="micelle-tail" /><circle cx="0" cy="-75" r="6" class="micelle-head" />
            <!-- 315 Deg -->
            <path d="M 21 -21 L 49 -49" class="micelle-tail" /><circle cx="53" cy="-53" r="6" class="micelle-head" />
          </g>
          <text x="480" y="225" class="node-text" font-weight="bold" text-anchor="middle">Micelle captures grease at center, ionic heads remain dissolved in surrounding water</text>
        </svg>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "सामान्य विज्ञान",
    "parentUrl": "../",
    "current": "कार्बन और उसके यौगिक"
}

hero_hi = {
    "title": "कार्बन और उसके यौगिक",
    "description": "कार्बन की बहुमुखी प्रकृति, श्रृंखला (Catenation) और चतुःसंयोजकता (Tetravalency) मापदंडों, अपररूपों (हीरा, ग्रेफाइट, फुलरीन), कार्यात्मक समूहों, नामकरण के नियमों, प्रमुख रासायनिक गुणों और साबुनों व अपमार्जकों की शोधन क्रिया को समझें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरैक्टिव कार्बन और उसके यौगिक मॉक टेस्ट",
        "description": "कार्बनिक नामकरण, अपररूपों के गुण, समजातीय श्रेणी, कार्यात्मक समूहों और साबुनों की शोधन क्रिया के अपने ज्ञान का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "कार्बनिक रसायन विज्ञान में ऐतिहासिक मील के पत्थर",
    "description": "प्रमुख खोजें जिन्होंने कार्बन और उसके यौगिकों के बारे में हमारी समझ को आकार दिया।",
    "cards": [
        {
            "period": "जैव शक्ति सिद्धांत (Vital Force Theory) का प्रस्ताव",
            "date": "1815",
            "details": "जोन्स जैकब बर्ज़ेलियस ने प्रस्ताव दिया कि कार्बनिक यौगिकों का निर्माण केवल सजीवों में उपस्थित एक 'जैव शक्ति' द्वारा ही हो सकता है।"
        },
        {
            "period": "यूरिया का संश्लेषण (जैव शक्ति का अंत)",
            "date": "1828",
            "details": "फ्रेडरिक वोहलर ने अमोनियम सायनेट (एक अकार्बनिक लवण) से प्रयोगशाला में यूरिया (एक कार्बनिक यौगिक) का संश्लेषण किया, जिससे यह सिद्ध हुआ कि कार्बनिक अणु प्रयोगशाला में बनाए जा सकते हैं।"
        },
        {
            "period": "केकुले द्वारा बेंजीन की संरचना",
            "date": "1865",
            "details": "अगस्त केकुले ने बेंजीन (C₆H₆) की चक्रीय संरचना का प्रस्ताव रखा जिसमें एकांतर एकल और द्वि-आबंध उपस्थित थे, जिसने सुगंधित (aromatic) रसायन विज्ञान की नींव रखी।"
        },
        {
            "period": "फुलरीन की खोज",
            "date": "1985",
            "details": "हेरोल्ड क्रोटो, रॉबर्ट कर्ल और रिचर्ड स्माली ने बकमिनस्टरफुलरीन (C₆₀) की खोज की, जो फुटबॉल के आकार का एक नया कार्बन अपररूप है।"
        },
        {
            "period": "ग्राफीन का पृथक्करण",
            "date": "2004",
            "details": "आंद्रे जीम और कॉन्स्टेंटिन नोवोसेलोव ने ग्राफीन (कार्बन की एक परमाणु मोटी परत) को अलग किया, जिसके विद्युत चालन और ताकत के गुण असाधारण हैं।"
        }
    ]
}

mnemonics_hi = {
    "title": "कार्बन और उसके यौगिकों के लिए याद रखने के तरीके (Mnemonics)",
    "description": "हाइड्रोकार्बन पूर्वलग्न (prefixes) और कार्यात्मक समूहों के नामकरण को याद रखने के लिए त्वरित ट्रिक्स।",
    "items": [
        {
            "title": "युक्ति 1: कार्बनिक नामकरण पूर्वलग्न",
            "phrase": "\"Mary Eats Peaches But Prefers Homecooked Meals\"",
            "decryption": "C₁ से C₆ तक की कार्बन श्रृंखला की लंबाई के पूर्वलग्न याद रखें:<br>• <strong>M</strong>ary &rarr; <strong>Meth-</strong> (1 कार्बन)<br>• <strong>E</strong>ats &rarr; <strong>Eth-</strong> (2 कार्बन)<br>• <strong>P</strong>eaches &rarr; <strong>Prop-</strong> (3 कार्बन)<br>• <strong>B</strong>ut &rarr; <strong>But-</strong> (4 कार्बन)<br>• <strong>P</strong>refers &rarr; <strong>Pent-</strong> (5 कार्बन)<br>• <strong>H</strong>omecooked &rarr; <strong>Hex-</strong> (6 कार्बन)"
        },
        {
            "title": "युक्ति 2: एल्केन, एल्कीन और एल्काइन के आबंध",
            "phrase": "\"A-E-Y (एकल, द्वि, त्रि आबंध)\"",
            "decryption": "वर्णानुक्रम में हाइड्रोकार्बन आबंधों को अलग करें:<br>• Alkan<strong>a</strong> (एल्केन) &rarr; एकल आबंध (C-C)<br>• Alken<strong>e</strong> (एल्कीन) &rarr; द्वि-आबंध (C=C)<br>• Alkyn<strong>e</strong> (एल्काइन) &rarr; त्रि-आबंध (C&equiv;C)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय स्मरण फ्लैशकार्ड",
    "description": "कार्बन रसायन विज्ञान के बारे में अपनी समझ का परीक्षण करने के लिए क्लिक करें।",
    "items": [
        {
            "question": "कार्बन आयनिक आबंध के बजाय सहसंयोजक आबंध (covalent bonds) क्यों बनाता है?",
            "answer": "कार्बन के संयोजी कोश में 4 इलेक्ट्रॉन होते हैं। 4 इलेक्ट्रॉन ग्रहण करने (C⁴⁻ बनाने) के लिए एक छोटे नाभिक में प्रोटॉन-इलेक्ट्रॉन प्रतिकर्षण के कारण बहुत अधिक ऊर्जा की आवश्यकता होती है। 4 इलेक्ट्रॉन खोने (C⁴⁺ बनाने) के लिए भारी मात्रा में आयनीकरण ऊर्जा चाहिए। इसलिए, कार्बन उत्कृष्ट गैस विन्यास प्राप्त करने के लिए इलेक्ट्रॉनों की <strong>साझेदारी</strong> करता है।",
            "icon": "fa-circle-nodes"
        },
        {
            "question": "प्रकृति में कार्बन यौगिकों की विशाल संख्या के दो मुख्य कारण क्या हैं?",
            "answer": "1. <strong>श्रृंखलन (Catenation)</strong>: कार्बन परमाणुओं में कार्बन के ही अन्य परमाणुओं के साथ सहसंयोजक आबंध बनाकर लंबी सीधी, शाखित या चक्रीय श्रृंखलाएं बनाने की अद्वितीय क्षमता।<br>2. <strong>चतुःसंयोजकता (Tetravalency)</strong>: 4 संयोजकता होने के कारण कार्बन अन्य चार एकल-संयोजी, द्वि-संयोजी या त्रि-संयोजी तत्वों के साथ आबंध बना सकता है।",
            "icon": "fa-sitemap"
        },
        {
            "question": "ग्रेफाइट विद्युत का सुचालक क्यों है जबकि हीरा कुचालक है?",
            "answer": "<strong>हीरे</strong> में, प्रत्येक कार्बन परमाणु 4 अन्य कार्बन परमाणुओं के साथ चतुष्फलकीय रूप से आबंधित होता है, जिससे कोई मुक्त इलेक्ट्रॉन नहीं बचता। <strong>ग्रेफाइट</strong> में, प्रत्येक कार्बन परमाणु 2D हेक्सागोनल परतों में 3 अन्य कार्बन परमाणुओं से आबंधित होता है, जिससे प्रति कार्बन एक संयोजी इलेक्ट्रॉन स्वतंत्र घूमता है और विद्युत का चालन करता है।",
            "icon": "fa-bolt"
        },
        {
            "question": "विकृत ऐल्कोहॉल (denatured alcohol) क्या है और इसे क्यों बनाया जाता है?",
            "answer": "औद्योगिक इथेनॉल का दुरुपयोग पीने के लिए रोकने के लिए, उसमें <strong>मेथनॉल</strong> जैसे जहरीले पदार्थ या कॉपर सल्फेट जैसे रंग मिलाने वाले पदार्थ मिलाए जाते हैं, जिससे यह पीने योग्य नहीं रह जाता। इसे विकृत ऐल्कोहॉल कहते हैं।",
            "icon": "fa-skull-crossbones"
        }
    ]
}

traps_hi = {
    "title": "परीक्षा में सामान्य गलतियों से बचें",
    "items": [
        "<strong>धोखा 1:</strong> यह मानना कि सभी हाइड्रोकार्बन क्लोरीन के साथ प्रतिस्थापन अभिक्रियाएं देते हैं। संतृप्त हाइड्रोकार्बन सूर्य के प्रकाश की उपस्थिति में <strong>प्रतिस्थापन अभिक्रिया</strong> देते हैं, जबकि असंतृप्त हाइड्रोकार्बन (एल्कीन/एल्काइन) निकेल/पैलेडियम उत्प्रेरक की उपस्थिति में <strong>संकलन (addition) अभिक्रिया</strong> देते हैं (जैसे तेलों का हाइड्रोजनीकरण)।",
        "<strong>धोखा 2:</strong> इथेनॉल और इथेनॉइक अम्ल की सोडियम बाइकार्बोनेट (NaHCO₃) के साथ अभिक्रियाओं में भ्रम। केवल इथेनॉइक अम्ल (एसिटिक अम्ल) ही NaHCO₃ के साथ क्रिया करके तेज बुदबुदाहट के साथ CO₂ गैस छोड़ता है। इथेनॉल NaHCO₃ के साथ अभिक्रिया <strong>नहीं</strong> करता।",
        "<strong>धोखा 3:</strong> बकमिनस्टरफुलरीन की संरचना को गलत समझना। C₆₀ फुलरीन में <strong>20 षटकोण (hexagons) और 12 पंचकोण (pentagons)</strong> होते हैं। परीक्षा में इन संख्याओं को आपस में बदलने की गलती न करें।",
        "<strong>धोखा 4:</strong> यह मानना कि साबुन सभी प्रकार के जल में समान रूप से झाग बनाता है। साबुन <strong>कठोर जल</strong> में उपस्थित कैल्शियम और मैग्नीशियम आयनों के साथ क्रिया करके अघुलनशील अवक्षेप बनाता है जिसे <strong>स्कम (scum)</strong> कहते हैं। अपमार्जक (detergents) कठोर जल में स्कम नहीं बनाते क्योंकि उनके अमोनियम या सल्फोनेट समूह Ca²⁺ या Mg²⁺ के साथ अघुलनशील लवण नहीं बनाते।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. कार्बन की बहुमुखी प्रकृति, सहसंयोजक आबंध और अपररूप",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>श्रृंखलन और चतुःसंयोजकता:</strong> कार्बन का आकार बहुत छोटा होता है, जिससे इसका नाभिक साझे के इलेक्ट्रॉन युग्मों को मजबूती से पकड़ कर रखता है। यही कारण है कि कार्बन-कार्बन आबंध अत्यधिक स्थिर और मजबूत होते हैं, जिससे लंबी श्रृंखलाओं का निर्माण संभव होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>कार्बन के अपररूप (Allotropes of Carbon):</strong>
            <div class="premium-table-container">
              <table class="premium-table">
                <thead>
                  <tr>
                    <th>गुणधर्म</th>
                    <th>हीरा (Diamond)</th>
                    <th>ग्रेफाइट (Graphite)</th>
                    <th>फुलरीन (C₆₀)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>संरचना</td>
                    <td>त्रिविमीय (3D) चतुष्फलकीय जाल</td>
                    <td>द्विविमीय (2D) षटकोणीय परतदार परतें</td>
                    <td>फुटबॉल के आकार का पिंजरा (geodesic cage)</td>
                  </tr>
                  <tr>
                    <td>संकरण (Hybridization)</td>
                    <td>sp³ संकरित</td>
                    <td>sp² संकरित</td>
                    <td>sp² संकरित (गोलाकार वक्रता के साथ)</td>
                  </tr>
                  <tr>
                    <td>कठोरता</td>
                    <td>प्राकृतिक रूप से पाया जाने वाला सबसे कठोर पदार्थ</td>
                    <td>मुलायम, चिकना और फिसलनदार</td>
                    <td>मध्यम कठोर ठोस</td>
                  </tr>
                  <tr>
                    <td>विद्युत चालकता</td>
                    <td>कुचालक (कोई मुक्त इलेक्ट्रॉन नहीं)</td>
                    <td>उत्कृष्ट सुचालक</td>
                    <td>कमरे के ताप पर अर्धचालक (Semiconductor)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </li>
        </ul>"""
    },
    {
        "title": "2. हाइड्रोकार्बन, नामकरण और कार्यात्मक समूह",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>समजातीय श्रेणी (Homologous Series):</strong> यौगिकों की ऐसी श्रृंखला जिसमें एक ही कार्यात्मक समूह होता है और जिसके रासायनिक गुण समान होते हैं। दो क्रमागत सदस्यों के बीच हमेशा <strong>-CH₂- समूह</strong> और आणविक द्रव्यमान में <strong>14 u</strong> का अंतर होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>कार्यात्मक समूह सारणी (Functional Groups Table):</strong>
            <div class="premium-table-container">
              <table class="premium-table">
                <thead>
                  <tr>
                    <th>वर्ग</th>
                    <th>कार्यात्मक समूह सूत्र</th>
                    <th>पूर्वलग्न / अनुलग्न (Suffix)</th>
                    <th>उदाहरण यौगिक</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>ऐल्कोहॉल (Alcohol)</td>
                    <td>-OH</td>
                    <td>अनुलग्न: -ol (-ऑल)</td>
                    <td>इथेनॉल (C₂H₅OH)</td>
                  </tr>
                  <tr>
                    <td>ऐल्डिहाइड (Aldehyde)</td>
                    <td>-CHO (कार्बन से द्वि-आबंधित ऑक्सीजन)</td>
                    <td>अनुलग्न: -al (-ऐल)</td>
                    <td>इथेनैल (CH₃CHO)</td>
                  </tr>
                  <tr>
                    <td>कीटोन (Ketone)</td>
                    <td>-CO- (दो कार्बनों के मध्य C=O)</td>
                    <td>अनुलग्न: -one (-ओन)</td>
                    <td>प्रोपेनोन (CH₃COCH₃)</td>
                  </tr>
                  <tr>
                    <td>कार्बोक्सिलिक अम्ल</td>
                    <td>-COOH</td>
                    <td>अनुलग्न: -oic acid (-ओइक अम्ल)</td>
                    <td>इथेनॉइक अम्ल (CH₃COOH)</td>
                  </tr>
                  <tr>
                    <td>हैलो समूह (Halogen)</td>
                    <td>-Cl, -Br, -I</td>
                    <td>पूर्वलग्न: क्लोरो-, ब्रोमो-</td>
                    <td>क्लोरोमीथेन (CH₃Cl)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </li>
        </ul>
        
        <!-- SVG Diagram 1: Hydrocarbon Nomenclature & Bonding Structures (Hindi labels inside SVG) -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .struct-line { stroke: var(--text-dark, #2c3e50); stroke-width: 2.5px; fill: none; }
            .atom-text { font-family: 'Courier New', monospace; font-weight: bold; font-size: 15px; fill: var(--primary, #8e44ad); }
            .label-head { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            .label-desc { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">कार्बनिक यौगिकों के आबंध: एल्केन, एल्कीन, एल्काइन</text>
          
          <!-- Ethane (Left) -->
          <g transform="translate(60, 50)">
            <text x="70" y="25" class="label-head" fill="#2980b9" text-anchor="middle">इथेन (C₂H₆)</text>
            <text x="70" y="42" class="label-desc" text-anchor="middle">एल्केन: संतृप्त (एकल आबंध)</text>
            
            <!-- Structural Drawing -->
            <!-- C - C -->
            <line x1="55" y1="105" x2="85" y2="105" class="struct-line" />
            <text x="40" y="110" class="atom-text">C</text>
            <text x="90" y="110" class="atom-text">C</text>
            <!-- Left C bonds -->
            <line x1="47" y1="95" x2="47" y2="75" class="struct-line" />
            <text x="42" y="70" class="atom-text">H</text>
            <line x1="47" y1="115" x2="47" y2="135" class="struct-line" />
            <text x="42" y="148" class="atom-text">H</text>
            <line x1="33" y1="105" x2="15" y2="105" class="struct-line" />
            <text x="3" y="110" class="atom-text">H</text>
            
            <!-- Right C bonds -->
            <line x1="97" y1="95" x2="97" y2="75" class="struct-line" />
            <text x="92" y="70" class="atom-text">H</text>
            <line x1="97" y1="115" x2="97" y2="135" class="struct-line" />
            <text x="92" y="148" class="atom-text">H</text>
            <line x1="105" y1="105" x2="123" y2="105" class="struct-line" />
            <text x="128" y="110" class="atom-text">H</text>
          </g>
          
          <!-- Ethene (Middle) -->
          <g transform="translate(320, 50)">
            <text x="70" y="25" class="label-head" fill="#d35400" text-anchor="middle">इथेन (C₂H₄)</text>
            <text x="70" y="42" class="label-desc" text-anchor="middle">एल्कीन: असंतृप्त (द्वि-आबंध)</text>
            
            <!-- Structural Drawing -->
            <!-- C = C -->
            <line x1="55" y1="101" x2="85" y2="101" class="struct-line" />
            <line x1="55" y1="109" x2="85" y2="109" class="struct-line" />
            <text x="40" y="110" class="atom-text">C</text>
            <text x="90" y="110" class="atom-text">C</text>
            <!-- Left C bonds -->
            <line x1="38" y1="95" x2="25" y2="78" class="struct-line" />
            <text x="15" y="72" class="atom-text">H</text>
            <line x1="38" y1="115" x2="25" y2="132" class="struct-line" />
            <text x="15" y="145" class="atom-text">H</text>
            
            <!-- Right C bonds -->
            <line x1="102" y1="95" x2="115" y2="78" class="struct-line" />
            <text x="118" y="72" class="atom-text">H</text>
            <line x1="102" y1="115" x2="115" y2="132" class="struct-line" />
            <text x="118" y="145" class="atom-text">H</text>
          </g>
          
          <!-- Ethyne (Right) -->
          <g transform="translate(560, 50)">
            <text x="70" y="25" class="label-head" fill="#c0392b" text-anchor="middle">इथाइन (C₂H₂)</text>
            <text x="70" y="42" class="label-desc" text-anchor="middle">एल्काइन: असंतृप्त (त्रि-आबंध)</text>
            
            <!-- Structural Drawing -->
            <!-- C ≡ C -->
            <line x1="55" y1="97" x2="85" y2="97" class="struct-line" />
            <line x1="55" y1="105" x2="85" y2="105" class="struct-line" />
            <line x1="55" y1="113" x2="85" y2="113" class="struct-line" />
            <text x="40" y="110" class="atom-text">C</text>
            <text x="90" y="110" class="atom-text">C</text>
            
            <!-- Bonds -->
            <line x1="33" y1="105" x2="15" y2="105" class="struct-line" />
            <text x="3" y="110" class="atom-text">H</text>
            <line x1="105" y1="105" x2="123" y2="105" class="struct-line" />
            <text x="128" y="110" class="atom-text">H</text>
          </g>
        </svg>"""
    },
    {
        "title": "3. कार्बन यौगिकों की रासायनिक अभिक्रियाएं, साबुन और अपमार्जक",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>महत्वपूर्ण रासायनिक अभिक्रियाएं:</strong>
            <br>• <strong>दहन (Combustion):</strong> C + O₂ &rarr; CO₂ + ऊष्मा + प्रकाश। संतृप्त हाइड्रोकार्बन स्वच्छ नीली लौ देते हैं, जबकि असंतृप्त हाइड्रोकार्बन अपूर्ण दहन के कारण पीली, कज्जली (sooty) लौ देते हैं।
            <br>• <strong>ऑक्सीकरण (Oxidation):</strong> क्षारीय KMnO₄ या अम्लीकृत K₂Cr₂O₇ इथेनॉल को इथेनॉइक अम्ल में ऑक्सीकृत करते हैं (C₂H₅OH &rarr; CH₃COOH)।
            <br>• <strong>संकलन अभिक्रिया (Addition Reaction):</strong> असंतृप्त वसा (वनस्पति तेलों) को निकेल उत्प्रेरक की उपस्थिति में हाइड्रोजन जोड़कर संतृप्त वसा (वनस्पति घी) में बदला जाता है (हाइड्रोजनीकरण)।
            <br>• <strong>प्रतिस्थापन अभिक्रिया (Substitution):</strong> संतृप्त हाइड्रोकार्बन सूर्य के प्रकाश की उपस्थिति में क्लोरीन के साथ अभिक्रिया करते हैं: CH₄ + Cl₂ &rarr; CH₃Cl + HCl।
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>साबुन बनाम अपमार्जक:</strong>
            <br>• <strong>साबुन (Soaps):</strong> लंबी श्रृंखला वाले कार्बोक्सिलिक अम्लों (वसा अम्लों) के सोडियम या पोटेशियम लवण होते हैं (जैसे सोडियम स्टीयरेट, C₁₇H₃₅COONa)। ये जैव-निम्नीकरणीय होते हैं, लेकिन Ca²⁺ और Mg²⁺ युक्त कठोर जल में अघुलनशील अवक्षेप (स्कम) बनाते हैं।
            <br>• <strong>अपमार्जक (Detergents):</strong> लंबी श्रृंखला वाले कार्बोक्सिलिक अम्लों के अमोनियम या सल्फोनेट लवण होते हैं। ये कठोर और मृदु दोनों प्रकार के जल में प्रभावी होते हैं क्योंकि इनके आवेशित सिरे कठोर जल में उपस्थित Ca²⁺ या Mg²⁺ के साथ अघुलनशील अवक्षेप नहीं बनाते।
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>शोधन क्रिया (मिसेल निर्माण):</strong> साबुन के अणुओं के दो भाग होते हैं:
            <br>1. <strong>जलरागी (Hydrophilic) सिरा:</strong> आयनिक भाग (ध्रुवीय सिरा) जो जल में घुलता है और बाहर की ओर निर्देशित होता है।
            <br>2. <strong>जलविरागी (Hydrophobic) सिरा:</strong> हाइड्रोकार्बन पूंछ जो तेल या मैल में घुलती है और केंद्र की ओर निर्देशित होती है।
          </li>
        </ul>
        
        <!-- Soap Micelle Cleansing Mechanism SVG (same styled SVG for Hindi version) -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .micelle-center { fill: #f39c12; stroke: #d35400; stroke-width: 2px; }
            .micelle-tail { stroke: var(--text-dark, #2c3e50); stroke-width: 2px; fill: none; }
            .micelle-head { fill: #2980b9; }
            
          </style>
          <text x="20" y="30" class="svg-title">साबुन मिसेल संरचना और शोधन क्रिया (Soap Micelle Cleansing Action)</text>
          
          <!-- Soap Molecule Key (Left) -->
          <g transform="translate(50, 60)">
            <rect x="0" y="0" width="200" height="130" fill="rgba(142, 68, 173, 0.05)" rx="6" stroke="rgba(142, 68, 173, 0.2)" />
            <text x="100" y="25" class="label-head" text-anchor="middle">एकल साबुन का अणु</text>
            
            <!-- Tail -->
            <path d="M 30 75 L 45 65 L 60 75 L 75 65 L 90 75 L 105 65 L 120 75 L 135 65" class="micelle-tail" />
            <!-- Head -->
            <circle cx="145" cy="65" r="10" class="micelle-head" />
            <text x="145" y="68" font-size="8px" fill="#ffffff" font-weight="bold" text-anchor="middle">COO⁻</text>
            
            <text x="80" y="105" class="label-desc" font-size="10px">जलविरागी पूंछ (तेल प्रेमी)</text>
            <text x="150" y="120" class="label-desc" font-size="10px" text-anchor="middle">जलरागी सिरा</text>
          </g>
          
          <!-- Micelle Ring (Right) -->
          <g transform="translate(480, 115)">
            <!-- Central Grease Drop -->
            <circle cx="0" cy="0" r="30" class="micelle-center" />
            <text x="0" y="5" class="node-text" font-weight="bold" fill="#ffffff" text-anchor="middle">मैल / तेल</text>
            
            <!-- Soap Tails radiating out -->
            <path d="M 30 0 L 70 0" class="micelle-tail" /><circle cx="75" cy="0" r="6" class="micelle-head" />
            <path d="M 21 21 L 49 49" class="micelle-tail" /><circle cx="53" cy="53" r="6" class="micelle-head" />
            <path d="M 0 30 L 0 70" class="micelle-tail" /><circle cx="0" cy="75" r="6" class="micelle-head" />
            <path d="M -21 21 L -49 49" class="micelle-tail" /><circle cx="-53" cy="53" r="6" class="micelle-head" />
            <path d="M -30 0 L -70 0" class="micelle-tail" /><circle cx="-75" cy="0" r="6" class="micelle-head" />
            <path d="M -21 -21 L -49 -49" class="micelle-tail" /><circle cx="-53" cy="-53" r="6" class="micelle-head" />
            <path d="M 0 -30 L 0 -70" class="micelle-tail" /><circle cx="0" cy="-75" r="6" class="micelle-head" />
            <path d="M 21 -21 L 49 -49" class="micelle-tail" /><circle cx="53" cy="-53" r="6" class="micelle-head" />
          </g>
          <text x="480" y="225" class="node-text" font-weight="bold" text-anchor="middle">मिसेल केंद्र में मैल को पकड़ता है, जबकि आयनिक सिरे बाहरी जल में घुले रहते हैं।</text>
        </svg>"""
    }
]

# ----------------- 50 PRACTICE QUESTIONS -----------------
practice_questions = [
    {
        "q": "Which of the following allotropes of carbon is used as a lubricant and in pencil leads?",
        "q_hi": "पेंसिल लीड और लुब्रिकेंट के रूप में कार्बन के किस अपररूप का उपयोग किया जाता है?",
        "opts": ["Diamond", "Graphite", "C₆₀ Fullerene", "Coal"],
        "opts_hi": ["हीरा", "ग्रेफाइट (Graphite)", "C₆₀ फुलरीन", "कोयला"],
        "ans": 1,
        "sol": "Graphite has a layered hexagonal structure with weak Van der Waals forces holding the sheets together, making it soft and slippery, ideal for pencil leads and lubricants.",
        "sol_hi": "ग्रेफाइट में कमजोर वैन डेर वाल्स बलों द्वारा जुड़ी षटकोणीय परतें होती हैं, जिससे यह नरम और फिसलन भरा होता है। इसीलिए इसका उपयोग पेंसिल की लीड और स्नेहक (lubricants) के रूप में होता है।"
    },
    {
        "q": "What is the general formula for Alkenes?",
        "q_hi": "एल्कीन (Alkenes) का सामान्य सूत्र क्या है?",
        "opts": ["CnH₂n+₂", "CnH₂n", "CnH₂n-₂", "CnH₂n+₁"],
        "opts_hi": ["CnH₂n+₂", "CnH₂n (CnH₂n)", "CnH₂n-₂", "CnH₂n+₁"],
        "ans": 1,
        "sol": "Alkanes have the general formula CnH₂n+₂. Alkenes containing one double bond have CnH₂n. Alkynes containing one triple bond have CnH₂n-₂.",
        "sol_hi": "एल्केन का सामान्य सूत्र CnH₂n+₂ होता है। एक द्वि-आबंध वाले एल्कीन का सूत्र CnH₂n होता है। एक त्रि-आबंध वाले एल्काइन का सूत्र CnH₂n-₂ होता है।"
    },
    {
        "q": "Which of the following compounds is the chief constituent of Natural Gas and Biogas?",
        "q_hi": "निम्नलिखित में से कौन सा यौगिक प्राकृतिक गैस और बायोगैस का मुख्य घटक है?",
        "opts": ["Ethane", "Methane", "Propane", "Butane"],
        "opts_hi": ["इथेन", "मीथेन (Methane)", "प्रोपेन", "ब्यूटेन"],
        "ans": 1,
        "sol": "Methane (CH₄) constitutes up to 75-90% of natural gas and is the primary combustible component in biogas.",
        "sol_hi": "मीथेन (CH₄) प्राकृतिक गैस का 75-90% तक हिस्सा बनाता है और बायोगैस में प्राथमिक दहनशील घटक है।"
    },
    {
        "q": "The unique property of carbon to bond with other carbon atoms to form long chains is called:",
        "q_hi": "कार्बन परमाणुओं का आपस में जुड़कर लंबी श्रृंखलाएं बनाने का विशिष्ट गुण कहलाता है:",
        "opts": ["Tetravalency", "Catenation", "Allotropy", "Isomerism"],
        "opts_hi": ["चतुःसंयोजकता", "श्रृंखलन (Catenation)", "अपररूपता", "समावयवता"],
        "ans": 1,
        "sol": "Catenation is the self-linking of carbon atoms through strong covalent bonds, enabling the creation of infinite chains, branches, and rings.",
        "sol_hi": "श्रृंखलन (Catenation) मजबूत सहसंयोजक आबंधों के माध्यम से कार्बन परमाणुओं का आपस में जुड़ने का गुण है, जिससे असीमित श्रृंखलाओं और वलयों का निर्माण संभव होता है।"
    },
    {
        "q": "Which gas is evolved with brisk effervescence when ethanoic acid reacts with sodium bicarbonate?",
        "q_hi": "जब इथेनॉइक अम्ल सोडियम बाइकार्बोनेट के साथ अभिक्रिया करता है तो तेज बुदबुदाहट के साथ कौन सी गैस निकलती है?",
        "opts": ["Hydrogen", "Carbon dioxide", "Oxygen", "Carbon monoxide"],
        "opts_hi": ["हाइड्रोजन", "कार्बन डाइऑक्साइड (Carbon dioxide)", "ऑक्सीजन", "कार्बन मोनोऑक्साइड"],
        "ans": 1,
        "sol": "Ethanoic acid reacts with sodium bicarbonate (NaHCO₃) to form sodium acetate, water, and Carbon Dioxide gas (CH₃COOH + NaHCO₃ &rarr; CH₃COONa + H₂O + CO₂).",
        "sol_hi": "इथेनॉइक अम्ल सोडियम बाइकार्बोनेट (NaHCO₃) के साथ अभिक्रिया करके सोडियम एसीटेट, जल और कार्बन डाइऑक्साइड गैस बनाता है (CH₃COOH + NaHCO₃ &rarr; CH₃COONa + H₂O + CO₂)।"
    },
    {
        "q": "What is the IUPAC name of the compound CH₃COCH₃?",
        "q_hi": "यौगिक CH₃COCH₃ का IUPAC नाम क्या है?",
        "opts": ["Propanone", "Ethanal", "Propanal", "Propanol"],
        "opts_hi": ["प्रोपेनोन (Propanone)", "इथेनैल", "प्रोपेनैल", "प्रोपेनॉल"],
        "ans": 0,
        "sol": "CH₃COCH₃ contains three carbon atoms and a ketone functional group (-CO-), hence named Propanone (commonly known as Acetone).",
        "sol_hi": "CH₃COCH₃ में तीन कार्बन परमाणु और एक कीटोन कार्यात्मक समूह (-CO-) होता है, इसलिए इसे प्रोपेनोन कहा जाता है (आमतौर पर इसे एसीटोन के रूप में जाना जाता है)।"
    },
    {
        "q": "Which catalyst is used in the hydrogenation of vegetable oils to form vanaspati ghee?",
        "q_hi": "वनस्पति तेलों से वनस्पति घी बनाने के लिए हाइड्रोजनीकरण में किस उत्प्रेरक का उपयोग किया जाता है?",
        "opts": ["Iron", "Nickel", "Copper", "Manganese dioxide"],
        "opts_hi": ["लोहा", "निकेल (Nickel)", "तांबा", "मैंगनीज डाइऑक्साइड"],
        "ans": 1,
        "sol": "Hydrogenation is an addition reaction where hydrogen gas is passed through unsaturated vegetable oils in the presence of a Nickel (Ni) or Palladium (Pd) catalyst.",
        "sol_hi": "हाइड्रोजनीकरण एक संकलन अभिक्रिया है जिसमें निकेल (Ni) या पैलेडियम (Pd) उत्प्रेरक की उपस्थिति में असंतृप्त वनस्पति तेलों से हाइड्रोजन गैस गुजारी जाती है।"
    },
    {
        "q": "Which of the following organic compounds is the main constituent of vinegar?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बनिक यौगिक सिरके (vinegar) का मुख्य घटक है?",
        "opts": ["Formic acid", "Acetic acid", "Citric acid", "Lactic acid"],
        "opts_hi": ["फॉार्मिक अम्ल", "एसिटिक अम्ल / इथेनॉइक अम्ल (Acetic acid)", "साइट्रिक अम्ल", "लैक्टिक अम्ल"],
        "ans": 1,
        "sol": "Vinegar is a 5-8% aqueous solution of Acetic acid (also known as Ethanoic acid, CH₃COOH).",
        "sol_hi": "सिरका एसिटिक अम्ल (जिसे इथेनॉइक अम्ल, CH₃COOH भी कहा जाता है) का 5-8% जलीय विलयन होता है।"
    },
    {
        "q": "Soaps form an insoluble precipitate with hard water due to reaction with which ions?",
        "q_hi": "कठोर जल के साथ साबुन किस आयन की अभिक्रिया के कारण अघुलनशील अवक्षेप बनाता है?",
        "opts": ["Sodium and Potassium ions", "Calcium and Magnesium ions", "Iron and Aluminum ions", "Chloride and Sulfate ions"],
        "opts_hi": ["सोडियम और पोटेशियम आयन", "कैल्शियम और मैग्नीशियम आयन (Calcium and Magnesium)", "लोहा और एल्युमिनियम आयन", "क्लोराइड और सल्फेट आयन"],
        "ans": 1,
        "sol": "Hard water contains soluble Calcium (Ca²⁺) and Magnesium (Mg²⁺) salts. Soap reacts with these ions to form insoluble calcium and magnesium fatty acid salts, called scum.",
        "sol_hi": "कठोर जल में घुलनशील कैल्शियम (Ca²⁺) और मैग्नीशियम (Mg²⁺) लवण होते हैं। साबुन इन आयनों के साथ क्रिया करके वसा अम्लों के अघुलनशील लवण बनाता है, जिसे स्कम कहा जाता है।"
    },
    {
        "q": "Which carbon allotrope has a cage-like structure resembling a geodesic dome?",
        "q_hi": "किस कार्बन अपररूप की संरचना भू-गणितीय गुंबद (geodesic dome) जैसी पिंजरेनुमा होती है?",
        "opts": ["Diamond", "Graphite", "Buckminsterfullerene", "Lonsdaleite"],
        "opts_hi": ["हीरा", "ग्रेफाइट", "बकमिनस्टरफुलरीन (Buckminsterfullerene)", "लोंसडेलाइट"],
        "ans": 2,
        "sol": "Buckminsterfullerene (C₆0) is a spherical cage structure composed of 60 carbon atoms forming interconnected hexagons and pentagons.",
        "sol_hi": "बकमिनस्टरफुलरीन (C₆₀) 60 कार्बन परमाणुओं से बना एक गोलाकार पिंजरे जैसा अपररूप है, जिसकी संरचना फुटबॉल या भू-गणितीय गुंबद जैसी होती है।"
    },
    {
        "q": "A homologous series of organic compounds differs by which chemical unit?",
        "q_hi": "कार्बनिक यौगिकों की एक समजातीय श्रेणी किस रासायनिक इकाई द्वारा भिन्न होती है?",
        "opts": ["-CH-", "-CH₂-", "-CH₃-", "-C₂H₅-"],
        "opts_hi": ["-CH-", "-CH₂- (-CH₂-)", "-CH₃-", "-C₂H₅-"],
        "ans": 1,
        "sol": "Successive members of a homologous series differ by a single carbon and two hydrogen atoms (-CH₂- unit) and 14 u in molecular mass.",
        "sol_hi": "एक समजातीय श्रेणी के क्रमागत सदस्य हमेशा एक कार्बन और दो हाइड्रोजन परमाणुओं (-CH₂- इकाई) और आणविक द्रव्यमान में 14 u से भिन्न होते हैं।"
    },
    {
        "q": "What is the common name of Ethanoic Acid?",
        "q_hi": "इथेनॉइक अम्ल का सामान्य नाम क्या है?",
        "opts": ["Formic Acid", "Acetic Acid", "Oxalic Acid", "Tartaric Acid"],
        "opts_hi": ["फॉर्मिक अम्ल", "एसिटिक अम्ल (Acetic Acid)", "ऑक्सेलिक अम्ल", "टार्टरिक अम्ल"],
        "ans": 1,
        "sol": "Ethanoic acid (CH₃COOH) is commonly known as Acetic acid. A 5-8% solution of acetic acid in water is called vinegar.",
        "sol_hi": "इथेनॉइक अम्ल (CH₃COOH) को सामान्यतः एसिटिक अम्ल कहा जाता है। पानी में एसिटिक अम्ल के 5-8% विलयन को सिरका कहते हैं।"
    },
    {
        "q": "Which chemical is added to ethanol to prepare 'Denatured Alcohol'?",
        "q_hi": "विकृत ऐल्कोहॉल (Denatured Alcohol) तैयार करने के लिए इथेनॉल में कौन सा रसायन मिलाया जाता है?",
        "opts": ["Methanol", "Ethanoic acid", "Sodium hydroxide", "Acetone"],
        "opts_hi": ["मेथनॉल (Methanol)", "इथेनॉइक अम्ल", "सोडियम हाइड्रोक्साइड", "एसीटोन"],
        "ans": 0,
        "sol": "Methanol (CH₃OH) is highly toxic. It is added to industrial ethanol to denature it, preventing human consumption.",
        "sol_hi": "मेथनॉल (CH₃OH) अत्यंत विषैला होता है। इसे औद्योगिक इथेनॉल में मिलाकर विकृत किया जाता है ताकि इसका दुरुपयोग पीने के लिए न हो सके।"
    },
    {
        "q": "The reaction of an ester with sodium hydroxide to yield alcohol and sodium salt of carboxylic acid is called:",
        "q_hi": "एस्टर की सोडियम हाइड्रोक्साइड के साथ अभिक्रिया जिससे ऐल्कोहॉल और कार्बोक्सिलिक अम्ल का सोडियम लवण प्राप्त होता है, कहलाती है:",
        "opts": ["Esterification", "Saponification", "Dehydration", "Hydrogenation"],
        "opts_hi": ["एस्टरीकरण", "साबुनीकरण (Saponification)", "निर्जलीकरण", "हाइड्रोजनीकरण"],
        "ans": 1,
        "sol": "Saponification is the alkaline hydrolysis of esters, which is chemically the reaction used to manufacture soaps from fats and oils.",
        "sol_hi": "साबुनीकरण एस्टर का क्षारीय जलअपघटन है। रासायनिक रूप से इसी अभिक्रिया का उपयोग वसा और तेलों से साबुन बनाने के लिए किया जाता है।"
    },
    {
        "q": "Which of the following organic compounds is a gas commonly used for ripening fruits?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बनिक यौगिक एक गैस है जिसका उपयोग फलों को पकाने के लिए किया जाता है?",
        "opts": ["Methane", "Ethane", "Ethylene (Ethene)", "Acetylene (Ethyne)"],
        "opts_hi": ["मीथेन", "इथेन", "एथिलीन / एथीन (Ethylene)", "एसिटिलीन / एथाइन"],
        "ans": 2,
        "sol": "Ethylene (Ethene, C₂H₄) is a natural plant hormone that triggers fruit ripening. Calcium carbide reacts with moisture to release acetylene, which is also used artificially.",
        "sol_hi": "एथिलीन (एथीन, C₂H₄) एक प्राकृतिक पादप हार्मोन है जो फलों के पकने की क्रिया को तेज करता है। कैल्शियम कार्बाइड नमी से क्रिया कर एसिटिलीन छोड़ता है, जिसका उपयोग भी कृत्रिम रूप से किया जाता है।"
    },
    {
        "q": "What is the hybridisation of carbon atoms in Diamond and Graphite respectively?",
        "q_hi": "हीरे और ग्रेफाइट में कार्बन परमाणुओं का संकरण (hybridisation) क्रमशः क्या होता है?",
        "opts": ["sp³ and sp²", "sp² and sp³", "sp³ and sp", "sp and sp²"],
        "opts_hi": ["sp³ और sp² (sp³ and sp²)", "sp² और sp³", "sp³ और sp", "sp और sp²"],
        "ans": 0,
        "sol": "In Diamond, each carbon atom is bonded to 4 others via single bonds (sp³ hybridised). In Graphite, each carbon is bonded to 3 others in layers (sp² hybridised).",
        "sol_hi": "हीरे में, प्रत्येक कार्बन परमाणु 4 अन्य परमाणुओं से एकल आबंधों द्वारा जुड़ा होता है (sp³ संकरित)। ग्रेफाइट में, प्रत्येक कार्बन 3 अन्य परमाणुओं से परतों में जुड़ा होता है (sp² संकरित)।"
    },
    {
        "q": "Which organic compound is commonly known as Wood Spirit?",
        "q_hi": "किस कार्बनिक यौगिक को सामान्यतः 'काष्ठ स्पिरिट' (Wood Spirit) कहा जाता है?",
        "opts": ["Ethanol", "Methanol", "Formaldehyde", "Formic acid"],
        "opts_hi": ["इथेनॉल", "मेथनॉल (Methanol)", "फॉर्मेल्डिहाइड", "फॉर्मिक अम्ल"],
        "ans": 1,
        "sol": "Methanol (CH₃OH) was historically produced by the destructive distillation of wood, which is why it is called wood spirit.",
        "sol_hi": "मेथनॉल (CH₃OH) को ऐतिहासिक रूप से लकड़ी के भंजक आसवन (destructive distillation) द्वारा प्राप्त किया जाता था, इसीलिए इसे काष्ठ स्पिरिट (Wood Spirit) कहा जाता है।"
    },
    {
        "q": "Saturated hydrocarbons burn with which type of flame during complete combustion?",
        "q_hi": "पूर्ण दहन के दौरान संतृप्त हाइड्रोकार्बन किस प्रकार की लौ के साथ जलते हैं?",
        "opts": ["Yellow, sooty flame", "Clean blue flame", "Green flame", "Red, smoky flame"],
        "opts_hi": ["पीली, कज्जली लौ", "स्वच्छ नीली लौ (Clean blue flame)", "हरी लौ", "लाल, धुएँ वाली लौ"],
        "ans": 1,
        "sol": "Saturated hydrocarbons (like LPG/methane) have a high ratio of hydrogen to carbon and undergo complete combustion, producing a clean blue flame.",
        "sol_hi": "संतृप्त हाइड्रोकार्बन (जैसे एलपीजी/मीथेन) में कार्बन की तुलना में हाइड्रोजन का अनुपात अधिक होता है और इनका पूर्ण दहन होता है, जिससे स्वच्छ नीली लौ पैदा होती है।"
    },
    {
        "q": "Unsaturated hydrocarbons burn with a yellow sooty flame due to:",
        "q_hi": "असंतृप्त हाइड्रोकार्बन पीली कज्जली लौ के साथ जलते हैं, इसका कारण क्या है?",
        "opts": ["Presence of moisture", "Low percentage of carbon", "Incomplete combustion due to high carbon content", "Presence of sulfur impurities"],
        "opts_hi": ["नमी की उपस्थिति", "कार्बन का कम प्रतिशत", "उच्च कार्बन सामग्री के कारण अपूर्ण दहन (Incomplete combustion)", "सल्फर की अशुद्धियों की उपस्थिति"],
        "ans": 2,
        "sol": "Unsaturated hydrocarbons (alkenes, alkynes) have a higher percentage of carbon. Air supply is often insufficient to burn this carbon completely, leading to soot particles that glow yellow.",
        "sol_hi": "असंतृप्त हाइड्रोकार्बन (एल्कीन, एल्काइन) में कार्बन का प्रतिशत अधिक होता है। उपलब्ध हवा इस कार्बन को पूरी तरह जलाने के लिए अक्सर अपर्याप्त होती है, जिससे न जले कार्बन के कण गर्म होकर पीले रंग में चमकते हैं (कज्जली लौ)।"
    },
    {
        "q": "Which functional group is present in the compound Propanone?",
        "q_hi": "प्रोपेनोन (Propanone) यौगिक में कौन सा कार्यात्मक समूह उपस्थित होता है?",
        "opts": ["Alcohol", "Aldehyde", "Ketone", "Carboxylic acid"],
        "opts_hi": ["ऐल्कोहॉल", "ऐल्डिहाइड", "कीटोन (Ketone)", "कार्बोक्सिलिक अम्ल"],
        "ans": 2,
        "sol": "Propanone (CH₃COCH₃) belongs to the Ketone family, containing the carbonyl group (-CO-) bonded to two carbon groups.",
        "sol_hi": "प्रोपेनोन (CH₃COCH₃) कीटोन वर्ग से संबंधित है, जिसमें दो कार्बन समूहों से आबंधित कार्बोनिल समूह (-CO-) होता है।"
    },
    {
        "q": "The reaction of ethanol with hot concentrated sulfuric acid at 443 K yields:",
        "q_hi": "443 K पर गर्म सांद्र सल्फ्यूरिक अम्ल के साथ इथेनॉल की अभिक्रिया से क्या प्राप्त होता है?",
        "opts": ["Ethene", "Ethane", "Diethyl ether", "Ethanoic acid"],
        "opts_hi": ["एथीन (Ethene)", "इथेन", "डाईइथाइल ईथर", "इथेनॉइक अम्ल"],
        "ans": 0,
        "sol": "Concentrated H₂SO₄ acts as a dehydrating agent. It removes water from ethanol at 443 K to produce Ethene (CH₃-CH₂-OH &rarr; CH₂=CH₂ + H₂O).",
        "sol_hi": "सांद्र H₂SO₄ एक निर्जलीकारक (dehydrating agent) के रूप में कार्य करता है। यह 443 K पर इथेनॉल से जल अणु निकालकर एथीन (CH₂=CH₂) बनाता है।"
    },
    {
        "q": "Which chemical substance is formed when ethanol is oxidized by alkaline potassium permanganate?",
        "q_hi": "क्षारीय पोटेशियम परमैंगनेट द्वारा इथेनॉल को ऑक्सीकृत करने पर कौन सा रासायनिक पदार्थ बनता है?",
        "opts": ["Ethanal", "Ethanoic Acid", "Methane", "Carbon dioxide"],
        "opts_hi": ["इथेनैल", "इथेनॉइक अम्ल (Ethanoic Acid)", "मीथेन", "कार्बन डाइऑक्साइड"],
        "ans": 1,
        "sol": "Alkaline KMnO₄ is a strong oxidizing agent. It oxidizes ethanol (C₂H₅OH) completely into ethanoic acid (CH₃COOH).",
        "sol_hi": "क्षारीय KMnO₄ एक प्रबल ऑक्सीकारक है। यह इथेनॉल (C₂H₅OH) को पूरी तरह से इथेनॉइक अम्ल (CH₃COOH) में ऑक्सीकृत कर देता है।"
    },
    {
        "q": "The cleansing action of soap is based on the formation of:",
        "q_hi": "साबुन की शोधन क्रिया किसके निर्माण पर आधारित है?",
        "opts": ["Precipitate", "Micelles", "Emulsion", "Acidic solution"],
        "opts_hi": ["अवक्षेप", "मिसेल (Micelles)", "पायस (Emulsion)", "अम्लीय विलयन"],
        "ans": 1,
        "sol": "Soap molecules form spherical structures called micelles around dirt/oil particles, capturing the dirt in the hydrophobic core, which is then washed away.",
        "sol_hi": "साबुन के अणु गंदगी/तेल के कणों के चारों ओर गोलाकार संरचनाएं बनाते हैं जिन्हें मिसेल कहा जाता है। ये गंदगी को केंद्र में फंसा लेते हैं, जिसे पानी से आसानी से धो दिया जाता है।"
    },
    {
        "q": "What is the structural formula of Ethanoic Acid?",
        "q_hi": "इथेनॉइक अम्ल का संरचनात्मक सूत्र क्या है?",
        "opts": ["CH₃OH", "CH₃COOH", "C₂H₅OH", "HCHO"],
        "opts_hi": ["CH₃OH", "CH₃COOH (CH₃COOH)", "C₂H₅OH", "HCHO"],
        "ans": 1,
        "sol": "Ethanoic acid is CH₃COOH. CH₃OH is methanol, C₂H₅OH is ethanol, and HCHO is formaldehyde.",
        "sol_hi": "इथेनॉइक अम्ल CH₃COOH है। CH₃OH मेथनॉल है, C₂H₅OH इथेनॉल है, और HCHO फॉर्मेल्डिहाइड है।"
    },
    {
        "q": "The covalent bonds in a molecule of Ethane (C₂H₆) total:",
        "q_hi": "इथेन (C₂H₆) के एक अणु में कुल सहसंयोजक आबंधों की संख्या होती है:",
        "opts": ["6", "7", "8", "9"],
        "opts_hi": ["6", "7 (7)", "8", "9"],
        "ans": 1,
        "sol": "In Ethane (CH₃-CH₃), there are 6 C-H single bonds and 1 C-C single bond, totaling 7 covalent bonds.",
        "sol_hi": "इथेन (CH₃-CH₃) में, 6 C-H एकल आबंध और 1 C-C एकल आबंध होते हैं, जिससे कुल सहसंयोजक आबंधों की संख्या 7 होती है।"
    },
    {
        "q": "Which allotrope of carbon has a structure made of layers of carbon atoms arranged in hexagons?",
        "q_hi": "कार्बन के किस अपररूप की संरचना षटकोणीय परतों के रूप में व्यवस्थित कार्बन परमाणुओं से बनी होती है?",
        "opts": ["Diamond", "Graphite", "Fullerene", "Coal"],
        "opts_hi": ["हीरा", "ग्रेफाइट (Graphite)", "फुलरीन", "कोयला"],
        "ans": 1,
        "sol": "Graphite is composed of flat layers of carbon atoms. Each atom is bonded to three others in a hexagonal pattern.",
        "sol_hi": "ग्रेफाइट कार्बन परमाणुओं की समतल परतों से बना होता है। प्रत्येक परमाणु एक षटकोणीय पैटर्न में तीन अन्य परमाणुओं से आबंधित होता है।"
    },
    {
        "q": "Esterification is the reaction between an alcohol and a:",
        "q_hi": "एस्टरीकरण (Esterification) ऐल्कोहॉल और किसके बीच की अभिक्रिया है?",
        "opts": ["Metal hydroxide", "Mineral acid", "Carboxylic acid", "Ketone"],
        "opts_hi": ["धातु हाइड्रोक्साइड", "खनिज अम्ल", "कार्बोक्सिलिक अम्ल (Carboxylic acid)", "कीटोन"],
        "ans": 2,
        "sol": "Esterification occurs when a carboxylic acid reacts with an alcohol in the presence of an acid catalyst (like conc. H₂SO₄) to form a sweet-smelling ester and water.",
        "sol_hi": "एस्टरीकरण तब होता है जब एक कार्बोक्सिलिक अम्ल किसी अम्ल उत्प्रेरक (जैसे सांद्र H₂SO₄) की उपस्थिति में ऐल्कोहॉल के साथ अभिक्रिया करके मीठी गंध वाला एस्टर और जल बनाता है।"
    },
    {
        "q": "Which of the following organic compounds is also known as Glacial Acetic Acid?",
        "q_hi": "निम्नलिखित में से किस कार्बनिक यौगिक को 'ग्लेशियर एसिटिक अम्ल' (Glacial Acetic Acid) भी कहा जाता है?",
        "opts": ["Pure Ethanoic Acid", "Dilute Acetic Acid", "Ethanol", "Formic Acid"],
        "opts_hi": ["शुद्ध इथेनॉइक अम्ल (Pure Ethanoic Acid)", "तनु एसिटिक अम्ल", "इथेनॉल", "फॉर्मिक अम्ल"],
        "ans": 0,
        "sol": "Pure ethanoic acid (100% concentration) has a freezing point of 16.6°C. It freezes into ice-like crystals in cold climates, hence called Glacial Acetic Acid.",
        "sol_hi": "शुद्ध इथेनॉइक अम्ल (100% सांद्रता) का हिमांक 16.6°C होता है। यह ठंडे मौसम में बर्फ जैसे क्रिस्टल में जम जाता है, इसीलिए इसे ग्लेशियल एसिटिक अम्ल कहा जाता है।"
    },
    {
        "q": "How many double bonds are present in a molecule of Benzene (C₆H₆)?",
        "q_hi": "बेंजीन (C₆H₆) के एक अणु में कितने द्वि-आबंध उपस्थित होते हैं?",
        "opts": ["1", "2", "3", "6"],
        "opts_hi": ["1", "2", "3 (3)", "6"],
        "ans": 2,
        "sol": "Benzene has a cyclic ring of 6 carbon atoms with alternating single and double bonds, meaning it contains exactly 3 double bonds.",
        "sol_hi": "बेंजीन में 6 कार्बन परमाणुओं की एक चक्रीय वलय होती है जिसमें एकांतर एकल और द्वि-आबंध होते हैं, अर्थात इसमें ठीक 3 द्वि-आबंध होते हैं।"
    },
    {
        "q": "Which gas is released when ethanol reacts with active Sodium metal?",
        "q_hi": "जब इथेनॉल सक्रिय सोडियम धातु के साथ अभिक्रिया करता है तो कौन सी गैस मुक्त होती है?",
        "opts": ["Oxygen", "Carbon dioxide", "Hydrogen", "Methane"],
        "opts_hi": ["ऑक्सीजन", "कार्बन डाइऑक्साइड", "हाइड्रोजन (Hydrogen)", "मीथेन"],
        "ans": 2,
        "sol": "Ethanol reacts with sodium to release Hydrogen gas and form sodium ethoxide (2C₂H₅OH + 2Na &rarr; 2C₂H₅ONa + H₂).",
        "sol_hi": "इथेनॉल सोडियम के साथ अभिक्रिया करके हाइड्रोजन गैस मुक्त करता है और सोडियम इथॉक्साइड बनाता है (2C₂H₅OH + 2Na &rarr; 2C₂H₅ONa + H₂)।"
    },
    {
        "q": "The soot in the flame of burning unsaturated compounds is composed of:",
        "q_hi": "असंतृप्त यौगिकों के जलने पर लौ में मिलने वाली कािख (soot) किससे बनी होती है?",
        "opts": ["Unburnt carbon particles", "Carbon monoxide", "Ash", "Hydrocarbons"],
        "opts_hi": ["बिना जले कार्बन कण (Unburnt carbon particles)", "कार्बन मोनोऑक्साइड", "राख", "हाइड्रोकार्बन"],
        "ans": 0,
        "sol": "Soot consists of extremely fine unburnt carbon particles produced due to incomplete combustion of high-carbon unsaturated organic compounds.",
        "sol_hi": "कािख (Soot) अत्यधिक महीन बिना जले कार्बन के कणों से बनी होती है जो उच्च कार्बन युक्त असंतृप्त यौगिकों के अपूर्ण दहन के कारण पैदा होते हैं।"
    },
    {
        "q": "What is the suffix used in IUPAC nomenclature for Aldehydes?",
        "q_hi": "ऐल्डिहाइड के लिए IUPAC नामकरण में किस अनुलग्न (suffix) का उपयोग किया जाता है?",
        "opts": ["-ol", "-al", "-one", "-oic acid"],
        "opts_hi": ["-ol (-ऑल)", "-al (-ऐल)", "-one (-ओन)", "-oic acid (-ओइक अम्ल)"],
        "ans": 1,
        "sol": "The suffix for aldehydes (-CHO group) is -al (e.g., methanal, ethanal). The suffix -ol is for alcohols, -one is for ketones, and -oic acid is for carboxylic acids.",
        "sol_hi": "ऐल्डिहाइड (-CHO समूह) के लिए अनुलग्न -al (-ऐल) है। -ol ऐल्कोहॉल के लिए, -one कीटोन के लिए, और -oic acid कार्बोक्सिलिक अम्ल के लिए होता है।"
    },
    {
        "q": "Which of the following organic compounds is the simplest alkene?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बनिक यौगिक सबसे सरल एल्कीन (simplest alkene) है?",
        "opts": ["Methane", "Methene", "Ethene", "Ethyne"],
        "opts_hi": ["मीथेन", "मीथीन (Methene)", "एथीन (Ethene)", "एथाइन"],
        "ans": 2,
        "sol": "Alkenes require a carbon-carbon double bond (C=C). Since methane has only 1 carbon, methene cannot exist. The simplest alkene is Ethene (C₂H₄).",
        "sol_hi": "एल्कीन में कार्बन-कार्बन द्वि-आबंध (C=C) का होना आवश्यक है। चूंकि मीथेन में केवल 1 कार्बन होता है, इसलिए मीथीन का अस्तित्व संभव नहीं है। सबसे सरल एल्कीन एथीन (C₂H₄) है।"
    },
    {
        "q": "What is the common name of Methanal?",
        "q_hi": "मेथनेल (Methanal) का सामान्य नाम क्या है?",
        "opts": ["Formaldehyde", "Acetaldehyde", "Formic acid", "Acetone"],
        "opts_hi": ["फॉर्मेल्डिहाइड (Formaldehyde)", "एसिटैल्डिहाइड", "फॉर्मिक अम्ल", "एसीटोन"],
        "ans": 0,
        "sol": "Methanal (HCHO) is commonly known as Formaldehyde. A 40% aqueous solution of formaldehyde is called Formalin, used to preserve biological specimens.",
        "sol_hi": "मेथनेल (HCHO) को आमतौर पर फॉर्मेल्डिहाइड कहा जाता है। फॉर्मेल्डिहाइड के 40% जलीय विलयन को फॉर्मेलिन कहा जाता है, जिसका उपयोग जैविक नमूनों को सुरक्षित रखने के लिए किया जाता है।"
    },
    {
        "q": "Detergents are chemically:",
        "q_hi": "अपमार्जक (Detergents) रासायनिक रूप से क्या होते हैं?",
        "opts": ["Sodium salts of fatty acids", "Sodium salts of sulfonic acids or ammonium salts with chlorides/bromides", "Calcium salts of fatty acids", "Potassium salts of long-chain fatty acids"],
        "opts_hi": ["वसा अम्लों के सोडियम लवण", "सल्फोनिक अम्लों के सोडियम लवण या क्लोराइड/ब्रोमाइड युक्त अमोनियम लवण (Sodium salts of sulfonic acids)", "वसा अम्लों के कैल्शियम लवण", "लंबी श्रृंखला वाले वसा अम्लों के पोटेशियम लवण"],
        "ans": 1,
        "sol": "Detergents are ammonium or sulfonate salts of long-chain carboxylic acids. Their charged ends do not form precipitate (scum) with Ca²⁺ and Mg²⁺ in hard water.",
        "sol_hi": "अपमार्जक लंबी श्रृंखला वाले कार्बोक्सिलिक अम्लों के अमोनियम या सल्फोनेट लवण होते हैं। इनके आवेशित सिरे कठोर जल में Ca²⁺ और Mg²⁺ के साथ अवक्षेप (स्कम) नहीं बनाते हैं।"
    },
    {
        "q": "Which of the following compounds is formed during the reaction of ethanol with ethanoic acid in the presence of acid?",
        "q_hi": "अम्ल की उपस्थिति में इथेनॉल की इथेनॉइक अम्ल के साथ अभिक्रिया के दौरान निम्नलिखित में से कौन सा यौगिक बनता है?",
        "opts": ["Ethyl ethanoate", "Methyl ethanoate", "Diethyl ether", "Ethyl acetate only"],
        "opts_hi": ["एथिल इथेनोएट (Ethyl ethanoate)", "मेथिल इथेनोएट", "डाईइथाइल ईथर", "केवल एथिल एसीटेट"],
        "ans": 0,
        "sol": "Ethanol (C₂H₅OH) reacts with ethanoic acid (CH₃COOH) to form Ethyl Ethanoate (an ester) and water. (CH₃COOH + C₂H₅OH &rarr; CH₃COOC₂H₅ + H₂O).",
        "sol_hi": "इथेनॉल (C₂H₅OH) इथेनॉइक अम्ल (CH₃COOH) के साथ अभिक्रिया करके एथिल इथेनोएट (एक एस्टर) और जल बनाता है (CH₃COOH + C₂H₅OH &rarr; CH₃COOC₂H₅ + H₂O)। इसे एथिल एसीटेट भी कहा जाता है।"
    },
    {
        "q": "Which gas is evolved during the combustion of coal and petroleum in insufficient air, leading to poisoning?",
        "q_hi": "हवा की कमी में कोयले और पेट्रोलियम के दहन के दौरान कौन सी गैस निकलती है, जिससे विषाक्तता होती है?",
        "opts": ["Carbon dioxide", "Carbon monoxide", "Sulfur dioxide", "Nitrous oxide"],
        "opts_hi": ["कार्बन डाइऑक्साइड", "कार्बन मोनोऑक्साइड (Carbon monoxide)", "सल्फर डाइऑक्साइड", "नाइट्रस ऑक्साइड"],
        "ans": 1,
        "sol": "Incomplete combustion of carbon fuels due to limited oxygen produces Carbon Monoxide (CO), which binds strongly to hemoglobin, causing asphyxiation and poisoning.",
        "sol_hi": "सीमित ऑक्सीजन के कारण कार्बन ईंधनों के अपूर्ण दहन से कार्बन मोनोऑक्साइड (CO) उत्पन्न होती है, जो हीमोग्लोबिन से मजबूती से जुड़कर दम घुटने और विषाक्तता का कारण बनती है।"
    },
    {
        "q": "How many covalent bonds are present in a molecule of Pentane (C₅H₁₂)?",
        "q_hi": "पेन्टेन (C₅H₁₂) के एक अणु में कुल कितने सहसंयोजक आबंध उपस्थित होते हैं?",
        "opts": ["12", "14", "16", "18"],
        "opts_hi": ["12", "14", "16 (16)", "18"],
        "ans": 2,
        "sol": "In Pentane, there are 4 C-C bonds and 12 C-H bonds, totaling 16 covalent bonds.",
        "sol_hi": "पेन्टेन में, 4 C-C आबंध और 12 C-H आबंध होते हैं, जिससे कुल सहसंयोजक आबंधों की संख्या 16 होती है।"
    },
    {
        "q": "What is the common name of Ethyne?",
        "q_hi": "इथाइन (Ethyne) का सामान्य नाम क्या है?",
        "opts": ["Ethylene", "Acetylene", "Propylene", "Butylene"],
        "opts_hi": ["एथिलीन", "एसिटिलीन (Acetylene)", "प्रोपलीन", "ब्यूटिलीन"],
        "ans": 1,
        "sol": "Ethyne (C₂H₂) is commonly known as Acetone or Acetylene, which is used in oxy-acetylene gas torches for welding metals.",
        "sol_hi": "इथाइन (C₂H₂) को सामान्यतः एसिटिलीन (Acetylene) कहा जाता है, जिसका उपयोग धातुओं की वेल्डिंग के लिए ऑक्सी-एसिटिलीन गैस टॉर्च में किया जाता है।"
    },
    {
        "q": "Which of the following organic compounds is a major component of LPG (Liquefied Petroleum Gas)?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बनिक यौगिक एलपीजी (तरलीकृत पेट्रोलियम गैस) का एक मुख्य घटक है?",
        "opts": ["Methane", "Ethane", "Propane and Butane", "Hexane"],
        "opts_hi": ["मीथेन", "इथेन", "प्रोपेन और ब्यूटेन (Propane and Butane)", "हेक्सेन"],
        "ans": 2,
        "sol": "LPG is primarily a mixture of Propane (C₃H₈) and Butane (C₄H₁₀), with Butane being the major component.",
        "sol_hi": "एलपीजी मुख्य रूप से प्रोपेन (C₃H₈) और ब्यूटेन (C₄H₁₀) का मिश्रण है, जिसमें ब्यूटेन प्रमुख घटक होता है।"
    },
    {
        "q": "Isomers are compounds that have the same:",
        "q_hi": "समावयवी (Isomers) वे यौगिक होते हैं जिनमें समान होता है:",
        "opts": ["Structural formula", "Molecular formula but different structures", "Chemical properties", "Melting points"],
        "opts_hi": ["संरचनात्मक सूत्र", "आणविक सूत्र लेकिन भिन्न संरचनाएं (Same molecular formula)", "रासायनिक गुण", "गलनांक"],
        "ans": 1,
        "sol": "Isomers are chemical compounds that share the same molecular formula (same number of atoms of each element) but differ in their structural arrangements.",
        "sol_hi": "समावयवी वे रासायनिक यौगिक होते हैं जिनका आणविक सूत्र समान होता है (प्रत्येक तत्व के परमाणुओं की संख्या समान) लेकिन उनके परमाणुओं की व्यवस्था (संरचनात्मक व्यवस्था) भिन्न होती है।"
    },
    {
        "q": "Which organic acid is present in ant stings causing burning pain?",
        "q_hi": "चींटी के डंक में कौन सा कार्बनिक अम्ल उपस्थित होता है जिससे जलन और दर्द होता है?",
        "opts": ["Acetic Acid", "Methanoic Acid", "Oxalic Acid", "Lactic Acid"],
        "opts_hi": ["एसिटिक अम्ल", "मेथेनॉइक अम्ल / फॉर्मिक अम्ल (Methanoic Acid)", "ऑक्सेलिक अम्ल", "लैक्टिक अम्ल"],
        "ans": 1,
        "sol": "Ant stings inject Formic acid, IUPAC name Methanoic acid (HCOOH), which causes sharp burning pain.",
        "sol_hi": "चींटी के डंक में फॉर्मिक अम्ल होता है, जिसका IUPAC नाम मेथेनॉइक अम्ल (HCOOH) है। यह त्वचा में जलन और दर्द पैदा करता है।"
    },
    {
        "q": "What type of reaction occurs when methane reacts with chlorine in the presence of sunlight?",
        "q_hi": "जब सूर्य के प्रकाश की उपस्थिति में मीथेन क्लोरीन के साथ अभिक्रिया करता है तो किस प्रकार की अभिक्रिया होती है?",
        "opts": ["Addition reaction", "Substitution reaction", "Oxidation reaction", "Combustion"],
        "opts_hi": ["संकलन अभिक्रिया", "प्रतिस्थापन अभिक्रिया (Substitution reaction)", "ऑक्सीकरण अभिक्रिया", "दहन"],
        "ans": 1,
        "sol": "Saturated hydrocarbons react with chlorine in sunlight via substitution, where chlorine atoms replace hydrogen atoms one by one (e.g., CH₄ + Cl₂ &rarr; CH₃Cl + HCl).",
        "sol_hi": "संतृप्त हाइड्रोकार्बन सूर्य के प्रकाश में क्लोरीन के साथ प्रतिस्थापन अभिक्रिया करते हैं, जिसमें क्लोरीन का परमाणु एक-एक करके हाइड्रोजन परमाणुओं को प्रतिस्थापित करता है (जैसे CH₄ + Cl₂ &rarr; CH₃Cl + HCl)।"
    },
    {
        "q": "The hydrophilic head of a soap molecule is:",
        "q_hi": "साबुन के अणु का जलरागी (hydrophilic) सिरा होता है:",
        "opts": ["Ionic and soluble in water", "Hydrocarbon chain and soluble in oil", "Non-polar", "Soluble in organic solvents only"],
        "opts_hi": ["आयनिक और जल में घुलनशील (Ionic and soluble in water)", "हाइड्रोकार्बन श्रृंखला और तेल में घुलनशील", "अध्रुवीय", "केवल कार्बनिक विलायक में घुलनशील"],
        "ans": 0,
        "sol": "The hydrophilic head is the ionic carboxylate group (-COO⁻Na⁺) which is polar and dissolves in water.",
        "sol_hi": "जलरागी सिरा आयनिक कार्बोक्सिलेट समूह (-COO⁻Na⁺) होता है जो ध्रुवीय होता है और जल के अणुओं के साथ आकर्षित होता है।"
    },
    {
        "q": "In soap micelles, the hydrophobic tails point towards:",
        "q_hi": "साबुन के मिसेल में, जलविरागी (hydrophobic) पूंछ किस ओर निर्देशित होती है?",
        "opts": ["Outward towards the water", "Inward towards the center of the micelle containing grease", "Random directions", "Along the surface of water"],
        "opts_hi": ["बाहर पानी की ओर", "अंदर मिसेल के केंद्र में मैल की ओर (Inward towards the center)", "यादृच्छिक दिशाओं में", "पानी की सतह के समानांतर"],
        "ans": 1,
        "sol": "The hydrophobic tails are hydrocarbon chains that repel water but dissolve in grease. They orient themselves inward, shielding themselves from water, capturing the grease drop.",
        "sol_hi": "जलविरागी पूंछ हाइड्रोकार्बन श्रृंखलाएं होती हैं जो पानी को पीछे धकेलती हैं लेकिन मैल/तेल में घुल जाती हैं। वे पानी से बचने के लिए अंदर की ओर निर्देशित होती हैं और मैल को केंद्र में जकड़ लेती हैं।"
    },
    {
        "q": "Which of the following compounds is an unsaturated cyclic hydrocarbon?",
        "q_hi": "निम्नलिखित में से कौन सा यौगिक एक असंतृप्त चक्रीय हाइड्रोकार्बन (unsaturated cyclic hydrocarbon) है?",
        "opts": ["Cyclohexane", "Benzene", "Hexane", "Cyclopentane"],
        "opts_hi": ["साइक्लोहेक्सेन", "बेंजीन (Benzene)", "हेक्सेन", "साइक्लोपेन्टेन"],
        "ans": 1,
        "sol": "Benzene (C₆H₆) is cyclic and unsaturated due to its double bonds. Cyclohexane and cyclopentane are cyclic but saturated (only single bonds). Hexane is open-chain.",
        "sol_hi": "बेंजीन (C₆H₆) चक्रीय है और इसमें द्वि-आबंधों के कारण यह असंतृप्त है। साइक्लोहेक्सेन और साइक्लोपेन्टेन चक्रीय हैं लेकिन संतृप्त हैं (केवल एकल आबंध)। हेक्सेन खुली श्रृंखला वाला है।"
    },
    {
        "q": "The functional group -CHO represents:",
        "q_hi": "कार्यात्मक समूह -CHO किसे दर्शाता है?",
        "opts": ["Alcohol", "Aldehyde", "Ketone", "Carboxylic acid"],
        "opts_hi": ["ऐल्कोहॉल", "ऐल्डिहाइड (Aldehyde)", "कीटोन", "कार्बोक्सिलिक अम्ल"],
        "ans": 1,
        "sol": "-CHO represents the Aldehyde group, which is always located at the end of a carbon chain.",
        "sol_hi": "-CHO ऐल्डिहाइड समूह को दर्शाता है, जो हमेशा कार्बन श्रृंखला के सिरे पर स्थित होता है।"
    },
    {
        "q": "Biogas contains what percentage of Methane gas?",
        "q_hi": "बायोगैस में मीथेन गैस का प्रतिशत लगभग कितना होता है?",
        "opts": ["10-20%", "30-40%", "50-75%", "90-95%"],
        "opts_hi": ["10-20%", "30-40%", "50-75% (50-75%)", "90-95%"],
        "ans": 2,
        "sol": "Biogas typically contains 50-75% methane (CH₄), 25-50% carbon dioxide (CO₂), and trace amounts of other gases like hydrogen sulfide.",
        "sol_hi": "बायोगैस में आमतौर पर 50-75% मीथेन (CH₄), 25-50% कार्बन डाइऑक्साइड (CO₂) और थोड़ी मात्रा में हाइड्रोजन सल्फाइड जैसी गैसें होती हैं।"
    },
    {
        "q": "Which of the following organic compounds is used as an antifreeze in automobile radiators?",
        "q_hi": "ऑटोमोबाइल रेडिएटर्स में एंटीफ्रीज (antifreeze) के रूप में निम्नलिखित में से किस कार्बनिक यौगिक का उपयोग किया जाता है?",
        "opts": ["Ethanol", "Ethylene Glycol", "Methanol", "Acetone"],
        "opts_hi": ["इथेनॉल", "इथिलीन ग्लाइकोल (Ethylene Glycol)", "मेथनॉल", "एसीटोन"],
        "ans": 1,
        "sol": "Ethylene Glycol (ethane-1,2-diol) is mixed with water in car radiators to lower the freezing point and raise the boiling point of the coolant.",
        "sol_hi": "इथिलीन ग्लाइकोल (ethane-1,2-diol) को कारों के रेडिएटर में पानी के साथ मिलाया जाता है ताकि यह एंटीफ्रीज के रूप में काम कर सके और हिमांक को कम व क्वथनांक को बढ़ा सके।"
    },
    {
        "q": "The reaction of vegetable oil with hydrogen in the presence of nickel is an example of:",
        "q_hi": "निकेल की उपस्थिति में वनस्पति तेल की हाइड्रोजन के साथ अभिक्रिया किसका एक उदाहरण है?",
        "opts": ["Substitution reaction", "Addition reaction", "Displacement reaction", "Dehydration"],
        "opts_hi": ["प्रतिस्थापन अभिक्रिया", "संकलन अभिक्रिया (Addition reaction)", "विस्थापन अभिक्रिया", "निर्जलीकरण"],
        "ans": 1,
        "sol": "Hydrogenation of unsaturated fats is a classic example of an addition reaction where hydrogen atoms add across carbon-carbon double bonds.",
        "sol_hi": "असंतृप्त वसा का हाइड्रोजनीकरण संकलन अभिक्रिया का एक उत्कृष्ट उदाहरण है जिसमें हाइड्रोजन के परमाणु कार्बन-कार्बन द्वि-आबंधों पर जुड़ जाते हैं।"
    }
]

# ----------------- 15 MOCK TEST QUESTIONS -----------------
mock_test_questions = [
    {
        "q": "Why is pure Ethanoic acid called Glacial Acetic Acid?",
        "q_hi": "शुद्ध इथेनॉइक अम्ल को 'ग्लेशियर एसिटिक अम्ल' क्यों कहा जाता है?",
        "opts": ["It is extracted from glaciers", "It freezes into ice-like crystals at cold room temperatures", "It reacts exothermically to melt ice", "It has a blue color similar to glaciers"],
        "opts_hi": ["यह ग्लेशियरों से निकाला जाता है", "यह ठंडे कमरे के तापमान पर बर्फ जैसे क्रिस्टल में जम जाता है (It freezes at low temperatures)", "यह बर्फ पिघलाने के लिए ऊष्मा छोड़ता है", "इसका रंग ग्लेशियर जैसा नीला होता है"],
        "ans": 1,
        "sol": "100% anhydrous acetic acid has a freezing point of 16.6°C (62°F). In winter or cool climates, it solidifies into crystalline forms resembling ice sheets.",
        "sol_hi": "100% निर्जल एसिटिक अम्ल का हिमांक 16.6°C (62°F) होता है। सर्दियों या ठंडे मौसम में यह जम कर बर्फ की चादरों जैसी संरचना बना लेता है।"
    },
    {
        "q": "An organic compound reacts with sodium metal to evolve a colorless gas that burns with a 'pop' sound. The compound is:",
        "q_hi": "एक कार्बनिक यौगिक सोडियम धातु के साथ अभिक्रिया करके एक रंगहीन गैस छोड़ता है जो 'पॉप' ध्वनि के साथ जलती है। वह यौगिक है:",
        "opts": ["Ethanoic acid only", "Ethanol only", "Both Ethanol and Ethanoic Acid", "Methane"],
        "opts_hi": ["केवल इथेनॉइक अम्ल", "केवल इथेनॉल", "इथेनॉल और इथेनॉइक अम्ल दोनों (Both Ethanol and Ethanoic Acid)", "मीथेन"],
        "ans": 2,
        "sol": "Both alcohols (like Ethanol) and carboxylic acids (like Ethanoic acid) react with active metals like Sodium to release Hydrogen gas (H₂), which ignites with a 'pop' sound.",
        "sol_hi": "ऐल्कोहॉल (जैसे इथेनॉल) और कार्बोक्सिलिक अम्ल (जैसे इथेनॉइक अम्ल) दोनों ही सोडियम जैसी सक्रिय धातुओं के साथ अभिक्रिया करके हाइड्रोजन गैस (H₂) मुक्त करते हैं, जो 'पॉप' ध्वनि के साथ जलती है।"
    },
    {
        "q": "Which of the following statements about Homologous Series is incorrect?",
        "q_hi": "समजातीय श्रेणी के बारे में निम्नलिखित में से कौन सा कथन गलत है?",
        "opts": ["The chemical properties remain similar", "The physical properties show a gradual gradation", "The successive members differ by 16 u in molecular mass", "The functional group is identical"],
        "opts_hi": ["रासायनिक गुण समान रहते हैं", "भौतिक गुण क्रमिक परिवर्तन दर्शाते हैं", "क्रमागत सदस्यों के आणविक द्रव्यमान में 16 u का अंतर होता है (Successive members differ by 16 u)", "कार्यात्मक समूह समान होता है"],
        "ans": 2,
        "sol": "Successive members in a homologous series differ by a -CH₂- unit, which has a mass of 14 u (C = 12 + H₂ = 2), not 16 u.",
        "sol_hi": "एक समजातीय श्रेणी के क्रमागत सदस्यों के बीच हमेशा -CH₂- समूह का अंतर होता है, जिसका आणविक द्रव्यमान 14 u होता है (C = 12 + H₂ = 2), न कि 16 u।"
    },
    {
        "q": "How many hexagons and pentagons of carbon are present in a molecule of Buckminsterfullerene (C₆₀)?",
        "q_hi": "बकमिनस्टरफुलरीन (C₆₀) के एक अणु में कार्बन के कितने षटकोण और पंचकोण उपस्थित होते हैं?",
        "opts": ["20 hexagons and 12 pentagons", "12 hexagons and 20 pentagons", "30 hexagons and 10 pentagons", "24 hexagons and 12 pentagons"],
        "opts_hi": ["20 षटकोण और 12 पंचकोण (20 hexagons and 12 pentagons)", "12 षटकोण और 20 पंचकोण", "30 षटकोण और 10 पंचकोण", "24 षटकोण और 12 पंचकोण"],
        "ans": 0,
        "sol": "C₆₀ fullerene is a truncated icosahedron containing exactly 20 hexagonal rings and 12 pentagonal rings of carbon atoms.",
        "sol_hi": "C₆0 फुलरीन की संरचना में ठीक 20 षटकोणीय (hexagonal) वलय और 12 पंचकोणीय (pentagonal) वलय शामिल होते हैं।"
    },
    {
        "q": "Saponification chemically involves the reaction of an ester with a strong base to yield:",
        "q_hi": "साबुनीकरण में रासायनिक रूप से एस्टर की एक मजबूत क्षार के साथ अभिक्रिया शामिल होती है, जिससे प्राप्त होता है:",
        "opts": ["Carboxylic acid and Water", "Soap (sodium salt of fatty acid) and Glycerol", "Ester and Alcohol", "Ether and Water"],
        "opts_hi": ["कारबोक्सिलिक अम्ल और जल", "साबुन (वसा अम्ल का सोडियम लवण) और ग्लिसरॉल (Soap and Glycerol)", "एस्टर और ऐल्कोहॉल", "ईथर और जल"],
        "ans": 1,
        "sol": "Esters (fats/triglycerides) react with NaOH to yield Glycerol (alcohol) and Sodium salts of long-chain fatty acids (soaps).",
        "sol_hi": "साबुनीकरण में एस्टर (वसा/ट्राइग्लिसराइड्स) NaOH के साथ क्रिया करके ग्लिसरॉल और वसा अम्लों के सोडियम लवण (साबुन) बनाते हैं।"
    },
    {
        "q": "Which of the following organic compounds will undergo an addition reaction?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बनिक यौगिक संकलन (addition) अभिक्रिया प्रदर्शित करेगा?",
        "opts": ["CH₄", "C₂H₆", "C₃H₆", "C₄H₁₀"],
        "opts_hi": ["CH₄", "C₂H₆", "C₃H₆ (C₃H₆)", "C₄H₁₀"],
        "ans": 2,
        "sol": "Addition reactions occur in unsaturated hydrocarbons (alkenes/alkynes). CH₄, C₂H₆, and C₄H₁₀ are saturated alkanes. C₃H₆ (Propene) is an unsaturated alkene and undergoes addition reactions.",
        "sol_hi": "संकलन (addition) अभिक्रियाएँ केवल असंतृप्त हाइड्रोकार्बनों (एल्कीन/एल्काइन) में होती हैं। CH₄, C₂H₆ और C₄H₁₀ संतृप्त एल्केन हैं। C₃H₆ (प्रोपिन) एक असंतृप्त एल्कीन है, इसलिए यह संकलन अभिक्रिया देगा।"
    },
    {
        "q": "The reaction: CH₃CH₂OH + CH₃COOH &rarr; CH₃COOCH₂CH₃ + H₂O in the presence of acid is called:",
        "q_hi": "अम्ल की उपस्थिति में होने वाली अभिक्रिया: CH₃CH₂OH + CH₃COOH &rarr; CH₃COOCH₂CH₃ + H₂O कहलाती है:",
        "opts": ["Saponification", "Esterification", "Hydrolysis", "Neutralization"],
        "opts_hi": ["साबुनीकरण", "एस्टरीकरण (Esterification)", "जलअपघटन", "उदासीनीकरण"],
        "ans": 1,
        "sol": "The reaction between a carboxylic acid (acetic acid) and an alcohol (ethanol) to form a sweet-smelling ester (ethyl ethanoate) is called Esterification.",
        "sol_hi": "कार्बोक्सिलिक अम्ल (एसिटिक अम्ल) और ऐल्कोहॉल (इथेनॉल) के बीच मीठी गंध वाले एस्टर (एथिल इथेनोएट) के निर्माण की अभिक्रिया को एस्टरीकरण कहते हैं।"
    },
    {
        "q": "Which of the following is not an allotrope of carbon?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बन का अपररूप नहीं है?",
        "opts": ["Diamond", "Graphite", "Carborundum", "Fullerene"],
        "opts_hi": ["हीरा", "ग्रेफाइट", "कार्बोरंडम (Carborundum)", "फुलरीन"],
        "ans": 2,
        "sol": "Diamond, Graphite, and Fullerenes are pure allotropic forms of carbon. Carborundum is Silicon Carbide (SiC), a chemical compound, not an allotrope.",
        "sol_hi": "हीरा, ग्रेफाइट और फुलरीन कार्बन के शुद्ध अपररूप हैं। कार्बोरंडम वास्तव में सिलिकॉन कार्बाइड (SiC) है, जो एक रासायनिक यौगिक है, अपररूप नहीं।"
    },
    {
        "q": "In the nomenclature of ketones, the suffix used is:",
        "q_hi": "कीटोन के नामकरण में किस अनुलग्न (suffix) का उपयोग किया जाता है?",
        "opts": ["-ol", "-al", "-one", "-oic"],
        "opts_hi": ["-ol", "-al", "-one (-one)", "-oic"],
        "ans": 2,
        "sol": "The suffix used for Ketones (-CO- group) is -one (pronounced as -own, e.g., Propanone). Suffix -ol is for alcohols, -al is for aldehydes.",
        "sol_hi": "कीटोन (-CO- समूह) के नामकरण में अनुलग्न -one (-ओन) का उपयोग किया जाता है (जैसे प्रोपेनोन)। -ol ऐल्कोहॉल के लिए और -al ऐल्डिहाइड के लिए होता है।"
    },
    {
        "q": "Which gas is evolved during the incomplete combustion of saturated hydrocarbons due to restricted air supply?",
        "q_hi": "हवा की सीमित आपूर्ति के कारण संतृप्त हाइड्रोकार्बन के अपूर्ण दहन से कौन सी गैस निकलती है?",
        "opts": ["Carbon dioxide", "Carbon monoxide", "Methane", "Sulfur dioxide"],
        "opts_hi": ["कार्बन डाइऑक्साइड", "कार्बन मोनोऑक्साइड (Carbon monoxide)", "मीथेन", "सल्फर डाइऑक्साइड"],
        "ans": 1,
        "sol": "Restricted oxygen supply leads to incomplete combustion of hydrocarbons, producing highly toxic Carbon Monoxide (CO) gas instead of Carbon Dioxide (CO₂).",
        "sol_hi": "ऑक्सीजन की सीमित आपूर्ति के कारण हाइड्रोकार्बनों का अपूर्ण दहन होता है, जिससे कार्बन डाइऑक्साइड (CO₂) के स्थान पर अत्यधिक विषैली कार्बन मोनोऑक्साइड (CO) गैस बनती है।"
    },
    {
        "q": "Detergents are preferred over soaps for washing clothes in hard water because:",
        "q_hi": "कठोर जल में कपड़े धोने के लिए साबुनों की तुलना में अपमार्जकों (detergents) को प्राथमिकता दी जाती है क्योंकि:",
        "opts": ["Detergents are cheaper than soaps", "Detergents do not form insoluble calcium/magnesium precipitates", "Detergents are biodegradable", "Detergents contain citric acid"],
        "opts_hi": ["अपमार्जक साबुनों से सस्ते होते हैं", "अपमार्जक अघुलनशील कैल्शियम/मैग्नीशियम अवक्षेप नहीं बनाते हैं (Detergents do not form scum)", "अपमार्जक जैव-निम्नीकरणीय होते हैं", "अपमार्जकों में साइट्रिक अम्ल होता है"],
        "ans": 1,
        "sol": "Detergents contain sulfonate or ammonium groups which do not form insoluble scum with Ca²⁺ and Mg²⁺ ions present in hard water, allowing them to lather easily.",
        "sol_hi": "अपमार्जक के आवेशित सिरे कठोर जल में मौजूद Ca²⁺ और Mg²⁺ आयनों के साथ अघुलनशील अवक्षेप (स्कम) नहीं बनाते हैं, जिससे वे कठोर जल में भी आसानी से झाग दे सकते हैं।"
    },
    {
        "q": "What is the structural formula of Propanal?",
        "q_hi": "प्रोपेनैल (Propanal) का संरचनात्मक सूत्र क्या है?",
        "opts": ["CH₃CH₂OH", "CH₃CH₂CHO", "CH₃COCH₃", "CH₃CH₂COOH"],
        "opts_hi": ["CH₃CH₂OH", "CH₃CH₂CHO (CH₃CH₂CHO)", "CH₃COCH₃", "CH₃CH₂COOH"],
        "ans": 1,
        "sol": "Propanal is a three-carbon aldehyde: CH₃CH₂CHO. CH₃CH₂OH is ethanol, CH₃COCH₃ is propanone, and CH₃CH₂COOH is propanoic acid.",
        "sol_hi": "प्रोपेनैल तीन कार्बन वाला ऐल्डिहाइड है: CH₃CH₂CHO। CH₃CH₂OH इथेनॉल है, CH₃COCH₃ प्रोपेनोन है, और CH₃CH₂COOH प्रोपेनॉइक अम्ल है।"
    },
    {
        "q": "The gas used in gas welding is:",
        "q_hi": "गैस वेल्डिंग में उपयोग की जाने वाली गैस कौन सी है?",
        "opts": ["Ethane", "Ethene", "Ethyne (Acetylene)", "Methane"],
        "opts_hi": ["इथेन", "एथीन", "इथाइन / एसिटिलीन (Ethyne)", "मीथेन"],
        "ans": 2,
        "sol": "Ethyne (Acetylene) is burned with oxygen (Oxy-acetylene flame) to produce an extremely hot flame (~3000°C) required to melt metals for welding.",
        "sol_hi": "इथाइन (एसिटिलीन) को ऑक्सीजन के साथ जलाया जाता है (ऑक्सी-एसिटिलीन लौ), जिससे अत्यधिक गर्म लौ (~3000°C) उत्पन्न होती है, जो वेल्डिंग के लिए धातुओं को पिघलाने में सक्षम होती है।"
    },
    {
        "q": "Which organic compound is oxidized to ethanoic acid during the souring of wine?",
        "q_hi": "वाइन के खट्टा होने के दौरान कौन सा कार्बनिक यौगिक इथेनॉइक अम्ल में ऑक्सीकृत हो जाता है?",
        "opts": ["Ethanol", "Methanol", "Acetone", "Formaldehyde"],
        "opts_hi": ["इथेनॉल (Ethanol)", "मेथनॉल", "एसीटोन", "फॉर्मेल्डिहाइड"],
        "ans": 0,
        "sol": "Souring of wine is caused by Acetobacter bacteria which oxidizes the Ethanol (alcohol) present in the wine into Ethanoic acid (vinegar taste).",
        "sol_hi": "वाइन का खट्टा होना एसीटोबैक्टर बैक्टीरिया के कारण होता है जो वाइन में उपस्थित इथेनॉल (ऐल्कोहॉल) को इथेनॉइक अम्ल (एसिटिक अम्ल) में ऑक्सीकृत कर देता है।"
    },
    {
        "q": "Which of the following organic compounds will react with sodium metal but will not react with sodium bicarbonate?",
        "q_hi": "निम्नलिखित में से कौन सा कार्बनिक यौगिक सोडियम धातु के साथ तो अभिक्रिया करेगा लेकिन सोडियम बाइकार्बोनेट के साथ अभिक्रिया नहीं करेगा?",
        "opts": ["Ethanol", "Ethanoic Acid", "Methane", "Ester"],
        "opts_hi": ["इथेनॉल (Ethanol)", "इथेनॉइक अम्ल", "मीथेन", "एस्टर"],
        "ans": 0,
        "sol": "Ethanol is slightly acidic and reacts with sodium to release hydrogen gas. However, it is too weak an acid to react with weak bases like sodium bicarbonate (NaHCO₃). Ethanoic acid reacts with both.",
        "sol_hi": "इथेनॉल सोडियम के साथ अभिक्रिया करके हाइड्रोजन गैस मुक्त करता है। लेकिन यह सोडियम बाइकार्बोनेट (NaHCO₃) जैसे कमजोर क्षारक के साथ अभिक्रिया करने के लिए बहुत कमजोर अम्ल है। इथेनॉइक अम्ल दोनों के साथ क्रिया करता है।"
    }
]

# ----------------- BUILD FINAL JSON OBJECTS -----------------
def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Thoroughly review bonding parameters, allotropes, homologous series, functional groups, nomenclature, chemical properties, and soaps.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Bonding & Allotropes of Carbon",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which hybridization is present in Diamond?", "opts": ["sp", "sp²", "sp³", "sp³d"], "ans": 2, "sol": "Diamond has sp³ hybridized carbon atoms forming a 3D network."},
                    {"type": "True/False", "q": "True or False: Graphite does not conduct electricity.", "ans": False, "sol": "False. Graphite has free valence electrons and conducts electricity well."},
                    {"type": "Fill in the Blank", "q": "C₆₀ Fullerene contains ________ pentagonal rings.", "ans": "12", "sol": "Fullerene contains 12 pentagonal rings and 20 hexagonal rings."}
                ]
            },
            {
                "title": "2. Hydrocarbons & Nomenclature",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is the suffix for Aldehydes?", "opts": ["-ol", "-al", "-one", "-oic"], "ans": 1, "sol": "Aldehydes use the suffix -al."},
                    {"type": "True/False", "q": "True or False: Homologous series members differ by a -CH₂- unit.", "ans": True, "sol": "True. Successive members differ by a -CH₂- group and 14 u mass."}
                ]
            },
            {
                "title": "3. Reactions, Soaps & Detergents",
                "masteryZone": [
                    {"type": "MCQ", "q": "Vegetable oil is converted to ghee using which reaction?", "opts": ["Substitution", "Dehydration", "Addition", "Esterification"], "ans": 2, "sol": "Hydrogenation is an addition reaction using nickel catalyst."},
                    {"type": "True/False", "q": "True or False: Soaps work effectively in hard water.", "ans": False, "sol": "False. Soaps form insoluble scum in hard water."}
                ]
            }
        ]
    }


def build_theory_hi():
    return {
        "breadcrumbs": breadcrumbs_hi,
        "hero": hero_hi,
        "labels": labels_hi,
        "timeline": timeline_hi,
        "mnemonics": mnemonics_hi,
        "flashcards": flashcards_hi,
        "traps": traps_hi,
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "आबंधों, अपररूपों, समजातीय श्रेणी, कार्यात्मक समूहों, नामकरण, रासायनिक गुणों और साबुनों की गहन समीक्षा करें।", "sections": deep_dive_hi}
    }

def build_practice_hi():
    practice_obj = {
        "practiceQuestions": [
            {"q": pq["q_hi"], "opts": pq["opts_hi"], "ans": pq["ans"], "sol": pq["sol_hi"]} for pq in practice_questions
        ],
        "mockTestQuestions": [
            {"q": mtq["q_hi"], "opts": mtq["opts_hi"], "ans": mtq["ans"], "sol": mtq["sol_hi"]} for mtq in mock_test_questions
        ]
    }
    return practice_obj

def build_mastery_hi():
    return {
        "sections": [
            {
                "title": "1. आबंध और कार्बन के अपररूप",
                "masteryZone": [
                    {"type": "MCQ", "q": "हीरे में कार्बन का संकरण क्या होता है?", "opts": ["sp", "sp²", "sp³", "sp³d"], "ans": 2, "sol": "हीरे में sp³ संकरित कार्बन परमाणु होते हैं जो 3D नेटवर्क बनाते हैं।"},
                    {"type": "True/False", "q": "सही या गलत: ग्रेफाइट विद्युत का चालन नहीं करता है।", "ans": False, "sol": "गलत। ग्रेफाइट में मुक्त संयोजी इलेक्ट्रॉन होते हैं और यह विद्युत का अच्छा सुचालक है।"},
                    {"type": "Fill in the Blank", "q": "C₆₀ फुलरीन में __________ पंचकोणीय वलय होते हैं।", "ans": "12", "sol": "फुलरीन में 12 पंचकोण और 20 षटकोण वलय होते हैं।"}
                ]
            },
            {
                "title": "2. हाइड्रोकार्बन और नामकरण",
                "masteryZone": [
                    {"type": "MCQ", "q": "ऐल्डिहाइड के लिए किस अनुलग्न (suffix) का उपयोग किया जाता है?", "opts": ["-ol", "-al", "-one", "-oic"], "ans": 1, "sol": "ऐल्डिहाइड के नामकरण में -al अनुलग्न का उपयोग होता है।"},
                    {"type": "True/False", "q": "सही या गलत: समजातीय श्रेणी के सदस्य -CH₂- इकाई से भिन्न होते हैं।", "ans": True, "sol": "सही। क्रमागत सदस्य -CH₂- समूह और 14 u द्रव्यमान से भिन्न होते हैं।"}
                ]
            },
            {
                "title": "3. रासायनिक अभिक्रियाएं, साबुन और अपमार्जक",
                "masteryZone": [
                    {"type": "MCQ", "q": "वनस्पति तेल को किस अभिक्रिया द्वारा घी में बदला जाता है?", "opts": ["प्रतिस्थापन", "निर्जलीकरण", "संकलन", "एस्टरीकरण"], "ans": 2, "sol": "निकेल उत्प्रेरक की उपस्थिति में हाइड्रोजनीकरण एक संकलन अभिक्रिया है।"},
                    {"type": "True/False", "q": "सही या गलत: साबुन कठोर जल में प्रभावी रूप से कार्य करते हैं।", "ans": False, "sol": "गलत। साबुन कठोर जल में अघुलनशील स्कम बनाते हैं।"}
                ]
            }
        ]
    }


# ----------------- FILE GENERATION -----------------
def write_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())
