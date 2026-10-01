import { createSharedStyles } from './shared-styles.mjs';

const registry = createSharedStyles('data-pe-topic-style', [['topic', 'physical-education-topic']]);

export const physicalEducationTopicStyleLink = registry.styles[0].link;
export const physicalEducationTopicCss = registry.styles[0].css;
export const hydratePhysicalEducationStyles = registry.hydrate;
export const externalizePhysicalEducationStyles = registry.externalize;

const translatorImport = "import { physicalEducationTopicStyleLink } from './lib/physical-education-styles.mjs';";
const translatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";

export function normalizePhysicalEducationTranslator(source) {
  let normalized = externalizePhysicalEducationStyles(source);
  normalized = normalized.split(physicalEducationTopicStyleLink).join('${physicalEducationTopicStyleLink}');
  if (!normalized.includes(translatorImport)) {
    if (!normalized.includes(translatorImportAnchor)) throw new Error('Physical Education translator import anchor not found.');
    normalized = normalized.replace(translatorImportAnchor, `${translatorImportAnchor}\n${translatorImport}`);
  }
  return normalized;
}

export function externalizePhysicalEducationTranslator(source) {
  if (source.includes('${physicalEducationTopicStyleLink}') && source.includes(translatorImport)) return source;
  const transformed = normalizePhysicalEducationTranslator(source);
  if (!transformed.includes('${physicalEducationTopicStyleLink}') || !transformed.includes(translatorImport)) {
    throw new Error('Physical Education topic stylesheet was not externalized exactly once.');
  }
  return transformed;
}
