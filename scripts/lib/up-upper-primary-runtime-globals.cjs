const declarations = [
  ['const TOPIC_STORAGE_KEY =', 'window.TOPIC_STORAGE_KEY ='],
  ['const TOPIC_CHECKBOX_ID =', 'window.TOPIC_CHECKBOX_ID ='],
  ['const testData =', 'window.testData ='],
];

function exposeUpperPrimaryRuntimeGlobals(html) {
  let output = html;
  for (const [legacy, global] of declarations) {
    const count = output.split(legacy).length - 1;
    if (count !== 1) return null;
    output = output.replace(legacy, global);
  }
  return output;
}
module.exports = { exposeUpperPrimaryRuntimeGlobals };
