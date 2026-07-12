/**
 * UPSSSC Lower Mains Science Page Generator
 * Uses Gemini API to generate detailed content for 19 geography topics
 * Run: node scripts/gen_geography_pages.js
 */

require('dotenv').config();
const { GoogleGenAI } = require('@google/genai');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({ apiKey: API_KEY });

const BASE = path.join(__dirname, '..', 'upsssc-lower-mains', 'science');

// Topic definitions
const TOPICS = [
    {
        key: 'acids-bases-and-salts',
        titleEn: 'Acids Bases And Salts',
        titleHi: 'Acids Bases And Salts (विज्ञान)',
        breadEn: 'Acids Bases And Salt',
        breadHi: 'Acids Bases And Salt',
        descEn: 'Comprehensive study guide covering Acids Bases And Salts for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Acids Bases And Salts को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Acids Bases And Salts" in Science (विज्ञान).`
    },
    {
        key: 'anaemia',
        titleEn: 'Anaemia',
        titleHi: 'Anaemia (विज्ञान)',
        breadEn: 'Anaemia',
        breadHi: 'Anaemia',
        descEn: 'Comprehensive study guide covering Anaemia for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Anaemia को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Anaemia" in Science (विज्ञान).`
    },
    {
        key: 'aquifers',
        titleEn: 'Aquifers',
        titleHi: 'Aquifers (विज्ञान)',
        breadEn: 'Aquifers',
        breadHi: 'Aquifers',
        descEn: 'Comprehensive study guide covering Aquifers for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Aquifers को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Aquifers" in Science (विज्ञान).`
    },
    {
        key: 'balanced-diet',
        titleEn: 'Balanced Diet',
        titleHi: 'Balanced Diet (विज्ञान)',
        breadEn: 'Balanced Diet',
        breadHi: 'Balanced Diet',
        descEn: 'Comprehensive study guide covering Balanced Diet for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Balanced Diet को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Balanced Diet" in Science (विज्ञान).`
    },
    {
        key: 'calorie-distribution',
        titleEn: 'Calorie Distribution',
        titleHi: 'Calorie Distribution (विज्ञान)',
        breadEn: 'Calorie Distribution',
        breadHi: 'Calorie Distribution',
        descEn: 'Comprehensive study guide covering Calorie Distribution for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Calorie Distribution को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Calorie Distribution" in Science (विज्ञान).`
    },
    {
        key: 'carbon-and-its-compounds',
        titleEn: 'Carbon And Its Compounds',
        titleHi: 'Carbon And Its Compounds (विज्ञान)',
        breadEn: 'Carbon And Its Compo',
        breadHi: 'Carbon And Its Compo',
        descEn: 'Comprehensive study guide covering Carbon And Its Compounds for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Carbon And Its Compounds को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Carbon And Its Compounds" in Science (विज्ञान).`
    },
    {
        key: 'cell-structure-and-functions',
        titleEn: 'Cell Structure And Functions',
        titleHi: 'Cell Structure And Functions (विज्ञान)',
        breadEn: 'Cell Structure And F',
        breadHi: 'Cell Structure And F',
        descEn: 'Comprehensive study guide covering Cell Structure And Functions for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Cell Structure And Functions को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Cell Structure And Functions" in Science (विज्ञान).`
    },
    {
        key: 'diarrhea',
        titleEn: 'Diarrhea',
        titleHi: 'Diarrhea (विज्ञान)',
        breadEn: 'Diarrhea',
        breadHi: 'Diarrhea',
        descEn: 'Comprehensive study guide covering Diarrhea for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Diarrhea को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Diarrhea" in Science (विज्ञान).`
    },
    {
        key: 'diseases-and-defence-mechanism',
        titleEn: 'Diseases And Defence Mechanism',
        titleHi: 'Diseases And Defence Mechanism (विज्ञान)',
        breadEn: 'Diseases And Defence',
        breadHi: 'Diseases And Defence',
        descEn: 'Comprehensive study guide covering Diseases And Defence Mechanism for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Diseases And Defence Mechanism को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Diseases And Defence Mechanism" in Science (विज्ञान).`
    },
    {
        key: 'drinking-water-quality-standards',
        titleEn: 'Drinking Water Quality Standards',
        titleHi: 'Drinking Water Quality Standards (विज्ञान)',
        breadEn: 'Drinking Water Quali',
        breadHi: 'Drinking Water Quali',
        descEn: 'Comprehensive study guide covering Drinking Water Quality Standards for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Drinking Water Quality Standards को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Drinking Water Quality Standards" in Science (विज्ञान).`
    },
    {
        key: 'electricity-and-magnetism',
        titleEn: 'Electricity And Magnetism',
        titleHi: 'Electricity And Magnetism (विज्ञान)',
        breadEn: 'Electricity And Magn',
        breadHi: 'Electricity And Magn',
        descEn: 'Comprehensive study guide covering Electricity And Magnetism for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Electricity And Magnetism को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Electricity And Magnetism" in Science (विज्ञान).`
    },
    {
        key: 'electromagnetic-resistivity-survey',
        titleEn: 'Electromagnetic Resistivity Survey',
        titleHi: 'Electromagnetic Resistivity Survey (विज्ञान)',
        breadEn: 'Electromagnetic Resi',
        breadHi: 'Electromagnetic Resi',
        descEn: 'Comprehensive study guide covering Electromagnetic Resistivity Survey for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Electromagnetic Resistivity Survey को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Electromagnetic Resistivity Survey" in Science (विज्ञान).`
    },
    {
        key: 'genetics-and-evolution',
        titleEn: 'Genetics And Evolution',
        titleHi: 'Genetics And Evolution (विज्ञान)',
        breadEn: 'Genetics And Evoluti',
        breadHi: 'Genetics And Evoluti',
        descEn: 'Comprehensive study guide covering Genetics And Evolution for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Genetics And Evolution को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Genetics And Evolution" in Science (विज्ञान).`
    },
    {
        key: 'gravitation',
        titleEn: 'Gravitation',
        titleHi: 'Gravitation (विज्ञान)',
        breadEn: 'Gravitation',
        breadHi: 'Gravitation',
        descEn: 'Comprehensive study guide covering Gravitation for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Gravitation को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Gravitation" in Science (विज्ञान).`
    },
    {
        key: 'heat-and-thermodynamics',
        titleEn: 'Heat And Thermodynamics',
        titleHi: 'Heat And Thermodynamics (विज्ञान)',
        breadEn: 'Heat And Thermodynam',
        breadHi: 'Heat And Thermodynam',
        descEn: 'Comprehensive study guide covering Heat And Thermodynamics for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Heat And Thermodynamics को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Heat And Thermodynamics" in Science (विज्ञान).`
    },
    {
        key: 'human-physiology-digestive-respiratory-circulatory',
        titleEn: 'Human Physiology Digestive Respiratory Circulatory',
        titleHi: 'Human Physiology Digestive Respiratory Circulatory (विज्ञान)',
        breadEn: 'Human Physiology Dig',
        breadHi: 'Human Physiology Dig',
        descEn: 'Comprehensive study guide covering Human Physiology Digestive Respiratory Circulatory for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Human Physiology Digestive Respiratory Circulatory को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Human Physiology Digestive Respiratory Circulatory" in Science (विज्ञान).`
    },
    {
        key: 'importance-of-food-in-various-diseases',
        titleEn: 'Importance Of Food In Various Diseases',
        titleHi: 'Importance Of Food In Various Diseases (विज्ञान)',
        breadEn: 'Importance Of Food I',
        breadHi: 'Importance Of Food I',
        descEn: 'Comprehensive study guide covering Importance Of Food In Various Diseases for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Importance Of Food In Various Diseases को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Importance Of Food In Various Diseases" in Science (विज्ञान).`
    },
    {
        key: 'importance-of-vaccination',
        titleEn: 'Importance Of Vaccination',
        titleHi: 'Importance Of Vaccination (विज्ञान)',
        breadEn: 'Importance Of Vaccin',
        breadHi: 'Importance Of Vaccin',
        descEn: 'Comprehensive study guide covering Importance Of Vaccination for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Importance Of Vaccination को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Importance Of Vaccination" in Science (विज्ञान).`
    },
    {
        key: 'light-and-optics',
        titleEn: 'Light And Optics',
        titleHi: 'Light And Optics (विज्ञान)',
        breadEn: 'Light And Optics',
        breadHi: 'Light And Optics',
        descEn: 'Comprehensive study guide covering Light And Optics for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Light And Optics को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Light And Optics" in Science (विज्ञान).`
    },
    {
        key: 'mechanics-motion-work-energy-power',
        titleEn: 'Mechanics Motion Work Energy Power',
        titleHi: 'Mechanics Motion Work Energy Power (विज्ञान)',
        breadEn: 'Mechanics Motion Wor',
        breadHi: 'Mechanics Motion Wor',
        descEn: 'Comprehensive study guide covering Mechanics Motion Work Energy Power for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Mechanics Motion Work Energy Power को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Mechanics Motion Work Energy Power" in Science (विज्ञान).`
    },
    {
        key: 'metals-and-non-metals',
        titleEn: 'Metals And Non Metals',
        titleHi: 'Metals And Non Metals (विज्ञान)',
        breadEn: 'Metals And Non Metal',
        breadHi: 'Metals And Non Metal',
        descEn: 'Comprehensive study guide covering Metals And Non Metals for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Metals And Non Metals को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Metals And Non Metals" in Science (विज्ञान).`
    },
    {
        key: 'periodic-classification-of-elements',
        titleEn: 'Periodic Classification Of Elements',
        titleHi: 'Periodic Classification Of Elements (विज्ञान)',
        breadEn: 'Periodic Classificat',
        breadHi: 'Periodic Classificat',
        descEn: 'Comprehensive study guide covering Periodic Classification Of Elements for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Periodic Classification Of Elements को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Periodic Classification Of Elements" in Science (विज्ञान).`
    },
    {
        key: 'plant-physiology-photosynthesis-transpiration',
        titleEn: 'Plant Physiology Photosynthesis Transpiration',
        titleHi: 'Plant Physiology Photosynthesis Transpiration (विज्ञान)',
        breadEn: 'Plant Physiology Pho',
        breadHi: 'Plant Physiology Pho',
        descEn: 'Comprehensive study guide covering Plant Physiology Photosynthesis Transpiration for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Plant Physiology Photosynthesis Transpiration को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Plant Physiology Photosynthesis Transpiration" in Science (विज्ञान).`
    },
    {
        key: 'properties-of-matter-elasticity-surface-tension',
        titleEn: 'Properties Of Matter Elasticity Surface Tension',
        titleHi: 'Properties Of Matter Elasticity Surface Tension (विज्ञान)',
        breadEn: 'Properties Of Matter',
        breadHi: 'Properties Of Matter',
        descEn: 'Comprehensive study guide covering Properties Of Matter Elasticity Surface Tension for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Properties Of Matter Elasticity Surface Tension को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Properties Of Matter Elasticity Surface Tension" in Science (विज्ञान).`
    },
    {
        key: 'protein',
        titleEn: 'Protein',
        titleHi: 'Protein (विज्ञान)',
        breadEn: 'Protein',
        breadHi: 'Protein',
        descEn: 'Comprehensive study guide covering Protein for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Protein को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Protein" in Science (विज्ञान).`
    },
    {
        key: 'role-of-science-and-technology-in-the-development-of-india',
        titleEn: 'Role Of Science And Technology In The Development Of India',
        titleHi: 'Role Of Science And Technology In The Development Of India (विज्ञान)',
        breadEn: 'Role Of Science And ',
        breadHi: 'Role Of Science And ',
        descEn: 'Comprehensive study guide covering Role Of Science And Technology In The Development Of India for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Role Of Science And Technology In The Development Of India को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Role Of Science And Technology In The Development Of India" in Science (विज्ञान).`
    },
    {
        key: 'sound-and-wave-motion',
        titleEn: 'Sound And Wave Motion',
        titleHi: 'Sound And Wave Motion (विज्ञान)',
        breadEn: 'Sound And Wave Motio',
        breadHi: 'Sound And Wave Motio',
        descEn: 'Comprehensive study guide covering Sound And Wave Motion for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Sound And Wave Motion को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Sound And Wave Motion" in Science (विज्ञान).`
    },
    {
        key: 'states-of-matter-solid-liquid-gas',
        titleEn: 'States Of Matter Solid Liquid Gas',
        titleHi: 'States Of Matter Solid Liquid Gas (विज्ञान)',
        breadEn: 'States Of Matter Sol',
        breadHi: 'States Of Matter Sol',
        descEn: 'Comprehensive study guide covering States Of Matter Solid Liquid Gas for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए States Of Matter Solid Liquid Gas को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "States Of Matter Solid Liquid Gas" in Science (विज्ञान).`
    },
    {
        key: 'structure-of-atom-molecules',
        titleEn: 'Structure Of Atom Molecules',
        titleHi: 'Structure Of Atom Molecules (विज्ञान)',
        breadEn: 'Structure Of Atom Mo',
        breadHi: 'Structure Of Atom Mo',
        descEn: 'Comprehensive study guide covering Structure Of Atom Molecules for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Structure Of Atom Molecules को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Structure Of Atom Molecules" in Science (विज्ञान).`
    },
    {
        key: 'tissues-plant-and-animal',
        titleEn: 'Tissues Plant And Animal',
        titleHi: 'Tissues Plant And Animal (विज्ञान)',
        breadEn: 'Tissues Plant And An',
        breadHi: 'Tissues Plant And An',
        descEn: 'Comprehensive study guide covering Tissues Plant And Animal for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Tissues Plant And Animal को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Tissues Plant And Animal" in Science (विज्ञान).`
    },
    {
        key: 'types-of-water-sources',
        titleEn: 'Types Of Water Sources',
        titleHi: 'Types Of Water Sources (विज्ञान)',
        breadEn: 'Types Of Water Sourc',
        breadHi: 'Types Of Water Sourc',
        descEn: 'Comprehensive study guide covering Types Of Water Sources for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Types Of Water Sources को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Types Of Water Sources" in Science (विज्ञान).`
    },
    {
        key: 'vitamin-related-diseases-and-prevention',
        titleEn: 'Vitamin Related Diseases And Prevention',
        titleHi: 'Vitamin Related Diseases And Prevention (विज्ञान)',
        breadEn: 'Vitamin Related Dise',
        breadHi: 'Vitamin Related Dise',
        descEn: 'Comprehensive study guide covering Vitamin Related Diseases And Prevention for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Vitamin Related Diseases And Prevention को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Vitamin Related Diseases And Prevention" in Science (विज्ञान).`
    },
    {
        key: 'vitamins',
        titleEn: 'Vitamins',
        titleHi: 'Vitamins (विज्ञान)',
        breadEn: 'Vitamins',
        breadHi: 'Vitamins',
        descEn: 'Comprehensive study guide covering Vitamins for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Vitamins को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Vitamins" in Science (विज्ञान).`
    },
    {
        key: 'water-cycle',
        titleEn: 'Water Cycle',
        titleHi: 'Water Cycle (विज्ञान)',
        breadEn: 'Water Cycle',
        breadHi: 'Water Cycle',
        descEn: 'Comprehensive study guide covering Water Cycle for UPSSSC Lower Mains.',
        descHi: 'UPSSSC लोअर मेन्स के लिए Water Cycle को कवर करने वाली मार्गदर्शिका।',
        prompt: `Generate UPSSSC Lower Mains exam content for "Water Cycle" in Science (विज्ञान).`
    }
];

