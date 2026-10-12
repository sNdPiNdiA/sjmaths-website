from ib_content import *
ai='applications-and-interpretation-sl/number-and-algebra/'
expand(ai+'financial-applications-and-amortization',card('Payments, annuities and effective rates',[
 r'<strong>Align the time units:</strong> with periodic decimal rate $i$ and N payments, END mode means payments occur after each period’s interest. BEGIN mode means before it. For unequal compounding and payment frequencies, the effective payment-period rate is $(1+j/k)^{k/m}-1$ for annual decimal nominal rate j, k compounds and m payments.',
 r'<strong>Ordinary savings annuity:</strong> deposits P at period ends give $FV=P((1+i)^N-1)/i$. BEGIN deposits give an extra factor $(1+i)$. At zero interest both formulas reduce to NP.',
 r'<strong>Loan repayments:</strong> $P=PV\,i/(1-(1+i)^{-N})$. After an END payment, $B_t=B_{t-1}(1+i)-P$; interest is $iB_{t-1}$ and principal repaid is P minus interest.',
 r'<strong>Effective annual rate:</strong> $(1+j/k)^k-1$. Compare offers on the same effective basis, including fees and realistic repayment terms.',
 'Calculator workflow: clear old settings; enter N, annual I%, P/Y, C/Y, PV, PMT, FV and END/BEGIN. Use opposite cash-flow signs for receipts and payments. Substitute the output into a recurrence or formula to check it.',
 'Keep unrounded values during calculation. Actual payments rounded to cents may require an adjusted final payment. A negative outstanding balance means an overpayment, not another full payment.'
])+card('Worked amortization schedule',[
 r'Loan 1000, interest 1% per month, end-of-month payments 400: month 1 interest10, principal390, balance610; month2 interest6.10, principal393.90, balance216.10.',
 r'Month3 balance before payment is $216.10(1.01)=218.261$. Final payment is 218.26 rounded to cents, rather than 400. Total interest is approximately24.26.',
 'Check balances, total principal and payment timing. Taxes, changing rates and late fees are outside this fixed-rate model.'
]),[
 (r'Deposit 200 at each year end for 3 years at 5% annual interest. Find the balance and explain the timeline.',r'$200(1.05^2+1.05+1)=630.50$. The first deposit earns two years’ interest, the last none.'),
 (r'Repeat with deposits at the beginning of each year.',r'Each deposit earns one more year: $630.50(1.05)=662.025$, or662.03. BEGIN and END are different models.'),
 (r'Compare 6% compounded monthly with 6.1% compounded annually, ignoring fees.',r'Monthly effective rate $(1.005)^{12}-1\approx6.16778\%$, so it produces the greater one-year growth. Compare effective rates, not nominal percentages.'),
 (r'A loan of1000 at1% monthly has payments400 at month ends. Construct its repayment schedule.',r'Month1: interest10, balance610. Month2: interest6.10, balance216.10. Month3: interest2.161, final payment218.261 before rounding. Total interest24.261.'),
 (r'How many complete years are needed for1000 to exceed1500 at5% annual interest?',r'$n>\ln1.5/\ln1.05\approx8.3104$. Minimum9: year8 about1477.46, year9 about1551.33.'),
 (r'A balance5000 accrues1% monthly interest. A customer pays40 at each month end. Describe the first month and whether the debt shrinks.',r'Interest50 exceeds payment40; new balance5010. Under this fixed rate and payment, the balance grows. Paying regularly does not guarantee amortization.'),
 (r'Find the year-end deposit needed to accumulate5000 in4years at4% annual interest.',r'$P=5000(0.04)/(1.04^4-1)\approx1177.45023$, or1177.45. N4, END, PV0, FV5000; PMT has the opposite sign to FV.')])
