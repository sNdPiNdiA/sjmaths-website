import crypto from 'node:crypto';

export const sscCglPolicyTabsRuntime = {
  bytes: 1171,
  sha256: '0265b47f7ef73cbecd18a990bf1e2cbce2fbb13b7769566f52dcab6ae62beefb',
  asset: '/assets/js/ssc-cgl-policy-tabs.js',
  attribute: 'data-ssc-cgl-policy-tabs="shared"',
};

const referenceTag = `<script ${sscCglPolicyTabsRuntime.attribute} src="${sscCglPolicyTabsRuntime.asset}"></script>`;

export function externalizeSscCglPolicyTabs(html) {
  const references = [...html.matchAll(/<script\b([^>]*)><\/script>/gi)]
    .filter(match => match[1].includes(sscCglPolicyTabsRuntime.attribute));
  if (references.length > 1) throw new Error('Duplicate SSC-CGL policy tab runtime references.');
  if (references.length === 1 && references[0][0] !== referenceTag) {
    throw new Error('Unexpected SSC-CGL policy tab runtime reference.');
  }

  const inline = [...html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)]
    .filter(match => !/\bsrc\s*=/i.test(match[1]))
    .filter(match => crypto.createHash('sha256').update(match[2].trim()).digest('hex') === sscCglPolicyTabsRuntime.sha256);
  if (inline.length > 1) throw new Error('Duplicate exact SSC-CGL policy tab controllers.');
  if (inline.length && references.length) throw new Error('Both inline and shared SSC-CGL policy tab controllers exist.');
  if (!inline.length) return html;
  if (Buffer.byteLength(inline[0][2].trim()) !== sscCglPolicyTabsRuntime.bytes) {
    throw new Error('SSC-CGL policy tab controller byte count mismatch.');
  }
  return html.replace(inline[0][0], referenceTag);
}
