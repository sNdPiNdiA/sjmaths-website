const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const consolidations = [
  // 1. Business Organization: Introduction and Scope (3 -> 1)
  {
    targetDir: 'commerce/business-organization/introduction-and-scope',
    title: 'Business Organization: Meaning, Nature of Trade, Commerce, and Industry',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/business-organization/meaning-and-nature-of-trade-and-commerce',
      'commerce/business-organization/industry',
      'commerce/business-organization/features-and-scope-of-business-organization'
    ],
    summaryIntro: 'A foundational comprehensive module covering the concepts of business, classification into Industry, Trade, and Commerce, characteristics of modern business organizations, and economic objectives.',
    points: [
      { bold: 'Concept of Business, Trade & Commerce:', desc: 'Business as an economic activity producing goods/services for profit. Trade as buying and selling. Commerce as trade plus aids to trade (transport, banking, insurance, warehousing, advertising).' },
      { bold: 'Classification of Industry:', desc: 'Primary (genetic, extractive), Secondary (manufacturing, construction), and Tertiary (service) industries. Heavy vs light, consumer vs capital goods.' },
      { bold: 'Features of Modern Business Organization:', desc: 'Economic institution, risk and uncertainty, continuous transactions, value addition, technological orientation, and social accountability.' },
      { bold: 'Scope and Interdependence:', desc: 'How commerce bridges geographical and temporal gaps between producers and ultimate consumers through specialized market intermediaries.' }
    ]
  },

  // 2. Company Accounts: Depreciation (Flatten nesting 1 -> 1)
  {
    targetDir: 'commerce/company-accounts/depreciation',
    title: 'Depreciation Accounting: Concepts, Causes, and Methods of Depreciation',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/company-accounts/depreciation/methods-of-depreciation'
    ],
    summaryIntro: 'Complete guide to depreciation accounting under AS-10 / Ind AS 16, detailing causes of asset wear and tear, Straight Line Method (SLM), Written Down Value (WDV), and accounting entries.',
    points: [
      { bold: 'Meaning, Need & Causes of Depreciation:', desc: 'Gradual, permanent decrease in book value of fixed tangible assets due to wear and tear, obsolescence, passage of time, or depletion.' },
      { bold: 'Straight Line Method (SLM / Fixed Instalment):', desc: 'Equal amount written off each year: (Cost - Scrap Value) / Life. Simplest method, suitable for assets with minimal maintenance changes.' },
      { bold: 'Written Down Value Method (WDV / Reducing Balance):', desc: 'Fixed percentage applied on diminishing opening balance. Recognised by Indian Income Tax Act; matches increasing repairs with decreasing depreciation.' },
      { bold: 'Other Methods & Disposal Accounting:', desc: 'Annuity method, Sinking Fund method, Insurance policy method, Revaluation method, and Machine Hour Rate method. Recording asset sales and profit/loss on disposal.' }
    ]
  },

  // 3. Business Economics: Nature & Scope (3 -> 1)
  {
    targetDir: 'commerce/business-economics/nature-and-scope',
    title: 'Business Economics: Definition, Nature, Scope, and Relationship with Trade',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/business-economics/definition-and-scope-of-economics',
      'commerce/business-economics/nature-and-scope-of-economics',
      'commerce/business-economics/relationship-between-trade-and-economics'
    ],
    summaryIntro: 'Comprehensive foundational module examining classical and modern definitions of economics, managerial economics as applied microeconomics, normative vs positive science, and its role in trade decisions.',
    points: [
      { bold: 'Evolution of Definitions:', desc: 'Wealth definition (Adam Smith), Welfare definition (Alfred Marshall), Scarcity definition (Lionel Robbins), and Growth definition (Paul Samuelson).' },
      { bold: 'Nature of Managerial / Business Economics:', desc: 'Applied microeconomics, pragmatic and problem-solving, normative in nature, prescriptive rather than descriptive, macroeconomic backdrop awareness.' },
      { bold: 'Scope of Business Economics:', desc: 'Demand analysis and forecasting, cost and production analysis, pricing policies, profit management, and capital budgeting.' },
      { bold: 'Economics and Modern Commerce / Trade:', desc: 'How market equilibrium, opportunity cost, and marginalism guide optimal resource allocation and competitive trade strategies.' }
    ]
  },

  // 4. Business Economics: Market Structures & Price Determination (3 -> 1)
  {
    targetDir: 'commerce/business-economics/market-structures-and-price',
    title: 'Market Structures: Perfect Competition, Monopoly, and Price Determination',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/business-economics/market-and-price/perfect-competition',
      'commerce/business-economics/market-and-price/monopoly',
      'commerce/business-economics/market-and-price/price-determination'
    ],
    summaryIntro: 'In-depth comparative analysis of product markets, revenue curves (AR & MR), short-run and long-run equilibrium of firms, price discrimination, and price determination mechanics.',
    points: [
      { bold: 'Perfect Competition:', desc: 'Large number of buyers/sellers, homogeneous products, free entry/exit, perfect knowledge, horizontal AR = MR curve. Price taker status where P = MR = MC.' },
      { bold: 'Monopoly & Price Discrimination:', desc: 'Single seller, no close substitutes, barriers to entry, downward sloping AR and MR curves. First, second, and third-degree price discrimination conditions.' },
      { bold: 'Equilibrium of Firm and Industry:', desc: 'Conditions of equilibrium: MR = MC and MC must cut MR from below. Abnormal profits, normal profits, and sub-normal losses in short run vs long run.' },
      { bold: 'Price Determination Under Different Horizons:', desc: 'Marshallian time elements: Market period (very short run), Short period, Long period, and Secular period pricing dynamics.' }
    ]
  },

  // 5. Business Economics: Macroeconomics — Trade Cycles and Population (2 -> 1)
  {
    targetDir: 'commerce/business-economics/macroeconomics/trade-cycles-and-population',
    title: 'Macroeconomics: Trade Cycles and Demographic / Population Theory',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/business-economics/macroeconomics/trade-cycle',
      'commerce/business-economics/macroeconomics/population-theory'
    ],
    summaryIntro: 'A core macroeconomic study of economic fluctuations, business cycle phases, monetary and fiscal stabilization policies, alongside Malthusian and Optimum demographic theories.',
    points: [
      { bold: 'Meaning & Phases of Trade / Business Cycles:', desc: 'Cyclical fluctuations in aggregate economic activity: Prosperity/Boom, Recession, Depression/Slump, and Recovery/Revival.' },
      { bold: 'Theories of Business Cycles:', desc: 'Hawtrey\'s Pure Monetary Theory, Hayek\'s Monetary Over-Investment Theory, Schumpeter\'s Innovation Theory, Keynesian Theory (effective demand and MEC).' },
      { bold: 'Measures to Control Economic Instability:', desc: 'Counter-cyclical fiscal policy (taxation, public spending, deficit financing) and central bank monetary policy (repo rate, CRR, OMO).' },
      { bold: 'Demographic Theories: Malthus vs Optimum Theory:', desc: 'Malthusian Theory (population grows geometrically, food supply arithmetically; preventive and positive checks) vs Modern Optimum Theory (maximizing per capita income; under, over, and optimum population).' }
    ]
  },

  // 6. Management: Functions of Management (7 -> 1)
  {
    targetDir: 'commerce/management/functions-of-management',
    title: 'Functions of Management: Planning, Organizing, Staffing, Directing, and Controlling',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/management/functions-of-management/planning',
      'commerce/management/functions-of-management/organization',
      'commerce/management/functions-of-management/staffing',
      'commerce/management/functions-of-management/direction',
      'commerce/management/functions-of-management/motivation',
      'commerce/management/functions-of-management/coordination',
      'commerce/management/functions-of-management/control'
    ],
    summaryIntro: 'The master comprehensive chapter on managerial process: Fayol\'s POCCC, Luther Gulick\'s POSDCORB, and Koontz & O\'Donnell\'s five universal functions of management.',
    points: [
      { bold: 'Planning & Decision Making:', desc: 'Primary function. Setting objectives, forecasting, establishing policies, procedures, rules, budgets, and programs. Management by Objectives (MBO).' },
      { bold: 'Organizing & Organizational Structures:', desc: 'Departmentation, span of control, scalar chain, formal vs informal organization, line and staff, functional, divisional, and project structures.' },
      { bold: 'Staffing & Human Resource Planning:', desc: 'Recruitment, selection, placement, training, performance appraisal, and compensation management.' },
      { bold: 'Directing, Supervision & Coordination:', desc: 'Communication channels, leadership, guidance, and coordination as the "essence of management" binding all functions together.' },
      { bold: 'Controlling Techniques:', desc: 'Establishing standards, measuring actual performance, analyzing variances, taking corrective action. Traditional vs modern control tools (PERT/CPM, budgets).' }
    ]
  },

  // 7. Management Thought: Schools and Theorists (4 -> 1)
  {
    targetDir: 'commerce/management-thought/schools-and-theorists',
    title: 'Evolution of Management Thought: Scientific, Administrative, and Human Relations Schools',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/management-thought/fw-taylor',
      'commerce/management-thought/henry-fayol',
      'commerce/management-thought/elton-mayo',
      'commerce/management-thought/schools-of-management-thought'
    ],
    summaryIntro: 'Historical evolution of managerial science from Classical approaches to Neo-Classical and Modern behavioral and contingency systems.',
    points: [
      { bold: 'F.W. Taylor & Scientific Management:', desc: '"Father of Scientific Management". Time and motion study, fatigue study, standardization of tools, differential piece-rate wage system, functional foremanship, mental revolution.' },
      { bold: 'Henry Fayol & Administrative Management:', desc: '"Father of General / Modern Management". 14 Administrative Principles, six industrial activities, and universal functional categorization (POCCC).' },
      { bold: 'Elton Mayo & Hawthorne Experiments:', desc: '"Father of Human Relations Approach". Illumination experiments, Relay Assembly Test Room, Bank Wiring Observation Room. Social and psychological group dynamics over pure economic incentives.' },
      { bold: 'Modern Management Approaches:', desc: 'Behavioural School (Maslow, McGregor, Herzberg), Systems Approach (input-process-output, open system), and Contingency / Situational Approach.' }
    ]
  },

  // 8. Marketing: Nature and Functions (2 -> 1)
  {
    targetDir: 'commerce/marketing/nature-and-functions',
    title: 'Marketing: Meaning, Nature, Scope, Functions, and Marketing Mix',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Section C',
    oldDirs: [
      'commerce/marketing/meaning-and-nature-of-marketing',
      'commerce/marketing/functions-of-marketing'
    ],
    summaryIntro: 'A foundational study of customer-centric marketing philosophies, societal marketing concepts, marketing vs selling, exchange functions, and the traditional 4Ps of marketing.',
    points: [
      { bold: 'Concept & Philosophy of Marketing:', desc: 'Transition across Production concept, Product concept, Selling concept, Marketing concept, and Societal Marketing concept.' },
      { bold: 'Marketing vs Selling Distinction:', desc: 'Selling focuses on seller\'s needs and converting goods into cash. Marketing focuses on customer needs and creating customer satisfaction.' },
      { bold: 'Functions of Marketing (Clark & Clark):', desc: 'Functions of Exchange (buying, assembling, selling), Physical Distribution (transportation, storage), and Facilitating Functions (financing, risk-bearing, standardization, market information).' },
      { bold: 'The Marketing Mix (4Ps):', desc: 'Product, Price, Place (distribution channels), and Promotion (advertising, personal selling, sales promotion, public relations).' }
    ]
  },

  // 9. Trade: Internal and International Trade (2 -> 1)
  {
    targetDir: 'commerce/trade/internal-and-international-trade',
    title: 'Trade: Internal Trade (Wholesale & Retail) and International / Foreign Trade',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Section C',
    oldDirs: [
      'commerce/trade/domestic-trade',
      'commerce/trade/foreign-trade'
    ],
    summaryIntro: 'Comprehensive guide covering wholesale and retail trade mechanisms, middlemen, super bazaars, department stores, alongside export-import procedures, documentation, and exchange controls.',
    points: [
      { bold: 'Internal / Domestic Trade:', desc: 'Wholesale Trade (bulk purchase, financing manufacturers, credit to retailers) vs Retail Trade (direct contact with consumer, variety of goods).' },
      { bold: 'Modern Retail Formats:', desc: 'Departmental stores, multiple/chain shops, mail order houses, super markets, consumer cooperatives, and vending machines.' },
      { bold: 'International / Foreign Trade Basics:', desc: 'Import, Export, and Entrepot trade. Differences between domestic and foreign trade (currencies, legal systems, tariffs, transport risks).' },
      { bold: 'Export-Import Procedures & Documents:', desc: 'Indents, Letter of Credit (L/C), Bill of Lading, Consular Invoice, Certificate of Origin, Mate\'s Receipt, and Customs clearance.' }
    ]
  },

  // 10. Money & Banking: Theories of Money, Inflation, and Price Indices (4 -> 1)
  {
    targetDir: 'commerce/money-and-banking/theories-of-money-and-inflation',
    title: 'Monetary Economics: Quantity Theory of Money, Gresham\'s Law, Inflation, and Price Indices',
    unitNameTgt: 'Money and Banking',
    unitNamePgt: 'Section B - Money & Banking',
    oldDirs: [
      'commerce/money-and-banking/money/greshams-law',
      'commerce/money-and-banking/money/quantity-theory-of-money',
      'commerce/money-and-banking/money/inflation',
      'commerce/money-and-banking/money/price-indices'
    ],
    summaryIntro: 'Authoritative monetary economics module covering Fisher and Cambridge quantity equations, Gresham\'s Law of bad money, demand-pull and cost-push inflation, and index numbers construction.',
    points: [
      { bold: 'Gresham\'s Law:', desc: '"Bad money drives out good money from circulation when both are legal tender of the same nominal value." Applications under bimetallism and paper currency.' },
      { bold: 'Quantity Theory of Money:', desc: 'Fisher\'s Equation of Exchange: MV + M\'V\' = PT (direct and proportional relation between money supply and price level). Cambridge Cash Balance Approach: M = kPY (Marshall, Pigou, Robertson, Keynes).' },
      { bold: 'Inflation: Causes, Types, and Control:', desc: 'Demand-pull vs Cost-push inflation. Creeping, walking, running, and galloping / hyperinflation. Monetary, fiscal, and administrative remedies. Deflation and stagflation.' },
      { bold: 'Index Numbers & Purchasing Power of Money:', desc: 'Barometer of economic activity. Wholesale Price Index (WPI) and Consumer Price Index (CPI). Laspeyres, Paasche, and Fisher\'s "Ideal" Index formulas.' }
    ]
  },

  // 11. Motivation and Leadership: Principles & Theories (2 -> 1)
  {
    targetDir: 'commerce/motivation-and-leadership/principles-and-theories',
    title: 'Organizational Behavior: Motivation Theories and Leadership Styles',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/motivation-and-leadership/leadership',
      'commerce/motivation-and-leadership/principles-of-motivation'
    ],
    summaryIntro: 'In-depth organizational behavior chapter analyzing Maslow, Herzberg, McGregor, and Ouchi theories alongside autocratic, democratic, and laissez-faire leadership paradigms.',
    points: [
      { bold: 'Motivation Meaning & Process:', desc: 'Inner psychological drive transforming latent energy into goal-directed performance. Financial (salary, bonus) vs non-financial (recognition, status, responsibility) incentives.' },
      { bold: 'Major Theories of Motivation:', desc: 'Maslow\'s Need Hierarchy Theory, Herzberg\'s Two-Factor Theory (Hygiene vs Motivators), McGregor\'s Theory X & Theory Y, and William Ouchi\'s Theory Z.' },
      { bold: 'Leadership: Concept and Approaches:', desc: 'Trait Theory, Behavioral Theory, Situational / Contingency Theory (Fiedler\'s Contingency Model, Hersey-Blanchard Situational Theory).' },
      { bold: 'Leadership Styles & Managerial Grid:', desc: 'Autocratic / Authoritarian, Democratic / Participative, and Laissez-faire / Free-rein styles. Blake & Mouton Managerial Grid (1,1 impoverished to 9,9 team management).' }
    ]
  },

  // 12. Statistics: Dispersion and Skewness (2 -> 1)
  {
    targetDir: 'commerce/statistics/dispersion-and-skewness',
    title: 'Measures of Dispersion and Skewness: Range, Quartile Deviation, Mean Deviation, and Standard Deviation',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/statistics/dispersion/measures-of-dispersion',
      'commerce/statistics/dispersion/skewness'
    ],
    summaryIntro: 'A complete quantitative statistics module on degree of variation around central tendency, absolute vs relative dispersion measures, Karl Pearson and Bowley skewness formulas.',
    points: [
      { bold: 'Concept of Dispersion (Scattering):', desc: 'Measures extent to which individual values deviate from central value. Absolute measures (concrete units) vs Relative measures (coefficients / pure numbers).' },
      { bold: 'Measures of Dispersion:', desc: 'Range, Interquartile Range & Quartile Deviation (Semi-interquartile range), Mean Deviation (minimum when taken around median), and Standard Deviation (Karl Pearson 1893, root-mean-square deviation).' },
      { bold: 'Variance & Coefficient of Variation (CV):', desc: 'Variance = (SD)^2. Coefficient of Variation (CV = (SD / Mean) * 100) as the universal measure for comparing consistency, stability, and uniformity of data series.' },
      { bold: 'Skewness (Asymmetry):', desc: 'Symmetrical distribution (Mean = Median = Mode). Positive skewness (Mean > Median > Mode, right tail) vs Negative skewness (Mode > Median > Mean, left tail). Karl Pearson\'s Sk = (Mean - Mode) / SD and Bowley\'s Quartile Skewness.' }
    ]
  },

  // 13. Statistics: Time Series Analysis (Flatten nesting 1 -> 1)
  {
    targetDir: 'commerce/statistics/time-series-analysis',
    title: 'Time Series Analysis: Components, Moving Averages, and Least Squares Method',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Economics & Statistics',
    oldDirs: [
      'commerce/statistics/time-series/analysis-of-time-series'
    ],
    summaryIntro: 'A comprehensive study of chronological data analysis, decomposition into Secular Trend, Seasonal, Cyclical, and Irregular components, and business forecasting methods.',
    points: [
      { bold: 'Meaning & Importance of Time Series:', desc: 'Chronological sequence of data observations over uniform intervals. Vital for business forecasting, budgeting, evaluating performance, and understanding economic growth.' },
      { bold: 'Four Components of Time Series:', desc: 'Secular Trend (T - long-term direction), Seasonal Variations (S - periodic changes within 1 year), Cyclical Fluctuations (C - business cycle swings), Irregular / Random Movements (I - unpredictable shocks).' },
      { bold: 'Mathematical Models of Time Series:', desc: 'Additive Model (Y = T + S + C + I) and Multiplicative Model (Y = T * S * C * I).' },
      { bold: 'Methods of Measuring Trend:', desc: 'Freehand graphic method, Semi-averages method, Moving averages method (odd and even period moving averages), and Method of Least Squares (fitting straight line Y = a + bX).' }
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

console.log('Commerce round 3 complete sweep consolidation and cleanup complete.');
