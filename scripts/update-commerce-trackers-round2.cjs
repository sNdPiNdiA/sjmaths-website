const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

const replacements = [
  // 1. Auditing Foundations
  {
    from: [
      'auditing/definition-of-auditing',
      'auditing/objectives-of-auditing',
      'auditing/significance-of-auditing'
    ],
    toKey: 'auditing/meaning-objectives-and-significance',
    toPath: '/commerce/auditing/meaning-objectives-and-significance/',
    toTitle: 'Auditing: Meaning, Objectives, and Significance'
  },
  // 2. Books of Original Entry & Ledger
  {
    from: [
      'accounting-fundamentals/journal',
      'accounting-fundamentals/ledger',
      'accounting-fundamentals/trial-balance'
    ],
    toKey: 'accounting-fundamentals/books-of-original-entry-and-ledger',
    toPath: '/commerce/accounting-fundamentals/books-of-original-entry-and-ledger/',
    toTitle: 'Books of Original Entry: Journal, Ledger, and Trial Balance'
  },
  // 3. Accounting Principles & Double Entry
  {
    from: [
      'accounting-fundamentals/accounting-concepts-and-conventions',
      'accounting-fundamentals/double-entry-system'
    ],
    toKey: 'accounting-fundamentals/principles-and-double-entry',
    toPath: '/commerce/accounting-fundamentals/principles-and-double-entry/',
    toTitle: 'Accounting Concepts, Conventions, and Double Entry System'
  },
  // 4. Business Environment Dimensions
  {
    from: [
      'business-environment/economic-environment',
      'business-environment/social-environment',
      'business-environment/cultural-environment',
      'business-environment/political-environment'
    ],
    toKey: 'business-environment/dimensions-of-business-environment',
    toPath: '/commerce/business-environment/dimensions-of-business-environment/',
    toTitle: 'Dimensions of Business Environment: Economic, Social, Cultural, and Political'
  },
  // 5. Forms of Business Organization
  {
    from: [
      'business-organization/forms-of-business-organization',
      'business-organization/sole-proprietorship',
      'business-organization/partnership',
      'business-organization/company'
    ],
    toKey: 'business-organization/forms-of-business-organization',
    toPath: '/commerce/business-organization/forms-of-business-organization/',
    toTitle: 'Forms of Business Organization: Sole Proprietorship, Partnership, and Company'
  },
  // 6. Commercial Banking
  {
    from: [
      'money-and-banking/banking/commercial-banks',
      'money-and-banking/banking/functions-of-commercial-banks',
      'money-and-banking/banking/types-of-banks'
    ],
    toKey: 'money-and-banking/commercial-banking',
    toPath: '/commerce/money-and-banking/commercial-banking/',
    toTitle: 'Commercial Banking: Functions, Structure, and Types of Banks'
  },
  // 7. International Financial Institutions
  {
    from: [
      'money-and-banking/international-financial-institutions/international-monetary-fund',
      'money-and-banking/international-financial-institutions/world-bank'
    ],
    toKey: 'money-and-banking/international-financial-institutions',
    toPath: '/commerce/money-and-banking/international-financial-institutions/',
    toTitle: 'International Financial Institutions: IMF and World Bank Group'
  },
  // 8. Demand Analysis
  {
    from: [
      'business-economics/demand/law-of-demand',
      'business-economics/demand/elasticity-of-demand'
    ],
    toKey: 'business-economics/demand-analysis',
    toPath: '/commerce/business-economics/demand-analysis/',
    toTitle: 'Demand Analysis: Law of Demand and Elasticity of Demand'
  },
  // 9. Production Theory
  {
    from: [
      'business-economics/production/production-function',
      'business-economics/production/laws-of-production',
      'business-economics/production/laws-of-returns'
    ],
    toKey: 'business-economics/production-theory',
    toPath: '/commerce/business-economics/production-theory/',
    toTitle: 'Theory of Production: Production Function and Laws of Returns'
  },
  // 10. National Income & GDP
  {
    from: [
      'business-economics/macroeconomics/national-income',
      'business-economics/macroeconomics/gross-domestic-product'
    ],
    toKey: 'business-economics/national-income-and-gdp',
    toPath: '/commerce/business-economics/national-income-and-gdp/',
    toTitle: 'Macroeconomics: National Income, GDP, and Economic Aggregates'
  },
  // 11. Cost Accounting Introduction & Elements
  {
    from: [
      'cost-accounting/meaning-and-objectives-of-cost-accounting',
      'cost-accounting/elements-of-cost',
      'cost-accounting/methods-of-cost-accounting'
    ],
    toKey: 'cost-accounting/introduction-and-elements',
    toPath: '/commerce/cost-accounting/introduction-and-elements/',
    toTitle: 'Cost Accounting: Meaning, Objectives, Elements, and Methods'
  },
  // 12. Statistical Data Presentation
  {
    from: [
      'statistics/data-collection',
      'statistics/data-classification',
      'statistics/tabulation',
      'statistics/frequency'
    ],
    toKey: 'statistics/collection-and-presentation-of-data',
    toPath: '/commerce/statistics/collection-and-presentation-of-data/',
    toTitle: 'Collection, Classification, and Tabulation of Statistical Data'
  },
  // 13. Official Statistics of India
  {
    from: [
      'statistics/india-statistics/agriculture-statistics',
      'statistics/india-statistics/industrial-statistics',
      'statistics/india-statistics/population-statistics'
    ],
    toKey: 'statistics/indian-statistics',
    toPath: '/commerce/statistics/indian-statistics/',
    toTitle: 'Official Statistics of India: Agriculture, Industry, and Population'
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
