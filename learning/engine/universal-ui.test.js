/**
 * universal-ui.test.js
 * 
 * Verification suite for the Universal Concept Mastery Application & Topic Loader:
 * - Dynamic topic resolution (?topic=...)
 * - Topic-agnostic rendering with Synthetic Topic (e.g. Linear Equations)
 * - FTA Canonical Dataset compatibility
 * - Error handling for missing / malformed topics
 */

import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

import { getRequestedTopicId, resolveTopicDataPath, loadTopicData, TOPIC_REGISTRY } from './topic-loader.js';
import { createLearningEngine } from './learning-engine.js';
import { loadEngineTopic } from './test-topic-fixture.js';
import { ConceptMasteryApp } from '../ui/concept-mastery/app.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const ftaPath = resolve(__dirname, '../topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json');
const ftaData = JSON.parse(readFileSync(ftaPath, 'utf8'));
const engineFtaData = loadEngineTopic(ftaPath);

// Synthetic non-FTA topic (Linear Equations)
const SYNTHETIC_LINEAR_TOPIC = {
  schema_version: '3.3.0',
  content_type: 'learning_topic',
  topic: {
    id: 'algebra-linear-eq-01',
    class: 8,
    subject: 'Algebra',
    chapter: 'Linear Equations',
    title: 'Solving One-Step Linear Equations',
    short_title: 'Linear Equations',
    description: 'Learn how inverse operations isolate variables to find solutions.'
  },
  skills: [
    { id: 'inverse_op', title: 'Apply Inverse Operation', description: 'Undo addition or subtraction' },
    { id: 'compute_var', title: 'Calculate Unknown Variable', description: 'Compute isolated variable value' }
  ],
  sequence: {
    mode: 'adaptive_sequential',
    ordered_units: ['concept_learning', 'worked_examples', 'guided_practice', 'mastery_gate']
  },
  units: {
    concept_learning: {
      instruction: ['Equations balance like a scale: whatever you do to one side, do to the other.']
    },
    worked_examples: {
      examples: [
        {
          title: 'Example 1',
          problem: 'Solve x + 7 = 15',
          steps: ['Subtract 7 from both sides: x = 15 - 7', 'x = 8'],
          final_answer: 'x = 8'
        }
      ]
    },
    guided_practice: {
      questions: [
        {
          id: 'lin_g_01',
          question: 'Solve x + 5 = 12:',
          number: 12,
          stage: 'guided_practice',
          support_level: 3,
          difficulty: 'easy',
          primary_skill_id: 'inverse_op',
          steps: [
            {
              divisors: [3, 5, 7],
              correct_divisor: 5,
              quotient: 7
            }
          ]
        }
      ]
    }
  }
};

describe('Universal Topic Loader & Registry', () => {
  test('A1. Extracts topic ID from query parameter ?topic=...', () => {
    assert.equal(getRequestedTopicId('http://localhost:8082/learning/ui/concept-mastery/?topic=cbse10-real-numbers-fta'), 'cbse10-real-numbers-fta');
    assert.equal(getRequestedTopicId('http://localhost:8082/learning/ui/concept-mastery/?topic=class-10-maths-chapter-1-fta'), 'class-10-maths-chapter-1-fta');
    assert.equal(getRequestedTopicId('http://localhost:8082/learning/ui/concept-mastery/?topic=fta'), 'fta');
  });

  test('A2. Resolves registered topic ID to relative JSON path', () => {
    const path1 = resolveTopicDataPath('cbse10-real-numbers-fta');
    const path2 = resolveTopicDataPath('class-10-maths-chapter-1-fta');
    assert.match(path1, /fta\.json$/);
    assert.equal(path2, null);
  });

  test('A3. Rejects unknown unregistered topic gracefully', async () => {
    await assert.rejects(
      async () => loadTopicData('non-existent-topic', { fetchFn: async () => ({ ok: false, status: 404 }) }),
      /not registered/
    );
  });
});

