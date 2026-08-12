document.addEventListener("DOMContentLoaded", () => {
  const developmentPath = "/class-10-social-science/economics/chapter-1-development/";
  const isDevelopmentResource = location.pathname.includes(developmentPath) &&
    location.pathname !== developmentPath && !location.pathname.endsWith("chapter-1-development/index.html");

  if (isDevelopmentResource) {
    const sourceStyles = [
      "https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Poppins:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css",
      "../../../assets/css/main.min.css?v=4ba21ce7",
      "../../../assets/css/layout.min.css?v=e4922b08",
      "../../../assets/css/component.min.css?v=8c99f11f",
      "../../../assets/css/improved-ui.min.css?v=86f5556a",
      "../../../class-9-science/science-chapter.css"
    ];
    document.querySelector('link[href$="assets/css/sst.css"]')?.remove();
    sourceStyles.forEach(href => {
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = href;
      document.head.append(link);
    });

    const pageId = document.body.dataset.sstPage;
    const resources = [
      ["concepts", "Concepts", "fas fa-book-open"],
      ["ncert-exercises", "NCERT", "fas fa-pencil-ruler"],
      ["practice", "Practice", "fas fa-pen-to-square"],
      ["pyqs", "PYQs", "fas fa-clock-rotate-left"],
      ["quiz", "Quiz", "fas fa-question-circle"],
      ["tests", "Tests", "fas fa-clipboard-check"],
      ["revision-notes", "Revision", "fas fa-rocket"]
    ];
    const current = resources.findIndex(([id]) => id === pageId);
    const main = document.querySelector("main.sst-container");
    const heading = main?.querySelector(".sst-header h1")?.textContent.trim() || "Development";
    const subtitle = main?.querySelector(".sst-header .sst-subtitle")?.textContent.trim() || "Study Resource";
    const sections = main ? [...main.children].filter(element => element.classList.contains("sst-section")) : [];

    if (main && sections.length) {
      const previous = current > 0 ? resources[current - 1] : ["index", "Overview", "fas fa-arrow-left"];
      const next = current < resources.length - 1 ? resources[current + 1] : ["index", "Overview", "fas fa-home"];
      const hrefFor = id => id === "index" ? "../index.html" : `../${id}/`;
      const wrapper = document.createElement("div");
      wrapper.className = "sj-container sj-development-resource";
      wrapper.innerHTML = `
        <nav class="sj-tbar" aria-label="Chapter navigation">
          <div class="sj-bcrumb"><a href="/">Home</a><i class="fas fa-chevron-right"></i><a href="/class-10-social-science/">Class 10 Social Science</a><i class="fas fa-chevron-right"></i><a href="../index.html">Development</a><i class="fas fa-chevron-right"></i><span style="color:#0f766e;">${subtitle}</span></div>
          <div class="sj-nav"><a href="${hrefFor(previous[0])}" class="sj-btn"><i class="${previous[2]}"></i> ${previous[1].toUpperCase()}</a><a href="${hrefFor(next[0])}" class="sj-btn next">${next[1].toUpperCase()} <i class="fas fa-arrow-right"></i></a></div>
        </nav>
        <nav class="sj-section-nav" aria-label="Study resources"><a href="../index.html" class="sj-section-link"><i class="fas fa-home"></i> Overview</a>${resources.map(([id,label,icon]) => `<a href="${hrefFor(id)}" class="sj-section-link ${id === pageId ? "active" : ""}"><i class="${icon}"></i> ${label}</a>`).join("")}</nav>
        <div class="sj-page-content"><h1>Development: ${subtitle}</h1><div class="sj-resource-content"></div></div>`;

      const content = wrapper.querySelector(".sj-resource-content");
      sections.forEach(section => content.append(section));
      content.querySelectorAll(".sst-card, .sst-question").forEach(card => card.classList.add("sj-card"));
      content.querySelectorAll(".sst-grid").forEach(grid => grid.classList.add("sj-development-grid"));
      content.querySelectorAll(".sst-section-label").forEach(label => label.classList.add("sj-development-section-label"));
      document.querySelector("header.sst-topbar")?.remove();
      main.replaceWith(wrapper);
      document.body.classList.add("sj-development-page");
      const pageStyle = document.createElement("style");
      pageStyle.textContent = `
        .sj-development-page .sj-page-content > h1 { margin-bottom: 1.5rem; }
        .sj-development-page .sj-development-section-label { margin: 0 0 1rem; color: #0f766e; font-size: .72rem; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; }
        .sj-development-page .sst-section + .sst-section { margin-top: 1.5rem; }
        .sj-development-page .sj-development-grid { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: 1rem; }
        .sj-development-page .sj-development-grid .sj-card { margin: 0; }
        .sj-development-page .sj-card { margin-bottom: 1rem; }
        .sj-development-page .sj-card h3 { color: #12355b; }
        .sj-development-page .sst-card p, .sj-development-page .sst-card li { color: #475569; font-size: .92rem; }
        .sj-development-page .sst-card ul { margin: .7rem 0 0; padding-left: 1.2rem; }
        .sj-development-page .sst-badge { display: inline-block; margin-bottom: .7rem; padding: .28rem .58rem; border-radius: 99px; color: #0f766e; background: #e6fffb; font-size: .65rem; font-weight: 800; text-transform: uppercase; }
        .sj-development-page .sst-formula { margin-top: .8rem; padding: .85rem 1rem; border-left: 4px solid #0f766e; border-radius: 0 10px 10px 0; color: #134e4a; background: #ecfdf5; font-weight: 700; }
        .sj-development-page .sst-question > strong { display: block; color: #12355b; font-size: 1rem; }
        .sj-development-page .sst-option { display: flex; gap: .6rem; align-items: center; margin-top: .55rem; padding: .72rem .85rem; border: 1px solid #dbe5ef; border-radius: 10px; color: #475569; background: #f8fafc; cursor: pointer; }
        .sj-development-page .sst-option:hover, .sj-development-page .sst-option.selected { border-color: #14b8a6; background: #f0fdfa; }
        .sj-development-page .sst-option.correct { border-color: #22c55e; background: #f0fdf4; }
        .sj-development-page .sst-answer-toggle { margin-top: .9rem; padding: .58rem .9rem; border: 1px solid #0f766e; border-radius: 9px; color: #0f766e; background: #fff; font-weight: 800; cursor: pointer; }
        .sj-development-page .sst-answer-toggle:hover { color: #fff; background: #0f766e; }
        .sj-development-page .sst-answer { margin-top: .8rem; padding: .85rem 1rem; border-left: 4px solid #16a34a; border-radius: 0 10px 10px 0; color: #166534; background: #f0fdf4; }
        .sj-development-page .sst-answer[hidden] { display: none!important; }
        @media (max-width: 720px) { .sj-development-page .sj-development-grid { grid-template-columns: 1fr; } }
      `;
      document.head.append(pageStyle);
      if (!document.querySelector("#header-container")) {
        document.body.insertAdjacentHTML("afterbegin", '<div id="header-container"></div>');
      }
      document.body.insertAdjacentHTML("beforeend", '<div id="footer-container"></div>');
      const headerScript = document.createElement("script");
      headerScript.src = "../../../assets/js/global-header.js";
      document.body.append(headerScript);
      const footerScript = document.createElement("script");
      footerScript.src = "../../../assets/js/global-footer.js";
      document.body.append(footerScript);
    }
  }

  const resourceTabs = document.querySelector("[data-sj-resource-tabs]");
  const resourcePanel = document.querySelector("#sj-resource-panel");
  const overviewPanel = document.querySelector("#sj-overview-panel");

  if (resourceTabs && resourcePanel && overviewPanel) {
    const tabLinks = [...resourceTabs.querySelectorAll("[data-sj-tab]")];
    const activateResource = async tab => {
      const link = tabLinks.find(item => item.dataset.sjTab === tab);
      if (!link) return;

      tabLinks.forEach(item => item.classList.toggle("active", item === link));
      overviewPanel.hidden = tab !== "overview";
      resourcePanel.classList.toggle("active", tab !== "overview");

      if (tab === "overview") {
        history.replaceState(null, "", "index.html");
        return;
      }

      history.replaceState(null, "", `#${tab}`);
      if (resourcePanel.dataset.loadedTab === tab) return;

      resourcePanel.dataset.loadedTab = tab;
      resourcePanel.innerHTML = '<div class="sj-resource-loading"><i class="fas fa-spinner fa-spin"></i> Loading study material...</div>';

      try {
        const response = await fetch(link.getAttribute("href"));
        if (!response.ok) throw new Error(`Could not load ${tab}`);
        const documentFragment = new DOMParser().parseFromString(await response.text(), "text/html");
        const sections = [...documentFragment.querySelectorAll("main .sst-section")];
        if (!sections.length) throw new Error(`No study content found for ${tab}`);
        resourcePanel.replaceChildren(...sections.map(section => document.importNode(section, true)));
        initialiseDynamicStudyControls(resourcePanel);
      } catch (error) {
        resourcePanel.innerHTML = '<div class="sj-resource-loading">This resource could not be loaded. Please use the chapter card below to open it directly.</div>';
      }
    };

    tabLinks.forEach(link => link.addEventListener("click", event => {
      event.preventDefault();
      activateResource(link.dataset.sjTab);
    }));

    const requestedTab = location.hash.slice(1);
    if (requestedTab && tabLinks.some(link => link.dataset.sjTab === requestedTab)) activateResource(requestedTab);
  }

  function initialiseDynamicStudyControls(scope = document) {
    scope.querySelectorAll("[data-sst-answer-toggle]").forEach(button => {
      if (button.dataset.sstBound) return;
      button.dataset.sstBound = "true";
      const question = button.closest(".sst-question");
      const answer = question?.querySelector(".sst-answer");
      if (!answer) return;
      button.addEventListener("click", () => {
        const opening = answer.hidden;
        answer.hidden = !opening;
        button.textContent = opening ? "Hide Answer" : "Show Answer";
        const correctLetter = answer.querySelector("strong")?.textContent.trim().replace(/[^A-D]/gi, "").charAt(0);
        if (opening && correctLetter) question.querySelectorAll(".sst-option").forEach(option => {
          const letter = option.querySelector("strong")?.textContent.trim().replace(/[^A-D]/gi, "").charAt(0);
          option.classList.toggle("correct", letter === correctLetter);
        });
      });
    });

    scope.querySelectorAll(".sst-option").forEach(option => {
      if (option.dataset.sstBound) return;
      option.dataset.sstBound = "true";
      option.setAttribute("role", "button");
      option.setAttribute("tabindex", "0");
      const select = () => { const question = option.closest(".sst-question"); question?.querySelectorAll(".sst-option").forEach(item => item.classList.remove("selected", "incorrect")); option.classList.add("selected"); };
      option.addEventListener("click", select);
      option.addEventListener("keydown", event => { if (event.key === "Enter" || event.key === " ") { event.preventDefault(); select(); } });
    });
  }

  initialiseDynamicStudyControls();

  document.querySelectorAll("[data-sst-answer-toggle]").forEach(button => {
    if (button.dataset.sstBound) return;
    const question = button.closest(".sst-question");
    const answer = question?.querySelector(".sst-answer");
    if (!answer) return;

    button.addEventListener("click", () => {
      const opening = answer.hidden;
      answer.hidden = !opening;
      question.classList.toggle("revealed", opening);
      button.textContent = opening ? "Hide Answer" : "Show Answer";

      if (opening) {
        const correctLetter = answer.querySelector("strong")?.textContent.trim().replace(/[^A-D]/gi, "").charAt(0);
        if (correctLetter) {
          question.querySelectorAll(".sst-option").forEach(option => {
            const letter = option.querySelector("strong")?.textContent.trim().replace(/[^A-D]/gi, "").charAt(0);
            option.classList.toggle("correct", letter === correctLetter);
          });
        }
      }
    });
  });

  document.querySelectorAll(".sst-option").forEach(option => {
    option.setAttribute("role", "button");
    option.setAttribute("tabindex", "0");
    const selectOption = () => {
      const question = option.closest(".sst-question");
      question?.querySelectorAll(".sst-option").forEach(item => item.classList.remove("selected", "incorrect"));
      option.classList.add("selected");
    };
    option.addEventListener("click", selectOption);
    option.addEventListener("keydown", event => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        selectOption();
      }
    });
  });

  const tabs = [...document.querySelectorAll(".sst-tab")];
  const panels = [...document.querySelectorAll(".sst-panel")];

  function activateTab(id, updateHash = true) {
    tabs.forEach(tab => {
      tab.classList.toggle("active", tab.dataset.tab === id);
    });

    panels.forEach(panel => {
      panel.classList.toggle("active", panel.id === "tab-" + id);
    });

    if (updateHash) {
      history.replaceState(null, "", "#" + id);
    }
  }

  tabs.forEach(tab => {
    tab.addEventListener("click", () => activateTab(tab.dataset.tab));
  });

  const initial = location.hash.replace("#", "");
  if (initial && tabs.some(tab => tab.dataset.tab === initial)) {
    activateTab(initial, false);
  }

  document.querySelectorAll(".sst-reveal").forEach(button => {
    button.addEventListener("click", () => {
      const question = button.closest(".sst-question");
      question.classList.toggle("revealed");
      button.textContent =
        question.classList.contains("revealed")
          ? "Hide answer"
          : "Show answer";
    });
  });

  document.querySelectorAll("[data-mini-test]").forEach(test => {
    const questions = [...test.querySelectorAll(".sst-question")];
    const submit = test.querySelector(".sst-submit");
    const score = test.querySelector(".sst-score");

    submit?.addEventListener("click", () => {
      let correct = 0;

      questions.forEach(q => {
        const selected = q.querySelector("input:checked");
        if (selected && selected.dataset.correct === "true") {
          correct++;
        }
        q.classList.add("revealed");
      });

      score.style.display = "block";
      score.textContent =
        `Score: ${correct}/${questions.length} · ` +
        (correct === questions.length
          ? "Excellent."
          : "Review the highlighted concepts and try again.");
    });
  });
});
