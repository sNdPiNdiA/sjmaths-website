import fs from 'node:fs';

// Parser-blocking at the original body position: data is present before the
// listener registers, and DOMContentLoaded cannot precede script execution.
export const historyRuntimeScript = '<script id="history-runtime" src="/assets/js/history-topic.js"></script>';
export const historyRuntimeSource = fs.readFileSync(new URL('../../assets/js/history-topic.js', import.meta.url), 'utf8').trim();
const normalize = source => source.replace(/\r\n/g, '\n').trim();

export function externalizeHistoryRuntime(html) {
  return html.replace(/<script id="history-runtime">([\s\S]*?)<\/script>/g, (tag, source) =>
    normalize(source) === normalize(historyRuntimeSource) ? historyRuntimeScript : tag);
}
