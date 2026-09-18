const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const replacements = [
  // 1. Business Organization: Introduction and Scope
  {
    from: [
      'business-organization/meaning-and-nature-of-trade-and-commerce',
      'business-organization/industry',
      'business-organization/features-and-scope-of-business-organization'
    ],
    toKey: 'business-organization/introduction-and-scope',
    toPath: '/commerce/business-organization/introduction-and-scope/',
    toTitle: 'Business Organization: Meaning, Nature of Trade, Commerce, and Industry'
  },
  // 2. Company Accounts: Depreciation
  {
    from: [
      'company-accounts/depreciation/methods-of-depreciation',
      'company-accounts/depreciation'
    ],
    toKey: 'company-accounts/depreciation',
    toPath: '/commerce/company-accounts/depreciation/',
    toTitle: 'Depreciation Accounting: Concepts, Causes, and Methods'
  },
  // 3. Business Economics: Nature and Scope
  {
    from: [
      'business-economics/definition-and-scope-of-economics',
      'business-economics/nature-and-scope-of-economics',
      'business-economics/relationship-between-trade-and-economics'
    ],
    toKey: 'business-economics/nature-and-scope',
    toPath: '/commerce/business-economics/nature-and-scope/',
    toTitle: 'Business Economics: Definition, Nature, Scope, and Trade Relations'
  },
  // 4. Business Economics: Market Structures and Price Determination
  {
    from: [
      'business-economics/market-and-price/perfect-competition',
      'business-economics/market-and-price/monopoly',
      'business-economics/market-and-price/price-determination'
    ],
    toKey: 'business-economics/market-structures-and-price',
    toPath: '/commerce/business-economics/market-structures-and-price/',
    toTitle: 'Market Structures: Perfect Competition, Monopoly, and Price Determination'
  },
  // 5. Business Economics: Trade Cycles and Population
  {
    from: [
      'business-economics/macroeconomics/trade-cycle',
      'business-economics/macroeconomics/population-theory',
      'business-economics/macroeconomics/trade-cycles-and-population'
    ],
    toKey: 'business-economics/trade-cycles-and-population',
    toPath: '/commerce/business-economics/trade-cycles-and-population/',
    toTitle: 'Macroeconomics: Trade Cycles and Demographic Theory'
  },
  // 6. Management: Functions of Management
  {
    from: [
      'management/functions-of-management/planning',
      'management/functions-of-management/organization',
      'management/functions-of-management/staffing',
      'management/functions-of-management/direction',
      'management/functions-of-management/motivation',
      'management/functions-of-management/coordination',
      'management/functions-of-management/control'
    ],
    toKey: 'management/functions-of-management',
    toPath: '/commerce/management/functions-of-management/',
    toTitle: 'Functions of Management: Planning, Organizing, Staffing, Directing, and Controlling'
  },
  // 7. Management Thought: Schools and Theorists
  {
    from: [
      'management-thought/fw-taylor',
      'management-thought/henry-fayol',
      'management-thought/elton-mayo',
      'management-thought/schools-of-management-thought'
    ],
    toKey: 'management-thought/schools-and-theorists',
    toPath: '/commerce/management-thought/schools-and-theorists/',
    toTitle: 'Evolution of Management Thought: Scientific, Administrative, and Human Relations'
  },
  // 8. Marketing: Nature and Functions
  {
    from: [
      'marketing/meaning-and-nature-of-marketing',
      'marketing/functions-of-marketing'
    ],
    toKey: 'marketing/nature-and-functions',
    toPath: '/commerce/marketing/nature-and-functions/',
    toTitle: 'Marketing: Meaning, Nature, Scope, Functions, and Marketing Mix'
  },
  // 9. Trade: Internal and International Trade
  {
    from: [
      'trade/domestic-trade',
      'trade/foreign-trade'
    ],
    toKey: 'trade/internal-and-international-trade',
    toPath: '/commerce/trade/internal-and-international-trade/',
    toTitle: 'Trade: Internal Trade (Wholesale & Retail) and International Trade'
  },
  // 10. Money & Banking: Theories of Money and Inflation
  {
    from: [
      'money-and-banking/money/greshams-law',
      'money-and-banking/money/quantity-theory-of-money',
      'money-and-banking/money/inflation',
      'money-and-banking/money/price-indices'
    ],
    toKey: 'money-and-banking/theories-of-money-and-inflation',
    toPath: '/commerce/money-and-banking/theories-of-money-and-inflation/',
    toTitle: 'Monetary Economics: Quantity Theory of Money, Gresham\'s Law, and Inflation'
  },
  // 11. Motivation and Leadership
  {
    from: [
      'motivation-and-leadership/leadership',
      'motivation-and-leadership/principles-of-motivation'
    ],
    toKey: 'motivation-and-leadership/principles-and-theories',
    toPath: '/commerce/motivation-and-leadership/principles-and-theories/',
    toTitle: 'Organizational Behavior: Motivation Theories and Leadership Styles'
  },
  // 12. Statistics: Dispersion and Skewness
  {
    from: [
      'statistics/dispersion/measures-of-dispersion',
      'statistics/dispersion/skewness'
    ],
    toKey: 'statistics/dispersion-and-skewness',
    toPath: '/commerce/statistics/dispersion-and-skewness/',
    toTitle: 'Measures of Dispersion and Skewness'
  },
  // 13. Statistics: Time Series Analysis
  {
    from: [
      'statistics/time-series/analysis-of-time-series'
    ],
    toKey: 'statistics/time-series-analysis',
    toPath: '/commerce/statistics/time-series-analysis/',
    toTitle: 'Time Series Analysis: Components, Moving Averages, and Trend'
  }
];

