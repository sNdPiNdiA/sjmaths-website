import crypto from 'node:crypto';
import { upscLanguageScript, upscLanguageSource } from './upsc-language.mjs';

export const upssscPetLegacyLanguageBytes = 1129;
export const upssscPetLegacyLanguageSha256 = '68792416a74422147daceb9ad811d7062e3d0ca016d3625e9fcc70c07c63a03a';
const normalize = source => source.replace(/\r\n/g, '\n').trim();
const normalizeWhitespace = source => normalize(source).replace(/\s+/g, '');

export function validateUpssscPetLegacyLanguage(source) {
  const normalized = normalize(source);
  const digest = crypto.createHash('sha256').update(normalized).digest('hex');
  if (Buffer.byteLength(normalized) !== upssscPetLegacyLanguageBytes || digest !== upssscPetLegacyLanguageSha256) {
    throw new Error(`Unexpected UPSSSC PET language bootstrap (bytes=${Buffer.byteLength(normalized)}, sha256=${digest}).`);
  }
  if (normalizeWhitespace(normalized) !== normalizeWhitespace(upscLanguageSource)) {
    throw new Error('UPSSSC PET language bootstrap differs semantically from the shared UPSC language bootstrap.');
  }
  return normalized;
}

export function externalizeUpssscPetLanguage(html, { strict = false } = {}) {
  let matches = 0;
  const output = html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => {
    try {
      validateUpssscPetLegacyLanguage(source);
      matches++;
      return upscLanguageScript;
    } catch (error) {
      if (error.message.startsWith('Unexpected UPSSSC PET language bootstrap')) return tag;
      throw error;
    }
  });
  if (strict && matches !== 1) throw new Error(`Expected one exact UPSSSC PET language bootstrap, found ${matches}.`);
  return output;
}
