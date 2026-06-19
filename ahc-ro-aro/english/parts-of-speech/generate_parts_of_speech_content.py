# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "parts-of-speech"
TOPIC_DISPLAY = "Parts Of Speech"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\english\{TOPIC}"

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "English",
    "parentUrl": "../",
    "current": "Parts Of Speech"
}

hero_en = {
    "title": "Parts Of Speech",
    "description": "Comprehensive guide on English Parts of Speech tailored for AHC RO/ARO. Learn key classifications, advanced usage rules, grammatical exceptions, fixed prepositions, and clausal connectives."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Parts of Speech Mock Test",
        "description": "Evaluate your understanding of parts of speech classifications, usage rules, and common grammatical exceptions. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Evolution of Parts of Speech Classifications",
    "description": "Milestones in standardizing the grammatical categories of language.",
    "cards": [
        {
            "period": "Sanskrit Grammatical Tradition",
            "date": "500 BC",
            "details": "The ancient grammarian **Yaska** defined four main categories of words in Nirukta: Nama (noun/substantive), Akhyata (verb), Upasarga (pre-verb/prefix), and Nipata (particle)."
        },
        {
            "period": "Eight Greek Parts of Speech",
            "date": "100 BC",
            "details": "Published in 'The Art of Grammar' by **Dionysius Thrax**. It defined the eight traditional parts of speech that inspired Latin and modern Western grammars."
        },
        {
            "period": "First English Grammar",
            "date": "1586",
            "details": "Written by **William Bullokar** as 'Pamphlet for Grammar'. He adapted the Latin parts of speech to show that English grammar follows systematic rules."
        },
        {
            "period": "Murray's Standardizing Grammar",
            "date": "1795",
            "details": "**Lindley Murray** published 'English Grammar', establishing the rigid definitions of the eight parts of speech taught in classrooms for over a century."
        },
        {
            "period": "Modern Generative Grammar",
            "date": "1957",
            "details": "Developed by **Noam Chomsky**. Grammatical categories were split into lexical categories (content words) and functional categories (structure words)."
        }
    ]
}

