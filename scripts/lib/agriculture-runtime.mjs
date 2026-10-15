import fs from 'node:fs';
import { createSharedScripts } from './shared-scripts.mjs';

// Immutable legacy fixtures are matching/translation adapters, not maintained
// browser implementations. Both modes execute maintained assets/js runtimes.
export const legacyAgricultureGenerated = fs.readFileSync(new URL('../fixtures/agriculture-generated-legacy.js', import.meta.url), 'utf8').trim();
export const legacyAgricultureRedesigned = fs.readFileSync(new URL('../fixtures/agriculture-topic-legacy.js', import.meta.url), 'utf8').trim();

const registry = createSharedScripts('data-agriculture-runtime', [
  ['generated', 'agriculture-generated', legacyAgricultureGenerated],
  ['redesigned', 'agriculture-topic', legacyAgricultureRedesigned],
]);

export const agricultureGeneratedScript = registry.scripts[0].tag;
export const agricultureRedesignedScript = registry.scripts[1].tag;
export const agricultureGeneratedRuntime = registry.scripts[0].source;
export const agricultureRedesignedRuntime = registry.scripts[1].source;
export const externalizeAgricultureRuntime = registry.externalize;
export const hydrateAgricultureRuntime = registry.hydrate;
