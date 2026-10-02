import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const class10ReaderTabsBytes = 5124;
export const class10ReaderTabsSha256 = 'dda062413b76f5544b29481980ac18b7d0e6d563674cf0aa12e8c61b411a3065';
export const class10ReaderTabsTag = '<script src="/assets/js/class-10-reader-tabs.js" data-class-10-reader-tabs="shared"></script>';
const assetPath = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../assets/js/class-10-reader-tabs.js');
const normalize = source => source.replace(/\r\n/g, '\n').trim();

export function validateClass10ReaderTabs(source) {
  const runtime = normalize(source);
  const digest = crypto.createHash('sha256').update(runtime).digest('hex');
  if (Buffer.byteLength(runtime) !== class10ReaderTabsBytes || digest !== class10ReaderTabsSha256) {
    throw new Error(`Unexpected Class 10 reader tab controller (bytes=${Buffer.byteLength(runtime)}, sha256=${digest}).`);
  }
  return runtime;
}

export function getClass10ReaderTabsRuntime() {
  return validateClass10ReaderTabs(fs.readFileSync(assetPath, 'utf8'));
}

export function externalizeClass10ReaderTabs(html, runtimeSource, { strict = false } = {}) {
  const runtime = validateClass10ReaderTabs(runtimeSource);
  let matches = 0;
  const output = html.replace(/<script>([\s\S]*?)<\/script>/gi, (tag, source) => {
    try {
      if (validateClass10ReaderTabs(source) !== runtime) return tag;
      matches++;
      return class10ReaderTabsTag;
    } catch (error) {
      if (error.message.startsWith('Unexpected Class 10 reader tab controller')) return tag;
      throw error;
    }
  });
  if (strict && matches !== 1) throw new Error(`Expected one exact Class 10 reader tab controller, found ${matches}.`);
  return output;
}

export function hydrateClass10ReaderTabs(html, runtimeSource = getClass10ReaderTabsRuntime()) {
  const runtime = validateClass10ReaderTabs(runtimeSource);
  return html.replace(/<script\b([^>]*)>\s*<\/script\s*>/gi, (tag, attributes) =>
    /data-class-10-reader-tabs=["']shared["']/.test(attributes) ? `<script>${runtime}</script>` : tag);
}
