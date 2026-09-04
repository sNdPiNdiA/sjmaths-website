#!/usr/bin/env python3
"""
SAT Topic Pages - 3-Call High Quality Gemini SEO Generator
SJMaths Digital SAT Math Prep Platform

Call 1: Concepts, Worked Examples, Formula Sheet & PYQ Analysis
Call 2: 20+ Graded Practice Questions (with Hints, Traditional & Desmos Tricks)
Call 3: 3-Level Mock Test (30 Questions: 10 Easy, 10 Medium, 10 Hard)
"""

import os
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)
import json
import re
import time
import argparse
import urllib.request
import urllib.error

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_api_key():
    """Load Gemini API Key from environment or .env file."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if api_key:
        return api_key
    
    env_path = os.path.join(REPO_ROOT, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip()
                elif line.startswith("GOOGLE_API_KEY="):
                    return line.split("=", 1)[1].strip()
    return None

from json_repair import repair_json

def clean_and_parse_json(raw_text):
    """Clean and parse JSON from Gemini using json_repair."""
    text = raw_text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        return json.loads(text, strict=False)
    except Exception:
        # Fallback to json_repair for any unescaped LaTeX backslashes or broken quotes
        return repair_json(text, return_objects=True)

def parse_correct_index(val):
    """Safely convert correct_index to integer (handles 0, '0', 'A', 'B', etc.)."""
    if val is None:
        return 0
    if isinstance(val, int):
        return val
    val_str = str(val).strip().upper()
    if val_str in ["A", "B", "C", "D"]:
        return ord(val_str) - ord("A")
    try:
        return int(val_str)
    except Exception:
        return 0

API_CALL_COUNT = 0

def get_tiered_model():
    """
    Tiered API model scheduling:
    - Calls 1 to 20: gemini-3.8-flash
    - Calls 21 to 40: gemini-3.7-flash
    - Calls 41+: gemini-3.6-flash
    """
    global API_CALL_COUNT
    if API_CALL_COUNT <= 20:
        return "gemini-3.8-flash"
    elif API_CALL_COUNT <= 40:
        return "gemini-3.7-flash"
    else:
        return "gemini-3.6-flash"

def call_gemini(api_key, prompt, model="tiered", max_retries=6, gap_seconds=15):
    """Call Gemini API with 15s pacing and 3.8 -> 3.7 -> 3.6 tiered rotation."""
    global API_CALL_COUNT
    
    # Gap of 15s between consecutive API calls
    if API_CALL_COUNT > 0 and gap_seconds > 0:
        print(f"\n[Pacing] Waiting {gap_seconds}s gap before next API call...", flush=True)
        time.sleep(gap_seconds)
        
    API_CALL_COUNT += 1
    target_model = get_tiered_model() if (model in [None, "tiered", "gemini-3.5-flash-lite"]) else model
    tier_label = "3.8 Flash (Calls 1-20)" if API_CALL_COUNT <= 20 else ("3.7 Flash (Calls 21-40)" if API_CALL_COUNT <= 40 else "3.6 Flash (Calls 41+)")
    print(f"\n=======================================================", flush=True)
    print(f">>> [API Call #{API_CALL_COUNT}] Active Model: {target_model} | Tier: {tier_label}", flush=True)
    print(f"=======================================================", flush=True)

    current_model = target_model
    for attempt in range(max_retries):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{current_model}:generateContent?key={api_key}"
        gen_config = {
            "responseMimeType": "application/json",
            "temperature": 0.2,
            "maxOutputTokens": 8192,
        }
        if "3.1-flash" in current_model:
            gen_config["thinkingConfig"] = {"thinkingBudget": 0}

        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": gen_config
        }
        headers = {"Content-Type": "application/json"}

        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            with urllib.request.urlopen(req, timeout=40) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidate_text = data["candidates"][0]["content"]["parts"][0]["text"]
                print(f"[API Call #{API_CALL_COUNT}] Success with {current_model}!", flush=True)
                return clean_and_parse_json(candidate_text)
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8")
            print(f"Gemini API Error ({current_model}) Attempt {attempt+1}/{max_retries} [{e.code}]: {err_msg[:100]}", flush=True)
            if e.code in [429, 503]:
                time.sleep(3 * (attempt + 1))
                if attempt >= 1 and current_model != "gemini-3.1-flash-lite":
                    print("-> Switching to resilient fallback model gemini-3.1-flash-lite due to upstream load...", flush=True)
                    current_model = "gemini-3.1-flash-lite"
            else:
                time.sleep(3)
        except Exception as e:
            print(f"Call attempt {attempt+1} failed: {e}", flush=True)
            if attempt >= 1 and current_model != "gemini-3.1-flash-lite":
                print("-> Switching to resilient fallback model gemini-3.1-flash-lite due to timeout...", flush=True)
                current_model = "gemini-3.1-flash-lite"
            time.sleep(3)
            
    raise RuntimeError(f"Failed to call Gemini ({current_model}) after {max_retries} attempts.")

# --------------------------------------------------------------------------
# Call 1: Concepts, Formulas, Traps & PYQ Analysis
# --------------------------------------------------------------------------
def fetch_concepts_and_formulas(api_key, domain, topic_title, model="gemini-3.5-flash-lite"):
    prompt = f"""You are an elite Digital SAT Math master instructor for SJMaths.
Generate in-depth Concept breakdowns, Formula Revision sheets, SAT Traps, and PYQ Exam trends for the topic: "{topic_title}" under the domain "{domain}".

Output STRICT JSON conforming to this schema:
{{
  "topic_title": "{topic_title}",
  "domain_name": "{domain}",
  "seo_meta_description": "Master {topic_title} for Digital SAT Math with concise concept summaries, 20+ graded practice questions with Desmos shortcuts, formula cheat sheet, and 3-level mock test.",
  "exam_weightage": "High Yield (1-3 Questions per Test)",
  "concepts": [
    {{
      "concept_title": "Concept 1: Definition & Key Properties",
      "summary": "Clear, concise 1-2 sentence core definition.",
      "key_rules": [
        "Rule 1 with math equations: $...$",
        "Rule 2 with math equations: $...$",
        "Rule 3 with math equations: $...$"
      ],
      "traditional_method": "Clear, step-by-step algebraic manipulation explanation.",
      "sat_speed_trick": "Desmos graphical trick, slider shortcut, or inspection method.",
      "worked_example": {{
        "problem": "Digital SAT style example question with LaTeX $...$",
        "traditional_solution": [
          "Step 1: [Setup or identification of cases]",
          "Step 2: [Algebraic equation on its own line: $...$]",
          "Step 3: [Next equation or case calculation: $...$]",
          "Step 4: [Final calculation and answer: $...$]"
        ],
        "speed_trick": [
          "Step 1: [Desmos input or shortcut setup]",
          "Step 2: [Intersection or graphical inspection step]",
          "Step 3: [Target answer obtained in under 20s]"
        ],
        "answer": "Correct answer / option"
      }}
    }}
  ],
  "pyq_trends": {{
    "frequency": "1-3 questions per test module",
    "historical_pattern": "Analysis of College Board question patterns and recent exam distributions.",
    "module1_weight": "Medium Frequency (Foundational tests)",
    "module2_weight": "High Frequency (Hard module score differentiator)"
  }},
  "formula_sheet": {{
    "core_formulas": [
      {{
        "name": "Formula/Property Name",
        "formula": "$...$",
        "description": "When and how to use it on the Digital SAT."
      }}
    ],
    "sat_traps": [
      {{
        "title": "Trap Title (e.g. Extraneous Solutions)",
        "description": "Common pitfall and how to avoid College Board distractors."
      }}
    ],
    "desmos_shortcuts": [
      {{
        "tactic": "Desmos Shortcut Name",
        "syntax": "y = f(x) syntax",
        "tip": "High speed strategy tip."
      }}
    ]
  }}
}}

CRITICAL TEXTBOOK FORMATTING REQUIREMENT:
In textbooks, every algebraic manipulation step, equation, and deduction appears on its OWN SEPARATE NEW LINE.
Do NOT combine multiple equations horizontally on one line with arrows or 'and'.
Provide 'traditional_solution' and 'speed_trick' as JSON ARRAYS OF STRINGS, where each string is ONE distinct step or line of mathematical working.
Provide 4-5 distinct concept archetypes. Keep explanations concise, structured in bullet points. Use LaTeX equations ($ for inline, $$ for block). Ensure valid JSON string escaping.
"""
    print(f"-> [Call 1/3] Fetching Concepts, Formulas & PYQs for {topic_title} with {model}...")
    return call_gemini(api_key, prompt, model=model)

# --------------------------------------------------------------------------
# Call 2: Practice Question Bank (20+ Graded Questions)
# --------------------------------------------------------------------------
def fetch_practice_questions(api_key, domain, topic_title, model="gemini-3.5-flash-lite"):
    prompt = f"""You are an expert Digital SAT Math problem creator for SJMaths.
Generate at least 20 authentic Digital SAT Math practice questions for the topic: "{topic_title}" under "{domain}".

Requirements:
1. Divide questions across 4 distinct question archetypes (5 questions per archetype).
2. For each archetype, progress in difficulty from Easy (Questions 1-2) -> Medium (Questions 3-4) -> Hard (Question 5).
3. Every question must have 4 multiple-choice options (A, B, C, D) with realistic SAT-style distractors.
4. Provide a targeted Hint, full Step-by-Step Algebraic Solution, and an instant Desmos / Speed Trick for every question.
5. TEXTBOOK STEP-BY-STEP FORMATTING:
   Every step in 'traditional_solution' and 'speed_trick' MUST be in a new line as in textbooks.
   Provide them as JSON ARRAYS OF STRINGS, where each element is ONE step or calculation line:
   "traditional_solution": [
     "Step 1: [Setup/Case definition]",
     "Step 2: [Equation on its own line: $...$]",
     "Step 3: [Next deduction on its own line: $...$]",
     "Step 4: [Final answer calculation: $...$]"
   ],
   "speed_trick": [
     "Step 1: [Desmos entry]",
     "Step 2: [Observation / shortcut]",
     "Step 3: [Target answer]"
   ]

