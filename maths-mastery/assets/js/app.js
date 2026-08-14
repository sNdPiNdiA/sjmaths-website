/* ============================================================
   SJMaths Maths Mastery
   STEP 32.17
   REAL EXAM INDEX INTEGRATION
   ============================================================ */

import {
    MathsMasteryApplication
} from "./maths-mastery-application.js";

import {
    ReadinessApplicationAdapter
} from "./knowledge/readiness-application-adapter.js";

import {
    ReadinessResolutionEngine
} from "./knowledge/readiness-resolution-engine.js";

import {
    initializeQuestionSelectionData
} from "./knowledge/question-selection-engine.js";

import {
    renderWelcome,
    renderOnboarding,
    renderExamSelection,
    renderFoundation,
    renderDiagnosticIntro,
    renderTargetSelection,
    renderReadinessEvaluation,
    renderAdaptiveQuestion,
    renderDiagnosticCompletion,
    updateHeaderContext,
    renderError,
    showStatus
} from "./ui.js";


let application = null;


/* ============================================================
   APPLICATION
   ============================================================ */

function getApplication() {

    if (!application) {

        application =
            new MathsMasteryApplication();

    }

    return application;
}


/* ============================================================
   STUDENT ID
   ============================================================ */

function getStudentId() {

    const key =
        "sjmaths-maths-mastery-student-id";

    let id =
        localStorage.getItem(
            key
        );

    if (!id) {

        id =
            "local";

        localStorage.setItem(
            key,
            id
        );
    }

    return id;
}


/* ============================================================
   BOOT
   ============================================================ */

async function boot() {

    try {

        const [
            readinessTaxonomy,
            readinessGraph,
            readinessTargets,
            selectionRules,
            questionIndex
        ] = await Promise.all([
            fetch("./data/taxonomy/readiness-taxonomy.json").then(r => r.json()),
            fetch("./data/taxonomy/readiness-graph.json").then(r => r.json()),
            fetch("./data/taxonomy/readiness-targets.json").then(r => r.json()),
            fetch("./data/config/question-selection-rules.json").then(r => r.json()),
            fetch("./data/knowledge/generated/question-index.json").then(r => r.json())
        ]);

        initializeQuestionSelectionData({
            rules: selectionRules,
            questionIndex: questionIndex
        });

        const resolutionEngine = new ReadinessResolutionEngine({
            readinessTaxonomy,
            readinessGraph,
            readinessTargets
        });

        const readinessAdapter = new ReadinessApplicationAdapter({
            resolutionEngine
        });

        application = new MathsMasteryApplication({
            readinessAdapter
        });

        const app =
            getApplication();

        const state =
            app.start(
                getStudentId()
            );

        showWelcomeScreen();

        window.SJMathsMastery = {

            application:
                app,

            state

        };


    }
    catch (error) {

        handleError(
            error
        );

    }

}


/* ============================================================
   ONBOARDING
   ============================================================ */

function beginOnboarding() {

    try {

        const app =
            getApplication();

        const state =
            app.beginOnboarding();


        renderOnboarding({

            onExam:
                () =>
                    showExamSelection(),

            onFoundation:
                () =>
                    showFoundation(
                        state
                    ),

            onDiagnostic:
                () =>
                    showDiagnostic()

        });


        syncDebugState();

    }
    catch (error) {

        handleError(
            error
        );

    }
}


/* ============================================================
   REAL EXAM INDEX
   ============================================================ */

async function loadExamIndex() {

    const url =
        "./data/knowledge/generated/exam-index.json";


    const response =
        await fetch(
            url,
            {
                cache: "no-cache"
            }
        );


    if (!response.ok) {

        throw new Error(
            `Unable to load exam index (${response.status}).`
        );

    }


    const data =
        await response.json();


    /*
     * Support both:
     *
     * {
     *     "ssc": {...},
     *     "banking": {...}
     * }
     *
     * and:
     *
     * [
     *     {...},
     *     {...}
     * ]
     *
     * without changing the underlying data file.
     */

    if (Array.isArray(data)) {

        return normalizeExamList(
            data
        );

    }


    if (
        data &&
        Array.isArray(
            data.exams
        )
    ) {

        return normalizeExamList(
            data.exams
        );

    }


    if (
        data &&
        typeof data === "object"
    ) {

        return normalizeExamList(

            Object.entries(
                data
            ).map(
                (
                    [
                        key,
                        value
                    ]
                ) => {

                    if (
                        value &&
                        typeof value === "object"
                    ) {

                        return {

                            ...value,

                            id:
                                value.id ||
                                key

                        };

                    }


                    return {

                        id:
                            key,

                        name:
                            key

                    };

                }
            )

        );

    }


    throw new Error(
        "Exam index has an unsupported structure."
    );
}


