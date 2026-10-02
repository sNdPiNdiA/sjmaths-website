import { createSharedScripts } from './shared-scripts.mjs';
import { hasMusicVocalRendererWiring } from './music-vocal-renderer-wiring.mjs';

const registry = createSharedScripts('data-music-vocal-topic-runtime', [['topic', 'music-vocal-topic']]);
export const musicVocalTopicRuntime = registry.scripts[0].source;
export const musicVocalTopicScript = registry.scripts[0].tag;
export const externalizeMusicVocalTopicRuntime = registry.externalize;
export const hydrateMusicVocalTopicRuntime = registry.hydrate;

const generatorImport = "import { musicVocalTopicScript } from './lib/music-vocal-runtime.mjs';";
const generatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";

export function normalizeMusicVocalGenerator(source) {
  let normalized = externalizeMusicVocalTopicRuntime(source);
  normalized = normalized.split(musicVocalTopicScript).join('${musicVocalTopicScript}');
  if (!normalized.includes(generatorImport)) {
    if (!normalized.includes(generatorImportAnchor)) throw new Error('Music Vocal generator import anchor not found.');
    normalized = normalized.replace(generatorImportAnchor, `${generatorImportAnchor}\n${generatorImport}`);
  }
  return normalized;
}

export function externalizeMusicVocalGenerator(source) {
  if (hasMusicVocalRendererWiring(source.replace(/\r\n/g, '\n')) && source.includes(generatorImport)) return source;
  if (source.includes('${musicVocalTopicScript}') && source.includes(generatorImport)) return source;
  const transformed = normalizeMusicVocalGenerator(source);
  if (!transformed.includes('${musicVocalTopicScript}') || !transformed.includes(generatorImport)) {
    throw new Error('Music Vocal generator controller was not externalized exactly once.');
  }
  return transformed;
}
