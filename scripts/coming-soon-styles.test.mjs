import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';
import { COMING_SOON_STYLE_SHA256, COMING_SOON_STYLESHEET_HREF, externalizeComingSoonStyle } from './lib/coming-soon-styles.mjs';
import crypto from 'node:crypto';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CSS_PATH = path.join(ROOT, 'assets/css/coming-soon-page.css');

test('shared stylesheet exactly matches the recovered placeholder style', () => {
  const css = fs.readFileSync(CSS_PATH, 'utf8').trim();
  assert.equal(crypto.createHash('sha256').update(css).digest('hex'), COMING_SOON_STYLE_SHA256);
});

test('externalizes only the exact coming-soon style and leaves page body unchanged', () => {
  const css = fs.readFileSync(CSS_PATH, 'utf8').trim();
  const html = `<!doctype html><html><head><style>\n${css}\n</style></head><body><main>Keep this content</main></body></html>`;
  const result = externalizeComingSoonStyle(html);
  assert.ok(result.includes(`<link rel="stylesheet" href="${COMING_SOON_STYLESHEET_HREF}">`));
  assert.ok(!result.includes('<style>'));
  assert.equal(result.slice(result.indexOf('<body>')), html.slice(html.indexOf('<body>')));
});

test('leaves unrelated stylesheets unchanged', () => {
  const html = '<html><head><style>body{color:red}</style></head><body>content</body></html>';
  assert.equal(externalizeComingSoonStyle(html), html);
});

test('rejects multiple inline style blocks when one is the target stylesheet', () => {
  const css = fs.readFileSync(CSS_PATH, 'utf8').trim();
  const html = `<head><style>${css}</style><style>body{color:red}</style></head><body></body>`;
  assert.throws(() => externalizeComingSoonStyle(html), /exactly one inline coming-soon stylesheet/);
});
