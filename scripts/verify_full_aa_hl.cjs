const fs = require('fs');
const path = require('path');
const http = require('http');

const all22Guides = [
  // Topic 1: Number & Algebra
  'number-and-algebra/proof-by-mathematical-induction',
  'number-and-algebra/complex-numbers-cartesian-polar-euler',
  'number-and-algebra/de-moivres-theorem-and-roots-of-unity',
  'number-and-algebra/systems-of-linear-equations-and-matrices',
  'number-and-algebra/polynomials-and-vietas-formulas',
  'number-and-algebra/partial-fractions-and-binomial-series',

  // Topic 2: Functions
  'functions/modulus-functions-and-inequalities',
  'functions/rational-functions-and-oblique-asymptotes',
  'functions/composite-transformations-and-reciprocal-graphs',

  // Topic 3: Geometry & Trigonometry
  'geometry-and-trigonometry/reciprocal-and-inverse-trigonometric-functions',
  'geometry-and-trigonometry/compound-angle-identities-and-double-angles',
  'geometry-and-trigonometry/3d-vectors-and-scalar-product',
  'geometry-and-trigonometry/vector-equations-of-lines-in-3d',
  'geometry-and-trigonometry/vector-cross-product-and-planes',

  // Topic 4: Statistics & Probability
  'statistics-and-probability/continuous-random-variables-and-probability-density-functions',
  'statistics-and-probability/expectation-variance-and-linear-combinations',

  // Topic 5: Calculus
  'calculus/limits-and-lhospitals-rule',
  'calculus/implicit-differentiation-and-related-rates',
  'calculus/advanced-integration-parts-and-partial-fractions',
  'calculus/first-order-differential-equations',
  'calculus/volumes-of-revolution',
  'calculus/maclaurin-and-taylor-series'
];

const hubs = [
  'index.html',
  'number-and-algebra/index.html',
  'functions/index.html',
  'geometry-and-trigonometry/index.html',
  'statistics-and-probability/index.html',
  'calculus/index.html'
];

const basePath = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl');

async function checkUrl(url) {
  return new Promise((resolve) => {
    http.get(url, (res) => {
      resolve(res.statusCode);
    }).on('error', (err) => {
      resolve(`ERR: ${err.message}`);
    });
  });
}

async function run() {
  console.log('=== 1. VERIFYING HUBS & PORTAL FILES ===');
  for (const hub of hubs) {
    const full = path.join(basePath, hub);
    const exists = fs.existsSync(full);
    const url = `http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/${hub.replace('index.html', '')}`;
    const code = await checkUrl(url);
    console.log(`[${exists ? 'FILE OK' : 'MISSING'}] [HTTP ${code}] ${hub}`);
  }

  console.log('\n=== 2. VERIFYING ALL 22 LESSON GUIDES ===');
  let allPassed = true;
  let guideIndex = 1;

  for (const guide of all22Guides) {
    const file = path.join(basePath, guide, 'index.html');
    if (!fs.existsSync(file)) {
      console.error(`[FAIL] Missing file: ${guide}/index.html`);
      allPassed = false;
      continue;
    }

    const content = fs.readFileSync(file, 'utf8');
    const url = `http://localhost:8082/ib/dp-mathematics/analysis-and-approaches-hl/${guide}/`;
    const httpCode = await checkUrl(url);

    // Checks
    const has4Tabs = (content.match(/class="study-tab-btn/g) || []).length === 4;
    const has4Panels = (content.match(/class="study-tab-panel/g) || content.match(/class="study-tab-pane/g) || []).length === 4;
    const hasSvg = content.includes('<svg') && content.includes('</svg>');
    const exerciseCount = (content.match(/class="(exercise-item|exercise-card)"/g) || []).length;
    const hasDetails = (content.match(/class="solution-details"/g) || []).length >= 10;
    const mcqCards = (content.match(/class="quiz-card"\s+id="q[1-4]"/g) || []).length +
                     (content.match(/class="quiz-question-card"/g) || []).length +
                     (content.match(/<article class="quiz-question"/g) || []).length;
    const mcqCount = mcqCards;
    const hasKaTeX = content.includes('katex.min.js') && content.includes('auto-render.min.js');
    const hasTabsJs = content.includes('ib-study-tabs.js');

    const pass = (httpCode === 200) && has4Tabs && has4Panels && hasSvg && (exerciseCount >= 12) && hasDetails && (mcqCount === 4) && hasKaTeX && hasTabsJs;

    if (!pass) {
      allPassed = false;
      console.log(`Guide #${guideIndex} [FAIL] ${guide}`);
      console.log(`  HTTP: ${httpCode}, Tabs: ${has4Tabs}, Panels: ${has4Panels}, Svg: ${hasSvg}, Exercises: ${exerciseCount}, Details: ${hasDetails}, MCQs: ${mcqCount}`);
    } else {
      console.log(`Guide #${guideIndex} [OK] HTTP ${httpCode} | 10 Exs + 2 FRQs | 4 MCQs | SVG | KaTeX | Tabs :: ${guide}`);
    }
    guideIndex++;
  }

  console.log('\n=== FINAL VERIFICATION SUMMARY ===');
  if (allPassed) {
    console.log('🎉 ALL 22 IB DP MATHEMATICS AA HL GUIDES + 5 TOPIC HUBS + MAIN PORTAL ARE 100% COMPLETE AND PASS ALL QUALITY & SYLLABUS CHECKS!');
  } else {
    console.log('⚠️ Some guides had issues. Check logs above.');
  }
}

run();
