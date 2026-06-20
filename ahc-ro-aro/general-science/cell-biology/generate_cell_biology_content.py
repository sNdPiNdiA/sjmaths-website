# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "cell-biology"
TOPIC_DISPLAY = "Cell Biology"
TOPIC_DISPLAY_HI = "कोशिका विज्ञान"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\general-science\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "General Science",
    "parentUrl": "../",
    "current": "Cell Biology"
}

hero_en = {
    "title": "Cell Biology",
    "description": "Master cell structures, prokaryotes vs. eukaryotes, organelles (mitochondria, chloroplasts, lysosomes), chromosome classifications, and key mechanisms of cell division (Mitosis & Meiosis) for competitive exams."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Cell Biology Mock Test",
        "description": "Test your knowledge of cellular structures, organelles, division phases, and historical discoveries. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Historical Milestones in Cell Biology",
    "description": "Key scientific discoveries that shaped the Cell Theory and modern cytology.",
    "cards": [
        {
            "period": "Discovery of Dead Cells",
            "date": "1665",
            "details": "Robert Hooke examines thin cork slices under a primitive microscope, coined the term 'Cell' (cellula meaning small rooms)."
        },
        {
            "period": "Discovery of Living Cells",
            "date": "1674",
            "details": "Anton van Leeuwenhoek observes free-living cells (bacteria, protozoa, sperm, red blood cells) under an improved microscope, calling them 'animalcules'."
        },
        {
            "period": "Cell Theory Proposal",
            "date": "1838-1839",
            "details": "M.J. Schleiden (botanist) and Theodore Schwann (zoologist) propose that all plants and animals are composed of cells, making cell the basic unit of life."
        },
        {
            "period": "Cell Lineage Concept",
            "date": "1855",
            "details": "Rudolf Virchow adds the crucial third tenet: 'Omnis cellula e cellula'—all cells arise from pre-existing cells."
        },
        {
            "period": "Electron Microscope Invention",
            "date": "1931",
            "details": "Ernst Ruska and Max Knoll build the first electron microscope, allowing scientists to see ultra-structures of cell organelles."
        }
    ]
}