Output STRICT JSON conforming to this schema:
{{
  "practice_questions": [
    {{
      "id": 1,
      "archetype": "Specific Question Archetype Name",
      "difficulty": "Easy",
      "question": "Question statement in LaTeX $...$",
      "options": [
        {{"label": "A", "text": "$...$"}},
        {{"label": "B", "text": "$...$"}},
        {{"label": "C", "text": "$...$"}},
        {{"label": "D", "text": "$...$"}}
      ],
      "correct_index": "0",
      "hint": "Actionable hint.",
      "traditional_solution": [
        "Step 1: ...",
        "Step 2: ..."
      ],
      "speed_trick": [
        "Step 1: ...",
        "Step 2: ..."
      ]
    }}
  ]
}}

Generate exactly 20 to 24 high-quality practice questions. Use valid JSON escaping for all backslashes.
"""
    print(f"-> [Call 2/3] Fetching 20+ Practice Questions for {topic_title} with {model}...")
    return call_gemini(api_key, prompt, model=model)

# --------------------------------------------------------------------------
# Call 3: 3-Level Mock Test (30 Questions Total)
# --------------------------------------------------------------------------
def fetch_mock_tests(api_key, domain, topic_title, model="gemini-3.5-flash-lite"):
    prompt = f"""You are an official Digital SAT Math test creator for SJMaths.
Generate a 30-question diagnostic mock test bank for "{topic_title}" under "{domain}" divided into 3 score tiers:
- Level 1: Foundation (10 Questions - Sub-600 SAT score tier)
- Level 2: Target 700+ (10 Questions - 600-740 SAT score tier)
- Level 3: 800-Mastery (10 Questions - 750-800 SAT score tier)

TEXTBOOK STEP-BY-STEP FORMATTING:
Every step in 'explanation' MUST be on a new line as in textbooks.
Provide 'explanation' as a JSON ARRAY OF STRINGS:
"explanation": [
  "Step 1: [Setup or property used]",
  "Step 2: [Algebraic equation on its own line: $...$]",
  "Step 3: [Final deduction confirming option: $...$]"
]

Output STRICT JSON conforming to this schema:
{{
  "mock_tests": {{
    "level1_foundation": [
      {{
        "id": 1,
        "question": "Digital SAT style question in LaTeX $...$",
        "options": [
          {{"label": "A", "text": "$...$"}},
          {{"label": "B", "text": "$...$"}},
          {{"label": "C", "text": "$...$"}},
          {{"label": "D", "text": "$...$"}}
        ],
        "correct_index": "0",
        "explanation": [
          "Step 1: ...",
          "Step 2: ..."
        ]
      }}
    ],
    "level2_target700": [
      {{
        "id": 1,
        "question": "Medium difficulty SAT question in LaTeX $...$",
        "options": [
          {{"label": "A", "text": "$...$"}},
          {{"label": "B", "text": "$...$"}},
          {{"label": "C", "text": "$...$"}},
          {{"label": "D", "text": "$...$"}}
        ],
        "correct_index": "0",
        "explanation": [
          "Step 1: ...",
          "Step 2: ..."
        ]
      }}
    ],
    "level3_800mastery": [
      {{
        "id": 1,
        "question": "Challenging hard module SAT question in LaTeX $...$",
        "options": [
          {{"label": "A", "text": "$...$"}},
          {{"label": "B", "text": "$...$"}},
          {{"label": "C", "text": "$...$"}},
          {{"label": "D", "text": "$...$"}}
        ],
        "correct_index": "0",
        "explanation": [
          "Step 1: ...",
          "Step 2: ..."
        ]
      }}
    ]
  }}
}}

Provide exactly 10 questions in level1_foundation, 10 in level2_target700, and 10 in level3_800mastery (30 mock questions total). Ensure valid JSON string escaping.
"""
    print(f"-> [Call 3/3] Fetching 3-Level 30Q Mock Test for {topic_title} with {model}...")
    return call_gemini(api_key, prompt, model=model)


# --------------------------------------------------------------------------
# Specialized Call: Desmos Calculator Mastery
# --------------------------------------------------------------------------
def fetch_desmos_data(api_key, topic_title, model="tiered"):
    prompt = f"""You are an elite Digital SAT Math & Desmos specialist instructor for SJMaths.
Generate an exhaustive, high-speed Desmos Calculator Mastery Guide for the topic: "{topic_title}".

Provide:
1. "techniques": 5 to 6 foundational & advanced Desmos techniques/syntax rules specifically for "{topic_title}".
   - "title": Technique Name (e.g. "Interactive Sliders for Unknown Constants", "Regression Formula ~ for Best Fit & Coefficients", "Finding Intersections with Clickable Points")
   - "syntax": Exact code to enter in Desmos (e.g. "y1 ~ ax1^2 + bx1 + c" or "y = 2x + k")
   - "description": Clear explanation of how it works and what SAT problem type it solves in seconds.
   - "when_to_use": When on the Digital SAT to choose Desmos over algebra.
   - "pro_tip": High-scoring timing or syntax tip.
2. "speed_walkthroughs": 4 to 5 classic Digital SAT Math questions comparing:
   - "problem": Authentic SAT question statement (LaTeX $...$).
   - "time_saved": Time saved (e.g. "⚡ 85s Saved (15s vs 100s)").
   - "traditional_method": Array of textbook steps (each step on its own line).
   - "desmos_hack": Array of high-speed Desmos steps with exact keystrokes/expressions to type.
   - "answer": Final correct answer.
3. "drills": 10 to 12 targeted Calculator Drill questions:
   - Mix: 70% MCQ, 30% SPR (Student-Produced Response where user enters a numeric answer).
   - For each drill:
     - "id": integer
     - "qtype": "mcq" or "spr"
     - "question": Statement with LaTeX $...$
     - "options": [{{"label":"A","text":"..."}}, {{"label":"B","text":"..."}}, {{"label":"C","text":"..."}}, {{"label":"D","text":"..."}}] (if mcq)
     - "correct_index": "0" (if mcq)
     - "spr_answer": "4.5" (if spr)
     - "desmos_command": "Exact command or expressions to enter in Desmos"
     - "explanation": Array of step strings explaining the calculation and graphical confirmation.

Output STRICT JSON conforming to this schema:
{{
  "topic_title": "{topic_title}",
  "seo_meta_description": "Master {topic_title} on the Digital SAT using built-in Desmos graphing calculator hacks, syntax commands, regressions, and speed drills.",
  "exam_weightage": "Essential Digital SAT Tool (5-8 Questions per Module)",
  "techniques": [
    {{
      "title": "...",
      "syntax": "...",
      "description": "...",
      "when_to_use": "...",
      "pro_tip": "..."
    }}
  ],
  "speed_walkthroughs": [
    {{
      "problem": "...",
      "time_saved": "...",
      "traditional_method": ["Step 1: ..."],
      "desmos_hack": ["Step 1: ..."],
      "answer": "..."
    }}
  ],
  "drills": [
    {{
      "id": 1,
      "qtype": "mcq",
      "question": "...",
      "options": [
        {{"label": "A", "text": "..."}},
        {{"label": "B", "text": "..."}},
        {{"label": "C", "text": "..."}},
        {{"label": "D", "text": "..."}}
      ],
      "correct_index": "0",
      "spr_answer": "...",
      "desmos_command": "...",
      "explanation": ["Step 1: ..."]
    }}
  ]
}}
Ensure valid JSON string escaping for all LaTeX backslashes.
"""
    print(f"-> Fetching Desmos Calculator Guide for {topic_title} with {model}...")
    return call_gemini(api_key, prompt, model=model)

# --------------------------------------------------------------------------
# Specialized Call: Student-Produced Response (SPR / Grid-In)
# --------------------------------------------------------------------------
def fetch_spr_data(api_key, topic_title, model="tiered"):
    prompt = f"""You are the leading Digital SAT Math assessment authority for SJMaths.
Generate the authoritative Student-Produced Response (SPR / Grid-In) Mastery Guide & Interactive Simulator for: "{topic_title}".

Provide:
1. "official_rules": 4 to 6 strict College Board rules for SPR entries:
   - "rule_number": "Rule 1", "Rule 2", etc.
   - "title": e.g. "Negative Signs and Fractions", "Repeating Decimals & Truncation", "No Mixed Numbers Allowed"
   - "summary": Clear rule definition.
   - "do_this": What the student should type (e.g. "Type 7/2 or 3.5").
   - "never_do_this": What College Board marks WRONG (e.g. "Never type 3 1/2 as Bluebook reads it as 31/2").
   - "example": Short illustrative example.
2. "common_traps": 5 to 6 common pitfalls where students lose points on the real SAT:
   - "trap_title": e.g. "Premature Rounding in Intermediate Steps", "Multiple Valid Answers in Inequalities", "Trailing Zeros"
   - "scenario": Problem scenario.
   - "flawed_input": Example invalid input.
   - "correct_input": Valid input that receives full credit.
   - "explanation": Why the scoring algorithm rejects the flawed input.
3. "simulator_questions": 12 to 15 authentic Digital SAT SPR questions (all questions are Student-Produced Response):
   - "id": integer
   - "difficulty": "Easy", "Medium", or "Hard"
   - "question": Question statement in LaTeX $...$
   - "expected_answer": Canonical answer string (e.g. "7/4" or "1.75" or "-3")
   - "accepted_answers": Array of strings of all valid representations (e.g. ["7/4", "1.75"])
   - "hint": Actionable strategy hint.
   - "solution_steps": Array of textbook steps (each step on its own line).

Output STRICT JSON conforming to this schema:
{{
  "topic_title": "{topic_title}",
  "seo_meta_description": "Master Digital SAT Student-Produced Response (Grid-In) questions for {topic_title}. Learn official College Board rules, avoid costly formatting traps, and practice with our interactive simulator.",
  "exam_weightage": "25% of Math Exam (5-6 Questions per Module)",
  "official_rules": [
    {{
      "rule_number": "Rule 1",
      "title": "...",
      "summary": "...",
      "do_this": "...",
      "never_do_this": "...",
      "example": "..."
    }}
  ],
  "common_traps": [
    {{
      "trap_title": "...",
      "scenario": "...",
      "flawed_input": "...",
      "correct_input": "...",
      "explanation": "..."
    }}
  ],
  "simulator_questions": [
    {{
      "id": 1,
      "difficulty": "Medium",
      "question": "...",
      "expected_answer": "...",
      "accepted_answers": ["..."],
      "hint": "...",
      "solution_steps": ["Step 1: ..."]
    }}
  ]
}}
Ensure valid JSON string escaping for all LaTeX backslashes.
"""
    print(f"-> Fetching SPR Grid-In Guide for {topic_title} with {model}...")
    return call_gemini(api_key, prompt, model=model)

# --------------------------------------------------------------------------
# Specialized Call: Strategy Guides (Editorial Article)
# --------------------------------------------------------------------------
def fetch_guide_data(api_key, topic_title, model="tiered"):
    prompt = f"""You are a world-class Digital SAT Math master tutor and author for SJMaths.
