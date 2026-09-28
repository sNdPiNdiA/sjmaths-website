import { createSharedStyles } from './shared-styles.mjs';

const registry = createSharedStyles('data-history-shared-style', [
  ['topic', 'history-topic'],
  ['expanded', 'history-topic-expanded'],
  ['legacy', 'history-legacy'],
]);
export const historyStyles = registry.styles;
export const historyStyleLink = historyStyles[0].link;
export const historyTopicCss = historyStyles[0].css;
export const hydrateHistoryStyles = registry.hydrate;
export const externalizeHistoryStyles = registry.externalize;
