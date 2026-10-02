#!/usr/bin/env node
/**
 * ============================================================================
 * Clean & Refine UP Upper Primary Teacher Content
 * Removes formulaic AI boilerplate, redundant numbering prefixes, prompt artifacts,
 * and awkward phrasing across English and Sanskrit topic pages.
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const ENGLISH_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'english');
const SANSKRIT_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'sanskrit');

// Human-crafted, authoritative lead descriptions for the 24 English topics
const ENGLISH_LEAD_DESCS = {
  'parts-of-speech-nouns-pronouns': 'Comprehensive study notes on noun classifications (proper, common, collective, abstract, material), countable and uncountable distinctions, pluralization rules, case syntax, pronoun types, and antecedent agreement.',
  'verbs-modals-auxiliary': 'Essential grammar notes covering transitive and intransitive verbs, primary and modal auxiliaries, semi-modals, non-finites (to-infinitives, bare infinitives, gerunds, participles), and participle clause syntax.',
  'adjectives-adverbs-degrees': 'Clear rules and practical patterns for qualitative and quantitative adjectives, degrees of comparison, OSASCOMP ordering, adverb classifications, position rules, and negative adverb inversions.',
  'tenses': 'Structured breakdown of all 12 tense aspect forms across present, past, and future, including time marker adverbials, stative verb restrictions, conditional sentences (Types 0-3), and sequence of tenses.',
  'active-passive': 'Transformation principles for active and passive voice across all tenses, subject-object interchange, imperative commands and requests, interrogative sentences, prepositional passives, and the four non-passivizable tenses.',
  'direct-indirect': 'Complete narration guide covering reporting verb changes, backshift of tenses, universal truth exceptions, pronoun shifts using the SON formula, and indirect conversions for statements, questions, and imperatives.',
  'subject-verb': 'Standard concord and agreement rules, compound subjects with coordinating and correlative conjunctions, indefinite pronouns, collective noun usage, and quantification expressions.',
  'articles': 'Systematic rules for indefinite articles (a, an) based on phonetic vowel sounds, definitive article (the) usages with proper nouns and superlatives, zero article omissions, and quantifiers (few/little).',
  'prepositions': 'Comprehensive prepositions of time, place, and motion, spatial relationships, high-yield fixed preposition combinations, and essential phrasal verbs.',
  'conjunctions': 'Detailed guide to coordinating (FANBOYS), subordinating, and correlative conjunctions, clause identification (noun, adjective, adverb), and sentence synthesis into simple, compound, and complex forms.',
  'error-spotting': 'Diagnostic framework for sentence correction: subject-verb discord, pronoun case errors, misplaced and dangling modifiers, faulty parallelism, redundancy, and tense sequence mismatches.',
  'punctuation-question-tags': 'Standard punctuation conventions (commas, semicolons, colons, apostrophes), capitalization rules, and question tag syntax covering positive-negative shifts, auxiliary verbs, and exceptions.',
  'vocabulary-synonyms-antonyms': 'High-frequency competitive vocabulary roots (Latin and Greek prefixes/suffixes), contextual synonyms and antonyms, tone elimination strategies, and shades of word meanings.',
  'idioms-phrases-expressions': 'Categorized idioms and idiomatic phrases (animals, colors, body parts, conflict, daily life), literal versus figurative meanings, and contextual usage in exam sentences.',
  'one-word-substitution': 'Category-wise one word substitutions covering forms of government (-archy, -cracy), scientific studies (-ology), phobias, manias, killings (-cide), and personality traits.',
  'spellings-confusing-words': 'Fundamental English spelling rules (i before e, consonant doubling, silent e), high-frequency misspelled examination words, homophones, homonyms, and commonly confused word pairs.',
  'shakespeare-elizabethan-age': 'Literary history of the Elizabethan and Jacobean era: William Shakespeare, the University Wits, the Globe Theatre, 37 plays categorized by genre, and the 154 sonnets structural analysis.',
  'milton-restoration-age': 'Puritan and Restoration literature: John Milton (Paradise Lost, Areopagitica, Samson Agonistes, Lycidas), John Dryden, heroic couplets, and Restoration comedy of manners.',
  'neoclassical-augustan-age': 'The Augustan Age and Neoclassicism: Alexander Pope (The Rape of the Lock, An Essay on Criticism), Jonathan Swift (Gullivers Travels), Addison and Steele (The Spectator), and Dr. Samuel Johnson.',
  'romantic-age-poets': 'The Romantic Revival: 1798 Lyrical Ballads, William Wordsworths critical preface and nature poetry, S.T. Coleridge and supernaturalism, John Keats and negative capability, and P.B. Shelley.',
  'victorian-age-writers': 'Victorian literature: industrialization and social realism, Alfred Lord Tennyson, Robert Brownings dramatic monologues, Charles Dickenss novels, and Thomas Hardys Wessex fatalism.',
  'modern-indian-english-writers': 'Modernist poetry and fiction: T.S. Eliots The Waste Land and objective correlative, Rabindranath Tagores Gitanjali, R.K. Narayans Malgudi novels, and Mulk Raj Anands progressive realism.',
  'unseen-prose-comprehension': 'Reading comprehension strategies: skimming for central ideas, scanning for factual details, inferring authorial tone, vocabulary in context, and strategic time management.',
  'unseen-poetry-comprehension': 'Poetry comprehension analysis: paraphrasing poetic syntax, rhyme scheme calculation, figures of speech (simile, metaphor, personification, alliteration, oxymoron), and stanzaic structure.'
};

function cleanEnglishContent(content, slug) {
  let updated = content;

  // 1. Replace lead description if available
  if (ENGLISH_LEAD_DESCS[slug]) {
    updated = updated.replace(
      /<p class="lead-desc">\s*<span>[\s\S]*?<\/span>\s*<\/p>/,
      `<p class="lead-desc">\n            <span>${ENGLISH_LEAD_DESCS[slug]}</span>\n        </p>`
    );
  }

  // 2. Clean Tab 1 Strategy Banner label
  updated = updated.replace(
    /<strong>Syllabus Focus &amp; High-Scoring Strategy:<\/strong>/g,
    '<strong>Syllabus Scope:</strong>'
  );

  // 3. Clean Concept Section Headings
  updated = updated.replace(/<span>1\. Core Rules, Theoretical Foundations &amp; Structures<\/span>/g, '<span>1. Core Grammatical Rules &amp; Foundations</span>');
  updated = updated.replace(/<span>2\. Detailed Classifications, Usage Patterns &amp; Examples<\/span>/g, '<span>2. Classifications &amp; Practical Applications</span>');
  updated = updated.replace(/<span>3\. Exceptions, Confusing Pairs &amp; Edge Cases<\/span>/g, '<span>3. Key Exceptions &amp; Structural Nuances</span>');
  updated = updated.replace(/<span>4\. UP Teaching Exam Trends &amp; High-Scoring Techniques<\/span>/g, '<span>4. Exam Insights &amp; Question Analysis</span>');

  // Also handle literature-specific headings if any
  updated = updated.replace(/<span>1\. Core Historical Background, Milestones &amp; Framework<\/span>/g, '<span>1. Historical Background &amp; Literary Milestones</span>');
  updated = updated.replace(/<span>2\. Major Authors, Works, Characters &amp; Themes<\/span>/g, '<span>2. Major Authors, Works &amp; Character Analysis</span>');
  updated = updated.replace(/<span>3\. Stylistic Features, Literary Devices &amp; Quotes<\/span>/g, '<span>3. Stylistic Features, Devices &amp; Famous Quotations</span>');

  // 4. Remove redundant "High-Yield Fact X:" prefixes inside fact rows
  updated = updated.replace(/(<div class="revision-fact-row">\s*<span class="fact-num-badge">#\d+<\/span>\s*<span>)\s*High-Yield Fact \d+:\s*/gi, '$1');
  updated = updated.replace(/(<div class="revision-fact-row">\s*<span class="fact-num-badge">#\d+<\/span>\s*<span>)\s*Fact \d+:\s*/gi, '$1');

  // 5. Remove redundant "Mnemonic X:" prefixes inside mnemonic cards
  updated = updated.replace(/(<i class="fas fa-lightbulb"[^>]*><\/i>)\s*Mnemonic \d+:\s*/gi, '$1 ');
  updated = updated.replace(/(<i class="fas fa-lightbulb"[^>]*><\/i>)\s*Mnemonic Rule \d+:\s*/gi, '$1 ');

  // 6. Remove redundant "Exam Trap X:" prefixes inside trap cards
  updated = updated.replace(/(<strong[^>]*>)\s*Exam Trap \d+:\s*/gi, '$1');
  updated = updated.replace(/(<strong[^>]*>)\s*Trap \d+:\s*/gi, '$1');

  // 7. Remove parenthetical Hindi explanations/hints in English concept cards
  updated = updated.replace(/\s*\((?:हिंदी में|हिन्दी में|हिन्दी संकेत|हिंदी संकेत|हिन्दी|हिंदी):[^\)]+\)/g, '');

  // 8. Clean MCQ explanation badge
  updated = updated.replace(/Detailed Explanation &amp; Rule:/g, 'Explanation &amp; Grammar Rule:');

  // 9. Remove robotic meta-sentences inside point-cards
  updated = updated.replace(/In UP Teacher exams, changing voice must NEVER alter the core tense or meaning of the original sentence\./g, 'Changing voice must never alter the core tense or meaning of the original sentence.');
  updated = updated.replace(/Under negative marking \(-1 mark\), use the 'Tense &amp; Verb Agreement Scan'\./g, 'Apply the systematic three-step Tense and Verb Agreement Scan.');

  return updated;
}

