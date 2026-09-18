const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// Definition of Commerce Consolidations
// Target paths are clean, flat, search-optimal URLs
const consolidations = [
  // 1. Entrepreneurship (4 -> 1)
  {
    targetDir: 'commerce/entrepreneurship',
    title: 'Entrepreneurship: Meaning, Nature, Scope and Importance',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/entrepreneurship/meaning-of-entrepreneurship',
      'commerce/entrepreneurship/definition-of-entrepreneurship',
      'commerce/entrepreneurship/nature-of-entrepreneurship',
      'commerce/entrepreneurship/importance-of-entrepreneurship'
    ],
    summaryIntro: 'A foundational comprehensive module on entrepreneurship, covering its conceptual meaning, economic significance, qualities of an entrepreneur, risk-bearing theories, and role in economic development.',
    points: [
      { bold: 'Meaning & Evolution:', desc: 'Derived from French "entreprendre" (to undertake); evolution from risk-bearer (Cantillon) to organizer (Say) and innovator (Schumpeter).' },
      { bold: 'Nature & Characteristics:', desc: 'Economic activity, creative innovation, purpose-driven leadership, risk-taking ability, and dynamic resource combination.' },
      { bold: 'Theories of Entrepreneurship:', desc: 'Schumpeter\'s Innovation Theory, McClelland\'s Need for Achievement (N-Ach), Knight\'s Risk and Uncertainty Bearing Theory.' },
      { bold: 'Role in Economic Growth:', desc: 'Capital formation, employment generation, balanced regional development, export promotion, and industrial diversification.' }
    ]
  },

  // 2. Consumer Protection (3 -> 1)
  {
    targetDir: 'commerce/consumer-protection',
    title: 'Consumer Protection and Consumer Protection Act 2019',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/consumer-protection/meaning-of-consumer-protection',
      'commerce/consumer-protection/importance-of-consumer-protection',
      'commerce/consumer-protection/consumer-protection-act-2019'
    ],
    summaryIntro: 'A comprehensive study of consumer rights, redressal mechanisms, importance of consumer awareness, and the key provisions of the Consumer Protection Act, 2019.',
    points: [
      { bold: 'Meaning & Caveat Emptor vs Venditor:', desc: 'Transition from "buyer beware" (Caveat Emptor) to consumer sovereignty and "seller beware" (Caveat Venditor).' },
      { bold: 'Six Consumer Rights:', desc: 'Right to Safety, Information, Choice, Being Heard, Redressal, and Consumer Education under the Consumer Protection Act.' },
      { bold: 'Consumer Protection Act, 2019 Structure:', desc: 'Establishment of Central Consumer Protection Authority (CCPA), inclusion of e-commerce, and product liability rules.' },
      { bold: 'Three-Tier Redressal Machinery:', desc: 'District Commission (up to ₹1 Crore), State Commission (₹1 Cr to ₹10 Cr), and National Commission (above ₹10 Crore) pecuniary jurisdictions.' }
    ]
  },

  // 3. Management Foundations (4 -> 1)
  {
    targetDir: 'commerce/management/principles-and-foundations',
    title: 'Management: Meaning, Nature, Scope and Principles',
    unitNameTgt: 'Business Organization & Management',
    unitNamePgt: 'Business Organization & Management',
    oldDirs: [
      'commerce/management/meaning-and-definition-of-management',
      'commerce/management/nature-of-management',
      'commerce/management/scope-of-management',
      'commerce/management/principles-of-management'
    ],
    summaryIntro: 'A comprehensive foundational chapter on management concepts, examining whether management is an art, science, or profession, its universal scope, and fundamental administrative principles.',
    points: [
      { bold: 'Definitions & Meaning:', desc: 'Definitions by Harold Koontz, George R. Terry, and Mary Parker Follett ("art of getting things done through people").' },
      { bold: 'Nature of Management:', desc: 'Analysis as an art (practical know-how), an inexact social science (systematized knowledge), and an emerging profession.' },
      { bold: 'Universality & Levels:', desc: 'Top, middle, and lower/supervisory management hierarchies with corresponding conceptual, human, and technical skills.' },
      { bold: 'General Principles of Management:', desc: 'Henry Fayol\'s 14 administrative principles (Division of Work, Authority & Responsibility, Unity of Command, Unity of Direction, Esprit de Corps).' }
    ]
  },

  // 4. Management Accounting Foundations (6 -> 1)
  {
    targetDir: 'commerce/management-accounting/nature-and-scope',
    title: 'Management Accounting: Meaning, Objectives, Scope and Functions',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/management-accounting/meaning-of-management-accounting',
      'commerce/management-accounting/objectives-of-management-accounting',
      'commerce/management-accounting/functions-of-management-accounting',
      'commerce/management-accounting/scope-of-management-accounting',
      'commerce/management-accounting/importance-of-management-accounting',
      'commerce/management-accounting/management-accounting-vs-financial-accounting'
    ],
    summaryIntro: 'A complete institutional overview of Management Accounting, contrasting internal decision-support mechanisms against statutory Financial Accounting and Cost Accounting frameworks.',
    points: [
      { bold: 'Definition & Meaning:', desc: 'Accounting for internal managerial planning, decision-making, performance evaluation, and policy formulation.' },
      { bold: 'Key Objectives & Functions:', desc: 'Supplying accounting data, modifying and analyzing data, facilitating control through standard costing and budgetary control.' },
      { bold: 'Comparison with Financial Accounting:', desc: 'Internal vs external reporting, optional vs statutory, futuristic vs historical, subjective vs GAAP-regulated.' },
      { bold: 'Scope & Major Tools:', desc: 'Ratio analysis, fund flow / cash flow, marginal costing, standard costing, and responsibility accounting.' }
    ]
  },

  // 5. Auditing — Vouching (4 -> 1)
  {
    targetDir: 'commerce/auditing/vouching',
    title: 'Vouching: Meaning, Significance, Types and Techniques',
    unitNameTgt: 'Auditing',
    unitNamePgt: 'Section A',
    oldDirs: [
      'commerce/auditing/vouching/meaning-of-vouching',
      'commerce/auditing/vouching/significance-of-vouching',
      'commerce/auditing/vouching/types-of-vouching',
      'commerce/auditing/vouching/vouching-of-initial-books'
    ],
    summaryIntro: 'An in-depth study of vouching as the "backbone of auditing", detailing documentation authentication, cash vs trading transactions, and verification of primary entry books.',
    points: [
      { bold: 'Definition & Core Concept:', desc: 'Vouching as the examination by the auditor of all documentary evidence which supports recorded transactions.' },
      { bold: 'Importance ("Backbone of Auditing"):', desc: 'De Paula and Dicksee dictum; establishing authority, authenticity, accuracy, and proper accounting classification.' },
      { bold: 'Primary vs Collateral Vouchers:', desc: 'Original supporting documents (invoices, receipts, contracts) vs secondary copies and subsidiary records.' },
      { bold: 'Vouching of Books of Original Entry:', desc: 'Vouching Cash Book (receipts, payments, bank reconciliation) and Purchase/Sales Day Books.' }
    ]
  },

  // 6. Auditing — Valuation & Verification (2 -> 1)
  {
    targetDir: 'commerce/auditing/valuation-and-verification',
    title: 'Verification and Valuation of Assets and Liabilities',
    unitNameTgt: 'Auditing',
    unitNamePgt: 'Section A',
    oldDirs: [
      'commerce/auditing/valuation-and-verification/valuation-of-assets',
      'commerce/auditing/valuation-and-verification/verification-of-assets'
    ],
    summaryIntro: 'A unified guide on physical and legal verification versus valuation of balance sheet items, examining auditor duties, case laws (Kingston Cotton Mill), and asset classes.',
    points: [
      { bold: 'Verification vs Valuation:', desc: 'Verification confirms existence, ownership, possession, and freedom from encumbrance; Valuation determines correct financial values.' },
      { bold: 'Auditor’s Legal Duty:', desc: '"An auditor is a watchdog, not a bloodhound" (Kingston Cotton Mill Case 1896); reliance on expert certificates.' },
      { bold: 'Valuation of Fixed Assets:', desc: 'At historical cost less accumulated depreciation; impairment testing principles.' },
      { bold: 'Valuation of Current Assets:', desc: 'Inventories at cost or net realizable value (NRV), whichever is lower (AS-2); valuation of debtors and provision for bad debts.' }
    ]
  },

  // 7. Final Accounts (3 -> 1)
  {
    targetDir: 'commerce/final-accounts',
    title: 'Final Accounts: Preparation, Adjustments and Closing Entries',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/final-accounts/final-accounts',
      'commerce/final-accounts/adjustment-entries',
      'commerce/final-accounts/final-accounts-with-adjustments'
    ],
    summaryIntro: 'A complete instructional guide to the preparation of Trading Account, Profit & Loss Account, and Balance Sheet, including standard yearend adjusting journal entries.',
    points: [
      { bold: 'Trading Account:', desc: 'Determination of Gross Profit / Gross Loss through cost of goods sold (COGS) and direct revenues.' },
      { bold: 'Profit & Loss Account:', desc: 'Calculation of Net Operating & Non-operating Profit/Loss incorporating administrative, selling, and financial overheads.' },
      { bold: 'Standard Adjustments:', desc: 'Closing stock, outstanding expenses, prepaid expenses, accrued income, unearned income, depreciation, and bad debt reserves.' },
      { bold: 'Balance Sheet Marshalling:', desc: 'Arrangement of Assets and Liabilities under Order of Liquidity and Order of Permanence.' }
    ]
  },

  // 8. Company Accounts — Shares (4 -> 1)
  {
    targetDir: 'commerce/company-accounts/shares',
    title: 'Share Capital: Types, Issue, Forfeiture and Reissue of Shares',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/company-accounts/shares/types-of-shares',
      'commerce/company-accounts/shares/issue-of-shares',
      'commerce/company-accounts/shares/forfeiture-of-shares',
      'commerce/company-accounts/shares/reissue-of-forfeited-shares'
    ],
    summaryIntro: 'A comprehensive corporate accounting chapter on share capital structures under Companies Act 2013, covering issue at par/premium/discount, calls in arrears, forfeiture, and reissue.',
    points: [
      { bold: 'Classification of Shares:', desc: 'Equity shares (voting rights, residual claims) vs Preference shares (cumulative, redeemable, participating, convertible).' },
      { bold: 'Issue of Shares:', desc: 'Issue for cash and consideration other than cash; pro-rata allotment in case of over-subscription; Securities Premium Reserve (Sec 52).' },
      { bold: 'Forfeiture of Shares:', desc: 'Cancellation of membership due to non-payment of calls; accounting treatment and credit balance in Forfeited Shares Account.' },
      { bold: 'Reissue & Capital Reserve:', desc: 'Reissue of forfeited shares at par/premium/discount; maximum discount rules and transfer of net profit to Capital Reserve Account.' }
    ]
  },

  // 9. Company Accounts — Debentures (2 -> 1)
  {
    targetDir: 'commerce/company-accounts/debentures',
    title: 'Debentures: Issue, Accounting and Redemption Methods',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/company-accounts/debentures/issue-of-debentures',
      'commerce/company-accounts/debentures/redemption-of-debentures'
    ],
    summaryIntro: 'A complete corporate debt accounting module detailing issuance terms, collateral security, Debenture Redemption Reserve (DRR), and methods of discharging debenture liabilities.',
    points: [
      { bold: 'Meaning & Classification:', desc: 'Secured/unsecured, convertible/non-convertible, redeemable/perpetual debentures; debt vs equity characteristics.' },
      { bold: 'Accounting for Issue:', desc: 'Issue at par, premium, or discount; accounting for issue with conditions of redemption.' },
      { bold: 'Debenture Redemption Reserve (DRR):', desc: 'Statutory requirements under Companies Act 2013 and SEBI guidelines; Debenture Redemption Investment (DRI).' },
      { bold: 'Methods of Redemption:', desc: 'Lump-sum payment, draw of lots, purchase in open market, and conversion into new shares or debentures.' }
    ]
  },

  // 10. Partnership Accounts — Retirement & Death (2 -> 1)
  {
    targetDir: 'commerce/partnership-accounts/retirement-and-death',
    title: 'Partnership Accounts: Retirement and Death of a Partner',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/partnership-accounts/retirement-of-partner',
      'commerce/partnership-accounts/death-of-partner'
    ],
    summaryIntro: 'An integrated study of partnership reconstitution upon a partner’s exit or demise, addressing gaining ratio, asset revaluation, treatment of goodwill, and executor settlements.',
    points: [
      { bold: 'Gaining Ratio Calculation:', desc: 'Determination of new profit-sharing ratio and gaining ratio (New Ratio minus Old Ratio) of continuing partners.' },
      { bold: 'Revaluation & Accumulated Reserves:', desc: 'Revaluation Account profit/loss allocation and distribution of general reserves among all partners in old ratio.' },
      { bold: 'Goodwill & Joint Life Policy:', desc: 'Valuation and compensation of outgoing partner’s goodwill share; accounting for Joint Life Policy (JLP) / individual policies.' },
      { bold: 'Settlement of Retiring Partner / Executor:', desc: 'Payment in lump-sum or transfer to Retiring Partner’s Loan Account / Deceased Partner\'s Executor Account with interest or profit share (Sec 37).' }
    ]
  },

  // 11. Taxation — Basic Concepts & Definitions (5 -> 1)
  {
    targetDir: 'commerce/taxation/basic-concepts',
    title: 'Income Tax: Basic Concepts, Assessee, Assessment Year and Tax Liability',
    unitNameTgt: 'Accounting',
    unitNamePgt: 'Accounts, Cost Accounting, Taxation & Management Accounting',
    oldDirs: [
      'commerce/taxation/assessee',
      'commerce/taxation/assessment-year',
      'commerce/taxation/previous-year',
      'commerce/taxation/important-taxation-definitions',
      'commerce/taxation/tax-liability'
    ],
    summaryIntro: 'A foundational direct taxation module detailing key definitions under Section 2 and 3 of the Income Tax Act 1961, tax rates, surcharge, health & education cess, and computation principles.',
    points: [
      { bold: 'Assessee & Person (Sec 2(7) & 2(31)):', desc: 'Ordinary assessee, deemed assessee, assessee in default; Individual, HUF, Firm, Company, AOP, BOI, Local Authority.' },
      { bold: 'Assessment Year vs Previous Year (Sec 2(9) & 3):', desc: 'Financial year in which income is earned (Previous Year) vs 12-month period beginning April 1 in which income is taxed (Assessment Year).' },
      { bold: 'Total Income & Gross Total Income (GTI):', desc: 'Aggregate of five heads of income less Chapter VI-A deductions (80C to 80U).' },
      { bold: 'Tax Liability & Rebate Sec 87A:', desc: 'Old vs New tax regimes, slab rates, surcharge thresholds, 4% Health & Education Cess, and round-off rules (Sec 288A/B).' }
    ]
  },

  // 12. Business Economics — Utility Analysis (3 -> 1)
  {
    targetDir: 'commerce/business-economics/utility-analysis',
    title: 'Utility Analysis: Total, Marginal and Law of Diminishing Marginal Utility',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Principles of Economics & Statistical Methods',
    oldDirs: [
      'commerce/business-economics/utility/total-utility',
      'commerce/business-economics/utility/marginal-utility',
      'commerce/business-economics/utility/law-of-marginal-utility'
    ],
    summaryIntro: 'A comprehensive microeconomics study of Cardinal Utility theory, interrelationship between Total Utility (TU) and Marginal Utility (MU), and consumer equilibrium conditions.',
    points: [
      { bold: 'Cardinal vs Ordinal Approach:', desc: 'Marshallian cardinal utility measured in "utils" vs Hicksian ordinal indifference curve approach.' },
      { bold: 'Relationship between TU and MU:', desc: 'When MU is positive TU rises; when MU is zero TU is maximum (saturation point); when MU is negative TU declines.' },
      { bold: 'Law of Diminishing Marginal Utility (DMU):', desc: 'Gossen’s First Law; psychological foundation, assumptions (homogeneous units, continuous consumption), and exceptions.' },
      { bold: 'Consumer’s Equilibrium:', desc: 'Single-commodity equilibrium (MUx = Px) and equi-marginal utility in multi-commodity purchases (Gossen\'s Second Law).' }
    ]
  },

  // 13. Business Economics — Cost Concepts (2 -> 1)
  {
    targetDir: 'commerce/business-economics/cost-concepts',
    title: 'Cost Concepts and Cost Curves: Average Cost and Marginal Cost',
    unitNameTgt: 'Business Economics',
    unitNamePgt: 'Principles of Economics & Statistical Methods',
    oldDirs: [
      'commerce/business-economics/cost/average-cost',
      'commerce/business-economics/cost/marginal-cost'
    ],
    summaryIntro: 'A rigorous microeconomic analysis of short-run and long-run cost curves, examining the U-shaped nature of AC/MC and the critical geometric relationship between Average and Marginal Cost.',
    points: [
      { bold: 'Short-Run Cost Structure:', desc: 'Total Fixed Cost (TFC), Total Variable Cost (TVC), Total Cost (TC = TFC + TVC); rectangular hyperbola AFC.' },
      { bold: 'Average Cost (AC) Breakdown:', desc: 'Average Cost equals Average Fixed Cost plus Average Variable Cost (AC = AFC + AVC).' },
      { bold: 'Relationship between AC and MC:', desc: 'When MC < AC, AC falls; when MC = AC, AC is minimum; when MC > AC, AC rises; MC cuts AC at its lowest point.' },
      { bold: 'Long-Run Average Cost (LAC):', desc: '"Envelope curve" or "planning curve"; internal and external economies and diseconomies of scale.' }
    ]
  },

  // 14. Statistics — Measures of Central Tendency (3 -> 1)
  {
    targetDir: 'commerce/statistics/measures-of-central-tendency',
    title: 'Measures of Central Tendency: Mean, Median and Mode',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Principles of Economics & Statistical Methods',
    oldDirs: [
      'commerce/statistics/central-tendency/mean',
      'commerce/statistics/central-tendency/median',
      'commerce/statistics/central-tendency/mode'
    ],
    summaryIntro: 'A foundational statistical methods chapter on statistical averages, calculation formulas across individual/discrete/continuous series, mathematical properties, and empirical relationships.',
    points: [
      { bold: 'Arithmetic Mean (AM):', desc: 'Algebraic balance point; properties: sum of deviations from mean is zero; calculation via direct, short-cut, and step-deviation methods.' },
      { bold: 'Median (Positional Average):', desc: 'Divides distribution into two equal halves; unaffected by extreme values; graphical determination through Ogives.' },
      { bold: 'Mode (Most Frequent Value):', desc: 'Value with highest density; grouping method; graphical determination through Histogram.' },
      { bold: 'Empirical Relationship:', desc: 'In moderately asymmetric distributions: Mode = 3 Median - 2 Mean; geometric mean and harmonic mean overview.' }
    ]
  },

  // 15. Statistics — Correlation & Regression (2 -> 1)
  {
    targetDir: 'commerce/statistics/correlation-and-regression',
    title: 'Correlation and Regression Analysis',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Principles of Economics & Statistical Methods',
    oldDirs: [
      'commerce/statistics/correlation-and-regression/correlation',
      'commerce/statistics/correlation-and-regression/regression'
    ],
    summaryIntro: 'A unified bivariate statistics guide comparing degree of association (Karl Pearson & Spearman) with directional estimation and prediction via linear regression lines.',
    points: [
      { bold: 'Karl Pearson’s Coefficient (r):', desc: 'Covariance method, range [-1 to +1], independent of change of origin and scale.' },
      { bold: 'Spearman’s Rank Correlation (rho):', desc: 'Qualitative data analysis, formula for tied and untied ranks.' },
      { bold: 'Linear Regression Lines:', desc: 'Regression of Y on X (byx) and X on Y (bxy); principle of least squares.' },
      { bold: 'Properties of Regression Coefficients:', desc: 'Geometric mean of byx and bxy equals correlation coefficient r; both coefficients have identical algebraic sign.' }
    ]
  },

  // 16. Statistics — Theoretical Probability Distributions (3 -> 1)
  {
    targetDir: 'commerce/statistics/theoretical-probability-distributions',
    title: 'Theoretical Probability Distributions: Binomial, Poisson and Normal',
    unitNameTgt: 'Statistics',
    unitNamePgt: 'Principles of Economics & Statistical Methods',
    oldDirs: [
      'commerce/statistics/frequency-distributions/binomial-distribution',
      'commerce/statistics/frequency-distributions/poisson-distribution',
      'commerce/statistics/frequency-distributions/normal-distribution'
    ],
    summaryIntro: 'A comprehensive study of discrete and continuous probability distributions, examining parameters, mean, variance, skewness, and practical exam applications.',
    points: [
      { bold: 'Binomial Distribution (Bernoulli):', desc: 'Discrete distribution with parameters n and p; Mean = np, Variance = npq; Mean is always greater than Variance.' },
      { bold: 'Poisson Distribution:', desc: 'Discrete distribution for rare events (n -> inf, p -> 0); parameter lambda; unique property: Mean = Variance = lambda.' },
      { bold: 'Normal Distribution (Gaussian):', desc: 'Continuous bell-shaped symmetric distribution; Mean = Median = Mode; total area under curve is 1.' },
      { bold: 'Area Properties of Normal Curve:', desc: 'Mean ± 1 sigma = 68.27%, Mean ± 2 sigma = 95.45%, Mean ± 3 sigma = 99.73% of total observations.' }
    ]
  },

  // 17. Money & Banking — Money Foundations (4 -> 1)
  {
    targetDir: 'commerce/money-and-banking/money-concepts',
    title: 'Money: Meaning, Functions, Types and Importance',
    unitNameTgt: 'Money & Banking',
    unitNamePgt: 'Section B / C',
    oldDirs: [
      'commerce/money-and-banking/money/definition-and-scope-of-money',
      'commerce/money-and-banking/money/functions-of-money',
      'commerce/money-and-banking/money/importance-of-money',
      'commerce/money-and-banking/money/types-of-money'
    ],
    summaryIntro: 'A comprehensive monetary economics module detailing barter drawbacks, primary, secondary, and contingent functions of money, legal tender classifications, and liquidity measures.',
    points: [
      { bold: 'Definition & Core Nature:', desc: '"Money is what money does" (Walker); generally accepted medium of exchange and standard unit of value.' },
      { bold: 'Fourfold Functional Classification:', desc: 'Primary (Medium of exchange, Measure of value); Secondary (Standard of deferred payments, Store of value); Contingent (Basis of credit, distribution of national income).' },
      { bold: 'Classification of Money:', desc: 'Commodity money, Metallic money, Paper currency, Credit money, Flat money, Legal tender (limited vs unlimited).' },
      { bold: 'RBI Monetary Aggregates:', desc: 'M1 (narrow money = currency + demand deposits + other deposits), M2, M3 (broad money), and M4.' }
    ]
  },

  // 18. Money & Banking — Digital Banking (2 -> 1)
  {
    targetDir: 'commerce/money-and-banking/digital-banking',
    title: 'Digital Banking and E-Banking: Systems, Services and Security',
    unitNameTgt: 'Money & Banking',
    unitNamePgt: 'Section B / C',
    oldDirs: [
      'commerce/money-and-banking/banking/e-banking',
      'commerce/money-and-banking/banking/digital-banking'
    ],
    summaryIntro: 'A modern digital financial systems chapter covering RTGS, NEFT, IMPS, UPI, core banking solutions, mobile wallets, and cybersecurity in financial transactions.',
    points: [
      { bold: 'E-Banking Evolution:', desc: 'Traditional brick-and-mortar banking to anytime-anywhere internet banking and Core Banking Solutions (CBS).' },
      { bold: 'Inter-Bank Settlement Mechanisms:', desc: 'NEFT (hourly batches), RTGS (real-time gross settlement for high values >= ₹2 Lakh), IMPS (immediate 24/7 payment service).' },
      { bold: 'Unified Payments Interface (UPI):', desc: 'NPCI framework, Virtual Payment Address (VPA), real-time peer-to-peer and peer-to-merchant interoperability.' },
      { bold: 'Security & Regulatory Measures:', desc: 'Two-factor authentication (2FA), encryption standards, RBI ombudsman scheme for digital transactions.' }
    ]
  },

  // 19. Money & Banking — Reserve Bank of India (2 -> 1)
  {
    targetDir: 'commerce/money-and-banking/reserve-bank-of-india',
    title: 'Reserve Bank of India: Organization, Monetary Policy and Functions',
    unitNameTgt: 'Money & Banking',
    unitNamePgt: 'Section B / C',
    oldDirs: [
      'commerce/money-and-banking/banking/reserve-bank-of-india',
      'commerce/money-and-banking/banking/functions-of-rbi'
    ],
    summaryIntro: 'An authoritative study of India’s central bank, established under RBI Act 1934 (Hilton Young Commission), examining currency monopoly, lender of last resort, and quantitative/qualitative credit control.',
    points: [
      { bold: 'Establishment & Nationalization:', desc: 'Formed on April 1, 1935 following Hilton Young Commission recommendations; nationalized on January 1, 1949.' },
      { bold: 'Core Central Banking Functions:', desc: 'Sole currency issuing authority (Minimum Reserve System), Banker to the Government, Banker’s Bank, and custodian of foreign exchange.' },
      { bold: 'Quantitative Credit Control:', desc: 'Repo Rate, Reverse Repo Rate, Marginal Standing Facility (MSF), Bank Rate, Cash Reserve Ratio (CRR), and Statutory Liquidity Ratio (SLR).' },
      { bold: 'Qualitative (Selective) Controls:', desc: 'Margin requirements, moral suasion, selective credit directives, and rationing of credit.' }
    ]
  }
];

