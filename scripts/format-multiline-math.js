import fs from 'fs';
import path from 'path';

const ftaPath = path.resolve('learning/data/class-10/mathematics/chapter-1-real-numbers/fta.json');
const data = JSON.parse(fs.readFileSync(ftaPath, 'utf8'));

function formatMultilineMath(mathStr) {
  if (!mathStr || typeof mathStr !== 'string') return mathStr;
  
  // If already aligned or simple single equality without multiple = signs, return
  if (mathStr.includes('\\begin{aligned}')) return mathStr;

  // Check if string contains multiple '=' signs (chain of equalities)
  const equalsCount = (mathStr.match(/=/g) || []).length;
  if (equalsCount >= 2) {
    // Split by '=' and create aligned multiline
    const parts = mathStr.split('=').map(p => p.trim());
    if (parts.length >= 3) {
      let aligned = `\\begin{aligned} & ${parts[0]} \\\\ &= ${parts.slice(1).join(' \\\\ &= ')} \\end{aligned}`;
      return aligned;
    }
  }

  return mathStr;
}

// Update worked examples
if (Array.isArray(data.worked_examples)) {
  data.worked_examples.forEach(we => {
    if (Array.isArray(we.steps)) {
      we.steps.forEach(st => {
        if (st.calculation) {
          st.calculation = formatMultilineMath(st.calculation);
        }
      });
    }
  });
}

// Update problem pools
if (Array.isArray(data.question_types)) {
  data.question_types.forEach(qt => {
    if (Array.isArray(qt.pool)) {
      qt.pool.forEach(prob => {
        if (Array.isArray(prob.steps)) {
          prob.steps.forEach(st => {
            if (st.rubric_math) {
              st.rubric_math = formatMultilineMath(st.rubric_math);
            }
          });
        }
      });
    }
  });
}

fs.writeFileSync(ftaPath, JSON.stringify(data, null, 2), 'utf8');
console.log('Successfully formatted all long equations into clean multiline aligned equations!');
