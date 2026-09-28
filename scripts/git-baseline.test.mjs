import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { execFileSync } from 'node:child_process';
import { readGitBaseline } from './lib/git-baseline.mjs';

test('single-process baseline preserves ordered UTF-8, binary, empty and chunk-spanning bytes', { timeout: 20000 }, async () => {
  const parent = path.resolve(os.tmpdir());
  const root = fs.mkdtempSync(path.join(parent, 'sj-refactor-git-'));
  const git = args => execFileSync('git', args, { cwd: root, windowsHide: true });
  try {
    git(['init', '--quiet']);
    const entries = [
      ['notes with spaces.html', Buffer.from('Original प्रश्न $x^2$\r\n\nContent\0')],
      ['large.bin', Buffer.alloc(200000, 127)],
      ['empty.txt', Buffer.alloc(0)],
    ];
    for (const [file, bytes] of entries) fs.writeFileSync(path.join(root, file), bytes);
    git(['add', '--all']);
    git(['-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '--quiet', '-m', 'baseline']);
    const files = entries.map(([file]) => file).reverse();
    const seen = [];
    for await (const [file, bytes] of readGitBaseline(files, { root })) {
      assert.deepEqual(bytes, git(['show', `HEAD:${file}`]));
      seen.push(file);
    }
    assert.deepEqual(seen, files);
    for await (const entry of readGitBaseline(files, { root })) {
      assert.equal(entry[0], files[0]);
      break; // Cancelling a consumer must reap the child before cleanup.
    }
    await assert.rejects(async () => {
      for await (const entry of readGitBaseline(['missing.html'], { root })) void entry;
    }, /Cannot read baseline.*missing/);
    await assert.rejects(async () => {
      for await (const entry of readGitBaseline(['notes with spaces.html'], { root, baseline: 'absent-ref' })) void entry;
    }, /Cannot read baseline/);
    await assert.rejects(async () => {
      for await (const entry of readGitBaseline(['bad\nrequest'], { root })) void entry;
    }, /one line/);
  } finally {
    if (path.dirname(root) !== parent || !path.basename(root).startsWith('sj-refactor-git-')) throw new Error('Unexpected fixture cleanup path.');
    fs.rmSync(root, { recursive: true, force: true });
  }
});
