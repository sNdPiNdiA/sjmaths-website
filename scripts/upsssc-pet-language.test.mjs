import test from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { ROOT } from './seo-html.cjs';
import { hydrateUpscLanguage, upscLanguageSource } from './lib/upsc-language.mjs';
import {
  externalizeUpssscPetLanguage,
  validateUpssscPetLegacyLanguage,
} from './lib/upsssc-pet-language.mjs';

const sample = 'upsssc-pet/economy/agricultural-reforms/index.html';
const baseline = execFileSync('git', ['show', `237db669da5fca0a8ff8ae6a5a601d284a367642:${sample}`], { cwd: ROOT, encoding: 'utf8', maxBuffer: 20e6 });
const legacy = [...baseline.matchAll(/<script>([\s\S]*?)<\/script>/gi)].map(match => match[1]).find(source => source.includes('sj_pref_lang') && source.includes('langEn'));

test('UPSSSC PET legacy source is fingerprinted and matches the existing shared language runtime', () => {
  assert.equal(validateUpssscPetLegacyLanguage(legacy), legacy.trim());
  assert.throws(() => validateUpssscPetLegacyLanguage(`${legacy}\nwindow.changed = true;`), /Unexpected UPSSSC PET language bootstrap/);
});

test('exact extraction reuses parser-blocking UPSC asset and hydration restores its source', () => {
  const prefix = '<body><button id="langEn">EN</button><button id="langHi">हिन्दी</button>';
  const input = `${prefix}<script>\n${legacy}\n</script><script type="module" src="auth.js"></script></body>`;
  const output = externalizeUpssscPetLanguage(input, { strict: true });
  assert.match(output, /<script src="\/assets\/js\/upsc-language\.js" data-upsc-shared-script="language"><\/script>/);
  assert.equal((output.match(/data-upsc-shared-script="language"/g) || []).length, 1);
  assert.equal(hydrateUpscLanguage(output), input.replace(`<script>\n${legacy}\n</script>`, `<script>${upscLanguageSource}</script>`));
  assert.equal(externalizeUpssscPetLanguage(output), output, 'repeat extraction is a no-op');
  assert.throws(() => externalizeUpssscPetLanguage('<script>different()</script>', { strict: true }), /found 0/);
});
