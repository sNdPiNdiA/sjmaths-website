from ib_content import *
b='applications-and-interpretation-sl/'
expand(b+'number-and-algebra/scientific-notation-and-rounding',card('Precision, bounds and estimation',[
 r'For a nonzero signed value, standard form has $1\le|a|<10$ in $a10^k$. Zero has no unique normalised exponent. Round the coefficient and renormalise if it becomes10.',
 r'A length reported as12.3cm to the nearest0.1cm implies $12.25\le L<12.35$ using the usual positive-number rounding convention. Bounds express measurement uncertainty, not just decimal formatting.',
 r'For positive dimensions, find product bounds by multiplying lower bounds and upper bounds; for a ratio use lower numerator/upper denominator and vice versa. Percentage error relative to an exact value0 is undefined.',
 'Estimate the order of magnitude before calculating. Preserve guard digits and report the units; significant figures and decimal places answer different questions.'
]),[
 (r'Write−0.00072in standard form and explain the coefficient condition.',r'$-7.2\times10^{-4}$; its coefficient has magnitude7.2. Negative numbers require absolute value in the condition.'),
 (r'Round $9.996\times10^5$ to3significant figures.',r'The coefficient rounds to10.0; renormalise to $1.00\times10^6$. The trailing zeros state three significant figures.'),
 (r'A rectangle has measured lengths12.3cm and4.0cm, each to the nearest0.1cm. Bound its area.',r'$12.25\le L<12.35$, $3.95\le W<4.05$. Thus $48.3875\le A<50.0175$cm². Multiplying rounded reported values gives49.2cm² but hides uncertainty.'),
 (r'An estimate is48 and the exact value is50. Find absolute and percentage errors. What changes if the exact value is0?',r'Absolute error2; percentage error $2/50\times100=4\%$. With exact value0 the percentage formula divides by zero, so report absolute error instead.'),
 (r'Estimate $(6.1\times10^8)/(2.9\times10^{-3})$ before calculating.',r'Estimate $2\times10^{11}$. Actual coefficient6.1/2.9≈2.10345, so result $2.10\times10^{11}$to3sf. An answer of order10⁵ indicates an exponent error.')])
p=ROOT/b/'number-and-algebra/scientific-notation-and-rounding/index.html';s=p.read_text(encoding='utf-8').replace('Any real number can be expressed','Any positive real number can be expressed').replace('$7582.88$ (or exact $\\approx 7582.9$)',r'$500\sqrt{230}$ exactly (approximately $7582.88$)');p.write_text(s,encoding='utf-8')
expand(b+'number-and-algebra/arithmetic-and-geometric-sequences',card('Select a model and check the index',[
 r'Equal additions suggest arithmetic; equal percentage changes suggest geometric. For a value at time0 use $A(t)=A_0r^t$, whereas a first listed term is $u_n=u_1r^{n-1}$.',
 r'For r1, a geometric sequence is constant and $S_n=nu_1$; do not divide by r−1. For negative r, signs alternate. Ratio comparisons need a nonzero preceding term.',
 r'For $\sum_{k=p}^q u_k$, the number of terms is q−p+1, not q. Recover $u_n=S_n-S_{n-1}$.',
 'A term-count solution must be a positive integer. For threshold inequalities compare adjacent integer times using unrounded values. Growth models may cease to be realistic when resources are limited.'
]),[
 (r'Evaluate $\sum_{k=3}^{8}(2k-1)$.',r'Terms5,7,9,11,13,15: six terms; sum $6(5+15)/2=60$.'),
 (r'Find the sum of eight terms of a geometric sequence with first term7and ratio1.',r'All terms are7, so S8=56. The usual quotient form is0/0 here; use the constant-sequence case.'),
 (r'For u1=8,r=−1/2, find u4andS4. Explain why a population model would be unsuitable.',r'u4=−1; terms8,−4,2,−1 sum5. Negative population values are infeasible.'),
 (r'Two savings plans start with1000. One gains50each year; the other grows5%annually. Compare after3years.',r'At time0both1000. At year3: arithmetic1150; geometric1000(1.05)^3=1157.625. They agree after1year but growth methods differ.'),
 (r'Given $S_n=2n^2+3n$, find un and determine whether the sequence is arithmetic.',r'$S_n-S_{n-1}=4n+1$forn≥2; u1=S1=5 also matches. Difference4, so arithmetic.')])
