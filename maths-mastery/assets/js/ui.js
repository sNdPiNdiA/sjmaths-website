/* ============================================================
   SJMaths Maths Mastery
   STEP 32.15
   LEARNER ONBOARDING UI
   ============================================================ */

export function getScreen() {

    return document.getElementById(
        "mastery-screen"
    );

}


export function updateHeaderContext({
    targetName = null,
    statusText = null,
    visible = false
} = {}) {

    const container = document.getElementById("header-learner-context");
    const targetEl = document.getElementById("header-target-name");
    const statusEl = document.getElementById("header-status-text");

    if (!container) return;

    if (!visible || !targetName) {
        container.hidden = true;
        return;
    }

    if (targetEl) targetEl.textContent = targetName;
    if (statusEl) statusEl.textContent = statusText || "Active";
    container.hidden = false;
}


/* ============================================================
   WELCOME
   ============================================================ */

export function renderWelcome({
    onStart = null,
    onSelectTarget = null,
    onStageClick = null
} = {}) {

    const screen = getScreen();

    if (!screen) return;

    updateHeaderContext({ visible: false });

    screen.innerHTML = `

        <div class="mastery-page">

            <section class="mastery-hero">

                <div class="mastery-hero__main">

                    <div class="mastery-eyebrow">
                        SJMaths Adaptive Learning System
                    </div>

                    <h1>
                        Master maths.
                        <span>Step by step.</span>
                    </h1>

                    <p class="mastery-hero__text">
                        A precision learning engine that diagnoses prerequisite gaps,
                        targets micro-interventions, and adapts to your performance with every question.
                    </p>

                    <div class="mastery-hero__actions">

                        <button
                            id="start-mastery-button"
                            class="mastery-button mastery-button--primary"
                            type="button"
                        >
                            Start learning
                            <span aria-hidden="true">→</span>
                        </button>

                        <div class="mastery-hero__note">
                            <span class="mastery-status-dot"></span>
                            Live prerequisite graph & adaptive diagnostic engine
                        </div>

                    </div>

                </div>


                <div
                    class="mastery-hero__visual"
                >

                    <div class="mastery-path-card">

                        <div class="mastery-path-card__header">

                            <span>
                                ADAPTIVE JOURNEY
                            </span>

                            <span>
                                01 / 03
                            </span>

                        </div>


                        <div class="mastery-path">

                            <div 
                                class="mastery-path__item mastery-path__item--active mastery-path__item--interactive"
                                data-stage="1"
                                title="Click to start direct target diagnostic"
                            >

                                <div class="mastery-path__icon">
                                    1
                                </div>

                                <div>

                                    <strong>
                                        Target & Diagnose
                                    </strong>

                                    <small>
                                        Identify prerequisite readiness
                                    </small>

                                </div>

                            </div>


                            <div class="mastery-path__line"></div>


                            <div 
                                class="mastery-path__item mastery-path__item--interactive"
                                data-stage="2"
                                title="Click to view target practice catalog"
                            >

                                <div class="mastery-path__icon">
                                    2
                                </div>

                                <div>

                                    <strong>
                                        Targeted Remediation
                                    </strong>

                                    <small>
                                        Fill foundational gaps first
                                    </small>

                                </div>

                            </div>


                            <div class="mastery-path__line"></div>


                            <div 
                                class="mastery-path__item mastery-path__item--interactive"
                                data-stage="3"
                                title="Click to view mastery goals"
                            >

                                <div class="mastery-path__icon">
                                    3
                                </div>

                                <div>

                                    <strong>
                                        Target Mastery
                                    </strong>

                                    <small>
                                        Verify comprehensive understanding
                                    </small>

                                </div>

                            </div>

                        </div>


                        <div class="mastery-path-card__footer">

                            <span>
                                Interactive Adaptive Control
                            </span>

                            <span>
                                ⚡ Active
                            </span>

                        </div>

                    </div>

                </div>

            </section>


            <!-- ========================================================
                 BELOW-HERO CONTROL DECK / QUICK-START TARGETS
                 ======================================================== -->

            <section class="mastery-deck">

                <div class="mastery-deck__header">
                    <span class="mastery-deck__kicker">FEATURED TARGET CURRICULUM</span>
                    <h2>Choose a target to evaluate readiness</h2>
                    <p>Select any topic to run live prerequisite diagnosis and start adaptive remediation.</p>
                </div>

                <div class="mastery-target-grid">

                    <button
                        type="button"
                        class="mastery-target-card"
                        data-quick-target="quadratic.factorisation"
                    >
                        <div class="mastery-target-card__top">
                            <span class="mastery-target-badge mastery-target-badge--core">Core Algebra</span>
                            <span class="mastery-target-badge">15 Prerequisites</span>
                        </div>
                        <div>
                            <h3>Quadratic Factorisation</h3>
                            <p>Splitting the middle term, algebraic identities, and factoring polynomial expressions.</p>
                        </div>
                        <div class="mastery-target-card__footer">
                            <span>Evaluate Readiness</span>
                            <span>→</span>
                        </div>
                    </button>

                    <button
                        type="button"
                        class="mastery-target-card"
                        data-quick-target="linear-equations-two-variables.graph"
                    >
                        <div class="mastery-target-card__top">
                            <span class="mastery-target-badge mastery-target-badge--core">Coordinate Algebra</span>
                            <span class="mastery-target-badge">Foundational</span>
                        </div>
                        <div>
                            <h3>Linear Equations</h3>
                            <p>Graphical representations, solutions of pairs of linear equations, and coordinate graphing.</p>
                        </div>
                        <div class="mastery-target-card__footer">
                            <span>Evaluate Readiness</span>
                            <span>→</span>
                        </div>
                    </button>

                    <button
                        type="button"
                        class="mastery-target-card"
                        data-quick-target="percentage.basic"
                    >
                        <div class="mastery-target-card__top">
                            <span class="mastery-target-badge mastery-target-badge--core">Applied Arithmetic</span>
                            <span class="mastery-target-badge">High Frequency</span>
                        </div>
                        <div>
                            <h3>Percentages & Fractions</h3>
                            <p>Percentage conversions, fractional parts, change ratios, and practical problem solving.</p>
                        </div>
                        <div class="mastery-target-card__footer">
                            <span>Evaluate Readiness</span>
                            <span>→</span>
                        </div>
                    </button>

                    <button
                        type="button"
                        class="mastery-target-card"
                        data-quick-target="ratio-proportion.proportion"
                    >
                        <div class="mastery-target-card__top">
                            <span class="mastery-target-badge mastery-target-badge--core">Proportions</span>
                            <span class="mastery-target-badge">Foundational</span>
                        </div>
                        <div>
                            <h3>Ratio & Proportion</h3>
                            <p>Simplifying ratios, direct and inverse variations, and comparative quantities.</p>
                        </div>
                        <div class="mastery-target-card__footer">
                            <span>Evaluate Readiness</span>
                            <span>→</span>
                        </div>
                    </button>

                </div>

            </section>

        </div>
    `;

    const button = document.getElementById("start-mastery-button");
    if (button && onStart) {
        button.addEventListener("click", onStart);
    }

    screen.querySelectorAll("[data-stage]").forEach(stageEl => {
        stageEl.addEventListener("click", () => {
            const stage = stageEl.dataset.stage;
            if (onStageClick) {
                onStageClick(stage);
            } else if (onStart) {
                onStart();
            }
        });
    });

    screen.querySelectorAll("[data-quick-target]").forEach(card => {
        card.addEventListener("click", () => {
            const targetId = card.dataset.quickTarget;
            if (onSelectTarget) {
                onSelectTarget(targetId);
            } else if (onStart) {
                onStart();
            }
        });
    });
}


