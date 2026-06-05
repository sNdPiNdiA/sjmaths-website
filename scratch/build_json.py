import json
import os

# Define folders
ENG_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Phases-of-Evolution-of-Harappan-Civilisation"
HIN_DIR = os.path.join(ENG_DIR, "hi")

# Ensure folders exist
os.makedirs(ENG_DIR, exist_ok=True)
os.makedirs(HIN_DIR, exist_ok=True)

# ----------------- ENGLISH DATA -----------------
eng_data = {
  "breadcrumbs": {
    "parent": "UPSC Syllabus",
    "parentUrl": "/upsc/",
    "current": "Phases of Evolution of Harappan Civilisation"
  },
  "hero": {
    "title": "Phases of Evolution of Harappan Civilisation",
    "description": "Master the evolutionary trajectory of the Indus Valley Civilisation, detailing the Pre-Harappan village cultures, Early Harappan proto-urban transitions, Mature Harappan peak urbanization, and Late Harappan post-urban rural adaptations for UPSC GS-1."
  },
  "labels": {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
      "title": "Interactive UPSC Mock Test",
      "description": "Test your knowledge on the Phases of Evolution of Harappan Civilisation. This timed test contains 10 high-quality, exam-standard questions with negative marking. Perfect for self-evaluation.",
      "startBtn": "Start Mock Test"
    },
    "mockPlay": {
      "prevBtn": "Previous Question",
      "nextBtn": "Next Question",
      "submitBtn": "Submit Test"
    }
  },
  "timeline": {
    "title": "The Evolutionary Horizon of Harappan Civilisation",
    "description": "Click on each phase card to explore the transition from chalcolithic rural roots to planned cities and eventual post-urban dispersion.",
    "cards": [
      {
        "period": "Pre & Early Harappan Phase",
        "date": "c. 3300 BCE – 2600 BCE",
        "details": "<strong>Emergence & Foundation</strong>: Gradual transition from Neolithic Mehrgarh to sedentary chalcolithic pastoralist villages.<br><br><strong>Key Characteristics</strong>: Emergence of defensive fortifications, specialized crafts (bead-making, metalworking), standardization of wheel-made pottery (Hakra and Ravi ware), and localized trade networks. Significant sites include Kot Diji, Kalibangan, Amri, and Bhirrana."
      },
      {
        "period": "Mature Harappan Phase",
        "date": "c. 2600 BCE – 1900 BCE",
        "details": "<strong>Urban Revolution</strong>: Complete consolidation of pan-regional integration, civic planning, and trade surplus.<br><br><strong>Key Characteristics</strong>: Standardized grid-planned cities, monumental baked-brick structures (Great Bath, Granaries), advanced drainage systems, writing/script, uniform weights and measures (16-binary system), long-distance trade with Mesopotamia (Meluhha trade), and high-quality bronze/steatite art. Core sites: Harappa, Mohenjo-daro, Rakhigarhi, Dholavira, and Lothal."
      },
      {
        "period": "Late Harappan Phase",
        "date": "c. 1900 BCE – 1300 BCE",
        "details": "<strong>Post-Urban Regression</strong>: Civic decay, de-urbanization, and regional fragmentation.<br><br><strong>Key Characteristics</strong>: Loss of systemic standardization (script, seal, weights), disappearance of long-distance foreign trade, replacement of large cities by small farming hamlets. Localized ceramic adaptations emerge, such as the Cemetery H, Jhukar, and Lustrous Red Ware cultures. Sites include Jhukar, Rangpur, Rojdi, and Daimabad."
      }
    ]
  },
  "mnemonics": {
    "title": "Mnemonics & Quick Memory Tricks",
    "description": "Use these visual phrases to recall the classification of sites into evolutionary phases for the UPSC Civil Services Examination.",
    "items": [
      {
        "title": "Mnemonic 1: Early Harappan Fortified Sites",
        "phrase": "\"K-B-A-K (Kabak / Crown) - The Early Fortified Pillars\"",
        "decryption": "**K**ot Diji, **B**anawali, **A**mri, and **K**alibangan (**KBAK**) represent the major Early Harappan sites that developed early fortifications, paving the way for Mature urbanization."
      },
      {
        "title": "Mnemonic 2: Late Harappan Regional Sub-Cultures",
        "phrase": "\"J-C-L (Junior College Lecture) Late Phases\"",
        "decryption": "**J**hukar Culture (Sindh), **C**emetery H (Punjab), and **L**ustrous Red Ware (Gujarat) (**JCL**) represent the distinct regional cultures of the Late Harappan post-urban phase."
      },
      {
        "title": "Mnemonic 3: Mature Harappan Metropolises",
        "phrase": "\"H-M-R-D-L (How Many Rupees Did Lothal make?)\"",
        "decryption": "**H**arappa, **M**ohenjo-daro, **R**akhigarhi, **D**holavira, and **L**othal (**HMRDL**) are the five principal mature metropolises showing high-order civic planning and monumental structures."
      }
    ]
  },
  "traps": {
    "title": "UPSC Common Exam Traps to Avoid",
    "items": [
      "<strong>Trap 1: The 'Sudden Birth' Fallacy:</strong> UPSC statements may claim the Harappan Civilisation sprang up suddenly without local roots. **False.** It was a gradual, indigenous evolution from Neolithic pastoral communities (like Mehrgarh) to Early Harappan chalcolithic stages, before maturing into planned urban centers.",
      "<strong>Trap 2: Mixing Site Phase Exclusivity:</strong> Do not assume a site belonged to only one phase. Sites like **Dholavira, Rakhigarhi, Kalibangan, Harappa, and Mohenjo-daro** show continuous occupation across all three phases (Early, Mature, and Late), whereas sites like Kot Diji (mostly Early) or Jhukar (purely Late) are specific phase markers.",
      "<strong>Trap 3: Iron & Metallurgy Misconceptions:</strong> Do not confuse late-phase bronze and copper technology with Iron. The entire Harappan trajectory (including Late Harappan) was **strictly pre-Iron**; iron makes its appearance in India much later during the Late Vedic period (c. 1000 BCE).",
      "<strong>Trap 4: The 'Decline' vs 'Extinction' Trap:</strong> The Late Harappan phase represents the **decline of urban infrastructure (de-urbanization)**, not the complete extinction of the population. People migrated eastward and southward, reverting to rural agricultural lives."
    ]
  },
  "deepDive": {
    "title": "Syllabus Core Study Notes (Deep-Dive)",
    "description": "Master the evolutionary trajectory, key features, stratigraphy, and academic theories of the Harappan Civilisation.",
    "sections": [
      {
        "title": "1. The Early Harappan Phase (c. 3300 BCE – 2600 BCE)",
        "content": "<p>The Early Harappan phase represents the formative, proto-urban stage of the civilization. It is characterized by the consolidation of agricultural village economies, early metallurgy, and regional trade connections. It is also known as the <strong>Regionalisation Era</strong>.</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-seedling\"></i> Hakra & Ravi Phases</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      The earliest prelude is the <strong>Hakra Ware Phase</strong> (c. 3800-3200 BCE), identified in the Ghaggar-Hakra valley (e.g., Bhirrana, Kunal). It is followed by the <strong>Ravi Phase</strong> (c. 3300-2800 BCE) at Harappa, marked by early wheel-made pottery, script-like graffiti, and bead making.\n    </p>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-shield-halved\"></i> Proto-Urban Characteristics</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>Fortifications:</strong> Defensive walls at Kot Diji and Kalibangan protecting settlements.</li>\n      <li><strong>Standardization:</strong> Emergence of uniform pottery styles (Kot Diji style) and early brick ratios (1:2:3 or 1:2:4).</li>\n      <li><strong>Specialization:</strong> Early metal works (bronze and copper) and shell manufacturing.</li>\n    </ul>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Key Sites and Features:</h4>\n<table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\">\n  <thead>\n    <tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\">\n      <th style=\"padding: 0.5rem; text-align: left;\">Site</th>\n      <th style=\"padding: 0.5rem; text-align: left;\">Key Early Harappan Evidence</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Bhirrana</td>\n      <td style=\"padding: 0.5rem;\">Oldest Harappan site yielding Hakra Ware, animal bones, and early multi-room houses.</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Kot Diji</td>\n      <td style=\"padding: 0.5rem;\">Massive defensive wall, wheel-made pottery with horned deity motifs, and a destruction layer indicating transition.</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Kalibangan</td>\n      <td style=\"padding: 0.5rem;\">A distinct pre-Harappan agricultural field showing criss-cross ploughed furrows.</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">Kunal</td>\n      <td style=\"padding: 0.5rem;\">Pre-Harappan silver crowns and necklaces, indicating early social stratification.</td>\n    </tr>\n  </tbody>\n</table>",
        "masteryZone": [
          {
            "type": "MCQ",
            "q": "Which of the following sites represents the earliest Hakra Ware phase of the Harappan evolution?",
            "opts": [
              "Bhirrana",
              "Mohenjo-daro",
              "Lothal",
              "Chanhudaro"
            ],
            "ans": 0,
            "sol": "Bhirrana in Haryana represents the oldest Hakra Ware phase (dating back to the 4th millennium BCE)."
          },
          {
            "type": "MCQ",
            "q": "The famous pre-mature agricultural ploughed field showing criss-cross furrows was discovered at:",
            "opts": [
              "Kalibangan",
              "Banawali",
              "Harappa",
              "Kot Diji"
            ],
            "ans": 0,
            "sol": "Kalibangan in Rajasthan yielded a unique pre-mature (Early Harappan) ploughed agricultural field."
          },
          {
            "type": "Statement-Based",
            "q": "Consider the following statements regarding the Early Harappan phase:\n1. It is also known as the Regionalisation Era of the Indus Valley Civilisation.\n2. The pottery of this era was completely hand-molded and lacked the use of the potter's wheel.\nWhich of the statements given above is/are correct?",
            "opts": [
              "1 only",
              "2 only",
              "Both 1 and 2",
              "Neither 1 nor 2"
            ],
            "ans": 0,
            "sol": "Statement 1 is correct: it represents the Regionalisation Era. Statement 2 is incorrect because the potter's wheel was widely used, leading to standardized wheel-made pottery like Ravi and Kot Diji ware."
          },
          {
            "type": "True/False",
            "q": "True or False: The Hakra Ware phase represents a transition stage that predates the Ravi phase at Harappa.",
            "ans": True,
            "sol": "True. The Hakra phase is older (c. 3800-3200 BCE) than the Ravi phase (c. 3300-2800 BCE)."
          },
          {
            "type": "One-Liner",
            "q": "At which Early Harappan site in Haryana were two silver crowns and gold ornaments discovered?",
            "sol": "Kunal"
          }
        ]
      },
      {
        "title": "2. The Mature Harappan Phase (c. 2600 BCE – 1900 BCE)",
        "content": "<p>The Mature Harappan phase represents the zenith of Indus Valley urbanization. Known as the <strong>Integration Era</strong>, it is marked by complete administrative cohesion, advanced civic planning, standardized technologies, and extensive trade.</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-city\"></i> Urban & Civic Zenith</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>Grid-Planned Settlements:</strong> Main streets running north-south and east-west, intersecting at right angles (grid pattern).</li>\n      <li><strong>Sanitation:</strong> Underground covered drains, soakage jars, and private toilets in homes.</li>\n      <li><strong>Double Division:</strong> Separation into a raised **Citadel** (administrative/religious buildings) and a **Lower Town** (residential quarters).</li>\n    </ul>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-scale-balanced\"></i> Commercial Integration</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      Standardized weight system using binary values (1, 2, 4, 8, 16, 32...) for lower weights and decimal values for higher weights. The ratio of bricks was strictly fixed at 1:2:4 (height:width:length) for all civic structures. Steatite seals and a yet-undeciphered script were used to authenticate commercial shipments to Mesopotamia.\n    </p>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Principal Urban Centers:</h4>\n<ul>\n  <li><strong>Harappa & Mohenjo-daro:</strong> Large dual metropolises of the Indus basin, showing granaries, citadel structures, and standard modular layout.</li>\n  <li><strong>Rakhigarhi (Haryana):</strong> The largest Harappan site in terms of geographic area, serving as a major Ghaggar basin trade hub.</li>\n  <li><strong>Dholavira (Kutch):</strong> Three-tier division (Citadel, Middle Town, Lower Town) and advanced stone water reservoirs.</li>\n  <li><strong>Lothal (Gujarat):</strong> Artificial dockyard connected to the Sabarmati river, bead factory, and double burials.</li>\n</ul>",
        "masteryZone": [
          {
            "type": "MCQ",
            "q": "The Mature Harappan brick dimensions followed a highly standardized ratio of (Thickness : Width : Length):",
            "opts": [
              "1 : 2 : 4",
              "1 : 3 : 9",
              "2 : 4 : 8",
              "1 : 2 : 3"
            ],
            "ans": 0,
            "sol": "The standard ratio of bricks used in the Mature Harappan phase was strictly 1:2:4."
          },
          {
            "type": "Multiple Correct MCQ",
            "q": "Which of the following elements characterize the Mature Harappan civic architecture? (Select all that apply)",
            "opts": [
              "Grid layout of streets intersecting at right angles",
              "Underground covered drainage systems with soak pits",
              "Use of massive stone pillars to support palaces",
              "Separation of settlements into a Citadel and a Lower Town"
            ],
            "ans": [0, 1, 3],
            "sol": "Mature Harappan architecture featured grids, drainage, and division into citadel/lower town. Massive stone pillars were not a feature of Harappan architecture (they appear under the Mauryas)."
          },
          {
            "type": "Match the Following",
            "q": "Match the Mature Harappan site with its unique archaeological discovery:",
            "items": [
              { "left": "I. Lothal", "key": "B" },
              { "left": "II. Dholavira", "key": "A" },
              { "left": "III. Rakhigarhi", "key": "C" }
            ],
            "options": [
              { "val": "A", "text": "A. Stone water reservoirs and three-tier city planning" },
              { "val": "B", "text": "B. Artificial brick dockyard and bead-making factory" },
              { "val": "C", "text": "C. Largest Harappan site by area with multiple granaries" }
            ],
            "sol": "Lothal has the dockyard, Dholavira has the reservoirs/three-tier layout, and Rakhigarhi is the largest site by area."
          },
          {
            "type": "Assertion-Reason",
            "q": "Assertion (A): Long-distance trade between the Harappan Civilisation and Mesopotamia peaked during the Mature phase.\nReason (R): Harappan seals and clay sealings have been excavated at several Mesopotamian sites like Ur, Kish, and Nippur.",
            "opts": [
              "Both A and R are true and R is the correct explanation of A",
              "Both A and R are true but R is not the correct explanation of A",
              "A is true but R is false",
              "A is false but R is true"
            ],
            "ans": 0,
            "sol": "Both A and R are true, and the presence of Harappan seals in Mesopotamia is direct physical proof of the trading relationship."
          }
        ]
      },
      {
        "title": "3. The Late Harappan Phase (c. 1900 BCE – 1300 BCE)",
        "content": "<p>The Late Harappan phase is a period of de-urbanization, civic decay, and regional fragmentation. Known as the <strong>Localisation Era</strong>, it represents the decline of central administrative systems and a shift back to localized, rural agricultural communities.</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-house-chimney-crack\"></i> Civic Decay & Ruralisation</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>Loss of Standards:</strong> Abandonment of grid plans; houses built of reused bricks in a haphazard layout.</li>\n      <li><strong>Disappearance of Tech:</strong> The script, steatite seals, and uniform cubical weights fell out of use.</li>\n      <li><strong>Rural Shift:</strong> Abandonment of great metropolises; population shifted towards small agrarian villages.</li>\n    </ul>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-palette\"></i> Regional Sub-Cultures</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      As integration broke down, distinct regional styles emerged in pottery and burials:\n      <br>• <strong>Cemetery H Culture:</strong> Located in Punjab, showing painted urn burials.\n      <br>• <strong>Jhukar Culture:</strong> Located in Sindh, showing painted pottery and round button seals.\n      <br>• <strong>Lustrous Red Ware:</strong> Located in Gujarat (Rangpur, Rojdi).\n    </p>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Decline Dynamics & Outposts:</h4>\n<ul>\n  <li><strong>Daimabad (Maharashtra):</strong> The southernmost Late Harappan outpost, famous for yielding the Daimabad Bronzes (chariot, bull, elephant).</li>\n  <li><strong>Alamgirpur & Hulas (UP):</strong> The easternmost outposts, showing late phase village cultures with lack of drainage.</li>\n  <li><strong>Bhagwanpura (Haryana):</strong> A key site showing a stratigraphic overlap between Late Harappan levels and the early Painted Grey Ware (PGW) culture.</li>\n</ul>",
        "masteryZone": [
          {
            "type": "MCQ",
            "q": "The Late Harappan phase in Sindh is archaeologically characterized by which localized culture?",
            "opts": [
              "Jhukar Culture",
              "Cemetery H Culture",
              "Malwa Culture",
              "Ahar-Banas Culture"
            ],
            "ans": 0,
            "sol": "The Jhukar culture represents the post-urban, Late Harappan phase in Sindh."
          },
          {
            "type": "Multiple Correct MCQ",
            "q": "What major changes occurred during the transition from Mature to Late Harappan phases? (Select all that apply)",
            "opts": [
              "Disappearance of the Harappan script and steatite seals",
              "Abandonment of the standardized cubical weights and measures",
              "Abandonment of the central municipal drainage system",
              "Introduction of iron tools and weaponry"
            ],
            "ans": [0, 1, 2],
            "sol": "The transition saw the loss of script, seals, standardized weights, and municipal drainage. Iron tools were NOT introduced; iron came to India around 1000 BCE, long after the Harappan Civilisation."
          },
          {
            "type": "One-Liner",
            "q": "Which southernmost outpost of the Harappan civilization yielded a set of four late-phase bronze sculptures, including a chariot?",
            "sol": "Daimabad"
          },
          {
            "type": "Assertion-Reason",
            "q": "Assertion (A): The Late Harappan phase does not represent the sudden, violent extinction of the Indus population.\nReason (R): Stratigraphic sequences show gradual migrations towards the Ganga-Yamuna Doab and Gujarat, adapting to changes in monsoonal rainfall.",
            "opts": [
              "Both A and R are true and R is the correct explanation of A",
              "Both A and R are true but R is not the correct explanation of A",
              "A is true but R is false",
              "A is false but R is true"
            ],
            "ans": 0,
            "sol": "Both A and R are true, and the gradual migration due to climate/monsoon shifts explains why it was a process of ruralisation rather than a sudden violent end."
          }
        ]
      }
    ]
  },
  "flashcards": {
    "title": "Active Recall Flashcards",
    "description": "Flashcards are key to mastering fact-dense UPSC questions. Click on any card below to flip it and reveal the answer.",
    "items": [
      {
        "question": "What is the oldest Harappan site according to the Archaeological Survey of India (ASI)?",
        "answer": "<strong>Bhirrana</strong> in Haryana. It yields early Hakra Ware levels dating back to c. 7500 BCE.",
        "icon": "fa-clock"
      },
      {
        "question": "Which Early Harappan site shows a destruction layer by fire prior to its Mature rebuild?",
        "answer": "<strong>Kot Diji</strong> in Sindh. A massive fire layer separates the Early Harappan Kot Dijian phase from the subsequent Mature Harappan occupation.",
        "icon": "fa-fire"
      },
      {
        "question": "In which phase does the Harappan script make its first organized appearance?",
        "answer": "The <strong>Early Harappan Phase</strong> (specifically during the Ravi Phase, c. 3300-2800 BCE, as potters' marks/graffiti).",
        "icon": "fa-pen-clip"
      },
      {
        "question": "What standard unit of weight was the basis for the Harappan commercial ratio?",
        "answer": "The binary weight unit of <strong>16</strong> (representing 13.63 grams) was the base unit for small transactions.",
        "icon": "fa-scale-balanced"
      },
      {
        "question": "Name the unique Late Harappan outpost situated in Maharashtra.",
        "answer": "<strong>Daimabad</strong> on the Pravara River. It yielded the famous Daimabad Bronzes (a chariot driver, bull, elephant, and rhino).",
        "icon": "fa-location-crosshairs"
      },
      {
        "question": "At which site is there a stratigraphic overlap of Late Harappan and PGW (Vedic) culture?",
        "answer": "<strong>Bhagwanpura</strong> in Haryana. It shows a continuous, overlapping habitation of Late Harappans and Painted Grey Ware (PGW) users.",
        "icon": "fa-layer-group"
      }
    ]
  },
  "practiceQuestions": [
    {
      "q": "Which of the following represents the correct chronological sequence of the developmental phases of the Harappan Civilisation?\n1. Hakra Ware Phase\n2. Ravi Phase\n3. Kot Dijian Phase\n4. Mature Harappan Phase\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 — 2 — 3 — 4",
        "2 — 1 — 3 — 4",
        "1 — 3 — 2 — 4",
        "3 — 1 — 2 — 4"
      ],
      "ans": 0,
      "sol": "The developmental sequence begins with the Hakra Ware phase (c. 3800-3200 BCE), followed by the Ravi phase at Harappa (c. 3300-2800 BCE), the Kot Dijian phase (c. 2800-2600 BCE), and finally the Mature Harappan phase (c. 2600-1900 BCE)."
    },
    {
      "q": "The transition from the Early Harappan to the Mature Harappan phase is marked by which of the following changes?\n1. Transition from rural agricultural settlements to fortified, grid-planned cities.\n2. Replacement of local pottery styles (like Kot Diji ware) by standardized Mature Harappan red-and-black painted pottery.\n3. Disappearance of regional scripts in favor of a standardized Indus script.\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "The transition to the Mature phase is marked by the consolidation of all three features: high urbanization with grid plans, standardized red-and-black pottery, and a unified script across all regions."
    },
    {
      "q": "With reference to the Early Harappan site of Kot Diji, consider the following statements:\n1. It is situated on the left bank of the Indus River opposite Mohenjo-daro.\n2. The site contains a defensive wall protecting the settlement from flood and attacks.\n3. A thick layer of ash and charcoal indicates the site was destroyed by fire before the Mature Harappan occupation.\nWhich of the statements given above are correct?",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "All three statements are correct. Kot Diji (Sindh) shows a clear Early Harappan fortified level, which was burned and then rebuilt as a Mature Harappan settlement."
    },
    {
      "q": "Which of the following sites has yielded evidence of all three phases (Early, Mature, and Late) of the Harappan Civilisation?\n1. Harappa\n2. Rakhigarhi\n3. Dholavira\n4. Kalibangan\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "3 and 4 only",
        "1, 2 and 3 only",
        "1, 2, 3 and 4"
      ],
      "ans": 3,
      "sol": "All four sites—Harappa, Rakhigarhi, Dholavira, and Kalibangan—show complete cultural continuity, preserving levels from the Early, Mature, and Late Harappan phases."
    },
    {
      "q": "The concept of 'Early Harappan' phase was first systematically defined by which archaeologist based on excavations in Pakistan?",
      "opts": [
        "M.R. Mughal",
        "John Marshall",
        "Mortimer Wheeler",
        "Alexander Cunningham"
      ],
      "ans": 0,
      "sol": "Archaeologist Rafique Mughal (M.R. Mughal) systematically defined the 'Early Harappan' phase, particularly through his surveys in Bahawalpur (Cholistan desert) and the Ghaggar-Hakra valley."
    },
    {
      "q": "With reference to the Hakra Ware phase of the Indus Valley Civilisation, which of the following statements is correct?",
      "opts": [
        "It represents the transition from pastoralism to sedentary agriculture in the Ghaggar-Hakra valley.",
        "It is completely absent in the Indian territory.",
        "It belongs to the Late Harappan post-urban phase.",
        "It was characterized by the widespread use of iron metallurgy."
      ],
      "ans": 0,
      "sol": "The Hakra Ware phase represents the earliest chalcolithic farming communities in the Ghaggar-Hakra basin, bridging the Neolithic (Mehrgarh) and Early Harappan periods."
    },
    {
      "q": "The pre-Harappan settlement of Amri in Sindh is famous for yielding which of the following specific archaeological findings?",
      "opts": [
        "Pottery painted with gazelle/antelope motifs",
        "A large stone dockyard",
        "Silver crowns",
        "A bronze statue of a dancing girl"
      ],
      "ans": 0,
      "sol": "Amri is famous for its pre-Harappan levels showing a distinct pottery style painted with gazelles and geometric designs."
    },
    {
      "q": "Which of the following sites is located in the Cholistan region of Pakistan and contains numerous Early Harappan sites?",
      "opts": [
        "Kunal",
        "Amri",
        "Ganweriwala",
        "Jalilpur"
      ],
      "ans": 2,
      "sol": "Ganweriwala is a massive Mature Harappan site in the Cholistan desert, but the Cholistan region itself contains hundreds of Hakra and Early Harappan sites mapped by Rafique Mughal."
    },
    {
      "q": "The pre-mature phase of Kalibangan (Kalibangan-I) is characterized by which of the following features?\n1. A fortress/citadel wall.\n2. Lack of proper drainage system inside the lower town.\n3. Distinctive pottery known as Fabric A to F.\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "All three statements are correct. The pre-mature Kalibangan phase had fortifications, lacked underground brick drains, and yielded the six distinct pottery fabrics classified by B.B. Lal."
    },
    {
      "q": "The 'Ravi Phase' of Harappa (c. 3300-2800 BCE) is primarily known for which of the following developments?",
      "opts": [
        "The first appearance of potters' marks and early scripts on pottery",
        "The construction of the Great Bath",
        "Mesopotamian cylinder seals",
        "Iron plowshares"
      ],
      "ans": 0,
      "sol": "The Ravi Phase represents the earliest occupation level at Harappa, showing the first graffiti marks that later evolved into the Indus script."
    },
    {
      "q": "What was the main reason for the shift from the Early Harappan rural phase to the Mature Harappan urban phase?",
      "opts": [
        "Agricultural surplus due to river silt and flood irrigation, enabling craft specialization",
        "Invasion by nomadic Indo-Aryans",
        "Introduction of canal irrigation networks from Central Asia",
        "Widespread mining of iron ore in Rajasthan"
      ],
      "ans": 0,
      "sol": "The mobilization of agricultural surplus along fertile river floodplains allowed the growth of specialized trade, craft guilds, and administrative classes, triggering urbanization."
    },
    {
      "q": "With reference to the Harappan city of Rakhigarhi, consider the following statements:\n1. It is located in the dry bed of the ancient Drishadvati River in Haryana.\n2. It has yielded evidence of both Early Harappan and Mature Harappan phases.\n3. It is currently recognized as the largest archaeological site of the Indus Valley Civilisation.\nWhich of the statements given above are correct?",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "All three statements are correct. Rakhigarhi is located in Haryana (ancient Drishadvati bed), contains both early and mature levels, and is the largest site by area, surpassing Mohenjo-daro."
    },
    {
      "q": "Which of the following sites has yielded a unique Mature Harappan inscription consisting of ten large-sized symbols (the Dholavira Signboard)?",
      "opts": [
        "Dholavira",
        "Lothal",
        "Harappa",
        "Banawali"
      ],
      "ans": 0,
      "sol": "Dholavira in Gujarat yielded a large wooden board containing ten large gypsum symbols, referred to as the Dholavira Signboard."
    },
    {
      "q": "The urban planning of Mature Harappan cities followed a grid pattern. This implies that:",
      "opts": [
        "Streets ran straight and cut each other at right angles",
        "Houses were built with round rooms and circular walls",
        "Drains were open and ran along the center of the streets",
        "All houses had identical heights and room layouts"
      ],
      "ans": 0,
      "sol": "Grid planning means that major roads intersected at 90-degree angles, creating regular rectangular blocks for housing."
    },
    {
      "q": "Which of the following Mature Harappan sites is famous for its unique three-tier division of the town instead of the typical two-tier division?",
      "opts": [
        "Dholavira",
        "Lothal",
        "Chanhudaro",
        "Rakhigarhi"
      ],
      "ans": 0,
      "sol": "Dholavira is unique because it is divided into three sections: the Citadel (Upper Town), the Middle Town, and the Lower Town."
    },
    {
      "q": "In which Mature Harappan site is there a complete absence of defensive fortifications or a citadel?",
      "opts": [
        "Chanhudaro",
        "Kalibangan",
        "Lothal",
        "Mohenjo-daro"
      ],
      "ans": 0,
      "sol": "Chanhudaro in Sindh is the only major Mature Harappan town without a fortified citadel structure. It was primarily an industrial center."
    },
    {
      "q": "The standardization of Mature Harappan weights and measures is indicated by which of the following evidence?",
      "opts": [
        "Chert cubical weights following a binary system of 1, 2, 4, 8, 16, 32...",
        "Bronze scales marked in millimeters",
        "Terracotta rulers showing uniform inches",
        "Clay tablets containing conversion charts"
      ],
      "ans": 0,
      "sol": "Standardized cubical weights made of polished chert followed a binary ratio for lower weights, with 16 being the standard base unit."
    },
    {
      "q": "The trade relations between Mature Harappan cities and Mesopotamia are mentioned in cuneiform texts. What term is used in Mesopotamian records to refer to the Indus region?",
      "opts": [
        "Meluhha",
        "Dilmun",
        "Magan",
        "Sumer"
      ],
      "ans": 0,
      "sol": "Mesopotamian inscriptions refer to the Indus Valley region as 'Meluhha', while Dilmun refers to Bahrain and Magan refers to Oman."
    },
    {
      "q": "Which of the following was the major source of Lapis Lazuli, a semi-precious blue stone imported by Mature Harappans?",
      "opts": [
        "Shortughai (Afghanistan)",
        "Khetri (Rajasthan)",
        "Badakhshan (Iran)",
        "Lothal (Gujarat)"
      ],
      "ans": 0,
      "sol": "Shortughai in Afghanistan was a Harappan trading colony established near Badakhshan to directly control the mining of Lapis Lazuli."
    },
    {
      "q": "With reference to Mature Harappan religious practices, which of the following is correct?",
      "opts": [
        "Worship of a male deity depicted on seals (proto-Shiva/Pashupati) and mother goddess figurines.",
        "Construction of monumental stone temples dedicated to various gods.",
        "Worship of anthropomorphic representations of Indra and Agni.",
        "Strict practice of cremation without any animal offerings."
      ],
      "ans": 0,
      "sol": "Religion was characterized by seals showing Pashupati, mother goddess clay figurines, tree worship, and fire altars. No temples were built."
    },
    {
      "q": "The decline of the Mature Harappan phase and the transition to the Late Harappan phase started around:",
      "opts": [
        "c. 1900 BCE",
        "c. 1500 BCE",
        "c. 1200 BCE",
        "c. 1000 BCE"
      ],
      "ans": 0,
      "sol": "The transition from Mature to Late Harappan (de-urbanization) started around 1900 BCE."
    },
    {
      "q": "The Late Harappan phase is also known as the:",
      "opts": [
        "Localisation Era",
        "Regionalisation Era",
        "Integration Era",
        "Imperial Era"
      ],
      "ans": 0,
      "sol": "The Late Harappan phase is known as the Localisation Era. The Early is Regionalisation, and the Mature is Integration."
    },
    {
      "q": "Which of the following features is characteristic of the Late Harappan settlements?\n1. Haphazard housing built with old, reused bricks.\n2. Disappearance of municipal drainage and sanitation.\n3. Return to rural agricultural economy.\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 2,
      "sol": "All three statements are correct. Late Harappan settlements show civic regression, house construction over older streets, lack of drains, and a return to rural farming."
    },
    {
      "q": "The Cemetery H culture of the Late Harappan phase is geographically located in:",
      "opts": [
        "Punjab (Pakistan/India)",
        "Sindh",
        "Gujarat",
        "Balochistan"
      ],
      "ans": 0,
      "sol": "The Cemetery H culture, named after a burial ground at Harappa, represents the Late Harappan phase in Punjab."
    },
    {
      "q": "The Lustrous Red Ware (LRW) culture represents the Late Harappan phase in which of the following regions?",
      "opts": [
        "Gujarat",
        "Sindh",
        "Punjab",
        "Gangetic Valley"
      ],
      "ans": 0,
      "sol": "Lustrous Red Ware (LRW) is the post-urban ceramic style characteristic of late-phase Gujarat sites like Rangpur and Rojdi."
    },
    {
      "q": "Which of the following outposts of the Late Harappan phase is located in western Uttar Pradesh, marking the easternmost limit of the civilization?",
      "opts": [
        "Alamgirpur",
        "Daimabad",
        "Manda",
        "Sutkagendor"
      ],
      "ans": 0,
      "sol": "Alamgirpur in Meerut district (UP) represents the easternmost Late Harappan site, situated on the Hindon River."
    },
    {
      "q": "With reference to the Late Harappan site of Daimabad in Maharashtra, consider the following statements:\n1. It is situated on the Pravara River, a tributary of the Godavari.\n2. It represents the southernmost limit of the Indus Valley Civilisation.\n3. It yielded a cache of four bronze objects: a chariot, rhinoceros, elephant, and bull.\nWhich of the statements given above are correct?",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "All three statements are correct. Daimabad (Maharashtra) is the southernmost outpost and yielded the famous Daimabad Bronzes."
    },
    {
      "q": "At which of the following sites in Haryana have archaeologists excavated structures showing an overlap of Late Harappan and Painted Grey Ware (PGW) cultures?",
      "opts": [
        "Bhagwanpura",
        "Rakhigarhi",
        "Banawali",
        "Kunal"
      ],
      "ans": 0,
      "sol": "Bhagwanpura in Haryana shows clear stratigraphic evidence of an overlap between the Late Harappan and the early Painted Grey Ware (associated with Vedic culture) users."
    },
    {
      "q": "What major change occurred in the settlement pattern during the Late Harappan phase?",
      "opts": [
        "Abandonment of large Indus basin sites and migration towards the Ganga-Yamuna Doab and Gujarat",
        "Establishment of large cities in the Thar Desert",
        "Migration across the Hindu Kush to Central Asia",
        "Complete abandonment of the Indian subcontinent"
      ],
      "ans": 0,
      "sol": "Due to changing monsoons and river drying, people migrated eastward (into Ganga-Yamuna Doab) and southward (into Gujarat), establishing rural farming hamlets."
    },
    {
      "q": "Which of the following theories explaining the decline of the Mature Harappan Civilisation is correctly matched with its proponent?",
      "opts": [
        "Aryan Invasion — Mortimer Wheeler",
        "Tectonic Uplift/Flood — Robert L. Raikes",
        "Drying of Ghaggar River — D.P. Agrawal",
        "All of the above are correctly matched"
      ],
      "ans": 3,
      "sol": "All three matches are correct. Wheeler proposed Aryan invasion, Raikes proposed tectonic uplift/flooding, and Agrawal linked decline to the drying of the Ghaggar-Hakra system."
    },
    {
      "q": "The 'Shahi-Tump' and 'Jhukar' cultures are associated with which phase of Harappan history?",
      "opts": [
        "Late Harappan Phase",
        "Early Harappan Phase",
        "Mature Harappan Phase",
        "Pre-Harappan Neolithic"
      ],
      "ans": 0,
      "sol": "Both Jhukar (Sindh) and Shahi-Tump (Balochistan) represent post-urban, Late Harappan regional cultures."
    },
    {
      "q": "The Late Harappan site of Hulas is located in which state of India?",
      "opts": [
        "Uttar Pradesh",
        "Haryana",
        "Punjab",
        "Rajasthan"
      ],
      "ans": 0,
      "sol": "Hulas is located in Saharanpur district, Uttar Pradesh, representing the Late Harappan phase in the upper Doab."
    },
    {
      "q": "Which of the following crafts continued to survive in Gujarat even during the Late Harappan phase?",
      "opts": [
        "Bead manufacturing and shell working",
        "Large-scale monumental brick-making",
        "Mesopotamian weight standardization",
        "Cylinder seal engraving"
      ],
      "ans": 0,
      "sol": "While complex civic systems collapsed, craft activities like shell working and bead-making survived in Gujarat (e.g., Rangpur) due to access to raw marine materials."
    },
    {
      "q": "Consider the following statements regarding the Ochre Coloured Pottery (OCP) culture:\n1. It is chronologically contemporary with the Late Harappan phase in the Upper Ganga valley.\n2. It represents a copper hoarding community.\nWhich of the statements given above is/are correct?",
      "opts": [
        "1 only",
        "2 only",
        "Both 1 and 2",
        "Neither 1 nor 2"
      ],
      "ans": 2,
      "sol": "Both statements are correct. OCP culture in the Upper Gangetic plain overlaps with Late Harappan and is associated with copper hoard discoveries."
    },
    {
      "q": "The destruction layer at Kot Diji and Amri suggests that:",
      "opts": [
        "A transitional phase between Early and Mature Harappan was accompanied by fires/conflicts",
        "Mesopotamians invaded and destroyed the towns",
        "The towns were submerged under the sea",
        "The residents abandoned the towns due to sudden volcanic eruptions"
      ],
      "ans": 0,
      "sol": "The ash layer separating the early and mature levels at Kot Diji points to a transition marked by fire, which may indicate warfare or intentional clearing."
    },
    {
      "q": "Which of the following terms is used by historians to describe the cultural transition showing both Harappan and Vedic elements in Haryana?",
      "opts": [
        "Late Harappan-PGW Overlap Phase",
        "Early Aryan Phase",
        "Bronze-Iron Age Synthesis",
        "Ghaggar Renaissance"
      ],
      "ans": 0,
      "sol": "The overlap of Late Harappan and PGW (Painted Grey Ware) cultures at Bhagwanpura represents this cultural transition."
    },
    {
      "q": "The Mature Harappan urban layout is strictly described as 'Orthogonal'. What does this term imply?",
      "opts": [
        "Streets intersecting at right angles forming rectangular grids",
        "Circular concentric streets centered on a temple",
        "Haphazard layout without any street planning",
        "Linear layout along a single river channel"
      ],
      "ans": 0,
      "sol": "Orthogonal refers to straight streets intersecting at 90-degree angles, creating rectangular grids."
    },
    {
      "q": "Which of the following animals is NOT depicted on Mature Harappan seals?",
      "opts": [
        "Lion",
        "Humped Bull",
        "Rhinoceros",
        "Tiger"
      ],
      "ans": 0,
      "sol": "The Lion is not depicted on Harappan seals (the tiger, bull, elephant, and rhino are). The lion becomes prominent under the Mauryas."
    },
    {
      "q": "The Late Harappan site of Manda in Jammu & Kashmir represents the northern limit of the civilization. It is situated on which river?",
      "opts": [
        "Chenab",
        "Jhelum",
        "Indus",
        "Ravi"
      ],
      "ans": 0,
      "sol": "Manda is located on the right bank of the Chenab River, J&K."
    },
    {
      "q": "The transition from the chalcolithic rural village of Mehrgarh to the Early Harappan phase shows that:",
      "opts": [
        "Urbanisation was a gradual process of development of local farming cultures",
        "Urbanisation was imported directly from Sumeria",
        "Nomadic hunters built the cities overnight",
        "Cities were founded by Mesopotamian merchants"
      ],
      "ans": 0,
      "sol": "Mehrgarh's sequence shows the transition from Neolithic farming to early chalcolithic village networks, proving the local, gradual roots of urbanization."
    },
    {
      "q": "The 'Meluhhan' trade with Mesopotamia began in which phase and declined in which phase?",
      "opts": [
        "Began in Mature, declined in Late",
        "Began in Early, declined in Mature",
        "Began in Late, declined in PGW",
        "Began in Neolithic, declined in Early"
      ],
      "ans": 0,
      "sol": "The direct maritime trade with Mesopotamia peaked during the Mature Harappan phase and completely collapsed in the Late Harappan phase."
    },
    {
      "q": "Which Late Harappan site has yielded a copper hoard including a bronze chariot, elephant, and rhinoceros?",
      "opts": [
        "Daimabad",
        "Rangpur",
        "Hulas",
        "Alamgirpur"
      ],
      "ans": 0,
      "sol": "Daimabad in Maharashtra yielded a cache of heavy bronze figures, including a chariot driven by a man."
    },
    {
      "q": "The Painted Grey Ware (PGW) culture, which overlaps with the Late Harappan at Bhagwanpura, is chronologically associated with:",
      "opts": [
        "The Early Iron Age and Vedic Period",
        "The Early Bronze Age",
        "The Neolithic Age",
        "The Mesolithic Age"
      ],
      "ans": 0,
      "sol": "PGW is associated with the Iron Age and the Vedic texts (specifically the Later Vedic period)."
    },
    {
      "q": "The decline of urban centers in the Indus Valley was accompanied by a shift in settlement direction towards:",
      "opts": [
        "East and South-East",
        "West and North-West",
        "Central Asia",
        "Persian Gulf"
      ],
      "ans": 0,
      "sol": "Settlements shifted eastward (into the Gangetic basin) and southward (into Gujarat)."
    },
    {
      "q": "Which of the following sites in Gujarat does NOT show any Mature Harappan phase, representing only the Late Harappan phase?",
      "opts": [
        "Rangpur",
        "Rojdi",
        "Lothal",
        "Dholavira"
      ],
      "ans": 0,
      "sol": "Lothal and Dholavira contain mature levels, but Rangpur and Rojdi are primary representatives of Gujarat's post-urban Late Harappan phase."
    },
    {
      "q": "The 'Horned Deity' motif painted on Kot Diji pottery is considered a precursor to which Mature Harappan religious element?",
      "opts": [
        "Pashupati / Proto-Shiva Seal",
        "Great Bath rituals",
        "Fire Altar worship",
        "Mother Goddess figurines"
      ],
      "ans": 0,
      "sol": "The horned figure painted on Kot Dijian pottery is considered an early form of the horned Pashupati figure found on Mature seals."
    },
    {
      "q": "With reference to the end of the Indus Civilisation, most modern scholars agree that it was caused by:",
      "opts": [
        "A combination of ecological changes, shifting monsoons, and drying of rivers",
        "A sudden, bloody invasion by Aryan tribes",
        "A massive earthquake that swallowed all cities",
        "A sudden epidemic of malaria"
      ],
      "ans": 0,
      "sol": "Most modern historians reject single-cause theories (like invasion or single floods) and attribute the decline to gradual environmental degradation, monsoonal shifts, and river course changes."
    },
    {
      "q": "Which of the following sites represents the northernmost outpost of the Mature Harappan phase, located in Afghanistan?",
      "opts": [
        "Shortughai",
        "Manda",
        "Sutkagendor",
        "Daimabad"
      ],
      "ans": 0,
      "sol": "Shortughai in northern Afghanistan is the northernmost outpost of the Mature phase, acting as a trading station for lapis lazuli."
    },
    {
      "q": "The transition from the Mature to the Late Harappan phase is marked by the replacement of standardized cubical weights by:",
      "opts": [
        "Localized stone/shell weights and barter system",
        "Mesopotamian cylinder weights",
        "Iron balance beams",
        "Greek coins"
      ],
      "ans": 0,
      "sol": "The demise of centralized administration led to the abandonment of standardized weights, forcing people to rely on local trade standards and barter."
    },
    {
      "q": "The post-urban Harappan culture at Harappa itself is known as:",
      "opts": [
        "Cemetery H Culture",
        "Jhukar Culture",
        "Ochre Coloured Pottery",
        "Banas Culture"
      ],
      "ans": 0,
      "sol": "The Cemetery H culture represents the Late Harappan phase at Harappa."
    }
  ],
  "mockTestQuestions": [
    {
      "q": "Consider the following statements regarding the developmental phases of the Harappan Civilisation:\n1. The Hakra Ware phase represents the earliest chalcolithic rural culture in the Ghaggar-Hakra basin.\n2. The Ravi phase at Harappa yields the first direct evidence of potters' marks and early scripts.\n3. The Kot Diji phase represents a fortified, proto-urban stage containing destruction levels by fire.\nWhich of the statements given above are correct?",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "All three statements are correct. These represent the stages of Early Harappan evolution leading to mature urbanization."
    },
    {
      "q": "Which of the following sites has yielded continuous stratigraphy spanning from the Pre-Harappan/Early Harappan phase, through the Mature phase, to the Late Harappan phase?\n1. Rakhigarhi\n2. Dholavira\n3. Kot Diji\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 0,
      "sol": "Rakhigarhi and Dholavira show all three phases. Kot Diji lacks the Late Harappan phase (it has Early and Mature, but was abandoned before the Late phase)."
    },
    {
      "q": "With reference to the Mature Harappan phase, which of the following is/are the key elements of administrative and civic integration?\n1. Standardized bricks with a strict 1:2:4 ratio.\n2. A unified weight system based on binary and decimal progressions.\n3. Complete absence of any regional variation in ceramic styles.\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 0,
      "sol": "Bricks (1:2:4) and weights were highly standardized. Regional variations in pottery still existed in minor forms, and 'complete absence' is an extreme incorrect statement."
    },
    {
      "q": "The Late Harappan phase, also known as the Localisation Era, is characterized by which of the following archaeological indicators?\n1. Disappearance of the Indus script and steatite seals.\n2. Return to haphazard civic planning and rural settlement structures.\n3. Emergence of regional pottery cultures like Cemetery H and Jhukar.\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 3,
      "sol": "All three statements are correct. The Localisation Era is marked by de-urbanization, loss of writing/weights, and fragmentation into regional cultures."
    },
    {
      "q": "Consider the following statements:\n1. Daimabad in Maharashtra represents the southernmost outpost of the Late Harappan phase.\n2. Bhagwanpura in Haryana shows a stratigraphic overlap of Late Harappan and early Painted Grey Ware (PGW) cultures.\nWhich of the statements given above is/are correct?",
      "opts": [
        "1 only",
        "2 only",
        "Both 1 and 2",
        "Neither 1 nor 2"
      ],
      "ans": 2,
      "sol": "Both statements are correct. Daimabad is the southernmost limit (Godavari basin), and Bhagwanpura provides the overlap with PGW (Vedic) culture."
    },
    {
      "q": "The pre-mature agricultural ploughed field discovered at Kalibangan is associated with which phase of the Harappan evolution?",
      "opts": [
        "Early Harappan Phase",
        "Mature Harappan Phase",
        "Late Harappan Phase",
        "Pre-Harappan Neolithic"
      ],
      "ans": 0,
      "sol": "The ploughed field at Kalibangan belongs to the Early Harappan (pre-mature) level, showing early agricultural standardization."
    },
    {
      "q": "Which of the following statements is/are correct regarding the decline of the Mature Harappan Civilisation?\n1. Modern research supports a gradual de-urbanization driven by climate change and monsoonal shifts rather than a sudden invasion.\n2. The population died out completely, leaving the Indus basin uninhabited for a thousand years.\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 only",
        "2 only",
        "Both 1 and 2",
        "Neither 1 nor 2"
      ],
      "ans": 0,
      "sol": "Statement 1 is correct. Statement 2 is incorrect because the population did not die out; they migrated to the Gangetic valley and Gujarat, establishing rural settlements."
    },
    {
      "q": "Which of the following Late Harappan regional cultures is correctly matched with its geographical area?\n1. Jhukar Culture — Sindh\n2. Cemetery H Culture — Punjab\n3. Lustrous Red Ware Culture — Gujarat\nSelect the correct answer using the codes given below:",
      "opts": [
        "1 and 2 only",
        "2 and 3 only",
        "1 and 3 only",
        "1, 2 and 3"
      ],
      "ans": 2,
      "sol": "All three matches are correct. These represent the post-urban regional cultures of the Localisation Era."
    },
    {
      "q": "With reference to the metal technology of the Harappan Civilisation, consider the following statements:\n1. The Mature Harappan phase is characterized by advanced bronze-casting using the lost-wax technique.\n2. The Late Harappan phase marks the transition into the early Iron Age of India.\nWhich of the statements given above is/are correct?",
      "opts": [
        "1 only",
        "2 only",
        "Both 1 and 2",
        "Neither 1 nor 2"
      ],
      "ans": 0,
      "sol": "Statement 1 is correct (e.g., Dancing Girl). Statement 2 is incorrect because the Late Harappan phase remained pre-Iron; Iron appeared in India around 1000 BCE during the Vedic period."
    },
    {
      "q": "Assertion (A): The shift from the Early Harappan to the Mature Harappan phase represents an urban revolution.\nReason (R): The introduction of uniform writing, weights, and modular brick construction integrated diverse regional cultures into a cohesive administrative system.\nSelect the correct answer using the codes given below:",
      "opts": [
        "Both A and R are true and R is the correct explanation of A",
        "Both A and R are true but R is not the correct explanation of A",
        "A is true but R is false",
        "A is false but R is true"
      ],
      "ans": 0,
      "sol": "Both statements are correct, and the administrative integration through standardized writing and weights is what allowed the urban mature phase to function."
    }
  ]
}

