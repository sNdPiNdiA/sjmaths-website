# SJMaths WebMCP — AI-Native Mathematics Learning Architecture

[![Schema: Universal v1.0.0](https://img.shields.io/badge/Schema-Universal_v1.0.0-8b5cf6.svg)](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/data/class-10/mathematics/cbse-class-10-mathematics.json)
[![WebMCP: 10 Tools Active](https://img.shields.io/badge/WebMCP-10_Active_Tools-10b981.svg)](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/src/webmcp-tools.js)
[![Test Suite: 100% Passing](https://img.shields.io/badge/Tests-56%2F56_Passing-0ea5e9.svg)](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/webmcp-edge-cases.test.mjs)
[![Curriculum: CBSE Class 10](https://img.shields.io/badge/Curriculum-CBSE_Class_10_(14_Chapters)-f59e0b.svg)](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/learning/topics/)

> **OpenAI WebMCP Hackathon Submission**  
> An autonomous, browser-native mathematical learning engine that turns static CBSE Class 10 curriculum into an interactive, safe canvas for AI agents using the **Web Model Context Protocol (WebMCP)** standard.

---

## 🌟 Executive Summary

Traditional online educational materials exist as static HTML pages or flat JSON files. When autonomous AI agents (such as OpenAI models or Gemini) attempt to tutor students using traditional websites, three critical failures emerge:

1. **Assessment Leakage:** Agents with raw DOM or file access prematurely disclose solutions and answer keys.
2. **Cognitive Disconnect:** Flat question lists lack explicit prerequisite dependency trees and multi-stage pedagogical scaffolding.
3. **No Closed-Loop Agency:** Static web pages cannot programmatically guide agents through diagnostic gates, error streak detection, adaptive multi-tier hints, and targeted remediation.

**SJMaths WebMCP** solves this by implementing a **100% browser-safe, zero-backend WebMCP tool layer** directly integrated with `document.modelContext`. An AI agent acts as an autonomous tutor that diagnostically evaluates prerequisite readiness, guides students through step-by-step problem typologies, provides progressive hints without leaking answers, and adapts learning paths in real-time.

---

## 📐 Architecture Overview

```
                          ┌──────────────────────────────────────────────┐
                          │         CBSE Class 10 Curriculum              │
                          │   (14 Chapters · 45 Topics · Foundations)    │
                          └──────────────────────┬───────────────────────┘
                                                 │
                                                 ▼
                          ┌──────────────────────────────────────────────┐
                          │       Universal Schema v1.0.0 JSON           │
                          │ (Concepts · Worked Solutions · 3-Stage Pool) │
                          └──────────────────────┬───────────────────────┘
                                                 │
                                                 ▼
                          ┌──────────────────────────────────────────────┐
                          │         Browser WebMCP Tool Adapter          │
                          │     (webmcp-tools.js + state-store.js)       │
                          └──────────────────────┬───────────────────────┘
                                                 │
                                                 ▼
 ┌────────────────────────────────────────────────────────────────────────────────────────────────┐
 │                      10 Production-Ready WebMCP Tools (document.modelContext)                  │
 ├────────────────────────┬───────────────────────────┬───────────────────────────────────────────┤
 │ 📚 Curriculum Discovery │ 🛡️ Secure Assessment      │ 🎯 Pedagogical Scaffolding & Remediation  │
 │  • get_curriculum_outline│  • evaluate_practice      │  • get_prerequisite_check                 │
 │  • get_chapter_topics    │  • get_topic_content      │  • get_hint (Levels 1 → 2 → 3)            │
 │  • get_topic_metadata    │  • start_mastery_exam     │  • get_next_learning_action               │
 │                          │                           │  • get_learning_progress                  │
 └────────────────────────┴───────────────────────────┴───────────────────────────────────────────┘
                                                 │
                                                 ▼
                          ┌──────────────────────────────────────────────┐
                          │        Autonomous AI Tutor (Live Agent)       │
                          │   (Multi-Step Tool Use · Error Diagnosis)    │
                          └──────────────────────┬───────────────────────┘
                                                 │
                                                 ▼
                          ┌──────────────────────────────────────────────┐
                          │           Student Interactive Canvas          │
                          │   Strategy → Guided Calc → Notebook Solve    │
                          └──────────────────────────────────────────────┘
```

---

## 🛠️ The 10 WebMCP Tools

Every tool is strictly typed, handles edge cases gracefully, and complies with **Universal Schema v1.0.0**:

| # | Tool Identifier | Purpose & Security Guarantee |
| :---: | :--- | :--- |
| `1` | **`get_curriculum_outline`** | Returns full CBSE Class 10 catalog (14 chapters, total topics, and universal prerequisite foundations). |
| `2` | **`get_chapter_topics`** | Retrieves all structured topic modules within a specific chapter (e.g. `chapter-1-real-numbers`). |
| `3` | **`get_topic_metadata`** | Fetches metadata, learning format, stage counts, and parent chapter links for any topic. |
| `4` | **`get_topic_content`** | Delivers concepts, worked solutions, and question pools. **Assessment Safe:** In `assessment` mode (default), all answer keys and strategy choices are automatically stripped to prevent leakage. |
| `5` | **`get_prerequisite_check`** | Validates learner mastery across foundation prerequisites before unlocking advanced units. |
| `6` | **`evaluate_practice`** | Evaluates student choices against verified dataset keys, tracks attempt history, and triggers remediation flags on error streaks ($\ge 2$). |
| `7` | **`get_hint`** | Delivers 3-tier progressive hints: **Level 1** (Conceptual Cue) $\rightarrow$ **Level 2** (Procedural Hint) $\rightarrow$ **Level 3** (Solution Key). Prevents level overflow. |
| `8` | **`get_next_learning_action`** | Real-time pedagogical agent inspecting student streaks and mastery state to recommend `practice`, `hint`, `remediate`, or `advance`. |
| `9` | **`start_mastery_exam`** | Initiates chapter-wide cumulative exam (10 questions, 60% pass criteria) with answer keys suppressed. |
| `10`| **`get_learning_progress`** | Computes client-side weighted progress metrics (% completed, chapters, topics, mastered skills). |

---

## 🧠 3-Stage Cognitive Typology Architecture

Rather than naive multiple-choice questions, SJMaths WebMCP implements a **3-Stage Cognitive Scaffolding Architecture** for every problem:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: Strategy Formulation                                               │
│ Student selects the correct mathematical strategy / first step from 4       │
│ carefully balanced options designed around common conceptual misconceptions.│
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2: Guided Calculation                                                 │
│ Student executes the numerical arithmetic (e.g. prime divisor & quotient)  │
│ with dual-step vertical math stacking and real-time validation.             │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3: Notebook Solve & Self-Audit                                        │
│ Student writes out the full proof / derivation in their physical notebook   │
│ and performs a structured self-audit against standard CBSE rubric checklists│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔒 Assessment Integrity & Anti-Leakage System

When AI models interact directly with curriculum content, they frequently leak answers when students ask for hints. SJMaths WebMCP enforces a multi-layer security model:

1. **Automatic Answer Stripping:** `get_topic_content` strips `is_correct`, `correct_strategy_index`, `correct_index`, `correct_answer`, `solution`, and `explanation` by default.
2. **Progressive Hint Gating:** The agent cannot access Level 3 solutions without stepping through Level 1 (Conceptual) and Level 2 (Procedural).
3. **Isolated State Execution:** Question states are keyed by `topic_id:question_id` to prevent cross-topic state collisions in multi-unit study sessions.

---

## 📊 Comprehensive Test Suite & Edge-Case Audit

An automated, cross-tool test harness verifies 100% resilience across all edge cases:

```bash
# Run the exhaustive WebMCP Edge Case Test Suite
node hackathon/webmcp/webmcp-edge-cases.test.mjs
```

### Benchmark Results (56 / 56 Passing):
- **Suite 1: Tool Registry & Dispatcher** (Missing tools, empty strings, null inputs) $\rightarrow$ `PASS`
- **Suite 2: Curriculum Outline** (Schema 1.0.0 compliance, 14 chapters) $\rightarrow$ `PASS`
- **Suite 3 & 4: Chapter & Topic Metadata** (Invalid IDs, missing params, foundations resolution) $\rightarrow$ `PASS`
- **Suite 5: Topic Content & Answer Stripping** (No answer leaks in assessment mode) $\rightarrow$ `PASS`
- **Suite 6: Prerequisite Graph & Mastery** (Unmet prerequisite tracking & skill resolution) $\rightarrow$ `PASS`
- **Suite 7: Practice Evaluation** (Correct vs incorrect scoring, error streak counter, remediation trigger) $\rightarrow$ `PASS`
- **Suite 8: Multi-Tier Hints** (Level 1 $\rightarrow$ Level 2 $\rightarrow$ Level 3 with bounds clamping at 3) $\rightarrow$ `PASS`
- **Suite 9: Pedagogical Agent** (State transitions: practice $\rightarrow$ hint $\rightarrow$ remediate $\rightarrow$ advance) $\rightarrow$ `PASS`
- **Suite 10: Mastery Exam & Progress** (Weighted completion math, session logging) $\rightarrow$ `PASS`
- **Suite 11: Full Catalog Crawl** (Exhaustive verification of all 45 topics) $\rightarrow$ `PASS`

---

## 🚀 Live Interactive Demo

Try the live judge-facing demonstration in any web browser:
👉 **[`hackathon/webmcp/demo/index.html`](file:///c:/Users/sande/Documents/GitHub/sjmaths-website/hackathon/webmcp/demo/index.html)**

### Key Demo Features:
- **Autonomous Live Agent Mode:** Enter a natural-language goal (e.g., *"Assess student Priya on Chapter 1 Real Numbers and provide hints if she makes errors"*). The agent uses WebMCP tools autonomously in a real-time execution loop.
- **Interactive Student Journey:** Walk through a 5-step simulated student journey demonstrating prerequisite checks, strategy choices, error streak detection, and hint requests.
- **Real-Time Tool Inspector:** View live JSON payloads, input schemas, and execution responses for every tool call.

---

## 📂 Repository Structure

```
hackathon/webmcp/
├── README.md                           # Master WebMCP documentation (this file)
├── webmcp-edge-cases.test.mjs          # Exhaustive 56-assertion edge case test suite
├── data/
│   └── class-10/mathematics/
│       └── cbse-class-10-mathematics.json  # Universal Schema v1.0.0 curriculum catalog
├── demo/
│   └── index.html                      # Interactive judge-facing demonstration UI
├── docs/
│   ├── architecture.md                 # Technical specification of WebMCP architecture
│   ├── demo-script.md                  # 2–3 minute video presentation walkthrough
│   └── migration-audit.md              # Content parity & migration audit report
└── src/
    ├── webmcp-tools.js                 # 10 Browser-safe WebMCP tools implementation
    ├── webmcp-register.js              # Native document.modelContext registration adapter
    ├── state-store.js                  # Client-side student state manager (State Version 2)
    ├── learning-engine.js              # Generic browser learning engine
    └── topic-convert.js                # Browser-safe dataset-to-unit converter
```

---

## 🏆 Submission Highlights

- **Standard Compliance:** Native implementation of W3C `document.modelContext` / WebMCP specification.
- **Zero Backend Dependencies:** 100% Vanilla JavaScript, runnable offline or via static web server.
- **True Pedagogical Depth:** Full CBSE Class 10 curriculum coverage with 3-Stage Typologies, not toy examples.
- **Security by Design:** Guaranteed zero answer-key leakage during autonomous agent tutoring.