mnemonics_en = {
    "title": "Recall Mnemonics",
    "description": "Memory aids to remember the parts of speech and coordinating conjunctions.",
    "items": [
        {
            "title": "Mnemonic 1: The Eight Parts of Speech",
            "phrase": "\"PAPA VINS (Pronoun, Adjective, Preposition, Adverb, Verb, Interjection, Noun, Conjunction)\"",
            "decryption": "Quickly list all eight components:<br>• **P** — **P**ronoun<br>• **A** — **A**djective<br>• **P** — **P**reposition<br>• **A** — **A**dverb<br>• **V** — **V**erb<br>• **I** — **I**nterjection<br>• **N** — **N**oun<br>• **S** — **S**ubordinate/Coordinating Conjunction"
        },
        {
            "title": "Mnemonic 2: Coordinating Conjunctions",
            "phrase": "\"FANBOYS\"",
            "decryption": "Remember the seven coordinating conjunctions used to join clauses of equal rank:<br>• **F** — **F**or<br>• **A** — **A**nd<br>• **N** — **N**or<br>• **B** — **B**ut<br>• **O** — **O**r<br>• **Y** — **Y**et<br>• **S** — **S**o"
        },
        {
            "title": "Mnemonic 3: Preposition Relationship",
            "phrase": "\"Anything a squirrel can do to a tree\"",
            "decryption": "Visual hook for simple prepositions of place and direction:<br>• A squirrel can run **up**, **down**, **into**, **through**, **behind**, **around**, or **under** the tree."
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What is a Gerund and which Part of Speech does it act as?",
            "answer": "A Gerund is a verb form ending in **-ing** that functions as a **Noun** (e.g., \"**Swimming** is great exercise\").",
            "icon": "fa-running"
        },
        {
            "question": "What is the key difference between a Transitive and an Intransitive Verb?",
            "answer": "A **Transitive Verb** requires a direct object to complete its meaning (e.g., \"She **bought** a book\"). An **Intransitive Verb** does not take a direct object (e.g., \"He **slept**\").",
            "icon": "fa-exchange-alt"
        },
        {
            "question": "Identify the word class of 'fast' in: 'He ran fast' vs 'He is a fast runner'.",
            "answer": "In \"He ran fast\", **fast** is an **Adverb** (modifies verb 'ran'). In \"fast runner\", **fast** is an **Adjective** (modifies noun 'runner').",
            "icon": "fa-tachometer-alt"
        },
        {
            "question": "What is a Correlative Conjunction?",
            "answer": "Conjunctions that work in pairs to join grammatically equal elements. Examples include **either...or**, **neither...nor**, and **not only...but also**.",
            "icon": "fa-link"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid (AHC RO/ARO Focus)",
    "items": [
        "<strong>Trap 1:</strong> Preposition vs. Adverb distinction. Words like 'before', 'after', 'in', and 'up' function as **Prepositions** if followed by a noun phrase object (e.g., \"She arrived **before** noon\"), but function as **Adverbs** if they stand alone without an object (e.g., \"She had arrived **before**\"). This is a highly frequent question format in RO/ARO.",
        "<strong>Trap 2:</strong> Adjectives ending in '-ly' mistaken for adverbs. Words like **friendly**, **brotherly**, **cowardly**, **mannerly**, and **silly** are adjectives, not adverbs. To modify a verb, you must use a phrase like \"in a cowardly manner\" instead of \"cowardly\".",
        "<strong>Trap 3:</strong> Conjunction pairings (Correlatives). AHC exams frequently test faulty pairings: **no sooner** must be paired with **than** (not *when* or *then*); **hardly/scarcely/barely** must be paired with **when** (not *than*); **lest** must be paired with **should** (and cannot take a negative word like *not*).",
        "<strong>Trap 4:</strong> Collective Nouns & Subject-Verb Agreement. Nouns like **committee**, **jury**, **audience**, and **fleet** take a singular verb when acting as a unified unit (e.g., \"The jury **was** unanimous\"), but a plural verb when members act individually (e.g., \"The jury **were** divided in their opinions\")."
    ]
}

deep_dive_en = [
    {
        "title": "1. Nouns & Pronouns: Classifications, Rules & Case Exceptions",
        "content": """<!-- SVG Parts of Speech Summary Table -->
        <svg viewBox="0 0 800 385" class="responsive-svg-diagram" style="margin:1.5rem 0; border-radius:12px; background:var(--bg-card,#ffffff); border:1px solid rgba(128,128,128,0.15); padding:15px; width:100%;">
          <style>
            .grid-header { fill: #8e44ad; font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 700; }
            .grid-cell-title { font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 700; }
            .grid-cell-text { fill: #555; font-family: 'Inter', sans-serif; font-size: 12px; }
            .header-bg { fill: rgba(142, 68, 173, 0.08); }
            .lexical-bg { fill: rgba(230, 126, 34, 0.05); }
            .functional-bg { fill: rgba(52, 152, 219, 0.05); }
            body.dark-mode .grid-cell-text { fill: #94a3b8; }
            body.dark-mode .header-bg { fill: rgba(168, 85, 247, 0.12); }
            body.dark-mode .lexical-bg { fill: rgba(230, 126, 34, 0.08); }
            body.dark-mode .functional-bg { fill: rgba(52, 152, 219, 0.08); }
          </style>
          
          <!-- Headers -->
          <rect x="10" y="10" width="780" height="40" rx="6" class="header-bg" />
          <text x="25" y="34" class="grid-header">Part of Speech</text>
          <text x="170" y="34" class="grid-header">Major Function</text>
          <text x="430" y="34" class="grid-header">AHC RO/ARO Exam Focus &amp; Examples</text>
          
          <!-- Row 1: Noun -->
          <rect x="10" y="55" width="780" height="35" rx="4" class="lexical-bg" />
          <text x="25" y="77" class="grid-cell-title" style="fill:#e67e22;">Noun (संज्ञा)</text>
          <text x="170" y="77" class="grid-cell-text">Names people, places, or ideas.</text>
          <text x="430" y="77" class="grid-cell-text">Singular/plural: <tspan font-weight="700" fill="#e67e22">cattle</tspan> (plural), <tspan font-weight="700" fill="#e67e22">scenery</tspan> (singular).</text>
          
          <!-- Row 2: Pronoun -->
          <rect x="10" y="95" width="780" height="35" rx="4" class="lexical-bg" />
          <text x="25" y="117" class="grid-cell-title" style="fill:#e67e22;">Pronoun (सर्वनाम)</text>
          <text x="170" y="117" class="grid-cell-text">Replaces nouns to avoid repetition.</text>
          <text x="430" y="117" class="grid-cell-text">Subject comparative: <tspan font-weight="700" fill="#e67e22">taller than I</tspan>; relative <tspan font-weight="700" fill="#e67e22">who/whom</tspan> rules.</text>
          
          <!-- Row 3: Verb -->
          <rect x="10" y="135" width="780" height="35" rx="4" class="lexical-bg" />
          <text x="25" y="157" class="grid-cell-title" style="fill:#e67e22;">Verb (क्रिया)</text>
          <text x="170" y="157" class="grid-cell-text">Expresses states or actions.</text>
          <text x="430" y="157" class="grid-cell-text">Confusing pairs: <tspan font-weight="700" fill="#e67e22">lie</tspan> (recline) vs. <tspan font-weight="700" fill="#e67e22">lay</tspan> (place); stative verbs.</text>
          
          <!-- Row 4: Adjective -->
          <rect x="10" y="175" width="780" height="35" rx="4" class="lexical-bg" />
          <text x="25" y="197" class="grid-cell-title" style="fill:#e67e22;">Adjective (विशेषण)</text>
          <text x="170" y="197" class="grid-cell-text">Modifies nouns or pronouns.</text>
          <text x="430" y="197" class="grid-cell-text">Absolute states: <tspan font-weight="700" fill="#e67e22">unique</tspan> (no 'more'); comparatives: <tspan font-weight="700" fill="#e67e22">senior to</tspan>.</text>
          
          <!-- Row 5: Adverb -->
          <rect x="10" y="215" width="780" height="35" rx="4" class="lexical-bg" />
          <text x="25" y="237" class="grid-cell-title" style="fill:#e67e22;">Adverb (क्रियाविशेषण)</text>
          <text x="170" y="237" class="grid-cell-text">Modifies verbs or adjectives.</text>
          <text x="430" y="237" class="grid-cell-text">Placement: adjective + <tspan font-weight="700" fill="#e67e22">enough</tspan>; double negative check.</text>
          
          <!-- Row 6: Preposition -->
          <rect x="10" y="255" width="780" height="35" rx="4" class="functional-bg" />
          <text x="25" y="277" class="grid-cell-title" style="fill:#3498db;">Preposition (संबंधसूचक)</text>
          <text x="170" y="277" class="grid-cell-text">Shows relationships between words.</text>
          <text x="430" y="277" class="grid-cell-text">Fixed combinations: <tspan font-weight="700" fill="#3498db">accuse of</tspan>, <tspan font-weight="700" fill="#3498db">abstain from</tspan>, <tspan font-weight="700" fill="#3498db">cope with</tspan>.</text>
          
          <!-- Row 7: Conjunction -->
          <rect x="10" y="295" width="780" height="35" rx="4" class="functional-bg" />
          <text x="25" y="317" class="grid-cell-title" style="fill:#3498db;">Conjunction (समुच्चयबोधक)</text>
          <text x="170" y="317" class="grid-cell-text">Joins words, phrases, or clauses.</text>
          <text x="430" y="317" class="grid-cell-text">Inversion: <tspan font-weight="700" fill="#3498db">No sooner... than</tspan>; <tspan font-weight="700" fill="#3498db">Hardly... when</tspan>.</text>
          
          <!-- Row 8: Interjection -->
          <rect x="10" y="335" width="780" height="35" rx="4" class="functional-bg" />
          <text x="25" y="357" class="grid-cell-title" style="fill:#3498db;">Interjection (विस्मयादिबोधक)</text>
          <text x="170" y="357" class="grid-cell-text">Expresses sudden emotions.</text>
          <text x="430" y="357" class="grid-cell-text">Stands grammatically independent: <tspan font-weight="700" fill="#3498db">Alas!</tspan>, <tspan font-weight="700" fill="#3498db">Hurrah!</tspan>, <tspan font-weight="700" fill="#3498db">Wow!</tspan></text>
        </svg>
        
        
        
        <p>Nouns and Pronouns are the subjects and objects of sentences. AHC exams frequently test their specific grammatical constraints and agreement anomalies.</p>
        
        <h3>A. Noun Classifications & Advanced Rules</h3>
        <p>A **Noun** is a naming word. Classifications include: Proper (specific names), Common (generic names), Collective (group names), Material (substances), and Abstract (ideas/emotions).</p>
        <ul>
          <li><strong>Rule 1 (Singular/Plural Form Traps):</strong> 
            <ul>
              <li>*Always Plural:* **cattle, gentry, poultry, clergy, folk, police, people** look singular but take plural verbs (e.g., <em>"The police **have** caught the thief"</em>).</li>
              <li>*Always Singular:* **scenery, poetry, furniture, advice, information, luggage, baggage, hair, mischief, business** are uncountable. They never take 's' or 'an' (e.g., <em>"The scenery of Himalayas **is** beautiful"</em>).</li>
              <li>*Form is Plural, Meaning is Singular:* **physics, mathematics, news, summons, innings, gallows, ethics, politics** (e.g., <em>"This news **is** true"</em>; <em>"A summons **was** served on him"</em>).</li>
              <li>*Identical Form:* **sheep, series, species, deer, fish** have the same singular and plural form.</li>
            </ul>
          </li>
          <li><strong>Rule 2 (Hyphenated & Compound Nouns):</strong> Compound nouns are pluralized by adding 's' to the root word, not the modifier (e.g., **commanders-in-chief**, **mothers-in-law**, **passers-by**). Hyphenated nouns never take a plural form when acting as adjectives (e.g., <em>"a ten-rupee note"</em>, not <em>"a ten-rupees note"</em>).</li>
          <li><strong>Rule 3 (Possessive Case / Apostrophe-S):</strong> 
            <ul>
              <li>Do not use double possessive (e.g., write <em>"the roof of my friend's house"</em>, not <em>"my friend's house's roof"</em>).</li>
              <li>Use apostrophe-s with living beings and personified objects (e.g., <em>"nature's laws"</em>, <em>"a day's leave"</em>), but use 'of' for non-living objects (e.g., <em>"the leg of the table"</em>).</li>
              <li>For joint possession, add apostrophe-s to the last noun (e.g., <em>"Rahul and Amit's father"</em>). For separate possession, add to both (e.g., <em>"Rahul's and Amit's fathers"</em>).</li>
            </ul>
          </li>
        </ul>

        <h3>B. Pronouns: Case, Order, and Relative Clauses</h3>
        <p>A **Pronoun** replaces a noun to avoid repetition.</p>
        <ul>
          <li><strong>Rule 1 (Order of Personal Pronouns):</strong> 
            <ul>
              <li>*Normal / Pleasant situations:* Follow the **231 rule** (Second Person, Third Person, First Person). E.g., <em>"**You, he and I** are studying together."</em></li>
              <li>*Negative / Confessional / Plural situations:* Follow the **123 rule** (First Person, Second Person, Third Person). E.g., <em>"**I, you and he** committed the mistake."</em></li>
            </ul>
          </li>
          <li><strong>Rule 2 (Subject vs. Object in Comparisons):</strong> When comparing two pronouns using *than* or *as*, keep their cases parallel. E.g., <em>"He runs faster than **I**"</em> (not <em>"than me"</em>, as it implies <em>"than I run"</em>).</li>
          <li><strong>Rule 3 (Relative Pronouns - Who vs. Whom vs. That):</strong>
            <ul>
              <li>**Who** is subjective (acts as the subject of the verb). E.g., <em>"The girl **who** won the medal is my sister."</em></li>
              <li>**Whom** is objective (acts as the object). E.g., <em>"The boy **whom** you met is a writer."</em></li>
              <li>**That** is mandatory instead of *who* or *which* after superlative adjectives, and expressions like *all, same, only, any, none, nothing*. E.g., <em>"This is the same pen **that** I bought."</em></li>
            </ul>
          </li>
          <li><strong>Rule 4 (Reflexive Pronouns):</strong> Reflexive pronouns (myself, himself) cannot stand alone as subjects without a preceding subject noun/pronoun. E.g., <em>"I am Amit"</em> or <em>"I myself did it"</em> (correct), but not <em>"Myself am Amit"</em> (incorrect).</li>
        </ul>"""
    },
    {
        "title": "2. Verbs, Adjectives & Adverbs: Action and Modifying Logic",
        "content": """<p>Verbs dictate the tense and state of a sentence, while Adjectives and Adverbs act as precise modifiers. Mastery of their structural constraints is vital for error detection.</p>
        
        <h3>A. Verbs: Transitive, Intransitive & Stative Verbs</h3>
        <ul>
          <li><strong>Transitive vs. Intransitive:</strong> Transitive verbs require a direct object (e.g., <em>"She **raised** the flag"</em>). Intransitive verbs do not take an object (e.g., <em>"The sun **rises** in the east"</em>).
            <ul>
              <li>*Confusing pair:* **Lie** (intransitive: lie-lay-lain; to recline) vs. **Lay** (transitive: lay-laid-laid; to place). E.g., <em>"I laid the baby on the bed"</em> vs. <em>"He lay on the grass."</em></li>
            </ul>
          </li>
          <li><strong>Stative Verbs (No Continuous Form):</strong> Verbs of perception (<em>see, hear, smell, taste</em>), emotion (<em>love, hate, wish, remember</em>), and ownership (<em>own, possess, belong, have</em>) are not used in the continuous/progressive tense in their standard sense. E.g., <em>"I **know** him"</em> (correct), not <em>"I am knowing him"</em> (incorrect).</li>
          <li><strong>Non-Finite Verbs:</strong>
            <ul>
              <li>**Gerund:** A verb form ending in *-ing* that acts as a **Noun** (e.g., <em>"**Reading** is a good habit"</em>).</li>
              <li>**Participle:** Acts as an **Adjective** (Present: *crying baby*; Past: *broken window*).</li>
              <li>**Infinitive:** The base form preceded by 'to' (*to study*). Do not split the infinitive by placing an adverb between 'to' and the verb (e.g., write <em>"to understand clearly"</em>, not <em>"to clearly understand"</em>).</li>
            </ul>
          </li>
        </ul>

        <h3>B. Adjectives: Ordering & Comparative Constraints</h3>
        <p>An **Adjective** modifies a noun or pronoun. Key rules include:</p>
        <ul>
          <li><strong>Rule 1 (Absolute Adjectives):</strong> Adjectives representing absolute states cannot be modified by *more* or *most*. These include: **unique, perfect, complete, dead, universal, round, absolute, empty, eternal**. E.g., <em>"This is a unique piece"</em> (not <em>"a most unique piece"</em>).</li>
          <li><strong>Rule 2 (Latin Comparatives):</strong> Adjectives ending in *-ior* (such as **senior, junior, inferior, superior, prior, anterior, posterior**) and the verb **prefer/preferable** take the preposition **to** instead of the conjunction *than*. E.g., <em>"He is senior **to** me"</em> (not <em>"senior than me"</em>).</li>
          <li><strong>Rule 3 (Order of Adjectives):</strong> When multiple adjectives describe a noun, arrange them in this order: **Opinion, Size, Age, Shape, Color, Origin, Material, Purpose** (Mnemonic: *OSASCOMP*). E.g., <em>"a beautiful, small, old, round, black, Indian, wooden table."</em></li>
          <li><strong>Rule 4 (Comparatives and Superlatives):</strong> Avoid double comparatives (e.g., write *more handsome*, not *more handsomer*). For comparing two things, use comparative degree; for more than two, use superlative.</li>
        </ul>

        <h3>C. Adverbs: Placement and Modifying Rules</h3>
        <p>An **Adverb** modifies a verb, adjective, or another adverb.</p>
        <ul>
          <li><strong>Rule 1 (Placement of 'Enough'):</strong> The adverb *enough* must be placed **after** the adjective/adverb it modifies (e.g., <em>"He is **bold enough** to face them"</em>), but **before** a noun (e.g., <em>"I have **enough money**"</em>).</li>
          <li><strong>Rule 2 (Double Negatives):</strong> Words like **hardly, scarcely, barely, seldom, rarely** are already negative in meaning. Do not use *not* or other negative words in the same clause (e.g., <em>"He could hardly walk"</em>, not <em>"He could not hardly walk"</em>).</li>
          <li><strong>Rule 3 (Adverbial Placement Order):</strong> When adverbs of Manner (M), Place (P), and Time (T) appear together, arrange them in the sequence **M -> P -> T** (e.g., <em>"She sang **sweetly** (M) **at the concert** (P) **yesterday** (T)."</em>).</li>
        </ul>"""
    },
    {
        "title": "3. Prepositions & Conjunctions: Linkers, Fixed Phrases & Correlatives",
        "content": """<p>These functional categories connect elements in sentences. The majority of fill-in-the-blanks and sentence-correction questions in RO/ARO target prepositional government and coordinate/subordinate pairs.</p>
        
        <h3>A. Prepositions: Cases, Rules & Fixed Prepositions</h3>
        <p>A **Preposition** links nouns/pronouns to other words in the sentence. Key rules:</p>
        <ul>
          <li><strong>Rule 1 (Objective Case):</strong> The pronoun following a preposition must always be in the objective case. E.g., <em>"Divide the apples between you and **me**"</em> (not <em>"you and I"</em>).</li>
          <li><strong>Rule 2 (Avoiding Redundant Prepositions):</strong> Do not use prepositions after transitive verbs like **enter, comprise, discuss, order, resemble, demand, join** when followed by their objects. E.g., <em>"The book comprises ten chapters"</em> (not <em>"comprises of"</em>); <em>"He entered the room"</em> (not <em>"entered into"</em>).</li>
          <li><strong>Rule 3 (Highly Tested Fixed Prepositions):</strong>
            <ul>
              <li>**Abstain / Refrain from:** <em>"You must abstain **from** bad habits."</em></li>
              <li>**Accuse of:** <em>"He was accused **of** murder."</em></li>
              <li>**Agree with (person) / Agree to (proposal):** <em>"I agree **with** John,"</em> but <em>"I agree **to** your terms."</em></li>
              <li>**Angry with (person) / Angry at (thing):** <em>"She was angry **with** me,"</em> but <em>"She was angry **at** his behavior."</em></li>
              <li>**Die of (disease) / Die from (external cause):** <em>"He died **of** cholera,"</em> but <em>"He died **from** overwork."</em></li>
              <li>**Cope with:** <em>"He can cope **with** any situation"</em> (never write *cope up with*).</li>
              <li>**Key to:** <em>"Hard work is the key **to** success."</em></li>
            </ul>
          </li>
        </ul>

        <h3>B. Conjunctions: Connectives & Correlative Pairs</h3>
        <p>A **Conjunction** joins words, phrases, or clauses. Classifications: Coordinating (FANBOYS), Subordinating (introduce dependent clauses), and Correlative (work in pairs).</p>
        <ul>
          <li><strong>Rule 1 (Correlative Pairings):</strong> Correlative conjunctions must be paired correctly:
            <ul>
              <li>**No sooner... than:** <em>"No sooner had he arrived **than** it started raining."</em> (Note: uses inversion after *No sooner*).</li>
              <li>**Hardly / Scarcely... when:** <em>"Hardly had I stepped out **when** it began to snow."</em> (Uses inversion).</li>
              <li>**Lest... should:** *Lest* means 'for fear that' and requires *should*. Do not use a negative word like *not* after lest. E.g., <em>"Run fast lest you **should** miss the train."</em></li>
              <li>**Although / Though... yet:** E.g., <em>"Although he is poor, **yet** he is honest"</em> (or use a comma instead of *yet*; never use *but*).</li>
            </ul>
          </li>
          <li><strong>Rule 2 (Parallel Structure with Correlatives):</strong> When using correlatives like *either...or*, *neither...nor*, and *not only...but also*, ensure both parts are followed by the same part of speech. E.g., <em>"He is not only **intelligent** (adjective) but also **hardworking** (adjective)"</em>; not <em>"He not only is intelligent but also hardworking."</em></li>
        </ul>

        <h3>C. Interjections: Emotional Exclamations</h3>
        <p>Words expressing sudden emotions: **Hurrah!** (joy), **Alas!** (grief), **Wow!** (wonder), **Fie!** (disapproval), **Hark!** (attention). They are grammatically independent of the rest of the sentence.</p>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Identify the part of speech of the underlined word in the sentence: 'She behaved in a very friendly manner.'",
        "opts": ["Adverb", "Adjective", "Noun", "Preposition"],
        "ans": 1,
        "sol": "Although 'friendly' ends in '-ly', it modifies the noun 'manner'. Therefore, it functions as an Adjective. Words like friendly, lovely, and silly are adjectives, not adverbs."
    },
    {
        "q": "In the sentence: 'He went up the hill,' what is the part of speech of the word 'up'?",
        "opts": ["Adverb", "Preposition", "Conjunction", "Verb"],
        "ans": 1,
        "sol": "In this sentence, 'up' is followed by the noun phrase 'the hill' (its object), which establishes a spatial relationship. Therefore, it functions as a Preposition."
    },
    {
        "q": "Identify the word class of 'up' in the sentence: 'The prices are going up.'",
        "opts": ["Preposition", "Adjective", "Adverb", "Noun"],
        "ans": 2,
        "sol": "Here, 'up' modifies the verb 'going' and does not take an object. Therefore, it functions as an Adverb of direction."
    },
    {
        "q": "Which part of speech is the word 'crying' in the phrase: 'a crying baby'?",
        "opts": ["Gerund", "Present Participle (Adjective)", "Verb", "Noun"],
        "ans": 1,
        "sol": "'Crying' modifies the noun 'baby' and functions as a verbal adjective, which is a Present Participle."
    },
    {
        "q": "In the sentence: 'Swimming is a healthy exercise,' what category does 'Swimming' belong to?",
        "opts": ["Verb", "Present Participle", "Gerund (Noun)", "Adverb"],
        "ans": 2,
        "sol": "'Swimming' is a verb form ending in -ing that acts as the subject of the sentence, which means it functions as a verbal noun or Gerund."
    },
    {
        "q": "Choose the sentence that contains a relative pronoun:",
        "opts": [
            "I know that he is honest.",
            "This is the book that I lost yesterday.",
            "That book belongs to me.",
            "Give me that."
        ],
        "ans": 1,
        "sol": "In the second sentence, 'that' refers back to 'the book' and introduces the relative clause 'I lost yesterday'. Hence, it is a Relative Pronoun."
    },
    {
        "q": "Identify the part of speech of the underlined word: 'He walked fast to catch the bus.'",
        "opts": ["Adjective", "Adverb", "Noun", "Conjunction"],
        "ans": 1,
        "sol": "Here, 'fast' modifies the action verb 'walked', describing how he walked. Therefore, it is an Adverb."
    },
    {
        "q": "In the sentence: 'He is a fast runner,' what is the part of speech of 'fast'?",
        "opts": ["Adverb", "Adjective", "Noun", "Pronoun"],
        "ans": 1,
        "sol": "Here, 'fast' modifies the noun 'runner'. Hence, it functions as an Adjective."
    },
    {
        "q": "Identify the relative pronoun in the following options:",
        "opts": ["Who", "Him", "Myself", "Each"],
        "ans": 0,
        "sol": "'Who' is a relative pronoun used to refer to people. 'Him' is a personal pronoun, 'Myself' is reflexive, and 'Each' is indefinite."
    },
    {
        "q": "Which category of conjunction does 'neither...nor' belong to?",
        "opts": ["Coordinating", "Subordinating", "Correlative", "Compound"],
        "ans": 2,
        "sol": "Conjunctions that are used in pairs, like 'neither...nor' and 'either...or', are classified as Correlative Conjunctions."
    },
    {
        "q": "In the sentence: 'She herself went to see the patient,' the word 'herself' is a/an:",
        "opts": ["Reflexive Pronoun", "Emphatic Pronoun", "Relative Pronoun", "Possessive Pronoun"],
        "ans": 1,
        "sol": "When reflexive pronouns (like herself, himself, myself) are used immediately after a noun or pronoun to add emphasis, they function as Emphatic Pronouns."
    },
    {
        "q": "In the sentence: 'She hurt herself,' the word 'herself' is a/an:",
        "opts": ["Reflexive Pronoun", "Emphatic Pronoun", "Demonstrative Pronoun", "Personal Pronoun"],
        "ans": 0,
        "sol": "In this sentence, the action of the verb 'hurt' reflects back to the subject 'She'. Thus, 'herself' is the object of the verb and functions as a Reflexive Pronoun."
    },
    {
        "q": "In the phrase: 'Those mangoes are ripe,' the word 'Those' is a/an:",
        "opts": ["Demonstrative Pronoun", "Demonstrative Adjective", "Possessive Adjective", "Distributive Pronoun"],
        "ans": 1,
        "sol": "Since 'Those' immediately precedes and modifies the noun 'mangoes', it functions as a Demonstrative Adjective. If it stood alone (e.g., 'Those are ripe'), it would be a Demonstrative Pronoun."
    },
    {
        "q": "Identify the subordinating conjunction in the following sentence: 'We shall not go out if it rains.'",
        "opts": ["shall", "not", "if", "out"],
        "ans": 2,
        "sol": "'if' is a subordinating conjunction because it introduces the dependent conditional clause 'if it rains'."
    },
    {
        "q": "What is the part of speech of the word 'before' in: 'I have seen you before.'?",
        "opts": ["Preposition", "Conjunction", "Adverb", "Adjective"],
        "ans": 2,
        "sol": "Since 'before' does not have an object here and refers to time, it functions as an Adverb of time."
    },
    {
        "q": "What is the part of speech of the word 'before' in: 'He stood before the judge.'?",
        "opts": ["Adverb", "Preposition", "Conjunction", "Noun"],
        "ans": 1,
        "sol": "In this sentence, 'before' is followed by the noun phrase 'the judge' (its object), signifying position. Therefore, it is a Preposition."
    },
    {
        "q": "Identify the collective noun in the sentence: 'The jury was unanimous in its decision.'",
        "opts": ["jury", "unanimous", "decision", "its"],
        "ans": 0,
        "sol": "'Jury' represents a group of judges or individuals acting as a single collective unit, making it a Collective Noun."
    },
    {
        "q": "Which of the following is an example of an abstract noun?",
        "opts": ["Gold", "Team", "Childhood", "London"],
        "ans": 2,
        "sol": "'Childhood' refers to a state or stage of life which is abstract, whereas 'Gold' is material, 'Team' is collective, and 'London' is proper."
    },
    {
        "q": "In the sentence: 'He is the man whom I met yesterday,' the word 'whom' is a/an:",
        "opts": ["Relative Pronoun", "Demonstrative Pronoun", "Interrogative Pronoun", "Adjective"],
        "ans": 0,
        "sol": "'Whom' is a Relative Pronoun used in the objective case, connecting the relative clause to the noun 'man'."
    },
    {
        "q": "Which part of speech is 'but' in the sentence: 'It is but right to admit our mistake.'?",
        "opts": ["Conjunction", "Adverb", "Preposition", "Pronoun"],
        "ans": 1,
        "sol": "In this context, 'but' means 'only' (it modifies the adjective 'right'). Hence, it functions as an Adverb."
    },
    {
        "q": "Identify the word class of 'but' in: 'All but John were present.'",
        "opts": ["Conjunction", "Adverb", "Preposition", "Verb"],
        "ans": 2,
        "sol": "In this sentence, 'but' means 'except' and links 'John' to the rest of the sentence. Hence, it functions as a Preposition."
    },
    {
        "q": "She runs very quickly. What word class is 'very'?",
        "opts": ["Adjective", "Adverb", "Verb", "Noun"],
        "ans": 1,
        "sol": "'Very' modifies the adverb 'quickly' by indicating degree. Therefore, it is an Adverb (Adverb of degree)."
    },
    {
        "q": "Which of the following is a Coordinating Conjunction?",
        "opts": ["Because", "Although", "But", "Unless"],
        "ans": 2,
        "sol": "'But' is a coordinating conjunction (part of the FANBOYS mnemonic). The other options are subordinating conjunctions."
    },
    {
        "q": "Identify the part of speech of 'round' in: 'The Earth moves round the Sun.'",
        "opts": ["Adjective", "Adverb", "Preposition", "Noun"],
        "ans": 2,
        "sol": "'round' is followed by the object 'the Sun', establishing a physical spatial relationship. Therefore, it is a Preposition."
    },
    {
        "q": "Identify the part of speech of 'round' in: 'The doctor made his daily round.'",
        "opts": ["Noun", "Adjective", "Verb", "Preposition"],
        "ans": 0,
        "sol": "In this sentence, 'round' is preceded by the possessive adjective 'his' and descriptive adjective 'daily', serving as the direct object of the verb 'made'. Hence, it is a Noun."
    },
    {
        "q": "In the sentence: 'It was a round table,' what is the part of speech of 'round'?",
        "opts": ["Noun", "Adjective", "Adverb", "Verb"],
        "ans": 1,
        "sol": "Here, 'round' describes the shape of the noun 'table'. Thus, it functions as an Adjective."
    },
    {
        "q": "Which of the following sentences uses 'crying' as a Gerund?",
        "opts": [
            "The crying child was comforted by his mother.",
            "Crying is not the solution to this problem.",
            "She was crying because she lost her keys.",
            "I heard someone crying in the hallway."
        ],
        "ans": 1,
        "sol": "In 'Crying is not the solution...', 'Crying' functions as the noun subject of the sentence, which is the definition of a Gerund."
    },
    {
        "q": "In the sentence: 'Alas! The great leader is no more,' what is the word 'Alas!'?",
        "opts": ["Conjunction", "Interjection", "Preposition", "Adverb"],
        "ans": 1,
        "sol": "'Alas!' is an Interjection because it expresses a sudden strong emotion (grief) and is grammatically independent of the rest of the sentence."
    },
    {
        "q": "Identify the indefinite pronoun in the following sentence: 'Does anyone know the answer?'",
        "opts": ["anyone", "know", "answer", "Does"],
        "ans": 0,
        "sol": "'anyone' is an indefinite pronoun because it refers to an unspecified person."
    },
    {
        "q": "What is the part of speech of the word 'still' in: 'Still waters run deep.'?",
        "opts": ["Noun", "Adjective", "Adverb", "Verb"],
        "ans": 1,
        "sol": "Here, 'still' modifies the noun 'waters' by describing its quiet or calm state. Therefore, it is an Adjective."
    },
    {
        "q": "What is the part of speech of 'still' in: 'He is still working in that firm.'?",
        "opts": ["Adverb", "Adjective", "Preposition", "Conjunction"],
        "ans": 0,
        "sol": "Here, 'still' modifies the verb phrase 'is working', describing the continuation of the action. Therefore, it is an Adverb."
    },
    {
        "q": "Identify the modal auxiliary verb in the sentence: 'You must submit your assignment by tomorrow.'",
        "opts": ["submit", "must", "by", "tomorrow"],
        "ans": 1,
        "sol": "'must' is a modal auxiliary verb that expresses obligation or necessity."
    },
    {
        "q": "Which part of speech is the word 'that' in: 'I know that you will pass.'?",
        "opts": ["Relative Pronoun", "Subordinating Conjunction", "Demonstrative Pronoun", "Adjective"],
        "ans": 1,
        "sol": "Here, 'that' is a conjunction linking the independent clause 'I know' with the dependent noun clause 'you will pass'. It does not refer to any preceding noun."
    },
    {
        "q": "In the sentence: 'She not only sang but also danced,' what type of conjunction is used?",
        "opts": ["Coordinating", "Subordinating", "Correlative", "Distributive"],
        "ans": 2,
        "sol": "'not only...but also' is a correlative conjunction because it is a paired conjunction linking equivalent parts."
    },
    {
        "q": "What is the part of speech of the word 'fast' in the phrase: 'He kept a fast for a week.'?",
        "opts": ["Verb", "Noun", "Adjective", "Adverb"],
        "ans": 1,
        "sol": "In this context, 'fast' refers to the act of abstaining from food. It is preceded by the article 'a', making it a Noun."
    },
    {
        "q": "In the sentence: 'They fast twice a week,' the word 'fast' is a/an:",
        "opts": ["Verb", "Noun", "Adjective", "Adverb"],
        "ans": 0,
        "sol": "Here, 'fast' is the action being performed by the subject 'They' (abstaining from food). Thus, it functions as a Verb."
    },
    {
        "q": "Identify the word class of the underlined word: 'The book on the table is mine.'",
        "opts": ["Possessive Adjective", "Possessive Pronoun", "Personal Pronoun", "Demonstrative Pronoun"],
        "ans": 1,
        "sol": "'mine' replaces the noun phrase 'my book' and shows possession without being followed by a noun. Therefore, it is a Possessive Pronoun."
    },
    {
        "q": "Which part of speech is 'my' in the sentence: 'This is my book.'?",
        "opts": ["Possessive Pronoun", "Possessive Adjective", "Personal Pronoun", "Demonstrative Adjective"],
        "ans": 1,
        "sol": "'my' modifies the noun 'book' directly to show possession. Therefore, it acts as a Possessive Adjective."
    },
    {
        "q": "In the sentence: 'Whom did you invite for the party?', the word 'Whom' is an:",
        "opts": ["Relative Pronoun", "Interrogative Pronoun", "Demonstrative Pronoun", "Adjective"],
        "ans": 1,
        "sol": "'Whom' is used here to ask a question, and it acts as the object of the verb. Thus, it is an Interrogative Pronoun."
    },
    {
        "q": "What is the part of speech of the word 'after' in: 'They arrived shortly after.'?",
        "opts": ["Preposition", "Conjunction", "Adverb", "Adjective"],
        "ans": 2,
        "sol": "Since 'after' has no noun object following it, it modifies the verb 'arrived' indicating time. Thus, it functions as an Adverb."
    },
    {
        "q": "What is the part of speech of 'after' in: 'They arrived after the storm had passed.'?",
        "opts": ["Preposition", "Conjunction", "Adverb", "Pronoun"],
        "ans": 1,
        "sol": "'after' connects the independent clause 'They arrived' with the dependent clause 'the storm had passed'. Hence, it functions as a Subordinating Conjunction."
    },
    {
        "q": "In the sentence: 'He took a book from the shelf,' the word 'from' is a/an:",
        "opts": ["Adverb", "Preposition", "Conjunction", "Interjection"],
        "ans": 1,
        "sol": "'from' establishes the relationship between 'took a book' and 'the shelf'. It functions as a Preposition."
    },
    {
        "q": "Identify the word class of 'all' in: 'All men are mortal.'",
        "opts": ["Adjective", "Pronoun", "Adverb", "Noun"],
        "ans": 0,
        "sol": "'All' modifies the noun 'men' directly. Therefore, it functions as a Limiting Adjective (or determiner)."
    },
    {
        "q": "Identify the word class of 'all' in: 'All of us were invited.'",
        "opts": ["Adjective", "Pronoun", "Adverb", "Noun"],
        "ans": 1,
        "sol": "In this sentence, 'All' stands in place of a noun phrase as the subject of the clause. Thus, it functions as an Indefinite Pronoun."
    },
    {
        "q": "Which part of speech is the word 'silently' in: 'She walked silently through the corridor.'?",
        "opts": ["Adjective", "Adverb", "Noun", "Preposition"],
        "ans": 1,
        "sol": "'silently' describes how the action 'walked' was performed, making it an Adverb of manner."
    },
    {
        "q": "In the sentence: 'The iron is hot,' the word 'hot' is a/an:",
        "opts": ["Noun", "Adjective", "Verb", "Adverb"],
        "ans": 1,
        "sol": "'hot' describes the state of the noun 'iron' and is placed after the linking verb 'is' (predicative use). Thus, it is an Adjective."
    },
    {
        "q": "What is the part of speech of the word 'class' in: 'This is a class project.'?",
        "opts": ["Noun", "Adjective", "Verb", "Pronoun"],
        "ans": 1,
        "sol": "Although 'class' is typically a noun, here it is used to modify the noun 'project'. Therefore, it functions as a noun adjunct or Adjective."
    },
    {
        "q": "In the sentence: 'Each of the boys got a prize,' the word 'Each' is a/an:",
        "opts": ["Distributive Pronoun", "Distributive Adjective", "Indefinite Pronoun", "Demonstrative Pronoun"],
        "ans": 0,
        "sol": "'Each' stands alone before the prepositional phrase 'of the boys' as the subject. Therefore, it is a Distributive Pronoun."
    },
    {
        "q": "In the sentence: 'Each boy got a prize,' the word 'Each' is a/an:",
        "opts": ["Distributive Pronoun", "Distributive Adjective", "Demonstrative Adjective", "Indefinite Pronoun"],
        "ans": 1,
        "sol": "Here, 'Each' directly modifies the singular noun 'boy'. Thus, it functions as a Distributive Adjective."
    },
    {
        "q": "Identify the conjunction in the sentence: 'Although he worked hard, he failed.'",
        "opts": ["Although", "worked", "hard", "failed"],
        "ans": 0,
        "sol": "'Although' is a subordinating conjunction introducing the concessive clause 'Although he worked hard'."
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Identify the part of speech of 'fast' in: 'He ran as fast as he could.'",
        "opts": ["Adjective", "Adverb", "Noun", "Verb"],
        "ans": 1,
        "sol": "In this sentence, 'fast' modifies the action verb 'ran'. Therefore, it is an Adverb."
    },
    {
        "q": "Which part of speech is 'that' in: 'Give me that pen.'?",
        "opts": ["Demonstrative Pronoun", "Demonstrative Adjective", "Relative Pronoun", "Conjunction"],
        "ans": 1,
        "sol": "'that' directly modifies the noun 'pen' to specify which pen. Hence, it functions as a Demonstrative Adjective."
    },
    {
        "q": "In the sentence: 'The baby cried for its mother,' the word 'its' is a/an:",
        "opts": ["Possessive Pronoun", "Possessive Adjective", "Personal Pronoun", "Demonstrative Adjective"],
        "ans": 1,
        "sol": "'its' modifies the noun 'mother' to show possession. Hence, it is a Possessive Adjective."
    },
    {
        "q": "What is the part of speech of the word 'running' in: 'He bought running shoes.'?",
        "opts": ["Gerund", "Present Participle (Adjective)", "Verb", "Noun adjunct"],
        "ans": 1,
        "sol": "'running' modifies the noun 'shoes' by describing their purpose/type, acting as a verbal adjective or Present Participle."
    },
    {
        "q": "Identify the type of verb underlined in the sentence: 'She is sleeping peacefully.'",
        "opts": ["Transitive Verb", "Intransitive Verb", "Modal Auxilary Verb", "Gerund"],
        "ans": 1,
        "sol": "The verb 'sleeping' does not transfer action to any direct object. Thus, it is an Intransitive Verb."
    },
    {
        "q": "In the sentence: 'Either you or he has to go,' what type of conjunction is used?",
        "opts": ["Coordinating", "Subordinating", "Correlative", "Distributive"],
        "ans": 2,
        "sol": "'Either...or' works as a pair to connect grammatically coordinate elements, classifying it as a Correlative Conjunction."
    },
    {
        "q": "Identify the relative pronoun in the sentence: 'The dog that barked all night belongs to our neighbor.'",
        "opts": ["that", "all", "our", "belongs"],
        "ans": 0,
        "sol": "'that' relates the dependent clause 'barked all night' back to the noun 'dog', functioning as a Relative Pronoun."
    },
    {
        "q": "What is the word class of 'about' in: 'We talked about our childhood plans.'?",
        "opts": ["Adverb", "Preposition", "Conjunction", "Adjective"],
        "ans": 1,
        "sol": "'about' is followed by the noun phrase object 'our childhood plans', functioning as a Preposition."
    },
    {
        "q": "Identify the word class of 'about' in: 'The train is about to leave.'?",
        "opts": ["Adverb", "Preposition", "Verb", "Adjective"],
        "ans": 0,
        "sol": "Here, 'about' modifies the infinitive 'to leave' indicating proximity of time. Therefore, it functions as an Adverb."
    },
    {
        "q": "Which part of speech is 'since' in the sentence: 'I have not seen him since we left school.'?",
        "opts": ["Preposition", "Conjunction", "Adverb", "Adjective"],
        "ans": 1,
        "sol": "'since' connects the main clause with the subordinate clausal time modifier 'we left school', functioning as a Subordinating Conjunction."
    },
    {
        "q": "What is the part of speech of the word 'since' in: 'I have not seen him since Monday.'?",
        "opts": ["Preposition", "Conjunction", "Adverb", "Noun"],
        "ans": 0,
        "sol": "'since' is followed directly by the noun object 'Monday', establishing a starting point in time. Hence, it is a Preposition."
    },
    {
        "q": "What is the part of speech of the word 'since' in: 'He left yesterday and I haven't seen him since.'?",
        "opts": ["Preposition", "Conjunction", "Adverb", "Adjective"],
        "ans": 2,
        "sol": "'since' stands alone without an object, modifying the verb phrase 'haven't seen' by indicating time. Hence, it is an Adverb."
    },
    {
        "q": "Identify the collective noun in: 'A fleet of ships was anchored at the harbor.'",
        "opts": ["fleet", "ships", "harbor", "anchored"],
        "ans": 0,
        "sol": "'fleet' is a collective noun representing a group of ships."
    },
    {
        "q": "In the sentence: 'Wow! That was a spectacular performance,' the word 'Wow!' is a/an:",
        "opts": ["Conjunction", "Interjection", "Adverb", "Adjective"],
        "ans": 1,
        "sol": "'Wow!' expresses strong, sudden emotion (admiration) and is grammatically independent. It is an Interjection."
    },
    {
        "q": "Identify the indefinite pronoun in: 'Many were called, but few were chosen.'",
        "opts": ["called", "but", "chosen", "Few / Many"],
        "ans": 3,
        "sol": "'Many' and 'few' function as Indefinite Pronouns because they represent unspecified groups of people."
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
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Master Nouns, Pronouns, Verbs, Adjectives, Adverbs, Prepositions, Conjunctions, and Interjections.", "sections": deep_dive_en}
    }

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Nouns, Pronouns & Adjectives",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which type of noun is 'committee'?", "opts": ["Proper Noun", "Abstract Noun", "Collective Noun", "Common Noun"], "ans": 2, "sol": "'Committee' represents a collective group of people acting as a single unit."},
                    {"type": "MCQ", "q": "In 'This is my book', what is the word 'my'?", "opts": ["Possessive Pronoun", "Possessive Adjective", "Personal Pronoun", "Demonstrative Pronoun"], "ans": 1, "sol": "'My' modifies the noun 'book' directly to show possession, making it a Possessive Adjective."},
                    {"type": "True/False", "q": "True or False: Relative pronouns connect relative clauses to their antecedent nouns.", "ans": True, "sol": "True. Relative pronouns like who, whom, and which relate dependent clauses to main nouns."},
                    {"type": "One-Liner", "q": "What type of noun represents a state, quality, or idea that cannot be physically touched?", "sol": "Abstract Noun"}
                ]
            },
            {
                "title": "2. Verbs & Adverbs",
                "masteryZone": [
                    {"type": "MCQ", "q": "What type of verb does not take a direct object?", "opts": ["Transitive Verb", "Intransitive Verb", "Auxiliary Verb", "Gerund"], "ans": 1, "sol": "Intransitive verbs do not transfer action to an object (e.g., 'sleep', 'arrive')."},
                    {"type": "MCQ", "q": "In 'She runs very fast', what is the word 'very'?", "opts": ["Adjective", "Adverb of Degree", "Verb", "Preposition"], "ans": 1, "sol": "'Very' modifies the adverb 'fast' by expressing degree, making it an Adverb of degree."},
                    {"type": "True/False", "q": "True or False: A Gerund is a verb form ending in -ing that functions as an adjective.", "ans": False, "sol": "False. A Gerund functions as a Noun; a Participle functions as an Adjective."},
                    {"type": "One-Liner", "q": "What abbreviation describes a verb form that behaves as a noun ending in -ing?", "sol": "Gerund"}
                ]
            },
            {
                "title": "3. Prepositions & Conjunctions",
                "masteryZone": [
                    {"type": "MCQ", "q": "In 'He stood before the door', what is the word 'before'?", "opts": ["Adverb", "Preposition", "Conjunction", "Adjective"], "ans": 1, "sol": "'Before' is followed by the object 'the door', making it a Preposition."},
                    {"type": "MCQ", "q": "Which of the following is a Coordinating Conjunction?", "opts": ["Although", "Because", "But", "Unless"], "ans": 2, "sol": "'But' is a coordinating conjunction (one of the FANBOYS)."},
                    {"type": "True/False", "q": "True or False: Subordinating conjunctions connect clauses of equal grammatical rank.", "ans": False, "sol": "False. Subordinating conjunctions connect dependent clauses to independent clauses. Coordinating conjunctions connect equal elements."},
                    {"type": "One-Liner", "q": "What part of speech is grammatically independent and expresses sudden emotion?", "sol": "Interjection"}
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
