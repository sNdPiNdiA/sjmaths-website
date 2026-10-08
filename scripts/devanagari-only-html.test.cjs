'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { parse } = require('./seo-html.cjs');
const { stripEnglishLayer } = require('./lib/devanagari-only-html.cjs');

test('removes English UI and content while preserving the Devanagari layer', () => {
  const source = `<!doctype html>
<html lang="en"><head><title>English title</title><meta name="description" content="English description"></head>
<body class="exam-ui"><main class="topic-container" id="main-content">
<div class="breadcrumbs"><a href="/">Home</a><a href="/up-assistant-teacher/">UP Assistant Teacher</a></div>
<div class="topic-header"><h1><span class="lang-en">English topic</span><span class="lang-hi">विषय का नाम</span></h1><p class="topic-desc"><span class="lang-en">English notes.</span><span class="lang-hi">हिन्दी विवरण।</span></p></div>
<a class="lang-en lang-hi">साझा हिन्दी पाठ</a>
<div class="study-tabs" aria-label="Topic resources"><button><span class="lang-en">Practice</span><span class="lang-hi">अभ्यास</span></button></div>
<button id="langEn">English</button><button id="langHi">हिन्दी</button><button id="headerLangToggleBtn">English</button>
<div id="topic-content"><div class="lang-en">English lesson text</div><div class="lang-hi">देवनागरी पाठ</div></div>
</main><button id="backToTop" aria-label="Back to Top"></button></body></html>`;
  const $ = parse(stripEnglishLayer(source, 'hindi'));
  assert.equal($('html').attr('lang'), 'hi');
  assert.ok($('body').hasClass('lang-hi'));
  assert.ok($('body').hasClass('devanagari-only'));
  assert.equal($('.lang-en').length, 0);
  assert.equal($('#langEn, #langHi, #headerLangToggleBtn').length, 0);
  assert.equal($('#topic-content').text().trim(), 'देवनागरी पाठ');
  assert.equal($('.breadcrumbs').text().replace(/\s+/g, ' ').trim(), 'मुख्य पृष्ठउत्तर प्रदेश सहायक अध्यापक');
  assert.equal($('.lang-hi').text().includes('साझा हिन्दी पाठ'), true);
  assert.equal($('.study-tabs').attr('aria-label'), 'विषय सामग्री');
  assert.equal($('#backToTop').attr('aria-label'), 'ऊपर जाएँ');
  assert.equal($('title').text(), 'विषय का नाम | हिन्दी | SJMaths');
  assert.equal($('meta[name="description"]').attr('content'), 'हिन्दी विवरण।');
});

test('writes the language-specific label into the title for Sanskrit pages', () => {
  const source = '<html><head><title>Sanskrit</title></head><body><main class="topic-container"><div class="topic-header"><h1><span class="lang-hi">बल</span><span class="lang-en">Force</span></h1><p class="topic-desc"><span class="lang-hi">बल का विवरण।</span><span class="lang-en">Force details.</span></p></div></main></body></html>';
  const $ = parse(stripEnglishLayer(source, 'sanskrit'));
  assert.equal($('html').attr('lang'), 'sa');
  assert.equal($('title').text(), 'बल | संस्कृत | SJMaths');
  assert.equal($('.lang-en').length, 0);
});
