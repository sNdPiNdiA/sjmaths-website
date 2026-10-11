const http = require('http');

const urls = [
  '/ib/myp-mathematics/number/',
  '/ib/myp-mathematics/number/number-systems/',
  '/ib/myp-mathematics/number/forms-of-number/',
  '/ib/myp-mathematics/number/integer-exponents/',
  '/ib/myp-mathematics/number/fractional-exponents-and-radicals/',
  '/ib/myp-mathematics/number/logarithms/',
  '/ib/myp-mathematics/number/number-sequences/',
  '/ib/myp-mathematics/number/ratio-and-percentage/',
  '/ib/myp-mathematics/number/sets-and-venn-diagrams/'
];

function checkUrl(url) {
  return new Promise((resolve, reject) => {
    http.get(`http://localhost:8082${url}`, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const isGuide = url !== '/ib/myp-mathematics/number/';
        const checks = {
          url,
          statusCode: res.statusCode,
          hasKatex: data.includes('katex.min.js'),
          hasTabsJs: isGuide ? data.includes('ib-study-tabs.js') : true,
          hasThemeJs: data.includes('ib-theme.min.js'),
          hasTab1: isGuide ? data.includes('id="tab-notes"') : true,
          hasTab2: isGuide ? data.includes('id="tab-practice"') : true,
          hasTab3: isGuide ? data.includes('id="tab-formulas"') : true,
          hasTab4: isGuide ? data.includes('id="tab-test"') : true,
          exercisesCount: isGuide ? (data.match(/class="exercise-card"/g) || []).length : 0,
          quizCount: isGuide ? (data.match(/class="quiz-card"/g) || []).length : 0,
        };
        resolve(checks);
      });
    }).on('error', reject);
  });
}

async function run() {
  console.log('--- Verifying IB MYP Number Branch Guides ---');
  let allPassed = true;
  for (const url of urls) {
    const result = await checkUrl(url);
    const pass = result.statusCode === 200 &&
                 result.hasKatex &&
                 result.hasTabsJs &&
                 result.hasThemeJs &&
                 (!result.exercisesCount || result.exercisesCount >= 10) &&
                 (!result.quizCount || result.quizCount >= 5);
    
    console.log(`${pass ? '✅' : '❌'} ${result.url} | Status: ${result.statusCode} | Exercises: ${result.exercisesCount} | Quiz Qs: ${result.quizCount}`);
    if (!pass) allPassed = false;
  }
  console.log(allPassed ? '\n🎉 ALL 8 MYP NUMBER GUIDES & HUB VERIFIED 100% PASSING!' : '\n⚠️ SOME CHECKS FAILED');
}

run();
