(function () {

  const path = window.location.pathname;
  const parts = path.split("/").filter(Boolean);

  // Detect class
  const classIndex = parts.indexOf("classes") + 1;
  const classSlug = parts[classIndex];
  const classNumber = classSlug.replace("class-", "");
  const classLabel = `Class ${classNumber}`;

  // Detect chapter + exercise
  const chapterIndex = parts.indexOf("ncert-exercise-practice") + 1;
  const chapterSlug = parts[chapterIndex];
  const exerciseFile = parts[parts.length - 1];

  const chapterNumber = chapterSlug.match(/\d+/)[0];
  const chapterName = chapterSlug
    .replace(/chapter-\d+-/, "")
    .replace(/-/g, " ")
    .replace(/\b\w/g, l => l.toUpperCase());

  const exerciseNumber = exerciseFile.match(/\d+-\d+/)[0].replace("-", ".");

  const pageTitle = `NCERT ${classLabel} Maths ${chapterName} Exercise ${exerciseNumber} Solutions | SJMaths`;
  const pageDesc = `Step-by-step NCERT ${classLabel} Maths Chapter ${chapterNumber} ${chapterName} Exercise ${exerciseNumber} solutions with formulas, diagrams and CBSE exam-oriented explanations.`;

  /* ---------- META ---------- */
  document.title = pageTitle;

  const metaDesc = document.createElement("meta");
  metaDesc.name = "description";
  metaDesc.content = pageDesc;
  document.head.appendChild(metaDesc);

  const canonical = document.createElement("link");
  canonical.rel = "canonical";
  canonical.href = window.location.href;
  document.head.appendChild(canonical);

  /* ---------- OPEN GRAPH ---------- */
  const ogData = {
    "og:title": pageTitle,
    "og:description": pageDesc,
    "og:type": "article",
    "og:url": window.location.href
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
    <a href="/classes/${classSlug}/">${classLabel}</a> ›
    <a href="/classes/${classSlug}/ncert-exercise-practice/">NCERT Exercises</a> ›
    <a href="/classes/${classSlug}/ncert-exercise-practice/${chapterSlug}/">${chapterName}</a> ›
    <span>Exercise ${exerciseNumber}</span>
  `;
  document.body.prepend(breadcrumb);

  /* ---------- STRUCTURED DATA ---------- */
  const jsonLD = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
          { "@type": "ListItem", "position": 2, "name": classLabel, "item": `https://sjmaths.com/classes/${classSlug}/` },
          { "@type": "ListItem", "position": 3, "name": "NCERT Exercises", "item": `https://sjmaths.com/classes/${classSlug}/ncert-exercise-practice/` },
          { "@type": "ListItem", "position": 4, "name": chapterName, "item": `https://sjmaths.com/classes/${classSlug}/ncert-exercise-practice/${chapterSlug}/` },
          { "@type": "ListItem", "position": 5, "name": `Exercise ${exerciseNumber}`, "item": window.location.href }
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
          "url": `https://sjmaths.com/classes/${classSlug}/`
        },
        "url": window.location.href,
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
            "name": `What is covered in ${classLabel} Maths Chapter ${chapterNumber} (${chapterName}) Exercise ${exerciseNumber}?`,
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
