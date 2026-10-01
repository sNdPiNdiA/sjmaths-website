import fs from 'node:fs';

const runtimePath = new URL('../../assets/js/sanskrit-topic.js', import.meta.url);
export const sanskritTopicRuntimeTag = '<script src="/assets/js/sanskrit-topic.js" data-sanskrit-topic-runtime="shared"></script>';
const normalize = source => source.replace(/\r\n/g, '\n').trim();

export function assertSanskritRuntimeTemplate(templateSource) {
  const scripts = [...templateSource.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
  const sharedRuntime = normalize(fs.readFileSync(runtimePath, 'utf8'));
  if (!scripts.some(match => normalize(match[1]) === sharedRuntime)) {
    throw new Error('Sanskrit generator no longer contains the audited shared runtime.');
  }
}

export function externalizeSanskritTopicRuntime(html, runtimeSource, { strict = false } = {}) {
  const runtime = normalize(runtimeSource ?? fs.readFileSync(runtimePath, 'utf8'));
  let matches = 0;
  const output = html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => {
    if (normalize(source) !== runtime) return tag;
    matches++;
    return sanskritTopicRuntimeTag;
  });
  if (strict && matches !== 1) {
    throw new Error(`Expected one exact Sanskrit topic runtime, found ${matches}.`);
  }
  return output;
}

export function hydrateSanskritTopicRuntime(html) {
  const runtime = fs.readFileSync(runtimePath, 'utf8').trim();
  return html.replace(/<script\b([^>]*)>\s*<\/script>/gi, (tag, attributes) =>
    /data-sanskrit-topic-runtime="shared"/.test(attributes) ? `<script>${runtime}</script>` : tag);
}

