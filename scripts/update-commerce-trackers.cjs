const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');

// Map of deleted/consolidated paths -> new canonical path & new title
const replacements = [
  // 1. Entrepreneurship
  {
    from: [
      'entrepreneurship/meaning-of-entrepreneurship',
      'entrepreneurship/definition-of-entrepreneurship',
      'entrepreneurship/nature-of-entrepreneurship',
      'entrepreneurship/importance-of-entrepreneurship'
    ],
    toKey: 'entrepreneurship',
    toPath: '/commerce/entrepreneurship/',
    toTitle: 'Entrepreneurship: Meaning, Nature, Scope & Importance'
  },
  // 2. Consumer Protection
  {
    from: [
      'consumer-protection/meaning-of-consumer-protection',
      'consumer-protection/importance-of-consumer-protection',
      'consumer-protection/consumer-protection-act-2019'
    ],
    toKey: 'consumer-protection',
    toPath: '/commerce/consumer-protection/',
    toTitle: 'Consumer Protection and Consumer Protection Act 2019'
  },
  // 3. Management Foundations
  {
    from: [
      'management/meaning-and-definition-of-management',
      'management/nature-of-management',
      'management/scope-of-management',
      'management/principles-of-management'
    ],
    toKey: 'management/principles-and-foundations',
    toPath: '/commerce/management/principles-and-foundations/',
    toTitle: 'Management: Meaning, Nature, Scope and Principles'
  },
  // 4. Management Accounting Foundations
  {
    from: [
      'management-accounting/meaning-of-management-accounting',
      'management-accounting/objectives-of-management-accounting',
      'management-accounting/functions-of-management-accounting',
      'management-accounting/scope-of-management-accounting',
      'management-accounting/importance-of-management-accounting',
      'management-accounting/management-accounting-vs-financial-accounting'
    ],
    toKey: 'management-accounting/nature-and-scope',
    toPath: '/commerce/management-accounting/nature-and-scope/',
    toTitle: 'Management Accounting: Meaning, Objectives, Scope and Functions'
  },
  // 5. Auditing — Vouching
  {
    from: [
      'auditing/vouching/meaning-of-vouching',
      'auditing/vouching/significance-of-vouching',
      'auditing/vouching/types-of-vouching',
      'auditing/vouching/vouching-of-initial-books'
    ],
    toKey: 'auditing/vouching',
    toPath: '/commerce/auditing/vouching/',
    toTitle: 'Vouching: Meaning, Significance, Types and Techniques'
  },
  // 6. Auditing — Valuation and Verification
  {
    from: [
      'auditing/valuation-and-verification/valuation-of-assets',
      'auditing/valuation-and-verification/verification-of-assets'
    ],
    toKey: 'auditing/valuation-and-verification',
    toPath: '/commerce/auditing/valuation-and-verification/',
    toTitle: 'Verification and Valuation of Assets and Liabilities'
  },
  // 7. Final Accounts
  {
    from: [
      'final-accounts/final-accounts',
      'final-accounts/adjustment-entries',
      'final-accounts/final-accounts-with-adjustments'
    ],
    toKey: 'final-accounts',
    toPath: '/commerce/final-accounts/',
    toTitle: 'Final Accounts: Preparation, Adjustments and Closing Entries'
  },
  // 8. Company Accounts — Shares
  {
    from: [
      'company-accounts/shares/types-of-shares',
      'company-accounts/shares/issue-of-shares',
      'company-accounts/shares/forfeiture-of-shares',
      'company-accounts/shares/reissue-of-forfeited-shares'
    ],
    toKey: 'company-accounts/shares',
    toPath: '/commerce/company-accounts/shares/',
    toTitle: 'Share Capital: Types, Issue, Forfeiture and Reissue of Shares'
  },
  // 9. Company Accounts — Debentures
  {
    from: [
      'company-accounts/debentures/issue-of-debentures',
      'company-accounts/debentures/redemption-of-debentures'
    ],
    toKey: 'company-accounts/debentures',
    toPath: '/commerce/company-accounts/debentures/',
    toTitle: 'Debentures: Issue, Accounting and Redemption Methods'
  },
  // 10. Partnership Accounts — Retirement & Death
  {
    from: [
      'partnership-accounts/retirement-of-partner',
      'partnership-accounts/death-of-partner'
    ],
    toKey: 'partnership-accounts/retirement-and-death',
    toPath: '/commerce/partnership-accounts/retirement-and-death/',
    toTitle: 'Partnership Accounts: Retirement and Death of a Partner'
  },
  // 11. Taxation — Basic Concepts
  {
    from: [
      'taxation/assessee',
      'taxation/assessment-year',
      'taxation/previous-year',
      'taxation/important-taxation-definitions',
      'taxation/tax-liability'
    ],
    toKey: 'taxation/basic-concepts',
    toPath: '/commerce/taxation/basic-concepts/',
    toTitle: 'Income Tax: Basic Concepts, Assessee, Assessment Year and Tax Liability'
  },
  // 12. Business Economics — Utility Analysis
  {
    from: [
      'business-economics/utility/total-utility',
      'business-economics/utility/marginal-utility',
      'business-economics/utility/law-of-marginal-utility'
    ],
    toKey: 'business-economics/utility-analysis',
    toPath: '/commerce/business-economics/utility-analysis/',
    toTitle: 'Utility Analysis: Total, Marginal and Law of Diminishing Marginal Utility'
  },
  // 13. Business Economics — Cost Concepts
  {
    from: [
      'business-economics/cost/average-cost',
      'business-economics/cost/marginal-cost'
    ],
    toKey: 'business-economics/cost-concepts',
    toPath: '/commerce/business-economics/cost-concepts/',
    toTitle: 'Cost Concepts and Cost Curves: Average Cost and Marginal Cost'
  },
  // 14. Statistics — Central Tendency
  {
    from: [
      'statistics/central-tendency/mean',
      'statistics/central-tendency/median',
      'statistics/central-tendency/mode'
    ],
    toKey: 'statistics/measures-of-central-tendency',
    toPath: '/commerce/statistics/measures-of-central-tendency/',
    toTitle: 'Measures of Central Tendency: Mean, Median and Mode'
  },
  // 15. Statistics — Correlation & Regression
  {
    from: [
      'statistics/correlation-and-regression/correlation',
      'statistics/correlation-and-regression/regression'
    ],
    toKey: 'statistics/correlation-and-regression',
    toPath: '/commerce/statistics/correlation-and-regression/',
    toTitle: 'Correlation and Regression Analysis'
  },
  // 16. Statistics — Theoretical Distributions
  {
    from: [
      'statistics/frequency-distributions/binomial-distribution',
      'statistics/frequency-distributions/poisson-distribution',
      'statistics/frequency-distributions/normal-distribution'
    ],
    toKey: 'statistics/theoretical-probability-distributions',
    toPath: '/commerce/statistics/theoretical-probability-distributions/',
    toTitle: 'Theoretical Probability Distributions: Binomial, Poisson and Normal'
  },
  // 17. Money & Banking — Money Concepts
  {
    from: [
      'money-and-banking/money/definition-and-scope-of-money',
      'money-and-banking/money/functions-of-money',
      'money-and-banking/money/importance-of-money',
      'money-and-banking/money/types-of-money'
    ],
    toKey: 'money-and-banking/money-concepts',
    toPath: '/commerce/money-and-banking/money-concepts/',
    toTitle: 'Money: Meaning, Functions, Types and Importance'
  },
  // 18. Money & Banking — Digital Banking
  {
    from: [
      'money-and-banking/banking/e-banking',
      'money-and-banking/banking/digital-banking'
    ],
    toKey: 'money-and-banking/digital-banking',
    toPath: '/commerce/money-and-banking/digital-banking/',
    toTitle: 'Digital Banking and E-Banking: Systems, Services and Security'
  },
  // 19. Money & Banking — Reserve Bank of India
  {
    from: [
      'money-and-banking/banking/reserve-bank-of-india',
      'money-and-banking/banking/functions-of-rbi'
    ],
    toKey: 'money-and-banking/reserve-bank-of-india',
    toPath: '/commerce/money-and-banking/reserve-bank-of-india/',
    toTitle: 'Reserve Bank of India: Organization, Monetary Policy and Functions'
  }
];

