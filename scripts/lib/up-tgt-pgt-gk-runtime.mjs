import crypto from 'node:crypto';
import fs from 'node:fs';

export const upTgtPgtGkRuntimeSrc = '/assets/js/up-tgt-pgt-gk-topic.js';
export const upTgtPgtGkRuntimeTag = `<script src="${upTgtPgtGkRuntimeSrc}" data-up-tgt-pgt-gk-runtime="topic"></script>`;
export const upTgtPgtGkLanguageRuntimeSrc = '/assets/js/up-tgt-pgt-gk-language.js';
export const upTgtPgtGkLanguageRuntimeTag = `<script src="${upTgtPgtGkLanguageRuntimeSrc}" data-up-tgt-pgt-gk-runtime="language"></script>`;
export const upTgtPgtGkRuntimeSource = fs.readFileSync(new URL('../../assets/js/up-tgt-pgt-gk-topic.js', import.meta.url), 'utf8').trim();
export const legacyUpTgtPgtGkRuntimeHash = 'b9bc6a3d7b2e9eb31c199c19295dbe52dba946197391d4e8c64fcde402a0b461';
export const legacyUpTgtPgtGkLanguageRuntimeHash = 'a2e070d55937ea5f7485a0755d83e9634706bc88a3142c0c541af61573139471';

const translatorImport = "import { upTgtPgtGkRuntimeTag } from './lib/up-tgt-pgt-gk-runtime.mjs';";
const translatorImportAnchor = "import { jsonrepair } from 'jsonrepair';";
const digest = source => crypto.createHash('sha256').update(source).digest('hex');

export function externalizeUpTgtPgtGkTopicRuntime(html, expectedHash = legacyUpTgtPgtGkRuntimeHash) {
  let topicReplacements = 0;
  let languageReplacements = 0;
  const output = html.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (tag, attributes, source) => {
    if (digest(source) === expectedHash) {
      topicReplacements++;
      return upTgtPgtGkRuntimeTag;
    }
    if (attributes.includes('id="bilingual-runtime"') && digest(source) === legacyUpTgtPgtGkLanguageRuntimeHash) {
      languageReplacements++;
      return upTgtPgtGkLanguageRuntimeTag;
    }
    return tag;
  });
  if (topicReplacements > 1 || languageReplacements > 1) throw new Error('Expected at most one of each legacy GK runtime per page.');
  if (!topicReplacements && !languageReplacements && html.includes(upTgtPgtGkRuntimeTag)) return html;
  if (!topicReplacements && !languageReplacements) throw new Error('Expected an exact legacy GK runtime or its shared reference.');
  return output;
}

function normalizeUpTgtPgtGkGenerator(source) {
  let output = source;
  if (!output.includes('${upTgtPgtGkRuntimeTag}')) {
    const runtimePattern = /<script>\s*document\.addEventListener\('DOMContentLoaded',\(\)=>\{/g;
    const starts = [...output.matchAll(runtimePattern)];
    const start = starts[0]?.index ?? -1;
    if (start < 0 || starts.length !== 1) {
      throw new Error('Could not uniquely locate the generator-owned GK inline runtime.');
    }
    const end = output.indexOf('</script>', start);
    if (end < 0 || output.slice(end + 9, end + 25) !== '</body></html>`;') {
      throw new Error('GK runtime is no longer at its expected location in the page template.');
    }
    output = output.slice(0, start) + '${upTgtPgtGkRuntimeTag}' + output.slice(end + 9);
  }
  if (!output.includes(translatorImport)) {
    if (!output.includes(translatorImportAnchor)) throw new Error('GK generator import anchor not found.');
    output = output.replace(translatorImportAnchor, `${translatorImportAnchor}\n${translatorImport}`);
  }
  return output;
}

export function externalizeUpTgtPgtGkGenerator(source) {
  if (source.includes('${upTgtPgtGkRuntimeTag}') && source.includes(translatorImport)) return source;
  const output = normalizeUpTgtPgtGkGenerator(source);
  if ((output.match(/\$\{upTgtPgtGkRuntimeTag\}/g) || []).length !== 1 || !output.includes(translatorImport)) {
    throw new Error('GK generator runtime was not externalized exactly once.');
  }
  return output;
}

export function normalizeUpTgtPgtGkGeneratorForParity(source) {
  return normalizeUpTgtPgtGkGenerator(source);
}
