# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "tenses-conditionals"
TOPIC_DISPLAY = "Tenses & Conditionals"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\english\{TOPIC}"

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "English",
    "parentUrl": "../",
    "current": "Tenses & Conditionals"
}

hero_en = {
    "title": "Tenses & Conditionals",
    "description": "Comprehensive guide on English Tenses and Conditionals for AHC RO/ARO. Master the twelve tenses, active/stative limits, four conditional types, mixed conditionals, and inversion structures."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Tenses & Conditionals Mock Test",
        "description": "Evaluate your understanding of tense rules, conditional clause pairings, and inversion structures. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Evolution of English Tenses & Moods",
    "description": "Milestones in standardizing temporal and hypothetical aspects of English grammar.",
    "cards": [
        {
            "period": "Old English Aspectual System",
            "date": "Before 1100 AD",
            "details": "Old English lacked complex future or perfect tenses, relying on simple past/present forms and prefixes (like *ge-*) to indicate completed action."
        },
        {
            "period": "Middle English Expansion",
            "date": "1100 - 1500 AD",
            "details": "Periphrastic auxiliary-driven structures emerged. The verbs 'have' and 'be' were adopted to form present/past perfect and continuous aspects."
        },
        {
            "period": "Wallis and the Future Tense",
            "date": "1653",
            "details": "Grammarian **John Wallis** formalized the rules distinguishing *shall* (first person) and *will* (second/third person) in formal English."
        },
        {
            "period": "Standardizing Conditional Moods",
            "date": "1795",
            "details": "Hypothetical clauses (Conditionals 1, 2, and 3) were codified in early pedagogical grammars, emphasizing subjunctive *were* in unreal conditions."
        },
        {
            "period": "Modern Aspectual Linguistics",
            "date": "1957",
            "details": "Syntactic structures by **Noam Chomsky** and others formalized tense as a separate auxiliary component from lexical verbs, dividing time from aspect."
        }
    ]
}

