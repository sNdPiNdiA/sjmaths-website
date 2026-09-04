# 🎙️ SJMaths WebMCP — Video Demo Presentation Script (2–3 Minutes)

> **Speaker:** Sandeep Jaiswal (Mathematics Educator & Creator of SJMaths)  
> **Topic:** AI-Native Adaptive Mathematics Learning using the Web Model Context Protocol (WebMCP)  
> **Target Duration:** ~2 Minutes 30 Seconds  
> **Visual Reference:** Split screen (ChatGPT/WebMCP Agent on Left or Browser with `https://sjmaths.com/hackathon/webmcp/demo/` on Right showing the Live Tool Inspector & 14-Step Adaptive Path).

---

## 🎬 Video Script & Visual Actions

### **Scene 1: Introduction & The Problem (0:00 - 0:35)**
**Visual:** Camera on speaker / opening shot of SJMaths homepage (`sjmaths.com`).

> **Narration:**  
> "Hi, I'm Sandeep Jaiswal, a school mathematics teacher. Every day in my classroom, I see students struggling with the same mathematics concept in very different ways. Some students forget foundational prerequisites, while others just need a small conceptual nudge rather than someone handing them the final solution.
>
> When students try using modern AI assistants on the web, two major problems happen: either the AI immediately gives away the entire answer, killing the thinking process, or it has zero awareness of the student's actual learning state.
>
> That led me to a question: **What if an external AI agent could connect directly to our learning system via the browser, understand a student's real-time state, and adapt what happens next without expensive backends or answer leakage?**
>
> That's why we built **SJMaths with WebMCP**."

---

### **Scene 2: Discovering Curriculum & Checking Prerequisites (0:35 - 1:05)**
**Visual:** Cut to `https://sjmaths.com/hackathon/webmcp/demo/`. Show the left panel showing **Priya's Adaptive Learning Path** and the right panel showing the **WebMCP Live Tool Inspector**.

> **Narration:**  
> "Here we have Priya, a Class 10 student learning Quadratic Equations—specifically, solving by factorisation. 
> 
> Instead of scraping messy HTML or relying on static prompts, the AI agent uses **13 browser-native WebMCP tools** registered directly in `document.modelContext`.
> 
> The agent first calls `get_curriculum_outline` to discover the syllabus across all 14 CBSE chapters, identifies the topic with `get_chapter_topics`, and runs `get_prerequisite_check` to verify if Priya has mastered foundational algebra from Class 9.
> 
> These are not hard-coded prompts; they are live, typed capabilities executing in-memory in under 1 millisecond."

---

### **Scene 3: Concept Teaching, Assessment Mode & Deliberate Error (1:05 - 1:45)**
**Visual:** Click Step 5 (`get_topic_concepts`), Step 6 (`get_worked_examples`), Step 7 (`get_practice_questions`), and then Step 8 (`evaluate_practice` with incorrect choice). Show the inspector displaying latency (`<0.5ms`) and the error streak counter increasing.

> **Narration:**  
> "Next, the agent fetches core formulas and common trap warnings with `get_topic_concepts`, provides a step-by-step model using `get_worked_examples`, and moves Priya into practice.
> 
> Notice what happens here: in assessment mode, all correct answers and solutions are stripped on the client side so the AI cannot accidentally leak the key.
> 
> Now let's deliberately make a mistake—Priya selects an incorrect option."

---

### **Scene 4: Progressive Scaffolding & State Recovery (1:45 - 2:15)**
**Visual:** Click Step 9 (`get_hint` - Level 1) and Step 10 (`evaluate_practice` with correct choice). Show the intervention counter resolve to 0 and topic mastery jump to 82%.

> **Narration:**  
> "Instead of simply blurting out the answer, the agent evaluates the response using `evaluate_practice` and recognizes that the student's error streak has increased. 
> 
> It requests a Level 1 conceptual hint using `get_hint`. Priya receives a subtle hint to rethink her middle-term split, reasons through the calculation, and tries again. 
> 
> This time, she gets it right! The error streak resets, and her topic mastery dynamically updates."

---

### **Scene 5: Closed-Loop Adaptation & Conclusion (2:15 - 2:45)**
**Visual:** Click Step 12 (`get_next_learning_action`), Step 13 (`start_mastery_exam`), and show the full loop diagram at the bottom.

> **Narration:**  
> "Now comes the most important part: the agent calls `get_next_learning_action` to ask the learning engine what Priya should do next based on her updated mastery. 
> 
> The next pedagogical step isn't static text—it is causally determined by what actually happened during the lesson.
> 
> This is the core idea of **SJMaths with WebMCP**: 
> 1. The student acts.
> 2. WebMCP exposes the learning operation.
> 3. The client-side state updates.
> 4. The agent adapts the learning path.
> 
> The entire system is 100% static with zero backend server costs. It transforms static educational content into an interactive, intelligent canvas for any AI agent.
> 
> That's **SJMaths with WebMCP**. Thank you!"

---

## 📋 Quick Video Recording Checklist
- [ ] **Resolution:** 1080p (Full HD) 16:9 ratio.
- [ ] **Audio:** Clear microphone audio without background noise.
- [ ] **Demo URL:** `https://sjmaths.com/hackathon/webmcp/demo/`
- [ ] **Pacing:** Keep narration clear, natural, and enthusiastic.
- [ ] **Key Highlights to Point at:** 
  - Sub-millisecond latency (`⚡ 0.3ms`) in the Live Inspector.
  - Dynamic metric updates (`4/4 Prerequisites`, `Streak 1 -> Resolved`, `Mastery 0% -> 82%`).
  - Answer-key suppression in `get_practice_questions`.
