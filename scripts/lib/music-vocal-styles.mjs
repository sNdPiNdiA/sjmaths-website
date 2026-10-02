import { createSharedStyles } from './shared-styles.mjs';

const registry = createSharedStyles('data-music-vocal-topic-style', [['topic', 'music-vocal-topic']]);
export const musicVocalTopicCss = registry.styles[0].css;
export const musicVocalTopicStyleLink = registry.styles[0].link;
export const externalizeMusicVocalStyles = registry.externalize;
export const hydrateMusicVocalStyles = registry.hydrate;

const generatorImport = "import { musicVocalTopicStyleLink } from './lib/music-vocal-styles.mjs';";
const anchor = "import { musicVocalTopicScript } from './lib/music-vocal-runtime.mjs';";

export function externalizeMusicVocalStyleGenerator(source) {
  if (source.includes(generatorImport) && source.split('${musicVocalTopicStyleLink}').length === 2) return source;
  const external = externalizeMusicVocalStyles(source);
  if (external.split(musicVocalTopicStyleLink).length !== 2 || !external.includes(anchor)) {
    throw new Error('Expected one exact Music Vocal generator stylesheet and the maintained runtime import.');
  }
  return external.replace(musicVocalTopicStyleLink, '${musicVocalTopicStyleLink}')
    .replace(anchor, `${anchor}\n${generatorImport}`);
}
