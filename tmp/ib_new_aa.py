from ib_content import *
a='analysis-and-approaches-hl/'
create(a+'number-and-algebra/counting-permutations-and-combinations','Counting, Permutations and Combinations','AA HL','Number and Algebra','Count ordered arrangements and unordered selections, with repetition, restrictions and probability applications.',[
 ('Counting principles',[
 'Addition rule: add mutually exclusive choices. Product rule: multiply successive choice counts. Check whether choices remain constant after earlier decisions.',
 r'For n distinct objects, $n!=n(n-1)\cdots1$, with0!=1. Ordered r-selections without replacement: $P(n,r)=n!/(n-r)!$. Unordered selections: $\binom nr=n!/[r!(n-r)!]$.',
 r'Worked comparison: choose captain and deputy from8people:8×7=56; choose a two-person committee: $\binom82=28$. Order doubles the first count.'
 ]),('Repetition and indistinguishable objects',[
 'A length-r code from n symbols with repetition has nʳ possibilities. If repetition is forbidden, use falling products. Leading-zero restrictions must be handled at the first position.',
 r'Permuting n objects with repeats n₁,…,nₖ gives $n!/(n_1!\cdots n_k!)$. Worked word LEVEL has5letters with twoLs and twoEs:5!/(2!2!)=30distinct arrangements.',
 r'Circular arrangements of n distinct objects have(n−1)! when rotations are identical and reflections are distinct. Fix one object’s position before arranging the rest.'
 ]),('Restrictions and complementary counting',[
 'For adjacent objects treat the group as one block, then multiply by its internal arrangements. For separated objects arrange the others first and choose gaps.',
 r'Worked: five people in a row, AandBtogether:4!×2=48. Not together:5!−48=72. These cases partition all arrangements.',
 r'At least one success is often total minus none. For three people chosen from four seniors and five juniors: at least one senior $\binom93-\binom53=74$.'
 ]),('Counting for probability and binomial coefficients',[
 r'With equally likely unordered samples use favourable selections/total selections. Exactly two reds when drawing3from5redand4blue is $\binom52\binom41/\binom93=10/21$.',
 r'In $(a+b)^n$, choosing r of the n factors to supply b explains the coefficient $\binom nr$. Do not apply equally likely counting to unequal-probability outcomes.',
 'Check0≤r≤n and whether replacement is allowed. Enumerating small cases is a useful check; it is not a substitute for a justified count.'
 ])],[
 ('A four-digit code uses digits0–9with repetition. How many codes? How many four-digit numbers?', 'Codes10⁴=10000. Numbers require a nonzero first digit:9×10³=9000.'),
 ('How many ordered podiums from7competitors?', '7×6×5=210; the three roles differ and nobody repeats.'),
 ('How many four-person committees from10people?',r'$\binom{10}4=210$. The same numerical result as a different problem does not make the methods interchangeable.'),
 ('Count distinct arrangements of BANANA.',r'6!/(3!2!)=60: threeAs,twoNs.'),
 ('Six distinct people sit around a circular table. Count arrangements with rotations identical, reflections distinct.', 'Fix one person:5!=120. If labelled seats are distinct instead, use6!=720.'),
 ('Four boys and three girls form a row with no two girls adjacent. Count arrangements.',r'Arrange boys4!; choose3of5gaps and arrange girls3!: $4!\binom53 3!=1440$.'),
 ('Draw4cards from a52-card deck without replacement. Find the probability of exactly2aces.',r'$\binom42\binom{48}2/\binom{52}4$. Choosing positions or ordering the entire hand is unnecessary.'),
 ('Choose3people from5seniorsand4juniors, with at least1ofeach. Count committees.',r'$\binom93-\binom53-\binom43=84-10-4=70$, alternatively5×6+10×4=70.')],[
 ('Which count describes a committee of3from8?',[r'$8^3$',r'$8!$',r'$\binom83$',r'$P(8,3)$'],'C','Committee order does not matter.'),
 ('How many arrangements of AAB?',['6','3','2','1'],'B','Divide3!by2!for identicalAs.'),
 ('A code has4symbols from5choices with repetition. Count it.',['20','120','625','5'],'C','Five independent choices at each of four positions give5⁴.'),
 ('What does an at-least-one complement subtract?',['Exactly one','All successful cases','None','Half the cases'],'C','At least one and none partition all outcomes.'),
 ('Why does circular counting fix one object?',['To remove reflected copies','To remove rotational copies','To allow repetition','To forbid neighbours'],'B','A fixed reference prevents counting the same rotation repeatedly.')])
