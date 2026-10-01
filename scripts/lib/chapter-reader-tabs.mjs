import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const chapterReaderTabsBytes = 3216;
export const chapterReaderTabsSha256 = '059c6fc8b924a9db284189d7c86e30f8c6fb314390d582d16a7872bf75ece335';
export const chapterReaderTabsTag = '<script src="/assets/js/chapter-reader-tabs.js" data-chapter-reader-tabs="shared"></script>';
const assetPath = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../assets/js/chapter-reader-tabs.js');
const normalize = source => source.replace(/\r\n/g, '\n').trim();

export function validateChapterReaderTabs(source) {
  const runtime = normalize(source);
  const digest = crypto.createHash('sha256').update(runtime).digest('hex');
  if (Buffer.byteLength(runtime) !== chapterReaderTabsBytes || digest !== chapterReaderTabsSha256) {
    throw new Error(`Unexpected chapter-reader tab controller (bytes=${Buffer.byteLength(runtime)}, sha256=${digest}).`);
  }
  return runtime;
}

export function getChapterReaderTabsRuntime() {
  return validateChapterReaderTabs(fs.readFileSync(assetPath, 'utf8'));
}

export function externalizeChapterReaderTabs(html, runtimeSource, { strict = false } = {}) {
  const runtime = validateChapterReaderTabs(runtimeSource);
  let matches = 0;
  const output = html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => {
    try {
      if (validateChapterReaderTabs(source) !== runtime) return tag;
      matches++;
      return chapterReaderTabsTag;
    } catch (error) {
      if (error.message.startsWith('Unexpected chapter-reader tab controller')) return tag;
      throw error;
    }
  });
  if (strict && matches !== 1) throw new Error(`Expected one exact chapter-reader controller, found ${matches}.`);
  return output;
}

export function hydrateChapterReaderTabs(html, runtimeSource = getChapterReaderTabsRuntime()) {
  const runtime = validateChapterReaderTabs(runtimeSource);
  return html.replace(/<script\b([^>]*)>\s*<\/script\s*>/gi, (tag, attributes) =>
    /data-chapter-reader-tabs=["']shared["']/.test(attributes) ? `<script>${runtime}</script>` : tag);
}
