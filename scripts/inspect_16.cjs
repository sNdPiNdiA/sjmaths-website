const fs = require('fs');
const cheerio = require('cheerio');

const files = [
  'class-11-applied-mathematics/chapter-16-circle-and-parabola/16-1-circle/index.html',
  'class-11-applied-mathematics/chapter-16-circle-and-parabola/16-2-parabola/index.html'
];

files.forEach(f => {
  console.log('=== ' + f + ' ===');
  const html = fs.readFileSync(f, 'utf8');
  const $ = cheerio.load(html);
  console.log('Title:', $('title').text());
  console.log('tab-learn text len:', $('#tab-learn').text().trim().length);
  console.log('tab-progress text len:', $('#tab-progress').text().trim().length);
  console.log('tab-worksheet text len:', $('#tab-worksheet').text().trim().length);
  console.log('tab-revision text len:', $('#tab-revision').text().trim().length);
  console.log('tab-mock text len:', $('#tab-mock').text().trim().length);

  // check mockObjectiveData
  const mockMatch = html.match(/window\.mockObjectiveData\s*=\s*(\[[\s\S]*?\]);\s*(?:window\.grade|function)/);
  if (mockMatch) {
    try {
      // evaluate
      const data = eval(mockMatch[1]);
      console.log('Mock questions count:', data.length);
      console.log('Sample question 1:', data[0].question.substring(0, 80));
      console.log('Sample explanation 1:', data[0].explanation.substring(0, 80));
    } catch(e) {
      console.log('Error parsing mockObjectiveData:', e.message);
    }
  } else {
    console.log('No window.mockObjectiveData found');
  }

  // check where boilerplate appears
  const phrases = [
    'By fundamental definition, the parameter satisfies the required identity constraint',
    'satisfies the required identity constraint',
    'Applied Mathematics analytical principles establish standard domain constraints',
    'analytical principles establish standard domain constraints',
    'systematic validation confirms correctness'
  ];
  phrases.forEach(p => {
    if (html.includes(p)) {
      console.log('Contains boilerplate phrase: "' + p + '"');
    }
  });
});

