(function () {

  const body = document.body;

  const classNo = body.dataset.class;
  const chapterNo = body.dataset.chapter;
  const chapterName = body.dataset.chaptername;
  const pageURL = window.location.href.split('?')[0].replace(/\/index\.html$/, '/');

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

  const hreflangIn = document.createElement("link");
  hreflangIn.rel = "alternate";
  hreflangIn.hreflang = "en-in";
  hreflangIn.href = pageURL;
  document.head.appendChild(hreflangIn);

  const hreflangDefault = document.createElement("link");
  hreflangDefault.rel = "alternate";
  hreflangDefault.hreflang = "x-default";
  hreflangDefault.href = pageURL;
  document.head.appendChild(hreflangDefault);

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

  /* ---------- BREADCRUMB HTML ---------- */
  window.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.breadcrumb')) return;

    const breadcrumb = document.createElement("nav");
    breadcrumb.className = "breadcrumb";

    // Inject Styles
    if (!document.getElementById('breadcrumb-style')) {
      const style = document.createElement('style');
      style.id = 'breadcrumb-style';
      style.textContent = `
              .breadcrumb {
                  max-width: 900px;
                  margin: 1rem 0 0;
                  padding: 0;
                  font-size: 0.9rem;
                  color: var(--text-light);
                  font-family: 'Poppins', sans-serif;
                  display: flex !important;
                  flex-wrap: wrap;
                  flex-direction: row !important;
                  justify-content: flex-start;
                  align-items: center;
                  gap: 8px;
                  position: static !important;
                  background: transparent !important;
                  box-shadow: none !important;
                  width: auto !important;
              }
              .breadcrumb a { text-decoration: none; color: inherit; transition: color 0.2s; white-space: nowrap; }
              .breadcrumb a:hover { color: var(--primary); }
              .breadcrumb .separator { font-size: 0.7em; opacity: 0.6; margin: 0 2px; }
              .breadcrumb span.current { color: var(--primary); font-weight: 500; white-space: nowrap; }
              @media (max-width: 600px) { .breadcrumb { font-size: 0.85rem; gap: 6px; } }
          `;
      document.head.appendChild(style);
    }

    breadcrumb.innerHTML = `
        <a href="/">Home</a> <i class="fas fa-chevron-right separator"></i>
        <a href="/classes/class-${classNo}/">${classLabel}</a> <i class="fas fa-chevron-right separator"></i>
        <a href="/classes/class-${classNo}/chapter-wise-notes/">Notes</a> <i class="fas fa-chevron-right separator"></i>
        <span class="current">${cleanChapter}</span>
      `;

    const contentWrapper = document.querySelector('.content-wrapper');
    const headerContainer = document.getElementById('header-container');
    const siteHeader = document.querySelector('header');

    // Priority 1: Inside .content-wrapper (Best for layout)
    if (contentWrapper) {
      contentWrapper.insertBefore(breadcrumb, contentWrapper.firstChild);
    }
    // Priority 2: After Header Container (if global header exists)
    else if (headerContainer && headerContainer.nextSibling) {
      headerContainer.parentNode.insertBefore(breadcrumb, headerContainer.nextSibling);
    }
    // Priority 3: After <header> tag
    else if (siteHeader && siteHeader.nextSibling) {
      siteHeader.parentNode.insertBefore(breadcrumb, siteHeader.nextSibling);
    }
    // Priority 4: Prepend to body (Fallback)
    else {
      document.body.prepend(breadcrumb);
    }
  });

  /* ---------- READING TIME ESTIMATE ---------- */
  window.addEventListener('DOMContentLoaded', () => {
    // 1. Target Hero & Main
    const hero = document.querySelector('.hero');
    const mainContent = document.querySelector('main');

    // Only run if we are on a notes page (has hero + main)
    if (hero && mainContent) {

      // 2. Calculate Time
      const text = mainContent.textContent || "";
      const wordsPerMinute = 200;
      const wordCount = text.split(/\s+/).filter(word => word.length > 0).length;
      const readingTimeMinutes = Math.ceil(wordCount / wordsPerMinute);

      // 3. Inject CSS (Idempotent)
      if (!document.getElementById('reading-time-style')) {
        const style = document.createElement('style');
        style.id = 'reading-time-style';
        style.textContent = `
                  .reading-time-estimate {
                      font-size: 0.95rem;
                      color: inherit;
                      opacity: 0.85;
                      color: inherit;
                      opacity: 0.85;
                      margin-top: 0;
                      margin-bottom: 0.2rem;
                      display: flex;
                      align-items: center;
                      gap: 8px;
                      justify-content: center;
                      font-weight: 500;
                  }
                  .reading-time-estimate i { font-size: 1rem; }
              `;
        document.head.appendChild(style);
      }

      // 4. Inject HTML (Idempotent)
      if (!hero.querySelector('.reading-time-estimate')) {
        const timeElement = document.createElement('p');
        timeElement.className = 'reading-time-estimate';
        timeElement.innerHTML = `<i class="far fa-clock"></i> <span>${readingTimeMinutes} min read</span>`;
        hero.appendChild(timeElement);
      }

      /* ---------- SCROLL PROGRESS BAR ---------- */
      // 1. Inject CSS
      if (!document.getElementById('scroll-progress-style')) {
        const style = document.createElement('style');
        style.id = 'scroll-progress-style';
        style.textContent = `
                  .progress-container {
                      position: fixed;
                      top: 0;
                      left: 0;
                      width: 100%;
                      height: 4px;
                      background: rgba(0,0,0,0.1);
                      z-index: 9999;
                  }
                  .progress-bar {
                      height: 100%;
                      background: var(--primary, #8e44ad);
                      width: 0%;
                      transition: width 0.1s ease-out;
                  }
              `;
        document.head.appendChild(style);
      }

      // 2. Inject HTML
      if (!document.querySelector('.progress-container')) {
        const container = document.createElement('div');
        container.className = 'progress-container';
        container.innerHTML = '<div class="progress-bar" id="progressBar"></div>';
        document.body.prepend(container);
      }

      // 3. Scroll Logic (Optimized)
      let ticking = false;
      window.addEventListener('scroll', () => {
        if (!ticking) {
          window.requestAnimationFrame(() => {
            const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (height > 0) ? (winScroll / height) * 100 : 0;
            const bar = document.getElementById("progressBar");
            if (bar) bar.style.width = scrolled + "%";
            ticking = false;
          });
          ticking = true;
        }
      }, { passive: true });
    }
  });

})();
