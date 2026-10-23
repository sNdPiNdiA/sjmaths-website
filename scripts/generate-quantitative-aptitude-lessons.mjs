import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { lessonExpansions } from './quantitative-aptitude-lesson-content.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const DATA_ROOT = path.join(ROOT, 'assets', 'data', 'quantitative-aptitude');
const CATALOG_PATH = path.join(DATA_ROOT, 'catalog.json');
const GENERATOR_ID = 'scripts/generate-quantitative-aptitude-lessons.mjs';
const writeEnabled = process.argv.includes('--write');

const lessons = [
  {
    id: 'number-system-and-properties',
    theory: String.raw`<p>The number system classifies values by the operations they support. Natural numbers are counting numbers; whole numbers add zero; integers include negatives. Rational numbers can be written as (p/q), where (p,q) are integers and (q\ne0). Irrational numbers, such as (sqrt2), cannot be written as such a fraction. Real numbers include both rational and irrational numbers.</p><p>Parity describes whether an integer is even or odd. The sum of two odd numbers is even, and the product of consecutive integers is always even. Prime factorisation expresses an integer greater than 1 as a product of primes.</p><p><strong>Worked example:</strong> If (n) is odd, then (n^2) is odd, so (n^2+1) is even.</p>`,
    tricks: String.raw`<ul><li>Check whether a question needs only parity, sign or divisibility before doing full arithmetic.</li><li>For consecutive integers, use the fact that one of every two is even.</li><li>Do not call 1 a prime number: a prime has exactly two positive divisors.</li></ul>`,
    notes: String.raw`<ul><li>Even integer: divisible by 2. Odd integer: leaves remainder 1 on division by 2.</li><li>Prime: exactly two positive factors, 1 and itself. The number 1 is neither prime nor composite.</li><li>Rational numbers have terminating or recurring decimal expansions; irrational decimals do not terminate or recur.</li></ul>`,
    questions: [
      { prompt: String.raw`If (n) is an odd integer, which expression is always even?`, options: [String.raw`(n^2)`, String.raw`(n^2+1)`, String.raw`(2n+1)`, String.raw`(n+2)`], answer: 1, solution: String.raw`An odd square is odd. Adding 1 gives an even integer. The other three expressions are odd.` },
      { prompt: String.raw`Which number is irrational?`, options: [String.raw`(sqrt{49})`, String.raw`(\frac{7}{11})`, String.raw`(sqrt{3})`, String.raw`(0.125)`], answer: 2, solution: String.raw`(sqrt3) is not a ratio of integers. The other values are rational: (7), (7/11), and (1/8).` },
    ],
  },
  {
    id: 'place-value-and-order-of-numbers',
    theory: String.raw`<p>In base ten, a digit's value depends on its position. Moving one place left multiplies its place value by 10; moving one place right divides it by 10. To compare decimals, align decimal points and compare digits from left to right, adding zeroes at the end if needed.</p><p>On a number line, values increase to the right. For negative numbers, the one with the greater absolute value is smaller: (-8<-3).</p><p><strong>Worked example:</strong> (0.507=0.500+0.007), so the 7 represents seven thousandths.</p>`,
    tricks: String.raw`<ul><li>Write decimals with the same number of places before comparing: (0.6=0.60).</li><li>For negatives, compare distance from zero and reverse the order.</li><li>Use place-value columns to prevent shifting digits during addition or subtraction.</li></ul>`,
    notes: String.raw`<ul><li>In (a.bc), (b) is tenths and (c) is hundredths.</li><li>Trailing zeroes after a decimal do not change value: (2.5=2.50).</li><li>Leading zeroes before the first nonzero digit do not change the number's magnitude.</li></ul>`,
    questions: [
      { prompt: String.raw`Which is greater: (0.505) or (0.55)?`, options: [String.raw`(0.505)`, String.raw`(0.55)`, String.raw`They are equal`, String.raw`Cannot be compared`], answer: 1, solution: String.raw`Write (0.55) as (0.550). Since (550) thousandths is greater than (505) thousandths, (0.55>0.505).` },
      { prompt: String.raw`What is the place value of 7 in (6,704.3)?`, options: [String.raw`(7)`, String.raw`(70)`, String.raw`(700)`, String.raw`(7,000)`], answer: 3, solution: String.raw`The 7 is in the thousands place, so its place value is (7\times1,000=7,000).` },
    ],
  },
  {
    id: 'factors-multiples-and-prime-numbers',
    theory: String.raw`<p>A factor divides a number exactly; a multiple is obtained by multiplying by an integer. A prime number greater than 1 has exactly two positive factors. Every integer greater than 1 has a unique prime factorisation apart from the order of factors.</p><p>If (N=p^a q^b), its positive divisor count is ((a+1)(b+1)). This follows because each divisor chooses an exponent from 0 through (a) for (p), and 0 through (b) for (q).</p><p><strong>Worked example:</strong> (72=2^3\cdot3^2), so it has ((3+1)(2+1)=12) positive divisors.</p>`,
    tricks: String.raw`<ul><li>For factor counting, first write the number as a product of prime powers.</li><li>To test whether a candidate is prime, it is enough to test prime divisors up to its square root.</li><li>List factor pairs rather than every integer from 1 to (N).</li></ul>`,
    notes: String.raw`<ul><li>Every factor of (N) is at most (N); factors occur in pairs whose product is (N).</li><li>A perfect square has an odd number of positive divisors.</li><li>Prime factorisation is unique; the number 1 has an empty prime factorisation.</li></ul>`,
    questions: [
      { prompt: String.raw`How many positive divisors does (360=2^3\cdot3^2\cdot5) have?`, options: [String.raw`(12)`, String.raw`(18)`, String.raw`(24)`, String.raw`(30)`], answer: 2, solution: String.raw`Use the divisor-count formula: ((3+1)(2+1)(1+1)=4\cdot3\cdot2=24).` },
      { prompt: String.raw`Which number is prime?`, options: [String.raw`(21)`, String.raw`(27)`, String.raw`(29)`, String.raw`(35)`], answer: 2, solution: String.raw`The square root of 29 is less than 6. Test primes 2, 3 and 5: none divides 29, so 29 is prime.` },
    ],
  },
  {
    id: 'divisibility-and-remainders',
    theory: String.raw`<p>When an integer (N) is divided by a positive integer (d), it can be written (N=dq+r), where (0\le r<d). The remainder (r) is the residue of (N) modulo (d). Divisibility tests use place-value properties to find this residue quickly.</p><p>For 3 and 9, a number has the same remainder as the sum of its digits because (10\equiv1pmod9). For 5, only the last digit matters. For 11, the alternating sum of digits determines divisibility.</p><p><strong>Worked example:</strong> (12,345) has digit sum 15, which leaves remainder 6 on division by 9; therefore (12,345) also leaves remainder 6.</p>`,
    tricks: String.raw`<ul><li>Reduce large terms modulo the divisor before combining them.</li><li>For a product, multiply the residues and reduce again.</li><li>Check that a reported remainder is smaller than the divisor.</li></ul>`,
    notes: String.raw`<ul><li>Divisible by 2: last digit even; by 5: last digit 0 or 5; by 10: last digit 0.</li><li>Divisible by 3 or 9: digit sum is divisible by 3 or 9.</li><li>If (a\equiv bpmod d), then sums, differences and products preserve the congruence.</li></ul>`,
    questions: [
      { prompt: String.raw`What is the remainder when (12,345) is divided by 9?`, options: [String.raw`(3)`, String.raw`(5)`, String.raw`(6)`, String.raw`(8)`], answer: 2, solution: String.raw`The digit sum is (1+2+3+4+5=15). Since (15=9+6), the remainder is 6.` },
      { prompt: String.raw`What is the remainder when (7^{20}) is divided by 8?`, options: [String.raw`(0)`, String.raw`(1)`, String.raw`(7)`, String.raw`Cannot be determined`], answer: 1, solution: String.raw`Since (7\equiv-1pmod8), (7^{20}\equiv(-1)^{20}=1pmod8).` },
    ],
  },
  {
    id: 'simplification-and-bodmas',
    theory: String.raw`<p>Evaluate grouped expressions in a fixed order: brackets first; powers and roots next; multiplication and division from left to right; then addition and subtraction from left to right. Multiplication does not automatically come before division, and addition does not automatically come before subtraction.</p><p><strong>Worked example:</strong> (36\div3+4(5-2)=12+12=24). First evaluate the bracket, then division and multiplication, then addition.</p>`,
    tricks: String.raw`<ul><li>Rewrite the expression with clear brackets before calculating.</li><li>For multiplication and division at the same priority, move left to right; do the same for addition and subtraction.</li><li>Estimate the result first to catch a misplaced operation.</li></ul>`,
    notes: String.raw`<ul><li>Brackets can be nested; evaluate the innermost group first.</li><li>Multiplication and division have equal priority.</li><li>Subtraction is not commutative: (a-b\ne b-a) in general.</li></ul>`,
    questions: [
      { prompt: String.raw`Evaluate (18-6\div3\times2).`, options: [String.raw`(10)`, String.raw`(14)`, String.raw`(16)`, String.raw`(8)`], answer: 1, solution: String.raw`Division and multiplication proceed left to right: (6\div3=2), then (2\times2=4). Thus (18-4=14).` },
      { prompt: String.raw`Evaluate (5+2(7-3)^2\div4).`, options: [String.raw`(9)`, String.raw`(11)`, String.raw`(13)`, String.raw`(21)`], answer: 2, solution: String.raw`The bracket is 4; its square is 16. Then (2\times16\div4=8), so the total is (5+8=13).` },
    ],
  },
  {
    id: 'approximation-and-estimation',
    theory: String.raw`<p>Estimation replaces exact inputs with nearby convenient values to predict the size of an answer. Rounding to a place value gives a controlled approximation; significant figures retain a chosen number of meaningful digits. Estimation is a reasonableness check unless the question explicitly asks for an approximate value.</p><p><strong>Worked example:</strong> (49.8\times20.2) is close to (50\times20=1,000). The exact product is (1,005.96), which is consistent with the estimate.</p>`,
    tricks: String.raw`<ul><li>Round factors in opposite directions when that keeps the product estimate balanced.</li><li>For division, round both numbers to nearby compatible values.</li><li>Use bounds when rounding could change which option is correct.</li></ul>`,
    notes: String.raw`<ul><li>In rounding, inspect the first discarded digit: 0–4 round down, 5–9 round up.</li><li>An estimate should have the same order of magnitude as the exact answer.</li><li>Do not report an estimate as exact unless the question permits approximation.</li></ul>`,
    questions: [
      { prompt: String.raw`Which is the best estimate of (398\times5.1)?`, options: [String.raw`(200)`, String.raw`(2,000)`, String.raw`(20,000)`, String.raw`(400)`], answer: 1, solution: String.raw`Round (398\approx400) and (5.1\approx5). Then (400\times5=2,000).` },
      { prompt: String.raw`To the nearest ten, what is (1,246)?`, options: [String.raw`(1,240)`, String.raw`(1,245)`, String.raw`(1,250)`, String.raw`(1,200)`], answer: 2, solution: String.raw`The ones digit is 6, so round the tens digit up: (1,246\approx1,250).` },
    ],
  },
  {
    id: 'unit-digit-and-cyclicity',
    theory: String.raw`<p>The unit digit of a power depends on the last digit of its base. Powers of a fixed last digit repeat in a cycle of at most four. Reduce the exponent modulo the cycle length, remembering that a remainder of zero selects the final cycle entry.</p><p><strong>Worked example:</strong> Unit digits of powers of 7 cycle as 7, 9, 3, 1. Since (2,025\equiv1pmod4), the unit digit of (7^{2025}) is 7.</p>`,
    tricks: String.raw`<ul><li>Write the short unit-digit cycle before applying the exponent.</li><li>For a cycle of length 4, exponents congruent to 0 use the fourth entry, not the first.</li><li>Ignore all base digits except the last one.</li></ul>`,
    notes: String.raw`<ul><li>Last digit 0, 1, 5 or 6 remains unchanged under positive powers.</li><li>For last digits 2, 3, 7 and 8, the cycle length is 4.</li><li>For last digits 4 and 9, the cycle length is 2.</li></ul>`,
    questions: [
      { prompt: String.raw`What is the unit digit of (3^{58})?`, options: [String.raw`(1)`, String.raw`(3)`, String.raw`(7)`, String.raw`(9)`], answer: 3, solution: String.raw`The cycle for 3 is (3,9,7,1). Since (58\equiv2pmod4), use the second entry: 9.` },
      { prompt: String.raw`What is the unit digit of (8^{31})?`, options: [String.raw`(2)`, String.raw`(4)`, String.raw`(6)`, String.raw`(8)`], answer: 0, solution: String.raw`The cycle for 8 is (8,4,2,6). Since (31\equiv3pmod4), use the third entry: 2.` },
    ],
  },
  {
    id: 'factorials-and-trailing-zeroes',
    theory: String.raw`<p>A trailing zero is produced by a factor of 10, and each 10 contributes one factor of 2 and one of 5. In (n!), factors of 2 are more abundant, so count factors of 5: (lfloor n/5\rfloor+lfloor n/25\rfloor+lfloor n/125\rfloor+\cdots), stopping when the quotient is zero.</p><p><strong>Worked example:</strong> (100!) has (lfloor100/5\rfloor+lfloor100/25\rfloor=20+4=24) trailing zeroes.</p>`,
    tricks: String.raw`<ul><li>Count multiples of 5, then add an extra count for multiples of 25, 125, and higher powers.</li><li>For a product that is not a factorial, count paired factors 2 and 5 directly.</li><li>Do not stop at (n/5); numbers such as 25 contribute more than one factor of 5.</li></ul>`,
    notes: String.raw`<ul><li>Trailing zeroes of (n!): (sum_{k\ge1}\lfloor n/5^k\rfloor).</li><li>The number of trailing zeroes is nondecreasing as (n) increases.</li><li>For (50!), the count is (10+2=12).</li></ul>`,
    questions: [
      { prompt: String.raw`How many trailing zeroes are in (50!)?`, options: [String.raw`(10)`, String.raw`(11)`, String.raw`(12)`, String.raw`(14)`], answer: 2, solution: String.raw`Count factors of 5: (lfloor50/5\rfloor=10) and (lfloor50/25\rfloor=2). Total: 12.` },
      { prompt: String.raw`How many trailing zeroes are in (125!)?`, options: [String.raw`(25)`, String.raw`(28)`, String.raw`(31)`, String.raw`(32)`], answer: 2, solution: String.raw`(lfloor125/5\rfloor+\lfloor125/25\rfloor+\lfloor125/125\rfloor=25+5+1=31).` },
    ],
  },
  {
    id: 'number-base-systems',
    theory: String.raw`<p>A numeral in base (b) uses digits from 0 to (b-1). Its value is the sum of each digit multiplied by the corresponding power of (b). To convert an integer from base ten to base (b), repeatedly divide by (b) and read the remainders from last to first.</p><p><strong>Worked example:</strong> (101101_2=1\cdot32+0\cdot16+1\cdot8+1\cdot4+0\cdot2+1=45).</p>`,
    tricks: String.raw`<ul><li>For binary-to-decimal conversion, label place values (1,2,4,8,16,\ldots).</li><li>For decimal-to-binary conversion, keep the remainder list in reverse order until the end.</li><li>A base-(b) numeral with (k) digits has value less than (b^k).</li></ul>`,
    notes: String.raw`<ul><li>Binary uses digits 0 and 1; octal uses 0–7; hexadecimal uses 0–9 and A–F.</li><li>Place values in base (b) are (b^0,b^1,b^2,\ldots).</li><li>Write the base as a subscript to avoid confusing numeral strings.</li></ul>`,
    questions: [
      { prompt: String.raw`Convert (101101_2) to base ten.`, options: [String.raw`(41)`, String.raw`(43)`, String.raw`(45)`, String.raw`(47)`], answer: 2, solution: String.raw`Use place values: (32+8+4+1=45).` },
      { prompt: String.raw`What is (29) in binary?`, options: [String.raw`(11101_2)`, String.raw`(11011_2)`, String.raw`(10111_2)`, String.raw`(11110_2)`], answer: 0, solution: String.raw`(29=16+8+4+1), so the bits for (16,8,4,2,1) are (1,1,1,0,1): (11101_2).` },
    ],
  },
  {
    id: 'indices-and-exponents',
    theory: String.raw`<p>For a nonzero base, exponents describe repeated multiplication and its extensions. The product rule adds exponents with the same base; the quotient rule subtracts them; a power raised to a power multiplies exponents. Negative exponents represent reciprocals, and a zero exponent gives 1 for a nonzero base.</p><p><strong>Worked example:</strong> ((2^3\cdot2^5)/2^4=2^{3+5-4}=2^4=16).</p>`,
    tricks: String.raw`<ul><li>Combine powers only when the bases match.</li><li>Apply powers to every factor inside parentheses: ((ab)^n=a^n b^n).</li><li>Convert negative exponents to reciprocals before comparing sizes.</li></ul>`,
    notes: String.raw`<ul><li>(a^m a^n=a^{m+n}), (a^m/a^n=a^{m-n}) for (a\ne0).</li><li>((a^m)^n=a^{mn}), (a^{-n}=1/a^n), and (a^0=1) for (a\ne0).</li><li>In general, (a^m+b^m\ne a^{2m}); exponent laws apply to products and quotients, not sums.</li></ul>`,
    questions: [
      { prompt: String.raw`Evaluate ((3^2)^3\div3^4).`, options: [String.raw`(3)`, String.raw`(9)`, String.raw`(27)`, String.raw`(81)`], answer: 1, solution: String.raw`((3^2)^3=3^6), and (3^6/3^4=3^2=9).` },
      { prompt: String.raw`Which is equal to (5^{-2})?`, options: [String.raw`(-25)`, String.raw`(-1/25)`, String.raw`(1/25)`, String.raw`(25)`], answer: 2, solution: String.raw`A negative exponent means reciprocal: (5^{-2}=1/5^2=1/25).` },
    ],
  },
  {
    id: 'unitary-method',
    theory: String.raw`<p>The unitary method finds the value for one unit first, then scales to the requested quantity. It applies to direct proportion; for inverse proportion, the product of corresponding quantities remains constant when the conditions are fixed.</p><p><strong>Worked example:</strong> Six identical notebooks cost ₹180. One costs (180/6=₹30), so four cost (4\cdot30=₹120).</p>`,
    tricks: String.raw`<ul><li>Label units at every step: rupees per notebook, kilometres per hour, and so on.</li><li>Ask whether more of one quantity means more or less of the other before scaling.</li><li>In inverse proportion, solve using equal products rather than scaling in the same direction.</li></ul>`,
    notes: String.raw`<ul><li>Direct proportion: (y/x=k). Inverse proportion: (xy=k).</li><li>The method assumes a constant rate or unchanged conditions.</li><li>Include currency symbols and measurement units in the final result.</li></ul>`,
    questions: [
      { prompt: String.raw`Eight metres of cloth cost ₹560. What is the cost of 13 metres at the same rate?`, options: [String.raw`₹840`, String.raw`₹910`, String.raw`₹980`, String.raw`₹1,040`], answer: 1, solution: String.raw`One metre costs (560/8=₹70). Thus 13 metres cost (13\cdot70=₹910).` },
      { prompt: String.raw`Five identical machines make 400 parts in an hour. At the same rate, how many parts do eight machines make in an hour?`, options: [String.raw`(560)`, String.raw`(600)`, String.raw`(640)`, String.raw`(800)`], answer: 2, solution: String.raw`One machine makes (400/5=80) parts per hour. Eight make (8\cdot80=640).` },
    ],
  },
  {
    id: 'problems-on-ages',
    theory: String.raw`<p>Age problems are linear-equation problems. If a person's present age is (x), then after (t) years it is (x+t), and (t) years ago it was (x-t). A difference in ages remains constant over time; a ratio usually changes.</p><p><strong>Worked example:</strong> Two ages are in the ratio (5:3) and total 48. One ratio part is (48/(5+3)=6), so the ages are 30 and 18.</p>`,
    tricks: String.raw`<ul><li>Define present ages first; express past and future ages from those variables.</li><li>Translate “twice as old” into an equation, not an age difference.</li><li>Check that the solved ages satisfy both the sum and time condition.</li></ul>`,
    notes: String.raw`<ul><li>Present age (x); (t) years later (x+t); (t) years earlier (x-t).</li><li>If ages are (a,b), their difference (a-b) is unchanged after the same number of years.</li><li>Ages in a ratio (m:n) with total (S) are (mS/(m+n)) and (nS/(m+n)).</li></ul>`,
    questions: [
      { prompt: String.raw`A and B together are 40 years old. Five years ago, A was twice B's age. What are their present ages?`, options: [String.raw`A 25, B 15`, String.raw`A 30, B 10`, String.raw`A 24, B 16`, String.raw`A 20, B 20`], answer: 0, solution: String.raw`Let their present ages be (A,B). Then (A+B=40) and (A-5=2(B-5)), so (A=2B-5). Hence (3B=45), (B=15), and (A=25).` },
      { prompt: String.raw`A parent is three times a child's age. In 12 years, the parent will be twice the child's age. How old is the child now?`, options: [String.raw`(8)`, String.raw`(10)`, String.raw`(12)`, String.raw`(14)`], answer: 2, solution: String.raw`Let the child be (x); the parent is (3x). Then (3x+12=2(x+12)), giving (x=12).` },
    ],
  },
  {
    id: 'data-based-arithmetic-word-problems',
    theory: String.raw`<p>Multi-step arithmetic problems combine operations and often hide a rate, fraction, percentage or unit conversion in the wording. Identify the quantities, write the relationship, calculate in a sensible order, and attach units to the result.</p><p><strong>Worked example:</strong> Three items cost ₹80 each. A ₹30 discount applies to the total: (3\cdot80-30=₹210).</p>`,
    tricks: String.raw`<ul><li>Mark “of,” “each,” “remaining,” “per,” and “total”; these words often reveal the operation.</li><li>Keep an intermediate total before applying a later discount or charge.</li><li>Estimate before exact calculation and check the final unit.</li></ul>`,
    notes: String.raw`<ul><li>Discounted price = marked price − discount; tax is then applied according to the stated rule.</li><li>Total distance = speed × time when speed is constant.</li><li>Do not add percentages with different bases without converting to actual amounts.</li></ul>`,
    questions: [
      { prompt: String.raw`A shop buys 5 pens at ₹18 each and 3 notebooks at ₹42 each. What is the bill before tax?`, options: [String.raw`₹196`, String.raw`₹216`, String.raw`₹226`, String.raw`₹246`], answer: 1, solution: String.raw`Pens cost (5\cdot18=₹90); notebooks cost (3\cdot42=₹126). Total (=₹216).` },
      { prompt: String.raw`A vehicle travels 240 km in 4 hours, then 90 km in 1.5 hours. What is its average speed for the whole journey?`, options: [String.raw`(54\text{ km/h})`, String.raw`(60\text{ km/h})`, String.raw`(66\text{ km/h})`, String.raw`(70\text{ km/h})`], answer: 1, solution: String.raw`Total distance (=330) km and total time (=5.5) h. Average speed (=330/5.5=60\text{ km/h}).` },
    ],
  },
  {
    id: 'pipes-and-cisterns',
    theory: String.raw`<p>Pipes and cisterns use work rates. A pipe that fills a tank in (a) hours has rate (1/a) tank per hour; a drain that empties it in (b) hours has rate (-1/b). Add simultaneous rates, then invert the net rate to find the time for one tank.</p><p><strong>Worked example:</strong> A fill pipe takes 6 hours and a drain takes 12 hours. Net rate (=1/6-1/12=1/12) tank per hour, so the tank fills in 12 hours.</p>`,
    tricks: String.raw`<ul><li>Choose “one tank” as the total work unit.</li><li>Use positive rates for filling and negative rates for emptying.</li><li>Check that the net rate is positive if the question says the tank fills.</li></ul>`,
    notes: String.raw`<ul><li>Combined rate = sum of individual signed rates.</li><li>Time = work ÷ rate.</li><li>If two inlet pipes fill in (a,b) hours, together they take (ab/(a+b)) hours.</li></ul>`,
    questions: [
      { prompt: String.raw`Two inlets fill a tank in 8 hours and 12 hours. How long do they take together?`, options: [String.raw`(4\text{ h})`, String.raw`(4.8\text{ h})`, String.raw`(5\text{ h})`, String.raw`(10\text{ h})`], answer: 1, solution: String.raw`Their combined rate is (1/8+1/12=5/24) tank per hour. Time (=24/5=4.8) hours.` },
      { prompt: String.raw`A pipe fills a tank in 10 hours and a leak empties it in 15 hours. If both are open, when is the tank full?`, options: [String.raw`(20\text{ h})`, String.raw`(25\text{ h})`, String.raw`(30\text{ h})`, String.raw`(35\text{ h})`], answer: 2, solution: String.raw`Net rate (=1/10-1/15=1/30) tank per hour, so the tank fills in 30 hours.` },
    ],
  },
  {
    id: 'work-and-wages',
    theory: String.raw`<p>When workers receive wages in proportion to work completed, compare their work amounts, not just their time. If workers have equal productivity, work is proportional to time. If productivity differs, work is productivity multiplied by time.</p><p><strong>Worked example:</strong> A and B work 6 and 9 days at the same rate. Their work ratio is (6:9=2:3); from ₹1,000, A receives ₹400 and B ₹600.</p>`,
    tricks: String.raw`<ul><li>Write each person's contribution in a common unit before sharing wages.</li><li>For equal work, a faster worker needs less time; do not assume time and work have the same ratio.</li><li>Verify that individual shares add to the total payment.</li></ul>`,
    notes: String.raw`<ul><li>Work amount = rate × time.</li><li>Wage share = total wages × individual work / total work.</li><li>Include hours and days consistently when comparing rates.</li></ul>`,
    questions: [
      { prompt: String.raw`A and B work at equal rates for 6 and 9 days. They share ₹1,500 in proportion to work. What is A's share?`, options: [String.raw`₹500`, String.raw`₹600`, String.raw`₹750`, String.raw`₹900`], answer: 1, solution: String.raw`The work ratio is (6:9=2:3). A receives (2/(2+3)\cdot1,500=₹600).` },
      { prompt: String.raw`A completes 10 units of work per day for 4 days. B completes 8 units per day for 5 days. From ₹1,200, how much should A receive in proportion to work?`, options: [String.raw`₹480`, String.raw`₹600`, String.raw`₹720`, String.raw`₹800`], answer: 1, solution: String.raw`Both complete 40 units: A (10\cdot4=40), B (8\cdot5=40). They split the payment equally, so A receives ₹600.` },
    ],
  },
  {
    id: 'problems-on-trains',
    theory: String.raw`<p>Train problems use speed, time and distance, with the train's length included when it fully clears an object. Convert kilometres per hour to metres per second by multiplying by (5/18). For opposite directions, add speeds; for the same direction, subtract the slower speed from the faster one.</p><p><strong>Worked example:</strong> A 180 m train at 54 km/h travels at 15 m/s. It passes a pole in (180/15=12) seconds.</p>`,
    tricks: String.raw`<ul><li>Passing a pole or person: distance is the train length.</li><li>Passing a platform: distance is train length plus platform length.</li><li>Two trains crossing: distance is the sum of lengths; use relative speed.</li></ul>`,
    notes: String.raw`<ul><li>(1\text{ km/h}=5/18\text{ m/s}); (1\text{ m/s}=18/5\text{ km/h}).</li><li>Time = total crossing distance / relative speed.</li><li>Keep all lengths and speeds in compatible units.</li></ul>`,
    questions: [
      { prompt: String.raw`A 150 m train moves at 72 km/h. How long does it take to pass a 250 m platform?`, options: [String.raw`(15\text{ s})`, String.raw`(18\text{ s})`, String.raw`(20\text{ s})`, String.raw`(25\text{ s})`], answer: 2, solution: String.raw`Speed (=72\cdot5/18=20) m/s. Distance (=150+250=400) m. Time (=400/20=20) s.` },
      { prompt: String.raw`Two trains of lengths 120 m and 180 m move in opposite directions at 36 km/h and 54 km/h. How long do they take to cross?`, options: [String.raw`(10\text{ s})`, String.raw`(12\text{ s})`, String.raw`(15\text{ s})`, String.raw`(20\text{ s})`], answer: 1, solution: String.raw`Relative speed (=90\text{ km/h}=25\text{ m/s}). Total length (=300) m, so time (=300/25=12) s.` },
    ],
  },
  {
    id: 'boats-and-streams',
    theory: String.raw`<p>A boat's downstream speed adds the still-water speed (b) and stream speed (s); upstream speed subtracts the stream speed. Thus (D=b+s) and (U=b-s). Solving gives (b=(D+U)/2) and (s=(D-U)/2).</p><p><strong>Worked example:</strong> If downstream speed is 15 km/h and upstream speed is 9 km/h, still-water speed is 12 km/h and stream speed is 3 km/h.</p>`,
    tricks: String.raw`<ul><li>Use average of downstream and upstream speeds for still water.</li><li>Use half their difference for stream speed.</li><li>For a journey against the stream, divide distance by upstream speed, not still-water speed.</li></ul>`,
    notes: String.raw`<ul><li>Downstream: (b+s). Upstream: (b-s).</li><li>For the same distance, time upstream is longer when stream speed is positive.</li><li>Check (b>s); otherwise the assumed upstream direction cannot be achieved.</li></ul>`,
    questions: [
      { prompt: String.raw`A boat travels downstream at 18 km/h and upstream at 12 km/h. What is the stream speed?`, options: [String.raw`(2\text{ km/h})`, String.raw`(3\text{ km/h})`, String.raw`(5\text{ km/h})`, String.raw`(6\text{ km/h})`], answer: 1, solution: String.raw`Stream speed (=(18-12)/2=3\text{ km/h}).` },
      { prompt: String.raw`A boat's still-water speed is 10 km/h and stream speed is 2 km/h. How long does it take to travel 32 km upstream?`, options: [String.raw`(3\text{ h})`, String.raw`(4\text{ h})`, String.raw`(5\text{ h})`, String.raw`(6\text{ h})`], answer: 1, solution: String.raw`Upstream speed (=10-2=8\text{ km/h}). Time (=32/8=4) hours.` },
    ],
  },
  {
    id: 'races-and-circular-motion',
    theory: String.raw`<p>In a race, compare distances covered in the same time or times taken for the same distance. On a circular track, the first meeting time is track length divided by relative speed: add speeds for opposite directions and subtract for the same direction.</p><p><strong>Worked example:</strong> On a 300 m circular track, runners at 5 m/s and 4 m/s in the same direction meet after (300/(5-4)=300) seconds.</p>`,
    tricks: String.raw`<ul><li>Convert each runner's speed to the same unit.</li><li>“A beats B by 20 m in a 100 m race” means B covers 80 m when A covers 100 m.</li><li>For repeated meetings, use the relative distance for one lap.</li></ul>`,
    notes: String.raw`<ul><li>Relative speed in the same direction is (|v_1-v_2|).</li><li>Relative speed in opposite directions is (v_1+v_2).</li><li>For a circular track of circumference (C), one same-direction catch-up interval is (C/|v_1-v_2|).</li></ul>`,
    questions: [
      { prompt: String.raw`Two runners move in opposite directions on a 400 m track at 6 m/s and 4 m/s. When do they first meet?`, options: [String.raw`(20\text{ s})`, String.raw`(40\text{ s})`, String.raw`(50\text{ s})`, String.raw`(100\text{ s})`], answer: 1, solution: String.raw`Their relative speed is (6+4=10) m/s. Time (=400/10=40) s.` },
      { prompt: String.raw`In a 100 m race, A finishes in 10 s and beats B by 20 m. How long does B take to finish 100 m at the same speed?`, options: [String.raw`(10\text{ s})`, String.raw`(11.5\text{ s})`, String.raw`(12.5\text{ s})`, String.raw`(15\text{ s})`], answer: 2, solution: String.raw`When A covers 100 m, B covers 80 m in 10 s, so B's speed is 8 m/s. B's 100 m time is (100/8=12.5) s.` },
    ],
  },
  {
    id: 'algebraic-expressions',
    theory: String.raw`<p>An algebraic expression combines variables, coefficients and constants with operations. Like terms have identical variable parts and can be combined; unlike terms cannot. The distributive law (a(b+c)=ab+ac) expands brackets, while taking out a common factor reverses the process.</p><p><strong>Worked example:</strong> (3(2x-1)-2x=6x-3-2x=4x-3). At (x=4), the value is 13.</p>`,
    tricks: String.raw`<ul><li>Collect like terms before substituting values.</li><li>When a minus sign precedes brackets, change every sign inside.</li><li>Substitute only after simplifying, unless values make direct evaluation easier.</li></ul>`,
    notes: String.raw`<ul><li>Coefficient is the numerical factor multiplying a variable.</li><li>(x\cdot x=x^2); (x+x=2x), not (x^2).</li><li>Use the distributive law to check expansions by multiplying back.</li></ul>`,
    questions: [
      { prompt: String.raw`Simplify (4(2x+3)-3x).`, options: [String.raw`(5x+12)`, String.raw`(8x+9)`, String.raw`(5x+3)`, String.raw`(11x+12)`], answer: 0, solution: String.raw`Distribute 4: (8x+12-3x=5x+12).` },
      { prompt: String.raw`Evaluate (a^2-2ab+b^2) for (a=5,b=2).`, options: [String.raw`(5)`, String.raw`(9)`, String.raw`(13)`, String.raw`(25)`], answer: 1, solution: String.raw`Substitute: (25-20+4=9). Equivalently, the expression is ((a-b)^2=3^2=9).` },
    ],
  },
  {
    id: 'linear-equations',
    theory: String.raw`<p>A linear equation in one variable has the form (ax+b=c), with (a\ne0). Apply the same operation to both sides to keep equality. For simultaneous linear equations, the solution is an ordered pair satisfying both equations; use substitution or elimination.</p><p><strong>Worked example:</strong> (3x+5=26) gives (3x=21), so (x=7). Check by substituting: (21+5=26).</p>`,
    tricks: String.raw`<ul><li>Clear simple fractions by multiplying every term by the common denominator.</li><li>Collect variable terms on one side and constants on the other.</li><li>Substitute the answer back into the original equation, not a transformed line.</li></ul>`,
    notes: String.raw`<ul><li>Adding or subtracting the same quantity on both sides preserves equality.</li><li>Dividing by a coefficient is valid only when it is nonzero.</li><li>Two linear equations may have one solution, no solution, or infinitely many solutions.</li></ul>`,
    questions: [
      { prompt: String.raw`Solve (5x-7=28).`, options: [String.raw`(5)`, String.raw`(6)`, String.raw`(7)`, String.raw`(8)`], answer: 2, solution: String.raw`Add 7: (5x=35); divide by 5 to get (x=7).` },
      { prompt: String.raw`If (2x+y=11) and (x=4), what is (y)?`, options: [String.raw`(1)`, String.raw`(2)`, String.raw`(3)`, String.raw`(4)`], answer: 2, solution: String.raw`Substitute (x=4): (8+y=11), so (y=3).` },
    ],
  },
  {
    id: 'quadratic-equations',
    theory: String.raw`<p>A quadratic equation has the form (ax^2+bx+c=0), where (a\ne0). It can be solved by factorisation, completing the square, or the quadratic formula. The discriminant (D=b^2-4ac) determines the real roots: positive gives two, zero gives one repeated root, and negative gives no real roots.</p><p><strong>Worked example:</strong> (2x^2-5x+2=(2x-1)(x-2)), so its roots are (1/2) and 2.</p>`,
    tricks: String.raw`<ul><li>Arrange the equation with zero on one side before factoring.</li><li>For integer roots, test factors of (ac) whose sum is (b).</li><li>Substitute each root into the original equation to check it.</li></ul>`,
    notes: String.raw`<ul><li>Quadratic formula: (x=(-b\pm\sqrt{b^2-4ac})/(2a)).</li><li>Sum of roots (=-b/a); product of roots (=c/a).</li><li>The discriminant must be nonnegative for real roots.</li></ul>`,
    questions: [
      { prompt: String.raw`What are the roots of (x^2-5x+6=0)?`, options: [String.raw`(1,6)`, String.raw`(2,3)`, String.raw`(-2,-3)`, String.raw`(3,6)`], answer: 1, solution: String.raw`Factor: (x^2-5x+6=(x-2)(x-3)). Thus (x=2) or (x=3).` },
      { prompt: String.raw`How many real roots does (x^2+4x+5=0) have?`, options: [String.raw`None`, String.raw`One`, String.raw`Two`, String.raw`Infinitely many`], answer: 0, solution: String.raw`The discriminant is (4^2-4(1)(5)=16-20=-4<0), so there are no real roots.` },
    ],
  },
  {
    id: 'polynomials',
    theory: String.raw`<p>A polynomial is a finite sum of terms (a_kx^k), where exponents (k) are nonnegative integers. Its degree is the greatest exponent with a nonzero coefficient. Factoring rewrites a polynomial as a product; the factor theorem says (x-a) is a factor exactly when (P(a)=0).</p><p><strong>Worked example:</strong> (x^2-5x+6=(x-2)(x-3)), so the zeros are 2 and 3.</p>`,
    tricks: String.raw`<ul><li>Look for a common factor before using identities.</li><li>For (x^2+bx+c), seek two numbers with product (c) and sum (b).</li><li>Use substitution (P(a)) to test a proposed linear factor.</li></ul>`,
    notes: String.raw`<ul><li>A nonzero constant polynomial has degree 0.</li><li>If (P(a)=0), then (x-a) divides (P(x)).</li><li>For a monic quadratic (x^2+bx+c), root sum is (-b) and root product is (c).</li></ul>`,
    questions: [
      { prompt: String.raw`Factor (x^2-7x+12).`, options: [String.raw`((x-2)(x-6))`, String.raw`((x-3)(x-4))`, String.raw`((x+3)(x+4))`, String.raw`((x-1)(x-12))`], answer: 1, solution: String.raw`The numbers 3 and 4 multiply to 12 and add to 7, so (x^2-7x+12=(x-3)(x-4)).` },
      { prompt: String.raw`What is the remainder when (P(x)=x^3-1) is divided by (x-1)?`, options: [String.raw`(0)`, String.raw`(1)`, String.raw`(-1)`, String.raw`(2)`], answer: 0, solution: String.raw`By the remainder theorem, the remainder is (P(1)=1^3-1=0).` },
    ],
  },
  {
    id: 'linear-inequalities',
    theory: String.raw`<p>An inequality compares quantities using (<,\le,>,\ge). Solve it like an equation while preserving order. If both sides are multiplied or divided by a negative number, reverse the inequality sign. A quadratic inequality can be solved by finding its zeros and testing the intervals they create.</p><p><strong>Worked example:</strong> (-2x+6\ge0) gives (-2x\ge-6); dividing by (-2) reverses the sign, so (x\le3).</p>`,
    tricks: String.raw`<ul><li>Mark critical values on a number line and test one value in each interval.</li><li>Keep strict endpoints open for (<,>), and include endpoints for (\le,\ge).</li><li>Check any sign reversal after dividing by a negative coefficient.</li></ul>`,
    notes: String.raw`<ul><li>Adding the same value to both sides does not reverse the inequality.</li><li>Multiplying by a positive value preserves order; multiplying by a negative value reverses it.</li><li>The solution may be an interval, a union of intervals, all real numbers, or no values.</li></ul>`,
    questions: [
      { prompt: String.raw`Solve (3x-5<7).`, options: [String.raw`(x<4)`, String.raw`(x>4)`, String.raw`(x<2/3)`, String.raw`(x>2/3)`], answer: 0, solution: String.raw`Add 5 to obtain (3x<12). Divide by positive 3: (x<4).` },
      { prompt: String.raw`Solve (-2x+6\ge0).`, options: [String.raw`(x\ge3)`, String.raw`(x\le3)`, String.raw`(x\ge-3)`, String.raw`(x\le-3)`], answer: 1, solution: String.raw`(-2x\ge-6). Dividing by (-2) reverses the sign, giving (x\le3).` },
    ],
  },
  {
    id: 'functions-and-graphs',
    theory: String.raw`<p>A function assigns exactly one output to each input in its domain. In (y=f(x)), the domain is the set of permitted (x)-values and the range is the set of resulting outputs. A graph displays ordered pairs ((x,f(x))); its vertical-line test checks whether it represents a function.</p><p><strong>Worked example:</strong> For (f(x)=x^2-1), (f(3)=9-1=8).</p>`,
    tricks: String.raw`<ul><li>Substitute the entire input expression when evaluating (f(a+h)).</li><li>Check denominators for zero and even-root radicands for negative values when finding a real domain.</li><li>Use intercepts and a few exact points to sketch a simple graph.</li></ul>`,
    notes: String.raw`<ul><li>For (f(x)=1/(x-2)), (x=2) is excluded from the domain.</li><li>For (f(x)=\sqrt{x-2}) over the reals, require (x\ge2).</li><li>A horizontal line may intersect a function's graph more than once; that concerns one-to-one behavior, not whether it is a function.</li></ul>`,
    questions: [
      { prompt: String.raw`If (f(x)=2x^2+1), what is (f(-2))?`, options: [String.raw`(5)`, String.raw`(7)`, String.raw`(9)`, String.raw`(-7)`], answer: 2, solution: String.raw`Substitute (-2): (f(-2)=2(-2)^2+1=2\cdot4+1=9).` },
      { prompt: String.raw`What is the real domain of (g(x)=\sqrt{x-5})?`, options: [String.raw`(x<5)`, String.raw`(x\le5)`, String.raw`(x>5)`, String.raw`(x\ge5)`], answer: 3, solution: String.raw`The radicand must be nonnegative: (x-5\ge0), so (x\ge5).` },
    ],
  },
  {
    id: 'logarithms',
    theory: String.raw`<p>A logarithm answers the question “to what power?” The statement (\log_b a=c) means (b^c=a), with (b>0), (b\ne1), and (a>0). Product, quotient and power rules follow from the corresponding laws of exponents.</p><p><strong>Worked example:</strong> (\log_2 32=5), because (2^5=32).</p>`,
    tricks: String.raw`<ul><li>Convert a logarithmic equation to exponential form to check it.</li><li>Combine logarithms only when they have the same base and valid positive arguments.</li><li>Do not split (\log_b(x+y)) into a sum; no such rule exists.</li></ul>`,
    notes: String.raw`<ul><li>\(\log_b(xy)=\log_bx+\log_by\).</li><li>\(\log_b(x/y)=\log_bx-\log_by\).</li><li>\(\log_b(x^k)=k\log_bx\), for positive (x).</li><li>\(\log_b1=0\) and \(\log_b b=1\).</li></ul>`,
    questions: [
      { prompt: String.raw`Evaluate (\log_3 81).`, options: [String.raw`(3)`, String.raw`(4)`, String.raw`(9)`, String.raw`(27)`], answer: 1, solution: String.raw`Since (3^4=81), (\log_3 81=4).` },
      { prompt: String.raw`If (\log_2 x=5), what is (x)?`, options: [String.raw`(10)`, String.raw`(16)`, String.raw`(25)`, String.raw`(32)`], answer: 3, solution: String.raw`By the definition of logarithm, (2^5=x), so (x=32).` },
    ],
  },
  {
    id: 'sequences-and-series',
    theory: String.raw`<p>A sequence is an ordered list; a series is the sum of its terms. In an arithmetic progression (AP), consecutive terms differ by a constant (d). In a geometric progression (GP), consecutive terms have a constant ratio (r).</p><p><strong>Worked example:</strong> In (4,7,10,\ldots), (a=4,d=3), so the 10th term is (a_ {10}=4+9\cdot3=31).</p>`,
    tricks: String.raw`<ul><li>Subtract consecutive terms to test for an AP; divide them to test for a GP when terms are nonzero.</li><li>Use (n), not (n-1), in the AP sum.</li><li>Check whether the problem asks for the nth term or the sum of terms.</li></ul>`,
    notes: String.raw`<ul><li>AP nth term: (a_n=a+(n-1)d).</li><li>AP sum: (S_n=n[2a+(n-1)d]/2=n(a+l)/2).</li><li>GP nth term: (a_n=ar^{n-1}); for (r\ne1), (S_n=a(r^n-1)/(r-1)).</li></ul>`,
    questions: [
      { prompt: String.raw`What is the 10th term of (4,7,10,\ldots)?`, options: [String.raw`(28)`, String.raw`(30)`, String.raw`(31)`, String.raw`(34)`], answer: 2, solution: String.raw`Here (a=4,d=3). Thus (a_{10}=4+(10-1)3=31).` },
      { prompt: String.raw`What is the sum of the first five terms of (1,2,4,8,\ldots)?`, options: [String.raw`(15)`, String.raw`(31)`, String.raw`(32)`, String.raw`(63)`], answer: 1, solution: String.raw`Add the five terms: (1+2+4+8+16=31).` },
    ],
  },
  {
    id: 'algebraic-word-problems',
    theory: String.raw`<p>Translate a word statement into variables, equations and constraints. Define what each variable represents, keep units consistent, solve, then verify that the result makes sense in the original context. “Twice a number” is (2x); “two more than twice a number” is (2x+2).</p><p><strong>Worked example:</strong> A number and its double total 36. Let the number be (x); (x+2x=36), so (x=12).</p>`,
    tricks: String.raw`<ul><li>Choose a variable for the unknown quantity and state its unit.</li><li>Translate relationship words before calculating: “is,” “difference,” “per,” and “at least” have distinct meanings.</li><li>Check the solution against every condition, including whole-number or positive constraints.</li></ul>`,
    notes: String.raw`<ul><li>Consecutive integers: (n,n+1); consecutive even integers: (2n,2n+2).</li><li>Distance = rate × time; total cost = unit price × quantity.</li><li>Reject solutions that violate the real-world domain, such as a negative number of items.</li></ul>`,
    questions: [
      { prompt: String.raw`The sum of three consecutive integers is 72. What is the middle integer?`, options: [String.raw`(22)`, String.raw`(23)`, String.raw`(24)`, String.raw`(25)`], answer: 2, solution: String.raw`Let them be (n-1,n,n+1). Their sum is (3n=72), so the middle integer is (n=24).` },
      { prompt: String.raw`A taxi charges ₹50 plus ₹12 per kilometre. What is the fare for 8 km?`, options: [String.raw`₹96`, String.raw`₹136`, String.raw`₹146`, String.raw`₹156`], answer: 2, solution: String.raw`Fare (=50+12\cdot8=50+96=₹146).` },
    ],
  },
  {
    id: 'lines-and-angles',
    theory: String.raw`<p>Angles on a straight line sum to (180^\circ); angles around a point sum to (360^\circ). Vertically opposite angles are equal. When a transversal crosses parallel lines, corresponding and alternate interior angles are equal, while co-interior angles on the same side sum to (180^\circ).</p><p><strong>Worked example:</strong> If one angle in a linear pair is (68^\circ), the other is (180^\circ-68^\circ=112^\circ).</p>`,
    tricks: String.raw`<ul><li>Mark parallel lines and the transversal before applying angle rules.</li><li>Find a vertical or corresponding angle first; then use a linear pair if needed.</li><li>Keep the degree symbol with angle measures.</li></ul>`,
    notes: String.raw`<ul><li>Linear pair: supplementary, total (180^\circ).</li><li>Vertically opposite angles: equal.</li><li>Triangle interior angles total (180^\circ); an exterior angle equals the sum of the two opposite interior angles.</li></ul>`,
    questions: [
      { prompt: String.raw`An angle forms a linear pair with (68^\circ). Find the angle.`, options: [String.raw`(102^\circ)`, String.raw`(112^\circ)`, String.raw`(122^\circ)`, String.raw`(292^\circ)`], answer: 1, solution: String.raw`A linear pair sums to (180^\circ), so the angle is (180^\circ-68^\circ=112^\circ).` },
      { prompt: String.raw`Two vertically opposite angles are formed. If one is (47^\circ), what is the other?`, options: [String.raw`(43^\circ)`, String.raw`(47^\circ)`, String.raw`(133^\circ)`, String.raw`(313^\circ)`], answer: 1, solution: String.raw`Vertically opposite angles are equal, so the other angle is (47^\circ).` },
    ],
  },
  {
    id: 'symmetry',
    theory: String.raw`<p>Reflection symmetry means a line divides a shape into mirror-image halves. Rotational symmetry means a turn of less than (360^\circ) maps a shape onto itself. The order of rotational symmetry is the number of matching positions in one full turn.</p><p><strong>Worked example:</strong> A square has four reflection axes and rotational symmetry of order 4; a turn of (90^\circ) maps it onto itself.</p>`,
    tricks: String.raw`<ul><li>Fold the figure mentally along a proposed mirror line to test reflection symmetry.</li><li>For rotational order, divide (360^\circ) by the smallest positive matching turn.</li><li>Do not confuse the number of symmetry lines with rotational order.</li></ul>`,
    notes: String.raw`<ul><li>An equilateral triangle has 3 reflection axes and rotational order 3.</li><li>A non-square rectangle has 2 reflection axes and rotational order 2.</li><li>A circle has infinitely many reflection axes and rotational symmetry at every angle.</li></ul>`,
    questions: [
      { prompt: String.raw`What is the rotational symmetry order of a square?`, options: [String.raw`(1)`, String.raw`(2)`, String.raw`(3)`, String.raw`(4)`], answer: 3, solution: String.raw`The square matches itself at (90^\circ,180^\circ,270^\circ), and (360^\circ), giving order 4.` },
      { prompt: String.raw`How many lines of reflection symmetry does an equilateral triangle have?`, options: [String.raw`(1)`, String.raw`(2)`, String.raw`(3)`, String.raw`(6)`], answer: 2, solution: String.raw`Each vertex-to-opposite-side midpoint line is a reflection axis. There are three vertices, so there are 3 lines.` },
    ],
  },
  {
    id: 'geometric-constructions',
    theory: String.raw`<p>Classical geometric constructions use an unmarked straightedge and compass to create exact points and lines from given data. A perpendicular bisector passes through a segment's midpoint at (90^\circ); every point on it is equally distant from the segment's endpoints. An angle bisector divides an angle into two equal angles.</p><p><strong>Worked construction idea:</strong> To bisect segment (AB), draw equal-radius arcs from (A) and (B) with radius greater than half of (AB). Join the two arc intersections.</p>`,
    tricks: String.raw`<ul><li>Keep the compass radius unchanged when drawing paired arcs.</li><li>Use intersections of arcs rather than estimated ruler measurements.</li><li>Label the constructed midpoint, perpendicular, or bisector so the result is verifiable.</li></ul>`,
    notes: String.raw`<ul><li>A compass transfers a length and draws circles or arcs.</li><li>A perpendicular bisector is the locus of points equidistant from two endpoints.</li><li>Construction quality depends on the given data; do not assume a diagram is to scale.</li></ul>`,
    questions: [
      { prompt: String.raw`A point lies on the perpendicular bisector of segment (AB). Which statement must be true?`, options: [String.raw`It is closer to (A)`, String.raw`It is closer to (B)`, String.raw`Its distances to (A) and (B) are equal`, String.raw`It lies at the midpoint`], answer: 2, solution: String.raw`Every point on the perpendicular bisector is equidistant from the segment's endpoints. The point need not be the midpoint.` },
      { prompt: String.raw`To construct the perpendicular bisector of (AB) using equal arcs from both endpoints, what must be true about the arc radius?`, options: [String.raw`Less than half of (AB)`, String.raw`Exactly half of (AB)`, String.raw`Greater than half of (AB)`, String.raw`It must equal (AB)`], answer: 2, solution: String.raw`A radius greater than half the segment makes the arcs intersect above and below (AB); joining those intersections gives the perpendicular bisector.` },
    ],
  },
  {
    id: 'coordinate-geometry',
    theory: String.raw`<p>A point in the Cartesian plane is written ((x,y)): (x) measures horizontal position and (y) vertical position from the origin. The distance formula follows from Pythagoras; the midpoint averages the two x-coordinates and the two y-coordinates.</p><p><strong>Worked example:</strong> Distance between ((1,2)) and ((4,6)) is (sqrt{(4-1)^2+(6-2)^2}=5).</p>`,
    tricks: String.raw`<ul><li>Subtract coordinates in the same order; squaring makes the distance sign-independent.</li><li>Plot a quick sketch to identify horizontal and vertical changes.</li><li>For horizontal or vertical segments, one coordinate difference is zero.</li></ul>`,
    notes: String.raw`<ul><li>Distance: (d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}).</li><li>Midpoint: (((x_1+x_2)/2,(y_1+y_2)/2)).</li><li>Points with equal x lie on a vertical line; equal y lie on a horizontal line.</li></ul>`,
    questions: [
      { prompt: String.raw`Find the distance between (1,2) and (4,6).`, options: [String.raw`(4)`, String.raw`(5)`, String.raw`(6)`, String.raw`(7)`], answer: 1, solution: String.raw`The coordinate differences are 3 and 4. Distance (=\sqrt{3^2+4^2}=\sqrt{25}=5).` },
      { prompt: String.raw`Find the midpoint of (-2,4) and (4,0).`, options: [String.raw`(1,2)`, String.raw`(2,1)`, String.raw`(-1,2)`, String.raw`(1,4)`], answer: 0, solution: String.raw`Average the coordinates: (((-2+4)/2,(4+0)/2)=(1,2)).` },
    ],
  },
  {
    id: 'spatial-visualisation',
    theory: String.raw`<p>Spatial visualisation means interpreting shapes from different views, nets, rotations, and cross-sections. A net is a flat arrangement of faces that folds into a solid. Counting faces, edges, and vertices provides a useful structural check for polyhedra.</p><p><strong>Worked example:</strong> A cube has 6 square faces, 12 edges and 8 vertices. Euler's relation gives (F-E+V=6-12+8=2).</p>`,
    tricks: String.raw`<ul><li>Mark one face on a net, then track its adjacent faces as the net folds.</li><li>For a rotation question, identify which dimensions or visible faces change and which remain.</li><li>Use Euler's relation only for convex polyhedra: (F-E+V=2).</li></ul>`,
    notes: String.raw`<ul><li>Cube: 6 faces, 12 edges, 8 vertices.</li><li>Triangular prism: 5 faces, 9 edges, 6 vertices.</li><li>A cross-section depends on the cutting plane; it need not match a face of the solid.</li></ul>`,
    questions: [
      { prompt: String.raw`How many vertices does a cube have?`, options: [String.raw`(6)`, String.raw`(8)`, String.raw`(10)`, String.raw`(12)`], answer: 1, solution: String.raw`A cube has four vertices on each of two parallel square faces: (4+4=8).` },
      { prompt: String.raw`A triangular prism has 5 faces and 6 vertices. How many edges does it have?`, options: [String.raw`(8)`, String.raw`(9)`, String.raw`(10)`, String.raw`(11)`], answer: 1, solution: String.raw`Use (F-E+V=2): (5-E+6=2), so (E=9).` },
    ],
  },
  {
    id: 'two-dimensional-mensuration',
    theory: String.raw`<p>Mensuration calculates perimeter and area of plane figures. Perimeter measures boundary length; area measures the region inside. Use consistent units: length units for perimeter and square units for area.</p><p><strong>Worked example:</strong> A rectangle of length 8 cm and width 5 cm has area (8\cdot5=40\text{ cm}^2) and perimeter (2(8+5)=26\text{ cm}).</p>`,
    tricks: String.raw`<ul><li>Sketch and label the figure before substituting dimensions.</li><li>Split a composite figure into familiar shapes, or subtract a cut-out.</li><li>For circles, use the given value of \(\pi\) consistently and keep radius distinct from diameter.</li></ul>`,
    notes: String.raw`<ul><li>Rectangle: (A=lw, P=2(l+w)); triangle: (A=bh/2).</li><li>Circle: (A=\pi r^2, C=2\pi r).</li><li>Parallelogram: (A=bh); trapezium: (A=(a+b)h/2), where (a,b) are parallel sides.</li></ul>`,
    questions: [
      { prompt: String.raw`A circle has radius 7 cm. Using (\pi=22/7), what is its area?`, options: [String.raw`(44\text{ cm}^2)`, String.raw`(154\text{ cm}^2)`, String.raw`(308\text{ cm}^2)`, String.raw`(49\text{ cm}^2)`], answer: 1, solution: String.raw`Area (=\pi r^2=(22/7)\cdot49=154\text{ cm}^2).` },
      { prompt: String.raw`A rectangle is 8 cm by 5 cm. What is its perimeter?`, options: [String.raw`(13\text{ cm})`, String.raw`(26\text{ cm})`, String.raw`(40\text{ cm})`, String.raw`(80\text{ cm})`], answer: 1, solution: String.raw`Perimeter (=2(8+5)=26\text{ cm}).` },
    ],
  },
  {
    id: 'measurement-units-and-conversion',
    theory: String.raw`<p>Measurement compares a quantity with a standard unit. Convert by using the exact relationship between units, then keep track of whether the quantity is length, area, volume, mass, capacity or time. A squared unit conversion is also squared: (1\text{ m}^2=10,000\text{ cm}^2), not (100\text{ cm}^2).</p><p><strong>Worked example:</strong> (2.5\text{ km}=2.5\cdot1,000=2,500\text{ m}).</p>`,
    tricks: String.raw`<ul><li>Write the conversion factor as a fraction so unwanted units cancel.</li><li>Check whether the converted number should grow or shrink.</li><li>For area and volume, apply the factor to every dimension.</li></ul>`,
    notes: String.raw`<ul><li>(1\text{ km}=1,000\text{ m}); (1\text{ m}=100\text{ cm}).</li><li>(1\text{ kg}=1,000\text{ g}); (1\text{ L}=1,000\text{ mL}).</li><li>(1\text{ h}=60\text{ min}=3,600\text{ s}).</li></ul>`,
    questions: [
      { prompt: String.raw`Convert (2.5\text{ km}) to metres.`, options: [String.raw`(250\text{ m})`, String.raw`(2,050\text{ m})`, String.raw`(2,500\text{ m})`, String.raw`(25,000\text{ m})`], answer: 2, solution: String.raw`Multiply by 1,000: (2.5\cdot1,000=2,500\text{ m}).` },
      { prompt: String.raw`Convert (3.2\text{ kg}) to grams.`, options: [String.raw`(32\text{ g})`, String.raw`(320\text{ g})`, String.raw`(3,200\text{ g})`, String.raw`(32,000\text{ g})`], answer: 2, solution: String.raw`Since (1\text{ kg}=1,000\text{ g}), (3.2\text{ kg}=3,200\text{ g}).` },
    ],
  },
  {
    id: 'tables-and-data-interpretation',
    theory: String.raw`<p>Data interpretation extracts values from tables and uses arithmetic to compare categories, totals, ratios, percentages and trends. Read the title, units, labels and time period before calculating. In a two-way table, distinguish row totals, column totals and individual cells.</p><p><strong>Worked example:</strong> Sales in two years are 40 and 50 units. The increase is 10 units, or (10/40\cdot100=25\%) relative to the first year.</p>`,
    tricks: String.raw`<ul><li>Write the requested unit beside your working: people, rupees, percent, or ratio.</li><li>For percentage change, divide by the original value.</li><li>Estimate table totals first; this helps catch a transposed row or column.</li></ul>`,
    notes: String.raw`<ul><li>Percentage of total = part / total × 100%.</li><li>Percentage change = (new − original) / original × 100%.</li><li>A ratio must compare quantities in compatible units.</li></ul>`,
    questions: [
      { prompt: String.raw`A table shows 40 units sold in Year 1 and 50 in Year 2. What is the percentage increase?`, options: [String.raw`(10\%)`, String.raw`(20\%)`, String.raw`(25\%)`, String.raw`(50\%)`], answer: 2, solution: String.raw`Increase (=50-40=10). Divide by the original 40: (10/40\cdot100=25\%).` },
      { prompt: String.raw`A survey table records 24 urban and 16 rural households. What fraction of the total is rural?`, options: [String.raw`(1/5)`, String.raw`(2/5)`, String.raw`(3/5)`, String.raw`(2/3)`], answer: 1, solution: String.raw`Total (=24+16=40). Rural fraction (=16/40=2/5).` },
    ],
  },
  {
    id: 'data-sufficiency',
    theory: String.raw`<p>Data sufficiency asks whether the statements provide enough information to answer a question, not necessarily what the answer is. Test each statement alone, then both together. A statement is sufficient if it determines one answer uniquely; it is insufficient if multiple answers remain possible.</p><p>For this lesson's practice, use the choices: A = statement I alone; B = statement II alone; C = both together, neither alone; D = each alone.</p>`,
    tricks: String.raw`<ul><li>Do not solve more than needed; test uniqueness.</li><li>Consider all values allowed by the question's domain.</li><li>Use the stated answer-choice convention, which can differ between examinations.</li></ul>`,
    notes: String.raw`<ul><li>Statement I alone: sufficient only if it fixes one requested value.</li><li>Statement II alone: test independently.</li><li>When combining statements, retain every condition; do not assume unstated positive or integer values.</li></ul>`,
    questions: [
      { prompt: String.raw`What is (x)? I. (x+y=10). II. (x-y=2).`, options: [String.raw`Statement I alone`, String.raw`Statement II alone`, String.raw`Both together; neither alone`, String.raw`Each alone`], answer: 2, solution: String.raw`Each statement alone allows multiple pairs. Together, adding the equations gives (2x=12), so (x=6) uniquely. The two statements together are sufficient.` },
      { prompt: String.raw`Is (x>0)? I. (x^2=9). II. (x\ne-3).`, options: [String.raw`Statement I alone`, String.raw`Statement II alone`, String.raw`Both together; neither alone`, String.raw`Each alone`], answer: 2, solution: String.raw`Statement I alone gives (x=3) or (-3), so it is insufficient. Statement II alone permits positive and negative values, also insufficient. Together they force (x=3), so both statements together are sufficient.` },
    ],
  },
  {
    id: 'dispersion-and-standard-deviation',
    theory: String.raw`<p>Measures of dispersion describe how spread out data are. The range is maximum minus minimum. Population variance is the mean squared deviation from the population mean; standard deviation is its square root. Variance is in squared units, while standard deviation returns to the data's units.</p><p><strong>Worked example:</strong> For (2,4,6,8), the mean is 5. Squared deviations sum to (9+1+1+9=20); population variance is 5 and standard deviation is (sqrt5).</p>`,
    tricks: String.raw`<ul><li>Find the mean before calculating deviations.</li><li>Keep track of whether the problem asks for population or sample variance.</li><li>Use range as a quick spread measure, but remember it uses only two data values.</li></ul>`,
    notes: String.raw`<ul><li>Range = maximum − minimum.</li><li>Population variance (\sigma^2=\sum(x-\mu)^2/N); standard deviation (\sigma=\sqrt{\sigma^2}).</li><li>Adding the same constant to every datum leaves standard deviation unchanged.</li></ul>`,
    questions: [
      { prompt: String.raw`Find the range of (3,7,12,15).`, options: [String.raw`(8)`, String.raw`(9)`, String.raw`(12)`, String.raw`(15)`], answer: 2, solution: String.raw`Range (=15-3=12).` },
      { prompt: String.raw`For population data (2,4,6,8), what is the variance?`, options: [String.raw`(2)`, String.raw`(4)`, String.raw`(5)`, String.raw`(sqrt5)`], answer: 2, solution: String.raw`Mean (=5). Squared deviations sum to 20; divide by (N=4): variance (=5).` },
    ],
  },
  {
    id: 'permutations-and-combinations',
    theory: String.raw`<p>Use permutations when order matters and combinations when order does not. Choosing and arranging (r) objects from (n) distinct objects gives (nP_r=n!/(n-r)!); choosing only gives (nC_r=n!/[r!(n-r)!]).</p><p><strong>Worked example:</strong> Choose 2 people from 5: (5C_2=5!/(2!3!)=10). If the two roles are president and secretary, order matters and there are (5P_2=20) assignments.</p>`,
    tricks: String.raw`<ul><li>Ask whether swapping two selected items creates a different outcome.</li><li>For a line-up, multiply decreasing choices; for an unordered team, divide out the internal orders.</li><li>Use (nC_r=nC_{n-r}) when choosing the smaller side is easier.</li></ul>`,
    notes: String.raw`<ul><li>(n!=n(n-1)\cdots2\cdot1), and (0!=1).</li><li>(nP_r=n!/(n-r)!).</li><li>(nC_r=n!/[r!(n-r)!]).</li></ul>`,
    questions: [
      { prompt: String.raw`How many ways can a team of 2 be chosen from 5 people?`, options: [String.raw`(5)`, String.raw`(10)`, String.raw`(20)`, String.raw`(25)`], answer: 1, solution: String.raw`Order does not matter: (5C_2=5\cdot4/2=10).` },
      { prompt: String.raw`How many ways can 3 distinct books be arranged from 5 distinct books?`, options: [String.raw`(10)`, String.raw`(20)`, String.raw`(60)`, String.raw`(125)`], answer: 2, solution: String.raw`Order matters: (5P_3=5\cdot4\cdot3=60).` },
    ],
  },
  {
    id: 'conditional-probability',
    theory: String.raw`<p>Conditional probability updates a probability after learning that event (B) occurred: (P(A\mid B)=P(A\cap B)/P(B)), where (P(B)>0). For independent events, learning that (B) occurred does not change the probability of (A); then (P(A\mid B)=P(A)).</p><p><strong>Worked example:</strong> A bag has 3 red and 2 blue counters. Given that the first counter drawn without replacement is red, 2 of the remaining 4 are red, so the chance the second is red is (1/2).</p>`,
    tricks: String.raw`<ul><li>After conditioning, restrict the sample space to outcomes consistent with the given event.</li><li>For draws without replacement, update the counts after each draw.</li><li>Check independence instead of assuming it.</li></ul>`,
    notes: String.raw`<ul><li>(P(A\mid B)=P(A\cap B)/P(B)).</li><li>Independent events: (P(A\cap B)=P(A)P(B)).</li><li>For a fair die, conditioning on an even result leaves sample space ({2,4,6}).</li></ul>`,
    questions: [
      { prompt: String.raw`A fair die is rolled. Given that the result is even, what is the probability it is greater than 3?`, options: [String.raw`(1/3)`, String.raw`(1/2)`, String.raw`(2/3)`, String.raw`(1)`], answer: 2, solution: String.raw`The conditioned outcomes are ({2,4,6}); those greater than 3 are ({4,6}). Probability (=2/3).` },
      { prompt: String.raw`A bag has 3 red and 2 blue counters. Two are drawn without replacement. Given the first is red, what is the chance the second is red?`, options: [String.raw`(1/5)`, String.raw`(1/2)`, String.raw`(3/5)`, String.raw`(2/3)`], answer: 1, solution: String.raw`After one red is removed, 2 red counters remain among 4 counters, so the probability is (2/4=1/2).` },
    ],
  },
  {
    id: 'set-theory-and-venn-diagrams',
    theory: String.raw`<p>A set is a collection of distinct objects. The union (A\cup B) contains members in either set; the intersection (A\cap B) contains members in both. A Venn diagram shows overlaps so that totals are counted once.</p><p><strong>Worked example:</strong> If (n(A)=20,n(B)=15,n(A\cap B)=5), then (n(A\cup B)=20+15-5=30).</p>`,
    tricks: String.raw`<ul><li>Place the intersection first, then fill the non-overlapping regions.</li><li>Subtract overlap when adding two set totals.</li><li>For three sets, use inclusion-exclusion and add back the triple intersection once.</li></ul>`,
    notes: String.raw`<ul><li>(n(A\cup B)=n(A)+n(B)-n(A\cap B)).</li><li>Neither = universal total − union.</li><li>The complement (A^c) contains elements in the universal set that are not in (A).</li></ul>`,
    questions: [
      { prompt: String.raw`In a group of 40, 24 study tea, 18 study coffee, and 10 study both. How many study neither?`, options: [String.raw`(6)`, String.raw`(8)`, String.raw`(10)`, String.raw`(12)`], answer: 1, solution: String.raw`Union (=24+18-10=32). Neither (=40-32=8).` },
      { prompt: String.raw`If (n(A)=20,n(B)=15,n(A\cap B)=5), find (n(A\cup B)).`, options: [String.raw`(25)`, String.raw`(30)`, String.raw`(35)`, String.raw`(40)`], answer: 1, solution: String.raw`Use inclusion-exclusion: (20+15-5=30).` },
    ],
  },
  {
    id: 'number-series',
    theory: String.raw`<p>A number series is an ordered sequence governed by a rule. Common rules use a constant difference, constant ratio, alternating operations, squares, cubes, primes, or two interleaved sequences. A proposed rule should explain every term, not just the last pair.</p><p><strong>Worked example:</strong> In (2,5,10,17,\ldots), the differences are 3, 5, 7; the next difference is 9, so the next term is 26.</p>`,
    tricks: String.raw`<ul><li>First inspect differences, then ratios, then alternating or paired patterns.</li><li>Check a candidate rule against all supplied terms.</li><li>For two interleaved sequences, separate odd-position and even-position terms.</li></ul>`,
    notes: String.raw`<ul><li>Constant difference indicates an arithmetic progression.</li><li>Constant ratio indicates a geometric progression.</li><li>Squares (1,4,9,16,\ldots) and cubes (1,8,27,\ldots) are common patterns.</li></ul>`,
    questions: [
      { prompt: String.raw`Find the next term: (2,5,10,17,\ldots).`, options: [String.raw`(24)`, String.raw`(25)`, String.raw`(26)`, String.raw`(27)`], answer: 2, solution: String.raw`The differences are 3, 5, 7, increasing by 2. Add 9: (17+9=26).` },
      { prompt: String.raw`Find the next term: (81,27,9,3,\ldots).`, options: [String.raw`(0)`, String.raw`(1)`, String.raw`(2)`, String.raw`(6)`], answer: 1, solution: String.raw`Each term is divided by 3, so the next term is (3/3=1).` },
    ],
  },
  {
    id: 'quantity-comparison',
    theory: String.raw`<p>Quantity comparison asks which of two expressions is greater, whether they are equal, or whether the relationship cannot be determined. Simplify both sides, use bounds, or test permitted cases. If variables have constraints, apply them before comparing.</p><p><strong>Worked example:</strong> (A=20\%\text{ of }50=10), while (B=15\%\text{ of }80=12); therefore (B>A).</p>`,
    tricks: String.raw`<ul><li>Compare simplified values rather than evaluating large expressions separately.</li><li>For an unknown variable, test the full permitted domain before declaring a fixed relationship.</li><li>Use equal denominators or common factors to compare fractions.</li></ul>`,
    notes: String.raw`<ul><li>“Cannot be determined” is appropriate when valid choices of variables produce different comparisons.</li><li>Squaring both sides preserves order only when both sides are known nonnegative.</li><li>For percentages, identify the base quantity before comparing.</li></ul>`,
    questions: [
      { prompt: String.raw`Compare (A=20\%\text{ of }50) and (B=15\%\text{ of }80).`, options: [String.raw`(A>B)`, String.raw`(A<B)`, String.raw`(A=B)`, String.raw`Cannot be determined`], answer: 1, solution: String.raw`(A=10) and (B=12), so (A<B).` },
      { prompt: String.raw`For real (x), compare (x^2) and (x).`, options: [String.raw`(x^2>x) always`, String.raw`(x^2<x) always`, String.raw`(x^2=x) always`, String.raw`Cannot be determined`], answer: 3, solution: String.raw`At (x=2), (x^2>x); at (x=1/2), (x^2<x); at (x=0), they are equal. The relationship depends on (x).` },
    ],
  },
  {
    id: 'mathematical-operations-and-symbols',
    theory: String.raw`<p>Coded-operation questions define a new symbol or rule, then ask you to apply it exactly as stated. The symbol may not have its usual arithmetic meaning. Substitute the given values, respect brackets, and distinguish the defined operation from ordinary multiplication or division.</p><p><strong>Worked example:</strong> If (a*b=a+b), then (4*3=4+3=7).</p>`,
    tricks: String.raw`<ul><li>Rewrite the definition beside each question before substituting.</li><li>Use brackets when a result becomes an input to another operation.</li><li>Check whether the rule is commutative or changes with argument order.</li></ul>`,
    notes: String.raw`<ul><li>A custom operator is defined only by the question's rule.</li><li>For (a\star b=a^2-b), swap (a,b) only if the expression asks for it; order matters.</li><li>Apply standard order of operations inside the defined rule.</li></ul>`,
    questions: [
      { prompt: String.raw`If (a*b=a+b), what is (7*5)?`, options: [String.raw`(2)`, String.raw`(12)`, String.raw`(35)`, String.raw`(75)`], answer: 1, solution: String.raw`Replace the custom symbol using its definition: (7*5=7+5=12).` },
      { prompt: String.raw`If (a\#b=a^2-b), find (5\#2).`, options: [String.raw`(13)`, String.raw`(21)`, String.raw`(23)`, String.raw`(27)`], answer: 2, solution: String.raw`Substitute (a=5,b=2): (5^2-2=25-2=23).` },
    ],
  },
  {
    id: 'clocks-and-calendars',
    theory: String.raw`<p>Clock questions compare the positions of the hour and minute hands. At (h:m), the minute hand is (6m^\circ) from 12 and the hour hand is (30h+0.5m^\circ) from 12. Take the smaller angle between them. Calendar questions use the fact that days repeat every 7 days.</p><p><strong>Worked example:</strong> At 3:00, the hands are (90^\circ) apart. Forty-five days after Sunday is Wednesday because (45\equiv3pmod7).</p>`,
    tricks: String.raw`<ul><li>For clock angles, calculate both hand positions from 12 before subtracting.</li><li>Reduce a day offset modulo 7; a remainder of 0 means the same weekday.</li><li>Count leap years only when the interval includes February 29 and the calendar rule applies.</li></ul>`,
    notes: String.raw`<ul><li>Minute-hand angle = (6m^\circ).</li><li>Hour-hand angle = (30h+0.5m^\circ).</li><li>Smaller angle = the smaller of (d) and (360^\circ-d), where (d) is the absolute difference.</li></ul>`,
    questions: [
      { prompt: String.raw`What is the smaller angle between the clock hands at 3:00?`, options: [String.raw`(60^\circ)`, String.raw`(90^\circ)`, String.raw`(120^\circ)`, String.raw`(180^\circ)`], answer: 1, solution: String.raw`At 3:00, the hour hand is (90^\circ) from 12 and the minute hand is at (0^\circ). Their smaller angle is (90^\circ).` },
      { prompt: String.raw`What day is 45 days after Sunday?`, options: [String.raw`Monday`, String.raw`Tuesday`, String.raw`Wednesday`, String.raw`Thursday`], answer: 2, solution: String.raw`(45=6\cdot7+3), so move forward 3 days from Sunday: Wednesday.` },
    ],
  },
  {
    id: 'logical-numerical-reasoning',
    theory: String.raw`<p>Logical numerical reasoning combines arithmetic with constraints. Translate each condition into a relation, eliminate impossible values, and ensure the conclusion follows from all conditions. A pattern is valid only when it is supported by the given information.</p><p><strong>Worked example:</strong> Two numbers total 30 and are in the ratio (2:3). The five ratio parts equal 30, so one part is 6 and the numbers are 12 and 18.</p>`,
    tricks: String.raw`<ul><li>Separate facts from assumptions; use only information stated or logically implied.</li><li>Use a table for several variables or cases.</li><li>Check the final values against every constraint and the requested order.</li></ul>`,
    notes: String.raw`<ul><li>Ratio (a:b) with sum (S) gives values (aS/(a+b)) and (bS/(a+b)).</li><li>For integer constraints, test parity and divisibility early.</li><li>For a “must be true” claim, one valid counterexample disproves it.</li></ul>`,
    questions: [
      { prompt: String.raw`Two numbers sum to 30 and have ratio (2:3). What is the smaller number?`, options: [String.raw`(10)`, String.raw`(12)`, String.raw`(15)`, String.raw`(18)`], answer: 1, solution: String.raw`The total has 5 parts, so one part is (30/5=6). The smaller number is (2\cdot6=12).` },
      { prompt: String.raw`A two-digit number has tens digit 3 and units digit 7. What is the number?`, options: [String.raw`(37)`, String.raw`(73)`, String.raw`(307)`, String.raw`(10)`], answer: 0, solution: String.raw`The tens digit contributes (3\cdot10=30); the units digit contributes 7. The number is 37.` },
    ],
  },
  {
    id: 'addition-subtraction-multiplication-division',
    theory: String.raw`<p>The four operations model combining, finding a difference, equal groups, and sharing or measuring groups. The inverse pairs are addition/subtraction and multiplication/division. Estimation and inverse checks help verify results.</p><p><strong>Worked example:</strong> (8+6\cdot2=8+12=20), because multiplication is done before addition.</p>`,
    tricks: String.raw`<ul><li>Estimate a sum or product before calculating exactly.</li><li>For subtraction, check by adding the difference back.</li><li>For division, verify quotient × divisor + remainder = dividend.</li></ul>`,
    notes: String.raw`<ul><li>Addition and multiplication are commutative; subtraction and division are not.</li><li>Multiplication and division have equal priority and are evaluated left to right.</li><li>Division by zero is undefined.</li></ul>`,
    questions: [
      { prompt: String.raw`Evaluate (8+6\cdot2).`, options: [String.raw`(20)`, String.raw`(28)`, String.raw`(32)`, String.raw`(14)`], answer: 0, solution: String.raw`Multiply first: (6\cdot2=12). Then (8+12=20).` },
      { prompt: String.raw`Evaluate (45\div5+7).`, options: [String.raw`(9)`, String.raw`(12)`, String.raw`(16)`, String.raw`(52)`], answer: 2, solution: String.raw`Divide first: (45\div5=9); then (9+7=16).` },
    ],
  },
  {
    id: 'money-and-everyday-arithmetic',
    theory: String.raw`<p>Money problems use decimal arithmetic for price, payment, change, discounts and totals. Align decimal points when adding or subtracting; interpret a percentage discount relative to the marked price. Keep the currency unit through each calculation.</p><p><strong>Worked example:</strong> A ₹800 item discounted by 10% costs (800-80=₹720).</p>`,
    tricks: String.raw`<ul><li>Calculate the discount amount first, then subtract it from the marked price.</li><li>For multiple items, multiply unit cost by quantity before adding.</li><li>Check change by adding change to the purchase total; it should equal the payment.</li></ul>`,
    notes: String.raw`<ul><li>Discount amount = marked price × discount rate.</li><li>Change = amount paid − bill total.</li><li>Convert paise to rupees using 100 paise = ₹1.</li></ul>`,
    questions: [
      { prompt: String.raw`A customer pays ₹500 for a bill of ₹376. What change is due?`, options: [String.raw`₹114`, String.raw`₹124`, String.raw`₹134`, String.raw`₹224`], answer: 1, solution: String.raw`Change (=500-376=₹124).` },
      { prompt: String.raw`An ₹800 item has a 10% discount. What is the price after discount?`, options: [String.raw`₹700`, String.raw`₹710`, String.raw`₹720`, String.raw`₹780`], answer: 2, solution: String.raw`Discount (=0.10\cdot800=₹80). Price (=800-80=₹720).` },
    ],
  },
  {
    id: 'time-and-measurement',
    theory: String.raw`<p>Time and measurement problems convert quantities to common units before comparing or combining. One hour is 60 minutes; one kilogram is 1,000 grams; one litre is 1,000 millilitres. For elapsed time, account for hour and minute boundaries rather than subtracting clock digits independently.</p><p><strong>Worked example:</strong> (2\text{ h }35\text{ min}=2\cdot60+35=155\text{ min}).</p>`,
    tricks: String.raw`<ul><li>Convert every quantity to one unit before adding or subtracting.</li><li>For elapsed time across noon or midnight, count the remaining part of the first day and then the next.</li><li>Estimate whether the converted number should be larger or smaller.</li></ul>`,
    notes: String.raw`<ul><li>(1\text{ h}=60\text{ min}); (1\text{ min}=60\text{ s}).</li><li>(1\text{ kg}=1,000\text{ g}); (1\text{ L}=1,000\text{ mL}).</li><li>Length, mass, capacity and time are distinct dimensions; do not add unlike units.</li></ul>`,
    questions: [
      { prompt: String.raw`Convert (2\text{ h }35\text{ min}) into minutes.`, options: [String.raw`(125\text{ min})`, String.raw`(145\text{ min})`, String.raw`(155\text{ min})`, String.raw`(235\text{ min})`], answer: 2, solution: String.raw`Two hours are 120 minutes; (120+35=155) minutes.` },
      { prompt: String.raw`Convert (3.5\text{ L}) into millilitres.`, options: [String.raw`(350\text{ mL})`, String.raw`(3,050\text{ mL})`, String.raw`(3,500\text{ mL})`, String.raw`(35,000\text{ mL})`], answer: 2, solution: String.raw`Since one litre is 1,000 mL, (3.5\cdot1,000=3,500) mL.` },
    ],
  },
  {
    id: 'patterns-and-sequences-school-mathematics',
    theory: String.raw`<p>A pattern repeats or changes according to a rule. It can use shapes, colours, positions, numbers or operations. Describe the smallest repeating unit or the change from one term to the next, then use the rule to predict or extend the pattern.</p><p><strong>Worked example:</strong> In (2,4,8,16,\ldots), each term doubles, so the next is 32.</p>`,
    tricks: String.raw`<ul><li>Compare corresponding features: shape, orientation, colour, count and position.</li><li>For number patterns, inspect differences and ratios.</li><li>Ask learners to explain the rule, not only name the next item.</li></ul>`,
    notes: String.raw`<ul><li>A repeating pattern has a fixed cycle unit.</li><li>A growing pattern changes by a consistent rule.</li><li>More than one rule may fit a short sequence; use the simplest rule supported by the context.</li></ul>`,
    questions: [
      { prompt: String.raw`Continue the pattern: (2,4,8,16,\ldots).`, options: [String.raw`(18)`, String.raw`(24)`, String.raw`(30)`, String.raw`(32)`], answer: 3, solution: String.raw`Each term is twice the previous term; (16\cdot2=32).` },
      { prompt: String.raw`Continue the square-number pattern: (1,4,9,16,\ldots).`, options: [String.raw`(20)`, String.raw`(24)`, String.raw`(25)`, String.raw`(36)`], answer: 2, solution: String.raw`These are (1^2,2^2,3^2,4^2); the next is (5^2=25).` },
    ],
  },
  {
    id: 'shapes-and-spatial-understanding',
    theory: String.raw`<p>Shape and spatial understanding includes describing 2D figures, recognising 3D solids, comparing attributes, and imagining how shapes fit or move. Classify a shape by properties such as sides, vertices, faces, edges, parallel sides and right angles rather than by appearance alone.</p><p><strong>Worked example:</strong> A hexagon has six sides and six vertices. A rectangular prism has six rectangular faces, 12 edges and 8 vertices.</p>`,
    tricks: String.raw`<ul><li>Rotate a shape mentally; its properties remain unchanged.</li><li>Count vertices and edges systematically, starting from one face or layer.</li><li>Separate a solid's faces from its edges and vertices.</li></ul>`,
    notes: String.raw`<ul><li>A polygon is a closed plane figure made of straight segments.</li><li>A prism has two matching parallel bases; its side faces are parallelograms.</li><li>For convex polyhedra, (F-E+V=2).</li></ul>`,
    questions: [
      { prompt: String.raw`How many sides does a hexagon have?`, options: [String.raw`(5)`, String.raw`(6)`, String.raw`(7)`, String.raw`(8)`], answer: 1, solution: String.raw`The prefix “hexa-” indicates six; a hexagon has six sides.` },
      { prompt: String.raw`How many faces does a rectangular prism have?`, options: [String.raw`(4)`, String.raw`(5)`, String.raw`(6)`, String.raw`(8)`], answer: 2, solution: String.raw`A rectangular prism has top, bottom, front, back, left and right faces: six in total.` },
    ],
  },
  {
    id: 'data-handling-school-mathematics',
    theory: String.raw`<p>Data handling collects, organises, represents and interprets information. A tally table records counts efficiently; pictographs and bar charts compare categories; a line graph is useful for change over time. Always read the title, scale, labels and key before interpreting a display.</p><p><strong>Worked example:</strong> If a pictograph uses one icon for 4 books and shows 5 icons, it represents (5\cdot4=20) books.</p>`,
    tricks: String.raw`<ul><li>Check whether a picture symbol represents one item or a group.</li><li>Read bar-chart scales between marked grid lines carefully.</li><li>Use the table totals to check the number of observations.</li></ul>`,
    notes: String.raw`<ul><li>Mode is the most frequent value; range is maximum minus minimum.</li><li>A bar chart uses separated bars for categories; a histogram represents grouped continuous intervals.</li><li>A graph's visual scale can exaggerate or reduce apparent differences.</li></ul>`,
    questions: [
      { prompt: String.raw`A pictograph uses one book symbol for 4 books. How many books do 5 symbols represent?`, options: [String.raw`(9)`, String.raw`(16)`, String.raw`(20)`, String.raw`(25)`], answer: 2, solution: String.raw`Multiply symbols by the key value: (5\cdot4=20) books.` },
      { prompt: String.raw`A data set is (2,3,3,5,7). What is its mode?`, options: [String.raw`(2)`, String.raw`(3)`, String.raw`(5)`, String.raw`(7)`], answer: 1, solution: String.raw`The value 3 appears twice; each other value appears once. The mode is 3.` },
    ],
  },
  {
    id: 'nature-and-logical-thinking-in-mathematics',
    theory: String.raw`<p>Mathematics develops precise reasoning about quantity, shape, structure, patterns and change. Logical thinking includes making conjectures, checking examples, identifying counterexamples, explaining steps and justifying conclusions. A correct answer is stronger when the learner can explain why the method works.</p><p>Inductive reasoning proposes a rule from examples; deductive reasoning applies established facts to reach a necessary conclusion. A few examples can suggest a conjecture but do not prove a universal statement.</p>`,
    tricks: String.raw`<ul><li>Ask “How do you know?” and “Will it always work?” to elicit reasoning.</li><li>Use a counterexample to test a universal claim.</li><li>Encourage more than one representation: objects, diagrams, words, tables and symbols.</li></ul>`,
    notes: String.raw`<ul><li>Induction generalises from cases; deduction derives a conclusion from accepted premises.</li><li>Problem solving includes understanding, planning, carrying out and checking.</li><li>Errors can reveal a learner's current strategy and misconception.</li></ul>`,
    questions: [
      { prompt: String.raw`A learner observes that the first five odd numbers sum to their count squared and conjectures this is always true. What kind of reasoning formed the conjecture?`, options: [String.raw`Inductive`, String.raw`Deductive`, String.raw`Circular`, String.raw`Contradictory`], answer: 0, solution: String.raw`The learner generalised a rule from several examples, which is inductive reasoning. A proof would still be needed to establish it for all cases.` },
      { prompt: String.raw`What is the strongest way to disprove the claim “every prime number is odd”?`, options: [String.raw`Give another odd prime`, String.raw`Give the counterexample 2`, String.raw`Repeat the definition`, String.raw`Draw a number line`], answer: 1, solution: String.raw`A single counterexample disproves a universal claim. The number 2 is prime and even.` },
    ],
  },
  {
    id: 'mathematics-curriculum-and-classroom',
    theory: String.raw`<p>A mathematics curriculum organises learning goals, content, progression, experiences and assessment. Effective planning connects prior knowledge to new ideas, gives learners time to reason and practise, and uses tasks that reveal understanding. A spiral progression revisits important ideas with increasing depth.</p><p>Classroom activities should align with the intended learning outcome; a lesson on fraction equivalence, for example, needs opportunities to compare and explain equivalent fractions.</p>`,
    tricks: String.raw`<ul><li>State a measurable learning outcome before choosing an activity.</li><li>Sequence concrete experiences, visual models and symbolic work when appropriate.</li><li>Use questions that expose reasoning, not just final answers.</li></ul>`,
    notes: String.raw`<ul><li>Curriculum, instruction and assessment should support the same learning goals.</li><li>Prior knowledge influences how learners interpret new mathematics.</li><li>Flexible grouping can provide support or extension without fixing labels on learners.</li></ul>`,
    questions: [
      { prompt: String.raw`Which plan best aligns a lesson on equivalent fractions with assessment?`, options: [String.raw`Memorise unrelated multiplication facts`, String.raw`Use fraction strips, then ask learners to explain why two fractions are equal`, String.raw`Copy a definition only`, String.raw`Skip practice and give a spelling test`], answer: 1, solution: String.raw`The model and explanation directly assess the learning goal: recognising and justifying equivalent fractions.` },
      { prompt: String.raw`What does a spiral curriculum do?`, options: [String.raw`Avoids revisiting topics`, String.raw`Repeats a topic at the same level only`, String.raw`Revisits key ideas with increasing depth`, String.raw`Teaches only through examinations`], answer: 2, solution: String.raw`A spiral curriculum returns to important concepts over time and develops them at increasing levels of complexity.` },
    ],
  },
  {
    id: 'language-of-mathematics',
    theory: String.raw`<p>Mathematical language includes everyday words, specialised terms, symbols, diagrams and statements. Learners need to connect these forms and understand that familiar words may have precise mathematical meanings: “difference,” “product,” “at least,” and “congruent” each carry specific meaning.</p><p>For example, “8 less than (x)” is (x-8), while “8 less than twice (x)” is (2x-8).</p>`,
    tricks: String.raw`<ul><li>Ask learners to restate a symbol or equation in words and draw a matching representation.</li><li>Teach vocabulary in context rather than as an isolated list.</li><li>Compare similar phrases that reverse operation order, such as “5 less than x” and “5 minus x.”</li></ul>`,
    notes: String.raw`<ul><li>“At least 5” means (x\ge5); “more than 5” means (x>5).</li><li>“Product” means multiplication; “quotient” means division.</li><li>Language support should preserve the mathematical idea while allowing learners to explain it in familiar language.</li></ul>`,
    questions: [
      { prompt: String.raw`Which expression means “8 less than (x)”?`, options: [String.raw`(8-x)`, String.raw`(x-8)`, String.raw`(8x)`, String.raw`(x/8)`], answer: 1, solution: String.raw`Start with (x) and subtract 8: (x-8).` },
      { prompt: String.raw`Which inequality means “at least 5”?`, options: [String.raw`(x<5)`, String.raw`(x\le5)`, String.raw`(x>5)`, String.raw`(x\ge5)`], answer: 3, solution: String.raw`“At least” includes 5 and values above it, so (x\ge5).` },
    ],
  },
  {
    id: 'child-thinking-and-mathematical-misconceptions',
    theory: String.raw`<p>Learners build mathematical ideas through prior knowledge, language, representations and practice. An incorrect answer can show a consistent strategy rather than carelessness. For example, comparing (1/3) and (1/2) by denominator size alone ignores that equal wholes are divided into different numbers of parts.</p><p>Teachers can ask learners to explain or model their thinking, identify the point where a strategy fails, then connect a more useful representation.</p>`,
    tricks: String.raw`<ul><li>Ask learners to show a model or explain a step before correcting an answer.</li><li>Use diagnostic examples that distinguish likely misconceptions.</li><li>Respond to the reasoning error, not only the final result.</li></ul>`,
    notes: String.raw`<ul><li>For equal numerators, the fraction with the smaller positive denominator is larger.</li><li>Equivalent representations can expose a misconception: (1/2=3/6), while (1/3=2/6).</li><li>Errors are evidence for instructional decisions and should be treated respectfully.</li></ul>`,
    questions: [
      { prompt: String.raw`A learner says (1/3>1/2) because 3 is greater than 2. Which response best addresses the misconception?`, options: [String.raw`Tell the learner to memorise the answer`, String.raw`Use equal-sized fraction strips to compare the parts`, String.raw`Change the topic`, String.raw`Say denominators are never useful`], answer: 1, solution: String.raw`Fraction strips make the whole and partition sizes visible: one half is larger than one third. The model addresses the reasoning behind the error.` },
      { prompt: String.raw`A learner writes (0.4=0.04). Which representation best supports correction?`, options: [String.raw`A place-value chart showing tenths and hundredths`, String.raw`A multiplication table only`, String.raw`A calendar`, String.raw`A triangle diagram`], answer: 0, solution: String.raw`A place-value chart shows (0.4) as 4 tenths and (0.04) as 4 hundredths, making their difference explicit.` },
    ],
  },
  {
    id: 'assessment-in-mathematics',
    theory: String.raw`<p>Assessment gathers evidence about mathematical understanding and uses it to guide learning. Formative assessment happens during instruction and informs next steps; summative assessment evaluates learning at the end of a unit or period. Diagnostic assessment identifies prior knowledge or a specific learning gap.</p><p>Useful evidence includes explanations, representations, questions, written work and observed strategies—not only a total score.</p>`,
    tricks: String.raw`<ul><li>Match each assessment item to the intended learning outcome.</li><li>Use short checks during a lesson so misconceptions can be addressed promptly.</li><li>Give feedback that identifies a next step, not only right or wrong.</li></ul>`,
    notes: String.raw`<ul><li>Formative: supports adjustment during learning.</li><li>Summative: judges achievement after a period of instruction.</li><li>Diagnostic: locates starting points, prior knowledge or gaps.</li></ul>`,
    questions: [
      { prompt: String.raw`A teacher uses an exit ticket to plan the next day's lesson. What is its main purpose?`, options: [String.raw`Formative assessment`, String.raw`Summative assessment`, String.raw`Placement only`, String.raw`Certification`], answer: 0, solution: String.raw`The exit ticket provides evidence during instruction and informs the next teaching step, so it is formative.` },
      { prompt: String.raw`A test at the end of a term is primarily which type of assessment?`, options: [String.raw`Diagnostic`, String.raw`Summative`, String.raw`Informal observation`, String.raw`Peer tutoring`], answer: 1, solution: String.raw`An end-of-term test evaluates achievement after a period of instruction, which is summative assessment.` },
    ],
  },
  {
    id: 'remedial-teaching-in-mathematics',
    theory: String.raw`<p>Remedial teaching responds to an identified learning gap with focused instruction and practice. Begin by diagnosing the prerequisite idea, then select a suitable representation, teach in manageable steps, provide guided practice and check progress. Support should be timely and respectful.</p><p><strong>Example:</strong> If a learner cannot add fractions with unlike denominators, first check equivalent fractions and common multiples before assigning longer exercises.</p>`,
    tricks: String.raw`<ul><li>Use assessment evidence to identify the specific gap instead of repeating the entire chapter.</li><li>Provide immediate feedback and a fresh check after instruction.</li><li>Fade prompts as the learner gains independence.</li></ul>`,
    notes: String.raw`<ul><li>Effective support is targeted, systematic and monitored.</li><li>Use concrete or visual models when abstract symbols are not yet secure.</li><li>Extension activities are also needed when learners have already mastered the target.</li></ul>`,
    questions: [
      { prompt: String.raw`Several learners make errors adding fractions with unlike denominators. What should the teacher do first?`, options: [String.raw`Assign harder fraction sums`, String.raw`Diagnose understanding of equivalent fractions and common denominators`, String.raw`Remove all fraction work`, String.raw`Give the same explanation louder`], answer: 1, solution: String.raw`The teacher should locate the prerequisite gap before planning targeted instruction.` },
      { prompt: String.raw`After targeted instruction, what best checks whether the support worked?`, options: [String.raw`A new problem testing the same skill independently`, String.raw`Repeating the original lecture only`, String.raw`A spelling quiz`, String.raw`No follow-up`], answer: 0, solution: String.raw`An independent, aligned problem provides evidence of whether the learner can now use the skill.` },
    ],
  },
  {
    id: 'mathematics-teaching-methods-and-materials',
    theory: String.raw`<p>Mathematics teaching can connect concrete objects, visual representations and abstract symbols. The concrete–representational–abstract progression helps learners build meaning, but transitions should depend on understanding rather than a fixed timetable. Learning materials should clarify the concept and invite mathematical action.</p><p>Fraction strips can model equivalence; place-value blocks can model regrouping; a number line can show order and operations.</p>`,
    tricks: String.raw`<ul><li>Ask what concept a material makes visible before using it.</li><li>Invite learners to predict, manipulate, describe and then record with symbols.</li><li>Move from a model to a matching equation so the representation is connected to notation.</li></ul>`,
    notes: String.raw`<ul><li>Concrete, visual and symbolic forms should reinforce one another.</li><li>A teaching aid is useful when learners reason with it, not merely look at it.</li><li>Check accessibility, safety and fit for the learning goal.</li></ul>`,
    questions: [
      { prompt: String.raw`Which material best models equivalent fractions such as (1/2) and (2/4)?`, options: [String.raw`Fraction strips of equal length`, String.raw`A calendar`, String.raw`A thermometer`, String.raw`A multiplication-only worksheet`], answer: 0, solution: String.raw`Equal-length fraction strips let learners compare the same whole and see that one half covers the same length as two fourths.` },
      { prompt: String.raw`Which sequence best connects regrouping in subtraction to written notation?`, options: [String.raw`Memorise an answer, then skip explanation`, String.raw`Use place-value blocks, draw the regrouping, then record the algorithm`, String.raw`Start with a timed test only`, String.raw`Teach unrelated geometry first`], answer: 1, solution: String.raw`The sequence connects a concrete model, a visual record and the symbolic algorithm.` },
    ],
  },
  {
    id: 'community-mathematics-and-inclusion',
    theory: String.raw`<p>Community mathematics connects mathematical ideas to meaningful contexts such as shopping, travel, measurement, local data and shared problem solving. Inclusive teaching anticipates differences in language, prior experience, access and pace, while maintaining meaningful learning goals for every learner.</p><p>Offer multiple ways to engage and respond—objects, diagrams, spoken explanations, large-print materials or assistive tools—so the mathematics remains accessible.</p>`,
    tricks: String.raw`<ul><li>Choose familiar, respectful contexts without stereotyping learners or communities.</li><li>Offer more than one representation and allow appropriate response modes.</li><li>Check that examples do not require background knowledge unrelated to the mathematical goal.</li></ul>`,
    notes: String.raw`<ul><li>Context can make a concept meaningful, but the underlying mathematics should remain explicit.</li><li>Universal design plans accessibility from the start rather than waiting for a learner to fail.</li><li>Use community knowledge as a resource and validate learners' strategies.</li></ul>`,
    questions: [
      { prompt: String.raw`A learner with low vision is working on a shape-classification task. Which adjustment best preserves the goal?`, options: [String.raw`Remove the mathematics task`, String.raw`Provide tactile shapes or enlarged high-contrast figures`, String.raw`Give only an unrelated oral test`, String.raw`Ask the learner to copy a distant board`], answer: 1, solution: String.raw`Tactile or enlarged high-contrast shapes improve access while preserving the classification objective.` },
      { prompt: String.raw`Which is the strongest use of a local shopping context for teaching addition?`, options: [String.raw`Use prices to add totals and explain the strategy`, String.raw`Mention shopping without doing mathematics`, String.raw`Require knowledge of a specific brand`, String.raw`Exclude learners unfamiliar with the store`], answer: 0, solution: String.raw`The prices create a meaningful context for the target operation, and learners explain the mathematics involved.` },
    ],
  },
];

