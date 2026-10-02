// Recognize only the maintained CLI wrapper, not a loose function-name marker.
export function hasMusicVocalRendererWiring(source) {
  return source.includes("import { compileMusicVocalHtml } from './lib/music-vocal-renderer.mjs';") &&
    source.includes('function compileHtml(content, questions, context) {\n  return compileMusicVocalHtml(content, questions, context, { musicVocalTopicScript, musicVocalTopicStyleLink });\n}');
}
