import { createSharedScripts } from './shared-scripts.mjs';

// These two classic controllers are shared by ASO topic and test pages. Keep
// them at their original parser-blocking DOM position during extraction.
const registry = createSharedScripts('data-aso-topic-runtime', [
  ['feedback', 'aso-topic-feedback'],
  ['tabs', 'aso-topic-tabs'],
]);
export const asoTopicScriptTags = registry.scripts.map(script => script.tag);
export const asoTopicRuntimes = registry.scripts;
const legacyIds = new Map([
  ['universal-quiz-feedback', registry.scripts[0]],
  ['universal-tab-engine', registry.scripts[1]],
]);
const normalize = source => source.replace(/\r\n/g, '\n').trim();
export const externalizeAsoTopicRuntimes = html => html.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attrs, source) => {
  if (/\b(?:async|defer|type|src)\b/i.test(attrs)) return tag;
  const id = attrs.match(/\bid=["']([^"']+)["']/i)?.[1];
  const runtime = legacyIds.get(id);
  return runtime && normalize(runtime.source) === normalize(source) ? runtime.tag : tag;
});
export const hydrateAsoTopicRuntimes = registry.hydrate;
