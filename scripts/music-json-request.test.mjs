import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
import { generateMusicJson } from './lib/music-json-request.mjs';

const source = execFileSync('git', ['show', '150c071b46:scripts/generate_music_vocal_hi.mjs'], { encoding: 'utf8' }).replace(/\r\n/g, '\n');
const original = source.slice(source.indexOf('async function generateJson('), source.indexOf('function escapeHtml('));
test('shared request source is the exact frozen loop with only dependency injection', () => {
  const expected = original
    .replace('async function generateJson(prompt, ai, validator, label, maxAttempts = 3) {', "export async function generateMusicJson(prompt, ai, validator, label, { model: MODEL, parseJson, maxAttempts = 3, warn = console.warn, sleep = ms => new Promise(resolve => setTimeout(resolve, ms)), emptyResponseMessage = 'Gemini returned an empty response' }) {")
    .replace("throw new Error('Gemini returned an empty response')", 'throw new Error(emptyResponseMessage)')
    .replaceAll('console.warn(', 'warn(')
    .replace('await new Promise((resolve) => setTimeout(resolve, waitMs));', 'await sleep(waitMs);');
  assert.equal(fs.readFileSync(new URL('./lib/music-json-request.mjs', import.meta.url), 'utf8').replace(/\r\n/g, '\n'), '// Existing Music generator retry policy; dependencies are injectable for offline tests.\n' + expected.trimEnd() + '\n');
});
test('Instrumental CLI changes only by the shared request import and forwarding wrapper', () => {
  const baseline = execFileSync('git', ['show', '150c071b46:scripts/generate_music_instrumental_hi.mjs'], { encoding: 'utf8' }).replace(/\r\n/g, '\n');
  const block = baseline.slice(baseline.indexOf('async function generateJson('), baseline.indexOf('function escapeHtml('));
  assert.equal(block, original.replace('Gemini returned an empty response', 'Gemini ने खाली उत्तर लौटाया'));
  const expected = baseline.replace("import { jsonrepair } from 'jsonrepair';", "import { jsonrepair } from 'jsonrepair';\nimport { generateMusicJson } from './lib/music-json-request.mjs';")
    .replace(block, "async function generateJson(prompt, ai, validator, label, maxAttempts = 3) {\n  return generateMusicJson(prompt, ai, validator, label, { model: MODEL, parseJson, maxAttempts, emptyResponseMessage: 'Gemini ने खाली उत्तर लौटाया' });\n}\n\n");
  const parserBlock = baseline.slice(baseline.indexOf('function parseJson('), baseline.indexOf('function requireText('));
  assert.equal(fs.readFileSync(new URL('./generate_music_instrumental_hi.mjs', import.meta.url), 'utf8').replace(/\r\n/g, '\n'), expected.replace(parserBlock, '').replace("import { jsonrepair } from 'jsonrepair';", "import { parseMusicJson as parseJson } from './lib/music-json-parser.mjs';"));
});
async function run(legacy, responses, rejectValidation, maxAttempts = 3) {
  const calls = [], waits = [], warnings = [];
  const ai = { models: { generateContent: async input => {
    calls.push(input);
    const response = responses[calls.length - 1];
    if (response instanceof Error) throw response;
    return response;
  } } };
  const validator = data => { if (rejectValidation(data)) throw new Error('missing concept'); };
  const sandbox = { MODEL: 'offline-model', parseJson: JSON.parse, console: { warn: message => warnings.push(message) }, setTimeout: (resolve, ms) => { waits.push(ms); resolve(); } };
  let request = generateMusicJson;
  if (legacy) { vm.runInNewContext(original + '\nthis.request = generateJson;', sandbox); request = sandbox.request; }
  let result;
  try {
    const value = legacy ? await request('prompt', ai, validator, 'Notes', maxAttempts) : await request('prompt', ai, validator, 'Notes', { model: 'offline-model', parseJson: JSON.parse, maxAttempts, warn: message => warnings.push(message), sleep: async ms => { waits.push(ms); } });
    result = { value };
  } catch (error) { result = { error: error?.message, validation: error?.isValidationError, partial: error?.partialData }; }
  return JSON.parse(JSON.stringify({ calls, waits, warnings, result }));
}
const response = value => ({ text: JSON.stringify(value) });
for (const [name, responses, reject, attempts] of [
  ['successful first response', [response({ ok: true })], () => false],
  ['corrected validation prompt', [response({ ok: false }), response({ ok: true })], d => !d.ok],
  ['final validation response retained', [response({ ok: false }), response({ ok: false }), response({ ok: false })], () => true],
  ['transient server failure', [Object.assign(new Error('server'), { status: 500 }), response({ ok: true })], () => false],
  ['empty response retry', [{ text: '' }, response({ ok: true })], () => false],
  ['malformed JSON retry', [{ text: '{' }, response({ ok: true })], () => false],
  ['exhausted transport retries', Array.from({ length: 3 }, () => new Error('network')), () => false],
  ['long backoff cap', Array.from({ length: 6 }, () => new Error('network')), () => false, 6],
  ...[400, 401, 403, 429].map(status => [`terminal status ${status}`, [Object.assign(new Error('terminal'), { status })], () => false]),
  ['nested quota status', [Object.assign(new Error('quota'), { response: { status: 429 } })], () => false],
  ['quota message', [new Error('RESOURCE_EXHAUSTED')], () => false]
]) test(`request policy preserves ${name}`, async () => {
  assert.deepEqual(await run(false, responses, reject, attempts), await run(true, responses, reject, attempts));
});

test('injected empty-response localization does not require a second retry implementation', async () => {
  await assert.rejects(generateMusicJson('prompt', { models: { generateContent: async () => ({ text: '' }) } }, () => {}, 'Notes', { model: 'offline', parseJson: JSON.parse, maxAttempts: 1, emptyResponseMessage: 'Gemini ने खाली उत्तर लौटाया' }), /Gemini ने खाली उत्तर लौटाया/);
});
