const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'statistics-and-probability');

const guides = [
  // Guide 15: Continuous Random Variables & PDFs
  {
    folder: 'continuous-random-variables-and-probability-density-functions',
    code: '4.13',
    title: 'Continuous Random Variables & PDFs',
    pageTitle: 'Continuous Random Variables & PDFs | IB Math AA HL | SJMaths',
    metaDesc: 'Master continuous random variables, probability density functions (PDF), and cumulative distribution functions (CDF) for IB DP Mathematics AA HL (Topic 4.13). Calculus probability, percentiles, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL continuous random variables, probability density function PDF, cumulative distribution function CDF, area under curve probability, median percentiles calculus',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Bridge calculus and probability. Master probability density functions (PDF) $f(x)$ satisfying $\\int f(x)\\,dx = 1$, integrate to compute interval probabilities $P(a \\le X \\le b)$, derive cumulative distribution functions (CDF) $F(x)$, and calculate medians and percentiles.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/vector-cross-product-and-planes/',
      title: 'Vector Cross Product & Equations of Planes'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/expectation-variance-and-linear-combinations/',
      title: 'Expectation, Variance & Linear Combinations'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-chart-area" style="color:var(--c-primary);"></i> Figure 4.1: PDF $f(x)$ with Probability Area vs CDF $F(x)$</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing PDF on left with shaded area between a and b, and CDF on right rising from 0 to 1">
            <!-- Left: PDF f(x) -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="330" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary, #4338ca)">PDF: f(x) ≥ 0, Total Area = 1</text>
              <line x1="30" y1="180" x2="300" y2="180" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="60" y1="35" x2="60" y2="200" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Shaded interval between a=120 and b=200 -->
              <path d="M 120,180 L 120,95 Q 160,50 200,95 L 200,180 Z" fill="rgba(99,102,241,0.25)" />
              <!-- Bell-like curve -->
              <path d="M 60,180 Q 110,180 130,120 Q 160,40 190,120 Q 210,180 280,180" fill="none" stroke="#6366f1" stroke-width="2.5" />
              <line x1="120" y1="180" x2="120" y2="95" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />
              <line x1="200" y1="180" x2="200" y2="95" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="120" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">a</text>
              <text x="200" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">b</text>
              <text x="160" y="140" text-anchor="middle" font-size="12" font-weight="bold" fill="#4338ca">P(a ≤ X ≤ b)</text>
              <text x="165" y="220" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Area = ∫ₐᵇ f(x) dx</text>
            </g>

            <!-- Right: CDF F(x) -->
            <g transform="translate(400, 20)">
              <rect x="0" y="0" width="330" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#10b981">CDF: F(x) = P(X ≤ x)</text>
              <line x1="30" y1="180" x2="300" y2="180" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="60" y1="35" x2="60" y2="200" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Upper boundary F=1 at y=70 -->
              <line x1="50" y1="70" x2="300" y2="70" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="3,3" />
              <text x="45" y="74" font-size="11" font-weight="bold" fill="#ef4444">1</text>
              <text x="45" y="125" font-size="11" fill="var(--c-text)">0.5</text>
              <line x1="50" y1="125" x2="160" y2="125" stroke="var(--c-border, #cbd5e1)" stroke-width="1" stroke-dasharray="2,2" />
              <!-- S-curve for CDF -->
              <path d="M 60,180 C 120,180 140,150 160,125 C 180,100 200,70 280,70" fill="none" stroke="#10b981" stroke-width="3" />
              <circle cx="160" cy="125" r="4" fill="#10b981" />
              <line x1="160" y1="125" x2="160" y2="180" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="160" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">m (median)</text>
              <text x="165" y="220" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">F(m) = 0.5, non-decreasing from 0 to 1</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Continuous Random Variables &amp; PDFs</h2>
        <p>A continuous random variable $X$ can take any real value in a continuous interval $[a, b]$ (or $(-\\infty, \\infty)$). It is described by its <strong>probability density function (PDF)</strong> $f(x)$ satisfying two mandatory conditions:</p>
        <ol class="theory-list">
          <li><strong>Non-negativity:</strong> $f(x) \\ge 0$ for all $x \\in \\mathbb{R}$.</li>
          <li><strong>Total Probability normalization:</strong>
          $$\\int_{-\\infty}^\\infty f(x)\\,dx = 1$$</li>
        </ol>
        <p><strong>Fundamental Principle:</strong> Probability is represented by <strong>area under the curve</strong>:</p>
        $$P(a \\le X \\le b) = \\int_a^b f(x)\\,dx$$
        <p><em>Crucial note:</em> The probability of any single exact exact value is zero: $P(X = c) = \\int_c^c f(x)\\,dx = 0$. Consequently, strict and non-strict inequalities have identical probabilities:</p>
        $$P(a \\le X \\le b) = P(a &lt; X \\le b) = P(a \\le X &lt; b) = P(a &lt; X &lt; b)$$

        <h2>2. Cumulative Distribution Function (CDF)</h2>
        <p>The <strong>cumulative distribution function (CDF)</strong> $F(x)$ represents the accumulated probability up to $x$:</p>
        $$F(x) = P(X \\le x) = \\int_{-\\infty}^x f(t)\\,dt$$
        <ul class="theory-list">
          <li><strong>Fundamental Theorem of Calculus:</strong> The PDF is the derivative of the CDF:
          $$f(x) = F\'(x) = \\frac{d}{dx}F(x)$$</li>
          <li><strong>Interval probability via CDF:</strong> $P(a \\le X \\le b) = F(b) - F(a)$.</li>
          <li><strong>Boundary conditions:</strong> $\\lim_{x \\to -\\infty} F(x) = 0$ and $\\lim_{x \\to \\infty} F(x) = 1$.</li>
        </ul>

        <h2>3. Median, Quartiles, and Percentiles</h2>
        <p>Quantiles are determined by setting the CDF equal to the desired accumulated probability:</p>
        <ul class="theory-list">
          <li><strong>Median ($m$):</strong> The 50th percentile: $F(m) = 0.5 \\iff \\int_{-\\infty}^m f(x)\\,dx = 0.5$.</li>
          <li><strong>Lower Quartile ($Q_1$):</strong> The 25th percentile: $F(Q_1) = 0.25$.</li>
          <li><strong>Upper Quartile ($Q_3$):</strong> The 75th percentile: $F(Q_3) = 0.75$.</li>
          <li><strong>Interquartile Range (IQR):</strong> $\\text{IQR} = Q_3 - Q_1$.</li>
        </ul>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Finding Normalization Constant $k$</h4>
          <p>A continuous random variable $X$ has PDF given by:</p>
          $$f(x) = \\begin{cases} k x(2 - x) & \\text{for } 0 \\le x \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}$$
          <p><strong>(a)</strong> Show that $k = \\frac{3}{4}$.<br>
          <strong>(b)</strong> Calculate $P(0.5 \\le X \\le 1.5)$.</p>
          <p><strong>Solution:</strong></p>
          <p><strong>(a) Normalization:</strong></p>
          $$\\int_0^2 k(2x - x^2)\\,dx = 1 \\implies k \\left[ x^2 - \\frac{x^3}{3} \\right]_0^2 = 1$$
          $$k \\left( 4 - \\frac{8}{3} \\right) = 1 \\implies k \\left(\\frac{4}{3}\\right) = 1 \\implies k = \\frac{3}{4}$$
          <p><strong>(b) Interval Probability:</strong></p>
          $$P(0.5 \\le X \\le 1.5) = \\int_{0.5}^{1.5} \\frac{3}{4}(2x - x^2)\\,dx = \\frac{3}{4}\\left[ x^2 - \\frac{x^3}{3} \\right]_{0.5}^{1.5}$$
          $$= \\frac{3}{4} \\left[ \\left(2.25 - \\frac{3.375}{3}\\right) - \\left(0.25 - \\frac{0.125}{3}\\right) \\right] = \\frac{3}{4} [ (2.25 - 1.125) - (0.25 - 0.04167) ]$$
          $$= \\frac{3}{4} [ 1.125 - 0.20833 ] = \\frac{3}{4}(0.91667) = \\frac{11}{16} = 0.6875$$
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Establishing the CDF and Finding the Median</h4>
          <p>For $f(x) = \\frac{3}{4}(2x - x^2)$ on $[0, 2]$:<br>
          <strong>(a)</strong> Find the cumulative distribution function $F(x)$ for all $x \\in \\mathbb{R}$.<br>
          <strong>(b)</strong> Find the median of $X$.</p>
          <p><strong>Solution:</strong></p>
          <p><strong>(a) CDF derivation:</strong><br>
          • For $x &lt; 0$: $F(x) = 0$.<br>
          • For $0 \\le x \\le 2$:</p>
          $$F(x) = \\int_0^x \\frac{3}{4}(2t - t^2)\\,dt = \\frac{3}{4}\\left[ t^2 - \\frac{t^3}{3} \\right]_0^x = \\frac{3}{4}x^2 - \\frac{1}{4}x^3 = \\frac{x^2(3 - x)}{4}$$
          <p>• For $x &gt; 2$: $F(x) = 1$.</p>
          <p><strong>(b) Median $m$:</strong><br>
          Set $F(m) = 0.5$: $\\frac{3m^2 - m^3}{4} = \\frac{1}{2} \\implies 3m^2 - m^3 = 2 \\implies m^3 - 3m^2 + 2 = 0$.<br>
          Notice $m = 1$ is a root: $1^3 - 3(1) + 2 = 0$.<br>
          Since $f(x)$ is symmetric about $x = 1$ (parabola with vertex at $x = 1$), the median is exactly $m = 1$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Conditional Probability with Continuous Random Variables</h4>
          <p>Let $X$ have PDF $f(x) = 2e^{-2x}$ for $x \\ge 0$. Calculate $P(X &gt; 3 \\mid X &gt; 1)$.</p>
          <p><strong>Solution:</strong></p>
          <p>By definition of conditional probability:</p>
          $$P(X &gt; 3 \\mid X &gt; 1) = \\frac{P(X &gt; 3 \\cap X &gt; 1)}{P(X &gt; 1)} = \\frac{P(X &gt; 3)}{P(X &gt; 1)}$$
          <p>For any $k &gt; 0$:</p>
          $$P(X &gt; k) = \\int_k^\\infty 2e^{-2x}\\,dx = \\left[-e^{-2x}\\right]_k^\\infty = 0 - (-e^{-2k}) = e^{-2k}$$
          <p>Therefore:</p>
          $$P(X &gt; 3 \\mid X &gt; 1) = \\frac{e^{-2(3)}}{e^{-2(1)}} = \\frac{e^{-6}}{e^{-2}} = e^{-4} \\approx 0.0183$$
          <p><em>(Notice this illustrates the famous "memoryless property" of the exponential distribution: $P(X &gt; s + t \\mid X &gt; s) = P(X &gt; t) = e^{-2(2)} = e^{-4}$.)</em></p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Normalization Constant)',
        text: 'A random variable $X$ has PDF $f(x) = c x^2$ for $0 \\le x \\le 3$. Find the value of $c$.',
        solution: '<p>$\\int_0^3 c x^2\\,dx = 1 \\implies c\\left[\\frac{x^3}{3}\\right]_0^3 = 1$. [M1]<br>$c\\left(\\frac{27}{3}\\right) = 9c = 1 \\implies c = \\frac{1}{9}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Probability from PDF)',
        text: 'Given $f(x) = \\frac{1}{9}x^2$ for $0 \\le x \\le 3$, find $P(1 \\le X \\le 2)$.',
        solution: '<p>$P(1 \\le X \\le 2) = \\int_1^2 \\frac{1}{9}x^2\\,dx = \\frac{1}{9}\\left[\\frac{x^3}{3}\\right]_1^2 = \\frac{1}{27}(8 - 1) = \\frac{7}{27}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Point Probability)',
        text: 'For a continuous random variable $X$, what is $P(X = 2)$? Explain why.',
        solution: '<p>$P(X = 2) = 0$. [A1]<br>For any continuous random variable, probability is represented by area under the density curve. A single point has width zero, so $\\int_2^2 f(x)\\,dx = 0$. [R1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: CDF from Piecewise PDF)',
        text: 'Let $f(x) = \\begin{cases} \\frac{1}{2}x & 0 \\le x \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}$. Find the CDF $F(x)$ for $0 \\le x \\le 2$.',
        solution: '<p>$F(x) = \\int_0^x \\frac{1}{2}t\\,dt = \\left[\\frac{t^2}{4}\\right]_0^x = \\frac{x^2}{4}$. [M1][A1]<br>Complete piecewise: $F(x) = 0$ for $x &lt; 0$, $\\frac{x^2}{4}$ for $0 \\le x \\le 2$, and $1$ for $x &gt; 2$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Finding the Median)',
        text: 'Find the median of the distribution with CDF $F(x) = \\frac{x^2}{4}$ for $0 \\le x \\le 2$.',
        solution: '<p>Set $F(m) = 0.5$: [M1]<br>$\\frac{m^2}{4} = 0.5 \\implies m^2 = 2 \\implies m = \\sqrt{2} \\approx 1.414$ (since $m \\in [0, 2]$). [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Finding PDF from Given CDF)',
        text: 'The CDF of $Y$ is $F(y) = 1 - \\frac{16}{y^2}$ for $y \\ge 4$. Find the PDF $f(y)$.',
        solution: '<p>$f(y) = F\'(y) = \\frac{d}{dy}\\left(1 - 16y^{-2}\\right)$ [M1]<br>$= 0 - 16(-2y^{-3}) = \\frac{32}{y^3}$ for $y \\ge 4$ (and 0 otherwise). [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Interquartile Range)',
        text: 'For $F(x) = \\frac{x^3}{8}$ for $0 \\le x \\le 2$, find the interquartile range (IQR).',
        solution: '<p>Lower quartile $Q_1$: $F(Q_1) = 0.25 \\implies \\frac{Q_1^3}{8} = \\frac{1}{4} \\implies Q_1^3 = 2 \\implies Q_1 = \\sqrt[3]{2} \\approx 1.260$. [M1]<br>Upper quartile $Q_3$: $F(Q_3) = 0.75 \\implies \\frac{Q_3^3}{8} = \\frac{3}{4} \\implies Q_3^3 = 6 \\implies Q_3 = \\sqrt[3]{6} \\approx 1.817$. [M1]<br>$\\text{IQR} = Q_3 - Q_1 = \\sqrt[3]{6} - \\sqrt[3]{2} \\approx 1.817 - 1.260 = 0.557$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Piecewise PDF with Two Intervals)',
        text: 'A random variable $X$ has PDF $f(x) = \\begin{cases} k x & 0 \\le x \\le 1 \\\\ k(2 - x) & 1 &lt; x \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}$.<br>(a) Find $k$.<br>(b) Find $P(0.5 \\le X \\le 1.5)$.',
        solution: '<p><strong>(a) Normalization:</strong> $\\int_0^1 kx\\,dx + \\int_1^2 k(2-x)\\,dx = 1$. [M1]<br>$k\\left[\\frac{x^2}{2}\\right]_0^1 + k\\left[2x - \\frac{x^2}{2}\\right]_1^2 = k(1/2) + k[(4 - 2) - (2 - 1/2)] = \\frac{k}{2} + \\frac{k}{2} = k = 1$. [A1]</p><p><strong>(b) Probability:</strong><br>By symmetry about $x = 1$, $P(0.5 \\le X \\le 1.5) = 2\\int_{0.5}^1 x\\,dx = 2\\left[\\frac{x^2}{2}\\right]_{0.5}^1 = 1^2 - 0.5^2 = 1 - 0.25 = 0.75$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Infinite Domain Exponential Distribution)',
        text: 'The lifetime $T$ (in years) of an electronic component has PDF $f(t) = 0.5e^{-0.5t}$ for $t \\ge 0$. Find the 90th percentile of component lifetime.',
        solution: '<p>CDF $F(t) = \\int_0^t 0.5e^{-0.5u}\\,du = \\left[-e^{-0.5u}\\right]_0^t = 1 - e^{-0.5t}$. [M1]<br>90th percentile $p_{90}$: $F(p_{90}) = 0.90$. [M1]<br>$1 - e^{-0.5p_{90}} = 0.90 \\implies e^{-0.5p_{90}} = 0.10$.<br>Take natural logs: $-0.5p_{90} = \\ln(0.10) = -\\ln(10) \\implies p_{90} = 2\\ln(10) \\approx 4.61$ years. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Mode of Continuous Distribution)',
        text: 'Find the mode of the distribution with PDF $f(x) = 12(x^2 - x^3)$ for $0 \\le x \\le 1$.',
        solution: '<p>The mode is the value of $x$ where $f(x)$ attains its global maximum. [M1]<br>$f\'(x) = 12(2x - 3x^2) = 12x(2 - 3x)$. [M1]<br>Setting $f\'(x) = 0 \\implies x = 0$ or $x = \\frac{2}{3}$.<br>$f\'\'(x) = 12(2 - 6x)$. At $x = 2/3$, $f\'\'(2/3) = 12(2 - 4) = -24 &lt; 0$ (local/global maximum).<br>Mode $= \\frac{2}{3}$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 4)</h2>
        <div class="formula-card">
          <h4>Syllabus 4.13: Continuous Random Variables</h4>
          $$P(a \\le X \\le b) = \\int_a^b f(x)\\,dx$$
          $$\\int_{-\\infty}^\\infty f(x)\\,dx = 1$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Relationship between CDF and PDF</h4>
          $$F(x) = \\int_{-\\infty}^x f(t)\\,dt, \\quad f(x) = F\'(x) = \\frac{d}{dx}F(x)$$
        </div>
        <div class="formula-card">
          <h4>2. Quantile Equations</h4>
          $$F(m) = 0.5 \\text{ (Median)}, \\quad F(Q_1) = 0.25, \\quad F(Q_3) = 0.75$$
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Dummy Variable in CDF Integral</h4>
          <p>Always write $F(x) = \\int_{-\\infty}^x f(t)\\,dt$ using a dummy variable $t$. Writing $\\int f(x)\\,dx$ with upper limit $x$ leads to confusing and mathematically invalid expressions.</p>
        </div>
        <div class="pitfall-card">
          <h4>P(X = c) = 0 Concept</h4>
          <p>In continuous probability, $P(X \\le c)$ is IDENTICAL to $P(X &lt; c)$. Do not treat continuous random variables like discrete distributions where $\\le$ and $&lt;$ differ!</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If $f(x)$ is a PDF on $[0, 4]$, then $\\int_0^4 f(x)\\,dx$ must equal:',
        options: [
          '0',
          '0.5',
          '1',
          '4'
        ],
        correct: 2,
        explanation: 'By the total probability axiom, the integral of any valid PDF over its entire domain must equal 1.'
      },
      {
        id: 'q2',
        prompt: 'If $F(x) = x^2/9$ for $0 \\le x \\le 3$, what is the median?',
        options: [
          '$1.5$',
          '$\\sqrt{4.5} \\approx 2.12$',
          '$2.25$',
          '$3$'
        ],
        correct: 1,
        explanation: '$F(m) = 0.5 \\implies m^2/9 = 0.5 \\implies m^2 = 4.5 \\implies m = \\sqrt{4.5} \\approx 2.12$.'
      },
      {
        id: 'q3',
        prompt: 'For a continuous random variable $X$, what is $P(X \\ge 5) - P(X > 5)$?',
        options: [
          '0',
          '0.5',
          '$f(5)$',
          '1'
        ],
        correct: 0,
        explanation: 'For any continuous random variable, $P(X = 5) = 0$, so $P(X \\ge 5) = P(X > 5)$, and their difference is 0.'
      },
      {
        id: 'q4',
        prompt: 'If the CDF of $X$ is $F(x) = x^3$ on $[0, 1]$, what is the PDF $f(x)$?',
        options: [
          '$3x^2$',
          '$x^4/4$',
          '$x^2/3$',
          '$3x$'
        ],
        correct: 0,
        explanation: '$f(x) = F\'(x) = \\frac{d}{dx}(x^3) = 3x^2$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'The continuous random variable $X$ has PDF $f(x) = \\begin{cases} \\frac{3}{8}x^2 & 0 \\le x \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}$.<br><strong>(a)</strong> Find the cumulative distribution function $F(x)$ for $0 \\le x \\le 2$. [2 marks]<br><strong>(b)</strong> Determine the median of $X$. [2 marks]<br><strong>(c)</strong> Find $P(X &gt; 1 \\mid X &lt; 1.5)$. [2 marks]',
        solution: `
          <p><strong>(a) CDF: [2 marks]</strong><br>
          $F(x) = \\int_0^x \\frac{3}{8}t^2\\,dt = \\frac{3}{8}\\left[\\frac{t^3}{3}\\right]_0^x = \\frac{x^3}{8}$ for $0 \\le x \\le 2$ [A1].</p>
          <p><strong>(b) Median: [2 marks]</strong><br>
          $F(m) = 0.5 \\implies \\frac{m^3}{8} = \\frac{1}{2} \\implies m^3 = 4 \\implies m = \\sqrt[3]{4} \\approx 1.587$ [A1].</p>
          <p><strong>(c) Conditional probability: [2 marks]</strong><br>
          $P(X &gt; 1 \\mid X &lt; 1.5) = \\frac{P(1 &lt; X &lt; 1.5)}{P(X &lt; 1.5)} = \\frac{F(1.5) - F(1)}{F(1.5)}$ [M1].<br>
          $F(1.5) = \\frac{1.5^3}{8} = \\frac{3.375}{8} = 0.421875$.<br>
          $F(1) = \\frac{1}{8} = 0.125$.<br>
          Probability $= \\frac{0.421875 - 0.125}{0.421875} = \\frac{0.296875}{0.421875} = \\frac{19}{27} \\approx 0.704$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'A random variable $X$ has PDF $f(x) = k\\sin x$ for $0 \\le x \\le \\pi$.<br><strong>(a)</strong> Find the value of $k$. [2 marks]<br><strong>(b)</strong> Find the CDF $F(x)$. [2 marks]<br><strong>(c)</strong> Show that the median is $\\frac{\\pi}{2}$ and find the lower quartile $Q_1$. [3 marks]',
        solution: `
          <p><strong>(a) Constant $k$: [2 marks]</strong><br>
          $\\int_0^\\pi k\\sin x\\,dx = 1 \\implies k[-\\cos x]_0^\\pi = k(1 - (-1)) = 2k = 1 \\implies k = \\frac{1}{2}$ [A1].</p>
          <p><strong>(b) CDF $F(x)$: [2 marks]</strong><br>
          $F(x) = \\int_0^x \\frac{1}{2}\\sin t\\,dt = \\frac{1}{2}[-\\cos t]_0^x = \\frac{1}{2}(1 - \\cos x) = \\frac{1 - \\cos x}{2}$ for $0 \\le x \\le \\pi$ [A1].</p>
          <p><strong>(c) Median &amp; Lower Quartile: [3 marks]</strong><br>
          $F(m) = 0.5 \\implies \\frac{1 - \\cos m}{2} = 0.5 \\implies 1 - \\cos m = 1 \\implies \\cos m = 0 \\implies m = \\frac{\\pi}{2}$ [A1].<br>
          Lower quartile: $F(Q_1) = 0.25 \\implies \\frac{1 - \\cos Q_1}{2} = 0.25 \\implies 1 - \\cos Q_1 = 0.5 \\implies \\cos Q_1 = 0.5$ [M1].<br>
          $Q_1 = \\arccos(0.5) = \\frac{\\pi}{3}$ [A1].</p>
        `
      }
    ]
  },

  // Guide 16: Expectation, Variance & Linear Combinations
  {
    folder: 'expectation-variance-and-linear-combinations',
    code: '4.14, 4.15',
    title: 'Expectation, Variance & Linear Combinations',
    pageTitle: 'Expectation, Variance & Linear Combinations | IB Math AA HL | SJMaths',
    metaDesc: 'Master expected value E(X), variance Var(X), and linear combinations of independent random variables for IB DP Mathematics AA HL (Topics 4.14 & 4.15). Calculus integration, aX ± bY, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL expected value continuous, variance Var(X) calculus, linear combinations random variables E(aX + bY), variance difference independent, Var(aX - bY)',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Harness integration to compute the mean $E(X) = \\int x f(x)\\,dx$ and variance $\\text{Var}(X) = E(X^2) - [E(X)]^2$. Master expectation and variance algebra for linear combinations of independent random variables $E(aX \\pm bY)$ and $\\text{Var}(aX \\pm bY)$.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/continuous-random-variables-and-probability-density-functions/',
      title: 'Continuous Random Variables & PDFs'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/limits-and-lhospitals-rule/',
      title: 'Advanced Limits & L’Hôpital’s Rule'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-calculator" style="color:var(--c-primary);"></i> Figure 4.2: Distribution Center of Mass: Mean $E(X)$ vs Standard Deviation $\\sigma$</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing PDF with mean mu at center of mass and variance spread sigma">
            <!-- Axes at center (380, 210) -->
            <line x1="80" y1="210" x2="680" y2="210" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="380" y1="30" x2="380" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="2" stroke-dasharray="4,4" />
            <text x="670" y="200" fill="var(--c-text)" font-size="13" font-weight="bold">x</text>
            <text x="390" y="45" fill="var(--c-text)" font-size="13" font-weight="bold">f(x)</text>

            <!-- Skewed PDF Curve -->
            <!-- Base from x=140 to x=620, peak at x=340, y=70, balance point E(X) at x=380 -->
            <path d="M 140,210 Q 240,205 280,140 Q 330,60 380,85 Q 460,120 540,185 Q 580,210 620,210" fill="none" stroke="#6366f1" stroke-width="3" />
            
            <!-- Shaded variance spread between mu - sigma (280) and mu + sigma (480) -->
            <rect x="280" y="195" width="200" height="15" fill="rgba(16,185,129,0.3)" rx="4" />
            <line x1="280" y1="200" x2="480" y2="200" stroke="#10b981" stroke-width="2" />
            <circle cx="280" cy="200" r="4" fill="#10b981" />
            <circle cx="480" cy="200" r="4" fill="#10b981" />
            <text x="280" y="235" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">μ - σ</text>
            <text x="480" y="235" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">μ + σ</text>

            <!-- Mean μ marker (balance fulcrum) -->
            <polygon points="380,210 370,225 390,225" fill="#ef4444" />
            <circle cx="380" cy="210" r="5" fill="#ef4444" />
            <text x="380" y="245" text-anchor="middle" font-size="13" font-weight="bold" fill="#ef4444">μ = E(X) (Center of Mass)</text>

            <!-- Mode Peak -->
            <circle cx="340" cy="65" r="4" fill="#f59e0b" />
            <text x="340" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="#f59e0b">Mode (Peak)</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Expected Value (Mean) of a Continuous Random Variable</h2>
        <p>The <strong>expected value</strong> $E(X)$ (or population mean $\\mu$) is the center of mass of the probability density function:</p>
        $$E(X) = \\mu = \\int_{-\\infty}^\\infty x f(x)\\,dx$$
        <p>For any continuous function $g(X)$ (such as $X^2$, $e^X$, etc.):</p>
        $$E(g(X)) = \\int_{-\\infty}^\\infty g(x) f(x)\\,dx$$

        <h2>2. Variance and Standard Deviation</h2>
        <p>The <strong>variance</strong> $\\text{Var}(X) = \\sigma^2$ measures the dispersion of the distribution around its mean:</p>
        $$\\text{Var}(X) = E\\left((X - \\mu)^2\\right) = E(X^2) - [E(X)]^2$$
        <p>where the second moment is computed by:</p>
        $$E(X^2) = \\int_{-\\infty}^\\infty x^2 f(x)\\,dx$$
        <p>The <strong>standard deviation</strong> is the positive square root: $\\sigma = \\sqrt{\\text{Var}(X)}$.</p>

        <h2>3. Linear Transformations of a Single Variable $aX + b$</h2>
        <ul class="theory-list">
          <li><strong>Expectation:</strong> $E(aX + b) = aE(X) + b$.</li>
          <li><strong>Variance:</strong> $\\text{Var}(aX + b) = a^2 \\text{Var}(X)$. <em>(Adding constant $b$ does not change spread!)</em></li>
          <li><strong>Standard deviation:</strong> $\\sigma_{aX + b} = |a|\\sigma_X$.</li>
        </ul>

        <h2>4. Linear Combinations of Independent Random Variables (Syllabus 4.15)</h2>
        <p>Let $X$ and $Y$ be random variables, and let $a, b \\in \\mathbb{R}$:</p>
        <ul class="theory-list">
          <li><strong>Expectation Rule (Always holds):</strong>
          $$E(aX + bY) = aE(X) + bE(Y)$$</li>
          <li><strong>Variance Rule (Requires $X$ and $Y$ to be INDEPENDENT):</strong>
          $$\\text{Var}(aX + bY) = a^2\\text{Var}(X) + b^2\\text{Var}(Y)$$
          $$\\text{Var}(aX - bY) = a^2\\text{Var}(X) + b^2\\text{Var}(Y)$$
          <br><strong>Critical Rule:</strong> Variances ALWAYS add! Subtracting random variables increases uncertainty, so $\\text{Var}(X - Y) = \\text{Var}(X) + \\text{Var}(Y)$, NEVER minus!</li>
        </ul>

        <h2>5. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Calculating Mean and Variance from a PDF</h4>
          <p>A continuous random variable $X$ has PDF $f(x) = 3x^2$ for $0 \\le x \\le 1$. Calculate $E(X)$, $\\text{Var}(X)$, and the standard deviation $\\sigma$.</p>
          <p><strong>Solution:</strong></p>
          <p>• Expected value $E(X)$:</p>
          $$E(X) = \\int_0^1 x(3x^2)\\,dx = \\int_0^1 3x^3\\,dx = \\left[ \\frac{3x^4}{4} \\right]_0^1 = \\frac{3}{4} = 0.75$$
          <p>• Second moment $E(X^2)$:</p>
          $$E(X^2) = \\int_0^1 x^2(3x^2)\\,dx = \\int_0^1 3x^4\\,dx = \\left[ \\frac{3x^5}{5} \\right]_0^1 = \\frac{3}{5} = 0.6$$
          <p>• Variance $\\text{Var}(X)$:</p>
          $$\\text{Var}(X) = E(X^2) - [E(X)]^2 = \\frac{3}{5} - \\left(\\frac{3}{4}\\right)^2 = \\frac{3}{5} - \\frac{9}{16} = \\frac{48 - 45}{80} = \\frac{3}{80} = 0.0375$$
          <p>• Standard deviation: $\\sigma = \\sqrt{\\frac{3}{80}} \\approx 0.194$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Linear Combinations of Independent Measurements</h4>
          <p>Independent random variables $X$ and $Y$ have means $E(X) = 20, E(Y) = 15$ and variances $\\text{Var}(X) = 4, \\text{Var}(Y) = 9$.<br>
          Find the mean and standard deviation of $W = 3X - 2Y + 5$.</p>
          <p><strong>Solution:</strong></p>
          <p>• Mean $E(W)$:</p>
          $$E(W) = E(3X - 2Y + 5) = 3E(X) - 2E(Y) + 5 = 3(20) - 2(15) + 5 = 60 - 30 + 5 = 35$$
          <p>• Variance $\\text{Var}(W)$:</p>
          $$\\text{Var}(W) = \\text{Var}(3X - 2Y + 5) = 3^2\\text{Var}(X) + (-2)^2\\text{Var}(Y) = 9(4) + 4(9) = 36 + 36 = 72$$
          <p>• Standard deviation $\\sigma_W = \\sqrt{72} = 6\\sqrt{2} \\approx 8.49$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Sum of $n$ Independent Identical Observations vs $n X$</h4>
          <p>Let $X$ have mean $\\mu = 10$ and variance $\\sigma^2 = 4$. Compare:<br>
          <strong>(a)</strong> $T = X_1 + X_2 + X_3 + X_4$ (sum of 4 independent observations).<br>
          <strong>(b)</strong> $S = 4X$ (single observation scaled by 4).</p>
          <p><strong>Solution:</strong></p>
          <p><strong>(a) Sum of 4 independent observations:</strong><br>
          $E(T) = E(X_1) + E(X_2) + E(X_3) + E(X_4) = 4(10) = 40$.<br>
          $\\text{Var}(T) = \\text{Var}(X_1) + \\text{Var}(X_2) + \\text{Var}(X_3) + \\text{Var}(X_4) = 4(4) = 16$.<br>
          Standard deviation $\\sigma_T = \\sqrt{16} = 4$.</p>
          <p><strong>(b) Scaled single observation $4X$:</strong><br>
          $E(S) = 4E(X) = 4(10) = 40$.<br>
          $\\text{Var}(S) = 4^2\\text{Var}(X) = 16(4) = 64$.<br>
          Standard deviation $\\sigma_S = \\sqrt{64} = 8$.<br>
          <em>(Notice that scaling a single variable produces 4 times the variance of summing independent variables!)</em></p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Expected Value Calculation)',
        text: 'A random variable $X$ has PDF $f(x) = 2x$ for $0 \\le x \\le 1$. Calculate $E(X)$.',
        solution: '<p>$E(X) = \\int_0^1 x(2x)\\,dx = \\int_0^1 2x^2\\,dx = \\left[\\frac{2x^3}{3}\\right]_0^1 = \\frac{2}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Variance from Moments)',
        text: 'Given that $E(X) = 5$ and $E(X^2) = 29$, calculate $\\text{Var}(X)$ and the standard deviation.',
        solution: '<p>$\\text{Var}(X) = E(X^2) - [E(X)]^2 = 29 - 5^2 = 29 - 25 = 4$. [A1]<br>Standard deviation $\\sigma = \\sqrt{4} = 2$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Linear Scaling)',
        text: 'If $E(X) = 12$ and $\\text{Var}(X) = 9$, find $E(2X - 5)$ and $\\text{Var}(2X - 5)$.',
        solution: '<p>$E(2X - 5) = 2E(X) - 5 = 2(12) - 5 = 19$. [A1]<br>$\\text{Var}(2X - 5) = 2^2\\text{Var}(X) = 4(9) = 36$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Variance of Continuous Distribution)',
        text: 'For $f(x) = \\frac{1}{2}$ on $[0, 2]$ (uniform distribution), calculate $\\text{Var}(X)$ by integration.',
        solution: '<p>$E(X) = \\int_0^2 x(1/2)\\,dx = \\left[\\frac{x^2}{4}\\right]_0^2 = 1$. [M1]<br>$E(X^2) = \\int_0^2 x^2(1/2)\\,dx = \\left[\\frac{x^3}{6}\\right]_0^2 = \\frac{8}{6} = \\frac{4}{3}$. [M1]<br>$\\text{Var}(X) = \\frac{4}{3} - 1^2 = \\frac{1}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Variance of Difference of Variables)',
        text: 'Independent variables $A$ and $B$ have variances $\\text{Var}(A) = 16$ and $\\text{Var}(B) = 25$. Calculate $\\text{Var}(A - B)$ and $\\text{Var}(2A - 3B)$.',
        solution: '<p>$\\text{Var}(A - B) = \\text{Var}(A) + (-1)^2\\text{Var}(B) = 16 + 25 = 41$. [A1]<br>$\\text{Var}(2A - 3B) = 2^2\\text{Var}(A) + (-3)^2\\text{Var}(B) = 4(16) + 9(25) = 64 + 225 = 289$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Expected Value of Non-linear Function)',
        text: 'If $X$ has PDF $f(x) = e^{-x}$ for $x \\ge 0$, calculate $E(e^{X/2})$.',
        solution: '<p>$E(e^{X/2}) = \\int_0^\\infty e^{x/2} e^{-x}\\,dx = \\int_0^\\infty e^{-x/2}\\,dx$. [M1]<br>$= \\left[ -2e^{-x/2} \\right]_0^\\infty = 0 - (-2) = 2$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Elevator Weight Capacity Model)',
        text: 'An elevator holds 8 passengers whose weights $W_i$ are independent random variables with mean $70$ kg and standard deviation $10$ kg. Find the mean and standard deviation of total weight $T = \\sum_{i=1}^8 W_i$.',
        solution: '<p>$E(T) = \\sum_{i=1}^8 E(W_i) = 8(70) = 560$ kg. [A1]<br>Since the weights are independent:<br>$\\text{Var}(T) = \\sum_{i=1}^8 \\text{Var}(W_i) = 8(10^2) = 8(100) = 800$ kg$^2$. [M1]<br>Standard deviation $\\sigma_T = \\sqrt{800} = 20\\sqrt{2} \\approx 28.3$ kg. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Linear Algebra of Sample Mean)',
        text: 'Let $\\bar{X} = \\frac{1}{n}\\sum_{i=1}^n X_i$ be the sample mean of $n$ independent identical observations with mean $\\mu$ and variance $\\sigma^2$. Prove that $E(\\bar{X}) = \\mu$ and $\\text{Var}(\\bar{X}) = \\frac{\\sigma^2}{n}$.',
        solution: '<p>$E(\\bar{X}) = E\\left(\\frac{1}{n}\\sum X_i\\right) = \\frac{1}{n}\\sum E(X_i) = \\frac{1}{n}(n\\mu) = \\mu$. [M1][A1]<br>$\\text{Var}(\\bar{X}) = \\text{Var}\\left(\\frac{1}{n}\\sum X_i\\right) = \\left(\\frac{1}{n}\\right)^2 \\text{Var}\\left(\\sum X_i\\right)$. [M1]<br>Since $X_i$ are independent, $\\text{Var}\\left(\\sum X_i\\right) = \\sum \\text{Var}(X_i) = n\\sigma^2$.<br>$\\text{Var}(\\bar{X}) = \\frac{1}{n^2}(n\\sigma^2) = \\frac{\\sigma^2}{n}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Mean of Symmetric Continuous Distribution)',
        text: 'Let $f(x)$ be a PDF symmetric about $x = c$, so that $f(c - u) = f(c + u)$. Prove that $E(X) = c$.',
        solution: '<p>$E(X) = \\int_{-\\infty}^\\infty x f(x)\\,dx$. Let $u = x - c \\implies x = c + u$. [M1]<br>$E(X) = \\int_{-\\infty}^\\infty (c + u)f(c + u)\\,du = c\\int_{-\\infty}^\\infty f(c + u)\\,du + \\int_{-\\infty}^\\infty u f(c + u)\\,du$. [M1]<br>Since $\\int_{-\\infty}^\\infty f(c + u)\\,du = 1$ (total probability) and $u f(c + u)$ is an <strong>odd function</strong> of $u$ ($(-u)f(c - u) = -u f(c + u)$), its integral is 0! [R1]<br>Therefore $E(X) = c(1) + 0 = c$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Profit Optimization Model)',
        text: 'A company sells two products with independent profits $X$ and $Y$ having $E(X) = 500, \\sigma_X = 50$ and $E(Y) = 800, \\sigma_Y = 80$. If the company forms a combined portfolio $P = 2X + 3Y$, find the probability that total profit exceeds $3200$, assuming $P$ is approximately normally distributed.',
        solution: '<p>$E(P) = 2(500) + 3(800) = 1000 + 2400 = 3400$. [A1]<br>$\\text{Var}(P) = 2^2(50^2) + 3^2(80^2) = 4(2500) + 9(6400) = 10000 + 57600 = 67600$. [M1]<br>$\\sigma_P = \\sqrt{67600} = 260$. [A1]<br>$z$-score for $3200$: $z = \\frac{3200 - 3400}{260} = \\frac{-200}{260} \\approx -0.769$. [M1]<br>$P(P &gt; 3200) = P(Z &gt; -0.769) = \\Phi(0.769) \\approx 0.779$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 4)</h2>
        <div class="formula-card">
          <h4>Syllabus 4.14, 4.15: Expectation &amp; Variance</h4>
          $$E(X) = \\int_{-\\infty}^\\infty x f(x)\\,dx$$
          $$\\text{Var}(X) = \\int_{-\\infty}^\\infty (x - \\mu)^2 f(x)\\,dx = \\int_{-\\infty}^\\infty x^2 f(x)\\,dx - \\mu^2$$
          $$E(aX + b) = aE(X) + b, \\quad \\text{Var}(aX + b) = a^2\\text{Var}(X)$$
          $$\\text{For independent } X, Y: \\quad E(aX + bY) = aE(X) + bE(Y)$$
          $$\\text{Var}(aX \\pm bY) = a^2\\text{Var}(X) + b^2\\text{Var}(Y)$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>Variance Always Adds!</h4>
          $$\\text{Var}(X - Y) = \\text{Var}(X) + \\text{Var}(Y) \\quad (\\text{NEVER } -)$$
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Independence Requirement</h4>
          <p>$\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y)$ ONLY holds if $X$ and $Y$ are independent! Expectation $E(X+Y) = E(X)+E(Y)$ always holds regardless of independence.</p>
        </div>
        <div class="pitfall-card">
          <h4>Squaring the Scale Factor</h4>
          <p>Remember that variance scales with the SQUARE of the coefficient: $\\text{Var}(3X) = 9\\text{Var}(X)$, NOT $3\\text{Var}(X)$.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If $X$ and $Y$ are independent with $\\text{Var}(X) = 5$ and $\\text{Var}(Y) = 3$, what is $\\text{Var}(2X - Y)$?',
        options: [
          '7',
          '17',
          '23',
          '20'
        ],
        correct: 2,
        explanation: '$\\text{Var}(2X - Y) = 2^2\\text{Var}(X) + (-1)^2\\text{Var}(Y) = 4(5) + 1(3) = 20 + 3 = 23$.'
      },
      {
        id: 'q2',
        prompt: 'For $f(x) = 1$ on $[0, 1]$, what is $E(X^2)$?',
        options: [
          '$1/2$',
          '$1/3$',
          '$1/4$',
          '1'
        ],
        correct: 1,
        explanation: '$E(X^2) = \\int_0^1 x^2(1)\\,dx = [x^3/3]_0^1 = 1/3$.'
      },
      {
        id: 'q3',
        prompt: 'Which condition is NOT required for $E(X + Y) = E(X) + E(Y)$?',
        options: [
          'Continuity of distributions',
          'Independence of $X$ and $Y$',
          'Existence of expectations',
          'Identical distributions'
        ],
        correct: 1,
        explanation: 'Expectation is linear by integration properties; independence is NOT required for linearity of expectation.'
      },
      {
        id: 'q4',
        prompt: 'If $E(X) = 4$ and $\\text{Var}(X) = 2$, what is $E(X^2)$?',
        options: [
          '14',
          '16',
          '18',
          '20'
        ],
        correct: 2,
        explanation: '$\\text{Var}(X) = E(X^2) - [E(X)]^2 \\implies 2 = E(X^2) - 16 \\implies E(X^2) = 18$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'The continuous random variable $X$ has PDF $f(x) = \\begin{cases} \\frac{1}{3}(x + 1) & 0 \\le x \\le 1 \\\\ \\frac{1}{3}(3 - x) & 1 &lt; x \\le 2 \\\\ 0 & \\text{otherwise} \\end{cases}$.<br><strong>(a)</strong> By symmetry, state the value of $E(X)$. [1 mark]<br><strong>(b)</strong> Calculate $E(X^2)$. [4 marks]<br><strong>(c)</strong> Hence find $\\text{Var}(X)$. [1 mark]',
        solution: `
          <p><strong>Density check:</strong> Each piece has area $\\frac{1}{3}\\int_0^1(x+1)\\,dx=\\frac12$ (the second piece is its reflection). Total area is $1$, and both pieces are non-negative.</p>
          <p><strong>(a) Mean by symmetry: [1 mark]</strong><br>
          The density is symmetric about $x=1$, so $E(X)=1$ [A1].</p>
          <p><strong>(b) Second moment: [4 marks]</strong><br>
          $E(X^2)=\\frac13\\int_0^1(x^3+x^2)\\,dx+\\frac13\\int_1^2(3x^2-x^3)\\,dx$ [M1].<br>
          First part: $\\frac13[\\frac{x^4}{4}+\\frac{x^3}{3}]_0^1=\\frac7{36}$ [A1].<br>
          Second part: $\\frac13[x^3-\\frac{x^4}{4}]_1^2=\\frac13(4-\\frac34)=\\frac{13}{12}$ [A1].<br>
          $E(X^2)=\\frac7{36}+\\frac{39}{36}=\\frac{23}{18}$ [A1].</p>
          <p><strong>(c) Variance: [1 mark]</strong><br>
          $\\operatorname{Var}(X)=E(X^2)-[E(X)]^2=\\frac{23}{18}-1=\\frac5{18}$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'A courier company handles standard parcels ($X$) and express parcels ($Y$) with independent weights having $E(X) = 2.4$ kg, $\\sigma_X = 0.5$ kg and $E(Y) = 1.8$ kg, $\\sigma_Y = 0.3$ kg.<br>A shipment contains 5 standard parcels and 3 express parcels.<br><strong>(a)</strong> Find the expected total weight of the shipment. [2 marks]<br><strong>(b)</strong> Find the standard deviation of the total weight. [3 marks]<br><strong>(c)</strong> Each standard parcel costs $\\$5$ per kg plus $\\$2$ handling, and each express parcel costs $\\$8$ per kg plus $\\$4$ handling. Find the variance of the total revenue. [2 marks]',
        solution: `
          <p><strong>(a) Expected total weight: [2 marks]</strong><br>
          $E(T) = 5E(X) + 3E(Y) = 5(2.4) + 3(1.8) = 12.0 + 5.4 = 17.4$ kg [A1].</p>
          <p><strong>(b) Standard deviation: [3 marks]</strong><br>
          Since parcels are independent:<br>
          $\\text{Var}(T) = 5\\text{Var}(X) + 3\\text{Var}(Y) = 5(0.5^2) + 3(0.3^2) = 5(0.25) + 3(0.09) = 1.25 + 0.27 = 1.52$ kg$^2$ [M1][A1].<br>
          $\\sigma_T = \\sqrt{1.52} \\approx 1.23$ kg [A1].</p>
          <p><strong>(c) Revenue variance: [2 marks]</strong><br>
          Cost per standard parcel: $C_X = 5X + 2 \\implies \\text{Var}(C_X) = 5^2(0.25) = 6.25$.<br>
          Cost per express parcel: $C_Y = 8Y + 4 \\implies \\text{Var}(C_Y) = 8^2(0.09) = 5.76$.<br>
          Total revenue: $5$ standard + $3$ express:<br>
          $\\text{Var}(\\text{Revenue}) = 5(6.25) + 3(5.76) = 31.25 + 17.28 = 48.53$ [A1].</p>
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
  <link rel="canonical" href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/${guide.folder}/">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${guide.pageTitle}">
  <meta property="og:description" content="${guide.metaDesc}">
  <meta property="og:url" content="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/${guide.folder}/">
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

  <script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/${guide.folder}/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"IB Mathematics","item":"https://sjmaths.com/ib/"},{"@type":"ListItem","position":3,"name":"IB DP Mathematics","item":"https://sjmaths.com/ib/dp-mathematics/"},{"@type":"ListItem","position":4,"name":"AA HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/"},{"@type":"ListItem","position":5,"name":"Stats & Probability HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/"},{"@type":"ListItem","position":6,"name":"${guide.title}","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/${guide.folder}/"}]},{"@type":"Article","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/${guide.folder}/#article","headline":"${guide.title} | IB Math AA HL Guide","description":"${guide.metaDesc}","url":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/${guide.folder}/","dateModified":"2026-10-11","inLanguage":"en","articleSection":"IB DP Mathematics AA HL · Topic ${guide.code}","author":{"@type":"Person","name":"Sandeep Jaiswal","url":"https://sjmaths.com/pages/about.html"},"publisher":{"@type":"Organization","name":"SJMaths","url":"https://sjmaths.com/","logo":{"@type":"ImageObject","url":"https://sjmaths.com/assets/icons/icon-512x512.png"}}}]}</script>
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
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/">Topic 4 HL</a>
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
      <a href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/">Statistics &amp; Probability</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
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
