# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "acids-bases-salts"
TOPIC_DISPLAY = "Acids, Bases & Salts"
TOPIC_DISPLAY_HI = "अम्ल, क्षारक और लवण"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\general-science\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "General Science",
    "parentUrl": "../",
    "current": "Acids, Bases & Salts"
}

hero_en = {
    "title": "Acids, Bases & Salts",
    "description": "Master Arrhenius, Brønsted-Lowry, and Lewis concepts, pH scale parameters, indicators (natural, synthetic, olfactory), reactions of acids and bases, and properties of important salts (Bleaching powder, Baking soda, Washing soda, Plaster of Paris)."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Acids, Bases & Salts Mock Test",
        "description": "Test your knowledge of pH values, acid-base theories, chemical properties, indicator colors, and industrial salts. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Scientific Milestones in Acid-Base Chemistry",
    "description": "Key historical theories that defined acids, bases, and salts.",
    "cards": [
        {
            "period": "Lavoisier's Oxygen Theory",
            "date": "1776",
            "details": "Antoine Lavoisier proposes that all acids contain oxygen (later disproved by Davy showing hydrochloric acid lacks oxygen)."
        },
        {
            "period": "Arrhenius Concept",
            "date": "1887",
            "details": "Svante Arrhenius defines acids as substances producing hydrogen ions (H⁺) in water, and bases as producing hydroxide ions (OH⁻)."
        },
        {
            "period": "Sorensen's pH Scale",
            "date": "1909",
            "details": "S.P.L. Sørensen introduces the pH scale as a convenient logarithmic method to measure hydrogen ion concentration."
        },
        {
            "period": "Brønsted-Lowry Theory",
            "date": "1923",
            "details": "Johannes Brønsted and Thomas Lowry independently define acids as proton (H⁺) donors and bases as proton acceptors."
        },
        {
            "period": "Lewis Electronic Theory",
            "date": "1923",
            "details": "G.N. Lewis defines acids as electron pair acceptors and bases as electron pair donors, expanding the scope beyond protons."
        }
    ]
}