describe('Synthetic Non-FTA Topic UI Compatibility', () => {
  test('B1. Initializes ConceptMasteryApp cleanly with synthetic Linear Equations topic', () => {
    // Mock container
    const mockContainer = { innerHTML: '' };
    const globalDoc = {
      getElementById: () => mockContainer,
      querySelectorAll: () => []
    };

    const app = new ConceptMasteryApp({ containerId: 'app-root' });
    app.container = mockContainer;
    app.topicData = SYNTHETIC_LINEAR_TOPIC;
    app.engine = createLearningEngine({ topicData: SYNTHETIC_LINEAR_TOPIC });

    app.render();

    // Verify dynamic header & titles
    assert.match(mockContainer.innerHTML, /Class 8 • Algebra/);
    assert.match(mockContainer.innerHTML, /The Big Idea/);
    assert.match(mockContainer.innerHTML, /Equations balance like a scale/);
    assert.doesNotMatch(mockContainer.innerHTML, /Fundamental Theorem/);
    assert.doesNotMatch(mockContainer.innerHTML, /Class 10/);
  });

  test('B2. Synthetic topic advances to worked examples and guided practice', () => {
    const mockContainer = { innerHTML: '' };
    const app = new ConceptMasteryApp({ containerId: 'app-root' });
    app.container = mockContainer;
    app.topicData = SYNTHETIC_LINEAR_TOPIC;
    app.engine = createLearningEngine({ topicData: SYNTHETIC_LINEAR_TOPIC });
    app.currentStageId = 'worked_examples';

    app.render();
    assert.match(mockContainer.innerHTML, /Worked Example/);
    assert.match(mockContainer.innerHTML, /Solve x \+ 7 = 15/);

    // See -> Try: navigation is app-owned, so move the rendered app explicitly.
    app.currentStageId = 'stage_1_strategy';
    app.render();
    assert.match(mockContainer.innerHTML, /Problem 1/);
    assert.match(mockContainer.innerHTML, /Solve x \+ 5 = 12/);
  });
});

describe('Canonical FTA Topic End-to-End Compatibility', () => {
  test('C1. Canonical FTA dataset loads dynamic header and objectives', () => {
    const mockContainer = { innerHTML: '' };
    const app = new ConceptMasteryApp({ containerId: 'app-root' });
    app.container = mockContainer;
    app.topicData = ftaData;
    app.engine = createLearningEngine({ topicData: ftaData });

    app.render();
    assert.match(mockContainer.innerHTML, /Class 10 • Mathematics/);
    assert.match(mockContainer.innerHTML, /Theorem 1\.1/);
    assert.match(mockContainer.innerHTML, /Fundamental Theorem of Arithmetic/);
  });

  test.skip('C2. Legacy FTA worked-example assertions (superseded by the current typology contract)', () => {
    const mockContainer = { innerHTML: '' };
    const app = new ConceptMasteryApp({ containerId: 'app-root' });
    app.container = mockContainer;
    app.topicData = ftaData;
    app.engine = createLearningEngine({ topicData: ftaData });
    app.currentStageId = 'worked_examples';

    app.render();

    // Verify no [object Object]
    assert.doesNotMatch(mockContainer.innerHTML, /\[object Object\]/);
    
    // Verify single example view with badge
    assert.match(mockContainer.innerHTML, /Worked Example 1 of 4/);
    assert.match(mockContainer.innerHTML, /84[\s\S]*?→[\s\S]*?42[\s\S]*?→[\s\S]*?21[\s\S]*?→[\s\S]*?7[\s\S]*?→[\s\S]*?1/);

    // Verify strict ordering in Step 1: Choose prime -> Why? -> 84 ÷ 2 = 42
    const html = mockContainer.innerHTML;
    const chooseIdx = html.indexOf('Choose prime:');
    const whyIdx = html.indexOf('Why?');
    const calcIdx = html.indexOf('84 ÷ 2 = 42');

    assert.ok(chooseIdx !== -1, 'Choose prime label exists');
    assert.ok(whyIdx !== -1, 'Why label exists');
    assert.ok(calcIdx !== -1, 'Calculation exists');
    assert.ok(chooseIdx < whyIdx, 'Choose prime appears BEFORE Why?');
    assert.ok(whyIdx < calcIdx, 'Why? appears BEFORE Calculation');

    // Verify Next Example button present
    assert.match(mockContainer.innerHTML, /Next Example \(2 of 3\) →/);
  });
});

