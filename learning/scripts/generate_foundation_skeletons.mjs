/**
 * generate_foundation_skeletons.mjs
 *
 * Creates folder + skeleton JSON (Schema v4.0.1) for every Prerequisite Microlearning
 * module listed in /learning/topics/class-10/mathematics/index.html ("Prerequisite
 * Microlearning — Skill Foundations": 17 modules, 74 microtopics) that does not yet
 * have content, registers each in learning/engine/topic-loader.js TOPIC_REGISTRY,
 * and writes a master README with the module → chapter mapping.
 *
 * Existing content files (factor-pairs, linear-equation-transposition) are untouched.
 * Run: node generate_foundation_skeletons.mjs   (idempotent; skips existing files)
 */
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const foundationsDir = path.join(root, "learning", "topics", "foundations", "mathematics");
const loaderPath = path.join(root, "learning", "engine", "topic-loader.js");
const indexHtmlPath = path.join(root, "learning", "topics", "class-10", "mathematics", "index.html");

// M1..M17 in curriculum order. M7 (factor-pairs) already has full content on disk.
const MODULES = [
  { code: "M1", slug: "prep-factors-multiples-divisibility", tier: "Tier 0 • Arithmetic", cat: "arithmetic", title: "Factors, Multiples & Divisibility", short: "Factors & Divisibility", count: 5, unlocks: "Ch 1, 4", chapters: [1, 4], desc: "Primes & factorisation trees, divisibility rules, HCF/LCM meaning, and even/odd parity laws for proof readiness." },
  { code: "M2", slug: "prep-fractions-ratios-percent", tier: "Tier 0 • Arithmetic", cat: "arithmetic", title: "Fractions, Ratios & Percent Sense", short: "Fractions & Percent", count: 5, unlocks: "Ch 3, 6, 14", chapters: [3, 6, 14], desc: "Fraction operations, simplest-form & conversions, ratio comparisons, cross-multiplication, and unitary method." },
  { code: "M3", slug: "prep-squares-roots-surds", tier: "Tier 0 • Arithmetic", cat: "arithmetic", title: "Squares, Roots & Surds", short: "Squares & Surds", count: 5, unlocks: "9 chapters", chapters: null, desc: "Squares to 25², surd simplification & rationalisation, and Pythagorean triples (3-4-5, 5-12-13) to automaticity." },
  { code: "M4", slug: "prep-exponent-laws", tier: "Tier 0 • Arithmetic", cat: "arithmetic", title: "Powers & Exponent Laws", short: "Exponent Laws", count: 3, unlocks: "Ch 1, 2", chapters: [1, 2], desc: "Product, quotient & power rules, zero/negative exponents, and prime-power decomposition of numbers." },
  { code: "M5", slug: "prep-linear-equation-one-variable", tier: "Tier 1 • Algebra Core", cat: "algebra", title: "Linear Equation in One Variable", short: "Linear Equation", count: 4, unlocks: "Gates 7 chapters", chapters: null, desc: "Transposition & balancing, solving ax + b = cx + d, fractional/negative coefficients, and checking solutions." },
  { code: "M6", slug: "prep-algebraic-identities-manipulation", tier: "Tier 1 • Algebra Core", cat: "algebra", title: "Algebraic Identities & Manipulation", short: "Identities", count: 4, unlocks: "Ch 2, 4, 8", chapters: [2, 4, 8], desc: "(a±b)² and a²−b² fluency, substitution & evaluation, sign rules with negatives, and formula rearrangement." },
  { code: "M7", slug: "factor-pairs", tier: "Tier 1 • Algebra Core", cat: "algebra", title: "Systematic Factor Pairs & Middle-Term Splitting", short: "Factor Pairs", count: 12, unlocks: "Ch 4 (factorisation)", chapters: [4], desc: "Sign signature rules, √N divisor stopping bounds, signed factor pair table generation, and 4-term grouping mastery.", exists: true },
  { code: "M8", slug: "prep-word-problem-translation", tier: "Tier 1 • Algebra Core", cat: "algebra", title: "Word-Problem Translation Patterns", short: "Word Problems", count: 6, unlocks: "Ch 3, 4, 5, 14", chapters: [3, 4, 5, 14], desc: "Sentence-to-equation workflow, speed-distance-time, cost/age/area setups, consecutive integers, and AP story patterns." },
  { code: "M9", slug: "prep-cartesian-plane-fluency", tier: "Tier 2 • Geometry Toolkit", cat: "geometry", title: "Cartesian Plane Fluency", short: "Cartesian Plane", count: 3, unlocks: "Ch 2, 3, 7", chapters: [2, 3, 7], desc: "Plotting (x, y) & quadrants, reading intercepts from graphs, and visually distinguishing parallel, intersecting & coincident lines." },
  { code: "M10", slug: "prep-pythagoras-right-triangle", tier: "Tier 2 • Geometry Toolkit", cat: "geometry", title: "Pythagoras & Right-Triangle Anatomy", short: "Pythagoras", count: 4, unlocks: "Gates 6 chapters", chapters: null, desc: "Theorem & converse, hypotenuse identification, altitude/base vocabulary, and the slant-height relation l² = r² + h²." },
  { code: "M11", slug: "prep-parallel-line-angle-facts", tier: "Tier 2 • Geometry Toolkit", cat: "geometry", title: "Parallel-Line Angle Facts", short: "Angle Facts", count: 3, unlocks: "Ch 6, 9", chapters: [6, 9], desc: "Alternate, corresponding & co-interior angles, vertically opposite pairs, and elevation ↔ depression as alternate angles." },
  { code: "M12", slug: "prep-geometry-ratio-similarity", tier: "Tier 2 • Geometry Toolkit", cat: "geometry", title: "Ratio in Geometry: Similarity Foundations", short: "Similarity Foundations", count: 4, unlocks: "Ch 6, 7", chapters: [6, 7], desc: "Scale factor intuition, corresponding sides in proportion, solving x/(x+3) = 4/5 style equations, and the midpoint theorem." },
  { code: "M13", slug: "prep-circle-anatomy-sector-fractions", tier: "Tier 3 • Measurement & Data", cat: "measurement", title: "Circle Anatomy & Fraction-of-Circle Thinking", short: "Circle Anatomy", count: 4, unlocks: "Ch 10, 11, 12", chapters: [10, 11, 12], desc: "Radius/chord/arc/tangent vocabulary, sector vs segment distinction, the 60°-is-⅙ model, and π fluency." },
  { code: "M14", slug: "prep-solids-recap-unit-conversions", tier: "Tier 3 • Measurement & Data", cat: "measurement", title: "Solid Vocabulary Recap (Class 9)", short: "Solids Recap", count: 4, unlocks: "Ch 11, 12", chapters: [11, 12], desc: "Cone/cylinder/sphere/hemisphere CSA-TSA-volume recall, cone-slant ↔ sector link, and cm³ ↔ litre ↔ m³ conversions." },
  { code: "M15", slug: "prep-data-tables-averages", tier: "Tier 3 • Measurement & Data", cat: "measurement", title: "Data Tables & Averages", short: "Data & Averages", count: 5, unlocks: "Ch 13", chapters: [13], desc: "Frequency tables & class intervals, class marks, cumulative frequency reading, and mean/mode/median on raw data." },
  { code: "M16", slug: "prep-proof-format-congruence", tier: "Tier 4 • Proof & Reasoning", cat: "proof", title: "If–Then Thinking & Proof Format", short: "Proof Format", count: 4, unlocks: "Ch 1, 6, 10", chapters: [1, 6, 10], desc: "Given/to-prove/proof structure, contradiction intuition, congruence rules (SSS, SAS, ASA, RHS), and Class 9 circle facts." },
  { code: "M17", slug: "prep-counting-chance-intuition", tier: "Tier 4 • Proof & Reasoning", cat: "proof", title: "Counting & Chance Intuition", short: "Counting & Chance", count: 6, unlocks: "Ch 14", chapters: [14], desc: "Sample spaces, coin/dice outcomes, 52-card deck structure, complementary events, and informal \"and\" vs \"or\"." }
];

