'use strict';

const FIXED_VALUE_KEYS = new Set(['type']);

function buildHindiTranslationPrompt(concepts, subject) {
  const subjectLabel = subject === 'sanskrit' ? 'Sanskrit' : 'Hindi';
  const subjectGuidance = subject === 'sanskrit'
    ? 'This is Sanskrit exam material. Write explanations in natural, student-friendly Hindi using Devanagari. Write Sanskrit grammatical terms, forms, verses, and examples in correct Devanagari wherever possible. In Sanskrit grammar, प्रथम पुरुष means third person, मध्यम पुरुष means second person, and उत्तम पुरुष means first person; use these equivalents correctly even when the source lists English 1st/2nd/3rd person. Translate English explanations and mnemonics; retain technical symbols, formulas, numerals, and standard exam abbreviations such as NCERT and UPTET.'
    : 'This is Hindi language and literature exam material. Write natural, student-friendly Hindi in Devanagari. Render Hindi grammatical and literary terms, authors, titles, and examples in Devanagari. Translate English explanations and mnemonics; retain technical symbols, formulas, numerals, and standard exam abbreviations such as NCERT and UPTET.';

  return `Translate the following ${subjectLabel} exam notes from English into the Hindi-language view.

LANGUAGE AND SCRIPT:
- ${subjectGuidance}
- Do not leave any Latin-script words or phrases in the translated view, including English glosses in parentheses (for example, translate "उपमा (Simile)" rather than keeping "Simile"). Write acronyms, names, mnemonics, and technical terms in Devanagari too. Latin letters may remain only inside mathematical notation/formulas.
- When a single Latin letter is a notation marker, write its Devanagari letter name (for example, I as आई and S as एस); do not reinterpret it as punctuation or a Sanskrit sign. Keep numeric labels as the same value, using Devanagari digits if needed.
- Convert Roman numerals that denote values (for example, VII) to the equivalent Devanagari digits.
- Do not leave explanatory sentences in English or romanized Hindi/Sanskrit. Use Devanagari for the translated view.
- Keep proper educational meaning, accepted terminology, names, examples, and all factual claims intact. Do not add, remove, summarize, or correct content.
- Preserve every number, formula, mathematical symbol, bullet, markdown marker, and the order of content.

STRUCTURE:
- Return only valid JSON with exactly the same keys, value types, array lengths, and ordering as the input.
- Keep structural enum values such as "table", "list", "subcards", "tip", and "trap" unchanged.
- Do not add translation metadata or wrap the result in Markdown fences.

SOURCE JSON:
${JSON.stringify(concepts)}`;
}

function buildHindiCleanupPrompt(translation, subject, findings) {
  const subjectLabel = subject === 'sanskrit' ? 'Sanskrit' : 'Hindi';
  const personGuidance = subject === 'sanskrit'
    ? 'Also preserve Sanskrit person terminology accurately: प्रथम पुरुष is third person, मध्यम पुरुष is second person, and उत्तम पुरुष is first person. When translating English 1st/2nd/3rd person, use उत्तम/मध्यम/प्रथम in that semantic order.'
    : '';
  return `Proofread this Hindi translation of ${subjectLabel} exam notes. These content paths still contain Latin-script text:
${findings.join('\n')}

Rewrite every human-readable value in natural Hindi using Devanagari only. Translate or transliterate all remaining English, romanized Hindi/Sanskrit, including English glosses in parentheses, acronyms, names, and mnemonics into Devanagari. Replace English-letter mnemonics with a short Hindi mnemonic in Devanagari, keeping the same recall facts. For Sanskrit notes, keep Sanskrit words, grammatical forms, verses, and examples in correct Devanagari. ${personGuidance} Latin letters are allowed only inside mathematical notation/formulas. For example, write the Hindi equivalents of names and exam bodies in Devanagari instead of leaving forms such as "Alam" or "UP".

Preserve the exact educational meaning and all facts. Do not add, remove, summarize, or reorder anything. Do not repeat any flagged Latin text. Convert Roman numerals that denote values (for example, VII) to equivalent Devanagari digits. Preserve all numbers, formulas, mathematical symbols, markdown, JSON keys, value types, array lengths, and ordering. Keep structural enum values such as "table", "list", "subcards", "tip", and "trap" unchanged. Return only the same valid JSON structure, with no Markdown fences.

TRANSLATION JSON:
${JSON.stringify(translation)}`;
}