expand(b+'functions/direct-and-inverse-variation',card('Identify the exponent and validate the model',[
 r'For positive data fitting $y=kx^n$, divide two observations: $y_2/y_1=(x_2/x_1)^n$, so $n=\ln(y_2/y_1)/\ln(x_2/x_1)$ for distinct x-values.',
 r'The units of k are [y]/[x]ⁿ. Check $y/x^n$ on further measurements; a constant from two points alone does not validate the model.',
 'For positive x and k, n>0 gives increasing power variation and n<0 decreasing inverse variation. Broader signs/domains need separate analysis.'
]),[
 (r'Data(2,12),(4,48),(6,108)follow a power model. Find n,k and check the third observation.',r'Ratio4=2ⁿ givesn2;k12/4=3. Prediction at6is108, agreeing with the third value.'),
 (r'For light intensity $I=1200/d^2$ with Iinlux and dinmetres, give units of1200and predict atd10. Explain one limitation.',r'Constant unitslux·m²; intensity12lux. A point-source inverse-square model ignores reflected light and background illumination.')])
expand(b+'functions/linear-models-and-gradients',card('Fit data, read residuals and build a tariff',[
 r'For noisy observations fit a least-squares line using paired lists. A residual is $e=y-\hat y$: positive means the model underpredicts. Inspect residual patterns and outliers; interpolation can still be inaccurate.',
 r'<strong>Worked data:</strong> x=1,2,3 and y=3,5,8 give $\bar x=2,\bar y=16/3$, slope2.5 and intercept1/3. Residuals1/6,−1/3,1/6sum0.',
 'For a piecewise price, use the excess quantity in later bands so earlier charges are not paid twice. Check values at breakpoints and realistic domains.'
]),[
 (r'Use the fitted line $y=2.5x+1/3$ above to predict atx2.5 and interpret an observed value7.',r'Prediction79/12≈6.5833; residual7−79/12=5/12≈0.417. Observed value exceeds the prediction. It is interpolation, but not guaranteed accurate.'),
 (r'A taxi charges30for the first2km then8per additionalkm. Write a model and find the fare for7km.',r'$C(d)=30$for0&lt;d≤2 and $30+8(d-2)$for d&gt;2. Fare70. The branches agree at2km; a no-trip charge atd0needs a stated policy.')])
expand(b+'functions/quadratic-and-exponential-models',card('Model comparison and shifted growth',[
 'Compare residuals on the same observations and validation data, not just visual appearance. A quadratic adds curvature but extra parameters can fit noise. State the fitted interval and units.',
 r'For $f(t)=ka^t+c$, the quantity following constant percentage change is f−c. Half-life/doubling applies to this excess above c, not generally to f itself. The asymptote is approached from above if k>0 and from below if k<0.',
 r'Example cooling80°Cto20°Cwith excess halving every10minutes: $T(t)=20+60(1/2)^{t/10}$. After10minutesT50, not40.'
]),[
 (r'Data atx0,1,2,3are2,5,10,17. Compare models L=5x+1 andQ=x²+2 using squared residuals.',r'Lpredictions1,6,11,16give residuals1,−1,−1,1; SSE4. Qmatches every datum,SSE0. ChooseQon these observations, then validate at additional x-values; exact fit does not justify unlimited extrapolation.'),
 (r'Using $T(t)=20+60(1/2)^{t/10}$, find when the temperature reaches35°C.',r'Excess15=60(1/2)^(t/10), ratio1/4, sot20minutes. Model domain t≥0; room temperature is assumed constant.')])
