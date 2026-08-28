import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ftaPath = path.resolve(__dirname, '../learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const data = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

// Fisher-Yates shuffle
function shuffleArray(array) {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

data.question_types.forEach(qType => {
  qType.pool.forEach(prob => {
    prob.steps.forEach(step => {
      if (Array.isArray(step.option_details) && step.option_details.length > 0) {
        // Shuffle option_details
        const shuffled = shuffleArray(step.option_details);
        step.option_details = shuffled;
        step.strategy_options = shuffled.map(o => o.text);
        step.correct_strategy_index = shuffled.findIndex(o => o.is_correct);
      } else if (Array.isArray(step.strategy_options)) {
        const correctOpt = step.strategy_options[step.correct_strategy_index || 0];
        const shuffled = shuffleArray(step.strategy_options);
        step.strategy_options = shuffled;
        step.correct_strategy_index = shuffled.indexOf(correctOpt);
      }
    });
  });
});

fs.writeFileSync(ftaPath, JSON.stringify(data, null, 2), 'utf8');
console.log('Successfully randomized options across all problems in fta.json!');