# ----------------- HINDI DATA -----------------
hin_data = {
  "breadcrumbs": {
    "parent": "यूपीएससी पाठ्यक्रम",
    "parentUrl": "/upsc/",
    "current": "हड़प्पा सभ्यता के विकास के चरण"
  },
  "hero": {
    "title": "हड़प्पा सभ्यता के विकास के चरण",
    "description": "सिंधु घाटी सभ्यता के विकासवादी प्रक्षेपवक्र का अध्ययन करें: पूर्व-हड़प्पा ग्रामीण संस्कृतियां, प्रारंभिक हड़प्पा प्रोटो-शहरी संक्रमण, परिपक्व हड़प्पा चरम शहरीकरण, और उत्तर-हड़प्पा ग्रामीण अनुकूलन।"
  },
  "labels": {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
      "title": "इंटरैक्टिव यूपीएससी मॉक टेस्ट",
      "description": "हड़प्पा सभ्यता के विकास के चरणों पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध परीक्षण में नकारात्मक अंकन के साथ 10 उच्च गुणवत्ता वाले प्रश्न हैं।",
      "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
      "prevBtn": "पिछला प्रश्न",
      "nextBtn": "अगला प्रश्न",
      "submitBtn": "परीक्षण सबमिट करें"
    }
  },
  "timeline": {
    "title": "हड़प्पा सभ्यता का विकासवादी क्षितिज",
    "description": "ताम्रपाषाण युग की ग्रामीण जड़ों से नियोजित शहरों और अंतिम उत्तर-शहरी बिखराव तक के संक्रमण को देखने के लिए प्रत्येक चरण कार्ड पर क्लिक करें।",
    "cards": [
      {
        "period": "पूर्व एवं प्रारंभिक हड़प्पा चरण",
        "date": "लगभग 3300 ईसा पूर्व – 2600 ईसा पूर्व",
        "details": "<strong>उद्भव और स्थापना</strong>: नवपाषाण मेहरगढ़ से गतिहीन ताम्रपाषाण चरवाहा गांवों में क्रमिक संक्रमण।<br><br><strong>मुख्य विशेषताएं</strong>: सुरक्षात्मक किलेबंदी, विशिष्ट शिल्प (मनके बनाना, धातु कर्म), मानकीकृत चाक-निर्मित मिट्टी के बर्तन (हाकड़ा और रावी संस्कृति), और स्थानीय व्यापार नेटवर्क का उदय। महत्वपूर्ण स्थलों में कोट दीजी, कालीबंगन, आमरी और भिरड़ाना शामिल हैं।"
      },
      {
        "period": "परिपक्व हड़प्पा चरण",
        "date": "लगभग 2600 ईसा पूर्व – 1900 ईसा पूर्व",
        "details": "<strong>शहरी क्रांति</strong>: क्षेत्रीय एकीकरण, नागरिक योजना और व्यापार अधिशेष का पूर्ण सुदृढ़ीकरण।<br><br><strong>मुख्य विशेषताएं</strong>: मानकीकृत ग्रिड-नियोजित शहर, विशाल पकी-ईंटों की संरचनाएं (विशाल स्नानागार, अन्नागार), उन्नत जल निकासी प्रणाली, लेखन/लिपि, समान बाट और माप (16-आधार प्रणाली), मेसोपोटामिया के साथ लंबी दूरी का व्यापार (मेलुहा व्यापार), और उच्च गुणवत्ता वाली कांस्य/सेलखड़ी कला। मुख्य स्थल: हड़प्पा, मोहनजोदड़ो, राखीगढ़ी, धोलावीरा और लोथल।"
      },
      {
        "period": "उत्तर हड़प्पा चरण",
        "date": "लगभग 1900 ईसा पूर्व – 1300 ईसा पूर्व",
        "details": "<strong>उत्तर-शहरी पतन</strong>: नागरिक क्षय, वि-शहरीकरण और क्षेत्रीय विखंडन।<br><br><strong>मुख्य विशेषताएं</strong>: प्रणालीगत मानकीकरण (लिपि, मुहर, बाट) का ह्रास, लंबी दूरी के विदेशी व्यापार का गायब होना, और बड़े नियोजित शहरों का छोटे कृषि गांवों में तब्दील होना। स्थानीय मृदभांड संस्कृतियों का उदय हुआ, जैसे सिमेट्री एच, झुकर और चमकीले लाल मृदभांड संस्कृतियां। स्थलों में झुकर, रंगपुर, रोजड़ी और दैमाबाद शामिल हैं।"
      }
    ]
  },
  "mnemonics": {
    "title": "याद रखने के स्मृति सूत्र (Mnemonics)",
    "description": "यूपीएससी परीक्षा के लिए स्थलों को उनके विकासवादी चरणों में वर्गीकृत करने के लिए इन स्मृति सूत्रों का उपयोग करें।",
    "items": [
      {
        "title": "स्मृति सूत्र 1: प्रारंभिक हड़प्पा किलेबंद स्थल",
        "phrase": "\"K-B-A-K (कबाक / मुकुट) - प्रारंभिक किलेबंद स्तंभ\"",
        "decryption": "**K**ot Diji (कोट दीजी), **B**anawali (बनावली), **A**mri (आमरी), और **K**alibangan (कालीबंगन) (**KBAK**) प्रमुख प्रारंभिक हड़प्पा स्थल हैं जहां प्रारंभिक किलेबंदी विकसित हुई थी।"
      },
      {
        "title": "स्मृति सूत्र 2: उत्तर हड़प्पा की क्षेत्रीय उप-संस्कृतियां",
        "phrase": "\"J-C-L (जूनियर कॉलेज लेक्चर) उत्तर चरण\"",
        "decryption": "**J**hukar Culture (झुकर संस्कृति - सिंध), **C**emetery H (सिमेट्री एच - पंजाब), और **L**ustrous Red Ware (चमकीले लाल मृदभांड - गुजरात) (**JCL**) उत्तर हड़प्पा चरण की विशिष्ट क्षेत्रीय संस्कृतियों का प्रतिनिधित्व करते हैं।"
      },
      {
        "title": "स्मृति सूत्र 3: परिपक्व हड़प्पा के महानगर",
        "phrase": "\"H-M-R-D-L (हाउ मेनी रुपीस डिड लोथल मेक?)\"",
        "decryption": "**H**arappa (हड़प्पा), **M**ohenjo-daro (मोहनजोदड़ो), **R**akhigarhi (राखीगढ़ी), **D**holavira (धोलावीरा), और **L**othal (लोथल) (**HMRDL**) नागरिक योजना और विशाल संरचनाओं वाले पांच प्रमुख महानगर हैं।"
      }
    ]
  },
  "traps": {
    "title": "यूपीएससी परीक्षा के सामान्य जाल (टैप्स) जिनसे बचें",
    "items": [
      "<strong>जाल 1: 'अचानक जन्म' का भ्रम:</strong> यूपीएससी के कथनों में दावा किया जा सकता है कि हड़प्पा सभ्यता बिना किसी स्थानीय जड़ के अचानक उत्पन्न हुई। यह **गलत** है। यह मेहरगढ़ जैसी नवपाषाण ग्रामीण संस्कृतियों से प्रारंभिक हड़प्पा ताम्रपाषाण चरणों में क्रमिक रूप से विकसित हुई थी।",
      "<strong>जाल 2: स्थलों की एकल-चरण विशिष्टता:</strong> यह न मानें कि एक स्थल केवल एक ही चरण का था। **धोलावीरा, राखीगढ़ी, कालीबंगन, हड़प्पा और मोहनजोदड़ो** जैसे स्थलों में तीनों चरणों (प्रारंभिक, परिपक्व और उत्तर) के निरंतर जमाव मिलते हैं, जबकि कोट दीजी (मुख्यतः प्रारंभिक) या झुकर (केवल उत्तर) विशिष्ट चरण के संकेतक हैं।",
      "<strong>जाल 3: लोहे और धातु विज्ञान की गलतफहमी:</strong> उत्तर-चरण की कांस्य और तांबा तकनीक को लोहे के साथ न मिलाएँ। संपूर्ण हड़प्पा सभ्यता **पूरी तरह से कांस्य युगीन (लौह-पूर्व)** थी; भारत में लोहा बहुत बाद में उत्तर वैदिक काल (लगभग 1000 ईसा पूर्व) में आया।",
      "<strong>जाल 4: 'पतन' बनाम 'विलुप्ति' का जाल:</strong> उत्तर हड़प्पा चरण शहरी बुनियादी ढांचे के **पतन (वि-शहरीकरण)** का प्रतिनिधित्व करता है, न कि जनसंख्या के पूर्ण विनाश का। लोग पूर्व और दक्षिण की ओर चले गए और ग्रामीण कृषि जीवन में लौट आए।"
    ]
  },
  "deepDive": {
    "title": "पाठ्यक्रम मुख्य अध्ययन नोट्स (गहन अध्ययन)",
    "description": "हड़प्पा सभ्यता के विकासवादी प्रक्षेपवक्र, मुख्य विशेषताओं, स्तरिकी और प्रमुख सिद्धांतों पर महारत हासिल करें।",
    "sections": [
      {
        "title": "1. प्रारंभिक हड़प्पा चरण (लगभग 3300 ईसा पूर्व – 2600 ईसा पूर्व)",
        "content": "<p>प्रारंभिक हड़प्पा चरण सभ्यता के प्रारंभिक, प्रोटो-शहरी चरण का प्रतिनिधित्व करता है। इसे <strong>क्षेत्रीयकरण का युग (Regionalisation Era)</strong> भी कहा जाता है।</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-seedling\"></i> हाकड़ा और रावी चरण</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      सबसे प्रारंभिक पृष्ठभूमि <strong>हाकड़ा मृदभांड चरण</strong> (लगभग 3800-3200 ईसा पूर्व) है, जिसे घग्गर-हाकड़ा घाटी (जैसे भिरड़ाना, कुणाल) में खोजा गया था। इसके बाद हड़प्पा में <strong>रावी चरण</strong> (लगभग 3300-2800 ईसा पूर्व) आता है, जो चाक-निर्मित बर्तनों और शुरुआती लिपि-जैसे चिह्नों के लिए जाना जाता है।\n    </p>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-shield-halved\"></i> प्रोटो-शहरी विशेषताएं</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>किलेबंदी:</strong> कोट दीजी और कालीबंगन में बस्तियों की सुरक्षा के लिए बनाई गई रक्षात्मक दीवारें।</li>\n      <li><strong>मानकीकरण:</strong> समान मृदभांड शैलियों (कोट दीजी शैली) और प्रारंभिक ईंट अनुपातों (1:2:3 या 1:2:4) का उदय।</li>\n      <li><strong>विशिष्टीकरण:</strong> तांबे और कांस्य का प्रारंभिक धातु कर्म और शंख उद्योग का विकास।</li>\n    </ul>\n  </div>\n</div>\n<h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">प्रमुख स्थल और विशेषताएं:</h4>\n<table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\">\n  <thead>\n    <tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\">\n      <th style=\"padding: 0.5rem; text-align: left;\">स्थल</th>\n      <th style=\"padding: 0.5rem; text-align: left;\">प्रमुख प्रारंभिक हड़प्पा साक्ष्य</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">भिरड़ाना</td>\n      <td style=\"padding: 0.5rem;\">सबसे पुराना हड़प्पा स्थल जहाँ हाकड़ा मृदभांड और शुरुआती बहु-कक्षीय घर मिले हैं।</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">कोट दीजी</td>\n      <td style=\"padding: 0.5rem;\">विशाल किलेबंदी की दीवार, सींग वाले देवता के चित्रों वाले मिट्टी के बर्तन, और अग्नि से विनाश की परत।</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">कालीबंगन</td>\n      <td style=\"padding: 0.5rem;\">एक अद्वितीय पूर्व-परिपक्व कृषि क्षेत्र जहाँ आड़े-तिरछे जुते हुए खेत मिले हैं।</td>\n    </tr>\n    <tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\">\n      <td style=\"padding: 0.5rem; font-weight: 600;\">कुणाल</td>\n      <td style=\"padding: 0.5rem;\">चांदी के दो मुकुट और आभूषण, जो प्रारंभिक सामाजिक स्तरीकरण को दर्शाते हैं।</td>\n    </tr>\n  </tbody>\n</table>",
        "masteryZone": [
          {
            "type": "MCQ",
            "q": "निम्नलिखित में से कौन सा स्थल हड़प्पा विकास के सबसे प्रारंभिक हाकड़ा मृदभांड चरण का प्रतिनिधित्व करता है?",
            "opts": [
              "भिरड़ाना",
              "मोहनजोदड़ो",
              "लोथल",
              "चन्हुदड़ो"
            ],
            "ans": 0,
            "sol": "हरियाणा का भिरड़ाना सबसे पुराना हाकड़ा मृदभांड चरण (चौथी सहस्राब्दी ईसा पूर्व) का प्रतिनिधित्व करता है।"
          },
          {
            "type": "MCQ",
            "q": "आड़े-तिरछे जुते हुए खेत का प्रसिद्ध पूर्व-परिपक्व साक्ष्य कहाँ से खोजा गया था?",
            "opts": [
              "कालीबंगन",
              "बनावली",
              "हड़प्पा",
              "कोट दीजी"
            ],
            "ans": 0,
            "sol": "राजस्थान के कालीबंगन से एक अद्वितीय पूर्व-परिपक्व (प्रारंभिक हड़प्पा) जुता हुआ खेत मिला है।"
          },
          {
            "type": "True/False",
            "q": "सत्य या असत्य: हाकड़ा मृदभांड चरण हड़प्पा के रावी चरण से पुराना है।",
            "ans": True,
            "sol": "सत्य। हाकड़ा चरण (लगभग 3800-3200 ईसा पूर्व) रावी चरण (लगभग 3300-2800 ईसा पूर्व) से पुराना है।"
          }
        ]
      },
      {
        "title": "2. परिपक्व हड़प्पा चरण (लगभग 2600 ईसा पूर्व – 1900 ईसा पूर्व)",
        "content": "<p>परिपक्व हड़प्पा चरण सिंधु घाटी सभ्यता के शहरीकरण का चरमोत्कर्ष है। इसे <strong>एकीकरण का युग (Integration Era)</strong> कहा जाता है।</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-city\"></i> शहरी और नागरिक शिखर</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>ग्रिड-नियोजित बस्तियां:</strong> मुख्य सड़कें उत्तर-दक्षिण और पूर्व-पश्चिम की ओर जाती थीं, जो एक-दूसरे को समकोण पर काटती थीं।</li>\n      <li><strong>स्वच्छता:</strong> भूमिगत ढकी हुई नालियां, सोखने वाले जार और घरों में निजी शौचालय।</li>\n      <li><strong>दोहरा विभाजन:</strong> बस्तियों का एक ऊंचे **गढ़ (Citadel)** और एक **निचले शहर (Lower Town)** में विभाजन।</li>\n    </ul>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-scale-balanced\"></i> व्यावसायिक एकीकरण</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      बाटों की मानकीकृत प्रणाली (निचले बाटों के लिए 1, 2, 4, 8, 16, 32... की द्विआधारी प्रणाली)। ईंटों का अनुपात सभी नागरिक संरचनाओं के लिए कड़ाई से 1:2:4 (मोटाई:चौड़ाई:लंबाई) था। व्यापारिक शिपमेंट को प्रमाणित करने के लिए सेलखड़ी की मुहरों और एक लिपि का उपयोग किया जाता था।\n    </p>\n  </div>\n</div>",
        "masteryZone": [
          {
            "type": "MCQ",
            "q": "परिपक्व हड़प्पा ईंट आयामों का अनुपात (मोटाई : चौड़ाई : लंबाई) क्या था?",
            "opts": [
              "1 : 2 : 4",
              "1 : 3 : 9",
              "2 : 4 : 8",
              "1 : 2 : 3"
            ],
            "ans": 0,
            "sol": "परिपक्व हड़प्पा चरण में प्रयुक्त ईंटों का मानक अनुपात कड़ाई से 1:2:4 था।"
          },
          {
            "type": "Assertion-Reason",
            "q": "कथन (A): परिपक्व चरण के दौरान हड़प्पा सभ्यता और मेसोपोटामिया के बीच लंबी दूरी का व्यापार अपने चरम पर था।\nकारण (R): उर, किश और निप्पुर जैसे मेसोपोटामिया के स्थलों से हड़प्पा की मुहरें मिली हैं।",
            "opts": [
              "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
              "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
              "A सत्य है लेकिन R असत्य है",
              "A असत्य है लेकिन R सत्य है"
            ],
            "ans": 0,
            "sol": "दोनों कथन सत्य हैं, और मेसोपोटामिया में हड़प्पा मुहरों की खोज सीधे व्यापारिक संबंधों का प्रमाण है।"
          }
        ]
      },
      {
        "title": "3. उत्तर हड़प्पा चरण (लगभग 1900 ईसा पूर्व – 1300 ईसा पूर्व)",
        "content": "<p>उत्तर हड़प्पा चरण वि-शहरीकरण, नागरिक क्षय और क्षेत्रीय विखंडन का काल है। इसे <strong>स्थानीयकरण का युग (Localisation Era)</strong> भी कहा जाता है।</p>\n<div class=\"deep-dive-grid\">\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-house-chimney-crack\"></i> नागरिक ह्रास और ग्रामीणकरण</div>\n    <ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\">\n      <li><strong>मानकों का ह्रास:</strong> ग्रिड योजना का परित्याग; पुरानी ईंटों से बेतरतीब मकानों का निर्माण।</li>\n      <li><strong>तकनीक का विलोपन:</strong> लिपि, सेलखड़ी मुहरों और मानकीकृत बाटों का उपयोग बंद हो गया।</li>\n      <li><strong>ग्रामीण बदलाव:</strong> बड़े शहरों का परित्याग और छोटे कृषि प्रधान गांवों का विकास।</li>\n    </ul>\n  </div>\n  <div class=\"info-subcard\">\n    <div class=\"subcard-header\"><i class=\"fas fa-palette\"></i> क्षेत्रीय उप-संस्कृतियां</div>\n    <p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">\n      केंद्रीय प्रशासन के पतन के साथ विभिन्न क्षेत्रों में अनूठी शैलियों का उदय हुआ:\n      <br>• <strong>सिमेट्री एच संस्कृति:</strong> पंजाब में, जहां चित्रित कलश समाधान (burials) मिले हैं।\n      <br>• <strong>झुकर संस्कृति:</strong> सिंध में, जहां गोल बटन मुहरें मिली हैं।\n      <br>• <strong>चमकीले लाल मृदभांड:</strong> गुजरात (रंगपुर, रोजड़ी) में।\n    </p>\n  </div>\n</div>",
        "masteryZone": [
          {
            "type": "MCQ",
            "q": "सिंध में उत्तर हड़प्पा चरण को पुरातात्विक रूप से किस स्थानीय संस्कृति द्वारा दर्शाया गया है?",
            "opts": [
              "झुकर संस्कृति",
              "सिमेट्री एच संस्कृति",
              "मालवा संस्कृति",
              "आहार-बनास संस्कृति"
            ],
            "ans": 0,
            "sol": "झुकर संस्कृति सिंध में उत्तर-शहरी, उत्तर हड़प्पा चरण का प्रतिनिधित्व करती है।"
          },
          {
            "type": "One-Liner",
            "q": "हड़प्पा सभ्यता का कौन सा सबसे दक्षिणी स्थल महाराष्ट्र में स्थित है जहां से चार कांस्य मूर्तियां (रथ सहित) मिली हैं?",
            "sol": "दैमाबाद"
          }
        ]
      }
    ]
  },
  "flashcards": {
    "title": "सक्रिय स्मरण फ्लैशकार्ड (Active Recall)",
    "description": "फ्लैशकार्ड्स यूपीएससी परीक्षा के तथ्यों को याद रखने का बेहतरीन तरीका हैं। उत्तर देखने के लिए कार्ड पर क्लिक करें।",
    "items": [
      {
        "question": "भारतीय पुरातत्व सर्वेक्षण (ASI) के अनुसार सबसे पुराना हड़प्पा स्थल कौन सा है?",
        "answer": "हरियाणा का <strong>भिरड़ाना</strong>। यहाँ शुरुआती हाकड़ा मृदभांड स्तर मिले हैं जो लगभग 7500 ईसा पूर्व के हैं।",
        "icon": "fa-clock"
      },
      {
        "question": "किस प्रारंभिक हड़प्पा स्थल से परिपक्व चरण से पहले भीषण आग से तबाही के साक्ष्य मिले हैं?",
        "answer": "सिंध का <strong>कोट दीजी</strong>। एक मोटी राख की परत प्रारंभिक कोट दीजी चरण को बाद के परिपक्व चरण से अलग करती है।",
        "icon": "fa-fire"
      },
      {
        "question": "हड़प्पा सभ्यता का कौन सा स्थल महाराष्ट्र में स्थित है और सबसे दक्षिणी सीमा बनाता है?",
        "answer": "प्रवरा नदी के तट पर स्थित <strong>दैमाबाद</strong>। यहाँ से प्रसिद्ध दैमाबाद कांस्य मूर्तियाँ मिली हैं।",
        "icon": "fa-location-crosshairs"
      }
    ]
  },
  "practiceQuestions": [
    {
      "q": "हड़प्पा सभ्यता के विकास के चरणों का सही कालानुक्रमिक क्रम क्या है?\n1. हाकड़ा मृदभांड चरण\n2. रावी चरण\n3. कोट दीजी चरण\n4. परिपक्व हड़प्पा चरण",
      "opts": [
        "1 — 2 — 3 — 4",
        "2 — 1 — 3 — 4",
        "1 — 3 — 2 — 4",
        "3 — 1 — 2 — 4"
      ],
      "ans": 0,
      "sol": "विकासवादी क्रम हाकड़ा मृदभांड चरण (लगभग 3800-3200 ईसा पूर्व) से शुरू होता है, इसके बाद हड़प्पा में रावी चरण (लगभग 3300-2800 ईसा पूर्व), कोट दीजी चरण (लगभग 2800-2600 ईसा पूर्व), और अंत में परिपक्व हड़प्पा चरण (लगभग 2600-1900 ईसा पूर्व) आता है।"
    },
    {
      "q": "कोट दीजी के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. यह सिंधु नदी के बाएं तट पर मोहनजोदड़ो के विपरीत दिशा में स्थित है।\n2. यहाँ बस्ती की सुरक्षा के लिए एक रक्षात्मक दीवार मिली है।\n3. राख की एक मोटी परत दर्शाती है कि परिपक्व चरण से पहले यह स्थल आग से नष्ट हो गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
      "opts": [
        "केवल 1 और 2",
        "केवल 2 and 3",
        "केवल 1 and 3",
        "1, 2 और 3"
      ],
      "ans": 3,
      "sol": "तीनों कथन सही हैं। कोट दीजी (सिंध) में प्रारंभिक किलेबंद बस्ती के साक्ष्य हैं, जो बाद में परिपक्व हड़प्पा बस्ती के रूप में पुनर्गठित हुई।"
    },
    {
      "q": "निम्नलिखित में से किस स्थल से हड़प्पा सभ्यता के तीनों चरणों (प्रारंभिक, परिपक्व और उत्तर) के साक्ष्य मिले हैं?",
      "opts": [
        "केवल हड़प्पा और राखीगढ़ी",
        "केवल धोलावीरा और कालीबंगन",
        "हड़प्पा, राखीगढ़ी, धोलावीरा और कालीबंगन",
        "कोट दीजी और लोथल"
      ],
      "ans": 2,
      "sol": "हड़प्पा, राखीगढ़ी, धोलावीरा और कालीबंगन इन चारों प्रमुख स्थलों से तीनों चरणों का निरंतर सांस्कृतिक जमाव प्राप्त हुआ है।"
    }
  ],
  "mockTestQuestions": [
    {
      "q": "हड़प्पा सभ्यता के विकास के चरणों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. हाकड़ा मृदभांड चरण घग्गर-हाकड़ा बेसिन में सबसे प्रारंभिक ताम्रपाषाण ग्रामीण संस्कृति का प्रतिनिधित्व करता है।\n2. हड़प्पा का रावी चरण बर्तनों पर प्रारंभिक लिपि और चिह्नों का पहला प्रत्यक्ष साक्ष्य प्रदान करता है।\n3. कोट दीजी चरण एक किलेबंद, प्रोटो-शहरी चरण का प्रतिनिधित्व करता है जहां आग से विनाश के स्तर मिले हैं।\nउपरोक्त में से कौन से कथन सही हैं?",
      "opts": [
        "केवल 1 और 2",
        "केवल 2 और 3",
        "केवल 1 और 3",
        "1, 2 और 3"
      ],
      "ans": 3,
      "sol": "तीनों कथन सही हैं। ये प्रारंभिक हड़प्पा विकास के विभिन्न चरणों को दर्शाते हैं जो परिपक्व शहरीकरण की ओर ले गए।"
    },
    {
      "q": "उत्तर हड़प्पा चरण (स्थानीयकरण का युग) के संदर्भ में निम्नलिखित में से कौन सी विशेषताएं सही हैं?\n1. लिपि और सेलखड़ी की मुहरों का विलोपन।\n2. नागरिक योजना का पतन और बेतरतीब आवासों का निर्माण।\n3. सिमेट्री एच और झुकर जैसी क्षेत्रीय मृदभांड संस्कृतियों का उदय।\nनीचे दिए गए कोड का उपयोग करके सही उत्तर चुनें:",
      "opts": [
        "केवल 1 और 2",
        "केवल 2 और 3",
        "केवल 1 and 3",
        "1, 2 और 3"
      ],
      "ans": 3,
      "sol": "तीनों कथन सही हैं। उत्तर हड़प्पा काल वि-शहरीकरण, नागरिक पतन और क्षेत्रीय विखंडन का काल था।"
    }
  ]
}

# ----------------- WRITE FILES -----------------
with open(os.path.join(ENG_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(HIN_DIR, "content.json"), "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Files created successfully!")