Write an authoritative, exhaustive, high-scoring strategy guide on: "{topic_title}".

Provide:
1. "title": Authoritative title (e.g. "Digital SAT Math: The Ultimate 800-Score Strategy Guide (2026)")
2. "seo_meta_description": Compelling 150-160 char meta description.
3. "read_time": e.g. "12 min read"
4. "last_updated": "Updated for 2026 Digital SAT"
5. "executive_summary": 2-3 engaging paragraphs explaining why this topic is the key to breaking past score plateaus (500 to 650 to 750+).
6. "key_takeaways": 4 to 5 bullet points of immediate takeaways.
7. "sections": 5 to 7 detailed, content-rich sections. Each section must include:
   - "id": slug identifier for TOC anchor (e.g. "adaptive-testing-algorithm")
   - "heading": Section Title
   - "paragraphs": 2-4 comprehensive paragraphs of deep strategic analysis.
   - "callout": Optional dict with {{"title": "...", "text": "..."}} for critical warnings or exam rules.
   - "bullet_points": Optional list of actionable rules, tactics, or study benchmarks.
   - "table": Optional structured table dict with {{"headers": [...], "rows": [[...], [...]]}} (e.g. Score Tier Benchmarks, Weekly Schedule, or Timing Breakdown).
8. "faq": 4 to 5 frequently asked questions with thorough, expert answers.

