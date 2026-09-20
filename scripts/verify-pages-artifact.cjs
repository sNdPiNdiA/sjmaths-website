#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { collectRuntimeJsonFiles } = require('./runtime-json-assets.cjs');

const ROOT = path.resolve(__dirname, '..');
const outputArgument = process.argv.find(argument => argument === '--output-dir' || argument.startsWith('--output-dir='));
const outputValue = outputArgument?.includes('=')
  ? outputArgument.split('=').slice(1).join('=')
  : (() => {
      const index = process.argv.indexOf('--output-dir');
      return index >= 0 ? process.argv[index + 1] : null;
    })();
const deploymentRoot = path.resolve(ROOT, outputValue || '.pages-dist');
const runtimeJsonFiles = collectRuntimeJsonFiles({ root: ROOT });

if (!fs.existsSync(deploymentRoot) || !fs.statSync(deploymentRoot).isDirectory()) {
  console.error(`❌ Pages artifact directory does not exist: ${path.relative(ROOT, deploymentRoot)}`);
  process.exit(1);
}

const missingRuntimeFiles = [...runtimeJsonFiles].filter(file => !fs.existsSync(path.join(deploymentRoot, file)));
const forbiddenDirectories = ['node_modules', 'scratch', '.git', 'scripts']
  .filter(directory => fs.existsSync(path.join(deploymentRoot, directory)));

function countFiles(directory) {
  let count = 0;
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const fullPath = path.join(directory, entry.name);
    count += entry.isDirectory() ? countFiles(fullPath) : 1;
  }
  return count;
}

const fileCount = countFiles(deploymentRoot);
const result = {
  output: path.relative(ROOT, deploymentRoot).replace(/\\/g, '/'),
  fileCount,
  runtimeJsonFiles: runtimeJsonFiles.size,
  missingRuntimeFiles: missingRuntimeFiles.length,
  forbiddenDirectories,
};
console.log(JSON.stringify(result, null, 2));

if (missingRuntimeFiles.length || forbiddenDirectories.length || fileCount > 20000) {
  if (missingRuntimeFiles.length) {
    console.error(`❌ Missing runtime JSON files: ${missingRuntimeFiles.slice(0, 20).join(', ')}${missingRuntimeFiles.length > 20 ? ' …' : ''}`);
  }
  if (forbiddenDirectories.length) {
    console.error(`❌ Development directories found in artifact: ${forbiddenDirectories.join(', ')}`);
  }
  if (fileCount > 20000) console.error(`❌ Artifact contains ${fileCount} files; Cloudflare Pages limit is 20,000.`);
  process.exit(1);
}

console.log('✅ Pages artifact passed runtime-asset and deployment-scope verification.');
