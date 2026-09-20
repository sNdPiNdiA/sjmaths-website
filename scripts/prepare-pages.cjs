#!/usr/bin/env node
/**
 * Cloudflare Pages Build Prepper
 * Cloudflare Pages Free/Pro plans have a limit of 20,000 files per deployment.
 * The repo has ~9,550 HTML pages + assets (~10,100 files), but contains 13,700+ generator JSON
 * files and 5,000+ node_modules files (total ~29,300 files).
 *
 * This script runs during the Cloudflare Pages build step to:
 * 1. Execute 'node build.js' to ensure fresh minified assets & cache busters.
 * 2. Prune node_modules, scratch, and embedded generator JSON files from the deployment container.
 * 3. Validate that total deployment files remain well under the 20,000 limit (~10,125 files).
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { collectRuntimeJsonFiles } = require('./runtime-json-assets.cjs');

const ROOT = path.resolve(__dirname, '..');
const isCloudflare = process.env.CF_PAGES === '1' || process.argv.includes('--force');
const dryRun = process.argv.includes('--dry-run');
const outputArgument = process.argv.find(argument => argument === '--output-dir' || argument.startsWith('--output-dir='));
const outputValue = outputArgument?.includes('=') ? outputArgument.split('=').slice(1).join('=') : (() => {
  const index = process.argv.indexOf('--output-dir');
  return index >= 0 ? process.argv[index + 1] : null;
})();
const deploymentRoot = outputValue ? path.resolve(ROOT, outputValue) : ROOT;
const deploymentRelative = path.relative(ROOT, deploymentRoot);
const stagedOutput = deploymentRoot !== ROOT;

if (stagedOutput && (deploymentRelative.startsWith('..') || path.isAbsolute(deploymentRelative))) {
  throw new Error(`Output directory must be inside the repository: ${outputValue}`);
}

console.log('🚀 [Cloudflare Pages Build] Starting pre-deployment preparation...');

// 1. Run build.js
if (dryRun) {
  console.log('🔎 Dry run requested; skipping asset build and filesystem pruning.');
} else {
  if (stagedOutput && fs.existsSync(deploymentRoot)) {
    fs.rmSync(deploymentRoot, { recursive: true, force: true });
  }
  console.log('📦 Running asset build and cache-buster hashing...');
  try {
    execSync('node build.js', { cwd: ROOT, stdio: 'inherit' });
  } catch (err) {
    console.error('❌ Build failed:', err.message);
    process.exit(1);
  }
}

if (!isCloudflare && !dryRun) {
  console.log('ℹ️  Running locally without --force. Skipping pruning of generator JSON files.');
  console.log('💡 In Cloudflare Pages, set Build Command to: npm run pages:build');
  process.exit(0);
}

console.log(`🧹 Pruning non-production assets for Cloudflare 20,000 file limit${stagedOutput ? ` in ${deploymentRelative}/` : ''}...`);

// Directories to remove completely in the Cloudflare build container
const DIRS_TO_REMOVE = ['node_modules', 'scratch', '__pycache__', '.git'];
if (stagedOutput) DIRS_TO_REMOVE.push('scripts');
const runtimeJsonFiles = collectRuntimeJsonFiles({ root: ROOT });

if (stagedOutput && !dryRun) {
  console.log(`📁 Copying the built site to ${deploymentRelative}/...`);
  fs.mkdirSync(deploymentRoot, { recursive: true });
  for (const entry of fs.readdirSync(ROOT, { withFileTypes: true })) {
    if (['node_modules', 'scratch', '.git', path.basename(deploymentRoot)].includes(entry.name)) continue;
    fs.cpSync(path.join(ROOT, entry.name), path.join(deploymentRoot, entry.name), { recursive: true });
  }
}

const productionRoot = stagedOutput ? deploymentRoot : ROOT;
if (!dryRun) {
  for (const dir of DIRS_TO_REMOVE) {
    const p = path.join(productionRoot, dir);
    if (fs.existsSync(p)) {
      try {
        fs.rmSync(p, { recursive: true, force: true });
        console.log(`  ✓ Removed ${dir}/`);
      } catch (e) {
        console.warn(`  ⚠️ Could not remove ${dir}:`, e.message);
      }
    }
  }
}

console.log(`  ✓ Preserving ${runtimeJsonFiles.size} runtime JSON files.`);

if (dryRun) {
  let jsonFiles = 0;
  let prunableJsonFiles = 0;
  function countJsonFiles(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        if (['.git', 'node_modules', 'scratch'].includes(entry.name)) continue;
        countJsonFiles(full);
      } else if (path.extname(entry.name).toLowerCase() === '.json') {
        jsonFiles++;
        const rel = path.relative(ROOT, full).replace(/\\/g, '/');
        if (!runtimeJsonFiles.has(rel)) prunableJsonFiles++;
      }
    }
  }
  countJsonFiles(ROOT);
  console.log(`  ✓ Dry-run result: ${jsonFiles - prunableJsonFiles} JSON files preserved, ${prunableJsonFiles} generator JSON files would be pruned.`);
  process.exit(0);
}

// Remove generator JSONs and non-essential python files recursively
let removedJsonCount = 0;
let removedPyCount = 0;

function pruneFiles(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === '.git') {
        continue;
      }
      if (entry.name === 'node_modules' || entry.name === 'scratch') {
        fs.rmSync(full, { recursive: true, force: true });
        continue;
      }
      pruneFiles(full);
      // Remove directory if empty
      try {
        if (fs.readdirSync(full).length === 0) {
          fs.rmdirSync(full);
        }
      } catch (e) {}
    } else {
      const ext = path.extname(entry.name).toLowerCase();
      // Keep deployment metadata plus JSON files referenced by runtime pages.
      if (ext === '.json') {
        const rel = path.relative(productionRoot, full).replace(/\\/g, '/');
        if (!runtimeJsonFiles.has(rel)) {
          fs.unlinkSync(full);
          removedJsonCount++;
        }
      } else if (['.py', '.pyc', '.ps1'].includes(ext)) {
        fs.unlinkSync(full);
        removedPyCount++;
      }
    }
  }
}

pruneFiles(productionRoot);
console.log(`  ✓ Pruned ${removedJsonCount} generator JSON files.`);
console.log(`  ✓ Pruned ${removedPyCount} developer scripts.`);

// Count remaining files
function countDeploymentFiles(dir) {
  let count = 0;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      count += countDeploymentFiles(full);
    } else {
      count++;
    }
  }
  return count;
}

const finalFileCount = countDeploymentFiles(productionRoot);
console.log(`\n📊 Final deployment file count: ${finalFileCount} files.`);

if (finalFileCount > 20000) {
  console.error(`❌ ERROR: File count (${finalFileCount}) still exceeds Cloudflare limit of 20,000!`);
  process.exit(1);
} else {
  console.log(`✅ SUCCESS: File count is ${finalFileCount} / 20,000 (safe margin). Ready for Cloudflare Pages deployment!`);
}
