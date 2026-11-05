const fs = require('fs');
const path = require('path');

const ch9 = require('./data_chapter_9.cjs');
const ch13 = require('./data_chapter_13.cjs');
const ch14 = require('./data_chapter_14.cjs');

const chapters = [ch9, ch13, ch14];

function renderMCQCard(q, idx) {
  const optionsHtml = q.options.map((opt, optIdx) => {
    const val = String.fromCharCode(97 + optIdx); // a, b, c, d
    return `<li>
            <label class="mcq-label">
                <input type="radio" name="${q.id}" value="${val}">
                <span class="opt-text">${opt}</span>
            </label>
        </li>`;
  }).join('');

  const stepsHtml = q.solutionSteps.map(step => {
    return `<div class="step-item"><i class="fas fa-angle-right"></i> <span>${step}</span></div>`;
  }).join('');

  return `<div class="question-card" data-qid="${q.id}">
                    <div class="q-header">
                        <span class="q-badge">Q${idx + 1}</span>
                    </div>
                    <div class="q-text">${q.question}</div>
                <ul class="mcq-options">${optionsHtml}</ul>
                        <div class="solution-container">
                            <button class="solution-toggle-btn" onclick="toggleSolution('${q.id}')">
                                <i class="fas fa-eye"></i> Show Solution
                            </button>
                            <div id="sol-${q.id}" class="solution-content" style="display: none;">
                    <div class="solution-steps">${stepsHtml}</div><div class="final-answer">${q.answer}</div>
                            </div>
                        </div>
                    </div>`;
}

function renderSubjectiveCard(q, idx) {
  const stepsHtml = q.solutionSteps.map(step => {
    return `<div class="step-item"><i class="fas fa-angle-right"></i> <span>${step}</span></div>`;
  }).join('');

  return `<div class="question-card" data-qid="${q.id}">
                    <div class="q-header">
                        <span class="q-badge">Q${idx + 1}</span>
                    </div>
                    <div class="q-text">${q.question}</div>
                        <div class="solution-container">
                            <button class="solution-toggle-btn" onclick="toggleSolution('${q.id}')">
                                <i class="fas fa-eye"></i> Show Solution
                            </button>
                            <div id="sol-${q.id}" class="solution-content" style="display: none;">
                    <div class="solution-steps">${stepsHtml}</div><div class="final-answer">${q.answer}</div>
                            </div>
                        </div>
                    </div>`;
}

