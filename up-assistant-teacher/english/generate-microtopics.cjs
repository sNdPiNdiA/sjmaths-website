const fs = require('fs');
const path = require('path');

// ============================================================================
// ENV LOADER
// ============================================================================
if (fs.existsSync('.env')) {
    const envContent = fs.readFileSync('.env', 'utf8');
    for (const line of envContent.split('\n')) {
        const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
        if (match) {
            const key = match[1];
            let value = match[2] || '';
            if (value.startsWith('"') && value.endsWith('"')) value = value.slice(1, -1);
            if (value.startsWith("'") && value.endsWith("'")) value = value.slice(1, -1);
            process.env[key] = process.env[key] || value.trim();
        }
    }
}

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    console.error('GEMINI_API_KEY is not set. Please add it to .env file.');
    process.exit(1);
}

// ============================================================================
// CONSTANTS
// ============================================================================
const REQUEST_DELAY_MS = 20000;
const MAX_RETRIES = 5;
let currentModel = 'gemini-3.5-flash-lite';

// ============================================================================
// ENGLISH MICROTOPICS (Grammar, Comprehension, and Literature)
// ============================================================================
const MICROTOPICS = [
    // --- SECTION 1: GRAMMAR ---
    {
        dir: 'tenses-all-12-tenses',
        name: 'Tenses - All 12 Tenses',
        hindiName: 'Tenses - All 12 Tenses (काल)',
        description: 'Tenses - present, past, and future tenses, their sub-types, structure, rules, and examples.',
        keywords: ['Tenses', 'Present Tense', 'Past Tense', 'Future Tense', 'English Grammar', 'Verb Forms'],
        type: 'grammar'
    },
    {
        dir: 'articles-a-an-the',
        name: 'Articles - A, An, The',
        hindiName: 'Articles - A, An, The (आर्टिकल्स)',
        description: 'Articles - definite and indefinite articles, usage rules, omissions, and examples.',
        keywords: ['Articles', 'A An The', 'Definite Article', 'Indefinite Article', 'Grammar Rules'],
        type: 'grammar'
    },
    {
        dir: 'prepositions-usage-examples',
        name: 'Prepositions - Usage & Examples',
        hindiName: 'Prepositions - Usage & Examples (संबंधबोधक अव्यय)',
        description: 'Prepositions - simple, compound, and phrasal prepositions, rules of usage, and examples.',
        keywords: ['Prepositions', 'Preposition Usage', 'Preposition Examples', 'Grammar'],
        type: 'grammar'
    },
    {
        dir: 'conjunctions-types-usage',
        name: 'Conjunctions - Types & Usage',
        hindiName: 'Conjunctions - Types & Usage (समुच्चयबोधक अव्यय)',
        description: 'Conjunctions - coordinating, subordinating, and correlative conjunctions, their usage, and examples.',
        keywords: ['Conjunctions', 'Coordinating Conjunctions', 'Subordinating Conjunctions', 'Correlative Conjunctions', 'Linking Words'],
        type: 'grammar'
    },
    {
        dir: 'pronouns-personal-reflexive-demonstrative',
        name: 'Pronouns - Personal, Reflexive, Demonstrative',
        hindiName: 'Pronouns - Personal, Reflexive, Demonstrative (सर्वनाम)',
        description: 'Pronouns - personal, reflexive, demonstrative, relative, and other types, rules of agreement, and usage.',
        keywords: ['Pronouns', 'Personal Pronouns', 'Reflexive Pronouns', 'Demonstrative Pronouns', 'Pronoun Rules'],
        type: 'grammar'
    },
    {
        dir: 'nouns-countable-uncountable-collective',
        name: 'Nouns - Countable, Uncountable, Collective',
        hindiName: 'Nouns - Countable, Uncountable, Collective (संज्ञा)',
        description: 'Nouns - countable and uncountable nouns, collective nouns, abstract nouns, and noun gender/number rules.',
        keywords: ['Nouns', 'Countable Nouns', 'Uncountable Nouns', 'Collective Nouns', 'Noun Rules'],
        type: 'grammar'
    },
    {
        dir: 'verbs-transitive-intransitive-modal',
        name: 'Verbs - Transitive, Intransitive, Modal',
        hindiName: 'Verbs - Transitive, Intransitive, Modal (क्रिया)',
        description: 'Verbs - transitive and intransitive verbs, modal auxiliary verbs, finite and non-finite verbs.',
        keywords: ['Verbs', 'Transitive Verbs', 'Intransitive Verbs', 'Modal Verbs', 'Auxiliary Verbs'],
        type: 'grammar'
    },
    {
        dir: 'adjectives-comparative-superlative',
        name: 'Adjectives - Comparative, Superlative',
        hindiName: 'Adjectives - Comparative, Superlative (विशेषण)',
        description: 'Adjectives - degrees of comparison (positive, comparative, superlative), rules of formation, and correct usage.',
        keywords: ['Adjectives', 'Degrees of Comparison', 'Comparative', 'Superlative', 'Adjective Rules'],
        type: 'grammar'
    },
    {
        dir: 'adverbs-types-position',
        name: 'Adverbs - Types & Position',
        hindiName: 'Adverbs - Types & Position (क्रियाविशेषण)',
        description: 'Adverbs - adverbs of time, place, manner, frequency, degree, rules of placement, and comparison.',
        keywords: ['Adverbs', 'Types of Adverbs', 'Position of Adverbs', 'Adverbial Phrases', 'Adverb Rules'],
        type: 'grammar'
    },
    {
        dir: 'subject-verb-agreement',
        name: 'Subject-Verb Agreement',
        hindiName: 'Subject-Verb Agreement (कर्ता-क्रिया सामंजस्य)',
        description: 'Subject-verb agreement - rules of concord, singular/plural subjects, collective nouns, compound subjects, and typical error patterns.',
        keywords: ['Subject Verb Agreement', 'Subject Verb Concord', 'Concord Rules', 'Grammar Errors'],
        type: 'grammar'
    },
    {
        dir: 'error-spotting-sentence-correction',
        name: 'Error Spotting & Sentence Correction',
        hindiName: 'Error Spotting & Sentence Correction (त्रुटि पहचान)',
        description: 'Error spotting and sentence correction - identifying grammatical errors, syntactic improvements, and word usage corrections.',
        keywords: ['Error Spotting', 'Sentence Correction', 'Grammar Errors', 'Spotting Errors', 'Sentence Improvement'],
        type: 'grammar'
    },
    {
        dir: 'fill-in-the-blanks-sentence-completion',
        name: 'Fill in the Blanks & Sentence Completion',
        hindiName: 'Fill in the Blanks & Sentence Completion (रिक्त स्थान पूर्ति)',
        description: 'Fill in the blanks and sentence completion - vocabulary fit, grammatical agreement, idiomatic expressions.',
        keywords: ['Fill in the blanks', 'Sentence Completion', 'Vocabulary Practice', 'Grammar Practice'],
        type: 'grammar'
    },

    // --- SECTION 2: COMPREHENSION ---
    {
        dir: 'reading-comprehension-main-idea',
        name: 'Reading Comprehension - Main Idea',
        hindiName: 'Reading Comprehension - Main Idea (पठन बोध - मुख्य विचार)',
        description: 'Reading comprehension strategies - identifying the main theme, primary purpose, central argument, and key details of a passage.',
        keywords: ['Reading Comprehension', 'Main Idea', 'Central Theme', 'Primary Purpose', 'Comprehension Strategies'],
        type: 'comprehension'
    },
    {
        dir: 'reading-comprehension-inference',
        name: 'Reading Comprehension - Inference',
        hindiName: 'Reading Comprehension - Inference (पठन बोध - निष्कर्ष एवं अनुमान)',
        description: 'Reading comprehension strategies - drawing logical inferences, understanding implied meanings, reading between the lines.',
        keywords: ['Inference', 'Logical Deduction', 'Implied Meaning', 'Comprehension Skills', 'Reading Strategies'],
        type: 'comprehension'
    },
    {
        dir: 'reading-comprehension-vocabulary-in-context',
        name: 'Reading Comprehension - Vocabulary in Context',
        hindiName: 'Reading Comprehension - Vocabulary in Context (पठन बोध - शब्दावली)',
        description: 'Reading comprehension strategies - deducing word meanings in context, identifying synonym/antonym relations within a passage.',
        keywords: ['Contextual Vocabulary', 'Word Meanings', 'Synonyms in Context', 'Comprehension Vocabulary'],
        type: 'comprehension'
    },
    {
        dir: 'reading-comprehension-tone-author',
        name: 'Reading Comprehension - Tone & Author\'s View',
        hindiName: 'Reading Comprehension - Tone & Author\'s View (पठन बोध - लेखक का दृष्टिकोण)',
        description: 'Reading comprehension strategies - recognizing the tone, attitude, style, and objective/subjective view of the author.',
        keywords: ['Author Tone', 'Author Viewpoint', 'Attitude of Author', 'Comprehension Tone', 'Style of Writing'],
        type: 'comprehension'
    },
    {
        dir: 'summary-writing',
        name: 'Summary Writing',
        hindiName: 'Summary Writing (सारांश लेखन)',
        description: 'Summary writing - condensing a passage, identifying essential points, avoiding redundancy, and structured drafting.',
        keywords: ['Summary Writing', 'Condensation', 'Précis Writing', 'Key Points Extraction', 'Drafting Skills'],
        type: 'comprehension'
    },
    {
        dir: 'note-making-paraphrasing',
        name: 'Note Making & Paraphrasing',
        hindiName: 'Note Making & Paraphrasing (नोट निर्माण एवं व्याख्या)',
        description: 'Note making and paraphrasing - formatting notes, abbreviations, restructuring sentences without changing meaning.',
        keywords: ['Note Making', 'Paraphrasing', 'Restructuring Text', 'Abbreviation Rules', 'Structured Notes'],
        type: 'comprehension'
    },
    {
        dir: 'short-answer-long-answer-questions',
        name: 'Short Answer & Long Answer Questions',
        hindiName: 'Short Answer & Long Answer Questions (लघु/विस्तृत प्रश्न)',
        description: 'Short and long answer comprehension questions - referencing the text, logical structure, word limits, and clarity.',
        keywords: ['Comprehension Questions', 'Short Answers', 'Long Answers', 'Writing Answers', 'Descriptive English'],
        type: 'comprehension'
    },
    {
        dir: 'textual-grammar-usage',
        name: 'Textual Grammar & Usage',
        hindiName: 'Textual Grammar & Usage (पाठ्य व्याकरण एवं प्रयोग)',
        description: 'Textual grammar - analyzing parts of speech, voice, narration, clause structure, and word choices directly from a passage.',
        keywords: ['Textual Grammar', 'Voice and Narration', 'Clause Analysis', 'Contextual Grammar', 'Syntactic Structure'],
        type: 'comprehension'
    },
    {
        dir: 'coherence-cohesion-in-text',
        name: 'Coherence & Cohesion in Text',
        hindiName: 'Coherence & Cohesion in Text (सुसंगति एवं संयोजन)',
        description: 'Coherence and cohesion - transition words, pronoun references, paragraph flow, and logical structuring of texts.',
        keywords: ['Coherence', 'Cohesion', 'Transition Words', 'Paragraph Flow', 'Text Connectives'],
        type: 'comprehension'
    },
    {
        dir: 'critical-analysis-of-passage',
        name: 'Critical Analysis of Passage',
        hindiName: 'Critical Analysis of Passage (गद्यांश का गहन विश्लेषण)',
        description: 'Critical analysis of passages - evaluating arguments, identifying logical fallacies, checking validity of claims.',
        keywords: ['Critical Analysis', 'Evaluation of Arguments', 'Logical Fallacies', 'Critical Reading'],
        type: 'comprehension'
    },

    // --- SECTION 3: LITERATURE ---
    {
        dir: 'william-shakespeare-plays-sonnets',
        name: 'William Shakespeare - Plays & Sonnets',
        hindiName: 'William Shakespeare - Plays & Sonnets',
        description: 'William Shakespeare - biography, major tragedies, comedies, historical plays, themes, style, and structure of sonnets.',
        keywords: ['William Shakespeare', 'Shakespeare Plays', 'Shakespeare Sonnets', 'Tragedies and Comedies', 'Elizabethan Drama'],
        type: 'literature'
    },
    {
        dir: 'jane-austen-pride-and-prejudice',
        name: 'Jane Austen - Pride and Prejudice',
        hindiName: 'Jane Austen - Pride and Prejudice',
        description: 'Jane Austen - life, key themes in novels, detailed study of Pride and Prejudice, character profiles (Elizabeth, Darcy), and social satire.',
        keywords: ['Jane Austen', 'Pride and Prejudice', 'Elizabeth Bennet', 'Fitzwilliam Darcy', 'Regency Novel', 'Social Satire'],
        type: 'literature'
    },
    {
        dir: 'charles-dickens-great-expectations-oliver-twist',
        name: 'Charles Dickens - Great Expectations, Oliver Twist',
        hindiName: 'Charles Dickens - Great Expectations, Oliver Twist',
        description: 'Charles Dickens - Victorian era context, themes of class, crime, industrialization, study of Great Expectations and Oliver Twist.',
        keywords: ['Charles Dickens', 'Great Expectations', 'Oliver Twist', 'Pip', 'Victorian Novel', 'Social Realism'],
        type: 'literature'
    },
    {
        dir: 'mark-twain-adventures-of-tom-sawyer',
        name: 'Mark Twain - Adventures of Tom Sawyer',
        hindiName: 'Mark Twain - Adventures of Tom Sawyer',
        description: 'Mark Twain - American realism, study of The Adventures of Tom Sawyer, themes of youth, freedom, hypocrisy, and humor.',
        keywords: ['Mark Twain', 'Tom Sawyer', 'Huckleberry Finn', 'American Realism', 'Satire', 'Youth Themes'],
        type: 'literature'
    },
    {
        dir: 'rabindranath-tagore-gitanjali-kabuliwala',
        name: 'Rabindranath Tagore - Gitanjali, Kabuliwala',
        hindiName: 'Rabindranath Tagore - Gitanjali, Kabuliwala',
        description: 'Rabindranath Tagore - Indian literature in English, spiritual poetry of Gitanjali, theme of human relationships in Kabuliwala.',
        keywords: ['Rabindranath Tagore', 'Gitanjali', 'Kabuliwala', 'Nobel Prize', 'Indian Poetry', 'Short Stories'],
        type: 'literature'
    },
    {
        dir: 'william-wordsworth-romantic-poetry',
        name: 'William Wordsworth - Romantic Poetry',
        hindiName: 'William Wordsworth - Romantic Poetry',
        description: 'William Wordsworth - Romanticism, concept of nature, Lyrical Ballads, analysis of major poems (Daffodils, Tintern Abbey).',
        keywords: ['William Wordsworth', 'Romantic Poetry', 'Nature Poet', 'Lyrical Ballads', 'Daffodils', 'Romantic Revival'],
        type: 'literature'
    },
    {
        dir: 'john-keats-odes-sonnets',
        name: 'John Keats - Odes & Sonnets',
        hindiName: 'John Keats - Odes & Sonnets',
        description: 'John Keats - second generation Romanticism, theme of beauty and transience, analysis of major odes (Ode to a Nightingale, Ode on a Grecian Urn).',
        keywords: ['John Keats', 'Odes of Keats', 'Ode to a Nightingale', 'Ode on a Grecian Urn', 'Negative Capability', 'Romantic Poetry'],
        type: 'literature'
    },
    {
        dir: 'robert-frost-modern-american-poetry',
        name: 'Robert Frost - Modern American Poetry',
        hindiName: 'Robert Frost - Modern American Poetry',
        description: 'Robert Frost - rustic settings, colloquial language, philosophical themes, analysis of Stopping by Woods, The Road Not Taken.',
        keywords: ['Robert Frost', 'Stopping by Woods', 'The Road Not Taken', 'American Poetry', 'Modernist Poetry', 'Metaphorical Poetry'],
        type: 'literature'
    },
    {
        dir: 'ts-eliot-modernist-poetry',
        name: 'T.S. Eliot - Modernist Poetry',
        hindiName: 'T.S. Eliot - Modernist Poetry',
        description: 'T.S. Eliot - Modernism, objective correlative, fragmentation, analysis of Love Song of J. Alfred Prufrock, The Waste Land.',
        keywords: ['T.S. Eliot', 'Prufrock', 'The Waste Land', 'Modernist Poetry', 'Objective Correlative', '20th Century Literature'],
        type: 'literature'
    },
    {
        dir: 'poetry-comprehension-themes-devices',
        name: 'Poetry Comprehension - Themes & Devices',
        hindiName: 'Poetry Comprehension - Themes & Devices',
        description: 'Poetry comprehension - stanza-wise analysis, theme identification, tone, rhyming scheme, and poetic devices.',
        keywords: ['Poetry Comprehension', 'Poetic Devices', 'Rhyme Scheme', 'Theme Analysis', 'Stanza Reading'],
        type: 'literature'
    },
    {
        dir: 'novel-comprehension-character-analysis',
        name: 'Novel Comprehension - Character Analysis',
        hindiName: 'Novel Comprehension - Character Analysis',
        description: 'Novel comprehension - plot structures, narrative perspective, character motivations, and thematic development.',
        keywords: ['Novel Comprehension', 'Character Analysis', 'Plot Structure', 'Narrative Perspective', 'Thematic Analysis'],
        type: 'literature'
    },
    {
        dir: 'short-story-plot-moral',
        name: 'Short Story - Plot & Moral',
        hindiName: 'Short Story - Plot & Moral',
        description: 'Short story analysis - exposition, climax, resolution, moral message, character arcs.',
        keywords: ['Short Story Analysis', 'Story Plot', 'Story Climax', 'Moral Lesson', 'Character Arc'],
        type: 'literature'
    },
    {
        dir: 'literary-devices-metaphor-simile-alliteration',
        name: 'Literary Devices - Metaphor, Simile, Alliteration',
        hindiName: 'Literary Devices - Metaphor, Simile, Alliteration',
        description: 'Literary devices - identification and effect of metaphor, simile, personification, alliteration, hyperbole, oxymoron.',
        keywords: ['Literary Devices', 'Figures of Speech', 'Metaphor', 'Simile', 'Alliteration', 'Personification', 'Oxymoron'],
        type: 'literature'
    },
    {
        dir: 'prose-style-narrative-descriptive',
        name: 'Prose Style - Narrative & Descriptive',
        hindiName: 'Prose Style - Narrative & Descriptive',
        description: 'Prose styles - narrative techniques, descriptive style, expository writing, persuasive techniques.',
        keywords: ['Prose Style', 'Narrative Style', 'Descriptive Style', 'Expository Prose', 'Writing Styles'],
        type: 'literature'
    },
    {
        dir: 'vocabulary-building-synonyms-antonyms-one-word-substitution',
        name: 'Vocabulary Building - Synonyms, Antonyms, One-word Substitution',
        hindiName: 'Vocabulary Building - Synonyms, Antonyms, One-word Substitution',
        description: 'Vocabulary building - common synonyms, antonyms, one-word substitutions, idioms, and phrases for UP Assistant Teacher.',
        keywords: ['Vocabulary Building', 'Synonyms Antonyms', 'One Word Substitution', 'Idioms and Phrases', 'English Vocabulary'],
        type: 'literature'
    }
];

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// ============================================================================
// GEMINI API CLIENT
// ============================================================================
async function callGemini(prompt, retries = MAX_RETRIES) {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${currentModel}:generateContent?key=${apiKey}`;
            const res = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: {
                        temperature: 0.7,
                        maxOutputTokens: 65536,
                        topP: 0.95,
                    },
                }),
            });

            if (res.status === 429 || res.status === 403) {
                console.log(`  ⚠️ Rate limited. Waiting before retry ${attempt}/${retries}...`);
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⏳ Waiting ${wait / 1000}s...`);
                await sleep(wait);
                continue;
            }

            if (res.status === 503) {
                const wait = REQUEST_DELAY_MS * 2;
                console.log(`  ⏳ Service unavailable (503). Waiting ${wait / 1000}s before retry ${attempt}/${retries}...`);
                await sleep(wait);
                continue;
            }

            if (!res.ok) {
                const errBody = await res.text();
                throw new Error(`Gemini API error ${res.status}: ${errBody.substring(0, 200)}`);
            }

            const data = await res.json();
            const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
            if (!text || text.trim().length === 0) {
                throw new Error('Empty response from API');
            }
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️ Retry ${attempt}/${retries} after error: ${err.message}`);
            await sleep(5000);
        }
    }
    throw new Error('Max retries exceeded');
}

// ============================================================================
// JSON PARSER
// ============================================================================
function parseResponse(raw) {
    if (!raw || typeof raw !== 'string') {
        throw new Error('Invalid response: expected string, got ' + typeof raw);
    }

    let cleaned = raw.trim();

    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    try { return JSON.parse(cleaned); } catch (err) { }

    const jsonMatch = cleaned.match(/[\{\[][\s\S]*[\}\]]/);
    if (jsonMatch) {
        const repaired = jsonMatch[0]
            .replace(/(\{|,|\[|\s)([A-Za-z0-9_\-]+)\s*:/g, '$1"$2":')
            .replace(/'([^'\\]*(?:\\.[^'\\]*)*)'/g, '"$1"')
            .replace(/,\s*([}\]])/g, '$1');
        try { return JSON.parse(repaired); } catch (e) {
            try { return JSON.parse(Function('"use strict"; return (' + repaired + ')')()); } catch (e2) { }
        }
    }

    const jsonStart = cleaned.indexOf('{');
    if (jsonStart >= 0) {
        let partial = cleaned.substring(jsonStart);
        partial = partial.replace(/,\s*$/, '');
        let opens = 0, closes = 0, openArr = 0, closeArr = 0;
        let inString = false, escape = false;
        for (let i = 0; i < partial.length; i++) {
            const ch = partial[i];
            if (escape) { escape = false; continue; }
            if (ch === '\\') { escape = true; continue; }
            if (ch === '"') { inString = !inString; continue; }
            if (inString) continue;
            if (ch === '{') opens++;
            else if (ch === '}') closes++;
            else if (ch === '[') openArr++;
            else if (ch === ']') closeArr++;
        }
        if (inString) partial += '"';
        while (openArr > closeArr) { partial += ']'; closeArr++; }
        while (opens > closes) { partial += '}'; closes++; }
        partial = partial.replace(/,\s*([}\]])/g, '$1');
        try { return JSON.parse(partial); } catch (e) {
            try { return JSON.parse(Function('"use strict"; return (' + partial + ')')()); } catch (e2) { }
        }
    }

    console.error('❌ Raw response (first 500 chars):', cleaned.substring(0, 500));
    throw new Error('No valid JSON found in response');
}

// ============================================================================
// PROMPT BUILDER — Concepts/Theories Tab (ENGLISH ONLY, NO PARAGRAPHS)
// ============================================================================
function buildConceptsPrompt(topic) {
    let focusInstructions = '';

    if (topic.type === 'literature') {
        focusInstructions = `Since this is an English LITERATURE topic:
