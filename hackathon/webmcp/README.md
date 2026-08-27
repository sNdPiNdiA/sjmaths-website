# SJMaths WebMCP — AI-Native Mathematics Learning

This directory contains the **SJMaths WebMCP Prototype**, demonstrating how static mathematics curriculum is transformed into an intelligent, autonomous, and safe AI learning engine directly within the browser using the **Web Model Context Protocol (WebMCP)** standard.

---

## 1. Problem
Traditional educational websites store learning materials as static HTML pages or flat JSON files. When autonomous AI coding assistants and browser agents interact with these platforms, they face critical limitations:
- **Lack of Pedagogical Structure:** Flat question arrays lack explicit prerequisite graphs, skill tagging, and cognitive scaffolding stages.
- **Assessment Leakage:** LLM tutors with direct access to page content frequently leak answer keys and complete derivations prematurely to students.
- **Absence of Adaptive Loops:** Static pages cannot programmatically guide AI agents through diagnostic checks, error streak detection, progressive multi-tier hints, and targeted remediation.

---

## 2. Solution
SJMaths WebMCP introduces the **Learning-Topic Architecture** paired with a browser-native WebMCP tool layer. Rather than scraping static DOM elements, AI agents interact with 8 declarative tools registered directly through the browser's `document.modelContext` API.

---

## 3. Architecture

```
Production SJMaths
        │
        │ (Existing verified educational corpus)
        ▼
Learning-Topic v2 JSON (chapter-4-data-v2.json)
        │
        ▼
Browser-Safe Learning Engine (webmcp-tools.js + state-store.js)
        │
        ▼
WebMCP Registration (webmcp-register.js via document.modelContext)
        │
        ▼
8 Agent Tools (Sanitized Assessment & Progress Interface)
        │
        ▼
AI Agent (Gemini / Claude via Model Context Protocol)
        │
        ▼
Adaptive Learning (Diagnostic → Guided Practice → Hint → Remediation → Mastery)
```

---

## 4. The 8 WebMCP Tools

| Tool Name | Purpose (One-Sentence Summary) |
| :--- | :--- |
| **`get_topic_outline`** | Returns high-level curriculum outline, units, and skill list for Class 10 Quadratic Equations. |
| **`get_unit_content`** | Retrieves instructional materials, core concepts, formulas, and practice items with configurable answer suppression. |
| **`get_prerequisite_check`** | Delivers diagnostic precheck questions to test prerequisite readiness before unlocking unit instruction. |
| **`evaluate_unit_practice`** | Evaluates student answers, tracks attempt history, and triggers adaptive remediation rules on repeated errors. |
| **`get_hint`** | Delivers progressive 3-tier scaffolding (Level 1: Conceptual cue, Level 2: Procedural step, Level 3: Full solution). |
| **`get_next_learning_action`** | Inspects learner state and error streaks to recommend the optimal next pedagogical learning action. |
| **`start_mastery_exam`** | Serves the 10-question chapter mastery gate exam with all answer keys and solution derivations strictly suppressed. |
| **`get_learning_progress`** | Summarizes overall student progress, completed units, mastered skills, and mastery exam readiness. |

---

## 5. Assessment Safety & Answer Sanitization

During initial testing with native Gemini agents, an assessment leakage vector was identified: when an agent evaluated an incorrect answer, verbose diagnostic feedback revealed the answer clue (`"a must be non-zero"`). 

To enforce strict assessment integrity:
- **Assessment Mode Answer Suppression:** `correct_index` and `solution` fields are automatically stripped in `assessment` mode across all retrieval and precheck tools.
- **Sanitized Evaluation Feedback:** Incorrect submissions return generic, non-revealing guidance (`"Incorrect. Review the prerequisite concept or request a hint."`).
- **Progressive Assistance:** Help is gated behind explicit `get_hint()` levels, preventing agents from inadvertently spoiling solutions.

---

