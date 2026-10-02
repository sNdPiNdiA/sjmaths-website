#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) English Language & Literature
 * Complete English Syllabus Content Generation Engine
 * Pointwise Concept Notes, Memory Mnemonics, Tips, Tricks, Mindmap, Tables, 10 MCQs & Mini Test
 *
 * Subject: English Language & Literature (90 Questions | 270 Marks | -1 Negative Marking)
 * Covers all 24 canonical topics in up-upper-primary-teacher/english/
 *
 * Uses common CSS: /assets/css/up-upper-primary-topic.min.css?v=20261002_03
 * Uses common JS:  /assets/js/up-upper-primary-topic.min.js?v=20261002_02
 * STRICT RULE: No footer-container, no global-footer.min.js
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-generation-status-upper-primary-english.json');
const OUTPUT_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'english');

// 1. API Configuration & Key Rotation
const KEY_CONFIGS = [
  { key: process.env.GEMINI_API_KEY_1, name: 'KEY_1', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'] },
  { key: process.env.GEMINI_API_KEY_2, name: 'KEY_2', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'] },
  { key: process.env.GEMINI_API_KEY,   name: 'KEY_3', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'] }
].filter(c => Boolean(c.key));

if (KEY_CONFIGS.length === 0) {
  console.error('ERROR: No valid GEMINI_API_KEY found in environment.');
  process.exit(1);
}

let keyIndex = 0;
function getActiveConfig() {
  return KEY_CONFIGS[keyIndex % KEY_CONFIGS.length];
}

function rotateKey() {
  keyIndex++;
  const next = getActiveConfig();
  console.log(`  [Key Rotation] Rotating to next API key (${next.name})...`);
}

// 2. Command Line Arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const ALL = args.includes('--all');
const LIMIT = (() => {
  const idx = args.indexOf('--limit');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : null;
})();
const TARGET_SLUG = (() => {
  const idx = args.indexOf('--topic');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const CONCURRENCY = (() => {
  const idx = args.indexOf('--concurrency');
  return idx !== -1 && args[idx + 1] ? Math.max(1, parseInt(args[idx + 1], 10)) : 3;
})();

// 3. Status Tracking
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch (e) {
    statusMap = {};
  }
}

function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// 4. English Syllabus Catalog (24 Canonical Topics across 4 Modules)
export const ENGLISH_TOPICS = [
  // ==================== Module 1: English Grammar (12 Topics) ====================
  {
    slug: 'parts-of-speech-nouns-pronouns',
    numStr: '#1.1',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Parts of Speech: Nouns, Pronouns, Cases & Numbers',
    shortTitle: 'Nouns & Pronouns',
    chkId: 'chk-english-1-1',
    coreFocus: 'Noun classifications (Proper, Common, Collective, Abstract, Material), Countable vs Uncountable nouns, Rules of Pluralization & Irregular plurals, Cases (Nominative, Objective, Possessive/Genitive rules with apostrophe), Pronoun types (Personal, Demonstrative, Relative, Reflexive, Emphatic, Indefinite, Distributive, Reciprocal), Relative pronoun rules (who vs whom, which vs that), and Pronoun-antecedent agreement.'
  },
  {
    slug: 'verbs-modals-auxiliary',
    numStr: '#1.2',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Verbs, Auxiliary Verbs, Modals & Non-Finites',
    shortTitle: 'Verbs & Modals',
    chkId: 'chk-english-1-2',
    coreFocus: 'Transitive vs Intransitive verbs, Primary auxiliaries (be, do, have), Modal auxiliaries (can, could, may, might, shall, should, will, would, must, ought to, used to, need, dare) expressing ability, obligation, probability & permission, Semi-modals, Non-finite verbs: Infinitives (to-infinitive, bare infinitive after let, make, bid), Gerunds vs Present Participles, and Participle clauses with dangling modifier traps.'
  },
  {
    slug: 'adjectives-adverbs-degrees',
    numStr: '#1.3',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Adjectives, Degrees of Comparison & Adverbs',
    shortTitle: 'Adjectives & Adverbs',
    chkId: 'chk-english-1-3',
    coreFocus: 'Types of Adjectives (Qualitative, Quantitative, Demonstrative, Possessive), Order of Adjectives (OSASCOMP rule), Degrees of Comparison (Positive, Comparative, Superlative rules, irregular degrees like far/further/farther, elder/older), Adverbs (Manner, Place, Time, Frequency, Degree), Adverb positioning rules (Inversion with hardly, scarcely, no sooner, seldom), and confusing pairs (hard/hardly, late/lately).'
  },
  {
    slug: 'tenses',
    numStr: '#1.4',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Tenses and Time Aspects: 12 Structure Patterns & Usage',
    shortTitle: 'Tenses & Time Aspects',
    chkId: 'chk-english-1-4',
    coreFocus: '12 Tense aspect forms across Present, Past, and Future (Simple, Continuous, Perfect, Perfect Continuous), Time markers/adverbials for each tense, Stative verbs vs Dynamic verbs in progressive aspect, Conditional sentences (Type 0, 1, 2, 3 and mixed conditionals), Sequence of tenses rules in subordinate clauses, and high-frequency exam traps with since/for and past perfect.'
  },
  {
    slug: 'active-passive',
    numStr: '#1.5',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Active and Passive Voice: Transformation Rules across Tenses',
    shortTitle: 'Active & Passive Voice',
    chkId: 'chk-english-1-5',
    coreFocus: 'Voice transformation rules across all tenses (including 4 tenses with no standard passive), Subject-object interchange and agent omission, Passive of Imperative sentences (Let + obj + be + V3, You are requested/ordered/advised to), Interrogative sentences (Who -> By whom), Prepositional passive verbs, Double-object verbs (Direct vs Indirect object passivization), and Quasipassive constructions.'
  },
  {
    slug: 'direct-indirect',
    numStr: '#1.6',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Direct and Indirect Speech: Reporting Verbs, Tense Shifts & Pronoun Changes',
    shortTitle: 'Direct & Indirect Speech',
    chkId: 'chk-english-1-6',
    coreFocus: 'Reporting verb changes (said to -> told, asked, ordered, exclaimed, prayed), Backshift of tenses (Present -> Past, Past Simple -> Past Perfect) and universal truth/habitual fact exceptions, Pronoun changes using SON formula (Subject, Object, No change), Time and place word shifts (now -> then, here -> there, today -> that day), Narration of Interrogative (if/whether, wh-words), Imperative, and Exclamatory/Optative sentences.'
  },
  {
    slug: 'subject-verb',
    numStr: '#1.7',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Subject-Verb Concord & Agreement: Standard Grammatical Rules',
    shortTitle: 'Subject-Verb Concord',
    chkId: 'chk-english-1-7',
    coreFocus: 'Singular and plural subject agreement rules, Compound subjects joined by and vs as well as, with, together with, along with, in addition to, Correlative conjunctions (either...or, neither...nor, not only...but also: rule of proximity), Indefinite pronouns (each, everyone, either, neither, none, both, few), Collective nouns (singular vs plural), Expressions of quantity/distance/money, and More than one vs A number of / The number of.'
  },
  {
    slug: 'articles',
    numStr: '#1.8',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Articles & Determiners: Uses, Definite Article Rules & Omissions',
    shortTitle: 'Articles & Determiners',
    chkId: 'chk-english-1-8',
    coreFocus: 'Indefinite articles a vs an based on phonetic vowel/consonant sounds (e.g., an honest man, a European, an MBA), Definite article the rules: unique objects, superlatives, musical instruments, rivers/oceans/mountains, holy books, ordinal numbers, Omission of articles (zero article) before proper nouns, abstract nouns, meals, languages, diseases, school/church/hospital (primary purpose), and Quantifying determiners (few/a few/the few, little/a little/the little, some vs any).'
  },
  {
    slug: 'prepositions',
    numStr: '#1.9',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Prepositions & Phrasal Verbs: Spatial, Temporal & Fixed Forms',
    shortTitle: 'Prepositions & Phrasals',
    chkId: 'chk-english-1-9',
    coreFocus: 'Prepositions of Place (in, at, on, between, among, amongst, amid), Prepositions of Time (at, in, on, by, for, since, during), Prepositions of Motion/Direction (into, onto, towards, through, across, along), Fixed prepositions after verbs, nouns, and adjectives (e.g., abstain from, adhere to, look forward to + gerund, superior to), and High-yield phrasal verbs (break down/out/into, bring about/up, call off/on/for, put off/up with, carry out/on).'
  },
  {
    slug: 'conjunctions',
    numStr: '#1.10',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Conjunctions, Clause Analysis & Sentence Synthesis',
    shortTitle: 'Conjunctions & Clauses',
    chkId: 'chk-english-1-10',
    coreFocus: 'Coordinating conjunctions (FANBOYS: For, And, Nor, But, Or, Yet, So), Subordinating conjunctions of time, condition, cause, purpose, concession (although, though, lest...should, unless, until, so that), Correlative conjunctions pairs & parallel structure (scarcely...when, hardly...when, no sooner...than, either...or), Clauses analysis (Principal, Coordinate, Subordinate: Noun, Adjective/Relative, Adverbial clauses), and Sentence synthesis (Simple, Compound, Complex).'
  },
  {
    slug: 'error-spotting',
    numStr: '#1.11',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Error Spotting & Sentence Correction: Diagnostic Rules',
    shortTitle: 'Error Spotting Rules',
    chkId: 'chk-english-1-11',
    coreFocus: 'Systematic diagnostic framework for spotting errors in sentences: Subject-verb mismatch, Incorrect pronoun case, Misplaced and dangling modifiers, Faulty parallelism in series/comparisons, Redundancy and superfluous words (return back, suppose if, cousin brother), Incorrect tense sequence, Wrong preposition usage, and Double negatives.'
  },
  {
    slug: 'punctuation-question-tags',
    numStr: '#1.12',
    secIdx: 1,
    secTitle: 'English Grammar',
    title: 'Punctuation Marks, Capitalization & Question Tag Syntax',
    shortTitle: 'Punctuation & Question Tags',
    chkId: 'chk-english-1-12',
    coreFocus: 'Standard punctuation marks: Period/Full stop, Comma rules (serial comma, introductory clause, appositives), Semicolon vs Colon usage, Apostrophe in contractions and possessives, Dash vs Hyphen, Quotation marks, Capitalization conventions in titles and proper nouns, and Question tag syntax: Auxiliary + pronoun rule, Positive statement -> Negative tag, Negative statement -> Positive tag, Exceptions (I am -> arent I?, Imperatives -> will you? / shall we?).'
  },

  // ==================== Module 2: Vocabulary & Language Skills (4 Topics) ====================
  {
    slug: 'vocabulary-synonyms-antonyms',
    numStr: '#2.1',
    secIdx: 2,
    secTitle: 'Vocabulary & Language Skills',
    title: 'Synonyms & Antonyms: High-Frequency Competitive Arsenal',
    shortTitle: 'Synonyms & Antonyms',
    chkId: 'chk-english-2-1',
    coreFocus: 'High-frequency vocabulary root words (Latin & Greek roots, prefixes, suffixes), Synonyms and Antonyms frequently tested in UP teaching exams (e.g., Ephemeral, Ubiquitous, Diligent, Pragmatic, Lucrative, Candid, Alleviate, Meticulous, Ostentatious, Pernicious), Contextual shade of meanings, Tone elimination strategies (Positive vs Negative charge), and Pair association techniques.'
  },
  {
    slug: 'idioms-phrases-expressions',
    numStr: '#2.2',
    secIdx: 2,
    secTitle: 'Vocabulary & Language Skills',
    title: 'Idioms & Phrases: Everyday Figurative Expressions',
    shortTitle: 'Idioms & Phrases',
    chkId: 'chk-english-2-2',
    coreFocus: 'Categorized high-yield idioms and idiomatic phrases: Animal idioms, Color idioms, Body-part idioms, Conflict/Peace idioms (e.g., Burn the midnight oil, Once in a blue moon, Break the ice, At the drop of a hat, Bite the bullet, Call it a day, Spill the beans, Beat around the bush, Through thick and thin, Apple of discord, Achilles heel), Literal vs Figurative meanings, and Contextual usage in exam sentences.'
  },
  {
    slug: 'one-word-substitution',
    numStr: '#2.3',
    secIdx: 2,
    secTitle: 'Vocabulary & Language Skills',
    title: 'One Word Substitution: People, Science, Government & Practices',
    shortTitle: 'One Word Substitution',
    chkId: 'chk-english-2-3',
    coreFocus: 'Systematic categories of One Word Substitutions: Types of Government/Rule (-archy, -cracy: Monarchy, Plutocracy, Oligarchy, Bureaucracy), Scientific studies and professions (-ology, -ist: Philatelist, Numismatist, Somnambulist, Polyglot), Phobias & Manias (Claustrophobia, Bibliomania), Murders/Killings (-cide: Regicide, Patricide, Fratricide, Genocide), and Character traits (Altruist, Misanthrope, Egotist, Ascetic, Hedonist).'
  },
  {
    slug: 'spellings-confusing-words',
    numStr: '#2.4',
    secIdx: 2,
    secTitle: 'Vocabulary & Language Skills',
    title: 'Spellings, Homophones, Homonyms & Words Often Confused',
    shortTitle: 'Spellings & Confusing Words',
    chkId: 'chk-english-2-4',
    coreFocus: 'Spelling rules in English: i before e except after c, doubling final consonants before suffixes (occur -> occurred, begin -> beginning), dropping silent e vs retaining e (noticeable, courageous), High-frequency misspelled words (Accommodate, Millennium, Embarrass, Committee, Occurrence, Gauge, Lieutenant, Bureaucracy), Homophones and Homonyms (Affect vs Effect, Compliment vs Complement, Principal vs Principle, Stationary vs Stationery, Loose vs Lose).'
  },

  // ==================== Module 3: History of English Literature & Major Writers (6 Topics) ====================
  {
    slug: 'shakespeare-elizabethan-age',
    numStr: '#3.1',
    secIdx: 3,
    secTitle: 'History of English Literature & Major Writers',
    title: 'Elizabethan Age: Shakespeare, Dramatic Art & Playwrights',
    shortTitle: 'Shakespeare & Elizabethan Age',
    chkId: 'chk-english-3-1',
    coreFocus: 'Historical background of Elizabethan and Jacobean Age, University Wits (Marlowe, Lyly, Greene, Nashe, Lodge, Peele, Kyd), William Shakespeare: Biography, The Globe Theatre, 37 Plays categorized (Four Great Tragedies: Hamlet, Othello, King Lear, Macbeth; Romantic Comedies: As You Like It, Twelfth Night; Roman Plays: Julius Caesar; Problem Plays), 154 Sonnets structure (Shakespearean/English sonnet: 3 quatrains + 1 couplet, rhyme scheme abab cdcd efef gg), and famous soliloquies/quotes.'
  },
  {
    slug: 'milton-restoration-age',
    numStr: '#3.2',
    secIdx: 3,
    secTitle: 'History of English Literature & Major Writers',
    title: 'Puritan & Restoration Literature: John Milton & John Dryden',
    shortTitle: 'Milton & Restoration Age',
    chkId: 'chk-english-3-2',
    coreFocus: 'Puritan Interregnum and Restoration (1660), John Milton: Life, political pamphlets (Areopagitica), Major poetical works (Paradise Lost: 12 books, epic conventions, Grand style, Satan as tragic hero; Paradise Regained; Samson Agonistes; Lycidas - pastoral elegy), John Dryden: Father of English Criticism, Heroic couplet mastery, Absalom and Achitophel, Mac Flecknoe, and Restoration Comedy of Manners (Congreve, Wycherley).'
  },
  {
    slug: 'neoclassical-augustan-age',
    numStr: '#3.3',
    secIdx: 3,
    secTitle: 'History of English Literature & Major Writers',
    title: 'Augustan Age: Alexander Pope, Jonathan Swift, Addison & Dr. Johnson',
    shortTitle: 'Augustan & Neoclassical Age',
    chkId: 'chk-english-3-3',
    coreFocus: 'Neoclassical literary ideals: Reason, order, decorum, imitation of classical ancients, Alexander Pope: Mock-heroic epic (The Rape of the Lock: sylphs, Belinda, Baron), An Essay on Criticism, An Essay on Man, Jonathan Swift: Satiric prose (Gullivers Travels: Lilliput, Brobdingnag, Laputa, Houyhnhnms; A Modest Proposal), Joseph Addison and Richard Steele: The Spectator, Coverley Papers, Dr. Samuel Johnson: Dictionary of the English Language (1755), Preface to Shakespeare, Lives of the Poets.'
  },
  {
    slug: 'romantic-age-poets',
    numStr: '#3.4',
    secIdx: 3,
    secTitle: 'History of English Literature & Major Writers',
    title: 'Romantic Revival: Wordsworth, Coleridge, Keats & Shelley',
    shortTitle: 'Romantic Poets',
    chkId: 'chk-english-3-4',
    coreFocus: 'Romantic Revival (1798 Publication of Lyrical Ballads by Wordsworth & Coleridge), Wordsworths Preface to Lyrical Ballads (Poetry is the spontaneous overflow of powerful feelings recollected in tranquility; Tintern Abbey, The Prelude, Intimations of Immortality), S.T. Coleridge: Supernaturalism (The Rime of the Ancient Mariner, Kubla Khan, Christabel; Primary vs Secondary Imagination), Younger Romantics: John Keats (Negative Capability, Odes: To a Nightingale, On a Grecian Urn), P.B. Shelley (Ode to the West Wind, To a Skylark, Prometheus Unbound), and Lord Byron (Byronic hero, Don Juan).'
  },
  {
    slug: 'victorian-age-writers',
    numStr: '#3.5',
    secIdx: 3,
    secTitle: 'History of English Literature & Major Writers',
    title: 'Victorian Age: Tennyson, Robert Browning, Dickens & Hardy',
    shortTitle: 'Victorian Writers',
    chkId: 'chk-english-3-5',
    coreFocus: 'Victorian Age characteristics: Industrialization, compromise, conflict between science and religion, Alfred Lord Tennyson: Poet Laureate (In Memoriam A.H.H., Ulysses, The Lady of Shalott, The Charge of the Light Brigade), Robert Browning: Master of Dramatic Monologue (My Last Duchess, The Last Ride Together, Fra Lippo Lippi, Andrea del Sarto), Charles Dickens: Social realism novels (Great Expectations, David Copperfield, Oliver Twist, A Tale of Two Cities), and Thomas Hardy: Wessex regional novels, fatalism/pessimism (Tess of the dUrbervilles, The Mayor of Casterbridge, Jude the Obscure).'
  },
  {
    slug: 'modern-indian-english-writers',
    numStr: '#3.6',
    secIdx: 3,
    secTitle: 'History of English Literature & Major Writers',
    title: 'Modern & Indian English Writing: T.S. Eliot, Tagore, R.K. Narayan, Mulk Raj Anand',
    shortTitle: 'Modern & Indian Writers',
    chkId: 'chk-english-3-6',
    coreFocus: 'Modernism in English literature: Fragmentation, disillusionment, stream of consciousness, T.S. Eliot: High Modernist poetry (The Waste Land 1922: 5 sections, mythic method; The Love Song of J. Alfred Prufrock; Objective Correlative, Dissociation of Sensibility), Rabindranath Tagore: Nobel Prize 1913 (Gitanjali, The Post Office, Gora), R.K. Narayan: Malgudi fiction (Swami and Friends, The Guide: Rajus transformation, The Bachelor of Arts), and Mulk Raj Anand: Social realism and progressive writing (Untouchable: Bakha, Coolie, Two Leaves and a Bud).'
  },

  // ==================== Module 4: Reading Comprehension (2 Topics) ====================
  {
    slug: 'unseen-prose-comprehension',
    numStr: '#4.1',
    secIdx: 4,
    secTitle: 'Reading Comprehension',
    title: 'Unseen Prose Passages: Analytical, Factual & Theme Comprehension',
    shortTitle: 'Unseen Prose Comprehension',
    chkId: 'chk-english-4-1',
    coreFocus: 'Techniques for tackling unseen prose passages under time pressure: Skimming for main idea vs scanning for specific factual details, Inference and tone deduction (Authors tone: objective, critical, humorous, satirical, didactic), Title selection strategies, Contextual vocabulary questions (deducing word meaning from surrounding context), Question-first vs Passage-first reading strategy, and 5 model solved passages reflecting UP teacher exam standards.'
  },
  {
    slug: 'unseen-poetry-comprehension',
    numStr: '#4.2',
    secIdx: 4,
    secTitle: 'Reading Comprehension',
    title: 'Unseen Poetry Comprehension: Stanzas, Rhyme Schemes & Poetic Devices',
    shortTitle: 'Unseen Poetry Comprehension',
    chkId: 'chk-english-4-2',
    coreFocus: 'Methods for analyzing unseen poetic stanzas: Unpacking poetic inverted syntax and paraphrasing, Identifying central theme and mood/tone, Rhyme scheme calculation (e.g., abab, aabb), Figures of Speech and Poetic devices (Simile, Metaphor, Personification, Alliteration, Onomatopoeia, Hyperbole, Oxymoron, Irony, Apostrophe, Synecdoche, Metonymy), Imagery and symbolism, and 5 model solved poetry comprehension sets with complete explanations.'
  }
];

// 5. Prompt Engineering for English Language & Literature Content Generation
function buildEnglishPrompt(topic) {
  return `
You are India's top English Literature & Grammar Professor and Master Educator specializing in the UP Upper Primary Assistant Teacher (Class 6-8 / Super TET Junior) Examination.
Generate an exhaustive, topper-grade, highly structured, 100% comprehensive study module in ENGLISH (with helpful Hindi explanatory hints where appropriate for UP candidates) for:

TOPIC SLUG: "${topic.slug}"
TOPIC NUMBER: "${topic.numStr}"
MODULE: "${topic.secTitle}"
TOPIC TITLE: "${topic.title}"
CORE SYLLABUS FOCUS: "${topic.coreFocus}"

Target Audience: UP Upper Primary Assistant Teacher (Class 6-8) Recruitment Aspirants (English Language & Literature: 90 Questions | 270 Marks | -1 Negative Marking).
Strict standards:
1. Every concept must be pointwise, exhaustive, with exact grammar rules, formulaic structures, examples, literature facts, dates, quotations, and common competitive traps.
2. Provide a concept flow Mindmap (4 to 6 branches, each with 4 to 5 concise subnodes).
3. 4 comprehensive concept sections using HTML point-grid with point-cards, tip-box, trick-box, and mnemonic-inline-box.
4. Comparative matrix table with 4 columns and 5-6 rows highlighting exam distinctions.
5. Exactly 10 authentic, exam-level Multiple Choice Questions (MCQs) with 4 options, 0-indexed correct_index, and detailed explanations that teach.
6. 10 high-yield revision facts.
7. 3 memory mnemonics (acronyms, rhymes, or association rules).
8. 3 exam traps highlighting where students lose marks due to negative marking (-1).
9. 3 self-assessment mastery checklist points.

Respond ONLY with a VALID JSON object adhering to this EXACT schema (NO markdown backticks outside, no preamble, no postscript):
{
  "key_focus_summary": "2-3 crisp sentences detailing exam weightage, question trends, and high-scoring strategy for this English topic.",
  "mindmap": {
    "central_node": "${topic.shortTitle}",
    "branches": [
      {
        "title": "Branch 1 Title",
        "icon": "fas fa-font",
        "nodes": ["Point A", "Point B", "Point C", "Point D"]
      },
      {
        "title": "Branch 2 Title",
        "icon": "fas fa-book",
        "nodes": ["Point A", "Point B", "Point C", "Point D"]
      },
      {
        "title": "Branch 3 Title",
        "icon": "fas fa-code-branch",
        "nodes": ["Point A", "Point B", "Point C", "Point D"]
      },
      {
        "title": "Branch 4 Title",
        "icon": "fas fa-bolt",
        "nodes": ["Point A", "Point B", "Point C", "Point D"]
      }
    ]
  },
  "concepts": [
    {
      "heading": "1. Core Rules, Theoretical Foundations & Structures",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>Fundamental Rule & Definition:</strong> ...detailed explanation with rules and formula...</div><div class=\\"point-card\\"><strong>Key Patterns & Structures:</strong> ...detailed structural breakdowns and examples...</div></div><div class=\\"tip-box\\"><strong><i class=\\"fas fa-lightbulb\\"></i> Exam Tip:</strong> ...high-yield observation...</div>"
    },
    {
      "heading": "2. Detailed Classifications, Usage Patterns & Examples",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>Major Categories & Types:</strong> ...comprehensive analysis of each category...</div><div class=\\"point-card\\"><strong>Standard Contextual Sentences:</strong> ...rich examples illustrating nuances...</div></div><div class=\\"trick-box\\"><strong><i class=\\"fas fa-magic\\"></i> Quick Identification Trick:</strong> ...5-second shortcut rule...</div>"
    },
    {
      "heading": "3. Exceptions, Confusing Pairs & Edge Cases",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>Crucial Exceptions:</strong> ...rules where standard patterns break down...</div><div class=\\"point-card\\"><strong>Commonly Confused Elements:</strong> ...side-by-side contrast of look-alike structures...</div></div><div class=\\"mnemonic-inline-box\\"><strong>Memory Formula:</strong> <code>...acronym/rule code...</code> ...brief explanation...</div>"
    },
    {
      "heading": "4. UP Teaching Exam Trends & High-Scoring Techniques",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>PYQ Trend Analysis:</strong> ...what UP teacher exams consistently ask...</div><div class=\\"point-card\\"><strong>Elimination & Speed Strategy:</strong> ...how to achieve 100% accuracy under negative marking...</div></div>"
    }
  ],
  "comparative_table": {
    "title": "Comparative Analysis & Key Distinctions",
    "headers": ["Category / Form", "Grammar Rule / Literary Feature", "Standard Examples", "Critical Exam Distinction"],
    "rows": [
      ["1. ...", "...", "...", "..."],
      ["2. ...", "...", "...", "..."],
      ["3. ...", "...", "...", "..."],
      ["4. ...", "...", "...", "..."],
      ["5. ...", "...", "...", "..."]
    ]
  },
  "mcqs": [
    {
      "question": "Standard UP Upper Primary Teacher exam-level question 1?",
      "options": [
        "A) Option 1",
        "B) Option 2",
        "C) Option 3",
        "D) Option 4"
      ],
      "correct_index": 0,
      "explanation": "Detailed pedagogical explanation referencing grammatical rules or literary context so students learn multiple related facts."
    }
  ],
  "revision_facts": [
    "High-Yield Fact 1: ...",
    "High-Yield Fact 2: ...",
    "High-Yield Fact 3: ...",
    "High-Yield Fact 4: ...",
    "High-Yield Fact 5: ...",
    "High-Yield Fact 6: ...",
    "High-Yield Fact 7: ...",
    "High-Yield Fact 8: ...",
    "High-Yield Fact 9: ...",
    "High-Yield Fact 10: ..."
  ],
  "mnemonics": [
    {
      "title": "Mnemonic Rule 1",
      "quote": "Acronym or Catchy Memory Rhyme",
      "explanation": "How to apply this mnemonic in the exam hall."
    },
    {
      "title": "Mnemonic Rule 2",
      "quote": "Shortcut Elimination Code",
      "explanation": "How to discard 2 options instantly."
    },
    {
      "title": "Mnemonic Rule 3",
      "quote": "Exception Recall Formula",
      "explanation": "Remembering irregulars and edge cases easily."
    }
  ],
  "exam_traps": [
    {
      "title": "Exam Trap 1: The Most Common False Friend Trap",
      "description": "Why 75% of candidates pick the wrong option and how to avoid it."
    },
    {
      "title": "Exam Trap 2: Subtle Agreement / Modifiers Pitfall",
      "description": "How the examiner hides the real subject or modifier to deceive candidates."
    },
    {
      "title": "Exam Trap 3: Overlooking Negative Phrasing or Exceptions",
      "description": "Not noticing words like 'except', 'incorrect', or tricky inverted structures."
    }
  ],
  "mastery_checklist": [
    "I have mastered all core rules, definitions, and formulas of this topic.",
    "I can accurately solve previous years UP teacher recruitment questions without second-guessing.",
    "I have reviewed all 10 practice MCQs and am completely alert to negative marking traps."
  ]
}
`.trim();
}

// 6. Page Rendering Engine (English Primary Mode, Common CSS/JS, No Footer, Dark Mode Ready)
function renderEnglishPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}/up-upper-primary-teacher/english/${topic.slug}/`;
  const pageTitle = `${topic.title} Notes, Rules, Mindmap & MCQs | UP Junior Super TET English | SJMaths`;
  const metaDesc = `UP Upper Primary Assistant Teacher 2026 English: Comprehensive notes, concept mindmap, comparison table, mnemonics, 10 practice MCQs & timed mini-quiz for ${topic.title}.`;

  const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  function cleanOptionText(opt) {
    if (!opt) return '';
    return String(opt).replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '').trim();
  }

  // Render Mindmap
  let mindmapHtml = '';
  if (data.mindmap && data.mindmap.branches && data.mindmap.branches.length > 0) {
    let branchesHtml = '';
    data.mindmap.branches.forEach((b) => {
      let subnodesHtml = (b.nodes || []).map(n => `<li class="mindmap-subnode-item"><i class="fas fa-angle-right" style="color: var(--brand-emerald); margin-right: 0.35rem;"></i>${esc(n)}</li>`).join('');
      branchesHtml += `
            <div class="mindmap-branch-card">
                <div class="mindmap-branch-title">
                    <i class="${esc(b.icon || 'fas fa-circle-dot')}" style="color: var(--brand-emerald);"></i>
                    <span>${esc(b.title)}</span>
                </div>
                <ul class="mindmap-subnodes">
                    ${subnodesHtml}
                </ul>
            </div>`;
    });

    mindmapHtml = `
        <div class="prep-card">
            <h2>
                <i class="fas fa-sitemap" style="color: var(--brand-emerald);"></i>
                <span>Concept Flow Mindmap (${esc(data.mindmap.central_node || topic.shortTitle)})</span>
            </h2>
            <div class="mindmap-wrapper">
                <div class="mindmap-root-node">
                    <span class="mindmap-root-badge">
                        <i class="fas fa-graduation-cap"></i>
                        <span>${esc(data.mindmap.central_node || topic.shortTitle)}</span>
                    </span>
                </div>
                <div class="mindmap-branches">
                    ${branchesHtml}
                </div>
            </div>
        </div>`;
  }

  // Render Concepts
  let conceptsHtml = '';
  (data.concepts || []).forEach(c => {
    conceptsHtml += `
        <div class="prep-card">
            <h2>
                <i class="fas fa-bookmark" style="color: var(--brand-emerald);"></i>
                <span>${esc(c.heading)}</span>
            </h2>
            <div class="topic-content-body">
                ${c.html_content || ''}
            </div>
        </div>`;
  });

  // Render Comparative Table
  let compTableHtml = '';
  if (data.comparative_table && data.comparative_table.headers && data.comparative_table.rows) {
    const tableData = data.comparative_table;
    const ths = tableData.headers.map(h => `<th>${esc(h)}</th>`).join('');
    const trs = tableData.rows.map(row => {
      const tds = (Array.isArray(row) ? row : Object.values(row)).map(c => `<td>${esc(c)}</td>`).join('');
      return `<tr>${tds}</tr>`;
    }).join('');

    compTableHtml = `
        <div class="prep-card">
            <h2>
                <i class="fas fa-table-columns" style="color: var(--brand-emerald);"></i>
                <span>${esc(tableData.title || 'Comparative Matrix & Exam Distinctions')}</span>
            </h2>
            <div class="table-scroll-wrapper">
                <table class="prep-table">
                    <thead>
                        <tr>${ths}</tr>
                    </thead>
                    <tbody>
                        ${trs}
                    </tbody>
                </table>
            </div>
        </div>`;
  }

  // Render Practice Questions (10 MCQs)
  let mcqsHtml = '';
  (data.mcqs || []).forEach((q, idx) => {
    let optionsListHtml = '';
    (q.options || []).forEach((opt, optIdx) => {
      const letter = ['A', 'B', 'C', 'D'][optIdx];
      const isCorrect = optIdx === q.correct_index;
      const cleaned = cleanOptionText(opt);
      optionsListHtml += `
            <button type="button" class="mcq-option-btn" data-correct="${isCorrect ? 'true' : 'false'}" onclick="handleMcqOptionClick(this, ${idx})">
                <span class="opt-label">${letter}</span>
                <span>${esc(cleaned)}</span>
            </button>`;
    });

    mcqsHtml += `
        <div class="mcq-item-card" id="mcq-card-${idx}">
            <div class="mcq-header-meta">
                <span class="mcq-q-pill">Question ${idx + 1} / ${data.mcqs.length}</span>
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> UP Super TET Junior English</span>
            </div>
            <div class="mcq-question-text">${esc(q.question)}</div>
            <div class="mcq-options-group">
                ${optionsListHtml}
            </div>
            <div class="mcq-explanation-box" id="mcq-exp-${idx}">
                <div class="exp-badge" style="color: var(--brand-emerald);"><i class="fas fa-check-circle"></i> Detailed Explanation &amp; Rule:</div>
                <div style="font-size: 0.95rem; line-height: 1.65; color: var(--text-sub);">${esc(q.explanation)}</div>
            </div>
        </div>`;
  });

  // Prepare testData for interactive mini test
  const testDataJson = JSON.stringify((data.mcqs || []).map(q => ({
    question: q.question,
    question_hi: q.question,
    options: (q.options || []).map(cleanOptionText),
    options_hi: (q.options || []).map(cleanOptionText),
    correct_index: q.correct_index,
    explanation: q.explanation,
    explanation_hi: q.explanation
  })));

  // Render Revision Facts
  let factsHtml = '';
  (data.revision_facts || []).forEach((f, fIdx) => {
    factsHtml += `
            <div class="revision-fact-row">
                <span class="fact-num-badge">#${fIdx + 1}</span>
                <span>${esc(f)}</span>
            </div>`;
  });

  // Render Mnemonics
  let mnemonicsHtml = '';
  (data.mnemonics || []).forEach(m => {
    mnemonicsHtml += `
            <div class="mnemonic-card">
                <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--text-headline); margin: 0 0 0.5rem 0;">
                    <i class="fas fa-lightbulb" style="color: var(--brand-emerald);"></i> ${esc(m.title)}
                </h3>
                <div class="mnemonic-quote-box">${esc(m.quote)}</div>
                <p style="margin: 0; font-size: 0.9rem; color: var(--text-sub); line-height: 1.6;">${esc(m.explanation)}</p>
            </div>`;
  });

  // Render Exam Traps
  let trapsHtml = '';
  (data.exam_traps || []).forEach(tr => {
    trapsHtml += `
            <div class="trap-card-item">
                <i class="fas fa-triangle-exclamation" style="font-size: 1.25rem; flex-shrink: 0; margin-top: 2px;"></i>
                <div>
                    <strong style="display: block; font-size: 0.98rem; margin-bottom: 0.25rem;">${esc(tr.title)}</strong>
                    <span>${esc(tr.description)}</span>
                </div>
            </div>`;
  });

  // Render Self-Assessment Checklist
  let checklistHtml = '';
  (data.mastery_checklist || []).forEach((item, cIdx) => {
    checklistHtml += `
        <label class="mastery-check-item">
            <input type="checkbox" id="chk-mastery-${cIdx}" class="custom-check" onchange="updateMasteryProgress()">
            <span>${esc(item)}</span>
        </label>`;
  });

  // Navigation Links
  const prevLink = prevTopic
    ? `<a href="/up-upper-primary-teacher/english/${prevTopic.slug}/" class="topic-nav-btn prev-btn"><i class="fas fa-chevron-left"></i> <span>Previous: ${esc(prevTopic.shortTitle)}</span></a>`
    : `<span class="topic-nav-btn prev-btn disabled"><i class="fas fa-chevron-left"></i> <span>First Topic</span></span>`;

  const nextLink = nextTopic
    ? `<a href="/up-upper-primary-teacher/english/${nextTopic.slug}/" class="topic-nav-btn next-btn"><span>Next: ${esc(nextTopic.shortTitle)}</span> <i class="fas fa-chevron-right"></i></a>`
    : `<span class="topic-nav-btn next-btn disabled"><span>Last Topic</span> <i class="fas fa-chevron-right"></i></span>`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${esc(pageTitle)}</title>
<meta content="${esc(topic.title)}, English Language & Literature, UP Upper Primary Teacher, Class 6-8 Teacher Syllabus, Super TET Junior Notes, UP Assistant Teacher, SJMaths" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="${esc(metaDesc)}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="${canonicalUrl}" rel="canonical"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Open Graph -->
<meta property="og:title" content="${esc(pageTitle)}"/>
<meta content="${esc(metaDesc)}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="${canonicalUrl}" property="og:url"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" property="og:image"/>

<!-- Twitter Card -->
<meta content="summary_large_image" name="twitter:card"/>
<meta content="${esc(pageTitle)}" name="twitter:title"/>
<meta content="${esc(metaDesc)}" name="twitter:description"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" name="twitter:image"/>

<!-- Fonts and Icons -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
<link as="style" crossorigin="anonymous" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript>
<link href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" rel="stylesheet"/>
</noscript>

<!-- Stylesheets (Common Asset Architecture) -->
<link href="/assets/css/main.min.css?v=a3faaea0" rel="stylesheet"/>
<link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
<link href="/assets/css/component.min.css?v=3fce8e36" rel="stylesheet"/>
<link href="/assets/css/improved-ui.min.css?v=dd2cffe9" rel="stylesheet"/>
<link href="/assets/css/pages.min.css?v=9e3bd560" rel="stylesheet"/>
<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>

<!-- Language Mode Enforcement: English Only -->
<style>
    .lang-en { display: inline !important; }
    .lang-hi { display: none !important; }
</style>

<!-- Breadcrumb Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://sjmaths.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "UP Upper Primary Teacher",
      "item": "https://sjmaths.com/up-upper-primary-teacher/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "English",
      "item": "https://sjmaths.com/up-upper-primary-teacher/english/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "${esc(topic.shortTitle)}",
      "item": "${canonicalUrl}"
    }
  ]
}
</script>

<!-- Theme & Palette Sync Script (Light / Dark Mode Persistence matching Homepage) -->
<script>
    (function () {
        const sjDark = localStorage.getItem('sjmaths-dark');
        const legacyTheme = localStorage.getItem('theme');
        const isDark = sjDark === 'on' || (sjDark === null && legacyTheme === 'dark') || (sjDark === null && legacyTheme === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
            document.documentElement.classList.add('dark-mode');
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark-mode');
            document.documentElement.setAttribute('data-theme', 'light');
        }
        const savedTheme = localStorage.getItem('sjmaths-theme');
        const themePalettes = {
            green: { primary: '#059669', 'primary-dark': '#047857', 'primary-light': '#ecfdf5' },
            blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#eff6ff' },
            purple: { primary: '#7c3aed', 'primary-dark': '#6d28d9', 'primary-light': '#f5f3ff' },
            orange: { primary: '#ea580c', 'primary-dark': '#c2410c', 'primary-light': '#fff7ed' }
        };
        if (savedTheme && themePalettes[savedTheme]) {
            Object.entries(themePalettes[savedTheme]).forEach(([k, v]) => {
                document.documentElement.style.setProperty('--brand-' + k, v);
            });
        }
    })();
</script>
</head>

<body class="lang-mode-en">
<script>
    (function () {
        const sjDark = localStorage.getItem('sjmaths-dark');
        const legacyTheme = localStorage.getItem('theme');
        const isDark = sjDark === 'on' || (sjDark === null && legacyTheme === 'dark') || (sjDark === null && legacyTheme === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    })();
</script>
<div id="header-container"></div>

<main class="topic-page-container">

    <!-- Top Action Bar -->
    <div class="top-action-bar">
        <div class="breadcrumb-trail">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/">UP Teacher Exam</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/english/">English Syllabus</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>${esc(topic.numStr)}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
            <a href="/up-upper-primary-teacher/english/" class="back-hub-btn">
                <i class="fas fa-arrow-left"></i>
                <span>English Syllabus Hub</span>
            </a>
            <a href="/up-upper-primary-teacher/" class="back-hub-btn">
                <i class="fas fa-th-large"></i>
                <span>All Subjects Hub</span>
            </a>
        </div>
    </div>

    <!-- Topic Hero Panel -->
    <div class="topic-hero-panel">
        <div class="topic-meta-row">
            <span class="topic-badge-pill">${esc(topic.numStr)} Core Syllabus</span>
            <span class="subject-tag-pill">Module ${topic.secIdx}: ${esc(topic.secTitle)}</span>
            <span class="subject-tag-pill">Class 6–8 Teacher</span>
        </div>
        <h1>
            <span>${esc(topic.title)}</span>
        </h1>
        <div class="topic-hero-subtitle">
            <span>UP Upper Primary Assistant Teacher Recruitment Examination 2026 (Super TET Junior)</span>
        </div>
        <p class="lead-desc">
            <span>${esc(data.key_focus_summary || topic.coreFocus)}</span>
        </p>
    </div>

    <!-- Live Completion Toggle -->
    <div class="completion-card">
        <div class="completion-card-left">
            <i class="fas fa-tasks" style="font-size: 1.5rem; color: var(--brand-emerald);"></i>
            <div>
                <strong style="font-size: 1rem; color: var(--text-headline);">
                    <span>Preparation Status</span>
                </strong>
                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: var(--text-muted);" id="statusDesc">
                    <span>Mark as completed once studied. Progress automatically synchronizes with the main English preparation hub.</span>
                </p>
            </div>
        </div>
        <button id="topicCompletionBtn" class="toggle-topic-btn" onclick="toggleTopicStatus()">
            <i class="fas fa-check-circle"></i>
            <span id="completionBtnText">Mark Complete</span>
        </button>
    </div>

    <!-- Study Tabs Strip -->
    <div class="study-tabs-strip" role="tablist">
        <button class="study-tab-btn active" data-tab="concepts">
            <i class="fas fa-book-open"></i>
            <span>1. Concepts &amp; Rules</span>
        </button>
        <button class="study-tab-btn" data-tab="practice">
            <i class="fas fa-list-check"></i>
            <span>2. Practice Questions (10 MCQs)</span>
        </button>
        <button class="study-tab-btn" data-tab="test">
            <i class="fas fa-stopwatch"></i>
            <span>3. Mini Test (5 Mins)</span>
        </button>
        <button class="study-tab-btn" data-tab="revision">
            <i class="fas fa-redo"></i>
            <span>4. Quick Recap &amp; Exam Traps</span>
        </button>
    </div>

    <!-- ==================== TAB 1: CONCEPTS & THEORY ==================== -->
    <div class="study-tab-pane active" id="tab-concepts">
        <div class="strategy-banner-box">
            <p style="margin: 0; font-size: 0.95rem; color: var(--text-headline); line-height: 1.6;">
                <i class="fas fa-compass" style="color: var(--brand-emerald); margin-right: 0.4rem;"></i>
                <strong>Syllabus Focus &amp; High-Scoring Strategy:</strong>
                <span>${esc(topic.coreFocus)}</span>
            </p>
        </div>

        <!-- Mindmap Component -->
        ${mindmapHtml}

        <!-- 4 Core Concepts -->
        ${conceptsHtml}

        <!-- Comparative Matrix Table -->
        ${compTableHtml}
    </div>

    <!-- ==================== TAB 2: PRACTICE QUESTIONS ==================== -->
    <div class="study-tab-pane" id="tab-practice">
        <div class="practice-summary-bar">
            <div>
                <strong style="color: var(--text-headline); font-size: 1.05rem;">Exam-Standard Practice MCQs (10 Questions)</strong>
                <p style="margin: 3px 0 0 0; font-size: 0.85rem; color: var(--text-muted);">Solve UP teacher recruitment pattern questions with instant feedback and pedagogical explanations.</p>
            </div>
            <div class="practice-score-badge" id="practiceScoreDisplay">Score: 0 / ${data.mcqs.length}</div>
        </div>

        ${mcqsHtml}
    </div>

    <!-- ==================== TAB 3: TIMED MINI TEST ==================== -->
    <div class="study-tab-pane" id="tab-test">
        <div class="prep-card">
            <div id="testIntroScreen" class="mini-test-intro">
                <i class="fas fa-stopwatch" style="font-size: 3rem; color: var(--brand-emerald); margin-bottom: 1rem;"></i>
                <h2 style="justify-content: center; border: none; margin-bottom: 0.5rem;">English Speed &amp; Accuracy Mini Test</h2>
                <p class="test-desc">This is a 5-minute timed test featuring 10 multiple-choice questions reflecting the exact UP Upper Primary Assistant Teacher marking scheme (+3 for correct, -1 for incorrect).</p>
                <div class="test-stats-row">
                    <span class="test-stat-chip"><i class="fas fa-question-circle"></i> Questions: 10</span>
                    <span class="test-stat-chip"><i class="fas fa-clock"></i> Time: 5 Minutes (300s)</span>
                    <span class="test-stat-chip"><i class="fas fa-award"></i> Total: 30 Marks</span>
                    <span class="test-stat-chip"><i class="fas fa-minus-circle" style="color: #dc2626;"></i> Negative Marking: -1</span>
                </div>
                <button type="button" class="start-test-btn" onclick="startMiniTest()">
                    <i class="fas fa-play"></i>
                    <span>Start Mini Test</span>
                </button>
            </div>

            <div id="testActiveScreen" style="display: none;">
                <div class="test-timer-bar">
                    <div>
                        <span style="font-size: 0.85rem; color: var(--text-muted);">Time Remaining</span>
                        <div class="test-countdown" id="testTimerText"><i class="fas fa-clock"></i> 05:00</div>
                    </div>
                    <button type="button" class="test-submit-btn" onclick="submitMiniTest()">
                        <i class="fas fa-paper-plane"></i>
                        <span>Submit Test</span>
                    </button>
                </div>

                <div id="testQuestionsContainer"></div>

                <div class="test-nav-controls">
                    <button type="button" class="test-btn-nav" id="btnPrevTestQ" onclick="navigateTestQuestion(-1)">
                        <i class="fas fa-chevron-left"></i> Previous Question
                    </button>
                    <span id="testQIndexIndicator" style="font-weight: 700; color: var(--text-sub);">1 / 10</span>
                    <button type="button" class="test-btn-nav" id="btnNextTestQ" onclick="navigateTestQuestion(1)">
                        Next Question <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
            </div>

            <div id="testResultScreen" style="display: none; text-align: center; padding: 2rem 1rem;">
                <i class="fas fa-trophy" style="font-size: 3.5rem; color: #f59e0b; margin-bottom: 1rem;"></i>
                <h2 style="justify-content: center; border: none; margin-bottom: 0.5rem;">Test Performance Scorecard</h2>
                <div style="font-size: 2.5rem; font-weight: 900; color: var(--brand-emerald); margin-bottom: 0.5rem;" id="finalScoreVal">0 / 30</div>
                <p id="testAccuracySummary" style="font-size: 1rem; color: var(--text-sub); margin-bottom: 1.5rem;"></p>
                <div id="testDetailedBreakdown" style="text-align: left; margin-top: 2rem;"></div>
                <button type="button" class="retry-test-btn" onclick="restartMiniTest()" style="margin-top: 1.5rem;">
                    <i class="fas fa-redo"></i> Retake Test
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 4: REVISION & EXAM TRAPS ==================== -->
    <div class="study-tab-pane" id="tab-revision">
        <div class="prep-card">
            <h2>
                <i class="fas fa-bolt" style="color: #f59e0b;"></i>
                <span>High-Yield Revision Points (10 Exam Facts)</span>
            </h2>
            <div class="revision-facts-grid">
                ${factsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-brain" style="color: var(--brand-indigo);"></i>
                <span>Memory Mnemonics &amp; Retention Vault</span>
            </h2>
            ${mnemonicsHtml}
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-triangle-exclamation" style="color: #dc2626;"></i>
                <span>Common Exam Traps &amp; Negative Marking Safeguards (-1 Penalty)</span>
            </h2>
            <div class="traps-container">
                ${trapsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-circle-check" style="color: var(--brand-emerald);"></i>
                <span>Self-Assessment Checklist</span>
            </h2>
            <div class="topic-mastery-checklist">
                ${checklistHtml}
            </div>
        </div>
    </div>

    <!-- Bottom Sequential Navigation -->
    <div class="bottom-topic-nav">
        ${prevLink}
        ${nextLink}
    </div>

</main>

<button aria-label="Back to Top" class="back-to-top-btn" id="backToTopBtn">
    <i class="fas fa-arrow-up"></i>
</button>

<!-- Interactive Logic & Shared Runtime Engine -->
<script>
    window.TOPIC_STORAGE_KEY = 'up-upper-primary-teacher-checklist-v2';
    window.TOPIC_CHECKBOX_ID = '${topic.chkId}';
    window.testData = ${testDataJson};
</script>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js?v=20261002_02"></script>
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=1594eda0"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=d48c181a"></script>
<script src="/assets/js/require-auth.min.js?v=3060658c" type="module"></script>
</body>
</html>
`;
}

// 7. Generation Orchestrator
async function generateEnglishTopicContent(topic) {
  const prompt = buildEnglishPrompt(topic);
  let lastErr = null;

  for (let attempt = 0; attempt < 8; attempt++) {
    const config = getActiveConfig();
    const ai = new GoogleGenAI({ apiKey: config.key });

    for (const model of config.models) {
      try {
        console.log(`    [Attempt ${attempt + 1}] Invoking Gemini API [${config.name} | ${model}] for: ${topic.slug}`);
        const response = await ai.models.generateContent({
          model,
          contents: prompt,
          config: {
            responseMimeType: 'application/json',
            temperature: 0.3
          }
        });

        const rawText = response.text;
        if (!rawText) throw new Error('Empty response received from model');

        let parsed;
        try {
          parsed = JSON.parse(rawText);
        } catch (e) {
          const repaired = jsonrepair(rawText);
          parsed = JSON.parse(repaired);
        }

        // Validate critical keys
        if (!parsed.concepts || !parsed.mcqs || parsed.mcqs.length < 5) {
          throw new Error(`Incomplete JSON payload (concepts: ${parsed.concepts?.length}, mcqs: ${parsed.mcqs?.length})`);
        }

        return parsed;
      } catch (err) {
        lastErr = err;
        console.warn(`    [Warning] ${config.name}/${model} failed on ${topic.slug}: ${err.message}`);
        // If rate limited or unavailable, wait briefly
        await new Promise(r => setTimeout(r, 1500));
      }
    }

    rotateKey();
    await new Promise(r => setTimeout(r, 2000));
  }

  throw new Error(`Exhausted all retries for topic: ${topic.slug}. Last error: ${lastErr?.message}`);
}

async function main() {
  console.log('================================================================');
  console.log('SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) English');
  console.log(`Starting English Syllabus Content Generator Engine`);
  console.log(`Total Topics Cataloged: ${ENGLISH_TOPICS.length}`);
  console.log(`Active API Keys: ${KEY_CONFIGS.length} (${KEY_CONFIGS.map(k => k.name).join(', ')})`);
  console.log('================================================================\n');

  let targets = ENGLISH_TOPICS;

  if (TARGET_SLUG) {
    targets = ENGLISH_TOPICS.filter(t => t.slug === TARGET_SLUG);
    if (targets.length === 0) {
      console.error(`ERROR: Target topic slug "${TARGET_SLUG}" not found in catalog.`);
      process.exit(1);
    }
  } else if (LIMIT) {
    targets = targets.slice(0, LIMIT);
  }

  let generatedCount = 0;
  let skippedCount = 0;

  const pendingTasks = [];
  for (let i = 0; i < targets.length; i++) {
    const topic = targets[i];
    const prevTopic = i > 0 ? targets[i - 1] : null;
    const nextTopic = i < targets.length - 1 ? targets[i + 1] : null;

    const topicDir = path.join(OUTPUT_DIR, topic.slug);
    const topicFile = path.join(topicDir, 'index.html');

    if (!FORCE && statusMap[topic.slug] && statusMap[topic.slug].status === 'completed' && fs.existsSync(topicFile)) {
      console.log(`[SKIP] Already completed: ${topic.slug}`);
      skippedCount++;
      continue;
    }

    pendingTasks.push({ topic, prevTopic, nextTopic, index: i, total: targets.length });
  }

  console.log(`\nPending to generate: ${pendingTasks.length} topics (Concurrency: ${CONCURRENCY})\n`);

  if (DRY_RUN) {
    pendingTasks.forEach(t => console.log(`  [DRY-RUN] Would generate: ${t.topic.slug}`));
    return;
  }

async function safeWriteFile(filePath, content, retries = 5) {
  const tempPath = `${filePath}.tmp.${Date.now()}`;
  for (let i = 0; i < retries; i++) {
    try {
      fs.writeFileSync(tempPath, content, 'utf8');
      if (fs.existsSync(filePath)) {
        try { fs.unlinkSync(filePath); } catch (e) {}
      }
      fs.copyFileSync(tempPath, filePath);
      try { fs.unlinkSync(tempPath); } catch (e) {}
      return;
    } catch (err) {
      try { if (fs.existsSync(tempPath)) fs.unlinkSync(tempPath); } catch (e) {}
      if (i === retries - 1) throw err;
      await new Promise(r => setTimeout(r, 600 * (i + 1)));
    }
  }
}

  let taskPointer = 0;
  async function worker(workerId) {
    while (taskPointer < pendingTasks.length) {
      const currentTask = pendingTasks[taskPointer++];
      const { topic, prevTopic, nextTopic, index, total } = currentTask;
      const topicDir = path.join(OUTPUT_DIR, topic.slug);
      const topicFile = path.join(topicDir, 'index.html');

      console.log(`[Worker ${workerId}][${index + 1}/${total}] Starting: ${topic.slug} (${topic.title.slice(0, 50)}...)`);

      try {
        const data = await generateEnglishTopicContent(topic);
        const html = renderEnglishPage(topic, data, prevTopic, nextTopic);

        if (!fs.existsSync(topicDir)) {
          fs.mkdirSync(topicDir, { recursive: true });
        }

        await safeWriteFile(topicFile, html, 5);

        statusMap[topic.slug] = {
          status: 'completed',
          timestamp: new Date().toISOString(),
          sizeBytes: html.length,
          title: topic.title,
          secIdx: topic.secIdx,
          chkId: topic.chkId
        };
        saveStatus();

        generatedCount++;
        console.log(`[Worker ${workerId}]  ✓ SUCCESS: Generated ${topic.slug} (${Math.round(html.length / 1024)} KB)`);

        await new Promise(r => setTimeout(r, 1000));
      } catch (err) {
        console.error(`[Worker ${workerId}]  ✗ FAILED: ${topic.slug} -> ${err.message}`);
        statusMap[topic.slug] = {
          status: 'failed',
          timestamp: new Date().toISOString(),
          error: err.message
        };
        saveStatus();
      }
    }
  }

  const pool = Array.from({ length: Math.min(CONCURRENCY, pendingTasks.length) }, (_, id) => worker(id + 1));
  await Promise.all(pool);

  console.log(`\n================================================================`);
  console.log(`Batch Summary:`);
  console.log(`  - Successfully Generated: ${generatedCount}`);
  console.log(`  - Skipped (Existing):     ${skippedCount}`);
  console.log(`  - Total Processed:        ${targets.length}`);
  console.log(`================================================================`);
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
