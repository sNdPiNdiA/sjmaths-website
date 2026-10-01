import { createSharedScripts } from './shared-scripts.mjs';

const registry = createSharedScripts('data-hindi-topic-runtime', [['topic', 'hindi-topic']]);
export const hindiTopicRuntime = registry.scripts[0].source;
export const hindiTopicScript = registry.scripts[0].tag;
export const externalizeHindiTopicRuntime = registry.externalize;
export const hydrateHindiTopicRuntime = registry.hydrate;

const generatorImport = "import { hindiTopicScript } from './lib/hindi-topic-runtime.mjs';";
const generatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";

// Normalize a legacy generator source to the intended shared-script form. This
// gives the migration and preservation checker a precise, reversible allowance.
export function normalizeHindiGenerator(source) {
  let normalized = externalizeHindiTopicRuntime(source);
  normalized = normalized.split(hindiTopicScript).join('${hindiTopicScript}');
  if (!normalized.includes(generatorImport)) {
    if (!normalized.includes(generatorImportAnchor)) throw new Error('Hindi generator import anchor not found.');
    normalized = normalized.replace(generatorImportAnchor, `${generatorImportAnchor}\n${generatorImport}`);
  }
  return normalized;
}

export function externalizeHindiGenerator(source) {
  if (source.includes('${hindiTopicScript}') && source.includes(generatorImport)) return source;
  const transformed = normalizeHindiGenerator(source);
  if (!transformed.includes('${hindiTopicScript}') || !transformed.includes(generatorImport)) {
    throw new Error('Hindi generator controller was not externalized exactly once.');
  }
  return transformed;
}