/* ============================================================
   ONBOARDING
   ============================================================ */

export function renderOnboarding({
    onExam = null,
    onFoundation = null,
    onDiagnostic = null
} = {}) {

    const screen = getScreen();

    if (!screen) return;


    screen.innerHTML = `

        <div class="mastery-page">

            <div class="mastery-flow-top">

                <button
                    type="button"
                    class="mastery-back-button"
                    data-onboarding-back
                >
                    <span>←</span>
                    Back
                </button>

                <span class="mastery-flow-step">
                    STEP 1 OF 3
                </span>

            </div>


            <section class="mastery-onboarding-header">

                <span class="mastery-onboarding-kicker">
                    PERSONALISE YOUR JOURNEY
                </span>

                <h1>
                    How do you want to learn?
                </h1>

                <p>
                    Maths Mastery can adapt your learning path
                    around your exam goal, your foundation level,
                    or your current knowledge.
                </p>

            </section>


            <section class="mastery-route-grid">


                <button
                    type="button"
                    class="mastery-route-card"
                    data-route="exam"
                >

                    <div class="mastery-route-card__icon">
                        EXAM
                    </div>

                    <div class="mastery-route-card__body">

                        <span class="mastery-route-card__eyebrow">
                            Goal focused
                        </span>

                        <h2>
                            Prepare for an exam
                        </h2>

                        <p>
                            Follow a structured path built
                            around your examination goal.
                        </p>

                    </div>

                    <span class="mastery-route-card__arrow">
                        →
                    </span>

                </button>


                <button
                    type="button"
                    class="mastery-route-card"
                    data-route="foundation"
                >

                    <div class="mastery-route-card__icon">
                        BASE
                    </div>

                    <div class="mastery-route-card__body">

                        <span class="mastery-route-card__eyebrow">
                            Build confidence
                        </span>

                        <h2>
                            Build your foundations
                        </h2>

                        <p>
                            Start from the fundamentals and
                            strengthen your mathematical base.
                        </p>

                    </div>

                    <span class="mastery-route-card__arrow">
                        →
                    </span>

                </button>


                <button
                    type="button"
                    class="mastery-route-card"
                    data-route="diagnostic"
                >

                    <div class="mastery-route-card__icon">
                        TEST
                    </div>

                    <div class="mastery-route-card__body">

                        <span class="mastery-route-card__eyebrow">
                            Find your level
                        </span>

                        <h2>
                            Take a diagnostic
                        </h2>

                        <p>
                            Let Maths Mastery identify a
                            suitable starting point for you.
                        </p>

                    </div>

                    <span class="mastery-route-card__arrow">
                        →
                    </span>

                </button>


            </section>

        </div>
    `;


    screen
        .querySelector(
            "[data-route='exam']"
        )
        ?.addEventListener(
            "click",
            () => onExam?.()
        );


    screen
        .querySelector(
            "[data-route='foundation']"
        )
        ?.addEventListener(
            "click",
            () => onFoundation?.()
        );


    screen
        .querySelector(
            "[data-route='diagnostic']"
        )
        ?.addEventListener(
            "click",
            () => onDiagnostic?.()
        );

}