Output STRICT JSON conforming to this schema:
{{
  "title": "...",
  "seo_meta_description": "...",
  "read_time": "12 min read",
  "last_updated": "2026 Digital SAT Edition",
  "executive_summary": "...",
  "key_takeaways": ["..."],
  "sections": [
    {{
      "id": "section-1",
      "heading": "...",
      "paragraphs": ["..."],
      "callout": {{"title": "...", "text": "..."}},
      "bullet_points": ["..."],
      "table": {{"headers": ["..."], "rows": [["..."]]}}
    }}
  ],
  "faq": [
    {{
      "question": "...",
      "answer": "..."
    }}
  ]
}}
Ensure valid JSON string escaping for all LaTeX backslashes.
"""
    print(f"-> Fetching Strategy Guide for {topic_title} with {model}...")
    return call_gemini(api_key, prompt, model=model)

def split_steps_smart(text):
    """Split a solution string or list into distinct textbook lines."""
    if not text:
        return []
    if isinstance(text, list):
        flat = []
        for item in text:
            s = str(item).strip()
            if not s:
                continue
            if '\n' in s:
                flat.extend([l.strip() for l in s.split('\n') if l.strip()])
            else:
                flat.append(s)
        return flat

    # Check for explicit newlines
    if '\n' in text:
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        if len(lines) > 1:
            return lines

    # Split on explicit step/case markers (e.g. "Step 1:", "Case 1:", "Check:", "Conclusion:")
    step_splits = re.split(r'(?=(?:Step\s*\d+|Case\s*\d+|Check\s*(?:x\s*=)?|Conclusion|Final Answer)\s*[:\.-])', text, flags=re.IGNORECASE)
    if len(step_splits) > 1:
        return [s.strip() for s in step_splits if s.strip()]

    # Split on sentence boundaries (period followed by space), taking care not to split inside math $...$
    parts = []
    curr = ""
    in_math = False
    i = 0
    while i < len(text):
        char = text[i]
        if char == '$':
            in_math = not in_math
            curr += char
        elif char == '.' and not in_math and i + 1 < len(text) and text[i+1].isspace():
            curr += '.'
            parts.append(curr.strip())
            curr = ""
            i += 1  # Skip the following whitespace
        elif char == ';' and not in_math:
            curr += ';'
            parts.append(curr.strip())
            curr = ""
        else:
            curr += char
        i += 1
    if curr.strip():
        parts.append(curr.strip())
    return [p for p in parts if p]

def format_steps(text):
    """Format mathematical solutions into clean textbook line-by-line steps."""
    if not text:
        return ""
    
    raw_lines = split_steps_smart(text)
    if not raw_lines:
        return f"<p>{text}</p>"

    html_steps = []
    step_counter = 1
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue

        # Check if line begins with a labeled badge
        step_match = re.match(r'^(Step\s*(\d+)|Case\s*\d+|For Case\s*\d+|Check|Note|Conclusion|Final Answer|Left Side|Right Side)\s*[:\.-]?\s*(.*)$', line, re.IGNORECASE)
        if step_match:
            badge = step_match.group(1).title()
            content = step_match.group(3).strip()
            if step_match.group(2):
                step_counter = int(step_match.group(2)) + 1
            if not content:
                content = line
        else:
            # If line is pure math equation or special line
            if line.startswith("$") and line.endswith("$"):
                badge = "Calc"
            elif any(line.lower().startswith(kw) for kw in ["case 1", "case 2", "check", "sum:", "product:"]):
                badge = "Calc"
            elif any(line.lower().startswith(kw) for kw in ["left side", "right side"]):
                badge = "Check"
            elif any(line.lower().startswith(kw) for kw in ["conclusion", "final answer", "since"]):
                badge = "Result"
            else:
                badge = f"Step {step_counter}"
                step_counter += 1
            content = line

        html_steps.append(f"""
        <div class="solution-step">
            <span class="step-badge">{badge}</span>
            <div class="step-content">{content}</div>
        </div>
        """)
    return f'<div class="solution-steps">{"".join(html_steps)}</div>'

# --------------------------------------------------------------------------
# HTML Compiler & Builder
# --------------------------------------------------------------------------
def render_html(data, rel_path):
    """Render 100% pre-rendered static HTML with 5 tabs and Schema.org JSON-LD."""
    domain_slug = rel_path.split("/")[0]
    topic_slug = rel_path.split("/")[1]
    title = data.get("topic_title", topic_slug.replace("-", " ").title())
    domain_name = data.get("domain_name", domain_slug.replace("-", " ").title())
    meta_desc = data.get("seo_meta_description", f"Master {title} for Digital SAT Math.")
    canonical_url = f"https://sjmaths.com/sat/{domain_slug}/{topic_slug}/"
    practice_questions = data.get("practice_questions", [])
    practice_count = len(practice_questions)
    
    # Build Schema.org Quiz & Questions
    quiz_questions = []
    for q in practice_questions[:10]:
        options = q.get("options", [])
        correct_idx = parse_correct_index(q.get("correct_index", 0))
        accepted_answer = options[correct_idx]["text"] if correct_idx < len(options) else ""
        suggested_answers = [opt["text"] for i, opt in enumerate(options) if i != correct_idx]
        
        quiz_questions.append({
            "@type": "Question",
            "name": q.get("question", "")[:100],
            "text": q.get("question", ""),
            "acceptedAnswer": {
                "@type": "Answer",
                "text": accepted_answer
            },
            "suggestedAnswer": [{"@type": "Answer", "text": s} for s in suggested_answers]
        })

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/"},
                    {"@type": "ListItem", "position": 2, "name": "SAT Hub", "item": "https://sjmaths.com/sat/"},
                    {"@type": "ListItem", "position": 3, "name": domain_name, "item": f"https://sjmaths.com/sat/{domain_slug}/"},
                    {"@type": "ListItem", "position": 4, "name": title, "item": canonical_url}
                ]
            },
            {
                "@type": "LearningResource",
                "name": f"{title} - Digital SAT Math Preparation",
                "description": meta_desc,
                "educationalLevel": "High School / SAT Prep",
                "learningResourceType": "Study Guide & Practice Bank",
                "provider": {
                    "@type": "Organization",
                    "name": "SJMaths",
                    "url": "https://sjmaths.com/"
                }
            },
            {
                "@type": "Quiz",
                "name": f"{title} SAT Practice Quiz",
                "hasPart": quiz_questions
            }
        ]
    }
    
    # Pre-render Tab 1: Learn
    concepts_html = []
    for idx, c in enumerate(data.get("concepts", []), 1):
        rules_li = "".join([f"<li>{r}</li>" for r in c.get("key_rules", [])])
        ex = c.get("worked_example", {})
        trad_steps = format_steps(ex.get("traditional_solution", ""))
        speed_steps = format_steps(ex.get("speed_trick", ""))
        
        concepts_html.append(f"""
        <article class="concept-card">
            <span class="concept-badge">Concept {idx}</span>
            <h3>{c.get("concept_title", "")}</h3>
            <p class="concept-lead">{c.get("summary", "")}</p>
            
            <ul class="concept-rules-list">
                {rules_li}
            </ul>

            <div class="dual-method-grid">
                <div class="method-box method-box-trad">
                    <div class="method-header">📘 Traditional Algebraic Method</div>
                    <p>{c.get("traditional_method", "")}</p>
                </div>
                <div class="method-box method-box-trick">
                    <div class="method-header">⚡ SAT Speed Trick & Desmos Hack</div>
                    <p>{c.get("sat_speed_trick", "")}</p>
                </div>
            </div>

            <div class="example-box">
                <div class="example-title">💡 Worked SAT Archetype Example</div>
                <p><strong>Problem:</strong> {ex.get("problem", "")}</p>
                <div style="margin-top:14px;">
                    <div style="font-weight:700; font-size:0.9rem; color:var(--ink-main); margin-bottom:6px;">📘 Step-by-Step Textbook Solution:</div>
                    {trad_steps}
                    <div style="margin-top:12px; font-weight:700; font-size:0.9rem; color:var(--theme-dark); margin-bottom:6px;">⚡ Speed / Desmos Tactic:</div>
                    {speed_steps}
                </div>
            </div>
        </article>
        """)
    learn_panel_html = "".join(concepts_html)

    # Pre-render Tab 2: Practice
    practice_cards_html = []
    archetypes = list(set(q.get("archetype", "General") for q in practice_questions))
    
    for q in practice_questions:
        diff = q.get("difficulty", "Medium")
        diff_class = f"diff-{diff.lower()}"
        opts_html = []
        for opt_idx, opt in enumerate(q.get("options", [])):
            opts_html.append(f"""
            <button class="option-btn" data-index="{opt_idx}">
                <span class="option-label">{opt.get("label", "A")}</span>
                <span class="option-text">{opt.get("text", "")}</span>
            </button>
            """)
        opts_rendered = "".join(opts_html)
        
        q_trad_steps = format_steps(q.get('traditional_solution', ''))
        q_speed_steps = format_steps(q.get('speed_trick', ''))
        
        practice_cards_html.append(f"""
        <div class="question-card practice-card" data-type="{q.get('archetype', 'General')}" data-correct="{parse_correct_index(q.get('correct_index', '0'))}">
            <div class="q-header">
                <div class="q-header-left">
                    <span class="q-number">Question {q.get('id', 1)}</span>
                    <span class="q-archetype-tag">{q.get('archetype', 'Archetype')}</span>
                </div>
                <span class="diff-badge {diff_class}">{diff}</span>
            </div>
            <div class="q-body">
                <p>{q.get('question', '')}</p>
            </div>
            <div class="options-grid">
                {opts_rendered}
            </div>
            <div class="q-actions">
                <button class="btn btn-theme btn-sm btn-check-answer">Check Answer</button>
                <button class="btn btn-secondary btn-sm btn-hint">💡 Hint</button>
                <button class="btn btn-secondary btn-sm btn-toggle-solution">View Solution</button>
            </div>
            <div class="hint-box" style="display:none; margin-top:14px; padding:12px 16px; background:var(--warning-soft); border-left:3px solid var(--warning); border-radius:var(--radius-sm); font-size:0.88rem; color:#92400e;">
                <strong>Hint:</strong> {q.get('hint', 'Think about the core definition.')}
            </div>
            <div class="solution-drawer">
                <div class="dual-method-grid">
                    <div class="method-box method-box-trad">
                        <div class="method-header">📘 Step-by-Step Algebraic Solution</div>
                        {q_trad_steps}
                    </div>
                    <div class="method-box method-box-trick">
                        <div class="method-header">⚡ Desmos Shortcut / Speed Hack</div>
                        {q_speed_steps}
                    </div>
                </div>
            </div>
        </div>
        """)
    practice_panel_html = "".join(practice_cards_html)
    filters_html = "".join([f'<button class="filter-chip" data-filter="{arch}">{arch}</button>' for arch in archetypes])

    # Pre-render Tab 3: PYQ Matrix
    pyq_data = data.get("pyq_trends", {})
    pyq_panel_html = f"""
    <div class="pyq-matrix-card">
        <div class="panel-header compact-header">
            <h2>Official SAT Exam Blueprint & Weightage</h2>
        </div>
        
        <div class="table-responsive">
            <table class="pyq-table">
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Exam Pattern & Weightage</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Question Frequency</strong></td>
                        <td>{pyq_data.get('frequency', '1-2 questions per test')}</td>
                    </tr>
                    <tr>
                        <td><strong>Module 1 Appearance</strong></td>
                        <td>{pyq_data.get('module1_weight', 'Medium Frequency (Foundational tests)')}</td>
                    </tr>
                    <tr>
                        <td><strong>Module 2 Appearance</strong></td>
                        <td>{pyq_data.get('module2_weight', 'High Frequency (Score differentiator)')}</td>
                    </tr>
                    <tr>
                        <td><strong>Pattern Analysis</strong></td>
                        <td>{pyq_data.get('historical_pattern', 'Regularly tests vertex shifts and extraneous solutions.')}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="background:var(--bg-subtle); border-radius:var(--radius-lg); padding:28px; text-align:center; margin-top:28px; border:1px dashed var(--border-strong);">
            <div style="font-size:1.8rem; margin-bottom:8px;">🏛️</div>
            <h3>Official SAT PYQ Drill Bank (2023–2026)</h3>
            <p style="color:var(--ink-muted); max-width:540px; margin:8px auto 18px; font-size:0.92rem;">
                We are compiling real verified College Board exam patterns with step-by-step Desmos shortcuts for {title}.
            </p>
            <span class="btn btn-theme btn-sm" style="cursor:default;">Updated for 2026 Testing Season</span>
        </div>
    </div>
    """

    # Pre-render Tab 4: Formula Sheet
    formula_items = "".join([f"""
    <div class="formula-card">
        <h3>{f.get('name', '')}</h3>
        <div style="font-size:1.15rem; margin-bottom:8px; font-weight:700; color:var(--ink-main);">{f.get('formula', '')}</div>
        <p style="font-size:0.88rem; color:var(--ink-muted);">{f.get('description', '')}</p>
    </div>
    """ for f in data.get("formula_sheet", {}).get("core_formulas", [])])
    
    traps_items = "".join([f"""
    <div class="trap-card">
        <div class="trap-title">⚠️ SAT Trap: {t.get('title', '')}</div>
        <div class="trap-desc">{t.get('description', '')}</div>
    </div>
    """ for t in data.get("formula_sheet", {}).get("sat_traps", [])])

    desmos_items = "".join([f"""
    <div style="background:var(--bg-subtle); border-radius:var(--radius-md); padding:16px; margin-bottom:12px; border:1px solid var(--border-subtle);">
        <div style="font-weight:800; font-size:0.92rem; color:var(--theme-dark); margin-bottom:4px;">🎯 {d.get('tactic', '')}</div>
        <code style="display:block; background:#ffffff; padding:6px 10px; border-radius:6px; font-family:'JetBrains Mono',monospace; font-size:0.85rem; margin-bottom:6px; border:1px solid var(--border-subtle);">{d.get('syntax', '')}</code>
        <div style="font-size:0.82rem; color:var(--ink-muted);">{d.get('tip', '')}</div>
    </div>
    """ for d in data.get("formula_sheet", {}).get("desmos_shortcuts", [])])

    formula_panel_html = f"""
    <div>
        <div class="panel-header compact-header">
            <h2>Revision, Traps & Desmos Syntax</h2>
        </div>

        <div class="formula-grid" style="margin-bottom:32px;">
            {formula_items}
        </div>

        <div style="display:grid; grid-template-columns:1fr; gap:24px; margin-top:32px;">
            <div>
                <h3 style="margin-bottom:16px;">🚨 Top SAT Traps & Misconceptions</h3>
                {traps_items}
            </div>
            <div>
                <h3 style="margin-bottom:16px;">⚡ Essential Desmos Cheatsheet</h3>
                {desmos_items}
            </div>
        </div>
    </div>
    """

    # Pre-render Tab 5: 3-Level Mock Test (30 Questions)
    def render_mock_list(q_list, level_name):
        rendered = []
        for mq in q_list:
            opts = "".join([f"""
            <button class="option-btn mock-option-btn" data-index="{opt_idx}">
                <span class="option-label">{opt.get('label', 'A')}</span>
                <span class="option-text">{opt.get('text', '')}</span>
            </button>
            """ for opt_idx, opt in enumerate(mq.get("options", []))])

            rendered.append(f"""
            <div class="question-card mock-q-card" data-correct="{parse_correct_index(mq.get('correct_index', '0'))}">
                <div class="q-header">
                    <span class="q-number">Question {mq.get('id', 1)}</span>
                    <span class="diff-badge">{level_name}</span>
                </div>
                <div class="q-body"><p>{mq.get('question', '')}</p></div>
                <div class="options-grid">{opts}</div>
                <div class="mock-solution" style="display:none; margin-top:14px; padding:12px 16px; background:var(--bg-subtle); border-radius:var(--radius-sm); font-size:0.88rem;">
                    <strong>Explanation:</strong>
                    {format_steps(mq.get('explanation', ''))}
                </div>
            </div>
            """)
        return "".join(rendered)

    mock_data = data.get("mock_tests", {})
    l1_html = render_mock_list(mock_data.get("level1_foundation", []), "Level 1: Foundation")
    l2_html = render_mock_list(mock_data.get("level2_target700", []), "Level 2: Target 700+")
    l3_html = render_mock_list(mock_data.get("level3_800mastery", []), "Level 3: 800 Mastery")

    mock_panel_html = f"""
    <div>
        <div class="panel-header compact-header">
            <h2>3-Level Mock Test (30 Questions)</h2>
        </div>

        <div class="mock-level-selector">
            <div class="level-card active" data-level="1">
                <div class="level-title">🟢 Level 1: Foundation</div>
                <div class="level-sub">10 Qs · Sub-600 Score</div>
            </div>
            <div class="level-card" data-level="2">
                <div class="level-title">🟡 Level 2: Target 700+</div>
                <div class="level-sub">10 Qs · 600–740 Score</div>
            </div>
            <div class="level-card" data-level="3">
                <div class="level-title">🔴 Level 3: 800-Mastery</div>
                <div class="level-sub">10 Qs · 750–800 Score</div>
            </div>
        </div>

        <div class="mock-level-content" data-level="1">
            {l1_html}
        </div>
        <div class="mock-level-content" data-level="2" style="display:none;">
            {l2_html}
        </div>
        <div class="mock-level-content" data-level="3" style="display:none;">
            {l3_html}
        </div>
    </div>
    """

    # Full HTML Page Template
    html_page = f"""<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - Digital SAT Math: Concepts, {practice_count}+ Practice Questions & Shortcuts | SJMaths</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <meta name="theme-color" content="#6366f1">
    <meta name="color-scheme" content="light">

    <!-- Open Graph -->
    <meta property="og:title" content="{title} - Digital SAT Math: Concepts, Practice & Tricks | SJMaths">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="article">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {json.dumps(schema_data, indent=2)}
    </script>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

    <!-- Stylesheet -->
    <link rel="stylesheet" href="/assets/css/sat-topic.min.css">

    <!-- MathJax 3 for LaTeX formula rendering -->
    <script src="/assets/js/sat-topic.min.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

