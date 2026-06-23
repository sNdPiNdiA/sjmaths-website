(function () {

  const path = window.location.pathname;
  const parts = path.split("/").filter(Boolean);

  // Detect class
  const classIndex = parts.indexOf("classes");
  const classSlug = classIndex >= 0 ? parts[classIndex + 1] : parts[0];
  const classNumber = (classSlug.match(/^class-(\d+)/) || [null, '9'])[1];
  const classLabel = `Class ${classNumber}`;
  const prettyClassSlug = /^class-\d+-maths$/.test(classSlug)
    ? classSlug
    : `class-${classNumber}-maths`;
  const prettyClassPath = `/${prettyClassSlug}/`;

  // Detect chapter + exercise
  const chapterIndex = parts.indexOf("ncert-exercise-practice") + 1;
  const chapterSlug = parts[chapterIndex];
  const exerciseFile = parts[parts.length - 1];

  const chapterNumber = chapterSlug.match(/\d+/)[0];
  const chapterName = chapterSlug
    .replace(/chapter-\d+-/, "")
    .replace(/-/g, " ")
    .replace(/\b\w/g, l => l.toUpperCase());

  const match = exerciseFile.match(/\d+-\d+/);
  const exerciseNumber = match ? match[0].replace("-", ".") : "";
  const isEndOfChapter = exerciseFile.includes("end-of-chapter") || (!match && (exerciseFile.includes("exercise") || exerciseFile.includes("chapter")));
  const exerciseLabel = isEndOfChapter ? "End of Chapter Exercises" : `Exercise ${exerciseNumber}`;

  const pageTitle = `NCERT ${classLabel} Maths ${chapterName} ${exerciseLabel} Solutions | SJMaths`;
  const pageDesc = `Step-by-step NCERT ${classLabel} Maths Chapter ${chapterNumber} ${chapterName} ${exerciseLabel} solutions with formulas, diagrams and CBSE exam-oriented explanations.`;

  /* ---------- META ---------- */
  document.title = pageTitle;

  const metaDesc = document.createElement("meta");
  metaDesc.name = "description";
  metaDesc.content = pageDesc;
  document.head.appendChild(metaDesc);

  const canonical = document.createElement("link");
  canonical.rel = "canonical";
  canonical.href = window.location.href.split('?')[0].replace(/\/index\.html$/, '/');
  document.head.appendChild(canonical);

  const hreflangIn = document.createElement("link");
  hreflangIn.rel = "alternate";
  hreflangIn.hreflang = "en-in";
  hreflangIn.href = window.location.href.split('?')[0].replace(/\/index\.html$/, '/');
  document.head.appendChild(hreflangIn);

  const hreflangDefault = document.createElement("link");
  hreflangDefault.rel = "alternate";
  hreflangDefault.hreflang = "x-default";
  hreflangDefault.href = window.location.href.split('?')[0].replace(/\/index\.html$/, '/');
  document.head.appendChild(hreflangDefault);

  /* ---------- OPEN GRAPH ---------- */
  const ogData = {
    "og:title": pageTitle,
    "og:description": pageDesc,
    "og:type": "article",
    "og:url": window.location.href.split('?')[0].replace(/\/index\.html$/, '/')
  };

  Object.keys(ogData).forEach(key => {
    const meta = document.createElement("meta");
    meta.setAttribute("property", key);
    meta.content = ogData[key];
    document.head.appendChild(meta);
  });

  /* ---------- BREADCRUMB HTML ---------- */
  const breadcrumb = document.createElement("nav");
  breadcrumb.className = "breadcrumb";
  breadcrumb.innerHTML = `
    <a href="/">Home</a> ›
    <a href="${prettyClassPath}">${classLabel}</a> ›
    <a href="${prettyClassPath}ncert-exercise-practice/">NCERT Exercises</a> ›
    <a href="${prettyClassPath}ncert-exercise-practice/${chapterSlug}/">${chapterName}</a> ›
    <span>${exerciseLabel}</span>
  `;

  // Insert INSIDE hero using prepend to ensure it pushes text down
  const hero = document.querySelector('.hero');
  const header = document.querySelector('header') || document.getElementById('header-container');

  if (hero) {
    hero.prepend(breadcrumb);
  } else if (header && header.parentNode) {
    header.after(breadcrumb);
  } else {
    document.body.prepend(breadcrumb);
  }

  /* ---------- STRUCTURED DATA ---------- */
  const jsonLD = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
          { "@type": "ListItem", "position": 2, "name": classLabel, "item": `https://sjmaths.com${prettyClassPath}` },
          { "@type": "ListItem", "position": 3, "name": "NCERT Exercises", "item": `https://sjmaths.com${prettyClassPath}ncert-exercise-practice/` },
          { "@type": "ListItem", "position": 4, "name": chapterName, "item": `https://sjmaths.com${prettyClassPath}ncert-exercise-practice/${chapterSlug}/` },
          { "@type": "ListItem", "position": 5, "name": exerciseLabel, "item": window.location.href.split('?')[0].replace(/\/index\.html$/, '/') }
        ]
      },
      {
        "@type": "LearningResource",
        "name": pageTitle,
        "description": pageDesc,
        "educationalLevel": classLabel,
        "learningResourceType": "NCERT Solutions",
        "inLanguage": "en",
        "audience": {
          "@type": "EducationalAudience",
          "educationalRole": "student"
        },
        "isPartOf": {
          "@type": "CreativeWorkSeries",
          "name": `CBSE ${classLabel} Mathematics`,
          "url": `https://sjmaths.com${prettyClassPath}`
        },
        "url": window.location.href.split('?')[0].replace(/\/index\.html$/, '/'),
        "publisher": {
          "@type": "Organization",
          "name": "SJMaths",
          "url": "https://sjmaths.com"
        }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": `What is covered in ${classLabel} Maths Chapter ${chapterNumber} (${chapterName}) ${exerciseLabel}?`,
            "acceptedAnswer": {
              "@type": "Answer",
              "text": `This exercise covers important concepts of ${chapterName} as per the NCERT ${classLabel} Mathematics syllabus with step-by-step solved questions.`
            }
          },
          {
            "@type": "Question",
            "name": "Are step-by-step NCERT solutions provided?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, all questions are solved step by step with clear reasoning, formulas, and exam-oriented methods as per CBSE guidelines."
            }
          },
          {
            "@type": "Question",
            "name": "Is this exercise important for CBSE exams?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, all exercises are strictly based on the latest NCERT syllabus and are highly important for school tests and board examinations."
            }
          },
          {
            "@type": "Question",
            "name": "Is the content on SJMaths free for students?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, all Class 9–12 NCERT exercise solutions on SJMaths are completely free for students."
            }
          }
        ]
      }
    ]
  };

  const schemaScript = document.createElement("script");
  schemaScript.type = "application/ld+json";
  schemaScript.textContent = JSON.stringify(jsonLD, null, 2);
  document.head.appendChild(schemaScript);

})();
