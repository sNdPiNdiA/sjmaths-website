/**
 * STEP 32.40
 *
 * Readiness Remediation Flow Contract Test
 */

import assert from "assert";


import {
    ReadinessRemediationFlow,
    READINESS_FLOW_STATES
} from "./readiness-remediation-flow.js";


console.log("");
console.log("============================================================");
console.log(" STEP 32.40 — REMEDIATION FLOW CONTRACT TEST");
console.log("============================================================");
console.log("");


const flow =
    new ReadinessRemediationFlow();


console.log(
    "✓ Remediation flow created"
);


/* ============================================================
   TEST 1 — TARGET SELECTION
   ============================================================ */

console.log("");
console.log(
    "TEST 1 — Target Selection"
);


let state =
    flow.selectTarget(
        "quadratic.factorisation"
    );


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.TARGET_SELECTED
);


assert.strictEqual(
    state.targetSkillId,
    "quadratic.factorisation"
);


console.log(
    "✓ Target selected"
);


/* ============================================================
   TEST 2 — READINESS CHECK
   ============================================================ */

console.log("");
console.log(
    "TEST 2 — Readiness Check"
);


state =
    flow.beginReadinessCheck();


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.READINESS_CHECK
);


console.log(
    "✓ Readiness check state entered"
);


/* ============================================================
   TEST 3 — NOT READY
   ============================================================ */

console.log("");
console.log(
    "TEST 3 — Not Ready"
);


const notReadyState = {

    targetSkillId:
        "quadratic.factorisation",

    readiness: {

        found:
            true,

        ready:
            false,

        missing: [

            {
                skillId:
                    "algebra.negative-brackets",

                name:
                    "Negative brackets"
            }
        ],

        remediationPath: [
            {
                skillId:
                    "algebra.sign-rules",

                name:
                    "Sign rules"
            }
        ]
    },

    interventionPlan: {

        interventionRequired:
            true,

        blocks: [

            {
                id:
                    "readiness.negative-brackets",

                skillId:
                    "algebra.negative-brackets",

                title:
                    "Negative brackets",

                diagnostic: {

                    questionCount:
                        5
                }
            }
        ]
    }
};


state =
    flow.applyReadinessState(
        notReadyState
    );


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.NOT_READY
);


console.log(
    "✓ Learner correctly marked not ready"
);


/* ============================================================
   TEST 4 — INTERVENTION
   ============================================================ */

console.log("");
console.log(
    "TEST 4 — Intervention"
);


state =
    flow.applyInterventionPlan(
        notReadyState.interventionPlan
    );


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.INTERVENTION
);


assert.strictEqual(
    state.currentIntervention.skillId,
    "algebra.negative-brackets"
);


console.log(
    "✓ Intervention selected"
);


/* ============================================================
   TEST 5 — DIAGNOSTIC
   ============================================================ */

console.log("");
console.log(
    "TEST 5 — Diagnostic"
);


state =
    flow.beginDiagnostic();


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.DIAGNOSTIC
);


console.log(
    "✓ Diagnostic state entered"
);


/* ============================================================
   TEST 6 — DIAGNOSTIC RESULT
   ============================================================ */

console.log("");
console.log(
    "TEST 6 — Diagnostic Result"
);


state =
    flow.submitDiagnosticResult({

        skillId:
            "algebra.negative-brackets",

        attempted:
            5,

        correct:
            5,

        score:
            100,

        passed:
            true
    });


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.DIAGNOSTIC_RESULT
);


assert.strictEqual(
    state.diagnosticResult.score,
    100
);


console.log(
    "✓ Diagnostic result accepted"
);


/* ============================================================
   TEST 7 — REASSESS
   ============================================================ */

console.log("");
console.log(
    "TEST 7 — Reassessment"
);


state =
    flow.beginReassessment();


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.REASSESS
);


console.log(
    "✓ Reassessment state entered"
);


/* ============================================================
   TEST 8 — REMEDIATION SUCCESS
   ============================================================ */

console.log("");
console.log(
    "TEST 8 — Remediation Success"
);


