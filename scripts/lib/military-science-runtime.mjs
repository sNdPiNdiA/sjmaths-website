import crypto from 'node:crypto';
import { createSharedScripts } from './shared-scripts.mjs';

const registry = createSharedScripts('data-military-science-topic-runtime', [['topic', 'military-science-topic']]);
export const militaryScienceTopicRuntime = registry.scripts[0].source;
export const militaryScienceTopicScript = registry.scripts[0].tag;
const legacyRuntimeHash = '8f5ee57ade655216cdbdae553523b3e3cd52634bd09989dd014b9cf0053a785d';
const normalize = source => source.replace(/\r\n/g, '\n').trim();
const sourceHash = source => crypto.createHash('sha256').update(normalize(source)).digest('hex');

export const externalizeMilitaryScienceTopicRuntime = html => {
  const current = registry.externalize(html);
  return current.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attrs, source) =>
    !/\b(?:async|defer|type|src)\b/i.test(attrs) && sourceHash(source) === legacyRuntimeHash
      ? militaryScienceTopicScript : tag);
};
export const hydrateMilitaryScienceTopicRuntime = registry.hydrate;

const generatorImport = "import { militaryScienceTopicScript } from './lib/military-science-runtime.mjs';";
const generatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";

export function normalizeMilitaryScienceGenerator(source) {
  let normalized = externalizeMilitaryScienceTopicRuntime(source);
  normalized = normalized.split(militaryScienceTopicScript).join('${militaryScienceTopicScript}');
  if (!normalized.includes(generatorImport)) {
    if (!normalized.includes(generatorImportAnchor)) throw new Error('Military Science generator import anchor not found.');
    normalized = normalized.replace(generatorImportAnchor, `${generatorImportAnchor}\n${generatorImport}`);
  }
  return normalized;
}

export function externalizeMilitaryScienceGenerator(source) {
  if (source.includes('${militaryScienceTopicScript}') && source.includes(generatorImport)) return source;
  const transformed = normalizeMilitaryScienceGenerator(source);
  if (!transformed.includes('${militaryScienceTopicScript}') || !transformed.includes(generatorImport)) {
    throw new Error('Military Science generator controller was not externalized exactly once.');
  }
  return transformed;
}
