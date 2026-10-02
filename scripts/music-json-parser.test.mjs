import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import { execFileSync } from 'node:child_process';
import { jsonrepair } from 'jsonrepair';
import { parseMusicJson } from './lib/music-json-parser.mjs';

const source = execFileSync('git', ['show', '150c071b46:scripts/generate_music_vocal_hi.mjs'], { encoding: 'utf8' }).replace(/\r\n/g, '\n');
const original = source.slice(source.indexOf('function parseJson('), source.indexOf('function requireText('));
const sandbox = { jsonrepair };
vm.runInNewContext(original + '\nthis.parse = parseJson;', sandbox);
const outcome = (parse, raw) => {
  try { return { value: JSON.stringify(parse(raw)) }; }
  catch (error) { return { error: error.message }; }
};
test('shared parser source preserves the complete original implementation', () => {
  assert.equal(fs.readFileSync(new URL('./lib/music-json-parser.mjs', import.meta.url), 'utf8').replace(/\r\n/g, '\n'), "import { jsonrepair } from 'jsonrepair';\n\n// Exact existing Music response parser, independent of API and page persistence.\n" + original.replace('function parseJson(', 'export function parseMusicJson(').trimEnd() + '\n');
  assert.deepEqual(parseMusicJson('```json\n{"title":"स्वर","points":["नाद"]}\n```'), { title: 'स्वर', points: ['नाद'] });
  assert.deepEqual(parseMusicJson("{title:'स्वर', points:['नाद',],}"), { title: 'स्वर', points: ['नाद'] });
});
test('parser preserves fenced, repaired, primitive and unrecoverable response outcomes', () => {
  for (const raw of ['{"title":"स्वर"}', ' ```JSON\n{"title":"स्वर"}\n``` ', "{title:'स्वर',}", '{"title":"स्वर"', '[1,2,]', 'null', 'false', '17', '"नाद"', '', null, undefined, '{"a": "unterminated', '\u0000', '```json\n[1, {bad: true}]\n```', '{"a":1} {"b":2}']) {
    assert.deepEqual(outcome(parseMusicJson, raw), outcome(sandbox.parse, raw));
  }
});
