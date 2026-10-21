---
name: exam-pyq-management
description: >-
  Workflows and scripts for extracting exam question papers, generating vector DI graphs,
  distributing questions into topic-wise subject modules, compiling HTML players, and auditing SEO.
---

# Exam PYQ Management Runbook

## Overview
Use this skill when adding or updating topic-wise Previous Year Questions (PYQs) for competitive exams (e.g. UPSSSC PET, UPSC, SSC).

## Workflow Steps

### Step 1: Extract & Clean Questions from Paper / PDF
- Extract questions into bilingual format `{en, hi}`.
- Ensure correct answer keys and detailed pedagogical explanations.
- For DI questions (graphs, tables), extract tabular data and draft vector SVGs.

### Step 2: Distribute to Subject Modules
- Load `manifest.json` to identify target subjects and question numbering ranges.
- Append new questions with appropriate sequential `qNum`, `subjectId`, `chapterId`, and `shift`.
- Update `totalQuestions`, `questionRange`, and `examShifts` in `manifest.json` and `all-pyqs.json`.

### Step 3: Rebuild HTML Pages
- Run the generator script:
  `python scratch/build_pet_html_pages.py`
- Verify that `<details class="pyq-seo-details">` is collapsed by default.
- Verify that single-question navigation and progress segments function smoothly.

### Step 4: Homepage & Navigation Integration
- Add feature button and topic chips to the relevant Exam Suite card in `index.html`.
- Add tool card in `#tools-section`.
- Add FAQ accordion item and JSON-LD schema.
- Update `assets/js/study-tracker.js` and minify with terser.

### Step 5: SEO Validation
- Run the SEO audit:
  `node scripts/audit-seo.cjs --scope=index.html,upsssc-pet-topicwise-pyqs,competitive-exams/index.html`
- Ensure 0 errors and 0 warnings before completing the task.