// ─── HTML Template Functions ──────────────────────────────────────────────────

function pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON) {
    return `<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.titleEn} - UPSSSC Lower Mains</title>

    <!-- CSS Dependencies -->
    <link
        href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=05feb74c">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c323837a">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=7bf51abb">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=9d684fc1">
    <style>
        .mermaid { overflow-x: auto; text-align: center; padding: 1.5rem 0; margin-bottom: 2rem; border-radius: 12px; background: rgba(0,0,0,0.02); }
        .mermaid svg { min-width: 800px; max-width: none !important; height: auto; }
    </style>
</head>

<body>
    <div class="container">
        <div class="top-controls">
            <button class="lang-toggle-btn" onclick="toggleLang()">A/अ</button>
        </div>

        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="../../index.html">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="../../index.html#geo">Science</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">${topic.breadEn}</span>
                <span class="lang-hi">${topic.breadHi}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">${topic.titleEn}</span>
                <span class="lang-hi">${topic.titleHi}</span>
            </h1>
            <p>
                <span class="lang-en">${topic.descEn}</span>
                <span class="lang-hi">${topic.descHi}</span>
            </p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory" onclick="switchTab('theory')">
                <span class="lang-en">Theory & Concepts</span>
                <span class="lang-hi">सिद्धांत और अवधारणाएं</span>
            </button>
            <button class="sub-nav-item" data-tab="practice" onclick="switchTab('practice')">
                <span class="lang-en">Practice (30 Qs)</span>
                <span class="lang-hi">अभ्यास (30 प्रश्न)</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs" onclick="switchTab('pyqs')">
                <span class="lang-en">UP Gov PYQs</span>
                <span class="lang-hi">यूपी सरकार PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test" onclick="switchTab('test')">
                <span class="lang-en">15-Q Test</span>
                <span class="lang-hi">15-प्रश्न टेस्ट</span>
            </button>
        </div>

        <div class="topic-content">

            <div id="tab-theory" class="tab-content" style="display:block">
${theoryHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span class="lang-en">Next: Practice Questions</span>
                        <span class="lang-hi">अगला: अभ्यास प्रश्न</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-practice" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Practice all 30 questions. Each question has an instant answer reveal.</span>
                    <span class="lang-hi">सभी 30 प्रश्नों का अभ्यास करें। प्रत्येक प्रश्न में तत्काल उत्तर।</span>
                </div>
${practiceHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span class="lang-en">Next: UP Gov PYQs</span>
                        <span class="lang-hi">अगला: यूपी सरकार PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-pyqs" class="tab-content" style="display:none">
                <div class="info-banner">
                    <span class="lang-en">Previous Year Questions from UP Government exams (UPSSSC, UP PCS, UP Lower PCS).</span>
                    <span class="lang-hi">यूपी सरकार परीक्षाओं के पिछले वर्ष के प्रश्न (UPSSSC, UP PCS, UP लोअर PCS)।</span>
                </div>
${pyqHtml}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span class="lang-en">Next: 15-Q Test</span>
                        <span class="lang-hi">अगला: 15-प्रश्न टेस्ट</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <div id="tab-test" class="tab-content" style="display:none">
                <div class="test-start-scr" id="test-start">
                    <h3>
                        <span class="lang-en">15-Question Timed Test</span>
                        <span class="lang-hi">15-प्रश्न समयबद्ध टेस्ट</span>
                    </h3>
                    <p>
                        <span class="lang-en">Test your knowledge with 15 curated questions. Time limit: 15 minutes.</span>
                        <span class="lang-hi">15 चयनित प्रश्नों के साथ अपना ज्ञान परखें। समय सीमा: 15 मिनट।</span>
                    </p>
                    <div class="tinfo-grid">
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Questions</span><span class="lang-hi">प्रश्न</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">15</div><div class="tinfo-lbl"><span class="lang-en">Minutes</span><span class="lang-hi">मिनट</span></div></div>
                        <div class="tinfo-card"><div class="tinfo-num">4</div><div class="tinfo-lbl"><span class="lang-en">Options each</span><span class="lang-hi">प्रत्येक विकल्प</span></div></div>
                    </div>
                    <button class="start-test-btn" onclick="startTest()">
                        <span class="lang-en">Start Test</span>
                        <span class="lang-hi">टेस्ट शुरू करें</span>
                    </button>
                </div>
                <div id="test-area" style="display:none">
                    <div class="test-hdr">
                        <div><span class="lang-en">Time Left</span><span class="lang-hi">शेष समय</span></div>
                        <div class="test-tmr" id="test-timer">15:00</div>
                    </div>
                    <div class="test-prog-bar"><div class="test-prog-fill" id="test-prog" style="width:0%"></div></div>
                    <div id="test-questions">
${testHtml}
                    </div>
                    <div style="text-align:center;margin:24px 0">
                        <button onclick="submitTest()" id="submit-btn" style="padding:13px 38px;background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;border:none;border-radius:30px;font-size:1.1rem;font-weight:700;cursor:pointer;box-shadow:0 8px 20px rgba(39,174,96,0.4);">
                            <i class="fas fa-paper-plane"></i>
                            <span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट जमा करें</span>
                        </button>
                    </div>
                </div>
                <div class="test-result" id="test-result">
                    <div style="font-size:1.3rem"><i class="fas fa-trophy"></i> <span class="lang-en">Test Complete!</span><span class="lang-hi">टेस्ट पूर्ण!</span></div>
                    <div class="result-score" id="res-score">0/15</div>
                    <div id="res-label" style="font-size:1rem;opacity:0.9;margin-bottom:5px"></div>
                    <div class="grade-bdg" id="res-grade"></div>
                    <div style="margin-top:18px">
                        <button class="tact-btn" onclick="retakeTest()" style="background:#059669;color:white"><i class="fas fa-redo"></i> <span class="lang-en">Retake</span><span class="lang-hi">पुनः दें</span></button>
                        <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#059669"><i class="fas fa-book"></i> <span class="lang-en">Practice More</span><span class="lang-hi">और अभ्यास करें</span></button>
                    </div>
                </div>
            </div>

        </div>
    </div>

            <script>
                window.upssscTestData = ${testDataJSON};
            </script>
            <script src="/assets/js/upsssc-lower.min.js?v=117a746d"></script>
            <script src="/assets/js/main.min.js?v=86340191"></script>
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
            <script>mermaid.initialize({startOnLoad:true, theme: 'default'});</script>
</body>

</html>`;
}