function assertCatalog(catalog) {
  if (catalog.schemaVersion !== 1 || !Array.isArray(catalog.groups)) {
    throw new Error('Unsupported quantitative aptitude catalog format.');
  }
}

function formatMathFragment(value) {
  const slash = String.fromCharCode(92);
  const html = String(value)
    .replace(/sqrt\s*\{?(\d+)\}?/g, `${slash}sqrt{$1}`)
    .replaceAll('pmod', `${slash}pmod`)
    .replaceAll('lfloor', `${slash}lfloor`)
    .replaceAll(`${slash}${slash}lfloor`, `${slash}lfloor`)
    .replaceAll('sum_', `${slash}sum_`)
    .replaceAll(`${slash}${slash}sum_`, `${slash}sum_`);
  const pairs = [];
  const stack = [];
  let insideMathJax = false;
  for (let index = 0; index < html.length; index += 1) {
    if (html[index] === slash && html[index + 1] === '(') {
      insideMathJax = true;
      index += 1;
      continue;
    }
    if (html[index] === slash && html[index + 1] === ')') {
      insideMathJax = false;
      index += 1;
      continue;
    }
    if (insideMathJax) continue;
    if (html[index] === '(') stack.push(index);
    if (html[index] === ')' && stack.length) pairs.push({ start: stack.pop(), end: index });
  }
  pairs.sort((a, b) => a.start - b.start || b.end - a.end);

  const edits = [];
  let coveredUntil = -1;
  for (const pair of pairs) {
    if (pair.start < coveredUntil) continue;
    const expression = html.slice(pair.start + 1, pair.end).trim();
    const mathLike = /[0-9=+*/^<>]/.test(expression)
      || expression.includes(slash)
      || /^[A-Za-z]$/.test(expression)
      || /^[A-Za-z],[A-Za-z]$/.test(expression);
    if (!mathLike) continue;
    edits.push({ index: pair.end, value: `${slash})` }, { index: pair.start + 1, value: `${slash}(` });
    coveredUntil = pair.end;
  }

  let formatted = html;
  for (const edit of edits.sort((a, b) => b.index - a.index)) {
    formatted = `${formatted.slice(0, edit.index)}${edit.value}${formatted.slice(edit.index)}`;
  }
  const mathCommands = [
    [/(?<!\\)\btimes\b/g, slash + 'times'],
    [/(?<!\\)\bdiv\b/g, slash + 'div'],
    [/(?<!\\)\ble\b/g, slash + 'le'],
    [/(?<!\\)\bge\b/g, slash + 'ge'],
    [/(?<!\\)\bneq\b/g, slash + 'neq'],
    [/(?<!\\)\bequiv\b/g, slash + 'equiv'],
    [/(?<!\\)\bsubset\b/g, slash + 'subset'],
    [/(?<!\\)\bunion\b/g, slash + 'cup'],
    [/(?<!\\)\bintersect\b/g, slash + 'cap'],
    [/(?<!\\)\bin\b/g, slash + 'in'],
    [/(?<!\\)\bmod\b/g, slash + 'bmod'],
    [/(?<!\\)\bplusminus\b/g, slash + 'pm'],
    [/(?<!\\)\bpi\b/g, slash + 'pi'],
    [/(?<!\\)\bDelta\b/g, slash + 'Delta'],
    [/(?<!\\)\bsum\b/g, slash + 'sum'],
    [/(?<!\\)\bmin\b/g, slash + 'min'],
    [/(?<!\\)\bmax\b/g, slash + 'max'],
    [/(?<!\\)\bfloor\b/g, slash + 'operatorname{floor}'],
    [/(?<!\\)\bdegrees\b/g, '^' + slash + 'circ'],
  ];
  return formatted.replace(/\\\(([\s\S]*?)\\\)/g, (match, expression) => {
    const replaceFunction = (source, name, render) => {
      let result = '';
      let cursor = 0;
      const matcher = new RegExp('\\b' + name + '\\s*\\(', 'g');
      let found;
      while ((found = matcher.exec(source))) {
        const open = matcher.lastIndex - 1;
        let depth = 1;
        let close = -1;
        for (let index = open + 1; index < source.length; index += 1) {
          if (source[index] === '(') depth += 1;
          if (source[index] === ')') depth -= 1;
          if (depth === 0) {
            close = index;
            break;
          }
        }
        if (close < 0) break;
        result += source.slice(cursor, found.index) + render(source.slice(open + 1, close));
        cursor = close + 1;
        matcher.lastIndex = cursor;
      }
      return result + source.slice(cursor);
    };
    let normalized = replaceFunction(expression, 'sqrt', radicand => slash + 'sqrt{' + radicand + '}');
    normalized = replaceFunction(normalized, 'floor', argument => slash + 'left' + slash + 'lfloor ' + argument + slash + 'right' + slash + 'rfloor');
    normalized = normalized.replace(/\^\(([^()]*)\)/g, '^{$1}');
    normalized = normalized.replace(/\^-(\w+)/g, '^{-$1}');
    for (const [pattern, replacement] of mathCommands) {
      normalized = normalized.replace(pattern, replacement);
    }
    return slash + '(' + normalized + slash + ')';
  });
}

