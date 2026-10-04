// KaTeX auto-render cannot pair delimiters across native HTML sub/sup nodes.
// Normalize those nodes only inside an explicit TeX expression; prose is kept.
export function normalizePhysicsMath(html) {
  return html.replace(/\$\$[\s\S]*?\$\$|(?<![\\$])\$(?!\$)[\s\S]*?(?<!\\)\$(?!\$)/g, expression =>
    expression.replace(/<(sub|sup)>([^<>]*)<\/\1>/g, (_, tag, value) =>
      `${tag === 'sup' ? '^' : '_'}{${value}}`));
}
