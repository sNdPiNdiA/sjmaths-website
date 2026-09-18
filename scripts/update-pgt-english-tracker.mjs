import fs from 'fs';

console.log('Updating up-pgt-english/index.html...');
let html = fs.readFileSync('up-pgt-english/index.html', 'utf8');

// 1. SECTION 1 (Language):
// Replace individual synonyms and antonyms with consolidated chapter
const oldSynAnt = `<div class="topic" data-key="language/vocabulary/synonyms" data-relevance="pgt" data-search="language synonyms pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Synonyms complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/language/vocabulary/synonyms/">Synonyms</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/language/vocabulary/synonyms/" aria-label="Open Synonyms">→</a>
            </div><div class="topic" data-key="language/vocabulary/antonyms" data-relevance="pgt" data-search="language antonyms pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Antonyms complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/language/vocabulary/antonyms/">Antonyms</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/language/vocabulary/antonyms/" aria-label="Open Antonyms">→</a>
            </div>`;

const newSynAnt = `<div class="topic" data-key="language/vocabulary/synonyms-and-antonyms" data-relevance="pgt" data-search="language synonyms antonyms vocabulary building pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Synonyms &amp; Antonyms complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/language/vocabulary/synonyms-and-antonyms/">Synonyms, Antonyms &amp; Vocabulary Building</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/language/vocabulary/synonyms-and-antonyms/" aria-label="Open Synonyms &amp; Antonyms">→</a>
            </div>`;

html = html.replace(oldSynAnt, newSynAnt);

// Flatten jumbled sentences URL
html = html.replace(
  /\/english\/language\/grammar\/sentence-rearrangement\/jumbled-sentences\//g,
  '/english/language/grammar/sentence-rearrangement/'
);
html = html.replace(
  'data-key="language/grammar/sentence-rearrangement/jumbled-sentences"',
  'data-key="language/grammar/sentence-rearrangement"'
);

// Replace prefixes & suffixes with Word Formation: Prefixes, Suffixes, and Root Words
const oldAffixes = `<div class="topic" data-key="language/vocabulary/prefixes" data-relevance="pgt" data-search="language prefixes pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Prefixes complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/language/vocabulary/prefixes/">Prefixes</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/language/vocabulary/prefixes/" aria-label="Open Prefixes">→</a>
            </div><div class="topic" data-key="language/vocabulary/suffixes" data-relevance="pgt" data-search="language suffixes pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Suffixes complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/language/vocabulary/suffixes/">Suffixes</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/language/vocabulary/suffixes/" aria-label="Open Suffixes">→</a>
            </div>`;

const newAffixes = `<div class="topic" data-key="language/vocabulary/word-formation-prefixes-suffixes" data-relevance="pgt" data-search="language word formation prefixes suffixes root words pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Word Formation (Prefixes &amp; Suffixes) complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/language/vocabulary/word-formation-prefixes-suffixes/">Word Formation: Prefixes, Suffixes &amp; Roots</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/language/vocabulary/word-formation-prefixes-suffixes/" aria-label="Open Word Formation">→</a>
            </div>`;

html = html.replace(oldAffixes, newAffixes);

// Update Language section topic count in desc from 16 to 14
html = html.replace(
  '<span><span class="section-title">Language</span><span class="section-desc">16 syllabus topics</span></span>',
  '<span><span class="section-title">Language</span><span class="section-desc">14 syllabus topics</span></span>'
);
html = html.replace(
  '<span data-section-done="section-1-language">0</span> / 16',
  '<span data-section-done="section-1-language">0</span> / 14'
);

