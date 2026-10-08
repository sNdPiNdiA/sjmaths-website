'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const {
  assertSameShape,
  buildHindiTranslationPrompt,
  extractEnglishValues,
  extractHindiValues,
  isBilingualConcepts,
  numericTokenDifferences,
  pairTranslatedValues,
  untranslatedLatinPaths,
} = require('./lib/up-assistant-bilingual.cjs');

const english = {
  sections: [
    { title: 'Overview', type: 'table', headers: ['Aspect'], rows: [['Swar', 'Vowels']] },
    { title: 'Notes', type: 'list', items: [{ term: 'Rule', definition: 'Read this carefully.' }] },
  ],
  upscNotes: [{ type: 'tip', content: 'Remember the rule.' }],
  keyTakeaways: ['Use the correct form.'],
};
const hindi = {
  sections: [
    { title: 'परिचय', type: 'table', headers: ['पहलू'], rows: [['स्वर', 'स्वर ध्वनियाँ']] },
    { title: 'टिप्पणियाँ', type: 'list', items: [{ term: 'नियम', definition: 'इसे ध्यान से पढ़ें।' }] },
  ],
  upscNotes: [{ type: 'tip', content: 'नियम याद रखें।' }],
  keyTakeaways: ['सही रूप का प्रयोग करें।'],
};

test('pairs Hindi content without replacing English and keeps renderer enums unchanged', () => {
  const paired = pairTranslatedValues(english, hindi);
  assert.deepEqual(paired.sections[0].title, { en: 'Overview', hi: 'परिचय' });
  assert.deepEqual(paired.sections[0].rows[0][0], { en: 'Swar', hi: 'स्वर' });
  assert.equal(paired.sections[0].type, 'table');
  assert.equal(paired.upscNotes[0].type, 'tip');
  assert.equal(isBilingualConcepts(paired), true);
  assert.equal(isBilingualConcepts(english), false);
});

test('rejects translation output that changes educational content structure', () => {
  assert.throws(() => assertSameShape(english, { ...hindi, sections: hindi.sections.slice(0, 1) }), /array shape/);
  assert.throws(() => assertSameShape(english, { ...hindi, sections: [{ ...hindi.sections[0], rows: [['पहलू']] }, hindi.sections[1]] }), /array shape/);
  assert.throws(() => assertSameShape(english, { ...hindi, upscNotes: [{ type: 'बख्शीश', content: 'नियम याद रखें।' }] }), /structural enum/);
});

test('translation prompt requires Devanagari while preserving structure and facts', () => {
  const hindiPrompt = buildHindiTranslationPrompt(english, 'hindi');
  const sanskritPrompt = buildHindiTranslationPrompt(english, 'sanskrit');
  assert.match(hindiPrompt, /natural, student-friendly Hindi in Devanagari/);
  assert.match(sanskritPrompt, /Sanskrit grammatical terms, forms, verses, and examples in correct Devanagari/);
  assert.match(sanskritPrompt, /प्रथम पुरुष means third person/);
  assert.match(hindiPrompt, /English glosses in parentheses/);
  assert.match(hindiPrompt, /Convert Roman numerals that denote values/);
  assert.match(hindiPrompt, /same keys, value types, array lengths, and ordering/);
});

test('finds untranslated Latin prose in the Hindi layer but ignores formulas', () => {
  const paired = pairTranslatedValues(english, hindi);
  paired.sections[0].headers[0].hi = 'Aspect';
  paired.sections[0].rows[0][0].hi = 'Swar';
  paired.sections[1].items[0].definition.hi = 'इसे ध्यान से पढ़ें। $x^2 + y^2 = 1$';
  assert.deepEqual(extractEnglishValues(paired).sections[0].headers[0], 'Aspect');
  const issues = untranslatedLatinPaths(paired);
  assert.equal(issues.length, 2);
  assert.match(issues[0], /Aspect/);
  assert.match(issues[1], /Swar/);
});

