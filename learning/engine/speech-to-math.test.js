// Speech-to-Math Parser Unit Tests
import { SpeechToMathParser } from '../ui/concept-mastery/speech-to-math.js';

let passed = 0;
let failed = 0;

function assert(condition, message) {
  if (condition) {
    console.log(`  [PASS] ${message}`);
    passed++;
  } else {
    console.error(`  [FAIL] ${message}`);
    failed++;
  }
}

console.log('\n====================================================');
console.log('SPEECH TO MATH PARSER TEST SUITE');
console.log('====================================================\n');

const parser = new SpeechToMathParser();

// 1. Spoken Word Numbers to Numerals
console.log('Test 1: Spoken numbers to numerals');
assert(parser.wordsToNumbers('five') === '5', 'Single digit "five" -> 5');
assert(parser.wordsToNumbers('fifteen') === '15', '"fifteen" -> 15');
assert(parser.wordsToNumbers('twenty five') === '25', '"twenty five" -> 25');
assert(parser.wordsToNumbers('seventy five') === '75', '"seventy five" -> 75');
assert(parser.wordsToNumbers('two hundred twenty five') === '225', '"two hundred twenty five" -> 225');
assert(parser.wordsToNumbers('three thousand three hundred seventy five') === '3375', '"three thousand three hundred seventy five" -> 3375');

// 2. Exponents and Powers
console.log('\nTest 2: Exponents and Powers');
assert(parser.parse('three squared') === '3²', '"three squared" -> 3²');
assert(parser.parse('two cubed') === '2³', '"two cubed" -> 2³');
assert(parser.parse('five to the power of four') === '5⁴', '"five to the power of four" -> 5⁴');
assert(parser.parse('three power two') === '3²', '"three power two" -> 3²');
assert(parser.parse('x squared') === 'x²', '"x squared" -> x²');
assert(parser.parse('p squared') === 'p²', '"p squared" -> p²');

// 3. Multiplication and Product Expressions
console.log('\nTest 3: Multiplication and Arithmetic Expressions');
assert(parser.parse('three squared times five') === '3² × 5', '"three squared times five" -> 3² × 5');
assert(parser.parse('two cubed into three squared') === '2³ × 3²', '"two cubed into three squared" -> 2³ × 3²');
assert(parser.parse('two times three into five') === '2 × 3 × 5', '"two times three into five" -> 2 × 3 × 5');
assert(parser.parse('twenty five divided by five') === '25 ÷ 5', '"twenty five divided by five" -> 25 ÷ 5');
assert(parser.parse('root five') === '√5', '"root five" -> √5');
assert(parser.parse('square root of seven') === '√7', '"square root of seven" -> √7');

// 4. Equations and Complex Statements
console.log('\nTest 4: Equations and Statements');
assert(parser.parse('p squared equals five q squared') === 'p² = 5q²', '"p squared equals five q squared" -> p² = 5q²');
assert(parser.parse('root five is irrational') === '√5 is irrational', '"root five is irrational" -> √5 is irrational');

// 5. Multi-field Intent Extraction (Ladder & HCF/LCM)
console.log('\nTest 5: Multi-Field Intent Extraction');
const ladderIntent1 = parser.extractFieldIntent('divisor 3 quotient 75');
assert(ladderIntent1 && ladderIntent1.divisor === '3' && ladderIntent1.quotient === '75', 'Extracts divisor 3 and quotient 75');

const ladderIntent2 = parser.extractFieldIntent('prime divisor is 5 and quotient is 15');
assert(ladderIntent2 && ladderIntent2.divisor === '5' && ladderIntent2.quotient === '15', 'Extracts verbose divisor 5 and quotient 15');

const hcfLcmIntent1 = parser.extractFieldIntent('HCF is 15 and LCM is 225');
assert(hcfLcmIntent1 && hcfLcmIntent1.hcf === '15' && hcfLcmIntent1.lcm === '225', 'Extracts HCF 15 and LCM 225');

const hcfLcmIntent2 = parser.extractFieldIntent('LCM 225 HCF 15');
assert(hcfLcmIntent2 && hcfLcmIntent2.hcf === '15' && hcfLcmIntent2.lcm === '225', 'Extracts reversed LCM 225 and HCF 15');

// 6. Multiple Choice Option Extraction
console.log('\nTest 6: Option Choice Detection');
assert(parser.extractOptionIndex('option A') === 0, '"option A" -> index 0');
assert(parser.extractOptionIndex('option B') === 1, '"option B" -> index 1');
assert(parser.extractOptionIndex('option 3') === 2, '"option 3" -> index 2');
assert(parser.extractOptionIndex('first option') === 0, '"first option" -> index 0');
assert(parser.extractOptionIndex('second choice') === 1, '"second choice" -> index 1');

// 7. Advanced Powers and Fractional Words
console.log('\nTest 7: Advanced Powers and Complex Multiplications');
assert(parser.parse('two raised to five') === '2⁵', '"two raised to five" -> 2⁵');
assert(parser.parse('ten power three') === '10³', '"ten power three" -> 10³');
assert(parser.parse('two times three squared times five cubed') === '2 × 3² × 5³', '"two times three squared times five cubed" -> 2 × 3² × 5³');
assert(parser.parse('two hundred twenty five divided by fifteen') === '225 ÷ 15', '"two hundred twenty five divided by fifteen" -> 225 ÷ 15');

console.log('\n====================================================');
console.log(`TOTAL TESTS: ${passed + failed}`);
console.log(`PASSED:      ${passed}`);
console.log(`FAILED:      ${failed}`);
console.log('====================================================\n');

if (failed > 0) {
  process.exit(1);
}