// ─── Gemini Prompt Builder ────────────────────────────────────────────────────

function buildPrompt(topic) {
    return `You are an expert UPSSSC Lower Mains exam content creator for Indian Science. 
Generate EXTREMELY COMPREHENSIVE and DETAILED exam-focused content for: "${topic.titleEn}" (${topic.titleHi})

CRITICAL SIZE REQUIREMENTS:
- The final HTML file must be at least 250KB
- The theory section alone must contain 15-20 detailed cards (card-premium divs)
- Each card must have extensive paragraphs with facts, data, figures, examples
- Theory must be 150KB+ of content with maximum detail

IMPORTANT: Return ONLY valid JSON. No markdown, no explanation. Just the JSON object.

Generate this exact JSON structure:
{
  "theory": "<VERY LARGE HTML string with 15-20 card-premium divs - MINIMUM 150KB OF THEORY CONTENT>",
  "practiceQs": [<array of exactly 30 MCQ objects WITH COMPLETE MIXTURE of all question types>],
  "pyqs": [<array of exactly 10 PYQ objects>],
  "testQs": [<array of exactly 15 MCQ objects>]
}

THEORY HTML RULES (CRITICAL - MAKE EXTREMELY DETAILED):
- Use these exact CSS classes: card-premium, card-title, theory-heading, theory-para, theory-highlight, theory-overflow-mb, tab-active-bar, theory-section-sep
- Each card has: <div class="card-premium"><h3 class="card-title">...</h3>...</div>
- Use <span class="lang-en">English text</span> and <span class="lang-hi">हिंदी पाठ</span> for ALL text
- Use <h4 class="lang-en theory-heading">heading</h4> and <h4 class="lang-hi theory-heading">शीर्षक</h4>
- Use tables with thead/tbody, class="tab-active-bar" on header rows
- Highlight key facts with <div class="theory-highlight">
- MAKE THEORY EXTREMELY DETAILED with 15-20 cards covering ALL aspects
- Each card must have 3-4 paragraphs of detailed content with facts, figures, data
- Include specific numbers, percentages, rankings, important dates, names of places, rivers, mountains, etc.
- Add multiple tables comparing different features, listing important data
- Make it suitable for UPSSSC Lower Mains, UP PCS level - maximum detail required

PRACTICE QUESTION RULES (30 questions - MUST INCLUDE ALL TYPES):
Each object: { "qEn": "English question", "qHi": "हिंदी प्रश्न", "opts": [{"en":"A option","hi":"A विकल्प"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "Explanation in English", "solHi": "हिंदी में व्याख्या" }
- ans is 0-based index (0=A, 1=B, 2=C, 3=D)
- MUST INCLUDE ALL THESE TYPES (at least 3-4 of each):
  * Factual questions (What, Which, Where, When, Who)
  * Match the column questions (Match column A with column B)
  * Multi-statement True/False questions (Which of the following statements are correct)
  * Assertion-Reason questions
  * Data-based questions (Based on census data, rankings, percentages)
  * Cause-Effect questions
  * Application-based questions
- All questions must be relevant to UPSSSC Lower Mains syllabus
- Explanations must be detailed with correct answers clearly marked

PYQ RULES (10 questions):
Each object: { "qEn": "...", "qHi": "...", "opts": [...], "ans": 0, "year": "UP PCS 2019", "solEn": "...", "solHi": "..." }
- Use realistic UP exam years: UP PCS 2015-2023, UPSSSC 2016-2023, UP Lower PCS 2018-2022
- Questions must be realistic past-exam style with detailed explanations

TEST QUESTION RULES (15 questions - different from practice):
Each object: { "qEn": "...", "qHi": "...", "opts": [{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."},{"en":"...","hi":"..."}], "ans": "A", "solEn": "...", "solHi": "..." }
- ans is "A", "B", "C", or "D" (letter, not number)
- These questions should be different from practice questions
- Include detailed explanations

Topic: ${topic.prompt}
CRITICAL REMINDERS:
1. Theory MUST have 15-20 cards with extensive content - each card 8-10KB of HTML
2. Total file size must exceed 250KB
3. Practice questions must include ALL types: factual, match-column, True/False, assertion-reason, data-based, cause-effect, application-based
4. Use specific data, figures, percentages, rankings from official sources
5. Make content exam-focused for UPSSSC Lower Mains with maximum detail`;
}

