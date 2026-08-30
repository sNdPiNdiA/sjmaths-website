import fs from 'fs';
import path from 'path';

const ftaPath = path.resolve('learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const data = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

data.question_types.forEach(qt => {
  qt.pool.forEach(prob => {
    prob.steps.forEach((step, sIdx) => {
      // 1. Clean calc_prompt so it does not give away divisors or answers
      if (step.expected_divisor !== undefined && step.expected_divisor !== null) {
        if (sIdx === 0) {
          step.calc_prompt = `Enter the smallest prime divisor and compute the resulting quotient:`;
        } else if (step.expected_quotient === 1) {
          step.calc_prompt = `Enter the final prime divisor and quotient 1:`;
        } else {
          step.calc_prompt = `Enter the next prime divisor and resulting quotient:`;
        }
      } else if (qt.type_id === 'type_2_composite_proofs') {
        if (sIdx === 0) {
          step.calc_prompt = `Enter the factored expression taking out the common term:`;
        } else if (sIdx === 1) {
          step.calc_prompt = `Enter the simplified product expression:`;
        } else {
          step.calc_prompt = `Enter the prime factorised form:`;
        }
      } else if (qt.type_id === 'type_3_ending_in_zero') {
        if (sIdx === 0) {
          step.calc_prompt = `State the base prime factorisation:`;
        } else {
          step.calc_prompt = `State the conclusion regarding prime factor 5:`;
        }
      } else if (qt.type_id === 'type_4_factor_trees') {
        step.calc_prompt = `Compute the missing branch value:`;
      } else {
        step.calc_prompt = `Compute and enter the step result:`;
      }

      // 2. Add dedicated hint
      if (!step.hint) {
        if (step.revisit_topic && step.revisit_topic.tip) {
          step.hint = step.revisit_topic.tip;
        } else if (step.expected_divisor) {
          if (step.expected_divisor === 2) {
            step.hint = 'Look at the last digit. Even digits (0, 2, 4, 6, 8) are always divisible by prime 2.';
          } else if (step.expected_divisor === 3) {
            step.hint = 'Add the digits of the number. If the sum is a multiple of 3, divide by prime 3.';
          } else if (step.expected_divisor === 5) {
            step.hint = 'If the number ends in 0 or 5, it is divisible by prime 5.';
          } else if (step.expected_divisor === 7) {
            step.hint = 'Check divisibility by prime 7 by dividing or testing multiples of 7.';
          } else if (step.expected_divisor === 11) {
            step.hint = 'Test divisibility by prime 11 (e.g. 121 ÷ 11).';
          } else if (step.expected_divisor === 13) {
            step.hint = 'Test divisibility by prime 13.';
          } else if (step.expected_divisor === 17) {
            step.hint = 'Test divisibility by prime 17.';
          } else {
            step.hint = `Test prime numbers in increasing order: 2, 3, 5, 7, 11, 13...`;
          }
        } else if (qt.type_id === 'type_2_composite_proofs') {
          step.hint = 'Identify the common number appearing in both terms and factor it out using distributive property.';
        } else if (qt.type_id === 'type_3_ending_in_zero') {
          step.hint = 'A number ends in 0 if and only if its prime factorisation contains BOTH 2 and 5 (since 10 = 2 × 5).';
        } else if (qt.type_id === 'type_4_factor_trees') {
          step.hint = 'In a factor tree, Parent Node = Left Branch × Right Branch.';
        } else {
          step.hint = 'Recall the fundamental theorem of arithmetic and division rules.';
        }
      }
    });
  });
});

fs.writeFileSync(ftaPath, JSON.stringify(data, null, 2), 'utf8');
console.log('Successfully updated fta.json with neutral calc_prompts and dedicated hints!');