function cleanSanskritContent(content) {
  let updated = content;

  // 1. Clean Tab 1 Strategy Banner label
  updated = updated.replace(
    /<strong>पाठ्यक्रम फोकस एवं उच्च अंक रणनीति:<\/strong>/g,
    '<strong>अध्याय का मुख्य विषय-क्षेत्र:</strong>'
  );

  // 2. Remove redundant "तथ्य X:" prefixes inside fact rows
  updated = updated.replace(/(<div class="revision-fact-row">\s*<span class="fact-num-badge">#\d+<\/span>\s*<span>)\s*तथ्य \d+:\s*/g, '$1');

  // 3. Remove redundant "स्मरण सूत्र X (...):" prefixes inside mnemonic cards
  updated = updated.replace(/(<i class="fas fa-lightbulb"[^>]*><\/i>)\s*स्मरण सूत्र \d+\s*(?:\([^)]*\))?:\s*/g, '$1 ');

  // 4. Remove redundant "परीक्षा जाल X:" prefixes inside trap cards
  updated = updated.replace(/(<strong[^>]*>)\s*परीक्षा जाल \d+:\s*/g, '$1');

  // 5. Clean explanation badge
  updated = updated.replace(/सटीक व्याख्या एवं विश्लेषण:/g, 'व्याख्या एवं शास्त्रीय नियम:');

  return updated;
}

function cleanGeneralKnowledgeAndSocialStudies(content) {
  let updated = content;

  // Remove "High-Yield Fact X:" if present
  updated = updated.replace(/(<div class="revision-fact-row">\s*<span class="fact-num-badge">#\d+<\/span>\s*<span>)\s*High-Yield Fact \d+:\s*/gi, '$1');
  updated = updated.replace(/(<div class="revision-fact-row">\s*<span class="fact-num-badge">#\d+<\/span>\s*<span>)\s*तथ्य \d+:\s*/g, '$1');

  // Remove "Exam Trap X:" if present
  updated = updated.replace(/(<strong[^>]*>)\s*Exam Trap \d+:\s*/gi, '$1');
  updated = updated.replace(/(<strong[^>]*>)\s*परीक्षा जाल \d+:\s*/g, '$1');

  // Remove "Mnemonic X:" if present
  updated = updated.replace(/(<i class="fas fa-lightbulb"[^>]*><\/i>)\s*Mnemonic \d+:\s*/gi, '$1 ');
  updated = updated.replace(/(<i class="fas fa-lightbulb"[^>]*><\/i>)\s*स्मरण सूत्र \d+\s*(?:\([^)]*\))?:\s*/g, '$1 ');

  return updated;
}

console.log('Cleaning English topics...');
let englishCount = 0;
if (fs.existsSync(ENGLISH_DIR)) {
  const dirs = fs.readdirSync(ENGLISH_DIR);
  for (const d of dirs) {
    const filePath = path.join(ENGLISH_DIR, d, 'index.html');
    if (!fs.existsSync(filePath)) continue;
    const original = fs.readFileSync(filePath, 'utf8');
    // skip redirect files
    if (original.includes('http-equiv="refresh"')) continue;

    const cleaned = cleanEnglishContent(original, d);
    if (cleaned !== original) {
      fs.writeFileSync(filePath, cleaned, 'utf8');
      englishCount++;
      console.log(`  ✓ Cleaned English topic: ${d}`);
    }
  }
}

console.log(`\nCleaning Sanskrit topics...`);
let sanskritCount = 0;
if (fs.existsSync(SANSKRIT_DIR)) {
  const dirs = fs.readdirSync(SANSKRIT_DIR);
  for (const d of dirs) {
    const filePath = path.join(SANSKRIT_DIR, d, 'index.html');
    if (!fs.existsSync(filePath)) continue;
    const original = fs.readFileSync(filePath, 'utf8');
    if (original.includes('http-equiv="refresh"')) continue;

    const cleaned = cleanSanskritContent(original);
    if (cleaned !== original) {
      fs.writeFileSync(filePath, cleaned, 'utf8');
      sanskritCount++;
      console.log(`  ✓ Cleaned Sanskrit topic: ${d}`);
    }
  }
}

console.log(`\nCleaning other subjects in up-upper-primary-teacher...`);
function walkAndCleanOtherSubjects(dir) {
  let cleanedCount = 0;
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      if (file !== 'english' && file !== 'sanskrit') {
        cleanedCount += walkAndCleanOtherSubjects(full);
      }
    } else if (file === 'index.html') {
      const original = fs.readFileSync(full, 'utf8');
      if (!original.includes('http-equiv="refresh"')) {
        const cleaned = cleanGeneralKnowledgeAndSocialStudies(original);
        if (cleaned !== original) {
          fs.writeFileSync(full, cleaned, 'utf8');
          cleanedCount++;
        }
      }
    }
  }
  return cleanedCount;
}

const otherCount = walkAndCleanOtherSubjects(path.join(ROOT, 'up-upper-primary-teacher'));

console.log(`\n================================================================`);
console.log(`Cleaned Summary:`);
console.log(`  - English Topics Refined:  ${englishCount}`);
console.log(`  - Sanskrit Topics Refined: ${sanskritCount}`);
console.log(`  - Other Topics Refined:    ${otherCount}`);
console.log(`================================================================\n`);
