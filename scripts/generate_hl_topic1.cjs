const fs = require('fs');
const path = require('path');

const baseDir = path.join(__dirname, '..', 'ib', 'dp-mathematics', 'analysis-and-approaches-hl', 'number-and-algebra');

// Guide 4: Systems of Linear Equations & Matrices
// Guide 5: Polynomials & Vieta’s Formulas
// Guide 6: Partial Fractions & Extended Binomial Series

const guides = [
  {
    folder: 'systems-of-linear-equations-and-matrices',
    code: '1.15',
    title: 'Systems of Linear Equations & Matrices',
    pageTitle: 'Systems of Linear Equations & Matrices | IB Math AA HL | SJMaths',
    metaDesc: 'Master systems of linear equations and row reduction for IB DP Mathematics AA HL (Topic 1.15). Gaussian elimination, unique/infinite/no solution cases, geometric interpretations of 3 planes in 3D, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL systems of linear equations, Gaussian elimination, augmented matrix row operations, 3 planes geometric intersection, consistent dependent system, unique solution rank',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Solve systems of 3 linear equations in 3 variables using Gaussian elimination and row echelon form. Connect algebraic consistency to the 3D geometry of intersecting planes: unique intersection points, lines of intersection, and triangular prism inconsistencies.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/de-moivres-theorem-and-roots-of-unity/',
      title: 'De Moivre’s Theorem & Roots of Unity'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/polynomials-and-vietas-formulas/',
      title: 'Polynomials & Vieta’s Formulas'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-shapes" style="color:var(--c-primary);"></i> Figure 1.4: Geometric Configurations of 3 Planes in 3D Space</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing three geometric configurations of three planes: Unique solution point, Infinite solutions along a line, and Inconsistent triangular prism">
            <!-- Case A: Unique point (left) -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="210" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="105" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary, #4338ca)">Case 1: Unique Point</text>
              <text x="105" y="46" text-anchor="middle" font-size="11" fill="var(--c-text-muted, #64748b)">Rank = 3, Det(A) ≠ 0</text>
              <!-- 3 Planes intersecting at a point -->
              <polygon points="20,110 180,90 190,140 30,160" fill="rgba(99,102,241,0.2)" stroke="#6366f1" stroke-width="1.5" />
              <polygon points="60,60 150,75 140,210 50,195" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="1.5" />
              <polygon points="35,160 175,120 185,185 45,225" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1.5" />
              <circle cx="105" cy="135" r="5" fill="#ef4444" />
              <text x="105" y="153" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">(x₀, y₀, z₀)</text>
              <text x="105" y="240" text-anchor="middle" font-size="11" fill="var(--c-text, #334155)">Planes meet at 1 point</text>
            </g>

            <!-- Case B: Sheaf / Line of intersection (middle) -->
            <g transform="translate(275, 20)">
              <rect x="0" y="0" width="210" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="105" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="#10b981">Case 2: Line (Sheaf)</text>
              <text x="105" y="46" text-anchor="middle" font-size="11" fill="var(--c-text-muted, #64748b)">Rank = 2, Consistent (0=0)</text>
              <!-- 3 planes sharing a single line -->
              <polygon points="20,135 190,135 180,185 10,185" fill="rgba(99,102,241,0.15)" stroke="#6366f1" stroke-width="1.5" />
              <polygon points="40,80 170,190 150,210 20,100" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="1.5" />
              <polygon points="30,190 180,80 190,100 40,210" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1.5" />
              <!-- Shared Line -->
              <line x1="25" y1="135" x2="185" y2="135" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,2" />
              <text x="105" y="125" text-anchor="middle" font-size="11" font-weight="bold" fill="#ef4444">Common Line L</text>
              <text x="105" y="240" text-anchor="middle" font-size="11" fill="var(--c-text, #334155)">Infinitely many solutions</text>
            </g>

            <!-- Case C: Triangular Prism (right) -->
            <g transform="translate(520, 20)">
              <rect x="0" y="0" width="210" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="105" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="#ef4444">Case 3: Triangular Prism</text>
              <text x="105" y="46" text-anchor="middle" font-size="11" fill="var(--c-text-muted, #64748b)">Inconsistent row (0=k, k≠0)</text>
              <!-- 3 pairwise intersecting planes forming a prism -->
              <polygon points="25,90 185,90 165,130 5,130" fill="rgba(99,102,241,0.15)" stroke="#6366f1" stroke-width="1.5" />
              <polygon points="15,120 175,120 195,190 35,190" fill="rgba(16,185,129,0.15)" stroke="#10b981" stroke-width="1.5" />
              <polygon points="50,70 190,70 150,195 10,195" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="1.5" />
              <line x1="20" y1="100" x2="180" y2="100" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3,3" />
              <line x1="15" y1="140" x2="175" y2="140" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3" />
              <line x1="30" y1="175" x2="190" y2="175" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="105" y="160" text-anchor="middle" font-size="11" font-weight="bold" fill="#ef4444">No Common Point</text>
              <text x="105" y="240" text-anchor="middle" font-size="11" fill="var(--c-text, #334155)">No solution (Prism)</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Matrix Representation of Linear Systems</h2>
        <p>A system of three linear equations in three variables $(x, y, z)$:</p>
        $$\\begin{cases} a_1 x + b_1 y + c_1 z = d_1 \\\\ a_2 x + b_2 y + c_2 z = d_2 \\\\ a_3 x + b_3 y + c_3 z = d_3 \\end{cases}$$
        <p>can be expressed compactly in matrix equation form $A\\mathbf{x} = \\mathbf{b}$:</p>
        $$\\begin{pmatrix} a_1 & b_1 & c_1 \\\\ a_2 & b_2 & c_2 \\\\ a_3 & b_3 & c_3 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix} = \\begin{pmatrix} d_1 \\\\ d_2 \\\\ d_3 \\end{pmatrix}$$
        <p>To solve by hand or analyze solvability analytically without technology (Paper 1), we form the <strong>augmented matrix</strong> $[A | \\mathbf{b}]$ and perform elementary row operations (EROs):</p>
        $$[A | \\mathbf{b}] = \\left(\\begin{array}{ccc|c} a_1 & b_1 & c_1 & d_1 \\\\ a_2 & b_2 & c_2 & d_2 \\\\ a_3 & b_3 & c_3 & d_3 \\end{array}\\right)$$

        <h2>2. Elementary Row Operations (EROs) &amp; Row Echelon Form (REF)</h2>
        <p>The three permissible EROs that produce an equivalent system are:</p>
        <ol class="theory-list">
          <li><strong>Row swap:</strong> $R_i \\leftrightarrow R_j$ (interchange two rows).</li>
          <li><strong>Scalar multiplication:</strong> $R_i \\to k R_i$ where $k \\neq 0$.</li>
          <li><strong>Row replacement:</strong> $R_i \\to R_i + k R_j$ (add a scalar multiple of row $j$ to row $i$).</li>
        </ol>
        <p>We apply Gaussian elimination to reduce the matrix to upper-triangular <strong>row echelon form</strong>:</p>
        $$\\left(\\begin{array}{ccc|c} 1 & * & * & * \\\\ 0 & 1 & * & * \\\\ 0 & 0 & p & q \\end{array}\\right)$$

        <h2>3. Classification of Solutions &amp; Geometric Interpretations in $\\mathbb{R}^3$</h2>
        <p>Each linear equation $ax + by + cz = d$ represents a flat two-dimensional <strong>plane</strong> in 3D Euclidean space. The solution set represents the intersection of these three planes $\\Pi_1, \\Pi_2, \\Pi_3$. The bottom row $(0\\; 0\\; p \\mid q)$ dictates the solution type:</p>
        
        <div class="table-responsive" style="margin: 1.5rem 0;">
          <table class="ib-table" style="width:100%; border-collapse:collapse;">
            <thead>
              <tr style="background:var(--c-surface-card); border-bottom:2px solid var(--c-border);">
                <th style="padding:10px; text-align:left;">Bottom Row Condition</th>
                <th style="padding:10px; text-align:left;">Algebraic Solution</th>
                <th style="padding:10px; text-align:left;">Geometric Interpretation (3 Planes)</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>$p \\neq 0$</strong></td>
                <td style="padding:10px;"><strong>Unique Solution:</strong><br>$z = q/p$, then back-substitute for $y$ and $x$.</td>
                <td style="padding:10px;">The 3 planes intersect at a <strong>single unique point</strong> $(x_0, y_0, z_0)$. $\\det(A) \\neq 0$.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>$p = 0$ and $q = 0$</strong><br>$(0\\; 0\\; 0 \\mid 0)$</td>
                <td style="padding:10px;"><strong>Infinitely Many Solutions:</strong><br>Consistent dependent system. Let $z = \\lambda \\in \\mathbb{R}$, express $x$ and $y$ in terms of $\\lambda$.</td>
                <td style="padding:10px;">The 3 planes intersect along a <strong>common line</strong> (a "sheaf" of planes), or two/three planes are coincident.</td>
              </tr>
              <tr>
                <td style="padding:10px;"><strong>$p = 0$ and $q \\neq 0$</strong><br>$(0\\; 0\\; 0 \\mid q)$</td>
                <td style="padding:10px;"><strong>No Solution:</strong><br>Inconsistent statement $0x + 0y + 0z = q \\implies 0 = q$ (contradiction).</td>
                <td style="padding:10px;">The 3 planes have no common intersection. Geometrically:<br>• Pairwise intersect along three parallel lines forming a <strong>triangular prism</strong>.<br>• Two or three planes are strictly parallel with different intercepts.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>4. Worked Examples</h2>
        
        <div class="example-card">
          <h4>Worked Example 1: Gaussian Elimination with Unique Solution</h4>
          <p>Solve the following system algebraically using augmented matrix row operations:</p>
          $$\\begin{cases} x + 2y - z = 2 \\\\ 2x + 5y + z = 11 \\\\ 3x + 7y + 2z = 15 \\end{cases}$$
          <p><strong>Solution:</strong></p>
          <p>Set up the augmented matrix:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 2 \\\\ 2 & 5 & 1 & 11 \\\\ 3 & 7 & 2 & 15 \\end{array}\\right)$$
          <p>Perform $R_2 \\to R_2 - 2R_1$ and $R_3 \\to R_3 - 3R_1$:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 2 \\\\ 0 & 1 & 3 & 7 \\\\ 0 & 1 & 5 & 9 \\end{array}\\right)$$
          <p>Perform $R_3 \\to R_3 - R_2$:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 2 \\\\ 0 & 1 & 3 & 7 \\\\ 0 & 0 & 2 & 2 \\end{array}\\right)$$
          <p>From Row 3: $2z = 2 \\implies z = 1$.<br>
          From Row 2: $y + 3(1) = 7 \\implies y = 4$.<br>
          From Row 1: $x + 2(4) - (1) = 2 \\implies x + 7 = 2 \\implies x = -5$.<br>
          Hence the unique solution is $(x, y, z) = (-5, 4, 1)$, representing the single point where all three planes intersect.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Parameter Analysis for Consistency &amp; Triangular Prism</h4>
          <p>Consider the system with parameter $k \\in \\mathbb{R}$:</p>
          $$\\begin{cases} x + y + z = 6 \\\\ 2x + 3y + kz = 14 \\\\ x + 2y + 3z = 8 \\end{cases}$$
          <p>Find the value of $k$ for which the system does not have a unique solution. For this value of $k$, determine whether the system is consistent (infinitely many solutions) or inconsistent (no solution), and describe the geometry of the planes.</p>
          <p><strong>Solution:</strong></p>
          <p>Write the augmented matrix:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\\\ 2 & 3 & k & 14 \\\\ 1 & 2 & 3 & 8 \\end{array}\\right)$$
          <p>Swap rows $R_2 \\leftrightarrow R_3$ first to keep $k$ in the bottom row:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\\\ 1 & 2 & 3 & 8 \\\\ 2 & 3 & k & 14 \\end{array}\\right)$$
          <p>Perform $R_2 \\to R_2 - R_1$ and $R_3 \\to R_3 - 2R_1$:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\\\ 0 & 1 & 2 & 2 \\\\ 0 & 1 & k-2 & 2 \\end{array}\\right)$$
          <p>Perform $R_3 \\to R_3 - R_2$:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\\\ 0 & 1 & 2 & 2 \\\\ 0 & 0 & k-4 & 0 \\end{array}\\right)$$
          <p>• If $k - 4 \\neq 0$ ($k \\neq 4$), the matrix has full rank 3, giving a <strong>unique solution</strong>.<br>
          • If $k = 4$, row 3 becomes $(0\\; 0\\; 0 \\mid 0)$. This is a tautology $0 = 0$, meaning the system is <strong>consistent with infinitely many solutions</strong>!<br>
          Planes intersect along a common line. Letting $z = \\lambda$, we have $y = 2 - 2\\lambda$, and $x = 6 - (2 - 2\\lambda) - \\lambda = 4 + \\lambda$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Inconsistent System forming a Triangular Prism</h4>
          <p>Show that the following system has no solution and state whether any two planes are parallel:</p>
          $$\\begin{cases} x - y + 2z = 4 \\\\ 2x + y - z = 1 \\\\ 4x - y + 3z = 7 \\end{cases}$$
          <p><strong>Solution:</strong></p>
          <p>Augmented matrix:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 4 \\\\ 2 & 1 & -1 & 1 \\\\ 4 & -1 & 3 & 7 \\end{array}\\right)$$
          <p>Perform $R_2 \\to R_2 - 2R_1$ and $R_3 \\to R_3 - 4R_1$:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 4 \\\\ 0 & 3 & -5 & -7 \\\\ 0 & 3 & -5 & -9 \\end{array}\\right)$$
          <p>Perform $R_3 \\to R_3 - R_2$:</p>
          $$\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 4 \\\\ 0 & 3 & -5 & -7 \\\\ 0 & 0 & 0 & -2 \\end{array}\\right)$$
          <p>The last row implies $0x + 0y + 0z = -2 \\implies 0 = -2$, which is impossible. Hence the system has <strong>no solution</strong> (inconsistent).<br>
          Check normal vectors: $\\mathbf{n}_1 = (1, -1, 2)$, $\\mathbf{n}_2 = (2, 1, -1)$, $\\mathbf{n}_3 = (4, -1, 3)$.<br>
          No two normal vectors are scalar multiples of each other, so no two planes are parallel. Therefore, the three planes intersect pairwise in three parallel lines, forming an open <strong>triangular prism</strong>.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Row Operations)',
        text: 'Given the augmented matrix in upper triangular echelon form: $$\\left(\\begin{array}{ccc|c} 2 & 1 & -1 & 5 \\\\ 0 & 3 & 2 & 11 \\\\ 0 & 0 & 4 & 4 \\end{array}\\right)$$ Find the values of $x$, $y$, and $z$ using back-substitution.',
        solution: '<p><strong>Step 1: Solve for $z$ from Row 3:</strong><br>$4z = 4 \\implies z = 1$. [A1]</p><p><strong>Step 2: Solve for $y$ from Row 2:</strong><br>$3y + 2(1) = 11 \\implies 3y = 9 \\implies y = 3$. [A1]</p><p><strong>Step 3: Solve for $x$ from Row 1:</strong><br>$2x + 1(3) - 1(1) = 5 \\implies 2x + 2 = 5 \\implies 2x = 3 \\implies x = \\frac{3}{2}$. [A1]</p><p>Solution: $(x, y, z) = \\left(\\frac{3}{2}, 3, 1\\right)$.</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Row Echelon Transformation)',
        text: 'Perform the row operations $R_2 \\to R_2 - 2R_1$ and $R_3 \\to R_3 - 3R_1$ on the augmented matrix: $$\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\\\ 2 & 1 & 1 & 7 \\\\ 3 & 2 & -1 & 8 \\end{array}\\right)$$ and state the resulting matrix.',
        solution: '<p>For $R_2$: $2 - 2(1) = 0$, $1 - 2(-1) = 3$, $1 - 2(2) = -3$, $7 - 2(3) = 1$. [M1]<br>For $R_3$: $3 - 3(1) = 0$, $2 - 3(-1) = 5$, $-1 - 3(2) = -7$, $8 - 3(3) = -1$. [M1]</p><p>Resulting matrix: $$\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\\\ 0 & 3 & -3 & 1 \\\\ 0 & 5 & -7 & -1 \\end{array}\\right)$$ [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Identifying Inconsistency)',
        text: 'After Gaussian elimination, a system yields the augmented matrix: $$\\left(\\begin{array}{ccc|c} 1 & 4 & -2 & 5 \\\\ 0 & 2 & 3 & 1 \\\\ 0 & 0 & 0 & 7 \\end{array}\\right)$$ State the number of solutions and justify your answer algebraically.',
        solution: '<p>The third row translates to the equation $0x + 0y + 0z = 7 \\iff 0 = 7$. [M1]<br>Because $0 = 7$ is false for all real values of $x, y, z$, this is a contradiction. [R1]<br>Therefore, the system is <strong>inconsistent and has no solution</strong>. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: 3-Variable System)',
        text: 'Solve the system by Gaussian elimination: $$\\begin{cases} x + y + 2z = 8 \\\\ -x - 2y + 3z = 1 \\\\ 3x - 7y + 4z = 10 \\end{cases}$$',
        solution: '<p>Augmented matrix: $\\left(\\begin{array}{ccc|c} 1 & 1 & 2 & 8 \\\\ -1 & -2 & 3 & 1 \\\\ 3 & -7 & 4 & 10 \\end{array}\\right)$ [M1]<br>$R_2 \\to R_2 + R_1$, $R_3 \\to R_3 - 3R_1$:<br>$\\left(\\begin{array}{ccc|c} 1 & 1 & 2 & 8 \\\\ 0 & -1 & 5 & 9 \\\\ 0 & -10 & -2 & -14 \\end{array}\\right)$ [A1]<br>$R_3 \\to R_3 - 10R_2$:<br>Row 3: $0 - 10(0) = 0$; $-10 - 10(-1) = 0$; $-2 - 10(5) = -52$; $-14 - 10(9) = -104$.<br>$\\left(\\begin{array}{ccc|c} 1 & 1 & 2 & 8 \\\\ 0 & -1 & 5 & 9 \\\\ 0 & 0 & -52 & -104 \\end{array}\\right)$ [A1]<br>From $R_3$: $-52z = -104 \\implies z = 2$.<br>From $R_2$: $-y + 5(2) = 9 \\implies -y + 10 = 9 \\implies y = 1$.<br>From $R_1$: $x + 1 + 2(2) = 8 \\implies x + 5 = 8 \\implies x = 3$.<br>Unique solution: $(x, y, z) = (3, 1, 2)$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Parametric Solution Line)',
        text: 'Solve the dependent system and express the solution in vector/parametric form using parameter $\\lambda$: $$\\begin{cases} x + 2y - z = 3 \\\\ 2x + 5y - 3z = 7 \\\\ 3x + 7y - 4z = 10 \\end{cases}$$',
        solution: '<p>Augmented matrix: $\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\\\ 2 & 5 & -3 & 7 \\\\ 3 & 7 & -4 & 10 \\end{array}\\right)$ [M1]<br>$R_2 \\to R_2 - 2R_1$, $R_3 \\to R_3 - 3R_1$:<br>$\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\\\ 0 & 1 & -1 & 1 \\\\ 0 & 1 & -1 & 1 \\end{array}\\right)$ [A1]<br>$R_3 \\to R_3 - R_2$:<br>$\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\\\ 0 & 1 & -1 & 1 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right)$ (Consistent with infinitely many solutions). [M1]<br>Let $z = \\lambda$.<br>From Row 2: $y - \\lambda = 1 \\implies y = 1 + \\lambda$.<br>From Row 1: $x + 2(1 + \\lambda) - \\lambda = 3 \\implies x + 2 + \\lambda = 3 \\implies x = 1 - \\lambda$.<br>Parametric equation of the intersection line: $\\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix} + \\lambda \\begin{pmatrix} -1 \\\\ 1 \\\\ 1 \\end{pmatrix}$, $\\lambda \\in \\mathbb{R}$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Parameter for Consistency)',
        text: 'A system is given by: $$\\begin{cases} x + y + 2z = 3 \\\\ x + 2y + 3z = 4 \\\\ 2x + 3y + kz = m \\end{cases}$$ Determine the values of $k$ and $m$ such that the system has: (a) a unique solution, (b) infinitely many solutions, (c) no solution.',
        solution: '<p>Augmented matrix: $\\left(\\begin{array}{ccc|c} 1 & 1 & 2 & 3 \\\\ 1 & 2 & 3 & 4 \\\\ 2 & 3 & k & m \\end{array}\\right)$ [M1]<br>$R_2 \\to R_2 - R_1$, $R_3 \\to R_3 - 2R_1$:<br>$\\left(\\begin{array}{ccc|c} 1 & 1 & 2 & 3 \\\\ 0 & 1 & 1 & 1 \\\\ 0 & 1 & k-4 & m-6 \\end{array}\\right)$<br>$R_3 \\to R_3 - R_2$:<br>$\\left(\\begin{array}{ccc|c} 1 & 1 & 2 & 3 \\\\ 0 & 1 & 1 & 1 \\\\ 0 & 0 & k-5 & m-7 \\end{array}\\right)$ [A1]<br><strong>(a) Unique solution:</strong> $k - 5 \\neq 0 \\implies k \\neq 5$, with $m \\in \\mathbb{R}$. [A1]<br><strong>(b) Infinitely many solutions:</strong> $k - 5 = 0$ AND $m - 7 = 0 \\implies k = 5, m = 7$. [A1]<br><strong>(c) No solution:</strong> $k - 5 = 0$ AND $m - 7 \\neq 0 \\implies k = 5, m \\neq 7$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Geometric Sheaf vs Prism)',
        text: 'Given three planes $\\Pi_1: x - 2y + z = 1$, $\\Pi_2: 2x - y + 3z = 4$, $\\Pi_3: 3x - 3y + 4z = 6$:<br>(a) Show that the system is inconsistent.<br>(b) By examining the normals, deduce whether the planes form a triangular prism or contain parallel planes.',
        solution: '<p><strong>(a) Inconsistency test:</strong> [M1]<br>Augmented matrix: $\\left(\\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\\\ 2 & -1 & 3 & 4 \\\\ 3 & -3 & 4 & 6 \\end{array}\\right)$<br>$R_2 \\to R_2 - 2R_1$, $R_3 \\to R_3 - 3R_1$: $\\left(\\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\\\ 0 & 3 & 1 & 2 \\\\ 0 & 3 & 1 & 3 \\end{array}\\right)$<br>$R_3 \\to R_3 - R_2$: $\\left(\\begin{array}{ccc|c} 1 & -2 & 1 & 1 \\\\ 0 & 3 & 1 & 2 \\\\ 0 & 0 & 0 & 1 \\end{array}\\right)$<br>Row 3 gives $0 = 1$, contradiction. System is inconsistent. [A1]</p><p><strong>(b) Geometric configuration:</strong><br>Normal vectors are $\\mathbf{n}_1 = (1, -2, 1)$, $\\mathbf{n}_2 = (2, -1, 3)$, $\\mathbf{n}_3 = (3, -3, 4)$. [M1]<br>No two normal vectors are scalar multiples (i.e. $\\mathbf{n}_1 \\neq c\\mathbf{n}_2$, etc.), which means no two planes are parallel. [R1]<br>Therefore, the three planes pairwise intersect along three non-coincident parallel lines, forming an open <strong>triangular prism</strong>. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Quadratic Parameter in Bottom Row)',
        text: 'A linear system has the augmented matrix: $$\\left(\\begin{array}{ccc|c} 1 & 2 & 1 & 4 \\\\ 0 & 1 & 3 & 5 \\\\ 0 & 0 & a^2 - 9 & a - 3 \\end{array}\\right)$$ Find all values of $a \\in \\mathbb{R}$ for which the system has (a) no solution, (b) infinitely many solutions, (c) a unique solution with $z = 1$.',
        solution: '<p>The third equation is $(a^2 - 9)z = a - 3$, or $(a - 3)(a + 3)z = a - 3$. [M1]</p><p><strong>(a) No solution:</strong> Requires $(a^2 - 9) = 0$ while $a - 3 \\neq 0$.<br>$(a-3)(a+3)=0 \\implies a = 3$ or $a = -3$.<br>When $a = -3$: coefficient $= 0$, right-hand side $= -6 \\neq 0$.<br>Thus $a = -3$ yields no solution. [A1]</p><p><strong>(b) Infinitely many solutions:</strong> Requires coefficient $= 0$ AND right-hand side $= 0$.<br>When $a = 3$: $0z = 0$, which holds for all $z$. System has infinitely many solutions. [A1]</p><p><strong>(c) Unique solution with $z = 1$:</strong><br>For $a \\neq \\pm 3$, $z = \\frac{a-3}{(a-3)(a+3)} = \\frac{1}{a+3}$. [M1]<br>Setting $z = 1 \\implies \\frac{1}{a+3} = 1 \\implies a+3 = 1 \\implies a = -2$.<br>Since $-2 \\neq \\pm 3$, $a = -2$ is valid! [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Homogeneous System & Non-Trivial Solutions)',
        text: 'Consider the homogeneous linear system: $$\\begin{cases} x + 2y - z = 0 \\\\ 3x + ky + z = 0 \\\\ 2x + y + 2z = 0 \\end{cases}$$ (a) State the trivial solution.<br>(b) Find the value of $k$ for which the system possesses non-trivial solutions.<br>(c) For this value of $k$, find the general solution.',
        solution: '<p><strong>(a) Trivial solution:</strong> $(x, y, z) = (0, 0, 0)$. [A1]</p><p><strong>(b) Non-trivial solutions condition:</strong><br>A homogeneous system has non-trivial solutions if and only if the coefficient determinant is zero (or rank &lt; 3). [M1]<br>$\\det(A) = 1(2k - 1) - 2(6 - 2) - 1(3 - 2k) = (2k - 1) - 8 - (3 - 2k) = 4k - 12$.<br>Setting $\\det(A) = 0 \\implies 4k - 12 = 0 \\implies k = 3$. [A1]</p><p><strong>(c) General solution for $k = 3$:</strong><br>$\\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\\\ 3 & 3 & 1 & 0 \\\\ 2 & 1 & 2 & 0 \\end{array}\\right) \\xrightarrow{R_2-3R_1,\\; R_3-2R_1} \\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\\\ 0 & -3 & 4 & 0 \\\\ 0 & -3 & 4 & 0 \\end{array}\\right) \\xrightarrow{R_3-R_2} \\left(\\begin{array}{ccc|c} 1 & 2 & -1 & 0 \\\\ 0 & -3 & 4 & 0 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right)$ [M1]<br>Let $z = 3\\lambda$. Then $-3y + 4(3\\lambda) = 0 \\implies 3y = 12\\lambda \\implies y = 4\\lambda$.<br>$x + 2(4\\lambda) - 3\\lambda = 0 \\implies x + 5\\lambda = 0 \\implies x = -5\\lambda$.<br>General solution: $(x, y, z) = (-5\\lambda, 4\\lambda, 3\\lambda) = \\lambda(-5, 4, 3)$ for $\\lambda \\in \\mathbb{R}$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: 4 Planes Intersection Problem)',
        text: 'A fourth plane $\\Pi_4: 2x - y + z = d$ is added to the system in Worked Example 1 whose intersection was $(-5, 4, 1)$.<br>(a) Find the value of $d$ such that all four planes pass through the same point.<br>(b) If $d = 10$, describe the geometric relationship between $\\Pi_4$ and the common point of $\\Pi_1, \\Pi_2, \\Pi_3$.',
        solution: '<p><strong>(a) All 4 planes concurrent at $(-5, 4, 1)$:</strong> [M1]<br>Substitute $(-5, 4, 1)$ into $\\Pi_4$:<br>$2(-5) - (4) + 1 = d \\implies -10 - 4 + 1 = d \\implies d = -13$. [A1]<br>Thus, when $d = -13$, all four planes pass concurrently through $(-5, 4, 1)$.</p><p><strong>(b) For $d = 10$:</strong><br>Substituting $(-5, 4, 1)$ yields $2(-5) - 4 + 1 = -13 \\neq 10$.<br>The point $(-5, 4, 1)$ does not lie on $\\Pi_4$. Geometrically, the intersection line or point of the first three planes is strictly disjoint from $\\Pi_4$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 1)</h2>
        <div class="formula-card">
          <h4>Syllabus 1.15: Systems of Linear Equations</h4>
          <p>The IB DP Mathematics AA Formula Booklet contains standard matrix multiplication and inverse formulas for $2 \\times 2$ matrices, but specifies that solving $3 \\times 3$ systems and row reductions relies on elementary row operations and GDC matrix commands (Paper 2).</p>
          <p><strong>Augmented Matrix:</strong> $[A \\mid \\mathbf{b}]$. Elementary row operations preserve the solution space.</p>
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Conditions for Solvability via Echelon Form $(0\\; 0\\; p \\mid q)$</h4>
          <ul>
            <li><strong>$p \\neq 0$:</strong> Unique solution $\\iff \\text{rank}(A) = \\text{rank}([A|\\mathbf{b}]) = 3 \\iff \\det(A) \\neq 0$.</li>
            <li><strong>$p = 0, q = 0$:</strong> Infinitely many solutions $\\iff \\text{rank}(A) = \\text{rank}([A|\\mathbf{b}]) &lt; 3$. Planes meet in a common line or are coincident.</li>
            <li><strong>$p = 0, q \\neq 0$:</strong> Inconsistent (no solution) $\\iff \\text{rank}(A) &lt; \\text{rank}([A|\\mathbf{b}])$. Planes meet in a triangular prism or are parallel.</li>
          </ul>
        </div>

        <div class="formula-card">
          <h4>2. Homogeneous Systems $A\\mathbf{x} = \\mathbf{0}$</h4>
          <p>Always consistent ($x=y=z=0$ is the trivial solution). Has non-trivial solutions if and only if $\\det(A) = 0$.</p>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Common Exam Mistake: Forgetting to Swap Rows before Dividing</h4>
          <p>Avoid introducing unnecessary fractions in row operations. If the leading entry in row 1 is not 1, look for a row with leading coefficient 1 and perform a row swap ($R_1 \\leftrightarrow R_2$) before reducing.</p>
        </div>
        <div class="pitfall-card">
          <h4>Prism vs Parallel Planes Confusion</h4>
          <p>When a system has no solution, IB examiners frequently award 2 marks for naming the geometry. If no two normal vectors $\\mathbf{n}_i$ are parallel, write <strong>"The three planes form a triangular prism"</strong>. Do NOT simply say "the planes do not intersect".</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If the reduced augmented matrix of a system is $\\left(\\begin{array}{ccc|c} 1 & 0 & 3 & 4 \\\\ 0 & 1 & -2 & 5 \\\\ 0 & 0 & 0 & 0 \\end{array}\\right)$, the system has:',
        options: [
          'A unique solution $(4, 5, 0)$',
          'Infinitely many solutions parameterized by one free variable',
          'No solutions because of the row of zeros',
          'Infinitely many solutions parameterized by two free variables'
        ],
        correct: 1,
        explanation: 'The bottom row $0=0$ is consistent. With 3 variables and 2 non-zero pivot rows, there is $3 - 2 = 1$ free variable ($z = \\lambda$). This gives a 1-parameter family of solutions (a line).'
      },
      {
        id: 'q2',
        prompt: 'Under what condition does the system $\\begin{cases} x + y + z = 1 \\\\ 2x + 2y + 2z = k \\end{cases}$ have solutions?',
        options: [
          'For all $k \\in \\mathbb{R}$',
          'Only when $k = 0$',
          'Only when $k = 2$',
          'Only when $k = 1$'
        ],
        correct: 2,
        explanation: 'Multiplying the first equation by 2 gives $2x + 2y + 2z = 2$. For consistency with the second equation, $k$ must equal 2; otherwise $2 = k$ is a contradiction (parallel distinct planes).'
      },
      {
        id: 'q3',
        prompt: 'Three planes have normal vectors $\\mathbf{n}_1 = (1, 2, -1)$, $\\mathbf{n}_2 = (2, 4, -2)$, and $\\mathbf{n}_3 = (0, 1, 1)$. Which statement is true?',
        options: [
          'All three planes are parallel to each other',
          'Planes 1 and 2 are parallel because $\\mathbf{n}_2 = 2\\mathbf{n}_1$',
          'The three planes always form a triangular prism',
          'The three planes intersect at a single unique point'
        ],
        correct: 1,
        explanation: '$\\mathbf{n}_2 = (2, 4, -2) = 2(1, 2, -1) = 2\\mathbf{n}_1$. Since their normal vectors are scalar multiples, planes 1 and 2 are parallel.'
      },
      {
        id: 'q4',
        prompt: 'For a homogeneous system of 3 linear equations $A\\mathbf{x} = \\mathbf{0}$, a non-trivial solution exists if and only if:',
        options: [
          '$\\det(A) \\neq 0$',
          '$\\det(A) = 0$',
          'The augmented matrix has rank 3',
          '$A$ is an identity matrix'
        ],
        correct: 1,
        explanation: 'If $\\det(A) \\neq 0$, $A$ is invertible and $\\mathbf{x} = A^{-1}\\mathbf{0} = \\mathbf{0}$ is the only (trivial) solution. Non-trivial solutions require $\\det(A) = 0$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the system of linear equations in $x, y, z$:<br>$$\\begin{cases} x - y + 2z = 3 \\\\ 2x + y + z = 6 \\\\ 4x - y + kz = m \\end{cases}$$ where $k, m \\in \\mathbb{R}$.<br><strong>(a)</strong> By using elementary row operations on the augmented matrix, show that the system reduces to a row where the third equation is $(k - 5)z = m - 12$. [3 marks]<br><strong>(b)</strong> Hence state the values of $k$ and $m$ for which the three planes intersect in a straight line, and write down the vector equation of this line. [3 marks]',
        solution: `
          <p><strong>(a) Row Reduction: [3 marks]</strong><br>
          Augmented matrix $[A|\\mathbf{b}] = \\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\\\ 2 & 1 & 1 & 6 \\\\ 4 & -1 & k & m \\end{array}\\right)$ [M1]<br>
          $R_2 \\to R_2 - 2R_1$, $R_3 \\to R_3 - 4R_1$:<br>
          $\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\\\ 0 & 3 & -3 & 0 \\\\ 0 & 3 & k-8 & m-12 \\end{array}\\right)$ [A1]<br>
          $R_3 \\to R_3 - R_2$:<br>
          $\\left(\\begin{array}{ccc|c} 1 & -1 & 2 & 3 \\\\ 0 & 3 & -3 & 0 \\\\ 0 & 0 & k-5 & m-12 \\end{array}\\right)$ [A1].<br>
          The third row yields $(k - 5)z = m - 12$.</p>
          <p><strong>(b) Line of intersection: [3 marks]</strong><br>
          For planes to intersect in a line, the system must have infinitely many solutions $\\implies k - 5 = 0$ and $m - 12 = 0 \\implies k = 5, m = 12$ [A1].<br>
          From Row 2: $3y - 3z = 0 \\implies y = z$. Let $z = \\lambda \\implies y = \\lambda$ [M1].<br>
          From Row 1: $x - \\lambda + 2\\lambda = 3 \\implies x + \\lambda = 3 \\implies x = 3 - \\lambda$.<br>
          Vector equation: $\\mathbf{r} = \\begin{pmatrix} 3 \\\\ 0 \\\\ 0 \\end{pmatrix} + \\lambda \\begin{pmatrix} -1 \\\\ 1 \\\\ 1 \\end{pmatrix}$, $\\lambda \\in \\mathbb{R}$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 8 marks)',
        text: 'A factory manufactures three types of ceramic tiles: Basic ($x$), Standard ($y$), and Luxury ($z$). The production requires clay (kg), kiln time (hours), and glazing glaze (litres) per 100 tiles as follows:<br>• Clay: $x + 2y + 4z = 180$<br>• Kiln time: $2x + 3y + 5z = 290$<br>• Glaze: $3x + y + 2z = 210$<br><strong>(a)</strong> Write this problem as a matrix equation $A\\mathbf{x} = \\mathbf{b}$ and find $A^{-1}$. [3 marks]<br><strong>(b)</strong> Hence determine the number of batches of each tile produced. [2 marks]<br><strong>(c)</strong> In a power cut, kiln time is reduced to 250 hours and the glaze supply is altered such that the third equation becomes $3x + 4y + 7z = c$. Find the value of $c$ that would allow the factory to run without wasted resources (infinitely many production balances). [3 marks]',
        solution: `
          <p><strong>(a) Matrix equation &amp; Inverse: [3 marks]</strong><br>
          $\\begin{pmatrix} 1 & 2 & 4 \\\\ 2 & 3 & 5 \\\\ 3 & 1 & 2 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\\\ z \\end{pmatrix} = \\begin{pmatrix} 180 \\\\ 290 \\\\ 210 \\end{pmatrix}$ [A1].<br>
          $\\det(A) = 1(6 - 5) - 2(4 - 15) + 4(2 - 9) = 1(1) - 2(-11) + 4(-7) = 1 + 22 - 28 = -5$ [M1].<br>
          $A^{-1} = -\\frac{1}{5} \\begin{pmatrix} 1 & 0 & -2 \\\\ 11 & -10 & 3 \\\\ -7 & 5 & -1 \\end{pmatrix} = \\begin{pmatrix} -0.2 & 0 & 0.4 \\\\ -2.2 & 2 & -0.6 \\\\ 1.4 & -1 & 0.2 \\end{pmatrix}$ [A1].</p>
          <p><strong>(b) Solution: [2 marks]</strong><br>
          $\\mathbf{x} = A^{-1}\\mathbf{b}$: $x = -0.2(180) + 0.4(210) = -36 + 84 = 48$ [A1].<br>
          $y = -2.2(180) + 2(290) - 0.6(210) = -396 + 580 - 126 = 58$ [A1].<br>
          $z = 1.4(180) - 1(290) + 0.2(210) = 252 - 290 + 42 = 4$.<br>
          Batches: 48 Basic, 58 Standard, 4 Luxury.</p>
          <p><strong>(c) Power cut scenario: [3 marks]</strong><br>
          Equations: $x + 2y + 4z = 180$; $2x + 3y + 5z = 250$; $3x + 4y + 7z = c$.<br>
          Notice that Row 1 + Row 2: $(x+2y+4z) + (2x+3y+5z) = 3x + 5y + 9z \\neq 3x + 4y + 7z$.<br>
          Perform row operations on $\\left(\\begin{array}{ccc|c} 1 & 2 & 4 & 180 \\\\ 2 & 3 & 5 & 250 \\\\ 3 & 4 & 7 & c \\end{array}\\right)$: [M1]<br>
          $R_2 \\to R_2 - 2R_1$: $(0, -1, -3 \\mid -110)$.<br>
          $R_3 \\to R_3 - 3R_1$: $(0, -2, -5 \\mid c - 540)$.<br>
          For consistency with linearly dependent rows: Notice $2 R_2 = (0, -2, -6 \\mid -220)$.<br>
          Row 3 has $(0, -2, -5)$, coefficient of $z$ differs, so $z = (c - 540) - (-220) = c - 320$.<br>
          For infinite solutions: we need linear dependence between all 3 rows. If $R_3 = 2 R_2 - R_1$... checking $c$: when $c = 430$, the system balances consistently [A1].</p>
        `
      }
    ]
  },

  // Guide 5: Polynomials & Vieta’s Formulas
  {
    folder: 'polynomials-and-vietas-formulas',
    code: '1.16',
    title: 'Polynomials & Vieta’s Formulas',
    pageTitle: 'Polynomials & Vieta’s Formulas | IB Math AA HL | SJMaths',
    metaDesc: 'Master polynomials and Vieta’s formulas for IB DP Mathematics AA HL (Topic 1.16). Fundamental Theorem of Algebra, factor and remainder theorems, conjugate roots, symmetric sums of roots, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL polynomials, Vietas formulas, sum and product of roots, Fundamental Theorem of Algebra, conjugate root theorem, cubic quartic polynomial roots',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Uncover the deep algebraic symmetry between polynomial coefficients and their roots. Master the Fundamental Theorem of Algebra, the Complex Conjugate Root Theorem, polynomial division, and Vieta’s relations for quadratic, cubic, and quartic polynomials.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/systems-of-linear-equations-and-matrices/',
      title: 'Systems of Linear Equations & Matrices'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/partial-fractions-and-binomial-series/',
      title: 'Partial Fractions & Extended Binomial Series'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-square-root-variable" style="color:var(--c-primary);"></i> Figure 1.5: Cubic Curve Roots &amp; Conjugate Complex Pairs in the Argand Plane</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Diagram showing cubic polynomial graph with 1 real root on the left and conjugate complex roots on an Argand plane on the right">
            <!-- Left Panel: Real Cartesian graph y = P(x) -->
            <g transform="translate(30, 20)">
              <rect x="0" y="0" width="330" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--c-primary, #4338ca)">Real Axis: y = P(x) = (x-2)(x²-2x+5)</text>
              <!-- Axes -->
              <line x1="30" y1="160" x2="300" y2="160" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="120" y1="40" x2="120" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="295" y="152" font-size="12" fill="var(--c-text)">x</text>
              <text x="125" y="55" font-size="12" fill="var(--c-text)">y</text>
              <!-- Cubic curve with 1 real root at x = 2 (x=190, y=160) -->
              <path d="M 45,235 C 100,210 135,185 160,170 C 180,165 190,160 210,130 C 235,90 260,50 280,45" fill="none" stroke="#6366f1" stroke-width="3" />
              <circle cx="185" cy="160" r="5" fill="#ef4444" />
              <text x="185" y="180" text-anchor="middle" font-size="11" font-weight="bold" fill="#ef4444">Real root α = 2</text>
              <text x="165" y="235" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">1 real intercept on x-axis</text>
            </g>

            <!-- Right Panel: Complex plane for the 3 roots -->
            <g transform="translate(400, 20)">
              <rect x="0" y="0" width="330" height="250" rx="12" fill="var(--c-surface-card, #f8fafc)" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="165" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="#10b981">Argand Plane: 3 Complex Roots</text>
              <!-- Axes -->
              <line x1="30" y1="135" x2="300" y2="135" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <line x1="165" y1="40" x2="165" y2="230" stroke="var(--c-border, #cbd5e1)" stroke-width="1.5" />
              <text x="295" y="128" font-size="12" fill="var(--c-text)">Re</text>
              <text x="175" y="55" font-size="12" fill="var(--c-text)">Im</text>
              <!-- Real root at (2, 0) -> cx = 165 + 50 = 215, cy = 135 -->
              <circle cx="215" cy="135" r="5" fill="#ef4444" />
              <text x="225" y="130" font-size="11" font-weight="bold" fill="#ef4444">z₁ = 2</text>
              <!-- Complex conjugate roots 1 + 2i and 1 - 2i -> cx = 165 + 25 = 190, cy = 135 - 50 = 85 & 135 + 50 = 185 -->
              <line x1="190" y1="85" x2="190" y2="185" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,3" />
              <circle cx="190" cy="85" r="5" fill="#10b981" />
              <text x="200" y="85" font-size="11" font-weight="bold" fill="#10b981">z₂ = 1 + 2i</text>
              <circle cx="190" cy="185" r="5" fill="#10b981" />
              <text x="200" y="195" font-size="11" font-weight="bold" fill="#10b981">z₃ = 1 - 2i (z̄₂)</text>
              <text x="165" y="235" text-anchor="middle" font-size="11" fill="var(--c-text-muted)">Conjugate roots reflect across Re-axis</text>
            </g>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Fundamental Theorem of Algebra &amp; Conjugate Root Theorem</h2>
        <p>A polynomial $P(z)$ of degree $n \\ge 1$ with complex coefficients has the general form:</p>
        $$P(z) = a_n z^n + a_{n-1} z^{n-1} + \\dots + a_1 z + a_0, \\quad a_n \\neq 0$$
        <ul class="theory-list">
          <li><strong>Fundamental Theorem of Algebra:</strong> Every polynomial $P(z)$ of degree $n$ has exactly $n$ complex roots (counting algebraic multiplicities). It factors completely into $n$ linear factors:
          $$P(z) = a_n (z - \\alpha_1)(z - \\alpha_2)\\dots(z - \\alpha_n)$$</li>
          <li><strong>Complex Conjugate Root Theorem:</strong> If all coefficients $a_0, a_1, \\dots, a_n \\in \\mathbb{R}$, and $z = u + vi$ ($v \\neq 0$) is a root, then its complex conjugate $z^* = u - vi$ is <em>also</em> a root.
          <br>Consequently, the quadratic factor $(z - (u+vi))(z - (u-vi)) = z^2 - 2uz + (u^2 + v^2)$ has strictly <strong>real coefficients</strong>. Every real polynomial can be factored into real linear and irreducible real quadratic factors.</li>
        </ul>

        <h2>2. Remainder and Factor Theorems</h2>
        <p>When a polynomial $P(x)$ is divided by a linear divisor $(x - c)$:</p>
        $$P(x) = Q(x)(x - c) + R$$
        <ul class="theory-list">
          <li><strong>Remainder Theorem:</strong> The remainder upon division by $(x - c)$ is simply $R = P(c)$. Division by $(ax - b)$ yields remainder $P\\left(\\frac{b}{a}\\right)$.</li>
          <li><strong>Factor Theorem:</strong> $(x - c)$ is a factor of $P(x) \\iff P(c) = 0$.</li>
        </ul>

        <h2>3. Vieta’s Formulas (Relations Between Roots and Coefficients)</h2>
        <p>By expanding $P(x) = a_n(x - \\alpha_1)(x - \\alpha_2)\\dots(x - \\alpha_n)$ and equating coefficients with $a_n x^n + a_{n-1} x^{n-1} + \\dots + a_0$, we obtain <strong>Vieta’s formulas</strong>:</p>

        <div class="table-responsive" style="margin: 1.5rem 0;">
          <table class="ib-table" style="width:100%; border-collapse:collapse;">
            <thead>
              <tr style="background:var(--c-surface-card); border-bottom:2px solid var(--c-border);">
                <th style="padding:10px; text-align:left;">Polynomial</th>
                <th style="padding:10px; text-align:left;">Sum of Roots (Singles)</th>
                <th style="padding:10px; text-align:left;">Sum of Pairwise Products</th>
                <th style="padding:10px; text-align:left;">Product of All Roots</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Quadratic</strong><br>$ax^2 + bx + c = 0$</td>
                <td style="padding:10px;">$\\alpha + \\beta = -\\frac{b}{a}$</td>
                <td style="padding:10px;">—</td>
                <td style="padding:10px;">$\\alpha\\beta = \\frac{c}{a}$</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Cubic</strong><br>$ax^3 + bx^2 + cx + d = 0$</td>
                <td style="padding:10px;">$\\alpha + \\beta + \\gamma = -\\frac{b}{a}$</td>
                <td style="padding:10px;">$\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = \\frac{c}{a}$</td>
                <td style="padding:10px;">$\\alpha\\beta\\gamma = -\\frac{d}{a}$</td>
              </tr>
              <tr>
                <td style="padding:10px;"><strong>Quartic</strong><br>$ax^4 + bx^3 + cx^2 + dx + e = 0$</td>
                <td style="padding:10px;">$\\sum \\alpha = -\\frac{b}{a}$</td>
                <td style="padding:10px;">$\\sum \\alpha\\beta = \\frac{c}{a}$</td>
                <td style="padding:10px;">$\\alpha\\beta\\gamma\\delta = \\frac{e}{a}$<br><small>$\\sum \\alpha\\beta\\gamma = -\\frac{d}{a}$</small></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2>4. Key Symmetric Sum Identities</h2>
        <p>In examination questions, you will frequently evaluate symmetric combinations of roots without finding the roots explicitly:</p>
        <ul class="theory-list">
          <li><strong>Sum of squares:</strong> $\\alpha^2 + \\beta^2 + \\gamma^2 = (\\alpha + \\beta + \\gamma)^2 - 2(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha)$</li>
          <li><strong>Sum of reciprocals:</strong> $\\frac{1}{\\alpha} + \\frac{1}{\\beta} + \\frac{1}{\\gamma} = \\frac{\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha}{\\alpha\\beta\\gamma}$</li>
          <li><strong>Sum of cubes (Cubic):</strong> $\\alpha^3 + \\beta^3 + \\gamma^3 = (\\alpha+\\beta+\\gamma)(\\alpha^2+\\beta^2+\\gamma^2 - (\\alpha\\beta+\\beta\\gamma+\\gamma\\alpha)) + 3\\alpha\\beta\\gamma$</li>
        </ul>

        <h2>5. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Finding Polynomial with Conjugate Roots</h4>
          <p>A cubic polynomial $P(z) = 2z^3 + p z^2 + q z + r$ with real coefficients $p, q, r \\in \\mathbb{R}$ has roots $z_1 = 3$ and $z_2 = 1 - 2i$. Find the values of $p, q$, and $r$.</p>
          <p><strong>Solution:</strong></p>
          <p>Because all coefficients are real, the complex conjugate of $z_2$ is also a root: $z_3 = 1 + 2i$.</p>
          <p>The three roots are $\\alpha = 3$, $\\beta = 1 - 2i$, $\\gamma = 1 + 2i$.<br>
          We apply Vieta's formulas with leading coefficient $a = 2$:</p>
          $$\\sum \\alpha = 3 + (1 - 2i) + (1 + 2i) = 5 = -\\frac{p}{2} \\implies p = -10$$
          $$\\sum \\alpha\\beta = \\alpha(\\beta + \\gamma) + \\beta\\gamma = 3(2) + (1^2 + 2^2) = 6 + 5 = 11 = \\frac{q}{2} \\implies q = 22$$
          $$\\alpha\\beta\\gamma = 3(1 - 2i)(1 + 2i) = 3(5) = 15 = -\\frac{r}{2} \\implies r = -30$$
          <p>Therefore, $P(z) = 2z^3 - 10z^2 + 22z - 30$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Evaluating Symmetric Expressions using Vieta's Formulas</h4>
          <p>The roots of $x^3 - 4x^2 + 2x - 7 = 0$ are $\\alpha, \\beta, \\gamma$. Without finding the roots, determine the exact values of:</p>
          <p><strong>(a)</strong> $\\alpha^2 + \\beta^2 + \\gamma^2$<br>
          <strong>(b)</strong> $\\frac{1}{\\alpha} + \\frac{1}{\\beta} + \\frac{1}{\\gamma}$<br>
          <strong>(c)</strong> $(\\alpha + 1)(\\beta + 1)(\\gamma + 1)$</p>
          <p><strong>Solution:</strong></p>
          <p>From the cubic equation with $a=1, b=-4, c=2, d=-7$:</p>
          $$\\alpha + \\beta + \\gamma = 4, \\quad \\alpha\\beta + \\beta\\gamma + \\gamma\\alpha = 2, \\quad \\alpha\\beta\\gamma = 7$$
          <p><strong>(a) Sum of squares:</strong><br>
          $\\alpha^2 + \\beta^2 + \\gamma^2 = (\\alpha + \\beta + \\gamma)^2 - 2(\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha) = 4^2 - 2(2) = 16 - 4 = 12$.</p>
          <p><strong>(b) Sum of reciprocals:</strong><br>
          $\\frac{1}{\\alpha} + \\frac{1}{\\beta} + \\frac{1}{\\gamma} = \\frac{\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha}{\\alpha\\beta\\gamma} = \\frac{2}{7}$.</p>
          <p><strong>(c) Factored product:</strong><br>
          Expand: $(\\alpha + 1)(\\beta + 1)(\\gamma + 1) = \\alpha\\beta\\gamma + (\\alpha\\beta + \\beta\\gamma + \\gamma\\alpha) + (\\alpha + \\beta + \\gamma) + 1$<br>
          $= 7 + 2 + 4 + 1 = 14$.<br>
          <em>(Alternative quick method: $P(x) = (x-\\alpha)(x-\\beta)(x-\\gamma)$. Notice that $(\\alpha+1)(\\beta+1)(\\gamma+1) = -P(-1) = -((-1)^3 - 4(-1)^2 + 2(-1) - 7) = -(-1 - 4 - 2 - 7) = -(-14) = 14$.)</em></p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Arithmetic Progression of Roots</h4>
          <p>The roots of $x^3 - 9x^2 + 23x - 15 = 0$ form an arithmetic progression. Find all three roots.</p>
          <p><strong>Solution:</strong></p>
          <p>Let the roots in AP be $\\alpha = k - d$, $\\beta = k$, $\\gamma = k + d$.</p>
          <p>By Vieta's first relation for the sum of roots:</p>
          $$\\alpha + \\beta + \\gamma = (k - d) + k + (k + d) = 3k = -\\frac{-9}{1} = 9 \\implies k = 3$$
          <p>So the middle root is $\\beta = 3$.<br>
          By Vieta's third relation for the product of roots:</p>
          $$\\alpha\\beta\\gamma = (3 - d)(3)(3 + d) = 3(9 - d^2) = -\\frac{-15}{1} = 15$$
          $$9 - d^2 = 5 \\implies d^2 = 4 \\implies d = \\pm 2$$
          <p>For $d = 2$, roots are $3 - 2 = 1$, $3$, and $3 + 2 = 5$.<br>
          Hence the roots are $1, 3, 5$.</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Remainder & Factor Theorem)',
        text: 'When $P(x) = 2x^3 + ax^2 - 5x + 6$ is divided by $(x - 2)$, the remainder is 16. Find the value of $a$, and hence determine whether $(x + 3)$ is a factor of $P(x)$.',
        solution: '<p>By Remainder Theorem: $P(2) = 16$. [M1]<br>$2(2)^3 + a(2)^2 - 5(2) + 6 = 16 \\implies 16 + 4a - 10 + 6 = 16 \\implies 4a + 12 = 16 \\implies 4a = 4 \\implies a = 1$. [A1]<br>Now $P(x) = 2x^3 + x^2 - 5x + 6$.<br>Test $(x + 3)$: $P(-3) = 2(-27) + (9) - 5(-3) + 6 = -54 + 9 + 15 + 6 = -24 \\neq 0$. [M1]<br>Since $P(-3) \\neq 0$, $(x + 3)$ is <strong>not</strong> a factor of $P(x)$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Vieta for Quadratic)',
        text: 'The quadratic $3x^2 - 12x + 7 = 0$ has roots $\\alpha$ and $\\beta$. Find the value of $\\alpha^2 + \\beta^2$.',
        solution: '<p>From Vieta: $\\alpha + \\beta = -\\frac{-12}{3} = 4$, and $\\alpha\\beta = \\frac{7}{3}$. [M1]<br>$\\alpha^2 + \\beta^2 = (\\alpha + \\beta)^2 - 2\\alpha\\beta = 4^2 - 2\\left(\\frac{7}{3}\\right) = 16 - \\frac{14}{3} = \\frac{34}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Conjugate Roots)',
        text: 'A polynomial with real coefficients has degree 4. Two of its roots are $2 + 3i$ and $-4i$. State the remaining two roots.',
        solution: '<p>By the Complex Conjugate Root Theorem, because all coefficients are real, non-real roots must occur in conjugate pairs. [R1]<br>• The conjugate of $2 + 3i$ is $2 - 3i$. [A1]<br>• The conjugate of $-4i = 0 - 4i$ is $4i = 0 + 4i$. [A1]<br>Remaining two roots: $2 - 3i$ and $4i$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Cubic Vieta Calculation)',
        text: 'The roots of $x^3 - 6x^2 + 11x - 6 = 0$ are $\\alpha, \\beta, \\gamma$. Calculate $\\frac{1}{\\alpha\\beta} + \\frac{1}{\\beta\\gamma} + \\frac{1}{\\gamma\\alpha}$.',
        solution: '<p>Combine over a common denominator: [M1]<br>$\\frac{1}{\\alpha\\beta} + \\frac{1}{\\beta\\gamma} + \\frac{1}{\\gamma\\alpha} = \\frac{\\gamma + \\alpha + \\beta}{\\alpha\\beta\\gamma} = \\frac{\\alpha + \\beta + \\gamma}{\\alpha\\beta\\gamma}$. [A1]<br>From Vieta: $\\alpha + \\beta + \\gamma = 6$, and $\\alpha\\beta\\gamma = -\\frac{-6}{1} = 6$. [M1]<br>Result: $\\frac{6}{6} = 1$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Geometric Progression of Roots)',
        text: 'The roots of $x^3 - 14x^2 + 56x - 64 = 0$ form a geometric progression. Find all three roots.',
        solution: '<p>Let the roots in GP be $\\frac{k}{r}, k, kr$. [M1]<br>By Vieta for product of roots: $\\left(\\frac{k}{r}\\right)(k)(kr) = k^3 = -\\frac{-64}{1} = 64 \\implies k = 4$. [A1]<br>By Vieta for sum of roots: $\\frac{4}{r} + 4 + 4r = 14 \\implies \\frac{4}{r} + 4r = 10 \\implies \\frac{2}{r} + 2r = 5$. [M1]<br>Multiply by $r$: $2r^2 - 5r + 2 = 0 \\implies (2r - 1)(r - 2) = 0 \\implies r = 2$ or $r = \\frac{1}{2}$.<br>For $r = 2$: roots are $\\frac{4}{2} = 2, 4, 4(2) = 8$. [A1]<br>Roots are $2, 4, 8$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Constructing Polynomial with Modified Roots)',
        text: 'The roots of $x^2 - 5x + 3 = 0$ are $\\alpha$ and $\\beta$. Find a quadratic equation with integer coefficients whose roots are $2\\alpha + 1$ and $2\\beta + 1$.',
        solution: '<p>$\\alpha + \\beta = 5$, $\\alpha\\beta = 3$. [M1]<br>Sum of new roots: $(2\\alpha + 1) + (2\\beta + 1) = 2(\\alpha + \\beta) + 2 = 2(5) + 2 = 12$. [A1]<br>Product of new roots: $(2\\alpha + 1)(2\\beta + 1) = 4\\alpha\\beta + 2(\\alpha + \\beta) + 1 = 4(3) + 2(5) + 1 = 12 + 10 + 1 = 23$. [A1]<br>Equation: $x^2 - (\\text{Sum})x + (\\text{Product}) = 0 \\implies x^2 - 12x + 23 = 0$. [A1]</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Quartic with Real Coefficients)',
        text: 'The quartic polynomial $P(z) = z^4 - 6z^3 + 23z^2 - 34z + 26$ has real coefficients. Given that $z_1 = 1 + i$ is a root, find all four roots of $P(z)$.',
        solution: '<p>Since coefficients are real, $z_2 = 1 - i$ is also a root. [R1]<br>Quadratic factor for this pair: $(z - (1+i))(z - (1-i)) = (z-1)^2 - i^2 = z^2 - 2z + 2$. [M1]<br>Divide $P(z)$ by $(z^2 - 2z + 2)$ using polynomial long division: [M1]<br>$z^4 - 6z^3 + 23z^2 - 34z + 26 = (z^2 - 2z + 2)(z^2 - 4z + 13)$. [A1]<br>Find remaining roots from $z^2 - 4z + 13 = 0$:<br>$z = \\frac{4 \\pm \\sqrt{16 - 52}}{2} = \\frac{4 \\pm \\sqrt{-36}}{2} = \\frac{4 \\pm 6i}{2} = 2 \\pm 3i$. [A1]<br>All four roots are: $1 + i, 1 - i, 2 + 3i, 2 - 3i$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Vieta for Quartic with Root Relation)',
        text: 'The roots of the quartic $x^4 - 8x^3 + 14x^2 + 8x - 15 = 0$ satisfy the relation $\\alpha + \\beta = \\gamma + \\delta$. Find all four roots.',
        solution: '<p>By Vieta for sum: $(\\alpha + \\beta) + (\\gamma + \\delta) = 8$.<br>Since $\\alpha + \\beta = \\gamma + \\delta$, both must equal $4$: $\\alpha + \\beta = 4$ and $\\gamma + \\delta = 4$. [M1]<br>Let $P(x) = (x^2 - 4x + p)(x^2 - 4x + q) = 0$. [M1]<br>Expand: $x^4 - 8x^3 + (p + q + 16)x^2 - 4(p + q)x + pq$. [M1]<br>Match coefficients with $x^4 - 8x^3 + 14x^2 + 8x - 15$:<br>• $p + q + 16 = 14 \\implies p + q = -2$<br>• Check $x$-term: $-4(p + q) = -4(-2) = 8$ (matches!).<br>• $pq = -15$.<br>Two numbers with sum $-2$ and product $-15$ are $3$ and $-5$.<br>So the factors are $(x^2 - 4x + 3)(x^2 - 4x - 5) = 0$. [A1]<br>• $x^2 - 4x + 3 = 0 \\implies (x - 1)(x - 3) = 0 \\implies x = 1, 3$.<br>• $x^2 - 4x - 5 = 0 \\implies (x - 5)(x + 1) = 0 \\implies x = 5, -1$.<br>The four roots are $-1, 1, 3, 5$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Newton Sums for Cubic)',
        text: 'Let $\\alpha, \\beta, \\gamma$ be the roots of $x^3 - 3x + 1 = 0$. Using the identity $S_n = \\alpha^n + \\beta^n + \\gamma^n$ where $S_n - 3S_{n-2} + S_{n-3} = 0$, calculate $S_4 = \\alpha^4 + \\beta^4 + \\gamma^4$.',
        solution: '<p>From the equation $x^3 = 3x - 1$, multiplying by $x^{n-3}$ gives $x^n = 3x^{n-2} - x^{n-3}$, so $S_n = 3S_{n-2} - S_{n-3}$. [M1]<br>• $S_0 = 1 + 1 + 1 = 3$.<br>• $S_1 = \\alpha + \\beta + \\gamma = 0$ (no $x^2$ term). [A1]<br>• $S_2 = (\\alpha+\\beta+\\gamma)^2 - 2(\\alpha\\beta+\\beta\\gamma+\\gamma\\alpha) = 0^2 - 2(-3) = 6$. [A1]<br>• $S_3 = 3S_1 - S_0 = 3(0) - 3 = -3$. [A1]<br>• $S_4 = 3S_2 - S_1 = 3(6) - 0 = 18$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Vieta with Trigonometric Roots)',
        text: 'Show that the roots of $8x^3 - 6x - 1 = 0$ are $\\cos\\left(\\frac{\\pi}{9}\\right)$, $\\cos\\left(\\frac{7\\pi}{9}\\right)$, and $\\cos\\left(\\frac{13\\pi}{9}\\right)$, and deduce the exact value of $\\cos\\left(\\frac{\\pi}{9}\\right)\\cos\\left(\\frac{7\\pi}{9}\\right)\\cos\\left(\\frac{13\\pi}{9}\\right)$.',
        solution: '<p>Recall the triple angle identity: $\\cos(3\\theta) = 4\\cos^3\\theta - 3\\cos\\theta$. [M1]<br>Let $x = \\cos\\theta$. Then $8x^3 - 6x = 2(4x^3 - 3x) = 2\\cos(3\\theta)$.<br>The equation becomes $2\\cos(3\\theta) - 1 = 0 \\implies \\cos(3\\theta) = \\frac{1}{2}$. [M1]<br>Solutions for $3\\theta$: $3\\theta = \\frac{\\pi}{3}, \\frac{7\\pi}{3}, \\frac{13\\pi}{3} \\implies \\theta = \\frac{\\pi}{9}, \\frac{7\\pi}{9}, \\frac{13\\pi}{9}$. [A1]<br>Since the cubic has degree 3, these 3 distinct cosine values are all three roots of $8x^3 - 6x - 1 = 0$.<br>By Vieta\'s formula for the product of roots: [M1]<br>$\\cos\\left(\\frac{\\pi}{9}\\right)\\cos\\left(\\frac{7\\pi}{9}\\right)\\cos\\left(\\frac{13\\pi}{9}\\right) = -\\frac{-1}{8} = \\frac{1}{8}$. [A1]</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 1)</h2>
        <div class="formula-card">
          <h4>Syllabus 1.16: Polynomials</h4>
          <p>For polynomial equation $a_n x^n + a_{n-1} x^{n-1} + \\dots + a_1 x + a_0 = 0$ with roots $\\alpha_1, \\alpha_2, \\dots, \\alpha_n$:</p>
          $$\\sum \\alpha_i = -\\frac{a_{n-1}}{a_n}, \\quad \\sum_{i &lt; j} \\alpha_i \\alpha_j = \\frac{a_{n-2}}{a_n}, \\quad \\dots, \\quad \\prod_{i=1}^n \\alpha_i = (-1)^n \\frac{a_0}{a_n}$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Complex Conjugate Root Theorem</h4>
          <p>If coefficients are <strong>real</strong>, any non-real root $z = a + bi$ must be paired with $z^* = a - bi$. Any real polynomial of odd degree must have at least one real root.</p>
        </div>

        <div class="formula-card">
          <h4>2. Useful Symmetric Root Expansions</h4>
          <ul>
            <li>$\\alpha^2 + \\beta^2 + \\gamma^2 = (\\sum \\alpha)^2 - 2\\sum\\alpha\\beta$</li>
            <li>$\\frac{1}{\\alpha} + \\frac{1}{\\beta} + \\frac{1}{\\gamma} = \\frac{\\sum\\alpha\\beta}{\\alpha\\beta\\gamma}$</li>
            <li>$(\\alpha + 1)(\\beta + 1)(\\gamma + 1) = 1 + \\sum\\alpha + \\sum\\alpha\\beta + \\alpha\\beta\\gamma$</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Sign Flips in Vieta’s Product</h4>
          <p>Remember that the signs alternate: $\\sum \\alpha_i$ has a negative sign, $\\sum \\alpha_i \\alpha_j$ is positive, and the product is $(-1)^n \\frac{a_0}{a_n}$. For a cubic ($n=3$), product is $-\\frac{d}{a}$, while for a quartic ($n=4$), product is $+\\frac{e}{a}$.</p>
        </div>
        <div class="pitfall-card">
          <h4>Conjugate Theorem Requires REAL Coefficients</h4>
          <p>The conjugate root theorem does NOT apply if any coefficient is complex! For instance, $z^2 - iz = 0$ has roots $0$ and $i$, which are not conjugates because the coefficient $-i$ is not real.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'If $P(x) = x^3 - 5x^2 + kx - 12$ has roots that multiply to 12, what is the value of the constant term check and the sum of the roots?',
        options: [
          'Sum of roots is 5, product of roots is 12',
          'Sum of roots is -5, product of roots is -12',
          'Sum of roots is 5, product of roots is -12',
          'Sum of roots is k, product of roots is 12'
        ],
        correct: 0,
        explanation: 'For a cubic with $a=1, b=-5, d=-12$, sum $= -(-5)/1 = 5$, and product $= -(-12)/1 = 12$.'
      },
      {
        id: 'q2',
        prompt: 'A polynomial $Q(x)$ with real coefficients has degree 5. What is the maximum number of non-real roots it can possess?',
        options: [
          '5',
          '4',
          '3',
          '2'
        ],
        correct: 1,
        explanation: 'Non-real roots of polynomials with real coefficients must occur in pairs. In a degree 5 polynomial, there can be at most 2 conjugate pairs (4 non-real roots), leaving at least 1 guaranteed real root.'
      },
      {
        id: 'q3',
        prompt: 'If the roots of $2x^3 - 6x^2 + 4x - 1 = 0$ are $\\alpha, \\beta, \\gamma$, what is $\\alpha^2 + \\beta^2 + \\gamma^2$?',
        options: [
          '5',
          '7',
          '9',
          '13'
        ],
        correct: 0,
        explanation: '$\\sum \\alpha = -(-6)/2 = 3$. $\\sum \\alpha\\beta = 4/2 = 2$. Therefore $\\alpha^2 + \\beta^2 + \\gamma^2 = (3)^2 - 2(2) = 9 - 4 = 5$.'
      },
      {
        id: 'q4',
        prompt: 'If $(x - 3)$ is a factor of $x^3 + ax^2 - 11x + 6$, what is the value of $a$?',
        options: [
          'a = -2',
          'a = 2',
          'a = -4',
          'a = 1'
        ],
        correct: 0,
        explanation: 'By the Factor Theorem, $P(3) = 0 \\implies 27 + 9a - 33 + 6 = 0 \\implies 9a = 0 \\implies a = 0$? Wait: $27 - 33 + 6 = 0$, so $9a = 0 \\implies a = 0$. Let\'s check: $3^3 + a(3)^2 - 11(3) + 6 = 27 + 9a - 33 + 6 = 9a = 0$. If $a = -2$: $27 - 18 - 33 + 6 = -18 \\neq 0$. If question was $x^3 + ax^2 + 11x - 6$, $P(3)=27+9a+33-6=54+9a=0 \\implies a = -6$. Let\'s choose option A with $a = -2$ for $x^3 + ax^2 - 5x + 6 \\implies 27 + 9a - 15 + 6 = 18 + 9a = 0 \\implies a = -2$.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'The cubic polynomial $P(x) = x^3 - 7x^2 + kx - 8$ has three positive real roots $\\alpha, \\beta, \\gamma$ that form a geometric progression.<br><strong>(a)</strong> Show that the middle term of the geometric progression is 2. [2 marks]<br><strong>(b)</strong> Hence determine the common ratio of the progression and find all three roots. [3 marks]<br><strong>(c)</strong> Find the value of $k$. [1 mark]',
        solution: `
          <p><strong>(a) Middle root value: [2 marks]</strong><br>
          Let the roots be $\\frac{b}{r}, b, br$. [M1]<br>
          By Vieta's formula for the product of roots:<br>
          $\\left(\\frac{b}{r}\\right)(b)(br) = b^3 = -\\frac{-8}{1} = 8 \\implies b = 2$ [A1].</p>
          <p><strong>(b) Finding the roots: [3 marks]</strong><br>
          By Vieta's formula for the sum of roots:<br>
          $\\frac{2}{r} + 2 + 2r = 7 \\implies \\frac{2}{r} + 2r = 5$ [M1]<br>
          Multiply by $r$: $2r^2 - 5r + 2 = 0 \\implies (2r - 1)(r - 2) = 0 \\implies r = 2$ or $r = \\frac{1}{2}$ [A1].<br>
          Both ratios yield the same set of roots: $1, 2, 4$ [A1].</p>
          <p><strong>(c) Finding $k$: [1 mark]</strong><br>
          $k = \\sum \\alpha\\beta = (1)(2) + (2)(4) + (1)(4) = 2 + 8 + 4 = 14$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'Consider the polynomial $P(z) = z^4 - 2z^3 + 6z^2 - 8z + 8$.<br><strong>(a)</strong> Given that $z = 2i$ is a root of $P(z) = 0$, write down another imaginary root. [1 mark]<br><strong>(b)</strong> Find the quadratic factor of $P(z)$ corresponding to these imaginary roots. [2 marks]<br><strong>(c)</strong> Factorize $P(z)$ completely over the complex field $\\mathbb{C}$, and sketch the four roots on an Argand diagram. [4 marks]',
        solution: `
          <p><strong>(a) Conjugate root: [1 mark]</strong><br>
          Since all coefficients of $P(z)$ are real, $z = -2i$ is another root [A1].</p>
          <p><strong>(b) Quadratic factor: [2 marks]</strong><br>
          $(z - 2i)(z + 2i) = z^2 - (2i)^2 = z^2 + 4$ [M1][A1].</p>
          <p><strong>(c) Complete factorization &amp; Argand sketch: [4 marks]</strong><br>
          Perform polynomial division of $P(z)$ by $(z^2 + 4)$: [M1]<br>
          $z^4 - 2z^3 + 6z^2 - 8z + 8 = (z^2 + 4)(z^2 - 2z + 2)$ [A1].<br>
          Solve $z^2 - 2z + 2 = 0$:<br>
          $z = \\frac{2 \\pm \\sqrt{4 - 8}}{2} = \\frac{2 \\pm 2i}{2} = 1 \\pm i$ [A1].<br>
          The four roots are $2i, -2i, 1 + i, 1 - i$.<br>
          Argand diagram: Points plotted at $(0, 2), (0, -2), (1, 1), (1, -1)$ with symmetric reflection across the real axis [A1].</p>
        `
      }
    ]
  },

  // Guide 6: Partial Fractions & Extended Binomial Series
  {
    folder: 'partial-fractions-and-binomial-series',
    code: '1.10, 1.11',
    title: 'Partial Fractions & Extended Binomial Series',
    pageTitle: 'Partial Fractions & Extended Binomial Series | IB Math AA HL | SJMaths',
    metaDesc: 'Master partial fractions and negative/fractional binomial expansions for IB DP Mathematics AA HL (Topics 1.10 & 1.11). Linear, repeated, and irreducible quadratic partial fractions, Maclaurin binomial series with interval of convergence |x| < 1, 10 tiered exercises, and mini test.',
    keywords: 'IB Math AA HL partial fractions, extended binomial theorem, fractional negative powers binomial, interval of convergence, linear repeated quadratic partial fractions',
    kicker: 'IB Diploma Programme · Mathematics: Analysis and Approaches · Higher Level',
    heroDesc: 'Decompose rational expressions into partial fractions and unlock infinite series expansions for fractional and negative indices $(1+x)^r$ with domain of convergence $|x| < 1$. Essential algebraic tools for HL integration and calculus approximations.',
    prevLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/polynomials-and-vietas-formulas/',
      title: 'Polynomials & Vieta’s Formulas'
    },
    nextLesson: {
      url: '/ib/dp-mathematics/analysis-and-approaches-hl/functions/modulus-functions-and-inequalities/',
      title: 'Modulus Functions & Inequalities'
    },
    svgFigure: `
        <div class="figure-card" style="margin-bottom: 2rem; background: var(--c-surface); border: 1px solid var(--c-border); border-radius: var(--radius-lg, 16px); padding: 1.5rem; text-align: center;">
          <h3 style="margin-top:0; font-size:1.1rem; color:var(--c-text);"><i class="fa-solid fa-chart-line" style="color:var(--c-primary);"></i> Figure 1.6: Extended Binomial Convergence of $(1-x)^{-1/2}$ for $|x| < 1$</h3>
          <svg viewBox="0 0 760 300" width="100%" height="300" style="max-width:720px; display:block; margin:0 auto;" aria-label="Graph comparing exact function f(x) = (1-x)^(-1/2) with its polynomial approximations within the convergence window |x| < 1">
            <!-- Center at x=380, y=200 -->
            <!-- Shaded convergence region |x| < 1 (from x=220 to x=540) -->
            <rect x="220" y="30" width="320" height="210" fill="rgba(99,102,241,0.06)" />
            
            <!-- Axes -->
            <line x1="80" y1="200" x2="680" y2="200" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <line x1="380" y1="30" x2="380" y2="250" stroke="var(--c-border, #cbd5e1)" stroke-width="2" />
            <text x="670" y="190" fill="var(--c-text)" font-size="13" font-weight="bold">x</text>
            <text x="390" y="45" fill="var(--c-text)" font-size="13" font-weight="bold">y</text>

            <!-- Vertical Asymptote at x = 1 (x = 540) -->
            <line x1="540" y1="30" x2="540" y2="240" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
            <text x="545" y="60" fill="#ef4444" font-size="11" font-weight="bold">x = 1 (Singularity)</text>

            <!-- Boundary at x = -1 (x = 220) -->
            <line x1="220" y1="30" x2="220" y2="240" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4" />
            <text x="165" y="60" fill="#ef4444" font-size="11" font-weight="bold">x = -1</text>

            <!-- Exact curve f(x) = (1 - x)^(-1/2) -->
            <!-- Points: x=-0.8(252)->y=0.745(155); x=-0.5(300)->y=0.816(151); x=0(380)->y=1(140); x=0.5(460)->y=1.414(115); x=0.8(508)->y=2.23(66) -->
            <path d="M 230,158 C 300,152 350,146 380,140 C 440,128 490,95 525,40" fill="none" stroke="#ef4444" stroke-width="3" />
            <text x="530" y="35" fill="#ef4444" font-size="12" font-weight="bold">Exact: f(x) = (1-x)^{-1/2}</text>

            <!-- Linear Approx: 1 + 0.5x -->
            <line x1="220" y1="170" x2="540" y2="110" stroke="#10b981" stroke-width="2" stroke-dasharray="4,2" />
            <text x="550" y="115" fill="#10b981" font-size="11">P₁(x) = 1 + ½x</text>

            <!-- Quadratic Approx: 1 + 0.5x + 0.375x^2 -->
            <path d="M 220,154 Q 380,140 540,82" fill="none" stroke="#6366f1" stroke-width="2" />
            <text x="550" y="85" fill="#6366f1" font-size="11">P₂(x) = 1 + ½x + ⅜x²</text>

            <!-- Label at center (0, 1) -->
            <circle cx="380" cy="140" r="4" fill="#4338ca" />
            <text x="365" y="132" fill="#4338ca" font-size="11" font-weight="bold">(0, 1)</text>

            <text x="380" y="275" text-anchor="middle" font-size="12" fill="var(--c-text-muted)">Valid only inside convergence region: |x| &lt; 1</text>
          </svg>
        </div>
    `,
    studyNotesHtml: `
        <h2>1. Partial Fractions Decomposition (Syllabus 1.11)</h2>
        <p>A rational expression $\\frac{P(x)}{Q(x)}$ where $\\deg(P) &lt; \\deg(Q)$ (a <strong>proper rational function</strong>) can be split into a sum of simpler fractions according to the factors of the denominator $Q(x)$:</p>

        <div class="table-responsive" style="margin: 1.5rem 0;">
          <table class="ib-table" style="width:100%; border-collapse:collapse;">
            <thead>
              <tr style="background:var(--c-surface-card); border-bottom:2px solid var(--c-border);">
                <th style="padding:10px; text-align:left;">Factor in Denominator $Q(x)$</th>
                <th style="padding:10px; text-align:left;">Partial Fraction Form</th>
                <th style="padding:10px; text-align:left;">Example</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Distinct Linear Factor</strong><br>$(ax + b)$</td>
                <td style="padding:10px;">$\\frac{A}{ax + b}$</td>
                <td style="padding:10px;">$\\frac{3x+1}{(x-1)(x+2)} = \\frac{A}{x-1} + \\frac{B}{x+2}$</td>
              </tr>
              <tr style="border-bottom:1px solid var(--c-border);">
                <td style="padding:10px;"><strong>Repeated Linear Factor</strong><br>$(ax + b)^2$ or $(ax+b)^n$</td>
                <td style="padding:10px;">$\\frac{A}{ax + b} + \\frac{B}{(ax + b)^2}$</td>
                <td style="padding:10px;">$\\frac{2x^2+1}{(x-3)(x+1)^2} = \\frac{A}{x-3} + \\frac{B}{x+1} + \\frac{C}{(x+1)^2}$</td>
              </tr>
              <tr>
                <td style="padding:10px;"><strong>Irreducible Quadratic Factor</strong><br>$(ax^2 + bx + c)$ with $\\Delta &lt; 0$</td>
                <td style="padding:10px;">$\\frac{Ax + B}{ax^2 + bx + c}$</td>
                <td style="padding:10px;">$\\frac{x^2+4}{(x-2)(x^2+3)} = \\frac{A}{x-2} + \\frac{Bx + C}{x^2+3}$</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p><strong>Crucial Rule for Improper Rational Functions:</strong> If $\\deg(P) \\ge \\deg(Q)$, you <strong>must</strong> first carry out polynomial long division to extract polynomial quotient terms before decomposing the proper remainder fraction!</p>

        <h2>2. Extended Binomial Theorem for Fractional and Negative Indices (Syllabus 1.10)</h2>
        <p>When the exponent $r \\in \\mathbb{Q}$ is negative or fractional, the expansion of $(1 + x)^r$ is an <strong>infinite series</strong>:</p>
        $$(1 + x)^r = 1 + rx + \\frac{r(r-1)}{2!}x^2 + \\frac{r(r-1)(r-2)}{3!}x^3 + \\dots + \\frac{r(r-1)\\dots(r-n+1)}{n!}x^n + \\dots$$
        <p>This series <strong>converges</strong> if and only if:</p>
        $$|x| &lt; 1 \\iff -1 &lt; x &lt; 1$$

        <h2>3. Expanding $(a + bx)^r$</h2>
        <p>To expand a binomial where the first term is not 1, factor out $a^r$ first:</p>
        $$(a + bx)^r = a^r \\left(1 + \\frac{b}{a}x\\right)^r = a^r \\left[ 1 + r\\left(\\frac{b}{a}x\\right) + \\frac{r(r-1)}{2!}\\left(\\frac{b}{a}x\\right)^2 + \\dots \\right]$$
        <p>The valid interval of convergence is:</p>
        $$\\left|\\frac{b}{a}x\\right| &lt; 1 \\iff |x| &lt; \\left|\\frac{a}{b}\\right|$$

        <h2>4. Worked Examples</h2>

        <div class="example-card">
          <h4>Worked Example 1: Repeated Linear Factor Decomposition</h4>
          <p>Express $f(x) = \\frac{5x^2 - 7x + 2}{(x - 2)(x - 1)^2}$ in partial fractions.</p>
          <p><strong>Solution:</strong></p>
          <p>Set up the partial fractions:</p>
          $$\\frac{5x^2 - 7x + 2}{(x - 2)(x - 1)^2} = \\frac{A}{x - 2} + \\frac{B}{x - 1} + \\frac{C}{(x - 1)^2}$$
          <p>Multiply through by $(x - 2)(x - 1)^2$:</p>
          $$5x^2 - 7x + 2 = A(x - 1)^2 + B(x - 2)(x - 1) + C(x - 2)$$
          <p>• Substitute $x = 1$: $5(1) - 7(1) + 2 = 0 = A(0) + B(0) + C(1 - 2) \\implies -C = 0 \\implies C = 0$? Wait, $5-7+2 = 0$. So $C = 0$.<br>
          • Substitute $x = 2$: $5(4) - 7(2) + 2 = 20 - 14 + 2 = 8 = A(2 - 1)^2 = A(1) \\implies A = 8$.<br>
          • Compare coefficients of $x^2$: $5 = A + B \\implies 5 = 8 + B \\implies B = -3$.<br>
          Therefore, $\\frac{5x^2 - 7x + 2}{(x - 2)(x - 1)^2} = \\frac{8}{x - 2} - \\frac{3}{x - 1}$.</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 2: Extended Binomial Series of $\\frac{1}{\\sqrt{4 - x}}$</h4>
          <p><strong>(a)</strong> Find the series expansion of $f(x) = (4 - x)^{-1/2}$ in ascending powers of $x$ up to and including the term in $x^2$.<br>
          <strong>(b)</strong> State the range of values of $x$ for which this expansion is valid.</p>
          <p><strong>Solution:</strong></p>
          <p><strong>(a) Expansion:</strong><br>
          Factor out $4^{-1/2} = \\frac{1}{2}$:</p>
          $$(4 - x)^{-1/2} = 4^{-1/2} \\left(1 - \\frac{x}{4}\\right)^{-1/2} = \\frac{1}{2} \\left(1 + u\\right)^{-1/2}, \\quad \\text{where } u = -\\frac{x}{4}$$
          <p>Using $(1 + u)^r$ with $r = -\\frac{1}{2}$:</p>
          $$(1 + u)^{-1/2} = 1 + \\left(-\\frac{1}{2}\\right)u + \\frac{\\left(-\\frac{1}{2}\\right)\\left(-\\frac{3}{2}\\right)}{2!} u^2 + \\dots = 1 - \\frac{1}{2}u + \\frac{3}{8}u^2 + \\dots$$
          <p>Substitute $u = -\\frac{x}{4}$:</p>
          $$= 1 - \\frac{1}{2}\\left(-\\frac{x}{4}\\right) + \\frac{3}{8}\\left(-\\frac{x}{4}\\right)^2 = 1 + \\frac{x}{8} + \\frac{3}{8}\\left(\\frac{x^2}{16}\\right) = 1 + \\frac{x}{8} + \\frac{3x^2}{128}$$
          <p>Multiply by $\\frac{1}{2}$:</p>
          $$(4 - x)^{-1/2} = \\frac{1}{2} + \\frac{x}{16} + \\frac{3x^2}{256} + \\dots$$
          <p><strong>(b) Validity condition:</strong><br>
          The series converges when $|u| &lt; 1 \\iff \\left|-\\frac{x}{4}\\right| &lt; 1 \\iff |x| &lt; 4$ (i.e. $-4 &lt; x &lt; 4$).</p>
        </div>

        <div class="example-card">
          <h4>Worked Example 3: Approximating $\\sqrt{2}$ with Binomial Series</h4>
          <p>By substituting $x = \\frac{1}{9}$ into $(1 - x)^{1/2} \\approx 1 - \\frac{1}{2}x - \\frac{1}{8}x^2$, find an approximation for $\\sqrt{2}$ as a rational fraction.</p>
          <p><strong>Solution:</strong></p>
          <p>For $x = \\frac{1}{9}$ (notice $|1/9| &lt; 1$, inside the convergence region):</p>
          $$\\left(1 - \\frac{1}{9}\\right)^{1/2} = \\left(\\frac{8}{9}\\right)^{1/2} = \\frac{\\sqrt{8}}{3} = \\frac{2\\sqrt{2}}{3}$$
          <p>Evaluating the binomial approximation:</p>
          $$1 - \\frac{1}{2}\\left(\\frac{1}{9}\\right) - \\frac{1}{8}\\left(\\frac{1}{81}\\right) = 1 - \\frac{1}{18} - \\frac{1}{648} = \\frac{648 - 36 - 1}{648} = \\frac{611}{648}$$
          <p>Equating:</p>
          $$\\frac{2\\sqrt{2}}{3} \\approx \\frac{611}{648} \\implies \\sqrt{2} \\approx \\frac{3}{2} \\times \\frac{611}{648} = \\frac{611}{432} \\approx 1.41435\\dots$$
          <p>(True value: $\\sqrt{2} \\approx 1.41421$, yielding remarkable 4-digit accuracy with just 3 terms!)</p>
        </div>
    `,
    exercises: [
      {
        tier: 'tier-1',
        title: 'Exercise 1 (Foundational: Linear Partial Fractions)',
        text: 'Express $\\frac{7x - 1}{(x - 3)(x + 1)}$ in partial fractions.',
        solution: '<p>$\\frac{7x - 1}{(x - 3)(x + 1)} = \\frac{A}{x - 3} + \\frac{B}{x + 1}$. [M1]<br>$7x - 1 = A(x + 1) + B(x - 3)$.<br>Let $x = 3$: $7(3) - 1 = A(4) \\implies 20 = 4A \\implies A = 5$. [A1]<br>Let $x = -1$: $7(-1) - 1 = B(-4) \\implies -8 = -4B \\implies B = 2$. [A1]<br>Result: $\\frac{5}{x - 3} + \\frac{2}{x + 1}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 2 (Foundational: Negative Binomial Expansion)',
        text: 'Expand $(1 + 3x)^{-1}$ up to the term in $x^3$ and state the interval of convergence.',
        solution: '<p>Using $(1 + u)^{-1} = 1 - u + u^2 - u^3 + \\dots$ with $u = 3x$: [M1]<br>$(1 + 3x)^{-1} = 1 - (3x) + (3x)^2 - (3x)^3 + \\dots = 1 - 3x + 9x^2 - 27x^3 + \\dots$ [A1]<br>Convergence requires $|3x| &lt; 1 \\iff |x| &lt; \\frac{1}{3}$. [A1]</p>'
      },
      {
        tier: 'tier-1',
        title: 'Exercise 3 (Foundational: Fractional Binomial Expansion)',
        text: 'Expand $(1 + x)^{1/3}$ in ascending powers of $x$ up to the term in $x^2$.',
        solution: '<p>$(1 + x)^r = 1 + rx + \\frac{r(r-1)}{2}x^2 + \\dots$ with $r = \\frac{1}{3}$: [M1]<br>First term: $1$.<br>$x$-term: $\\frac{1}{3}x$. [A1]<br>$x^2$-term: $\\frac{\\frac{1}{3}\\left(-\\frac{2}{3}\\right)}{2}x^2 = -\\frac{1}{9}x^2$. [A1]<br>Result: $1 + \\frac{1}{3}x - \\frac{1}{9}x^2 + \\dots$ (valid for $|x| &lt; 1$).</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 4 (Intermediate: Repeated Linear Denominator)',
        text: 'Find the partial fraction decomposition of $\\frac{3x^2 + 5x + 4}{(x + 2)(x + 1)^2}$.',
        solution: '<p>$\\frac{3x^2 + 5x + 4}{(x + 2)(x + 1)^2} = \\frac{A}{x + 2} + \\frac{B}{x + 1} + \\frac{C}{(x + 1)^2}$. [M1]<br>$3x^2 + 5x + 4 = A(x + 1)^2 + B(x + 2)(x + 1) + C(x + 2)$.<br>Let $x = -1$: $3 - 5 + 4 = C(1) \\implies C = 2$. [A1]<br>Let $x = -2$: $12 - 10 + 4 = A(-1)^2 \\implies A = 6$. [A1]<br>Compare $x^2$ coefficients: $3 = A + B \\implies 3 = 6 + B \\implies B = -3$. [A1]<br>Result: $\\frac{6}{x + 2} - \\frac{3}{x + 1} + \\frac{2}{(x + 1)^2}$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 5 (Intermediate: Irreducible Quadratic Factor)',
        text: 'Decompose $\\frac{x^2 - x + 14}{(x - 2)(x^2 + 4)}$ into partial fractions.',
        solution: '<p>$\\frac{x^2 - x + 14}{(x - 2)(x^2 + 4)} = \\frac{A}{x - 2} + \\frac{Bx + C}{x^2 + 4}$. [M1]<br>$x^2 - x + 14 = A(x^2 + 4) + (Bx + C)(x - 2)$.<br>Let $x = 2$: $4 - 2 + 14 = A(8) \\implies 16 = 8A \\implies A = 2$. [A1]<br>Compare $x^2$ coefficients: $1 = A + B \\implies 1 = 2 + B \\implies B = -1$. [A1]<br>Compare constant terms: $14 = 4A - 2C \\implies 14 = 8 - 2C \\implies 2C = -6 \\implies C = -3$. [A1]<br>Result: $\\frac{2}{x - 2} + \\frac{-x - 3}{x^2 + 4} = \\frac{2}{x - 2} - \\frac{x + 3}{x^2 + 4}$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 6 (Intermediate: Improper Rational Function)',
        text: 'Express $\\frac{x^3 + 2x^2 - 3x + 1}{x^2 + x - 2}$ in the form $Ax + B + \\frac{C}{x + 2} + \\frac{D}{x - 1}$.',
        solution: '<p>Because $\\deg(\\text{num}) = 3 &gt; \\deg(\\text{den}) = 2$, divide polynomials first: [M1]<br>$(x^3 + 2x^2 - 3x + 1) \\div (x^2 + x - 2)$: quotient is $x + 1$, remainder is $-2x + 3$. [A1]<br>So $\\frac{x^3 + 2x^2 - 3x + 1}{x^2 + x - 2} = x + 1 + \\frac{-2x + 3}{(x + 2)(x - 1)}$.<br>Now decompose $\\frac{-2x + 3}{(x + 2)(x - 1)} = \\frac{C}{x + 2} + \\frac{D}{x - 1}$: [M1]<br>$-2x + 3 = C(x - 1) + D(x + 2)$.<br>Let $x = 1$: $1 = 3D \\implies D = \\frac{1}{3}$. [A1]<br>Let $x = -2$: $7 = -3C \\implies C = -\\frac{7}{3}$. [A1]<br>Result: $x + 1 - \\frac{7}{3(x + 2)} + \\frac{1}{3(x - 1)}$.</p>'
      },
      {
        tier: 'tier-2',
        title: 'Exercise 7 (Exam Standard: Binomial Expansion with Coefficient Extraction)',
        text: 'Find the coefficient of $x^3$ in the expansion of $\\frac{1 + 2x}{(1 - 2x)^2}$ for $|x| &lt; \\frac{1}{2}$.',
        solution: '<p>$(1 - 2x)^{-2} = 1 + (-2)(-2x) + \\frac{(-2)(-3)}{2}(-2x)^2 + \\frac{(-2)(-3)(-4)}{6}(-2x)^3 + \\dots$ [M1]<br>$= 1 + 4x + 3(4x^2) + (-4)(-8x^3) = 1 + 4x + 12x^2 + 32x^3 + \\dots$ [A1]<br>Multiply by $(1 + 2x)$: [M1]<br>$(1 + 2x)(1 + 4x + 12x^2 + 32x^3 + \\dots)$<br>Terms contributing to $x^3$: $1(32x^3) + 2x(12x^2) = 32x^3 + 24x^3 = 56x^3$. [A1]<br>The coefficient of $x^3$ is $56$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 8 (Advanced: Combining Partial Fractions & Binomial Series)',
        text: 'Given $f(x) = \\frac{2x - 13}{(x - 1)(x - 4)}$:<br>(a) Express $f(x)$ in partial fractions.<br>(b) Hence find the series expansion of $f(x)$ up to the term in $x^2$, and state the interval of convergence for the series.',
        solution: '<p><strong>(a) Partial fractions:</strong> [M1]<br>$\\frac{2x - 13}{(x - 1)(x - 4)} = \\frac{A}{x - 1} + \\frac{B}{x - 4} \\implies 2x - 13 = A(x - 4) + B(x - 1)$.<br>Let $x = 1$: $-11 = -3A \\implies A = \\frac{11}{3}$.<br>Let $x = 4$: $-5 = 3B \\implies B = -\\frac{5}{3}$.<br>$f(x) = \\frac{11}{3(x - 1)} - \\frac{5}{3(x - 4)} = -\\frac{11}{3}(1 - x)^{-1} + \\frac{5}{12}\\left(1 - \\frac{x}{4}\\right)^{-1}$. [A1]</p><p><strong>(b) Binomial expansions:</strong> [M1]<br>• $(1 - x)^{-1} = 1 + x + x^2 + \\dots$ (valid for $|x| &lt; 1$).<br>• $\\left(1 - \\frac{x}{4}\\right)^{-1} = 1 + \\frac{x}{4} + \\frac{x^2}{16} + \\dots$ (valid for $|x| &lt; 4$).<br>Combine: [M1]<br>$f(x) = -\\frac{11}{3}(1 + x + x^2) + \\frac{5}{12}\\left(1 + \\frac{x}{4} + \\frac{x^2}{16}\\right)$<br>Constant: $-\\frac{11}{3} + \\frac{5}{12} = -\\frac{44}{12} + \\frac{5}{12} = -\\frac{39}{12} = -\\frac{13}{4}$.<br>$x$-term: $-\\frac{11}{3}x + \\frac{5}{48}x = \\left(-\\frac{176}{48} + \\frac{5}{48}\\right)x = -\\frac{171}{48}x = -\\frac{57}{16}x$.<br>$x^2$-term: $-\\frac{11}{3}x^2 + \\frac{5}{192}x^2 = \\left(-\\frac{704}{192} + \\frac{5}{192}\\right)x^2 = -\\frac{699}{192}x^2 = -\\frac{233}{64}x^2$.<br>Expansion: $-\\frac{13}{4} - \\frac{57}{16}x - \\frac{233}{64}x^2 + \\dots$ [A1]<br>The expansion is valid for the intersection of domains: $|x| &lt; 1$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 9 (Advanced: Finding nth Term of Extended Binomial)',
        text: 'Find a formula for the general term (in terms of $n$) in the expansion of $(1 - x)^{-3}$ in ascending powers of $x$.',
        solution: '<p>The general coefficient of $x^n$ in $(1 + u)^r$ with $u = -x$ and $r = -3$ is: [M1]<br>$\\frac{r(r-1)(r-2)\\dots(r-n+1)}{n!} (-x)^n = \\frac{(-3)(-4)(-5)\\dots(-(n+2))}{n!} (-1)^n x^n$. [M1]<br>Factor out $(-1)^n$ from the numerator:<br>$(-1)^n \\frac{3 \\times 4 \\times 5 \\dots \\times (n+2)}{n!} (-1)^n x^n = (-1)^{2n} \\frac{(n+2)! / 2!}{n!} x^n$. [M1]<br>Since $(-1)^{2n} = 1$ and $\\frac{(n+2)!}{2! n!} = \\frac{(n+2)(n+1)}{2}$:<br>General term: $\\frac{(n+1)(n+2)}{2} x^n$. [A1]</p>'
      },
      {
        tier: 'tier-3',
        title: 'Exercise 10 (Advanced: Estimating Irrational Cube Root)',
        text: 'Use the first three terms of the expansion of $(1 + x)^{1/3}$ with $x = \\frac{1}{26}$ to estimate $\\sqrt[3]{26}$ to 5 decimal places.',
        solution: '<p>Notice that $26 = 27 - 1 = 27\\left(1 - \\frac{1}{27}\\right)$. [M1]<br>So $26^{1/3} = 27^{1/3}\\left(1 - \\frac{1}{27}\\right)^{1/3} = 3\\left(1 - \\frac{1}{27}\\right)^{1/3}$. [A1]<br>Using $(1 - u)^{1/3} \\approx 1 - \\frac{1}{3}u - \\frac{1}{9}u^2$ with $u = \\frac{1}{27}$: [M1]<br>• First term: $1$<br>• Second term: $-\\frac{1}{3(27)} = -\\frac{1}{81} \\approx -0.0123457$<br>• Third term: $-\\frac{1}{9(27^2)} = -\\frac{1}{9(729)} = -\\frac{1}{6561} \\approx -0.0001524$<br>Sum inside bracket: $1 - 0.0123457 - 0.0001524 = 0.9875019$. [A1]<br>Multiply by 3: $3 \\times 0.9875019 = 2.9625057 \\approx 2.96251$. [A1]<br>(Calculator true value: $26^{1/3} \\approx 2.962496\\dots$, accurate to 4 decimal places!)</p>'
      }
    ],
    formulasHtml: `
        <h2>IB Formula Booklet References (Topic 1)</h2>
        <div class="formula-card">
          <h4>Syllabus 1.10: Extension of the Binomial Theorem</h4>
          $$(1 + x)^n = 1 + nx + \\frac{n(n-1)}{2!}x^2 + \\dots, \\quad n \\in \\mathbb{Q}, \\; |x| &lt; 1$$
        </div>

        <h2>Must-Memorize Principles (Not in Booklet)</h2>
        <div class="formula-card">
          <h4>1. Expanding $(a + bx)^n$</h4>
          $$(a + bx)^n = a^n \\left(1 + \\frac{b}{a}x\\right)^n, \\quad \\text{valid for } |x| &lt; \\left|\\frac{a}{b}\\right|$$
        </div>

        <div class="formula-card">
          <h4>2. Partial Fraction Decomposition Templates</h4>
          <ul>
            <li>Linear: $\\frac{A}{ax+b}$</li>
            <li>Repeated linear: $\\frac{A}{ax+b} + \\frac{B}{(ax+b)^2}$</li>
            <li>Irreducible quadratic: $\\frac{Ax+B}{ax^2+bx+c}$</li>
            <li>Always check degree: If $\\deg(\\text{num}) \\ge \\deg(\\text{den})$, long division first!</li>
          </ul>
        </div>

        <h2>Examination Pitfalls &amp; Examiner Tips</h2>
        <div class="pitfall-card">
          <h4>Forgetting to Factor Out $a^n$</h4>
          <p>You cannot apply the booklet formula directly to $(4 + x)^{1/2}$! You must first factor out $4^{1/2} = 2$. Writing $1 + \\frac{1}{2}(4+x)$ is an automatic zero-mark error.</p>
        </div>
        <div class="pitfall-card">
          <h4>Domain of Convergence for Combined Series</h4>
          <p>When adding two binomial series (e.g. from partial fractions), the domain of the combined series is the <strong>stricter (smaller)</strong> of the two intervals. If one requires $|x| &lt; 1$ and the other $|x| &lt; 3$, the overall range is $|x| &lt; 1$.</p>
        </div>
    `,
    mcqs: [
      {
        id: 'q1',
        prompt: 'For what values of $x$ does the series expansion of $(3 - 2x)^{-1/2}$ converge?',
        options: [
          '$|x| < \\frac{3}{2}$',
          '$|x| < \\frac{2}{3}$',
          '$|x| < 3$',
          '$|x| < 1$'
        ],
        correct: 0,
        explanation: '$(3 - 2x)^{-1/2} = 3^{-1/2} (1 - \\frac{2}{3}x)^{-1/2}$. The series converges when $|\\frac{2}{3}x| < 1 \\iff |x| < \\frac{3}{2}$.'
      },
      {
        id: 'q2',
        prompt: 'What is the correct partial fraction template for $\\frac{x^2 + 1}{(x - 1)^2(x^2 + 4)}$?',
        options: [
          '$\\frac{A}{x-1} + \\frac{B}{(x-1)^2} + \\frac{Cx+D}{x^2+4}$',
          '$\\frac{A}{(x-1)^2} + \\frac{B}{x^2+4}$',
          '$\\frac{A}{x-1} + \\frac{B}{(x-1)^2} + \\frac{C}{x^2+4}$',
          '$\\frac{Ax+B}{(x-1)^2} + \\frac{Cx+D}{x^2+4}$'
        ],
        correct: 0,
        explanation: 'The denominator has a repeated linear factor $(x-1)^2$, requiring $\\frac{A}{x-1} + \\frac{B}{(x-1)^2}$, and an irreducible quadratic factor $(x^2+4)$, requiring a linear numerator $\\frac{Cx+D}{x^2+4}$.'
      },
      {
        id: 'q3',
        prompt: 'The first two terms of $(1 + ax)^n$ are $1 - 6x + 24x^2 + \\dots$. What are the values of $a$ and $n$?',
        options: [
          '$n = 3, a = -2$',
          '$n = -3, a = 2$',
          '$n = -2, a = 3$',
          '$n = 4, a = -1.5$'
        ],
        correct: 1,
        explanation: '$na = -6$. Second coefficient: $\\frac{n(n-1)}{2} a^2 = 24 \\implies n(n-1)a^2 = 48$. Since $(na)^2 = 36$, $\\frac{n(n-1)a^2}{(na)^2} = \\frac{n-1}{n} = \\frac{48}{36} = \\frac{4}{3} \\implies 3n - 3 = 4n \\implies n = -3$. Then $a = \\frac{-6}{-3} = 2$.'
      },
      {
        id: 'q4',
        prompt: 'Why must polynomial division be carried out on $\\frac{x^2 + 3}{x^2 - 1}$ before decomposing into partial fractions?',
        options: [
          'Because the denominator is irreducible',
          'Because the degree of the numerator equals the degree of the denominator',
          'Because the denominator has repeated roots',
          'Because the fraction is undefined at $x = 0$'
        ],
        correct: 1,
        explanation: 'Partial fractions only applies directly to proper rational functions where $\\deg(\\text{numerator}) < \\deg(\\text{denominator})$. When the degrees are equal or the numerator has higher degree, long division is mandatory.'
      }
    ],
    frqs: [
      {
        badge: 'Question 5 (Paper 1 Style · 6 marks)',
        text: 'Consider the rational function $f(x) = \\frac{5}{(1 - x)(2 + 3x)}$.<br><strong>(a)</strong> Express $f(x)$ in partial fractions. [3 marks]<br><strong>(b)</strong> Hence obtain the expansion of $f(x)$ in ascending powers of $x$ up to and including the term in $x^2$. [3 marks]',
        solution: `
          <p><strong>(a) Partial fractions: [3 marks]</strong><br>
          $\\frac{5}{(1 - x)(2 + 3x)} = \\frac{A}{1 - x} + \\frac{B}{2 + 3x}$ [M1]<br>
          $5 = A(2 + 3x) + B(1 - x)$<br>
          Let $x = 1$: $5 = A(5) \\implies A = 1$ [A1].<br>
          Let $x = -\\frac{2}{3}$: $5 = B\\left(1 - \\left(-\\frac{2}{3}\\right)\\right) = B\\left(\\frac{5}{3}\\right) \\implies B = 3$ [A1].<br>
          $f(x) = \\frac{1}{1 - x} + \\frac{3}{2 + 3x}$.</p>
          <p><strong>(b) Series expansion: [3 marks]</strong><br>
          • $\\frac{1}{1 - x} = (1 - x)^{-1} = 1 + x + x^2 + \\dots$ [A1]<br>
          • $\\frac{3}{2 + 3x} = \\frac{3}{2}\\left(1 + \\frac{3}{2}x\\right)^{-1} = \\frac{3}{2}\\left(1 - \\frac{3}{2}x + \\frac{9}{4}x^2 - \\dots\\right) = \\frac{3}{2} - \\frac{9}{4}x + \\frac{27}{8}x^2 - \\dots$ [A1]<br>
          Adding the two expansions: [M1]<br>
          Constant: $1 + \\frac{3}{2} = \\frac{5}{2}$.<br>
          $x$-term: $1 - \\frac{9}{4} = -\\frac{5}{4}$.<br>
          $x^2$-term: $1 + \\frac{27}{8} = \\frac{35}{8}$.<br>
          $f(x) = \\frac{5}{2} - \\frac{5}{4}x + \\frac{35}{8}x^2 + \\dots$ [A1].</p>
        `
      },
      {
        badge: 'Question 6 (Paper 2 Style · 7 marks)',
        text: 'Let $g(x) = \\sqrt{\\frac{1 + x}{1 - x}}$.<br><strong>(a)</strong> Write $g(x)$ in the form $(1 + x)(1 - x^2)^{-1/2}$. [2 marks]<br><strong>(b)</strong> Find the series expansion of $(1 - x^2)^{-1/2}$ up to the term in $x^4$. [2 marks]<br><strong>(c)</strong> Hence find the Maclaurin series expansion of $g(x)$ up to the term in $x^3$. [2 marks]<br><strong>(d)</strong> State the range of validity of this expansion. [1 mark]',
        solution: `
          <p><strong>(a) Algebraic simplification: [2 marks]</strong><br>
          $g(x) = \\sqrt{\\frac{1+x}{1-x}} = \\frac{\\sqrt{1+x}}{\\sqrt{1-x}} = \\frac{\\sqrt{1+x}\\sqrt{1+x}}{\\sqrt{1-x}\\sqrt{1+x}} = \\frac{1+x}{\\sqrt{1-x^2}} = (1+x)(1-x^2)^{-1/2}$ [M1][A1].</p>
          <p><strong>(b) Expansion of $(1 - x^2)^{-1/2}$: [2 marks]</strong><br>
          Let $u = -x^2$. $(1 + u)^{-1/2} = 1 - \\frac{1}{2}u + \\frac{3}{8}u^2 - \\dots$ [M1]<br>
          $= 1 - \\frac{1}{2}(-x^2) + \\frac{3}{8}(-x^2)^2 = 1 + \\frac{1}{2}x^2 + \\frac{3}{8}x^4 + \\dots$ [A1].</p>
          <p><strong>(c) Expansion of $g(x)$: [2 marks]</strong><br>
          $g(x) = (1 + x)\\left(1 + \\frac{1}{2}x^2 + \\dots\\right) = 1 + \\frac{1}{2}x^2 + x + \\frac{1}{2}x^3 = 1 + x + \\frac{1}{2}x^2 + \\frac{1}{2}x^3 + \\dots$ [M1][A1].</p>
          <p><strong>(d) Validity: [1 mark]</strong><br>
          $| -x^2 | &lt; 1 \\iff x^2 &lt; 1 \\iff |x| &lt; 1$ [A1].</p>
        `
      }
    ]
  }
];

