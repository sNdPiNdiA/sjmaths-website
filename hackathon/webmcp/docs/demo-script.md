# SJMaths WebMCP — 2–3 Minute Judge Demonstration Script

**Demo Title:** AI-Native Mathematics Learning with WebMCP  
**Topic:** Class 10 Mathematics · Chapter 4: Quadratic Equations  
**Demo URL:** `hackathon/webmcp/demo/index.html`  
**Duration:** ~2 minutes 45 seconds  

---

## Script Overview & Timeline

```
[0:00 - 0:30] Introduction & The Problem with Static Curriculum
[0:30 - 1:00] The Learning-Topic Architecture & Native WebMCP Registration
[1:00 - 1:40] AI Agent Discovery, Prerequisite Diagnosis & Assessment Safety
[1:40 - 2:15] Adaptive Remediation & Multi-Tier Progressive Hints
[2:15 - 2:45] Client-Side Progress Tracking & Permanent Integration Roadmap
```

---

## Detailed Demonstration Walkthrough

### 1. Introduction & The Problem (0:00 – 0:30)

* **UI State:** Demo page loaded at `hackathon/webmcp/demo/index.html`. Hero header clearly visible showing *"SJMaths · AI-Native Learning"* with green status badges: *"WebMCP: Active (8 Tools)"* and *"MathJax 3: Active"*.
* **Spoken Script:**
  > *"Hello judges. SJMaths is an open educational platform helping millions of students master mathematics. Today, educational content on the web is completely static — trapped inside HTML pages and flat JSON files. When an AI agent tries to tutor a student, it either scrapes the screen, hallucinates curriculum structure, or leaks exam answer keys. Today we are presenting SJMaths WebMCP: an AI-native mathematics learning architecture that turns structured curriculum into an interactive, agentic learning engine directly in the browser."*

---

### 2. Architecture & Native WebMCP Registration (0:30 – 1:00)

* **Action:** Scroll down slightly to show the **WebMCP Protocol & Tool Output Inspector** at the bottom, highlighting the 8 registered tool tags.
* **Expected Tool Call:** Browser initialization automatically runs `registerWebMCPTools(chapterData)` via `document.modelContext.registerTool()`.
* **Visible Result:** 8 active tool tags displayed (`get_topic_outline`, `get_unit_content`, `get_prerequisite_check`, `evaluate_unit_practice`, `get_hint`, `get_next_learning_action`, `start_mastery_exam`, `get_learning_progress`).
* **Spoken Script:**
  > *"Instead of modifying our existing production website, we created a self-contained Learning-Topic architecture. Using the W3C WebMCP standard via `document.modelContext`, the page registers 8 dedicated mathematical learning tools. An AI assistant like Gemini can autonomously inspect the curriculum outline, retrieve sanitized unit lessons, diagnose prerequisites, evaluate student responses, and provide progressive hints."*

---

### 3. AI Discovery & Prerequisite Diagnosis (1:00 – 1:40)

* **Action:** Direct attention to the main tutoring workspace displaying the diagnostic precheck question:  
  *"Standard form of quadratic eq is $ax^2+bx+c=0$. Condition on 'a' is:"* with options `$a \neq 0$`, `$a > 0$`, `$a = 1$`.
* **Expected Tool Call:** `get_prerequisite_check({ unit_id: "unit-1-standard-form-factorisation" })`
* **Visible Result:** MathJax renders LaTeX formulas cleanly. Raw JSON response in the inspector confirms `correct_index` and `solution` are strictly suppressed.
* **Spoken Script:**
  > *"Notice that before teaching new concepts, the system initiates a diagnostic check. Crucially, when our AI agent accesses the curriculum in assessment mode, all correct answers and solutions are strictly suppressed. The agent acts as a true proctor and cannot leak the answer key."*

---

### 4. Student Mistake, Remediation & Progressive Hints (1:40 – 2:15)

* **Action 1 (Student Error):** Click option **2. $a > 0$** (incorrect) and click **"Submit Answer"**.
* **Expected Tool Call 1:** `evaluate_unit_practice({ question_id: "u1-precheck", selected_index: 1 })`
* **Visible Result 1:** Red feedback banner displays: *"✗ Incorrect. Review the prerequisite concept or request a hint."* Notice that answer clues (`"a must be non-zero"`) are completely withheld. The error streak counter increments to 1.

* **Action 2 (Second Error & Remediation):** Click option **3. $a = 1$** (incorrect) and click **"Submit Answer"**.
* **Expected Tool Call 2:** `evaluate_unit_practice({ question_id: "u1-precheck", selected_index: 2 })`
* **Visible Result 2:** Red banner updates: *"✗ Incorrect... [REMEDIATION RULE TRIGGERED: Error streak ≥ 2. Reviewing formula cards recommended.]"*. The timeline highlights the **Remediate** stage, and the Error Streak turns red (streak = 2).

* **Action 3 (Progressive Hint):** Click **"Request Progressive Hint"**.
* **Expected Tool Call 3:** `get_hint({ question_id: "u1-precheck", hint_level: 1 })`
* **Visible Result 3:** Blue banner displays Level 1 Conceptual Hint: `[Level 1 - conceptual]: Recall the fundamental principle for skill "skill-identify-quadratic".`
* **Spoken Script:**
  > *"When the student makes repeated mistakes, the learning engine detects the error streak and triggers an adaptive remediation directive. Rather than giving away the answer, the student or agent can request progressive, multi-tier hints — from high-level conceptual nudges to intermediate procedural steps."*

---

### 5. Success, State Update & Future Roadmap (2:15 – 2:45)

* **Action 1 (Correct Answer):** Click option **1. $a \neq 0$** (correct) and click **"Submit Answer"**.
* **Expected Tool Call:** `evaluate_unit_practice({ question_id: "u1-precheck", selected_index: 0 })`
* **Visible Result:** Green feedback banner appears: *"✓ Correct! If a=0, it becomes linear."* The Error Streak resets to 0. The timeline advances to **2. Practice**, and the system automatically loads practice question `u1-p-1`.
* **Action 2 (Progress Update):** Click **"Next Learning Action"**.
* **Visible Result:** Next action box displays: `continue_practice: Continue active unit practice questions.` Learner progress state updates dynamically.
* **Spoken Script:**
  > *"Once the prerequisite is satisfied, the student advances seamlessly into guided practice. All progress is tracked in client-side storage without backend dependencies. This Chapter 4 prototype proves that WebMCP can transform static web curriculum into an autonomous, safe, and adaptive learning companion. Following this hackathon, we plan to roll this architecture out across all 15 chapters of the SJMaths curriculum. Thank you!"*