// ─── HTML builders from JSON data ────────────────────────────────────────────

function buildPracticeHtml(qs) {
    const letters = ['A', 'B', 'C', 'D'];
    return qs.map((q, i) => {
        const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="q${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
        return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${letters[q.ans]}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${letters[q.ans]}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
    }).join('');
}

function buildPyqHtml(qs) {
    const letters = ['A', 'B', 'C', 'D'];
    return qs.map((q, i) => {
        const opts = q.opts.map((o, j) => `
                    <label class="opt-label">
                        <input type="radio" class="opt-radio" name="pyq${i}" value="${letters[j]}">
                        <span class="lang-en"><b>${letters[j]}.</b> ${o.en}</span>
                        <span class="lang-hi"><b>${letters[j]}.</b> ${o.hi}</span>
                    </label>`).join('');
        return `
                <div class="practice-question-card">
                    <div class="q-row">
                        <div class="q-num-badge">${i + 1}</div>
                        <div class="q-body">
                            <span class="badge-pyq lang-en">${q.year} (UP Exam)</span>
                            <span class="badge-pyq lang-hi">${q.year} (यूपी परीक्षा)</span>
                            <p class="q-text lang-en">${q.qEn}</p>
                            <p class="q-text lang-hi">${q.qHi}</p>
                            <div class="q-options">${opts}
                            </div>
                            <details class="solution-details">
                                <summary class="lang-en">Show Answer</summary>
                                <summary class="lang-hi">उत्तर देखें</summary>
                                <p class="solution-correct lang-en">✔ Correct: ${letters[q.ans]}</p>
                                <p class="solution-correct lang-hi">✔ सही उत्तर: ${letters[q.ans]}</p>
                                <p class="lang-en">${q.solEn}</p>
                                <p class="lang-hi">${q.solHi}</p>
                            </details>
                        </div>
                    </div>
                </div>`;
    }).join('');
}