const CHAPTER_NAMES = {
  1: "Real Numbers", 2: "Polynomials", 3: "Pair of Linear Equations in Two Variables",
  4: "Quadratic Equations", 5: "Arithmetic Progressions", 6: "Triangles",
  7: "Coordinate Geometry", 8: "Introduction to Trigonometry", 9: "Applications of Trigonometry",
  10: "Circles", 11: "Areas Related to Circles", 12: "Surface Areas & Volumes",
  13: "Statistics", 14: "Probability"
};

function skeleton(mod, prev, next) {
  const topicId = `math-foundations-${mod.slug}`;
  const stage = (id, n, name, d) => ({ id, title: `${n}. ${name}`, description: d });
  return {
    schema_version: "4.0.1",
    content_type: "learning_topic",
    topic: {
      id: topicId,
      class: 10,
      board: "CBSE",
      subject: "Mathematics",
      chapter: `Foundations — ${mod.tier}`,
      title: mod.title,
      short_title: mod.short,
      description: mod.desc,
      status: "active",
      unlock_all_types: true,
      learning_format: "concept_mastery",
      student_journey: "Concepts → Worked Solutions → Strategy Choices → Guided Calculation → Notebook Solve",
      module_code: mod.code,
      tier: mod.tier,
      microtopic_count: mod.count,
      unlocks: mod.unlocks,
      unlocks_chapters: mod.chapters
    },
    previous_topic: prev ? { id: prev.slug, title: prev.title, url: `/learning/ui/concept-mastery/?topic=${prev.slug}` } : null,
    next_topic: next ? { id: next.slug, title: next.title, url: `/learning/ui/concept-mastery/?topic=${next.slug}` } : null,
    stages: {
      progression: [
        stage("concepts", 1, "Concepts", `Core ideas of ${mod.short} explained from first principles`),
        stage("worked_examples", 2, "Solutions", `Worked solutions building the ${mod.short} toolkit`),
        stage("stage_1_strategy", 3, "Strategy", "Strategy-choice questions on selecting the right approach"),
        stage("stage_2_calc", 4, "Guided Calc", "Fill-in-the-step guided calculations"),
        stage("stage_3_notebook", 5, "Notebook", "Self-audited full solutions in the notebook")
      ]
    },
    reference_drawer: null,
    concepts: [],
    worked_examples: [],
    question_types: []
  };
}

