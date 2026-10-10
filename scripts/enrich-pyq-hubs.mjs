import fs from 'node:fs';
import path from 'node:path';
import * as cheerio from 'cheerio';

const ROOT = process.cwd();
const base = 'class-10-maths/previous-year-questions';

const chapterData = {
  'chapter-2-polynomials': {
    name: 'Polynomials',
    num: 2,
    unit: 'Unit 2: Algebra',
    marks: '4 to 5 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Identifying number of zeroes from graphs of \\(y = p(x)\\) by counting \\(x\\)-axis intersections, finding zeroes of simple quadratic polynomials, or calculating \\(\\alpha + \\beta\\) and \\(\\alpha\\beta\\).' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Finding zeroes of quadratic polynomials by splitting the middle term and verifying the relationship between zeroes and coefficients: \\(\\alpha + \\beta = -b/a\\) and \\(\\alpha\\beta = c/a\\).' },
      { title: 'Section C / D (3 Marks)', desc: 'Forming a quadratic polynomial given its zeroes or the sum and product of zeroes, and evaluating symmetric expressions such as \\(\\alpha^2 + \\beta^2\\), \\(1/\\alpha + 1/\\beta\\), and \\(\\alpha/\\beta + \\beta/\\alpha\\).' }
    ],
    tips: 'Be careful with signs when using \\(\\alpha + \\beta = -b/a\\). When forming a polynomial, always write the general family \\(k[x^2 - (\\alpha+\\beta)x + \\alpha\\beta]\\) where \\(k\\) is a real constant. When factoring polynomials with roots like \\(4\\sqrt{3}x^2 + 5x - 2\\sqrt{3}\\), verify intermediate products carefully.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-2-polynomials/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-2-polynomials/exercise-2-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-2-polynomials/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-2-polynomials/test-1-solutions.html'
  },
  'chapter-3-pair-of-linear-equations-in-two-variables': {
    name: 'Pair of Linear Equations in Two Variables',
    num: 3,
    unit: 'Unit 2: Algebra',
    marks: '4 to 6 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Testing consistency conditions for pairs of equations: unique solution (\\(a_1/a_2 \\neq b_1/b_2\\)), infinitely many solutions (\\(a_1/a_2 = b_1/b_2 = c_1/c_2\\)), or no solution (\\(a_1/a_2 = b_1/b_2 \\neq c_1/c_2\\)).' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Solving pairs of linear equations algebraically using the Elimination Method or Substitution Method, including equations with coefficients that interchange.' },
      { title: 'Section D / E (4 to 5 Marks Word Problems)', desc: 'Real-world word problems based on upstream and downstream boat speeds, speed-distance-time relationships, two-digit number digit reversal, and age problems.' }
    ],
    tips: 'For upstream and downstream questions, always assume boat speed in still water as \\(x\\) km/h and stream speed as \\(y\\) km/h; speed upstream is \\((x-y)\\) km/h and downstream is \\((x+y)\\) km/h (with \\(x > y\\)). In consistency questions, ensure both equations are written in standard form \\(ax + by + c = 0\\) before taking ratios.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-3-pair-of-linear-equations-in-two-variables/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-3-pair-of-linear-equations-in-two-variables/exercise-3-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-3-pair-of-linear-equations-in-two-variables/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-3-pair-of-linear-equations-in-two-variables/test-1-solutions.html'
  },
  'chapter-4-quadratic-equations': {
    name: 'Quadratic Equations',
    num: 4,
    unit: 'Unit 2: Algebra',
    marks: '5 to 6 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Identifying whether an equation is quadratic, evaluating the discriminant \\(D = b^2 - 4ac\\), or determining the nature of roots for given values of parameter \\(k\\).' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Solving quadratic equations by factorisation (splitting the middle term) and applying the quadratic formula \\(x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}\\) to solve radical and fractional equations.' },
      { title: 'Section D / E (4 to 5 Marks)', desc: 'Challenging word problems on train speeds (train travelling at uniform speed taking less time if speed increased), water taps filling a tank together, and geometric dimensions.' }
    ],
    tips: 'When questions state that a quadratic equation has real and equal roots, set \\(D = b^2 - 4ac = 0\\) and solve for the unknown parameter. Check for extraneous roots in fractional equations by ensuring denominators are non-zero. Clearly specify units (km/h, hours, meters) in final answers for word problems.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-4-quadratic-equations/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-4-quadratic-equations/exercise-4-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-4-quadratic-equations/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-4-quadratic-equations/test-1-solutions.html'
  },
  'chapter-5-arithmetic-progressions': {
    name: 'Arithmetic Progressions',
    num: 5,
    unit: 'Unit 2: Algebra',
    marks: '4 to 6 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Finding common difference \\(d\\), evaluating the \\(n\\)-th term from given AP sequence, or identifying which term of an AP is zero or negative.' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Direct application of the \\(n\\)-th term formula \\(a_n = a + (n-1)d\\) and sum of first \\(n\\) terms formula \\(S_n = \\frac{n}{2}[2a + (n-1)d] = \\frac{n}{2}(a + l)\\).' },
      { title: 'Section E (4 Marks Case Study)', desc: 'CBSE Case-Based Questions often feature AP applications such as tiered stadium seating, annual salary increments, tree planting along highways, or daily production savings.' }
    ],
    tips: 'When the sum of \\(n\\) terms \\(S_n\\) is given as a quadratic expression in \\(n\\), find the \\(n\\)-th term using \\(a_n = S_n - S_{n-1}\\) and the first term using \\(a_1 = S_1\\). When assuming three terms in AP, choose \\(a - d, a, a + d\\) for algebraic simplicity in sum-based problems.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-5-arithmetic-progressions/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-5-arithmetic-progressions/exercise-5-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-5-arithmetic-progressions/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-5-arithmetic-progressions/test-1-solutions.html'
  },
  'chapter-6-triangles': {
    name: 'Triangles',
    num: 6,
    unit: 'Unit 4: Geometry',
    marks: '8 to 10 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Ratio of corresponding sides of similar triangles, ratio of perimeters, and applying AA/SAS similarity criteria in geometric diagrams.' },
      { title: 'Section C (3 Marks Theorem Proof)', desc: 'Formal proof of the Basic Proportionality Theorem (BPT / Thales Theorem): if a line is drawn parallel to one side of a triangle, it divides the other two sides in the same ratio.' },
      { title: 'Section D / E (4 to 5 Marks Proofs)', desc: 'Higher-order geometric proofs using similarity criteria (AA, SAS, SSS), such as proving diagonals of a trapezium divide proportionally or median ratios in similar triangles.' }
    ],
    tips: 'BPT is one of the most frequently asked 3-mark or 5-mark theorem proofs in CBSE history. Always draw a neat diagram with proper labeling, clearly write Given, To Prove, Construction, and Proof step-by-step with justification in brackets for every statement.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-6-triangles/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-6-triangles/exercise-6-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-6-triangles/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-6-triangles/test-1-solutions.html'
  },
  'chapter-7-coordinate-geometry': {
    name: 'Coordinate Geometry',
    num: 7,
    unit: 'Unit 3: Coordinate Geometry',
    marks: '6 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Distance of a point from origin \\(\\sqrt{x^2+y^2}\\), distance from axes, or coordinates of midpoint of a line segment.' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Distance Formula \\(d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\\) applied to check collinearity of points, isosceles/equilateral triangles, or parallelogram properties.' },
      { title: 'Section C / D (3 to 4 Marks)', desc: 'Section Formula for internal division: finding coordinates of points of trisection, finding the ratio in which the \\(x\\)-axis or \\(y\\)-axis divides a segment by assuming ratio \\(k:1\\).' }
    ],
    tips: 'When finding the ratio in which an axis divides a line segment, assume the ratio as \\(k:1\\). If dividing by the \\(x\\)-axis, set the \\(y\\)-coordinate of the point of division to \\(0\\); if by the \\(y\\)-axis, set the \\(x\\)-coordinate to \\(0\\). Always double-check negative signs inside square roots.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-7-coordinate-geometry/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-7-coordinate-geometry/exercise-7-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-7-coordinate-geometry/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-7-coordinate-geometry/test-1-solutions.html'
  },
  'chapter-8-introduction-to-trigonometry': {
    name: 'Introduction to Trigonometry',
    num: 8,
    unit: 'Unit 5: Trigonometry',
    marks: '7 to 8 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Definitions of trigonometric ratios (\\(\\sin, \\cos, \\tan, \\cot, \\sec, \\text{cosec}\\)), values at standard angles (\\(0^\\circ, 30^\\circ, 45^\\circ, 60^\\circ, 90^\\circ\\)), and evaluating trigonometric expressions.' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Right-angled triangle ratio evaluations given one ratio (e.g. if \\(\\tan A = 4/3\\), find other ratios), and trigonometric equations involving complementary angle relationships.' },
      { title: 'Section D (5 Marks Identity Proof)', desc: 'Rigorous algebraic proofs of trigonometric identities using \\(\\sin^2\\theta + \\cos^2\\theta = 1\\), \\(1 + \\tan^2\\theta = \\sec^2\\theta\\), and \\(1 + \\cot^2\\theta = \\text{cosec}^2\\theta\\).' }
    ],
    tips: 'Memorize the standard trigonometric table thoroughly. For 5-mark identity proofs, convert all terms into \\(\\sin\\theta\\) and \\(\\cos\\theta\\) if direct identities are not obvious, or rationalize denominators with conjugate expressions (e.g. multiplying by \\(1 - \\sin\\theta\\)).',
    notes: '/class-10-maths/chapter-wise-notes/chapter-8-introduction-to-trigonometry/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-8-introduction-to-trigonometry/exercise-8-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-8-introduction-to-trigonometry/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-8-introduction-to-trigonometry/test-1-solutions.html'
  },
  'chapter-9-applications-of-trigonometry': {
    name: 'Applications of Trigonometry (Heights and Distances)',
    num: 9,
    unit: 'Unit 5: Trigonometry',
    marks: '4 to 5 marks',
    topics: [
      { title: 'Section C / D (3 to 5 Marks Word Problem)', desc: 'Calculating heights of towers, poles, and multi-storey buildings or widths of rivers given angles of elevation and depression from single or dual observation points.' },
      { title: 'Section E (4 Marks Case Study)', desc: 'Real-world scenarios such as air-traffic control observing planes, maritime lighthouse observations of incoming ships, or kite flying string angle measurements.' }
    ],
    tips: 'A correct geometric diagram constitutes 50% of the solution in heights and distances problems. Clearly distinguish between angle of elevation (looking upwards from horizontal line of sight) and angle of depression (looking downwards from horizontal line of sight). Use \\(\\sqrt{3} \\approx 1.732\\) only when specified in the question.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-9-applications-of-trigonometry/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-9-applications-of-trigonometry/exercise-9-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-9-applications-of-trigonometry/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-9-applications-of-trigonometry/test-1-solutions.html'
  },
  'chapter-10-circles': {
    name: 'Circles',
    num: 10,
    unit: 'Unit 4: Geometry',
    marks: '4 to 6 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Angle between tangent and radius at point of contact (\\(90^\\circ\\)), number of tangents from points inside, on, or outside a circle, and angle subtended by tangents at center.' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Applying Theorem 10.1 (tangent perpendicular to radius) and Theorem 10.2 (equal tangent lengths from an external point) to find lengths, angles, and chord relationships.' },
      { title: 'Section D (5 Marks Proof)', desc: 'Proving that opposite sides of a quadrilateral circumscribing a circle subtend supplementary angles at the center, or proving \\(AB + CD = AD + BC\\) for circumscribing quadrilaterals.' }
    ],
    tips: 'Theorem 10.2 is frequently asked as a direct theorem proof. Remember that radii drawn to points of contact create right angles, which often allows you to apply Pythagoras theorem in right triangles formed by radius, tangent, and line from center to external point.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-10-circles/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-10-circles/exercise-10-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-10-circles/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-10-circles/test-1-solutions.html'
  },
  'chapter-11-areas-related-to-circles': {
    name: 'Areas Related to Circles',
    num: 11,
    unit: 'Unit 6: Mensuration',
    marks: '3 to 4 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Formula-based questions on perimeter (circumference) and area of circle, area of semicircle, or relation between central angle and sector area.' },
      { title: 'Section B / C (2 or 3 Marks)', desc: 'Finding area of sector of a circle \\(\\frac{\\theta}{360^\\circ}\\pi r^2\\) and length of an arc \\(\\frac{\\theta}{360^\\circ}2\\pi r\\), such as clock minute hand sweeps in 5 or 15 minutes.' },
      { title: 'Section C / D (3 Marks Composite Area)', desc: 'Calculating area of minor and major segments by subtracting the area of triangle from sector area, especially for central angles of \\(60^\\circ\\) and \\(90^\\circ\\).' }
    ],
    tips: 'For central angle \\(90^\\circ\\), the triangle is right-angled with area \\(\\frac{1}{2}r^2\\). For central angle \\(60^\\circ\\), the triangle is equilateral with area \\(\\frac{\\sqrt{3}}{4}r^2\\). Ensure \\(\\pi\\) is substituted as \\(22/7\\) or \\(3.14\\) strictly according to paper instructions.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-11-areas-related-to-circles/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-11-areas-related-to-circles/exercise-11-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-11-areas-related-to-circles/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-11-areas-related-to-circles/test-1-solutions.html'
  },
  'chapter-12-surface-areas-and-volumes': {
    name: 'Surface Areas and Volumes',
    num: 12,
    unit: 'Unit 6: Mensuration',
    marks: '5 to 6 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Ratio of volumes of two spheres, surface area of hemisphere, or slant height of cone \\(l = \\sqrt{r^2+h^2}\\).' },
      { title: 'Section C (3 Marks)', desc: 'Total surface area and volume of combined solids (e.g. test tube consisting of cylinder surmounted by hemisphere, toy in form of cone mounted on hemisphere).' },
      { title: 'Section D / E (4 to 5 Marks)', desc: 'Conversion of one solid shape into another (melting metallic spheres into a cylinder where volume remains constant) and water flow rate problems through cylindrical pipes into tanks.' }
    ],
    tips: 'When two solids are joined (such as a cylinder and hemisphere), remember that the joined circular base is internal, so Total Surface Area is \\(\\text{CSA of cylinder} + \\text{CSA of hemisphere}\\), NOT the sum of their individual total surface areas. Keep \\(\\pi\\) in common factor calculations to simplify arithmetic.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-12-surface-areas-and-volumes/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-12-surface-areas-and-volumes/exercise-12-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-12-surface-areas-and-volumes/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-12-surface-areas-and-volumes/test-1-solutions.html'
  },
  'chapter-13-statistics': {
    name: 'Statistics',
    num: 13,
    unit: 'Unit 7: Statistics & Probability',
    marks: '7 to 8 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Empirical relationship between three measures of central tendency: \\(\\text{Mode} = 3\\text{Median} - 2\\text{Mean}\\), class mark calculation \\(\\frac{\\text{upper}+\\text{lower}}{2}\\), and modal class identification.' },
      { title: 'Section C (3 Marks)', desc: 'Calculating Mean of grouped data using Direct Method or Assumed Mean Method, and calculating Mode using modal formula \\(l + (\\frac{f_1-f_0}{2f_1-f_0-f_2})h\\).' },
      { title: 'Section D (5 Marks)', desc: 'Calculating Median of grouped data using \\(l + (\\frac{N/2 - cf}{f})h\\), and solving for missing frequencies \\(x\\) and \\(y\\) (or \\(f_1, f_2\\)) when total frequency and median are given.' }
    ],
    tips: 'In median calculations, the cumulative frequency \\(cf\\) in the formula is the cumulative frequency of the class PRECEDING the median class. For continuous grouped data, ensure classes are exclusive (if given 0-9, 10-19, convert to 0.5-9.5, 9.5-19.5 before taking boundaries). Always verify that calculated mean/median/mode lies within the modal or median class interval.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-13-statistics/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-13-statistics/exercise-13-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-13-statistics/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-13-statistics/test-1-solutions.html'
  },
  'chapter-14-probability': {
    name: 'Probability',
    num: 14,
    unit: 'Unit 7: Statistics & Probability',
    marks: '3 to 4 marks',
    topics: [
      { title: 'Section A (1 Mark MCQ)', desc: 'Probability of sure event (1), impossible event (0), range of probability \\(0 \\le P(E) \\le 1\\), and relation \\(P(E) + P(\\text{not } E) = 1\\).' },
      { title: 'Section B (2 Marks)', desc: 'Tossing two coins simultaneously (sample space 4 outcomes), tossing a single fair die (primes, odd, numbers greater than 4), or selecting colored balls/marbles from an urn.' },
      { title: 'Section C (3 Marks)', desc: 'Well-shuffled deck of 52 playing cards (face cards, black kings, red aces, spades) or tossing two dice simultaneously (36 outcomes: sum equal to 8, doublet, sum at least 10).' }
    ],
    tips: 'In playing card questions, remember that a standard deck has 12 face cards (4 Kings, 4 Queens, 4 Jacks) and 4 Aces (Aces are not face cards). In two-dice problems, always write the total number of elementary outcomes as \\(6 \\times 6 = 36\\) before listing favourable outcomes.',
    notes: '/class-10-maths/chapter-wise-notes/chapter-14-probability/',
    ncert: '/class-10-maths/ncert-exercise-practice/chapter-14-probability/exercise-14-1.html',
    worksheets: '/class-10-maths/worksheets/chapter-14-probability/standard.html',
    tests: '/class-10-maths/tests/chapter-wise/chapter-14-probability/test-1.html'
  }
};

