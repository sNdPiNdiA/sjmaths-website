const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const consolidations = [
  // 1. Economic Systems
  {
    targetDir: 'economics/economic-systems',
    title: 'Economic Systems: Capitalism, Socialism, and Mixed Economy',
    kicker: 'Economic Systems',
    oldDirs: [
      'economics/economic-systems/capitalism',
      'economics/economic-systems/socialism',
      'economics/economic-systems/mixed-economy'
    ],
    summaryIntro: 'A comprehensive comparative analysis of global economic systems: capitalist market economy, socialist planned economy, and mixed economic frameworks.',
    points: [
      { bold: 'Capitalism (Market Economy):', desc: 'Private ownership of means of production, profit motive, consumer sovereignty, price mechanism (invisible hand), and minimal state intervention.' },
      { bold: 'Socialism (Command Economy):', desc: 'Social / state ownership of production factors, central economic planning, social welfare orientation, absence of competition, and government price fixing.' },
      { bold: 'Mixed Economy Framework:', desc: 'Coexistence of public and private sectors, indicative planning, state regulation of basic/strategic industries, and social security provisions (Indian model).' },
      { bold: 'Comparative Evaluation:', desc: 'Merits and limitations regarding resource allocation efficiency, income inequality, economic freedom, and crisis resilience.' }
    ]
  },

  // 2. Economic Theory: Foundations & Analysis
  {
    targetDir: 'economics/economic-theory/foundations-and-analysis',
    title: 'Economic Theory: Definition, Nature, Micro vs Macro, Static vs Dynamic Analysis',
    kicker: 'Economic Theory',
    oldDirs: [
      'economics/economic-theory/foundations/definition',
      'economics/economic-theory/foundations/nature',
      'economics/economic-theory/analysis/micro-analysis',
      'economics/economic-theory/analysis/macro-analysis',
      'economics/economic-theory/analysis/static-analysis',
      'economics/economic-theory/analysis/dynamic-analysis'
    ],
    summaryIntro: 'An authoritative study of foundational methodology in economics, contrasting classical vs modern definitions, micro vs macro perspectives, and static vs dynamic equilibrium models.',
    points: [
      { bold: 'Definitions of Economics:', desc: 'Wealth definition (Adam Smith), Welfare definition (Alfred Marshall), Scarcity definition (Lionel Robbins), and Growth-oriented definition (Paul Samuelson).' },
      { bold: 'Nature of Economic Science:', desc: 'Positive science (what is) vs Normative science (what ought to be); deductive vs inductive reasoning methodologies.' },
      { bold: 'Microeconomics vs Macroeconomics:', desc: 'Ragnar Frisch dichotomy (1933): Individual consumer and firm optimization (Micro) vs aggregate output, employment, and general price level (Macro).' },
      { bold: 'Static vs Dynamic Economic Analysis:', desc: 'Static analysis (timeless equilibrium), Comparative statics (comparing two equilibrium states), and Dynamic analysis (time-lagged path of adjustment).' }
    ]
  },

  // 3. Elementary Statistics: Central Tendency
  {
    targetDir: 'economics/elementary-statistics/central-tendency',
    title: 'Measures of Central Tendency: Mean, Median, and Mode',
    kicker: 'Elementary Statistics',
    oldDirs: [
      'economics/elementary-statistics/central-tendency/mean',
      'economics/elementary-statistics/central-tendency/median',
      'economics/elementary-statistics/central-tendency/mode'
    ],
    summaryIntro: 'A foundational quantitative statistics chapter on statistical averages, algebraic and positional properties, calculation across individual, discrete, and continuous series.',
    points: [
      { bold: 'Arithmetic Mean:', desc: 'Sum of observations divided by total count. Properties: algebraic sum of deviations from mean is zero; sum of squared deviations is minimum. Weighted arithmetic mean.' },
      { bold: 'Median (Positional Average):', desc: 'Middle value dividing ordered data into two equal halves. Partition values: Quartiles (Q1, Q3), Deciles, and Percentiles. Less affected by extreme outliers.' },
      { bold: 'Mode (Most Frequent Value):', desc: 'Value occurring with highest frequency. Determination through inspection, grouping method, and empirical relation: Mode = 3 Median - 2 Mean.' },
      { bold: 'Geometric & Harmonic Mean:', desc: 'GM for ratios, percentages, and index numbers; HM for rates and speed. Mathematical relationship: AM >= GM >= HM.' }
    ]
  },

  // 4. Growth and Development: Theories of Growth
  {
    targetDir: 'economics/growth-and-development/theories-of-growth',
    title: 'Theories of Economic Growth: Harrod-Domar, Arthur Lewis, and Rostow Stages',
    kicker: 'Growth & Development',
    oldDirs: [
      'economics/growth-and-development/theories/harrod-domar',
      'economics/growth-and-development/theories/lewis',
      'economics/growth-and-development/theories/rostow'
    ],
    summaryIntro: 'In-depth analysis of classical, dual-sector, and post-Keynesian growth models explaining long-term capital accumulation and structural transition.',
    points: [
      { bold: 'Harrod-Domar Growth Model:', desc: 'Dual role of investment (generating income and expanding capacity). Actual growth rate (g), Warranted rate (gw), and Natural rate (gn). Razor-edge equilibrium instability.' },
      { bold: 'Arthur Lewis Dual-Sector Model:', desc: 'Economic development with unlimited supplies of labour from traditional subsistence sector to capitalist modern sector; reinvestment of capitalist surplus.' },
      { bold: 'Rostow\'s Stages of Economic Growth:', desc: 'Historical modernization stages: Traditional Society, Pre-conditions for Take-off, The Take-off, Drive to Maturity, and Age of High Mass-Consumption.' },
      { bold: 'Schumpeter\'s Innovation Theory:', desc: 'Role of entrepreneurial innovation, cyclical growth waves, and creative destruction in capitalistic progress.' }
    ]
  },

  // 5. Growth and Development: Concepts and Obstacles
  {
    targetDir: 'economics/growth-and-development/concepts-and-obstacles',
    title: 'Economic Development: Concepts, Measures, Obstacles, and Vicious Circle of Poverty',
    kicker: 'Growth & Development',
    oldDirs: [
      'economics/growth-and-development/economic-development',
      'economics/growth-and-development/economic-progress',
      'economics/growth-and-development/measures-of-development',
      'economics/growth-and-development/problems-of-economic-development',
      'economics/growth-and-development/reasons-of-low-economic-development',
      'economics/growth-and-development/vicious-circle-of-poverty'
    ],
    summaryIntro: 'A foundational developmental economics text covering qualitative transformations, measurement indices (PQLI, HDI), structural bottlenecks, and Ragnar Nurkse\'s vicious circle of poverty.',
    points: [
      { bold: 'Growth vs Development Distinction:', desc: 'Economic growth (quantitative increase in real GDP) vs Economic development (growth accompanied by structural, institutional, and distributional change).' },
      { bold: 'Measures of Economic Development:', desc: 'Per Capita Income, Physical Quality of Life Index (PQLI - Morris D. Morris), Human Development Index (HDI - Mahbub ul Haq and Amartya Sen).' },
      { bold: 'Vicious Circle of Poverty (Ragnar Nurkse):', desc: 'Supply side: Low income -> Low savings -> Low investment -> Capital deficiency -> Low productivity -> Low income. Demand side: Low income -> Low buying power -> Low inducement to invest.' },
      { bold: 'Obstacles to Economic Development:', desc: 'Capital deficiency, market imperfections, rapid population pressure, technological backwardness, and socio-cultural constraints.' }
    ]
  },

  // 6. Indian Economy: Agriculture - Structure & Farmers
  {
    targetDir: 'economics/indian-economy/agriculture-sector/farmers-and-problems',
    title: 'Indian Agriculture: Problems, Marginal and Small Farmers, and Solutions',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/agriculture-sector/problems',
      'economics/indian-economy/agriculture-sector/problems/solutions',
      'economics/indian-economy/agriculture-sector/farmers/small-farmers',
      'economics/indian-economy/agriculture-sector/farmers/marginal-farmers'
    ],
    summaryIntro: 'Detailed analytical study of Indian agrarian structure, landholding fragmentation, small and marginal farmer distress, and policy solutions.',
    points: [
      { bold: 'Agrarian Structure & Farm Categories:', desc: 'Marginal farmers (below 1 hectare), Small farmers (1 to 2 hectares), Semi-medium (2 to 4 ha), Medium (4 to 10 ha), and Large farmers (above 10 ha).' },
      { bold: 'Major Structural Problems of Agriculture:', desc: 'Low productivity, monsoon dependency, sub-division and fragmentation of landholdings, disguised unemployment, and inadequate institutional credit.' },
      { bold: 'Agrarian Reforms & Institutional Solutions:', desc: 'Abolition of intermediaries (zamindari), tenancy reforms, land ceiling acts, consolidation of holdings (Chakbandi), and cooperative farming.' },
      { bold: 'Technological & Financial Interventions:', desc: 'Kisan Credit Card (KCC), PM-KISAN income support, micro-irrigation, crop insurance (PMFBY), and promotion of Farmer Producer Organisations (FPOs).' }
    ]
  },

  // 7. Indian Economy: Agriculture - Marketing & Food Security
  {
    targetDir: 'economics/indian-economy/agriculture-sector/marketing-and-food-security',
    title: 'Agricultural Marketing, Price Policy, Public Distribution System, and Food Security',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/agriculture-sector/agricultural-marketing',
      'economics/indian-economy/agriculture-sector/agricultural-price-policy',
      'economics/indian-economy/agriculture-sector/food-security',
      'economics/indian-economy/agriculture-sector/public-distribution-system'
    ],
    summaryIntro: 'A comprehensive study of India\'s agricultural supply chain, APMC mandis, Minimum Support Price (MSP), buffer stocks, and Targeted Public Distribution System (TPDS).',
    points: [
      { bold: 'Agricultural Marketing Defects & Reforms:', desc: 'Malpractices of middlemen, distress sale, lack of grading and cold storage. Regulated markets (APMCs), electronic National Agriculture Market (e-NAM).' },
      { bold: 'Agricultural Price Policy & MSP:', desc: 'Minimum Support Price recommended by Commission for Agricultural Costs and Prices (CACP) covering A2+FL and C2 costs; procurement prices.' },
      { bold: 'Buffer Stocks & Food Corporation of India (FCI):', desc: 'Procurement, storage, and strategic buffer stocking of foodgrains to stabilize market prices during production shocks.' },
      { bold: 'Food Security & Targeted PDS (TPDS):', desc: 'National Food Security Act (NFSA) 2013, Antyodaya Anna Yojana (AAY), priority households, digital ration card portability (One Nation One Ration Card).' }
    ]
  },

  // 8. Indian Economy: Unemployment
  {
    targetDir: 'economics/indian-economy/employment/unemployment-in-india',
    title: 'Unemployment in India: Types, Causes, and Remedial Measures',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/employment/visible-unemployment',
      'economics/indian-economy/employment/invisible-unemployment',
      'economics/indian-economy/employment/under-employment',
      'economics/indian-economy/employment/unemployment/causes',
      'economics/indian-economy/employment/unemployment/remedies'
    ],
    summaryIntro: 'An authoritative overview of employment dynamics in India, measurement metrics by NSO/NSSO, structural causes of joblessness, and government employment schemes.',
    points: [
      { bold: 'Types of Unemployment:', desc: 'Disguised unemployment (marginal productivity is zero), Seasonal, Structural, Frictional, Cyclical, Open / Visible unemployment, and Under-employment.' },
      { bold: 'Measurement Criteria (NSSO / NSO):', desc: 'Usual Principal and Subsidiary Status (UPSS), Current Weekly Status (CWS), and Current Daily Status (CDS).' },
      { bold: 'Structural Causes of Unemployment in India:', desc: 'Rapid population growth, jobless growth in services/manufacturing, slow agricultural transformation, outdated education/skill mismatch.' },
      { bold: 'Government Schemes & Interventions:', desc: 'MGNREGA (100 days statutory wage employment guarantee), Deendayal Antyodaya Yojana-NRLM/NULM, Skill India, and PM Mudra Yojana.' }
    ]
  },

  // 9. Indian Economy: Foreign Trade
  {
    targetDir: 'economics/indian-economy/foreign-trade',
    title: 'Foreign Trade of India: Structure, Recent Trends, and Import Substitution',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/foreign-trade/structure',
      'economics/indian-economy/foreign-trade/recent-trends',
      'economics/indian-economy/foreign-trade/import-substitution'
    ],
    summaryIntro: 'In-depth study of India\'s merchandise and services trade, directional shift from West to East, export promotion vs import substitution strategies.',
    points: [
      { bold: 'Composition of Foreign Trade:', desc: 'Shift from primary agricultural goods to manufactured engineering items, petroleum products, chemicals, pharmaceuticals, and software services.' },
      { bold: 'Direction of Foreign Trade:', desc: 'Diversification of trade partners: USA, China, UAE, EU, ASEAN, and African nations.' },
      { bold: 'Import Substitution vs Export Promotion:', desc: 'Pre-1991 inward-looking industrialization (import substitution through tariffs and quotas) vs Post-1991 export orientation and free trade agreements.' },
      { bold: 'Trade Balance & Current Account Deficit (CAD):', desc: 'Persistent merchandise trade deficit offset by robust software services surplus and private inward remittances.' }
    ]
  },

  // 10. Indian Economy: Industrial Sector & MSME
  {
    targetDir: 'economics/indian-economy/industrial-sector/policy-and-msme',
    title: 'Industrial Development in India: Industrial Policies, Problems, and MSME Sector',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/industrial-sector/industrial-policy',
      'economics/indian-economy/industrial-sector/new-industrial-policy',
      'economics/indian-economy/industrial-sector/problems-of-industrialisation',
      'economics/indian-economy/industrial-sector/msme-sector/micro-enterprises',
      'economics/indian-economy/industrial-sector/msme-sector/small-enterprises',
      'economics/indian-economy/industrial-sector/msme-sector/medium-enterprises'
    ],
    summaryIntro: 'Comprehensive review of industrial planning in India, Industrial Policy Resolutions (1948, 1956, 1991), and revised composite criteria for MSMEs.',
    points: [
      { bold: 'Industrial Policy Resolutions (1948 & 1956):', desc: 'IPR 1956 as the "Economic Constitution of India", establishing state-led commanding heights, Schedule A/B/C classification, and industrial licensing.' },
      { bold: 'New Industrial Policy (NIP 1991):', desc: 'Abolition of industrial licensing (except strategic goods), contraction of public sector reservation, deregulation of MRTP, and liberal foreign direct investment (FDI).' },
      { bold: 'MSME Sector Composite Criteria (2020):', desc: 'Micro (Investment <= 1 Cr, Turnover <= 5 Cr), Small (Investment <= 10 Cr, Turnover <= 50 Cr), Medium (Investment <= 50 Cr, Turnover <= 250 Cr).' },
      { bold: 'Role and Challenges of MSMEs:', desc: 'Employment generation, decentralised growth, export contribution (40%+). Challenges: Delayed payments, lack of working capital, outdated technology.' }
    ]
  },

  // 11. Indian Economy: National Income
  {
    targetDir: 'economics/indian-economy/national-income-structure',
    title: 'National Income in India: Sectoral Structure, Growth Trends, and Inequalities',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/national-income/structure',
      'economics/indian-economy/national-income/distribution'
    ],
    summaryIntro: 'An analytical review of structural transformation in Indian GDP, sectoral contributions (Primary, Secondary, Tertiary), and economic regional disparities.',
    points: [
      { bold: 'Sectoral Composition of GDP:', desc: 'Structural shift from Primary sector dominance at Independence to Services sector (>54%) dominance, with agriculture remaining the largest employer (>45%).' },
      { bold: 'Growth Trends in National Income:', desc: 'Pre-1980 "Hindu rate of growth" (~3.5%), post-reform acceleration to 7-8% GDP growth trajectory, and base year revisions by NSO.' },
      { bold: 'Income Inequality & Wealth Distribution:', desc: 'Measurement via Gini Coefficient and Lorenz Curve; urban-rural divide and regional disparities between forward and lagging states.' },
      { bold: 'Policy Recommendations:', desc: 'Progressive taxation, inclusive financial deepening, targeted social safety nets, and labour-intensive industrialization.' }
    ]
  },

  // 12. Indian Economy: Industrial Relations
  {
    targetDir: 'economics/indian-economy/industrial-relations',
    title: 'Industrial Relations in India: Industrial Disputes and Role of Trade Unions',
    kicker: 'Indian Economy',
    oldDirs: [
      'economics/indian-economy/industrial-relations/industrial-disputes',
      'economics/indian-economy/industrial-relations/trade-unions/role'
    ],
    summaryIntro: 'A complete overview of industrial relations in India, forms and settlement of industrial disputes (Industrial Disputes Act 1947), and trade unionism.',
    points: [
      { bold: 'Industrial Disputes: Causes and Forms:', desc: 'Strikes, lockouts, gherao, lay-off, retrenchment. Underlying causes: wage demands, bonus disputes, working conditions, and recognition issues.' },
      { bold: 'Settlement Machinery (Industrial Disputes Act 1947):', desc: 'Works Committees, Conciliation Officers, Boards of Conciliation, Courts of Inquiry, Labour Courts, Industrial Tribunals, and National Tribunals.' },
      { bold: 'Trade Union Movement in India:', desc: 'Trade Unions Act 1926. Historical evolution (AITUC, INTUC, BMS, CITU), functions of trade unions, collective bargaining, and multi-unionism problems.' },
      { bold: 'Recent Labour Reforms:', desc: 'Consolidation of 29 central labour laws into 4 Labour Codes (Wages, Industrial Relations, Social Security, Occupational Safety).' }
    ]
  },

  // 13. International Trade: Theories
  {
    targetDir: 'economics/international-trade/theories-of-trade',
    title: 'Theories of International Trade: Comparative Cost, Heckscher-Ohlin, and Opportunity Cost',
    kicker: 'International Trade',
    oldDirs: [
      'economics/international-trade/trade-theories/comparative-cost-theory',
      'economics/international-trade/trade-theories/reciprocal-demand-theory',
      'economics/international-trade/trade-theories/opportunity-cost-theory',
      'economics/international-trade/trade-theories/heckscher-ohlin-theory',
      'economics/international-trade/trade-theories/leontief-paradox'
    ],
    summaryIntro: 'The master comprehensive module on classical and modern theories of international trade: comparative advantage, reciprocal demand, and factor endowments.',
    points: [
      { bold: 'Absolute & Comparative Cost Advantage:', desc: 'Adam Smith\'s Absolute Advantage (1776) vs David Ricardo\'s Comparative Cost Advantage (1817) based on labour cost differentials.' },
      { bold: 'J.S. Mill\'s Theory of Reciprocal Demand:', desc: 'Determination of terms of trade and distribution of gains from trade based on relative strength and elasticity of each nation\'s demand.' },
      { bold: 'Haberler\'s Opportunity Cost Theory:', desc: 'Restating comparative advantage using Production Possibility Curves (PPC) under constant, increasing, and decreasing opportunity costs.' },
      { bold: 'Heckscher-Ohlin Factor Endowment Theory & Leontief Paradox:', desc: '2x2x2 model: Capital-abundant nations export capital-intensive goods; labour-abundant nations export labour-intensive goods. Leontief Paradox empirical contradiction (US exports were labour-intensive).' }
    ]
  },

  // 14. International Trade: BoP & Exchange Rate
  {
    targetDir: 'economics/international-trade/balance-of-payments-and-exchange-rate',
    title: 'Balance of Payments, Foreign Exchange Determination, and Trade Policy',
    kicker: 'International Trade',
    oldDirs: [
      'economics/international-trade/balance-of-payments/causes-of-imbalance',
      'economics/international-trade/balance-of-payments/remedies',
      'economics/international-trade/foreign-exchange-rate-determination/purchasing-power-parity',
      'economics/international-trade/foreign-exchange-rate-determination/balance-of-payments-theory',
      'economics/international-trade/trade-policy/free-trade',
      'economics/international-trade/trade-policy/protection'
    ],
    summaryIntro: 'A foundational macroeconomic and international finance chapter covering Current and Capital account components, disequilibrium correction, PPP exchange determination, and tariff protection.',
    points: [
      { bold: 'Balance of Trade vs Balance of Payments:', desc: 'BoT (visible merchandise imports/exports only) vs BoP (complete systematic accounting of all economic transactions between residents and rest of world).' },
      { bold: 'BoP Disequilibrium & Correction Measures:', desc: 'Causes: developmental spending, cyclical swings, structural changes. Remedies: Devaluation, depreciation, export subsidies, import quotas, exchange controls.' },
      { bold: 'Foreign Exchange Rate Determination:', desc: 'Purchasing Power Parity (PPP) Theory (Gustav Cassel - Absolute and Relative) vs Modern Balance of Payments / Demand-Supply Theory of foreign exchange.' },
      { bold: 'Free Trade vs Protectionism:', desc: 'Arguments for free trade (optimal specialization) vs arguments for protection (infant industry argument, employment protection, national defense, anti-dumping).' }
    ]
  },

  // 15. International Trade: Institutions
  {
    targetDir: 'economics/international-trade/international-institutions',
    title: 'International Financial & Trade Institutions: IMF, World Bank, ADB, and WTO',
    kicker: 'International Trade',
    oldDirs: [
      'economics/international-trade/institutions/imf',
      'economics/international-trade/institutions/ibrd',
      'economics/international-trade/institutions/ida',
      'economics/international-trade/institutions/adb',
      'economics/international-trade/institutions/wto'
    ],
    summaryIntro: 'Comprehensive institutional overview of global multilateral financial and trade bodies, functions, SDRs, development lending, and dispute settlement.',
    points: [
      { bold: 'International Monetary Fund (IMF):', desc: 'Bretton Woods twin. Exchange rate surveillance, short-term BoP assistance, conditionality, Special Drawing Rights (SDRs), and quota revisions.' },
      { bold: 'World Bank Group (IBRD & IDA):', desc: 'IBRD (middle-income country reconstruction/development loans) and IDA ("soft loan window" offering long-term interest-free credits to poorest nations).' },
      { bold: 'Asian Development Bank (ADB):', desc: 'Headquarters in Manila (1966); promoting social and economic development in Asia-Pacific through concessional sovereign and private loans.' },
      { bold: 'World Trade Organization (WTO):', desc: 'Established 1995 replacing GATT (1947). Ministerial conferences, Most Favoured Nation (MFN) rule, national treatment, TRIPS, TRIMS, and dispute settlement body.' }
    ]
  },

  // 16. Macro Economics: National Income Accounting
  {
    targetDir: 'economics/macro-economics/national-income-accounting',
    title: 'National Income Accounting: Concepts, Aggregates, and Methods of Measurement',
    kicker: 'Macroeconomics',
    oldDirs: [
      'economics/macro-economics/national-income/concept',
      'economics/macro-economics/national-income/components',
      'economics/macro-economics/national-income/methods-of-accounting'
    ],
    summaryIntro: 'A foundational macroeconomic text covering circular flow of income, definitions by Marshall, Pigou, and Fisher, national accounting identities, and estimation methods.',
    points: [
      { bold: 'National Income Aggregates:', desc: 'GDP, NDP, GNP, NNP, National Income (NNP_fc), Personal Income (PI), and Personal Disposable Income (PDI). Depreciation and Net Indirect Tax adjustments.' },
      { bold: 'Three Measurement Methods:', desc: 'Product / Value Added Method, Income Method (factor payments: wages, rent, interest, profit), and Expenditure Method (C + I + G + X - M).' },
      { bold: 'Circular Flow of Income:', desc: 'Real flows vs money flows in 2-sector, 3-sector, and 4-sector open economies. Leakages (savings, taxes, imports) vs Injections (investment, government spending, exports).' },
      { bold: 'Nominal vs Real GDP & Accounting Difficulties:', desc: 'GDP deflator. Pitfalls: non-monetized transactions, informal economy, transfer payments, and double counting prevention.' }
    ]
  },

  // 17. Macro Economics: Employment & Consumption
  {
    targetDir: 'economics/macro-economics/employment-and-consumption',
    title: 'Macroeconomic Theories of Employment, Output, Consumption, and Investment',
    kicker: 'Macroeconomics',
    oldDirs: [
      'economics/macro-economics/employment-and-income/classical-theory',
      'economics/macro-economics/employment-and-income/keynesian-theory',
      'economics/macro-economics/consumption-and-investment/consumption-function',
      'economics/macro-economics/consumption-and-investment/investment-function'
    ],
    summaryIntro: 'A central macroeconomic chapter contrasting Say\'s Law and Classical wage-price flexibility against Keynesian Effective Demand, consumption psychology, and investment multiplier.',
    points: [
      { bold: 'Classical Theory of Employment:', desc: 'Say\'s Law of Markets ("Supply creates its own demand"), full employment assumption, Pigou\'s wage cut policy, and quantity theory of money link.' },
      { bold: 'Keynesian General Theory (1936):', desc: 'Rejection of automatic full employment. Principle of Effective Demand (Aggregate Demand Price = Aggregate Supply Price). Underemployment equilibrium.' },
      { bold: 'Consumption Function (Propensity to Consume):', desc: 'Keynesian Psychological Law of Consumption. Average Propensity to Consume (APC) and Marginal Propensity to Consume (MPC: 0 < MPC < 1).' },
      { bold: 'Investment Function & Multiplier:', desc: 'Autonomous vs Induced investment. Marginal Efficiency of Capital (MEC) vs rate of interest. Investment Multiplier (K = 1 / (1 - MPC) = 1 / MPS).' }
    ]
  },

  // 18. Macro Economics: Inflation & Stagflation
  {
    targetDir: 'economics/macro-economics/inflation-and-stagflation',
    title: 'Inflation, Reflation, Stagflation: Causes, Effects, and Control Measures',
    kicker: 'Macroeconomics',
    oldDirs: [
      'economics/macro-economics/inflation/causes',
      'economics/macro-economics/inflation/control-measures',
      'economics/macro-economics/inflation/reflation',
      'economics/macro-economics/inflation/stagflation'
    ],
    summaryIntro: 'Comprehensive coverage of monetary disequilibrium, demand-pull and cost-push inflation, inflationary gap, Phillips Curve, stagflation, and stabilization policies.',
    points: [
      { bold: 'Types and Causes of Inflation:', desc: 'Demand-Pull Inflation (excessive aggregate demand) vs Cost-Push Inflation (rising input/wage costs). Creeping, walking, running, and hyperinflation.' },
      { bold: 'Keynesian Inflationary Gap:', desc: 'Excess of aggregate demand over aggregate supply at full employment level of real output.' },
      { bold: 'Stagflation & Phillips Curve:', desc: 'Original Phillips Curve (inverse relationship between inflation and unemployment) breakdown during 1970s stagflation (stagnant growth + high inflation).' },
      { bold: 'Policy Measures to Combat Inflation:', desc: 'Monetary policy tightening (hiking policy rates, CRR, reverse repo), fiscal surplus budgeting, and direct price/supply management.' }
    ]
  },

  // 19. Micro Economics: Indifference Curve Analysis
  {
    targetDir: 'economics/micro-economics/consumer-behaviour/indifference-curve-analysis',
    title: 'Indifference Curve Analysis: Consumer Equilibrium, Price, Income, and Substitution Effects',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/consumer-behaviour/indifference-curve-technique',
      'economics/micro-economics/consumer-behaviour/consumer-equilibrium',
      'economics/micro-economics/consumer-behaviour/indifference-curve-effects/price-effect',
      'economics/micro-economics/consumer-behaviour/indifference-curve-effects/income-effect',
      'economics/micro-economics/consumer-behaviour/indifference-curve-effects/substitution-effect'
    ],
    summaryIntro: 'A foundational ordinal utility module covering indifference curve properties, marginal rate of substitution, budget constraint, and Hicksian/Slutsky decomposition.',
    points: [
      { bold: 'Indifference Curve Concept & Properties:', desc: 'Locus of consumption bundles yielding equal satisfaction. Downward sloping, convex to the origin due to Diminishing Marginal Rate of Substitution (MRS_xy), non-intersecting.' },
      { bold: 'Budget Line (Price Line):', desc: 'Equation: P_x * X + P_y * Y = M. Slope = -(P_x / P_y).' },
      { bold: 'Consumer\'s Equilibrium:', desc: 'Tangency condition where MRS_xy = P_x / P_y and indifference curve must be strictly convex to origin.' },
      { bold: 'Decomposition of Price Effect:', desc: 'Price Effect = Substitution Effect + Income Effect. Hicksian (compensating variation in income) vs Slutsky (cost-difference approach) decompositions for normal, inferior, and Giffen goods.' }
    ]
  },

  // 20. Micro Economics: Demand, Elasticity & Utility
  {
    targetDir: 'economics/micro-economics/consumer-behaviour/demand-and-utility',
    title: 'Demand Theory, Elasticity of Demand, Utility Analysis, and Consumer\'s Surplus',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/consumer-behaviour/demand-theory',
      'economics/micro-economics/consumer-behaviour/law-of-demand',
      'economics/micro-economics/consumer-behaviour/elasticity-of-demand',
      'economics/micro-economics/consumer-behaviour/utility-analysis',
      'economics/micro-economics/consumer-behaviour/consumers-surplus'
    ],
    summaryIntro: 'Complete cardinal and ordinal demand fundamentals, Law of Diminishing Marginal Utility, Law of Demand, price/income/cross elasticity formulas, and Marshallian Consumer\'s Surplus.',
    points: [
      { bold: 'Cardinal Utility & Gossen\'s Laws:', desc: 'Total Utility (TU) and Marginal Utility (MU). Gossen\'s First Law (Law of Diminishing Marginal Utility) and Second Law (Law of Equi-Marginal Utility).' },
      { bold: 'Law of Demand & Determinants:', desc: 'Inverse price-quantity relationship. Market demand aggregation, movement along curve vs shift in demand curve, exceptions to law of demand.' },
      { bold: 'Elasticity of Demand (Price, Income, Cross):', desc: 'Price elasticity degrees (0, <1, 1, >1, infinity). Measurement: Total outlay method, point/geometric method, percentage method. Positive vs negative cross elasticity.' },
      { bold: 'Marshallian Consumer\'s Surplus:', desc: 'Difference between what a consumer is willing to pay and what they actually pay: CS = Total Utility - (Price * Quantity).' }
    ]
  },

  // 21. Micro Economics: Production Functions & Returns
  {
    targetDir: 'economics/micro-economics/production-theory/production-functions-and-returns',
    title: 'Theory of Production: Production Functions, Law of Variable Proportions, and Returns to Scale',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/production-theory/production-function',
      'economics/micro-economics/production-theory/cobb-douglas-production-function',
      'economics/micro-economics/production-theory/law-of-variable-proportions',
      'economics/micro-economics/production-theory/laws-of-returns',
      'economics/micro-economics/production-theory/returns-to-scale',
      'economics/micro-economics/production-theory/iso-product-curve-analysis'
    ],
    summaryIntro: 'In-depth study of physical input-output functions, short-run diminishing returns, long-run homogeneous production, isoquants, and producer equilibrium.',
    points: [
      { bold: 'Short-Run: Law of Variable Proportions:', desc: 'Behaviour of TP, AP, and MP as variable factor increases: Stage I (Increasing returns, MP > AP), Stage II (Diminishing returns, rational stage where AP > MP > 0), Stage III (Negative returns, MP < 0).' },
      { bold: 'Cobb-Douglas Production Function:', desc: 'Q = A * L^alpha * K^beta. Properties: constant returns to scale when alpha + beta = 1; elasticity of substitution is unity; output elasticities of labour and capital.' },
      { bold: 'Long-Run: Laws of Returns to Scale:', desc: 'Increasing, constant, and diminishing returns to scale driven by internal and external economies/diseconomies of scale.' },
      { bold: 'Isoquants & Producer Equilibrium:', desc: 'Equal product curves. Marginal Rate of Technical Substitution (MRTS_LK). Isocost line tangency: MRTS_LK = w / r.' }
    ]
  },

  // 22. Micro Economics: Cost and Revenue Curves
  {
    targetDir: 'economics/micro-economics/production-theory/cost-and-revenue-curves',
    title: 'Cost and Revenue Analysis: Short-Run and Long-Run Curves',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/production-theory/cost-curves',
      'economics/micro-economics/production-theory/revenue-curves'
    ],
    summaryIntro: 'Complete mathematical and graphical analysis of fixed, variable, average, and marginal cost curves alongside TR, AR, and MR in competitive and imperfect markets.',
    points: [
      { bold: 'Short-Run Cost Structure:', desc: 'Total Fixed Cost (TFC - horizontal), Total Variable Cost (TVC - inverse S), and Total Cost (TC = TFC + TVC). Average Fixed Cost (AFC - rectangular hyperbola).' },
      { bold: 'U-Shaped AC and MC Relationships:', desc: 'MC passes through minimum point of AVC and AC. MC = d(TC)/dQ. AC rises when MC > AC; falls when MC < AC.' },
      { bold: 'Long-Run Cost Curves (Envelope Curve):', desc: 'Long-Run Average Cost (LAC) as envelope of short-run SAC curves. Planning curve reflecting economies and diseconomies of scale.' },
      { bold: 'Revenue Concepts (TR, AR, MR):', desc: 'Perfect competition: P = AR = MR (horizontal). Monopoly / Imperfect competition: downward sloping AR and MR (MR lies below AR). Relationship: MR = AR * (1 - 1/e).' }
    ]
  },

  // 23. Micro Economics: Theories of Rent and Wages
  {
    targetDir: 'economics/micro-economics/distribution-theory/theories-of-rent-and-wages',
    title: 'Theory of Distribution: Marginal Productivity, Ricardian vs Modern Rent, and Wage Determination',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/distribution-theory/marginal-productivity-theory',
      'economics/micro-economics/distribution-theory/theories-of-rent/classical-theory',
      'economics/micro-economics/distribution-theory/theories-of-rent/modern-theory',
      'economics/micro-economics/distribution-theory/wage-determination/perfect-competition',
      'economics/micro-economics/distribution-theory/wage-determination/imperfect-competition'
    ],
    summaryIntro: 'A foundational microeconomic distribution chapter covering Marginal Productivity factor pricing, Ricardian differential rent, Marshallian quasi-rent, and competitive vs monopsonistic wage determination.',
    points: [
      { bold: 'Marginal Productivity Theory of Distribution:', desc: 'Factor rewarded according to value of its marginal product (VMP / MRP). Equilibrium where Factor Price = Marginal Revenue Product (MRP).' },
      { bold: 'Ricardian Theory of Rent:', desc: 'Rent as differential surplus arising from original and indestructible powers of soil (extensive and intensive cultivation). No-rent (marginal) land.' },
      { bold: 'Modern Theory of Rent & Quasi-Rent:', desc: 'Rent as transfer earnings surplus: Actual Earning - Transfer Earning. Marshall\'s Quasi-Rent as temporary surplus on man-made capital equipment in short run.' },
      { bold: 'Wage Determination Under Perfect vs Imperfect Competition:', desc: 'Interaction of labour demand (MRP curve) and labour supply. Monopsony and trade union collective bargaining wage determination.' }
    ]
  },

  // 24. Micro Economics: Theories of Interest and Profit
  {
    targetDir: 'economics/micro-economics/distribution-theory/theories-of-interest-and-profit',
    title: 'Theories of Interest and Profit: Classical, Loanable Funds, Liquidity Preference, and Knight\'s Theory',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/distribution-theory/theories-of-interest/neo-classical-theory',
      'economics/micro-economics/distribution-theory/theories-of-interest/keynesian-theory',
      'economics/micro-economics/distribution-theory/loanable-fund-theory',
      'economics/micro-economics/distribution-theory/liquidity-preference-theory',
      'economics/micro-economics/distribution-theory/knights-profit-theory'
    ],
    summaryIntro: 'A comprehensive study of capital and risk rewards: Classical real interest theory, Neo-Classical Loanable Funds, Keynesian Liquidity Preference, and non-insurable uncertainty profit theories.',
    points: [
      { bold: 'Classical & Loanable Funds Theories of Interest:', desc: 'Classical theory: equilibrium between real saving and investment. Neo-Classical (Wicksell, Ohlin): demand for loanable funds (Investment + Hoarding + Disinvestment) equals supply (Savings + Bank Money + Dishoarding).' },
      { bold: 'Keynesian Liquidity Preference Theory:', desc: 'Interest as purely monetary phenomenon rewarding parting with liquidity. Three motives for holding money: Transaction, Precautionary, and Speculative motive (liquidity trap).' },
      { bold: 'IS-LM Synthesis (Hicks-Hansen):', desc: 'Integration of real goods market equilibrium (IS curve) and money market equilibrium (LM curve) to determine simultaneous output and interest rate.' },
      { bold: 'Theories of Profit (Knight, Schumpeter, Walker):', desc: 'Frank Knight\'s Risk, Uncertainty and Profit (profit as reward for bearing non-insurable, unforeseen uncertainty) and Schumpeter\'s Dynamic Innovation Theory.' }
    ]
  },

  // 25. Micro Economics: Market Structures
  {
    targetDir: 'economics/micro-economics/market-structures',
    title: 'Market Structures: Perfect Competition, Monopoly, Monopolistic Competition, and Oligopoly',
    kicker: 'Microeconomics',
    oldDirs: [
      'economics/micro-economics/market-theory/perfect-competition',
      'economics/micro-economics/market-theory/monopoly',
      'economics/micro-economics/market-theory/monopolistic-competition',
      'economics/micro-economics/market-theory/duopoly',
      'economics/micro-economics/market-theory/oligopoly',
      'economics/micro-economics/market-theory/equilibrium-of-firm',
      'economics/micro-economics/market-theory/price-output-determination'
    ],
    summaryIntro: 'The master comprehensive chapter on product market classifications, price-output determination under varying degrees of competition, product differentiation, and strategic interdependence.',
    points: [
      { bold: 'Perfect Competition:', desc: 'Large number of buyers/sellers, homogeneous products, price taker (P = AR = MR). Short-run supernormal/normal profit; long-run equilibrium at minimum LAC (P = MC = minimum LAC).' },
      { bold: 'Monopoly & Price Discrimination:', desc: 'Single seller, high entry barriers, price maker. Pigou\'s three degrees of price discrimination; dumping in international trade.' },
      { bold: 'Monopolistic Competition (Chamberlin):', desc: 'Large number of sellers, product differentiation, selling costs, excess capacity in long-run equilibrium.' },
      { bold: 'Oligopoly & Duopoly Models:', desc: 'Few interdependent firms. Paul Sweezy\'s Kinked Demand Curve model (price rigidity); Cournot, Bertrand, and Stackelberg duopoly models.' }
    ]
  },

  // 26. Money & Banking: Money Concepts & Supply
  {
    targetDir: 'economics/money-and-banking/money-concepts-and-supply',
    title: 'Money: Meaning, Functions, Demand, Supply, and Value of Money',
    kicker: 'Money & Banking',
    oldDirs: [
      'economics/money-and-banking/money/functions-of-money',
      'economics/money-and-banking/money/demand-for-money',
      'economics/money-and-banking/money/supply-of-money',
      'economics/money-and-banking/money/value-of-money',
      'economics/money-and-banking/money-supply/determinants'
    ],
    summaryIntro: 'Foundational monetary economics covering barter limitations, primary and secondary functions of money, money supply monetary aggregates (M1, M2, M3, M4), and high-powered money.',
    points: [
      { bold: 'Evolution & Functions of Money:', desc: 'Primary (Medium of exchange, Measure of value), Secondary (Store of value, Standard of deferred payments), and Contingent functions.' },
      { bold: 'Monetary Aggregates in India (RBI):', desc: 'M1 (Currency with public + Demand deposits + Other deposits with RBI), M2 (M1 + Post office savings), M3 (Broad Money: M1 + Time deposits with banks), M4 (M3 + Total post office deposits).' },
      { bold: 'High-Powered Money (Reserve Money - M0):', desc: 'Currency in circulation + Bankers\' deposits with RBI + Other deposits with RBI. High-powered money as the monetary base for credit creation.' },
      { bold: 'Determinants of Money Supply & Multiplier:', desc: 'Money Multiplier (m = M3 / M0) determined by currency-deposit ratio (c) and reserve-deposit ratio (r).' }
    ]
  },

  // 27. Money & Banking: Quantity Theories
  {
    targetDir: 'economics/money-and-banking/quantity-theories-of-money',
    title: 'Quantity Theory of Money: Fisher\'s Transaction Approach, Cambridge Cash-Balance, and Keynesian Reformulation',
    kicker: 'Money & Banking',
    oldDirs: [
      'economics/money-and-banking/quantity-theory-of-money/fisher',
      'economics/money-and-banking/quantity-theory-of-money/cambridge-approach',
      'economics/money-and-banking/quantity-theory-of-money/keynesian-approach'
    ],
    summaryIntro: 'An in-depth analysis of classical transaction equations of exchange, neoclassical cash-balance formulations, and Keynesian monetary transmission mechanism.',
    points: [
      { bold: 'Fisher\'s Transactions Approach:', desc: 'Equation of exchange: PT = MV + M\'V\'. Direct and proportional relation between money stock and price level; neutrality of money assumption.' },
      { bold: 'Cambridge Cash-Balance Approach:', desc: 'Equations by Marshall (M = kPY), Pigou (P = kR / M), Robertson (M = kPT), and Keynes (n = p(k + rk\')). Focus on money as store of value rather than just medium of exchange.' },
      { bold: 'Keynesian Reformulation of Quantity Theory:', desc: 'Money affects prices indirectly via interest rates and investment. Output changes before full employment; price level changes only after full employment.' },
      { bold: 'Milton Friedman\'s Modern Quantity Theory:', desc: 'Restatement of quantity theory as theory of demand for money. Stability of money demand function.' }
    ]
  },

  // 28. Money & Banking: Banking System & Credit Control
  {
    targetDir: 'economics/money-and-banking/banking-system-and-credit-control',
    title: 'Banking System: Commercial Banking, Credit Creation, Central Bank Functions, and Credit Control',
    kicker: 'Money & Banking',
    oldDirs: [
      'economics/money-and-banking/banking/commercial-banks/functions',
      'economics/money-and-banking/banking/commercial-banks/credit-creation',
      'economics/money-and-banking/banking/central-banks/functions',
      'economics/money-and-banking/credit-control-methods/quantitative-methods',
      'economics/money-and-banking/credit-control-methods/qualitative-methods',
      'economics/money-and-banking/monetary-policy/instruments'
    ],
    summaryIntro: 'Complete overview of financial intermediation, fractional reserve credit multiplier, Reserve Bank of India regulatory powers, quantitative and selective monetary tools.',
    points: [
      { bold: 'Commercial Bank Functions & Credit Creation:', desc: 'Accepting deposits, advancing loans. Credit creation multiplier = 1 / Cash Reserve Ratio (CRR). Primary cash deposits vs derivative credit deposits.' },
      { bold: 'Central Bank Functions (Reserve Bank of India):', desc: 'Bank of issue, banker to government, bankers\' bank and lender of last resort, custodian of foreign exchange reserves, controller of credit.' },
      { bold: 'Quantitative / General Credit Control Tools:', desc: 'Bank Rate, Repo and Reverse Repo Rates, Cash Reserve Ratio (CRR), Statutory Liquidity Ratio (SLR), and Open Market Operations (OMO).' },
      { bold: 'Qualitative / Selective Credit Control Tools:', desc: 'Fixing margin requirements on collateral, regulation of consumer credit, rationing of credit, moral suasion, and direct action.' }
    ]
  },

  // 29. Population Theory
  {
    targetDir: 'economics/population-theory/theories-of-population',
    title: 'Theories of Population: Malthusian Theory and Optimum Population Theory',
    kicker: 'Population Theory',
    oldDirs: [
      'economics/population-theory/malthus-theory',
      'economics/population-theory/optimum-population-theory'
    ],
    summaryIntro: 'A foundational demographic economics chapter contrasting Thomas Malthus\'s pessimistic natural ratios against the modern Optimum Population model (Edwin Cannan, Dalton, Robbins).',
    points: [
      { bold: 'Malthusian Theory of Population (1798):', desc: 'Population increases in geometric progression (1, 2, 4, 8, 16...) while food production increases in arithmetic progression (1, 2, 3, 4, 5...).' },
      { bold: 'Malthusian Checks:', desc: 'Preventive checks (moral restraint, delayed marriage) and Positive checks (famines, epidemics, wars). Iron Law of Wages connection.' },
      { bold: 'Optimum Theory of Population (Cannan, Dalton, Carr-Saunders):', desc: 'Point of population which, combined with other existing resources, yields maximum output per capita. Under-population vs over-population.' },
      { bold: 'Dalton\'s Maladjustment Formula:', desc: 'M = (A - O) / O, where A is Actual Population, O is Optimum Population, and M is degree of maladjustment (positive = overpopulation, negative = underpopulation).' }
    ]
  },

  // 30. Public Finance: Nature & Maximum Social Advantage
  {
    targetDir: 'economics/public-finance/nature-and-maximum-social-advantage',
    title: 'Public Finance: Meaning, Scope, and Principle of Maximum Social Advantage',
    kicker: 'Public Finance',
    oldDirs: [
      'economics/public-finance/private-finance',
      'economics/public-finance/public-finance',
      'economics/public-finance/maximum-social-advantage',
      'economics/public-finance/maximum-social-welfare'
    ],
    summaryIntro: 'A foundational study of public economy, public vs private finance differences, Musgrave\'s three fiscal branches, and Dalton-Pigou Principle of Maximum Social Advantage.',
    points: [
      { bold: 'Nature & Scope of Public Finance:', desc: 'Study of government revenue, public expenditure, public debt, and financial administration. Richard Musgrave\'s 3 fiscal functions: Allocation, Distribution, and Stabilization.' },
      { bold: 'Public Finance vs Private Finance:', desc: 'Adjustment of income and expenditure, elasticity of finance, borrowing powers (internal vs external), motive (social welfare vs individual profit), and secrecy.' },
      { bold: 'Principle of Maximum Social Advantage (Dalton):', desc: 'Fiscal operations must maximize net social welfare: Marginal Social Sacrifice of Taxation (MSS) = Marginal Social Benefit of Public Expenditure (MSB).' },
      { bold: 'Pigou\'s Ideal State of Public Finance:', desc: 'Expenditure should be pushed in all directions up to the point where utility of marginal pound spent equals satisfaction lost from marginal pound raised in taxes.' }
    ]
  },

  // 31. Public Finance: Canons & Theories of Taxation
  {
    targetDir: 'economics/public-finance/canons-and-theories-of-taxation',
    title: 'Taxation: Canons, Ability to Pay Theory, Impact, Incidence, and Economic Effects',
    kicker: 'Public Finance',
    oldDirs: [
      'economics/public-finance/taxation/principles',
      'economics/public-finance/taxation/ability-to-pay-and-profit-theory',
      'economics/public-finance/taxation/impact-of-tax',
      'economics/public-finance/taxation/incidence-of-tax',
      'economics/public-finance/taxation/economic-effects',
      'economics/public-finance/taxation/justice-in-taxes'
    ],
    summaryIntro: 'An authoritative study of tax economics, Adam Smith\'s four canons of taxation, proportional vs progressive tax equity, shifting, impact, and ultimate incidence.',
    points: [
      { bold: 'Adam Smith\'s Four Canons of Taxation:', desc: 'Canon of Equality / Ability, Canon of Certainty, Canon of Convenience, and Canon of Economy. Modern canons: Productivity, Elasticity, and Flexibility.' },
      { bold: 'Theories of Tax Distribution / Equity:', desc: 'Benefit Received Theory (Lindahl/Bowen) vs Ability to Pay Theory (Sacrifice approaches: Equal Absolute, Equal Proportional, Equal Marginal Sacrifice).' },
      { bold: 'Impact, Shifting, and Incidence of Taxation:', desc: 'Impact (initial money burden on person who pays legally), Shifting (transferring burden forward to buyer or backward to supplier), Incidence (ultimate resting point of money burden).' },
      { bold: 'Economic Effects of Taxation:', desc: 'Effects on ability to work and save, willingness to work and save, resource allocation across industries, and income distribution.' }
    ]
  },

  // 32. Public Finance: Public Debt & Expenditure
  {
    targetDir: 'economics/public-finance/public-debt-and-expenditure',
    title: 'Public Expenditure and Public Debt: Principles, Burden, and Redemption',
    kicker: 'Public Finance',
    oldDirs: [
      'economics/public-finance/public-expenditure/principles',
      'economics/public-finance/public-expenditure/objectives',
      'economics/public-finance/public-debt/burden',
      'economics/public-finance/public-debt/redemption',
      'economics/public-finance/public-debt',
      'economics/public-finance/deficit-financing'
    ],
    summaryIntro: 'Comprehensive coverage of public outlay canons, Wagner\'s Law of increasing state activities, public debt classification, shifting burden across generations, and debt redemption.',
    points: [
      { bold: 'Canons of Public Expenditure (Findlay Shirras):', desc: 'Canon of Benefit, Canon of Economy, Canon of Sanction, and Canon of Surplus.' },
      { bold: 'Wagner\'s Law & Wiseman-Peacock Hypothesis:', desc: 'Adolph Wagner: Law of increasing state activities as economies industrialize. Wiseman-Peacock: Displacement, inspection, and concentration effects during social upheavals.' },
      { bold: 'Public Debt: Classification and Burden:', desc: 'Internal vs External debt; Productive vs Deadweight debt; Funded vs Floating debt. Real direct burden vs money burden of debt.' },
      { bold: 'Methods of Debt Redemption & Deficit Financing:', desc: 'Refunding, Sinking Fund creation, Capital levy, Budget surplus redemption. Role of Deficit Financing in developing economies and inflationary risks.' }
    ]
  },

  // 33. Public Finance: Fiscal Federalism & Budget
  {
    targetDir: 'economics/public-finance/fiscal-federalism-and-budget',
    title: 'Fiscal Federalism: Union-State Financial Relations, Finance Commission, and Union Budget',
    kicker: 'Public Finance',
    oldDirs: [
      'economics/public-finance/centre-and-states/revenue-sources',
      'economics/public-finance/centre-and-states/expenditure',
      'economics/public-finance/finance-commission',
      'economics/public-finance/union-budget/components'
    ],
    summaryIntro: 'Constitutional financial relations in India (Articles 268-293), tax division, Finance Commission horizontal/vertical devolution criteria, and Union Budget accounting.',
    points: [
      { bold: 'Centre-State Financial Relations:', desc: 'Division of taxation powers (Union List, State List, Concurrent List). GST (101st Constitutional Amendment Act) and unified indirect taxation.' },
      { bold: 'Finance Commission of India (Article 280):', desc: 'Constitutional quasi-judicial body appointed every 5 years by the President. Vertical devolution of net tax proceeds and horizontal distribution formula among states.' },
      { bold: 'Components of Union Budget:', desc: 'Revenue Budget (Revenue Receipts: tax and non-tax; Revenue Expenditure) and Capital Budget (Capital Receipts: borrowings, disinvestment; Capital Expenditure).' },
      { bold: 'Budgetary Deficit Concepts:', desc: 'Fiscal Deficit = Total Expenditure - Total Receipts excluding borrowings; Revenue Deficit = Revenue Expenditure - Revenue Receipts; Primary Deficit = Fiscal Deficit - Interest Payments.' }
    ]
  }
];