test('preserves numeric facts while accepting Devanagari digit forms', () => {
  const source = { count: '52 letters; 11 vowels; 0.5 ratio' };
  const translated = { count: '५२ वर्ण; ११ स्वर; ०.५ अनुपात' };
  assert.deepEqual(numericTokenDifferences(source, translated), []);
  assert.deepEqual(numericTokenDifferences(source, { count: '५१ वर्ण; ११ स्वर; ०.५ अनुपात' }), [
    '$.count: source [52, 11, 0.5] "52 letters; 11 vowels; 0.5 ratio"; Hindi [51, 11, 0.5] "५१ वर्ण; ११ स्वर; ०.५ अनुपात"',
  ]);
  const paired = pairTranslatedValues(source, translated);
  assert.deepEqual(extractEnglishValues(paired), source);
  assert.deepEqual(extractHindiValues(paired), translated);
  assert.deepEqual(
    numericTokenDifferences({ points: '1. First point; 10 examples.' }, { points: 'प्रथम बिंदु; दस उदाहरण।' }),
    [],
    'Hindi number words and ordinals preserve the same numeric facts',
  );
  assert.deepEqual(
    numericTokenDifferences({ points: 'one, two and fifth' }, { points: 'एक, दो और पाँचवीं' }),
    [],
    'spelled-out source numbers can match their Hindi equivalents',
  );
  assert.deepEqual(numericTokenDifferences({ points: '33 letters' }, { points: 'तैंतीस वर्ण' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Correct matras (I, II, U, U)' }, { point: 'मात्राओं (इ, ई, उ, ऊ)' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'zero marks' }, { point: 'शून्य चिह्न' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'first and one' }, { point: 'सर्वप्रथम और एक।' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'A concept' }, { point: 'एक अवधारणा' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'First and second' }, { point: 'द्वितीय और प्रथम' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'four options' }, { point: 'चारों विकल्प' }), []);
  assert.deepEqual(numericTokenDifferences({ point: '5S-BIMB means 5 senses' }, { point: 'पंच-बिम्ब सूत्र; 5 इंद्रिय' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'one of four pillars' }, { point: 'चार स्तंभों में से एक।' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Threefold merit' }, { point: 'त्रिविध गुण' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Act VII' }, { point: 'अंक ७' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Twelfth and thirteenth Parva' }, { point: 'बारहवां और तेरहवां पर्व' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'zero negative ambiguity' }, { point: 'बिना किसी नकारात्मक अस्पष्टता के' }), []);
  assert.deepEqual(numericTokenDifferences({ point: '3rd, 4th, 5th, 1st and 2nd' }, { point: 'तीसरे, चौथे, पाँचवें, पहले और दूसरे' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'One should not act hastily.' }, { point: 'जल्दबाजी में कार्य नहीं करना चाहिए।' }), []);
  assert.deepEqual(numericTokenDifferences({ point: 'One action is required.' }, { point: 'एक कार्य आवश्यक है।' }), []);
  assert.deepEqual(numericTokenDifferences({ point: '1st, 2nd, 3rd, 4th, 5th, 6th, 7th case' }, { point: 'प्रथमा, द्वितीया, तृतीया, चतुर्थी, पंचमी, षष्ठी, सप्तमी विभक्ति' }), []);
  assert.deepEqual(
    numericTokenDifferences(
      { points: '1st person, 2nd person, 3rd person' },
      { points: 'उत्तम पुरुष, मध्यम पुरुष, प्रथम पुरुष' },
      'sanskrit',
    ),
    [],
  );
  assert.deepEqual(
    numericTokenDifferences(
      { points: '1st, 2nd, 3rd person' },
      { points: 'पुरुष (उत्तम, मध्यम, प्रथम)' },
      'sanskrit',
    ),
    [],
  );
  assert.deepEqual(
    numericTokenDifferences({ point: '1st person' }, { point: 'प्रथम पुरुष' }, 'sanskrit').length,
    1,
    'Sanskrit प्रथम पुरुष means third person, not first person',
  );
  assert.deepEqual(numericTokenDifferences({ point: 'Ten hasyate' }, { point: 'तेन हस्यते' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences({ point: 'First Future / Periphrastic' }, { point: 'अनद्यतन भविष्यत्' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Twenty-two prefixes' }, { point: 'बाईस उपसर्ग' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences({ point: 'PRA-PARA-VI-ANG-NI' }, { point: 'प्र-परा-वि-आङ्-नि' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences({ point: 'First Poet of Sanskrit' }, { point: 'संस्कृत के आदि कवि' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Dvigu is a numeral first member.' }, { point: 'द्विगु तत्पुरुष में संख्यावाची प्रथम पद होता है।' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences({ point: 'Classification of the Navarasa (Nine Rasas)' }, { point: 'नवरस का वर्गीकरण' }, 'sanskrit'), []);
  assert.deepEqual(numericTokenDifferences(
    { point: 'Match first, second, or third person.' },
    { point: 'प्रथम, मध्यम, या उत्तम पुरुष।' },
    'sanskrit',
  ), []);
});
