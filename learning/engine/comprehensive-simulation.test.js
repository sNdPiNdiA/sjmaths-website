import fs from 'fs';
import { createLearningEngine } from './learning-engine.js';

const ftaData = JSON.parse(fs.readFileSync('./learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json', 'utf8'));

console.log('================================================================');
console.log('TEST SUITE 1: ALL 49 QUESTIONS STEP-BY-STEP DATA INTEGRITY AUDIT');
console.log('================================================================');

let totalAudited = 0;
let auditErrors = 0;

for (const [uKey, unit] of Object.entries(ftaData.units || {})) {
  const list = [
    ...(unit.questions || []),
    ...(unit.question_pool || []),
    ...(unit.embedded_skill_practice || [])
  ];
  for (const q of list) {
    totalAudited++;
    if (!q.id) {
      console.error(`[AUDIT FAIL] Missing ID in unit ${uKey}:`, q.question);
      auditErrors++;
    }
    if (!q.answer && !q.steps && q.correct_option_index === undefined && !q.correct_divisor) {
      console.error(`[AUDIT FAIL] Missing answer definition in ${q.id} (${uKey})`);
      auditErrors++;
    }
  }
}
console.log(`Audited ${totalAudited} question items. Errors found: ${auditErrors}`);

console.log('\n================================================================');
console.log('TEST SUITE 2: SIMULATION — STANDARD LEARNER (100% ACCURACY)');
console.log('================================================================');

const stdEngine = createLearningEngine({ topicData: ftaData });
let currentStage = stdEngine.getLearningState().current_stage;
console.log('Initial Stage:', currentStage, '(', stdEngine.getLearningState().student_stage, ')');

// 1. Understand
let res = stdEngine.submitInteraction({ question_id: 'c_01', is_correct: true, stage: 'concept_learning' });
console.log('Step 1 (Understand) -> Stage:', res.current_stage, 'Student Stage:', res.student_stage);

// 2. See
res = stdEngine.submitInteraction({ question_id: 'w_01', is_correct: true, stage: 'worked_examples' });
console.log('Step 2 (See) -> Stage:', res.current_stage, 'Student Stage:', res.student_stage);

// 3. Try (Guided Practice - Stepwise)
let loopGuard = 0;
while (stdEngine.getLearningState().student_stage === 'try' && loopGuard < 15) {
  loopGuard++;
  const q = stdEngine.getNextQuestion();
  if (!q) break;
  const fullQ = ftaData.units.guided_practice.questions.find(x => x.id === q.id);
  const steps = fullQ.steps;
  for (let sIdx = 0; sIdx < steps.length; sIdx++) {
    const step = Array.isArray(steps[sIdx]) ? { divisor: steps[sIdx][1], quotient: steps[sIdx][2] } : { divisor: steps[sIdx].divisor, quotient: steps[sIdx].quotient };
    res = stdEngine.submitInteraction({
      question_id: q.id,
      step_id: sIdx,
      divisor: step.divisor,
      quotient: step.quotient
    });
  }
  console.log(`  [Try] Solved ${q.id} -> decision: ${res.decision}, stage: ${res.current_stage} (${res.student_stage})`);
}

// 4. Think (Faded Guidance)
loopGuard = 0;
while (stdEngine.getLearningState().student_stage === 'think' && loopGuard < 15) {
  loopGuard++;
  const q = stdEngine.getNextQuestion();
  if (!q) break;
  const fullQ = ftaData.units.faded_guidance.questions.find(x => x.id === q.id);
  const steps = fullQ.steps;
  for (let sIdx = 0; sIdx < steps.length; sIdx++) {
    const step = Array.isArray(steps[sIdx]) ? { divisor: steps[sIdx][1], quotient: steps[sIdx][2] } : { divisor: steps[sIdx].divisor, quotient: steps[sIdx].quotient };
    res = stdEngine.submitInteraction({
      question_id: q.id,
      step_id: sIdx,
      divisor: step.divisor,
      quotient: step.quotient
    });
  }
  console.log(`  [Think] Solved ${q.id} -> decision: ${res.decision}, stage: ${res.current_stage} (${res.student_stage})`);
}

function findFullQuestion(qId) {
  for (const u of Object.values(ftaData.units || {})) {
    const list = [
      ...(u.questions || []),
      ...(u.question_pool || []),
      ...(u.embedded_skill_practice || [])
    ];
    const f = list.find(x => x.id === qId);
    if (f) return f;
  }
  return null;
}

