import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import { execFileSync } from 'node:child_process';
import { externalizeMusicVocalStyles, hydrateMusicVocalStyles, externalizeMusicVocalStyleGenerator, musicVocalTopicCss, musicVocalTopicStyleLink } from './lib/music-vocal-styles.mjs';

test('Music Vocal style is the frozen source and extraction preserves cascade and variants', () => {
  assert.equal(Buffer.byteLength(musicVocalTopicCss), 3104);
  assert.equal(crypto.createHash('sha256').update(musicVocalTopicCss).digest('hex'), '3cd6b57667f17ee0865df79252dee6fdf4d52e08868cd6180a9b06a5f7699a9b');
  const html = `<head><style>${musicVocalTopicCss}</style><style>.later{color:red}</style></head><main>Notes and questions</main>`;
  const expected = `<head>${musicVocalTopicStyleLink}<style>.later{color:red}</style></head><main>Notes and questions</main>`;
  assert.equal(externalizeMusicVocalStyles(html), expected);
  assert.equal(externalizeMusicVocalStyles(expected), expected);
  const variant = `<style>${musicVocalTopicCss}.edited{}</style>`;
  assert.equal(externalizeMusicVocalStyles(variant), variant);
  assert.equal(hydrateMusicVocalStyles(musicVocalTopicStyleLink.replace('.css', '.min.css?v=abc')), `<style>${musicVocalTopicCss}</style>`);
});

test('Music Vocal generator differs only by the stylesheet extraction and exact renderer move', () => {
  const original = execFileSync('git', ['show', '5d341a929ac7484c0c9c6e84486dab4e33a95995:scripts/generate_music_vocal_hi.mjs'], { encoding: 'utf8' });
  const current = fs.readFileSync(new URL('./generate_music_vocal_hi.mjs', import.meta.url), 'utf8');
  const normalize = source => source.replace(/\r\n/g, '\n');
  const styled = normalize(externalizeMusicVocalStyleGenerator(original));
  const block = styled.slice(styled.indexOf('function escapeHtml('), styled.indexOf('function chooseApiKey('));
  const schemaBlock = styled.slice(styled.indexOf('function requireText('), styled.indexOf('function buildContentPrompt('));
  const schemaTypes = "const QUESTION_TYPES = ['mcq', 'assertion_reason', 'true_false', 'fill_blank', 'match_following', 'case_based', 'short_answer'];";
  const expected = styled.replace(block, 'function compileHtml(content, questions, context) {\n  return compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink });\n}\n\n')
    .replace(schemaBlock, '\n').replace(schemaTypes + '\n', '')
    .replace("import { musicVocalTopicStyleLink } from './lib/music-vocal-styles.mjs';", "import { musicVocalTopicStyleLink } from './lib/music-vocal-styles.mjs';\nimport { compileMusicVocalHtml } from './lib/music-vocal-renderer.mjs';\nimport { QUESTION_TYPES, validateContent, validateQuestions } from './lib/music-vocal-schema.mjs';");
  const requestBlock = styled.slice(styled.indexOf('async function generateJson('), styled.indexOf('function escapeHtml('));
  const withRequest = expected.replace(requestBlock, 'async function generateJson(prompt, ai, validator, label, maxAttempts = 3) {\n  return generateMusicJson(prompt, ai, validator, label, { model: MODEL, parseJson, maxAttempts });\n}\n\n')
    .replace("import { QUESTION_TYPES, validateContent, validateQuestions } from './lib/music-vocal-schema.mjs';", "import { QUESTION_TYPES, validateContent, validateQuestions } from './lib/music-vocal-schema.mjs';\nimport { generateMusicJson } from './lib/music-json-request.mjs';");
  const parserBlock = styled.slice(styled.indexOf('function parseJson('), styled.indexOf('function requireText('));
  assert.equal(normalize(current), withRequest.replace(parserBlock, '').replace("import { jsonrepair } from 'jsonrepair';", "import { parseMusicJson as parseJson } from './lib/music-json-parser.mjs';"));
  const renderer = normalize(fs.readFileSync(new URL('./lib/music-vocal-renderer.mjs', import.meta.url), 'utf8'));
  assert.equal(renderer, '// Pure renderer: CLI owns generation, persistence and the shared asset references.\n' + block.replace('function compileHtml(content, questions, context) {', 'export function compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink }) {').trimEnd() + '\n');
  assert.equal(externalizeMusicVocalStyleGenerator(current), current);
  const schema = normalize(fs.readFileSync(new URL('./lib/music-vocal-schema.mjs', import.meta.url), 'utf8'));
  assert.equal(schema, '// Music Vocal content contract, kept independent of API calls and file writes.\nexport ' + schemaTypes + '\n\n' + schemaBlock.replace('function validateContent(', 'export function validateContent(').replace('function validateQuestions(', 'export function validateQuestions(').trimEnd() + '\n');
});
