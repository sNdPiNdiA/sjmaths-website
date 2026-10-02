import crypto from 'node:crypto';

export const sscCglPolicyMiniTestRuntime = {
  bytes: 2673,
  sha256: 'afcba0bfde91bb3ad9a31d4cc04d7160546d177ef708f4386ee394f6f0b6bd0a',
  asset: '/assets/js/ssc-cgl-policy-mini-test.js',
  attribute: 'data-ssc-cgl-policy-mini-test="shared"',
};
const referenceTag = `<script ${sscCglPolicyMiniTestRuntime.attribute} src="${sscCglPolicyMiniTestRuntime.asset}"></script>`;

export function externalizeSscCglPolicyMiniTest(html) {
  const references = [...html.matchAll(/<script\b([^>]*)><\/script>/gi)]
    .filter(match => match[1].includes(sscCglPolicyMiniTestRuntime.attribute));
  if (references.length > 1) throw new Error('Duplicate SSC-CGL policy mini-test runtime references.');
  if (references.length === 1 && references[0][0] !== referenceTag) {
    throw new Error('Unexpected SSC-CGL policy mini-test runtime reference.');
  }

  const inline = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(match => !/\bsrc\s*=/i.test(match[1]))
    .filter(match => crypto.createHash('sha256').update(match[2].trim()).digest('hex') === sscCglPolicyMiniTestRuntime.sha256);
  if (inline.length > 1) throw new Error('Duplicate exact SSC-CGL policy mini-test controllers.');
  if (inline.length && references.length) throw new Error('Both inline and shared SSC-CGL policy mini-test controllers exist.');
  if (!inline.length) return html;
  if (Buffer.byteLength(inline[0][2].trim()) !== sscCglPolicyMiniTestRuntime.bytes) {
    throw new Error('SSC-CGL policy mini-test controller byte count mismatch.');
  }
  return html.replace(inline[0][0], referenceTag);
}

