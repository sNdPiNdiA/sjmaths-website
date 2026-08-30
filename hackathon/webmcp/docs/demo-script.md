# SJMaths WebMCP — 2–3 Minute Judge Demonstration Script

**Demo Title:** AI-Native Mathematics Learning with WebMCP  
**Topic:** Class 10 Mathematics · Chapter 4: Quadratic Equations  
**Demo URL:** `hackathon/webmcp/demo/index.html`  
**Duration:** ~2 minutes 45 seconds  
**Persona:** Priya, a Class 10 student mastering Quadratic Equations  

---

## Script Overview & Timeline

```
[0:00 - 0:25] Introduction & The Problem with Static Curriculum
[0:25 - 0:50] The Learning-Topic Architecture & Native WebMCP Registration
[0:50 - 2:10] The Student Journey: Discovery → Practice → Hint → Retry (11 Steps)
[2:10 - 2:30] Mastery Exam & Client-Side Progress Tracking
[2:30 - 2:45] Closing & Permanent Integration Roadmap
```

---

## Recording Tips

* Use the **▶ Run Full Journey** button (top of the Student Journey card) to auto-play all 11 steps sequentially (~1.6 s each) — perfect for hands-free recording.
* Alternatively, click each step individually and narrate.
* The right-hand **Tool Response** panel shows the exact JSON returned by each tool, with the invoked call shown in the toolbar chip and a **Copy** button for pasting raw output.
* If you plan to show **Live Agent Mode**, click **Set key** before recording and paste your Gemini API key once — it is stored in browser `localStorage` and never visible on screen. Clear it before sharing your screen if you prefer.
* Hard-refresh with `Ctrl + Shift + R` before recording to clear cached CSS.

---

## Detailed Demonstration Walkthrough

### 1. Introduction & The Problem (0:00 – 0:25)

* **UI State:** Demo page loaded at `hackathon/webmcp/demo/index.html`. Hero header shows *"∫ SJMaths WebMCP"* with badges: *"10 Tools Active"*, *"CBSE Class 10"*, *"Schema v4.0.1"*. Platform stats visible: **14 chapters · 43 topics · 85 skills · 10 tools**.
* **Spoken Script:**
  > *"Hello judges. SJMaths is an open educational platform helping millions of students master mathematics. Today, educational content on the web is completely static — trapped inside HTML pages and flat JSON files. When an AI agent tries to tutor a student, it either scrapes the screen, hallucinates curriculum structure, or leaks exam answer keys. Today we're presenting SJMaths WebMCP: an AI-native mathematics learning architecture that turns structured curriculum into an interactive, agentic learning engine directly in the browser."*

---

### 2. Architecture & Native WebMCP Registration (0:25 – 0:50)

* **Action:** Point to the **Registered MCP Tools** panel on the right, showing all 10 registered tools.
* **Expected Tool Call:** Page initialization automatically runs `registerWebMCPTools(chapterData)` via `navigator.modelContext.registerTool()` (with `window`/`document` fallbacks).
* **Visible Result:** All 10 tool names listed: `get_curriculum_outline`, `get_chapter_topics`, `get_topic_metadata`, `get_topic_content`, `get_prerequisite_check`, `evaluate_practice`, `get_hint`, `get_next_learning_action`, `start_mastery_exam`, `get_learning_progress`.
* **Spoken Script:**
  > *"Instead of modifying our existing production website, we built a self-contained Learning-Topic architecture. Using the WebMCP standard via `navigator.modelContext`, the page registers 10 dedicated mathematical learning tools. An AI agent like Gemini can autonomously inspect the curriculum, retrieve sanitized lessons, diagnose prerequisites, evaluate responses, and deliver progressive hints — all through typed, structured tool calls instead of fragile DOM scraping."*

---

### 3. The Student Journey — 11 Steps (0:50 – 2:10)

* **Action:** Click **▶ Run Full Journey** (or step through manually). Each step's JSON response appears instantly in the Tool Response panel.