function updateTrackerFile(filePath, isPgt) {
  let html = fs.readFileSync(filePath, 'utf8');

  for (const rep of replacements) {
    // For each cluster of 'from' keys:
    // Keep the FIRST occurrence and convert it to toKey, toPath, toTitle
    // Remove subsequent occurrences in the tracker
    let firstFound = false;

    for (const oldSub of rep.from) {
      // Find the topic block matching data-key="...oldSub..."
      // Regex for topic block: <div class="topic" data-key="...oldSub..."[\s\S]*?<\/div>\s*<a class="open-link"[\s\S]*?<\/a><\/div>
      const escaped = oldSub.replace(/[\/\\^$*+?.()|[\]{}]/g, '\\$&');
      const topicRegex = new RegExp(`<div class="topic" data-key="${escaped}"[\\s\\S]*?class="open-link"[^>]*?>→<\\/a><\\/div>`, 'g');

      if (!firstFound) {
        // Replace first occurrence with consolidated topic markup
        if (topicRegex.test(html)) {
          firstFound = true;
          html = html.replace(topicRegex, (match) => {
            // Keep exam-tag and family-tag if present
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
        // Subsequent occurrences of the cluster get removed from the tracker
        html = html.replace(topicRegex, '');
      }
    }
  }

  // Update section topic counts and overall counts in the tracker
  // Recount topics in each section card
  const secCardRegex = /<article class="section-card[^"]*" id="([^"]+)"[\s\S]*?<\/article>/g;
  let totalTopics = 0;
  html = html.replace(secCardRegex, (cardMatch, cardId) => {
    const topicCount = (cardMatch.match(/<div class="topic"/g) || []).length;
    totalTopics += topicCount;

    // Replace <span class="section-desc">... syllabus topics</span>
    let updatedCard = cardMatch.replace(/<span class="section-desc">\d+ syllabus topics<\/span>/, `<span class="section-desc">${topicCount} syllabus topics</span>`);
    // Replace <small><span data-section-done="...">0</span> / \d+</small>
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

updateTrackerFile(path.join(ROOT, 'up-tgt-commerce/index.html'), false);
updateTrackerFile(path.join(ROOT, 'up-pgt-commerce/index.html'), true);
