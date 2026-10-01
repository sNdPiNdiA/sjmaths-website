import { createSharedScripts } from './shared-scripts.mjs';
// English and Geography generators use this exact classic five-tab runtime.
const registry = createSharedScripts('data-exam-topic-runtime', [['topic', 'exam-topic']]);
export const examTopicScript = registry.scripts[0].tag;
export const examTopicRuntime = registry.scripts[0].source;
export const externalizeExamTopicRuntime = registry.externalize;
export const hydrateExamTopicRuntime = registry.hydrate;