function generateCommerceHtml(item) {
  const relPath = item.targetDir.replace(/\\/g, '/');
  const canonicalUrl = `https://sjmaths.com/${relPath}/`;

  const checklistItems = item.points.map(p => `
          <label class="check-item"><input type="checkbox"> <span><strong>${p.bold}</strong> ${p.desc}</span></label>`).join('');

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${item.title} — Commerce Study Guide | SJ Maths</title>
<meta name="description" content="Comprehensive study guide, key concepts, and exam revision notes for ${item.title}. Preparation notes for UP TGT & PGT Commerce.">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#0f766e">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="/favicon.png">

<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${item.title} — Commerce Study Guide">
<meta property="og:description" content="Study notes and revision checklist for ${item.title}.">
<meta property="og:url" content="${canonicalUrl}">
<meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${item.title} — Commerce Study Guide">
<meta name="twitter:description" content="Study notes and revision checklist for ${item.title}.">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "${item.title}",
  "headline": "${item.title} — Commerce Study Guide",
  "description": "Study notes, syllabus alignment, and key concepts for ${item.title}.",
  "url": "${canonicalUrl}",
  "isPartOf": {
    "@type": "WebSite",
    "name": "SJ Maths",
    "url": "https://sjmaths.com/"
  },
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://sjmaths.com/"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Commerce",
        "item": "https://sjmaths.com/up-tgt-commerce/"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "${item.unitNameTgt}",
        "item": "${canonicalUrl}"
      },
      {
        "@type": "ListItem",
        "position": 4,
        "name": "${item.title}",
        "item": "${canonicalUrl}"
      }
    ]
  }
}
</script>