/* ============================================================
   EXAM SELECTION
   ============================================================ */

export function renderExamSelection({
    exams = [],
    onSelect = null,
    onBack = null
} = {}) {

    const screen = getScreen();

    if (!screen) return;


    const validExams =
        Array.isArray(exams)
            ? exams
            : [];


    screen.innerHTML = `

        <div class="mastery-page">

            <div class="mastery-flow-top">

                <button
                    type="button"
                    class="mastery-back-button"
                    data-back
                >
                    ← Back
                </button>

                <span class="mastery-flow-step">
                    STEP 2 OF 3
                </span>

            </div>


            <section class="mastery-onboarding-header">

                <span class="mastery-onboarding-kicker">
                    EXAM GOAL
                </span>

                <h1>
                    What are you preparing for?
                </h1>

                <p>
                    Choose your exam path so the learning
                    system can personalise what comes next.
                </p>

            </section>


            <section class="mastery-route-list">

                ${
                    validExams.length
                        ? validExams.map(
                            exam => `

                                <button
                                    type="button"
                                    class="mastery-route-card mastery-route-card--compact"
                                    data-exam-id="${escapeHtml(
                                        exam.id
                                    )}"
                                >

                                    <div class="mastery-route-card__icon">
                                        ${escapeHtml(
                                            exam.code ||
                                            "EXAM"
                                        )}
                                    </div>

                                    <div class="mastery-route-card__body">

                                        <h2>
                                            ${escapeHtml(
                                                exam.name ||
                                                exam.title ||
                                                exam.id
                                            )}
                                        </h2>

                                        <p>
                                            ${escapeHtml(
                                                exam.description ||
                                                "Personalised exam preparation."
                                            )}
                                        </p>

                                    </div>

                                    <span class="mastery-route-card__arrow">
                                        →
                                    </span>

                                </button>
                            `
                        ).join("")
                        : `
                            <div class="mastery-empty-state">

                                <div class="mastery-empty-state__icon">
                                    i
                                </div>

                                <h2>
                                    Exam routes are loading
                                </h2>

                                <p>
                                    The configured exam routes
                                    are not currently exposed
                                    by the application state.
                                </p>

                            </div>
                        `
                }

            </section>

        </div>
    `;


    screen
        .querySelector(
            "[data-back]"
        )
        ?.addEventListener(
            "click",
            () => onBack?.()
        );


    screen
        .querySelectorAll(
            "[data-exam-id]"
        )
        .forEach(
            button => {

                button.addEventListener(
                    "click",
                    () => {

                        onSelect?.(
                            button.dataset.examId
                        );

                    }
                );

            }
        );

}


/* ============================================================
   FOUNDATION
   ============================================================ */

export function renderFoundation({
    onSelect = null,
    onDiagnostic = null,
    onBack = null
} = {}) {

    const screen = getScreen();

    if (!screen) return;


    screen.innerHTML = `

        <div class="mastery-page">

            <div class="mastery-flow-top">

                <button
                    type="button"
                    class="mastery-back-button"
                    data-back
                >
                    ← Back
                </button>

                <span class="mastery-flow-step">
                    STEP 2 OF 3
                </span>

            </div>


            <section class="mastery-onboarding-header">

                <span class="mastery-onboarding-kicker">
                    FOUNDATION
                </span>

                <h1>
                    Where should we begin?
                </h1>

                <p>
                    Start from the mathematical foundation
                    that matches your current learning route.
                </p>

            </section>


            <section class="mastery-route-list">

                <button
                    type="button"
                    class="mastery-route-card mastery-route-card--compact"
                    data-foundation="number-system"
                >

                    <div class="mastery-route-card__icon">
                        01
                    </div>

                    <div class="mastery-route-card__body">

                        <span class="mastery-route-card__eyebrow">
                            Foundation route
                        </span>

                        <h2>
                            Number System
                        </h2>

                        <p>
                            Establish the numerical foundation
                            required for later mathematics.
                        </p>

                    </div>

                    <span class="mastery-route-card__arrow">
                        →
                    </span>

                </button>

            </section>


            <div class="mastery-secondary-action">

                <button
                    type="button"
                    class="mastery-text-button"
                    data-diagnostic
                >
                    Prefer to find your level first?
                    <span>Take a diagnostic →</span>
                </button>

            </div>

        </div>
    `;


    screen
        .querySelector(
            "[data-back]"
        )
        ?.addEventListener(
            "click",
            () => onBack?.()
        );


    screen
        .querySelector(
            "[data-foundation]"
        )
        ?.addEventListener(
            "click",
            () => {

                onSelect?.(
                    "number-system"
                );

            }
        );


    screen
        .querySelector(
            "[data-diagnostic]"
        )
        ?.addEventListener(
            "click",
            () => onDiagnostic?.()
        );

}


