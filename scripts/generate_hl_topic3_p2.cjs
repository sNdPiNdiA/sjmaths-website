const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'geometry-and-trigonometry');

const guides = [
  // Guide 11: Compound Angle Identities & Double Angles
  {
    folder: 'compound-angle-identities-and-double-angles',
    code: '3.9',
    title: 'Compound Angle Identities & Double Angles',
    pageTitle: 'Compound Angle Identities & Double Angles | IB Math AA HL | SJMaths',
    metaDesc: 'Master compound angle identities, double angle formulas, and harmonic form R cos(x ± α) for IB DP Mathematics AA HL (Topic 3.9). Exact values, proofs, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL compound angle identities, addition formulas sin cos tan, double angle formulas, harmonic linear combination R cos(x - alpha), exact trigonometric values',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Derive and apply addition and subtraction formulas for sine, cosine, and tangent. Master double angle identities, power-reduction substitutions, and harmonic linear combinations $a\\sin x + b\\cos x = R\\sin(x \\pm \\alpha)$.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/reciprocal-and-inverse-trigonometric-functions/',
      title: 'Reciprocal & Inverse Trigonometric Functions'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/3d-vectors-and-scalar-product/',
      title: '3D Vectors & The Scalar Product'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-wave-square" style="color:var(--c-primary);"></i> Figure 3.2: Harmonic Combination: $a\\sin x + b\\cos x = R\\sin(x + \\alpha)$</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing triangle relation for R and alpha on left and composite wave on right">
            <!-- Left: Right triangle for R and alpha -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="280" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="140" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary, #4338ca)">Triangle Construction</text>
              <line x1="50" y1="200" x2="230" y2="200" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
              <line x1="230" y1="200" x2="230" y2="70" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
              <line x1="50" y1="200" x2="230" y2="70" stroke="#6366f1" stroke-width="3" />
              <!-- Angle arc -->
              <path d="M 90,200 A 40 40 0 0 0 85,175" fill="none" stroke="#ef4444" stroke-width="2" />
              <text x="100" y="190" fill="#ef4444" font-size="14" font-weight="bold">α</text>
              <text x="140" y="220" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-text)">a (adjacent)</text>
              <text x="245" y="140" font-size="13" font-weight="bold" fill="var(--c-text)">b (opp)</text>
              <text x="120" y="125" font-size="14" font-weight="bold" fill="#6366f1">R = √(a² + b²)</text>
              <text x="140" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">tan α = b/a</text>
            </g>

            <!-- Right: Single combined wave -->
            <g transform="translate(350, 20)">
              <rect x="0" y="0" width="380" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="190" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#10b981">Combined Wave: y = R sin(x + α)</text>
              <line x1="30" y1="130" x2="350" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="100" y1="35" x2="100" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Sine wave with phase shift left by alpha -->
              <path d="M 50,130 Q 90,40 140,130 T 230,130 T 320,130" fill="none" stroke="#10b981" stroke-width="3" />
              <!-- Amplitude lines at y = +R and y = -R -->
              <line x1="40" y1="40" x2="340" y2="40" stroke="#ef4444" stroke-width="1" stroke-dasharray="3,3" />
              <line x1="40" y1="220" x2="340" y2="220" stroke="#ef4444" stroke-width="1" stroke-dasharray="3,3" />
              <text x="345" y="45" font-size="11" font-weight="bold" fill="#ef4444">+R (Max)</text>
              <text x="345" y="225" font-size="11" font-weight="bold" fill="#ef4444">-R (Min)</text>
              <text x="190" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Single harmonic wave with amplitude R</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Compound Angle Addition and Subtraction Formulas</h2>
        <p>The addition and subtraction formulas allow expressing trigonometric functions of sums $(A \\pm B)$ in terms of individual angles:</p>
        $$\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A\\sin B$$
        $$\\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A\\sin B$$
        $$\\tan(A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1 \\mp \\tan A\\tan B}$$
        <p>Notice the sign convention: $\\cos(A + B)$ contains a <strong>minus</strong> sign, whereas $\\cos(A - B)$ contains a <strong>plus</strong> sign.</p>

        <h2>2. Double Angle Formulas</h2>
        <p>Setting $A = B = \\theta$ yields the double angle formulas:</p>
        $$\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta$$
        $$\\cos(2\\theta) = \\cos^2\\theta - \\sin^2\\theta = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta$$
        $$\\tan(2\\theta) = \\frac{2\\tan\\theta}{1 - \\tan^2\\theta}$$
        <p>Rearranging the cosine double angle formula gives powerful power-reduction formulas essential for calculus integration:</p>
        $$\\cos^2\\theta = \\frac{1 + \\cos(2\\theta)}{2}, \\quad \\sin^2\\theta = \\frac{1 - \\cos(2\\theta)}{2}$$

        <h2>3. Harmonic Linear Combination: $a\\sin x + b\\cos x$</h2>
        <p>Any linear combination of sine and cosine with identical angular frequencies can be synthesized into a single phase-shifted wave:</p>
        $$a\\sin x + b\\cos x = R\\sin(x + \\alpha) = R(\\sin x\\cos\\alpha + \\cos x\\sin\\alpha)$$
        <p>Equating coefficients: $R\\cos\\alpha = a$ and $R\\sin\\alpha = b$. Squaring and adding gives:</p>
        $$R = \\sqrt{a^2 + b^2}, \\quad \\tan\\alpha = \\frac{b}{a}$$
        <p>Alternatively, in cosine form: $a\\sin x + b\\cos x = R\\cos(x - \\alpha)$ where $R\\cos\\alpha = b$ and $R\\sin\\alpha = a$.</p>
        <p><strong>Maximum and Minimum Values:</strong> The expression $a\\sin x + b\\cos x$ has a maximum value of $+R = +\\sqrt{a^2+b^2}$ and a minimum value of $-R = -\\sqrt{a^2+b^2}$.</p>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Exact Value of $\\cos(75^\\circ)$ and $\\sin(15^\\circ)$</h4>
          <p>Find the exact value of $\\cos(75^\\circ)$ without a calculator.</p>
          <p><strong>Solution:</strong></p>
          <p>Express $75^\\circ$ as the compound sum of special angles: $75^\\circ = 45^\\circ + 30^\\circ$.</p>
          $$\\cos(75^\\circ) = \\cos(45^\\circ + 30^\\circ) = \\cos(45^\\circ)\\cos(30^\\circ) - \\sin(45^\\circ)\\sin(30^\\circ)$$
          $$= \\left(\\frac{\\sqrt{2}}{2}\\right)\\left(\\frac{\\sqrt{3}}{2}\\right) - \\left(\\frac{\\sqrt{2}}{2}\\right)\\left(\\frac{1}{2}\\right) = \\frac{\\sqrt{6} - \\sqrt{2}}{4}$$
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Solving Equation using Harmonic Form</h4>
          <p>Solve $\\sqrt{3}\\sin x + \\cos x = 1$ for $0 \\le x \\le 2\\pi$.</p>
          <p><strong>Solution:</strong></p>
          <p>Express the left-hand side in the form $R\\sin(x + \\alpha)$:</p>
          $$R = \\sqrt{(\\sqrt{3})^2 + 1^2} = \\sqrt{3 + 1} = 2$$
          $$R\\cos\\alpha = \\sqrt{3} \\implies \\cos\\alpha = \\frac{\\sqrt{3}}{2}, \\quad R\\sin\\alpha = 1 \\implies \\sin\\alpha = \\frac{1}{2}$$
          $$\\tan\\alpha = \\frac{1}{\\sqrt{3}} \\implies \\alpha = \\frac{\\pi}{6}$$
          <p>The equation becomes:</p>
          $$2\\sin\\left(x + \\frac{\\pi}{6}\\right) = 1 \\implies \\sin\\left(x + \\frac{\\pi}{6}\\right) = \\frac{1}{2}$$
          <p>For $x \\in [0, 2\\pi]$, $x + \\frac{\\pi}{6} \\in \\left[\\frac{\\pi}{6}, 2\\pi + \\frac{\\pi}{6}\\right] = \\left[\\frac{\\pi}{6}, \\frac{13\\pi}{6}\\right]$:</p>
          $$x + \\frac{\\pi}{6} = \\frac{\\pi}{6}, \\quad x + \\frac{\\pi}{6} = \\frac{5\\pi}{6}, \\quad x + \\frac{\\pi}{6} = \\frac{13\\pi}{6}$$
          <p>• $x + \\frac{\\pi}{6} = \\frac{\\pi}{6} \\implies x = 0$<br>
          • $x + \\frac{\\pi}{6} = \\frac{5\\pi}{6} \\implies x = \\frac{4\\pi}{6} = \\frac{2\\pi}{3}$<br>
          • $x + \\frac{\\pi}{6} = \\frac{13\\pi}{6} \\implies x = 2\\pi$<br>
          Solutions: $x \\in \\left\\{0, \\frac{2\\pi}{3}, 2\\pi\\right\\}$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Triple Angle Identity Proof</h4>
          <p>Prove the identity $\\cos(3\\theta) = 4\\cos^3\\theta - 3\\cos\\theta$.</p>
          <p><strong>Solution:</strong></p>
          <p>Write $3\\theta = 2\\theta + \\theta$ and apply the cosine addition formula:</p>
          $$\\cos(3\\theta) = \\cos(2\\theta + \\theta) = \\cos(2\\theta)\\cos\\theta - \\sin(2\\theta)\\sin\\theta$$
          <p>Substitute double angle formulas $\\cos(2\\theta) = 2\\cos^2\\theta - 1$ and $\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta$:</p>
          $$= (2\\cos^2\\theta - 1)\\cos\\theta - (2\\sin\\theta\\cos\\theta)\\sin\\theta$$
          $$= 2\\cos^3\\theta - \\cos\\theta - 2\\sin^2\\theta\\cos\\theta$$
          <p>Substitute $\\sin^2\\theta = 1 - \\cos^2\\theta$:</p>
          $$= 2\\cos^3\\theta - \\cos\\theta - 2(1 - \\cos^2\\theta)\\cos\\theta = 2\\cos^3\\theta - \\cos\\theta - 2\\cos\\theta + 2\\cos^3\\theta$$
          $$= 4\\cos^3\\theta - 3\\cos\\theta$$
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Double Angle Sine)',
        text: 'Given $\\sin\\theta = \\frac{3}{5}$ and $\\theta$ is an acute angle, find the exact value of $\\sin(2\\theta)$ and $\\cos(2\\theta)$.',
        solution: '<p>Since $\\theta$ is acute, $\\cos\\theta = \\sqrt{1 - 9/25} = \\frac{4}{5}$. [M1]<br>$\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta = 2\\left(\\frac{3}{5}\\right)\\left(\\frac{4}{5}\\right) = \\frac{24}{25}$. [A1]<br>$\\cos(2\\theta) = \\cos^2\\theta - \\sin^2\\theta = \\frac{16}{25} - \\frac{9}{25} = \\frac{7}{25}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Exact Value of Tan 15°)',
        text: 'Use the formula for $\\tan(A - B)$ to find the exact value of $\\tan(15^\\circ)$ in simplest surd form.',
        solution: '<p>$\\tan(15^\\circ) = \\tan(45^\\circ - 30^\\circ) = \\frac{\\tan 45^\\circ - \\tan 30^\\circ}{1 + \\tan 45^\\circ\\tan 30^\\circ} = \\frac{1 - 1/\\sqrt{3}}{1 + 1/\\sqrt{3}} = \\frac{\\sqrt{3} - 1}{\\sqrt{3} + 1}$. [M1]<br>Rationalize denominator: $\\frac{(\\sqrt{3}-1)^2}{3 - 1} = \\frac{3 - 2\\sqrt{3} + 1}{2} = \\frac{4 - 2\\sqrt{3}}{2} = 2 - \\sqrt{3}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Power Reduction in Cosine)',
        text: 'Express $\\cos^4\\theta$ in terms of cosines of multiple angles.',
        solution: '<p>$\\cos^2\\theta = \\frac{1 + \\cos(2\\theta)}{2}$. [M1]<br>$\\cos^4\\theta = \\left(\\frac{1 + \\cos(2\\theta)}{2}\\right)^2 = \\frac{1 + 2\\cos(2\\theta) + \\cos^2(2\\theta)}{4}$. [M1]<br>Since $\\cos^2(2\\theta) = \\frac{1 + \\cos(4\\theta)}{2}$:<br>$\\cos^4\\theta = \\frac{1}{4}\\left(1 + 2\\cos(2\\theta) + \\frac{1 + \\cos(4\\theta)}{2}\\right) = \\frac{3}{8} + \\frac{1}{2}\\cos(2\\theta) + \\frac{1}{8}\\cos(4\\theta)$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: R-Formula Amplitude and Phase)',
        text: 'Express $3\\cos x - 4\\sin x$ in the form $R\\cos(x + \\alpha)$ where $R &gt; 0$ and $0 &lt; \\alpha &lt; \\frac{\\pi}{2}$. State the minimum value of the expression.',
        solution: '<p>$R\\cos(x + \\alpha) = R\\cos x\\cos\\alpha - R\\sin x\\sin\\alpha = 3\\cos x - 4\\sin x$.<br>$R = \\sqrt{3^2 + (-4)^2} = \\sqrt{25} = 5$. [A1]<br>$R\\cos\\alpha = 3 \\implies \\cos\\alpha = 3/5$, $R\\sin\\alpha = 4 \\implies \\sin\\alpha = 4/5$.<br>$\\alpha = \\arctan(4/3) \\approx 0.927$ rad. [A1]<br>Form: $5\\cos(x + 0.927)$. Minimum value is $-R = -5$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Solving Quadratic Equation with Double Angle)',
        text: 'Solve $\\cos(2x) + 3\\sin x = 2$ for $0 \\le x \\le 2\\pi$.',
        solution: '<p>Use $\\cos(2x) = 1 - 2\\sin^2 x$: [M1]<br>$(1 - 2\\sin^2 x) + 3\\sin x = 2 \\implies 2\\sin^2 x - 3\\sin x + 1 = 0$. [M1]<br>$(2\\sin x - 1)(\\sin x - 1) = 0$.<br>• $\\sin x = \\frac{1}{2} \\implies x = \\frac{\\pi}{6}, \\frac{5\\pi}{6}$. [A1]<br>• $\\sin x = 1 \\implies x = \\frac{\\pi}{2}$. [A1]<br>Solutions: $x \\in \\left\\{\\frac{\\pi}{6}, \\frac{\\pi}{2}, \\frac{5\\pi}{6}\\right\\}$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Proving Tangent Addition Identity)',
        text: 'Given $\\tan A = \\frac{1}{2}$ and $\\tan B = \\frac{1}{3}$, show that $A + B = \\frac{\\pi}{4}$ where $A$ and $B$ are acute.',
        solution: '<p>$\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A\\tan B} = \\frac{1/2 + 1/3}{1 - (1/2)(1/3)} = \\frac{5/6}{1 - 1/6} = \\frac{5/6}{5/6} = 1$. [M1]<br>Since $A, B$ are acute ($0 &lt; A, B &lt; \\pi/2$), $0 &lt; A + B &lt; \\pi$. [R1]<br>$\\tan(A + B) = 1 \\implies A + B = \\frac{\\pi}{4}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Double Angle Tangent Equation)',
        text: 'Solve $\\tan(2x) = 4\\tan x$ for $0 &lt; x &lt; \\pi$.',
        solution: '<p>Use $\\tan(2x) = \\frac{2\\tan x}{1 - \\tan^2 x}$: [M1]<br>$\\frac{2\\tan x}{1 - \\tan^2 x} = 4\\tan x \\implies 2\\tan x = 4\\tan x(1 - \\tan^2 x)$. [M1]<br>$2\\tan x [1 - 2(1 - \\tan^2 x)] = 0 \\implies 2\\tan x [2\\tan^2 x - 1] = 0$.<br>• $\\tan x = 0 \\implies x$ has no solution in $(0, \\pi)$? At $x = 0$ or $\\pi$, outside open interval. But wait: if $x \\in (0, \\pi)$, $\\tan x \\neq 0$.<br>• $2\\tan^2 x - 1 = 0 \\implies \\tan^2 x = \\frac{1}{2} \\implies \\tan x = \\pm\\frac{1}{\\sqrt{2}}$. [A1]<br>$\\tan x = \\frac{1}{\\sqrt{2}} \\implies x = \\arctan(1/\\sqrt{2}) \\approx 0.615$ rad.<br>$\\tan x = -\\frac{1}{\\sqrt{2}} \\implies x = \\pi - 0.615 \\approx 2.53$ rad. [A1]<br>Solutions: $x \\approx 0.615, 2.53$ rad.</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Sin 3x Expansion)',
        text: 'Show that $\\sin(3x) = 3\\sin x - 4\\sin^3 x$. Hence find all solutions to $\\sin(3x) = 2\\sin x$ for $0 \\le x \\le \\pi$.',
        solution: '<p>$\\sin(3x) = \\sin(2x+x) = \\sin(2x)\\cos x + \\cos(2x)\\sin x$ [M1]<br>$= (2\\sin x\\cos x)\\cos x + (1 - 2\\sin^2 x)\\sin x = 2\\sin x\\cos^2 x + \\sin x - 2\\sin^3 x$<br>$= 2\\sin x(1 - \\sin^2 x) + \\sin x - 2\\sin^3 x = 3\\sin x - 4\\sin^3 x$. [A1]<br>Now solve $\\sin(3x) = 2\\sin x$:<br>$3\\sin x - 4\\sin^3 x = 2\\sin x \\implies \\sin x - 4\\sin^3 x = 0 \\implies \\sin x(1 - 4\\sin^2 x) = 0$. [M1]<br>• $\\sin x = 0 \\implies x = 0, \\pi$. [A1]<br>• $\\sin^2 x = \\frac{1}{4} \\implies \\sin x = \\frac{1}{2}$ (since in $[0, \\pi]$, $\\sin x \\ge 0$) $\\implies x = \\frac{\\pi}{6}, \\frac{5\\pi}{6}$. [A1]<br>Solutions: $x \\in \\left\\{0, \\frac{\\pi}{6}, \\frac{5\\pi}{6}, \\pi\\right\\}$.</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Harmonic Wave Maximum of Rational Expression)',
        text: 'Find the maximum value and the smallest positive $x$ where it occurs for $f(x) = \\frac{12}{5\\cos x + 12\\sin x + 20}$.',
        solution: '<p>Let $g(x) = 5\\cos x + 12\\sin x$. [M1]<br>$R = \\sqrt{5^2 + 12^2} = \\sqrt{169} = 13$. [A1]<br>Then $-13 \\le g(x) \\le 13$.<br>To maximize $f(x) = \\frac{12}{g(x) + 20}$, we must <strong>minimize</strong> the denominator: [M1]<br>Minimum denominator occurs when $g(x) = -13$:<br>$\\text{Denominatior} = -13 + 20 = 7$.<br>Maximum value: $f_{\\text{max}} = \\frac{12}{7}$. [A1]<br>Smallest positive $x$: $13\\sin(x + \\alpha) = -13 \\implies \\sin(x + \\alpha) = -1$, where $\\tan\\alpha = 5/12 \\approx 0.395$ rad.<br>$x + 0.395 = \\frac{3\\pi}{2} \\implies x = \\frac{3\\pi}{2} - 0.395 \\approx 4.712 - 0.395 = 4.32$ rad. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Half-Angle Tangent Substitution $t$-formula)',
        text: 'Let $t = \\tan\\left(\\frac{\\theta}{2}\\right)$. Prove that $\\sin\\theta = \\frac{2t}{1 + t^2}$ and $\\cos\\theta = \\frac{1 - t^2}{1 + t^2}$.',
        solution: '<p>Using $\\sin\\theta = 2\\sin(\\theta/2)\\cos(\\theta/2) = \\frac{2\\sin(\\theta/2)\\cos(\\theta/2)}{\\cos^2(\\theta/2) + \\sin^2(\\theta/2)}$. [M1]<br>Divide numerator and denominator by $\\cos^2(\\theta/2)$:<br>$\\sin\\theta = \\frac{2\\tan(\\theta/2)}{1 + \\tan^2(\\theta/2)} = \\frac{2t}{1 + t^2}$. [A1]<br>Similarly, $\\cos\\theta = \\cos^2(\\theta/2) - \\sin^2(\\theta/2) = \\frac{\\cos^2(\\theta/2) - \\sin^2(\\theta/2)}{\\cos^2(\\theta/2) + \\sin^2(\\theta/2)}$.<br>Divide by $\\cos^2(\\theta/2)$:<br>$\\cos\\theta = \\frac{1 - \\tan^2(\\theta/2)}{1 + \\tan^2(\\theta/2)} = \\frac{1 - t^2}{1 + t^2}$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 3)</h2>
        <div class="formula-card">
          <h4>Syllabus 3.9: Compound &amp; Double Angle Formulas</h4>
          $$\\sin(A \\pm B) = \\sin A\\cos B \\pm \\cos A\\sin B$$
          $$\\cos(A \\pm B) = \\cos A\\cos B \\mp \\sin A\\sin B$$
          $$\\tan(A \\pm B) = \\frac{\\tan A \\pm \\tan B}{1 \\mp \\tan A\\tan B}$$
          $$\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta, \\quad \\cos(2\\theta) = \\cos^2\\theta - \\sin^2\\theta = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta$$
          $$\\tan(2\\theta) = \\frac{2\\tan\\theta}{1 - \\tan^2\\theta}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Harmonic Linear Combination</h4>
          $$a\\sin x + b\\cos x = R\\sin(x + \\alpha), \\quad R = \\sqrt{a^2+b^2}, \\; \\tan\\alpha = \\frac{b}{a}$$
          $$\\text{Amplitude Range: } [-\\sqrt{a^2+b^2}, +\\sqrt{a^2+b^2}]$$
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Sign in Cosine Addition Formula</h4>
          <p>Remember that $\\cos(A + B)$ has a MINUS sign: $\\cos(A+B) = \\cos A\\cos B - \\sin A\\sin B$. One of the most frequent algebraic sign errors in Paper 1!</p>
        </div>
        <div class="pitfall-card">
          <h4>Adjusting the Domain for $(x + \\alpha)$</h4>
          <p>When solving $R\\sin(x + \\alpha) = c$, immediately adjust your search interval to $\\alpha \\le x + \\alpha \\le 2\\pi + \\alpha$. Otherwise, you will miss roots in Quadrant 4 or pick extraneous values outside $[0, 2\\pi]$.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'What is the maximum value of $f(x) = 5\\sin x - 12\\cos x + 3$?',
        options: [
          '10',
          '13',
          '16',
          '20'
        ],
        correct: 2,
        explanation: '$R = \\sqrt{5^2 + (-12)^2} = 13$. The maximum of $5\\sin x - 12\\cos x$ is 13. Adding 3 gives $13 + 3 = 16$.'
      },
      {
        id: 'q2',
        prompt: 'Which expression is equivalent to $\\frac{1 - \\cos(2x)}{\\sin(2x)}$?',
        options: [
          '$\\tan x$',
          '$\\cot x$',
          '$\\sin x$',
          '$\\cos x$'
        ],
        correct: 0,
        explanation: '$\\frac{1 - (1 - 2\\sin^2 x)}{2\\sin x\\cos x} = \\frac{2\\sin^2 x}{2\\sin x\\cos x} = \\frac{\\sin x}{\\cos x} = \\tan x$.'
      },
      {
        id: 'q3',
        prompt: 'If $\\cos\\theta = -\\frac{1}{3}$, what is the value of $\\cos(2\\theta)$?',
        options: [
          '$-\\frac{7}{9}$',
          '$\\frac{7}{9}$',
          '$-\\frac{1}{9}$',
          '$\\frac{2}{3}$'
        ],
        correct: 0,
        explanation: '$\\cos(2\\theta) = 2\\cos^2\\theta - 1 = 2(-1/3)^2 - 1 = 2(1/9) - 1 = 2/9 - 1 = -7/9$.'
      },
      {
        id: 'q4',
        prompt: 'What is the exact value of $\\sin(105^\\circ)$?',
        options: [
          '$\\frac{\\sqrt{6} + \\sqrt{2}}{4}$',
          '$\\frac{\\sqrt{6} - \\sqrt{2}}{4}$',
          '$\\frac{\\sqrt{3} + 1}{2}$',
          '$\\frac{\\sqrt{2} + 1}{4}$'
        ],
        correct: 0,
        explanation: '$\\sin(105^\\circ) = \\sin(60^\\circ + 45^\\circ) = \\sin 60^\\circ\\cos 45^\\circ + \\cos 60^\\circ\\sin 45^\\circ = \\frac{\\sqrt{3}}{2}\\frac{\\sqrt{2}}{2} + \\frac{1}{2}\\frac{\\sqrt{2}}{2} = \\frac{\\sqrt{6} + \\sqrt{2}}{4}$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Let $f(x) = \\sin(x + \\frac{\\pi}{3}) - \\sin(x - \\frac{\\pi}{3})$.<br><strong>(a)</strong> Show that $f(x) = \\sqrt{3}\\cos x$. [3 marks]<br><strong>(b)</strong> Hence solve $f(x) = 1$ for $0 \\le x \\le 2\\pi$. [3 marks]',
        solution: `
          <p><strong>(a) Expansion &amp; Simplification: [3 marks]</strong><br>
          $\\sin(x + \\pi/3) = \\sin x\\cos(\\pi/3) + \\cos x\\sin(\\pi/3) = \\frac{1}{2}\\sin x + \\frac{\\sqrt{3}}{2}\\cos x$ [M1].<br>
          $\\sin(x - \\pi/3) = \\sin x\\cos(\\pi/3) - \\cos x\\sin(\\pi/3) = \\frac{1}{2}\\sin x - \\frac{\\sqrt{3}}{2}\\cos x$ [M1].<br>
          Subtracting: $f(x) = 2\\left(\\frac{\\sqrt{3}}{2}\\cos x\\right) = \\sqrt{3}\\cos x$ [A1].</p>
          <p><strong>(b) Solving $f(x) = 1$: [3 marks]</strong><br>
          $\\sqrt{3}\\cos x = 1 \\implies \\cos x = \\frac{1}{\\sqrt{3}}$ [M1].<br>
          In $[0, 2\\pi]$, reference angle is $\\arccos(1/\\sqrt{3}) \\approx 0.955$ rad [A1].<br>
          Quadrants 1 &amp; 4: $x_1 \\approx 0.955$, $x_2 = 2\\pi - 0.955 \\approx 5.33$ rad [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'Consider the function $g(x) = 4\\cos(2x) - 3\\sin(2x)$.<br><strong>(a)</strong> Express $g(x)$ in the form $R\\cos(2x + \\alpha)$ where $R &gt; 0$ and $0 &lt; \\alpha &lt; \\frac{\\pi}{2}$. [3 marks]<br><strong>(b)</strong> Find the smallest positive value of $x$ for which $g(x)$ is a maximum. [2 marks]<br><strong>(c)</strong> Solve $g(x) = 2.5$ for $0 \\le x \\le \\pi$. [2 marks]',
        solution: `
          <p><strong>(a) Harmonic form: [3 marks]</strong><br>
          $R = \\sqrt{4^2 + (-3)^2} = 5$ [A1].<br>
          $R\\cos(2x + \\alpha) = R\\cos(2x)\\cos\\alpha - R\\sin(2x)\\sin\\alpha$.<br>
          $5\\cos\\alpha = 4 \\implies \\cos\\alpha = 0.8$, $5\\sin\\alpha = 3 \\implies \\sin\\alpha = 0.6$.<br>
          $\\alpha = \\arctan(0.75) \\approx 0.6435$ rad [A1].<br>
          $g(x) = 5\\cos(2x + 0.644)$ [A1].</p>
          <p><strong>(b) Maximum point: [2 marks]</strong><br>
          Maximum occurs when $\\cos(2x + 0.6435) = 1 \\implies 2x + 0.6435 = 2\\pi$ [M1]<br>
          $2x = 2\\pi - 0.6435 = 5.6397 \\implies x \\approx 2.82$ rad [A1].</p>
          <p><strong>(c) Solving $g(x) = 2.5$: [2 marks]</strong><br>
          $5\\cos(2x + 0.6435) = 2.5 \\implies \\cos(2x + 0.6435) = 0.5$ [M1].<br>
          $2x + 0.6435 = \\frac{\\pi}{3} \\approx 1.0472 \\implies 2x = 0.4037 \\implies x \\approx 0.202$ rad.<br>
          Next: $2x + 0.6435 = 2\\pi - \\frac{\\pi}{3} = \\frac{5\\pi}{3} \\approx 5.236 \\implies 2x = 4.5925 \\implies x \\approx 2.30$ rad [A1].<br>
          Solutions: $x \\approx 0.202, 2.30$ rad.</p>
        `
      }
    ]
  }
];

function generateHtml(guide) {
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
  <link rel="canonical" href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/${guide.folder}/">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${guide.pageTitle}">
  <meta property="og:description" content="${guide.metaDesc}">
  <meta property="og:url" content="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/${guide.folder}/">
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
  <link rel="stylesheet" href="/assets/css/ib-page.min.css?v=ac6d658f">
  <link rel="stylesheet" href="/assets/css/ib-dp-aa-sl-guides.css">

  <!-- KaTeX for Mathematical Typesetting -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous" onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false},{left:'\\\\(',right:'\\\\)',display:false},{left:'\\\\[',right:'\\\\]',display:true}],throwOnError:false})"></script>

  <script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/${guide.folder}/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"IB Mathematics","item":"https://sjmaths.com/ib/"},{"@type":"ListItem","position":3,"name":"IB DP Mathematics","item":"https://sjmaths.com/ib/dp-mathematics/"},{"@type":"ListItem","position":4,"name":"AA HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/"},{"@type":"ListItem","position":5,"name":"Geometry & Trig HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/"},{"@type":"ListItem","position":6,"name":"${guide.title}","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/${guide.folder}/"}]},{"@type":"Article","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/${guide.folder}/#article","headline":"${guide.title} | IB Math AA HL Guide","description":"${guide.metaDesc}","url":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/${guide.folder}/","dateModified":"2026-10-11","inLanguage":"en","articleSection":"IB DP Mathematics AA HL · Topic ${guide.code}","author":{"@type":"Person","name":"Sandeep Jaiswal","url":"https://sjmaths.com/pages/about.html"},"publisher":{"@type":"Organization","name":"SJMaths","url":"https://sjmaths.com/","logo":{"@type":"ImageObject","url":"https://sjmaths.com/assets/icons/icon-512x512.png"}}}]}</script>
</head>
<body>
<a class="skip-link study-skip" href="#main-content">Skip to main content</a>
<header class="ib-nav-header">
  <div class="ib-nav-container">
    <a href="/" class="ib-nav-brand"><span aria-hidden="true">∑</span> SJMaths</a>
    <nav class="ib-nav-links" aria-label="Main navigation">
      <a href="/ib/">IB Hub</a>
      <a href="/ib/dp-mathematics/">DP Portal</a>
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/">AA HL Hub</a>
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/">Topic 3 HL</a>
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
      <a href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/">Geometry &amp; Trigonometry</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
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
<script src="/assets/js/ib-study-tabs.js" defer></script>
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
