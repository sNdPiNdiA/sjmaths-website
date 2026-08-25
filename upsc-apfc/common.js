/*
=========================================================
UPSC APFC — COMMON UI RUNTIME
---------------------------------------------------------
Reusable runtime for ALL topic pages.

The API should generate CONTENT JSON ONLY.

This runtime owns:
- tabs
- accordions
- search
- guided lessons
- quick checks
- quizzes
- PYQs
- flashcards
- mini tests
- scores
- progress persistence
- mistake book
- localStorage
- notifications
- accessibility
=========================================================
*/

(() => {
  "use strict";

  const STORAGE_PREFIX = "sjmaths-upsc-apfc:";

  const $ = (sel, root = document) =>
    root.querySelector(sel);

  const $$ = (sel, root = document) =>
    [...root.querySelectorAll(sel)];

  const escapeHTML = (value = "") =>
    String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");

  const slugify = (value = "") =>
    String(value)
      .toLowerCase()
      .trim()
      .replace(/['’]/g, "")
      .replace(/&/g, " and ")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");

  function getPageKey(config = {}) {
    return (
      config.pageKey ||
      document.body.dataset.pageKey ||
      location.pathname.replace(/\/+$/, "") ||
      "default"
    );
  }

  function loadJSON(key, fallback) {
    try {
      const raw =
        localStorage.getItem(
          STORAGE_PREFIX + key
        );

      return raw
        ? JSON.parse(raw)
        : fallback;

    } catch {
      return fallback;
    }
  }

  function saveJSON(key, value) {
    try {
      localStorage.setItem(
        STORAGE_PREFIX + key,
        JSON.stringify(value)
      );
    } catch {
      /* Storage unavailable */
    }
  }

  function removeJSON(key) {
    try {
      localStorage.removeItem(
        STORAGE_PREFIX + key
      );
    } catch {}
  }

  function uid(prefix = "id") {
    return `${prefix}-${Date.now()}-${Math.random()
      .toString(36)
      .slice(2, 8)}`;
  }

  function notify(
    message,
    tone = "info"
  ) {

    let stack =
      $(".ui-toast-stack");

    if (!stack) {

      stack =
        document.createElement(
          "div"
        );

      stack.className =
        "ui-toast-stack";

      stack.setAttribute(
        "aria-live",
        "polite"
      );

      document.body.appendChild(
        stack
      );
    }

    const item =
      document.createElement(
        "div"
      );

    item.className =
      "ui-toast";

    item.dataset.tone =
      tone;

    item.textContent =
      message;

    stack.appendChild(
      item
    );

    setTimeout(() => {

      item.style.opacity = "0";
      item.style.transform =
        "translateY(6px)";

      setTimeout(
        () => item.remove(),
        220
      );

    }, 2600);
  }

  /* =========================================================
     TABS
  ========================================================= */

  function initTabs(
    root = document
  ) {

    const groups =
      $$("[data-ui-tabs]", root);

    groups.forEach(group => {

      const tabs =
        $$(".ui-tab", group);

      const panelsRoot =
        group.closest(
          "[data-ui-tabs-root]"
        ) ||
        group.parentElement;

      const panels =
        $$(".ui-tab-panel", panelsRoot);

      const activate = (
        name,
        updateHash = true
      ) => {

        tabs.forEach(tab => {

          const active =
            tab.dataset.tab === name;

          tab.classList.toggle(
            "is-active",
            active
          );

          tab.setAttribute(
            "aria-selected",
            String(active)
          );

          tab.setAttribute(
            "tabindex",
            active ? "0" : "-1"
          );
        });

        panels.forEach(panel => {

          const active =
            panel.dataset.tabPanel ===
            name;

          panel.classList.toggle(
            "is-active",
            active
          );

          panel.hidden =
            !active;
        });

        if (
          updateHash &&
          history.replaceState
        ) {

          history.replaceState(
            null,
            "",
            `#${name}`
          );
        }

        group.dispatchEvent(
          new CustomEvent(
            "ui:tabchange",
            {
              detail: {
                name
              }
            }
          )
        );
      };

      tabs.forEach(tab => {

        tab.addEventListener(
          "click",
          () =>
            activate(
              tab.dataset.tab
            )
        );

        tab.addEventListener(
          "keydown",
          event => {

            if (
              ![
                "ArrowLeft",
                "ArrowRight",
                "Home",
                "End"
              ].includes(
                event.key
              )
            ) {
              return;
            }

            event.preventDefault();

            const index =
              tabs.indexOf(tab);

            let next =
              index;

            if (
              event.key ===
              "ArrowLeft"
            ) {

              next =
                index <= 0
                  ? tabs.length - 1
                  : index - 1;
            }

            if (
              event.key ===
              "ArrowRight"
            ) {

              next =
                index >= tabs.length - 1
                  ? 0
                  : index + 1;
            }

            if (
              event.key ===
              "Home"
            ) {
              next = 0;
            }

            if (
              event.key ===
              "End"
            ) {
              next =
                tabs.length - 1;
            }

            tabs[next].focus();

            activate(
              tabs[next].dataset.tab
            );
          }
        );
      });

      const hash =
        location.hash.replace(
          /^#/,
          ""
        );

      const initial =
        tabs.find(
          t =>
            t.dataset.tab ===
            hash
        ) ||
        tabs[0];

      if (initial) {

        activate(
          initial.dataset.tab,
          false
        );
      }

    });
  }

  /* =========================================================
     ACCORDIONS
     Kept for FAQs / optional advanced areas.
     Learn tab itself uses guided lessons.
  ========================================================= */

  function initAccordions(
    root = document
  ) {

    $$(
      "[data-accordion]",
      root
    ).forEach(item => {

      const trigger =
        $(
          ".ui-accordion-trigger",
          item
        );

      const panel =
        $(
          ".ui-accordion-panel",
          item
        );

      if (
        !trigger ||
        !panel
      ) {
        return;
      }

      const open =
        item.classList.contains(
          "is-open"
        );

      trigger.setAttribute(
        "aria-expanded",
        String(open)
      );

      panel.hidden =
        !open;

      trigger.addEventListener(
        "click",
        () => {

          const next =
            !item.classList.contains(
              "is-open"
            );

          item.classList.toggle(
            "is-open",
            next
          );

          trigger.setAttribute(
            "aria-expanded",
            String(next)
          );

          panel.hidden =
            !next;
        }
      );

    });
  }

  /* =========================================================
     SEARCH
  ========================================================= */

  function initSearch(
    config = {}
  ) {

    const input =
      $(
        config.input ||
        "[data-ui-search]"
      );

    const targets =
      $$(
        config.target ||
        "[data-search-text]"
      );

    const empty =
      $(
        config.empty ||
        "[data-search-empty]"
      );

    if (
      !input ||
      !targets.length
    ) {
      return;
    }

    const run = () => {

      const query =
        input.value
          .trim()
          .toLowerCase();

      let visible = 0;

      targets.forEach(
        target => {

          const text =
            (
              target.dataset
                .searchText ||
              target.textContent ||
              ""
            ).toLowerCase();

          const show =
            !query ||
            text.includes(
              query
            );

          target.hidden =
            !show;

          if (show) {
            visible++;
          }

        }
      );

      if (empty) {

        empty.classList.toggle(
          "is-visible",
          visible === 0
        );
      }

      document.dispatchEvent(
        new CustomEvent(
          "ui:search",
          {
            detail: {
              query,
              visible
            }
          }
        )
      );
    };

    input.addEventListener(
      "input",
      run
    );

    run();
  }

  /* =========================================================
     SEARCH CLEAR
  ========================================================= */

  function initSearchClear(
    inputSelector,
    clearSelector
  ) {

    const input =
      $(inputSelector);

    const clear =
      $(clearSelector);

    if (
      !input ||
      !clear
    ) {
      return;
    }

    const sync =
      () => {

        clear.classList.toggle(
          "is-visible",
          !!input.value
        );
      };

    input.addEventListener(
      "input",
      sync
    );

    clear.addEventListener(
      "click",
      () => {

        input.value = "";

        input.dispatchEvent(
          new Event(
            "input",
            {
              bubbles: true
            }
          )
        );

        input.focus();
      }
    );

    sync();
  }

  /* =========================================================
     CONCEPTS
     Used for reference-style sections such as FAQs/PYQs.
  ========================================================= */

  function renderConcepts(items = [], target) {

  if (!target) return;

  if (!items.length) {
    target.innerHTML = `
      <div class="ui-empty is-visible">
        No content available yet.
      </div>
    `;
    return;
  }

  target.innerHTML = `
    <div class="ui-reference-stack">

      ${items.map((item, index) => `
        <article class="ui-reference-card">

          <div class="ui-reference-head">

            <div class="ui-reference-number">
              ${String(index + 1).padStart(2, "0")}
            </div>

            <div class="ui-reference-heading">

              <h3>
                ${escapeHTML(
                  item.title ||
                  `Item ${index + 1}`
                )}
              </h3>

              ${
                item.tag
                  ? `
                    <span class="ui-badge primary">
                      ${escapeHTML(item.tag)}
                    </span>
                  `
                  : ""
              }

            </div>

          </div>

          <div class="ui-reference-body ui-prose">
            ${
              item.html ||
              escapeHTML(item.body || "")
            }
          </div>

        </article>
      `).join("")}

    </div>
  `;
}

  /* =========================================================
     GUIDED LESSON ENGINE
     ---------------------------------------------------------
     API content structure:

     lessonSteps: [
       {
         title,
         tag,
         bodyHtml,
         exampleHtml,
         trapHtml,
         deepHtml,

         quickCheck: {
           questionHtml,
           options: [],
           answer,
           explanation,
           difficulty
         }
       }
     ]

     Design principle:
     - Main theory is open and continuous.
     - Examples are visible.
     - Exam traps are visible.
     - Advanced detail is optional.
     - Quick checks appear only at useful intervals.
     - Student progress persists locally.
  ========================================================= */

  function renderLesson(
    data = {},
    root
  ) {

    if (!root) {
      return;
    }

    const steps =
      data.lessonSteps ||
      [];

    if (!steps.length) {

      root.innerHTML = `
        <div class="ui-empty is-visible">
          No lesson content available.
        </div>
      `;

      return;
    }

    const pageKey =
      data.meta?.slug ||
      document.body.dataset.pageKey ||
      "lesson";

    const completedKey =
      `lesson-completed:${pageKey}`;

    const completed =
      new Set(
        loadJSON(
          completedKey,
          []
        )
      );

    const esc =
      value =>
        escapeHTML(
          value || ""
        );

    root.innerHTML = `

      <div class="ui-lesson">

        <!-- =========================
             LESSON INTRO
        ========================== -->

        <div class="ui-lesson-intro">

          <div class="ui-lesson-kicker">
            Guided learning
          </div>

          <h2 class="ui-lesson-heading">
            ${esc(
              data.meta?.lessonTitle ||
              data.meta?.title ||
              "Learn this topic"
            )}
          </h2>

          <p class="ui-lesson-lead">
            ${esc(
              data.meta?.lessonLead ||
              "Understand the idea first, then connect it to examples, exceptions and exam questions."
            )}
          </p>

          <div class="ui-lesson-map">

            <div class="ui-lesson-map-item">
              <strong>01</strong>
              <span>Big picture</span>
            </div>

            <div class="ui-lesson-map-item">
              <strong>02</strong>
              <span>Core ideas</span>
            </div>

            <div class="ui-lesson-map-item">
              <strong>03</strong>
              <span>Application</span>
            </div>

            <div class="ui-lesson-map-item">
              <strong>04</strong>
              <span>Exam traps</span>
            </div>

            <div class="ui-lesson-map-item">
              <strong>05</strong>
              <span>Recall</span>
            </div>

          </div>

        </div>

        <!-- =========================
             PROGRESS
        ========================== -->

        <div class="ui-lesson-progress">

          <div class="ui-lesson-progress-top">

            <span>
              Learning progress
            </span>

            <strong
              data-lesson-progress
            >
              0%
            </strong>

          </div>

          <div
            class="ui-lesson-progress-track"
          >

            <div
              class="ui-lesson-progress-fill"
              data-lesson-progress-fill
            ></div>

          </div>

        </div>

        <!-- =========================
             LESSON STEPS
        ========================== -->

        <div class="ui-lesson-stack">

          ${steps.map(
            (
              step,
              index
            ) => `

              <article
                class="ui-lesson-step"
                data-lesson-step="${index}"
              >

                <div
                  class="ui-lesson-step-head"
                >

                  <div
                    class="ui-lesson-step-number"
                  >
                    ${
                      String(
                        index + 1
                      ).padStart(
                        2,
                        "0"
                      )
                    }
                  </div>

                  <div>

                    <div
                      class="ui-lesson-step-kicker"
                    >
                      ${esc(
                        step.tag ||
                        "Core concept"
                      )}
                    </div>

                    <h3
                      class="ui-lesson-step-title"
                    >
                      ${esc(
                        step.title ||
                        `Lesson ${index + 1}`
                      )}
                    </h3>

                  </div>

                </div>

                <div
                  class="ui-lesson-body ui-prose"
                >

                  ${
                    step.bodyHtml ||
                    esc(
                      step.body ||
                      ""
                    )
                  }

                </div>

                ${
                  step.exampleHtml
                    ? `
                      <div
                        class="ui-lesson-example"
                      >

                        <div
                          class="ui-lesson-example-label"
                        >
                          Example
                        </div>

                        <p>
                          ${
                            step.exampleHtml
                          }
                        </p>

                      </div>
                    `
                    : ""
                }

                ${
                  step.trapHtml
                    ? `
                      <div
                        class="ui-lesson-trap"
                      >

                        <div
                          class="ui-lesson-trap-label"
                        >
                          Exam trap
                        </div>

                        <p>
                          ${
                            step.trapHtml
                          }
                        </p>

                      </div>
                    `
                    : ""
                }

                ${
                  step.deepHtml
                    ? `
                      <details
                        class="ui-lesson-deep"
                      >

                        <summary>
                          Dig deeper —
                          optional advanced detail
                        </summary>

                        <div
                          class="
                            ui-lesson-deep-content
                            ui-prose
                          "
                        >
                          ${
                            step.deepHtml
                          }
                        </div>

                      </details>
                    `
                    : ""
                }

                ${
                  step.quickCheck
                    ? `
                      <div
                        class="ui-lesson-check"
                        data-lesson-check="${index}"
                      >

                        <div
                          class="ui-lesson-check-head"
                        >

                          <span
                            class="
                              ui-lesson-check-label
                            "
                          >
                            Quick check
                          </span>

                          <span
                            class="ui-badge"
                          >
                            ${esc(
                              step.quickCheck
                                .difficulty ||
                              "Recall"
                            )}
                          </span>

                        </div>

                        <div
                          class="ui-lesson-check-question"
                        >
                          ${
                            step.quickCheck
                              .questionHtml ||
                            esc(
                              step.quickCheck
                                .question ||
                              ""
                            )
                          }
                        </div>

                        <div
                          class="
                            ui-lesson-check-options
                          "
                        >

                          ${
                            (
                              step
                                .quickCheck
                                .options ||
                              []
                            )
                              .map(
                                (
                                  option,
                                  i
                                ) => `

                                  <button
                                    class="
                                      ui-lesson-check-option
                                    "
                                    type="button"
                                    data-quick-answer="${i}"
                                  >

                                    <span
                                      class="
                                        ui-lesson-check-letter
                                      "
                                    >
                                      ${
                                        String.fromCharCode(
                                          65 + i
                                        )
                                      }
                                    </span>

                                    <span>
                                      ${esc(
                                        option
                                      )}
                                    </span>

                                  </button>

                                `
                              )
                              .join("")
                          }

                        </div>

                        <div
                          class="
                            ui-lesson-check-feedback
                          "
                          data-feedback
                        ></div>

                      </div>
                    `
                    : ""
                }

                <div
                  class="ui-lesson-step-footer"
                >

                  <button
                    class="
                      ui-lesson-complete
                      ${
                        completed.has(
                          index
                        )
                          ? "is-done"
                          : ""
                      }
                    "
                    type="button"
                    data-lesson-complete="${index}"
                  >

                    ${
                      completed.has(
                        index
                      )
                        ? "✓ Learned"
                        : "Mark learned"
                    }

                  </button>

                </div>

              </article>

            `
          ).join("")}

        </div>

        <!-- =========================
             NEXT ACTION
        ========================== -->

        <div
          class="ui-lesson-next"
        >

          <div>

            <strong>
              Lesson complete
            </strong>

            <span>
              Move to practice when
              the ideas are clear.
            </span>

          </div>

          <button
            type="button"
            data-lesson-next
          >
            Practice →
          </button>

        </div>

      </div>
    `;

    /* =====================================================
       PROGRESS
    ===================================================== */

    const progressLabel =
      $(
        "[data-lesson-progress]",
        root
      );

    const progressFill =
      $(
        "[data-lesson-progress-fill]",
        root
      );

    function updateProgress() {

      const percent =
        Math.round(
          (
            completed.size /
            steps.length
          ) * 100
        );

      if (progressLabel) {
        progressLabel.textContent =
          `${percent}%`;
      }

      if (progressFill) {
        progressFill.style.width =
          `${percent}%`;
      }
    }

    /* =====================================================
       MARK LEARNED
    ===================================================== */

    $$(
      "[data-lesson-complete]",
      root
    ).forEach(button => {

      button.addEventListener(
        "click",
        () => {

          const index =
            Number(
              button.dataset
                .lessonComplete
            );

          if (
            completed.has(
              index
            )
          ) {

            completed.delete(
              index
            );

            button.classList.remove(
              "is-done"
            );

            button.textContent =
              "Mark learned";

          } else {

            completed.add(
              index
            );

            button.classList.add(
              "is-done"
            );

            button.textContent =
              "✓ Learned";
          }

          saveJSON(
            completedKey,
            [...completed].sort(
              (a,b) => a - b
            )
          );

          updateProgress();
        }
      );

    });

    /* =====================================================
       QUICK CHECKS
    ===================================================== */

    $$(
      "[data-lesson-check]",
      root
    ).forEach(check => {

      const index =
        Number(
          check.dataset
            .lessonCheck
        );

      const model =
        steps[index]?.quickCheck;

      if (!model) {
        return;
      }

      const optionButtons =
        $$(
          "[data-quick-answer]",
          check
        );

      const feedback =
        $(
          "[data-feedback]",
          check
        );

      optionButtons.forEach(
        button => {

          button.addEventListener(
            "click",
            () => {

              const chosen =
                Number(
                  button.dataset
                    .quickAnswer
                );

              optionButtons.forEach(
                option => {

                  const optionIndex =
                    Number(
                      option.dataset
                        .quickAnswer
                    );

                  option.disabled =
                    true;

                  if (
                    optionIndex ===
                    Number(
                      model.answer
                    )
                  ) {

                    option.classList.add(
                      "is-correct"
                    );

                  }

                  if (
                    optionIndex ===
                      chosen &&
                    optionIndex !==
                      Number(
                        model.answer
                      )
                  ) {

                    option.classList.add(
                      "is-wrong"
                    );
                  }
                }
              );

              if (feedback) {

                feedback.innerHTML =
                  model.explanationHtml ||
                  esc(
                    model.explanation ||
                    ""
                  );

                feedback.classList.add(
                  "is-visible"
                );
              }
            }
          );
        }
      );
    });

    /* =====================================================
       MOVE TO PRACTICE
    ===================================================== */

    const next =
      $(
        "[data-lesson-next]",
        root
      );

    if (next) {

      next.addEventListener(
        "click",
        () => {

          const practice =
            document.querySelector(
              '[data-tab="practice"]'
            );

          if (practice) {

            practice.click();

            window.scrollTo({
              top:0,
              behavior:"smooth"
            });
          }

        }
      );
    }

    updateProgress();
  }

  /* =========================================================
     QUIZ
  ========================================================= */

  function renderQuiz(
    questions = [],
    root,
    options = {}
  ) {

    if (!root) {
      return;
    }

    const stateKey =
      `${
        options.storageKey ||
        "quiz"
      }:${location.pathname}`;

    const saved =
      loadJSON(
        stateKey,
        {
          index:0,
          answers:{},
          score:0,
          finished:false
        }
      );

    const state = {
      ...saved,
      questions,
      index:Math.min(
        saved.index || 0,
        Math.max(
          questions.length - 1,
          0
        )
      )
    };

    if (!questions.length) {

      root.innerHTML = `
        <div class="ui-empty is-visible">
          No questions available.
        </div>
      `;

      return;
    }

    const render = () => {

      const q =
        state.questions[
          state.index
        ];

      const answered =
        Object.prototype
          .hasOwnProperty.call(
            state.answers,
            state.index
          );

      const chosen =
        state.answers[
          state.index
        ];

      root.innerHTML = `

        <div class="ui-question">

          <div
            class="ui-badge-row"
          >

            <span
              class="ui-badge primary"
            >
              Question
              ${
                state.index + 1
              }/${
                state.questions.length
              }
            </span>

            ${
              q.difficulty
                ? `
                  <span class="ui-badge">
                    ${escapeHTML(
                      q.difficulty
                    )}
                  </span>
                `
                : ""
            }

            ${
              q.topic
                ? `
                  <span class="ui-badge">
                    ${escapeHTML(
                      q.topic
                    )}
                  </span>
                `
                : ""
            }

          </div>

          <div
            class="ui-question-stem"
          >
            ${
              q.questionHtml ||
              escapeHTML(
                q.question ||
                ""
              )
            }
          </div>

          <div class="ui-options">

            ${
              (q.options || [])
                .map(
                  (
                    option,
                    i
                  ) => {

                    const selected =
                      chosen === i;

                    const correct =
                      q.answer === i;

                    let cls =
                      "ui-option";

                    if (
                      answered &&
                      correct
                    ) {

                      cls +=
                        " is-correct";
                    }

                    if (
                      answered &&
                      selected &&
                      !correct
                    ) {

                      cls +=
                        " is-wrong";
                    }

                    return `

                      <button
                        class="${cls}"
                        type="button"
                        data-option="${i}"
                        ${
                          answered
                            ? "disabled"
                            : ""
                        }
                      >

                        <span
                          class="
                            ui-option-marker
                          "
                        >
                          ${
                            String.fromCharCode(
                              65 + i
                            )
                          }
                        </span>

                        <span>
                          ${
                            escapeHTML(
                              option
                            )
                          }
                        </span>

                      </button>

                    `;
                  }
                )
                .join("")
            }

          </div>

          <div
            class="
              ui-explanation
              ${
                answered
                  ? "is-visible"
                  : ""
              }
            "
          >
            ${
              q.explanationHtml ||
              escapeHTML(
                q.explanation ||
                ""
              )
            }
          </div>

          <div
            class="ui-question-footer"
          >

            <div
              class="ui-badge-row"
            >

              <span
                class="ui-badge"
              >
                ${
                  state.questions.length
                    ? Math.round(
                        (
                          Object.keys(
                            state.answers
                          ).length /
                          state.questions.length
                        ) * 100
                      )
                    : 0
                }% attempted
              </span>

            </div>

            <div
              class="ui-question-nav"
            >

              <button
                class="ui-btn"
                type="button"
                data-prev
                ${
                  state.index === 0
                    ? "disabled"
                    : ""
                }
              >
                ←
              </button>

              <button
                class="
                  ui-btn
                  ui-btn-primary
                "
                type="button"
                data-next
              >

                ${
                  state.index ===
                  state.questions.length - 1
                    ? "Finish"
                    : "Next →"
                }

              </button>

            </div>

          </div>

        </div>
      `;

      $$(
        "[data-option]",
        root
      ).forEach(
        button => {

          button.addEventListener(
            "click",
            () => {

              const selectedIndex =
                Number(
                  button.dataset
                    .option
                );

              state.answers[
                state.index
              ] =
                selectedIndex;

              saveJSON(
                stateKey,
                {
                  index:
                    state.index,

                  answers:
                    state.answers,

                  score:
                    state.score,

                  finished:
                    false
                }
              );

              render();
            }
          );
        }
      );

      const prev =
        $(
          "[data-prev]",
          root
        );

      const next =
        $(
          "[data-next]",
          root
        );

      if (prev) {

        prev.addEventListener(
          "click",
          () => {

            if (
              state.index > 0
            ) {

              state.index--;

              saveJSON(
                stateKey,
                {
                  index:
                    state.index,

                  answers:
                    state.answers,

                  score:
                    state.score,

                  finished:
                    false
                }
              );

              render();
            }
          }
        );
      }

      if (next) {

        next.addEventListener(
          "click",
          () => {

            if (!answered) {

              notify(
                "Answer the question first."
              );

              return;
            }

            if (
              state.index <
              state.questions.length - 1
            ) {

              state.index++;

              saveJSON(
                stateKey,
                {
                  index:
                    state.index,

                  answers:
                    state.answers,

                  score:
                    state.score,

                  finished:
                    false
                }
              );

              render();

            } else {

              state.finished =
                true;

              saveJSON(
                stateKey,
                {
                  index:
                    state.index,

                  answers:
                    state.answers,

                  score:
                    state.score,

                  finished:
                    true
                }
              );

              renderResults(
                root,
                state,
                options
              );
            }
          }
        );
      }
    };

    render();
  }

  /* =========================================================
     QUIZ RESULTS
  ========================================================= */

  function renderResults(
    root,
    state,
    options = {}
  ) {

    const total =
      state.questions.length;

    const answered =
      Object.keys(
        state.answers
      ).length;

    const score =
      state.questions.reduce(
        (
          totalScore,
          q,
          index
        ) =>
          totalScore +
          (
            state.answers[index] ===
            q.answer
              ? 1
              : 0
          ),
        0
      );

    const percent =
      total
        ? Math.round(
            (
              score /
              total
            ) * 100
          )
        : 0;

    const level =
      percent >= 90
        ? "Mastered"
        : percent >= 75
        ? "Strong"
        : percent >= 60
        ? "Developing"
        : percent >= 40
        ? "Weak"
        : "Relearn";

    root.innerHTML = `

      <div
        class="ui-grid ui-grid-2"
      >

        <div class="ui-card">

          <div
            class="ui-card-body"
            style="text-align:center"
          >

            <div
              class="ui-score-ring"
              style="--score:${percent}%"
            >

              <div>

                <strong>
                  ${percent}%
                </strong>

                <span>
                  score
                </span>

              </div>

            </div>

            <div
              class="ui-badge-row"
              style="
                justify-content:center;
                margin-top:14px;
              "
            >

              <span
                class="
                  ui-badge
                  primary
                "
              >
                ${escapeHTML(
                  level
                )}
              </span>

            </div>

          </div>

        </div>

        <div class="ui-card">

          <div
            class="ui-card-body"
          >

            <div
              class="ui-definition"
            >

              <span
                class="ui-definition-term"
              >
                Correct
              </span>

              <span
                class="
                  ui-definition-value
                "
              >
                ${score}/${total}
              </span>

            </div>

            <div
              style="height:8px"
            ></div>

            <div
              class="ui-definition"
            >

              <span
                class="ui-definition-term"
              >
                Attempted
              </span>

              <span
                class="
                  ui-definition-value
                "
              >
                ${answered}/${total}
              </span>

            </div>

            <div
              style="height:8px"
            ></div>

            <button
              class="
                ui-btn
                ui-btn-primary
              "
              type="button"
              data-retry
            >
              Retake Quiz
            </button>

          </div>

        </div>

      </div>
    `;

    const retry =
      $(
        "[data-retry]",
        root
      );

    if (retry) {

      retry.addEventListener(
        "click",
        () => {

          removeJSON(
            `${
              options.storageKey ||
              "quiz"
            }:${location.pathname}`
          );

          renderQuiz(
            state.questions,
            root,
            options
          );
        }
      );
    }

    document.dispatchEvent(
      new CustomEvent(
        "ui:quizcomplete",
        {
          detail:{
            score,
            total,
            percent,
            level
          }
        }
      )
    );
  }

  /* =========================================================
     FLASHCARDS
  ========================================================= */

  function renderFlashcards(
    cards = [],
    root
  ) {

    if (!root) {
      return;
    }

    if (!cards.length) {

      root.innerHTML = `
        <div
          class="
            ui-empty
            is-visible
          "
        >
          No flashcards available.
        </div>
      `;

      return;
    }

    let index = 0;

    const draw = () => {

      const card =
        cards[index];

      root.innerHTML = `

        <div
          class="
            ui-flashcard
          "
          data-flash
        >

          <div
            class="
              ui-flashcard-inner
            "
          >

            <div
              class="
                ui-flashface
                front
              "
            >

              <div>

                <div
                  class="
                    ui-badge
                    primary
                  "
                >
                  Question
                </div>

                <div
                  class="
                    ui-prose
                  "
                  style="
                    margin-top:12px
                  "
                >
                  ${
                    card.frontHtml ||
                    escapeHTML(
                      card.front ||
                      ""
                    )
                  }
                </div>

              </div>

            </div>

            <div
              class="
                ui-flashface
                back
              "
            >

              <div>

                <div
                  class="ui-badge"
                >
                  Answer
                </div>

                <div
                  class="
                    ui-prose
                  "
                  style="
                    margin-top:12px
                  "
                >
                  ${
                    card.backHtml ||
                    escapeHTML(
                      card.back ||
                      ""
                    )
                  }
                </div>

              </div>

            </div>

          </div>

        </div>

        <div
          class="ui-question-footer"
          style="
            margin-top:10px
          "
        >

          <span
            class="ui-badge"
          >
            ${index + 1}/${cards.length}
          </span>

          <div
            class="ui-question-nav"
          >

            <button
              class="ui-btn"
              type="button"
              data-prev
            >
              ←
            </button>

            <button
              class="
                ui-btn
                ui-btn-primary
              "
              type="button"
              data-flip
            >
              Flip
            </button>

            <button
              class="ui-btn"
              type="button"
              data-next
            >
              →
            </button>

          </div>

        </div>
      `;

      const flash =
        $(
          "[data-flash]",
          root
        );

      $(
        "[data-flip]",
        root
      )?.addEventListener(
        "click",
        () =>
          flash.classList.toggle(
            "is-flipped"
          )
      );

      $(
        "[data-prev]",
        root
      )?.addEventListener(
        "click",
        () => {

          index =
            (
              index -
              1 +
              cards.length
            ) %
            cards.length;

          draw();
        }
      );

      $(
        "[data-next]",
        root
      )?.addEventListener(
        "click",
        () => {

          index =
            (
              index +
              1
            ) %
            cards.length;

          draw();
        }
      );

      flash?.addEventListener(
        "click",
        () =>
          flash.classList.toggle(
            "is-flipped"
          )
      );
    };

    draw();
  }

  /* =========================================================
     MISTAKE BOOK
  ========================================================= */

  function renderMistakes(
    root,
    pageKey
  ) {

    if (!root) {
      return;
    }

    const key =
      `mistakes:${pageKey}`;

    const items =
      loadJSON(
        key,
        []
      );

    if (!items.length) {

      root.innerHTML = `
        <div
          class="
            ui-empty
            is-visible
          "
        >
          No saved mistakes yet.
        </div>
      `;

      return;
    }

    root.innerHTML = `

      <div class="ui-grid">

        ${
          items
            .map(
              (
                item,
                index
              ) => `

                <article
                  class="ui-mistake-item"
                >

                  <strong>
                    ${escapeHTML(
                      item.question ||
                      "Question"
                    )}
                  </strong>

                  <span>
                    Saved
                    ${escapeHTML(
                      item.date ||
                      ""
                    )}
                  </span>

                  <div
                    class="ui-prose"
                  >
                    ${
                      item.noteHtml ||
                      escapeHTML(
                        item.note ||
                        ""
                      )
                    }
                  </div>

                  <button
                    class="ui-btn"
                    type="button"
                    data-remove-mistake="${index}"
                  >
                    Remove
                  </button>

                </article>
              `
            )
            .join("")
        }

      </div>
    `;

    $$(
      "[data-remove-mistake]",
      root
    ).forEach(
      button => {

        button.addEventListener(
          "click",
          () => {

            const index =
              Number(
                button.dataset
                  .removeMistake
              );

            items.splice(
              index,
              1
            );

            saveJSON(
              key,
              items
            );

            renderMistakes(
              root,
              pageKey
            );
          }
        );
      }
    );
  }

  function saveMistake(
    pageKey,
    item
  ) {

    const key =
      `mistakes:${pageKey}`;

    const items =
      loadJSON(
        key,
        []
      );

    items.unshift({
      id:
        uid(
          "mistake"
        ),

      date:
        new Date()
          .toLocaleDateString(),

      ...item
    });

    saveJSON(
      key,
      items.slice(
        0,
        100
      )
    );

    notify(
      "Saved to your mistake book.",
      "success"
    );
  }

  /* =========================================================
     REVEAL ANIMATION
  ========================================================= */

  function initReveal(
    root = document
  ) {

    const nodes =
      $$(".ui-reveal", root);

    if (
      !(
        "IntersectionObserver"
        in window
      )
    ) {

      nodes.forEach(
        node =>
          node.classList.add(
            "is-visible"
          )
      );

      return;
    }

    const observer =
      new IntersectionObserver(
        entries => {

          entries.forEach(
            entry => {

              if (
                entry.isIntersecting
              ) {

                entry.target.classList.add(
                  "is-visible"
                );

                observer.unobserve(
                  entry.target
                );
              }
            }
          );

        },
        {
          threshold:.08
        }
      );

    nodes.forEach(
      node =>
        observer.observe(
          node
        )
    );
  }

  /* =========================================================
     MASTER MOUNT
  ========================================================= */

  function mountContent(
    config = {}
  ) {

    /*
      API should generate CONTENT JSON ONLY.

      Example:

      {
        meta:{...},

        lessonSteps: [
          {
            title,
            tag,
            bodyHtml,
            exampleHtml,
            trapHtml,
            deepHtml,

            quickCheck:{
              questionHtml,
              options:[],
              answer,
              explanation,
              difficulty
            }
          }
        ],

        concepts:[],
        practice:[],
        upscQuiz:[],
        pyqs:[],

        revision:{
          oneMinute:[],
          fiveMinute:[],
          examDay:[]
        },

        flashcards:[],

        miniTests:{
          foundation:[],
          apfc:[],
          challenge:[]
        },

        currentUpdates:[],
        faqs:[]
      }
    */

    const data =
      config.data ||
      window.APFC_CONTENT ||
      {};

    const pageKey =
      getPageKey(
        config
      );

    initTabs(
      document
    );

    initAccordions(
      document
    );

    initReveal(
      document
    );

    /* -----------------------------
       Guided lesson
    ----------------------------- */

    if (
      config.targets?.lesson
    ) {

      renderLesson(
        data,
        $(
          config.targets.lesson
        )
      );
    }

    /* -----------------------------
       Search
    ----------------------------- */

    if (
      config.search
    ) {

      initSearch(
        config.search
      );

      initSearchClear(
        config.search.input ||
        "[data-ui-search]",

        config.search.clear ||
        "[data-ui-search-clear]"
      );
    }

    /* -----------------------------
       Legacy/reference concepts
    ----------------------------- */

    if (
      config.targets?.concepts
    ) {

      renderConcepts(
        data.concepts ||
        [],

        $(
          config.targets
            .concepts
        )
      );
    }

    /* -----------------------------
       Practice
    ----------------------------- */

    if (
      config.targets?.practice
    ) {

      renderQuiz(
        data.practice ||
        [],

        $(
          config.targets
            .practice
        ),

        {
          storageKey:
            `${pageKey}:practice`
        }
      );
    }

    /* -----------------------------
       UPSC quiz
    ----------------------------- */

    if (
      config.targets?.upscQuiz
    ) {

      renderQuiz(
        data.upscQuiz ||
        [],

        $(
          config.targets
            .upscQuiz
        ),

        {
          storageKey:
            `${pageKey}:upsc`
        }
      );
    }

    /* -----------------------------
       PYQs
    ----------------------------- */

    if (
      config.targets?.pyqs
    ) {

      renderConcepts(
        data.pyqs ||
        [],

        $(
          config.targets
            .pyqs
        )
      );
    }

    /* -----------------------------
       Revision
    ----------------------------- */

    if (
      config.targets?.revision
    ) {

      const target =
        $(
          config.targets
            .revision
        );

      if (target) {

        if (
          data.revisionHtml
        ) {

          target.innerHTML =
            data.revisionHtml;

        } else if (
          typeof data.revision ===
          "string"
        ) {

          target.innerHTML =
            escapeHTML(
              data.revision
            );

        } else {

          const revision =
            data.revision ||
            {};

          const format =
            array =>
              Array.isArray(
                array
              )
                ? `
                  <div class="ui-prose">
                    <ol>
                      ${
                        array
                          .map(
                            item =>
                              `<li>${escapeHTML(
                                item
                              )}</li>`
                          )
                          .join("")
                      }
                    </ol>
                  </div>
                `
                : "";

          target.innerHTML = `

            ${
              revision.oneMinute
                ? `
                  <div
                    class="ui-card"
                  >

                    <div
                      class="ui-card-head"
                    >
                      <h3
                        class="ui-card-title"
                      >
                        1-Minute Revision
                      </h3>
                    </div>

                    <div
                      class="ui-card-body"
                    >
                      ${format(
                        revision.oneMinute
                      )}
                    </div>

                  </div>
                `
                : ""
            }

            ${
              revision.fiveMinute
                ? `
                  <div
                    class="ui-card"
                  >

                    <div
                      class="ui-card-head"
                    >
                      <h3
                        class="ui-card-title"
                      >
                        5-Minute Revision
                      </h3>
                    </div>

                    <div
                      class="ui-card-body"
                    >
                      ${format(
                        revision.fiveMinute
                      )}
                    </div>

                  </div>
                `
                : ""
            }

            ${
              revision.examDay
                ? `
                  <div
                    class="ui-card"
                  >

                    <div
                      class="ui-card-head"
                    >
                      <h3
                        class="ui-card-title"
                      >
                        Exam-Day Revision
                      </h3>
                    </div>

                    <div
                      class="ui-card-body"
                    >
                      ${format(
                        revision.examDay
                      )}
                    </div>

                  </div>
                `
                : ""
            }
          `;
        }
      }
    }

    /* -----------------------------
       Flashcards
    ----------------------------- */

    if (
      config.targets?.flashcards
    ) {

      renderFlashcards(
        data.flashcards ||
        [],

        $(
          config.targets
            .flashcards
        )
      );
    }

    /* -----------------------------
       Mini tests
    ----------------------------- */

    if (
      config.targets?.miniTests
    ) {

      const root =
        $(
          config.targets
            .miniTests
        );

      if (root) {

        const tests =
          data.miniTests ||
          {};

        root.innerHTML = `

          <div
            class="ui-level-grid"
          >

            <article
              class="ui-level-card"
            >

              <strong>
                Level 1 —
                Foundation
              </strong>

              <span>
                Core understanding
              </span>

              <button
                class="
                  ui-btn
                  ui-btn-primary
                "
                type="button"
                data-test="foundation"
                style="
                  margin-top:10px
                "
              >
                Start Test
              </button>

            </article>

            <article
              class="ui-level-card"
            >

              <strong>
                Level 2 —
                APFC
              </strong>

              <span>
                Applied exam preparation
              </span>

              <button
                class="
                  ui-btn
                  ui-btn-primary
                "
                type="button"
                data-test="apfc"
                style="
                  margin-top:10px
                "
              >
                Start Test
              </button>

            </article>

            <article
              class="ui-level-card"
            >

              <strong>
                Level 3 —
                UPSC Challenge
              </strong>

              <span>
                High-difficulty reasoning
              </span>

              <button
                class="
                  ui-btn
                  ui-btn-primary
                "
                type="button"
                data-test="challenge"
                style="
                  margin-top:10px
                "
              >
                Start Test
              </button>

            </article>

          </div>

          <div
            data-mini-test-engine
            style="
              margin-top:12px
            "
          ></div>
        `;

        const engine =
          $(
            "[data-mini-test-engine]",
            root
          );

        $$(
          "[data-test]",
          root
        ).forEach(
          button => {

            button.addEventListener(
              "click",
              () => {

                const testKey =
                  button.dataset.test;

                renderQuiz(
                  tests[testKey] ||
                  [],

                  engine,

                  {
                    storageKey:
                      `${pageKey}:mini:${testKey}`
                  }
                );

                engine.scrollIntoView({
                  behavior:
                    "smooth",

                  block:
                    "start"
                });
              }
            );
          }
        );
      }
    }

    /* -----------------------------
       Current updates
    ----------------------------- */

    if (
      config.targets
        ?.currentUpdates
    ) {

      renderConcepts(
        data.currentUpdates ||
        [],

        $(
          config.targets
            .currentUpdates
        )
      );
    }

    /* -----------------------------
       FAQs
    ----------------------------- */

    if (
      config.targets?.faqs
    ) {

      renderConcepts(
        data.faqs ||
        [],

        $(
          config.targets
            .faqs
        )
      );
    }

    /* -----------------------------
       Mistakes
    ----------------------------- */

    if (
      config.targets?.mistakes
    ) {

      renderMistakes(
        $(
          config.targets
            .mistakes
        ),

        pageKey
      );
    }

    /* -----------------------------
       Ready event
    ----------------------------- */

    document.dispatchEvent(
      new CustomEvent(
        "ui:ready",
        {
          detail:{
            pageKey,
            data
          }
        }
      )
    );

    return {

      data,

      pageKey,

      notify,

      saveMistake:
        item =>
          saveMistake(
            pageKey,
            item
          ),

      load:
        (
          key,
          fallback
        ) =>
          loadJSON(
            `${pageKey}:${key}`,
            fallback
          ),

      save:
        (
          key,
          value
        ) =>
          saveJSON(
            `${pageKey}:${key}`,
            value
          ),

      remove:
        key =>
          removeJSON(
            `${pageKey}:${key}`
          )
    };
  }

  /* =========================================================
     PUBLIC API
  ========================================================= */

  window.UPSCAPFC = {

    version:
      "2.0.0",

    mount:
      mountContent,

    tabs:
      initTabs,

    accordions:
      initAccordions,

    search:
      initSearch,

    lesson:
      renderLesson,

    quiz:
      renderQuiz,

    flashcards:
      renderFlashcards,

    concepts:
      renderConcepts,

    mistakes:
      renderMistakes,

    saveMistake,

    notify,

    escapeHTML,

    slugify
  };

  /* =========================================================
     AUTO MOUNT
  ========================================================= */

  document.addEventListener(
    "DOMContentLoaded",
    () => {

      if (
        window.APFC_CONFIG
      ) {

        window.APFC_APP =
          mountContent(
            window.APFC_CONFIG
          );
      }

    }
  );

})();