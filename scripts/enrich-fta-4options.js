import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ftaPath = path.resolve(__dirname, '../learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const data = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

// High-yield 4-option enrichment data per question type and step
data.question_types.forEach(qType => {
  qType.pool.forEach(prob => {
    prob.steps.forEach(step => {
      // Ensure at least 4 options
      if (step.strategy_options && step.strategy_options.length === 3) {
        const correct = step.strategy_options[step.correct_strategy_index];
        const d1 = step.strategy_options[(step.correct_strategy_index + 1) % 3];
        const d2 = step.strategy_options[(step.correct_strategy_index + 2) % 3];
        
        let d3 = "Stop factorisation because intermediate number is already simplified";
        if (step.focus && step.focus.toLowerCase().includes('first')) {
          d3 = "Divide by 4 (since it divides the number)";
        } else if (step.focus && step.focus.toLowerCase().includes('second')) {
          d3 = "Divide by 6 (composite divisor)";
        } else if (step.focus && step.focus.toLowerCase().includes('third')) {
          d3 = "Divide by 9 (composite divisor)";
        } else if (step.focus && step.focus.toLowerCase().includes('exponential') || step.focus && step.focus.toLowerCase().includes('final')) {
          d3 = "Multiply all quotient terms by the original number";
        } else if (qType.type_id === 'type_2_composite_proofs') {
          d3 = "Add 1 directly to the entire product without factoring";
        } else if (qType.type_id === 'type_3_ending_in_zero') {
          d3 = "Check if base is divisible by 9";
        } else if (qType.type_id === 'type_4_factor_trees') {
          d3 = "Subtract child branches from root";
        }

        step.strategy_options = [correct, d1, d2, d3];
        step.correct_strategy_index = 0;
      }
    });
  });
});

fs.writeFileSync(ftaPath, JSON.stringify(data, null, 2), 'utf8');
console.log('Successfully enriched all questions in fta.json with 4 options and close distractors!');
