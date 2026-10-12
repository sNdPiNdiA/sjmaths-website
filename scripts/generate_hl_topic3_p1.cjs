const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'geometry-and-trigonometry');

const guides = [
  // Guide 10: Reciprocal & Inverse Trigonometric Functions
  {
    folder: 'reciprocal-and-inverse-trigonometric-functions',
    code: '3.10',
    title: 'Reciprocal & Inverse Trigonometric Functions',
    pageTitle: 'Reciprocal & Inverse Trigonometric Functions | IB Math AA HL | SJMaths',
    metaDesc: 'Master secant, cosecant, cotangent and inverse trigonometric functions (arcsin, arccos, arctan) for IB DP Mathematics AA HL (Topic 3.10). Restricted domains, principal branches, Pythagorean identities, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL reciprocal trigonometric functions, sec csc cot, inverse trig functions arcsin arccos arctan, principal domains range, 1 + tan^2 = sec^2',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Explore reciprocal circular functions $\\sec x, \\csc x, \\cot x$ and their Pythagorean identities. Master the principal restricted branches, domains, ranges, and asymptotic behaviors of $\\arcsin x, \\arccos x, \\arctan x$.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/functions/composite-transformations-and-reciprocal-graphs/',
      title: 'Composite Transformations & Reciprocal Graphs'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/compound-angle-identities-and-double-angles/',
      title: 'Compound Angle Identities & Double Angles'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-wave-square" style="color:var(--c-primary);"></i> Figure 3.1: Principal Branches of Inverse Trigonometric Functions</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Graphs showing principal branches of arcsin, arccos, and arctan with domains and ranges">
            <!-- Panel 1: y = arcsin(x), Domain [-1, 1], Range [-pi/2, pi/2] -->
            <g transform="translate(25, 20)">
              <rect x="0" y="0" width="215" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="107" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#6366f1">y = arcsin(x)</text>
              <line x1="25" y1="130" x2="190" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="107" y1="35" x2="107" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- S-curve through (-1, -pi/2)->(50, 205), (0, 0)->(107, 130), (1, pi/2)->(165, 55) -->
              <path d="M 50,205 C 80,185 95,150 107,130 C 120,110 135,75 165,55" fill="none" stroke="#6366f1" stroke-width="2.5" />
              <circle cx="50" cy="205" r="4" fill="#6366f1" />
              <circle cx="165" cy="55" r="4" fill="#6366f1" />
              <text x="107" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">D: [-1, 1], R: [-π/2, π/2]</text>
            </g>

            <!-- Panel 2: y = arccos(x), Domain [-1, 1], Range [0, pi] -->
            <g transform="translate(272, 20)">
              <rect x="0" y="0" width="215" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="107" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">y = arccos(x)</text>
              <line x1="25" y1="210" x2="190" y2="210" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="107" y1="35" x2="107" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Curve through (-1, pi)->(50, 50), (0, pi/2)->(107, 130), (1, 0)->(165, 210) -->
              <path d="M 50,50 C 80,70 95,110 107,130 C 120,150 135,190 165,210" fill="none" stroke="#10b981" stroke-width="2.5" />
              <circle cx="50" cy="50" r="4" fill="#10b981" />
              <circle cx="165" cy="210" r="4" fill="#10b981" />
              <text x="107" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">D: [-1, 1], R: [0, π]</text>
            </g>

            <!-- Panel 3: y = arctan(x), Domain R, Range (-pi/2, pi/2) -->
            <g transform="translate(520, 20)">
              <rect x="0" y="0" width="215" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="107" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#f59e0b">y = arctan(x)</text>
              <line x1="25" y1="130" x2="190" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="107" y1="35" x2="107" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Horizontal asymptotes y = pi/2 (y=65) and y = -pi/2 (y=195) -->
              <line x1="25" y1="65" x2="190" y2="65" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="3,3" />
              <line x1="25" y1="195" x2="190" y2="195" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="3,3" />
              <path d="M 30,190 C 70,185 95,150 107,130 C 120,110 145,75 185,70" fill="none" stroke="#f59e0b" stroke-width="2.5" />
              <text x="107" y="240" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">D: ℝ, R: (-π/2, π/2)</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Reciprocal Trigonometric Functions</h2>
        <p>The three reciprocal trigonometric functions are defined as:</p>
        $$\\sec x = \\frac{1}{\\cos x}, \\quad \\csc x = \\frac{1}{\\sin x}, \\quad \\cot x = \\frac{1}{\\tan x} = \\frac{\\cos x}{\\sin x}$$
        <ul class="theory-list">
          <li><strong>Secant ($\\sec x$):</strong> Undefined where $\\cos x = 0$ (vertical asymptotes at $x = \\frac{\\pi}{2} + k\\pi, k \\in \\mathbb{Z}$). Range is $(-\\infty, -1] \\cup [1, \\infty)$. Even function: $\\sec(-x) = \\sec x$. Period $2\\pi$.</li>
          <li><strong>Cosecant ($\\csc x$):</strong> Undefined where $\\sin x = 0$ (vertical asymptotes at $x = k\\pi, k \\in \\mathbb{Z}$). Range is $(-\\infty, -1] \\cup [1, \\infty)$. Odd function: $\\csc(-x) = -\\csc x$. Period $2\\pi$.</li>
          <li><strong>Cotangent ($\\cot x$):</strong> Undefined where $\\sin x = 0$ (vertical asymptotes at $x = k\\pi$). Zeros where $\\cos x = 0$ ($x = \\frac{\\pi}{2} + k\\pi$). Range is all real numbers $\\mathbb{R}$. Odd function: $\\cot(-x) = -\\cot x$. Period $\\pi$.</li>
        </ul>

        <h2>2. Extended Pythagorean Identities</h2>
        <p>Dividing $\\cos^2 x + \\sin^2 x = 1$ by $\\cos^2 x$ and $\\sin^2 x$ produces the fundamental AHL identities:</p>
        $$1 + \\tan^2 x = \\sec^2 x, \\quad 1 + \\cot^2 x = \\csc^2 x$$

        <h2>3. Inverse Trigonometric Functions &amp; Principal Domains</h2>
        <p>Because trigonometric functions are periodic, their domains must be restricted to ensure they are one-to-one (bijective) before defining their inverses:</p>
        <div class="table-responsive" style="margin: 1.5rem 0;">
          <table class="ib-table" style="width:100%; border-collapse:collapse;">
            <thead>
              <tr style="background:var(--c-surface-card); border-bottom:2px solid var(--c-border);">
                <th style="padding:10px; text-align:left;">Function</th>
                <th style="padding:10px; text-align:left;">Domain</th>
                <th style="padding:10px; text-align:left;">Principal Range (Value)</th>
                <th style="padding:10px; text-align:left;">Key Features</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>$y = \\arcsin x$</strong></td>
                <td style="padding:10px;">$[-1, 1]$</td>
                <td style="padding:10px;">$\\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right]$</td>
                <td style="padding:10px;">Odd function: $\\arcsin(-x) = -\\arcsin x$. Vertical tangents at $x = \\pm 1$.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>$y = \\arccos x$</strong></td>
                <td style="padding:10px;">$[-1, 1]$</td>
                <td style="padding:10px;">$[0, \\pi]$</td>
                <td style="padding:10px;">$\\arccos(-x) = \\pi - \\arccos x$. Identity: $\\arcsin x + \\arccos x = \\frac{\\pi}{2}$.</td>
              </tr>
              <tr>
                <td style="padding:10px;"><strong>$y = \\arctan x$</strong></td>
                <td style="padding:10px;">$\\mathbb{R}$ (all real numbers)</td>
                <td style="padding:10px;">$\\left(-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right)$</td>
                <td style="padding:10px;">Odd function. Horizontal asymptotes: $y = \\pm\\frac{\\pi}{2}$ as $x \\to \\pm\\infty$.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Solving Equations Involving Secant and Tangent</h4>
          <p>Solve the equation $2\\sec^2 x - 5\\tan x = 5$ for $0 \\le x \\le 2\\pi$.</p>
          <p><strong>Solution:</strong></p>
          <p>Use the Pythagorean identity $\\sec^2 x = 1 + \\tan^2 x$:</p>
          $$2(1 + \\tan^2 x) - 5\\tan x = 5 \\implies 2 + 2\\tan^2 x - 5\\tan x - 5 = 0$$
          $$2\\tan^2 x - 5\\tan x - 3 = 0$$
          <p>Factorize the quadratic in $\\tan x$:</p>
          $$(2\\tan x + 1)(\\tan x - 3) = 0$$
          <p>• Case 1: $\\tan x = 3$.<br>
          Reference angle $\\alpha = \\arctan(3) \\approx 1.249$ rad.<br>
          In $[0, 2\\pi]$: $x_1 = 1.25$ rad (Quad 1), $x_2 = 1.249 + \\pi \\approx 4.39$ rad (Quad 3).<br>
          • Case 2: $\\tan x = -\\frac{1}{2}$.<br>
          Reference angle $\\beta = \\arctan(0.5) \\approx 0.4636$ rad.<br>
          In $[0, 2\\pi]$: $x_3 = \\pi - 0.4636 \\approx 2.68$ rad (Quad 2), $x_4 = 2\\pi - 0.4636 \\approx 5.82$ rad (Quad 4).<br>
          Solutions (to 3 s.f.): $x \\in \\{1.25, 2.68, 4.39, 5.82\\}$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Exact Value of Composite Inverse Trigonometric Expression</h4>
          <p>Evaluate the exact value of $\\cos\\left(2\\arcsin\\left(-\\frac{3}{5}\\right)\\right)$ without a calculator.</p>
          <p><strong>Solution:</strong></p>
          <p>Let $\\theta = \\arcsin\\left(-\\frac{3}{5}\\right)$.<br>
          By definition of principal branch, $\\theta \\in \\left[-\\frac{\\pi}{2}, 0\\right]$ with $\\sin\\theta = -\\frac{3}{5}$.</p>
          <p>We need $\\cos(2\\theta)$. Using the double angle formula for cosine:</p>
          $$\\cos(2\\theta) = 1 - 2\\sin^2\\theta$$
          $$\\cos(2\\theta) = 1 - 2\\left(-\\frac{3}{5}\\right)^2 = 1 - 2\\left(\\frac{9}{25}\\right) = 1 - \\frac{18}{25} = \\frac{7}{25}$$
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Simplifying Algebraic Inverse Expression</h4>
          <p>Simplify $\\tan(\\arccos x)$ for $0 &lt; x \\le 1$ into an algebraic expression in $x$.</p>
          <p><strong>Solution:</strong></p>
          <p>Let $\\theta = \\arccos x$. Then $\\cos\\theta = x$ and $\\theta \\in \\left[0, \\frac{\\pi}{2}\\right)$.<br>
          Consider a right-angled triangle where the adjacent side is $x$ and the hypotenuse is $1$.<br>
          By Pythagoras, the opposite side is $\\sqrt{1^2 - x^2} = \\sqrt{1 - x^2}$.<br>
          Therefore:</p>
          $$\\tan(\\arccos x) = \\tan\\theta = \\frac{\\text{opposite}}{\\text{adjacent}} = \\frac{\\sqrt{1 - x^2}}{x}$$
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Exact Inverse Angles)',
        text: 'Find the exact value in radians of: (a) $\\arcsin\\left(\\frac{\\sqrt{3}}{2}\\right)$, (b) $\\arccos\\left(-\\frac{1}{2}\\right)$, (c) $\\arctan(-1)$.',
        solution: '<p><strong>(a)</strong> In $[-\\pi/2, \\pi/2]$, $\\sin(\\pi/3) = \\sqrt{3}/2 \\implies \\frac{\\pi}{3}$. [A1]<br><strong>(b)</strong> In $[0, \\pi]$, $\\cos(2\\pi/3) = -1/2 \\implies \\frac{2\\pi}{3}$. [A1]<br><strong>(c)</strong> In $(-\\pi/2, \\pi/2)$, $\\tan(-\\pi/4) = -1 \\implies -\\frac{\\pi}{4}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Reciprocal Identity Application)',
        text: 'Given that $\\tan\\theta = -\\frac{4}{3}$ and $\\frac{\\pi}{2} &lt; \\theta &lt; \\pi$, find the exact values of $\\sec\\theta$, $\\csc\\theta$, and $\\cot\\theta$.',
        solution: '<p>In Quadrant 2: $\\cot\\theta = \\frac{1}{\\tan\\theta} = -\\frac{3}{4}$. [A1]<br>$\\sec^2\\theta = 1 + \\tan^2\\theta = 1 + \\frac{16}{9} = \\frac{25}{9}$. Since $\\theta$ is in Quad 2, $\\sec\\theta &lt; 0 \\implies \\sec\\theta = -\\frac{5}{3}$. [A1]<br>$\\cos\\theta = -\\frac{3}{5} \\implies \\sin\\theta = \\frac{4}{5} \\implies \\csc\\theta = \\frac{5}{4}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Solving Basic Reciprocal Equation)',
        text: 'Solve $\\csc x = 2$ for $0 \\le x \\le 2\\pi$.',
        solution: '<p>$\\csc x = 2 \\implies \\sin x = \\frac{1}{2}$. [M1]<br>In $[0, 2\\pi]$, $x = \\frac{\\pi}{6}$ or $x = \\frac{5\\pi}{6}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Quadratic in Cosecant)',
        text: 'Solve $2\\csc^2 x - 3\\csc x - 2 = 0$ for $0 \\le x \\le 2\\pi$.',
        solution: '<p>Factor: $(2\\csc x + 1)(\\csc x - 2) = 0$. [M1]<br>• $\\csc x = -\\frac{1}{2} \\implies \\sin x = -2$ (no real solution, since $-1 \\le \\sin x \\le 1$). [A1]<br>• $\\csc x = 2 \\implies \\sin x = \\frac{1}{2} \\implies x = \\frac{\\pi}{6}, \\frac{5\\pi}{6}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Composite Trig-Inverse Expression)',
        text: 'Evaluate $\\sin\\left(2\\arccos\\left(\\frac{4}{5}\\right)\\right)$ exactly.',
        solution: '<p>Let $\\theta = \\arccos(4/5)$. Then $\\cos\\theta = 4/5$ and $\\sin\\theta = \\sqrt{1 - 16/25} = 3/5$. [M1]<br>$\\sin(2\\theta) = 2\\sin\\theta\\cos\\theta = 2\\left(\\frac{3}{5}\\right)\\left(\\frac{4}{5}\\right) = \\frac{24}{25}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Proving Identity with Secant and Cosecant)',
        text: 'Prove the identity: $\\sec x + \\csc x = \\frac{\\sin x + \\cos x}{\\sin x \\cos x}$.',
        solution: '<p>LHS $= \\frac{1}{\\cos x} + \\frac{1}{\\sin x}$ [M1]<br>$= \\frac{\\sin x + \\cos x}{\\cos x \\sin x} = \\text{RHS}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Domain and Range of Transformed Arcsin)',
        text: 'Find the domain and range of $g(x) = 3\\arcsin(2x - 1) + \\pi$.',
        solution: '<p>Domain: $-1 \\le 2x - 1 \\le 1$ [M1]<br>$0 \\le 2x \\le 2 \\implies 0 \\le x \\le 1$. Domain is $[0, 1]$. [A1]<br>Range of standard $\\arcsin$ is $[-\\pi/2, \\pi/2]$.<br>Minimum: $3(-\\pi/2) + \\pi = -\\frac{3\\pi}{2} + \\pi = -\\frac{\\pi}{2}$. [M1]<br>Maximum: $3(\\pi/2) + \\pi = \\frac{3\\pi}{2} + \\pi = \\frac{5\\pi}{2}$.<br>Range is $\\left[-\\frac{\\pi}{2}, \\frac{5\\pi}{2}\\right]$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Inverse Trig Equation)',
        text: 'Solve $\\arctan(2x) + \\arctan(x) = \\frac{\\pi}{4}$ for $x &gt; 0$.',
        solution: '<p>Take tangent of both sides: [M1]<br>$\\tan(\\arctan(2x) + \\arctan(x)) = \\tan(\\pi/4) = 1$.<br>Using $\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A\\tan B}$:<br>$\\frac{2x + x}{1 - (2x)(x)} = 1 \\implies \\frac{3x}{1 - 2x^2} = 1$ [M1]<br>$3x = 1 - 2x^2 \\implies 2x^2 + 3x - 1 = 0$. [A1]<br>$x = \\frac{-3 \\pm \\sqrt{9 - 4(2)(-1)}}{4} = \\frac{-3 \\pm \\sqrt{17}}{4}$.<br>Since $x &gt; 0$, $x = \\frac{\\sqrt{17} - 3}{4} \\approx 0.281$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Derivative of Inverse Function via Chain Rule)',
        text: 'Let $y = \\arcsin x$. Use implicit differentiation on $\\sin y = x$ to show that $\\frac{dy}{dx} = \\frac{1}{\\sqrt{1 - x^2}}$ for $-1 &lt; x &lt; 1$.',
        solution: '<p>$\\sin y = x$ for $y \\in [-\\pi/2, \\pi/2]$. [M1]<br>Differentiate with respect to $x$: $\\cos y \\frac{dy}{dx} = 1 \\implies \\frac{dy}{dx} = \\frac{1}{\\cos y}$. [M1]<br>In $[-\\pi/2, \\pi/2]$, $\\cos y \\ge 0$, so $\\cos y = +\\sqrt{1 - \\sin^2 y} = \\sqrt{1 - x^2}$. [M1]<br>Therefore $\\frac{dy}{dx} = \\frac{1}{\\sqrt{1 - x^2}}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Sum of Arcsin and Arccos Identity)',
        text: 'Prove that $\\arcsin x + \\arccos x = \\frac{\\pi}{2}$ for all $x \\in [-1, 1]$.',
        solution: '<p>Let $\\theta = \\arcsin x$. Then $\\sin\\theta = x$ and $\\theta \\in [-\\pi/2, \\pi/2]$. [M1]<br>Notice that $\\cos\\left(\\frac{\\pi}{2} - \\theta\\right) = \\sin\\theta = x$. [M1]<br>Check interval: Since $-\\frac{\\pi}{2} \\le \\theta \\le \\frac{\\pi}{2}$, multiplying by $-1$ and adding $\\frac{\\pi}{2}$ gives $0 \\le \\frac{\\pi}{2} - \\theta \\le \\pi$, which is precisely the principal range of $\\arccos$! [R1]<br>Therefore $\\arccos x = \\frac{\\pi}{2} - \\theta = \\frac{\\pi}{2} - \\arcsin x$.<br>Adding $\\arcsin x$: $\\arcsin x + \\arccos x = \\frac{\\pi}{2}$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 3)</h2>
        <div class="formula-card">
          <h4>Syllabus 3.10: Reciprocal &amp; Inverse Trigonometry</h4>
          <p><strong>Pythagorean Identities:</strong></p>
          $$1 + \\tan^2\\theta = \\sec^2\\theta, \\quad 1 + \\cot^2\\theta = \\csc^2\\theta$$
          <p><strong>Inverse Derivatives:</strong></p>
          $$\\frac{d}{dx}(\\arcsin x) = \\frac{1}{\\sqrt{1-x^2}}, \\quad \\frac{d}{dx}(\\arccos x) = -\\frac{1}{\\sqrt{1-x^2}}, \\quad \\frac{d}{dx}(\\arctan x) = \\frac{1}{1+x^2}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Principal Ranges</h4>
          <ul>
            <li>$\\arcsin x \\in [-\\pi/2, \\pi/2]$</li>
            <li>$\\arccos x \\in [0, \\pi]$</li>
            <li>$\\arctan x \\in (-\\pi/2, \\pi/2)$</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Negative Arguments in Arccos</h4>
          <p>$\\arccos(-x) \\neq -\\arccos(x)$! Because the range is $[0, \\pi]$, $\\arccos(-x) = \\pi - \\arccos(x)$. For example, $\\arccos(-0.5) = \\pi - \\frac{\\pi}{3} = \\frac{2\\pi}{3}$.</p>
        </div>
        <div class="pitfall-card">
          <h4>Reciprocal vs Inverse Notation</h4>
          <p>$\\sin^{-1} x$ is the <strong>inverse function</strong> ($\\arcsin x$), NOT the reciprocal $\\frac{1}{\\sin x}$ (which is $\\csc x$). Never write $(\\sin x)^{-1}$ for $\\arcsin x$!</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'What is the principal value of $\\arccos\\left(-\\frac{\\sqrt{3}}{2}\\right)$?',
        options: [
          '$-\\frac{\\pi}{6}$',
          '$\\frac{5\\pi}{6}$',
          '$\\frac{2\\pi}{3}$',
          '$\\frac{7\\pi}{6}$'
        ],
        correct: 1,
        explanation: '$\\arccos(-x) = \\pi - \\arccos(x) = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}$.'
      },
      {
        id: 'q2',
        prompt: 'Which value is undefined for the function $y = \\sec x$?',
        options: [
          '$x = 0$',
          '$x = \\pi$',
          '$x = \\frac{\\pi}{2}$',
          '$x = 2\\pi$'
        ],
        correct: 2,
        explanation: '$\\sec x = 1/\\cos x$. At $x = \\pi/2$, $\\cos(\\pi/2) = 0$, so $\\sec(\\pi/2)$ is undefined.'
      },
      {
        id: 'q3',
        prompt: 'What is the exact value of $\\cos(\\arctan(\\sqrt{3}))$?',
        options: [
          '$\\frac{1}{2}$',
          '$\\frac{\\sqrt{3}}{2}$',
          '$\\frac{1}{\\sqrt{2}}$',
          '1'
        ],
        correct: 0,
        explanation: '$\\arctan(\\sqrt{3}) = \\frac{\\pi}{3}$. $\\cos\\left(\\frac{\\pi}{3}\\right) = \\frac{1}{2}$.'
      },
      {
        id: 'q4',
        prompt: 'What are the horizontal asymptotes of $y = \\arctan(x)$?',
        options: [
          '$y = \\pm 1$',
          '$y = \\pm \\frac{\\pi}{2}$',
          '$y = \\pm \\pi$',
          '$x = \\pm \\frac{\\pi}{2}$'
        ],
        correct: 1,
        explanation: 'As $x \\to \\pm\\infty$, $\\arctan(x) \\to \\pm\\frac{\\pi}{2}$, so the horizontal asymptotes are $y = \\pm\\frac{\\pi}{2}$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the equation $3\\sec^2 x - 4 = 0$ for $0 \\le x \\le 2\\pi$.<br><strong>(a)</strong> Express the equation in terms of $\\cos x$. [2 marks]<br><strong>(b)</strong> Hence find all solutions in the given interval in terms of $\\pi$. [4 marks]',
        solution: `
          <p><strong>(a) In terms of $\\cos x$: [2 marks]</strong><br>
          $\\sec^2 x = \\frac{4}{3} \\implies \\cos^2 x = \\frac{3}{4}$ [M1]<br>
          $\\cos x = \\pm\\frac{\\sqrt{3}}{2}$ [A1].</p>
          <p><strong>(b) Solutions in $[0, 2\\pi]$: [4 marks]</strong><br>
          Reference angle is $\\frac{\\pi}{6}$ [M1].<br>
          • $\\cos x = \\frac{\\sqrt{3}}{2}$: Quadrants 1 &amp; 4 $\\implies x = \\frac{\\pi}{6}, \\frac{11\\pi}{6}$ [A1].<br>
          • $\\cos x = -\\frac{\\sqrt{3}}{2}$: Quadrants 2 &amp; 3 $\\implies x = \\frac{5\\pi}{6}, \\frac{7\\pi}{6}$ [A1].<br>
          All solutions: $x \\in \\left\\{\\frac{\\pi}{6}, \\frac{5\\pi}{6}, \\frac{7\\pi}{6}, \\frac{11\\pi}{6}\\right\\}$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'Let $f(x) = \\arccos(x^2 - 1)$.<br><strong>(a)</strong> Find the largest possible domain of $f$. [3 marks]<br><strong>(b)</strong> Find the coordinates of the maximum and minimum points on the graph of $f$. [4 marks]',
        solution: `
          <p><strong>(a) Domain: [3 marks]</strong><br>
          The argument of $\\arccos$ must satisfy $-1 \\le x^2 - 1 \\le 1$ [M1].<br>
          Add 1: $0 \\le x^2 \\le 2$ [M1].<br>
          Since $x^2 \\ge 0$ is always true for real $x$, this simplifies to $x^2 \\le 2 \\implies -\\sqrt{2} \\le x \\le \\sqrt{2}$ [A1].<br>
          Domain: $[-\\sqrt{2}, \\sqrt{2}]$.</p>
          <p><strong>(b) Extrema: [4 marks]</strong><br>
          $\\arccos u$ is a strictly decreasing function of $u$ on $[-1, 1]$ [R1].<br>
          • Minimum of $x^2 - 1$ is at $x = 0$, where $u = -1$.<br>
          Since $\\arccos(-1) = \\pi$, the maximum of $f$ occurs at $(0, \\pi)$ [A1].<br>
          • Maximum of $x^2 - 1$ is at $x = \\pm\\sqrt{2}$, where $u = 2 - 1 = 1$.<br>
          Since $\\arccos(1) = 0$, the minimum points are $(\\sqrt{2}, 0)$ and $(-\\sqrt{2}, 0)$ [A1].<br>
          Maximum: $(0, \\pi)$; Minima: $(\\pm\\sqrt{2}, 0)$ [A1].</p>
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
  <link rel="stylesheet" href="/assets/css/ib-page.min.css?v=33705aff">
  <link rel="stylesheet" href="/assets/css/ib-dp-aa-sl-guides.css?v=d12c2f9e">

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
    <a href="/" class="ib-nav-brand"><span aria-hidden="true">∫</span> SJMaths</a>
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
