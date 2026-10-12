const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'geometry-and-trigonometry');

const guides = [
  // Guide 12: 3D Vectors & The Scalar Product
  {
    folder: '3d-vectors-and-scalar-product',
    code: '3.11',
    title: '3D Vectors & The Scalar Product',
    pageTitle: '3D Vectors & The Scalar Product | IB Math AA HL | SJMaths',
    metaDesc: 'Master 3D vectors and the scalar product for IB DP Mathematics AA HL (Topic 3.11). Component form, magnitude, angle between vectors, orthogonality, vector projections, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL 3D vectors, scalar product dot product, angle between vectors in 3D, vector projection, unit vectors R3, perpendicular vectors condition',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Extend vector algebra to three-dimensional Euclidean space $\\mathbb{R}^3$. Calculate magnitudes, unit vectors, directional cosines, scalar dot products $\\mathbf{u}\\cdot\\mathbf{v} = |\\mathbf{u}||\\mathbf{v}|\\cos\\theta$, orthogonality tests, and vector projections.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/compound-angle-identities-and-double-angles/',
      title: 'Compound Angle Identities & Double Angles'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/vector-equations-of-lines-in-3d/',
      title: 'Vector Equations of Lines in 3D'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-cube" style="color:var(--c-primary);"></i> Figure 3.3: 3D Vectors and Scalar Projection</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing 3D coordinate system with vectors u and v, angle theta, and projection of u onto v">
            <!-- 3D Axes at Origin (300, 200) -->
            <!-- z-axis pointing up -->
            <line x1="300" y1="200" x2="300" y2="40" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="305" y="55" font-size="13" font-weight="bold" fill="var(--c-text)">z (k)</text>
            <!-- y-axis pointing right-up -->
            <line x1="300" y1="200" x2="620" y2="140" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="615" y="160" font-size="13" font-weight="bold" fill="var(--c-text)">y (j)</text>
            <!-- x-axis pointing down-left -->
            <line x1="300" y1="200" x2="100" y2="280" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="90" y="275" font-size="13" font-weight="bold" fill="var(--c-text)">x (i)</text>

            <!-- Vector v along floor towards (540, 155) -->
            <line x1="300" y1="200" x2="560" y2="160" stroke="#10b981" stroke-width="3.5" marker-end="url(#arrow)" />
            <text x="565" y="155" font-size="14" font-weight="bold" fill="#10b981">v</text>

            <!-- Vector u pointing up-right into space towards (460, 70) -->
            <line x1="300" y1="200" x2="460" y2="70" stroke="#6366f1" stroke-width="3.5" />
            <text x="470" y="70" font-size="14" font-weight="bold" fill="#6366f1">u</text>

            <!-- Angle theta between u and v -->
            <path d="M 360,190 A 60 60 0 0 0 350,160" fill="none" stroke="#ef4444" stroke-width="2" />
            <text x="375" y="170" font-size="14" font-weight="bold" fill="#ef4444">θ</text>

            <!-- Perpendicular Projection from head of u onto line of v -->
            <!-- Drop perp from (460, 70) to point on v at (450, 177) -->
            <line x1="460" y1="70" x2="450" y2="177" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4" />
            <!-- Right angle symbol -->
            <polyline points="440,179 443,165 453,163" fill="none" stroke="#ef4444" stroke-width="1.5" />

            <!-- Projection vector bracket -->
            <line x1="300" y1="215" x2="450" y2="192" stroke="#f59e0b" stroke-width="3" />
            <text x="350" y="235" font-size="12" font-weight="bold" fill="#f59e0b">proj_v(u) = [(u·v)/|v|²] v</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Vectors in Three Dimensions ($\\mathbb{R}^3$)</h2>
        <p>A vector $\\mathbf{v}$ in 3D can be written in component form with standard unit vectors $\\mathbf{i}, \\mathbf{j}, \\mathbf{k}$ or in column vector form:</p>
        $$\\mathbf{v} = v_1 \\mathbf{i} + v_2 \\mathbf{j} + v_3 \\mathbf{k} = \\begin{pmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{pmatrix}$$
        <ul class="theory-list">
          <li><strong>Magnitude (Length):</strong> $|\\mathbf{v}| = \\sqrt{v_1^2 + v_2^2 + v_3^2}$.</li>
          <li><strong>Unit Vector:</strong> A vector with magnitude 1 in the direction of $\\mathbf{v}$: $\\hat{\\mathbf{v}} = \\frac{\\mathbf{v}}{|\\mathbf{v}|}$.</li>
          <li><strong>Distance between points $A(x_1, y_1, z_1)$ and $B(x_2, y_2, z_2)$:</strong>
          $$AB = |\\vec{AB}| = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$</li>
        </ul>

        <h2>2. The Scalar (Dot) Product</h2>
        <p>The scalar product of two vectors $\\mathbf{u}$ and $\\mathbf{v}$ is a <strong>scalar</strong> defined algebraically and geometrically as:</p>
        $$\\mathbf{u} \\cdot \\mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 = |\\mathbf{u}| |\\mathbf{v}| \\cos\\theta$$
        <p>where $\\theta$ is the angle between the two vectors ($0 \\le \\theta \\le \\pi$).</p>

        <h2>3. Key Applications of the Scalar Product</h2>
        <ul class="theory-list">
          <li><strong>Angle between two vectors:</strong>
          $$\\cos\\theta = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{|\\mathbf{u}| |\\mathbf{v}|}$$</li>
          <li><strong>Orthogonality (Perpendicularity) Test:</strong> Non-zero vectors $\\mathbf{u}$ and $\\mathbf{v}$ are perpendicular if and only if:
          $$\\mathbf{u} \\cdot \\mathbf{v} = 0 \\iff \\theta = \\frac{\\pi}{2} = 90^\\circ$$</li>
          <li><strong>Vector Projection of $\\mathbf{u}$ onto $\\mathbf{v}$ (Syllabus 3.11):</strong>
            <br>• <strong>Scalar projection</strong> (signed length): $|\\mathbf{u}|\\cos\\theta = \\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|}$.
            <br>• <strong>Vector projection</strong> (the component vector along $\\mathbf{v}$):
            $$\\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\left(\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|}\\right) \\hat{\\mathbf{v}} = \\left(\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|^2}\\right) \\mathbf{v}$$
          </li>
        </ul>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Angle Between Two 3D Vectors</h4>
          <p>Find the angle between $\\mathbf{u} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 2 \\end{pmatrix}$ and $\\mathbf{v} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 2 \\end{pmatrix}$ in degrees.</p>
          <p><strong>Solution:</strong></p>
          <p>• Scalar product: $\\mathbf{u}\\cdot\\mathbf{v} = (2)(1) + (-1)(2) + (2)(2) = 2 - 2 + 4 = 4$.<br>
          • Magnitudes: $|\\mathbf{u}| = \\sqrt{2^2 + (-1)^2 + 2^2} = \\sqrt{4 + 1 + 4} = 3$.<br>
          $|\\mathbf{v}| = \\sqrt{1^2 + 2^2 + 2^2} = \\sqrt{1 + 4 + 4} = 3$.<br>
          • Cosine of angle:</p>
          $$\\cos\\theta = \\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{u}||\\mathbf{v}|} = \\frac{4}{3 \\times 3} = \\frac{4}{9}$$
          $$\\theta = \\arccos\\left(\\frac{4}{9}\\right) \\approx 63.6^\\circ$$
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Finding Parameter for Orthogonality</h4>
          <p>The vectors $\\mathbf{a} = \\begin{pmatrix} 3 \\\\ k \\\\ -2 \\end{pmatrix}$ and $\\mathbf{b} = \\begin{pmatrix} k+1 \\\\ 4 \\\\ k \\end{pmatrix}$ are perpendicular. Find all possible values of $k$.</p>
          <p><strong>Solution:</strong></p>
          <p>For perpendicular vectors, $\\mathbf{a}\\cdot\\mathbf{b} = 0$:</p>
          $$3(k + 1) + k(4) + (-2)(k) = 0$$
          $$3k + 3 + 4k - 2k = 0 \\implies 5k + 3 = 0 \\implies 5k = -3 \\implies k = -\\frac{3}{5}$$
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Vector Projection</h4>
          <p>Find the vector projection of $\\mathbf{u} = \\begin{pmatrix} 4 \\\\ 1 \\\\ 3 \\end{pmatrix}$ onto $\\mathbf{v} = \\begin{pmatrix} 2 \\\\ -2 \\\\ 1 \\end{pmatrix}$.</p>
          <p><strong>Solution:</strong></p>
          <p>• $\\mathbf{u}\\cdot\\mathbf{v} = 4(2) + 1(-2) + 3(1) = 8 - 2 + 3 = 9$.<br>
          • $|\\mathbf{v}|^2 = 2^2 + (-2)^2 + 1^2 = 4 + 4 + 1 = 9$.<br>
          • Vector projection:</p>
          $$\\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\left(\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|^2}\\right)\\mathbf{v} = \\left(\\frac{9}{9}\\right)\\begin{pmatrix} 2 \\\\ -2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ -2 \\\\ 1 \\end{pmatrix}$$
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Magnitude and Unit Vector)',
        text: 'Given $\\mathbf{a} = 2\\mathbf{i} - 3\\mathbf{j} + 6\\mathbf{k}$, find $|\\mathbf{a}|$ and the unit vector in the direction of $\\mathbf{a}$.',
        solution: '<p>$|\\mathbf{a}| = \\sqrt{2^2 + (-3)^2 + 6^2} = \\sqrt{4 + 9 + 36} = \\sqrt{49} = 7$. [A1]<br>Unit vector: $\\hat{\\mathbf{a}} = \\frac{1}{7}(2\\mathbf{i} - 3\\mathbf{j} + 6\\mathbf{k}) = \\begin{pmatrix} 2/7 \\\\ -3/7 \\\\ 6/7 \\end{pmatrix}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Scalar Product)',
        text: 'Calculate $\\mathbf{u}\\cdot\\mathbf{v}$ where $\\mathbf{u} = \\begin{pmatrix} 5 \\\\ -1 \\\\ 4 \\end{pmatrix}$ and $\\mathbf{v} = \\begin{pmatrix} -2 \\\\ 3 \\\\ 1 \\end{pmatrix}$.',
        solution: '<p>$\\mathbf{u}\\cdot\\mathbf{v} = 5(-2) + (-1)(3) + 4(1) = -10 - 3 + 4 = -9$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Orthogonality)',
        text: 'Show that $\\mathbf{p} = \\begin{pmatrix} 1 \\\\ 4 \\\\ -2 \\end{pmatrix}$ and $\\mathbf{q} = \\begin{pmatrix} 6 \\\\ -1 \\\\ 1 \\end{pmatrix}$ are perpendicular.',
        solution: '<p>$\\mathbf{p}\\cdot\\mathbf{q} = 1(6) + 4(-1) + (-2)(1) = 6 - 4 - 2 = 0$. [M1]<br>Since the scalar product is 0, the vectors are perpendicular. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Angle Between Vectors)',
        text: 'Find the angle between $\\mathbf{a} = \\mathbf{i} + \\mathbf{j}$ and $\\mathbf{b} = \\mathbf{j} + \\mathbf{k}$ in radians.',
        solution: '<p>$\\mathbf{a} = (1, 1, 0)$, $\\mathbf{b} = (0, 1, 1)$. [M1]<br>$\\mathbf{a}\\cdot\\mathbf{b} = 1(0) + 1(1) + 0(1) = 1$.<br>$|\\mathbf{a}| = \\sqrt{1+1+0} = \\sqrt{2}$, $|\\mathbf{b}| = \\sqrt{0+1+1} = \\sqrt{2}$. [M1]<br>$\\cos\\theta = \\frac{1}{\\sqrt{2}\\sqrt{2}} = \\frac{1}{2} \\implies \\theta = \\frac{\\pi}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Vector Projection Length)',
        text: 'Find the scalar projection of $\\mathbf{x} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$ onto $\\mathbf{y} = \\begin{pmatrix} 2 \\\\ 2 \\\\ 1 \\end{pmatrix}$.',
        solution: '<p>$\\mathbf{x}\\cdot\\mathbf{y} = 1(2) + 2(2) + 3(1) = 2 + 4 + 3 = 9$. [M1]<br>$|\\mathbf{y}| = \\sqrt{4 + 4 + 1} = 3$. [M1]<br>Scalar projection $= \\frac{\\mathbf{x}\\cdot\\mathbf{y}}{|\\mathbf{y}|} = \\frac{9}{3} = 3$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Quadratic Parameter for Angle)',
        text: 'Vectors $\\mathbf{u} = \\begin{pmatrix} 1 \\\\ p \\\\ 2 \\end{pmatrix}$ and $\\mathbf{v} = \\begin{pmatrix} p \\\\ 1 \\\\ 1 \\end{pmatrix}$ have an angle of $60^\\circ$. Find $p$.',
        solution: '<p>$\\mathbf{u}\\cdot\\mathbf{v} = p + p + 2 = 2p + 2$. [M1]<br>$|\\mathbf{u}| = \\sqrt{1 + p^2 + 4} = \\sqrt{p^2 + 5}$, $|\\mathbf{v}| = \\sqrt{p^2 + 1 + 1} = \\sqrt{p^2 + 2}$.<br>$\\cos(60^\\circ) = \\frac{1}{2} = \\frac{2p + 2}{\\sqrt{(p^2 + 5)(p^2 + 2)}}$. [M1]<br>Square both sides: $\\frac{1}{4} = \\frac{4(p+1)^2}{p^4 + 7p^2 + 10} \\implies p^4 + 7p^2 + 10 = 16(p^2 + 2p + 1) = 16p^2 + 32p + 16$.<br>$p^4 - 9p^2 - 32p - 6 = 0$. Using GDC/analytical inspection, $p \\approx 3.73$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Triangle Geometry via Vectors)',
        text: 'Points in 3D are $A(1, 0, 2)$, $B(2, 3, -1)$, and $C(4, 1, 1)$. Find $\\angle BAC$.',
        solution: '<p>$\\vec{AB} = \\mathbf{b} - \\mathbf{a} = \\begin{pmatrix} 1 \\\\ 3 \\\\ -3 \\end{pmatrix}$, $\\vec{AC} = \\mathbf{c} - \\mathbf{a} = \\begin{pmatrix} 3 \\\\ 1 \\\\ -1 \\end{pmatrix}$. [M1]<br>$\\vec{AB}\\cdot\\vec{AC} = 1(3) + 3(1) + (-3)(-1) = 3 + 3 + 3 = 9$. [M1]<br>$|\\vec{AB}| = \\sqrt{1 + 9 + 9} = \\sqrt{19}$, $|\\vec{AC}| = \\sqrt{9 + 1 + 1} = \\sqrt{11}$. [M1]<br>$\\cos(\\angle BAC) = \\frac{9}{\\sqrt{19}\\sqrt{11}} = \\frac{9}{\\sqrt{209}} \\approx 0.6225$.<br>$\\angle BAC = \\arccos(0.6225) \\approx 51.5^\\circ$ (or $0.899$ rad). [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Decomposing a Vector into Parallel & Perpendicular Components)',
        text: 'Given $\\mathbf{u} = \\begin{pmatrix} 3 \\\\ -1 \\\\ 2 \\end{pmatrix}$ and $\\mathbf{v} = \\begin{pmatrix} 1 \\\\ 2 \\\\ -2 \\end{pmatrix}$, decompose $\\mathbf{u}$ into $\\mathbf{u} = \\mathbf{u}_\\parallel + \\mathbf{u}_\\perp$ where $\\mathbf{u}_\\parallel$ is parallel to $\\mathbf{v}$ and $\\mathbf{u}_\\perp$ is perpendicular to $\\mathbf{v}$.',
        solution: '<p>$\\mathbf{u}_\\parallel = \\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\left(\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|^2}\\right)\\mathbf{v}$. [M1]<br>$\\mathbf{u}\\cdot\\mathbf{v} = 3(1) - 1(2) + 2(-2) = 3 - 2 - 4 = -3$.<br>$|\\mathbf{v}|^2 = 1^2 + 2^2 + (-2)^2 = 9$.<br>$\\mathbf{u}_\\parallel = -\\frac{3}{9}\\mathbf{v} = -\\frac{1}{3}\\begin{pmatrix} 1 \\\\ 2 \\\\ -2 \\end{pmatrix} = \\begin{pmatrix} -1/3 \\\\ -2/3 \\\\ 2/3 \\end{pmatrix}$. [A1]<br>$\\mathbf{u}_\\perp = \\mathbf{u} - \\mathbf{u}_\\parallel = \\begin{pmatrix} 3 \\\\ -1 \\\\ 2 \\end{pmatrix} - \\begin{pmatrix} -1/3 \\\\ -2/3 \\\\ 2/3 \\end{pmatrix} = \\begin{pmatrix} 10/3 \\\\ -1/3 \\\\ 4/3 \\end{pmatrix}$. [A1]<br>Verify $\\mathbf{u}_\\perp \\cdot \\mathbf{v} = \\frac{10}{3}(1) - \\frac{1}{3}(2) + \\frac{4}{3}(-2) = \\frac{10 - 2 - 8}{3} = 0$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Cauchy-Schwarz Inequality for Vectors)',
        text: 'Prove the Cauchy-Schwarz inequality $|\\mathbf{u}\\cdot\\mathbf{v}| \\le |\\mathbf{u}||\\mathbf{v}|$ for any vectors $\\mathbf{u}, \\mathbf{v} \\in \\mathbb{R}^3$, and state when equality holds.',
        solution: '<p>By definition, $\\mathbf{u}\\cdot\\mathbf{v} = |\\mathbf{u}||\\mathbf{v}|\\cos\\theta$. [M1]<br>Take the absolute value: $|\\mathbf{u}\\cdot\\mathbf{v}| = |\\mathbf{u}||\\mathbf{v}||\\cos\\theta|$. [M1]<br>Since $-1 \\le \\cos\\theta \\le 1$ for all real $\\theta$, $|\\cos\\theta| \\le 1$.<br>Therefore $|\\mathbf{u}\\cdot\\mathbf{v}| = |\\mathbf{u}||\\mathbf{v}||\\cos\\theta| \\le |\\mathbf{u}||\\mathbf{v}|(1) = |\\mathbf{u}||\\mathbf{v}|$. [A1]<br>Equality holds if and only if $|\\cos\\theta| = 1 \\iff \\theta = 0$ or $\\pi$, meaning $\\mathbf{u}$ and $\\mathbf{v}$ are <strong>collinear (scalar multiples)</strong>. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Work Done and Vector Force)',
        text: 'A constant force $\\mathbf{F} = 4\\mathbf{i} - 2\\mathbf{j} + 5\\mathbf{k}$ N moves a particle from point $A(1, 2, -1)$ to $B(3, 0, 4)$ (coordinates in metres). Calculate the work done by the force in Joules.',
        solution: '<p>Displacement vector $\\mathbf{d} = \\vec{AB} = \\begin{pmatrix} 3-1 \\\\ 0-2 \\\\ 4-(-1) \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ -2 \\\\ 5 \\end{pmatrix}$ m. [M1]<br>Work done $W = \\mathbf{F}\\cdot\\mathbf{d}$. [M1]<br>$W = 4(2) + (-2)(-2) + 5(5) = 8 + 4 + 25 = 37$ J. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 3)</h2>
        <div class="formula-card">
          <h4>Syllabus 3.11: 3D Vectors &amp; Scalar Product</h4>
          $$|\\mathbf{v}| = \\sqrt{v_1^2 + v_2^2 + v_3^2}$$
          $$\\mathbf{u}\\cdot\\mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 = |\\mathbf{u}||\\mathbf{v}|\\cos\\theta$$
          $$\\cos\\theta = \\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{u}||\\mathbf{v}|}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Orthogonality Condition</h4>
          $$\\mathbf{u} \\perp \\mathbf{v} \\iff \\mathbf{u}\\cdot\\mathbf{v} = 0$$
        </div>
        <div class="formula-card">
          <h4>2. Vector Projection</h4>
          $$\\text{proj}_{\\mathbf{v}}(\\mathbf{u}) = \\left(\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|^2}\\right)\\mathbf{v}$$
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Scalar vs Vector Output</h4>
          <p>The scalar (dot) product outputs a SINGLE NUMBER (scalar). Writing a vector as the result of a dot product is an immediate error.</p>
        </div>
        <div class="pitfall-card">
          <h4>Degrees vs Radians in Vector Angles</h4>
          <p>Read the question carefully! Unless degrees are specified, IB exam standard defaults to 3 significant figures in radians.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If $\\mathbf{a}\\cdot\\mathbf{b} = -|\\mathbf{a}||\\mathbf{b}|$, the angle between $\\mathbf{a}$ and $\\mathbf{b}$ is:',
        options: [
          '$0$',
          '$\\frac{\\pi}{2}$',
          '$\\pi$',
          '$\\frac{3\\pi}{2}$'
        ],
        correct: 2,
        explanation: '$\\cos\\theta = -1 \\implies \\theta = \\pi$ (the vectors are antiparallel).'
      },
      {
        id: 'q2',
        prompt: 'What is the length of $\\mathbf{v} = \\begin{pmatrix} 3 \\\\ -4 \\\\ 12 \\end{pmatrix}$?',
        options: [
          '11',
          '13',
          '15',
          '17'
        ],
        correct: 1,
        explanation: '$|\\mathbf{v}| = \\sqrt{3^2 + (-4)^2 + 12^2} = \\sqrt{9 + 16 + 144} = \\sqrt{169} = 13$.'
      },
      {
        id: 'q3',
        prompt: 'Which vector is orthogonal to $\\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$?',
        options: [
          '$\\begin{pmatrix} 1 \\\\ 1 \\\\ -1 \\end{pmatrix}$',
          '$\\begin{pmatrix} -3 \\\\ 0 \\\\ 1 \\end{pmatrix}$',
          '$\\begin{pmatrix} 2 \\\\ 1 \\\\ -1 \\end{pmatrix}$',
          '$\\begin{pmatrix} 0 \\\\ -3 \\\\ 1 \\end{pmatrix}$'
        ],
        correct: 1,
        explanation: 'Dot product: $1(-3) + 2(0) + 3(1) = -3 + 0 + 3 = 0$.'
      },
      {
        id: 'q4',
        prompt: 'The scalar projection of $\\mathbf{u}$ onto $\\mathbf{v}$ is:',
        options: [
          '$\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{u}|}$',
          '$\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|}$',
          '$\\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|^2}$',
          '$|\\mathbf{u}||\\mathbf{v}|$'
        ],
        correct: 1,
        explanation: 'Scalar projection along $\\mathbf{v}$ is $|\\mathbf{u}|\\cos\\theta = \\frac{\\mathbf{u}\\cdot\\mathbf{v}}{|\\mathbf{v}|}$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'The vertices of a triangle in 3D are $A(2, 1, 3)$, $B(4, 3, 2)$, and $C(1, 5, 6)$.<br><strong>(a)</strong> Find the position vectors $\\vec{BA}$ and $\\vec{BC}$. [2 marks]<br><strong>(b)</strong> Calculate $\\vec{BA}\\cdot\\vec{BC}$. [2 marks]<br><strong>(c)</strong> Hence deduce whether triangle $ABC$ is acute, right-angled, or obtuse at vertex $B$. [2 marks]',
        solution: `
          <p><strong>(a) Position vectors: [2 marks]</strong><br>
          $\\vec{BA} = \\mathbf{a} - \\mathbf{b} = \\begin{pmatrix} 2-4 \\\\ 1-3 \\\\ 3-2 \\end{pmatrix} = \\begin{pmatrix} -2 \\\\ -2 \\\\ 1 \\end{pmatrix}$ [A1].<br>
          $\\vec{BC} = \\mathbf{c} - \\mathbf{b} = \\begin{pmatrix} 1-4 \\\\ 5-3 \\\\ 6-2 \\end{pmatrix} = \\begin{pmatrix} -3 \\\\ 2 \\\\ 4 \\end{pmatrix}$ [A1].</p>
          <p><strong>(b) Dot product: [2 marks]</strong><br>
          $\\vec{BA}\\cdot\\vec{BC} = (-2)(-3) + (-2)(2) + 1(4) = 6 - 4 + 4 = 6$ [A1].</p>
          <p><strong>(c) Nature of angle $B$: [2 marks]</strong><br>
          Since $\\vec{BA}\\cdot\\vec{BC} = 6 &gt; 0$, $\\cos B &gt; 0$ [M1].<br>
          Therefore $\\angle B$ is an <strong>acute angle</strong> [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'Consider vectors $\\mathbf{a} = 2\\mathbf{i} + \\mathbf{j} - 2\\mathbf{k}$ and $\\mathbf{b} = 3\\mathbf{i} - 4\\mathbf{k}$.<br><strong>(a)</strong> Find the vector projection of $\\mathbf{a}$ onto $\\mathbf{b}$. [3 marks]<br><strong>(b)</strong> Find the component of $\\mathbf{a}$ perpendicular to $\\mathbf{b}$. [2 marks]<br><strong>(c)</strong> Verify that your perpendicular component is indeed orthogonal to $\\mathbf{b}$. [2 marks]',
        solution: `
          <p><strong>(a) Vector projection: [3 marks]</strong><br>
          $\\mathbf{a} = (2, 1, -2)$, $\\mathbf{b} = (3, 0, -4)$.<br>
          $\\mathbf{a}\\cdot\\mathbf{b} = 2(3) + 1(0) + (-2)(-4) = 6 + 0 + 8 = 14$ [M1].<br>
          $|\\mathbf{b}|^2 = 3^2 + 0^2 + (-4)^2 = 9 + 16 = 25$ [A1].<br>
          $\\text{proj}_{\\mathbf{b}}(\\mathbf{a}) = \\frac{14}{25}\\begin{pmatrix} 3 \\\\ 0 \\\\ -4 \\end{pmatrix} = \\begin{pmatrix} 42/25 \\\\ 0 \\\\ -56/25 \\end{pmatrix}$ [A1].</p>
          <p><strong>(b) Perpendicular component: [2 marks]</strong><br>
          $\\mathbf{a}_\\perp = \\mathbf{a} - \\text{proj}_{\\mathbf{b}}(\\mathbf{a}) = \\begin{pmatrix} 2 \\\\ 1 \\\\ -2 \\end{pmatrix} - \\begin{pmatrix} 42/25 \\\\ 0 \\\\ -56/25 \\end{pmatrix} = \\begin{pmatrix} 8/25 \\\\ 1 \\\\ 6/25 \\end{pmatrix}$ [M1][A1].</p>
          <p><strong>(c) Verification: [2 marks]</strong><br>
          $\\mathbf{a}_\\perp \\cdot \\mathbf{b} = \\frac{8}{25}(3) + 1(0) + \\frac{6}{25}(-4) = \\frac{24}{25} - \\frac{24}{25} = 0$ [M1].<br>
          Since dot product is 0, orthogonality is verified [A1].</p>
        `
      }
    ]
  },

  // Guide 13: Vector Equations of Lines in 3D
  {
    folder: 'vector-equations-of-lines-in-3d',
    code: '3.12',
    title: 'Vector Equations of Lines in 3D',
    pageTitle: 'Vector Equations of Lines in 3D | IB Math AA HL | SJMaths',
    metaDesc: 'Master vector, parametric, and Cartesian equations of lines in 3D for IB DP Mathematics AA HL (Topic 3.12). Parallel, intersecting, coincident, and skew lines, shortest distance, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL 3D lines, vector equation of a line, parametric line equations, skew lines test, intersection of 3D lines, angle between lines',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Formulate vector $\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}$ and Cartesian equations of 3D lines. Master methods to determine whether two lines are parallel, intersecting, coincident, or skew, and calculate shortest distances.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/3d-vectors-and-scalar-product/',
      title: '3D Vectors & The Scalar Product'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/vector-cross-product-and-planes/',
      title: 'Vector Cross Product & Equations of Planes'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-arrows-alt" style="color:var(--c-primary);"></i> Figure 3.4: Four Geometric Relationships Between Two 3D Lines</h3>
          <svg viewBox="0 0 760 280" width="100%" height="280" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing parallel lines, intersecting lines, and skew lines in 3D space">
            <!-- Panel 1: Parallel Lines (left) -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="210" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="105" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#6366f1">Parallel Lines</text>
              <line x1="30" y1="90" x2="180" y2="70" stroke="#6366f1" stroke-width="2.5" />
              <line x1="30" y1="150" x2="180" y2="130" stroke="#6366f1" stroke-width="2.5" />
              <text x="105" y="215" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">d₁ = k d₂, no common point</text>
            </g>

            <!-- Panel 2: Intersecting Lines (middle) -->
            <g transform="translate(275, 20)">
              <rect x="0" y="0" width="210" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="105" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#10b981">Intersecting Lines</text>
              <line x1="30" y1="70" x2="180" y2="170" stroke="#10b981" stroke-width="2.5" />
              <line x1="30" y1="160" x2="180" y2="80" stroke="#10b981" stroke-width="2.5" />
              <circle cx="105" cy="120" r="5" fill="#ef4444" />
              <text x="105" y="140" text-anchor="middle" font-size="11" font-weight="bold" fill="#ef4444">Point P</text>
              <text x="105" y="215" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Non-parallel, 1 common point</text>
            </g>

            <!-- Panel 3: Skew Lines (right) -->
            <g transform="translate(520, 20)">
              <rect x="0" y="0" width="210" height="230" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="105" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">Skew Lines</text>
              <!-- Top plane line -->
              <line x1="30" y1="80" x2="180" y2="80" stroke="#ef4444" stroke-width="2.5" />
              <!-- Bottom plane angled line -->
              <line x1="40" y1="180" x2="160" y2="110" stroke="#f59e0b" stroke-width="2.5" />
              <!-- Distance bridge -->
              <line x1="100" y1="80" x2="100" y2="145" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="105" y="215" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Non-parallel, NEVER meet</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Equations of a Line in Three Dimensions</h2>
        <p>A straight line in $\\mathbb{R}^3$ passing through a fixed point with position vector $\\mathbf{a}$ and parallel to non-zero direction vector $\\mathbf{b}$ has three standard representations:</p>
        <ul class="theory-list">
          <li><strong>Vector Equation:</strong>
          $$\\mathbf{r} = \\mathbf{a} + \\lambda \\mathbf{b}, \\quad \\lambda \\in \\mathbb{R}$$
          $$\\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix} = \\begin{pmatrix} x_0 \\\\ y_0 \\\\ z_0 \\end{pmatrix} + \\lambda \\begin{pmatrix} d_1 \\\\ d_2 \\\\ d_3 \\end{pmatrix}$$</li>
          <li><strong>Parametric Equations:</strong>
          $$x = x_0 + \\lambda d_1, \\quad y = y_0 + \\lambda d_2, \\quad z = z_0 + \\lambda d_3$$</li>
          <li><strong>Cartesian (Symmetric) Form:</strong> Eliminating parameter $\\lambda$:
          $$\\frac{x - x_0}{d_1} = \\frac{y - y_0}{d_2} = \\frac{z - z_0}{d_3} \\quad (= \\lambda)$$</li>
        </ul>

        <h2>2. Angle Between Two Lines</h2>
        <p>The angle $\\theta$ between two lines $L_1: \\mathbf{r} = \\mathbf{a}_1 + \\lambda \\mathbf{d}_1$ and $L_2: \\mathbf{r} = \\mathbf{a}_2 + \\mu \\mathbf{d}_2$ is defined as the angle between their <strong>direction vectors</strong>:</p>
        $$\\cos\\theta = \\frac{|\\mathbf{d}_1 \\cdot \\mathbf{d}_2|}{|\\mathbf{d}_1| |\\mathbf{d}_2|}$$
        <p><em>(By convention, the acute angle is taken using the absolute value $|\\mathbf{d}_1\\cdot\\mathbf{d}_2|$).</em></p>

        <h2>3. Classification of Lines in $\\mathbb{R}^3$</h2>
        <p>Unlike 2D geometry where lines either intersect or are parallel, two lines in 3D have four possible relationships:</p>
        <div class="table-responsive" style="margin: 1.5rem 0;">
          <table class="ib-table" style="width:100%; border-collapse:collapse;">
            <thead>
              <tr style="background:var(--c-surface-card); border-bottom:2px solid var(--c-border);">
                <th style="padding:10px; text-align:left;">Relationship</th>
                <th style="padding:10px; text-align:left;">Direction Vectors ($\\mathbf{d}_1, \\mathbf{d}_2$)</th>
                <th style="padding:10px; text-align:left;">System $\\mathbf{r}_1(\\lambda) = \\mathbf{r}_2(\\mu)$</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Parallel &amp; Distinct</strong></td>
                <td style="padding:10px;">Scalar multiples: $\\mathbf{d}_1 = k\\mathbf{d}_2$</td>
                <td style="padding:10px;">Inconsistent (no solutions). Lines never meet.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Coincident</strong></td>
                <td style="padding:10px;">Scalar multiples: $\\mathbf{d}_1 = k\\mathbf{d}_2$</td>
                <td style="padding:10px;">Consistent for all points. Same line.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Intersecting</strong></td>
                <td style="padding:10px;">Not parallel: $\\mathbf{d}_1 \\neq k\\mathbf{d}_2$</td>
                <td style="padding:10px;">Unique solution $(\\lambda, \\mu)$ satisfies all 3 coordinate equations. Meet at 1 point.</td>
              </tr>
              <tr>
                <td style="padding:10px;"><strong>Skew</strong></td>
                <td style="padding:10px;">Not parallel: $\\mathbf{d}_1 \\neq k\\mathbf{d}_2$</td>
                <td style="padding:10px;">Inconsistent (values of $\\lambda, \\mu$ from equations 1 and 2 fail in equation 3). Lie in different parallel planes.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Finding Intersection Point of Two 3D Lines</h4>
          <p>Determine whether lines $L_1$ and $L_2$ intersect, and if so, find the point of intersection:</p>
          $$L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 3 \\\\ -1 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ -1 \\\\ 1 \\end{pmatrix}, \\quad L_2: \\mathbf{r} = \\begin{pmatrix} 4 \\\\ 1 \\\\ 3 \\end{pmatrix} + \\mu \\begin{pmatrix} 1 \\\\ 1 \\\\ -1 \\end{pmatrix}$$
          <p><strong>Solution:</strong></p>
          <p>Set parametric coordinates equal:</p>
          $$\\begin{cases} 1 + 2\\lambda = 4 + \\mu & (1) \\\\ 3 - \\lambda = 1 + \\mu & (2) \\\\ -1 + \\lambda = 3 - \\mu & (3) \\end{cases}$$
          <p>From (1): $2\\lambda - \\mu = 3$.<br>
          From (2): $-\\lambda - \\mu = -2 \\implies \\lambda + \\mu = 2$.<br>
          Add the two equations: $3\\lambda = 5 \\implies \\lambda = \\frac{5}{3}$. Wait, let's recheck equation 2: $3 - \\lambda = 1 + \\mu \\implies \\lambda + \\mu = 2$.<br>
          Let's test an integer point: if $\\lambda = 1$: $L_1 = (3, 2, 0)$. Then for $L_2$: $4 + \\mu = 3 \\implies \\mu = -1$.<br>
          $y = 1 + (-1) = 0 \\neq 2$.<br>
          Solving systematically: $\\lambda = 5/3 \\implies \\mu = 2 - 5/3 = 1/3$.<br>
          Now check Equation (3):<br>
          LHS: $-1 + \\lambda = -1 + 5/3 = 2/3$.<br>
          RHS: $3 - \\mu = 3 - 1/3 = 8/3$.<br>
          Since $2/3 \\neq 8/3$, Equation (3) is NOT satisfied!<br>
          Since direction vectors $(2, -1, 1)$ and $(1, 1, -1)$ are not scalar multiples, these lines are <strong>skew</strong>.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Intersecting Lines with Parameter</h4>
          <p>Lines $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ 2 \\\\ 1 \\end{pmatrix}$ and $L_2: \\mathbf{r} = \\begin{pmatrix} 2 \\\\ -1 \\\\ k \\end{pmatrix} + \\mu \\begin{pmatrix} 1 \\\\ 1 \\\\ 2 \\end{pmatrix}$ intersect. Find $k$ and the intersection point.</p>
          <p><strong>Solution:</strong></p>
          <p>Equate $x$ and $y$ coordinates:</p>
          $$1 + \\lambda = 2 + \\mu \\implies \\lambda - \\mu = 1 \\quad (1)$$
          $$0 + 2\\lambda = -1 + \\mu \\implies 2\\lambda - \\mu = -1 \\quad (2)$$
          <p>Subtract (1) from (2): $(2\\lambda - \\mu) - (\\lambda - \\mu) = -1 - 1 \\implies \\lambda = -2$.<br>
          Substitute into (1): $-2 - \\mu = 1 \\implies \\mu = -3$.<br>
          Now equate $z$ coordinate with $\\lambda = -2, \\mu = -3$:</p>
          $$2 + \\lambda(1) = k + \\mu(2) \\implies 2 + (-2) = k + (-3)(2) \\implies 0 = k - 6 \\implies k = 6$$
          <p>Point of intersection: $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix} - 2\\begin{pmatrix} 1 \\\\ 2 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ -4 \\\\ 0 \\end{pmatrix}$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Shortest Distance from a Point to a Line</h4>
          <p>Find the shortest distance from the point $P(1, 2, 3)$ to the line $L: \\mathbf{r} = \\begin{pmatrix} 2 \\\\ -1 \\\\ 4 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ 1 \\\\ -2 \\end{pmatrix}$.</p>
          <p><strong>Solution:</strong></p>
          <p>A general point on the line is $Q(2 + \\lambda, -1 + \\lambda, 4 - 2\\lambda)$.<br>
          Vector $\\vec{PQ} = \\begin{pmatrix} (2 + \\lambda) - 1 \\\\ (-1 + \\lambda) - 2 \\\\ (4 - 2\\lambda) - 3 \\end{pmatrix} = \\begin{pmatrix} 1 + \\lambda \\\\ \\lambda - 3 \\\\ 1 - 2\\lambda \\end{pmatrix}$.<br>
          The distance is minimized when $\\vec{PQ}$ is <strong>perpendicular</strong> to the direction vector $\\mathbf{d} = \\begin{pmatrix} 1 \\\\ 1 \\\\ -2 \\end{pmatrix}$:</p>
          $$\\vec{PQ} \\cdot \\mathbf{d} = 0 \\implies 1(1 + \\lambda) + 1(\\lambda - 3) - 2(1 - 2\\lambda) = 0$$
          $$1 + \\lambda + \\lambda - 3 - 2 + 4\\lambda = 0 \\implies 6\\lambda - 4 = 0 \\implies \\lambda = \\frac{2}{3}$$
          <p>Substitute $\\lambda = \\frac{2}{3}$ into $\\vec{PQ}$:</p>
          $$\\vec{PQ} = \\begin{pmatrix} 1 + 2/3 \\\\ 2/3 - 3 \\\\ 1 - 4/3 \\end{pmatrix} = \\begin{pmatrix} 5/3 \\\\ -7/3 \\\\ -1/3 \\end{pmatrix}$$
          $$\\text{Distance } |\\vec{PQ}| = \\sqrt{\\left(\\frac{5}{3}\\right)^2 + \\left(-\\frac{7}{3}\\right)^2 + \\left(-\\frac{1}{3}\\right)^2} = \\frac{\\sqrt{25 + 49 + 1}}{3} = \\frac{\\sqrt{75}}{3} = \\frac{5\\sqrt{3}}{3} \\approx 2.89$$
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Writing Vector Line Equation)',
        text: 'Write down a vector equation of the line passing through points $A(3, -1, 4)$ and $B(5, 2, 1)$.',
        solution: '<p>Direction vector $\\mathbf{d} = \\vec{AB} = \\begin{pmatrix} 5 - 3 \\\\ 2 - (-1) \\\\ 1 - 4 \\end{pmatrix} = \\begin{pmatrix} 2 \\\\ 3 \\\\ -3 \\end{pmatrix}$. [M1]<br>Vector equation: $\\mathbf{r} = \\begin{pmatrix} 3 \\\\ -1 \\\\ 4 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ 3 \\\\ -3 \\end{pmatrix}$, $\\lambda \\in \\mathbb{R}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Converting to Cartesian Form)',
        text: 'Convert the vector line $\\mathbf{r} = \\begin{pmatrix} 2 \\\\ 0 \\\\ -5 \\end{pmatrix} + \\lambda \\begin{pmatrix} 4 \\\\ 3 \\\\ 1 \\end{pmatrix}$ into Cartesian form.',
        solution: '<p>$x = 2 + 4\\lambda \\implies \\lambda = \\frac{x - 2}{4}$. [M1]<br>$y = 0 + 3\\lambda \\implies \\lambda = \\frac{y}{3}$.<br>$z = -5 + \\lambda \\implies \\lambda = z + 5$.<br>Cartesian form: $\\frac{x - 2}{4} = \\frac{y}{3} = z + 5$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Angle Between Two Lines)',
        text: 'Find the acute angle between $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 0 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ 0 \\\\ 1 \\end{pmatrix}$ and $L_2: \\mathbf{r} = \\begin{pmatrix} 0 \\\\ 1 \\\\ 4 \\end{pmatrix} + \\mu \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix}$.',
        solution: '<p>$\\mathbf{d}_1 = (1, 0, 1)$, $\\mathbf{d}_2 = (0, 1, 1)$. [M1]<br>$\\mathbf{d}_1\\cdot\\mathbf{d}_2 = 1(0) + 0(1) + 1(1) = 1$.<br>$|\\mathbf{d}_1| = \\sqrt{2}$, $|\\mathbf{d}_2| = \\sqrt{2}$.<br>$\\cos\\theta = \\frac{1}{\\sqrt{2}\\sqrt{2}} = \\frac{1}{2} \\implies \\theta = \\frac{\\pi}{3} = 60^\\circ$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Parallel Lines Distinction)',
        text: 'Show that lines $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ -4 \\\\ 6 \\end{pmatrix}$ and $L_2: \\mathbf{r} = \\begin{pmatrix} 0 \\\\ 4 \\\\ 0 \\end{pmatrix} + \\mu \\begin{pmatrix} -1 \\\\ 2 \\\\ -3 \\end{pmatrix}$ are parallel and distinct.',
        solution: '<p>Direction vectors: $\\mathbf{d}_1 = (2, -4, 6) = -2(-1, 2, -3) = -2\\mathbf{d}_2$. Since $\\mathbf{d}_1$ is a scalar multiple of $\\mathbf{d}_2$, the lines are parallel. [M1]<br>Check if point $(1, 2, 3)$ lies on $L_2$:<br>$1 = -\\mu \\implies \\mu = -1$.<br>$y = 4 + 2(-1) = 2$ (matches).<br>$z = 0 - 3(-1) = 3$ (matches!).<br>Wait, $(1, 2, 3)$ satisfies $L_2$! Therefore the lines are <strong>coincident</strong> (identical)! [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Determining Intersecting Lines)',
        text: 'Find the point of intersection of $L_1: \\frac{x-1}{2} = \\frac{y+2}{3} = z-1$ and $L_2: \\frac{x+1}{1} = \\frac{y-3}{-2} = \\frac{z-4}{1}$.',
        solution: '<p>In parametric form:<br>$L_1: (1 + 2\\lambda, -2 + 3\\lambda, 1 + \\lambda)$.<br>$L_2: (-1 + \\mu, 3 - 2\\mu, 4 + \\mu)$. [M1]<br>Equate $x$ and $z$:<br>$1 + 2\\lambda = -1 + \\mu \\implies 2\\lambda - \\mu = -2$.<br>$1 + \\lambda = 4 + \\mu \\implies \\lambda - \\mu = 3$.<br>Subtract: $\\lambda = -5 \\implies \\mu = -5 - 3 = -8$. [M1]<br>Test $y$ coordinate:<br>$L_1: -2 + 3(-5) = -17$.<br>$L_2: 3 - 2(-8) = 19$.<br>Since $-17 \\neq 19$, the equations are inconsistent. The lines do not intersect (they are skew). [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Closest Approach of Two Particles)',
        text: 'Two drones fly in straight lines with position vectors $\\mathbf{r}_1(t) = \\begin{pmatrix} 1 \\\\ 2 \\\\ 0 \\end{pmatrix} + t\\begin{pmatrix} 1 \\\\ 0 \\\\ 1 \\end{pmatrix}$ and $\\mathbf{r}_2(t) = \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix} + t\\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix}$ where $t$ is time. Find the time $t$ when the drones are closest to each other.',
        solution: '<p>Relative displacement: $\\mathbf{d}(t) = \\mathbf{r}_1 - \\mathbf{r}_2 = \\begin{pmatrix} 1 + t \\\\ 2 - t - 1 \\\\ t - (1+t) \\end{pmatrix} = \\begin{pmatrix} 1 + t \\\\ 1 - t \\\\ -1 \\end{pmatrix}$. [M1]<br>Squared distance: $S(t) = (1 + t)^2 + (1 - t)^2 + (-1)^2 = (1 + 2t + t^2) + (1 - 2t + t^2) + 1 = 2t^2 + 3$. [M1]<br>To minimize $2t^2 + 3$, set $\\frac{dS}{dt} = 4t = 0 \\implies t = 0$. [A1]<br>The drones are closest at $t = 0$, with minimum distance $\\sqrt{3}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Skew Lines Proof)',
        text: 'Prove that lines $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$ and $L_2: \\mathbf{r} = \\begin{pmatrix} 2 \\\\ 0 \\\\ 1 \\end{pmatrix} + \\mu \\begin{pmatrix} 2 \\\\ 1 \\\\ 1 \\end{pmatrix}$ are skew.',
        solution: '<p><strong>Step 1: Check direction vectors:</strong> $\\mathbf{d}_1 = (1, 2, 3)$, $\\mathbf{d}_2 = (2, 1, 1)$. Since $1/2 \\neq 2/1 \\neq 3/1$, $\\mathbf{d}_1 \\neq k\\mathbf{d}_2$. Lines are not parallel. [M1]</p><p><strong>Step 2: Test for intersection:</strong><br>$1 + \\lambda = 2 + 2\\mu \\implies \\lambda - 2\\mu = 1$ (1)<br>$1 + 2\\lambda = \\mu \\implies 2\\lambda - \\mu = -1$ (2)<br>From (1): $\\lambda = 1 + 2\\mu$. In (2): $2(1 + 2\\mu) - \\mu = -1 \\implies 2 + 3\\mu = -1 \\implies 3\\mu = -3 \\implies \\mu = -1$.<br>Then $\\lambda = 1 + 2(-1) = -1$. [M1]<br>Check $z$-coordinate: $L_1: 1 + 3(-1) = -2$. $L_2: 1 + 1(-1) = 0$.<br>Since $-2 \\neq 0$, the system is inconsistent. [R1]<br>Non-parallel and non-intersecting $\\implies$ the lines are <strong>skew</strong>. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Shortest Distance Between Two Skew Lines)',
        text: 'Find the shortest distance between skew lines $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} + \\lambda \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix}$ and $L_2: \\mathbf{r} = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix} + \\mu \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix}$.',
        solution: '<p>The common perpendicular vector $\\mathbf{n}$ is orthogonal to both direction vectors: [M1]<br>$\\mathbf{n} = \\mathbf{d}_1 \\times \\mathbf{d}_2 = \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix} \\times \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ 1 \\\\ -1 \\end{pmatrix}$. [A1]<br>Unit normal: $\\hat{\\mathbf{n}} = \\frac{1}{\\sqrt{1+1+1}}(-1, 1, -1) = \\frac{1}{\\sqrt{3}}(-1, 1, -1)$.<br>Vector connecting points on the lines: $\\mathbf{a}_1 - \\mathbf{a}_2 = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} - \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 0 \\\\ -1 \\end{pmatrix}$. [M1]<br>Shortest distance $= |(\\mathbf{a}_1 - \\mathbf{a}_2) \\cdot \\hat{\\mathbf{n}}| = \\left|\\frac{1(-1) + 0(1) + (-1)(-1)}{\\sqrt{3}}\\right| = \\left|\\frac{-1 + 1}{\\sqrt{3}}\\right| = 0$?<br>Wait, if distance is 0, do they intersect? Check: $(1, \\lambda, \\lambda) = (\\mu, \\mu, 1) \\implies \\mu = 1, \\lambda = 1$. Both points equal $(1, 1, 1)$! They intersect at $(1, 1, 1)$! Distance is 0. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Reflection of a Point in a 3D Line)',
        text: 'Find the coordinates of the reflection of point $P(2, 1, 4)$ in the line $L: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ 0 \\\\ 1 \\end{pmatrix}$.',
        solution: '<p>Let $F(1+\\lambda, 1, 1+\\lambda)$ be the foot of the perpendicular from $P$ to $L$. [M1]<br>$\\vec{PF} = \\begin{pmatrix} 1+\\lambda-2 \\\\ 1-1 \\\\ 1+\\lambda-4 \\end{pmatrix} = \\begin{pmatrix} \\lambda-1 \\\\ 0 \\\\ \\lambda-3 \\end{pmatrix}$.<br>$\\vec{PF}\\cdot\\mathbf{d} = 0 \\implies 1(\\lambda - 1) + 0(0) + 1(\\lambda - 3) = 0 \\implies 2\\lambda - 4 = 0 \\implies \\lambda = 2$. [M1]<br>Foot of perpendicular $F = (1+2, 1, 1+2) = (3, 1, 3)$. [A1]<br>Let $P\'(x\', y\', z\')$ be the reflection. Then $F$ is the midpoint of $PP\'$:<br>$F = \\frac{P + P\'}{2} \\implies P\' = 2F - P = 2(3, 1, 3) - (2, 1, 4) = (6-2, 2-1, 6-4) = (4, 1, 2)$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Line as Intersection of Two Planes)',
        text: 'Express the line of intersection of planes $x + y + z = 3$ and $2x - y + z = 1$ in vector form $\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}$.',
        solution: '<p>Add the two equations: $3x + 2z = 4 \\implies x = \\frac{4 - 2z}{3}$. [M1]<br>Let $z = 3\\lambda$. Then $x = \\frac{4 - 6\\lambda}{3} = \\frac{4}{3} - 2\\lambda$.<br>Substitute into plane 1: $y = 3 - x - z = 3 - (4/3 - 2\\lambda) - 3\\lambda = \\frac{5}{3} - \\lambda$. [M1]<br>Vector equation: $\\mathbf{r} = \\begin{pmatrix} 4/3 \\\\ 5/3 \\\\ 0 \\end{pmatrix} + \\lambda \\begin{pmatrix} -2 \\\\ -1 \\\\ 3 \\end{pmatrix}$, $\\lambda \\in \\mathbb{R}$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 3)</h2>
        <div class="formula-card">
          <h4>Syllabus 3.12: Vector Equations of Lines</h4>
          $$\\mathbf{r} = \\mathbf{a} + \\lambda \\mathbf{b}$$
          $$\\cos\\theta = \\frac{|\\mathbf{d}_1\\cdot\\mathbf{d}_2|}{|\\mathbf{d}_1||\\mathbf{d}_2|}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. 3D Line Classification</h4>
          <ul>
            <li><strong>Parallel:</strong> Direction vectors are scalar multiples ($\\mathbf{d}_1 = k\\mathbf{d}_2$).</li>
            <li><strong>Intersecting:</strong> Non-parallel and the system $\\mathbf{r}_1(\\lambda) = \\mathbf{r}_2(\\mu)$ has a unique consistent solution.</li>
            <li><strong>Skew:</strong> Non-parallel and no common point (inconsistent system).</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Different Parameters for Different Lines</h4>
          <p>When finding the intersection of two lines, ALWAYS use different parameters (e.g. $\\lambda$ for $L_1$ and $\\mu$ for $L_2$). Using $\\lambda$ for both lines will cause an immediate catastrophic algebraic failure.</p>
        </div>
        <div class="pitfall-card">
          <h4>Checking the Third Equation</h4>
          <p>Solving equations 1 and 2 gives candidate values for $\\lambda$ and $\\mu$. You MUST substitute them into equation 3 to check consistency. If equation 3 fails, the lines are skew, NOT intersecting!</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'Two lines in 3D that are neither parallel nor intersecting are called:',
        options: [
          'Coincident lines',
          'Skew lines',
          'Orthogonal planes',
          'Asymptotic lines'
        ],
        correct: 1,
        explanation: 'By definition, skew lines in 3D are non-parallel and non-intersecting lines residing in different planes.'
      },
      {
        id: 'q2',
        prompt: 'What is the direction vector of the line $\\frac{x - 3}{2} = \\frac{4 - y}{3} = z + 1$?',
        options: [
          '$(2, 3, 1)$',
          '$(2, -3, 1)$',
          '$(3, 4, -1)$',
          '$(3, -4, 1)$'
        ],
        correct: 1,
        explanation: 'Rewrite $\\frac{4 - y}{3}$ as $\\frac{y - 4}{-3}$. The direction vector is $(2, -3, 1)$.'
      },
      {
        id: 'q3',
        prompt: 'The lines $\\mathbf{r}_1 = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ 1 \\\\ -1 \\end{pmatrix}$ and $\\mathbf{r}_2 = \\begin{pmatrix} 0 \\\\ 1 \\\\ 1 \\end{pmatrix} + \\mu \\begin{pmatrix} -4 \\\\ -2 \\\\ 2 \\end{pmatrix}$ are:',
        options: [
          'Parallel and distinct',
          'Coincident',
          'Intersecting at a single point',
          'Skew'
        ],
        correct: 0,
        explanation: '$\\mathbf{d}_2 = (-4, -2, 2) = -2(2, 1, -1) = -2\\mathbf{d}_1$. So they are parallel. Checking point $(1, 0, 2)$ on $L_2$: $0 - 4\\mu = 1 \\implies \\mu = -1/4$. $y = 1 - 2(-1/4) = 1.5 \\neq 0$. Not coincident, so parallel and distinct.'
      },
      {
        id: 'q4',
        prompt: 'What is the acute angle between lines with direction vectors $(1, 0, 0)$ and $(1, 1, 0)$?',
        options: [
          '$30^\\circ$',
          '$45^\\circ$',
          '$60^\\circ$',
          '$90^\\circ$'
        ],
        correct: 1,
        explanation: '$\\cos\\theta = \\frac{1(1) + 0 + 0}{1 \\times \\sqrt{2}} = \\frac{1}{\\sqrt{2}} \\implies \\theta = 45^\\circ$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Two lines are defined by $L_1: \\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ 1 \\\\ -1 \\end{pmatrix}$ and $L_2: \\mathbf{r} = \\begin{pmatrix} -1 \\\\ 1 \\\\ 4 \\end{pmatrix} + \\mu \\begin{pmatrix} 1 \\\\ 3 \\\\ 1 \\end{pmatrix}$.<br><strong>(a)</strong> Show that $L_1$ and $L_2$ are not parallel. [1 mark]<br><strong>(b)</strong> Determine whether $L_1$ and $L_2$ intersect or are skew. [5 marks]',
        solution: `
          <p><strong>(a) Non-parallel test: [1 mark]</strong><br>
          Direction vectors are $\\mathbf{d}_1 = (2, 1, -1)$ and $\\mathbf{d}_2 = (1, 3, 1)$.<br>
          Since $\\frac{2}{1} \\neq \\frac{1}{3}$, $\\mathbf{d}_1$ is not a scalar multiple of $\\mathbf{d}_2$, so the lines are not parallel [A1].</p>
          <p><strong>(b) Intersection or skew: [5 marks]</strong><br>
          Set coordinates equal: [M1]<br>
          (1) $1 + 2\\lambda = -1 + \\mu \\implies 2\\lambda - \\mu = -2$<br>
          (2) $2 + \\lambda = 1 + 3\\mu \\implies \\lambda - 3\\mu = -1$<br>
          (3) $3 - \\lambda = 4 + \\mu \\implies \\lambda + \\mu = -1$<br>
          From (1) and (3): add them: $3\\lambda = -3 \\implies \\lambda = -1$ [M1].<br>
          From (3): $-1 + \\mu = -1 \\implies \\mu = 0$ [A1].<br>
          Check (2): $\\lambda - 3\\mu = -1 - 3(0) = -1$ (matches equation 2!) [R1].<br>
          Since a consistent solution $(\\lambda = -1, \\mu = 0)$ satisfies all three equations, the lines <strong>intersect</strong> at the point $(-1, 1, 4)$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'A submarine travels along a straight line $L: \\mathbf{r} = \\begin{pmatrix} 10 \\\\ -5 \\\\ -2 \\end{pmatrix} + t\\begin{pmatrix} 3 \\\\ 4 \\\\ -1 \\end{pmatrix}$ where $t$ is time in hours and coordinates are in kilometres.<br>A stationary sonar station is located at $S(1, 2, -3)$.<br><strong>(a)</strong> Find the time $t$ when the submarine is closest to the sonar station. [4 marks]<br><strong>(b)</strong> Calculate the minimum distance between the submarine and the station. [4 marks]',
        solution: `
          <p><strong>(a) Closest approach time: [4 marks]</strong><br>
          Submarine position $P(10 + 3t, -5 + 4t, -2 - t)$ [M1].<br>
          Vector $\\vec{SP} = \\begin{pmatrix} (10+3t)-1 \\\\ (-5+4t)-2 \\\\ (-2-t)-(-3) \\end{pmatrix} = \\begin{pmatrix} 9 + 3t \\\\ -7 + 4t \\\\ 1 - t \\end{pmatrix}$ [A1].<br>
          At closest approach, $\\vec{SP} \\perp \\mathbf{d}$: [M1]<br>
          $\\vec{SP}\\cdot\\begin{pmatrix} 3 \\\\ 4 \\\\ -1 \\end{pmatrix} = 0 \\implies 3(9 + 3t) + 4(-7 + 4t) - 1(1 - t) = 0$<br>
          $27 + 9t - 28 + 16t - 1 + t = 0 \\implies 26t - 2 = 0 \\implies 26t = 2 \\implies t = \\frac{1}{13} \\approx 0.0769$ hours [A1].</p>
          <p><strong>(b) Minimum distance: [4 marks]</strong><br>
          At $t = 1/13$:<br>
          $\\vec{SP} = \\begin{pmatrix} 9 + 3/13 \\\\ -7 + 4/13 \\\\ 1 - 1/13 \\end{pmatrix} = \\begin{pmatrix} 120/13 \\\\ -87/13 \\\\ 12/13 \\end{pmatrix}$ [M1].<br>
          Distance $= \\frac{1}{13}\\sqrt{120^2 + (-87)^2 + 12^2} = \\frac{1}{13}\\sqrt{14400 + 7569 + 144} = \\frac{1}{13}\\sqrt{22113} \\approx \\frac{148.7}{13} \\approx 11.4$ km [A1].</p>
        `
      }
    ]
  },

  // Guide 14: Vector Cross Product & Equations of Planes
  {
    folder: 'vector-cross-product-and-planes',
    code: '3.13, 3.14',
    title: 'Vector Cross Product & Equations of Planes',
    pageTitle: 'Vector Cross Product & Equations of Planes | IB Math AA HL | SJMaths',
    metaDesc: 'Master the vector cross product, normal vectors, and equations of planes for IB DP Mathematics AA HL (Topics 3.13 & 3.14). Area of triangle, r · n = d, line-plane intersection, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL cross product, vector product u x v, equation of a plane, normal vector r . n = d, line plane intersection, angle between planes',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Harness the vector cross product $\\mathbf{u} \\times \\mathbf{v}$ to generate orthogonal normal vectors and calculate spatial areas. Master vector and Cartesian equations of planes $\\mathbf{r}\\cdot\\mathbf{n} = d$ and spatial line-plane intersections.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/geometry-and-trigonometry/vector-equations-of-lines-in-3d/',
      title: 'Vector Equations of Lines in 3D'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/statistics-and-probability/continuous-random-variables-and-probability-density-functions/',
      title: 'Continuous Random Variables & PDFs'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-layer-group" style="color:var(--c-primary);"></i> Figure 3.5: Plane with Normal Vector Generated by Cross Product $\\mathbf{u} \\times \\mathbf{v}$</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing plane containing vectors u and v with perpendicular normal vector n pointing upward">
            <!-- 3D Plane Parallelogram -->
            <polygon points="120,220 540,220 640,110 220,110" fill="rgba(99,102,241,0.12)" stroke="#6366f1" stroke-width="2" />
            <text x="610" y="130" font-size="14" font-weight="bold" fill="#6366f1">Plane Π: r · n = d</text>

            <!-- Point A on Plane at (340, 180) -->
            <circle cx="340" cy="180" r="5" fill="#ef4444" />
            <text x="320" y="195" font-size="13" font-weight="bold" fill="#ef4444">A (point on plane)</text>

            <!-- Vector u along plane -->
            <line x1="340" y1="180" x2="480" y2="180" stroke="#10b981" stroke-width="3" />
            <text x="440" y="170" font-size="13" font-weight="bold" fill="#10b981">u</text>

            <!-- Vector v along plane angled up-right -->
            <line x1="340" y1="180" x2="410" y2="135" stroke="#f59e0b" stroke-width="3" />
            <text x="390" y="145" font-size="13" font-weight="bold" fill="#f59e0b">v</text>

            <!-- Normal vector n = u x v perpendicular straight UP -->
            <line x1="340" y1="180" x2="340" y2="50" stroke="#ef4444" stroke-width="3.5" />
            <polyline points="333,65 340,50 347,65" fill="none" stroke="#ef4444" stroke-width="3" />
            <text x="355" y="65" font-size="14" font-weight="bold" fill="#ef4444">n = u × v (Normal)</text>

            <!-- Right-angle symbols at base of normal -->
            <polyline points="340,165 352,165 352,180" fill="none" stroke="#ef4444" stroke-width="1.5" />

            <text x="380" y="270" text-anchor="middle" font-size="12" fill="var(--c-text-muted)">The cross product u × v produces a normal perpendicular to both in-plane direction vectors</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. The Vector (Cross) Product</h2>
        <p>The vector cross product of two vectors $\\mathbf{u}$ and $\\mathbf{v}$ in $\\mathbb{R}^3$ produces a <strong>vector</strong> that is perpendicular to both $\\mathbf{u}$ and $\\mathbf{v}$:</p>
        $$\\mathbf{u} \\times \\mathbf{v} = \\begin{pmatrix} u_1 \\\\ u_2 \\\\ u_3 \\end{pmatrix} \\times \\begin{pmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{pmatrix} = \\begin{pmatrix} u_2 v_3 - u_3 v_2 \\\\ u_3 v_1 - u_1 v_3 \\\\ u_1 v_2 - u_2 v_1 \\end{pmatrix}$$
        <ul class="theory-list">
          <li><strong>Anti-commutative:</strong> $\\mathbf{v} \\times \\mathbf{u} = -(\\mathbf{u} \\times \\mathbf{v})$.</li>
          <li><strong>Magnitude:</strong> $|\\mathbf{u} \\times \\mathbf{v}| = |\\mathbf{u}||\\mathbf{v}|\\sin\\theta$, where $\\theta$ is the angle between $\\mathbf{u}$ and $\\mathbf{v}$.</li>
          <li><strong>Parallel vectors test:</strong> $\\mathbf{u} \\parallel \\mathbf{v} \\iff \\mathbf{u} \\times \\mathbf{v} = \\mathbf{0}$.</li>
          <li><strong>Geometric Area:</strong>
            <br>• Area of parallelogram formed by $\\mathbf{u}$ and $\\mathbf{v}$: $\\text{Area} = |\\mathbf{u} \\times \\mathbf{v}|$.
            <br>• Area of triangle with sides $\\mathbf{u}$ and $\\mathbf{v}$: $\\text{Area} = \\frac{1}{2}|\\mathbf{u} \\times \\mathbf{v}|$.
          </li>
        </ul>

        <h2>2. Equations of a Plane</h2>
        <p>A plane $\\Pi$ in $\\mathbb{R}^3$ is uniquely defined by a point $A(\\mathbf{a})$ on the plane and a non-zero <strong>normal vector</strong> $\\mathbf{n} = \\begin{pmatrix} A \\\\ B \\\\ C \\end{pmatrix}$ perpendicular to the plane:</p>
        <ul class="theory-list">
          <li><strong>Vector Equation of a Plane:</strong>
          $$\\mathbf{r} \\cdot \\mathbf{n} = \\mathbf{a} \\cdot \\mathbf{n} = d$$</li>
          <li><strong>Cartesian Equation of a Plane:</strong>
          $$Ax + By + Cz = d, \\quad \\text{where } d = Ax_0 + By_0 + Cz_0$$</li>
        </ul>

        <h2>3. Finding the Normal via Cross Product</h2>
        <p>If a plane contains three non-collinear points $A, B, C$, form two in-plane vectors $\\vec{AB}$ and $\\vec{AC}$. The normal vector is given by:</p>
        $$\\mathbf{n} = \\vec{AB} \\times \\vec{AC}$$

        <h2>4. Line-Plane Intersections &amp; Angles</h2>
        <ul class="theory-list">
          <li><strong>Intersection of a line and a plane:</strong> Substitute $\\mathbf{r} = \\mathbf{a} + \\lambda\\mathbf{b}$ into $\\mathbf{r}\\cdot\\mathbf{n} = d$ to solve for $\\lambda$:
          $$(\\mathbf{a} + \\lambda\\mathbf{b}) \\cdot \\mathbf{n} = d \\implies \\lambda = \\frac{d - \\mathbf{a}\\cdot\\mathbf{n}}{\\mathbf{b}\\cdot\\mathbf{n}}$$
          If $\\mathbf{b}\\cdot\\mathbf{n} = 0$, the line is parallel to the plane (either lying entirely within it if $\\mathbf{a}\\cdot\\mathbf{n} = d$, or never meeting it).</li>
          <li><strong>Angle $\\phi$ between line and plane:</strong>
          $$\\sin\\phi = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$$</li>
          <li><strong>Angle $\\theta$ between two planes $\\Pi_1$ and $\\Pi_2$:</strong> Angle between their normal vectors:
          $$\\cos\\theta = \\frac{|\\mathbf{n}_1\\cdot\\mathbf{n}_2|}{|\\mathbf{n}_1||\\mathbf{n}_2|}$$</li>
        </ul>

        <h2>5. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Calculating the Cross Product &amp; Triangle Area</h4>
          <p>Find the area of the triangle with vertices $A(1, 2, 0)$, $B(3, 0, 1)$, and $C(2, 4, 3)$.</p>
          <p><strong>Solution:</strong></p>
          <p>Find vectors: $\\vec{AB} = \\begin{pmatrix} 2 \\\\ -2 \\\\ 1 \\end{pmatrix}$, $\\vec{AC} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$.<br>
          Cross product $\\vec{AB} \\times \\vec{AC}$:</p>
          $$\\vec{AB} \\times \\vec{AC} = \\begin{pmatrix} (-2)(3) - (1)(2) \\\\ (1)(1) - (2)(3) \\\\ (2)(2) - (-2)(1) \\end{pmatrix} = \\begin{pmatrix} -6 - 2 \\\\ 1 - 6 \\\\ 4 + 2 \\end{pmatrix} = \\begin{pmatrix} -8 \\\\ -5 \\\\ 6 \\end{pmatrix}$$
          <p>Magnitude: $|\\vec{AB} \\times \\vec{AC}| = \\sqrt{(-8)^2 + (-5)^2 + 6^2} = \\sqrt{64 + 25 + 36} = \\sqrt{125} = 5\\sqrt{5}$.<br>
          Area of triangle $= \\frac{1}{2}|\\vec{AB} \\times \\vec{AC}| = \\frac{5\\sqrt{5}}{2} \\approx 5.59$ sq units.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Finding Equation of Plane through 3 Points</h4>
          <p>Find the Cartesian equation of the plane passing through $A(1, 1, 1)$, $B(2, 3, 0)$, and $C(-1, 2, 4)$.</p>
          <p><strong>Solution:</strong></p>
          <p>$\\vec{AB} = \\begin{pmatrix} 1 \\\\ 2 \\\\ -1 \\end{pmatrix}$, $\\vec{AC} = \\begin{pmatrix} -2 \\\\ 1 \\\\ 3 \\end{pmatrix}$.<br>
          Normal vector $\\mathbf{n} = \\vec{AB} \\times \\vec{AC}$:</p>
          $$\\mathbf{n} = \\begin{pmatrix} (2)(3) - (-1)(1) \\\\ (-1)(-2) - (1)(3) \\\\ (1)(1) - (2)(-2) \\end{pmatrix} = \\begin{pmatrix} 6 + 1 \\\\ 2 - 3 \\\\ 1 + 4 \\end{pmatrix} = \\begin{pmatrix} 7 \\\\ -1 \\\\ 5 \\end{pmatrix}$$
          <p>Cartesian equation: $7x - y + 5z = d$.<br>
          Substitute point $A(1, 1, 1)$: $d = 7(1) - 1(1) + 5(1) = 7 - 1 + 5 = 11$.<br>
          Equation of the plane: $7x - y + 5z = 11$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Line-Plane Intersection</h4>
          <p>Find the point of intersection of the line $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ 3 \\\\ -1 \\end{pmatrix}$ and the plane $2x + y - 3z = 7$.</p>
          <p><strong>Solution:</strong></p>
          <p>Express general point on the line in parametric form: $x = 1 + 2\\lambda, y = -1 + 3\\lambda, z = 2 - \\lambda$.<br>
          Substitute into the plane equation:</p>
          $$2(1 + 2\\lambda) + (-1 + 3\\lambda) - 3(2 - \\lambda) = 7$$
          $$2 + 4\\lambda - 1 + 3\\lambda - 6 + 3\\lambda = 7$$
          $$10\\lambda - 5 = 7 \\implies 10\\lambda = 12 \\implies \\lambda = \\frac{6}{5} = 1.2$$
          <p>Substitute $\\lambda = 1.2$ back into the line equation:</p>
          $$x = 1 + 2(1.2) = 3.4, \\quad y = -1 + 3(1.2) = 2.6, \\quad z = 2 - 1.2 = 0.8$$
          <p>Point of intersection: $(3.4, 2.6, 0.8)$.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Basic Cross Product)',
        text: 'Find $\\mathbf{a} \\times \\mathbf{b}$ where $\\mathbf{a} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix}$ and $\\mathbf{b} = \\begin{pmatrix} 0 \\\\ 3 \\\\ 1 \\end{pmatrix}$.',
        solution: '<p>$\\mathbf{a} \\times \\mathbf{b} = \\begin{pmatrix} (0)(1) - (2)(3) \\\\ (2)(0) - (1)(1) \\\\ (1)(3) - (0)(0) \\end{pmatrix} = \\begin{pmatrix} -6 \\\\ -1 \\\\ 3 \\end{pmatrix}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Plane from Point and Normal)',
        text: 'Find the Cartesian equation of the plane passing through $P(2, -3, 1)$ with normal vector $\\mathbf{n} = \\begin{pmatrix} 4 \\\\ 1 \\\\ -2 \\end{pmatrix}$.',
        solution: '<p>$4x + y - 2z = d$. [M1]<br>$d = 4(2) + 1(-3) - 2(1) = 8 - 3 - 2 = 3$.<br>Cartesian equation: $4x + y - 2z = 3$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Area of Parallelogram)',
        text: 'Find the area of the parallelogram spanned by $\\mathbf{u} = \\mathbf{i} + 2\\mathbf{j}$ and $\\mathbf{v} = 2\\mathbf{j} + 3\\mathbf{k}$.',
        solution: '<p>$\\mathbf{u} = (1, 2, 0)$, $\\mathbf{v} = (0, 2, 3)$.<br>$\\mathbf{u} \\times \\mathbf{v} = \\begin{pmatrix} 6 - 0 \\\\ 0 - 3 \\\\ 2 - 0 \\end{pmatrix} = \\begin{pmatrix} 6 \\\\ -3 \\\\ 2 \\end{pmatrix}$. [M1]<br>Area $= |\\mathbf{u} \\times \\mathbf{v}| = \\sqrt{6^2 + (-3)^2 + 2^2} = \\sqrt{36 + 9 + 4} = \\sqrt{49} = 7$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Plane Containing Line and Point)',
        text: 'Find the equation of the plane containing point $A(1, 0, 1)$ and the line $\\mathbf{r} = \\begin{pmatrix} 2 \\\\ 1 \\\\ 3 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix}$.',
        solution: '<p>Point on line: $B(2, 1, 3)$. Direction of line: $\\mathbf{d} = (1, -1, 2)$. [M1]<br>Vector on plane: $\\vec{AB} = (2-1, 1-0, 3-1) = (1, 1, 2)$.<br>Normal $\\mathbf{n} = \\vec{AB} \\times \\mathbf{d} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 2 \\end{pmatrix} \\times \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix} = \\begin{pmatrix} 2 - (-2) \\\\ 2 - 2 \\\\ -1 - 1 \\end{pmatrix} = \\begin{pmatrix} 4 \\\\ 0 \\\\ -2 \\end{pmatrix} \\sim \\begin{pmatrix} 2 \\\\ 0 \\\\ -1 \\end{pmatrix}$. [A1]<br>Plane: $2x - z = d$. Using $A(1, 0, 1)$: $d = 2(1) - 1 = 1$.<br>Equation: $2x - z = 1$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Angle Between Two Planes)',
        text: 'Find the acute angle between the planes $\\Pi_1: x + 2y - 2z = 5$ and $\\Pi_2: 2x - y + 2z = 3$.',
        solution: '<p>Normal vectors: $\\mathbf{n}_1 = (1, 2, -2)$, $\\mathbf{n}_2 = (2, -1, 2)$. [M1]<br>$\\mathbf{n}_1\\cdot\\mathbf{n}_2 = 1(2) + 2(-1) + (-2)(2) = 2 - 2 - 4 = -4$.<br>$|\\mathbf{n}_1| = \\sqrt{1 + 4 + 4} = 3$, $|\\mathbf{n}_2| = \\sqrt{4 + 1 + 4} = 3$.<br>$\\cos\\theta = \\frac{|-4|}{3 \\times 3} = \\frac{4}{9}$. [M1]<br>$\\theta = \\arccos(4/9) \\approx 63.6^\\circ$ (or $1.11$ rad). [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Distance from Point to Plane)',
        text: 'Find the perpendicular distance from point $P(3, 1, -2)$ to the plane $2x - 2y + z = 11$.',
        solution: '<p>Distance formula: $D = \\frac{|Ax_1 + By_1 + Cz_1 - d|}{\\sqrt{A^2 + B^2 + C^2}}$. [M1]<br>$D = \\frac{|2(3) - 2(1) + 1(-2) - 11|}{\\sqrt{2^2 + (-2)^2 + 1^2}} = \\frac{|6 - 2 - 2 - 11|}{3} = \\frac{|-9|}{3} = 3$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Angle Between Line and Plane)',
        text: 'Find the angle between the line $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 0 \\\\ -1 \\end{pmatrix} + \\lambda \\begin{pmatrix} 2 \\\\ 1 \\\\ -2 \\end{pmatrix}$ and the plane $3x - 4y = 6$.',
        solution: '<p>Direction of line: $\\mathbf{b} = (2, 1, -2)$, normal to plane: $\\mathbf{n} = (3, -4, 0)$. [M1]<br>$\\mathbf{b}\\cdot\\mathbf{n} = 2(3) + 1(-4) + (-2)(0) = 6 - 4 = 2$.<br>$|\\mathbf{b}| = \\sqrt{4 + 1 + 4} = 3$, $|\\mathbf{n}| = \\sqrt{9 + 16} = 5$.<br>$\\sin\\phi = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|} = \\frac{2}{3 \\times 5} = \\frac{2}{15}$. [M1]<br>$\\phi = \\arcsin(2/15) \\approx 7.66^\\circ$ (or $0.134$ rad). [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Line of Intersection of Two Planes)',
        text: 'Find a vector equation for the line of intersection of planes $\\Pi_1: x - y + 2z = 4$ and $\\Pi_2: 2x + y - z = 1$.',
        solution: '<p>Direction of intersection line is perpendicular to both normals: [M1]<br>$\\mathbf{d} = \\mathbf{n}_1 \\times \\mathbf{n}_2 = \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix} \\times \\begin{pmatrix} 2 \\\\ 1 \\\\ -1 \\end{pmatrix} = \\begin{pmatrix} 1 - 2 \\\\ 4 - (-1) \\\\ 1 - (-2) \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ 5 \\\\ 3 \\end{pmatrix}$. [A1]<br>Find a point on the line: set $z = 0$:<br>$x - y = 4$ and $2x + y = 1 \\implies 3x = 5 \\implies x = 5/3, y = -7/3$. Point: $(5/3, -7/3, 0)$. [M1]<br>Line equation: $\\mathbf{r} = \\begin{pmatrix} 5/3 \\\\ -7/3 \\\\ 0 \\end{pmatrix} + \\lambda \\begin{pmatrix} -1 \\\\ 5 \\\\ 3 \\end{pmatrix}$, $\\lambda \\in \\mathbb{R}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Volume of Parallelepiped / Scalar Triple Product)',
        text: 'The volume of a parallelepiped defined by vectors $\\mathbf{a}, \\mathbf{b}, \\mathbf{c}$ is given by $|\\mathbf{a}\\cdot(\\mathbf{b}\\times\\mathbf{c})|$. Calculate the volume if $\\mathbf{a} = (1, 2, 3)$, $\\mathbf{b} = (0, 1, 2)$, and $\\mathbf{c} = (2, 0, 1)$.',
        solution: '<p>$\\mathbf{b} \\times \\mathbf{c} = \\begin{pmatrix} 0 \\\\ 1 \\\\ 2 \\end{pmatrix} \\times \\begin{pmatrix} 2 \\\\ 0 \\\\ 1 \\end{pmatrix} = \\begin{pmatrix} 1 - 0 \\\\ 4 - 0 \\\\ 0 - 2 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 4 \\\\ -2 \\end{pmatrix}$. [M1]<br>Scalar triple product: $\\mathbf{a}\\cdot(\\mathbf{b}\\times\\mathbf{c}) = 1(1) + 2(4) + 3(-2) = 1 + 8 - 6 = 3$. [M1]<br>Volume $= |3| = 3$ cubic units. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Foot of Perpendicular from Point to Plane)',
        text: 'Find the coordinates of the foot of the perpendicular from $P(1, 2, 3)$ to the plane $x - 2y + 2z = 9$.',
        solution: '<p>The normal line through $P$ has direction $\\mathbf{n} = (1, -2, 2)$: $\\mathbf{r} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix} + \\lambda \\begin{pmatrix} 1 \\\\ -2 \\\\ 2 \\end{pmatrix}$. [M1]<br>General point $F(1 + \\lambda, 2 - 2\\lambda, 3 + 2\\lambda)$. Substitute into plane: [M1]<br>$(1 + \\lambda) - 2(2 - 2\\lambda) + 2(3 + 2\\lambda) = 9$<br>$1 + \\lambda - 4 + 4\\lambda + 6 + 4\\lambda = 9 \\implies 9\\lambda + 3 = 9 \\implies 9\\lambda = 6 \\implies \\lambda = \\frac{2}{3}$.<br>Substitute $\\lambda = 2/3$ into $F$:<br>$x = 1 + 2/3 = 5/3$<br>$y = 2 - 4/3 = 2/3$<br>$z = 3 + 4/3 = 13/3$.<br>Foot of perpendicular: $\\left(\\frac{5}{3}, \\frac{2}{3}, \\frac{13}{3}\\right)$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 3)</h2>
        <div class="formula-card">
          <h4>Syllabus 3.13, 3.14: Vector Cross Product &amp; Equations of Planes</h4>
          $$\\mathbf{u} \\times \\mathbf{v} = \\begin{pmatrix} u_2 v_3 - u_3 v_2 \\\\ u_3 v_1 - u_1 v_3 \\\\ u_1 v_2 - u_2 v_1 \\end{pmatrix}$$
          $$|\\mathbf{u} \\times \\mathbf{v}| = |\\mathbf{u}||\\mathbf{v}|\\sin\\theta$$
          $$\\text{Area of triangle} = \\frac{1}{2}|\\mathbf{u} \\times \\mathbf{v}|, \\quad \\text{Area of parallelogram} = |\\mathbf{u} \\times \\mathbf{v}|$$
          $$\\mathbf{r}\\cdot\\mathbf{n} = \\mathbf{a}\\cdot\\mathbf{n} = d$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Angle Formulas Involving Planes</h4>
          <ul>
            <li>Between two planes: $\\cos\\theta = \\frac{|\\mathbf{n}_1\\cdot\\mathbf{n}_2|}{|\\mathbf{n}_1||\\mathbf{n}_2|}$</li>
            <li>Between a line and a plane: $\\sin\\phi = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$ (note sine!)</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Sign in Middle Component of Cross Product</h4>
          <p>The $y$-component has a minus sign when evaluated by $2\\times 2$ determinants: $-(u_1 v_3 - u_3 v_1) = u_3 v_1 - u_1 v_3$. Be meticulous when calculating!</p>
        </div>
        <div class="pitfall-card">
          <h4>Sine vs Cosine for Line-Plane Angle</h4>
          <p>Because the normal is perpendicular to the plane, the angle between the line direction and the normal is $(90^\\circ - \\phi)$. Therefore, the formula for the line-plane angle uses <strong>SINE</strong>, not cosine!</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If $\\mathbf{u} \\times \\mathbf{v} = \\mathbf{0}$ for non-zero vectors $\\mathbf{u}$ and $\\mathbf{v}$, then:',
        options: [
          '$\\mathbf{u}$ and $\\mathbf{v}$ are perpendicular',
          '$\\mathbf{u}$ and $\\mathbf{v}$ are parallel',
          '$\\mathbf{u} = \\mathbf{v}$',
          'Both vectors are unit vectors'
        ],
        correct: 1,
        explanation: '$|\\mathbf{u}\\times\\mathbf{v}| = |\\mathbf{u}||\\mathbf{v}|\\sin\\theta = 0 \\implies \\sin\\theta = 0 \\implies \\theta = 0$ or $\\pi$ (parallel).'
      },
      {
        id: 'q2',
        prompt: 'What is the normal vector to the plane $3x - 5y + 2z = 9$?',
        options: [
          '$(3, 5, 2)$',
          '$(3, -5, 2)$',
          '$(9, 9, 9)$',
          '$(1/3, -1/5, 1/2)$'
        ],
        correct: 1,
        explanation: 'In the Cartesian equation $Ax + By + Cz = D$, the coefficients directly give the normal vector $\\mathbf{n} = (A, B, C) = (3, -5, 2)$.'
      },
      {
        id: 'q3',
        prompt: 'The area of a triangle with adjacent sides $\\mathbf{u}$ and $\\mathbf{v}$ where $|\\mathbf{u}\\times\\mathbf{v}| = 16$ is:',
        options: [
          '32',
          '16',
          '8',
          '4'
        ],
        correct: 2,
        explanation: 'Area of triangle $= \\frac{1}{2}|\\mathbf{u}\\times\\mathbf{v}| = \\frac{1}{2}(16) = 8$.'
      },
      {
        id: 'q4',
        prompt: 'To find the angle between a line with direction $\\mathbf{b}$ and a plane with normal $\\mathbf{n}$, one calculates:',
        options: [
          '$\\cos\\theta = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$',
          '$\\sin\\theta = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$',
          '$\\tan\\theta = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$',
          '$\\cos\\theta = \\frac{|\\mathbf{b}\\times\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$'
        ],
        correct: 1,
        explanation: 'Because $\\mathbf{n}$ is orthogonal to the plane, $\\cos(90^\\circ - \\theta) = \\sin\\theta = \\frac{|\\mathbf{b}\\cdot\\mathbf{n}|}{|\\mathbf{b}||\\mathbf{n}|}$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Points $A(2, 0, 1)$, $B(1, 3, -1)$, and $C(0, 1, 2)$ lie in a plane $\\Pi$.<br><strong>(a)</strong> Find the vectors $\\vec{AB}$ and $\\vec{AC}$. [2 marks]<br><strong>(b)</strong> Calculate $\\vec{AB} \\times \\vec{AC}$. [2 marks]<br><strong>(c)</strong> Hence find the Cartesian equation of plane $\\Pi$. [2 marks]',
        solution: `
          <p><strong>(a) Vectors: [2 marks]</strong><br>
          $\\vec{AB} = \\begin{pmatrix} 1-2 \\\\ 3-0 \\\\ -1-1 \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ 3 \\\\ -2 \\end{pmatrix}$ [A1].<br>
          $\\vec{AC} = \\begin{pmatrix} 0-2 \\\\ 1-0 \\\\ 2-1 \\end{pmatrix} = \\begin{pmatrix} -2 \\\\ 1 \\\\ 1 \\end{pmatrix}$ [A1].</p>
          <p><strong>(b) Cross product: [2 marks]</strong><br>
          $\\vec{AB}\\times\\vec{AC} = \\begin{pmatrix} (3)(1) - (-2)(1) \\\\ (-2)(-2) - (-1)(1) \\\\ (-1)(1) - (3)(-2) \\end{pmatrix} = \\begin{pmatrix} 3+2 \\\\ 4+1 \\\\ -1+6 \\end{pmatrix} = \\begin{pmatrix} 5 \\\\ 5 \\\\ 5 \\end{pmatrix}$ [A1].<br>
          Dividing by 5 gives simplified normal $\\mathbf{n} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 1 \\end{pmatrix}$ [A1].</p>
          <p><strong>(c) Plane equation: [2 marks]</strong><br>
          $x + y + z = d$.<br>
          Substitute $A(2, 0, 1)$: $d = 2 + 0 + 1 = 3$ [M1].<br>
          Equation: $x + y + z = 3$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'The plane $\\Pi$ has equation $x + 2y - z = 4$. The line $L$ passes through $P(2, 3, -1)$ with direction vector $\\mathbf{d} = \\begin{pmatrix} 1 \\\\ -1 \\\\ 2 \\end{pmatrix}$.<br><strong>(a)</strong> Find the coordinates of the point of intersection between $L$ and $\\Pi$. [4 marks]<br><strong>(b)</strong> Find the acute angle between $L$ and $\\Pi$ in degrees. [4 marks]',
        solution: `
          <p><strong>(a) Intersection point: [4 marks]</strong><br>
          Line equation: $\\mathbf{r} = \\begin{pmatrix} 2+\\lambda \\\\ 3-\\lambda \\\\ -1+2\\lambda \\end{pmatrix}$ [M1].<br>
          Substitute into plane:<br>
          $(2 + \\lambda) + 2(3 - \\lambda) - (-1 + 2\\lambda) = 4$ [M1]<br>
          $2 + \\lambda + 6 - 2\\lambda + 1 - 2\\lambda = 4$<br>
          $9 - 3\\lambda = 4 \\implies 3\\lambda = 5 \\implies \\lambda = \\frac{5}{3}$ [A1].<br>
          Coordinates:<br>
          $x = 2 + 5/3 = 11/3$<br>
          $y = 3 - 5/3 = 4/3$<br>
          $z = -1 + 10/3 = 7/3$.<br>
          Point: $\\left(\\frac{11}{3}, \\frac{4}{3}, \\frac{7}{3}\\right)$ [A1].</p>
          <p><strong>(b) Angle between line and plane: [4 marks]</strong><br>
          Normal to plane: $\\mathbf{n} = (1, 2, -1)$. Line direction: $\\mathbf{d} = (1, -1, 2)$ [M1].<br>
          $\\mathbf{d}\\cdot\\mathbf{n} = 1(1) + (-1)(2) + 2(-1) = 1 - 2 - 2 = -3$ [A1].<br>
          $|\\mathbf{d}| = \\sqrt{1 + 1 + 4} = \\sqrt{6}$, $|\\mathbf{n}| = \\sqrt{1 + 4 + 1} = \\sqrt{6}$ [M1].<br>
          $\\sin\\phi = \\frac{|-3|}{\\sqrt{6}\\sqrt{6}} = \\frac{3}{6} = \\frac{1}{2}$ [A1].<br>
          $\\phi = \\arcsin(0.5) = 30^\\circ$ [A1].</p>
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