const readyAfterRemediation = {

    targetSkillId:
        "quadratic.factorisation",

    readiness: {

        found:
            true,

        ready:
            true,

        missing: [],

        remediationPath: []
    }
};


state =
    flow.continueAfterReassessment(
        readyAfterRemediation
    );


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.TARGET_LEARNING
);


assert.strictEqual(
    state.currentIntervention,
    null
);


console.log(
    "✓ Learner returned to target learning"
);


/* ============================================================
   TEST 9 — STILL NOT READY
   ============================================================ */

console.log("");
console.log(
    "TEST 9 — Remediation Still Incomplete"
);


flow.selectTarget(
    "quadratic.factorisation"
);


flow.beginReadinessCheck();


flow.applyReadinessState(
    notReadyState
);


flow.applyInterventionPlan(
    notReadyState.interventionPlan
);


flow.beginDiagnostic();


flow.submitDiagnosticResult({

    skillId:
        "algebra.negative-brackets",

    attempted:
        5,

    correct:
        2,

    score:
        40,

    passed:
        false
});


flow.beginReassessment();


const stillBlocked = {

    targetSkillId:
        "quadratic.factorisation",

    readiness: {

        found:
            true,

        ready:
            false,

        missing: [

            {
                skillId:
                    "algebra.negative-brackets",

                name:
                    "Negative brackets"
            }
        ],

        remediationPath: [

            {
                skillId:
                    "algebra.negative-brackets",

                name:
                    "Negative brackets"
            }
        ]
    }
};


state =
    flow.continueAfterReassessment(
        stillBlocked,
        notReadyState.interventionPlan
    );


assert.strictEqual(
    state.state,
    READINESS_FLOW_STATES.INTERVENTION
);


assert.strictEqual(
    state.currentIntervention.skillId,
    "algebra.negative-brackets"
);


console.log(
    "✓ Still-blocked learner receives another intervention"
);


/* ============================================================
   TEST 10 — UNKNOWN TARGET SAFETY
   ============================================================ */

console.log("");
console.log(
    "TEST 10 — Missing Target Protection"
);


const freshFlow =
    new ReadinessRemediationFlow();


assert.throws(
    () => {

        freshFlow.beginReadinessCheck();

    }
);


console.log(
    "✓ Missing target safely rejected"
);


/* ============================================================
   TEST 11 — HISTORY
   ============================================================ */

console.log("");
console.log(
    "TEST 11 — State History"
);


assert.ok(
    flow.history.length >
    0
);


assert.ok(
    flow.history.some(
        item =>
            item.state ===
            READINESS_FLOW_STATES.DIAGNOSTIC
    )
);


assert.ok(
    flow.history.some(
        item =>
            item.state ===
            READINESS_FLOW_STATES.REASSESS
    )
);


console.log(
    `✓ State transitions recorded: ${flow.history.length}`
);


/* ============================================================
   TEST 12 — READ-ONLY
   ============================================================ */

console.log("");
console.log(
    "TEST 12 — Read-Only Contract"
);


const before =
    JSON.stringify(
        flow.snapshot()
    );


const snapshot =
    flow.snapshot();


snapshot.state =
    "MUTATED";


snapshot.targetSkillId =
    "MUTATED";


const after =
    JSON.stringify(
        flow.snapshot()
    );


assert.strictEqual(
    before,
    after
);


console.log(
    "✓ Returned snapshots are isolated"
);


/* ============================================================
   SUMMARY
   ============================================================ */

console.log("");
console.log("============================================================");
console.log(" STEP 32.40 PASSED");
console.log("============================================================");
console.log("");

console.log(
    "✓ Target selection"
);

console.log(
    "✓ Readiness check"
);

console.log(
    "✓ Not-ready transition"
);

console.log(
    "✓ Intervention selection"
);

console.log(
    "✓ Diagnostic state"
);

console.log(
    "✓ Diagnostic result"
);

console.log(
    "✓ Reassessment"
);

console.log(
    "✓ Successful remediation"
);

console.log(
    "✓ Repeated intervention"
);

console.log(
    "✓ Target safety"
);

console.log(
    "✓ State history"
);

console.log(
    "✓ Read-only snapshot contract"
);

console.log("");
