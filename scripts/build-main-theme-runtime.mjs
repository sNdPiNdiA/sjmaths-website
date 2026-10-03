import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import esbuild from 'esbuild';
import { fileURLToPath } from 'node:url';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { createReferenceUpdater } from './lib/build-references.mjs';

const scriptPath = fileURLToPath(import.meta.url);
const defaultRoot = path.resolve(path.dirname(scriptPath), '..');
const rootArg = process.argv.find(arg => arg.startsWith('--root='));
const root = rootArg ? path.resolve(rootArg.slice('--root='.length)) : defaultRoot;
const dryRun = process.argv.includes('--dry-run');
const selectedAssets = process.argv.filter(arg => arg.startsWith('--asset=')).map(arg => arg.slice('--asset='.length));
if (!selectedAssets.length) selectedAssets.push('assets/js/main.js');
const mapping = {};
const hashes = {};
const writes = new Map();

for (const source of new Set(selectedAssets)) {
    if (path.isAbsolute(source) || source.split(/[\\/]/).includes('..') || !/^(assets|utils)[\\/].+\.(js|css)$/.test(source) || source.includes('.min.')) {
        throw new Error(`Unsupported source asset: ${source}`);
    }
    const normalizedSource = source.replace(/\\/g, '/');
    const extension = path.extname(normalizedSource);
    const output = normalizedSource.slice(0, -extension.length) + `.min${extension}`;
    const sourcePath = path.join(root, normalizedSource);
    const outputPath = path.join(root, output);
    const result = esbuild.buildSync({ entryPoints: [sourcePath], outfile: outputPath, minify: true, sourcemap: false, write: false });
    const outputBytes = Buffer.from(result.outputFiles[0].contents);
    mapping[normalizedSource] = output;
    hashes[output] = crypto.createHash('md5').update(outputBytes).digest('hex').slice(0, 8);
    writes.set(outputPath, outputBytes);
}

const updateReferences = createReferenceUpdater(mapping, hashes);
const ignoredDirs = new Set(['node_modules', '.git', '.firebase', 'gs-question-bank', 'assets', 'utils', 'scripts', '.github', '.venv', 'scratch', '.pages-dist']);

function collectHtml(directory) {
    for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
        const filePath = path.join(directory, entry.name);
        if (entry.isDirectory()) {
            if (!ignoredDirs.has(entry.name)) collectHtml(filePath);
        } else if (entry.isFile() && entry.name.endsWith('.html')) {
            const before = fs.readFileSync(filePath, 'utf8');
            const after = updateReferences(before).replace(/^([^\r\n]*main\.min\.js[^\r\n]*?)[\t ]+(?=\r?$)/gm, '$1');
            if (after !== before) writes.set(filePath, Buffer.from(after, 'utf8'));
        }
    }
}

collectHtml(root);
const changedWrites = new Map([...writes].filter(([filePath, contents]) =>
    !fs.existsSync(filePath) || !fs.readFileSync(filePath).equals(contents)));

if (dryRun) {
    const versions = Object.entries(hashes).map(([asset, hash]) => `${asset}?v=${hash}`).join(', ');
    console.log(`Theme asset build dry run: ${changedWrites.size} files would change; no files written. ${versions}`);
} else {
    commitBuildWrites(changedWrites);
    const versions = Object.entries(hashes).map(([asset, hash]) => `${asset}?v=${hash}`).join(', ');
    console.log(`Theme asset build complete: ${changedWrites.size} files updated. ${versions}`);
}
