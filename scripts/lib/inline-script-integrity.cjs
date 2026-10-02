const vm = require('node:vm');
const crypto = require('node:crypto');

// Compile classic inline scripts without executing them or altering lesson data.
function inspectInlineScripts(html) {
  const scripts = [], seen = new Map();
  for (const match of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)) {
    const attrs = match[1];
    if (/\bsrc\s*=/i.test(attrs)) continue;
    const type = attrs.match(/\btype\s*=\s*["']([^"']*)["']/i)?.[1]?.toLowerCase() || '';
    if (type && !['text/javascript', 'application/javascript'].includes(type)) continue;
    const source = match[2];
    const hash = crypto.createHash('sha256').update(source.replace(/\r\n/g, '\n').trim()).digest('hex');
    let syntaxError = null;
    try { new vm.Script(source); } catch (error) { syntaxError = error.message; }
    const previous = seen.get(hash);
    const script = { offset: match.index, bytes: Buffer.byteLength(source), hash, syntaxError,
      nestedDocumentMarkup: /<(?:body|html)\b/i.test(source), duplicateOf: previous ?? null };
    if (previous === undefined) seen.set(hash, scripts.length);
    scripts.push(script);
  }
  return scripts;
}
module.exports = { inspectInlineScripts };