function updateTrackerFile(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  for (const rep of replacements) {
    let firstFound = false;

    for (const oldSub of rep.from) {
      const escaped = oldSub.replace(/[\/\\^$*+?.()|[\]{}]/g, '\\$&');
      const topicRegex = new RegExp(`<div class="topic" data-key="${escaped}"[\\s\\S]*?class="open-link"[^>]*?>→<\\/a><\\/div>`, 'g');

      if (!firstFound) {
        if (topicRegex.test(html)) {
          firstFound = true;
          html = html.replace(topicRegex, (match) => {
            const tagMatch = match.match(/<span class="exam-tag[^"]*">([^<]+)<\/span>/);
            const tagClass = match.match(/class="exam-tag ([^"]+)"/);
            const familyMatch = match.match(/<span class="family-tag">([^<]+)<\/span>/);

            let tagsHtml = '';
            if (tagMatch) {
              tagsHtml += `<span class="exam-tag ${tagClass ? tagClass[1] : 'shared'}">${tagMatch[1]}</span>`;
            }
            if (familyMatch) {
              tagsHtml += `<span class="family-tag">${familyMatch[1]}</span>`;
            }

            const searchAttr = `${rep.toTitle.toLowerCase()} ${rep.toKey} commerce`;

            return `<div class="topic" data-key="${rep.toKey}" data-relevance="shared" data-search="${searchAttr}">
<label class="check-wrap"><input class="topic-check" type="checkbox" aria-label="Mark ${rep.toTitle} complete"></label>
<div class="topic-main"><a class="topic-link" href="${rep.toPath}">${rep.toTitle}</a><div class="topic-tags">${tagsHtml}</div></div>
<a class="open-link" href="${rep.toPath}" aria-label="Open ${rep.toTitle}">→</a></div>`;
          });
        }
      } else {
        html = html.replace(topicRegex, '');
      }
    }
  }

  // Recount topics in each section card
  const secCardRegex = /<article class="section-card[^"]*" id="([^"]+)"[\s\S]*?<\/article>/g;
  let totalTopics = 0;
  html = html.replace(secCardRegex, (cardMatch, cardId) => {
    const topicCount = (cardMatch.match(/<div class="topic"/g) || []).length;
    totalTopics += topicCount;

    let updatedCard = cardMatch.replace(/<span class="section-desc">\d+ syllabus topics<\/span>/, `<span class="section-desc">${topicCount} syllabus topics</span>`);
    updatedCard = updatedCard.replace(new RegExp(`(<small><span data-section-done="${cardId}">0<\\/span> \\/ )\\d+(<\\/small>)`), `$1${topicCount}$2`);
    return updatedCard;
  });

  console.log(`${path.basename(filePath)} new total topics: ${totalTopics}`);

  // Replace overall progress numbers
  html = html.replace(/<span id="completedCount">0<\/span> \/ \d+<br>topics complete/, `<span id="completedCount">0</span> / ${totalTopics}<br>topics complete`);
  html = html.replace(/<strong id="pendingStat">\d+<\/strong><span>Remaining<\/span>/, `<strong id="pendingStat">${totalTopics}</strong><span>Remaining</span>`);
  html = html.replace(/<div class="metric"><strong>\d+<\/strong><span>Total tracked topics<\/span><\/div>/, `<div class="metric"><strong>${totalTopics}</strong><span>Total tracked topics</span></div>`);
  html = html.replace(/<span class="tag">\d+ Tracked Topics<\/span>/, `<span class="tag">${totalTopics} Tracked Topics</span>`);

  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`Updated ${path.basename(filePath)} successfully.`);
}

updateTrackerFile(path.join(ROOT, 'up-tgt-commerce/index.html'));
updateTrackerFile(path.join(ROOT, 'up-pgt-commerce/index.html'));
