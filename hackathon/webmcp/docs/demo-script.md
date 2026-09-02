# SJMaths WebMCP — 2–3 Minute Judge Demonstration Script

**Demo Title:** AI-Native Mathematics Learning with WebMCP  
**Scope:** Full CBSE Class 10 Mathematics Curriculum (14 Chapters · 45 Topics)  
**Demo URL:** [`hackathon/webmcp/demo/index.html`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/demo/index.html)  
**Target Duration:** ~2 minutes 30 seconds  

---

## ⏱️ Timeline & Presentation Flow

```
[0:00 - 0:30] Problem: The Flaws of Traditional Static Curriculum & AI Tutoring
[0:30 - 1:00] Architecture: 10 WebMCP Tools & Native document.modelContext Registration
[1:00 - 1:45] Live Demo Part 1: Autonomous AI Agent in Action (Goal-Driven Tutoring)
[1:45 - 2:15] Live Demo Part 2: 3-Stage Typology, Anti-Leakage & Progressive Hints
[2:15 - 2:30] Conclusion: 100% Tested, Browser-Native, Ready for Production
```

---

## 🎙️ Step-by-Step Spoken Script & Actions

### 1. Introduction & The Problem (0:00 – 0:30)

* **Screen View:** Open [`hackathon/webmcp/demo/index.html`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/demo/index.html). The top header is clearly visible with status badges: `10 Tools Active`, `CBSE Class 10`, `Schema v1.0.0`.
* **Spoken Script:**
  > *"Hello judges. Online mathematics education today is completely static — locked inside flat HTML pages or basic JSON files. When an AI agent attempts to tutor a student on traditional websites, it suffers from screen-scraping hallucinations, lacks pedagogical scaffolding, and worst of all, leaks the answer keys when students ask for hints.*  
  > *Today, we present **SJMaths WebMCP**: an AI-native mathematics learning architecture that turns an entire Class 10 curriculum into an interactive, secure canvas for autonomous AI agents directly within the browser."*

---

### 2. Architecture & WebMCP Registration (0:30 – 1:00)

* **Screen Action:** Highlight the **Platform Stats** (14 Chapters, 45 Topics, 10 Tools, 100% Client-Side) and the **Registered WebMCP Tools** in the right-hand panel.
* **Spoken Script:**
  > *"Instead of relying on a complex server backend, SJMaths WebMCP is 100% browser-native. Using the Web Model Context Protocol standard, we register **10 declarative mathematical tools** directly into `document.modelContext`.*  
  > *These tools allow an AI agent to query curriculum outlines, verify prerequisite skills, fetch sanitized content without answer keys, evaluate multi-step practice, and deliver 3-tier progressive hints."*

---

### 3. Live Demo Part 1: Autonomous Agent Mode (1:00 – 1:45)

* **Screen Action:** In the **Autonomous Live Agent Mode** panel:
  1. Click **"🤖 Run Agent"** on the prompt: *"You are an AI Math Tutor. Assess student Priya on Chapter 1 Real Numbers (FTA). Check prerequisites, evaluate her attempt on Question 1 Step 1, provide Level 1 hint if incorrect, and recommend next action."*
  2. Watch the live agent execution log stream real-time tool calls (`get_curriculum_outline` $\rightarrow$ `get_prerequisite_check` $\rightarrow$ `evaluate_practice` $\rightarrow$ `get_hint` $\rightarrow$ `get_next_learning_action`).
* **Spoken Script:**
  > *"Watch our autonomous agent in action. Given a high-level tutoring goal, the agent dynamically chooses tools: first inspecting the curriculum outline, checking whether Priya has mastered foundational prerequisites, evaluating her practice choice, and intelligently deciding to provide a conceptual hint when she struggles — all in a single coordinated loop without human intervention."*

---

### 4. Live Demo Part 2: 3-Stage Typology & Anti-Leakage (1:45 – 2:15)

* **Screen Action:** In the **Student Journey Demo** panel on the left:
  1. Click through **Step 1 (Curriculum Outline)** to show the 14 chapters.
  2. Click **Step 2 (Prerequisite Diagnostic)** to show the prerequisite graph.
  3. Click **Step 3 (Assessment-Mode Content)** to show the raw JSON in the console below, highlighting that `correct_strategy_index` and `solution` are completely suppressed.
  4. Click **Step 4 (Progressive Hint Tier 1)** showing the conceptual cue without revealing the calculation.
* **Spoken Script:**
  > *"Every problem in our curriculum follows a **3-Stage Cognitive Typology**: Strategy Choice $\rightarrow$ Guided Calculation $\rightarrow$ Notebook Solve. Crucially, our tools enforce an Anti-Leakage policy: in assessment mode, all answer keys are strictly stripped, ensuring the agent acts as an honest proctor."*

---

### 5. Conclusion & Verification (2:15 – 2:30)

* **Screen Action:** Briefly display the terminal showing the **56/56 passing edge-case test suite**.
* **Spoken Script:**
  > *"SJMaths WebMCP is backed by an exhaustive test suite with 100% pass rates across 56 edge-case assertions. It is lightweight, zero-backend, and fully generic across all 14 chapters of CBSE Class 10. Thank you!"*
