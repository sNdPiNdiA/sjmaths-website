import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { createHomepageThemeBootstrap } from './lib/homepage-theme-bootstrap.mjs';

const require = createRequire(import.meta.url);
const { ROOT } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const known = new Map([
    ['index.html', '3c9e5f02f7de5d74e5a27f16f48ced64fe02024229c39ba07383f4f1cb91e38e'],
    ['pages/index.html', '0ec3ecedf66181e9fd8dbd16afb03d5355a2db545630ecb883db242a17863ac0'],
    ['competitive-exams/index.html', '57cdd2d48f5521597a919b84f3dd38877645921e91fb2414d12c2cd25014613d']
]);
const writes = new Map();
const digest = source => crypto.createHash('sha256').update(source.trim()).digest('hex');

for (const [file, expectedHash] of known) {
    const absolute = path.join(ROOT, file);
    const before = fs.readFileSync(absolute, 'utf8');
    let replacements = 0;
    const html = before.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attributes, source) => {
        if (/\bsrc\s*=|\btype\s*=|\bdefer\b|\basync\b/i.test(attributes) || digest(source) !== expectedHash) return tag;
        const paletteStart = source.indexOf('const savedTheme = localStorage.getItem');
        if (paletteStart < 0) throw new Error(`Palette bootstrap missing from ${file}`);
        let paletteBootstrap = source.slice(paletteStart).trim();
        if (file === 'index.html') {
            paletteBootstrap = paletteBootstrap.replace(/\}\)\(\);\s*$/, '').trimEnd();
        }
        replacements++;
        return `<script>${createHomepageThemeBootstrap(paletteBootstrap)}</script>`;
    });
    if (replacements !== 1) throw new Error(`Expected one known theme bootstrap in ${file}; found ${replacements}.`);
    writes.set(absolute, Buffer.from(html, 'utf8'));
}

if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', updatedPages: writes.size }, null, 2));
