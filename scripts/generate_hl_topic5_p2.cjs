const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'calculus');

const guides = [
  // =========================================================================
  // GUIDE 20: First-Order Differential Equations & Euler's Method
  // =========================================================================
  {
    folder: 'first-order-differential-equations',
    code: '5.16 & 5.17',
    title: 'First-Order Differential Equations & Euler’s Method',
    pageTitle: 'First-Order Differential Equations & Euler’s Method | IB Math AA HL | SJMaths',
    metaDesc: 'Master first-order differential equations for IB DP Mathematics AA HL (Topics 5.16 & 5.17). Separation of variables, integrating factor method, Euler’s step method, slope fields, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL differential equations, separation of variables, integrating factor method, Eulers method step size, slope fields, initial value problem',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Solve analytical and numerical first-order differential equations: separation of variables $\\frac{dy}{dx} = g(x)h(y)$, integrating factor $I(x) = e^{\\int P(x)dx}$ for linear ODEs, and Euler’s step-by-step approximation $y_{n+1} = y_n + h f(x_n, y_n)$.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/advanced-integration-parts-and-partial-fractions/',
      title: 'Advanced Integration: Parts, Substitutions & Partial Fractions'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/volumes-of-revolution/',
      title: 'Volumes of Revolution'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-chart-line" style="color:var(--c-primary);"></i> Figure 5.4: Euler’s Numerical Step Method vs. Exact Solution Curve</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing Euler's method tangent steps approximating an exact solution curve">
            <!-- Axes -->
            <line x1="80" y1="240" x2="700" y2="240" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="120" y1="30" x2="120" y2="250" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="690" y="230" fill="var(--c-text)" font-size="13" font-weight="bold">x</text>
            <text x="130" y="45" fill="var(--c-text)" font-size="13" font-weight="bold">y</text>

            <!-- Exact Solution Curve (smooth exponential-like curve) -->
            <path d="M 160,200 Q 280,185 400,140 T 640,40" fill="none" stroke="#10b981" stroke-width="3" />
            <text x="610" y="30" font-size="13" font-weight="bold" fill="#10b981">Exact Solution y(x)</text>

            <!-- Euler Step 0: (x0, y0) at (160, 200) -->
            <circle cx="160" cy="200" r="5" fill="#6366f1" />
            <text x="145" y="220" font-size="12" font-weight="bold" fill="#6366f1">(x₀, y₀)</text>

            <!-- Euler Step 1: line from (160, 200) to (300, 180) -->
            <line x1="160" y1="200" x2="300" y2="180" stroke="#6366f1" stroke-width="2.5" />
            <circle cx="300" cy="180" r="5" fill="#6366f1" />
            <text x="290" y="200" font-size="12" font-weight="bold" fill="#6366f1">(x₁, y₁)</text>

            <!-- Euler Step 2: line from (300, 180) to (440, 135) -->
            <line x1="300" y1="180" x2="440" y2="135" stroke="#6366f1" stroke-width="2.5" />
            <circle cx="440" cy="135" r="5" fill="#6366f1" />
            <text x="430" y="155" font-size="12" font-weight="bold" fill="#6366f1">(x₂, y₂)</text>

            <!-- Euler Step 3: line from (440, 135) to (580, 70) -->
            <line x1="440" y1="135" x2="580" y2="70" stroke="#6366f1" stroke-width="2.5" />
            <circle cx="580" cy="70" r="5" fill="#ef4444" />
            <text x="590" y="75" font-size="12" font-weight="bold" fill="#ef4444">(x₃, y₃) Numerical</text>

            <!-- Error gap at x3 -->
            <line x1="580" y1="70" x2="580" y2="55" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3" />
            <circle cx="580" cy="55" r="4" fill="#10b981" />
            <text x="590" y="55" font-size="11" font-weight="bold" fill="#ef4444">Truncation Error</text>

            <!-- Step size indicator h -->
            <line x1="160" y1="245" x2="300" y2="245" stroke="#6366f1" stroke-width="1.5" marker-end="url(#arrow)" />
            <line x1="160" y1="240" x2="160" y2="250" stroke="#6366f1" stroke-width="1.5" />
            <line x1="300" y1="240" x2="300" y2="250" stroke="#6366f1" stroke-width="1.5" />
            <text x="225" y="260" font-size="12" font-weight="bold" fill="#6366f1">Step size h</text>

            <!-- Formula display -->
            <rect x="240" y="15" width="280" height="42" rx="8" fill="var(--c-surface-raised, #f8fafc)" stroke="var(--c-border)" />
            <text x="380" y="42" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary)">y_{n+1} = y_n + h · f(x_n, y_n)</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Separation of Variables (Topic 5.16)</h2>
        <p>A first-order ordinary differential equation (ODE) is <strong>separable</strong> if it can be expressed in the form:</p>
        $$\\frac{dy}{dx} = g(x) \\, h(y) \\quad \\Longleftrightarrow \\quad \\frac{1}{h(y)} \\, dy = g(x) \\, dx$$
        <p>Integrating both sides yields the general solution:</p>
        $$\\int \\frac{1}{h(y)} \\, dy = \\int g(x) \\, dx + C$$
        <div class="alert-box alert-tip" style="background:var(--c-surface-raised); border-left:4px solid var(--c-primary); padding:1rem; margin:1.25rem 0; border-radius:8px;">
          <strong>Examiner Tip:</strong> Always add the constant of integration $C$ immediately upon performing the indefinite integration, <em>before</em> applying algebraic transformations such as taking exponentials or square roots.
        </div>

        <h2>2. Linear Differential Equations &amp; Integrating Factor Method (Topic 5.16)</h2>
        <p>A linear first-order differential equation has standard form:</p>
        $$\\frac{dy}{dx} + P(x)\\,y = Q(x)$$
        <p>To solve, multiply every term by the <strong>integrating factor</strong> $I(x)$ defined as:</p>
        $$I(x) = e^{\\int P(x) \\, dx}$$
        <p>By the product rule, the left-hand side collapses into the exact derivative of a single product:</p>
        $$\\frac{d}{dx}\\left[ y \\cdot I(x) \\right] = Q(x) \\cdot I(x)$$
        <p>Integrating with respect to $x$ gives the closed-form general solution:</p>
        $$y \\cdot I(x) = \\int Q(x) \\, I(x) \\, dx + C \\quad \\implies \\quad y = \\frac{1}{I(x)}\\left( \\int Q(x) \\, I(x) \\, dx + C \\right)$$

        <h2>3. Euler’s Method for Numerical Solutions (Topic 5.17)</h2>
        <p>When an ODE $\\frac{dy}{dx} = f(x, y)$ cannot be solved analytically in elementary functions, <strong>Euler’s Method</strong> provides a first-order numerical approximation over successive discrete increments of step size $h$:</p>
        $$\\begin{cases} x_{n+1} = x_n + h \\\\ y_{n+1} = y_n + h \\cdot f(x_n, y_n) \\end{cases}$$
        <div class="alert-box alert-warning" style="background:var(--c-surface-raised); border-left:4px solid #f59e0b; padding:1rem; margin:1.25rem 0; border-radius:8px;">
          <strong>Error Analysis &amp; Concavity:</strong>
          <ul style="margin:0.5rem 0 0 1.25rem;">
            <li>If $y''(x) > 0$ (curve is concave up), the tangent lines lie <em>below</em> the curve $\\implies$ Euler’s method yields an <strong>underestimate</strong>.</li>
            <li>If $y''(x) < 0$ (curve is concave down), the tangent lines lie <em>above</em> the curve $\\implies$ Euler’s method yields an <strong>overestimate</strong>.</li>
          </ul>
        </div>
    `,
    exercises: [
      {
        num: 1,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Find the general solution of the differential equation $\\frac{dy}{dx} = 2x(y^2 + 1)$.',
        solution: `
          <p><strong>Step 1: Separate variables:</strong></p>
          $$\\frac{1}{y^2 + 1}\\,dy = 2x\\,dx$$
          <p><strong>Step 2: Integrate both sides:</strong></p>
          $$\\int \\frac{1}{y^2 + 1}\\,dy = \\int 2x\\,dx \\implies \\arctan(y) = x^2 + C$$
          <p><strong>Step 3: Solve explicitly for $y$:</strong></p>
          $$y = \\tan(x^2 + C)$$
        `
      },
      {
        num: 2,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Solve the initial value problem $\\frac{dy}{dx} = \\frac{e^{2x}}{y}$, with initial condition $y(0) = -3$.',
        solution: `
          <p><strong>Step 1: Separate variables and integrate:</strong></p>
          $$y\\,dy = e^{2x}\\,dx \\implies \\int y\\,dy = \\int e^{2x}\\,dx \\implies \\frac{1}{2}y^2 = \\frac{1}{2}e^{2x} + C$$
          <p>Multiply by 2: $y^2 = e^{2x} + K$, where $K = 2C$.</p>
          <p><strong>Step 2: Apply initial condition $y(0) = -3$:</strong></p>
          $$(-3)^2 = e^0 + K \\implies 9 = 1 + K \\implies K = 8$$
          <p><strong>Step 3: Choose the correct sign branch:</strong></p>
          <p>Since $y(0) = -3 < 0$, we choose the negative square root:</p>
          $$y = -\\sqrt{e^{2x} + 8}$$
        `
      },
      {
        num: 3,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Find the general solution of the linear differential equation $\\frac{dy}{dx} + \\frac{2}{x}y = 5x^2$, for $x > 0$.',
        solution: `
          <p><strong>Step 1: Identify standard form:</strong></p>
          <p>Here $P(x) = \\frac{2}{x}$ and $Q(x) = 5x^2$.</p>
          <p><strong>Step 2: Compute integrating factor $I(x)$:</strong></p>
          $$I(x) = e^{\\int \\frac{2}{x}\\,dx} = e^{2\\ln x} = e^{\\ln(x^2)} = x^2$$
          <p><strong>Step 3: Multiply the ODE by $I(x) = x^2$:</strong></p>
          $$\\frac{d}{dx}\\left[ x^2 y \\right] = x^2(5x^2) = 5x^4$$
          <p><strong>Step 4: Integrate with respect to $x$:</strong></p>
          $$x^2 y = \\int 5x^4\\,dx = x^5 + C$$
          <p><strong>Step 5: Solve for $y$:</strong></p>
          $$y = x^3 + \\frac{C}{x^2}$$
        `
      },
      {
        num: 4,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Solve the initial value problem $\\frac{dy}{dx} + y\\tan x = \\cos^2 x$, given that $y(0) = 2$, for $-\\frac{\\pi}{2} < x < \\frac{\\pi}{2}$.',
        solution: `
          <p><strong>Step 1: Find integrating factor $I(x)$:</strong></p>
          $$I(x) = e^{\\int \\tan x\\,dx} = e^{\\ln|\\sec x|} = \\sec x$$
          <p><strong>Step 2: Apply the product rule integration:</strong></p>
          $$\\frac{d}{dx}\\left[ y\\sec x \\right] = \\sec x \\cos^2 x = \\cos x$$
          $$y\\sec x = \\int \\cos x\\,dx = \\sin x + C$$
          <p><strong>Step 3: Substitute $x=0, y=2$:</strong></p>
          $$2\\sec(0) = \\sin(0) + C \\implies 2(1) = 0 + C \\implies C = 2$$
          <p><strong>Step 4: Solve for $y$:</strong></p>
          $$y = \\frac{\\sin x + 2}{\\sec x} = \\sin x \\cos x + 2\\cos x = \\frac{1}{2}\\sin 2x + 2\\cos x$$
        `
      },
      {
        num: 5,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Given the differential equation $\\frac{dy}{dx} = x + y^2$ with $y(0) = 1$, use Euler’s method with step size $h = 0.1$ to approximate $y(0.2)$ to 4 decimal places.',
        solution: `
          <p><strong>Step 1: First iteration from $x_0 = 0$ to $x_1 = 0.1$:</strong></p>
          $$f(x_0, y_0) = f(0, 1) = 0 + 1^2 = 1$$
          $$y_1 = y_0 + h\\cdot f(x_0, y_0) = 1 + 0.1(1) = 1.1$$
          <p><strong>Step 2: Second iteration from $x_1 = 0.1$ to $x_2 = 0.2$:</strong></p>
          $$f(x_1, y_1) = f(0.1, 1.1) = 0.1 + (1.1)^2 = 0.1 + 1.21 = 1.31$$
          $$y_2 = y_1 + h\\cdot f(x_1, y_1) = 1.1 + 0.1(1.31) = 1.1 + 0.131 = 1.231$$
          <p>Therefore, the approximation is $y(0.2) \\approx 1.2310$.</p>
        `
      },
      {
        num: 6,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'A hot cup of coffee with initial temperature $90^\\circ\\text{C}$ is placed in a room at constant temperature $20^\\circ\\text{C}$. Newton’s law of cooling gives $\\frac{dT}{dt} = -k(T - 20)$. After 5 minutes, $T = 60^\\circ\\text{C}$. Find the temperature after 15 minutes.',
        solution: `
          <p><strong>Step 1: Separate variables:</strong></p>
          $$\\frac{1}{T - 20}\\,dT = -k\\,dt \\implies \\ln(T - 20) = -kt + C \\implies T - 20 = A e^{-kt}$$
          <p><strong>Step 2: Use initial condition $T(0) = 90$:</strong></p>
          $$90 - 20 = A e^0 \\implies A = 70 \\implies T(t) = 20 + 70e^{-kt}$$
          <p><strong>Step 3: Find decay constant $k$ using $T(5) = 60$:</strong></p>
          $$60 = 20 + 70e^{-5k} \\implies 40 = 70e^{-5k} \\implies e^{-5k} = \\frac{4}{7}$$
          <p><strong>Step 4: Evaluate temperature at $t = 15$:</strong></p>
          <p>Notice that $e^{-15k} = (e^{-5k})^3 = \\left(\\frac{4}{7}\\right)^3 = \\frac{64}{343}$.</p>
          $$T(15) = 20 + 70\\left(\\frac{64}{343}\\right) = 20 + \\frac{10 \\times 64}{49} = 20 + \\frac{640}{49} \\approx 20 + 13.06 = 33.1^\\circ\\text{C}$$
        `
      },
      {
        num: 7,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'Find the particular solution to $x\\frac{dy}{dx} - y = x^3 e^x$ satisfying $y(1) = 0$, for $x > 0$.',
        solution: `
          <p><strong>Step 1: Convert to standard linear form:</strong></p>
          <p>Divide by $x$:</p>
          $$\\frac{dy}{dx} - \\frac{1}{x}y = x^2 e^x$$
          <p><strong>Step 2: Determine integrating factor $I(x)$:</strong></p>
          $$I(x) = e^{\\int -\\frac{1}{x}\\,dx} = e^{-\\ln x} = \\frac{1}{x}$$
          <p><strong>Step 3: Multiply and integrate:</strong></p>
          $$\\frac{d}{dx}\\left[ \\frac{y}{x} \\right] = \\frac{1}{x}(x^2 e^x) = x e^x$$
          $$\\frac{y}{x} = \\int x e^x\\,dx$$
          <p>Using integration by parts with $u = x, dv = e^x dx$:</p>
          $$\\int x e^x\\,dx = x e^x - e^x + C = e^x(x - 1) + C$$
          <p><strong>Step 4: Apply $y(1) = 0$:</strong></p>
          $$\\frac{0}{1} = e^1(1 - 1) + C \\implies C = 0$$
          <p><strong>Step 5: Final solution:</strong></p>
          $$y = x^2 e^x - x e^x = x(x - 1)e^x$$
        `
      },
      {
        num: 8,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'Consider the differential equation $\\frac{dy}{dx} = 2x - y$ with $y(0) = 1$. Use Euler’s method with step $h = 0.5$ to estimate $y(1)$. Determine whether this estimate is an overestimate or an underestimate by evaluating the second derivative $y\'\'$.',
        solution: `
          <p><strong>Step 1: Euler iteration:</strong></p>
          <p>$x_0 = 0, y_0 = 1$:</p>
          $$y_1 = y_0 + 0.5(2(0) - 1) = 1 - 0.5 = 0.5 \\quad (x_1 = 0.5)$$
          <p>$x_1 = 0.5, y_1 = 0.5$:</p>
          $$y_2 = y_1 + 0.5(2(0.5) - 0.5) = 0.5 + 0.5(0.5) = 0.5 + 0.25 = 0.75 \\quad (x_2 = 1)$$
          <p>So the Euler estimate is $y(1) \\approx 0.75$.</p>
          <p><strong>Step 2: Second derivative analysis:</strong></p>
          $$y'' = \\frac{d}{dx}[2x - y] = 2 - y' = 2 - (2x - y) = 2 - 2x + y$$
          <p>On the interval $[0, 1]$, $2 - 2x \\ge 0$ and $y(x) > 0$, so $y''(x) > 0$.</p>
          <p>Since the curve is concave up ($y'' > 0$), the tangent lines lie below the actual solution, meaning Euler’s method yields an <strong>underestimate</strong>.</p>
        `
      },
      {
        num: 9,
        tier: 'HL Distinction',
        badgeClass: 'badge-hl',
        stem: 'A tank initially contains $100\\text{ L}$ of pure water. Brine containing $0.5\\text{ kg/L}$ of salt flows in at $4\\text{ L/min}$, and the thoroughly mixed solution drains out at $4\\text{ L/min}$. Set up and solve the differential equation for the mass of salt $S(t)$ in the tank at time $t$, and find the limiting salt mass as $t \\to \\infty$.',
        solution: `
          <p><strong>Step 1: Rate of change equation:</strong></p>
          $$\\frac{dS}{dt} = \\text{Rate In} - \\text{Rate Out}$$
          $$\\text{Rate In} = 4\\text{ L/min} \\times 0.5\\text{ kg/L} = 2\\text{ kg/min}$$
          $$\\text{Rate Out} = 4\\text{ L/min} \\times \\frac{S(t)}{100}\\text{ kg/L} = \\frac{S}{25}\\text{ kg/min}$$
          $$\\frac{dS}{dt} = 2 - \\frac{S}{25} = \\frac{50 - S}{25}$$
          <p><strong>Step 2: Separate variables:</strong></p>
          $$\\frac{1}{50 - S}\\,dS = \\frac{1}{25}\\,dt \\implies -\\ln|50 - S| = \\frac{t}{25} + C$$
          $$50 - S = A e^{-t/25}$$
          <p><strong>Step 3: Initial condition $S(0) = 0$ (pure water):</strong></p>
          $$50 - 0 = A e^0 \\implies A = 50$$
          $$S(t) = 50\\left(1 - e^{-t/25}\\right)$$
          <p><strong>Step 4: Limiting salt mass:</strong></p>
          $$\\lim_{t \\to \\infty} S(t) = 50(1 - 0) = 50\\text{ kg}$$
        `
      },
      {
        num: 10,
        tier: 'HL Distinction',
        badgeClass: 'badge-hl',
        stem: 'A falling object of mass $m$ experiences downward gravity $mg$ and air resistance proportional to velocity $kv$. Starting from rest ($v(0) = 0$), solve $m\\frac{dv}{dt} = mg - kv$. Then show that as $t \\to \\infty$, the terminal velocity is $v_T = \\frac{mg}{k}$.',
        solution: `
          <p><strong>Step 1: Rewrite as standard linear ODE:</strong></p>
          $$\\frac{dv}{dt} + \\frac{k}{m}v = g$$
          <p><strong>Step 2: Integrating factor:</strong></p>
          $$I(t) = e^{\\int (k/m)dt} = e^{kt/m}$$
          <p><strong>Step 3: Multiply and integrate:</strong></p>
          $$\\frac{d}{dt}\\left[ v e^{kt/m} \\right] = g e^{kt/m}$$
          $$v e^{kt/m} = \\int g e^{kt/m}\\,dt = \\frac{mg}{k}e^{kt/m} + C$$
          $$v(t) = \\frac{mg}{k} + C e^{-kt/m}$$
          <p><strong>Step 4: Apply $v(0) = 0$:</strong></p>
          $$0 = \\frac{mg}{k} + C \\implies C = -\\frac{mg}{k}$$
          $$v(t) = \\frac{mg}{k}\\left(1 - e^{-kt/m}\\right)$$
          <p><strong>Step 5: Limit as $t \\to \\infty$:</strong></p>
          <p>Since $k, m > 0$, $\\lim_{t \\to \\infty} e^{-kt/m} = 0$, giving $v_T = \\frac{mg}{k}$.</p>
        `
      }
    ],
    formulasHtml: `
        <h2>Topic 5.16 &amp; 5.17 Formula Booklet Reference</h2>
        <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem; margin-bottom:1.5rem;">
          <h3 style="margin-top:0; color:var(--c-primary);"><i class="fa-solid fa-book-bookmark"></i> Official IB Formula Booklet Entries</h3>
          <ul style="line-height:2;">
            <li><strong>Integrating Factor:</strong> For $\\frac{dy}{dx} + P(x)y = Q(x)$, the integrating factor is $I(x) = e^{\\int P(x)dx}$.</li>
            <li><strong>Euler’s Method:</strong> $y_{n+1} = y_n + h \\cdot f(x_n, y_n), \\quad x_{n+1} = x_n + h$</li>
          </ul>
        </div>

        <h2>Essential Pitfalls &amp; Strategy Cards</h2>
        <div class="grid grid-2" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.25rem;">
          <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem;">
            <h4 style="margin-top:0; color:#ef4444;"><i class="fa-solid fa-triangle-exclamation"></i> Pitfall: Dropping the Constant $+ C$</h4>
            <p>In $\\ln|y| = \\int g(x)dx + C$, students frequently write $y = e^{\\int g(x)dx} + C$. The exponentiation must apply to the entire sum: $y = e^{\\int g(x)dx + C} = A e^{\\int g(x)dx}$ where $A = \\pm e^C$.</p>
          </div>
          <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem;">
            <h4 style="margin-top:0; color:#f59e0b;"><i class="fa-solid fa-triangle-exclamation"></i> Pitfall: Sign in Integrating Factor</h4>
            <p>Ensure the ODE is in standard form $\\frac{dy}{dx} + P(x)y = Q(x)$ before taking $P(x)$. If the equation is $\\frac{dy}{dx} - \\frac{2}{x}y = 1$, then $P(x) = -\\frac{2}{x}$, giving $I(x) = e^{-2\\ln x} = x^{-2} = \\frac{1}{x^2}$.</p>
          </div>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        stem: 'What is the integrating factor for the linear differential equation $x\\frac{dy}{dx} + 3y = \\cos x$ (for $x > 0$)?',
        options: [
          { text: '$e^{3x}$', isCorrect: false, feedback: 'Incorrect. Remember to divide by $x$ first to put the equation in standard form $\\frac{dy}{dx} + P(x)y = Q(x)$.' },
          { text: '$x^3$', isCorrect: true, feedback: 'Correct! Standard form is $\\frac{dy}{dx} + \\frac{3}{x}y = \\frac{\\cos x}{x}$. Then $I(x) = e^{\\int \\frac{3}{x}dx} = e^{3\\ln x} = x^3$.' },
          { text: '$\\ln(x^3)$', isCorrect: false, feedback: 'Incorrect. The exponential of $3\\ln x$ simplifies directly to $x^3$.' },
          { text: '$\\frac{1}{x^3}$', isCorrect: false, feedback: 'Incorrect. The sign of $P(x) = +\\frac{3}{x}$ is positive.' }
        ]
      },
      {
        id: 'q2',
        stem: 'Given $\\frac{dy}{dx} = y - x$ with $y(1) = 2$, what is the Euler approximation for $y(1.2)$ using a single step of $h = 0.2$?',
        options: [
          { text: '2.1', isCorrect: false, feedback: 'Incorrect. Check your step calculation: $f(1, 2) = 2 - 1 = 1$.' },
          { text: '2.2', isCorrect: true, feedback: 'Correct! $y_1 = y_0 + h\\cdot f(x_0, y_0) = 2 + 0.2(2 - 1) = 2 + 0.2 = 2.2$.' },
          { text: '2.4', isCorrect: false, feedback: 'Incorrect. $h = 0.2$, not $0.4$.' },
          { text: '1.8', isCorrect: false, feedback: 'Incorrect. $f(1, 2) = 1 > 0$, so $y$ increases.' }
        ]
      },
      {
        id: 'q3',
        stem: 'If an analytical solution $y(x)$ satisfies $y\'\'(x) < 0$ on the interval $[a, b]$, Euler’s method produces:',
        options: [
          { text: 'An exact value', isCorrect: false, feedback: 'Incorrect. Euler’s method is only exact for linear functions where $y\'\' = 0$.' },
          { text: 'An overestimate', isCorrect: true, feedback: 'Correct! When $y\'\' < 0$, the curve is concave down, so tangent lines lie above the true curve, causing an overestimate.' },
          { text: 'An underestimate', isCorrect: false, feedback: 'Incorrect. Underestimates occur when $y\'\' > 0$ (concave up).' },
          { text: 'Oscillatory error', isCorrect: false, feedback: 'Incorrect. With constant concavity sign, error is monotonic.' }
        ]
      },
      {
        id: 'q4',
        stem: 'Which substitution converts $\\frac{dy}{dx} = f\\left(\\frac{y}{x}\\right)$ into a separable differential equation?',
        options: [
          { text: '$u = y - x$', isCorrect: false, feedback: 'Incorrect. That substitution is used when the RHS is of the form $f(y - x)$.' },
          { text: '$y = v x$', isCorrect: true, feedback: 'Correct! Letting $y = vx \\implies \\frac{dy}{dx} = v + x\\frac{dv}{dx}$, which reduces the ODE to $x\\frac{dv}{dx} = f(v) - v$, a separable ODE.' },
          { text: '$u = x^2 + y^2$', isCorrect: false, feedback: 'Incorrect. Polar transformations are not the standard homogeneous substitution.' },
          { text: '$u = e^{y/x}$', isCorrect: false, feedback: 'Incorrect.' }
        ]
      }
    ],
    frqs: [
      {
        id: 'frq1',
        title: 'Question 5 (FRQ) · Linear Differential Equation with Boundary Condition',
        stem: 'Consider the differential equation $(x + 1)\\frac{dy}{dx} + 2y = (x + 1)^3$ for $x > -1$, with $y(0) = 1$.<br>(a) Show that the integrating factor is $(x + 1)^2$. [2 marks]<br>(b) Find the explicit particular solution $y(x)$. [5 marks]',
        markscheme: `
          <p><strong>(a) Standard form and integrating factor:</strong></p>
          $$\\frac{dy}{dx} + \\frac{2}{x + 1}y = (x + 1)^2 \\quad \\text{[M1]}$$
          $$I(x) = e^{\\int \\frac{2}{x + 1}dx} = e^{2\\ln(x + 1)} = (x + 1)^2 \\quad \\text{[A1]}$$
          <p><strong>(b) Multiply and integrate:</strong></p>
          $$\\frac{d}{dx}\\left[ (x + 1)^2 y \\right] = (x + 1)^2 (x + 1)^2 = (x + 1)^4 \\quad \\text{[M1]}$$
          $$(x + 1)^2 y = \\int (x + 1)^4 dx = \\frac{1}{5}(x + 1)^5 + C \\quad \\text{[M1][A1]}$$
          <p>Apply $x=0, y=1$:</p>
          $$(1)^2(1) = \\frac{1}{5}(1)^5 + C \\implies 1 = \\frac{1}{5} + C \\implies C = \\frac{4}{5} \\quad \\text{[M1]}$$
          $$y = \\frac{1}{5}(x + 1)^3 + \\frac{4}{5(x + 1)^2} \\quad \\text{[A1]}$$
        `
      },
      {
        id: 'frq2',
        title: 'Question 6 (FRQ) · Euler’s Method vs Exact Solution',
        stem: 'Consider $\\frac{dy}{dx} = 2x - y$ with $y(0) = 2$.<br>(a) Use Euler’s method with step size $h = 0.1$ to approximate $y(0.2)$. [3 marks]<br>(b) Solve the ODE analytically to find the exact value of $y(0.2)$. [4 marks]<br>(c) Calculate the percentage error of the Euler approximation. [2 marks]',
        markscheme: `
          <p><strong>(a) Euler iterations:</strong></p>
          <p>$x_0 = 0, y_0 = 2 \\implies f(0, 2) = -2$</p>
          $$y_1 = 2 + 0.1(-2) = 1.8 \\quad (x_1 = 0.1) \\quad \\text{[M1]}$$
          <p>$f(0.1, 1.8) = 2(0.1) - 1.8 = 0.2 - 1.8 = -1.6$</p>
          $$y_2 = 1.8 + 0.1(-1.6) = 1.8 - 0.16 = 1.64 \\quad \\text{[A1]}$$
          <p><strong>(b) Analytical solution:</strong></p>
          $$\\frac{dy}{dx} + y = 2x \\implies I(x) = e^x \\quad \\text{[M1]}$$
          $$\\frac{d}{dx}[y e^x] = 2x e^x \\implies y e^x = 2(x e^x - e^x) + C = 2e^x(x - 1) + C \\quad \\text{[M1]}$$
          <p>Apply $y(0) = 2 \\implies 2 = 2(-1) + C \\implies C = 4$</p>
          $$y(x) = 2(x - 1) + 4e^{-x} = 2x - 2 + 4e^{-x} \\quad \\text{[A1]}$$
          <p>At $x = 0.2$: $y(0.2) = 2(0.2) - 2 + 4e^{-0.2} = -1.6 + 4(0.81873) = 1.6749$ [A1]</p>
          <p><strong>(c) Percentage error:</strong></p>
          $$\\text{Error} = \\left|\\frac{1.6749 - 1.6400}{1.6749}\\right| \\times 100\\% = \\frac{0.0349}{1.6749} \\times 100\\% \\approx 2.08\\% \\quad \\text{[M1][A1]}$$
        `
      }
    ]
  },

  // =========================================================================
  // GUIDE 21: Volumes of Revolution
  // =========================================================================
  {
    folder: 'volumes-of-revolution',
    code: '5.11 & 5.14',
    title: 'Volumes of Revolution (x and y Axes)',
    pageTitle: 'Volumes of Revolution (x and y Axes) | IB Math AA HL | SJMaths',
    metaDesc: 'Master volumes of revolution for IB DP Mathematics AA HL (Topics 5.11 & 5.14). Rotation around the x-axis and y-axis, washer method, shifted axes, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL volumes of revolution, rotate around x-axis, rotate around y-axis, washer method, solid of revolution calculus, pi integral y squared',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Calculate volumes of solids generated by revolving regions $2\\pi$ radians about coordinate axes: $V = \\pi \\int [f(x)]^2 dx$ around the $x$-axis, $V = \\pi \\int [g(y)]^2 dy$ around the $y$-axis, and the washer method $V = \\pi \\int (f^2 - g^2) dx$.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/first-order-differential-equations/',
      title: 'First-Order Differential Equations & Euler’s Method'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/maclaurin-and-taylor-series/',
      title: 'Maclaurin & Taylor Series'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-arrows-spin" style="color:var(--c-primary);"></i> Figure 5.5: Cylindrical Disk Slicing for Volume of Revolution about the x-axis</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="3D perspective diagram showing a curve rotated about the x-axis with an integrated circular disk element">
            <!-- Axis of revolution: x-axis -->
            <line x1="60" y1="140" x2="700" y2="140" stroke="var(--c-border, #cbd5e1)" stroke-width="2.5" />
            <line x1="120" y1="20" x2="120" y2="260" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
            <text x="690" y="130" fill="var(--c-text)" font-size="13" font-weight="bold">x (Axis of rotation)</text>
            <text x="130" y="35" fill="var(--c-text)" font-size="13" font-weight="bold">y</text>

            <!-- 3D Solid profile upper and lower -->
            <path d="M 180,140 Q 300,60 540,40" fill="none" stroke="#6366f1" stroke-width="3" />
            <path d="M 180,140 Q 300,220 540,240" fill="none" stroke="#6366f1" stroke-width="3" stroke-dasharray="4,4" />
            <text x="550" y="45" font-size="13" font-weight="bold" fill="#6366f1">y = f(x)</text>

            <!-- Representative Disk Slice at x = 360 -->
            <!-- Back of disk -->
            <ellipse cx="360" cy="140" rx="14" ry="60" fill="rgba(99, 102, 241, 0.15)" stroke="#6366f1" stroke-width="2" />
            <!-- Front of disk (thickness dx) -->
            <ellipse cx="380" cy="140" rx="14" ry="62" fill="rgba(99, 102, 241, 0.3)" stroke="#6366f1" stroke-width="2" />
            <line x1="360" y1="80" x2="380" y2="78" stroke="#6366f1" stroke-width="2" />
            <line x1="360" y1="200" x2="380" y2="202" stroke="#6366f1" stroke-width="2" />

            <!-- Radius indicator -->
            <line x1="380" y1="140" x2="380" y2="78" stroke="#ef4444" stroke-width="2" />
            <circle cx="380" cy="140" r="3" fill="#ef4444" />
            <text x="390" y="115" font-size="12" font-weight="bold" fill="#ef4444">r = y = f(x)</text>

            <!-- Thickness indicator dx -->
            <text x="365" y="225" font-size="12" font-weight="bold" fill="#6366f1">dx</text>

            <!-- Bounds x = a and x = b -->
            <line x1="180" y1="130" x2="180" y2="150" stroke="var(--c-text)" stroke-width="2" />
            <text x="175" y="165" font-size="13" font-weight="bold" fill="var(--c-text)">x = a</text>
            <line x1="540" y1="130" x2="540" y2="150" stroke="var(--c-text)" stroke-width="2" />
            <text x="535" y="165" font-size="13" font-weight="bold" fill="var(--c-text)">x = b</text>

            <!-- Formula Banner -->
            <rect x="220" y="10" width="320" height="35" rx="6" fill="var(--c-surface-raised, #f8fafc)" stroke="var(--c-border)" />
            <text x="380" y="32" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary)">dV = π · [f(x)]² dx  ⇒  V = π ∫ [f(x)]² dx</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Revolution About the x-axis (Topic 5.11)</h2>
        <p>When a plane region bounded by $y = f(x)$, the $x$-axis, and vertical lines $x = a$ and $x = b$ is rotated through $360^\\circ$ ($2\\pi$ radians) about the $x$-axis, slicing perpendicular to the axis of rotation produces thin cylindrical disks with radius $r = f(x)$ and thickness $dx$:</p>
        $$dV = \\pi r^2 \\, dx = \\pi [f(x)]^2 \\, dx$$
        <p>Integrating all circular cross-sections from $x = a$ to $x = b$ gives:</p>
        $$V_x = \\pi \\int_a^b [f(x)]^2 \\, dx = \\pi \\int_a^b y^2 \\, dx$$

        <h2>2. Revolution About the y-axis (Topic 5.14 HL)</h2>
        <p>When a region bounded by $x = g(y)$, the $y$-axis, and horizontal lines $y = c$ and $y = d$ is rotated $360^\\circ$ about the $y$-axis, the circular disks have radius $r = g(y) = x$ and thickness $dy$:</p>
        $$V_y = \\pi \\int_c^d [g(y)]^2 \\, dy = \\pi \\int_c^d x^2 \\, dy$$
        <div class="alert-box alert-tip" style="background:var(--c-surface-raised); border-left:4px solid var(--c-primary); padding:1rem; margin:1.25rem 0; border-radius:8px;">
          <strong>Examiner Tip for y-axis Rotations:</strong> Always rearrange the equation to make $x$ the subject in terms of $y$, and remember that the limits of integration must be $y$-coordinates ($y = c$ to $y = d$).
        </div>

        <h2>3. Washer Method: Region Between Two Curves</h2>
        <p>When the rotated region is bounded between an outer curve $y_{\\text{outer}} = f(x)$ and an inner curve $y_{\\text{inner}} = g(x)$:</p>
        $$V = \\pi \\int_a^b \\left( [f(x)]^2 - [g(x)]^2 \\right) dx$$
        <div class="alert-box alert-warning" style="background:var(--c-surface-raised); border-left:4px solid #f59e0b; padding:1rem; margin:1.25rem 0; border-radius:8px;">
          <strong>Fatal Examination Error:</strong> Never calculate $[f(x) - g(x)]^2$! The area of a washer ring is $\\pi R^2 - \\pi r^2 = \\pi (R^2 - r^2)$, which is the <em>difference of squares</em>, not the square of the difference!
        </div>
    `,
    exercises: [
      {
        num: 1,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Find the volume of the solid generated when the curve $y = \\sqrt{x}$ from $x = 0$ to $x = 4$ is revolved $360^\\circ$ about the $x$-axis.',
        solution: `
          <p><strong>Step 1: Formula for rotation about the $x$-axis:</strong></p>
          $$V = \\pi \\int_0^4 y^2\\,dx$$
          <p><strong>Step 2: Substitute $y^2 = (\\sqrt{x})^2 = x$:</strong></p>
          $$V = \\pi \\int_0^4 x\\,dx = \\pi \\left[ \\frac{1}{2}x^2 \\right]_0^4 = \\pi \\left( \\frac{16}{2} - 0 \\right) = 8\\pi$$
        `
      },
      {
        num: 2,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Find the volume of the solid generated by revolving the region bounded by $y = e^x$, the lines $x = 0$, $x = 2$, and the $x$-axis about the $x$-axis.',
        solution: `
          <p><strong>Step 1: Set up the integral:</strong></p>
          $$V = \\pi \\int_0^2 (e^x)^2\\,dx = \\pi \\int_0^2 e^{2x}\\,dx$$
          <p><strong>Step 2: Evaluate:</strong></p>
          $$V = \\pi \\left[ \\frac{1}{2}e^{2x} \\right]_0^2 = \\frac{\\pi}{2}(e^4 - e^0) = \\frac{\\pi}{2}(e^4 - 1)$$
        `
      },
      {
        num: 3,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'The region enclosed by $y = x^2$, the $y$-axis, and the line $y = 4$ is revolved $360^\\circ$ about the $y$-axis. Calculate the volume.',
        solution: `
          <p><strong>Step 1: Express $x$ in terms of $y$:</strong></p>
          <p>Since $y = x^2$ in the first quadrant, $x^2 = y$.</p>
          <p><strong>Step 2: Set up the integral with respect to $y$:</strong></p>
          $$V = \\pi \\int_0^4 x^2\\,dy = \\pi \\int_0^4 y\\,dy$$
          <p><strong>Step 3: Compute the volume:</strong></p>
          $$V = \\pi \\left[ \\frac{1}{2}y^2 \\right]_0^4 = \\pi \\left( \\frac{16}{2} \\right) = 8\\pi$$
        `
      },
      {
        num: 4,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Find the volume formed when the region bounded by $y = \\sin x$ from $x = 0$ to $x = \\pi$ and the $x$-axis is rotated $360^\\circ$ about the $x$-axis.',
        solution: `
          <p><strong>Step 1: Set up the integral:</strong></p>
          $$V = \\pi \\int_0^\\pi \\sin^2 x\\,dx$$
          <p><strong>Step 2: Use the double angle identity $\\sin^2 x = \\frac{1 - \\cos 2x}{2}$:</strong></p>
          $$V = \\pi \\int_0^\\pi \\frac{1 - \\cos 2x}{2}\\,dx = \\frac{\\pi}{2} \\left[ x - \\frac{1}{2}\\sin 2x \\right]_0^\\pi$$
          <p><strong>Step 3: Evaluate limits:</strong></p>
          $$V = \\frac{\\pi}{2} \\left( \\pi - \\frac{1}{2}\\sin(2\\pi) - (0 - 0) \\right) = \\frac{\\pi}{2}(\\pi - 0) = \\frac{\\pi^2}{2}$$
        `
      },
      {
        num: 5,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'The region between $y = x$ and $y = x^2$ is revolved $360^\\circ$ about the $x$-axis. Find the volume of the resulting solid.',
        solution: `
          <p><strong>Step 1: Find points of intersection:</strong></p>
          $$x = x^2 \\implies x(x - 1) = 0 \\implies x = 0 \\text{ and } x = 1$$
          <p>On $[0, 1]$, $x \\ge x^2$, so $y_{\\text{outer}} = x$ and $y_{\\text{inner}} = x^2$.</p>
          <p><strong>Step 2: Apply the washer method:</strong></p>
          $$V = \\pi \\int_0^1 \\left( [x]^2 - [x^2]^2 \\right) dx = \\pi \\int_0^1 (x^2 - x^4)\\,dx$$
          <p><strong>Step 3: Integrate:</strong></p>
          $$V = \\pi \\left[ \\frac{1}{3}x^3 - \\frac{1}{5}x^5 \\right]_0^1 = \\pi \\left( \\frac{1}{3} - \\frac{1}{5} \\right) = \\pi \\left( \\frac{2}{15} \\right) = \\frac{2\\pi}{15}$$
        `
      },
      {
        num: 6,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Find the volume generated when the curve $y = \\ln x$, from $y = 0$ to $y = 2$, is rotated $360^\\circ$ about the $y$-axis.',
        solution: `
          <p><strong>Step 1: Express $x$ as a function of $y$:</strong></p>
          $$y = \\ln x \\implies x = e^y$$
          <p><strong>Step 2: Set up the integral with respect to $y$:</strong></p>
          $$V = \\pi \\int_0^2 x^2\\,dy = \\pi \\int_0^2 (e^y)^2\\,dy = \\pi \\int_0^2 e^{2y}\\,dy$$
          <p><strong>Step 3: Evaluate:</strong></p>
          $$V = \\pi \\left[ \\frac{1}{2}e^{2y} \\right]_0^2 = \\frac{\\pi}{2}(e^4 - 1)$$
        `
      },
      {
        num: 7,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'The region enclosed by $y = \\frac{1}{\\sqrt{x^2 + 1}}$, the $x$-axis, $x = 0$, and $x = 1$ is rotated $360^\\circ$ about the $x$-axis. Find the volume.',
        solution: `
          <p><strong>Step 1: Set up the volume integral:</strong></p>
          $$V = \\pi \\int_0^1 y^2\\,dx = \\pi \\int_0^1 \\frac{1}{x^2 + 1}\\,dx$$
          <p><strong>Step 2: Integrate using standard arctan derivative:</strong></p>
          $$V = \\pi [\\arctan x]_0^1 = \\pi (\\arctan(1) - \\arctan(0)) = \\pi \\left( \\frac{\\pi}{4} - 0 \\right) = \\frac{\\pi^2}{4}$$
        `
      },
      {
        num: 8,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'Find the volume generated by rotating the region enclosed by $y = x^2$ and $y = 4$ about the line $y = 4$.',
        solution: `
          <p><strong>Step 1: Understand the shifted axis of rotation:</strong></p>
          <p>The line of rotation is the horizontal line $y = 4$. The distance from a point on the curve $(x, x^2)$ to the line $y = 4$ is the radius:</p>
          $$r(x) = 4 - x^2$$
          <p><strong>Step 2: Determine limits:</strong></p>
          <p>Intersection points are $x^2 = 4 \\implies x = -2$ to $x = 2$.</p>
          <p><strong>Step 3: Set up and evaluate integral:</strong></p>
          $$V = \\pi \\int_{-2}^2 (4 - x^2)^2\\,dx = 2\\pi \\int_0^2 (16 - 8x^2 + x^4)\\,dx$$
          $$V = 2\\pi \\left[ 16x - \\frac{8}{3}x^3 + \\frac{1}{5}x^5 \\right]_0^2 = 2\\pi \\left( 32 - \\frac{64}{3} + \\frac{32}{5} \\right)$$
          <p>Finding common denominator $15$:</p>
          $$32 - \\frac{64}{3} + \\frac{32}{5} = \\frac{480 - 320 + 96}{15} = \\frac{256}{15}$$
          $$V = 2\\pi \\times \\frac{256}{15} = \\frac{512\\pi}{15}$$
        `
      },
      {
        num: 9,
        tier: 'HL Distinction',
        badgeClass: 'badge-hl',
        stem: 'A glass goblet is designed by revolving the curve $y = 2 + \\sqrt{x}$ from $x = 0$ to $x = 9$ about the $x$-axis, where all coordinates are in centimetres.<br>(a) Find the total volume of the solid in $\\text{cm}^3$.<br>(b) If water is poured into the goblet at a constant rate of $10\\text{ cm}^3/\\text{s}$, find the rate of change of the water level $h$ when $h = 4\\text{ cm}$.',
        solution: `
          <p><strong>(a) Volume of the solid:</strong></p>
          $$V = \\pi \\int_0^9 (2 + \\sqrt{x})^2\\,dx = \\pi \\int_0^9 (4 + 4\\sqrt{x} + x)\\,dx$$
          $$V = \\pi \\left[ 4x + 4\\left(\\frac{2}{3}x^{3/2}\\right) + \\frac{1}{2}x^2 \\right]_0^9 = \\pi \\left[ 4(9) + \\frac{8}{3}(27) + \\frac{81}{2} \\right]$$
          $$V = \\pi \\left[ 36 + 72 + 40.5 \\right] = 148.5\\pi\\text{ cm}^3 = \\frac{297\\pi}{2}\\text{ cm}^3$$
          <p><strong>(b) Related rates for depth $h$:</strong></p>
          <p>The volume as a function of depth $h$ is $V(h) = \\pi \\int_0^h (2 + \\sqrt{x})^2 dx$.</p>
          <p>By the Fundamental Theorem of Calculus: $\\frac{dV}{dh} = \\pi (2 + \\sqrt{h})^2$.</p>
          <p>Using the chain rule: $\\frac{dV}{dt} = \\frac{dV}{dh} \\cdot \\frac{dh}{dt}$.</p>
          <p>At $h = 4$: $\\frac{dV}{dh} = \\pi (2 + \\sqrt{4})^2 = \\pi (2 + 2)^2 = 16\\pi$.</p>
          $$10 = 16\\pi \\cdot \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{10}{16\\pi} = \\frac{5}{8\\pi}\\text{ cm/s} \\approx 0.199\\text{ cm/s}$$
        `
      },
      {
        num: 10,
        tier: 'HL Distinction',
        badgeClass: 'badge-hl',
        stem: 'A circle of radius $r$ centered at $(R, 0)$ where $R > r$ has equation $(x - R)^2 + y^2 = r^2$. Rotating this circle $360^\\circ$ about the $y$-axis generates a solid ring called a <strong>torus</strong>. Prove using calculus that the volume of the torus is $V = 2\\pi^2 R r^2$.',
        solution: `
          <p><strong>Step 1: Express curves as $x$ in terms of $y$:</strong></p>
          $$(x - R)^2 = r^2 - y^2 \\implies x = R \\pm \\sqrt{r^2 - y^2}$$
          <p>Outer radius: $x_2 = R + \\sqrt{r^2 - y^2}$</p>
          <p>Inner radius: $x_1 = R - \\sqrt{r^2 - y^2}$</p>
          <p>The limits in $y$ are from $-r$ to $+r$.</p>
          <p><strong>Step 2: Set up washer method for rotation about $y$-axis:</strong></p>
          $$V = \\pi \\int_{-r}^r (x_2^2 - x_1^2)\\,dy$$
          <p>Notice the difference of squares factorization:</p>
          $$x_2^2 - x_1^2 = (x_2 - x_1)(x_2 + x_1)$$
          $$x_2 - x_1 = 2\\sqrt{r^2 - y^2}, \\quad x_2 + x_1 = 2R$$
          $$(x_2^2 - x_1^2) = (2\\sqrt{r^2 - y^2})(2R) = 4R\\sqrt{r^2 - y^2}$$
          <p><strong>Step 3: Integrate:</strong></p>
          $$V = \\pi \\int_{-r}^r 4R\\sqrt{r^2 - y^2}\\,dy = 4\\pi R \\int_{-r}^r \\sqrt{r^2 - y^2}\\,dy$$
          <p>Notice that $\\int_{-r}^r \\sqrt{r^2 - y^2} dy$ is geometrically the area of a semicircle of radius $r$, which is $\\frac{1}{2}\\pi r^2$:</p>
          $$V = 4\\pi R \\left( \\frac{1}{2}\\pi r^2 \\right) = 2\\pi^2 R r^2$$
          <p>This matches the famous Pappus Centroid Theorem result ($V = 2\\pi R \\cdot \\pi r^2$).</p>
        `
      }
    ],
    formulasHtml: `
        <h2>Topic 5.11 &amp; 5.14 Formula Booklet Reference</h2>
        <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem; margin-bottom:1.5rem;">
          <h3 style="margin-top:0; color:var(--c-primary);"><i class="fa-solid fa-book-bookmark"></i> Official IB Formula Booklet Entries</h3>
          <ul style="line-height:2;">
            <li><strong>Rotation about the x-axis:</strong> $V = \\pi \\int_a^b y^2 \\, dx$</li>
            <li><strong>Rotation about the y-axis (HL):</strong> $V = \\pi \\int_c^d x^2 \\, dy$</li>
          </ul>
        </div>

        <h2>Essential Pitfalls &amp; Strategy Cards</h2>
        <div class="grid grid-2" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.25rem;">
          <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem;">
            <h4 style="margin-top:0; color:#ef4444;"><i class="fa-solid fa-triangle-exclamation"></i> Pitfall: Forgetting $\\pi$ in Volume Integrals</h4>
            <p>Because students are accustomed to finding 2D area $\\int y dx$, they frequently omit the leading multiplier $\\pi$ when finding volumes of revolution. Always check the $\\pi$ symbol first!</p>
          </div>
          <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem;">
            <h4 style="margin-top:0; color:#f59e0b;"><i class="fa-solid fa-triangle-exclamation"></i> Pitfall: Limits in y-axis Rotation</h4>
            <p>When revolving about the $y$-axis, the integration variable is $y$. You must convert given $x$-limits to corresponding $y$-limits using $y = f(x)$ before setting up $\\int_c^d x^2 dy$.</p>
          </div>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        stem: 'What is the volume obtained by rotating the line $y = 2x$ from $x = 0$ to $x = 3$ about the $x$-axis?',
        options: [
          { text: '$18\\pi$', isCorrect: false, feedback: 'Incorrect. Remember to square the integrand: $y^2 = 4x^2$.' },
          { text: '$36\\pi$', isCorrect: true, feedback: 'Correct! $V = \\pi \\int_0^3 (2x)^2 dx = 4\\pi [\\frac{x^3}{3}]_0^3 = 4\\pi(9) = 36\\pi$.' },
          { text: '$24\\pi$', isCorrect: false, feedback: 'Incorrect.' },
          { text: '$54\\pi$', isCorrect: false, feedback: 'Incorrect.' }
        ]
      },
      {
        id: 'q2',
        stem: 'Which integral calculates the volume generated by revolving the region between $y = \\sqrt{x}$ and $y = x$ about the $x$-axis?',
        options: [
          { text: '$\\pi \\int_0^1 (\\sqrt{x} - x)^2 dx$', isCorrect: false, feedback: 'Incorrect! The washer method requires the difference of squares $\\pi \\int (R^2 - r^2)dx$, not the square of the difference.' },
          { text: '$\\pi \\int_0^1 (x - x^2) dx$', isCorrect: true, feedback: 'Correct! $V = \\pi \\int_0^1 ((\\sqrt{x})^2 - (x)^2) dx = \\pi \\int_0^1 (x - x^2) dx$.' },
          { text: '$\\pi \\int_0^1 (x^2 - x) dx$', isCorrect: false, feedback: 'Incorrect. On $[0, 1]$, $\\sqrt{x} \\ge x$, so the outer radius is $\\sqrt{x}$.' },
          { text: '$2\\pi \\int_0^1 x(\\sqrt{x} - x) dx$', isCorrect: false, feedback: 'Incorrect. Cylindrical shells is not in the IB syllabus.' }
        ]
      },
      {
        id: 'q3',
        stem: 'Revolving $y = x^3$ (for $0 \\le x \\le 2$) about the $y$-axis gives which integral for volume?',
        options: [
          { text: '$\\pi \\int_0^2 x^6 dx$', isCorrect: false, feedback: 'Incorrect. That would be rotation about the $x$-axis.' },
          { text: '$\\pi \\int_0^8 y^{2/3} dy$', isCorrect: true, feedback: 'Correct! $x = y^{1/3} \\implies x^2 = y^{2/3}$. The limits for $y$ are $0^3 = 0$ to $2^3 = 8$.' },
          { text: '$\\pi \\int_0^8 y^6 dy$', isCorrect: false, feedback: 'Incorrect.' },
          { text: '$\\pi \\int_0^2 y^{1/3} dy$', isCorrect: false, feedback: 'Incorrect.' }
        ]
      },
      {
        id: 'q4',
        stem: 'When the region under $y = f(x)$ from $x=a$ to $x=b$ is revolved about the horizontal line $y = -2$, the radius of each disk is:',
        options: [
          { text: '$f(x) - 2$', isCorrect: false, feedback: 'Incorrect. The line is $y = -2$, so distance is $f(x) - (-2) = f(x) + 2$.' },
          { text: '$f(x) + 2$', isCorrect: true, feedback: 'Correct! Distance from $(x, f(x))$ to the axis $y = -2$ is $f(x) - (-2) = f(x) + 2$.' },
          { text: '$2 - f(x)$', isCorrect: false, feedback: 'Incorrect.' },
          { text: '$\\sqrt{f(x)^2 + 4}$', isCorrect: false, feedback: 'Incorrect.' }
        ]
      }
    ],
    frqs: [
      {
        id: 'frq1',
        title: 'Question 5 (FRQ) · Dual Axis Comparison',
        stem: 'Let $R$ be the region enclosed by $y = e^x$, the line $x = 1$, and both coordinate axes.<br>(a) Find the volume $V_x$ when $R$ is revolved $360^\\circ$ about the $x$-axis. [3 marks]<br>(b) Find the volume $V_y$ when $R$ is revolved $360^\\circ$ about the $y$-axis. [4 marks]',
        markscheme: `
          <p><strong>(a) Volume around $x$-axis:</strong></p>
          $$V_x = \\pi \\int_0^1 (e^x)^2 dx = \\pi \\int_0^1 e^{2x} dx \\quad \\text{[M1]}$$
          $$V_x = \\pi \\left[ \\frac{1}{2}e^{2x} \\right]_0^1 = \\frac{\\pi}{2}(e^2 - 1) \\quad \\text{[A1][A1]}$$
          <p><strong>(b) Volume around $y$-axis:</strong></p>
          <p>The region spans $y$ from $0$ to $e$. From $y=0$ to $y=1$, it is a cylinder of radius $x=1$. From $y=1$ to $y=e$, the curve bounds it with outer radius $1$ and inner radius $x = \\ln y$ [M1]:</p>
          $$V_y = \\pi \\int_0^1 (1)^2 dy + \\pi \\int_1^e \\left( 1^2 - (\\ln y)^2 \\right) dy \\quad \\text{[M1]}$$
          $$V_1 = \\pi(1) = \\pi$$
          <p>Using $\\int (\\ln y)^2 dy = y(\\ln y)^2 - 2y\\ln y + 2y$ [M1]:</p>
          $$\\int_1^e (\\ln y)^2 dy = [e(1) - 2e(1) + 2e] - [0 - 0 + 2] = e - 2$$
          $$\\pi \\int_1^e (1 - (\\ln y)^2) dy = \\pi [ (e - 1) - (e - 2) ] = \\pi(1) = \\pi$$
          $$V_y = \\pi + \\pi = 2\\pi \\quad \\text{[A1]}$$
        `
      },
      {
        id: 'frq2',
        title: 'Question 6 (FRQ) · Architectural Dome Model',
        stem: 'An architectural dome has the shape of a solid formed by rotating $y = 6 - \\frac{x^2}{6}$ about the $y$-axis, where $x, y$ are measured in metres and $y \\ge 0$.<br>(a) Find the maximum height and the ground radius of the dome. [2 marks]<br>(b) Calculate the enclosed volume of the dome in $\\text{m}^3$. [4 marks]',
        markscheme: `
          <p><strong>(a) Dimensions:</strong></p>
          <p>At $x=0$, maximum height is $y = 6\\text{ m}$ [A1].</p>
          <p>At ground level $y=0$: $6 - \\frac{x^2}{6} = 0 \\implies x^2 = 36 \\implies x = 6\\text{ m}$ ground radius [A1].</p>
          <p><strong>(b) Volume calculation:</strong></p>
          <p>Express $x^2$ in terms of $y$:</p>
          $$\\frac{x^2}{6} = 6 - y \\implies x^2 = 6(6 - y) = 36 - 6y \\quad \\text{[M1]}$$
          <p>Integrate with respect to $y$ from $y = 0$ to $y = 6$ [M1]:</p>
          $$V = \\pi \\int_0^6 x^2 dy = \\pi \\int_0^6 (36 - 6y) dy \\quad \\text{[A1]}$$
          $$V = \\pi \\left[ 36y - 3y^2 \\right]_0^6 = \\pi [ 36(6) - 3(36) ] = \\pi [ 216 - 108 ] = 108\\pi\\text{ m}^3 \\quad \\text{[A1]}$$
          $$\\approx 339.3\\text{ m}^3$$
        `
      }
    ]
  },

  // =========================================================================
  // GUIDE 22: Maclaurin & Taylor Series
  // =========================================================================
  {
    folder: 'maclaurin-and-taylor-series',
    code: '5.18',
    title: 'Maclaurin & Taylor Series',
    pageTitle: 'Maclaurin & Taylor Series | IB Math AA HL | SJMaths',
    metaDesc: 'Master Maclaurin and Taylor series for IB DP Mathematics AA HL (Topic 5.18). Derivations, standard booklet series, polynomial expansions, indeterminate limits, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL Maclaurin series, Taylor polynomials, power series expansions, standard series formula booklet, limits using series, radius of convergence',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Approximate and represent functions as infinite power series: $f(x) = \\sum_{n=0}^\\infty \\frac{f^{(n)}(0)}{n!} x^n$, booklet series for $e^x, \\ln(1+x), \\sin x, \\cos x, \\arctan x$, series multiplication, and limit evaluation.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/volumes-of-revolution/',
      title: 'Volumes of Revolution'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/calculus/',
      title: 'Topic 5 Calculus Hub'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-wave-square" style="color:var(--c-primary);"></i> Figure 5.6: Maclaurin Polynomial Approximations Converging to sin(x)</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing Maclaurin polynomials of degree 1, 3, and 5 converging to the sine curve around x = 0">
            <!-- Axes -->
            <line x1="80" y1="140" x2="680" y2="140" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="380" y1="20" x2="380" y2="260" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="670" y="130" fill="var(--c-text)" font-size="13" font-weight="bold">x</text>
            <text x="390" y="35" fill="var(--c-text)" font-size="13" font-weight="bold">y</text>
            <text x="365" y="155" fill="var(--c-text)" font-size="12">0</text>

            <!-- Exact curve y = sin(x) (green) -->
            <path d="M 140,140 Q 200,40 260,140 T 380,140 T 500,140 T 620,140" fill="none" stroke="#10b981" stroke-width="3" />
            <text x="625" y="135" font-size="13" font-weight="bold" fill="#10b981">y = sin(x)</text>

            <!-- Degree 1: P1(x) = x (linear tangent, purple) -->
            <line x1="280" y1="240" x2="480" y2="40" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,4" />
            <text x="490" y="55" font-size="12" font-weight="bold" fill="#8b5cf6">P₁(x) = x</text>

            <!-- Degree 3: P3(x) = x - x^3/6 (blue cubic) -->
            <path d="M 240,240 Q 320,170 380,140 Q 440,110 520,40" fill="none" stroke="#3b82f6" stroke-width="2.5" />
            <text x="530" y="45" font-size="12" font-weight="bold" fill="#3b82f6">P₃(x) = x - x³/6</text>

            <!-- Expansion center point (0, 0) -->
            <circle cx="380" cy="140" r="5" fill="#ef4444" />
            <text x="395" y="160" font-size="12" font-weight="bold" fill="#ef4444">Center x = 0</text>

            <!-- General formula banner -->
            <rect x="200" y="10" width="360" height="36" rx="6" fill="var(--c-surface-raised, #f8fafc)" stroke="var(--c-border)" />
            <text x="380" y="33" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary)">f(x) = f(0) + f'(0)x + [f''(0)/2!]x² + [f'''(0)/3!]x³ + ...</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. The Maclaurin Series Definition (Topic 5.18)</h2>
        <p>A function $f(x)$ that is infinitely differentiable at $x = 0$ can be represented as a power series called its <strong>Maclaurin series</strong>:</p>
        $$f(x) = \\sum_{n=0}^\\infty \\frac{f^{(n)}(0)}{n!} \\, x^n = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\frac{f'''(0)}{3!}x^3 + \\dots$$
        <p>The polynomial formed by truncating after the $n$-th degree term is denoted $P_n(x)$ and provides a local polynomial approximation around $x = 0$.</p>

        <h2>2. Standard Series in the IB Formula Booklet</h2>
        <p>The following standard Maclaurin series are provided in the IB Mathematics AA HL Formula Booklet:</p>
        <ul style="line-height:2.2;">
          <li>$e^x = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\dots = \\sum_{n=0}^\\infty \\frac{x^n}{n!} \\quad (\\text{for all } x \\in \\mathbb{R})$</li>
          <li>$\\ln(1+x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\dots = \\sum_{n=1}^\\infty (-1)^{n-1}\\frac{x^n}{n} \\quad (-1 < x \\le 1)$</li>
          <li>$\\sin x = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\dots = \\sum_{n=0}^\\infty (-1)^n \\frac{x^{2n+1}}{(2n+1)!} \\quad (\\text{for all } x \\in \\mathbb{R})$</li>
          <li>$\\cos x = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\dots = \\sum_{n=0}^\\infty (-1)^n \\frac{x^{2n}}{(2n)!} \\quad (\\text{for all } x \\in \\mathbb{R})$</li>
          <li>$\\arctan x = x - \\frac{x^3}{3} + \\frac{x^5}{5} - \\dots = \\sum_{n=0}^\\infty (-1)^n \\frac{x^{2n+1}}{2n+1} \\quad (|x| \\le 1)$</li>
        </ul>

        <h2>3. Algebraic Operations &amp; Substitution</h2>
        <p>New series can be rapidly derived without computing higher derivatives by:</p>
        <ul>
          <li><strong>Substitution:</strong> Replace $x$ with $kx$ or $x^p$ (e.g., $e^{-x^2} = 1 - x^2 + \\frac{x^4}{2} - \\dots$).</li>
          <li><strong>Multiplication:</strong> Expand polynomials and collect terms up to the requested degree.</li>
          <li><strong>Term-by-term Differentiation &amp; Integration:</strong> $\\frac{d}{dx}[\\sum a_n x^n] = \\sum n a_n x^{n-1}$.</li>
          <li><strong>Limit Evaluation:</strong> Substitute power series into indeterminate expressions $\\lim_{x \\to 0} \\frac{f(x)}{g(x)}$ to eliminate factors of $x$.</li>
        </ul>
    `,
    exercises: [
      {
        num: 1,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Use the Maclaurin formula $f(x) = \\sum_{n=0}^\\infty \\frac{f^{(n)}(0)}{n!} x^n$ to derive the first three non-zero terms of $f(x) = \\cos(2x)$.',
        solution: `
          <p><strong>Step 1: Compute derivatives and evaluate at $x = 0$:</strong></p>
          $$f(x) = \\cos(2x) \\implies f(0) = 1$$
          $$f'(x) = -2\\sin(2x) \\implies f'(0) = 0$$
          $$f''(x) = -4\\cos(2x) \\implies f''(0) = -4$$
          $$f'''(x) = 8\\sin(2x) \\implies f'''(0) = 0$$
          $$f^{(4)}(x) = 16\\cos(2x) \\implies f^{(4)}(0) = 16$$
          <p><strong>Step 2: Assemble Maclaurin series:</strong></p>
          $$f(x) = 1 + 0x + \\frac{-4}{2!}x^2 + 0x^3 + \\frac{16}{4!}x^4 + \\dots$$
          $$f(x) = 1 - 2x^2 + \\frac{2}{3}x^4 + \\dots$$
        `
      },
      {
        num: 2,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Using the standard series for $e^u$, write down the Maclaurin expansion of $e^{-3x^2}$ up to the term in $x^4$.',
        solution: `
          <p><strong>Step 1: Standard expansion:</strong></p>
          $$e^u = 1 + u + \\frac{u^2}{2!} + \\dots$$
          <p><strong>Step 2: Substitute $u = -3x^2$:</strong></p>
          $$e^{-3x^2} = 1 + (-3x^2) + \\frac{(-3x^2)^2}{2!} + \\dots = 1 - 3x^2 + \\frac{9x^4}{2} - \\dots$$
        `
      },
      {
        num: 3,
        tier: 'Core Algorithmic',
        badgeClass: 'badge-core',
        stem: 'Find the Maclaurin series for $\\ln(1 + 2x)$ up to the term in $x^3$, and state the interval of convergence.',
        solution: `
          <p><strong>Step 1: Standard booklet series:</strong></p>
          $$\\ln(1 + u) = u - \\frac{u^2}{2} + \\frac{u^3}{3} - \\dots \\quad \\text{for } -1 < u \\le 1$$
          <p><strong>Step 2: Substitute $u = 2x$:</strong></p>
          $$\\ln(1 + 2x) = (2x) - \\frac{(2x)^2}{2} + \\frac{(2x)^3}{3} - \\dots = 2x - 2x^2 + \\frac{8}{3}x^3 - \\dots$$
          <p><strong>Step 3: Interval of convergence:</strong></p>
          $$-1 < 2x \\le 1 \\implies -\\frac{1}{2} < x \\le \\frac{1}{2}$$
        `
      },
      {
        num: 4,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Find the Maclaurin expansion of $f(x) = e^x \\sin x$ up to and including the term in $x^3$.',
        solution: `
          <p><strong>Step 1: Write series for each component up to $x^3$:</strong></p>
          $$e^x = 1 + x + \\frac{x^2}{2} + \\frac{x^3}{6} + \\dots$$
          $$\\sin x = x - \\frac{x^3}{6} + \\dots$$
          <p><strong>Step 2: Multiply and collect terms up to degree 3:</strong></p>
          $$e^x \\sin x = \\left( 1 + x + \\frac{x^2}{2} \\right) \\left( x - \\frac{x^3}{6} \\right) + \\mathcal{O}(x^4)$$
          $$= 1(x) - 1\\left(\\frac{x^3}{6}\\right) + x(x) + \\left(\\frac{x^2}{2}\\right)(x) + \\dots$$
          $$= x - \\frac{x^3}{6} + x^2 + \\frac{x^3}{2}$$
          <p>Combine $x^3$ coefficients: $-\\frac{1}{6} + \\frac{1}{2} = \\frac{2}{6} = \\frac{1}{3}$.</p>
          $$e^x \\sin x = x + x^2 + \\frac{1}{3}x^3 + \\dots$$
        `
      },
      {
        num: 5,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Use the Maclaurin series for $\\cos x$ and $e^x$ to evaluate $\\lim_{x \\to 0} \\frac{1 - \\cos(3x)}{x(e^{2x} - 1)}$.',
        solution: `
          <p><strong>Step 1: Expand numerator:</strong></p>
          $$\\cos(3x) = 1 - \\frac{(3x)^2}{2} + \\dots = 1 - \\frac{9}{2}x^2 + \\dots$$
          $$1 - \\cos(3x) = \\frac{9}{2}x^2 + \\dots$$
          <p><strong>Step 2: Expand denominator:</strong></p>
          $$e^{2x} - 1 = (1 + 2x + \\dots) - 1 = 2x + \\dots$$
          $$x(e^{2x} - 1) = x(2x + \\dots) = 2x^2 + \\dots$$
          <p><strong>Step 3: Evaluate limit:</strong></p>
          $$\\lim_{x \\to 0} \\frac{\\frac{9}{2}x^2 + \\dots}{2x^2 + \\dots} = \\frac{9/2}{2} = \\frac{9}{4}$$
        `
      },
      {
        num: 6,
        tier: 'Standard Exam',
        badgeClass: 'badge-standard',
        stem: 'Find the Taylor series of $f(x) = \\ln x$ in powers of $(x - 1)$ up to the third degree term.',
        solution: `
          <p><strong>Step 1: Evaluate derivatives at $x = 1$:</strong></p>
          $$f(1) = \\ln 1 = 0$$
          $$f'(x) = x^{-1} \\implies f'(1) = 1$$
          $$f''(x) = -x^{-2} \\implies f''(1) = -1$$
          $$f'''(x) = 2x^{-3} \\implies f'''(1) = 2$$
          <p><strong>Step 2: Apply Taylor series formula around $a = 1$:</strong></p>
          $$f(x) = f(1) + f'(1)(x-1) + \\frac{f''(1)}{2!}(x-1)^2 + \\frac{f'''(1)}{3!}(x-1)^3 + \\dots$$
          $$f(x) = 0 + 1(x-1) - \\frac{1}{2}(x-1)^2 + \\frac{2}{6}(x-1)^3 + \\dots$$
          $$f(x) = (x-1) - \\frac{1}{2}(x-1)^2 + \\frac{1}{3}(x-1)^3 - \\dots$$
        `
      },
      {
        num: 7,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'Use the first three non-zero terms of the Maclaurin series for $e^{-x^2}$ to approximate the definite integral $\\int_0^{0.5} e^{-x^2} dx$, and give your answer to 5 decimal places.',
        solution: `
          <p><strong>Step 1: Write the Maclaurin expansion of $e^{-x^2}$:</strong></p>
          $$e^{-x^2} = 1 - x^2 + \\frac{x^4}{2} - \\dots$$
          <p><strong>Step 2: Integrate term by term:</strong></p>
          $$\\int_0^{0.5} \\left( 1 - x^2 + \\frac{x^4}{2} \\right) dx = \\left[ x - \\frac{x^3}{3} + \\frac{x^5}{10} \\right]_0^{0.5}$$
          <p><strong>Step 3: Evaluate at $x = 0.5 = \\frac{1}{2}$:</strong></p>
          $$= \\frac{1}{2} - \\frac{1}{3}\\left(\\frac{1}{8}\\right) + \\frac{1}{10}\\left(\\frac{1}{32}\\right) = \\frac{1}{2} - \\frac{1}{24} + \\frac{1}{320}$$
          $$= 0.5 - 0.041667 + 0.003125 = 0.461458 \\dots \\approx 0.46146$$
        `
      },
      {
        num: 8,
        tier: 'Extended Problem',
        badgeClass: 'badge-extended',
        stem: 'Given that $y = f(x)$ satisfies the differential equation $\\frac{dy}{dx} = x^2 + y^2$ with initial condition $y(0) = 1$, find the Maclaurin series for $y$ up to the term in $x^3$.',
        solution: `
          <p><strong>Step 1: Initial values:</strong></p>
          $$y(0) = 1$$
          $$y'(0) = 0^2 + (y(0))^2 = 0 + 1^2 = 1$$
          <p><strong>Step 2: Differentiate implicitly to find higher derivatives:</strong></p>
          $$y'' = \\frac{d}{dx}[x^2 + y^2] = 2x + 2y y'$$
          $$y''(0) = 2(0) + 2(1)(1) = 2$$
          <p><strong>Step 3: Third derivative:</strong></p>
          $$y''' = \\frac{d}{dx}[2x + 2y y'] = 2 + 2(y')^2 + 2y y''$$
          $$y'''(0) = 2 + 2(1)^2 + 2(1)(2) = 2 + 2 + 4 = 8$$
          <p><strong>Step 4: Assemble series:</strong></p>
          $$y(x) = y(0) + y'(0)x + \\frac{y''(0)}{2!}x^2 + \\frac{y'''(0)}{3!}x^3 + \\dots$$
          $$y(x) = 1 + x + \\frac{2}{2}x^2 + \\frac{8}{6}x^3 + \\dots = 1 + x + x^2 + \\frac{4}{3}x^3 + \\dots$$
        `
      },
      {
        num: 9,
        tier: 'HL Distinction',
        badgeClass: 'badge-hl',
        stem: 'By substituting $x = i\\theta$ into the Maclaurin expansion of $e^x$, separate the real and imaginary parts to prove Euler’s formula: $e^{i\\theta} = \\cos\\theta + i\\sin\\theta$.',
        solution: `
          <p><strong>Step 1: Expand $e^{i\\theta}$ using the standard series:</strong></p>
          $$e^{i\\theta} = 1 + (i\\theta) + \\frac{(i\\theta)^2}{2!} + \\frac{(i\\theta)^3}{3!} + \\frac{(i\\theta)^4}{4!} + \\frac{(i\\theta)^5}{5!} + \\dots$$
          <p><strong>Step 2: Simplify powers of $i$:</strong></p>
          <p>$i^1 = i, \\, i^2 = -1, \\, i^3 = -i, \\, i^4 = 1, \\, i^5 = i, \\dots$</p>
          $$e^{i\\theta} = 1 + i\\theta - \\frac{\\theta^2}{2!} - i\\frac{\\theta^3}{3!} + \\frac{\\theta^4}{4!} + i\\frac{\\theta^5}{5!} - \\dots$$
          <p><strong>Step 3: Group into real and imaginary components:</strong></p>
          $$\\text{Re} = 1 - \\frac{\\theta^2}{2!} + \\frac{\\theta^4}{4!} - \\dots = \\cos\\theta$$
          $$\\text{Im} = \\theta - \\frac{\\theta^3}{3!} + \\frac{\\theta^5}{5!} - \\dots = \\sin\\theta$$
          $$e^{i\\theta} = \\cos\\theta + i\\sin\\theta \\quad \\blacksquare$$
        `
      },
      {
        num: 10,
        tier: 'HL Distinction',
        badgeClass: 'badge-hl',
        stem: 'Show that the Maclaurin series for $\\sec x$ up to $x^4$ is $1 + \\frac{1}{2}x^2 + \\frac{5}{24}x^4 + \\dots$ by performing long division of series $\\frac{1}{\\cos x}$ or using the identity $\\sec x \\cos x = 1$.',
        solution: `
          <p><strong>Step 1: Write $\\cos x$ and let $\\sec x = a_0 + a_2 x^2 + a_4 x^4 + \\dots$:</strong></p>
          <p>Since $\\sec x$ is an even function, all odd-degree terms vanish.</p>
          $$\\cos x = 1 - \\frac{x^2}{2} + \\frac{x^4}{24} - \\dots$$
          <p><strong>Step 2: Multiply series and set equal to 1:</strong></p>
          $$\\left( a_0 + a_2 x^2 + a_4 x^4 + \\dots \\right) \\left( 1 - \\frac{x^2}{2} + \\frac{x^4}{24} - \\dots \\right) = 1$$
          <p><strong>Step 3: Equate coefficients of powers of $x$:</strong></p>
          <p>Constant term: $a_0 \\cdot 1 = 1 \\implies a_0 = 1$</p>
          <p>$x^2$ coefficient: $a_2 - \\frac{1}{2}a_0 = 0 \\implies a_2 = \\frac{1}{2}(1) = \\frac{1}{2}$</p>
          <p>$x^4$ coefficient: $a_4 - \\frac{1}{2}a_2 + \\frac{1}{24}a_0 = 0$</p>
          $$a_4 = \\frac{1}{2}a_2 - \\frac{1}{24}a_0 = \\frac{1}{2}\\left(\\frac{1}{2}\\right) - \\frac{1}{24}(1) = \\frac{1}{4} - \\frac{1}{24} = \\frac{6 - 1}{24} = \\frac{5}{24}$$
          <p><strong>Step 4: Final expansion:</strong></p>
          $$\\sec x = 1 + \\frac{1}{2}x^2 + \\frac{5}{24}x^4 + \\dots \\quad \\blacksquare$$
        `
      }
    ],
    formulasHtml: `
        <h2>Topic 5.18 Formula Booklet Reference</h2>
        <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem; margin-bottom:1.5rem;">
          <h3 style="margin-top:0; color:var(--c-primary);"><i class="fa-solid fa-book-bookmark"></i> Official IB Formula Booklet Entries</h3>
          <ul style="line-height:2.2;">
            <li><strong>Maclaurin Series:</strong> $f(x) = f(0) + f'(0)x + \\frac{f''(0)}{2!}x^2 + \\dots = \\sum_{n=0}^\\infty \\frac{f^{(n)}(0)}{n!}x^n$</li>
            <li><strong>Taylor Series about x = a:</strong> $f(x) = f(a) + f'(a)(x-a) + \\frac{f''(a)}{2!}(x-a)^2 + \\dots$</li>
            <li>$e^x = 1 + x + \\frac{x^2}{2!} + \\dots$</li>
            <li>$\\ln(1+x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\dots \\quad (|x| < 1)$</li>
            <li>$\\sin x = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\dots$</li>
            <li>$\\cos x = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\dots$</li>
            <li>$\\arctan x = x - \\frac{x^3}{3} + \\frac{x^5}{5} - \\dots \\quad (|x| \\le 1)$</li>
          </ul>
        </div>

        <h2>Essential Pitfalls &amp; Strategy Cards</h2>
        <div class="grid grid-2" style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1.25rem;">
          <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem;">
            <h4 style="margin-top:0; color:#ef4444;"><i class="fa-solid fa-triangle-exclamation"></i> Pitfall: Factorial vs Constant Denominators</h4>
            <p>Notice that the series for $\\sin x, \\cos x$, and $e^x$ have factorials in the denominators ($3! = 6, 4! = 24$), whereas $\\ln(1+x)$ and $\\arctan x$ have plain integers ($2, 3, 4, 5$). Confusing these is a frequent loss of marks.</p>
          </div>
          <div class="formula-card" style="background:var(--c-surface); border:1px solid var(--c-border); border-radius:12px; padding:1.25rem;">
            <h4 style="margin-top:0; color:#f59e0b;"><i class="fa-solid fa-triangle-exclamation"></i> Pitfall: Valid Range of Convergence</h4>
            <p>The expansions for $\\ln(1+x)$ and $\\arctan x$ are only valid when $|x| \\le 1$. If asked for $\\ln(3+x)$, factor out 3 first: $\\ln 3 + \\ln(1 + x/3)$, with $|x/3| < 1$.</p>
          </div>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        stem: 'What is the coefficient of $x^3$ in the Maclaurin expansion of $f(x) = \\sin(2x)$?',
        options: [
          { text: '$-\\frac{1}{6}$', isCorrect: false, feedback: 'Incorrect. Remember to replace $x$ with $2x$: $\\frac{(2x)^3}{3!} = \\frac{8x^3}{6}$.' },
          { text: '$-\\frac{4}{3}$', isCorrect: true, feedback: 'Correct! $\\sin(2x) = (2x) - \\frac{(2x)^3}{3!} + \\dots = 2x - \\frac{8}{6}x^3 = 2x - \\frac{4}{3}x^3$.' },
          { text: '$\\frac{4}{3}$', isCorrect: false, feedback: 'Incorrect. The sign in the sine expansion alternates: $+ - + -$.' },
          { text: '$-\\frac{8}{3}$', isCorrect: false, feedback: 'Incorrect. $3! = 6$, not $3$.' }
        ]
      },
      {
        id: 'q2',
        stem: 'What is the value of $\\lim_{x \\to 0} \\frac{e^{x^2} - 1 - x^2}{x^4}$ evaluated using series expansions?',
        options: [
          { text: '0', isCorrect: false, feedback: 'Incorrect.' },
          { text: '1', isCorrect: false, feedback: 'Incorrect.' },
          { text: '$\\frac{1}{2}$', isCorrect: true, feedback: 'Correct! $e^{x^2} = 1 + x^2 + \\frac{(x^2)^2}{2!} + \\dots = 1 + x^2 + \\frac{1}{2}x^4$. Subtracting $1 + x^2$ leaves $\\frac{1}{2}x^4$, so the limit is $\\frac{1}{2}$.' },
          { text: '$\\frac{1}{4}$', isCorrect: false, feedback: 'Incorrect. $2! = 2$.' }
        ]
      },
      {
        id: 'q3',
        stem: 'Which function has the Maclaurin series $\\sum_{n=0}^\\infty (-1)^n x^{2n} = 1 - x^2 + x^4 - x^6 + \\dots$ for $|x| < 1$?',
        options: [
          { text: '$\\cos x$', isCorrect: false, feedback: 'Incorrect. $\\cos x$ has factorials in denominators.' },
          { text: '$\\frac{1}{1 + x^2}$', isCorrect: true, feedback: 'Correct! By the geometric series $\\frac{1}{1 - r} = \\sum r^n$ with $r = -x^2$.' },
          { text: '$\\arctan x$', isCorrect: false, feedback: 'Incorrect. $\\arctan x = \\int \\frac{1}{1+x^2}dx = x - \\frac{x^3}{3} + \\dots$.' },
          { text: '$\\frac{1}{1 - x^2}$', isCorrect: false, feedback: 'Incorrect. That would have all positive signs.' }
        ]
      },
      {
        id: 'q4',
        stem: 'If $P_2(x) = 3 - 4x + 5x^2$ is the second-degree Maclaurin polynomial for $f(x)$, what is $f\'\'(0)$?',
        options: [
          { text: '5', isCorrect: false, feedback: 'Incorrect. In $P_2(x)$, the coefficient of $x^2$ is $\\frac{f\'\'(0)}{2!}$.' },
          { text: '10', isCorrect: true, feedback: 'Correct! $\\frac{f\'\'(0)}{2!} = 5 \\implies f\'\'(0) = 5 \\times 2 = 10$.' },
          { text: '2.5', isCorrect: false, feedback: 'Incorrect.' },
          { text: '-4', isCorrect: false, feedback: 'Incorrect. $-4$ is $f\'(0)$.' }
        ]
      }
    ],
    frqs: [
      {
        id: 'frq1',
        title: 'Question 5 (FRQ) · Series Expansion and Definite Integration',
        stem: 'Let $f(x) = \\frac{\\sin x}{x}$ for $x \\ne 0$, and $f(0) = 1$.<br>(a) Write down the Maclaurin expansion of $f(x)$ up to the term in $x^4$. [2 marks]<br>(b) Hence, approximate $\\int_0^1 \\frac{\\sin x}{x} dx$ using these terms. [3 marks]<br>(c) Explain why this approximation is strictly an overestimate or underestimate. [2 marks]',
        markscheme: `
          <p><strong>(a) Series expansion:</strong></p>
          $$\\sin x = x - \\frac{x^3}{6} + \\frac{x^5}{120} - \\dots \\quad \\text{[M1]}$$
          $$f(x) = \\frac{\\sin x}{x} = 1 - \\frac{x^2}{6} + \\frac{x^4}{120} - \\dots \\quad \\text{[A1]}$$
          <p><strong>(b) Integrate term by term:</strong></p>
          $$\\int_0^1 \\left( 1 - \\frac{x^2}{6} + \\frac{x^4}{120} \\right) dx = \\left[ x - \\frac{x^3}{18} + \\frac{x^5}{600} \\right]_0^1 \\quad \\text{[M1][A1]}$$
          $$= 1 - \\frac{1}{18} + \\frac{1}{600} = 1 - 0.055556 + 0.001667 \\approx 0.94611 \\quad \\text{[A1]}$$
          <p><strong>(c) Alternating series remainder:</strong></p>
          <p>The series is an alternating series with monotonically decreasing terms. The next omitted term is negative ($-\\int_0^1 \\frac{x^6}{5040}dx = -\\frac{1}{35280}$), so the truncated sum is an <strong>overestimate</strong> [R1][A1].</p>
        `
      },
      {
        id: 'frq2',
        title: 'Question 6 (FRQ) · Limit Evaluation and Differential Equation',
        stem: 'Consider the function $g(x) = \\ln(1 + x) - x\\cos x$.<br>(a) Find the Maclaurin expansion of $g(x)$ up to the term in $x^3$. [4 marks]<br>(b) Hence, determine the value of $\\lim_{x \\to 0} \\frac{g(x)}{x^3}$. [3 marks]',
        markscheme: `
          <p><strong>(a) Maclaurin series for each term:</strong></p>
          $$\\ln(1+x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\dots \\quad \\text{[M1][A1]}$$
          $$\\cos x = 1 - \\frac{x^2}{2} + \\dots \\implies x\\cos x = x - \\frac{x^3}{2} + \\dots \\quad \\text{[M1]}$$
          $$g(x) = \\left( x - \\frac{x^2}{2} + \\frac{x^3}{3} \\right) - \\left( x - \\frac{x^3}{2} \\right) + \\dots$$
          $$g(x) = -\\frac{1}{2}x^2 + \\left( \\frac{1}{3} + \\frac{1}{2} \\right)x^3 + \\dots = -\\frac{1}{2}x^2 + \\frac{5}{6}x^3 + \\dots \\quad \\text{[A1]}$$
          <p><strong>(b) Limit calculation:</strong></p>
          <p>Notice the lowest degree non-zero term in $g(x)$ is $-\\frac{1}{2}x^2$:</p>
          $$\\frac{g(x)}{x^3} = \\frac{-\\frac{1}{2}x^2 + \\frac{5}{6}x^3 + \\dots}{x^3} = -\\frac{1}{2x} + \\frac{5}{6} + \\dots \\quad \\text{[M1]}$$
          <p>As $x \\to 0$, $-\\frac{1}{2x} \\to \\pm\\infty$, so the two-sided limit <strong>does not exist</strong> (diverges) [A2].</p>
          <p><em>(Note: if evaluating $\\lim_{x \\to 0} \\frac{g(x)}{x^2}$, the limit would be $-\\frac{1}{2}$.)</em></p>
        `
      }
    ]
  }
];

