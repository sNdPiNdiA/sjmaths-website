const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const BASE_URL = 'https://sjmaths.com';

const ORG_SCHEMA = {
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "SJ Maths",
  "url": `${BASE_URL}/`,
  "logo": `${BASE_URL}/favicon.png`,
  "sameAs": [
    "https://youtube.com/@sjmaths"
  ],
  "description": "Comprehensive CBSE Class 9-12 Mathematics, Science, SAT Math, and Competitive Exam PYQs, Worksheets, Chapter Notes, and Mock Tests."
};

const WEBSITE_SCHEMA = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "SJ Maths",
  "url": `${BASE_URL}/`,
  "potentialAction": {
    "@type": "SearchAction",
    "target": `${BASE_URL}/search.html?q={search_term_string}`,
    "query-input": "required name=search_term_string"
  }
};

const CATEGORY_FAQS = {
  'class-10-maths': {
    name: "CBSE Class 10 Mathematics Complete Study Package",
    level: "Class 10 CBSE",
    faqs: [
      {
        q: "What resources are available for CBSE Class 10 Maths on SJ Maths?",
        a: "SJ Maths provides chapter-wise formula notes, NCERT exemplar exercise solutions, past 10 years solved board PYQs, interactive unit online test papers, and timed mock exams for Class 10 Mathematics."
      },
      {
        q: "Are the Class 10 Maths practice tests and solutions free?",
        a: "Yes, all chapter notes, NCERT practice questions, chapter-wise mock tests, and full-length board paper simulations on SJ Maths are completely free."
      },
      {
        q: "Does SJ Maths cover both Standard and Basic Class 10 Maths?",
        a: "Yes! Our question bank and 7 full-length mock sets are curated for both CBSE Class 10 Mathematics Standard (Code 041) and Mathematics Basic (Code 241)."
      }
    ]
  },
  'class-11-maths': {
    name: "CBSE Class 11 Mathematics Study Package",
    level: "Class 11 CBSE",
    faqs: [
      {
        q: "Which topics are included in Class 11 Maths on SJ Maths?",
        a: "We cover Sets, Relations & Functions, Trigonometric Functions, Complex Numbers, Linear Inequalities, Permutations & Combinations, Binomial Theorem, Sequences & Series, Straight Lines, Conic Sections, 3D Geometry, Limits & Derivatives, Statistics, and Probability."
      },
      {
        q: "Are NCERT solutions and practice sets available for Class 11?",
        a: "Yes, chapter-wise NCERT solutions, formula sheets, practice worksheets, and unit tests are freely accessible."
      }
    ]
  },
  'class-11-chemistry': {
    name: "CBSE Class 11 Chemistry Notes & Practice Sets",
    level: "Class 11 CBSE Chemistry",
    faqs: [
      {
        q: "What Class 11 Chemistry topics are covered?",
        a: "We cover Some Basic Concepts of Chemistry, Structure of Atom, Classification of Elements, Chemical Bonding, Thermodynamics, Equilibrium, Redox Reactions, Organic Chemistry Basics, and Hydrocarbons."
      },
      {
        q: "Are chemical formulas and key reaction notes included?",
        a: "Yes, concise reaction mechanisms, formula sheets, NCERT practice questions, and chapter test papers are provided."
      }
    ]
  },
  'class-12-maths': {
    name: "CBSE Class 12 Mathematics Complete Package",
    level: "Class 12 CBSE",
    faqs: [
      {
        q: "What Class 12 Maths topics are available on SJ Maths?",
        a: "We cover all 13 chapters of CBSE Class 12 Mathematics including Calculus (Integration & Differentiation), Vectors & 3D Geometry, Matrices, Probability, and Linear Programming with detailed step-by-step solutions."
      },
      {
        q: "Are Class 12 PYQs with detailed step-by-step solutions provided?",
        a: "Yes, SJ Maths features chapter-wise authentic past board exam questions from 2014 to 2024 with detailed mark-wise breakdown."
      }
    ]
  },
  'sat': {
    name: "Digital SAT Math Practice & Concept Package",
    level: "Digital SAT / High School Entrance Exam",
    faqs: [
      {
        q: "What SAT Math prep materials are provided?",
        a: "SJ Maths offers Digital SAT Math practice sets covering Algebra, Advanced Math, Problem-Solving & Data Analysis, and Geometry & Trigonometry."
      },
      {
        q: "Does SJ Maths mirror the Digital SAT Math module format?",
        a: "Yes, our online SAT practice tests include Module 1 and Module 2 adaptive-level questions with timer controls and instant score feedback."
      }
    ]
  },
  'class-9-maths': {
    name: "CBSE Class 9 Mathematics Complete Study Guide",
    level: "Class 9 CBSE",
    faqs: [
      {
        q: "What chapters are included in Class 9 Maths?",
        a: "Number Systems, Polynomials, Coordinate Geometry, Linear Equations in Two Variables, Euclid's Geometry, Lines & Angles, Triangles, Quadrilaterals, Circles, Heron's Formula, and Statistics."
      }
    ]
  }
};

