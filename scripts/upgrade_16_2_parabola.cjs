const fs = require('fs');
const cheerio = require('cheerio');

const filePath = 'class-11-applied-mathematics/chapter-16-circle-and-parabola/16-2-parabola/index.html';
const rawHtml = fs.readFileSync(filePath, 'utf8');
const $ = cheerio.load(rawHtml);

// 1. LEARN TAB
const learnContent = `
<h2>1. Fundamental Conic Definition of a Parabola</h2>
<p>In analytical geometry, a <strong>parabola</strong> is defined as the locus of a point $P(x, y)$ that moves in a plane such that its distance from a fixed point $S$ (called the <strong>focus</strong>) is strictly equal to its perpendicular distance from a fixed straight line $L$ (called the <strong>directrix</strong>).</p>

<div class="formula-card">
  <div class="formula-title">Conic Ratio and Eccentricity Condition</div>
  $$\\frac{SP}{PM} = e = 1 \\implies SP = PM$$
  <p>Where:</p>
  <ul>
    <li>$S$ is the fixed focus.</li>
    <li>$M$ is the foot of the perpendicular drawn from moving point $P$ to the directrix line $L$.</li>
    <li>$e = 1$ is the <strong>eccentricity</strong> characteristic of all parabolas.</li>
  </ul>
</div>

<p><strong>Key Structural Terminology:</strong></p>
<ul>
  <li><strong>Axis of the Parabola:</strong> The straight line passing through the focus perpendicular to the directrix. The parabola is completely symmetrical about its axis.</li>
  <li><strong>Vertex ($V$):</strong> The point of intersection of the parabola with its axis. The vertex is the exact midpoint between the focus $S$ and the directrix.</li>
  <li><strong>Focal Chord:</strong> Any line segment passing through the focus and having both its endpoints on the parabola.</li>
  <li><strong>Latus Rectum:</strong> The specific focal chord drawn perpendicular to the axis of the parabola.</li>
  <li><strong>Double Ordinate:</strong> Any chord drawn perpendicular to the axis of symmetry.</li>
</ul>

<h2>2. Four Standard Orientations of a Parabola</h2>
<p>When the vertex is located at the origin $O(0, 0)$ and the axis coincides with one of the coordinate axes, parabolas assume four canonical equations depending on their orientation:</p>

<div class="table-responsive">
  <table class="table-comparison">
    <thead>
      <tr>
        <th>Characteristic</th>
        <th>Rightward ($y^2 = 4ax$)</th>
        <th>Leftward ($y^2 = -4ax$)</th>
        <th>Upward ($x^2 = 4ay$)</th>
        <th>Downward ($x^2 = -4ay$)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Orientation</strong></td>
        <td>Opens towards $+x$</td>
        <td>Opens towards $-x$</td>
        <td>Opens towards $+y$</td>
        <td>Opens towards $-y$</td>
      </tr>
      <tr>
        <td><strong>Focus ($S$)</strong></td>
        <td>$(a, 0)$</td>
        <td>$(-a, 0)$</td>
        <td>$(0, a)$</td>
        <td>$(0, -a)$</td>
      </tr>
      <tr>
        <td><strong>Directrix Equation</strong></td>
        <td>$x = -a$ ($x + a = 0$)</td>
        <td>$x = a$ ($x - a = 0$)</td>
        <td>$y = -a$ ($y + a = 0$)</td>
        <td>$y = a$ ($y - a = 0$)</td>
      </tr>
      <tr>
        <td><strong>Axis of Symmetry</strong></td>
        <td>$y = 0$ (x-axis)</td>
        <td>$y = 0$ (x-axis)</td>
        <td>$x = 0$ (y-axis)</td>
        <td>$x = 0$ (y-axis)</td>
      </tr>
      <tr>
        <td><strong>Vertex ($V$)</strong></td>
        <td>$(0, 0)$</td>
        <td>$(0, 0)$</td>
        <td>$(0, 0)$</td>
        <td>$(0, 0)$</td>
      </tr>
      <tr>
        <td><strong>Length of Latus Rectum</strong></td>
        <td>$4a$</td>
        <td>$4a$</td>
        <td>$4a$</td>
        <td>$4a$</td>
      </tr>
      <tr>
        <td><strong>Latus Rectum Endpoints</strong></td>
        <td>$(a, \\pm 2a)$</td>
        <td>$(-a, \\pm 2a)$</td>
        <td>$(\\pm 2a, a)$</td>
        <td>$(\\pm 2a, -a)$</td>
      </tr>
      <tr>
        <td><strong>Focal Distance of $P(x_1, y_1)$</strong></td>
        <td>$x_1 + a$</td>
        <td>$a - x_1$</td>
        <td>$y_1 + a$</td>
        <td>$a - y_1$</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="callout tip">
  <strong>Parameter Convention ($a &gt; 0$):</strong> The constant $a$ represents the physical geometric distance from the vertex to the focus, and identically from the vertex to the directrix. Hence, $a$ is always positive. The total distance between the focus and directrix is $2a$.
</div>

<h2>3. Step-by-Step Worked Examples</h2>

<div class="example-card">
  <div class="example-title">Example 1: Parameter Identification from Standard Equation</div>
  <p><strong>Problem:</strong> Find the coordinates of the focus, equation of the directrix, axis of symmetry, and length of the latus rectum for the parabola $x^2 = -12y$.</p>
  <p><strong>Solution:</strong></p>
  <ol>
    <li>Comparing with standard form $x^2 = -4ay$:
      $$4a = 12 \\implies a = 3$$
    </li>
    <li>Since the equation has $x^2$ and a negative linear term in $y$, this is a downward-opening parabola symmetric about the y-axis.</li>
    <li><strong>Focus:</strong> $(0, -a) = (0, -3)$.</li>
    <li><strong>Directrix:</strong> $y = a \\implies y = 3$ (or $y - 3 = 0$).</li>
    <li><strong>Axis of Symmetry:</strong> $x = 0$ (the y-axis).</li>
    <li><strong>Length of Latus Rectum:</strong> $4a = 12\\text{ units}$.</li>
  </ol>
</div>

<div class="example-card">
  <div class="example-title">Example 2: Determining Equation from Vertex and a Boundary Point</div>
  <p><strong>Problem:</strong> A parabola has its vertex at the origin $(0, 0)$, its axis along the x-axis, and its curve passes through the coordinate point $(3, -6)$. Find its Cartesian equation and focus.</p>
  <p><strong>Solution:</strong></p>
  <ol>
    <li>Since the axis is along the x-axis, the equation is of the form $y^2 = 4ax$ or $y^2 = -4ax$.</li>
    <li>The point $(3, -6)$ has a positive x-coordinate ($x = 3 &gt; 0$). Hence, the parabola opens towards the positive x-axis:
      $$y^2 = 4ax$$
    </li>
    <li>Substitute $(3, -6)$ into the equation:
      $$(-6)^2 = 4a(3) \\implies 36 = 12a \\implies a = 3$$
    </li>
    <li>Equation of the parabola:
      $$y^2 = 4(3)x \\implies y^2 = 12x$$
    </li>
    <li>Focus is located at $(a, 0) = (3, 0)$.</li>
  </ol>
</div>

<div class="example-card">
  <div class="example-title">Example 3: Applied Real-World Case Study &mdash; Parabolic Solar Thermal Collector</div>
  <p><strong>Problem:</strong> An industrial thermal engineering company designs a parabolic trough collector to concentrate incident solar radiation onto a central fluid pipe. The parabolic reflector has an aperture diameter of $4\\text{ meters}$ across its rim and a central depth of $1\\text{ meter}$.</p>
  <p>(a) Determine the Cartesian equation of the parabolic profile placing the vertex at the origin.<br>
  (b) At what exact distance from the vertex should the heat-absorbing pipe (focus) be mounted to maximize concentrated thermal absorption?</p>
  <p><strong>Solution:</strong></p>
  <ol>
    <li><strong>Model Formulation:</strong><br>
      Let the vertex be at $V(0, 0)$ and orient the parabola opening upward along the y-axis: $x^2 = 4ay$.<br>
      The aperture width is $4\\text{ m}$, spanning horizontally from $x = -2$ to $x = +2$.<br>
      At the outer rim ($x = 2$), the depth is $y = 1\\text{ m}$. Thus, point $(2, 1)$ lies on the parabola.
    </li>
    <li><strong>Calculating Focal Parameter $a$:</strong><br>
      Substitute $(2, 1)$ into $x^2 = 4ay$:
      $$2^2 = 4a(1) \\implies 4 = 4a \\implies a = 1\\text{ meter}$$
    </li>
    <li><strong>Parabolic Equation:</strong><br>
      $$x^2 = 4(1)y \\implies x^2 = 4y$$
    </li>
    <li><strong>Placement of Absorber Pipe:</strong><br>
      The reflective property of parabolas ensures that all incoming parallel rays of sunlight reflect directly through the focus $S(0, a) = (0, 1)$.<br>
      Therefore, the heat absorber pipe must be positioned exactly <strong>$1\\text{ meter}$ above the vertex</strong> (level with the outer rim plane).
    </li>
  </ol>
</div>
`;