function renderPractice(questions) {
  return `<ol class="qa-practice">${questions.map(question => {
    const options = question.options.map(option => `<li>${option}</li>`).join('');
    const answer = question.options[question.answer];
    const level = question.level ? `<p class="qa-practice__level"><strong>${question.level}:</strong></p>` : '';
    return `<li>${level}<p>${question.prompt}</p><ol type="A">${options}</ol><details><summary>Show answer and solution</summary><p><strong>Answer: ${answer}</strong></p><p>${question.solution}</p></details></li>`;
  }).join('')}</ol>`;
}

function makeTopicData(topic, catalogTopic) {
  if (!Array.isArray(topic.questions) || topic.questions.length !== 5) {
    throw new Error('Exactly five worked practice questions are required for ' + topic.id + '.');
  }
  if (!Array.isArray(topic.prerequisites) || topic.prerequisites.length < 1
    || !Array.isArray(topic.coverage) || topic.coverage.length < 5) {
    throw new Error('Prerequisites and a detailed coverage checklist are required for ' + topic.id + '.');
  }
  const practiceLevels = topic.questions.map(question => question.level);
  if (practiceLevels.join('|') !== 'Core|Core|Foundation|Standard|Challenge') {
    throw new Error('Practice levels must progress from Core through Foundation, Standard and Challenge in ' + topic.id + '.');
  }
  for (const question of topic.questions) {
    if (!question.prompt || !question.solution || !Array.isArray(question.options)
      || question.options.length !== 4 || question.answer < 0 || question.answer >= question.options.length) {
      throw new Error('Invalid answer key in ' + topic.id + '.');
    }
  }

  return {
    schemaVersion: 1,
    generatedBy: GENERATOR_ID,
    id: topic.id,
    title: catalogTopic.title,
    description: `Comprehensive shared preparation notes and worked practice for ${catalogTopic.title}. Review the target examination syllabus and level before reuse.`,
    source: { type: 'sjmaths-authored-shared-content', examId: null },
    learningMap: {
      prerequisites: topic.prerequisites,
      coverage: topic.coverage,
      practiceLevels: ['Core', 'Foundation', 'Standard', 'Challenge'],
    },
    sections: [
      { id: 'theory', label: 'Concepts and worked examples', format: 'html-fragment', reusePolicy: 'same-syllabus-review', html: formatMathFragment(topic.theory) },
      { id: 'tricks', label: 'Methods and exam checks', format: 'html-fragment', reusePolicy: 'same-syllabus-review', html: formatMathFragment(topic.tricks) },
      { id: 'notes', label: 'Key facts and formulas', format: 'html-fragment', reusePolicy: 'same-syllabus-review', html: formatMathFragment(topic.notes) },
      { id: 'practice', label: 'Worked practice', format: 'html-fragment', reusePolicy: 'same-syllabus-review', html: formatMathFragment(renderPractice(topic.questions)) },
    ],
    reviewFlags: [],
  };
}