function buildBreadcrumbList(relPath) {
  const parts = relPath.split('/').filter(Boolean);
  if (parts.length > 0 && parts[parts.length - 1] === 'index.html') {
    parts.pop();
  }

  const items = [{ name: 'Home', url: `${BASE_URL}/` }];
  let currentAcc = '';

  for (const p of parts) {
    currentAcc += `/${p}`;
    const name = p.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
    items.push({ name, url: `${BASE_URL}${currentAcc}/` });
  }

  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": items.map((item, index) => ({
      "@type": "ListItem",
      "position": index + 1,
      "name": item.name,
      "item": item.url
    }))
  };
}

function findIndexHtmlFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    if (file === 'node_modules' || file === '.git' || file === 'scratch' || file === '.firebase') continue;
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory()) {
      results = results.concat(findIndexHtmlFiles(fullPath));
    } else if (file === 'index.html') {
      results.push(fullPath);
    }
  }
  return results;
}

const allIndexFiles = findIndexHtmlFiles(ROOT_DIR);
let count = 0;

allIndexFiles.forEach(absPath => {
  const relPath = path.relative(ROOT_DIR, absPath).replace(/\\/g, '/');
  let html = fs.readFileSync(absPath, 'utf8');

  // Strip previous auto-injected schema
  html = html.replace(/<script type="application\/ld\+json" data-seo-schema="true">[\s\S]*?<\/script>\n?/g, '');

  const schemas = [];

  // Organization & Website on root
  if (relPath === 'index.html') {
    schemas.push(ORG_SCHEMA);
    schemas.push(WEBSITE_SCHEMA);
  }

  // Breadcrumbs
  if (relPath !== 'index.html') {
    schemas.push(buildBreadcrumbList(relPath));
  }

  // Category FAQ & Learning Resource
  const topCategory = relPath.split('/')[0];
  const catData = CATEGORY_FAQS[topCategory];

  if (catData && relPath === `${topCategory}/index.html`) {
    schemas.push({
      "@context": "https://schema.org",
      "@type": "LearningResource",
      "name": catData.name,
      "learningResourceType": ["Notes", "Worksheet", "Practice Problems", "Quiz"],
      "educationalLevel": catData.level,
      "inLanguage": "en",
      "provider": {
        "@type": "Organization",
        "name": "SJ Maths"
      }
    });

    if (catData.faqs) {
      schemas.push({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": catData.faqs.map(f => ({
          "@type": "Question",
          "name": f.q,
          "acceptedAnswer": {
            "@type": "Answer",
            "text": f.a
          }
        }))
      });
    }
  }

  if (schemas.length > 0 && html.includes('</head>')) {
    const scriptBlocks = schemas.map(s =>
      `<script type="application/ld+json" data-seo-schema="true">\n${JSON.stringify(s, null, 2)}\n</script>`
    ).join('\n');

    html = html.replace('</head>', `${scriptBlocks}\n</head>`);
    fs.writeFileSync(absPath, html, 'utf8');
    count++;
  }
});

console.log(`Injected structured JSON-LD schemas into ${count} index.html pages.`);
