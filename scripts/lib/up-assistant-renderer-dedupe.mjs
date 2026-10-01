import fs from 'node:fs';
import crypto from 'node:crypto';

const sharedReference = /<script\b(?=[^>]*\bdata-up-assistant-tabs-runtime=["']shared["'])[^>]*>\s*<\/script\s*>/gi;
const normalize = source => source.replace(/\r\n/g, '\n').trim();
const expectedFingerprint = '87c3fb8fe6b1956704e72b5920f0715525722f7da6452c940a3bc57cd24e1e2e';

export function extractUpAssistantDuplicateRuntime(html) {
  const candidates = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => normalize(match[1]));
  const runtime = candidates.find(source => Buffer.byteLength(source) === 1031
    && crypto.createHash('sha256').update(source).digest('hex') === expectedFingerprint);
  if (!runtime) throw new Error('The audited 1,031-byte UP Assistant duplicate runtime was not found.');
  return runtime;
}

export function getUpAssistantDuplicateRuntime() {
  const assetPath = new URL('../../assets/js/up-assistant-tabs.js', import.meta.url);
  if (!fs.existsSync(assetPath)) throw new Error('Runtime asset is absent; retrieve the exact source from the Git baseline.');
  const runtime = normalize(fs.readFileSync(assetPath, 'utf8'));
  const digest = crypto.createHash('sha256').update(runtime).digest('hex');
  if (Buffer.byteLength(runtime) !== 1031 || digest !== expectedFingerprint) {
    throw new Error(`UP Assistant duplicate runtime changed (bytes=${Buffer.byteLength(runtime)}, sha256=${digest}).`);
  }
  return runtime;
}

export function removeUpAssistantDuplicateRuntime(html, runtimeSource, { strict = false } = {}) {
  if (!runtimeSource) throw new Error('Exact duplicate source is required for safe removal.');
  const runtime = normalize(runtimeSource);
  let inlineMatches = 0;
  const withoutInline = html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => {
    if (normalize(source) !== runtime) return tag;
    inlineMatches++;
    return '';
  });
  let referenceMatches = 0;
  const output = withoutInline.replace(sharedReference, () => {
    referenceMatches++;
    return '';
  });
  if (strict && inlineMatches + referenceMatches !== 1) {
    throw new Error(`Expected one exact redundant UP Assistant runtime, found ${inlineMatches + referenceMatches}.`);
  }
  return output;
}
