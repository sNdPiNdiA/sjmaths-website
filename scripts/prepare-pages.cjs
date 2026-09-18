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

const ROOT = path.resolve(__dirname, '..');
const isCloudflare = process.env.CF_PAGES === '1' || process.argv.includes('--force');

console.log('🚀 [Cloudflare Pages Build] Starting pre-deployment preparation...');

// 1. Run build.js
console.log('📦 Running asset build and cache-buster hashing...');
try {
  execSync('node build.js', { cwd: ROOT, stdio: 'inherit' });
} catch (err) {
  console.error('❌ Build failed:', err.message);
  process.exit(1);
}

if (!isCloudflare) {
  console.log('ℹ️  Running locally without --force. Skipping pruning of generator JSON files.');
  console.log('💡 In Cloudflare Pages, set Build Command to: npm run pages:build');
  process.exit(0);
}

console.log('🧹 Pruning non-production assets and generator JSONs for Cloudflare 20,000 file limit...');

// Directories to remove completely in the Cloudflare build container
const DIRS_TO_REMOVE = ['node_modules', 'scratch', '__pycache__', '.git'];
for (const dir of DIRS_TO_REMOVE) {
  const p = path.join(ROOT, dir);
  if (fs.existsSync(p)) {
    try {
      fs.rmSync(p, { recursive: true, force: true });
      console.log(`  ✓ Removed ${dir}/`);
    } catch (e) {
      console.warn(`  ⚠️ Could not remove ${dir}:`, e.message);
    }
  }
}

// Remove generator JSONs and non-essential python files recursively
let removedJsonCount = 0;
let removedPyCount = 0;

function pruneFiles(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === 'node_modules' || entry.name === 'scratch' || entry.name === '.git') {
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
      // Keep manifest.json and assets/js/search-index.json
      if (ext === '.json') {
        const rel = path.relative(ROOT, full).replace(/\\/g, '/');
        if (rel !== 'manifest.json' && rel !== 'assets/js/search-index.json') {
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

pruneFiles(ROOT);
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

const finalFileCount = countDeploymentFiles(ROOT);
console.log(`\n📊 Final deployment file count: ${finalFileCount} files.`);

if (finalFileCount > 20000) {
  console.error(`❌ ERROR: File count (${finalFileCount}) still exceeds Cloudflare limit of 20,000!`);
  process.exit(1);
} else {
  console.log(`✅ SUCCESS: File count is ${finalFileCount} / 20,000 (safe margin). Ready for Cloudflare Pages deployment!`);
}
