const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS9_DIR = path.join(ROOT_DIR, 'class-9-maths');
const CLASS11_DIR = path.join(ROOT_DIR, 'class-11-maths');

const CLASS9_MAPPINGS = [
  { flat: 'chapter-1-use-of-coordinates.html', target: 'chapter-wise-notes/chapter-1-use-of-coordinates/' },
  { flat: 'chapter-2-polynomials.html', target: 'chapter-wise-notes/chapter-2-linear-polynomials/' },
  { flat: 'chapter-3-coordinate-geometry.html', target: 'chapter-wise-notes/chapter-3-world-of-numbers/' },
  { flat: 'chapter-4-linear-equations-in-two-variables.html', target: 'chapter-wise-notes/chapter-4-algebraic-identities/' },
  { flat: 'chapter-5-introduction-to-euclids-geometry.html', target: 'chapter-wise-notes/chapter-5-circles/' },
  { flat: 'chapter-5-euclids-geometry.html', target: 'chapter-wise-notes/chapter-5-circles/' },
  { flat: 'chapter-6-lines-and-angles.html', target: 'chapter-wise-notes/chapter-6-perimeter-and-area/' },
  { flat: 'chapter-7-triangles.html', target: 'chapter-wise-notes/chapter-7-probability/' },
  { flat: 'chapter-8-quadrilaterals.html', target: 'chapter-wise-notes/chapter-8-sequences-and-progressions/' },
  { flat: 'chapter-9-circles.html', target: 'chapter-wise-notes/chapter-9-triangles/' },
  { flat: 'chapter-10-herons-formula.html', target: 'chapter-wise-notes/chapter-10-herons-formula/' },
  { flat: 'chapter-11-surface-areas-and-volumes.html', target: 'chapter-wise-notes/chapter-11-surface-areas-and-volumes/' },
  { flat: 'chapter-12-statistics.html', target: 'chapter-wise-notes/chapter-12-statistics/' },
];

const CLASS11_MAPPINGS = [
  { flat: 'chapter-1-sets.html', target: 'chapter-wise-notes/chapter-1-sets/' },
  { flat: 'chapter-2-relations-functions.html', target: 'chapter-wise-notes/chapter-2-relations-and-functions/' },
  { flat: 'chapter-3-trigonometric-functions.html', target: 'chapter-wise-notes/chapter-3-trigonometric-functions/' },
  { flat: 'chapter-4-complex-numbers-and-quadratic-equations.html', target: 'chapter-wise-notes/chapter-4-complex-numbers-and-quadratic-equations/' },
  { flat: 'chapter-5-linear-inequalities.html', target: 'chapter-wise-notes/chapter-5-linear-inequalities/' },
  { flat: 'chapter-6-permutations-and-combinations.html', target: 'chapter-wise-notes/chapter-6-permutations-and-combinations/' },
  { flat: 'chapter-7-binomial-theorem.html', target: 'chapter-wise-notes/chapter-7-binomial-theorem/' },
  { flat: 'chapter-8-sequences-and-series.html', target: 'chapter-wise-notes/chapter-8-sequences-and-series/' },
  { flat: 'chapter-9-straight-lines.html', target: 'chapter-wise-notes/chapter-9-straight-lines/' },
  { flat: 'chapter-10-conic-sections.html', target: 'chapter-wise-notes/chapter-10-conic-sections/' },
  { flat: 'chapter-11-three-dimensional-geometry.html', target: 'chapter-wise-notes/chapter-11-introduction-to-three-dimensional-geometry/' },
  { flat: 'chapter-12-limits-and-derivatives.html', target: 'chapter-wise-notes/chapter-12-limits-and-derivatives/' },
  { flat: 'chapter-13-statistics.html', target: 'chapter-wise-notes/chapter-13-statistics/' },
  { flat: 'chapter-14-probability.html', target: 'chapter-wise-notes/chapter-14-probability/' },
];

function processClass(classNum, classDir, mappings) {
  console.log(`📌 Updating Class ${classNum} flat HTML chapter files to redirect...`);
  
  for (const item of mappings) {
    const flatPath = path.join(classDir, item.flat);
    const targetUrl = `https://sjmaths.com/class-${classNum}-maths/${item.target}`;
    
    if (fs.existsSync(flatPath)) {
      const redirectHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="${targetUrl}">
    <meta http-equiv="refresh" content="0; url=${targetUrl}">
    <title>Redirecting to Class ${classNum} Maths Notes | SJMaths</title>
</head>
<body>
    <p>Redirecting to <a href="${targetUrl}">${targetUrl}</a>...</p>
    <script>window.location.replace('${targetUrl}');</script>
</body>
</html>`;
      fs.writeFileSync(flatPath, redirectHtml, 'utf8');
      console.log(`  ✓ Updated redirect & canonical for ${item.flat} -> ${item.target}`);
    }
  }

  // Update Index dashboard links
  const indexPath = path.join(classDir, 'index.html');
  if (fs.existsSync(indexPath)) {
    let content = fs.readFileSync(indexPath, 'utf8');
    for (const item of mappings) {
      const oldHref = `/class-${classNum}-maths/${item.flat}`;
      const newHref = `/class-${classNum}-maths/${item.target}`;
      content = content.replaceAll(oldHref, newHref);
    }
    // Fix any href="#" links in dashboard
    content = content.replace('<a href="#" class="feature-card">\n      <span class="card-badge badge-board card-badge-absolute">Coming Soon</span>', '<a href="/class-9-maths/chapter-mastery/" class="feature-card">\n      <span class="card-badge badge-board card-badge-absolute">Coming Soon</span>');
    fs.writeFileSync(indexPath, content, 'utf8');
    console.log(`  ✓ Fixed internal links in class-${classNum}-maths/index.html`);
  }
}

function updateFirebaseRedirects() {
  console.log('📌 Updating firebase.json 301 redirects for Class 9 & Class 11...');
  const firebasePath = path.join(ROOT_DIR, 'firebase.json');
  const firebaseData = JSON.parse(fs.readFileSync(firebasePath, 'utf8'));

  if (!firebaseData.hosting.redirects) {
    firebaseData.hosting.redirects = [];
  }

  const existingSources = new Set(firebaseData.hosting.redirects.map(r => r.source));

  let addedCount = 0;
  const allMappings = [
    ...CLASS9_MAPPINGS.map(m => ({ ...m, classNum: 9 })),
    ...CLASS11_MAPPINGS.map(m => ({ ...m, classNum: 11 }))
  ];

  for (const item of allMappings) {
    const source = `/class-${item.classNum}-maths/${item.flat}`;
    const destination = `/class-${item.classNum}-maths/${item.target}`;

    if (!existingSources.has(source)) {
      firebaseData.hosting.redirects.unshift({
        source: source,
        destination: destination,
        type: 301
      });
      addedCount++;
    }
  }

  if (addedCount > 0) {
    fs.writeFileSync(firebasePath, JSON.stringify(firebaseData, null, 2), 'utf8');
    console.log(`  ✓ Added ${addedCount} 301 redirects to firebase.json`);
  } else {
    console.log('  ✓ firebase.json 301 redirects are already up to date.');
  }
}

function run() {
  processClass(9, CLASS9_DIR, CLASS9_MAPPINGS);
  processClass(11, CLASS11_DIR, CLASS11_MAPPINGS);
  updateFirebaseRedirects();
}

run();
