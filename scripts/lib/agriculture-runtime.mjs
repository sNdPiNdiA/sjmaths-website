import { createSharedScripts } from './shared-scripts.mjs';
// Keep both established variants: generated and redesigned pages have different
// quiz selectors, feedback classes and scroll offsets. Do not merge semantics.
const registry = createSharedScripts('data-agriculture-runtime', [
  ['generated', 'agriculture-generated'],
  ['redesigned', 'agriculture-topic'],
]);
export const agricultureGeneratedScript = registry.scripts[0].tag;
export const agricultureRedesignedScript = registry.scripts[1].tag;
export const agricultureGeneratedRuntime = registry.scripts[0].source;
export const agricultureRedesignedRuntime = registry.scripts[1].source;
export const externalizeAgricultureRuntime = registry.externalize;
export const hydrateAgricultureRuntime = registry.hydrate;