mnemonics_en = {
    "title": "Acids, Bases & Salts Mnemonics",
    "description": "Quick memory aids for litmus color changes and salt compositions.",
    "items": [
        {
            "title": "Mnemonic 1: Litmus Color Change",
            "phrase": "\"BAR (Blue to Red is Acid) & RBB (Red to Blue is Base)\"",
            "decryption": "Remember how litmus changes color:<br>• <strong>B</strong>lue to <strong>R</strong>ed is <strong>A</strong>cid (<strong>BAR</strong>)<br>• <strong>R</strong>ed to <strong>B</strong>lue is <strong>B</strong>ase (<strong>RBB</strong>)"
        },
        {
            "title": "Mnemonic 2: Baking Soda vs Washing Soda",
            "phrase": "\"Baking has Hydrogen (NaHCO₃), Washing has Water (Na₂CO₃·10H₂O)\"",
            "decryption": "Differentiate the chemical formulas:<br>• <strong>Baking Soda</strong>: Sodium <strong>Bi</strong>carbonate / Sodium <strong>Hydrogen</strong> Carbonate (NaHCO₃). Think of \"Bi\" / \"Hydrogen\" for baking.<br>• <strong>Washing Soda</strong>: Sodium Carbonate Decahydrate (Na₂CO₃&middot;10H₂O). Needs <strong>water</strong> molecules (10H₂O) to wash!"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Click to flip and test your understanding of acid-base concepts.",
    "items": [
        {
            "question": "What is the difference between a Strong Acid and a Concentrated Acid?",
            "answer": "A <strong>Strong Acid</strong> completely ionizes in water to release H⁺ ions (e.g., HCl). A <strong>Concentrated Acid</strong> simply has a high ratio of acid to water in the solution, regardless of its ionization strength.",
            "icon": "fa-circle-exclamation"
        },
        {
            "question": "Why does dry HCl gas not change the color of dry blue litmus paper?",
            "answer": "Because acids only dissociate to release H⁺ / H₃O⁺ ions <strong>in the presence of water</strong>. Without moisture, dry HCl gas cannot exhibit acidic properties.",
            "icon": "fa-droplet-slash"
        },
        {
            "question": "What is the chemical name of Plaster of Paris, and how is it prepared?",
            "answer": "Plaster of Paris is <strong>Calcium Sulfate Hemihydrate</strong> (CaSO₄&middot;0.5H₂O). It is prepared by heating Gypsum (CaSO₄&middot;2H₂O) at <strong>373 K (100°C)</strong>.",
            "icon": "fa-mortar-pestle"
        },
        {
            "question": "How do Phenolphthalein and Methyl Orange indicators change in acid and base?",
            "answer": "• <strong>Phenolphthalein</strong>: Colorless in acid, <strong>Pink</strong> in base.<br>• <strong>Methyl Orange</strong>: <strong>Red</strong> in acid, <strong>Yellow</strong> in base.",
            "icon": "fa-flask-vial"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Diluting acid by adding water directly to concentrated acid. This reaction is highly exothermic. The heat generated can cause the mixture to splash out and cause burns. Always dilute by <strong>adding acid slowly to water</strong> with constant stirring.",
        "<strong>Trap 2:</strong> Confusing Baking Soda with Baking Powder. Baking Soda is pure <strong>Sodium Hydrogen Carbonate (NaHCO₃)</strong>. Baking Powder is a mixture of baking soda and a mild edible acid like <strong>tartaric acid</strong> (which prevents a bitter taste by neutralizing the sodium carbonate formed during heating).",
        "<strong>Trap 3:</strong> Assuming all bases are alkalis. An <strong>alkali</strong> is a base that is soluble in water (e.g., NaOH, KOH). Bases like Copper Oxide (CuO) or Ferric Hydroxide (Fe(OH)₃) do not dissolve in water and are not alkalis.",
        "<strong>Trap 4:</strong> Misinterpreting pH values. pH is a negative logarithmic scale. Therefore, a solution with <strong>pH 3 is 10 times more acidic</strong> than a solution with pH 4, and <strong>100 times more acidic</strong> than a solution with pH 5."
    ]
}

deep_dive_en = [
    {
        "title": "1. Theories of Acids & Bases, Indicators & Natural Sources",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Arrhenius Concept:</strong> Acids release H⁺ ions in aqueous solutions (e.g., HCl &rarr; H⁺ + Cl⁻). Bases release OH⁻ ions in aqueous solutions (e.g., NaOH &rarr; Na⁺ + OH⁻).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Brønsted-Lowry Concept:</strong> Acids are proton (H⁺) donors. Bases are proton (H⁺) acceptors. For example, NH₃ (base) accepts a proton from H₂O (acid).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Lewis Concept:</strong> Acids are electron-pair acceptors (e.g., BF₃, AlCl₃, H⁺). Bases are electron-pair donors (e.g., NH₃, H₂O, F⁻).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Indicators:</strong>
            <br>• <strong>Natural:</strong> Litmus (Purple dye from Lichens; Red in acid, Blue in base), Turmeric (Remains yellow in acid, turns Reddish-brown in base).
            <br>• <strong>Synthetic:</strong> Phenolphthalein (Colorless in acid, Pink in base), Methyl Orange (Red in acid, Yellow in base).
            <br>• <strong>Olfactory (Smell changes):</strong> Onion, Clove oil, Vanilla essence (lose their smell in basic solutions, retain smell in acidic solutions).
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>Natural Sources of Acids (Highly Tested in Exams):</strong>
            <div class="premium-table-container">
              <table class="premium-table">
                <thead>
                  <tr>
                    <th>Source</th>
                    <th>Acid Present</th>
                    <th>Source</th>
                    <th>Acid Present</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Vinegar</td>
                    <td>Acetic Acid (Ethanoic Acid)</td>
                    <td>Lemon / Orange</td>
                    <td>Citric Acid</td>
                  </tr>
                  <tr>
                    <td>Tomato / Spinach</td>
                    <td>Oxalic Acid</td>
                    <td>Tamarind / Grapes</td>
                    <td>Tartaric Acid</td>
                  </tr>
                  <tr>
                    <td>Sour milk / Curd</td>
                    <td>Lactic Acid</td>
                    <td>Apples</td>
                    <td>Malic Acid</td>
                  </tr>
                  <tr>
                    <td>Ant / Wasp / Nettle sting</td>
                    <td>Methanoic Acid (Formic Acid)</td>
                    <td>Rancid Butter</td>
                    <td>Butyric Acid</td>
                  </tr>
                  <tr>
                    <td>Tea</td>
                    <td>Tannic Acid</td>
                    <td>Wheat</td>
                    <td>Glutamic Acid</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </li>
        </ul>
        
        <!-- SVG Diagram 1: Neutralization Reaction -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .beaker-line { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 2.5px; }
            .acid-color { fill: rgba(231, 76, 60, 0.15); }
            .base-color { fill: rgba(52, 152, 219, 0.15); }
            .neutral-color { fill: rgba(46, 204, 113, 0.15); }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            .label-head { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .beaker-line { stroke: #cbd5e1; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">Neutralization: Acid + Base &rarr; Salt + Water + Heat</text>
          
          <!-- Acid Beaker (Left) -->
          <g transform="translate(60, 40)">
            <rect x="20" y="40" width="100" height="90" class="acid-color" />
            <path d="M 20 20 L 20 130 L 120 130 L 120 20" class="beaker-line" />
            <text x="70" y="85" class="label-head" fill="#e74c3c" text-anchor="middle">Acid (HCl)</text>
            <text x="70" y="105" class="annot-text" text-anchor="middle">Releases H⁺ ions</text>
            <text x="70" y="155" class="annot-text" font-weight="bold" text-anchor="middle">pH &lt; 7</text>
          </g>
          
          <!-- Plus Sign -->
          <text x="230" y="115" font-family="'Outfit', sans-serif;" font-size="28px;" fill="var(--text-dark, #2c3e50)" text-anchor="middle">+</text>
          
          <!-- Base Beaker (Middle) -->
          <g transform="translate(290, 40)">
            <rect x="20" y="40" width="100" height="90" class="base-color" />
            <path d="M 20 20 L 20 130 L 120 130 L 120 20" class="beaker-line" />
            <text x="70" y="85" class="label-head" fill="#3498db" text-anchor="middle">Base (NaOH)</text>
            <text x="70" y="105" class="annot-text" text-anchor="middle">Releases OH⁻ ions</text>
            <text x="70" y="155" class="annot-text" font-weight="bold" text-anchor="middle">pH &gt; 7</text>
          </g>
          
          <!-- Equals / Yields Arrow -->
          <path d="M 460 100 L 520 100" stroke="var(--text-dark, #2c3e50)" stroke-width="2" fill="none" />
          <polygon points="520,100 510,95 510,105" fill="var(--text-dark, #2c3e50)" />
          <text x="490" y="90" class="annot-text" text-anchor="middle">Neutralize</text>
          
          <!-- Salt + Water Flask (Right) -->
          <g transform="translate(560, 40)">
            <rect x="20" y="40" width="120" height="90" class="neutral-color" />
            <path d="M 20 20 L 20 130 L 140 130 L 140 20" class="beaker-line" />
            <text x="80" y="75" class="label-head" fill="#2ecc71" text-anchor="middle">Salt + Water</text>
            <text x="80" y="95" class="annot-text" text-anchor="middle">(NaCl + H₂O)</text>
            <text x="80" y="115" class="annot-text" fill="#e67e22" text-anchor="middle">Exothermic (Heat)</text>
            <text x="80" y="155" class="annot-text" font-weight="bold" text-anchor="middle">pH &asymp; 7</text>
          </g>
        </svg>"""
    },
    {
        "title": "2. pH Scale, Everyday Importance, Aqua Regia & Weak Acids in Drinks",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>pH Scale:</strong> Ranges from 0 (very acidic) to 14 (very alkaline). pH 7 is neutral. pH = -log[H⁺]. As [H⁺] increases, pH decreases.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Body pH range:</strong> Human body works within the narrow pH range of <strong>7.0 to 7.8</strong>. Blood pH is slightly basic at <strong>7.35 to 7.45</strong>.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Tooth Decay:</strong> Starts when the pH of the mouth falls <strong>below 5.5</strong> (bacteria produce acids by degrading sugar particles). Prevented by using basic toothpaste.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Acid Rain:</strong> When the pH of rain water falls <strong>below 5.6</strong>. Affects aquatic life when it flows into rivers, lowering river pH.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Self Defense by Animals:</strong> Bee sting contains formic acid (methanoic acid), causing pain; cured by applying a mild base like baking soda. Wasp sting is alkaline, treated by applying mild vinegar (acetic acid). Nettle leaf hair injects methanoic acid, cured by rubbing dock plant leaf (basic).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Aqua Regia (Royal Water / अम्लराज):</strong> A freshly prepared mixture of <strong>concentrated Hydrochloric Acid (HCl) and concentrated Nitric Acid (HNO₃) in a 3:1 ratio</strong> by volume. It is a highly fuming, corrosive liquid. It can dissolve noble metals like Gold (Au) and Platinum (Pt), even though neither acid can do so individually.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Weak Acids in Beverages:</strong> Soda water and aerated drinks contain dissolved Carbon Dioxide under pressure, which forms weak <strong>Carbonic Acid (H₂CO₃)</strong>. Some beverages also contain <strong>Phosphoric Acid (H₃PO₄)</strong> to add a tart flavor.</li>
        </ul>
        
        <!-- SVG Diagram 2: pH Scale Color Bar -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <defs>
            <linearGradient id="phGradient" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#e74c3c" />
              <stop offset="25%" stop-color="#e67e22" />
              <stop offset="50%" stop-color="#2ecc71" />
              <stop offset="75%" stop-color="#3498db" />
              <stop offset="100%" stop-color="#9b59b6" />
            </linearGradient>
          </defs>
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .ph-bar { fill: url(#phGradient); rx: 6px; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            .ticks { stroke: #ffffff; stroke-width: 1.5px; }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">The pH Scale & Common Substances</text>
          
          <!-- Gradient Bar -->
          <rect x="40" y="70" width="720" height="40" class="ph-bar" />
          
          <!-- Tick Marks and Numbers -->
          <!-- pH 0 -->
          <line x1="40" y1="70" x2="40" y2="110" class="ticks" />
          <text x="40" y="130" class="annot-text" font-weight="bold" text-anchor="middle">0</text>
          <text x="40" y="55" class="annot-text" fill="#e74c3c" text-anchor="middle">Battery Acid</text>
          
          <!-- pH 2 -->
          <line x1="143" y1="70" x2="143" y2="110" class="ticks" />
          <text x="143" y="130" class="annot-text" font-weight="bold" text-anchor="middle">2</text>
          <text x="143" y="55" class="annot-text" text-anchor="middle">Lemon (2.2)</text>
          
          <!-- pH 5.6 -->
          <line x1="328" y1="70" x2="328" y2="110" class="ticks" />
          <text x="328" y="130" class="annot-text" font-weight="bold" text-anchor="middle">5.6</text>
          <text x="328" y="55" class="annot-text" text-anchor="middle">Acid Rain</text>
          
          <!-- pH 7 -->
          <line x1="400" y1="70" x2="400" y2="110" class="ticks" stroke="#2c3e50" stroke-width="2" />
          <text x="400" y="130" class="annot-text" font-weight="bold" text-anchor="middle">7</text>
          <text x="400" y="55" class="annot-text" fill="#2ecc71" font-weight="bold" text-anchor="middle">Neutral (Pure Water)</text>
          
          <!-- pH 7.4 -->
          <line x1="420" y1="70" x2="420" y2="110" class="ticks" />
          <text x="445" y="150" class="annot-text" text-anchor="middle">Blood (7.4)</text>
          
          <!-- pH 10 -->
          <line x1="554" y1="70" x2="554" y2="110" class="ticks" />
          <text x="554" y="130" class="annot-text" font-weight="bold" text-anchor="middle">10</text>
          <text x="554" y="55" class="annot-text" text-anchor="middle">Milk of Magnesia</text>
          
          <!-- pH 14 -->
          <line x1="760" y1="70" x2="760" y2="110" class="ticks" />
          <text x="760" y="130" class="annot-text" font-weight="bold" text-anchor="middle">14</text>
          <text x="760" y="55" class="annot-text" fill="#9b59b6" text-anchor="middle">NaOH</text>
          
          <text x="140" y="190" class="annot-text" fill="#e74c3c" font-weight="bold">Increasing Acidic Character &larr;</text>
          <text x="660" y="190" class="annot-text" fill="#9b59b6" font-weight="bold">&rarr; Increasing Basic Character</text>
        </svg>"""
    },
    {
        "title": "3. Important Industrial Salts, Vitriols & Hydrated Minerals",
        "content": """<p>Several salts produced from common salt (NaCl) and key hydrated minerals have vital domestic and industrial applications:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Salt (Common & Chemical Name)</th>
                <th>Chemical Formula</th>
                <th>Preparation & Reaction</th>
                <th>Key Properties & Exam Traps</th>
                <th>Major Uses</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Caustic Soda</strong><br>(Sodium Hydroxide)</td>
                <td><strong>NaOH</strong></td>
                <td>Prepared by the <strong>Chlor-alkali process</strong> (electrolysis of brine):<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">2NaCl + 2H₂O &rarr; 2NaOH + Cl₂&uarr; + H₂&uarr;</span></td>
                <td>Strong base/alkali. Byproducts released: <strong>Chlorine gas at the anode</strong> and <strong>Hydrogen gas at the cathode</strong>.</td>
                <td>Soaps, detergents, paper manufacturing, degreasing metals.</td>
              </tr>
              <tr>
                <td><strong>Bleaching Powder</strong><br>(Calcium Oxychloride)</td>
                <td><strong>CaOCl₂</strong></td>
                <td>Produced by passing chlorine gas over dry slaked lime:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">Ca(OH)₂ + Cl₂ &rarr; CaOCl₂ + H₂O</span></td>
                <td>Smells of chlorine because it reacts slowly with atmospheric CO₂ to release chlorine gas:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">CaOCl₂ + CO₂ &rarr; CaCO₃ + Cl₂&uarr;</span></td>
                <td>Bleaching cotton & wood pulp, disinfecting drinking water, oxidizing agent.</td>
              </tr>
              <tr>
                <td><strong>Baking Soda</strong><br>(Sodium Hydrogen Carbonate)</td>
                <td><strong>NaHCO₃</strong></td>
                <td>Produced via the <strong>Solvay process</strong> using NaCl, NH₃, CO₂, and H₂O. Decomposes on heating:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">2NaHCO₃ &rarr; Na₂CO₃ + H₂O + CO₂&uarr;</span></td>
                <td><strong>Baking Powder</strong> is a mixture of baking soda and a mild acid like <strong>tartaric acid</strong>. The acid neutralizes the bitter-tasting Na₂CO₃ byproduct into pleasant sodium tartrate.</td>
                <td>Baking cakes/breads, ingredient in antacids, soda-acid fire extinguishers.</td>
              </tr>
              <tr>
                <td><strong>Washing Soda</strong><br>(Sodium Carbonate Decahydrate)</td>
                <td><strong>Na₂CO₃&middot;10H₂O</strong></td>
                <td>Obtained by heating baking soda to get sodium carbonate, followed by its recrystallization.</td>
                <td>Exhibits <strong>efflorescence</strong>—loses 9 water molecules when exposed to dry air to form monohydrate:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">Na₂CO₃&middot;10H₂O &rarr; Na₂CO₃&middot;H₂O + 9H₂O</span><br>Anhydrous Na₂CO₃ is called <strong>Soda Ash</strong>.</td>
                <td>Glass, soap, paper industries, removing permanent hardness of water.</td>
              </tr>
              <tr>
                <td><strong>Plaster of Paris</strong><br>(Calcium Sulfate Hemihydrate)</td>
                <td><strong>CaSO₄&middot;0.5H₂O</strong></td>
                <td>Prepared by heating Gypsum (CaSO₄&middot;2H₂O) at <strong>373 K (100&deg;C)</strong>:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">CaSO₄&middot;2H₂O &rarr; CaSO₄&middot;0.5H₂O + 1.5H₂O</span></td>
                <td>Rehydration sets it back into hard Gypsum. Heating <strong>above 373 K</strong> forms anhydrous CaSO₄ (<strong>Dead Burnt Plaster</strong>), which loses its setting property.</td>
                <td>Supporting fractured bones, plaster casts, making toys, smooth finishes.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p style="margin-top: 1.5rem; font-weight: bold;">Common Vitriols & Alums (Frequently Asked in Exams):</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Common Name</th>
                <th>Chemical Name</th>
                <th>Chemical Formula</th>
                <th>Key Uses & Properties</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Blue Vitriol (नीला थोथा)</td>
                <td>Copper(II) Sulfate Pentahydrate</td>
                <td>CuSO₄&middot;5H₂O</td>
                <td>Fungicide, electroplating, beautiful blue crystals.</td>
              </tr>
              <tr>
                <td>Green Vitriol (हरा कसीस)</td>
                <td>Iron(II) Sulfate Heptahydrate</td>
                <td>FeSO₄&middot;7H₂O</td>
                <td>Treating iron deficiency, manufacturing inks, green crystals.</td>
              </tr>
              <tr>
                <td>White Vitriol (उजला थोथा)</td>
                <td>Zinc Sulfate Heptahydrate</td>
                <td>ZnSO₄&middot;7H₂O</td>
                <td>Dyes, preserving wood, white crystals.</td>
              </tr>
              <tr>
                <td>Epsom Salt</td>
                <td>Magnesium Sulfate Heptahydrate</td>
                <td>MgSO₄&middot;7H₂O</td>
                <td>Bath salt, agricultural fertilizer.</td>
              </tr>
              <tr>
                <td>Potash Alum (फिटकरी)</td>
                <td>Potassium Aluminum Sulfate</td>
                <td>K₂SO₄&middot;Al₂(SO₄)₃&middot;24H₂O</td>
                <td>Purification of water (coagulation of impurities), shaving antiseptic.</td>
              </tr>
              <tr>
                <td>Hypo (हाइपो)</td>
                <td>Sodium Thiosulfate Pentahydrate</td>
                <td>Na₂S₂O₃&middot;5H₂O</td>
                <td>Used in photography for fixing films (dissolves unreacted silver halide).</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <!-- SVG Diagram 3: Gypsum - Plaster of Paris Cycle -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .box-rect { fill: rgba(155, 89, 182, 0.1); stroke: var(--primary, #8e44ad); stroke-width: 2px; rx: 6px; }
            .flow-arrow { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 1.5px; }
            .box-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            .box-sub { font-family: 'Inter', sans-serif; font-size: 12px; fill: var(--text-dark, #2c3e50); }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .box-rect { fill: rgba(168, 85, 247, 0.12); stroke: #a855f7; }
            body.dark-mode .box-title { fill: #a855f7; }
            body.dark-mode .box-sub { fill: #cbd5e1; }
            body.dark-mode .flow-arrow { stroke: #cbd5e1; }
          </style>
          <text x="20" y="30" class="svg-title">Gypsum & Plaster of Paris Interconversion Cycle</text>
          
          <!-- Gypsum Box (Left) -->
          <g transform="translate(60, 70)">
            <rect x="0" y="0" width="220" height="90" class="box-rect" />
            <text x="110" y="30" class="box-title" text-anchor="middle">Gypsum</text>
            <text x="110" y="52" class="box-sub" text-anchor="middle" font-weight="bold">CaSO₄&middot;2H₂O</text>
            <text x="110" y="72" class="box-sub" text-anchor="middle">Hard crystal mass</text>
          </g>
          
          <!-- Forward Arrow (Top) -->
          <path d="M 300 95 L 480 95" class="flow-arrow" />
          <polygon points="480,95 470,90 470,100" fill="var(--text-dark, #2c3e50)" />
          <text x="390" y="85" class="annot-text" fill="#e74c3c" text-anchor="middle">Heat at 373 K (100°C)</text>
          <text x="390" y="110" class="annot-text" text-anchor="middle">Loses 1.5 H₂O</text>
          
          <!-- Backward Arrow (Bottom) -->
          <path d="M 480 135 L 300 135" class="flow-arrow" />
          <polygon points="300,135 310,130 310,140" fill="var(--text-dark, #2c3e50)" />
          <text x="390" y="150" class="annot-text" fill="#3498db" text-anchor="middle">Add Water (+ 1.5 H₂O)</text>
          <text x="390" y="165" class="annot-text" text-anchor="middle">Sets to hard mass</text>
          
          <!-- Plaster of Paris Box (Right) -->
          <g transform="translate(500, 70)">
            <rect x="0" y="0" width="220" height="90" class="box-rect" />
            <text x="110" y="30" class="box-title" text-anchor="middle">Plaster of Paris (PoP)</text>
            <text x="110" y="52" class="box-sub" text-anchor="middle" font-weight="bold">CaSO₄&middot;0.5H₂O</text>
            <text x="110" y="72" class="box-sub" text-anchor="middle">Fine white powder</text>
          </g>
        </svg>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "सामान्य विज्ञान",
    "parentUrl": "../",
    "current": "अम्ल, क्षारक और लवण"
}

hero_hi = {
    "title": "अम्ल, क्षारक और लवण",
    "description": "आरहेनियस, ब्रोंस्टेड-लोरी और लुईस अवधारणाओं, पीएच स्केल के मापदंडों, सूचकों (प्राकृतिक, कृत्रिम, गंधीय), अम्ल-क्षारक प्रतिक्रियाओं और प्रमुख औद्योगिक लवणों (विरंजक चूर्ण, बेकिंग सोडा, धावन सोडा, प्लास्टर ऑफ पेरिस) में महारत हासिल करें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "अम्ल, क्षारक और लवण मॉक टेस्ट",
        "description": "पीएच मान, अम्ल-क्षारक सिद्धांतों, रासायनिक गुणों, सूचकों के रंग परिवर्तन और औद्योगिक लवणों की अपनी समझ का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "अम्ल-क्षारक रसायन विज्ञान में मील के पत्थर",
    "description": "अम्ल, क्षारक और लवण को परिभाषित करने वाले प्रमुख ऐतिहासिक सिद्धांत।",
    "cards": [
        {
            "period": "लेवोज़ियर का ऑक्सीजन सिद्धांत",
            "date": "1776",
            "details": "एंटोनी लेवोज़ियर ने प्रस्ताव दिया कि सभी अम्लों में ऑक्सीजन होती है (बाद में डेवी ने यह साबित कर गलत ठहराया कि हाइड्रोक्लोरिक अम्ल में ऑक्सीजन नहीं होती)।"
        },
        {
            "period": "आरहेनियस अवधारणा",
            "date": "1887",
            "details": "स्वान्ते आरहेनियस ने अम्लों को जलीय विलयन में Hydrogen आयन (H⁺) और क्षारकों को Hydroxide आयन (OH⁻) मुक्त करने वाले पदार्थों के रूप में परिभाषित किया।"
        },
        {
            "period": "सोरेन्सन का पीएच स्केल",
            "date": "1909",
            "details": "एस.पी.एल. सोरेन्सन ने हाइड्रोजन आयन सांद्रता को मापने की एक सरल लघुगणकीय (logarithmic) विधि के रूप में पीएच (pH) स्केल की शुरुआत की।"
        },
        {
            "period": "ब्रोंस्टेड-लोरी सिद्धांत",
            "date": "1923",
            "details": "जोहान्स ब्रोंस्टेड और थॉमस लोरी ने स्वतंत्र रूप से अम्लों को प्रोटॉन (H⁺) दाता और क्षारकों को प्रोटॉन ग्राही के रूप में परिभाषित किया।"
        },
        {
            "period": "लुईस इलेक्ट्रॉनिक सिद्धांत",
            "date": "1923",
            "details": "जी.एन. लुईस ने अम्लों को इलेक्ट्रॉन युग्म ग्राही और क्षारकों को इलेक्ट्रॉन युग्म दाता के रूप में परिभाषित कर इसका दायरा प्रोटॉन से आगे बढ़ाया।"
        }
    ]
}

mnemonics_hi = {
    "title": "अम्ल, क्षारक और लवण के स्मृति सूत्र",
    "description": "लिटमस रंग परिवर्तन और रासायनिक सूत्रों को याद रखने के त्वरित सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: लिटमस पत्र रंग परिवर्तन",
            "phrase": "\"अनीला (अम्ल नीले को लाल करता है) और छालनी (क्षार लाल को नीला करता है)\"",
            "decryption": "लिटमस का रंग परिवर्तन याद रखें:<br>• <strong>अ</strong>म्ल <strong>नी</strong>ले लिटमस को <strong>ला</strong>ल करता है (<strong>अनीला</strong>)<br>• <strong>क्षा</strong>र <strong>ला</strong>ल लिटमस को <strong>नी</strong>ला करता है (<strong>छालनी</strong>)"
        },
        {
            "title": "स्मृति सूत्र 2: बेकिंग सोडा बनाम धावन (वाशिंग) सोडा",
            "phrase": "\"खाने वाले में हाइड्रोजन (NaHCO₃), धोने वाले में जल (Na₂CO₃·10H₂O) होता है\"",
            "decryption": "रासायनिक सूत्रों में अंतर करें:<br>• <strong>बेकिंग सोडा (खाने का सोडा)</strong>: सोडियम बाइकार्बोनेट / सोडियम हाइड्रोजन कार्बोनेट (NaHCO₃)। इसमें 'हाइड्रोजन' या 'बाई' होता है।<br>• <strong>धावन सोडा (धोने का सोडा)</strong>: सोडियम कार्बोनेट डेकाहाइड्रेट (Na₂CO₃&middot;10H₂O)। कपड़े धोने के लिए <strong>10 बाल्टी जल</strong> (10H₂O) की आवश्यकता होती है।"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए क्लिक करें और अपनी समझ की जांच करें।",
    "items": [
        {
            "question": "प्रबल अम्ल (Strong Acid) और सांद्र अम्ल (Concentrated Acid) में क्या अंतर है?",
            "answer": "एक <strong>प्रबल अम्ल</strong> जल में पूरी तरह से आयनित होकर H⁺ आयन देता है (जैसे HCl)। जबकि <strong>सांद्र अम्ल</strong> केवल विलयन में पानी की तुलना में अम्ल की अधिक मात्रा को दर्शाता है, चाहे उसकी आयनीकरण क्षमता कुछ भी हो।",
            "icon": "fa-circle-exclamation"
        },
        {
            "question": "शुष्क HCl गैस शुष्क नीले लिटमस पत्र का रंग क्यों नहीं बदलती?",
            "answer": "क्योंकि अम्ल केवल <strong>जल की उपस्थिति</strong> में ही आयनित होकर H⁺ / H₃O⁺ आयन मुक्त करते हैं। नमी की अनुपस्थिति में शुष्क HCl गैस अम्लीय गुण प्रदर्शित नहीं कर पाती।",
            "icon": "fa-droplet-slash"
        },
        {
            "question": "प्लास्टर ऑफ पेरिस का रासायनिक नाम क्या है, और यह कैसे तैयार किया जाता है?",
            "answer": "प्लास्टर ऑफ पेरिस का रासायनिक नाम <strong>कैल्शियम सल्फेट हेमीहाइड्रेट</strong> (CaSO₄&middot;0.5H₂O) है। इसे जिप्सम (CaSO₄&middot;2H₂O) को <strong>373 K (100°C)</strong> पर गर्म करके तैयार किया जाता है।",
            "icon": "fa-mortar-pestle"
        },
        {
            "question": "फिनोलफ्थेलीन और मिथाइल ऑरेंज सूचक अम्ल तथा क्षारक में क्या रंग परिवर्तन दर्शाते हैं?",
            "answer": "• <strong>फिनोलफ्थेलीन</strong>: अम्ल में रंगहीन, <strong>क्षारक में गुलाबी (Pink)</strong>।<br>• <strong>मिथाइल ऑरेंज</strong>: अम्ल में <strong>लाल</strong>, क्षारक में <strong>पीला (Yellow)</strong>।",
            "icon": "fa-flask-vial"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> सांद्र अम्ल को पतला (dilute) करने के लिए उसमें सीधे पानी मिलाना। यह प्रतिक्रिया अत्यधिक ऊष्माक्षेपी (exothermic) होती है। इससे उत्पन्न ऊष्मा के कारण मिश्रण बाहर छलक सकता है और दुर्घटना हो सकती है। हमेशा <strong>अम्ल को धीरे-धीरे पानी में</strong> मिलाना चाहिए, न कि पानी को अम्ल में।",
        "<strong>भ्रम 2:</strong> बेकिंग सोडा और बेकिंग पाउडर को एक ही समझना। बेकिंग सोडा शुद्ध <strong>सोडियम हाइड्रोजन कार्बोनेट (NaHCO₃)</strong> है। जबकि बेकिंग पाउडर बेकिंग सोडा और <strong>टार्टरिक अम्ल</strong> जैसे हल्के खाद्य अम्ल का मिश्रण होता है (जो गर्म करने पर बनने वाले सोडियम कार्बोनेट के कड़वे स्वाद को उदासीन कर देता है)।",
        "<strong>भ्रम 3:</strong> सभी क्षारकों को क्षार (Alkali) मानना। <strong>क्षार (Alkali)</strong> वह क्षारक है जो जल में विलेय होता है (जैसे NaOH, KOH)। कॉपर ऑक्साइड (CuO) या फेरिक हाइड्रोक्साइड (Fe(OH)₃) जैसे क्षारक जल में नहीं घुलते, इसलिए वे क्षार नहीं हैं।",
        "<strong>भ्रम 4:</strong> पीएच (pH) मान को गलत समझना। पीएच एक ऋणात्मक लघुगणकीय स्केल है। इसलिए, <strong>pH 3 का विलयन pH 4 के विलयन से 10 गुना अधिक अम्लीय</strong> होता है, और <strong>pH 5 के विलयन से 100 गुना अधिक अम्लीय</strong> होता है।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. अम्ल एवं क्षारकों के सिद्धांत, सूचक और प्राकृतिक स्रोत",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>आरहेनियस सिद्धांत (Arrhenius Concept):</strong> अम्ल जलीय विलयन में H⁺ आयन देते हैं (जैसे: HCl &rarr; H⁺ + Cl⁻)। क्षारक जलीय विलयन में OH⁻ आयन देते हैं (जैसे: NaOH &rarr; Na⁺ + OH⁻)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>ब्रोंस्टेड-लोरी सिद्धांत:</strong> अम्ल प्रोटॉन (H⁺) दाता होते हैं। क्षारक प्रोटॉन (H⁺) ग्राही होते हैं। उदाहरण के लिए, NH₃ (क्षारक) H₂O (अम्ल) से प्रोटॉन स्वीकार करता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>लुईस सिद्धांत:</strong> अम्ल इलेक्ट्रॉन-युग्म ग्राही होते हैं (जैसे: BF₃, AlCl₃, H⁺)। क्षारक इलेक्ट्रॉन-युग्म दाता होते हैं (जैसे: NH₃, H₂O, F⁻)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>सूचक (Indicators):</strong>
            <br>• <strong>प्राकृतिक सूचक:</strong> लिटमस (लाइकेन से प्राप्त बैंगनी रंग का रंजक; अम्ल में लाल, क्षार में नीला), हल्दी (अम्ल में पीली रहती है, क्षार में लाल-भूरा रंग देती है)।
            <br>• <strong>कृत्रिम (Synthetic):</strong> फिनोलफ्थेलीन (अम्ल में रंगहीन, क्षार में गुलाबी), मिथाइल ऑरेंज (अम्ल में लाल, क्षार में पीला)।
            <br>• <strong>गंधीय सूचक (Olfactory):</strong> प्याज, लौंग का तेल, वैनिला एसेंस (क्षारीय विलयन में इनकी गंध समाप्त हो जाती है, अम्लीय विलयन में गंध बनी रहती है)।
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>अम्लों के प्राकृतिक स्रोत (परीक्षाओं में सर्वाधिक पूछे जाने वाले):</strong>
            <div class="premium-table-container">
              <table class="premium-table">
                <thead>
                  <tr>
                    <th>स्रोत (Source)</th>
                    <th>उपस्थित अम्ल (Acid)</th>
                    <th>स्रोत (Source)</th>
                    <th>उपस्थित अम्ल (Acid)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>सिरका (Vinegar)</td>
                    <td>एसिटिक अम्ल (एथेनॉइक अम्ल)</td>
                    <td>नींबू / संतरा</td>
                    <td>साइट्रिक अम्ल</td>
                  </tr>
                  <tr>
                    <td>टमाटर / पालक</td>
                    <td>ऑक्सेलिक अम्ल</td>
                    <td>इमली / अंगूर</td>
                    <td>टार्टरिक अम्ल</td>
                  </tr>
                  <tr>
                    <td>खट्टा दूध / दही</td>
                    <td>लैक्टिक अम्ल</td>
                    <td>सेब (Apples)</td>
                    <td>मैलिक अम्ल (Malic Acid)</td>
                  </tr>
                  <tr>
                    <td>चींटी / ततैया / नेटल डंक</td>
                    <td>मेथेनॉइक अम्ल (फॉर्मिक अम्ल)</td>
                    <td>दुर्गंधयुक्त मक्खन</td>
                    <td>ब्यूटिरिक अम्ल (Butyric Acid)</td>
                  </tr>
                  <tr>
                    <td>चाय (Tea)</td>
                    <td>टैनिक अम्ल (Tannic Acid)</td>
                    <td>गेहूं (Wheat)</td>
                    <td>ग्लूटेमिक अम्ल (Glutamic Acid)</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </li>
        </ul>
        
        <!-- SVG Diagram 1: Neutralization Reaction -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .beaker-line { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 2.5px; }
            .acid-color { fill: rgba(231, 76, 60, 0.15); }
            .base-color { fill: rgba(52, 152, 219, 0.15); }
            .neutral-color { fill: rgba(46, 204, 113, 0.15); }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            .label-head { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .beaker-line { stroke: #cbd5e1; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">उदासीनीकरण: अम्ल + क्षारक &rarr; लवण + जल + ऊष्मा</text>
          
          <!-- Acid Beaker (Left) -->
          <g transform="translate(60, 40)">
            <rect x="20" y="40" width="100" height="90" class="acid-color" />
            <path d="M 20 20 L 20 130 L 120 130 L 120 20" class="beaker-line" />
            <text x="70" y="85" class="label-head" fill="#e74c3c" text-anchor="middle">अम्ल (HCl)</text>
            <text x="70" y="105" class="annot-text" text-anchor="middle">H⁺ आयन देता है</text>
            <text x="70" y="155" class="annot-text" font-weight="bold" text-anchor="middle">pH &lt; 7</text>
          </g>
          
          <!-- Plus Sign -->
          <text x="230" y="115" font-family="'Outfit', sans-serif;" font-size="28px;" fill="var(--text-dark, #2c3e50)" text-anchor="middle">+</text>
          
          <!-- Base Beaker (Middle) -->
          <g transform="translate(290, 40)">
            <rect x="20" y="40" width="100" height="90" class="base-color" />
            <path d="M 20 20 L 20 130 L 120 130 L 120 20" class="beaker-line" />
            <text x="70" y="85" class="label-head" fill="#3498db" text-anchor="middle">क्षारक (NaOH)</text>
            <text x="70" y="105" class="annot-text" text-anchor="middle">OH⁻ आयन देता है</text>
            <text x="70" y="155" class="annot-text" font-weight="bold" text-anchor="middle">pH &gt; 7</text>
          </g>
          
          <!-- Equals / Yields Arrow -->
          <path d="M 460 100 L 520 100" stroke="var(--text-dark, #2c3e50)" stroke-width="2" fill="none" />
          <polygon points="520,100 510,95 510,105" fill="var(--text-dark, #2c3e50)" />
          <text x="490" y="90" class="annot-text" text-anchor="middle">उदासीनीकरण</text>
          
          <!-- Salt + Water Flask (Right) -->
          <g transform="translate(560, 40)">
            <rect x="20" y="40" width="120" height="90" class="neutral-color" />
            <path d="M 20 20 L 20 130 L 140 130 L 140 20" class="beaker-line" />
            <text x="80" y="75" class="label-head" fill="#2ecc71" text-anchor="middle">लवण + जल</text>
            <text x="80" y="95" class="annot-text" text-anchor="middle">(NaCl + H₂O)</text>
            <text x="80" y="115" class="annot-text" fill="#e67e22" text-anchor="middle">ऊष्माक्षेपी (ऊष्मा)</text>
            <text x="80" y="155" class="annot-text" font-weight="bold" text-anchor="middle">pH &asymp; 7</text>
          </g>
        </svg>"""
    },
    {
        "title": "2. पीएच स्केल, दैनिक जीवन में इसका महत्व, अम्लराज (Aqua Regia) और पेय पदार्थों में अम्ल",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>पीएच स्केल:</strong> 0 (अत्यधिक अम्लीय) से 14 (अत्यधिक क्षारीय) तक होता है। पीएच 7 उदासीन होता है। pH = -log[H⁺]। जैसे-जैसे H⁺ बढ़ता है, pH घटता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>शरीर का पीएच परास:</strong> मानव शरीर <strong>7.0 से 7.8</strong> पीएच परास के बीच कार्य करता है। रक्त का पीएच थोड़ा क्षारीय <strong>7.35 से 7.45</strong> होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>दंत क्षय:</strong> जब मुंह का पीएच <strong>5.5 से नीचे</strong> गिर जाता है (जीवाणु भोजन के बाद मुंह में बचे शर्करा का अपघटन कर अम्ल बनाते हैं)। क्षारीय दंतमंजन के उपयोग से इसे रोका जाता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>अम्ल वर्षा (Acid Rain):</strong> जब वर्षा के जल का पीएच मान <strong>5.6 से कम</strong> हो जाता है। यह नदियों के जल का पीएच गिराकर जलीय जीवों को प्रभावित करता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>जीव-जंतुओं द्वारा आत्मरक्षा:</strong>- मधुमक्खी का डंक मेथेनॉइक अम्ल (फॉर्मिक अम्ल) छोड़ता है जिससे दर्द होता है; इसे बेकिंग सोडा जैसे हल्के क्षारक से ठीक किया जाता है। ततैया (wasp) का डंक क्षारीय होता है, इसे हल्के सिरके (एसिटिक अम्ल) से ठीक किया जाता है। नेटल (बिच्छू बूटी) के पत्तों के डंक वाले बाल मेथेनॉइक अम्ल छोड़ते हैं, इसे डॉक पौधे की पत्ती रगड़कर (क्षारीय) ठीक किया जाता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>अम्लराज (Aqua Regia / रॉयल वाटर):</strong> यह <strong>सांद्र हाइड्रोक्लोरिक अम्ल (HCl) और सांद्र नाइट्रिक अम्ल (HNO₃) का 3:1 के अनुपात में</strong> ताजा बना मिश्रण होता है। यह अत्यंत संक्षारक (corrosive) और धूमयुक्त द्रव है जो सोना (Au) और प्लेटिनम (Pt) जैसी महान धातुओं (noble metals) को भी घोल सकता है, जबकि इनमें से कोई भी अम्ल अकेले ऐसा नहीं कर सकता।</li>
          <li style="margin-bottom: 0.75rem;"><strong>पेय पदार्थों में दुर्बल अम्ल:</strong> सोडा वाटर और शीतल पेय पदार्थों (soft drinks) में उच्च दाब पर carbon dioxide घुली होती है, जो जल से क्रिया कर दुर्बल <strong>कार्बोनिक अम्ल (H₂CO₃)</strong> बनाती है। कुछ पेय पदार्थों में तीखा स्वाद देने के लिए <strong>फॉस्फोरिक अम्ल (H₃PO₄)</strong> भी मिलाया जाता है।</li>
        </ul>
        
        <!-- SVG Diagram 2: pH Scale Color Bar -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <defs>
            <linearGradient id="phGradient" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#e74c3c" />
              <stop offset="25%" stop-color="#e67e22" />
              <stop offset="50%" stop-color="#2ecc71" />
              <stop offset="75%" stop-color="#3498db" />
              <stop offset="100%" stop-color="#9b59b6" />
            </linearGradient>
          </defs>
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .ph-bar { fill: url(#phGradient); rx: 6px; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            .ticks { stroke: #ffffff; stroke-width: 1.5px; }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">पीएच स्केल और सामान्य पदार्थ (pH Scale)</text>
          
          <!-- Gradient Bar -->
          <rect x="40" y="70" width="720" height="40" class="ph-bar" />
          
          <!-- Tick Marks and Numbers -->
          <!-- pH 0 -->
          <line x1="40" y1="70" x2="40" y2="110" class="ticks" />
          <text x="40" y="130" class="annot-text" font-weight="bold" text-anchor="middle">0</text>
          <text x="40" y="55" class="annot-text" fill="#e74c3c" text-anchor="middle">बैटरी एसिड</text>
          
          <!-- pH 2 -->
          <line x1="143" y1="70" x2="143" y2="110" class="ticks" />
          <text x="143" y="130" class="annot-text" font-weight="bold" text-anchor="middle">2</text>
          <text x="143" y="55" class="annot-text" text-anchor="middle">नींबू (2.2)</text>
          
          <!-- pH 5.6 -->
          <line x1="328" y1="70" x2="328" y2="110" class="ticks" />
          <text x="328" y="130" class="annot-text" font-weight="bold" text-anchor="middle">5.6</text>
          <text x="328" y="55" class="annot-text" text-anchor="middle">अम्ल वर्षा</text>
          
          <!-- pH 7 -->
          <line x1="400" y1="70" x2="400" y2="110" class="ticks" stroke="#2c3e50" stroke-width="2" />
          <text x="400" y="130" class="annot-text" font-weight="bold" text-anchor="middle">7</text>
          <text x="400" y="55" class="annot-text" fill="#2ecc71" font-weight="bold" text-anchor="middle">उदासीन (शुद्ध जल)</text>
          
          <!-- pH 7.4 -->
          <line x1="420" y1="70" x2="420" y2="110" class="ticks" />
          <text x="445" y="150" class="annot-text" text-anchor="middle">रक्त (7.4)</text>
          
          <!-- pH 10 -->
          <line x1="554" y1="70" x2="554" y2="110" class="ticks" />
          <text x="554" y="130" class="annot-text" font-weight="bold" text-anchor="middle">10</text>
          <text x="554" y="55" class="annot-text" text-anchor="middle">मिल्क ऑफ मैग्नीशिया</text>
          
          <!-- pH 14 -->
          <line x1="760" y1="70" x2="760" y2="110" class="ticks" />
          <text x="760" y="130" class="annot-text" font-weight="bold" text-anchor="middle">14</text>
          <text x="760" y="55" class="annot-text" fill="#9b59b6" text-anchor="middle">NaOH</text>
          
          <text x="140" y="190" class="annot-text" fill="#e74c3c" font-weight="bold">बढ़ती अम्लीय प्रकृति &larr;</text>
          <text x="660" y="190" class="annot-text" fill="#9b59b6" font-weight="bold">&rarr; बढ़ती क्षारीय प्रकृति</text>
        </svg>"""
    },
    {
        "title": "3. महत्वपूर्ण औद्योगिक लवण, विट्रिओल (Vitriols) और हाइड्रेटेड खनिज",
        "content": """<p>साधारण नमक (NaCl) से उत्पादित होने वाले लवणों और हाइड्रेटेड खनिजों के कई घरेलू और औद्योगिक उपयोग हैं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>लवण (सामान्य और रासायनिक नाम)</th>
                <th>रासायनिक सूत्र</th>
                <th>निर्माण विधि और रासायनिक समीकरण</th>
                <th>प्रमुख विशेषताएँ और परीक्षा के भ्रम (Traps)</th>
                <th>मुख्य उपयोग</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>कास्टिक सोडा</strong><br>(सोडियम हाइड्रोक्साइड)</td>
                <td><strong>NaOH</strong></td>
                <td><strong>क्लोर-अल्कली प्रक्रिया</strong> (नमक के जलीय विलयन के विद्युत अपघटन) द्वारा:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">2NaCl + 2H₂O &rarr; 2NaOH + Cl₂&uarr; + H₂&uarr;</span></td>
                <td>प्रबल क्षारक। सह-उत्पाद के रूप में <strong>एनोड पर क्लोरीन गैस</strong> और <strong>कैथोड पर हाइड्रोजन गैस</strong> मुक्त होती है।</td>
                <td>साबुन, अपमार्जक, कागज निर्माण, धातुओं से ग्रीस हटाने में।</td>
              </tr>
              <tr>
                <td><strong>विरंजक चूर्ण</strong><br>(कैल्शियम ऑक्सीक्लोराइड)</td>
                <td><strong>CaOCl₂</strong></td>
                <td>शुष्क बुझे हुए चूने पर क्लोरीन गैस प्रवाहित करके:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">Ca(OH)₂ + Cl₂ &rarr; CaOCl₂ + H₂O</span></td>
                <td>हवा में खुला छोड़ने पर यह वायुमंडलीय CO₂ से क्रिया करके क्लोरीन गैस मुक्त करता है, जिससे इसमें से क्लोरीन की तीव्र गंध आती है:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">CaOCl₂ + CO₂ &rarr; CaCO₃ + Cl₂&uarr;</span></td>
                <td>सूती कपड़ों व लकड़ी की लुगदी का विरंजन, पीने के पानी का कीटाणुशोधन,  ऑक्सीकारक।</td>
              </tr>
              <tr>
                <td><strong>बेकिंग सोडा</strong><br>(सोडियम हाइड्रोजन कार्बोनेट)</td>
                <td><strong>NaHCO₃</strong></td>
                <td>NaCl, NH₃, CO₂ और H₂O के साथ <strong>साल्वे प्रक्रिया</strong> द्वारा। गर्म करने पर अपघटित होता है:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">2NaHCO₃ &rarr; Na₂CO₃ + H₂O + CO₂&uarr;</span></td>
                <td><strong>बेकिंग पाउडर</strong> बेकिंग सोडा और <strong>टार्टरिक अम्ल</strong> का मिश्रण है। अम्ल कड़वे सोडियम कार्बोनेट (Na₂CO₃) को उदासीन कर उसे स्वादिष्ट सोडियम टार्टरेट में बदल देता है।</td>
                <td>ब्रेड व केक को फुलाने, एंटासिड के रूप में, सोडा-अम्ल अग्निशामक यंत्रों में।</td>
              </tr>
              <tr>
                <td><strong>धावन सोडा</strong><br>(सोडियम कार्बोनेट डेकाहाइड्रेट)</td>
                <td><strong>Na₂CO₃&middot;10H₂O</strong></td>
                <td>बेकिंग सोडा को गर्म करके सोडियम कार्बोनेट प्राप्त करने तथा उसके पुनः क्रिस्टलीकरण द्वारा।</td>
                <td>इसमें <strong>उत्फुल्लन (Efflorescence)</strong> का गुण होता है—शुष्क हवा में रखने पर यह 9 जल अणु खोकर मोनोहाइड्रेट बनाता है:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">Na₂CO₃&middot;10H₂O &rarr; Na₂CO₃&middot;H₂O + 9H₂O</span><br>निर्जल Na₂CO₃ को <strong>सोडा ऐश</strong> कहते हैं।</td>
                <td>कांच, साबुन, कागज उद्योगों में, जल की स्थायी कठोरता दूर करने में।</td>
              </tr>
              <tr>
                <td><strong>प्लास्टर ऑफ पेरिस</strong><br>(कैल्शियम सल्फेट हेमीहाइड्रेट)</td>
                <td><strong>CaSO₄&middot;0.5H₂O</strong></td>
                <td>जिप्सम (CaSO₄&middot;2H₂O) को <strong>373 K (100&deg;C)</strong> पर गर्म करके:<br><span style="font-size: 0.9em; font-family: monospace; display: block; margin-top: 4px;">CaSO₄&middot;2H₂O &rarr; CaSO₄&middot;0.5H₂O + 1.5H₂O</span></td>
                <td>जल मिलाने पर यह पुनः जमकर जिप्सम बन जाता है। <strong>373 K से अधिक</strong> गर्म करने पर निर्जल CaSO₄ (<strong>मृत तापित प्लास्टर</strong>) बनता है, जिसमें जमने का गुण नहीं होता।</td>
                <td>टूटी हड्डियों को सहारा देने वाले प्लास्टर कास्ट, खिलौने व सजावटी सामान बनाने में।</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p style="margin-top: 1.5rem; font-weight: bold;">प्रमुख विट्रिओल, फिटकरी और हाइपो (परीक्षाओं के अति-महत्वपूर्ण तथ्य):</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>सामान्य नाम</th>
                <th>रासायनिक नाम</th>
                <th>रासायनिक सूत्र</th>
                <th>प्रमुख उपयोग एवं विशेषताएं</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>नीला थोथा (Blue Vitriol)</td>
                <td>कॉपर(II) सल्फेट पेंटाहाइड्रेट</td>
                <td>CuSO₄&middot;5H₂O</td>
                <td>कवकनाशी (Fungicide), विद्युत लेपन, सुंदर नीले रंग के क्रिस्टल।</td>
              </tr>
              <tr>
                <td>हरा कसीस (Green Vitriol)</td>
                <td>आयरन(II) सल्फेट Heptahydrate</td>
                <td>FeSO₄&middot;7H₂O</td>
                <td>लोहे की कमी के उपचार, स्याही निर्माण, हरे रंग के क्रिस्टल।</td>
              </tr>
              <tr>
                <td>उजला थोथा (White Vitriol)</td>
                <td>जिंक सल्फेट हेप्टाहाइड्रेट</td>
                <td>ZnSO₄&middot;7H₂O</td>
                <td>रंग-रोगन, लकड़ी के संरक्षण में, सफेद क्रिस्टल।</td>
              </tr>
              <tr>
                <td>इप्सम लवण (Epsom Salt)</td>
                <td>मैग्नीशियम सल्फेट हेप्टाहाइड्रेट</td>
                <td>MgSO₄&middot;7H₂O</td>
                <td>बाथ साल्ट, कृषि उर्वरक के रूप में।</td>
              </tr>
              <tr>
                <td>फिटकरी (Potash Alum)</td>
                <td>पोटेशियम एल्युमिनियम सल्फेट</td>
                <td>K₂SO₄&middot;Al₂(SO₄)₃&middot;24H₂O</td>
                <td>जल का शुद्धिकरण (स्कंदन), शेविंग के बाद एंटीसेप्टिक के रूप में।</td>
              </tr>
              <tr>
                <td>हाइपो (Hypo)</td>
                <td>सोडियम थायोसल्फेट पेंटाहाइड्रेट</td>
                <td>Na₂S₂O₃&middot;5H₂O</td>
                <td>फोटोग्राफी में फिल्म फिक्सर के रूप में (अघुलनशील सिल्वर हैलाइड को घोलने के लिए)।</td>
              </tr>
            </tbody>
          </table>
        </div>
        
        <!-- SVG Diagram 3: Gypsum - Plaster of Paris Cycle -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .box-rect { fill: rgba(155, 89, 182, 0.1); stroke: var(--primary, #8e44ad); stroke-width: 2px; rx: 6px; }
            .flow-arrow { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 1.5px; }
            .box-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            .box-sub { font-family: 'Inter', sans-serif; font-size: 12px; fill: var(--text-dark, #2c3e50); }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .box-rect { fill: rgba(168, 85, 247, 0.12); stroke: #a855f7; }
            body.dark-mode .box-title { fill: #a855f7; }
            body.dark-mode .box-sub { fill: #cbd5e1; }
            body.dark-mode .flow-arrow { stroke: #cbd5e1; }
          </style>
          <text x="20" y="30" class="svg-title">जिप्सम और प्लास्टर ऑफ पेरिस का अंतरूपांतरण चक्र</text>
          
          <!-- Gypsum Box (Left) -->
          <g transform="translate(60, 70)">
            <rect x="0" y="0" width="220" height="90" class="box-rect" />
            <text x="110" y="30" class="box-title" text-anchor="middle">जिप्सम (Gypsum)</text>
            <text x="110" y="52" class="box-sub" text-anchor="middle" font-weight="bold">CaSO₄&middot;2H₂O</text>
            <text x="110" y="72" class="box-sub" text-anchor="middle">कठोर क्रिस्टलीय द्रव्यमान</text>
          </g>
          
          <!-- Forward Arrow (Top) -->
          <path d="M 300 95 L 480 95" class="flow-arrow" />
          <polygon points="480,95 470,90 470,100" fill="var(--text-dark, #2c3e50)" />
          <text x="390" y="85" class="annot-text" fill="#e74c3c" text-anchor="middle">373 K (100°C) पर गर्म करना</text>
          <text x="390" y="110" class="annot-text" text-anchor="middle">1.5 H₂O अणु मुक्त होते हैं</text>
          
          <!-- Backward Arrow (Bottom) -->
          <path d="M 480 135 L 300 135" class="flow-arrow" />
          <polygon points="300,135 310,130 310,140" fill="var(--text-dark, #2c3e50)" />
          <text x="390" y="150" class="annot-text" fill="#3498db" text-anchor="middle">जल मिलाना (+ 1.5 H₂O)</text>
          <text x="390" y="165" class="annot-text" text-anchor="middle">कठोर होकर जिप्सम बनता है</text>
          
          <!-- Plaster of Paris Box (Right) -->
          <g transform="translate(500, 70)">
            <rect x="0" y="0" width="220" height="90" class="box-rect" />
            <text x="110" y="30" class="box-title" text-anchor="middle">प्लास्टर ऑफ पेरिस (PoP)</text>
            <text x="110" y="52" class="box-sub" text-anchor="middle" font-weight="bold">CaSO₄&middot;0.5H₂O</text>
            <text x="110" y="72" class="box-sub" text-anchor="middle">महीन सफेद पाउडर</text>
          </g>
        </svg>"""
    }
]

practice_questions = [
    {
        "q": "What is the pH of a neutral solution at 25°C?",
        "q_hi": "25°C पर एक उदासीन विलयन का पीएच (pH) क्या होता है?",
        "opts": ["0", "7", "14", "5.6"],
        "opts_hi": ["0", "7 (7)", "14", "5.6"],
        "ans": 1,
        "sol": "A neutral solution (like pure water) has a pH of 7 at 25°C.",
        "sol_hi": "25°C पर एक उदासीन विलयन (जैसे शुद्ध जल) का पीएच मान 7 होता है।"
    },
    {
        "q": "Which acid is present in ant stings and nettle leaf hair?",
        "q_hi": "चींटी के डंक और नेटल (बिच्छू बूटी) के पत्तों में कौन सा अम्ल मौजूद होता है?",
        "opts": ["Acetic acid", "Citric acid", "Methanoic acid", "Tartaric acid"],
        "opts_hi": ["एसिटिक अम्ल", "साइट्रिक अम्ल", "मेथेनॉइक अम्ल (Methanoic acid)", "टार्टरिक अम्ल"],
        "ans": 2,
        "sol": "Methanoic acid (also known as formic acid, HCOOH) is present in ant stings and nettle stings, causing a burning pain.",
        "sol_hi": "चींटी के डंक और नेटल के डंक में मेथेनॉइक अम्ल (जिसे फॉर्मिक अम्ल, HCOOH भी कहा जाता है) मौजूद होता है, जो जलन और दर्द का कारण बनता है।"
    },
    {
        "q": "What color does phenolphthalein turn in a basic solution?",
        "q_hi": "क्षारीय विलयन में फिनोलफ्थेलीन (phenolphthalein) का रंग कैसा हो जाता है?",
        "opts": ["Red", "Pink", "Yellow", "Colorless"],
        "opts_hi": ["लाल", "गुलाबी (Pink)", "पीला", "रंगहीन"],
        "ans": 1,
        "sol": "Phenolphthalein is synthetic indicator that remains colorless in acidic solutions and turns pink in basic solutions.",
        "sol_hi": "फिनोलफ्थेलीन एक कृत्रिम सूचक है जो अम्लीय विलयन में रंगहीन रहता है और क्षारीय विलयन में गुलाबी हो जाता है।"
    },
    {
        "q": "Which of the following is water soluble base (alkali)?",
        "q_hi": "निम्नलिखित में से कौन सा जल में विलेय क्षारक (Alkali) है?",
        "opts": ["Sodium Hydroxide", "Potassium Hydroxide", "Calcium Hydroxide", "All of the above"],
        "opts_hi": ["सोडियम हाइड्रोक्साइड", "पोटेशियम हाइड्रोक्साइड", "कैल्शियम हाइड्रोक्साइड", "उपरोक्त सभी (All of the above)"],
        "ans": 3,
        "sol": "Bases that are soluble in water are called alkalis. NaOH, KOH, and Ca(OH)₂ are all soluble in water.",
        "sol_hi": "जल में घुलनशील क्षारकों को क्षार (alkalis) कहा जाता है। NaOH, KOH और Ca(OH)₂ ये सभी जल में विलेय हैं।"
    },
    {
        "q": "Bleaching powder is chemically designated as:",
        "q_hi": "रासायनिक रूप से विरंजक चूर्ण (Bleaching powder) को किस नाम से जाना जाता है?",
        "opts": ["Calcium Chloride", "Calcium Carbonate", "Calcium Oxychloride", "Calcium Sulfate"],
        "opts_hi": ["कैल्शियम क्लोराइड", "कैल्शियम कार्बोनेट", "कैल्शियम ऑक्सीक्लोराइड (Calcium Oxychloride)", "कैल्शियम सल्फेट"],
        "ans": 2,
        "sol": "Bleaching powder is Calcium Oxychloride (CaOCl₂), prepared by the action of chlorine gas on dry slaked lime.",
        "sol_hi": "विरंजक चूर्ण कैल्शियम ऑक्सीक्लोराइड (CaOCl₂) है, जो शुष्क बुझे हुए चूने पर क्लोरीन गैस की क्रिया द्वारा तैयार किया जाता है।"
    },
    {
        "q": "Which gas is released when an acid reacts with a metal?",
        "q_hi": "जब कोई अम्ल किसी धातु के साथ अभिक्रिया करता है, तो कौन सी गैस निकलती है?",
        "opts": ["Oxygen", "Carbon dioxide", "Hydrogen", "Nitrogen"],
        "opts_hi": ["ऑक्सीजन", "कार्बन डाइऑक्साइड", "हाइड्रोजन (Hydrogen)", "नाइट्रोजन"],
        "ans": 2,
        "sol": "Acids react with active metals to produce a metal salt and release hydrogen gas (H₂), which burns with a pop sound.",
        "sol_hi": "अम्ल सक्रिय धातुओं के साथ अभिक्रिया करके धातु लवण बनाते हैं और हाइड्रोजन गैस (H₂) मुक्त करते हैं, जो पॉप ध्वनि के साथ जलती है।"
    },
    {
        "q": "What is the chemical name and formula of Baking Soda?",
        "q_hi": "बेकिंग सोडा (Baking Soda) का रासायनिक नाम और सूत्र क्या है?",
        "opts": ["Sodium Carbonate, Na₂CO₃", "Sodium Hydrogen Carbonate, NaHCO₃", "Sodium Hydroxide, NaOH", "Sodium Chloride, NaCl"],
        "opts_hi": ["सोडियम कार्बोनेट, Na₂CO₃", "सोडियम हाइड्रोजन कार्बोनेट, NaHCO₃ (NaHCO₃)", "सोडियम हाइड्रोक्साइड, NaOH", "सोडियम क्लोराइड, NaCl"],
        "ans": 1,
        "sol": "Baking soda is Sodium Hydrogen Carbonate or Sodium Bicarbonate (NaHCO₃).",
        "sol_hi": "बेकिंग सोडा सोडियम हाइड्रोजन कार्बोनेट या सोडियम बाइकार्बोनेट (NaHCO₃) है।"
    },
    {
        "q": "Which indicator is an olfactory indicator?",
        "q_hi": "निम्नलिखित में से कौन सा गंधीय सूचक (Olfactory indicator) है?",
        "opts": ["Litmus", "Methyl orange", "Onion", "Turmeric"],
        "opts_hi": ["लिटमस", "मिथाइल ऑरेंज", "प्याज (Onion)", "हल्दी"],
        "ans": 2,
        "sol": "Olfactory indicators change their odor depending on whether they are in acidic or basic medium. Onion, vanilla, and clove are examples.",
        "sol_hi": "गंधीय सूचक अम्लीय या क्षारीय माध्यम के आधार पर अपनी गंध बदलते हैं। प्याज, वैनिला और लौंग इसके उदाहरण हैं।"
    },
    {
        "q": "Tooth decay starts when the pH of the mouth is lower than:",
        "q_hi": "दंत क्षय तब शुरू होता है जब मुंह का पीएच किससे कम होता है?",
        "opts": ["7.0", "5.5", "6.5", "8.2"],
        "opts_hi": ["7.0", "5.5 (5.5)", "6.5", "8.2"],
        "ans": 1,
        "sol": "Bacteria in the mouth degrade sugar food particles to produce acid. When the pH drops below 5.5, tooth enamel (calcium phosphate) starts dissolving.",
        "sol_hi": "मुंह में मौजूद बैक्टीरिया शर्करा युक्त खाद्य कणों को अपघटित कर अम्ल बनाते हैं। जब पीएच 5.5 से नीचे गिर जाता है, तो दांतों का इनेमल (कैल्शियम फॉस्फेट) घुलना शुरू हो जाता है।"
    },
    {
        "q": "Acid rain occurs when the pH of rainwater drops below:",
        "q_hi": "अम्ल वर्षा (Acid rain) तब होती है जब वर्षा जल का पीएच किससे नीचे गिर जाता है?",
        "opts": ["7.0", "6.5", "5.6", "8.0"],
        "opts_hi": ["7.0", "6.5", "5.6 (5.6)", "8.0"],
        "ans": 2,
        "sol": "Rainwater is slightly acidic due to dissolved CO₂. However, when sulfur and nitrogen oxides form acids, dropping pH below 5.6, it is classified as acid rain.",
        "sol_hi": "घुलनशील CO₂ के कारण वर्षा जल थोड़ा अम्लीय होता है। हालाँकि, जब सल्फर और नाइट्रोजन के ऑक्साइड अम्ल बनाते हैं और पीएच 5.6 से नीचे गिर जाता है, तो इसे अम्ल वर्षा के रूप में वर्गीकृत किया जाता है।"
    },
    {
        "q": "Which of the following is a strong base?",
        "q_hi": "निम्नलिखित में से कौन सा एक प्रबल क्षारक (Strong base) है?",
        "opts": ["Ammonium Hydroxide", "Calcium Hydroxide", "Sodium Hydroxide", "Magnesium Hydroxide"],
        "opts_hi": ["अमोनियम हाइड्रोक्साइड", "कैल्शियम हाइड्रोक्साइड", "सोडियम हाइड्रोक्साइड (NaOH)", "मैग्नीशियम हाइड्रोक्साइड"],
        "ans": 2,
        "sol": "Sodium Hydroxide (NaOH) and Potassium Hydroxide (KOH) are strong bases because they undergo complete dissociation in aqueous solutions.",
        "sol_hi": "सोडियम हाइड्रोक्साइड (NaOH) और पोटेशियम हाइड्रोक्साइड (KOH) प्रबल क्षारक हैं क्योंकि वे जलीय विलयनों में पूरी तरह से आयनित हो जाते हैं।"
    },
    {
        "q": "The reaction: Acid + Base &rarr; Salt + Water is called a:",
        "q_hi": "अभिक्रिया: अम्ल + क्षारक &rarr; लवण + जल कहलाती है:",
        "opts": ["Decomposition reaction", "Combination reaction", "Neutralization reaction", "Displacement reaction"],
        "opts_hi": ["अपघटन अभिक्रिया", "संयोजन अभिक्रिया", "उदासीनीकरण अभिक्रिया (Neutralization)", "विस्थापन अभिक्रिया"],
        "ans": 2,
        "sol": "A neutralization reaction occurs when an acid and base react to form a salt and water, usually releasing heat.",
        "sol_hi": "उदासीनीकरण अभिक्रिया तब होती है जब एक अम्ल और क्षारक आपस में क्रिया करके लवण और जल बनाते हैं, जिसमें आमतौर पर ऊष्मा निकलती है।"
    },
    {
        "q": "What is the chemical formula of Plaster of Paris?",
        "q_hi": "प्लास्टर ऑफ पेरिस का रासायनिक सूत्र क्या है?",
        "opts": ["CaSO₄&middot;2H₂O", "CaSO₄&middot;0.5H₂O", "CaSO₄&middot;H₂O", "CaCO₃"],
        "opts_hi": ["CaSO₄&middot;2H₂O", "CaSO₄&middot;0.5H₂O (CaSO₄·0.5H₂O)", "CaSO₄&middot;H₂O", "CaCO₃"],
        "ans": 1,
        "sol": "Plaster of Paris is calcium sulfate hemihydrate with the formula CaSO₄&middot;0.5H₂O (or 2CaSO₄&middot;H₂O).",
        "sol_hi": "प्लास्टर ऑफ पेरिस कैल्शियम सल्फेट हेमीहाइड्रेट है जिसका सूत्र CaSO₄&middot;0.5H₂O (या 2CaSO₄&middot;H₂O) होता है।"
    },
    {
        "q": "Which acid is found in vinegar?",
        "q_hi": "सिरके (Vinegar) में कौन सा अम्ल पाया जाता है?",
        "opts": ["Citric acid", "Lactic acid", "Methanoic acid", "Acetic acid"],
        "opts_hi": ["साइट्रिक अम्ल", "लैक्टिक अम्ल", "मेथेनॉइक अम्ल", "एसिटिक अम्ल (Acetic acid)"],
        "ans": 3,
        "sol": "Vinegar is a 5-8% aqueous solution of acetic acid (ethanoic acid, CH₃COOH).",
        "sol_hi": "सिरका एसिटिक अम्ल (एथेनॉइक अम्ल, CH₃COOH) का 5-8% जलीय विलयन है।"
    },
    {
        "q": "Washing Soda contains how many water molecules of crystallization?",
        "q_hi": "धावन सोडा (Washing Soda) में क्रिस्टलीकरण के कितने जल के अणु होते हैं?",
        "opts": ["2", "5", "7", "10"],
        "opts_hi": ["2", "5", "7", "10 (10)"],
        "ans": 3,
        "sol": "Washing soda is Sodium Carbonate Decahydrate, which has the formula Na₂CO₃&middot;10H₂O. Thus, it has 10 water molecules of crystallization.",
        "sol_hi": "धावन सोडा सोडियम कार्बोनेट डेकाहाइड्रेट है, जिसका सूत्र Na₂CO₃&middot;10H₂O होता है। अतः इसमें क्रिस्टलीकरण के 10 जल अणु होते हैं।"
    },
    {
        "q": "What happens when an acid reacts with a metal carbonate?",
        "q_hi": "जब कोई अम्ल किसी धातु कार्बोनेट के साथ अभिक्रिया करता है तो क्या होता है?",
        "opts": ["Oxygen gas is evolved", "Carbon dioxide gas is evolved", "Hydrogen gas is evolved", "No reaction occurs"],
        "opts_hi": ["ऑक्सीजन गैस निकलती है", "कार्बन डाइऑक्साइड गैस निकलती है (CO₂ gas is evolved)", "हाइड्रोजन गैस निकलती है", "कोई अभिक्रिया नहीं होती"],
        "ans": 1,
        "sol": "Acids react with metal carbonates and hydrogen carbonates to produce salt, water, and carbon dioxide gas (which turns lime water milky).",
        "sol_hi": "अम्ल धातु कार्बोनेट और हाइड्रोजन कार्बोनेट के साथ अभिक्रिया करके लवण, जल और कार्बन डाइऑक्साइड गैस (जो चूने के पानी को दूधिया कर देती है) बनाते हैं।"
    },
    {
        "q": "Which substance is used to cure honeybee stings?",
        "q_hi": "मधुमक्खी के डंक के दर्द निवारण के लिए किस पदार्थ का उपयोग किया जाता है?",
        "opts": ["Vinegar", "Baking soda paste", "Lemon juice", "Concentrated HCl"],
        "opts_hi": ["सिरका", "बेकिंग सोडा का पेस्ट (Baking soda paste)", "नींबू का रस", "सांद्र HCl"],
        "ans": 1,
        "sol": "Bee sting contains formic acid. Applying a mild base like baking soda (NaHCO₃) paste neutralizes the acid and provides relief.",
        "sol_hi": "मधुमक्खी के डंक में फॉर्मिक अम्ल होता है। बेकिंग सोडा (NaHCO₃) जैसे हल्के क्षारक का पेस्ट लगाने से अम्ल उदासीन हो जाता है और दर्द से राहत मिलती है।"
    },
    {
        "q": "Pure water and blood have pH values of approximately:",
        "q_hi": "शुद्ध जल और रक्त का पीएच मान लगभग कितना होता है?",
        "opts": ["7.0 and 7.4", "6.0 and 8.0", "7.0 and 5.6", "1.0 and 14.0"],
        "opts_hi": ["7.0 और 7.4 (7.0 and 7.4)", "6.0 और 8.0", "7.0 और 5.6", "1.0 और 14.0"],
        "ans": 0,
        "sol": "Pure water is neutral with a pH of 7.0. Blood is slightly alkaline/basic with a pH of around 7.4.",
        "sol_hi": "शुद्ध जल 7.0 पीएच के साथ उदासीन होता है। रक्त लगभग 7.4 पीएच के साथ थोड़ा क्षारीय होता है।"
    },
    {
        "q": "According to Lewis theory, an acid is an:",
        "q_hi": "लुईस सिद्धांत के अनुसार, एक अम्ल होता है:",
        "opts": ["Proton donor", "Proton acceptor", "Electron pair acceptor", "Electron pair donor"],
        "opts_hi": ["प्रोटॉन दाता", "प्रोटॉन ग्राही", "इलेक्ट्रॉन युग्म ग्राही (Electron pair acceptor)", "इलेक्ट्रॉन युग्म दाता"],
        "ans": 2,
        "sol": "Lewis defined acids as substances that can accept a pair of electrons (e.g., BF₃, AlCl₃, H⁺).",
        "sol_hi": "लुईस ने अम्लों को उन पदार्थों के रूप में परिभाषित किया जो एक इलेक्ट्रॉन युग्म को स्वीकार कर सकते हैं (जैसे BF₃, AlCl₃, H⁺)।"
    },
    {
        "q": "Which acid is present in tamarind and grapes?",
        "q_hi": "इमली और अंगूर में कौन सा अम्ल मौजूद होता है?",
        "opts": ["Citric acid", "Tartaric acid", "Oxalic acid", "Methanoic acid"],
        "opts_hi": ["साइट्रिक अम्ल", "टार्टरिक अम्ल (Tartaric acid)", "ऑक्सेलिक अम्ल", "मेथेनॉइक अम्ल"],
        "ans": 1,
        "sol": "Tamarind and grapes contain tartaric acid. Tomatoes contain oxalic acid, and citrus fruits like lemon contain citric acid.",
        "sol_hi": "इमली और अंगूर में टार्टरिक अम्ल होता है। टमाटर में ऑक्सेलिक अम्ल और खट्टे फलों जैसे नींबू में साइट्रिक अम्ल होता है।"
    },
    {
        "q": "Gypsum is chemically:",
        "q_hi": "रासायनिक रूप से जिप्सम (Gypsum) क्या है?",
        "opts": ["Calcium sulfate hemihydrate", "Calcium sulfate dihydrate", "Calcium carbonate decahydrate", "Magnesium sulfate heptahydrate"],
        "opts_hi": ["कैल्शियम सल्फेट हेमीहाइड्रेट", "कैल्शियम सल्फेट डाइहाइड्रेट (Calcium sulfate dihydrate)", "कैल्शियम कार्बोनेट डेकाहाइड्रेट", "मैग्नीशियम सल्फेट हेप्टाहाइड्रेट"],
        "ans": 1,
        "sol": "Gypsum is Calcium Sulfate Dihydrate (CaSO₄&middot;2H₂O). When heated to 373 K, it loses water to form Plaster of Paris.",
        "sol_hi": "जिप्सम कैल्शियम सल्फेट डाइहाइड्रेट (CaSO₄&middot;2H₂O) है। 373 K पर गर्म करने पर यह जल के अणु खोकर प्लास्टर ऑफ पेरिस बनाता है।"
    },
    {
        "q": "The gas that turns lime water milky is:",
        "q_hi": "चूने के पानी को दूधिया करने वाली गैस है:",
        "opts": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "opts_hi": ["ऑक्सीजन", "नाइट्रोजन", "कार्बन डाइऑक्साइड (Carbon dioxide)", "हाइड्रोजन"],
        "ans": 2,
        "sol": "Carbon dioxide (CO₂) reacts with lime water [Ca(OH)₂] to form a white precipitate of Calcium Carbonate (CaCO₃), which turns the solution milky.",
        "sol_hi": "कार्बन डाइऑक्साइड (CO₂) चूने के पानी [Ca(OH)₂] के साथ अभिक्रिया करके कैल्शियम कार्बोनेट (CaCO₃) का सफेद अवक्षेप बनाता है, जिससे विलयन दूधिया हो जाता है।"
    },
    {
        "q": "What is the common name of Sodium Hydroxide?",
        "q_hi": "सोडियम हाइड्रोक्साइड का सामान्य नाम क्या है?",
        "opts": ["Baking soda", "Washing soda", "Caustic soda", "Bleaching powder"],
        "opts_hi": ["बेकिंग सोडा", "धावन सोडा", "कास्टिक सोडा (Caustic soda)", "विरंजक चूर्ण"],
        "ans": 2,
        "sol": "Sodium Hydroxide (NaOH) is commonly known as Caustic Soda. It is a strong base/alkali.",
        "sol_hi": "सोडियम हाइड्रोक्साइड (NaOH) को आमतौर पर कास्टिक सोडा के रूप में जाना जाता है। यह एक प्रबल क्षारक/क्षार है।"
    },
    {
        "q": "Which of the following is a weak acid?",
        "q_hi": "निम्नलिखित में से कौन सा एक दुर्बल अम्ल (Weak acid) है?",
        "opts": ["Hydrochloric acid", "Sulfuric acid", "Nitric acid", "Acetic acid"],
        "opts_hi": ["हाइड्रोक्लोरिक अम्ल", "सल्फ्यूरिक अम्ल", "नाइट्रिक अम्ल", "एसिटिक अम्ल (Acetic acid)"],
        "ans": 3,
        "sol": "Acetic acid (CH₃COOH) is a weak organic acid because it does not fully ionize in water. HCl, H₂SO₄, and HNO₃ are strong mineral acids.",
        "sol_hi": "एसिटिक अम्ल (CH₃COOH) एक दुर्बल कार्बनिक अम्ल है क्योंकि यह पानी में पूरी तरह से आयनित नहीं होता है। HCl, H₂SO₄ और HNO₃ प्रबल खनिज अम्ल हैं।"
    },
    {
        "q": "The range of pH values for acidic solutions is:",
        "q_hi": "अम्लीय विलयनों के लिए पीएच (pH) मानों का परास होता है:",
        "opts": ["Exactly 7", "Between 7 and 14", "Between 0 and 7", "None of these"],
        "opts_hi": ["ठीक 7", "7 और 14 के बीच", "0 और 7 के बीच (Between 0 and 7)", "इनमें से कोई नहीं"],
        "ans": 2,
        "sol": "Acidic solutions have a pH value less than 7 (between 0 and 7). Basic solutions have a pH greater than 7.",
        "sol_hi": "अम्लीय विलयनों का पीएच मान 7 से कम (0 और 7 के बीच) होता है। क्षारीय विलयनों का पीएच 7 से अधिक होता है।"
    },
    {
        "q": "What is the byproduct gas released at the anode during the Chlor-alkali process?",
        "q_hi": "क्लोर-एल्कली प्रक्रिया के दौरान एनोड पर कौन सी सह-उत्पाद गैस निकलती है?",
        "opts": ["Hydrogen gas", "Chlorine gas", "Oxygen gas", "Carbon dioxide"],
        "opts_hi": ["हाइड्रोजन gas", "क्लोरीन गैस (Chlorine gas)", "ऑक्सीजन गैस", "कार्बन डाइऑक्साइड"],
        "ans": 1,
        "sol": "During the electrolysis of brine (Chlor-alkali process), Chlorine gas is released at the anode, and Hydrogen gas is released at the cathode.",
        "sol_hi": "क्लोर-एल्कली प्रक्रिया (नमक के जलीय विलयन का विद्युत अपघटन) में एनोड पर chlorine gas और कैथोड पर हाइड्रोजन गैस निकलती है।"
    },
    {
        "q": "Which plant leaf is used as traditional remedy for nettle stings?",
        "q_hi": "नेटल (बिच्छू बूटी) के डंक के पारंपरिक उपचार के रूप में किस पौधे की पत्ती का उपयोग किया जाता है?",
        "opts": ["Nettle leaf", "Dock plant leaf", "Mint leaf", "Coriander leaf"],
        "opts_hi": ["नेटल की पत्ती", "डॉक पौधे की पत्ती (Dock plant leaf)", "पुदीने की पत्ती", "धनिया की पत्ती"],
        "ans": 1,
        "sol": "The nettle sting injects methanoic acid. Rubbing the leaf of the dock plant, which grows nearby and contains basic juices, neutralizes the acid.",
        "sol_hi": "नेटल का डंक मेथेनॉइक अम्ल छोड़ता है। इसके पास ही उगने वाले डॉक पौधे (Dock plant) की पत्ती को रगड़ने से, जिसका रस क्षारीय होता है, अम्ल उदासीन हो जाता है।"
    },
    {
        "q": "The formula of copper sulfate crystals (Blue Vitriol) is:",
        "q_hi": "कॉपर सल्फेट क्रिस्टल (नीला थोथा / नीला कसीस) का सूत्र है:",
        "opts": ["CuSO₄&middot;2H₂O", "CuSO₄&middot;5H₂O", "CuSO₄&middot;7H₂O", "CuSO₄"],
        "opts_hi": ["CuSO₄&middot;2H₂O", "CuSO₄&middot;5H₂O (CuSO₄·5H₂O)", "CuSO₄&middot;7H₂O", "CuSO₄"],
        "ans": 1,
        "sol": "Copper sulfate pentahydrate (CuSO₄&middot;5H₂O) has blue color due to the presence of 5 water molecules of crystallization.",
        "sol_hi": "कॉपर सल्फेट पेंटाहाइड्रेट (CuSO₄&middot;5H₂O) में क्रिस्टलीकरण के 5 जल अणुओं की उपस्थिति के कारण इसका रंग नीला होता है।"
    },
    {
        "q": "Which acid is present in tomato?",
        "q_hi": "टमाटर में कौन सा अम्ल मौजूद होता है?",
        "opts": ["Citric acid", "Oxalic acid", "Acetic acid", "Tartaric acid"],
        "opts_hi": ["साइट्रिक अम्ल", "ऑक्सेलिक अम्ल (Oxalic acid)", "एसिटिक अम्ल", "टार्टरिक अम्ल"],
        "ans": 1,
        "sol": "Tomatoes contain oxalic acid. Citrus fruits contain citric acid, and vinegar contains acetic acid.",
        "sol_hi": "टमाटर में ऑक्सेलिक अम्ल होता है। खट्टे फलों में साइट्रिक अम्ल और सिरके में एसिटिक अम्ल होता है।"
    },
    {
        "q": "Which of the following is water-insoluble base?",
        "q_hi": "निम्नलिखित में से कौन सा जल में अघुलनशील क्षारक है?",
        "opts": ["NaOH", "KOH", "Fe(OH)₃", "Ca(OH)₂"],
        "opts_hi": ["NaOH", "KOH", "Fe(OH)₃ (Ferric Hydroxide)", "Ca(OH)₂"],
        "ans": 2,
        "sol": "Ferric Hydroxide [Fe(OH)₃] and Copper Hydroxide [Cu(OH)₂] are bases but they are insoluble in water, so they are not alkalis. NaOH and KOH are highly soluble alkalis.",
        "sol_hi": "फेरिक हाइड्रोक्साइड [Fe(OH)₃] और कॉपर हाइड्रोक्साइड [Cu(OH)₂] क्षारक हैं लेकिन वे जल में अघुलनशील हैं, इसलिए वे क्षार (alkalis) नहीं हैं। NaOH और KOH अत्यधिक विलेय क्षार हैं।"
    },
    {
        "q": "What is the ratio of concentrated HCl to concentrated HNO₃ in Aqua Regia?",
        "q_hi": "अम्लराज (Aqua Regia) में सांद्र HCl और सांद्र HNO₃ का अनुपात क्या होता है?",
        "opts": ["1:3", "3:1", "1:1", "3:2"],
        "opts_hi": ["1:3", "3:1 (3:1)", "1:1", "3:2"],
        "ans": 1,
        "sol": "Aqua Regia (Royal Water) is a freshly prepared mixture of concentrated HCl and concentrated HNO₃ in a 3:1 ratio by volume.",
        "sol_hi": "अम्लराज (Aqua Regia / रॉयल वाटर) सांद्र HCl और सांद्र HNO₃ का आयतन के अनुसार 3:1 के अनुपात में ताजा बना मिश्रण होता है।"
    },
    {
        "q": "Which acid is present in aerated soft drinks and soda water?",
        "q_hi": "शीतल पेय (Soft drinks) और सोडा वाटर में कौन सा अम्ल मौजूद होता है?",
        "opts": ["Carbonic acid", "Citric acid", "Hydrochloric acid", "Sulfuric acid"],
        "opts_hi": ["कार्बोनिक अम्ल (Carbonic acid)", "साइट्रिक अम्ल", "हाइड्रोक्लोरिक अम्ल", "सल्फ्यूरिक अम्ल"],
        "ans": 0,
        "sol": "Soda water and aerated drinks contain dissolved carbon dioxide under pressure, which forms weak Carbonic acid (H₂CO₃).",
        "sol_hi": "सोडा वाटर और शीतल पेय पदार्थों में उच्च दाब पर कार्बन डाइऑक्साइड घुली होती है, जो जल से क्रिया कर दुर्बल कार्बोनिक अम्ल (H₂CO₃) बनाती है।"
    },
    {
        "q": "Potash Alum (fitkari) is commonly used in water purification for:",
        "q_hi": "पानी के शुद्धिकरण में फिटकरी (Potash Alum) का उपयोग मुख्य रूप से किसलिए किया जाता है?",
        "opts": ["Killing bacteria", "Coagulation / Loading of suspended impurities", "Removing permanent hardness", "Adding taste to water"],
        "opts_hi": ["बैक्टीरिया को मारने के लिए", "निलंबित अशुद्धियों के स्कंदन (Coagulation) के लिए", "स्थायी कठोरता दूर करने के लिए", "पानी में स्वाद बढ़ाने के लिए"],
        "ans": 1,
        "sol": "Potash Alum is a double salt (K₂SO₄·Al₂(SO₄)₃·24H₂O) which acts as coagulating agent, helping suspended colloidal impurities to settle down.",
        "sol_hi": "फिटकरी एक द्विक लवण (double salt) है जो एक स्कंदक (coagulator) के रूप में कार्य करता है, जिससे पानी में निलंबित कोलाइडल अशुद्धियों को नीचे बैठने में मदद मिलती है।"
    },
    {
        "q": "Which of the following is chemically known as Green Vitriol?",
        "q_hi": "निम्नलिखित में से किसे रासायनिक रूप से हरा कसीस (Green Vitriol) कहा जाता है?",
        "opts": ["Copper sulfate pentahydrate", "Iron(II) sulfate heptahydrate", "Zinc sulfate heptahydrate", "Magnesium sulfate heptahydrate"],
        "opts_hi": ["कॉपर सल्फेट पेंटाहाइड्रेट", "आयरन(II) सल्फेट हेप्टाहाइड्रेट (FeSO₄·7H₂O)", "जिंक सल्फेट हेप्टाहाइड्रेट", "मैग्नीशियम सल्फेट हेप्टाहाइड्रेट"],
        "ans": 1,
        "sol": "Green Vitriol is Iron(II) Sulfate Heptahydrate (FeSO₄&middot;7H₂O). Blue Vitriol is CuSO₄&middot;5H₂O, and White Vitriol is ZnSO₄&middot;7H₂O.",
        "sol_hi": "हरा कसीस (Green Vitriol) आयरन(II) सल्फेट हेप्टाहाइड्रेट (FeSO₄&middot;7H₂O) है। नीला थोथा CuSO₄&middot;5H₂O होता है, और उजला थोथा ZnSO₄&middot;7H₂O होता है।"
    },
    {
        "q": "Which acid is present in apples?",
        "q_hi": "सेब में कौन सा अम्ल मौजूद होता है?",
        "opts": ["Malic acid", "Oxalic acid", "Citric acid", "Formic acid"],
        "opts_hi": ["मैलिक अम्ल (Malic acid)", "ऑक्सेलिक अम्ल", "साइट्रिक अम्ल", "फॉर्मिक अम्ल"],
        "ans": 0,
        "sol": "Apples contain Malic acid (from the Latin malum, meaning apple). Tomatoes contain oxalic acid, lemons contain citric acid, and ants contain formic acid.",
        "sol_hi": "सेब में  मैलिक अम्ल (Malic acid) होता है। टमाटर में ऑक्सेलिक अम्ल, नींबू में साइट्रिक अम्ल और चींटियों में फॉर्मिक अम्ल होता है।"
    },
    {
        "q": "What is formed when Gypsum is heated above 373 K (100°C), resulting in the loss of all water of crystallization?",
        "q_hi": "जब जिप्सम को 373 K (100°C) से अधिक गर्म किया जाता है, जिससे क्रिस्टलीकरण का सारा जल नष्ट हो जाता है, तो क्या बनता है?",
        "opts": ["Plaster of Paris", "Dead Burnt Plaster", "Slaked Lime", "Anhydrous Copper Sulfate"],
        "opts_hi": ["प्लास्टर ऑफ पेरिस", "मृत तापित प्लास्टर (Dead Burnt Plaster)", "बुझा हुआ चूना", "निर्जल कॉपर सल्फेट"],
        "ans": 1,
        "sol": "Heating gypsum above 373 K removes all crystallization water, yielding anhydrous calcium sulfate (CaSO₄), known as Dead Burnt Plaster. It lacks setting properties.",
        "sol_hi": "जिप्सम को 373 K से ऊपर गर्म करने पर क्रिस्टलीकरण का संपूर्ण जल समाप्त हो जाता है, जिससे निर्जल कैल्शियम सल्फेट (CaSO₄) बनता है, जिसे मृत तापित प्लास्टर कहा जाता है। इसमें जमने के गुण नहीं होते।"
    },
    {
        "q": "The property of Washing Soda losing its water of crystallization when exposed to dry air is called:",
        "q_hi": "शुष्क हवा के संपर्क में आने पर धावन सोडा द्वारा अपने क्रिस्टलीकरण का जल खोने के गुण को क्या कहा जाता है?",
        "opts": ["Deliquescence", "Efflorescence", "Sublimation", "Dehydration"],
        "opts_hi": ["प्रस्वेदन (Deliquescence)", "उत्फुल्लन (Efflorescence)", "उर्ध्वपातन", "निर्जलीकरण"],
        "ans": 1,
        "sol": "Washing soda (Na₂CO₃·10H₂O) loses 9 water molecules to form sodium carbonate monohydrate (Na₂CO₃·H₂O) when exposed to air. This property is known as efflorescence.",
        "sol_hi": "धावन सोडा (Na₂CO₃·10H₂O) हवा के संपर्क में आने पर 9 जल अणुओं को खोकर सोडियम कार्बोनेट मोनोहाइड्रेट बनाता है। इस गुण को उत्फुल्लन (Efflorescence) कहा जाता है।"
    },
    {
        "q": "Which chemical compound is known as 'Hypo' and is widely used in photography for fixing films?",
        "q_hi": "किस रासायनिक यौगिक को 'हाइपो' कहा जाता है और फोटोग्राफी में फिल्मों को फिक्स करने के लिए बड़े पैमाने पर उपयोग किया जाता है?",
        "opts": ["Sodium thiosulfate", "Sodium sulfate", "Ammonium chloride", "Silver bromide"],
        "opts_hi": ["सोडियम थायोसल्फेट (Sodium thiosulfate)", "सोडियम सल्फेट", "अमोनियम क्लोराइड", "सिल्वर ब्रोमाइड"],
        "ans": 0,
        "sol": "Sodium thiosulfate pentahydrate (Na₂S₂O₃·5H₂O), commonly called Hypo, is used in photography as a fixer because it dissolves unreacted silver halides.",
        "sol_hi": "सोडियम थायोसल्फेट पेंटाहाइड्रेट (Na₂S₂O₃·5H₂O) को सामान्यतः हाइपो कहा जाता है, जिसका उपयोग फोटोग्राफी में फिक्सर के रूप में अघुलनशील सिल्वर हैलाइड को घोलने के लिए किया जाता है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "What is the conjugate acid of NH₃ according to Brønsted-Lowry theory?",
        "q_hi": "ब्रोंस्टेड-लोरी सिद्धांत के अनुसार NH₃ का संयुग्मी अम्ल (conjugate acid) क्या है?",
        "opts": ["NH₂⁻", "NH₄⁺", "NH₄OH", "HNO₃"],
        "opts_hi": ["NH₂⁻", "NH₄⁺ (NH₄⁺)", "NH₄OH", "HNO₃"],
        "ans": 1,
        "sol": "According to Brønsted-Lowry, a conjugate acid is formed when a base accepts a proton. NH₃ + H⁺ &rarr; NH₄⁺.",
        "sol_hi": "ब्रोंस्टेड-लोरी के अनुसार, जब कोई क्षारक प्रोटॉन स्वीकार करता है तो संयुग्मी अम्ल बनता है। NH₃ + H⁺ &rarr; NH₄⁺।"
    },
    {
        "q": "The color of methyl orange indicator in an acidic solution is:",
        "q_hi": "अम्लीय विलयन में मिथाइल ऑरेंज सूचक का रंग होता है:",
        "opts": ["Yellow", "Orange", "Red", "Pink"],
        "opts_hi": ["पीला", "नारंगी", "लाल (Red)", "गुलाबी"],
        "ans": 2,
        "sol": "Methyl orange turns red in acidic solutions (pH < 3.1) and yellow in basic solutions (pH > 4.4).",
        "sol_hi": "मिथाइल ऑरेंज अम्लीय विलयन में लाल (pH < 3.1) और क्षारीय विलयन में पीला (pH > 4.4) हो जाता है।"
    },
    {
        "q": "Which substance is added to acidic soil by farmers to neutralize it?",
        "q_hi": "मिट्टी की अम्लीयता को उदासीन करने के लिए किसानों द्वारा उसमें क्या मिलाया जाता है?",
        "opts": ["Gypsum", "Quicklime (CaO) or Slaked lime [Ca(OH)₂]", "Ammonium sulfate", "Citric acid"],
        "opts_hi": ["जिप्सम", "बिना बुझा चूना (CaO) या बुझा हुआ चूना [Ca(OH)₂]", "अमोनियम सल्फेट", "साइट्रिक अम्ल"],
        "ans": 1,
        "sol": "If the soil is too acidic, it is treated with bases like quicklime (calcium oxide) or slaked lime (calcium hydroxide) or chalk (calcium carbonate) to raise the pH.",
        "sol_hi": "यदि मिट्टी बहुत अम्लीय है, तो पीएच बढ़ाने के लिए उसमें बिना बुझा चूना (कैल्शियम ऑक्साइड) या बुझा हुआ चूना (कैल्शियम हाइड्रोक्साइड) या चाक जैसे क्षारक मिलाए जाते हैं।"
    },
    {
        "q": "Which of the following compounds is a Lewis Acid but not an Arrhenius acid?",
        "q_hi": "निम्नलिखित में से कौन सा यौगिक लुईस अम्ल है लेकिन आरहेनियस अम्ल नहीं है?",
        "opts": ["HCl", "H₂SO₄", "BF₃", "HNO₃"],
        "opts_hi": ["HCl", "H₂SO₄", "BF₃ (Boron Trifluoride)", "HNO₃"],
        "ans": 2,
        "sol": "Boron Trifluoride (BF₃) has an incomplete octet and can accept an electron pair (Lewis Acid), but it doesn't contain or release hydrogen ions in water (Arrhenius acid).",
        "sol_hi": "बोरोन ट्राइफ्लोराइड (BF₃) का अष्टक अपूर्ण होता है और यह एक इलेक्ट्रॉन युग्म स्वीकार कर सकता है (लुईस अम्ल), लेकिन इसमें जल में हाइड्रोजन आयन मुक्त करने की क्षमता नहीं होती (आरहेनियस अम्ल)।"
    },
    {
        "q": "A solution reacts with crushed egg-shells to give a gas that turns lime-water milky. The solution contains:",
        "q_hi": "एक विलयन कुचले हुए अंडे के छिलके के साथ अभिक्रिया करके एक गैस देता है जो चूने के पानी को दूधिया कर देती है। इस विलयन में है:",
        "opts": ["NaCl", "HCl", "LiCl", "KCl"],
        "opts_hi": ["NaCl", "HCl (Hydrochloric Acid)", "LiCl", "KCl"],
        "ans": 1,
        "sol": "Eggshells are made of Calcium Carbonate (CaCO₃). It reacts with acids like HCl to release Carbon dioxide (CO₂), which turns lime water milky.",
        "sol_hi": "अंडे के छिलके कैल्शियम कार्बोनेट (CaCO₃) के बने होते हैं। यह HCl जैसे अम्लों के साथ अभिक्रिया करके कार्बन डाइऑक्साइड (CO₂) मुक्त करता है, जो चूने के पानी को दूधिया कर देती है।"
    },
    {
        "q": "Plaster of Paris sets into a hard solid mass when mixed with water due to the formation of:",
        "q_hi": "जल मिलाने पर प्लास्टर ऑफ पेरिस किसके बनने के कारण एक कठोर ठोस द्रव्यमान में बदल जाता है?",
        "opts": ["Calcium Carbonate", "Gypsum", "Calcium Hydroxide", "Anhydrous Calcium Sulfate"],
        "opts_hi": ["कैल्शियम कार्बोनेट", "जिप्सम (Gypsum)", "कैल्शियम हाइड्रोक्साइड", "निर्जल कैल्शियम सल्फेट"],
        "ans": 1,
        "sol": "Plaster of Paris (CaSO₄&middot;0.5H₂O) reacts with water to form Gypsum (CaSO₄&middot;2H₂O), which sets into a hard crystalline solid.",
        "sol_hi": "प्लास्टर ऑफ पेरिस (CaSO₄&middot;0.5H₂O) पानी के साथ अभिक्रिया करके जिप्सम (CaSO₄&middot;2H₂O) बनाता है, जो एक कठोर क्रिस्टलीय ठोस में बदल जाता है।"
    },
    {
        "q": "What is the pH of an aqueous solution having a hydrogen ion concentration of 10⁻⁵ M?",
        "q_hi": "10⁻⁵ M हाइड्रोजन आयन सांद्रता वाले जलीय विलयन का पीएच क्या होगा?",
        "opts": ["5", "-5", "9", "7"],
        "opts_hi": ["5 (5)", "-5", "9", "7"],
        "ans": 0,
        "sol": "pH = -log[H⁺] = -log(10⁻⁵) = 5.",
        "sol_hi": "pH = -log[H⁺] = -log(10⁻⁵) = 5।"
    },
    {
        "q": "Which of the following salts does not contain water of crystallization?",
        "q_hi": "निम्नलिखित में से किस लवण में क्रिस्टलीकरण का जल नहीं होता है?",
        "opts": ["Blue Vitriol", "Baking Soda", "Washing Soda", "Gypsum"],
        "opts_hi": ["नीला थोथा", "बेकिंग सोडा (Baking Soda)", "धावन सोडा", "जिप्सम"],
        "ans": 1,
        "sol": "Baking soda (NaHCO₃) is an anhydrous powder. Blue vitriol (CuSO₄&middot;5H₂O), Washing soda (Na₂CO₃&middot;10H₂O), and Gypsum (CaSO₄&middot;2H₂O) contain water of crystallization.",
        "sol_hi": "बेकिंग सोडा (NaHCO₃) एक निर्जल पाउडर है। नीला थोथा (CuSO₄&middot;5H₂O), धावन सोडा (Na₂CO₃&middot;10H₂O), और जिप्सम (CaSO₄&middot;2H₂O) में क्रिस्टलीकरण का जल होता है।"
    },
    {
        "q": "Which acid is present in curd and sour milk?",
        "q_hi": "दही और खट्टे दूध में कौन सा अम्ल मौजूद होता है?",
        "opts": ["Citric acid", "Lactic acid", "Tartaric acid", "Oxalic acid"],
        "opts_hi": ["साइट्रिक अम्ल", "लैक्टिक अम्ल (Lactic acid)", "टार्टरिक अम्ल", "ऑक्सेलिक अम्ल"],
        "ans": 1,
        "sol": "Curd and sour milk contain Lactic acid produced by lactobacillus bacteria fermenting lactose sugar.",
        "sol_hi": "दही और खट्टे दूध में लैक्टिक अम्ल होता है जो लैक्टोबैसिलस बैक्टीरिया द्वारा लैक्टोज शर्करा के किण्वन से बनता है।"
    },
    {
        "q": "The reaction of slaked lime Ca(OH)₂ with Chlorine gas yields:",
        "q_hi": "बुझे हुए चूने Ca(OH)₂ की chlorine gas के साथ क्रिया से क्या प्राप्त होता है?",
        "opts": ["Caustic Soda", "Bleaching Powder", "Baking Soda", "Washing Soda"],
        "opts_hi": ["कास्टिक सोडा", "विरंजक चूर्ण (Bleaching Powder)", "बेकिंग सोडा", "धावन सोडा"],
        "ans": 1,
        "sol": "Calcium Hydroxide (slaked lime) reacts with chlorine gas to form Bleaching Powder (Calcium Oxychloride, CaOCl₂) and water.",
        "sol_hi": "कैल्शियम हाइड्रोक्साइड (बुझा हुआ चूना) chlorine gas के साथ अभिक्रिया करके विरंजक चूर्ण (कैल्शियम ऑक्सीक्लोराइड, CaOCl₂) और जल बनाता है।"
    },
    {
        "q": "What is the pH of a 0.01 M NaOH solution?",
        "q_hi": "0.01 M NaOH विलयन का पीएच क्या होगा?",
        "opts": ["2", "12", "7", "10"],
        "opts_hi": ["2", "12 (12)", "7", "10"],
        "ans": 1,
        "sol": "NaOH is a strong base: [OH⁻] = 10⁻² M. pOH = -log[OH⁻] = 2. Since pH + pOH = 14, pH = 14 - 2 = 12.",
        "sol_hi": "NaOH एक प्रबल क्षारक है: [OH⁻] = 10⁻² M। pOH = -log[OH⁻] = 2। चूंकि pH + pOH = 14, इसलिए pH = 14 - 2 = 12।"
    },
    {
        "q": "In the chlor-alkali process, hydrogen gas is collected at the:",
        "q_hi": "क्लोर-एल्कली प्रक्रिया में हाइड्रोजन गैस कहाँ एकत्रित होती है?",
        "opts": ["Anode", "Cathode", "Both electrodes", "Bottom of the cell"],
        "opts_hi": ["एनोड पर", "कैथोड पर (Cathode)", "दोनों इलेक्ट्रोड पर", "सेल के पेंदे में"],
        "ans": 1,
        "sol": "During electrolysis of brine, positive H⁺ ions migrate to the negative electrode, the Cathode, and receive electrons to form H₂ gas.",
        "sol_hi": "नमक के विद्युत अपघटन के दौरान, धनावेशित H⁺ आयन ऋणावेशित इलेक्ट्रोड, कैथोड की ओर गति करते हैं और इलेक्ट्रॉन ग्रहण कर H₂ गैस बनाते हैं।"
    },
    {
        "q": "Which indicator changes to reddish-brown in basic solutions?",
        "q_hi": "कौन सा सूचक क्षारीय विलयन में लाल-भूरा हो जाता है?",
        "opts": ["Litmus", "Turmeric", "Phenolphthalein", "Methyl orange"],
        "opts_hi": ["लिटमस", "हल्दी (Turmeric)", "फिनोलफ्थेलीन", "मिथाइल ऑरेंज"],
        "ans": 1,
        "sol": "Turmeric is a natural indicator that remains yellow in acidic solutions but turns reddish-brown in basic solutions (like soap water).",
        "sol_hi": "हल्दी एक प्राकृतिक सूचक है जो अम्लीय विलयन में पीली रहती है लेकिन क्षारीय विलयन (जैसे साबुन का पानी) में लाल-भूरे रंग की हो जाती है।"
    },
    {
        "q": "The acid produced in our stomach that helps in digestion is:",
        "q_hi": "हमारे पेट में उत्पन्न होने वाला अम्ल जो पाचन में सहायता करता है, वह है:",
        "opts": ["Sulfuric acid", "Hydrochloric acid", "Citric acid", "Phosphoric acid"],
        "opts_hi": ["सल्फ्यूरिक अम्ल", "हाइड्रोक्लोरिक अम्ल (Hydrochloric acid)", "साइट्रिक अम्ल", "फॉस्फोरिक अम्ल"],
        "ans": 1,
        "sol": "Our stomach produces Hydrochloric acid (HCl) to create an acidic medium required for the activation of pepsin enzyme to digest proteins.",
        "sol_hi": "हमारा पेट प्रोटीन के पाचन के लिए पेप्सिन एंजाइम को सक्रिय करने के लिए आवश्यक अम्लीय माध्यम बनाने हेतु हाइड्रोक्लोरिक अम्ल (HCl) का उत्पादन करता है।"
    },
    {
        "q": "Which of the following is a conjugate base of HSO₄⁻?",
        "q_hi": "निम्नलिखित में से कौन सा HSO₄⁻ का संयुग्मी क्षारक (conjugate base) है?",
        "opts": ["H₂SO₄", "SO₄²⁻", "SO₃²⁻", "H⁺"],
        "opts_hi": ["H₂SO₄", "SO₄²⁻ (SO₄²⁻)", "SO₃²⁻", "H⁺"],
        "ans": 1,
        "sol": "According to Brønsted-Lowry, a conjugate base is formed when an acid loses a proton. HSO₄⁻ - H⁺ &rarr; SO₄²⁻.",
        "sol_hi": "ब्रोंस्टेड-लोरी के अनुसार, जब कोई अम्ल एक प्रोटॉन खो देता है तो संयुग्मी क्षारक बनता है। HSO₄⁻ - H⁺ &rarr; SO₄²⁻।"
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
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Thoroughly review acid-base definitions, indicators, pH scale parameters, neutralization, and industrial salts.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Theories of Acids & Bases & Indicators",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which of the following is a Lewis base?", "opts": ["BF₃", "AlCl₃", "NH₃", "H⁺"], "ans": 2, "sol": "NH₃ (Ammonia) has a lone pair of electrons to donate, making it a Lewis base."},
                    {"type": "True/False", "q": "True or False: Turmeric turns pink in a basic solution.", "ans": False, "sol": "False. Turmeric turns reddish-brown in basic solutions."},
                    {"type": "Fill in the Blank", "q": "Phenolphthalein turns ________ in basic solutions.", "ans": "Pink", "sol": "Phenolphthalein is pink in basic solutions and colorless in acidic solutions."}
                ]
            },
            {
                "title": "2. pH Scale & Its Everyday Importance",
                "masteryZone": [
                    {"type": "MCQ", "q": "Tooth decay starts when mouth pH is:", "opts": ["Below 7", "Below 5.5", "Above 8.5", "Below 3.0"], "ans": 1, "sol": "Tooth decay begins below pH 5.5 as the enamel starts dissolving."},
                    {"type": "True/False", "q": "True or False: Acid rain has a pH value higher than 6.0.", "ans": False, "sol": "False. Acid rain is characterized by pH below 5.6."}
                ]
            },
            {
                "title": "3. Important Industrial Salts & Chemical Formulas",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is the chemical formula of bleaching powder?", "opts": ["NaHCO₃", "Na₂CO₃·10H₂O", "CaOCl₂", "CaSO₄·0.5H₂O"], "ans": 2, "sol": "Bleaching powder is Calcium Oxychloride (CaOCl₂)."},
                    {"type": "True/False", "q": "True or False: Washing soda contains 10 water molecules of crystallization.", "ans": True, "sol": "True. Washing soda formula is Na₂CO₃·10H₂O."}
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
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "अम्ल-क्षारक परिभाषाओं, सूचकों, पीएच स्केल, उदासीनीकरण और औद्योगिक लवणों की गहन समीक्षा करें।", "sections": deep_dive_hi}
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
                "title": "1. अम्ल एवं क्षारकों के सिद्धांत और सूचक",
                "masteryZone": [
                    {"type": "MCQ", "q": "निम्नलिखित में से कौन सा लुईस क्षारक है?", "opts": ["BF₃", "AlCl₃", "NH₃", "H⁺"], "ans": 2, "sol": "NH₃ (अमोनिया) में दान करने के लिए एक एकाकी इलेक्ट्रॉन युग्म होता है, जो इसे लुईस क्षारक बनाता है।"},
                    {"type": "True/False", "q": "सही या गलत: हल्दी क्षारीय विलयन में गुलाबी हो जाती है।", "ans": False, "sol": "गलत। हल्दी क्षारीय विलयन में लाल-भूरे रंग की हो जाती है।"},
                    {"type": "Fill in the Blank", "q": "फिनोलफ्थेलीन क्षारीय विलयन में __________ हो जाता है।", "ans": "गुलाबी", "sol": "फिनोलफ्थेलीन क्षारीय विलयन में गुलाबी और अम्लीय विलयन में रंगहीन होता है।"}
                ]
            },
            {
                "title": "2. पीएच स्केल और दैनिक जीवन में इसका महत्व",
                "masteryZone": [
                    {"type": "MCQ", "q": "दंत क्षय तब शुरू होता है जब मुंह का पीएच होता है:", "opts": ["7 से नीचे", "5.5 से नीचे", "8.5 से ऊपर", "3.0 से नीचे"], "ans": 1, "sol": "दंत क्षय तब शुरू होता है जब पीएच 5.5 से कम हो जाता है, जिससे इनेमल घुलने लगता है।"},
                    {"type": "True/False", "q": "सही या गलत: अम्ल वर्षा का पीएच मान 6.0 से अधिक होता है।", "ans": False, "sol": "गलत। अम्ल वर्षा का पीएच 5.6 से कम होता है।"}
                ]
            },
            {
                "title": "3. महत्वपूर्ण औद्योगिक लवण और उनके रासायनिक सूत्र",
                "masteryZone": [
                    {"type": "MCQ", "q": "विरंजक चूर्ण का रासायनिक सूत्र क्या है?", "opts": ["NaHCO₃", "Na₂CO₃·10H₂O", "CaOCl₂", "CaSO₄·0.5H₂O"], "ans": 2, "sol": "विरंजक चूर्ण कैल्शियम ऑक्सीक्लोराइड (CaOCl₂) है।"},
                    {"type": "True/False", "q": "सही या गलत: धावन सोडा में क्रिस्टलीकरण के 10 जल अणु होते हैं।", "ans": True, "sol": "सही। धावन सोडा का सूत्र Na₂CO₃·10H₂O है।"}
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