- Focus on the **author's life, literary period/movement, key works, plot summaries, characters, themes, style, and iconic quotes**.
- In SECTION 2 (Concepts and Theories), structure subcards around biographical context, major themes, analysis of key works, and literary style.
- In SECTION 3 (Important Facts and Data), include tables detailing:
  a) List of major works, publication years, and genres.
  b) Major characters, their roles, and parent works.
  c) Famous quotes, their speakers, and source works.
  d) Key literary terms/movements associated with this topic.`;
    } else {
        focusInstructions = `Since this is an English GRAMMAR/COMPREHENSION topic:
- Focus on **definitions, classification, strict grammatical rules, syntactic structures, exceptions, and usage guidelines**.
- In SECTION 2 (Concepts and Theories), structure subcards around core rules, usage cases, formulas, sentence structures, and step-by-step methods.
- In SECTION 3 (Important Facts and Data), include tables detailing:
  a) Core rules, formulas, and structural formulas.
  b) Common sentence templates and examples.
  c) Grammatical exceptions and comparison of correct vs. incorrect usage.
  d) Differences between closely related terms (e.g., transitive vs. intransitive, coordinate vs. subordinate).`;
    }

    return `You are an expert faculty member for UP Assistant Teacher (अंग्रेजी) exam preparation. Create ULTRA-COMPREHENSIVE, EXAM-FOCUSED concept notes for the topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: English (अंग्रेजी)