<body data-theme="{domain_slug}">
    <!-- Navigation -->
    <header class="nav">
        <div class="wrap nav-in">
            <a href="/" class="brand" aria-label="SJMaths Home">
                <span class="brand-symbol" aria-hidden="true">∫</span><span class="brand-name">SJ<span>Maths</span></span>
                <span class="brand-badge">{domain_name}</span>
            </a>

            <nav class="nav-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/{domain_slug}/">{domain_name}</a>
                <a href="/sat/diagnostic/">Diagnostic</a>
                <a href="/sat/mock-tests/">Mock Tests</a>
            </nav>

            <a href="/sat/diagnostic/" class="btn btn-theme btn-nav-action">Free Diagnostic</a>
        </div>
    </header>

    <!-- Hero Header -->
    <header class="topic-hero">
        <div class="wrap">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
                <a href="/">Home</a>
                <span class="separator">/</span>
                <a href="/sat/">SAT Hub</a>
                <span class="separator">/</span>
                <a href="/sat/{domain_slug}/">{domain_name}</a>
                <span class="separator">/</span>
                <span class="current">{title}</span>
            </nav>

            <div class="topic-meta-row">
                <span class="domain-pill">{domain_name}</span>
                <span class="meta-badge-subtle">⚡ {data.get('exam_weightage', 'High Yield')}</span>
            </div>

            <h1 class="topic-title">{title}</h1>
            <p class="topic-hero-sub">Digital SAT Math Preparation & Desmos Strategies</p>

            <div class="hero-chips-row">
                <span class="hero-chip"><strong class="chip-num">{len(data.get('concepts', []))}</strong> Concepts</span>
                <span class="hero-chip"><strong class="chip-num">{practice_count}</strong> Practice Qs</span>
                <span class="hero-chip"><strong class="chip-num">30</strong> Mock Qs</span>
                <span class="hero-chip hero-chip-accent">⚡ Desmos Speed Hacks</span>
            </div>
        </div>
    </header>

    <!-- App Bottom Navigation (Mobile) / Sticky Top Tabs (Desktop) -->
    <nav class="tab-nav-wrapper" aria-label="Topic Navigation Tabs">
        <div class="wrap">
            <div class="tab-nav-list">
                <button class="tab-btn active" data-tab="learn">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
                    </span>
                    <span class="tab-label">Learn</span>
                </button>
                <button class="tab-btn" data-tab="practice">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                        <span class="tab-count-badge">{practice_count}</span>
                    </span>
                    <span class="tab-label">Practice</span>
                </button>
                <button class="tab-btn" data-tab="pyqs">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="21" x2="21" y2="21"/><line x1="4" y1="10" x2="20" y2="10"/><polygon points="12 2 2 7 22 7 12 2"/><line x1="6" y1="10" x2="6" y2="21"/><line x1="10" y1="10" x2="10" y2="21"/><line x1="14" y1="10" x2="14" y2="21"/><line x1="18" y1="10" x2="18" y2="21"/></svg>
                    </span>
                    <span class="tab-label">PYQs</span>
                </button>
                <button class="tab-btn" data-tab="formulas">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                    </span>
                    <span class="tab-label">Formulas</span>
                </button>
                <button class="tab-btn" data-tab="mock-test">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                        <span class="tab-count-badge">30Q</span>
                    </span>
                    <span class="tab-label">Mock</span>
                </button>
            </div>
        </div>
    </nav>

    <!-- Main Content Panels -->
    <main class="tab-panels-container">
        <div class="wrap">
            <!-- Tab 1: Learn -->
            <section id="learn" class="tab-panel active" aria-labelledby="tab-learn">
                <div class="panel-header compact-header">
                    <h2>Key Concepts & Worked Archetypes</h2>
                </div>
                {learn_panel_html}
            </section>

            <!-- Tab 2: Practice -->
            <section id="practice" class="tab-panel" aria-labelledby="tab-practice">
                <div class="panel-header compact-header">
                    <h2>Practice Questions ({practice_count})</h2>
                </div>
                <div class="practice-filters">
                    <button class="filter-chip active" data-filter="all">All Questions ({practice_count})</button>
                    {filters_html}
                </div>
                {practice_panel_html}
            </section>

            <!-- Tab 3: PYQs -->
            <section id="pyqs" class="tab-panel" aria-labelledby="tab-pyqs">
                {pyq_panel_html}
            </section>

            <!-- Tab 4: Formula Sheet -->
            <section id="formulas" class="tab-panel" aria-labelledby="tab-formulas">
                {formula_panel_html}
            </section>

            <!-- Tab 5: Mock Test -->
            <section id="mock-test" class="tab-panel" aria-labelledby="tab-mock-test">
                {mock_panel_html}
            </section>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <div class="wrap footer-in">
            <a href="/" class="brand">
                <span class="brand-symbol">∫</span><span class="brand-name">SJ<span>Maths</span></span>
            </a>
            <div>© 2026 SJMaths. Targeted Digital SAT Math Preparation.</div>
            <div class="footer-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/algebra/">Algebra</a>
                <a href="/sat/advanced-math/">Advanced Math</a>
                <a href="/sat/problem-solving-data-analysis/">Data Analysis</a>
                <a href="/sat/geometry-trigonometry/">Geometry & Trig</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""
    return html_page


def render_desmos_page(data, slug):
    """Render 3-Tab Desmos Calculator Guide Page."""
    title = data.get("topic_title", "Desmos Strategy")
    meta_desc = data.get("seo_meta_description", f"Master Desmos techniques for {title} on Digital SAT Math.")
    canonical_url = f"https://sjmaths.com/sat/{slug}/"
    parts = slug.split("/")
    domain_slug = parts[0]
    topic_slug = parts[1]

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/"},
                    {"@type": "ListItem", "position": 2, "name": "SAT Hub", "item": "https://sjmaths.com/sat/"},
                    {"@type": "ListItem", "position": 3, "name": "Desmos Mastery", "item": "https://sjmaths.com/sat/desmos/"},
                    {"@type": "ListItem", "position": 4, "name": title, "item": canonical_url}
                ]
            },
            {
                "@type": "LearningResource",
                "name": f"{title} - Desmos Digital SAT Math Strategy",
                "description": meta_desc,
                "educationalLevel": "High School / SAT Prep",
                "learningResourceType": "Calculator Guide & Practice",
                "provider": {"@type": "Organization", "name": "SJMaths", "url": "https://sjmaths.com/"}
            }
        ]
    }

    # Tab 1: Technique & Syntax
    techniques_html = []
    for idx, t in enumerate(data.get("techniques", []), 1):
        techniques_html.append(f"""
        <div class="desmos-syntax-card">
            <div class="desmos-syntax-header">
                <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.15rem; font-weight:800; color:var(--ink-main);">{t.get('title', '')}</h3>
                <span class="diff-badge" style="background:#ecfdf5; color:#047857;">{t.get('when_to_use', 'High Speed')}</span>
            </div>
            <code class="desmos-syntax-code">{t.get('syntax', '')}</code>
            <p style="margin:10px 0; font-size:0.92rem; line-height:1.6; color:var(--ink-main);">{t.get('description', '')}</p>
            <div style="margin-top:12px; font-size:0.86rem; color:#065f46; background:#f0fdf4; border:1px solid #bbf7d0; padding:10px 14px; border-radius:var(--radius-sm);">
                <strong>💡 Pro-Tip:</strong> {t.get('pro_tip', '')}
            </div>
        </div>
        """)
    tab1_html = "".join(techniques_html)

    # Tab 2: Speed Walkthroughs
    walkthroughs_html = []
    for idx, w in enumerate(data.get("speed_walkthroughs", []), 1):
        walkthroughs_html.append(f"""
        <div class="walkthrough-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
                <span class="q-number" style="font-family:'Space Grotesk',sans-serif; font-weight:800; font-size:0.95rem; color:var(--theme-dark);">Walkthrough #{idx}</span>
                <span class="time-saved-badge">{w.get('time_saved', '⚡ Fast Hack')}</span>
            </div>
            <div class="q-body" style="font-size:1rem; margin-bottom:16px; line-height:1.65;"><p>{w.get('problem', '')}</p></div>
            <div class="walkthrough-comparison">
                <div class="method-box traditional">
                    <div class="method-title">⏳ Traditional 2-Minute Method</div>
                    {format_steps(w.get('traditional_method', ''))}
                </div>
                <div class="method-box desmos">
                    <div class="method-title">⚡ Desmos 15-Second Hack</div>
                    {format_steps(w.get('desmos_hack', ''))}
                    <div style="margin-top:14px; padding-top:10px; border-top:1px dashed #a7f3d0; font-weight:700; color:#047857; font-size:0.9rem;">
                        Target Answer: {w.get('answer', '')}
                    </div>
                </div>
            </div>
        </div>
        """)
    tab2_html = "".join(walkthroughs_html)

    # Tab 3: Calculator Drills
    drills_html = []
    for idx, q in enumerate(data.get("drills", []), 1):
        qtype = q.get("qtype", "mcq")
        if qtype == "spr":
            ans = str(q.get("spr_answer", ""))
            drills_html.append(f"""
            <div class="spr-card practice-card" data-qtype="spr" data-answer="{ans}">
                <div class="q-header">
                    <span class="q-number">Drill #{idx} (SPR)</span>
                    <span class="diff-badge">⚡ Calculator Drill</span>
                </div>
                <div class="q-body"><p>{q.get('question', '')}</p></div>
                <div class="spr-container">
                    <span class="spr-badge-label">Desmos Calculator Grid-In</span>
                    <div class="spr-input-row">
                        <input type="text" class="spr-input" placeholder="Type answer..." data-answer="{ans}">
                        <button type="button" class="spr-check-btn">Check</button>
                    </div>
                    <div class="spr-feedback" style="display:none;"></div>
                </div>
                <div style="margin:12px 0; padding:10px 14px; background:#1e1e2e; color:#a6e3a1; border-radius:var(--radius-sm); font-family:'JetBrains Mono',monospace; font-size:0.86rem;">
                    <strong>Desmos Entry:</strong> {q.get('desmos_command', '')}
                </div>
                <div class="card-actions">
                    <button class="btn-toggle-solution">Step-by-Step Solution</button>
                </div>
                <div class="solution-drawer">
                    <div class="solution-block desmos">
                        <h4>Desmos Walkthrough & Verification</h4>
                        {format_steps(q.get('explanation', ''))}
                    </div>
                </div>
            </div>
            """)
        else:
            correct_idx = parse_correct_index(q.get("correct_index", 0))
            opts_html = []
            for opt in q.get("options", []):
                o_label = opt.get("label", "A")
                o_idx = ord(o_label) - ord("A") if len(o_label) == 1 else 0
                opts_html.append(f"""
                <button class="option-btn" data-index="{o_idx}">
                    <span class="option-letter">{o_label}</span>
                    <span class="option-text">{opt.get('text', '')}</span>
                </button>
                """)
            drills_html.append(f"""
            <div class="practice-card" data-type="mcq" data-correct="{correct_idx}">
                <div class="q-header">
                    <span class="q-number">Drill #{idx}</span>
                    <span class="diff-badge">⚡ Calculator Drill</span>
                </div>
                <div class="q-body"><p>{q.get('question', '')}</p></div>
                <div class="options-grid">{''.join(opts_html)}</div>
                <div style="margin:12px 0; padding:10px 14px; background:#1e1e2e; color:#a6e3a1; border-radius:var(--radius-sm); font-family:'JetBrains Mono',monospace; font-size:0.86rem;">
                    <strong>Desmos Entry:</strong> {q.get('desmos_command', '')}
                </div>
                <div class="card-actions">
                    <button class="btn-check-answer">Check Answer</button>
                    <button class="btn-toggle-solution">Step-by-Step Solution</button>
                </div>
                <div class="solution-drawer">
                    <div class="solution-block desmos">
                        <h4>Desmos Walkthrough & Verification</h4>
                        {format_steps(q.get('explanation', ''))}
                    </div>
                </div>
            </div>
            """)
    tab3_html = "".join(drills_html)

    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - Desmos Digital SAT Math Shortcuts & Speed Drills | SJMaths</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <meta name="theme-color" content="#10b981">
    <meta name="color-scheme" content="light">

    <meta property="og:title" content="{title} - Desmos Digital SAT Math Shortcuts | SJMaths">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="article">

    <script type="application/ld+json">
    {json.dumps(schema_data, indent=2)}
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/sat-topic.min.css">
    <script src="/assets/js/sat-topic.min.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

