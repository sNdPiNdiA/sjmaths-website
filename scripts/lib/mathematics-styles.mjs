import { createSharedStyles } from './shared-styles.mjs';

const registry = createSharedStyles('data-mathematics-shared-style', [['topic', 'mathematics-topic']]);
export const mathematicsTopicStyleLink = registry.styles[0].link
  .replace('/assets/css/mathematics-topic.css', '/assets/css/mathematics-topic.min.css?v=4472833c');
export const mathematicsTopicCss = registry.styles[0].css;
export const hydrateMathematicsStyles = registry.hydrate;
export const externalizeMathematicsStyles = html => registry.externalize(html)
  .replace(registry.styles[0].link, mathematicsTopicStyleLink);

const generatorImport = "import { mathematicsTopicStyleLink } from './lib/mathematics-styles.mjs';";
const generatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";

export function normalizeMathematicsGenerator(source) {
  let normalized = externalizeMathematicsStyles(source);
  normalized = normalized.split(mathematicsTopicStyleLink).join('${mathematicsTopicStyleLink}');
  if (!normalized.includes(generatorImport)) {
    if (!normalized.includes(generatorImportAnchor)) throw new Error('Mathematics generator import anchor not found.');
    normalized = normalized.replace(generatorImportAnchor, `${generatorImportAnchor}\n${generatorImport}`);
  }
  return normalized;
}

export function externalizeMathematicsGenerator(source) {
  if (source.includes('${mathematicsTopicStyleLink}') && source.includes(generatorImport)) return source;
  const transformed = normalizeMathematicsGenerator(source);
  if (!transformed.includes('${mathematicsTopicStyleLink}') || !transformed.includes(generatorImport)) {
    throw new Error('Mathematics topic stylesheet was not externalized exactly once.');
  }
  return transformed;
}
