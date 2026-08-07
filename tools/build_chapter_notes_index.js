import fs from 'fs';
import path from 'path';

// Define metadata for all classes (identical configurations to main hubs to ensure matched URLs)
const classConfigs = {
  'class-9-maths': {
    classNum: '9',
    title: 'Class 9 Maths Chapter Wise Notes | SJMaths',
    description: 'Class 9 Maths chapter wise notes for CBSE board revision with formulas, solved examples and practice questions.',
    keywords: 'Class 9 Maths, CBSE Class 9 Maths, NCERT Class 9 Maths, SJMaths, Class 9 Maths Notes, Class 9, Notes',
    canonical: 'https://sjmaths.com/class-9-maths/chapter-wise-notes/',
    chapters: [
      { num: '01', name: 'Number Systems', notesFolder: 'chapter-1-use-of-coordinates' },
      { num: '02', name: 'Polynomials', notesFolder: 'chapter-2-linear-polynomials' },
      { num: '03', name: 'Coordinate Geometry', notesFolder: 'chapter-3-world-of-numbers' },
      { num: '04', name: 'Linear Equations in Two Variables', notesFolder: 'chapter-4-algebraic-identities' },
      { num: '05', name: "Introduction to Euclid's Geometry", notesFolder: 'chapter-5-circles' },
      { num: '06', name: 'Lines and Angles', notesFolder: 'chapter-6-perimeter-and-area' },
      { num: '07', name: 'Triangles', notesFolder: 'chapter-7-probability' },
      { num: '08', name: 'Quadrilaterals', notesFolder: 'chapter-8-sequences-and-progressions' },
      { num: '09', name: 'Circles', notesFolder: 'chapter-9-triangles' },
      { num: '10', name: "Heron's Formula", notesFolder: 'chapter-10-herons-formula' },
      { num: '11', name: 'Surface Areas and Volumes', notesFolder: 'chapter-11-surface-areas-and-volumes' },
      { num: '12', name: 'Statistics', notesFolder: 'chapter-12-statistics' }
    ],
    faqs: [
      { q: 'Are these Class 9 Maths notes sufficient for CBSE exams?', a: 'Yes, these notes cover all key concepts, formulas, and theorems required for school examinations and CBSE Class 9 curriculum. They are designed for quick revision.' },
      { q: 'Do these notes include important formulas?', a: 'Absolutely. Each chapter note includes a dedicated section for important formulas and identities to help you memorize them easily.' }
    ]
  },
  'class-11-maths': {
    classNum: '11',
    title: 'Class 11 Maths Chapter Wise Notes | SJMaths',
    description: 'Class 11 Maths chapter wise notes for CBSE board revision with formulas, solved examples and practice questions.',
    keywords: 'Class 11 Maths, CBSE Class 11 Maths, NCERT Class 11 Maths, SJMaths, Class 11 Maths Notes, Class 11, Notes',
    canonical: 'https://sjmaths.com/class-11-maths/chapter-wise-notes/',
    chapters: [
      { num: '01', name: 'Sets', notesFolder: 'chapter-1-sets' },
      { num: '02', name: 'Relations and Functions', notesFolder: 'chapter-2-relations-and-functions' },
      { num: '03', name: 'Trigonometric Functions', notesFolder: 'chapter-3-trigonometric-functions' },
      { num: '04', name: 'Complex Numbers & Quadratic Equations', notesFolder: 'chapter-4-complex-numbers-and-quadratic-equations' },
      { num: '05', name: 'Linear Inequalities', notesFolder: 'chapter-5-linear-inequalities' },
      { num: '06', name: 'Permutations and Combinations', notesFolder: 'chapter-6-permutations-and-combinations' },
      { num: '07', name: 'Binomial Theorem', notesFolder: 'chapter-7-binomial-theorem' },
      { num: '08', name: 'Sequences and Series', notesFolder: 'chapter-8-sequences-and-series' },
      { num: '09', name: 'Straight Lines', notesFolder: 'chapter-9-straight-lines' },
      { num: '10', name: 'Conic Sections', notesFolder: 'chapter-10-conic-sections' },
      { num: '11', name: 'Three Dimensional Geometry', notesFolder: 'chapter-11-introduction-to-three-dimensional-geometry' },
      { num: '12', name: 'Limits and Derivatives', notesFolder: 'chapter-12-limits-and-derivatives' },
      { num: '13', name: 'Statistics', notesFolder: 'chapter-13-statistics' },
      { num: '14', name: 'Probability', notesFolder: 'chapter-14-probability' }
    ],
    faqs: [
      { q: 'Are these Class 11 Maths notes sufficient for school exams and JEE prep?', a: 'Yes, these notes cover all key concepts, formulas, and derivations required for CBSE Class 11 exams, and build a strong foundation for competitive engineering exams like JEE.' },
      { q: 'Do these notes include important formulas?', a: 'Absolutely. Each chapter note includes a dedicated section for important formulas and identities to help you memorize them easily.' }
    ]
  },
  'class-12-maths': {
    classNum: '12',
    title: 'Class 12 Maths Chapter Wise Notes | SJMaths',
    description: 'Class 12 Maths chapter wise notes for CBSE board revision with formulas, solved examples and exam-focused practice resources.',
    keywords: 'Class 12 Maths, CBSE Class 12 Maths, NCERT Class 12 Maths, SJMaths, Class 12 Maths Notes, Class 12, Notes',
    canonical: 'https://sjmaths.com/class-12-maths/chapter-wise-notes/',
    chapters: [
      { num: '01', name: 'Relations and Functions', notesFolder: 'chapter-1-relations-and-functions' },
      { num: '02', name: 'Inverse Trigonometric Functions', notesFolder: 'chapter-2-inverse-trigonometric-functions' },
      { num: '03', name: 'Matrices', notesFolder: 'chapter-3-matrices' },
      { num: '04', name: 'Determinants', notesFolder: 'chapter-4-determinants' },
      { num: '05', name: 'Continuity and Differentiability', notesFolder: 'chapter-5-continuity-and-differentiability' },
      { num: '06', name: 'Applications of Derivatives', notesFolder: 'chapter-6-applications-of-derivatives' },
      { num: '07', name: 'Integrals', notesFolder: 'chapter-7-integrals' },
      { num: '08', name: 'Applications of Integrals', notesFolder: 'chapter-8-applications-of-integrals' },
      { num: '09', name: 'Differential Equations', notesFolder: 'chapter-9-differential-equations' },
      { num: '10', name: 'Vector Algebra', notesFolder: 'chapter-10-vector-algebra' },
      { num: '11', name: 'Three Dimensional Geometry', notesFolder: 'chapter-11-three-dimensional-geometry' },
      { num: '12', name: 'Linear Programming', notesFolder: 'chapter-12-linear-programming' },
      { num: '13', name: 'Probability', notesFolder: 'chapter-13-probability' }
    ],
    faqs: [
      { q: 'Are these Class 12 Maths notes sufficient for CBSE Board Exams?', a: 'Yes, these notes cover all key concepts, formulas, and theorems required for the CBSE Class 12 Board Exams. They are designed for quick revision and conceptual clarity.' },
      { q: 'Do these notes include important formulas?', a: 'Absolutely. Each chapter note includes a dedicated section for important formulas and identities to help you memorize them easily.' }
    ]
  }
};

