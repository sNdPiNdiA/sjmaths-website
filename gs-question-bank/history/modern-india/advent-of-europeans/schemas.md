# GS Question Bank JSON Schema Specification

This document details the standardized JSON schemas for files in the GS Question Bank. All questions generated must adhere to these schemas and include rich metadata tags.

---

## 1. Multiple Choice Questions (MCQ)
**Applies to**: `mcq_easy.json`, `mcq_medium.json`, `mcq_hard.json`, `multiple_statement.json`, `assertion_reason.json`, `pyq_upsc.json`, `pyq_ssc.json`, `pyq_railway.json`, `pyq_state_pcs.json`, `pyq_teaching.json`

```json
[
  {
    "id": "String (unique identifier, e.g. mcq-01-01-001)",
    "question": "String (the question text)",
    "options": [
      "String (Option A)",
      "String (Option B)",
      "String (Option C)",
      "String (Option D)"
    ],
    "correct_index": "Number (0-based index of correct option: 0 to 3)",
    "explanation": "String (detailed explanation referencing historical context)",
    "difficulty": "String ('easy' | 'medium' | 'hard')",
    "tags": ["Array of Strings (e.g. ['Vasco da Gama', 'Portuguese', 'Zamorin'])"],
    "exam_tags": ["Array of Strings (e.g. ['UPSC', 'State PCS', 'SSC'])"],
    "syllabus_ref": "String (relative path, e.g. 'history/modern-india/advent-of-europeans/02_Portuguese_Arrival/Vasco_da_Gama')"
  }
]
```

---

## 2. Match the Following & Chronology
**Applies to**: `match_following.json`, `pair_matching.json`, `chronology.json`, `arrange_sequence.json`

```json
[
  {
    "id": "String (unique identifier)",
    "question": "String (the question text setting up the matching/chronology task)",
    "items": [
      {
        "left": "String (left item)",
        "right": "String (right matching item / value)"
      }
    ],
    "options": [
      "String (Option A pattern, e.g. 'A-1, B-2, C-3')",
      "String (Option B)",
      "String (Option C)",
      "String (Option D)"
    ],
    "correct_index": "Number (0-based index of correct option)",
    "explanation": "String (detailed explanation of the sequence or matches)",
    "tags": ["Array of Strings"],
    "exam_tags": ["Array of Strings"],
    "syllabus_ref": "String"
  }
]
```

---

## 3. Fill in the Blanks & True/False
**Applies to**: `fill_blanks.json`, `true_false.json`, `one_liner.json`, `odd_one_out.json`

```json
[
  {
    "id": "String (unique identifier)",
    "question": "String (the question text)",
    "correct_answer": "String or Boolean (the expected answer)",
    "explanation": "String (context and explanation)",
    "tags": ["Array of Strings"],
    "exam_tags": ["Array of Strings"],
    "syllabus_ref": "String"
  }
]
```

---

## 4. Subjective / Mains Written Questions
**Applies to**: `short_answer.json`, `long_answer.json`, `mains_10m.json`, `mains_15m.json`, `mains_20m.json`, `interview.json`

```json
[
  {
    "id": "String (unique identifier)",
    "question": "String (the essay/written prompt)",
    "marks": "Number (e.g. 10, 15, 20)",
    "word_limit": "Number (e.g. 150, 250)",
    "model_answer": "String (structured model answer checklist or key points)",
    "tags": ["Array of Strings"],
    "exam_tags": ["Array of Strings"],
    "syllabus_ref": "String"
  }
]
```

---

## 6. Map-Based Questions — "Eliminate the Wrong Map Fact"
**Applies to**: `map_based.json`

Each question presents 4 options, each pairing a **Settlement / Port / Battle Site / Route** with a **geographical location or European power**. Three options are historically correct; one is deliberately wrong. The student must identify the incorrect pairing.

```json
[
  {
    "id": "String (unique identifier, e.g. map-01-001)",
    "question": "String (always starts with 'Which of the following is NOT correctly matched?' and specifies the category, e.g. 'European settlements and their locations')",
    "options": [
      "String (e.g. 'Goa — West coast of India (Portuguese)')",
      "String (e.g. 'Pondicherry — Coromandel Coast (French)')",
      "String (e.g. 'Surat — Eastern coast of India (English)')",
      "String (e.g. 'Calicut — Malabar Coast (Portuguese)')"
    ],
    "correct_index": "Number (0-based index of the WRONG / incorrect option)",
    "wrong_fact": "String (the incorrect claim in the wrong option, e.g. 'Surat is on the western, not eastern coast')",
    "explanation": "String (explains why the chosen option is wrong AND confirms the correct facts for all other options)",
    "difficulty": "String ('easy' | 'medium' | 'hard')",
    "geo_tags": ["Array of Strings — geographical entities tested, e.g. ['Goa', 'Malabar Coast', 'Coromandel Coast']"],
    "tags": ["Array of Strings — historical tags"],
    "exam_tags": ["Array of Strings (e.g. ['UPSC', 'State PCS', 'SSC'])"],
    "syllabus_ref": "String (relative path)"
  }
]
```

**Rules for question writers:**
- All 4 options must look plausible — the wrong option should have a believable but subtle error (wrong coast, wrong century, wrong European power, wrong city).
- Vary the position of the wrong option (do not always put it at index 2 or 3).
- Each topic's `map_based.json` should contain **3 questions** of mixed difficulty (1 easy, 1 medium, 1 hard).
- Questions must be specific to the topic's geography (e.g. a topic on Portuguese settlements should test Portuguese ports and coasts).

---

## 5. Descriptive & Revision Tools
**Applies to**: `facts.json`, `flashcards.json`, `revision_questions.json`, `concept_traps.json`, `common_mistakes.json`, `memory_hooks.json`

```json
[
  {
    "id": "String (unique identifier)",
    "title": "String (brief concept title)",
    "question": "String (front of card or question prompt)",
    "answer": "String (back of card or key fact details)",
    "trap_details": "String (common mistake or trap to watch out for)",
    "explanation": "String (detailed context)",
    "tags": ["Array of Strings"],
    "exam_tags": ["Array of Strings"],
    "syllabus_ref": "String"
  }
]
```
