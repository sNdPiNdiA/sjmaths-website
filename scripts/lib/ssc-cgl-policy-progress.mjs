import crypto from 'node:crypto';

export const sscCglPolicyProgressRuntime = {
  bytes: 2743,
  sha256: 'ee61594bd855370ab95c390d63b64fb22f506724de71c0bcc0570a4c21b02f7e',
  asset: '/assets/js/ssc-cgl-policy-progress.js',
  attribute: 'data-ssc-cgl-policy-progress="shared"',
};
const referenceTag = `<script ${sscCglPolicyProgressRuntime.attribute} src="${sscCglPolicyProgressRuntime.asset}"></script>`;

function hash(source) {
  return crypto.createHash('sha256').update(source).digest('hex');
}

export function externalizeSscCglPolicyProgress(html) {
  const references = [...html.matchAll(/<script\b([^>]*)><\/script>/gi)]
    .filter(match => match[1].includes(sscCglPolicyProgressRuntime.attribute));
  if (references.length > 1) throw new Error('Duplicate SSC-CGL policy progress runtime references.');
  if (references.length === 1 && references[0][0] !== referenceTag) {
    throw new Error('Unexpected SSC-CGL policy progress runtime reference.');
  }

  const inline = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(match => !/\bsrc\s*=/i.test(match[1]))
    .filter(match => hash(match[2].trim()) === sscCglPolicyProgressRuntime.sha256);
  if (inline.length > 1) throw new Error('Duplicate exact SSC-CGL policy progress controllers.');
  if (inline.length && references.length) throw new Error('Both inline and shared SSC-CGL policy progress controllers exist.');
  if (!inline.length) {
    if (references.length === 1) return html;
    return html;
  }

  if (Buffer.byteLength(inline[0][2].trim()) !== sscCglPolicyProgressRuntime.bytes) {
    throw new Error('SSC-CGL policy progress controller byte count mismatch.');
  }
  return html.replace(inline[0][0], referenceTag);
}