/* ============================================================
   NORMALIZE
   ============================================================ */

function normalizeExamList(
    exams
) {

    return exams

        .map(
            exam => {

                if (
                    typeof exam ===
                    "string"
                ) {

                    return {

                        id:
                            exam,

                        code:
                            exam.toUpperCase(),

                        name:
                            exam

                    };

                }


                return {

                    id:
                        exam?.id ||
                        exam?.examId ||
                        "",

                    code:
                        exam?.code ||
                        exam?.shortCode ||
                        exam?.id?.toUpperCase() ||
                        "EXAM",

                    name:
                        exam?.name ||
                        exam?.title ||
                        exam?.examName ||
                        exam?.id ||
                        "Exam",

                    description:
                        exam?.description ||
                        ""

                };

            }
        )

        .filter(
            exam =>
                Boolean(
                    exam.id
                )
        );
}


/* ============================================================
   EXAM SELECTION
   ============================================================ */

async function showExamSelection() {

    try {

        const exams =
            await loadExamIndex();


        renderExamSelection({

            exams,

            onBack:
                () =>
                    beginOnboarding(),

            onSelect:
                examId =>
                    selectExam(
                        examId
                    )

        });


        syncDebugState();

    }
    catch (error) {

        handleError(
            error
        );

    }
}


/* ============================================================
   SELECT EXAM
   ============================================================ */

function selectExam(
    examId
) {

    try {

        const app =
            getApplication();


        if (!examId) {

            throw new Error(
                "An exam must be selected."
            );

        }


        const state =
            app.selectExam(
                examId
            );


        showFoundation(
            state
        );


    }
    catch (error) {

        handleError(
            error
        );

    }
}


/* ============================================================
   FOUNDATION
   ============================================================ */

function showFoundation(
    state = null
) {

    try {

        const app =
            getApplication();


        renderFoundation({

            onBack:
                () =>
                    beginOnboarding(),

            onSelect:
                foundation => {

                    try {

                        const nextState =
                            app.chooseFoundation(
                                foundation
                            );


                        showDiagnostic(
                            nextState
                        );

                    }
                    catch (error) {

                        handleError(
                            error
                        );

                    }

                },

            onDiagnostic:
                () =>
                    showDiagnostic()

        });


        syncDebugState();

    }
    catch (error) {

        handleError(
            error
        );

    }
}


/* ============================================================
   DIAGNOSTIC
   ============================================================ */

function showDiagnostic(
    state = null
) {

    try {

        const app =
            getApplication();


        const diagnosticState =
            state ||
            app.startDiagnostic();


        renderDiagnosticIntro({

            onBack:
                () =>
                    beginOnboarding(),

            onBegin:
                () =>
                    beginDiagnostic(
                        diagnosticState
                    )

        });


        syncDebugState();

    }
    catch (error) {

        handleError(
            error
        );

    }
}


function showWelcomeScreen() {
    renderWelcome({
        onStart: () => showTargetSelection(),
        onSelectTarget: targetId => startAdaptiveTargetFlow(targetId),
        onStageClick: stage => {
            if (stage === "1") {
                startAdaptiveTargetFlow("quadratic.factorisation");
            } else if (stage === "2") {
                showTargetSelection();
            } else {
                beginOnboarding();
            }
        }
    });
    syncDebugState();
}


/* ============================================================
   TARGET SELECTION & ADAPTIVE FLOW
   ============================================================ */

async function showTargetSelection() {
    try {
        renderTargetSelection({
            onSelect: targetId => startAdaptiveTargetFlow(targetId),
            onBack: () => showWelcomeScreen()
        });
        syncDebugState();
    } catch (error) {
        handleError(error);
    }
}

async function startAdaptiveTargetFlow(targetSkillId) {
    try {
        const app = getApplication();
        showStatus("Evaluating prerequisite knowledge graph…");

        const readinessState = await app.startAdaptiveTarget(targetSkillId);

        renderReadinessEvaluation({
            targetSkillId,
            readinessState,
            onStartDiagnostic: () => runAdaptiveDiagnosticFlow(targetSkillId),
            onBack: () => showTargetSelection()
        });
        syncDebugState();
    } catch (error) {
        handleError(error);
    }
}

