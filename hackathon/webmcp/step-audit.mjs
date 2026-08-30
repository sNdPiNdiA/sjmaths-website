/**
 * step-audit.mjs
 *
 * Verifies EACH of the 11 Student-Journey steps against ALL 43 topics / 14 chapters,
 * not just the scripted Chapter 4 topic — simulating a judge or live agent picking
 * anything off-script.
 */
import { readFileSync, existsSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createWebMCPTools } from "./src/webmcp-tools.js";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const catalogPath = path.join(root, "hackathon", "webmcp", "data", "class-10", "mathematics", "cbse-class-10-mathematics.json");
const catalog = JSON.parse(readFileSync(catalogPath, "utf8"));

const allTopics = [];
for (const ch of catalog.chapters || []) {
  for (const t of ch.topics || []) allTopics.push({ ...t, chapterId: ch.id, chapterTitle: ch.title });
}
console.log(`Auditing ${allTopics.length} topics across ${catalog.chapters.length} chapters, step by step\n`);

const tools = createWebMCPTools(catalog);

const fails = Object.fromEntries(Array.from({ length: 11 }, (_, i) => [i + 1, []]));
const pointerFails = [];
const catalogIds = new Set(allTopics.map(t => t.id));
const LEAK_KEYS = ["correct_strategy_index", "is_correct", "correct_answer", "correct_index", "correct_option_index", "option_details"];

function check(step, topicId, cond, msg) {
  if (!cond) fails[step].push(`${topicId}: ${msg}`);
}

// ---- STEP 1: curriculum outline totals vs actual chapter contents ----
{
  const o = await tools.executeTool("get_curriculum_outline", {});
  const actual = o.chapters.reduce((s, c) => s + c.topic_count, 0);
  check(1, "curriculum", o.curriculum_id === "cbse-class-10-mathematics", `id=${o.curriculum_id}`);
  check(1, "curriculum", o.total_chapters === 14 && o.chapters.length === 14, "chapter totals mismatch");
  check(1, "curriculum", o.total_topics === 43 && actual === 43, `declared ${o.total_topics} vs actual ${actual}`);
}

// ---- STEP 2: every chapter lists its topics, every data_path file exists ----
for (const ch of catalog.chapters || []) {
  const ct = await tools.executeTool("get_chapter_topics", { chapter_id: ch.id });
  check(2, ch.id, Array.isArray(ct.topics) && ct.topics.length === (ch.topics || []).length, "topic list mismatch");
  for (const t of ch.topics || []) {
    const file = path.join(root, t.data_path || "");
    check(2, ch.id, !!t.data_path && existsSync(file), `missing data_path file: ${t.data_path}`);
  }
}

// ---- STEP 10: exam config (topic-independent) ----
{
  const ex = await tools.executeTool("start_mastery_exam", {});
  check(10, "exam", ex.total_questions === 10 && ex.pass_percent === 60 && ex.duration_minutes === 30, "exam config");
}