| # | Step | Tool Call | What Judges See |
|---|------|-----------|-----------------|
| 1 | Discover the Curriculum | `get_curriculum_outline` | Full CBSE Class 10 outline — 14 chapters, 43 topics |
| 2 | Choose a Chapter | `get_chapter_topics("chapter-4-quadratic-equations")` | All 5 Chapter 4 topics with metadata |
| 3 | Preview the Topic | `get_topic_metadata("...solving-by-factorisation")` | Difficulty & estimated duration before committing |
| 4 | Check Readiness | `get_prerequisite_check("...solving-by-factorisation")` | Prerequisite skill verification — **before** the topic opens |
| 5 | Open the Topic | `get_topic_content(..., "assessment")` | 5 learning stages with **solutions suppressed** |
| 6 | First Attempt: Incorrect | `evaluate_practice("t1_p1", 0, false)` | Evaluated without revealing the answer — `error_streak: 1` |
| 7 | Stuck? Get a Hint | `get_hint("t1_p1", 0)` | Level-1 conceptual hint — a nudge, not the answer |
| 8 | Retry: Correct | `evaluate_practice("t1_p1", 2, true)` | Success — **error streak resets to 0** |
| 9 | What's Next? | `get_next_learning_action(...)` | AI-recommended next action from live performance state |
| 10 | Mastery Exam | `start_mastery_exam` | Exam initialized with solutions suppressed |
| 11 | Track Progress | `get_learning_progress("cbse-class-10-mathematics")` | Completed topics, mastered skills, exam readiness |

* **Spoken Script:**
  > *"Let's follow Priya, a Class 10 student mastering Quadratic Equations. The agent first discovers the full curriculum — 14 chapters, 43 topics, 85 skills. She picks Chapter 4, and before opening a topic, the agent scouts its metadata and verifies her prerequisite skills are mastered. When she opens 'Solving by Factorisation' in assessment mode, notice the JSON — correct answers and solutions are strictly suppressed. The agent acts as a true proctor and cannot leak the answer key. She attempts a question… incorrect. The error streak ticks to one. Instead of revealing the answer, the agent requests a progressive conceptual hint. With that nudge, her retry is correct — and the error streak resets to zero. The engine then recommends her next learning action from live performance state."*

---

### 4. Mastery Exam & Progress Tracking (2:10 – 2:30)

* **Action:** Steps 10 and 11 in the journey (or click manually if narrating).
* **Expected Tool Calls:** `start_mastery_exam` → `get_learning_progress({ curriculum_id: "cbse-class-10-mathematics" })`
* **Visible Result:** Exam initialized with solutions suppressed; progress summary shows completed topics, mastered skills, and exam readiness.
* **Spoken Script:**
  > *"When she's ready, the agent can initialize a mastery exam — again with all solutions suppressed — and every bit of progress is tracked client-side in browser storage. No backend, no data leaving the student's device."*

---

### 5. Closing & Roadmap (2:30 – 2:45)

* **Spoken Script:**
  > *"This prototype proves that WebMCP can transform static web curriculum into an autonomous, safe, and adaptive learning companion — with assessment integrity enforced by the tool layer itself, not by prompting. Following this hackathon, we plan to roll this architecture out across the full SJMaths curriculum — Classes 9 through 12. Thank you!"*

---

### 6. Bonus: Live Agent Mode (if time permits, or if judges ask)

* **Setup (before recording):** Click **Set key** and paste a Gemini API key once — it is saved to browser `localStorage` and never shown on screen. A green *"API key saved — agent ready"* status confirms setup.
* **Action:** Keep the pre-filled goal (guiding Priya through *Solving by Factorisation*), then click **🤖 Run Live Agent**.
* **What Judges See:** A real LLM (default model: `gemini-3.5-flash-lite`) autonomously plans and calls the same 10 WebMCP tools via native function calling — no scripts, no button clicks. The log streams its reasoning, tool calls, and sanitized results live.
* **Spoken Script:**
  > *"And this isn't a canned demo — a real Gemini model is now driving the exact same 10 tools through native function calling. It discovers the curriculum, checks prerequisites, evaluates Priya's answers, and requests hints entirely on its own. Notice it never receives the answer key — suppression is enforced in the tool layer."*

---

## Key Talking Points (If Judges Ask Questions)

| Question | Answer |
|---|---|
| **How do you prevent answer leakage?** | `get_topic_content` and `start_mastery_exam` accept a `mode` parameter. In `assessment` mode, `correct_index` and `solution` fields are stripped at the tool layer — the agent physically cannot receive them. |
| **What if the student keeps failing?** | `evaluate_practice` tracks consecutive errors. At 2+ errors, a remediation directive is returned directing the agent to prerequisite microlearning modules. |
| **Where does state live?** | Entirely client-side (`state-store.js`, State Version 3) — persisted in browser storage, zero backend. |
| **Is this spec-conformant WebMCP?** | Yes — tools register via `navigator.modelContext.registerTool()`, with `window`/`document` fallbacks for early polyfills. |
| **How is it tested?** | 82 automated assertions in `src/test-runner.js` covering all 10 tools, input validation, state persistence, and skill mastery evaluation. |

