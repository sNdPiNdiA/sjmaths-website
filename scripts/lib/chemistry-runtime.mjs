import fs from 'node:fs';
import { createSharedScripts } from './shared-scripts.mjs';

// Immutable legacy fixtures are matching/translation adapters, not maintained
// browser implementations. Both modes execute chemistry-topic.js.
export const legacyChemistryEnglish = fs.readFileSync(new URL('../fixtures/chemistry-runtime-legacy.js', import.meta.url), 'utf8').trim();
const languageSnippet = fs.readFileSync(new URL('../fixtures/chemistry-language-legacy.txt', import.meta.url), 'utf8');
const registration = "document.addEventListener('DOMContentLoaded', () => {";
export const legacyChemistryBilingual = legacyChemistryEnglish.replace(registration, registration + languageSnippet);
const registry = createSharedScripts('data-chemistry-runtime', [
  ['english', 'chemistry-topic', legacyChemistryEnglish],
  ['bilingual', 'chemistry-topic', legacyChemistryBilingual],
]);
export const chemistryEnglishScript = registry.scripts[0].tag;
export const chemistryBilingualScript = registry.scripts[1].tag;
export const externalizeChemistryRuntime = registry.externalize;
export const hydrateChemistryRuntime = registry.hydrate;
