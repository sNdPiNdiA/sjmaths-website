const fs = require('fs');
const path = require('path');

function collectRuntimeJsonFiles({ root = path.resolve(__dirname, '..') } = {}) {
  const preserved = new Set([
    'manifest.json',
    'assets/js/search-index.json',
    '.well-known/assetlinks.json',
  ]);
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

    // UPSC pages can load tab payloads by constructing tabs/<key>.json at
    // runtime. Those URLs are not literal references for the general scanner,
    // so derive the dependencies from the page's embedded data instead.
    if (relative.startsWith('upsc/') && relative.endsWith('.html') && source.includes('upsc-page-data')) {
      const pageDataPattern = /<script\b([^>]*)>([\s\S]*?)<\/script\s*>/gi;
      for (const match of source.matchAll(pageDataPattern)) {
        if (!/\bid\s*=\s*["']upsc-page-data["']/i.test(match[1])) continue;
        let pageData;
        try {
          pageData = JSON.parse(match[2]);
        } catch (error) {
          throw new Error(`Unable to parse embedded UPSC page data in ${relative}: ${error.message}`);
        }
        if (!Array.isArray(pageData.tabs)) continue;
        for (const tab of pageData.tabs) {
          if (typeof tab !== 'string' || pageData[tab]) continue;
          const sidecar = path.posix.join(path.posix.dirname(relative), 'tabs', `${tab}.json`);
          const absolute = path.join(root, sidecar);
          if (fs.existsSync(absolute) && fs.statSync(absolute).isFile()) preserved.add(sidecar);
        }
        break;
      }
    }
  }

  function collectManifestReferences(value, sourceFile) {
    if (typeof value === 'string') {
      if (/\.json(?:[?#]|$)/i.test(value)) addReference(value, sourceFile);
      return;
    }
    if (Array.isArray(value)) {
      for (const item of value) collectManifestReferences(item, sourceFile);
      return;
    }
    if (value && typeof value === 'object') {
      for (const item of Object.values(value)) collectManifestReferences(item, sourceFile);
    }
  }

  for (const manifestPath of [...preserved].filter(file => /(?:^|\/)manifest\.json$/i.test(file))) {
    const manifestFile = path.join(root, manifestPath);
    if (!fs.existsSync(manifestFile)) continue;
    try {
      collectManifestReferences(JSON.parse(fs.readFileSync(manifestFile, 'utf8')), manifestPath);
    } catch {
      // Some deployment manifests are not JSON documents; preserve the manifest itself only.
    }
  }

  return preserved;
}

module.exports = { collectRuntimeJsonFiles };
