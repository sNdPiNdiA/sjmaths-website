import crypto from 'node:crypto';

export const ahcRoAroLanguageRuntime = {
  bytes: 1484,
  sha256: '827e703b62afcb1ebfa4df198d2b3a321a564573f2997c91b8531ae2b004dac7',
  asset: '/assets/js/ahc-ro-aro-language.js',
  attribute: 'data-ahc-ro-aro-language="shared"',
};
const referenceTag = `<script ${ahcRoAroLanguageRuntime.attribute} src="${ahcRoAroLanguageRuntime.asset}"></script>`;

// Keep the first identical classic-script reference. Its DOMContentLoaded
// callback still sees all later lesson sections, including concatenated pages.
export function deduplicateAhcRoAroLanguageReferences(html) {
  let seen = false;
  let firstTag;
  return html.replace(/(^[\t ]*)?<script\b([^>]*)><\/script>(\r?\n)?/gim, (tag, indentation, attributes, lineEnding) => {
    if (!attributes.includes(ahcRoAroLanguageRuntime.attribute)) return tag;
    const reference = tag.slice(indentation?.length || 0, tag.length - (lineEnding?.length || 0));
    if (!/^<script data-ahc-ro-aro-language="shared" src="\/assets\/js\/ahc-ro-aro-language(?:\.min)?\.js(?:\?v=[a-f0-9]+)?"><\/script>$/.test(reference)) {
      throw new Error('Unexpected AHC RO/ARO language reference; cannot deduplicate.');
    }
    if (seen && reference !== firstTag) throw new Error('Mixed AHC RO/ARO language references; cannot deduplicate.');
    if (seen) return '';
    seen = true;
    firstTag = reference;
    return tag;
  });
}

export function externalizeAhcRoAroLanguageRuntime(html) {
  const references = [...html.matchAll(/<script\b([^>]*)><\/script>/gi)]
    .filter(match => match[1].includes(ahcRoAroLanguageRuntime.attribute));
  if (references.length > 1) throw new Error('Duplicate AHC RO/ARO language runtime references.');
  if (references.length === 1 && !/^<script data-ahc-ro-aro-language="shared" src="\/assets\/js\/ahc-ro-aro-language(?:\.min)?\.js(?:\?v=[a-f0-9]+)?"><\/script>$/.test(references[0][0])) {
    throw new Error('Unexpected AHC RO/ARO language runtime reference.');
  }

  const inline = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(match => !/\bsrc\s*=/i.test(match[1]))
    .filter(match => crypto.createHash('sha256').update(match[2].trim()).digest('hex') === ahcRoAroLanguageRuntime.sha256);
  if (inline.length > 1) throw new Error('Duplicate exact AHC RO/ARO language runtimes.');
  if (inline.length && references.length) throw new Error('Both inline and shared AHC RO/ARO language runtimes exist.');
  if (!inline.length) return html;
  if (Buffer.byteLength(inline[0][2].trim()) !== ahcRoAroLanguageRuntime.bytes) {
    throw new Error('AHC RO/ARO language runtime byte count mismatch.');
  }
  return html.replace(inline[0][0], referenceTag);
}

