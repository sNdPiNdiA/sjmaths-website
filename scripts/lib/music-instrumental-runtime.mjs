import crypto from 'node:crypto';
import { createSharedScripts } from './shared-scripts.mjs';

const registry = createSharedScripts('data-music-instrumental-topic-runtime', [['topic', 'music-instrumental-topic']]);
export const musicInstrumentalTopicRuntime = registry.scripts[0].source;
export const musicInstrumentalTopicScript = registry.scripts[0].tag;
const legacyRuntimeHash = '56e09a65d8c304716a236287e3f81942626838914a8c1bb739a8b8729f61c1f0';
const normalize = source => source.replace(/\r\n/g, '\n').trim();
const legacyHash = source => crypto.createHash('sha256').update(normalize(source)).digest('hex');
export const externalizeMusicInstrumentalTopicRuntime = html => {
  const current = registry.externalize(html);
  return current.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attrs, source) =>
    !/\b(?:async|defer|type|src)\b/i.test(attrs) && legacyHash(source) === legacyRuntimeHash
      ? musicInstrumentalTopicScript : tag);
};
export const hydrateMusicInstrumentalTopicRuntime = registry.hydrate;

const generatorImport = "import { musicInstrumentalTopicScript } from './lib/music-instrumental-runtime.mjs';";
const generatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";

export function normalizeMusicInstrumentalGenerator(source) {
  let normalized = externalizeMusicInstrumentalTopicRuntime(source);
  normalized = normalized.split(musicInstrumentalTopicScript).join('${musicInstrumentalTopicScript}');
  if (!normalized.includes(generatorImport)) {
    if (!normalized.includes(generatorImportAnchor)) throw new Error('Music Instrumental generator import anchor not found.');
    normalized = normalized.replace(generatorImportAnchor, `${generatorImportAnchor}\n${generatorImport}`);
  }
  return normalized;
}

export function externalizeMusicInstrumentalGenerator(source) {
  if (source.includes('${musicInstrumentalTopicScript}') && source.includes(generatorImport)) return source;
  const transformed = normalizeMusicInstrumentalGenerator(source);
  if (!transformed.includes('${musicInstrumentalTopicScript}') || !transformed.includes(generatorImport)) {
    throw new Error('Music Instrumental generator controller was not externalized exactly once.');
  }
  return transformed;
}
