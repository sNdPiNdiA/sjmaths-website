const ENTITY_LATEX = {
  '&alpha;': '\\alpha', '&beta;': '\\beta', '&gamma;': '\\gamma', '&delta;': '\\delta',
  '&Delta;': '\\Delta', '&epsilon;': '\\epsilon', '&eta;': '\\eta', '&hbar;': '\\hbar',
  '&chi;': '\\chi', '&lambda;': '\\lambda', '&mu;': '\\mu', '&nu;': '\\nu',
  '&omega;': '\\omega', '&Omega;': '\\Omega', '&phi;': '\\phi', '&Phi;': '\\Phi',
  '&pi;': '\\pi', '&psi;': '\\psi', '&Psi;': '\\Psi', '&rho;': '\\rho',
  '&sigma;': '\\sigma', '&Sigma;': '\\Sigma', '&tau;': '\\tau', '&theta;': '\\theta', '&xi;': '\\xi',
  '&times;': '\\times ', '&middot;': '\\cdot ', '&approx;': '\\approx ', '&sqrt;': '\\sqrt{}',
  '&prop;': '\\propto ', '&propto;': '\\propto ', '&part;': '\\partial ',
  '&partial;': '\\partial ', '&nabla;': '\\nabla ', '&sum;': '\\sum ',
  '&int;': '\\int ', '&oint;': '\\oint ', '&infin;': '\\infty ', '&infty;': '\\infty ',
  '&le;': '\\le ', '&ge;': '\\ge ', '&ne;': '\\ne ', '&plusmn;': '\\pm ',
  '&rArr;': '\\Rightarrow ', '&implies;': '\\implies ', '&perp;': '\\perp ',
  '&sim;': '\\sim ', '&asymp;': '\\asymp ', '&radic;': '\\sqrt{}',
  '&icirc;': '\\hat{i}', '&jhat;': '\\hat{j}', '&khat;': '\\hat{k}',
  '&langle;': '\\langle ', '&rangle;': '\\rangle ', '&zbar;': '\\bar{z}'
};

const PLAIN_LATEX_NAMES = [
  'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'eta', 'chi', 'lambda', 'mu', 'nu',
  'omega', 'phi', 'pi', 'rho', 'sigma', 'tau', 'theta', 'xi', 'psi', 'sqrt', 'nabla',
  'partial', 'sum', 'int', 'infty', 'times', 'cdot', 'approx', 'propto', 'sin', 'cos',
  'tan', 'log', 'ln', 'lim', 'left', 'right', 'text', 'mathrm', 'mathbf', 'langle', 'rangle', 'dfrac', 'varepsilon', 'vec'
];

/** Recover LaTeX commands that were interpreted as JSON escape sequences. */
export function repairLatexControls(value) {
  return String(value ?? '')
    .replace(/\u0008(?=[A-Za-z])/g, '\\b')
    .replace(/\u0009(?=[A-Za-z])/g, '\\t')
    .replace(/\u000B(?=[A-Za-z])/g, '\\v')
    .replace(/\u000C(?=[A-Za-z])/g, '\\f')
    .replace(/\u000D(?=[A-Za-z])/g, '\\r')
    .replace(/\n(?=(?:abla|u|eq|ot|mid|le|ge|in|not|partial|pm)\b)/g, '\\n')
    .replace(/[\u0008-\u000D]/g, ' ');
}

export function repairPhysicsData(value) {
  if (typeof value === 'string') return normalizeInlineMath(value);
  if (Array.isArray(value)) return value.map(repairPhysicsData);
  if (value && typeof value === 'object') {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, repairPhysicsData(item)]));
  }
  return value;
}

export function decodeEmbeddedTags(value) {
  return repairLatexControls(value).replace(/&lt;(\/?)(sub|sup|br)&gt;/gi, '<$1$2>');
}

export function normalizeInlineMath(value) {
  return repairLatexControls(value)
    .replace(/\u0348/g, '')
    .replace(/([A-Za-z])\$([A-Za-z])/g, '$1$2')
    .replace(/\^\$/g, '^')
    .replace(/\^-\^([0-9])\^([0-9])/g, '^(-$1$2)')
    .replace(/\^\(-([0-9]+)\)/g, (_, digits) => '^{' + '-' + digits + '}')
    .replace(/\^-\^([0-9]+)/g, (_, digits) => '^{' + '-' + digits + '}')
    .replace(/\\\\(?=[A-Za-z])/g, '\\')
    .replace(/\${2,}/g, '$');
}

