import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { commitBuildWrites } from './lib/build-transaction.mjs';
import { ibThemeBootstrap } from './lib/ib-theme-bootstrap.mjs';

const require = createRequire(import.meta.url);
const { ROOT } = require('./seo-html.cjs');
const apply = process.argv.includes('--apply');
const bootstrapHash = 'e1cefc58cdc639aab61bd36c85a4d88a8d4c46153cea3d682983f1465a95a328';
const toggleHash = '5a70a77cd69383f5db53a9680b37521d7c29f7f10a671773f65a954a35356bbf';
const bootstrapPages = ['ib/index.html', 'ib/myp-mathematics/index.html', 'ib/dp-mathematics/index.html', 'ib/command-terms/index.html'];
const togglePages = ['ib/dp-mathematics/analysis-and-approaches-sl/index.html', 'ib/myp-mathematics/algebra/index.html', 'ib/myp-mathematics/geometry-and-trigonometry/index.html', 'ib/myp-mathematics/statistics-and-probability/index.html'];
const targets = new Set([...bootstrapPages, ...togglePages]);
const writes = new Map();
const counts = { bootstraps: 0, togglers: 0, runtimesAdded: 0 };

const digest = source => crypto.createHash('sha256').update(source.trim()).digest('hex');
for (const file of targets) {
    const absolute = path.join(ROOT, file);
    const before = fs.readFileSync(absolute, 'utf8');
    let html = before.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attributes, source) => {
        if (/\bsrc\s*=|\btype\s*=|\bdefer\b|\basync\b/i.test(attributes)) return tag;
        const hash = digest(source);
        if (hash === bootstrapHash) {
            if (!bootstrapPages.includes(file)) throw new Error(`Unexpected IB bootstrap in ${file}`);
            counts.bootstraps++;
            return `<script>${ibThemeBootstrap}</script>`;
        }
        if (hash === toggleHash) {
            if (!togglePages.includes(file)) throw new Error(`Unexpected IB toggler in ${file}`);
            counts.togglers++;
            return '';
        }
        return tag;
    });
    if (togglePages.includes(file)) {
        html = html.replace(/<body\b([^>]*)>/i, `<body$1>\n<script>${ibThemeBootstrap}</script>`);
    }
    if (!html.includes('/assets/js/ib-theme.min.js')) {
        html = html.replace(/<\/body>/i, '    <script src="/assets/js/ib-theme.min.js"></script>\n</body>');
        counts.runtimesAdded++;
    }
    if (html !== before) writes.set(absolute, Buffer.from(html, 'utf8'));
}

if (counts.bootstraps !== 4 || counts.togglers !== 4 || counts.runtimesAdded !== 8 || writes.size !== 8) {
    throw new Error(`Unexpected IB migration inventory: ${JSON.stringify({ counts, changedPages: writes.size })}`);
}
if (apply) commitBuildWrites(writes);
console.log(JSON.stringify({ mode: apply ? 'apply' : 'dry-run', changedPages: writes.size, ...counts }, null, 2));
