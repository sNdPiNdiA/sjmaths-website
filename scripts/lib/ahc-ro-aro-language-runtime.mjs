import crypto from 'node:crypto';

export const ahcRoAroLanguageRuntime = {
  bytes: 1484,
  sha256: '827e703b62afcb1ebfa4df198d2b3a321a564573f2997c91b8531ae2b004dac7',
  asset: '/assets/js/ahc-ro-aro-language.js',
  attribute: 'data-ahc-ro-aro-language="shared"',
};
const referenceTag = `<script ${ahcRoAroLanguageRuntime.attribute} src="${ahcRoAroLanguageRuntime.asset}"></script>`;

export function externalizeAhcRoAroLanguageRuntime(html) {
  const references = [...html.matchAll(/<script\b([^>]*)><\/script>/gi)]
    .filter(match => match[1].includes(ahcRoAroLanguageRuntime.attribute));
  if (references.length > 1) throw new Error('Duplicate AHC RO/ARO language runtime references.');
  if (references.length === 1 && references[0][0] !== referenceTag) {
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

