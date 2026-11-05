/**
 * scripts/remediate_all_116_meta.cjs
 * Remediates all 116 truncated and broken meta descriptions across the repository.
 */

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

const descriptions = {
  // === UPSSSC LOWER MAINS (1) ===
  "upsssc-lower-mains/-template/index.html":
    "Prepare for UPSSSC Lower Mains with comprehensive syllabus notes, solved practice questions, exam trend analysis, and interactive test modules.", // 144

  // === UPSSSC PET (2) ===
  "upsssc-pet/current-affairs/economic-updates/index.html":
    "Master UPSSSC PET economic updates with bilingual month-wise summaries, Union Budget analysis, RBI monetary policy shifts, and solved practice questions.", // 153
  "upsssc-pet/current-affairs/international-events/index.html":
    "Explore UPSSSC PET international current affairs with bilingual monthly recaps of global summits, bilateral treaties, key leaders, and practice quizzes.", // 152

  // === UPSC TOPICWISE PYQS (14) ===
  "upsc-topicwise-pyqs/art-and-culture/philosophy-and-religion/index.html":
    "Master official UPSC Prelims PYQs on Philosophy and Religion with bilingual solutions, detailed explanations, key concepts, and exam trend analysis.", // 149
  "upsc-topicwise-pyqs/geography/population-and-demography/index.html":
    "Master official UPSC Prelims PYQs on Population and Demography with bilingual solutions, detailed concepts, census data, and exam trend analysis.", // 145
  "upsc-topicwise-pyqs/geography/transport-and-infrastructure-geography/index.html":
    "Master official UPSC Prelims PYQs on Transport and Infrastructure Geography with bilingual solutions, key concepts, and complete trend analysis.", // 145
  "upsc-topicwise-pyqs/geography/world-political-geography-and-borders/index.html":
    "Master official UPSC Prelims PYQs on World Political Geography and Borders with bilingual solutions, map concepts, and strategic trend analysis.", // 144
  "upsc-topicwise-pyqs/indian-economy/banking-and-financial-sector/index.html":
    "Master official UPSC Prelims PYQs on Banking and the Financial Sector with bilingual solutions, core concepts, RBI updates, and trend analysis.", // 143
  "upsc-topicwise-pyqs/indian-economy/digital-payments-and-financial-inclusion/index.html":
    "Master official UPSC Prelims PYQs on Digital Payments and Financial Inclusion with bilingual solutions, key concepts, and targeted trend analysis.", // 147
  "upsc-topicwise-pyqs/indian-economy/economic-planning-and-five-year-plans/index.html":
    "Master official UPSC Prelims PYQs on Economic Planning and Five-Year Plans with bilingual solutions, key model concepts, and exam trend analysis.", // 145
  "upsc-topicwise-pyqs/indian-economy/external-sector-and-balance-of-payments/index.html":
    "Master official UPSC Prelims PYQs on the External Sector and Balance of Payments with bilingual solutions, core concepts, and exam trend analysis.", // 146
  "upsc-topicwise-pyqs/indian-polity/constitutional-framework-and-development/index.html":
    "Master official UPSC Prelims PYQs on Constitutional Framework and Development with bilingual solutions, key articles, and exam trend analysis.", // 143
  "upsc-topicwise-pyqs/indian-polity/directive-principles-of-state-policy/index.html":
    "Master official UPSC Prelims PYQs on Directive Principles of State Policy (DPSP) with bilingual solutions, key concepts, and exam trend analysis.", // 145
  "upsc-topicwise-pyqs/indian-polity/elections-and-electoral-reforms/index.html":
    "Master official UPSC Prelims PYQs on Elections and Electoral Reforms with bilingual solutions, constitutional concepts, and exam trend analysis.", // 144
  "upsc-topicwise-pyqs/indian-polity/federalism-and-centre-state-relations/index.html":
    "Master official UPSC Prelims PYQs on Federalism and Centre-State Relations with bilingual solutions, schedule analysis, and exam trend insights.", // 144
  "upsc-topicwise-pyqs/indian-polity/parliament-and-state-legislatures/index.html":
    "Master official UPSC Prelims PYQs on Parliament and State Legislatures with bilingual solutions, legislative concepts, and exam trend analysis.", // 143
  "upsc-topicwise-pyqs/modern-history/constitutional-developments-and-british-plans/index.html":
    "Master official UPSC Prelims PYQs on Constitutional Developments and British Plans with bilingual solutions, key concepts, and exam trend analysis.", // 147

  // === UPSC APFC (12) ===
  "upsc-apfc/accountancy/ratio-analysis/index.html":
    "Master Ratio Analysis for UPSC APFC with high-yield tabular breakdowns, memory mnemonics, exam traps, active recall flashcards, and practice drills.", // 147
  "upsc-apfc/current-affairs/awards-sports-and-persons-in-news/index.html":
    "Master Awards, Sports & Persons in News 2026 for UPSC APFC with month-wise compilations, high-yield factual capsules, and targeted practice tests.", // 146
  "upsc-apfc/current-affairs/economy-budget-and-rbi-decisions/index.html":
    "Master Economy, Budget & RBI Decisions 2026 for UPSC APFC with monthly compilations, Economic Survey insights, Union Budget data, and mock tests.", // 145
  "upsc-apfc/general-science/chemistry/chemistry-in-everyday-life/index.html":
    "Master Chemistry in Everyday Life for UPSC APFC with high-yield tabular summaries, memory mnemonics, exam trap alerts, and interactive flashcards.", // 146
  "upsc-apfc/general-science/physics/gravitation-and-pressure/index.html":
    "Master Gravitation and Pressure for UPSC APFC with conceptual notes, high-yield tabular summaries, memory mnemonics, and interactive flashcards.", // 143
  "upsc-apfc/general-science/physics/light-reflection-and-refraction/index.html":
    "Master Light Reflection and Refraction for UPSC APFC with clear formula breakdowns, high-yield tables, memory mnemonics, and active recall drills.", // 146
  "upsc-apfc/general-science/physics/magnetism-and-electromagnetism/index.html":
    "Master Magnetism and Electromagnetism for UPSC APFC with high-yield tabular summaries, core concept formulas, memory mnemonics, and test drills.", // 144
  "upsc-apfc/indian-economy/digital-payments-and-cbdc/index.html":
    "Master Digital Payments and CBDC for UPSC APFC with high-yield fintech comparisons, regulatory frameworks, memory mnemonics, and practice quizzes.", // 147
  "upsc-apfc/labour-codes-and-industrial-relations/code-on-social-security-2020/index.html":
    "Master the Code on Social Security 2020 for UPSC APFC with complete statutory concepts, comparison tables, visual maps, mnemonics, and mock tests.", // 146
  "upsc-apfc/labour-codes-and-industrial-relations/code-on-wages-2019/index.html":
    "Master the Code on Wages 2019 for UPSC APFC with updated Central Rules, minimum wage provisions, floor wages, statutory definitions, and tests.", // 143
  "upsc-apfc/labour-codes-and-industrial-relations/labour-codes-overview-and-comparison/index.html":
    "Master the 4 New Labour Codes for UPSC APFC with detailed comparative tables, statutory timelines, key amendments, mnemonics, and practice MCQs.", // 145
  "upsc-apfc/polity-and-governance/emergency-provisions/index.html":
    "Master Emergency Provisions for UPSC APFC with constitutional articles, high-yield comparison tables, memory mnemonics, and active recall drills.", // 146

  // === CLASS 9 SCIENCE (32) ===
  "class-9-science/chapter-1-exploration-entering-world-of-secondary-science/concepts/index.html":
    "Master Class 9 Science Chapter 1 core scientific concepts and interactive models with clear explanations, NCERT notes, practice questions, and quizzes.", // 151
  "class-9-science/chapter-1-exploration-entering-world-of-secondary-science/index.html":
    "Explore Class 9 Science Chapter 1: Exploration and Scientific Thinking with complete syllabus guides, clear explanations, diagrams, and study resources.", // 153
  "class-9-science/chapter-1-exploration-entering-world-of-secondary-science/tests/index.html":
    "Test your knowledge of Class 9 Science Chapter 1 with chapter practice tests, timed mock questions, detailed answer solutions, and exam review notes.", // 151
  "class-9-science/chapter-10-sound-waves-characteristics-and-applications/index.html":
    "Master Sound Waves and Their Characteristics in Class 9 Science Chapter 10 with clear concepts, NCERT exercise support, practice questions, and quizzes.", // 153
  "class-9-science/chapter-11-reproduction-how-life-continues/index.html":
    "Explore Class 9 Science Chapter 11: Reproduction with complete syllabus guidance, clear biological explanations, practice questions, and revision notes.", // 153
  "class-9-science/chapter-12-patterns-in-life-diversity-and-classification/concepts/index.html":
    "Master Class 9 Science Chapter 12 Life Diversity and Classification with interactive concept models, clear biological diagrams, and practice questions.", // 152
  "class-9-science/chapter-12-patterns-in-life-diversity-and-classification/index.html":
    "Study Patterns in Life and Diversity for Class 9 Science Chapter 12 with NCERT curriculum support, detailed topic guides, quizzes, and revision notes.", // 151
  "class-9-science/chapter-12-patterns-in-life-diversity-and-classification/ncert-exercises/index.html":
    "Solve Class 9 Science Chapter 12 Life Diversity and Classification NCERT exercises with step-by-step solutions, key points, and exam practice questions.", // 153
  "class-9-science/chapter-12-patterns-in-life-diversity-and-classification/revision-notes/index.html":
    "Revise Class 9 Science Chapter 12 Life Diversity and Classification with quick revision notes, key classification mnemonics, and summary mind maps.", // 147
  "class-9-science/chapter-13-earth-as-a-system-energy-matter-and-life/index.html":
    "Explore Earth as a System in Class 9 Science Chapter 13 with comprehensive guides on energy flow, matter cycles, NCERT questions, and practice quizzes.", // 151
  "class-9-science/chapter-2-cell-building-block-of-life/index.html":
    "Master Class 9 Science Chapter 2: Cell - The Building Block of Life with detailed cell structure guides, organelle diagrams, and practice questions.", // 149
  "class-9-science/chapter-3-tissues-in-action/index.html":
    "Study Class 9 Science Chapter 3: Tissues in Action with complete plant and animal tissue overviews, clear diagrams, exam prep, and practice questions.", // 151
  "class-9-science/chapter-3-tissues-in-action/ncert-exercises/index.html":
    "Solve NCERT exercise solutions for Class 9 Science Chapter 3 Tissues in Action with step-by-step answers, diagrams, revision tips, and practice MCQs.", // 150
  "class-9-science/chapter-4-describing-motion-around-us/concepts/index.html":
    "Master Class 9 Science Chapter 4 Describing Motion with interactive speed, velocity, and acceleration models, clear explanations, and practice questions.", // 153
  "class-9-science/chapter-4-describing-motion-around-us/index.html":
    "Explore Class 9 Science Chapter 4: Describing Motion Around Us with comprehensive syllabus overviews, motion formulas, graphs, and solved practice drills.", // 155
  "class-9-science/chapter-4-describing-motion-around-us/ncert-exercises/index.html":
    "Solve NCERT exercise questions for Class 9 Science Chapter 4 Describing Motion with complete numerical solutions, graph explanations, and test tips.", // 148
  "class-9-science/chapter-5-exploring-mixtures-and-their-separation/concepts/index.html":
    "Master Class 9 Science Chapter 5 Mixtures and Their Separation with interactive separation technique models, concept notes, and practice questions.", // 148
  "class-9-science/chapter-5-exploring-mixtures-and-their-separation/index.html":
    "Study Class 9 Science Chapter 5: Exploring Mixtures and Separation with thorough syllabus notes, experiment steps, diagrams, and practice questions.", // 149
  "class-9-science/chapter-5-exploring-mixtures-and-their-separation/ncert-exercises/index.html":
    "Solve NCERT exercise solutions for Class 9 Science Chapter 5 Mixtures and Separation with clear step-by-step answers and revision practice questions.", // 150
  "class-9-science/chapter-6-how-forces-affect-motion/concepts/index.html":
    "Master Class 9 Science Chapter 6 How Forces Affect Motion with interactive Newton's laws models, force balance concepts, and solved practice drills.", // 148
  "class-9-science/chapter-6-how-forces-affect-motion/index.html":
    "Explore Class 9 Science Chapter 6: How Forces Affect Motion with complete syllabus guides, inertia concepts, momentum formulas, and practice questions.", // 152
  "class-9-science/chapter-6-how-forces-affect-motion/ncert-exercises/index.html":
    "Solve Class 9 Science Chapter 6 How Forces Affect Motion NCERT exercises with step-by-step momentum calculations, solutions, and exam practice tips.", // 149
  "class-9-science/chapter-6-how-forces-affect-motion/revision-notes/index.html":
    "Revise Class 9 Science Chapter 6 How Forces Affect Motion with quick summary notes, Newton's laws formulas, mnemonics, and key exam revision points.", // 148
  "class-9-science/chapter-7-work-energy-and-simple-machines/concepts/index.html":
    "Master Class 9 Science Chapter 7 Work, Energy and Simple Machines with interactive physics models, power formulas, and solved practice questions.", // 146
  "class-9-science/chapter-7-work-energy-and-simple-machines/index.html":
    "Study Class 9 Science Chapter 7: Work, Energy and Simple Machines with full syllabus coverage, kinetic and potential energy guides, and exam practice.", // 152
  "class-9-science/chapter-7-work-energy-and-simple-machines/ncert-exercises/index.html":
    "Solve Class 9 Science Chapter 7 Work, Energy and Simple Machines NCERT exercises with complete numerical solutions, formulas, and practice questions.", // 150
  "class-9-science/chapter-7-work-energy-and-simple-machines/revision-notes/index.html":
    "Revise Class 9 Science Chapter 7 Work, Energy and Simple Machines with concise formula sheets, conservation of energy notes, and exam mnemonics.", // 145
  "class-9-science/chapter-8-journey-inside-atom/concepts/index.html":
    "Master Class 9 Science Chapter 8 Journey Inside the Atom with interactive atomic models, subatomic particle charts, and concept practice questions.", // 148
  "class-9-science/chapter-8-journey-inside-atom/index.html":
    "Explore Class 9 Science Chapter 8: Journey Inside the Atom with complete syllabus notes, Thomson and Rutherford atomic models, and practice questions.", // 151
  "class-9-science/chapter-9-atomic-foundations-of-matter/concepts/index.html":
    "Master Class 9 Science Chapter 9 Atomic Foundations of Matter with interactive valency models, chemical formula rules, and concept practice drills.", // 147
  "class-9-science/chapter-9-atomic-foundations-of-matter/index.html":
    "Study Class 9 Science Chapter 9: Atomic Foundations of Matter with molecular mass tutorials, mole concept guides, formulas, and practice questions.", // 148
  "class-9-science/chapter-9-atomic-foundations-of-matter/revision-notes/index.html":
    "Revise Class 9 Science Chapter 9 Atomic Foundations of Matter with concise mole concept notes, chemical formula mnemonics, and exam practice tips.", // 146

  // === UPPSC RO/ARO (55) ===
  "uppsc-ro-aro/agriculture/agricultural-revolutions-soils/index.html":
    "Master UPPSC RO/ARO Agricultural Revolutions and Soil Classification with comprehensive notes, previous year questions (PYQs), and mock test drills.", // 149
  "uppsc-ro-aro/agriculture/commerce-foreign-trade-industry/index.html":
    "Master UPPSC RO/ARO Commerce, Foreign Trade Policy, and Balance of Payments with in-depth notes, previous year questions (PYQs), and mock test series.", // 152
  "uppsc-ro-aro/agriculture/commercial-crops-inputs-irrigation/index.html":
    "Master UPPSC RO/ARO Commercial Cash Crops, Farm Mechanisation, and Irrigation Systems with detailed study notes, PYQ analysis, and 3-level mock tests.", // 151
  "uppsc-ro-aro/agriculture/cropping-patterns-food-crops/index.html":
    "Master UPPSC RO/ARO Cropping Patterns, Agricultural Seasons, and Major Food Crops with structured study notes, previous year questions, and mock tests.", // 151
  "uppsc-ro-aro/economy/banking-monetary-policy-rbi/index.html":
    "Master UPPSC RO/ARO Banking System in India, Reserve Bank of India, and Monetary Policy with concise study notes, previous year questions, and tests.", // 149
  "uppsc-ro-aro/economy/economic-planning-niti-aayog/index.html":
    "Master UPPSC RO/ARO Economic Planning in India, Five-Year Plans, and NITI Aayog with high-yield revision notes, previous year questions, and tests.", // 147
  "uppsc-ro-aro/economy/fiscal-policy-budget-taxation/index.html":
    "Master UPPSC RO/ARO Fiscal Policy, Union Budget Architecture, and Taxation Systems with clear conceptual notes, previous year questions, and practice.", // 150
  "uppsc-ro-aro/economy/indian-culture-heritage/index.html":
    "Master UPPSC RO/ARO Indian Culture, Classical Arts, and Architectural Heritage with comprehensive study notes, previous year questions, and mock tests.", // 151
  "uppsc-ro-aro/economy/national-income-gdp-measurement/index.html":
    "Master UPPSC RO/ARO National Income Accounting and GDP Measurement Methodologies with clear formula notes, previous year questions, and practice drills.", // 153
  "uppsc-ro-aro/economy/poverty-inequality-unemployment/index.html":
    "Master UPPSC RO/ARO Poverty Estimation, Inequality Metrics, and Social Welfare Programs with targeted study notes, previous year questions, and tests.", // 150
  "uppsc-ro-aro/geography/agriculture-industries-transport-india/index.html":
    "Master UPPSC RO/ARO Agriculture, Major Industries, and Transport of India with comprehensive geography notes, previous year questions, and test drills.", // 151
  "uppsc-ro-aro/geography/great-northern-plains-peninsular-plateau/index.html":
    "Master UPPSC RO/ARO Northern Plains, Peninsular Plateau, Coasts, and Islands with detailed physiographic notes, previous year questions, and quizzes.", // 150
  "uppsc-ro-aro/geography/lithosphere-plate-tectonics-landforms/index.html":
    "Master UPPSC RO/ARO Lithosphere, Plate Tectonics, and Continental Landforms with conceptual geography notes, previous year questions, and test engines.", // 151
  "uppsc-ro-aro/geography/soils-natural-vegetation-forests-india/index.html":
    "Master UPPSC RO/ARO Soils, Natural Vegetation, and Forests of India with high-yield geography notes, previous year questions (PYQs), and mock tests.", // 149
  "uppsc-ro-aro/geography/world-agriculture-industrial-regions/index.html":
    "Master UPPSC RO/ARO World Agricultural Belts and Major Industrial Clusters with complete global geography notes, previous year questions, and tests.", // 149
  "uppsc-ro-aro/geography/world-rivers-lakes-drainage/index.html":
    "Master UPPSC RO/ARO World Rivers, Drainage Basins, and Major Lakes with comprehensive global geography notes, previous year questions, and mock tests.", // 151
  "uppsc-ro-aro/geography/world-straits-canals-maritime-routes/index.html":
    "Master UPPSC RO/ARO Strategic Straits, Canals, and Maritime Trade Routes with detailed world geography notes, previous year questions, and test drills.", // 152
  "uppsc-ro-aro/history/chauri-chaura-swaraj-party/index.html":
    "Master UPPSC RO/ARO Chauri Chaura Incident, Movement Suspension, and Swaraj Party with in-depth modern history notes, previous year questions, and tests.", // 154
  "uppsc-ro-aro/history/communal-award-poona-pact/index.html":
    "Master UPPSC RO/ARO Round Table Conferences, Communal Award, and Poona Pact with detailed modern history notes, previous year questions, and mock tests.", // 153
  "uppsc-ro-aro/history/cripps-mission-quit-india/index.html":
    "Master UPPSC RO/ARO Cripps Mission, Quit India Movement, and Parallel Governments with high-yield modern history notes, PYQs, and 3-level tests.", // 144
  "uppsc-ro-aro/history/home-rule-lucknow-pact/index.html":
    "Master UPPSC RO/ARO Home Rule League Movement and Lucknow Pact with comprehensive modern history study notes, previous year questions, and test engines.", // 153
  "uppsc-ro-aro/history/ina-subhash-bose-rin-mutiny/index.html":
    "Master UPPSC RO/ARO Indian National Army, Subhash Bose, and RIN Mutiny with detailed modern history study notes, previous year questions, and mock tests.", // 153
  "uppsc-ro-aro/history/lahore-congress-purna-swaraj/index.html":
    "Master UPPSC RO/ARO Lahore Congress Session, Purna Swaraj, and Independence Day with complete modern history study notes, PYQs, and mock test drills.", // 151
  "uppsc-ro-aro/history/mahajanapadas-magadha/index.html":
    "Master UPPSC RO/ARO 16 Mahajanapadas, Rise of Magadha, and Foreign Invasions with structured ancient history notes, previous year questions, and tests.", // 151
  "uppsc-ro-aro/history/moderate-phase-drain-wealth/index.html":
    "Master UPPSC RO/ARO Moderate Phase of Congress and Drain of Wealth Theory with analytical history study notes, previous year questions, and test drills.", // 152
  "uppsc-ro-aro/history/mountbatten-plan-independence/index.html":
    "Master UPPSC RO/ARO Mountbatten Plan, Independence Act 1947, and State Integration with detailed modern history notes, previous year questions, and tests.", // 155
  "uppsc-ro-aro/history/prehistoric-period/index.html":
    "Master UPPSC RO/ARO Prehistoric Period, Stone Age, and Chalcolithic Cultures with comprehensive ancient history notes, previous year questions, and tests.", // 154
  "uppsc-ro-aro/history/round-table-gandhi-irwin-karachi/index.html":
    "Master UPPSC RO/ARO Gandhi-Irwin Pact, Round Table Conference, and Karachi Session with in-depth modern history notes, PYQs, and 3-level test engines.", // 151
  "uppsc-ro-aro/history/rowlatt-jallianwala-non-cooperation/index.html":
    "Master UPPSC RO/ARO Rowlatt Act, Jallianwala Bagh, and Non-Cooperation Movement with detailed modern history notes, PYQ analysis, and mock tests.", // 147
  "uppsc-ro-aro/history/simon-commission-nehru-report/index.html":
    "Master UPPSC RO/ARO Simon Commission, Nehru Report, and Jinnah's 14 Points with comprehensive modern history notes, previous year questions, and tests.", // 152
  "uppsc-ro-aro/history/surat-split-morley-minto-ghadar/index.html":
    "Master UPPSC RO/ARO Surat Split, Morley-Minto Reforms, and Ghadar Movement with structured modern history study notes, previous year questions, and tests.", // 154
  "uppsc-ro-aro/history/wavell-plan-cabinet-mission/index.html":
    "Master UPPSC RO/ARO Wavell Plan, Shimla Conference, and Cabinet Mission Plan with high-yield modern history study notes, PYQs, and 3-level test drills.", // 152
  "uppsc-ro-aro/history/ww2-resignation-august-offer/index.html":
    "Master UPPSC RO/ARO World War II Resignations, August Offer, and Individual Satyagraha with detailed history study notes, PYQs, and mock test drills.", // 150
  "uppsc-ro-aro/polity/constitution-making-features-amendments/index.html":
    "Master UPPSC RO/ARO Constitution Making, Salient Features, and Landmark Amendments with comprehensive polity study notes, PYQs, and 3-level tests.", // 147
  "uppsc-ro-aro/polity/constitutional-statutory-bodies/index.html":
    "Master UPPSC RO/ARO Constitutional, Statutory, and Non-Constitutional Bodies with structured Indian polity study notes, previous year questions, and tests.", // 155
  "uppsc-ro-aro/polity/dpsp-fundamental-duties/index.html":
    "Master UPPSC RO/ARO Directive Principles of State Policy and Fundamental Duties with concise Indian polity notes, previous year questions, and mock tests.", // 153
  "uppsc-ro-aro/polity/federalism-centre-state-relations-emergency/index.html":
    "Master UPPSC RO/ARO Federalism, Centre-State Relations, and Emergency Provisions with detailed Indian polity notes, PYQ analysis, and mock test drills.", // 152
  "uppsc-ro-aro/population-ecology/ecology-biodiversity-conservation/index.html":
    "Master UPPSC RO/ARO Ecology, Biodiversity Hotspots, and Conservation in India & UP with comprehensive environment notes, PYQs, and mock test drills.", // 150
  "uppsc-ro-aro/population-ecology/environmental-pollution-climate-change/index.html":
    "Master UPPSC RO/ARO Environmental Pollution, Climate Change, and Net Zero Pathways with updated environmental study notes, PYQs, and 3-level tests.", // 149
  "uppsc-ro-aro/population-ecology/migration-trends-india/index.html":
    "Master UPPSC RO/ARO Migration Dynamics, Inter-State Corridors, and Impact in India & UP with structured demographic notes, PYQs, and mock test drills.", // 152
  "uppsc-ro-aro/population-ecology/urbanisation-problems-missions/index.html":
    "Master UPPSC RO/ARO Urbanisation Dynamics, Slum Challenges, and Urban Missions with high-yield population study notes, PYQs, and 3-level test engines.", // 152
  "uppsc-ro-aro/science/biology-nutrition-vitamins-human-health/index.html":
    "Master UPPSC RO/ARO Nutrition, Vitamins, Minerals, and Human Health with high-yield general science study notes, previous year questions, and mock tests.", // 152
  "uppsc-ro-aro/science/biology-plant-physiology-botany/index.html":
    "Master UPPSC RO/ARO Plant Physiology, Botany, and Economic Plants with comprehensive general science study notes, previous year questions, and mock tests.", // 152
  "uppsc-ro-aro/science/biotechnology-nuclear-energy-nanotechnology/index.html":
    "Master UPPSC RO/ARO Biotechnology, Nuclear Energy, and Nanotechnology with modern science study notes, previous year questions (PYQs), and mock tests.", // 149
  "uppsc-ro-aro/science/chemistry-carbon-compounds-applied-chemistry/index.html":
    "Master UPPSC RO/ARO Carbon Compounds and Applied Chemistry with clear general science study notes, previous year questions (PYQs), and 3-level mock tests.", // 152
  "uppsc-ro-aro/science/information-technology-telecom-ai-robotics/index.html":
    "Master UPPSC RO/ARO Information Technology, Telecommunications, AI, and Robotics with concise science study notes, previous year questions, and mock tests.", // 154
  "uppsc-ro-aro/science/science-technology-everyday-life-policies/index.html":
    "Master UPPSC RO/ARO Science and Technology in Everyday Life and National Missions with complete science study notes, PYQs, and 3-level test engines.", // 149
  "uppsc-ro-aro/science/space-technology-isro-missions-remote-sensing/index.html":
    "Master UPPSC RO/ARO Space Technology, ISRO Launchers, and Remote Sensing with high-yield general science notes, previous year questions, and mock tests.", // 151
  "uppsc-ro-aro/up-special/up-agriculture-livestock-forests/index.html":
    "Master UPPSC RO/ARO Agriculture, Agro-Climatic Zones, and UP Forests with comprehensive UP Special study notes, previous year questions, and mock tests.", // 151
  "uppsc-ro-aro/up-special/up-art-culture-heritage/index.html":
    "Master UPPSC RO/ARO Art, Culture, Fairs, Festivals, and Heritage of UP with high-yield UP Special notes, previous year questions, and 3-level mock tests.", // 153
  "uppsc-ro-aro/up-special/up-economy-industries-odop/index.html":
    "Master UPPSC RO/ARO Economy, Industrial Clusters, and ODOP Scheme of UP with detailed UP Special notes, previous year questions, and 3-level test drills.", // 153
  "uppsc-ro-aro/up-special/up-education-research-institutes/index.html":
    "Master UPPSC RO/ARO Education, Research Institutes, and Universities of UP with structured UP Special notes, previous year questions, and mock tests.", // 149
  "uppsc-ro-aro/up-special/up-geography-drainage-irrigation/index.html":
    "Master UPPSC RO/ARO Physiography, Drainage Systems, and Irrigation of UP with comprehensive UP Special notes, previous year questions, and mock tests.", // 149
  "uppsc-ro-aro/up-special/up-history-freedom-struggle/index.html":
    "Master UPPSC RO/ARO History of Uttar Pradesh and the Freedom Struggle with detailed UP Special study notes, previous year questions (PYQs), and mock tests.", // 154
  "uppsc-ro-aro/up-special/up-infrastructure-transport-admin/index.html":
    "Master UPPSC RO/ARO Expressways, Airports, Transport, and Administration of UP with concise UP Special notes, previous year questions, and mock tests." // 151
};

