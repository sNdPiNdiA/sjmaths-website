function recoverRepeatedBodyPage(html, katexBlock) {
  if (typeof katexBlock !== 'string' || !katexBlock.trim()) return null;
  const marker = '<script>\n    document.addEventListener("DOMContentLoaded", function () {\n        if (typeof renderMathInElement === \'function\')';
  const markerIndex = html.indexOf(marker);
  const headEnd = html.indexOf('</head>', markerIndex);
  if (markerIndex < 0 || headEnd < 0 || html.indexOf('<html', 0) !== html.lastIndexOf('<html')) return null;
  const bodyStarts = [...html.matchAll(/<body\b[^>]*>/gi)];
  if (bodyStarts.length < 2) return null;
  const realBodyStart = bodyStarts.find(match => match.index > headEnd);
  if (!realBodyStart) return null;
  const bodyContent = bodyStarts.map(match => {
    const close = html.indexOf('</body>', match.index);
    return close < 0 ? null : html.slice(match.index, close + '</body>'.length);
  });
  if (bodyContent.some(body => body === null) || bodyContent.some(body => body !== bodyContent[0])) return null;
  if (bodyContent[0] !== bodyContent.at(-1)) return null;
  const htmlClose = html.slice(html.lastIndexOf('</html>') + '</html>'.length).trim();
  if (htmlClose) return null;
  const preservedBody = html.slice(realBodyStart.index, realBodyStart.index + bodyContent.at(-1).length);
  const prefix = html.slice(0, markerIndex);
  if (!prefix.includes('</script>')) return null;
  return `${prefix}${katexBlock}\n</head>\n${preservedBody}\n</html>\n`;
}
module.exports = { recoverRepeatedBodyPage };
