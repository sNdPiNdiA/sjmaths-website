#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..', '..');
const SCRIPTS_DIR = __dirname;

function fileExists(p) { try { return fs.statSync(p).isFile(); } catch { return false; } }
function dirExists(p) { try { return fs.statSync(p).isDirectory(); } catch { return false; } }

function detectPython() {
  if (process.env.SJ_PYTHON) return process.env.SJ_PYTHON;
  if (process.platform === 'win32') return 'python';
  return 'python3';
}

const PYTHON = detectPython();

const STEPS = [
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
    cmd: PYTHON,
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
    label: 'Generate job pages',
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
  const args = { only: null, dryRun: false, strict: false, start: null };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--only') args.only = argv[++i];
    else if (a === '--from') args.start = argv[++i];
    else if (a === '--dry-run') args.dryRun = true;
    else if (a === '--strict') args.strict = true;
    else if (a === '--help' || a === '-h') {
      console.log('Usage: node orchestrator.js [--only <step>] [--from <step>] [--dry-run] [--strict]');
      console.log('Steps: ' + STEPS.map(s => s.id).join(', '));
      process.exit(0);
    }
  }
  return args;
}

function runStep(step) {
  if (!fileExists(step.args[0])) {
    return { ok: false, reason: 'script-missing', path: step.args[0] };
  }
  console.log(`\n[orchestrator] -> ${step.label}`);
  const pretty = `${step.cmd} ${step.args.map(a => /\s/.test(a) ? `"${a}"` : a).join(' ')}`;
  console.log(`[orchestrator]    ${pretty}`);
  const started = Date.now();
  const result = spawnSync(step.cmd, step.args, { stdio: 'inherit', cwd: ROOT });
  const elapsed = ((Date.now() - started) / 1000).toFixed(1);
  if (result.error) {
    console.error(`[orchestrator] ERROR launching ${step.id}: ${result.error.message}`);
    return { ok: false, reason: 'launch-failed' };
  }
  if (result.status !== 0) {
    return { ok: false, reason: `exit-${result.status}`, elapsed };
  }
  console.log(`[orchestrator]    step "${step.id}" OK (${elapsed}s)`);
  return { ok: true, elapsed };
}

function main() {
  const args = parseArgs(process.argv);

  // Print a brief environment summary for log clarity
  console.log(`[orchestrator] Sarkari Jobs pipeline starting`);
  console.log(`[orchestrator] platform=${process.platform} node=${process.version} python=${PYTHON}`);
  console.log(`[orchestrator] cwd=${ROOT}`);

  if (args.dryRun) {
    console.log(`\n[orchestrator] DRY RUN - listing ${STEPS.length} steps:`);
    for (const s of STEPS) {
      const present = fileExists(s.args[0]);
      console.log(`  ${present ? 'OK    ' : 'MISS  '} ${s.id.padEnd(10)} ${s.label}`);
    }
    process.exit(0);
  }

  let steps = STEPS;
  if (args.only) {
    steps = STEPS.filter(s => s.id === args.only);
    if (steps.length === 0) {
      console.error(`[orchestrator] No step matches --only=${args.only}. Available: ${STEPS.map(s => s.id).join(', ')}`);
      process.exit(1);
    }
  } else if (args.start) {
    const idx = STEPS.findIndex(s => s.id === args.start);
    if (idx < 0) {
      console.error(`[orchestrator] No step matches --from=${args.start}. Available: ${STEPS.map(s => s.id).join(', ')}`);
      process.exit(1);
    }
    steps = STEPS.slice(idx);
  }

  const t0 = Date.now();
  let failed = null;
  for (const step of steps) {
    const r = runStep(step);
    if (!r.ok) {
      if (r.reason === 'script-missing' && !args.strict) {
        console.warn(`[orchestrator] WARN: ${step.id} script not found at ${r.path} - skipping`);
        continue;
      }
      failed = { step, reason: r.reason };
      break;
    }
  }

  const totalElapsed = ((Date.now() - t0) / 1000).toFixed(1);
  if (failed) {
    console.error(`\n[orchestrator] FAILED at step "${failed.step.id}" (${failed.reason}) after ${totalElapsed}s`);
    process.exit(1);
  }
  console.log(`\n[orchestrator] Pipeline complete in ${totalElapsed}s`);
}

main();
