import { spawn } from 'node:child_process';

// Stream original file bytes through one Git process. Comparison policy stays
// with each caller; this helper neither normalizes content nor changes files.
export async function* readGitBaseline(files, { root, baseline = 'HEAD' }) {
  if (!files.length) return;
  const specs = files.map(file => `${baseline}:${file}`);
  if (specs.some(spec => /[\r\n\0]/.test(spec))) throw new Error('Git baseline requests must fit on one line.');
  const child = spawn('git', ['cat-file', '--batch'], { cwd: root, windowsHide: true });
  let stderr = '', inputError;
  child.stderr.on('data', chunk => { stderr = (stderr + chunk.toString('utf8')).slice(-8192); });
  child.stdin.on('error', error => { inputError = error; });
  const completion = new Promise(resolve => {
    child.once('error', error => resolve({ error }));
    child.once('close', (code, signal) => resolve({ code, signal }));
  });
  child.stdin.end(specs.join('\n') + '\n');
  const chunks = child.stdout[Symbol.asyncIterator]();
  let buffer = Buffer.alloc(0);
  const more = async () => {
    const next = await chunks.next();
    if (next.done) throw new Error(`Truncated Git baseline output: ${stderr || inputError?.message || 'unexpected EOF'}`);
    buffer = buffer.length ? Buffer.concat([buffer, next.value]) : next.value;
  };
  const take = async size => {
    while (buffer.length < size) await more();
    const bytes = buffer.subarray(0, size);
    buffer = buffer.subarray(size);
    return bytes;
  };
  try {
    for (let index = 0; index < files.length; index++) {
      while (!buffer.includes(10)) {
        if (buffer.length > 65536) throw new Error('Invalid Git baseline header.');
        await more();
      }
      const newline = buffer.indexOf(10);
      const header = (await take(newline + 1)).subarray(0, newline).toString('utf8');
      const match = header.match(/^[a-f0-9]{40,64} blob (\d+)$/);
      if (!match) throw new Error(`Cannot read baseline ${specs[index]}: ${header}`);
      const size = Number(match[1]);
      if (!Number.isSafeInteger(size)) throw new Error('Invalid Git baseline object size.');
      const bytes = await take(size);
      if ((await take(1))[0] !== 10) throw new Error('Invalid Git baseline object separator.');
      yield [files[index], bytes];
    }
    if (buffer.length || !(await chunks.next()).done) throw new Error('Unexpected extra Git baseline output.');
    const result = await completion;
    if (result.error || result.code !== 0 || inputError) {
      throw new Error(`Git baseline failed: ${result.error?.message || inputError?.message || stderr || result.signal || result.code}`);
    }
  } finally {
    // An aborted consumer must not leave a blocked cat-file child behind.
    child.stdout.destroy();
    child.stderr.destroy();
    if (child.exitCode === null && !child.killed) child.kill();
    await completion;
  }
}