// ---- 1. Create skeleton files for modules without content ----
let created = 0, skipped = 0;
for (let i = 0; i < MODULES.length; i++) {
  const mod = MODULES[i];
  const dir = path.join(foundationsDir, mod.cat, mod.slug);
  const file = path.join(dir, `${mod.slug}.json`);
  if (mod.exists || existsSync(file)) { skipped++; continue; }
  mkdirSync(dir, { recursive: true });
  const prev = i > 0 ? MODULES[i - 1] : null;
  const next = i < MODULES.length - 1 ? MODULES[i + 1] : null;
  writeFileSync(file, JSON.stringify(skeleton(mod, prev, next), null, 2) + "\n", "utf8");
  created++;
}
console.log(`Skeletons: ${created} created, ${skipped} already present (${MODULES.length} modules total)`);

// ---- 2. Register in topic-loader.js TOPIC_REGISTRY (short + math-foundations- aliases) ----
let loader = readFileSync(loaderPath, "utf8");
const anchor = loader.indexOf("'math-foundations-factor-pairs'");
if (anchor === -1) throw new Error("Anchor entry 'math-foundations-factor-pairs' not found in topic-loader.js");
const needle = "  }\n});";
const at = loader.indexOf(needle, anchor);
if (at === -1) throw new Error("TOPIC_REGISTRY closing marker not found");