function generateHTML(ch, ex) {
  const cardsHtml = ex.questions.map((q, idx) => {
    return q.type === 'mcq' ? renderMCQCard(q, idx) : renderSubjectiveCard(q, idx);
  }).join('');

  return `<!DOCTYPE html>
<html lang="en">

<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Class 11 ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} Exemplar Solutions | SJMaths</title>
    <link rel="icon" type="image/png" href="/favicon.png">
    <meta name="description" content="Practice Class 11 Maths ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} NCERT Exemplar solutions for exam preparation and concept mastery.">


    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="https://sjmaths.com/class-11-maths/ncert-exemplar-practice/${ch.chapterSlug}/exemplar-${ch.chapterNum}-${ex.exNum}">
<!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>

    <!-- Font Awesome -->
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473"
        onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript>
        <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473">
    </noscript>

    <!-- Shared CSS -->
    <link rel="stylesheet" href="/assets/css/exercise-shared.min.css?v=d2e3359a">
    <link rel="stylesheet" href="/assets/css/footer.min.css?v=ead230d6">

    <!-- MathJax -->
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] },
            svg: { fontCache: 'global' }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-svg.js" data-cfasync="false"></script>


  <!-- Structured Data: Breadcrumbs -->
  <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://sjmaths.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Resources",
      "item": "https://sjmaths.com/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Class 11",
      "item": "https://sjmaths.com/class-11-maths/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Ncert Examplar Practice",
      "item": "https://sjmaths.com/class-11-maths/ncert-exemplar-practice/"
    },
    {
      "@type": "ListItem",
      "position": 5,
      "name": "${ch.chapterName}",
      "item": "https://sjmaths.com/class-11-maths/ncert-exemplar-practice/"
    },
    {
      "@type": "ListItem",
      "position": 6,
      "name": "Exemplar ${ch.chapterNum} ${ex.exNum}.html",
      "item": "https://sjmaths.com/class-11-maths/ncert-exemplar-practice/${ch.chapterSlug}/exemplar-${ch.chapterNum}-${ex.exNum}"
    }
  ]
}
  </script>

    <link rel="stylesheet" href="/assets/css/main.min.css?v=2d265739">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=c2396f5e">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=1d28fefd">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=c2cafd6e">
    <link rel="stylesheet" href="/assets/css/ai-seo.min.css?v=d7149c24">

    <!-- Custom AI Meta Signals -->
    <meta name="ai-purpose" content="Educational mathematics content for CBSE students (Classes 9–12)">
    <meta name="ai-topics" content="CBSE Maths, NCERT Solutions, ${ch.chapterNum} ${ch.chapterName.toLowerCase()}, Board Exam Preparation">
    <meta name="ai-audience" content="Students, Teachers, Tutors">


    <!-- Structured Data: WebPage/Audience (AI Generated) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "audience": {
        "@type": "EducationalAudience",
        "educationalRole": "student"
      }
    }
    </script>

    <meta property="og:title" content="Class 11 ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} Exemplar Solutions | SJMaths">
    <meta property="og:description" content="Practice Class 11 Maths ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} NCERT Exemplar solutions for exam preparation and concept mastery.">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://sjmaths.com/class-11-maths/ncert-exemplar-practice/${ch.chapterSlug}/exemplar-${ch.chapterNum}-${ex.exNum}">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Class 11 ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} Exemplar Solutions | SJMaths">
    <meta name="twitter:description" content="Practice Class 11 Maths ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} NCERT Exemplar solutions for exam preparation and concept mastery.">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <meta name="keywords" content="Class 11 Maths, CBSE Class 11 Maths, NCERT Class 11 Maths, SJMaths, Class 11 NCERT Solutions, ${ch.chapterName} NCERT Solutions, Exemplar ${ch.chapterNum} ${ex.exNum} Class 11 Maths">
    <meta name="author" content="SJMaths">
    <!-- SEO LearningResource: Class 11 -->
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "Chapter ${ch.chapterNum} - ${ch.chapterName}",
  "headline": "Class 11 ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} Exemplar Solutions",
  "description": "Practice Class 11 Maths ${ch.chapterName} Exemplar ${ch.chapterNum} ${ex.exNum} NCERT Exemplar solutions for exam preparation and concept mastery.",
  "url": "https://sjmaths.com/class-11-maths/ncert-exemplar-practice/${ch.chapterSlug}/exemplar-${ch.chapterNum}-${ex.exNum}",
  "image": "https://sjmaths.com/assets/icons/icon-512x512.png",
  "inLanguage": "en-IN",
  "isPartOf": {
    "@type": "Course",
    "name": "Class 11 Maths",
    "url": "https://sjmaths.com/class-11-maths/",
    "provider": {
      "@type": "Organization",
      "name": "SJMaths",
      "url": "https://sjmaths.com"
    }
  },
  "educationalLevel": "Class 11",
  "learningResourceType": "Practice and revision resource",
  "about": [
    "Class 11 Maths",
    "CBSE Mathematics"
  ],
  "publisher": {
    "@type": "Organization",
    "name": "SJMaths",
    "url": "https://sjmaths.com",
    "logo": {
      "@type": "ImageObject",
      "url": "https://sjmaths.com/assets/icons/icon-512x512.png"
    }
  }
}
    </script>
<!-- KaTeX for High-Fidelity Mathematical & Scientific Typesetting -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous"/>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function () {
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(document.body, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\\\(', right: '\\\\)', display: false },
                    { left: '\\\\[', right: '\\\\]', display: true }
                ],
                ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'option'],
                throwOnError: false
            });
        }
    });
</script></head>

<body data-class="11" data-chapter="${ch.chapterNum}" data-chaptername="${ch.chapterName}">
    <div id="header-container"></div>

    <!-- Hero Section -->
    <div class="hero">
        <nav class="breadcrumb">
            <a href="/">Home</a> <span>›</span>
            <a href="/class-11-maths/">Class 11</a> <span>›</span>
            <a href="../">Exemplar</a> <span>›</span>
            <span>Exercise ${ch.chapterNum}.${ex.exNum}</span>
        </nav>
        <h1>Chapter ${ch.chapterNum} - ${ch.chapterName}</h1>

    <div class="floating-notes-link" style="margin-bottom: 20px; text-align: center;">
        <a href="../../chapter-wise-notes/${ch.chapterSlug}/" style="color: var(--primary); font-weight: 600; text-decoration: none;">
            <i class="fas fa-book-open"></i> Revise Chapter Notes
        </a>
    </div>


    <!-- AI Summary Block -->
    <section class="ai-summary">
        <h2><i class="fas fa-list-ul"></i> Overview</h2>
        <p>This page provides comprehensive <strong>Class 11 Maths Exemplar Chapter ${ch.chapterNum} Exercise ${ch.chapterNum}.${ex.exNum} Solutions</strong>. Detailed step-by-step solutions for Class 11 Maths NCERT Exemplar Chapter ${ch.chapterNum} ${ch.chapterName} Exercise ${ch.chapterNum}.${ex.exNum}. Free PDF download and interactive practice.</p>
    </section>

        <p>Exercise ${ch.chapterNum}.${ex.exNum}</p>
    </div>

    <!-- Main Content -->
    <div class="container" style="max-width: 900px; margin: 0 auto; padding: 0 20px 4rem;">
        <div id="question-container">
<!-- Initial HTML generated by scripts/prerender-seo-content.cjs; edit the authored JSON, then regenerate. -->
<div id="${ex.sectionLetter}">
                <h2 style="margin:1.2rem 0;color:#7b1fa2;text-align:center;">
                    ${ex.title}
                </h2>
            ${cardsHtml}</div>
</div>
    </div>

    <!-- Bottom Navigation -->
    <div class="bottom-nav">
        <a href="${ex.prevUrl}" class="nav-btn btn-prev">${ex.prevText}</a>
        <a href="${ex.nextUrl}" class="nav-btn btn-next">${ex.nextText}</a>
    </div>

    <!-- Footer -->
    <div id="footer-container"></div>

    <!-- Floating Controls -->
    <div class="floating-controls">
        <a href="../" class="back-btn-floating" title="Back to Chapter">
            <i class="fas fa-arrow-left"></i>
        </a>
    </div>

    <!-- Scripts -->
    <script src="/assets/js/main.min.js?v=bccca5f2" data-cfasync="false"></script>
    <script src="/assets/js/exercise.min.js?v=c438a378"></script>
    <script>
        window.QUESTIONS_JSON = 'exemplar-${ch.chapterNum}-${ex.exNum}.json';
    </script>
    <script src="/assets/js/questions-loader.min.js?v=cb82826c"></script>


    <script src="/assets/js/global-header.min.js?v=7e828b18" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=35eb8e52" defer data-cfasync="false"></script>
    <script type="module">
        const load = async () => {
            try {
                await import("/assets/js/firebase-analytics-only.min.js?v=b9396571");
            } catch (e) { console.debug("Analytics deferred"); }
        };
        if ('requestIdleCallback' in window) requestIdleCallback(load); else setTimeout(load, 3000);
    </script>
  <script type="module" src="/assets/js/require-auth.min.js?v=3814152d"></script>
</body>
</html>
`;
}

