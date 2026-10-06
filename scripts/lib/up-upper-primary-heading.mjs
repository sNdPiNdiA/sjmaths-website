const HEADING_LIMIT = 54;

/** Return a compact display heading while leaving the full topic name for notes and metadata. */
export function compactUpUpperPrimaryHeading(value, maxLength = HEADING_LIMIT) {
  const title = String(value || '').replace(/\s+/g, ' ').trim();
  if (title.length <= maxLength) return title;

  const boundaries = [' — ', ' – ', ': ']
    .map((separator) => ({ separator, index: title.indexOf(separator) }))
    .filter(({ index }) => index > 9)
    .sort((a, b) => a.index - b.index);

  for (const { index } of boundaries) {
    const lead = title.slice(0, index).trim();
    if (lead.length <= maxLength) return lead;
  }

  const clauses = title.split(/,\s*/);
  if (clauses.length > 1) {
    const lead = clauses.slice(0, 2).join(', ').trim();
    if (lead.length <= maxLength) return lead;
    if (clauses[0].length <= maxLength) return clauses[0].trim();
  }

  const parenthesis = title.indexOf(' (');
  if (parenthesis > 9 && parenthesis <= maxLength) return title.slice(0, parenthesis).trim();

  const conjunction = title.indexOf(' & ');
  if (conjunction > 9 && conjunction <= maxLength) return title.slice(0, conjunction).trim();

  return title;
}

export function compactUpUpperPrimaryModuleLabel(value) {
  const title = String(value || '')
    .replace(/^\s*(?:Module|खण्ड|इकाई)\s*[0-9०-९]+\s*[:·-]\s*/u, '')
    .replace(/\s*\((?:Topics?\s+\d+\s+(?:to|से)\s+\d+|\d+\s+(?:Micro-Topics?|Topics?|अध्याय))\)\s*$/iu, '')
    .trim();
  return compactUpUpperPrimaryHeading(title);
}
