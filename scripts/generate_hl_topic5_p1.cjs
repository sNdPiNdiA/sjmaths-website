const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'calculus');

const guides = [
  // Guide 17: Limits & L'Hôpital's Rule
  {
    folder: 'limits-and-lhospitals-rule',
    code: '5.12',
    title: 'Advanced Limits & L’Hôpital’s Rule',
    pageTitle: 'Advanced Limits & L’Hôpital’s Rule | IB Math AA HL | SJMaths',
    metaDesc: 'Master L\'Hôpital\'s Rule and indeterminate limits for IB DP Mathematics AA HL (Topic 5.12). 0/0 and inf/inf forms, repeated applications, algebraic transformations, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL Lhopitals rule, indeterminate forms 0/0 and inf/inf, repeated differentiation limits, limit of product 0 x infinity, growth rates hierarchy',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Evaluate indeterminate limits using L’Hôpital’s rule $\\lim \\frac{f(x)}{g(x)} = \\lim \\frac{f\'(x)}{g\'(x)}$ for $\\frac{0}{0}$ and $\\frac{\\infty}{\\infty}$. Transform products $0 \\times \\infty$ and differences $\\infty - \\infty$, and master function growth hierarchies.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/expectation-variance-and-linear-combinations/',
      title: 'Expectation, Variance & Linear Combinations'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/implicit-differentiation-and-related-rates/',
      title: 'Implicit Differentiation & Related Rates'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-infinity" style="color:var(--c-primary);"></i> Figure 5.1: Geometric Intuition of L'Hôpital's Rule at Indeterminate Form $\\frac{0}{0}$</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing curves f(x) and g(x) both vanishing at x=c with their tangent lines dictating the limit ratio f'(c)/g'(c)">
            <!-- Axes at x=100, y=180 -->
            <line x1="80" y1="180" x2="680" y2="180" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="200" y1="30" x2="200" y2="240" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
            <text x="670" y="170" fill="var(--c-text)" font-size="13" font-weight="bold">x</text>
            <text x="210" y="45" fill="var(--c-text)" font-size="13" font-weight="bold">y</text>

            <!-- Vertical dotted line at x = c (x = 380) -->
            <line x1="380" y1="30" x2="380" y2="240" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
            <text x="380" y="260" text-anchor="middle" font-size="13" font-weight="bold" fill="#ef4444">x = c (where f(c) = 0 and g(c) = 0)</text>

            <!-- Curve f(x) passing through (380, 180) with slope m1 = 0.8 -->
            <path d="M 220,240 Q 340,195 380,180 Q 440,150 560,70" fill="none" stroke="#6366f1" stroke-width="3" />
            <text x="570" y="75" font-size="13" font-weight="bold" fill="#6366f1">y = f(x)</text>

            <!-- Tangent to f(x) at x=c -->
            <line x1="260,230" y1="230" x2="500,130" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="3,3" />
            <text x="510" y="130" font-size="11" fill="#6366f1">Slope = f'(c)</text>

            <!-- Curve g(x) passing through (380, 180) with slope m2 = 0.4 -->
            <path d="M 220,215 Q 320,195 380,180 Q 460,160 580,125" fill="none" stroke="#10b981" stroke-width="3" />
            <text x="590" y="130" font-size="13" font-weight="bold" fill="#10b981">y = g(x)</text>

            <!-- Tangent to g(x) at x=c -->
            <line x1="240,215" y1="215" x2="520,145" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3" />
            <text x="530" y="155" font-size="11" fill="#10b981">Slope = g'(c)</text>

            <!-- Common zero point (c, 0) -->
            <circle cx="380" cy="180" r="5" fill="#ef4444" />
            <text x="360" y="195" font-size="12" font-weight="bold" fill="#ef4444">(c, 0)</text>

            <text x="380" y="25" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-text)">lim_{x→c} [f(x)/g(x)] = [f'(c)(x-c)] / [g'(c)(x-c)] = f'(c) / g'(c)</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Indeterminate Forms</h2>
        <p>Direct substitution into a limit $\\lim_{x \\to c} \\frac{f(x)}{g(x)}$ may lead to an undefined indeterminate expression:</p>
        <ul class="theory-list">
          <li><strong>Primary Indeterminate Quotients:</strong> $\\frac{0}{0}$ and $\\frac{\\pm\\infty}{\\pm\\infty}$.</li>
          <li><strong>Indeterminate Products:</strong> $0 \\times \\infty$.</li>
          <li><strong>Indeterminate Differences:</strong> $\\infty - \\infty$.</li>
          <li><em>Warning:</em> $\\frac{0}{\\infty} = 0$, $\\frac{\\infty}{0} = \\pm\\infty$, and $\\frac{k}{0} = \\text{undefined/}\\pm\\infty$ are <strong>determinate</strong> forms. Do NOT use L'Hôpital's rule on determinate forms!</li>
        </ul>

        <h2>2. L'Hôpital's Rule Statement (Syllabus 5.12)</h2>
        <p>Suppose $f$ and $g$ are differentiable near $c$ and $g'(x) \\neq 0$. If:</p>
        $$\\lim_{x \\to c} f(x) = 0 \\quad \\text{and} \\quad \\lim_{x \\to c} g(x) = 0 \\quad \\left(\\frac{0}{0}\\right)$$
        <p>OR</p>
        $$\\lim_{x \\to c} |f(x)| = \\infty \\quad \\text{and} \\quad \\lim_{x \\to c} |g(x)| = \\infty \\quad \\left(\\frac{\\infty}{\\infty}\\right)$$
        <p>Then:</p>
        $$\\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\lim_{x \\to c} \\frac{f'(x)}{g'(x)}$$
        <p>provided the limit on the right exists (or is $\\pm\\infty$).</p>
        <p><strong>Examiner Requirement:</strong> In IB exams, you <strong>must explicitly state</strong> that the form is $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$ before differentiating!</p>

        <h2>3. Transforming Other Indeterminate Forms</h2>
        <ul class="theory-list">
          <li><strong>Product $0 \\times \\infty$:</strong> Rewrite $f(x) g(x)$ as a quotient:
          $$f(x) g(x) = \\frac{f(x)}{1/g(x)} \\quad \\left(\\frac{0}{0}\\right) \\quad \\text{or} \\quad \\frac{g(x)}{1/f(x)} \\quad \\left(\\frac{\\infty}{\\infty}\\right)$$</li>
          <li><strong>Difference $\\infty - \\infty$:</strong> Combine into a single algebraic fraction via a common denominator before evaluating.</li>
        </ul>

        <h2>4. Growth Rates Hierarchy at Infinity</h2>
        <p>As $x \\to \\infty$, functions grow at fundamentally different orders of magnitude:</p>
        $$\\ln x \\ll x^p \\ll a^x \\ll x! \\ll x^x \\quad (p &gt; 0, a &gt; 1)$$
        <p>Consequently: $\\lim_{x \\to \\infty} \\frac{\\ln x}{x^p} = 0$ and $\\lim_{x \\to \\infty} \\frac{x^p}{e^x} = 0$.</p>

        <h2>5. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Basic 0/0 Limit</h4>
          <p>Evaluate $\\lim_{x \\to 0} \\frac{e^{3x} - 1 - 3x}{x^2}$.</p>
          <p><strong>Solution:</strong></p>
          <p>Direct substitution at $x = 0$:</p>
          $$\\text{Numerator: } e^0 - 1 - 0 = 0, \\quad \\text{Denominator: } 0^2 = 0 \\quad \\implies \\text{Indeterminate form } \\frac{0}{0}$$
          <p>Apply L'Hôpital's Rule by differentiating numerator and denominator:</p>
          $$\\lim_{x \\to 0} \\frac{\\frac{d}{dx}(e^{3x} - 1 - 3x)}{\\frac{d}{dx}(x^2)} = \\lim_{x \\to 0} \\frac{3e^{3x} - 3}{2x}$$
          <p>Direct substitution at $x = 0$: $\\frac{3(1) - 3}{0} = \\frac{0}{0}$. Indeterminate again!<br>
          Apply L'Hôpital's Rule a second time:</p>
          $$= \\lim_{x \\to 0} \\frac{\\frac{d}{dx}(3e^{3x} - 3)}{\\frac{d}{dx}(2x)} = \\lim_{x \\to 0} \\frac{9e^{3x}}{2} = \\frac{9(1)}{2} = \\frac{9}{2}$$
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Product Form $0 \\times \\infty$</h4>
          <p>Evaluate $\\lim_{x \\to 0^+} x^2 \\ln x$.</p>
          <p><strong>Solution:</strong></p>
          <p>As $x \\to 0^+$, $x^2 \\to 0$ and $\\ln x \\to -\\infty$, which is an indeterminate product $0 \\times (-\\infty)$.</p>
          <p>Rewrite as a quotient $\\frac{\\infty}{\\infty}$ by moving $x^2$ to the denominator:</p>
          $$\\lim_{x \\to 0^+} \\frac{\\ln x}{x^{-2}}$$
          <p>Form is $\\frac{-\\infty}{\\infty}$. Apply L'Hôpital's Rule:</p>
          $$= \\lim_{x \\to 0^+} \\frac{1/x}{-2x^{-3}} = \\lim_{x \\to 0^+} \\left(-\\frac{1}{2} \\frac{x^3}{x}\\right) = \\lim_{x \\to 0^+} \\left(-\\frac{1}{2} x^2\\right) = -\\frac{1}{2}(0)^2 = 0$$
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Difference Form $\\infty - \\infty$</h4>
          <p>Evaluate $\\lim_{x \\to 0} \\left( \\frac{1}{x} - \\frac{1}{\\sin x} \\right)$.</p>
          <p><strong>Solution:</strong></p>
          <p>Direct substitution gives $\\infty - \\infty$. Combine over a common denominator:</p>
          $$\\lim_{x \\to 0} \\frac{\\sin x - x}{x \\sin x}$$
          <p>At $x = 0$, this is form $\\frac{0}{0}$. Apply L'Hôpital's Rule:</p>
          $$= \\lim_{x \\to 0} \\frac{\\cos x - 1}{\\sin x + x\\cos x}$$
          <p>At $x = 0$, $\\frac{1 - 1}{0 + 0} = \\frac{0}{0}$. Apply L'Hôpital's Rule a second time:</p>
          $$= \\lim_{x \\to 0} \\frac{-\\sin x}{\\cos x + (\\cos x - x\\sin x)} = \\lim_{x \\to 0} \\frac{-\\sin x}{2\\cos x - x\\sin x} = \\frac{0}{2(1) - 0} = \\frac{0}{2} = 0$$
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Standard Trig Limit)',
        text: 'Evaluate $\\lim_{x \\to 0} \\frac{\\sin(5x)}{2x}$ using L\'Hôpital\'s rule.',
        solution: '<p>Direct substitution: $\\frac{\\sin 0}{0} = \\frac{0}{0}$ (indeterminate form). [M1]<br>Apply L\'Hôpital: $\\lim_{x \\to 0} \\frac{5\\cos(5x)}{2} = \\frac{5\\cos(0)}{2} = \\frac{5(1)}{2} = \\frac{5}{2}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Infinity over Infinity)',
        text: 'Evaluate $\\lim_{x \\to \\infty} \\frac{3x^2 + 1}{5x^2 - 4x}$.',
        solution: '<p>Form $\\frac{\\infty}{\\infty}$. [M1]<br>Apply L\'Hôpital: $\\lim_{x \\to \\infty} \\frac{6x}{10x - 4} = \\frac{\\infty}{\\infty}$.<br>Apply L\'Hôpital again: $\\lim_{x \\to \\infty} \\frac{6}{10} = \\frac{3}{5}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Exponential over Linear)',
        text: 'Evaluate $\\lim_{x \\to \\infty} \\frac{e^{2x}}{x}$.',
        solution: '<p>Form $\\frac{\\infty}{\\infty}$. [M1]<br>Apply L\'Hôpital: $\\lim_{x \\to \\infty} \\frac{2e^{2x}}{1} = +\\infty$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Repeated L\'Hôpital with Trig Functions)',
        text: 'Evaluate $\\lim_{x \\to 0} \\frac{1 - \\cos x}{x^2}$.',
        solution: '<p>Form $\\frac{1 - 1}{0} = \\frac{0}{0}$. [M1]<br>First application: $\\lim_{x \\to 0} \\frac{\\sin x}{2x}$ (still $\\frac{0}{0}$).<br>Second application: $\\lim_{x \\to 0} \\frac{\\cos x}{2} = \\frac{1}{2}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Natural Log Limit)',
        text: 'Evaluate $\\lim_{x \\to 1} \\frac{\\ln x}{x^2 - 1}$.',
        solution: '<p>Form $\\frac{\\ln 1}{1 - 1} = \\frac{0}{0}$. [M1]<br>Apply L\'Hôpital: $\\lim_{x \\to 1} \\frac{1/x}{2x} = \\lim_{x \\to 1} \\frac{1}{2x^2} = \\frac{1}{2}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Product Form at Zero)',
        text: 'Evaluate $\\lim_{x \\to 0^+} x \\ln(x)$.',
        solution: '<p>Form $0 \\times (-\\infty)$. Rewrite: $\\lim_{x \\to 0^+} \\frac{\\ln x}{1/x}$ (form $\\frac{-\\infty}{\\infty}$). [M1]<br>Apply L\'Hôpital: $\\lim_{x \\to 0^+} \\frac{1/x}{-1/x^2} = \\lim_{x \\to 0^+} (-x) = 0$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Limit with Inverse Trig)',
        text: 'Evaluate $\\lim_{x \\to 0} \\frac{\\arctan x - x}{x^3}$.',
        solution: '<p>Form $\\frac{0 - 0}{0} = \\frac{0}{0}$. [M1]<br>First application: $\\lim_{x \\to 0} \\frac{\\frac{1}{1+x^2} - 1}{3x^2} = \\lim_{x \\to 0} \\frac{\\frac{1 - (1+x^2)}{1+x^2}}{3x^2} = \\lim_{x \\to 0} \\frac{-x^2}{3x^2(1+x^2)}$. [M1]<br>Cancel $x^2$: $\\lim_{x \\to 0} \\frac{-1}{3(1+x^2)} = -\\frac{1}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Unknown Parameter in Limit)',
        text: 'Given that $\\lim_{x \\to 0} \\frac{\\sin(2x) + a x + b x^3}{x^3} = L$ where $L$ is a finite non-zero constant, find the values of $a$, $b$, and $L$.',
        solution: '<p>At $x = 0$, denominator is 0. For limit to be finite, numerator must be 0: $\\sin 0 + 0 = 0$ (holds).<br>Apply L\'Hôpital: $\\lim_{x \\to 0} \\frac{2\\cos(2x) + a + 3bx^2}{3x^2}$. [M1]<br>At $x = 0$, denominator is 0. So numerator must be 0:<br>$2\\cos(0) + a + 0 = 2 + a = 0 \\implies a = -2$. [A1]<br>Now limit is: $\\lim_{x \\to 0} \\frac{2\\cos(2x) - 2 + 3bx^2}{3x^2}$ (form $\\frac{0}{0}$).<br>Apply L\'Hôpital again: $\\lim_{x \\to 0} \\frac{-4\\sin(2x) + 6bx}{6x} = \\lim_{x \\to 0} \\left(-\\frac{4\\sin(2x)}{6x} + b\\right)$. [M1]<br>Since $\\lim_{x \\to 0} \\frac{\\sin(2x)}{x} = 2$: $-\\frac{4(2)}{6} + b = -\\frac{4}{3} + b$.<br>For any finite non-zero $L$: $L = b - \\frac{4}{3}$. (If evaluated through third L\'Hôpital: $\\frac{-8\\cos(2x) + 6b}{6} = \\frac{-8 + 6b}{6} = b - \\frac{4}{3}$). [A1]<br>$a = -2, L = b - \\frac{4}{3}$.</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Indeterminate Power $1^\\infty$)',
        text: 'Evaluate $\\lim_{x \\to 0} (1 + 3x)^{1/x}$ using natural logarithms.',
        solution: '<p>Let $y = (1 + 3x)^{1/x}$. Then $\\ln y = \\frac{\\ln(1 + 3x)}{x}$. [M1]<br>Evaluate $\\lim_{x \\to 0} \\frac{\\ln(1 + 3x)}{x}$ (form $\\frac{0}{0}$): [M1]<br>Apply L\'Hôpital: $\\lim_{x \\to 0} \\frac{\\frac{3}{1+3x}}{1} = 3$. [A1]<br>Since $\\lim_{x \\to 0} \\ln y = 3$, $\\lim_{x \\to 0} y = e^3$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Difference of Radicals Limit)',
        text: 'Evaluate $\\lim_{x \\to \\infty} \\left( \\sqrt{x^2 + 4x} - x \\right)$.',
        solution: '<p>Form $\\infty - \\infty$. Multiply by conjugate: [M1]<br>$\\lim_{x \\to \\infty} \\frac{(\\sqrt{x^2 + 4x} - x)(\\sqrt{x^2 + 4x} + x)}{\\sqrt{x^2 + 4x} + x} = \\lim_{x \\to \\infty} \\frac{(x^2 + 4x) - x^2}{\\sqrt{x^2 + 4x} + x} = \\lim_{x \\to \\infty} \\frac{4x}{\\sqrt{x^2 + 4x} + x}$. [M1]<br>Divide numerator and denominator by $x$:<br>$= \\lim_{x \\to \\infty} \\frac{4}{\\sqrt{1 + 4/x} + 1} = \\frac{4}{\\sqrt{1 + 0} + 1} = \\frac{4}{2} = 2$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 5)</h2>
        <div class="formula-card">
          <h4>Syllabus 5.12: L’Hôpital’s Rule</h4>
          $$\\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\lim_{x \\to c} \\frac{f\'(x)}{g\'(x)}$$
          <p>Condition: $\\lim_{x \\to c} f(x) = 0$ and $\\lim_{x \\to c} g(x) = 0$, OR $\\lim_{x \\to c} f(x) = \\pm\\infty$ and $\\lim_{x \\to c} g(x) = \\pm\\infty$.</p>
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Converting Product Form $0 \\times \\infty$</h4>
          $$f(x)g(x) = \\frac{f(x)}{1/g(x)} \\quad \\left(\\frac{0}{0}\\right)$$
        </div>
        <div class="formula-card">
          <h4>2. Growth Hierarchy at Infinity</h4>
          $$\\ln x \\ll x^k \\ll e^x \\quad (k &gt; 0)$$
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Never Apply Quotient Rule to L'Hôpital</h4>
          <p>L'Hôpital's rule requires differentiating the numerator and denominator <strong>separately</strong>: $\\frac{f\'(x)}{g\'(x)}$. Do NOT use the quotient rule $\\frac{f\'g - fg\'}{g^2}$!</p>
        </div>
        <div class="pitfall-card">
          <h4>Check the Condition FIRST</h4>
          <p>Always state "Form $\\frac{0}{0}$" or "Form $\\frac{\\infty}{\\infty}$". Applying L'Hôpital to a determinate limit (e.g. $\\frac{1}{0}$ or $\\frac{2}{3}$) will yield completely incorrect answers.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'Which of the following is an indeterminate form where L\'Hôpital\'s rule can be directly applied?',
        options: [
          '$\\frac{0}{\\infty}$',
          '$\\frac{\\infty}{0}$',
          '$\\frac{0}{0}$',
          '$\\frac{1}{0}$'
        ],
        correct: 2,
        explanation: 'L\'Hôpital\'s rule applies directly to indeterminate quotient forms $0/0$ and $\\pm\\infty/\\pm\\infty$.'
      },
      {
        id: 'q2',
        prompt: 'What is $\\lim_{x \\to 0} \\frac{e^x - 1}{x}$?',
        options: [
          '0',
          '1',
          'e',
          '$\\infty$'
        ],
        correct: 1,
        explanation: 'Form $0/0$. Apply L\'Hôpital: $\\lim_{x \\to 0} \\frac{e^x}{1} = e^0 = 1$.'
      },
      {
        id: 'q3',
        prompt: 'What is $\\lim_{x \\to \\infty} \\frac{\\ln(x)}{x^2}$?',
        options: [
          '0',
          '1',
          '$1/2$',
          '$\\infty$'
        ],
        correct: 0,
        explanation: 'Form $\\infty/\\infty$. Apply L\'Hôpital: $\\lim_{x \\to \\infty} \\frac{1/x}{2x} = \\lim_{x \\to \\infty} \\frac{1}{2x^2} = 0$.'
      },
      {
        id: 'q4',
        prompt: 'If direct substitution gives $\\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\frac{2}{0}$, one should:',
        options: [
          'Apply L\'Hôpital\'s rule immediately',
          'Recognize this as a vertical asymptote (determinate $\\pm\\infty$ or undefined)',
          'Multiply by $x$',
          'Take natural logs'
        ],
        correct: 1,
        explanation: '$2/0$ is NOT indeterminate; it indicates a vertical asymptote where the limit does not exist or approaches $\\pm\\infty$. L\'Hôpital does not apply.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the limit $L = \\lim_{x \\to 0} \\frac{\\cos(2x) - 1 + 2x^2}{x^4}$.<br><strong>(a)</strong> State the indeterminate form of the limit at $x = 0$. [1 mark]<br><strong>(b)</strong> By repeated application of L’Hôpital’s rule, find the value of $L$. [5 marks]',
        solution: `
          <p><strong>(a) Indeterminate form: [1 mark]</strong><br>
          At $x = 0$: $\\cos(0) - 1 + 0 = 0$, denominator $0^4 = 0$. Form is $\\frac{0}{0}$ [A1].</p>
          <p><strong>(b) Repeated L'Hôpital: [5 marks]</strong><br>
          1st: $\\lim_{x \\to 0} \\frac{-2\\sin(2x) + 4x}{4x^3}$ (form $\\frac{0}{0}$) [M1].<br>
          2nd: $\\lim_{x \\to 0} \\frac{-4\\cos(2x) + 4}{12x^2}$ (form $\\frac{-4+4}{0} = \\frac{0}{0}$) [M1].<br>
          3rd: $\\lim_{x \\to 0} \\frac{8\\sin(2x)}{24x}$ (form $\\frac{0}{0}$) [M1].<br>
          4th: $\\lim_{x \\to 0} \\frac{16\\cos(2x)}{24} = \\frac{16(1)}{24} = \\frac{2}{3}$ [A1].<br>
          $L = \\frac{2}{3}$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'Let $f(x) = \\frac{x - \\sin x}{x^3}$ for $x \\neq 0$.<br><strong>(a)</strong> Find $\\lim_{x \\to 0} f(x)$. [3 marks]<br><strong>(b)</strong> Hence define $f(0)$ so that $f$ is continuous at $x = 0$. [1 mark]<br><strong>(c)</strong> Find $\\lim_{x \\to \\infty} f(x)$. [3 marks]',
        solution: `
          <p><strong>(a) Limit at 0: [3 marks]</strong><br>
          Form $\\frac{0 - 0}{0} = \\frac{0}{0}$ [M1].<br>
          1st: $\\lim_{x \\to 0} \\frac{1 - \\cos x}{3x^2}$ (form $\\frac{0}{0}$) [M1].<br>
          2nd: $\\lim_{x \\to 0} \\frac{\\sin x}{6x} = \\frac{1}{6}$ [A1].</p>
          <p><strong>(b) Value for continuity: [1 mark]</strong><br>
          $f(0) = \\lim_{x \\to 0} f(x) = \\frac{1}{6}$ [A1].</p>
          <p><strong>(c) Limit at infinity: [3 marks]</strong><br>
          $f(x) = \\frac{x}{x^3} - \\frac{\\sin x}{x^3} = \\frac{1}{x^2} - \\frac{\\sin x}{x^3}$ [M1].<br>
          As $x \\to \\infty$, $\\frac{1}{x^2} \\to 0$.<br>
          Since $-1 \\le \\sin x \\le 1$, $-\\frac{1}{x^3} \\le \\frac{\\sin x}{x^3} \\le \\frac{1}{x^3}$.<br>
          By the squeeze theorem, $\\lim_{x \\to \\infty} \\frac{\\sin x}{x^3} = 0$ [M1].<br>
          Therefore $\\lim_{x \\to \\infty} f(x) = 0 - 0 = 0$ [A1].</p>
        `
      }
    ]
  },

  // Guide 18: Implicit Differentiation & Related Rates
  {
    folder: 'implicit-differentiation-and-related-rates',
    code: '5.10, 5.11',
    title: 'Implicit Differentiation & Related Rates',
    pageTitle: 'Implicit Differentiation & Related Rates | IB Math AA HL | SJMaths',
    metaDesc: 'Master implicit differentiation, tangents to curves, and related rates of change for IB DP Mathematics AA HL (Topics 5.10 & 5.11). Second derivatives d²y/dx², geometric rates of change, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL implicit differentiation, related rates of change, chain rule implicit, tangent and normal implicit curve, second derivative d2y/dx2 implicit',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Differentiate relations where $y$ is defined implicitly $F(x, y) = 0$. Find tangents, normals, and second derivatives $d^2y/dx^2$, and model dynamic physical systems using multivariable related rates of change.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/limits-and-lhospitals-rule/',
      title: 'Advanced Limits & L’Hôpital’s Rule'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/advanced-integration-parts-and-partial-fractions/',
      title: 'Advanced Integration: Parts & Partial Fractions'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-circle-nodes" style="color:var(--c-primary);"></i> Figure 5.2: Implicit Curve Tangent &amp; Conical Related Rates</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing implicit circle curve with tangent on left and conical tank related rates on right">
            <!-- Left: Implicit Circle Curve x^2 + y^2 = 25 -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="330" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary, #4338ca)">Implicit Curve: x² + y² = 25</text>
              <line x1="40" y1="130" x2="290" y2="130" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="165" y1="35" x2="165" y2="220" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <!-- Circle -->
              <circle cx="165" cy="130" r="75" fill="none" stroke="#6366f1" stroke-width="2.5" />
              <!-- Point P(3, 4) at (165 + 45 = 210, 130 - 60 = 70) -->
              <circle cx="210" cy="70" r="5" fill="#ef4444" />
              <text x="220" y="65" font-size="12" font-weight="bold" fill="#ef4444">P(3, 4)</text>
              <!-- Tangent line slope = -3/4 -->
              <line x1="150" y1="25" x2="270" y2="115" stroke="#ef4444" stroke-width="2" />
              <text x="165" y="215" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">2x + 2y(dy/dx) = 0 → dy/dx = -x/y = -3/4</text>
            </g>

            <!-- Right: Conical Tank Related Rates -->
            <g transform="translate(400, 20)">
              <rect x="0" y="0" width="330" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#10b981">Related Rates: Inverted Cone</text>
              <!-- Inverted cone outline -->
              <polygon points="60,60 270,60 165,210" fill="none" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
              <!-- Water level inside -->
              <polygon points="95,110 235,110 165,210" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="2" />
              <!-- Variables r and h -->
              <line x1="165" y1="110" x2="235" y2="110" stroke="#f59e0b" stroke-width="2" />
              <text x="200" y="105" font-size="11" font-weight="bold" fill="#f59e0b">r(t)</text>
              <line x1="165" y1="110" x2="165" y2="210" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3" />
              <text x="145" y="165" font-size="11" font-weight="bold" fill="#10b981">h(t)</text>
              <text x="165" y="215" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">dV/dt = (dV/dh) · (dh/dt)</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Implicit Differentiation Fundamentals</h2>
        <p>When an equation connects $x$ and $y$ implicitly in the form $F(x, y) = 0$ (e.g. $x^3 + y^3 = 3xy$), we differentiate both sides with respect to $x$, treating $y$ as an implicit function of $x$ via the <strong>chain rule</strong>:</p>
        $$\\frac{d}{dx}[y^n] = n y^{n-1} \\frac{dy}{dx}$$
        $$\\frac{d}{dx}[x y] = (1)y + x\\frac{dy}{dx} = y + x\\frac{dy}{dx} \\quad \\text{(Product Rule)}$$
        $$\\frac{d}{dx}[\\sin y] = \\cos y \\frac{dy}{dx}, \\quad \\frac{d}{dx}[e^y] = e^y \\frac{dy}{dx}$$
        <p>After differentiating, collect all terms containing $\\frac{dy}{dx}$ on one side and factor out $\\frac{dy}{dx}$ to isolate it.</p>

        <h2>2. Tangents and Normals to Implicit Curves</h2>
        <p>At a given point $(x_1, y_1)$ on the curve:</p>
        <ul class="theory-list">
          <li><strong>Gradient of Tangent:</strong> $m = \\left.\\frac{dy}{dx}\\right|_{(x_1, y_1)}$.</li>
          <li><strong>Tangent Equation:</strong> $y - y_1 = m(x - x_1)$.</li>
          <li><strong>Normal Equation:</strong> $y - y_1 = -\\frac{1}{m}(x - x_1)$ (where $m \\neq 0$).</li>
          <li><strong>Horizontal Tangent:</strong> Occurs where $\\frac{dy}{dx} = 0$.</li>
          <li><strong>Vertical Tangent:</strong> Occurs where $\\frac{dy}{dx} \\to \\pm\\infty$ (denominator of derivative equals 0).</li>
        </ul>

        <h2>3. Related Rates of Change (Syllabus 5.11)</h2>
        <p>Related rates problems connect the rates of change of multiple related physical quantities with respect to time $t$ using the chain rule:</p>
        $$\\frac{dy}{dt} = \\frac{dy}{dx} \\cdot \\frac{dx}{dt}$$
        <p><strong>Systematic 4-Step Method:</strong></p>
        <ol class="theory-list">
          <li><strong>Identify given rates and required rate:</strong> e.g., given $\\frac{dV}{dt}$, find $\\frac{dh}{dt}$.</li>
          <li><strong>Write a geometric equation relating variables:</strong> e.g. volume of cone $V = \\frac{1}{3}\\pi r^2 h$.</li>
          <li><strong>Eliminate unwanted variables:</strong> Use geometric similarity (e.g., $\\frac{r}{h} = \\frac{R}{H} \\implies r = \\frac{R}{H}h$).</li>
          <li><strong>Differentiate with respect to $t$:</strong> Apply the chain rule $\\frac{dV}{dt} = \\frac{dV}{dh} \\frac{dh}{dt}$, substitute instantaneous values, and solve.</li>
        </ol>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Folium of Descartes Tangent</h4>
          <p>Find the equation of the tangent to the curve $x^3 + y^3 = 6xy$ at the point $(3, 3)$.</p>
          <p><strong>Solution:</strong></p>
          <p>Differentiate implicitly with respect to $x$:</p>
          $$3x^2 + 3y^2 \\frac{dy}{dx} = 6\\left(1 \\cdot y + x\\frac{dy}{dx}\\right) = 6y + 6x\\frac{dy}{dx}$$
          <p>Divide by 3:</p>
          $$x^2 + y^2 \\frac{dy}{dx} = 2y + 2x\\frac{dy}{dx}$$
          $$(y^2 - 2x)\\frac{dy}{dx} = 2y - x^2 \\implies \\frac{dy}{dx} = \\frac{2y - x^2}{y^2 - 2x}$$
          <p>Evaluate at $(3, 3)$:</p>
          $$m = \\left.\\frac{dy}{dx}\\right|_{(3, 3)} = \\frac{2(3) - 3^2}{3^2 - 2(3)} = \\frac{6 - 9}{9 - 6} = \\frac{-3}{3} = -1$$
          <p>Equation of tangent: $y - 3 = -1(x - 3) \\implies y - 3 = -x + 3 \\implies x + y = 6$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Inverted Conical Tank Related Rates</h4>
          <p>Water pours into an inverted conical tank of height 6 m and base radius 2 m at a constant rate of $0.5\\text{ m}^3/\\text{min}$. At what rate is the water level rising when the water is 3 m deep?</p>
          <p><strong>Solution:</strong></p>
          <p>Given: $\\frac{dV}{dt} = 0.5\\text{ m}^3/\\text{min}$. Required: $\\left.\\frac{dh}{dt}\\right|_{h=3}$.<br>
          Volume of cone: $V = \\frac{1}{3}\\pi r^2 h$.<br>
          By similar triangles: $\\frac{r}{h} = \\frac{2}{6} = \\frac{1}{3} \\implies r = \\frac{h}{3}$.<br>
          Substitute $r$ into volume formula:</p>
          $$V = \\frac{1}{3}\\pi \\left(\\frac{h}{3}\\right)^2 h = \\frac{\\pi h^3}{27}$$
          <p>Differentiate with respect to $t$:</p>
          $$\\frac{dV}{dt} = \\frac{3\\pi h^2}{27} \\frac{dh}{dt} = \\frac{\\pi h^2}{9} \\frac{dh}{dt}$$
          <p>Substitute $h = 3$ and $\\frac{dV}{dt} = 0.5$:</p>
          $$0.5 = \\frac{\\pi (3^2)}{9} \\frac{dh}{dt} = \\frac{9\\pi}{9} \\frac{dh}{dt} = \\pi \\frac{dh}{dt}$$
          $$\\frac{dh}{dt} = \\frac{0.5}{\\pi} = \\frac{1}{2\\pi} \\approx 0.159\\text{ m/min}$$
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Sliding Ladder Problem</h4>
          <p>A ladder of length 5 m leans against a vertical wall. The base of the ladder slides away from the wall at $0.8\\text{ m/s}$. How fast is the top of the ladder sliding down the wall when the base is 3 m from the wall?</p>
          <p><strong>Solution:</strong></p>
          <p>Let $x$ be the distance from wall to base, and $y$ be the height of the ladder on the wall.<br>
          By Pythagoras: $x^2 + y^2 = 5^2 = 25$.<br>
          Given: $\\frac{dx}{dt} = 0.8\\text{ m/s}$. When $x = 3$, $y = \\sqrt{25 - 9} = 4\\text{ m}$.<br>
          Differentiate with respect to $t$:</p>
          $$2x\\frac{dx}{dt} + 2y\\frac{dy}{dt} = 0 \\implies x\\frac{dx}{dt} + y\\frac{dy}{dt} = 0$$
          $$3(0.8) + 4\\frac{dy}{dt} = 0 \\implies 2.4 + 4\\frac{dy}{dt} = 0 \\implies \\frac{dy}{dt} = -\\frac{2.4}{4} = -0.6\\text{ m/s}$$
          <p>The top of the ladder is sliding down at a speed of $0.6\\text{ m/s}$.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Basic Implicit Derivative)',
        text: 'Find $\\frac{dy}{dx}$ for the circle $x^2 + y^2 = 100$ at the point $(6, 8)$.',
        solution: '<p>$2x + 2y\\frac{dy}{dx} = 0 \\implies \\frac{dy}{dx} = -\\frac{x}{y}$. [M1]<br>At $(6, 8)$: $\\frac{dy}{dx} = -\\frac{6}{8} = -\\frac{3}{4}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Product Term Differentiation)',
        text: 'Find $\\frac{dy}{dx}$ in terms of $x$ and $y$ for $x^2 y + y^3 = 5$.',
        solution: '<p>$\\frac{d}{dx}(x^2 y) = 2xy + x^2\\frac{dy}{dx}$. [M1]<br>$2xy + x^2\\frac{dy}{dx} + 3y^2\\frac{dy}{dx} = 0$<br>$(x^2 + 3y^2)\\frac{dy}{dx} = -2xy \\implies \\frac{dy}{dx} = -\\frac{2xy}{x^2 + 3y^2}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Expanding Circle Rate of Change)',
        text: 'The radius of a circle increases at $3\\text{ cm/s}$. Find the rate of increase of its area when $r = 10\\text{ cm}$.',
        solution: '<p>$A = \\pi r^2 \\implies \\frac{dA}{dt} = 2\\pi r \\frac{dr}{dt}$. [M1]<br>$\\frac{dA}{dt} = 2\\pi(10)(3) = 60\\pi \\approx 188.5\\text{ cm}^2/\\text{s}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Tangent and Normal to Ellipse)',
        text: 'Find the equations of the tangent and normal to the ellipse $x^2 + 4y^2 = 8$ at the point $(2, 1)$.',
        solution: '<p>$2x + 8y\\frac{dy}{dx} = 0 \\implies \\frac{dy}{dx} = -\\frac{2x}{8y} = -\\frac{x}{4y}$. [M1]<br>At $(2, 1)$: $m = -\\frac{2}{4(1)} = -\\frac{1}{2}$. [A1]<br>Tangent: $y - 1 = -\\frac{1}{2}(x - 2) \\implies x + 2y = 4$. [A1]<br>Normal: gradient $= 2 \\implies y - 1 = 2(x - 2) \\implies y = 2x - 3$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Expanding Spherical Balloon)',
        text: 'A spherical balloon is inflated such that its volume increases at $100\\text{ cm}^3/\\text{s}$. Find the rate at which its surface area is increasing when the radius is $5\\text{ cm}$.',
        solution: '<p>$V = \\frac{4}{3}\\pi r^3 \\implies \\frac{dV}{dt} = 4\\pi r^2 \\frac{dr}{dt}$. [M1]<br>$100 = 4\\pi (25) \\frac{dr}{dt} = 100\\pi \\frac{dr}{dt} \\implies \\frac{dr}{dt} = \\frac{1}{\\pi}\\text{ cm/s}$. [A1]<br>Surface area $S = 4\\pi r^2 \\implies \\frac{dS}{dt} = 8\\pi r \\frac{dr}{dt}$. [M1]<br>$\\frac{dS}{dt} = 8\\pi(5)\\left(\\frac{1}{\\pi}\\right) = 40\\text{ cm}^2/\\text{s}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Second Derivative Implicitly)',
        text: 'Find $\\frac{d^2y}{dx^2}$ in terms of $y$ for the curve $x^2 - y^2 = 4$.',
        solution: '<p>$2x - 2y\\frac{dy}{dx} = 0 \\implies \\frac{dy}{dx} = \\frac{x}{y}$. [M1]<br>Differentiate again using quotient rule: [M1]<br>$\\frac{d^2y}{dx^2} = \\frac{1(y) - x\\frac{dy}{dx}}{y^2} = \\frac{y - x(x/y)}{y^2} = \\frac{y^2 - x^2}{y^3}$. [M1]<br>Since $x^2 - y^2 = 4 \\implies y^2 - x^2 = -4$:<br>$\\frac{d^2y}{dx^2} = -\\frac{4}{y^3}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Horizontal and Vertical Tangents)',
        text: 'Find all points on the curve $x^2 + xy + y^2 = 27$ where the tangent is horizontal.',
        solution: '<p>$2x + \\left(y + x\\frac{dy}{dx}\\right) + 2y\\frac{dy}{dx} = 0 \\implies (x + 2y)\\frac{dy}{dx} = -(2x + y)$. [M1]<br>$\\frac{dy}{dx} = -\\frac{2x + y}{x + 2y}$.<br>Horizontal tangent requires $\\frac{dy}{dx} = 0 \\implies 2x + y = 0 \\implies y = -2x$. [A1]<br>Substitute into curve equation: [M1]<br>$x^2 + x(-2x) + (-2x)^2 = 27 \\implies x^2 - 2x^2 + 4x^2 = 27 \\implies 3x^2 = 27 \\implies x^2 = 9 \\implies x = \\pm 3$.<br>• $x = 3 \\implies y = -6$. Point: $(3, -6)$. [A1]<br>• $x = -3 \\implies y = 6$. Point: $(-3, 6)$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Walking Away from Streetlight Shadow Rate)',
        text: 'A person 1.8 m tall walks away from a 6 m tall streetlight at $1.5\\text{ m/s}$. Find: (a) the rate at which the length of the person\'s shadow is growing, (b) the speed of the tip of the shadow.',
        solution: '<p>Let $x$ be the distance from streetlight to person, $s$ be shadow length. [M1]<br>By similar triangles: $\\frac{s}{1.8} = \\frac{x + s}{6} \\implies 6s = 1.8x + 1.8s \\implies 4.2s = 1.8x \\implies s = \\frac{1.8}{4.2}x = \\frac{3}{7}x$. [A1]<br><strong>(a) Shadow length growth:</strong> $\\frac{ds}{dt} = \\frac{3}{7}\\frac{dx}{dt} = \\frac{3}{7}(1.5) = \\frac{4.5}{7} = \\frac{9}{14} \\approx 0.643\\text{ m/s}$. [A1]<br><strong>(b) Speed of tip of shadow:</strong> Tip position $= x + s = x + \\frac{3}{7}x = \\frac{10}{7}x$.<br>Speed $= \\frac{10}{7}\\frac{dx}{dt} = \\frac{10}{7}(1.5) = \\frac{15}{7} \\approx 2.14\\text{ m/s}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Exponential-Trig Implicit Curve)',
        text: 'Find the gradient of the tangent to $e^y \\sin x = x + y$ at the origin $(0, 0)$.',
        solution: '<p>Differentiate implicitly: [M1]<br>$\\frac{d}{dx}[e^y \\sin x] = e^y \\frac{dy}{dx} \\sin x + e^y \\cos x$.<br>$\\frac{d}{dx}[x + y] = 1 + \\frac{dy}{dx}$.<br>Equation: $e^y \\sin x \\frac{dy}{dx} + e^y \\cos x = 1 + \\frac{dy}{dx}$. [A1]<br>Substitute $(x, y) = (0, 0)$: [M1]<br>$e^0 \\sin(0) \\frac{dy}{dx} + e^0 \\cos(0) = 1 + \\frac{dy}{dx}$<br>$0 + 1(1) = 1 + \\frac{dy}{dx} \\implies 1 = 1 + \\frac{dy}{dx} \\implies \\frac{dy}{dx} = 0$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Trough Water Rate Problem)',
        text: 'A water trough of length 4 m has an equilateral triangular cross-section with sides 2 m pointing downwards. Water is pumped in at $0.2\\text{ m}^3/\\text{min}$. Find the rate of rise of the water level when the depth is 1 m.',
        solution: '<p>Cross section is an equilateral triangle of side 2. Height $H = 2\\sin(60^\\circ) = \\sqrt{3}$. Base $B = 2$. [M1]<br>At depth $h$, water surface width $b$: $\\frac{b}{h} = \\frac{2}{\\sqrt{3}} \\implies b = \\frac{2}{\\sqrt{3}}h$. [M1]<br>Cross-sectional area: $A = \\frac{1}{2} b h = \\frac{1}{2}\\left(\\frac{2}{\\sqrt{3}}h\\right)h = \\frac{h^2}{\\sqrt{3}}$.<br>Total volume $V = \\text{Area} \\times \\text{length} = 4\\left(\\frac{h^2}{\\sqrt{3}}\\right) = \\frac{4}{\\sqrt{3}}h^2$. [A1]<br>$\\frac{dV}{dt} = \\frac{8}{\\sqrt{3}}h \\frac{dh}{dt}$. [M1]<br>When $h = 1$ and $\\frac{dV}{dt} = 0.2$:<br>$0.2 = \\frac{8}{\\sqrt{3}}(1) \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{0.2\\sqrt{3}}{8} = \\frac{\\sqrt{3}}{40} \\approx 0.0433\\text{ m/min}$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 5)</h2>
        <div class="formula-card">
          <h4>Syllabus 5.10, 5.11: Implicit Differentiation &amp; Chain Rule</h4>
          $$\\frac{dy}{dx} = \\frac{dy}{du} \\frac{du}{dx}$$
          $$\\text{Product Rule: } \\frac{d}{dx}(uv) = u\\frac{dv}{dx} + v\\frac{du}{dx}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Standard Implicit Derivative Patterns</h4>
          $$\\frac{d}{dx}[y^n] = n y^{n-1} \\frac{dy}{dx}, \\quad \\frac{d}{dx}[xy] = y + x\\frac{dy}{dx}$$
        </div>
        <div class="formula-card">
          <h4>2. Related Rates Template</h4>
          $$\\frac{dy}{dt} = \\frac{dy}{dx} \\cdot \\frac{dx}{dt}$$
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Forgetting $\\frac{dy}{dx}$ on $y$-terms</h4>
          <p>Every time you differentiate a term with $y$ with respect to $x$, you MUST multiply by $\\frac{dy}{dx}$. Writing $\\frac{d}{dx}(y^2) = 2y$ instead of $2y\\frac{dy}{dx}$ is the most common error in HL calculus.</p>
        </div>
        <div class="pitfall-card">
          <h4>Substituting Numbers TOO EARLY in Related Rates</h4>
          <p>Never substitute the numerical snapshot (e.g. $h = 3$) BEFORE differentiating! If you substitute early, the quantity becomes a constant and its derivative erroneously vanishes to zero.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'What is $\\frac{d}{dx}(x^2 y)$?',
        options: [
          '$2x y$',
          '$x^2 \\frac{dy}{dx}$',
          '$2x y + x^2 \\frac{dy}{dx}$',
          '$2x \\frac{dy}{dx}$'
        ],
        correct: 2,
        explanation: 'By the product rule: $\\frac{d}{dx}(x^2) \\cdot y + x^2 \\cdot \\frac{d}{dx}(y) = 2xy + x^2 \\frac{dy}{dx}$.'
      },
      {
        id: 'q2',
        prompt: 'At what points does the circle $x^2 + y^2 = 25$ have vertical tangents?',
        options: [
          '$(0, \\pm 5)$',
          '$(\\pm 5, 0)$',
          '$(3, 4)$',
          '$(-3, -4)$'
        ],
        correct: 1,
        explanation: '$\\frac{dy}{dx} = -\\frac{x}{y}$. Vertical tangents occur where the denominator $y = 0 \\implies x^2 = 25 \\implies x = \\pm 5$. Points are $(\\pm 5, 0)$.'
      },
      {
        id: 'q3',
        prompt: 'If $V = x^3$ and $\\frac{dx}{dt} = 2$, what is $\\frac{dV}{dt}$ when $x = 4$?',
        options: [
          '24',
          '48',
          '96',
          '128'
        ],
        correct: 2,
        explanation: '$\\frac{dV}{dt} = 3x^2 \\frac{dx}{dt} = 3(4^2)(2) = 3(16)(2) = 96$.'
      },
      {
        id: 'q4',
        prompt: 'The tangent to an implicit curve is horizontal if and only if:',
        options: [
          '$\\frac{dy}{dx} = 0$',
          '$\\frac{dy}{dx}$ is undefined',
          '$\\frac{d^2y}{dx^2} = 0$',
          '$y = 0$'
        ],
        correct: 0,
        explanation: 'A horizontal tangent line has slope zero, which requires $\\frac{dy}{dx} = 0$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'A curve is defined implicitly by $x^2 + 2xy + 3y^2 = 11$.<br><strong>(a)</strong> Show that $\\frac{dy}{dx} = -\\frac{x + y}{x + 3y}$. [3 marks]<br><strong>(b)</strong> Find the coordinates of the two points on the curve where the tangent is parallel to the $x$-axis. [3 marks]',
        solution: `
          <p><strong>(a) Implicit differentiation: [3 marks]</strong><br>
          $2x + 2\\left(y + x\\frac{dy}{dx}\\right) + 6y\\frac{dy}{dx} = 0$ [M1]<br>
          $2x + 2y + (2x + 6y)\\frac{dy}{dx} = 0$<br>
          Divide by 2: $(x + 3y)\\frac{dy}{dx} = -(x + y) \\implies \\frac{dy}{dx} = -\\frac{x + y}{x + 3y}$ [A1].</p>
          <p><strong>(b) Horizontal tangents: [3 marks]</strong><br>
          Parallel to $x$-axis $\\implies \\frac{dy}{dx} = 0 \\implies x + y = 0 \\implies y = -x$ [M1].<br>
          Substitute into curve equation:<br>
          $x^2 + 2x(-x) + 3(-x)^2 = 11 \\implies x^2 - 2x^2 + 3x^2 = 11 \\implies 2x^2 = 11 \\implies x = \\pm\\sqrt{\\frac{11}{2}}$ [A1].<br>
          Points: $\\left(\\sqrt{5.5}, -\\sqrt{5.5}\\right)$ and $\\left(-\\sqrt{5.5}, \\sqrt{5.5}\\right)$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'A sand timer consists of sand falling from an upper container onto a conical pile. The height of the cone is always equal to its base radius ($h = r$). Sand falls at a rate of $12\\text{ cm}^3/\\text{s}$.<br><strong>(a)</strong> Express the volume $V$ in terms of $h$ only. [1 mark]<br><strong>(b)</strong> Find the rate at which the height of the sand pile is increasing when $h = 6\\text{ cm}$. [3 marks]<br><strong>(c)</strong> Find the rate at which the base area of the cone is increasing at this instant. [4 marks]',
        solution: `
          <p><strong>(a) Volume formula: [1 mark]</strong><br>
          $V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi h^3$ [A1].</p>
          <p><strong>(b) Rate of height increase: [3 marks]</strong><br>
          $\\frac{dV}{dt} = \\pi h^2 \\frac{dh}{dt}$ [M1].<br>
          Substitute $h = 6$ and $\\frac{dV}{dt} = 12$:<br>
          $12 = \\pi (36) \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{12}{36\\pi} = \\frac{1}{3\\pi} \\approx 0.106\\text{ cm/s}$ [A1].</p>
          <p><strong>(c) Rate of base area increase: [4 marks]</strong><br>
          Base area $A = \\pi r^2 = \\pi h^2$ [M1].<br>
          $\\frac{dA}{dt} = 2\\pi h \\frac{dh}{dt}$ [M1].<br>
          Substitute $h = 6$ and $\\frac{dh}{dt} = \\frac{1}{3\\pi}$:<br>
          $\\frac{dA}{dt} = 2\\pi(6)\\left(\\frac{1}{3\\pi}\\right) = 12\\pi \\left(\\frac{1}{3\\pi}\\right) = 4\\text{ cm}^2/\\text{s}$ [A1].</p>
        `
      }
    ]
  },

  // Guide 19: Advanced Integration: Parts & Partial Fractions
  {
    folder: 'advanced-integration-parts-and-partial-fractions',
    code: '5.13',
    title: 'Advanced Integration: Parts & Partial Fractions',
    pageTitle: 'Advanced Integration: Parts & Partial Fractions | IB Math AA HL | SJMaths',
    metaDesc: 'Master integration by parts and integration using partial fractions for IB DP Mathematics AA HL (Topic 5.13). LIATE rule, repeated parts, cyclic loops, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL integration by parts, LIATE rule, repeated integration by parts, partial fractions integration, cyclic integral e^x sin x, arctan integration',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Expand your integration repertoire. Master integration by parts $\\int u\\,dv = uv - \\int v\\,du$ using the LIATE hierarchy, conquer cyclic looping integrals, and integrate rational expressions via partial fraction decompositions.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/implicit-differentiation-and-related-rates/',
      title: 'Implicit Differentiation & Related Rates'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/first-order-differential-equations/',
      title: 'First-Order Differential Equations'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-puzzle-piece" style="color:var(--c-primary);"></i> Figure 5.3: Geometric Representation of Integration by Parts: $uv = \\int u\\,dv + \\int v\\,du$</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing u-v rectangle partitioned into two integral areas ∫ u dv and ∫ v du">
            <!-- Axes at (180, 220) -->
            <line x1="120" y1="220" x2="620" y2="220" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="180" y1="30" x2="180" y2="250" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="610" y="210" fill="var(--c-text)" font-size="13" font-weight="bold">u</text>
            <text x="190" y="45" fill="var(--c-text)" font-size="13" font-weight="bold">v</text>

            <!-- Outer Rectangle with corners (180, 220), (520, 220), (520, 70), (180, 70) -->
            <!-- Total area = u · v -->
            <!-- Curve dividing the rectangle from (180, 220) to (520, 70) -->
            <path d="M 220,200 Q 340,180 500,80" fill="none" stroke="#6366f1" stroke-width="3" />

            <!-- Shaded Area 1: ∫ u dv (horizontal strips to v-axis) -->
            <path d="M 180,200 L 220,200 Q 340,180 500,80 L 180,80 Z" fill="rgba(99,102,241,0.2)" />
            <text x="310" y="130" font-size="14" font-weight="bold" fill="#6366f1">Area = ∫ u dv</text>

            <!-- Shaded Area 2: ∫ v du (vertical strips to u-axis) -->
            <path d="M 220,200 Q 340,180 500,80 L 500,220 L 220,220 Z" fill="rgba(16,185,129,0.2)" />
            <text x="380" y="195" font-size="14" font-weight="bold" fill="#10b981">Area = ∫ v du</text>

            <!-- Total Rectangle Dimension Labels -->
            <line x1="500" y1="70" x2="500" y2="220" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />
            <text x="500" y="240" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">u₁</text>
            <line x1="180" y1="80" x2="500" y2="80" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3" />
            <text x="160" y="85" font-size="12" font-weight="bold" fill="#ef4444">v₁</text>

            <text x="380" y="265" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-text)">Total Rectangle Area u·v = ∫ u dv + ∫ v du  ⟹  ∫ u dv = uv - ∫ v du</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Integration by Parts Formula</h2>
        <p>Integration by parts is derived from the product rule of differentiation:</p>
        $$\\frac{d}{dx}[uv] = u\\frac{dv}{dx} + v\\frac{du}{dx} \\implies u\\frac{dv}{dx} = \\frac{d}{dx}[uv] - v\\frac{du}{dx}$$
        <p>Integrating both sides gives the fundamental formula:</p>
        $$\\int u \\frac{dv}{dx}\\,dx = uv - \\int v \\frac{du}{dx}\\,dx \\quad \\iff \\quad \\int u\\,dv = uv - \\int v\\,du$$
        <p>For definite integrals with limits $a$ to $b$:</p>
        $$\\int_a^b u\\,dv = [uv]_a^b - \\int_a^b v\\,du$$

        <h2>2. Choosing $u$ with the LIATE Rule</h2>
        <p>Select $u$ to be the function that appears <strong>first</strong> in the LIATE acronym:</p>
        <ol class="theory-list">
          <li><strong>L:</strong> <strong>L</strong>ogarithmic functions ($\\ln x, \\log_a x$)</li>
          <li><strong>I:</strong> <strong>I</strong>nverse trigonometric functions ($\\arcsin x, \\arctan x$)</li>
          <li><strong>A:</strong> <strong>A</strong>lgebraic / polynomial functions ($x^n, x^2 + 1$)</li>
          <li><strong>T:</strong> <strong>T</strong>rigonometric functions ($\\sin x, \\cos x$)</li>
          <li><strong>E:</strong> <strong>E</strong>xponential functions ($e^x, 2^x$)</li>
        </ol>

        <h2>3. Special Integration by Parts Techniques</h2>
        <ul class="theory-list">
          <li><strong>Integrating $\\ln x$ or $\\arctan x$ alone:</strong> Write as $\\int 1 \\cdot \\ln x\\,dx$, letting $u = \\ln x$ and $dv = 1\\,dx$.</li>
          <li><strong>Repeated Integration by Parts:</strong> For $\\int x^2 e^x\\,dx$ or $\\int x^2 \\cos x\\,dx$, apply parts twice to reduce the power of $x$ until a standard integral is reached.</li>
          <li><strong>Cyclic (Looping) Integrals:</strong> For $\\int e^{ax}\\sin(bx)\\,dx$, applying parts twice reproduces the original integral $I$. Solve for $I$ algebraically:
          $$I = (\\dots) - k I \\implies (1 + k)I = (\\dots) \\implies I = \\frac{\\dots}{1 + k}$$</li>
        </ul>

        <h2>4. Integration via Partial Fractions</h2>
        <p>Decomposing rational functions simplifies them into standard integrals:</p>
        $$\\int \\frac{1}{ax + b}\\,dx = \\frac{1}{a}\\ln|ax + b| + C$$
        $$\\int \\frac{1}{(ax + b)^2}\\,dx = -\\frac{1}{a(ax + b)} + C$$
        $$\\int \\frac{1}{x^2 + a^2}\\,dx = \\frac{1}{a}\\arctan\\left(\\frac{x}{a}\\right) + C$$

        <h2>5. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Repeated Integration by Parts</h4>
          <p>Evaluate $\\int x^2 e^x\\,dx$.</p>
          <p><strong>Solution:</strong></p>
          <p>By LIATE, choose $u = x^2$ (Algebraic) and $dv = e^x\\,dx$ (Exponential):</p>
          $$du = 2x\\,dx, \\quad v = e^x$$
          $$\\int x^2 e^x\\,dx = x^2 e^x - \\int 2x e^x\\,dx = x^2 e^x - 2\\int x e^x\\,dx$$
          <p>Apply parts a second time to $\\int x e^x\\,dx$ with $u_1 = x, dv_1 = e^x\\,dx$ ($du_1 = dx, v_1 = e^x$):</p>
          $$\\int x e^x\\,dx = x e^x - \\int e^x\\,dx = x e^x - e^x$$
          <p>Substitute back:</p>
          $$\\int x^2 e^x\\,dx = x^2 e^x - 2(x e^x - e^x) + C = (x^2 - 2x + 2)e^x + C$$
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Cyclic Looping Integral</h4>
          <p>Evaluate $I = \\int e^x \\cos x\\,dx$.</p>
          <p><strong>Solution:</strong></p>
          <p>Let $u = \\cos x, dv = e^x\\,dx \\implies du = -\\sin x\\,dx, v = e^x$:</p>
          $$I = e^x \\cos x - \\int e^x(-\\sin x)\\,dx = e^x \\cos x + \\int e^x \\sin x\\,dx$$
          <p>Apply parts again to $\\int e^x \\sin x\\,dx$ with $u = \\sin x, dv = e^x\\,dx \\implies du = \\cos x\\,dx, v = e^x$:</p>
          $$\\int e^x \\sin x\\,dx = e^x \\sin x - \\int e^x \\cos x\\,dx = e^x \\sin x - I$$
          <p>Substitute back into the expression for $I$:</p>
          $$I = e^x \\cos x + e^x \\sin x - I$$
          $$2I = e^x(\\cos x + \\sin x) \\implies I = \\frac{e^x(\\cos x + \\sin x)}{2} + C$$
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Integration by Partial Fractions</h4>
          <p>Evaluate $\\int_2^3 \\frac{5x - 3}{(x - 1)(x + 1)}\\,dx$.</p>
          <p><strong>Solution:</strong></p>
          <p>Partial fraction decomposition: $\\frac{5x - 3}{(x - 1)(x + 1)} = \\frac{A}{x - 1} + \\frac{B}{x + 1}$.<br>
          $5x - 3 = A(x + 1) + B(x - 1)$.<br>
          • $x = 1$: $2 = 2A \\implies A = 1$.<br>
          • $x = -1$: $-8 = -2B \\implies B = 4$.</p>
          $$\\int_2^3 \\left( \\frac{1}{x - 1} + \\frac{4}{x + 1} \\right)\\,dx = \\left[ \\ln|x - 1| + 4\\ln|x + 1| \\right]_2^3$$
          $$= [ \\ln(2) + 4\\ln(4) ] - [ \\ln(1) + 4\\ln(3) ] = \\ln(2) + 4\\ln(2^2) - 0 - 4\\ln(3)$$
          $$= \\ln(2) + 8\\ln(2) - 4\\ln(3) = 9\\ln(2) - 4\\ln(3) = \\ln\\left(\\frac{2^9}{3^4}\\right) = \\ln\\left(\\frac{512}{81}\\right) \\approx 1.844$$
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Standard Integration by Parts)',
        text: 'Evaluate $\\int x \\sin x\\,dx$.',
        solution: '<p>LIATE: $u = x \\implies du = dx$; $dv = \\sin x\\,dx \\implies v = -\\cos x$. [M1]<br>$\\int x \\sin x\\,dx = -x\\cos x - \\int (-\\cos x)\\,dx = -x\\cos x + \\sin x + C$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Integrating Natural Log)',
        text: 'Evaluate $\\int \\ln x\\,dx$.',
        solution: '<p>Write as $\\int 1 \\cdot \\ln x\\,dx$. $u = \\ln x \\implies du = \\frac{1}{x}dx$; $dv = 1\\,dx \\implies v = x$. [M1]<br>$\\int \\ln x\\,dx = x\\ln x - \\int x\\left(\\frac{1}{x}\\right)dx = x\\ln x - \\int 1\\,dx = x\\ln x - x + C$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Linear Partial Fraction Integral)',
        text: 'Evaluate $\\int \\frac{3}{2x + 5}\\,dx$.',
        solution: '<p>$\\frac{3}{2}\\int \\frac{2}{2x + 5}\\,dx = \\frac{3}{2}\\ln|2x + 5| + C$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Definite Integral by Parts)',
        text: 'Evaluate $\\int_0^1 x e^{2x}\\,dx$.',
        solution: '<p>$u = x, dv = e^{2x}dx \\implies du = dx, v = \\frac{1}{2}e^{2x}$. [M1]<br>$= \\left[\\frac{1}{2}x e^{2x}\\right]_0^1 - \\int_0^1 \\frac{1}{2}e^{2x}\\,dx = \\frac{1}{2}e^2 - \\left[\\frac{1}{4}e^{2x}\\right]_0^1$ [M1]<br>$= \\frac{1}{2}e^2 - \\left(\\frac{1}{4}e^2 - \\frac{1}{4}\\right) = \\frac{1}{4}e^2 + \\frac{1}{4} = \\frac{e^2 + 1}{4}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Inverse Tangent Integration)',
        text: 'Find $\\int \\arctan x\\,dx$.',
        solution: '<p>$u = \\arctan x \\implies du = \\frac{1}{1+x^2}dx$; $dv = 1\\,dx \\implies v = x$. [M1]<br>$\\int \\arctan x\\,dx = x\\arctan x - \\int \\frac{x}{1+x^2}\\,dx$. [M1]<br>$= x\\arctan x - \\frac{1}{2}\\ln(1 + x^2) + C$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Partial Fractions with Repeated Factor)',
        text: 'Evaluate $\\int \\frac{x + 2}{(x + 1)^2}\\,dx$.',
        solution: '<p>$\\frac{x + 2}{(x + 1)^2} = \\frac{(x + 1) + 1}{(x + 1)^2} = \\frac{1}{x + 1} + \\frac{1}{(x + 1)^2}$. [M1]<br>$\\int \\left(\\frac{1}{x + 1} + (x + 1)^{-2}\\right)dx = \\ln|x + 1| - \\frac{1}{x + 1} + C$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Definite Integral with Partial Fractions)',
        text: 'Evaluate $\\int_0^1 \\frac{2x^2 + 5x + 1}{(x + 1)(x + 2)}\\,dx$.',
        solution: '<p>Degree numerator = degree denominator = 2. Divide polynomials first: [M1]<br>$\\frac{2x^2 + 5x + 1}{x^2 + 3x + 2} = 2 + \\frac{-x - 3}{x^2 + 3x + 2} = 2 - \\frac{x + 3}{(x + 1)(x + 2)}$. [A1]<br>Decompose $\\frac{x + 3}{(x + 1)(x + 2)} = \\frac{A}{x + 1} + \\frac{B}{x + 2}$: $A = 2, B = -1$.<br>Integral: $\\int_0^1 \\left(2 - \\frac{2}{x + 1} + \\frac{1}{x + 2}\\right)dx = [2x - 2\\ln(x+1) + \\ln(x+2)]_0^1$ [M1]<br>$= [2 - 2\\ln 2 + \\ln 3] - [0 - 0 + \\ln 2] = 2 - 3\\ln 2 + \\ln 3 = 2 + \\ln(3/8)$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Cyclic Integral with Exponential and Sine)',
        text: 'Find $\\int e^{2x}\\sin x\\,dx$.',
        solution: '<p>Let $I = \\int e^{2x}\\sin x\\,dx$. $u = \\sin x, dv = e^{2x}dx \\implies du = \\cos x\\,dx, v = \\frac{1}{2}e^{2x}$. [M1]<br>$I = \\frac{1}{2}e^{2x}\\sin x - \\frac{1}{2}\\int e^{2x}\\cos x\\,dx$.<br>For $\\int e^{2x}\\cos x\\,dx$: $u = \\cos x, dv = e^{2x}dx \\implies du = -\\sin x\\,dx, v = \\frac{1}{2}e^{2x}$. [M1]<br>$= \\frac{1}{2}e^{2x}\\cos x + \\frac{1}{2}\\int e^{2x}\\sin x\\,dx = \\frac{1}{2}e^{2x}\\cos x + \\frac{1}{2}I$.<br>Substitute back: $I = \\frac{1}{2}e^{2x}\\sin x - \\frac{1}{2}\\left(\\frac{1}{2}e^{2x}\\cos x + \\frac{1}{2}I\\right) = \\frac{1}{2}e^{2x}\\sin x - \\frac{1}{4}e^{2x}\\cos x - \\frac{1}{4}I$. [M1]<br>$\\frac{5}{4}I = \\frac{1}{4}e^{2x}(2\\sin x - \\cos x) \\implies I = \\frac{e^{2x}(2\\sin x - \\cos x)}{5} + C$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Reduction Formula for Powers of Natural Log)',
        text: 'Let $I_n = \\int (\\ln x)^n\\,dx$. Show that $I_n = x(\\ln x)^n - n I_{n-1}$, and hence evaluate $\\int (\\ln x)^2\\,dx$.',
        solution: '<p>$u = (\\ln x)^n, dv = dx \\implies du = n(\\ln x)^{n-1}\\frac{1}{x}dx, v = x$. [M1]<br>$I_n = x(\\ln x)^n - \\int x \\cdot n(\\ln x)^{n-1}\\frac{1}{x}dx = x(\\ln x)^n - n\\int (\\ln x)^{n-1}\\,dx = x(\\ln x)^n - n I_{n-1}$. [A1]<br>For $n = 2$: $I_2 = x(\\ln x)^2 - 2I_1$.<br>Since $I_1 = \\int \\ln x\\,dx = x\\ln x - x$:<br>$I_2 = x(\\ln x)^2 - 2(x\\ln x - x) + C = x(\\ln x)^2 - 2x\\ln x + 2x + C$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Partial Fraction with Irreducible Quadratic)',
        text: 'Evaluate $\\int \\frac{2x^2 - x + 4}{x(x^2 + 4)}\\,dx$.',
        solution: '<p>$\\frac{2x^2 - x + 4}{x(x^2 + 4)} = \\frac{A}{x} + \\frac{Bx + C}{x^2 + 4}$. [M1]<br>$2x^2 - x + 4 = A(x^2 + 4) + (Bx + C)x$.<br>• $x = 0$: $4 = 4A \\implies A = 1$. [A1]<br>• Compare $x^2$: $2 = A + B \\implies 2 = 1 + B \\implies B = 1$.<br>• Compare $x$: $-1 = C \\implies C = -1$.<br>Integral: $\\int \\left( \\frac{1}{x} + \\frac{x - 1}{x^2 + 4} \\right)dx = \\int \\frac{1}{x}\\,dx + \\frac{1}{2}\\int \\frac{2x}{x^2 + 4}\\,dx - \\int \\frac{1}{x^2 + 4}\\,dx$. [M1]<br>$= \\ln|x| + \\frac{1}{2}\\ln(x^2 + 4) - \\frac{1}{2}\\arctan\\left(\\frac{x}{2}\\right) + C$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 5)</h2>
        <div class="formula-card">
          <h4>Syllabus 5.13: Advanced Integration</h4>
          $$\\int u\\frac{dv}{dx}\\,dx = uv - \\int v\\frac{du}{dx}\\,dx$$
          $$\\int \\frac{1}{x^2 + a^2}\\,dx = \\frac{1}{a}\\arctan\\left(\\frac{x}{a}\\right) + C$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>LIATE Rule for Parts</h4>
          <p><strong>L</strong>ogarithmic $\\to$ <strong>I</strong>nverse trig $\\to$ <strong>A</strong>lgebraic $\\to$ <strong>T</strong>rigonometric $\\to$ <strong>E</strong>xponential</p>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Sign Errors in Cyclic Integrals</h4>
          <p>When applying parts twice, watch double and triple negative signs: $-(-(-I)) = -I$. Always write out parentheses carefully.</p>
        </div>
        <div class="pitfall-card">
          <h4>Forgetting $\\frac{1}{a}$ in Arctan</h4>
          <p>$\\int \\frac{1}{x^2 + 9}\\,dx = \\frac{1}{3}\\arctan\\left(\\frac{x}{3}\\right) + C$. Forgetting the leading $\\frac{1}{3}$ factor is a classic error.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'According to the LIATE hierarchy, which function should be chosen as $u$ in $\\int x^3 \\ln x\\,dx$?',
        options: [
          '$x^3$',
          '$\\ln x$',
          '$1$',
          '$x$'
        ],
        correct: 1,
        explanation: 'Logarithmic functions (L) take highest precedence in LIATE over Algebraic (A).'
      },
      {
        id: 'q2',
        prompt: 'What is $\\int \\frac{1}{x^2 + 16}\\,dx$?',
        options: [
          '$\\arctan(x/4) + C$',
          '$\\frac{1}{4}\\arctan(x/4) + C$',
          '$\\frac{1}{16}\\arctan(x/16) + C$',
          '$\\ln|x^2 + 16| + C$'
        ],
        correct: 1,
        explanation: 'Standard booklet formula: $\\frac{1}{a}\\arctan(x/a)$ with $a = 4$, yielding $\\frac{1}{4}\\arctan(x/4) + C$.'
      },
      {
        id: 'q3',
        prompt: 'What is $\\int x e^x\\,dx$?',
        options: [
          '$x e^x - e^x + C$',
          '$x e^x + e^x + C$',
          '$\\frac{1}{2}x^2 e^x + C$',
          '$e^x + C$'
        ],
        correct: 0,
        explanation: '$uv - \\int v\\,du = x e^x - \\int e^x\\,dx = x e^x - e^x + C$.'
      },
      {
        id: 'q4',
        prompt: 'Why can $\\int \\ln x\\,dx$ be solved by integration by parts?',
        options: [
          'Because $\\ln x$ is an algebraic polynomial',
          'By treating the integrand as $1 \\cdot \\ln x$ with $dv = 1\\,dx$',
          'By using trigonometric substitution',
          'Because $\\frac{d}{dx}(\\ln x) = e^x$'
        ],
        correct: 1,
        explanation: 'Writing the integrand as $1 \\cdot \\ln x$ allows setting $u = \\ln x$ and $dv = dx$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the integral $I = \\int_1^e x^2 \\ln x\\,dx$.<br><strong>(a)</strong> Use integration by parts to show that $I = \\left[ \\frac{x^3}{3}\\ln x \\right]_1^e - \\int_1^e \\frac{x^2}{3}\\,dx$. [3 marks]<br><strong>(b)</strong> Hence evaluate the exact value of $I$ in terms of $e$. [3 marks]',
        solution: `
          <p><strong>(a) Parts set up: [3 marks]</strong><br>
          $u = \\ln x \\implies du = \\frac{1}{x}dx$ [M1].<br>
          $dv = x^2 dx \\implies v = \\frac{x^3}{3}$ [M1].<br>
          $I = \\left[ \\frac{x^3}{3}\\ln x \\right]_1^e - \\int_1^e \\frac{x^3}{3}\\left(\\frac{1}{x}\\right)dx = \\left[ \\frac{x^3}{3}\\ln x \\right]_1^e - \\int_1^e \\frac{x^2}{3}\\,dx$ [A1].</p>
          <p><strong>(b) Evaluation: [3 marks]</strong><br>
          First term: $\\left( \\frac{e^3}{3}\\ln e \\right) - \\left( \\frac{1}{3}\\ln 1 \\right) = \\frac{e^3}{3} - 0 = \\frac{e^3}{3}$ [A1].<br>
          Second term: $\\int_1^e \\frac{x^2}{3}\\,dx = \\left[ \\frac{x^3}{9} \\right]_1^e = \\frac{e^3 - 1}{9}$ [A1].<br>
          $I = \\frac{e^3}{3} - \\frac{e^3 - 1}{9} = \\frac{3e^3 - e^3 + 1}{9} = \\frac{2e^3 + 1}{9}$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'A curve has gradient $\\frac{dy}{dx} = \\frac{x + 7}{(x - 1)(x + 3)}$.<br><strong>(a)</strong> Express $\\frac{dy}{dx}$ in partial fractions. [3 marks]<br><strong>(b)</strong> Given that the curve passes through $(2, 5)$, find the equation of the curve in the form $y = f(x)$. [4 marks]',
        solution: `
          <p><strong>(a) Partial fractions: [3 marks]</strong><br>
          $\\frac{x + 7}{(x - 1)(x + 3)} = \\frac{A}{x - 1} + \\frac{B}{x + 3}$ [M1].<br>
          $x + 7 = A(x + 3) + B(x - 1)$.<br>
          • $x = 1$: $8 = 4A \\implies A = 2$ [A1].<br>
          • $x = -3$: $4 = -4B \\implies B = -1$ [A1].<br>
          $\\frac{dy}{dx} = \\frac{2}{x - 1} - \\frac{1}{x + 3}$.</p>
          <p><strong>(b) Integration &amp; Particular Solution: [4 marks]</strong><br>
          $y = \\int \\left(\\frac{2}{x - 1} - \\frac{1}{x + 3}\\right)dx = 2\\ln|x - 1| - \\ln|x + 3| + C$ [M1][A1].<br>
          Substitute $(2, 5)$:<br>
          $5 = 2\\ln(1) - \\ln(5) + C = 0 - \\ln 5 + C \\implies C = 5 + \\ln 5$ [M1].<br>
          $y = 2\\ln|x - 1| - \\ln|x + 3| + 5 + \\ln 5 = \\ln\\left( \\frac{5(x - 1)^2}{|x + 3|} \\right) + 5$ [A1].</p>
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
  <link rel="canonical" href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${guide.pageTitle}">
  <meta property="og:description" content="${guide.metaDesc}">
  <meta property="og:url" content="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/">
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

  <script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"IB Mathematics","item":"https://sjmaths.com/ib/"},{"@type":"ListItem","position":3,"name":"IB DP Mathematics","item":"https://sjmaths.com/ib/dp-mathematics/"},{"@type":"ListItem","position":4,"name":"AA HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/"},{"@type":"ListItem","position":5,"name":"Calculus HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/"},{"@type":"ListItem","position":6,"name":"${guide.title}","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/"}]},{"@type":"Article","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/#article","headline":"${guide.title} | IB Math AA HL Guide","description":"${guide.metaDesc}","url":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/","dateModified":"2026-10-11","inLanguage":"en","articleSection":"IB DP Mathematics AA HL · Topic ${guide.code}","author":{"@type":"Person","name":"Sandeep Jaiswal","url":"https://sjmaths.com/pages/about.html"},"publisher":{"@type":"Organization","name":"SJMaths","url":"https://sjmaths.com/","logo":{"@type":"ImageObject","url":"https://sjmaths.com/assets/icons/icon-512x512.png"}}}]}</script>
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
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/calculus/">Topic 5 HL</a>
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
      <a href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/">Calculus</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
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
