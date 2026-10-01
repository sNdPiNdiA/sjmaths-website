import fs from 'node:fs';

const stylePath = new URL('../../assets/css/ssc-cgl-topic.css', import.meta.url);
const runtimePath = new URL('../../assets/js/ssc-cgl-topic.js', import.meta.url);
export const sscCglTopicStyleLink = '<link rel="stylesheet" href="/assets/css/ssc-cgl-topic.css" data-ssc-cgl-topic-style="shared">';
export const sscCglTopicRuntimeTag = '<script src="/assets/js/ssc-cgl-topic.js" data-ssc-cgl-topic-runtime="shared"></script>';
const normalize = source => source.replace(/\r\n/g, '\n').trim();
const readSource = (url, supplied) => supplied ?? fs.readFileSync(url, 'utf8');

export function externalizeSscCglTopicAssets(html, styleSource, runtimeSource) {
  const style = normalize(readSource(stylePath, styleSource));
  const runtime = normalize(readSource(runtimePath, runtimeSource));
  const withStyle = html.replace(/<style>([\s\S]*?)<\/style>/gi, (tag, source) => normalize(source) === style ? sscCglTopicStyleLink : tag);
  return withStyle.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => normalize(source) === runtime ? sscCglTopicRuntimeTag : tag);
}

export function hydrateSscCglTopicAssets(html) {
  const style = fs.readFileSync(stylePath, 'utf8').trim();
  const runtime = fs.readFileSync(runtimePath, 'utf8').trim();
  const withScript = html.replace(/<script\b([^>]*)>\s*<\/script>/gi, (tag, attributes) =>
    /data-ssc-cgl-topic-runtime="shared"/.test(attributes) ? `<script>${runtime}</script>` : tag);
  return withScript.replace(/<link\b([^>]*)>/gi, (tag, attributes) =>
    /data-ssc-cgl-topic-style="shared"/.test(attributes) ? `<style>${style}</style>` : tag);
}
