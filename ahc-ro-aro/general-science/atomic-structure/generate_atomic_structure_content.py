# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "atomic-structure"
TOPIC_DISPLAY = "Atomic Structure"
TOPIC_DISPLAY_HI = "परमाणु संरचना"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\general-science\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "General Science",
    "parentUrl": "../",
    "current": "Atomic Structure"
}

hero_en = {
    "title": "Atomic Structure",
    "description": "Master subatomic particles (electrons, protons, neutrons), atomic models (Dalton, Thomson, Rutherford, Bohr, Quantum), atomic number, mass number, isotopes, isobars, isotones, electronic configuration rules (Bohr-Bury, Aufbau, Pauli, Hund), and quantum numbers."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Atomic Structure Mock Test",
        "description": "Assess your understanding of atomic models, electronic configurations, quantum numbers, isotopes, and subatomic particles. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Historical Evolution of Atomic Theory",
    "description": "Key discoveries and theories that shaped our modern understanding of the atom.",
    "cards": [
        {
            "period": "Dalton's Atomic Theory",
            "date": "1808",
            "details": "John Dalton proposes that matter consists of indivisible atoms, which can neither be created nor destroyed."
        },
        {
            "period": "Discovery of Electron (Cathode Rays)",
            "date": "1897",
            "details": "J.J. Thomson discovers the electron using cathode ray tube experiments, proving atoms are divisible."
        },
        {
            "period": "Goldstein & Canal Rays",
            "date": "1886 / 1900s",
            "details": "Eugen Goldstein observes positively charged canal rays, laying the foundation for Rutherford's proton discovery."
        },
        {
            "period": "Rutherford's Gold Foil Experiment",
            "date": "1911",
            "details": "Ernest Rutherford discovers the dense atomic nucleus, showing that most of an atom is empty space."
        },
        {
            "period": "Bohr's Atomic Model",
            "date": "1913",
            "details": "Niels Bohr introduces quantized orbits where electrons revolve without radiating energy."
        },
        {
            "period": "Discovery of Neutron",
            "date": "1932",
            "details": "James Chadwick discovers the neutral subatomic particle, the neutron, completing the nucleus model."
        }
    ]
}

