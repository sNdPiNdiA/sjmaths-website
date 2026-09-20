const fs = require('fs');
const path = require('path');

function collectRuntimeJsonFiles({ root = path.resolve(__dirname, '..') } = {}) {
  const preserved = new Set(['manifest.json', 'assets/js/search-index.json']);
  const sources = [];

  function collect(dir) {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      const relative = path.relative(root, full).replace(/\\/g, '/');
      if (entry.isDirectory()) {
        if (['.git', 'node_modules', 'scratch', '.pages-dist', 'scripts'].includes(entry.name)) continue;
        collect(full);
        continue;
      }
      if (entry.name.endsWith('.html') || entry.name.endsWith('.js')) {
        sources.push({ relative, source: fs.readFileSync(full, 'utf8') });
      }
    }
  }

  collect(root);
  const referencePattern = /["'`]([^"'`]*?\.json(?:[?#][^"'`]*)?)["'`]/gi;
  const addReference = (reference, sourceFile) => {
    const clean = reference.split(/[?#]/, 1)[0].replace(/\\/g, '/');
    if (!clean || /^(?:https?:|\/\/|data:|blob:)/i.test(clean)) return;
    const candidate = clean.startsWith('/')
      ? clean.slice(1)
      : path.posix.normalize(path.posix.join(path.posix.dirname(sourceFile), clean));
    if (!candidate || candidate.startsWith('../')) return;
    const absolute = path.join(root, candidate);
    if (fs.existsSync(absolute) && fs.statSync(absolute).isFile()) preserved.add(candidate);
  };

  for (const { relative, source } of sources) {
    for (const match of source.matchAll(referencePattern)) addReference(match[1], relative);
    if (/questions-loader(?:\.min)?\.js/i.test(source)) addReference('questions.json', relative);
  }
  return preserved;
}

module.exports = { collectRuntimeJsonFiles };
