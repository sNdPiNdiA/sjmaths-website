import { createSharedScripts } from './shared-scripts.mjs';
const registry = createSharedScripts('data-upsc-shared-script', [['language', 'upsc-language']]);
export const upscLanguageScript = registry.scripts[0].tag;
export const upscLanguageSource = registry.scripts[0].source;
export const externalizeUpscLanguage = registry.externalize;
