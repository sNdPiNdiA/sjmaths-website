/**
 * topic-loader.js
 * 
 * Topic Loader & Registry service for the generic SJMaths mastery-learning system.
 * Dynamically resolves topic identifiers to data paths or remote endpoints.
 */

// Registry of known learning topics across classes, subjects, chapters
export const TOPIC_REGISTRY = Object.freeze({
  'cbse10-real-numbers-fta': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json'
  },

  'fta': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/fta/fta.json'
  },

  'cbse10-real-numbers-hcf-lcm': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.json'
  },

  'hcf-lcm': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/hcf-lcm/hcf-lcm.json'
  },

  'cbse10-real-numbers-proof-of-irrationality': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json'
  },

  'cbse10-real-numbers-irrationality': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json'
  },

  'proof-of-irrationality': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json'
  },

  'irrationality': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.js',
    fsPath: '../topics/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality/proof-of-irrationality.json'
  },

  'cbse10-polynomials-zeroes': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.js',
    fsPath: '../topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.json'
  },

  'zeroes': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.js',
    fsPath: '../topics/class-10/mathematics/chapter-2-polynomials/zeroes/zeroes.json'
  },

  'cbse10-polynomials-zeroes-coefficients': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.js',
    fsPath: '../topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.json'
  },

  'zeroes-coefficients': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.js',
    fsPath: '../topics/class-10/mathematics/chapter-2-polynomials/zeroes-coefficients/zeroes-coefficients.json'
  },

  'cbse10-linear-equations-graphical-consistency': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.json'
  },

  'graphical-consistency': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/graphical-consistency/graphical-consistency.json'
  },

  'cbse10-linear-equations-substitution-method': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.json'
  },

  'substitution-method': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/substitution-method/substitution-method.json'
  },

  'cbse10-linear-equations-elimination-method': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json'
  },

  'cbse10-linear-equations-elimination': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json'
  },

  'elimination': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json'
  },

  'elimination-method': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/elimination-method/elimination-method.json'
  },

  'cbse10-linear-equations-linear-word-problems': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.json'
  },

  'linear-word-problems': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.js',
    fsPath: '../topics/class-10/mathematics/chapter-3-linear-equations/linear-word-problems/linear-word-problems.json'
  },

  'cbse10-quadratic-equations-standard-form-roots': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.json'
  },

  'standard-form-roots': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/standard-form-roots/standard-form-roots.json'
  },

  'cbse10-quadratic-equations-solving-by-factorisation': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.json'
  },

  'solving-by-factorisation': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/solving-by-factorisation/solving-by-factorisation.json'
  },

  'cbse10-quadratic-equations-quadratic-formula': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.json'
  },

  'quadratic-formula': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-formula/quadratic-formula.json'
  },

  'cbse10-quadratic-equations-nature-of-roots': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.json'
  },

  'nature-of-roots': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/nature-of-roots/nature-of-roots.json'
  },

  'cbse10-quadratic-equations-quadratic-word-problems': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.json'
  },

  'quadratic-word-problems': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.js',
    fsPath: '../topics/class-10/mathematics/chapter-4-quadratic-equations/quadratic-word-problems/quadratic-word-problems.json'
  },

  'cbse10-arithmetic-progressions-ap-basics-nth-term': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.json'
  },

  'ap-basics-nth-term': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-basics-nth-term/ap-basics-nth-term.json'
  },

  'cbse10-arithmetic-progressions-nth-term-from-end': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.json'
  },

  'nth-term-from-end': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/nth-term-from-end/nth-term-from-end.json'
  },

  'cbse10-arithmetic-progressions-sum-of-n-terms': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.json'
  },

  'sum-of-n-terms': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/sum-of-n-terms/sum-of-n-terms.json'
  },

  'cbse10-arithmetic-progressions-relation-an-sn': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.json'
  },

  'relation-an-sn': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/relation-an-sn/relation-an-sn.json'
  },

  'cbse10-arithmetic-progressions-ap-applications': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.json'
  },

  'ap-applications': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.js',
    fsPath: '../topics/class-10/mathematics/chapter-5-arithmetic-progressions/ap-applications/ap-applications.json'
  },

  'cbse10-triangles-bpt-theorem': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.js',
    fsPath: '../topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.json'
  },

  'bpt-theorem': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.js',
    fsPath: '../topics/class-10/mathematics/chapter-6-triangles/bpt-theorem/bpt-theorem.json'
  },

  'cbse10-triangles-converse-bpt': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.js',
    fsPath: '../topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.json'
  },

  'converse-bpt': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.js',
    fsPath: '../topics/class-10/mathematics/chapter-6-triangles/converse-bpt/converse-bpt.json'
  },

  'cbse10-triangles-criteria-similarity': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.js',
    fsPath: '../topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.json'
  },

  'criteria-similarity': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.js',
    fsPath: '../topics/class-10/mathematics/chapter-6-triangles/criteria-similarity/criteria-similarity.json'
  },

  'cbse10-coordinate-geometry-distance-formula': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.json'
  },

  'distance-formula': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/distance-formula/distance-formula.json'
  },

  'cbse10-coordinate-geometry-section-formula-internal': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.json'
  },

  'section-formula-internal': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/section-formula-internal/section-formula-internal.json'
  },

  'cbse10-coordinate-geometry-midpoint-trisection': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.json'
  },

  'midpoint-trisection': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/midpoint-trisection/midpoint-trisection.json'
  },

  'cbse10-coordinate-geometry-finding-ratio': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.json'
  },

  'finding-ratio': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.js',
    fsPath: '../topics/class-10/mathematics/chapter-7-coordinate-geometry/finding-ratio/finding-ratio.json'
  },

  'cbse10-introduction-to-trigonometry-trig-ratios-right-triangle': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.js',
    fsPath: '../topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.json'
  },

  'trig-ratios-right-triangle': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.js',
    fsPath: '../topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trig-ratios-right-triangle/trig-ratios-right-triangle.json'
  },

  'cbse10-introduction-to-trigonometry-specific-angles-values': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.js',
    fsPath: '../topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.json'
  },

  'specific-angles-values': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.js',
    fsPath: '../topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/specific-angles-values/specific-angles-values.json'
  },

  'cbse10-introduction-to-trigonometry-trigonometric-identities': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.js',
    fsPath: '../topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.json'
  },

  'trigonometric-identities': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.js',
    fsPath: '../topics/class-10/mathematics/chapter-8-introduction-to-trigonometry/trigonometric-identities/trigonometric-identities.json'
  },

  'cbse10-applications-of-trigonometry-single-angle-heights-distances': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.js',
    fsPath: '../topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.json'
  },

  'single-angle-heights-distances': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.js',
    fsPath: '../topics/class-10/mathematics/chapter-9-applications-of-trigonometry/single-angle-heights-distances/single-angle-heights-distances.json'
  },

  'cbse10-applications-of-trigonometry-two-angles-heights-distances': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.js',
    fsPath: '../topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.json'
  },

  'two-angles-heights-distances': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.js',
    fsPath: '../topics/class-10/mathematics/chapter-9-applications-of-trigonometry/two-angles-heights-distances/two-angles-heights-distances.json'
  },

  'cbse10-circles-tangent-radius-theorem': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.js',
    fsPath: '../topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.json'
  },

  'tangent-radius-theorem': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.js',
    fsPath: '../topics/class-10/mathematics/chapter-10-circles/tangent-radius-theorem/tangent-radius-theorem.json'
  },

  'cbse10-circles-lengths-tangents-external-point': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.js',
    fsPath: '../topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.json'
  },

  'lengths-tangents-external-point': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.js',
    fsPath: '../topics/class-10/mathematics/chapter-10-circles/lengths-tangents-external-point/lengths-tangents-external-point.json'
  },

  'cbse10-circles-circle-tangent-proofs': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.js',
    fsPath: '../topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.json'
  },

  'circle-tangent-proofs': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.js',
    fsPath: '../topics/class-10/mathematics/chapter-10-circles/circle-tangent-proofs/circle-tangent-proofs.json'
  },

  'cbse10-areas-related-to-circles-sector-area-arc-length': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.js',
    fsPath: '../topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.json'
  },

  'sector-area-arc-length': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.js',
    fsPath: '../topics/class-10/mathematics/chapter-11-areas-related-to-circles/sector-area-arc-length/sector-area-arc-length.json'
  },

  'cbse10-areas-related-to-circles-segment-area': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.js',
    fsPath: '../topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.json'
  },

  'segment-area': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.js',
    fsPath: '../topics/class-10/mathematics/chapter-11-areas-related-to-circles/segment-area/segment-area.json'
  },

  'cbse10-surface-areas-volumes-combination-solids-surface-area': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.js',
    fsPath: '../topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.json'
  },

  'combination-solids-surface-area': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.js',
    fsPath: '../topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-surface-area/combination-solids-surface-area.json'
  },

  'cbse10-surface-areas-volumes-combination-solids-volume': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.js',
    fsPath: '../topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.json'
  },

  'combination-solids-volume': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.js',
    fsPath: '../topics/class-10/mathematics/chapter-12-surface-areas-volumes/combination-solids-volume/combination-solids-volume.json'
  },

  'cbse10-statistics-mean-direct-assumed': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.json'
  },

  'mean-direct-assumed': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/mean-direct-assumed/mean-direct-assumed.json'
  },

  'cbse10-statistics-mode-grouped-data': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.json'
  },

  'mode-grouped-data': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/mode-grouped-data/mode-grouped-data.json'
  },

  'cbse10-statistics-median-grouped-data': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.json'
  },

  'median-grouped-data': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/median-grouped-data/median-grouped-data.json'
  },

  'cbse10-statistics-empirical-relationship': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.json'
  },

  'empirical-relationship': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.js',
    fsPath: '../topics/class-10/mathematics/chapter-13-statistics/empirical-relationship/empirical-relationship.json'
  },

  'cbse10-probability-classical-probability': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.js',
    fsPath: '../topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.json'
  },

  'classical-probability': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.js',
    fsPath: '../topics/class-10/mathematics/chapter-14-probability/classical-probability/classical-probability.json'
  },

  'cbse10-probability-coins-dice-cards': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.js',
    fsPath: '../topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.json'
  },

  'coins-dice-cards': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.js',
    fsPath: '../topics/class-10/mathematics/chapter-14-probability/coins-dice-cards/coins-dice-cards.json'
  },

  'cbse10-probability-real-life-probability': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.js',
    fsPath: '../topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.json'
  },

  'real-life-probability': {
    dataPath: '/learning/topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.json',
    cssPath: '/learning/topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.css',
    jsPath: '/learning/topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.js',
    fsPath: '../topics/class-10/mathematics/chapter-14-probability/real-life-probability/real-life-probability.json'
  },

  'math-foundations-linear-equation-transposition': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.js',
    fsPath: '../topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.json'
  },

  'linear-equation-transposition': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.js',
    fsPath: '../topics/foundations/mathematics/algebra/linear-equation-transposition/linear-equation-transposition.json'
  },

  'factor-pairs': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.js',
    fsPath: '../topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.json'
  },

  'math-foundations-factor-pairs': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.js',
    fsPath: '../topics/foundations/mathematics/algebra/factor-pairs/factor-pairs.json'
  },

  'prep-factors-multiples-divisibility': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.json'
  },

  'math-foundations-prep-factors-multiples-divisibility': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-factors-multiples-divisibility/prep-factors-multiples-divisibility.json'
  },

  'prep-fractions-ratios-percent': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.json'
  },

  'math-foundations-prep-fractions-ratios-percent': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-fractions-ratios-percent/prep-fractions-ratios-percent.json'
  },

  'prep-squares-roots-surds': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.json'
  },

  'math-foundations-prep-squares-roots-surds': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-squares-roots-surds/prep-squares-roots-surds.json'
  },

  'prep-exponent-laws': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.json'
  },

  'math-foundations-prep-exponent-laws': {
    dataPath: '/learning/topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.json',
    cssPath: '/learning/topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.css',
    jsPath: '/learning/topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.js',
    fsPath: '../topics/foundations/mathematics/arithmetic/prep-exponent-laws/prep-exponent-laws.json'
  },

  'prep-linear-equation-one-variable': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.js',
    fsPath: '../topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.json'
  },

  'math-foundations-prep-linear-equation-one-variable': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.js',
    fsPath: '../topics/foundations/mathematics/algebra/prep-linear-equation-one-variable/prep-linear-equation-one-variable.json'
  },

  'prep-algebraic-identities-manipulation': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.js',
    fsPath: '../topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.json'
  },

  'math-foundations-prep-algebraic-identities-manipulation': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.js',
    fsPath: '../topics/foundations/mathematics/algebra/prep-algebraic-identities-manipulation/prep-algebraic-identities-manipulation.json'
  },

  'prep-word-problem-translation': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.js',
    fsPath: '../topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.json'
  },

  'math-foundations-prep-word-problem-translation': {
    dataPath: '/learning/topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.json',
    cssPath: '/learning/topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.css',
    jsPath: '/learning/topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.js',
    fsPath: '../topics/foundations/mathematics/algebra/prep-word-problem-translation/prep-word-problem-translation.json'
  },

  'prep-cartesian-plane-fluency': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.json'
  },

  'math-foundations-prep-cartesian-plane-fluency': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-cartesian-plane-fluency/prep-cartesian-plane-fluency.json'
  },

  'prep-pythagoras-right-triangle': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.json'
  },

  'math-foundations-prep-pythagoras-right-triangle': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-pythagoras-right-triangle/prep-pythagoras-right-triangle.json'
  },

  'prep-parallel-line-angle-facts': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.json'
  },

  'math-foundations-prep-parallel-line-angle-facts': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-parallel-line-angle-facts/prep-parallel-line-angle-facts.json'
  },

  'prep-geometry-ratio-similarity': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.json'
  },

  'math-foundations-prep-geometry-ratio-similarity': {
    dataPath: '/learning/topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.json',
    cssPath: '/learning/topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.css',
    jsPath: '/learning/topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.js',
    fsPath: '../topics/foundations/mathematics/geometry/prep-geometry-ratio-similarity/prep-geometry-ratio-similarity.json'
  },

  'prep-circle-anatomy-sector-fractions': {
    dataPath: '/learning/topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.json',
    cssPath: '/learning/topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.css',
    jsPath: '/learning/topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.js',
    fsPath: '../topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.json'
  },

  'math-foundations-prep-circle-anatomy-sector-fractions': {
    dataPath: '/learning/topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.json',
    cssPath: '/learning/topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.css',
    jsPath: '/learning/topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.js',
    fsPath: '../topics/foundations/mathematics/measurement/prep-circle-anatomy-sector-fractions/prep-circle-anatomy-sector-fractions.json'
  },

  'prep-solids-recap-unit-conversions': {
    dataPath: '/learning/topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.json',
    cssPath: '/learning/topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.css',
    jsPath: '/learning/topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.js',
    fsPath: '../topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.json'
  },

  'math-foundations-prep-solids-recap-unit-conversions': {
    dataPath: '/learning/topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.json',
    cssPath: '/learning/topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.css',
    jsPath: '/learning/topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.js',
    fsPath: '../topics/foundations/mathematics/measurement/prep-solids-recap-unit-conversions/prep-solids-recap-unit-conversions.json'
  },

  'prep-data-tables-averages': {
    dataPath: '/learning/topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.json',
    cssPath: '/learning/topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.css',
    jsPath: '/learning/topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.js',
    fsPath: '../topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.json'
  },

  'math-foundations-prep-data-tables-averages': {
    dataPath: '/learning/topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.json',
    cssPath: '/learning/topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.css',
    jsPath: '/learning/topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.js',
    fsPath: '../topics/foundations/mathematics/measurement/prep-data-tables-averages/prep-data-tables-averages.json'
  },

  'prep-proof-format-congruence': {
    dataPath: '/learning/topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.json',
    cssPath: '/learning/topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.css',
    jsPath: '/learning/topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.js',
    fsPath: '../topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.json'
  },

  'math-foundations-prep-proof-format-congruence': {
    dataPath: '/learning/topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.json',
    cssPath: '/learning/topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.css',
    jsPath: '/learning/topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.js',
    fsPath: '../topics/foundations/mathematics/proof/prep-proof-format-congruence/prep-proof-format-congruence.json'
  },

  'prep-counting-chance-intuition': {
    dataPath: '/learning/topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.json',
    cssPath: '/learning/topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.css',
    jsPath: '/learning/topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.js',
    fsPath: '../topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.json'
  },

  'math-foundations-prep-counting-chance-intuition': {
    dataPath: '/learning/topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.json',
    cssPath: '/learning/topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.css',
    jsPath: '/learning/topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.js',
    fsPath: '../topics/foundations/mathematics/proof/prep-counting-chance-intuition/prep-counting-chance-intuition.json'
  }
});