mnemonics_en = {
    "title": "Atomic Structure Mnemonics",
    "description": "Quick memory aids for subatomic particle discoverers and orbital filling rules.",
    "items": [
        {
            "title": "Mnemonic 1: Discoverers of Subatomic Particles",
            "phrase": "\"PEN - GTC (Proton-Goldstein/Rutherford, Electron-Thomson, Neutron-Chadwick)\"",
            "decryption": "Match particles with their discoverers:<br>• <strong>P</strong>roton: <strong>G</strong>oldstein (first observed anode rays) / Rutherford (named and characterized proton)<br>• <strong>E</strong>lectron: <strong>T</strong>homson (J.J. Thomson)<br>• <strong>N</strong>eutron: <strong>C</strong>hadwick (James Chadwick)"
        },
        {
            "title": "Mnemonic 2: Orbital Energy Order",
            "phrase": "\"Aufbau Principle (n+l rule)\"",
            "decryption": "Always fill electrons in orbitals of <strong>lowest energy first</strong> (1s &lt; 2s &lt; 2p &lt; 3s &lt; 3p &lt; 4s &lt; 3d)."
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Click to flip and test your understanding of atomic structure concepts.",
    "items": [
        {
            "question": "Why is Rutherford's model called the Nuclear Model of the Atom?",
            "answer": "Because it established that the entire positive charge and almost all the mass of the atom are concentrated in a tiny, dense center called the <strong>nucleus</strong>.",
            "icon": "fa-circle-dot"
        },
        {
            "question": "What is the Bohr-Bury rule for the maximum number of electrons in a shell?",
            "answer": "The maximum capacity of a shell is given by <strong>2n²</strong>, where 'n' is the shell number. Furthermore, the outermost shell can hold a <strong>maximum of 8 electrons</strong>.",
            "icon": "fa-atom"
        },
        {
            "question": "What are Isotopes, Isobars, and Isotones?",
            "answer": "• <strong>Isotopes</strong>: Same Atomic Number (Z), different Mass Number (A).<br>• <strong>Isobars</strong>: Same Mass Number (A), different Atomic Number (Z).<br>• <strong>Isotones</strong>: Same number of Neutrons (A - Z).",
            "icon": "fa-scale-balanced"
        },
        {
            "question": "What do the four Quantum Numbers represent?",
            "answer": "1. <strong>Principal (n)</strong>: Orbit/Energy Level (size).<br>2. <strong>Azimuthal (l)</strong>: Orbital Shape (s, p, d, f).<br>3. <strong>Magnetic (m)</strong>: Orbital Orientation.<br>4. <strong>Spin (s)</strong>: Electron Rotation Direction (+1/2, -1/2).",
            "icon": "fa-circle-question"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing the mass number with the atomic mass. The <strong>Mass Number (A)</strong> is always an integer (Protons + Neutrons), while the <strong>Atomic Mass</strong> is a fractional average of naturally occurring isotopes (e.g., Chlorine mass is 35.5, but its mass numbers are 35 and 37).",
        "<strong>Trap 2:</strong> Assuming 3d fills before 4s. According to the <strong>(n+l) rule</strong>, the energy of 4s (4+0=4) is lower than 3d (3+2=5). Therefore, the <strong>4s orbital fills before the 3d orbital</strong>.",
        "<strong>Trap 3:</strong> Misunderstanding Valency vs Valence Electrons. <strong>Valence Electrons</strong> are the total electrons in the outermost shell, whereas <strong>Valency</strong> is the combining capacity (e.g., Oxygen has 6 valence electrons, but its valency is 8 - 6 = 2).",
        "<strong>Trap 4:</strong> Assuming neutrons are present in all atoms. <strong>Protium (¹H)</strong> is the only stable isotope in the universe that has <strong>no neutrons</strong> (1 proton, 0 neutrons)."
    ]
}

deep_dive_en = [
    {
        "title": "1. Subatomic Particles & Cathode/Anode Rays",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Electron (e⁻):</strong> Discovered by J.J. Thomson (1897) via Cathode Ray experiments. Mass is 9.1 &times; 10⁻³¹ kg (approx. 1/1837 of hydrogen atom mass). Charge is -1.6 &times; 10⁻¹⁹ Coulomb.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Proton (p⁺):</strong> Eugen Goldstein (1886) discovered anode rays (canal rays). Named and fully established by Ernest Rutherford (1919). Mass is 1.672 &times; 10⁻²⁷ kg. Charge is +1.6 &times; 10⁻¹⁹ Coulomb.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Neutron (n⁰):</strong> Discovered by James Chadwick (1932) by bombarding Beryllium with alpha particles. It is neutral (no charge) and has a mass of 1.675 &times; 10⁻²⁷ kg (slightly heavier than a proton).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Cathode Rays:</strong> Travel in straight lines, produce heating effect, consist of negatively charged particles, and are deflected by electrical and magnetic fields.</li>
        </ul>
        
        <!-- SVG Diagram 1: Rutherford Gold Foil Scattering -->
        <svg viewBox="0 0 800 260" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .atom-gold { fill: rgba(241, 196, 15, 0.15); stroke: #f1c40f; stroke-width: 1.5px; }
            .nucleus-gold { fill: #f39c12; stroke: #d35400; stroke-width: 1.5px; }
            .alpha-ray { stroke: #e74c3c; stroke-width: 2px; fill: none; }
            .arrow-head { fill: #e74c3c; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
          </style>
          <text x="20" y="30" class="svg-title">Rutherford's Alpha Particle Scattering Experiment</text>
          
          <!-- Gold Atoms Foil (Right Side) -->
          <circle cx="500" cy="80" r="45" class="atom-gold" />
          <circle cx="500" cy="80" r="6" class="nucleus-gold" />
          
          <circle cx="500" cy="170" r="45" class="atom-gold" />
          <circle cx="500" cy="170" r="6" class="nucleus-gold" />
          
          <!-- Alpha Rays entering from Left -->
          <!-- Ray 1: Passes straight through -->
          <path d="M 100 50 L 700 50" class="alpha-ray" />
          <polygon points="700,50 690,46 690,54" class="arrow-head" />
          <text x="710" y="53" class="annot-text">Undeflected Ray (Most space is empty)</text>
          
          <!-- Ray 2: Deflected near nucleus -->
          <path d="M 100 100 L 450 100 Q 480 100 550 140 L 680 210" class="alpha-ray" />
          <polygon points="680,210 670,204 676,213" class="arrow-head" />
          <text x="690" y="210" class="annot-text">Slightly Deflected Ray</text>
          
          <!-- Ray 3: Rebounds / Bounces back -->
          <path d="M 100 170 L 490 170" class="alpha-ray" />
          <path d="M 490 170 L 120 185" class="alpha-ray" />
          <polygon points="120,185 130,189 128,180" class="arrow-head" />
          <text x="100" y="210" class="annot-text" fill="#e74c3c">Rebounded Ray (1 in 12,000 hits dense Nucleus)</text>
          
          <!-- Labels -->
          <text x="500" y="235" class="annot-text" font-weight="bold" text-anchor="middle">Gold Nucleus (+ve)</text>
          <path d="M 500 220 L 500 185" stroke="var(--text-dark, #2c3e50)" stroke-width="1" fill="none" />
        </svg>"""
    },
    {
        "title": "2. Atomic Models: Thomson, Rutherford, Bohr",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Thomson's Model (Plum Pudding):</strong> Proposed that an atom consists of a positively charged sphere with electrons embedded in it like raisins in a pudding. Atom is electrically neutral overall.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Rutherford's Model:</strong> Most space inside atom is empty. Nucleus is positively charged, extremely small, and dense. Electrons revolve around the nucleus in circular paths. Drawback: Could not explain stability of atom (revolving charged particles must lose energy and collapse).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Bohr's Model:</strong> Electrons revolve only in certain non-radiating orbits called discrete orbits or energy shells (K, L, M, N...). Electrons gain or lose energy only when jumping between energy levels.</li>
        </ul>
        
        <!-- SVG Diagram 2: Bohr's Model of Atom -->
        <svg viewBox="0 0 800 260" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .nucleus-bohr { fill: #8e44ad; stroke: #2c3e50; stroke-width: 1.5px; }
            .nucleus-text { fill: #ffffff; font-family: 'Inter', sans-serif; font-size: 11px; font-weight: bold; }
            .orbit-line { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 1.2px; stroke-dasharray: 4 4; }
            .electron-dot { fill: #3498db; stroke: #2980b9; stroke-width: 1px; }
            .orbit-label { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">Bohr's Model of the Atom (Quantized Energy Levels)</text>
          
          <!-- Central Nucleus -->
          <circle cx="200" cy="130" r="30" class="nucleus-bohr" />
          <text x="200" y="133" class="nucleus-text" text-anchor="middle">Nucleus</text>
          <text x="200" y="145" class="nucleus-text" text-anchor="middle" font-size="9">(p⁺ + n⁰)</text>
          
          <!-- Orbits -->
          <!-- K shell (n=1) -->
          <circle cx="200" cy="130" r="55" class="orbit-line" />
          <circle cx="200" cy="75" r="5" class="electron-dot" />
          <circle cx="200" cy="185" r="5" class="electron-dot" />
          
          <!-- L shell (n=2) -->
          <circle cx="200" cy="130" r="85" class="orbit-line" />
          <circle cx="130" cy="85" r="5" class="electron-dot" />
          <circle cx="270" cy="175" r="5" class="electron-dot" />
          
          <!-- M shell (n=3) -->
          <circle cx="200" cy="130" r="115" class="orbit-line" />
          
          <!-- Legend and Rules on Right -->
          <g transform="translate(420, 50)">
            <rect x="0" y="0" width="340" height="170" fill="none" stroke="rgba(128,128,128,0.2)" rx="8" />
            <text x="20" y="25" class="orbit-label" font-weight="bold" fill="var(--primary, #8e44ad)" font-size="13">Bohr-Bury Orbit Filling Rules:</text>
            <text x="20" y="55" class="orbit-label">• Max capacity of Shell: <strong>2n²</strong></text>
            <text x="20" y="80" class="orbit-label">  - n=1 (K Shell): Max 2 e⁻</text>
            <text x="20" y="105" class="orbit-label">  - n=2 (L Shell): Max 8 e⁻</text>
            <text x="20" y="130" class="orbit-label">  - n=3 (M Shell): Max 18 e⁻</text>
            <text x="20" y="155" class="orbit-label">• Outer shell can have <strong>max 8 e⁻</strong> (octet rule).</text>
          </g>
        </svg>"""
    },
    {
        "title": "3. Isotopes, Isobars, Isotones & Valency",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Atomic Number (Z):</strong> The number of protons present in the nucleus of an atom. In neutral atoms, Protons = Electrons.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Mass Number (A):</strong> The sum of protons and neutrons in the nucleus (collectively called nucleons). Formula: A = Protons (Z) + Neutrons (N).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Isotopes:</strong> Atoms of the same element with the same atomic number but different mass numbers. Example: Protium (¹H), Deuterium (²H), Tritium (³H). Applications: Cobalt-60 (cancer treatment), Carbon-14 (carbon dating), Uranium-235 (nuclear fuel).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Isobars:</strong> Atoms of different elements with the same mass number but different atomic numbers. Example: Argon (⁴⁰Ar) and Calcium (⁴⁰Ca).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Isotones:</strong> Atoms of different elements containing the same number of neutrons. Example: Carbon-14 (¹⁴C, 8 neutrons) and Oxygen-16 (¹⁶O, 8 neutrons).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Valency:</strong> The combining capacity of an atom. Determined by the number of valence electrons. If valence electrons are &le; 4, Valency = Valence electrons. If valence electrons are &gt; 4, Valency = 8 - Valence electrons.</li>
        </ul>
        
        <!-- SVG Diagram 3: Isotopes of Hydrogen -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .proton-dot { fill: #e74c3c; stroke: #c0392b; stroke-width: 1px; }
            .neutron-dot { fill: #34495e; stroke: #2c3e50; stroke-width: 1px; }
            .electron-dot-h { fill: #3498db; }
            .iso-orbit { fill: none; stroke: rgba(128, 128, 128, 0.3); stroke-dasharray: 3 3; stroke-width: 1px; }
            .iso-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">Isotopes of Hydrogen (Comparative Nuclear Composition)</text>
          
          <!-- Protium (Left) -->
          <g transform="translate(80, 40)">
            <circle cx="100" cy="80" r="15" fill="rgba(128,128,128,0.1)" stroke="rgba(128,128,128,0.3)" />
            <!-- Nucleus (1 proton) -->
            <circle cx="100" cy="80" r="8" class="proton-dot" />
            <!-- Orbit -->
            <circle cx="100" cy="80" r="45" class="iso-orbit" />
            <circle cx="100" cy="35" r="4" class="electron-dot-h" />
            
            <text x="100" y="145" class="iso-title" text-anchor="middle">Protium (¹₁H)</text>
            <text x="100" y="165" class="annot-text" text-anchor="middle">Protons: 1 | Neutrons: 0</text>
            <text x="100" y="180" class="annot-text" text-anchor="middle">Most common isotope</text>
          </g>
          
          <!-- Deuterium (Center) -->
          <g transform="translate(300, 40)">
            <circle cx="100" cy="80" r="18" fill="rgba(128,128,128,0.1)" stroke="rgba(128,128,128,0.3)" />
            <!-- Nucleus (1 proton, 1 neutron) -->
            <circle cx="95" cy="80" r="7" class="proton-dot" />
            <circle cx="105" cy="80" r="7" class="neutron-dot" />
            <!-- Orbit -->
            <circle cx="100" cy="80" r="45" class="iso-orbit" />
            <circle cx="100" cy="35" r="4" class="electron-dot-h" />
            
            <text x="100" y="145" class="iso-title" text-anchor="middle">Deuterium (²₁H)</text>
            <text x="100" y="165" class="annot-text" text-anchor="middle">Protons: 1 | Neutrons: 1</text>
            <text x="100" y="180" class="annot-text" text-anchor="middle">Used in Heavy Water (D₂O)</text>
          </g>
          
          <!-- Tritium (Right) -->
          <g transform="translate(520, 40)">
            <circle cx="100" cy="80" r="20" fill="rgba(128,128,128,0.1)" stroke="rgba(128,128,128,0.3)" />
            <!-- Nucleus (1 proton, 2 neutrons) -->
            <circle cx="93" cy="83" r="6" class="proton-dot" />
            <circle cx="107" cy="83" r="6" class="neutron-dot" />
            <circle cx="100" cy="73" r="6" class="neutron-dot" />
            <!-- Orbit -->
            <circle cx="100" cy="80" r="45" class="iso-orbit" />
            <circle cx="100" cy="35" r="4" class="electron-dot-h" />
            
            <text x="100" y="145" class="iso-title" text-anchor="middle">Tritium (³₁H)</text>
            <text x="100" y="165" class="annot-text" text-anchor="middle">Protons: 1 | Neutrons: 2</text>
            <text x="100" y="180" class="annot-text" text-anchor="middle" fill="#e74c3c">Radioactive (beta emitter)</text>
          </g>
        </svg>"""
    },
    {
        "title": "4. Quantum Numbers & Electronic Configuration Rules",
        "content": """<p>In modern quantum atomic theory, four quantum numbers describe the address and energy state of an electron in an atom:</p>
        <ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Principal Quantum Number (n):</strong> Describes the shell (orbit) number, size, and energy of the shell. Values: n = 1, 2, 3... (K, L, M...).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Azimuthal/Subsidiary Quantum Number (l):</strong> Defines the shape of the orbital or subshell. Values: l = 0 to (n-1). Shapes: l=0 (s, spherical), l=1 (p, dumbbell), l=2 (d, double dumbbell), l=3 (f, complex).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Magnetic Quantum Number (m_l):</strong> Describes the orientation of orbitals in space. Values: -l to +l. Example: for p-orbital (l=1), m_l = -1, 0, +1 (three orientations: p_x, p_y, p_z).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Spin Quantum Number (m_s):</strong> Describes the spin direction of the electron. Values: +1/2 (clockwise) or -1/2 (counter-clockwise).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Aufbau Principle:</strong> Orbitals are filled in the order of increasing energy levels (determined by the n+l rule). Lower (n+l) value fills first.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Pauli Exclusion Principle:</strong> No two electrons in an atom can have the same set of all four quantum numbers. This means an orbital can hold a maximum of 2 electrons with opposite spins.</li>
          <li style="margin-bottom: 0.75rem;"><strong>Hund's Rule of Maximum Multiplicity:</strong> Pairing of electrons in degenerate orbitals (same subshell) does not occur until all orbitals are singly occupied.</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "सामान्य विज्ञान",
    "parentUrl": "../",
    "current": "परमाणु संरचना"
}

hero_hi = {
    "title": "परमाणु संरचना",
    "description": "अपरमाणुक कणों (इलेक्ट्रॉन, प्रोटॉन, न्यूट्रॉन), प्रमुख परमाणु मॉडलों (डालटन, थॉमसन, रदरफोर्ड, बोहर, क्वांटम), परमाणु संख्या, द्रव्यमान संख्या, समस्थानिकों, समभारिकों, समन्यूट्रॉनिकों, संयोजकता, इलेक्ट्रॉनिक विन्यास नियमों (बोहर-बरी, Aufbau, पाउली, हुंड) और क्वांटम संख्याओं पर मजबूत पकड़ बनाएं।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव परमाणु संरचना मॉक टेस्ट",
        "description": "परमाणु मॉडल, इलेक्ट्रॉनिक विन्यास, क्वांटम संख्या, समस्थानिकों और अपरमाणुक कणों की अपनी समझ का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "परमाणु सिद्धांत का ऐतिहासिक विकास",
    "description": "परमाणु की आधुनिक समझ को आकार देने वाली प्रमुख खोजें और सिद्धांत।",
    "cards": [
        {
            "period": "डालटन का परमाणु सिद्धांत",
            "date": "1808",
            "details": "जॉन डालटन ने प्रस्ताव दिया कि पदार्थ अविभाज्य परमाणुओं से बना है, जिन्हें न तो बनाया जा सकता है और न ही नष्ट किया जा सकता है।"
        },
        {
            "period": "इलेक्ट्रॉन की खोज (कैथोड किरणें)",
            "date": "1897",
            "details": "जे.जे. थॉमसन ने कैथोड किरण ट्यूब प्रयोगों का उपयोग करके इलेक्ट्रॉन की खोज की, जिससे साबित हुआ कि परमाणु विभाज्य है।"
        },
        {
            "period": "गोल्डस्टीन और कैनाल किरणें",
            "date": "1886 / 1900s",
            "details": "यूजीन गोल्डस्टीन ने धनावेशित कैनाल किरणों (canal rays) का प्रेक्षण किया, जिसने रदरफोर्ड द्वारा प्रोटॉन की खोज की आधारशिला रखी।"
        },
        {
            "period": "रदरफोर्ड का स्वर्ण पत्र प्रयोग",
            "date": "1911",
            "details": "अर्नेस्ट रदरफोर्ड ने सघन परमाणु नाभिक की खोज की, जिससे स्पष्ट हुआ कि परमाणु का अधिकांश भाग खाली स्थान है।"
        },
        {
            "period": "बोहर का परमाणु मॉडल",
            "date": "1913",
            "details": "नील्स बोहर ने क्वांटम कक्षाओं की शुरुआत की जहाँ इलेक्ट्रॉन बिना ऊर्जा उत्सर्जित किए घूमते हैं।"
        },
        {
            "period": "न्यूट्रॉन की खोज",
            "date": "1932",
            "details": "जेम्स चैडविक ने उदासीन अपरमाणुक कण, न्यूट्रॉन की खोज की, जिससे नाभिकीय मॉडल पूर्ण हुआ।"
        }
    ]
}

mnemonics_hi = {
    "title": "परमाणु संरचना के स्मृति सूत्र",
    "description": "अपरमाणुक कणों के खोजकर्ताओं और उपकोशों में इलेक्ट्रॉन भरने के नियमों के त्वरित सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: अपरमाणुक कणों के खोजकर्ता",
            "phrase": "\"ईंट पर नाच (इलेक्ट्रॉन-थॉमसन, प्रोटॉन-रदरफोर्ड, न्यूट्रॉन-चैडविक)\"",
            "decryption": "कणों को उनके खोजकर्ताओं से मिलाएँ:<br>• <strong>ईं</strong>ट: <strong>इ</strong>लेक्ट्रॉन - जे. जे. <strong>थ</strong>ॉमसन (Thomson)<br>• <strong>प</strong>र: <strong>प्र</strong>ोटॉन - <strong>र</strong>दरफोर्ड (Rutherford) [नोट: खोज का श्रेय Goldstein को भी जाता है जिन्होंने कैनाल किरणों का पता लगाया था]<br>• <strong>ना</strong>च: <strong>न्यू</strong>ट्रॉन - जेम्स <strong>चै</strong>डविक (Chadwick)"
        },
        {
            "title": "स्मृति सूत्र 2: कक्षक ऊर्जा नियम",
            "phrase": "\"Aufbau सिद्धांत (n+l नियम)\"",
            "decryption": "इलेक्ट्रॉन हमेशा सबसे <strong>कम ऊर्जा वाले कक्षकों</strong> में पहले भरे जाते हैं (1s &lt; 2s &lt; 2p &lt; 3s &lt; 3p &lt; 4s &lt; 3d)।"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए क्लिक करें और अपनी समझ की जांच करें।",
    "items": [
        {
            "question": "रदरफोर्ड के मॉडल को परमाणु का नाभिकीय मॉडल क्यों कहा जाता है?",
            "answer": "क्योंकि इसने यह स्थापित किया कि परमाणु का पूरा धनावेश और उसका लगभग सारा द्रव्यमान एक बहुत छोटे और सघन केंद्र में केंद्रित होता है जिसे <strong>नाभिक (Nucleus)</strong> कहते हैं।",
            "icon": "fa-circle-dot"
        },
        {
            "question": "कोशों में इलेक्ट्रॉनों की अधिकतम संख्या के लिए बोहर-बरी का नियम क्या है?",
            "answer": "किसी कोश की अधिकतम क्षमता <strong>2n²</strong> द्वारा दी जाती है, जहाँ 'n' कोश की संख्या है। इसके अतिरिक्त, सबसे बाहरी कोश में <strong>अधिकतम 8 इलेक्ट्रॉन</strong> ही हो सकते हैं।",
            "icon": "fa-atom"
        },
        {
            "question": "समस्थानिक, समभारिक और समन्यूट्रॉनिक क्या हैं?",
            "answer": "• <strong>समस्थानिक (Isotopes)</strong>: समान परमाणु क्रमांक (Z), भिन्न द्रव्यमान संख्या (A)।<br>• <strong>समभारिक (Isobars)</strong>: समान द्रव्यमान संख्या (A), भिन्न परमाणु क्रमांक (Z)।<br>• <strong>समन्यूट्रॉनिक (Isotones)</strong>: न्यूट्रॉनों की संख्या समान (A - Z)।",
            "icon": "fa-scale-balanced"
        },
        {
            "question": "चारों क्वांटम संख्याएं (Quantum Numbers) क्या दर्शाती हैं?",
            "answer": "1. <strong>मुख्य (n)</strong>: कोश / ऊर्जा स्तर (आकार)।<br>2. <strong>द्विगंशी / एजिमुथल (l)</strong>: कक्षक का आकार (s, p, d, f)।<br>3. <strong>चुंबकीय (m)</strong>: कक्षक का त्रिविम विन्यास।<br>4. <strong>चक्रण (s)</strong>: इलेक्ट्रॉन के घूमने की दिशा (+1/2, -1/2)।",
            "icon": "fa-circle-question"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> द्रव्यमान संख्या (Mass Number) को परमाणु भार (Atomic Mass) के साथ भ्रमित करना। <strong>द्रव्यमान संख्या (A)</strong> हमेशा एक पूर्णांक होती है (प्रोटॉन + न्यूट्रॉन), जबकि <strong>परमाणु भार</strong> प्राकृतिक रूप से पाए जाने वाले समस्थानिकों का औसत भार होता है (जैसे क्लोरीन का द्रव्यमान 35.5 है, लेकिन इसकी द्रव्यमान संख्या 35 और 37 होती है)।",
        "<strong>भ्रम 2:</strong> यह मानना कि 3d कक्षक 4s से पहले भरता है। <strong>(n+l) नियम</strong> के अनुसार, 4s (4+0=4) की ऊर्जा 3d (3+2=5) से कम होती है। इसलिए, <strong>4s कक्षक 3d कक्षक से पहले भरता है</strong>।",
        "<strong>भ्रम 3:</strong> संयोजकता (Valency) और संयोजी इलेक्ट्रॉन (Valence Electrons) में अंतर न समझ पाना। <strong>संयोजी इलेक्ट्रॉन</strong> सबसे बाहरी कोश में मौजूद कुल इलेक्ट्रॉनों की संख्या है, जबकि <strong>संयोजकता</strong> तत्वों के जुड़ने की क्षमता होती है (जैसे ऑक्सीजन में 6 संयोजी इलेक्ट्रॉन होते हैं, लेकिन उसकी संयोजकता 8 - 6 = 2 होती है)।",
        "<strong>भ्रम 4:</strong> यह मान लेना कि सभी परमाणुओं में न्यूट्रॉन मौजूद होते हैं। हाइड्रोजन का समस्थानिक <strong>प्रोटियम (¹H)</strong> ब्रह्मांड में एकमात्र ऐसा स्थिर परमाणु है जिसमें <strong>कोई न्यूट्रॉन नहीं</strong> होता (1 प्रोटॉन, 0 न्यूट्रॉन)।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. अपरमाणुक कण एवं कैथोड/एनोड किरणें",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>इलेक्ट्रॉन (e⁻):</strong> जे.जे. थॉमसन (1897) द्वारा कैथोड किरण प्रयोगों के माध्यम से खोजा गया। इसका द्रव्यमान 9.1 &times; 10⁻³¹ kg (हाइड्रोजन परमाणु के द्रव्यमान का लगभग 1/1837वां भाग) होता है। इसका आवेश -1.6 &times; 10⁻¹⁹ कूलाम होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>प्रोटॉन (p⁺):</strong> यूजीन गोल्डस्टीन (1886) ने एनोड किरणों (कैनाल किरणों) की खोज की। अर्नेस्ट रदरफोर्ड (1919) द्वारा प्रोटॉन नाम दिया गया और इसे पूरी तरह स्थापित किया गया। इसका द्रव्यमान 1.672 &times; 10⁻²७ kg होता है। इसका आवेश +1.6 &times; 10⁻¹⁹ कूलाम होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>न्यूट्रॉन (n⁰):</strong> जेम्स चैडविक (1932) द्वारा बेरिलियम पर अल्फा कणों की बमबारी करके खोजा गया। यह उदासीन (कोई आवेश नहीं) होता है और इसका द्रव्यमान 1.675 &times; 10⁻²७ kg (प्रोटॉन से थोड़ा भारी) होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>कैथोड किरणें:</strong> सीधी रेखाओं में चलती हैं, तापीय प्रभाव पैदा करती हैं, ऋणावेशित कणों से बनी होती हैं, और विद्युत तथा चुंबकीय क्षेत्रों द्वारा विक्षेपित होती हैं।</li>
        </ul>
        
        <!-- SVG Diagram 1: Rutherford Gold Foil Scattering -->
        <svg viewBox="0 0 800 260" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .atom-gold { fill: rgba(241, 196, 15, 0.15); stroke: #f1c40f; stroke-width: 1.5px; }
            .nucleus-gold { fill: #f39c12; stroke: #d35400; stroke-width: 1.5px; }
            .alpha-ray { stroke: #e74c3c; stroke-width: 2px; fill: none; }
            .arrow-head { fill: #e74c3c; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
          </style>
          <text x="20" y="30" class="svg-title">रदरफोर्ड का अल्फा कण प्रकीर्णन प्रयोग (स्वर्ण पत्र प्रयोग)</text>
          
          <!-- Gold Atoms Foil (Right Side) -->
          <circle cx="500" cy="80" r="45" class="atom-gold" />
          <circle cx="500" cy="80" r="6" class="nucleus-gold" />
          
          <circle cx="500" cy="170" r="45" class="atom-gold" />
          <circle cx="500" cy="170" r="6" class="nucleus-gold" />
          
          <!-- Alpha Rays entering from Left -->
          <!-- Ray 1: Passes straight through -->
          <path d="M 100 50 L 700 50" class="alpha-ray" />
          <polygon points="700,50 690,46 690,54" class="arrow-head" />
          <text x="710" y="53" class="annot-text">बिना विक्षेपित किरण (परमाणु का अधिकांश भाग खाली है)</text>
          
          <!-- Ray 2: Deflected near nucleus -->
          <path d="M 100 100 L 450 100 Q 480 100 550 140 L 680 210" class="alpha-ray" />
          <polygon points="680,210 670,204 676,213" class="arrow-head" />
          <text x="690" y="210" class="annot-text">थोड़ी विक्षेपित किरण</text>
          
          <!-- Ray 3: Rebounds / Bounces back -->
          <path d="M 100 170 L 490 170" class="alpha-ray" />
          <path d="M 490 170 L 120 185" class="alpha-ray" />
          <polygon points="120,185 130,189 128,180" class="arrow-head" />
          <text x="100" y="210" class="annot-text" fill="#e74c3c">वापस लौटने वाली किरण (12,000 में से 1 सघन नाभिक से टकराती है)</text>
          
          <!-- Labels -->
          <text x="500" y="235" class="annot-text" font-weight="bold" text-anchor="middle">स्वर्ण नाभिक (धनावेशित)</text>
          <path d="M 500 220 L 500 185" stroke="var(--text-dark, #2c3e50)" stroke-width="1" fill="none" />
        </svg>"""
    },
    {
        "title": "2. परमाणु मॉडल: थॉमसन, रदरफोर्ड, बोहर",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>थॉमसन का मॉडल (तरबूज मॉडल / प्लम पुडिंग):</strong> इसके अनुसार परमाणु एक धनावेशित गोला है जिसमें इलेक्ट्रॉन उसी तरह धंसे होते हैं जैसे तरबूज में बीज। परमाणु समग्र रूप से उदासीन होता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>रदरफोर्ड का मॉडल:</strong> परमाणु के अंदर का अधिकांश भाग खाली है। नाभिक धनावेशित, बहुत छोटा और सघन होता है। इलेक्ट्रॉन नाभिक के चारों ओर वर्तुलाकार (circular) मार्ग में घूमते हैं। दोष: यह परमाणु के स्थायित्व की व्याख्या नहीं कर सका (चक्रण करते आवेशित कणों को ऊर्जा खोकर नाभिक में गिर जाना चाहिए था)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>बोहर का मॉडल:</strong> इलेक्ट्रॉन केवल कुछ निश्चित गैर-विकिरण कक्षाओं में ही घूमते हैं जिन्हें विविक्त कक्षाएँ (discrete orbits) या ऊर्जा कोश (K, L, M, N...) कहा जाता है। ऊर्जा का आदान-प्रदान केवल एक कोश से दूसरे में कूदने पर होता है।</li>
        </ul>
        
        <!-- SVG Diagram 2: Bohr's Model of Atom -->
        <svg viewBox="0 0 800 260" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .nucleus-bohr { fill: #8e44ad; stroke: #2c3e50; stroke-width: 1.5px; }
            .nucleus-text { fill: #ffffff; font-family: 'Inter', sans-serif; font-size: 11px; font-weight: bold; }
            .orbit-line { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 1.2px; stroke-dasharray: 4 4; }
            .electron-dot { fill: #3498db; stroke: #2980b9; stroke-width: 1px; }
            .orbit-label { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">बोहर का परमाणु मॉडल (ऊर्जा स्तर और कोश)</text>
          
          <!-- Central Nucleus -->
          <circle cx="200" cy="130" r="30" class="nucleus-bohr" />
          <text x="200" y="133" class="nucleus-text" text-anchor="middle">नाभिक</text>
          <text x="200" y="145" class="nucleus-text" text-anchor="middle" font-size="9">(p⁺ + n⁰)</text>
          
          <!-- Orbits -->
          <!-- K shell (n=1) -->
          <circle cx="200" cy="130" r="55" class="orbit-line" />
          <circle cx="200" cy="75" r="5" class="electron-dot" />
          <circle cx="200" cy="185" r="5" class="electron-dot" />
          
          <!-- L shell (n=2) -->
          <circle cx="200" cy="130" r="85" class="orbit-line" />
          <circle cx="130" cy="85" r="5" class="electron-dot" />
          <circle cx="270" cy="175" r="5" class="electron-dot" />
          
          <!-- M shell (n=3) -->
          <circle cx="200" cy="130" r="115" class="orbit-line" />
          
          <!-- Legend and Rules on Right -->
          <g transform="translate(420, 50)">
            <rect x="0" y="0" width="340" height="170" fill="none" stroke="rgba(128,128,128,0.2)" rx="8" />
            <text x="20" y="25" class="orbit-label" font-weight="bold" fill="var(--primary, #8e44ad)" font-size="13">बोहर-बरी इलेक्ट्रॉन वितरण नियम:</text>
            <text x="20" y="55" class="orbit-label">• कोश की अधिकतम क्षमता: <strong>2n²</strong></text>
            <text x="20" y="80" class="orbit-label">  - n=1 (K कोश): अधिकतम 2 इलेक्ट्रॉन</text>
            <text x="20" y="105" class="orbit-label">  - n=2 (L कोश): अधिकतम 8 इलेक्ट्रॉन</text>
            <text x="20" y="130" class="orbit-label">  - n=3 (M कोश): अधिकतम 18 इलेक्ट्रॉन</text>
            <text x="20" y="155" class="orbit-label">• सबसे बाहरी कोश में <strong>अधिकतम 8 e⁻</strong> हो सकते हैं।</text>
          </g>
        </svg>"""
    },
    {
        "title": "3. समस्थानिक, समभारिक, समन्यूट्रॉनिक एवं संयोजकता",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>परमाणु संख्या (Z):</strong> किसी परमाणु के नाभिक में मौजूद प्रोटॉनों की संख्या। उदासीन परमाणु में: प्रोटॉन = इलेक्ट्रॉन।</li>
          <li style="margin-bottom: 0.75rem;"><strong>द्रव्यमान संख्या (A):</strong> नाभिक में मौजूद प्रोटॉनों और न्यूट्रॉनों की कुल संख्या का योग (इन्हें सामूहिक रूप से न्यूक्लिऑन कहा जाता है)। सूत्र: A = Z (प्रोटॉन) + N (न्यूट्रॉन)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>समस्थानिक (Isotopes):</strong> एक ही तत्व के वे परमाणु जिनका परमाणु क्रमांक समान लेकिन द्रव्यमान संख्या भिन्न होती है। उदाहरण: प्रोटियम (¹H), ड्यूटेरियम (²H), ट्राइटियम (³H)। अनुप्रयोग: कोबाल्ट-60 (कैंसर का उपचार), कार्बन-14 (आयु निर्धारण), यूरेनियम-235 (परमाणु ईंधन)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>समभारिक (Isobars):</strong> विभिन्न तत्वों के वे परमाणु जिनकी द्रव्यमान संख्या समान लेकिन परमाणु क्रमांक भिन्न होता है। उदाहरण: आर्गन (⁴⁰Ar) और कैल्शियम (⁴⁰Ca)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>समन्यूट्रॉनिक (Isotones):</strong> विभिन्न तत्वों के वे परमाणु जिनमें न्यूट्रॉनों की संख्या समान होती है। उदाहरण: कार्बन-14 (¹⁴C, 8 न्यूट्रॉन) और ऑक्सीजन-16 (¹⁶O, 8 न्यूट्रॉन)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>संयोजकता (Valency):</strong> किसी परमाणु के संयोजन करने की क्षमता। यदि बाहरी कोश के इलेक्ट्रॉन &le; 4 हैं, तो संयोजकता = संयोजी इलेक्ट्रॉन। यदि बाहरी इलेक्ट्रॉन &gt; 4 हैं, तो संयोजकता = 8 - संयोजी इलेक्ट्रॉन।</li>
        </ul>
        
        <!-- SVG Diagram 3: Isotopes of Hydrogen -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .proton-dot { fill: #e74c3c; stroke: #c0392b; stroke-width: 1px; }
            .neutron-dot { fill: #34495e; stroke: #2c3e50; stroke-width: 1px; }
            .electron-dot-h { fill: #3498db; }
            .iso-orbit { fill: none; stroke: rgba(128, 128, 128, 0.3); stroke-dasharray: 3 3; stroke-width: 1px; }
            .iso-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 13px; }
            
            
            
          </style>
          <text x="20" y="30" class="svg-title">हाइड्रोजन के समस्थानिक (नाभिकीय संरचना की तुलना)</text>
          
          <!-- Protium (Left) -->
          <g transform="translate(80, 40)">
            <circle cx="100" cy="80" r="15" fill="rgba(128,128,128,0.1)" stroke="rgba(128,128,128,0.3)" />
            <!-- Nucleus (1 proton) -->
            <circle cx="100" cy="80" r="8" class="proton-dot" />
            <!-- Orbit -->
            <circle cx="100" cy="80" r="45" class="iso-orbit" />
            <circle cx="100" cy="35" r="4" class="electron-dot-h" />
            
            <text x="100" y="145" class="iso-title" text-anchor="middle">प्रोटियम (¹₁H)</text>
            <text x="100" y="165" class="annot-text" text-anchor="middle">प्रोटॉन: 1 | न्यूट्रॉन: 0</text>
            <text x="100" y="180" class="annot-text" text-anchor="middle">सबसे आम समस्थानिक</text>
          </g>
          
          <!-- Deuterium (Center) -->
          <g transform="translate(300, 40)">
            <circle cx="100" cy="80" r="18" fill="rgba(128,128,128,0.1)" stroke="rgba(128,128,128,0.3)" />
            <!-- Nucleus (1 proton, 1 neutron) -->
            <circle cx="95" cy="80" r="7" class="proton-dot" />
            <circle cx="105" cy="80" r="7" class="neutron-dot" />
            <!-- Orbit -->
            <circle cx="100" cy="80" r="45" class="iso-orbit" />
            <circle cx="100" cy="35" r="4" class="electron-dot-h" />
            
            <text x="100" y="145" class="iso-title" text-anchor="middle">ड्यूटेरियम (²₁H)</text>
            <text x="100" y="165" class="annot-text" text-anchor="middle">प्रोटॉन: 1 | न्यूट्रॉन: 1</text>
            <text x="100" y="180" class="annot-text" text-anchor="middle">भारी जल (D₂O) में प्रयुक्त</text>
          </g>
          
          <!-- Tritium (Right) -->
          <g transform="translate(520, 40)">
            <circle cx="100" cy="80" r="20" fill="rgba(128,128,128,0.1)" stroke="rgba(128,128,128,0.3)" />
            <!-- Nucleus (1 proton, 2 neutrons) -->
            <circle cx="93" cy="83" r="6" class="proton-dot" />
            <circle cx="107" cy="83" r="6" class="neutron-dot" />
            <circle cx="100" cy="73" r="6" class="neutron-dot" />
            <!-- Orbit -->
            <circle cx="100" cy="80" r="45" class="iso-orbit" />
            <circle cx="100" cy="35" r="4" class="electron-dot-h" />
            
            <text x="100" y="145" class="iso-title" text-anchor="middle">ट्राइटियम (³₁H)</text>
            <text x="100" y="165" class="annot-text" text-anchor="middle">प्रोटॉन: 1 | न्यूट्रॉन: 2</text>
            <text x="100" y="180" class="annot-text" text-anchor="middle" fill="#e74c3c">रेडियोधर्मी (बिटा उत्सर्जक)</text>
          </g>
        </svg>"""
    },
    {
        "title": "4. क्वांटम संख्याएं एवं इलेक्ट्रॉनिक विन्यास के नियम",
        "content": """<p>आधुनिक क्वांटम परमाणु सिद्धांत में, चार क्वांटम संख्याएं किसी परमाणु में इलेक्ट्रॉन के पते और ऊर्जा की स्थिति का वर्णन करती हैं:</p>
        <ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>मुख्य क्वांटम संख्या (n):</strong> यह मुख्य कोश (ऑर्बिट) संख्या, उसके आकार और ऊर्जा को दर्शाती है। मान: n = 1, 2, 3... (K, L, M...)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>द्विगंशी क्वांटम संख्या (l):</strong> यह उपकोश या कक्षक के आकार को परिभाषित करती है। मान: l = 0 से (n-1)। उपकोश आकार: l=0 (s कक्षक, गोलाकार), l=1 (p कक्षक, डम्बल), l=2 (d कक्षक, द्विडम्बल), l=3 (f कक्षक, जटिल)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>चुंबकीय क्वांटम संख्या (m_l):</strong> यह त्रिविम में कक्षक के विन्यास (orientation) को दर्शाती है। मान: -l से +l। उदाहरण: p कक्षक (l=1) के लिए, m_l = -1, 0, +1 (तीन विन्यास: p_x, p_y, p_z)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>चक्रण क्वांटम संख्या (m_s):</strong> यह इलेक्ट्रॉन के स्वयं की धुरी पर घूमने की दिशा दर्शाती है। मान: +1/2 (दक्षिणावर्त) या -1/2 (वामावर्त)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>Aufbau सिद्धांत:</strong> कक्षकों को उनकी बढ़ती ऊर्जा के क्रम में भरा जाता है (n+l नियम)। जिस कक्षक का n+l मान कम होता है, वह पहले भरता है।</li>
          <li style="margin-bottom: 0.75rem;"><strong>पाउली का अपवर्जन सिद्धांत:</strong> किसी भी परमाणु में किन्हीं दो इलेक्ट्रॉनों के लिए चारों क्वांटम संख्याओं का मान एक समान नहीं हो सकता। इसका अर्थ है कि एक कक्षक में विपरीत चक्रण वाले अधिकतम 2 इलेक्ट्रॉन ही रह सकते हैं।</li>
          <li style="margin-bottom: 0.75rem;"><strong>हुंड का नियम (अधिकतम बहुलता का नियम):</strong> किसी उपकोश (जैसे p, d, f) के कक्षकों में इलेक्ट्रॉनों का युग्मन (pairing) तब तक नहीं होता जब तक कि सभी कक्षकों में एक-एक इलेक्ट्रॉन न भर जाए।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Who discovered the electron?",
        "q_hi": "इलेक्ट्रॉन की खोज किसने की थी?",
        "opts": ["J.J. Thomson", "Ernest Rutherford", "John Dalton", "James Chadwick"],
        "opts_hi": ["जे.जे. थॉमसन (J.J. Thomson)", "अर्नेस्ट रदरफोर्ड", "जॉन डालटन", "जेम्स चैडविक"],
        "ans": 0,
        "sol": "J.J. Thomson discovered the electron in 1897 through his cathode ray tube experiments.",
        "sol_hi": "जे.जे. थॉमसन ने 1897 में कैथोड किरण ट्यूब प्रयोगों के माध्यम से इलेक्ट्रॉन की खोज की थी।"
    },
    {
        "q": "Which subatomic particle is absent in a normal Hydrogen (Protium) atom?",
        "q_hi": "एक सामान्य हाइड्रोजन (प्रोटियम) परमाणु में कौन सा अपरमाणुक कण अनुपस्थित होता है?",
        "opts": ["Proton", "Electron", "Neutron", "Positron"],
        "opts_hi": ["प्रोटॉन", "इलेक्ट्रॉन", "न्यूट्रॉन (Neutron)", "पॉज़िट्रॉन"],
        "ans": 2,
        "sol": "Protium (¹H) has 1 proton and 1 electron, but 0 neutrons. It is the only stable atom without neutrons.",
        "sol_hi": "प्रोटियम (¹H) में 1 प्रोटॉन और 1 इलेक्ट्रॉन होता है, लेकिन 0 न्यूट्रॉन होते हैं। यह बिना न्यूट्रॉन वाला एकमात्र स्थिर परमाणु है।"
    },
    {
        "q": "Goldstein's experiments with canal rays led to the discovery of:",
        "q_hi": "कैनाल किरणों के साथ गोल्डस्टीन के प्रयोगों से किसकी खोज हुई?",
        "opts": ["Electrons", "Protons", "Neutrons", "Mesons"],
        "opts_hi": ["इलेक्ट्रॉन", "प्रोटॉन (Protons)", "न्यूट्रॉन", "मेसॉन"],
        "ans": 1,
        "sol": "Eugen Goldstein discovered canal rays in 1886, which were positively charged particles, later identified as protons.",
        "sol_hi": "यूजीन गोल्डस्टीन ने 1886 में कैनाल किरणों की खोज की, जो धनावेशित कण थे, जिन्हें बाद में प्रोटॉन के रूप में पहचाना गया।"
    },
    {
        "q": "Rutherford's alpha-scattering experiment used which metal foil?",
        "q_hi": "रदरफोर्ड के अल्फा-प्रकीर्णन प्रयोग में किस धातु की पन्नी का उपयोग किया गया था?",
        "opts": ["Silver", "Platinum", "Gold", "Aluminum"],
        "opts_hi": ["चांदी", "प्लेटिनम", "सोना (Gold)", "एल्युमिनियम"],
        "ans": 2,
        "sol": "Rutherford used gold foil because gold is highly malleable and could be made into an extremely thin sheet (about 1000 atoms thick).",
        "sol_hi": "रदरफोर्ड ने सोने की पन्नी का उपयोग किया क्योंकि सोना अत्यधिक आघातवर्धनीय (malleable) होता है और इसकी बहुत पतली शीट (लगभग 1000 परमाणु मोटी) बनाई जा सकती थी।"
    },
    {
        "q": "The atomic number of an element is equal to the number of:",
        "q_hi": "किसी तत्व का परमाणु क्रमांक किसके बराबर होता है?",
        "opts": ["Neutrons", "Protons", "Electrons + Neutrons", "Protons + Neutrons"],
        "opts_hi": ["न्यूट्रॉन", "प्रोटॉन (Protons)", "इलेक्ट्रॉन + न्यूट्रॉन", "प्रोटॉन + न्यूट्रॉन"],
        "ans": 1,
        "sol": "The atomic number (Z) of an element is defined as the number of protons in the nucleus of its atom.",
        "sol_hi": "किसी तत्व का परमाणु क्रमांक (Z) उसके परमाणु के नाभिक में मौजूद प्रोटॉनों की संख्या के रूप में परिभाषित किया जाता है।"
    },
    {
        "q": "What is the maximum number of electrons that can be accommodated in the M shell?",
        "q_hi": "M कोश (M shell) में अधिकतम कितने इलेक्ट्रॉन आ सकते हैं?",
        "opts": ["2", "8", "18", "32"],
        "opts_hi": ["2", "8", "18 (18)", "32"],
        "ans": 2,
        "sol": "According to the 2n² rule, for the M shell n=3. Max electrons = 2 &times; (3)² = 2 &times; 9 = 18.",
        "sol_hi": "2n² नियम के अनुसार, M कोश के लिए n=3। अधिकतम इलेक्ट्रॉन = 2 &times; (3)² = 2 &times; 9 = 18।"
    },
    {
        "q": "Which isotope is used in the treatment of cancer?",
        "q_hi": "कैंसर के उपचार में किस समस्थानिक (Isotope) का उपयोग किया जाता है?",
        "opts": ["Uranium-235", "Cobalt-60", "Iodine-131", "Carbon-14"],
        "opts_hi": ["यूरेनियम-235", "कोबाल्ट-60 (Cobalt-60)", "आयोडीन-131", "कार्बन-14"],
        "ans": 1,
        "sol": "Cobalt-60 is a radioactive isotope of cobalt that emits gamma rays, which are used to destroy cancer cells.",
        "sol_hi": "कोबाल्ट-60 कोबाल्ट का एक रेडियोधर्मी समस्थानिक है जो गामा किरणें उत्सर्जित करता है, जिनका उपयोग कैंसर कोशिकाओं को नष्ट करने के लिए किया जाता है।"
    },
    {
        "q": "Atoms with the same mass number but different atomic numbers are called:",
        "q_hi": "समान द्रव्यमान संख्या लेकिन भिन्न परमाणु क्रमांक वाले परमाणुओं को कहा जाता है:",
        "opts": ["Isotopes", "Isobars", "Isotones", "Isomers"],
        "opts_hi": ["समस्थानिक", "समभारिक (Isobars)", "समन्यूट्रॉनिक", "समावयवी (Isomers)"],
        "ans": 1,
        "sol": "Isobars are atoms of different chemical elements that have the same mass number (A) but different atomic numbers (Z).",
        "sol_hi": "समभारिक (Isobars) विभिन्न रासायनिक तत्वों के वे परमाणु होते हैं जिनकी द्रव्यमान संख्या (A) समान लेकिन परमाणु क्रमांक (Z) भिन्न होता है।"
    },
    {
        "q": "What is the valency of Nitrogen (Atomic Number = 7)?",
        "q_hi": "नाइट्रोजन (परमाणु क्रमांक = 7) की संयोजकता (Valency) क्या है?",
        "opts": ["7", "5", "3", "2"],
        "opts_hi": ["7", "5", "3 (3)", "2"],
        "ans": 2,
        "sol": "Nitrogen has configuration 2, 5. It has 5 valence electrons. Valency = 8 - 5 = 3.",
        "sol_hi": "नाइट्रोजन का इलेक्ट्रॉनिक विन्यास 2, 5 है। इसमें 5 संयोजी इलेक्ट्रॉन हैं। संयोजकता = 8 - 5 = 3।"
    },
    {
        "q": "The electronic configuration of Sodium (Na, Z=11) is:",
        "q_hi": "सोडियम (Na, Z=11) का इलेक्ट्रॉनिक विन्यास है:",
        "opts": ["2, 9", "2, 8, 1", "8, 2, 1", "2, 7, 2"],
        "opts_hi": ["2, 9", "2, 8, 1 (2, 8, 1)", "8, 2, 1", "2, 7, 2"],
        "ans": 1,
        "sol": "Sodium has 11 electrons. The K shell takes 2, L shell takes 8, and the remaining 1 goes to the M shell: 2, 8, 1.",
        "sol_hi": "सोडियम में 11 इलेक्ट्रॉन होते हैं। K कोश में 2, L कोश में 8, और शेष 1 M कोश में जाता है: 2, 8, 1।"
    },
    {
        "q": "The concept of discrete, stationary orbits for electrons was proposed by:",
        "q_hi": "इलेक्ट्रॉनों के लिए विविक्त, स्थिर कक्षाओं की अवधारणा किसके द्वारा प्रस्तावित की गई थी?",
        "opts": ["J.J. Thomson", "Ernest Rutherford", "Niels Bohr", "Erwin Schrödinger"],
        "opts_hi": ["जे.जे. थॉमसन", "अर्नेस्ट रदरफोर्ड", "नील्स बोहर (Niels Bohr)", "इरविन श्रोडिंगर"],
        "ans": 2,
        "sol": "Niels Bohr modified Rutherford's model in 1913 by introducing quantized stationary orbits to prevent electrons from falling into the nucleus.",
        "sol_hi": "नील्स बोहर ने 1913 में इलेक्ट्रॉनों को नाभिक में गिरने से रोकने के लिए क्वांटम स्थिर कक्षाओं की शुरुआत करके रदरफोर्ड के मॉडल में संशोधन किया।"
    },
    {
        "q": "Which isotope is used in carbon dating to find the age of fossils?",
        "q_hi": "जीवाश्मों की आयु ज्ञात करने के लिए कार्बन डेटिंग में किस समस्थानिक का उपयोग किया जाता है?",
        "opts": ["Carbon-12", "Carbon-13", "Carbon-14", "Cobalt-60"],
        "opts_hi": ["कार्बन-12", "कार्बन-13", "कार्बन-14 (Carbon-14)", "कोबाल्ट-60"],
        "ans": 2,
        "sol": "Carbon-14 is a radioactive isotope of carbon used in radiocarbon dating to determine the age of organic materials.",
        "sol_hi": "कार्बन-14 कार्बन का एक रेडियोधर्मी समस्थानिक है जिसका उपयोग कार्बनिक पदार्थों की आयु निर्धारित करने के लिए रेडियोकार्बन डेटिंग में किया जाता है।"
    },
    {
        "q": "What is the mass number of an atom containing 6 protons and 8 neutrons?",
        "q_hi": "6 प्रोटॉन और 8 न्यूट्रॉन वाले परमाणु की द्रव्यमान संख्या क्या होगी?",
        "opts": ["6", "8", "14", "2"],
        "opts_hi": ["6", "8", "14 (14)", "2"],
        "ans": 2,
        "sol": "Mass Number (A) = Protons + Neutrons = 6 + 8 = 14.",
        "sol_hi": "द्रव्यमान संख्या (A) = प्रोटॉन + न्यूट्रॉन = 6 + 8 = 14।"
    },
    {
        "q": "Which quantum number determines the orientation of an orbital in space?",
        "q_hi": "कौन सी क्वांटम संख्या त्रिविम में कक्षक के अभिविन्यास (orientation) को निर्धारित करती है?",
        "opts": ["Principal Quantum Number", "Azimuthal Quantum Number", "Magnetic Quantum Number", "Spin Quantum Number"],
        "opts_hi": ["मुख्य क्वांटम संख्या", "द्विगंशी क्वांटम संख्या", "चुंबकीय क्वांटम संख्या (Magnetic Quantum Number)", "चक्रण क्वांटम संख्या"],
        "ans": 2,
        "sol": "The Magnetic Quantum Number (m_l) determines the spatial orientation of the orbital.",
        "sol_hi": "चुंबकीय क्वांटम संख्या (m_l) कक्षक के स्थानिक अभिविन्यास को निर्धारित करती है।"
    },
    {
        "q": "Which rule states that no two electrons in an atom can have the same set of four quantum numbers?",
        "q_hi": "कौन सा नियम बताता है कि एक परमाणु में किन्हीं दो इलेक्ट्रॉनों के लिए चारों क्वांटम संख्याओं का मान समान नहीं हो सकता?",
        "opts": ["Hund's Rule", "Aufbau Principle", "Pauli Exclusion Principle", "Heisenberg Principle"],
        "opts_hi": ["हुंड का नियम", "Aufbau सिद्धांत", "पाउली का अपवर्जन सिद्धांत (Pauli Exclusion Principle)", "हाइजेनबर्ग का सिद्धांत"],
        "ans": 2,
        "sol": "The Pauli Exclusion Principle states that no two electrons in an atom can have the same four quantum numbers, limiting an orbital to 2 electrons.",
        "sol_hi": "पाउली का अपवर्जन सिद्धांत बताता है कि किसी परमाणु में दो इलेक्ट्रॉनों के चारों क्वांटम नंबर समान नहीं हो सकते, जिससे एक कक्षक में अधिकतम 2 इलेक्ट्रॉन ही आ सकते हैं।"
    },
    {
        "q": "For the Azimuthal Quantum Number l = 1, what is the designation of the subshell?",
        "q_hi": "द्विगंशी क्वांटम संख्या l = 1 के लिए, उपकोश का नाम क्या होगा?",
        "opts": ["s", "p", "d", "f"],
        "opts_hi": ["s", "p (p)", "d", "f"],
        "ans": 1,
        "sol": "The subshells are designated as: l=0 is s, l=1 is p, l=2 is d, and l=3 is f.",
        "sol_hi": "उपकोशों को इस प्रकार नामित किया जाता है: l=0 के लिए s, l=1 के लिए p, l=2 के लिए d, और l=3 के लिए f।"
    },
    {
        "q": "According to the Aufbau Principle, which of the following orbitals is filled first?",
        "q_hi": "Aufbau सिद्धांत के अनुसार, निम्नलिखित में से कौन सा कक्षक पहले भरा जाता है?",
        "opts": ["3d", "4s", "4p", "4d"],
        "opts_hi": ["3d", "4s (4s)", "4p", "4d"],
        "ans": 1,
        "sol": "For 4s, n+l = 4+0 = 4. For 3d, n+l = 3+2 = 5. According to the (n+l) rule, 4s has lower energy and is filled before 3d.",
        "sol_hi": "4s के लिए n+l = 4+0 = 4। 3d के लिए n+l = 3+2 = 5। (n+l) नियम के अनुसार, 4s की ऊर्जा कम है और यह 3d से पहले भरा जाता है।"
    },
    {
        "q": "How many neutrons are present in one atom of Uranium-235 (Atomic number = 92)?",
        "q_hi": "यूरेनियम-235 (परमाणु संख्या = 92) के एक परमाणु में कितने न्यूट्रॉन मौजूद होते हैं?",
        "opts": ["92", "235", "143", "327"],
        "opts_hi": ["92", "235", "143 (143)", "327"],
        "ans": 2,
        "sol": "Number of Neutrons (N) = Mass Number (A) - Atomic Number (Z) = 235 - 92 = 143.",
        "sol_hi": "न्यूट्रॉनों की संख्या (N) = द्रव्यमान संख्या (A) - परमाणु क्रमांक (Z) = 235 - 92 = 143।"
    },
    {
        "q": "Who discovered the neutron?",
        "q_hi": "न्यूट्रॉन की खोज किसने की थी?",
        "opts": ["J.J. Thomson", "Ernest Rutherford", "James Chadwick", "Niels Bohr"],
        "opts_hi": ["जे.जे. थॉमसन", "अर्नेस्ट रदरफोर्ड", "जेम्स चैडविक (James Chadwick)", "नील्स बोहर"],
        "ans": 2,
        "sol": "James Chadwick discovered the neutron in 1932 by bombarding beryllium with alpha particles.",
        "sol_hi": "जेम्स चैडविक ने 1932 में बेरिलियम पर अल्फा कणों की बमबारी करके न्यूट्रॉन की खोज की थी।"
    },
    {
        "q": "Which of the following pairs are Isobars?",
        "q_hi": "निम्नलिखित में से कौन सा युग्म समभारिक (Isobars) है?",
        "opts": ["¹H and ²H", "¹²C and ¹⁴C", "⁴⁰Ar and ⁴⁰Ca", "¹⁶O and ¹⁸O"],
        "opts_hi": ["¹H और ²H", "¹²C और ¹⁴C", "⁴⁰Ar और ⁴⁰Ca (⁴⁰Ar and ⁴⁰Ca)", "¹⁶O और ¹⁸O"],
        "ans": 2,
        "sol": "Argon (⁴⁰Ar, Z=18) and Calcium (⁴⁰Ca, Z=20) have different atomic numbers but the same mass number (40), making them Isobars.",
        "sol_hi": "आर्गन (⁴⁰Ar, Z=18) और कैल्शियम (⁴⁰Ca, Z=20) के परमाणु क्रमांक अलग-अलग हैं लेकिन द्रव्यमान संख्या समान (40) है, जो उन्हें समभारिक बनाती है।"
    },
    {
        "q": "What is the maximum capacity of the N shell (n = 4) to hold electrons?",
        "q_hi": "N कोश (n = 4) की इलेक्ट्रॉन धारण करने की अधिकतम क्षमता क्या है?",
        "opts": ["8", "18", "32", "50"],
        "opts_hi": ["8", "18", "32 (32)", "50"],
        "ans": 2,
        "sol": "For the N shell, n=4. Max capacity = 2n² = 2 &times; (4)² = 2 &times; 16 = 32 electrons.",
        "sol_hi": "N कोश के लिए, n=4। अधिकतम क्षमता = 2n² = 2 &times; (4)² = 2 &times; 16 = 32 इलेक्ट्रॉन।"
    },
    {
        "q": "Which isotope is used to diagnose or treat Goitre (thyroid disorder)?",
        "q_hi": "घेंघा रोग (Goitre / थायराइड विकार) के निदान या उपचार में किस समस्थानिक का उपयोग किया जाता है?",
        "opts": ["Cobalt-60", "Iodine-131", "Uranium-238", "Sodium-24"],
        "opts_hi": ["कोबाल्ट-60", "आयोडीन-131 (Iodine-131)", "यूरेनियम-238", "सोडियम-24"],
        "ans": 1,
        "sol": "Iodine-131 is used in medical diagnostics and treatment of thyroid gland disorders, including goitre.",
        "sol_hi": "आयोडीन-131 का उपयोग चिकित्सा निदान और थायराइड ग्रंथि के विकारों (जैसे घेंघा) के उपचार में किया जाता है।"
    },
    {
        "q": "An atom has 8 valence electrons. Which group of elements does it belong to?",
        "q_hi": "एक परमाणु में 8 संयोजी इलेक्ट्रॉन होते हैं। यह किस समूह के तत्वों से संबंधित है?",
        "opts": ["Alkali Metals", "Halogens", "Noble Gases", "Chalcogens"],
        "opts_hi": ["क्षार धातुएं", "हैलोजन", "उत्कृष्ट गैसें (Noble Gases)", "कैल्कोजन"],
        "ans": 2,
        "sol": "Noble gases (except Helium which has 2) have 8 valence electrons, which gives them a stable octet and low reactivity.",
        "sol_hi": "उत्कृष्ट गैसों (हीलियम को छोड़कर, जिसमें 2 होते हैं) में 8 संयोजी इलेक्ट्रॉन होते हैं, जो उन्हें एक स्थिर अष्टक और कम क्रियाशीलता प्रदान करता है।"
    },
    {
        "q": "The pairing of electrons in p-orbitals starts only after all three orbitals are singly occupied. This is according to:",
        "q_hi": "p-कक्षकों में इलेक्ट्रॉनों का युग्मन तभी शुरू होता है जब तीनों कक्षक एक-एक करके भर जाते हैं। यह किसके अनुसार है?",
        "opts": ["Pauli Exclusion Principle", "Hund's Rule", "Aufbau Principle", "Bohr-Bury Rules"],
        "opts_hi": ["पाउली अपवर्जन सिद्धांत", "हुंड का नियम (Hund's Rule)", "Aufbau सिद्धांत", "बोहर-बरी नियम"],
        "ans": 1,
        "sol": "Hund's Rule of Maximum Multiplicity states that degenerate orbitals (same subshell) must be singly filled before pairing begins.",
        "sol_hi": "हुंड का नियम (Hund's Rule) बताता है कि एक ही उपकोश के कक्षकों में इलेक्ट्रॉनों का युग्मन तब तक नहीं होता जब तक कि सभी में एक-एक इलेक्ट्रॉन न भर जाए।"
    },
    {
        "q": "Which particle is responsible for carrying canal rays?",
        "q_hi": "कैनाल किरणों को ले जाने के लिए कौन सा कण जिम्मेदार है?",
        "opts": ["Electrons", "Protons", "Neutrons", "Alpha particles"],
        "opts_hi": ["इलेक्ट्रॉन", "प्रोटॉन (Protons)", "न्यूट्रॉन", "अल्फा कण"],
        "ans": 1,
        "sol": "Canal rays consist of positively charged gaseous ions, whose fundamental positive particles are protons.",
        "sol_hi": "कैनाल किरणों में धनावेशित गैसीय आयन होते हैं, जिनके मूलभूत धनावेशित कण प्रोटॉन होते हैं।"
    },
    {
        "q": "What is the shape of a p-orbital?",
        "q_hi": "p-कक्षक (p-orbital) का आकार कैसा होता है?",
        "opts": ["Spherical", "Dumbbell", "Double dumbbell", "Circular"],
        "opts_hi": ["गोलाकार", "डम्बल (Dumbbell)", "द्वि-डम्बल (Double dumbbell)", "वृत्ताकार"],
        "ans": 1,
        "sol": "An s-orbital is spherical, a p-orbital is dumbbell-shaped, and a d-orbital is double-dumbbell-shaped.",
        "sol_hi": "s-कक्षक गोलाकार होता है, p-कक्षक डम्बल के आकार का होता है, और d-कक्षक द्वि-डम्बल आकार का होता है।"
    },
    {
        "q": "An atom has 3 protons, 4 neutrons, and 3 electrons. What is its valency?",
        "q_hi": "एक परमाणु में 3 प्रोटॉन, 4 न्यूट्रॉन और 3 इलेक्ट्रॉन हैं। इसकी संयोजकता क्या है?",
        "opts": ["3", "4", "1", "2"],
        "opts_hi": ["3", "4", "1 (1)", "2"],
        "ans": 2,
        "sol": "The atomic number is Z=3 (Lithium). Electronic configuration is 2, 1. Having 1 valence electron, its valency is 1.",
        "sol_hi": "परमाणु संख्या Z=3 (लिथियम) है। इलेक्ट्रॉनिक विन्यास 2, 1 है। बाहरी कोश में 1 इलेक्ट्रॉन होने के कारण इसकी संयोजकता 1 है।"
    },
    {
        "q": "Which subatomic particle was discovered last?",
        "q_hi": "किस अपरमाणुक कण की खोज सबसे अंत में हुई थी?",
        "opts": ["Electron", "Proton", "Neutron", "Positron"],
        "opts_hi": ["इलेक्ट्रॉन", "प्रोटॉन", "न्यूट्रॉन (Neutron)", "पॉज़िट्रॉन"],
        "ans": 2,
        "sol": "The electron was discovered in 1897, the proton in 1919 (Rutherford), and the neutron in 1932 (Chadwick), which was the last of the three.",
        "sol_hi": "इलेक्ट्रॉन की खोज 1897 में हुई थी, प्रोटॉन की 1919 में (रदरफोर्ड द्वारा), और न्यूट्रॉन की 1932 में (चैडविक द्वारा), जो कि तीनों में सबसे अंत में था।"
    },
    {
        "q": "What designation is given to the orbital with n=3 and l=2?",
        "q_hi": "n=3 और l=2 वाले कक्षक को क्या नाम दिया जाता है?",
        "opts": ["3s", "3p", "3d", "4d"],
        "opts_hi": ["3s", "3p", "3d (3d)", "4d"],
        "ans": 2,
        "sol": "Since n=3 and l=2 (which corresponds to 'd'), the designation is 3d.",
        "sol_hi": "चूँकि n=3 और l=2 ('d' कक्षक) है, इसलिए इसे 3d कहा जाता है।"
    },
    {
        "q": "The sum of protons and neutrons in an atom is called the:",
        "q_hi": "किसी परमाणु में प्रोटॉनों और न्यूट्रॉनों के योग को कहा जाता है:",
        "opts": ["Atomic number", "Mass number", "Atomic mass", "Valency"],
        "opts_hi": ["परमाणु क्रमांक", "द्रव्यमान संख्या (Mass number)", "परमाणु द्रव्यमान", "संयोजकता"],
        "ans": 1,
        "sol": "The mass number (A) is the sum of protons and neutrons in the nucleus of an atom.",
        "sol_hi": "द्रव्यमान संख्या (A) परमाणु के नाभिक में मौजूद प्रोटॉनों और न्यूट्रॉनों का योग है।"
    },
    {
        "q": "Which of the following is not a isotopes of hydrogen?",
        "q_hi": "निम्नलिखित में से कौन सा हाइड्रोजन का समस्थानिक नहीं है?",
        "opts": ["Protium", "Deuterium", "Tritium", "Helium"],
        "opts_hi": ["प्रोटियम", "ड्यूटेरियम", "ट्राइटियम", "हीलियम (Helium)"],
        "ans": 3,
        "sol": "Protium, Deuterium, and Tritium are isotopes of hydrogen. Helium is a different element altogether.",
        "sol_hi": "प्रोटियम, ड्यूटेरियम और ट्राइटियम हाइड्रोजन के समस्थानिक हैं। हीलियम एक पूरी तरह से अलग तत्व है।"
    },
    {
        "q": "What is the maximum number of electrons that can be held in a single orbital?",
        "q_hi": "एक अकेले कक्षक (orbital) में अधिकतम कितने इलेक्ट्रॉन रह सकते हैं?",
        "opts": ["2", "6", "10", "14"],
        "opts_hi": ["2 (2)", "6", "10", "14"],
        "ans": 0,
        "sol": "According to the Pauli Exclusion Principle, any single orbital can hold a maximum of 2 electrons with opposite spins.",
        "sol_hi": "पाउली अपवर्जन सिद्धांत के अनुसार, कोई भी अकेला कक्षक विपरीत चक्रण वाले अधिकतम 2 इलेक्ट्रॉन ही धारण कर सकता है।"
    },
    {
        "q": "In the symbol ³⁵₁₇Cl, what does the number 17 represent?",
        "q_hi": "प्रतीक ³⁵₁₇Cl में, संख्या 17 क्या दर्शाती है?",
        "opts": ["Mass number", "Atomic number", "Number of neutrons", "Valency"],
        "opts_hi": ["द्रव्यमान संख्या", "परमाणु संख्या (Atomic number)", "न्यूट्रॉनों की संख्या", "संयोजकता"],
        "ans": 1,
        "sol": "In standard isotopic notation (ᴬ_Z X), the subscript Z is the Atomic Number (number of protons). So 17 is the atomic number.",
        "sol_hi": "मानक समस्थानिक संकेतन (ᴬ_Z X) में, निचला अंक Z परमाणु क्रमांक (प्रोटॉन संख्या) होता है। अतः 17 परमाणु क्रमांक है।"
    },
    {
        "q": "Which shell of an atom is filled first according to energy levels?",
        "q_hi": "ऊर्जा स्तरों के अनुसार परमाणु का कौन सा कोश सबसे पहले भरा जाता है?",
        "opts": ["K shell", "L shell", "M shell", "N shell"],
        "opts_hi": ["K कोश (K shell)", "L कोश", "M कोश", "N कोश"],
        "ans": 0,
        "sol": "The K shell (n=1) is closest to the nucleus, has the lowest energy level, and is filled first.",
        "sol_hi": "K कोश (n=1) नाभिक के सबसे निकट होता है, इसका ऊर्जा स्तर सबसे कम होता है, और यह सबसे पहले भरा जाता है।"
    },
    {
        "q": "The mass of an electron is approximately ________ times the mass of a proton.",
        "q_hi": "एक इलेक्ट्रॉन का द्रव्यमान प्रोटॉन के द्रव्यमान का लगभग ________ गुना होता है।",
        "opts": ["1", "1837", "1/1837", "2000"],
        "opts_hi": ["1", "1837", "1/1837 (1/1837)", "2000"],
        "ans": 2,
        "sol": "The mass of an electron is very small, about 1/1837 (often rounded to 1/2000) of the mass of a proton.",
        "sol_hi": "इलेक्ट्रॉन का द्रव्यमान बहुत कम होता है, जो प्रोटॉन के द्रव्यमान का लगभग 1/1837 (आमतौर पर 1/2000) भाग होता है।"
    },
    {
        "q": "What is the valency of Carbon (Z = 6)?",
        "q_hi": "कार्बन (Z = 6) की संयोजकता क्या है?",
        "opts": ["2", "4", "6", "8"],
        "opts_hi": ["2", "4 (4)", "6", "8"],
        "ans": 1,
        "sol": "Carbon has atomic number 6. Configuration is 2, 4. With 4 valence electrons, its combining capacity (valency) is 4.",
        "sol_hi": "कार्बन का परमाणु क्रमांक 6 है। इसका इलेक्ट्रॉनिक विन्यास 2, 4 है। बाहरी कोश में 4 इलेक्ट्रॉन होने के कारण इसकी संयोजकता 4 है।"
    },
    {
        "q": "Which subatomic particle is electrically neutral?",
        "q_hi": "कौन सा अपरमाणुक कण विद्युत रूप से उदासीन होता है?",
        "opts": ["Electron", "Proton", "Neutron", "Positron"],
        "opts_hi": ["इलेक्ट्रॉन", "प्रोटॉन", "न्यूट्रॉन (Neutron)", "पॉज़िट्रॉन"],
        "ans": 2,
        "sol": "Neutrons are neutral particles with zero net charge. Protons are positive and electrons are negative.",
        "sol_hi": "न्यूट्रॉन शून्य शुद्ध आवेश वाले उदासीन कण होते हैं। प्रोटॉन धनात्मक और इलेक्ट्रॉन ऋणात्मक होते हैं।"
    },
    {
        "q": "Which experiment disproved Thomson's 'plum pudding' model of the atom?",
        "q_hi": "किस प्रयोग ने थॉमसन के 'प्लस पुडिंग' परमाणु मॉडल को गलत साबित किया?",
        "opts": ["Milikan's oil drop experiment", "Rutherford's gold foil experiment", "Davisson-Germer experiment", "Cathode ray experiment"],
        "opts_hi": ["मिलिकन का तेल बूंद प्रयोग", "रदरफोर्ड का स्वर्ण पत्र प्रयोग (Rutherford's gold foil experiment)", "डेविसन-जर्मर प्रयोग", "कैथोड किरण प्रयोग"],
        "ans": 1,
        "sol": "Rutherford's alpha scattering gold foil experiment showed that the atom has a positive center nucleus, which disproved the plum pudding model.",
        "sol_hi": "रदरफोर्ड के स्वर्ण पत्र प्रयोग से पता चला कि परमाणु में एक धनात्मक केंद्र नाभिक होता है, जिसने प्लम पुडिंग मॉडल को गलत साबित कर दिया।"
    },
    {
        "q": "How many electrons are in the valence shell of Chlorine (Z = 17)?",
        "q_hi": "क्लोरीन (Z = 17) के संयोजी कोश (Valence shell) में कितने इलेक्ट्रॉन होते हैं?",
        "opts": ["1", "7", "8", "17"],
        "opts_hi": ["1", "7 (7)", "8", "17"],
        "ans": 1,
        "sol": "Chlorine has 17 electrons. The electronic configuration is 2, 8, 7. The outermost shell (valence shell) contains 7 electrons.",
        "sol_hi": "क्लोरीन में 17 इलेक्ट्रॉन होते हैं। इसका इलेक्ट्रॉनिक विन्यास 2, 8, 7 है। सबसे बाहरी कोश (संयोजी कोश) में 7 इलेक्ट्रॉन होते हैं।"
    },
    {
        "q": "Who proposed the plum pudding model of the atom?",
        "q_hi": "परमाणु का प्लम पुडिंग मॉडल किसने प्रस्तावित किया था?",
        "opts": ["John Dalton", "J.J. Thomson", "Ernest Rutherford", "Niels Bohr"],
        "opts_hi": ["जॉन डालटन", "जे.जे. थॉमसन (J.J. Thomson)", "अर्नेस्ट रदरफोर्ड", "नील्स बोहर"],
        "ans": 1,
        "sol": "J.J. Thomson proposed the plum pudding model in 1904, visualising the atom as electrons embedded in a sphere of positive charge.",
        "sol_hi": "जे.जे. थॉमसन ने 1904 में प्लम पुडिंग मॉडल प्रस्तावित किया था, जिसमें उन्होंने परमाणु को धनावेशित गोले में धंसे इलेक्ट्रॉनों के रूप में देखा था।"
    },
    {
        "q": "Which values are allowed for the Spin Quantum Number?",
        "q_hi": "चक्रण क्वांटम संख्या (Spin Quantum Number) के लिए कौन से मान अनुमत हैं?",
        "opts": ["0 and 1", "+1 and -1", "+1/2 and -1/2", "Any real number"],
        "opts_hi": ["0 और 1", "+1 और -1", "+1/2 और -1/2 (+1/2 and -1/2)", "कोई भी वास्तविक संख्या"],
        "ans": 2,
        "sol": "The electron can spin in only two directions: clockwise (+1/2) or counter-clockwise (-1/2).",
        "sol_hi": "इलेक्ट्रॉन केवल दो दिशाओं में घूम सकता है: दक्षिणावर्त (+1/2) या वामावर्त (-1/2)।"
    },
    {
        "q": "The atomic weight of Chlorine is 35.5. This fractional value is because:",
        "q_hi": "क्लोरीन का परमाणु भार 35.5 है। यह भिन्नात्मक (Fractional) मान किस कारण से है?",
        "opts": ["It has fractional protons", "It is an average mass of its isotopes Cl-35 and Cl-37", "It gains electrons from surroundings", "It has unstable neutrons"],
        "opts_hi": ["इसमें आंशिक प्रोटॉन होते हैं", "यह इसके समस्थानिकों Cl-35 और Cl-37 का औसत द्रव्यमान है (average mass of isotopes)", "यह परिवेश से इलेक्ट्रॉन प्राप्त करता है", "इसमें अस्थिर न्यूट्रॉन होते हैं"],
        "ans": 1,
        "sol": "Chlorine exists as a mixture of two isotopes (Cl-35 and Cl-37 in 3:1 ratio). The average atomic mass is calculated as (35*3 + 37*1)/4 = 35.5.",
        "sol_hi": "क्लोरीन दो समस्थानिकों (3:1 के अनुपात में Cl-35 और Cl-37) के मिश्रण के रूप में मौजूद है। औसत परमाणु द्रव्यमान की गणना इस प्रकार की जाती है: (35*3 + 37*1)/4 = 35.5।"
    },
    {
        "q": "Which subatomic particle resides outside the nucleus of an atom?",
        "q_hi": "कौन सा अपरमाणुक कण परमाणु के नाभिक के बाहर रहता है?",
        "opts": ["Proton", "Neutron", "Electron", "Deuteron"],
        "opts_hi": ["प्रोटॉन", "न्यूट्रॉन", "इलेक्ट्रॉन (Electron)", "ड्यूट्रॉन"],
        "ans": 2,
        "sol": "Electrons revolve outside the nucleus in specific energy levels/orbits, whereas protons and neutrons reside inside the nucleus.",
        "sol_hi": "इलेक्ट्रॉन नाभिक के बाहर विशिष्ट ऊर्जा स्तरों/कक्षाओं में चक्कर लगाते हैं, जबकि प्रोटॉन और न्यूट्रॉन नाभिक के अंदर रहते हैं।"
    },
    {
        "q": "The formula 2n² for determining maximum electrons in a shell was given by:",
        "q_hi": "किसी कोश में अधिकतम इलेक्ट्रॉनों के निर्धारण के लिए 2n² का सूत्र किसके द्वारा दिया गया था?",
        "opts": ["Dalton", "Rutherford", "Bohr and Bury", "Schrödinger"],
        "opts_hi": ["डालटन", "रदरफोर्ड", "बोहर और बरी (Bohr and Bury)", "श्रोडिंगर"],
        "ans": 2,
        "sol": "The Bohr-Bury scheme describes the distribution of electrons in different orbits of an atom using the 2n² rule.",
        "sol_hi": "बोहर-बरी योजना 2n² नियम का उपयोग करके परमाणु की विभिन्न कक्षाओं में इलेक्ट्रॉनों के वितरण का वर्णन करती है।"
    },
    {
        "q": "Which isotope is used as fuel in nuclear reactors?",
        "q_hi": "परमाणु रिएक्टरों में ईंधन के रूप में किस समस्थानिक का उपयोग किया जाता है?",
        "opts": ["Uranium-235", "Uranium-238", "Cobalt-60", "Carbon-14"],
        "opts_hi": ["यूरेनिंयम-235 (Uranium-235)", "यूरेनियम-238", "कोबाल्ट-60", "कार्बन-14"],
        "ans": 0,
        "sol": "Uranium-235 undergoes nuclear fission when bombarded with neutrons and is widely used as fuel in nuclear reactors.",
        "sol_hi": "यूरेनियम-235 पर न्यूट्रॉनों की बमबारी करने पर परमाणु विखंडन होता है और इसका उपयोग परमाणु रिएक्टरों में ईंधन के रूप में किया जाता है।"
    },
    {
        "q": "What is the valency of Helium (Z = 2)?",
        "q_hi": "हीलियम (Z = 2) की संयोजकता (Valency) क्या है?",
        "opts": ["2", "0", "1", "8"],
        "opts_hi": ["2", "0 (0)", "1", "8"],
        "ans": 1,
        "sol": "Helium has only 1 shell (K shell) which is completely filled with 2 electrons (duplet). Since it is stable, its valency is 0.",
        "sol_hi": "हीलियम में केवल 1 कोश (K कोश) होता है जो 2 इलेक्ट्रॉनों (द्विक) से पूरी तरह भरा होता है। चूंकि यह स्थिर है, इसकी संयोजकता 0 है।"
    },
    {
        "q": "Two atoms are called Isotones if they have:",
        "q_hi": "दो परमाणुओं को समन्यूट्रॉनिक (Isotones) कहा जाता है यदि उनके पास:",
        "opts": ["Same atomic number", "Same mass number", "Same number of neutrons", "Same number of electrons"],
        "opts_hi": ["समान परमाणु संख्या", "समान द्रव्यमान संख्या", "न्यूट्रॉनों की संख्या समान हो (Same number of neutrons)", "इलेक्ट्रॉनों की संख्या समान हो"],
        "ans": 2,
        "sol": "Isotones are atoms of different elements that contain the same number of neutrons in their nuclei.",
        "sol_hi": "समन्यूट्रॉनिक (Isotones) विभिन्न तत्वों के वे परमाणु होते हैं जिनके नाभिक में न्यूट्रॉनों की संख्या समान होती है।"
    },
    {
        "q": "What is the value of Azimuthal Quantum Number (l) for an s-orbital?",
        "q_hi": "s-कक्षक के लिए द्विगंशी क्वांटम संख्या (l) का मान क्या होता है?",
        "opts": ["0", "1", "2", "3"],
        "opts_hi": ["0 (0)", "1", "2", "3"],
        "ans": 0,
        "sol": "For s-orbital l=0. For p-orbital l=1. For d-orbital l=2. For f-orbital l=3.",
        "sol_hi": "s-कक्षक के लिए l=0। p-कक्षक के लिए l=1। d-कक्षक के लिए l=2। f-कक्षक के लिए l=3।"
    },
    {
        "q": "If n=2, what are the allowed values for the Azimuthal Quantum Number l?",
        "q_hi": "यदि n=2 है, तो द्विगंशी क्वांटम संख्या l के लिए कौन से मान अनुमत हैं?",
        "opts": ["0, 1, 2", "0, 1", "1, 2", "Only 2"],
        "opts_hi": ["0, 1, 2", "0, 1 (0, 1)", "1, 2", "केवल 2"],
        "ans": 1,
        "sol": "The allowed values for l range from 0 to (n-1). For n=2, l can be 0 (s-orbital) and 1 (p-orbital).",
        "sol_hi": "l के अनुमत मान 0 से (n-1) तक होते हैं। n=2 के लिए, l का मान 0 (s-कक्षक) और 1 (p-कक्षक) हो सकता है।"
    },
    {
        "q": "Who proposed the wave mechanical model of the atom based on wave-particle duality?",
        "q_hi": "तरंग-कण द्वैतता के आधार पर परमाणु का तरंग यांत्रिकी मॉडल (wave mechanical model) किसने प्रस्तावित किया था?",
        "opts": ["Niels Bohr", "Erwin Schrödinger", "Ernest Rutherford", "J.J. Thomson"],
        "opts_hi": ["नील्स बोहर", "इरविन श्रोडिंगर (Erwin Schrödinger)", "अर्नेस्ट रदरफोर्ड", "जे.जे. थॉमसन"],
        "ans": 1,
        "sol": "Erwin Schrödinger developed the wave equation in 1926, which forms the basis of the quantum mechanical model of the atom.",
        "sol_hi": "इरविन श्रोडिंगर ने 1926 में तरंग समीकरण विकसित किया, जो परमाणु के क्वांटम यांत्रिकी मॉडल का आधार है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which isotope is used in nuclear reactors as a neutron absorber or control rod material?",
        "q_hi": "परमाणु रिएक्टरों में न्यूट्रॉन अवशोषक या नियंत्रण छड़ (control rod) सामग्री के रूप में किस समस्थानिक का उपयोग किया जाता है?",
        "opts": ["Uranium-235", "Boron-10", "Cobalt-60", "Carbon-14"],
        "opts_hi": ["यूरेनियम-235", "बोरोन-10 (Boron-10)", "कोबाल्ट-60", "कार्बन-14"],
        "ans": 1,
        "sol": "Boron-10 has a high cross-section for neutron absorption and is commonly used in control rods of nuclear reactors.",
        "sol_hi": "बोरोन-10 में न्यूट्रॉन अवशोषण की उच्च क्षमता होती है और इसका उपयोग आमतौर पर परमाणु रिएक्टरों की नियंत्रण छड़ों में किया जाता है।"
    },
    {
        "q": "According to the n+l rule, which orbital fills first among 3d, 4s, 4p, and 5s?",
        "q_hi": "n+l नियम के अनुसार, 3d, 4s, 4p और 5s में से कौन सा कक्षक सबसे पहले भरता है?",
        "opts": ["3d", "4s", "4p", "5s"],
        "opts_hi": ["3d", "4s (4s)", "4p", "5s"],
        "ans": 1,
        "sol": "Calculating n+l: 4s (4+0=4), 3d (3+2=5), 4p (4+1=5), 5s (5+0=5). Since 4s has the lowest n+l value of 4, it fills first.",
        "sol_hi": "n+l की गणना: 4s (4+0=4), 3d (3+2=5), 4p (4+1=5), 5s (5+0=5)। चूँकि 4s का n+l मान सबसे कम (4) है, इसलिए यह सबसे पहले भरता है।"
    },
    {
        "q": "What is the total number of orbitals associated with the Principal Quantum Number n = 3?",
        "q_hi": "मुख्य क्वांटम संख्या n = 3 से जुड़े कक्षकों (orbitals) की कुल संख्या क्या है?",
        "opts": ["3", "6", "9", "18"],
        "opts_hi": ["3", "6", "9 (9)", "18"],
        "ans": 2,
        "sol": "The total number of orbitals in a shell 'n' is given by n². For n=3, number of orbitals = (3)² = 9 (one 3s, three 3p, and five 3d orbitals).",
        "sol_hi": "किसी कोश 'n' में कक्षकों की कुल संख्या n² द्वारा दी जाती है। n=3 के लिए, कक्षकों की संख्या = (3)² = 9 (एक 3s, तीन 3p, और पांच 3d कक्षक)।"
    },
    {
        "q": "An element has Z = 15. What is the valency of this element in its ground state?",
        "q_hi": "एक तत्व का Z = 15 है। मूल अवस्था (ground state) में इस तत्व की संयोजकता क्या होगी?",
        "opts": ["5", "3", "8", "2"],
        "opts_hi": ["5", "3 (3)", "8", "2"],
        "ans": 1,
        "sol": "Z=15 (Phosphorus). Electronic configuration is 2, 8, 5. Valence electrons = 5. Valency = 8 - 5 = 3.",
        "sol_hi": "Z=15 (फास्फोरस)। इलेक्ट्रॉनिक विन्यास 2, 8, 5 है। संयोजी इलेक्ट्रॉन = 5। संयोजकता = 8 - 5 = 3।"
    },
    {
        "q": "Which subatomic particle was discovered by bombarding Beryllium with alpha particles?",
        "q_hi": "बेरिलियम पर अल्फा कणों की बमबारी करके किस अपरमाणुक कण की खोज की गई थी?",
        "opts": ["Electron", "Proton", "Neutron", "Positron"],
        "opts_hi": ["इलेक्ट्रॉन", "प्रोटॉन", "न्यूट्रॉन (Neutron)", "पॉज़िट्रॉन"],
        "ans": 2,
        "sol": "James Chadwick bombarded Beryllium with alpha particles in 1932 and noticed the emission of highly penetrating neutral radiation, which led to the discovery of neutrons.",
        "sol_hi": "जेम्स चैडविक ने 1932 में बेरिलियम पर अल्फा कणों की बमबारी की और अत्यधिक मर्मभेदी उदासीन विकिरण के उत्सर्जन को देखा, जिससे न्यूट्रॉन की खोज हुई।"
    },
    {
        "q": "Which of the following is a pair of Isotones?",
        "q_hi": "निम्नलिखित में से कौन सा समन्यूट्रॉनिक (Isotones) का युग्म है?",
        "opts": ["³₀Si and ³¹₁₅P", "¹⁴₆C and ¹⁶₈O", "¹H and ³H", "⁴⁰Ar and ⁴⁰Ca"],
        "opts_hi": ["³₀Si और ³¹₁₅P (Silicon and Phosphorus)", "¹⁴₆C और ¹⁶₈O (Carbon and Oxygen)", "¹H और ³H", "⁴⁰Ar और ⁴⁰Ca"],
        "ans": 1,
        "sol": "Calculating neutrons (A-Z): For ¹⁴₆C, neutrons = 14-6 = 8. For ¹⁶₈O, neutrons = 16-8 = 8. Since both have 8 neutrons, they are Isotones.",
        "sol_hi": "न्यूट्रॉनों की गणना (A-Z): ¹⁴₆C के लिए, न्यूट्रॉन = 14-6 = 8। ¹⁶₈O के लिए, न्यूट्रॉन = 16-8 = 8। चूंकि दोनों में 8 न्यूट्रॉन हैं, वे समन्यूट्रॉनिक (Isotones) हैं।"
    },
    {
        "q": "Which quantum number specifies the energy subshell of an electron in an atom?",
        "q_hi": "कौन सी क्वांटम संख्या किसी परमाणु में इलेक्ट्रॉन के ऊर्जा उपकोश (subshell) को निर्दिष्ट करती है?",
        "opts": ["Principal Quantum Number", "Azimuthal Quantum Number", "Magnetic Quantum Number", "Spin Quantum Number"],
        "opts_hi": ["मुख्य क्वांटम संख्या", "द्विगंशी क्वांटम संख्या (Azimuthal Quantum Number)", "चुंबकीय क्वांटम संख्या", "चक्रण क्वांटम संख्या"],
        "ans": 1,
        "sol": "The Azimuthal Quantum Number (l) specifies the subshell (s, p, d, f) and shape of the electron orbital.",
        "sol_hi": "द्विगंशी क्वांटम संख्या (l) उपकोश (s, p, d, f) और इलेक्ट्रॉन कक्षक के आकार को निर्दिष्ट करती है।"
    },
    {
        "q": "What is the maximum number of electrons that can be filled in a d-subshell?",
        "q_hi": "एक d-उपकोश (d-subshell) में अधिकतम कितने इलेक्ट्रॉन भरे जा सकते हैं?",
        "opts": ["2", "6", "10", "14"],
        "opts_hi": ["2", "6", "10 (10)", "14"],
        "ans": 2,
        "sol": "A d-subshell has 5 orbitals. Since each orbital can hold 2 electrons, the d-subshell can accommodate a maximum of 10 electrons. Formula: 2(2l+1) = 2(2*2+1) = 10.",
        "sol_hi": "d-उपकोश में 5 कक्षक होते हैं। चूंकि प्रत्येक कक्षक में 2 इलेक्ट्रॉन हो सकते हैं, इसलिए d-उपकोश में अधिकतम 10 इलेक्ट्रॉन आ सकते हैं। सूत्र: 2(2l+1) = 2(2*2+1) = 10।"
    },
    {
        "q": "Who demonstrated that cathode rays consist of particles of very low mass compared to hydrogen?",
        "q_hi": "किसने प्रदर्शित किया कि कैथोड किरणों में हाइड्रोजन की तुलना में बहुत कम द्रव्यमान वाले कण होते हैं?",
        "opts": ["E. Goldstein", "J.J. Thomson", "John Dalton", "Robert Millikan"],
        "opts_hi": ["ई. गोल्डस्टीन", "जे.जे. थॉमसन (J.J. Thomson)", "जॉन डालटन", "रॉबर्ट मिलिकन"],
        "ans": 1,
        "sol": "J.J. Thomson determined the charge-to-mass (e/m) ratio of electrons, proving that they are subatomic particles much lighter than hydrogen atoms.",
        "sol_hi": "जे.जे. थॉमसन ने इलेक्ट्रॉनों के आवेश-से-द्रव्यमान (e/m) अनुपात को निर्धारित किया, जिससे साबित हुआ कि वे हाइड्रोजन परमाणुओं की तुलना में बहुत हल्के अपरमाणुक कण हैं।"
    },
    {
        "q": "The electronic configuration of Copper (Cu, Z=29) in its ground state is anomalous because of:",
        "q_hi": "तांबे (Copper, Z=29) का मूल अवस्था में इलेक्ट्रॉनिक विन्यास विसंगत (anomalous) होता है:",
        "opts": ["[Ar] 3d⁹ 4s²", "[Ar] 3d¹⁰ 4s¹", "[Ar] 3d⁸ 4s² 4p¹", "[Ar] 4s² 4p⁴"],
        "opts_hi": ["[Ar] 3d⁹ 4s²", "[Ar] 3d¹⁰ 4s¹ ([Ar] 3d¹⁰ 4s¹)", "[Ar] 3d⁸ 4s² 4p¹", "[Ar] 4s² 4p⁴"],
        "ans": 1,
        "sol": "Copper's configuration is [Ar] 3d¹⁰ 4s¹ instead of [Ar] 3d⁹ 4s² because half-filled and fully-filled subshells (like 3d¹⁰) have extra stability.",
        "sol_hi": "तांबे का विन्यास [Ar] 3d⁹ 4s² के बजाय [Ar] 3d¹⁰ 4s¹ होता है क्योंकि आधे भरे और पूरी तरह भरे हुए उपकोशों (जैसे 3d¹⁰) में अतिरिक्त स्थिरता होती है।"
    },
    {
        "q": "Which particles were used by Rutherford to bombard the gold foil?",
        "q_hi": "रदरफोर्ड द्वारा सोने की पन्नी पर बमबारी करने के लिए किन कणों का उपयोग किया गया था?",
        "opts": ["Protons", "Neutrons", "Alpha particles", "Beta particles"],
        "opts_hi": ["प्रोटॉन", "न्यूट्रॉन", "अल्फा कण (Alpha particles)", "बीटा कण"],
        "ans": 2,
        "sol": "Rutherford used fast-moving Helium-4 nuclei, which are double-charged helium ions called alpha particles (He²⁺).",
        "sol_hi": "रदरफोर्ड ने तेजी से चलने वाले हीलियम-4 नाभिकों का उपयोग किया, जो कि द्वि-आवेशित हीलियम आयन होते हैं जिन्हें अल्फा कण (He²⁺) कहा जाता है।"
    },
    {
        "q": "What is the relation between mass number (A), atomic number (Z), and number of neutrons (N)?",
        "q_hi": "द्रव्यमान संख्या (A), परमाणु संख्या (Z) और न्यूट्रॉनों की संख्या (N) के बीच क्या संबंध है?",
        "opts": ["A = Z - N", "A = Z + N", "Z = A + N", "N = Z - A"],
        "opts_hi": ["A = Z - N", "A = Z + N (A = Z + N)", "Z = A + N", "N = Z - A"],
        "ans": 1,
        "sol": "Mass number (A) is the sum of protons (Z) and neutrons (N). Therefore, A = Z + N.",
        "sol_hi": "द्रव्यमान संख्या (A) प्रोटॉन (Z) और न्यूट्रॉन (N) का योग है। इसलिए, A = Z + N।"
    },
    {
        "q": "Which subatomic particle is the lightest?",
        "q_hi": "कौन सा अपरमाणुक कण सबसे हल्का होता है?",
        "opts": ["Proton", "Neutron", "Electron", "Alpha particle"],
        "opts_hi": ["प्रोटॉन", "न्यूट्रॉन", "इलेक्ट्रॉन (Electron)", "अल्फा कण"],
        "ans": 2,
        "sol": "The electron has a mass of 9.1 &times; 10⁻³¹ kg, which is about 1/1837 times the mass of a proton or neutron, making it the lightest.",
        "sol_hi": "इलेक्ट्रॉन का द्रव्यमान 9.1 &times; 10⁻³¹ kg होता है, जो प्रोटॉन या न्यूट्रॉन के द्रव्यमान का लगभग 1/1837 गुना होता है, जिससे यह सबसे हल्का होता है।"
    },
    {
        "q": "What is the valency of Argon (Ar, Z = 18)?",
        "q_hi": "आर्गन (Ar, Z = 18) की संयोजकता (Valency) क्या है?",
        "opts": ["8", "0", "2", "6"],
        "opts_hi": ["8", "0 (0)", "2", "6"],
        "ans": 1,
        "sol": "Argon has electronic configuration 2, 8, 8. Its valence shell (M shell) has 8 electrons, completing its octet. Hence, its combining capacity (valency) is 0.",
        "sol_hi": "आर्गन का इलेक्ट्रॉनिक विन्यास 2, 8, 8 है। इसके संयोजी कोश (M कोश) में 8 इलेक्ट्रॉन होते हैं, जो इसका अष्टक पूरा करते हैं। इसलिए इसकी संयोजकता 0 है।"
    },
    {
        "q": "Which of the following describes Hund's Rule?",
        "q_hi": "निम्नलिखित में से कौन हुंड के नियम (Hund's Rule) का वर्णन करता है?",
        "opts": ["No two electrons can have same spins in an orbital", "Orbitals of equal energy are occupied singly before pairing", "Electrons fill lowest energy orbital first", "Orbitals can hold maximum 2 electrons"],
        "opts_hi": ["एक कक्षक में दो इलेक्ट्रॉनों के चक्रण समान नहीं हो सकते", "समान ऊर्जा वाले कक्षक युग्मन से पहले एक-एक करके भरे जाते हैं (Occupied singly before pairing)", "इलेक्ट्रॉन पहले निम्नतम ऊर्जा कक्षक भरते हैं", "कक्षकों में अधिकतम 2 इलेक्ट्रॉन हो सकते हैं"],
        "ans": 1,
        "sol": "Hund's Rule states that degenerate orbitals (orbitals of equal energy) are singly occupied with parallel spins before electron pairing begins.",
        "sol_hi": "हुंड का नियम बताता है कि समान ऊर्जा वाले कक्षक (degenerate orbitals) इलेक्ट्रॉनों के युग्मन से पहले समानांतर चक्रण के साथ एक-एक करके भरे जाते हैं।"
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
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Thoroughly review subatomic particles, atomic models, electronic configuration principles, and quantum numbers.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Subatomic Particles & Cathode/Anode Rays",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which particle is the heaviest among subatomic particles?", "opts": ["Electron", "Proton", "Neutron", "Positron"], "ans": 2, "sol": "The neutron is slightly heavier than the proton (1.675 x 10^-27 kg vs 1.672 x 10^-27 kg)."},
                    {"type": "True/False", "q": "True or False: Cathode rays consist of positively charged particles.", "ans": False, "sol": "False. Cathode rays consist of negatively charged electrons."},
                    {"type": "Fill in the Blank", "q": "The electron was discovered by ________.", "ans": "J.J. Thomson", "sol": "J.J. Thomson discovered the electron in 1897."}
                ]
            },
            {
                "title": "2. Atomic Models: Thomson, Rutherford, Bohr",
                "masteryZone": [
                    {"type": "MCQ", "q": "Rutherford's gold foil experiment proved the presence of:", "opts": ["Electrons", "Protons", "Nucleus", "Neutrons"], "ans": 2, "sol": "It proved the presence of a tiny, dense, positively charged nucleus in the center of the atom."},
                    {"type": "True/False", "q": "True or False: In Bohr's model, electrons can revolve in any circular path of any radius.", "ans": False, "sol": "False. Electrons revolve only in certain quantized discrete orbits where they do not radiate energy."}
                ]
            },
            {
                "title": "3. Isotopes, Isobars, Isotones & Valency",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which isotope is used in treating Goitre?", "opts": ["Cobalt-60", "Carbon-14", "Iodine-131", "Uranium-235"], "ans": 2, "sol": "Iodine-131 is used to treat goitre (thyroid disorder)."},
                    {"type": "True/False", "q": "True or False: Isobars have the same chemical properties.", "ans": False, "sol": "False. Isobars have different atomic numbers (different elements), so they have completely different chemical properties."}
                ]
            },
            {
                "title": "4. Quantum Numbers & Electronic Configuration Rules",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which quantum number describes the shape of the orbital?", "opts": ["Principal (n)", "Azimuthal (l)", "Magnetic (m)", "Spin (s)"], "ans": 1, "sol": "The Azimuthal Quantum Number (l) determines the subshell shape (s, p, d, f)."},
                    {"type": "True/False", "q": "True or False: The 3d orbital is filled before the 4s orbital according to Aufbau Principle.", "ans": False, "sol": "False. The 4s orbital is filled before 3d because it has a lower n+l value (4 vs 5)."}
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
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "अपरमाणुक कणों, परमाणु मॉडलों, इलेक्ट्रॉनिक विन्यास के सिद्धांतों और क्वांटम संख्याओं की गहन समीक्षा करें।", "sections": deep_dive_hi}
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
                "title": "1. अपरमाणुक कण एवं कैथोड/एनोड किरणें",
                "masteryZone": [
                    {"type": "MCQ", "q": "अपरमाणुक कणों में सबसे भारी कण कौन सा है?", "opts": ["इलेक्ट्रॉन", "प्रोटॉन", "न्यूट्रॉन", "पॉज़िट्रॉन"], "ans": 2, "sol": "न्यूट्रॉन प्रोटॉन से थोड़ा भारी होता है (1.675 x 10^-27 kg बनाम 1.672 x 10^-27 kg)।"},
                    {"type": "True/False", "q": "सही या गलत: कैथोड किरणें धनावेशित कणों से बनी होती हैं।", "ans": False, "sol": "गलत। कैथोड किरणें ऋणावेशित इलेक्ट्रॉनों से बनी होती हैं।"},
                    {"type": "Fill in the Blank", "q": "इलेक्ट्रॉन की खोज किसके द्वारा की गई थी? ________", "ans": "जे.जे. थॉमसन", "sol": "जे.जे. थॉमसन ने 1897 में इलेक्ट्रॉन की खोज की थी।"}
                ]
            },
            {
                "title": "2. परमाणु मॉडल: थॉमसन, रदरफोर्ड, बोहर",
                "masteryZone": [
                    {"type": "MCQ", "q": "रदरफोर्ड के स्वर्ण पत्र प्रयोग ने किसकी उपस्थिति सिद्ध की?", "opts": ["इलेक्ट्रॉन", "प्रोटॉन", "नाभिक", "न्यूट्रॉन"], "ans": 2, "sol": "इसने परमाणु के केंद्र में एक बहुत छोटे, सघन, धनावेशित नाभिक की उपस्थिति सिद्ध की।"},
                    {"type": "True/False", "q": "सही या गलत: बोहर के मॉडल में इलेक्ट्रॉन किसी भी त्रिज्या के किसी भी वृत्ताकार पथ में घूम सकते हैं।", "ans": False, "sol": "गलत। इलेक्ट्रॉन केवल कुछ निश्चित क्वांटम कक्षाओं में घूमते हैं जहाँ वे ऊर्जा विकीर्ण नहीं करते हैं।"}
                ]
            },
            {
                "title": "3. समस्थानिक, समभारिक, समन्यूट्रॉनिक एवं संयोजकता",
                "masteryZone": [
                    {"type": "MCQ", "q": "घेंघा रोग के उपचार में किस समस्थानिक का उपयोग किया जाता है?", "opts": ["कोबाल्ट-60", "कार्बन-14", "आयोडीन-131", "यूरेनियम-235"], "ans": 2, "sol": "आयोडीन-131 का उपयोग घेंघा (थायराइड विकार) के उपचार में किया जाता है।"},
                    {"type": "True/False", "q": "सही या गलत: समभारिकों के रासायनिक गुण समान होते हैं।", "ans": False, "sol": "गलत। समभारिकों के परमाणु क्रमांक भिन्न (अलग तत्व) होते हैं, इसलिए उनके रासायनिक गुण पूरी तरह भिन्न होते हैं।"}
                ]
            },
            {
                "title": "4. क्वांटम संख्याएं एवं इलेक्ट्रॉनिक विन्यास के नियम",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सी क्वांटम संख्या कक्षक के आकार का वर्णन करती है?", "opts": ["मुख्य (n)", "द्विगंशी (l)", "चुंबकीय (m)", "चक्रण (s)"], "ans": 1, "sol": "द्विगंशी क्वांटम संख्या (l) उपकोश का आकार (s, p, d, f) निर्धारित करती है।"},
                    {"type": "True/False", "q": "सही या गलत: Aufbau सिद्धांत के अनुसार 3d कक्षक 4s कक्षक से पहले भरा जाता है।", "ans": False, "sol": "गलत। 4s कक्षक 3d से पहले भरा जाता है क्योंकि इसका n+l मान कम (4 बनाम 5) होता है।"}
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