export function mathSource(value) {
  let text = decodeEmbeddedTags(value)
    .replace(/\\\\(?=[A-Za-z])/g, '\\')
    .replace(/&amp;/gi, '&')
    .replace(/&frac(?=\{)/gi, '\\frac')
    .replace(/&sup-;&sup([0-9]);&sup([0-9]);/gi, '^(-$1$2)')
    .replace(/&sup-;&sup([A-Za-z0-9]+);/gi, '^(-$1)')
    .replace(/&sup-([A-Za-z0-9]+);/gi, '^(-$1)')
    .replace(/&sup-;(?:(?:\^)?\{?([0-9]+)\}?)/gi, '^(-$1)')
    .replace(/&sub(?:script)?([A-Za-z0-9]+);/gi, '_{$1}')
    .replace(/&sup([A-Za-z0-9]+);/gi, '^{$1}')
    .replace(/(?<!\\)jleft/g, 'j\\left')
    .replace(/\\left(?!\s*[([{|.\\])/g, '')
    .replace(/\\right(?!\s*[)\]}|.\\])/g, '')
    .replace(/(?<!\\)lnleft/g, '\\ln\\left')
    .replace(/([A-Za-z])left/g, '$1\\left')
    .replace(/(?<![_A-Za-z])([ijkn])\^(?=\s|[),.;+*=([\\]|$)/g, '\\hat{$1}')
    .replace(/\bv_d_n\b/g, 'v_{d_n}')
    .replace(/\bv_d_p\b/g, 'v_{d_p}')
    .replace(/\\right\s*\(/g, '\\text{right }(')
    .replace(/\\frac\{\\sqrt\{([^{}]+)\}\{([^{}]+)\}\}/g, '\\frac{\\sqrt{$1}}{$2}')
    .replace(/\\frac\{\\sqrt\{([^{}]+)\}\{([^{}]+)\}/g, '\\frac{\\sqrt{$1}}{$2}')
    .replace(/_\{([^{}]+)\}_\{([^{}]+)\}/g, '_{$1$2}')
    .replace(/_([A-Za-z0-9])_\{([^{}]+)\}/g, '_{$1$2}')
    .replace(/\\text\{([^{}]*)\^\{(-?[0-9]+)\}([^{}]*)\}/g, (_, before, exponent, after) => '\\text{' + before + '}^{' + exponent + '}\\text{' + after + '}')
    .replace(/\\text\{([^{}]*)\^(-?[0-9]+)([^{}]*)\}/g, (_, before, exponent, after) => '\\text{' + before + '}^{' + exponent + '}\\text{' + after + '}')
    .replace(/\\right-circularly/gi, '\\text{right-circularly}')
    .replace(/\\right-hand/gi, '\\text{right-hand}')
    .replace(/\\left\s+and\s+\\right\s+gaps/gi, '\\text{left and right gaps}')
    .replace(/\\,\s*(?=\^)/g, '')
    .replace(/\\\./g, '')
    .replace(/\\'/g, '')
    .replace(/\\text\{\$([^}]*)\}/g, '\\text{$1}')
    .replace(/<sub>(.*?)<\/sub>/gi, '_{$1}')
    .replace(/<sup>(.*?)<\/sup>/gi, '^{$1}')
    .replace(/&lt;/gi, '\\langle ')
    .replace(/&gt;/gi, ' \\rangle');
  text = text.replaceAll('/left(', '');
  for (const [entity, command] of Object.entries(ENTITY_LATEX)) text = text.replaceAll(entity, command);
  text = text.replace(/\\sqrt\{\}\s*\(([^()]*)\)/g, '\\sqrt{$1}');
  text = text.replace(/\\sqrt\{\}\s*\[([^\]]*)\]/g, '\\sqrt{$1}');
  text = text.replace(/([A-Za-z])_([A-Za-z])_([A-Za-z])/g, '$1_{$2_$3}');
  const names = new RegExp(`(?<!\\\\)\\b(${PLAIN_LATEX_NAMES.join('|')})(?=\\b|_)`, 'gi');
  text = text.replace(names, (_, name) => `\\${name.toLowerCase()}`);
  text = text.replace(/\\vec\\'/g, '\\vec');
  text = text.replace(/\\lnleft/g, '\\ln\\left');
  text = text.replace(/\^\{([^{}]+)\}\^\{([^{}]+)\}/g, '^{$1$2}');
  text = text.replace(/\^\(-([0-9])\)\^\{([0-9])\}/g, '^(-$1$2)');
  text = text.replace(/\^\(-([0-9]+)\)/g, (_, digits) => '^{' + '-' + digits + '}');
  text = text.replace(/\^-\^([0-9]+)/g, (_, digits) => '^{' + '-' + digits + '}');
  text = text.replace(/\\right-(circularly|hand)/gi, (_, word) => '\\text{right-' + word + '}');
  text = text.replaceAll('/left(', '');
  text = text.replace(/__+/g, '_');
  text = text.replace(/\\text\{([^{}]*)\^\{(-?[0-9]+)\}([^{}]*)\}/g, (_, before, exponent, after) => '\\text{' + before + '}^{' + exponent + '}\\text{' + after + '}');
  text = text.replace(/\\text\{([^{}]*)\^(-?[0-9]+)([^{}]*)\}/g, (_, before, exponent, after) => '\\text{' + before + '}^{' + exponent + '}\\text{' + after + '}');
  text = text.replace(/\^\{(-?[0-9]+)\}\^\\circ/g, (_, exponent) => '^{' + exponent + '}\\,\\text{°}');
  text = text.replace(/b_n\s*=\s*\\begin\{cases\}[\s\S]*?\\end\{cases\}/g, 'b_n = \\frac{4V}{n\\pi} \\text{ for odd } n,\\quad b_n = 0 \\text{ for even } n');
  text = text.replace(/b_n\s*=\s*\\begin\{cases\}[\s\S]*$/g, 'b_n = \\frac{4V}{n\\pi} \\text{ for odd } n,\\quad b_n = 0 \\text{ for even } n');
  let depth = 0;
  let balanced = '';
  for (const character of text) {
    if (character === '{') depth += 1;
    if (character === '}') {
      if (depth === 0) continue;
      depth -= 1;
    }
    balanced += character;
  }
  return balanced + '}'.repeat(depth);
}

export function mathEntityMap() {
  return ENTITY_LATEX;
}