let updatedCount = 0;

for (const [folder, data] of Object.entries(chapterData)) {
  const filePath = path.join(ROOT, base, folder, 'index.html');
  if (!fs.existsSync(filePath)) continue;

  let content = fs.readFileSync(filePath, 'utf8');
  if (content.includes('CBSE Board Exam Blueprint &amp; Topic Weightage') || content.includes('CBSE Board Exam Blueprint & Topic Weightage')) {
    console.log(`Skipping ${folder} (already enriched)`);
    continue;
  }

  const $ = cheerio.load(content);
  
  const topicsHtml = data.topics.map(t => `
        <li><strong>${t.title}:</strong> ${t.desc}</li>`).join('');

  const blueprintHtml = `
    <section class="pyq-section" style="margin-top: 28px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: clamp(20px, 4vw, 32px); box-shadow: 0 4px 16px rgba(15,23,42,0.04);">
      <h2 style="color: #0f172a; margin-top: 0; font-size: clamp(1.25rem, 3vw, 1.6rem);">CBSE Board Exam Blueprint &amp; Topic Weightage: ${data.name}</h2>
      <p style="color: #475569; line-height: 1.7; font-size: 1rem;">In the Class 10 CBSE Board Examination, <strong>${data.name}</strong> is a high-yielding component of <strong>${data.unit}</strong>, consistently carrying <strong>${data.marks}</strong> in the annual 80-mark written board paper. Recurring question formats observed over past board papers include:</p>
      <ul style="line-height: 1.8; color: #334155; margin: 16px 0 20px 24px; font-size: 0.95rem;">${topicsHtml}
      </ul>
      <h3 style="color: #0f172a; font-size: 1.18rem; margin-top: 22px;">Key Revision Tips &amp; Common Pitfalls</h3>
      <p style="color: #475569; line-height: 1.7; font-size: 0.95rem;">${data.tips}</p>
      <div style="margin-top: 24px; padding: 18px; background: #f0fdf4; border-radius: 14px; border: 1px solid #bbf7d0;">
        <strong style="color: #166534; font-size: 0.98rem;">Complete ${data.name} Preparation Cluster:</strong>
        <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-top: 10px; font-size: 0.92rem;">
          <a href="${data.notes}" style="color: #15803d; font-weight: 600; text-decoration: underline;">${data.name} Revision Notes</a> &bull;
          <a href="${data.ncert}" style="color: #15803d; font-weight: 600; text-decoration: underline;">NCERT Exercise Solutions</a> &bull;
          <a href="${data.worksheets}" style="color: #15803d; font-weight: 600; text-decoration: underline;">Case Study &amp; HOTS Worksheets</a> &bull;
          <a href="${data.tests}" style="color: #15803d; font-weight: 600; text-decoration: underline;">Chapter Practice Test</a>
        </div>
      </div>
    </section>`;

  // Insert before closing </main>
  const mainCloseIndex = content.lastIndexOf('</main>');
  if (mainCloseIndex > -1) {
    content = content.slice(0, mainCloseIndex) + blueprintHtml + '\n  ' + content.slice(mainCloseIndex);
    fs.writeFileSync(filePath, content, 'utf8');
    updatedCount++;
    console.log(`Enriched: ${folder}/index.html`);
  }
}

console.log(`Total PYQ chapter hubs enriched: ${updatedCount}`);