function generateEconomicsHtml(item) {
  const checklistItems = item.points.map(p => `
          <label class="check-item"><input type="checkbox"> <span><strong>${p.bold}</strong> ${p.desc}</span></label>`).join('');

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${item.title} — Economics Study Guide | SJ Maths</title>
<meta name="description" content="${item.summaryIntro.replace(/"/g, '&quot;')}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="SJ Maths">
<meta name="theme-color" content="#16324f">
<link rel="canonical" href="https://sjmaths.com/${item.targetDir}/">
<link rel="icon" type="image/png" href="/favicon.png">

<meta property="og:type" content="article">
<meta property="og:site_name" content="SJ Maths">
<meta property="og:title" content="${item.title} — Economics Study Guide">
<meta property="og:description" content="${item.summaryIntro.replace(/"/g, '&quot;')}">
<meta property="og:url" content="https://sjmaths.com/${item.targetDir}/">
<meta property="og:image" content="https://sjmaths.com/assets/images/og-default.jpg">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${item.title} — Economics Study Guide">
<meta name="twitter:description" content="${item.summaryIntro.replace(/"/g, '&quot;')}">

<style>
:root {
  --bg: #f5f8fc;
  --surface: #ffffff;
  --ink: #162438;
  --ink2: #465b77;
  --muted: #6f829c;
  --border: #dbe4f0;
  --primary: #1d4ed8;
  --primary-bg: #eff6ff;
  --accent: #d97706;
  --accent-bg: #fffbeb;
  --green: #15803d;
  --green-bg: #f0fdf4;
  --red: #b91c1c;
  --radius: 14px;
  --shadow: 0 8px 24px rgba(22, 36, 56, 0.08);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.6;
  padding-bottom: 60px;
}
.site-header {
  background: #112239;
  color: #fff;
  padding: 14px 20px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.header-inner {
  max-width: 1040px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.brand-link {
  color: #fff;
  text-decoration: none;
  font-weight: 700;
  font-size: 1.15rem;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.brand-sub {
  font-size: 0.72rem;
  color: #93c5fd;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding-left: 6px;
  border-left: 1px solid rgba(255,255,255,0.2);
}
.back-btn {
  color: #dbeafe;
  text-decoration: none;
  font-size: 0.82rem;
  border: 1px solid rgba(255,255,255,0.18);
  padding: 6px 12px;
  border-radius: 6px;
  transition: background .15s;
}
.back-btn:hover { background: rgba(255,255,255,0.08); }

.wrap { max-width: 1040px; margin: 0 auto; padding: 24px 20px 0; }

.hero {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 28px 32px;
  box-shadow: var(--shadow);
  margin-bottom: 24px;
}
.breadcrumb {
  font-size: 0.8rem;
  color: var(--muted);
  margin-bottom: 10px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
}
.breadcrumb a { color: var(--primary); text-decoration: none; }
.breadcrumb a:hover { text-decoration: underline; }
.kicker {
  color: var(--primary);
  font-size: 0.76rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  margin-bottom: 6px;
}
h1 {
  font-size: 1.7rem;
  font-weight: 800;
  line-height: 1.3;
  margin-bottom: 10px;
  color: #0f172a;
}
.lead { font-size: 0.95rem; color: var(--ink2); margin-bottom: 16px; }

.exam-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 8px;
}
.exam-chip {
  background: var(--primary-bg);
  color: var(--primary);
  border: 1px solid #bfdbfe;
  font-size: 0.76rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 999px;
  text-decoration: none;
}
.exam-chip:hover { background: #dbeafe; }

.main-grid {
  display: grid;
  grid-template-columns: 1fr 310px;
  gap: 24px;
  align-items: start;
}
@media(max-width:840px) {
  .main-grid { grid-template-columns: 1fr; }
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px 28px;
  box-shadow: var(--shadow);
  margin-bottom: 20px;
}
.card h2 {
  font-size: 1.15rem;
  font-weight: 700;
  margin-bottom: 12px;
  color: #0f172a;
}
.card p { font-size: 0.92rem; color: var(--ink2); margin-bottom: 12px; }

.checklist {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 12px;
}
.check-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-size: 0.88rem;
  color: var(--ink2);
  cursor: pointer;
}
.check-item input[type="checkbox"] {
  margin-top: 4px;
  accent-color: var(--primary);
}

.sidebar-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px 22px;
  box-shadow: var(--shadow);
  margin-bottom: 20px;
  position: sticky;
  top: 20px;
}
.sidebar-card h3 { font-size: 0.96rem; font-weight: 700; margin-bottom: 8px; }
.action-box {
  background: var(--primary-bg);
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  padding: 14px;
  margin-top: 10px;
}
.action-box strong { font-size: 0.86rem; color: #1e3a8a; display: block; margin-bottom: 4px; }
.action-box p { font-size: 0.78rem; color: #1d4ed8; margin-bottom: 10px; }
.action-btn {
  display: inline-block;
  background: var(--primary);
  color: #fff;
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 6px 14px;
  border-radius: 6px;
  transition: background .15s;
}
.action-btn:hover { background: #1e40af; }

.footer {
  border-top: 1px solid var(--border);
  margin-top: 48px;
  padding: 24px 20px;
  font-size: 0.82rem;
  color: var(--muted);
  background: var(--surface);
}
.footer-inner {
  max-width: 1040px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}
.footer a { color: var(--primary); text-decoration: none; }
</style>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a class="brand-link" href="/">
      <span>SJ Maths</span>
      <span class="brand-sub">Economics</span>
    </a>
    <a class="back-btn" href="/up-pgt-economics/">← Back to UP PGT Economics</a>
  </div>
</header>

<main class="wrap">
  <section class="hero">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a>
      <span>›</span>
      <a href="/up-pgt-economics/">Economics</a>
      <span>›</span>
      <span>${item.kicker}</span>
      <span>›</span>
      <span>${item.title}</span>
    </nav>
    <div class="kicker">${item.kicker}</div>
    <h1>${item.title}</h1>
    <p class="lead">${item.summaryIntro}</p>

    <div class="exam-badges">
      <span style="font-size:.74rem;color:var(--muted);align-self:center">Appears in:</span>
      <a class="exam-chip" href="/up-pgt-economics/">UP PGT Economics Tracker →</a>
      <a class="exam-chip" href="/up-tgt-social-science/">UP TGT Social Science Tracker →</a>
    </div>
  </section>

  <div class="main-grid">
    <div class="content-col">
      <article class="card">
        <h2>1. Syllabus Overview &amp; Exam Focus</h2>
        <p>In the official teacher recruitment and competitive syllabus, <strong>${item.title}</strong> is a core examination unit of <em>${item.kicker}</em>. Questions test fundamental theories, key definitions, policy frameworks, graphical properties, and real-world economic applications.</p>
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
          <label class="check-item"><input type="checkbox"> <span>Memorized essential definitions, formulas &amp; economic laws</span></label>
          <label class="check-item"><input type="checkbox"> <span>Solved minimum 20 previous years' questions (PYQ)</span></label>
          <label class="check-item"><input type="checkbox"> <span>Attempted timed self-assessment test</span></label>
          <label class="check-item"><input type="checkbox"> <span>Marked complete on main syllabus tracker</span></label>
        </div>
      </article>
    </div>

    <aside class="sidebar-col">
      <div class="sidebar-card">
        <h3>Exam Trackers</h3>
        <p style="font-size:.84rem;color:var(--ink2);margin:0 0 12px">Track this topic alongside the complete syllabus on your exam progress trackers.</p>
        <div class="action-box">
          <strong>UP PGT Economics</strong>
          <p>Interactive progress tracking, instant search &amp; filter</p>
          <a class="action-btn" href="/up-pgt-economics/">Open PGT Tracker →</a>
        </div>
        <div class="action-box" style="margin-top:12px;background:#f0fdf4;border-color:#bbf7d0">
          <strong style="color:#166534">UP TGT Social Science</strong>
          <p style="color:#15803d">Economics section syllabus tracking &amp; PYQs</p>
          <a class="action-btn" href="/up-tgt-social-science/" style="background:#16a34a">Open TGT Tracker →</a>
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
      <a href="/up-pgt-economics/">UP PGT Economics</a> &nbsp;•&nbsp;
      <a href="/up-tgt-social-science/">UP TGT Social Science</a>
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

  const html = generateEconomicsHtml(item);
  fs.writeFileSync(path.join(targetDirAbs, 'index.html'), html, 'utf8');
  console.log(`Created consolidated Economics page: ${item.targetDir}/index.html`);
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
console.log(`Total fragmented Economics sub-directories deleted: ${deletedTotal}`);

// 3. Clean up empty parent directories inside economics
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

  if (dir !== path.join(ROOT, 'economics') && fs.readdirSync(dir).length === 0) {
    fs.rmdirSync(dir);
    console.log(`Removed empty parent directory: ${path.relative(ROOT, dir)}`);
  }
}
cleanEmptyDirs(path.join(ROOT, 'economics'));

console.log('Economics consolidation and directory cleanup complete.');