// 2. SECTION 2B (Figures of Speech - Option 1b: 3 clusters):
const oldFigures = `<div class="topic-list"><div class="topic" data-key="literature/figures-of-speech/simile" data-relevance="pgt" data-search="figures of speech simile pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Simile complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/simile/">Simile</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/simile/" aria-label="Open Simile">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/metaphor" data-relevance="pgt" data-search="figures of speech metaphor pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Metaphor complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/metaphor/">Metaphor</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/metaphor/" aria-label="Open Metaphor">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/personification" data-relevance="pgt" data-search="figures of speech personification pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Personification complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/personification/">Personification</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/personification/" aria-label="Open Personification">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/hyperbole" data-relevance="pgt" data-search="figures of speech hyperbole pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Hyperbole complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/hyperbole/">Hyperbole</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/hyperbole/" aria-label="Open Hyperbole">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/alliteration" data-relevance="pgt" data-search="figures of speech alliteration pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Alliteration complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/alliteration/">Alliteration</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/alliteration/" aria-label="Open Alliteration">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/onomatopoeia" data-relevance="pgt" data-search="figures of speech onomatopoeia pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Onomatopoeia complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/onomatopoeia/">Onomatopoeia</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/onomatopoeia/" aria-label="Open Onomatopoeia">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/oxymoron" data-relevance="pgt" data-search="figures of speech oxymoron pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Oxymoron complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/oxymoron/">Oxymoron</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/oxymoron/" aria-label="Open Oxymoron">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/pun" data-relevance="pgt" data-search="figures of speech pun pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Pun complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/pun/">Pun</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/pun/" aria-label="Open Pun">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/synecdoche" data-relevance="pgt" data-search="figures of speech synecdoche pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Synecdoche complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/synecdoche/">Synecdoche</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/synecdoche/" aria-label="Open Synecdoche">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/metonymy" data-relevance="pgt" data-search="figures of speech metonymy pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Metonymy complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/metonymy/">Metonymy</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/metonymy/" aria-label="Open Metonymy">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/euphemism" data-relevance="pgt" data-search="figures of speech euphemism pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Euphemism complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/euphemism/">Euphemism</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/euphemism/" aria-label="Open Euphemism">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/apostrophe" data-relevance="pgt" data-search="figures of speech apostrophe pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Apostrophe complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/apostrophe/">Apostrophe</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/apostrophe/" aria-label="Open Apostrophe">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/antithesis" data-relevance="pgt" data-search="figures of speech antithesis pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Antithesis complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/antithesis/">Antithesis</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/antithesis/" aria-label="Open Antithesis">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/transferred-epithet" data-relevance="pgt" data-search="figures of speech transferred epithet pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Transferred Epithet complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/transferred-epithet/">Transferred Epithet</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/transferred-epithet/" aria-label="Open Transferred Epithet">→</a>
            </div></div>`;

const newFigures = `<div class="topic-list"><div class="topic" data-key="literature/figures-of-speech/figures-of-comparison-and-association" data-relevance="pgt" data-search="figures of speech comparison association simile metaphor personification apostrophe metonymy synecdoche pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Figures of Comparison &amp; Association complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/figures-of-comparison-and-association/">Figures of Comparison &amp; Association (Simile, Metaphor, Personification, Metonymy, Synecdoche, Apostrophe)</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/figures-of-comparison-and-association/" aria-label="Open Figures of Comparison &amp; Association">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/figures-of-contrast-and-emphasis" data-relevance="pgt" data-search="figures of speech contrast emphasis antithesis oxymoron hyperbole euphemism transferred epithet pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Figures of Contrast &amp; Emphasis complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/figures-of-contrast-and-emphasis/">Figures of Contrast &amp; Emphasis (Antithesis, Oxymoron, Hyperbole, Euphemism, Transferred Epithet)</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/figures-of-contrast-and-emphasis/" aria-label="Open Figures of Contrast &amp; Emphasis">→</a>
            </div><div class="topic" data-key="literature/figures-of-speech/figures-of-sound-and-wordplay" data-relevance="pgt" data-search="figures of speech sound wordplay alliteration onomatopoeia pun pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Figures of Sound &amp; Wordplay complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/figures-of-speech/figures-of-sound-and-wordplay/">Figures of Sound &amp; Wordplay (Alliteration, Onomatopoeia, Pun)</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/figures-of-speech/figures-of-sound-and-wordplay/" aria-label="Open Figures of Sound &amp; Wordplay">→</a>
            </div></div>`;

html = html.replace(oldFigures, newFigures);
html = html.replace(
  '<span><span class="section-title">Figures of Speech</span><span class="section-desc">14 syllabus topics</span></span>',
  '<span><span class="section-title">Figures of Speech</span><span class="section-desc">3 syllabus topics</span></span>'
);
html = html.replace(
  '<span data-section-done="section-3-figures-of-speech">0</span> / 14',
  '<span data-section-done="section-3-figures-of-speech">0</span> / 3'
);

