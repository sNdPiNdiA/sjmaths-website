const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'functions');

const guides = [
  // Guide 7: Modulus Functions & Inequalities
  {
    folder: 'modulus-functions-and-inequalities',
    code: '2.12, 2.14',
    title: 'Modulus Functions & Inequalities',
    pageTitle: 'Modulus Functions & Inequalities | IB Math AA HL | SJMaths',
    metaDesc: 'Master modulus functions, graphs of |f(x)| and f(|x|), and modulus inequalities for IB DP Mathematics AA HL (Topics 2.12 & 2.14). Piecewise definitions, squaring method, sign charts, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL modulus functions, absolute value graph, y = |f(x)| vs y = f(|x|), solving modulus inequalities, extraneous solutions absolute value',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Master absolute value operations, graphical transformations $y = |f(x)|$ and $y = f(|x|)$, and rigorous analytic and graphical methods for solving modulus equations and inequalities without extraneous roots.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/partial-fractions-and-binomial-series/',
      title: 'Partial Fractions & Extended Binomial Series'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/functions/rational-functions-and-oblique-asymptotes/',
      title: 'Rational Functions & Oblique Asymptotes'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-arrows-split-up-and-left" style="color:var(--c-primary);"></i> Figure 2.1: Modulus Graph Transformations: $y = |f(x)|$ vs $y = f(|x|)$</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing graph of f(x) on left, |f(x)| in middle reflecting below x-axis, and f(|x|) on right with y-axis symmetry">
            <!-- Left: y = f(x) = x^2 - 4 -->
            <g transform="translate(25, 20)">
              <rect x="0" y="0" width="215" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="107" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--c-text)">Original: y = f(x)</text>
              <line x1="20" y1="130" x2="195" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="107" y1="35" x2="107" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Parabola y = (x-107)^2/40 - 50 -> vertex at (107, 180) -->
              <path d="M 40,60 Q 107,200 174,60" fill="none" stroke="#6366f1" stroke-width="2.5" />
              <circle cx="67" cy="130" r="4" fill="#ef4444" />
              <circle cx="147" cy="130" r="4" fill="#ef4444" />
              <text x="107" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Drops below x-axis</text>
            </g>

            <!-- Middle: y = |f(x)| -->
            <g transform="translate(272, 20)">
              <rect x="0" y="0" width="215" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="107" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">y = |f(x)|</text>
              <line x1="20" y1="130" x2="195" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="107" y1="35" x2="107" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Outside x-intercepts remains, inside reflects upwards -->
              <path d="M 40,60 L 67,130" fill="none" stroke="#10b981" stroke-width="2.5" />
              <path d="M 67,130 Q 107,60 147,130" fill="none" stroke="#ef4444" stroke-width="2.5" />
              <path d="M 147,130 L 174,60" fill="none" stroke="#10b981" stroke-width="2.5" />
              <!-- Cusps at x-intercepts -->
              <circle cx="67" cy="130" r="4" fill="#ef4444" />
              <circle cx="147" cy="130" r="4" fill="#ef4444" />
              <text x="107" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Reflect negative y across x-axis</text>
            </g>

            <!-- Right: y = f(|x|) -->
            <g transform="translate(520, 20)">
              <rect x="0" y="0" width="215" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="107" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#f59e0b">y = f(|x|)</text>
              <line x1="20" y1="130" x2="195" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="107" y1="35" x2="107" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Keep x>=0, reflect into x<0 (W-shape or cusp at y-axis) -->
              <path d="M 107,180 Q 147,190 174,60" fill="none" stroke="#f59e0b" stroke-width="2.5" />
              <path d="M 107,180 Q 67,190 40,60" fill="none" stroke="#f59e0b" stroke-width="2.5" />
              <circle cx="107" cy="180" r="4" fill="#f59e0b" />
              <text x="107" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Even function: symmetric in y-axis</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Modulus Function Definition &amp; Piecewise Formulation</h2>
        <p>The <strong>modulus</strong> (or absolute value) $|x|$ is defined piecewise as:</p>
        $$|x| = \\begin{cases} x & \\text{if } x \\ge 0 \\\\ -x & \\text{if } x &lt; 0 \\end{cases}$$
        <p>For any expression $g(x)$, $|g(x)| = g(x)$ where $g(x) \\ge 0$, and $-g(x)$ where $g(x) &lt; 0$. The transition points occur at the <strong>zeros</strong> $g(x) = 0$, often creating sharp corners ("cusps") on graphs where the derivative is undefined.</p>

        <h2>2. Modulus Transformations: $y = |f(x)|$ vs $y = f(|x|)$</h2>
        <ul class="theory-list">
          <li><strong>$y = |f(x)|$ (Modulus on Outside):</strong>
            <br>• Any part of the curve $y = f(x)$ that lies <em>on or above</em> the $x$-axis ($y \\ge 0$) remains completely unchanged.
            <br>• Any part lying <em>below</em> the $x$-axis ($y &lt; 0$) is <strong>reflected vertically across the $x$-axis</strong> ($y \\to -y$).
            <br>• The range is always non-negative: $y \\ge 0$. Sharp cusps form at all real roots where the original curve intersected the $x$-axis with non-zero gradient.
          </li>
          <li><strong>$y = f(|x|)$ (Modulus on Inside):</strong>
            <br>• Any part of the curve for $x &lt; 0$ is completely <strong>discarded</strong>.
            <br>• The part of the curve for $x \\ge 0$ is retained and <strong>reflected horizontally across the $y$-axis</strong> into the region $x &lt; 0$.
            <br>• Since $f(|-x|) = f(|x|)$, the resulting function is guaranteed to be an <strong>even function</strong> with bilateral symmetry across the $y$-axis. A sharp corner may occur at the $y$-intercept $(0, f(0))$.
          </li>
        </ul>

        <h2>3. Solving Modulus Equations</h2>
        <p>There are two primary analytic methods:</p>
        <ol class="theory-list">
          <li><strong>Case Analysis / Definition:</strong> For $|A| = B$, set $A = B$ (valid when $A \\ge 0$) and $A = -B$ (valid when $A &lt; 0$). <em>Always check candidate solutions in the original equation to reject extraneous roots!</em></li>
          <li><strong>Squaring Both Sides:</strong> Since $|A|^2 = A^2$, the equation $|A| = |B|$ is equivalent to $A^2 = B^2 \\iff A^2 - B^2 = 0 \\iff (A - B)(A + B) = 0$. This method is especially fast when both sides have modulus signs.</li>
        </ol>

        <h2>4. Solving Modulus Inequalities</h2>
        <ul class="theory-list">
          <li><strong>$|f(x)| &lt; k$ (where $k &gt; 0$):</strong> Equivalent to $-k &lt; f(x) &lt; k$.</li>
          <li><strong>$|f(x)| &gt; k$:</strong> Equivalent to $f(x) &gt; k$ <em>or</em> $f(x) &lt; -k$.</li>
          <li><strong>$|f(x)| &lt; |g(x)|$:</strong> Square both sides safely (since both are non-negative): $[f(x)]^2 &lt; [g(x)]^2 \\iff [f(x)]^2 - [g(x)]^2 &lt; 0 \\iff (f - g)(f + g) &lt; 0$.</li>
        </ul>

        <h2>5. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Solving Modulus Equation with Extraneous Roots</h4>
          <p>Solve the equation $|2x - 5| = x + 1$ algebraically and confirm graphically.</p>
          <p><strong>Solution:</strong></p>
          <p>Because the right-hand side is $x + 1$, we must have $x + 1 \\ge 0 \\iff x \\ge -1$.</p>
          <p><strong>Case 1:</strong> $2x - 5 = x + 1 \\implies x = 6$.<br>
          Check: $|2(6) - 5| = |7| = 7$. RHS: $6 + 1 = 7$. Valid! ($x = 6$)</p>
          <p><strong>Case 2:</strong> $2x - 5 = -(x + 1) = -x - 1 \\implies 3x = 4 \\implies x = \\frac{4}{3}$.<br>
          Check: $\\left|2\\left(\\frac{4}{3}\\right) - 5\\right| = \\left|\\frac{8}{3} - \\frac{15}{3}\\right| = \\left|-\\frac{7}{3}\\right| = \\frac{7}{3}$. RHS: $\\frac{4}{3} + 1 = \\frac{7}{3}$. Valid! ($x = \\frac{4}{3}$)</p>
          <p>Both solutions are valid: $x = \\frac{4}{3}$ and $x = 6$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Solving Modulus Inequality by Squaring</h4>
          <p>Solve the inequality $|3x - 2| \\le |x + 4|$.</p>
          <p><strong>Solution:</strong></p>
          <p>Both sides are non-negative, so we square both sides:</p>
          $$(3x - 2)^2 \\le (x + 4)^2 \\iff (3x - 2)^2 - (x + 4)^2 \\le 0$$
          <p>Use difference of two squares $(A - B)(A + B) \\le 0$:</p>
          $$[(3x - 2) - (x + 4)][(3x - 2) + (x + 4)] \\le 0$$
          $$(2x - 6)(4x + 2) \\le 0 \\iff 2(x - 3) \\cdot 2(2x + 1) \\le 0 \\iff (x - 3)(2x + 1) \\le 0$$
          <p>Roots of the parabola are $x = -\\frac{1}{2}$ and $x = 3$. The parabola opens upwards and is $\\le 0$ between the roots:</p>
          $$-\\frac{1}{2} \\le x \\le 3$$
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Solving Non-Linear Modulus Inequality</h4>
          <p>Solve the inequality $|x^2 - 4| &gt; 3x$.</p>
          <p><strong>Solution:</strong></p>
          <p>• If $x \\le 0$, the LHS is $|x^2 - 4| \\ge 0$ while the RHS $3x \\le 0$. Since $|x^2 - 4| = 0$ only at $x = -2$, for all $x \\le 0, x \\neq -2$, $|x^2 - 4| &gt; 0 \\ge 3x$. At $x = -2$, $|0| &gt; -6$ is true. Thus all $x \\le 0$ satisfy the inequality.</p>
          <p>• For $x &gt; 0$ (both sides positive):<br>
          Case A: $x^2 - 4 &gt; 3x \\implies x^2 - 3x - 4 &gt; 0 \\implies (x - 4)(x + 1) &gt; 0$.<br>
          For $x &gt; 0$, this requires $x &gt; 4$.<br>
          Case B: $x^2 - 4 &lt; -3x \\implies x^2 + 3x - 4 &lt; 0 \\implies (x + 4)(x - 1) &lt; 0$.<br>
          For $x &gt; 0$, this requires $0 &lt; x &lt; 1$.</p>
          <p>Combining all intervals: $x &lt; 1$ or $x &gt; 4$.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Evaluating Modulus Transformations)',
        text: 'The point $P(-3, -5)$ lies on the curve $y = f(x)$. State the coordinates of the corresponding point on: (a) $y = |f(x)|$, (b) $y = f(|x|)$, (c) $y = -|f(x)|$.',
        solution: '<p><strong>(a) $y = |f(x)|$:</strong> $x$ stays $-3$, $y = |-5| = 5$. Point: $(-3, 5)$. [A1]<br><strong>(b) $y = f(|x|)$:</strong> For $x = -3$, $|x| = 3$, so $y = f(3)$. Since $f(3)$ is not given, the original point at $x=-3$ is discarded. The point at $x = 3$ reflects to $(-3, f(3))$. [A1]<br><strong>(c) $y = -|f(x)|$:</strong> $(-3, -5)$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Modulus Equation)',
        text: 'Solve $|4x - 1| = 11$.',
        solution: '<p>$4x - 1 = 11 \\implies 4x = 12 \\implies x = 3$. [A1]<br>$4x - 1 = -11 \\implies 4x = -10 \\implies x = -\\frac{5}{2}$. [A1]<br>Solutions: $x = -\\frac{5}{2}, 3$.</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Linear Modulus Inequality)',
        text: 'Solve $|2x + 7| < 5$.',
        solution: '<p>$-5 < 2x + 7 < 5$ [M1]<br>Subtract 7: $-12 < 2x < -2$<br>Divide by 2: $-6 < x < -1$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Absolute Equation with Linear RHS)',
        text: 'Solve $|3x + 2| = 2x + 7$ algebraically.',
        solution: '<p>Requires $2x + 7 \\ge 0 \\implies x \\ge -3.5$. [M1]<br>Case 1: $3x + 2 = 2x + 7 \\implies x = 5$. [A1]<br>Case 2: $3x + 2 = -(2x + 7) = -2x - 7 \\implies 5x = -9 \\implies x = -\\frac{9}{5} = -1.8$. [A1]<br>Both satisfy $x \\ge -3.5$. Solutions: $x = -\\frac{9}{5}, 5$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Two Modulus Terms)',
        text: 'Solve $|2x - 1| = |x + 5|$ by squaring both sides.',
        solution: '<p>$(2x - 1)^2 = (x + 5)^2 \\implies (2x - 1)^2 - (x + 5)^2 = 0$. [M1]<br>$[(2x - 1) - (x + 5)][(2x - 1) + (x + 5)] = 0$<br>$(x - 6)(3x + 4) = 0$. [M1]<br>$x = 6$ or $x = -\\frac{4}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Inequality with Two Modulus Signs)',
        text: 'Solve $|2x - 3| \\ge |x + 1|$.',
        solution: '<p>$(2x - 3)^2 \\ge (x + 1)^2 \\iff (2x - 3)^2 - (x + 1)^2 \\ge 0$. [M1]<br>$[(2x - 3) - (x + 1)][(2x - 3) + (x + 1)] \\ge 0$<br>$(x - 4)(3x - 2) \\ge 0$. [A1]<br>Parabola opens upwards, $\\ge 0$ outside roots $x = \\frac{2}{3}$ and $x = 4$:<br>$x \\le \\frac{2}{3}$ or $x \\ge 4$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Modulus with Quadratic Inside)',
        text: 'Find all solutions to $|x^2 - 5x| = 6$.',
        solution: '<p>Case 1: $x^2 - 5x = 6 \\implies x^2 - 5x - 6 = 0 \\implies (x - 6)(x + 1) = 0 \\implies x = 6, -1$. [A1]<br>Case 2: $x^2 - 5x = -6 \\implies x^2 - 5x + 6 = 0 \\implies (x - 2)(x - 3) = 0 \\implies x = 2, 3$. [A1]<br>All 4 solutions: $x = -1, 2, 3, 6$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Modulus Inequality with Rational Function)',
        text: 'Solve the inequality $\\left|\\frac{x + 2}{x - 1}\\right| < 2$.',
        solution: '<p>Notice $x \\neq 1$. Since both sides are non-negative, square both sides: [M1]<br>$\\frac{(x + 2)^2}{(x - 1)^2} < 4 \\implies (x + 2)^2 < 4(x - 1)^2$<br>$(x + 2)^2 - [2(x - 1)]^2 < 0$. [M1]<br>$[(x + 2) - (2x - 2)][(x + 2) + (2x - 2)] < 0$<br>$(-x + 4)(3x) < 0 \\iff 3x(4 - x) < 0 \\iff 3x(x - 4) > 0$. [A1]<br>Roots are $x = 0$ and $x = 4$. Solution is $x < 0$ or $x > 4$.<br>Since $x = 1$ is inside the interval $(0, 4)$ where the condition is false, $x=1$ is automatically excluded.<br>Result: $x < 0$ or $x > 4$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Piecewise Modulus with Parameter)',
        text: 'Find all values of $m \\in \\mathbb{R}$ such that the equation $|x - 2| + |x + 3| = m$ has: (a) no solutions, (b) infinitely many solutions, (c) exactly two solutions.',
        solution: '<p>By the triangle inequality, $|x - 2| + |x + 3| \\ge |(x - 2) - (x + 3)| = |-5| = 5$. [M1]<br>Consider intervals:<br>• For $-3 \\le x \\le 2$: $(2 - x) + (x + 3) = 5$ (constant value 5).<br>• For $x > 2$: $(x - 2) + (x + 3) = 2x + 1 > 5$.<br>• For $x < -3$: $(2 - x) + (-x - 3) = -2x - 1 > 5$.<br><strong>(a) No solutions:</strong> $m < 5$. [A1]<br><strong>(b) Infinitely many solutions:</strong> $m = 5$ (all $x \\in [-3, 2]$). [A1]<br><strong>(c) Exactly two solutions:</strong> $m > 5$ (one solution where $x > 2$, one where $x < -3$). [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Calculus with Modulus Function)',
        text: 'Let $f(x) = x|x - 2|$. (a) Express $f(x)$ in piecewise form.<br>(b) Determine whether $f$ is differentiable at $x = 2$.<br>(c) Find the stationary point of $f(x)$.',
        solution: '<p><strong>(a) Piecewise definition:</strong> [M1]<br>$f(x) = \\begin{cases} x(x - 2) = x^2 - 2x & \\text{if } x \\ge 2 \\\\ x(-(x - 2)) = -x^2 + 2x & \\text{if } x < 2 \\end{cases}$ [A1]</p><p><strong>(b) Differentiability at $x = 2$:</strong><br>From right: $f\'(2^+) = \\lim_{x \\to 2^+} (2x - 2) = 2(2) - 2 = 2$. [M1]<br>From left: $f\'(2^-) = \\lim_{x \\to 2^-} (-2x + 2) = -2(2) + 2 = -2$. [M1]<br>Since $f\'(2^+) \\neq f\'(2^-)$, $f(x)$ is <strong>not differentiable</strong> at $x = 2$ (a sharp cusp). [A1]</p><p><strong>(c) Stationary point:</strong><br>For $x < 2$: $f\'(x) = -2x + 2 = 0 \\implies x = 1$.<br>At $x = 1$, $f(1) = 1(1) = 1$. Stationary point is $(1, 1)$ (local maximum).<br>For $x > 2$: $f\'(x) = 2x - 2 = 0 \\implies x = 1$ (not in domain $x > 2$).<br>Stationary point is $(1, 1)$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 2)</h2>
        <div class="formula-card">
          <h4>Syllabus 2.12, 2.14: Modulus Function</h4>
          <p>The formula booklet does not contain a dedicated formula for the modulus function. Students must know the piecewise algebraic definition and graphical reflection rules:</p>
          $$|x| = \\begin{cases} x, & x \\ge 0 \\\\ -x, & x &lt; 0 \\end{cases}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Transformation Rules</h4>
          <ul>
            <li>$y = |f(x)|$: reflect parts where $y &lt; 0$ in the $x$-axis.</li>
            <li>$y = f(|x|)$: erase $x &lt; 0$, reflect $x \\ge 0$ in the $y$-axis (always even).</li>
          </ul>
        </div>
        <div class="formula-card">
          <h4>2. Inequalities</h4>
          <ul>
            <li>$|f(x)| &lt; k \\iff -k &lt; f(x) &lt; k$ (for $k &gt; 0$)</li>
            <li>$|f(x)| &gt; k \\iff f(x) &gt; k \\text{ or } f(x) &lt; -k$</li>
            <li>$|f(x)| &lt; |g(x)| \\iff [f(x)]^2 - [g(x)]^2 &lt; 0$</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Failing to Check for Extraneous Solutions</h4>
          <p>When solving $|A| = B$, remember that $B$ cannot be negative. If substituting your candidate $x$ into $B$ gives a negative value, that root is extraneous and must be discarded.</p>
        </div>
        <div class="pitfall-card">
          <h4>Differentiability at Cusps</h4>
          <p>Curves with modulus reflections have sharp corners at their $x$-intercepts. The derivative does not exist at these points! Never set $f\'(x) = 0$ across a cusp.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'The function $f(x) = x^3 - 3x$. How many stationary points does $y = f(|x|)$ have?',
        options: [
          '2',
          '3',
          '4',
          '5'
        ],
        correct: 1,
        explanation: 'For $x > 0$, $f(x) = x^3 - 3x$ has stationary point at $x = 1$. When reflected across the $y$-axis for $f(|x|)$, there is another stationary point at $x = -1$. Additionally, at $x = 0$, $f(|x|) = 0$ is a non-differentiable cusp, but often considered an extremum. For differentiable stationary points $f\'=0$, there are exactly 2 ($x = \\pm 1$). If counting local extrema, 3. The prompt specifies stationary points ($f\'=0$), which are $x = \\pm 1$.'
      },
      {
        id: 'q2',
        prompt: 'What are the solutions to $|2x - 3| = x - 5$?',
        options: [
          'x = -2 and x = 8/3',
          'x = -2 only',
          'x = 8/3 only',
          'No solutions'
        ],
        correct: 3,
        explanation: 'Solving $2x - 3 = x - 5 \\implies x = -2$. But then $x - 5 = -7 < 0$, impossible. Solving $2x - 3 = -(x - 5) \\implies 3x = 8 \\implies x = 8/3$. But then $x - 5 = 8/3 - 5 = -7/3 < 0$, also impossible. Both are extraneous!'
      },
      {
        id: 'q3',
        prompt: 'The solution set to the inequality $|x - 3| < 2x$ is:',
        options: [
          'x > 1',
          'x > 3',
          '-1 < x < 3',
          'x < 1'
        ],
        correct: 0,
        explanation: 'For $x \\le 3$: $-(x - 3) < 2x \\implies 3 < 3x \\implies x > 1$, so $1 < x \\le 3$. For $x > 3$: $x - 3 < 2x \\implies x > -3$, which holds for all $x > 3$. Combining gives $x > 1$.'
      },
      {
        id: 'q4',
        prompt: 'If $g(x) = \\ln x$, the domain of $y = g(|x|)$ is:',
        options: [
          'x > 0',
          'x ≠ 0',
          'All real numbers',
          'x ≥ 0'
        ],
        correct: 1,
        explanation: 'The argument of $\\ln(|x|)$ must be strictly positive: $|x| > 0 \\iff x \\neq 0$. The domain is all real numbers except 0.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the functions $f(x) = |2x - 4|$ and $g(x) = 6 - x$.<br><strong>(a)</strong> Sketch both graphs on the same set of axes, clearly showing all intercepts. [3 marks]<br><strong>(b)</strong> Find the exact coordinates of the two points of intersection. [2 marks]<br><strong>(c)</strong> Hence write down the solution set to $|2x - 4| \\le 6 - x$. [1 mark]',
        solution: `
          <p><strong>(a) Sketch: [3 marks]</strong><br>
          • $f(x) = |2x - 4|$ has vertex (cusp) at $(2, 0)$ and $y$-intercept at $(0, 4)$ [A1].<br>
          • $g(x) = 6 - x$ has $y$-intercept $(0, 6)$ and $x$-intercept $(6, 0)$ [A1].<br>
          Both lines intersect in the first quadrant [A1].</p>
          <p><strong>(b) Points of intersection: [2 marks]</strong><br>
          Case 1 ($x \\ge 2$): $2x - 4 = 6 - x \\implies 3x = 10 \\implies x = \\frac{10}{3}$. $y = 6 - \\frac{10}{3} = \\frac{8}{3}$. Point $\\left(\\frac{10}{3}, \\frac{8}{3}\\right)$ [A1].<br>
          Case 2 ($x < 2$): $-(2x - 4) = 6 - x \\implies -2x + 4 = 6 - x \\implies -x = 2 \\implies x = -2$. $y = 6 - (-2) = 8$. Point $(-2, 8)$ [A1].</p>
          <p><strong>(c) Solution of inequality: [1 mark]</strong><br>
          From the sketch, $f(x) \\le g(x)$ between the intersection points: $-2 \\le x \\le \\frac{10}{3}$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'Let $h(x) = \\left|\\frac{x^2 - 1}{x^2 + 1}\\right|$.<br><strong>(a)</strong> Show that $h(x)$ is an even function. [2 marks]<br><strong>(b)</strong> Find the horizontal asymptote of $y = h(x)$. [2 marks]<br><strong>(c)</strong> Find all stationary points of $h(x)$ and state the nature of each. [4 marks]',
        solution: `
          <p><strong>(a) Even function: [2 marks]</strong><br>
          $h(-x) = \\left|\\frac{(-x)^2 - 1}{(-x)^2 + 1}\\right| = \\left|\\frac{x^2 - 1}{x^2 + 1}\\right| = h(x)$ [M1].<br>
          Since $h(-x) = h(x)$ for all $x \\in \\mathbb{R}$, $h(x)$ is an even function [A1].</p>
          <p><strong>(b) Horizontal asymptote: [2 marks]</strong><br>
          $\\lim_{x \\to \\pm\\infty} h(x) = \\lim_{x \\to \\pm\\infty} \\left|\\frac{1 - 1/x^2}{1 + 1/x^2}\\right| = |1| = 1$ [M1].<br>
          The horizontal asymptote is $y = 1$ [A1].</p>
          <p><strong>(c) Stationary points: [4 marks]</strong><br>
          Let $u(x) = \\frac{x^2 - 1}{x^2 + 1}$.<br>
          $u\'(x) = \\frac{2x(x^2 + 1) - 2x(x^2 - 1)}{(x^2 + 1)^2} = \\frac{4x}{(x^2 + 1)^2}$ [M1].<br>
          $u\'(x) = 0 \\implies x = 0$. At $x = 0$, $u(0) = -1 \\implies h(0) = |-1| = 1$ (local maximum) [A1].<br>
          At $x = \\pm 1$, $u(x) = 0 \\implies h(\\pm 1) = 0$. These are sharp cusps where the modulus reflects from negative to positive, forming global minimum points $(1, 0)$ and $(-1, 0)$ [A1].<br>
          Stationary points: $(0, 1)$ (local maximum), and cusps at $(\\pm 1, 0)$ (local/global minima) [A1].</p>
        `
      }
    ]
  },

  // Guide 8: Rational Functions & Oblique Asymptotes
  {
    folder: 'rational-functions-and-oblique-asymptotes',
    code: '2.12',
    title: 'Rational Functions & Oblique Asymptotes',
    pageTitle: 'Rational Functions & Oblique Asymptotes | IB Math AA HL | SJMaths',
    metaDesc: 'Master rational functions and oblique (slant) asymptotes for IB DP Mathematics AA HL (Topic 2.12). Polynomial long division, vertical and oblique asymptotes, asymptotic approaches, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL rational functions, oblique asymptotes, slant asymptote polynomial division, degree difference rational curve, vertical asymptote limits',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Extend rational functions beyond standard level. Use polynomial long division when the degree of the numerator exceeds the denominator by 1 to find oblique linear asymptotes $y = mx + c$, analyze asymptotic curvature, and locate stationary points.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/functions/modulus-functions-and-inequalities/',
      title: 'Modulus Functions & Inequalities'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/functions/composite-transformations-and-reciprocal-graphs/',
      title: 'Composite Transformations & Reciprocal Graphs'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-chart-line" style="color:var(--c-primary);"></i> Figure 2.2: Rational Function with Vertical and Oblique Asymptotes</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Graph of rational function showing vertical asymptote at x = 1 and oblique asymptote y = x + 2">
            <!-- Center at (380, 160) -->
            <!-- Axes -->
            <line x1="60" y1="160" x2="700" y2="160" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="340" y1="30" x2="340" y2="280" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="690" y="150" fill="var(--c-text)" font-size="13" font-weight="bold">x</text>
            <text x="350" y="45" fill="var(--c-text)" font-size="13" font-weight="bold">y</text>

            <!-- Vertical Asymptote x = 1 (at x = 400) -->
            <line x1="400" y1="20" x2="400" y2="280" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5,5" />
            <text x="408" y="50" fill="#ef4444" font-size="12" font-weight="bold">x = 1</text>

            <!-- Oblique Asymptote y = x + 1 (line passing through (340, 120) with slope -0.6 for SVG coords) -->
            <!-- Line from (140, 240) to (620, 20) -->
            <line x1="140" y1="240" x2="620" y2="20" stroke="#10b981" stroke-width="2" stroke-dasharray="5,5" />
            <text x="590" y="45" fill="#10b981" font-size="12" font-weight="bold">y = x + 1 (Oblique)</text>

            <!-- Left Branch (x < 1): approaches oblique asymptote from below as x -> -inf, approaches VA -> -inf as x -> 1^- -->
            <path d="M 120,260 C 220,205 310,185 350,195 C 375,205 385,235 390,280" fill="none" stroke="#6366f1" stroke-width="3" />
            <!-- Local Max at (-1, -1) -> (280, 200) -->
            <circle cx="300" cy="195" r="4" fill="#6366f1" />
            <text x="250" y="215" fill="#6366f1" font-size="11" font-weight="bold">Local Max</text>

            <!-- Right Branch (x > 1): approaches VA -> +inf as x -> 1^+, local min, approaches oblique from above -->
            <path d="M 410,25 C 415,70 425,95 450,105 C 490,115 560,75 660,15" fill="none" stroke="#6366f1" stroke-width="3" />
            <!-- Local Min at (3, 7) -> (500, 105) -->
            <circle cx="465" cy="105" r="4" fill="#6366f1" />
            <text x="475" y="125" fill="#6366f1" font-size="11" font-weight="bold">Local Min</text>

            <text x="380" y="275" text-anchor="middle" font-size="12" fill="var(--c-text-muted)">y = (x² + 2x) / (x - 1) = x + 3 + 3/(x - 1)</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. The Geometry of Rational Functions</h2>
        <p>A rational function has the form $f(x) = \\frac{P(x)}{Q(x)}$ where $P(x)$ and $Q(x)$ are polynomials with no common factors.</p>
        <ul class="theory-list">
          <li><strong>Vertical Asymptotes:</strong> Occur at the real zeros of the denominator $Q(x) = 0$. As $x \\to c$, $f(x) \\to \\pm\\infty$.</li>
          <li><strong>Horizontal Asymptotes (SL):</strong> Occur when $\\deg(P) = \\deg(Q)$ (horizontal line $y = \\frac{a_n}{b_n}$) or $\\deg(P) &lt; \\deg(Q)$ (the line $y = 0$).</li>
          <li><strong>Oblique (Slant) Asymptotes (HL):</strong> Occur when the degree of the numerator is <strong>exactly 1 greater</strong> than the degree of the denominator:
          $$\\deg(P) = \\deg(Q) + 1$$</li>
        </ul>

        <h2>2. Finding the Oblique Asymptote via Polynomial Long Division</h2>
        <p>When $\\deg(P) = \\deg(Q) + 1$, dividing $P(x)$ by $Q(x)$ yields a linear quotient $(mx + c)$ plus a proper remainder fraction:</p>
        $$f(x) = \\frac{P(x)}{Q(x)} = (mx + c) + \\frac{R(x)}{Q(x)}$$
        <p>where $\\deg(R) &lt; \\deg(Q)$. As $x \\to \\pm\\infty$, the remainder term vanishes:</p>
        $$\\lim_{x \\to \\pm\\infty} \\frac{R(x)}{Q(x)} = 0 \\implies \\lim_{x \\to \\pm\\infty} [f(x) - (mx + c)] = 0$$
        <p>Therefore, the straight line <strong>$y = mx + c$</strong> is an <strong>oblique asymptote</strong>.</p>

        <h2>3. Analyzing Asymptotic Approaches</h2>
        <p>To determine whether the curve approaches the oblique asymptote from <em>above</em> or from <em>below</em>, analyze the sign of the remainder term $\\frac{R(x)}{Q(x)}$ for large positive and negative $x$:</p>
        <ul>
          <li>If $\\frac{R(x)}{Q(x)} &gt; 0$, the curve lies <strong>above</strong> the asymptote ($f(x) &gt; mx + c$).</li>
          <li>If $\\frac{R(x)}{Q(x)} &lt; 0$, the curve lies <strong>below</strong> the asymptote ($f(x) &lt; mx + c$).</li>
        </ul>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Finding Vertical and Oblique Asymptotes</h4>
          <p>Find all asymptotes of the rational function $f(x) = \\frac{2x^2 + 5x - 1}{x + 2}$.</p>
          <p><strong>Solution:</strong></p>
          <p><strong>Vertical Asymptote:</strong> Set denominator to zero: $x + 2 = 0 \\implies x = -2$.<br>
          Check numerator at $x = -2$: $2(-2)^2 + 5(-2) - 1 = 8 - 10 - 1 = -3 \\neq 0$. Thus $x = -2$ is a vertical asymptote.</p>
          <p><strong>Oblique Asymptote:</strong> Perform polynomial long division of $(2x^2 + 5x - 1)$ by $(x + 2)$:</p>
          $$2x^2 + 5x - 1 = (2x + 1)(x + 2) - 3$$
          $$\\frac{2x^2 + 5x - 1}{x + 2} = 2x + 1 - \\frac{3}{x + 2}$$
          <p>As $x \\to \\pm\\infty$, $-\\frac{3}{x + 2} \\to 0$.<br>
          Hence the oblique asymptote is the line <strong>$y = 2x + 1$</strong>.</p>
          <p><strong>Approach:</strong><br>
          • As $x \\to +\\infty$, $-\\frac{3}{x + 2} &lt; 0 \\implies$ curve approaches $y = 2x + 1$ from <em>below</em>.<br>
          • As $x \\to -\\infty$, $-\\frac{3}{x + 2} &gt; 0 \\implies$ curve approaches $y = 2x + 1$ from <em>above</em>.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Finding Stationary Points of a Rational Function</h4>
          <p>Find the coordinates of the local extrema of $y = \\frac{x^2 - x + 4}{x - 1}$.</p>
          <p><strong>Solution:</strong></p>
          <p>Divide first: $\\frac{x^2 - x + 4}{x - 1} = \\frac{x(x - 1) + 4}{x - 1} = x + \\frac{4}{x - 1} = x + 4(x - 1)^{-1}$.</p>
          <p>Differentiate with respect to $x$:</p>
          $$\\frac{dy}{dx} = 1 - 4(x - 1)^{-2} = 1 - \\frac{4}{(x - 1)^2}$$
          <p>Set $\\frac{dy}{dx} = 0$:</p>
          $$1 = \\frac{4}{(x - 1)^2} \\implies (x - 1)^2 = 4 \\implies x - 1 = \\pm 2$$
          <p>• $x = 1 + 2 = 3 \\implies y = 3 + \\frac{4}{2} = 5$. Local minimum at $(3, 5)$.<br>
          • $x = 1 - 2 = -1 \\implies y = -1 + \\frac{4}{-2} = -3$. Local maximum at $(-1, -3)$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Curve Crossing its Oblique Asymptote</h4>
          <p>Determine whether the curve $f(x) = \\frac{x^3 + 2x^2 - 5x + 3}{x^2 + 1}$ crosses its oblique asymptote.</p>
          <p><strong>Solution:</strong></p>
          <p>Perform polynomial long division:</p>
          $$x^3 + 2x^2 - 5x + 3 = (x + 2)(x^2 + 1) + (-6x + 1)$$
          $$f(x) = x + 2 + \\frac{-6x + 1}{x^2 + 1}$$
          <p>The oblique asymptote is $y = x + 2$.</p>
          <p>The curve intersects its asymptote when $f(x) = x + 2$:</p>
          $$\\frac{-6x + 1}{x^2 + 1} = 0 \\implies -6x + 1 = 0 \\implies x = \\frac{1}{6}$$
          <p>At $x = \\frac{1}{6}$, $y = \\frac{1}{6} + 2 = \\frac{13}{6}$.<br>
          Yes! The curve crosses its oblique asymptote at the point $\\left(\\frac{1}{6}, \\frac{13}{6}\\right)$.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Finding Oblique Equation)',
        text: 'Find the equation of the oblique asymptote of $f(x) = \\frac{3x^2 - 4x + 5}{x - 1}$.',
        solution: '<p>Divide $(3x^2 - 4x + 5)$ by $(x - 1)$: [M1]<br>$3x^2 - 4x + 5 = 3x(x - 1) - x + 5 = 3x(x - 1) - 1(x - 1) + 4 = (3x - 1)(x - 1) + 4$.<br>$f(x) = 3x - 1 + \\frac{4}{x - 1}$. [A1]<br>Oblique asymptote: $y = 3x - 1$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Vertical Asymptote Behavior)',
        text: 'For $g(x) = \\frac{x^2 + 1}{x - 3}$, evaluate $\\lim_{x \\to 3^+} g(x)$ and $\\lim_{x \\to 3^-} g(x)$.',
        solution: '<p>At $x \\to 3$, numerator $\\to 3^2 + 1 = 10 &gt; 0$. [M1]<br>As $x \\to 3^+$, denominator $(x - 3) \\to 0^+$, so $\\lim_{x \\to 3^+} g(x) = +\\infty$. [A1]<br>As $x \\to 3^-$, denominator $(x - 3) \\to 0^-$, so $\\lim_{x \\to 3^-} g(x) = -\\infty$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Identifying Asymptote Types)',
        text: 'State whether each function has a horizontal or oblique asymptote, and write down its equation:<br>(a) $y = \\frac{4x^2 + 1}{2x^2 - 3}$, (b) $y = \\frac{x^3 + 2}{x^2 + 4}$, (c) $y = \\frac{2x - 1}{x^2 + 5}$.',
        solution: '<p><strong>(a)</strong> Degrees equal (2 = 2): Horizontal asymptote $y = \\frac{4}{2} = 2$. [A1]<br><strong>(b)</strong> Degree num = 3, den = 2 ($3 = 2 + 1$): Oblique asymptote $y = x$ (since $x^3 + 2 = x(x^2 + 4) - 4x + 2$). [A1]<br><strong>(c)</strong> Degree num &lt; den (1 &lt; 2): Horizontal asymptote $y = 0$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Slant Asymptote with Negative Leading Term)',
        text: 'Find the oblique asymptote of $h(x) = \\frac{7 - 4x - 2x^2}{x + 3}$.',
        solution: '<p>Rewrite numerator in standard order: $-2x^2 - 4x + 7$. [M1]<br>Divide by $(x + 3)$: $-2x^2 - 4x + 7 = -2x(x + 3) + 2x + 7 = -2x(x + 3) + 2(x + 3) + 1 = (-2x + 2)(x + 3) + 1$. [M1]<br>$h(x) = -2x + 2 + \\frac{1}{x + 3}$.<br>Oblique asymptote is $y = -2x + 2$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Stationary Points & Nature)',
        text: 'Find the stationary points of $f(x) = \\frac{x^2 + 9}{x}$ and determine their nature using the second derivative.',
        solution: '<p>$f(x) = x + 9x^{-1}$. [M1]<br>$f\'(x) = 1 - 9x^{-2} = 1 - \\frac{9}{x^2}$.<br>$f\'(x) = 0 \\implies x^2 = 9 \\implies x = \\pm 3$. [A1]<br>$f\'\'(x) = 18x^{-3} = \\frac{18}{x^3}$. [M1]<br>• At $x = 3$: $f(3) = 6$, $f\'\'(3) = \\frac{18}{27} &gt; 0 \\implies (3, 6)$ is a local minimum. [A1]<br>• At $x = -3$: $f(-3) = -6$, $f\'\'(-3) = -\\frac{18}{27} &lt; 0 \\implies (-3, -6)$ is a local maximum. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Determining Approach Direction)',
        text: 'Show that the curve $y = \\frac{x^2 - 2x + 5}{x - 1}$ never intersects its oblique asymptote, and determine its position relative to the asymptote for $x &gt; 1$ and $x &lt; 1$.',
        solution: '<p>$\\frac{x^2 - 2x + 5}{x - 1} = \\frac{(x - 1)^2 + 4}{x - 1} = (x - 1) + \\frac{4}{x - 1}$. [M1]<br>Oblique asymptote: $y = x - 1$.<br>Difference $y - (x - 1) = \\frac{4}{x - 1} \\neq 0$ for all real $x$. Hence the curve never crosses its asymptote. [A1]<br>• For $x &gt; 1$: $\\frac{4}{x - 1} &gt; 0 \\implies$ curve lies strictly <strong>above</strong> the asymptote. [A1]<br>• For $x &lt; 1$: $\\frac{4}{x - 1} &lt; 0 \\implies$ curve lies strictly <strong>below</strong> the asymptote. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Parameterized Asymptotes)',
        text: 'The rational curve $y = \\frac{a x^2 + b x - 8}{x - 2}$ has an oblique asymptote $y = 3x + 10$. Find the values of constants $a$ and $b$.',
        solution: '<p>Perform division of $(a x^2 + b x - 8)$ by $(x - 2)$: [M1]<br>$a x^2 + b x - 8 = (3x + 10)(x - 2) + R$. [M1]<br>Expand: $(3x + 10)(x - 2) = 3x^2 - 6x + 10x - 20 = 3x^2 + 4x - 20$.<br>Comparing coefficients of $x^2$ and $x$:<br>$a = 3$. [A1]<br>$b = 4$. [A1]<br>(Remainder $R = -8 - (-20) = 12$).</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: No Real Stationary Points)',
        text: 'Show that the curve $f(x) = \\frac{x^2 + 2x - 1}{x + 1}$ has no local extrema, and explain this geometrically.',
        solution: '<p>$f(x) = \\frac{(x+1)^2 - 2}{x + 1} = (x + 1) - \\frac{2}{x + 1} = x + 1 - 2(x + 1)^{-1}$. [M1]<br>$f\'(x) = 1 + 2(x + 1)^{-2} = 1 + \\frac{2}{(x + 1)^2}$. [M1]<br>Since $(x + 1)^2 &gt; 0$ for all $x \\neq -1$, $\\frac{2}{(x + 1)^2} &gt; 0$, which means $f\'(x) \\ge 1 &gt; 0$ everywhere on its domain. [R1]<br>Because the derivative is strictly positive, $f(x)$ is strictly increasing on $(-\\infty, -1)$ and on $(-1, \\infty)$, so it has <strong>no stationary points / local extrema</strong>. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Quadratic Denominator Oblique Asymptote)',
        text: 'Find the oblique asymptote and the point where the curve intersects it for $y = \\frac{2x^3 - x^2 + 4x - 5}{x^2 + 2}$.',
        solution: '<p>Divide numerator by $(x^2 + 2)$: [M1]<br>$2x^3 - x^2 + 4x - 5 = 2x(x^2 + 2) - (x^2 + 2) - 3 = (2x - 1)(x^2 + 2) - 3$. [M1]<br>$y = 2x - 1 - \\frac{3}{x^2 + 2}$.<br>Oblique asymptote is $y = 2x - 1$. [A1]<br>Intersection with asymptote requires remainder term $= 0$:<br>$-\\frac{3}{x^2 + 2} = 0$, which has no real solutions (since numerator is $-3 \\neq 0$).<br>Hence the curve never intersects its oblique asymptote. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Full Sketching Analysis)',
        text: 'For $f(x) = \\frac{x^2 - 4}{x - 1}$:<br>(a) Find intercepts and all asymptotes.<br>(b) Find stationary points.<br>(c) State the range of $f(x)$.',
        solution: '<p><strong>(a) Intercepts &amp; Asymptotes:</strong> [M1]<br>• $y$-intercept: $f(0) = 4$. $x$-intercepts: $x = \\pm 2$.<br>• Vertical asymptote: $x = 1$.<br>• $f(x) = \\frac{(x - 1)(x + 1) - 3}{x - 1} = x + 1 - \\frac{3}{x - 1}$. Oblique asymptote: $y = x + 1$. [A1]</p><p><strong>(b) Stationary points:</strong><br>$f\'(x) = 1 + \\frac{3}{(x - 1)^2}$. Since $3/(x-1)^2 &gt; 0$, $f\'(x) &gt; 0$ everywhere. No stationary points! [A1]</p><p><strong>(c) Range:</strong><br>As $x \\to 1^+$, $f(x) \\to -\\infty$; as $x \\to +\\infty$, $f(x) \\to +\\infty$. Continuous on $(1, \\infty) \\implies$ takes all real values. Same on $(-\\infty, 1)$.<br>Range is $\\mathbb{R}$ (all real numbers). [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 2)</h2>
        <div class="formula-card">
          <h4>Syllabus 2.12: Rational Functions</h4>
          <p>The IB Formula Booklet does not provide the oblique asymptote formula. The syllabus requires students to apply polynomial division and limit arguments:</p>
          $$f(x) = mx + c + \\frac{R(x)}{Q(x)} \\implies y = mx + c \\text{ is the oblique asymptote if } \\lim_{x \\to \\pm\\infty} \\frac{R(x)}{Q(x)} = 0$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Condition for Oblique Asymptotes</h4>
          $$\\deg(\\text{Numerator}) = \\deg(\\text{Denominator}) + 1$$
        </div>

        <div class="formula-card">
          <h4>2. Relative Position to Asymptote</h4>
          <ul>
            <li>$\\frac{R(x)}{Q(x)} &gt; 0 \\implies$ curve lies above the asymptote.</li>
            <li>$\\frac{R(x)}{Q(x)} &lt; 0 \\implies$ curve lies below the asymptote.</li>
            <li>$\\frac{R(x)}{Q(x)} = 0 \\implies$ point where curve crosses the asymptote.</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Horizontal vs Oblique Confusion</h4>
          <p>A rational function CANNOT have both a horizontal asymptote and an oblique asymptote. If the degree of the numerator exceeds the denominator by 1, there is no horizontal asymptote.</p>
        </div>
        <div class="pitfall-card">
          <h4>"Curves Cannot Cross Asymptotes" Myth</h4>
          <p>Curves can <strong>never cross a vertical asymptote</strong> (where the function is undefined), but curves CAN and frequently do cross horizontal and oblique asymptotes at finite values of $x$.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'Which of the following functions possesses an oblique asymptote?',
        options: [
          '$f(x) = \\frac{2x^2 + 1}{x^2 - 4}$',
          '$f(x) = \\frac{x^3 - 2}{x + 1}$',
          '$f(x) = \\frac{x^2 - 3x + 2}{x - 4}$',
          '$f(x) = \\frac{5x - 1}{x^2 + 2}$'
        ],
        correct: 2,
        explanation: 'An oblique asymptote requires degree of numerator to be exactly 1 greater than denominator. For $\\frac{x^2 - 3x + 2}{x - 4}$, degree is $2 - 1 = 1$.'
      },
      {
        id: 'q2',
        prompt: 'The oblique asymptote of $y = \\frac{4x^2 - 1}{2x + 3}$ is:',
        options: [
          '$y = 2x - 3$',
          '$y = 2x + 3$',
          '$y = 2x$',
          '$y = 4x - 6$'
        ],
        correct: 0,
        explanation: 'Divide $4x^2 - 1$ by $2x + 3$: $4x^2 - 1 = 2x(2x + 3) - 6x - 1 = 2x(2x + 3) - 3(2x + 3) + 8 = (2x - 3)(2x + 3) + 8$. So $y = 2x - 3 + \\frac{8}{2x+3}$. Oblique asymptote is $y = 2x - 3$.'
      },
      {
        id: 'q3',
        prompt: 'Which statement about the curve $y = \\frac{x^3 + 2x^2 + x - 4}{x^2 + 1}$ and its oblique asymptote is correct?',
        options: [
          '$(4, 6)$',
          '$(2, 4)$',
          '$(0, -4)$',
          'It never crosses'
        ],
        correct: 3,
        explanation: 'Polynomial division gives $y = x + 2 - \\frac{6}{x^2 + 1}$. Since $-6/(x^2 + 1)$ is never zero for real $x$, the curve never meets its oblique asymptote $y = x + 2$ (option D).'
      },
      {
        id: 'q4',
        prompt: 'As $x \\to +\\infty$, the curve $y = 3x - 1 - \\frac{5}{x + 2}$ approaches its oblique asymptote from:',
        options: [
          'Above',
          'Below',
          'It oscillates across the line',
          'It does not approach'
        ],
        correct: 1,
        explanation: 'As $x \\to +\\infty$, $-\\frac{5}{x + 2} < 0$. Therefore $y < 3x - 1$, approaching the line $y = 3x - 1$ from below.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the rational function $f(x) = \\frac{x^2 - 5x + 6}{x - 1}$.<br><strong>(a)</strong> Write $f(x)$ in the form $ax + b + \\frac{c}{x - 1}$ where $a, b, c \\in \\mathbb{Z}$. [2 marks]<br><strong>(b)</strong> State the equations of both asymptotes of $y = f(x)$. [2 marks]<br><strong>(c)</strong> Show that the graph of $f(x)$ has no points of inflection. [2 marks]',
        solution: `
          <p><strong>(a) Form $ax + b + \\frac{c}{x - 1}$: [2 marks]</strong><br>
          $x^2 - 5x + 6 = x(x - 1) - 4x + 6 = x(x - 1) - 4(x - 1) + 2 = (x - 4)(x - 1) + 2$ [M1].<br>
          $f(x) = x - 4 + \\frac{2}{x - 1}$ ($a = 1, b = -4, c = 2$) [A1].</p>
          <p><strong>(b) Asymptotes: [2 marks]</strong><br>
          Vertical asymptote: $x = 1$ [A1].<br>
          Oblique asymptote: $y = x - 4$ [A1].</p>
          <p><strong>(c) Points of inflection: [2 marks]</strong><br>
          $f\'(x) = 1 - 2(x - 1)^{-2}$ [M1].<br>
          $f\'\'(x) = 4(x - 1)^{-3} = \\frac{4}{(x - 1)^3}$ [A1].<br>
          For a point of inflection, $f\'\'(x) = 0$. But $\\frac{4}{(x - 1)^3} \\neq 0$ for all $x \\neq 1$. Hence there are no points of inflection [R1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'A curve has equation $y = \\frac{2x^2 + kx + 8}{x - 2}$ where $k$ is a constant.<br><strong>(a)</strong> Express $y$ in terms of $x$ and $k$ by polynomial division. [2 marks]<br><strong>(b)</strong> Given that the curve has stationary points, find the range of possible values for $k$. [4 marks]<br><strong>(c)</strong> If $k = -1$, find the coordinates of the local minimum. [2 marks]',
        solution: `
          <p><strong>(a) Division: [2 marks]</strong><br>
          $2x^2 + kx + 8 = 2x(x - 2) + (k + 4)x + 8 = 2x(x - 2) + (k + 4)(x - 2) + 2(k + 4) + 8 = (2x + k + 4)(x - 2) + (2k + 16)$ [M1].<br>
          $y = 2x + k + 4 + \\frac{2k + 16}{x - 2}$ [A1].</p>
          <p><strong>(b) Existence of stationary points: [4 marks]</strong><br>
          $\\frac{dy}{dx} = 2 - \\frac{2k + 16}{(x - 2)^2}$ [M1].<br>
          Setting $\\frac{dy}{dx} = 0 \\implies 2 = \\frac{2k + 16}{(x - 2)^2} \\implies (x - 2)^2 = \\frac{2k + 16}{2} = k + 8$ [M1].<br>
          For real solutions to exist ($x \\neq 2$), we require $k + 8 &gt; 0$ [R1].<br>
          Hence $k &gt; -8$ [A1].</p>
          <p><strong>(c) For $k = -1$: [2 marks]</strong><br>
          $(x - 2)^2 = -1 + 8 = 7 \\implies x - 2 = \\pm \\sqrt{7} \\implies x = 2 \\pm \\sqrt{7}$ [M1].<br>
          Local minimum occurs at $x = 2 + \\sqrt{7} \\approx 4.65$.<br>
          $y = 2(2 + \\sqrt{7}) + (-1) + 4 + \\frac{2(-1)+16}{\\sqrt{7}} = 4 + 2\\sqrt{7} + 3 + \\frac{14}{\\sqrt{7}} = 7 + 2\\sqrt{7} + 2\\sqrt{7} = 7 + 4\\sqrt{7} \\approx 17.58$ [A1].</p>
        `
      }
    ]
  },

  // Guide 9: Composite Transformations & Reciprocal Graphs
  {
    folder: 'composite-transformations-and-reciprocal-graphs',
    code: '2.13',
    title: 'Composite Transformations & Reciprocal Graphs',
    pageTitle: 'Composite Transformations & Reciprocal Graphs | IB Math AA HL | SJMaths',
    metaDesc: 'Master composite transformations, reciprocal graphs y = 1/f(x), squared graphs y = [f(x)]^2, and odd/even function symmetry for IB DP Mathematics AA HL (Topic 2.13). 10 tiered exercises and mini test.',
    keywords: 'IB Math AA HL reciprocal graphs, y = 1/f(x), y = [f(x)]^2, odd and even functions, graph sketching transformations, invariant points',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Deduce new function curves from known graphs. Master the reciprocal mapping $y = \\frac{1}{f(x)}$, the squared mapping $y = [f(x)]^2$, identify invariant points, and classify algebraic and graphical symmetry of odd and even functions.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/functions/rational-functions-and-oblique-asymptotes/',
      title: 'Rational Functions & Oblique Asymptotes'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/reciprocal-and-inverse-trigonometric-functions/',
      title: 'Reciprocal & Inverse Trigonometric Functions'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-arrows-spin" style="color:var(--c-primary);"></i> Figure 2.3: Mapping $y = f(x)$ to Reciprocal $y = 1/f(x)$</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing graph of f(x) on left and reciprocal graph 1/f(x) on right showing zeros becoming asymptotes">
            <!-- Left: y = f(x) -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="330" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary, #4338ca)">Original Curve: y = f(x)</text>
              <line x1="20" y1="130" x2="310" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="165" y1="35" x2="165" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Cubic-like or inverted parabola with zeros at x = 90 and x = 240, max at (165, 60) -->
              <path d="M 50,210 Q 165,-30 280,210" fill="none" stroke="#6366f1" stroke-width="3" />
              <circle cx="95" cy="130" r="4" fill="#ef4444" />
              <text x="80" y="148" font-size="11" font-weight="bold" fill="#ef4444">x₁ (zero)</text>
              <circle cx="235" cy="130" r="4" fill="#ef4444" />
              <text x="235" y="148" font-size="11" font-weight="bold" fill="#ef4444">x₂ (zero)</text>
              <circle cx="165" cy="50" r="4" fill="#10b981" />
              <text x="175" y="55" font-size="11" font-weight="bold" fill="#10b981">Local Max (y = 2)</text>
              <text x="165" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Zeros at x₁, x₂; Max at x = 0</text>
            </g>

            <!-- Right: y = 1/f(x) -->
            <g transform="translate(400, 20)">
              <rect x="0" y="0" width="330" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#10b981">Reciprocal: y = 1/f(x)</text>
              <line x1="20" y1="130" x2="310" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="165" y1="35" x2="165" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Vertical asymptotes at x = 95 and x = 235 -->
              <line x1="95" y1="35" x2="95" y2="230" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
              <line x1="235" y1="35" x2="235" y2="230" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
              <!-- Middle U-shape with local min at (165, 90) (y = 1/2 = 0.5) -->
              <path d="M 105,40 Q 165,90 225,40" fill="none" stroke="#10b981" stroke-width="2.5" />
              <circle cx="165" cy="90" r="4" fill="#10b981" />
              <text x="175" y="100" font-size="11" font-weight="bold" fill="#10b981">Local Min (y = 0.5)</text>
              <!-- Outer branches negative tending to 0 as |x| -> inf -->
              <path d="M 30,145 Q 60,150 85,225" fill="none" stroke="#10b981" stroke-width="2.5" />
              <path d="M 245,225 Q 270,150 300,145" fill="none" stroke="#10b981" stroke-width="2.5" />
              <text x="165" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Zeros become VAs; Max becomes Min</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. The Reciprocal Transformation: $y = \\frac{1}{f(x)}$</h2>
        <p>Given the graph of $y = f(x)$, sketching $y = \\frac{1}{f(x)}$ follows strict mathematical rules:</p>
        <div class="table-responsive" style="margin: 1.5rem 0;">
          <table class="ib-table" style="width:100%; border-collapse:collapse;">
            <thead>
              <tr style="background:var(--c-surface-card); border-bottom:2px solid var(--c-border);">
                <th style="padding:10px; text-align:left;">Feature on $y = f(x)$</th>
                <th style="padding:10px; text-align:left;">Corresponding Feature on $y = \\frac{1}{f(x)}$</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>$x$-intercepts ($f(x) = 0$)</strong></td>
                <td style="padding:10px;"><strong>Vertical asymptotes</strong> ($x = c$). The signs on each side match the signs of $f(x)$.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Vertical asymptotes</strong> ($f(x) \\to \\pm\\infty$)</td>
                <td style="padding:10px;"><strong>$x$-intercepts</strong> ($y \\to 0$). The curve passes through or touches $(c, 0)$.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Invariant Points</strong> ($f(x) = 1$ or $f(x) = -1$)</td>
                <td style="padding:10px;"><strong>Points of intersection</strong>: $\\frac{1}{1} = 1$ and $\\frac{1}{-1} = -1$. Curves cross at these heights!</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Local maximum</strong> at $(a, b)$ with $b &gt; 0$</td>
                <td style="padding:10px;"><strong>Local minimum</strong> at $\\left(a, \\frac{1}{b}\\right)$.</td>
              </tr>
              <tr>
                <td style="padding:10px;"><strong>Horizontal asymptote</strong> $y = L$ ($L \\neq 0$)</td>
                <td style="padding:10px;"><strong>Horizontal asymptote</strong> $y = \\frac{1}{L}$. (If $L = 0$, $y \\to \\pm\\infty$).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>2. The Squared Transformation: $y = [f(x)]^2$</h2>
        <ul class="theory-list">
          <li><strong>Range:</strong> $y \\ge 0$ everywhere (the entire graph lies on or above the $x$-axis).</li>
          <li><strong>Zeros:</strong> Real zeros of $f(x)$ remain zeros, but they become <strong>tangent to the $x$-axis</strong> (turning points) because the derivative $\\frac{d}{dx}[f(x)]^2 = 2f(x)f\'(x) = 0$ at all zeros.</li>
          <li><strong>Invariant Points:</strong> Where $f(x) = 0$ ($y = 0$) and $f(x) = 1$ ($y = 1$). Any points where $f(x) = -1$ map to $y = (-1)^2 = 1$.</li>
          <li><strong>Turning Points:</strong> If $f(x)$ has a turning point at $(a, b)$, then $[f(x)]^2$ has a turning point at $(a, b^2)$.</li>
        </ul>

        <h2>3. Odd and Even Functions (Syllabus 2.13)</h2>
        <ul class="theory-list">
          <li><strong>Even Functions:</strong> Satisfy $f(-x) = f(x)$ for all $x$ in the domain.
            <br>• Graphically: Reflective symmetry across the $y$-axis (e.g., $\\cos x$, $x^2$, $x^4 + 3$, $|x|$).
            <br>• Derivative property: If $f$ is even, $f\'$ is an <strong>odd function</strong>.
          </li>
          <li><strong>Odd Functions:</strong> Satisfy $f(-x) = -f(x)$ for all $x$ in the domain.
            <br>• Graphically: Rotational symmetry of order 2 (180° rotation) about the origin $(0, 0)$ (e.g., $\\sin x$, $x^3$, $\\tan x$, $\\frac{1}{x}$).
            <br>• Origin property: If $0$ is in the domain, $f(0) = -f(0) \\implies f(0) = 0$.
            <br>• Derivative property: If $f$ is odd, $f\'$ is an <strong>even function</strong>.
          </li>
        </ul>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Sketching Reciprocal of a Quadratic</h4>
          <p>The graph of $f(x) = (x - 1)(x - 5) = x^2 - 6x + 5$ has vertex at $(3, -4)$. Sketch $g(x) = \\frac{1}{f(x)}$, stating all asymptotes and the local maximum.</p>
          <p><strong>Solution:</strong></p>
          <p>• Zeros of $f(x)$ are $x = 1$ and $x = 5$. Therefore, $g(x)$ has <strong>vertical asymptotes</strong> at $x = 1$ and $x = 5$.<br>
          • As $|x| \\to \\infty$, $f(x) \\to +\\infty$, so $g(x) \\to 0^+$ (horizontal asymptote $y = 0$).<br>
          • The local minimum of $f(x)$ is at $(3, -4)$. The reciprocal transformation maps this to a <strong>local maximum</strong> at $\\left(3, -\\frac{1}{4}\\right)$.<br>
          • Invariant points: $f(x) = 1 \\implies x^2 - 6x + 4 = 0 \\implies x = 3 \\pm \\sqrt{5}$. At these points, $g(x) = 1$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Classifying Odd, Even, or Neither</h4>
          <p>Determine algebraically whether each function is odd, even, or neither:<br>
          <strong>(a)</strong> $f(x) = \\frac{x^3}{x^2 + 1}$<br>
          <strong>(b)</strong> $g(x) = x \\sin x + x^2$<br>
          <strong>(c)</strong> $h(x) = e^x - e^{-x}$</p>
          <p><strong>Solution:</strong></p>
          <p><strong>(a)</strong> $f(-x) = \\frac{(-x)^3}{(-x)^2 + 1} = \\frac{-x^3}{x^2 + 1} = -f(x)$.<br>
          Since $f(-x) = -f(x)$, $f(x)$ is an <strong>odd function</strong>.</p>
          <p><strong>(b)</strong> $g(-x) = (-x)\\sin(-x) + (-x)^2 = (-x)(-\\sin x) + x^2 = x\\sin x + x^2 = g(x)$.<br>
          Since $g(-x) = g(x)$, $g(x)$ is an <strong>even function</strong>.</p>
          <p><strong>(c)</strong> $h(-x) = e^{-x} - e^{-(-x)} = e^{-x} - e^x = -(e^x - e^{-x}) = -h(x)$.<br>
          Since $h(-x) = -h(x)$, $h(x)$ is an <strong>odd function</strong>.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Expressing Any Function as Sum of Odd and Even Parts</h4>
          <p>Show that any function $f(x)$ can be uniquely expressed as the sum of an even function $f_{\\text{even}}(x)$ and an odd function $f_{\\text{odd}}(x)$.</p>
          <p><strong>Solution:</strong></p>
          <p>Define:</p>
          $$f_{\\text{even}}(x) = \\frac{f(x) + f(-x)}{2}, \\quad f_{\\text{odd}}(x) = \\frac{f(x) - f(-x)}{2}$$
          <p>Check sum: $f_{\\text{even}}(x) + f_{\\text{odd}}(x) = \\frac{f(x) + f(-x) + f(x) - f(-x)}{2} = \\frac{2f(x)}{2} = f(x)$.<br>
          Check even property:<br>
          $f_{\\text{even}}(-x) = \\frac{f(-x) + f(-(-x))}{2} = \\frac{f(-x) + f(x)}{2} = f_{\\text{even}}(x)$ (Even!).<br>
          Check odd property:<br>
          $f_{\\text{odd}}(-x) = \\frac{f(-x) - f(-(-x))}{2} = \\frac{f(-x) - f(x)}{2} = -\\frac{f(x) - f(-x)}{2} = -f_{\\text{odd}}(x)$ (Odd!).<br>
          Hence any function can be uniquely decomposed into an even and odd part.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Reciprocal of Linear Graph)',
        text: 'The linear function $f(x) = 2x - 6$ has $x$-intercept 3 and $y$-intercept -6. State all asymptotes and the $y$-intercept of $g(x) = \\frac{1}{f(x)}$.',
        solution: '<p>Zero of $f$ is $x = 3 \\implies$ Vertical asymptote is $x = 3$. [A1]<br>As $|x| \\to \\infty$, $f(x) \\to \\pm\\infty \\implies$ Horizontal asymptote is $y = 0$. [A1]<br>$y$-intercept: $g(0) = \\frac{1}{f(0)} = \\frac{1}{-6} = -\\frac{1}{6}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Algebraic Odd/Even Test)',
        text: 'Determine whether $f(x) = x^4 - 3x^2 + 7$ is odd, even, or neither.',
        solution: '<p>$f(-x) = (-x)^4 - 3(-x)^2 + 7 = x^4 - 3x^2 + 7 = f(x)$. [M1]<br>Since $f(-x) = f(x)$, $f$ is an <strong>even function</strong>. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Invariant Points on Squared Graph)',
        text: 'A curve $y = f(x)$ passes through $(-2, 0)$, $(1, 1)$, $(3, -1)$, and $(5, 2)$. State the coordinates of the corresponding points on $y = [f(x)]^2$.',
        solution: '<p>• $(-2, 0) \\to (-2, 0^2) = (-2, 0)$. [A1]<br>• $(1, 1) \\to (1, 1^2) = (1, 1)$. [A1]<br>• $(3, -1) \\to (3, (-1)^2) = (3, 1)$. [A1]<br>• $(5, 2) \\to (5, 2^2) = (5, 4)$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Reciprocal Transformation with Stationary Point)',
        text: 'The graph of $f(x)$ has a local minimum at $(4, -2)$. State the coordinates and nature of the corresponding stationary point on $y = \\frac{1}{f(x)}$.',
        solution: '<p>The reciprocal transformation inverts the $y$-coordinate: $y = \\frac{1}{-2} = -0.5$. [M1]<br>The nature flips: a local minimum with negative $y$ becomes a <strong>local maximum</strong> at $(4, -0.5)$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Even/Odd Product Properties)',
        text: 'Let $f(x)$ be an odd function and $g(x)$ be an even function. Prove that the product $h(x) = f(x)g(x)$ is an odd function.',
        solution: '<p>$h(-x) = f(-x)g(-x)$. [M1]<br>Since $f$ is odd, $f(-x) = -f(x)$. Since $g$ is even, $g(-x) = g(x)$.<br>$h(-x) = (-f(x))g(x) = -(f(x)g(x)) = -h(x)$. [M1]<br>Therefore $h(x)$ is an <strong>odd function</strong>. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Squared Graph Stationary Behavior)',
        text: 'Let $g(x) = [f(x)]^2$. Use the chain rule to show that $g\'(x) = 0$ whenever $f(x) = 0$, and interpret this graphically.',
        solution: '<p>By the chain rule: $g\'(x) = 2f(x)f\'(x)$. [M1]<br>When $f(x) = 0$, $g\'(x) = 2(0)f\'(x) = 0$. [A1]<br>Geometrically, this means that every $x$-intercept of $f(x)$ becomes a stationary turning point on $y = [f(x)]^2$ (the curve touches and is tangent to the $x$-axis without crossing below it). [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Reciprocal of Trigonometric Graph)',
        text: 'Given $f(x) = 2\\sin x + 1$ for $0 \\le x \\le 2\\pi$, find the equations of all vertical asymptotes of $y = \\frac{1}{f(x)}$.',
        solution: '<p>Vertical asymptotes occur where $f(x) = 0$: [M1]<br>$2\\sin x + 1 = 0 \\implies \\sin x = -\\frac{1}{2}$. [M1]<br>In $[0, 2\\pi]$, reference angle is $\\frac{\\pi}{6}$. Quadrants 3 and 4:<br>$x = \\pi + \\frac{\\pi}{6} = \\frac{7\\pi}{6}$ and $x = 2\\pi - \\frac{\\pi}{6} = \\frac{11\\pi}{6}$. [A1]<br>Vertical asymptotes are $x = \\frac{7\\pi}{6}$ and $x = \\frac{11\\pi}{6}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Composite Odd/Even Functions)',
        text: 'Let $f(x)$ and $g(x)$ be functions. Prove that:<br>(a) If $g(x)$ is even, then $(f \\circ g)(x)$ is always even, regardless of $f$.<br>(b) If both $f$ and $g$ are odd, then $(f \\circ g)(x)$ is odd.',
        solution: '<p><strong>(a) Even inner function:</strong> [M1]<br>$(f \\circ g)(-x) = f(g(-x))$. Since $g$ is even, $g(-x) = g(x)$.<br>$= f(g(x)) = (f \\circ g)(x)$. Thus $(f \\circ g)$ is even. [A1]</p><p><strong>(b) Both odd:</strong> [M1]<br>$(f \\circ g)(-x) = f(g(-x))$. Since $g$ is odd, $g(-x) = -g(x)$.<br>$= f(-g(x))$. Since $f$ is odd, $f(-u) = -f(u)$.<br>$= -f(g(x)) = -(f \\circ g)(x)$. Thus $(f \\circ g)$ is odd. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Reciprocal Graph with Oblique Asymptote)',
        text: 'The function $f(x) = \\frac{x^2 - 1}{x + 2}$ has an oblique asymptote. Describe the behavior of $g(x) = \\frac{1}{f(x)}$ as $x \\to \\pm\\infty$, and state its horizontal asymptote.',
        solution: '<p>$g(x) = \\frac{1}{f(x)} = \\frac{x + 2}{x^2 - 1}$. [M1]<br>In $g(x)$, degree of numerator is 1, degree of denominator is 2. [M1]<br>As $x \\to \\pm\\infty$, $\\lim_{x \\to \\pm\\infty} \\frac{x + 2}{x^2 - 1} = \\lim_{x \\to \\pm\\infty} \\frac{1/x + 2/x^2}{1 - 1/x^2} = \\frac{0}{1} = 0$. [A1]<br>Therefore, the oblique asymptote of $f(x)$ maps to the horizontal asymptote $y = 0$ on the reciprocal curve $g(x)$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Integral of Even and Odd Functions)',
        text: 'Use symmetry properties to evaluate:<br>(a) $\\int_{-\\pi/4}^{\\pi/4} x^5 \\cos(x^2)\\,dx$<br>(b) $\\int_{-2}^2 (3x^2 + 5x^3)\\,dx$',
        solution: '<p><strong>(a) Odd integrand:</strong> [M1]<br>Let $k(x) = x^5 \\cos(x^2)$.<br>$k(-x) = (-x)^5 \\cos((-x)^2) = -x^5 \\cos(x^2) = -k(x)$ (Odd!).<br>The integral of any continuous odd function over symmetric bounds $[-a, a]$ is strictly zero.<br>$\\int_{-\\pi/4}^{\\pi/4} x^5 \\cos(x^2)\\,dx = 0$. [A1]</p><p><strong>(b) Splitting into even and odd parts:</strong> [M1]<br>$\\int_{-2}^2 (3x^2 + 5x^3)\\,dx = 3\\int_{-2}^2 x^2\\,dx + 5\\int_{-2}^2 x^3\\,dx$.<br>$5x^3$ is odd, so $\\int_{-2}^2 5x^3\\,dx = 0$. [A1]<br>$3x^2$ is even, so $3\\int_{-2}^2 x^2\\,dx = 2 \\times 3\\int_0^2 x^2\\,dx = 6\\left[\\frac{x^3}{3}\\right]_0^2 = 2(8) = 16$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 2)</h2>
        <div class="formula-card">
          <h4>Syllabus 2.13: Function Transformations &amp; Symmetry</h4>
          <p>The Formula Booklet includes basic translation and stretch notation, but does not provide reciprocal, squared, or odd/even algebraic formulas.</p>
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Reciprocal Mapping $y = \\frac{1}{f(x)}$</h4>
          <ul>
            <li>$f(x) = 0 \\implies$ Vertical asymptote.</li>
            <li>Vertical asymptote of $f(x) \\implies x$-intercept of $\\frac{1}{f(x)}$.</li>
            <li>$f(x) = \\pm 1 \\implies$ Invariant points.</li>
            <li>Local maximum $(a, b) \\implies$ Local minimum $\\left(a, \\frac{1}{b}\\right)$.</li>
          </ul>
        </div>
        <div class="formula-card">
          <h4>2. Odd and Even Algebraic Tests</h4>
          <ul>
            <li><strong>Even:</strong> $f(-x) = f(x) \\implies$ Symmetric about the $y$-axis.</li>
            <li><strong>Odd:</strong> $f(-x) = -f(x) \\implies$ Rotational symmetry 180° about the origin.</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Sign Consistency in Reciprocals</h4>
          <p>The reciprocal of a positive number is ALWAYS positive, and the reciprocal of a negative number is ALWAYS negative. The graph of $y = \\frac{1}{f(x)}$ must have identical signs to $f(x)$ in every interval!</p>
        </div>
        <div class="pitfall-card">
          <h4>Odd Function Value at Origin</h4>
          <p>If an odd function is defined at $x = 0$, its value MUST be 0 ($f(0) = 0$). If $f(0) \\neq 0$, the function cannot be odd!</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If $f(x)$ has a local minimum at $(2, 4)$, then $y = \\frac{1}{f(x)}$ has:',
        options: [
          'A local maximum at $(2, 0.25)$',
          'A local minimum at $(2, 0.25)$',
          'A vertical asymptote at $x = 2$',
          'A local maximum at $(-2, -4)$'
        ],
        correct: 0,
        explanation: 'The reciprocal of a local minimum at height 4 becomes a local maximum at height $1/4 = 0.25$.'
      },
      {
        id: 'q2',
        prompt: 'Which of the following functions is neither odd nor even?',
        options: [
          '$f(x) = x^3 - \\sin x$',
          '$g(x) = x^2 + \\cos x$',
          '$h(x) = e^x$',
          '$k(x) = |x| + 5$'
        ],
        correct: 2,
        explanation: '$h(-x) = e^{-x} \\neq e^x$ (not even) and $e^{-x} \\neq -e^x$ (not odd). Thus $e^x$ is neither.'
      },
      {
        id: 'q3',
        prompt: 'If $f(x)$ has $x$-intercepts at $x = -1$ and $x = 3$, how many $x$-intercepts does $y = [f(x)]^2$ have?',
        options: [
          '0',
          '1',
          '2',
          '4'
        ],
        correct: 2,
        explanation: '$[f(x)]^2 = 0 \\iff f(x) = 0$. The $x$-intercepts remain exactly at $x = -1$ and $x = 3$, though the curve touches without crossing.'
      },
      {
        id: 'q4',
        prompt: 'If $f$ is an even function and $g$ is an odd function, what is the nature of $f(g(x))$?',
        options: [
          'Odd',
          'Even',
          'Neither',
          'Cannot be determined'
        ],
        correct: 1,
        explanation: '$f(g(-x)) = f(-g(x)) = f(g(x))$ because $f$ is even. Hence the composite function is even.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'The function $f$ is defined by $f(x) = x\\sqrt{4 - x^2}$ for $-2 \\le x \\le 2$.<br><strong>(a)</strong> Show that $f$ is an odd function. [2 marks]<br><strong>(b)</strong> Find the stationary points of $f(x)$. [3 marks]<br><strong>(c)</strong> Hence sketch the graph of $f(x)$ showing all key features. [1 mark]',
        solution: `
          <p><strong>(a) Odd function proof: [2 marks]</strong><br>
          $f(-x) = (-x)\\sqrt{4 - (-x)^2} = -x\\sqrt{4 - x^2} = -f(x)$ [M1].<br>
          Since $f(-x) = -f(x)$ for all $x \\in [-2, 2]$, $f$ is an odd function [A1].</p>
          <p><strong>(b) Stationary points: [3 marks]</strong><br>
          $f\'(x) = 1\\sqrt{4 - x^2} + x\\left(\\frac{-2x}{2\\sqrt{4 - x^2}}\\right) = \\sqrt{4 - x^2} - \\frac{x^2}{\\sqrt{4 - x^2}} = \\frac{4 - 2x^2}{\\sqrt{4 - x^2}}$ [M1].<br>
          $f\'(x) = 0 \\implies 4 - 2x^2 = 0 \\implies x^2 = 2 \\implies x = \\pm\\sqrt{2}$ [A1].<br>
          • At $x = \\sqrt{2}$: $y = \\sqrt{2}\\sqrt{4 - 2} = \\sqrt{2}\\sqrt{2} = 2$. Local maximum at $(\\sqrt{2}, 2)$.<br>
          • At $x = -\\sqrt{2}$: by odd symmetry, local minimum at $(-\\sqrt{2}, -2)$ [A1].</p>
          <p><strong>(c) Sketch: [1 mark]</strong><br>
          Passes through $(-2, 0), (0, 0), (2, 0)$ with rotational symmetry order 2 about origin [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'Let $f(x) = \\frac{1}{x^2 - 4}$.<br><strong>(a)</strong> State the equations of all asymptotes of $y = f(x)$. [2 marks]<br><strong>(b)</strong> Sketch $y = f(x)$ and on the same axes sketch $y = [f(x)]^2$. [3 marks]<br><strong>(c)</strong> Find the coordinates of the invariant points where $f(x) = [f(x)]^2$. [3 marks]',
        solution: `
          <p><strong>(a) Asymptotes: [2 marks]</strong><br>
          Vertical asymptotes: $x^2 - 4 = 0 \\implies x = 2$ and $x = -2$ [A1].<br>
          Horizontal asymptote: $\\lim_{x \\to \\pm\\infty} \\frac{1}{x^2 - 4} = 0 \\implies y = 0$ [A1].</p>
          <p><strong>(b) Sketch comparison: [3 marks]</strong><br>
          • $f(x)$ is negative for $-2 &lt; x &lt; 2$ with local max at $(0, -0.25)$ [A1].<br>
          • $[f(x)]^2 = \\frac{1}{(x^2 - 4)^2}$ is positive everywhere, with local min at $(0, 0.0625)$ and asymptotes at $x = \\pm 2, y = 0$ [A1][A1].</p>
          <p><strong>(c) Invariant points: [3 marks]</strong><br>
          $f(x) = [f(x)]^2 \\iff f(x)[1 - f(x)] = 0$ [M1].<br>
          Since $f(x) = \\frac{1}{x^2 - 4} \\neq 0$, we must have $f(x) = 1$ [M1].<br>
          $\\frac{1}{x^2 - 4} = 1 \\implies x^2 - 4 = 1 \\implies x^2 = 5 \\implies x = \\pm\\sqrt{5}$ [A1].<br>
          Invariant points: $(\\sqrt{5}, 1)$ and $(-\\sqrt{5}, 1)$.</p>
        `
      }
    ]
  }
];

function generateHtml(guide) {
  const mcqsJson = JSON.stringify(guide.mcqs.map(q => ({
    id: q.id,
    correct: q.correct,
    explanation: q.explanation
  }))).replace(/</g, '\\u003c');

  const mcqsMarkup = guide.mcqs.map((q, idx) => {
    const opts = q.options.map((opt, optIdx) => `
              <label class="quiz-option" data-option="${optIdx}">
                <input type="radio" name="${q.id}" value="${optIdx}">
                <span class="opt-letter">${String.fromCharCode(65 + optIdx)}</span>
                <span class="opt-text">${opt}</span>
              </label>
    `).join('\n');

    return `
          <div class="quiz-card" id="${q.id}">
            <div class="quiz-card-header">
              <span class="quiz-badge">Question ${idx + 1} of 4</span>
            </div>
            <p class="quiz-question">${q.prompt}</p>
            <div class="quiz-options">
              ${opts}
            </div>
            <div class="quiz-feedback" style="display:none;"></div>
          </div>
    `;
  }).join('\n');

  const exercisesMarkup = guide.exercises.map((ex, idx) => `
          <div class="exercise-card">
            <span class="exercise-badge ${ex.tier}">${ex.title}</span>
            <p class="question-text">${ex.text}</p>
            <details class="solution-details">
              <summary>Show Full Solution</summary>
              <div class="solution-content">
                ${ex.solution}
              </div>
            </details>
          </div>
  `).join('\n');

  const frqsMarkup = guide.frqs.map((frq, idx) => `
          <div class="exercise-card">
            <span class="exercise-badge ${idx === 0 ? 'tier-2' : 'tier-3'}">${frq.badge}</span>
            <p class="question-text">${frq.text}</p>
            <details class="solution-details">
              <summary>Show Full Markscheme</summary>
              <div class="solution-content">
                ${frq.solution}
              </div>
            </details>
          </div>
  `).join('\n');

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${guide.pageTitle}</title>
  <meta name="description" content="${guide.metaDesc}">
  <meta name="keywords" content="${guide.keywords}">
  <meta name="author" content="SJMaths - Sandeep Jaiswal (PGT Maths)">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/${guide.folder}/">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${guide.pageTitle}">
  <meta property="og:description" content="${guide.metaDesc}">
  <meta property="og:url" content="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/${guide.folder}/">
  <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <meta property="og:site_name" content="SJMaths">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${guide.pageTitle}">
  <meta name="twitter:description" content="${guide.metaDesc}">
  <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
  <link rel="icon" type="image/png" href="/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"></noscript>
  <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473">
  <link rel="stylesheet" href="/assets/css/main.min.css?v=e4c665a0">
  <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
  <link rel="stylesheet" href="/assets/css/component.min.css?v=85dbb37c">
  <link rel="stylesheet" href="/assets/css/ib-page.min.css?v=33705aff">
  <link rel="stylesheet" href="/assets/css/ib-dp-aa-sl-guides.css?v=d12c2f9e">

  <!-- KaTeX for Mathematical Typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous" onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false},{left:'\\\\(',right:'\\\\)',display:false},{left:'\\\\[',right:'\\\\]',display:true}],throwOnError:false})"></script>

  <script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/${guide.folder}/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"IB Mathematics","item":"https://sjmaths.com/ib/"},{"@type":"ListItem","position":3,"name":"IB DP Mathematics","item":"https://sjmaths.com/ib/dp-mathematics/"},{"@type":"ListItem","position":4,"name":"AA HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/"},{"@type":"ListItem","position":5,"name":"Functions HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/"},{"@type":"ListItem","position":6,"name":"${guide.title}","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/${guide.folder}/"}]},{"@type":"Article","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/${guide.folder}/#article","headline":"${guide.title} | IB Math AA HL Guide","description":"${guide.metaDesc}","url":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/${guide.folder}/","dateModified":"2026-10-11","inLanguage":"en","articleSection":"IB DP Mathematics AA HL · Topic ${guide.code}","author":{"@type":"Person","name":"Sandeep Jaiswal","url":"https://sjmaths.com/pages/about.html"},"publisher":{"@type":"Organization","name":"SJMaths","url":"https://sjmaths.com/","logo":{"@type":"ImageObject","url":"https://sjmaths.com/assets/icons/icon-512x512.png"}}}]}</script>
</head>
<body>
<a class="skip-link study-skip" href="#main-content">Skip to main content</a>
<header class="ib-nav-header">
  <div class="ib-nav-container">
    <a href="/" class="ib-nav-brand"><span aria-hidden="true">∫</span> SJMaths</a>
    <nav class="ib-nav-links" aria-label="Main navigation">
      <a href="/ib/">IB Hub</a>
      <a href="/ib/dp-mathematics/">DP Portal</a>
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/">AA HL Hub</a>
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/functions/">Topic 2 HL</a>
      <button id="theme-toggle" class="ib-theme-btn" type="button" aria-label="Toggle Dark Mode"><i class="fa-solid fa-moon" aria-hidden="true"></i></button>
    </nav>
  </div>
</header>

<section class="ib-hero">
  <div class="ib-hero-container">
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
      <a href="https://sjmaths.com/">Home</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
      <a href="https://sjmaths.com/ib/">IB Mathematics</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
      <a href="https://sjmaths.com/ib/dp-mathematics/">IB DP Mathematics</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
      <a href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/">AA HL</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
      <a href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/functions/">Functions</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
      <span aria-current="page">${guide.title}</span>
    </nav>
    <p class="guide-kicker">${guide.kicker}</p>
    <h1 class="ib-hero-title">${guide.title}</h1>
    <p class="ib-hero-desc">${guide.heroDesc}</p>
    <div class="meta-pills">
      <span class="meta-pill"><i class="fa-solid fa-layer-group" aria-hidden="true"></i> Syllabus AHL ${guide.code}</span>
      <span class="meta-pill"><i class="fa-solid fa-certificate" aria-hidden="true"></i> Paper 1 &amp; Paper 2 Skill</span>
      <span class="meta-pill"><i class="fa-solid fa-bolt" aria-hidden="true"></i> 4 Interactive Tabs</span>
      <span class="meta-pill"><i class="fa-solid fa-list-check" aria-hidden="true"></i> 10 Tiered Problems + Mini Test</span>
    </div>
  </div>
</section>

<main id="main-content" class="main-content study-main">
  <div class="study-layout">
    <article class="study-article">
      <!-- 4 Tabs Bar -->
      <nav class="study-tabs-nav" role="tablist" aria-label="Study Guide Tabs">
        <button class="study-tab-btn active" role="tab" aria-selected="true" data-tab="tab-notes" id="tab-btn-notes">
          <i class="fa-solid fa-book-open" aria-hidden="true"></i> 1. Study Notes
        </button>
        <button class="study-tab-btn" role="tab" aria-selected="false" data-tab="tab-practice" id="tab-btn-practice">
          <i class="fa-solid fa-pen-to-square" aria-hidden="true"></i> 2. Practice Exercises (10)
        </button>
        <button class="study-tab-btn" role="tab" aria-selected="false" data-tab="tab-formulas" id="tab-btn-formulas">
          <i class="fa-solid fa-square-root-variable" aria-hidden="true"></i> 3. Formula Sheet
        </button>
        <button class="study-tab-btn" role="tab" aria-selected="false" data-tab="tab-test" id="tab-btn-test">
          <i class="fa-solid fa-stopwatch" aria-hidden="true"></i> 4. Mini Test
        </button>
      </nav>

      <!-- TAB 1: STUDY NOTES -->
      <section class="study-tab-panel active" id="tab-notes" role="tabpanel" aria-labelledby="tab-btn-notes">
        ${guide.svgFigure}
        ${guide.studyNotesHtml}
      </section>

      <!-- TAB 2: PRACTICE EXERCISES -->
      <section class="study-tab-panel" id="tab-practice" role="tabpanel" aria-labelledby="tab-btn-practice">
        <h2>Practice Exercises (10 Tiered Questions)</h2>
        <p>Work through these 10 examination-style exercises progressing from core algorithmic competence to advanced IB distinction problems. Click each toggle to reveal detailed algebraic solutions.</p>
        ${exercisesMarkup}
      </section>

      <!-- TAB 3: FORMULA SHEET -->
      <section class="study-tab-panel" id="tab-formulas" role="tabpanel" aria-labelledby="tab-btn-formulas">
        ${guide.formulasHtml}
      </section>

      <!-- TAB 4: MINI TEST -->
      <section class="study-tab-panel" id="tab-test" role="tabpanel" aria-labelledby="tab-btn-test">
        <h2>Topic Mastery Diagnostic Test</h2>
        <p>Complete this timed diagnostic test to verify your conceptual command and examination technique under exam conditions.</p>

        <!-- Section A: MCQs -->
        <h3>Section A: Diagnostic Multiple Choice Questions</h3>
        <script type="application/json" id="ib-quiz-answer-key">${mcqsJson}</script>
        ${mcqsMarkup}

        <div style="margin: 24px 0; text-align: center;">
          <button type="button" class="btn btn-primary" id="btn-submit-quiz" style="padding: 12px 28px; font-weight: 700; border-radius: 8px;">
            <i class="fa-solid fa-check-double" aria-hidden="true"></i> Calculate Score &amp; Review Solutions
          </button>
          <div id="quiz-score-display" style="display:none; margin-top:16px; font-size:1.15rem; font-weight:bold; color:var(--c-primary);"></div>
        </div>

        <!-- Section B: FRQs -->
        <h3 style="margin-top: 36px;">Section B: Examination-Style Free Response Questions</h3>
        ${frqsMarkup}
      </section>

      <!-- Unit Navigation -->
      <nav class="related-guides" aria-label="Related study guides" style="margin-top: 2rem;">
        <a href="${guide.prevLesson.url}">
          <span>Previous Lesson</span>
          <strong>${guide.prevLesson.title}</strong>
        </a>
        <a href="${guide.nextLesson.url}">
          <span>Next Lesson</span>
          <strong>${guide.nextLesson.title}</strong>
        </a>
      </nav>
    </article>
  </div>
</main>

<footer class="ib-footer">
  <p>© 2026 SJMaths · DP Mathematics AA HL · Sandeep Jaiswal (PGT Maths).</p>
</footer>

<script src="/assets/js/ib-theme.min.js?v=97caae90" defer></script>
<script src="/assets/js/ib-study-tabs.js?v=20261012-tabs-init-once" defer></script>
<script src="/assets/js/mobile-tab-dock.js?v=20261011-mobile-tab-dock" defer></script>
</body>
</html>
`;
}

// Generate files
guides.forEach(g => {
  const dir = path.join(baseDir, g.folder);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  const filePath = path.join(dir, 'index.html');
  const html = generateHtml(g);
  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`Generated: ${g.folder}/index.html (${html.length} chars)`);
});
