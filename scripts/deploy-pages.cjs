#!/usr/bin/env node

const path = require('path');
const { execFileSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const projectArgument = process.argv.find(argument => argument === '--project-name' || argument.startsWith('--project-name='));
const projectFromArgument = projectArgument?.includes('=')
  ? projectArgument.split('=').slice(1).join('=')
  : (() => {
      const index = process.argv.indexOf('--project-name');
      return index >= 0 ? process.argv[index + 1] : null;
    })();
const projectName = projectFromArgument || process.env.CF_PAGES_PROJECT;

if (!projectName) {
  console.error('❌ Set CF_PAGES_PROJECT or pass --project-name before deploying.');
  process.exit(1);
}

const node = process.execPath;
const verifier = path.join(__dirname, 'verify-pages-artifact.cjs');
const wrangler = process.platform === 'win32' ? 'wrangler.cmd' : 'wrangler';

try {
  execFileSync(node, [verifier, '--output-dir', '.pages-dist'], { cwd: ROOT, stdio: 'inherit' });
  execFileSync(wrangler, ['whoami'], { cwd: ROOT, stdio: 'inherit' });
  execFileSync(wrangler, ['pages', 'deploy', '.pages-dist', '--project-name', projectName], { cwd: ROOT, stdio: 'inherit' });
} catch (error) {
  console.error('❌ Pages deployment stopped. Authenticate Wrangler and confirm the project name before retrying.');
  process.exit(error.status || 1);
}
