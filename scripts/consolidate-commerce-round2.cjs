const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const consolidations = [
  // 1. Auditing Foundations (3 -> 1)
  {
    targetDir: 'commerce/auditing/meaning-objectives-and-significance',
    title: 'Auditing: Meaning, Objectives, and Significance',
    unitNameTgt: 'Auditing',
    unitNamePgt: 'Section A',
    oldDirs: [
      'commerce/auditing/definition-of-auditing',
      'commerce/auditing/objectives-of-auditing',
      'commerce/auditing/significance-of-auditing'
    ],
    summaryIntro: 'A complete foundational guide to Auditing, tracing its historical roots from the Latin word "Audire" (to hear), definition under international standards, primary vs secondary objectives, and practical significance.',
    points: [
      { bold: 'Origin & Concept of Auditing:', desc: 'Derived from Latin "audire". Systematic, independent examination of books, accounts, statutory records, documents and vouchers of an organization to ensure true and fair view.' },
      { bold: 'Primary vs Secondary Objectives:', desc: 'Primary: Expressing an objective opinion on financial statements. Secondary: Detection and prevention of errors (clerical, commission, omission, principle, compensating) and fraud (misappropriation of cash/goods, manipulation of accounts).' },
      { bold: 'Basic Principles Governing an Audit:', desc: 'Integrity, objectivity, independence, confidentiality, technical competence, documentation, and compliance with auditing standards (SA).' },
      { bold: 'Significance & Advantages:', desc: 'Protection of shareholder/owner interests, moral check on employees, assists taxation assessments, facilitates loan approvals, and enhances credibility.' }
    ]
  },

  // 2. Books of Original Entry & Ledger (3 -> 1)
  {
    targetDir: 'commerce/accounting-fundamentals/books-of-original-entry-and-ledger',
    title: 'Books of Original Entry: Journal, Ledger, and Trial Balance',
    unitNameTgt: 'Book-keeping and Accounting',
    unitNamePgt: 'Section A - Accounting',
    oldDirs: [
      'commerce/accounting-fundamentals/journal',
      'commerce/accounting-fundamentals/ledger',
      'commerce/accounting-fundamentals/trial-balance'
    ],
    summaryIntro: 'A foundational accounting module detailing the sequential flow of transactions: recording in books of prime entry (Journal & subsidiary books), classifying into accounts (Ledger), and verifying arithmetical accuracy (Trial Balance).',
    points: [
      { bold: 'Journal & Rules of Debit/Credit:', desc: 'Primary book of daily chronological record. Golden rules for Personal Accounts (Debit receiver, Credit giver), Real Accounts (Debit what comes in, Credit what goes out), and Nominal Accounts (Debit all expenses/losses, Credit all incomes/gains).' },
      { bold: 'Subsidiary Books:', desc: 'Specialized journals: Cash Book, Purchases Book, Sales Book, Return Inward/Outward Books, Bills Receivable/Payable, and Journal Proper.' },
      { bold: 'Ledger & Posting Process:', desc: 'Principal book of accounts containing all personal, real, and nominal accounts. Rules of posting, folio referencing, and balancing (debit vs credit balance).' },
      { bold: 'Trial Balance & Error Verification:', desc: 'Statement of debit and credit balances prepared to establish arithmetical accuracy. Distinguishes errors disclosed by trial balance from errors not disclosed (compensating, complete omission, principle errors).' }
    ]
  },

  // 3. Accounting Principles & Double Entry (2 -> 1)
  {
    targetDir: 'commerce/accounting-fundamentals/principles-and-double-entry',
    title: 'Accounting Concepts, Conventions, and Double Entry System',
    unitNameTgt: 'Book-keeping and Accounting',
    unitNamePgt: 'Section A - Accounting',
    oldDirs: [
      'commerce/accounting-fundamentals/accounting-concepts-and-conventions',
      'commerce/accounting-fundamentals/double-entry-system'
    ],
    summaryIntro: 'A definitive study of Generally Accepted Accounting Principles (GAAP), accounting concepts, conventions, and the dual aspect foundation of modern double entry bookkeeping.',
    points: [
      { bold: 'Double Entry Bookkeeping System:', desc: 'Origin by Fra Luca Pacioli (1494). Dual aspect equation: Assets = Liabilities + Capital. Every transaction has equal and opposite debit and credit effects.' },
      { bold: 'Fundamental Accounting Concepts:', desc: 'Business Entity Concept, Money Measurement, Going Concern, Accounting Period, Cost Concept, Dual Aspect, Realization, and Accrual Concept.' },
      { bold: 'Accounting Conventions:', desc: 'Convention of Full Disclosure, Consistency, Materiality, and Conservatism / Prudence ("Anticipate no profit, provide for all possible losses").' },
      { bold: 'Accounting Standards & IND AS:', desc: 'Role of ICAI and convergence with International Financial Reporting Standards (IFRS) to ensure uniformity, comparability, and transparency.' }
    ]
  },

  // 4. Business Environment Dimensions (4 -> 1)
  {
    targetDir: 'commerce/business-environment/dimensions-of-business-environment',
    title: 'Dimensions of Business Environment: Economic, Social, Cultural, and Political',
    unitNameTgt: 'Business Environment',
    unitNamePgt: 'Section C - Business Environment',
    oldDirs: [
      'commerce/business-environment/economic-environment',
      'commerce/business-environment/social-environment',
      'commerce/business-environment/cultural-environment',
      'commerce/business-environment/political-environment'
    ],
    summaryIntro: 'An in-depth analysis of macro-environmental forces shaping business decisions in India: economic policies, socio-cultural values, demographic structures, and political-legal governance.',
    points: [
      { bold: 'Economic Environment:', desc: 'Economic system (Mixed economy), Fiscal & Monetary policy, industrial licensing, inflation rate, per capita income, and LPG reforms (Liberalisation, Privatisation, Globalisation 1991).' },
      { bold: 'Social & Cultural Environment:', desc: 'Customs, traditions, values, literacy rate, urbanization, family structure, taste patterns, consumer lifestyle changes, and corporate social responsibility (CSR).' },
      { bold: 'Political-Legal Framework:', desc: 'Political stability, government ideology, constitution, legislative enactments (Companies Act, MRTP/Competition Act, FEMA, Consumer Protection Act), and judicial decisions.' },
      { bold: 'Strategic Business Adaptation:', desc: 'Environmental scanning, PESTLE analysis, and managerial flexibility in responding to dynamic global and domestic threats and opportunities.' }
    ]
  },

  // 5. Forms of Business Organization (4 -> 1)
  {
    targetDir: 'commerce/business-organization/forms-of-business-organization',
    title: 'Forms of Business Organization: Sole Proprietorship, Partnership, and Company',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/business-organization/forms-of-business-organization',
      'commerce/business-organization/sole-proprietorship',
      'commerce/business-organization/partnership',
      'commerce/business-organization/company'
    ],
    summaryIntro: 'A comprehensive comparative chapter on ownership structures in commerce: Sole Proprietorship, General Partnership (Indian Partnership Act 1932), and Joint Stock Companies (Companies Act 2013).',
    points: [
      { bold: 'Sole Proprietorship (One-Man Business):', desc: 'Oldest, simplest form. Single owner, unlimited liability, full managerial control, business secrecy, and lack of separate legal entity.' },
      { bold: 'Partnership (Indian Partnership Act, 1932):', desc: 'Relation between persons agreeing to share profits of a business carried on by all or any of them acting for all. Mutual agency, unlimited joint & several liability, minimum 2 / maximum 50 members.' },
      { bold: 'Joint Stock Company (Companies Act, 2013):', desc: 'Artificial person created by law, having separate legal entity, perpetual succession, common seal, and limited liability of shareholders. Private vs Public vs One Person Company (OPC).' },
      { bold: 'Comparative Criteria for Choice of Form:', desc: 'Capital requirements, risk exposure, legal formalities, managerial flexibility, operational scale, continuity, and tax liability.' }
    ]
  },

  // 6. Commercial Banking (3 -> 1)
  {
    targetDir: 'commerce/money-and-banking/commercial-banking',
    title: 'Commercial Banking: Functions, Structure, and Types of Banks',
    unitNameTgt: 'Banking',
    unitNamePgt: 'Section B - Money & Banking',
    oldDirs: [
      'commerce/money-and-banking/banking/commercial-banks',
      'commerce/money-and-banking/banking/functions-of-commercial-banks',
      'commerce/money-and-banking/banking/types-of-banks'
    ],
    summaryIntro: 'A complete overview of the commercial banking system in India: classification of scheduled vs non-scheduled banks, primary banking functions, secondary agency services, and credit creation mechanics.',
    points: [
      { bold: 'Meaning & Classification of Banks:', desc: 'Institutions accepting deposits for lending or investing. Scheduled vs Non-scheduled banks; Public Sector Banks, Private Banks, Regional Rural Banks (RRBs), Foreign Banks, Small Finance Banks, and Payment Banks.' },
      { bold: 'Primary Functions:', desc: 'Accepting deposits (Current, Savings, Fixed, Recurring) and Granting loans/advances (Overdraft, Cash Credit, Term Loans, Discounting bills of exchange).' },
      { bold: 'Agency & Utility Services:', desc: 'Collection of cheques, remittance facilities, demat accounts, locker services, underwriting, issuance of letters of credit and bank guarantees.' },
      { bold: 'Credit Creation Mechanism:', desc: 'How commercial banks create derivative deposits based on Cash Reserve Ratio (CRR) and initial primary cash deposits (Credit Multiplier = 1 / CRR).' }
    ]
  },

  // 7. International Financial Institutions (2 -> 1)
  {
    targetDir: 'commerce/money-and-banking/international-financial-institutions',
    title: 'International Financial Institutions: IMF and World Bank Group',
    unitNameTgt: 'Foreign Trade and International Finance',
    unitNamePgt: 'Section B - Money & Banking',
    oldDirs: [
      'commerce/money-and-banking/international-financial-institutions/international-monetary-fund',
      'commerce/money-and-banking/international-financial-institutions/world-bank'
    ],
    summaryIntro: 'Detailed analytical study of the Bretton Woods twins (1944): International Monetary Fund (IMF) for short-term balance of payments stability, and World Bank (IBRD/IDA) for long-term reconstruction and poverty alleviation.',
    points: [
      { bold: 'Bretton Woods Conference (1944):', desc: 'Establishment of IMF and IBRD to rebuild postwar international economic order and avoid beggar-thy-neighbour exchange depreciations.' },
      { bold: 'International Monetary Fund (IMF):', desc: 'Headquarters: Washington D.C. Objectives: exchange rate stability, multilateral payment systems, eliminating foreign exchange restrictions, short-term financial assistance for BoP disequilibrium.' },
      { bold: 'Special Drawing Rights (SDR) & Quota System:', desc: 'Created by IMF in 1969 as supplementary international reserve asset (paper gold). Valuation basket: USD, Euro, RMB, Yen, GBP. Voting power determined by quotas.' },
      { bold: 'World Bank Group (IBRD & Affiliates):', desc: 'IBRD (loans to middle-income governments), IDA ("soft loan window" for poorest nations), IFC (private sector financing), MIGA (political risk insurance), ICSID (investment disputes).' }
    ]
  },

  // 8. Demand Analysis (2 -> 1)
  {
    targetDir: 'commerce/business-economics/demand-analysis',
    title: 'Demand Analysis: Law of Demand and Elasticity of Demand',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/business-economics/demand/law-of-demand',
      'commerce/business-economics/demand/elasticity-of-demand'
    ],
    summaryIntro: 'A core Microeconomic foundation examining consumer demand determinants, the Law of Demand, causes of downward sloping demand curves, and price, income, and cross elasticity of demand.',
    points: [
      { bold: 'Meaning & Law of Demand:', desc: 'Inverse relationship between price of a good and quantity demanded, ceteris paribus (other factors remaining constant): Q_d = f(P).' },
      { bold: 'Reasons for Downward Slope & Exceptions:', desc: 'Law of Diminishing Marginal Utility, Substitution Effect, Income Effect, New Consumers, Multiple Uses. Exceptions: Giffen goods, Veblen/conspicuous consumption, emergency shortages, speculative goods.' },
      { bold: 'Price Elasticity of Demand (Ed):', desc: 'Responsiveness of quantity demanded to changes in price: Perfectly Inelastic (0), Inelastic (<1), Unitary (1), Elastic (>1), Perfectly Elastic (Infinity).' },
      { bold: 'Measurement Methods & Income/Cross Elasticity:', desc: 'Percentage / Proportionate method, Total Outlay / Expenditure method, Point / Geometric method. Income elasticity (positive for normal, negative for inferior) and Cross elasticity (positive for substitutes, negative for complements).' }
    ]
  },

  // 9. Production Theory (3 -> 1)
  {
    targetDir: 'commerce/business-economics/production-theory',
    title: 'Theory of Production: Production Function and Laws of Returns',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/business-economics/production/production-function',
      'commerce/business-economics/production/laws-of-production',
      'commerce/business-economics/production/laws-of-returns'
    ],
    summaryIntro: 'A comprehensive study of technical production relationships, short-run returns to a variable factor (Law of Variable Proportions), and long-run expansion paths (Returns to Scale).',
    points: [
      { bold: 'Production Function Concept:', desc: 'Physical and technical relationship between inputs and output per unit of time: Q = f(L, K, Land, E). Fixed vs variable factors.' },
      { bold: 'Short-Run: Law of Variable Proportions:', desc: 'As more of a variable factor is added to fixed factors, Total Product (TP), Marginal Product (MP), and Average Product (AP) pass through three distinct stages.' },
      { bold: 'Three Stages of Production:', desc: 'Stage I (Increasing Returns, MP > AP), Stage II (Diminishing Returns, rational stage where AP > MP > 0, ending where MP=0), Stage III (Negative Returns, MP < 0, TP decreases).' },
      { bold: 'Long-Run: Laws of Returns to Scale:', desc: 'All factors are variable in fixed proportions: Increasing Returns to Scale (internal/external economies), Constant Returns to Scale (linear homogeneous Cobb-Douglas), and Diminishing Returns to Scale (internal diseconomies of scale).' }
    ]
  },

  // 10. National Income & GDP (2 -> 1)
  {
    targetDir: 'commerce/business-economics/national-income-and-gdp',
    title: 'Macroeconomics: National Income, GDP, and Economic Aggregates',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/business-economics/macroeconomics/national-income',
      'commerce/business-economics/macroeconomics/gross-domestic-product'
    ],
    summaryIntro: 'A foundational macroeconomic chapter on National Income accounting, gross and net aggregates at market price and factor cost, circular flow of income, and estimation methods in India.',
    points: [
      { bold: 'Key Aggregates (GDP, GNP, NNP):', desc: 'GDP_mp (Gross Domestic Product at market prices), NDP = GDP - Depreciation, GNP = GDP + NFIA (Net Factor Income from Abroad), NNP_fc = National Income (NNP at factor cost = NNP_mp - Net Indirect Taxes).' },
      { bold: 'Real vs Nominal GDP & GDP Deflator:', desc: 'Nominal GDP at current prices vs Real GDP at constant base-year prices. GDP Deflator = (Nominal GDP / Real GDP) * 100.' },
      { bold: 'Three Measurement Methods:', desc: 'Product / Value Added Method (Gross Output - Intermediate Consumption), Income Method (Wages + Rent + Interest + Profit), and Expenditure Method (C + I + G + X - M).' },
      { bold: 'Measurement Difficulties in India:', desc: 'Non-monetized transactions, presence of large unorganized informal sector, illiteracy, lack of reliable accounting records, and double counting risks.' }
    ]
  },

  // 11. Cost Accounting Introduction & Elements (3 -> 1)
  {
    targetDir: 'commerce/cost-accounting/introduction-and-elements',
    title: 'Cost Accounting: Meaning, Objectives, Elements, and Methods',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Cost Accounting',
    oldDirs: [
      'commerce/cost-accounting/meaning-and-objectives-of-cost-accounting',
      'commerce/cost-accounting/elements-of-cost',
      'commerce/cost-accounting/methods-of-cost-accounting'
    ],
    summaryIntro: 'A complete introductory text on Cost Accounting principles, cost determination, cost control, structural elements of cost, and manufacturing cost sheet preparation.',
    points: [
      { bold: 'Meaning, Scope & Objectives:', desc: 'Systematic classification, recording, allocation, and analysis of expenditures for ascertaining product cost, controlling expenses, and aiding managerial price fixing.' },
      { bold: 'Elements of Cost:', desc: 'Material (Direct + Indirect), Labour (Direct + Indirect), and Expenses (Direct + Indirect). Prime Cost = Direct Material + Direct Labour + Direct Expenses.' },
      { bold: 'Overhead Classification & Cost Sheet:', desc: 'Factory/Works Overheads (Works Cost), Office & Administrative Overheads (Cost of Production), Selling & Distribution Overheads (Cost of Sales / Total Cost).' },
      { bold: 'Methods of Costing:', desc: 'Unit / Output costing (brickworks, sugar), Job costing (custom orders), Batch costing (pharmaceuticals), Contract costing (construction), Process costing (chemicals, oil refineries), Operating / Service costing (transport, hospitals).' }
    ]
  },

  // 12. Statistical Data Presentation (4 -> 1)
  {
    targetDir: 'commerce/statistics/collection-and-presentation-of-data',
    title: 'Collection, Classification, and Tabulation of Statistical Data',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/statistics/data-collection',
      'commerce/statistics/data-classification',
      'commerce/statistics/tabulation',
      'commerce/statistics/frequency'
    ],
    summaryIntro: 'A foundational statistical methods chapter detailing the primary data lifecycle: collection instruments, classification by attributes and variables, frequency distribution construction, and table design.',
    points: [
      { bold: 'Data Collection: Primary vs Secondary:', desc: 'Primary data methods (Direct personal interview, Indirect oral investigation, Information through correspondents, Questionnaires and Schedules). Secondary data sources and scrutiny criteria (reliability, suitability, adequacy).' },
      { bold: 'Classification of Statistical Data:', desc: 'Grouping data into homogeneous classes according to shared characteristics: Geographical / Spatial, Chronological / Temporal, Qualitative (by attributes), and Quantitative (by variables).' },
      { bold: 'Frequency Distributions:', desc: 'Discrete vs Continuous series. Class intervals, class limits, class mid-points, open-end classes, inclusive vs exclusive method of classification, cumulative frequency (less than / more than).' },
      { bold: 'Principles of Tabulation:', desc: 'Systematic presentation of data in columns and rows. Essential parts of a table: Table Number, Title, Head Note, Stub (row headings), Caption (column headings), Body, Footnote, and Source Note.' }
    ]
  },

  // 13. Official Statistics of India (3 -> 1)
  {
    targetDir: 'commerce/statistics/indian-statistics',
    title: 'Official Statistics of India: Agriculture, Industry, and Population',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/statistics/india-statistics/agriculture-statistics',
      'commerce/statistics/india-statistics/industrial-statistics',
      'commerce/statistics/india-statistics/population-statistics'
    ],
    summaryIntro: 'An authoritative study of Indian statistical systems, official government data collection agencies (NSO, MoSPI, Registrar General), and key agricultural, industrial, and demographic series.',
    points: [
      { bold: 'Statistical Architecture of India:', desc: 'National Statistical Office (NSO) formed by merging CSO (Central Statistical Office) and NSSO (National Sample Survey Office) under MoSPI.' },
      { bold: 'Agricultural Statistics:', desc: 'Land utilization classification, crop production statistics, Directorate of Economics and Statistics (DES), Agricultural Census (conducted every 5 years), and remote sensing data.' },
      { bold: 'Industrial Statistics:', desc: 'Index of Industrial Production (IIP - monthly series, current base year 2011-12), Annual Survey of Industries (ASI), and Eight Core Industries index.' },
      { bold: 'Population & Demographic Statistics:', desc: 'Decennial Census of India conducted under Census Act 1948 by Registrar General and Census Commissioner. Key parameters: Population growth rate, sex ratio, literacy rate, density, and Sample Registration System (SRS) for birth/death rates.' }
    ]
  }
];