- Exam: UP Assistant Teacher Recruitment Examination
- Topic Directory: ${topic.dir}
- Keywords to target: ${topic.keywords.join(', ')}

${focusInstructions}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. **STRICTLY NO PARAGRAPHS** — Do NOT use the "paragraph" type anywhere. Every section must be a table, list, or subcards.
2. Content must be **point-wise, bulleted, tabular, and structured** for rapid exam revision.
3. Use **bold** for key terms, names, dates, and figures within table cells and list items.
4. Content must be **comprehensive and exam-focused** — cover ALL important facts, concepts, and principles that UP Assistant Teacher asks.
5. **LANGUAGE: Use ENGLISH ONLY** for all content including headers, rows, and items.

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- A comprehensive overview table with 8-10 rows covering: What/Who, Era/Period, Why Important, Key Features, Sub-types/Major Works, Significance for Exam, and other essential facts.
- Headers: ["Aspect", "Key Details"]

SECTION 2 — "Concepts and Theories" (type: "subcards")
- 5-7 subcards, each covering a major sub-topic or theme.
- Each subcard must have a title and detailed point-wise content (NOT paragraphs).
- Include at least 2-3 powerful mnemonics within these subcards to help memorize sequences, lists, and facts.

SECTION 3 — "Important Facts and Data" (type: "table")
- 3-4 detailed tables with 8-12 rows each covering the details specified in the focus instructions above.

