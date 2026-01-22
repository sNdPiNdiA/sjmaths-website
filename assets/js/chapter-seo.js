(function () {

  const body = document.body;

  const classNo = body.dataset.class;
  const chapterNo = body.dataset.chapter;
  const chapterName = body.dataset.chaptername;
  const pageURL = window.location.href;

  if (!classNo || !chapterNo || !chapterName) return;

  const classLabel = `Class ${classNo}`;
  const cleanChapter = chapterName.trim();
  const slugChapter = cleanChapter.toLowerCase().replace(/ /g, "-");

  const title = `NCERT ${classLabel} Maths Chapter ${chapterNo} ${cleanChapter} Notes & Solutions | SJMaths`;
  const description = `Complete NCERT ${classLabel} Mathematics Chapter ${chapterNo} ${cleanChapter} notes with definitions, theorems, formulas, examples and exam-oriented explanations.`;

  /* ---------- META ---------- */
  document.title = title;

  const metaDesc = document.createElement("meta");
  metaDesc.name = "description";
  metaDesc.content = description;
  document.head.appendChild(metaDesc);

  const canonical = document.createElement("link");
  canonical.rel = "canonical";
  canonical.href = pageURL;
  document.head.appendChild(canonical);

  /* ---------- OPEN GRAPH ---------- */
  const og = {
    "og:title": title,
    "og:description": description,
    "og:type": "article",
    "og:url": pageURL
  };

  Object.keys(og).forEach(key => {
    const meta = document.createElement("meta");
    meta.setAttribute("property", key);
    meta.content = og[key];
    document.head.appendChild(meta);
  });

  /* ---------- BREADCRUMB HTML ---------- */
  const breadcrumb = document.createElement("nav");
  breadcrumb.className = "breadcrumb";
  breadcrumb.innerHTML = `
    <a href="/">Home</a> ›
    <a href="/classes/class-${classNo}/">${classLabel}</a> ›
    <a href="/classes/class-${classNo}/chapter-wise-notes/">Chapter Notes</a> ›
    <span>${cleanChapter}</span>
  `;
  document.body.prepend(breadcrumb);

  /* ---------- JSON-LD ---------- */
  const schema = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
          { "@type": "ListItem", "position": 2, "name": classLabel, "item": `https://sjmaths.com/classes/class-${classNo}/` },
          { "@type": "ListItem", "position": 3, "name": "Chapter Notes", "item": `https://sjmaths.com/classes/class-${classNo}/chapter-wise-notes/` },
          { "@type": "ListItem", "position": 4, "name": cleanChapter, "item": pageURL }
        ]
      },
      {
        "@type": "LearningResource",
        "name": title,
        "description": description,
        "educationalLevel": classLabel,
        "learningResourceType": "LectureNotes",
        "inLanguage": "en",
        "audience": {
          "@type": "EducationalAudience",
          "educationalRole": "student"
        },
        "isPartOf": {
          "@type": "CreativeWorkSeries",
          "name": `CBSE ${classLabel} Mathematics`,
          "url": `https://sjmaths.com/classes/class-${classNo}/`
        },
        "url": pageURL,
        "publisher": {
          "@type": "Organization",
          "name": "SJMaths",
          "url": "https://sjmaths.com"
        }
      },
      {
        "@type": "Article",
        "headline": title,
        "description": description,
        "author": { "@type": "Organization", "name": "SJMaths" },
        "publisher": { "@type": "Organization", "name": "SJMaths" },
        "mainEntityOfPage": { "@type": "WebPage", "@id": pageURL }
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": `What is covered in Class ${classNo} Maths Chapter ${chapterNo} ${cleanChapter}?`,
            "acceptedAnswer": {
              "@type": "Answer",
              "text": `This chapter covers all NCERT concepts of ${cleanChapter} with theory, theorems, formulas, worked examples and practice questions as per the latest CBSE syllabus.`
            }
          },
          {
            "@type": "Question",
            "name": "Are NCERT solutions available for this chapter?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, all exercises are solved step by step with clear reasoning and exam-oriented methods."
            }
          },
          {
            "@type": "Question",
            "name": "Is this chapter important for board exams?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Yes, this chapter is strictly based on the CBSE syllabus and is highly important for school tests and board examinations."
            }
          }
        ]
      }
    ]
  };

  const script = document.createElement("script");
  script.type = "application/ld+json";
  script.textContent = JSON.stringify(schema, null, 2);
  document.head.appendChild(script);

})();