function assertSameShape(source, translated, location = '$') {
  if (Array.isArray(source)) {
    if (!Array.isArray(translated) || source.length !== translated.length) {
      throw new Error(`Translation changed array shape at ${location}`);
    }
    source.forEach((value, index) => assertSameShape(value, translated[index], `${location}[${index}]`));
    return;
  }
  if (source && typeof source === 'object') {
    if (!translated || typeof translated !== 'object' || Array.isArray(translated)) {
      throw new Error(`Translation changed object shape at ${location}`);
    }
    const sourceKeys = Object.keys(source).sort();
    const translatedKeys = Object.keys(translated).sort();
    if (sourceKeys.join('\0') !== translatedKeys.join('\0')) {
      throw new Error(`Translation changed object keys at ${location}`);
    }
    for (const key of sourceKeys) assertSameShape(source[key], translated[key], `${location}.${key}`);
    return;
  }
  if (typeof source !== typeof translated) {
    throw new Error(`Translation changed value type at ${location}`);
  }
}

function pairTranslatedValues(source, translated, key = '') {
  if (FIXED_VALUE_KEYS.has(key)) return source;
  if (Array.isArray(source)) return source.map((value, index) => pairTranslatedValues(value, translated[index], key));
  if (source && typeof source === 'object') {
    return Object.fromEntries(Object.keys(source).map(childKey => [
      childKey,
      pairTranslatedValues(source[childKey], translated[childKey], childKey),
    ]));
  }
  if (typeof source === 'string') return { en: source, hi: translated };
  return source;
}

function extractEnglishValues(value, key = '') {
  if (FIXED_VALUE_KEYS.has(key)) return value;
  if (Array.isArray(value)) return value.map(item => extractEnglishValues(item, key));
  if (value && typeof value === 'object') {
    if (typeof value.en === 'string' && typeof value.hi === 'string') return value.en;
    return Object.fromEntries(Object.keys(value).map(childKey => [childKey, extractEnglishValues(value[childKey], childKey)]));
  }
  return value;
}

function extractHindiValues(value, key = '') {
  if (FIXED_VALUE_KEYS.has(key)) return value;
  if (Array.isArray(value)) return value.map(item => extractHindiValues(item, key));
  if (value && typeof value === 'object') {
    if (typeof value.en === 'string' && typeof value.hi === 'string') return value.hi;
    return Object.fromEntries(Object.keys(value).map(childKey => [
      childKey,
      extractHindiValues(value[childKey], childKey),
    ]));
  }
  return value;
}