// 1. Validation check
const findings = JSON.parse(fs.readFileSync(path.join(__dirname, 'source_audit_findings.json'), 'utf8'));
const targetFiles = findings.truncatedDescription.map(x => x.file);

console.log(`Target files from source_audit_findings: ${targetFiles.length}`);
console.log(`Descriptions mapped: ${Object.keys(descriptions).length}`);

let errorCount = 0;
for (const f of targetFiles) {
  if (!descriptions[f]) {
    console.error(`MISSING MAPPING for: ${f}`);
    errorCount++;
  }
}

for (const [f, desc] of Object.entries(descriptions)) {
  if (desc.length < 140 || desc.length > 155) {
    console.error(`INVALID LENGTH (${desc.length}) for ${f}: "${desc}"`);
    errorCount++;
  }
  if (desc.endsWith('...') || desc.endsWith(',') || desc.endsWith(' and') || desc.endsWith(' or') || desc.endsWith(' with')) {
    console.error(`INVALID ENDING for ${f}: "${desc}"`);
    errorCount++;
  }
}

if (errorCount > 0) {
  console.error(`Found ${errorCount} errors. Aborting remediation.`);
  process.exit(1);
}

console.log('All 116 mappings passed validation! Applying updates...');

function updateFileMeta(filePath, newDesc) {
  let content = fs.readFileSync(filePath, 'utf8');
  let original = content;

  // 1. Update <meta name="description">, <meta property="og:description">, and <meta name="twitter:description">
  content = content.replace(/<meta\s+([^>]*?)>/gi, (tag, attrs) => {
    const isDesc = /name=["']description["']/i.test(attrs);
    const isOgDesc = /property=["']og:description["']/i.test(attrs);
    const isTwDesc = /name=["']twitter:description["']/i.test(attrs);

    if (isDesc || isOgDesc || isTwDesc) {
      return tag.replace(/content=(["'])([\s\S]*?)\1/i, (m, quote) => {
        return `content=${quote}${newDesc}${quote}`;
      });
    }
    return tag;
  });

  // 2. Update JSON-LD if truncated or template
  content = content.replace(/<script\s+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi, (scriptBlock, jsonText) => {
    if (jsonText.includes('...') || jsonText.includes('SEO description here') || /"description":\s*"[^"]*,\s*and\b/i.test(jsonText)) {
      const updatedJson = jsonText.replace(/"description":\s*"([^"]*)"/gi, (m, oldDesc) => {
        if (oldDesc.includes('...') || oldDesc.includes('SEO description here') || oldDesc.endsWith(' and')) {
          return `"description": "${newDesc}"`;
        }
        return m;
      });
      return scriptBlock.replace(jsonText, updatedJson);
    }
    return scriptBlock;
  });

  if (content !== original) {
    fs.writeFileSync(filePath, content, 'utf8');
    return true;
  }
  return false;
}

let updatedCount = 0;
for (const [relPath, newDesc] of Object.entries(descriptions)) {
  const fullPath = path.resolve(ROOT_DIR, relPath);
  if (updateFileMeta(fullPath, newDesc)) {
    updatedCount++;
  } else {
    console.warn(`No changes applied to: ${relPath}`);
  }
}

console.log(`Successfully updated ${updatedCount} / ${Object.keys(descriptions).length} files.`);
