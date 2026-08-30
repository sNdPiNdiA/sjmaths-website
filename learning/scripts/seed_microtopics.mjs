/**
 * seed_microtopics.mjs
 *
 * Fills the empty `concepts[]` array of every foundation skeleton with named
 * microtopic stubs (one per microtopic on the index.html module cards — 69 across
 * the 16 skeleton modules; M7 factor-pairs already has its 4 concepts + 12 problems
 * of full content). Each stub keeps the Schema v4 shape (id/title/subtitle/summary/
 * points/formula/trap) with `status: "stub"` so content can be added one by one;
 * the flag is removed once real content is written.
 *
 * Run: node seed_microtopics.mjs   (idempotent — skips non-empty concepts[])
 */
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const foundationsDir = path.join(root, "learning", "topics", "foundations", "mathematics");

// Microtopic names derived from each module card's description in index.html,
// split so the count matches the card's "N Microtopics" label.
const MICROTOPICS = {
  "prep-factors-multiples-divisibility": ["Primes & Factorisation Trees", "Divisibility Rules (2–11)", "HCF: Meaning & Finding", "LCM: Meaning & Finding", "Even/Odd Parity Laws for Proof"],
  "prep-fractions-ratios-percent": ["Fraction Operations", "Simplest Form & Conversions", "Ratio Comparisons", "Cross-Multiplication", "Unitary Method"],
  "prep-squares-roots-surds": ["Squares to 25²", "Square Roots & Estimation", "Surd Simplification", "Rationalisation", "Pythagorean Triples (3-4-5, 5-12-13)"],
  "prep-exponent-laws": ["Product, Quotient & Power Rules", "Zero & Negative Exponents", "Prime-Power Decomposition"],
  "prep-linear-equation-one-variable": ["Transposition & Balancing", "Solving ax + b = cx + d", "Fractional & Negative Coefficients", "Checking Solutions"],
  "prep-algebraic-identities-manipulation": ["(a±b)² and a²−b² Fluency", "Substitution & Evaluation", "Sign Rules with Negatives", "Formula Rearrangement"],
  "prep-word-problem-translation": ["Sentence-to-Equation Workflow", "Speed–Distance–Time Setups", "Cost & Age Setups", "Area & Perimeter Setups", "Consecutive Integer Patterns", "AP Story Patterns"],
  "prep-cartesian-plane-fluency": ["Plotting (x, y) & Quadrants", "Reading Intercepts from Graphs", "Parallel vs Intersecting vs Coincident Lines"],
  "prep-pythagoras-right-triangle": ["Theorem & Converse", "Hypotenuse Identification", "Altitude/Base Vocabulary", "Slant-Height Relation l² = r² + h²"],
  "prep-parallel-line-angle-facts": ["Alternate, Corresponding & Co-interior Angles", "Vertically Opposite Pairs", "Elevation ↔ Depression as Alternate Angles"],
  "prep-geometry-ratio-similarity": ["Scale Factor Intuition", "Corresponding Sides in Proportion", "Solving x/(x+3) = 4/5 Style Equations", "Midpoint Theorem"],
  "prep-circle-anatomy-sector-fractions": ["Radius/Chord/Arc/Tangent Vocabulary", "Sector vs Segment Distinction", "The 60°-is-⅙ Fraction Model", "π Fluency"],
  "prep-solids-recap-unit-conversions": ["Solid Vocabulary: Cone/Cylinder/Sphere/Hemisphere", "CSA vs TSA Formulas", "Cone-Slant ↔ Sector Link", "cm³ ↔ Litre ↔ m³ Conversions"],
  "prep-data-tables-averages": ["Frequency Tables & Class Intervals", "Class Marks", "Cumulative Frequency Reading", "Mean on Raw Data", "Mode & Median on Raw Data"],
  "prep-proof-format-congruence": ["Given/To-Prove/Proof Structure", "Contradiction Intuition", "Congruence Rules (SSS, SAS, ASA, RHS)", "Class 9 Circle Facts"],
  "prep-counting-chance-intuition": ["Sample Spaces", "Coin Outcomes", "Dice Outcomes", "52-Card Deck Structure", "Complementary Events", "Informal 'and' vs 'or'"]
};


// ---- Seed skeletons ----
import { readdirSync } from "node:fs";
const slugFile = {};
for (const cat of readdirSync(foundationsDir, { withFileTypes: true })) {
  if (!cat.isDirectory()) continue;
  for (const dir of readdirSync(path.join(foundationsDir, cat.name), { withFileTypes: true })) {
    if (!dir.isDirectory()) continue;
    const f = path.join(foundationsDir, cat.name, dir.name, `${dir.name}.json`);
    try { readFileSync(f, "utf8"); slugFile[dir.name] = f; } catch { /* no file */ }
  }
}
let seeded = 0, skipped = 0, totalMT = 0;
for (const [slug, titles] of Object.entries(MICROTOPICS)) {
  const file = slugFile[slug];
  if (!file) { console.log(`!! missing skeleton: ${slug}`); continue; }
  const json = JSON.parse(readFileSync(file, "utf8"));
  if (json.concepts && json.concepts.length > 0) { skipped++; continue; }
  json.concepts = titles.map((t, i) => stub(slug, i, t));
  writeFileSync(file, JSON.stringify(json, null, 2) + "\n", "utf8");
  seeded++; totalMT += titles.length;
}
console.log(`Microtopics seeded: ${totalMT} across ${seeded} modules (${skipped} already had concepts)`);

// ---- Append microtopic breakdown to foundations README ----
const readmePath = path.join(root, "learning", "topics", "foundations", "README.md");
let readme = readFileSync(readmePath, "utf8");
const marker = "<!-- microtopic-breakdown -->";
if (!readme.includes(marker)) {
  const section = [marker, "", "## Microtopic breakdown", "",
    "Microtopics live in each module's `concepts[]` array (Schema v4) — that is what the",
    "concept-mastery UI renders as concepts and what the WebMCP tools expose as content.",
    "Stub entries carry `\"status\": \"stub\"`; remove the flag as you author each one.", ""].join("\n");
  const rows = Object.entries(MICROTOPICS).map(([slug, ts]) => `- **${slug}** (${ts.length}): ${ts.join(" · ")}`);
  readme = readme.replace("## Adding content to a skeleton", section + rows.join("\n") + "\n\n## Adding content to a skeleton");
  writeFileSync(readmePath, readme, "utf8");
  console.log("README.md: microtopic breakdown appended");
} else {
  console.log("README.md: breakdown already present");
}

function stub(slug, i, title) {
  return {
    id: `mt_${String(i + 1).padStart(2, "0")}`,
    title: `${i + 1}. ${title}`,
    subtitle: "Microtopic stub — content pending",
    summary: `Learning objectives for "${title}" (${slug}) are to be authored.`,
    status: "stub",
    points: [],
    formula: null,
    trap: null
  };
}