function numericTokenDifferences(source, translated, subject = 'hindi') {
  const englishNumberWords = [
    ['0', ['zero']], ['1', ['one', 'first']], ['2', ['two', 'second']], ['3', ['three', 'third']],
    ['4', ['four', 'fourth']], ['5', ['five', 'fifth']], ['6', ['six', 'sixth']],
    ['7', ['seven', 'seventh']], ['8', ['eight', 'eighth']], ['9', ['nine', 'ninth']],
    ['10', ['ten', 'tenth']], ['11', ['eleven', 'eleventh']], ['12', ['twelve', 'twelfth']],
    ['13', ['thirteen', 'thirteenth']], ['14', ['fourteen', 'fourteenth']], ['15', ['fifteen', 'fifteenth']],
    ['16', ['sixteen', 'sixteenth']], ['17', ['seventeen', 'seventeenth']], ['18', ['eighteen', 'eighteenth']],
    ['19', ['nineteen', 'nineteenth']], ['20', ['twenty', 'twentieth']],
  ];
  const hindiNumberWords = [
    ['0', ['शून्य']],
    ['1', ['एक', 'पहला', 'पहली', 'पहले', 'प्रथम', 'प्रथमा', 'सर्वप्रथम']],
    ['2', ['दो', 'दोनों', 'दूसरा', 'दूसरी', 'दूसरे', 'द्वितीय', 'द्वितीया']],
    ['3', ['तीन', 'तीनों', 'तीसरा', 'तीसरी', 'तीसरे', 'तृतीय', 'तृतीया', 'त्रिविध', 'त्रय', 'त्रयो', 'त्रयी', 'त्रिअंश', 'तिहाई', 'तृतीयांश']],
    ['4', ['चार', 'चारों', 'चौथा', 'चौथी', 'चौथे', 'चतुर्थ', 'चतुर्थी']],
    ['5', ['पाँच', 'पांच', 'पाँचवाँ', 'पाँचवीं', 'पाँचवें', 'पाँचवां', 'पांचवाँ', 'पांचवीं', 'पांचवें', 'पंच', 'पञ्च', 'पंचम', 'पञ्चम', 'पंचमी', 'पञ्चमी', 'पंचरात्र', 'पञ्चरात्र']],
    ['6', ['छह', 'छः', 'छठा', 'छठी', 'छठे', 'षष्ठ', 'षष्ठी']],
    ['7', ['सात', 'सातवाँ', 'सातवीं', 'सातवें', 'सप्तम', 'सप्तमी']],
    ['8', ['आठ', 'आठवाँ', 'आठवीं', 'आठवें', 'अष्टम']],
    ['9', ['नौ', 'नौवाँ', 'नौवीं', 'नौवें', 'नवम']],
    ['10', ['दस', 'दसवाँ', 'दसवीं', 'दसवें', 'दशम']],
    ['11', ['ग्यारह', 'ग्यारहवाँ', 'ग्यारहवां', 'ग्यारहवीं', 'एकादश']],
    ['12', ['बारह', 'बारहवाँ', 'बारहवां', 'बारहवीं', 'द्वादश']],
    ['13', ['तेरह', 'तेरहवाँ', 'तेरहवां', 'तेरहवीं', 'त्रयोदश']],
    ['14', ['चौदह', 'चौदहवाँ', 'चौदहवां', 'चौदहवीं', 'चतुर्दश']],
    ['15', ['पंद्रह', 'पन्द्रह', 'पंद्रहवाँ', 'पंद्रहवां', 'पन्द्रहवाँ', 'पन्द्रहवां', 'पंचदश']],
    ['16', ['सोलह', 'सोलहवाँ', 'सोलहवां', 'सोलहवीं', 'षोडश']],
    ['17', ['सत्रह', 'सत्रहवाँ', 'सत्रहवां', 'सत्रहवीं', 'सप्तदश']],
    ['18', ['अठारह', 'अठारहवाँ', 'अठारहवां', 'अठारहवीं', 'अष्टादश']],
    ['19', ['उन्नीस', 'उन्नीसवाँ', 'उन्नीसवां', 'उन्नीसवीं', 'नवदश']],
    ['20', ['बीस', 'बीसवाँ', 'बीसवां', 'बीसवीं', 'विंशति']],
    ['21', ['इक्कीस']], ['22', ['बाईस']], ['23', ['तेईस']], ['24', ['चौबीस']], ['25', ['पच्चीस']],
    ['26', ['छब्बीस']], ['27', ['सत्ताईस']], ['28', ['अट्ठाईस']], ['29', ['उनतीस']],
    ['30', ['तीस', 'त्रिंशत्']], ['31', ['इकतीस']], ['32', ['बत्तीस']], ['33', ['तैंतीस']],
    ['34', ['चौंतीस']], ['35', ['पैंतीस']], ['36', ['छत्तीस']], ['37', ['सैंतीस']],
    ['38', ['अड़तीस']], ['39', ['उनतालीस']], ['40', ['चालीस', 'चत्वारिंशत्']],
    ['41', ['इकतालीस']], ['42', ['बयालीस']], ['43', ['तैंतालीस']], ['44', ['चवालीस']],
    ['45', ['पैंतालीस']], ['46', ['छियालीस']], ['47', ['सैंतालीस']], ['48', ['अड़तालीस']],
    ['49', ['उनचास']], ['50', ['पचास', 'पञ्चाशत्']], ['51', ['इक्यावन']], ['52', ['बावन']],
    ['53', ['तिरपन']], ['54', ['चौवन']], ['55', ['पचपन']], ['56', ['छप्पन']],
    ['57', ['सत्तावन']], ['58', ['अट्ठावन']], ['59', ['उनसठ']], ['60', ['साठ']],
    ['100', ['सौ', 'शत']],
  ];
  const findWordMatches = (value, entries, hindi = false) => {
    const text = String(value);
    const matches = [];
    for (const [number, words] of entries) {
      const boundary = hindi ? '(?<![\\p{L}\\p{M}])' : '\\b';
      const endBoundary = hindi ? '(?![\\p{L}\\p{M}])' : '\\b';
      const expression = new RegExp(`${boundary}(?:${words.join('|')})${endBoundary}`, 'giu');
      for (const match of text.matchAll(expression)) matches.push({ index: match.index, token: number });
    }
    return matches.sort((left, right) => left.index - right.index);
  };
  const toEnglishTokens = value => {
    const text = String(value);
    const matches = [...text.matchAll(/\d+(?:[.,]\d+)?/g)].map(match => ({ index: match.index, token: match[0] }));
    const digitCounts = new Map();
    for (const match of matches) digitCounts.set(match.token, (digitCounts.get(match.token) || 0) + 1);
    const romanValues = new Map([['II', '2'], ['III', '3'], ['IV', '4'], ['VI', '6'], ['VII', '7'], ['VIII', '8'], ['IX', '9']]);
    for (const match of text.matchAll(/\b(?:II|III|IV|VI|VII|VIII|IX)\b/g)) {
      matches.push({ index: match.index, token: romanValues.get(match[0]) });
    }
    for (const match of findWordMatches(text, englishNumberWords)) {
      if (match.token === '1' && /^(?:should|must|may|can|could|would|will|does|is|was|has|have|cannot|never|also|always|often|simply|then|not|who|that|another)\b/i.test(text.slice(match.index + 3).trimStart())) continue;
      if (match.token === '1' && /^another\b/i.test(text.slice(match.index).replace(/^one\s+/i, ''))) continue;
      if (match.token === '0' && /^zero\s+(?:guesswork|negative\s+ambiguity|ambiguity)\b/i.test(text.slice(match.index))) continue;
      const digitCount = digitCounts.get(match.token) || 0;
      if (digitCount > 0) continue;
      matches.push(match);
    }
    return matches.sort((left, right) => left.index - right.index).map(match => match.token);
  };
  const toHindiTokens = (value, expected) => {
    const text = String(value);
    const matches = [...text.matchAll(/[\d०-९]+(?:[.,][\d०-९]+)?/g)].map(match => ({
      index: match.index,
      token: match[0].replace(/[०-९]/g, digit => String('०१२३४५६७८९'.indexOf(digit))),
    }));
    const expectedCounts = new Map();
    const actualCounts = new Map();
    for (const token of expected) expectedCounts.set(token, (expectedCounts.get(token) || 0) + 1);
    for (const match of matches) actualCounts.set(match.token, (actualCounts.get(match.token) || 0) + 1);
    const wordMatches = findWordMatches(text, hindiNumberWords, true);
    const personTerms = subject === 'sanskrit'
      ? [
        ...[...text.matchAll(/(प्रथम|मध्यम|उत्तम)\s+पुरुष/g)].map(match => ({
          index: match.index,
          token: match[1] === 'प्रथम' ? '3' : match[1] === 'मध्यम' ? '2' : '1',
        })),
        ...[...text.matchAll(/पुरुष\s*[([]([^\])]*?)[\])]/g)].flatMap(group => [
          ...group[1].matchAll(/(?<!\p{Script=Devanagari})(प्रथम|मध्यम|उत्तम)(?!\p{Script=Devanagari})/gu),
        ].map(match => ({
          index: group.index + group[0].indexOf(group[1]) + match.index,
          token: match[1] === 'प्रथम' ? '3' : match[1] === 'मध्यम' ? '2' : '1',
        }))),
      ]
      : [...text.matchAll(/(मध्यम|उत्तम|अन्य)\s+पुरुष/g)].map(match => ({
        index: match.index,
        token: match[1] === 'उत्तम' ? '1' : match[1] === 'मध्यम' ? '2' : '3',
      }));
    for (const person of personTerms) {
      for (let index = wordMatches.length - 1; index >= 0; index--) {
        if (wordMatches[index].index === person.index) wordMatches.splice(index, 1);
      }
      wordMatches.push(person);
    }
    for (const match of wordMatches) {
      const token = match.token;
      const expectedCount = expectedCounts.get(token) || 0;
      const actualCount = actualCounts.get(token) || 0;
      if (actualCount >= expectedCount) continue;
      matches.push(match);
      actualCounts.set(token, actualCount + 1);
    }
    return matches.sort((left, right) => left.index - right.index).map(match => match.token);
  };
  const differences = [];
  const visit = (english, hindi, location = '$', key = '') => {
    if (FIXED_VALUE_KEYS.has(key)) return;
    if (Array.isArray(english)) return english.forEach((item, index) => visit(item, hindi[index], `${location}[${index}]`, key));
    if (english && typeof english === 'object') {
      for (const childKey of Object.keys(english)) visit(english[childKey], hindi[childKey], `${location}.${childKey}`, childKey);
      return;
    }
    if (typeof english !== 'string' || typeof hindi !== 'string') return;
    const expected = toEnglishTokens(english);
    const actual = toHindiTokens(hindi, expected);
    const counts = tokens => tokens.reduce((result, token) => result.set(token, (result.get(token) || 0) + 1), new Map());
    const expectedCounts = counts(expected);
    const actualCounts = counts(actual);
    const sameFacts = expectedCounts.size === actualCounts.size
      && [...expectedCounts].every(([token, count]) => actualCounts.get(token) === count);
    if (!sameFacts) {
      const excerpt = value => String(value).replace(/\s+/g, ' ').trim().slice(0, 220);
      differences.push(`${location}: source [${expected.join(', ')}] "${excerpt(english)}"; Hindi [${actual.join(', ')}] "${excerpt(hindi)}"`);
    }
  };
  visit(source, translated);
  return differences;
}

