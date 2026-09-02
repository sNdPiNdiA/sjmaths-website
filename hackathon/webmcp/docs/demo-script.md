# SJMaths WebMCP — 2–3 Minute Demonstration Script

**Demo Title:** AI-Native Mathematics Learning with WebMCP  
**Scope:** Full CBSE Class 10 Mathematics Curriculum (14 Chapters · 45 Topics)  
**Demo URL:** [`hackathon/webmcp/demo/index.html`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/demo/index.html)  
**Target Duration:** ~2 minutes 30 seconds  

---

## ⏱️ Timeline & Presentation Flow

```
[0:00 - 0:30] Problem: The Flaws of Traditional Static Curriculum & AI Tutoring
[0:30 - 1:00] Architecture: 13 WebMCP Tools & Native document.modelContext Registration
[1:00 - 1:45] Live Demo Part 1: Autonomous AI Agent in Action (Multi-Turn Goal-Driven Tutoring)
[1:45 - 2:15] Live Demo Part 2: 14-Step Student Journey, Granular Tools & Anti-Leakage
[2:15 - 2:30] Conclusion: 61/61 Tested, Browser-Native, Ready for Production
```

---

## 🎙️ Step-by-Step Spoken Script & Actions

### 1. Introduction & The Problem (0:00 – 0:30)

* **Screen View:** Open [`hackathon/webmcp/demo/index.html`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/demo/index.html). The top header is clearly visible with status badges: `13 Tools Active`, `CBSE Class 10`, `Schema v1.0.0`.
* **Spoken Script:**
  > *"Online mathematics education today is completely static — locked inside flat HTML pages or basic JSON files. When an AI agent attempts to tutor a student on traditional websites, it suffers from screen-scraping hallucinations, lacks pedagogical scaffolding, and worst of all, leaks the answer keys when students ask for hints.*  
  > *Today, we present **SJMaths WebMCP**: an AI-native mathematics learning architecture that turns an entire Class 10 curriculum into an interactive, secure canvas for autonomous AI agents directly within the browser."*

---

### 2. Architecture & WebMCP Registration (0:30 – 1:00)

* **Screen Action:** Highlight the **Platform Stats** (14 Chapters, 45 Topics, 85 Skills, 13 Tools, 100% Client-Side) and the **14-Step Interactive Student Journey** in the left panel.
* **Spoken Script:**
  > *"Instead of relying on a complex server backend, SJMaths WebMCP is 100% browser-native. Using the Web Model Context Protocol standard, we register **13 declarative mathematical tools** directly into `document.modelContext`.*  
  > *These tools allow an AI agent to query curriculum outlines, verify prerequisite skills, fetch isolated concepts, inspect worked models, load secure practice questions, evaluate multi-step attempts, and deliver 3-tier progressive hints."*

---

### 3. Live Demo Part 1: Autonomous Agent Mode (1:00 – 1:45)

* **Screen Action:** In the **Autonomous Live Agent Mode** panel:
  1. Click **"🤖 Run Agent"** on the prompt: *"Guide a Class 10 student named Priya through mastering 'Solving by Factorisation' in Chapter 4: Quadratic Equations. Discover curriculum, check prerequisites, evaluate attempts, give progressive hints when stuck, and track progress."*
  2. Watch the live agent execution log stream real-time tool calls (`get_curriculum_outline` $\rightarrow$ `get_prerequisite_check` $\rightarrow$ `get_topic_concepts` $\rightarrow$ `evaluate_practice` $\rightarrow$ `get_hint` $\rightarrow$ `get_next_learning_action`).
  3. Type follow-up `"ok next"` and demonstrate **Multi-Turn Persistent Chat**.
* **Spoken Script:**
  > *"Watch our autonomous agent in action. Given a high-level tutoring goal, the agent dynamically chooses tools: first inspecting curriculum prerequisites, delivering core concepts, evaluating Priya's practice choice, and intelligently deciding to provide a conceptual hint when she struggles. Even better, our agent maintains full multi-turn conversational memory, allowing natural follow-up tutoring seamlessly."*

---

### 4. Live Demo Part 2: 14-Step Student Journey & Anti-Leakage (1:45 – 2:15)

* **Screen Action:** In the **Student Journey Demo** panel on the left:
  1. Click **"▶ Run Full Journey"** to watch the automated 14-step flow execute.
  2. Click **Step 5 (`get_topic_concepts`)** and **Step 6 (`get_worked_examples`)** to show granular content delivery.
  3. Highlight **Step 7 (`get_practice_questions`)** showing that in assessment mode, `correct_strategy_index` and `solution` are completely suppressed.
* **Spoken Script:**
  > *"Every problem in our curriculum follows a **3-Stage Cognitive Typology**: Strategy Choice $\rightarrow$ Guided Calculation $\rightarrow$ Notebook Solve. Crucially, our tools enforce an Anti-Leakage policy: in assessment mode, all answer keys are strictly stripped, ensuring the agent acts as an honest proctor."*

---

### 5. Conclusion & Verification (2:15 – 2:30)

* **Screen Action:** Briefly display the terminal showing the **61/61 passing edge-case test suite**.
* **Spoken Script:**
  > *"SJMaths WebMCP is backed by an exhaustive test suite with 100% pass rates across 61 edge-case assertions. It is lightweight, zero-backend, and fully generic across all 14 chapters of CBSE Class 10. Thank you!"*
