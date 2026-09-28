const fs = require('fs');

const updates = {
  'military-science/india-national-security/neighbouring-countries/security-problems/index.html': {
    title: "India&#39;s Security Problems &amp; Neighbouring Countries | UP PGT Military Science | SJ Maths"
  },
  'military-science/science-technology-and-security/scientific-and-technological-base/index.html': {
    title: 'Scientific and Technological Base for National Security | UP PGT Military Science | SJ Maths'
  },
  'music-vocal/raga-theory/anuvadi/index.html': {
    title: 'अनुवादी स्वर: राग सिद्धांत | UP PGT संगीत गायन | SJ Maths'
  },
  'up-tgt-pgt-gk/art-culture/unesco-sites/index.html': {
    title: 'UNESCO World Heritage Sites in India | UP TGT/PGT Art &amp; Culture | SJ Maths'
  },
  'up-tgt-pgt-gk/art-culture/up-gharanas/index.html': {
    title: 'UP Music Gharanas: Lucknow, Banaras, Kirana &amp; Agra | UP TGT/PGT | SJ Maths'
  },
  'up-tgt-pgt-gk/general-science/carbon-compounds/index.html': {
    title: 'Carbon, Allotropes, Soaps &amp; Detergents | UP TGT/PGT Science | SJ Maths'
  },
  'up-tgt-pgt-gk/general-science/cell-structure/index.html': {
    title: 'Cell Structure &amp; Genetics: DNA, RNA and Mendel&#39;s Laws | UP TGT/PGT | SJ Maths'
  },
  'up-tgt-pgt-gk/general-science/communicable-diseases/index.html': {
    title: 'Diseases &amp; Immunization: Vaccines and Antibiotics | UP TGT/PGT Science | SJ Maths'
  },
  'up-tgt-pgt-gk/general-science/human-systems/index.html': {
    title: 'Human Body Systems: Digestive, Circulatory &amp; Nervous | UP TGT/PGT | SJ Maths'
  },
  'up-tgt-pgt-gk/indian-history/mughal-empire/index.html': {
    title: 'Mughal Empire &amp; Administration: Akbar, Mansabdari and Revenue | UP TGT/PGT | SJ Maths'
  },
  'up-tgt-pgt-gk/indian-history/social-reform/index.html': {
    title: 'Socio-Religious Reform Movements in 19th-Century India | UP TGT/PGT | SJ Maths'
  },
  'up-tgt-pgt-gk/indian-history/vijayanagara/index.html': {
    title: 'Vijayanagara &amp; Bahmani Kingdoms: History and Culture | UP TGT/PGT | SJ Maths'
  },
  'ssc-cgl/english/fill-in-the-blanks/index.html': {
    title: 'Fill in the Blanks for SSC CGL Tier 1 &amp; Tier 2 | SJMaths'
  },
  'ssc-cgl/english/fill-in-the-blanks/fill-in-the-blanks-single-double-blanks-vocabulary-grammar-fits/index.html': {
    title: 'Fill in the Blanks: Single/Double Blanks &amp; Vocabulary | SSC CGL | SJMaths'
  },
  'ssc-cgl/english/one-word-substitution/index.html': {
    title: 'One Word Substitution for SSC CGL Tier 1 &amp; Tier 2 | SJMaths'
  },
  'ssc-cgl/english/one-word-substitution/one-word-substitution-categories/index.html': {
    title: 'One Word Substitution: Categories | SSC CGL | SJMaths'
  },
  'ssc-cgl/english/sentence-correction/index.html': {
    title: 'Sentence Correction for SSC CGL Tier 1 &amp; Tier 2 | SJMaths'
  },
  'ssc-cgl/english/sentence-correction/sentence-correction-improvement-tense-syntax-modifier-placement/index.html': {
    title: 'Sentence Correction &amp; Improvement: Tense and Syntax | SSC CGL | SJMaths'
  },
  'ssc-cgl/finance-economics/single-and-double-entry/index.html': {
    title: 'Single and Double Entry for SSC CGL: Books of Original Entry | SJMaths',
    description: 'Learn single and double entry accounting for SSC CGL Tier 1 &amp; Tier 2 with key concepts, notes, formulas, practice questions and self-evaluation.'
  },
  'ssc-cgl/finance-economics/single-and-double-entry-books-of-original-entry/index.html': {
    title: 'Single and Double Entry: Books of Original Entry | SSC CGL | SJMaths',
    description: 'Study books of original entry and single/double entry accounting for SSC CGL Tier 1 &amp; Tier 2 with concepts, examples, practice questions and self-evaluation.'
  },
  'military-science/international-security/emerging-dimensions-of-world-security/index.html': {
    description: 'International terrorism and world security: structured Military Science study notes on terrorism typology, networks, counter-terrorism and India for UP PGT preparation.'
  },
  'military-science/international-security/international-terrorism/index.html': {
    description: 'International terrorism: structured Military Science study notes on state sponsorship, financing, counter-terrorism and future threats for UP PGT preparation.'
  },
  'music-vocal/comparison/hindustani-and-carnatic/notes/index.html': {
    description: 'हिंदुस्तानी और कर्नाटक स्वरों की तुलना: Music Vocal के लिए हिन्दी अध्ययन नोट्स, अवधारणा क्विज़, पुनरावृत्ति सारांश और विषय परीक्षा।'
  },
  'music-vocal/comparison/hindustani-and-carnatic/swaras-notes/index.html': {
    description: 'कर्नाटक और हिन्दुस्तानी स्वरों की तुलना: Music Vocal के लिए हिन्दी अध्ययन नोट्स, अवधारणा क्विज़, पुनरावृत्ति सारांश और विषय परीक्षा।'
  },
  'sanskrit/bharatiya-darshana/vedanta-sara/brahma-ka-svarupa/index.html': {
    ogImage: 'https://sjmaths.com/assets/icons/icon-512x512.png'
  }
};

