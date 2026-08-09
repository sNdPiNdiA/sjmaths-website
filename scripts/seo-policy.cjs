const path = require('path');

const DOMAIN = 'https://sjmaths.com';

const SITEMAP_GROUPS = {
  'class-9-maths/': 'sitemap-class-9.xml',
  'class-10-maths/': 'sitemap-class-10.xml',
  'class-11-maths/': 'sitemap-class-11.xml',
  'class-11-applied-mathematics/': 'sitemap-class-11-applied-mathematics.xml',
  'class-12-maths/': 'sitemap-class-12.xml',
  'ahc-ro-aro/': 'sitemap-ahc-ro-aro.xml',
  'upsc/': 'sitemap-upsc.xml',
  'ssc-cgl/': 'sitemap-ssc-cgl.xml',
  'upsssc-lower-mains/': 'sitemap-upsssc-lower-mains.xml',
  'up-assistant-teacher/': 'sitemap-up-assistant-teacher.xml',
};

const SITEMAP_ORDER = [
  'sitemap-main.xml',
  'sitemap-class-9.xml',
  'sitemap-class-10.xml',
  'sitemap-class-11.xml',
  'sitemap-class-11-applied-mathematics.xml',
  'sitemap-class-12.xml',
  'sitemap-ahc-ro-aro.xml',
  'sitemap-upsc.xml',
  'sitemap-ssc-cgl.xml',
  'sitemap-upsssc-lower-mains.xml',
  'sitemap-up-assistant-teacher.xml',
];

const SKIPPED_DIRS = new Set([
  '.git',
  '.firebase',
  '.vscode',
  'assets',
  'components',
  'dataconnect',
  'digital-evaluation',
  'node_modules',
  'questions-module',
  'scripts',
  'src',
  'utils',
]);

const FORCE_NOINDEX_PATHS = new Set([
  '404.html',
  'dashboard.html',
  'login.html',
  'my-submissions.html',
  'notifications.html',
  'offline.html',
  'profile.html',
  'search.html',
  'settings.html',
  'signup.html',
  'teacher-dashboard.html',
  'pages/admin.html',
  'pages/coming-soon.html',
  'pages/manage-content.html',
  'pages/settings.html',
  'class-12-maths/ncert-exercise-practice/chapter-10-vector-algebra/exercise-2.html',
  'class-9-maths/tests/chapter-wise/chapter-1-number-system/test-2.html',
  'class-11-maths/tests/unit-wise/unit-6-probability/index.html',
  'class-11-maths/tests/unit-wise/unit-6-probability/test-1.html',
  'class-11-maths/tests/unit-wise/unit-6-probability/test-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-10-vector-algebra/exercise-3.html',
  'class-12-maths/tests/unit-wise/unit-1-relations-and-functions/index.html',
  'class-12-maths/tests/unit-wise/unit-1-relations-and-functions/test-1.html',
  'class-12-maths/tests/unit-wise/unit-1-relations-and-functions/test-2.html',
  'class-12-maths/sample-papers/set1.html',
  'class-12-maths/sample-papers/set2.html',
  'class-12-maths/sample-papers/set3.html',
  'class-12-maths/sample-papers/set4.html',
  'class-12-maths/sample-papers/set5.html',
  'class-12-maths/sample-papers/set6.html',
  'class-12-maths/sample-papers/set7.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-5-continuity-and-differentiability/derivative-formulae.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-7-integrals/standard-integrals.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-8-applications-of-integrals/area-under-curves.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-9-differential-equations/solution-of-differential-equations.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-11-three-dimensional-geometry/index.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-12-linear-programming/index.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-13-probability/index.html',
]);

const FORCE_NOINDEX_BASENAMES = new Set([
  'final-evaluation.html',
  'free-evaluation.html',
  'paid-evaluation.html',
  'performance-dashboard.html',
]);