/* ============================================================
   DIAGNOSTIC
   ============================================================ */

export function renderDiagnosticIntro({
    onBegin = null,
    onBack = null
} = {}) {

    const screen = getScreen();

    if (!screen) return;


    screen.innerHTML = `

        <div class="mastery-page">

            <div class="mastery-flow-top">

                <button
                    type="button"
                    class="mastery-back-button"
                    data-back
                >
                    ← Back
                </button>

                <span class="mastery-flow-step">
                    STEP 2 OF 3
                </span>

            </div>


            <section class="mastery-diagnostic">

                <span class="mastery-onboarding-kicker">
                    DIAGNOSTIC
                </span>

                <h1>
                    Let's find your starting point.
                </h1>

                <p>
                    A diagnostic helps Maths Mastery understand
                    your current level so the next learning step
                    is more relevant.
                </p>


                <div class="mastery-diagnostic-points">

                    <div>
                        <strong>
                            No pressure
                        </strong>

                        <span>
                            It is used to understand your starting
                            point, not simply to give you a score.
                        </span>
                    </div>


                    <div>
                        <strong>
                            Personalised
                        </strong>

                        <span>
                            The result can guide the learning path
                            that follows.
                        </span>
                    </div>


                    <div>
                        <strong>
                            Useful evidence
                        </strong>

                        <span>
                            Your performance becomes part of the
                            learner state.
                        </span>
                    </div>

                </div>


                <button
                    type="button"
                    class="mastery-button mastery-button--primary"
                    data-begin
                >
                    Begin diagnostic
                    <span>→</span>
                </button>

            </section>

        </div>
    `;


    screen
        .querySelector(
            "[data-back]"
        )
        ?.addEventListener(
            "click",
            () => onBack?.()
        );


    screen
        .querySelector(
            "[data-begin]"
        )
        ?.addEventListener(
            "click",
            () => onBegin?.()
        );

}


/* ============================================================
   HELPERS
   ============================================================ */

export function showStatus(
    message
) {

    const status =
        document.getElementById(
            "mastery-status"
        );

    if (!status) return;


    status.textContent =
        message;

    status.hidden =
        false;


    clearTimeout(
        showStatus.timer
    );


    showStatus.timer =
        setTimeout(
            () => {

                status.hidden =
                    true;

            },
            3000
        );

}


export function renderError(
    message
) {

    const screen =
        getScreen();

    if (!screen) return;


    screen.innerHTML = `

        <div class="mastery-page">

            <div class="mastery-error">

                <strong>
                    Maths Mastery could not continue.
                </strong>

                <p>
                    ${escapeHtml(message)}
                </p>

            </div>

        </div>
    `;

}


function escapeHtml(
    value
) {

    return String(
        value ?? ""
    )

    .replaceAll(
        "&",
        "&amp;"
    )

    .replaceAll(
        "<",
        "&lt;"
    )

    .replaceAll(
        ">",
        "&gt;"
    )

    .replaceAll(
        '"',
        "&quot;"
    )

    .replaceAll(
        "'",
        "&#039;"
    );

}

/* ============================================================
   STEP 32.21 — SYLLABUS OVERVIEW
   ============================================================ */

