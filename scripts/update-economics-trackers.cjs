const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// Map of old fragmented economics paths to the new consolidated paths
const mapping = [
  // Economic Systems
  {
    from: [
      'economics/economic-systems/capitalism',
      'economics/economic-systems/socialism',
      'economics/economic-systems/mixed-economy'
    ],
    to: '/economics/economic-systems/',
    title: 'Economic Systems: Capitalism, Socialism, and Mixed Economy'
  },
  // Economic Theory
  {
    from: [
      'economics/economic-theory/foundations/definition',
      'economics/economic-theory/foundations/nature',
      'economics/economic-theory/analysis/micro-analysis',
      'economics/economic-theory/analysis/macro-analysis',
      'economics/economic-theory/analysis/static-analysis',
      'economics/economic-theory/analysis/dynamic-analysis',
      'economics/economic-theory/foundations',
      'economics/economic-theory/analysis'
    ],
    to: '/economics/economic-theory/foundations-and-analysis/',
    title: 'Economic Theory: Definition, Nature, Micro vs Macro, Static vs Dynamic Analysis'
  },
  // Elementary Statistics: Central Tendency
  {
    from: [
      'economics/elementary-statistics/central-tendency/mean',
      'economics/elementary-statistics/central-tendency/median',
      'economics/elementary-statistics/central-tendency/mode'
    ],
    to: '/economics/elementary-statistics/central-tendency/',
    title: 'Measures of Central Tendency: Mean, Median, and Mode'
  },
  // Growth & Development
  {
    from: [
      'economics/growth-and-development/theories/harrod-domar',
      'economics/growth-and-development/theories/lewis',
      'economics/growth-and-development/theories/rostow',
      'economics/growth-and-development/theories'
    ],
    to: '/economics/growth-and-development/theories-of-growth/',
    title: 'Theories of Economic Growth: Harrod-Domar, Arthur Lewis, and Rostow'
  },
  {
    from: [
      'economics/growth-and-development/economic-development',
      'economics/growth-and-development/economic-progress',
      'economics/growth-and-development/measures-of-development',
      'economics/growth-and-development/problems-of-economic-development',
      'economics/growth-and-development/reasons-of-low-economic-development',
      'economics/growth-and-development/vicious-circle-of-poverty'
    ],
    to: '/economics/growth-and-development/concepts-and-obstacles/',
    title: 'Economic Development: Concepts, Measures, Obstacles, and Vicious Circle of Poverty'
  },
  // Indian Economy: Agriculture
  {
    from: [
      'economics/indian-economy/agriculture-sector/problems',
      'economics/indian-economy/agriculture-sector/problems/solutions',
      'economics/indian-economy/agriculture-sector/farmers/small-farmers',
      'economics/indian-economy/agriculture-sector/farmers/marginal-farmers',
      'economics/indian-economy/agriculture-sector/farmers-and-problems'
    ],
    to: '/economics/indian-economy/agricultural-problems-and-farmers/',
    title: 'Indian Agriculture: Problems, Marginal and Small Farmers, and Solutions'
  },
  {
    from: [
      'economics/indian-economy/agriculture-sector/agricultural-marketing',
      'economics/indian-economy/agriculture-sector/agricultural-price-policy',
      'economics/indian-economy/agriculture-sector/food-security',
      'economics/indian-economy/agriculture-sector/public-distribution-system',
      'economics/indian-economy/agriculture-sector/marketing-and-food-security'
    ],
    to: '/economics/indian-economy/agricultural-marketing-and-food-security/',
    title: 'Agricultural Marketing, Price Policy, Public Distribution System, and Food Security'
  },
  {
    from: [
      'economics/indian-economy/agriculture-sector/rural-development-programmes'
    ],
    to: '/economics/indian-economy/rural-development-programmes/',
    title: 'Rural Development Programmes in India'
  },
  // Indian Economy: Employment & Unemployment
  {
    from: [
      'economics/indian-economy/employment/visible-unemployment',
      'economics/indian-economy/employment/invisible-unemployment',
      'economics/indian-economy/employment/under-employment',
      'economics/indian-economy/employment/unemployment/causes',
      'economics/indian-economy/employment/unemployment/remedies',
      'economics/indian-economy/employment/unemployment-in-india'
    ],
    to: '/economics/indian-economy/unemployment-in-india/',
    title: 'Unemployment in India: Types, Causes, and Remedial Measures'
  },
  // Indian Economy: Foreign Trade
  {
    from: [
      'economics/indian-economy/foreign-trade/structure',
      'economics/indian-economy/foreign-trade/recent-trends',
      'economics/indian-economy/foreign-trade/import-substitution'
    ],
    to: '/economics/indian-economy/foreign-trade/',
    title: 'Foreign Trade of India: Structure, Recent Trends, and Import Substitution'
  },
  // Indian Economy: Industrial Sector & MSME
  {
    from: [
      'economics/indian-economy/industrial-sector/industrial-policy',
      'economics/indian-economy/industrial-sector/new-industrial-policy',
      'economics/indian-economy/industrial-sector/problems-of-industrialisation',
      'economics/indian-economy/industrial-sector/msme-sector/micro-enterprises',
      'economics/indian-economy/industrial-sector/msme-sector/small-enterprises',
      'economics/indian-economy/industrial-sector/msme-sector/medium-enterprises',
      'economics/indian-economy/industrial-sector/msme-sector',
      'economics/indian-economy/industrial-sector/policy-and-msme'
    ],
    to: '/economics/indian-economy/industrial-policy-and-msme/',
    title: 'Industrial Development in India: Policies, Problems, and MSME Sector'
  },
  // Indian Economy: National Income
  {
    from: [
      'economics/indian-economy/national-income/structure',
      'economics/indian-economy/national-income/distribution'
    ],
    to: '/economics/indian-economy/national-income-structure/',
    title: 'National Income in India: Sectoral Structure, Growth Trends, and Inequalities'
  },
  // Indian Economy: Industrial Relations
  {
    from: [
      'economics/indian-economy/industrial-relations/industrial-disputes',
      'economics/indian-economy/industrial-relations/trade-unions/role'
    ],
    to: '/economics/indian-economy/industrial-relations/',
    title: 'Industrial Relations in India: Disputes and Role of Trade Unions'
  },
  // Indian Economy: Policies
  {
    from: [
      'economics/indian-economy/policies/population',
      'economics/indian-economy/policies/poverty',
      'economics/indian-economy/policies/unemployment',
      'economics/indian-economy/policies'
    ],
    to: '/economics/indian-economy/policies-for-poverty-population-and-unemployment/',
    title: 'Socio-Economic Policies: Poverty, Population, and Unemployment in India'
  },
  // Indian Economy: Population
  {
    from: [
      'economics/indian-economy/population/trends'
    ],
    to: '/economics/indian-economy/demographic-trends-in-india/',
    title: 'Demographic Trends and Population Dynamics in India'
  },
  // International Trade: Theories
  {
    from: [
      'economics/international-trade/trade-theories/comparative-cost-theory',
      'economics/international-trade/trade-theories/reciprocal-demand-theory',
      'economics/international-trade/trade-theories/opportunity-cost-theory',
      'economics/international-trade/trade-theories/heckscher-ohlin-theory',
      'economics/international-trade/trade-theories/leontief-paradox',
      'economics/international-trade/trade-theories'
    ],
    to: '/economics/international-trade/theories-of-trade/',
    title: 'Theories of International Trade: Comparative Cost, Heckscher-Ohlin, and Opportunity Cost'
  },
  // International Trade: BoP & Exchange Rate
  {
    from: [
      'economics/international-trade/balance-of-payments/causes-of-imbalance',
      'economics/international-trade/balance-of-payments/remedies',
      'economics/international-trade/balance-of-payments',
      'economics/international-trade/foreign-exchange-rate-determination/purchasing-power-parity',
      'economics/international-trade/foreign-exchange-rate-determination/balance-of-payments-theory',
      'economics/international-trade/foreign-exchange-rate-determination',
      'economics/international-trade/trade-policy/free-trade',
      'economics/international-trade/trade-policy/protection'
    ],
    to: '/economics/international-trade/balance-of-payments-and-exchange-rate/',
    title: 'Balance of Payments, Foreign Exchange Determination, and Trade Policy'
  },
  // International Trade: Institutions
  {
    from: [
      'economics/international-trade/institutions/imf',
      'economics/international-trade/institutions/ibrd',
      'economics/international-trade/institutions/ida',
      'economics/international-trade/institutions/adb',
      'economics/international-trade/institutions/wto',
      'economics/international-trade/institutions'
    ],
    to: '/economics/international-trade/international-institutions/',
    title: 'International Financial & Trade Institutions: IMF, World Bank, ADB, and WTO'
  },
  // Macro Economics: National Income Accounting
  {
    from: [
      'economics/macro-economics/national-income/concept',
      'economics/macro-economics/national-income/components',
      'economics/macro-economics/national-income/methods-of-accounting',
      'economics/macro-economics/national-income'
    ],
    to: '/economics/macro-economics/national-income-accounting/',
    title: 'National Income Accounting: Concepts, Aggregates, and Methods'
  },
  // Macro Economics: Employment & Consumption
  {
    from: [
      'economics/macro-economics/employment-and-income/classical-theory',
      'economics/macro-economics/employment-and-income/keynesian-theory',
      'economics/macro-economics/consumption-and-investment/consumption-function',
      'economics/macro-economics/consumption-and-investment/investment-function',
      'economics/macro-economics/employment-and-income',
      'economics/macro-economics/consumption-and-investment'
    ],
    to: '/economics/macro-economics/employment-and-consumption/',
    title: 'Macroeconomic Theories of Employment, Output, Consumption, and Investment'
  },
  // Macro Economics: Inflation & Stagflation
  {
    from: [
      'economics/macro-economics/inflation/causes',
      'economics/macro-economics/inflation/control-measures',
      'economics/macro-economics/inflation/reflation',
      'economics/macro-economics/inflation/stagflation',
      'economics/macro-economics/inflation'
    ],
    to: '/economics/macro-economics/inflation-and-stagflation/',
    title: 'Inflation, Reflation, Stagflation: Causes, Effects, and Control Measures'
  },
  // Macro Economics: Trade Cycle Theories
  {
    from: [
      'economics/macro-economics/trade-cycle/theories',
      'economics/macro-economics/trade-cycle'
    ],
    to: '/economics/macro-economics/trade-cycle-theories/',
    title: 'Theories of Trade Cycles: Monetary, Innovation, and Keynesian'
  },
  // Micro Economics: Indifference Curve Analysis
  {
    from: [
      'economics/micro-economics/consumer-behaviour/indifference-curve-technique',
      'economics/micro-economics/consumer-behaviour/consumer-equilibrium',
      'economics/micro-economics/consumer-behaviour/indifference-curve-effects/price-effect',
      'economics/micro-economics/consumer-behaviour/indifference-curve-effects/income-effect',
      'economics/micro-economics/consumer-behaviour/indifference-curve-effects/substitution-effect',
      'economics/micro-economics/consumer-behaviour/indifference-curve-analysis'
    ],
    to: '/economics/micro-economics/indifference-curve-analysis/',
    title: 'Indifference Curve Analysis: Consumer Equilibrium, Price, Income, and Substitution Effects'
  },
  // Micro Economics: Demand & Utility
  {
    from: [
      'economics/micro-economics/consumer-behaviour/demand-theory',
      'economics/micro-economics/consumer-behaviour/law-of-demand',
      'economics/micro-economics/consumer-behaviour/elasticity-of-demand',
      'economics/micro-economics/consumer-behaviour/utility-analysis',
      'economics/micro-economics/consumer-behaviour/consumers-surplus',
      'economics/micro-economics/consumer-behaviour/demand-and-utility'
    ],
    to: '/economics/micro-economics/demand-and-utility/',
    title: 'Demand Theory, Elasticity of Demand, Utility Analysis, and Consumer\'s Surplus'
  },
  // Micro Economics: Revealed Preference
  {
    from: [
      'economics/micro-economics/consumer-behaviour/revealed-preference-theory'
    ],
    to: '/economics/micro-economics/revealed-preference-theory/',
    title: 'Samuelson\'s Revealed Preference Theory of Demand'
  },
  // Micro Economics: Production Functions
  {
    from: [
      'economics/micro-economics/production-theory/production-function',
      'economics/micro-economics/production-theory/cobb-douglas-production-function',
      'economics/micro-economics/production-theory/law-of-variable-proportions',
      'economics/micro-economics/production-theory/laws-of-returns',
      'economics/micro-economics/production-theory/returns-to-scale',
      'economics/micro-economics/production-theory/iso-product-curve-analysis',
      'economics/micro-economics/production-theory/production-functions-and-returns'
    ],
    to: '/economics/micro-economics/production-functions-and-returns/',
    title: 'Theory of Production: Production Functions, Law of Variable Proportions, and Returns to Scale'
  },
  // Micro Economics: Cost and Revenue
  {
    from: [
      'economics/micro-economics/production-theory/cost-curves',
      'economics/micro-economics/production-theory/revenue-curves',
      'economics/micro-economics/production-theory/cost-and-revenue-curves'
    ],
    to: '/economics/micro-economics/cost-and-revenue-curves/',
    title: 'Cost and Revenue Analysis: Short-Run and Long-Run Curves'
  },
  // Micro Economics: Theories of Rent and Wages
  {
    from: [
      'economics/micro-economics/distribution-theory/marginal-productivity-theory',
      'economics/micro-economics/distribution-theory/theories-of-rent/classical-theory',
      'economics/micro-economics/distribution-theory/theories-of-rent/modern-theory',
      'economics/micro-economics/distribution-theory/wage-determination/perfect-competition',
      'economics/micro-economics/distribution-theory/wage-determination/imperfect-competition',
      'economics/micro-economics/distribution-theory/theories-of-rent-and-wages'
    ],
    to: '/economics/micro-economics/theories-of-rent-and-wages/',
    title: 'Theory of Distribution: Marginal Productivity, Ricardian vs Modern Rent, and Wage Determination'
  },
  // Micro Economics: Theories of Interest and Profit
  {
    from: [
      'economics/micro-economics/distribution-theory/theories-of-interest/neo-classical-theory',
      'economics/micro-economics/distribution-theory/theories-of-interest/keynesian-theory',
      'economics/micro-economics/distribution-theory/loanable-fund-theory',
      'economics/micro-economics/distribution-theory/liquidity-preference-theory',
      'economics/micro-economics/distribution-theory/knights-profit-theory',
      'economics/micro-economics/distribution-theory/theories-of-interest-and-profit'
    ],
    to: '/economics/micro-economics/theories-of-interest-and-profit/',
    title: 'Theories of Interest and Profit: Classical, Loanable Funds, Liquidity Preference, and Knight\'s Theory'
  },
  // Micro Economics: Market Structures
  {
    from: [
      'economics/micro-economics/market-theory/perfect-competition',
      'economics/micro-economics/market-theory/monopoly',
      'economics/micro-economics/market-theory/monopolistic-competition',
      'economics/micro-economics/market-theory/duopoly',
      'economics/micro-economics/market-theory/oligopoly',
      'economics/micro-economics/market-theory/equilibrium-of-firm',
      'economics/micro-economics/market-theory/price-output-determination',
      'economics/micro-economics/market-theory'
    ],
    to: '/economics/micro-economics/market-structures/',
    title: 'Market Structures: Perfect Competition, Monopoly, Monopolistic Competition, and Oligopoly'
  },
  // Money & Banking: Money Concepts & Supply
  {
    from: [
      'economics/money-and-banking/money/functions-of-money',
      'economics/money-and-banking/money/demand-for-money',
      'economics/money-and-banking/money/supply-of-money',
      'economics/money-and-banking/money/value-of-money',
      'economics/money-and-banking/money-supply/determinants'
    ],
    to: '/economics/money-and-banking/money-concepts-and-supply/',
    title: 'Money: Meaning, Functions, Demand, Supply, and Value of Money'
  },
  // Money & Banking: Quantity Theories
  {
    from: [
      'economics/money-and-banking/quantity-theory-of-money/fisher',
      'economics/money-and-banking/quantity-theory-of-money/cambridge-approach',
      'economics/money-and-banking/quantity-theory-of-money/keynesian-approach',
      'economics/money-and-banking/quantity-theory-of-money'
    ],
    to: '/economics/money-and-banking/quantity-theories-of-money/',
    title: 'Quantity Theory of Money: Fisher\'s Approach, Cambridge Cash-Balance, and Keynes'
  },
  // Money & Banking: Banking System & Credit Control
  {
    from: [
      'economics/money-and-banking/banking/commercial-banks/functions',
      'economics/money-and-banking/banking/commercial-banks/credit-creation',
      'economics/money-and-banking/banking/central-banks/functions',
      'economics/money-and-banking/credit-control-methods/quantitative-methods',
      'economics/money-and-banking/credit-control-methods/qualitative-methods',
      'economics/money-and-banking/credit-control-methods',
      'economics/money-and-banking/monetary-policy/instruments'
    ],
    to: '/economics/money-and-banking/banking-system-and-credit-control/',
    title: 'Banking System: Commercial Banking, Credit Creation, Central Bank Functions, and Credit Control'
  },
  // Population Theory
  {
    from: [
      'economics/population-theory/malthus-theory',
      'economics/population-theory/optimum-population-theory'
    ],
    to: '/economics/population-theory/theories-of-population/',
    title: 'Theories of Population: Malthusian Theory and Optimum Population Theory'
  },
  // Public Finance: Nature & Maximum Social Advantage
  {
    from: [
      'economics/public-finance/private-finance',
      'economics/public-finance/public-finance',
      'economics/public-finance/maximum-social-advantage',
      'economics/public-finance/maximum-social-welfare'
    ],
    to: '/economics/public-finance/nature-and-maximum-social-advantage/',
    title: 'Public Finance: Meaning, Scope, and Principle of Maximum Social Advantage'
  },
  // Public Finance: Taxation
  {
    from: [
      'economics/public-finance/taxation/principles',
      'economics/public-finance/taxation/ability-to-pay-and-profit-theory',
      'economics/public-finance/taxation/impact-of-tax',
      'economics/public-finance/taxation/incidence-of-tax',
      'economics/public-finance/taxation/economic-effects',
      'economics/public-finance/taxation/justice-in-taxes',
      'economics/public-finance/taxation'
    ],
    to: '/economics/public-finance/canons-and-theories-of-taxation/',
    title: 'Taxation: Canons, Ability to Pay Theory, Impact, Incidence, and Economic Effects'
  },
  // Public Finance: Debt & Expenditure
  {
    from: [
      'economics/public-finance/public-expenditure/principles',
      'economics/public-finance/public-expenditure/objectives',
      'economics/public-finance/public-debt/burden',
      'economics/public-finance/public-debt/redemption',
      'economics/public-finance/public-debt',
      'economics/public-finance/deficit-financing'
    ],
    to: '/economics/public-finance/public-debt-and-expenditure/',
    title: 'Public Expenditure and Public Debt: Principles, Burden, and Redemption'
  },
  // Public Finance: Fiscal Federalism & Budget
  {
    from: [
      'economics/public-finance/centre-and-states/revenue-sources',
      'economics/public-finance/centre-and-states/expenditure',
      'economics/public-finance/finance-commission',
      'economics/public-finance/union-budget/components',
      'economics/public-finance/centre-and-states',
      'economics/public-finance/union-budget'
    ],
    to: '/economics/public-finance/fiscal-federalism-and-budget/',
    title: 'Fiscal Federalism: Union-State Financial Relations, Finance Commission, and Union Budget'
  }
];