mnemonics_en = {
    "title": "Recall Mnemonics",
    "description": "Memory hooks to instantly recall tense structures and conditional pairings.",
    "items": [
        {
            "title": "Mnemonic 1: Since vs. For (Time Reference)",
            "phrase": "\"S-P vs F-D (Since-Point, For-Duration)\"",
            "decryption": "Rule of time indicators:<br>• **S**ince is used with a **P**oint of time (e.g., Since 1995, Since Monday).<br>• **F**or is used with a **D**uration of time (e.g., For 5 hours, For 2 years)."
        },
        {
            "title": "Mnemonic 2: Conditional Type 3 Pairings",
            "phrase": "\"HAD + WOULD HAVE\"",
            "decryption": "The standard structure of the Third (Past Unreal) Conditional:<br>• If-clause uses **had + Past Participle (V3)**.<br>• Main clause uses **would have + Past Participle (V3)**."
        },
        {
            "title": "Mnemonic 3: Inversion Formula",
            "phrase": "\"Drop 'If' and Swap (Had / Were / Should)\"",
            "decryption": "To create an inverted conditional, drop the word 'If' and place the auxiliary before the subject:<br>• *If I had known* -> **Had I known**<br>• *If I were a king* -> **Were I a king**<br>• *If you should need* -> **Should you need**"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "Why is 'If it will rain, we will stay inside' incorrect?",
            "answer": "Because the conditional (if) clause **cannot** take future indicators like **will** or **shall**. It must use Simple Present: \"If it **rains**, we will stay inside.\"",
            "icon": "fa-cloud-showers-heavy"
        },
        {
            "question": "What is the structural rule of the Second Conditional?",
            "answer": "It expresses unreal/hypothetical present or future states. Structure: **If + Simple Past (V2), would + Base Verb (V1)**. Subjunctive **were** is used for all subjects.",
            "icon": "fa-magic"
        },
        {
            "question": "When do you use Past Perfect vs. Simple Past for two past actions?",
            "answer": "Use **Past Perfect (had + V3)** for the earlier action (first action) and **Simple Past (V2)** for the later action (second action). E.g., \"The train **had left** before I **reached** the station.\"",
            "icon": "fa-clock"
        },
        {
            "question": "Invert this clause: 'If I were to win the lottery...'",
            "answer": "Drop 'If' and place 'Were' first: **\"Were I to win the lottery...\"**",
            "icon": "fa-random"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid (AHC RO/ARO Focus)",
    "items": [
        "<strong>Trap 1:</strong> Using double future verbs in conditional sentences. In First Conditionals, the conditional clause takes Simple Present, not future. E.g., \"If you **will work** hard, you **will pass**\" is incorrect. Correct: \"If you **work** hard, you **will pass**\".",
        "<strong>Trap 2:</strong> Incorrectly pairing 'had V3' with 'would V1' in past hypotheticals. E.g., \"If she **had studied**, she **would pass** the exam.\" This is incorrect. A past unreal condition requires: \"If she **had studied**, she **would have passed** the exam.\"",
        "<strong>Trap 3:</strong> Misplacing 'since' in present perfect continuous when a duration is given. Remember, **since** specifies the starting point (e.g., since morning), whereas **for** specifies the length of time (e.g., for three hours).",
        "<strong>Trap 4:</strong> Using progressive tenses with stative verbs to show duration. E.g., \"I am knowing him for years\" is incorrect. You must use Present Perfect: \"I **have known** him for years.\""
    ]
}

deep_dive_en = [
    {
        "title": "1. Core Tenses & Sequence Rules",
        "content": """<!-- SVG Conditionals Summary Table -->
        <svg viewBox="0 0 800 245" class="responsive-svg-diagram" style="margin:1.5rem 0; border-radius:12px; background:var(--bg-card,#ffffff); border:1px solid rgba(128,128,128,0.15); padding:15px; width:100%;">
          <style>
            .grid-header { fill: #8e44ad; font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 700; }
            .grid-cell-title { font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 700; }
            .grid-cell-text { fill: #555; font-family: 'Inter', sans-serif; font-size: 12px; }
            .header-bg { fill: rgba(142, 68, 173, 0.08); }
            .row-bg { fill: rgba(230, 126, 34, 0.05); }
            body.dark-mode .grid-cell-text { fill: #94a3b8; }
            body.dark-mode .header-bg { fill: rgba(168, 85, 247, 0.12); }
            body.dark-mode .row-bg { fill: rgba(230, 126, 34, 0.08); }
          </style>
          
          <!-- Headers -->
          <rect x="10" y="10" width="780" height="40" rx="6" class="header-bg" />
          <text x="25" y="34" class="grid-header">Conditional Type</text>
          <text x="170" y="34" class="grid-header">If-Clause Tense</text>
          <text x="360" y="34" class="grid-header">Main-Clause Tense</text>
          <text x="540" y="34" class="grid-header">Example Sentence</text>
          
          <!-- Zero Conditional -->
          <rect x="10" y="55" width="780" height="35" rx="4" class="row-bg" />
          <text x="25" y="77" class="grid-cell-title" style="fill:#e67e22;">Zero (Facts)</text>
          <text x="170" y="77" class="grid-cell-text">Simple Present</text>
          <text x="360" y="77" class="grid-cell-text">Simple Present</text>
          <text x="540" y="77" class="grid-cell-text">If you heat ice, it melts.</text>
          
          <!-- 1st Conditional -->
          <rect x="10" y="95" width="780" height="35" rx="4" class="row-bg" />
          <text x="25" y="117" class="grid-cell-title" style="fill:#e67e22;">1st (Real Future)</text>
          <text x="170" y="117" class="grid-cell-text">Simple Present</text>
          <text x="360" y="117" class="grid-cell-text">will / can + V1</text>
          <text x="540" y="117" class="grid-cell-text">If it rains, we will stay.</text>
          
          <!-- 2nd Conditional -->
          <rect x="10" y="135" width="780" height="35" rx="4" class="row-bg" />
          <text x="25" y="157" class="grid-cell-title" style="fill:#e67e22;">2nd (Unreal Pres.)</text>
          <text x="170" y="157" class="grid-cell-text">Simple Past (were)</text>
          <text x="360" y="157" class="grid-cell-text">would / could + V1</text>
          <text x="540" y="157" class="grid-cell-text">If I were rich, I would travel.</text>
          
          <!-- 3rd Conditional -->
          <rect x="10" y="175" width="780" height="35" rx="4" class="row-bg" />
          <text x="25" y="197" class="grid-cell-title" style="fill:#e67e22;">3rd (Unreal Past)</text>
          <text x="170" y="197" class="grid-cell-text">Past Perfect</text>
          <text x="360" y="197" class="grid-cell-text">would have + V3</text>
          <text x="540" y="197" class="grid-cell-text">Had I studied, I would have passed.</text>
        </svg>

        <h3>A. Present Perfect vs. Simple Past</h3>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Tense</th>
                <th>Time Markers</th>
                <th>Core Rule &amp; Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Simple Past</strong> (V2)</td>
                <td>yesterday, ago, in 2012, last week</td>
                <td>Action finished at a definite past time.<br><em>Example: "She **left** yesterday."</em></td>
              </tr>
              <tr>
                <td><strong>Present Perfect</strong> (has/have + V3)</td>
                <td>already, yet, since, for, recently</td>
                <td>Action finished in past, linked to present. Do not use past time markers.<br><em>Example: "She **has left**."</em></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>B. The Double Past Rule (Past Perfect)</h3>
        <p>When two actions happened in the past, sequence them as follows:</p>
        <ul>
          <li><strong>1st Action (Earlier):</strong> Past Perfect (<em>had + V3</em>)</li>
          <li><strong>2nd Action (Later):</strong> Simple Past (<em>V2</em>)</li>
          <li><em>Example: "The train **had left** (1st) before we **reached** (2nd) the station."</em></li>
        </ul>

        <h3>C. Sequence of Tenses</h3>
        <ul>
          <li><strong>Rule:</strong> If Principal Clause is in past, Subordinate Clause must be in past.<br><em>Example: "He said that he **was** (not 'is') studying."</em></li>
          <li><strong>Exception:</strong> Keep in Simple Present if expressing a universal truth or fact.<br><em>Example: "He proved that oil **floats** (not 'floated') on water."</em></li>
        </ul>"""
    },
    {
        "title": "2. Conditionals & Advanced Connectives",
        "content": """<h3>A. The 4 Conditional Structures</h3>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Type</th>
                <th>Condition Clause (If)</th>
                <th>Result Clause (Main)</th>
                <th>Focus Rule</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Zero</strong></td>
                <td>Simple Present</td>
                <td>Simple Present</td>
                <td>Scientific/factual truths.</td>
              </tr>
              <tr>
                <td><strong>1st</strong></td>
                <td>Simple Present</td>
                <td>will / can / may + V1</td>
                <td>Possible future. **No future verb in 'if' clause**.</td>
              </tr>
              <tr>
                <td><strong>2nd</strong></td>
                <td>Simple Past (<strong>were</strong>)</td>
                <td>would / could + V1</td>
                <td>Unreal present. Use <strong>were</strong> for all subjects.</td>
              </tr>
              <tr>
                <td><strong>3rd</strong></td>
                <td>Past Perfect (had + V3)</td>
                <td>would have + V3</td>
                <td>Unreal past hypothetical events.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>B. Unless, Until, In Case</h3>
        <ul>
          <li><strong>Unless</strong> (if not) &amp; <strong>Until</strong> (time limit): Do **not** use *not* or *will/shall* in their clauses.<br><em>Example: "Unless you **study** (not 'will not study'), you will fail."</em></li>
          <li><strong>In Case</strong> (precaution): Use present tense instead of future.<br><em>Example: "Take an umbrella in case it **rains** (not 'will rain')."</em></li>
        </ul>

        <h3>C. Mixed Conditionals</h3>
        <ul>
          <li><strong>Past Condition, Present Result:</strong> If + Past Perfect, would + V1.<br><em>Example: "If I **had won** the lottery (past), I **would be** rich today."</em></li>
          <li><strong>Present Condition, Past Result:</strong> If + Simple Past, would have + V3.<br><em>Example: "If she **were** cooperative, she **would have helped** us yesterday."</em></li>
        </ul>"""
    },
    {
        "title": "3. Inversion, Moods & Stative Shifts",
        "content": """<h3>A. Stylistic Inversion (Omitting 'If')</h3>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Type</th>
                <th>Original Structure</th>
                <th>Inverted Structure</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1st Conditional</strong></td>
                <td>If you should need help...</td>
                <td><strong>Should you</strong> need help...</td>
              </tr>
              <tr>
                <td><strong>2nd Conditional</strong></td>
                <td>If I were a king...</td>
                <td><strong>Were I</strong> a king...</td>
              </tr>
              <tr>
                <td><strong>3rd Conditional</strong></td>
                <td>If they had asked...</td>
                <td><strong>Had they</strong> asked...</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>B. Imaginary Wishes & overdue Actions</h3>
        <ul>
          <li><strong>It is high time:</strong> Followed by subject + **Simple Past (V2)**.<br><em>Example: "It is high time we **started** (not 'start') studying."</em></li>
          <li><strong>Wish / As if:</strong> Followed by subjunctive **were**.<br><em>Example: "I wish I **were** there." / "He speaks as if he **knew** everything."</em></li>
        </ul>

        <h3>C. Stative vs. Dynamic Shifts</h3>
        <p>Stative verbs (<em>know, own, belong, taste, have</em>) cannot be continuous. E.g., write <em>"I **own** a car"</em>, not <em>"I am owning"</em>.
        <br>However, if the meaning shifts to an active dynamic process, continuous is allowed:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Verb</th>
                <th>Stative (No Continuous)</th>
                <th>Dynamic (Continuous Allowed)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>have</strong></td>
                <td>I **have** a house (possession).</td>
                <td>I **am having** dinner (eating).</td>
              </tr>
              <tr>
                <td><strong>taste</strong></td>
                <td>The soup **tastes** good (state).</td>
                <td>He **is tasting** the soup (action).</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Identify the correct form of the verb to fill in the blank: 'If he ________ harder, he would have passed the exam last week.'",
        "opts": ["studied", "had studied", "studies", "would have studied"],
        "ans": 1,
        "sol": "This is a Third Conditional sentence referring to an unreal past event (indicated by 'last week' and 'would have passed'). The 'if' clause must use the Past Perfect tense ('had studied')."
    },
    {
        "q": "Choose the grammatically correct sentence from the options below:",
        "opts": [
            "If you will call me, I will come.",
            "If you call me, I will come.",
            "If you call me, I come.",
            "If you would call me, I would come."
        ],
        "ans": 1,
        "sol": "In a First Conditional sentence, the conditional clause must take the Simple Present tense ('If you call me'), and the main clause takes the simple future ('I will come')."
    },
    {
        "q": "Identify the error in the tense usage: 'The train left before we reached the station yesterday.'",
        "opts": ["left", "reached", "before", "yesterday"],
        "ans": 0,
        "sol": "When two past actions are related in time, the earlier action must be in the Past Perfect tense. The train leaving happened first, so it should be 'had left' instead of 'left'."
    },
    {
        "q": "Select the correct option to fill in the blank: 'I ________ him since we were children.'",
        "opts": ["am knowing", "have been knowing", "have known", "knew"],
        "ans": 2,
        "sol": "'Know' is a stative verb and cannot be used in continuous/progressive forms. To show duration since childhood, the Present Perfect tense ('have known') is required."
    },
    {
        "q": "Identify the correct sentence structure using inversion:",
        "opts": [
            "Had I known the truth, I would not have believed him.",
            "Had I knew the truth, I would not have believed him.",
            "If I had known the truth, I would not believe him.",
            "Would I have known the truth, I had not believed him."
        ],
        "ans": 0,
        "sol": "'Had I known' is the correct inverted form of the Third Conditional clause 'If I had known', paired correctly with the past unreal consequence 'would not have believed'."
    },
    {
        "q": "Fill in the blank: 'By this time next year, she ________ her graduation degree.'",
        "opts": ["will complete", "is completing", "will have completed", "completes"],
        "ans": 2,
        "sol": "The time marker 'By this time next year' denotes a deadline in the future, which requires the Future Perfect tense ('will have completed')."
    },
    {
        "q": "Choose the correct verb form: 'Our teacher said that the sun ________ in the east.'",
        "opts": ["rises", "rose", "has risen", "is rising"],
        "ans": 0,
        "sol": "Universal truths and scientific facts must be kept in the Simple Present tense, even if the principal reporting verb ('said') is in the past tense."
    },
    {
        "q": "Fill in the blank: 'If I ________ a king, I would help the poor.'",
        "opts": ["was", "were", "am", "had been"],
        "ans": 1,
        "sol": "This is a Second Conditional sentence expressing a hypothetical/unreal present condition. The past subjunctive 'were' must be used for all subjects."
    },
    {
        "q": "Identify the correct structure for the sentence: 'Hardly ________ entered the room when the lights went out.'",
        "opts": ["he had", "had he", "did he", "he did"],
        "ans": 1,
        "sol": "'Hardly' is a negative adverb that requires subject-auxiliary inversion when placed at the beginning of a clause. Thus, 'had he' is correct."
    },
    {
        "q": "Choose the correct sentence from the options:",
        "opts": [
            "We are living here since 2015.",
            "We have been living here since 2015.",
            "We live here since 2015.",
            "We were living here for 2015."
        ],
        "ans": 1,
        "sol": "An action that began in the past and is still continuing up to the present requires the Present Perfect Continuous tense ('have been living') with the point in time marker 'since'."
    },
    {
        "q": "Fill in the blank: 'She ________ to the market before I called her.'",
        "opts": ["goes", "has gone", "had gone", "was going"],
        "ans": 2,
        "sol": "The action of going to the market took place before another past action (calling). Therefore, the earlier action must be in the Past Perfect ('had gone')."
    },
    {
        "q": "What is the correct conditional structure: 'If he ________ rich, he would buy a yacht.'",
        "opts": ["is", "was", "were", "would be"],
        "ans": 2,
        "sol": "This represents a Second Conditional (hypothetical present/future state). The subjunctive form 'were' is used in the 'if' clause."
    },
    {
        "q": "Choose the correct verb form: 'I ________ a book when he knocked at the door.'",
        "opts": ["read", "was reading", "had read", "have read"],
        "ans": 1,
        "sol": "A continuous background action in the past ('was reading') was interrupted by a short completed action ('knocked'). Hence, Past Continuous is appropriate."
    },
    {
        "q": "Identify the correct inversion structure: '________ you need any help, do not hesitate to contact me.'",
        "opts": ["Were", "Had", "Should", "If should"],
        "ans": 2,
        "sol": "'Should you need' is the correct inverted form of the First Conditional 'If you should need'."
    },
    {
        "q": "Identify the correct form: 'Since she started her new job, she ________ extremely busy.'",
        "opts": ["is", "was", "has been", "had been"],
        "ans": 2,
        "sol": "An action or state that started in the past and has continued to the present is expressed in the Present Perfect ('has been')."
    },
    {
        "q": "Choose the correct conditional sentence:",
        "opts": [
            "If he had run fast, he would catch the train.",
            "If he ran fast, he would have caught the train.",
            "If he had run fast, he would have caught the train.",
            "If he would have run fast, he would catch the train."
        ],
        "ans": 2,
        "sol": "This is a standard Third Conditional structure: If + Past Perfect ('had run'), would have + V3 ('would have caught')."
    },
    {
        "q": "Fill in the blank: 'I ________ for the exam for three hours before my friend arrived.'",
        "opts": ["have been studying", "had been studying", "studied", "was studying"],
        "ans": 1,
        "sol": "An action that was in progress for a duration ('for three hours') before another past point ('friend arrived') must be in the Past Perfect Continuous ('had been studying')."
    },
    {
        "q": "Choose the correct option: 'Water ________ at 0 degrees Celsius.'",
        "opts": ["freezes", "froze", "will freeze", "is freezing"],
        "ans": 0,
        "sol": "Universal scientific facts are always expressed in the Simple Present tense ('freezes')."
    },
    {
        "q": "Fill in the blank: 'He behaves as if he ________ everything.'",
        "opts": ["knows", "knew", "know", "had known"],
        "ans": 1,
        "sol": "The phrase 'as if' introduces an unreal/imaginary comparison. Thus, it requires the past subjunctive form ('knew') to denote present unreality."
    },
    {
        "q": "What is the correct structure: 'No sooner ________ the station than the train left.'",
        "opts": ["we had reached", "had we reached", "we reached", "did we reached"],
        "ans": 1,
        "sol": "'No sooner' at the beginning of a sentence requires inversion of the auxiliary verb. 'had we reached' is correct, followed by 'than' for the main clause."
    },
    {
        "q": "Identify the correct form: 'It is high time we ________ studying seriously.'",
        "opts": ["start", "started", "should start", "must start"],
        "ans": 1,
        "sol": "The phrases 'It is high time' or 'It is time' are followed by the subjunctive Simple Past (V2) to express a present necessity that is overdue."
    },
    {
        "q": "Fill in the blank: 'He ________ to London last month.'",
        "opts": ["has traveled", "traveled", "had traveled", "travels"],
        "ans": 1,
        "sol": "'Last month' is a definite past time marker, which requires the Simple Past tense ('traveled')."
    },
    {
        "q": "Select the correct option: 'When I reach home, my mother ________ food.'",
        "opts": ["cooks", "will be cooking", "had cooked", "will cook"],
        "ans": 1,
        "sol": "This expresses a future action in progress at a specific time in the future, which is denoted by the Future Continuous ('will be cooking')."
    },
    {
        "q": "Choose the correct conditional structure: 'Were she my daughter, I ________ not allow her to go out late.'",
        "opts": ["will", "shall", "would", "had"],
        "ans": 2,
        "sol": "'Were she my daughter' is the inverted form of the Second Conditional 'If she were my daughter'. The main clause requires 'would + V1'."
    },
    {
        "q": "Fill in the blank: 'I ________ my dinner before my brother returned.'",
        "opts": ["have finished", "had finished", "finished", "was finishing"],
        "ans": 1,
        "sol": "The finishing of dinner occurred before another past event (brother's return). Therefore, the earlier past action must be in the Past Perfect ('had finished')."
    },
    {
        "q": "Select the correct sentence:",
        "opts": [
            "Unless you do not work hard, you will fail.",
            "Unless you work hard, you will fail.",
            "If you work hard, you will fail.",
            "Unless you will work hard, you will fail."
        ],
        "ans": 1,
        "sol": "'Unless' is negative in meaning (meaning 'if not'). It should not be followed by 'not'. Also, it cannot take 'will' in its clause."
    },
    {
        "q": "Identify the correct form: 'If he ________ to me, I would have helped him.'",
        "opts": ["comes", "came", "had come", "would have come"],
        "ans": 2,
        "sol": "This is a Third Conditional sentence ('would have helped'). The conditional clause must use the Past Perfect ('had come')."
    },
    {
        "q": "Fill in the blank: 'He ________ in this company for five years.'",
        "opts": ["is working", "works", "has been working", "was working"],
        "ans": 2,
        "sol": "An action showing continuation and duration ('for five years') from the past to the present requires the Present Perfect Continuous ('has been working')."
    },
    {
        "q": "Choose the correct sentence:",
        "opts": [
            "I will write to you when I will arrive.",
            "I will write to you when I arrive.",
            "I write to you when I will arrive.",
            "I will write to you when I would arrive."
        ],
        "ans": 1,
        "sol": "In clauses introduced by time connectors like *when, before, after, until*, do not use the future tense. Use the Simple Present ('when I arrive') instead."
    },
    {
        "q": "Identify the correct form: 'If I had not lost my passport, I ________ on a plane right now.'",
        "opts": ["would fly", "would have flown", "would be flying", "will be flying"],
        "ans": 2,
        "sol": "This is a mixed conditional: an unreal past condition ('had not lost') with a present continuing result ('right now'). Hence, 'would be flying' is correct."
    },
    {
        "q": "Choose the correct option: 'By the end of this month, we ________ here for two years.'",
        "opts": ["will live", "will have been living", "are living", "have lived"],
        "ans": 1,
        "sol": "'By the end of this month' coupled with a duration ('for two years') requires the Future Perfect Continuous tense ('will have been living')."
    },
    {
        "q": "Identify the correct sentence using 'lest':",
        "opts": [
            "Walk carefully lest you should not fall.",
            "Walk carefully lest you should fall.",
            "Walk carefully lest you will fall.",
            "Walk carefully lest you would fall."
        ],
        "ans": 1,
        "sol": "'Lest' is inherently negative and must be paired with 'should' without the negative word 'not'."
    },
    {
        "q": "Fill in the blank: 'I ________ a sound sleep last night.'",
        "opts": ["have had", "had", "was having", "had had"],
        "ans": 1,
        "sol": "'Last night' is a definite past time marker, requiring the Simple Past tense ('had')."
    },
    {
        "q": "What is the correct structure: 'If they ________ more time, they could have finished the project.'",
        "opts": ["had", "have", "had had", "would have had"],
        "ans": 2,
        "sol": "This is a Third Conditional sentence. The past perfect of the verb 'have' is 'had had' (auxiliary 'had' + V3 'had')."
    },
    {
        "q": "Select the correct option: 'I wish I ________ rich.'",
        "opts": ["am", "was", "were", "had been"],
        "ans": 2,
        "sol": "Present imaginary wishes use the past subjunctive form 'were' for all subjects."
    },
    {
        "q": "Fill in the blank: 'The bell ________ before I reached school.'",
        "opts": ["rang", "had rung", "has rung", "was ringing"],
        "ans": 1,
        "sol": "The ringing of the bell occurred before reaching school, requiring Past Perfect ('had rung') for the earlier past action."
    },
    {
        "q": "Choose the correct sentence:",
        "opts": [
            "We are knowing each other for a long time.",
            "We know each other for a long time.",
            "We have known each other for a long time.",
            "We have been knowing each other for a long time."
        ],
        "ans": 2,
        "sol": "'Know' is a stative verb. Duration must be expressed in the Present Perfect ('have known')."
    },
    {
        "q": "Fill in the blank: 'She ________ her homework before she went to bed.'",
        "opts": ["finished", "has finished", "had finished", "was finishing"],
        "ans": 2,
        "sol": "The finishing of homework was completed before going to bed, requiring Past Perfect ('had finished') for the earlier past action."
    },
    {
        "q": "Choose the correct option: 'If he ________ now, he will miss the train.'",
        "opts": ["does not leave", "will not leave", "did not leave", "leaves"],
        "ans": 0,
        "sol": "This is a First Conditional sentence. The conditional clause takes the Simple Present negative ('does not leave')."
    },
    {
        "q": "Select the correct form: 'Since the accident, he ________ afraid of driving.'",
        "opts": ["is", "was", "has been", "had been"],
        "ans": 2,
        "sol": "A state that started in the past (at the accident) and continues to the present requires the Present Perfect ('has been')."
    },
    {
        "q": "Fill in the blank: 'I ________ him yesterday.'",
        "opts": ["have met", "met", "had met", "meet"],
        "ans": 1,
        "sol": "Definite past time markers like 'yesterday' require Simple Past ('met')."
    },
    {
        "q": "Choose the correct conditional sentence:",
        "opts": [
            "If I had known, I would tell you.",
            "If I knew, I would have told you.",
            "If I had known, I would have told you.",
            "If I would have known, I would have told you."
        ],
        "ans": 2,
        "sol": "Standard Third Conditional: If + Past Perfect ('had known'), would have + V3 ('would have told')."
    },
    {
        "q": "Fill in the blank: 'He ________ since morning.'",
        "opts": ["is reading", "has been reading", "reads", "was reading"],
        "ans": 1,
        "sol": "An action continuing from past to present starting at a specific point ('since morning') takes Present Perfect Continuous ('has been reading')."
    },
    {
        "q": "What is the correct structure: 'If he ________ harder, he would have succeeded.'",
        "opts": ["tried", "had tried", "tries", "would have tried"],
        "ans": 1,
        "sol": "Third Conditional: If + Past Perfect ('had tried'), would have + V3."
    },
    {
        "q": "Select the correct option: 'It ________ since yesterday.'",
        "opts": ["is raining", "rains", "has been raining", "rained"],
        "ans": 2,
        "sol": "Action continuing from a point in the past to present takes Present Perfect Continuous ('has been raining')."
    },
    {
        "q": "Fill in the blank: 'The train ________ before I reached the station.'",
        "opts": ["left", "had left", "has left", "leaves"],
        "ans": 1,
        "sol": "Past Perfect ('had left') is required for the earlier of the two past actions."
    },
    {
        "q": "Choose the correct sentence:",
        "opts": [
            "I have seen him last week.",
            "I saw him last week.",
            "I had seen him last week.",
            "I have been seeing him last week."
        ],
        "ans": 1,
        "sol": "Definite past time reference ('last week') requires Simple Past ('saw')."
    },
    {
        "q": "Fill in the blank: 'If you ________ the truth, you would not be in trouble now.'",
        "opts": ["speak", "had spoken", "spoke", "would have spoken"],
        "ans": 1,
        "sol": "Mixed conditional: past unreal action ('had spoken') with present result ('would not be in trouble now')."
    },
    {
        "q": "Choose the correct option: 'He ________ writing stories for ten years.'",
        "opts": ["is", "has been", "was", "has"],
        "ans": 1,
        "sol": "Duration from past to present takes Present Perfect Continuous ('has been' + writing)."
    },
    {
        "q": "Identify the correct form: 'Should she ________, tell her I am waiting.'",
        "opts": ["comes", "came", "come", "will come"],
        "ans": 2,
        "sol": "After inverted 'Should', use the base form of the verb ('come') without '-s'."
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Identify the correct form of the verb: 'If I ________ a bird, I would fly in the sky.'",
        "opts": ["was", "were", "am", "had been"],
        "ans": 1,
        "sol": "This is a Second Conditional (hypothetical present). Use subjunctive 'were' for all subjects."
    },
    {
        "q": "Choose the grammatically correct sentence:",
        "opts": [
            "Unless you do not hurry, you will miss the train.",
            "Unless you hurry, you will miss the train.",
            "If you hurry, you will miss the train.",
            "Unless you will hurry, you will miss the train."
        ],
        "ans": 1,
        "sol": "'Unless' is negative and cannot take 'not' or 'will' in its clause."
    },
    {
        "q": "Identify the error in tense: 'By the time the doctor had arrived, the patient died.'",
        "opts": ["had arrived", "died", "By the time", "the"],
        "ans": 0,
        "sol": "The patient dying happened first, so it should be 'had died' (Past Perfect), and the doctor arriving happened second, so it should be 'arrived' (Simple Past). Thus, 'had arrived' is the error."
    },
    {
        "q": "Select the correct option to fill in the blank: 'I ________ this house since 2018.'",
        "opts": ["am owning", "have been owning", "have owned", "owned"],
        "ans": 2,
        "sol": "'Own' is a stative verb of possession, which does not take continuous aspect. Use Present Perfect 'have owned'."
    },
    {
        "q": "Identify the correct sentence structure using inversion:",
        "opts": [
            "Had we played well, we would have won.",
            "Had we played well, we had won.",
            "If we had played well, we would win.",
            "Would we have played well, we had won."
        ],
        "ans": 0,
        "sol": "'Had we played well' is the correct inverted Third Conditional clause, matched with 'would have won'."
    },
    {
        "q": "Fill in the blank: 'By next December, we ________ here for five years.'",
        "opts": ["will live", "are living", "will have been living", "will have lived"],
        "ans": 2,
        "sol": "'By next December' paired with a duration ('for five years') requires Future Perfect Continuous 'will have been living'."
    },
    {
        "q": "Choose the correct verb form: 'Water ________ at 100 degrees Celsius.'",
        "opts": ["boils", "boiled", "will boil", "is boiling"],
        "ans": 0,
        "sol": "Scientific facts are expressed in Simple Present 'boils'."
    },
    {
        "q": "Fill in the blank: 'If he ________ earlier, he would have met the director.'",
        "opts": ["arrived", "had arrived", "arrives", "would arrive"],
        "ans": 1,
        "sol": "Third Conditional past unreal: If + Past Perfect ('had arrived'), would have + V3."
    },
    {
        "q": "Identify the correct structure: 'No sooner ________ seen the police than he ran away.'",
        "opts": ["he had", "had he", "did he", "he did"],
        "ans": 1,
        "sol": "Inversion is required after 'No sooner' at the start of a sentence: 'had he' is correct."
    },
    {
        "q": "Choose the correct sentence from the options:",
        "opts": [
            "It is raining since morning.",
            "It has been raining since morning.",
            "It rains since morning.",
            "It was raining since morning."
        ],
        "ans": 1,
        "sol": "Action continuing from a past point to the present requires Present Perfect Continuous 'has been raining'."
    },
    {
        "q": "Fill in the blank: 'She ________ the office before I arrived.'",
        "opts": ["leaves", "has left", "had left", "was leaving"],
        "ans": 2,
        "sol": "Earlier of two past actions requires Past Perfect ('had left')."
    },
    {
        "q": "What is the correct conditional structure: 'Were he to ask me, I ________ help him.'",
        "opts": ["will", "shall", "would", "had"],
        "ans": 2,
        "sol": "Inverted Second Conditional 'Were he to ask me' requires 'would + V1' in the main clause."
    },
    {
        "q": "Choose the correct verb form: 'He ________ TV when the door bell rang.'",
        "opts": ["watched", "was watching", "had watched", "has watched"],
        "ans": 1,
        "sol": "Background continuous past action ('was watching') interrupted by a short completed action ('rang')."
    },
    {
        "q": "Identify the correct inversion structure: '________ you fail to comply, penalties will apply.'",
        "opts": ["Should", "Had", "Were", "If should"],
        "ans": 0,
        "sol": "'Should you fail' is the inverted First Conditional 'If you should fail'."
    },
    {
        "q": "Identify the correct form: 'Since she changed schools, she ________ much happier.'",
        "opts": ["is", "was", "has been", "had been"],
        "ans": 2,
        "sol": "State starting at a past point and continuing to the present requires Present Perfect 'has been'."
    }
]

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Master English tenses, continuous limits, four conditional categories, mixed conditions, and stylistic inversions.", "sections": deep_dive_en}
    }

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. English Tense Rules & Exceptions",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which tense is used for an action completed in the past with a definite past time marker?", "opts": ["Present Perfect", "Simple Past", "Past Perfect", "Past Continuous"], "ans": 1, "sol": "Simple Past (V2) is used with definite past time markers (e.g. yesterday, last year)."},
                    {"type": "MCQ", "q": "In 'The train had left before we reached', which action occurred first?", "opts": ["We reached", "The train left", "Both occurred simultaneously", "Cannot be determined"], "ans": 1, "sol": "The Past Perfect 'had left' indicates the train leaving occurred first in past time."},
                    {"type": "True/False", "q": "True or False: Stative verbs like 'own' or 'belong' are commonly used in the continuous tense to show duration.", "ans": False, "sol": "False. Stative verbs cannot take continuous aspect. Use Perfect tense (e.g. 'have owned') to show duration."},
                    {"type": "One-Liner", "q": "What tense is used for universal and scientific truths?", "sol": "Simple Present"}
                ]
            },
            {
                "title": "2. Conditional Clauses (Types 0-3)",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which conditional structure expresses an unreal past condition and its past result?", "opts": ["Zero Conditional", "First Conditional", "Second Conditional", "Third Conditional"], "ans": 3, "sol": "Third Conditional expresses unreal past conditions and results (If + Past Perfect, would have + V3)."},
                    {"type": "MCQ", "q": "If I ________ rich, I would buy a house.", "opts": ["was", "were", "am", "had been"], "ans": 1, "sol": "Second Conditional unreal present/future uses the subjunctive 'were' for all subjects."},
                    {"type": "True/False", "q": "True or False: You can use 'will' or 'shall' in the conditional clause of a First Conditional sentence.", "ans": False, "sol": "False. Use Simple Present in the 'if' clause (e.g. 'If it rains', not 'If it will rain')."},
                    {"type": "One-Liner", "q": "Which conditional type represents scientific laws and universal facts?", "sol": "Zero Conditional"}
                ]
            },
            {
                "title": "3. Inversion in Conditionals",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is the inverted form of 'If I had known'?", "opts": ["Had I known", "Were I known", "Should I known", "Did I know"], "ans": 0, "sol": "'Had I known' is the correct inverted Third Conditional clause."},
                    {"type": "MCQ", "q": "What is the inverted form of 'If you should need help'?", "opts": ["Should you need help", "Had you need help", "Were you need help", "Need you help"], "ans": 0, "sol": "'Should you need help' is the correct inverted First Conditional clause."},
                    {"type": "True/False", "q": "True or False: Inverted conditional clauses drop the conjunction 'if'.", "ans": True, "sol": "True. Inversion moves the auxiliary verb to the front and omits the word 'if'."},
                    {"type": "One-Liner", "q": "What modal verb is used to invert a First Conditional clause?", "sol": "Should"}
                ]
            }
        ]
    }

# ----------------- FILE GENERATION -----------------
import re

def parse_markdown(data):
    if isinstance(data, str):
        return re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #e67e22; font-weight: 700;">\1</strong>', data)
    elif isinstance(data, dict):
        return {k: parse_markdown(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parse_markdown(item) for item in data]
    return data

def write_json(filepath, data):
    formatted_data = parse_markdown(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())
