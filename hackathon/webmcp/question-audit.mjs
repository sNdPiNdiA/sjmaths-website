/**
 * question-audit.mjs
 *
 * Deepest sweep: verifies EVERY question in EVERY pool of EVERY topic (43 topics,
 * all question_types pools), not just a sample.
 *
 *  Data level (from disk JSON):
 *   - question ids present and unique within a topic
 *   - correct_strategy_index is an integer within strategy_options range
 *   - hint level 1/2/3 sources exist (focus / strategy_question / correct option)
 *
 *  Tool level (live executeTool calls):
 *   - evaluate_practice wrong  -> validated, is_correct=false, streak -> 1
 *   - evaluate_practice correct-> validated against real key, is_correct=true, streak -> 0
 *   - get_hint level 1         -> real text, and does NOT leak the correct option
 *   - get_topic_content        -> reported question count matches disk per topic
 */
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createWebMCPTools } from "./src/webmcp-tools.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const catalogPath = path.join(root, "hackathon", "webmcp", "data", "class-10", "mathematics", "cbse-class-10-mathematics.json");
const catalog = JSON.parse(readFileSync(catalogPath, "utf8"));

const tools = createWebMCPTools(catalog);
const topics = (catalog.chapters || []).flatMap(ch => (ch.topics || []).map(t => ({ ...t, ch: ch.number })));

const fails = {
  dup_id: [], key_range: [], hint_missing: [], hint_leak: [],
  wrong_eval: [], correct_eval: [], streak: [], count_mismatch: [], no_questions: []
};
function bad(cat, msg) { fails[cat].push(msg); }

let qTotal = 0;
let topicIdx = 0;
for (const t of topics) {
  topicIdx++;
  const disk = JSON.parse(readFileSync(path.join(root, t.data_path), "utf8"));
  const pools = disk.question_types || [];
  let diskCount = 0;
  const seenIds = new Set();

  for (const pool of pools) {
    for (const q of pool.pool || []) {
      qTotal++;
      diskCount++;
      const label = `ch${t.ch}/${t.id}/${q.id}`;

      if (seenIds.has(q.id)) bad("dup_id", label);
      seenIds.add(q.id);

      const step = (q.steps || [])[0] || {};
      const key = step.correct_strategy_index;
      const opts = step.strategy_options || [];
      if (!Number.isInteger(key) || key < 0 || key >= opts.length) {
        bad("key_range", `${label} key=${key} options=${opts.length}`);
        continue; // cannot safely evaluate without a valid key
      }
      if (!step.focus) bad("hint_missing", `${label} L1 focus`);
      if (!step.strategy_question) bad("hint_missing", `${label} L2 strategy_question`);
      if (!opts[key]) bad("hint_missing", `${label} L3 correct option`);

      // --- live tool checks ---
      const wrong = await tools.executeTool("evaluate_practice", { topic_id: t.id, question_id: q.id, selected_index: 99 });
      if (!wrong.validated_against_content || wrong.is_correct !== false) bad("wrong_eval", label);
      if (wrong.error_streak !== 1) bad("streak", `${label} after wrong: ${wrong.error_streak}`);

      const right = await tools.executeTool("evaluate_practice", { topic_id: t.id, question_id: q.id, selected_index: key });
      if (!right.validated_against_content || right.is_correct !== true) bad("correct_eval", label);
      if (right.error_streak !== 0) bad("streak", `${label} after correct: ${right.error_streak}`);

      const hint = await tools.executeTool("get_hint", { topic_id: t.id, question_id: q.id, current_level: 0 });
      if (!hint.hint_text) bad("hint_missing", `${label} tool L1 text`);
      else if (hint.hint_text === opts[key]) bad("hint_leak", `${label} L1 hint equals correct option`);

      // --- PART2 ---
    }
  }

  if (diskCount === 0) bad("no_questions", t.id);
  const content = await tools.executeTool("get_topic_content", { topic_id: t.id, mode: "assessment" });
  if (content.total_question_count !== diskCount) {
    bad("count_mismatch", `${t.id}: tool=${content.total_question_count} disk=${diskCount}`);
  }
}

// ---- Report ----
console.log(`\nScanned ${qTotal} questions across ${topics.length} topics\n`);
const labels = {
  dup_id: "duplicate question ids in a topic",
  key_range: "answer key missing / out of range",
  hint_missing: "hint source missing",
  hint_leak: "level-1 hint leaks the answer",
  wrong_eval: "wrong attempt mis-evaluated",
  correct_eval: "correct attempt mis-evaluated",
  streak: "error streak mis-tracked",
  count_mismatch: "tool question count != disk",
  no_questions: "topic has no questions"
};
let total = 0;
for (const [k, label] of Object.entries(labels)) {
  const n = fails[k].length;
  total += n;
  console.log(`${n === 0 ? "PASS" : "FAIL x" + n}  ${label}`);
  for (const f of fails[k].slice(0, 8)) console.log(`        !! ${f}`);
  if (fails[k].length > 8) console.log(`        ... and ${fails[k].length - 8} more`);
}
console.log(`\n====================================================`);
console.log(total === 0
  ? `QUESTION AUDIT: every one of the ${qTotal} questions validates end-to-end`
  : `QUESTION AUDIT: ${total} issues found across ${qTotal} questions`);
console.log(`====================================================`);