/**
 * Normalizes a topic identifier string.
 */
export function normalizeTopicId(rawId) {
  if (!rawId || typeof rawId !== 'string') return '';
  return rawId.trim().toLowerCase();
}

/**
 * Resolves a topic ID to its full metadata entry from the registry.
 */
export function resolveTopic(topicId) {
  const normalized = normalizeTopicId(topicId);
  if (TOPIC_REGISTRY[normalized]) return TOPIC_REGISTRY[normalized];

  // Try stripping or adding prefixes
  const stripped = normalized.replace(/^(?:cbse10-|math-foundations-|prep-)/, '');
  for (const [key, val] of Object.entries(TOPIC_REGISTRY)) {
    if (key.includes(stripped) || stripped.includes(key)) {
      return val;
    }
  }

  // Graceful fallback to default FTA topic rather than null
  return TOPIC_REGISTRY['cbse10-real-numbers-fta'] || null;
}

/**
 * Resolves the requested topic ID from URL search parameters or hash.
 */
export function getRequestedTopicId(defaultTopic = 'cbse10-real-numbers-fta') {
  if (typeof window === 'undefined') return defaultTopic;
  const params = new URLSearchParams(window.location.search);
  const topicFromQuery = params.get('topic') || params.get('id') || params.get('slug');
  if (topicFromQuery) {
    return normalizeTopicId(topicFromQuery);
  }
  const hash = window.location.hash.replace(/^#\/?/, '').trim();
  if (hash && hash.length > 2 && !hash.startsWith('concept_')) {
    return normalizeTopicId(hash);
  }
  return defaultTopic;
}

export function resolveTopicAssetPaths(topicId) {
  return resolveTopic(topicId);
}

export function resolveTopicDataPath(topicId) {
  const meta = resolveTopic(topicId);
  return meta ? meta.dataPath : null;
}

/**
 * Fetches and returns the topic JSON data for a given topic ID.
 */
export async function loadTopicData(topicId) {
  const topicMeta = resolveTopic(topicId);
  
  if (!topicMeta) {
    throw new Error(`Topic "${topicId}" is not registered in the TOPIC_REGISTRY.`);
  }

  // 1. In browser environments: Fetch via dataPath HTTP URL
  if (typeof window !== 'undefined' && typeof window.fetch === 'function') {
    const response = await fetch(topicMeta.dataPath);
    if (!response.ok) {
      throw new Error(`Failed to fetch topic data from "${topicMeta.dataPath}": HTTP ${response.status} ${response.statusText}`);
    }
    return await response.json();
  }

  // 2. In Node.js environments (unit tests / server build tools): Read from file system
  if (typeof process !== 'undefined' && process.versions && process.versions.node) {
    const { promises: fs } = await import('fs');
    const path = await import('path');
    const { fileURLToPath } = await import('url');

    const __dirname = path.dirname(fileURLToPath(import.meta.url));
    const fullFsPath = path.resolve(__dirname, topicMeta.fsPath);
    
    const fileContent = await fs.readFile(fullFsPath, 'utf8');
    return JSON.parse(fileContent);
  }

  throw new Error('Unsupported runtime environment for loadTopicData.');
}

/**
 * Injects topic-specific CSS styles if they exist.
 */
export function injectTopicStyles(topicId) {
  if (typeof document === 'undefined') return;

  const topicMeta = resolveTopic(topicId);
  if (!topicMeta || !topicMeta.cssPath) return;

  const existing = document.getElementById(`topic-style-${normalizeTopicId(topicId)}`);
  if (existing) return;

  const link = document.createElement('link');
  link.id = `topic-style-${normalizeTopicId(topicId)}`;
  link.rel = 'stylesheet';
  link.href = topicMeta.cssPath;
  document.head.appendChild(link);
}
