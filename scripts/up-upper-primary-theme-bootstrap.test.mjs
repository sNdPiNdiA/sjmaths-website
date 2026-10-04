import assert from 'node:assert/strict';
import fs from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';
import { migrateUpUpperPrimaryThemeBootstraps } from './lib/up-upper-primary-theme-bootstrap.mjs';

test('migrated English and Hindi Upper Primary pages retain palette setup and remain idempotent', () => {
    for (const file of [
        'up-upper-primary-teacher/english/active-passive/index.html',
        'up-upper-primary-teacher/hindi/varnamala/index.html'
    ]) {
        const before = fs.readFileSync(file, 'utf8');
        const { html, counts } = migrateUpUpperPrimaryThemeBootstraps(before);
        const replacements = Object.values(counts).reduce((sum, count) => sum + count, 0);
        assert.equal(replacements, 0, `${file} should not need another migration`);
        assert.ok(html.includes("sjmaths.theme.preference"), `${file} should use the canonical preference`);
        assert.ok(html.includes('const savedTheme = localStorage.getItem'), `${file} should preserve palette setup`);
        assert.ok(html.includes("getAttribute('data-theme') === 'dark'"), `${file} should sync body theme from the root`);
        assert.ok(!html.includes('<\\/script>'), `${file} should emit valid script closing tags`);

        for (const match of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
            if (/\bsrc\s*=|\btype\s*=|\bdefer\b|\basync\b/i.test(match[1])) continue;
            new vm.Script(match[2], { filename: file });
        }
    }
});
