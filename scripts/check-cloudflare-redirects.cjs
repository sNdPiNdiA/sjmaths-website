const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { ROOT } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');

const REDIRECTS_FILE = path.join(ROOT, '_redirects');
const STATIC_LIMIT = 2000;
const DYNAMIC_LIMIT = 100;

function parseRedirects(source) {
  const rules = [];
  const invalid = [];

  source.split(/\r?\n/).forEach((raw, index) => {
    const line = raw.trim();
    if (!line || line.startsWith('#')) return;
    const [sourcePath, destination, status, ...extra] = line.split(/\s+/);
    if (!sourcePath?.startsWith('/') || !destination || !/^\d{3}$/.test(status || '') || extra.length) {
      invalid.push({ line: index + 1, raw });
      return;
    }
    rules.push({
      source: sourcePath,
      destination,
      status: Number(status),
      line: index + 1,
      dynamic: /[:*]/.test(sourcePath),
    });
  });

  return { rules, invalid };
}

function repositoryFiles() {
  return execFileSync('git', ['ls-files', '-co', '--exclude-standard'], {
    cwd: ROOT,
    encoding: 'utf8',
    maxBuffer: 64 * 1024 * 1024,
  }).split(/\r?\n/).filter(Boolean).map(file => file.replace(/\\/g, '/'));
}

function compiledRules(rules) {
  return rules.map(rule => {
    const keys = [];
    const pattern = rule.source.split(/(:[\w]+|\*)/).map(part => {
      if (part === '*') { keys.push('splat'); return '(.*)'; }
      if (part.startsWith(':')) { keys.push(part.slice(1)); return '([^/]+)'; }
      return part.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }).join('');
    return { ...rule, regex: new RegExp('^' + pattern + '$'), keys };
  });
}

function analyzeRedirects(source, files = repositoryFiles()) {
  const { rules, invalid } = parseRedirects(source);
  const staticRules = rules.filter(rule => !rule.dynamic);
  const dynamicRules = rules.filter(rule => rule.dynamic);
  const errors = invalid.map(row => ({ code: 'invalid-rule', ...row }));
  const firstDynamic = rules.findIndex(rule => rule.dynamic);

  if (staticRules.length > STATIC_LIMIT) {
    errors.push({ code: 'static-limit', count: staticRules.length, limit: STATIC_LIMIT });
  }
  if (dynamicRules.length > DYNAMIC_LIMIT) {
    errors.push({ code: 'dynamic-limit', count: dynamicRules.length, limit: DYNAMIC_LIMIT });
  }
  if (firstDynamic !== -1) {
    for (const rule of rules.slice(firstDynamic + 1)) {
      if (!rule.dynamic) errors.push({ code: 'static-after-dynamic', line: rule.line, source: rule.source });
    }
  }

  const seen = new Map();
  for (const rule of rules) {
    if (seen.has(rule.source)) {
      errors.push({ code: 'duplicate-source', source: rule.source, lines: [seen.get(rule.source), rule.line] });
    } else {
      seen.set(rule.source, rule.line);
    }
  }

  const resolve = createResolver(files, compiledRules(rules));
  for (const rule of rules) {
    if (/[:*]/.test(rule.destination) || /^https?:\/\//i.test(rule.destination)) continue;
    const target = resolve(rule.destination);
    if (!target.file) {
      errors.push({
        code: 'missing-destination',
        line: rule.line,
        source: rule.source,
        destination: rule.destination,
        redirect: target.redirect,
      });
    }
  }

  return {
    total: rules.length,
    static: staticRules.length,
    dynamic: dynamicRules.length,
    errors,
  };
}

function main() {
  const result = analyzeRedirects(fs.readFileSync(REDIRECTS_FILE, 'utf8'));
  console.log(JSON.stringify(result, null, 2));
  if (result.errors.length) process.exitCode = 1;
}

if (require.main === module) main();

module.exports = { analyzeRedirects, parseRedirects, STATIC_LIMIT, DYNAMIC_LIMIT };