describe('Current FTA Worked Example Contract', () => {
  test('C2-current. Renders the current first example with ordered reasoning and navigation', () => {
    const mockContainer = { innerHTML: '' };
    const app = new ConceptMasteryApp({ containerId: 'app-root' });
    app.container = mockContainer;
    app.topicData = ftaData;
    app.engine = createLearningEngine({ topicData: ftaData });
    app.currentStageId = 'worked_examples';
    app.render();

    const html = mockContainer.innerHTML;
    assert.match(html, /Worked Example 1 of 4/);
    assert.match(html, /Express 120 as a product of its prime factors/);
    const whyIndex = html.indexOf('Why?');
    const calculationIndex = html.indexOf('120 \\div 2 = 60');
    assert.ok(whyIndex >= 0 && calculationIndex >= 0 && whyIndex < calculationIndex, 'Reason appears before the calculation');
    assert.match(html, /Next Example \(2 of 4\)/);
  });
});

describe('Guided Practice Option Feedback & Contextual Hints', () => {
  test('E1. Invalid choice (5 for 84) returns option-specific diagnosis and contextual hint', () => {
    const engine = createLearningEngine({ topicData: engineFtaData });
    const result = engine.submitInteraction({
      question_id: 'g_01',
      step_id: 0,
      divisor: 5,
      input_type: 'divisor'
    });

    assert.strictEqual(result.is_correct, false);
    assert.strictEqual(result.mathematical_validity, 'invalid');
    assert.match(result.feedback, /divisible/i);
    assert.match(result.hint, /prime 2/i);
  });

  test('E2. Correct divisor (2 for 84) is classified with pedagogical guidance', () => {
    const engine = createLearningEngine({ topicData: engineFtaData });
    const result = engine.submitInteraction({
      question_id: 'g_01',
      step_id: 0,
      divisor: 2,
      input_type: 'divisor'
    });

    assert.strictEqual(result.mathematical_validity, 'valid_preferred');
    assert.match(result.feedback, /correct|divisible/i);
  });

  test('E3. Need a Hint returns step-aware progressive hint content', () => {
    const engine = createLearningEngine({ topicData: engineFtaData });
    const hint1 = engine.requestHint({ question_id: 'g_01', step_id: 0, hint_level: 1 });
    assert.ok(hint1.hint_text, 'Hint level 1 returns text');
    assert.match(hint1.hint_text, /prime 2/i);

    const hint2 = engine.requestHint({ question_id: 'g_01', step_id: 0, hint_level: 2 });
    assert.ok(hint2.hint_text, 'Hint level 2 returns text');
    assert.match(hint2.hint_text, /divisible|even/i);
  });

  test('E4. Correct choice (2 for 84) proceeds with positive feedback', () => {
    const engine = createLearningEngine({ topicData: engineFtaData });
    const result = engine.submitInteraction({
      question_id: 'g_01',
      step_id: 0,
      divisor: 2,
      input_type: 'divisor'
    });

    assert.strictEqual(result.is_correct, true);
    assert.match(result.feedback, /correct|divisible/i);
  });
});

describe('Stage & Learning State Persistence', () => {
  test('F1. Engine re-initializes from exported raw state at exact stage without resetting', () => {
    const engine1 = createLearningEngine({ topicData: engineFtaData });
    // Advance to worked examples
    engine1.submitInteraction({ question_id: 'c_01', is_correct: true, stage: 'concept_learning' });
    // Advance to guided practice
    engine1.submitInteraction({ question_id: 'w_01', is_correct: true, stage: 'worked_examples' });

    const rawState = engine1.exportRawState();
    assert.strictEqual(rawState.current_stage, 'guided_practice');

    // Simulate page reload by creating engine2 with the persisted state
    const engine2 = createLearningEngine({
      topicData: engineFtaData,
      studentState: rawState
    });

    const state2 = engine2.getLearningState();
    assert.strictEqual(state2.current_stage, 'guided_practice');
    assert.strictEqual(state2.student_stage, 'try');
  });
});
