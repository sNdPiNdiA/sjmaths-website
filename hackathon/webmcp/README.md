# SJMaths WebMCP - AI-Native Mathematics Learning

This directory contains the **SJMaths WebMCP Prototype**, demonstrating how static mathematics curriculum is transformed into an intelligent, autonomous, and safe AI learning engine directly within the browser using the **Web Model Context Protocol (WebMCP)** standard.

---

## 1. Problem

Traditional educational websites store learning materials as static HTML pages or flat JSON files. When autonomous AI coding assistants and browser agents interact with these platforms, they face critical limitations:

- **Lack of Pedagogical Structure:** Flat question arrays lack explicit prerequisite graphs, skill tagging, and cognitive scaffolding stages.
- **Assessment Leakage:** LLM tutors with direct access to page content frequently leak answer keys and complete derivations prematurely to students.
- **Absence of Adaptive Loops:** Static pages cannot programmatically guide AI agents through diagnostic checks, error streak detection, progressive multi-tier hints, and targeted remediation.

---

## 2. Solution

SJMaths WebMCP introduces the **Learning-Topic Architecture** paired with a browser-native WebMCP tool layer. Rather than scraping static DOM elements, AI agents interact with 10 declarative tools registered directly through the browser WebMCP `navigator.modelContext` API (with `window`/`document` fallbacks for polyfills).

---

## 3. Architecture

```
Production SJMaths
        |
        | (Existing verified educational corpus)
        V
Learning-Topic v4.0.1 JSON (cbse-class-10-mathematics.json)
        |
        V
Browser-Safe Learning Engine (webmcp-tools.js + state-store.js)
        |
        V
WebMCP Registration (webmcp-register.js via document.modelContext)
        |
        V
10 Agent Tools (Sanitized Assessment & Progress Interface)
        |
        V
AI Agent (Gemini / any function-calling LLM via WebMCP)
        |
        V
Adaptive Learning (Diagnostic -> Guided Practice -> Hint -> Remediation -> Mastery)
```

---

## 4. The 10 WebMCP Tools

| Tool Name | Purpose (One-Sentence Summary) |
| :--- | :--- |
| **`get_curriculum_outline`** | Returns complete CBSE Class 10 curriculum with 14 chapters and 43 topics. |
| **`get_chapter_topics`** | Retrieves all topics for a specific chapter with metadata. |
| **`get_topic_metadata`** | Returns metadata for a specific topic including data path and stage count. |
| **`get_topic_content`** | Retrieves topic content with configurable answer suppression for assessment. |
| **`get_prerequisite_check`** | Returns prerequisite microlearning modules for foundational concepts. |
| **`evaluate_practice`** | Evaluates student answers, tracks attempts, and triggers remediation on errors. |
| **`get_hint`** | Delivers progressive 3-tier scaffolding (Conceptual, Procedural, Solution). |
| **`get_next_learning_action`** | Recommends optimal next pedagogical action based on student state. |
| **`start_mastery_exam`** | Initializes the CBSE Class 10 mastery exam with solutions suppressed. |
| **`get_learning_progress`** | Summarizes overall progress, completed topics, mastered skills, and exam readiness. |

---

## 5. Assessment Safety & Answer Sanitization

To enforce strict assessment integrity:

- **Assessment Mode Answer Suppression:** Solutions and correct indices are automatically stripped in `assessment` mode.
- **Study Mode:** Full solutions available only when explicitly requested.
- **Progressive Hints:** 3-tier hint system prevents premature answer revelation.

---

## 6. Evidence-Based Mastery Engine

- **State Version 3:** Updated for Schema v4.0.1 with chapter/topic tracking.
- **Skill Mastery Policy:** Requires 2+ distinct questions with at least 1 from independent/transfer stages.
- **Error Streak Detection:** Automatically flags when a student makes 2+ consecutive errors.
- **Remediation Directives:** Directs struggling learners to prerequisite modules.