expand(b+'calculus/derivatives-and-tangents',card('Reading and estimating rates',[
 'The derivative has units of output per input. Positive derivative means increasing value, not necessarily positive value. A zero derivative need not be a turning point.',
 r'Estimate a rate at t using the symmetric secant $[f(t+h)-f(t-h)]/(2h)$. It is an estimate from finite data, not an exact instantaneous rate.',
 r'If f′(a)=0, the tangent is horizontal y=f(a) and the normal is vertical x=a. A cusp or discontinuity can make the derivative undefined.'
]),[
 (r'Tank volumes at minutes4,5,6are920,900,876litres. Estimate the rate at5minutes and compare the one-sided rates.',r'Central estimate(876−920)/2=−22L/min. One-sided estimates−20and−24L/minsuggest drainage is accelerating. Measurement spacing limits precision.'),
 (r'For f(x)=x³ find the tangent and normal at0. Is this a local extremum?',r'f′0=0andf0=0: tangent y0,normalx0. f′=3x²ispositive on both sides, so0is a stationary inflection, not an extremum.')])
expand(b+'calculus/optimization-in-context',card('Global extrema on a constrained domain',[
 'On a closed bounded interval, compare all feasible stationary points, endpoints and points where the derivative does not exist. A local second-derivative test alone does not establish a global optimum.',
 'For an open domain the best value may be approached but never attained. State the feasible dimensions before differentiating. Discrete outputs require comparing nearby allowed integers.',
 r'Example profit P(q)=−q²+12q−20 for0≤q≤4: unconstrained vertexq6is infeasible. P′>0on the permitted interval, so maximumP4=12.'
]),[
 (r'Find the global minimum and maximum of $f(x)=x^3-3x$ on[-2,3].',r'f′=3x²−3givesx±1. Candidate valuesf−2=−2,f−1=2,f1=−2,f3=18. Global minimum−2at−2and1; maximum18at3.'),
 (r'Profit is $P(n)=-(n-5.4)^2+30$ for integer nfrom0to10. Find the best output.',r'Continuous vertex5.4; compare integers5and6:P5=29.84,P6=29.64. Bestn5. Simply rounding a reported optimum without comparison is insufficient.')])
expand(b+'calculus/trapezoidal-rule-and-definite-integrals',card('Unequal intervals, signed values and uncertainty',[
 r'Unequal spacings require $\sum_i (x_{i+1}-x_i)(y_i+y_{i+1})/2$; do not use a single h. The estimate integrates the piecewise-linear interpolant.',
 r'A definite integral is signed. Total geometric area is $\int|f|$; distance travelled is $\int|v|$. Split at sign changes, including interpolated zeros when using tabulated data.',
 'Concavity gives an error direction for the signed integral if it holds on every strip. Changing concavity or noisy measurements can invalidate a single overall over/under claim. More strips do not remove measurement error.'
]),[
 (r'At t0,1,3seconds, velocities are2,4,−2m/s. Under linear interpolation find displacement and total distance.',r'Trapezoids:1(2+4)/2+2(4−2)/2=5m displacement. Zero occurs t=7/3. Positive area3+8/3andnegative magnitude2/3give distance19/3≈6.33m.'),
 (r'Use one trapezoid for $f(x)=x^2-1$ on[0,2]. Compare signed integral and total area.',r'Trapezoid2(−1+3)/2=2; exact integral2/3. Convexity gives an overestimate of the signed integral. Exact total area is2, after splitting at1; the coincidence with the trapezoid value is not a general rule.')])
