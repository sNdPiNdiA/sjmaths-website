const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS12_DIR = path.join(ROOT_DIR, 'class-12-maths');

// Chapter mappings from flat .html to clean folder-based notes
const CHAPTER_MAPPINGS = [
  { flat: 'chapter-1-relations-and-functions.html', target: 'chapter-wise-notes/chapter-1-relations-and-functions/' },
  { flat: 'chapter-2-inverse-trigonometric-functions.html', target: 'chapter-wise-notes/chapter-2-inverse-trigonometric-functions/' },
  { flat: 'chapter-3-matrices.html', target: 'chapter-wise-notes/chapter-3-matrices/' },
  { flat: 'chapter-4-determinants.html', target: 'chapter-wise-notes/chapter-4-determinants/' },
  { flat: 'chapter-5-continuity-and-differentiability.html', target: 'chapter-wise-notes/chapter-5-continuity-and-differentiability/' },
  { flat: 'chapter-6-applications-of-derivatives.html', target: 'chapter-wise-notes/chapter-6-applications-of-derivatives/' },
  { flat: 'chapter-7-integrals.html', target: 'chapter-wise-notes/chapter-7-integrals/' },
  { flat: 'chapter-8-applications-of-integrals.html', target: 'chapter-wise-notes/chapter-8-applications-of-integrals/' },
  { flat: 'chapter-9-differential-equations.html', target: 'chapter-wise-notes/chapter-9-differential-equations/' },
  { flat: 'chapter-10-vector-algebra.html', target: 'chapter-wise-notes/chapter-10-vector-algebra/' },
  { flat: 'chapter-11-three-dimensional-geometry.html', target: 'chapter-wise-notes/chapter-11-three-dimensional-geometry/' },
  { flat: 'chapter-12-linear-programming.html', target: 'chapter-wise-notes/chapter-12-linear-programming/' },
  { flat: 'chapter-13-probability.html', target: 'chapter-wise-notes/chapter-13-probability/' },
];

function fixFlatFilesRedirects() {
  console.log('📌 Updating Class 12 flat HTML chapter files to redirect to primary canonical URLs...');
  
  for (const item of CHAPTER_MAPPINGS) {
    const flatPath = path.join(CLASS12_DIR, item.flat);
    const targetUrl = `https://sjmaths.com/class-12-maths/${item.target}`;
    
    if (fs.existsSync(flatPath)) {
      const redirectHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="${targetUrl}">
    <meta http-equiv="refresh" content="0; url=${targetUrl}">
    <title>Redirecting to Class 12 Maths Notes | SJMaths</title>
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
}

function fixClass12IndexDashboard() {
  console.log('📌 Updating class-12-maths/index.html internal links...');
  const indexPath = path.join(CLASS12_DIR, 'index.html');
  let content = fs.readFileSync(indexPath, 'utf8');

  // 1. Update Chapter Grid links
  for (const item of CHAPTER_MAPPINGS) {
    const oldHref = `/class-12-maths/${item.flat}`;
    const newHref = `/class-12-maths/${item.target}`;
    content = content.replaceAll(oldHref, newHref);
  }

  // 2. Fix Sample Papers href="#" -> sample-papers/
  content = content.replace(
    '<h2>Sample Papers</h2>',
    '<h2>Sample Papers</h2>'
  );
  content = content.replace(
    '<a href="#" class="feature-card">\n            <div class="f-icon"><i class="fas fa-file-contract"></i></div>\n            <h2>Sample Papers</h2>',
    '<a href="sample-papers/" class="feature-card">\n            <div class="f-icon"><i class="fas fa-file-contract"></i></div>\n            <h2>Sample Papers</h2>'
  );

  // 3. Fix Full PYPs href="#" -> previous-years-papers/
  content = content.replace(
    '<a href="#" class="feature-card">\n            <div class="f-icon"><i class="fas fa-history"></i></div>\n            <h2>Full PYPs</h2>',
    '<a href="previous-years-papers/" class="feature-card">\n            <div class="f-icon"><i class="fas fa-history"></i></div>\n            <h2>Full PYPs</h2>'
  );

  // 4. Fix Additional Questions by CBSE card href="#" -> ncert-exercise-practice/
  content = content.replace(
    '<a href="#" class="feature-card">\n            <span class="card-badge"',
    '<a href="ncert-exercise-practice/" class="feature-card">\n            <span class="card-badge"'
  );

  fs.writeFileSync(indexPath, content, 'utf8');
  console.log('  ✓ Fixed internal links in class-12-maths/index.html');
}

function updateFirebaseRedirects() {
  console.log('📌 Updating firebase.json 301 redirects for Class 12...');
  const firebasePath = path.join(ROOT_DIR, 'firebase.json');
  const firebaseData = JSON.parse(fs.readFileSync(firebasePath, 'utf8'));

  if (!firebaseData.hosting.redirects) {
    firebaseData.hosting.redirects = [];
  }

  const existingSources = new Set(firebaseData.hosting.redirects.map(r => r.source));

  let addedCount = 0;
  for (const item of CHAPTER_MAPPINGS) {
    const source = `/class-12-maths/${item.flat}`;
    const destination = `/class-12-maths/${item.target}`;

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

function cleanupClass12JunkFiles() {
  console.log('📌 Cleaning up junk / duplicate files in class-12-maths...');
  const junkFiles = [
    'chapter-6-data-utf8.json',
    'minify.js',
    'search.js',
    'user-profile.js'
  ];

  for (const file of junkFiles) {
    const filePath = path.join(CLASS12_DIR, file);
    if (fs.existsSync(filePath)) {
      fs.unlinkSync(filePath);
      console.log(`  ✓ Deleted ${file}`);
    }
  }
}

function run() {
  fixFlatFilesRedirects();
  fixClass12IndexDashboard();
  updateFirebaseRedirects();
  cleanupClass12JunkFiles();
}

run();