SECTION 4 — "Tricks to Remember" (type: "list")
- 6-8 items with "term" = trick title, "definition" = detailed trick explanation
- Include memory tricks, acronyms, association techniques, and quick recall methods in English

SECTION 5 — "Mistakes to Avoid" (type: "list")
- 6-8 items with "term" = common mistake, "definition" = correct fact/rule and why students get confused
- Cover frequently confused concepts, facts, and rules

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items with "term" = key point title, "definition" = concise point-wise summary
- This is the final revision summary covering ALL essential facts

ADDITIONAL REQUIREMENTS:
- "upscNotes": Include 4-6 notes with type "tip" (exam strategy) and "trap" (common traps)
- "keyTakeaways": Include 5-8 concise, high-yield takeaways

OUTPUT FORMAT — Return ONLY valid JSON with this exact structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["Aspect", "Key Details"],
      "rows": [
        ["Aspect 1", "**Key detail** with bold important terms"],
        ["Aspect 2", "Another **important** detail"]
      ]
    },
    {
      "title": "Concepts and Theories",
      "type": "subcards",
      "items": [
        {
          "title": "Sub-topic 1 with **mnemonic**",
          "content": "• Point 1 with **bold** terms\\n• Point 2 with **bold** terms\\n• **Mnemonic:** Phrase to remember"
        }
      ]
    },
    {
      "title": "Important Facts and Data",
      "type": "table",
      "headers": ["Column 1", "Column 2", "Column 3"],
      "rows": [
        ["Data 1", "Data 2", "Data 3"]
      ]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [
        {
          "term": "Trick 1: Title",
          "definition": "Detailed explanation of the trick with **bold** key terms"
        }
      ]
    },
    {
      "title": "Mistakes to Avoid",
      "type": "list",
      "items": [
        {
          "term": "Mistake 1: Common error",
          "definition": "Correct fact and why students get confused"
        }
      ]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [
        {
          "term": "Key Point 1",
          "definition": "Concise summary point with **bold** key terms"
        }
      ]
    }
  ],
  "upscNotes": [
    {
      "type": "tip",
      "content": "Exam strategy tip for UP Assistant Teacher"
    },
    {
      "type": "trap",
      "content": "Common trap students fall into"
    }
  ],
  "keyTakeaways": [
    "High-yield takeaway 1",
    "High-yield takeaway 2"
  ]
}

