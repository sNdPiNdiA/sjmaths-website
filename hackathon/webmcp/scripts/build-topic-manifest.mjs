#!/usr/bin/env node
/**
 * build-topic-manifest.mjs
 *
 * Scans learning/topics/ and generates learning/topics/index.json — the
 * single source of truth the webmcp demo uses to populate its chapter
 * selector. Run this whenever topics are added/removed/renamed:
 *
 *   node hackathon/webmcp/scripts/build-topic-manifest.mjs
 *
 * A "topic" is a directory containing <name>/<name>.json. Topics are grouped
 * by their parent directory (e.g. class-10/mathematics/chapter-4-quadratic-equations
 * or foundations/mathematics/algebra).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const topicsRoot = path.join(repoRoot, 'learning', 'topics');
const outFile = path.join(topicsRoot, 'index.json');

/** Recursively collect directories that directly contain topic JSON files. */
function findTopicDirs(dir) {
  const found = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    const full = path.join(dir, entry.name);
    const hasOwnJson = fs.existsSync(path.join(full, `${entry.name}.json`));
    if (hasOwnJson) {
      found.push(full);
    } else {
      found.push(...findTopicDirs(full));
    }
  }
  return found;
}

/** Derive a display title for a group from its topic metadata + dir name. */
const STRAND_LABELS = { proof: 'Proof & Data' };
function groupTitle(basePath, key, topicMeta) {
  if (basePath.startsWith('foundations')) {
    // e.g. basePath .../foundations/mathematics/arithmetic -> "Foundations · Arithmetic"
    const strand = basePath.split('/').pop();
    return `Foundations · ${STRAND_LABELS[strand] || (strand.charAt(0).toUpperCase() + strand.slice(1))}`;
  }
  // e.g. dir "chapter-4-quadratic-equations" -> "Chapter 4: Quadratic Equations"
  // Strip a redundant "Chapter N -/:" prefix if topic.chapter metadata has one.
  const m = key.match(/^chapter-(\d+)-(.*)$/);
  let name = (topicMeta.chapter || (m ? m[2] : key)).trim();
  if (m) name = name.replace(/^chapter\s*\d+\s*[-–—:]?\s*/i, '') || m[2];
  return m ? `Chapter ${m[1]}: ${name}` : name;
}

const topicDirs = findTopicDirs(topicsRoot);
if (topicDirs.length === 0) {
  console.error('No topic directories found under', topicsRoot);
  process.exit(1);
}

const groupsByPath = new Map();
for (const topicDir of topicDirs) {
  const topicId = path.basename(topicDir);
  const basePath = path.relative(topicsRoot, topicDir).split(path.sep).slice(0, -1).join('/');

  let raw;
  try {
    raw = JSON.parse(fs.readFileSync(path.join(topicDir, `${topicId}.json`), 'utf8'));
  } catch (err) {
    console.warn(`  ! skipping ${topicId}: unreadable JSON (${err.message})`);
    continue;
  }
  const meta = raw.topic || {};

  const gKey = basePath.split('/').pop();
  if (!groupsByPath.has(basePath)) {
    const isFoundations = basePath.startsWith('foundations');
    groupsByPath.set(basePath, {
      key: isFoundations ? `foundations-${gKey}` : gKey,
      basePath,
      title: groupTitle(basePath, gKey, meta),
      category: isFoundations ? 'foundations' : 'cbse-class-10',
      topics: []
    });
  }
  groupsByPath.get(basePath).topics.push({
    id: topicId,
    title: meta.title || topicId,
    short_title: meta.short_title || meta.title || topicId
  });
}

// Sort topics alphabetically within each group, then order groups:
// CBSE Class 10 chapters by number first, Foundations strands after.
const groups = [...groupsByPath.values()];
groups.forEach(g => g.topics.sort((a, b) => a.id.localeCompare(b.id)));
groups.sort((a, b) => {
  const catRank = (g) => (g.category === 'cbse-class-10' ? 0 : 1);
  if (catRank(a) !== catRank(b)) return catRank(a) - catRank(b);
  return a.key.localeCompare(b.key, undefined, { numeric: true });
});

const manifest = {
  schema_version: 1,
  generated_at: new Date().toISOString(),
  source: 'learning/topics',
  groups
};

fs.writeFileSync(outFile, JSON.stringify(manifest, null, 2) + '\n');
console.log(`Wrote ${outFile}`);
console.log(`  ${groups.length} groups, ${groups.reduce((n, g) => n + g.topics.length, 0)} topics`);
for (const g of groups) {
  console.log(`  - ${g.key} (${g.topics.length} topics)`);
}