const catalog = JSON.parse(fs.readFileSync(CATALOG_PATH, 'utf8'));
assertCatalog(catalog);
const catalogTopics = catalog.groups.flatMap(group => group.topics);
const catalogById = new Map(catalogTopics.map(topic => [topic.id, topic]));
const lessonIds = new Set();
const outputs = [];
const unusedExpansions = Object.keys(lessonExpansions).filter(id => !lessons.some(lesson => lesson.id === id));
if (unusedExpansions.length) throw new Error('Unused lesson expansions: ' + unusedExpansions.join(', '));

for (const lesson of lessons) {
  if (lessonIds.has(lesson.id)) throw new Error(`Duplicate authored lesson id: ${lesson.id}`);
  lessonIds.add(lesson.id);
  const expansion = lessonExpansions[lesson.id];
  if (!expansion) throw new Error(`Comprehensive content is missing for ${lesson.id}.`);
  const catalogTopic = catalogById.get(lesson.id);
  if (!catalogTopic) throw new Error(`Lesson is missing from catalog: ${lesson.id}`);
  const filePath = path.join(DATA_ROOT, `${lesson.id}.json`);
  const expandedLesson = {
    ...lesson,
    ...expansion,
    questions: [
      ...lesson.questions.map(question => ({ ...question, level: 'Core' })),
      ...expansion.questions,
    ],
  };
  const data = makeTopicData(expandedLesson, catalogTopic);
  if (fs.existsSync(filePath)) {
    const current = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    if (current.generatedBy !== GENERATOR_ID) {
      throw new Error(`Refusing to overwrite existing topic file: ${path.relative(ROOT, filePath)}`);
    }
  }
  outputs.push({ filePath, contents: `${JSON.stringify(data, null, 2)}\n` });
}

const missing = catalogTopics.filter(topic => !fs.existsSync(path.join(DATA_ROOT, `${topic.id}.json`)) && !lessonIds.has(topic.id));
if (missing.length) throw new Error(`Missing lesson content for: ${missing.map(topic => topic.id).join(', ')}`);

if (writeEnabled) {
  for (const output of outputs) fs.writeFileSync(output.filePath, output.contents, 'utf8');
  for (const topic of catalogTopics) {
    topic.contentStatus = 'shared-content';
    topic.dataFile = `${topic.id}.json`;
  }
  fs.writeFileSync(CATALOG_PATH, `${JSON.stringify(catalog, null, 2)}\n`, 'utf8');
}

console.log(JSON.stringify({
  mode: writeEnabled ? 'write' : 'dry-run',
  curatedTopics: lessons.length,
  filesToWrite: outputs.length,
  catalogTopics: catalogTopics.length,
}, null, 2));
