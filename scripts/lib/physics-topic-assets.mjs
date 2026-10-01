import fs from 'node:fs';

const stylePath = new URL('../../assets/css/physics-topic.css', import.meta.url);
const runtimePath = new URL('../../assets/js/physics-topic.js', import.meta.url);
export const physicsTopicStyleLink = '<link rel="stylesheet" href="/assets/css/physics-topic.css" data-physics-topic-style="lesson">';
export const physicsTopicRuntimeTag = '<script src="/assets/js/physics-topic.js" data-physics-topic-runtime="lesson"></script>';
const normalize = source => source.replace(/\r\n/g, '\n').trim();

const readSource = (url, supplied) => supplied ?? fs.readFileSync(url, 'utf8');

export function externalizePhysicsTopicAssets(html, styleSource, runtimeSource) {
  const style = normalize(readSource(stylePath, styleSource));
  const runtime = normalize(readSource(runtimePath, runtimeSource));
  const withStyle = html.replace(/<style>([\s\S]*?)<\/style>/gi, (tag, source) => normalize(source) === style ? physicsTopicStyleLink : tag);
  return withStyle.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => normalize(source) === runtime ? physicsTopicRuntimeTag : tag);
}

export function hydratePhysicsTopicAssets(html) {
  const style = fs.readFileSync(stylePath, 'utf8').trim();
  const runtime = fs.readFileSync(runtimePath, 'utf8').trim();
  const withScript = html.replace(/<script\b([^>]*)>\s*<\/script>/gi, (tag, attributes) =>
    /data-physics-topic-runtime="lesson"/.test(attributes) ? `<script>${runtime}</script>` : tag);
  return withScript.replace(/<link\b([^>]*)>/gi, (tag, attributes) =>
    /data-physics-topic-style="lesson"/.test(attributes) ? `<style>${style}</style>` : tag);
}

export function externalizePhysicsTopicGenerator(source, styleSource, runtimeSource) {
  return externalizePhysicsTopicAssets(source, styleSource, runtimeSource);
}
