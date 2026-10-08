'use strict';

const { applyEdits, compact, editElement, parse, setMetadata } = require('../seo-html.cjs');

function classesOf($, element) {
  return String($(element).attr('class') || '').split(/\s+/).filter(Boolean);
}

function isInsideRange(element, ranges) {
  const location = element?.sourceCodeLocation;
  return Boolean(location && ranges.some(range => location.startOffset >= range.start && location.endOffset <= range.end));
}

function updateStartTag(source, element, update) {
  const location = element?.sourceCodeLocation?.startTag;
  if (!location) throw new Error('HTML element has no source start tag.');
  const original = source.slice(location.startOffset, location.endOffset);
  return {
    start: location.startOffset,
    end: location.endOffset,
    text: update(original),
  };
}

function setClassAttribute(tag, transform) {
  const match = tag.match(/\bclass\s*=\s*(["'])([^"']*)\1/i);
  if (!match) return tag.replace(/>$/, ` class="${transform('')}"`);
  const next = transform(match[2]);
  return tag.slice(0, match.index) + match[0].replace(match[2], next) + tag.slice(match.index + match[0].length);
}

function setAttribute(tag, name, value) {
  const expression = new RegExp(`\\s${name}\\s*=\\s*(["'])[^"']*\\1`, 'i');
  const replacement = ` ${name}="${String(value).replace(/&/g, '&amp;').replace(/"/g, '&quot;')}"`;
  return expression.test(tag) ? tag.replace(expression, replacement) : tag.replace(/>$/, `${replacement}>`);
}

function removeAttribute(tag, name) {
  return tag.replace(new RegExp(`\\s${name}(?:\\s*=\\s*(?:"[^"]*"|'[^']*'|[^\\s>]+))?`, 'i'), '');
}

function stripEnglishLayer(source, subject = 'hindi') {
  let html = String(source);
  let $ = parse(html);
  const removals = [];
  const shared = [];
  $('.lang-en').each((_, element) => {
    const classes = classesOf($, element);
    if (classes.includes('lang-hi')) {
      shared.push(element);
      return;
    }
    let ancestor = element.parent;
    while (ancestor && ancestor.type !== 'root') {
      const ancestorClasses = classesOf($, ancestor);
      if (ancestorClasses.includes('lang-en') && !ancestorClasses.includes('lang-hi')) return;
      ancestor = ancestor.parent;
    }
    removals.push(element);
  });

  const controls = $('#langEn, #langHi, #headerLangToggleBtn, .lang-toggle, .lang-toggle-btn');
  controls.each((_, element) => {
    if (!isInsideRange(element, removals.map(item => item.sourceCodeLocation).filter(Boolean).map(loc => ({ start: loc.startOffset, end: loc.endOffset })))) {
      let ancestor = element.parent;
      while (ancestor && ancestor.type !== 'root') {
        const ancestorClasses = classesOf($, ancestor);
        if (ancestorClasses.includes('lang-en') && !ancestorClasses.includes('lang-hi')) return;
        ancestor = ancestor.parent;
      }
      removals.push(element);
    }
  });

  const removalRanges = removals.map(element => {
    const location = element.sourceCodeLocation;
    if (!location) throw new Error('English-only HTML element has no source location.');
    return { start: location.startOffset, end: location.endOffset };
  });
  const edits = removals.map(element => editElement(element, ''));
  shared.forEach(element => {
    if (isInsideRange(element, removalRanges)) return;
    edits.push(updateStartTag(html, element, tag => setClassAttribute(tag, value =>
      value.split(/\s+/).filter(className => className && className !== 'lang-en').join(' '))));
  });
  html = applyEdits(html, edits);

  $ = parse(html);
  const heading = compact($('.topic-header h1, .syllabus-header h1').first().find('.lang-hi').text()
    || $('.topic-header h1, .syllabus-header h1').first().text());
  const descriptionNode = $('.topic-desc, .syllabus-header > p').first();
  const description = compact(descriptionNode.find('.lang-hi').text() || descriptionNode.text()) || heading;

  const sourceTagEdits = [];
  const htmlLanguage = subject === 'sanskrit' ? 'sa' : 'hi';
  $('html').each((_, element) => sourceTagEdits.push(updateStartTag(html, element, tag => setAttribute(tag, 'lang', htmlLanguage))));
  $('body').each((_, element) => sourceTagEdits.push(updateStartTag(html, element, tag => {
    let result = setClassAttribute(tag, value => [...new Set([...value.split(/\s+/).filter(Boolean), 'lang-hi', 'devanagari-only'])].join(' '));
    return result;
  })));
  $('.breadcrumbs a[href="/"]').each((_, element) => {
    if (compact($(element).text()) !== 'Home') return;
    const location = element.sourceCodeLocation;
    sourceTagEdits.push({ start: location.startTag.endOffset, end: location.endTag.startOffset, text: 'मुख्य पृष्ठ' });
  });
  $('.breadcrumbs a[href="/up-assistant-teacher/"]').each((_, element) => {
    if (!/UP Assistant Teacher/i.test(compact($(element).text()))) return;
    const location = element.sourceCodeLocation;
    sourceTagEdits.push({ start: location.startTag.endOffset, end: location.endTag.startOffset, text: 'उत्तर प्रदेश सहायक अध्यापक' });
  });
  $('.study-tabs').each((_, element) => sourceTagEdits.push(updateStartTag(html, element, tag => setAttribute(tag, 'aria-label', 'विषय सामग्री'))));
  $('#backToTop').each((_, element) => sourceTagEdits.push(updateStartTag(html, element, tag => setAttribute(tag, 'aria-label', 'ऊपर जाएँ'))));
  $('.syllabus-checkbox[aria-label]').each((_, element) => sourceTagEdits.push(updateStartTag(html, element, tag => removeAttribute(tag, 'aria-label'))));
  html = applyEdits(html, sourceTagEdits);
  html = html.replace(/(upsc-language\.min\.js\?v=)[^"'&\s]+/gi, '$1devanagari-only-20261009');

  if (!html.includes('id="devanagari-only-controls"')) {
    const headEnd = html.search(/<\/head\s*>/i);
    if (headEnd >= 0) {
      const style = '<style id="devanagari-only-controls">body.devanagari-only #headerLangToggleBtn,body.devanagari-only #langEn,body.devanagari-only #langHi,body.devanagari-only .lang-toggle,body.devanagari-only .lang-toggle-btn{display:none!important}body.devanagari-only .lang-en:not(.lang-hi){display:none!important}</style>\n';
      html = `${html.slice(0, headEnd)}${style}${html.slice(headEnd)}`;
    }
  }

  if (heading) {
    const subjectLabel = subject === 'sanskrit' ? 'संस्कृत' : 'हिन्दी';
    const title = $('.topic-header').length
      ? `${heading} | ${subjectLabel} | SJMaths`
      : `${heading} - उत्तर प्रदेश सहायक अध्यापक पाठ्यक्रम | SJMaths`;
    html = setMetadata(html, {
      title,
      description,
      'og:title': title,
      'og:description': description,
      'twitter:title': title,
      'twitter:description': description,
    });
  }

  if (!html.includes('devanagari-only')) throw new Error('Could not mark the page as Devanagari-only.');
  return html;
}

module.exports = { stripEnglishLayer };
