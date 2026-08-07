import fs from 'fs';
import path from 'path';

// Define metadata for all classes
const classConfigs = {
  'class-9-maths': {
    classNum: '9',
    title: 'Class 9 Maths NCERT Solutions, Notes, Worksheets | SJMaths',
    description: 'Class 9 Maths hub for NCERT solutions, chapter notes, worksheets, practice tests and CBSE board preparation resources.',
    keywords: 'Class 9 Maths, CBSE Class 9 Maths, NCERT Class 9 Maths, SJMaths, Class 9 Maths NCERT Solutions, Class 9 Maths Notes, Class 9 Maths Worksheets',
    canonical: 'https://sjmaths.com/class-9-maths/',
    h1: 'CBSE Class 9 Mathematics Preparation Hub',
    breadcrumbsSpan: 'Class 9 Maths',
    badgeChapters: '12 Chapters',
    badgeUnitTests: '6 Unit Tests',
    badgeMockPapers: '6 Full Mock Papers',
    badgePYQs: 'NCERT Exemplar',
    units: [
      { id: 'unit1', name: 'Unit 1: Number Systems' },
      { id: 'unit2', name: 'Unit 2: Algebra' },
      { id: 'unit3', name: 'Unit 3: Coordinate Geometry' },
      { id: 'unit4', name: 'Unit 4: Geometry' },
      { id: 'unit5', name: 'Unit 5: Mensuration' },
      { id: 'unit6', name: 'Unit 6: Statistics & Probability' }
    ],
    chapters: [
      {
        num: '01',
        name: 'Number Systems',
        icon: 'fas fa-calculator',
        unitId: 'unit1',
        unitName: 'Unit 1: Number Systems',
        notesFolder: 'chapter-1-use-of-coordinates',
        ncertFolder: 'chapter-1-use-of-coordinates',
        sheetFolder: 'chapter-1-number-system',
        exemplarFolder: 'chapter-1-number-system',
        testFolder: 'chapter-1-number-system'
      },
      {
        num: '02',
        name: 'Polynomials',
        icon: 'fas fa-chart-line',
        unitId: 'unit2',
        unitName: 'Unit 2: Algebra',
        notesFolder: 'chapter-2-linear-polynomials',
        ncertFolder: 'chapter-2-polynomials',
        sheetFolder: 'chapter-2-polynomials',
        exemplarFolder: 'chapter-2-polynomials',
        testFolder: 'chapter-2-polynomials'
      },
      {
        num: '03',
        name: 'Coordinate Geometry',
        icon: 'fas fa-border-all',
        unitId: 'unit3',
        unitName: 'Unit 3: Coordinate Geometry',
        notesFolder: 'chapter-3-world-of-numbers',
        ncertFolder: 'chapter-3-coordinate-geometry',
        sheetFolder: 'chapter-3-coordinate-geometry',
        exemplarFolder: 'chapter-3-coordinate-geometry',
        testFolder: 'chapter-3-coordinate-geometry'
      },
      {
        num: '04',
        name: 'Linear Equations in Two Variables',
        icon: 'fas fa-project-diagram',
        unitId: 'unit2',
        unitName: 'Unit 2: Algebra',
        notesFolder: 'chapter-4-algebraic-identities',
        ncertFolder: 'chapter-4-linear-equations-in-two-variables',
        sheetFolder: 'chapter-4-linear-equations-in-two-variables',
        exemplarFolder: 'chapter-4-linear-equations-in-two-variables',
        testFolder: 'chapter-4-linear-equations-in-two-variables'
      },
      {
        num: '05',
        name: "Introduction to Euclid's Geometry",
        icon: 'fas fa-shapes',
        unitId: 'unit4',
        unitName: 'Unit 4: Geometry',
        notesFolder: 'chapter-5-circles',
        ncertFolder: 'chapter-5-circles',
        sheetFolder: 'chapter-5-introduction-to-euclids-geometry',
        exemplarFolder: 'chapter-5-circles',
        testFolder: 'chapter-5-introduction-to-euclids-geometry'
      },
      {
        num: '06',
        name: 'Lines and Angles',
        icon: 'fas fa-draw-polygon',
        unitId: 'unit4',
        unitName: 'Unit 4: Geometry',
        notesFolder: 'chapter-6-perimeter-and-area',
        ncertFolder: 'chapter-6-perimeter-and-area',
        sheetFolder: 'chapter-6-lines-and-angles',
        exemplarFolder: 'chapter-6-perimeter-and-area',
        testFolder: 'chapter-6-lines-and-angles'
      },
      {
        num: '07',
        name: 'Triangles',
        icon: 'fas fa-play',
        unitId: 'unit4',
        unitName: 'Unit 4: Geometry',
        notesFolder: 'chapter-7-probability',
        ncertFolder: 'chapter-7-probability',
        sheetFolder: 'chapter-7-triangles',
        exemplarFolder: 'chapter-7-probability',
        testFolder: 'chapter-7-triangles'
      },
      {
        num: '08',
        name: 'Quadrilaterals',
        icon: 'fas fa-vector-square',
        unitId: 'unit4',
        unitName: 'Unit 4: Geometry',
        notesFolder: 'chapter-8-sequences-and-progressions',
        ncertFolder: 'chapter-8-sequences-and-progressions',
        sheetFolder: 'chapter-8-quadrilaterals',
        exemplarFolder: 'chapter-8-sequences-and-progressions',
        testFolder: 'chapter-8-quadrilaterals'
      },
      {
        num: '09',
        name: 'Circles',
        icon: 'fas fa-circle-notch',
        unitId: 'unit4',
        unitName: 'Unit 4: Geometry',
        notesFolder: 'chapter-9-triangles',
        ncertFolder: 'chapter-9-triangles',
        sheetFolder: 'chapter-9-circles',
        exemplarFolder: 'chapter-9-triangles',
        testFolder: 'chapter-9-circles'
      },
      {
        num: '10',
        name: "Heron's Formula",
        icon: 'fas fa-square-root-alt',
        unitId: 'unit5',
        unitName: 'Unit 5: Mensuration',
        notesFolder: 'chapter-10-herons-formula',
        ncertFolder: 'chapter-10-herons-formula',
        sheetFolder: 'chapter-10-herons-formula',
        exemplarFolder: 'chapter-10-heron-formula',
        testFolder: 'chapter-10-herons-formula'
      },
      {
        num: '11',
        name: 'Surface Areas and Volumes',
        icon: 'fas fa-cube',
        unitId: 'unit5',
        unitName: 'Unit 5: Mensuration',
        notesFolder: 'chapter-11-surface-areas-and-volumes',
        ncertFolder: 'chapter-11-surface-areas-and-volumes',
        sheetFolder: 'chapter-11-surface-areas-and-volumes',
        exemplarFolder: 'chapter-11-surface-areas-and-volumes',
        testFolder: 'chapter-11-surface-areas-and-volumes'
      },
      {
        num: '12',
        name: 'Statistics',
        icon: 'fas fa-chart-bar',
        unitId: 'unit6',
        unitName: 'Unit 6: Statistics & Probability',
        notesFolder: 'chapter-12-statistics',
        ncertFolder: 'chapter-12-statistics',
        sheetFolder: 'chapter-12-statistics',
        exemplarFolder: 'chapter-12-statistics',
        testFolder: 'chapter-12-statistics'
      }
    ],
    faqs: [
      { q: 'What study materials are available for Class 9 Maths?', a: 'We provide chapter-wise notes, NCERT solutions, practice exercises, printable worksheets, and online tests for Class 9 Mathematics.' },
      { q: 'Are the Class 9 Maths NCERT solutions free?', a: 'Yes, all NCERT solutions and chapter notes on SJMaths are completely free to access to help students prepare for their exams.' },
      { q: 'How can I practice for Class 9 Maths exams?', a: 'You can start by reviewing the chapter notes, solving the NCERT exercises, and then testing your knowledge with our worksheets and chapter-wise tests.' }
    ]
  },
  'class-11-maths': {
    classNum: '11',
    title: 'Class 11 Maths NCERT Solutions, Notes, Worksheets | SJMaths',
    description: 'Class 11 Maths hub for NCERT solutions, chapter notes, worksheets, mock tests and CBSE board preparation resources.',
    keywords: 'Class 11 Maths, CBSE Class 11 Maths, NCERT Class 11 Maths, SJMaths, Class 11 Maths NCERT Solutions, Class 11 Maths Notes, Class 11 Maths Worksheets',
    canonical: 'https://sjmaths.com/class-11-maths/',
    h1: 'CBSE Class 11 Mathematics Preparation Hub',
    breadcrumbsSpan: 'Class 11 Maths',
    badgeChapters: '14 Chapters',
    badgeUnitTests: '5 Unit Tests',
    badgeMockPapers: '5 Full Mock Papers',
    badgePYQs: 'NCERT Exemplar',
    units: [
      { id: 'unit1', name: 'Unit 1: Sets and Functions' },
      { id: 'unit2', name: 'Unit 2: Algebra' },
      { id: 'unit3', name: 'Unit 3: Coordinate Geometry' },
      { id: 'unit4', name: 'Unit 4: Calculus' },
      { id: 'unit5', name: 'Unit 5: Statistics & Probability' }
    ],
    chapters: [
      { num: '01', name: 'Sets', icon: 'fas fa-layer-group', unitId: 'unit1', unitName: 'Unit 1: Sets and Functions', notesFolder: 'chapter-1-sets', ncertFolder: 'chapter-1-sets', sheetFolder: 'chapter-1-sets', exemplarFolder: 'chapter-1-sets', testFolder: 'chapter-1-sets' },
      { num: '02', name: 'Relations and Functions', icon: 'fas fa-link', unitId: 'unit1', unitName: 'Unit 1: Sets and Functions', notesFolder: 'chapter-2-relations-and-functions', ncertFolder: 'chapter-2-relations-and-functions', sheetFolder: 'chapter-2-relations-and-functions', exemplarFolder: 'chapter-2-relations-and-functions', testFolder: 'chapter-2-relations-and-functions' },
      { num: '03', name: 'Trigonometric Functions', icon: 'fas fa-wave-square', unitId: 'unit1', unitName: 'Unit 1: Sets and Functions', notesFolder: 'chapter-3-trigonometric-functions', ncertFolder: 'chapter-3-trigonometric-functions', sheetFolder: 'chapter-3-trigonometric-functions', exemplarFolder: 'chapter-3-trigonometric-functions', testFolder: 'chapter-3-trigonometric-functions' },
      { num: '04', name: 'Complex Numbers & Quadratic Equations', icon: 'fas fa-calculator', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-4-complex-numbers-and-quadratic-equations', ncertFolder: 'chapter-4-complex-numbers-and-quadratic-equations', sheetFolder: 'chapter-4-complex-numbers-and-quadratic-equations', exemplarFolder: 'chapter-4-complex-numbers-and-quadratic-equations', testFolder: 'chapter-4-complex-numbers-and-quadratic-equations' },
      { num: '05', name: 'Linear Inequalities', icon: 'fas fa-greater-than-equal', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-5-linear-inequalities', ncertFolder: 'chapter-5-linear-inequalities', sheetFolder: 'chapter-5-linear-inequalities', exemplarFolder: 'chapter-5-linear-inequalities', testFolder: 'chapter-5-linear-inequalities' },
      { num: '06', name: 'Permutations and Combinations', icon: 'fas fa-project-diagram', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-6-permutations-and-combinations', ncertFolder: 'chapter-6-permutations-and-combinations', sheetFolder: 'chapter-6-permutations-and-combinations', exemplarFolder: 'chapter-6-permutations-and-combinations', testFolder: 'chapter-6-permutations-and-combinations' },
      { num: '07', name: 'Binomial Theorem', icon: 'fas fa-chart-line', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-7-binomial-theorem', ncertFolder: 'chapter-7-binomial-theorem', sheetFolder: 'chapter-7-binomial-theorem', exemplarFolder: 'chapter-7-binomial-theorem', testFolder: 'chapter-7-binomial-theorem' },
      { num: '08', name: 'Sequences and Series', icon: 'fas fa-list-ol', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-8-sequences-and-series', ncertFolder: 'chapter-8-sequences-and-series', sheetFolder: 'chapter-8-sequences-and-series', exemplarFolder: 'chapter-8-sequences-and-series', testFolder: 'chapter-8-sequences-and-series' },
      { num: '09', name: 'Straight Lines', icon: 'fas fa-slash', unitId: 'unit3', unitName: 'Unit 3: Coordinate Geometry', notesFolder: 'chapter-9-straight-lines', ncertFolder: 'chapter-9-straight-lines', sheetFolder: 'chapter-9-straight-lines', exemplarFolder: 'chapter-9-straight-lines', testFolder: 'chapter-9-straight-lines' },
      { num: '10', name: 'Conic Sections', icon: 'fas fa-shapes', unitId: 'unit3', unitName: 'Unit 3: Coordinate Geometry', notesFolder: 'chapter-10-conic-sections', ncertFolder: 'chapter-10-conic-sections', sheetFolder: 'chapter-10-conic-sections', exemplarFolder: 'chapter-10-conic-sections', testFolder: 'chapter-10-conic-sections' },
      { num: '11', name: 'Three Dimensional Geometry', icon: 'fas fa-cube', unitId: 'unit3', unitName: 'Unit 3: Coordinate Geometry', notesFolder: 'chapter-11-introduction-to-three-dimensional-geometry', ncertFolder: 'chapter-11-introduction-to-three-dimensional-geometry', sheetFolder: 'chapter-11-introduction-to-three-dimensional-geometry', exemplarFolder: 'chapter-11-introduction-to-three-dimensional-geometry', testFolder: 'chapter-11-introduction-to-three-dimensional-geometry' },
      { num: '12', name: 'Limits and Derivatives', icon: 'fas fa-history', unitId: 'unit4', unitName: 'Unit 4: Calculus', notesFolder: 'chapter-12-limits-and-derivatives', ncertFolder: 'chapter-12-limits-and-derivatives', sheetFolder: 'chapter-12-limits-and-derivatives', exemplarFolder: 'chapter-12-limits-and-derivatives', testFolder: 'chapter-12-limits-and-derivatives' },
      { num: '13', name: 'Statistics', icon: 'fas fa-chart-bar', unitId: 'unit5', unitName: 'Unit 5: Statistics & Probability', notesFolder: 'chapter-13-statistics', ncertFolder: 'chapter-13-statistics', sheetFolder: 'chapter-13-statistics', exemplarFolder: 'chapter-13-statistics', testFolder: 'chapter-13-statistics' },
      { num: '14', name: 'Probability', icon: 'fas fa-percentage', unitId: 'unit5', unitName: 'Unit 5: Statistics & Probability', notesFolder: 'chapter-14-probability', ncertFolder: 'chapter-14-probability', sheetFolder: 'chapter-14-probability', exemplarFolder: 'chapter-14-probability', testFolder: 'chapter-14-probability' }
    ],
    faqs: [
      { q: 'Is Class 11 Maths important for JEE?', a: 'Yes, Class 11 forms the foundation for Calculus, Coordinate Geometry, and Algebra, which are crucial topics for JEE Main and Advanced.' },
      { q: 'What study materials are available for Class 11?', a: 'We provide detailed chapter notes, NCERT solutions, NCERT Exemplar problems, worksheets, and unit-wise tests.' },
      { q: 'Are the Class 11 Maths resources free?', a: 'Yes, all notes, solutions, and test papers on SJMaths are completely free to access.' }
    ]
  },
  'class-12-maths': {
    classNum: '12',
    title: 'Class 12 Maths NCERT Solutions, Notes, PYQs, Tests | SJMaths',
    description: 'Class 12 Maths hub for NCERT solutions, chapter notes, worksheets, PYQs, sample papers and unit-wise online tests for CBSE board exam preparation.',
    keywords: 'Class 12 Maths, CBSE Class 12 Maths, NCERT Class 12 Maths, SJMaths, Class 12 Maths NCERT Solutions, Class 12 Maths Notes, Class 12 Maths PYQs, Class 12 Maths Worksheets, Class 12 Mock Papers',
    canonical: 'https://sjmaths.com/class-12-maths/',
    h1: 'CBSE Class 12 Mathematics Preparation Hub',
    breadcrumbsSpan: 'Class 12 Maths',
    badgeChapters: '13 Chapters',
    badgeUnitTests: '6 Unit Tests',
    badgeMockPapers: '7 Full Mock Papers',
    badgePYQs: '10+ Yrs PYQs',
    units: [
      { id: 'unit1', name: 'Unit 1: Relations and Functions' },
      { id: 'unit2', name: 'Unit 2: Algebra' },
      { id: 'unit3', name: 'Unit 3: Calculus' },
      { id: 'unit4', name: 'Unit 4: Vectors and 3D Geometry' },
      { id: 'unit5', name: 'Unit 5: Linear Programming' },
      { id: 'unit6', name: 'Unit 6: Probability' }
    ],
    chapters: [
      { num: '01', name: 'Relations and Functions', icon: 'fas fa-link', unitId: 'unit1', unitName: 'Unit 1: Relations and Functions', notesFolder: 'chapter-1-relations-and-functions', ncertFolder: 'chapter-1-relations-and-functions', pyqFolder: 'chapter-1-relations-and-functions', testFolder: 'chapter-1-relations-and-functions' },
      { num: '02', name: 'Inverse Trigonometric Functions', icon: 'fas fa-wave-square', unitId: 'unit1', unitName: 'Unit 1: Relations and Functions', notesFolder: 'chapter-2-inverse-trigonometric-functions', ncertFolder: 'chapter-2-inverse-trigonometric-functions', pyqFolder: 'chapter-2-inverse-trigonometric-functions', testFolder: 'chapter-2-inverse-trigonometric-functions' },
      { num: '03', name: 'Matrices', icon: 'fas fa-th', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-3-matrices', ncertFolder: 'chapter-3-matrices', pyqFolder: 'chapter-3-matrices', testFolder: 'chapter-3-matrices' },
      { num: '04', name: 'Determinants', icon: 'fas fa-border-all', unitId: 'unit2', unitName: 'Unit 2: Algebra', notesFolder: 'chapter-4-determinants', ncertFolder: 'chapter-4-determinants', pyqFolder: 'chapter-4-determinants', testFolder: 'chapter-4-determinants' },
      { num: '05', name: 'Continuity and Differentiability', icon: 'fas fa-bezier-curve', unitId: 'unit3', unitName: 'Unit 3: Calculus', notesFolder: 'chapter-5-continuity-and-differentiability', ncertFolder: 'chapter-5-continuity-and-differentiability', pyqFolder: 'chapter-5-continuity-and-differentiability', testFolder: 'chapter-5-continuity-and-differentiability' },
      { num: '06', name: 'Applications of Derivatives', icon: 'fas fa-chart-line', unitId: 'unit3', unitName: 'Unit 3: Calculus', notesFolder: 'chapter-6-applications-of-derivatives', ncertFolder: 'chapter-6-applications-of-derivatives', pyqFolder: 'chapter-6-applications-of-derivatives', testFolder: 'chapter-6-applications-of-derivatives' },
      { num: '07', name: 'Integrals', icon: 'fas fa-calculator', unitId: 'unit3', unitName: 'Unit 3: Calculus', notesFolder: 'chapter-7-integrals', ncertFolder: 'chapter-7-integrals', pyqFolder: 'chapter-7-integrals', testFolder: 'chapter-7-integrals' },
      { num: '08', name: 'Applications of Integrals', icon: 'fas fa-chart-area', unitId: 'unit3', unitName: 'Unit 3: Calculus', notesFolder: 'chapter-8-applications-of-integrals', ncertFolder: 'chapter-8-applications-of-integrals', pyqFolder: 'chapter-8-applications-of-integrals', testFolder: 'chapter-8-applications-of-integrals' },
      { num: '09', name: 'Differential Equations', icon: 'fas fa-project-diagram', unitId: 'unit3', unitName: 'Unit 3: Calculus', notesFolder: 'chapter-9-differential-equations', ncertFolder: 'chapter-9-differential-equations', pyqFolder: 'chapter-9-differential-equations', testFolder: 'chapter-9-differential-equations' },
      { num: '10', name: 'Vector Algebra', icon: 'fas fa-external-link-alt', unitId: 'unit4', unitName: 'Unit 4: Vectors and 3D Geometry', notesFolder: 'chapter-10-vector-algebra', ncertFolder: 'chapter-10-vector-algebra', pyqFolder: 'chapter-10-vector-algebra', testFolder: 'chapter-10-vector-algebra' },
      { num: '11', name: 'Three Dimensional Geometry', icon: 'fas fa-cube', unitId: 'unit4', unitName: 'Unit 4: Vectors and 3D Geometry', notesFolder: 'chapter-11-three-dimensional-geometry', ncertFolder: 'chapter-11-three-dimensional-geometry', pyqFolder: 'chapter-11-three-dimensional-geometry', testFolder: 'chapter-11-three-dimensional-geometry' },
      { num: '12', name: 'Linear Programming', icon: 'fas fa-map-signs', unitId: 'unit5', unitName: 'Unit 5: Linear Programming', notesFolder: 'chapter-12-linear-programming', ncertFolder: 'chapter-12-linear-programming', pyqFolder: 'chapter-12-linear-programming', testFolder: 'chapter-12-linear-programming' },
      { num: '13', name: 'Probability', icon: 'fas fa-percentage', unitId: 'unit6', unitName: 'Unit 6: Probability', notesFolder: 'chapter-13-probability', ncertFolder: 'chapter-13-probability', pyqFolder: 'chapter-13-probability', testFolder: 'chapter-13-probability' }
    ],
    faqs: [
      { q: 'What is the best way to prepare for Class 12 Maths board exams?', a: 'Click any chapter above to open its dedicated learning page. There you will find 5 pedagogical tabs: Chapter Notes, NCERT Solutions, Worksheets, PYQs, and Chapter Tests.' },
      { q: 'Are the Class 12 Maths notes, solutions, and tests free?', a: 'Yes, all study resources on SJMaths—including chapter notes, NCERT solutions, worksheets, PYQs, unit tests, and mock papers—are 100% free for all students.' },
      { q: 'Does SJMaths cover the latest CBSE syllabus for Class 12?', a: 'Yes, all resources are structured as per the latest NCERT syllabus and CBSE guidelines, making them ideal for standard Mathematics board exams.' }
    ]
  }
};

// Generate topic chips dynamically from data JSON files if possible
function getTopicChips(classDir, ch) {
  try {
    const jsonPath = path.join(classDir, `chapter-${parseInt(ch.num)}-data.json`);
    if (fs.existsSync(jsonPath)) {
      const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
      if (data.concepts && data.concepts.length > 0) {
        return data.concepts.slice(0, 4).map(c => c.title);
      }
    }
  } catch (e) {
    console.warn(`Error reading JSON for ${classDir} ch ${ch.num}:`, e.message);
  }
  // Fallbacks
  return ['Key Concepts', 'Formulas', 'NCERT Solutions', 'Practice Exercises'];
}

// Master Class 10 template load
const templateHtml = fs.readFileSync('class-10-maths/index.html', 'utf8');

for (const [classDir, cfg] of Object.entries(classConfigs)) {
  console.log(`Generating ${classDir}/index.html...`);

  // Build the list of chapters HTML
  let chaptersGridHtml = '';
  for (const ch of cfg.chapters) {
    const chips = getTopicChips(classDir, ch);
    const chipsHtml = chips.map(chip => `<span class="topic-chip">${chip}</span>`).join('\n                        ');

    let tabsHtml = '';
    if (classDir === 'class-9-maths') {
      tabsHtml = `
                        <a href="/class-9-maths/chapter-wise-notes/${ch.notesFolder}/" class="quick-tab-pill notes-tab"><i class="fas fa-book-open"></i><span>Notes</span></a>
                        <a href="/class-9-maths/ncert-exercise-practice/${ch.ncertFolder}/exercise-${parseInt(ch.num)}-1.html" class="quick-tab-pill ncert-tab"><i class="fas fa-pen-nib"></i><span>NCERT</span></a>
                        <a href="/class-9-maths/worksheets/${ch.sheetFolder}/standard.html" class="quick-tab-pill sheet-tab"><i class="fas fa-file-alt"></i><span>Sheets</span></a>
                        <a href="/class-9-maths/ncert-examplar-practice/${ch.exemplarFolder}/" class="quick-tab-pill pyq-tab"><i class="fas fa-lightbulb"></i><span>Exemplar</span></a>
                        <a href="/class-9-maths/tests/chapter-wise/${ch.testFolder}/test-1.html" class="quick-tab-pill test-tab"><i class="fas fa-check-circle"></i><span>Test</span></a>
      `;
    } else if (classDir === 'class-11-maths') {
      tabsHtml = `
                        <a href="/class-11-maths/chapter-wise-notes/${ch.notesFolder}/" class="quick-tab-pill notes-tab"><i class="fas fa-book-open"></i><span>Notes</span></a>
                        <a href="/class-11-maths/ncert-exercise-practice/${ch.ncertFolder}/exercise-${parseInt(ch.num)}-1.html" class="quick-tab-pill ncert-tab"><i class="fas fa-pen-nib"></i><span>NCERT</span></a>
                        <a href="/class-11-maths/worksheets/${ch.sheetFolder}/standard.html" class="quick-tab-pill sheet-tab"><i class="fas fa-file-alt"></i><span>Sheets</span></a>
                        <a href="/class-11-maths/ncert-exemplar-practice/${ch.exemplarFolder}/" class="quick-tab-pill pyq-tab"><i class="fas fa-lightbulb"></i><span>Exemplar</span></a>
                        <a href="/class-11-maths/tests/chapter-wise/${ch.testFolder}/test-1.html" class="quick-tab-pill test-tab"><i class="fas fa-check-circle"></i><span>Test</span></a>
      `;
    } else if (classDir === 'class-12-maths') {
      tabsHtml = `
                        <a href="/class-12-maths/chapter-wise-notes/${ch.notesFolder}/" class="quick-tab-pill notes-tab"><i class="fas fa-book-open"></i><span>Notes</span></a>
                        <a href="/class-12-maths/ncert-exercise-practice/${ch.ncertFolder}/exercise-${parseInt(ch.num)}-1.html" class="quick-tab-pill ncert-tab"><i class="fas fa-pen-nib"></i><span>NCERT</span></a>
                        <a href="#" class="quick-tab-pill sheet-tab disabled" style="opacity: 0.5; pointer-events: none;"><i class="fas fa-file-alt"></i><span>Sheets</span></a>
                        <a href="/class-12-maths/previous-years-questions-chapter-wise/${ch.pyqFolder}/" class="quick-tab-pill pyq-tab"><i class="fas fa-history"></i><span>PYQs</span></a>
                        <a href="/class-12-maths/tests/chapter-wise/${ch.testFolder}/test-1.html" class="quick-tab-pill test-tab"><i class="fas fa-check-circle"></i><span>Test</span></a>
      `;
    }

    chaptersGridHtml += `
            <!-- Chapter ${ch.num} -->
            <div class="ch-card-item" data-unit="${ch.unitId}">
                <div>
                    <div class="ch-card-header">
                        <span class="ch-num-badge"><i class="fas fa-layer-group"></i> Chapter ${ch.num}</span>
                        <span class="ch-unit-pill"><i class="fas fa-cubes"></i> ${ch.unitName}</span>
                    </div>
                    <h3 class="ch-card-title"><i class="${ch.icon}"></i> ${ch.name}</h3>
                    <div class="ch-topic-chips">
                        ${chipsHtml}
                    </div>
                    <div class="ch-quick-tabs-grid">
                        ${tabsHtml}
                    </div>
                </div>
                <a href="/${classDir}/chapter-wise-notes/${ch.notesFolder}/" class="ch-primary-cta">
                    <span>Explore Chapter & All Tabs</span>
                    <i class="fas fa-arrow-right"></i>
                </a>
            </div>
    `;
  }

  // Build the Unit filter select options HTML
  let unitFilterHtml = `<option value="all">All Units (1 - ${cfg.units.length})</option>`;
  for (const unit of cfg.units) {
    unitFilterHtml += `\n                    <option value="${unit.id}">${unit.name}</option>`;
  }

  // Build the FAQs section HTML
  let faqsHtml = '';
  for (const faq of cfg.faqs) {
    faqsHtml += `
        <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem 1.5rem; margin-bottom: 1rem; box-shadow: var(--card-shadow);">
            <h3 style="font-size: 1.05rem; font-weight: 700; color: #0f172a; margin: 0 0 0.5rem;">${faq.q}</h3>
            <p style="font-size: 0.9rem; color: #334155; margin: 0; line-height: 1.5;">${faq.a}</p>
        </div>`;
  }

  // Construct the page structure
  let page = templateHtml;

  // Replace class-10 specifics in JSON-LD schemas
  page = page.replace(/"name": "Class 10"/g, `"name": "Class ${cfg.classNum}"`);
  page = page.replace(/class-10-maths/g, `${classDir}`);
  page = page.replace(/Class 10 Maths/g, `Class ${cfg.classNum} Maths`);
  page = page.replace(/Class 10 Mathematics/g, `Class ${cfg.classNum} Mathematics`);
  page = page.replace(/Class 10/g, `Class ${cfg.classNum}`);

  // 1. Replace metadata
  page = page.replace(/<title>.*?<\/title>/, `<title>${cfg.title}</title>`);
  page = page.replace(/<meta name="description" content=".*?"\s*\/?>/, `<meta name="description" content="${cfg.description}">`);
  page = page.replace(/<meta name="keywords" content=".*?"\s*\/?>/, `<meta name="keywords" content="${cfg.keywords}">`);
  page = page.replace(/<link rel="canonical" href=".*?"\s*\/?>/, `<link rel="canonical" href="${cfg.canonical}">`);
  
  // Open Graph
  page = page.replace(/<meta property="og:title" content=".*?"\s*\/?>/, `<meta property="og:title" content="${cfg.title}">`);
  page = page.replace(/<meta property="og:description" content=".*?"\s*\/?>/, `<meta property="og:description" content="${cfg.description}">`);
  page = page.replace(/<meta property="og:url" content=".*?"\s*\/?>/, `<meta property="og:url" content="${cfg.canonical}">`);

  // Twitter
  page = page.replace(/<meta name="twitter:title" content=".*?"\s*\/?>/, `<meta name="twitter:title" content="${cfg.title}">`);
  page = page.replace(/<meta name="twitter:description" content=".*?"\s*\/?>/, `<meta name="twitter:description" content="${cfg.description}">`);

  // Breadcrumbs span
  page = page.replace(/<span>Class \d+ Maths<\/span>/, `<span>${cfg.breadcrumbsSpan}</span>`);
  
  // H1 and H1 subtext
  page = page.replace(/<h1>CBSE Class \d+ Mathematics Preparation Hub<\/h1>/, `<h1>${cfg.h1}</h1>`);
  page = page.replace(/<p>Select any chapter below to access its complete 5-step learning system: Chapter Notes, NCERT Solutions, Worksheets, PYQs, and Chapter Tests.<\/p>/, `Select study resources below including Chapter Notes, NCERT Solutions, Worksheets, and practice tests.`);

  // Hero badges
  page = page.replace(/<span class="hero-badge"><i class="fas fa-book"><\/i> \d+ Chapters<\/span>/, `<span class="hero-badge"><i class="fas fa-book"></i> ${cfg.badgeChapters}</span>`);
  page = page.replace(/<span class="hero-badge"><i class="fas fa-history"><\/i> .*?<\/span>/, `<span class="hero-badge"><i class="fas fa-history"></i> ${cfg.badgePYQs}</span>`);
  page = page.replace(/<span class="hero-badge"><i class="fas fa-vial"><\/i> \d+ Unit Tests<\/span>/, `<span class="hero-badge"><i class="fas fa-vial"></i> ${cfg.badgeUnitTests}</span>`);
  page = page.replace(/<span class="hero-badge"><i class="fas fa-file-signature"><\/i> \d+ Full Mock Papers<\/span>/, `<span class="hero-badge"><i class="fas fa-file-signature"></i> ${cfg.badgeMockPapers}</span>`);

  // Disable/hide Smart Learning engine banner for Class 9, 11, 12 since it is Class 10 beta only
  page = page.replace(/<div class="learning-banner-container">[\s\S]*?<\/div>\s*<\/div>/, '');

  // Sticky controls title & options
  page = page.replace(/All \d+ CBSE Chapters/, `All ${cfg.badgeChapters}`);
  page = page.replace(/<select class="unit-filter-select" id="unit-filter"[\s\S]*?<\/select>/, `<select class="unit-filter-select" id="unit-filter" onchange="applyFilter()">\n                    ${unitFilterHtml}\n                </select>`);

  // Grid chapters replacement - USE SECURE INDEX LOOKUP INSTEAD OF FRAGILE REGEX
  const gridStartIndex = page.indexOf('<div class="hub-grid" id="chapters-grid">');
  const mainEndIndex = page.indexOf('</main>', gridStartIndex);
  if (gridStartIndex !== -1 && mainEndIndex !== -1) {
    page = page.substring(0, gridStartIndex) + 
           `<div class="hub-grid" id="chapters-grid">\n${chaptersGridHtml}\n            </div>\n        ` +
           page.substring(mainEndIndex);
  }

  // FAQ section replacement
  page = page.replace(/<section style="max-width: 900px; margin: 40px auto; padding: 0 20px;">[\s\S]*?<\/section>/, `<section style="max-width: 900px; margin: 40px auto; padding: 0 20px;">\n        <h2 style="text-align: center; font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-bottom: 1.5rem;">\n            <i class="far fa-question-circle" style="color: var(--primary);"></i> Frequently Asked Questions\n        </h2>\n        ${faqsHtml}\n    </section>`);

  // Save the file
  fs.writeFileSync(`${classDir}/index.html`, page, 'utf8');
  console.log(`Successfully generated ${classDir}/index.html`);
}
