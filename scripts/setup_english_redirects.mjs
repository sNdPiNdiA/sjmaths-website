#!/usr/bin/env node
/**
 * Setup clean HTML redirects for legacy and nested English directories to canonical 24 topics.
 */

import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const BASE_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'english');

const REDIRECTS = [
  {
    from: 'parts-of-speech',
    to: '/up-upper-primary-teacher/english/parts-of-speech-nouns-pronouns/'
  },
  {
    from: 'vocabulary',
    to: '/up-upper-primary-teacher/english/vocabulary-synonyms-antonyms/'
  },
  {
    from: 'unseen-passage-comprehension',
    to: '/up-upper-primary-teacher/english/unseen-prose-comprehension/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'active-and-passive-voice'),
    to: '/up-upper-primary-teacher/english/active-passive/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'articles-and-determiners'),
    to: '/up-upper-primary-teacher/english/articles/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'conjunctions-and-clause-analysis'),
    to: '/up-upper-primary-teacher/english/conjunctions/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'direct-and-indirect-speech'),
    to: '/up-upper-primary-teacher/english/direct-indirect/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'error-spotting-sentence-correction'),
    to: '/up-upper-primary-teacher/english/error-spotting/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'parts-of-speech-nouns-pronouns-verbs'),
    to: '/up-upper-primary-teacher/english/parts-of-speech-nouns-pronouns/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'prepositions-and-phrasal-verbs'),
    to: '/up-upper-primary-teacher/english/prepositions/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'subject-verb-concord-agreement'),
    to: '/up-upper-primary-teacher/english/subject-verb/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'tenses-and-time-aspects'),
    to: '/up-upper-primary-teacher/english/tenses/'
  },
  {
    from: path.join('english-grammar-syntax-vocabulary', 'vocabulary-synonyms-antonyms-idioms'),
    to: '/up-upper-primary-teacher/english/vocabulary-synonyms-antonyms/'
  },
  {
    from: 'english-grammar-syntax-vocabulary',
    to: '/up-upper-primary-teacher/english/'
  },
  {
    from: 'history-of-english-literature-language',
    to: '/up-upper-primary-teacher/english/'
  },
  {
    from: 'major-writers-poets-and-works',
    to: '/up-upper-primary-teacher/english/'
  }
];

function buildRedirectHtml(targetUrl) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta http-equiv="refresh" content="0; url=${targetUrl}"/>
<link rel="canonical" href="https://sjmaths.com${targetUrl}"/>
<title>Redirecting...</title>
<script>window.location.replace("${targetUrl}");</script>
</head>
<body>
<p>This page has moved. If you are not redirected automatically, <a href="${targetUrl}">click here</a>.</p>
</body>
</html>
`;
}

console.log('Setting up English redirect stubs...');
let count = 0;
for (const r of REDIRECTS) {
  const dir = path.join(BASE_DIR, r.from);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  const file = path.join(dir, 'index.html');
  fs.writeFileSync(file, buildRedirectHtml(r.to), 'utf8');
  console.log(`  ✓ ${r.from} -> ${r.to}`);
  count++;
}
console.log(`Successfully configured ${count} redirect stubs.`);
