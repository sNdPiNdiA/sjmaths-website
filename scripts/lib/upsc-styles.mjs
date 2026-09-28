import { createSharedStyles } from './shared-styles.mjs';
const registry = createSharedStyles('data-upsc-shared-style', [['microtopic', 'upsc-microtopic']]);
export const upscStyleLink = registry.styles[0].link;
export const upscTopicCss = registry.styles[0].css;
export const hydrateUpscStyles = registry.hydrate;
export const externalizeUpscStyles = registry.externalize;
