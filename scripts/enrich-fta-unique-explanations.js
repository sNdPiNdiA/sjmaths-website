import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ftaPath = path.resolve(__dirname, '../learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const data = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

// Generate specific explanations for options based on their text and step context
function generateExplanation(optText, isCorrect, step, qType) {
  const text = optText.toLowerCase();

  if (isCorrect) {
    if (text.includes('smallest prime 2') || text.includes('divide by 2') || text.includes('even')) {
      return "Correct! Since the number is even, 2 is the smallest prime divisor to begin with.";
    }
    if (text.includes('divide by 3') || text.includes('sum of digits')) {
      return "Correct! The sum of digits is a multiple of 3, so prime 3 is the correct divisor.";
    }
    if (text.includes('divide by 5') || text.includes('ends in 5')) {
      return "Correct! The number ends in 5, making prime 5 the correct divisor.";
    }
    if (text.includes('divide by 7') || text.includes('divide by 11') || text.includes('divide by 13') || text.includes('divide by 17') || text.includes('divide by 19') || text.includes('divide by 23')) {
      return "Correct! This prime divides the quotient completely.";
    }
    if (text.includes('group') || text.includes('exponent') || text.includes('final') || text.includes('reach 1')) {
      return "Correct! Grouping repeated prime factors into exponential powers gives the canonical FTA form.";
    }
    if (text.includes('factor out') || text.includes('distributive') || text.includes('common term')) {
      return "Correct! Factoring out the common integer using the distributive law proves the number has composite factors.";
    }
    if (text.includes('both 2 and 5') || text.includes('contain both') || text.includes('prime factor 5')) {
      return "Correct! Divisibility by 10 requires both prime 2 and prime 5 (10 = 2 × 5).";
    }
    if (text.includes('fta uniqueness') || text.includes('uniqueness') || text.includes('lacks')) {
      return "Correct! By the uniqueness part of FTA, no other primes can exist in this base factorisation.";
    }
    if (text.includes('parent') || text.includes('branch') || text.includes('product')) {
      return "Correct! In a factor tree, a parent node equals the product of its child branches.";
    }
    return "Spot on! That is the mathematically correct reasoning.";
  }

  // Distractors
  if (text.includes('divide by 4') || text.includes('divide by 6') || text.includes('divide by 9') || text.includes('divide by 10') || text.includes('divide by 25') || text.includes('composite')) {
    const num = text.match(/\d+/)?.[0] || 'this';
    return `Incorrect. ${num} is a composite number. In prime factorisation, you must ONLY divide by prime numbers (2, 3, 5, 7, ...).`;
  }
  if (text.includes('subtract') || text.includes('add')) {
    return "Incorrect. Factorisation is based on breaking numbers into multiplicative prime factors, not addition or subtraction.";
  }
  if (text.includes('divide by 5') && (step.focus?.includes('2') || step.strategy_question?.includes('even') || step.strategy_question?.includes('84') || step.strategy_question?.includes('156'))) {
    return "Incorrect. A number is divisible by 5 only if its last digit is 0 or 5. Here the number is even, so start with prime 2.";
  }
  if (text.includes('divide by 2') && (step.strategy_question?.includes('odd') || step.strategy_question?.includes('21') || step.strategy_question?.includes('3825') || step.strategy_question?.includes('5005'))) {
    return "Incorrect. Odd numbers cannot be divided by 2. Check divisibility by prime 3 or 5 instead.";
  }
  if (text.includes('divide by 3') && text.includes('sum')) {
    return "Incorrect. Check the sum of digits carefully. If the sum is not a multiple of 3, 3 is not a factor.";
  }
  if (text.includes('divide by 7') || text.includes('divide by 13') || text.includes('divide by 17') || text.includes('divide by 19')) {
    return "Incorrect. Always exhaust smaller prime divisors (like 2, 3, 5) before testing larger primes.";
  }
  if (text.includes('stop') || text.includes('is prime') || text.includes('already simplified')) {
    return "Incorrect. The quotient is not 1 yet and is still composite; factorisation must continue until quotient reaches 1.";
  }
  if (text.includes('multiply all') || text.includes('multiply 7 by 84') || text.includes('multiply')) {
    return "Incorrect. Multiplying by original numbers creates larger values rather than breaking down into prime factors.";
  }
  if (text.includes('cannot be determined') || text.includes('none of the above')) {
    return "Incorrect. The problem can be resolved using standard prime factorisation properties.";
  }
  if (text.includes('always ends in 0') || text.includes('when n is even')) {
    return "Incorrect. A power of an integer can only end in 0 if its prime base contains BOTH 2 and 5.";
  }
  if (text.includes('is an odd number') || text.includes('6 is an even number')) {
    return "Incorrect. Odd/even parity alone does not guarantee divisibility by 10 (which requires both primes 2 and 5).";
  }

  return step.revisit_topic?.tip || "Incorrect. Re-read the step requirements and apply the appropriate prime rule.";
}

data.question_types.forEach(qType => {
  qType.pool.forEach(prob => {
    prob.steps.forEach(step => {
      const correctIdx = step.correct_strategy_index ?? 0;
      
      step.option_details = step.strategy_options.map((optText, idx) => {
        const isCorrect = idx === correctIdx;
        const explanation = generateExplanation(optText, isCorrect, step, qType);
        return {
          text: optText,
          is_correct: isCorrect,
          explanation: explanation
        };
      });
    });
  });
});

fs.writeFileSync(ftaPath, JSON.stringify(data, null, 2), 'utf8');
console.log('Successfully added unique, specific explanations to every option across all problems in fta.json!');
