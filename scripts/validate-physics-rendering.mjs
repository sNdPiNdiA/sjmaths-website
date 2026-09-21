#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const PHYSICS_ROOT = path.join(ROOT, 'physics');

function collect(directory, suffix) {
  const files = [];
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...collect(fullPath, suffix));
    else if (entry.isFile() && entry.name.endsWith(suffix)) files.push(fullPath);
  }
  return files;
}

function hasControl(value) {
  if (typeof value === 'string') return /[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(value);
  if (Array.isArray(value)) return value.some(hasControl);
  if (value && typeof value === 'object') return Object.values(value).some(hasControl);
  return false;
}

const jsonFiles = collect(PHYSICS_ROOT, '.json');
const htmlFiles = collect(PHYSICS_ROOT, 'index.html');
const invalidJson = [];
const controlJson = [];
for (const file of jsonFiles) {
  try {
    const parsed = JSON.parse(fs.readFileSync(file, 'utf8'));
    if (hasControl(parsed)) controlJson.push(file);
  } catch (error) {
    invalidJson.push(`${file}: ${error.message}`);
  }
}

const controlHtml = htmlFiles.filter(file => /[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(fs.readFileSync(file, 'utf8')));
const report = {
  jsonFiles: jsonFiles.length,
  htmlFiles: htmlFiles.length,
  invalidJson: invalidJson.length,
  controlJson: controlJson.length,
  controlHtml: controlHtml.length,
  examples: {
    invalidJson: invalidJson.slice(0, 5),
    controlJson: controlJson.slice(0, 5),
    controlHtml: controlHtml.slice(0, 5)
  }
};
console.log(JSON.stringify(report, null, 2));
if (invalidJson.length || controlJson.length || controlHtml.length) process.exit(1);