let solvedExpected = 0;
for (const t of allTopics) {
  // ---- STEP 3: metadata ----
  try {
    const meta = await tools.executeTool("get_topic_metadata", { topic_id: t.id });
    check(3, t.id, meta.topic?.id === t.id && !!meta.topic?.title, "bad metadata");
    check(3, t.id, meta.topic?.stage_count === 5, `stage_count=${meta.topic?.stage_count}`);
  } catch (e) { check(3, t.id, false, e.message); }

  // ---- STEP 4: prerequisites resolve and are unmet for a fresh student ----
  try {
    const pre = await tools.executeTool("get_prerequisite_check", { topic_id: t.id });
    check(4, t.id, pre.prerequisite_count >= (t.id === allTopics[0].id ? 2 : 3), `only ${pre.prerequisite_count} prereqs`);
    check(4, t.id, pre.all_prerequisites_met === false, "fresh student shows prereqs met");
    for (const p of pre.prerequisites) {
      check(4, t.id, typeof p.mastered === "boolean", "prereq missing mastered flag");
      if (p.kind === "previous_topic") check(4, t.id, catalogIds.has(p.id), `prereq id not in catalog: ${p.id}`);
    }
  } catch (e) { check(4, t.id, false, e.message); }

  // ---- STEP 5: content loads, 5 stages, questions, zero leakage ----
  let content = null;
  try {
    content = await tools.executeTool("get_topic_content", { topic_id: t.id, mode: "assessment" });
    check(5, t.id, content.content_loaded === true, "topic JSON did not load");
    check(5, t.id, content.stage_count === 5, `stage_count=${content.stage_count}`);
    check(5, t.id, content.total_question_count > 0, "no questions");
    const raw = JSON.stringify(content);
    const leaks = LEAK_KEYS.filter(k => raw.includes(`"${k}"`));
    check(5, t.id, leaks.length === 0, `answer leak: ${leaks.join(",")}`);
  } catch (e) { check(5, t.id, false, e.message); continue; }

  // ---- pointer integrity (previous/next must resolve in catalog) ----
  for (const [kind, p] of [["prev", content.previous_topic], ["next", content.next_topic]]) {
    if (p && !catalogIds.has(p.id)) pointerFails.push(`${t.id} ${kind}_topic -> ${p.id}`);
  }

  // First question of the first pool drives steps 6-8
  const q = content.question_types?.[0]?.pool?.[0];
  if (!q?.id) { check(6, t.id, false, "no question to evaluate"); continue; }

  // Real answer key straight from the topic JSON on disk
  const disk = JSON.parse(readFileSync(path.join(root, t.data_path), "utf8"));
  const diskQ = (disk.question_types || []).flatMap(x => x.pool || []).find(x => x.id === q.id);
  const key = diskQ?.steps?.[0]?.correct_strategy_index;
  check(6, t.id, typeof key === "number", "answer key missing on disk");

  // ---- STEP 6: wrong attempt is validated, streak -> 1 ----
  try {
    const wrong = await tools.executeTool("evaluate_practice", { topic_id: t.id, question_id: q.id, selected_index: 99 });
    check(6, t.id, wrong.validated_against_content === true, "not validated against content");
    check(6, t.id, wrong.is_correct === false, "wrong attempt reported correct");
    check(6, t.id, wrong.error_streak === 1, `streak=${wrong.error_streak}`);
  } catch (e) { check(6, t.id, false, e.message); }

  // ---- STEP 7: hint level 1 is conceptual with real text ----
  try {
    const hint = await tools.executeTool("get_hint", { topic_id: t.id, question_id: q.id, current_level: 0 });
    check(7, t.id, hint.hint_level === 1 && hint.hint_type === "conceptual", "level/type wrong");
    check(7, t.id, typeof hint.hint_text === "string" && hint.hint_text.length > 3, "hint text missing (generic fallback)");
  } catch (e) { check(7, t.id, false, e.message); }

  // ---- STEP 8: correct attempt validated against the REAL key, streak -> 0 ----
  if (typeof key === "number") {
    try {
      const right = await tools.executeTool("evaluate_practice", { topic_id: t.id, question_id: q.id, selected_index: key });
      check(8, t.id, right.validated_against_content === true && right.is_correct === true, "correct attempt not validated");
      check(8, t.id, right.error_streak === 0, `streak=${right.error_streak} after correct`);
      solvedExpected++;
    } catch (e) { check(8, t.id, false, e.message); }
  }

  // ---- STEP 9: next action responds from live state ----
  try {
    const na = await tools.executeTool("get_next_learning_action", { topic_id: t.id });
    check(9, t.id, typeof na.action === "string" && na.action.length > 0 && typeof na.reason === "string", "missing action/reason");
  } catch (e) { check(9, t.id, false, e.message); }
}

// ---- STEP 11: progress totals after the full sweep ----
{
  const pr = await tools.executeTool("get_learning_progress", {});
  check(11, "progress", pr.total_chapters === 14 && pr.total_topics === 43, "totals changed");
  check(11, "progress", pr.questions_solved === solvedExpected, `solved ${pr.questions_solved} != expected ${solvedExpected}`);
  check(11, "progress", pr.topics_completed === 0, "audit should not complete topics");
}

// ---- Report ----
const stepNames = {
  1: "get_curriculum_outline", 2: "get_chapter_topics", 3: "get_topic_metadata",
  4: "get_prerequisite_check", 5: "get_topic_content", 6: "evaluate_practice (wrong)",
  7: "get_hint", 8: "evaluate_practice (correct)", 9: "get_next_learning_action",
  10: "start_mastery_exam", 11: "get_learning_progress"
};
let total = 0;
for (let s = 1; s <= 11; s++) {
  const n = fails[s].length;
  total += n;
  console.log(`STEP ${String(s).padStart(2)} ${stepNames[s].padEnd(28)} ${n === 0 ? "PASS (all topics/chapters)" : `FAIL x${n}`}`);
  for (const f of fails[s].slice(0, 10)) console.log(`        !! ${f}`);
  if (fails[s].length > 10) console.log(`        ... and ${fails[s].length - 10} more`);
}
console.log(`POINTER INTEGRITY ${pointerFails.length === 0 ? "PASS (all prev/next resolve)" : `FAIL x${pointerFails.length}`}`);
for (const f of pointerFails.slice(0, 10)) console.log(`        !! ${f}`);
console.log(`\n====================================================`);
console.log(total === 0 && pointerFails.length === 0
  ? "STEP AUDIT: all 11 steps hold for ALL 43 topics / 14 chapters"
  : `STEP AUDIT: ${total} step failures, ${pointerFails.length} broken pointers`);
console.log(`====================================================`);