mnemonics_en = {
    "title": "Cell Biology Mnemonics",
    "description": "Easy-to-remember memory aids for cell structures and division phases.",
    "items": [
        {
            "title": "Mnemonic 1: Stages of Mitosis",
            "phrase": "\"I Proposed Men Are Tall (IPMAT)\"",
            "decryption": "Remember the sequence of cell division stages:<br>• <strong>I</strong>: Interphase (preparation)<br>• <strong>P</strong>: Prophase (condensation)<br>• <strong>M</strong>: Metaphase (alignment at middle)<br>• <strong>A</strong>: Anaphase (pulling apart)<br>• <strong>T</strong>: Telophase (two new nuclei)"
        },
        {
            "title": "Mnemonic 2: Meiosis Prophase I Sub-stages",
            "phrase": "\"Lazy Zebras Play Dual Decisions (LZPDD)\"",
            "decryption": "Remember Meiosis Prophase I phases in chronological order:<br>• <strong>L</strong>eptotene (chromosomes condense)<br>• <strong>Z</strong>ygote (synapsis/pairing)<br>• <strong>P</strong>achytene (crossing over/recombination)<br>• <strong>D</strong>iplotene (chiasmata visible)<br>• <strong>D</strong>iakinesis (nuclear envelope breaks)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Click to flip and test your Cytology knowledge.",
    "items": [
        {
            "question": "Which organelle is called the 'Suicide Bag' of the cell and why?",
            "answer": "<strong>Lysosomes</strong>. They contain powerful hydrolytic enzymes that digest cellular wastes. If the cell is damaged, they can burst and digest the cell itself.",
            "icon": "fa-skull-crossbones"
        },
        {
            "question": "Differentiate between 70S and 80S ribosomes.",
            "answer": "• <strong>70S ribosomes</strong>: Found in prokaryotes, mitochondria, and chloroplasts. Subunits are 50S and 30S.<br>• <strong>80S ribosomes</strong>: Found in eukaryotic cytoplasm. Subunits are 60S and 40S. ('S' stands for Svedberg unit of sedimentation coefficient).",
            "icon": "fa-microscope"
        },
        {
            "question": "Why is the inner membrane of Mitochondria deeply folded into cristae?",
            "answer": "To <strong>maximize the surface area</strong> available for chemical reactions of the Electron Transport Chain (ETC) and ATP synthase, optimizing ATP generation.",
            "icon": "fa-bolt"
        },
        {
            "question": "What is 'Crossing Over' and when does it occur?",
            "answer": "The exchange of genetic material between non-sister chromatids of homologous chromosomes. It occurs during the <strong>Pachytene</strong> stage of Prophase I in Meiosis, leading to genetic variation.",
            "icon": "fa-dna"
        }
    ]
}

traps_en = {
    "title": "Common Cytology Exam Traps",
    "items": [
        "<strong>Trap 1:</strong> Believing viruses are cellular organisms. Viruses are **acellular/non-cellular** entities. They lack cell machinery and are an exception to Cell Theory. They only reproduce inside host cells.",
        "<strong>Trap 2:</strong> Confusing Plant and Animal vacuoles. Plant cells have a **single, massive central vacuole** (occupying up to 90% volume) bounded by the **tonoplast** membrane. Animal cells have multiple small, temporary vacuoles.",
        "<strong>Trap 3:</strong> Misinterpreting Karyotype Metaphase study. Chromosomes are best studied, counted, and photographed during **Metaphase** because they are maximally condensed and aligned at the equatorial plate. Do not confuse it with Anaphase (where they pull apart).",
        "<strong>Trap 4:</strong> Assuming all eukaryotic cells contain a nucleus. Mature mammalian **Red Blood Cells (RBCs)** and plant **sieve tube cells** are **enucleated** (lack a nucleus) to optimize transport efficiency."
    ]
}

deep_dive_en = [
    {
        "title": "1. Cell Theory, Prokaryotic vs. Eukaryotic Cells & Cell Walls",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Cell Theory Tenets:</strong> Proposed by Schleiden and Schwann (1839), modified by Virchow (1855). State: (1) All living organisms are made of cells. (2) The cell is the structural/functional unit of life. (3) All cells arise from pre-existing cells. <strong>Exceptions:</strong> Viruses, Viroids, Prions (lack protoplasm/cellular structure).</li>
          <li style="margin-bottom: 0.75rem;"><strong>Prokaryotic vs. Eukaryotic Cells:</strong>
            <br>• <strong>Prokaryotes:</strong> No membrane-bound nucleus (naked DNA in nucleoid region). Lacks double-membranous organelles. Ribosomes are 70S. Cell wall contains peptidoglycan (in bacteria). Examples: Bacteria, Cyanobacteria (Blue-green algae), Mycoplasma (PPLO - smallest living cell, lacks cell wall).
            <br>• <strong>Eukaryotes:</strong> Defined nucleus with nuclear membrane. Double-membrane organelles (mitochondria, plastids) present. Ribosomes are 80S (cytoplasm) & 70S (organelles). Examples: Protists, Fungi, Plants, Animals.
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>Cell Wall & Cell Membrane:</strong>
            <br>• <strong>Cell Wall:</strong> Rigid, fully permeable, non-living outer layer. Present in Plants (cellulose), Fungi (chitin), Bacteria (peptidoglycan). Absent in Animals.
            <br>• <strong>Cell Membrane:</strong> Semi-permeable, living, fluid-like phospholipid bilayer with embedded proteins. Described by the <strong>Fluid Mosaic Model</strong> (Singer & Nicolson, 1972).
          </li>
        </ul>
        
        <!-- SVG Diagram 1: Prokaryote vs Eukaryote -->
        <svg viewBox="0 0 800 280" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .border-line { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 2px; }
            .prok-bg { fill: rgba(230, 126, 34, 0.08); stroke: #d35400; stroke-width: 2; rx: 12px;}
            .euk-bg { fill: rgba(52, 152, 219, 0.08); stroke: #2980b9; stroke-width: 2; rx: 12px;}
            .inner-cell { fill: rgba(46, 204, 113, 0.15); stroke: #27ae60; stroke-width: 1.5; }
            .nucleoid { fill: none; stroke: #c0392b; stroke-width: 1.5; stroke-dasharray: 2; }
            .organelle { fill: #9b59b6; stroke: #8e44ad; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            .label-head { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 14px; }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .border-line { stroke: #cbd5e1; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">Prokaryotic Cell (Left) vs Eukaryotic Cell (Right)</text>
          
          <!-- Prokaryotic Cell -->
          <g transform="translate(60, 50)">
            <rect x="0" y="0" width="300" height="190" class="prok-bg" />
            <text x="150" y="25" class="label-head" fill="#d35400" text-anchor="middle">Prokaryote (e.g., Bacteria)</text>
            <path d="M 40 100 Q 80 140 120 90 T 260 110" class="nucleoid" />
            <text x="150" y="85" class="annot-text" fill="#c0392b" font-weight="bold" text-anchor="middle">Naked DNA (Nucleoid)</text>
            <circle cx="50" cy="150" r="2" fill="#2c3e50" />
            <circle cx="80" cy="160" r="2" fill="#2c3e50" />
            <circle cx="210" cy="150" r="2" fill="#2c3e50" />
            <text x="130" y="170" class="annot-text" text-anchor="middle">70S Ribosomes</text>
            <text x="150" y="145" class="annot-text" text-anchor="middle">No membrane organelles</text>
          </g>
          
          <!-- Eukaryotic Cell -->
          <g transform="translate(440, 50)">
            <rect x="0" y="0" width="300" height="190" class="euk-bg" />
            <text x="150" y="25" class="label-head" fill="#2980b9" text-anchor="middle">Eukaryote (Plant/Animal)</text>
            <circle cx="150" cy="110" r="30" class="inner-cell" />
            <circle cx="150" cy="110" r="10" fill="#27ae60" />
            <text x="150" y="70" class="annot-text" fill="#27ae60" font-weight="bold" text-anchor="middle">True Nucleus</text>
            
            <rect x="50" y="70" width="30" height="15" rx="3" class="organelle" />
            <text x="65" y="100" class="annot-text" text-anchor="middle">Mitochondria</text>
            
            <circle cx="240" cy="120" r="3" fill="#2c3e50" />
            <circle cx="250" cy="130" r="3" fill="#2c3e50" />
            <text x="240" y="155" class="annot-text" text-anchor="middle">80S Ribosomes</text>
            <text x="150" y="170" class="annot-text" text-anchor="middle">Membrane-bound organelles present</text>
          </g>
        </svg>"""
    },
    {
        "title": "2. Structure & Function of Cell Organelles (Mitochondria, Chloroplasts, Lysosomes)",
        "content": """<p>Eukaryotic cells contain specialized subcellular components called organelles. Their roles and properties are highly tested in competitive exams:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Organelle</th>
                <th>Membrane Status</th>
                <th>Key Discoverer / Term</th>
                <th>Core Function & Exam Notes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Mitochondria</strong></td>
                <td>Double Membrane</td>
                <td>Kölliker (discovered), Benda (coined term)</td>
                <td><strong>Powerhouse of the Cell</strong>: Site of aerobic respiration (Krebs Cycle, Electron Transport). Synthesizes <strong>ATP</strong>. Contains circular DNA and 70S ribosomes (Semi-autonomous). Shows maternal inheritance.</td>
              </tr>
              <tr>
                <td><strong>Plastids</strong> (Chloroplast)</td>
                <td>Double Membrane</td>
                <td>Schimper (coined Chloroplast)</td>
                <td><strong>Kitchen of the Cell</strong>: Found in plants. Contains chlorophyll pigment. Site of photosynthesis (Light reaction in <strong>Thylakoid/Grana</strong>; Dark reaction in <strong>Stroma</strong>). Semi-autonomous (own DNA/70S ribosomes).</td>
              </tr>
              <tr>
                <td><strong>Ribosome</strong></td>
                <td>Non-Membranous</td>
                <td>George Palade (discovered Palade particles)</td>
                <td><strong>Protein Factory</strong>: Composed of RNA (rRNA) and proteins. Site of protein synthesis. Smallest organelle. Found free in cytoplasm or bound to Rough Endoplasmic Reticulum (RER).</td>
              </tr>
              <tr>
                <td><strong>Lysosome</strong></td>
                <td>Single Membrane</td>
                <td>Christian de Duve</td>
                <td><strong>Suicidal Bags</strong>: Rich in acid hydrolases (active at pH ~5). Autophagy, cell debris cleaning, cell digestion under pathological conditions.</td>
              </tr>
              <tr>
                <td><strong>Endoplasmic Reticulum (ER)</strong></td>
                <td>Single Membrane</td>
                <td>Porter, Claude & Fullam</td>
                <td><strong>Rough ER (RER):</strong> Has ribosomes; involved in protein folding/transport. <br><strong>Smooth ER (SER):</strong> Lacks ribosomes; synthesizes lipids/steroid hormones, detoxifies drugs/toxins in liver.</td>
              </tr>
              <tr>
                <td><strong>Golgi Apparatus</strong></td>
                <td>Single Membrane</td>
                <td>Camillo Golgi</td>
                <td><strong>Director of Macromolecular Traffic</strong>: Packaging, sorting, and chemical modification of proteins and lipids. Site of glycoprotein and glycolipid formation. Contributes to lysosome formation.</td>
              </tr>
              <tr>
                <td><strong>Nucleus</strong></td>
                <td>Double Membrane</td>
                <td>Robert Brown (1831)</td>
                <td><strong>Brain of the Cell</strong>: Contains genetic material (DNA/chromatin). Houses the <strong>nucleolus</strong> (site of active rRNA synthesis and ribosome subunit assembly). Bounded by a porous nuclear envelope.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. Chromosome Classifications & Cell Division (Mitosis vs. Meiosis)",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>Chromosome Anatomy & Centromere Classifications:</strong> Chromosomes are thread-like structures containing chromatin (DNA + Histone proteins). Based on the location of the **Centromere** (primary constriction), they are classified into:
            <br>• <strong>Metacentric:</strong> Centromere in the middle; forms two equal arms (V-shape during anaphase).
            <br>• <strong>Sub-metacentric:</strong> Centromere slightly away from the center; one arm is slightly shorter (L-shape during anaphase).
            <br>• <strong>Acrocentric:</strong> Centromere close to one end; one arm is extremely short, the other is long (J-shape during anaphase).
            <br>• <strong>Telocentric:</strong> Centromere at the terminal end; possesses only one arm (I-shape / rod-shape during anaphase).
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>Mitosis (Equational Division):</strong> Occurs in somatic cells. Results in two identical diploid (2n) daughter cells. 
            <br>• **Prophase:** Chromatin condenses into chromosomes; spindle fibers form; nucleolus and nuclear envelope disappear.
            <br>• **Metaphase:** Chromosomes line up at the cell's equator. Studied for karyotype analysis.
            <br>• **Anaphase:** Sister chromatids split at centromere and pull to opposite poles (shortest phase).
            <br>• **Telophase:** Nuclear membranes reform around two sets of chromosomes; chromosomes decondense.
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>Meiosis (Reductional Division):</strong> Occurs in germ/reproductive cells. Reduces the chromosome number by half to produce four haploid (n) gametes. Consists of Meiosis I (reductional) and Meiosis II (equational).
            <br>• **Prophase I (Highly Tested sub-stages):**
            <br>&nbsp;&nbsp;1. <em>Leptotene:</em> Chromatin threads condense.
            <br>&nbsp;&nbsp;2. <em>Zygotene:</em> Pairing of homologous chromosomes (**Synapsis**) occurs, forming a bivalent (synaptonemal complex).
            <br>&nbsp;&nbsp;3. <em>Pachytene:</em> Non-sister chromatids of homologous chromosomes exchange genetic material (**Crossing over** mediated by *recombinase* enzyme).
            <br>&nbsp;&nbsp;4. <em>Diplotene:</em> Synaptonemal complex dissolves; homologous chromosomes separate slightly but remain connected at cross points called **Chiasmata**.
            <br>&nbsp;&nbsp;5. <em>Diakinesis:</em> Chiasmata move to chromosome ends (terminalization); nuclear envelope disintegrates.
          </li>
        </ul>
        
        <!-- SVG Diagram 2: Chromosome Anatomy -->
        <svg viewBox="0 0 800 220" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .chrom-arm { fill: rgba(155, 89, 182, 0.2); stroke: #8e44ad; stroke-width: 2; }
            .centromere { fill: #e74c3c; stroke: #c0392b; stroke-width: 1.5; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">Chromosome Types based on Centromere Position</text>
          
          <!-- Metacentric -->
          <g transform="translate(60, 50)">
            <path d="M 40 10 L 40 70 M 60 10 L 60 70 M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">Metacentric</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(Equal Arms - V)</text>
          </g>
          
          <!-- Sub-metacentric -->
          <g transform="translate(240, 50)">
            <path d="M 40 30 L 40 70 M 60 30 L 60 70 M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">Sub-metacentric</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(Shorter p-arm - L)</text>
          </g>
          
          <!-- Acrocentric -->
          <g transform="translate(420, 50)">
            <path d="M 40 50 L 40 70 M 60 50 L 60 70 M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">Acrocentric</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(Tiny p-arm - J)</text>
          </g>
          
          <!-- Telocentric -->
          <g transform="translate(600, 50)">
            <path d="M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">Telocentric</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(Centromere at end - I)</text>
          </g>
        </svg>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "सामान्य विज्ञान",
    "parentUrl": "../",
    "current": "कोशिका विज्ञान"
}

hero_hi = {
    "title": "कोशिका विज्ञान",
    "description": "कोशिका संरचनाओं, प्रोकैरियोटिक बनाम यूकैरियोटिक कोशिकाओं, कोशिकांगों (माइटोकॉन्ड्रिया, क्लोरोप्लास्ट, लाइसोसोम), गुणसूत्रों के वर्गीकरण और कोशिका विभाजन (समसूत्री और अर्धसूत्रीविभाजन) की प्रमुख प्रक्रियाओं में महारत हासिल करें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरैक्टिव कोशिका विज्ञान मॉक टेस्ट",
        "description": "कोशिका संरचनाओं, कोशिकांगों, विभाजन के चरणों और ऐतिहासिक खोजों से संबंधित अपने ज्ञान का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "कोशिका विज्ञान में ऐतिहासिक मील के पत्थर",
    "description": "प्रमुख वैज्ञानिक खोजें जिन्होंने कोशिका सिद्धांत और आधुनिक कोशिका विज्ञान की रूपरेखा तैयार की।",
    "cards": [
        {
            "period": "मृत कोशिका की खोज",
            "date": "1665",
            "details": "रॉबर्ट हुक ने आदिम सूक्ष्मदर्शी के तहत कॉर्क के पतले टुकड़ों का अध्ययन किया और 'सेल' (cellula जिसका अर्थ छोटे कमरे हैं) शब्द गढ़ा।"
        },
        {
            "period": "जीवित कोशिका की खोज",
            "date": "1674",
            "details": "एंटोन वैन लीउवेनहोक ने एक उन्नत सूक्ष्मदर्शी के तहत स्वतंत्र रूप से जीवित कोशिकाओं (जीवाणु, प्रोटोजोआ, शुक्राणु, आरबीसी) को देखा और उन्हें 'एनीमलक्यूल्स' (animalcules) कहा।"
        },
        {
            "period": "कोशिका सिद्धांत का प्रस्ताव",
            "date": "1838-1839",
            "details": "एम.जे. श्लाइडेन (वनस्पतिशास्त्री) और थियोडोर श्वान (जंतु वैज्ञानिक) ने प्रस्ताव दिया कि सभी पौधे और जंतु कोशिकाओं से बने हैं, जिससे कोशिका जीवन की मूलभूत इकाई बन गई।"
        },
        {
            "period": "कोशिका वंशानुक्रम अवधारणा",
            "date": "1855",
            "details": "रुडोल्फ विरचो ने एक महत्वपूर्ण तीसरा नियम जोड़ा: 'ओमनिस सेलुला ई सेलुला'—सभी कोशिकाएं पूर्व-मौजूद कोशिकाओं से उत्पन्न होती हैं।"
        },
        {
            "period": "इलेक्ट्रॉन सूक्ष्मदर्शी का आविष्कार",
            "date": "1931",
            "details": "अर्न्स्ट रुस्का और मैक्स नॉल ने पहला इलेक्ट्रॉन सूक्ष्मदर्शी बनाया, जिससे वैज्ञानिकों को कोशिकांगों की सूक्ष्म संरचना देखने में मदद मिली।"
        }
    ]
}

mnemonics_hi = {
    "title": "कोशिका विज्ञान के स्मृति सूत्र (Mnemonics)",
    "description": "कोशिका संरचनाओं और विभाजन के चरणों को आसानी से याद रखने वाले स्मृति सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: समसूत्री विभाजन (Mitosis) के चरण",
            "phrase": "\"I Proposed Men Are Tall (IPMAT)\"",
            "decryption": "कोशिका विभाजन के चरणों के क्रम को याद रखें:<br>• <strong>I</strong>: Interphase (इंटरफेज - तैयारी)<br>• <strong>P</strong>: Prophase (प्रोफेज - गुणसूत्र संघनन)<br>• <strong>M</strong>: Metaphase (मेटाफेज - मध्य में संरेखण)<br>• <strong>A</strong>: Anaphase (एनाफेज - ध्रुवों की ओर खिंचाव)<br>• <strong>T</strong>: Telophase (टीलोफेज - दो नए केंद्रक)"
        },
        {
            "title": "स्मृति सूत्र 2: अर्धसूत्रीविभाजन प्रोफेज I की उप-अवस्थाएं",
            "phrase": "\"Lazy Zebras Play Dual Decisions (LZPDD)\"",
            "decryption": "अर्धसूत्रीविभाजन के प्रोफेज I चरणों को कालानुक्रमिक क्रम में याद रखें:<br>• <strong>L</strong>eptotene (लेप्टोटीन - गुणसूत्र संघनन)<br>• <strong>Z</strong>ygote (जायगोटीन - सूत्रयुग्मन/जोड़ी बनाना)<br>• <strong>P</strong>achytene (पैकीटीन - जीन विनिमय/क्रॉसिंग ओवर)<br>• <strong>D</strong>iplotene (डिप्लोटीन - कयाज्मेटा दिखाई देना)<br>• <strong>D</strong>iakinesis (डायकइनेसिस - केंद्रक झिल्ली का टूटना)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए क्लिक करें और कोशिका विज्ञान की अपनी समझ की जांच करें।",
    "items": [
        {
            "question": "किस कोशिकांग को कोशिका की 'आत्मघाती थैली' (Suicide Bag) कहा जाता है और क्यों?",
            "answer": "<strong>लाइसोसोम</strong>। इनमें शक्तिशाली पाचक एंजाइम (जल-अपघटकीय एंजाइम) होते हैं जो कोशिकीय अपशिष्टों को पचाते हैं। यदि कोशिका क्षतिग्रस्त हो जाती है, तो ये फट सकते हैं और स्वयं कोशिका को पचा सकते हैं।",
            "icon": "fa-skull-crossbones"
        },
        {
            "question": "70S और 80S राइबोसोम में अंतर स्पष्ट करें।",
            "answer": "• <strong>70S राइबोसोम</strong>: प्रोकैरियोट्स, माइटोकॉन्ड्रिया और क्लोरोप्लास्ट में पाए जाते हैं। इनकी उपइकाइयां 50S और 30S हैं।<br>• <strong>80S राइबोसोम</strong>: यूकैरियोट्स के कोशिकाद्रव्य में पाए जाते हैं। इनकी उपइकाइयां 60S और 40S हैं। ('S' स्वेडबर्ग इकाई को दर्शाता है जो अवसादन गुणांक मापती है)।",
            "icon": "fa-microscope"
        },
        {
            "question": "माइटोकॉन्ड्रिया की आंतरिक झिल्ली क्रिस्टी (cristae) के रूप में गहराई से मुड़ी हुई क्यों होती है?",
            "answer": "इलेक्ट्रॉन परिवहन श्रृंखला (ETC) और एटीपी सिंथेस की रासायनिक प्रतिक्रियाओं के लिए उपलब्ध <strong>सतह क्षेत्र को अधिकतम करने के लिए</strong>, जिससे एटीपी का उत्पादन अनुकूलित होता है।",
            "icon": "fa-bolt"
        },
        {
            "question": "जीन विनिमय (Crossing Over) क्या है और यह कब होता है?",
            "answer": "समजात गुणसूत्रों के गैर-सहोदर क्रोमैटिड्स (non-sister chromatids) के बीच आनुवंशिक सामग्री का आदान-प्रदान। यह अर्धसूत्रीविभाजन के प्रोफेज I की <strong>पैकीटीन (Pachytene)</strong> अवस्था में होता है, जो आनुवंशिक विविधता लाता है।",
            "icon": "fa-dna"
        }
    ]
}

traps_hi = {
    "title": "कोशिका विज्ञान परीक्षा के सामान्य भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> विषाणु (Viruses) को कोशिकीय जीव मानना। विषाणु **अकोशिकीय (non-cellular)** होते हैं। इनमें कोशिकीय तंत्र नहीं होता और ये कोशिका सिद्धांत के अपवाद हैं। ये केवल मेजबान कोशिका के भीतर प्रजनन करते हैं।",
        "<strong>भ्रम 2:</strong> पादप और जंतु कोशिकाओं की रिक्तिकाओं (vacuoles) में भ्रम। पादप कोशिकाओं में एक **एकल, विशाल केंद्रीय रिक्तिका** होती है (जो आयतन का 90% तक घेरती है) जो **टोनोप्लास्ट** नामक झिल्ली से घिरी होती है। जंतु कोशिकाओं में कई छोटी, अस्थायी रिक्तिकाएं होती हैं।",
        "<strong>भ्रम 3:</strong> कैरियोटाइप (Karyotype) अध्ययन के चरण में गलती। गुणसूत्रों का अध्ययन, गणना और छायाचित्रण करने के लिए **मेटाफेज** सबसे अच्छा चरण है क्योंकि इस समय वे अधिकतम संघनित होते हैं और मध्य रेखा (equator) पर संरेखित होते हैं। इसे एनाफेज (जहां वे अलग खिंचते हैं) से भ्रमित न करें।",
        "<strong>भ्रम 4:</strong> सभी यूकैरियोटिक कोशिकाओं में केंद्रक की उपस्थिति मानना। परिपक्व स्तनधारी **लाल रक्त कोशिकाएं (RBCs)** और पौधों की **चालनी नलिका कोशिकाएं (sieve tubes)** **केंद्रक रहित (enucleated)** होती हैं ताकि परिवहन दक्षता को अनुकूलित किया जा सके।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. कोशिका सिद्धांत, प्रोकैरियोटिक बनाम यूकैरियोटिक कोशिकाएं और कोशिका भित्ति",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>कोशिका सिद्धांत (Cell Theory):</strong> श्लाइडेन और श्वान (1839) द्वारा प्रस्तावित, रुडोल्फ विरचो (1855) द्वारा संशोधित। सिद्धांत के मुख्य बिंदु: (1) सभी जीवित जीव कोशिकाओं से बने हैं। (2) कोशिका जीवन की संरचनात्मक और कार्यात्मक इकाई है। (3) सभी कोशिकाएं पूर्व-मौजूद कोशिकाओं से उत्पन्न होती हैं। <strong>अपवाद:</strong> विषाणु (Viruses), वाइरॉइड्स, प्रीयॉन्स (इनमें प्रोटोप्लाज्म या कोशिकीय संरचना नहीं होती)।</li>
          <li style="margin-bottom: 0.75rem;"><strong>प्रोकैरियोटिक बनाम यूकैरियोटिक कोशिकाएं:</strong>
            <br>• <strong>प्रोकैरियोट्स:</strong> कोई स्पष्ट केंद्रक झिल्ली नहीं (नग्न डीएनए केंद्रकाभ या nucleoid क्षेत्र में होता है)। दोहरी झिल्ली वाले कोशिकांग अनुपस्थित होते हैं। राइबोसोम 70S प्रकार के होते हैं। कोशिका भित्ति में पेप्टिडोग्लाइकन होता है (जीवाणु में)। उदाहरण: जीवाणु, नील-हरित शैवाल (सायनोबैक्टीरिया), माइकोप्लाज्मा (PPLO - सबसे छोटी जीवित कोशिका, कोशिका भित्ति रहित)।
            <br>• <strong>यूकैरियोट्स:</strong> स्पष्ट केंद्रक झिल्ली युक्त सुव्यवस्थित केंद्रक। दोहरी झिल्ली वाले कोशिकांग (माइटोकॉन्ड्रिया, लवक) उपस्थित होते हैं। राइबोसोम 80S (कोशिकाद्रव्य में) और 70S (कोशिकांगों में) होते हैं। उदाहरण: प्रोटिस्टा, कवक, पौधे, जंतु।
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>कोशिका भित्ति और कोशिका झिल्ली:</strong>
            <br>• <strong>कोशिका भित्ति:</strong> कठोर, पूरी तरह से पारगम्य, निर्जीव बाहरी परत। पौधों (सेलुलोज), कवक (काइटिन), जीवाणु (पेप्टिडोग्लाइकन) में पाई जाती है। जंतुओं में अनुपस्थित होती है।
            <br>• <strong>कोशिका झिल्ली:</strong> अर्ध-पारगम्य, सजीव, लिपिड और प्रोटीन से बनी द्विलायर संरचना। इसे <strong>फ्लुइड मोज़ेक मॉडल</strong> (सिंगर और निकोलसन, 1972) द्वारा समझाया गया है।
          </li>
        </ul>
        
        <!-- SVG Diagram 1: Prokaryote vs Eukaryote -->
        <svg viewBox="0 0 800 280" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .border-line { fill: none; stroke: var(--text-dark, #2c3e50); stroke-width: 2px; }
            .prok-bg { fill: rgba(230, 126, 34, 0.08); stroke: #d35400; stroke-width: 2; rx: 12px;}
            .euk-bg { fill: rgba(52, 152, 219, 0.08); stroke: #2980b9; stroke-width: 2; rx: 12px;}
            .inner-cell { fill: rgba(46, 204, 113, 0.15); stroke: #27ae60; stroke-width: 1.5; }
            .nucleoid { fill: none; stroke: #c0392b; stroke-width: 1.5; stroke-dasharray: 2; }
            .organelle { fill: #9b59b6; stroke: #8e44ad; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            .label-head { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--primary, #8e44ad); font-size: 14px; }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .border-line { stroke: #cbd5e1; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">प्रोकैरियोटिक कोशिका (बाएं) बनाम यूकैरियोटिक कोशिका (दाएं)</text>
          
          <!-- Prokaryotic Cell -->
          <g transform="translate(60, 50)">
            <rect x="0" y="0" width="300" height="190" class="prok-bg" />
            <text x="150" y="25" class="label-head" fill="#d35400" text-anchor="middle">प्रोकैरियोट (जैसे, जीवाणु)</text>
            <path d="M 40 100 Q 80 140 120 90 T 260 110" class="nucleoid" />
            <text x="150" y="85" class="annot-text" fill="#c0392b" font-weight="bold" text-anchor="middle">नग्न डीएनए (केंद्राभ)</text>
            <circle cx="50" cy="150" r="2" fill="#2c3e50" />
            <circle cx="80" cy="160" r="2" fill="#2c3e50" />
            <circle cx="210" cy="150" r="2" fill="#2c3e50" />
            <text x="130" y="170" class="annot-text" text-anchor="middle">70S राइबोसोम</text>
            <text x="150" y="145" class="annot-text" text-anchor="middle">झिल्लीदार कोशिकांग अनुपस्थित</text>
          </g>
          
          <!-- Eukaryotic Cell -->
          <g transform="translate(440, 50)">
            <rect x="0" y="0" width="300" height="190" class="euk-bg" />
            <text x="150" y="25" class="label-head" fill="#2980b9" text-anchor="middle">यूकैरियोट (पादप/जंतु)</text>
            <circle cx="150" cy="110" r="30" class="inner-cell" />
            <circle cx="150" cy="110" r="10" fill="#27ae60" />
            <text x="150" y="70" class="annot-text" fill="#27ae60" font-weight="bold" text-anchor="middle">सत्य केंद्रक</text>
            
            <rect x="50" y="70" width="30" height="15" rx="3" class="organelle" />
            <text x="65" y="100" class="annot-text" text-anchor="middle">माइटोकॉन्ड्रिया</text>
            
            <circle cx="240" cy="120" r="3" fill="#2c3e50" />
            <circle cx="250" cy="130" r="3" fill="#2c3e50" />
            <text x="240" y="155" class="annot-text" text-anchor="middle">80S राइबोसोम</text>
            <text x="150" y="170" class="annot-text" text-anchor="middle">झिल्लीदार कोशिकांग उपस्थित</text>
          </g>
        </svg>"""
    },
    {
        "title": "2. कोशिकांगों की संरचना एवं कार्य (माइटोकॉन्ड्रिया, लवक, लाइसोसोम)",
        "content": """<p>यूकैरियोटिक कोशिकाओं में विशिष्ट उप-कोशिकीय घटक होते हैं जिन्हें कोशिकांग (organelles) कहा जाता है। प्रतियोगी परीक्षाओं में इनकी भूमिकाएँ और विशेषताएँ अत्यधिक पूछी जाती हैं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>कोशिकांग</th>
                <th>झिल्ली की स्थिति</th>
                <th>प्रमुख खोजकर्ता / शब्द</th>
                <th>मुख्य कार्य और परीक्षा संकेत</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>माइटोकॉन्ड्रिया</strong></td>
                <td>दोहरी झिल्ली</td>
                <td>कोलिकर (खोज), बेंडा (नामकरण)</td>
                <td><strong>कोशिका का पावरहाउस</strong>: वायवीय श्वसन का स्थल (क्रेब्स चक्र, इलेक्ट्रॉन परिवहन)। <strong>एटीपी</strong> का संश्लेषण करता है। इसमें गोलाकार डीएनए और 70S राइबोसोम होते हैं (अर्ध-स्वायत्त)। यह मातृ वंशागति (maternal inheritance) को दर्शाता है।</td>
              </tr>
              <tr>
                <td><strong>लवक (Plastids)</strong></td>
                <td>दोहरी झिल्ली</td>
                <td>शिम्पर (क्लोरोप्लास्ट शब्द)</td>
                <td><strong>कोशिका की रसोई</strong>: पौधों में पाए जाते हैं। क्लोरोफिल वर्णक होता है। प्रकाश संश्लेषण का स्थल (<strong>थायलाकोइड/ग्रेना</strong> में प्रकाश अभिक्रिया; <strong>स्ट्रोमा</strong> में अप्रकाशिक अभिक्रिया)। अर्ध-स्वायत्त (स्वयं का डीएनए/70S राइबोसोम)।</td>
              </tr>
              <tr>
                <td><strong>राइबोसोम</strong></td>
                <td>झिल्ली रहित</td>
                <td>जॉर्ज पेलेड (खोज)</td>
                <td><strong>प्रोटीन कारखाना</strong>: आरएनए (rRNA) और प्रोटीन से बने होते हैं। प्रोटीन संश्लेषण का मुख्य स्थल। सबसे छोटा कोशिकांग। कोशिकाद्रव्य में मुक्त या खुरदुरी अंतःप्रद्रव्यी जालिका (RER) से बंधे होते हैं।</td>
              </tr>
              <tr>
                <td><strong>लाइसोसोम</strong></td>
                <td>एकल झिल्ली</td>
                <td>क्रिश्चियन डी ड्यूव</td>
                <td><strong>आत्मघाती थैली</strong>: जल-अपघटकीय एंजाइमों (pH ~5 पर सक्रिय) से भरपूर। स्व-भक्षण (Autophagy), कोशिकीय मलबे की सफाई, और रोगग्रस्त अवस्था में कोशिका को पचाना।</td>
              </tr>
              <tr>
                <td><strong>अंतःप्रद्रव्यी जालिका (ER)</strong></td>
                <td>एकल झिल्ली</td>
                <td>पोर्टर, क्लाउड और फुलम</td>
                <td><strong>खुरदुरी ER (RER):</strong> राइबोसोम युक्त; प्रोटीन संश्लेषण/परिवहन। <br><strong>चिकनी ER (SER):</strong> राइबोसोम रहित; लिपिड/स्टेरॉयड हार्मोन संश्लेषण और यकृत में विषाक्त पदार्थों का विषहरण।</td>
              </tr>
              <tr>
                <td><strong>गोल्जी उपकरण</strong></td>
                <td>एकल झिल्ली</td>
                <td>कैमिलो गोल्जी</td>
                <td><strong>कोशिकीय यातायात का निदेशक</strong>: प्रोटीनों और लिपिडों की पैकेजिंग, छंटाई और रासायनिक संशोधन। ग्लाइकोप्रोटीन और ग्लाइकोलिपिड निर्माण का स्थल। लाइसोसोम के निर्माण में सहायक।</td>
              </tr>
              <tr>
                <td><strong>केंद्रक (Nucleus)</strong></td>
                <td>दोहरी झिल्ली</td>
                <td>रॉबर्ट ब्राउन (1831)</td>
                <td><strong>कोशिका का मस्तिष्क</strong>: आनुवंशिक सामग्री (डीएनए/क्रोमेटिन) रखता है। <strong>केंद्रिका (nucleolus)</strong> का घर (सक्रिय rRNA संश्लेषण और राइबोसोम निर्माण स्थल)। छिद्रयुक्त केंद्रक झिल्ली से घिरा होता है।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. गुणसूत्रों का वर्गीकरण और कोशिका विभाजन (समसूत्री बनाम अर्धसूत्रीविभाजन)",
        "content": """<ul style="padding-left: 1.25rem; line-height: 1.7; margin-bottom: 1.5rem;">
          <li style="margin-bottom: 0.75rem;"><strong>गुणसूत्र संरचना और सेंट्रोमियर वर्गीकरण:</strong> गुणसूत्र क्रोमेटिन (डीएनए + हिस्टोन प्रोटीन) से बने धागे जैसी संरचनाएं हैं। सेंट्रोमियर (प्राथमिक संकीर्णन) की स्थिति के आधार पर, इन्हें वर्गीकृत किया जाता है:
            <br>• <strong>मध्यकेंद्री (Metacentric):</strong> सेंट्रोमियर बिल्कुल बीच में होता है; दो समान भुजाएं बनाता है (एनाफेज में V-आकार)।
            <br>• <strong>उप-मध्यकेंद्री (Sub-metacentric):</strong> सेंट्रोमियर केंद्र से थोड़ा दूर होता है; एक भुजा थोड़ी छोटी होती है (एनाफेज में L-आकार)।
            <br>• <strong>अग्रकेंद्री (Acrocentric):</strong> सेंट्रोमियर एक छोर के बहुत पास होता है; एक भुजा बहुत छोटी और दूसरी बहुत लंबी होती है (एनाफेज में J-आकार)।
            <br>• <strong>अंतकेंद्री (Telocentric):</strong> सेंट्रोमियर बिल्कुल अंतिम छोर पर होता है; केवल एक भुजा होती है (एनाफेज में I-आकार / छड़-आकार)।
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>समसूत्री विभाजन (Mitosis):</strong> कायिक (somatic) कोशिकाओं में होता है। इसके परिणामस्वरूप दो समान द्विगुणित (2n) संतति कोशिकाएं बनती हैं।
            <br>• **प्रोफेज (Prophase):** क्रोमेटिन गुणसूत्रों में संघनित होता है; तर्कु तंतु बनते हैं; केंद्रिका और केंद्रक झिल्ली विलुप्त हो जाते हैं।
            <br>• **मेटाफेज (Metaphase):** गुणसूत्र कोशिका के मध्य (equator) में संरेखित होते हैं। कैरियोटाइप विश्लेषण के लिए इसका अध्ययन किया जाता है।
            <br>• **एनाफेज (Anaphase):** सिस्टर क्रोमैटिड्स सेंट्रोमियर पर विभाजित होते हैं और विपरीत ध्रुवों की ओर खिंचते हैं (सबसे छोटा चरण)।
            <br>• **टीलोफेज (Telophase):** गुणसूत्रों के दो समूहों के चारों ओर केंद्रक झिल्ली पुनः बन जाती है; गुणसूत्र फिर से फैल जाते हैं।
          </li>
          <li style="margin-bottom: 0.75rem;"><strong>अर्धसूत्रीविभाजन (Meiosis):</strong> जनन (germ/reproductive) कोशिकाओं में होता है। यह चार अगुणित (n) युग्मक बनाने के लिए गुणसूत्रों की संख्या को आधा कर देता है। इसमें अर्धसूत्री I (न्यूनकारी) और अर्धसूत्री II (समकारी) शामिल हैं।
            <br>• **प्रोफेज I (अत्यधिक पूछे जाने वाले उप-चरण):**
            <br>&nbsp;&nbsp;1. <em>लेप्टोटीन:</em> क्रोमेटिन धागे संघनित होने लगते हैं।
            <br>&nbsp;&nbsp;2. <em>जायगोटीन:</em> समजात गुणसूत्रों की जोड़ी बनना (**सूत्रयुग्मन या Synapsis**) होता है, जिससे द्वियुजी (bivalent) बनते हैं।
            <br>&nbsp;&nbsp;3. <em>पैकीटीन:</em> समजात गुणसूत्रों के गैर-सहोदर क्रोमैटिड्स के बीच आनुवंशिक सामग्री का आदान-प्रदान (**जीन विनिमय या Crossing over**) होता है जो रिकॉम्बिनेज एंजाइम द्वारा संचालित होता है।
            <br>&nbsp;&nbsp;4. <em>डिप्लोटीन:</em> समजात गुणसूत्र अलग होने लगते हैं लेकिन **कयाज्मेटा (Chiasmata)** नामक बिंदुओं पर जुड़े रहते हैं।
            <br>&nbsp;&nbsp;5. <em>डायकइनेसिस:</em> कयाज्मेटा का सिरों की ओर विस्थापन (terminalization) होता है; केंद्रक झिल्ली विघटित हो जाती है।
          </li>
        </ul>
        
        <!-- SVG Diagram 2: Chromosome Anatomy -->
        <svg viewBox="0 0 800 220" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card, #ffffff); padding: 10px; border: 1px solid rgba(128, 128, 128, 0.15);">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: 700; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .chrom-arm { fill: rgba(155, 89, 182, 0.2); stroke: #8e44ad; stroke-width: 2; }
            .centromere { fill: #e74c3c; stroke: #c0392b; stroke-width: 1.5; }
            .annot-text { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            body.dark-mode .svg-title { fill: #f1f5f9; }
            body.dark-mode .annot-text { fill: #e2e8f0; }
          </style>
          <text x="20" y="30" class="svg-title">सेंट्रोमियर की स्थिति के आधार पर गुणसूत्रों के प्रकार</text>
          
          <!-- Metacentric -->
          <g transform="translate(60, 50)">
            <path d="M 40 10 L 40 70 M 60 10 L 60 70 M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">मध्यकेंद्री (Metacentric)</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(समान भुजाएँ - V)</text>
          </g>
          
          <!-- Sub-metacentric -->
          <g transform="translate(240, 50)">
            <path d="M 40 30 L 40 70 M 60 30 L 60 70 M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">उप-मध्यकेंद्री (Sub-metacentric)</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(छोटी p-भुजा - L)</text>
          </g>
          
          <!-- Acrocentric -->
          <g transform="translate(420, 50)">
            <path d="M 40 50 L 40 70 M 60 50 L 60 70 M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">अग्रकेंद्री (Acrocentric)</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(अतिसूक्ष्म p-भुजा - J)</text>
          </g>
          
          <!-- Telocentric -->
          <g transform="translate(600, 50)">
            <path d="M 40 85 L 40 145 M 60 85 L 60 145" class="chrom-arm" stroke-linecap="round" />
            <circle cx="50" cy="77.5" r="10" class="centromere" />
            <text x="50" y="165" class="annot-text" font-weight="bold" text-anchor="middle">अंतकेंद्री (Telocentric)</text>
            <text x="50" y="180" class="annot-text" text-anchor="middle">(अंत में सेंट्रोमियर - I)</text>
          </g>
        </svg>"""
    }
]

# ----------------- 50 PRACTICE QUESTIONS (BILINGUAL) -----------------
practice_questions = [
    {
        "q": "Who coined the term 'Cell' after observing thin sections of cork?",
        "q_hi": "कॉर्क के पतले टुकड़ों का अवलोकन करने के बाद 'सेल' (कोशिका) शब्द किसने गढ़ा था?",
        "opts": ["Robert Brown", "Robert Hooke", "Anton van Leeuwenhoek", "Theodore Schwann"],
        "opts_hi": ["रॉबर्ट ब्राउन", "रॉबर्ट हुक", "एंटोन वैन लीउवेनहोक", "थियोडोर श्वान"],
        "ans": 1,
        "sol": "Robert Hooke coined the term 'Cell' in 1665 in his book Micrographia after observing dead cell walls of cork under a primitive microscope.",
        "sol_hi": "रॉबर्ट हुक ने 1665 में अपनी पुस्तक 'माइक्रोग्राफिया' में कॉर्क की मृत कोशिकाओं की दीवारों को देखकर 'सेल' शब्द गढ़ा था।"
    },
    {
        "q": "The concept 'Omnis cellula e cellula' (All cells arise from pre-existing cells) was proposed by:",
        "q_hi": "'ओमनिस सेलुला ई सेलुला' (सभी कोशिकाएं पूर्व-मौजूद कोशिकाओं से उत्पन्न होती हैं) की अवधारणा किसके द्वारा प्रस्तावित की गई थी?",
        "opts": ["Matthias Schleiden", "Theodore Schwann", "Rudolf Virchow", "Louis Pasteur"],
        "opts_hi": ["मैथियास श्लाइडेन", "थियोडोर श्वान", "रुडोल्फ विरचो", "लुई पाश्चर"],
        "ans": 2,
        "sol": "Rudolf Virchow proposed the cell lineage concept ('Omnis cellula e cellula') in 1855, modifying the original cell theory of Schleiden and Schwann.",
        "sol_hi": "रुडोल्फ विरचो ने 1855 में कोशिका वंशानुक्रम अवधारणा ('ओमनिस सेलुला ई सेलुला') का प्रस्ताव दिया, जिसने श्लाइडेन और श्वान के मूल कोशिका सिद्धांत को संशोधित किया।"
    },
    {
        "q": "Which of the following is an exception to the Cell Theory?",
        "q_hi": "निम्नलिखित में से कौन सा कोशिका सिद्धांत का अपवाद है?",
        "opts": ["Bacteria", "Fungi", "Viruses", "Algae"],
        "opts_hi": ["जीवाणु", "कवक", "विषाणु (Viruses)", "शैवाल"],
        "ans": 2,
        "sol": "Viruses are acellular/non-cellular entities that lack a protoplasm and cellular machinery. They behave as non-living matter outside host cells and living matter inside them.",
        "sol_hi": "विषाणु (Viruses) अकोशिकीय होते हैं जिनमें प्रोटोप्लाज्म और कोशिकीय मशीनरी का अभाव होता है। वे मेजबान कोशिकाओं के बाहर निर्जीव और भीतर सजीव के रूप में व्यवहार करते हैं।"
    },
    {
        "q": "Which of the following organisms lacks a cell wall?",
        "q_hi": "निम्नलिखित में से किस जीव में कोशिका भित्ति का अभाव होता है?",
        "opts": ["Mycoplasma", "Cyanobacteria", "Fungi", "Green Algae"],
        "opts_hi": ["माइकोप्लाज्मा (Mycoplasma)", "सायनोबैक्टीरिया", "कवक", "हरे शैवाल"],
        "ans": 0,
        "sol": "Mycoplasma (PPLO) is the smallest known living cell and lacks a cell wall. Due to this, they are pleomorphic (can change shape) and are naturally resistant to antibiotics like penicillin that target cell wall synthesis.",
        "sol_hi": "माइकोप्लाज्मा (PPLO) सबसे छोटा ज्ञात जीवित जीव है जिसमें कोशिका भित्ति का अभाव होता है। इसके कारण वे बहुरूपी (आकार बदल सकते हैं) होते हैं और पेनिसिलिन जैसे एंटीबायोटिक दवाओं के प्रति प्रतिरोधी होते हैं।"
    },
    {
        "q": "Which of the following organelles is double membrane-bound?",
        "q_hi": "निम्नलिखित में से कौन सा कोशिकांग दोहरी झिल्ली से घिरा होता है?",
        "opts": ["Lysosome", "Ribosome", "Mitochondria", "Golgi Apparatus"],
        "opts_hi": ["लाइसोसोम", "राइबोसोम", "माइटोकॉन्ड्रिया", "गोल्जी उपकरण"],
        "ans": 2,
        "sol": "Mitochondria and Plastids (like Chloroplasts) are double membrane-bound organelles. Lysosomes and Golgi bodies are single-membrane bound, while Ribosomes lack a membrane entirely.",
        "sol_hi": "माइटोकॉन्ड्रिया और लवक (जैसे क्लोरोप्लास्ट) दोहरी झिल्ली से घिरे कोशिकांग हैं। लाइसोसोम और गोल्जी उपकरण एकल-झिल्ली से घिरे होते हैं, जबकि राइबोसोम में झिल्ली नहीं होती है।"
    },
    {
        "q": "The primary component of a plant cell wall is:",
        "q_hi": "पादप कोशिका भित्ति का प्राथमिक घटक क्या है?",
        "opts": ["Chitin", "Peptidoglycan", "Cellulose", "Phospholipids"],
        "opts_hi": ["काइटिन", "पेप्टिडोग्लाइकन", "सेलुलोज (Cellulose)", "फास्फोलिपिड्स"],
        "ans": 2,
        "sol": "Plant cell walls are primarily composed of Cellulose, a polysaccharide. Fungi walls contain Chitin, bacterial walls contain Peptidoglycan, and animal cells lack walls but have a Phospholipid bilayer membrane.",
        "sol_hi": "पादप कोशिका भित्तियाँ मुख्य रूप से सेलुलोज (एक पॉलीसेकेराइड) से बनी होती हैं। कवक की दीवारों में काइटिन, जीवाणु की दीवारों में पेप्टिडोग्लाइकन होता है, और जंतु कोशिकाओं में भित्ति नहीं होती।"
    },
    {
        "q": "Which organelle is referred to as the 'Powerhouse of the Cell'?",
        "q_hi": "किस कोशिकांग को 'कोशिका का पावरहाउस' कहा जाता है?",
        "opts": ["Chloroplast", "Golgi Apparatus", "Mitochondria", "Ribosome"],
        "opts_hi": ["क्लोरोप्लास्ट", "गोल्जी उपकरण", "माइटोकॉन्ड्रिया", "राइबोसोम"],
        "ans": 2,
        "sol": "Mitochondria are the powerhouses of the cell because they oxidize carbohydrates and fats to generate cellular energy in the form of ATP (Adenosine Triphosphate).",
        "sol_hi": "माइटोकॉन्ड्रिया को कोशिका का पावरहाउस कहा जाता है क्योंकि वे कार्बोहाइड्रेट और वसा का ऑक्सीकरण करके एटीपी (ATP) के रूप में कोशिकीय ऊर्जा उत्पन्न करते हैं।"
    },
    {
        "q": "Which organelle contains hydrolytic enzymes and is known as the 'Suicidal Bag'?",
        "q_hi": "किस कोशिकांग में जल-अपघटकीय एंजाइम होते हैं और उसे 'आत्मघाती थैली' कहा जाता है?",
        "opts": ["Lysosome", "Centrosome", "Vacuole", "Peroxisome"],
        "opts_hi": ["लाइसोसोम", "तारककाय (Centrosome)", "रिक्तिका (Vacuole)", "परऑक्सीसोम"],
        "ans": 0,
        "sol": "Lysosomes contain acidic hydrolytic enzymes (active at pH ~5.0) which can digest macromolecules, cell debris, or the entire damaged cell itself during autolysis.",
        "sol_hi": "लाइसोसोम में अम्लीय जल-अपघटकीय एंजाइम होते हैं जो मैक्रोमोलेक्यूल्स, कोशिकीय मलबे या ऑटोलाइज़िस के दौरान क्षतिग्रस्त कोशिका को पचा सकते हैं।"
    },
    {
        "q": "The site of ribosomal RNA (rRNA) synthesis inside the eukaryotic cell is the:",
        "q_hi": "यूकैरियोटिक कोशिका के भीतर राइबोसोमल आरएनए (rRNA) संश्लेषण का स्थल कौन सा है?",
        "opts": ["Cytoplasm", "Nucleolus", "Golgi Body", "Rough Endoplasmic Reticulum"],
        "opts_hi": ["कोशिकाद्रव्य", "केंद्रिका (Nucleolus)", "गोल्जी काय", "खुरदुरी अंतःप्रद्रव्यी जालिका"],
        "ans": 1,
        "sol": "The nucleolus is a dense, non-membranous sub-compartment within the nucleus responsible for the transcription of rRNA and assembly of ribosomal subunits.",
        "sol_hi": "केंद्रिका (nucleolus) केंद्रक के भीतर एक सघन, झिल्ली रहित उप-भाग है जो rRNA के प्रतिलेखन और राइबोसोम की उप-इकाइयों के संयोजन के लिए जिम्मेदार है।"
    },
    {
        "q": "Fluid Mosaic Model of the cell membrane was proposed by:",
        "q_hi": "कोशिका झिल्ली का 'फ्लुइड मोज़ेक मॉडल' किसके द्वारा प्रस्तावित किया गया था?",
        "opts": ["Watson and Crick", "Singer and Nicolson", "Schleiden and Schwann", "Robert Hooke"],
        "opts_hi": ["वाटसन और क्रिक", "सिंगर और निकोलसन", "श्लाइडेन और श्वान", "रॉबर्ट हुक"],
        "ans": 1,
        "sol": "Jonathan Singer and Garth Nicolson proposed the Fluid Mosaic Model in 1972, describing the cell membrane as a mosaic of proteins floating in a fluid phospholipid bilayer.",
        "sol_hi": "जोनाथन सिंगर और गार्थ निकोलसन ने 1972 में 'फ्लुइड मोज़ेक मॉडल' का प्रस्ताव दिया था, जिसमें कोशिका झिल्ली को तरल फॉस्फोलिपिड द्विलायर में तैरते हुए प्रोटीनों के मोज़ेक के रूप में वर्णित किया गया था।"
    },
    {
        "q": "Which of the following organelles is semi-autonomous and contains circular DNA and 70S ribosomes?",
        "q_hi": "निम्नलिखित में से कौन सा कोशिकांग अर्ध-स्वायत्त है और उसमें गोलाकार डीएनए और 70S राइबोसोम होते हैं?",
        "opts": ["Lysosome", "Mitochondria", "Golgi Apparatus", "Endoplasmic Reticulum"],
        "opts_hi": ["लाइसोसोम", "माइटोकॉन्ड्रिया", "गोल्जी उपकरण", "अंतःप्रद्रव्यी जालिका"],
        "ans": 1,
        "sol": "Mitochondria and Chloroplasts are semi-autonomous organelles because they possess their own genetic machinery (circular DNA and 70S ribosomes) and can synthesize some of their own proteins.",
        "sol_hi": "माइटोकॉन्ड्रिया और क्लोरोप्लास्ट अर्ध-स्वायत्त कोशिकांग हैं क्योंकि उनके पास अपनी आनुवंशिक मशीनरी (गोलाकार डीएनए और 70S राइबोसोम) होती है और वे अपने स्वयं के कुछ प्रोटीन संश्लेषित कर सकते हैं।"
    },
    {
        "q": "Ribosomes are composed of:",
        "q_hi": "राइबोसोम किससे बने होते हैं?",
        "opts": ["DNA and Proteins", "RNA and Proteins", "Lipids and Proteins", "RNA and Lipids"],
        "opts_hi": ["डीएनए और प्रोटीन", "आरएनए (RNA) और प्रोटीन", "लिपिड और प्रोटीन", "आरएनए और लिपिड"],
        "ans": 1,
        "sol": "Ribosomes are ribonucleoprotein particles composed of Ribosomal RNA (rRNA) and proteins. They lack any lipid membrane wrapper.",
        "sol_hi": "राइबोसोम राइबोन्यूक्लियोप्रोटीन कण होते हैं जो राइबोसोमल आरएनए (rRNA) और प्रोटीन से बने होते हैं। इनमें कोई लिपिड झिल्ली नहीं होती है।"
    },
    {
        "q": "In which stage of cell division can the morphology of chromosomes be studied most clearly?",
        "q_hi": "कोशिका विभाजन के किस चरण में गुणसूत्रों की आकारिकी (morphology) का सबसे स्पष्ट रूप से अध्ययन किया जा सकता है?",
        "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "opts_hi": ["प्रोफेज", "मेटाफेज", "एनाफेज", "टीलोफेज"],
        "ans": 1,
        "sol": "During Metaphase, chromosomes are maximally condensed, clearly visible, and aligned at the equatorial plate, making it the ideal stage for karyotype studies.",
        "sol_hi": "मेटाफेज के दौरान, गुणसूत्र अधिकतम संघनित और स्पष्ट रूप से दिखाई देते हैं तथा भूमध्यरेखीय प्लेट पर संरेखित होते हैं, जिससे यह कैरियोटाइप अध्ययनों के लिए आदर्श चरण बन जाता है।"
    },
    {
        "q": "During cell division, spindle fibers attach to which part of the chromosome?",
        "q_hi": "कोशिका विभाजन के दौरान, तर्कु तंतु (spindle fibers) गुणसूत्र के किस भाग से जुड़ते हैं?",
        "opts": ["Telomere", "Chromomere", "Kinetochore", "Nucleolar Organizer"],
        "opts_hi": ["टीलोमीयर", "क्रोमोमीयर", "काइनेटोकोर (Kinetochore)", "केंद्रिकीय आयोजक"],
        "ans": 2,
        "sol": "Spindle fibers attach to the kinetochores, which are disc-shaped protein complexes assembled on the centromere region of each chromosome.",
        "sol_hi": "तर्कु तंतु काइनेटोकोर (kinetochores) से जुड़ते हैं, जो प्रत्येक गुणसूत्र के सेंट्रोमियर क्षेत्र पर इकट्ठे डिस्क के आकार के प्रोटीन कॉम्प्लेक्स होते हैं।"
    },
    {
        "q": "Crossing over, which leads to genetic recombination in eukaryotes, occurs during which stage of Meiosis?",
        "q_hi": "जीन विनिमय (Crossing over), जो यूकैरियोट्स में आनुवंशिक पुनर्संयोजन की ओर ले जाता है, अर्धसूत्रीविभाजन के किस चरण के दौरान होता है?",
        "opts": ["Zygotene", "Pachytene", "Diplotene", "Diakinesis"],
        "opts_hi": ["जायगोटीन", "पैकीटीन (Pachytene)", "डिप्लोटीन", "डायकइनेसिस"],
        "ans": 1,
        "sol": "Crossing over occurs during the Pachytene stage of Prophase I in Meiosis I. Homologous chromosomes swap segments of non-sister chromatids.",
        "sol_hi": "जीन विनिमय (Crossing over) अर्धसूत्रीविभाजन I के प्रोफेज I की पैकीटीन (Pachytene) अवस्था के दौरान होता है, जिसमें समजात गुणसूत्रों के गैर-सहोदर क्रोमैटिड्स आपस में आनुवंशिक सामग्री बदलते हैं।"
    },
    {
        "q": "The pairing of homologous chromosomes during zygotene is called:",
        "q_hi": "जायगोटीन के दौरान समजात गुणसूत्रों के युग्मन (जोड़ी बनाने) को क्या कहा जाता है?",
        "opts": ["Synapsis", "Chiasmata", "Recombination", "Terminalization"],
        "opts_hi": ["सूत्रयुग्मन (Synapsis)", "कयाज्मेटा", "पुनर्संयोजन", "उपांतीकरण"],
        "ans": 0,
        "sol": "Synapsis is the pairing of homologous maternal and paternal chromosomes during the Zygotene stage of Prophase I in Meiosis. It forms a structure called a bivalent or tetrad.",
        "sol_hi": "सूत्रयुग्मन (Synapsis) अर्धसूत्रीविभाजन के प्रोफेज I के जायगोटीन चरण के दौरान समजात मातृ और पितृ गुणसूत्रों का युग्मन है। यह एक द्वियुजी (bivalent) संरचना बनाता है।"
    },
    {
        "q": "Which chromosome type has its centromere at the terminal end, possessing only one arm?",
        "q_hi": "किस प्रकार के गुणसूत्र का सेंट्रोमियर बिल्कुल अंतिम छोर पर होता है, जिसके पास केवल एक ही भुजा होती है?",
        "opts": ["Metacentric", "Sub-metacentric", "Acrocentric", "Telocentric"],
        "opts_hi": ["मध्यकेंद्री", "उप-मध्यकेंद्री", "अग्रकेंद्री", "अंतकेंद्री (Telocentric)"],
        "ans": 3,
        "sol": "Telocentric chromosomes have the centromere at the very end of the chromosome, giving them a rod-like appearance (I-shape) during anaphase. Humans do not have telocentric chromosomes.",
        "sol_hi": "अंतकेंद्री (Telocentric) गुणसूत्रों में सेंट्रोमियर गुणसूत्र के अंतिम छोर पर होता है, जिससे वे एनाफेज के दौरान छड़ जैसे (I-आकार) दिखते हैं। मनुष्यों में अंतकेंद्री गुणसूत्र नहीं होते।"
    },
    {
        "q": "The membrane that bounds the central vacuole of a plant cell is called:",
        "q_hi": "पादप कोशिका की केंद्रीय रिक्तिका को घेरने वाली झिल्ली को क्या कहा जाता है?",
        "opts": ["Plasma membrane", "Tonoplast", "Cell wall", "Amyloplast"],
        "opts_hi": ["प्लाज्मा झिल्ली", "टोनोप्लास्ट (Tonoplast)", "कोशिका भित्ति", "एमाइलोप्लास्ट"],
        "ans": 1,
        "sol": "The tonoplast is the single membrane that delimits the large central vacuole in plant cells, regulating the movement of ions and materials into the vacuole.",
        "sol_hi": "टोनोप्लास्ट वह एकल झिल्ली है जो पादप कोशिकाओं में बड़ी केंद्रीय रिक्तिका को घेरे रहती है और आयनों के आवागमन को नियंत्रित करती है।"
    },
    {
        "q": "The organelle responsible for lipid synthesis and detoxification of drugs in the liver is:",
        "q_hi": "यकृत में लिपिड संश्लेषण और दवाओं के विषहरण (detoxification) के लिए जिम्मेदार कोशिकांग है:",
        "opts": ["Rough Endoplasmic Reticulum", "Smooth Endoplasmic Reticulum", "Golgi Apparatus", "Lysosome"],
        "opts_hi": ["खुरदुरी अंतःप्रद्रव्यी जालिका", "चिकनी अंतःप्रद्रव्यी जालिका (SER)", "गोल्जी उपकरण", "लाइसोसोम"],
        "ans": 1,
        "sol": "Smooth Endoplasmic Reticulum (SER) is devoid of ribosomes. It is specialized for lipid and steroid synthesis, carbohydrate metabolism, and drug detoxification (specifically in hepatocytes/liver cells).",
        "sol_hi": "चिकनी अंतःप्रद्रव्यी जालिका (SER) में राइबोसोम नहीं होते। यह लिपिड संश्लेषण, कार्बोहाइड्रेट चयापचय और दवाओं के विषहरण (विशेष रूप से यकृत कोशिकाओं में) के लिए विशिष्ट है।"
    },
    {
        "q": "Which cell organelle is active in the package and dispatch of proteins and glycoproteins?",
        "q_hi": "प्रोटीनों और ग्लाइकोप्रोटीनों की पैकेजिंग तथा उनके प्रेषण (dispatch) में कौन सा कोशिकांग सक्रिय होता है?",
        "opts": ["Golgi Apparatus", "Mitochondria", "Lysosome", "Centriole"],
        "opts_hi": ["गोल्जी उपकरण (Golgi Apparatus)", "माइटोकॉन्ड्रिया", "लाइसोसोम", "तारककेंद्र"],
        "ans": 0,
        "sol": "The Golgi Apparatus modifies proteins and lipids received from the endoplasmic reticulum, packages them into vesicles, and directs them to various destinations. It is also the major site for synthesizing glycoproteins and glycolipids.",
        "sol_hi": "गोल्जी उपकरण अंतःप्रद्रव्यी जालिका से प्राप्त प्रोटीन और लिपिड को संशोधित करता है, उन्हें पुटिकाओं (vesicles) में पैक करता है और गंतव्यों तक पहुंचाता है। यह ग्लाइकोप्रोटीन संश्लेषण का मुख्य स्थल भी है।"
    },
    {
        "q": "Which organelle is absent in plant cells but present in animal cells to help form the spindle poles during cell division?",
        "q_hi": "कौन सा कोशिकांग पादप कोशिकाओं में अनुपस्थित होता है लेकिन जंतु कोशिकाओं में कोशिका विभाजन के दौरान तर्कु ध्रुव (spindle poles) बनाने में मदद करने के लिए उपस्थित होता है?",
        "opts": ["Centrosome / Centriole", "Mitochondria", "Plastids", "Ribosomes"],
        "opts_hi": ["तारककाय / तारककेंद्र (Centrosome)", "माइटोकॉन्ड्रिया", "लवक (Plastids)", "राइबोसोम"],
        "ans": 0,
        "sol": "Centrosomes containing centrioles are present in animal cells where they organize spindle fibers during division. Plant cells lack centrioles but can still form mitotic spindles from other microtubule organizing centers.",
        "sol_hi": "तारककाय (Centrosome) जिसमें सेंट्रीओल होते हैं, जंतु कोशिकाओं में पाए जाते हैं जहां वे विभाजन के दौरान तर्कु तंतुओं को व्यवस्थित करते हैं। पादप कोशिकाओं में इनका अभाव होता है।"
    },
    {
        "q": "The X-like structures formed by homologous chromosomes during their separation in diplotene are called:",
        "q_hi": "डिप्लोटीन चरण में समजात गुणसूत्रों के अलग होने के दौरान बनने वाली X-जैसी संरचनाओं को क्या कहा जाता है?",
        "opts": ["Centromeres", "Chiasmata", "Synaptonemal Complex", "Spindles"],
        "opts_hi": ["सेंट्रोमियर", "कयाज्मेटा (Chiasmata)", "सूत्रयुग्मकीय सम्मिश्र", "तर्कु"],
        "ans": 1,
        "sol": "During the Diplotene stage, the synaptonemal complex dissolves, and homologous chromosomes begin to separate except at crossing-over sites. These persisting cross connections form 'X'-shaped structures called Chiasmata.",
        "sol_hi": "डिप्लोटीन चरण के दौरान, सूत्रयुग्मकीय सम्मिश्र घुल जाता है, और समजात गुणसूत्र अलग होने लगते हैं, सिवाय जीन विनिमय वाले स्थलों के। इन बचे हुए संपर्क बिंदुओं को कयाज्मेटा (Chiasmata) कहा जाता है जो 'X' आकार के होते हैं।"
    },
    {
        "q": "The pigment-free plastids specialized for storing food materials (starch, lipids, proteins) in plants are called:",
        "q_hi": "पौधों में खाद्य पदार्थों (स्टार्च, वसा, प्रोटीन) को संचित करने वाले वर्णक-रहित लवक कहलाते हैं:",
        "opts": ["Chromoplasts", "Leucoplasts", "Chloroplasts", "Rhodoplasts"],
        "opts_hi": ["क्रोमोप्लास्ट", "ल्यूकोप्लास्ट (Leucoplasts)", "क्लोरोप्लास्ट", "रोडोप्लास्ट"],
        "ans": 1,
        "sol": "Leucoplasts are colorless plastids that store nutrients: Amyloplasts store starch (carbohydrates), Elaioplasts store lipids (oils/fats), and Aleuroplasts store proteins.",
        "sol_hi": "ल्यूकोप्लास्ट (अवर्णलवक) रंगहीन लवक होते हैं जो पोषक तत्वों का संचय करते हैं: एमाइलोप्लास्ट स्टार्च संचित करते हैं, इलियोप्लास्ट वसा/तेल और एल्यूरोप्लास्ट प्रोटीन संचित करते हैं।"
    },
    {
        "q": "Which of the following organelles is also known as the 'cell within a cell'?",
        "q_hi": "निम्नलिखित में से किस कोशिकांग को 'कोशिका के भीतर कोशिका' भी कहा जाता है?",
        "opts": ["Ribosome", "Mitochondria", "Lysosome", "Endoplasmic Reticulum"],
        "opts_hi": ["राइबोसोम", "माइटोकॉन्ड्रिया (Mitochondria)", "लाइसोसोम", "अंतःप्रद्रव्यी जालिका"],
        "ans": 1,
        "sol": "Mitochondria (and Chloroplasts) are referred to as 'cells within a cell' due to the endosymbiotic theory, which states they evolved from free-living prokaryotic ancestors that were engulfed by ancestral eukaryotic cells.",
        "sol_hi": "माइटोकॉन्ड्रिया (और क्लोरोप्लास्ट) को अंतःसहजीवी सिद्धांत (endosymbiotic theory) के कारण 'कोशिका के भीतर कोशिका' कहा जाता है। माना जाता है कि ये स्वतंत्र रहने वाले जीवाणुओं से विकसित हुए हैं।"
    },
    {
        "q": "Which subunit combination makes up the 80S eukaryotic ribosome?",
        "q_hi": "कौन सा उप-इकाई संयोजन 80S यूकैरियोटिक राइबोसोम का निर्माण करता है?",
        "opts": ["50S and 30S", "60S and 40S", "50S and 40S", "60S and 30S"],
        "opts_hi": ["50S और 30S", "60S और 40S (60S & 40S)", "50S और 40S", "60S और 30S"],
        "ans": 1,
        "sol": "Eukaryotic 80S ribosomes are assembled from a large 60S subunit and a small 40S subunit. Prokaryotic 70S ribosomes are made of 50S and 30S subunits.",
        "sol_hi": "यूकैरियोटिक 80S राइबोसोम एक बड़ी 60S उप-इकाई और एक छोटी 40S उप-इकाई से मिलकर बना होता है। प्रोकैरियोटिक 70S राइबोसोम 50S और 30S उप-इकाइयों से बनता है।"
    },
    {
        "q": "What is the function of the nucleolus?",
        "q_hi": "केंद्रिका (nucleolus) का क्या कार्य है?",
        "opts": ["DNA Replication", "rRNA synthesis and ribosome assembly", "Cell wall formation", "Lipid synthesis"],
        "opts_hi": ["डीएनए प्रतिकृति", "rRNA संश्लेषण और राइबोसोम असेंबली", "कोशिका भित्ति का निर्माण", "लिपिड संश्लेषण"],
        "ans": 1,
        "sol": "The nucleolus is primarily responsible for transcribing ribosomal RNA (rRNA) and assembling ribosomal subunits, which are then transported to the cytoplasm.",
        "sol_hi": "केंद्रिका मुख्य रूप से राइबोसोमल आरएनए (rRNA) के प्रतिलेखन और राइबोसोम की उप-इकाइयों को असेंबल करने के लिए जिम्मेदार है, जो फिर कोशिकाद्रव्य में भेज दिए जाते हैं।"
    },
    {
        "q": "The cell organelle that plays a key role in synthesizing steroid hormones in animal endocrine cells is:",
        "q_hi": "जंतु अंतःस्रावी कोशिकाओं में स्टेरॉयड हार्मोन के संश्लेषण में प्रमुख भूमिका निभाने वाला कोशिकांग है:",
        "opts": ["Smooth Endoplasmic Reticulum", "Rough Endoplasmic Reticulum", "Golgi apparatus", "Lysosomes"],
        "opts_hi": ["चिकनी अंतःप्रद्रव्यी जालिका (SER)", "खुरदुरी अंतःप्रद्रव्यी जालिका", "गोल्जी उपकरण", "लाइसोसोम"],
        "ans": 0,
        "sol": "Smooth Endoplasmic Reticulum (SER) contains enzymes involved in lipid synthesis, including cholesterol, phospholipids, and steroid hormones (like testosterone and estrogen) in endocrine glands.",
        "sol_hi": "चिकनी अंतःप्रद्रव्यी जालिका (SER) में लिपिड संश्लेषण से जुड़े एंजाइम होते हैं, जो अंतःस्रावी ग्रंथियों में कोलेस्ट्रॉल, फॉस्फोलिपिड और स्टेरॉयड हार्मोन के निर्माण में मदद करते हैं।"
    },
    {
        "q": "The shortest phase of mitosis is:",
        "q_hi": "समसूत्री विभाजन (mitosis) का सबसे छोटा चरण कौन सा है?",
        "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "opts_hi": ["प्रोफेज", "मेटाफेज", "एनाफेज (Anaphase)", "टीलोफेज"],
        "ans": 2,
        "sol": "Anaphase is the shortest phase of mitosis. It takes only a few minutes, during which sister chromatids separate at the centromere and migrate toward opposite poles.",
        "sol_hi": "एनाफेज समसूत्री विभाजन का सबसे छोटा चरण है। इसमें केवल कुछ मिनट लगते हैं, जिसके दौरान सिस्टर क्रोमैटिड्स सेंट्रोमियर पर अलग हो जाते हैं और विपरीत ध्रुवों की ओर खिंचते हैं।"
    },
    {
        "q": "Who discovered the nucleus in the cell in 1831?",
        "q_hi": "1831 में कोशिका में केंद्रक (nucleus) की खोज किसने की थी?",
        "opts": ["Robert Hooke", "Robert Brown", "Rudolf Virchow", "Purkinje"],
        "opts_hi": ["रॉबर्ट हुक", "रॉबर्ट ब्राउन (Robert Brown)", "रुडोल्फ विरचो", "पुरकिंजे"],
        "ans": 1,
        "sol": "Robert Brown discovered and described the cell nucleus in 1831 while studying orchid cells under a microscope.",
        "sol_hi": "रॉबर्ट ब्राउन ने 1831 में ऑर्किड कोशिकाओं के अध्ययन के दौरान कोशिका के केंद्रक की खोज की और इसका विवरण दिया था।"
    },
    {
        "q": "Which of the following cell organelles is non-membranous?",
        "q_hi": "निम्नलिखित में से कौन सा कोशिकांग झिल्ली रहित होता है?",
        "opts": ["Mitochondria", "Ribosome", "Lysosome", "Plastid"],
        "opts_hi": ["माइटोकॉन्ड्रिया", "राइबोसोम (Ribosome)", "लाइसोसोम", "लवक"],
        "ans": 1,
        "sol": "Ribosomes (and Centrosomes in animals) do not possess any membrane. Mitochondria and plastids have double membranes, while lysosomes have a single membrane.",
        "sol_hi": "राइबोसोम (और जंतुओं में तारककाय) में कोई झिल्ली नहीं होती है। माइटोकॉन्ड्रिया और लवक में दोहरी झिल्ली होती है, जबकि लाइसोसोम में एकल झिल्ली होती है।"
    },
    {
        "q": "Chromosomes are composed of DNA and which type of basic proteins?",
        "q_hi": "गुणसूत्र डीएनए और किस प्रकार के क्षारीय प्रोटीनों से बने होते हैं?",
        "opts": ["Albumins", "Globulins", "Histones", "Tubulins"],
        "opts_hi": ["एल्ब्यूमिन", "ग्लोब्युलिन", "हिस्टोन (Histones)", "ट्यूबुलिन"],
        "ans": 2,
        "sol": "Chromosomal chromatin is composed of DNA wrapped around basic proteins called Histones. Histones are rich in basic amino acids like lysine and arginine, which give them a positive charge to bind tightly with negatively charged DNA.",
        "sol_hi": "गुणसूत्रीय क्रोमेटिन डीएनए और हिस्टोन (Histones) नामक क्षारीय प्रोटीनों से बने होते हैं। हिस्टोन में लाइसिन और आर्जिनिन जैसे अमीनो अम्ल प्रचुर मात्रा में होते हैं, जो उन्हें धनावेश प्रदान करते हैं।"
    },
    {
        "q": "Karyokinesis refers to the division of:",
        "q_hi": "कैरियोकाइनेसिस (Karyokinesis) से तात्पर्य किसके विभाजन से है?",
        "opts": ["Cytoplasm", "Nucleus", "Cell wall", "Plastids"],
        "opts_hi": ["कोशिकाद्रव्य", "केंद्रक (Nucleus)", "कोशिका भित्ति", "लवक"],
        "ans": 1,
        "sol": "Cell division consists of Karyokinesis (division of the nucleus) followed by Cytokineses (division of the cytoplasm to form separate cells).",
        "sol_hi": "कोशिका विभाजन में पहले कैरियोकाइनेसिस (केंद्रक का विभाजन) होता है, जिसके बाद साइटोकाइनेसिस (कोशिकाद्रव्य का विभाजन) होता है।"
    },
    {
        "q": "The term 'Protoplasm' was coined by:",
        "q_hi": "'प्रोटोप्लाज्म' (जीवद्रव्य) शब्द किसके द्वारा गढ़ा गया था?",
        "opts": ["Robert Hooke", "J.E. Purkinje", "Robert Brown", "Hugo von Mohl"],
        "opts_hi": ["रॉबर्ट हुक", "जे.ई. पुरकिंजे (J.E. Purkinje)", "रॉबर्ट ब्राउन", "ह्यूगो वॉन मोहल"],
        "ans": 1,
        "sol": "Jan Evangelista Purkinje coined the term 'Protoplasm' in 1839 to describe the fluid/jelly-like living content of a cell.",
        "sol_hi": "जे.ई. पुरकिंजे ने 1839 में कोशिका के भीतर मौजूद जीवित तरल पदार्थ को दर्शाने के लिए 'प्रोटोप्लाज्म' (जीवद्रव्य) शब्द गढ़ा था।"
    },
    {
        "q": "Which of the following cell organelles is involved in the formation of lysosomes?",
        "q_hi": "निम्नलिखित में से कौन सा कोशिकांग लाइसोसोम के निर्माण में शामिल होता है?",
        "opts": ["Mitochondria", "Golgi Apparatus", "Ribosomes", "Plastids"],
        "opts_hi": ["माइटोकॉन्ड्रिया", "गोल्जी उपकरण (Golgi Apparatus)", "राइबोसोम", "लवक"],
        "ans": 1,
        "sol": "Lysosomes originate from the Golgi Apparatus. Hydrolytic enzymes synthesized in the RER are transported to the Golgi body, where they are packaged into functional lysosomes.",
        "sol_hi": "लाइसोसोम गोल्जी उपकरण (Golgi Apparatus) से उत्पन्न होते हैं। RER में बने हाइड्रोलाइटिक एंजाइम गोल्जी उपकरण में भेजे जाते हैं, जहां से उन्हें लाइसोसोम के रूप में पैक किया जाता है।"
    },
    {
        "q": "Which eukaryotic cell organelle is considered to have evolved via endosymbiosis of an aerobic bacterium?",
        "q_hi": "किस यूकैरियोटिक कोशिकांग को एक वायवीय जीवाणु के अंतःसहजीवन (endosymbiosis) के माध्यम से विकसित माना जाता है?",
        "opts": ["Chloroplast", "Mitochondria", "Lysosome", "Peroxisome"],
        "opts_hi": ["क्लोरोप्लास्ट", "माइटोकॉन्ड्रिया (Mitochondria)", "लाइसोसोम", "परऑक्सीसोम"],
        "ans": 1,
        "sol": "Mitochondria are thought to have evolved from an aerobic alpha-proteobacterium that entered into an endosymbiotic relationship with a host archaeal/eukaryotic cell. Chloroplasts similarly evolved from photosynthetic cyanobacteria.",
        "sol_hi": "माना जाता है कि माइटोकॉन्ड्रिया एक वायवीय जीवाणु के प्राचीन यूकैरियोटिक कोशिका में प्रवेश करने और परस्पर सहजीवन बनाने से उत्पन्न हुए हैं। इसी प्रकार क्लोरोप्लास्ट सायनोबैक्टीरिया से बने हैं।"
    },
    {
        "q": "The L-shaped chromosomes during anaphase are classified as:",
        "q_hi": "एनाफेज के दौरान 'L' आकार वाले गुणसूत्रों को किस रूप में वर्गीकृत किया जाता है?",
        "opts": ["Metacentric", "Sub-metacentric", "Acrocentric", "Telocentric"],
        "opts_hi": ["मध्यकेंद्री", "उप-मध्यकेंद्री (Sub-metacentric)", "अग्रकेंद्री", "अंतकेंद्री"],
        "ans": 1,
        "sol": "Sub-metacentric chromosomes have their centromere slightly off-center. When pulled during anaphase, the unequal arms form an L-shape (or J-shape for acrocentric, V-shape for metacentric).",
        "sol_hi": "उप-मध्यकेंद्री (Sub-metacentric) गुणसूत्रों में सेंट्रोमियर केंद्र से थोड़ा अलग होता है। एनाफेज के दौरान खींचे जाने पर उनकी असमान भुजाएं L-आकार बनाती हैं।"
    },
    {
        "q": "In plant cell division, cytokinesis occurs through the formation of a:",
        "q_hi": "पादप कोशिका विभाजन में, साइटोकाइनेसिस (कोशिकाद्रव्य विभाजन) किसके बनने से होता है?",
        "opts": ["Cleavage furrow", "Cell plate", "Contractile ring", "Spindle pole"],
        "opts_hi": ["क्लीवेज खांच", "कोशिका पट्ट (Cell plate)", "संकुचनशील वलय", "तर्कु ध्रुव"],
        "ans": 1,
        "sol": "Because of the rigid plant cell wall, animal-like cleavage furrows cannot form. Instead, plant cytokinesis occurs via cell plate formation starting from the center (phragmoplast) and growing outward.",
        "sol_hi": "कठोर कोशिका भित्ति के कारण पौधों में क्लीवेज खांच नहीं बन सकती। इसके बजाय, पादप साइटोकाइनेसिस कोशिका पट्ट (cell plate) के निर्माण द्वारा केंद्र से बाहर की ओर होता है।"
    },
    {
        "q": "The enzyme recombinase, which facilitates crossing over, is highly active during which stage of meiosis?",
        "q_hi": "जीन विनिमय को सुगम बनाने वाला एंजाइम रिकॉम्बिनेज (recombinase) अर्धसूत्रीविभाजन के किस चरण के दौरान अत्यधिक सक्रिय होता है?",
        "opts": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        "opts_hi": ["लेप्टोटीन", "जायगोटीन", "पैकीटीन (Pachytene)", "डिप्लोटीन"],
        "ans": 2,
        "sol": "Recombinase is the enzyme complex that catalyzes genetic crossing over during the Pachytene stage of Prophase I in Meiosis I.",
        "sol_hi": "रिकॉम्बिनेज वह एंजाइम कॉम्प्लेक्स है जो अर्धसूत्रीविभाजन I के प्रोफेज I की पैकीटीन (Pachytene) अवस्था के दौरान आनुवंशिक क्रॉसिंग ओवर को उत्प्रेरित करता है।"
    },
    {
        "q": "Chromosomes with terminal centromeres are studied as:",
        "q_hi": "अंतिम सेंट्रोमियर वाले गुणसूत्रों का अध्ययन किस रूप में किया जाता है?",
        "opts": ["Acrocentric", "Telocentric", "Metacentric", "Sub-metacentric"],
        "opts_hi": ["अग्रकेंद्री", "अंतकेंद्री (Telocentric)", "मध्यकेंद्री", "उप-मध्यकेंद्री"],
        "ans": 1,
        "sol": "Telocentric chromosomes have centromeres at the very tip (telomeric region). They appear I-shaped or rod-shaped during anaphase.",
        "sol_hi": "अंतकेंद्री (Telocentric) गुणसूत्रों में सेंट्रोमियर बिल्कुल अंतिम छोर पर होता है। ये एनाफेज के दौरान छड़ जैसे दिखते हैं।"
    },
    {
        "q": "Which plant cell organelle is rich in catalase enzyme and metabolizes hydrogen peroxide?",
        "q_hi": "कौन सा पादप कोशिकांग कैटालेज (catalase) एंजाइम से भरपूर होता है और हाइड्रोजन परऑक्साइड का चयापचय करता है?",
        "opts": ["Lysosome", "Peroxisome", "Glyoxysome", "Ribosome"],
        "opts_hi": ["लाइसोसोम", "परऑक्सीसोम (Peroxisome)", "ग्लाइऑक्सीसोम", "राइबोसोम"],
        "ans": 1,
        "sol": "Peroxisomes contain oxidative enzymes like catalase that degrade hydrogen peroxide (H₂O₂), a toxic byproduct of cellular respiration, into water and oxygen.",
        "sol_hi": "परऑक्सीसोम (Peroxisome) में कैटालेज जैसे ऑक्सीडेटिव एंजाइम होते हैं जो कोशिका श्वसन के हानिकारक उपोत्पाद हाइड्रोजन परऑक्साइड (H₂O₂) को पानी और ऑक्सीजन में तोड़ते हैं।"
    },
    {
        "q": "Which of the following represents the correct sequential order of Meiosis Prophase I sub-stages?",
        "q_hi": "निम्नलिखित में से कौन सा अर्धसूत्रीविभाजन प्रोफेज I के उप-चरणों के सही क्रमिक अनुक्रम को दर्शाता है?",
        "opts": [
            "Leptotene -> Pachytene -> Zygotene -> Diplotene -> Diakinesis",
            "Leptotene -> Zygotene -> Pachytene -> Diplotene -> Diakinesis",
            "Zygotene -> Leptotene -> Pachytene -> Diplotene -> Diakinesis",
            "Leptotene -> Zygotene -> Diplotene -> Pachytene -> Diakinesis"
        ],
        "opts_hi": [
            "लेप्टोटीन -> पैकीटीन -> जायगोटीन -> डिप्लोटीन -> डायकइनेसिस",
            "लेप्टोटीन -> जायगोटीन -> पैकीटीन -> डिप्लोटीन -> डायकइनेसिस",
            "जायगोटीन -> लेप्टोटीन -> पैकीटीन -> डिप्लोटीन -> डायकइनेसिस",
            "लेप्टोटीन -> जायगोटीन -> डिप्लोटीन -> पैकीटीन -> डायकइनेसिस"
        ],
        "ans": 1,
        "sol": "The correct sequential order of Prophase I is: Leptotene, Zygotene (synapsis), Pachytene (crossing over), Diplotene (chiasmata formation), and Diakinesis (terminalization). Memory aid: LZPDD.",
        "sol_hi": "प्रोफेज I के चरणों का सही क्रम है: लेप्टोटीन, जायगोटीन, पैकीटीन, डिप्लोटीन और डायकइनेसिस। इसे LZPDD स्मृति सूत्र से याद रखा जा सकता है।"
    },
    {
        "q": "A eukaryotic plant cell has cell walls primarily containing cellulose. What is the fungal cell wall made of?",
        "q_hi": "एक यूकैरियोटिक पादप कोशिका की कोशिका भित्ति में मुख्य रूप से सेलुलोज होता है। कवक की कोशिका भित्ति किससे बनी होती है?",
        "opts": ["Peptidoglycan", "Chitin", "Starch", "Glycogen"],
        "opts_hi": ["पेप्टिडोग्लाइकन", "काइटिन (Chitin)", "स्टार्च", "ग्लाइकोजन"],
        "ans": 1,
        "sol": "The cell wall of Fungi is composed of Chitin, a polymer of N-acetylglucosamine. Bacteria have peptidoglycan walls.",
        "sol_hi": "कवक की कोशिका भित्ति काइटिन (Chitin) से बनी होती है, जो N-एसिटाइलग्लूकोसामाइन का बहुलक है। जीवाणुओं में पेप्टिडोग्लाइकन की भित्ति होती है।"
    },
    {
        "q": "The active transport of molecules across the cell membrane requires energy in the form of:",
        "q_hi": "कोशिका झिल्ली के पार अणुओं के सक्रिय परिवहन (active transport) के लिए किस रूप में ऊर्जा की आवश्यकता होती है?",
        "opts": ["AMP", "ADP", "ATP", "NAD+"],
        "opts_hi": ["AMP", "ADP", "एटीपी (ATP)", "NAD+"],
        "ans": 2,
        "sol": "Active transport moves substances against their concentration gradient (from low to high concentration) and requires chemical energy in the form of ATP.",
        "sol_hi": "सक्रिय परिवहन अणुओं को उनकी सांद्रता प्रवणता के विपरीत (कम से अधिक सांद्रता की ओर) ले जाता है, जिसके लिए एटीपी (ATP) के रूप में रासायनिक ऊर्जा की आवश्यकता होती है।"
    },
    {
        "q": "Maternal inheritance of mitochondrial DNA is observed because:",
        "q_hi": "माइटोकॉन्ड्रियल डीएनए की मातृ वंशागति (maternal inheritance) क्यों देखी जाती है?",
        "opts": [
            "Maternal DNA is stronger",
            "Mitochondria of sperm are degraded or not entered into the egg during fertilization",
            "Egg cell has no nucleus",
            "Sperm cell has no mitochondria"
        ],
        "opts_hi": [
            "मातृ डीएनए अधिक मजबूत होता है",
            "निषेचन के दौरान शुक्राणु के माइटोकॉन्ड्रिया नष्ट हो जाते हैं या अंडे में प्रवेश नहीं करते हैं",
            "अंड कोशिका में केंद्रक नहीं होता है",
            "शुक्राणु कोशिका में माइटोकॉन्ड्रिया नहीं होते हैं"
        ],
        "ans": 1,
        "sol": "During fertilization, only the sperm nucleus enters the egg. The sperm's mitochondria (located in the tail/midpiece) are shed or destroyed, so all mitochondria in the zygote come exclusively from the egg cytoplasm.",
        "sol_hi": "निषेचन के दौरान, केवल शुक्राणु का केंद्रक अंडे में प्रवेश करता है। शुक्राणु के माइटोकॉन्ड्रिया (जो पूंछ/मध्य भाग में होते हैं) बाहर ही छूट जाते हैं या नष्ट हो जाते हैं, जिससे युग्मनज (zygote) के सभी माइटोकॉन्ड्रिया केवल अंडे से आते हैं।"
    },
    {
        "q": "The terminalization of chiasmata takes place in which sub-stage of Prophase I?",
        "q_hi": "कयाज्मेटा का उपांतीकरण (terminalization) प्रोफेज I के किस उप-चरण में होता है?",
        "opts": ["Zygotene", "Pachytene", "Diplotene", "Diakinesis"],
        "opts_hi": ["जायगोटीन", "पैकीटीन", "डिप्लोटीन", "डायकइनेसिस (Diakinesis)"],
        "ans": 3,
        "sol": "Diakinesis is characterized by the terminalization of chiasmata (chiasmata shift to the ends of chromosomes) along with the completion of chromosome condensation and spindle formation.",
        "sol_hi": "डायकइनेसिस (Diakinesis) चरण की विशेषता कयाज्मेटा का उपांतीकरण (गुणसूत्रों के सिरों की ओर खिसकना) है, साथ ही गुणसूत्र संघनन और तर्कु तंतुओं का निर्माण पूरा होता है।"
    },
    {
        "q": "Which of the following statement is true regarding Mitosis?",
        "q_hi": "समसूत्री विभाजन (Mitosis) के संबंध में निम्नलिखित में से कौन सा कथन सत्य है?",
        "opts": [
            "It leads to the formation of haploid cells",
            "It involves two rounds of chromosome division",
            "It maintains the diploid chromosome number in daughter cells",
            "It occurs only in reproductive cells"
        ],
        "opts_hi": [
            "यह अगुणित कोशिकाओं के निर्माण की ओर ले जाता है",
            "इसमें गुणसूत्र विभाजन के दो चक्र शामिल होते हैं",
            "यह संतति कोशिकाओं में द्विगुणित गुणसूत्र संख्या बनाए रखता है",
            "यह केवल जनन कोशिकाओं में होता है"
        ],
        "ans": 2,
        "sol": "Mitosis is also called equational division. It occurs in somatic cells and maintains the same diploid chromosome number (2n) in daughter cells as the parent cell.",
        "sol_hi": "समसूत्री विभाजन को समकारी विभाजन भी कहा जाता है। यह कायिक कोशिकाओं में होता है और संतति कोशिकाओं में जनक कोशिका के समान द्विगुणित गुणसूत्र संख्या (2n) बनाए रखता है।"
    },
    {
        "q": "Which cell organelles are involved in the photorespiration pathway in plants?",
        "q_hi": "पौधों में प्रकाश-श्वसन (photorespiration) पथ में कौन से कोशिकांग शामिल होते हैं?",
        "opts": [
            "Chloroplast, Mitochondria, and Ribosome",
            "Chloroplast, Peroxisome, and Mitochondria",
            "Chloroplast, Lysosome, and Mitochondria",
            "Chloroplast, Vacuole, and Ribosome"
        ],
        "opts_hi": [
            "क्लोरोप्लास्ट, माइटोकॉन्ड्रिया और राइबोसोम",
            "क्लोरोप्लास्ट, परऑक्सीसोम और माइटोकॉन्ड्रिया (Chloroplast, Peroxisome & Mitochondria)",
            "क्लोरोप्लास्ट, लाइसोसोम और माइटोकॉन्ड्रिया",
            "क्लोरोप्लास्ट, रिक्तिका और राइबोसोम"
        ],
        "ans": 1,
        "sol": "Photorespiration (C2 cycle) in plants is a cooperative metabolic process involving three organelles in sequence: Chloroplast, Peroxisome, and Mitochondria.",
        "sol_hi": "पौधों में प्रकाश-श्वसन (C2 चक्र) एक सहयोगात्मक चयापचय प्रक्रिया है जिसमें क्रमबद्ध रूप से तीन कोशिकांग शामिल होते हैं: क्लोरोप्लास्ट, परऑक्सीसोम और माइटोकॉन्ड्रिया।"
    },
    {
        "q": "The site of light reactions during photosynthesis in chloroplasts is the:",
        "q_hi": "क्लोरोप्लास्ट में प्रकाश संश्लेषण के दौरान प्रकाश अभिक्रियाओं (light reactions) का स्थल है:",
        "opts": ["Stroma", "Thylakoid/Grana membrane", "Inner membrane", "Periplastidial space"],
        "opts_hi": ["स्ट्रोमा", "थायलाकोइड/ग्रेना झिल्ली (Thylakoid/Grana)", "आंतरिक झिल्ली", "लवक-अवकाश"],
        "ans": 1,
        "sol": "Light-dependent reactions (which capture light and produce ATP and NADPH) occur in the thylakoid membranes (stacked as grana). The light-independent (dark) reactions occur in the fluid stroma.",
        "sol_hi": "प्रकाश-निर्भर अभिक्रियाएँ (जो प्रकाश ग्रहण कर एटीपी और एनएडीपीएच बनाती हैं) थायलाकोइड झिल्लियों (ग्रेना) में होती हैं। प्रकाश-स्वतंत्र (अप्रकाशिक) अभिक्रियाएँ तरल स्ट्रोमा (Stroma) में होती हैं।"
    },
    {
        "q": "Which cell organelle is active in synthesising ribosomal RNA in eukaryotes?",
        "q_hi": "यूकैरियोट्स में राइबोसोमल आरएनए के संश्लेषण में कौन सा कोशिकांग सक्रिय है?",
        "opts": ["Golgi bodies", "Lysosomes", "Nucleolus", "Cytoplasm"],
        "opts_hi": ["गोल्जी काय", "लाइसोसोम", "केंद्रिका (Nucleolus)", "कोशिकाद्रव्य"],
        "ans": 2,
        "sol": "The nucleolus is the active site for transcribing ribosomal RNA (rRNA) and initial assembly of ribosomes.",
        "sol_hi": "केंद्रिका (nucleolus) राइबोसोमल आरएनए (rRNA) के प्रतिलेखन और राइबोसोम के प्रारंभिक असेंबली का सक्रिय स्थल है।"
    },
    {
        "q": "Which structural fiber is the primary component of spindle fibers?",
        "q_hi": "कौन सा संरचनात्मक तंतु तर्कु तंतुओं (spindle fibers) का प्राथमिक घटक है?",
        "opts": ["Actin filaments", "Microtubules", "Intermediate filaments", "Collagen fibers"],
        "opts_hi": ["एक्टिन तंतु", "सूक्ष्मनलिकाएं (Microtubules)", "मध्यवर्ती तंतु", "कोलेजन तंतु"],
        "ans": 1,
        "sol": "Spindle fibers are composed of microtubules, which are polymer cylinders made of tubulin proteins (alpha and beta tubulin).",
        "sol_hi": "तर्कु तंतु सूक्ष्मनलिकाओं (microtubules) से बने होते हैं, जो ट्यूबुलिन प्रोटीन (अल्फा और बीटा ट्यूबुलिन) से बने बहुलक बेलनाकार संरचनाएं हैं।"
    }
]

# Adding remaining practice questions to reach 50
extra_pqs = [
    {
        "q": "The chromosome count in a normal human somatic cell is:",
        "q_hi": "एक सामान्य मानव कायिक कोशिका में गुणसूत्रों की संख्या कितनी होती है?",
        "opts": ["23", "46", "48", "44"],
        "opts_hi": ["23", "46 (46)", "48", "44"],
        "ans": 1,
        "sol": "A normal human somatic cell has 46 chromosomes (23 pairs: 22 pairs of autosomes and 1 pair of sex chromosomes). Gametes contain 23 chromosomes.",
        "sol_hi": "एक सामान्य मानव कायिक कोशिका में 46 गुणसूत्र होते हैं (23 जोड़े: 22 जोड़े अलिंगसूत्र और 1 जोड़ा लिंगसूत्र)। युग्मकों में 23 गुणसूत्र होते हैं।"
    },
    {
        "q": "The cell wall of plants is synthesized by which organelle during cell division?",
        "q_hi": "कोशिका विभाजन के दौरान पादप कोशिका भित्ति का निर्माण किस कोशिकांग द्वारा किया जाता है?",
        "opts": ["Mitochondria", "Golgi Apparatus / Phragmoplast", "Lysosomes", "Plastids"],
        "opts_hi": ["माइटोकॉन्ड्रिया", "गोल्जी उपकरण / फ्रैग्मोप्लास्ट", "लाइसोसोम", "लवक"],
        "ans": 1,
        "sol": "During plant cytokinesis, secretory vesicles from the Golgi Apparatus align at the equator to form a cell plate (phragmoplast), which eventually matures into the new cell wall.",
        "sol_hi": "पादप कोशिकाद्रव्य विभाजन के दौरान, गोल्जी उपकरण से निकलने वाली स्रावी पुटिकाएं भूमध्य रेखा पर संरेखित होकर कोशिका पट्ट (cell plate) बनाती हैं, जो आगे चलकर कोशिका भित्ति बनती है।"
    },
    {
        "q": "Which organelle plays a primary role in cellular autophagy (self-eating of old organelles)?",
        "q_hi": "कोशिकीय स्व-भक्षण (autophagy - पुराने अंगों को पचाना) में कौन सा कोशिकांग प्राथमिक भूमिका निभाता है?",
        "opts": ["Ribosome", "Lysosome", "Centrosome", "Peroxisome"],
        "opts_hi": ["राइबोसोम", "लाइसोसोम (Lysosome)", "तारककाय", "परऑक्सीसोम"],
        "ans": 1,
        "sol": "Lysosomes are responsible for autophagy, engulfing damaged organelles or macromolecules in autophagosomes and digesting them using hydrolytic enzymes to recycle nutrients.",
        "sol_hi": "लाइसोसोम स्व-भक्षण (autophagy) के लिए जिम्मेदार हैं, जो क्षतिग्रस्त अंगों को घेरकर जल-अपघटकीय एंजाइमों का उपयोग करके उन्हें पचाते हैं ताकि पोषक तत्वों का पुनर्चक्रण किया जा सके।"
    },
    {
        "q": "Which of the following eukaryotic organelles does not contain any DNA?",
        "q_hi": "निम्नलिखित में से किस यूकैरियोटिक कोशिकांग में डीएनए नहीं होता है?",
        "opts": ["Nucleus", "Mitochondria", "Chloroplast", "Golgi Apparatus"],
        "opts_hi": ["केंद्रक", "माइटोकॉन्ड्रिया", "क्लोरोप्लास्ट", "गोल्जी उपकरण (Golgi Apparatus)"],
        "ans": 3,
        "sol": "The nucleus, mitochondria, and chloroplasts contain DNA. The Golgi Apparatus is a membranous packaging organelle and does not possess its own genetic material.",
        "sol_hi": "केंद्रक, माइटोकॉन्ड्रिया और क्लोरोप्लास्ट में डीएनए होता है। गोल्जी उपकरण एक पैकेजिंग अंग है और इसमें अपना आनुवंशिक पदार्थ नहीं होता है।"
    },
    {
        "q": "Which of the following biological structures is considered the boundary of an animal cell?",
        "q_hi": "निम्नलिखित में से किस जैविक संरचना को जंतु कोशिका की सीमा माना जाता है?",
        "opts": ["Cell wall", "Plasma membrane", "Tonoplast", "Nuclear membrane"],
        "opts_hi": ["कोशिका भित्ति", "प्लाज्मा झिल्ली (Plasma membrane)", "टोनोप्लास्ट", "केंद्रक झिल्ली"],
        "ans": 1,
        "sol": "The plasma membrane forms the outermost boundary of an animal cell. Plant cells have an additional external cell wall.",
        "sol_hi": "प्लाज्मा झिल्ली जंतु कोशिका की सबसे बाहरी सीमा बनाती है। पादप कोशिकाओं में इसके बाहर एक अतिरिक्त कोशिका भित्ति होती है।"
    },
    {
        "q": "The primary site of ATP synthesis during cellular respiration in eukaryotes is the:",
        "q_hi": "यूकैरियोट्स में कोशिकीय श्वसन के दौरान एटीपी संश्लेषण का प्राथमिक स्थल है:",
        "opts": ["Cytoplasm", "Mitochondrial Matrix", "Mitochondrial Inner Membrane / Cristae", "Ribosome"],
        "opts_hi": ["कोशिकाद्रव्य", "माइटोकॉन्ड्रियल मैट्रिक्स", "माइटोकॉन्ड्रियल आंतरिक झिल्ली (Cristae)", "राइबोसोम"],
        "ans": 2,
        "sol": "While glycolysis occurs in cytoplasm and Krebs cycle in mitochondrial matrix, the bulk of ATP is synthesized by ATP synthase embedded in the inner mitochondrial membrane (cristae) via oxidative phosphorylation.",
        "sol_hi": "यद्यपि ग्लाइकोलाइसिस कोशिकाद्रव्य में और क्रेब्स चक्र माइटोकॉन्ड्रिया के मैट्रिक्स में होता है, अधिकांश एटीपी संश्लेषण ऑक्सीडेटिव फास्फारिलीकरण द्वारा आंतरिक झिल्ली (क्रिस्टी) में होता है।"
    },
    {
        "q": "Which organelle is rich in plant seeds to convert stored fats into carbohydrates during germination?",
        "q_hi": "अंकुरण के दौरान संचित वसा को कार्बोहाइड्रेट में बदलने के लिए पौधों के बीजों में कौन सा कोशिकांग प्रचुर मात्रा में होता है?",
        "opts": ["Peroxisome", "Glyoxysome", "Lysosome", "Amyloplast"],
        "opts_hi": ["परऑक्सीसोम", "ग्लाइऑक्सीसोम (Glyoxysome)", "लाइसोसोम", "एमाइलोप्लास्ट"],
        "ans": 1,
        "sol": "Glyoxysomes are specialized peroxisomes found in fat-storing tissues of plant seeds. They contain enzymes of the glyoxylate cycle, converting stored lipids into sugars for the germinating seedling.",
        "sol_hi": "ग्लाइऑक्सीसोम (Glyoxysomes) बीजों में पाए जाने वाले विशिष्ट परऑक्सीसोम हैं, जो वसा को शर्करा में परिवर्तित करते हैं ताकि अंकुरित होने वाले पौधे को ऊर्जा मिल सके।"
    },
    {
        "q": "Cell division by meiosis always results in the production of daughter cells that are:",
        "q_hi": "अर्धसूत्रीविभाजन द्वारा कोशिका विभाजन के परिणामस्वरूप हमेशा बनने वाली संतति कोशिकाएं होती हैं:",
        "opts": ["Diploid", "Haploid", "Polyploid", "Identical clone"],
        "opts_hi": ["द्विगुणित", "अगुणित (Haploid)", "बहुगुणित", "समान क्लोन"],
        "ans": 1,
        "sol": "Meiosis is reductional division, halving the chromosomal count of diploid (2n) germ cells to produce haploid (n) gametes.",
        "sol_hi": "अर्धसूत्रीविभाजन एक न्यूनकारी विभाजन है, जो द्विगुणित (2n) जनन कोशिकाओं की गुणसूत्र संख्या को आधा कर अगुणित (n) युग्मक बनाता है।"
    },
    {
        "q": "The synaptonemal complex is formed during which sub-stage of Prophase I?",
        "q_hi": "सूत्रयुग्मकीय सम्मिश्र (synaptonemal complex) का निर्माण प्रोफेज I के किस उप-चरण के दौरान होता है?",
        "opts": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        "opts_hi": ["लेप्टोटीन", "जायगोटीन (Zygotene)", "पैकीटीन", "डिप्लोटीन"],
        "ans": 1,
        "sol": "The synaptonemal complex is a protein structure formed between homologous chromosomes during Zygotene, mediating chromosome pairing (synapsis).",
        "sol_hi": "सूत्रयुग्मकीय सम्मिश्र एक प्रोटीन संरचना है जो जायगोटीन के दौरान समजात गुणसूत्रों के बीच बनती है, जो सूत्रयुग्मन (synapsis) को सुगम बनाती है।"
    },
    {
        "q": "Study of cell structure, function, and biochemistry is called:",
        "q_hi": "कोशिका की संरचना, कार्य और जैव रसायन के अध्ययन को क्या कहा जाता है?",
        "opts": ["Histology", "Cytology / Cell Biology", "Physiology", "Genetics"],
        "opts_hi": ["औतिकी (Histology)", "कोशिका विज्ञान (Cytology)", "शरीर क्रिया विज्ञान", "आनुवंशिकी"],
        "ans": 1,
        "sol": "Cytology (or Cell Biology) is the branch of biology focused on studying cell structures, functions, replication, and biochemical pathways.",
        "sol_hi": "साइटोलॉजी (Cytology) या कोशिका विज्ञान जीव विज्ञान की वह शाखा है जो कोशिकाओं की संरचना, कार्य, प्रजनन और जैव रसायनों के अध्ययन पर केंद्रित है।"
    },
    {
        "q": "Which of the following represents a cell organelle that is not bound by a membrane in prokaryotes?",
        "q_hi": "निम्नलिखित में से कौन सा प्रोकैरियोट्स में एक झिल्ली रहित कोशिकांग को दर्शाता है?",
        "opts": ["Mitochondria", "Ribosome", "Nucleolus", "Mesosome"],
        "opts_hi": ["माइटोकॉन्ड्रिया", "राइबोसोम (Ribosome)", "केंद्रिका", "मीसोसोम"],
        "ans": 1,
        "sol": "Ribosomes are the only organelles found in both prokaryotes (70S) and eukaryotes (80S), and they are not bound by any membrane in either group.",
        "sol_hi": "राइबोसोम एकमात्र ऐसे कोशिकांग हैं जो प्रोकैरियोट्स (70S) और यूकैरियोट्स (80S) दोनों में पाए जाते हैं, और दोनों में ही ये झिल्ली रहित होते हैं।"
    },
    {
        "q": "Which pigment-containing plastids give yellow, orange, or red colors to flowers and fruits in plants?",
        "q_hi": "वर्णक युक्त कौन से लवक पौधों में फूलों और फलों को पीला, नारंगी या लाल रंग प्रदान करते हैं?",
        "opts": ["Chloroplasts", "Chromoplasts", "Leucoplasts", "Amyloplasts"],
        "opts_hi": ["क्लोरोप्लास्ट", "क्रोमोप्लास्ट (Chromoplasts)", "ल्यूकोप्लास्ट", "एमाइलोप्लास्ट"],
        "ans": 1,
        "sol": "Chromoplasts are carotenoid-rich plastids responsible for the bright yellow, orange, and red colors of fruits, flowers, and aging leaves.",
        "sol_hi": "क्रोमोप्लास्ट (वर्णलवक) कैरोटीनॉयड से भरपूर लवक होते हैं जो फलों, फूलों और पकने वाली पत्तियों को चमकीले पीले, नारंगी और लाल रंग प्रदान करते हैं।"
    },
    {
        "q": "The chromosome division where centromeres split occurs in which stage of mitosis?",
        "q_hi": "समसूत्री विभाजन के किस चरण में गुणसूत्रों का विभाजन होता है जहाँ सेंट्रोमियर विभाजित होते हैं?",
        "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "opts_hi": ["प्रोफेज", "मेटाफेज", "एनाफेज (Anaphase)", "टीलोफेज"],
        "ans": 2,
        "sol": "During Anaphase of mitosis, centromeres split and sister chromatids are pulled towards opposite poles by contracting spindle fibers.",
        "sol_hi": "समसूत्री विभाजन के एनाफेज चरण के दौरान, सेंट्रोमियर विभाजित होते हैं और सिस्टर क्रोमैटिड्स विपरीत ध्रुवों की ओर खींचे जाते हैं।"
    },
    {
        "q": "A cell containing 20 chromosomes undergoes mitosis. How many chromosomes will be in each daughter cell?",
        "q_hi": "20 गुणसूत्रों वाली एक कोशिका समसूत्री विभाजन से गुजरती है। प्रत्येक संतति कोशिका में कितने गुणसूत्र होंगे?",
        "opts": ["10", "20", "40", "5"],
        "opts_hi": ["10", "20 (20)", "40", "5"],
        "ans": 1,
        "sol": "Mitosis is equational division. The daughter cells will have the exact same number of chromosomes as the parent cell (20 chromosomes).",
        "sol_hi": "समसूत्री विभाजन समकारी विभाजन है। संतति कोशिकाओं में जनक कोशिका के समान ही गुणसूत्र (20 गुणसूत्र) होंगे।"
    },
    {
        "q": "The genetic material of prokaryotic cells is called a 'nucleoid' because:",
        "q_hi": "प्रोकैरियोटिक कोशिकाओं की आनुवंशिक सामग्री को 'केंद्रकाभ' (nucleoid) कहा जाता है क्योंकि:",
        "opts": [
            "It has a nuclear membrane",
            "It is naked circular DNA without a nuclear membrane wrapper",
            "It is located outside the cell",
            "It is protein-only"
        ],
        "opts_hi": [
            "इसमें केंद्रक झिल्ली होती है",
            "यह केंद्रक झिल्ली के बिना नग्न गोलाकार डीएनए होता है",
            "यह कोशिका के बाहर स्थित होता है",
            "यह केवल प्रोटीन से बना होता है"
        ],
        "ans": 1,
        "sol": "Prokaryotic genetic material is called a nucleoid (meaning nucleus-like) because it lacks a nuclear membrane or histone packaging, existing as a naked, supercoiled circular chromosome in the cytoplasm.",
        "sol_hi": "प्रोकैरियोटिक आनुवंशिक पदार्थ को केंद्रकाभ कहा जाता है क्योंकि इसमें केंद्रक झिल्ली और हिस्टोन प्रोटीन नहीं होते, और यह नग्न डीएनए के रूप में रहता है।"
    },
    {
        "q": "Which of the following organelles contains its own genetic material but is inherited almost exclusively from the mother?",
        "q_hi": "निम्नलिखित में से किस कोशिकांग में अपना स्वयं का आनुवंशिक पदार्थ होता है लेकिन यह लगभग विशेष रूप से माता से विरासत में मिलता है?",
        "opts": ["Ribosome", "Mitochondria", "Lysosome", "Endoplasmic Reticulum"],
        "opts_hi": ["राइबोसोम", "माइटोकॉन्ड्रिया (Mitochondria)", "लाइसोसोम", "अंतःप्रद्रव्यी जालिका"],
        "ans": 1,
        "sol": "Mitochondria contain their own DNA (mtDNA) and are inherited maternally because the egg cell provides all the cytoplasm and organelles to the zygote, while sperm mitochondria are excluded.",
        "sol_hi": "माइटोकॉन्ड्रिया में अपना डीएनए होता है और यह मातृ रूप से वंशागत होता है क्योंकि अंडाणु ही युग्मनज को कोशिकाद्रव्य और अंग प्रदान करता है।"
    },
    {
        "q": "Who proposed that 'all animal tissues are made of cells' in 1839?",
        "q_hi": "1839 में किसने प्रस्तावित किया था कि 'सभी जंतु ऊतक कोशिकाओं से बने होते हैं'?",
        "opts": ["Matthias Schleiden", "Theodore Schwann", "Robert Hooke", "Rudolf Virchow"],
        "opts_hi": ["मैथियास श्लाइडेन", "थियोडोर श्वान (Theodore Schwann)", "रॉबर्ट हुक", "रुडोल्फ विरचो"],
        "ans": 1,
        "sol": "Matthias Schleiden proposed plants are made of cells in 1838. Theodore Schwann extended this in 1839 stating all animal tissues are composed of cells, creating the joint Cell Theory.",
        "sol_hi": "थियोडोर श्वान ने 1839 में जंतुओं के लिए यह प्रस्तावित किया, जिससे श्लाइडेन (1838, पौधे) के साथ मिलकर कोशिका सिद्धांत की स्थापना हुई।"
    },
    {
        "q": "What is the structural monomer of microtubules?",
        "q_hi": "सूक्ष्मनलिकाओं (microtubules) का संरचनात्मक एकलक (monomer) क्या है?",
        "opts": ["Actin", "Myosin", "Tubulin", "Keratin"],
        "opts_hi": ["एक्टिन", "मायोसिन", "ट्यूबुलिन (Tubulin)", "केराटिन"],
        "ans": 2,
        "sol": "Microtubules are composed of tubulin protein dimers (alpha and beta tubulin) polymerized into hollow tubes. They form the cytoskeleton, cilia, flagella, and spindle fibers.",
        "sol_hi": "सूक्ष्मनलिकाएं ट्यूबुलिन (Tubulin) प्रोटीन से बनी होती हैं। ये तर्कु तंतु, कशाभिका (flagella) और कोशिका पंजर (cytoskeleton) का निर्माण करती हैं।"
    },
    {
        "q": "Which chromosome has centromere located very near to one end, yielding one very short and one very long arm?",
        "q_hi": "किस गुणसूत्र का सेंट्रोमियर एक छोर के बहुत पास होता है, जिससे एक बहुत छोटी और दूसरी बहुत लंबी भुजा बनती है?",
        "opts": ["Metacentric", "Sub-metacentric", "Acrocentric", "Telocentric"],
        "opts_hi": ["मध्यकेंद्री", "उप-मध्यकेंद्री", "अग्रकेंद्री (Acrocentric)", "अंतकेंद्री"],
        "ans": 2,
        "sol": "Acrocentric chromosomes have centromeres located near one terminal end, producing a tiny short arm (p-arm) and a long arm (q-arm). They form J-shape during anaphase.",
        "sol_hi": "अग्रकेंद्री (Acrocentric) गुणसूत्रों में सेंट्रोमियर एक छोर के अत्यंत निकट होता है, जिससे गुणसूत्रों की एक भुजा बहुत छोटी और दूसरी बहुत लंबी हो जाती है।"
    },
    {
        "q": "Which of the following cellular structures is responsible for maintaining turgidity in plant cells?",
        "q_hi": "निम्नलिखित में से कौन सी कोशिकीय संरचना पादप कोशिकाओं में स्फीति (turgidity) बनाए रखने के लिए जिम्मेदार है?",
        "opts": ["Chloroplast", "Vacuole", "Mitochondria", "Lysosome"],
        "opts_hi": ["क्लोरोप्लास्ट", "रिक्तिका (Vacuole)", "माइटोकॉन्ड्रिया", "लाइसोसोम"],
        "ans": 1,
        "sol": "The large central vacuole of plant cells absorbs water by osmosis and exerts turgor pressure against the cell wall, maintaining cell shape and turgidity.",
        "sol_hi": "पादप कोशिकाओं में बड़ी केंद्रीय रिक्तिका (Vacuole) परासरण द्वारा पानी सोखकर कोशिका भित्ति पर दबाव डालती है जिससे कोशिका तनी रहती है।"
    },
    {
        "q": "Cellular respiration step Krebs cycle takes place in which compartment of mitochondria?",
        "q_hi": "कोशिकीय श्वसन का क्रेब्स चक्र (Krebs cycle) माइटोकॉन्ड्रिया के किस भाग में होता है?",
        "opts": ["Inner Membrane", "Outer Membrane", "Matrix", "Intermembrane Space"],
        "opts_hi": ["आंतरिक झिल्ली", "बाहरी झिल्ली", "मैट्रिक्स (Matrix)", "अंतरा-झिल्ली अवकाश"],
        "ans": 2,
        "sol": "The enzymes of the Krebs Cycle (citric acid cycle) are located free in the mitochondrial Matrix. The electron transport chain enzymes are located in the inner membrane.",
        "sol_hi": "क्रेब्स चक्र के एंजाइम माइटोकॉन्ड्रिया के मैट्रिक्स (Matrix) में स्वतंत्र रूप से पाए जाते हैं, जबकि ETC आंतरिक झिल्ली में होता है।"
    },
    {
        "q": "Which cellular junction helps in direct cytoplasmic communication between adjacent plant cells?",
        "q_hi": "कौन सा कोशिकीय जोड़ समीपवर्ती पादप कोशिकाओं के बीच सीधे कोशिकाद्रव्यी संचार में सहायता करता है?",
        "opts": ["Tight Junctions", "Gap Junctions", "Plasmodesmata", "Desmosomes"],
        "opts_hi": ["दृढ़ जोड़", "अंतराली जोड़ (Gap Junctions)", "प्लास्मोडेस्मेटा (Plasmodesmata)", "डेस्मोसोम"],
        "ans": 2,
        "sol": "Plasmodesmata are microscopic channels crossing the cell walls of plant cells, facilitating direct cytoplasmic transport and communication between adjacent cells. Animal cells use Gap junctions.",
        "sol_hi": "प्लास्मोडेस्मेटा (Plasmodesmata) सूक्ष्म नलिकाएं हैं जो पादप कोशिका भित्ति को पार कर समीपवर्ती कोशिकाओं के कोशिकाद्रव्य को जोड़ती हैं।"
    },
    {
        "q": "The cell wall of bacteria is chemically made of:",
        "q_hi": "जीवाणुओं की कोशिका भित्ति रासायनिक रूप से किससे बनी होती है?",
        "opts": ["Cellulose", "Chitin", "Peptidoglycan", "Pectin"],
        "opts_hi": ["सेलुलोज", "काइटिन", "पेप्टिडोग्लाइकन (Peptidoglycan)", "पेक्टिन"],
        "ans": 2,
        "sol": "Bacterial cell walls contain Peptidoglycan (also called murein), which is a polymer of sugars and amino acids. Fungi walls contain chitin and plants have cellulose.",
        "sol_hi": "जीवाणुओं की कोशिका भित्ति पेप्टिडोग्लाइकन (Peptidoglycan) से बनी होती है। कवक में काइटिन और पौधों में सेलुलोज होता है।"
    },
    {
        "q": "In animal cells, secretory vesicles are pinched off from which face of the Golgi apparatus?",
        "q_hi": "जंतु कोशिकाओं में, स्रावी पुटिकाएं (secretory vesicles) गोल्जी उपकरण के किस फलक (face) से अलग होती हैं?",
        "opts": ["Cis face", "Trans face", "Proximal face", "Forming face"],
        "opts_hi": ["सिस फेस (Cis face)", "ट्रांस फेस (Trans face)", "समीपस्थ फलक", "निर्माण फलक"],
        "ans": 1,
        "sol": "Proteins enter the Golgi from ER at the Cis face (forming face) and exit packaged in vesicles from the Trans face (maturing face).",
        "sol_hi": "प्रोटीन गोल्जी के सिस फेस (Cis face) पर प्रवेश करते हैं और रासायनिक बदलावों के बाद ट्रांस फेस (Trans face) से पुटिकाओं के रूप में बाहर निकलते हैं।"
    },
    {
        "q": "During cell division, nucleolus and nuclear membrane completely disappear in which phase?",
        "q_hi": "कोशिका विभाजन के दौरान, केंद्रिका और केंद्रक झिल्ली किस चरण में पूरी तरह से विलुप्त हो जाते हैं?",
        "opts": ["Late Prophase", "Metaphase", "Early Anaphase", "Telophase"],
        "opts_hi": ["लेट प्रोफेज (Late Prophase)", "मेटाफेज", "अर्ली एनाफेज", "टीलोफेज"],
        "ans": 0,
        "sol": "By the end of Prophase (Late Prophase), the nucleolus disintegrates, and the nuclear envelope breaks down completely, allowing spindles to access chromosomes.",
        "sol_hi": "प्रोफेज के अंत (Late Prophase) तक, केंद्रिका विघटित हो जाती है और केंद्रक झिल्ली पूरी तरह से टूट जाती है, जिससे तर्कु तंतु गुणसूत्रों तक पहुँच पाते हैं।"
    },
    {
        "q": "Mitotic division is absent in which of the following tissues in adult humans?",
        "q_hi": "वयस्क मनुष्यों में निम्नलिखित में से किस ऊतक में समसूत्री विभाजन अनुपस्थित होता है?",
        "opts": ["Skin epithelial cells", "Bone marrow cells", "Nerve cells / Neurons", "Liver cells"],
        "opts_hi": ["त्वचा उपकला कोशिकाएं", "अस्थि मज्जा कोशिकाएं", "तंत्रिका कोशिकाएं / न्यूरॉन्स", "यकृत कोशिकाएं"],
        "ans": 2,
        "sol": "Mature neurons in adult humans enter a permanent G0 phase and lose their centrioles, making them incapable of mitotic division.",
        "sol_hi": "वयस्क मनुष्यों में परिपक्व न्यूरॉन्स स्थायी G0 चरण में प्रवेश कर जाते हैं और इनमें सेंट्रीओल्स नहीं होते, जिससे इनमें समसूत्री विभाजन नहीं हो पाता।"
    },
    {
        "q": "Which type of chromosome is represented by a V-shape during anaphase movement?",
        "q_hi": "एनाफेज गति के दौरान V-आकार द्वारा किस प्रकार के गुणसूत्र को दर्शाया जाता है?",
        "opts": ["Metacentric", "Sub-metacentric", "Acrocentric", "Telocentric"],
        "opts_hi": ["मध्यकेंद्री (Metacentric)", "उप-मध्यकेंद्री", "अग्रकेंद्री", "अंतकेंद्री"],
        "ans": 0,
        "sol": "Metacentric chromosomes have equal arms. When pulled from the centromere during anaphase, the arms drag behind to form a symmetric V-shape.",
        "sol_hi": "मध्यकेंद्री (Metacentric) गुणसूत्रों में बराबर भुजाएं होती हैं। एनाफेज के दौरान खींचे जाने पर ये दोनों भुजाएं V-आकार बनाती हैं।"
    },
    {
        "q": "The chromosome pairing synapsis in meiosis I leads to the formation of a structure termed:",
        "q_hi": "अर्धसूत्रीविभाजन I में गुणसूत्र युग्मन सूत्रयुग्मन (synapsis) से बनने वाली संरचना को क्या कहा जाता है?",
        "opts": ["Univalent", "Bivalent / Tetrad", "Sister chromatid", "Kinetochore"],
        "opts_hi": ["एकयुजी", "द्वियुजी / टेट्राड (Bivalent)", "सिस्टर क्रोमैटिड", "काइनेटोकोर"],
        "ans": 1,
        "sol": "Synapsis results in homologous pairs aligning alongside each other. This paired structure is called a Bivalent (refers to the two chromosomes) or a Tetrad (refers to the four chromatids).",
        "sol_hi": "सूत्रयुग्मन के परिणामस्वरूप समजात गुणसूत्रों के जोड़े बनते हैं। इस युग्मित संरचना को द्वियुजी (Bivalent) या टेट्राड कहा जाता है।"
    },
    {
        "q": "The fluid portion of cytoplasm excluding organelles is called:",
        "q_hi": "कोशिकांगों को छोड़कर कोशिकाद्रव्य का तरल भाग क्या कहलाता है?",
        "opts": ["Protoplasm", "Cytosol", "Nucleoplasm", "Tonoplasm"],
        "opts_hi": ["जीवद्रव्य", "साइटोसोल (Cytosol)", "केंद्रकद्रव्य", "टोनोप्लाज्म"],
        "ans": 1,
        "sol": "Cytosol is the soluble, fluid phase of the cytoplasm surrounding the organelles. Cytoplasm includes both cytosol and suspended organelles.",
        "sol_hi": "साइटोसोल (Cytosol) कोशिकांगों को छोड़कर कोशिकाद्रव्य का घुलनशील, तरल भाग होता है। जबकि कोशिकाद्रव्य में साइटोसोल और कोशिकांग दोनों आते हैं।"
    },
    {
        "q": "Which cell organelle is active in synthesising cell wall carbohydrates like pectin and hemicellulose?",
        "q_hi": "पेक्टिन और हेमीसेलुलोज जैसे कोशिका भित्ति कार्बोहाइड्रेट के संश्लेषण में कौन सा कोशिकांग सक्रिय है?",
        "opts": ["Chloroplast", "Golgi Apparatus", "Mitochondria", "Ribosome"],
        "opts_hi": ["क्लोरोप्लास्ट", "गोल्जी उपकरण (Golgi Apparatus)", "माइटोकॉन्ड्रिया", "राइबोसोम"],
        "ans": 1,
        "sol": "The Golgi apparatus is the site where non-cellulose cell wall polysaccharides (like pectin and hemicellulose) are synthesized and packaged for transport to the cell plate.",
        "sol_hi": "गोल्जी उपकरण (Golgi apparatus) वह स्थान है जहाँ पेक्टिन और हेमीसेलुलोज जैसे गैर-सेलुलोज कार्बोहाइड्रेट का संश्लेषण और पैकेजिंग होती है।"
    }
]

practice_questions.extend(extra_pqs)

# ----------------- 15 MOCK TEST QUESTIONS (BILINGUAL) -----------------
mock_test_questions = [
    {
        "q": "Who proposed the Cell Theory stating all living cells are composed of cells?",
        "q_hi": "किसने कोशिका सिद्धांत प्रस्तावित किया था कि सभी जीवित जीव कोशिकाओं से बने हैं?",
        "opts": ["Robert Hooke and Robert Brown", "Schleiden and Schwann", "Watson and Crick", "Darwin and Mendel"],
        "opts_hi": ["रॉबर्ट हुक और रॉबर्ट ब्राउन", "श्लाइडेन और श्वान (Schleiden & Schwann)", "वाटसन और क्रिक", "डार्विन और मेंडेल"],
        "ans": 1,
        "sol": "Matthias Schleiden (botanist, 1838) and Theodore Schwann (zoologist, 1839) jointly proposed the Cell Theory.",
        "sol_hi": "मैथियास श्लाइडेन (वनस्पतिशास्त्री, 1838) और थियोडोर श्वान (जंतु वैज्ञानिक, 1839) ने संयुक्त रूप से कोशिका सिद्धांत का प्रस्ताव रखा था।"
    },
    {
        "q": "Which organelle is referred to as the 'Kitchen of the Cell'?",
        "q_hi": "किस कोशिकांग को 'कोशिका की रसोई' कहा जाता है?",
        "opts": ["Mitochondria", "Golgi body", "Chloroplast", "Endoplasmic Reticulum"],
        "opts_hi": ["माइटोकॉन्ड्रिया", "गोल्जी काय", "क्लोरोप्लास्ट (Chloroplast)", "अंतःप्रद्रव्यी जालिका"],
        "ans": 2,
        "sol": "Chloroplasts are called the kitchen of the cell because they synthesize glucose (food) through photosynthesis using sunlight, carbon dioxide, and water.",
        "sol_hi": "क्लोरोप्लास्ट को कोशिका की रसोई कहा जाता है क्योंकि वे सूर्य के प्रकाश, कार्बन डाइऑक्साइड और पानी का उपयोग करके प्रकाश संश्लेषण के माध्यम से ग्लूकोज (भोजन) का निर्माण करते हैं।"
    },
    {
        "q": "Which organelle synthesizes proteins and is the smallest organelle in the cell?",
        "q_hi": "कौन सा कोशिकांग प्रोटीन का संश्लेषण करता है और कोशिका का सबसे छोटा कोशिकांग है?",
        "opts": ["Lysosome", "Ribosome", "Centrosome", "Peroxisome"],
        "opts_hi": ["लाइसोसोम", "राइबोसोम (Ribosome)", "तारककाय", "परऑक्सीसोम"],
        "ans": 1,
        "sol": "Ribosomes are the site of protein synthesis. They are the smallest, non-membranous cell organelles, measuring about 20 nm.",
        "sol_hi": "राइबोसोम प्रोटीन संश्लेषण के स्थल हैं। वे लगभग 20 नैनोमीटर आकार वाले कोशिका के सबसे छोटे, झिल्ली रहित कोशिकांग हैं।"
    },
    {
        "q": "The membrane surrounding the vacuole in a plant cell is:",
        "q_hi": "पादप कोशिका में रिक्तिका (vacuole) को घेरने वाली झिल्ली होती है:",
        "opts": ["Tonoplast", "Plasma membrane", "Cell Wall", "Nuclear membrane"],
        "opts_hi": ["टोनोप्लास्ट (Tonoplast)", "प्लाज्मा झिल्ली", "कोशिका भित्ति", "केंद्रक झिल्ली"],
        "ans": 0,
        "sol": "The central vacuole in plant cells is bounded by a single semi-permeable membrane called the Tonoplast.",
        "sol_hi": "पादप कोशिकाओं में बड़ी केंद्रीय रिक्तिका एक एकल अर्ध-पारगम्य झिल्ली से घिरी होती है जिसे टोनोप्लास्ट कहा जाता है।"
    },
    {
        "q": "Crossing over occurs during which phase of Meiosis Prophase I?",
        "q_hi": "जीन विनिमय (Crossing over) अर्धसूत्रीविभाजन प्रोफेज I के किस चरण में होता है?",
        "opts": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        "opts_hi": ["लेप्टोटीन", "जायगोटीन", "पैकीटीन (Pachytene)", "डिप्लोटीन"],
        "ans": 2,
        "sol": "Crossing over (exchange of genetic segments between homologous chromosomes) takes place during the Pachytene stage, mediated by the recombinase enzyme.",
        "sol_hi": "जीन विनिमय (समजात गुणसूत्रों के बीच आनुवंशिक टुकड़ों का आदान-प्रदान) पैकीटीन चरण के दौरान होता है, जो रिकॉम्बिनेज एंजाइम द्वारा संचालित होता है।"
    },
    {
        "q": "Which chromosome has centromere at the center dividing it into two equal arms?",
        "q_hi": "किस गुणसूत्र का सेंट्रोमियर बिल्कुल केंद्र में होता है जो इसे दो बराबर भुजाओं में विभाजित करता है?",
        "opts": ["Metacentric", "Sub-metacentric", "Acrocentric", "Telocentric"],
        "opts_hi": ["मध्यकेंद्री (Metacentric)", "उप-मध्यकेंद्री", "अग्रकेंद्री", "अंतकेंद्री"],
        "ans": 0,
        "sol": "Metacentric chromosomes have a centrally located centromere, creating two equal-sized arms (p-arm and q-arm).",
        "sol_hi": "मध्यकेंद्री (Metacentric) गुणसूत्रों में सेंट्रोमियर बीच में होता है, जिससे दो समान आकार की भुजाएं (p और q भुजाएं) बनती हैं।"
    },
    {
        "q": "Which organelle packages proteins and is also called the 'Director of Macromolecular Traffic'?",
        "q_hi": "कौन सा कोशिकांग प्रोटीनों की पैकेजिंग करता है और उसे 'मैक्रोमोलेक्यूलर ट्रैफिक का निदेशक' भी कहा जाता है?",
        "opts": ["Mitochondria", "Golgi Apparatus", "Lysosome", "Centrosome"],
        "opts_hi": ["माइटोकॉन्ड्रिया", "गोल्जी उपकरण (Golgi Apparatus)", "लाइसोसोम", "तारककाय"],
        "ans": 1,
        "sol": "The Golgi Apparatus packages, processes, and targets macromolecules to their destinations, earning it the title 'Director of Macromolecular Traffic'.",
        "sol_hi": "गोल्जी उपकरण (Golgi Apparatus) मैक्रोमोलेक्यूल्स की पैकेजिंग, प्रसंस्करण और उन्हें उनके गंतव्य तक भेजने का कार्य करता है, इसलिए इसे यह उपाधि दी गई है।"
    },
    {
        "q": "Which stage of mitosis is studied for chromosome count and karyotype analysis?",
        "q_hi": "गुणसूत्र संख्या और कैरियोटाइप विश्लेषण के लिए समसूत्री विभाजन के किस चरण का अध्ययन किया जाता है?",
        "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "opts_hi": ["प्रोफेज", "मेटाफेज (Metaphase)", "एनाफेज", "टीलोफेज"],
        "ans": 1,
        "sol": "Metaphase is chosen because chromosomes are aligned at the equator and are in their most condensed state, allowing clear counting and visualization.",
        "sol_hi": "मेटाफेज को इसलिए चुना जाता है क्योंकि इस दौरान गुणसूत्र भूमध्य रेखा पर संरेखित होते हैं और अपने सबसे अधिक संघनित रूप में होते हैं, जिससे उन्हें स्पष्ट देखना संभव होता है।"
    },
    {
        "q": "Which of the following cellular structures is absent in mammalian mature Red Blood Cells (RBCs)?",
        "q_hi": "स्तनधारियों की परिपक्व लाल रक्त कोशिकाओं (RBCs) में निम्नलिखित में से कौन सी कोशिकीय संरचना अनुपस्थित होती है?",
        "opts": ["Cell Membrane", "Cytoplasm", "Nucleus", "Hemoglobin"],
        "opts_hi": ["कोशिका झिल्ली", "कोशिकाद्रव्य", "केंद्रक (Nucleus)", "हीमोग्लोबिन"],
        "ans": 2,
        "sol": "Mature mammalian RBCs lack a nucleus (and other organelles like mitochondria) to accommodate more hemoglobin and carry oxygen efficiently.",
        "sol_hi": "स्तनधारियों की परिपक्व लाल रक्त कोशिकाओं (RBCs) में केंद्रक (Nucleus) नहीं होता है ताकि वे हीमोग्लोबिन के लिए अधिक स्थान बना सकें और ऑक्सीजन का कुशलतापूर्वक परिवहन कर सकें।"
    },
    {
        "q": "The cell wall of fungi is chemically composed of:",
        "q_hi": "कवक की कोशिका भित्ति रासायनिक रूप से किससे बनी होती है?",
        "opts": ["Cellulose", "Peptidoglycan", "Chitin", "Lignin"],
        "opts_hi": ["सेलुलोज", "पेप्टिडोग्लाइकन", "काइटिन (Chitin)", "लिग्निन"],
        "ans": 2,
        "sol": "Fungal cell walls are composed of Chitin, which is a polymer of N-acetylglucosamine. Plant walls contain cellulose.",
        "sol_hi": "कवक की कोशिका भित्ति काइटिन (Chitin) से बनी होती है, जबकि पौधों की कोशिका भित्ति में सेलुलोज होता है।"
    },
    {
        "q": "In which stage of Meiosis Prophase I does chromosome pairing (synapsis) occur?",
        "q_hi": "अर्धसूत्रीविभाजन प्रोफेज I के किस चरण में गुणसूत्र युग्मन (synapsis) होता है?",
        "opts": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"],
        "opts_hi": ["लेप्टोटीन", "जायगोटीन (Zygotene)", "पैकीटीन", "डिप्लोटीन"],
        "ans": 1,
        "sol": "Synapsis (pairing of homologous chromosomes) occurs during the Zygotene stage, forming a bivalent structure.",
        "sol_hi": "सूत्रयुग्मन या सायनेप्सिस (समजात गुणसूत्रों की जोड़ी बनना) जायगोटीन चरण के दौरान होता है।"
    },
    {
        "q": "Which of the following organelles is known as the 'Suicidal Bag' of the cell?",
        "q_hi": "निम्नलिखित में से किस कोशिकांग को कोशिका की 'आत्मघाती थैली' कहा जाता है?",
        "opts": ["Lysosome", "Centrosome", "Vacuole", "Ribosome"],
        "opts_hi": ["लाइसोसोम (Lysosome)", "तारककाय", "रिक्तिका", "राइबोसोम"],
        "ans": 0,
        "sol": "Lysosomes are known as suicidal bags because they contain hydrolytic digestive enzymes that can digest the cell if it gets damaged or undergoes autolysis.",
        "sol_hi": "लाइसोसोम को आत्मघाती थैली कहा जाता है क्योंकि इनमें जल-अपघटकीय पाचक एंजाइम होते हैं जो कोशिका के क्षतिग्रस्त होने पर उसे नष्ट कर सकते हैं।"
    },
    {
        "q": "The shortest phase of mitosis is:",
        "q_hi": "समसूत्री विभाजन का सबसे छोटा चरण कौन सा है?",
        "opts": ["Prophase", "Metaphase", "Anaphase", "Telophase"],
        "opts_hi": ["प्रोफेज", "मेटाफेज", "एनाफेज (Anaphase)", "टीलोफेज"],
        "ans": 2,
        "sol": "Anaphase is the shortest phase of mitosis, during which chromosomes split at the centromere and migrate to opposite poles.",
        "sol_hi": "एनाफेज समसूत्री विभाजन का सबसे छोटा चरण है, जिसके दौरान गुणसूत्र सेंट्रोमियर पर विभाजित होते हैं और विपरीत ध्रुवों की ओर खिंचते हैं।"
    },
    {
        "q": "Which organelle is semi-autonomous and inherits maternally?",
        "q_hi": "कौन सा कोशिकांग अर्ध-स्वायत्त है और मातृ रूप से वंशागत (inherit) होता है?",
        "opts": ["Ribosome", "Mitochondria", "Lysosome", "Golgi body"],
        "opts_hi": ["राइबोसोम", "माइटोकॉन्ड्रिया (Mitochondria)", "लाइसोसोम", "गोल्जी काय"],
        "ans": 1,
        "sol": "Mitochondria have their own circular DNA and 70S ribosomes (semi-autonomous) and are inherited only from the mother's egg cell.",
        "sol_hi": "माइटोकॉन्ड्रिया में अपना स्वयं का गोलाकार डीएनए और 70S राइबोसोम होता है तथा यह केवल माता के अंडे से ही संतान में स्थानांतरित होता है।"
    },
    {
        "q": "The Fluid Mosaic Model of the cell membrane was proposed by Singer and Nicolson in which year?",
        "q_hi": "सिंगर और निकोलसन द्वारा कोशिका झिल्ली का 'फ्लुइड मोज़ेक मॉडल' किस वर्ष प्रस्तावित किया गया था?",
        "opts": ["1953", "1972", "1985", "1965"],
        "opts_hi": ["1953", "1972 (1972)", "1985", "1965"],
        "ans": 1,
        "sol": "S.J. Singer and G.L. Nicolson proposed the Fluid Mosaic Model of the biological membrane in 1972.",
        "sol_hi": "एस.जे. सिंगर और जी.एल. निकोलसन ने 1972 में जैविक झिल्ली के 'फ्लुइड मोज़ेक मॉडल' का प्रस्ताव दिया था।"
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
        "deepDive": {
            "title": f"{TOPIC_DISPLAY} Core Study Notes",
            "description": "Thoroughly review cell discovery milestones, organelles and their vital functions, chromosome types, and comparison of cell division pathways.",
            "sections": deep_dive_en
        }
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Cell Theory & Eukaryotic vs Prokaryotic Basics",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which of the following lacks a cellular structure?", "opts": ["Bacteria", "Virus", "Amoeba", "Yeast"], "ans": 1, "sol": "Viruses are acellular (lacking cellular structure) and behave as particles outside host cells."},
                    {"type": "True/False", "q": "True or False: Mycoplasma has a peptidoglycan cell wall.", "ans": False, "sol": "False. Mycoplasma is unique among bacteria because it completely lacks a cell wall."},
                    {"type": "Fill in the Blank", "q": "The phrase 'Omnis cellula e cellula' was coined by Rudolf ________.", "ans": "Virchow", "sol": "Rudolf Virchow added the cell lineage concept to Cell Theory in 1855."}
                ]
            },
            {
                "title": "2. Cell Organelles & Specialized Functions",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which organelle is the site of cellular protein factories?", "opts": ["Nucleus", "Ribosome", "Mitochondria", "Lysosome"], "ans": 1, "sol": "Ribosomes are protein factories of the cell, translating mRNA into polypeptide chains."},
                    {"type": "True/False", "q": "True or False: Chloroplasts and Mitochondria contain 70S ribosomes.", "ans": True, "sol": "True. Both organelles have bacterial ancestry and contain 70S ribosomes and circular DNA."},
                    {"type": "Fill in the Blank", "q": "The single membrane bounding the plant vacuole is the ________.", "ans": "Tonoplast", "sol": "The tonoplast regulates molecular transport between cytoplasm and plant vacuole."}
                ]
            },
            {
                "title": "3. Chromosome Anatomy & Cell Division",
                "masteryZone": [
                    {"type": "MCQ", "q": "During Meiosis, crossing over occurs in which stage?", "opts": ["Leptotene", "Zygotene", "Pachytene", "Diplotene"], "ans": 2, "sol": "Crossing over (homologous recombination) takes place during the Pachytene stage of Prophase I."},
                    {"type": "True/False", "q": "True or False: Acrocentric chromosomes form a V-shape during anaphase.", "ans": False, "sol": "False. Metacentric chromosomes form a V-shape. Acrocentric chromosomes form a J-shape."},
                    {"type": "Fill in the Blank", "q": "The shortest stage of mitotic division is ________.", "ans": "Anaphase", "sol": "Anaphase is the shortest stage of mitosis, lasting only a few minutes."}
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
        "deepDive": {
            "title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स",
            "description": "कोशिका खोज के चरणों, कोशिकांगों और उनके कार्यों, गुणसूत्रों के प्रकार और कोशिका विभाजन की प्रक्रियाओं का विस्तृत अध्ययन करें।",
            "sections": deep_dive_hi
        }
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
                "title": "1. कोशिका सिद्धांत और प्रोकैरियोटिक बनाम यूकैरियोटिक आधार",
                "masteryZone": [
                    {"type": "MCQ", "q": "निम्नलिखित में से किसमें कोशिकीय संरचना का अभाव होता है?", "opts": ["जीवाणु", "विषाणु (Virus)", "अमीबा", "खमीर (Yeast)"], "ans": 1, "sol": "विषाणु (Viruses) अकोशकीय होते हैं, जिनमें कोई कोशिकीय संरचना नहीं होती।"},
                    {"type": "True/False", "q": "सही या गलत: माइकोप्लाज्मा में पेप्टिडोग्लाइकन की कोशिका भित्ति होती है।", "ans": False, "sol": "गलत। जीवाणुओं में माइकोप्लाज्मा अद्वितीय है क्योंकि इसमें कोशिका भित्ति का पूर्ण अभाव होता है।"},
                    {"type": "Fill in the Blank", "q": "'ओमनिस सेलुला ई सेलुला' कथन रुडोल्फ __________ द्वारा दिया गया था।", "ans": "विरचो", "sol": "रुडोल्फ विरचो ने 1855 में कोशिका सिद्धांत में यह जोड़ा था।"}
                ]
            },
            {
                "title": "2. कोशिकांग और उनके विशिष्ट कार्य",
                "masteryZone": [
                    {"type": "MCQ", "q": "कौन सा कोशिकांग कोशिका के प्रोटीन कारखाने के रूप में जाना जाता है?", "opts": ["केंद्रक", "राइबोसोम (Ribosome)", "माइटोकॉन्ड्रिया", "लाइसोसोम"], "ans": 1, "sol": "राइबोसोम प्रोटीन कारखाने हैं जो mRNA का अनुवाद कर प्रोटीन बनाते हैं।"},
                    {"type": "True/False", "q": "सही या गलत: क्लोरोप्लास्ट और माइटोकॉन्ड्रिया में 70S राइबोसोम होते हैं।", "ans": True, "sol": "सही। दोनों कोशिकांगों में जीवाणु जैसी विशेषताएं होती हैं जिनमें 70S राइबोसोम और गोलाकार डीएनए होता है।"},
                    {"type": "Fill in the Blank", "q": "पादप रिक्तिका को घेरने वाली एकल झिल्ली __________ कहलाती है।", "ans": "टोनोप्लास्ट", "sol": "टोनोप्लास्ट रिक्तिका और कोशिकाद्रव्य के बीच अणुओं के परिवहन को नियंत्रित करती है।"}
                ]
            },
            {
                "title": "3. गुणसूत्र संरचना और कोशिका विभाजन",
                "masteryZone": [
                    {"type": "MCQ", "q": "अर्धसूत्रीविभाजन के दौरान जीन विनिमय (crossing over) किस चरण में होता है?", "opts": ["लेप्टोटीन", "जायगोटीन", "पैकीटीन (Pachytene)", "डिप्लोटीन"], "ans": 2, "sol": "जीन विनिमय प्रोफेज I की पैकीटीन (Pachytene) अवस्था के दौरान समजात गुणसूत्रों के बीच होता है।"},
                    {"type": "True/False", "q": "सही या गलत: अग्रकेंद्री (Acrocentric) गुणसूत्र एनाफेज में V-आकार बनाते हैं।", "ans": False, "sol": "गलत। मध्यकेंद्री (Metacentric) गुणसूत्र V-आकार बनाते हैं, जबकि अग्रकेंद्री J-आकार बनाते हैं।"},
                    {"type": "Fill in the Blank", "q": "समसूत्री विभाजन की सबसे छोटी अवस्था __________ है।", "ans": "एनाफेज", "sol": "एनाफेज समसूत्री विभाजन की सबसे छोटी अवस्था है जो कुछ ही मिनट चलती है।"}
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