const CORE_INDEX_PATHS = new Set([
  'index.html',
  'important-questions.html',
  'pages/about.html',
  'pages/class-10-maths-formula-concept-bible.html',
  'pages/class-11-maths-formula-bible.html',
  'pages/class-12-maths-formula-bible.html',
  'pages/class-9-maths-formula-concept-bible.html',
  'pages/contact.html',
  'pages/cookie-policy.html',
  'pages/disclaimer.html',
  'pages/ebooks.html',
  'pages/faq.html',
  'pages/pricing.html',
  'pages/privacy-policy.html',
  'pages/index.html',
  'pages/support.html',
  'pages/terms.html',
  'maths-mastery/index.html',
  'upsssc-lower-mains/index.html',
  'up-assistant-teacher/index.html',
  'current-affairs/index.html',
  'current-affairs/weekly/index.html',
  'current-affairs/bimonthly/index.html',
  'current-affairs/monthly/index.html',
  'maths-mastery/algebra/index.html',
  'ssc-cgl/syllabus/index.html',
  'ssc-cgl/quantitative-aptitude/index.html',
  'ssc-cgl/reasoning/index.html',
  'ssc-cgl/english/index.html',
  'ssc-cgl/general-awareness/index.html',
  'ssc-cgl/computer-knowledge/index.html',
  'ssc-cgl/statistics/index.html',
  'ssc-cgl/finance-economics/index.html',
  'maths-mastery/arithmetic/index.html',
  'maths-mastery/arithmetic/topics/fractions/index.html',
  'maths-mastery/calculus/index.html',
  'maths-mastery/coordinate-geometry/index.html',
  'maths-mastery/geometry/index.html',
  'maths-mastery/trigonometry/index.html',
  'maths-mastery/vectors-3d/index.html',
]);

const STRONG_NCERT_EXERCISE_INDEX_PATHS = new Set([
  'class-9-maths/ncert-exercise-practice/chapter-2-polynomials/exercise-2-4.html',
  'class-9-maths/ncert-exercise-practice/chapter-9-triangles/exercise-9-3.html',
  'class-10-maths/ncert-exercise-practice/chapter-11-areas-related-to-circles/exercise-11-1.html',
  'class-10-maths/ncert-exercise-practice/chapter-14-probability/exercise-14-1.html',
  'class-12-maths/ncert-exercise-practice/chapter-1-relations-and-functions/exercise-1-1.html',
  'class-12-maths/ncert-exercise-practice/chapter-1-relations-and-functions/exercise-1-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-10-vector-algebra/exercise-10-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-10-vector-algebra/exercise-10-3.html',
  'class-12-maths/ncert-exercise-practice/chapter-10-vector-algebra/misc-exercise.html',
  'class-12-maths/ncert-exercise-practice/chapter-11-three-dimensional-geometry/exercise-11-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-13-probability/exercise-13-1.html',
  'class-12-maths/ncert-exercise-practice/chapter-13-probability/exercise-13-3.html',
  'class-12-maths/ncert-exercise-practice/chapter-13-probability/misc-exercise.html',
  'class-12-maths/ncert-exercise-practice/chapter-2-inverse-trigonometric-functions/exercise-2-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-3-matrices/exercise-3-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-3-matrices/exercise-3-3.html',
  'class-12-maths/ncert-exercise-practice/chapter-3-matrices/misc-exercise.html',
  'class-12-maths/ncert-exercise-practice/chapter-4-determinants/exercise-4-4.html',
  'class-12-maths/ncert-exercise-practice/chapter-5-continuity-and-differentiability/exercise-5-1.html',
  'class-12-maths/ncert-exercise-practice/chapter-6-applications-of-derivatives/exercise-6-1.html',
  'class-12-maths/ncert-exercise-practice/chapter-6-applications-of-derivatives/exercise-6-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-6-applications-of-derivatives/exercise-6-3.html',
  'class-12-maths/ncert-exercise-practice/chapter-7-integrals/exercise-7-2.html',
  'class-12-maths/ncert-exercise-practice/chapter-7-integrals/exercise-7-6.html',
  'class-12-maths/ncert-exercise-practice/chapter-7-integrals/exercise-7-8.html',
  'class-12-maths/ncert-exercise-practice/chapter-7-integrals/misc-exercise.html',
  'class-12-maths/ncert-exercise-practice/chapter-8-applications-of-integrals/misc-exercise.html',
  'class-12-maths/ncert-exercise-practice/chapter-9-differential-equations/exercise-9-3.html',
  'class-12-maths/ncert-exercise-practice/chapter-9-differential-equations/exercise-9-5.html',
]);