<body data-theme="desmos">
    <header class="nav">
        <div class="wrap nav-in">
            <a href="/" class="brand" aria-label="SJMaths Home">
                <span class="brand-symbol" aria-hidden="true">∫</span><span class="brand-name">SJ<span>Maths</span></span>
                <span class="brand-badge" style="background:#ecfdf5; color:#047857; border:1px solid #a7f3d0;">DESMOS</span>
            </a>
            <nav class="nav-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/desmos/">Desmos Mastery</a>
                <a href="/sat/diagnostic/">Diagnostic</a>
                <a href="/sat/mock-tests/">Mock Tests</a>
            </nav>
            <a href="/sat/diagnostic/" class="btn btn-theme btn-nav-action">Free Diagnostic</a>
        </div>
    </header>

    <header class="topic-hero">
        <div class="wrap">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
                <a href="/">Home</a>
                <span class="separator">/</span>
                <a href="/sat/">SAT Hub</a>
                <span class="separator">/</span>
                <a href="/sat/desmos/">Desmos Mastery</a>
                <span class="separator">/</span>
                <span class="current">{title}</span>
            </nav>

            <div class="topic-meta-row">
                <span class="domain-pill" style="background:#ecfdf5; color:#047857; border-color:#a7f3d0;">⚡ DESMOS CALCULATOR</span>
                <span class="meta-badge-subtle">⚡ {data.get('exam_weightage', 'High Yield')}</span>
            </div>

            <h1 class="topic-title">{title}</h1>
            <p class="topic-hero-sub">Digital SAT Math Desmos Hacks, Keystrokes & Speed Walkthroughs</p>

            <div class="hero-chips-row">
                <span class="hero-chip"><strong class="chip-num">{len(data.get('techniques', []))}</strong> Syntax Rules</span>
                <span class="hero-chip"><strong class="chip-num">{len(data.get('speed_walkthroughs', []))}</strong> Speed Hacks</span>
                <span class="hero-chip"><strong class="chip-num">{len(data.get('drills', []))}</strong> Calculator Drills</span>
            </div>
        </div>
    </header>

    <nav class="tab-nav-wrapper" aria-label="Desmos Guide Tabs">
        <div class="wrap">
            <div class="tab-nav-list">
                <button class="tab-btn active" data-tab="syntax">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>
                        <span class="tab-count-badge">{len(data.get('techniques', []))}</span>
                    </span>
                    <span class="tab-label">Technique & Syntax</span>
                </button>
                <button class="tab-btn" data-tab="walkthroughs">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
                        <span class="tab-count-badge">{len(data.get('speed_walkthroughs', []))}</span>
                    </span>
                    <span class="tab-label">Speed Walkthroughs</span>
                </button>
                <button class="tab-btn" data-tab="drills">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                        <span class="tab-count-badge">{len(data.get('drills', []))}</span>
                    </span>
                    <span class="tab-label">Calculator Drills</span>
                </button>
            </div>
        </div>
    </nav>

    <main class="tab-panels-container">
        <div class="wrap">
            <section id="syntax" class="tab-panel active">
                <div class="panel-header compact-header">
                    <h2>Desmos Syntax & Core Techniques</h2>
                </div>
                {tab1_html}
            </section>

            <section id="walkthroughs" class="tab-panel">
                <div class="panel-header compact-header">
                    <h2>Speed Walkthroughs: 15s Desmos Hack vs 2-Min Algebra</h2>
                </div>
                {tab2_html}
            </section>

            <section id="drills" class="tab-panel">
                <div class="panel-header compact-header">
                    <h2>Targeted Calculator Drills ({len(data.get('drills', []))} Questions)</h2>
                </div>
                {tab3_html}
            </section>
        </div>
    </main>

    <footer>
        <div class="wrap footer-in">
            <a href="/" class="brand">
                <span class="brand-symbol">∫</span><span class="brand-name">SJ<span>Maths</span></span>
            </a>
            <div>© 2026 SJMaths. Targeted Digital SAT Math Preparation.</div>
            <div class="footer-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/desmos/">Desmos Mastery</a>
                <a href="/sat/student-produced-response/">SPR / Grid-In</a>
                <a href="/sat/guides/">Strategy Guides</a>
            </div>
        </div>
    </footer>
