#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const { execFileSync, spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..');
const SCRIPTS_DIR = __dirname;
const CONFIG_PATH = path.join(SCRIPTS_DIR, 'config', 'portals.json');

// Detect Python binary: SJ_PYTHON env var > python3 > python > py
function detectPython() {
  if (process.env.SJ_PYTHON) return process.env.SJ_PYTHON;
  if (exists('C:\\Windows\\py.exe')) return 'py';
  // On Windows, `python3` rarely exists; on Linux/macOS, `python` rarely exists.
  if (process.platform === 'win32') return 'python';
  return 'python3';
}

function exists(p) {
  try { return fs.statSync(p).isFile(); } catch { return false; }
}

const PIPELINE = [
  {
    id: 'fetch',
    label: 'Fetch new notifications from official portals',
    cmd: 'node',
    args: [path.join(SCRIPTS_DIR, 'fetch-notifications.js')],
  },
  {
    id: 'download',
    label: 'Download official PDFs',
    cmd: 'node',
    args: [path.join(SCRIPTS_DIR, 'download-pdf.js')],
  },
  {
    id: 'extract',
    label: 'Extract text from PDFs (pdfplumber + Tesseract fallback)',
    cmd: detectPython(),
    args: [path.join(SCRIPTS_DIR, 'extract_pdf.py')],
  },
  {
    id: 'parse',
    label: 'Parse structured fields (regex + heuristics)',
    cmd: 'node',
    args: [path.join(SCRIPTS_DIR, 'parse_fields.js')],
  },
  {
    id: 'generate',
    label: 'Generate job pages and update hub',
    cmd: 'node',
    args: [path.join(SCRIPTS_DIR, 'generate-page.js')],
  },
  {
    id: 'database',
    label: 'Update jobs.json and processed.json',
    cmd: 'node',
    args: [path.join(SCRIPTS_DIR, 'update-database.js')],
  },
  {
    id: 'hub',
    label: 'Regenerate sarkari-jobs hub page',
    cmd: 'node',
    args: [path.join(SCRIPTS_DIR, 'update-hub.js')],
  },
];

function parseArgs(argv) {
  const args = { only: null, dryRun: false, skipMissing: true };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--only') args.only = argv[++i];
    else if (a === '--dry-run') args.dryRun = true;
    else if (a === '--strict') args.skipMissing = false;
  }
  return args;
}

function exists(p) {
  try { return fs.statSync(p).isFile(); } catch { return false; }
}

function runStep(step) {
  if (!exists(step.args[0])) {
    return { ok: false, reason: 'script-missing' };
  }
  console.log(`\n[orchestrator] -> ${step.label}`);
  console.log(`[orchestrator]    ${step.cmd} ${step.args.map(a => (a.includes(' ') ? `"${a}"` : a)).join(' ')}`);
  const result = spawnSync(step.cmd, step.args, { stdio: 'inherit', cwd: ROOT });
  if (result.error) {
    console.error(`[orchestrator] ERROR launching ${step.id}:`, result.error.message);
    return { ok: false, reason: 'launch-failed' };
  }
  if (result.status !== 0) {
    return { ok: false, reason: `exit-${result.status}` };
  }
  return { ok: true };
}

function main() {
  const args = parseArgs(process.argv);

  if (!exists(CONFIG_PATH)) {
    console.error(`[orchestrator] FATAL: portals.json not found at ${CONFIG_PATH}`);
    process.exit(1);
  }

  const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  const enabledPortals = (config.portals || []).filter(p => p.enabled);
  console.log(`[orchestrator] Sarkari Jobs pipeline starting`);
  console.log(`[orchestrator] Portals enabled: ${enabledPortals.length}/${(config.portals || []).length} (${enabledPortals.map(p => p.id).join(', ')})`);

  if (args.dryRun) {
    console.log(`[orchestrator] DRY RUN - listing steps only:`);
    PIPELINE.forEach((s, i) => {
      const present = exists(s.args[0]);
      console.log(`  ${i + 1}. [${present ? 'OK' : 'PENDING'}] ${s.label}`);
    });
    process.exit(0);
  }

  const steps = args.only ? PIPELINE.filter(s => s.id === args.only) : PIPELINE;
  if (steps.length === 0) {
    console.error(`[orchestrator] No pipeline step matches --only=${args.only}`);
    process.exit(1);
  }

  const start = Date.now();
  let failed = null;
  for (const step of steps) {
    const r = runStep(step);
    if (!r.ok) {
      if (r.reason === 'script-missing') {
        if (args.skipMissing) {
          console.warn(`[orchestrator] WARN: ${step.id} script not yet implemented - skipping`);
          continue;
        }
      }
      failed = { step, reason: r.reason };
      break;
    }
  }

  const elapsed = ((Date.now() - start) / 1000).toFixed(1);
  if (failed) {
    console.error(`\n[orchestrator] FAILED at step "${failed.step.id}" (${failed.reason}) after ${elapsed}s`);
    process.exit(1);
  }
  console.log(`\n[orchestrator] Pipeline complete in ${elapsed}s`);
}

main();