function generateCommerceHtml(item) {
  const checklistItems = item.points.map(p => `
          <label class="check-item"><input type="checkbox"> <span><strong>${p.bold}</strong> ${p.desc}</span></label>`).join('');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${item.title} — Commerce Lecture Notes | SJ Maths</title>
  <meta name="description" content="${item.summaryIntro.replace(/"/g, '&quot;')}">
  <link rel="canonical" href="https://sjmaths.com/${item.targetDir}/">
  <link rel="icon" type="image/png" href="/favicon.png">
  <style>
    :root {
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --primary-light: #e0f2fe;
      --accent: #0f172a;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #334155;
      --heading: #0f172a;
      --border: #e2e8f0;
      --success: #16a34a;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --font: 'Inter', system-ui, -apple-system, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.6; padding-top: 60px; }
    header { position: fixed; top: 0; left: 0; right: 0; height: 60px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(8px); border-bottom: 1px solid var(--border); z-index: 1000; display: flex; align-items: center; justify-content: space-between; padding: 0 24px; }
    .brand { font-weight: 700; font-size: 1.25rem; color: var(--primary); text-decoration: none; display: flex; align-items: center; gap: 8px; }
    .nav-links { display: flex; gap: 16px; }
    .nav-links a { text-decoration: none; color: var(--text); font-size: 0.9rem; font-weight: 500; transition: color 0.2s; }
    .nav-links a:hover { color: var(--primary); }
    .container { max-width: 1100px; margin: 0 auto; padding: 40px 20px; }
    .hero { background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 36px; margin-bottom: 32px; box-shadow: var(--shadow); position: relative; overflow: hidden; }
    .hero::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(to right, var(--primary), #38bdf8); }
    .breadcrumb { font-size: 0.85rem; color: #64748b; margin-bottom: 12px; }
    .breadcrumb a { color: var(--primary); text-decoration: none; }
    h1 { font-size: 2rem; color: var(--heading); margin-bottom: 12px; line-height: 1.25; }
    .subtitle { font-size: 1.05rem; color: #475569; margin-bottom: 20px; max-width: 850px; }
    .badges { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
    .badge { padding: 4px 12px; border-radius: 9999px; font-size: 0.8rem; font-weight: 600; background: var(--primary-light); color: var(--primary-dark); }
    .main-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 32px; }
    @media (max-width: 768px) { .main-grid { grid-template-columns: 1fr; } }
    .card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 28px; margin-bottom: 24px; box-shadow: var(--shadow); }
    h2 { font-size: 1.35rem; color: var(--heading); margin-bottom: 16px; padding-bottom: 8px; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 8px; }
    p { margin-bottom: 16px; color: #475569; }
    .checklist { display: flex; flex-direction: column; gap: 12px; margin-top: 16px; }
    .check-item { display: flex; align-items: flex-start; gap: 10px; cursor: pointer; font-size: 0.92rem; }
    .check-item input { margin-top: 4px; accent-color: var(--primary); }
    .sidebar-card { background: white; border: 1px solid var(--border); border-radius: var(--radius); padding: 24px; box-shadow: var(--shadow); position: sticky; top: 84px; }
    .sidebar-card h3 { font-size: 1.1rem; color: var(--heading); margin-bottom: 12px; }
    .action-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px; margin-top: 16px; }
    .action-box strong { color: #166534; font-size: 0.95rem; }
    .action-box p { font-size: 0.82rem; color: #15803d; margin: 6px 0 12px; }
    .action-btn { display: inline-block; background: var(--primary); color: white; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; font-weight: 600; text-decoration: none; transition: background 0.2s; }
    .action-btn:hover { background: var(--primary-dark); }
    .footer { text-align: center; padding: 32px; border-top: 1px solid var(--border); color: #64748b; font-size: 0.85rem; margin-top: 48px; }
    .footer a { color: var(--primary); text-decoration: none; }
  </style>
</head>
<body>
<header>
  <a href="/" class="brand">SJ Maths</a>
  <nav class="nav-links">
    <a href="/">Home</a>
    <a href="/up-tgt-commerce/">TGT Commerce</a>
    <a href="/up-pgt-commerce/">PGT Commerce</a>
  </nav>
</header>

<div class="container">
  <section class="hero">
    <div class="breadcrumb">
      <a href="/">Home</a> / <a href="/commerce/">Commerce</a> / <span>${item.title}</span>
    </div>
    <h1>${item.title}</h1>
    <p class="subtitle">${item.summaryIntro}</p>
    <div class="badges">
      <span class="badge">Master Syllabus Chapter</span>
      <span class="badge">UP TGT &amp; PGT Commerce</span>
      <span class="badge">Complete Lecture Notes</span>
    </div>
  </section>

  <div class="main-grid">
    <div class="content-col">
      <article class="card">
        <h2>1. Syllabus Overview &amp; Exam Focus</h2>
        <p>In the official teacher recruitment and competitive syllabus, <strong>${item.title}</strong> is a core examination unit of <em>${item.unitNameTgt}</em>. Questions test definitions, accounting/management principles, legal provisions, formulas, and real-world commercial applications.</p>
        <p>Study this consolidated module systematically to master both theoretical fundamentals and examination numerical patterns.</p>
      </article>

      <article class="card">
        <h2>2. Key Concepts &amp; Essential Principles</h2>
        <p>Master the following core concepts for <strong>${item.title}</strong>:</p>
        <div class="checklist">${checklistItems}
        </div>
      </article>

      <article class="card">
        <h2>3. Self-Assessment &amp; Study Checklist</h2>
        <p>Use this interactive checklist to verify your exam preparation status for this topic:</p>
        <div class="checklist">
          <label class="check-item"><input type="checkbox"> <span>Read theoretical notes &amp; conceptual summary</span></label>
          <label class="check-item"><input type="checkbox"> <span>Memorized essential definitions, formulas &amp; accounting entries</span></label>
          <label class="check-item"><input type="checkbox"> <span>Solved minimum 20 previous years' questions (PYQ)</span></label>
          <label class="check-item"><input type="checkbox"> <span>Attempted timed self-assessment test</span></label>
          <label class="check-item"><input type="checkbox"> <span>Marked complete on main syllabus tracker</span></label>
        </div>
      </article>
    </div>

    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>Exam Tracker</h3>
        <p style="font-size:.84rem;color:#475569;margin:0 0 12px">Track this topic alongside the complete syllabus on your exam progress tracker.</p>
        <div class="action-box">
          <strong>UP TGT Commerce</strong>
          <p>Interactive progress tracking, instant search &amp; filter</p>
          <a class="action-btn" href="/up-tgt-commerce/">Open Tracker →</a>
        </div>
        <div class="action-box" style="margin-top:12px;background:#f0f9ff;border-color:#bae6fd">
          <strong style="color:#0369a1">UP PGT Commerce</strong>
          <p style="color:#0284c7">Advanced PGT syllabus tracking &amp; PYQ references</p>
          <a class="action-btn" href="/up-pgt-commerce/">Open PGT Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</div>

<footer class="footer">
  <span>SJ Maths • Master Subject Library • ${item.title}</span><br>
  <a href="https://sjmaths.com/">Home</a> &nbsp;•&nbsp;
  <a href="/up-tgt-commerce/">UP TGT Commerce</a> &nbsp;•&nbsp;
  <a href="/up-pgt-commerce/">UP PGT Commerce</a>
</footer>
</body>
</html>
`;
}

// 1. Create consolidated target pages
for (const item of consolidations) {
  const targetDirAbs = path.join(ROOT, item.targetDir);
  if (!fs.existsSync(targetDirAbs)) {
    fs.mkdirSync(targetDirAbs, { recursive: true });
  }

  const html = generateCommerceHtml(item);
  fs.writeFileSync(path.join(targetDirAbs, 'index.html'), html, 'utf8');
  console.log(`Created consolidated Commerce page: ${item.targetDir}/index.html`);
}

// 2. Delete older fragmented directories
let deletedTotal = 0;
for (const item of consolidations) {
  const targetDirAbs = path.join(ROOT, item.targetDir);
  for (const oldDir of item.oldDirs) {
    const oldDirAbs = path.join(ROOT, oldDir);
    if (oldDirAbs === targetDirAbs) continue; // Don't delete self if same
    if (fs.existsSync(oldDirAbs)) {
      fs.rmSync(oldDirAbs, { recursive: true, force: true });
      console.log(`  Deleted old: ${oldDir}`);
      deletedTotal++;
    }
  }
}
console.log(`Total fragmented Commerce sub-directories deleted: ${deletedTotal}`);

// 3. Clean up empty parent directories inside commerce
function cleanEmptyDirs(dir) {
  let isDir = false;
  try { isDir = fs.statSync(dir).isDirectory(); } catch (e) { return; }
  if (!isDir) return;

  const entries = fs.readdirSync(dir);
  for (const ent of entries) {
    const full = path.join(dir, ent);
    if (fs.statSync(full).isDirectory()) {
      cleanEmptyDirs(full);
    }
  }

  if (dir !== path.join(ROOT, 'commerce') && fs.readdirSync(dir).length === 0) {
    fs.rmdirSync(dir);
    console.log(`Removed empty parent directory: ${path.relative(ROOT, dir)}`);
  }
}
cleanEmptyDirs(path.join(ROOT, 'commerce'));

console.log('Commerce round 2 consolidation and cleanup complete.');