</body>
</html>"""

def render_spr_page(data, slug):
    """Render 3-Tab Student-Produced Response (SPR) Page."""
    title = data.get("topic_title", "Student-Produced Response")
    meta_desc = data.get("seo_meta_description", f"Master SPR Grid-In rules and practice for {title} on Digital SAT Math.")
    canonical_url = f"https://sjmaths.com/sat/{slug}/"
    parts = slug.split("/")
    domain_slug = parts[0]
    topic_slug = parts[1]

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/"},
                    {"@type": "ListItem", "position": 2, "name": "SAT Hub", "item": "https://sjmaths.com/sat/"},
                    {"@type": "ListItem", "position": 3, "name": "Student-Produced Response", "item": "https://sjmaths.com/sat/student-produced-response/"},
                    {"@type": "ListItem", "position": 4, "name": title, "item": canonical_url}
                ]
            },
            {
                "@type": "LearningResource",
                "name": f"{title} - SAT Math Grid-In Rules & Practice",
                "description": meta_desc,
                "educationalLevel": "High School / SAT Prep",
                "learningResourceType": "Exam Practice & Rules",
                "provider": {"@type": "Organization", "name": "SJMaths", "url": "https://sjmaths.com/"}
            }
        ]
    }

    # Tab 1: Official Rules
    rules_html = []
    for idx, r in enumerate(data.get("official_rules", []), 1):
        rules_html.append(f"""
        <div class="concept-card" style="margin-bottom:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <span class="concept-badge">{r.get('rule_number', f'Rule {idx}')}</span>
                <span class="diff-badge" style="background:#fef3c7; color:#92400e;">Official Bluebook Rule</span>
            </div>
            <h3 style="margin-bottom:8px; font-size:1.15rem;">{r.get('title', '')}</h3>
            <p style="margin-bottom:14px; font-size:0.92rem; color:var(--ink-main); line-height:1.6;">{r.get('summary', '')}</p>
            
            <div style="display:grid; grid-template-columns:1fr; gap:12px; margin-bottom:12px;">
                <div style="background:#ecfdf5; border:1.5px solid #a7f3d0; padding:12px 16px; border-radius:var(--radius-sm);">
                    <div style="font-weight:800; color:#065f46; font-size:0.84rem; text-transform:uppercase; margin-bottom:4px;">✓ DO THIS:</div>
                    <div style="font-size:0.9rem; color:#047857;">{r.get('do_this', '')}</div>
                </div>
                <div style="background:#fef2f2; border:1.5px solid #fecaca; padding:12px 16px; border-radius:var(--radius-sm);">
                    <div style="font-weight:800; color:#991b1b; font-size:0.84rem; text-transform:uppercase; margin-bottom:4px;">✗ NEVER DO THIS:</div>
                    <div style="font-size:0.9rem; color:#b91c1c;">{r.get('never_do_this', '')}</div>
                </div>
            </div>
            <div style="font-size:0.86rem; color:var(--ink-muted); font-style:italic;">
                Example: {r.get('example', '')}
            </div>
        </div>
        """)
    tab1_html = "".join(rules_html)

    # Tab 2: Common Traps
    traps_html = []
    for idx, t in enumerate(data.get("common_traps", []), 1):
        traps_html.append(f"""
        <div class="trap-card" style="padding:18px 20px; margin-bottom:18px; border-radius:var(--radius-md);">
            <div class="trap-title" style="font-size:1.05rem; margin-bottom:6px;">⚠️ Trap #{idx}: {t.get('trap_title', '')}</div>
            <p style="margin-bottom:12px; font-size:0.92rem; color:#78350f;">{t.get('scenario', '')}</p>
            <div style="display:flex; gap:16px; flex-wrap:wrap; margin-bottom:10px;">
                <div style="padding:6px 12px; background:#fee2e2; border-radius:var(--radius-sm); font-size:0.86rem; color:#991b1b; font-weight:700;">
                    ✗ Flawed Input: {t.get('flawed_input', '')} (0 Points)
                </div>
                <div style="padding:6px 12px; background:#dcfce7; border-radius:var(--radius-sm); font-size:0.86rem; color:#166534; font-weight:700;">
                    ✓ Correct Input: {t.get('correct_input', '')} (1 Point)
                </div>
            </div>
            <div style="font-size:0.86rem; color:#92400e; line-height:1.5;">
                <strong>Explanation:</strong> {t.get('explanation', '')}
            </div>
        </div>
        """)
    tab2_html = "".join(traps_html)

    # Tab 3: Interactive Grid-In Simulator
    sim_html = []
    for idx, q in enumerate(data.get("simulator_questions", []), 1):
        ans = str(q.get("expected_answer", ""))
        sim_html.append(f"""
        <div class="spr-card practice-card" data-qtype="spr" data-answer="{ans}">
            <div class="q-header">
                <span class="q-number">Grid-In Question #{idx}</span>
                <span class="diff-badge">{q.get('difficulty', 'Medium')}</span>
            </div>
            <div class="q-body"><p>{q.get('question', '')}</p></div>
            <div class="spr-container">
                <span class="spr-badge-label">Digital SAT Grid-In Simulator</span>
                <div class="spr-input-row">
                    <input type="text" class="spr-input" placeholder="Type answer (e.g. 7/4 or 1.75)" data-answer="{ans}">
                    <button type="button" class="spr-check-btn">Submit Answer</button>
                </div>
                <div class="spr-rules-hint">Official Bluebook rules apply: integers, terminating or rounded decimals, and improper fractions accepted. No mixed numbers.</div>
                <div class="spr-feedback" style="display:none;"></div>
            </div>
            <div class="card-actions">
                <button class="btn-hint">Hint</button>
                <button class="btn-toggle-solution">Step-by-Step Solution</button>
            </div>
            <div class="hint-box" style="display:none;">
                <strong>Hint:</strong> {q.get('hint', '')}
            </div>
            <div class="solution-drawer">
                <div class="solution-block traditional">
                    <h4>Official Step-by-Step Solution</h4>
                    {format_steps(q.get('solution_steps', ''))}
                </div>
            </div>
        </div>
        """)
    tab3_html = "".join(sim_html)

    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} - SAT Math Grid-In Rules & Interactive Practice | SJMaths</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <meta name="theme-color" content="#d97706">
    <meta name="color-scheme" content="light">

    <meta property="og:title" content="{title} - Digital SAT SPR Rules & Practice | SJMaths">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="article">

    <script type="application/ld+json">
    {json.dumps(schema_data, indent=2)}
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/sat-topic.min.css">
    <script src="/assets/js/sat-topic.min.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

<body data-theme="student-produced-response">
    <header class="nav">
        <div class="wrap nav-in">
            <a href="/" class="brand" aria-label="SJMaths Home">
                <span class="brand-symbol" aria-hidden="true">∫</span><span class="brand-name">SJ<span>Maths</span></span>
                <span class="brand-badge" style="background:#fffbeb; color:#92400e; border:1px solid #fde68a;">SPR / GRID-IN</span>
            </a>
            <nav class="nav-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/student-produced-response/">SPR / Grid-In</a>
                <a href="/sat/diagnostic/">Diagnostic</a>
                <a href="/sat/mock-tests/">Mock Tests</a>
            </nav>
            <a href="/sat/diagnostic/" class="btn btn-theme btn-nav-action">Free Diagnostic</a>
        </div>
    </header>

    <header class="topic-hero">
        <div class="wrap">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
                <a href="/">Home</a>
                <span class="separator">/</span>
                <a href="/sat/">SAT Hub</a>
                <span class="separator">/</span>
                <a href="/sat/student-produced-response/">SPR Mastery</a>
                <span class="separator">/</span>
                <span class="current">{title}</span>
            </nav>

            <div class="topic-meta-row">
                <span class="domain-pill" style="background:#fffbeb; color:#92400e; border-color:#fde68a;">✏️ STUDENT-PRODUCED RESPONSE</span>
                <span class="meta-badge-subtle">⚡ {data.get('exam_weightage', '25% of Math Exam')}</span>
            </div>

            <h1 class="topic-title">{title}</h1>
            <p class="topic-hero-sub">Official Digital SAT Grid-In Formatting Rules, Traps & Interactive Practice</p>

            <div class="hero-chips-row">
                <span class="hero-chip"><strong class="chip-num">{len(data.get('official_rules', []))}</strong> Official Rules</span>
                <span class="hero-chip"><strong class="chip-num">{len(data.get('common_traps', []))}</strong> Traps & Mistakes</span>
                <span class="hero-chip"><strong class="chip-num">{len(data.get('simulator_questions', []))}</strong> Simulator Qs</span>
            </div>
        </div>
    </header>

    <nav class="tab-nav-wrapper" aria-label="SPR Guide Tabs">
        <div class="wrap">
            <div class="tab-nav-list">
                <button class="tab-btn active" data-tab="rules">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                        <span class="tab-count-badge">{len(data.get('official_rules', []))}</span>
                    </span>
                    <span class="tab-label">Official Grid-In Rules</span>
                </button>
                <button class="tab-btn" data-tab="traps">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                        <span class="tab-count-badge">{len(data.get('common_traps', []))}</span>
                    </span>
                    <span class="tab-label">Common Traps</span>
                </button>
                <button class="tab-btn" data-tab="simulator">
                    <span class="tab-icon-wrap">
                        <svg class="tab-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                        <span class="tab-count-badge">{len(data.get('simulator_questions', []))}</span>
                    </span>
                    <span class="tab-label">Grid-In Simulator</span>
                </button>
            </div>
        </div>
    </nav>

    <main class="tab-panels-container">
        <div class="wrap">
            <section id="rules" class="tab-panel active">
                <div class="panel-header compact-header">
                    <h2>Official Bluebook Grid-In Rules</h2>
                </div>
                {tab1_html}
            </section>

            <section id="traps" class="tab-panel">
                <div class="panel-header compact-header">
                    <h2>Common Grid-In Traps That Cost Points</h2>
                </div>
                {tab2_html}
            </section>

            <section id="simulator" class="tab-panel">
                <div class="panel-header compact-header">
                    <h2>Interactive Grid-In Practice Simulator ({len(data.get('simulator_questions', []))} Questions)</h2>
                </div>
                {tab3_html}
            </section>
        </div>
    </main>

    <footer>
        <div class="wrap footer-in">
            <a href="/" class="brand">
                <span class="brand-symbol">∫</span><span class="brand-name">SJ<span>Maths</span></span>
            </a>
            <div>© 2026 SJMaths. Targeted Digital SAT Math Preparation.</div>
            <div class="footer-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/student-produced-response/">SPR / Grid-In</a>
                <a href="/sat/desmos/">Desmos Mastery</a>
                <a href="/sat/guides/">Strategy Guides</a>
            </div>
        </div>
    </footer>
</body>
</html>"""

def render_guide_page(data, slug):
    """Render Editorial Long-Form SAT Strategy Guide (sat/guides)."""
    title = data.get("title", "Digital SAT Math Strategy Guide")
    meta_desc = data.get("seo_meta_description", f"Comprehensive Digital SAT Math strategy guide for {title}.")
    canonical_url = f"https://sjmaths.com/sat/{slug}/"
    parts = slug.split("/")
    domain_slug = parts[0]
    topic_slug = parts[1]

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/"},
                    {"@type": "ListItem", "position": 2, "name": "SAT Hub", "item": "https://sjmaths.com/sat/"},
                    {"@type": "ListItem", "position": 3, "name": "Strategy Guides", "item": "https://sjmaths.com/sat/guides/"},
                    {"@type": "ListItem", "position": 4, "name": title, "item": canonical_url}
                ]
            },
            {
                "@type": "Article",
                "headline": title,
                "description": meta_desc,
                "author": {"@type": "Organization", "name": "SJMaths"},
                "publisher": {"@type": "Organization", "name": "SJMaths", "url": "https://sjmaths.com/"},
                "datePublished": "2026-01-01",
                "dateModified": "2026-09-01"
            }
        ]
    }

    # Build TOC & Sections
    toc_html = []
    sections_html = []

    for idx, s in enumerate(data.get("sections", []), 1):
        s_id = s.get("id", f"section-{idx}")
        s_heading = s.get("heading", f"Section {idx}")
        toc_html.append(f'<li><a href="#{s_id}">{s_heading}</a></li>')

        # Paragraphs
        p_html = "".join([f"<p>{p}</p>" for p in s.get("paragraphs", [])])

        # Callout
        callout_html = ""
        if s.get("callout") and isinstance(s["callout"], dict):
            c_title = s["callout"].get("title", "Key Takeaway")
            c_text = s["callout"].get("text", "")
            callout_html = f"""
            <div class="guide-callout">
                <div class="guide-callout-title">📌 {c_title}</div>
                <p style="margin:0;">{c_text}</p>
            </div>
            """

        # Bullet Points
        bullets_html = ""
        if s.get("bullet_points") and isinstance(s["bullet_points"], list):
            b_items = "".join([f"<li>{b}</li>" for b in s["bullet_points"]])
            bullets_html = f'<ul style="margin:16px 0 20px; padding-left:24px; line-height:1.7;">{b_items}</ul>'

        # Table
        table_html = ""
        if s.get("table") and isinstance(s["table"], dict):
            headers = s["table"].get("headers", [])
            rows = s["table"].get("rows", [])
            if headers and rows:
                th_str = "".join([f"<th style='padding:10px 14px; background:var(--bg-subtle); text-align:left; border-bottom:2px solid var(--border-subtle); font-size:0.88rem;'>{h}</th>" for h in headers])
                tr_list = []
                for row in rows:
                    td_str = "".join([f"<td style='padding:10px 14px; border-bottom:1px solid var(--border-subtle); font-size:0.88rem;'>{c}</td>" for c in row])
                    tr_list.append(f"<tr>{td_str}</tr>")
                table_html = f"""
                <div style="overflow-x:auto; margin:20px 0; border:1px solid var(--border-subtle); border-radius:var(--radius-md);">
                    <table style="width:100%; border-collapse:collapse;">
                        <thead><tr>{th_str}</tr></thead>
                        <tbody>{''.join(tr_list)}</tbody>
                    </table>
                </div>
                """

        sections_html.append(f"""
        <section id="{s_id}" style="scroll-margin-top:100px; margin-bottom:40px;">
            <h2>{s_heading}</h2>
            {p_html}
            {callout_html}
            {bullets_html}
            {table_html}
        </section>
        """)

    # FAQ
    faq_html = []
    for f in data.get("faq", []):
        faq_html.append(f"""
        <div style="margin-bottom:18px; padding:18px 22px; background:var(--bg-surface); border:1px solid var(--border-subtle); border-radius:var(--radius-md);">
            <h3 style="font-size:1.05rem; margin-bottom:8px; color:var(--theme-dark);">{f.get('question', '')}</h3>
            <p style="margin:0; font-size:0.92rem; line-height:1.65; color:var(--ink-main);">{f.get('answer', '')}</p>
        </div>
        """)

    takeaways_li = "".join([f"<li><strong>{t}</strong></li>" for t in data.get("key_takeaways", [])])

    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} | SJMaths Digital SAT Prep</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index,follow,max-image-preview:large">
    <meta name="theme-color" content="#4f46e5">
    <meta name="color-scheme" content="light">

    <meta property="og:title" content="{title} | SJMaths">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="article">

    <script type="application/ld+json">
    {json.dumps(schema_data, indent=2)}
    </script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/sat-topic.min.css">
    <script src="/assets/js/sat-topic.min.js"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