// 3. SECTION 2C (Rhetoric and Prosody):
const oldRhetoric = `<div class="topic-list"><div class="topic" data-key="literature/rhetoric-and-prosody/rhetoric" data-relevance="pgt" data-search="rhetoric and prosody rhetoric pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Rhetoric complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/rhetoric-and-prosody/rhetoric/">Rhetoric</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/rhetoric-and-prosody/rhetoric/" aria-label="Open Rhetoric">→</a>
            </div><div class="topic" data-key="literature/rhetoric-and-prosody/prosody" data-relevance="pgt" data-search="rhetoric and prosody prosody pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Prosody complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/rhetoric-and-prosody/prosody/">Prosody</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/rhetoric-and-prosody/prosody/" aria-label="Open Prosody">→</a>
            </div></div>`;

const newRhetoric = `<div class="topic-list"><div class="topic" data-key="literature/rhetoric-and-prosody" data-relevance="pgt" data-search="rhetoric and prosody classical devices metrical feet scansion pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Rhetoric and Prosody complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/rhetoric-and-prosody/">Rhetoric and Prosody (Classical Devices &amp; Scansion)</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/rhetoric-and-prosody/" aria-label="Open Rhetoric and Prosody">→</a>
            </div></div>`;

html = html.replace(oldRhetoric, newRhetoric);
html = html.replace(
  '<span><span class="section-title">Rhetoric and Prosody</span><span class="section-desc">2 syllabus topics</span></span>',
  '<span><span class="section-title">Rhetoric and Prosody</span><span class="section-desc">1 syllabus topic</span></span>'
);
html = html.replace(
  '<span data-section-done="section-4-rhetoric-and-prosody">0</span> / 2',
  '<span data-section-done="section-4-rhetoric-and-prosody">0</span> / 1'
);

// 4. SECTION 2D (Poetic Forms: Epic and Mock-Epic unified):
const oldEpic = `<div class="topic" data-key="literature/poetic-forms/epic" data-relevance="pgt" data-search="major stanza forms epic pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Epic complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/poetic-forms/epic/">Epic</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/poetic-forms/epic/" aria-label="Open Epic">→</a>
            </div><div class="topic" data-key="literature/poetic-forms/mock-epic" data-relevance="pgt" data-search="major stanza forms mock epic pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Mock Epic complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/poetic-forms/mock-epic/">Mock Epic</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/poetic-forms/mock-epic/" aria-label="Open Mock Epic">→</a>
            </div>`;

const newEpic = `<div class="topic" data-key="literature/poetic-forms/epic-and-mock-epic" data-relevance="pgt" data-search="major stanza forms epic and mock epic heroi-comical satire pgt only">
              <label class="check-wrap" title="Mark complete"><input class="topic-check" type="checkbox" aria-label="Mark Epic and Mock-Epic complete"></label>
              <div class="topic-main"><a class="topic-link" href="/english/literature/poetic-forms/epic-and-mock-epic/">Epic &amp; Mock-Epic</a><div class="topic-tags"><span class="exam-tag only">PGT Only</span></div></div>
              <a class="open-link" href="/english/literature/poetic-forms/epic-and-mock-epic/" aria-label="Open Epic &amp; Mock-Epic">→</a>
            </div>`;

html = html.replace(oldEpic, newEpic);
html = html.replace(
  '<span><span class="section-title">Major Stanza Forms</span><span class="section-desc">7 syllabus topics</span></span>',
  '<span><span class="section-title">Major Stanza Forms</span><span class="section-desc">6 syllabus topics</span></span>'
);
html = html.replace(
  '<span data-section-done="section-5-major-stanza-forms">0</span> / 7',
  '<span data-section-done="section-5-major-stanza-forms">0</span> / 6'
);

// Update overall PGT counts
// Total PGT topics was 74.
// Removed: 1 syn/ant (-1), 1 affixes (-1), 11 figures of speech (-11), 1 rhetoric (-1), 1 epic (-1) = 74 - 15 = 59 topics
html = html.replace(/74 Tracked Topics/g, '59 Tracked Topics');
html = html.replace(/74<br>topics complete/g, '59<br>topics complete');
html = html.replace(/id="pendingStat">74<\/strong>/g, 'id="pendingStat">59<\/strong>');
html = html.replace(/>74<\/span><span>Total tracked topics/g, '>59</span><span>Total tracked topics');
html = html.replace(/>64<\/span><span>PGT Only/g, '>49</span><span>PGT Only');

fs.writeFileSync('up-pgt-english/index.html', html, 'utf8');
console.log('✓ up-pgt-english/index.html updated successfully.');