expand(b+'statistics-and-probability/bivariate-data-and-spearmans-rank',card('Tied ranks and reliable predictions',[
 'Rank both variables in the same direction and preserve paired rows. For ties use average occupied ranks, then calculate Pearson correlation of the rank columns; the no-ties shortcut is not exact with ties.',
 r'Example x=1,2,2,4 and y=10,20,30,40: ranks x=1,2.5,2.5,4, y=1,2,3,4. Centred dot product4.5, sums of squares4.5and5, so $r_s=4.5/\sqrt{22.5}\approx0.948683$.',
 'Strong correlation is evidence of association, not causation. Compare scatter plot, residuals, context, sample design and outliers. Interpolation is usually safer than extrapolation, not guaranteed accurate.'
]),[
 (r'Calculate Spearman correlation for the tied dataset above and compare the no-ties shortcut.',r'Pearson on ranks gives0.948683. Σd²=0.5makes the shortcut0.95; it differs because xhas ties. Enter rank lists in the calculator, not raw values.'),
 (r'A nearly perfect decreasing nonlinear relationship is observed. Describe Pearson versus Spearman and one causal caution.',r'Spearman can be near−1because the ranking is consistently reversed; Pearson may have smaller magnitude because the pattern curves. A confounder or selection bias could explain association.')])
expand(b+'statistics-and-probability/normal-distribution-and-z-scores',card('Check a normal model and condition on selection',[
 'Inspect symmetry, outliers and a roughly bell-shaped distribution. A normal model has unbounded tails, so consider whether predictions below0or beyond physical limits are negligible. A sample mean alone does not establish normality.',
 r'For b>a, $P(X>b\mid X>a)=P(X>b)/P(X>a)$. The denominator represents the selected group, not the entire population.',
 'Calculator workflow: enter standard deviation, not variance; sketch the requested tail before selecting CDF or inverse CDF. Recheck the boundary by putting it back into the CDF.'
]),[
 (r'For X∼N(100,10²), find P(X&gt;120|X&gt;110).',r'Tails are0.0227501and0.1586553. Ratio≈0.143393or14.3%. Do not subtract the two tail probabilities for a conditional question.'),
 (r'Waiting times have mean5minutes andSD4minutes with a strong right skew. Explain a normal model risk.',r'Normal N(5,16) predicts P(X&lt;0)=Φ(−1.25)≈0.10565, impossible for a waiting time. The skew and substantial negative tail make this model unsuitable.')])
expand(b+'statistics-and-probability/chi-square-test-for-independence',card('Goodness of fit: one categorical variable',[
 'Independence uses a two-way table; goodness of fit compares one observed frequency distribution with specified probabilities. State H0andH1for the claimed distribution.',
 r'Expected counts $E_i=Np_i$ must sum toN. Use $\chi^2=\sum(O_i-E_i)^2/E_i$. For a fully specified k-category SLmodel,df=k−1. Fitted parameters require a degree-of-freedom adjustment in more advanced settings.',
 'Check independent observations and adequate expected counts. Combine categories only when substantively appropriate and before interpreting the revised test. Failure to reject is insufficient evidence against H0, not proof that H0is true.',
 r'<strong>Worked die test:</strong>60rolls give counts8,9,10,11,12,10. Fair-die expectations10each; statistic(4+1+0+1+4+0)/10=1,df5. With p≈0.9626, fail to reject fairness at5%; do not claim the die is proved fair.'
]),[
 (r'A stated distribution has probabilities0.5,0.3,0.2. Observed counts in100trials are40,35,25. Compute expected counts, statistic anddf, using critical value5.991at5%.',r'E50,30,20. χ²=100/50+25/30+25/20=49/12≈4.0833;df2. It is below5.991, so fail to reject. Insufficient evidence that the category proportions differ from the stated model.'),
 (r'A two-way2×2table is [[30,10],[10,30]]. Compute independence expectations and the test decision at5%using critical3.841.',r'Row and column totals40each,N80, so each expectation20. Statistic4(100/20)=20;df1. Reject independence because20&gt;3.841. This establishes statistical association, not a causal mechanism.')])
