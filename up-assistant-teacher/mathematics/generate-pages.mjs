#!/usr/bin/env node
/** Write manually authored English Mathematics Study tabs into their pages. */

import fs from 'node:fs';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { MATHEMATICS_PRACTICE, MATHEMATICS_STUDY } from './manual-study-content.mjs';

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SCRIPT_DIR, '../..');
const TRACKER_PATH = path.join(ROOT, 'up-assistant-teacher', 'index.html');
const GENERATOR_VERSION = 'manual-maths-study-v1';

function parseArgs(argv) {
  const options = { dryRun: false, force: false, limit: null, topic: null };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--dry-run') options.dryRun = true;
    else if (arg === '--force') options.force = true;
    else if (arg === '--topic') options.topic = argv[++i] || '';
    else if (arg === '--limit') options.limit = Number.parseInt(argv[++i], 10);
    else if (arg === '--help' || arg === '-h') options.help = true;
    else throw new Error('Unknown option: ' + arg);
  }
  if (options.limit !== null && (!Number.isInteger(options.limit) || options.limit < 1)) throw new Error('--limit must be a positive integer.');
  return options;
}

function usage() {
  return [
    'Generate English-only Mathematics Study tabs from manually authored content. No API key or network access is used.',
    '',
    '  npm run generate:up-assistant-mathematics -- [--dry-run] [--topic <slug>] [--limit <n>] [--force]',
    '',
    'Options:',
    '  --dry-run       List pages without writing files',
    '  --topic <slug>  Generate one topic, e.g. average',
    '  --limit <n>     Generate at most n topics in tracker order',
    '  --force         Replace non-placeholder content as well'
  ].join('\n');
}

