const DELIMITED_MATH_PATTERN = /\$\$[\s\S]*?\$\$|\$(?:\\.|[^$\\]|\\.)+\$|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]/g;
const MATHEMATICAL_SOURCE_PATTERN = /\\[a-zA-Z]+|(?:[A-Za-z0-9)\]}])\s*[_^]\s*(?:\{[^{}]+\}|[A-Za-z0-9])|[≤≥≠∈∉∞√π∑∫]|\b[A-Za-z]\s*(?:=|<|>|≤|≥)\s*[A-Za-z0-9(+-]/;
const ENGLISH_CONNECTOR_PATTERN = /\b(?:and|are|as|because|both|but|for|from|in|is|of|on|or|the|to|with)\b/i;
const INLINE_MATH_TOKEN_PATTERN = /\b[A-Za-z0-9][A-Za-z0-9_^{},().]*(?:\s*[+\-*/]\s*[A-Za-z0-9][A-Za-z0-9_^{},().]*)*\s*(?:=|<|>|≤|≥)\s*[A-Za-z0-9][A-Za-z0-9_^{},().]*(?:\s*[+\-*/]\s*[A-Za-z0-9][A-Za-z0-9_^{},().]*)*|\\[a-zA-Z]+(?:\s*\{(?:[^{}]|\{[^{}]*\})*\})*(?:\s*[_^]\s*(?:\{(?:[^{}]|\{[^{}]*\})*\}|[A-Za-z0-9]+))?|[A-Za-z0-9]\s*[_^]\s*(?:\{[^{}]+\}|[A-Za-z0-9]+)/g;

function hasDelimitedMath(value) {
  DELIMITED_MATH_PATTERN.lastIndex = 0;
  return DELIMITED_MATH_PATTERN.test(value);
}

function stripOptionLetter(value, letter) {
  const escapedLetter = letter.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const completeTextLabel = new RegExp(`^\\s*\\\\text\\{\\s*\\(${escapedLetter}\\)\\s*\\}\\s*`, 'i');
  if (completeTextLabel.test(value)) return value.replace(completeTextLabel, '');

  const textLabel = new RegExp(`^(\\s*\\\\text\\{)\\s*\\(${escapedLetter}\\)\\s*`, 'i');
  if (textLabel.test(value)) return value.replace(textLabel, '$1');

  const prefix = new RegExp(`^\\s*\\(${escapedLetter}\\)\\s*`, 'i');
  return value.replace(prefix, '');
}

function removeUnmatchedDollarSigns(value) {
  // Generated content occasionally contains one stray dollar before an
  // otherwise un-delimited formula. Treat those as a bad delimiter and repair
  // them before adding a balanced pair.
  return value.replace(/\\?\$/g, '');
}

function unwrapExistingMath(value) {
  return value.replace(DELIMITED_MATH_PATTERN, match => {
    if (match.startsWith('$$')) return match.slice(2, -2);
    if (match.startsWith('\\(') || match.startsWith('\\[')) return match.slice(2, -2);
    return match.slice(1, -1);
  });
}

function containsNaturalLanguage(value) {
  const outsideCommands = value
    .replace(/\\[a-zA-Z]+/g, ' ')
    .replace(/\{[^{}]*\}/g, ' ')
    .replace(/[{}_^\\$]/g, ' ');
  const words = outsideCommands.match(/[A-Za-z]{4,}/g) || [];
  return words.length > 0 || ENGLISH_CONNECTOR_PATTERN.test(outsideCommands);
}

function wrapInlineMathTokens(value) {
  return value.replace(INLINE_MATH_TOKEN_PATTERN, token => `$${token.trim()}$`);
}

export function hasUndelimitedMathematics(value) {
  const unrenderedText = String(value ?? '').replace(DELIMITED_MATH_PATTERN, ' ');
  return MATHEMATICAL_SOURCE_PATTERN.test(unrenderedText);
}

export function normalizeRepeatedDisplayMathDelimiters(value) {
  return String(value ?? '').replace(/\${3,}/g, () => '$$');
}

function repairUnescapedSetClosers(source) {
  let result = '';
  let setDepth = 0;
  let groupDepth = 0;

  for (let index = 0; index < source.length; index++) {
    const character = source[index];
    const next = source[index + 1];
    const isEscapedBrace = character === '\\' && (index === 0 || source[index - 1] !== '\\');

    if (isEscapedBrace && next === '{') {
      setDepth++;
      result += '\\{';
      index++;
      continue;
    }

    if (isEscapedBrace && next === '}') {
      if (setDepth > 0) setDepth--;
      result += '\\}';
      index++;
      continue;
    }

    if (character === '{') {
      groupDepth++;
      result += character;
      continue;
    }

    if (character === '}' && groupDepth > 0) {
      groupDepth--;
      result += character;
      continue;
    }

    if (character === '}' && setDepth > 0) {
      setDepth--;
      result += '\\}';
      continue;
    }

    result += character;
  }

  return result;
}

export function normalizeMathematicsMarkup(value) {
  function normalizeTextSegment(text) {
    const source = normalizeRepeatedDisplayMathDelimiters(text);
    const ranges = [];
    const dollarRuns = [...source.matchAll(/\$+/g)]
      .filter(match => {
        let slashes = 0;
        for (let index = match.index - 1; index >= 0 && source[index] === '\\'; index--) slashes++;
        return slashes % 2 === 0;
      });

    for (const runLength of [1, 2]) {
      const tokens = dollarRuns.filter(match => match[0].length === runLength);
      for (let index = 0; index + 1 < tokens.length; index += 2) {
        const open = tokens[index];
        const close = tokens[index + 1];
        if (close.index < open.index + runLength) continue;
        ranges.push({ start: open.index, contentStart: open.index + runLength, contentEnd: close.index, end: close.index + runLength, delimiterLength: runLength });
      }
    }

    const slashTokens = [...source.matchAll(/\\\(|\\\)|\\\[|\\\]/g)];
    let open = null;
    for (const token of slashTokens) {
      const tokenValue = token[0];
      if (tokenValue === '\\(' || tokenValue === '\\[') {
        open = token;
        continue;
      }
      if (open && ((open[0] === '\\(' && tokenValue === '\\)') || (open[0] === '\\[' && tokenValue === '\\]'))) {
        ranges.push({ start: open.index, contentStart: open.index + 2, contentEnd: token.index, end: token.index + 2, delimiterLength: 2 });
        open = null;
      }
    }

    ranges.sort((left, right) => left.start - right.start || right.end - left.end);
    let result = '';
    let cursor = 0;
    for (const range of ranges) {
      if (range.start < cursor) continue;
      const opening = source.slice(range.start, range.contentStart);
      const closing = source.slice(range.contentEnd, range.end);
      result += source.slice(cursor, range.contentStart);
      result += repairUnescapedSetClosers(source.slice(range.contentStart, range.contentEnd));
      result += closing;
      cursor = range.end;
    }
    return result + source.slice(cursor);
  }

  const protectedBlocks = [];
  const withoutScripts = String(value ?? '').replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1\s*>/gi, block => `\uE000${protectedBlocks.push(block) - 1}\uE001`);
  const htmlTagPattern = /<!--[^]*?-->|<\/?[a-z][a-z0-9:-]*(?:\s[^<>]*|\/?)>/gi;
  const normalized = withoutScripts.split(/(<!--[^]*?-->|<\/?[a-z][a-z0-9:-]*(?:\s[^<>]*|\/?)>)/gi);
  for (let index = 0; index < normalized.length; index++) {
    htmlTagPattern.lastIndex = 0;
    if (!htmlTagPattern.test(normalized[index])) normalized[index] = normalizeTextSegment(normalized[index]);
  }
  return normalized.join('').replace(/\uE000(\d+)\uE001/g, (_, index) => protectedBlocks[Number(index)]);
}