function untranslatedLatinPaths(value) {
  const problems = [];
  const visit = (item, location = '$', key = '') => {
    if (FIXED_VALUE_KEYS.has(key)) return;
    if (typeof item === 'string') {
      const prose = item
        .replace(/\\\([\s\S]*?\\\)/g, ' ')
        .replace(/\\\[[\s\S]*?\\\]/g, ' ')
        .replace(/\$[^$]*\$/g, ' ');
      if (/[A-Za-z]{2,}/.test(prose) || /\b[A-Z](?:\s*[-–/]\s*[A-Z]){1,}\b/.test(prose)) {
        problems.push(`${location}: ${prose.replace(/\s+/g, ' ').trim().slice(0, 240)}`);
      }
      return;
    }
    if (Array.isArray(item)) return item.forEach((child, index) => visit(child, `${location}[${index}]`, key));
    if (item && typeof item === 'object') {
      if (typeof item.en === 'string' && typeof item.hi === 'string') return visit(item.hi, `${location}.hi`, 'hi');
      for (const childKey of Object.keys(item)) visit(item[childKey], `${location}.${childKey}`, childKey);
    }
  };
  visit(value);
  return problems;
}

function isBilingualConcepts(concepts) {
  if (!concepts || typeof concepts !== 'object' || !Array.isArray(concepts.sections)) return false;
  let paired = 0;
  let missing = false;
  const visit = (value, key = '') => {
    if (FIXED_VALUE_KEYS.has(key)) return;
    if (typeof value === 'string') { missing = true; return; }
    if (Array.isArray(value)) return value.forEach(item => visit(item, key));
    if (value && typeof value === 'object') {
      if (typeof value.en === 'string' && typeof value.hi === 'string') { paired++; return; }
      for (const childKey of Object.keys(value)) visit(value[childKey], childKey);
    }
  };
  visit(concepts);
  return paired > 0 && !missing;
}

module.exports = {
  assertSameShape,
  buildHindiCleanupPrompt,
  buildHindiTranslationPrompt,
  extractEnglishValues,
  extractHindiValues,
  isBilingualConcepts,
  numericTokenDifferences,
  pairTranslatedValues,
  untranslatedLatinPaths,
};