function extractPageData(html, filePath) {
  const matches = [...html.matchAll(/<script\b[^>]*\bid=["']upsc-page-data["'][^>]*>([\s\S]*?)<\/script>/gi)];
  if (matches.length !== 1) throw new Error(filePath + ': expected one upsc-page-data block, found ' + matches.length + '.');
  return JSON.parse(matches[0][1].trim());
}

function topicNames(existingData, slug) {
  const label = String(existingData.concepts?.sections?.[0]?.rows?.[0]?.[1] || slug);
  return {
    name: label.match(/\*\*(.*?)\*\*/)?.[1] || slug,
    hindiName: label.match(/\(([^()]*)\)/)?.[1] || ''
  };
}

function templatePage(slug, name, hindiName) {
  const templatePath = path.join(SCRIPT_DIR, 'average', 'index.html');
  const templateHtml = fs.readFileSync(templatePath, 'utf8');
  const templateData = extractPageData(templateHtml, templatePath);
  const html = templateHtml
    .replaceAll('Average', name)
    .replaceAll('औसत', hindiName)
    .replaceAll('/mathematics/average/', '/mathematics/' + slug + '/')
    .replaceAll('up-assistant-teacher.mathematics.average', 'up-assistant-teacher.mathematics.' + slug);
  return {
    html,
    pageData: {
      ...templateData,
      topicId: 'up-assistant-teacher.mathematics.' + slug,
      topicName: name,
      hindiName,
      subject: 'Mathematics',
      subjectDir: 'mathematics'
    }
  };
}

function discoverTopics() {
  if (!fs.existsSync(TRACKER_PATH)) throw new Error('Syllabus tracker not found: ' + TRACKER_PATH);
  const tracker = fs.readFileSync(TRACKER_PATH, 'utf8');
  const slugs = [...new Set([...tracker.matchAll(/href=["']\/up-assistant-teacher\/mathematics\/([^/"']+)\/?(?:[?#][^"']*)?["']/g)].map((match) => match[1]))].sort();
  return slugs.map((slug) => {
    if (!MATHEMATICS_STUDY[slug]) throw new Error('No manually authored Study tab exists for syllabus topic: ' + slug);
    const directory = path.join(SCRIPT_DIR, slug);
    const pagePath = path.join(directory, 'index.html');
    const dataPath = path.join(directory, 'data.json');
    const conceptsPath = path.join(directory, 'tabs', 'concepts.json');
    if (!fs.existsSync(pagePath)) throw new Error('Required page file is missing: ' + pagePath);
    let html = fs.readFileSync(pagePath, 'utf8');
    let pageData;
    try {
      pageData = extractPageData(html, pagePath);
    } catch (error) {
      if (html.trim().length >= 500) throw error;
      const existingData = fs.existsSync(dataPath) ? JSON.parse(fs.readFileSync(dataPath, 'utf8')) : {};
      const names = topicNames(existingData, slug);
      const fallback = templatePage(slug, names.name, names.hindiName);
      html = fallback.html;
      pageData = fallback.pageData;
      console.warn(slug + ': repairing its incomplete HTML shell from the existing Mathematics page template.');
    }
    const existingData = fs.existsSync(dataPath) ? JSON.parse(fs.readFileSync(dataPath, 'utf8')) : pageData;
    const conceptsText = JSON.stringify(existingData.concepts || {});
    const isPlaceholder = /under preparation|check back soon|being compiled|coming soon|resources are being/i.test(conceptsText);
    const hasExistingContent = !isPlaceholder && conceptsText.length > 1000;
    const generatedByUs = String(existingData.version?.generator || '').startsWith('up-assistant-maths-');
    const isCurrent = existingData.version?.generator === GENERATOR_VERSION;
    return { slug, pagePath, dataPath, conceptsPath, html, pageData, existingData, hasExistingContent, generatedByUs, isCurrent };
  });
}

function validateStudy(study, slug) {
  const errors = [];
  const hasTextbookSequence = Array.isArray(study?.sections)
    && study.sections.length > 0
    && study.sections.every((section) => section.type === 'paragraph' && section.title?.trim() && section.content?.trim());
  if (hasTextbookSequence) {
    if (!study.coverageAudit?.concepts?.length || !study.coverageAudit?.questionTypes?.length || !study.coverageAudit?.proofsAndDerivations?.length) errors.push(slug + ': coverage list is incomplete.');
    if (!study.keyTakeaways?.length) errors.push(slug + ': key takeaways are missing.');
    if (/\p{Script=Devanagari}/u.test(JSON.stringify(study))) errors.push(slug + ': Study tab must be English-only.');
    return errors;
  }
  const expectedTitles = [
    'Formula and skill map',
    'Core concepts and worked examples',
    'Question types and solving approaches',
    'Proofs and derivations',
    'Common errors and how to avoid them'
  ];
  if (!study || !Array.isArray(study.sections)) return [slug + ': study sections are missing.'];
  for (const title of expectedTitles) {
    const group = study.sections.find((item) => item.title === title);
    if (!group?.items?.length || group.type !== 'subcards') errors.push(slug + ': ' + title + ' is missing or empty.');
  }
  for (const group of study.sections) {
    if (group.type !== 'subcards' || !Array.isArray(group.items)) continue;
    for (const [index, item] of group.items.entries()) {
      if (!item.title?.trim() || !item.content?.trim()) errors.push(slug + ': ' + group.title + ' card ' + (index + 1) + ' is incomplete.');
      if (['Core concepts and worked examples', 'Question types and solving approaches'].includes(group.title) && !/worked example/i.test(item.content || '')) {
        errors.push(slug + ': ' + group.title + ' card "' + item.title + '" needs a worked example.');
      }
    }
  }
  if (!study.coverageAudit?.concepts?.length || !study.coverageAudit?.questionTypes?.length || !study.coverageAudit?.proofsAndDerivations?.length) errors.push(slug + ': coverage list is incomplete.');
  if (!study.keyTakeaways?.length) errors.push(slug + ': key takeaways are missing.');
  if (/\p{Script=Devanagari}/u.test(JSON.stringify(study))) errors.push(slug + ': Study tab must be English-only.');
  return errors;
}

function studyCounts(study) {
  return {
    concepts: study.coverageAudit?.concepts?.length || study.sections?.[1]?.items?.length || 0,
    questionTypes: study.coverageAudit?.questionTypes?.length || study.sections?.[2]?.items?.length || 0,
    proofs: study.coverageAudit?.proofsAndDerivations?.length || study.sections?.[3]?.items?.length || 0
  };
}

function validatePractice(practice, slug) {
  if (!practice) return [];
  const questions = Object.values(practice.levels || {}).flat();
  const errors = [];
  if (questions.length !== 30) errors.push(slug + ': expected 30 practice questions; found ' + questions.length + '.');
  for (const [level, items] of Object.entries(practice.levels || {})) {
    if (!Array.isArray(items) || items.length !== 10) errors.push(slug + ': ' + level + ' should contain 10 questions.');
  }
  const hasBalancedInlineMath = (value) => {
    let insideMath = false;
    for (const [token] of String(value || '').matchAll(/\\[()]/g)) {
      if (token === '\\(') {
        if (insideMath) return false;
        insideMath = true;
      } else {
        if (!insideMath) return false;
        insideMath = false;
      }
    }
    return !insideMath;
  };
  const ids = new Set();
  for (const [index, question] of questions.entries()) {
    if (!question.id || ids.has(question.id)) errors.push(slug + ': practice question ' + (index + 1) + ' has a missing or duplicate ID.');
    ids.add(question.id);
    if (!question.question?.trim() || !question.explanation?.trim()) errors.push(slug + ': practice question ' + (index + 1) + ' is missing its prompt or explanation.');
    if (!Array.isArray(question.options) || question.options.length !== 4 || question.options.map((option) => option.letter).sort().join('') !== 'ABCD') {
      errors.push(slug + ': practice question ' + (index + 1) + ' must have A-D options.');
    }
    if (!['A', 'B', 'C', 'D'].includes(question.correctAnswer)) errors.push(slug + ': practice question ' + (index + 1) + ' has an invalid answer key.');
    for (const [field, value] of [['question', question.question], ['explanation', question.explanation], ...(Array.isArray(question.options) ? question.options : []).map((option, optionIndex) => ['option ' + (optionIndex + 1), option.text])]) {
      if (!hasBalancedInlineMath(value)) errors.push(slug + ': practice question ' + (index + 1) + ' has unbalanced math delimiters in ' + field + '.');
    }
  }
  return errors;
}

function buildOutputs(topic) {
  const concepts = MATHEMATICS_STUDY[topic.slug];
  const validationErrors = validateStudy(concepts, topic.slug);
  validationErrors.push(...validatePractice(MATHEMATICS_PRACTICE[topic.slug], topic.slug));
  if (validationErrors.length) throw new Error(validationErrors.join('\n'));
  const payload = {
    ...topic.pageData,
    concepts,
    practice: MATHEMATICS_PRACTICE[topic.slug] || topic.pageData.practice,
    pyqs: topic.pageData.pyqs,
    test: topic.pageData.test,
    revision: topic.pageData.revision,
    version: { generator: GENERATOR_VERSION },
    generatedAt: new Date().toISOString()
  };
  const contentHash = createHash('sha256').update(JSON.stringify(concepts)).digest('hex');
  const externalData = { ...payload, contentHash };
  let updates = 0;
  const html = topic.html.replace(/(<script\b[^>]*\bid=["']upsc-page-data["'][^>]*>)([\s\S]*?)(<\/script>)/i, (_all, open, _old, close) => {
    updates += 1;
    return open + '\n' + JSON.stringify(externalData, null, 2) + '\n' + close;
  });
  if (updates !== 1) throw new Error(topic.slug + ': could not update embedded page data.');
  const outputs = [[topic.pagePath, html]];
  if (fs.existsSync(topic.dataPath)) {
    outputs.push([topic.dataPath, JSON.stringify(externalData, null, 2) + '\n']);
  }
  if (fs.existsSync(path.dirname(topic.conceptsPath))) {
    outputs.push([topic.conceptsPath, JSON.stringify(concepts, null, 2) + '\n']);
  }
  return outputs;
}

function writeOutputs(outputs) {
  const staged = [];
  try {
    for (const [target, content] of outputs) {
      const temporary = target + '.tmp-' + process.pid;
      fs.writeFileSync(temporary, content, 'utf8');
      staged.push([temporary, target]);
    }
    for (const [temporary, target] of staged) fs.renameSync(temporary, target);
  } catch (error) {
    for (const [temporary] of staged) if (fs.existsSync(temporary)) fs.unlinkSync(temporary);
    throw error;
  }
}

export function main(argv = process.argv.slice(2)) {
  const options = parseArgs(argv);
  if (options.help) {
    console.log(usage());
    return { generated: 0, skipped: 0 };
  }
  let topics = discoverTopics();
  if (topics.length !== 18) throw new Error('Expected 18 Mathematics syllabus topics; found ' + topics.length + '.');
  if (options.topic) {
    topics = topics.filter((item) => item.slug === options.topic);
    if (!topics.length) throw new Error('Topic not found: ' + options.topic);
  }
  if (options.limit !== null) topics = topics.slice(0, options.limit);
  const candidates = topics.filter((item) => options.force || (!item.isCurrent && (!item.hasExistingContent || item.generatedByUs)));
  const skipped = topics.length - candidates.length;
  console.log('Mathematics manual Study-tab generation: selected ' + topics.length + '; queued ' + candidates.length + '; protected ' + skipped + '.');
  if (options.dryRun) {
    for (const item of candidates) {
      const counts = studyCounts(MATHEMATICS_STUDY[item.slug]);
      console.log('  READY ' + item.slug + ': ' + counts.concepts + ' concepts, ' + counts.questionTypes + ' question types.');
    }
    console.log('Dry run only: no network calls and no files changed.');
    return { generated: 0, skipped };
  }
  let generated = 0;
  for (const item of candidates) {
    const outputs = buildOutputs(item);
    writeOutputs(outputs);
    generated += 1;
    const counts = studyCounts(MATHEMATICS_STUDY[item.slug]);
    console.log('  Wrote ' + item.slug + ': ' + counts.concepts + ' concepts, ' + counts.questionTypes + ' question types, ' + counts.proofs + ' proofs/derivations.');
  }
  console.log('Finished: ' + generated + ' English Study tabs written; Practice, Test, and Revision tabs preserved.');
  return { generated, skipped };
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  try {
    main();
  } catch (error) {
    console.error('Generation stopped: ' + error.message);
    process.exitCode = 1;
  }
}
