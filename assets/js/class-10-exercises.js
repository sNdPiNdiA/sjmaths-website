const class10Formulas = {
  1: [
    { title: "Euclid's Division Lemma", tex: "Given positive integers $a$ and $b$, there exist unique integers $q$ and $r$ satisfying $a = bq + r$, where $0 \\le r < b$." },
    { title: "Fundamental Theorem of Arithmetic", tex: "Every composite number can be expressed (factorised) as a product of primes, and this factorisation is unique, apart from the order in which the prime factors occur." },
    { title: "HCF and LCM Relation", tex: "For any two positive integers $a$ and $b$, $HCF(a, b) \\times LCM(a, b) = a \\times b$." },
    { title: "Rational Numbers & Decimals", tex: "Let $x = p/q$ be a rational number. If the prime factorisation of $q$ is of the form $2^n 5^m$ ($n, m$ are non-negative integers), then $x$ has a terminating decimal expansion. Otherwise, it is non-terminating repeating." }
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