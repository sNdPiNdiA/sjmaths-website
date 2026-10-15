import fs from 'node:fs';
import { createSharedScripts } from './shared-scripts.mjs';

const legacyFixtureUrl = new URL('../fixtures/upsc-language-legacy.js', import.meta.url);
const legacySource = fs.readFileSync(legacyFixtureUrl, 'utf8').trim();

const registry = createSharedScripts('data-upsc-shared-script', [['language', 'upsc-language', legacySource]]);
export const upscLanguageScript = registry.scripts[0].tag;
export const upscLanguageSource = registry.scripts[0].source;
export const externalizeUpscLanguage = registry.externalize;
export const hydrateUpscLanguage = registry.hydrate;