function setMeta(head, attribute, key, value) {
  const escapedKey = key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const expression = new RegExp(`<meta\\b(?=[^>]*\\b${attribute}=["']${escapedKey}["'])[^>]*>`, 'i');
  if (!expression.test(head)) return { head, changed: false };
  return {
    head: head.replace(expression, `<meta ${attribute}="${key}" content="${value}">`),
    changed: true
  };
}

let changedFiles = 0;
for (const [file, update] of Object.entries(updates)) {
  const original = fs.readFileSync(file, 'utf8');
  const closingHead = original.toLowerCase().indexOf('</head>');
  if (closingHead < 0) throw new Error(`Missing </head>: ${file}`);

  let head = original.slice(0, closingHead);
  const body = original.slice(closingHead);
  const oldTitle = (head.match(/<title\b[^>]*>([\s\S]*?)<\/title>/i) || [])[1];
  const oldDescriptionTag = (head.match(/<meta\b(?=[^>]*\bname=["']description["'])[^>]*>/i) || [])[0];
  const oldDescription = oldDescriptionTag && (oldDescriptionTag.match(/\bcontent=["']([^"']*)["']/i) || [])[1];

  if (update.title) {
    const titleExpression = /<title\b[^>]*>[\s\S]*?<\/title>/i;
    if (!titleExpression.test(head)) throw new Error(`Missing title: ${file}`);
    head = head.replace(titleExpression, `<title>${update.title}</title>`);
    for (const [attribute, key] of [['property', 'og:title'], ['name', 'twitter:title']]) {
      const result = setMeta(head, attribute, key, update.title);
      if (!result.changed) throw new Error(`Missing ${key}: ${file}`);
      head = result.head;
    }
    if (oldTitle) head = head.split(oldTitle).join(update.title);
  }

  if (update.description) {
    for (const [attribute, key] of [['name', 'description'], ['property', 'og:description'], ['name', 'twitter:description']]) {
      const result = setMeta(head, attribute, key, update.description);
      if (!result.changed) throw new Error(`Missing ${key}: ${file}`);
      head = result.head;
    }
    if (oldDescription) head = head.split(oldDescription).join(update.description);
  }

  if (update.ogImage && !/<meta\b[^>]*property=["']og:image["']/i.test(head)) {
    const ogUrlExpression = /<meta\b[^>]*property=["']og:url["'][^>]*>/i;
    if (!ogUrlExpression.test(head)) throw new Error(`Missing og:url: ${file}`);
    head = head.replace(ogUrlExpression, match => `${match}\n<meta property="og:image" content="${update.ogImage}">`);
  }

  if (head !== original.slice(0, closingHead)) {
    fs.writeFileSync(file, head + body, 'utf8');
    changedFiles += 1;
    console.log(`updated ${file}`);
  }
}

console.log(`Updated ${changedFiles} files.`);