IMPORTANT:
- Use ONLY English text. Do NOT use Hindi or bilingual format.
- Every section must be comprehensive and detailed — this is for serious exam preparation.
- Include ALL important facts, figures, names, dates, rules, and concepts.
- The content must be exam-focused with keywords naturally embedded.
- NO paragraphs anywhere — only tables, lists, and subcards.`;
}

// ============================================================================
// FALLBACK CONCEPTS DATA
// ============================================================================
function buildFallbackConcepts(topic) {
    return {
        sections: [
            {
                title: 'Detailed Brief Overview',
                type: 'table',
                headers: ['Aspect', 'Key Details'],
                rows: [
                    ['Topic', `**${topic.name}** (${topic.hindiName})`],
                    ['Subject', '**English** for UP Assistant Teacher'],
                    ['Status', 'Content under preparation — check back soon for comprehensive notes']
                ]
            }
        ],
        upscNotes: [
            { type: 'tip', content: `This topic is important for UP Assistant Teacher exam. Study ${topic.name} thoroughly.` }
        ],
        keyTakeaways: [
            `Study ${topic.name} thoroughly for UP Assistant Teacher`,
            'Focus on important concepts, facts, and principles',
            'Practice with previous year questions'
        ]
    };
}

// ============================================================================
// MAIN GENERATION LOOP
// ============================================================================
async function main() {
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ UP Assistant Teacher - English Microtopics Generator         ║');
    console.log(`║ Model: ${currentModel}                                          ║`);
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

    const totalTopics = MICROTOPICS.length;
    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < totalTopics; i++) {
        const topic = MICROTOPICS[i];
        console.log(`\n${'='.repeat(80)}`);
        console.log(`[${i + 1}/${totalTopics}] Processing: ${topic.name} (${topic.hindiName}) [Type: ${topic.type}]`);
        console.log(`${'='.repeat(80)}`);

        // Create microtopic folder directly under english
        const outputDir = path.join(process.cwd(), 'up-assistant-teacher', 'english', topic.dir);
        fs.mkdirSync(outputDir, { recursive: true });

        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData = null;

        try {
            console.log('  📝 Generating concepts/theories content...');
            const prompt = buildConceptsPrompt(topic);
            const raw = await callGemini(prompt);
            const parsed = parseResponse(raw);

            if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
                throw new Error('Generated content missing "sections" array');
            }

            // Ensure no paragraph type sections
            const paragraphSections = parsed.sections.filter(s => s.type === 'paragraph');
            if (paragraphSections.length > 0) {
                console.log('  ⚠️ Found paragraph sections — converting to list format...');
                parsed.sections = parsed.sections.map(section => {
                    if (section.type === 'paragraph') {
                        return {
                            title: section.title,
                            type: 'list',
                            items: [{ term: 'Key Point', definition: section.content || '' }]
                        };
                    }
                    return section;
                });
            }

            conceptsData = parsed;
            console.log('  ✅ Concepts content generated successfully!');

            fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
            console.log('  💾 Saved tabs/concepts.json');

            successCount++;
        } catch (err) {
            console.error(`  ❌ Failed to generate concepts: ${err.message}`);
            conceptsData = buildFallbackConcepts(topic);
            failCount++;
        }

        // Generate index.html with 4-tab structure
        const html = assembleMicrotopicPage(topic, conceptsData);
        fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
        console.log('  💾 Saved index.html');

        // Save data.json
        fs.writeFileSync(path.join(outputDir, 'data.json'), JSON.stringify({
            concepts: conceptsData,
            practice: null,
            pyqs: null,
            test: null
        }, null, 2), 'utf8');
        console.log('  💾 Saved data.json');

        console.log(`  🎉 Completed: ${topic.name}`);

        if (i < totalTopics - 1) {
            console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s before next topic...`);
            await sleep(REQUEST_DELAY_MS);
        }
    }

    console.log(`\n${'='.repeat(80)}`);
    console.log(`📊 SUMMARY: ${successCount} succeeded, ${failCount} failed out of ${totalTopics} topics`);
    console.log(`${'='.repeat(80)}`);
    console.log('\n✅ All English microtopic pages generated successfully!');
    console.log('📁 Microtopic folders created directly under: up-assistant-teacher/english/');
}