export function renderSyllabusOverview({
    syllabus,
    onBack = null,
    onStart = null
} = {}) {

    const screen =
        getScreen();

    if (!screen) {
        return;
    }


    const sections =
        Array.isArray(
            syllabus?.sections
        )
            ? syllabus.sections
            : [];


    const topicCount =
        sections.reduce(
            (
                total,
                section
            ) =>
                total +
                (
                    Array.isArray(
                        section.topics
                    )
                        ? section.topics.length
                        : 0
                ),
            0
        );


    screen.innerHTML = `

        <div class="mastery-page">

            <div class="mastery-flow-top">

                <button
                    type="button"
                    class="mastery-back-button"
                    data-syllabus-back
                >
                    ← Back
                </button>

                <span class="mastery-flow-step">
                    YOUR SYLLABUS
                </span>

            </div>


            <section class="mastery-syllabus-header">

                <span class="mastery-onboarding-kicker">
                    ${escapeHtml(
                        syllabus?.subject ||
                        "MATHEMATICS"
                    )}
                </span>

                <h1>
                    ${escapeHtml(
                        syllabus?.name ||
                        "Your syllabus"
                    )}
                </h1>

                <p>
                    ${escapeHtml(
                        syllabus?.description ||
                        "A structured learning path for your selected exam."
                    )}
                </p>


                <div class="mastery-syllabus-stats">

                    <div>
                        <strong>
                            ${sections.length}
                        </strong>

                        <span>
                            Sections
                        </span>
                    </div>


                    <div>
                        <strong>
                            ${topicCount}
                        </strong>

                        <span>
                            Topics
                        </span>
                    </div>

                </div>

            </section>


            <section class="mastery-syllabus-sections">

                ${
                    sections.map(
                        section => `

                            <article
                                class="mastery-syllabus-section"
                            >

                                <div
                                    class="mastery-syllabus-section__header"
                                >

                                    <div>

                                        <span>
                                            SECTION ${
                                                escapeHtml(
                                                    String(
                                                        section.order ||
                                                        ""
                                                    )
                                                )
                                            }
                                        </span>

                                        <h2>
                                            ${escapeHtml(
                                                section.name ||
                                                section.id
                                            )}
                                        </h2>

                                    </div>

                                    <small>
                                        ${
                                            Array.isArray(
                                                section.topics
                                            )
                                                ? section.topics.length
                                                : 0
                                        }
                                        topics
                                    </small>

                                </div>


                                <div
                                    class="mastery-syllabus-topic-list"
                                >

                                    ${
                                        (
                                            Array.isArray(
                                                section.topics
                                            )
                                                ? section.topics
                                                : []
                                        )
                                        .sort(
                                            (
                                                a,
                                                b
                                            ) =>
                                                (
                                                    a.order || 0
                                                ) -
                                                (
                                                    b.order || 0
                                                )
                                        )
                                        .map(
                                            (
                                                topic,
                                                index
                                            ) => `

                                                <div
                                                    class="mastery-syllabus-topic"
                                                >

                                                    <span
                                                        class="mastery-syllabus-topic__number"
                                                    >
                                                        ${String(
                                                            index + 1
                                                        ).padStart(
                                                            2,
                                                            "0"
                                                        )}
                                                    </span>


                                                    <div
                                                        class="mastery-syllabus-topic__body"
                                                    >

                                                        <strong>
                                                            ${escapeHtml(
                                                                topic.name ||
                                                                topic.topicId
                                                            )}
                                                        </strong>

                                                        <span>
                                                            ${escapeHtml(
                                                                topic.topicId
                                                            )}
                                                        </span>

                                                    </div>


                                                    <span
                                                        class="mastery-syllabus-topic__priority mastery-syllabus-topic__priority--${escapeHtml(
                                                            topic.priority ||
                                                            "medium"
                                                        )}"
                                                    >
                                                        ${
                                                            topic.priority ||
                                                            "medium"
                                                        }
                                                    </span>

                                                </div>

                                            `
                                        )
                                        .join("")
                                    }

                                </div>

                            </article>

                        `
                    )
                    .join("")
                }

            </section>


            <section class="mastery-syllabus-start">

                <div>

                    <span>
                        READY TO BEGIN?
                    </span>

                    <strong>
                        Build your personalised learning path.
                    </strong>

                    <p>
                        You can begin with a diagnostic or start
                        from the syllabus foundation.
                    </p>

                </div>


                <button
                    type="button"
                    class="mastery-button mastery-button--primary"
                    data-syllabus-start
                >
                    Continue
                    <span>→</span>
                </button>

            </section>

        </div>
    `;


    screen
        .querySelector(
            "[data-syllabus-back]"
        )
        ?.addEventListener(
            "click",
            () => onBack?.()
        );


    screen
        .querySelector(
            "[data-syllabus-start]"
        )
        ?.addEventListener(
            "click",
            () => onStart?.()
        );
}


/* ============================================================
   TARGET SELECTION SCREEN
   ============================================================ */