// 2. PROGRESS TAB
const progressContent = `
<h2>Progress Check & Skill Assessment</h2>
<p>Solve these structured exercises to test your mastery of focal geometry, directrix equations, and applied parabolic designs.</p>

<div class="exercise-tier">
  <div class="tier-badge tier-foundation">Tier 1: Foundations & Parameter Derivation</div>
  <div class="exercise-item">
    <p><strong>Problem 1:</strong> Find the focus, vertex, directrix, and latus rectum of the parabola $y^2 = 20x$.</p>
    <details>
      <summary>View Complete Solution</summary>
      <p>Comparing with $y^2 = 4ax$: $4a = 20 \\implies a = 5$.</p>
      <ul>
        <li>Vertex: $(0, 0)$</li>
        <li>Focus: $(a, 0) = (5, 0)$</li>
        <li>Directrix: $x = -a \\implies x = -5$ (or $x + 5 = 0$)</li>
        <li>Length of Latus Rectum: $4a = 20\\text{ units}$</li>
      </ul>
    </details>
  </div>
  <div class="exercise-item">
    <p><strong>Problem 2:</strong> Find the equation of the parabola with focus at $(0, -4)$ and directrix $y = 4$.</p>
    <details>
      <summary>View Complete Solution</summary>
      <p>The focus lies on the negative y-axis at $(0, -a) = (0, -4) \\implies a = 4$.</p>
      <p>The directrix is $y = a = 4$.</p>
      <p>This corresponds to a downward-opening vertical parabola: $x^2 = -4ay$.</p>
      <p>Equation: $x^2 = -4(4)y \\implies x^2 = -16y$.</p>
    </details>
  </div>
</div>

<div class="exercise-tier">
  <div class="tier-badge tier-intermediate">Tier 2: Geometric & Focal Distance Analysis</div>
  <div class="exercise-item">
    <p><strong>Problem 3:</strong> Find the coordinates of a point on the parabola $y^2 = 8x$ whose focal distance is $6\\text{ units}$.</p>
    <details>
      <summary>View Complete Solution</summary>
      <p>$4a = 8 \\implies a = 2$.</p>
      <p>For $y^2 = 4ax$, the focal distance of any point $P(x, y)$ is given by $x + a$.</p>
      <p>$$x + a = 6 \\implies x + 2 = 6 \\implies x = 4$$</p>
      <p>Substitute $x = 4$ into $y^2 = 8x$:</p>
      <p>$$y^2 = 8(4) = 32 \\implies y = \\pm \\sqrt{32} = \\pm 4\\sqrt{2}$$</p>
      <p>The required points are $(4, 4\\sqrt{2})$ and $(4, -4\\sqrt{2})$.</p>
    </details>
  </div>
  <div class="exercise-item">
    <p><strong>Problem 4:</strong> Find the coordinates of the endpoints of the latus rectum for $x^2 = 12y$.</p>
    <details>
      <summary>View Complete Solution</summary>
      <p>$4a = 12 \\implies a = 3$. Focus is $(0, 3)$.</p>
      <p>The latus rectum is the horizontal line $y = 3$.</p>
      <p>Substituting $y = 3$: $x^2 = 12(3) = 36 \\implies x = \\pm 6$.</p>
      <p>Endpoints are $(-6, 3)$ and $(6, 3)$. Distance between them $= 6 - (-6) = 12 = 4a$.</p>
    </details>
  </div>
</div>

<div class="exercise-tier">
  <div class="tier-badge tier-advanced">Tier 3: Applied Structural & Engineering Models</div>
  <div class="exercise-item">
    <p><strong>Problem 5:</strong> A suspension bridge cable hangs in a parabolic arc between two towers $120\\text{ m}$ apart. The top of each tower is $30\\text{ m}$ above the road deck, and the lowest point of the cable is $6\\text{ m}$ above the road deck. Taking the origin at the vertex (lowest point of the cable), determine the height of the cable at a horizontal distance of $30\\text{ m}$ from the center.</p>
    <details>
      <summary>View Complete Solution</summary>
      <p>Let vertex be $V(0, 0)$ and parabola equation be $x^2 = 4ay$.</p>
      <p>The span is $120\\text{ m}$, so towers are at $x = \\pm 60\\text{ m}$.</p>
      <p>Height of tower above lowest point: $y = 30 - 6 = 24\\text{ m}$.</p>
      <p>Point on cable: $(60, 24)$. Substitute: $60^2 = 4a(24) \\implies 3600 = 96a \\implies 4a = \\frac{3600}{24} = 150$.</p>
      <p>Parabolic equation: $x^2 = 150y \\implies y = \\frac{x^2}{150}$.</p>
      <p>At $x = 30\\text{ m}$: $y = \\frac{30^2}{150} = \\frac{900}{150} = 6\\text{ m}$.</p>
      <p>Total height above the road deck: $6\\text{ m (cable height above vertex)} + 6\\text{ m (vertex height above road)} = 12\\text{ meters}$.</p>
    </details>
  </div>
</div>
`;