<body data-theme="guides">
    <header class="nav">
        <div class="wrap nav-in">
            <a href="/" class="brand" aria-label="SJMaths Home">
                <span class="brand-symbol" aria-hidden="true">∫</span><span class="brand-name">SJ<span>Maths</span></span>
                <span class="brand-badge" style="background:#eef2ff; color:#4338ca; border:1px solid #c7d2fe;">GUIDES</span>
            </a>
            <nav class="nav-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/guides/">Strategy Guides</a>
                <a href="/sat/diagnostic/">Diagnostic</a>
                <a href="/sat/mock-tests/">Mock Tests</a>
            </nav>
            <a href="/sat/diagnostic/" class="btn btn-theme btn-nav-action">Free Diagnostic</a>
        </div>
    </header>

    <header class="topic-hero">
        <div class="wrap">
            <nav class="breadcrumbs" aria-label="Breadcrumb">
                <a href="/">Home</a>
                <span class="separator">/</span>
                <a href="/sat/">SAT Hub</a>
                <span class="separator">/</span>
                <a href="/sat/guides/">Strategy Guides</a>
                <span class="separator">/</span>
                <span class="current">{title}</span>
            </nav>

            <div class="topic-meta-row">
                <span class="domain-pill" style="background:#eef2ff; color:#4338ca; border-color:#c7d2fe;">📚 STRATEGY GUIDE</span>
                <span class="meta-badge-subtle">⏱️ {data.get('read_time', '12 min read')}</span>
                <span class="meta-badge-subtle">🔄 {data.get('last_updated', '2026 Edition')}</span>
            </div>

            <h1 class="topic-title">{title}</h1>
            <p class="topic-hero-sub">In-Depth Strategic Playbook for Digital SAT Math Mastery</p>
        </div>
    </header>

    <main>
        <div class="wrap guide-article-wrap">
            <aside class="guide-toc-sidebar">
                <div class="guide-toc-card">
                    <div class="guide-toc-title">Table of Contents</div>
                    <ul class="guide-toc-list">
                        <li><a href="#executive-takeaways">Executive Overview</a></li>
                        {''.join(toc_html)}
                        <li><a href="#faq">Frequently Asked Questions</a></li>
                    </ul>
                </div>
            </aside>

            <article class="guide-prose">
                <div id="executive-takeaways" class="guide-callout" style="scroll-margin-top:100px;">
                    <div class="guide-callout-title">⚡ Executive Summary & Core Rules</div>
                    <p style="margin-bottom:12px;">{data.get('executive_summary', '')}</p>
                    <ul style="margin:0; padding-left:20px; line-height:1.7;">
                        {takeaways_li}
                    </ul>
                </div>

                {''.join(sections_html)}

                <div id="faq" style="scroll-margin-top:100px; margin-top:50px;">
                    <h2>Frequently Asked Questions</h2>
                    {''.join(faq_html)}
                </div>
            </article>
        </div>
    </main>

    <footer>
        <div class="wrap footer-in">
            <a href="/" class="brand">
                <span class="brand-symbol">∫</span><span class="brand-name">SJ<span>Maths</span></span>
            </a>
            <div>© 2026 SJMaths. Targeted Digital SAT Math Preparation.</div>
            <div class="footer-links">
                <a href="/sat/">SAT Hub</a>
                <a href="/sat/guides/">Strategy Guides</a>
                <a href="/sat/desmos/">Desmos Mastery</a>
                <a href="/sat/student-produced-response/">SPR / Grid-In</a>
            </div>
        </div>
    </footer>
</body>
</html>"""

def generate_topic(domain_slug, topic_slug, api_key, force=False, model="tiered"):
    """Generate dataset and HTML for a single topic."""
    cache_file = os.path.join(CACHE_DIR, f"{domain_slug}_{topic_slug}.json")
    topic_title = topic_slug.replace("-", " ").title()
    domain_title = domain_slug.replace("-", " ").title()

    if os.path.exists(cache_file) and not force:
        print(f"[{domain_slug}/{topic_slug}] Loading complete topic from cache: {cache_file}")
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        print(f"\n=======================================================")
        print(f"Generating [{domain_slug}/{topic_slug}] with {model}...")
        print(f"=======================================================")
        
        if domain_slug == "desmos":
            data = fetch_desmos_data(api_key, topic_title, model=model)
        elif domain_slug == "student-produced-response":
            data = fetch_spr_data(api_key, topic_title, model=model)
        elif domain_slug == "guides":
            data = fetch_guide_data(api_key, topic_title, model=model)
        else:
            part1 = fetch_concepts_and_formulas(api_key, domain_title, topic_title, model=model)
            time.sleep(1)
            part2 = fetch_practice_questions(api_key, domain_title, topic_title, model=model)
            time.sleep(1)
            part3 = fetch_mock_tests(api_key, domain_title, topic_title, model=model)

            p1 = part1 if isinstance(part1, dict) else (part1[0] if isinstance(part1, list) and part1 else {})
            p2 = part2 if isinstance(part2, dict) else {"practice_questions": part2 if isinstance(part2, list) else []}
            p3 = part3 if isinstance(part3, dict) else (part3[0] if isinstance(part3, list) and part3 else {})

            data = {
                "topic_title": p1.get("topic_title", topic_title),
                "domain_name": p1.get("domain_name", domain_title),
                "seo_meta_description": p1.get("seo_meta_description", f"Master {topic_title} for Digital SAT Math."),
                "exam_weightage": p1.get("exam_weightage", "High Yield"),
                "concepts": p1.get("concepts", []),
                "pyq_trends": p1.get("pyq_trends", {}),
                "formula_sheet": p1.get("formula_sheet", {}),
                "practice_questions": p2.get("practice_questions", []) if isinstance(p2.get("practice_questions"), list) else [],
                "mock_tests": p3.get("mock_tests", {}) if isinstance(p3.get("mock_tests"), dict) else {}
            }

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[{domain_slug}/{topic_slug}] Cached dataset successfully!")

    # Compile HTML
    target_html = os.path.join(REPO_ROOT, "sat", domain_slug, topic_slug, "index.html")
    os.makedirs(os.path.dirname(target_html), exist_ok=True)
    
    if domain_slug == "desmos":
        html_content = render_desmos_page(data, f"{domain_slug}/{topic_slug}")
    elif domain_slug == "student-produced-response":
        html_content = render_spr_page(data, f"{domain_slug}/{topic_slug}")
    elif domain_slug == "guides":
        html_content = render_guide_page(data, f"{domain_slug}/{topic_slug}")
    else:
        html_content = render_html(data, f"{domain_slug}/{topic_slug}")

    with open(target_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[{domain_slug}/{topic_slug}] Rendered static HTML -> {target_html}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate SEO-optimized SAT Topic Pages with 3-Call Pipeline")
    parser.add_argument("--topic", help="Topic path e.g. advanced-math/absolute-value")
    parser.add_argument("--domain", nargs="+", help="Generate all topics for domain(s) e.g. algebra geometry-trigonometry")
    parser.add_argument("--model", default="tiered", help="Gemini model name (or 'tiered' for 3.8 -> 3.7 -> 3.6)")
    parser.add_argument("--all", action="store_true", help="Generate all topic pages")
    parser.add_argument("--workers", type=int, default=1, help="Number of concurrent workers for multi-topic generation")
    parser.add_argument("--force", action="store_true", help="Force regenerate cache")
    args = parser.parse_args()

    api_key = load_api_key()
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in environment or .env file.")
        sys.exit(1)

    import concurrent.futures

    def run_worker(item):
        d, t = item
        try:
            generate_topic(d, t, api_key, force=args.force, model=args.model)
            return True
        except Exception as e:
            print(f"ERROR generating {d}/{t}: {e}")
            return False

    if args.topic:
        parts = args.topic.replace("\\", "/").strip("/").split("/")
        if len(parts) != 2:
            print("ERROR: Topic format must be domain/topic (e.g. advanced-math/absolute-value)")
            sys.exit(1)
        generate_topic(parts[0], parts[1], api_key, force=args.force, model=args.model)
    elif args.domain:
        for domain_name in args.domain:
            domain_dir = os.path.join(REPO_ROOT, "sat", domain_name)
            if not os.path.exists(domain_dir):
                print(f"ERROR: Domain directory not found: {domain_dir}")
                continue
            subdirs = sorted([d for d in os.listdir(domain_dir) if os.path.isdir(os.path.join(domain_dir, d)) and os.path.exists(os.path.join(domain_dir, d, "index.html"))])
            print(f"\n=======================================================")
            print(f"Domain: {domain_name} ({len(subdirs)} topics) with {args.workers} workers: {subdirs}")
            print(f"=======================================================")
            items = [(domain_name, t) for t in subdirs]
            if args.workers > 1:
                with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
                    list(executor.map(run_worker, items))
            else:
                for item in items:
                    run_worker(item)
    elif args.all:
        sat_dir = os.path.join(REPO_ROOT, "sat")
        topics = []
        for domain in os.listdir(sat_dir):
            domain_path = os.path.join(sat_dir, domain)
            if os.path.isdir(domain_path) and domain not in ["mock-tests", "diagnostic", "guides"]:
                for top in os.listdir(domain_path):
                    top_path = os.path.join(domain_path, top)
                    if os.path.isdir(top_path) and os.path.exists(os.path.join(top_path, "index.html")):
                        topics.append((domain, top))
        
        print(f"Found {len(topics)} topic pages to generate with {args.workers} workers.")
        if args.workers > 1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
                list(executor.map(run_worker, topics))
        else:
            for item in topics:
                run_worker(item)
    else:
        generate_topic("advanced-math", "absolute-value", api_key, force=args.force, model=args.model)