export function renderTargetSelection({
    targets = [],
    onSelect = null,
    onBack = null
} = {}) {

    const screen = getScreen();
    if (!screen) return;

    updateHeaderContext({ visible: false });

    const defaultTargets = [
        {
            id: "quadratic.factorisation",
            name: "Quadratic Factorisation",
            category: "Core Algebra",
            prerequisites: 15,
            description: "Splitting middle terms, standard form ax² + bx + c, and algebraic identities."
        },
        {
            id: "linear-equations-two-variables.graph",
            name: "Linear Equations (Graphs)",
            category: "Coordinate Algebra",
            prerequisites: 3,
            description: "Graphical plotting, simultaneous lines, and intersection coordinate solutions."
        },
        {
            id: "percentage.basic",
            name: "Percentages & Fractions",
            category: "Applied Arithmetic",
            prerequisites: 2,
            description: "Percentage equivalents, base conversions, and fractional transformations."
        },
        {
            id: "profit-loss.profit",
            name: "Profit & Loss Calculations",
            category: "Commercial Maths",
            prerequisites: 3,
            description: "Cost price, selling price, percentage markup, and discount computation."
        },
        {
            id: "ratio-proportion.proportion",
            name: "Ratio & Proportion",
            category: "Foundations",
            prerequisites: 2,
            description: "Comparing quantities, unitary method, and direct/inverse variations."
        }
    ];

    const displayTargets = targets && targets.length > 0 ? targets : defaultTargets;

    screen.innerHTML = `
        <div class="mastery-page">
            <div class="mastery-flow-top">
                <button type="button" class="mastery-back-button" data-back>
                    ← Back
                </button>
                <span class="mastery-flow-step">
                    TARGET SELECTION
                </span>
            </div>

            <section class="mastery-onboarding-header">
                <span class="mastery-onboarding-kicker">ADAPTIVE CURRICULUM</span>
                <h1>Select your target skill</h1>
                <p>Choose any mathematical topic. The adaptive engine will test your prerequisite readiness graph.</p>
            </section>

            <section class="mastery-target-grid">
                ${displayTargets.map(target => `
                    <button
                        type="button"
                        class="mastery-target-card"
                        data-target-id="${escapeHtml(target.id || target.targetSkillId)}"
                    >
                        <div class="mastery-target-card__top">
                            <span class="mastery-target-badge mastery-target-badge--core">${escapeHtml(target.category || "Curriculum")}</span>
                            <span class="mastery-target-badge">${escapeHtml(String(target.prerequisites || "Prerequisite Check"))}</span>
                        </div>
                        <div>
                            <h3>${escapeHtml(target.name || target.id || target.targetSkillId)}</h3>
                            <p>${escapeHtml(target.description || "Adaptive target skill with automated prerequisite checking.")}</p>
                        </div>
                        <div class="mastery-target-card__footer">
                            <span>Evaluate Live Readiness</span>
                            <span>→</span>
                        </div>
                    </button>
                `).join("")}
            </section>
        </div>
    `;

    screen.querySelector("[data-back]")?.addEventListener("click", () => onBack?.());

    screen.querySelectorAll("[data-target-id]").forEach(btn => {
        btn.addEventListener("click", () => {
            onSelect?.(btn.dataset.targetId);
        });
    });
}


/* ============================================================
   READINESS EVALUATION SCREEN (NOT_READY / READY)
   ============================================================ */

export function renderReadinessEvaluation({
    targetSkillId,
    targetName = null,
    readinessState,
    onStartDiagnostic = null,
    onBack = null
} = {}) {

    const screen = getScreen();
    if (!screen) return;

    const displayName = targetName || targetSkillId.replace(/\./g, " — ").replace(/-/g, " ").toUpperCase();
    const isReady = readinessState?.readiness?.ready === true;
    const missing = readinessState?.readiness?.missing || [];
    const remediation = readinessState?.readiness?.remediationPath || [];

    updateHeaderContext({
        targetName: displayName,
        statusText: isReady ? "Ready" : `Needs ${missing.length} Prerequisites`,
        visible: true
    });

    screen.innerHTML = `
        <div class="mastery-page">
            <div class="mastery-flow-top">
                <button type="button" class="mastery-back-button" data-back>
                    ← Back to Targets
                </button>
                <span class="mastery-flow-step">
                    READINESS EVALUATION
                </span>
            </div>

            <section class="mastery-onboarding-header">
                <span class="mastery-onboarding-kicker">PREREQUISITE GRAPH ASSESSMENT</span>
                <h1>${escapeHtml(displayName)}</h1>
                <p>Live analysis of prerequisite mastery required before tackling this target skill.</p>
            </section>

            <section class="mastery-eval-card">
                <div class="mastery-eval-header">
                    <div>
                        <strong style="font-size: 1.15rem; color: var(--mastery-black); display: block;">
                            Readiness Diagnosis
                        </strong>
                        <span style="font-size: 0.8rem; color: var(--mastery-muted);">
                            Evaluated via mathematical dependency graph
                        </span>
                    </div>

                    <span class="mastery-eval-status-pill ${isReady ? "mastery-eval-status-pill--ready" : "mastery-eval-status-pill--not-ready"}">
                        ${isReady ? "✓ Ready to Learn" : "⚠️ Needs Prerequisite Remediation"}
                    </span>
                </div>

                ${!isReady ? `
                    <div style="margin-bottom: 20px;">
                        <strong style="font-size: 0.9rem; color: var(--mastery-red);">
                            ${missing.length} Prerequisite Gaps Detected:
                        </strong>
                        <div class="mastery-prereq-list">
                            ${(remediation.length ? remediation : missing).slice(0, 5).map((item, idx) => {
                                const name = typeof item === "string" ? item : (item.name || item.skillId || `Skill #${idx + 1}`);
                                return `
                                    <div class="mastery-prereq-item">
                                        <div>
                                            <strong>${idx + 1}. ${escapeHtml(name)}</strong>
                                        </div>
                                        <span class="mastery-prereq-item__tag">Prerequisite</span>
                                    </div>
                                `;
                            }).join("")}
                            ${(remediation.length || missing.length) > 5 ? `
                                <div style="font-size: 0.76rem; color: var(--mastery-muted); padding: 4px 16px;">
                                    + ${(remediation.length || missing.length) - 5} more foundational skills mapped
                                </div>
                            ` : ""}
                        </div>
                    </div>

                    <div style="background: #fffaf8; border: 1px dashed #f5c2ba; border-radius: 12px; padding: 16px; margin-bottom: 24px;">
                        <strong style="font-size: 0.86rem; color: var(--mastery-black); display: block; margin-bottom: 4px;">
                            Recommended Action: Diagnostic & Micro-Intervention
                        </strong>
                        <p style="font-size: 0.8rem; color: var(--mastery-muted); margin: 0;">
                            Take the 5-question adaptive diagnostic to identify exact misconceptions and unlock this target.
                        </p>
                    </div>

                    <button
                        type="button"
                        class="mastery-button mastery-button--primary"
                        data-start-diagnostic
                    >
                        Start Targeted Diagnostic (5 Questions)
                        <span>→</span>
                    </button>
                ` : `
                    <div style="background: #f2faf4; border: 1px solid #bce6c6; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
                        <strong style="font-size: 0.95rem; color: #2b8245; display: block; margin-bottom: 6px;">
                            All prerequisites mastered!
                        </strong>
                        <p style="font-size: 0.82rem; color: #3b5a43; margin: 0;">
                            Your knowledge graph shows complete readiness for ${escapeHtml(displayName)}.
                        </p>
                    </div>

                    <button
                        type="button"
                        class="mastery-button mastery-button--primary"
                        data-start-diagnostic
                    >
                        Begin Target Practice
                        <span>→</span>
                    </button>
                `}
            </section>
        </div>
    `;

    screen.querySelector("[data-back]")?.addEventListener("click", () => onBack?.());
    screen.querySelector("[data-start-diagnostic]")?.addEventListener("click", () => onStartDiagnostic?.());
}