// 3. WORKSHEET TAB
const worksheetContent = `
<h2>Comprehensive Practice Worksheet</h2>
<p>Work through these rigorous problems on parabolic geometry and standard properties.</p>

<div class="exercise-item">
  <p><strong>1.</strong> For the parabola $y^2 = -8x$, determine: (a) focus, (b) equation of directrix, (c) axis, (d) length of latus rectum.</p>
  <details>
    <summary>Show Solution</summary>
    <p>$4a = 8 \\implies a = 2$. Opens leftward.</p>
    <p>(a) Focus: $(-2, 0)$<br>
    (b) Directrix: $x = 2$ ($x - 2 = 0$)<br>
    (c) Axis: $y = 0$ (x-axis)<br>
    (d) Length of latus rectum: $4a = 8\\text{ units}$.</p>
  </details>
</div>

<div class="exercise-item">
  <p><strong>2.</strong> Find the equation of the parabola whose vertex is $(0, 0)$, axis is along the y-axis, and which passes through the point $(-4, -2)$.</p>
  <details>
    <summary>Show Solution</summary>
    <p>Since the axis is along the y-axis and $y = -2 &lt; 0$, the parabola opens downward: $x^2 = -4ay$.</p>
    <p>Substitute $(-4, -2)$: $(-4)^2 = -4a(-2) \\implies 16 = 8a \\implies a = 2$.</p>
    <p>Equation: $x^2 = -8y$.</p>
  </details>
</div>

<div class="exercise-item">
  <p><strong>3.</strong> Prove that the area of the triangle formed by the vertex and the two endpoints of the latus rectum of the parabola $y^2 = 4ax$ is $2a^2$.</p>
  <details>
    <summary>Show Solution</summary>
    <p>The vertex is $V(0, 0)$.</p>
    <p>The endpoints of the latus rectum are $L_1(a, 2a)$ and $L_2(a, -2a)$.</p>
    <p>Base of the triangle is the latus rectum: length $= 2a - (-2a) = 4a$.</p>
    <p>Height is the horizontal distance from the vertex $(0, 0)$ to the focus $(a, 0)$, which is $a$.</p>
    <p>$$\\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 4a \\times a = 2a^2\\text{ sq units}$$</p>
  </details>
</div>

<div class="exercise-item">
  <p><strong>4.</strong> An arch is in the form of a parabola with vertical axis. The arch is $10\\text{ m}$ high and $5\\text{ m}$ wide at the base. How wide is it at a height of $2\\text{ m}$ from the vertex (top)?</p>
  <details>
    <summary>Show Solution</summary>
    <p>Place vertex at origin $(0, 0)$ with axis vertical downwards: $x^2 = -4ay$.</p>
    <p>At the base, $y = -10\\text{ m}$, width is $5\\text{ m}$ ($x = \\pm 2.5$).</p>
    <p>$(2.5)^2 = -4a(-10) \\implies 6.25 = 40a \\implies 4a = \\frac{6.25}{10} = 0.625$.</p>
    <p>Equation: $x^2 = 0.625(-y)$.</p>
    <p>At $2\\text{ m}$ below vertex ($y = -2$): $x^2 = 0.625(2) = 1.25 \\implies x = \\sqrt{1.25} \\approx 1.118\\text{ m}$.</p>
    <p>Total width $= 2x = 2(1.118) \\approx 2.24\\text{ meters}$.</p>
  </details>
</div>
`;