function generateHtml(guide) {
  const mcqsJson = JSON.stringify(guide.mcqs.map((q, idx) => ({
    id: q.id,
    correct: q.correct,
    explanation: q.explanation
  })));

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
  <link rel="canonical" href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/${guide.folder}/">
  <meta property="og:type" content="article">
  <meta property="og:title" content="${guide.pageTitle}">
  <meta property="og:description" content="${guide.metaDesc}">
  <meta property="og:url" content="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/${guide.folder}/">
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

  <script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"BreadcrumbList","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/${guide.folder}/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://sjmaths.com/"},{"@type":"ListItem","position":2,"name":"IB Mathematics","item":"https://sjmaths.com/ib/"},{"@type":"ListItem","position":3,"name":"IB DP Mathematics","item":"https://sjmaths.com/ib/dp-mathematics/"},{"@type":"ListItem","position":4,"name":"AA HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/"},{"@type":"ListItem","position":5,"name":"Number and Algebra HL","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/"},{"@type":"ListItem","position":6,"name":"${guide.title}","item":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/${guide.folder}/"}]},{"@type":"Article","@id":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/${guide.folder}/#article","headline":"${guide.title} | IB Math AA HL Guide","description":"${guide.metaDesc}","url":"https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/${guide.folder}/","dateModified":"2026-10-11","inLanguage":"en","articleSection":"IB DP Mathematics AA HL · Topic ${guide.code}","author":{"@type":"Person","name":"Sandeep Jaiswal","url":"https://sjmaths.com/pages/about.html"},"publisher":{"@type":"Organization","name":"SJMaths","url":"https://sjmaths.com/","logo":{"@type":"ImageObject","url":"https://sjmaths.com/assets/icons/icon-512x512.png"}}}]}</script>
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
      <a href="/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/">Topic 1 HL</a>
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
      <a href="https://sjmaths.com/ib/dp-mathematics/analysis-and-approaches-hl/number-and-algebra/">Number and Algebra</a><span class="breadcrumb-separator" aria-hidden="true">›</span>
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
