/**
 * proof-of-irrationality.test.js
 * 
 * End-to-end verification and simulation suite for Proof of Irrationality curriculum.
 */

import assert from 'node:assert';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createLearningEngine } from './learning-engine.js';
import { resolveTopicDataPath } from './topic-loader.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const jsonPath = path.resolve(__dirname, '../data/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality.json');
const topicData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

console.log('================================================================');
console.log('TEST SUITE: PROOF OF IRRATIONALITY INTEGRITY & SIMULATION');
console.log('================================================================');

// 1. Topic Resolution
const resolvedPath = resolveTopicDataPath('cbse10-real-numbers-irrationality');
assert.strictEqual(resolvedPath, '../../data/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality.json', 'Topic ID must resolve correctly');
console.log('✔ Topic ID resolution verified');

// 2. Data Integrity Audit
const requiredUnits = ['concept_learning', 'worked_examples', 'guided_practice', 'faded_guidance', 'constructed_solution', 'independent_solution', 'transfer_mastery'];
for (const u of requiredUnits) {
  assert(topicData.units[u], `Unit ${u} must exist`);
}
console.log('✔ All 7 required core units present');

// 3. Engine Simulation across all 8 stages
const engine = createLearningEngine({ topicData });

// Stage 1: Understand
assert.strictEqual(engine.getLearningState().current_stage, 'concept_learning');
engine.setStage('worked_examples');
console.log('✔ Advanced from Understand to See');

// Stage 2: See
engine.setStage('guided_practice');
console.log('✔ Advanced from See to Try');

// Stage 3: Try (Solve g_01 step-by-step)
const q_g01 = engine.getNextQuestion();
assert.strictEqual(q_g01.id, 'g_01', 'First guided question should be g_01');
const g1_step0 = engine.submitInteraction({
  question_id: 'g_01',
  step_id: 0,
  selected_index: 0,
  response: 'Assume √2 = p/q (where p, q are integers and q ≠ 0)'
});
assert.strictEqual(g1_step0.is_correct, true, 'g_01 step 0 must be correct');

const g1_step1 = engine.submitInteraction({
  question_id: 'g_01',
  step_id: 1,
  selected_index: 0,
  response: 'gcd(p, q) = 1 (p and q have no common factor other than 1)'
});
assert.strictEqual(g1_step1.is_correct, true, 'g_01 step 1 must be correct');

const g1_step2 = engine.submitInteraction({
  question_id: 'g_01',
  step_id: 2,
  selected_index: 0,
  response: 'p² = 2q²'
});
assert.strictEqual(g1_step2.is_correct, true, 'g_01 step 2 must be correct');
console.log('✔ Guided Practice (Try) step-by-step interaction verified');

// Stage 4: Think (Solve f_01)
engine.setStage('faded_guidance');
const q_f01 = engine.getNextQuestion();
assert.strictEqual(q_f01.id, 'f_01', 'First think question should be f_01');
const f1_eval = engine.submitInteraction({
  question_id: 'f_01',
  selected_index: 0,
  response: 'Since 2 is prime and divides p², by Theorem 1.2, 2 must divide p'
});
assert.strictEqual(f1_eval.is_correct, true, 'f_01 must evaluate as correct');
console.log('✔ Faded Guidance (Think) reasoning interaction verified');

// Stage 5: Build (Solve b_01 step 0)
engine.setStage('constructed_solution');
const q_b01 = engine.getNextQuestion();
assert.strictEqual(q_b01.id, 'b_01', 'First build question should be b_01');
const b1_eval = engine.submitInteraction({
  question_id: 'b_01',
  step_id: 0,
  selected_index: 0,
  response: 'Assume √3 = p/q where p, q are coprime integers and q ≠ 0'
});
assert.strictEqual(b1_eval.is_correct, true, 'b_01 step 0 must evaluate as correct');
console.log('✔ Constructed Solution (Build) step interaction verified');

// Stage 6: Solve (Solve i_01)
engine.setStage('independent_solution');
const q_i01 = engine.getNextQuestion();
assert.strictEqual(q_i01.id, 'i_01', 'First solve question should be i_01');
const i1_eval = engine.submitInteraction({
  question_id: 'i_01',
  selected_index: 0,
  response: 'Assume √7 = a/b (coprime) ⇒ a² = 7b² ⇒ 7|a (a=7k) ⇒ b² = 7k² ⇒ 7|b ⇒ gcd(a,b) ≥ 7 (Contradiction). Hence √7 is irrational.'
});
assert.strictEqual(i1_eval.is_correct, true, 'i_01 must evaluate as correct');
console.log('✔ Independent Solution (Solve) interaction verified');

// Stage 7: Apply (Solve tm_01)
engine.setStage('transfer_mastery');
const q_tm01 = engine.getNextQuestion();
assert.strictEqual(q_tm01.id, 'tm_01', 'First apply question should be tm_01');
const tm1_eval = engine.submitInteraction({
  question_id: 'tm_01',
  selected_index: 0,
  response: 'Without assuming gcd(p,q)=1, showing that 2 divides both p and q does not contradict anything (since fractions can normally have common factors before reduction)'
});
assert.strictEqual(tm1_eval.is_correct, true, 'tm_01 must evaluate as correct');
console.log('✔ Transfer Mastery (Apply) interaction verified');

console.log('================================================================');
console.log('ALL PROOF OF IRRATIONALITY TESTS PASSED WITH 100% SUCCESS!');
console.log('================================================================');