// 4. REVISION TAB
const revisionContent = `
<h2>Quick Reference & High-Yield Summary</h2>

<div class="table-responsive">
  <table class="table-comparison">
    <thead>
      <tr>
        <th>Equation</th>
        <th>Axis</th>
        <th>Focus</th>
        <th>Directrix</th>
        <th>Latus Rectum</th>
        <th>Focal Length ($SP$)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>$y^2 = 4ax$</td>
        <td>$y = 0$ (x-axis)</td>
        <td>$(a, 0)$</td>
        <td>$x = -a$</td>
        <td>$4a$</td>
        <td>$x_1 + a$</td>
      </tr>
      <tr>
        <td>$y^2 = -4ax$</td>
        <td>$y = 0$ (x-axis)</td>
        <td>$(-a, 0)$</td>
        <td>$x = a$</td>
        <td>$4a$</td>
        <td>$a - x_1$</td>
      </tr>
      <tr>
        <td>$x^2 = 4ay$</td>
        <td>$x = 0$ (y-axis)</td>
        <td>$(0, a)$</td>
        <td>$y = -a$</td>
        <td>$4a$</td>
        <td>$y_1 + a$</td>
      </tr>
      <tr>
        <td>$x^2 = -4ay$</td>
        <td>$x = 0$ (y-axis)</td>
        <td>$(0, -a)$</td>
        <td>$y = a$</td>
        <td>$4a$</td>
        <td>$a - y_1$</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="callout tip">
  <strong>High-Yield Exam Reminders:</strong>
  <ul>
    <li><strong>Eccentricity:</strong> For any parabola, $e = 1$ unconditionally.</li>
    <li><strong>Vertex is Midpoint:</strong> The vertex $(0, 0)$ always bisects the distance between the focus and the foot of the directrix on the axis.</li>
    <li><strong>Optical Property:</strong> Any ray originating from the focus and striking the interior reflects parallel to the axis of symmetry (used in automotive headlights and flashlights). Conversely, any ray parallel to the axis reflects through the focus (used in satellite dishes and radio telescopes).</li>
  </ul>
</div>
`;