/* ============================================================
   ADAPTIVE QUESTION RUNNER
   ============================================================ */

export function renderAdaptiveQuestion({
    questionIndex = 0,
    totalQuestions = 5,
    targetSkillId = "",
    question,
    selectedOptionId = null,
    isSubmitted = false,
    isCorrect = false,
    onSelectOption = null,
    onSubmit = null,
    onNext = null,
    onBack = null
} = {}) {

    const screen = getScreen();
    if (!screen) return;

    const qText = question?.question?.text || question?.text || "Question content loading…";
    const options = question?.options || [];
    const solutionSteps = question?.solution?.steps || [];
    const correctOptionId = question?.answer?.value || question?.correctOptionId;

    updateHeaderContext({
        targetName: targetSkillId.replace(/\./g, " ").toUpperCase(),
        statusText: `Q ${questionIndex + 1} of ${totalQuestions}`,
        visible: true
    });

    screen.innerHTML = `
        <div class="mastery-page">
            <div class="mastery-flow-top">
                <button type="button" class="mastery-back-button" data-back>
                    ← Exit Diagnostic
                </button>
                <span class="mastery-flow-step">
                    ADAPTIVE DIAGNOSTIC
                </span>
            </div>

            <section class="mastery-quiz-card">
                <div class="mastery-quiz-top">
                    <span class="mastery-quiz-counter">
                        QUESTION ${questionIndex + 1} OF ${totalQuestions}
                    </span>
                    <span class="mastery-quiz-difficulty">
                        ${escapeHtml(question?.difficulty || "adaptive")}
                    </span>
                </div>

                <div class="mastery-progress-bar" style="margin-bottom: 24px;">
                    <div
                        class="mastery-progress-bar__value"
                        style="width: ${((questionIndex + (isSubmitted ? 1 : 0)) / totalQuestions) * 100}%;"
                    ></div>
                </div>

                <h2 class="mastery-quiz-question-text">
                    ${escapeHtml(qText)}
                </h2>

                <div class="mastery-quiz-options">
                    ${options.map((opt, idx) => {
                        const optId = opt.id || String.fromCharCode(97 + idx);
                        const isThisSelected = selectedOptionId === optId;
                        let stateClass = "";
                        if (isSubmitted) {
                            if (optId === correctOptionId) {
                                stateClass = "is-correct";
                            } else if (isThisSelected && !isCorrect) {
                                stateClass = "is-incorrect";
                            }
                        } else if (isThisSelected) {
                            stateClass = "is-selected";
                        }

                        return `
                            <button
                                type="button"
                                class="mastery-quiz-option ${stateClass}"
                                data-option-id="${escapeHtml(optId)}"
                                ${isSubmitted ? "disabled" : ""}
                            >
                                <span class="mastery-quiz-option__marker">${escapeHtml(optId.toUpperCase())}</span>
                                <span>${escapeHtml(opt.text || opt.label || "")}</span>
                            </button>
                        `;
                    }).join("")}
                </div>

                ${isSubmitted ? `
                    <div style="margin-bottom: 24px;">
                        <div style="display: flex; align-items: center; gap: 8px; font-weight: 900; font-size: 1rem; color: ${isCorrect ? "#2b8245" : "var(--mastery-red)"}; margin-bottom: 12px;">
                            ${isCorrect ? "✓ Correct! Well done." : "✕ Incorrect — Review the solution steps below."}
                        </div>

                        ${solutionSteps.length > 0 ? `
                            <div class="mastery-solution-box">
                                <h4>Step-by-Step Mathematical Explanation</h4>
                                ${solutionSteps.map(step => `
                                    <div class="mastery-solution-step">
                                        <strong>Step ${step.step || 1}:</strong> ${escapeHtml(step.text || "")}
                                    </div>
                                `).join("")}
                            </div>
                        ` : ""}
                    </div>

                    <button
                        type="button"
                        class="mastery-button mastery-button--primary"
                        data-next
                    >
                        ${questionIndex + 1 >= totalQuestions ? "Finish Diagnostic & View Results" : "Next Question"}
                        <span>→</span>
                    </button>
                ` : `
                    <button
                        type="button"
                        class="mastery-button mastery-button--primary"
                        data-submit
                        ${!selectedOptionId ? "disabled style='opacity: 0.5; cursor: not-allowed;'" : ""}
                    >
                        Submit Answer
                        <span>→</span>
                    </button>
                `}
            </section>
        </div>
    `;

    screen.querySelector("[data-back]")?.addEventListener("click", () => onBack?.());

    screen.querySelectorAll("[data-option-id]").forEach(btn => {
        btn.addEventListener("click", () => {
            if (!isSubmitted) {
                onSelectOption?.(btn.dataset.optionId);
            }
        });
    });

    screen.querySelector("[data-submit]")?.addEventListener("click", () => {
        if (selectedOptionId && !isSubmitted) {
            onSubmit?.();
        }
    });

    screen.querySelector("[data-next]")?.addEventListener("click", () => {
        onNext?.();
    });
}


