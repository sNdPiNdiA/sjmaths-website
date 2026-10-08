const fs = require('fs');
const path = require('path');
const { parse, applyEdits } = require('./seo-html.cjs');

const ROOT = path.resolve(__dirname, '..');
const section = path.join(ROOT, 'up-assistant-teacher/english');
const generator = path.join(section, 'generate-microtopics.cjs');
const translations = new Map([
  ['William Shakespeare - Plays & Sonnets', 'विलियम शेक्सपियर — नाटक एवं सॉनेट'],
  ['Jane Austen - Pride and Prejudice', 'जेन ऑस्टिन — प्राइड एंड प्रेजुडिस'],
  ['Charles Dickens - Great Expectations, Oliver Twist', 'चार्ल्स डिकेंस — ग्रेट एक्सपेक्टेशंस, ओलिवर ट्विस्ट'],
  ['Mark Twain - Adventures of Tom Sawyer', 'मार्क ट्वेन — द एडवेंचर्स ऑफ टॉम सॉयर'],
  ['Rabindranath Tagore - Gitanjali, Kabuliwala', 'रवीन्द्रनाथ टैगोर — गीतांजलि, काबुलीवाला'],
  ['William Wordsworth - Romantic Poetry', 'विलियम वर्ड्सवर्थ — रोमांटिक कविता'],
  ['John Keats - Odes & Sonnets', 'जॉन कीट्स — ओड्स एवं सॉनेट'],
  ['Robert Frost - Modern American Poetry', 'रॉबर्ट फ्रॉस्ट — आधुनिक अमेरिकी कविता'],
  ['T.S. Eliot - Modernist Poetry', 'टी. एस. एलियट — आधुनिकतावादी कविता'],
  ['Poetry Comprehension - Themes & Devices', 'कविता-बोध — विषय-वस्तु एवं काव्य-शिल्प'],
  ['Novel Comprehension - Character Analysis', 'उपन्यास-बोध — पात्र-विश्लेषण'],
  ['Short Story - Plot & Moral', 'लघुकथा — कथानक एवं संदेश'],
  ['Literary Devices - Metaphor, Simile, Alliteration', 'साहित्यिक उपकरण — रूपक, उपमा एवं अनुप्रास'],
  ['Prose Style - Narrative & Descriptive', 'गद्य-शैली — कथात्मक एवं वर्णनात्मक लेखन'],
  ['Vocabulary Building - Synonyms, Antonyms, One-word Substitution', 'शब्दावली-विकास — समानार्थी, विलोम एवं वाक्यांश के लिए एक शब्द'],
]);

function walk(dir, callback) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(file, callback);
    else callback(file);
  }
}

function translateNamedFields(value, stats) {
  if (Array.isArray(value)) {
    value.forEach(item => translateNamedFields(item, stats));
  } else if (value && typeof value === 'object') {
    for (const [key, child] of Object.entries(value)) {
      if (key === 'hindiName' && translations.has(child)) {
        value[key] = translations.get(child);
        stats.jsonFields++;
      } else {
        translateNamedFields(child, stats);
      }
    }
  }
}

const stats = { generatorEntries: 0, htmlLanguageLabels: 0, jsonFields: 0, embeddedJsonFields: 0 };
const originalGenerator = fs.readFileSync(generator, 'utf8');
let source = originalGenerator;
for (const [english, hindi] of translations) {
  const escaped = english.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const pattern = new RegExp(`(hindiName:\\s*')${escaped}(')`, 'g');
  source = source.replace(pattern, (_, before, after) => {
    stats.generatorEntries++;
    return `${before}${hindi}${after}`;
  });
}
if (source !== originalGenerator) fs.writeFileSync(generator, source);

walk(section, file => {
  if (file.endsWith('.json')) {
    const before = fs.readFileSync(file, 'utf8');
    const parsed = JSON.parse(before);
    const countBefore = stats.jsonFields;
    translateNamedFields(parsed, stats);
    if (stats.jsonFields !== countBefore) fs.writeFileSync(file, `${JSON.stringify(parsed, null, 2)}\n`);
    return;
  }
  if (!file.endsWith('.html')) return;

  const before = fs.readFileSync(file, 'utf8');
  const $ = parse(before);
  const edits = [];
  $('.lang-hi').each((_, element) => {
    const english = $(element).text().replace(/\s+/g, ' ').trim();
    const hindi = translations.get(english);
    const location = element.sourceCodeLocation;
    if (!hindi || !location?.startTag || !location?.endTag) return;
    edits.push({ start: location.startTag.endOffset, end: location.endTag.startOffset, text: hindi });
    stats.htmlLanguageLabels++;
  });
  $('script[type="application/json"]').each((_, element) => {
    const text = $(element).html();
    let parsed;
    try { parsed = JSON.parse(text); } catch { return; }
    const countBefore = stats.jsonFields;
    translateNamedFields(parsed, stats);
    const changed = stats.jsonFields - countBefore;
    if (!changed) return;
    const location = element.sourceCodeLocation;
    if (!location?.startTag || !location?.endTag) return;
    edits.push({ start: location.startTag.endOffset, end: location.endTag.startOffset, text: `\n${JSON.stringify(parsed, null, 2)}\n` });
    stats.embeddedJsonFields += changed;
  });
  if (edits.length) fs.writeFileSync(file, applyEdits(before, edits));
});

console.log(JSON.stringify(stats, null, 2));