---

## 7. Verified Empirical Evidence

- **Native WebMCP Registration:** All 10 tools register cleanly via `navigator.modelContext.registerTool()` (with `window`/`document` fallbacks).
- **Schema v4.0.1 Compliance:** Full alignment with Universal Schema v4.0.1.
- **Curriculum Coverage:** Complete CBSE Class 10 Mathematics (14 chapters, 43 topics).
- **Automated Test Coverage:** 82 automated test assertions.
- **LaTeX Math Rendering:** MathJax 3 dynamic typesetting.

---

## 8. Demonstration

Open the standalone, judge-facing demonstration page in any modern browser:

**[hackathon/webmcp/demo/index.html](demo/index.html)**

The demo includes a scripted **11-step Student Journey** (the **Run Full Journey** button auto-plays all steps) plus an optional **Live Agent Mode**, where a real LLM (Google Gemini via native function calling) autonomously drives the same 10 tools — no scripts, no button clicks. The Gemini API key is set once via the *Set key* prompt and stored only in browser `localStorage`; it is never rendered in the page.

To serve locally (recommended, so ES modules and fonts load cleanly):

```powershell
cd hackathon/webmcp/demo
python -m http.server 8080
```

---

## 9. Repository Structure

```
hackathon/webmcp/
+-- README.md                           # Master project documentation (this file)
+-- demo/
|   +-- index.html                      # Interactive judge-facing demonstration page
+-- docs/
|   +-- architecture.md                 # Learning-Topic & WebMCP architecture specs
|   +-- demo-script.md                  # Live judge demonstration script
|   +-- migration-audit.md              # Full content parity & skill mapping audit report
+-- data/
|   +-- class-10/
|       +-- mathematics/
|           +-- cbse-class-10-mathematics.json  # CBSE Class 10 curriculum catalog (Schema v4.0.1)
+-- src/
    +-- state-store.js                  # Client-side student state manager (State Version 3)
    +-- webmcp-tools.js                 # Browser-safe implementation of the 10 tools
    +-- webmcp-register.js              # Native document.modelContext registration adapter
    +-- test-runner.js                  # Automated test verification suite
```

---

## 10. Curriculum Coverage

### CBSE Class 10 Mathematics (14 Chapters, 43 topics)

| # | Chapter | Topics |
|---|---------|--------|
| 1 | Real Numbers | FTA, HCF & LCM, Proofs of Irrationality |
| 2 | Polynomials | Zeroes, Zeroes-Coefficients Relationship |
| 3 | Linear Equations | Substitution, Elimination, Graphical, Word Problems |
| 4 | Quadratic Equations | Standard Form, Factorisation, Formula, Nature, Word Problems |
| 5 | Arithmetic Progressions | nth Term, Sum, Relation, Applications |
| 6 | Triangles | Similarity, BPT, Converse BPT |
| 7 | Coordinate Geometry | Distance, Section, Midpoint |
| 8 | Trigonometry | Ratios, Values, Identities |
| 9 | Applications of Trig | Single Angle, Two Angles |
| 10 | Circles | Tangent, Proofs, Lengths |
| 11 | Areas Related to Circles | Sector, Segment |
| 12 | Surface Areas & Volumes | SA Combined, Volume Combined |
| 13 | Statistics | Mean, Median, Mode, Empirical |
| 14 | Probability | Classical, Coins/Dice/Cards, Real-Life |

### Foundations (Prerequisite Microlearning)

- Factor Pairs
- Linear Equation Transposition

---

## 11. Future Integration Roadmap

1. **Dynamic Topic Loading:** Load individual topic JSON files on-demand.
2. **Adaptive Difficulty:** Cognitive difficulty weights based on student performance.
3. **Spaced Retrieval:** Interval-based review scheduling.
4. **Multi-Class Expansion:** Extend to Classes 9, 11, and 12.