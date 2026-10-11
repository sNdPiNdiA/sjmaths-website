const http = require('http');

const lessons = [
  'data-collection-and-presentation',
  'graphical-data-representation',
  'measures-of-central-tendency',
  'measures-of-spread',
  'population-and-sampling',
  'probability',
  'conditional-probability',
  'correlation-and-regression'
];

async function checkLesson(slug) {
  const url = `http://localhost:8082/ib/myp-mathematics/statistics-and-probability/${slug}/`;
  return new Promise((resolve) => {
    http.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const hasTabs = data.includes('study-tabs-nav') && (data.includes('tab-notes') || data.includes('tab-study-notes')) && (data.includes('tab-practice') || data.includes('tab-exercises'));
        const exercisesCount = (data.match(/class="exercise-card"/g) || []).length;
        const quizCount = (data.match(/class="quiz-card"/g) || []).length;
        resolve({
          slug,
          status: res.statusCode,
          hasTabs,
          exercisesCount,
          quizCount
        });
      });
    }).on('error', (err) => {
      resolve({ slug, error: err.message });
    });
  });
}

async function run() {
  console.log('Verifying all 8 Statistics & Probability lessons on localhost:8082...\n');
  let allPass = true;
  for (const slug of lessons) {
    const res = await checkLesson(slug);
    if (res.status === 200 && res.hasTabs && res.exercisesCount === 10 && res.quizCount === 5) {
      console.log(`[PASS] ${slug} -> Status 200 | Tabs OK | 10 Exercises | 5 Quizzes`);
    } else {
      console.log(`[FAIL] ${slug} ->`, res);
      allPass = false;
    }
  }
  if (allPass) {
    console.log('\nAll 8 Statistics & Probability lessons verified successfully!');
  } else {
    console.log('\nSome lessons failed verification.');
    process.exit(1);
  }
}

run();
