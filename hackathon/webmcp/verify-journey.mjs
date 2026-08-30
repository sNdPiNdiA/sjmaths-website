import { readFileSync } from "fs";
import path from "path";
import { createWebMCPTools } from "./src/webmcp-tools.js";
import { StateStore } from "./src/state-store.js";

// Stub browser fetch with local file reads so the journey runs end-to-end in Node
globalThis.fetch = async (url) => {
  // data_path is repo-root-relative; resolve against repo root (two levels up)
  const p = url.replace(/^\//, "").split("?")[0];
  const abs = path.resolve(process.cwd(), "..", "..", p);
  try {
    const body = readFileSync(abs, "utf8");
    return { ok: true, json: async () => JSON.parse(body) };
  } catch {
    return { ok: false, status: 404, statusText: "Not Found", json: async () => null };
  }
};

const catalog = JSON.parse(readFileSync("data/class-10/mathematics/cbse-class-10-mathematics.json", "utf8"));
// Mirror the demo exactly: fresh memory-only store (resets every page load)
const stateStore = new StateStore({ useMemoryOnly: true });
const tools = createWebMCPTools(catalog, stateStore);
const TOPIC = "cbse10-quadratic-equations-solving-by-factorisation";
const CHAPTER = "chapter-4-quadratic-equations";

let pass = 0, fail = 0;
function check(label, cond, detail = "") {
  if (cond) { pass++; console.log(`  [PASS] ${label}${detail ? " — " + detail : ""}`); }
  else { fail++; console.error(`  [FAIL] ${label}${detail ? " — " + detail : ""}`); }
}

const run = (t, p) => tools.executeTool(t, p);

console.log("\nSTEP 1 — Discover the Curriculum (get_curriculum_outline)");
const outline = await run("get_curriculum_outline", {});
check("curriculum id is cbse-class-10-mathematics", outline.curriculum_id === "cbse-class-10-mathematics");
check("14 chapters", outline.total_chapters === 14 && outline.chapters.length === 14);
check("43 topics declared", outline.total_topics === 43);
const topicSum = outline.chapters.reduce((s, c) => s + c.topic_count, 0);
check("declared topic count matches actual chapter contents", topicSum === outline.total_topics, `sum=${topicSum}`);
check("schema version present", !!outline.schema_version);

console.log("\nSTEP 2 — Choose a Chapter (get_chapter_topics)");
const chTopics = await run("get_chapter_topics", { chapter_id: CHAPTER });
check("chapter 4 returned", chTopics.chapter_id === CHAPTER && chTopics.chapter_number === 4);
check("lists all 5 topics (as the card promises)", chTopics.topics.length === 5, `count=${chTopics.topics.length}`);
check("target topic present", chTopics.topics.some(t => t.id === TOPIC));
check("every topic has a valid data_path", chTopics.topics.every(t => t.data_path && t.data_path.startsWith("/learning/topics/")));

console.log("\nSTEP 3 — Preview the Topic (get_topic_metadata)");
const meta = await run("get_topic_metadata", { topic_id: TOPIC });
check("chapter context included", meta.chapter_id === CHAPTER && !!meta.chapter_title);
check("topic id/title returned", meta.topic.id === TOPIC && !!meta.topic.title);
check("5-stage path (stage_count)", meta.topic.stage_count === 5, `stage_count=${meta.topic.stage_count}`);

console.log("\nSTEP 4 — Check Readiness (get_prerequisite_check)");
const prereq = await run("get_prerequisite_check", { topic_id: TOPIC });
check("3 prerequisites (2 foundations + previous topic)", prereq.prerequisite_count === 3,
  prereq.prerequisites.map(x => x.id).join(", "));
check("not all met for a fresh student", prereq.all_prerequisites_met === false);
check("every prerequisite has a mastered flag", prereq.prerequisites.every(p => typeof p.mastered === "boolean"));

console.log("\nSTEP 5 — Open the Topic (get_topic_content, assessment)");
const content = await run("get_topic_content", { topic_id: TOPIC, mode: "assessment" });
check("content loaded", content.content_loaded === true);
check("5 learning stages", content.stage_count === 5 && (content.learning_stages || []).length === 5);
check("60 questions across pools", content.total_question_count === 60, `total=${content.total_question_count}`);
check("pool sizes match summary", (content.question_type_summary || []).every((s, i) =>
  s.pool_size === (content.question_types || [])[i]?.pool?.length));
const raw = JSON.stringify(content);
const leaked = ["correct_strategy_index", "is_correct", "option_details", "correct_answer", "solution"].filter(k => raw.includes(`"${k}"`));
check("assessment mode strips ALL answer keys", leaked.length === 0, leaked.length ? "leaked: " + leaked.join(",") : "none");

console.log("\nSTEP 6 — First Attempt: Incorrect (evaluate_practice)");
const wrong = await run("evaluate_practice", { topic_id: TOPIC, question_id: "t1_p1", selected_index: 0 });
check("validated against real answer key", wrong.validated_against_content === true);
check("is_correct is false", wrong.is_correct === false);
check("error streak incremented to 1", wrong.error_streak === 1);

console.log("\nSTEP 7 — Stuck? Get a Hint (get_hint)");
const hint = await run("get_hint", { topic_id: TOPIC, question_id: "t1_p1", current_level: 0 });
check("hint level 1 (progressive)", hint.hint_level === 1);
check("level 1 is conceptual (not the answer)", hint.hint_type === "conceptual");
check("hint text derived from the question's own steps", typeof hint.hint_text === "string" && hint.hint_text.length > 0,
  JSON.stringify(hint.hint_text));

console.log("\nSTEP 8 — Retry: Correct (evaluate_practice)");
const right = await run("evaluate_practice", { topic_id: TOPIC, question_id: "t1_p1", selected_index: 2 });
check("validated against real answer key", right.validated_against_content === true);
check("is_correct is true", right.is_correct === true);
check("error streak reset to 0 (as the card promises)", right.error_streak === 0);
// Demo post-action: mark topic complete + set current topic (mirrors demo step 8 `post`)
const st = stateStore.getState();
st.current_topic_id = TOPIC;
stateStore.saveState(st);
stateStore.completeTopic(TOPIC);

console.log("\nSTEP 9 — What's Next? (get_next_learning_action)");
const next = await run("get_next_learning_action", { topic_id: TOPIC });
check("returns an action from live state", ["practice", "hint", "remediate", "advance"].includes(next.action), `action=${next.action}`);
check("reflects reset error streak", next.error_streak === 0);
check("includes a reason", !!next.reason);

console.log("\nSTEP 10 — Mastery Exam (start_mastery_exam)");
const exam = await run("start_mastery_exam", {});
check("10-question exam", exam.total_questions === 10);
check("60% pass mark", exam.pass_percent === 60);
check("timed (30 minutes)", exam.duration_minutes === 30);

console.log("\nSTEP 11 — Track Progress (get_learning_progress)");
const progress = await run("get_learning_progress", { curriculum_id: "cbse-class-10-mathematics" });
check("nonzero progress after the journey", progress.overall_progress_percent > 0, `${progress.overall_progress_percent}%`);
check("1 topic completed", progress.topics_completed === 1);
check("1 question solved", progress.questions_solved === 1);
check("current topic is the one she just mastered", progress.current_topic_id === TOPIC);
check("0 chapters completed (exam not taken yet)", progress.chapters_completed === 0);
check("totals intact (14 chapters / 43 topics)", progress.total_chapters === 14 && progress.total_topics === 43);

console.log("\nSanity — study mode DOES include answers");
const study = await run("get_topic_content", { topic_id: TOPIC, mode: "study" });
const leakStudy = JSON.stringify(study.question_types || {}).match(/"correct_strategy_index"/);
check("study mode keeps correct_strategy_index", !!leakStudy);

console.log(`\n====================================================`);
console.log(`JOURNEY VERIFICATION: ${pass} passed, ${fail} failed`);
console.log(`====================================================`);
process.exit(fail ? 1 : 0);
