#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PHYSICS_ROOT = path.join(ROOT, 'physics');
const BASE_URL = process.env.PHYSICS_TEST_BASE_URL || 'http://localhost:8082';

function collect(directory) {
  const files = [];
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...collect(fullPath));
    else if (entry.isFile() && entry.name === 'index.html') files.push(fullPath);
  }
  return files.sort();
}

const files = collect(PHYSICS_ROOT);
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
const failures = [];
for (const file of files) {
  const relative = path.relative(ROOT, path.dirname(file)).replace(/\\/g, '/');
  const url = `${BASE_URL}/${relative}/`;
  try {
    const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 15000 });
    await page.waitForTimeout(250);
    const errors = await page.locator('.katex-error').allTextContents();
    if (response?.status() !== 200 || errors.length) failures.push({ url, status: response?.status(), katexErrors: errors.slice(0, 3) });
  } catch (error) {
    failures.push({ url, error: error.message });
  }
}
await browser.close();
console.log(JSON.stringify({ pages: files.length, failures: failures.length, examples: failures.slice(0, 10) }, null, 2));
if (failures.length) process.exit(1);