function buildTestHtml(qs) {
    return qs.map((q, i) => {
        const opts = q.opts.map((o, j) => {
            const letters = ['A', 'B', 'C', 'D'];
            return `\n                                <div class="test-opt" data-qi="${i}" data-ch="${letters[j]}" onclick="selOpt(this)"><span class="opt-ltr">${letters[j]}</span><span class="lang-en">${o.en}</span><span class="lang-hi">${o.hi}</span></div>`;
        }).join('');
        return `
                        <div class="test-qblock" id="tq-${i}">
                            <p class="test-qtext"><span class="test-qnum">Q${i + 1}</span><span style="display:block;margin-top:6px"><span class="lang-en">${q.qEn}</span><span class="lang-hi">${q.qHi}</span></span></p>
                            <div class="test-opts-grid">${opts}
                            </div><input type="hidden" id="tans-${i}" value="${q.ans}"><input type="hidden" id="tsel-${i}" value="">
                        </div>`;
    }).join('');
}

// ─── Model pool ──────────────────────────────────────────────────────────────
const MODEL_POOL = [
    'gemini-3.1-flash-lite',
    'gemini-3.5-flash',
];

// ─── Main Generator ───────────────────────────────────────────────────────────

async function generateTopic(topic) {
    console.log(`\n⟳ Generating: ${topic.titleEn}...`);

    // ── Pass 1: Theory (3 calls to reach 250KB+) ────────────────────────────
    const theoryPrompt = `You are an expert UPSSSC Lower Mains exam content creator for Indian Science.
Generate EXTREMELY COMPREHENSIVE theory content for: "${topic.titleEn}" (${topic.titleHi})

CRITICAL: Theory must be 150KB+ of HTML with 15-20 detailed cards.

Return ONLY valid JSON:
{
  "theory": "<VERY LARGE HTML with 15-20 card-premium divs. Each card 3-4 paragraphs with facts, data, tables. Minimum 150KB total theory content.>"
}

RULES:
- STRUCTURE YOUR THEORY CONTENT IN THIS EXACT ORDER:
  1. Detailed Mindmap (Use Mermaid.js \`mindmap\` syntax inside <pre class="mermaid">...</pre>. DO NOT use flowchart/graph TD. Nodes MUST be very concise, 1-3 words max).
  2. Brief Explanation & Overview (a concise 1-2 card summary to build foundation).
  3. Detailed Explanations (10-15 detailed cards diving deep into every aspect).
  4. Tips, Tricks, and Mnemonics (memorization techniques for the exam).
- Use card-premium, card-title, theory-heading, theory-para, theory-highlight, tab-active-bar, theory-section-sep
- Bilingual: <span class="lang-en"> and <span class="lang-hi">
- Include 4+ tables with geographical data
- Include 5+ theory-highlight boxes
- Every paragraph substantive with real data

Topic: ${topic.prompt}`;

    let theoryHtml = '';
    for (let attempt = 0; attempt < 3; attempt++) {
        try {
            console.log(`  → Theory generation: attempt ${attempt + 1}/3`);
            const response = await ai.models.generateContent({
                model: MODEL_POOL[0],
                contents: theoryPrompt,
                config: {
                    thinkingConfig: { thinkingBudget: 0 },
                    temperature: 0.7,
                    maxOutputTokens: 131072
                }
            });
            let jsonStr = response.text.trim();
            if (jsonStr.startsWith('```')) jsonStr = jsonStr.replace(/^```(?:json)?\n?/, '').replace(/\n?```$/, '');
            const data = JSON.parse(jsonStr);
            theoryHtml = data.theory || '';
            console.log(`  ✓ Theory generated: ${Math.round(theoryHtml.length / 1024)} KB`);
            break;
        } catch (err) {
            console.log(`  ⚠ Theory attempt ${attempt + 1} failed: ${err.message}`);
            await new Promise(r => setTimeout(r, 3000));
        }
    }


    // ── Pass 2: Questions ───────────────────────────────────────────────────
    const questionsPrompt = `You are an expert UPSSSC Lower Mains exam content creator for Indian Science.
Generate practice questions, PYQs, and test for: "${topic.titleEn}" (${topic.titleHi})

CRITICAL: Include ALL question types with detailed explanations.

Return ONLY valid JSON:
{
  "practiceQs": [30 MCQ objects - MIXTURE of all types],
  "pyqs": [10 PYQ objects],
  "testQs": [15 MCQ objects]
}

PRACTICE (30 Qs) DISTRIBUTION:
- Q1-6: Factual
- Q7-10: Match the column
- Q11-15: Multi-statement True/False
- Q16-20: Assertion-Reason
- Q21-24: Data-based (census, stats)
- Q25-27: Cause-Effect
- Q28-30: Application-based

Format each MCQ:
{ "qEn": "...", "qHi": "...", "opts": [{"en":"A","hi":"A"},{"en":"B","hi":"B"},{"en":"C","hi":"C"},{"en":"D","hi":"D"}], "ans": 0, "solEn": "50+ word explanation", "solHi": "व्याख्या" }

PYQs: Use real UP exam years (UP PCS 2015-2023, UPSSSC 2016-2023). Each with year field.
Test: 15 different questions from practice.

Topic: ${topic.prompt}`;

    let practiceQs = [], pyqs = [], testQs = [];
    for (let attempt = 0; attempt < 2; attempt++) {
        try {
            console.log(`  → Questions: attempt ${attempt + 1}/2`);
            const response = await ai.models.generateContent({
                model: MODEL_POOL[0],
                contents: questionsPrompt,
                config: {
                    thinkingConfig: { thinkingBudget: 0 },
                    temperature: 0.7,
                    maxOutputTokens: 131072
                }
            });
            let jsonStr = response.text.trim();
            if (jsonStr.startsWith('```')) jsonStr = jsonStr.replace(/^```(?:json)?\n?/, '').replace(/\n?```$/, '');
            const data = JSON.parse(jsonStr);
            practiceQs = data.practiceQs || [];
            pyqs = data.pyqs || [];
            testQs = data.testQs || [];
            console.log(`  ✓ Questions: ${practiceQs.length} practice, ${pyqs.length} PYQs, ${testQs.length} test`);
            break;
        } catch (err) {
            console.log(`  ⚠ Questions attempt ${attempt + 1} failed: ${err.message}`);
            await new Promise(r => setTimeout(r, 3000));
        }
    }

    // ── Combine and Write ───────────────────────────────────────────────────
    const practiceHtml = buildPracticeHtml(practiceQs);
    const pyqHtml = buildPyqHtml(pyqs);
    const testHtml = buildTestHtml(testQs);
    const testDataJSON = JSON.stringify(testQs.map(q => ({ ans: q.ans, solEn: q.solEn, solHi: q.solHi })));

    const html = pageShell(topic, theoryHtml, practiceHtml, pyqHtml, testHtml, testDataJSON);

    const outDir = path.join(BASE, topic.key);
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });
    const outFile = path.join(outDir, 'index.html');
    fs.writeFileSync(outFile, html, 'utf8');

    const sizeKB = Math.round(html.length / 1024);
    console.log(`  ✓ Written: ${topic.key}/index.html (${sizeKB} KB)`);
}

