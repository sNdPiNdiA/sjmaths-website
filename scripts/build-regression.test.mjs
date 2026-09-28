import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';

const buildScript = fileURLToPath(new URL('../build.js', import.meta.url));
function fixture(t) {
    const root = fs.mkdtempSync(path.join(os.tmpdir(), 'sjmaths-build-test-'));
    t.after(() => {
        const resolved = path.resolve(root);
        assert.equal(path.dirname(resolved), path.resolve(os.tmpdir()));
        assert.ok(path.basename(resolved).startsWith('sjmaths-build-test-'));
        fs.rmSync(resolved, { recursive: true, force: true });
    });
    const write = (relative, contents) => {
        const file = path.join(root, relative);
        fs.mkdirSync(path.dirname(file), { recursive: true });
        fs.writeFileSync(file, contents);
        return file;
    };
    write('assets/js/example.js', 'window.example = 42;');
    write('assets/js/example.min.js', 'OLD SCRIPT');
    write('assets/css/example.css', 'body { color: green; }');
    write('assets/css/example.min.css', 'OLD CSS');
    write('assets/js/legacy.min.js', 'LEGACY OUTPUT');
    write('index.html', '<link href="/assets/css/example.css"><script src="/assets/js/example.min.js?v=old"></script>');
    write('service-worker.js', "const CACHE_NAME = 'old'; const ASSETS = ['/assets/js/example.min.js?v=old'];");
    write('scratch/snapshot.html', '<script src="/assets/js/example.js"></script>');
    write('.pages-dist/index.html', '<script src="/assets/js/example.js"></script>');
    return { root, write, read: relative => fs.readFileSync(path.join(root, relative), 'utf8') };
}
function build(root, ...args) {
    return spawnSync(process.execPath, [buildScript, `--root=${root}`, ...args], { encoding: 'utf8' });
}

test('failed asset compilation preserves existing assets, page references and worker', t => {
    const f = fixture(t);
    f.write('assets/js/broken.js', 'function (');
    const result = build(f.root);
    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /Build aborted without writing files/);
    assert.equal(f.read('assets/js/example.min.js'), 'OLD SCRIPT');
    assert.equal(f.read('assets/css/example.min.css'), 'OLD CSS');
    assert.match(f.read('index.html'), /v=old/);
    assert.match(f.read('service-worker.js'), /CACHE_NAME = 'old'/);
    assert.equal(fs.existsSync(path.join(f.root, 'assets/js/broken.min.js')), false);
});

test('successful build updates assets and hashes without changing local snapshots or deleting legacy outputs', t => {
    const f = fixture(t);
    const result = build(f.root);
    assert.equal(result.status, 0, result.stderr);
    assert.match(f.read('assets/js/example.min.js'), /window\.example=42/);
    assert.match(f.read('index.html'), /example\.min\.css\?v=[a-f0-9]{8}/);
    assert.match(f.read('index.html'), /example\.min\.js\?v=[a-f0-9]{8}/);
    assert.match(f.read('service-worker.js'), /CACHE_NAME = 'sjmaths-v[a-f0-9]{8}'/);
    assert.match(f.read('scratch/snapshot.html'), /example\.js/);
    assert.match(f.read('.pages-dist/index.html'), /example\.js/);
    assert.equal(f.read('assets/js/legacy.min.js'), 'LEGACY OUTPUT');
    const repeated = build(f.root);
    assert.equal(repeated.status, 0, repeated.stderr);
    assert.match(repeated.stdout, /0 files updated/);
});

test('dry run compiles and validates without writing assets or pages', t => {
    const f = fixture(t);
    const result = build(f.root, '--dry-run');
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /no files written/);
    assert.equal(f.read('assets/js/example.min.js'), 'OLD SCRIPT');
    assert.match(f.read('index.html'), /v=old/);
});

test('preparation failure leaves served files intact and cleans temporary replacements', t => {
    const f = fixture(t);
    const target = path.join(f.root, 'assets/js/example.min.js');
    const io = { ...fs, writeFileSync(file, ...args) {
        if (String(file).includes('missing-parent')) throw new Error('injected preparation failure');
        return fs.writeFileSync(file, ...args);
    } };
    assert.throws(() => commitBuildWrites(new Map([[target, Buffer.from('NEW')], [path.join(f.root, 'missing-parent/new.js'), Buffer.from('NEW')]]), io), /preparation failure/);
    assert.equal(f.read('assets/js/example.min.js'), 'OLD SCRIPT');
    assert.equal(fs.readdirSync(path.dirname(target)).some(name => name.includes('.sj-build-')), false);
});

test('commit failure restores already-replaced files and cleans temporary replacements', t => {
    const f = fixture(t);
    const script = path.join(f.root, 'assets/js/example.min.js');
    const css = path.join(f.root, 'assets/css/example.min.css');
    const io = { ...fs, renameSync(from, to) {
        if (to === css) throw new Error('injected commit failure');
        return fs.renameSync(from, to);
    } };
    assert.throws(() => commitBuildWrites(new Map([[script, Buffer.from('NEW')], [css, Buffer.from('NEW')]]), io), /commit failure/);
    assert.equal(f.read('assets/js/example.min.js'), 'OLD SCRIPT');
    assert.equal(f.read('assets/css/example.min.css'), 'OLD CSS');
    assert.equal(fs.readdirSync(path.dirname(script)).some(name => name.includes('.sj-build-')), false);
    assert.equal(fs.readdirSync(path.dirname(css)).some(name => name.includes('.sj-build-')), false);
});