function updatePgtEconomicsTracker() {
  const filePath = path.join(ROOT, 'up-pgt-economics/index.html');
  let html = fs.readFileSync(filePath, 'utf8');

  for (const map of mapping) {
    let firstFound = false;

    for (const oldSub of map.from) {
      const keySimple = oldSub.replace(/^economics\//, '');
      const escapedSimple = keySimple.replace(/[\/\\^$*+?.()|[\]{}]/g, '\\$&');

      const topicRegex = new RegExp(`<div class="topic" data-key="${escapedSimple}"[\\s\\S]*?class="open-topic"[^>]*?>→<\\/a>\\s*<\\/div>`, 'g');

      if (!firstFound) {
        if (topicRegex.test(html)) {
          firstFound = true;
          const newKey = map.to.replace(/^\/economics\//, '').replace(/\/$/, '');
          const searchAttr = `${map.title.toLowerCase()} ${newKey} economics`;

          html = html.replace(topicRegex, `<div class="topic" data-key="${newKey}" data-search="${searchAttr}">
<label class="check"><input class="topic-check" type="checkbox" aria-label="Mark ${map.title} complete"></label>
<div class="topic-copy"><a class="topic-link" href="${map.to}">${map.title}</a><span class="topic-path">${map.to}</span></div>
<a class="open-topic" href="${map.to}" aria-label="Open ${map.title}">→</a>
</div>`);
        }
      } else {
        html = html.replace(topicRegex, '');
      }
    }
  }

  // Recount topics in each section card
  const secCardRegex = /<article class="section-card" id="([^"]+)"[\s\S]*?<\/article>/g;
  let totalTopics = 0;
  html = html.replace(secCardRegex, (cardMatch, cardId) => {
    const topicCount = (cardMatch.match(/<div class="topic"/g) || []).length;
    totalTopics += topicCount;

    let updatedCard = cardMatch.replace(/<span class="section-meta">\d+ tracked topics<\/span>/, `<span class="section-meta">${topicCount} tracked topics</span>`);
    updatedCard = updatedCard.replace(new RegExp(`(<span data-done="${cardId}">0<\\/span> \\/ )\\d+`), `$1${topicCount}`);
    return updatedCard;
  });

  console.log(`up-pgt-economics new total tracked topics: ${totalTopics}`);

  // Replace overall progress numbers
  html = html.replace(/<span id="doneCount">0<\/span> \/ \d+<br>topics complete/, `<span id="doneCount">0</span> / ${totalTopics}<br>topics complete`);
  html = html.replace(/<strong id="statPending">\d+<\/strong><span>Remaining<\/span>/, `<strong id="statPending">${totalTopics}</strong><span>Remaining</span>`);
  html = html.replace(/<span class="tag">\d+ tracked topics<\/span>/, `<span class="tag">${totalTopics} tracked topics</span>`);

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('Updated up-pgt-economics/index.html successfully.');
}