const QUESTIONS_MODULE_RENDERED_INDEX_PATHS = new Set([
  'class-10-maths/previous-year-questions/chapter-4-quadratic-equations/nature-of-roots.html',
  'class-10-maths/previous-year-questions/chapter-4-quadratic-equations/quadratic-formula.html',
  'class-10-maths/previous-year-questions/chapter-4-quadratic-equations/solving-by-factorisation.html',
  'class-10-maths/previous-year-questions/chapter-4-quadratic-equations/word-problems.html',
  'class-10-maths/previous-year-questions/chapter-5-arithmetic-progressions/nth-term.html',
  'class-10-maths/previous-year-questions/chapter-5-arithmetic-progressions/sum-of-n-terms.html',
  'class-10-maths/previous-year-questions/chapter-5-arithmetic-progressions/word-problems.html',
  'class-10-maths/previous-year-questions/chapter-6-triangles/basic-proportionality-theorem.html',
  'class-10-maths/previous-year-questions/chapter-6-triangles/pythagoras-theorem.html',
  'class-10-maths/previous-year-questions/chapter-6-triangles/similar-triangles.html',
  'class-10-maths/previous-year-questions/chapter-7-coordinate-geometry/distance-formula.html',
  'class-10-maths/previous-year-questions/chapter-7-coordinate-geometry/section-formula.html',
  'class-10-maths/previous-year-questions/chapter-8-introduction-to-trigonometry/trigonometric-identities.html',
  'class-10-maths/previous-year-questions/chapter-8-introduction-to-trigonometry/trigonometric-ratios.html',
  'class-10-maths/previous-year-questions/chapter-8-introduction-to-trigonometry/values-of-trigonometric-ratios.html',
  'class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-3.html',
  'class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-4.html',
  'class-11-maths/ncert-exercise-practice/chapter-1-sets/exercise-1-5.html',
  'class-11-maths/ncert-exercise-practice/chapter-1-sets/misc-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-3.html',
  'class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/exercise-10-4.html',
  'class-11-maths/ncert-exercise-practice/chapter-10-conic-sections/miscellaneous-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-11-introduction-to-three-dimensional-geometry/exercise-11-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-11-introduction-to-three-dimensional-geometry/exercise-11-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-11-introduction-to-three-dimensional-geometry/miscellaneous-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-12-limits-and-derivatives/exercise-12-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-12-limits-and-derivatives/exercise-12-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-13-statistics/exercise-13-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-13-statistics/exercise-13-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-14-probability/exercise-14-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-14-probability/exercise-14-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/exercise-2-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/exercise-2-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/exercise-2-3.html',
  'class-11-maths/ncert-exercise-practice/chapter-2-relations-and-functions/misc-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/exercise-3-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/exercise-3-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/exercise-3-3.html',
  'class-11-maths/ncert-exercise-practice/chapter-3-trigonometric-functions/misc-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-4-complex-numbers-and-quadratic-equations/exercise-4-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-4-complex-numbers-and-quadratic-equations/exercise-4-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-5-linear-inequalities/exercise-5-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-5-linear-inequalities/miscellaneous-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-3.html',
  'class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/exercise-6-4.html',
  'class-11-maths/ncert-exercise-practice/chapter-6-permutations-and-combinations/miscellaneous-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-7-binomial-theorem/exercise-7-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-7-binomial-theorem/miscellaneous-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-8-sequences-and-series/exercise-8-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-8-sequences-and-series/exercise-8-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-8-sequences-and-series/miscellaneous-exercise.html',
  'class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/exercise-9-1.html',
  'class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/exercise-9-2.html',
  'class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/exercise-9-3.html',
  'class-11-maths/ncert-exercise-practice/chapter-9-straight-lines/miscellaneous-exercise.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-1-relations-and-functions/one-one-onto-functions.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-1-relations-and-functions/types-of-relations.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-2-inverse-trigonometric-functions/principal-values.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-2-inverse-trigonometric-functions/properties-of-inverse-trigonometric-functions.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-2-inverse-trigonometric-functions/simplification-of-itf.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-3-matrices/operations-on-matrices.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-3-matrices/symmetric-and-skew-symmetric.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-3-matrices/transpose-of-matrix.html',
  'class-12-maths/previous-years-questions-chapter-wise/chapter-3-matrices/types-of-matrices.html',
]);

const EXCLUDED_INTERACTIVE_CHAPTER_PATHS = new Set([
  'class-9-maths/chapter-5-introduction-to-euclids-geometry.html',
]);