create(a+'number-and-algebra/proof-by-contradiction','Proof by Contradiction','AA HL','Number and Algebra','Build contradiction proofs using parity, divisibility and irrationality; distinguish proof, counterexample and induction.',[
 ('Structure of a contradiction proof',[
 'To prove statementP, assume its negation. Deduce an impossibility while recording each justified implication. Conclude that the negation is false andPtrue.',
 'Negate quantifiers carefully: the negation of “every” is “there exists at least one counterexample”. Negating an inequality includes its equality case.',
 'A numerical check can disprove a universal claim but cannot establish it. Contradiction is not circular reasoning: do not assume the statement you are trying to prove.'
 ]),('Worked proof: irrationality of √2',[
 r'Assume $\sqrt2=p/q$ with positive integers p,qcoprime. Squaring givesp²=2q², sop²iseven.',
 'If pisodd, p=2k+1makesp²=4k²+4k+1odd. Thuspiseven, p=2r.',
 'Then4r²=2q², soq²=2r²andqiseven. Both share factor2, contradicting coprimality. Hence√2isirrational.'
 ]),('Divisibility and prime proofs',[
 'Euclid’s proof: assume only finitely many primes p₁,…,pₙ. SetN=p₁⋯pₙ+1. N>1has a prime divisor, but division by every listed prime leaves remainder1. Contradiction.',
 'Nneed not itself be prime; the argument only requires a prime divisor. Replacing this step with “Nisprime” makes the proof invalid.',
 'For integer equations, exploit parity or remainders. Identify exactly which integer property yields the contradiction.'
 ]),('Choose a valid proof method',[
 'Direct proof starts with the hypotheses and reaches the conclusion. Contrapositive proves notQ⇒notP for P⇒Q. Contradiction assumes PandnotQ. Induction handles an integer-indexed family through a base case and an inductive implication.',
 'For a rationality claim, use lowest terms and a nonzero denominator. For a claim that fails, provide a counterexample satisfying the original assumptions.'
 ])],[
 ('Prove that the square of an odd integer is odd.',r'Write n=2k+1. Thenn²=2(2k²+2k)+1, which is odd. This direct lemma supports irrationality proofs.'),
 ('Prove√3isirrational, using that3divides n²only if3dividesn.',r'Assume√3=p/qinlowestterms. p²=3q²impliesp=3r; thenq²=3r²implies3dividesq, contradicting coprimality. The lemma follows because square residuesmod3are0or1.'),
 ('Prove that no integers x,y satisfy2x+4y=7.', 'The left side is even and the right side odd. Assuming a solution contradicts parity.'),
 ('Negate “for every real x, x²&gt;0” and decide the original claim.', 'Negation: there exists realxwithx²≤0. x0is a counterexample; the original claim is false.'),
 ('Critique: “If there were finitely many primes, their product plus1would be prime.”', 'The product-plus-one can be composite. Every prime divisor is absent from the finite list, which supplies the valid contradiction.'),
 ('Prove that a rational number plus an irrational number is irrational.', 'Assume their sum rational. Subtract the given rational number; closure of rationals under subtraction would make the irrational number rational. Contradiction.'),
 ('Prove there is no smallest positive rational number.', 'Assumeqisthe smallest positive rational. q/2isrational,positiveandsmallerthanq. This contradicts minimality.')],[
 ('What is assumed first in contradiction?',['The conclusion','The negation of the desired claim','An example','The answer key'],'B','Assume the claim is false and derive an impossibility.'),
 ('Why use a fraction in lowest terms?',['To approximate it','To rule out a common factor','To ensure a decimal ends','To square it'],'B','A common prime divisor then contradicts the initial representation.'),
 ('Product of known primes plus1must be…',['Prime','Even','Divisible by a prime outside the list','A square'],'C','The new number may be composite, but its prime divisors are not listed.'),
 ('One counterexample establishes…',['A universal claim','Its falsity','All cases','Induction'],'B','A universal claim is false when one permitted case fails.'),
 ('Negation of x&gt;3is…',['x&lt;3','x≥3','x≤3','x=3'],'C','The negation includes equality.')])
