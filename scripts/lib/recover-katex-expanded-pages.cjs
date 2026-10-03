function recoverRepeatedBodyPage(html, katexBlock) {
  if (typeof katexBlock !== 'string' || !katexBlock.trim()) return null;
  const marker = /<script>\r?\n    document\.addEventListener\("DOMContentLoaded", function \(\) \{\r?\n        if \(typeof renderMathInElement === 'function'\)/;
  const markerMatch = marker.exec(html);
  const markerIndex = markerMatch?.index ?? -1;
  const headEnd = html.indexOf('</head>', markerIndex);
  if (markerIndex < 0 || headEnd < 0 || html.indexOf('<html', 0) !== html.lastIndexOf('<html')) return null;
  const bodyStarts = [...html.matchAll(/<body\b[^>]*>/gi)];
  if (bodyStarts.length < 2) return null;

  // Some damaged files contain repeated complete body/document copies separated
  // by the remainder of the truncated KaTeX block. Preserve the first complete
  // copy only; compare all copies after cache-buster normalization first.
  const htmlEnds = [...html.matchAll(/<\/html\s*>/gi)];
  const firstCompleteEnd = html.indexOf('</html>', bodyStarts[0].index);
  if (htmlEnds.length === bodyStarts.length && headEnd < firstCompleteEnd) {
    const copies = bodyStarts.map(start => {
      const end = html.indexOf('</html>', start.index);
      if (end < 0) return null;
      return html.slice(start.index, end + '</html>'.length)
        .replace(/([?&]v=)[^"'&#\s]+/g, '$1<CACHE_VERSION>');
    });
    if (copies.some(copy => copy === null) || copies.some(copy => copy !== copies[0])) return null;
    const firstEnd = html.indexOf('</html>', bodyStarts[0].index);
    const lineEnding = html.includes('\r\n') ? '\r\n' : '\n';
    return `${html.slice(0, markerIndex)}${katexBlock}${lineEnding}${html.slice(headEnd, firstEnd + '</html>'.length)}${lineEnding}`;
  }

  // Affected science/physics pages can have a complete, but empty, document
  // shell before the repeated lesson bodies. The damaged renderer leaves this
  // exact fragment between the shell and the first body. Keep the valid head
  // metadata, discard only that empty shell's closing tags, then retain one
  // byte-identical lesson body.
  const firstBody = bodyStarts[0];
  const firstBodyEnd = html.indexOf('</body>', firstBody.index);
  const bodyCopy = html.slice(firstBody.index, firstBodyEnd + '</body>'.length);
  const firstBodyPrefix = html.slice(0, firstBody.index);
  const emptyShellTail = /<\/body\s*>\s*<\/html\s*>\s*,\s*right\s*:\s*['"]?\s*$/i.exec(firstBodyPrefix);
  const bodyCopies = bodyStarts.map(start => {
    const end = html.indexOf('</body>', start.index);
    return end < 0 ? null : html.slice(start.index, end + '</body>'.length)
      .replace(/([?&]v=)[^"'&#\s]+/g, '$1<CACHE_VERSION>');
  });
  const identicalBodies = bodyCopies.every(copy => copy !== null && copy === bodyCopies[0]);
  if (markerIndex > firstBody.index && firstBodyEnd >= 0 && emptyShellTail
    && identicalBodies
    && (html.match(/<html\b/gi) || []).length === 1
    && (firstBodyPrefix.match(/<head\b/gi) || []).length === 1
    && !(firstBodyPrefix.match(/<\/head\s*>/gi) || []).length) {
    const cleanPrefix = firstBodyPrefix.slice(0, emptyShellTail.index);
    const lineEnding = html.includes('\r\n') ? '\r\n' : '\n';
    return `${cleanPrefix}${katexBlock}${lineEnding}</head>${lineEnding}${bodyCopy}${lineEnding}</html>${lineEnding}`;
  }

  // Retain the existing recovery path for legacy pages where repeated body
  // markup was injected into one document shell rather than full page copies.
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
  const lineEnding = html.includes('\r\n') ? '\r\n' : '\n';
  return `${prefix}${katexBlock}${lineEnding}</head>${lineEnding}${preservedBody}${lineEnding}</html>${lineEnding}`;
}
module.exports = { recoverRepeatedBodyPage };
