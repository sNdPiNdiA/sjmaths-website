/* Keep exercise answers and quiz prompts in the initial HTML response.
 * JSON remains the editable source. --patch emits targeted apply_patch input;
 * the default/--check verifies that the published HTML is in sync.
 * Usage: node scripts/prerender-ganita-manjari.cjs --check
 */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');
const root = path.resolve(__dirname, '..');
const scope = 'class-9-ganita-manjari-part-2';
const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));

function prerender(source, file) {
  const $ = cheerio.load(source, { sourceCodeLocationInfo: true });
  const replacements = [];
  const answers = JSON.parse($('#exercise-answers').text() || '[]');
  const details = $('#p-exercises details');
  if (answers.length && answers.length !== details.length) throw new Error(file + ': answer count mismatch');
  details.each((index, detail) => {
    if (!answers.length) return;
    const answer = answers[index].answer;
    if (typeof answer !== 'string' || !answer.trim()) throw new Error(file + ': missing answer ' + index);
    const markup = '<div class="answer-box"><div class="answer-controls"><span class="answer-kicker">Answer / method</span><button type="button" class="btng btn tog" aria-expanded="false">Show Answer</button></div><div class="an answer-text">' + escape(answer).replace(/\n/g, '&#10;') + '</div></div>';
    const box = $(detail).find('.answer-box').first()[0];
    if (box) {
      replacements.push({ start: box.sourceCodeLocation.startOffset, end: box.sourceCodeLocation.endOffset, markup });
    } else {
      const body = $(detail).children('.db')[0];
      const at = (body || detail).sourceCodeLocation.endTag.startOffset;
      replacements.push({ start: at, end: at, markup: body ? markup : '<div class="db">' + markup + '</div>' });
    }
  });
  const quiz = $('#quiz')[0];
  const questions = JSON.parse($('#quiz-data').text() || '[]');
  if (!quiz || !questions.length) throw new Error(file + ': missing quiz');
  const markup = questions.map((q, i) => {
    if (!Array.isArray(q.o) || !Number.isInteger(q.a) || q.a < 0 || q.a >= q.o.length) throw new Error(file + ': invalid quiz item ' + i);
    return '<div class="mc"><h4>Q' + (i + 1) + '. ' + escape(q.q) + '</h4>' + q.o.map(o => '<button type="button" class="op">' + escape(o) + '</button>').join('') + '</div>';
  }).join('');
  replacements.push({ start: quiz.sourceCodeLocation.startTag.endOffset, end: quiz.sourceCodeLocation.endTag.startOffset, markup });
  for (const r of replacements.sort((a, b) => b.start - a.start)) source = source.slice(0, r.start) + r.markup + source.slice(r.end);
  return source;
}

let stale = 0;
let patch = '*** Begin Patch\n';
for (const dir of fs.readdirSync(path.join(root, scope), { withFileTypes: true }).filter(d => d.isDirectory())) {
  const file = scope + '/' + dir.name + '/index.html';
  const before = fs.readFileSync(path.join(root, file), 'utf8');
  const after = prerender(before, file);
  if (after === before) continue;
  stale++;
  if (!process.argv.includes('--patch')) { console.error(file + ': static answers/quiz need rebuilding'); continue; }
  const oldLines = before.replace(/\r\n/g, '\n').split('\n');
  const newLines = after.replace(/\r\n/g, '\n').split('\n');
  if (oldLines.length !== newLines.length) throw new Error(file + ': unexpected source line changes');
  patch += '*** Update File: ' + path.join(root, file).replace(/\\/g, '/') + '\n';
  oldLines.forEach((line, i) => {
    if (line !== newLines[i]) patch += '@@\n-' + line + '\n+' + newLines[i] + '\n';
  });
}
if (process.argv.includes('--patch')) process.stdout.write(patch + '*** End Patch\n');
else { console.log('Static Ganita Manjari content: ' + (stale ? stale + ' stale pages' : 'all six chapters in sync')); process.exitCode = stale ? 1 : 0; }