p=ROOT/ai/'financial-applications-and-amortization/index.html';s=p.read_text(encoding='utf-8').replace('is required.</li>','can be used.</li>').replace('Official Financial Mathematics Formulas','Financial Mathematics Formulas');s=s.replace('If both $PV$ and $PMT$ have the same sign when modeling a savings annuity, the calculator will return an error or negative future balance.','For a loan, PV and PMT have opposite signs. For savings, the initial investment and recurring deposits can have the same sign; the eventual withdrawal FV has the opposite sign.');p.write_text(s,encoding='utf-8')
expand(ai+'systems-of-linear-equations',card('Elimination, classification and validation',[
 r'<strong>Elimination:</strong> multiply entire equations to make one variable’s coefficients equal, subtract, solve the reduced equation, then substitute back. Example $2x+y=10$, $x-y=2$ gives $3x=12$, x4,y2.',
 r'<strong>Two-variable determinant:</strong> $a_1b_2-a_2b_1\ne0$ gives one solution. If zero, eliminate and distinguish $0=0$ from $0=c\ne0$. The slope description applies only to nonvertical lines.',
 r'<strong>Worked classifications:</strong> $x+y=3,\;2x+2y=6$ gives $(x,y)=(t,3-t)$ for any real t. Replacing6by7 gives no solution.',
 'Three different equations need not be independent. Three planes can intersect in a point or a line, coincide, or have no common point. A singular coefficient matrix does not itself distinguish no solution from infinitely many.',
 'For calculator input keep the variable order fixed and enter0 for missing coefficients. Check every original equation. A solver error requires classification; it is not proof of no solution.',
 'Define quantities and units before forming equations. Nonnegative weights and whole-number counts are contextual constraints; a unique real solution can still be infeasible.'
]),[
 (r'Solve $3x+2y=16$, $x-y=2$ by elimination.',r'Twice the second equation added to the first gives5x20; x4,y2. Checks:12+4=16 and4−2=2.'),
 (r'Classify $x+2y=5$, $2x+4y=10$ and describe every solution.',r'The second equation is twice the first. Infinitely many: $(x,y)=(5-2t,t)$, t real.'),
 (r'Classify $x+2y=5$, $2x+4y=11$.',r'Subtract twice the first from the second to get0=1. No solution; the lines are parallel and distinct.'),
 (r'Solve $x=3$, $2x+y=8$ and explain why slopes are unnecessary.',r'Substitute x3 to obtainy2. The vertical line and oblique line meet at(3,2).'),
 (r'Solve $x+y+z=6$, $x-y+z=2$, $2x+y-z=1$.',r'Subtract first two to gety2. Then x+z4 and2x−z=−1, sox1,z3. Check each equation:6,2,1.'),
 (r'Find all solutions of $x+y+z=6$, $2x+2y+2z=12$, $x-y=0$.',r'x=y=t,z=6−2t. The first two equations are dependent. If all quantities are nonnegative,0≤t≤3.'),
 (r'A 10kg mixture uses ingredients costing2/kg and5/kg. The total cost is32. Find both masses.',r'Let x,ykg: x+y10,2x+5y32. Subtract2(x+y) to get3y12, so y4,x6. Units and nonnegativity are valid.'),
 (r'A box contains10 items costing2 or5 each, with total cost31. Is the model feasible for whole items?',r'x+y10,2x+5y31 givesy11/3,x19/3. This is a unique real solution but not a valid whole-item count; the stated data cannot describe such a box.')],quizzes=[
 ('Elimination gives0=7. What follows?',['One solution','Infinitely many','No solution','A zero variable'],'C','A contradiction makes the system inconsistent.'),
 ('A ticket system gives2.5adult tickets. What should you conclude?',['Round to3','Ignore the fraction','Check model feasibility','Every real solution is valid'],'C','Ticket counts must be integers; do not round a system solution.'),
 ('Two proportional equations give0=0. How many real solutions for two unknowns?',['None','One','Two','Infinitely many'],'D','The equations describe the same line, leaving one free parameter.')])
p=ROOT/ai/'systems-of-linear-equations/index.html';s=p.read_text(encoding='utf-8').replace('three distinct linear relationships','three independent linear relationships for a unique solution').replace('The slopes are different ($m_1 \\ne m_2$).','For nonvertical lines, the slopes are different ($m_1 \\ne m_2$).').replace('check your equation coefficients for sign errors.','check the equations and the feasibility of the original data. A correct algebraic solution can be physically impossible.');p.write_text(s,encoding='utf-8')