## 6. Adaptive Learning & Evidence-Based Skill Mastery

The prototype implements a complete cognitive feedback loop with evidence-based skill evaluation:
$$\text{Diagnosis} \longrightarrow \text{Practice} \longrightarrow \text{Evaluation} \longrightarrow \text{Error Streak Detection} \longrightarrow \text{Remediation} \longrightarrow \text{Hints} \longrightarrow \text{Progress}$$

- **Prerequisite Diagnostic:** Enforces readiness checks before starting new units (diagnostic prechecks never award mastery).
- **Evidence-Based Mastery Policy:** A skill transition to `mastered` status requires:
  1. At least **2 distinct questions** answered correctly for that skill.
  2. At least **1 of those correct answers** from higher problem stages (`independent_solution` or `transfer_mastery`).
  3. Guided-practice success alone is insufficient for skill mastery.
- **Error Streak Detection:** Automatically flags when a student makes $\ge 2$ consecutive errors.
- **Remediation Directives:** Directs struggling learners to specific formula review cards.
- **State Versioning:** Student state uses `state_version: 2` with automatic legacy state migration and in-memory fallback.

---

## 7. Verified Empirical Evidence

- **Native WebMCP Registration:** All 8 tools register cleanly via `document.modelContext.registerTool({ name, description, inputSchema, execute })`.
- **Autonomous Tool Discovery:** Verified that Gemini successfully selects and executes `get_topic_outline` and `get_prerequisite_check` from natural-language prompts.
- **Automated Test Coverage:** 91/91 automated test assertions passing in [`hackathon/webmcp/src/test-runner.js`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/src/test-runner.js).
- **Evidence-Based Mastery Engine:** Verified across guided, independent, transfer, and diagnostic precheck test suites.
- **LaTeX Math Rendering:** MathJax 3 dynamic typesetting renders mathematical formulas seamlessly across all dynamic UI elements.
- **Production Isolation:** 100% of production files (`class-10-maths/chapter-4-data.json`, production HTML/CSS/JS, `firebase.json`, `_redirects`) remain untouched.

---

## 8. Demonstration

Open the standalone, judge-facing demonstration page in any modern browser:
👉 **[`hackathon/webmcp/demo/index.html`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/demo/index.html)**

For a guided 2–3 minute walkthrough, see:
📄 **[`hackathon/webmcp/docs/demo-script.md`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/docs/demo-script.md)**

---

## 9. Repository Structure

```
hackathon/webmcp/
├── README.md                           # Master project documentation (this file)
├── demo/
│   └── index.html                      # Interactive judge-facing demonstration page
├── docs/
│   ├── architecture.md                 # Learning-Topic & WebMCP architecture specs
│   ├── demo-script.md                  # 2–3 minute live judge demonstration script
│   └── migration-audit.md              # Full content parity & skill mapping audit report
├── data/
│   └── chapter-4/
│       └── chapter-4-data-v2.json      # Audited Class 10 Chapter 4 Learning-Topic dataset
└── src/
    ├── state-store.js                  # Client-side student state manager (State Version 2)
    ├── webmcp-tools.js                 # Browser-safe implementation of the 8 tools
    ├── webmcp-register.js              # Native document.modelContext registration adapter
    └── test-runner.js                  # Automated test verification suite
```

---

## 10. Future Permanent Integration Roadmap

This prototype validates **Class 10 Chapter 4 (Quadratic Equations)** as the pilot for SJMaths' permanent AI-native curriculum. 

Following validation:
1. **Curriculum-Wide Rollout:** The remaining 14 chapters of Class 10 Mathematics and senior secondary modules will be converted to the Learning-Topic JSON architecture.
2. **Permanent Production Integration:** Upgrading the verified evidence-based mastery engine with cognitive difficulty weights, mastery gate verification, and spaced retrieval intervals.
3. **Zero Production Downtime:** Production legacy systems remain active throughout the validation period.
