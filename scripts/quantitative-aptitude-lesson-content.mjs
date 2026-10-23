const html = chunks => chunks.join('');

export const lessonExpansions = {
  'number-system-and-properties': {
    prerequisites: ['Whole-number operations', 'Basic fractions and powers'],
    coverage: ['Natural, whole, integer, rational, irrational and real numbers', 'Closure and ordering', 'Parity and signs', 'Prime and composite numbers', 'Decimal forms', 'Prime factorisation and perfect powers', 'Properties of operations'],
    theory: html([
      "<h3>Learning route</h3><p>Classify a number first, then use its properties to simplify a problem. The real number system contains rational and irrational numbers. Natural numbers are counting numbers; questions may specify whether zero is included. Whole numbers include zero; integers include negative whole numbers. A rational number is a quotient of integers with a nonzero denominator. Irrational numbers cannot be written as such a quotient.</p>",
      "<h3>Representation and structure</h3><p>Rational decimals terminate or eventually repeat: (0.375=3/8) and (0.2727...=3/11). An irrational decimal neither terminates nor repeats. The square root of a nonnegative integer is rational exactly when the integer is a perfect square: (sqrt{49}=7), while (sqrt{3}) is irrational. Do not assume that every expression containing an irrational number is irrational: (sqrt{2} times sqrt{2}=2).</p>",
      "<p>Integers are closed under addition, subtraction and multiplication, but not division; (1/2) is not an integer. Rational numbers are closed under the four operations when division by zero is excluded. Real numbers are ordered on a number line, and infinitely many real numbers lie between any two distinct real numbers.</p>",
      "<h3>Parity, signs and factorisation</h3><p>An even integer is divisible by 2; an odd integer leaves remainder 1 on division by 2. Even plus even and odd plus odd are even; even plus odd is odd. A product is even if at least one integer factor is even. Every integer greater than 1 has a unique prime factorisation, apart from factor order. One is neither prime nor composite.</p>",
      "<p><strong>Worked example:</strong> For odd (n), write (n=2k+1). Then (n(n+1)=(2k+1)(2k+2)=2(2k+1)(k+1)), so consecutive integers have an even product.</p>"
    ]),
    tricks: html([
      "<h3>Choose a property before calculating</h3><ul><li>Use parity when only evenness or oddness is asked; full multiplication is unnecessary.</li><li>For a square-root classification, simplify the radicand to a perfect square times a square-free factor.</li><li>For a claim about every integer, use a symbolic form such as (n=2k) or (n=2k+1); examples alone do not prove a rule.</li><li>Check denominator restrictions before cancelling or dividing.</li></ul>",
      "<h3>Frequent traps</h3><ul><li>Zero is even and an integer, but is not a positive natural number.</li><li>A prime has exactly two positive divisors; 1 has only one.</li><li>A rational plus an irrational is irrational, but two irrational numbers can have a rational sum.</li><li>Do not use real-number rules for square roots of negative values unless complex numbers are in scope.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Number sets: N is contained in Z, Z in Q, and Q in R; irrationals are R excluding Q.</li><li>Even: (2k). Odd: (2k+1), for integer k.</li><li>Prime factorisation: (N=p_1^{a_1}p_2^{a_2}...).</li><li>For nonzero a, (a^0=1); division by zero is undefined.</li><li>Rational decimal: terminating or recurring. Irrational decimal: nonterminating and nonrecurring.</li><li>Prove universal statements or disprove them with a valid counterexample.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "For every integer (n), which product is always even?", options: ["(n(n+1))", "(n^2+1)", "(2n+1)", "(n^2+n+1)"], answer: 0, solution: "One of two consecutive integers is even, so their product (n(n+1)) is even." },
      { level: 'Standard', prompt: "Which expression is rational?", options: ["(sqrt{2})", "(sqrt{18}/sqrt{2})", "(pi)", "(sqrt{5}+1)"], answer: 1, solution: "(sqrt{18}/sqrt{2}=sqrt{9}=3), which is rational. The other expressions are irrational." },
      { level: 'Challenge', prompt: "If a is rational and b is irrational, which statement must be true?", options: ["(a+b) is irrational", "(ab) is irrational for every a", "(a/b) is rational", "(b-a) is rational"], answer: 0, solution: "A rational plus an irrational is irrational. The product claim fails for a=0; the quotient and difference are not generally rational." }
    ]
  },
  'place-value-and-order-of-numbers': {
    prerequisites: ['Decimal notation', 'Addition and subtraction'],
    coverage: ['Base-ten place values', 'Expanded and standard form', 'Ordering signed numbers', 'Decimal comparison', 'Rounding', 'Significant figures', 'Error bounds'],
    theory: html([
      "<h3>Place value</h3><p>In base ten, each position is ten times the position to its right. In (6,704.308), the 7 represents (7,000), the 3 represents (3/10), and the 8 represents (8/1,000). Expanded form is (6,704.308=6,000+700+4+0.3+0.008). Zero can hold a place even when it contributes no value.</p>",
      "<h3>Compare and order</h3><p>On a number line, values increase from left to right. For negative values, the one closer to zero is greater: (-3>-8). To compare decimals, align decimal points and append trailing zeroes if useful; (0.600>0.598). Leading zeroes do not change magnitude, and trailing zeroes after a decimal do not change value.</p>",
      "<h3>Rounding and significant figures</h3><p>To round to a place, inspect the digit immediately to its right: 0–4 leaves the retained digit unchanged; 5–9 increases it by one. Significant figures begin at the first nonzero digit. In (0.004786), the first two significant figures are 4 and 7, so the value to two significant figures is (0.0048). Rounding to unit u gives an error no greater than half a unit, subject to the tie convention.</p>",
      "<p><strong>Worked example:</strong> To the nearest hundred, (18,749) becomes (18,700), since the tens digit is 4. To two significant figures it becomes (19,000), since the third significant digit is 7.</p>"
    ]),
    tricks: html([
      "<ul><li>Pad the shorter decimal on the right; never compare decimal digit counts alone.</li><li>For negative values, compare magnitudes and reverse the order.</li><li>Mark the requested place, then inspect exactly one digit to its right.</li><li>Use scientific notation to compare very large or small values.</li><li>State the requested precision; “round 2,347” is incomplete without a place or significant-figure count.</li></ul>",
      "<h3>Common errors</h3><ul><li>Appending zeroes to a whole number changes its value; appending decimal zeroes does not.</li><li>Rounding an intermediate value repeatedly can accumulate error.</li><li>At an exact halfway value, follow the rounding convention specified by the question.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Place values: (...,10^3,10^2,10^1,10^0,10^-1,10^-2,...).</li><li>Nearest unit u: absolute rounding error is at most (u/2).</li><li>Significant figures start at the first nonzero digit.</li><li>Check that the rounded value is close to the original and has the requested precision.</li><li>Keep extra digits during intermediate calculations and round at the end.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "What is the value of the digit 6 in (48,623.5)?", options: ["(6)", "(60)", "(600)", "(6,000)"], answer: 2, solution: "The 6 is in the hundreds place, so its value is (600)." },
      { level: 'Standard', prompt: "Round (0.004786) to two significant figures.", options: ["(0.0047)", "(0.0048)", "(0.00479)", "(0.0050)"], answer: 1, solution: "The first two significant digits are 4 and 7; the next digit is 8, so round 7 up: (0.0048)." },
      { level: 'Challenge', prompt: "Which interval contains the positive values that round to (3.7) to the nearest tenth under the usual half-up rule?", options: ["([3.65,3.75))", "([3.7,3.8))", "((3.65,3.75])", "([3.6,3.8))"], answer: 0, solution: "The midpoint boundaries are 3.65 and 3.75. The lower tie rounds up to 3.7, while 3.75 rounds to 3.8; therefore the interval is ([3.65,3.75))." }
    ]
  },
  'factors-multiples-and-prime-numbers': {
    prerequisites: ['Multiplication facts', 'Division with remainder'],
    coverage: ['Factors and multiples', 'Prime and composite classification', 'Prime factorisation', 'Factor pairs', 'Divisor count', 'Perfect squares and cubes', 'GCF and LCM'],
    theory: html([
      "<h3>Factors, multiples and primes</h3><p>A positive integer d is a factor of n when n/d is an integer; n is then a multiple of d. Factors occur in pairs: for 36, the pairs are (1,36), (2,18), (3,12), (4,9), and (6,6). A prime greater than 1 has exactly two positive factors; a composite number has more than two. One is neither.</p>",
      "<h3>Prime factorisation and divisor count</h3><p>Write a number as a product of prime powers. If (N=p^a q^b r^c), each divisor chooses an exponent from 0 through the corresponding exponent, so the divisor count is ((a+1)(b+1)(c+1)). The greatest common factor uses the smaller exponent of each common prime; the least common multiple uses the larger exponent of every prime present.</p>",
      "<p><strong>Worked example:</strong> (360=2^3 times 3^2 times 5) has ((3+1)(2+1)(1+1)=24) positive divisors. For 36 and 60, the GCF is (2^2 times 3=12), while the LCM is (2^2 times 3^2 times 5=180).</p>",
      "<h3>Perfect powers</h3><p>A prime factorisation is a perfect square when every exponent is even, and a perfect cube when every exponent is divisible by 3. To make a number a square by multiplication, supply the missing prime factors needed to make all exponents even.</p>"
    ]),
    tricks: html([
      "<ul><li>To test n for primality, test prime divisors only up to the square root of n.</li><li>For divisor counts, factor first instead of listing divisors.</li><li>Compare prime exponents in columns for GCF and LCM.</li><li>For the smallest multiplier making a square or cube, balance exponent remainders.</li><li>For two positive integers, verify GCF times LCM equals their product.</li></ul>",
      "<h3>Common errors</h3><ul><li>Do not count 1 as prime or composite.</li><li>An LCM includes primes occurring in either number, not only their common primes.</li><li>A perfect square has an odd divisor count because its square-root factor pairs with itself.</li></ul>"
    ]),
    notes: html([
      "<ul><li>If (N=p_1^{a_1}p_2^{a_2}...), then (d(N)=\\prod_i(a_i+1)).</li><li>GCF: minimum common exponents. LCM: maximum exponents.</li><li>Coprime positive integers have GCF 1 and LCM equal to their product.</li><li>Square: all prime exponents even. Cube: all exponents multiples of 3.</li><li>Trial division through the square root of n is enough to test primality.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Find the greatest common factor of (36) and (48).", options: ["(6)", "(8)", "(12)", "(16)"], answer: 2, solution: "The common prime factors with minimum exponents are (2^2 times 3=12)." },
      { level: 'Standard', prompt: "How many positive divisors does (2^4 times 3^2) have?", options: ["(8)", "(12)", "(15)", "(18)"], answer: 2, solution: "Apply the divisor formula: ((4+1)(2+1)=5 times 3=15)." },
      { level: 'Challenge', prompt: "What is the least positive integer that must multiply (180) to make a perfect square?", options: ["(2)", "(3)", "(5)", "(10)"], answer: 2, solution: "(180=2^2 times 3^2 times 5). Only the exponent of 5 is odd, so multiply by 5; (900=30^2)." }
    ]
  },
  'divisibility-and-remainders': {
    prerequisites: ['Place value', 'Division with remainder'],
    coverage: ['Division algorithm', 'Divisibility tests from 2 through 11', 'Modular addition and multiplication', 'Powers and residue cycles', 'Digit-sum methods', 'Standard remainder bounds'],
    theory: html([
      "<h3>Division algorithm</h3><p>For integer N and positive divisor d, there are unique integers q and r such that (N=dq+r) and (0 le r<d). Congruence (a equiv b pmod d) means a and b leave the same remainder on division by d.</p>",
      "<h3>Fast divisibility tests</h3><ul><li>2: last digit even; 5: last digit 0 or 5; 10: last digit 0.</li><li>3 and 9: digit sum divisible by 3 or 9.</li><li>4: final two digits divisible by 4; 8: final three digits divisible by 8.</li><li>6: divisible by both 2 and 3.</li><li>11: alternating sum of digits is divisible by 11, including zero.</li></ul>",
      "<p>The digit-sum tests work because powers of 10 have remainder 1 modulo 3 and 9. For 11, powers of 10 alternate between remainders 1 and -1.</p>",
      "<h3>Remainders of expressions</h3><p>Reduce terms before adding or multiplying. If a and b have remainders r and s modulo d, then their sum has remainder congruent to (r+s), and their product to (rs); reduce again to 0 through d-1. For powers, look for a repeating residue cycle.</p>",
      "<p><strong>Worked example:</strong> To find the remainder of (7^4) on division by 5, note that (7 equiv 2 pmod 5), so (7^4 equiv 2^4=16 equiv 1 pmod 5).</p>"
    ]),
    tricks: html([
      "<ul><li>For a large power, write a short residue cycle and reduce the exponent using its period.</li><li>For a large sum, reduce each addend before summing.</li><li>For a product, reduce factors first to keep numbers small.</li><li>For divisibility by a composite number, use its coprime factors when possible; for 12, test both 3 and 4.</li><li>Confirm each final remainder is nonnegative and smaller than the divisor.</li></ul>"
    ]),
    notes: html([
      "<ul><li>(N=dq+r), where (0 le r<d).</li><li>Remainders preserve addition, subtraction and multiplication.</li><li>Power remainders repeat periodically; the period may be shorter than the divisor.</li><li>For a negative intermediate remainder, add the divisor to return to the standard range.</li><li>For 11, use the alternating digit sum.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Which number is divisible by both 3 and 4?", options: ["(1,326)", "(1,332)", "(1,342)", "(1,352)"], answer: 1, solution: "For 1,332, the digit sum is 9, so it is divisible by 3; the last two digits, 32, are divisible by 4." },
      { level: 'Standard', prompt: "What is the remainder when (7^4) is divided by 5?", options: ["(0)", "(1)", "(2)", "(4)"], answer: 1, solution: "Modulo 5, 7 has remainder 2, and (2^4=16) leaves remainder 1." },
      { level: 'Challenge', prompt: "What is the remainder when (123,456) is divided by 11?", options: ["(0)", "(1)", "(2)", "(3)"], answer: 3, solution: "The alternating digit sum is (6-5+4-3+2-1=3), so the remainder modulo 11 is 3." }
    ]
  },
  'simplification-and-bodmas': {
    prerequisites: ['Four operations with integers and fractions', 'Powers and roots'],
    coverage: ['Nested grouping symbols', 'Order of operations', 'Left-to-right evaluation at equal priority', 'Fractions and signed numbers', 'Powers and roots', 'Implied multiplication', 'Estimation checks'],
    theory: html([
      "<h3>Order of operations</h3><p>Evaluate grouping symbols from the innermost outward; then powers and roots; then multiplication and division from left to right; finally addition and subtraction from left to right. Multiplication and division have equal priority, as do addition and subtraction. BODMAS is a memory aid, not permission to perform every division before multiplication.</p>",
      "<p>For example, (18-6 div 3 times 2) is evaluated as (18-2 times 2=14). With fractions, the fraction bar groups its entire numerator and denominator before the division is carried out.</p>",
      "<h3>Signs and grouping</h3><p>A negative sign before brackets changes every term when the brackets are removed: (-(a-b+c)=-a+b-c). Exponents apply before a leading negative unless that negative is inside parentheses: (-3^2=-9), while ((-3)^2=9). Implied multiplication, such as (2x), is multiplication; preserve its place in the order.</p>",
      "<p><strong>Worked example:</strong> For (5+2(7-3)^2 div 4), the bracket is 4, its square is 16, multiplication and division left to right give 8, and the answer is 13.</p>"
    ]),
    tricks: html([
      "<ul><li>Rewrite a dense expression with explicit brackets around a numerator and denominator.</li><li>For chained multiplication and division, move left to right; do the same for addition and subtraction.</li><li>Estimate the sign and size before calculating exactly.</li><li>Distribute a minus sign to every term in a bracket.</li><li>Substitute the result back into an equivalent expression when possible.</li></ul>",
      "<h3>Frequent errors</h3><ul><li>Doing multiplication before an earlier division because of the order of letters in a mnemonic.</li><li>Squaring only the first term instead of the entire bracket.</li><li>Dropping a negative sign while removing parentheses.</li><li>Changing the grouping of a fraction without a fraction bar or brackets.</li></ul>"
    ]),
    notes: html([
      "<ol><li>Grouping symbols.</li><li>Powers and roots.</li><li>Multiplication/division, left to right.</li><li>Addition/subtraction, left to right.</li></ol><ul><li>((-a)^2=a^2), but (-a^2)=-(a^2).</li><li>Division by zero is undefined.</li><li>Use parentheses to make the intended order unambiguous.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Evaluate (24 div 6 times 2).", options: ["(2)", "(8)", "(12)", "(16)"], answer: 1, solution: "Division and multiplication have equal priority: (24 div 6=4), then (4 times 2=8)." },
      { level: 'Standard', prompt: "Evaluate (20-3(2+1)^2).", options: ["(-7)", "(7)", "(11)", "(47)"], answer: 0, solution: "The bracket is 3, its square is 9, and (3 times 9=27). Then (20-27=-7)." },
      { level: 'Challenge', prompt: "Evaluate ((-3)^2-(-3^2)).", options: ["(0)", "(9)", "(18)", "(-18)"], answer: 2, solution: "((-3)^2=9). In (-3^2), the exponent applies before the leading negative, so its value is -9. Thus (9-(-9)=18)." }
    ]
  },
  'approximation-and-estimation': {
    prerequisites: ['Place value and rounding', 'Four operations'],
    coverage: ['Rounding to place value', 'Significant figures', 'Compatible-number estimates', 'Bounds and error', 'Order of magnitude', 'Approximation in arithmetic'],
    theory: html([
      "<h3>Estimate and exact value</h3><p>Estimation replaces difficult values with nearby convenient numbers to predict a result or check whether an exact answer is reasonable. Rounding has a stated precision; an estimate is usually not exact. For products, choose rounded factors that are easy to multiply; for division, use compatible numerator and denominator values.</p>",
      "<h3>Bounds and error</h3><p>If a positive value rounds to a to the nearest unit u, the original value is within half a unit of a, subject to the tie convention. Absolute error is the magnitude of the difference from the exact value. Relative error compares that error with the exact value. Keeping more significant figures generally gives a tighter approximation.</p>",
      "<p><strong>Worked example:</strong> (49.8 times 20.2) is close to (50 times 20=1,000). The exact result is 1,005.96, so the estimate has the right scale and is a useful check.</p>",
      "<h3>Choosing precision</h3><p>Keep guard digits while calculating and round only the final result unless the question says otherwise. If options are far apart, a rough estimate may eliminate choices. If options are close, use exact arithmetic or bounds rather than rounding too early.</p>"
    ]),
    tricks: html([
      "<ul><li>Round one factor up and another down when that balances a product estimate.</li><li>For a percentage, estimate the base value first; 10% is one tenth.</li><li>Use the first nonzero digit to compare orders of magnitude.</li><li>When a choice is near a rounding boundary, calculate exactly or bound it.</li><li>Keep units and precision consistent in measurement and money problems.</li></ul>",
      "<h3>Common traps</h3><ul><li>Repeatedly rounding intermediate results can accumulate error.</li><li>More decimal places do not mean more accuracy when input measurements are approximate.</li><li>Use an approximation symbol or words such as about; do not present an estimate as exact.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Nearest unit u: rounding error is at most u/2.</li><li>Significant figures start at the first nonzero digit.</li><li>Estimate first, but compute exactly when the question or close options require it.</li><li>Check sign, units and order of magnitude.</li><li>Round intermediate values only when explicitly instructed.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Round (6,847) to the nearest hundred.", options: ["(6,800)", "(6,840)", "(6,850)", "(6,900)"], answer: 0, solution: "The tens digit is 4, so the hundreds digit stays unchanged: 6,847 rounds to 6,800." },
      { level: 'Standard', prompt: "Which is the best estimate of (19.8 times 0.49)?", options: ["(1)", "(10)", "(100)", "(1,000)"], answer: 1, solution: "Use (20 times 0.5=10). The exact product is close to 10." },
      { level: 'Challenge', prompt: "Which value rounds to (8.4 cm) to the nearest tenth under the usual half-up rule?", options: ["(8.34 cm)", "(8.41 cm)", "(8.46 cm)", "(8.51 cm)"], answer: 1, solution: "Values from 8.35 cm up to but not including 8.45 cm round to 8.4 cm. Only 8.41 cm is in that interval." }
    ]
  },
  'unit-digit-and-cyclicity': {
    prerequisites: ['Powers and exponents', 'Division with remainder'],
    coverage: ['Last-digit cycles for digits 0–9', 'Cycle length and exponent remainder', 'Zero exponents', 'Remainder-zero case', 'Modular powers', 'Products of large powers'],
    theory: html([
      "<h3>Find the repeating cycle</h3><p>Only the last digit of a base affects the last digit of its positive integer powers. Powers of 0, 1, 5 and 6 have constant last digits. The cycles for 2 and 8, and for 3 and 7, usually have length 4; 4 and 9 have length 2. A cycle can shorten in special cases.</p>",
      "<p>Reduce the exponent modulo the cycle length. A nonzero remainder selects that position in the cycle. A remainder of zero selects the final position, not the first. For powers of 7, the cycle is (7,9,3,1); because 20 is a multiple of 4, the unit digit of (7^20) is 1.</p>",
      "<h3>Products and special exponents</h3><p>For a product, find each factor's unit digit, multiply those digits, and keep only the final digit. For a nonzero base, an exponent of zero gives 1. A unit digit is not defined in the ordinary integer sense for a negative exponent.</p>",
      "<p><strong>Worked example:</strong> The cycle for 3 is (3,9,7,1). Since (58 mod 4=2), the unit digit of (3^58) is the second entry, 9.</p>"
    ]),
    tricks: html([
      "<ul><li>Write the short cycle before reducing the exponent.</li><li>For cycle length 4, exponents divisible by 4 use entry 4.</li><li>For a product of powers, reduce each factor separately before multiplying.</li><li>Check whether the exponent is zero; do not apply positive-power cycle rules blindly.</li><li>Bases ending in 0, 1, 5 or 6 need no cycle calculation.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Cycles: 2 gives (2,4,8,6); 3 gives (3,9,7,1); 7 gives (7,9,3,1); 8 gives (8,4,2,6).</li><li>4 gives (4,6); 9 gives (9,1).</li><li>Last digits 0, 1, 5 and 6 remain fixed for positive powers.</li><li>If n mod k is 0, choose the kth item of a cycle of length k.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "What is the unit digit of (2^103)?", options: ["(2)", "(4)", "(6)", "(8)"], answer: 3, solution: "The cycle for 2 is (2,4,8,6). Since (103 mod 4=3), use the third entry: 8, which is choice D." },
      { level: 'Standard', prompt: "What is the unit digit of (9^64)?", options: ["(1)", "(3)", "(7)", "(9)"], answer: 0, solution: "The cycle for 9 is (9,1). An even exponent gives the second entry, 1." },
      { level: 'Challenge', prompt: "What is the unit digit of (7^8 times 3^5)?", options: ["(1)", "(3)", "(7)", "(9)"], answer: 1, solution: "The unit digit of 7^8 is 1 because the exponent selects cycle entry 4. The unit digit of 3^5 is 3. Their product has unit digit 3." }
    ]
  },
  'factorials-and-trailing-zeroes': {
    prerequisites: ['Prime factorisation', 'Powers of 10'],
    coverage: ['Factorial notation', 'Prime exponents in n!', 'Trailing zeroes in factorials', 'Trailing zeroes in products', 'Repeated factors of 5', 'Factorial divisibility'],
    theory: html([
      "<h3>Factorials and prime exponents</h3><p>(n!) is the product of the positive integers from 1 through n. To count how many times a prime p divides n!, count multiples of p, then add extra counts for multiples of p^2, p^3, and higher powers: \\(\\left\\lfloor n/p\\right\\rfloor+\\left\\lfloor n/p^2\\right\\rfloor+...\\). A multiple of p^2 contributes two factors of p.</p>",
      "<h3>Trailing zeroes</h3><p>Each trailing zero needs one factor of 10, which consists of a factor of 2 and a factor of 5. In a factorial, factors of 2 are more abundant, so count factors of 5 and stop when the quotient is zero.</p>",
      "<p><strong>Worked example:</strong> In (100!), the number of factors of 5 is \\(\\left\\lfloor 100/5\\right\\rfloor+\\left\\lfloor 100/25\\right\\rfloor=20+4=24\\), so it ends in 24 zeroes.</p>",
      "<h3>Other products and factorial quotients</h3><p>For a general product, factor each number and pair one 2 with one 5 per trailing zero. For a factorial quotient, subtract prime exponents only after confirming that the quotient is an integer and all terms are defined.</p>"
    ]),
    tricks: html([
      "<ul><li>Count multiples of 5 first, then add extra counts for 25, 125 and higher powers.</li><li>Use repeated division by 5; do not round the quotients.</li><li>For a general product, the zero count is the smaller of its total number of factors 2 and factors 5.</li><li>For divisibility, compare prime exponents instead of expanding factorials.</li><li>Check the scale: n! has fewer than n trailing zeroes for positive n.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Exponent of p in n!: \\(\\sum_{j\\ge1}\\left\\lfloor n/p^j\\right\\rfloor\\).</li><li>Trailing zeroes in n!: \\(\\sum_{j\\ge1}\\left\\lfloor n/5^j\\right\\rfloor\\).</li><li>For a product with a factors of 2 and b factors of 5, zero count is \\(\\min(a,b)\\).</li><li>Factorials grow quickly; expansion is unnecessary for these counts.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "How many trailing zeroes are in (200!)?", options: ["(40)", "(48)", "(49)", "(50)"], answer: 2, solution: "Count factors of 5: (floor(200/5)+floor(200/25)+floor(200/125)=40+8+1=49)." },
      { level: 'Standard', prompt: "What is the greatest exponent e such that (5^e) divides (24!)?", options: ["(4)", "(5)", "(6)", "(8)"], answer: 0, solution: "The exponent is (floor(24/5)+floor(24/25)=4+0=4)." },
      { level: 'Challenge', prompt: "How many trailing zeroes are in the product (25 times 16 times 40)?", options: ["(1)", "(2)", "(3)", "(4)"], answer: 2, solution: "There are 7 factors of 2 and 3 factors of 5, so the product has min(7,3)=3 trailing zeroes." }
    ]
  },
  'number-base-systems': {
    prerequisites: ['Place value', 'Repeated division'],
    coverage: ['Positional notation in base b', 'Valid digits and base constraints', 'Conversion to decimal', 'Conversion from decimal', 'Binary, octal and hexadecimal', 'Grouping conversions', 'Arithmetic in another base'],
    theory: html([
      "<h3>Positional notation</h3><p>In base b, allowed digits are 0 through b-1 and place values are powers of b. Thus (d_k...d_1d_0)_b represents (d_k b^k+...+d_1 b+d_0). A digit equal to or larger than the base is invalid. The subscript identifies the base.</p>",
      "<h3>Convert to and from base ten</h3><p>To convert to decimal, expand by place values. To convert a positive decimal integer to base b, repeatedly divide by b, record remainders, and read them upward from the last remainder. For a fractional part, repeatedly multiply by the new base and read the integer parts in order.</p>",
      "<p>Binary uses 0 and 1; octal uses 0–7; hexadecimal uses 0–9 and A–F, where A is 10 through F is 15. Binary-to-octal groups bits in threes; binary-to-hexadecimal groups in fours, starting at the radix point and padding with zeroes at the outside edge if needed.</p>",
      "<p><strong>Worked example:</strong> (101101_2=1 times 32+0 times 16+1 times 8+1 times 4+0 times 2+1=45).</p>",
      "<h3>Arithmetic in another base</h3><p>Add or multiply as in decimal, but carry when a column reaches the base. In base 2, (1+1=10_2); in base 8, (7+1=10_8).</p>"
    ]),
    tricks: html([
      "<ul><li>Write place-value powers below the digits before expanding.</li><li>Check a conversion by converting back or bounding it between adjacent powers.</li><li>Keep decimal-to-base remainders in reverse order until the end.</li><li>For binary-octal or binary-hex conversion, group outward from the radix point.</li><li>Validate every digit against the base before calculating.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Base-b numeral value: sum of digit times its place value b^i.</li><li>There are b digit symbols in base b, including zero.</li><li>Binary place values: (1,2,4,8,16,32,...).</li><li>Octal corresponds to groups of 3 binary bits; hexadecimal to groups of 4.</li><li>A k-digit numeral with nonzero first digit is at least b^(k-1) and less than b^k.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Convert (110101_2) to base ten.", options: ["(51)", "(52)", "(53)", "(54)"], answer: 2, solution: "Use place values: (32+16+4+1=53)." },
      { level: 'Standard', prompt: "Write (83) in base eight.", options: ["(113_8)", "(123_8)", "(133_8)", "(103_8)"], answer: 1, solution: "Repeated division by 8 gives remainders 3, 2, 1; read upward to get (123_8)." },
      { level: 'Challenge', prompt: "What is (132_4) in base ten?", options: ["(26)", "(28)", "(30)", "(34)"], answer: 2, solution: "Expand by powers of 4: (1 times 16+3 times 4+2=30)." }
    ]
  },
  'indices-and-exponents': {
    prerequisites: ['Multiplication', 'Fractions and roots'],
    coverage: ['Product and quotient laws', 'Power of a power and product', 'Zero and negative exponents', 'Rational exponents and radicals', 'Scientific notation', 'Domain restrictions and undefined forms'],
    theory: html([
      "<h3>Exponent laws</h3><p>For a nonzero base a, (a^m times a^n=a^(m+n)), (a^m/a^n=a^(m-n)), and ((a^m)^n=a^(mn)). A power distributes across multiplication: ((ab)^n=a^n b^n). It does not distribute across addition: ((a+b)^n) is not generally (a^n+b^n).</p>",
      "<h3>Zero, negative and fractional powers</h3><p>For nonzero a, (a^0=1) and (a^-n=1/a^n). A fractional exponent represents a root: (a^{1/n}=\\sqrt[n]{a}). For a real even root, the radicand must be nonnegative. Reduce a rational exponent and check the real-domain restriction. In ordinary school algebra, (0^0) is undefined.</p>",
      "<h3>Scientific notation</h3><p>Scientific notation writes a nonzero number as (a times 10^n), where (1 le |a|<10) and n is an integer. It helps compare magnitude and multiply or divide very large and small measurements.</p>",
      "<p><strong>Worked example:</strong> (16^{3/4}=(\\sqrt[4]{16})^3=2^3=8).</p>"
    ]),
    tricks: html([
      "<ul><li>Combine powers only when their bases match; combine bases only when exponent laws permit it.</li><li>Convert negative exponents to reciprocals before comparing magnitude.</li><li>For a rational exponent, evaluate an exact root first when possible.</li><li>Apply a power to every factor inside parentheses.</li><li>Keep the sign outside a power distinct from a negative base: (-3^2)=-9, while ((-3)^2=9).</li></ul>"
    ]),
    notes: html([
      "<ul><li>(a^m a^n=a^(m+n)); (a^m/a^n=a^(m-n)) for nonzero a.</li><li>((a^m)^n=a^(mn)); ((ab)^n=a^n b^n).</li><li>(a^-n=1/a^n); (a^0=1) for nonzero a.</li><li>(a^{m/n}=\\sqrt[n]{a^m}) when the real root exists.</li><li>Normalize scientific notation so (1 le |a|<10).</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Simplify (x^7/x^3), where x is nonzero.", options: ["(x^4)", "(x^10)", "(x^21)", "(1/x^4)"], answer: 0, solution: "Subtract exponents for the same nonzero base: (x^(7-3)=x^4)." },
      { level: 'Standard', prompt: "Evaluate (16^(3/4)).", options: ["(4)", "(8)", "(12)", "(16)"], answer: 1, solution: "The fourth root of 16 is 2, then (2^3=8)." },
      { level: 'Challenge', prompt: "Write (0.000072) in scientific notation.", options: ["(7.2 times 10^-5)", "(7.2 times 10^-4)", "(7.2 times 10^-6)", "(72 times 10^-5)"], answer: 0, solution: "Move the decimal five places right to get 7.2, so the power is -5: (7.2 times 10^-5)." }
    ]
  },
  'unitary-method': {
    prerequisites: ['Ratios and rates', 'Direct and inverse proportion'],
    coverage: ['Value per one unit', 'Direct proportion', 'Inverse proportion', 'Compound unitary method', 'Rates with units', 'Constant-rate assumptions'],
    theory: html([
      "<h3>One unit, then the required units</h3><p>The unitary method finds the value or rate for one unit and scales it to the required amount. If 8 metres cost ₹560, one metre costs ₹70 and 13 metres cost ₹910, provided the price per metre is constant. State the unit at every step so rupees per metre is not confused with metres per rupee.</p>",
      "<h3>Direct and inverse variation</h3><p>In direct proportion, the ratio of corresponding quantities is constant: doubling one doubles the other. In inverse proportion, their product is constant: doubling one halves the other. Work-and-time problems are inverse only when worker efficiency and conditions remain unchanged. For compound situations, change one quantity at a time and decide whether the relationship is direct or inverse.</p>",
      "<p><strong>Worked example:</strong> Eight workers finish a job in 15 days. At the same rate, 12 workers need (8 × 15/12=10) days. The total work is 120 worker-days.</p>"
    ]),
    tricks: html([
      "<ul><li>Write the one-unit rate with its units before scaling.</li><li>Ask whether more of the first quantity means more or less of the second before choosing direct or inverse proportion.</li><li>For several changing quantities, use a ratio table and label each relationship.</li><li>Check whether the problem justifies a constant rate.</li><li>Convert units before comparing rates such as metres per second and kilometres per hour.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Direct proportion: y/x is constant.</li><li>Inverse proportion: xy is constant.</li><li>Work = rate × time; for identical workers, worker-days can remain constant.</li><li>Unitary steps require an unchanged rate or proportional relationship.</li><li>Include requested units in the final answer.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Twelve books cost ₹540 at a constant price. What do 7 books cost?", options: ["₹280", "₹315", "₹350", "₹378"], answer: 1, solution: "One book costs (540/12=₹45). Seven cost (7 × ₹45=₹315)." },
      { level: 'Standard', prompt: "Eight workers complete a job in 15 days. How many days do 12 equally efficient workers need?", options: ["(8 days)", "(10 days)", "(12 days)", "(22.5 days)"], answer: 1, solution: "Work is constant: (8 × 15=120) worker-days. Time is (120/12=10) days." },
      { level: 'Challenge', prompt: "Three identical pumps fill a tank in 8 hours. How long would four pumps take under the same conditions?", options: ["(4 h)", "(6 h)", "(8 h)", "(10 h)"], answer: 1, solution: "Pump count and time are inversely proportional: (3 × 8=4t), so (t=6) hours." }
    ]
  },
  'problems-on-ages': {
    prerequisites: ['Linear equations', 'Ratios'],
    coverage: ['Present, past and future age expressions', 'Constant age differences', 'Changing age ratios', 'Sum and difference conditions', 'Multi-person age equations', 'Checking realistic ages'],
    theory: html([
      "<h3>Use one reference time</h3><p>Choose present ages as variables. If a person is x years old now, the age after t years is x+t and the age t years ago is x-t. The difference between two people's ages stays constant; their ratio changes with time.</p>",
      "<h3>Translate the relationships</h3><p>A is twice B means (A=2B), while A is 2 years older than B means (A=B+2). Keep the reference time explicit: five years ago A was twice B is (A-5=2(B-5)), not (A-5=2B). Solve the equations and verify every condition at its stated time.</p>",
      "<p><strong>Worked example:</strong> A and B total 40 now. Five years ago A was twice B: (A+B=40) and (A-5=2(B-5)). The solution is (A=25, B=15); five years ago they were 20 and 10.</p>"
    ]),
    tricks: html([
      "<ul><li>Make a present/past/future table before forming equations.</li><li>When ages shift by the same amount, shift each age before comparing ratios.</li><li>Use the constant age difference as a quick check.</li><li>For three people, define only independent ages and express the rest from sums or differences.</li><li>Reject solutions that imply an impossible negative age at the stated time.</li></ul>"
    ]),
    notes: html([
      "<ul><li>After t years: x+t. t years ago: x-t.</li><li>Age difference is invariant: (A+t)-(B+t)=A-B.</li><li>Age ratio is generally not invariant.</li><li>Substitute the solution into every original condition.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Two present ages sum to 39. In 5 years, their ages will be in the ratio (4:3). What are their present ages?", options: ["23 and 16", "24 and 15", "21 and 18", "25 and 14"], answer: 0, solution: "Their future sum is 49. With ratio 4:3, the future ages are 28 and 21; subtract 5 to get 23 and 16." },
      { level: 'Standard', prompt: "A father is three times his child's age now. Four years ago, he was five times the child's age. How old is the child now?", options: ["(6)", "(8)", "(10)", "(12)"], answer: 1, solution: "Let the child's age be c; the father is 3c. Four years ago: (3c-4=5(c-4)). Thus (16=2c), so c=8." },
      { level: 'Challenge', prompt: "A is 6 years older than B. Four years from now, their ages will sum to 42. What are their current ages?", options: ["17 and 11", "18 and 12", "19 and 13", "20 and 14"], answer: 3, solution: "Their present sum is (42-8=34). With difference 6, the ages are ((34+6)/2=20) and ((34-6)/2=14)." }
    ]
  },
  'data-based-arithmetic-word-problems': {
    prerequisites: ['Percentages and ratios', 'Averages', 'Unit conversion'],
    coverage: ['Extracting values from prose and tables', 'Choosing operations and equations', 'Unit conversion', 'Rates and totals', 'Percent change and discounts', 'Estimation and validation'],
    theory: html([
      "<h3>Translate the situation first</h3><p>Read once for context and again to identify the requested quantity. Record known values with units, distinguish totals from rates, and mark irrelevant information. Convert units before combining quantities. A short table can keep categories and time periods clear.</p>",
      "<h3>Build a calculation plan</h3><p>Add to combine amounts, subtract to find differences or remainders, multiply for equal groups, and divide for per-unit rates or equal sharing. Percent increase is based on the original value; a discount is subtracted from the marked price. For journeys at different speeds, average speed is total distance divided by total time; do not average speeds unless the time intervals are equal.</p>",
      "<p><strong>Worked example:</strong> A vehicle goes 240 km in 4 h and 90 km in 1.5 h. Total distance is 330 km and total time is 5.5 h, so average speed is (330/5.5=60) km/h.</p>",
      "<h3>Validate the result</h3><p>Estimate the answer, check units, and decide whether it should be larger or smaller than the starting value. Keep currency, percentages, quantities and rates distinct.</p>"
    ]),
    tricks: html([
      "<ul><li>Write given value → operation → unit beside each number.</li><li>For several steps, calculate intermediate totals in a short table.</li><li>Convert quantities to one unit before adding or comparing.</li><li>For average rates, divide total output by total corresponding input.</li><li>Check the answer with an estimate and with the story's direction.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Percent change = change/original × 100%.</li><li>Average rate = total measured output / total corresponding input.</li><li>Discounted price = marked price × (1-discount rate).</li><li>Write units at every step and cancel only when the operation justifies it.</li><li>Do not round intermediate values unless instructed.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "A family buys groceries for ₹1,240 and pays ₹60 for delivery. If it pays ₹1,500, how much change should it receive?", options: ["₹180", "₹200", "₹220", "₹260"], answer: 1, solution: "Total cost is (1,240+60=₹1,300). Change is (1,500-1,300=₹200)." },
      { level: 'Standard', prompt: "A 240 km trip takes 4 hours and a further 90 km takes 1.5 hours. What is the average speed for the whole trip?", options: ["(55 km/h)", "(60 km/h)", "(62 km/h)", "(65 km/h)"], answer: 1, solution: "Total distance is 330 km; total time is 5.5 h. Average speed is (330/5.5=60 km/h)." },
      { level: 'Challenge', prompt: "A shop buys 12 items at ₹80 each. It sells 9 at ₹100 each and the rest at ₹60 each. What is its total profit or loss?", options: ["₹60 profit", "₹60 loss", "₹120 profit", "₹120 loss"], answer: 2, solution: "Cost is (12 × 80=₹960). Revenue is (9 × 100+3 × 60=₹1,080), so profit is ₹120." }
    ]
  },
  'pipes-and-cisterns': {
    prerequisites: ['Fractions', 'Rate and time'],
    coverage: ['Inlet and outlet rates', 'Combined pipes', 'Leaks and drains', 'Net filling or emptying', 'Partial filling', 'Consistent rate assumptions'],
    theory: html([
      "<h3>Convert completion time into a rate</h3><p>If a pipe fills a tank in a hours, its rate is 1/a tank per hour. An outlet that empties it in b hours has rate -1/b. Add signed rates while pipes operate together. A positive net rate fills the tank; a negative rate empties it.</p>",
      "<p>For several pipes, use a common time unit and add their rates. If the tank is partly filled, calculate the remaining fraction before dividing by the net rate. These methods assume constant rates and unchanged capacity.</p>",
      "<p><strong>Worked example:</strong> Pipes that fill a tank in 6 h and 12 h have combined rate (1/6+1/12=1/4) tank per hour, so they fill it in 4 h. A 9 h leak changes the net rate to (1/4-1/9=5/36) tank per hour.</p>"
    ]),
    tricks: html([
      "<ul><li>Choose one tank as one work unit and write each rate as tanks per hour.</li><li>Use plus for inlets and minus for outlets or leaks.</li><li>Find the net rate before calculating time.</li><li>For alternating operation, calculate work during each interval and update the remaining fraction.</li><li>Check that the net rate has the correct sign and the time is plausible.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Filling rate from time t: 1/t tank per unit time.</li><li>Net rate = sum of inlet rates minus sum of outlet rates.</li><li>Time = remaining work / positive net rate.</li><li>Zero net rate means the water level is unchanged.</li><li>Convert all rates to the same time unit before adding.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Two pipes fill a tank in 6 hours and 12 hours. How long do they take together?", options: ["(3 h)", "(4 h)", "(6 h)", "(9 h)"], answer: 1, solution: "Combined rate is (1/6+1/12=1/4) tank per hour, so the tank fills in 4 hours." },
      { level: 'Standard', prompt: "A pipe fills a tank in 6 hours and a leak empties it in 9 hours. If both stay open, how long does an empty tank take to fill?", options: ["(12 h)", "(15 h)", "(18 h)", "(54 h)"], answer: 2, solution: "Net rate is (1/6-1/9=1/18) tank per hour, so filling takes 18 hours." },
      { level: 'Challenge', prompt: "A tank is one-third full. An inlet fills it in 4 hours and an outlet empties it in 12 hours. How long until it is full with both open?", options: ["(2 h)", "(3 h)", "(4 h)", "(6 h)"], answer: 2, solution: "Remaining work is 2/3 tank. Net rate is (1/4-1/12=1/6) tank per hour, so time is ((2/3)/(1/6)=4) hours." }
    ]
  },
  'work-and-wages': {
    prerequisites: ['Fractions', 'Ratios', 'Time and work'],
    coverage: ['Work as rate × time', 'Individual and combined efficiencies', 'Wage shares by contribution', 'Different worker rates', 'Partial work', 'Equal-condition assumptions'],
    theory: html([
      "<h3>Work, rate and time</h3><p>Represent a completed job as one unit. If a worker completes it in a days, the daily rate is 1/a. Add rates for people working together. If output is given in units per day, contribution is rate × days. A person's wage share is proportional to work actually completed, not automatically to the number of workers or days.</p>",
      "<h3>Sharing wages</h3><p>For equal work conditions, compare contributions (rate × time). If A and B produce work in ratio m:n, divide total wages in that ratio. With different rates, compute each contribution first. Account for absences or unequal hours explicitly.</p>",
      "<p><strong>Worked example:</strong> A completes a job in 12 days and B in 18 days. Their daily rates are 1/12 and 1/18, so their rate ratio is 3:2. For equal working time, a ₹1,500 wage pool is shared as ₹900 and ₹600.</p>"
    ]),
    tricks: html([
      "<ul><li>Use total work = 1 when only completion times are known; use actual units when output rates are provided.</li><li>For wages, compute each contribution, then divide the wage pool by the contribution ratio.</li><li>Equal-rate workers: work is proportional to time. Equal-time workers: work is proportional to rate.</li><li>Check that wage shares add to the total.</li><li>Keep the job and time unit consistent across workers.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Work = rate × time.</li><li>Combined rate is the sum of individual rates for simultaneous work.</li><li>Wage share = total wages × (individual work / total work).</li><li>Equal-rate workers: contribution ratio equals time ratio.</li><li>Equal-time workers: contribution ratio equals rate ratio.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "A and B work at the same rate. A works 4 days and B works 6 days. They share ₹1,500 in proportion to work. What is A's share?", options: ["₹500", "₹600", "₹750", "₹900"], answer: 1, solution: "Their work ratio is (4:6=2:3). A receives (2/5 × 1,500=₹600)." },
      { level: 'Standard', prompt: "A completes a job in 12 days and B in 18 days. How long do they take together?", options: ["(6 days)", "(7.2 days)", "(9 days)", "(15 days)"], answer: 1, solution: "Combined rate is (1/12+1/18=5/36) job per day. Time is (36/5=7.2) days." },
      { level: 'Challenge', prompt: "A produces 12 units per day for 5 days; B produces 8 units per day for 6 days. They divide ₹1,080 according to work. What is A's share?", options: ["₹540", "₹600", "₹720", "₹800"], answer: 1, solution: "A produces 60 units; B produces 48. A's fraction is (60/108=5/9), so A receives (5/9 × 1,080=₹600)." }
    ]
  },
  'problems-on-trains': {
    prerequisites: ['Time-speed-distance', 'Unit conversion'],
    coverage: ['Passing a pole or person', 'Passing a platform or bridge', 'Two trains crossing', 'Same- and opposite-direction relative speed', 'Kilometres per hour to metres per second', 'Train lengths and elapsed time'],
    theory: html([
      "<h3>Distance needed to clear an object</h3><p>To pass a stationary pole, a train covers its own length. To pass a platform or bridge, it covers train length plus platform length. Two trains crossing completely cover the sum of their lengths.</p>",
      "<h3>Relative speed</h3><p>For opposite directions, relative speed is the sum of speeds; for the same direction, it is the absolute difference. Divide the required crossing distance by relative speed. Convert speeds to metres per second when lengths are in metres: 1 km/h = 5/18 m/s. A moving person is treated as another moving object.</p>",
      "<p><strong>Worked example:</strong> A 150 m train at 72 km/h passes a 250 m platform. Speed is (72 × 5/18=20) m/s; distance is 400 m; time is (400/20=20) seconds.</p>"
    ]),
    tricks: html([
      "<ul><li>Draw the train and mark how far its front travels before its rear clears the object.</li><li>Use sum for opposite directions and difference for the same direction.</li><li>Convert every speed to a common unit before division.</li><li>For a pole or signal, do not add a platform length.</li><li>Check that the result is a time.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Pole: time = train length / relative speed.</li><li>Platform: time = (train length + platform length) / train speed.</li><li>Two trains: crossing distance = sum of lengths; use relative speed.</li><li>km/h to m/s: multiply by 5/18. m/s to km/h: multiply by 18/5.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "A 120 m train travels at 54 km/h. How long does it take to pass a pole?", options: ["(6 s)", "(8 s)", "(10 s)", "(12 s)"], answer: 1, solution: "Speed is (54 × 5/18=15) m/s. Time is (120/15=8) seconds." },
      { level: 'Standard', prompt: "Two trains 120 m and 180 m long travel in opposite directions at 36 km/h and 54 km/h. How long do they take to cross?", options: ["(10 s)", "(12 s)", "(15 s)", "(20 s)"], answer: 1, solution: "Total length is 300 m. Relative speed is (90 km/h=25 m/s). Time is (300/25=12) seconds." },
      { level: 'Challenge', prompt: "A 200 m train at 72 km/h overtakes a 100 m train at 54 km/h in the same direction. How long does the faster train take to pass it?", options: ["(30 s)", "(45 s)", "(60 s)", "(90 s)"], answer: 2, solution: "Distance is 300 m. Relative speed is (18 km/h=5 m/s). Time is (300/5=60) seconds." }
    ]
  },
  'boats-and-streams': {
    prerequisites: ['Time-speed-distance', 'Solving two linear equations'],
    coverage: ['Still-water speed', 'Current speed', 'Upstream and downstream rates', 'Recovering speeds from observations', 'Travel time', 'Constant-current assumptions'],
    theory: html([
      "<h3>Current changes ground speed</h3><p>Let b be a boat's speed in still water and s the current speed. Downstream motion is aided by the current, so its speed is b+s. Upstream motion is opposed, so its speed is b-s, provided b>s. These formulas assume the current and boat speed stay constant.</p>",
      "<p>If downstream and upstream speeds are known, add them and halve to find b; subtract and halve to find s. Use distance divided by the appropriate ground speed to find travel time. Do not add the current speed in both directions.</p>",
      "<p><strong>Worked example:</strong> A boat goes downstream at 18 km/h and upstream at 12 km/h. Still-water speed is (18+12)/2=15 km/h; current speed is (18-12)/2=3 km/h.</p>"
    ]),
    tricks: html([
      "<ul><li>Label each speed as upstream, downstream, still-water or current.</li><li>Use the sum for still-water speed and the difference for current speed.</li><li>Check that upstream speed is positive and smaller than downstream speed.</li><li>Use consistent distance units in round-trip problems.</li><li>For equal distances, do not take the arithmetic mean of unequal speeds.</li></ul>"
    ]),
    notes: html([
      "<ul><li>Downstream speed = b+s. Upstream speed = b-s.</li><li>Still-water speed = (downstream + upstream)/2.</li><li>Current speed = (downstream - upstream)/2.</li><li>Time = distance / ground speed.</li><li>For equal distances at speeds D and U, average speed = 2DU/(D+U).</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "A boat's downstream speed is 20 km/h and upstream speed is 12 km/h. Find the current speed.", options: ["(2 km/h)", "(4 km/h)", "(6 km/h)", "(8 km/h)"], answer: 1, solution: "Current speed is half the difference: ((20-12)/2=4) km/h." },
      { level: 'Standard', prompt: "A boat's still-water speed is 16 km/h and the current is 4 km/h. How long does a 48 km upstream trip take?", options: ["(3 h)", "(4 h)", "(5 h)", "(6 h)"], answer: 1, solution: "Upstream speed is (16-4=12) km/h. Time is (48/12=4) hours." },
      { level: 'Challenge', prompt: "A boat covers equal distances upstream at 12 km/h and downstream at 20 km/h. What is its average speed for the round trip?", options: ["(14 km/h)", "(15 km/h)", "(16 km/h)", "(16.5 km/h)"], answer: 1, solution: "For equal distances, average speed is the harmonic mean: (2 × 12 × 20/(12+20)=15) km/h." }
    ]
  },
  'races-and-circular-motion': {
    prerequisites: ['Ratios', 'Time-speed-distance'],
    coverage: ['Speed ratios in races', 'Lead and distance gaps', 'Circular-track meeting times', 'Same- and opposite-direction motion', 'Lap differences', 'Unit consistency'],
    theory: html([
      "<h3>Race comparisons</h3><p>For the same race distance, speed is inversely proportional to finishing time. If A beats B by d metres in a race of length L, then when A finishes B has covered L-d. Their speed ratio is (L:(L-d)). Use distance = speed × time to find a missing value.</p>",
      "<h3>Circular tracks</h3><p>On a circular track of length C, runners moving in opposite directions meet at relative speed u+v; those moving in the same direction meet at |u-v|. The first meeting time is track length divided by relative speed. Subsequent meetings occur at the same interval if speeds stay constant.</p>",
      "<p><strong>Worked example:</strong> On a 400 m track, runners move in opposite directions at 6 m/s and 4 m/s. Relative speed is 10 m/s, so they first meet after (400/10=40) seconds.</p>"
    ]),
    tricks: html([
      "<ul><li>At the instant the winner finishes, compare the loser's covered distance with the full race length.</li><li>Use relative speed; add for opposite directions and subtract for the same direction.</li><li>For repeated meetings, count relative laps rather than individual laps.</li><li>Convert track length and speeds to compatible units.</li><li>Distinguish a meeting, an overtake and a finish gap.</li></ul>"
    ]),
    notes: html([
      "<ul><li>For equal race distance, speed ratio is the inverse of time ratio.</li><li>If A beats B by d in an L-metre race, (v_A/v_B=L/(L-d)).</li><li>First circular-track meeting time = circumference / relative speed.</li><li>Same direction: relative speed = absolute speed difference.</li><li>Opposite directions: relative speed = sum of speeds.</li></ul>"
    ]),
    questions: [
      { level: 'Foundation', prompt: "Two runners move in opposite directions on a 400 m track at 6 m/s and 4 m/s. When do they first meet?", options: ["(20 s)", "(30 s)", "(40 s)", "(50 s)"], answer: 2, solution: "Relative speed is (6+4=10) m/s. Time is (400/10=40) seconds." },
      { level: 'Standard', prompt: "In a 100 m race, A finishes in 10 seconds and beats B by 20 m. How long does B take to run 100 m at the same speed?", options: ["(10 s)", "(11 s)", "(12.5 s)", "(15 s)"], answer: 2, solution: "When A finishes, B has run 80 m in 10 s, so B's speed is 8 m/s. Time for 100 m is (100/8=12.5) s." },
      { level: 'Challenge', prompt: "Two runners start together on a 500 m circular track and run in the same direction at 7 m/s and 5 m/s. After how long does the faster runner first lap the slower one?", options: ["(100 s)", "(200 s)", "(250 s)", "(500 s)"], answer: 2, solution: "Relative speed is (7-5=2) m/s. One full lap of separation requires 500 m, so time is (500/2=250) seconds." }
    ]
  },
  'algebraic-expressions': {
    prerequisites: ['Integers and fractions', 'Order of operations', 'Distributive property'],
    coverage: ['Terms, coefficients and constants', 'Like and unlike terms', 'Addition and subtraction of expressions', 'Expansion and factorisation', 'Substitution and evaluation', 'Algebraic identities and sign control'],
    theory: html([
      "<h3>Reading an expression</h3><p>An algebraic expression combines numbers, variables and operations without an equality sign. In (5x^2-3x+7), the terms are (5x^2), (-3x) and (7); their coefficients are 5, -3 and 7. The degree of a term is the sum of its variable exponents, so the first term has degree 2.</p>",
      "<h3>Collecting and operating</h3><p>Like terms have exactly the same variables raised to the same powers. Add their coefficients: (4a-7a=-3a). Multiply every term when expanding: (m(n+p)=mn+mp). A negative sign before parentheses changes the sign of every term inside.</p>",
      "<h3>Identities and factorisation</h3><p>Useful identities are (a+b)^2=a^2+2ab+b^2, (a-b)^2=a^2-2ab+b^2, and (a+b)(a-b)=a^2-b^2. Factorisation reverses expansion by taking out a common factor or recognising an identity.</p>",
      "<p><strong>Worked example:</strong> Simplify (3(2x-1)-2(x+4)). Expanding gives (6x-3-2x-8=4x-11). At (x=3), the value is (12-11=1).</p>"
    ]),
    tricks: html(["<ul><li>Write a subtraction as addition of the opposite before removing brackets.</li><li>Combine like terms only after expansion; (x) and (x^2) are unlike.</li><li>Check a factorisation by multiplying the factors back.</li><li>When evaluating, substitute a negative value in parentheses, such as ((-2)^2).</li><li>Use a common factor first, then check for an identity.</li></ul>"]),
    notes: html(["<ul><li>Coefficient is the signed numerical factor; constant term has no variable.</li><li>(x+x=2x), whereas (x times x=x^2).</li><li>(a^2-b^2=(a-b)(a+b)).</li><li>For a polynomial, degree is the largest exponent after like terms are combined.</li><li>Equivalent expressions have the same value for every permitted variable value.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Simplify (5a-3b+2a+8b).", options: ["(7a+5b)", "(7a-11b)", "(3a+5b)", "(7ab)"], answer: 0, solution: "Collect like terms: (5a+2a=7a) and (-3b+8b=5b). The result is (7a+5b)." },
      { level: 'Standard', prompt: "Expand and simplify (2(3x-4)-3(x+1)).", options: ["(3x-11)", "(9x-5)", "(3x-5)", "(9x-11)"], answer: 0, solution: "Distribute: (6x-8-3x-3=3x-11)." },
      { level: 'Challenge', prompt: "If (p+q=9) and (pq=14), evaluate (p^2+q^2).", options: ["(25)", "(53)", "(67)", "(81)"], answer: 1, solution: "Use ((p+q)^2=p^2+2pq+q^2). Thus (p^2+q^2=9^2-2(14)=81-28=53)." }
    ]
  },
  'linear-equations': {
    prerequisites: ['Integer operations', 'Fractions and ratios', 'Algebraic expressions'],
    coverage: ['Equivalent equations and inverse operations', 'Equations with brackets and fractions', 'Variables on both sides', 'Word-problem translation', 'Two-variable systems', 'Substitution checks and special cases'],
    theory: html([
      "<h3>One-variable equations</h3><p>An equation states that two expressions have equal values. Preserve equality by applying the same operation to both sides. For (ax+b=c), isolate (x) using inverse operations. If (a=0), the equation is either impossible or true for every value, depending on the remaining constants.</p>",
      "<h3>Brackets and fractions</h3><p>Expand or clear denominators carefully. Multiplying every term of an equation by a common nonzero denominator removes fractions without changing its solution.</p>",
      "<h3>Simultaneous equations</h3><p>A pair of linear equations represents two lines. Their intersection is the solution. Substitution replaces one variable using an equation; elimination adds or subtracts equations to cancel a variable. Parallel distinct lines give no solution; coincident lines give infinitely many.</p>",
      "<p><strong>Worked example:</strong> Solve (3(2x-1)=2x+13). Expanding gives (6x-3=2x+13), so (4x=16) and (x=4). Substitution into the original gives (3(8-1)=21) and (8+13=21).</p>"
    ]),
    tricks: html(["<ul><li>Keep a clear line for each equality-preserving operation.</li><li>When clearing fractions, multiply every term on both sides.</li><li>In a word problem, define the unknown and its unit before forming an equation.</li><li>Check in the original equation, especially after clearing denominators.</li><li>For two equations, choose elimination when coefficients can be matched quickly.</li></ul>"]),
    notes: html(["<ul><li>Adding or subtracting the same expression on both sides preserves equality.</li><li>Division by a coefficient is allowed only if it is nonzero.</li><li>For (ax+b=cx+d), if (a neq c), then (x=(d-b)/(a-c)).</li><li>Two linear equations can have one, none or infinitely many solutions.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Solve (4x+7=31).", options: ["(4)", "(5)", "(6)", "(7)"], answer: 2, solution: "Subtract 7 to get (4x=24); divide by 4, so (x=6)." },
      { level: 'Standard', prompt: "Solve (2(x-3)=x+5).", options: ["(7)", "(9)", "(11)", "(13)"], answer: 2, solution: "Expand to get (2x-6=x+5). Subtract (x) and add 6: (x=11)." },
      { level: 'Challenge', prompt: "Solve the system (2x+y=11) and (x-y=1).", options: ["((3,5))", "((4,3))", "((5,1))", "((6,-1))"], answer: 1, solution: "Add the equations: (3x=12), so (x=4). Then (4-y=1), giving (y=3). The solution is ((4,3))." }
    ]
  },
  'quadratic-equations': {
    prerequisites: ['Algebraic expressions', 'Factorisation', 'Linear equations'],
    coverage: ['Standard form and coefficients', 'Factorisation and zero-product property', 'Completing the square', 'Quadratic formula', 'Discriminant and root types', 'Sum/product of roots and applications'],
    theory: html([
      "<h3>Forms and solutions</h3><p>A quadratic equation is (ax^2+bx+c=0), where (a neq 0). Factoring into two linear factors and using the zero-product property is often fastest. Otherwise, complete the square or apply the quadratic formula.</p>",
      "<h3>Formula and discriminant</h3><p>The roots are (x=(-b plusminus sqrt(b^2-4ac))/(2a)). The discriminant (D=b^2-4ac) determines real roots: (D>0) gives two distinct real roots, (D=0) one repeated real root, and (D<0) no real roots.</p>",
      "<h3>Root relationships</h3><p>If roots are (r) and (s), then (r+s=-b/a) and (rs=c/a). These relationships can answer questions about roots without solving the equation.</p>",
      "<p><strong>Worked example:</strong> Solve (2x^2-5x+2=0). Factor as ((2x-1)(x-2)=0), so (x=1/2) or (x=2). Their sum is (5/2=-b/a) and product is (1=c/a).</p>"
    ]),
    tricks: html(["<ul><li>Write all terms on one side and identify (a,b,c), including zero coefficients.</li><li>Try integer factor pairs when the coefficients are small.</li><li>Use the discriminant before attempting a full solution if only the number of roots is asked.</li><li>Do not divide an equation by an expression that could be zero without checking that case.</li><li>Check roots by substitution into the original equation.</li></ul>"]),
    notes: html(["<ul><li>Quadratic formula: (x=(-b plusminus sqrt(b^2-4ac))/(2a)).</li><li>Root sum is (-b/a); root product is (c/a).</li><li>A parabola opens upward for (a>0) and downward for (a<0).</li><li>The vertex has x-coordinate (-b/(2a)).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Solve (x^2-9=0).", options: ["(x=3 only)", "(x=-3 only)", "(x=3 or x=-3)", "(x=9 or x=-9)"], answer: 2, solution: "Factor: ((x-3)(x+3)=0). Thus (x=3) or (x=-3)." },
      { level: 'Standard', prompt: "How many distinct real roots does (x^2-6x+9=0) have?", options: ["(0)", "(1)", "(2)", "Infinitely many"], answer: 1, solution: "The discriminant is ((-6)^2-4(1)(9)=36-36=0), so there is one repeated real root." },
      { level: 'Challenge', prompt: "The roots of (x^2-7x+k=0) differ by 1. Find (k).", options: ["(10)", "(12)", "(13)", "(14)"], answer: 1, solution: "The roots have sum 7 and differ by 1, so they are 3 and 4. Their product is (k=12)." }
    ]
  },
  'polynomials': {
    prerequisites: ['Algebraic expressions', 'Exponents', 'Factorisation'],
    coverage: ['Polynomial terms and degree', 'Addition, subtraction and multiplication', 'Identities and factorisation', 'Remainder theorem', 'Factor theorem', 'Zeros and coefficient relationships'],
    theory: html([
      "<h3>Structure and degree</h3><p>A polynomial in (x) is a finite sum of terms (a_k x^k) with nonnegative integer exponents. After like terms are combined, its highest exponent with a nonzero coefficient is its degree. A nonzero constant has degree zero; the zero polynomial has no defined degree in the usual convention.</p>",
      "<h3>Zeros, factors and remainders</h3><p>A number (r) is a zero if (P(r)=0). The factor theorem says ((x-r)) is a factor exactly when (P(r)=0). The remainder theorem says division by ((x-r)) leaves remainder (P(r)).</p>",
      "<h3>Quadratic relationships</h3><p>For (ax^2+bx+c) with roots (r,s), (r+s=-b/a) and (rs=c/a). Factorisation is useful for identifying zeros and solving polynomial equations.</p>",
      "<p><strong>Worked example:</strong> Let (P(x)=x^3-4x). Then (P(2)=8-8=0), so ((x-2)) is a factor. Factoring fully gives (x(x-2)(x+2)).</p>"
    ]),
    tricks: html(["<ul><li>Arrange terms in descending powers and insert missing zero-coefficient terms when using division.</li><li>Test simple integer roots among factors of the constant term for monic polynomials.</li><li>Take out the greatest common factor before using identities.</li><li>Verify a proposed factor by substitution or multiplication.</li></ul>"]),
    notes: html(["<ul><li>Polynomial exponents are whole numbers 0, 1, 2, and so on; variables cannot appear in denominators or exponents.</li><li>Remainder on division by ((x-a)) is (P(a)).</li><li>Factor ((x-a)) corresponds to zero (a), not (-a).</li><li>For a monic cubic with roots (r,s,t), sum of roots is the negative coefficient of (x^2).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "What is the degree of (4x^5-3x^2+7)?", options: ["(2)", "(3)", "(5)", "(7)"], answer: 2, solution: "The highest exponent with a nonzero coefficient is 5, so the degree is 5." },
      { level: 'Standard', prompt: "What is the remainder when (P(x)=x^2+2x+5) is divided by (x+1)?", options: ["(2)", "(4)", "(5)", "(8)"], answer: 1, solution: "Since (x+1=x-(-1)), the remainder is (P(-1)=1-2+5=4)." },
      { level: 'Challenge', prompt: "If (x-3) is a factor of (x^2+kx-12), find (k).", options: ["(-1)", "(1)", "(4)", "(7)"], answer: 1, solution: "By the factor theorem, substitute (x=3): (9+3k-12=0), so (3k=3) and (k=1)." }
    ]
  },
  'linear-inequalities': {
    prerequisites: ['Integer operations', 'Linear equations', 'Number line'],
    coverage: ['Inequality symbols and solution sets', 'Operations preserving order', 'Reversal under negative multiplication', 'Compound inequalities', 'Interval notation and endpoints', 'Quadratic sign intervals'],
    theory: html([
      "<h3>Order and transformations</h3><p>An inequality compares values using (<), (le), (>), or (ge). Adding or subtracting the same quantity preserves its direction. Multiplication or division by a positive number also preserves it; multiplication or division by a negative number reverses it.</p>",
      "<h3>Solution sets</h3><p>A solution is any value that makes the original inequality true. Show a strict endpoint with an open circle and an inclusive endpoint with a closed circle. A compound inequality can describe an interval, such as (2 le x < 7).</p>",
      "<h3>Polynomial inequalities</h3><p>For a factored product, mark its zeros on a number line and test the sign in each interval. Include a zero only for a non-strict inequality. This sign-chart method also works for rational expressions after recording excluded denominator zeros.</p>",
      "<p><strong>Worked example:</strong> Solve (-3<2x+1 le 9). Subtract 1 throughout to obtain (-4<2x le 8); divide by positive 2 to get (-2<x le 4).</p>"
    ]),
    tricks: html(["<ul><li>Reverse the sign only when multiplying or dividing by a negative number.</li><li>Keep all three parts of a compound inequality in the same operation.</li><li>For products, use critical points and one test value per interval.</li><li>For rational inequalities, a denominator zero is excluded even if cancellation seems possible.</li><li>Substitute an interior value and check boundary inclusion separately.</li></ul>"]),
    notes: html(["<ul><li>(a<b) means every value between them is strictly ordered; it does not include equality.</li><li>For (x^2-a^2>0), the solution is (x<-a) or (x>a) when (a>0).</li><li>Interval brackets include endpoints; parentheses exclude them.</li><li>Multiplying by an expression of unknown sign requires a sign analysis.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Solve (5x-4 le 11).", options: ["(x le 3)", "(x ge 3)", "(x le 15/5)", "(x ge 15/5)"], answer: 0, solution: "Add 4: (5x le 15). Divide by positive 5: (x le 3)." },
      { level: 'Standard', prompt: "Solve (-2x+6>0).", options: ["(x>3)", "(x<3)", "(x>-3)", "(x<-3)"], answer: 1, solution: "Subtract 6: (-2x>-6). Dividing by (-2) reverses the sign, so (x<3)." },
      { level: 'Challenge', prompt: "Solve ((x-2)(x+1) le 0).", options: ["(x le -1 or x ge 2)", "(-1 le x le 2)", "(x<-1)", "(x>2)"], answer: 1, solution: "The zeros are (-1) and 2. The product is negative between the roots and zero at each endpoint, so (-1 le x le 2)." }
    ]
  },
  'functions-and-graphs': {
    prerequisites: ['Coordinate plane', 'Algebraic expressions', 'Linear equations'],
    coverage: ['Function notation and evaluation', 'Domain and range', 'Graph and intercept interpretation', 'Vertical-line test', 'Composite and inverse ideas', 'Linear, quadratic and reciprocal examples'],
    theory: html([
      "<h3>Function rule</h3><p>A function assigns exactly one output to each permitted input. The domain is the allowed input set and the range is the resulting output set. In (f(x)), the symbol names the output; it is not multiplication.</p>",
      "<h3>Domain restrictions</h3><p>For real-valued expressions, a denominator cannot be zero and the radicand of an even root must be nonnegative. For (f(x)=1/(x-2)), exclude (x=2); for (g(x)=sqrt(x-3)), require (x ge 3).</p>",
      "<h3>Graphs and transformations</h3><p>The graph consists of points ((x,f(x))). A vertical line intersects a function's graph at most once. The x-intercepts solve (f(x)=0); the y-intercept is (f(0)) when defined. Replacing (x) by (x-h) shifts a graph right by (h); adding (k) shifts it upward by (k).</p>",
      "<p><strong>Worked example:</strong> For (f(x)=x^2-4x+3), factor as ((x-1)(x-3)); the x-intercepts are 1 and 3, while the y-intercept is (f(0)=3).</p>"
    ]),
    tricks: html(["<ul><li>For (f(a+h)), substitute the entire expression (a+h) wherever (x) appears.</li><li>Check denominator and root restrictions before stating a domain.</li><li>Use intercepts and symmetry to sketch simple polynomial graphs.</li><li>A graph may pass the vertical-line test without being one-to-one.</li><li>For composition, evaluate the inside function first.</li></ul>"]),
    notes: html(["<ul><li>For (f(x)=mx+c), slope is (m) and y-intercept is (c).</li><li>For (f(x)=x^2), outputs are nonnegative and the graph is symmetric about the y-axis.</li><li>Horizontal-line test is a test for one-to-one behavior, not for being a function.</li><li>Inverse functions swap input and output and require one-to-one restriction.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "If (f(x)=3x-2), find (f(5)).", options: ["(11)", "(13)", "(15)", "(17)"], answer: 1, solution: "Substitute 5: (f(5)=3(5)-2=13)." },
      { level: 'Standard', prompt: "What is the real domain of (g(x)=1/(x^2-9))?", options: ["All real x", "(x neq 3 only)", "(x neq -3 only)", "(x neq -3 and x neq 3)"], answer: 3, solution: "The denominator factors as ((x-3)(x+3)); exclude both values (-3) and 3." },
      { level: 'Challenge', prompt: "For (h(x)=x^2+2x), what is the minimum value over the real numbers?", options: ["(-2)", "(-1)", "(0)", "(1)"], answer: 1, solution: "Complete the square: (x^2+2x=(x+1)^2-1). Since a square is at least zero, the minimum is (-1)." }
    ]
  },
  'logarithms': {
    prerequisites: ['Indices and exponents', 'Algebraic equations', 'Positive-number properties'],
    coverage: ['Definition, base and argument restrictions', 'Product, quotient and power laws', 'Change of base', 'Exponential-logarithmic conversion', 'Solving logarithmic equations with domain checks', 'Common and natural logarithms'],
    theory: html([
      "<h3>Definition and restrictions</h3><p>(log_b(a)=c) means exactly that (b^c=a). For real logarithms, the base satisfies (b>0) and (b neq 1), and the argument satisfies (a>0). A logarithm is an exponent, not a product.</p>",
      "<h3>Laws</h3><p>For positive (x,y) and valid base (b), (log_b(xy)=log_b(x)+log_b(y)); (log_b(x/y)=log_b(x)-log_b(y)); and (log_b(x^k)=k log_b(x)). Also (log_b(1)=0) and (log_b(b)=1).</p>",
      "<h3>Change of base and equations</h3><p>(log_b(a)=log_c(a)/log_c(b)) when the expressions are defined. To solve an equation, combine only valid logs, convert to exponential form, and check every candidate in the original domain.</p>",
      "<p><strong>Worked example:</strong> Solve (log_2(x-1)=3). The domain first requires (x>1). Convert to exponential form: (x-1=2^3=8), so (x=9), which satisfies the domain.</p>"
    ]),
    tricks: html(["<ul><li>Write the argument-positive condition before solving.</li><li>Never split a sum inside a logarithm: (log_b(x+y)) has no product-law expansion.</li><li>Use exponent form to verify an exact logarithm value.</li><li>After combining logs, keep track of restrictions from every original argument.</li><li>For estimates, compare the argument with nearby powers of the base.</li></ul>"]),
    notes: html(["<ul><li>(log_b(xy)=log_b(x)+log_b(y)); (log_b(x/y)=log_b(x)-log_b(y)).</li><li>(log_b(x^r)=r log_b(x)) for (x>0).</li><li>Common logarithm has base 10; natural logarithm has base (e).</li><li>For (b>1), the log function increases; for (0<b<1), it decreases.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Evaluate (log_5 125).", options: ["(2)", "(3)", "(5)", "(25)"], answer: 1, solution: "Since (5^3=125), (log_5(125)=3)." },
      { level: 'Standard', prompt: "If (log_3(x+1)=2), find (x).", options: ["(2)", "(6)", "(8)", "(9)"], answer: 2, solution: "Convert to exponential form: (x+1=3^2=9), so (x=8). The argument is positive." },
      { level: 'Challenge', prompt: "If (log_2(a)=3) and (log_2(b)=2), find (log_2(a^2/b)).", options: ["(2)", "(3)", "(4)", "(8)"], answer: 2, solution: "Use the laws: (2log_2(a)-log_2(b)=2(3)-2=4)." }
    ]
  },
  'sequences-and-series': {
    prerequisites: ['Number patterns', 'Algebraic expressions', 'Exponents'],
    coverage: ['Terms, indices and general terms', 'Arithmetic progressions and common difference', 'Finite arithmetic series', 'Geometric progressions and common ratio', 'Finite and infinite geometric sums', 'Pattern recognition and consistency checks'],
    theory: html([
      "<h3>Sequences and general terms</h3><p>A sequence is an ordered list generated by a rule. The nth term gives the value at position (n). Check differences, ratios, alternating patterns and familiar figurate numbers before guessing a rule.</p>",
      "<h3>Arithmetic progression</h3><p>An arithmetic progression (AP) has constant difference (d). Its nth term is (a_n=a+(n-1)d), where (a) is the first term. The sum of the first (n) terms is (S_n=n/2(2a+(n-1)d)=n/2(a+l)), where (l) is the last term.</p>",
      "<h3>Geometric progression</h3><p>A geometric progression (GP) has constant ratio (r). Its nth term is (a_n=ar^{n-1}); for (r neq 1), the first n terms sum to (S_n=a(1-r^n)/(1-r)). An infinite GP converges to (a/(1-r)) only when (|r|<1).</p>",
      "<p><strong>Worked example:</strong> In (4,7,10,...), (a=4) and (d=3). The 12th term is (4+11(3)=37), and the first 12 terms sum to (12/2(4+37)=246).</p>"
    ]),
    tricks: html(["<ul><li>Write the first several differences before deciding whether a sequence is arithmetic.</li><li>For a GP, divide consecutive nonzero terms to check the ratio.</li><li>Translate the stated position carefully: the first term uses exponent zero in a GP formula.</li><li>For sums, identify whether the last term or number of terms is known.</li><li>Do not use an infinite GP sum when (|r| ge 1).</li></ul>"]),
    notes: html(["<ul><li>AP nth term: (a+(n-1)d); AP sum: (n/2)(first+last).</li><li>GP nth term: (ar^{n-1}); finite GP sum: (a(1-r^n)/(1-r)).</li><li>Triangular numbers: (n(n+1)/2).</li><li>Square numbers have successive differences that are consecutive odd numbers.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Find the 10th term of the AP (3, 7, 11, ...).", options: ["(35)", "(37)", "(39)", "(43)"], answer: 2, solution: "Here (a=3), (d=4). Thus (a_10=3+9(4)=39)." },
      { level: 'Standard', prompt: "Find the sum of the first 8 terms of (2, 6, 10, ...).", options: ["(112)", "(120)", "(128)", "(136)"], answer: 2, solution: "The eighth term is (2+7(4)=30). Sum is (8/2)(2+30)=128." },
      { level: 'Challenge', prompt: "A GP begins (81, 27, 9, ...). Find the sum of its first four terms.", options: ["(108)", "(120)", "(121)", "(126)"], answer: 1, solution: "The first four terms are 81, 27, 9 and 3. Their sum is (81+27+9+3=120)." }
    ]
  },
  'algebraic-word-problems': {
    prerequisites: ['Algebraic expressions', 'Linear equations', 'Ratios and percentages'],
    coverage: ['Define variables and units', 'Translate relationships into equations', 'Consecutive integers and digit problems', 'Age and mixture formulations', 'Number and geometry applications', 'Validate solutions in the original context'],
    theory: html([
      "<h3>Model before solving</h3><p>Choose a variable for the unknown and state what it measures. Translate each sentence into an equation or inequality, keeping units consistent. Solve the model, then interpret the result in context.</p>",
      "<h3>Common structures</h3><p>Consecutive integers can be written as (n,n+1) or (n,n+2) for consecutive even or odd values. A two-digit number with tens digit (a) and units digit (b) is (10a+b); reversing its digits gives (10b+a). For a rectangle, perimeter is (2l+2w) and area is (lw).</p>",
      "<h3>Checking the model</h3><p>A valid answer must satisfy the original conditions, restrictions and requested units. Reject impossible values such as a negative count of people, even if they solve an algebraic equation.</p>",
      "<p><strong>Worked example:</strong> The sum of two consecutive integers is 41. Let them be (n) and (n+1). Then (2n+1=41), so (n=20); the integers are 20 and 21, and their sum checks to 41.</p>"
    ]),
    tricks: html(["<ul><li>Make a small variable legend before writing equations.</li><li>Use a diagram or table for geometry, digits, rates and mixtures.</li><li>Translate comparison words precisely: '5 less than x' is (x-5).</li><li>Keep money, distance, time and percentage units consistent.</li><li>Substitute the answer back into every condition, not only the equation first formed.</li></ul>"]),
    notes: html(["<ul><li>Percent of a quantity: (p/100 times quantity).</li><li>Two-digit number: (10t+u); digit reversal changes its value by (9(t-u)).</li><li>For fixed sum (S) and difference (D), the larger value is ((S+D)/2).</li><li>Area and perimeter describe different quantities; include units in the final answer.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "The sum of three consecutive integers is 72. What is the middle integer?", options: ["(23)", "(24)", "(25)", "(26)"], answer: 1, solution: "Let the integers be (n-1,n,n+1). Their sum is (3n=72), so the middle integer is 24." },
      { level: 'Standard', prompt: "A two-digit number has tens digit 3 more than its units digit. Their sum is 9. Find the number.", options: ["(36)", "(63)", "(72)", "(81)"], answer: 1, solution: "Let the units digit be (u); tens digit is (u+3). Then (2u+3=9), so (u=3) and the tens digit is 6. The number is 63." },
      { level: 'Challenge', prompt: "A rectangle's length is 4 cm more than its width. Its perimeter is 36 cm. Find its area.", options: ["(60 cm^2)", "(65 cm^2)", "(77 cm^2)", "(80 cm^2)"], answer: 2, solution: "Let width be (w), length (w+4). Then (2w+2(w+4)=36), so (w=7) and length is 11. Area is (7 times 11=77 cm^2)." }
    ]
  },
  'lines-and-angles': {
    prerequisites: ['Basic geometric vocabulary', 'Fractions and equations'],
    coverage: ['Points, lines, rays and segments', 'Adjacent and vertically opposite angles', 'Linear pairs and perpendicular lines', 'Parallel lines with a transversal', 'Angle sums in triangles and polygons', 'Reasoned multi-step angle calculations'],
    theory: html([
      "<h3>Angle relationships</h3><p>A point, line, ray and segment describe different geometric objects. Adjacent angles share a vertex and side without overlapping. A linear pair sums to 180 degrees; vertically opposite angles are equal. Perpendicular lines meet at 90 degrees.</p>",
      "<h3>Parallel lines</h3><p>When a transversal crosses parallel lines, corresponding angles are equal, alternate interior angles are equal, and same-side interior angles sum to 180 degrees. These relationships can also establish that two lines are parallel.</p>",
      "<h3>Polygon angle sums</h3><p>The interior-angle sum of an n-sided polygon is ((n-2) times 180 degrees). A regular polygon has equal interior angles, each equal to ((n-2) times 180/n) degrees. An exterior angle at each vertex sums to 360 degrees around a polygon.</p>",
      "<p><strong>Worked example:</strong> Two same-side interior angles are (3x+10) degrees and (2x+20) degrees. They sum to 180, so (5x+30=180), giving (x=30); the angles are 100 and 80 degrees.</p>"
    ]),
    tricks: html(["<ul><li>Mark the known relation on the diagram before forming an equation.</li><li>Distinguish equal angle pairs from supplementary pairs.</li><li>For a transversal, identify whether angles are corresponding, alternate or same-side before calculating.</li><li>Use a polygon's interior sum only after counting its sides correctly.</li></ul>"]),
    notes: html(["<ul><li>Angles on a straight line sum to 180 degrees; angles around a point sum to 360 degrees.</li><li>Vertically opposite angles are equal.</li><li>Triangle angle sum is 180 degrees; quadrilateral angle sum is 360 degrees.</li><li>For a regular n-gon, exterior angle is (360/n) degrees.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "One angle in a linear pair is 68 degrees. Find the other.", options: ["(22 degrees)", "(68 degrees)", "(112 degrees)", "(292 degrees)"], answer: 2, solution: "A linear pair sums to 180 degrees: (180-68=112) degrees." },
      { level: 'Standard', prompt: "Parallel lines are cut by a transversal. A corresponding angle is 73 degrees. What is its alternate interior angle?", options: ["(73 degrees)", "(107 degrees)", "(180 degrees)", "(287 degrees)"], answer: 0, solution: "Corresponding and alternate interior angles are both equal when the lines are parallel, so the angle is 73 degrees." },
      { level: 'Challenge', prompt: "Find each interior angle of a regular decagon.", options: ["(120 degrees)", "(135 degrees)", "(144 degrees)", "(150 degrees)"], answer: 2, solution: "The interior sum is ((10-2) times 180=1440) degrees. Divide by 10: each angle is 144 degrees." }
    ]
  },
  'symmetry': {
    prerequisites: ['Basic shapes', 'Coordinate plane', 'Fractions and angles'],
    coverage: ['Line or reflection symmetry', 'Rotational symmetry and order', 'Symmetry in common polygons', 'Reflection in coordinate axes', 'Translation, rotation and reflection distinctions', 'Symmetry in patterns and designs'],
    theory: html([
      "<h3>Line symmetry</h3><p>A line of symmetry divides a figure into two congruent mirror images. Corresponding points lie equal perpendicular distances from the line. A figure may have zero, one or several lines of symmetry.</p>",
      "<h3>Rotational symmetry</h3><p>A figure has rotational symmetry when a turn smaller than a full turn maps it onto itself. Its order is the number of matching positions in one 360-degree turn; the smallest positive angle is (360/order) degrees.</p>",
      "<h3>Coordinate reflections</h3><p>Reflection across the x-axis maps ((x,y)) to ((x,-y)); across the y-axis it maps to ((-x,y)); across the origin it maps to ((-x,-y)). A reflection preserves lengths and angles but reverses orientation.</p>",
      "<p><strong>Worked example:</strong> A regular hexagon has six reflection axes and rotational symmetry of order 6. Its smallest matching turn is (360/6=60) degrees.</p>"
    ]),
    tricks: html(["<ul><li>For line symmetry, test whether folding on the proposed line makes every point coincide.</li><li>Count distinct matching positions during one complete 360-degree turn.</li><li>Do not count the full 360-degree turn as an additional nontrivial position.</li><li>Use coordinate rules to track signs under reflection.</li><li>Translation slides a figure and does not create a mirror image or turn.</li></ul>"]),
    notes: html(["<ul><li>Reflection preserves distances and angle sizes.</li><li>Order 1 means no nontrivial rotational symmetry.</li><li>A circle has infinitely many lines of symmetry and rotational symmetry through every angle.</li><li>A non-square rectangle has two lines of symmetry and rotational order 2.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "How many lines of symmetry does a non-square rectangle have?", options: ["(1)", "(2)", "(3)", "(4)"], answer: 1, solution: "A non-square rectangle has one horizontal and one vertical midpoint axis, so it has 2." },
      { level: 'Standard', prompt: "A regular pentagon has rotational symmetry of what order?", options: ["(2)", "(4)", "(5)", "(10)"], answer: 2, solution: "A regular n-sided polygon maps to itself n times in one full turn. For a pentagon the order is 5." },
      { level: 'Challenge', prompt: "Reflect the point ((-3,4)) across the y-axis. What is its image?", options: ["((-3,-4))", "((3,4))", "((3,-4))", "((4,-3))"], answer: 1, solution: "Reflection across the y-axis changes the sign of x and keeps y: ((-3,4)) maps to ((3,4))." }
    ]
  },
  'geometric-constructions': {
    prerequisites: ['Lines and angles', 'Triangles', 'Compass and straightedge use'],
    coverage: ['Accurate ruler-compass conventions', 'Perpendicular bisectors', 'Angle bisectors', 'Constructing standard angles', 'Triangle construction by SSS, SAS and ASA', 'Loci and construction reasoning'],
    theory: html([
      "<h3>Permitted construction tools</h3><p>Classical constructions use an unmarked straightedge to draw a line through known points and a compass to copy a radius. Keep the compass width fixed when transferring equal distances; label construction arcs and intersections clearly.</p>",
      "<h3>Bisectors and standard angles</h3><p>A perpendicular bisector passes through a segment's midpoint at 90 degrees. Points on it are equidistant from the segment endpoints. An angle bisector divides an angle into two equal angles; its points are equidistant from the two arms.</p>",
      "<h3>Triangle construction</h3><p>Three side lengths construct a unique triangle when they satisfy the triangle inequality. Two sides and their included angle (SAS), or two angles and a corresponding side (ASA/AAS), also determine a triangle. An SSA specification can be ambiguous.</p>",
      "<p><strong>Worked construction:</strong> To construct the perpendicular bisector of segment (AB), draw equal-radius arcs centered at A and B using a radius greater than half (AB). Join the two arc intersection points; this line bisects (AB) at right angles.</p>"
    ]),
    tricks: html(["<ul><li>Use the same compass opening for paired arcs that must be equal.</li><li>Choose a radius large enough for the arcs to intersect on both sides.</li><li>Do not erase the arcs: they show why the construction is valid.</li><li>Check triangle data with the triangle inequality before drawing.</li><li>Distinguish an angle bisector from a perpendicular bisector.</li></ul>"]),
    notes: html(["<ul><li>A point on a perpendicular bisector is equidistant from the two endpoints.</li><li>A point on an angle bisector is equidistant from the angle's sides.</li><li>Constructible angles include 60, 90, 30 and 45 degrees using standard steps.</li><li>Three lengths form a triangle only when the sum of any two exceeds the third.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "What is the locus of points equidistant from the endpoints of a fixed segment?", options: ["A circle centered at an endpoint", "The perpendicular bisector", "A parallel line", "The segment itself"], answer: 1, solution: "Every point equidistant from both endpoints lies on the segment's perpendicular bisector." },
      { level: 'Standard', prompt: "Which set of side lengths cannot form a triangle?", options: ["(4,5,6)", "(3,4,6)", "(5,5,9)", "(2,3,6)"], answer: 3, solution: "The sum of the two shorter sides must exceed the longest side. Here (2+3=5<6), so no triangle is possible." },
      { level: 'Challenge', prompt: "Two sides and their included angle are given. Which criterion determines the triangle uniquely?", options: ["(SSS)", "(SAS)", "(SSA in every case)", "One side only"], answer: 1, solution: "Two sides and the included angle determine a unique triangle by the SAS congruence criterion." }
    ]
  },
  'coordinate-geometry': {
    prerequisites: ['Integers and ordered pairs', 'Linear equations', 'Pythagorean theorem'],
    coverage: ['Cartesian axes and quadrants', 'Plotting ordered pairs', 'Distance and midpoint', 'Slope and parallel/perpendicular lines', 'Line equations and intercepts', 'Coordinate proofs and geometric interpretation'],
    theory: html([
      "<h3>Cartesian plane</h3><p>A point is written ((x,y)): move horizontally by x and vertically by y. The origin is ((0,0)); the axes divide the plane into four quadrants. Signs are (+,+), (-,+), (-,-), and (+,-) in quadrants I through IV.</p>",
      "<h3>Distance, midpoint and slope</h3><p>For points ((x_1,y_1)) and ((x_2,y_2)), distance is (sqrt((x_2-x_1)^2+(y_2-y_1)^2)); midpoint is (((x_1+x_2)/2,(y_1+y_2)/2)). Slope is ((y_2-y_1)/(x_2-x_1)) when (x_2 neq x_1); a vertical line has undefined slope.</p>",
      "<h3>Lines</h3><p>Slope-intercept form is (y=mx+c). Parallel nonvertical lines have equal slopes; perpendicular nonvertical lines have slopes whose product is (-1). The intercept form and point-slope form can be used when those values are known.</p>",
      "<p><strong>Worked example:</strong> Between ((1,2)) and ((4,6)), the slope is ((6-2)/(4-1)=4/3), the midpoint is ((5/2,4)), and the distance is (sqrt(3^2+4^2)=5).</p>"
    ]),
    tricks: html(["<ul><li>Keep x-coordinate changes and y-coordinate changes in consistent order.</li><li>Square both coordinate differences before adding in the distance formula.</li><li>For vertical lines, avoid dividing by a zero x-difference.</li><li>Sketch intercepts to check a line equation's signs and direction.</li><li>Use the midpoint to split a segment into equal parts.</li></ul>"]),
    notes: html(["<ul><li>Distance formula comes from the Pythagorean theorem.</li><li>Midpoint coordinates are the averages of corresponding endpoint coordinates.</li><li>Horizontal line slope is 0; vertical line slope is undefined.</li><li>For (Ax+By+C=0), slope is (-A/B) when (B neq 0).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "In which quadrant is ((-4,-2))?", options: ["I", "II", "III", "IV"], answer: 2, solution: "Both coordinates are negative, so the point is in quadrant III." },
      { level: 'Standard', prompt: "Find the midpoint of ((2,-1)) and ((8,5)).", options: ["((3,2))", "((5,2))", "((5,3))", "((10,4))"], answer: 1, solution: "Average coordinates: (((2+8)/2,(-1+5)/2)=(5,2))." },
      { level: 'Challenge', prompt: "What is the slope of a line perpendicular to a line of slope (2/3)?", options: ["(2/3)", "(-2/3)", "(3/2)", "(-3/2)"], answer: 3, solution: "Perpendicular slopes are negative reciprocals. The required slope is (-3/2), since ((2/3)(-3/2)=-1)." }
    ]
  },
  'spatial-visualisation': {
    prerequisites: ['2D shapes', '3D solids', 'Directions and coordinates'],
    coverage: ['Faces, edges and vertices', 'Nets and folding', 'Views and projections', 'Rotations and reflections of solids', 'Cubes, painted faces and cuts', 'Spatial directions and hidden-face reasoning'],
    theory: html([
      "<h3>Representing solids</h3><p>A three-dimensional object can be described by its faces, edges and vertices. A net is a flat arrangement that folds along edges into a solid without overlap. Orthographic views show the object from a chosen direction; perspective drawings suggest depth.</p>",
      "<h3>Visualising transformations</h3><p>Rotation changes orientation but preserves shape and size. A reflection produces a mirror image. When mentally rotating a labelled solid, track one distinctive face or vertex rather than relying on a visual impression.</p>",
      "<h3>Cube reasoning</h3><p>In a cube net, adjacent faces share an edge after folding; opposite faces do not share an edge. If a cube is painted on the outside and cut into equal small cubes, the number of painted faces depends on whether a small cube is at a corner, edge, face interior or fully interior.</p>",
      "<p><strong>Worked example:</strong> A cube painted on all six faces is cut into (n^3) unit cubes. For (n ge 2), corner cubes have 3 painted faces, non-corner edge cubes 2, face-interior cubes 1, and interior cubes 0.</p>"
    ]),
    tricks: html(["<ul><li>Mark a reference face before folding or rotating a diagram mentally.</li><li>For painted-cube counts, classify by location instead of listing every small cube.</li><li>Use the net's shared edges to infer adjacency; page proximity alone is not enough.</li><li>Check the stated viewing direction before comparing front, side and top views.</li><li>Rotate the object mentally while keeping labels attached to the same face.</li></ul>"]),
    notes: html(["<ul><li>Cube has 6 faces, 12 edges and 8 vertices.</li><li>For an (n by n by n) painted cube: corners = 8; edge-interior cubes = (12(n-2)); face-interior cubes = (6(n-2)^2); inner cubes = ((n-2)^3), for (n ge 2).</li><li>A net must have exactly six square faces and fold without overlap.</li><li>Rigid rotations and reflections preserve all lengths and angles.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "How many faces does a cube have?", options: ["(4)", "(6)", "(8)", "(12)"], answer: 1, solution: "A cube has six square faces." },
      { level: 'Standard', prompt: "A cube is painted on every outer face and cut into (3^3) equal cubes. How many small cubes have exactly two painted faces?", options: ["(8)", "(12)", "(18)", "(24)"], answer: 1, solution: "Each of the 12 edges has (3-2=1) non-corner cube. Total: 12." },
      { level: 'Challenge', prompt: "A fully painted cube is divided into (4^3) unit cubes. How many small cubes have no paint?", options: ["(4)", "(8)", "(16)", "(27)"], answer: 1, solution: "Only interior cubes have no paint. Their count is ((4-2)^3=8)." }
    ]
  },
  'two-dimensional-mensuration': {
    prerequisites: ['Fractions and decimals', 'Lines and angles', 'Basic shape properties'],
    coverage: ['Perimeter and area of plane figures', 'Composite and shaded regions', 'Circle circumference and area', 'Arc length and sector area', 'Similarity and scale effects', 'Unit conversion and boundary interpretation'],
    theory: html([
      "<h3>Perimeter and area</h3><p>Perimeter measures boundary length; area measures the region inside. Rectangle: (P=2(l+w)), (A=lw). Triangle: (A=1/2 bh). Parallelogram: (A=bh). Trapezium: (A=1/2(a+b)h), where (a,b) are parallel sides.</p>",
      "<h3>Circles and sectors</h3><p>For radius (r), circumference is (2 pi r) and area is (pi r^2). An arc with central angle (theta) degrees has length ((theta/360) times 2 pi r); its sector area is ((theta/360) times pi r^2).</p>",
      "<h3>Composite regions and scale</h3><p>Break a composite figure into known shapes or subtract a cut-out. A length scale factor (k) multiplies perimeter by (k) and area by (k^2). State whether a diagram's dimensions refer to a radius, diameter, height or slant side.</p>",
      "<p><strong>Worked example:</strong> A 14 cm by 10 cm rectangle has a 4 cm by 3 cm corner removed. The remaining area is (14 times 10 - 4 times 3=128 cm^2).</p>"
    ]),
    tricks: html(["<ul><li>Sketch and label dimensions before selecting a formula.</li><li>Convert every length to the same unit before finding area or perimeter.</li><li>For a shaded region, calculate the enclosing area and subtract unshaded parts.</li><li>Use the diameter as (2r) only when the problem supplies a diameter.</li><li>Check whether the requested boundary includes an internal edge around a cut-out.</li></ul>"]),
    notes: html(["<ul><li>Square: (A=s^2), (P=4s); circle: (A=pi r^2), circumference (2 pi r).</li><li>Area uses square units and perimeter uses linear units.</li><li>Changing all lengths by factor (k) changes area by factor (k^2).</li><li>For an annulus, area is (pi(R^2-r^2)).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Find the area of a triangle with base 12 cm and perpendicular height 7 cm.", options: ["(19 cm^2)", "(42 cm^2)", "(84 cm^2)", "(168 cm^2)"], answer: 1, solution: "Area is (1/2 times 12 times 7=42 cm^2)." },
      { level: 'Standard', prompt: "A circle has diameter 14 cm. Find its circumference in terms of (pi).", options: ["(7 pi cm)", "(14 pi cm)", "(28 pi cm)", "(49 pi cm)"], answer: 1, solution: "Radius is 7 cm. Circumference is (2 pi times 7=14 pi cm)." },
      { level: 'Challenge', prompt: "A square's side is increased by 20%. By what percentage does its area increase?", options: ["(20%)", "(40%)", "(44%)", "(144%)"], answer: 2, solution: "The new side factor is (1.2). Area factor is (1.2^2=1.44), so area increases by 44%." }
    ]
  },
  'measurement-units-and-conversion': {
    prerequisites: ['Place value and decimals', 'Fractions and ratios', 'Area and volume'],
    coverage: ['Metric length, mass and capacity', 'Area and volume unit scaling', 'Time and temperature units', 'Compound rates and derived units', 'Conversion factors and dimensional analysis', 'Rounding and measurement precision'],
    theory: html([
      "<h3>Metric units</h3><p>The metric system scales by powers of ten: (1 km=1000 m), (1 m=100 cm), (1 kg=1000 g), and (1 L=1000 mL). Multiply when converting to a smaller unit and divide when converting to a larger unit.</p>",
      "<h3>Area and volume</h3><p>Unit factors are squared for area and cubed for volume: (1 m^2=10,000 cm^2), while (1 m^3=1,000,000 cm^3). Since (1 L=1000 cm^3), a volume conversion cannot use the linear factor alone.</p>",
      "<h3>Rates and precision</h3><p>Write units beside quantities in compound measures, such as (km/h) or (kg/m^3). Convert before combining different units. Keep unrounded intermediate values when accuracy matters, then round the final measurement to the required precision.</p>",
      "<p><strong>Worked example:</strong> Convert (2.4 m^2) to square centimetres. Since (1 m=100 cm), square the factor: (1 m^2=10,000 cm^2); therefore (2.4 m^2=24,000 cm^2).</p>"
    ]),
    tricks: html(["<ul><li>Write the conversion factor as a fraction so unwanted units cancel.</li><li>For squared or cubed units, square or cube the entire linear conversion factor.</li><li>Estimate the order of magnitude to catch misplaced decimal points.</li><li>Convert minutes to hours before using a speed in kilometres per hour.</li><li>Use a consistent precision and round only at the end.</li></ul>"]),
    notes: html(["<ul><li>(1 hour=60 minutes=3600 seconds); (1 day=24 hours).</li><li>(1 hectare=10,000 m^2); (1 km^2=1,000,000 m^2).</li><li>Temperature: (F=(9/5)C+32); temperature differences use (Delta F=(9/5)Delta C).</li><li>Mass and weight are different physical quantities, though everyday contexts may use 'weight' informally.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Convert (3.6 km) to metres.", options: ["(36 m)", "(360 m)", "(3600 m)", "(36,000 m)"], answer: 2, solution: "Multiply by 1000: (3.6 times 1000=3600 m)." },
      { level: 'Standard', prompt: "Convert (0.75 L) to millilitres.", options: ["(75 mL)", "(750 mL)", "(7500 mL)", "(0.075 mL)"], answer: 1, solution: "Since (1 L=1000 mL), (0.75 L=750 mL)." },
      { level: 'Challenge', prompt: "Convert (2.5 m^3) to litres.", options: ["(250 L)", "(2500 L)", "(25,000 L)", "(2,500,000 L)"], answer: 1, solution: "One cubic metre is 1000 litres. Thus (2.5 m^3=2500 L)." }
    ]
  },
  'tables-and-data-interpretation': {
    prerequisites: ['Fractions, ratios and percentages', 'Averages', 'Unit conversion'],
    coverage: ['Read titles, labels, units and footnotes', 'Tables and frequency distributions', 'Bar, line and pie charts', 'Percent change and comparison', 'Weighted totals and averages', 'Multi-step data questions and reasonableness checks'],
    theory: html([
      "<h3>Read the representation first</h3><p>Identify the population, time period, units, scale and whether values are actual counts or percentages. In a grouped table, check whether frequencies are raw counts, cumulative counts or relative frequencies.</p>",
      "<h3>Core calculations</h3><p>Percentage share is (part/whole times 100%). Percentage change is ((new-old)/old times 100%). In a pie chart, a sector angle is (part/whole times 360 degrees). For a frequency table, mean is (sum of value times frequency)/(sum of frequencies).</p>",
      "<h3>Comparisons and estimates</h3><p>Compare like units and denominators. A ratio can be simplified before conversion to percentages. If a graph uses a nonzero baseline or uneven scale, read the axis carefully rather than judging bar heights visually.</p>",
      "<p><strong>Worked example:</strong> A table reports sales of 120 units in January and 150 in February. Increase is 30; percentage increase uses January as the base: (30/120 times 100%=25%).</p>"
    ]),
    tricks: html(["<ul><li>Read the axis scale before extracting a value from a graph.</li><li>Write the denominator explicitly for every percentage.</li><li>For a pie chart, convert a fraction of the total to a 360-degree angle.</li><li>Use weighted rather than simple average when group sizes differ.</li><li>Estimate first and check that the result fits the table's total and units.</li></ul>"]),
    notes: html(["<ul><li>Mean of frequency data: (sum(fx)/sum(f)).</li><li>Percentage-point change is the subtraction of two percentages; percent change divides by the starting value.</li><li>A pie chart's sectors sum to 360 degrees and shares sum to 100%.</li><li>Median requires ordered observations; a table may need cumulative frequencies.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A class has 18 girls and 12 boys. What percentage of the class are girls?", options: ["(40%)", "(50%)", "(60%)", "(66 2/3%)"], answer: 2, solution: "Total is 30. Girls' share is (18/30 times 100%=60%)." },
      { level: 'Standard', prompt: "A value rises from 80 to 100. What is the percentage increase?", options: ["(20%)", "(25%)", "(30%)", "(125%)"], answer: 1, solution: "Increase is 20 relative to the starting value 80: (20/80 times 100%=25%)." },
      { level: 'Challenge', prompt: "Scores 60, 70 and 80 have frequencies 2, 3 and 5. Find the mean.", options: ["(72)", "(73)", "(74)", "(75)"], answer: 1, solution: "Weighted total is (60 times 2+70 times 3+80 times 5=730); frequency total is 10. Mean is 73." }
    ]
  },
  'data-sufficiency': {
    prerequisites: ['Linear equations', 'Ratios and percentages', 'Logical reasoning'],
    coverage: ['Question target and answer choices', 'Sufficiency versus numerical solution', 'Use each statement independently', 'Combine statements only when needed', 'Uniqueness and multiple-solution tests', 'Avoid hidden assumptions and outside information'],
    theory: html([
      "<h3>What sufficiency asks</h3><p>Data-sufficiency questions ask whether the supplied statements determine a unique answer to the target question. You do not need to calculate the answer when a clear uniqueness test is enough.</p>",
      "<h3>Test statements systematically</h3><p>Evaluate statement I alone, then statement II alone, then both together if neither is sufficient. A statement is sufficient only if it produces one answer under all stated conditions. Try distinct valid values to prove insufficiency.</p>",
      "<h3>Information discipline</h3><p>Use only facts stated or standard definitions. Do not assume a variable is positive, an integer, or a particular shape unless the question says so. Check edge cases, zero denominators and ambiguous interpretations.</p>",
      "<p><strong>Worked example:</strong> Asked for integer (x), statement I says (x+y=10), and statement II says (y=4). I alone leaves many pairs; II alone gives no x. Together, (x=6), a unique value, so both are required.</p>"
    ]),
    tricks: html(["<ul><li>Keep the target question visible while testing the statements.</li><li>Use counterexamples to show a statement is insufficient.</li><li>Check whether the requested result is a value, a yes/no decision, or a comparison.</li><li>Do not solve more than the question requires.</li><li>When both statements are combined, confirm there is still only one admissible answer.</li></ul>"]),
    notes: html(["<ul><li>Sufficient means enough to determine exactly one answer, not merely to produce an equation.</li><li>For a yes/no target, all valid cases must lead to the same yes or no.</li><li>For a numerical target, two different possible values prove insufficiency.</li><li>Do not import assumptions absent from the question.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "What is the value of x? I: (x+y=9). II: (y=4).", options: ["I alone is sufficient", "II alone is sufficient", "Both together are sufficient, neither alone is", "Each alone is sufficient"], answer: 2, solution: "I alone permits many pairs and II alone says nothing about x. Together, (x=9-4=5), uniquely." },
      { level: 'Standard', prompt: "Is integer n even? I: (n^2) is even. II: (n) is divisible by 2.", options: ["I alone is sufficient, II alone is not", "II alone is sufficient, I alone is not", "Both are individually sufficient", "Neither is sufficient"], answer: 2, solution: "An integer has an even square exactly when it is even, so statement I answers yes. Statement II directly says n is even. Each statement alone is sufficient." },
      { level: 'Challenge', prompt: "Is (x>0)? I: (x^2=9). II: (x^3>0).", options: ["I alone is sufficient", "II alone is sufficient", "Both together are required", "Neither is sufficient"], answer: 1, solution: "I permits x=3 or x=-3, so it is insufficient. II implies x>0, so II alone is sufficient." }
    ]
  },
  'dispersion-and-standard-deviation': {
    prerequisites: ['Mean, median and mode', 'Fractions and squares', 'Frequency tables'],
    coverage: ['Range and interquartile range', 'Variance and standard deviation', 'Population versus sample convention', 'Grouped-data calculations', 'Effect of shifting and scaling data', 'Interpretation of spread and outliers'],
    theory: html([
      "<h3>Measures of spread</h3><p>Range is maximum minus minimum. Quartiles divide ordered data into four parts; the interquartile range (IQR) is (Q_3-Q_1) and is less affected by extreme values.</p>",
      "<h3>Variance and standard deviation</h3><p>Population variance is the mean squared deviation from the population mean: (sigma^2=sum((x-mu)^2)/N). Population standard deviation is (sigma=sqrt(sigma^2)). For a sample estimate, the common unbiased variance denominator is (n-1); use the convention specified by the problem.</p>",
      "<h3>Interpretation</h3><p>Standard deviation is in the same units as the data; variance is in squared units. Adding a constant shifts the mean but leaves spread unchanged. Multiplying every observation by (k) multiplies standard deviation by (|k|) and variance by (k^2).</p>",
      "<p><strong>Worked example:</strong> For data (2,4,6), mean is 4. Population variance is ((4+0+4)/3=8/3), and population standard deviation is (sqrt(8/3), approximately 1.63).</p>"
    ]),
    tricks: html(["<ul><li>Sort observations before finding range, quartiles or median-based spread.</li><li>Subtract the mean from each observation before squaring deviations.</li><li>Do not confuse population denominator (N) with sample denominator (n-1).</li><li>Use the same data units throughout and report standard deviation in original units.</li><li>For a quick comparison, look at the scale and outliers as well as a single spread statistic.</li></ul>"]),
    notes: html(["<ul><li>Range = maximum - minimum; IQR = upper quartile - lower quartile.</li><li>Variance cannot be negative; standard deviation is its nonnegative square root.</li><li>Adding c to all values: mean shifts by c; variance does not change.</li><li>For equally likely values, population variance can be computed as (mean of squares - square of mean).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Find the range of (4, 9, 11, 15).", options: ["(7)", "(9)", "(11)", "(19)"], answer: 2, solution: "Range is maximum minus minimum: (15-4=11)." },
      { level: 'Standard', prompt: "For data (2,4,6), what is the population variance?", options: ["(4/3)", "(2)", "(8/3)", "(4)"], answer: 2, solution: "Mean is 4; squared deviations are 4, 0 and 4. Divide their sum 8 by 3: variance is (8/3)." },
      { level: 'Challenge', prompt: "If every observation is multiplied by 3, how does its standard deviation change?", options: ["Unchanged", "Multiplied by 3", "Multiplied by 6", "Multiplied by 9"], answer: 1, solution: "Scaling all observations by a factor (k) scales standard deviation by (|k|). Here it is multiplied by 3." }
    ]
  },
  'permutations-and-combinations': {
    prerequisites: ['Factorials and counting principles', 'Fractions', 'Basic probability'],
    coverage: ['Fundamental counting principle', 'Permutations when order matters', 'Combinations when order does not matter', 'Arrangements with repeated objects', 'Circular arrangements', 'Restrictions, cases and overcounting checks'],
    theory: html([
      "<h3>Counting principle and factorials</h3><p>If a task has successive choices with (m) and (n) possibilities, there are (mn) combined outcomes. Factorial is (n!=n(n-1)...1), with (0!=1).</p>",
      "<h3>Order matters: permutations</h3><p>The number of ordered selections of (r) distinct objects from (n) is (nP_r=n!/(n-r)!). For arranging all n distinct objects in a line, there are (n!) orders. With repeated identical objects, divide by each repeated-count factorial.</p>",
      "<h3>Order does not matter: combinations</h3><p>The number of ways to choose r objects from n is (nC_r=n!/(r!(n-r)!)). Each chosen group is counted (r!) times by permutations, so divide by that overcount.</p>",
      "<p><strong>Worked example:</strong> Choose a president and secretary from 8 people: offices differ, so there are (8 times 7=56) assignments. Choose a 2-person committee: order is irrelevant, so (8C_2=28).</p>"
    ]),
    tricks: html(["<ul><li>Ask whether swapping two selected people creates a new outcome.</li><li>Apply restrictions before counting; split into disjoint cases when needed.</li><li>For repeated letters, divide by factorials of identical-letter counts.</li><li>For a circle, rotations are considered the same in an ordinary round-table arrangement.</li><li>Check whether repetition is allowed in each position.</li></ul>"]),
    notes: html(["<ul><li>(nP_r=n!/(n-r)!) and (nC_r=n!/(r!(n-r)!)).</li><li>(nC_r=nC_{n-r}); choosing a group equals choosing who is left out.</li><li>Number of circular arrangements of n distinct people is ((n-1)!).</li><li>For identical objects, divide the total arrangements by the factorial for each repeated type.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "How many ways can 3 different books be arranged on a shelf?", options: ["(3)", "(6)", "(9)", "(27)"], answer: 1, solution: "Order matters. There are (3!=3 times 2 times 1=6) arrangements." },
      { level: 'Standard', prompt: "How many 2-person committees can be selected from 7 people?", options: ["(14)", "(21)", "(42)", "(49)"], answer: 1, solution: "Order does not matter: (7C_2=7 times 6/2=21)." },
      { level: 'Challenge', prompt: "How many distinct arrangements can be made from the letters of LEVEL?", options: ["(20)", "(30)", "(60)", "(120)"], answer: 1, solution: "There are 5 letters with L repeated twice and E repeated twice. Count is (5!/(2!2!)=30)." }
    ]
  },
  'conditional-probability': {
    prerequisites: ['Fractions and ratios', 'Set theory', 'Basic probability'],
    coverage: ['Sample spaces and events', 'Conditional probability', 'Multiplication rule', 'Independent and dependent events', 'Bayes theorem and reverse conditioning', 'Tree tables and without-replacement problems'],
    theory: html([
      "<h3>Conditional probability</h3><p>The probability of A given B is (P(A|B)=P(A intersect B)/P(B)), provided (P(B)>0). Conditioning restricts the sample space to outcomes where B occurred.</p>",
      "<h3>Multiplication and independence</h3><p>The multiplication rule is (P(A intersect B)=P(A|B)P(B)). Events are independent when (P(A|B)=P(A)); equivalently, (P(A intersect B)=P(A)P(B)). Drawing without replacement generally makes successive outcomes dependent.</p>",
      "<h3>Bayes theorem</h3><p>For mutually exclusive and exhaustive causes (B_i), (P(B_j|A)=P(A|B_j)P(B_j)/sum_i P(A|B_i)P(B_i)). Separate prior probability from the likelihood of the observed evidence.</p>",
      "<p><strong>Worked example:</strong> A bag has 3 red and 2 blue balls. Without replacement, after drawing a red ball, 2 red remain among 4 balls. Thus the probability the next ball is red, given the first was red, is (2/4=1/2).</p>"
    ]),
    tricks: html(["<ul><li>Rewrite the condition in words: the denominator is the event already known to have occurred.</li><li>Use a tree diagram for sequential events and label branch probabilities at each stage.</li><li>For without replacement, update counts after each draw.</li><li>For reverse-conditioning questions, use Bayes theorem and include all possible causes in the denominator.</li><li>Check probabilities remain between 0 and 1 and branch totals equal 1.</li></ul>"]),
    notes: html(["<ul><li>(P(A|B)=P(A intersect B)/P(B)).</li><li>Independent events satisfy (P(A intersect B)=P(A)P(B)).</li><li>Mutually exclusive events with positive probabilities are not independent.</li><li>Complement: (P(A^c)=1-P(A)).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A card is known to be a face card in a standard deck. What is the probability it is a king?", options: ["(1/13)", "(1/4)", "(1/3)", "(4/13)"], answer: 2, solution: "There are 12 face cards (J, Q, K) and 4 are kings. The conditional probability is (4/12=1/3)." },
      { level: 'Standard', prompt: "A bag has 4 green and 3 yellow balls. Two are drawn without replacement. Given the first is green, what is the probability the second is green?", options: ["(1/2)", "(3/7)", "(2/3)", "(4/7)"], answer: 0, solution: "After a green is removed, 3 green remain among 6 balls. Probability is (3/6=1/2)." },
      { level: 'Challenge', prompt: "A disease affects 1% of a population. A test is positive for 90% of affected people and 5% of unaffected people. Given a positive result, what is the probability of disease?", options: ["(2/13)", "(9/59)", "(1/2)", "(9/10)"], answer: 0, solution: "Bayes numerator is (0.01 times 0.90=0.009). Positive probability is (0.009+0.99 times 0.05=0.0585). Thus the probability is (0.009/0.0585=2/13)." }
    ]
  },
  'set-theory-and-venn-diagrams': {
    prerequisites: ['Fractions and percentages', 'Basic counting', 'Logical statements'],
    coverage: ['Set membership and notation', 'Union, intersection and complement', 'Subset and universal set', 'Two-set and three-set inclusion-exclusion', 'Venn diagram counts', 'Applications to survey and classification data'],
    theory: html([
      "<h3>Set language</h3><p>A set is a collection of distinct elements. (x in A) means x belongs to A; (A subset B) means every element of A is also in B. The universal set contains all elements under discussion. The complement (A^c) consists of universal elements not in A.</p>",
      "<h3>Operations</h3><p>Union (A union B) includes elements in either set; intersection (A intersect B) includes elements in both. For finite sets, (n(A union B)=n(A)+n(B)-n(A intersect B)); subtract the overlap once because it was counted twice.</p>",
      "<h3>Three sets</h3><p>For three sets, add the individual sizes, subtract each pairwise intersection, then add the triple intersection once. A Venn diagram helps separate 'only A', pair-only regions, the centre overlap, and neither.</p>",
      "<p><strong>Worked example:</strong> In a group of 40, 24 study A, 18 study B, and 7 study both. At least one is (24+18-7=35), so neither is (40-35=5).</p>"
    ]),
    tricks: html(["<ul><li>Fill the centre overlap first when solving a Venn diagram from totals.</li><li>Distinguish 'A or B' inclusive union from exclusive-or wording.</li><li>Use the total universe to find the 'neither' region.</li><li>For three sets, add the triple intersection back after subtracting pairwise overlaps.</li><li>Check that every disjoint region sums to the stated total.</li></ul>"]),
    notes: html(["<ul><li>(n(A union B)=n(A)+n(B)-n(A intersect B)).</li><li>(n(A^c)=n(U)-n(A)).</li><li>If (A subset B), then (A intersect B=A) and (A union B=B).</li><li>For disjoint sets, intersection size is zero.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "If (n(A)=20), (n(B)=15), and (n(A intersect B)=5), find (n(A union B)).", options: ["(25)", "(30)", "(35)", "(40)"], answer: 1, solution: "Use inclusion-exclusion: (20+15-5=30)." },
      { level: 'Standard', prompt: "In a class of 50, 28 study Hindi, 22 study English and 10 study both. How many study neither?", options: ["(8)", "(10)", "(12)", "(18)"], answer: 1, solution: "At least one is (28+22-10=40). Neither is (50-40=10)." },
      { level: 'Challenge', prompt: "In a group of 30, (n(A)=16), (n(B)=14), (n(A intersect B)=6). How many are in A only?", options: ["(6)", "(8)", "(10)", "(16)"], answer: 2, solution: "A only is (n(A)-n(A intersect B)=16-6=10)." }
    ]
  },
  'number-series': {
    prerequisites: ['Four operations', 'Factors and multiples', 'Squares and powers'],
    coverage: ['Constant and changing differences', 'Constant ratios and geometric patterns', 'Alternating and interleaved series', 'Squares, cubes, primes and figurate numbers', 'Recursive and mixed-operation rules', 'Missing-term verification and ambiguity awareness'],
    theory: html([
      "<h3>Systematic pattern search</h3><p>For a sequence (a_1,a_2,...), first calculate consecutive differences. Constant first differences indicate an arithmetic sequence; constant second differences indicate a quadratic pattern. If differences do not help, test ratios, alternating subsequences, or operations applied term by term.</p>",
      "<h3>Familiar number families</h3><p>Recognise squares (1,4,9,...), cubes, primes, triangular numbers, powers of 2 and factorials. Some series interleave two simple patterns at odd and even positions, so separate positions before assuming one rule.</p>",
      "<h3>Check the rule</h3><p>A proposed rule should explain every given transition and produce one consistent missing term. Short series can support multiple rules; prefer the simplest rule consistent with all terms and the exam's stated convention.</p>",
      "<p><strong>Worked example:</strong> In (2,5,10,17,26,...), the differences are 3,5,7,9. The next difference is 11, so the next term is (26+11=37). Equivalently, terms are (n^2+1) beginning at (n=1).</p>"
    ]),
    tricks: html(["<ul><li>Write the difference row explicitly; do not rely on visual intuition.</li><li>For alternating patterns, compare terms two positions apart.</li><li>Check multiplication and addition together, such as (times 2, then add 1).</li><li>Test the rule against all terms, not only the final pair.</li><li>If a series is underdetermined, state the simplest conventional pattern used.</li></ul>"]),
    notes: html(["<ul><li>AP: constant first difference; quadratic pattern: constant second difference.</li><li>Geometric sequence: constant ratio between consecutive nonzero terms.</li><li>Triangular number (T_n=n(n+1)/2).</li><li>Squares have successive differences 3, 5, 7, 9, ...</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Find the next term: (7, 12, 17, 22, ...).", options: ["(25)", "(26)", "(27)", "(28)"], answer: 2, solution: "The common difference is 5. Next term is (22+5=27)." },
      { level: 'Standard', prompt: "Find the next term: (3, 6, 12, 24, ...).", options: ["(36)", "(42)", "(48)", "(54)"], answer: 2, solution: "Each term is multiplied by 2, so the next term is (24 times 2=48)." },
      { level: 'Challenge', prompt: "Find the next term: (1, 4, 10, 20, 35, ...).", options: ["(49)", "(50)", "(54)", "(56)"], answer: 3, solution: "Differences are 3, 6, 10, 15, which increase by 3, 4, 5; next difference is 21. Thus (35+21=56)." }
    ]
  },
  'quantity-comparison': {
    prerequisites: ['Fractions and decimals', 'Ratios and percentages', 'Linear inequalities'],
    coverage: ['Compare signed numbers and fractions', 'Use common denominators and cross multiplication', 'Compare ratios and percentages', 'Estimate without full computation', 'Algebraic quantities and domain conditions', 'Equality, insufficiency and range cases'],
    theory: html([
      "<h3>Numerical comparisons</h3><p>To compare fractions with positive denominators, use a common denominator or cross multiplication. For decimals, align place values. For negative values, the number closer to zero is greater.</p>",
      "<h3>Ratios, rates and percentages</h3><p>Convert quantities to common units before comparing. Compare a rate using the same denominator or calculate unit rates. A percent is a fraction out of 100, so percent comparisons depend on their stated bases.</p>",
      "<h3>Algebraic comparisons</h3><p>When quantities contain variables, record the domain and sign assumptions first. A comparison may vary with the variable; test critical values or derive an inequality. Do not choose one quantity as greater from a single convenient example.</p>",
      "<p><strong>Worked example:</strong> Compare (3/7) and (4/9). Cross products are (3 times 9=27) and (4 times 7=28), so (3/7<4/9).</p>"
    ]),
    tricks: html(["<ul><li>Check units before comparing distances, prices or rates.</li><li>For positive fractions, cross multiply; if denominators can be negative, first account for their signs.</li><li>Estimate nearby benchmark values such as (1/2), 1 and 100%.</li><li>For variable expressions, test boundaries and sign changes rather than one sample value.</li><li>Keep equality as a possible outcome unless strict inequality is proved.</li></ul>"]),
    notes: html(["<ul><li>If (a,b>0), then (a/b<c/d) exactly when (ad<bc).</li><li>Multiplying both sides of an inequality by a negative quantity reverses its direction.</li><li>Unit price = total price divided by number or measure of units.</li><li>Percent increase and decrease use the original amount as the base.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Which fraction is greater: (5/8) or (3/5)?", options: ["(5/8)", "(3/5)", "They are equal", "Cannot be determined"], answer: 0, solution: "Cross products are (5 times 5=25) and (3 times 8=24). Therefore (5/8>3/5)." },
      { level: 'Standard', prompt: "Which is the better unit price: 750 g for Rs 90 or 1 kg for Rs 116?", options: ["750 g pack", "1 kg pack", "Same price per kg", "Cannot be compared"], answer: 1, solution: "First pack costs (90/0.75=Rs 120) per kg; the second costs Rs 116 per kg, so the 1 kg pack is cheaper." },
      { level: 'Challenge', prompt: "For positive x, compare (x/(x+1)) with (1/2).", options: ["First is always greater", "Second is always greater", "They are equal only at x=1", "The comparison cannot be determined"], answer: 3, solution: "Compare by multiplying by the positive quantity (2(x+1)): the first is greater exactly when (2x>x+1), or (x>1). They are equal at x=1 and the second is greater for (0<x<1), so no fixed ordering holds." }
    ]
  },
  'mathematical-operations-and-symbols': {
    prerequisites: ['Integers and rational numbers', 'Order of operations', 'Algebraic substitution'],
    coverage: ['Meaning of arithmetic and comparison symbols', 'Grouping and operation precedence', 'Absolute value and modulus', 'Exponent and root notation', 'Coded or defined operations', 'Reading compound expressions accurately'],
    theory: html([
      "<h3>Symbols and grouping</h3><p>Parentheses, brackets and fraction bars group expressions. Exponentiation is evaluated before multiplication and addition; multiplication and division have equal precedence and are handled left to right, as are addition and subtraction. A fraction bar groups its entire numerator and denominator.</p>",
      "<h3>Absolute value and relations</h3><p>Absolute value (|x|) is distance from zero, so it is nonnegative: (|x|=x) for (x ge 0) and (|x|=-x) for (x<0). Symbols such as (<, ge, neq) compare values rather than perform arithmetic.</p>",
      "<h3>Defined operations</h3><p>A question may define a new operation, for example (a star b=a^2+b). Use that definition exactly; it does not inherit familiar arithmetic properties unless they can be proved.</p>",
      "<p><strong>Worked example:</strong> With (a star b=2a-b), evaluate ((3 star 1) star 2). First (3 star 1=5); then (5 star 2=8). The operation is not assumed associative.</p>"
    ]),
    tricks: html(["<ul><li>Rewrite complex expressions with explicit parentheses before calculating.</li><li>Use the defined-operation rule at every occurrence, including nested expressions.</li><li>Evaluate absolute value only after finding the sign of its contents.</li><li>Do not cancel terms across addition; cancellation applies to common factors.</li><li>Check whether a symbol is a relation, operation, unit or grouping mark.</li></ul>"]),
    notes: html(["<ul><li>Standard precedence: grouping, exponents/roots, multiplication/division left to right, addition/subtraction left to right.</li><li>(|a-b|) is the distance between numbers a and b on the number line.</li><li>(a^0=1) for (a neq 0); zero to the zeroth power is not universally defined in elementary contexts.</li><li>For signed integers, subtraction is addition of the additive inverse.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Evaluate (18-6 div 3 times 2).", options: ["(8)", "(14)", "(16)", "(18)"], answer: 1, solution: "Division and multiplication are evaluated left to right: (6 div 3=2), then (2 times 2=4); finally (18-4=14)." },
      { level: 'Standard', prompt: "If (a star b=a^2-b), find (3 star 4).", options: ["(1)", "(5)", "(9)", "(13)"], answer: 1, solution: "Apply the definition: (3 star 4=3^2-4=9-4=5)." },
      { level: 'Challenge', prompt: "Solve (|x-4|=3).", options: ["(x=1 only)", "(x=7 only)", "(x=1 or x=7)", "(x=-1 or x=7)"], answer: 2, solution: "Absolute value 3 means (x-4=3) or (x-4=-3). Thus (x=7) or (x=1)." }
    ]
  },
  'clocks-and-calendars': {
    prerequisites: ['Fractions and ratios', 'Angles', 'Time-unit conversion'],
    coverage: ['Clock-face angles and hand speeds', 'Relative movement of clock hands', 'Elapsed time and 12/24-hour notation', 'Leap-year rules', 'Odd days and weekday shifts', 'Date arithmetic and calendar constraints'],
    theory: html([
      "<h3>Clock angles</h3><p>The minute hand turns 6 degrees per minute; the hour hand turns 0.5 degrees per minute. At h hours and m minutes, their angular positions from 12 are (30h+0.5m) and (6m) degrees. The smaller angle is the lesser of their absolute difference and (360 degrees minus that difference).</p>",
      "<h3>Elapsed time</h3><p>Convert times to minutes from a common reference or use 24-hour notation to cross noon and midnight safely. A 12-hour clock repeats its face, so attach AM/PM when the context requires it.</p>",
      "<h3>Calendar arithmetic</h3><p>An ordinary year has 365 days, or 1 odd day beyond 52 weeks; a leap year has 366 days, or 2 odd days. In the Gregorian calendar, a year divisible by 4 is a leap year except century years, which must be divisible by 400.</p>",
      "<p><strong>Worked example:</strong> At 3:20, the minute hand is at (120 degrees) and the hour hand at (90+10=100 degrees). The smaller angle is 20 degrees.</p>"
    ]),
    tricks: html(["<ul><li>For clock angles, include the hour hand's movement during the minutes elapsed.</li><li>Take the smaller of the two angles around the dial.</li><li>For weekdays, reduce elapsed days modulo 7.</li><li>Apply the century exception when checking leap years.</li><li>Convert a finish time after midnight to the next calendar day before subtracting.</li></ul>"]),
    notes: html(["<ul><li>Minute hand speed is (6 degrees/min); hour hand speed is (0.5 degrees/min).</li><li>Relative hand speed is (5.5 degrees/min).</li><li>Gregorian leap year: divisible by 4, except century years unless divisible by 400.</li><li>A date shifted by seven days falls on the same weekday.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "How many odd days are in an ordinary 365-day year?", options: ["(0)", "(1)", "(2)", "(5)"], answer: 1, solution: "There are 52 complete weeks and 1 extra day, so one odd day." },
      { level: 'Standard', prompt: "Find the smaller angle between the clock hands at 2:30.", options: ["(75 degrees)", "(90 degrees)", "(105 degrees)", "(120 degrees)"], answer: 2, solution: "Minute hand is at 180 degrees; hour hand is at (60+15=75) degrees. The difference is 105 degrees." },
      { level: 'Challenge', prompt: "Is the year 2100 a leap year in the Gregorian calendar?", options: ["Yes, because it is divisible by 4", "No, because it is a century not divisible by 400", "Yes, because all century years are leap years", "No, because it is not divisible by 4"], answer: 1, solution: "Century years must be divisible by 400. Since 2100 is divisible by 100 but not 400, it is not a leap year." }
    ]
  },
  'logical-numerical-reasoning': {
    prerequisites: ['Number system', 'Ratios and percentages', 'Sequences', 'Basic logic'],
    coverage: ['Numerical analogies and classification', 'Series and missing-number patterns', 'Arithmetic logic and coded rules', 'Order, ranking and constraints', 'Data-based deductions', 'Proof by checking alternatives and conditions'],
    theory: html([
      "<h3>Translate the task</h3><p>Numerical reasoning combines calculation with rule discovery. Identify whether the task asks for a value, a pattern, an order or a conclusion. Record given facts and constraints before testing answer choices.</p>",
      "<h3>Pattern and relationship reasoning</h3><p>For analogies, determine the exact operation linking the first pair and apply it to the second pair. For classifications, state a property shared by all members of one group and absent from the other. For number grids, inspect rows, columns and diagonals in turn.</p>",
      "<h3>Constraint reasoning</h3><p>Represent order conditions with inequalities or a short table. If P is before Q and Q before R, then P is before R by transitivity. Use every condition and reject any arrangement that violates even one.</p>",
      "<p><strong>Worked example:</strong> In a number analogy, (4 maps to 19) by the rule (n^2+3). Applying the same rule to 5 gives (25+3=28). Verify the rule against every provided pair before using it.</p>"
    ]),
    tricks: html(["<ul><li>Test simple operations and their order before trying complex formulas.</li><li>For a grid, make one hypothesis and check it across every row or column.</li><li>Translate words like 'at least', 'exactly' and 'before' into precise constraints.</li><li>Use answer choices to verify a rule, but do not force a rule that fits only one example.</li><li>Separate necessary conclusions from possibilities that could be true.</li></ul>"]),
    notes: html(["<ul><li>If (A<B) and (B<C), then (A<C).</li><li>In an ordering with distinct ranks, a position count is not the same as a value difference.</li><li>Odd/even, divisibility, digit sum and place value are common numerical properties.</li><li>A valid pattern must satisfy all supplied terms and conditions.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Complete the analogy: (6:36 :: 9:?).", options: ["(45)", "(54)", "(72)", "(81)"], answer: 3, solution: "The relation is squaring: (6^2=36). Therefore (9^2=81)." },
      { level: 'Standard', prompt: "A is taller than B, B is taller than C, and D is taller than A. Who is tallest?", options: ["A", "B", "C", "D"], answer: 3, solution: "The conditions give (D>A>B>C), so D is tallest." },
      { level: 'Challenge', prompt: "A two-digit number has digit sum 11. Reversing its digits increases it by 27. What is the original number?", options: ["(38)", "(47)", "(56)", "(65)"], answer: 1, solution: "Let tens and units digits be a,b. Then (a+b=11). Reversal difference is (9(b-a)=27), so (b-a=3). Solving gives (a=4,b=7), hence 47." }
    ]
  },
  'addition-subtraction-multiplication-division': {
    prerequisites: ['Whole numbers and place value', 'Signed numbers', 'Fractions and decimals'],
    coverage: ['Place-value algorithms for four operations', 'Regrouping and estimation', 'Signed-number rules', 'Properties and operation order', 'Division with quotient and remainder', 'Fractions, decimals and checking inverse operations'],
    theory: html([
      "<h3>Four operations and place value</h3><p>Add and subtract by aligning place-value columns. Multiplication distributes over addition: (a(b+c)=ab+ac). Division asks how many equal groups or how many units fit; for integers, (a=bq+r) with (0 le r<b) when (b>0).</p>",
      "<h3>Signed numbers</h3><p>Adding a negative is subtraction. Subtracting a negative is addition. For multiplication and division, equal signs give a positive result and different signs give a negative result. Division by zero is undefined.</p>",
      "<h3>Fractions and decimals</h3><p>Add fractions using a common denominator. Multiply numerators and denominators; for division, multiply by the reciprocal of a nonzero divisor. Convert terminating decimals to fractions by place value when useful.</p>",
      "<p><strong>Worked example:</strong> Evaluate (18-2 times (3+4)). First the bracket gives 7, then multiplication gives 14, and subtraction gives 4. Estimate and reverse operations to check arithmetic.</p>"
    ]),
    tricks: html(["<ul><li>Estimate the size and sign of the answer before calculating exactly.</li><li>Align decimal points for addition and subtraction; preserve place value when multiplying.</li><li>For division, check using (dividend=divisor times quotient+remainder).</li><li>Reduce fractions before multiplying to keep numbers small.</li><li>Follow operation precedence and use parentheses to remove ambiguity.</li></ul>"]),
    notes: html(["<ul><li>Commutative: addition and multiplication; subtraction and division are not commutative.</li><li>Associative: addition and multiplication; grouping matters for subtraction and division.</li><li>Distributive law: (a(b+c)=ab+ac).</li><li>For nonzero a, (a/a=1); zero has no reciprocal.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Evaluate (-8)+13.", options: ["(-21)", "(-5)", "(5)", "(21)"], answer: 2, solution: "Starting at -8 and moving 13 units right gives 5." },
      { level: 'Standard', prompt: "Calculate (3/4 div 2/5).", options: ["(3/10)", "(5/6)", "(15/8)", "(8/15)"], answer: 2, solution: "Divide by a fraction by multiplying by its reciprocal: (3/4 times 5/2=15/8)." },
      { level: 'Challenge', prompt: "When 157 is divided by 12, what are the quotient and remainder?", options: ["(q=12,r=13)", "(q=13,r=1)", "(q=13,r=13)", "(q=14,r=-11)"], answer: 1, solution: "(12 times 13+1=157), and the remainder 1 satisfies (0 le 1<12)." }
    ]
  },
  'money-and-everyday-arithmetic': {
    prerequisites: ['Four operations', 'Decimals and percentages', 'Unit conversion'],
    coverage: ['Money notation and decimal arithmetic', 'Budgets, totals and change', 'Unit price and best buys', 'Discount, tax and sale price', 'Simple interest and payment totals', 'Rounding, estimation and financial reasonableness'],
    theory: html([
      "<h3>Everyday calculations</h3><p>Keep money values in one currency and align decimal places when adding or subtracting. A budget compares income with expenses; balance is income minus spending. For repeated purchases, multiply the price per item by the quantity.</p>",
      "<h3>Unit price and sale price</h3><p>Unit price is (total price/quantity). Discount amount is (discount rate times marked price), and sale price is (marked price times (1-discount rate)). Tax is calculated using the base specified by the problem; add it after discount only when the stated rules say so.</p>",
      "<h3>Interest and installments</h3><p>Simple interest is (I=Prt) when rate is expressed as a decimal and time units match the rate period. Total repayment is principal plus interest; any installment calculation must also consider the number and timing of payments if specified.</p>",
      "<p><strong>Worked example:</strong> An item marked Rs 2,000 has a 15% discount. Discount is (0.15 times 2000=Rs 300); sale price before any separately stated tax is Rs 1,700.</p>"
    ]),
    tricks: html(["<ul><li>Compare unit prices only after converting quantities to the same unit.</li><li>Calculate percentage discount from the marked price unless another base is stated.</li><li>Keep discount, tax and final payment as separate steps.</li><li>Estimate a total before exact calculation to catch misplaced decimals.</li><li>For simple interest, convert months to years when the annual rate is used.</li></ul>"]),
    notes: html(["<ul><li>Sale price = marked price - discount.</li><li>Simple interest: (I=Prt); amount: (A=P+I).</li><li>A percentage is a rate per 100; 18% = 0.18.</li><li>Round currency to the smallest permitted unit only at the final step.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A customer buys items costing Rs 38.50 and Rs 24.75 and pays Rs 100. How much change is due?", options: ["(Rs 26.25)", "(Rs 36.75)", "(Rs 37.25)", "(Rs 38.75)"], answer: 1, solution: "Total is (38.50+24.75=Rs 63.25). Change is (100-63.25=Rs 36.75)." },
      { level: 'Standard', prompt: "A Rs 1,500 item is discounted by 20%. Find its sale price before tax.", options: ["(Rs 1,100)", "(Rs 1,200)", "(Rs 1,250)", "(Rs 1,300)"], answer: 1, solution: "Discount is (0.20 times 1500=Rs 300). Sale price is (1500-300=Rs 1,200)." },
      { level: 'Challenge', prompt: "Find simple interest on Rs 8,000 at 7.5% per year for 2 years.", options: ["(Rs 600)", "(Rs 1,000)", "(Rs 1,200)", "(Rs 1,500)"], answer: 2, solution: "(I=Prt=8000 times 0.075 times 2=Rs 1,200)." }
    ]
  },
  'time-and-measurement': {
    prerequisites: ['Place value and unit conversion', 'Fractions and decimals', 'Four operations'],
    coverage: ['Elapsed time and time intervals', 'Length, mass and capacity', 'Area and volume units', 'Temperature and scale reading', 'Precision, estimation and instrument resolution', 'Compound measures and unit consistency'],
    theory: html([
      "<h3>Time intervals</h3><p>Convert hours and minutes to one unit before adding or subtracting. A duration crossing midnight must include the date change. For a rate such as speed, express time in the unit required by the rate.</p>",
      "<h3>Measure and convert</h3><p>Length, mass and capacity use scaled units. Area conversion factors are squared and volume conversion factors are cubed. Read a measuring instrument from its scale divisions, including the correct unit and sensible precision.</p>",
      "<h3>Accuracy and estimation</h3><p>Measurements are approximate to an instrument's resolution. Do not report more precision than the data supports. Estimate first to catch impossible results, then calculate and round as directed.</p>",
      "<p><strong>Worked example:</strong> A journey takes 1 hour 45 minutes. In minutes, this is (60+45=105 minutes); at (60 km/h), that duration is (1.75 hours), so distance is (60 times 1.75=105 km).</p>"
    ]),
    tricks: html(["<ul><li>Convert to a common unit before comparing or combining measurements.</li><li>For elapsed time, use a timeline or convert both times to minutes from midnight.</li><li>Label every answer with its unit.</li><li>Square or cube a linear conversion factor when changing area or volume.</li><li>Round only as instructed and retain guard digits in intermediate work.</li></ul>"]),
    notes: html(["<ul><li>(1 h=60 min), (1 min=60 s), (1 kg=1000 g), (1 L=1000 mL).</li><li>(1 m^2=10,000 cm^2) and (1 m^3=1,000,000 cm^3).</li><li>Speed = distance/time; density = mass/volume.</li><li>For Celsius and Fahrenheit, (F=(9/5)C+32).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "How many minutes are in 2 hours 35 minutes?", options: ["(125)", "(135)", "(155)", "(235)"], answer: 2, solution: "(2 times 60+35=155) minutes." },
      { level: 'Standard', prompt: "A container holds 2.4 L. How many millilitres is this?", options: ["(24 mL)", "(240 mL)", "(2400 mL)", "(24,000 mL)"], answer: 2, solution: "Multiply by 1000: (2.4 times 1000=2400 mL)." },
      { level: 'Challenge', prompt: "A vehicle travels 150 km in 2 hours 30 minutes. Find its average speed.", options: ["(50 km/h)", "(55 km/h)", "(60 km/h)", "(75 km/h)"], answer: 2, solution: "Time is (2.5 h). Average speed is (150/2.5=60 km/h)." }
    ]
  },
  'patterns-and-sequences-school-mathematics': {
    prerequisites: ['Whole-number operations', 'Multiplication tables', 'Basic algebra'],
    coverage: ['Repeating, growing and shrinking patterns', 'Visual and shape patterns', 'Input-output tables', 'Recursive and position rules', 'Linear and quadratic growth', 'Generalising patterns with words, symbols and diagrams'],
    theory: html([
      "<h3>Notice and describe</h3><p>A pattern is an arrangement or sequence with a rule. Students can describe what changes, what stays constant and how one stage relates to the next. Patterns may repeat, grow, shrink, alternate or combine rules.</p>",
      "<h3>From cases to a general rule</h3><p>Record stage number and output in a table. Constant first differences suggest a linear rule; constant second differences suggest a quadratic rule. A recursive rule describes how to get the next term; an explicit rule gives a term directly from its position.</p>",
      "<h3>Visual patterns</h3><p>Count tiles, dots, matchsticks or other units in early stages, then separate fixed parts from repeated additions. Draw or explain why the rule works so that the formula reflects the structure rather than only fitting a few data points.</p>",
      "<p><strong>Worked example:</strong> A row of joined squares uses 4 matchsticks for one square and 3 more for each additional square. For n squares in a row, the count is (4+3(n-1)=3n+1).</p>"
    ]),
    tricks: html(["<ul><li>Show at least three stages so a repeating or alternating rule becomes visible.</li><li>Use a table to connect stage number to count.</li><li>Distinguish 'add 3 each time' from 'multiply by 3 each time'.</li><li>Check an explicit formula against the first and a later stage.</li><li>Invite a diagram or verbal explanation to test whether a rule is meaningful.</li></ul>"]),
    notes: html(["<ul><li>Constant first difference corresponds to a linear sequence.</li><li>Constant second difference corresponds to a quadratic sequence.</li><li>Recursive rule needs an initial term and a rule for the next term.</li><li>Several formulas may fit a short list; additional stages or structural reasoning can distinguish them.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A pattern has 5 dots in stage 1 and adds 4 dots each stage. How many dots are in stage 4?", options: ["(13)", "(15)", "(17)", "(20)"], answer: 2, solution: "Stages are 5, 9, 13, 17; stage 4 has 17 dots." },
      { level: 'Standard', prompt: "A matchstick pattern of joined squares follows (3n+1). How many matchsticks are needed for 8 squares?", options: ["(24)", "(25)", "(27)", "(32)"], answer: 1, solution: "Substitute (n=8): (3 times 8+1=25) matchsticks." },
      { level: 'Challenge', prompt: "The sequence is (2, 6, 12, 20, ...). Which rule gives its nth term?", options: ["(n^2+1)", "(n(n+1))", "(2n+1)", "(2^n)"], answer: 1, solution: "For (n=1,2,3,4), (n(n+1)) gives 2, 6, 12 and 20." }
    ]
  },
  'shapes-and-spatial-understanding': {
    prerequisites: ['Position and direction', 'Lines and angles', '2D and 3D shape vocabulary'],
    coverage: ['Classifying 2D shapes by properties', 'Polygons, circles and symmetry', '3D solids and their nets', 'Position, direction and coordinate language', 'Congruence, similarity and transformations', 'Spatial reasoning through construction and visualisation'],
    theory: html([
      "<h3>Shape properties and classification</h3><p>Classify figures using defining properties rather than appearance. A polygon is a closed plane figure made of straight segments. Quadrilaterals can be grouped by parallel sides, equal sides, right angles and symmetry; categories can overlap, such as a square being both a rectangle and a rhombus.</p>",
      "<h3>Three-dimensional objects</h3><p>Prisms have two congruent parallel bases; pyramids have one base and triangular faces meeting at an apex. A cylinder has two circular bases and one curved surface; a cone has one circular base and an apex. Nets show faces before folding.</p>",
      "<h3>Transformations and scale</h3><p>Translation slides, rotation turns and reflection flips a figure. These rigid transformations preserve lengths and angles. Similar figures have equal corresponding angles and proportional corresponding sides; congruent figures are the same shape and size.</p>",
      "<p><strong>Worked example:</strong> A rectangle with side lengths 3 cm and 5 cm has area 15 cm^2 and perimeter 16 cm. A scale factor of 2 makes corresponding lengths 6 cm and 10 cm, perimeter 32 cm, and area 60 cm^2.</p>"
    ]),
    tricks: html(["<ul><li>Ask which property defines a class and which properties are only typical examples.</li><li>Use a fold, tracing or dynamic diagram to test symmetry and congruence.</li><li>Distinguish a prism's two matching bases from its lateral faces.</li><li>Use the same orientation and units when comparing corresponding sides.</li><li>Let learners build, draw, describe and then formalise a shape relationship.</li></ul>"]),
    notes: html(["<ul><li>A rectangle has four right angles; a rhombus has four equal sides; a square has both sets of properties.</li><li>Congruent figures have equal corresponding lengths and angles.</li><li>Similar figures preserve angle measures and use one scale factor for all corresponding lengths.</li><li>Euler's relation for a convex polyhedron is (V-E+F=2).</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Which property is shared by every rectangle?", options: ["All four sides are equal", "Opposite sides are equal and all angles are right angles", "Exactly one pair of parallel sides", "No parallel sides"], answer: 1, solution: "A rectangle has two pairs of equal opposite sides and four right angles." },
      { level: 'Standard', prompt: "A similar triangle has a side corresponding to 6 cm on a 4 cm side. What is the scale factor from the first triangle to the second?", options: ["(2/3)", "(3/2)", "(2)", "(10)"], answer: 1, solution: "Scale factor is corresponding new length divided by original: (6/4=3/2)." },
      { level: 'Challenge', prompt: "A convex polyhedron has 8 vertices and 12 edges. How many faces does it have?", options: ["(4)", "(6)", "(8)", "(12)"], answer: 1, solution: "Euler's relation is (V-E+F=2). Thus (8-12+F=2), so (F=6)." }
    ]
  },
  'data-handling-school-mathematics': {
    prerequisites: ['Counting and fractions', 'Tables and graphs', 'Mean, median and mode'],
    coverage: ['Collecting and classifying data', 'Tally marks and frequency tables', 'Bar, pictograph, line and circle graphs', 'Mean, median, mode and range', 'Chance language and simple probability', 'Questioning samples, scale and misleading displays'],
    theory: html([
      "<h3>From question to data</h3><p>Decide what variable is being measured, who or what is included, and whether values are categories or numerical measurements. A sample should represent the population fairly; convenience samples can bias conclusions.</p>",
      "<h3>Organising and displaying</h3><p>Tally and frequency tables count observations. Bar graphs compare categories; line graphs show change across an ordered scale such as time; pictographs use a key; circle graphs show parts of a whole. Choose a display that matches the data and label axes, units and scale.</p>",
      "<h3>Summaries and chance</h3><p>Mean uses every value and is sensitive to extremes; median is the middle ordered value; mode is the most frequent value. Range describes the full spread. For equally likely outcomes, probability is (favourable outcomes/total outcomes).</p>",
      "<p><strong>Worked example:</strong> For scores (2,3,3,7,10), mean is 5, median is 3, mode is 3 and range is 8. The high score affects the mean more than the median.</p>"
    ]),
    tricks: html(["<ul><li>Read graph keys and scales before interpreting visual height or area.</li><li>Sort data before finding the median and state how an even count is handled.</li><li>Use a frequency table to avoid recounting raw observations.</li><li>Ask who was excluded from the sample and whether the sample is representative.</li><li>Compare the mean and median when data contain outliers.</li></ul>"]),
    notes: html(["<ul><li>Mean = total of values divided by number of observations.</li><li>Median is the middle ordered value, or mean of two middle values for an even count.</li><li>Probability lies from 0 to 1; impossible = 0 and certain = 1.</li><li>A fair graph needs clear labels, consistent intervals and an honest baseline.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Find the median of (3, 5, 8, 10, 14).", options: ["(5)", "(8)", "(9)", "(10)"], answer: 1, solution: "The five ordered observations have middle value 8." },
      { level: 'Standard', prompt: "A fair six-sided die is rolled once. What is the probability of rolling an even number?", options: ["(1/6)", "(1/3)", "(1/2)", "(2/3)"], answer: 2, solution: "Even outcomes are 2, 4 and 6: (3/6=1/2)." },
      { level: 'Challenge', prompt: "Which measure is usually least affected by one extremely high observation?", options: ["Mean", "Median", "Range", "Maximum"], answer: 1, solution: "The median depends on the middle position in ordered data and is generally more resistant to an extreme value than the mean." }
    ]
  },
  'nature-and-logical-thinking-in-mathematics': {
    prerequisites: ['Patterns and sequences', 'Mathematical language', 'Basic problem solving'],
    coverage: ['Mathematics as a system of relationships and structures', 'Inductive pattern exploration', 'Conjectures, examples and counterexamples', 'Deductive reasoning and proof', 'Problem-solving strategies and reflection', 'Reasoning, communication and multiple solution paths'],
    theory: html([
      "<h3>Mathematical thinking</h3><p>Mathematics studies quantities, structures, patterns, space and change through precise definitions and justified relationships. A mathematical answer includes reasoning that explains why it follows from the assumptions.</p>",
      "<h3>Explore and justify</h3><p>Inductive reasoning uses examples to form a conjecture; examples can suggest a rule but cannot establish a universal statement. A single valid counterexample disproves a universal claim. Deductive reasoning derives a conclusion from accepted definitions, facts and logical steps.</p>",
      "<h3>Problem-solving cycle</h3><p>Understand the problem, represent it, plan a strategy, carry it out, and check whether the result answers the original question. Strategies include drawing a diagram, making a table, looking for a pattern, working backwards and simplifying a related problem.</p>",
      "<p><strong>Worked example:</strong> Observing that the first several odd numbers sum to squares suggests (1+3+...+(2n-1)=n^2). Verify by induction: it is true for (n=1); adding the next odd number ((2n+1)) to (n^2) gives ((n+1)^2).</p>"
    ]),
    tricks: html(["<ul><li>Separate exploration from proof: a pattern is a conjecture until justified.</li><li>Test boundary cases and search for counterexamples before claiming a rule.</li><li>Ask learners to explain why a strategy works, not only report an answer.</li><li>Compare two valid solution methods to reveal structure.</li><li>Return to the original question and check units, constraints and reasonableness.</li></ul>"]),
    notes: html(["<ul><li>Induction from examples is useful for discovery but does not prove every case.</li><li>A counterexample is enough to refute a universal statement.</li><li>A proof must use valid reasoning from definitions, assumptions or established results.</li><li>Metacognition means planning, monitoring and evaluating one's own problem-solving.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A student checks a rule for the first five whole numbers and says it is true for all whole numbers. What is the main logical gap?", options: ["The examples may suggest a pattern but do not prove every case", "A pattern can never be used in mathematics", "Whole numbers cannot be tested", "Only a calculator can prove it"], answer: 0, solution: "A finite set of examples supports a conjecture but does not establish a universal claim." },
      { level: 'Standard', prompt: "Which is enough to disprove the statement 'Every prime number is odd'?", options: ["A second odd prime", "The number 2", "The number 9", "A composite even number"], answer: 1, solution: "The prime 2 is even, so it is a counterexample to the universal statement." },
      { level: 'Challenge', prompt: "A learner finds the sum of 1 through 20. Which strategy uses a useful structure?", options: ["Add 1, then stop", "Pair first and last terms: 1+20, 2+19, and so on", "Multiply 20 by itself", "Subtract 1 from every term"], answer: 1, solution: "Each of the 10 pairs sums to 21, so total is (10 times 21=210). Pairing reveals a structure and completes the calculation." }
    ]
  },
  'mathematics-curriculum-and-classroom': {
    prerequisites: ['School mathematics content', 'Learning objectives', 'Assessment principles'],
    coverage: ['Aims and purposes of mathematics education', 'Conceptual progression and prerequisite links', 'Learning outcomes and lesson planning', 'Sequencing, pacing and spiral review', 'Classroom dialogue and mathematical norms', 'Differentiation, resources and evidence-informed adjustment'],
    theory: html([
      "<h3>Purpose and progression</h3><p>A mathematics curriculum develops number sense, conceptual understanding, procedural fluency, reasoning, problem solving, communication and the ability to apply mathematics. Concepts build on prerequisites and should move from intuitive experiences toward increasing abstraction and generalisation.</p>",
      "<h3>Plan a learning sequence</h3><p>Start with a clear, observable learning outcome. Identify prerequisite knowledge, select examples and representations, anticipate likely errors, plan questions and decide what evidence will show learning. A lesson typically connects prior knowledge, introduces or explores a new idea, provides guided practice and closes with review or assessment.</p>",
      "<h3>Responsive classroom</h3><p>Use student responses and work samples to adjust pacing, examples and support. Provide opportunities for explanation, multiple strategies and productive discussion. Maintain high expectations while varying access, scaffolds and extension.</p>",
      "<p><strong>Worked planning example:</strong> For comparing fractions, an outcome might be 'justify which of two fractions is greater'. Prerequisites include equivalent fractions and number-line placement; evidence should include a comparison and a reason, not only a selected symbol.</p>"
    ]),
    tricks: html(["<ul><li>Write outcomes as observable student actions rather than broad teacher intentions.</li><li>Plan a diagnostic prompt before teaching a new concept.</li><li>Connect concrete, visual, verbal and symbolic representations.</li><li>Use a short exit question to decide the next lesson's starting point.</li><li>Align practice and assessment with the stated learning objective.</li></ul>"]),
    notes: html(["<ul><li>Vertical progression links a concept across grade levels; horizontal connections link ideas within a level.</li><li>Spiral review revisits important ideas with growing depth and complexity.</li><li>Formative evidence is used during learning to guide next steps.</li><li>Curriculum coverage alone does not show whether students understand or can apply a concept.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Which is the clearest measurable learning outcome for a lesson on equivalent fractions?", options: ["Understand fractions", "Enjoy mathematics", "Generate and justify two fractions equivalent to 3/4", "Listen to the teacher"], answer: 2, solution: "It names an observable student task and the mathematical idea to demonstrate." },
      { level: 'Standard', prompt: "Before teaching subtraction of unlike fractions, which prerequisite is most important to check?", options: ["Equivalent fractions and common denominators", "Properties of circles", "Long division of polynomials", "Reading a bar graph"], answer: 0, solution: "A common denominator lets the fractions represent like-sized parts before subtracting." },
      { level: 'Challenge', prompt: "Half the class selects an incorrect method on an exit question. What is the strongest next instructional move?", options: ["Move on because the lesson plan is complete", "Use the responses to diagnose the misconception and adjust instruction", "Record zero without discussing the work", "Repeat the same explanation unchanged"], answer: 1, solution: "Formative evidence should inform a targeted next step; inspect the error pattern and respond with an appropriate explanation or task." }
    ]
  },
  'language-of-mathematics': {
    prerequisites: ['Reading comprehension', 'Number and operation vocabulary', 'Basic mathematical representations'],
    coverage: ['Precise vocabulary and definitions', 'Symbols, expressions and conventions', 'Translating verbal statements to mathematics', 'Reading graphs, diagrams and notation', 'Mathematical explanation and argument', 'Multilingual access without lowering conceptual demand'],
    theory: html([
      "<h3>Precision and meaning</h3><p>Mathematical words have precise meanings. 'Difference', 'factor', 'product', 'at least', 'congruent' and 'similar' should be taught with examples and nonexamples. Everyday and mathematical meanings may differ, as with 'mean', 'odd' or 'rational'.</p>",
      "<h3>Representations and translation</h3><p>Learners move among spoken language, written sentences, symbols, tables, graphs, diagrams and physical models. Translation should preserve meaning: 'five less than x' is (x-5), while 'five less than twice x' is (2x-5).</p>",
      "<h3>Mathematical communication</h3><p>Students should state a claim, show relevant steps and explain why those steps are valid. Sentence frames, labelled diagrams, word banks and opportunities to discuss in a familiar language can support access while keeping the mathematical reasoning rigorous.</p>",
      "<p><strong>Worked example:</strong> 'The quotient of a number and 4, increased by 3' translates to (x/4+3). Parentheses clarify that the division is done before adding 3.</p>"
    ]),
    tricks: html(["<ul><li>Ask students to restate a word problem in their own words before calculating.</li><li>Highlight relational words and identify which quantity they connect.</li><li>Use examples and nonexamples to sharpen definitions.</li><li>Require labels and units in diagrams, tables and final answers.</li><li>Accept varied explanation routes while checking that the mathematical meaning is precise.</li></ul>"]),
    notes: html(["<ul><li>'At least 5' means (x ge 5); 'more than 5' means (x>5).</li><li>'Twice the sum of a and b' is (2(a+b)); the sum of twice a and b is (2a+b).</li><li>Equality expresses a relation between two equivalent quantities, not an instruction to calculate the next answer.</li><li>Multiple representations can expose different features of the same concept.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Which expression means '7 less than twice x'?", options: ["(7-2x)", "(2(x-7))", "(2x-7)", "(7x-2)"], answer: 2, solution: "Twice x is (2x); 7 less than that is (2x-7)." },
      { level: 'Standard', prompt: "Which statement best explains why (3/4) is greater than (2/3)?", options: ["Four is greater than three", "With denominator 12, (9/12>8/12)", "Three is a larger numerator", "The fraction bar means addition"], answer: 1, solution: "Equivalent fractions with a common denominator show the comparison directly: (3/4=9/12) and (2/3=8/12)." },
      { level: 'Challenge', prompt: "A learner translates 'the sum of a number and 6, divided by 2' as (x+6/2). What is the correct expression?", options: ["(x+6/2)", "((x+6)/2)", "(2x+6)", "(x/2+6)"], answer: 1, solution: "The phrase says the entire sum is divided by 2, so parentheses are required: ((x+6)/2)." }
    ]
  },
  'child-thinking-and-mathematical-misconceptions': {
    prerequisites: ['Developmentally appropriate mathematics', 'Mathematical representations', 'Formative assessment'],
    coverage: ['Prior knowledge and learner strategies', 'Conceptual change and cognitive conflict', 'Common number and operation misconceptions', 'Misconceptions in fractions, equality and geometry', 'Diagnostic questions and student explanations', 'Responsive feedback and conceptual repair'],
    theory: html([
      "<h3>Use learner thinking as evidence</h3><p>Students build new ideas from prior experiences, which may include partial strategies and misconceptions. Listen to explanations and inspect written work to identify the reasoning behind an answer; the same incorrect result can arise from different causes.</p>",
      "<h3>Common misconceptions</h3><p>Examples include believing multiplication always makes a number larger, assuming a larger denominator makes a fraction larger, reading the equals sign as 'the answer comes next', or classifying a shape only by its orientation. These require carefully chosen comparisons, not only repeated correction.</p>",
      "<h3>Respond productively</h3><p>Ask students to predict, represent and explain. Contrast cases that reveal the conflict, use a number line or concrete model, and guide the learner to revise the rule. Feedback should identify the next mathematical step and preserve a student's willingness to reason.</p>",
      "<p><strong>Worked diagnostic example:</strong> Ask whether (1/3) or (1/5) is larger and why. A learner choosing (1/5) because 5 is larger may be comparing denominators as whole numbers. A same-size whole split into equal parts, or a number-line model, makes each fifth visibly smaller than each third.</p>"
    ]),
    tricks: html(["<ul><li>Ask 'How did you decide?' before labeling an answer as careless.</li><li>Use a contrast pair that changes one feature at a time.</li><li>Represent the same idea concretely, visually and symbolically.</li><li>Do not teach a shortcut that reinforces a false general rule.</li><li>Check for conceptual change with a new example after instruction.</li></ul>"]),
    notes: html(["<ul><li>Misconception diagnosis focuses on the learner's underlying rule, not only the error mark.</li><li>Conceptual and procedural knowledge support one another.</li><li>Useful feedback is specific, actionable and connected to the learning goal.</li><li>Manipulatives help when their actions are explicitly connected to mathematical symbols and language.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A learner says (1/8) is greater than (1/4) because 8 is greater than 4. Which response best addresses the idea?", options: ["Say 'wrong' and give the answer", "Compare both fractions using equal-sized wholes or a number line", "Ask the learner to memorise 8 is smaller", "Avoid discussing denominators"], answer: 1, solution: "A visual model makes the inverse relation between denominator size and unit-fraction size observable." },
      { level: 'Standard', prompt: "A student writes (3+4=7) correctly but writes (3+4=7+0) as false because 'the answer is already there'. What misconception is most likely?", options: ["Equals means 'is the same value as' is not understood", "Addition is not commutative", "Zero is a negative number", "Seven is not a whole number"], answer: 0, solution: "The student appears to read the equals sign only as a direction to produce an answer, rather than as an equivalence relation." },
      { level: 'Challenge', prompt: "After a learner uses an incorrect rule, what evidence best shows that conceptual understanding has improved?", options: ["The learner repeats the teacher's sentence", "The learner solves a new example and explains why the corrected rule applies", "The learner copies the worked solution", "The learner finishes faster"], answer: 1, solution: "Transfer to a fresh example with an explanation shows more than imitation or speed." }
    ]
  },
  'assessment-in-mathematics': {
    prerequisites: ['Learning outcomes', 'Question and task design', 'Feedback principles'],
    coverage: ['Diagnostic, formative and summative purposes', 'Assessment of concepts, fluency and reasoning', 'Validity, reliability and fairness', 'Question types and mathematical communication', 'Rubrics, feedback and self-assessment', 'Using results to adapt teaching'],
    theory: html([
      "<h3>Purpose and timing</h3><p>Diagnostic assessment identifies entry knowledge and gaps. Formative assessment gathers evidence during learning so teaching and learning can adjust. Summative assessment judges achievement at the end of a period or unit. One task can serve different purposes depending on how its evidence is used.</p>",
      "<h3>Quality evidence</h3><p>Validity concerns whether a task measures the intended learning. Reliability concerns consistency of results. Fair assessment removes irrelevant barriers, uses clear language and gives learners an appropriate opportunity to show the target skill.</p>",
      "<h3>Assess mathematical proficiency</h3><p>Use a balanced range of selected-response items, explanations, investigations, oral reasoning and work samples. A rubric can distinguish accuracy, strategy, representation and justification. Feedback should be timely and point to a next step.</p>",
      "<p><strong>Worked assessment example:</strong> If the outcome is comparing fractions with justification, an item asking only students to copy a rule provides weak evidence. A comparison plus a number-line placement and explanation better matches the outcome.</p>"
    ]),
    tricks: html(["<ul><li>Align every assessment item with a stated learning outcome.</li><li>Use student work and explanations, not only final answers, to diagnose strategies.</li><li>Check whether language difficulty is obscuring the mathematics being assessed.</li><li>Give feedback that students can act on before the next assessment.</li><li>Look for class-wide error patterns and respond instructionally.</li></ul>"]),
    notes: html(["<ul><li>Assessment for learning is formative use of evidence; assessment of learning is summative judgment.</li><li>A clear success criterion describes the quality of the mathematical work expected.</li><li>Reliability alone does not guarantee validity.</li><li>Self-assessment and peer explanation can develop metacognition when criteria are clear.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A teacher uses a short question during a lesson and reteaches based on responses. This is primarily:", options: ["Diagnostic assessment only", "Formative assessment", "Summative assessment", "Norm-referenced grading"], answer: 1, solution: "The evidence is gathered during learning and used to adjust instruction, so it is formative." },
      { level: 'Standard', prompt: "Which task best assesses the outcome 'justify a method for finding 3/4 of 20'?", options: ["Copy a definition of fraction", "State only that the answer is 15", "Find 3/4 of 20 and explain the representation or steps", "Write the multiplication table of 4"], answer: 2, solution: "The task directly elicits both the target calculation and a justification of the method." },
      { level: 'Challenge', prompt: "A test gives consistent scores but mostly measures reading complexity rather than the intended arithmetic. Which quality is most compromised?", options: ["Reliability", "Validity", "Scoring speed", "Coverage of names"], answer: 1, solution: "The test does not adequately measure its intended construct, so its validity is compromised." }
    ]
  },
  'remedial-teaching-in-mathematics': {
    prerequisites: ['Assessment and diagnosis', 'Prerequisite progression', 'Mathematical representations'],
    coverage: ['Identify specific prerequisite gaps', 'Distinguish procedural slips from conceptual barriers', 'Plan short targeted interventions', 'Use concrete, visual and symbolic scaffolds', 'Practice, feedback and gradual release', 'Monitor progress and adapt or fade support'],
    theory: html([
      "<h3>Diagnose before intervening</h3><p>Remedial teaching responds to a specific learning need. Use a brief diagnostic task, interview or work sample to locate the missing prerequisite and determine whether the barrier is conceptual, procedural, linguistic or related to confidence and access.</p>",
      "<h3>Targeted teaching cycle</h3><p>Set a small observable goal, connect to what the learner knows, model one strategy, guide practice with feedback, then provide independent practice. Move between concrete, pictorial and symbolic representations and explicitly connect them.</p>",
      "<h3>Monitor and adjust</h3><p>Use frequent low-stakes checks on fresh examples. If progress stalls, revisit the diagnosis or change the representation, examples or amount of scaffolding. Fade support when the learner can select and use the strategy independently.</p>",
      "<p><strong>Worked intervention example:</strong> If a student subtracts fractions by subtracting both numerators and denominators, first check whether the student understands equal-sized parts. Use same-size fraction strips to rename (3/4-1/2) as (3/4-2/4), then connect the model to the common-denominator procedure.</p>"
    ]),
    tricks: html(["<ul><li>Teach the prerequisite gap, not a long list of unrelated exercises.</li><li>Ask the learner to think aloud to expose the strategy being used.</li><li>Use worked examples followed by partially completed examples and then independent tasks.</li><li>Provide enough varied practice to test transfer, not only repetition of one item.</li><li>Set a review date and use progress evidence to fade or revise support.</li></ul>"]),
    notes: html(["<ul><li>Remediation is targeted support, not punishment or simply assigning more of the same work.</li><li>Scaffolding should support success while preserving meaningful student thinking.</li><li>Concrete materials are most useful when their features map clearly to the mathematical idea.</li><li>Progress monitoring checks whether the intervention is working for this learner.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A student repeatedly adds denominators when adding fractions. What should the teacher do first?", options: ["Assign 50 more problems immediately", "Diagnose the student's understanding of equal-sized fractional parts", "Remove fractions from the course", "Teach decimal multiplication instead"], answer: 1, solution: "The error suggests a conceptual issue about units and equivalent parts. Diagnose the reasoning before selecting an intervention." },
      { level: 'Standard', prompt: "Which sequence best supports a learner who cannot yet subtract unlike fractions?", options: ["Abstract rule, timed test, then no feedback", "Fraction strips, matching visual partitions, symbolic common-denominator work", "Memorise answers, skip models, increase speed", "Use unrelated geometry examples"], answer: 1, solution: "The sequence connects a concrete model to a visual representation and then to symbols." },
      { level: 'Challenge', prompt: "When should a scaffold be faded?", options: ["As soon as the teacher has modelled once", "When evidence shows the learner can perform the target independently across suitable examples", "Only at the end of the school year", "Never, because support should remain identical"], answer: 1, solution: "Fading follows demonstrated independence and transfer, while monitoring continues for retention." }
    ]
  },
  'mathematics-teaching-methods-and-materials': {
    prerequisites: ['Mathematical content knowledge', 'Learning objectives', 'Classroom assessment'],
    coverage: ['Explicit instruction and worked examples', 'Inquiry, discovery and problem-based learning', 'Discussion and cooperative learning', 'Concrete manipulatives and visual models', 'Digital and non-digital resource selection', 'Method choice, sequencing and evidence of learning'],
    theory: html([
      "<h3>Choose a method for the learning goal</h3><p>Explicit instruction can make a new procedure visible through clear modelling and guided practice. Inquiry and problem solving invite learners to investigate, make conjectures and compare strategies. Discussion helps students articulate and examine mathematical reasoning. No single method is best for every goal or learner.</p>",
      "<h3>Use materials purposefully</h3><p>Objects such as counters, base-ten blocks, fraction strips, geoboards and measuring tools can make relationships visible. A material is useful when the learner can connect its actions and features to the mathematical idea; manipulatives should not become an unexplained activity.</p>",
      "<h3>Sequence support</h3><p>Connect prior knowledge, introduce a representation, model or explore the key idea, guide practice, invite independent application, and check understanding. Select examples that reveal both the rule and its boundaries.</p>",
      "<p><strong>Worked teaching example:</strong> To introduce area, students can cover a rectangle with unit squares, count rows and columns, organise the count as (length times width), and then connect the model to the formula (A=lw).</p>"
    ]),
    tricks: html(["<ul><li>Choose a teaching strategy based on the intended concept, procedure or reasoning outcome.</li><li>Use examples and nonexamples to clarify when a method applies.</li><li>Ask questions that reveal student thinking instead of only checking completion.</li><li>Connect the material's physical action to diagrams and notation explicitly.</li><li>Review whether the resource is accessible, accurate and appropriate for the class.</li></ul>"]),
    notes: html(["<ul><li>Concrete-to-representational-to-abstract is a useful progression, not a mandatory one-way rule.</li><li>Guided practice gives feedback before independent application.</li><li>Cooperative work needs individual accountability and purposeful mathematical roles.</li><li>Technology should improve access, feedback, visualisation or exploration for the learning goal.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "Which material most directly models equal parts of one whole for comparing 1/3 and 1/4?", options: ["Fraction strips with equal-length wholes", "A ruler without marked units", "A multiplication chart", "A calendar"], answer: 0, solution: "Fraction strips with the same whole length make the size of thirds and fourths directly comparable." },
      { level: 'Standard', prompt: "A teacher demonstrates a new division procedure, solves one example aloud, and then guides students through a similar problem. This mainly combines:", options: ["Modelling and guided practice", "Summative testing and ranking", "Unstructured discovery only", "Remedial placement"], answer: 0, solution: "The teacher makes the process visible and supports practice before independent work." },
      { level: 'Challenge', prompt: "What makes a digital geometry tool instructionally useful?", options: ["It contains many animations", "It enables students to manipulate a figure and test a geometric conjecture tied to the lesson goal", "It replaces all teacher questions", "It is used regardless of accessibility"], answer: 1, solution: "The tool is valuable when its interaction supports a specific mathematical investigation and evidence of reasoning." }
    ]
  },
  'community-mathematics-and-inclusion': {
    prerequisites: ['Number and measurement in context', 'Inclusive teaching principles', 'Mathematical communication'],
    coverage: ['Mathematics in local work and daily life', 'Culturally responsive examples and learner assets', 'Accessibility and multiple ways to participate', 'Gender, language and socioeconomic bias checks', 'Differentiation without lowering mathematical goals', 'Family and community connections with learner privacy'],
    theory: html([
      "<h3>Mathematics in community contexts</h3><p>Mathematics appears in markets, transport, construction, farming, crafts, cooking, budgeting, public data and local environmental decisions. Contexts can make a concept meaningful and show that mathematical reasoning is used in many kinds of work and knowledge.</p>",
      "<h3>Inclusion and access</h3><p>Plan for varied language backgrounds, disabilities, prior opportunities and ways of communicating. Use accessible print and digital materials, clear diagrams, assistive supports, flexible participation and more than one representation. Preserve the intellectual goal while varying the route and scaffold.</p>",
      "<h3>Respectful context selection</h3><p>Choose familiar and varied examples without stereotyping learners or assigning ability by identity. Avoid requiring students to disclose family income, migration, health or other private details. Invite optional local examples and check whose experiences are represented.</p>",
      "<p><strong>Worked lesson example:</strong> To teach ratios, learners can compare recipes, map scales, or community transport timetables. Offer equivalent printed and enlarged visual formats, allow a labelled diagram or written explanation, and assess the ratio reasoning rather than handwriting speed.</p>"
    ]),
    tricks: html(["<ul><li>Audit examples for assumptions about resources, family structure, language and access.</li><li>Offer multiple ways to engage with the problem and explain reasoning.</li><li>Use local knowledge as a resource while checking its mathematical accuracy together.</li><li>Keep assessment criteria focused on mathematics rather than accent, speed or handwriting unless those are the actual outcomes.</li><li>Invite participation without requiring personal or sensitive disclosures.</li></ul>"]),
    notes: html(["<ul><li>Equity means providing supports responsive to barriers so learners can access meaningful mathematical goals.</li><li>Multiple representations and accessible formats benefit diverse learners.</li><li>Context should enrich mathematical thinking, not distract or introduce hidden prerequisites.</li><li>High expectations and appropriate scaffolding can be maintained together.</li></ul>"]),
    questions: [
      { level: 'Foundation', prompt: "A teacher wants a context for proportional reasoning. Which choice is most inclusive?", options: ["Use only one expensive hobby familiar to a few students", "Offer several contexts and allow students to choose a familiar one", "Require students to share household income", "Assume every learner has the same transport experience"], answer: 1, solution: "A choice of contexts offers access through varied experiences without requiring personal disclosure." },
      { level: 'Standard', prompt: "A student can explain a geometry solution orally but has difficulty writing due to a motor barrier. If handwriting is not the learning goal, what is an appropriate response?", options: ["Mark the mathematics as incorrect", "Allow an accessible response format while assessing the same geometric reasoning", "Remove the geometry objective", "Require the student to disclose medical details to classmates"], answer: 1, solution: "An accessible response mode removes an irrelevant barrier while preserving the learning objective." },
      { level: 'Challenge', prompt: "Which practice best connects community knowledge with rigorous mathematics?", options: ["Accept every local estimate without checking it", "Use a familiar context, identify quantities and assumptions, then verify calculations and interpretations", "Avoid all real-world contexts", "Use community examples only for students from that community"], answer: 1, solution: "A meaningful context can launch analysis, while explicit assumptions and verification maintain mathematical rigor." }
    ]
  },
};