async function runAdaptiveDiagnosticFlow(targetSkillId) {
    try {
        const app = getApplication();
        showStatus("Preparing 5-question adaptive diagnostic…");

        const diagnostic = await app.prepareAdaptiveDiagnostic({
            questionCount: 5
        });

        const questions = diagnostic?.questions || [];
        if (questions.length === 0) {
            throw new Error("No diagnostic questions found for this prerequisite path.");
        }

        let currentQIndex = 0;
        let selectedOptionId = null;
        let isSubmitted = false;
        let isCorrect = false;
        let correctCount = 0;
        const answersRecorded = [];

        function renderCurrentQuestion() {
            const currentQ = questions[currentQIndex];
            const correctVal = currentQ?.answer?.value || currentQ?.correctOptionId;

            renderAdaptiveQuestion({
                questionIndex: currentQIndex,
                totalQuestions: questions.length,
                targetSkillId,
                question: currentQ,
                selectedOptionId,
                isSubmitted,
                isCorrect,
                onSelectOption: optId => {
                    selectedOptionId = optId;
                    renderCurrentQuestion();
                },
                onSubmit: async () => {
                    isSubmitted = true;
                    isCorrect = (selectedOptionId === correctVal);
                    if (isCorrect) correctCount++;

                    answersRecorded.push({
                        questionId: currentQ.id,
                        selectedOptionId,
                        isCorrect
                    });

                    // Submit answer into adaptive pipeline
                    await app.submitAdaptiveAnswer({
                        question: currentQ,
                        result: {
                            correct: isCorrect,
                            score: isCorrect ? 100 : 0
                        }
                    });

                    renderCurrentQuestion();
                },
                onNext: async () => {
                    if (currentQIndex + 1 < questions.length) {
                        currentQIndex++;
                        selectedOptionId = null;
                        isSubmitted = false;
                        isCorrect = false;
                        renderCurrentQuestion();
                    } else {
                        // Complete diagnostic and record learning
                        await app.completeAdaptiveDiagnostic(answersRecorded);
                        renderCompletionScreen();
                    }
                },
                onBack: () => startAdaptiveTargetFlow(targetSkillId)
            });
        }

        function renderCompletionScreen() {
            renderDiagnosticCompletion({
                targetSkillId,
                correctCount,
                totalQuestions: questions.length,
                score: Math.round((correctCount / questions.length) * 100),
                onReassess: () => startAdaptiveTargetFlow(targetSkillId),
                onReturnToTarget: () => showTargetSelection(),
                onHome: () => showWelcomeScreen()
            });
            syncDebugState();
        }

        renderCurrentQuestion();
        syncDebugState();
    } catch (error) {
        handleError(error);
    }
}


function beginDiagnostic(
    state
) {
    if (state?.flow?.targetSkillId) {
        runAdaptiveDiagnosticFlow(state.flow.targetSkillId);
    } else {
        startAdaptiveTargetFlow("quadratic.factorisation");
    }
}


/* ============================================================
   DEBUG STATE
   ============================================================ */

function syncDebugState() {

    if (!application) {
        return;
    }


    window.SJMathsMastery =
        Object.assign(

            window.SJMathsMastery || {},

            {

                application,

                state:
                    safeGetState()

            }

        );

}


function safeGetState() {

    try {

        return application.getState();

    }
    catch {

        return null;

    }

}


/* ============================================================
   ERROR
   ============================================================ */

function handleError(
    error
) {

    console.error(
        "[Maths Mastery]",
        error
    );


    renderError(

        error?.message ||
        "Something went wrong while starting Maths Mastery."

    );

}


/* ============================================================
   DOM START
   ============================================================ */

if (
    document.readyState ===
    "loading"
) {

    document.addEventListener(
        "DOMContentLoaded",
        () => {

            boot();

        },
        {
            once: true
        }
    );

}
else {

    boot();

}

/* ============================================================
   STEP 32.21 — SYLLABUS LOADING
   ============================================================ */

async function loadSyllabus(
    examId
) {

    if (!examId) {

        throw new Error(
            "Exam ID is required to load syllabus."
        );
    }


    const response =
        await fetch(
            `./data/syllabi/${encodeURIComponent(
                examId
            )}.json`,
            {
                cache: "no-cache"
            }
        );


    if (!response.ok) {

        throw new Error(
            `Syllabus could not be loaded for ${examId}.`
        );
    }


    return await response.json();
}


async function showSelectedExamSyllabus(
    examId
) {

    try {

        const syllabus =
            await loadSyllabus(
                examId
            );


        renderSyllabusOverview({

            syllabus,

            onBack:
                () =>
                    showExamSelection(),

            onStart:
                () =>
                    showDiagnostic(
                        syllabus
                    )

        });


        syncDebugState();


    }
    catch (error) {

        handleError(
            error
        );

    }
}

