import fs from 'fs';
import path from 'path';

let apiKey = '';
if (fs.existsSync('.env')) {
  const env = fs.readFileSync('.env', 'utf8');
  for (const line of env.split('\n')) {
    if (line.startsWith('GEMINI_API_KEY=')) apiKey = line.split('=')[1].trim();
  }
}

const prompt = `You are a top UPSC CSE faculty. Write high-yield concepts and theory notes for the UPSC microtopic: "Himalayas".
Context: Subject: Geography, Parent: Physiography & Drainage.

STRICT INSTRUCTIONS:
1. ONLY English language for all content. No Hindi translation needed.
2. NO long paragraphs. Keep every point crisp, analytical, bulleted, and strictly relevant to "Himalayas".
3. Include high-yield mnemonics, memory tricks, and UPSC examiner traps (common mistakes).
4. Strictly return ONLY valid JSON matching this schema:

{
  "overview": {
    "title": "Himalayas",
    "definition": "The Himalayas are young fold mountains formed by the collision of the Indian and Eurasian tectonic plates, acting as a climatic and physical barrier in South Asia.",
    "importanceInUpsc": "Crucial for GS-1 Geography (orogeny, geomorphology, drainage) and GS-3 Environment & Disaster Management (glaciology, landslides, seismic zones).",
    "learningOutcomes": [
      "Understand the structural division (Trans, Greater, Lesser, Outer Himalayas).",
      "Analyze the role of syntaxial bends and longitudinal valleys (Duns)."
    ],
    "prerequisites": ["Plate Tectonics Theory"],
    "estimatedReadingTime": 15
  },
  "concepts": {
    "sections": [
      {
        "title": "Geological Origin & Plate Tectonics",
        "type": "paragraph",
        "content": "• **Orogeny**: Formed during Tertiary period via collision of Indian & Eurasian plates.\n• **Tethys Geosyncline**: Marine sediments compressed and uplifted into fold mountains.\n• **Ongoing Uplift**: Northward movement of Indian plate (~5 cm/yr) makes the region highly seismically active (Zone IV & V)."
      },
      {
        "title": "Longitudinal Structural Divisions",
        "type": "table",
        "headers": ["Division", "Alternative Name", "Average Elevation", "Key Ranges & Features"],
        "rows": [
          ["Trans-Himalayas", "Tibetan Himalayas", "6000 m", "Karakoram (K2), Ladakh, Zaskar, Kailash ranges; cold desert climate."],
          ["Greater Himalayas", "Himadri", "6100 m", "Continuous core of granite; Mt Everest, Kanchenjunga; perennial snow glaciers."],
          ["Lesser Himalayas", "Himachal", "3700 - 4500 m", "Pir Panjal (longest), Dhaula Dhar, Nag Tibba; prominent hill stations & Duns."],
          ["Outer Himalayas", "Shiwaliks", "900 - 1100 m", "Unconsolidated fluvial sediments; prone to landslides; flat valleys (Duns & Duars)."]
        ]
      },
      {
        "title": "Key Geomorphological Characteristics",
        "type": "list",
        "items": [
          {
            "term": "Syntaxial Bends",
            "definition": "Hairpin structural bends at Nanga Parbat in the west and Namcha Barwa in the east due to rigid peninsular shield resistance."
          },
          {
            "term": "Major Thrusts & Faults",
            "definition": "Himalayan Frontal Thrust (HFT), Main Boundary Thrust (MBT), Main Central Thrust (MCT), and Indus-Tsangpo Suture Zone (ITSZ)."
          },
          {
            "term": "Karewas of Kashmir",
            "definition": "Lacustrine clay and silt deposits in Kashmir Valley ideal for Saffron (Zafran) cultivation."
          }
        ]
      },
      {
        "title": "High-Yield Memory Hacks & Mnemonics",
        "type": "subcards",
        "items": [
          {
            "title": "Mnemonic: North to South Himalayan Ranges",
            "content": "• **Trick**: **K-L-Z-P-D-S** -> **K**al **L**adakh **Z**askar **P**ir Panjal **D**haula Dhar **S**hiwalik.\n• **Usage**: Solves standard UPSC Prelims North-to-South arrangement questions instantly."
          },
          {
            "title": "Mnemonic: North to South Major Thrust Faults",
            "content": "• **Trick**: **ITSZ -> MCT -> MBT -> HFT** (**I**ndian **M**ountain **M**akes **H**istory).\n• **Structure**: ITSZ (Trans/Greater), MCT (Greater/Lesser), MBT (Lesser/Shiwalik), HFT (Shiwalik/Indo-Gangetic Plain)."
          }
        ]
      }
    ],
    "upscNotes": [
      {
        "type": "trap",
        "content": "Examiner Trap: Assuming Shiwaliks are crystalline like Himadri. Shiwaliks consist of unconsolidated river boulders and sand, making them highly unstable and erosion-prone."
      },
      {
        "type": "tip",
        "content": "Prelims Strategy: Remember that Pir Panjal is in the Lesser Himalayas (Himachal), whereas Karakoram and Zaskar are Trans-Himalayan."
      }
    ],
    "keyTakeaways": [
      "Himalayas are young, active fold mountains with 4 major longitudinal divisions separated by thrust faults.",
      "Syntaxial bends at Nanga Parbat and Namcha Barwa shape the drainage and tectonic orientation.",
      "Karewa formations in J&K are lacustrine terraces known for saffron cultivation."
    ]
  }
}`;

const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`;
const payload = {
  contents: [{ parts: [{ text: prompt }] }],
  generationConfig: { responseMimeType: 'application/json' }
};

const res = await fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(payload)
});

const data = await res.json();
console.log('Gemini 3.5 Flash Lite Output:');
console.log(data.candidates[0].content.parts[0].text);
