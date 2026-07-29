/**
 * Update the PAGE_TEMPLATE in upsc-microtopic-template.js to include:
 * 1. Premium styles (dark mode, responsive, animations)
 * 2. Language toggle buttons and script
 * 3. Failsafe overlay script
 * 4. Debug helpers script
 */
const fs = require('fs');

const templatePath = 'upsc/upsc-microtopic-template.js';
const sourcePath = 'upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/index.html';

console.log('Reading source template...');
const source = fs.readFileSync(sourcePath, 'utf8');

// Extract the premium <style> block
const styleStart = source.indexOf('<style>');
const styleEnd = source.indexOf('</style>', styleStart) + 8;
const premiumStyles = source.substring(styleStart, styleEnd);

// Extract the language toggle buttons (in the topic-meta-bar)
const metaBarStart = source.indexOf('<div class="topic-meta-bar">');
const metaBarEnd = source.indexOf('</div>', metaBarStart) + 6;
const metaBarContent = source.substring(metaBarStart, metaBarEnd);

// Extract all scripts from the template's footer section (after "Reusable renderers")
const reusableRenderersIdx = source.indexOf('<!-- Reusable renderers -->');
const footerSection = source.substring(reusableRenderersIdx);

// Extract language toggle script, failsafe script, debug script separately
const langToggleIdx = source.indexOf('// Language toggle:');
// Find the opening <script> tag before this comment
let langScriptOpen = langToggleIdx;
while (langScriptOpen > 0 && source.substring(langScriptOpen - 8, langScriptOpen).indexOf('<script>') === -1) {
    langScriptOpen--;
}
const langScriptClose = source.indexOf('</script>', langToggleIdx) + 9;
const langToggleScript = source.substring(langScriptOpen, langScriptClose);

// Failsafe script
const failsafeIdx = source.indexOf('// Failsafe:');
let failsafeOpen = failsafeIdx;
while (failsafeOpen > 0 && source.substring(failsafeOpen - 8, failsafeOpen).indexOf('<script>') === -1) {
    failsafeOpen--;
}
const failsafeClose = source.indexOf('</script>', failsafeIdx) + 9;
const failsafeScript = source.substring(failsafeOpen, failsafeClose);

// Debug helpers script
const debugIdx = source.indexOf('// Debug helpers:');
let debugOpen = debugIdx;
while (debugOpen > 0 && source.substring(debugOpen - 8, debugOpen).indexOf('<script>') === -1) {
    debugOpen--;
}
const debugClose = source.indexOf('</script>', debugIdx) + 9;
const debugScript = source.substring(debugOpen, debugClose);

console.log('Styles extracted:', premiumStyles.length, 'chars');
console.log('Meta bar extracted:', metaBarContent.length, 'chars');
console.log('Lang toggle script:', langToggleScript.length, 'chars');
console.log('Failsafe script:', failsafeScript.length, 'chars');
console.log('Debug script:', debugScript.length, 'chars');

// Now read the current master template
let master = fs.readFileSync(templatePath, 'utf8');

// 1. Replace the premium styles section in PAGE_TEMPLATE
// Find the existing style block in PAGE_TEMPLATE
const pageTemplateStart = master.indexOf('const PAGE_TEMPLATE = `');
const pageTemplateContentStart = master.indexOf('<style>', pageTemplateStart);
const pageTemplateContentEnd = master.indexOf('</style>', pageTemplateContentStart) + 8;

// Replace existing styles with premium ones
const oldStyleBlock = master.substring(pageTemplateContentStart, pageTemplateContentEnd);
master = master.replace(oldStyleBlock, premiumStyles);
console.log('✓ Replaced style block');

// 2. Add language toggle buttons to the topic-meta-bar
// Find the meta bar in PAGE_TEMPLATE
const metaBarInTemplate = master.indexOf('<div class="topic-meta-bar">', pageTemplateStart);
const metaBarEndInTemplate = master.indexOf('</div>', metaBarInTemplate) + 6;

// Replace the meta bar content with the improved one
// First check what the existing meta bar looks like
const existingMetaBar = master.substring(metaBarInTemplate, metaBarEndInTemplate);
console.log('Existing meta bar:', existingMetaBar.substring(0, 100) + '...');

// The existing meta bar uses placeholders like [DIFFICULTY]. We need to keep those
// but add language toggle. Let's build the new meta bar
const newMetaBar = `<div class="topic-meta-bar">
                <span class="topic-difficulty [DIFFICULTY_CLASS]">
                    <i class="fas fa-signal"></i>
                    <span class="lang-en">[DIFFICULTY_LABEL]</span>
                    <span class="lang-hi">[DIFFICULTY_LABEL_HI]</span>
                </span>
                <span class="topic-study-time">
                    <i class="fas fa-clock"></i>
                    <span class="lang-en">[STUDY_TIME_LABEL]</span>
                    <span class="lang-hi">[STUDY_TIME_LABEL_HI]</span>
                </span>
                <div class="lang-toggle">
                    <button id="langEn" class="active" aria-pressed="true">EN</button>
                    <button id="langHi" aria-pressed="false">हिन्दी</button>
                </div>
            </div>`;

master = master.replace(existingMetaBar, newMetaBar);
console.log('✓ Replaced meta bar with language toggle');

// 3. Replace the footer scripts section - find the renderer scripts area
// The existing PAGE_TEMPLATE should have upsc-renderer.js references
// Find the last script tag before the end of the page template
const pageTemplateEnd = master.indexOf('`', pageTemplateStart + 'const PAGE_TEMPLATE = `'.length);
const pageTemplateBody = master.substring(pageTemplateStart, pageTemplateEnd);

// Replace everything from "<!-- Reusable renderers -->" onwards with the full footer
// First check if it exists
const rendererSectionIdx = pageTemplateBody.indexOf('<!-- Reusable renderers -->');
if (rendererSectionIdx !== -1) {
    const beforeRenderer = pageTemplateBody.substring(0, rendererSectionIdx);
    const newPageTemplate = beforeRenderer + footerSection;
    master = master.replace(pageTemplateBody, newPageTemplate);
    console.log('✓ Replaced footer section (from Reusable renderers)');
} else {
    console.log('⚠ Could not find "Reusable renderers" section in PAGE_TEMPLATE');
    // Find the end of PAGE_TEMPLATE - the closing backtick
    const lastNewline = pageTemplateBody.lastIndexOf('\n');
    const beforeEnd = pageTemplateBody.substring(0, lastNewline);
    const newPageTemplate = beforeEnd + '\n' + footerSection;
    master = master.replace(pageTemplateBody, newPageTemplate);
    console.log('✓ Appended footer section');
}

fs.writeFileSync(templatePath, master);
console.log('\n✓ Master template updated successfully!');