function generateHtml(guide) {
  const exercisesMarkup = guide.exercises.map(ex => `
        <article class="exercise-item" id="ex-${ex.num}">
          <div class="exercise-header">
            <span class="exercise-badge ${ex.badgeClass}">${ex.tier}</span>
            <span class="exercise-number">Exercise ${ex.num}</span>
          </div>
          <div class="exercise-stem">
            <p>${ex.stem}</p>
          </div>
          <details class="solution-details">
            <summary class="solution-toggle">
              <span>View Full Algebraic Solution</span>
              <i class="fa-solid fa-chevron-down" aria-hidden="true"></i>
            </summary>
            <div class="solution-content">
              ${ex.solution}
            </div>
          </details>
        </article>
  `).join('\n');

  const mcqsMarkup = guide.mcqs.map((mcq, idx) => `
        <div class="quiz-question-card" id="quiz-${mcq.id}" data-correct="${mcq.options.findIndex(o => o.isCorrect)}">
          <div class="quiz-question-header">
            <span class="badge badge-core">Question ${idx + 1} of 4</span>
            <span class="quiz-points">1 Mark</span>
          </div>
          <p class="quiz-stem">${mcq.stem}</p>
          <div class="quiz-options-group">
            ${mcq.options.map((opt, optIdx) => `
              <label class="quiz-option-label" for="${mcq.id}-opt-${optIdx}">
                <input type="radio" name="${mcq.id}" id="${mcq.id}-opt-${optIdx}" value="${optIdx}">
                <span class="quiz-option-text">${opt.text}</span>
              </label>
            `).join('')}
          </div>
          <div class="quiz-feedback-box" id="${mcq.id}-feedback" style="display:none; margin-top:12px; padding:12px; border-radius:8px;">
            ${mcq.options.map((opt, optIdx) => `
              <div class="option-feedback" data-opt="${optIdx}" style="display:none;">
                <strong>${opt.isCorrect ? '✓ Correct:' : '✗ Incorrect:'}</strong> ${opt.feedback}
              </div>
            `).join('')}
          </div>
        </div>
  `).join('\n');

  const frqsMarkup = guide.frqs.map(frq => `
        <article class="exercise-item" id="${frq.id}">
          <div class="exercise-header">
            <span class="exercise-badge badge-hl">Examination Paper 1/2</span>
            <span class="exercise-number">${frq.title}</span>
          </div>
          <div class="exercise-stem">
            <p>${frq.stem}</p>
          </div>
          <details class="solution-details">
            <summary class="solution-toggle">
              <span>View Official IB Markscheme</span>
              <i class="fa-solid fa-chevron-down" aria-hidden="true"></i>
            </summary>
            <div class="solution-content">
              ${frq.markscheme}
            </div>
          </details>
        </article>
  `).join('\n');

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${guide.pageTitle}</title>
  <meta name="description" content="${guide.metaDesc}">
  <meta name="keywords" content="${guide.keywords}">
  <meta name="author" content="Sandeep Jaiswal">
  <link rel="canonical" href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/">

  <!-- Open Graph -->
  <meta property="og:title" content="${guide.pageTitle}">
  <meta property="og:description" content="${guide.metaDesc}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/calculus/${guide.folder}/">

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
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/calculus/">Calculus</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
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
          <i class="fa-solid fa-pen-to-square" aria-hidden="true"></i> 2. Practice Exercises
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