// 5. MOCK TAB
const mockTabContent = `
<h2>10-Question Diagnostic Assessment: Parabola</h2>
<p class="exam-instruction">Attempt all 10 diagnostic questions covering standard equations, focal geometry, directrices, latus rectum properties, and applied physical systems. Click <strong>Submit Diagnostic Mock</strong> to evaluate your answers with detailed step-by-step solutions.</p>

<div id="mock-exam-container"></div>

<div style="margin-top: 24px; text-align: center;">
  <button type="button" class="btn btn-primary" onclick="gradeObjectiveSection()" style="padding: 10px 24px; font-weight: 600; cursor: pointer;">Submit Diagnostic Mock</button>
  <button type="button" class="btn btn-secondary" onclick="resetMockExam()" style="padding: 10px 24px; font-weight: 600; margin-left: 12px; cursor: pointer;">Reset Test</button>
</div>

<div id="mock-results" style="display: none; margin-top: 30px; padding: 20px; border-radius: 8px; background-color: #f8fafc; border: 1px solid #e2e8f0;"></div>
<div id="mock-review" style="margin-top: 20px;"></div>
`;

// 6. MOCK OBJECTIVE DATA (10 authentic questions)
const mockScript = `
window.mockObjectiveData = [
  {
    question: "Find the coordinates of the focus and the equation of the directrix for the parabola y^2 = 12x.",
    options: [
      "Focus: (3, 0), Directrix: x = -3",
      "Focus: (-3, 0), Directrix: x = 3",
      "Focus: (0, 3), Directrix: y = -3",
      "Focus: (12, 0), Directrix: x = -12"
    ],
    correct: 0,
    explanation: "Comparing with standard form y^2 = 4ax, we have 4a = 12 => a = 3. Since the parabola opens to the right, the focus is at (a, 0) = (3, 0), and the directrix equation is x = -a => x = -3 (or x + 3 = 0)."
  },
  {
    question: "For the parabola x^2 = -16y, find the length of the latus rectum and the coordinates of the focus.",
    options: [
      "Length of Latus Rectum: 16, Focus: (0, -4)",
      "Length of Latus Rectum: 4, Focus: (0, -4)",
      "Length of Latus Rectum: 16, Focus: (-4, 0)",
      "Length of Latus Rectum: 8, Focus: (0, -2)"
    ],
    correct: 0,
    explanation: "Comparing with x^2 = -4ay, 4a = 16 => a = 4. The length of the latus rectum is 4a = 16. The parabola opens downward along the y-axis, so the focus is at (0, -a) = (0, -4)."
  },
  {
    question: "Find the equation of the parabola with vertex at (0, 0), passing through (2, 3), and symmetric with respect to the y-axis (opening upward).",
    options: [
      "3x^2 = 4y",
      "4x^2 = 3y",
      "y^2 = 6x",
      "3x^2 = 2y"
    ],
    correct: 0,
    explanation: "The equation of an upward-opening parabola symmetric to the y-axis is x^2 = 4ay. Substituting (2, 3): 2^2 = 4a(3) => 4 = 12a => 4a = 4/3. Thus the equation is x^2 = (4/3)y => 3x^2 = 4y."
  },
  {
    question: "An engineer designs a parabolic solar collector with a diameter of 8 m across its rim and a depth of 2 m at its center. How far from the vertex should the heating receiver (focus) be positioned?",
    options: [
      "2 meters",
      "4 meters",
      "1 meter",
      "0.5 meters"
    ],
    correct: 0,
    explanation: "Let the vertex be at (0, 0) and the parabola open upward: x^2 = 4ay. The outer rim is at depth y = 2 m and width 8 m (so x = 4 m). Substituting (4, 2): 4^2 = 4a(2) => 16 = 8a => a = 2 m. The focus is at (0, a) = (0, 2 m), which is exactly 2 meters from the vertex."
  },
  {
    question: "Find the focal distance of any point P(x1, y1) lying on the standard parabola y^2 = 4ax.",
    options: [
      "x1 + a",
      "x1 - a",
      "y1 + a",
      "sqrt(x1^2 + y1^2)"
    ],
    correct: 0,
    explanation: "By the fundamental definition of a parabola, the distance from any point P(x1, y1) on the curve to the focus S is equal to its perpendicular distance to the directrix x = -a. The distance to the directrix is x1 - (-a) = x1 + a."
  },
  {
    question: "What are the coordinates of the endpoints of the latus rectum of the parabola y^2 = 8x?",
    options: [
      "(2, 4) and (2, -4)",
      "(4, 2) and (-4, 2)",
      "(2, 2) and (2, -2)",
      "(0, 4) and (0, -4)"
    ],
    correct: 0,
    explanation: "Comparing with y^2 = 4ax: 4a = 8 => a = 2. The focus is at (a, 0) = (2, 0). The latus rectum is the vertical line x = 2. Substituting x = 2 into y^2 = 8x gives y^2 = 16 => y = +-4. The endpoints are (2, 4) and (2, -4)."
  },
  {
    question: "Find the equation of the parabola whose focus is (-3, 0) and directrix is x = 3.",
    options: [
      "y^2 = -12x",
      "y^2 = 12x",
      "x^2 = -12y",
      "y^2 = -6x"
    ],
    correct: 0,
    explanation: "The focus is (-3, 0) which matches (-a, 0) with a = 3, and directrix is x = a = 3. This is a leftward-opening parabola: y^2 = -4ax = -4(3)x = -12x."
  },
  {
    question: "A suspension bridge cable hangs in a parabolic curve between two towers 100 m apart. The towers are 30 m high and the lowest point of the cable is 10 m above the road. If the origin is placed at the lowest point of the cable, what is the parabolic equation?",
    options: [
      "x^2 = 125y",
      "x^2 = 250y",
      "y^2 = 125x",
      "x^2 = 62.5y"
    ],
    correct: 0,
    explanation: "Origin at lowest point (0, 0). The towers are at x = +-50 m. The height of the tower above the lowest point is 30 - 10 = 20 m. Point on cable: (50, 20). Equation x^2 = 4ay => 50^2 = 4a(20) => 2500 = 80a => 4a = 2500/20 = 125. Thus x^2 = 125y."
  },
  {
    question: "What is the eccentricity (e) of any parabolic conic section?",
    options: [
      "e = 1",
      "e < 1",
      "e > 1",
      "e = 0"
    ],
    correct: 0,
    explanation: "By mathematical definition, a conic section is a parabola if and only if its eccentricity e = SP/PM is strictly equal to 1."
  },
  {
    question: "Find the coordinates of the point on the parabola y^2 = 16x whose focal distance is 8.",
    options: [
      "(4, 8) and (4, -8)",
      "(8, 4) and (8, -4)",
      "(2, 8) and (2, -8)",
      "(4, 4) and (4, -4)"
    ],
    correct: 0,
    explanation: "Here 4a = 16 => a = 4. The focal distance of a point (x, y) on y^2 = 4ax is x + a = 8 => x + 4 = 8 => x = 4. Substituting x = 4 into y^2 = 16x: y^2 = 16(4) = 64 => y = +-8. The points are (4, 8) and (4, -8)."
  }
];

function renderMockExam() {
  const container = document.getElementById('mock-exam-container');
  if (!container || !window.mockObjectiveData) return;
  container.innerHTML = '';
  
  window.mockObjectiveData.forEach((item, index) => {
    const qDiv = document.createElement('div');
    qDiv.className = 'exercise-item';
    qDiv.style.marginBottom = '20px';
    qDiv.style.padding = '16px';
    qDiv.style.border = '1px solid #e2e8f0';
    qDiv.style.borderRadius = '8px';
    qDiv.style.backgroundColor = '#ffffff';
    
    let html = '<p style="font-weight: 600; margin-bottom: 12px;">Q' + (index + 1) + '. ' + item.question + '</p>';
    html += '<div class="options-group" style="display: flex; flex-direction: column; gap: 8px;">';
    
    item.options.forEach((opt, optIdx) => {
      html += '<label style="display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 6px 10px; border-radius: 4px; border: 1px solid #edf2f7;">';
      html += '<input type="radio" name="mock_q' + index + '" value="' + optIdx + '">';
      html += '<span>' + opt + '</span>';
      html += '</label>';
    });
    
    html += '</div>';
    qDiv.innerHTML = html;
    container.appendChild(qDiv);
  });
}

function gradeObjectiveSection() {
  if (!window.mockObjectiveData) return;
  let score = 0;
  const total = window.mockObjectiveData.length;
  let reviewHtml = '<h3>Diagnostic Review & Detailed Explanations</h3>';
  
  window.mockObjectiveData.forEach((item, index) => {
    const selected = document.querySelector('input[name="mock_q' + index + '"]:checked');
    const selectedVal = selected ? parseInt(selected.value) : -1;
    const isCorrect = selectedVal === item.correct;
    if (isCorrect) score++;
    
    reviewHtml += '<div style="margin-bottom: 16px; padding: 12px; border-radius: 6px; border-left: 4px solid ' + (isCorrect ? '#10b981' : '#ef4444') + '; background-color: ' + (isCorrect ? '#f0fdf4' : '#fef2f2') + ';">';
    reviewHtml += '<p style="font-weight: 600; margin-bottom: 6px;">Q' + (index + 1) + ': ' + (isCorrect ? 'Correct (+1)' : 'Incorrect (0)') + '</p>';
    reviewHtml += '<p style="margin-bottom: 6px;"><strong>Question:</strong> ' + item.question + '</p>';
    reviewHtml += '<p style="margin-bottom: 6px;"><strong>Your Answer:</strong> ' + (selectedVal >= 0 ? item.options[selectedVal] : '<em>Not Attempted</em>') + '</p>';
    reviewHtml += '<p style="margin-bottom: 6px;"><strong>Correct Answer:</strong> ' + item.options[item.correct] + '</p>';
    reviewHtml += '<p style="margin-top: 6px; font-size: 0.9em; color: #475569;"><strong>Explanation:</strong> ' + item.explanation + '</p>';
    reviewHtml += '</div>';
  });
  
  const resultsDiv = document.getElementById('mock-results');
  const percentage = Math.round((score / total) * 100);
  resultsDiv.innerHTML = '<h4>Performance Summary</h4><p style="font-size: 1.2em; font-weight: 700; color: ' + (percentage >= 70 ? '#059669' : '#dc2626') + ';">Your Score: ' + score + ' / ' + total + ' (' + percentage + '%)</p><p>' + (percentage >= 80 ? 'Exceptional command of parabolic geometry, focal parameters, and applied models.' : 'Review standard orientation tables and latus rectum definitions before retaking.') + '</p>';
  resultsDiv.style.display = 'block';
  
  const reviewDiv = document.getElementById('mock-review');
  reviewDiv.innerHTML = reviewHtml;
  if (window.MathJax && window.MathJax.typesetPromise) {
    window.MathJax.typesetPromise();
  }
}

function resetMockExam() {
  const container = document.getElementById('mock-exam-container');
  if (container) {
    const inputs = container.querySelectorAll('input[type="radio"]');
    inputs.forEach(input => input.checked = false);
  }
  const resultsDiv = document.getElementById('mock-results');
  if (resultsDiv) {
    resultsDiv.style.display = 'none';
    resultsDiv.innerHTML = '';
  }
  const reviewDiv = document.getElementById('mock-review');
  if (reviewDiv) reviewDiv.innerHTML = '';
}

document.addEventListener('DOMContentLoaded', renderMockExam);
`;

// Update DOM elements
$('#tab-learn').html(learnContent);
$('#tab-progress').html(progressContent);
$('#tab-worksheet').html(worksheetContent);
$('#tab-revision').html(revisionContent);
$('#tab-mock').html(mockTabContent);

// Remove existing inline mock script and inject new clean script
$('script').each((i, el) => {
  const text = $(el).html();
  if (text.includes('mockObjectiveData') || text.includes('gradeObjectiveSection')) {
    $(el).remove();
  }
});

// Append mock script right before closing body
$('body').append('<script>' + mockScript + '<\\/script>');

fs.writeFileSync(filePath, $.html(), 'utf8');
console.log('Successfully upgraded 16-2-parabola/index.html');
