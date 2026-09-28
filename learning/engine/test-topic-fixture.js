import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { normalizeTopicData } from './learning-engine.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ftaPath = path.join(__dirname, '../topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json');

const legacySkillIds = [
  'prime_factorisation', 'divisor_selection', 'division_calculation',
  'completion_condition', 'expanded_form', 'exponential_form',
  'uniqueness', 'error_analysis', 'reverse_factorisation',
  'divisibility_reasoning', 'incomplete_factorisation'
];

export function loadEngineTopic(relativePath = ftaPath) {
  const raw = JSON.parse(fs.readFileSync(relativePath, 'utf8'));
  const topic = normalizeTopicData(raw);

  // Keep the older integration-test IDs as fixture aliases while the source
  // curriculum retains its current fta_t*_p* identifiers.
  const stagePrefixes = [
    ['guided_practice', 'g'],
    ['faded_guidance', 'f'],
    ['constructed_solution', 'c'],
    ['confidence_bridge', 'b'],
    ['independent_solution', 'i'],
    ['transfer_mastery', 'tm']
  ];
  for (const [stage, prefix] of stagePrefixes) {
    const questions = topic.units?.[stage]?.questions || [];
    questions.forEach((question, index) => {
      question.id = `${prefix}_${String(index + 1).padStart(2, '0')}`;
    });
  }

  topic.sequence.internal_only_units = ['independence_bridge', 'confidence_bridge'];
  topic.question_model ||= {};
  topic.question_model.task_types = [
    'divisibility_reasoning', 'uniqueness_reasoning', 'direct_factorisation'
  ];
  topic.units.transfer_mastery.questions.forEach((question, index) => {
    question.task_type = topic.question_model.task_types[index % topic.question_model.task_types.length];
  });
  Object.entries(topic.skills).forEach(([skillId, skill]) => {
    if (skillId.startsWith('type_')) skill.importance = 'support';
  });
  for (const skillId of legacySkillIds) {
    topic.skills[skillId] ||= {
      id: skillId,
      name: skillId,
      importance: 'core',
      mastery_evidence: {
        minimum_distinct_correct: 1,
        minimum_low_support_correct: 1,
        low_support_levels: [0, 1]
      }
    };
  }
  return topic;
}

export { ftaPath };
