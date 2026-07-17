#!/usr/bin/env node
/**
 * gen_applied_math_content.js
 * ──────────────────────────────────────────────────────────────────────────
 * Uses Gemini model rotation to spread quota across 3 models:
 *   Topics  1-20:  gemini-2.5-flash-lite
 *   Topics 21-40:  gemini-3.5-flash
 *   Topics 41-74:  gemini-3.1-flash-lite
 *
 * Usage:
 *   node scripts/gen_applied_math_content.js <GEMINI_API_KEY> [--only <dir>]
 *
 * Options:
 *   --only <dir>   Process only one specific microtopic directory (for testing)
 *   --resume       Skip topics where index.html already has >400 lines
 * ──────────────────────────────────────────────────────────────────────────
 */

'use strict';

const fs   = require('fs');
const path = require('path');
const https = require('https');

// ── Config ────────────────────────────────────────────────────────────────
const BASE = path.join(__dirname, '..', 'class-11-applied-mathematics');
const args = process.argv.slice(2);
const API_KEY = args[0] || process.env.GEMINI_API_KEY;
const ONLY    = args.includes('--only')   ? args[args.indexOf('--only')   + 1] : null;
const RESUME  = args.includes('--resume');

// Single model: gemini-3.1-flash-lite (fresh quota)
const SINGLE_MODEL = 'gemini-3.1-flash-lite';

function getModel(_callIndex) {
  return SINGLE_MODEL;
}

if (!API_KEY) {
  console.error('❌  No API key found. Usage: node scripts/gen_applied_math_content.js <GEMINI_API_KEY>');
  process.exit(1);
}

