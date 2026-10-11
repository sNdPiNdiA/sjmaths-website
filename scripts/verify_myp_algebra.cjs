const http = require('http');
const fs = require('fs');
const path = require('path');

const baseUrl = 'http://localhost:8082';

const topics = [
  '/ib/myp-mathematics/algebra/',
  '/ib/myp-mathematics/algebra/algebraic-expressions/',
  '/ib/myp-mathematics/algebra/linear-equations-and-inequalities/',
  '/ib/myp-mathematics/algebra/quadratic-functions/',
  '/ib/myp-mathematics/algebra/exponential-functions/',
  '/ib/myp-mathematics/algebra/systems-of-equations/',
  '/ib/myp-mathematics/algebra/functions-and-transformations/',
  '/ib/myp-mathematics/algebra/polynomials/',
  '/ib/myp-mathematics/algebra/sequences-and-series/'
];

function fetchUrl(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ status: res.statusCode, data }));
    }).on('error', reject);
  });
}

async function run() {
  console.log('Testing MYP Algebra pages on ' + baseUrl + '...\n');
  let allPassed = true;

  for (const topic of topics) {
    try {
      const res = await fetchUrl(baseUrl + topic);
      if (res.status !== 200) {
        console.error(`❌ [${res.status}] ${topic}`);
        allPassed = false;
        continue;
      }

      if (topic === '/ib/myp-mathematics/algebra/') {
        const hasUnavailable = res.data.includes('not yet available');
        if (hasUnavailable) {
          console.error(`❌ Hub contains 'not yet available' placeholders!`);
          allPassed = false;
        } else {
          console.log(`✅ [200] Hub: All 8 topic cards active`);
        }
      } else {
        const hasTabs = res.data.includes('tab-notes') && res.data.includes('tab-practice') && res.data.includes('tab-formulas') && res.data.includes('tab-test');
        const exerciseCount = (res.data.match(/class="exercise-card"/g) || []).length;
        const quizCount = (res.data.match(/class="quiz-card"/g) || []).length;
        const detailsCount = (res.data.match(/class="solution-details"/g) || []).length;

        if (hasTabs && exerciseCount === 10 && quizCount === 5 && detailsCount === 10) {
          console.log(`✅ [200] ${topic} -> 4 Tabs, ${exerciseCount} Exercises with Solutions, ${quizCount} Quiz Questions`);
        } else {
          console.error(`❌ ${topic} FAILED verification: tabs=${hasTabs}, exercises=${exerciseCount}, quiz=${quizCount}, details=${detailsCount}`);
          allPassed = false;
        }
      }
    } catch (err) {
      console.error(`❌ Error fetching ${topic}:`, err.message);
      allPassed = false;
    }
  }

  if (allPassed) {
    console.log('\n🎉 ALL 8 MYP ALGEBRA LESSONS & HUB FULLY VERIFIED (100% PASS)!');
  } else {
    process.exit(1);
  }
}

run();
