import { createSharedStyles } from './shared-styles.mjs';
const registry = createSharedStyles('data-aso-shared-style', [['lesson', 'aso-lesson']]);
export const asoStyleLink = registry.styles[0].link;
export const asoLessonCss = registry.styles[0].css;
export const hydrateAsoStyles = registry.hydrate;
export const externalizeAsoStyles = registry.externalize;
