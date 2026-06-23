const class10Formulas = {
  1: [
    { title: "Euclid's Division Lemma", tex: "Given positive integers $a$ and $b$, there exist unique integers $q$ and $r$ satisfying $a = bq + r$, where $0 \\le r < b$." },
    { title: "Fundamental Theorem of Arithmetic", tex: "Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur." },
    { title: "HCF and LCM Relation", tex: "For any two positive integers $a$ and $b$, $HCF(a, b) \\times LCM(a, b) = a \\times b$." },
    { title: "Rational Numbers & Decimals", tex: "Let $x = p/q$ be a rational number. If the prime factorisation of $q$ is of the form $2^n 5^m$ ($n, m$ are non-negative integers), then $x$ has a terminating decimal expansion. Otherwise, it is non-terminating repeating." }
  ],
  2: [
    { title: "Quadratic Polynomial", tex: "Standard form: $ax^2 + bx + c$ ($a \\neq 0$)." },
    { title: "Relationship between Zeroes and Coefficients", tex: "If $\\alpha$ and $\\beta$ are zeroes of $ax^2 + bx + c$:<br>Sum of zeroes ($\\alpha + \\beta$) = $-\\frac{b}{a}$<br>Product of zeroes ($\\alpha\\beta$) = $\\frac{c}{a}$" },
    { title: "Forming a Quadratic Polynomial", tex: "$k[x^2 - (\\text{Sum of zeroes})x + (\\text{Product of zeroes})]$" }
  ],
  3: [
    { title: "Pair of Linear Equations", tex: "General form: $a_1x + b_1y + c_1 = 0$ and $a_2x + b_2y + c_2 = 0$." },
    { title: "Conditions for Solvability", tex: "1. <b>Intersecting Lines (Unique Solution):</b> $\\frac{a_1}{a_2} \\neq \\frac{b_1}{b_2}$<br>2. <b>Coincident Lines (Infinitely Many Solutions):</b> $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$<br>3. <b>Parallel Lines (No Solution):</b> $\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$" }
  ],
  4: [
    { title: "Quadratic Equation", tex: "Standard form: $ax^2 + bx + c = 0$ ($a \\neq 0$)." },
    { title: "Quadratic Formula", tex: "$x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$" },
    { title: "Nature of Roots", tex: "Discriminant $D = b^2 - 4ac$:<br>1. $D > 0$: Two distinct real roots.<br>2. $D = 0$: Two equal real roots.<br>3. $D < 0$: No real roots." }
  ],
  5: [
    { title: "General Term of AP", tex: "$a_n = a + (n-1)d$, where $a$ is the first term and $d$ is the common difference." },
    { title: "Sum of First n Terms", tex: "$S_n = \\frac{n}{2}[2a + (n-1)d]$ or $S_n = \\frac{n}{2}(a + l)$, where $l$ is the last term." },
    { title: "Sum of First n Positive Integers", tex: "$S_n = \\frac{n(n+1)}{2}$" }
  ],
  6: [
    { title: "Basic Proportionality Theorem (BPT)", tex: "If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio." },
    { title: "Criteria for Similarity", tex: "1. <b>AAA:</b> Corresponding angles are equal.<br>2. <b>SSS:</b> Corresponding sides are in the same ratio.<br>3. <b>SAS:</b> One angle is equal and including sides are proportional." },
    { title: "Areas of Similar Triangles", tex: "The ratio of the areas of two similar triangles is equal to the square of the ratio of their corresponding sides." }
  ],
  7: [
    { title: "Distance Formula", tex: "Distance between $P(x_1, y_1)$ and $Q(x_2, y_2)$ is $\\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$." },
    { title: "Section Formula", tex: "The coordinates of the point $P(x, y)$ dividing the line segment joining $A(x_1, y_1)$ and $B(x_2, y_2)$ internally in the ratio $m_1 : m_2$ are $(\\frac{m_1x_2 + m_2x_1}{m_1 + m_2}, \\frac{m_1y_2 + m_2y_1}{m_1 + m_2})$." },
    { title: "Area of Triangle", tex: "Area of $\\Delta ABC$ with vertices $(x_1, y_1), (x_2, y_2), (x_3, y_3)$ is $\\frac{1}{2} |x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)|$." }
  ]
};

function openFormulaPopup(chapter) {
  let overlay = document.querySelector('.formula-popup-overlay');
  
  // Create popup if it doesn't exist
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.className = 'formula-popup-overlay';
    overlay.innerHTML = `
      <div class="formula-popup-content">
        <button class="formula-popup-close" onclick="closeFormulaPopup()">&times;</button>
        <h2 style="margin-bottom:20px; color:var(--primary); font-size:1.5rem;">Chapter Formulas</h2>
        <div id="formula-list"></div>
      </div>
    `;
    document.body.appendChild(overlay);
    
    // Close on click outside
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) closeFormulaPopup();
    });
  }
  
  const list = overlay.querySelector('#formula-list');
  const formulas = class10Formulas[chapter] || [];
  
  if (formulas.length === 0) {
    list.innerHTML = '<p>No formulas available for this chapter yet.</p>';
  } else {
    list.innerHTML = formulas.map(f => `
      <div class="formula-item">
        <span class="formula-title">${f.title}</span>
        <div>${f.tex}</div>
      </div>
    `).join('');
  }
  
  overlay.style.display = 'flex';
  
  // Trigger MathJax to render the new content
  if (window.MathJax) {
    MathJax.typesetPromise([list]).catch((err) => console.log('MathJax error:', err));
  }
}

function closeFormulaPopup() {
  const overlay = document.querySelector('.formula-popup-overlay');
  if (overlay) overlay.style.display = 'none';
}