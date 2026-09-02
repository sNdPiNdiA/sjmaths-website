# Chapter 4 Learning-Topic & WebMCP Architecture Specification

This document details the **Learning-Topic Architecture** designed for SJMaths and specifies how legacy production chapter structures are transitioned into intelligent, scaffolded, agent-ready learning modules.

---

## 1. Context & Motivation

The legacy SJMaths chapter data format (`chapter-*-data.json`) structured educational content as flat lists of practice questions, previous year questions (PYQs), and end-of-unit tests across major concepts. 

While efficient for direct UI rendering, the legacy format lacks:
- Explicit prerequisite dependency graphs.
- Granular skill mapping for individual assessment items.
- Multi-tier progressive hint systems (concept cues $\to$ intermediate steps $\to$ full derivations).
- Adaptive remediation policies for struggling students.
- Context-safe agent inspection hooks (Model Context Protocol).

The **Learning-Topic Architecture** formalizes these pedagogical layers into a unified, self-contained JSON schema while designed to preserve 100% of existing educational content, subject to the migration audit and manual review of identified anomalies.

---

## 2. Structural Schema Overview

```
schema_version         -> Semantic versioning of the content schema (e.g. 2.0.0)
content_type           -> Fixed as "learning_topic"
topic                  -> Metadata (ID, Title, Grade, Subject, Standard, Description)
scope                  -> Pedagogical metrics (Total units, Skills, Estimated time, Target mastery)
prerequisites          -> Explicit diagnostic checks & conceptual dependencies
sequence               -> Unit execution order & gating policies
skills                 -> Granular atomic competencies mapped across units
units                  -> Learning units containing instruction, worked examples, practice, & tests
question_engine        -> Declared learning stages & assessment suppression capabilities
remediation            -> Policy triggers and instructional fallback mechanisms
hint_system            -> Progressive multi-tier hint tiers
mastery                -> Unit checkpoints and chapter-level mastery gate definitions
delayed_retrieval      -> Spaced repetition review schedules
progress_tracking      -> Client-side metrics and state tracking policies
completion             -> Badging, completion rewards, and next chapter progression links
webmcp                 -> MCP namespace, capabilities, and tool contract definitions
```

---

## 3. Relationship to Existing SJMaths Architecture

| Existing SJMaths Architecture | Learning-Topic / WebMCP Architecture |
| :--- | :--- |
| **Concept Division:** Flat concept objects in `concepts[]` | **Learning Units:** Scaffolded `units[]` comprising instruction, callouts, worked examples, and multi-stage practice. |
| **Practice & PYQ Arrays:** Generic question arrays | **Skill-Indexed Stages:** Every item tagged with `skill_id`, `stage` (`guided_practice`, `independent_solution`, `transfer_mastery`), `difficulty`, and progressive hints. |
| **Monolithic Testing:** Immediate solution disclosure | **Answer Suppression & Gating:** Assessment mode can hide direct answers; progression governed by `unit_mastery_gate` and `chapter_mastery_gate`. |
| **Static Script Rendering:** Basic DOM manipulation in `chapter.js` | **WebMCP Extensible:** Fully compatible with Vanilla JavaScript rendering engines, while simultaneously exposing JSON-RPC / MCP tools for AI tutoring. |

---

## 4. WebMCP Integration Model

WebMCP acts as the intelligent bridge enabling AI coding assistants and interactive browser agents to inspect learning state and guide learners:

- **Namespace:** `sjmaths.curriculum` (chapter-agnostic; tool descriptions are generated from the loaded topic data)
- **Standard Tool Definitions (8):**
  1. `get_topic_outline`: Returns high-level curriculum outline, skills, and unit boundaries.
  2. `get_unit_content`: Retrieves sanitized instructional materials. Assessment-only — answer keys are never exposed on the tool surface.
  3. `get_prerequisite_check`: Delivers diagnostic precheck questions with the answer key suppressed.
  4. `evaluate_unit_practice`: Validates learner submissions and delivers targeted feedback.
  5. `get_hint`: Progressive 3-tier hints with attempt-based gating on deeper levels.
  6. `get_next_learning_action`: Recommends the next pedagogical action from live learner state.
  7. `start_mastery_exam`: Serves the cumulative chapter mastery exam (up to 10 questions) fully sanitized.
  8. `get_learning_progress`: Summarizes progress, completed units, mastered skills, and exam readiness.

---

## 5. Migration Principles

1. **Content Preservation:** Every precheck, paragraph, formula, box, practice question, PYQ, and solution from legacy Chapter 4 data is preserved without omission.
2. **Pedagogical Integrity:** Questions are categorized according to cognitive load (diagnostic $\to$ guided $\to$ independent $\to$ transfer $\to$ mastery check).
3. **No Content Invention:** If a pedagogical stage (e.g. faded guidance) lacks dedicated legacy material, it is marked as pending future expansion rather than populated with placeholder data.
4. **Stateless Content:** Student progress state is never embedded in the content schema; only tracking policies are defined.

---

## 6. Evidence-Based Skill Mastery Policy (State Version 2)

The SJMaths WebMCP prototype implements an **Evidence-Based Skill Mastery Engine** to ensure robust pedagogical evaluation:

### Mastery Policy Criteria:
A skill transition to `mastered` status requires meeting BOTH conditions:
1. **Distinct Question Requirement:** At least **2 distinct questions** associated with that skill must be answered correctly (duplicate attempts on the same question do not produce additional evidence).
2. **Cognitive Stage Requirement:** At least **1 of those correct answers** must come from higher-order problem stages:
   - `independent_solution` (Independent problem solving)
   - `transfer_mastery` (Board exam Previous Year Questions / Application)
3. **Diagnostic Precheck Exclusion:** Prechecks are diagnostic readiness gates and never award skill mastery evidence.
4. **Guided-Practice Boundary:** Success on guided practice questions alone is insufficient for mastery.

### Production Roadmap (Future Expansion):
Building upon the 2-distinct-question baseline, future production iterations will expand this model to include:
- **Cognitive Difficulty Weighting:** Tiered weighting across `easy`, `medium`, `hard` problems.
- **Mastery Gate Verification:** Final skill validation confirmed through the unit assessment checkpoint (`unit_mastery_gate`) and chapter exam (`chapter_mastery_gate`).
- **Decay & Spaced Retrieval:** Factoring in delayed retrieval checkpoints at 3, 7, and 21-day intervals.
- **Bayesian Knowledge Tracing:** Modeling probability of mastery longitudinally.