// Master Class 10 chapter notes index load
const templateHtml = fs.readFileSync('class-10-maths/chapter-wise-notes/index.html', 'utf8');

for (const [classDir, cfg] of Object.entries(classConfigs)) {
  console.log(`Generating ${classDir}/chapter-wise-notes/index.html...`);

  // Build the list of chapters HTML
  let chaptersGridHtml = '';
  for (const ch of cfg.chapters) {
    // Standard names used in the cards
    let displayName = ch.name;
    if (displayName.length > 30) {
      displayName = displayName.substring(0, 28) + '...';
    }

    chaptersGridHtml += `
        <a href="/${classDir}/chapter-wise-notes/${ch.notesFolder}/" class="chapter-card">
            <div class="chap-number">${ch.num}</div>
            <div class="chap-info">
                <span>Chapter ${parseInt(ch.num)}</span>
                <h2>${displayName}</h2>
            </div>
            <div class="arrow-icon"><i class="fas fa-chevron-right"></i></div>
        </a>\n`;
  }

  // Build JSON-LD Items List
  let itemListElements = [];
  cfg.chapters.forEach((ch, index) => {
    itemListElements.push(`{ "@type": "ListItem", "position": ${index + 1}, "name": "${ch.name}", "url": "https://sjmaths.com/${classDir}/chapter-wise-notes/${ch.notesFolder}/" }`);
  });
  const itemListJson = `[\n        ${itemListElements.join(',\n        ')}\n      ]`;

  // Build JSON-LD FAQs List
  let faqListElements = [];
  cfg.faqs.forEach(faq => {
    faqListElements.push(`{
          "@type": "Question",
          "name": "${faq.q}",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "${faq.a}"
          }
        }`);
  });
  const faqListJson = `[\n        ${faqListElements.join(',\n        ')}\n      ]`;

  // Build the bottom SEO FAQ blocks HTML
  let bottomFaqHtml = '';
  for (const faq of cfg.faqs) {
    bottomFaqHtml += `
        <div class="faq-item" style="margin-bottom: 20px;">
            <h4 style="font-size: 1.1rem; font-weight: 600; color: var(--text-main, #2c3e50); margin-bottom: 8px;">${faq.q}</h4>
            <p style="color: var(--text-light, #7f8c8d); line-height: 1.5;">${faq.a}</p>
        </div>`;
  }

  // Construct the page structure
  let page = templateHtml;

  // Replace class-10 global string occurrences
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

  // JSON-LD Lists Injection
  // Replace ItemList elements
  page = page.replace(/"itemListElement":\s*\[[\s\S]*?\]\s*\}\s*<\/script>/, `"itemListElement": ${itemListJson}\n    }\n    </script>`);
  // Replace FAQPage elements
  page = page.replace(/"@type": "FAQPage"[\s\S]*?"mainEntity":\s*\[[\s\S]*?\]\s*\}\s*<\/script>/, `"@type": "FAQPage",\n      "mainEntity": ${faqListJson}\n    }\n    </script>`);

  // Breadcrumbs text
  page = page.replace(/<span>Class \d+<\/span>/, `<span>Class ${cfg.classNum}</span>`);

  // H2 Headline Bottom
  page = page.replace(/Class \d+ Maths: Chapter-wise Revision Notes & Formulas/, `Class ${cfg.classNum} Maths: Chapter-wise Revision Notes & Formulas`);
  page = page.replace(/Our comprehensive chapter-wise notes provide clear, concise summaries of all critical concepts, theorems, and formulas[\s\S]*?<\/p>/, `Our comprehensive chapter-wise notes provide clear, concise summaries of all critical concepts, theorems, and formulas for Class ${cfg.classNum} Mathematics.`);

  // Chapters list replacement
  const gridStartIndex = page.indexOf('<main class="chapters-container">');
  const gridEndIndex = page.indexOf('</main>', gridStartIndex);
  if (gridStartIndex !== -1 && gridEndIndex !== -1) {
    page = page.substring(0, gridStartIndex) + 
           `<main class="chapters-container">\n        ${chaptersGridHtml}` +
           page.substring(gridEndIndex);
  }

  // FAQ section bottom replacement
  page = page.replace(/<h3 style="color: var\(--primary, #059669\);[\s\S]*?<\/section>/, `<h3 style="color: var(--primary, #059669); font-size: 1.4rem; margin-bottom: 15px; border-bottom: 2px solid rgba(5, 150, 105, 0.2); padding-bottom: 10px;">Frequently Asked Questions</h3>\n        ${bottomFaqHtml}\n    </section>`);

  // Save the file
  fs.writeFileSync(`${classDir}/chapter-wise-notes/index.html`, page, 'utf8');
  console.log(`Successfully generated ${classDir}/chapter-wise-notes/index.html`);
}