function updateTgtSocialScienceTracker() {
  const filePath = path.join(ROOT, 'up-tgt-social-science/index.html');
  let html = fs.readFileSync(filePath, 'utf8');

  // Replace any obsolete /economics/... hrefs in TGT Social Science with their consolidated canonical URLs
  for (const map of mapping) {
    for (const oldSub of map.from) {
      const oldUrlRegex = new RegExp(`href="\\/economics\\/${oldSub.replace(/^economics\//, '')}\\/?"`, 'g');
      html = html.replace(oldUrlRegex, `href="${map.to}"`);
    }
  }

  // Also replace any hrefs that were flattened directly
  const directFlattening = [
    { from: '/economics/indian-economy/agriculture-sector/farmers-and-problems/', to: '/economics/indian-economy/agricultural-problems-and-farmers/' },
    { from: '/economics/indian-economy/agriculture-sector/marketing-and-food-security/', to: '/economics/indian-economy/agricultural-marketing-and-food-security/' },
    { from: '/economics/indian-economy/agriculture-sector/rural-development-programmes/', to: '/economics/indian-economy/rural-development-programmes/' },
    { from: '/economics/indian-economy/employment/unemployment-in-india/', to: '/economics/indian-economy/unemployment-in-india/' },
    { from: '/economics/indian-economy/industrial-sector/policy-and-msme/', to: '/economics/indian-economy/industrial-policy-and-msme/' },
    { from: '/economics/indian-economy/population/trends/', to: '/economics/indian-economy/demographic-trends-in-india/' },
    { from: '/economics/macro-economics/trade-cycle/theories/', to: '/economics/macro-economics/trade-cycle-theories/' },
    { from: '/economics/micro-economics/consumer-behaviour/demand-and-utility/', to: '/economics/micro-economics/demand-and-utility/' },
    { from: '/economics/micro-economics/consumer-behaviour/indifference-curve-analysis/', to: '/economics/micro-economics/indifference-curve-analysis/' },
    { from: '/economics/micro-economics/consumer-behaviour/revealed-preference-theory/', to: '/economics/micro-economics/revealed-preference-theory/' },
    { from: '/economics/micro-economics/distribution-theory/theories-of-interest-and-profit/', to: '/economics/micro-economics/theories-of-interest-and-profit/' },
    { from: '/economics/micro-economics/distribution-theory/theories-of-rent-and-wages/', to: '/economics/micro-economics/theories-of-rent-and-wages/' },
    { from: '/economics/micro-economics/production-theory/cost-and-revenue-curves/', to: '/economics/micro-economics/cost-and-revenue-curves/' },
    { from: '/economics/micro-economics/production-theory/production-functions-and-returns/', to: '/economics/micro-economics/production-functions-and-returns/' }
  ];

  for (const df of directFlattening) {
    html = html.replace(new RegExp(df.from.replace(/\//g, '\\/'), 'g'), df.to);
  }

  fs.writeFileSync(filePath, html, 'utf8');
  console.log('Updated up-tgt-social-science/index.html links successfully.');
}

updatePgtEconomicsTracker();
updateTgtSocialScienceTracker();