function generateJSON(ch, ex) {
  const jsonQuestions = ex.questions.map((q, idx) => {
    const item = {
      id: q.id,
      number: idx + 1,
      question: q.question,
      solutionSteps: q.solutionSteps,
      finalAnswer: q.answer
    };
    if (q.options) {
      item.options = q.options;
    }
    return item;
  });

  return JSON.stringify({
    sections: [
      {
        section: ex.title,
        questions: jsonQuestions
      }
    ]
  }, null, 4);
}

// Write files
chapters.forEach(ch => {
  const chDir = path.join(__dirname, '../class-11-maths/ncert-exemplar-practice', ch.chapterSlug);
  exCount = 0;
  ch.exercises.forEach(ex => {
    const htmlFileName = `exemplar-${ch.chapterNum}-${ex.exNum}.html`;
    const jsonFileName = `exemplar-${ch.chapterNum}-${ex.exNum}.json`;

    const htmlPath = path.join(chDir, htmlFileName);
    const jsonPath = path.join(chDir, jsonFileName);

    const htmlContent = generateHTML(ch, ex);
    const jsonContent = generateJSON(ch, ex);

    fs.writeFileSync(htmlPath, htmlContent, 'utf8');
    fs.writeFileSync(jsonPath, jsonContent, 'utf8');

    console.log(`Generated: ${ch.chapterSlug}/${htmlFileName} and ${jsonFileName} (${ex.questions.length} questions)`);
  });
});

console.log('All 9 NCERT Exemplar chapters successfully populated!');