/* ============================================================
   DIAGNOSTIC COMPLETION & SUMMARY SCREEN
   ============================================================ */

export function renderDiagnosticCompletion({
    targetSkillId,
    correctCount = 0,
    totalQuestions = 5,
    score = 0,
    onReassess = null,
    onReturnToTarget = null,
    onHome = null
} = {}) {

    const screen = getScreen();
    if (!screen) return;

    const percentage = Math.round((correctCount / Math.max(1, totalQuestions)) * 100);
    const passed = percentage >= 60;

    updateHeaderContext({
        targetName: targetSkillId.replace(/\./g, " ").toUpperCase(),
        statusText: `Score: ${percentage}%`,
        visible: true
    });

    screen.innerHTML = `
        <div class="mastery-page">
            <div class="mastery-flow-top">
                <button type="button" class="mastery-back-button" data-home>
                    ← Home
                </button>
                <span class="mastery-flow-step">
                    DIAGNOSTIC COMPLETE
                </span>
            </div>

            <section class="mastery-quiz-card" style="text-align: center;">
                <div style="display: inline-flex; align-items: center; justify-content: center; width: 80px; height: 80px; border-radius: 50%; background: ${passed ? "#e6f8ec" : "#fff1ed"}; color: ${passed ? "#28a745" : "var(--mastery-red)"}; font-size: 2.2rem; margin: 0 auto 20px;">
                    ${passed ? "🏆" : "📈"}
                </div>

                <h1 style="font-size: 1.8rem; font-weight: 900; color: var(--mastery-black); margin: 0 0 8px 0;">
                    ${passed ? "Great Work!" : "Diagnostic Complete"}
                </h1>

                <p style="color: var(--mastery-muted); font-size: 0.92rem; max-width: 480px; margin: 0 auto 28px;">
                    Your answers have been recorded in the adaptive learner profile and integrated with the prerequisite graph.
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 16px; max-width: 460px; margin: 0 auto 32px;">
                    <div style="background: #fcfcfb; border: 1px solid var(--mastery-border); border-radius: 14px; padding: 18px;">
                        <span style="font-size: 0.68rem; font-weight: 800; color: var(--mastery-muted); text-transform: uppercase;">Score</span>
                        <strong style="display: block; font-size: 1.6rem; font-weight: 950; color: var(--mastery-black); margin-top: 4px;">
                            ${percentage}%
                        </strong>
                    </div>

                    <div style="background: #fcfcfb; border: 1px solid var(--mastery-border); border-radius: 14px; padding: 18px;">
                        <span style="font-size: 0.68rem; font-weight: 800; color: var(--mastery-muted); text-transform: uppercase;">Accuracy</span>
                        <strong style="display: block; font-size: 1.6rem; font-weight: 950; color: var(--mastery-black); margin-top: 4px;">
                            ${correctCount} / ${totalQuestions}
                        </strong>
                    </div>
                </div>

                <div style="display: flex; flex-direction: column; gap: 12px; max-width: 380px; margin: 0 auto;">
                    <button
                        type="button"
                        class="mastery-button mastery-button--primary"
                        data-reassess
                    >
                        Reassess Target Readiness
                        <span>→</span>
                    </button>

                    <button
                        type="button"
                        class="mastery-button"
                        style="background: #f4f4f0; color: var(--mastery-black);"
                        data-return
                    >
                        Explore Other Targets
                    </button>
                </div>
            </section>
        </div>
    `;

    screen.querySelector("[data-home]")?.addEventListener("click", () => onHome?.());
    screen.querySelector("[data-reassess]")?.addEventListener("click", () => onReassess?.());
    screen.querySelector("[data-return]")?.addEventListener("click", () => onReturnToTarget?.());
}