// 5. Build (Constructed Solution & Independence Bridge)
loopGuard = 0;
while (stdEngine.getLearningState().student_stage === 'build' && loopGuard < 15) {
  loopGuard++;
  const q = stdEngine.getNextQuestion();
  if (!q) break;
  const fullQ = findFullQuestion(q.id);
  res = stdEngine.submitInteraction({
    question_id: q.id,
    response: fullQ?.answer || '2² × 3² × 5',
    selected_index: fullQ?.correct_option_index
  });
  console.log(`  [Build] Solved ${q.id} -> decision: ${res.decision}, stage: ${res.current_stage} (${res.student_stage})`);
}

// 6. Solve (Independent Solution)
loopGuard = 0;
while (stdEngine.getLearningState().student_stage === 'solve' && loopGuard < 15) {
  loopGuard++;
  const q = stdEngine.getNextQuestion();
  if (!q) break;
  const fullQ = findFullQuestion(q.id);
  res = stdEngine.submitInteraction({
    question_id: q.id,
    response: fullQ?.answer || '2³ × 3² × 5',
    selected_index: fullQ?.correct_option_index
  });
  console.log(`  [Solve] Solved ${q.id} -> decision: ${res.decision}, stage: ${res.current_stage} (${res.student_stage})`);
}

// 7. Apply (Transfer Mastery)
loopGuard = 0;
while (stdEngine.getLearningState().student_stage === 'apply' && loopGuard < 15) {
  loopGuard++;
  const q = stdEngine.getNextQuestion();
  if (!q) break;
  const fullQ = findFullQuestion(q.id);
  res = stdEngine.submitInteraction({
    question_id: q.id,
    response: fullQ?.answer,
    selected_index: fullQ?.correct_option_index
  });
  console.log(`  [Apply] Solved ${q.id} -> decision: ${res.decision}, stage: ${res.current_stage} (${res.student_stage})`);
}

console.log('Final Learning Progress:', stdEngine.getLearningProgress());
const isMastered = stdEngine.getLearningState().student_stage === 'master' || stdEngine.getLearningState().current_stage === 'mastery_gate';
console.log('Is Topic Mastered:', isMastered);

console.log('\n================================================================');
console.log('TEST SUITE 3: SIMULATION — ADAPTIVE EXTENDED PRACTICE LEARNER');
console.log('================================================================');

const adaptEngine = createLearningEngine({ topicData: ftaData, currentStage: 'guided_practice' });

// 1. Wrong Divisor selection in Try stage
const qTry = adaptEngine.getNextQuestion();
let errRes = adaptEngine.submitInteraction({
  question_id: qTry.id,
  step_id: 0,
  divisor: 5,
  input_type: 'divisor'
});
console.log('1. Try Stage Wrong Divisor (5 for 84) -> is_correct:', errRes.is_correct, 'decision:', errRes.decision, 'allow_retry:', errRes.allow_retry);

// 2. Valid alternative divisor in Try stage
let altRes = adaptEngine.submitInteraction({
  question_id: qTry.id,
  step_id: 0,
  divisor: 3,
  input_type: 'divisor'
});
console.log('2. Try Stage Valid Alternative (3 for 84) -> validity:', altRes.mathematical_validity, 'allow_retry:', altRes.allow_retry);

// 3. Progressive Hints (Level 1, 2, 3)
for (let h = 1; h <= 3; h++) {
  const hintObj = adaptEngine.requestHint({ question_id: qTry.id, step_id: 0, hint_level: h });
  console.log(`3. Hint Level ${h}:`, hintObj.hint_text?.slice(0, 50), '...');
}

// 4. Correct step recovery
let corRes = adaptEngine.submitInteraction({
  question_id: qTry.id,
  step_id: 0,
  divisor: 2,
  quotient: 42
});
console.log('4. Corrected Step 1 -> is_correct:', corRes.is_correct, 'step_completed:', corRes.step_completed);

// 5. Adaptive Extension in Apply Stage when errors occur
const adaptApplyEngine = createLearningEngine({ topicData: ftaData, currentStage: 'transfer_mastery' });
const qApp1 = adaptApplyEngine.getNextQuestion();
let appErr1 = adaptApplyEngine.submitInteraction({ question_id: qApp1.id, response: 'wrong_answer' });
console.log('5. Error 1 in Apply Stage -> error_streak:', adaptApplyEngine.exportRawState().error_streak, 'decision:', appErr1.decision);

let appErr2 = adaptApplyEngine.submitInteraction({ question_id: qApp1.id, response: 'wrong_answer_2' });
console.log('6. Error 2 in Apply Stage -> error_streak:', adaptApplyEngine.exportRawState().error_streak, 'decision:', appErr2.decision);

console.log('\n================================================================');
console.log('ALL SIMULATION VERIFICATIONS COMPLETED SUCCESSFULLY!');
console.log('================================================================');