export function formatMathematicsOption(option, optionLetter) {
  const original = String(option ?? '').trim();
  if (!original) return original;

  const letter = /^[A-D]$/i.test(String(optionLetter)) ? String(optionLetter).toUpperCase() : '';
  if (!letter) return original;

  const labeledOriginal = stripOptionLetter(original, letter);
  const containsDelimitedMath = hasDelimitedMath(original);
  const unwrapped = containsDelimitedMath ? unwrapExistingMath(original) : original;
  const source = stripOptionLetter(unwrapped, letter);
  if (!source.trim()) throw new Error(`MCQ option ${letter} contains only its repeated label`);
  const textOnly = source.match(/^\s*\\text\{([^{}]*)\}\s*$/i);
  if (textOnly) return textOnly[1];

  if (containsDelimitedMath && !hasUndelimitedMathematics(original)) {
    return source === unwrapped ? original : `$${source}$`;
  }

  if (!MATHEMATICAL_SOURCE_PATTERN.test(source)) return labeledOriginal;

  const value = removeUnmatchedDollarSigns(source);

  // Explicit \text commands mark prose that belongs inside the formula.
  // Otherwise keep explanatory English outside math mode, even when the
  // option starts with a mathematical symbol.
  if (/\\text\s*\{/.test(value) || !containsNaturalLanguage(value)) {
    return `$${value}$`;
  }

  // Keep explanatory English in normal text while typesetting embedded TeX
  // tokens such as \mathbb{R} or \mathbf{a}.
  return wrapInlineMathTokens(value);
}