async function main() {
    console.log('=== UPSSSC Lower Mains Science Page Generator ===');
    console.log(`Using Gemini API Key: ${API_KEY ? API_KEY.substring(0, 10) + '...' : 'NOT FOUND'}`);

    if (!API_KEY) {
        console.error('ERROR: GEMINI_API_KEY not found in .env');
        process.exit(1);
    }

    const retryKeys = process.env.RETRY_KEYS ? process.env.RETRY_KEYS.split(',').map(k => k.trim()) : null;
    const topicsToRun = retryKeys ? TOPICS.filter(t => t.key.includes(retryKeys)) : TOPICS;

    if (retryKeys) console.log(`Retrying only: ${retryKeys.join(', ')}`);
    console.log(`Topics to generate: ${topicsToRun.length}`);

    const failed = [];
    for (const topic of topicsToRun) {
        try {
            await generateTopic(topic);
            await new Promise(r => setTimeout(r, 3000));
        } catch (err) {
            console.error(`  ✗ Failed: ${topic.key} — err.message`);
            failed.push(topic.key);
        }
    }

    console.log('\n=== Generation Complete ===');
    if (failed.length > 0) {
        console.log(`Failed topics (${failed.length}): ${failed.join(', ')}`);
        console.log(`Retry with: RETRY_KEYS=${failed.join(',')} node scripts/gen_geography_pages.js`);
    } else {
        console.log('All topics generated successfully! ✓');
    }
}

main().catch(console.error);