// ── All 74 microtopics (Units 2–7) ───────────────────────────────────────
const MICROTOPICS = [
  // ── UNIT 2: Algebra ──────────────────────────────────────────────────
  { dir: '2-1-introduction-to-sets/set-as-well-defined-collection-of-objects',
    title: 'Set as Well-Defined Collection of Objects',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Introduction to Sets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-1-introduction-to-sets/different-types-of-sets-on-the-basis-of-number-of-elements-in-the-set',
    title: 'Different Types of Sets on the Basis of Number of Elements',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Introduction to Sets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-1-introduction-to-sets/differentiate-between-equal-set-and-equivalent-set',
    title: 'Difference Between Equal Set and Equivalent Set',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Introduction to Sets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-1-introduction-to-sets/representation-of-a-set-in-roster-form-and-set-builder-form',
    title: 'Representation of a Set: Roster Form and Set-Builder Form',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Introduction to Sets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-2-subsets/subsets',
    title: 'Subsets',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Subsets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-2-subsets/universal-set',
    title: 'Universal Set',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Subsets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-2-subsets/power-set-and-its-elements',
    title: 'Power Set and Its Elements',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Subsets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-2-subsets/subset-of-real-numbers-as-intervals',
    title: 'Subset of Real Numbers as Intervals',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Subsets',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-3-venn-diagrams/concept-of-venn-diagram-to-understand-the-relationship-between-sets',
    title: 'Concept of Venn Diagram to Understand the Relationship Between Sets',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Venn Diagrams',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-3-venn-diagrams/operations-on-sets',
    title: 'Operations on Sets',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Venn Diagrams',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-3-venn-diagrams/problems-using-venn-diagram',
    title: 'Problems Using Venn Diagram',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Venn Diagrams',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-4-ordered-pairs/significance-of-specific-arrangement-of-elements-in-a-pair',
    title: 'Significance of Specific Arrangement of Elements in a Pair',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Ordered Pairs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-4-ordered-pairs/cartesian-product-of-two-sets',
    title: 'Cartesian Product of Two Sets',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Ordered Pairs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-5-relations/domain-and-range-of-a-relation',
    title: 'Domain and Range of a Relation',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Relations',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-5-relations/expressing-relation-as-a-subset-of-cartesian-product',
    title: 'Expressing a Relation as a Subset of Cartesian Product',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Relations',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-6-mathematical-logic/logical-problems-involving-odd-man-out-syllogism-blood-relation-and-coding-decoding',
    title: 'Logical Problems: Odd Man Out, Syllogism, Blood Relations & Coding-Decoding',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Mathematical Logic',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-7-sequence-and-series/differentiate-between-sequence-and-series',
    title: 'Differentiate Between Sequence and Series',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Sequence and Series',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-8-arithmetic-progression/arithmetic-mean-am-of-two-positive-numbers',
    title: 'Arithmetic Mean (AM) of Two Positive Numbers',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Arithmetic Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/introduction-of-geometric-progression-gp',
    title: 'Introduction to Geometric Progression (GP)',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/nth-term-of-a-gp',
    title: 'nth Term of a GP',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/sum-of-n-terms-and-sum-of-infinite-terms-of-a-gp',
    title: 'Sum of n Terms and Sum of Infinite Terms of a GP',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/geometric-mean-gm-of-two-positive-numbers',
    title: 'Geometric Mean (GM) of Two Positive Numbers',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/relation-between-am-and-gm-and-related-problems',
    title: 'Relation Between AM and GM and Related Problems',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/problems-based-on-applications-of-gp',
    title: 'Problems Based on Applications of GP',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '2-9-geometric-progression/application-problems-based-on-ap-and-gp',
    title: 'Application Problems Based on AP and GP',
    unit: '2', unitName: 'Algebra',
    topicGroup: 'Geometric Progression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  // ── UNIT 3: Calculus ─────────────────────────────────────────────────
  { dir: '3-1-functions-and-their-graphs/dependent-and-independent-variables',
    title: 'Dependent and Independent Variables',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Functions and Their Graphs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-1-functions-and-their-graphs/definition-of-function-using-dependent-and-independent-variable',
    title: 'Definition of Function Using Dependent and Independent Variable',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Functions and Their Graphs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-1-functions-and-their-graphs/domain-range-and-codomain-of-a-given-function',
    title: 'Domain, Range and Codomain of a Given Function',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Functions and Their Graphs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-1-functions-and-their-graphs/types-of-functions',
    title: 'Types of Functions',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Functions and Their Graphs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-1-functions-and-their-graphs/graphical-representation-of-function',
    title: 'Graphical Representation of a Function',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Functions and Their Graphs',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-2-limits-and-continuity/limit-of-a-function',
    title: 'Limit of a Function',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Limits and Continuity',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-2-limits-and-continuity/continuity-of-a-function',
    title: 'Continuity of a Function',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Limits and Continuity',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-3-differentiation/finding-the-derivative-of-the-functions',
    title: 'Finding the Derivative of Functions',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Differentiation',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-3-differentiation/instantaneous-rate-of-change',
    title: 'Instantaneous Rate of Change',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Differentiation',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-4-algebra-of-derivatives/differentiation-of-addition-subtraction-multiplication-and-division-of-two-or-more-functions',
    title: 'Differentiation of Sum, Difference, Product and Quotient of Functions',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Algebra of Derivatives',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '3-4-algebra-of-derivatives/differentiation-of-a-function-of-a-function',
    title: 'Differentiation of a Function of a Function (Chain Rule)',
    unit: '3', unitName: 'Calculus',
    topicGroup: 'Algebra of Derivatives',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  // ── UNIT 4: Combinatorics & Probability ──────────────────────────────
  { dir: '4-1-combinatorics/factorial-of-a-number',
    title: 'Factorial of a Number',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-1-combinatorics/fundamental-principle-of-counting',
    title: 'Fundamental Principle of Counting',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-1-combinatorics/concept-of-permutation',
    title: 'Concept of Permutation',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-1-combinatorics/simple-problems-based-on-permutations',
    title: 'Simple Problems Based on Permutations',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-1-combinatorics/define-combination',
    title: 'Define Combination',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-1-combinatorics/problems-based-on-combinations',
    title: 'Problems Based on Combinations',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-1-combinatorics/difference-between-permutation-and-combination',
    title: 'Difference Between Permutation and Combination',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Combinatorics',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-2-probability/random-experiment-and-sample-space-with-suitable-examples',
    title: 'Random Experiment and Sample Space with Suitable Examples',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Probability',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-2-probability/event-and-its-types',
    title: 'Event and Its Types',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Probability',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-2-probability/concept-of-probability',
    title: 'Concept of Probability',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Probability',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-2-probability/concept-of-conditional-probability',
    title: 'Concept of Conditional Probability',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Probability',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '4-2-probability/problems-based-on-calculating-probabilities-in-real-life-situations',
    title: 'Problems Based on Calculating Probabilities in Real Life Situations',
    unit: '4', unitName: 'Combinatorics and Probability',
    topicGroup: 'Probability',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  // ── UNIT 5: Statistics ───────────────────────────────────────────────
  { dir: '5-1-measures-of-dispersion/meaning-of-dispersion-in-a-data-set',
    title: 'Meaning of Dispersion in a Data Set',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Measures of Dispersion',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-1-measures-of-dispersion/range-mean-deviation-standard-deviation-and-variance',
    title: 'Range, Mean Deviation, Standard Deviation and Variance',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Measures of Dispersion',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-2-percentiles/concept-of-percentile-rank',
    title: 'Concept of Percentile Rank',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Percentiles',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-2-percentiles/calculate-and-interpret-percentile-rank-of-scores-in-a-given-ungrouped-data-set',
    title: 'Calculate and Interpret Percentile Rank of Scores in Ungrouped Data',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Percentiles',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-3-correlation/concept-of-correlation',
    title: 'Concept of Correlation',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Correlation',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-3-correlation/karl-pearsons-coefficient-of-correlation-for-ungrouped-data',
    title: "Karl Pearson's Coefficient of Correlation for Ungrouped Data",
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Correlation',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-3-correlation/spearmans-rank-correlation-for-ungrouped-data',
    title: "Spearman's Rank Correlation for Ungrouped Data",
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Correlation',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-4-regression/concept-of-regression-analysis',
    title: 'Concept of Regression Analysis',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Regression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-4-regression/dependent-and-independent-variables',
    title: 'Dependent and Independent Variables in Regression',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Regression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-4-regression/regression-equations',
    title: 'Regression Equations',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Regression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-4-regression/regression-coefficients',
    title: 'Regression Coefficients',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Regression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '5-4-regression/properties-of-regression-equations',
    title: 'Properties of Regression Equations',
    unit: '5', unitName: 'Statistics',
    topicGroup: 'Regression',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  // ── UNIT 6: Financial Mathematics ────────────────────────────────────
  { dir: '6-1-interest-and-interest-rates/concept-of-interest-rates',
    title: 'Concept of Interest Rates',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Interest and Interest Rates',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-1-interest-and-interest-rates/concept-of-effective-rate-of-interest',
    title: 'Concept of Effective Rate of Interest',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Interest and Interest Rates',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-1-interest-and-interest-rates/comparison-between-nominal-interest-rate-effective-rate-and-real-interest-rate',
    title: 'Comparison: Nominal, Effective and Real Interest Rate',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Interest and Interest Rates',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-1-interest-and-interest-rates/practical-applications-of-interest-rate-wrt-simple-and-compound-interest',
    title: 'Practical Applications of Simple and Compound Interest',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Interest and Interest Rates',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-2-annuities/meaning-of-immediate-annuity-annuity-due-and-deferred-annuity',
    title: 'Meaning of Immediate Annuity, Annuity Due and Deferred Annuity',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Annuities',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-2-annuities/concept-of-annuity-in-real-life-situations',
    title: 'Concept of Annuity in Real Life Situations',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Annuities',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-2-annuities/future-and-present-value-of-ordinary-annuity-annuity-due-up-to-3-period',
    title: 'Future and Present Value of Ordinary Annuity and Annuity Due (up to 3 periods)',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Annuities',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-3-taxes-and-utility-bills/concept-of-income-tax-and-gst-wrt-tax-new-tax-guidelines',
    title: 'Concept of Income Tax and GST (New Tax Guidelines)',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Taxes and Utility Bills',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '6-3-taxes-and-utility-bills/utility-bills-and-its-various-types-electricity-water-and-png-bills',
    title: 'Utility Bills: Electricity, Water and PNG Bills',
    unit: '6', unitName: 'Financial Mathematics',
    topicGroup: 'Taxes and Utility Bills',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  // ── UNIT 7: Coordinate Geometry ──────────────────────────────────────
  { dir: '7-1-straight-lines/concept-of-slope-of-a-line',
    title: 'Concept of Slope of a Line',
    unit: '7', unitName: 'Coordinate Geometry',
    topicGroup: 'Straight Lines',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '7-1-straight-lines/various-forms-of-equation-of-line',
    title: 'Various Forms of Equation of a Line',
    unit: '7', unitName: 'Coordinate Geometry',
    topicGroup: 'Straight Lines',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '7-2-circles-and-parabola/different-form-of-equations-of-a-circle',
    title: 'Different Forms of Equations of a Circle',
    unit: '7', unitName: 'Coordinate Geometry',
    topicGroup: 'Circles and Parabola',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '7-2-circles-and-parabola/determination-of-the-equations-of-circle-and-parabola-as-a-locus-of-a-point-in-a-plane-under-certain-conditions',
    title: 'Equations of Circle and Parabola as Locus of a Point',
    unit: '7', unitName: 'Coordinate Geometry',
    topicGroup: 'Circles and Parabola',
    curriculum: 'CBSE Class 11 Applied Mathematics' },

  { dir: '7-2-circles-and-parabola/solve-problems-based-on-applications-of-circle',
    title: 'Problems Based on Applications of Circle',
    unit: '7', unitName: 'Coordinate Geometry',
    topicGroup: 'Circles and Parabola',
    curriculum: 'CBSE Class 11 Applied Mathematics' },
];

// ── Gemini API call ────────────────────────────────────────────────────────
function callGemini(prompt, model = MODEL) {
  return new Promise((resolve, reject) => {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${API_KEY}`;
    const body = JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: {
        responseMimeType: 'application/json',
        temperature: 0.3,
        maxOutputTokens: 8192
      }
    });

    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };

    const req = https.request(url, options, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(data);
          if (parsed.error) return reject(new Error(parsed.error.message));
          let text = parsed.candidates?.[0]?.content?.parts?.[0]?.text;
          if (!text) {
            const err = parsed.error;
            return reject(new Error(err ? err.message : 'Empty response from Gemini'));
          }
          // Fix common JSON escaping issues
          text = text.replace(/\\(?!["\\bfnrtu/])/g, '\\\\');
          // Strip markdown code block wrappers if present
          text = text.replace(/^```json\s*/i, '').replace(/```\s*$/i, '').trim();
          resolve(JSON.parse(text));
        } catch (e) {
          reject(new Error('Failed to parse Gemini response: ' + e.message));
        }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}
// ── Build structured prompt ────────────────────────────────────────────────
function buildPrompt(topic) {
  return `
You are a senior CBSE Class 11 Applied Mathematics author writing an NCERT-style textbook exercise set.
Generate comprehensive, textbook-quality educational content for the following microtopic:

Topic: "${topic.title}"
Unit: ${topic.unit} – ${topic.unitName}
Topic Group: ${topic.topicGroup}
Curriculum: ${topic.curriculum}

Return ONLY a valid JSON object with EXACTLY this structure (no markdown, no code block, no LaTeX backslash notation — use Unicode math symbols: ², ³, ₁, ₂, ∈, ∉, ⊂, ⊆, ∪, ∩, ∞, √, ≤, ≥, ≠, →, ⟹, π, σ, μ, Σ, α, β, γ):

{
  "seoDescription": "A compelling 150-character meta description for this topic",

  "theory": [
    {
      "heading": "...",
      "body": "Clear textbook-style explanation (3-5 sentences) with precise mathematical language and real examples. Mention specific objects, numbers, or formulas.",
      "formula": "Key formula with Unicode symbols. e.g.  aₙ = a·rⁿ⁻¹  or  σ² = Σ(xᵢ − x̄)²/n  or  P(A|B) = P(A∩B)/P(B)",
      "exampleTitle": "Solved Example: Find / Calculate / Verify / Show that ...",
      "exampleSolution": "Step 1: ...<br>Step 2: ...<br>Step 3: ...<br>Answer: ... (use actual numbers and Unicode math)"
    }
  ],

  "mcqs": [
    {
      "difficulty": "easy|medium|hard|very hard",
      "question": "MUST use specific numbers/expressions. e.g. 'If A = {2, 4, 6, 8}, find n(A).' NOT vague definition questions. Computation or application required.",
      "A": "specific numeric/expression option",
      "B": "specific numeric/expression option",
      "C": "specific numeric/expression option",
      "D": "specific numeric/expression option",
      "answer": "A|B|C|D",
      "solution": "Show the calculation/reasoning step by step in 2-3 lines."
    }
  ],

  "assertionReason": [
    {
      "assertion": "A precise mathematical statement about ${topic.title} (use specific example or formula)",
      "reason": "The mathematical reason/theorem that explains/contradicts the assertion",
      "answer": "A|B|C|D",
      "solution": "Detailed explanation of why this option is correct."
    }
  ],

  "shortAnswer": [
    {
      "difficulty": "medium|hard",
      "question": "Multi-part NCERT-style question with specific data. Format: 'Given [specific data/expression], find: (i) ... (ii) ... (iii) ...' Each sub-part must require computation.",
      "solution": "(i) Solution with calculation steps...<br>(ii) Solution with calculation steps...<br>(iii) Solution with calculation steps..."
    }
  ],

  "longAnswer": [
    {
      "difficulty": "hard|very hard",
      "question": "Comprehensive problem requiring 5+ steps. e.g. Prove that... / A survey of 100 students shows... find using formula. / If [specific scenario with real numbers], find [multiple quantities].",
      "solution": "Step 1: State what is given and what is to be found.<br>Step 2: Apply the relevant formula/theorem.<br>Step 3: Substitute the specific values.<br>Step 4: Simplify step-by-step.<br>Step 5: State the final answer with units if applicable."
    }
  ],

  "caseStudy": {
    "context": "A realistic scenario paragraph with SPECIFIC NUMERICAL DATA relevant to ${topic.title}. E.g. 'In a class of 40 students, 25 play cricket, 18 play football...' or 'A company's monthly profit for 6 months is: ₹12000, ₹15000, ₹18000...' — must include actual numbers students can compute with.",
    "subQuestions": [
      { "question": "Specific computational question using the data above (i) Find... (ii) Calculate...", "solution": "Full worked solution with steps and final numerical answer." },
      { "question": "A harder follow-up: Verify that... / Using the above result, find... / If an additional condition is added, determine...", "solution": "Complete step-by-step solution." }
    ]
  },

  "pyqs": [
    {
      "year": "CBSE 2023|CBSE 2022|CBSE Sample Paper 2024|CBSE Sample Paper 2023|CBSE 2020",
      "question": "Actual board-exam style question with specific numbers. Match the style and difficulty of real CBSE Applied Maths board papers.",
      "marks": 1,
      "answer": "Option letter if MCQ, else null",
      "solution": "Complete solution as expected in board exams, with each step shown."
    }
  ],

  "testQuestions": [
    {
      "question": "Computation/application MCQ with specific values. NOT definition-only questions.",
      "A": "...", "B": "...", "C": "...", "D": "...",
      "answer": "A|B|C|D",
      "solution": "Brief 1-2 line explanation with key calculation."
    }
  ]
}

CRITICAL CONTENT REQUIREMENTS:
1. theory: exactly 3 cards — definitions, key properties, and a worked example each
2. mcqs: exactly 7 questions (2 easy, 2 medium, 2 hard, 1 very hard)
   - EVERY MCQ must have SPECIFIC numbers/sets/expressions in the question stem
   - Options must be specific values, NOT vague like "True/False" or "Always/Never"
   - e.g. for Sets: A={1,2,3}, for GP: first term=3 ratio=2, for Statistics: data=[4,7,9,12,3]
3. assertionReason: exactly 2 pairs — both must use specific mathematical examples
4. shortAnswer: exactly 3 multi-part questions, each with (i)(ii)(iii) sub-parts
   - Each sub-part must require a distinct calculation
   - NCERT Exercise style: clear, unambiguous, specific
5. longAnswer: exactly 2 full-solution problems — each needs minimum 5 computation steps
6. caseStudy: exactly 1 with 2 sub-questions — must use REAL numbers students compute
7. pyqs: exactly 4 questions — marks field must be a NUMBER (1, 2, or 4), not a string
8. testQuestions: exactly 10 MCQs with specific numerical values
9. ALL content strictly about "${topic.title}" ONLY — no tangential topics
10. NO LaTeX backslash notation — Unicode symbols ONLY
11. Difficulty strictly progresses easy → very hard
12. In solutions, show ALL working steps — not just the final answer
`;
}

// ── HTML generator ─────────────────────────────────────────────────────────
function uid() { return Math.random().toString(36).slice(2, 9); }

function diffBadge(diff) {
  const styles = {
    'easy':      'background:#d1fae5;color:#065f46',
    'medium':    'background:#fef3c7;color:#92400e',
    'hard':      'background:#fee2e2;color:#991b1b',
    'very hard': 'background:#ede9fe;color:#5b21b6'
  };
  const s = styles[diff] || styles['medium'];
  return `<span style="float:right;font-size:0.7rem;padding:2px 9px;border-radius:12px;font-weight:600;${s}">${diff}</span>`;
}

function buildHTML(topic, data) {
  const unitPath = topic.dir.split('/')[0];
  const breadcrumbUnit = `Unit ${topic.unit} – ${topic.unitName}`;

  // ── Theory cards ──
  const theoryHTML = data.theory.map(card => `
    <div class="card-premium">
      <h3 class="card-title">${card.heading}</h3>
      <p class="theory-para">${card.body}</p>
      ${card.formula ? `<div class="theory-highlight">${card.formula}</div>` : ''}
      ${card.exampleTitle ? `
      <div class="theory-example" style="margin-top:15px;border-left:3px solid var(--primary);padding-left:15px;">
        <strong>Example:</strong> ${card.exampleTitle}
        <details class="solution-details" style="margin-top:5px;">
          <summary>Show Step-by-Step Solution</summary>
          <p class="solution-explanation">${card.exampleSolution}</p>
        </details>
      </div>` : ''}
    </div>`).join('\n');

  // ── MCQs ──
  let mcqNum = 0;
  const mcqHTML = data.mcqs.map(q => {
    mcqNum++;
    const id = 'mcq-' + uid();
    return `
    <div class="practice-question-card">
      <div class="q-row">
        <div class="q-num-badge">${mcqNum}</div>
        <div class="q-body">
          <p class="q-text">${diffBadge(q.difficulty)}${q.question}</p>
          <div class="q-options">
            ${['A','B','C','D'].map(l => `
            <label class="opt-label">
              <input type="radio" class="opt-radio" name="${id}" value="${l}">
              <span><b>${l}.</b> ${q[l]}</span>
            </label>`).join('')}
          </div>
          <details class="solution-details">
            <summary>Show Answer</summary>
            <p class="solution-correct">✔ Correct: ${q.answer}</p>
            <p class="solution-explanation">${q.solution}</p>
          </details>
        </div>
      </div>
    </div>`;
  }).join('\n');

  // ── Assertion-Reason ──
  let arNum = 0;
  const arHTML = data.assertionReason.map(q => {
    arNum++;
    const id = 'ar-' + uid();
    return `
    <div class="practice-question-card">
      <div class="q-row">
        <div class="q-num-badge">${arNum}</div>
        <div class="q-body">
          <p class="q-text">
            <strong>Assertion (A):</strong> ${q.assertion}<br>
            <strong>Reason (R):</strong> ${q.reason}<br><br>
            <em>Choose the correct option:</em><br>
            (A) Both A and R are true and R is the correct explanation of A.<br>
            (B) Both A and R are true but R is not the correct explanation of A.<br>
            (C) A is true but R is false.<br>
            (D) A is false but R is true.
          </p>
          <div class="q-options">
            ${['A','B','C','D'].map(l => `
            <label class="opt-label">
              <input type="radio" class="opt-radio" name="${id}" value="${l}">
              <span><b>${l}.</b> Option ${l}</span>
            </label>`).join('')}
          </div>
          <details class="solution-details">
            <summary>Show Answer</summary>
            <p class="solution-correct">✔ Correct: ${q.answer}</p>
            <p class="solution-explanation">${q.solution}</p>
          </details>
        </div>
      </div>
    </div>`;
  }).join('\n');

  // ── Short Answer ──
  let saNum = 0;
  const saHTML = data.shortAnswer.map(q => {
    saNum++;
    return `
    <div class="practice-question-card">
      <div class="q-row">
        <div class="q-num-badge">${saNum}</div>
        <div class="q-body">
          <p class="q-text">${diffBadge(q.difficulty)}${q.question}</p>
          <details class="solution-details">
            <summary>Show Answer &amp; Solution</summary>
            <p class="solution-explanation">${q.solution}</p>
          </details>
        </div>
      </div>
    </div>`;
  }).join('\n');

  // ── Long Answer ──
  let laNum = 0;
  const laHTML = data.longAnswer.map(q => {
    laNum++;
    return `
    <div class="practice-question-card">
      <div class="q-row">
        <div class="q-num-badge">${laNum}</div>
        <div class="q-body">
          <p class="q-text">${diffBadge(q.difficulty)}${q.question}</p>
          <details class="solution-details">
            <summary>Show Answer &amp; Solution</summary>
            <p class="solution-explanation">${q.solution}</p>
          </details>
        </div>
      </div>
    </div>`;
  }).join('\n');

  // ── Case Study ──
  const cs = data.caseStudy;
  const caseHTML = `
    <div class="practice-question-card">
      <div class="q-row">
        <div class="q-num-badge">★</div>
        <div class="q-body">
          <p class="q-text"><strong>Case Study:</strong> ${cs.context}</p>
          <div style="margin-left:15px;margin-top:10px;">
            ${cs.subQuestions.map((sq, i) => `
            <p style="margin-top:15px;"><strong>Sub-question ${i+1}:</strong> ${sq.question}</p>
            <details class="solution-details">
              <summary>Show Solution</summary>
              <p class="solution-explanation">${sq.solution}</p>
            </details>`).join('')}
          </div>
        </div>
      </div>
    </div>`;

  // ── PYQs ──
  let pyqNum = 0;
  const pyqHTML = data.pyqs.map(q => {
    pyqNum++;
    return `
    <div class="practice-question-card" style="border-left:4px solid #e67e22;">
      <div class="q-row">
        <div class="q-num-badge" style="background:#e67e22;">${pyqNum}</div>
        <div class="q-body">
          <div style="margin-bottom:8px;display:flex;gap:8px;flex-wrap:wrap;">
            <span style="background:#fef3c7;color:#92400e;padding:2px 10px;border-radius:12px;font-size:0.75rem;font-weight:600;">📋 ${q.year}</span>
            ${q.marks ? `<span style="background:#e0f2fe;color:#0369a1;padding:2px 10px;border-radius:12px;font-size:0.75rem;font-weight:600;">📝 ${q.marks} Mark${q.marks>1?'s':''}</span>` : ''}
          </div>
          <p class="q-text">${q.question}</p>
          <details class="solution-details">
            <summary>Show Answer &amp; Solution</summary>
            ${q.answer ? `<p class="solution-correct">✔ Answer: ${q.answer}</p>` : ''}
            <p class="solution-explanation">${q.solution}</p>
          </details>
        </div>
      </div>
    </div>`;
  }).join('\n');

  // ── Test blocks ──
  const testBlocksHTML = data.testQuestions.map((q, i) => `
    <div class="test-qblock" id="tq-${i}">
      <p class="test-qtext">
        <span class="test-qnum">Q${i+1}</span>
        <span style="display:block;margin-top:6px">${q.question}</span>
      </p>
      <div class="test-opts-grid">
        ${['A','B','C','D'].map(l => `
        <div class="test-opt" data-qi="${i}" data-ch="${l}" onclick="selOpt(this)">
          <span class="opt-ltr">${l}</span>
          <span>${q[l]}</span>
        </div>`).join('')}
      </div>
      <input type="hidden" id="tans-${i}" value="${q.answer}">
      <input type="hidden" id="tsel-${i}" value="">
    </div>`).join('\n');

  // ── staticTestData for Gemini dynamic mode ──
  const staticTestData = JSON.stringify(data.testQuestions.map(q => ({
    qEn: q.question,
    qHi: q.question,
    optsEn: [q.A, q.B, q.C, q.D],
    optsHi: ['','','',''],
    ans: q.answer,
    solEn: q.solution,
    solHi: ''
  })));

  return `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topic.title} – Class 11 Applied Mathematics | SJMaths</title>
    <meta name="description" content="${data.seoDescription}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://sjmaths.com/class-11-applied-mathematics/${topic.dir}/">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=574ed909">
    <link rel="stylesheet" href="/assets/css/topic-details.min.css?v=052ea02c">
    <link rel="stylesheet" href="/assets/css/upsssc-lower.min.css?v=94ee8a40">
    <!-- MathJax -->
    <script>
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        processEnvironments: true
      },
      options: { skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre'] }
    };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
</head>
<body>
    <div id="header-container"></div>

    <div class="container">
        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="/class-11-applied-mathematics/">Syllabus</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/class-11-applied-mathematics/#unit-${topic.unit}">${breadcrumbUnit}</a>
                <i class="fas fa-chevron-right"></i>
                <span>${topic.topicGroup}</span>
                <i class="fas fa-chevron-right"></i>
                <span>${topic.title}</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>${topic.title}</h1>
            <p>${data.seoDescription}</p>
        </div>

        <div class="subject-nav">
            <button class="sub-nav-item active" data-tab="theory">
                <span>Theory &amp; Concepts</span>
            </button>
            <button class="sub-nav-item" data-tab="practice">
                <span>Practice Questions</span>
            </button>
            <button class="sub-nav-item" data-tab="pyqs">
                <span>CBSE PYQs</span>
            </button>
            <button class="sub-nav-item" data-tab="test">
                <span>10-Q Mini Test</span>
            </button>
        </div>

        <div class="topic-content">

            <!-- ═══════════════════ TAB 1: THEORY ═══════════════════ -->
            <div id="tab-theory" class="tab-content" style="display:block">
                ${theoryHTML}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="practice" onclick="switchTab('practice')">
                        <span>Next: Practice Questions</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- ═══════════════════ TAB 2: PRACTICE ═══════════════════ -->
            <div id="tab-practice" class="tab-content" style="display:none">
                <h3 class="exercise-section-title">Section A: Multiple Choice Questions (MCQs)</h3>
                ${mcqHTML}

                <h3 class="exercise-section-title" style="margin-top:2rem;">Section B: Assertion–Reason Questions</h3>
                ${arHTML}

                <h3 class="exercise-section-title" style="margin-top:2rem;">Section C: Short Answer Questions</h3>
                ${saHTML}

                <h3 class="exercise-section-title" style="margin-top:2rem;">Section D: Long Answer Questions</h3>
                ${laHTML}

                <h3 class="exercise-section-title" style="margin-top:2rem;">Section E: Case-Based Question</h3>
                ${caseHTML}

                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="pyqs" onclick="switchTab('pyqs')">
                        <span>Next: CBSE PYQs</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- ═══════════════════ TAB 3: PYQs ═══════════════════ -->
            <div id="tab-pyqs" class="tab-content" style="display:none">
                <h3 class="exercise-section-title">CBSE Board &amp; Sample Paper Past Year Questions</h3>
                ${pyqHTML}
                <div class="next-tab-btn-container">
                    <button class="next-tab-btn" data-tab="test" onclick="switchTab('test')">
                        <span>Next: 10-Q Mini Test</span>
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- ═══════════════════ TAB 4: MINI TEST ═══════════════════ -->
            <div id="tab-test" class="tab-content" style="display:none">
                <div class="test-container">
                    <div class="card-premium" style="margin-bottom:2rem;">
                        <h4 class="card-title">Dynamic Test Generator (Gemini Powered)</h4>
                        <p style="font-size:0.9rem;margin-bottom:1rem;">
                            Enter your Gemini API Key to generate a fresh test in real-time. Or click <strong>Use Static Test</strong> to load pre-generated questions.
                        </p>
                        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:1rem;">
                            <input type="password" id="gemini-api-key-input" placeholder="Enter Gemini API Key (AIzaSy...)"
                                style="padding:10px;border:1px solid var(--border);border-radius:8px;flex-grow:1;font-family:inherit;background:var(--card-bg);color:var(--text);">
                            <button onclick="saveApiKey()" style="padding:10px 20px;background:var(--primary);color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">Save Key</button>
                        </div>
                        <div style="display:flex;gap:10px;">
                            <button id="gen-dynamic-btn" onclick="generateDynamicTest()"
                                style="padding:10px 20px;background:#3498db;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;display:none;">
                                Generate Dynamic Test
                            </button>
                            <button onclick="loadStaticTest()"
                                style="padding:10px 20px;background:#7f8c8d;color:white;border:none;border-radius:8px;cursor:pointer;font-weight:bold;">
                                Use Static Test
                            </button>
                        </div>
                    </div>

                    <div id="test-start-scr">
                        <p class="test-desc">This test contains 10 multiple-choice questions covering <strong>${topic.title}</strong>. You have 10 minutes to complete it.</p>
                        <button class="start-test-btn" onclick="startTest()">Start Test</button>
                    </div>

                    <div id="test-area" style="display:none">
                        <div class="test-hdr">
                            <div>Time Left</div>
                            <div class="test-tmr" id="tmr-display">10:00</div>
                        </div>
                        <div class="test-prog-bar"><div class="test-prog-fill" id="prog-fill" style="width:0%"></div></div>
                        <div id="test-questions"></div>
                        <div style="text-align:center;margin:24px 0">
                            <button onclick="submitTest()" id="submit-btn"
                                style="padding:13px 38px;background:linear-gradient(135deg,#27ae60,#2ecc71);color:white;border:none;border-radius:30px;font-size:1.1rem;font-weight:700;cursor:pointer;box-shadow:0 8px 20px rgba(39,174,96,0.4);">
                                <i class="fas fa-paper-plane"></i> Submit Test
                            </button>
                        </div>
                    </div>

                    <div class="test-result" id="test-result" style="display:none">
                        <div style="font-size:1.3rem"><i class="fas fa-trophy"></i> Test Complete!</div>
                        <div class="result-score" id="res-score">0/10</div>
                        <div id="res-label" style="font-size:1rem;opacity:0.9;margin-bottom:5px"></div>
                        <div class="grade-bdg" id="res-grade"></div>
                        <div style="margin-top:18px">
                            <button class="tact-btn" onclick="retakeTest()" style="background:#059669;color:white"><i class="fas fa-redo"></i> Retake</button>
                            <button class="tact-btn" data-tab="practice" onclick="switchTab('practice')" style="background:white;color:#059669"><i class="fas fa-book"></i> Practice More</button>
                        </div>
                    </div>
                </div>
            </div>

        </div><!-- /topic-content -->
    </div><!-- /container -->

    <div id="footer-container"></div>

    <script>
        window.staticTestData = ${staticTestData};
        window.upssscTestData = [];
    </script>

    <script src="/assets/js/search.min.js?v=68a0a505" defer></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer></script>
    <script src="/assets/js/global-header.min.js?v=b494d036" defer></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer></script>
    <script src="/assets/js/upsssc-lower.min.js?v=04b168f8" defer></script>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const keyInput  = document.getElementById('gemini-api-key-input');
            const dynamicBtn = document.getElementById('gen-dynamic-btn');
            const savedKey  = localStorage.getItem('gemini-api-key');
            if (savedKey) { keyInput.value = savedKey; dynamicBtn.style.display = 'inline-block'; }
            window.upssscTestData = JSON.parse(JSON.stringify(window.staticTestData));
            renderTestQuestions(window.upssscTestData);
        });

        function saveApiKey() {
            const key = document.getElementById('gemini-api-key-input').value.trim();
            if (key) {
                localStorage.setItem('gemini-api-key', key);
                document.getElementById('gen-dynamic-btn').style.display = 'inline-block';
                alert('API Key saved!');
            } else {
                localStorage.removeItem('gemini-api-key');
                document.getElementById('gen-dynamic-btn').style.display = 'none';
                alert('API Key cleared.');
            }
        }

        function loadStaticTest() {
            window.upssscTestData = JSON.parse(JSON.stringify(window.staticTestData));
            renderTestQuestions(window.upssscTestData);
            alert('Loaded static pre-generated test questions.');
        }

        function renderTestQuestions(data) {
            const container = document.getElementById('test-questions');
            container.innerHTML = '';
            data.forEach((q, idx) => {
                const qBlock = document.createElement('div');
                qBlock.className = 'test-qblock';
                qBlock.id = 'tq-' + idx;
                let fmtQ = q.qEn
                    .replace(/\\*\\*Assertion \\(A\\):\\*\\*/g, '<strong>Assertion (A):</strong>')
                    .replace(/\\*\\*Reason \\(R\\):\\*\\*/g, '<strong>Reason (R):</strong>')
                    .replace(/\\*\\*Case Study:\\*\\*/g, '<strong>Case Study:</strong>')
                    .replace(/\\n/g, '<br>');
                qBlock.innerHTML = \`
                    <p class="test-qtext">
                        <span class="test-qnum">Q\${idx+1}</span>
                        <span style="display:block;margin-top:6px">\${fmtQ}</span>
                    </p>
                    <div class="test-opts-grid">
                        <div class="test-opt" data-qi="\${idx}" data-ch="A" onclick="selOpt(this)"><span class="opt-ltr">A</span><span>\${q.optsEn[0]}</span></div>
                        <div class="test-opt" data-qi="\${idx}" data-ch="B" onclick="selOpt(this)"><span class="opt-ltr">B</span><span>\${q.optsEn[1]}</span></div>
                        <div class="test-opt" data-qi="\${idx}" data-ch="C" onclick="selOpt(this)"><span class="opt-ltr">C</span><span>\${q.optsEn[2]}</span></div>
                        <div class="test-opt" data-qi="\${idx}" data-ch="D" onclick="selOpt(this)"><span class="opt-ltr">D</span><span>\${q.optsEn[3]}</span></div>
                    </div>
                    <input type="hidden" id="tans-\${idx}" value="\${q.ans}">
                    <input type="hidden" id="tsel-\${idx}" value="">
                \`;
                container.appendChild(qBlock);
            });
        }

        async function generateDynamicTest() {
            const apiKey = localStorage.getItem('gemini-api-key');
            if (!apiKey) { alert('Please save your Gemini API Key first.'); return; }
            const btn = document.getElementById('gen-dynamic-btn');
            btn.disabled = true; btn.textContent = 'Generating...';
            const prompt = \`Generate a 10-question multiple choice test for CBSE Class 11 Applied Mathematics on: "${topic.title}". Return ONLY a JSON array, each object: {"qEn":"...","optsEn":["A","B","C","D"],"ans":"A","solEn":"..."}\`;
            try {
                const res = await fetch(\`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=\${apiKey}\`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ contents:[{parts:[{text:prompt}]}], generationConfig:{responseMimeType:'application/json'} })
                });
                const result = await res.json();
                const quizData = JSON.parse(result.candidates[0].content.parts[0].text);
                window.upssscTestData = quizData.map(q => ({ qEn:q.qEn, qHi:q.qEn, optsEn:q.optsEn, optsHi:['','','',''], ans:q.ans, solEn:q.solEn, solHi:'' }));
                renderTestQuestions(window.upssscTestData);
                alert('Dynamic test generated!');
            } catch(err) {
                alert('Generation failed: ' + err.message + '. Using static test.');
                loadStaticTest();
            } finally {
                btn.disabled = false; btn.textContent = 'Generate Dynamic Test';
            }
        }
    </script>
</body>
</html>`;
}

// ── Delay helper ───────────────────────────────────────────────────────────
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── Main ───────────────────────────────────────────────────────────────────
async function main() {
  const topics = ONLY
    ? MICROTOPICS.filter(t => t.dir.includes(ONLY))
    : MICROTOPICS;

  if (!topics.length) {
    console.error(`❌  No topics found matching: ${ONLY}`);
    process.exit(1);
  }

  console.log(`\n🚀  Generating content for ${topics.length} microtopic(s) using gemini-3.1-flash-lite...\n`);

  let success = 0, failed = 0, callIndex = 0;
  const failedTopics = [];

  for (let i = 0; i < topics.length; i++) {
    const topic = topics[i];
    const outPath = path.join(BASE, ...topic.dir.split('/'), 'index.html');

    // Skip if resume mode and file already has content
    if (RESUME && fs.existsSync(outPath)) {
      const lines = fs.readFileSync(outPath, 'utf8').split('\n').length;
      if (lines > 400) {
        console.log(`⏭  [${i+1}/${topics.length}] SKIP (${lines} lines): ${topic.title}`);
        continue;
      }
    }

    process.stdout.write(`⏳  [${i+1}/${topics.length}] ${topic.title}... `);
    const currentModel = getModel(callIndex);
    process.stdout.write(`[${currentModel.split('-').slice(-2).join('-')}] `);

    let data = null;
    let attempts = 0;
    const maxAttempts = 5;

    while (!data && attempts < maxAttempts) {
      attempts++;
      try {
        data = await callGemini(buildPrompt(topic), currentModel);
      } catch (err) {
          const errMsg = err.message || '';
          // Parse retry-after time from quota error messages
          const retryMatch = errMsg.match(/retry in ([\d.]+)s/i);
          // Exponential backoff: 30s, 60s, 120s, 180s if no specific retry time
          const fallbackWait = Math.min(30 * Math.pow(2, attempts - 1), 180);
          const waitSec = retryMatch ? (Math.ceil(parseFloat(retryMatch[1])) + 5) : fallbackWait;
          if (attempts < maxAttempts) {
            process.stdout.write(`\n    ⚠  Attempt ${attempts} failed (wait ${waitSec}s): ${errMsg.split('\n')[0]}\n    `);
            await sleep(waitSec * 1000);
          } else {
            console.error(`\n    ❌  Failed after ${maxAttempts} attempts: ${errMsg.split('\n')[0]}`);
            failed++;
            failedTopics.push(topic.title);
          }
      }
    }

    if (!data) continue;

    try {
      // Ensure directory exists
      const dir = path.dirname(outPath);
      if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

      const html = buildHTML(topic, data);
      fs.writeFileSync(outPath, html, 'utf8');
      const lineCount = html.split('\n').length;
      console.log(`✅  Done (${lineCount} lines)`);
      success++;
      callIndex++;  // Only increment call index on successful generation
    } catch (err) {
      console.error(`\n    ❌  HTML generation/write error: ${err.message}`);
      failed++;
      failedTopics.push(topic.title);
    }

    // Rate limiting: 4s delay to stay under 15 RPM (gemini-2.5-flash free tier is 20 RPM)
    if (i < topics.length - 1) await sleep(4000);
  }

  console.log(`\n${'─'.repeat(60)}`);
  console.log(`✅  Success: ${success}  |  ❌ Failed: ${failed}`);
  if (failedTopics.length) {
    console.log('\nFailed topics (re-run with --only <partial-name>):');
    failedTopics.forEach(t => console.log('  •', t));
  }
  console.log(`\nDone! View at: http://localhost:8082/class-11-applied-mathematics/\n`);
}

main().catch(err => {
  console.error('Fatal error:', err.message);
  process.exit(1);
});