const newBlocks = [];
for (const mod of MODULES) {
  if (mod.exists) continue; // factor-pairs already registered
  const block = (alias) => `  '${alias}': {
    dataPath: '/learning/topics/foundations/mathematics/${mod.cat}/${mod.slug}/${mod.slug}.json',
    cssPath: '/learning/topics/foundations/mathematics/${mod.cat}/${mod.slug}/${mod.slug}.css',
    jsPath: '/learning/topics/foundations/mathematics/${mod.cat}/${mod.slug}/${mod.slug}.js',
    fsPath: '../topics/foundations/mathematics/${mod.cat}/${mod.slug}/${mod.slug}.json'
  }`;
  newBlocks.push(block(mod.slug), block(`math-foundations-${mod.slug}`));
}
const ALREADY = "prep-factors-multiples-divisibility";
if (!loader.includes(ALREADY)) {
  loader = loader.slice(0, at) + `  },\n\n` + newBlocks.join(",\n\n") + `\n});` + loader.slice(at + needle.length);
  writeFileSync(loaderPath, loader, "utf8");
  console.log(`topic-loader.js: ${newBlocks.length} registry entries added`);
} else {
  console.log("topic-loader.js: registry entries already present, skipped");
}

// ---- 3. Master README with the full module → chapter mapping ----
const lines = [
  "# Foundations — Prerequisite Microlearning Modules",
  "",
  "Source of truth: the \"Prerequisite Microlearning — Skill Foundations\" section of",
  "`learning/topics/class-10/mathematics/index.html` — **17 modules • 74 microtopics**,",
  "sequenced from arithmetic to proofs. Clear these first and every Class 10 chapter becomes comfortable.",
  "",
  "| Module | Tier | Title | Microtopics | Unlocks (chapters) | Folder | Status |",
  "|---|---|---|---|---|---|---|"
];
for (const m of MODULES) {
  const rel = `foundations/mathematics/${m.cat}/${m.slug}/`;
  const chList = m.chapters ? m.chapters.map(c => `Ch ${c} (${CHAPTER_NAMES[c]})`).join(", ") : m.unlocks;
  lines.push(`| ${m.code} | ${m.tier} | ${m.title} | ${m.count} | ${chList} | \`${rel}\` | ${m.exists ? "content ready" : "skeleton — needs content"} |`);
}
lines.push(
  "",
  "> Note: `linear-equation-transposition` (algebra) also exists on disk with full content;",
  "> it is referenced by the WebMCP prerequisite chain even though it has no index card.",
  "",
  "## Content status",
  "",
  "- **factor-pairs (M7)** and **linear-equation-transposition** — full Schema 4.0.x content, live in the concept-mastery UI and the WebMCP prerequisite check.",
  "- **15 skeleton modules** — folders and Schema 4.0.1 JSON scaffolds (empty `concepts`, `worked_examples`, `question_types`) ready for content, one module at a time.",
  "",
  "## Adding content to a skeleton",
  "",
  "1. Open the module's `<slug>/<slug>.json`.",
  "2. Fill `concepts[]` (see `algebra/factor-pairs/factor-pairs.json` for the exact shape).",
  "3. Fill `worked_examples[]` and `reference_drawer`.",
  "4. Add question pools to `question_types[]` (`type`, `title`, `pool[]` with `steps[0].focus`, `strategy_question`, `strategy_options[]`, `correct_strategy_index`).",
  "5. Launch check: `/learning/ui/concept-mastery/?topic=<slug>` — the module is already registered in `learning/engine/topic-loader.js`.",
  ""
);
writeFileSync(path.join(root, "learning", "topics", "foundations", "README.md"), lines.join("\n") + "\n", "utf8");
console.log("README.md written with the full module → chapter mapping");

// ---- 4. Cross-check: every foundation id referenced by index.html must now resolve ----
const html = readFileSync(indexHtmlPath, "utf8");
const ids = [...new Set([...html.matchAll(/topic=((?:prep-|factor-pairs|linear-equation-transposition)[a-z0-9-]*)/g)].map(m => m[1]))];
const missing = ids.filter(id => !loader.includes(`'${id}':`) && !loader.includes(`'math-foundations-${id}':`));
console.log(`Index foundation links: ${ids.length} unique ids, unresolved after patch: ${missing.length ? missing.join(", ") : "none"}`);