// ============================================================================
// HTML PAGE ASSEMBLER — 4-Tab Structure for Microtopics
// ============================================================================
function assembleMicrotopicPage(topic, conceptsData) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/up-assistant-teacher/english/${topic.dir}/`;
    const title = `${topic.name} | ${topic.hindiName} - अंग्रेजी | SJMaths`;
    const description = topic.description;

    return `<!DOCTYPE html>
<html lang="hi">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <meta name="description" content="${description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="${canonicalUrl}">
    <meta name="keywords" content="${topic.keywords.join(', ')}, UP Assistant Teacher, अंग्रेजी, English">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="${canonicalUrl}">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title}">
    <meta name="twitter:description" content="${description}">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 10px 30px -5px rgba(212, 175, 55, 0.1);
            --accent-gradient: linear-gradient(135deg, #d4af37, #2980b9);
        }
        body.dark-mode {
            --glass-bg: rgba(30, 30, 46, 0.95);
            --glass-border: rgba(255, 255, 255, 0.05);
            --shadow-lg: 0 10px 30px -5px rgba(0, 0, 0, 0.3);
        }
        .topic-container {
            max-width: 1100px;
            margin: 2rem auto;
            padding: 2.5rem 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }
        .breadcrumbs {
            margin-bottom: 1.5rem;
            font-size: 0.88rem;
            color: #64748b;
            background: rgba(255, 255, 255, 0.6);
            display: inline-block;
            padding: 0.6rem 1.2rem;
            border-radius: 999px;
            border: 1px solid rgba(0, 0, 0, 0.04);
        }
        .breadcrumbs a {
            color: #d4af37;
            text-decoration: none;
            font-weight: 500;
        }
        .breadcrumbs a:hover {
            text-decoration: underline;
        }
        .breadcrumbs i {
            margin: 0 0.5rem;
            font-size: 0.7rem;
            color: #94a3b8;
        }
        .topic-header {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.03), rgba(41, 128, 185, 0.03));
            border: 1px solid rgba(212, 175, 55, 0.1);
            border-radius: 1.25rem;
            padding: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .topic-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(2rem, 5vw, 2.5rem);
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.75rem;
            line-height: 1.2;
        }
        .topic-desc {
            color: #475569;
            font-size: 1rem;
            line-height: 1.7;
            max-width: 700px;
            margin: 0 auto;
        }
        .topic-meta-bar {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            align-items: center;
            margin-top: 1.5rem;
            padding-top: 1.25rem;
            border-top: 1px solid rgba(0, 0, 0, 0.05);
        }
        .back-link {
            display: inline-block;
            margin-bottom: 1.5rem;
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .back-link:hover {
            text-decoration: underline;
        }
        .study-tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            padding: 0.55rem;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            margin-bottom: 2rem;
            position: sticky;
            top: 88px;
            z-index: 100;
            backdrop-filter: blur(16px);
            justify-content: center;
        }
        .tab-btn {
            border: none;
            background: transparent;
            color: #475569;
            padding: 0.65rem 1.1rem;
            border-radius: 999px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            font-family: 'Outfit', sans-serif;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
            white-space: nowrap;
        }
        .tab-btn:hover {
            background: rgba(212, 175, 55, 0.08);
            color: #d4af37;
        }
        .tab-btn.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 8px 20px rgba(212, 175, 55, 0.25);
        }
        .topic-content {
            min-height: 400px;
        }
        .tab-panel {
            display: none;
            animation: slideUp 0.4s ease-out;
        }
        .tab-panel.active {
            display: block;
        }
        .content-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-lg);
        }
        .content-card h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .content-card h2 i {
            color: #d4af37;
        }
        .content-card p, .content-card li {
            font-size: 0.95rem;
            color: var(--text-light);
            line-height: 1.7;
        }
        .content-card ul {
            margin: 0.5rem 0;
            padding-left: 1.5rem;
        }
        .content-card li {
            margin-bottom: 0.5rem;
        }
        @media (max-width: 768px) {
            .study-tabs {
                flex-wrap: nowrap;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                padding: 0.4rem;
                scrollbar-width: none;
                justify-content: flex-start;
            }
            .study-tabs::-webkit-scrollbar {
                display: none;
            }
            .tab-btn {
                font-size: 0.85rem;
                padding: 0.5rem 0.9rem;
            }
            .topic-container {
                padding: 0 1rem 2rem;
            }
            .topic-header {
                padding: 1.5rem 1rem;
            }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>

<body>
    <div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <a href="/up-assistant-teacher/english/" class="back-link"><i class="fas fa-arrow-left"></i> <span class="lang-hi">वापस अंग्रेजी पर जाएँ</span><span class="lang-en">Back to English</span></a>

        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right"></i>
            <a href="/up-assistant-teacher/">UP Assistant Teacher</a> <i class="fas fa-chevron-right"></i>
            <a href="/up-assistant-teacher/english/">अंग्रेजी</a> <i class="fas fa-chevron-right"></i>
            <span>${topic.hindiName}</span>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-hi">${topic.hindiName}</span>
                <span class="lang-en">${topic.name}</span>
            </h1>
            <p class="topic-desc">
                <span class="lang-hi">${topic.description}</span>
                <span class="lang-en">${topic.description}</span>
            </p>
            <div class="topic-meta-bar">
                <span style="display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; background: rgba(245, 158, 11, 0.1); color: #b45309; border: 1px solid rgba(245, 158, 11, 0.2);">
                    <i class="fas fa-signal"></i> <span class="lang-hi">मध्यम</span><span class="lang-en">Medium</span>
                </span>
                <span style="display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #475569; background: rgba(100, 116, 139, 0.06); border: 1px solid rgba(100, 116, 139, 0.12);">
                    <i class="fas fa-clock"></i> <span class="lang-hi">कुल 45 मिनट</span><span class="lang-en">45 min total</span>
                </span>
            </div>
        </div>

        <!-- Tabs Navigation -->
        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="tab-concepts" role="tab" aria-selected="true">
                <i class="fas fa-book-open"></i>
                <span class="lang-hi">1. अवधारणाएँ एवं सिद्धांत</span>
                <span class="lang-en">1. Concepts & Theories</span>
            </button>
            <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false">
                <i class="fas fa-list-check"></i>
                <span class="lang-hi">2. अभ्यास प्रश्न</span>
                <span class="lang-en">2. Practice Questions</span>
            </button>
            <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false">
                <i class="fas fa-stopwatch"></i>
                <span class="lang-hi">3. मिनी टेस्ट</span>
                <span class="lang-en">3. Mini Test</span>
            </button>
            <button class="tab-btn" data-tab="tab-revision" role="tab" aria-selected="false">
                <i class="fas fa-redo"></i>
                <span class="lang-hi">4. पुनरावृत्ति</span>
                <span class="lang-en">4. Revision</span>
            </button>
        </div>

        <!-- Tab Content Container -->
        <div class="topic-content" id="topic-content"></div>

        <!-- Embedded Data for Renderer -->
        <script id="upsc-page-data" type="application/json">
        ${JSON.stringify({
            topicId: 'up-assistant-teacher.english.' + topic.dir,
            topicName: topic.name,
            hindiName: topic.hindiName,
            subject: 'English',
            subjectDir: 'english',
            concepts: conceptsData || null,
            practice: null,
            pyqs: null,
            test: null,
            version: { generator: 'v1', prompt: '1.0' },
            contentHash: 'sha256-placeholder',
            generatedAt: now
        }, null, 2)}
        </script>
    </main>

    <div id="footer-container"></div>

    <button id="backToTop" class="back-to-top" aria-label="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabPanels = document.querySelectorAll('.tab-panel');

            tabButtons.forEach(function(button) {
                button.addEventListener('click', function() {
                    const targetTab = button.getAttribute('data-tab');

                    tabButtons.forEach(function(btn) {
                        btn.classList.remove('active');
                        btn.setAttribute('aria-selected', 'false');
                    });
                    button.classList.add('active');
                    button.setAttribute('aria-selected', 'true');

                    tabPanels.forEach(function(panel) {
                        panel.classList.remove('active');
                        if (panel.id === targetTab) {
                            panel.classList.add('active');
                        }
                    });
                });
            });
        });
    </script>

    <script src="/assets/js/upsc-renderer.min.js" defer data-cfasync="false"></script>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>

</html>`;
}

// ============================================================================
// RUN
// ============================================================================
main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