<style>
:root{--bg:#f6f8fb;--paper:#fff;--ink:#182238;--ink2:#4c576b;--muted:#7b8698;--line:#e1e7ef;--softline:#edf1f5;--brand:#0f766e;--accent:#0d9488;--accent-soft:#0f766e12;--accent-border:#0f766e33;--shadow:0 16px 38px rgba(15,118,110,.07)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:radial-gradient(circle at 100% 0,rgba(15,118,110,.06),transparent 28rem),radial-gradient(circle at 0 31rem,rgba(13,148,136,.045),transparent 26rem),var(--bg);color:var(--ink);font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
.wrap{width:min(1180px,calc(100% - 32px));margin:auto}
.site-header{height:66px;position:sticky;top:0;z-index:90;background:rgba(255,255,255,.96);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.header-inner{height:100%;display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:flex;gap:11px;align-items:center}
.brand-mark{width:39px;height:39px;border-radius:11px;background:linear-gradient(145deg,#0f766e,#14b8a6);display:grid;place-items:center;color:#fff;font-weight:900}
.brand-name{display:block;font-weight:850}
.brand-sub{display:block;color:var(--muted);font-size:.68rem}
.back-btn{display:inline-flex;align-items:center;gap:6px;font-size:.84rem;font-weight:700;color:var(--brand);padding:8px 14px;border-radius:10px;background:var(--accent-soft);border:1px solid var(--accent-border);transition:all .15s}
.back-btn:hover{background:var(--brand);color:#fff}

.hero{padding:32px 0 24px}
.breadcrumb{display:flex;gap:6px;align-items:center;flex-wrap:wrap;color:var(--muted);font-size:.78rem;margin-bottom:12px}
.breadcrumb a:hover{color:var(--brand)}
.kicker{display:inline-flex;gap:7px;align-items:center;color:var(--brand);font-size:.72rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}
.kicker:before{content:"";width:18px;height:2px;background:var(--brand);border-radius:99px}
h1{margin:0 0 10px;font-size:clamp(1.6rem,3.2vw,2.4rem);font-weight:900;letter-spacing:-.03em;color:#0e1726;line-height:1.15}
.lead{margin:0 0 16px;color:var(--ink2);font-size:.96rem;max-width:820px;line-height:1.6}
.exam-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.exam-chip{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:999px;background:#eaf8f5;border:1px solid #cce9e4;color:#0f766e;font-size:.76rem;font-weight:700}

.main-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:24px;padding-bottom:64px}
.card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;margin-bottom:18px;box-shadow:0 2px 10px rgba(15,118,110,.03)}
.card h2{margin:0 0 12px;font-size:1.25rem;letter-spacing:-.02em;color:#111c2e}
.card p{margin:0 0 14px;color:var(--ink2);line-height:1.65;font-size:.92rem}
.checklist{display:grid;gap:8px;margin-top:14px}
.check-item{display:flex;align-items:flex-start;gap:10px;padding:10px 12px;border:1px solid var(--softline);border-radius:10px;background:#fbfcfe;font-size:.85rem;color:var(--ink);cursor:pointer}
.check-item input{margin-top:3px;accent-color:var(--brand);cursor:pointer}

.sidebar-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:20px;position:sticky;top:86px}
.sidebar-card h3{margin:0 0 10px;font-size:.95rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.action-box{background:var(--accent-soft);border:1px solid var(--accent-border);border-radius:14px;padding:16px;margin-top:14px;text-align:center}
.action-box strong{display:block;font-size:.92rem;color:var(--brand)}
.action-box p{margin:6px 0 12px;font-size:.78rem;color:var(--ink2)}
.action-btn{display:inline-block;padding:9px 16px;background:var(--brand);color:#fff;font-size:.78rem;font-weight:800;border-radius:9px}

.footer{padding:30px 0;background:#fff;border-top:1px solid var(--line);color:var(--muted);font-size:.78rem;margin-top:40px}
.footer-inner{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.footer a{color:var(--brand);font-weight:700}
@media(max-width:860px){.main-grid{grid-template-columns:1fr}.sidebar-card{position:static}}
</style>
</head>
<body>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="https://sjmaths.com/">
      <span class="brand-mark">SJ</span>
      <span>
        <span class="brand-name">SJ Maths</span>
        <span class="brand-sub">Master Subject Library</span>
      </span>
    </a>
    <a class="back-btn" href="/up-tgt-commerce/">← Back to UP TGT Commerce</a>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span>›</span>
      <a href="/up-tgt-commerce/">Commerce</a>
      <span>›</span>
      <span>${item.unitNameTgt}</span>
      <span>›</span>
      <span>${item.title}</span>
    </nav>
    <div class="kicker">${item.unitNameTgt}</div>
    <h1>${item.title}</h1>
    <p class="lead">${item.summaryIntro}</p>

    <div class="exam-badges">
      <span style="font-size:.74rem;color:var(--muted);align-self:center">Appears in:</span>
      <a class="exam-chip" href="/up-tgt-commerce/">UP TGT Commerce Tracker →</a>
      <a class="exam-chip" href="/up-pgt-commerce/">UP PGT Commerce Tracker →</a>
    </div>
  </section>

  <div class="main-grid">
    <div class="content-col">
      <article class="card">
        <h2>1. Syllabus Overview & Exam Focus</h2>
        <p>In the official teacher recruitment and competitive syllabus, <strong>${item.title}</strong> is a core examination unit of <em>${item.unitNameTgt}</em>. Questions test definitions, accounting/management principles, legal provisions, formulas, and real-world commercial applications.</p>
        <p>Study this consolidated module systematically to master both theoretical fundamentals and examination numerical patterns.</p>
      </article>

      <article class="card">
        <h2>2. Key Concepts & Essential Principles</h2>
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
        <p style="font-size:.84rem;color:var(--ink2);margin:0 0 12px">Track this topic alongside the complete syllabus on your exam progress tracker.</p>
        <div class="action-box">
          <strong>UP TGT Commerce</strong>
          <p>Interactive progress tracking, instant search &amp; filter</p>
          <a class="action-btn" href="/up-tgt-commerce/">Open Tracker →</a>
        </div>
      </div>
    </aside>
  </div>
</main>

<footer class="footer">
  <div class="wrap footer-inner">
    <span>SJ Maths • Master Subject Library • ${item.title}</span>
    <div>
      <a href="https://sjmaths.com/">Home</a> &nbsp;•&nbsp;
      <a href="/up-tgt-commerce/">UP TGT Commerce</a> &nbsp;•&nbsp;
      <a href="/up-pgt-commerce/">UP PGT Commerce</a>
    </div>
  </div>
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
    if (oldDirAbs === targetDirAbs) continue; // Don't delete self
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

console.log('Commerce consolidation and cleanup complete.');