create(a+'statistics-and-probability/bayes-theorem-and-total-probability','Bayes’ Theorem and Total Probability','AA HL','Statistics and Probability','Reverse conditional probabilities with two or three source events, tables and probability trees.',[
 ('Partition the sample space',[
 r'Events A₁,…,Aₖform a partition if disjoint and exhaustive. Then $P(B)=\sum_iP(A_i)P(B\mid A_i)$. Each product is a joint probability.',
 r'For P(B)>0, $P(A_i\mid B)=P(A_i)P(B\mid A_i)/P(B)$. The denominator includes every path ending inB, not only the path of interest.',
 'Prior probability describes sources before observingB; posterior describes the revised source probability afterB. P(B|A)andP(A|B)are usually different.'
 ]),('Worked three-source example',[
 'Factories A,B,Csupply50%,30%,20%ofitems; defect rates1%,2%,5%. Joint defect probabilities are0.005,0.006,0.010.',
 r'Total defect probability0.021. Given a defect, $P(C\mid D)=0.010/0.021=10/21\approx0.47619$. The largest defect rate is not the posterior probability.',
 r'For a nondefect use complement rates0.99,0.98,0.95. $P(A\mid D^c)=0.495/0.979\approx0.50562$.'
 ]),('Base rates and diagnostic interpretation',[
 r'Disease prevalence1%, sensitivity95%, false-positive rate5%. $P(+)=0.01(0.95)+0.99(0.05)=0.059$. $P(D\mid+)=0.0095/0.059=19/118\approx16.1\%$.',
 'A positive result is not the same as certainty of disease. A low base rate can make most positives false. Use a10000-person frequency table to check:95truepositives,495falsepositives.',
 'Repeated-test multiplication requires conditional independence given the disease status. Reusing the single-test posterior without a valid dependence model is incorrect.'
 ]),('Inverse probability and modelling',[
 'When a mixture fraction is unknown, total probability can form an equation for it. Check the resulting fraction is in[0,1].',
 'State the partition, label every tree branch, calculate joint paths, sum the evidence paths, and divide. A zero evidence probability makes the conditional probability undefined.'
 ])],[
 ('Using the factory data above, find P(B|defect).',r'0.006/0.021=2/7≈0.286. Denominator is the total defect probability.'),
 ('Using the same data, find P(C|nondefect).',r'0.20(0.95)/0.979=190/979≈0.194076. Conditional proportions still sum to1across factories.'),
 ('Two machines produce in proportion40%and60%, with failure rates3%and1%. Given failure, find the first machine probability.',r'Joint failures0.012and0.006; posterior0.012/0.018=2/3.'),
 ('A test has sensitivity90%, false-positive rate10%, prevalence20%. Find P(disease|positive).',r'0.18/(0.18+0.08)=9/13≈0.692308. This reverses the condition; it is not0.9.'),
 ('Bags AandBare chosen with probabilitiesp,1−p. Red probabilities0.8and0.2; overallred0.5. Findp.',r'0.8p+0.2(1−p)=0.5implies0.6p0.3, sop0.5. It is a valid mixture fraction.'),
 ('For the1%prevalence test above, compute posterior after two positives, assuming conditional independence.',r'Joint diseased positives0.01(0.95)²=0.009025; healthy positives0.99(0.05)²=0.002475. Posterior0.009025/0.0115=361/460≈0.784783. Explain the independence assumption.'),
 ('Sources A,B,C have priors0.2,0.3,0.5and evidence likelihoods0.4,0.2,0.1. Find all posteriors.',r'Joint terms0.08,0.06,0.05; total0.19. Posteriors8/19,6/19,5/19sum1.')],[
 ('Bayes’ denominator is…',['The prior','Total evidence probability','The desired likelihood','Always1'],'B','Sum joint paths over the exhaustive partition.'),
 ('P(A|B)equalsP(B|A)…',['Always','Only if independent','Not generally','Never'],'C','The direction and base rates matter.'),
 ('Can the source events overlap in the partition formula as written?',['Yes','No','Only if rare','Only with3events'],'B','A partition is disjoint and exhaustive.'),
 ('Conditional probability given an impossible event is…',['0','1','0.5','Undefined'],'D','The denominator is0.'),
 ('Two positive tests can be multiplied without qualification…',['Always','Only under an appropriate independence assumption','If equal','If percentages'],'B','Dependence between tests affects the joint likelihood.')])