const HIDDEN_PATH_PATTERN = /(^|\/)[._][^/]+/;
const NOINDEX_PATTERN = /<meta\b(?=[^>]*\bname=["']robots["'])(?=[^>]*\bcontent=["'][^"']*\bnoindex\b)[^>]*>/i;
const LOGIN_REDIRECT_PATTERN =
  /(?:window\.)?location\.(?:href|replace)\s*=\s*["'][^"']*login\.html["']/i;
const CLIENT_REDIRECT_PATTERN =
  /(?:window\.)?location\.(?:href|replace)\s*=\s*["'][^"']+["']|<meta[^>]+http-equiv=["']refresh["']/i;
const TITLE_PATTERN = /<title>\s*[^<]+\s*<\/title>/i;
const DESCRIPTION_PATTERN = /<meta\b(?=[^>]*\bname=["']description["'])(?=[^>]*\bcontent=["']([^"']+)["'])[^>]*>/i;

function shouldSkipDir(dirName) {
  return SKIPPED_DIRS.has(dirName) || dirName.startsWith('.');
}

function normalizePath(filePath, rootDir) {
  return path.relative(rootDir, filePath).split(path.sep).join('/');
}

function encodeUrlPath(relativePath) {
  return relativePath
    .split('/')
    .map((segment) => encodeURIComponent(segment))
    .join('/');
}

function toUrl(relativePath, domain = DOMAIN) {
  let urlPath = relativePath.replace(/^classes\/class-(9|10|11|12)\//, 'class-$1-maths/');

  if (urlPath === 'index.html') {
    return `${domain}/`;
  }

  if (urlPath.endsWith('/index.html')) {
    const dirPath = urlPath.slice(0, -'index.html'.length);
    return `${domain}/${encodeUrlPath(dirPath)}`;
  }

  return `${domain}/${encodeUrlPath(urlPath)}`;
}

function toLocalUrl(relativePath) {
  const absoluteUrl = toUrl(relativePath);
  return absoluteUrl.replace(DOMAIN, '') || '/';
}

function getSitemapName(relativePath) {
  for (const [prefix, fileName] of Object.entries(SITEMAP_GROUPS)) {
    if (relativePath.startsWith(prefix)) {
      return fileName;
    }
  }

  return 'sitemap-main.xml';
}

function getPriority(url) {
  if (url === `${DOMAIN}/`) {
    return '1.0';
  }

  if (/^https:\/\/sjmaths\.com\/(?:class-(?:9|10|11|12)-maths|class-11-applied-mathematics|maths-mastery)\/$/.test(url)) {
    return '0.9';
  }

  if (/\/chapter-wise-notes\/chapter-[^/]+\/$/.test(url)) {
    return '0.7';
  }

  return '0.8';
}

function getChangefreq(url) {
  if (url === `${DOMAIN}/`) {
    return 'weekly';
  }

  if (/^https:\/\/sjmaths\.com\/(?:class-(?:9|10|11|12)-maths|class-11-applied-mathematics|maths-mastery)\/$/.test(url)) {
    return 'weekly';
  }

  return 'monthly';
}

function isManagedHtmlPath(relativePath) {
  return (
    relativePath.endsWith('.html') &&
    !HIDDEN_PATH_PATTERN.test(relativePath) &&
    !relativePath.split('/').some((segment) => SKIPPED_DIRS.has(segment))
  );
}

function isForcedNoindexPath(relativePath) {
  return (
    FORCE_NOINDEX_PATHS.has(relativePath) ||
    FORCE_NOINDEX_BASENAMES.has(path.posix.basename(relativePath))
  );
}

function isHighConfidenceIndexPath(relativePath) {
  if (!isManagedHtmlPath(relativePath) || isForcedNoindexPath(relativePath)) {
    return false;
  }

  if (CORE_INDEX_PATHS.has(relativePath)) {
    return true;
  }

  if (STRONG_NCERT_EXERCISE_INDEX_PATHS.has(relativePath)) {
    return true;
  }

  if (QUESTIONS_MODULE_RENDERED_INDEX_PATHS.has(relativePath)) {
    return true;
  }

  if (/^class-(?:9|10|11|12)-maths\/index\.html$/.test(relativePath)) {
    return true;
  }

  if (/^class-11-applied-mathematics\/index\.html$/.test(relativePath)) {
    return true;
  }

  if (/^class-11-applied-mathematics\/[^/]+\/index\.html$/.test(relativePath)) {
    return true;
  }

  if (/^class-11-applied-mathematics\/[^/]+\/[^/]+\/index\.html$/.test(relativePath)) {
    return true;
  }

  if (/^class-(?:9|10|11|12)-maths\/chapter-wise-notes\/index\.html$/.test(relativePath)) {
    return true;
  }

  if (/^class-(?:9|10|11|12)-maths\/chapter-wise-notes\/chapter-[^/]+\/index\.html$/.test(relativePath)) {
    return true;
  }

  if (
    /^class-(?:9|10|11|12)-maths\/(?:chapter-mastery|full-length-test-papers|ncert-exemplar-practice|ncert-exercise-practice|previous-year-questions|previous-years-questions-chapter-wise|sample-papers|tests|worksheets)\/index\.html$/.test(
      relativePath
    )
  ) {
    return true;
  }

  if (/^class-10-maths\/previous-year-questions\/chapter-wise\/index\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 10 NCERT exercise practice detail pages
  if (/^class-10-maths\/ncert-exercise-practice\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 10 Worksheet detail pages
  if (/^class-10-maths\/worksheets\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 10 Chapter-wise Test detail pages (excluding index.html)
  if (/^class-10-maths\/tests\/chapter-wise\/chapter-[^/]+\/(?!index\.html).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 12 NCERT exercise practice detail pages (excluding index.html and stray short-named exercise stubs)
  if (/^class-12-maths\/ncert-exercise-practice\/chapter-[^/]+\/(?!index\.html|exercise-\d+\.html).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 12 PYQ topic detail pages
  if (/^class-12-maths\/previous-years-questions-chapter-wise\/chapter-wise\/chapter-[^/]+\/(?!index\.html).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 12 Test detail pages (excluding index.html and unit-1 test placeholders)
  if (/^class-12-maths\/tests\/(?:chapter-wise|unit-wise|full-length-tests)(?:\/chapter-[^/]+|\/unit-[^/]+)?\/(?!index\.html|test-\d+\.html).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 12 Sample Paper detail pages (excluding index.html and set stubs)
  if (/^class-12-maths\/sample-papers\/(?!index\.html|set\d+\.html).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 11 NCERT exercise practice detail pages
  if (/^class-11-maths\/ncert-exercise-practice\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 11 NCERT exemplar practice detail pages
  if (/^class-11-maths\/ncert-exemplar-practice\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 11 Worksheet detail pages
  if (/^class-11-maths\/worksheets\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 11 Test detail pages (excluding index.html)
  if (/^class-11-maths\/tests\/(?:chapter-wise|unit-wise|full-length-tests)(?:\/chapter-[^/]+|\/unit-[^/]+)?\/(?!index\.html).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 9 NCERT exercise practice detail pages
  if (/^class-9-maths\/ncert-exercise-practice\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 9 Worksheet detail pages
  if (/^class-9-maths\/worksheets\/chapter-[^/]+\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include Class 9 Test detail pages (excluding index.html)
  if (/^class-9-maths\/tests\/(?!.*index\.html)(?:chapter-wise|unit-wise|full-length-tests).+\.html$/.test(relativePath)) {
    return true;
  }

  // Include all Chapter-wise PYQ topic pages and their hubs (Chapter 1 to 15)
  if (
    /^class-10-maths\/previous-year-questions\/chapter-wise\/chapter-(?:[1-9]|1[0-5])-.+\/.+\.html$/.test(relativePath)
  ) {
    return true;
  }

  // Include all SSC CGL topic detail pages
  if (/^ssc-cgl\/[^/]+\/[^/]+\/index\.html$/.test(relativePath)) {
    return true;
  }

  // Include all UPSC topic and subtopic detail pages
  if (/^upsc\/.+\.html$/.test(relativePath)) {
    return true;
  }

  // Include all AHC RO/ARO pages
  if (relativePath.startsWith('ahc-ro-aro/') && relativePath.endsWith('index.html')) {
    return true;
  }

  // Include all UPSC pages
  if (relativePath.startsWith('upsc/') && relativePath.endsWith('index.html')) {
    return true;
  }

  // Include all SSC CGL pages
  if (relativePath.startsWith('ssc-cgl/') && relativePath.endsWith('index.html')) {
    return true;
  }

  // Include all UPSSSC Lower Mains pages
  if (relativePath.startsWith('upsssc-lower-mains/') && relativePath.endsWith('.html')) {
    return true;
  }

  // Include all UP Assistant Teacher pages
  if (relativePath.startsWith('up-assistant-teacher/') && relativePath.endsWith('.html')) {
    return true;
  }

  return false;
}

function hasNoindex(content) {
  return NOINDEX_PATTERN.test(content);
}

function hasRedirect(content) {
  return LOGIN_REDIRECT_PATTERN.test(content) || CLIENT_REDIRECT_PATTERN.test(content);
}

function hasTitle(content) {
  return TITLE_PATTERN.test(content);
}

function hasDescription(content) {
  return DESCRIPTION_PATTERN.test(content);
}

function isSitemapEligibleHtml(relativePath, content) {
  return (
    isHighConfidenceIndexPath(relativePath) &&
    Boolean(content.trim()) &&
    !hasNoindex(content) &&
    !hasRedirect(content) &&
    hasTitle(content) &&
    hasDescription(content)
  );
}

module.exports = {
  DOMAIN,
  SITEMAP_ORDER,
  shouldSkipDir,
  normalizePath,
  toUrl,
  toLocalUrl,
  getSitemapName,
  getPriority,
  getChangefreq,
  isManagedHtmlPath,
  isForcedNoindexPath,
  isHighConfidenceIndexPath,
  isSitemapEligibleHtml,
  hasNoindex,
  hasRedirect,
  hasTitle,
  hasDescription,
};