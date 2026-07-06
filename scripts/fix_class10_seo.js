const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..');
const CLASS10_DIR = path.join(ROOT_DIR, 'class-10-maths');

// Chapter mappings from flat .html to clean folder-based notes
const CHAPTER_MAPPINGS = [
  { flat: 'chapter-1-real-numbers.html', target: 'chapter-wise-notes/chapter-1-real-numbers/' },
  { flat: 'chapter-2-polynomials.html', target: 'chapter-wise-notes/chapter-2-polynomials/' },
  { flat: 'chapter-3-linear-equations.html', target: 'chapter-wise-notes/chapter-3-pair-of-linear-equations-in-two-variables/' },
  { flat: 'chapter-4-quadratic-equations.html', target: 'chapter-wise-notes/chapter-4-quadratic-equations/' },
  { flat: 'chapter-5-arithmetic-progressions.html', target: 'chapter-wise-notes/chapter-5-arithmetic-progressions/' },
  { flat: 'chapter-6-triangles.html', target: 'chapter-wise-notes/chapter-6-triangles/' },
  { flat: 'chapter-7-coordinate-geometry.html', target: 'chapter-wise-notes/chapter-7-coordinate-geometry/' },
  { flat: 'chapter-8-trigonometry.html', target: 'chapter-wise-notes/chapter-8-introduction-to-trigonometry/' },
  { flat: 'chapter-9-trigonometry-applications.html', target: 'chapter-wise-notes/chapter-9-applications-of-trigonometry/' },
  { flat: 'chapter-10-circles.html', target: 'chapter-wise-notes/chapter-10-circles/' },
  { flat: 'chapter-11-areas-circles.html', target: 'chapter-wise-notes/chapter-11-areas-related-to-circles/' },
  { flat: 'chapter-12-surface-areas-volumes.html', target: 'chapter-wise-notes/chapter-12-surface-areas-and-volumes/' },
  { flat: 'chapter-13-statistics.html', target: 'chapter-wise-notes/chapter-13-statistics/' },
  { flat: 'chapter-14-probability.html', target: 'chapter-wise-notes/chapter-14-probability/' },
];

function fixFlatFilesRedirects() {
  console.log('📌 Updating flat HTML chapter files to redirect to primary canonical URLs...');
  
  for (const item of CHAPTER_MAPPINGS) {
    const flatPath = path.join(CLASS10_DIR, item.flat);
    const targetUrl = `https://sjmaths.com/class-10-maths/${item.target}`;
    
    if (fs.existsSync(flatPath)) {
      const redirectHtml = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="${targetUrl}">
    <meta http-equiv="refresh" content="0; url=${targetUrl}">
    <title>Redirecting to Class 10 Maths Notes | SJMaths</title>
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

function fixClass10IndexDashboard() {
  console.log('📌 Updating class-10-maths/index.html internal links...');
  const indexPath = path.join(CLASS10_DIR, 'index.html');
  let content = fs.readFileSync(indexPath, 'utf8');

  // 1. Update Chapter Grid links
  for (const item of CHAPTER_MAPPINGS) {
    const oldHref = `/class-10-maths/${item.flat}`;
    const newHref = `/class-10-maths/${item.target}`;
    content = content.replaceAll(oldHref, newHref);
  }

  // 2. Fix Previous Years Papers redirect card to point to active PYQ hub
  content = content.replace(
    'href="/class-10-maths/previous-years-papers/"',
    'href="/class-10-maths/previous-year-questions/"'
  );

  // 3. Fix Additional Questions by CBSE card from href="#" to practice exercises
  content = content.replace(
    '<a href="#" class="feature-card">',
    '<a href="/class-10-maths/ncert-exercise-practice/" class="feature-card">'
  );

  fs.writeFileSync(indexPath, content, 'utf8');
  console.log('  ✓ Fixed internal links in class-10-maths/index.html');
}

function updateFirebaseRedirects() {
  console.log('📌 Updating firebase.json 301 redirects...');
  const firebasePath = path.join(ROOT_DIR, 'firebase.json');
  const firebaseData = JSON.parse(fs.readFileSync(firebasePath, 'utf8'));

  if (!firebaseData.hosting.redirects) {
    firebaseData.hosting.redirects = [];
  }

  const existingSources = new Set(firebaseData.hosting.redirects.map(r => r.source));

  let addedCount = 0;
  for (const item of CHAPTER_MAPPINGS) {
    const source = `/class-10-maths/${item.flat}`;
    const destination = `/class-10-maths/${item.target}`;

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
  fixFlatFilesRedirects();
  fixClass10IndexDashboard();
  updateFirebaseRedirects();
}

run();
