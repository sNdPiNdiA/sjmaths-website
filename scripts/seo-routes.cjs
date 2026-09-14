const fs = require('fs');
const path = require('path');
const { ROOT } = require('./seo-html.cjs');
const DOMAIN = 'https://sjmaths.com';
function readRedirects() {
  return fs.readFileSync(path.join(ROOT, '_redirects'), 'utf8').split(/\r?\n/).map((line, index) => {
    const [source, destination, status] = line.trim().split(/\s+/);
    if (!source?.startsWith('/') || !destination || !/^\d{3}$/.test(status)) return null;
    const keys = [];
    const pattern = source.split(/(:[\w]+|\*)/).map(part => {
      if (part === '*') { keys.push('splat'); return '(.*)'; }
      if (part.startsWith(':')) { keys.push(part.slice(1)); return '([^/]+)'; }
      return part.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }).join('');
    return { source, destination, status: Number(status), regex: new RegExp('^' + pattern + '$'), keys, line: index + 1 };
  }).filter(Boolean);
}
function createResolver(files, rules = readRedirects()) {
  const fileSet = new Set(files);
  const cache = new Map();
  function physical(pathname) {
    const rel = pathname.replace(/^\//, '');
    return [rel || 'index.html', rel + '.html', rel.replace(/\/$/, '') + '/index.html'].find(p => fileSet.has(p));
  }
  function resolve(value, base = DOMAIN + '/') {
    let url;
    try { url = new URL(value, base); } catch { return { invalid: true }; }
    if (!['sjmaths.com', 'www.sjmaths.com'].includes(url.hostname)) return { external: true };
    let pathname;
    try { pathname = decodeURIComponent(url.pathname); } catch { return { invalid: true }; }
    if (cache.has(pathname)) return cache.get(pathname);
    let current = pathname;
    const chain = [];
    const visited = new Set();
    for (let i = 0; i < 15; i++) {
      if (visited.has(current)) return { loop: true, pathname, chain };
      visited.add(current);
      const rule = rules.find(r => r.regex.test(current));
      if (!rule) break;
      const match = current.match(rule.regex);
      const params = Object.fromEntries(rule.keys.map((key, idx) => [key, match[idx + 1]]));
      const destination = rule.destination.replace(/:(\w+)/g, (_, key) => params[key] ?? ':' + key);
      chain.push({ source: current, destination, status: rule.status, line: rule.line });
      current = new URL(destination, DOMAIN).pathname;
      if (rule.status === 200) break;
    }
    const result = { file: physical(current), pathname, redirect: chain.some(r => r.status !== 200) ? current : undefined, chain };
    cache.set(pathname, result);
    return result;
  }
  resolve.physical = physical;
  return resolve;
}
module.exports = { readRedirects, createResolver };
