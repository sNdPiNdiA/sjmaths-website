const http = require('http');

const branches = [
  {
    name: 'Number',
    slug: 'number',
    lessons: [
      'number-systems',
      'forms-of-number',
      'integer-exponents',
      'fractional-exponents-and-radicals',
      'logarithms',
      'number-sequences',
      'ratio-and-percentage',
      'sets-and-venn-diagrams'
    ]
  },
  {
    name: 'Algebra',
    slug: 'algebra',
    lessons: [
      'algebraic-expressions',
      'linear-equations-and-inequalities',
      'quadratic-functions',
      'exponential-functions',
      'systems-of-equations',
      'functions-and-transformations',
      'polynomials',
      'sequences-and-series'
    ]
  },
  {
    name: 'Geometry & Trigonometry',
    slug: 'geometry-and-trigonometry',
    lessons: [
      'triangle-properties-and-pythagoras',
      'trigonometric-ratios',
      'sine-and-cosine-rules',
      'radians-and-unit-circle',
      'circle-geometry',
      'perimeter-area-and-volume',
      'vectors',
      'transformations-and-coordinates'
    ]
  },
  {
    name: 'Statistics & Probability',
    slug: 'statistics-and-probability',
    lessons: [
      'data-collection-and-presentation',
      'graphical-data-representation',
      'measures-of-central-tendency',
      'measures-of-spread',
      'population-and-sampling',
      'probability',
      'conditional-probability',
      'correlation-and-regression'
    ]
  }
];

function fetchUrl(url) {
  return new Promise((resolve) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        resolve({ status: res.statusCode, body: data });
      });
    }).on('error', (err) => {
      resolve({ error: err.message, status: 0 });
    });
  });
}

async function verifyHub(branch) {
  const url = `http://localhost:8082/ib/myp-mathematics/${branch.slug}/`;
  const res = await fetchUrl(url);
  if (res.status !== 200) {
    return { ok: false, msg: `Hub status ${res.status}` };
  }
  const hasUnavailable = res.body.includes('data-unavailable-href') || res.body.includes('(not yet available)');
  if (hasUnavailable) {
    return { ok: false, msg: `Hub still has unavailable link placeholders` };
  }
  return { ok: true, msg: 'Hub 200 OK & 0 unavailable placeholders' };
}

async function verifyLesson(branchSlug, lessonSlug) {
  const url = `http://localhost:8082/ib/myp-mathematics/${branchSlug}/${lessonSlug}/`;
  const res = await fetchUrl(url);
  if (res.status !== 200) {
    return { ok: false, msg: `Status ${res.status}` };
  }
  const body = res.body;
  const hasNav = body.includes('study-tabs-nav');
  const hasTabNotes = body.includes('tab-notes') || body.includes('tab-study-notes');
  const hasTabPractice = body.includes('tab-practice') || body.includes('tab-exercises');
  const hasTabFormula = body.includes('tab-formula') || body.includes('tab-formulas');
  const hasTabTest = body.includes('tab-test') || body.includes('tab-quiz');
  
  const exercises = (body.match(/class="exercise-card"/g) || []).length;
  const quizzes = (body.match(/class="quiz-card"/g) || []).length;
  const hasMethodMarks = body.includes('[M1]') || body.includes('[A1]');
  const hasCriteria = body.includes('Criterion A') || body.includes('Criteria');

  const ok = hasNav && hasTabNotes && hasTabPractice && hasTabFormula && hasTabTest &&
             exercises === 10 && quizzes === 5 && hasMethodMarks && hasCriteria;

  return {
    ok,
    exercises,
    quizzes,
    hasTabs: hasNav && hasTabNotes && hasTabPractice && hasTabFormula && hasTabTest,
    hasMethodMarks,
    hasCriteria
  };
}

async function main() {
  console.log('========================================================');
  console.log('       MASTER AUDIT: ALL 32 IB MYP LESSONS & HUBS       ');
  console.log('========================================================\n');

  let totalLessons = 0;
  let passedLessons = 0;
  let hubFails = 0;

  for (const b of branches) {
    console.log(`\n--- [Branch: ${b.name}] ---`);
    const hubRes = await verifyHub(b);
    if (hubRes.ok) {
      console.log(`  [HUB PASS] ${b.slug}/ -> ${hubRes.msg}`);
    } else {
      console.log(`  [HUB FAIL] ${b.slug}/ -> ${hubRes.msg}`);
      hubFails++;
    }

    for (const slug of b.lessons) {
      totalLessons++;
      const lRes = await verifyLesson(b.slug, slug);
      if (lRes.ok) {
        passedLessons++;
        console.log(`  [LESSON PASS] ${slug} (10 Ex, 5 Quiz, 4 Tabs, Marks: OK, Criteria: OK)`);
      } else {
        console.log(`  [LESSON FAIL] ${slug} ->`, lRes);
      }
    }
  }

  console.log('\n========================================================');
  console.log(`SUMMARY: ${passedLessons}/${totalLessons} Lessons Passed.`);
  console.log(`Branch Hubs with issues: ${hubFails}`);
  console.log('========================================================\n');

  if (passedLessons === 32 && hubFails === 0) {
    console.log('ALL 32 IB MYP LESSONS & ALL 4 BRANCH HUBS ARE 100% VERIFIED!');
    process.exit(0);
  } else {
    process.exit(1);
  }
}

main();
